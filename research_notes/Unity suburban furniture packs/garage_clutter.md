# Unity Asset Store: realistic garage/workshop props and household clutter/debris packs (Unity 6 URP, abandoned US suburb)

How these notes were made (3 Oct 2026): I downloaded each product page from assetstore.unity.com with curl and read the product JSON embedded in the page. The fields used were name, publisher, finalPrice/originalPrice/discount, rating {average,count}, reviewCount, srps (the render-pipeline compatibility table: "standard"=Built-in, "lightweight"=URP, "hd"=HDRP), supportedUnityVersions, currentVersion and publishedDate, description/keyFeatures, and **aiDescription**, which is the field behind the store's "Created with AI" disclosure. Some pages were also checked with WebFetch, and they matched.

The store hides the star average until a pack has enough ratings. In the JSON this shows as `average: 0` with a non-zero count, and it is reported below as "not enough ratings (N)". "Favs" is the store's favorites/hotness count. URLs on marketplace.unity.com and assetstore.unity.com resolve to the same listings.

Abbreviations: BiRP = Built-in, U6 = a Unity 6000.x version is listed in the compatibility table.

## Best realistic garage / workshop / tool packs

### Takeaway
No garage pack on the Unity store is clearly AAA-grade for first-person use. The strongest live options:
- **Basement House Props** and **Workshop Garage Props** (both by 32cm): 4K PBR, based on real objects.
- **Storage Clutter** (SpaceZeta): updated Sept 2026.
- **Garage Workbench** (PolySquid): explicitly lists Unity 6 with BiRP+URP, updated March 2026.
- **Workshop Tools and Toolboxes – Combo Pack** (enyra3D): the most hand-tool variety, with published per-item poly counts.

None of these has more than two ratings. Dekogon, Next Level 3D and Lowlypoly garage packs did not turn up on the Unity store. Dekogon's interior lines appear on Fab instead.

### Cited Findings
- **Garage Workbench** (PolySquid)
  - URL: https://assetstore.unity.com/packages/3d/props/tools/garage-workbench-131418
  - Price: $14.99, no sale. Not enough ratings (2), 93 favs.
  - Compatibility table: BiRP + URP, tested on 6000.3.10f1 and 2022.3.48f1 (U6 yes). No HDRP.
  - v1.3.5, 30 Mar 2026. First published 2018. 118 MB.
  - Content: modular shelves (3), a high-quality animatable vise, 8 tools, 10+ bottles/cans, 7 trash props, a fuse box with gauges, modular copper pipes and a garage lamp. Described as "fairly low poly, but looks stunning up close", aimed at "survival… FPS", with props usable as weapons.
  - Not stated: poly counts, texture resolution, LODs. No AI disclosure.
  - [Store](https://assetstore.unity.com/packages/tools/garage-workbench-131418); [WebFetch of marketplace page](https://marketplace.unity.com/packages/3d/props/tools/garage-workbench-131418)
- **Garage Tools** (PolySquid), the light version of Garage Workbench
  - URL: https://assetstore.unity.com/packages/slug/131508
  - Price: $5.99. No ratings, 78 favs.
  - Compatibility table: BiRP + HDRP on 2022.3.19f1. No URP row, no U6.
  - v1.2, 13 Mar 2024.
  - Content: 9 tools (vise, drill, metal saw, file, socket wrench, wrench, screwdriver, pliers, hammer) with PBR materials.
  - No AI disclosure.
  - [Store](https://assetstore.unity.com/packages/slug/131508)
- **Basement House Props** (32cm)
  - URL: https://assetstore.unity.com/packages/3d/props/basement-house-props-263053
  - Price: $15.00. Note: a WebFetch rendering showed $16.50, probably a currency/display artifact; the JSON finalPrice is 15.00. Not enough ratings (1), 26 favs.
  - Compatibility table: BiRP + URP + HDRP on 2021.3.28f1. No U6 listed.
  - v1.0, 22 Sep 2023. 2.6 GB.
  - Specs: 68 meshes, about 190k vertices total, 197 textures, **4096 PBR** (Albedo, Normal, Roughness, Metalness, AO plus HDRP mask).
  - Content: "based in real ones, realistic scale". Wooden shelves pre-filled with objects, 2 toolboxes, 21 tools, trunks, plastic crate, trash can, water/oil tanks, ladder, fuse box, water heater, 3 paint buckets with brush and roller, 5 cleaning tools, 2 paper piles. Most items have old and new texture sets.
  - LODs not stated. No AI disclosure.
  - [Store](https://assetstore.unity.com/packages/3d/props/basement-house-props-263053)
- **Workshop Garage Props** (32cm)
  - URL: https://assetstore.unity.com/packages/3d/props/workshop-garage-props-203190
  - Price: $19.99. No ratings, 16 favs.
  - Compatibility table: none (empty). Unity 2019.4.20.
  - v1.0, 18 Oct 2021.
  - Content: four-post lift, 2 tool storage boxes, car jack, jack stand, air compressor, 2 repair ramps, engine hoist crane.
  - Specs: 70 meshes, 79k verts, 59 textures at **4096** (Albedo/Normal/Roughness/Metal/AO plus HDRP mask).
  - This is auto-shop gear, which fits a mechanic's garage more than a home garage. No AI disclosure.
  - [Store](https://assetstore.unity.com/packages/3d/props/workshop-garage-props-203190)
- **Workshop Tools and Toolboxes – Combo Pack** (enyra3D)
  - URL: https://assetstore.unity.com/packages/slug/231730
  - Price: $10.00. No ratings, 5 favs.
  - Compatibility table: BiRP only on 2021.3.5f1. No URP row, no U6.
  - v1.0, 21 Sep 2022.
  - Content: 117 prefabs including workbench, pegboard, toolholders, toolboxes in 5 colours, hammers, pliers, 8 spanners, chisels, clamps, 5 saws, scrapers, mallets, tapes, box cutter, level, vise.
  - Specs: 46 textures at 2K. Per-item tris are low: workbench 848, hack saw 1124, most hand tools 80–600.
  - No AI disclosure.
  - [Store](https://assetstore.unity.com/packages/slug/231730)
- **Toolboxes & Tools** (enyra3D)
  - URL: https://assetstore.unity.com/packages/3d/props/tools/toolboxes-tools-143490
  - Price: $5.99. Rating 5.0 (3 ratings, 1 review).
  - No compatibility table. Unity 2017.3. v1.0, Apr 2019.
  - [Store](https://marketplace.unity.com/packages/3d/props/tools/toolboxes-tools-143490)
- **Collection of models for garage** (Rusik3Dmodels)
  - URL: https://assetstore.unity.com/packages/3d/props/interior/collection-of-models-for-garage-99795
  - Price: $15.99. Rating 5.0 (11 ratings, 5 reviews), 198 favs.
  - No compatibility table. Unity 5.3.4. v1.0, Oct 2017.
  - Content: 110 models (car hoist, keys, tools, cans, barrels, desks, cupboards, tire equipment), 64,868 polys in total.
  - Textures: 4096 Diffuse/Specular/Normal/Occlusion. This is a specular workflow, so it would need material conversion for URP Lit.
  - [Store](https://assetstore.unity.com/packages/3d/props/interior/collection-of-models-for-garage-99795)
- **Garage Repair Workshop** (Aerolife)
  - URL: https://assetstore-fallback.unity.com/packages/3d/environments/urban/garage-repair-workshop-194895
  - Price: $25.00. Not enough ratings (1).
  - No compatibility table. Unity 2020.1.17. v1.0, May 2021.
  - Content: 50+ props, building interior/exterior, 4K textures, about 60k polys for the whole scene.
  - [Store](https://assetstore-fallback.unity.com/packages/3d/environments/urban/garage-repair-workshop-194895)
- **Garage Environment PBR** (Friki_Studio)
  - Price: $34.99. Not enough ratings (1).
  - No compatibility table. Unity 2019.2.4. v1.0, May 2021.
  - [Store](https://marketplace.unity.com/packages/3d/environments/urban/garage-environment-pbr-194593)
- **Garage Props** (StormBringer Studios)
  - URL: https://assetstore.unity.com/packages/3d/props/garage-props-201062
  - Price: $15. Unity 2018.4.36. v1.0, Oct 2021.
  - Keywords suggest a "man cave" garage (darts, basketball, drill, ratchet).
  - [Store](https://assetstore.unity.com/packages/3d/props/garage-props-201062)
- **Redneck Village** (PolySquid)
  - URL: https://assetstore.unity.com/packages/3d/environments/redneck-village-141618
  - Price: $24.99. Not enough ratings (2), 88 favs.
  - Compatibility table: BiRP + URP on 6000.3.10f1 and 2022.3.48f1 (U6 yes).
  - v1.4.5, 31 Mar 2026.
  - Content: 3 wooden buildings plus a garage, a car, a **lawnmower**, the full Garage Workbench pack, furniture with beer/coolers, garden props. This is one of the few store sources found for a realistic lawn mower.
  - Rural rather than suburban in theme.
  - [Store](https://assetstore-fallback.unity.com/packages/3d/environments/redneck-village-141618)
- **Push Lawn Mower** (Rescue3D Game Assets)
  - URL: https://assetstore.unity.com/packages/3d/props/push-lawn-mower-192887
  - Price: $9.00. No ratings.
  - No compatibility table. Unity 2018.4.30. v1.0, Apr 2021.
  - [Store](https://assetstore.unity.com/packages/3d/props/push-lawn-mower-192887)
- **Garage Environment Pack – Low Poly** (Immortal Factory)
  - Price: $18. 8 MB.
  - Excluded: the name says low poly, and the file is too small for realistic PBR.
  - [Store](https://assetstore.unity.com/packages/slug/198331)

### Inferences
- Shortlist for a Unity 6 URP garage:
  - Basement House Props: hero shelves, paint cans, tools, water heater, fuse box.
  - Storage Clutter: boxes, paint cans, drums, workbench (see next section).
  - Garage Workbench: verified on U6 + URP.
  - enyra3D combo: tool variety.
  - Redneck Village: lawnmower.
- The 4K 32cm packs will need texture downsizing (2K) to stay within a reasonable VRAM budget for a dense suburb.
- Gas cans and jerry cans were not found as a dedicated realistic Unity-store pack. City Trash pack has "canisters"/gas cylinders, and a Zombie Apocalypse Pack mentions a fuel can but is from 2015. Treat this as a gap: check Fab, or Dekogon's suburb lines on Fab, if licensing allows.

### Gaps
- No reviews or forum opinions were found on the quality of any garage pack. All have 0–2 ratings except the 2017 Rusik3Dmodels pack (11).
- LODs are not stated for any garage pack checked.
- I did not find Dekogon, Next Level 3D, Lowlypoly, Rarebyte or Leartes garage packs on the Unity store. A search pointed to Dekogon interior products being on Fab ([search result](https://www.fab.com/category/3d-model/furniture-fixtures?utm_type=p)). I did not verify whether they are on the Unity store under other names.

## Best realistic household clutter / abandoned / post-apocalyptic interior debris packs

### Takeaway
The best-verified options for an abandoned-house look in Unity 6 URP:
- **House Props & Furniture Vol. 2** (Finward Studios): 356 meshes, U6/URP, updated 26 Sep 2026, rating 5.0 from 11.
- **Dirty Apartments** (Triplebrick): purpose-built post-apocalyptic interiors, U6/URP, 4.0 from 55 ratings.
- **Urban Trash KIT** (Aparicio Silva): U6, all three pipelines, 3 LODs each.
- **Storage Clutter** (SpaceZeta): updated Sept 2026.

Photoscanned options:
- **3D Debris Scans** (ScansLibrary): HDRP-only table, U6, 4 LODs.
- **Garbage and Debris Vol. 1** (Unimodels): 2019, no pipeline table.

Coverage for toys, electronics and papers is thin. None of the packs checked focuses on household-item loot such as toys or electronics.

### Cited Findings
- **House Props & Furniture Vol. 2** (Finward Studios)
  - URL: https://assetstore.unity.com/packages/3d/props/interior/house-props-furniture-vol-2-265523
  - Price: $79.00, no sale on 3 Oct 2026. A search snippet showed an older $39.99 sale. Rating 5.0 (11), 464 favs.
  - Compatibility table: BiRP/URP/HDRP on **6000.0.83f1**, 2021.3.30f1 and 2019.4.30f1.
  - v1.2.0, **26 Sep 2026**. 2.1 GB.
  - Specs: 356 meshes, 177 textures, 1K–4K (mostly 2K/4K), BaseColor/MaskMap/Normal (+Emissive).
  - "Objects have slight wearing" and cabinets/drawers open. LODs "only for a few most triangle heavy objects". About 940k tris in the demo scene.
  - No AI disclosure.
  - [Store](https://assetstore.unity.com/packages/3d/props/interior/house-props-furniture-vol-2-265523)
- **Suburb Neighborhood House Pack (Modular)** (Finward Studios), the companion house shell
  - URL: https://assetstore.unity.com/packages/slug/72712
  - Price: $89.00. Rating 5.0 (127 ratings, 95 reviews), 4,762 favs.
  - Compatibility table: all three pipelines, including **6000.0.83f1**.
  - v2.0.0, 25 Sep 2026.
  - No AI disclosure.
  - [Store](https://assetstore.unity.com/packages/slug/72712)
- **Dirty Apartments** (Triplebrick)
  - URL: https://assetstore.unity.com/packages/3d/environments/urban/dirty-apartments-21403
  - Price: $35.00. Rating **4.0 (55 ratings, 17 reviews)**, 841 favs.
  - Compatibility table: BiRP/URP/HDRP on **6000.0.29f1** and 2022.3.53f1.
  - v1.5, 17 Dec 2024.
  - Content: "modular interior level kit designed for… post-apocalyptic environments". About 200–1200 tris per model, 20 furniture props with up to 4 texture options, props and decals, 133 prefabs.
  - The setting is apartments, not houses. LODs not stated. No AI disclosure.
  - [Store](https://assetstore.unity.com/packages/3d/environments/urban/dirty-apartments-21403)
- **Storage Clutter** (SpaceZeta)
  - URL: https://marketplace.unity.com/packages/3d/props/interior/storage-clutter-263145
  - Price: $15.99. No ratings, 10 favs.
  - Compatibility table: BiRP on 2021.3.6f1; BiRP/URP/HDRP on 2022.3.62f2. No U6 row.
  - v1.1, **23 Sep 2026**.
  - Content: 65 prefabs plus 12 pre-built clutter prefabs. 10 cardboard boxes, 5 metal boxes, 3 paint cans, plastic bins/drawers, 16 product bottles, steel drums (clean and rusted), old toolbox, wires/hoses, pallet, wood and metal shelves, workbench.
  - Textures: 1K/2K Base/Roughness/Metallic/Normal on the Autodesk Interactive shader, so materials need conversion for URP. Nothing opens.
  - LODs not stated. No AI disclosure.
  - [Store](https://marketplace.unity.com/packages/3d/props/interior/storage-clutter-263145)
- **Urban Trash KIT** (Aparicio Silva)
  - URL: https://assetstore.unity.com/packages/3d/props/urban-trash-kit-310785
  - Price: $22.00. The description says "Promotional price!" but the JSON shows no discount. No ratings, 10 favs.
  - Compatibility table: BiRP/URP/HDRP on **6000.0.37f1**.
  - v1.6, 21 Feb 2025.
  - Specs: 83 meshes / 75 prefabs, 2K PBR, **3 LODs per object**, 300–11,000 tris, working lids on bins and dumpsters, custom colliders.
  - Caveat: the store pitch says "handpainted textures" while the keywords say "Realistic". Check screenshots before buying.
  - No AI disclosure.
  - [Store](https://assetstore.unity.com/packages/3d/props/urban-trash-kit-310785)
- **City Pack: Urban Trash Collection (110+ Models)** (Pedro H Crispim)
  - URL: https://assetstore.unity.com/packages/3d/props/exterior/city-trash-pack-110-assets-117248
  - Price: $19.99. Rating 5.0 (3 ratings, 1 review).
  - Compatibility table: URP only on 2022.3.3f1.
  - v1, Aug 2023.
  - Specs: most models 1–3k tris (maximum 8,296). Barrels, bottles, cardboard, cinder blocks, gas cylinders, pallets, tarps, tires, trash bags, bins, trash piles, paper pieces.
  - [Store](https://assetstore.unity.com/packages/3d/props/exterior/city-trash-pack-110-assets-117248)
- **3D Debris Scans** (ScansLibrary), **photoscanned**
  - URL: https://assetstore.unity.com/packages/3d/environments/3d-debris-scans-309440
  - Price: $49.00. No ratings.
  - Compatibility table: **HDRP only** on 6000.0.35f1. The description says "supports Unity 6".
  - v1.0, Mar 2025.
  - Content: 33 scanned assets (asphalt/brick/concrete/Ytong rubble, polystyrene foam debris, paving), each with High/Medium/Low versions and **4 LOD levels**. 2K Albedo/Specular/Normal/AO, which is a specular workflow.
  - This is construction rubble, not household junk. URP use would need a material conversion (unverified).
  - [Store](https://assetstore.unity.com/packages/3d/environments/3d-debris-scans-309440); [ScansLibrary forum thread](https://discussions.unity.com/t/scanned-assets-scanslibrary/1611739). The thread also lists texture packs on the store, including "Paper Cardboard Scans" (310893) and "Dirty Cloth Scans" (310813); I did not verify those product pages.
- **Garbage and Debris Vol. 1** (Unimodels), **photoscanned**
  - URL: https://assetstore.unity.com/packages/3d/environments/garbage-and-debris-vol-1-151857
  - Price: $12.99. Not enough ratings (2), 33 favs.
  - No compatibility table. Unity 2018.3.4. v1.0, Sep 2019. 1.2 GB.
  - Content: "49 Realistic photoscanned trash and garbage". Vertex counts range from 76 verts (single debris) to about 58k (oil groups) and 54k (pallet groups).
  - No AI disclosure.
  - [Store](https://assetstore.unity.com/packages/3d/environments/garbage-and-debris-vol-1-151857)
- **Damaged Cardboard Box Pack – 16 Game Ready Props** (Dimonati)
  - URL: https://marketplace.unity.com/packages/3d/props/old-cardboard-pack-309359
  - Price: $12.99. Not enough ratings (2).
  - Compatibility table: BiRP on **6000.0.35f1**.
  - v1.0, Feb 2025.
  - Specs: 16 boxes, including 5 crushed/damaged. 48–466 tris, 1–2K textures, about 1000 px/m texel density, real-world sizes listed.
  - [Store](https://marketplace.unity.com/packages/3d/props/old-cardboard-pack-309359)
- **Cardboard & Debris Pack** (SpeedTutor)
  - URL: https://marketplace.unity.com/packages/3d/props/cardboard-debris-pack-227630
  - Price: $6.99. Rating 5.0 (4).
  - Compatibility table: all pipelines on 2020.3.14f1.
  - Content: 20 prefabs (12 boxes, 8 alpha decals), 2–150 tris, 1–2K textures. "As seen in Unity's Official NEON environmental demo".
  - [Store](https://marketplace.unity.com/packages/3d/props/cardboard-debris-pack-227630)
- **Rubble and Debris – Modular Set** (Loknar Studio)
  - URL: https://marketplace.unity.com/packages/3d/props/exterior/rubble-and-debris-modular-set-116330
  - Price: $19.99. Rating 5.0 (10 ratings, 6 reviews), 657 favs.
  - The description claims HDRP/URP support, but the store table is empty. Unity 2018.4.25. v1.3, Feb 2021.
  - Specs: 11 rubble piles + 50 debris pieces, 4K PBR, 4 LODs per pile (100/66/33/10%), about 3–4k tris at LOD0.
  - [Store](https://marketplace.unity.com/packages/3d/props/exterior/rubble-and-debris-modular-set-116330)
- **Post Apocalyptic World Pack** (Crescent_Art)
  - URL: https://assetstore.unity.com/packages/3d/environments/urban/post-apocalyptic-world-pack-188358
  - Price: $34.99. Rating **4.0 (25)**, 465 favs.
  - Compatibility table: BiRP/URP/HDRP/custom on 2019.3.13f1 and 2020.3.22f1. No U6.
  - v1.1, Dec 2021.
  - Content: 64 props (dumpsters, rubbish, vehicles) plus 30+ buildings, with LODs and collision. This is exterior/city, not house interiors.
  - [Store](https://assetstore.unity.com/packages/3d/environments/urban/post-apocalyptic-world-pack-188358)
- **Abandoned House – Basic Version** (VIS Games)
  - URL: https://marketplace.unity.com/packages/3d/environments/abandoned-house-basic-version-181444
  - Price: $24.95. No ratings.
  - Compatibility table: BiRP/URP/HDRP on **6000.0.24f1** and 2021.1.16f1.
  - v3.1, Apr 2025.
  - Content: an old US-style wooden house with a garage, 48k tris for the house shell, 1K–4K textures. The basic version contains only doors, light switches and the kitchen, so it is a shell more than a prop source.
  - [Store](https://marketplace.unity.com/packages/3d/environments/abandoned-house-basic-version-181444)
- **Older or unsupported** packs, mostly 2015–2018 with no pipeline table; use with caution:
  - Abandoned Building Props Vol. 1 (Aron Versteeg): $10, Unity 4.5.5. [Store](https://marketplace.unity.com/packages/3d/props/industrial/abandoned-building-props-volume-1-25795)
  - Abandoned Room (EmranBayati): $19.99, 2020, 70+ objects, 512–2048 textures. [Store](https://marketplace.unity.com/packages/3d/environments/urban/abandoned-room-179611)
  - Apocalyptic Supermarket (3D OToole): $19.99, 2016, 5.0 from 3. [Store](https://marketplace.unity.com/packages/3d/props/interior/apocalyptic-supermarket-58065)
  - Post Apocalyptic World (PolyPixel): $25, 4.0 from 15, Unity 5.5. [Store](https://marketplace.unity.com/packages/3d/environments/urban/post-apocalyptic-world-38992)
  - Apocalypse Houses (Brandon Gillespie): $20, 2020. [Store](https://marketplace.unity.com/packages/3d/environments/urban/apocalypse-houses-159668)
  - Debris (Kyrylo Sibiriakov): $10, 2015. [Store](https://assetstore-fallback.unity.com/packages/3d/props/debris-48314)
  - Debris pack (Med-art): $25, 2016, photogrammetry concrete/brick. [Store](https://marketplace.unity.com/packages/3d/props/debris-pack-70136)
- **Free option:** Survival Game Tools (cookiepopworks.com) has canned food, battery, flashlight, walkie-talkie and first aid. 5.0 (16), 2,694 favs, Unity 2017.4. [Store](https://assetstore.unity.com/packages/3d/props/tools/survival-game-tools-139872)
- "Urban Debris & Trash Vol. 4 – Scanned Essentials" (23 photoscanned debris models from abandoned locations) appears to be a **Fab** listing, not a Unity-store one. [Fab](https://www.fab.com/listings/3489d9be-47d8-4d41-9328-88799edbec88?lang=es-mx)

### Inferences
- For dense interior dressing in URP on Unity 6, Finward's House Props Vol. 2 plus its Suburb House Pack is the strongest-supported pairing. Both are verified on U6, updated within the last two weeks, and highly rated.
- Layer on top of that:
  - Dirty Apartments for post-apocalyptic wallpaper/decal/furniture wear.
  - Storage Clutter, Basement House Props and the cardboard packs for boxes.
  - Urban Trash KIT or the City Trash pack for exterior garbage.
- Photoscanned household junk (toys, electronics, papers) is essentially missing from the Unity store results. ScansLibrary and Unimodels scans are rubble and garbage. This category likely needs Fab or Megascans-sourced content, or custom work (inference).

### Gaps
- No verified Unity-store packs focused on realistic **toys, consumer electronics, scattered papers/mail, or broken furniture**. Searches mostly returned stylized or low-poly packs.
- No Unity forum or Reddit quality opinions were collected in the time budget.
- Exact star breakdowns are hidden by the store for packs with few ratings.

## URP + Unity 6 support, LODs, poly/texture budgets

### Takeaway
Packs whose compatibility table **explicitly lists a 6000.x version with URP**:
- Garage Workbench and Redneck Village (6000.3.10f1)
- House Props & Furniture Vol. 2 and Suburb Neighborhood House Pack (6000.0.83f1)
- Dirty Apartments (6000.0.29f1)
- Urban Trash KIT (6000.0.37f1)
- Abandoned House – Basic (6000.0.24f1)

Damaged Cardboard Box Pack lists 6000.0.35f1 for BiRP only, and 3D Debris Scans lists 6000.0.35f1 for HDRP only.

Explicit LODs: Urban Trash KIT (3), 3D Debris Scans (4), Rubble & Debris Modular (4/2), Post Apocalyptic World Pack (stated), and Finward Vol. 2 (only for heavy objects).

### Cited Findings
- Compatibility tables, versions and dates come from each product page's embedded data; the per-pack lines above give the links.
- Per-pack budgets where stated:

  | Pack | Polys | Textures |
  |---|---|---|
  | enyra3D combo | 32–1,124 tris per tool | 2K |
  | Basement House Props | 190k verts over 68 meshes | 4K |
  | Workshop Garage Props | 79k verts over 70 meshes | 4K |
  | Dirty Apartments | about 200–1,200 tris per model | not stated |
  | Urban Trash KIT | 300–11k tris, 3 LODs | 2K |
  | Damaged Cardboard | 48–466 tris | 1–2K |
  | City Trash | 1–3k tris | not stated |
  | House Props Vol. 2 | about 940k tris in demo scene | 1–4K, MaskMap workflow |

  Sources: [enyra3D](https://assetstore.unity.com/packages/slug/231730), [32cm Basement](https://assetstore.unity.com/packages/3d/props/basement-house-props-263053), [32cm Workshop](https://assetstore.unity.com/packages/3d/props/workshop-garage-props-203190), [Dirty Apartments](https://assetstore.unity.com/packages/3d/environments/urban/dirty-apartments-21403), [Urban Trash KIT](https://assetstore.unity.com/packages/3d/props/urban-trash-kit-310785), [Dimonati](https://marketplace.unity.com/packages/3d/props/old-cardboard-pack-309359), [City Trash](https://assetstore.unity.com/packages/3d/props/exterior/city-trash-pack-110-assets-117248), [Finward](https://assetstore.unity.com/packages/3d/props/interior/house-props-furniture-vol-2-265523)
- Some packs use specular or Autodesk Interactive workflows and will need conversion to URP/Lit:
  - Storage Clutter (Autodesk Interactive) — [Store](https://marketplace.unity.com/packages/3d/props/interior/storage-clutter-263145)
  - Collection of models for garage (Specular) — [Store](https://assetstore.unity.com/packages/3d/props/interior/collection-of-models-for-garage-99795)
  - 3D Debris Scans (Specular) — [Store](https://assetstore.unity.com/packages/3d/environments/3d-debris-scans-309440)
- PolySquid packs ship Built-in by default, with a URP upgrade package — [Garage Workbench pitch](https://assetstore.unity.com/packages/3d/props/tools/garage-workbench-131418); [Redneck Village](https://assetstore-fallback.unity.com/packages/3d/environments/redneck-village-141618)

### Inferences
- Packs with no compatibility table (most of the pre-2022 packs) will probably work in URP after material conversion. That is not the same as a verified listing, so treat them as unverified for U6.
- The 4K-heavy packs (32cm, Rusik3Dmodels, Loknar) should be imported at 2K for a large open suburb.

### Gaps
- LOD presence is unstated for most garage packs: PolySquid, 32cm, enyra3D, Storage Clutter.
- Not confirmed: whether ScansLibrary's HDRP-only scans convert cleanly to URP.

## Any "Created with AI" labels?

### Takeaway
None of the roughly 50 garage/clutter/debris product pages checked has an AI-content disclosure (the aiDescription field is empty). The only disclosure in this space is on **American Suburb Top-Down Pack** (Art Equilibrium). It is a top-down/isometric suburb pack, not first-person quality, but it is relevant because of its theme.

### Cited Findings
- **American Suburb Top-Down Pack** (Art Equilibrium)
  - URL: https://assetstore.unity.com/packages/slug/395606
  - Price: **$14.00 on sale (60% off; regular $34.99)** on 3 Oct 2026. Rating 5.0 (17 ratings, 18 reviews).
  - Compatibility table: BiRP/URP/HDRP on 6000.0.74f1.
  - v1.0, 26 Jul 2026.
  - Specs: 749 prefabs, 2048 textures, props 4–850 polys, **LOD: No**. "Designed primarily for top-down, isometric…" games.
  - AI disclosure text, verbatim: "Some high-poly source models and texture elements were created with the assistance of AI tools. All final low-poly, game-ready models… were manually created, optimized, retopologized… Any AI-generated textures were manually edited and refined in Adobe Photoshop… The scripts included in the package were also created with AI assistance."
  - [Store](https://assetstore.unity.com/packages/slug/395606)
- An empty aiDescription was confirmed for every pack listed in the sections above, including Finward, PolySquid, 32cm, SpaceZeta, Aparicio Silva, Triplebrick and ScansLibrary — [pages as cited above].

### Inferences
- An empty field means the publisher declared no AI use. It is not independent proof that none was used.

### Gaps
- I did not check whether the store shows an AI badge separately from the aiDescription field, for example as a visual label rendered client-side. The field is assumed to be what drives the "Created with AI" disclosure.
