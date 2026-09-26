"""Generates the supporting pictures for the KS1 phonics texts with Replicate (Flux 2 Pro).
Usage:  python3 -B gen_images.py pilot      # a small spread of pictures to check the style
        python3 -B gen_images.py all        # every text that does not have a picture yet
        python3 -B gen_images.py 7-3 9-0    # specific pictures ("<phase>-<text number from 0>"), regenerated even if present
Briefs come from img_briefs_*.json (written to show the scene without giving away the answers).
Pictures are saved as img/p<phase>-<n>.jpg (optimised for the web); the originals go to img_originals/ (git-ignored)."""
import os, re, sys, json, glob, time, pathlib, io, concurrent.futures as cf, urllib.request
import replicate
from PIL import Image

here = pathlib.Path(__file__).parent
os.environ["REPLICATE_API_TOKEN"] = open(os.path.expanduser("~/replicate_token.txt")).read().strip()
MODEL = "black-forest-labs/flux-2-pro"
STYLE = ("Friendly flat vector children's picture-book illustration, soft rounded shapes, bright clear colours, "
         "plain pale background, simple uncluttered composition with one clear focal point. "
         "No text, no letters, no numbers, no signs, no speech bubbles, no watermark.")
# one visible disability per picture with children, rotated (diversity rule); prosthetics described as natural and everyday
SKIN = ["deep brown skin", "light brown skin", "pale skin", "olive skin", "medium brown skin", "warm tan skin"]
POOL = ["a child with a shorter left arm, joining in naturally", "a child wearing a hearing aid on one ear",
        "a child using a manual wheelchair, joining in naturally", "a child with a flesh-coloured prosthetic lower arm, natural and well-fitted",
        "a child with thick prescription glasses", "a child on forearm crutches", "a child with leg braces visible below their trousers",
        "a child with Down's syndrome, part of the scene naturally", "a child with a cochlear implant processor visible behind one ear",
        "a child with vitiligo visible on their face and hands, joining in naturally", "a child with one hand, joining in naturally",
        "a child of noticeably shorter stature, joining in naturally"]

def briefs():
    out = []
    for f in sorted(glob.glob(str(here / "img_briefs_*.json"))): out += json.load(open(f))
    out.sort(key=lambda b: (b["phase"], b["idx"])); return out

def full_prompt(b, n):
    p = b["prompt"].rstrip(". ") + ". " + STYLE
    p += " Draw only the characters described in the scene and no other people or animals; do not add a crowd."
    if b.get("has_children"):
        plural = re.search(r"\\b(two|three|four|children|friends|pair|group|siblings|classmates)\\b", b["prompt"].lower())
        who = POOL[n % len(POOL)]
        if plural:
            p += f" Give the children different skin tones and features; one of them is {who}, drawn simply and respectfully as an ordinary child."
        else:
            p += f" There is exactly one child, with {SKIN[n % len(SKIN)]}, who is {who}, drawn simply and respectfully as an ordinary child."
    return p

def generate(b, n):
    key = f'{b["phase"]}-{b["idx"]}'
    for attempt in range(3):
        try:
            out = replicate.run(MODEL, input={"prompt": full_prompt(b, n), "aspect_ratio": "3:2", "output_format": "jpg", "output_quality": 92})
            data = out.read() if hasattr(out, "read") else urllib.request.urlopen(str(out[0] if isinstance(out, list) else out)).read()
            (here / "img_originals").mkdir(exist_ok=True); (here / "img_originals" / f"p{key}.jpg").write_bytes(data)
            im = Image.open(io.BytesIO(data)).convert("RGB"); im.thumbnail((900, 600))
            (here / "img").mkdir(exist_ok=True); im.save(here / "img" / f"p{key}.jpg", "JPEG", quality=80, optimize=True)
            return key, "ok"
        except Exception as e:
            err = str(e)[:150]; time.sleep(8 * (attempt + 1))
    return key, "FAILED: " + err

if __name__ == "__main__":
    mode = sys.argv[1] if len(sys.argv) > 1 else "pilot"
    B = briefs(); index = {(b["phase"], b["idx"]): (n, b) for n, b in enumerate(B)}
    if mode == "pilot": todo = [index[k] for k in [(1,0),(3,2),(5,1),(6,3),(8,4),(10,2)] if k in index]
    elif mode == "all": todo = [v for k, v in index.items() if not (here / "img" / f"p{k[0]}-{k[1]}.jpg").exists()]
    else: todo = [index[tuple(map(int, a.split("-")))] for a in sys.argv[1:]]
    print(len(todo), "pictures to generate", flush=True)
    with cf.ThreadPoolExecutor(4) as ex:
        for key, status in ex.map(lambda t: generate(t[1], t[0]), todo): print(key, status, flush=True)
