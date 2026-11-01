#!/usr/bin/env python3
"""Costruisce pokemon.json (stesso formato compatto di cards.json) da PokemonTCG/pokemon-tcg-data.
Uso: make_pkm_db.py <cartella pokemon-tcg-data> <output.json> <data AAAA-MM-GG>
Dati: PokemonTCG/pokemon-tcg-data (licenza MIT)."""
import json, os, sys, collections
src, out, date = sys.argv[1], sys.argv[2], sys.argv[3]
sets_meta = {s["id"]: s for s in json.load(open(os.path.join(src, "sets", "en.json"), encoding="utf8"))}
sets, rars, rsets = collections.OrderedDict(), collections.OrderedDict(), collections.OrderedDict()
def idx(d, k):
    if k not in d: d[k] = len(d)
    return d[k]
byname = collections.OrderedDict()
cdir = os.path.join(src, "cards", "en")
for fn in sorted(os.listdir(cdir)):
    if not fn.endswith(".json"): continue
    sid = fn[:-5]
    meta = sets_meta.get(sid, {})
    for c in json.load(open(os.path.join(cdir, fn), encoding="utf8")):
        name = (c.get("name") or "").strip()
        num = str(c.get("number") or "").strip()
        if not name or not num: continue
        prefix = (meta.get("ptcgoCode") or sid).upper()
        si = idx(sets, (meta.get("name") or sid).strip())
        rs = idx(rsets, tuple(idx(rars, r) for r in ([c["rarity"]] if c.get("rarity") else [])))
        byname.setdefault(name, []).append([si, prefix, num, "EN" + str(rs), c.get("id") or (sid + "-" + num)])
cards = []
for name, groups in byname.items():
    cards.append([groups[0][4], [name], groups])
if len(cards) < 2000:
    sys.exit("Troppe poche carte (%d): dati incompleti, non scrivo il file." % len(cards))
db = {"v": 1, "date": date, "sets": list(sets), "rar": list(rars), "rs": [list(k) for k in rsets], "cards": cards}
with open(out, "w", encoding="utf8") as f:
    json.dump(db, f, ensure_ascii=False, separators=(",", ":"))
print("cards", len(cards), "sets", len(sets), "rarities", len(rars), "size MB", round(os.path.getsize(out) / 1e6, 2))
