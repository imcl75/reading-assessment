"""Per-text character renames applied AFTER the qa patches, so the patch files (which match on the
original wording) keep working. Added 22.10.26 to stop first names repeating across texts.
Each entry: text id -> {old name: new name}. Applied to every string in the test (passage,
questions, answers, mark-scheme guidance)."""
import re

RENAMES = {
    # Kofi kept in 23-1 (The Piano Tuner)
    "18-3": {"Kofi": "Kojo"},
    "20-1": {"Kofi": "Jonah", "Priya": "Tamsin"},
    "29-2": {"Kofi": "Yaw"},
    # Amara kept in 27-1 (Fog on Carrow Ridge)
    "18-2": {"Amara": "Freya"},
    "22-1": {"Amara": "Nia"},
    "28-5": {"Amara": "Leila"},
    "34-1": {"Amara": "Lena"},
    # Callum kept in 32-3 (A Piece Out of Place)
    "21-3": {"Callum": "Elliot"},
    "24-2": {"Callum": "Rohan"},
    "29-4": {"Callum": "Declan"},
    "30-4": {"Callum": "Felix", "Priya": "Rosa"},
    # Priya kept in 25-1 (The Final Leg)
    "32-3": {"Priya": "Imogen"},
    # Ravi kept in 21-1 (The Bookshop on Chapel Lane)
    "22-3": {"Ravi": "Hassan"},
    "26-1": {"Ravi": "Theo"},
}

def _sub(v, pats):
    if isinstance(v, str):
        for p, new in pats:
            v = p.sub(new, v)
        return v
    if isinstance(v, list):
        return [_sub(x, pats) for x in v]
    if isinstance(v, dict):
        return {k: _sub(x, pats) for k, x in v.items()}
    return v

def apply_renames(tests):
    for t in tests:
        m = RENAMES.get(t["id"])
        if not m:
            continue
        pats = [(re.compile(r"\b%s\b" % re.escape(o)), n) for o, n in m.items()]
        for k in list(t):
            if k != "id":
                t[k] = _sub(t[k], pats)
