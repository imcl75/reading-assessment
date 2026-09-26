"""Shared validation for comprehension tests (used by build.py and check_batch.py)."""
import re
# Target length by book level (agreed): ~250 at 18, ~400 at 24, ~500 from 28, roughly linear between; 31-34 stay at ~500
TARGET = {18:250,19:275,20:300,21:325,22:350,23:375,24:400,25:425,26:450,27:475,28:500,29:500,30:500,31:500,32:500,33:500,34:500}
# Questions per test: 10 at 18 rising to 12 at 24 and 14 from 27
QS = {18:10,19:10,20:11,21:11,22:12,23:12,24:12,25:13,26:13,27:14,28:14,29:14,30:14,31:14,32:14,33:14,34:14}
RANGE = lambda l: (round(TARGET[l]*0.92), round(TARGET[l]*1.08))
DOMAINS = {"2a","2b","2c","2d","2e","2g"}
KINDS = {"find","mc","short","order","tf"}
def syl(w):
    w=re.sub(r'[^a-z]','',w.lower()); n=len(re.findall(r'[aeiouy]+',w))
    if w.endswith('e') and not w.endswith('le') and n>1:n-=1
    return max(n,1) if w else 0
def fk(x):
    s=len(re.findall(r'[.!?]+["”]?(?:\s|$)',x+" ")); w=x.split()
    return 0.39*len(w)/s+11.8*sum(map(syl,w))/len(w)-15.59
# Target Flesch-Kincaid grade by book level, from the real benchmark texts (smoothed). F = fiction (narrative, fictional recount),
# N = non-fiction, D = description (midway). F1-F4 (levels 31-34) rise steadily above level 30.
FKT = {
 "F":{18:3.6,19:3.8,20:3.5,21:4.1,22:5.0,23:5.2,24:5.4,25:5.7,26:6.0,27:6.3,28:6.6,29:6.9,30:7.2,31:7.6,32:8.0,33:8.4,34:8.8},
 "N":{18:3.7,19:4.2,20:3.7,21:4.7,22:5.4,23:5.7,24:6.0,25:6.4,26:6.8,27:7.1,28:7.5,29:7.8,30:8.0,31:8.4,32:8.8,33:9.2,34:9.6},
}
def fk_kind(t): return "F" if t["type"] in ("Narrative","Recount (Fictional)") else "D" if t["type"]=="Description" else "N"
def fk_target(t):
    k=fk_kind(t); l=t["level"]
    return (FKT["F"][l]+FKT["N"][l])/2 if k=="D" else FKT[k][l]
def fk_warnings(tests):
    out=[]
    for t in tests:
        v=fk(" ".join(t["text"])); tg=fk_target(t); lo=1.5 if t["level"]<=21 else 0.8   # the grade is a rough guide at the lowest levels
        if v<tg-lo: out.append(f'{t["id"]}: reading grade {v:.1f} is too easy for this level (target {tg:.1f}, allow {tg-lo:.1f} to {tg+1.5:.1f})')
        elif v>tg+1.5: out.append(f'{t["id"]}: reading grade {v:.1f} is too hard for this level (target {tg:.1f}, allow {tg-lo:.1f} to {tg+1.5:.1f})')
    return out
def validate(tests):
    err=[]; ids=set(); titles=set()
    for t in tests:
        i0=t["id"]; l=t["level"]
        if l not in TARGET: err.append(f"{i0}: level {l} not supported"); continue
        if i0 in ids: err.append(f"{i0}: duplicate id")
        ids.add(i0)
        if t["title"].lower() in titles: err.append(f"{i0}: duplicate title")
        titles.add(t["title"].lower())
        if not i0.startswith(f"{l}-"): err.append(f"{i0}: id must start with '{l}-'")
        x=" ".join(t["text"]); n=len(x.split()); lo,hi=RANGE(l)
        if not lo<=n<=hi: err.append(f"{i0}: {n} words, need {lo}-{hi} (target {TARGET[l]})")
        nq=QS[l]
        if len(t["qs"])!=nq: err.append(f"{i0}: {len(t['qs'])} questions, need {nq}")
        if sum(q["d"]=="2d" for q in t["qs"])<3: err.append(f"{i0}: needs 3+ inference (2d) questions")
        if not any(q["d"]=="2a" for q in t["qs"]): err.append(f"{i0}: needs a vocabulary (2a) question")
        if not any(q["d"]=="2c" for q in t["qs"]): err.append(f"{i0}: needs a summarise/sequence (2c) question")
        keys=[q["a"] for q in t["qs"] if q["k"]=="mc"]
        if len(keys)>=3 and len(set(keys))<2: err.append(f"{i0}: all multiple-choice answers are '{keys[0]}' - vary the correct letter")
        for i,q in enumerate(t["qs"],1):
            w=f"{i0} Q{i}"
            if q["d"] not in DOMAINS: err.append(f"{w}: bad domain {q['d']}")
            if q["k"] not in KINDS: err.append(f"{w}: bad kind {q['k']}")
            if q["m"] not in (1,2): err.append(f"{w}: marks must be 1 or 2")
            elif q["m"]==2 and l<=24: err.append(f"{w}: levels up to 24 must be 1-mark questions")
            elif q["m"]==2 and l<=28 and not re.search(r"\btwo\b",q["q"].lower()): err.append(f'{w}: 2 marks only for a "give two ..." question at levels 25-28')
            if not q.get("g") and q["k"]=="short": err.append(f"{w}: short answer needs marking guidance (g)")
            if q["k"]=="find" and q["a"].lower() not in x.lower(): err.append(f"{w}: 'find' answer not verbatim in text")
            if q["k"]=="mc":
                if len(q.get("opts",[]))!=4: err.append(f"{w}: mc needs 4 options")
                elif q["a"] not in "ABCD" or len(q["a"])!=1: err.append(f"{w}: mc key must be A-D")
            if q["k"]=="order" and sorted(q["a"])!=list(range(1,len(q["items"])+1)): err.append(f"{w}: bad order key")
            if q["k"]=="tf" and (len(q["a"])!=len(q["items"]) or set(q["a"])-{"T","F"}): err.append(f"{w}: bad tf key")
    return err
