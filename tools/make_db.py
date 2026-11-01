"""Genera cards.json (elenco carte, stampe, espansioni, rarità) dai dati di DawnbrandBots/yaml-yugi.

Uso: python3 make_db.py <cartella data/cards> <cards.json> <data AAAA-MM-GG>
"""
import json, os, sys, collections
src = sys.argv[1]; out = sys.argv[2]; date = sys.argv[3] if len(sys.argv) > 3 else ""
LANGS = [("en","EN"),("it","IT"),("de","DE"),("fr","FR"),("es","ES"),("pt","PT"),("ja","JP"),("ko","KR"),("zh-CN","SC")]
LK = dict(LANGS)
DEF = {"EN":"EN","IT":"IT","DE":"DE","FR":"FR","ES":"SP","PT":"PT","JP":"JP","KR":"KR","SC":"SC"}
NAME_LANGS = ["en","it","de","fr","es","pt"]
MARKERS = sorted(["EN","E","DE","G","FR","F","IT","I","SP","S","ES","PT","P","JP","J","KR","K","SC","AE","TC"], key=len, reverse=True)
sets = {}; rars = {}; rsets = {}
def idx(d, k):
    if k not in d: d[k] = len(d)
    return d[k]
def split_code(code):
    if "-" in code:
        prefix, rest = code.split("-", 1)
        for m in MARKERS:
            if rest.startswith(m) and len(rest) > len(m):
                return prefix, m, rest[len(m):]
    return "", "", code
cards = []
for fn in sorted(os.listdir(src)):
    if not fn.endswith(".json"): continue
    with open(os.path.join(src, fn), encoding="utf8") as f:
        c = json.load(f)
    nm = c.get("name") or {}
    en = (nm.get("en") or "").strip()
    if not en: continue
    names = [en]
    for l in NAME_LANGS[1:]:
        v = (nm.get(l) or "").strip()
        names.append("" if (not v or v == en) else v)
    while len(names) > 1 and names[-1] == "": names.pop()
    groups = collections.OrderedDict()
    for lk, lv in (c.get("sets") or {}).items():
        if lk not in LK: continue
        L = LK[lk]
        for s in lv or []:
            code = (s.get("set_number") or "").strip().upper()
            if not code: continue
            si = idx(sets, (s.get("set_name") or "").strip())
            rs = idx(rsets, tuple(idx(rars, r) for r in (s.get("rarities") or [])))
            prefix, marker, number = split_code(code)
            ent = L + ("" if (not prefix or marker == DEF[L]) else "~" + marker + "~") + str(rs)
            groups.setdefault((si, prefix, number), []).append(ent)
    if not groups: continue
    cards.append([c.get("password") or 0, names, [[k[0], k[1], k[2], " ".join(v)] for k, v in groups.items()]])
if len(cards) < 5000:
    sys.exit("Troppe poche carte (%d): dati incompleti, non scrivo il file." % len(cards))
db = {"v": 1, "date": date, "sets": list(sets), "rar": list(rars), "rs": [list(k) for k in rsets], "cards": cards}
with open(out, "w", encoding="utf8") as f:
    json.dump(db, f, ensure_ascii=False, separators=(",", ":"))
print("cards", len(cards), "sets", len(sets), "rarities", len(rars), "rarity-sets", len(rsets))
print("size MB", round(os.path.getsize(out)/1e6, 2))
