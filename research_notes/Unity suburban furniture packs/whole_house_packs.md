# Whole-House / Multi-Room Realistic Interior Packs on the Unity Asset Store (verified 2026-10-03)

**How the data was verified.** Every price, rating, compatibility, version, date and "Created with AI" field below comes from the live Asset Store on 2026-10-03. I pulled it from the store's own product GraphQL endpoint (`assetstore.unity.com/api/graphql/batch`), which is the data source that fills each product page. I also cross-checked several packs by fetching the product page directly with WebFetch, and the two sources agreed (for example, Suburb Neighborhood showed v2.0.0, released 2026-09-25, with 6000.0.83f1 tested on Built-in, URP and HDRP).
- **Ratings:** the `rating.average` field is a whole-star value as the store displays it. "Ratings" is the number of star ratings. "Written reviews" is the separate `reviewCount` field.
- **AI disclosure:** the store's AI disclosure is held in a product field called `aiDescription`. When it is filled in, the page shows the "Created with AI" disclosure. I confirmed this on a pack where the field is filled (Art Equilibrium, see the AI question below). For all other packs the field was empty.
- **Prices:** `finalPrice` is the price today and `originalPrice` is the list price. A gap between them means a sale is running.
- **Pipeline codes:** in the store data, "lightweight" means URP, "standard" means Built-in and "hd" means HDRP.

---

## Q1. Which multi-room house interior packs are the most realistic and the best reviewed?

### Takeaway
Three publishers stand out on rating count and depth: Finward Studios (Suburb Neighborhood House Pack, Atmospheric House, House Props & Furniture Vol. 2, House Furniture Pack), NOT_Lonely (HQ Residential House) and Gabro Media (HQ Suburban House). All are 5-star, all are realistic PBR, and all are whole houses or whole-house prop suites with an American suburban flavor. ArchVizPRO (Oneiros) has the highest-fidelity archviz-style interiors (4K, URP-only, Unity 6). However, those interiors are European or modernist luxury spaces with few ratings. None of the whole-house packs I found are photoscanned. Only small prop packs are photoscanned (DeltaRaccoons).

### Cited Findings

**Candidate table (all store facts as of 2026-10-03)**

| # | Pack (publisher) | Price now / list | Stars (ratings / written reviews) | Pipelines | Unity 6 listed? | Latest version (date) | AI label |
|---|---|---|---|---|---|---|---|
| 1 | Suburb Neighborhood House Pack (Modular) (Finward Studios) | $89 / $89 | 5 (127 / 95) | Built-in, URP, HDRP | Yes, 6000.0.83f1 | 2.0.0 (2026-09-25) | None |
| 2 | Atmospheric House (Modular) (Finward Studios) | $99 / $99 | 5 (58 / 58) | Built-in, URP, HDRP | Yes, 6000.0.16f1 | 1.1.0 (2024-08-29) | None |
| 3 | House Props & Furniture Vol. 2 (Finward Studios) | $79 / $79 | 5 (11 / 11) | Built-in, URP, HDRP | Yes, 6000.0.83f1 | 1.2.0 (2026-09-26) | None |
| 4 | House Furniture Pack (Finward Studios) | $35 / $35 | 5 (27 / 21) | Built-in, URP, HDRP | Yes, 6000.0.83f1 | 2.0.0 (2026-09-26) | None |
| 5 | HQ Residential House (NOT_Lonely) | $70 / $70 | 5 (116 / 68) | Built-in, URP, HDRP | No, only 2019.4.38f1 | 2.2.1 (2024-12-17) | None |
| 6 | HQ Suburban House (Gabro Media) | $36 / $36 in the store data (description says 40% off until Oct 12, original $60) | 5 (14 / 7) | Built-in, URP, HDRP (via upgrade packs) | No, highest is 2023.2.8f1 | 1.6 (2024-12-12) | None |
| 7 | American Home Asset – Interior & Exterior (E6 Model) | $39.99 / $39.99 | No ratings | URP only | No, 2022.3.57f1 | 1.0 (2026-01-12) | None |
| 8 | Residential House Pack (URP) (Nimoyo) | $14.99 / $14.99 | No ratings | URP only | Yes, 6000.5.1f1 | 1.1 (2026-08-17) | None |
| 9 | HD Apartment (Slyt Digital) | $15 / $15 | 0 shown (2 ratings) | Built-in, URP, HDRP | Yes, 6000.0.59f2 | 2.1 (2025-10-24) | None |
| 10 | Interior Realistic – Low Poly 3D Models Pack (ithappy) | **$124.50 on sale** / $249 | 5 (16 / 16) | Built-in, URP, HDRP, custom | Yes, 6000.0.28f1 | 2.5 (2026-08-27) | None |
| 11 | ArchVizPRO Interior Vol.8 URP (ArchVizPRO) | $39.99 / $39.99 | 5 (7 / 7) | URP only | Yes, 6000.0.48f1 | 1.1 (2025-05-31) | None |
| 12 | ArchVizPRO Interior Vol.6 URP (ArchVizPRO) | $39.99 / $39.99 | 0 shown (1 rating) | URP only | Yes, 6000.0.48f1 | 1.1 (2025-06-12) | None |
| 13 | Country houses with interiors (PolySquid) | $24.99 / $24.99 | 5 (6 / 6) | Built-in, URP | Yes, 6000.3.11f1 | 1.3.5 (2026-03-23) | None |
| 14 | Vintage House (Manufactura K4) | $65 / $65 | 5 (22 / 11) | No pipeline table (Built-in era) | No, 2017.4.17 | 1.3 (2019-02-04) | None |
| 15 | Realistic House Interior&Exterior (Must Have Studio) | No price returned (possibly deprecated or unavailable; unverified) | 5 (3 / 3) | Built-in, URP, HDRP | No, 2019.4.28f1 | 1.0 (2021-07-21) | None |
| 16 | HQ Modular House Interior Pack (Knife Entertainment) | $39.99 / $39.99 | 4 (21 / 15) | No pipeline table | No, 5.5.1 | 1.0 (2018-01-17) | None |
| 17 | Apartment Kit (Brick Project Studio) | Free | 5 (79 / 74) | Built-in only | No, 2020.3.40f1 | 4.2 (2023-06-20) | None |

**Per-pack details**

- **Suburb Neighborhood House Pack (Modular), Finward Studios.** [Store page](https://assetstore.unity.com/packages/3d/environments/urban/suburb-neighborhood-house-pack-modular-72712)
  - Contents: modular houses with both interiors and exteriors, plus a modular suburban road system with sidewalks, mailboxes, cars, lamps and electric poles. Interior furniture includes beds, chairs, tables and paintings.
  - Scale: 5 ready-made, furnished houses and more than 450 objects. Download size is about 4.2 GB.
  - Textures: 256 px to 2K. BaseColor, MaskMap and Normal maps for most assets.
  - Budget: "Approximately 1.5 million triangles in demo scene."
  - LODs: not mentioned.
  - Notes: includes day and night demo scenes. The page says "URP is default render pipeline for Unity 6 and upwards." Store tags include Suburb, kitchen and neighborhood.
- **Atmospheric House (Modular), Finward Studios.** [Store page](https://assetstore.unity.com/packages/3d/environments/urban/atmospheric-house-modular-192712)
  - Contents: modular walls, floors, ceiling, roof, porch and kitchen cabinets, plus interior props. More than 600 objects; download size about 6.2 GB.
  - Wear system: clean and worn materials for every object. A material swapper changes the house "from new and clean to old and worn with a single click."
  - Interactivity: drawers, cabinets, doors and windows open.
  - Textures: mostly 2K, ranging from 512 px to 4K. BaseColor, MaskMap, Normal and Emissive maps, plus Multimask textures.
  - Budget: about 1.1M triangles in the demo scene.
  - Pipeline caveat: the tweakable wear shader works only in URP and HDRP, not Built-in.
  - Store tags include abandoned, Suburb and Night. A worn-house toggle fits a zombie setting well.
- **House Props & Furniture Vol. 2, Finward Studios.** [Store page](https://assetstore.unity.com/packages/3d/props/interior/house-props-furniture-vol-2-265523)
  - Scale: 356 meshes and 177 textures, about 2.1 GB.
  - Textures: 1K to 4K, mostly 2K and 4K. BaseColor, MaskMap, Normal and Emissive maps.
  - Interactivity: openable cabinets, drawers and doors with modeled interiors (no animations included).
  - LODs: "LOD's only for a few most triangle heavy objects." Every object has a custom lightmap UV.
  - Budget: about 940k triangles in the demo scene.
  - Caveat: this is a props pack. The demo scene has no working house model. The page says it is designed as an add-on to Atmospheric House and Suburb Neighborhood. Store tags include Farmhouse and Suburb.
- **House Furniture Pack, Finward Studios.** [Store page](https://assetstore.unity.com/packages/3d/props/house-furniture-pack-88646)
  - Contents: more than 170 interior props taken from the Suburb Neighborhood pack. The house itself is not included.
  - Textures: 512 px to 2K.
  - Interactivity: modular kitchen cabinets that snap to a 0.1 grid. Drawers and cabinets open, except the kitchen ones.
- **HQ Residential House, NOT_Lonely.** [Store page](https://assetstore.unity.com/packages/3d/environments/urban/hq-residential-house-48976)
  - The store pitch reads "Interactive and customizable American-style house."
  - Features: PBR materials and "made by a real house blueprint." More than 200 unique objects.
  - Interactivity: scripted doors, windows and closets.
  - Budget: "tris count - 135k total in the demo scene."
  - Bonus: a Modular Interiors system.
  - Store tags: usa, two story, FPS, Horror.
  - Publisher claim: assets were used in Phasmophobia, Boneworks and House Flipper.
  - One user review (2015) compares it to the houses in Silent Hill P.T. and Allison Road.
  - Caveat: the compatibility table lists only 2019.4.38f1, even though the latest version is from Dec 2024.
- **HQ Suburban House, Gabro Media.** [Store page](https://assetstore.unity.com/packages/3d/environments/urban/hq-suburban-house-81890)
  - Contents: "A complete modern, two-story family home fully furnished," with more than 200 interactive props.
  - LODs and colliders: "Every model comes with colliders, LOD models provided."
  - Materials: PBR metallic workflow baked from high-poly models. Separated and pivoted doors, drawers and switches.
  - Budget: house about 40k tris, car about 30k, full demo scene about 300k.
  - Pipelines: HDRP and URP upgrade packs are included.
  - Platform: the page says it is "Not suitable for mobile."
  - Note: the store data says the pack was first published in 2017 by Gabro Media, not NOT_Lonely. The page says it "works well together with HQ Residential House."
- **American Home Asset – Interior & Exterior, E6 Model.** [Store page](https://assetstore.unity.com/packages/3d/environments/american-home-asset-interior-exterior-328239)
  - Contents: a single-story American-style house.
  - Rooms: 1-car garage, 2 adult bedrooms, 1 children's room, 4 storage rooms, a fully equipped kitchen in 3 material variants (clean white, aged/dirty white, wood), living room, 2 bathrooms and a garden.
  - Interactivity: the fridge, oven, dishwasher, washing machine and all cabinets open.
  - Scale and textures: 282 textures at 2048 px and about 100 meshes.
  - Budget: 200k–300k tris. No LODs.
  - Pitch: "simulation, horror, survival."
- **Residential House Pack (URP), Nimoyo.** [Store page](https://assetstore.unity.com/packages/3d/environments/urban/residential-house-pack-urp-345862)
  - Contents: 17 ready-made houses "with full interiors." 712 prefabs and 1,732 textures.
  - Maps: Albedo, Metallic, Normal, Occlusion and Height, at 512 px to 2K.
  - LODs: only the trees, plants and grass have LODs (2–3 levels).
  - Platform: PC only, and the page says it is not tested on mobile or VR.
  - Built in Unity 6000.5.1. Download size is about 6.1 GB.
- **HD Apartment, Slyt Digital.** [Store page](https://assetstore.unity.com/packages/3d/environments/urban/hd-apartment-97614)
  - Contents: 210+ prefabs and 170 PBR materials in 2K.
  - Maps: Albedo, Metallic/Specular, Normal, Height, Occlusion and Mask.
  - Geometry: described only as "low poly."
  - Scenes: 3 apartments and a stairwell, each with HDRP, URP and Built-in versions. Doors and furniture open.
- **Interior Realistic – Low Poly 3D Models Pack, ithappy.** [Store page](https://assetstore.unity.com/packages/3d/props/interior/interior-realistic-low-poly-3d-models-pack-241355)
  - Contents: 836 assets and 40 prepared rooms (living room, bedroom, kitchen, bathroom, nursery, hallway, study, office, game room).
  - Geometry: 328k tris for the entire pack.
  - Textures: color and roughness maps only, at 2048 px.
  - Style: the name says "realistic," but the pitch is "3D Low-poly assets." It is a clean, untextured-detail style, not photoreal.
- **ArchVizPRO Interior Vol.8 URP, ArchVizPRO.** [Store page](https://assetstore.unity.com/packages/3d/environments/urban/archvizpro-interior-vol-8-urp-226014)
  - Contents: a modern apartment with a living room and open kitchen, a relax zone, 2 bedrooms and 2 bathrooms.
  - Scale and textures: 150+ prefabs and 4K textures.
  - LODs: "Level of detail (LOD)" is listed. This is the only ArchVizPRO volume whose page mentions LODs.
- **ArchVizPRO Interior Vol.6 URP.** [Store page](https://assetstore.unity.com/packages/3d/environments/urban/archvizpro-interior-vol-6-urp-274067)
  - Contents: a "Scandinavian house" with a living room, kitchen, bedroom, studio, bathroom, relaxation room and 2 courtyards.
  - Scale and textures: 200+ prefabs and 4K textures.
- **Other ArchVizPRO URP volumes.** All are listed for Unity 6000.0.48f1 and are URP only.
  - Vol.1 ($29.99): [store page](https://assetstore.unity.com/packages/3d/environments/urban/archvizpro-interior-vol-1-urp-269445)
  - Vol.2, an industrial loft: [store page](https://assetstore.unity.com/packages/3d/environments/urban/archvizpro-interior-vol-2-urp-281948)
  - Vol.3, "a beautiful European apartment": [store page](https://assetstore.unity.com/packages/3d/environments/urban/archvizpro-interior-vol-3-urp-270835)
  - Vol.7, inspired by the Azuma House (4★, 4 ratings): [store page](https://assetstore.unity.com/packages/3d/environments/urban/archvizpro-interior-vol-7-urp-226477)
  - Vol.9, a luxury villa: [store page](https://assetstore.unity.com/packages/3d/environments/urban/archvizpro-interior-vol-9-urp-236479)
  - Vol.10, a pool and solarium retreat: [store page](https://assetstore.unity.com/packages/3d/environments/urban/archvizpro-interior-vol-10-urp-255834)
- **Country houses with interiors, PolySquid.** [Store page](https://assetstore.unity.com/packages/3d/environments/urban/country-houses-with-interiors-155343)
  - Contents: 3 houses with interiors, a pickup and a lawnmower. Vertex-paint damage on materials.
  - Pitch: "redneck country house set … Perfect for horror games."
- **Vintage House, Manufactura K4.** [Store page](https://assetstore.unity.com/packages/3d/environments/vintage-house-98229)
  - Contents: 450+ prefabs with modular walls, plus kitchen, bathroom, bedroom, toilet and living-room furniture and clutter. Hi-res PBR materials.
  - Caveat: last updated in 2019.
- **Realistic House Interior&Exterior, Must Have Studio.** [Store page](https://assetstore.unity.com/packages/3d/environments/urban/realistic-house-interior-exterior-197957)
  - Contents: 188 models (33 architecture modules, 36 furniture pieces, 17 appliances, 102 props). Pitched as "multi-story house in American-style."
  - Rooms: garage, hall, dining room, living room, toilet, bathroom, laundry, 2 bedrooms, work room and garden house.
  - Geometry: 24–5,000 polys per model.
  - Textures: 512 px to 2K, with Albedo, Normal and Metallic maps.
  - Caveat: the store data returned no price. The pack may be deprecated (unverified).
  - The release thread lists no LODs and says "Standard pipeline (HDRP conversion planned)." — [Unity Discussions](https://discussions.unity.com/t/released-realistic-house-interior-exterior/885012)
- **HQ Modular House Interior Pack, Knife Entertainment.** [Store page](https://assetstore.unity.com/packages/3d/environments/urban/hq-modular-house-interior-pack-107018)
  - Contents: "HQ interior of a old house." More than 100 objects and PBR materials.
  - LODs: "LOD system for all objects."
  - Caveat: uploaded with Unity 5.5.1, and the pipeline table is empty.
- **Apartment Kit, Brick Project Studio (free).** [Store page](https://assetstore.unity.com/packages/3d/environments/apartment-kit-124055)
  - Contents: 200+ prefabs covering living room, kitchen appliances (fridge, stove, range hood), bedroom and bathroom.
  - Interactivity: a demo with FPS controls and working drawers and doors.
  - Pipelines: Built-in only.

**Lower-value packs found (realistic but weak, old or thin)**
- HQ Modern House Complete Pack (Archteria 3D): $19.99, 2★ from 3 ratings, last updated 2020, no pipeline table. — [store page](https://assetstore.unity.com/packages/3d/environments/hq-modern-house-complete-pack-162631)
- HQ Apartment interior (Bright Vision Game): $24.99, no ratings. 66 prefabs with 2K atlas maps (Albedo, Mask, Normal) and per-object tris listed (bed 4,377 tris, fridge 965 tris). Built-in, URP and HDRP on 2021.3.33. — [store page](https://assetstore.unity.com/packages/3d/environments/hq-apartment-interior-284211)
- Realistic Interiors Vol1 (Underhill Labz): $20, 80+ models, Built-in only. — [store page](https://assetstore.unity.com/packages/3d/props/interior/realistic-interiors-vol1-148120)
- Realistic Apartment asset pack (Friki_Studio): $14.99. All 4K PBR textures with Albedo, Normal, Roughness, Metallic and AO maps. Very heavy: the bedroom set alone is 1,116K tris. — [store page](https://assetstore.unity.com/packages/3d/props/interior/realistic-apartment-asset-pack-202540)
- The Abandoned House – Modular Pack (The Naked Dev): no price returned. 160 prefabs, 2K textures, 68 to 6.8k tris per asset, no LODs. — [store page](https://assetstore.unity.com/packages/3d/environments/urban/the-abandoned-house-modular-pack-248113)
- House Prop Package / 260+ Variations (PackDev): $49.99. Average 4,370 tris per mesh, 512 px to 4K textures, "LODs: Not included." — [store page](https://assetstore.unity.com/packages/3d/props/house-prop-package-260-variations-226293)
- Modular Suburban House (FANNΞC): $19.99, an American-style modular shell with 87 prefabs and 2K textures. It is mostly architecture with few furnishings. — [store page](https://assetstore.unity.com/packages/3d/environments/modular-suburban-house-311154)

**Photoscanned packs**
- The only photogrammetry household items I found are DeltaRaccoons' small crockery packs:
  - Scan Kitchen Service 02: 8 models, $11.99. — [store page](https://assetstore.unity.com/packages/3d/props/interior/scan-kitchen-service-02-pack-props-211537)
  - Scan Kitchen Service 01: 4 models, $7.99. — [store page](https://assetstore.unity.com/packages/3d/props/interior/scan-kitchen-service-01-pack-props-208336)
  - Both have 4 LOD levels and 2048 px maps (Albedo, Normal, MetallicSmoothness), and are Built-in and URP on 2020.1.6.

### Inferences
- For first-person quality and US-suburb fit with active support, the strongest combination is Finward's ecosystem: Suburb Neighborhood (houses and street) plus Atmospheric House (clean-to-worn interiors) plus House Props & Furniture Vol. 2 (dense 2K–4K props). It is the only realistic set that is 5-star, highly rated, Unity 6 tested on all three pipelines, and updated in Sep 2026.
- NOT_Lonely's HQ Residential House is the best-proven single American house by reputation (116 ratings and a shipped-games claim). It needs a Unity 6 / URP smoke test because the store does not list Unity 6.
- ArchVizPRO has the highest texture fidelity (4K) and Unity 6 URP support, but its interiors are European or luxury spaces. It suits cherry-picking props, not an American suburb.

### Gaps
- I found no independent Reddit or r/Unity3D quality comparisons of these packs. Searches returned only store pages and an [80.lv article on Atmospheric House](https://80.lv/articles/creating-an-atmospheric-house-in-unity), which I did not read.
- I found no Asset Store listings for Dekogon, Next Level 3D (apart from small 2020 studio-apartment scenes such as [Vol.3, $19.99](https://assetstore.unity.com/packages/3d/environments/urban/hq-archviz-modern-studio-apartment-3-168430) at 730k faces and 128 px to 4K textures), Leartes, Kobra or NatureManufacture whole-house interiors. These publishers are mostly on Fab/Unreal or have no such Unity pack (unverified).

---

## Q2. Which packs explicitly support URP and Unity 6?

### Takeaway
The store's compatibility tables list Unity 6 (6000.x) with URP for these packs:
- Suburb Neighborhood (6000.0.83f1)
- Atmospheric House (6000.0.16f1)
- House Props & Furniture Vol. 2 (6000.0.83f1)
- House Furniture Pack (6000.0.83f1)
- Residential House Pack (URP) (6000.5.1f1, URP only)
- HD Apartment (6000.0.59f2)
- Interior Realistic (ithappy) (6000.0.28f1)
- Country houses with interiors (6000.3.11f1)
- All ArchVizPRO URP volumes (6000.0.48f1)

HQ Residential House and HQ Suburban House support URP but do not list Unity 6. American Home Asset is URP on 2022.3 only.

### Cited Findings
- Finward's three main packs were updated on Sep 25–26, 2026, with 6000.0.83f1 tested for Built-in, URP and HDRP:
  - [Suburb Neighborhood](https://assetstore.unity.com/packages/3d/environments/urban/suburb-neighborhood-house-pack-modular-72712)
  - [House Props Vol. 2](https://assetstore.unity.com/packages/3d/props/interior/house-props-furniture-vol-2-265523)
  - [House Furniture Pack](https://assetstore.unity.com/packages/3d/props/house-furniture-pack-88646)
- HQ Residential House (NOT_Lonely) lists only 2019.4.38f1 (Built-in, URP, HDRP), even though its latest version 2.2.1 is dated 2024-12-17. — [store page](https://assetstore.unity.com/packages/3d/environments/urban/hq-residential-house-48976)
- HQ Suburban House (Gabro Media) is tested up to 2023.2.8f1 on all three pipelines. — [store page](https://assetstore.unity.com/packages/3d/environments/urban/hq-suburban-house-81890)
- Residential House Pack (URP) (Nimoyo) is "URP Version Only," made with Shader Graph, and lists Unity 6000.5.1. — [store page](https://assetstore.unity.com/packages/3d/environments/urban/residential-house-pack-urp-345862)
- Every ArchVizPRO URP volume "supports only URP." Each lists 6000.0.48f1. — [Vol.6](https://assetstore.unity.com/packages/3d/environments/urban/archvizpro-interior-vol-6-urp-274067), [Vol.8](https://assetstore.unity.com/packages/3d/environments/urban/archvizpro-interior-vol-8-urp-226014)
- Built-in only, so URP needs manual conversion:
  - [Apartment Kit](https://assetstore.unity.com/packages/3d/environments/apartment-kit-124055)
  - [Realistic Interiors Vol1](https://assetstore.unity.com/packages/3d/props/interior/realistic-interiors-vol1-148120)
- No pipeline table at all:
  - [Vintage House](https://assetstore.unity.com/packages/3d/environments/vintage-house-98229)
  - [HQ Modular House Interior Pack](https://assetstore.unity.com/packages/3d/environments/urban/hq-modular-house-interior-pack-107018)
  - [HQ Modern House Complete Pack](https://assetstore.unity.com/packages/3d/environments/hq-modern-house-complete-pack-162631)

### Inferences
- If a pack lists a URP package for 2019–2023 but not Unity 6 (NOT_Lonely, Gabro Media), it will probably still import in Unity 6 URP after a material upgrade. This should be tested before purchase decisions; it is not guaranteed.

### Gaps
- Unity 6 listings only show what the publisher submitted for testing. I could not verify real-world import problems (shader errors, broken Shader Graph nodes) in 6000.x for any pack.

---

## Q3. Which packs include LODs, and what are their poly and texture budgets?

### Takeaway
Explicit LODs are rare among whole-house packs. The packs that list them:
- HQ Suburban House: LOD models for all props; house about 40k tris, demo scene about 300k.
- HQ Modular House Interior Pack: "LOD system for all objects."
- ArchVizPRO Vol.8: lists LODs.
- House Props & Furniture Vol. 2: LODs only for its heaviest objects.
- DeltaRaccoons scan packs: LOD0–LOD3.
- Residential House Pack (URP): LODs only on vegetation.

Most others state no LODs. They rely instead on moderate per-object tris and 2K textures.

### Cited Findings

| Pack | LODs | Tri budget | Textures |
|---|---|---|---|
| HQ Suburban House | "LOD models provided" | House ~40k, demo scene ~300k | PBR metallic |
| HQ Residential House | Not stated | 135k tris in demo scene | PBR |
| Suburb Neighborhood | Not stated | ~1.5M tris in demo scene | 256 px – 2K (BaseColor / MaskMap / Normal) |
| Atmospheric House | Not stated | ~1.1M tris in demo scene | Mostly 2K, 512 px – 4K, plus Multimask |
| House Props & Furniture Vol. 2 | Only on a few heavy objects | ~940k tris in demo scene, 356 meshes | 1K – 4K (mostly 2K/4K) |
| American Home Asset | No | 200k – 300k tris | 282 textures at 2048 px, PBR |
| Residential House Pack (URP) | Vegetation only (2–3 levels) | Not stated | 512 px – 2K (Albedo, Metallic, Normal, Occlusion, Height) |
| HD Apartment | Not stated | "Low poly" | 2K PBR (incl. Height and Mask maps) |
| ithappy Interior Realistic | Not stated | 328k tris for whole pack | 2048 px (color, roughness only) |
| ArchVizPRO Vol.8 | "Level of detail (LOD)" listed | Not stated | 4K |
| Realistic House Interior&Exterior | No | 24 – 5,000 polys per model | 512 px – 2K (Albedo, Normal, Metallic) |
| Realistic Apartment asset pack | Not stated | Bedroom set alone 1,116K tris | All 4K PBR |
| The Abandoned House – Modular Pack | No | 68 – 6.8k tris per asset | 2K |
| House Prop Package / 260+ Variations | "LODs: Not included" | Avg 4,370 tris per mesh | 512 px – 4K |
| DeltaRaccoons Scan Kitchen packs | LOD0–LOD3 | LOD0 ~1.3k – 10k tris | 2K, photogrammetry |

Sources for each row:
- HQ Suburban House: [store page](https://assetstore.unity.com/packages/3d/environments/urban/hq-suburban-house-81890)
- HQ Residential House: [store page](https://assetstore.unity.com/packages/3d/environments/urban/hq-residential-house-48976)
- Suburb Neighborhood: [store page](https://assetstore.unity.com/packages/3d/environments/urban/suburb-neighborhood-house-pack-modular-72712)
- Atmospheric House: [store page](https://assetstore.unity.com/packages/3d/environments/urban/atmospheric-house-modular-192712)
- House Props & Furniture Vol. 2: [store page](https://assetstore.unity.com/packages/3d/props/interior/house-props-furniture-vol-2-265523)
- American Home Asset: [store page](https://assetstore.unity.com/packages/3d/environments/american-home-asset-interior-exterior-328239)
- Residential House Pack (URP): [store page](https://assetstore.unity.com/packages/3d/environments/urban/residential-house-pack-urp-345862)
- HD Apartment: [store page](https://assetstore.unity.com/packages/3d/environments/urban/hd-apartment-97614)
- ithappy Interior Realistic: [store page](https://assetstore.unity.com/packages/3d/props/interior/interior-realistic-low-poly-3d-models-pack-241355)
- ArchVizPRO Vol.8: [store page](https://assetstore.unity.com/packages/3d/environments/urban/archvizpro-interior-vol-8-urp-226014)
- Realistic House Interior&Exterior: [store page](https://assetstore.unity.com/packages/3d/environments/urban/realistic-house-interior-exterior-197957)
- Realistic Apartment asset pack: [store page](https://assetstore.unity.com/packages/3d/props/interior/realistic-apartment-asset-pack-202540)
- The Abandoned House – Modular Pack: [store page](https://assetstore.unity.com/packages/3d/environments/urban/the-abandoned-house-modular-pack-248113)
- House Prop Package: [store page](https://assetstore.unity.com/packages/3d/props/house-prop-package-260-variations-226293)
- DeltaRaccoons Scan Kitchen Service 02: [store page](https://assetstore.unity.com/packages/3d/props/interior/scan-kitchen-service-02-pack-props-211537)

### Inferences
- For a zombie game that streams several houses, Finward's demo scenes at about 1–1.5M tris (with no LODs stated) need occlusion culling and room-by-room loading. NOT_Lonely (135k) and Gabro Media (about 40k for the house, with LODs) are much lighter per house.

### Gaps
- The Finward pages do not state LODs for Suburb Neighborhood or Atmospheric House, and I could not inspect the package contents.

---

## Q4. Which packs show the "Created with AI" label on the store page?

### Takeaway
None of the 30+ house and interior candidates I checked have an AI disclosure. The `aiDescription` field was empty for all of them. The only AI-disclosed pack I found in this space is Art Equilibrium's "American Suburb Top-Down Pack." It is realistic but built for top-down cameras.

### Cited Findings
- American Suburb Top-Down Pack (Art Equilibrium) carries this AI disclosure: "Some high-poly source models and texture elements were created with the assistance of AI tools … Any AI-generated textures were manually edited and refined in Adobe Photoshop." — [store page](https://assetstore.unity.com/packages/3d/environments/urban/american-suburb-top-down-pack-395606)
- Other details for that pack:
  - Price: $14 on sale (list $34.99).
  - Rating: 5★ from 17 ratings.
  - Pipelines: Built-in, URP and HDRP on 6000.0.74f1.
  - Content: 749 prefabs with 2K textures. Props are 4–850 polys and architecture is 4–3,480 polys. No LODs.
  - Released 2026-07-26.
  - It is designed for top-down and isometric games, so it is not first-person quality.
- Every pack in the Q1 table, plus the lower-value packs and the DeltaRaccoons scans, had an empty AI disclosure field on 2026-10-03. (Sources: the respective store pages linked above.)

### Inferences
- The older, established packs (2015–2024) predate the disclosure requirement or are hand-made. If AI-free provenance matters, the Finward, NOT_Lonely, Gabro Media and ArchVizPRO packs are safe picks as of today.

### Gaps
- I inferred that a filled `aiDescription` is what drives the visible "Created with AI" badge from the store data. I did not compare it against a screenshot of the rendered page.

---

## Q5. Which packs look specifically American and which look European?

### Takeaway
**Explicitly American:**
- HQ Residential House: "American-style house," tagged usa.
- American Home Asset: single-story American house with a garage and laundry appliances.
- Realistic House Interior&Exterior: "American-style."
- Modular Suburban House (FANNΞC): "American-style," shell only.
- PolySquid Country houses: rural "redneck" US style.
- Finward Suburb Neighborhood and Atmospheric House: tagged Suburb, with porches, mailboxes and electric poles, which reads as North American.

**Explicitly European or non-US:**
- ArchVizPRO Vol.3: "European apartment."
- ArchVizPRO Vol.6: "Scandinavian house."
- ArchVizPRO Vol.7: Azuma House, a Japanese reference.
- ArchVizPRO Vol.9/10: luxury villa and pool retreat.

### Cited Findings
- HQ Residential House is described as "fully interactive American-style house." — [store page](https://assetstore.unity.com/packages/3d/environments/urban/hq-residential-house-48976)
- American Home Asset is described as a "single-story American-style house," with an openable fridge, oven, dishwasher and washing machine, and a 1-car garage. — [store page](https://assetstore.unity.com/packages/3d/environments/american-home-asset-interior-exterior-328239)
- Realistic House Interior&Exterior says "multi-story house in American-style," with a laundry room and garage. — [store page](https://assetstore.unity.com/packages/3d/environments/urban/realistic-house-interior-exterior-197957)
- Suburb Neighborhood includes "mailboxes, cars, lamps, electric poles" and a suburban road system. — [store page](https://assetstore.unity.com/packages/3d/environments/urban/suburb-neighborhood-house-pack-modular-72712)
- Atmospheric House includes a modular "porch." — [store page](https://assetstore.unity.com/packages/3d/environments/urban/atmospheric-house-modular-192712)
- ArchVizPRO interiors are European or Scandinavian:
  - Vol.3 is "a beautiful European apartment." — [store page](https://assetstore.unity.com/packages/3d/environments/urban/archvizpro-interior-vol-3-urp-270835)
  - Vol.6 is a "Scandinavian house." — [store page](https://assetstore.unity.com/packages/3d/environments/urban/archvizpro-interior-vol-6-urp-274067)

### Inferences
- Because Finward is a Finnish studio, its interiors may mix Nordic and US cues. The suburb, mailbox and porch elements suggest a North-American target, but this should be checked against screenshots (outlet type, appliance styling).

### Gaps
- None of the store pages mention US-style electrical outlets, light switches or appliance standards (top-freezer fridge, front-load washer and so on). Confirming them needs a visual check of the screenshots or videos, which I did not do.
