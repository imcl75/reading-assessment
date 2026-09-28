/* "Print marking sheets" + "Import scanned papers" for the comprehension tool.
   Inlined into comprehension/index.html by build.py (the SCAN_MARKING placeholder in template.html).
   Reuses SaveResults' authed /_api call, uuid and date helpers — see save_results.js — and its same
   dark-until-proven gate (?results=on). The teacher marks a printed sheet by colouring in a circle per
   question (0..max), scans the stack, and Claude reads which circle was coloured — never the pupil's
   handwritten answer itself. Nothing about the scan is stored anywhere; only the confirmed marks are,
   via the normal /readingresults-db save, once the teacher has checked them here. */
const ScanMarking = (function(){
  let cfg = null, roster = null, card = null, rows = [], tableCache = {}, historyCache = {};
  const $q = id => document.getElementById(id);
  const h = s => String(s == null ? '' : s).replace(/[&<>"]/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));
  const norm = s => String(s || '').normalize('NFC').toLowerCase().replace(/[-–—_']/g, ' ').replace(/[^a-z0-9 ]/g, '').replace(/ +/g, ' ').trim();
  // "Save as PDF" takes its default filename from document.title — the static <title> tag left
  // every save as the generic "Reading Comprehension by Level" regardless of what was actually
  // printed (Innes, 28.09.26). Set it just for the print, then put it back.
  function printWithTitle(name, fn){
    const old = document.title;
    document.title = name;
    try { fn(); } finally { document.title = old; }
  }

  const css = '#scanCard .row{display:flex;flex-wrap:wrap;gap:10px;align-items:center;margin:8px 0}'
    + '#scanCard select,#scanCard input[type=file]{font-size:16px;padding:8px;border:1px solid #c9d3dc;border-radius:8px;background:#fff}'
    + '#scanCard .hint{font-size:.85rem;color:#4b5563;margin:4px 0 10px}'
    + '#scanCard table.rev{width:100%;border-collapse:collapse;margin-top:10px;font-size:.85rem}'
    + '#scanCard table.rev th,#scanCard table.rev td{border:1px solid #dbe4ec;padding:6px 8px;text-align:left;vertical-align:top}'
    + '#scanCard .qm{display:inline-flex;align-items:center;gap:3px;margin:2px 10px 6px 0;padding-right:9px;border-right:1px solid #e5ebf1}'
    + '#scanCard .qm .qn{font-size:.75rem;color:#456;font-weight:700;margin-right:1px}'
    + '#scanCard .qm button{width:24px;height:24px;border-radius:50%;border:1.5px solid #c9d3dc;background:#fff;font-size:.75rem;font-weight:700;cursor:pointer;padding:0}'
    + '#scanCard .qm button.on{background:var(--dark,#0a0101);color:#fff;border-color:var(--dark,#0a0101)}'
    + '#scanCard .qm button.unclear{border-color:#b9770e;box-shadow:0 0 0 2px #f2d27a55}'
    + '#scanCard .rtotal{font-weight:700}'
    + '#scanCard .badrow{background:#fff7e0}'
    + '#scanCard .st{margin:8px 0;font-weight:700}#scanCard .st.ok{color:#146c2e}#scanCard .st.bad{color:#b3261e}'
    + '#scanCard .plist{display:flex;flex-wrap:wrap;gap:6px 14px;margin:6px 0 4px;max-height:160px;overflow-y:auto;padding:8px;border:1px solid #dbe4ec;border-radius:8px}'
    + '#scanCard .plist label{display:flex;align-items:center;gap:5px;font-size:.9rem;white-space:nowrap}'
    + '#scanCard .plink{background:none;border:0;color:#0a6fa8;text-decoration:underline;font:inherit;cursor:pointer;padding:0}';

  function build(){
    const st = document.createElement('style'); st.textContent = css; document.head.appendChild(st);
    card = document.createElement('section'); card.className = 'card'; card.id = 'scanCard';
    card.innerHTML = '<h2>Print &amp; scan marking sheets</h2>'
      + '<p class="hint">This is the sheet the children write their answers on — their name is pre-printed, one per pupil. After marking each question in the usual way, colour in the ONE circle under it that shows the mark it earned, with a highlighter. Marked the wrong one? Scribble solidly over it in pen, then colour the right one — a scribbled-out circle is read as not chosen. Scan the marked stack, upload it below, and check the readings before saving.</p>'
      + '<div class="row"><label for="scClass">Class</label><select id="scClass"><option value="">Loading classes…</option></select></div>'
      + '<div id="scPupilsWrap" hidden><p class="hint" style="margin:0 0 4px">Untick anyone sitting a different test at a different level — print and scan them separately, after choosing their level above. <button class="plink" id="scAll">Select all</button> &middot; <button class="plink" id="scNone">Select none</button></p>'
      + '<div class="plist" id="scPupils"></div></div>'
      + '<div class="row"><button class="act alt" id="scPrintTexts" disabled>Print texts for the ticked pupils</button>'
      + '<button class="act alt" id="scPrintAnswers" disabled>Print answer sheets for the ticked pupils</button></div>'
      + '<p class="hint" style="margin:2px 0 10px">Two separate print jobs — the texts and the answer sheets come out as their own documents, easier to print and staple separately. An answer sheet that runs to more than one page repeats the pupil’s name on every page.</p>'
      + '<p class="hint" id="scTextNote" style="margin:2px 0 10px"></p>'
      + '<div class="row"><label for="scFile">Scanned file (PDF, or a single photo)</label><input type="file" id="scFile" accept="application/pdf,image/*">'
      + '<button class="act" id="scRead" disabled>Read scan</button></div>'
      + '<p class="st" id="scStatus"></p><div id="scReview"></div>'
      + '<div class="row" id="scSaveRow" hidden><button class="act" id="scSaveAll">Save all checked rows</button></div>';
    (document.querySelector('main') || document.body).appendChild(card);
    $q('scPrintTexts').onclick = () => printSheets('buildPupilPassageHTML');
    $q('scPrintAnswers').onclick = () => printSheets('buildPupilAnswerHTML');
    $q('scAll').onclick = () => setAllTicked(true);
    $q('scNone').onclick = () => setAllTicked(false);
    $q('scPupils').addEventListener('change', e => { if (e.target.classList.contains('scpu')) reconcileText(); });
    $q('scFile').onchange = () => { $q('scRead').disabled = !$q('scFile').files.length; };
    $q('scRead').onclick = readScan;
    $q('scSaveAll').onclick = saveAll;
    loadRoster();
  }

  async function loadRoster(){
    const d = await SaveResults.call('GET', '/pupils');
    if (!d.pupils) { $q('scClass').innerHTML = '<option value="">Class lists unavailable</option>'; return; }
    roster = {};
    d.pupils.forEach(p => { const c = p.class || p.code || '?'; (roster[c] = roster[c] || []).push(p); });
    Object.values(roster).forEach(list => list.sort((a,b) => (a.last+a.first).localeCompare(b.last+b.first)));
    const names = Object.keys(roster).sort();
    $q('scClass').innerHTML = '<option value="">Choose a class</option>' + names.map(n => '<option value="'+h(n)+'">'+h(n)+'</option>').join('');
    $q('scClass').onchange = renderPupilList;
  }

  // Table (seating group) order — Innes, 28.09.26: "the spelling tool has a 'table order' function
  // which helps with handing out the papers". Pulled read-only from the spelling tools' own Class
  // Manager data (see reading_results_db.py's sibling spelling_class_table.py); a class with no table
  // data just falls back to name order, so this never blocks printing.
  async function loadTable(cls){
    if (tableCache[cls]) return tableCache[cls];
    const d = await SaveResults.call('GET', '/classtable/' + encodeURIComponent(cls));
    return (tableCache[cls] = (d && d.ok) ? (d.table || {}) : {});
  }

  // Text-history avoidance (Innes, 28.09.26): a re-test at the same level should default to a text
  // none of the ticked pupils have already done. One fetch per class (any attempt counts, voided or
  // not — a voided save still means the pupil saw that text), cached and filtered client-side by
  // level/test id, so ticking/unticking pupils or changing level doesn't need a fresh request each time.
  async function loadHistory(cls){
    if (historyCache[cls]) return historyCache[cls];
    const d = await SaveResults.call('GET', '/readingresults-db', {class: cls, tool: 'comprehension', include_voided: 1, limit: 2000});
    return (historyCache[cls] = (d && d.results) || []);
  }
  function setTextNote(msg, warn){
    const el = $q('scTextNote'); if (!el) return;
    el.textContent = msg || ''; el.style.color = warn ? 'var(--amber,#b9770e)' : '';
  }
  function reconcileText(){
    if (!card) return;
    const cls = $q('scClass').value;
    const ticked = [...$q('scPupils').querySelectorAll('.scpu:checked')].map(cb => cb.value);
    if (!cls || !ticked.length) { setTextNote(''); return; }
    const rows = historyCache[cls] || [];
    const meta = cfg.getMeta(), texts = cfg.listTexts();
    const seenBy = upn => new Set(rows.filter(r => r.upn === upn && String(r.level) === String(meta.level)).map(r => r.test_id));
    const doneAlready = i => ticked.some(upn => seenBy(upn).has(texts[i].id));
    const cur = cfg.getIndex();
    if (!doneAlready(cur)) { setTextNote(''); return; }
    const alt = texts.findIndex((t, i) => !doneAlready(i));
    if (alt !== -1) {
      const pool = roster[cls] || [];
      const offender = ticked.find(upn => seenBy(upn).has(texts[cur].id));
      const found = pool.find(p => p.upn === offender);
      const name = found ? (found.first + ' ' + found.last) : 'a ticked pupil';
      cfg.selectText(alt);
      setTextNote('Switched to "' + texts[alt].title + '" — ' + name + ' has already done "' + texts[cur].title + '" at this level.');
    } else {
      setTextNote('Everyone ticked has already done every text at this level. Untick some and print them separately, or accept a repeat.', true);
    }
  }
  function sortByTable(pool, table){
    return [...pool].sort((a, b) => {
      const ta = table[a.upn], tb = table[b.upn];
      if (ta && tb && ta !== tb) return ta.localeCompare(tb, undefined, {numeric: true});
      if (ta && !tb) return -1;
      if (tb && !ta) return 1;
      return (a.last + a.first).localeCompare(b.last + b.first);
    });
  }
  function renderPupilRows(pool, table){
    $q('scPupils').innerHTML = sortByTable(pool, table).map(p =>
      '<label><input type="checkbox" class="scpu" value="'+h(p.upn)+'" checked>'+h(p.first+' '+p.last)
      + (table[p.upn] ? ' <span style="color:#789">(Table '+h(table[p.upn])+')</span>' : '') + '</label>'
    ).join('');
  }
  async function renderPupilList(){
    const cls = $q('scClass').value, pool = roster[cls] || [];
    $q('scPupilsWrap').hidden = !cls;
    $q('scPrintTexts').disabled = $q('scPrintAnswers').disabled = !cls;
    setTextNote('');
    if (!cls) return;
    renderPupilRows(pool, {});   // show names immediately; re-render once table order has loaded
    const [table] = await Promise.all([loadTable(cls), loadHistory(cls)]);
    if ($q('scClass').value === cls) { renderPupilRows(pool, table); reconcileText(); }
  }
  function setAllTicked(on){ $q('scPupils').querySelectorAll('.scpu').forEach(cb => cb.checked = on); reconcileText(); }

  // ---- Print ----
  // Each pupil gets the SAME sheet they'd normally write their answers on (passage + questions), just with their
  // name pre-printed instead of a blank field, and a row of marking circles under each question — Innes, 28.09.26:
  // one sheet, written on by the child then marked and scanned by the teacher, not a separate marking-only sheet.
  // Only the TICKED pupils print, so a pupil sitting a different level's test can be left out here and done
  // separately (untick, pick their level above, tick just them, print again).
  let printedSheets = [];
  async function printSheets(builderName){
    const cls = $q('scClass').value;
    const ticked = new Set([...$q('scPupils').querySelectorAll('.scpu:checked')].map(cb => cb.value));
    const table = await loadTable(cls);
    const pupils = sortByTable(roster[cls] || [], table).filter(p => ticked.has(p.upn));
    if (!pupils.length) return;
    printedSheets.forEach(e => e.remove()); printedSheets = [];
    document.querySelectorAll('.sheet.active').forEach(e => e.classList.remove('active'));
    const holder = document.getElementById('sheets') || document.body;
    const html = pupils.map(p => cfg[builderName](p.first + ' ' + p.last, cls)).join('');
    const wrap = document.createElement('div');
    wrap.innerHTML = html;
    [...wrap.children].forEach(el => { holder.appendChild(el); printedSheets.push(el); });
    const meta = cfg.getMeta();
    const kind = builderName === 'buildPupilPassageHTML' ? 'Texts' : 'Answers';
    printWithTitle('Reading Comprehension - Level ' + meta.level + ' - ' + meta.title + ' - ' + kind, () => window.print());
    printedSheets.forEach(e => e.remove()); printedSheets = [];
  }

  // ---- Read scan ----
  function status(msg, ok){ const e = $q('scStatus'); e.textContent = msg || ''; e.className = 'st' + (ok === true ? ' ok' : ok === false ? ' bad' : ''); }

  async function readScan(){
    const file = $q('scFile').files[0]; if (!file) return;
    const t = cfg.getTest();
    const questions = t.qs.map((q,i) => ({n: i+1, max: q.m}));
    rows = []; $q('scReview').innerHTML = ''; $q('scSaveRow').hidden = true;
    status('Reading the scan… this can take a little while for a full class.');
    $q('scRead').disabled = true;
    const fd = new FormData(); fd.append('file', file); fd.append('questions', JSON.stringify(questions));
    let res;
    try {
      res = await fetch('/_api/planning/readingscan-db?token=__hub__', {method: 'POST', headers: {'X-WFA-Proxy': '1'}, body: fd});
    } catch(e) { status('Could not reach the school server. Check the wifi and try again.', false); $q('scRead').disabled = false; return; }
    if (res.status === 401) { status('Your staff sign-in has ended. Sign in again in another tab, then retry.', false); $q('scRead').disabled = false; return; }
    if (!res.ok || !res.body) { status('The school server did not answer properly.', false); $q('scRead').disabled = false; return; }
    const reader = res.body.getReader(), decoder = new TextDecoder(); let buf = '', total = null, seen = 0;
    while (true) {
      const {done, value} = await reader.read(); if (done) break;
      buf += decoder.decode(value, {stream: true});
      let idx;
      while ((idx = buf.indexOf('\n\n')) !== -1) {
        const chunk = buf.slice(0, idx); buf = buf.slice(idx + 2);
        if (!chunk.startsWith('data: ')) continue;
        let ev; try { ev = JSON.parse(chunk.slice(6)); } catch(e) { continue; }
        if (ev.type === 'total') { total = ev.total; status('Read 0 of ' + total + ' pages so far…'); }
        else if (ev.type === 'fatal') { status(ev.message, false); $q('scRead').disabled = false; return; }
        else if (ev.type === 'page') { addRow(ev, t); seen++; status('Read ' + seen + (total ? ' of ' + total : '') + ' pages so far…'); }
        else if (ev.type === 'error') { seen++; addFailedRow(ev); status('Read ' + seen + (total ? ' of ' + total : '') + ' pages so far…'); }
      }
    }
    status(seen ? ('Done: ' + seen + ' page' + (seen === 1 ? '' : 's') + ' read. Check the rows below, then save.') : 'Nothing was found in that file.', seen > 0);
    $q('scSaveRow').hidden = seen === 0;
    $q('scRead').disabled = false;
  }

  function matchPupil(name, cls){
    const pool = roster[cls] || []; const target = norm(name);
    if (!target) return '';
    let hit = pool.find(p => norm(p.first + ' ' + p.last) === target);
    if (!hit) { const toks = target.split(' '); hit = pool.find(p => toks.includes(norm(p.first)) && toks.includes(norm(p.last))); }
    return hit ? hit.upn : '';
  }

  function addFailedRow(ev){
    const div = document.createElement('div');
    div.className = 'badrow'; div.style.padding = '6px 8px'; div.style.marginTop = '6px'; div.style.borderRadius = '8px';
    div.textContent = 'Page ' + (ev.page + 1) + ': could not be read (' + ev.message + '). Mark that pupil by hand instead.';
    $q('scReview').appendChild(div);
  }

  function addRow(ev, t){
    // A question page can run to more than one physical page (see comprehension/template.html's
    // paginateQuestions) — every page repeats the pupil's name, and a page only ever shows circles
    // for the questions printed on it, so pages for the same pupil are merged into ONE row here
    // rather than becoming separate, partial results. Matched by the name as read, since that's
    // printed identically on every page of the same pupil's sheet.
    const cls = $q('scClass').value;
    const key = norm(ev.name);
    let row = key ? rows.find(r => r.nameKey === key && !r.saved) : null;
    if (!row) {
      row = {id: SaveResults.uuid(), pages: [], name: ev.name, nameKey: key, upn: matchPupil(ev.name, cls),
             marks: t.qs.map(() => null), saved: false};
      rows.push(row);
    }
    row.pages.push(ev.page);
    row.pages.sort((a, b) => a - b);   // pages of the same test are scanned concurrently and can complete
                                        // out of order (Innes, 28.09.26: saw "2, 1" instead of "1, 2") — the
                                        // marks merge is already order-independent, this just keeps the
                                        // displayed page list reading naturally
    t.qs.forEach((q, i) => {
      const v = ev.marks[String(i + 1)];
      if (v !== null && v !== undefined) row.marks[i] = v;
    });
    renderReview(t);
  }

  function rowMarksComplete(row){ return row.marks.every(m => m !== null && m !== undefined); }

  function renderReview(t){
    const pool = roster[$q('scClass').value] || [];
    const pupilOpts = pool.map(p => '<option value="'+h(p.upn)+'">'+h(p.first+' '+p.last)+'</option>').join('');
    $q('scReview').innerHTML = '<table class="rev"><tr><th>Page</th><th>Pupil</th><th>Marks</th><th>Total</th><th></th></tr>' +
      rows.map((r,ri) => {
        const score = r.marks.reduce((a,b)=>a+(b||0),0), max = t.qs.reduce((a,q)=>a+q.m,0);
        return '<tr data-row="'+ri+'"' + (r.saved ? ' style="opacity:.5"' : '') + '>'
          + '<td>' + r.pages.map(p=>p+1).join(', ') + '</td>'
          + '<td><select class="rpupil"' + (r.saved?' disabled':'') + '><option value="">' + (r.upn ? '' : 'Not matched — choose') + '</option>' + pupilOpts + '</select>'
          + (r.name ? '<div class="hint">read as: ' + h(r.name) + '</div>' : '') + '</td>'
          + '<td>' + t.qs.map((q,qi) => '<span class="qm" data-q="'+qi+'"><b class="qn">'+(qi+1)+')</b> ' +
              Array.from({length:q.m+1},(_,v)=>'<button data-v="'+v+'" class="'+(r.marks[qi]===v?'on':'')+(r.marks[qi]==null&&v===0?' unclear':'')+'"'+(r.saved?' disabled':'')+'>'+v+'</button>').join('') + '</span>').join('') + '</td>'
          + '<td class="rtotal">' + score + ' / ' + max + '</td>'
          + '<td>' + (r.saved ? 'Saved' : '<button class="act alt rsave">Save</button>') + '</td></tr>';
      }).join('') + '</table>';
    rows.forEach((r, ri) => {
      const tr = $q('scReview').querySelector('tr[data-row="'+ri+'"]'); if (!tr) return;
      const sel = tr.querySelector('.rpupil'); sel.value = r.upn; sel.onchange = () => { r.upn = sel.value; };
      tr.querySelectorAll('.qm').forEach(g => g.addEventListener('click', e => {
        const b = e.target.closest('button'); if (!b) return;
        r.marks[+g.dataset.q] = +b.dataset.v; renderReview(t);
      }));
      const saveBtn = tr.querySelector('.rsave'); if (saveBtn) saveBtn.onclick = () => saveRow(r, t);
    });
  }

  async function saveRow(row, t){
    if (!row.upn) { status('Page ' + row.pages.map(p=>p+1).join(', ') + ': choose which pupil this is before saving.', false); return; }
    if (!rowMarksComplete(row)) { status('Page ' + row.pages.map(p=>p+1).join(', ') + ': one or more marks could not be read — tap the missing ones before saving.', false); return; }
    const meta = cfg.getMeta(), total = t.qs.reduce((a,q)=>a+q.m,0);
    const body = {action: 'save', client_id: row.id, upn: row.upn, tool: 'comprehension', source: 'paper',
      taken_on: SaveResults.today(), test_id: meta.test_id, level: meta.level, marks: row.marks, total: total,
      domains: t.qs.map(q=>q.d), maxes: t.qs.map(q=>q.m)};
    const d = await SaveResults.call('POST', '/readingresults-db', {}, body);
    if (d.ok) { row.saved = true; status('Saved.', true); renderReview(t); }
    else status(d.error || 'Could not save that row.', false);
  }

  async function saveAll(){
    const t = cfg.getTest();
    for (const r of rows) if (!r.saved) await saveRow(r, t);
  }

  return {
    init(c){ cfg = c; if (SaveResults.isOn()) build(); },
    // Called by the host page when the level/text selection changes (steps 1-2), so a class
    // already ticked below gets re-checked against the newly chosen text — Innes, 28.09.26.
    onSelectionChanged(){ reconcileText(); },
  };
})();
