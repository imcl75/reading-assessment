/* "Print marking sheets" + "Import scanned papers" for the comprehension tool.
   Inlined into comprehension/index.html by build.py (the SCAN_MARKING placeholder in template.html).
   Reuses SaveResults' authed /_api call, uuid and date helpers — see save_results.js — and its same
   dark-until-proven gate (?results=on). The teacher marks a printed sheet by colouring in a circle per
   question (0..max), scans the stack, and Claude reads which circle was coloured — never the pupil's
   handwritten answer itself. Nothing about the scan is stored anywhere; only the confirmed marks are,
   via the normal /readingresults-db save, once the teacher has checked them here. */
const ScanMarking = (function(){
  let cfg = null, roster = null, card = null, rows = [];
  const $q = id => document.getElementById(id);
  const h = s => String(s == null ? '' : s).replace(/[&<>"]/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));
  const norm = s => String(s || '').normalize('NFC').toLowerCase().replace(/[-–—_']/g, ' ').replace(/[^a-z0-9 ]/g, '').replace(/ +/g, ' ').trim();

  const css = '#scanCard .row{display:flex;flex-wrap:wrap;gap:10px;align-items:center;margin:8px 0}'
    + '#scanCard select,#scanCard input[type=file]{font-size:16px;padding:8px;border:1px solid #c9d3dc;border-radius:8px;background:#fff}'
    + '#scanCard .hint{font-size:.85rem;color:#4b5563;margin:4px 0 10px}'
    + '#scanCard table.rev{width:100%;border-collapse:collapse;margin-top:10px;font-size:.85rem}'
    + '#scanCard table.rev th,#scanCard table.rev td{border:1px solid #dbe4ec;padding:6px 8px;text-align:left;vertical-align:top}'
    + '#scanCard .qm{display:inline-flex;gap:3px;margin:2px 4px 2px 0}'
    + '#scanCard .qm button{width:24px;height:24px;border-radius:50%;border:1.5px solid #c9d3dc;background:#fff;font-size:.75rem;font-weight:700;cursor:pointer;padding:0}'
    + '#scanCard .qm button.on{background:var(--dark,#0a0101);color:#fff;border-color:var(--dark,#0a0101)}'
    + '#scanCard .qm button.unclear{border-color:#b9770e;box-shadow:0 0 0 2px #f2d27a55}'
    + '#scanCard .rtotal{font-weight:700}'
    + '#scanCard .badrow{background:#fff7e0}'
    + '#scanCard .st{margin:8px 0;font-weight:700}#scanCard .st.ok{color:#146c2e}#scanCard .st.bad{color:#b3261e}'
    + '.scansheet{width:420px}.scansheet .qrow{border-top:1px solid var(--line,#cfe3ee);padding:6px 0;display:flex;justify-content:space-between;align-items:center}'
    + '.scansheet .circ{display:inline-flex;gap:6px}.scansheet .circ span{display:inline-flex;align-items:center;justify-content:center;width:22px;height:22px;border:1.5px solid #000;border-radius:50%;font-size:.75rem}';

  function build(){
    const st = document.createElement('style'); st.textContent = css; document.head.appendChild(st);
    card = document.createElement('section'); card.className = 'card'; card.id = 'scanCard';
    card.innerHTML = '<h2>Print &amp; scan marking sheets</h2>'
      + '<p class="hint">A compact sheet per pupil for this test: their name, and a row of circles per question. Colour in the ONE circle that shows the mark each question earned, with a highlighter. Scan the stack, upload it below, and check the readings before saving.</p>'
      + '<div class="row"><label for="scClass">Class</label><select id="scClass"><option value="">Loading classes…</option></select>'
      + '<button class="act alt" id="scPrint" disabled>Print marking sheets for this class</button></div>'
      + '<div class="row"><label for="scFile">Scanned file (PDF, or a single photo)</label><input type="file" id="scFile" accept="application/pdf,image/*">'
      + '<button class="act" id="scRead" disabled>Read scan</button></div>'
      + '<p class="st" id="scStatus"></p><div id="scReview"></div>'
      + '<div class="row" id="scSaveRow" hidden><button class="act" id="scSaveAll">Save all checked rows</button></div>';
    (document.querySelector('main') || document.body).appendChild(card);
    $q('scPrint').onclick = printSheets;
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
    const names = Object.keys(roster).sort();
    $q('scClass').innerHTML = '<option value="">Choose a class</option>' + names.map(n => '<option value="'+h(n)+'">'+h(n)+'</option>').join('');
    $q('scClass').onchange = () => { $q('scPrint').disabled = !$q('scClass').value; };
  }

  // ---- Print ----
  function printSheets(){
    const t = cfg.getTest(), meta = cfg.getMeta(), cls = $q('scClass').value, pupils = (roster[cls] || []);
    if (!pupils.length) return;
    document.querySelectorAll('.scansheet').forEach(e => e.remove());
    document.querySelectorAll('.sheet.active').forEach(e => e.classList.remove('active'));
    const holder = document.getElementById('sheets') || document.body;
    pupils.forEach(p => {
      const sec = document.createElement('section');
      sec.className = 'sheet scansheet active';
      sec.innerHTML = '<div class="head"><h1>'+h(p.first+' '+p.last)+'</h1><small>'+h(cls)+' &middot; '+h(meta.title)+' &middot; Marking sheet</small></div>'
        + '<p class="hint" style="margin:2px 0 8px">Colour in ONE circle per row with a highlighter. Marked the wrong one? Scribble solidly over it in pen, then colour the right one.</p>'
        + t.qs.map((q,i)=>'<div class="qrow"><b>Q'+(i+1)+'</b><span class="circ">'+
            Array.from({length:q.m+1},(_,v)=>'<span>'+v+'</span>').join('')+'</span></div>').join('')
        + '<div class="foot"><span>Wallscourt Farm Academy</span><span>Colour in one circle per row</span></div>';
      holder.appendChild(sec);
    });
    window.print();
    document.querySelectorAll('.scansheet').forEach(e => e.remove());
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
    const cls = $q('scClass').value;
    const row = {id: SaveResults.uuid(), page: ev.page, name: ev.name, upn: matchPupil(ev.name, cls),
                 marks: t.qs.map((q,i) => ev.marks[String(i+1)]), saved: false};
    rows.push(row);
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
          + '<td>' + (r.page+1) + '</td>'
          + '<td><select class="rpupil"' + (r.saved?' disabled':'') + '><option value="">' + (r.upn ? '' : 'Not matched — choose') + '</option>' + pupilOpts + '</select>'
          + (r.name ? '<div class="hint">read as: ' + h(r.name) + '</div>' : '') + '</td>'
          + '<td>' + t.qs.map((q,qi) => '<span class="qm" data-q="'+qi+'">' +
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
    if (!row.upn) { status('Page ' + (row.page+1) + ': choose which pupil this is before saving.', false); return; }
    if (!rowMarksComplete(row)) { status('Page ' + (row.page+1) + ': one or more marks could not be read — tap the missing ones before saving.', false); return; }
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

  return { init(c){ cfg = c; if (SaveResults.isOn()) build(); } };
})();
