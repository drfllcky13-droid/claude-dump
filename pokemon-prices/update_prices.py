"""Fetch TCGplayer market prices for the Pokémon card checklist page.

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
    # Gengar
    "base3-5": 106521, "base3-20": 44428, "gym1-14": 88874, "gym2-29": 88875,
    "neo4-6": 84599, "lc-11": 85670, "ecard1-13": 85671, "ecard1-48": 85673,
    "ecard3-10": 85669, "ecard3-H09": 85668, "ex6-108": 85680,
    "ex12-5": 85674, "dp1-27": 85675, "dp7-18": 85676, "pl2-40": 85681,
    "pl4-16": 85677, "pl4-17": 85678, "pl4-97": 85682, "hgss4-94": 85679,
    "xyp-XY166": 125253, "xy4-34": 94167, "xy4-35": 94168, "xy4-114": 94683,
    "xy4-121": 94688, "xy8-60": 107179, "g1-35": 113693, "sm4-38": 149061,
    "sm9-53": 183828, "sm9-164": 183829, "sm9-165": 183830, "sm9-186": 183831,
    "sm10-70": 189170, "swshp-SWSH052": 222072, "swshp-SWSH241": 285257,
    "swsh1-85": 208393, "swsh6-57": 241716, "swsh8-156": 253370,
    "swsh8-157": 253371, "swsh8-271": 253266, "swsh11-066": 283941,
    "swsh11tg-TG06": 284266, "sv03.5-094": 516663, "sv04.5-057": 534419,
    "sv05-104": 542848, "sv05-193": 542914, "mep-073": 696608,
    "me02-056": 660380, "me02.5-125": 675937, "me02.5-284": 676096,
    "me03-050": 684431, "30th-090": 716485, "30th-154": 717610,
    "30th-c-018": 716198,
    # Morpeko
    "swshp-SWSH012": 206428, "swshp-SWSH031": 210579, "swshp-SWSH056": 223757,
    "swshp-SWSH116": 241881, "swshp-SWSH215": 268444, "swshp-SWSH216": 268445,
    "swshp-SWSH217": 268446, "swshp-SWSH218": 268447, "swshp-SWSH287": 477065,
    "swshp-SWSH288": 477066, "swshp-SWSH289": 477067, "swshp-SWSH290": 477068,
    "swsh1-78": 208376, "swsh1-79": 208377, "swsh1-80": 208380,
    "swsh1-190": 208378, "swsh1-204": 208381, "swsh2-73": 213159,
    "swsh4.5-35": 232468, "swsh4.5-36": 232470, "swsh4.5-37": 232475,
    "swsh4.5-38": 232478, "swsh4.5sv-SV044": 232403, "swsh5-98": 234229,
    "swsh8-109": 253267, "swsh8-179": 253393, "swsh9-095": 263813,
    "swsh12-116": 451770, "svp-206": 635456, "sv04-121": 523796,
    "sv04-206": 523887, "sv06-072": 550116, "sv10-137": 632944,
    "me05-055": 704812, "me05-102": 704859, "me05-117": 704874,
    "30th-061": 716460, "30th-135": 716223,
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
    if len(cards) < len(PRODUCTS) * 0.9:
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
