import sys
from levels import check_text, word_count
from texts_src import B
tot=bad=0
for lv,items in B.items():
    for i,(title,text,qs) in enumerate(items,1):
        tot+=1
        f=check_text(text,lv); n=word_count(text)
        if f or len(qs)!=3 or not any(q[0]=="why" for q in qs):
            bad+=1; print(f"L{lv}.{i} {title!r} ({n}w):",[(w,y[:22]) for w,y in f])
        elif "-v" in sys.argv: print(f"L{lv}.{i} ok {n}w")
print("texts:",tot,"with problems:",bad)
print({lv:[word_count(t[1]) for t in items] for lv,items in B.items()})
