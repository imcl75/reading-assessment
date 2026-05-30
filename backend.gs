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

// ── Entry point ──────────────────────────────────────────────────────────────
function doPost(e) {
  try {
    const data = JSON.parse(e.postData.contents);
    const ss = SpreadsheetApp.openById(
      '13h2sUXYMUPjoe1OlUzAuOpGvstPg2lQfTlvqJopTT5w'
    );

    // 1. Save raw assessment data
    saveResults(ss, data);

    // 2. Mark extended questions with Claude (synchronous — takes ~5–10s)
    const aiMarks = markWithClaude(data);

    // 3. Save AI marks to separate sheet
    saveAIMarks(ss, data, aiMarks);

    // 4. Update the Results sheet with the AI scores
    updateResultsWithAIScores(ss, data.pupilName, data.date, aiMarks);

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

// ── Save raw submission ──────────────────────────────────────────────────────
function saveResults(ss, data) {
  let sheet = ss.getSheetByName(RESULTS_SHEET);
  if (!sheet) {
    sheet = ss.insertSheet(RESULTS_SHEET);
    const headers = [
      'Timestamp', 'Pupil', 'Date', 'Time Taken', 'Sections Completed',
      'Auto Score', 'Total Marks', 'Percentage'
    ];
    ALL_QIDS.forEach(qid => {
      headers.push('Q' + qid + ' Score', 'Q' + qid + ' Answer');
    });
    sheet.getRange(1, 1, 1, headers.length).setValues([headers]);
    sheet.getRange(1, 1, 1, headers.length).setFontWeight('bold');
    sheet.setFrozenRows(1);
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
    pct
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
    sheet.getRange(1, 1, 1, 6).setValues([
      ['Pupil', 'Date', 'Question', 'AI Score', 'Max Marks', 'AI Reasoning']
    ]);
    sheet.getRange(1, 1, 1, 6).setFontWeight('bold');
    sheet.setFrozenRows(1);
    sheet.setColumnWidth(6, 500);
  }

  const date = data.date || new Date().toLocaleDateString('en-GB');
  Object.entries(aiMarks).forEach(([qid, mark]) => {
    sheet.appendRow([
      data.pupilName, date, qid,
      mark.score !== null ? mark.score : '?',
      mark.max,
      mark.reasoning || ''
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
    const answer = (data.answers || {})['Q' + rq.id] || '';

    if (!answer.trim()) {
      results['Q' + rq.id] = {
        score: 0, max: rq.max,
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
        score: null, max: rq.max,
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

Respond with ONLY a JSON object, nothing else:
{"score": <integer 0–${rq.max}>, "max": ${rq.max}, "reasoning": "<one clear sentence explaining your marking decision>"}`;
}
