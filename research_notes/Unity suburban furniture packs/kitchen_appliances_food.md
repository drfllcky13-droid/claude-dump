# Kitchen Furniture, Household Appliances & Food Packaging / Grocery Props (Unity Asset Store)

Method note: every "verified" figure below was taken from the live assetstore.unity.com product page on 2026-10-03, by reading the store's embedded product JSON (fields: price/originalPrice + discount, rating average/count, reviewCount, supportedUnityVersions, srps, currentVersion name/date, aiDescription). How to read the fields:
- **Rating "hidden (n)"**: the store returns `average: 0` when a pack has fewer than about 3 ratings. Such packs effectively show no star score, so n is the number of ratings only.
- **SRP field**: "standard" = Built-in, "lightweight" = URP, "hd" = HDRP. These are the pipelines the publisher ticked for the *upload* version listed. A pack can also work in other versions.
- **AI field**: the store's "Created with AI" disclosure text (`aiDescription`). It was **empty for every pack below**. For calibration, the same page data contained a populated disclosure for a different pack (American Suburb Top-Down Pack, 395606), so the field does work.
- **Prices**: no pack below had an active discount at fetch time (discount = 0%). A sitewide "Autumn Sale" banner was present on the store, but none of these items were in it.
- No forum or Reddit quality opinions were collected (see Gaps).

## Which kitchen / appliance packs are most realistic and best reviewed? American-style vs European?

### Takeaway
No kitchen or appliance pack in this niche has a meaningful review base. The best-rated is POLYBOX "Kitchen Pack" (5 stars, 13 ratings), a small baked-lighting scene kit rather than a lootable-appliance set. The strongest *appliance* candidates for a US suburb are:
- **32cm "Kitchen Appliances Pack"**: the only pack that explicitly includes "American fridges", plus washing machines. 4K PBR, URP+HDRP, 2026.
- **Bendylab "Home Appliances v1"**: 4K, Built-in/URP/HDRP, color/dirt shader.
- **Kraffing Fridge/Kitchen Packs**: Built-in+URP, updated in 2026.
- **Dekogon "Kitchen Props" VOL.1–7 / MEGA PACK**: "AAA realistic" claim and the largest volume (940 assets), but last updated in 2020 on Unity 2019.3.

For base cabinets in US sizing, the old Immerse Interactive packs use 24"/36" cabinets but are from 2015–16 and Built-in-era.

### Cited Findings

**32cm – Kitchen Appliances Pack (verified)**
- URL: https://assetstore.unity.com/packages/3d/props/electronics/kitchen-appliances-pack-356008
- Price and rating: $29.99 regular, no sale. 0 ratings.
- Unity and pipelines: upload on 2021.3.45f2, SRP tags "standard, custom". The description says "Works with URP and HDRP".
- Version: v1.0, 2026-02-05.
- Contents: 2 American fridges, 2 fridges, 2 freezers, 3 washing machines, kettle, 2 microwaves, 2 blenders, 2 toasters, 3 coffee machines. 53 prefabs, 217 textures at 4096 px (Albedo, Normal, Metal, Rough, AO, Emissive, HDRP mask).
- Tris: American fridges 6k/7k, washers 3.5k–12k, microwaves ~1k, small appliances up to 60k (toaster, blender), kettle 50k.
- LODs: not stated. No AI label.
- No range, dishwasher or dryer.
- [Store page](https://assetstore.unity.com/packages/3d/props/electronics/kitchen-appliances-pack-356008)

**32cm – Washing Machine Set 3 (verified)**
- URL: https://assetstore.unity.com/packages/3d/props/furniture/washing-machine-set-3-336032
- Price and rating: $4.99. 0 ratings.
- Unity and pipelines: 2021.3.34f1, Built-in/URP/HDRP/custom.
- Version: v1.0, 2025-10-23.
- Contents: 1 washer, 3.5k tris, 4096 PBR, 3 texture sets. LODs not stated. No AI label.
- [Store page](https://assetstore.unity.com/packages/3d/props/furniture/washing-machine-set-3-336032)

**Bendylab Studios – Home Appliances v1 (verified)**
- URL: https://assetstore.unity.com/packages/3d/props/electronics/home-appliances-v1-339504
- Price and rating: $21.00. 0 ratings.
- Unity and pipelines: 2021.3.45f2, Built-in/URP/HDRP.
- Version: v1.0, 2025-11-14.
- Contents: 17 meshes, 75 prefabs, 50 textures at 4096. Tris 76–3,756.
- Features: color-adjustable mask material and a "dirt generator" per asset, useful for an abandoned look.
- LODs not stated. No AI label.
- Exact appliance list not given in the text. A search snippet says fridge, dishwasher, microwave, coffee machine and vacuum (unverified).
- [Store page](https://assetstore.unity.com/packages/3d/props/electronics/home-appliances-v1-339504)

**Kraffing – Kitchen Pack V1 (verified)**
- URL: https://assetstore.unity.com/packages/3d/props/kitchen-pack-v1-kitchen-appliance-game-ready-pbr-built-in-urp-co-374178
- Price and rating: $12.99. 0 ratings.
- Unity and pipelines: 2022.3.62f3, Built-in+URP.
- Version: v1.0.0, 2026-06-23.
- Contents: 20 meshes/prefabs, 35.5k polys total, 2048 PBR (Base, AO, Height, Metal, Normal, Rough), 4 color variations. No AI label.
- [Store page](https://assetstore.unity.com/packages/3d/props/kitchen-pack-v1-kitchen-appliance-game-ready-pbr-built-in-urp-co-374178)

**Kraffing – Kitchen PackV2 (verified)**
- URL: https://assetstore.unity.com/packages/3d/props/electronics/kitchen-packv2-kitchens-appliance-game-ready-pbr-built-in-urp-co-271428
- Price and rating: $12.99. 0 ratings.
- Unity and pipelines: 2022.3.56f1, Built-in+URP.
- Version: v1.0.0, 2026-03-19.
- Contents: 20 meshes, 27.5k polys total, 2048 PBR. No AI label.
- [Store page](https://assetstore.unity.com/packages/3d/props/electronics/kitchen-packv2-kitchens-appliance-game-ready-pbr-built-in-urp-co-271428)

**Kraffing – single fridges and Vol. 3 (verified)**
- Fridge V1: $6.99, 7.6k polys, 2022.3.62 Built-in+URP, v1.0.1, 2026-04-21.
- Fridge V2: $6.99, 11.2k polys, v1.0.0, 2025-12-16.
- PBR Asset – Kitchen Pack Vol. 3: $8.99, 2021.3.16 Built-in only, 2024-01-17.
  - Contents: stove, dishwasher, fridge, hood, microwave, with interior detail. Up to 2K textures.
  - Heavy: dishwasher 42k tris, stove 45k tris.
- [Fridge V1](https://assetstore.unity.com/packages/3d/props/fridge-v1-kitchen-appliance-game-ready-pbr-built-in-urp-compatib-328248); [Fridge V2](https://assetstore.unity.com/packages/3d/props/electronics/fridge-v2-kitchen-appliance-game-ready-pbr-built-in-urp-compatib-347900); [Vol.3](https://assetstore.unity.com/packages/3d/props/electronics/pbr-asset-kitchen-pack-vol-3-272350)

**Dekogon Studios – Kitchen Props VOL.1 – 7 MEGA PACK (verified)**
- URL: https://assetstore.unity.com/packages/3d/props/kitchen-props-vol-1-7-mega-pack-178154
- Price and rating: $199.99. Rating hidden (1 rating, 1 review).
- Unity and pipelines: 2019.3.15f1, tagged Built-in/URP/HDRP. The description says "Universal Rendering Pipeline".
- Version: v1.0, 2020-09-07 (no update since). 940 assets, 1.09 GB.
- Description: "100+ Prefab Assets", "most 2048 pixels +", "realistic AAA quality visuals".
- No poly or LOD data, no item list. No AI label.
- Individual volumes:
  - VOL.1: $29.99, 60 prefabs.
  - VOL.3: $39.99, 34 prefabs.
  - VOL.5: $39.99, 32 prefabs.
  - VOL.7: $39.99, 14 prefabs.
  - All are v1.0 from 2020-09-04 with 0 ratings.
- [MEGA](https://assetstore.unity.com/packages/3d/props/kitchen-props-vol-1-7-mega-pack-178154); [VOL.1](https://assetstore.unity.com/packages/3d/props/kitchen-props-vol-1-178147); [VOL.3](https://assetstore.unity.com/packages/3d/props/kitchen-props-vol-3-178152); [VOL.5](https://assetstore.unity.com/packages/3d/props/kitchen-props-vol-5-178148); [VOL.7](https://assetstore.unity.com/packages/3d/props/kitchen-props-vol-7-178153)

**Dekogon – Retro Mid Century Mod Props VOL.3 – Kitchen Furniture (verified)**
- Price and rating: $39.99. Rating hidden (1 rating).
- Unity and pipelines: 2019.4.16, Built-in only. Version v1.0, 2020-12-21.
- Description: "all branding and labels are custom made" (legally safe); channel-packed R/M/AO; most textures 2048+.
- 1950s styling, so it is a poor fit for a present-day suburb.
- [Store page](https://assetstore.unity.com/packages/3d/props/furniture/retro-mid-century-mod-props-vol-3-kitchen-furniture-126178)

**POLYBOX – Kitchen Pack (verified)**
- URL: https://assetstore.unity.com/packages/slug/kitchen-pack-38322
- Price and rating: $39.99. **5 stars, 13 ratings** (5 reviews).
- Unity and pipelines: supported 2018.2, 2019.1, **6000.3.2**. SRP tag Built-in only.
- Version: **v10.0, 2026-05-26** (first published 2015).
- Contents: "photo-real & modern kitchen", 28 assets, whole pack under 16k tris, baked Mental Ray lightmaps (relighting is needed if the scene changes).
- Better suited as a mobile/VR showcase scene than as modular lootables. No AI label.
- [Store page](https://assetstore.unity.com/packages/slug/kitchen-pack-38322)

**Frogbytes – Realistic Kitchen Appliances Pack (verified)**
- URL: https://assetstore.unity.com/packages/slug/realistic-kitchen-appliances-pack-131344
- Price and rating: $17.99. 5 stars, 3 ratings.
- Unity and pipelines: Unity 5.5.1 only, no SRP listed. Version v1.0, 2019-02-12.
- Contents: 2 fridges, gas + induction oven, wall oven, hood, rice cooker, dishwasher, 2 sinks. Mostly 4096 PBR. Doors, buttons and drawers are separate with pivots.
- Looks European (built-in wall oven, rice cooker). No AI label.
- [Store page](https://assetstore.unity.com/packages/slug/realistic-kitchen-appliances-pack-131344)

**Frogbytes – Realistic Kitchen Pack! (verified)**
- Price and rating: $14.99. 5 stars, 6 ratings.
- Unity and pipelines: Unity 5.0.1/5.5.1. Version v1.1, 2017-09-05.
- Contents: microwaves, kettle, toaster, blender, pots and pans, utensils, jars. Mostly 2048 PBR. No AI label.
- [Store page](https://assetstore.unity.com/packages/3d/props/interior/realistic-kitchen-pack-80277)

**Boxx-Games Assets – Kitchen – Cabinets and Appliances (verified)**
- Price and rating: $8.00. 0 ratings.
- Unity and pipelines: 2021.3.16/2021.3.24, Built-in + URP. Version v1.1.0, 2023-05-03.
- Contents: 129 models, 626 prefabs, 184 texture sets at 2048 (Albedo, AO, Metal, Normal), 39.8k tris across all models.
- Interactivity: all cabinet doors and drawers open, microwave opens. The page suggests cabinets as "a hiding place for collectible items", which suits looting.
- Demo has 6 kitchen rooms. LODs not stated. No AI label.
- [Store page](https://assetstore.unity.com/packages/3d/props/interior/kitchen-cabinets-and-appliances-244135)

**Omniia – 2 styles 1 modular kitchen (verified)**
- Price and rating: $10.99. 0 ratings.
- Unity and pipelines: 2021.3.30, URP only. Version 2023-11-24.
- Contents: 86 meshes, LODs No, 2048 textures, opening doors and drawers, 2 fridges, microwave, air fryer. No AI label.
- [Store page](https://assetstore.unity.com/packages/3d/environments/2-styles-1-modular-kitchen-270751)

**Immerse Interactive – Kitchen Appliances / Modern Kitchen and Bathroom: Cabinets and Sinks (verified)**
- Kitchen Appliances: $65.00, Unity 5.1, 2015. Contents: fridge, dishwasher, microwave, cooktop/stove, oven, double oven, in black/white/brushed metal.
- Cabinets and Sinks: $125.00, Unity 5.2, 2016. Contents: base cabinets in **24-inch and 36-inch** widths (US sizing), wall cabinets in 12/24/36 inch, crown molding.
- Both have hidden ratings (1 rating each). No AI label.
- [Appliances](https://assetstore.unity.com/packages/slug/kitchen-appliances-50143); [Cabinets](https://assetstore.unity.com/packages/3d/modern-kitchen-and-bathroom-cabinets-and-sinks-51207)

**Robot Skeleton – Kitchen Appliances with Packaging (verified)**
- Price and rating: $9.99. Rating hidden (2 ratings).
- Unity and pipelines: 2020.3, Built-in. Version v1.1, 2021-03-25.
- Contents: coffee machine, espresso machine, kettle, microwave, stand mixer, toaster, with retail boxes. 12–1,802 tris, 4096 maps.
- [Store page](https://assetstore.unity.com/packages/3d/props/electronics/kitchen-appliances-with-packaging-155472)

**Other packs checked (verified)**
- Helix Studio "Kitchen Equipment PBR" (154832): $16.99, Unity 5.6/2018.2, 9 prefabs, 1.6k–41k tris, 2k textures, LODs none, doors open.
- Kerimcan Uyanik "Modular Kitchen Pack" (372024): $15, Unity 6000.3.10 Built-in/URP, but **stylized** single-atlas albedo only, so it is excluded on style.
- [Helix](https://assetstore.unity.com/packages/3d/props/interior/kitchen-equipment-pbr-154832); [Kerimcan](https://assetstore.unity.com/packages/3d/props/interior/modular-kitchen-pack-372024)

### Inferences
- No current kitchen or appliance pack combines everything we want: US-style range plus top-freezer or French-door fridge, washer *and* dryer, LODs, Unity 6 URP, and a real review base. Expect to mix packs:
  - 32cm for American fridges and washers.
  - Bendylab for dirt and variation shaders.
  - Boxx-Games or Immerse for openable cabinets in US sizes.
- A dryer, a freestanding US slide-in range and a dishwasher in a URP 2025+ pack were not found together. Kraffing Vol.3 has a dishwasher and stove, but it is Built-in only and heavy at 42–45k tris.
- Dekogon's "AAA" packs have never been updated since 2020. URP materials from 2019.3 should upgrade to Unity 6 URP, but this is not listed by the publisher.
- Several 2025–26 packs (32cm, Kraffing, Bendylab) have zero ratings, so quality can only be judged from screenshots.

### Gaps
- Exact item lists for Dekogon Kitchen Props VOL.1–7: the store pages give only prefab counts, and dekogon.com/shop did not list contents. It is unknown whether they include fridges or ranges or only small props.
- LOD presence is not stated for 32cm, Bendylab, Kraffing or Dekogon.
- No pack was found that is explicitly a US "top-freezer" or "French-door" fridge or a US freestanding range. Only 32cm uses the word "American fridge".
- Publishers named in the brief that were not checked: Next Level 3D, Lowlypoly, Kobra Game Studios, Alexandr Voevodov, Rarebyte, NOT_Lonely. No kitchen packs from them surfaced in searches, and none were verified.

## Which food packaging / grocery / supermarket prop packs are realistic and close-up quality?

### Takeaway
For first-person close-ups, the best-documented realistic food packs are:
- **Phoenix3D "P3D: Survival Canned Food and Snacks"**: 50+ items, up to 4K, LOD0/LOD1 listed, all pipelines, aimed at survival games.
- **3D Division Studios canned-food packs**: 4K/2K/1K by size, 3 LODs, 4 can states from sealed to open-empty, explicitly AI-free labels, released Sept 2026.
- **PijayArt Survival Foods / Survival Bundle**: 1K–4K, Built-in+URP, no LODs.

Larger store-scale sets include:
- Dekogon "Shopping and Market VOL 2 – Grocery Store": fixtures, not food.
- 3D Everything "Convenience Store": Unity 6000.0.56, but low-poly and 1024 textures.
- Mixall "Grocery store – parking and supermarket": 941 prefabs, 3 stars from 4 ratings.
- Cybernetic Walrus "Grocery Store Furniture Pack Vol. 1": LODs, collisions, all pipelines; fixtures only.

None of these packs has a meaningful review count.

### Cited Findings

**Phoenix3D Studio – P3D: Survival Canned Food and Snacks (verified)**
- URL: https://assetstore.unity.com/packages/3d/props/p3d-survival-canned-food-and-snacks-312545
- Price and rating: $17.97. 0 ratings.
- Unity and pipelines: 2022.3.55f1, Built-in/URP/HDRP. Version v1.0, 2025-03-04. 284 MB.
- Contents: "50+ unique models of canned goods, chips, biscuits, instant noodles", drink bottles and cans, water bottles, a vending machine and a shop fridge.
- Textures: Albedo/Normal/Rough/Metal "up to 4K".
- **LODs listed**: e.g. Canned Food 1 has LOD0 2,156 / LOD1 644 tris; Drink Can 1 has 1,530 / 533; vending machine 9,321 / 1,398.
- Claims a "3-year update guarantee". No AI label.
- [Store page](https://assetstore.unity.com/packages/3d/props/p3d-survival-canned-food-and-snacks-312545)

**3D Division Studios – Canned Food – Fruits and Vegetables – PBR Game Ready (verified)**
- URL: https://assetstore.unity.com/packages/3d/props/food/canned-food-fruits-and-vegetables-pbr-game-ready-401732
- Price and rating: $9.99. 0 ratings.
- Unity and pipelines: 2022.3.59f1, **URP + HDRP** (Shader Graph). Version v1.0, **2026-09-01**.
- Contents: 5 foods (corn, fruit cocktail, peach, peas, pineapple), each in 4 states (closed, open with lid, open no lid, empty). 20 prefabs, 1,148–1,686 polys.
- Technical: "LODs: Yes, 3 LODs", custom collisions, ORM packing, texel density 10.24 ("AAA standard for FPS").
- Page states "Handcrafted, AI-free textures and logos". No AI label.
- [Store page](https://assetstore.unity.com/packages/3d/props/food/canned-food-fruits-and-vegetables-pbr-game-ready-401732)

**3D Division Studios – Canned Food – Fishes – PBR Game Ready (verified)**
- Price and rating: $9.99. 0 ratings.
- Unity and pipelines: 2022.3.59, URP+HDRP. Version v1.0, 2026-09-01.
- Contents: sardine, anchovy, salmon and tuna in 4 states. 16 prefabs, 276–1,136 polys, 3 LODs, same texture spec as above, AI-free claim.
- [Store page](https://assetstore.unity.com/packages/3d/props/food/canned-food-fishes-pbr-game-ready-401196)

**PijayArt – Survival Foods Package (verified)**
- Price and rating: $9.99. 0 ratings.
- Unity and pipelines: 2018.4.30 + 2021.3.45 (URP). Version 2025-08-07.
- Contents: 25 meshes (canned foods, drink cans, vending machines), 12–1,660 tris, 1024/2048/4096 textures. No AI label.
- [Store page](https://assetstore.unity.com/packages/3d/props/survival-foods-package-186744)

**PijayArt – Survival Bundle Package (verified)**
- Price and rating: $19.99. Rating hidden (1 rating).
- Unity and pipelines: 2021.3.31 Built-in / 2021.3.45 URP. Version v1.0, 2025-08-11.
- Contents: 45 props (melee weapons, canned food, medical, market items, vending machines), 12–5,766 tris, 1K–4K textures. **"LODs: No"**.
- [Store page](https://assetstore.unity.com/packages/3d/props/survival-bundle-package-306756)

**AF Creations – Survival Food Bundle – Packaged Products (verified)**
- Price and rating: $4.99. 0 ratings.
- Unity and pipelines: **6000.1.12f1, URP + HDRP**. Version v1.0, 2025-09-29.
- Contents: 18 assets with opened and unopened variants (36 meshes), 44–3,172 polys. Textures are only 256–1024, which is weaker for close-ups. "Survival/post apocalypse style". No AI label.
- [Store page](https://assetstore.unity.com/packages/3d/props/food/survival-food-bundle-packaged-products-332980)

**Robot Skeleton – Groceries Pack (verified)**
- Price and rating: $7.99. Rating hidden (1 rating).
- Unity and pipelines: 2019.3.7, no SRP listed. Version v1.0, 2020-06-15.
- Contents: 23 items (bread, butter, milk, OJ, eggs, flour, yogurt, produce bags, etc.), 110–2,986 tris, 2048 maps (1024 for loose produce), Albedo/Rough/Normal/AO.
- [Store page](https://assetstore.unity.com/packages/3d/props/food/groceries-pack-170260)

**polyworkz – 3D Survival Food Pack (verified)**
- Price and rating: $4.99. Rating hidden (1 rating).
- Unity and pipelines: 2021.3.23, Built-in.
- Contents: 18 items, 4,350 polys total (e.g. pork & beans can 540, MRE 118, chips bag 156), 2K Base/Normal/Metal/AO.
- [Store page](https://assetstore.unity.com/packages/3d/props/food/3d-survival-food-pack-252506)

**Sakari Games – Photoscanned food pack (verified)**
- Price and rating: $9.99. 0 ratings.
- Unity and pipelines: 2020.1.6, Built-in. Version v1.0, 2021-02-04.
- Contents: 11 photoscanned and retopologized items (coffee pack, pasta, rice, oils, honey, chocolate bar, toilet paper, etc.).
- [Store page](https://assetstore.unity.com/packages/3d/props/food/photoscanned-food-pack-187422)

**Dekogon Studios – Shopping and Market VOL 2 – Grocery Store (verified)**
- Price and rating: $29.99. 0 ratings.
- Unity and pipelines: 2019.3.15, Built-in tag. The description says URP. Version v1.0, 2020-12-11.
- Contents: 39 prefabs, mostly 2048+ textures. Fixtures only: checkout counters, cooler (12.9k polys), open-top freezer, carts, baskets, stands. No food items are listed.
- [Store page](https://assetstore.unity.com/packages/3d/props/shopping-and-market-vol-2-grocery-store-184259)

**3D Everything – Convenience Store (verified)**
- Price and rating: $25.00. Rating hidden (2 ratings).
- Unity and pipelines: **6000.0.56f1, Built-in + URP**. Version v1.3, 2025-09-01.
- Contents: 77 models (food, drinks, coolers, freezers, ATM, register), 200–3,500 polys, **1024 textures, "low-poly"**. Below close-up quality. No AI label.
- [Store page](https://assetstore.unity.com/packages/3d/props/interior/convenience-store-162304)

**Mixall – Grocery store – parking and supermarket (verified)**
- Price and rating: $99.99. **3 stars, 4 ratings**.
- Unity and pipelines: 2019.4.0, Built-in + URP. Version v1.0, 2022-06-02. 2.47 GB.
- Contents: 378 unique models / 941 prefabs, 2 to 89.4k tris, 512–4096 Albedo/Normal/Metal. Includes non-food goods (sport, tools).
- [Store page](https://assetstore.unity.com/packages/3d/environments/grocery-store-parking-and-supermarket-224033)

**Cybernetic Walrus – Grocery Store Furniture Pack Vol. 1 (verified)**
- Price and rating: $24.99. 0 ratings.
- Unity and pipelines: 2020.3.32, Built-in/URP/HDRP. Version v1.0, 2022-12-10.
- Contents: 32 meshes, **LODs and collision meshes on all objects**, 74–5,626 tris, 1K/2K textures. Fixtures (fridges, shelves, conveyor belts), not food.
- [Store page](https://assetstore.unity.com/packages/3d/props/grocery-store-furniture-pack-vol-1-238689)

**Bright Vision Game – Grocery Store Environment HQ (verified)**
- Price and rating: $15. 0 ratings.
- Unity and pipelines: 2021.3.33, Built-in/URP/HDRP.
- Contents: 2048 atlas, very low-poly products (cola 1,008 tris, snack box 144 tris), clean and worn variants. Background quality only.
- [Store page](https://assetstore.unity.com/packages/3d/environments/landscapes/grocery-store-environment-hq-288645)

**fyodor – Assorted Drinks and Snacks (verified)**
- Price and rating: $8.95. 0 ratings.
- Unity and pipelines: 2022.3.7, all pipelines.
- Contents: 76 prefabs at 50–200 polys on a single 2k atlas. Too low for close-ups.
- [Store page](https://assetstore.unity.com/packages/3d/props/assorted-drinks-and-snacks-264603)

**3D OToole – Apocalyptic Supermarket (verified)**
- Price and rating: $19.99. 5 stars, 3 ratings.
- Unity and pipelines: Unity 5.3.2. Version 2016.
- Contents: modular looted supermarket with decay states, tin cans, soda bottles, empty food boxes. Thematically ideal but very old.
- [Store page](https://assetstore.unity.com/packages/3d/props/interior/apocalyptic-supermarket-58065)

### Inferences
- Phoenix3D plus the two 3D Division can packs give the best close-up-quality, LOD-equipped, survival-oriented food set for URP.
  - The 3D Division can states (sealed to opened to empty) map directly onto consume/loot mechanics.
  - Neither pack has reviews yet.
- Cereal boxes specifically were not found in any realistic pack. Searches returned only cartoon or low-poly cereal packs, so cereal and other box goods may need custom work or a different store.
- Brand handling: Dekogon states labels are "custom made by our studio" (fictional, legally safe), and 3D Division says its logos are handcrafted. Other packs did not state brand policy, so check screenshots for real trademarks.

### Gaps
- Phoenix3D's full item list was truncated on the page excerpt.
- No user reviews exist for most food packs, so close-up quality can only be judged from screenshots, which were not inspected.
- No realistic cereal-box or pantry-dry-goods pack (beyond Groceries Pack and Photoscanned food pack) was found on the Unity store.

## URP + Unity 6 support, LODs, poly/texture budgets?

### Takeaway
Unity 6 (6000.x) is explicitly listed for only a few packs here:
- POLYBOX Kitchen Pack (6000.3.2)
- 3D Everything Convenience Store (6000.0.56)
- AF Creations Survival Food Bundle (6000.1.12)
- Kerimcan Modular Kitchen (6000.3.10), which is stylized

Most realistic packs are uploaded from 2019.3–2022.3 with a URP tag. Explicit LODs are stated only by:
- Phoenix3D (LOD0/LOD1)
- 3D Division (3 LODs)
- Cybernetic Walrus (LODs and collisions)

Packs that explicitly state **no** LODs: PijayArt, Omniia, Helix, Kerimcan.

### Cited Findings
- **Unity 6 listed**:
  - POLYBOX Kitchen Pack: 6000.3.2 — [source](https://assetstore.unity.com/packages/slug/kitchen-pack-38322)
  - 3D Everything Convenience Store: 6000.0.56 — [source](https://assetstore.unity.com/packages/3d/props/interior/convenience-store-162304)
  - AF Creations Survival Food Bundle: 6000.1.12 — [source](https://assetstore.unity.com/packages/3d/props/food/survival-food-bundle-packaged-products-332980)
- **URP tagged but no Unity 6 listed**:
  - Dekogon Kitchen MEGA and volumes: 2019.3 — [source](https://assetstore.unity.com/packages/3d/props/kitchen-props-vol-1-7-mega-pack-178154)
  - Bendylab: 2021.3 — [source](https://assetstore.unity.com/packages/3d/props/electronics/home-appliances-v1-339504)
  - Kraffing: 2022.3 — [source](https://assetstore.unity.com/packages/3d/props/kitchen-pack-v1-kitchen-appliance-game-ready-pbr-built-in-urp-co-374178)
  - Phoenix3D: 2022.3 — [source](https://assetstore.unity.com/packages/3d/props/p3d-survival-canned-food-and-snacks-312545)
  - 3D Division: 2022.3 — [source](https://assetstore.unity.com/packages/3d/props/food/canned-food-fruits-and-vegetables-pbr-game-ready-401732)
- **URP claimed only in the description**: 32cm Kitchen Appliances Pack, whose SRP tag shows Built-in/custom — [source](https://assetstore.unity.com/packages/3d/props/electronics/kitchen-appliances-pack-356008)
- **Budgets for close-up props**:
  - 3D Division cans: 1.1–1.7k polys at 1K–4K with texel density 10.24.
  - Phoenix3D cans: 1.5–5.3k LOD0.
  - 32cm small appliances: up to 60k tris, which is heavy.
  - Kraffing Vol.3 stove: 45k tris.
  - Bendylab appliances: max 3.8k at 4K textures, the most budget-friendly of the appliance packs.
  - Sources: [3D Division](https://assetstore.unity.com/packages/3d/props/food/canned-food-fruits-and-vegetables-pbr-game-ready-401732), [Phoenix3D](https://assetstore.unity.com/packages/3d/props/p3d-survival-canned-food-and-snacks-312545), [32cm](https://assetstore.unity.com/packages/3d/props/electronics/kitchen-appliances-pack-356008), [Kraffing Vol.3](https://assetstore.unity.com/packages/3d/props/electronics/pbr-asset-kitchen-pack-vol-3-272350), [Bendylab](https://assetstore.unity.com/packages/3d/props/electronics/home-appliances-v1-339504)

### Inferences
- For Unity 6 URP, nearly all candidates will need a material-upgrade pass. The URP packs (Dekogon, Phoenix3D, 3D Division, Bendylab, Kraffing) should be low-risk; the Built-in-only ones (Frogbytes, Immerse, Robot Skeleton, Kraffing Vol.3) need conversion.
- Heavy small-appliance meshes (32cm toaster/blender at 60k, kettle at 50k; Kraffing stove and dishwasher at 42–45k) would need decimation or LOD generation for a populated suburb.

### Gaps
- Actual URP/Unity 6 import behavior was not tested, and no forum reports were found.

## Any "Created with AI" labels?

### Takeaway
None of the roughly 35 kitchen, appliance and food packs checked carries a "Created with AI" disclosure: the store's `aiDescription` field was empty on every page. 3D Division Studios goes further and advertises "Handcrafted, AI-free textures and logos".

### Cited Findings
- `aiDescription` was empty on every product page scraped, for example:
  - [32cm](https://assetstore.unity.com/packages/3d/props/electronics/kitchen-appliances-pack-356008)
  - [Phoenix3D](https://assetstore.unity.com/packages/3d/props/p3d-survival-canned-food-and-snacks-312545)
  - [Dekogon MEGA](https://assetstore.unity.com/packages/3d/props/kitchen-props-vol-1-7-mega-pack-178154)
  - [Bendylab](https://assetstore.unity.com/packages/3d/props/electronics/home-appliances-v1-339504)
  - [POLYBOX](https://assetstore.unity.com/packages/slug/kitchen-pack-38322)
- The field does work: the same page data held a populated AI disclosure for "American Suburb Top-Down Pack" (395606), which reads "Some high-poly source models and texture elements were created with the assistance of AI tools…". That is outside this topic, but it is relevant to the wider suburb search. — [embedded on store page](https://assetstore.unity.com/packages/3d/props/interior/realistic-kitchen-pack-80277)
- 3D Division states "Handcrafted, AI-free textures and logos". — [source](https://assetstore.unity.com/packages/3d/props/food/canned-food-fruits-and-vegetables-pbr-game-ready-401732)

### Inferences
- AI disclosure is not a differentiator in this niche. Most candidates predate the policy or are handmade.

### Gaps
- The visual badge itself was not seen. Its absence was inferred from the empty data field.
