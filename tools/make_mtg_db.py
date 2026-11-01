#!/usr/bin/env python3
"""Costruisce magic.json (stesso formato compatto di cards.json) dal file "Default Cards" di Scryfall.
Uso: make_mtg_db.py <default-cards.json> <output.json> <data AAAA-MM-GG>
Dati: Scryfall (https://scryfall.com/docs/api/bulk-data)."""
import json, sys, collections
src, out, date = sys.argv[1], sys.argv[2], sys.argv[3]
LANG = {"en": "EN", "it": "IT", "de": "DE", "fr": "FR", "es": "ES", "pt": "PT", "ja": "JP", "ko": "KR", "ru": "RU", "zhs": "SC", "zht": "TC"}
RAR = {"common": "Common", "uncommon": "Uncommon", "rare": "Rare", "mythic": "Mythic Rare", "special": "Special", "bonus": "Bonus"}
sets, rars, rsets = collections.OrderedDict(), collections.OrderedDict(), collections.OrderedDict()
def idx(d, k):
    if k not in d: d[k] = len(d)
    return d[k]
byname = collections.OrderedDict()
for c in json.load(open(src, encoding="utf8")):
    if c.get("layout") in ("art_series",) or c.get("digital"): continue
    name = (c.get("name") or "").strip()
    num = str(c.get("collector_number") or "").strip()
    code = (c.get("set") or "").strip().upper()
    if not name or not num or not code: continue
    si = idx(sets, (c.get("set_name") or code).strip())
    r = RAR.get(c.get("rarity") or "", (c.get("rarity") or "").capitalize())
    rs = idx(rsets, tuple(idx(rars, x) for x in ([r] if r else [])))
    lg = LANG.get(c.get("lang") or "en", "EN")
    byname.setdefault(name, []).append([si, code, num, lg + str(rs), c.get("id") or ""])
cards = [[g[0][4], [n], g] for n, g in byname.items()]
if len(cards) < 5000:
    sys.exit("Troppe poche carte (%d): dati incompleti, non scrivo il file." % len(cards))
db = {"v": 1, "date": date, "sets": list(sets), "rar": list(rars), "rs": [list(k) for k in rsets], "cards": cards}
with open(out, "w", encoding="utf8") as f:
    json.dump(db, f, ensure_ascii=False, separators=(",", ":"))
print("cards", len(cards), "sets", len(sets), "rarities", len(rars))
