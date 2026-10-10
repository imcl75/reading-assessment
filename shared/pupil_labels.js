/* Initials labels for pupils (shared by every reading-assessment tool; inlined by each tool's build.py
   together with save_results.js). Same rule as WFANames.initialsLabels in wfa-shared/web/names-file.js
   and names_display.py on the server: first letter of the first name + first letter of the last word of
   the surname, upper case ("IM"); pupils in the SAME class whose labels clash get 2 then 3 letters
   ("InMc"). Screens and printed sheets show these labels, never full names; the pupil's identity value
   everywhere (dropdown values, requests, localStorage) is the pupil CODE (pupilId, "p_" + 10 chars). */
const PupilLabels = (function(){
  const LETTERS = /[^A-Za-zÀ-ɏ]/g;
  // pairs: [[first, last], ...] -> labels, same order, clash-aware across the list
  function labels(pairs){
    const P = pairs.map(p => {
      const f = String(p[0] || '').trim().split(/\s+/)[0] || '';
      const lw = String(p[1] || '').trim().split(/\s+/).filter(Boolean);
      return [f.replace(LETTERS, ''), (lw.length ? lw[lw.length - 1] : '').replace(LETTERS, '')];
    });
    const lab = (i, n) => {
      const f = P[i][0], l = P[i][1];
      if (!l) return f ? f.charAt(0).toUpperCase() + f.slice(1, 2).toLowerCase() : '';
      if (n === 1) return (f.charAt(0) + l.charAt(0)).toUpperCase();
      const fp = f.slice(0, n), lp = l.slice(0, n);
      return fp.charAt(0).toUpperCase() + fp.slice(1) + lp.charAt(0).toUpperCase() + lp.slice(1);
    };
    const lv = P.map(() => 1);
    let out = [];
    for (let guard = 0; guard < 40; guard++) {
      out = P.map((_, i) => lab(i, lv[i]));
      const groups = {};
      out.forEach((t, i) => { (groups[t.toLowerCase()] = groups[t.toLowerCase()] || []).push(i); });
      let changed = false;
      Object.keys(groups).forEach(k => {
        const idxs = groups[k];
        if (idxs.length < 2) return;
        const distinct = {};
        idxs.forEach(i => { distinct[(P[i][0] + '|' + P[i][1]).toLowerCase()] = 1; });
        if (Object.keys(distinct).length < 2) return;
        idxs.forEach(i => { if (P[i][1] && lv[i] < Math.max(P[i][0].length, P[i][1].length)) { lv[i]++; changed = true; } });
      });
      if (!changed) break;
    }
    const seen = {};
    return out.map(t => { const k = t.toLowerCase(); seen[k] = (seen[k] || 0) + 1; return seen[k] === 1 ? t : t + ' ' + seen[k]; });
  }
  // /_api/planning/pupils list -> {className: [pupil, ...]} sorted by first name then surname (first-initial order), each pupil
  // given .label (clash-aware inside its own class) and .code (pupilId, '' if the pupil has none yet).
  function byClass(pupils){
    const roster = {};
    (pupils || []).forEach(p => { const c = p.class || p.code || '?'; (roster[c] = roster[c] || []).push(p); });
    Object.values(roster).forEach(list => {
      list.sort((a, b) => (a.first + ' ' + a.last).localeCompare(b.first + ' ' + b.last));
      const ls = labels(list.map(p => [p.first, p.last]));
      list.forEach((p, i) => { p.label = ls[i]; p.pcode = String(p.pupilId || '').trim(); });
    });
    return roster;
  }
  return {labels, byClass};
})();
