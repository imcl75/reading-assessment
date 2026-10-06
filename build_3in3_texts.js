// Builds 3in3/texts.json (passages + which text each session used) from the pupil pages, so the teacher
// profile pages can show the passage next to a pupil's answers. Re-run after changing any 3in3/yN/index.html text:
//   node build_3in3_texts.js
const fs = require('fs'), vm = require('vm');
const out = {};
function grab(file, textsName, sessionsName, from) {
  const s = fs.readFileSync(file, 'utf8');
  const a = s.indexOf(from), b = s.indexOf('const ALL_SESSIONS');
  return vm.runInNewContext(s.slice(a, b) + `;({T:${textsName},S:${sessionsName}})`);
}
const sources = {
  Y3: ['3in3/y5/index.html', 'TEXTS_Y3', 'SESSIONS_Y3', 'const TEXTS_Y3'],
  Y4: ['3in3/y4/index.html', 'TEXTS', 'SESSIONS', 'const TEXTS'],
  Y5: ['3in3/y5/index.html', 'TEXTS_Y5', 'SESSIONS_Y5', 'const TEXTS_Y3'],
  Y6: ['3in3/y6/index.html', 'TEXTS_Y6', 'SESSIONS_Y6', 'const TEXTS_Y3'],
};
for (const [yr, [file, t, s, from]] of Object.entries(sources)) {
  const g = grab(file, t, s, from);
  const sessions = {};
  g.S.forEach(x => { sessions[x.idx] = x.textIndex; });
  out[yr] = { texts: g.T, sessions };
}
fs.writeFileSync('3in3/texts.json', JSON.stringify(out));
console.log('wrote 3in3/texts.json', Object.fromEntries(Object.entries(out).map(([k, v]) => [k, Object.keys(v.texts).length + ' texts, ' + Object.keys(v.sessions).length + ' sessions'])));
