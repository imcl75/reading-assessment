"""Build show/index.html: the OPEN "Show on iPad" reading page.

The teacher's laptop page (Reading Assessment.html, kept in the CLF Staff-Tools library) shows a QR code holding only
which text to show, e.g. https://reading.wallscourt-farm-academy.co.uk/show/?a=fluency&id=31 . The iPad camera opens
this page, which shows that text, large, for the child to read. No pupil data, no sign-in, no calls to any server:
the texts are copied in here from the four teacher tools (only what the child reads: title, words, pictures).

Run after changing any text in fluency/, phonics/, pm-benchmark/ or comprehension/:
    python3 show/build.py
"""
import json, os, re, shutil

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)
VERSION = 'WFA-14.11.26a'


def const(folder, name):
    s = open(os.path.join(REPO, folder, 'index.html'), encoding='utf-8').read()
    m = re.search(r'^const ' + name + r' = (\[.*?\]);\s*$', s, re.M)
    assert m, (folder, name)
    return json.loads(m.group(1))


lv = lambda l: 'F' + str(l - 30) if l > 30 else str(l)
texts = {'fluency': [], 'phonics': [], 'pm_benchmark': [], 'comprehension': []}

for t in const('fluency', 'TEXTS'):
    texts['fluency'].append({'id': str(t['level']), 'level': 'Level ' + lv(t['level']), 'title': t['title'], 'paras': [t['text'].strip()]})

os.makedirs(os.path.join(HERE, 'img'), exist_ok=True)
for lvl in const('phonics', 'DATA'):
    for i, t in enumerate(lvl['texts']):
        imgs = []
        for src in t.get('images') or []:
            m = re.fullmatch(r'img/(p\d+-\d+[ab]\.jpg)(\?v=[0-9a-f]+)?', src)
            assert m, src
            shutil.copyfile(os.path.join(REPO, 'phonics', 'img', m.group(1)), os.path.join(HERE, 'img', m.group(1)))
            imgs.append('img/' + m.group(1) + (m.group(2) or ''))
        texts['phonics'].append({'id': '%d-%d' % (lvl['level'], i), 'level': lvl['name'], 'title': t['title'], 'paras': [t['text'].strip()], 'images': imgs})

for lvl in const('pm-benchmark', 'DATA'):
    for t in lvl['texts']:
        texts['pm_benchmark'].append({'id': t['id'], 'level': 'Level %d · %s' % (t['level'], t.get('colour') or ''), 'title': t['title'],
                                      'paras': [' '.join(p['lines']) for p in t['pages']]})

for lvl in const('comprehension', 'DATA'):
    for t in lvl['texts']:
        texts['comprehension'].append({'id': t['id'], 'level': 'Level ' + lv(t['level']), 'title': t['title'], 'paras': list(t['text'])})

for k, v in texts.items():
    ids = [t['id'] for t in v]
    assert len(ids) == len(set(ids)), (k, 'ids must be unique')
    assert v, k

data = json.dumps(texts, ensure_ascii=False, separators=(',', ':')).replace('<', '\\u003c')
page = open(os.path.join(HERE, 'template.html'), encoding='utf-8').read()
assert page.count('/*@@TEXTS@@*/null') == 1
page = page.replace('/*@@TEXTS@@*/null', data).replace('@@VERSION@@', VERSION)
assert '@@' not in page
assert 'fetch(' not in page and 'XMLHttpRequest' not in page and '/_api' not in page
assert not re.search(r'<(script|link)[^>]+(src|href)="https?://', page), 'no external loads'
open(os.path.join(HERE, 'index.html'), 'w', encoding='utf-8').write(page)
print('wrote show/index.html', len(page.encode()), 'bytes;', {k: len(v) for k, v in texts.items()}, 'pictures', len(os.listdir(os.path.join(HERE, 'img'))))
