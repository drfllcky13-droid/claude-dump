"""Fetch TCGplayer market prices for the Pokémon card checklist page.

Writes pokemon-prices/prices.json as:
  {"updated": "YYYY-MM-DD", "checked": ISO time of this run,
   "cards": {card_id: {market, reverse, pid, listed?}},
   "previous": {"updated": ..., "cards": ...}}
"previous" holds the last snapshot from an earlier day, so the page can
show how each price moved.
"""
import concurrent.futures
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
# Booster packs: "pack-<product id>".
PRODUCTS.update({f"pack-{pid}": pid for pid in [
    138132, 138131, 138130, 138128, 138129, 138133, 138134, 138149,
    138136, 138135, 138137, 138138, 138140, 138139, 138141, 138142,
    138144, 138143, 138145, 138146, 138148, 138147, 138150, 138151,
    138152, 138153, 98558, 98565, 98519, 98550, 98595, 98946,
    98578, 98562, 98546, 98577, 98944, 98557, 98522, 98566,
    98533, 98529, 98525, 98561, 98569, 98545, 98585, 98537,
    98589, 98591, 98542, 98574, 98594, 98530, 98582, 98586,
    98534, 98515, 98553, 98549, 98570, 98538, 98521, 98541,
    98948, 98554, 98526, 98517, 98573, 98581, 91602, 91595,
    92169, 94622, 97751, 229226, 129906, 100490, 107666, 111279,
    187238, 168114, 130013, 129907, 129385, 129889, 133774, 155880,
    146996, 155662, 164297, 170274, 173392, 175510, 181699, 187239,
    185718, 191883, 198634, 199263, 206028, 210562, 216852, 218789,
    221312, 232636, 229276, 236257, 244337, 248577, 247646, 256124,
    265521, 274421, 277325, 283388, 453466, 476451, 493976, 501256,
    504467, 512822, 528038, 532841, 543843, 552997, 557331, 565604,
    593294, 610935, 624683, 630434, 630699, 644352, 654144, 672434,
    672398, 684446, 692944, 696613, 704192, 712099, 141227, 141228,
    190532, 190533, 190534, 141229, 190535, 190536, 190537, 189810,
    190359, 190360, 231300, 231299, 231304, 231305, 231301, 231306,
    231303, 231302, 232748, 232770, 282530, 280301, 482138, 488324,
    517551, 551628, 577596, 639713, 649191, 670914, 704373, 530756,
    505945, 516527, 579930, 615609, 694977, 701484, 701485,
]})
URL = "https://mpapi.tcgplayer.com/v2/product/{}/pricepoints"
HISTORY_URL = "https://infinite-api.tcgplayer.com/price/history/{}/detailed?range=annual"
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/128 Safari/537.36",
    "Origin": "https://www.tcgplayer.com",
    "Referer": "https://www.tcgplayer.com/",
}
OUT = pathlib.Path(__file__).with_name("prices.json")
HISTORY_OUT = pathlib.Path(__file__).with_name("history.json")


def get_json(url):
    with urllib.request.urlopen(urllib.request.Request(url, headers=HEADERS), timeout=30) as r:
        return json.load(r)


def fetch(pid):
    data = get_json(URL.format(pid))
    points = {p["printingType"]: p["marketPrice"] for p in data}
    listed = next((p["listedMedianPrice"] for p in data if p["printingType"] == "Normal"), None)
    normal, foil = points.get("Normal"), points.get("Foil")
    # Cards with a regular print show it first; their foil is the reverse holo.
    if normal is not None:
        return {"market": normal, "reverse": foil, "pid": pid}
    if foil is not None:
        return {"market": foil, "reverse": None, "pid": pid}
    # Rare old sealed packs often have no recent sales, only listings.
    return {"market": None, "reverse": None, "listed": listed, "pid": pid}


def fetch_history(pid):
    """A year of weekly market prices, oldest first: {"start", "m"[, "r"]}.

    "m" is the main printing (Near Mint, or Unopened for sealed product);
    "r" is the reverse holo when the card has one.
    """
    series = {}
    for row in get_json(HISTORY_URL.format(pid)).get("result") or []:
        if row["condition"] not in ("Near Mint", "Unopened"):
            continue
        buckets = sorted(row["buckets"], key=lambda b: b["bucketStartDate"])
        prices = [round(float(b["marketPrice"]), 2) or None for b in buckets]
        series[row["variant"]] = (buckets[0]["bucketStartDate"] if buckets else None, prices)
    if not series:
        return None
    main_variant = "Normal" if "Normal" in series else next(
        (v for v in series if v != "Reverse Holofoil"), next(iter(series)))
    start, prices = series[main_variant]
    out = {"start": start, "m": prices}
    if main_variant == "Normal" and "Reverse Holofoil" in series:
        out["r"] = series["Reverse Holofoil"][1]
    return out


def update_history(today):
    """Refresh the weekly history at most once every 6 days."""
    old = json.loads(HISTORY_OUT.read_text()) if HISTORY_OUT.exists() else {}
    if old.get("updated") and (datetime.date.fromisoformat(today)
                               - datetime.date.fromisoformat(old["updated"])).days < 6:
        return
    items = {}

    def one(item):
        cid, pid = item
        try:
            return cid, fetch_history(pid)
        except Exception as e:
            print(f"history failed {cid}: {e}", file=sys.stderr)
            return cid, (old.get("items") or {}).get(cid)

    with concurrent.futures.ThreadPoolExecutor(6) as pool:
        for cid, h in pool.map(one, PRODUCTS.items()):
            if h:
                items[cid] = h
    HISTORY_OUT.write_text(json.dumps({"updated": today, "items": items}, separators=(",", ":")) + "\n")
    print(f"{today}: history for {len(items)} items")


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
    update_history(today)


if __name__ == "__main__":
    main()
