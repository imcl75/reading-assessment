"""Checks every text is decodable at its level (and uses its own phase without being ALL new-phase words),
then builds a single self-contained index.html."""
import json, pathlib, sys, hashlib
from levels import ADD, NAMES, check_text, cum, mix_problems, phase_mix
from texts_src import B
try: from texts_src import SKIP_CHECKS
except ImportError: SKIP_CHECKS=False
here = pathlib.Path(__file__).parent
SOUND_ORDER = {1:"s a t p i n m d g o c k ck e u r h b f ff l ll ss",2:"j v w x y z zz qu ch sh th ng",
 3:"ai ee igh oa oo ar or ur; -ing endings with no change to the root word",4:"ow oi ear air ure er",
 5:"adjacent consonants in one-syllable words (CVCC, CCVC, CCVCC, CCCVC); -ed endings",
 6:"polysyllabic words, longer consonant clusters and all graphemes so far; -es, -er, -est, un-; contractions",
 7:"ay ou ie ea oy ir ue aw wh ph ew oe au ey",8:"split digraphs a-e e-e i-e o-e u-e",
 9:"no new graphemes — consolidates the whole of Phase 5a",
 10:"alternative pronunciations (e.g. snow, chief, head, find, cold, soft c and g, y as in by / very)",
 11:"alternative spellings (e.g. tch, dge, kn, wr, mb, ture, tion)"}
DECODABLE={"a","an","and","as","at","in","is","it","on","up","his","has"}   # ordinary decodable words, not ULS common exception words
data=[]; errors=0
for lv in sorted(B):
    items=[]
    cum_sounds="; ".join(SOUND_ORDER[k] for k in range(1,lv+1))
    _,cew,_=cum(lv); cew={w for w in cew if w.lower() not in DECODABLE}
    for title,text,qs in B[lv]:
        bad=[] if SKIP_CHECKS else check_text(text,lv); mix=[] if SKIP_CHECKS else mix_problems(text,lv)
        if bad or mix or len(qs)!=3 or not any(q[0]=="why" for q in qs):
            errors+=1; print("FAIL",lv,NAMES[lv],"|",title,"|",bad,mix)
        toks,fl=phase_mix(text,lv)
        focus=[] if lv==1 else list(dict.fromkeys(t.lower() for t,f in zip(toks,fl) if f==lv))
        # up to two pictures per text, side by side: p{level}-{n}a.jpg and p{level}-{n}b.jpg
        # (the address changes whenever a picture changes, so a stale copy held by a cache is never shown)
        images=[f'img/{p.name}?v={hashlib.md5(p.read_bytes()).hexdigest()[:8]}' for p in (here/'img'/f'p{lv}-{len(items)}{k}.jpg' for k in 'ab') if p.exists()]
        items.append(dict(title=title,text=text,focus=focus,images=images,qs=[dict(t=t,q=q,a=a) for t,q,a in qs]))
    data.append(dict(level=lv,name=NAMES[lv],sounds=cum_sounds,cew=", ".join(sorted(cew,key=str.lower)),texts=items))
if errors: sys.exit("not built: %d problem(s)"%errors)
html=(here/"template.html").read_text().replace("/*DATA*/",json.dumps(data,ensure_ascii=False)).replace("/*SAVE_RESULTS*/","".join((here.parent / "shared" / f).read_text() for f in ("names-file.js", "pupil_labels.js", "save_results.js")))
(here/"index.html").write_text(html)
print("built index.html:",sum(len(d["texts"]) for d in data),"texts across",len(data),"phases, all decodable at their level")
