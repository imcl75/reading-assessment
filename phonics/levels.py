"""Decodability rules built from the Unlocking Letters and Sounds progression (Phases 2-5c).
Used ONLY as an internal checker; the ULS document itself is not reproduced."""
import re

VOW1 = list("aeiou")
# grapheme sets added at each level (spelling-based; pronunciation traps are handled in TRAPS below)
ADD = {
 1: dict(g="s a t p i n m d g o c k e u r h b f l ck ff ll ss".split(),
         cew="the to into no go I a and is it in at an as his has up on".split()),
 2: dict(g="j v w x y z zz qu ch sh th ng".split(), cew="me we be he she".split()),
 3: dict(g="ai ee igh oa oo ar or ur".split(), cew="was you they all".split()),
 4: dict(g="ow oi ear air ure er".split(), cew="are my her".split()),
 5: dict(g=[], cew="said have like so do some come were there little one when out what".split()),
 6: dict(g=[], cew=[]),      # Phase 4 Mastery: polysyllabic words, longer clusters, -es -er -est un-, contractions, possessives
 7: dict(g="ay ou ie ea oy ir ue aw wh ph ew oe au ey".split(), cew="oh their people Mr Mrs looked called asked Monday Tuesday Wednesday Thursday Friday Saturday Sunday".split()),
 8: dict(g=[], cew=[], split=True),
 9: dict(g=[], cew=[]),      # Phase 5a (all): no new graphemes/CEW \u2014 consolidates the whole of Phase 5a, same decodability as level 8
 10: dict(g=["y!any"], cew="water where who again thought through mouse work many laughed because different any eyes friends once please".split()),
 11: dict(g="tch dge kn gn wr mb ture tion ci sion augh".split(), cew=[]),
}
NAMES = {1:"Phase 2",2:"Phase 3 (Weeks 1\u20133)",3:"Phase 3 (Weeks 4\u20136)",4:"Phase 3 (Weeks 7\u20138)",5:"Phase 4",6:"Phase 4 Mastery",
         7:"Phase 5a (Weeks 1\u20134)",8:"Phase 5a (Weeks 5\u20136)",9:"Phase 5a (all)",10:"Phase 5b",11:"Phase 5c"}
NOADJ_MAX = 4          # levels 1-4: no adjacent consonant graphemes (CVC-type words)
SUFFIX_FROM = {"s":1,"ing":3,"ed":5,"es":6,"er":6,"est":6}   # -ed and -ing are Phase 4; -es -er -est un- come with Phase 4 Mastery (Y1 revision)
CONTRACTIONS = {"it's","i'm","don't","can't","isn't","didn't","let's","that's","he's","she's","i'll","we'll","they're","we're"}  # from Phase 4 Mastery

# words that segment on spelling but are taught later / pronounced differently -> minimum level
TRAPS = {}
def trap(level, words):
    for w in words.split(): TRAPS[w] = level
trap(99,"of put push pull full bull bush to do so no go he she we me be you your said all they")  # only via CEW list
trap(10,"snow low show know slow grow blow flow own row yellow window follow tomorrow elbow pillow below bow throw")
trap(10,"bread head dead ready heavy breath great break steak bear pear wear heart learn earth early tear read weather feather")
trap(10,"field chief thief brief believe piece niece")
trap(10,"soup touch young four tough country journey group route")
trap(10,"fast last past after grass class plant ask master castle want wash watch swan wasp swap wallet was")
trap(10,"mother son ton month other brother love glove done none above wonder monkey money honey front dozen")
trap(10,"both gold cold old most post told hold host roll bolt colt jolt ghost only open over zero hello photo ago also potato")
trap(10,"find kind mind wild child blind behind mild climb pint")
trap(10,"unit music human pupil sugar")
trap(10,"give live gem gentle giant giraffe age page cage huge large orange change gym")
trap(10,"key donkey money valley monkey turkey")
trap(10,"shoe canoe warm warn war ward swarm quarter blown grown shown known thrown comb tomb answer")
trap(10,"pass glass brass cast mask task")
trap(11,"listen castle whistle ball tall fall wall small hall call stall picture nature future treasure measure pleasure special station action nation caught taught daughter thought word world worm work")

def cum(level):
    g=set(); cew=set(); split=False
    for l in range(1,level+1):
        g|=set(x for x in ADD[l]["g"] if "!" not in x); cew|=set(ADD[l]["cew"]); split|=ADD[l].get("split",False)
    if level>=10: g|={"y"}
    return g,cew,split

def segs(word,g,split,level):
    """yield graphemes lists for word using allowed graphemes; y only word-initial before Phase 5b."""
    word=word.lower(); n=len(word); out=[]
    ordered=sorted(g,key=lambda x:-len(x))
    def rec(i,acc):
        if i==n: out.append(list(acc)); return
        # split digraph: vowel + consonant grapheme + final e
        if split and word[i] in "aeiou":
            for c in ordered:
                if c in VOW1 or c in ("y",): continue
                j=i+1+len(c)
                if word[i+1:j]==c and j==n-1 and word[j]=="e" and c not in ("qu",):
                    acc.append(word[i]+"-e:"+c); rec(n,acc); acc.pop()
        for gr in ordered:
            if word.startswith(gr,i):
                if gr=="y" and i>0 and level<10: continue
                acc.append(gr); rec(i+len(gr),acc); acc.pop()
    rec(0,[])
    return out

def is_vowel_g(gr):
    return gr in VOW1 or gr in "ai ee igh oa oo ar or ur ow oi ear air ure er ay ou ie ea oy ir ue aw ew oe au ey".split() or "-e:" in gr

def word_ok(word,level):
    raw=word; w=word.lower().strip("'’").replace("’","'")
    if not w: return True,""
    if not w.replace("'","").isalpha(): return False,"non-letter"
    if "'" in w and not (w in CONTRACTIONS or w.endswith("'s")): return False,"apostrophe"
    if w in CONTRACTIONS and level>=6: return True,""
    if "'" in w and level<6: return False,"apostrophe before Phase 4 Mastery"
    w=w.replace("’","'")
    g,cew,split=cum(level)
    cewl={c.lower() for c in cew}
    if w in cewl: return True,""
    if w in TRAPS and TRAPS[w]>level: return False,"taught later / irregular (phase %s)"%TRAPS[w]
    if level<11 and ("tch" in w or "dge" in w or re.match(r"(kn|gn|wr)",w) or w.endswith("mb")): return False,"alternative spelling taught at Phase 5c"
    # silent-e dropped before a suffix (hoping, baking, hoped): reads as a different word
    pat = r"(?<![aeiou])[aeiou][bcdfghjklmnpqrstvxz]" + (r"(ing|ed|er|est)$" if level<8 else r"ing$")
    if re.search(pat,w) and not (w in cewl): return False,"silent-e drop before suffix"
    if level<7 and ("ph" in w or w.startswith("wh")): return False,"ph/wh taught at Phase 5a"
    cands=[(w,"")]
    if level>=6 and w.endswith("'s"): cands.append((w[:-2],"'s"))
    if level>=8 and len(w)>3:
        for suf in ("d","r"):
            if w.endswith(suf) and w[:-1].endswith("e"): cands.append((w[:-1],suf))
        if w.endswith("st") and w[:-2].endswith("e"): cands.append((w[:-2],"st"))
    # suffix/prefix stripping
    for suf,lv in SUFFIX_FROM.items():
        if level>=lv and w.endswith(suf) and len(w)>len(suf)+1:
            cands.append((w[:-len(suf)],suf))
    if level>=6 and w.startswith("un") and len(w)>4: cands.append((w[2:],"un"))
    for base,suf in cands:
        if base in cewl: return True,""
        if not base: continue
        if base in TRAPS and TRAPS[base]>level: continue   # derived forms of later-taught words (smallest, oldest)
        for s in segs(base,g,split,level):
            # open-syllable single vowel (he, go, no) not decodable unless CEW
            if s and s[-1] in VOW1 and len(s)>1 and s[-1]!="a" and not any("-e:" in x for x in s): continue
            if level<=NOADJ_MAX:
                bad=any((not is_vowel_g(s[k])) and (not is_vowel_g(s[k+1])) for k in range(len(s)-1))
                if bad: continue
            if level==5 and sum(1 for x in s if is_vowel_g(x))>1: continue   # Phase 4: one-syllable words only
            # soft c before e/i/y (cell, city) not taught until 5b
            if level<10 and re.search(r"c[eiy]",base): continue
            # vowel digraph + r that makes a different sound (chair, deer, board, door) is taught later
            if any(s[k+1]=="r" and (k+2==len(s) or s[k+2][0] not in "aeiouy") and ((s[k]=="ai" and level<4) or (s[k] in ("ee","oa","oo") and level<11)) for k in range(len(s)-1)): continue
            # o+w, a+w, e+w are the digraphs ow / aw / ew, not two separate sounds (cow, saw, few)
            if any((s[k],s[k+1]) in (("o","w"),) for k in range(len(s)-1)) and level<4: continue
            if any((s[k],s[k+1]) in (("a","w"),("e","w")) for k in range(len(s)-1)) and level<7: continue
            # two single vowel letters side by side (out, eat, boat as o-u-t) are never decoded that way
            if any(s[k] in VOW1 and s[k+1] in VOW1 for k in range(len(s)-1)): continue
            # single vowel + r not followed by a vowel (girl, bird, cart) needs ir/ur/ar/er/or
            if any(s[k] in VOW1 and s[k+1]=="r" and (k+2==len(s) or not (s[k+2][0] in "aeiouy")) for k in range(len(s)-1)): continue
            # silent-e dropped before a suffix (hoping, baking) - reads as a different word
            if suf in ("ing","ed","er","est") and len(s)>=2 and s[-1] not in VOW1 and len(s[-1])==1 and s[-2] in VOW1: continue
            return True,""
    return False,"not decodable at this level"

def check_text(text,level):
    bad=[]
    for tok in re.findall(r"[A-Za-z][A-Za-z'’]*",text):
        ok,why=word_ok(tok,level)
        if not ok: bad.append((tok,why))
    return bad

def word_count(text): return len(text.split())


def first_level(word, top=11):
    """The first level (1-11) at which a word is decodable/taught, or None."""
    for l in range(1, top+1):
        if word_ok(word, l)[0]: return l
    return None

def phase_mix(text, level):
    """Words per first-taught level. Used to make sure a text assesses its own phase (some new words) but is not made
    only of new-phase words, and still draws on earlier phases (cumulative assessment)."""
    toks = re.findall(r"[A-Za-z][A-Za-z'\u2019]*", text)
    fl = [first_level(t) for t in toks]
    return toks, fl

def mix_problems(text, level):
    if level == 1: return []
    toks, fl = phase_mix(text, level)
    new = sum(1 for f in fl if f == level); n = len(toks)
    out = []
    # Phase 5a (all) is deliberately a pure consolidation phase (ADD[9] adds no grapheme/CEW, and
    # no suffix threshold lands on exactly 9 either — see cum()), so no word can ever be "new to
    # this phase". Skip the new-word-count check there; the earlier-phase-mix check below still
    # applies, so a text still has to draw on real content, just none of it introduced at level 9.
    if level != 9 and new < 3: out.append(f"only {new} word(s) taught at this phase (need 3+)")
    if new > 0.4*n: out.append(f"{new} of {n} words are new to this phase (max 40%)")
    earlier = {f for f in fl if f and 2 <= f < level}
    need = 3 if level >= 10 else 2 if level >= 5 else 1 if level >= 3 else 0
    if len(earlier) < need: out.append(f"draws on only {len(earlier)} earlier phase(s) after Phase 2 (need {need}+)")
    return out
