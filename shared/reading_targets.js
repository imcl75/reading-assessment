// Expected-standard reading level by year group and term (Innes, 05.10.26). F(n) = Free Reader n = level 30+n; null = no target set.
// One copy, built into the Fluency and Results pages (/*TARGETS*/).
const TARGETS = {
  Y2:[null,null,18,20,22,23], Y3:[24,25,25,26,26,27], Y4:[27,28,28,29,30,31],
  Y5:[31,32,32,33,33,34], Y6:[34,35,36,36,36,36]
};
// yearGroup may arrive as "Y5", "5" or "Year 5"; term as 1-6. Returns a level number or null.
function targetLevelFor(yearGroup, term){
  const m = String(yearGroup == null ? '' : yearGroup).match(/(\d)/), t = +term;
  const row = m && TARGETS['Y' + m[1]];
  return row && t >= 1 && t <= 6 && row[t - 1] != null ? row[t - 1] : null;
}
