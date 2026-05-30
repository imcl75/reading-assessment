/**
 * Reading Assessment Backend — Google Apps Script
 * ================================================
 * SETUP INSTRUCTIONS:
 *
 * The Google Sheet has already been created for you:
 * https://docs.google.com/spreadsheets/d/13h2sUXYMUPjoe1OlUzAuOpGvstPg2lQfTlvqJopTT5w/edit
 *
 * 1. Open the sheet above, go to Extensions → Apps Script.
 *    Delete any existing code and paste this entire file in. Save (Ctrl+S).
 *
 * 2. Set your Anthropic API key:
 *    In Apps Script: Project Settings (⚙️) → Script Properties → Add:
 *      ANTHROPIC_KEY  → your Anthropic API key (sk-ant-...)
 *    (Find yours at https://console.anthropic.com/settings/keys)
 *
 * 3. Deploy the script:
 *    Click Deploy → New Deployment → Type: Web App
 *    Execute as: Me
 *    Who has access: Anyone
 *    Click Deploy, copy the Web App URL.
 *
 * 4. Paste the Web App URL into index.html where it says BACKEND_URL = ''
 *    Then commit and push.
 *
 * The script creates two sheets automatically:
 *   "Results"  — one row per pupil, all question scores and answers
 *   "AI Marks" — Claude's mark and reasoning for each extended question
 */

// ── Sheet tab names ──────────────────────────────────────────────────────────
const RESULTS_SHEET  = 'Results';
const AI_MARKS_SHEET = 'AI Marks';

// All question IDs in order (for consistent column layout)
const ALL_QIDS = [
  '1','2','3','4','5','6','7','8','9','10','11','12','13a','13b',
  '14','15','16','17','18','19','20','21','22',
  '23','24','25','26','27','28','29','30','31','32a','32b'
];

// Type b questions that need AI marking (with guidance)
const TYPE_B_QUESTIONS = {
  'Q6':  { question: 'What are the benefits of booking a private party? Give two.', max: 2,
            guidance: 'Award 1 mark per benefit (max 2). Accept any reasonable paraphrase of: exclusive pool use / pool to yourselves; floats and water toys included; party tea/food provided. Do not accept vague answers without reference to a specific benefit.' },
  'Q9':  { question: 'How does the centre make sure that people are safe?', max: 1,
            guidance: 'Award 1 mark for reference to lifeguards / poolside lifeguards / responsible adults supervising. Accept reasonable paraphrase. Do not accept simply "they are safe" without explaining the mechanism.' },
  'Q17': { question: 'In verse two, where would you find the mouse peeping?', max: 1,
            guidance: 'Award 1 mark for reference to the tree roots / round about the tall tree roots / around the tree roots. Accept reasonable paraphrase that conveys the correct location.' },
  'Q20': { question: 'Find and copy a group of words which show that it has been hard work for the farmer to stack the grain.', max: 1,
            guidance: 'Award 1 mark for any phrase that conveys difficulty/effort in stacking the grain, e.g. "stacked with so much pain" or "with so much pain". Accept partial copies that retain the core meaning of effort/difficulty.' },
  'Q23': { question: 'Why was it easy for the pigeon to find food?', max: 1,
            guidance: 'Award 1 mark for reference to humans/people littering or leaving food on the ground. Accept any reasonable paraphrase e.g. "people dropped food", "humans left scraps".' },
  'Q25': { question: 'How can you tell that the pigeon is anxious when he first sees the eagle?', max: 1,
            guidance: 'Award 1 mark for reference to the pigeon being alarmed / fluttering upwards / panicking / clumsy panic. Accept any answer that conveys a clear sign of anxiety from the text.' },
};

// Type c question IDs (already extended/review in the frontend)
const TYPE_C_QIDS = ['Q13b', 'Q18', 'Q22', 'Q32b'];

// ── Entry point (POST) ───────────────────────────────────────────────────────
function doPost(e) {
  try {
    const data = JSON.parse(e.postData.contents);
    const ss = SpreadsheetApp.openById(
      '13h2sUXYMUPjoe1OlUzAuOpGvstPg2lQfTlvqJopTT5w'
    );

    // Save raw assessment data only — Claude marking triggered separately via admin
    saveResults(ss, data);

    return ContentService
      .createTextOutput(JSON.stringify({ ok: true }))
      .setMimeType(ContentService.MimeType.JSON);

  } catch (err) {
    console.error(err);
    return ContentService
      .createTextOutput(JSON.stringify({ ok: false, error: err.toString() }))
      .setMimeType(ContentService.MimeType.JSON);
  }
}

// ── Entry point (GET) ────────────────────────────────────────────────────────
function doGet(e) {
  const action   = (e && e.parameter && e.parameter.action)   || 'results';
  const callback = (e && e.parameter && e.parameter.callback) || null;
  const ss = SpreadsheetApp.openById('13h2sUXYMUPjoe1OlUzAuOpGvstPg2lQfTlvqJopTT5w');

  let result;
  if (action === 'results') {
    result = getSubmissionsSummary(ss);
  } else if (action === 'mark') {
    result = markAllPending(ss);
  } else {
    result = { error: 'unknown action' };
  }
  return jsonResponse(result, callback);
}

function jsonResponse(obj, callback) {
  const json = JSON.stringify(obj);
  if (callback) {
    // JSONP — bypasses browser CORS restrictions
    return ContentService
      .createTextOutput(callback + '(' + json + ')')
      .setMimeType(ContentService.MimeType.JAVASCRIPT);
  }
  return ContentService
    .createTextOutput(json)
    .setMimeType(ContentService.MimeType.JSON);
}

// ── Get submissions summary ──────────────────────────────────────────────────
function getSubmissionsSummary(ss) {
  const sheet = ss.getSheetByName(RESULTS_SHEET);
  if (!sheet) return [];

  const data = sheet.getDataRange().getValues();
  if (data.length <= 1) return [];

  const headers = data[0];

  // Find "Assessment ID" column if present
  const assessmentIdCol = headers.indexOf('Assessment ID');

  // Determine if a row has any AI scores by checking AI Score columns
  // (columns named like "Q13b Score" etc that have a numeric value AND were set by AI)
  // We use the AI Marks sheet presence to determine status
  const aiMarksSheet = ss.getSheetByName(AI_MARKS_SHEET);
  const markedPupils = new Set();
  if (aiMarksSheet) {
    const aiData = aiMarksSheet.getDataRange().getValues();
    for (let i = 1; i < aiData.length; i++) {
      // col 0 = Pupil, col 1 = Date, col 2 = Question, col 3 = AI Score
      if (aiData[i][3] !== '' && aiData[i][3] !== null && aiData[i][3] !== '?') {
        markedPupils.add(aiData[i][0] + '|' + aiData[i][1]);
      }
    }
  }

  const submissions = [];
  for (let i = 1; i < data.length; i++) {
    const row = data[i];
    const timestamp = row[0];
    const pupil     = row[1];
    const date      = row[2];
    const timeTaken = row[3];
    const sections  = row[4];
    const autoScore = row[5];
    const totalMax  = row[6];
    const assessmentId = assessmentIdCol >= 0 ? row[assessmentIdCol] : '';

    // Check aiStatus: look for any numeric value in the AI Score columns
    // that would have been written by updateResultsWithAIScores
    let hasAIScore = false;
    // Check Q13b, Q18, Q22, Q32b, Q6, Q9, Q17, Q20, Q23, Q25 score columns
    const reviewQids = ['13b','18','22','32b','6','9','17','20','23','25'];
    reviewQids.forEach(qid => {
      const colHeader = 'Q' + qid + ' Score';
      const colIdx = headers.indexOf(colHeader);
      if (colIdx >= 0) {
        const val = row[colIdx];
        if (typeof val === 'number') hasAIScore = true;
      }
    });

    // Also check via AI Marks sheet
    const dateStr = date instanceof Date ? date.toLocaleDateString('en-GB') : String(date);
    if (markedPupils.has(pupil + '|' + dateStr)) hasAIScore = true;

    let tsStr = '';
    if (timestamp instanceof Date) {
      tsStr = timestamp.toISOString();
    } else {
      tsStr = String(timestamp);
    }

    submissions.push({
      row: i + 1,
      pupil: pupil || '',
      date: dateStr,
      timestamp: tsStr,
      timeTaken: String(timeTaken || ''),
      sections: String(sections || ''),
      assessmentId: String(assessmentId || ''),
      autoScore: autoScore || 0,
      totalMax: totalMax || 0,
      aiStatus: hasAIScore ? 'marked' : 'pending'
    });
  }

  return submissions;
}

// ── Mark all pending submissions ─────────────────────────────────────────────
function markAllPending(ss) {
  const sheet = ss.getSheetByName(RESULTS_SHEET);
  if (!sheet) return { ok: false, error: 'No Results sheet found' };

  const data = sheet.getDataRange().getValues();
  if (data.length <= 1) return { ok: true, marked: 0, results: [] };

  const headers = data[0];
  const summary = getSubmissionsSummary(ss);
  const pending = summary.filter(s => s.aiStatus === 'pending');

  if (pending.length === 0) return { ok: true, marked: 0, results: [] };

  const allResults = [];

  pending.forEach(sub => {
    const rowIdx = sub.row - 1; // 0-based
    const rowData = data[rowIdx];

    // Reconstruct answers object from row data
    // Columns: 0=Timestamp,1=Pupil,2=Date,3=Time Taken,4=Sections,5=Auto Score,6=Total Marks,7=Percentage
    // Then from col 8 onwards: possibly Assessment ID col, then pairs of [Q{id} Score, Q{id} Answer]
    // We find each answer by locating the "Q{id} Answer" column header
    const answers = {};
    ALL_QIDS.forEach(qid => {
      const ansColHeader = 'Q' + qid + ' Answer';
      const ansColIdx = headers.indexOf(ansColHeader);
      if (ansColIdx >= 0) {
        answers['Q' + qid] = String(rowData[ansColIdx] || '');
      }
    });

    // Build review questions list: type b + type c
    const reviewQuestions = [];

    // Type b questions
    Object.entries(TYPE_B_QUESTIONS).forEach(([qid, info]) => {
      reviewQuestions.push({
        id: qid.replace('Q', ''),
        qid: qid,
        question: info.question,
        guidance: info.guidance,
        max: info.max,
        prompt: ''
      });
    });

    // Type c questions — get guidance from the data payload if present,
    // or use hardcoded guidance below
    const TYPE_C_GUIDANCE = {
      'Q13b': { question: 'Explain your answer to question 13 using evidence from the text.', max: 1,
                guidance: 'Award 1 mark for reference to any of: information parents need (times/prices/safety/booking); parents would book a party; text is persuading parents to bring their children. Do not accept generic answers without text evidence.' },
      'Q18':  { question: "What impression does the word 'nibbling' give you about how the mouse eats?", max: 1,
                guidance: 'Award 1 mark for any answer suggesting the mouse eats gently / delicately / carefully / in small bites / slowly / quietly / daintily. Do not accept answers that simply repeat "it nibbles" without conveying an impression of how it eats.' },
      'Q22':  { question: 'How do you think the poet feels about field mice? Use evidence from the whole text to support your answer.', max: 2,
                guidance: 'Award 2 marks for: a clear statement of the poet\'s feelings (fond/caring/protective/affectionate) WITH supporting evidence from the poem. Award 1 mark for: feeling stated without evidence OR evidence given without a clear statement of feeling.' },
      'Q32b': { question: 'Explain your answer to question 32.', max: 1,
                guidance: 'Award 1 mark for: reference to evidence that shows the pigeon is wise/clever/calm, e.g. "not in the slightest bit flustered", uses logic/reason rather than force, points out the eagle\'s chain, speech about sticking together and being smart.' },
    };

    Object.entries(TYPE_C_GUIDANCE).forEach(([qid, info]) => {
      reviewQuestions.push({
        id: qid.replace('Q', ''),
        qid: qid,
        question: info.question,
        guidance: info.guidance,
        max: info.max,
        prompt: ''
      });
    });

    // Call Claude for each question
    const rowData2 = { pupilName: sub.pupil, date: sub.date, answers, reviewQuestions };
    const aiMarks = markWithClaude(rowData2);

    // Save AI marks
    saveAIMarks(ss, rowData2, aiMarks);

    // Update Results sheet with AI scores
    updateResultsWithAIScores(ss, sub.pupil, sub.date, aiMarks);

    allResults.push({
      pupil: sub.pupil,
      date: sub.date,
      marks: aiMarks
    });
  });

  return { ok: true, marked: pending.length, results: allResults };
}

// ── Save raw submission ──────────────────────────────────────────────────────
function saveResults(ss, data) {
  let sheet = ss.getSheetByName(RESULTS_SHEET);
  if (!sheet) {
    sheet = ss.insertSheet(RESULTS_SHEET);
    const headers = [
      'Timestamp', 'Pupil', 'Date', 'Time Taken', 'Sections Completed',
      'Auto Score', 'Total Marks', 'Percentage', 'Assessment ID'
    ];
    ALL_QIDS.forEach(qid => {
      headers.push('Q' + qid + ' Score', 'Q' + qid + ' Answer');
    });
    sheet.getRange(1, 1, 1, headers.length).setValues([headers]);
    sheet.getRange(1, 1, 1, headers.length).setFontWeight('bold');
    sheet.setFrozenRows(1);
  } else {
    // Migrate: insert Assessment ID column after Percentage if not already present
    const existingHeaders = sheet.getRange(1, 1, 1, sheet.getLastColumn()).getValues()[0];
    if (existingHeaders.indexOf('Assessment ID') < 0) {
      const pctIdx = existingHeaders.indexOf('Percentage');
      if (pctIdx >= 0) {
        sheet.insertColumnAfter(pctIdx + 1);
        const newCol = pctIdx + 2; // 1-based
        sheet.getRange(1, newCol).setValue('Assessment ID').setFontWeight('bold');
      }
    }
  }

  const sectionNames = { 0: 'Making Waves', 1: 'The Field Mouse', 2: 'Food Chain' };
  const sectionsStr = (data.sections || [0,1,2]).map(s => sectionNames[s] || s).join(', ');
  const pct = data.totalMax ? Math.round(data.total / data.totalMax * 100) + '%' : '-';

  const row = [
    new Date().toISOString(),
    data.pupilName,
    data.date || new Date().toLocaleDateString('en-GB'),
    data.timeTaken || '',
    sectionsStr,
    data.total,
    data.totalMax,
    pct,
    data.assessmentId || ''
  ];

  ALL_QIDS.forEach(qid => {
    const sc = data.scores ? data.scores['Q' + qid] : null;
    row.push(sc ? (sc.score !== null && sc.score !== undefined ? sc.score : 'pending') : '-');
    row.push(data.answers ? (data.answers['Q' + qid] || '') : '');
  });

  sheet.appendRow(row);
}

// ── Update AI scores into Results sheet ─────────────────────────────────────
function updateResultsWithAIScores(ss, pupilName, date, aiMarks) {
  if (!Object.keys(aiMarks).length) return;
  const sheet = ss.getSheetByName(RESULTS_SHEET);
  if (!sheet) return;

  // Find the pupil's row (last row matching name)
  const data = sheet.getDataRange().getValues();
  let targetRow = -1;
  for (let i = data.length - 1; i >= 1; i--) {
    if (data[i][1] === pupilName) { targetRow = i + 1; break; }
  }
  if (targetRow < 0) return;

  // Find column index for each question's score
  const headers = data[0];
  Object.entries(aiMarks).forEach(([qid, mark]) => {
    const colHeader = qid + ' Score';
    const colIdx = headers.indexOf(colHeader);
    if (colIdx >= 0 && mark.score !== null) {
      sheet.getRange(targetRow, colIdx + 1).setValue(mark.score);
    }
  });
}

// ── Save AI marks detail ─────────────────────────────────────────────────────
function saveAIMarks(ss, data, aiMarks) {
  if (!Object.keys(aiMarks).length) return;

  let sheet = ss.getSheetByName(AI_MARKS_SHEET);
  if (!sheet) {
    sheet = ss.insertSheet(AI_MARKS_SHEET);
    sheet.getRange(1, 1, 1, 8).setValues([
      ['Pupil', 'Date', 'Question', 'AI Score', 'Max Marks', 'Confidence', 'AI Reasoning', 'Answer']
    ]);
    sheet.getRange(1, 1, 1, 8).setFontWeight('bold');
    sheet.setFrozenRows(1);
    sheet.setColumnWidth(7, 500);
  }

  const date = data.date || new Date().toLocaleDateString('en-GB');
  Object.entries(aiMarks).forEach(([qid, mark]) => {
    sheet.appendRow([
      data.pupilName, date, qid,
      mark.score !== null ? mark.score : '?',
      mark.max,
      mark.confidence || '',
      mark.reasoning || '',
      (data.answers || {})['Q' + qid.replace('Q','').replace('q','')] || (data.answers || {})[qid] || ''
    ]);
  });
}

// ── Claude marking ───────────────────────────────────────────────────────────
function markWithClaude(data) {
  const apiKey = PropertiesService.getScriptProperties().getProperty('ANTHROPIC_KEY');
  if (!apiKey) {
    console.warn('No ANTHROPIC_KEY set — skipping AI marking');
    return {};
  }

  const reviewQuestions = data.reviewQuestions || [];
  const results = {};

  reviewQuestions.forEach(rq => {
    const answer = (data.answers || {})['Q' + rq.id] || (data.answers || {})[rq.qid] || '';

    if (!answer.trim()) {
      results['Q' + rq.id] = {
        score: 0, max: rq.max, confidence: 'high',
        reasoning: 'No answer given — awarded 0.'
      };
      return;
    }

    const prompt = buildMarkingPrompt(rq, answer);

    try {
      const response = UrlFetchApp.fetch('https://api.anthropic.com/v1/messages', {
        method: 'post',
        headers: {
          'Content-Type': 'application/json',
          'x-api-key': apiKey,
          'anthropic-version': '2023-06-01'
        },
        payload: JSON.stringify({
          model: 'claude-opus-4-5',
          max_tokens: 300,
          messages: [{ role: 'user', content: prompt }]
        }),
        muteHttpExceptions: true
      });

      const body = JSON.parse(response.getContentText());
      if (body.content && body.content[0] && body.content[0].text) {
        // Extract the JSON from Claude's response
        const text = body.content[0].text.trim();
        const jsonMatch = text.match(/\{[\s\S]*\}/);
        if (jsonMatch) {
          const mark = JSON.parse(jsonMatch[0]);
          // Clamp score to valid range
          mark.score = Math.max(0, Math.min(rq.max, Math.round(mark.score)));
          results['Q' + rq.id] = mark;
        }
      }
    } catch (err) {
      console.error('Claude error for Q' + rq.id + ':', err);
      results['Q' + rq.id] = {
        score: null, max: rq.max, confidence: 'low',
        reasoning: 'AI marking error — please review manually.'
      };
    }
  });

  return results;
}

function buildMarkingPrompt(rq, answer) {
  return `You are marking a Year 4 (age 8-9) reading comprehension assessment for a UK primary school.

Question ${rq.id} — worth ${rq.max} mark${rq.max > 1 ? 's' : ''}.
${rq.prompt ? 'Question context: ' + rq.prompt.replace(/<[^>]+>/g, '') + '\n' : ''}Question: ${rq.question.replace(/<[^>]+>/g, '')}

Official marking guidance:
${rq.guidance}

Pupil's answer: "${answer}"

Apply the marking guidance strictly. Consider that this is a 8-9 year old child — accept answers that demonstrate the correct understanding even if they are brief or not perfectly worded.

Set confidence to 'high' if the answer clearly matches or clearly does not match the guidance. Set 'medium' if you had to use judgement. Set 'low' if the answer is ambiguous or you are uncertain about the mark.

Respond with ONLY a JSON object, nothing else:
{"score": <integer 0–${rq.max}>, "max": ${rq.max}, "confidence": "high"|"medium"|"low", "reasoning": "<one clear sentence explaining your marking decision>"}`;
}
