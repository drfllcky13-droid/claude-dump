"""Fetch TCGplayer market prices for the Banette / Mega Attack Rare checklist.

Writes pokemon-prices/prices.json as:
  {"updated": "YYYY-MM-DD", "checked": ISO time of this run,
   "cards": {card_id: {market, reverse, pid}},
   "previous": {"updated": ..., "cards": ...}}
"previous" holds the last snapshot from an earlier day, so the page can
show how each price moved.
"""
import datetime
import json
import pathlib
import sys
import urllib.request

# Checklist card id -> TCGplayer product id.
PRODUCTS = {
    "ex5-1": 83719, "ex14-1": 83720, "ex16-4": 83721, "hgss4-14": 83724,
    "pl1-19": 83723, "dp3-23": 83722, "xy6-31": 98067, "xy6-32": 98068,
    "me05-034": 704791, "sv09-060": 623487, "swsh6-63": 241724,
    "sm7-65": 170886, "sm7-66": 170887, "swsh4-68": 226472,
    "swsh11-073": 283951, "ex12-85": 83725, "sv01-088": 487954,
    "me02.5-091": 675903, "sm7-157": 170888, "sm7-174": 170915,
    "sv01-229": 490087, "me02.5-234": 676046, "sma-SV61": 197810,
    "swsh11tg-TG07": 284267,
    "mep-023": 659612, "mep-032": 685510, "mep-033": 685511,
    "me02.5-265": 676077, "me02.5-266": 676078, "me02.5-267": 676079,
    "me02.5-268": 676080, "me02.5-269": 676081, "me02.5-270": 676082,
    "me02.5-271": 676083,
}
URL = "https://mpapi.tcgplayer.com/v2/product/{}/pricepoints"
OUT = pathlib.Path(__file__).with_name("prices.json")


def fetch(pid):
    req = urllib.request.Request(URL.format(pid), headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=30) as r:
        points = {p["printingType"]: p["marketPrice"] for p in json.load(r)}
    normal, foil = points.get("Normal"), points.get("Foil")
    # Cards with a regular print show it first; their foil is the reverse holo.
    if normal is not None:
        return {"market": normal, "reverse": foil, "pid": pid}
    return {"market": foil, "reverse": None, "pid": pid}


def main():
    cards = {}
    for cid, pid in PRODUCTS.items():
        try:
            cards[cid] = fetch(pid)
        except Exception as e:  # keep going; one bad card shouldn't block the rest
            print(f"failed {cid}: {e}", file=sys.stderr)
    if len(cards) < len(PRODUCTS) - 4:
        sys.exit(f"only got {len(cards)} of {len(PRODUCTS)} prices; not writing")

    now = datetime.datetime.now(datetime.timezone.utc)
    today = now.strftime("%Y-%m-%d")
    old = json.loads(OUT.read_text()) if OUT.exists() else None
    if old and old.get("updated") != today:
        previous = {"updated": old["updated"], "cards": old["cards"]}
    else:
        previous = (old or {}).get("previous")
    OUT.write_text(json.dumps({"updated": today, "checked": now.strftime("%Y-%m-%dT%H:%M:%SZ"),
                               "cards": cards, "previous": previous}, indent=1) + "\n")
    print(f"{today}: {len(cards)} prices")


if __name__ == "__main__":
    main()
