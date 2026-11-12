/* Save-to-pupil panel shared by the teacher tools (fluency, phonics, comprehension, PM benchmark).
   Inlined into each tool's index.html by its build.py (the SAVE_RESULTS placeholder in template.html).
   Talks to /_api/planning/... on this same site: a Cloudflare Worker checks the staff sign-in and adds the
   API token, so no token lives in this page.

   Flow (11.11.26): STEP 1 at the very top of the page = who you are assessing (class, pupil, term, date), with a
   sticky bar that keeps the chosen child in view while you assess. The bottom card only saves, and says plainly
   who it will save for. After a save, "Next pupil" clears the child and the marks so a result can't be saved twice
   or to the wrong child. A result saved to the wrong child / term / date can be moved afterwards (Move / Remove on
   the pupil's earlier results here, and on the Results page). A save that fails is kept on this device and shown at
   the top until it is saved. */
const SaveResults = (function(){
  const ON = true;
  const API = '/_api/planning', PENDING_KEY = 'ra_pending', CLASS_KEY = 'ra_last_class', PUPIL_KEY = 'ra_last_pupil';
  let cfg = null, roster = null, current = null, lastSaved = null, saving = false, card = null, topCard = null, bar = null;
  let attemptSig = '', attemptId = '', rosterLoading = null, shown = '';   // shown = the child the marks on screen belong to
  const $q = id => document.getElementById(id);
  const h = s => String(s == null ? '' : s).replace(/[&<>"]/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));
  const store = {
    get(k){ try { return localStorage.getItem(k); } catch(e){ return null; } },
    set(k,v){ try { localStorage.setItem(k, v); } catch(e){} },
    del(k){ try { localStorage.removeItem(k); } catch(e){} },
  };
  const uuid = () => (window.crypto && crypto.randomUUID) ? crypto.randomUUID() : 'ra-' + Date.now().toString(36) + Math.random().toString(36).slice(2, 12);
  const today = () => { const d = new Date(); return d.getFullYear() + '-' + String(d.getMonth()+1).padStart(2,'0') + '-' + String(d.getDate()).padStart(2,'0'); };
  const ukDate = iso => { const m = /^(\d{4})-(\d\d)-(\d\d)/.exec(iso || ''); if (!m) return iso || ''; return +m[3] + ' ' + ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'][+m[2]-1] + ' ' + m[1]; };

  const SIGNIN_MSG = 'Your staff sign-in has ended. Open this page in a new tab, sign in, then come back here and press Try again. Your result is kept on this device.';
  async function call(method, path, params, body){
    const qs = new URLSearchParams(Object.assign({token: '__hub__'}, params || {}));
    let res;
    try {
      res = await fetch(API + path + '?' + qs, {
        method, headers: Object.assign({'X-WFA-Proxy': '1'}, body ? {'Content-Type': 'application/json'} : {}),
        body: body ? JSON.stringify(body) : undefined, cache: 'no-store'});
    } catch(e){ return {error: 'Could not reach the school server. Check the wifi. Your result is kept on this device.', network: true}; }
    if (res.status === 401 || res.status === 403) return {error: SIGNIN_MSG, signin: true};
    let data = null;
    try { data = await res.json(); } catch(e){}
    if (!data) {
      // not JSON: a sign-in page from Cloudflare (HTML / redirected), or a server error page
      if (res.status < 500 && (res.redirected || /html/i.test(res.headers.get('content-type') || ''))) return {error: SIGNIN_MSG, signin: true};
      return {error: 'The school server had a problem (error ' + res.status + '). Your result is kept on this device: press Try again in a minute.', network: true, status: res.status};
    }
    return data;
  }

  const css = '#srStick{position:sticky;top:0;z-index:30;margin:-4px -4px 12px}'
    + '.srbar{display:flex;align-items:center;gap:10px;flex-wrap:wrap;padding:10px 14px;border-radius:10px;font-weight:700;font-size:1rem;box-shadow:0 2px 6px rgba(0,0,0,.15)}'
    + '.srbar.ok{background:#146c2e;color:#fff}.srbar.bad{background:#b3261e;color:#fff}'
    + '.srbar button{margin-left:auto;background:#fff;color:#0a0101;border:0;border-radius:8px;padding:6px 12px;font:inherit;font-size:.85rem;cursor:pointer}'
    + '.srPendBox .pend{background:#fff7e0;border:2px solid #e0a800;border-radius:10px;padding:10px 12px;margin-top:8px;color:#0a0101;font-weight:400;font-size:.9rem}'
    + '#srTop h2,#saveCard h2{margin-top:0}#srTop .hint{margin:0 0 8px;font-size:.9rem;color:#456}'
    + '.sr{display:grid;grid-template-columns:repeat(auto-fit,minmax(150px,1fr));gap:10px;margin:8px 0}'
    + '.sr>div{min-width:0}'
    + '#srTop label,#saveCard label,.srfix label{display:block;font-size:.8rem;font-weight:700;margin-bottom:3px}'
    + '#srTop select,#srTop input,.srfix select,.srfix input{width:100%;min-width:0;max-width:100%;box-sizing:border-box;font-size:16px;padding:9px;border:1px solid #c9d3dc;border-radius:8px;background:#fff}'
    + '#srWho{margin:8px 0 0;font-weight:700}#srWho.ok{color:#146c2e}#srWho.bad{color:#b3261e}'
    + '.srFor{font-size:1.1rem;margin:4px 0 10px}.srFor b{font-size:1.3rem}.srFor.bad{color:#b3261e;font-weight:700}'
    + '#saveCard .st,#srTop .st{margin:10px 0 4px;font-weight:700}.st.ok{color:#146c2e}.st.bad{color:#b3261e}'
    + '.hist{font-size:.85rem;color:#4b5563;margin:8px 0 0;padding-left:18px}.hist li{margin:4px 0}.hist .note{color:#8a5a00;font-size:.78rem}'
    + '.link{background:none;border:0;color:#0a6fa8;text-decoration:underline;font:inherit;cursor:pointer;padding:0 4px}'
    + '.srfix{background:#f1f8fc;border:1px solid #c9d3dc;border-radius:10px;padding:10px;margin:6px 0;color:#0a0101}'
    + '.srfix .row{display:grid;grid-template-columns:repeat(auto-fit,minmax(130px,1fr));gap:8px;margin-bottom:8px}'
    + '.srfix .btns{display:flex;gap:10px;align-items:center;flex-wrap:wrap}';

  function termOptions(sel){ return [1,2,3,4,5,6].map(n => '<option value="'+n+'"'+(n === sel ? ' selected' : '')+'>Term '+n+'</option>').join(''); }

  function build(){
    const st = document.createElement('style'); st.textContent = css; document.head.appendChild(st);
    const main = document.querySelector('main') || document.body;

    // Sticky bar: who is being assessed, and anything not yet saved
    bar = document.createElement('div'); bar.id = 'srStick';
    bar.innerHTML = '<div class="srbar bad" id="srBar"><span id="srBarTxt"></span><button id="srBarBtn" type="button">Choose</button></div><div class="srPendBox"></div>';
    main.insertBefore(bar, main.firstChild);

    // Step 1: choose the child, at the very top
    topCard = document.createElement('section'); topCard.className = 'card'; topCard.id = 'srTop';
    topCard.innerHTML = '<h2>Step 1: Who are you assessing?</h2>'
      + '<p class="hint">Choose the child before you start. The result is saved to the child shown here.</p>'
      + '<div class="sr"><div><label for="srClass">Class</label><select id="srClass"><option value="">Loading classes…</option></select></div>'
      + '<div><label for="srPupil">Pupil</label><select id="srPupil" disabled><option value="">Choose a class first</option></select></div>'
      + '<div><label for="srTerm">Term</label><select id="srTerm">' + termOptions(0) + '</select></div>'
      + '<div><label for="srDate">Date taken</label><input type="date" id="srDate"></div></div>'
      + '<p id="srWho"></p><ul class="hist" id="srHist"></ul>';
    main.insertBefore(topCard, bar.nextSibling);

    // Bottom card: save only
    card = document.createElement('section'); card.className = 'card'; card.id = 'saveCard';
    card.innerHTML = '<h2>Save the result</h2><div class="srPendBox"></div>'
      + '<p class="srFor" id="srFor"></p>'
      + '<div class="actions"><button class="act" id="srSave" disabled>Save result</button><button class="link" id="srUndo" hidden>Undo</button><button class="act" id="srNext" hidden>Next pupil &rsaquo;</button></div>'
      + '<p class="st" id="srStatus"></p><a id="srSignin" class="link" href="" target="_blank" rel="noopener" hidden>Open a new tab to sign in</a>';
    main.appendChild(card);

    $q('srDate').value = today();
    $q('srClass').onchange = onClass; $q('srPupil').onchange = onPupil;
    $q('srSave').onclick = save; $q('srUndo').onclick = undo; $q('srNext').onclick = nextPupil;
    $q('srDate').oninput = $q('srTerm').onchange = () => refresh();
    $q('srBarBtn').onclick = () => { topCard.scrollIntoView({behavior: 'smooth', block: 'start'}); setTimeout(() => { const e = $q('srPupil').disabled ? $q('srClass') : $q('srPupil'); try { e.focus(); } catch(x){} }, 350); };
    $q('srSignin').href = location.href;
    showPending(); loadRoster();
    // a save that failed is tried again by itself when the wifi comes back or the page is reopened
    window.addEventListener('online', retryPending);
    document.addEventListener('visibilitychange', () => { if (document.visibilityState === 'visible') retryPending(); });
  }

  function ensureRoster(){
    if (roster) return Promise.resolve(roster);
    if (!rosterLoading) rosterLoading = call('GET', '/pupils').then(d => {
      rosterLoading = null;
      if (d && d.pupils) roster = PupilLabels.byClass(d.pupils);   // sorted, each pupil gets .label (initials) and .pcode (pupil code)
      return roster;
    });
    return rosterLoading;
  }
  function classNames(){
    return Object.keys(roster).sort((a, b) => (roster[a][0].yearGroup || '').localeCompare(roster[b][0].yearGroup || '', undefined, {numeric: true}) || a.localeCompare(b));
  }
  function pupilOptions(cls, selected){
    const list = roster && roster[cls] || [];
    return '<option value="">' + (cls ? 'Choose a pupil' : 'Choose a class first') + '</option>' + list.map(p => p.pcode
      ? '<option value="'+h(p.pcode)+'" data-pupil-id="'+h(p.pcode)+'"'+(p.pcode === selected ? ' selected' : '')+'>'+h(p.label)+'</option>'
      : '<option value="" disabled>'+h(p.label)+' (no code yet)</option>').join('');
  }
  function classOf(code){ for (const c of Object.keys(roster || {})) if (roster[c].some(p => p.pcode === code)) return c; return ''; }
  function labelOf(code){ for (const c of Object.keys(roster || {})) { const p = roster[c].find(p => p.pcode === code); if (p) return p.label; } return ''; }

  async function loadRoster(){
    await ensureRoster();
    if (!roster) { status('Could not load the class lists. Check the wifi or sign in again.', false); $q('srClass').innerHTML = '<option value="">Class lists unavailable</option>'; return; }
    $q('srClass').innerHTML = '<option value="">Choose a class</option>' + classNames().map(n => '<option value="'+h(n)+'">'+h(n)+'</option>').join('');
    const last = store.get(CLASS_KEY);
    if (last && roster[last]) { $q('srClass').value = last; onClass(); }
    // the pupil is NOT pre-filled from last time: choosing the child is the first step, every time
    const c = await call('GET', '/readingresults-db', {limit: 1});
    if (c && c.current) { current = c.current; $q('srTerm').value = String(c.current.term); }
    refresh();
  }
  function onClass(){
    const c = $q('srClass').value;
    switchGuard('');
    store.set(CLASS_KEY, c);
    $q('srPupil').disabled = !c;
    $q('srPupil').innerHTML = pupilOptions(c, '');
    $q('srHist').innerHTML = ''; refresh();
    if (cfg.onPupilChange) cfg.onPupilChange('');
  }
  // Changing the child must not carry the last child's marks over: clear them if that result was saved, otherwise ask.
  function switchGuard(next){
    const was = shown; shown = next;
    if (!was || was === next || !cfg.reset) return;
    const saved = !!lastSaved || (!!attemptId && pendingList().some(x => x.payload.client_id === attemptId)), dirty = cfg.dirty ? cfg.dirty() : true;
    if (saved || !dirty) { try { cfg.reset(); } catch(e){} return; }
    if (confirm('You have marks for the previous child that are not saved.\n\nOK = clear them and start fresh for this child.\nCancel = keep the marks and use them for this child.')) { try { cfg.reset(); } catch(e){} }
  }
  async function onPupil(){
    const upn = $q('srPupil').value;   // upn here = the pupil CODE (server accepts a code or a UPN in `upn`)
    switchGuard(upn);
    lastSaved = null; refresh();
    if (cfg.onPupilChange) cfg.onPupilChange(upn);
    $q('srHist').innerHTML = '';
    if (!upn) return;
    loadHistory();
  }
  async function loadHistory(){
    const u = $q('srPupil').value; if (!u) return;
    const d = await call('GET', '/readingresults-db', {upn: u, tool: cfg.tool, limit: 8});
    if (u !== $q('srPupil').value || !d.results) return;
    renderHist(d.results);
  }
  function renderHist(results){
    const ul = $q('srHist');
    ul.innerHTML = results.length
      ? '<li><b>Earlier results for this pupil</b> <span class="note">Saved to the wrong child, term or date? Use Move. Wrong test? Remove it and assess again.</span></li>'
        + results.map(r => '<li data-id="'+r.id+'">' + h(ukDate(r.taken_on)) + ' &middot; Term ' + r.term + ' &middot; ' + h(describe(r))
          + (r.edit_note ? ' <span class="note">(corrected: ' + h(r.edit_note) + ')</span>' : '')
          + ' <button class="link" data-act="move" data-id="'+r.id+'">Move</button><button class="link" data-act="remove" data-id="'+r.id+'">Remove</button><div class="fixhost"></div></li>').join('')
      : '<li>No results saved for this pupil yet.</li>';
    ul.onclick = e => {
      const b = e.target.closest('button[data-act]'); if (!b) return;
      const r = results.find(x => x.id === +b.dataset.id); if (!r) return;
      const host = b.closest('li').querySelector('.fixhost');
      if (b.dataset.act === 'move') fixResult(r, host, loadHistory);
      else removeResult(r, host, loadHistory);
    };
  }
  function describe(r){
    const bands = {greater_depth: 'greater depth', on_track: 'on track', not_yet: 'not yet on track', o1: 'O1', o2: 'O2', y: 'Y', a: 'A', secure: 'secure', nearly: 'nearly there', on_target: 'on target', below_target: 'below target', excellent: 'excellent', satisfactory: 'satisfactory', unsatisfactory: 'unsatisfactory'};
    const b = bands[r.band] || r.band;
    if (r.tool === 'fluency') return 'Level ' + r.level + ': ' + r.detail.wcpm + ' words correct per minute, ' + r.detail.accuracy + '% accurate (' + b + ')' + (r.detail.rubric_total != null ? ', rubric ' + r.detail.rubric_total + '/20' : '');
    if (r.tool === 'phonics') return r.level + ': ' + r.score + '/3 (' + b + ')' + (r.detail && r.detail.rubric_total != null ? ', rubric ' + r.detail.rubric_total + '/20' : '');
    if (r.tool === 'pm_benchmark') return 'Level ' + r.level + ' (' + (r.detail && r.detail.colour || '') + '): ' + r.detail.accuracy + '% accurate, comprehension ' + r.score + '/' + r.total;
    return 'Level ' + r.level + ' test ' + r.test_id + ': ' + r.score + '/' + r.total + ', ' + r.percent + '% (' + b + ')';
  }

  // ---- Correcting a saved result (also used by the Results page) ----
  async function fixResult(r, host, done){
    if (host.firstChild) { host.innerHTML = ''; return; }   // second tap closes it
    host.innerHTML = '<div class="srfix">Loading…</div>';
    await ensureRoster();
    if (!roster) { host.innerHTML = '<div class="srfix">Could not load the class lists.</div>'; return; }
    const code = r.pupilCode || r.upn, cls = classOf(code) || Object.keys(roster)[0];
    host.innerHTML = '<div class="srfix"><b>Move this result</b> (' + h(describe(r)) + ')'
      + '<div class="row"><div><label>Class</label><select class="fxc">' + classNames().map(n => '<option value="'+h(n)+'"'+(n === cls ? ' selected' : '')+'>'+h(n)+'</option>').join('') + '</select></div>'
      + '<div><label>Pupil</label><select class="fxp">' + pupilOptions(cls, code) + '</select></div>'
      + '<div><label>Term</label><select class="fxt">' + termOptions(r.term) + '</select></div>'
      + '<div><label>Date taken</label><input type="date" class="fxd" value="' + h((r.taken_on || '').slice(0, 10)) + '"></div></div>'
      + '<div class="btns"><button class="act fxs" type="button">Save change</button><button class="link fxx" type="button">Cancel</button><span class="st fxm"></span></div></div>';
    const q = s => host.querySelector(s);
    q('.fxc').onchange = () => { q('.fxp').innerHTML = pupilOptions(q('.fxc').value, ''); };
    q('.fxx').onclick = () => { host.innerHTML = ''; };
    q('.fxs').onclick = async () => {
      const pup = q('.fxp').value; if (!pup) { q('.fxm').textContent = 'Choose the pupil.'; q('.fxm').className = 'st fxm bad'; return; }
      q('.fxs').disabled = true; q('.fxm').textContent = 'Saving…'; q('.fxm').className = 'st fxm';
      const d = await call('POST', '/readingresults-db', {}, {action: 'update', id: r.id, upn: pup, term: +q('.fxt').value, taken_on: q('.fxd').value});
      if (d.ok) { if (lastSaved && lastSaved.id === r.id) lastSaved = null; host.innerHTML = '<div class="srfix st ok">' + (d.changed ? 'Moved: now with ' + h(labelOf(pup)) + ' (' + h(classOf(pup)) + '), Term ' + d.result.term + ', ' + h(ukDate(d.result.taken_on)) + '.' : 'No change.') + '</div>'; setTimeout(() => done && done(), 900); }
      else { q('.fxs').disabled = false; q('.fxm').textContent = d.error || 'Could not change it.'; q('.fxm').className = 'st fxm bad'; }
    };
  }
  async function removeResult(r, host, done){
    if (!confirm('Remove this result?\n\n' + describe(r) + '\n\nIt will disappear from the pupil\'s record. (To put it with a different child, use Move instead.)')) return;
    const d = await call('POST', '/readingresults-db', {}, {action: 'void', id: r.id});
    if (d.ok) { if (lastSaved && lastSaved.id === r.id) { lastSaved = null; refresh(false); } done && done(); }
    else { host.innerHTML = '<div class="srfix st bad">' + h(d.error || 'Could not remove it.') + '</div>'; }
  }

  // ---- Saving ----
  function sig(){ const s = cfg.get(); return JSON.stringify([$q('srPupil').value, s.body, $q('srDate').value, $q('srTerm').value]); }
  function status(msg, ok){ const e = $q('srStatus'); if (!e) return; e.textContent = msg || ''; e.className = 'st' + (ok === true ? ' ok' : ok === false ? ' bad' : ''); }
  function chosenText(){
    const sel = $q('srPupil'), cls = $q('srClass').value;
    if (!sel.value) return null;
    return {name: sel.options[sel.selectedIndex].text, cls: cls, term: $q('srTerm').value, date: $q('srDate').value};
  }

  function refresh(msg){
    if (!card) return;
    const s = cfg.get(), pupil = $q('srPupil').value, btn = $q('srSave'), who = chosenText();
    const done = lastSaved && lastSaved.sig === sig();
    btn.disabled = saving || !s.ready || !pupil || !!done;
    btn.textContent = done ? 'Saved' : (who ? 'Save result for ' + who.name : 'Save result');
    $q('srNext').hidden = !done; $q('srUndo').hidden = !done;
    // the sticky bar and the Step 1 line
    const b = $q('srBar');
    if (who) {
      const line = who.name + ' (' + who.cls + ') · Term ' + who.term + ' · ' + ukDate(who.date);
      b.className = 'srbar ok'; $q('srBarTxt').innerHTML = 'Assessing: <span data-pupil-id="' + h(pupil) + '">' + h(who.name) + '</span> (' + h(who.cls) + ') &middot; Term ' + h(who.term) + ' &middot; ' + h(ukDate(who.date));
      $q('srBarBtn').textContent = 'Change';
      $q('srWho').className = 'ok'; $q('srWho').textContent = 'Saving this result for ' + line;
      $q('srFor').className = 'srFor'; $q('srFor').innerHTML = 'Saving for: <b data-pupil-id="' + h(pupil) + '">' + h(who.name) + '</b> (' + h(who.cls) + ') &middot; Term ' + h(who.term) + ' &middot; ' + h(ukDate(who.date)) + ' <button class="link" id="srChange" type="button">Wrong child? Change</button>';
      $q('srChange').onclick = () => $q('srBarBtn').onclick();
    } else {
      b.className = 'srbar bad'; $q('srBarTxt').textContent = 'Choose who you are assessing (Step 1) before you save';
      $q('srBarBtn').textContent = 'Choose pupil';
      $q('srWho').className = 'bad'; $q('srWho').textContent = 'No pupil chosen yet.';
      $q('srFor').className = 'srFor bad'; $q('srFor').innerHTML = 'No pupil chosen. <button class="link" id="srChange" type="button">Choose the pupil at the top</button>';
      $q('srChange').onclick = () => $q('srBarBtn').onclick();
    }
    if (msg !== false && !saving && !done) status(!pupil ? '' : !s.ready ? s.hint : 'Ready to save: ' + s.summary);
    if (!done && !saving && msg !== false) $q('srSignin').hidden = true;
  }

  async function save(){
    const s = cfg.get(), sel = $q('srPupil'); if (!s.ready || !sel.value || saving) return;
    const sg = sig();
    if (sg !== attemptSig) { attemptSig = sg; attemptId = uuid(); }   // the same marks keep the same id, so a retry can never add it twice
    saving = true; refresh();
    const payload = Object.assign({action: 'save', client_id: attemptId, upn: sel.value, tool: cfg.tool, source: 'paper',
      taken_on: $q('srDate').value, term: +$q('srTerm').value}, s.body);
    const name = sel.options[sel.selectedIndex].text + ' (' + $q('srClass').value + ')';
    await send(payload, name, s.summary, sg);
    saving = false; refresh(false);
  }
  async function send(payload, name, summary, sg){
    status('Saving…'); $q('srSignin').hidden = true;
    const d = await call('POST', '/readingresults-db', {}, payload);
    if (d.ok) {
      dropPending(payload.client_id);
      if (sg) { lastSaved = {id: d.result.id, sig: sg, name: name}; attemptSig = ''; }
      status('Saved for ' + name + ': ' + (summary || describe(d.result)) + ' (Term ' + d.result.term + ')' + (d.duplicate ? ' – already saved' : '') + (sg ? '. Now press Next pupil.' : '.'), true);
      if ($q('srPupil').value === (payload.upn)) loadHistory();
      return true;
    }
    if (d.network || d.signin) { keepPending(payload, name, summary); $q('srSignin').hidden = !d.signin; }
    status((d.error || 'Could not save. Try again.') + ((d.network || d.signin) ? '' : ' Nothing was saved.'), false);
    return false;
  }
  async function undo(){
    if (!lastSaved) return; const id = lastSaved.id, name = lastSaved.name;
    const d = await call('POST', '/readingresults-db', {}, {action: 'void', id: id});
    if (d.ok) { lastSaved = null; status('Removed the result for ' + name + '.', true); loadHistory(); refresh(false); }
    else status(d.error || 'Could not remove it.', false);
  }
  // After a save: clear the child and the marks, ready for the next one
  function nextPupil(){
    lastSaved = null; attemptSig = ''; shown = '';
    $q('srPupil').value = ''; $q('srHist').innerHTML = '';
    if (cfg.onPupilChange) cfg.onPupilChange('');
    if (cfg.reset) { try { cfg.reset(); } catch(e){} }
    status(''); refresh();
    topCard.scrollIntoView({behavior: 'smooth', block: 'start'});
    setTimeout(() => { try { $q('srPupil').focus(); } catch(e){} }, 350);
  }

  // A save that failed (wifi, sign-in ended, server problem) is kept on this device with its own id so a retry can never
  // add it twice; the same child + marks is only ever kept once.
  function pendingList(){ try { return JSON.parse(store.get(PENDING_KEY) || '[]'); } catch(e){ return []; } }
  function keepPending(payload, name, summary){
    const key = x => JSON.stringify([x.upn, x.tool, x.taken_on, x.term, x.test_id, x.level, x.marks, x.attempted, x.errors, x.seconds, x.rubric]);
    const l = pendingList().filter(x => x.payload.client_id !== payload.client_id && key(x.payload) !== key(payload));
    l.push({payload: payload, name: name, summary: summary}); store.set(PENDING_KEY, JSON.stringify(l)); showPending();
  }
  function dropPending(id){ store.set(PENDING_KEY, JSON.stringify(pendingList().filter(x => x.payload.client_id !== id))); showPending(); }
  let retrying = false;
  async function retryPending(){
    if (retrying || saving) return; const l = pendingList(); if (!l.length) return;
    retrying = true;
    for (const x of l) { const ok = await send(x.payload, x.name, x.summary); if (!ok) break; }
    retrying = false; refresh(false);
  }
  function showPending(){
    const l = pendingList();
    const html = l.length ? '<div class="pend"><b>' + l.length + ' result' + (l.length > 1 ? 's' : '') + ' not saved yet:</b> ' + l.map(x => h(x.name) + ' (' + h(x.summary) + ')').join('; ')
      + ' <button class="link" data-pend="retry">Try again</button><button class="link" data-pend="drop">Discard</button></div>' : '';
    document.querySelectorAll('.srPendBox').forEach(box => {
      box.innerHTML = html;
      box.onclick = e => { const b = e.target.closest('button[data-pend]'); if (!b) return;
        if (b.dataset.pend === 'retry') retryPending();
        else if (confirm('Discard ' + l.length + ' result' + (l.length > 1 ? 's' : '') + ' that have not been saved? They will be lost.')) { store.del(PENDING_KEY); showPending(); } };
    });
  }

  return {
    init(c){ cfg = c; if (ON) build(); },
    refresh(){ if (ON && card) refresh(); },
    isOn(){ return ON; },
    call,   // exposed so other shared modules (e.g. scan_marking.js) reuse the same authed /_api call + 401 handling, instead of duplicating it
    uuid, today,
    fixResult, removeResult, describe,   // the Results page uses these for its Move / Remove links
  };
})();
