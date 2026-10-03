# Unity Asset Store: realistic bathroom, bedroom, living room and laundry packs (for a Unity 6 URP first-person zombie game set in a present-day US suburb)

**How this was checked.** Every store figure below comes from the live assetstore.unity.com product page, fetched on 2026-10-03. The data was read from the store's embedded page state: price, rating, render pipelines (SRP table), supported Unity versions, the `aiDescription` field and the current version with its date.

**Field meanings:**
- Under "SRP", `standard` means Built-in, `lightweight` means URP, `hd` means HDRP, and `custom` means a custom SRP.
- "Ratings n" is the number of star ratings. "Reviews" is the number of written reviews.
- The store's `rating.average` field is a whole number. It shows 0 for packs with very few ratings, so "avg 0" means not enough ratings, not 0 stars.

**AI disclosure.** "Created with AI" means the store page fills in the `aiDescription` disclosure field.
- Two packs here had it filled in: Laundry & Functional Washing Machine Pack (318699) and American Suburb Top-Down Pack (395606).
- Every other pack listed had an empty AI field when fetched.

**Sale status.** An "Autumn Sale 2026" banner was live sitewide ("Save 50% off on top sellers and 70% off new daily drops"). Even so, every pack below showed no discount (final price = original price) except 395606. Prices can change during the sale.

**Prices that could not be read.** Two packs returned a null price object in the page state: Living Room Furniture (261648) and Modern Furniture & Decorations for Living Room (272297). Their prices are **unverified**. They may be unpurchasable or may load client-side.

## Best realistic BATHROOM packs?

### Takeaway
No bathroom pack is clearly the best, and none has many ratings (all have 0–1 ratings).
- **Bathroom PBR – Full Pack (Arigasoft)** has the most content and the best stated specs: 90+ unique props, per-prop triangle counts, textures up to 4K, and Built-in, URP and HDRP. It is not listed for Unity 6.
- **Dirty Bathroom Collection – HQ (VIS Games)** is the best thematic fit for a zombie game. It is Unity 6 native, has 4K textures, and every fixture comes in clean, dirty and bloody variants. It contains only a few fixture types.
- **Bathroom Environment Product Props (CoolWorks)** is the only bathroom pack with real LOD chains and URP builds for Unity 6. It is clutter only (bottles, cans and so on), not fixtures.

### Cited Findings
- **Bathroom PBR – Full Pack** by Arigasoft. [Store](https://assetstore.unity.com/packages/3d/props/interior/bathroom-pbr-full-pack-274322)
  - **Price:** $24.99 regular, not on sale.
  - **Ratings:** 0 ratings, 0 reviews.
  - **Pipelines:** SRP table lists Built-in, URP and HDRP for 2021.3.1f1. Supported Unity version is 2021.3.1 only, with **no 6000.x listed**.
  - **Size and version:** 1,844 assets, about 1.68 GB. v1.0, published 2024-04-12, never updated.
  - **AI field:** empty.
  - **Contents:** "170+ elements (90+ unique props)". These include 4 bathtubs (~1,100–6,200 tris), 1 bidet (~1,300 tris), 1 toilet (~4,000 tris), 1 shower (~2,500 tris), 2 washbasins (~1,060–1,080 tris), 7 furnitures, 2 laundry baskets, 1 water heater, 6 mirrors, outlets and switches, plus walls, floors, ceilings, doors and windows.
  - **Textures:** 1 PBR material per prop, 5 textures per prop. Resolution is 1024 for small props and 4096 for large ones. Maps are Albedo, Metallic/Smoothness, HDRP Mask, Normal, AO and Emissive.
  - **Other:** "No demo scene available". Built at real size.
  - **LODs:** not mentioned.
- **Dirty Bathroom Collection – HQ** by VIS Games. [Store](https://assetstore.unity.com/packages/3d/props/dirty-bathroom-collection-hq-333160)
  - **Price:** $14.95 regular.
  - **Ratings:** 0 ratings.
  - **Pipelines:** Built-in, URP and HDRP on **Unity 6000.0.24**.
  - **Version:** v1.0, 2025-09-11. 283 assets, about 816 MB.
  - **AI field:** empty.
  - **Contents:** "2 different sinks, a shower and 4 different toilettes". Every prop has "a clean, dirty and bloody version and 3 different color texture-sets". 189 prefabs in total.
  - **Textures:** 4096 maps: Albedo, Normal and a Mask map (AO, Metallic, Smoothness).
  - **Not included:** tubs and vanities are not listed. Poly counts and LODs are not stated.
- **Bathroom Environment Product Props** by CoolWorks Studio. [Store](https://assetstore.unity.com/packages/3d/props/interior/bathroom-environment-product-props-168169)
  - **Price:** $29.99.
  - **Ratings:** 0 ratings.
  - **Pipelines:** separate builds, with URP on **6000.0.40f1**, HDRP on 6000.0.39f1 and Built-in on 2021.3.31f1.
  - **Version:** v1.0.1, 2025-03-17. 403 assets.
  - **AI field:** empty.
  - **Contents:** 99 prefabs and 30 meshes of bathroom and drugstore products.
  - **LODs:** "around 5 LoD variants per model". Examples: Bottle_Plastic_03 ranges 98–9,016 tris over 6 LODs, and Combs range 28–10,152 tris.
  - **Textures:** up to 4K Albedo, Normal, AO and Specular/Smoothness, in both specular and metalness workflows.
  - **Not included:** no toilets or tubs. It is consumables and clutter only.
- **Bathroom Assets** by DevDen. [Store](https://assetstore.unity.com/packages/3d/props/interior/bathroom-assets-201230)
  - **Price:** $14.99.
  - **Ratings:** 0 ratings.
  - **Pipelines:** Built-in, URP and HDRP on 2021.3.0f1. No 6000.x.
  - **Version:** v1.1, 2025-03-27.
  - **AI field:** empty.
  - **Contents and specs:** 19 models and 52 prefabs, 57,444 tris in total, 2048 textures (Albedo, Metallic, Normal and Occlusion; Base, Mask and Normal for HDRP).
- **Bathroom / 43+ Assets** by PackDev. [Store](https://assetstore.unity.com/packages/3d/props/bathroom-43-assets-225918)
  - **Price:** $15.99.
  - **Ratings:** 0 ratings.
  - **Pipelines:** Built-in and URP on 2019.4.34f1.
  - **Version:** v1.0, 2022-07-08.
  - **AI field:** empty.
  - **Specs:** 43 meshes and 43 prefabs, about 3,035 tris per mesh on average, textures from 1024 to 4096, 195 textures in total. "LODs: Not included".
- **Realistic Modern Urban Public Bathroom Asset Package** by Aligned Games. [Store](https://assetstore.unity.com/packages/3d/environments/urban/realistic-modern-urban-public-bathroom-asset-package-308885)
  - **Price:** $20.00.
  - **Ratings:** 0 ratings.
  - **Pipelines:** Built-in, URP, HDRP and custom on **Unity 6000.0.33**.
  - **Version:** v1.0, 2025-02-24.
  - **AI field:** empty.
  - **Specs:** 31 assets (stalls, urinals, toilets, sinks), about 500 polys on average, textures 256–2048 with an average of **512**. Low texture budget.
- **PBR Toilet & Bathroom Props** by DCF Productions. [Store](https://assetstore.unity.com/packages/3d/props/interior/pbr-toilet-bathroom-props-173882)
  - **Price:** $4.99.
  - **Ratings:** 0 ratings.
  - **Pipelines:** SRP table is empty. Unity 2018.4.2. URP and HDRP need material conversion.
  - **Version:** v1.3, 2021-01-25.
  - **Contents:** toilet, urinal, bathtub, shower, sink (2 variants), plunger, toiletries, scale and more. Textures 512–4K.
  - **Oddity:** the description mentions "Blueprint class for articulation", which is Unreal wording. The pack looks like a port from Unreal.
- **Bathroom Pack PBR** by Nexus Gamesoft. [Store](https://assetstore.unity.com/packages/3d/props/interior/bathroom-pack-pbr-75855)
  - **Price:** $12.95.
  - **Ratings:** 0 ratings.
  - **Unity version:** 5.0.0. Last update v1.1, 2017-01-18.
  - **Contents:** 18 items, including a **"Squat Toilet"**, bathtub, shower, sink, water heater and washing machine.
  - **Textures:** 2048 Albedo, MetallicSmoothness, Normal, Occlusion and Height maps.
- **Painless Props – Bathroom and Laundry** by Little Arms Studios. [Store](https://assetstore.unity.com/packages/3d/painless-props-bathroom-and-laundry-43042)
  - **Price:** $4.99.
  - **Ratings:** 5 stars from 3 ratings, 2 reviews.
  - **Unity version:** 5.1.1/5.6.0. Last update v1.3, 2017-04-11.
  - **Contents:** low-poly toilet, shower stall, sink, washer, dryer, iron, ironing board and more.

### Inferences
- **Best fit for a zombie game:**
  - Pair Dirty Bathroom HQ (fixtures with blood and dirt states, Unity 6) with CoolWorks Bathroom Environment Product Props (LOD'd clutter, Unity 6 URP).
  - Add Arigasoft Full Pack if bathtubs, cabinets and towels are needed. It claims URP support but is only tested up to 2021.3, so it needs a Unity 6 test import.
- **Weaker options:**
  - Nexus (75855), DCF (173882) and Painless Props (43042) are 2015–2021 Built-in-era packs. They are low priority for a Unity 6 URP project.
  - Aligned Games' public restroom pack is a commercial restroom, not a home bathroom, and its textures average 512.

### Gaps
- I found no bathroom pack with a meaningful number of ratings. Quality could not be checked through reviews.
- Arigasoft does not say whether it includes LODs.
- Dirty Bathroom HQ does not state poly counts.
- Whether the toilets and tubs look American (close-coupled toilet, alcove tub with tile surround, US vanity) could not be checked without viewing the screenshots. The page text does not say.

## Best realistic BEDROOM packs?

### Takeaway
There is no strong, well-rated, Unity 6 URP realistic bedroom pack.
- **Next Level 3D "HQ ArchViz Bedroom Vol.1"** has the highest fidelity: Built-in, URP and HDRP, 4K textures. It is a complete heavy scene (420k tris) and is only tested on 2020.3.
- **POLYBOX "Bedroom Pack"** is the only bedroom pack updated for Unity 6 (6000.3.2, 2026-05-22). It is Built-in only, has 5 stars from 7 ratings, and is a very light pack (under 10k tris) with baked lighting.
- **Robot Skeleton "Bedroom Items – HDRP"** has fully stated specs: the bed is 7,998 tris with 4K maps. It ships HDRP and Built-in folders only, with no URP.
- For US suburban bedrooms, the general house-props packs (next section) are likely the better source.

### Cited Findings
- **HQ ArchViz Bedroom Vol.1** by Next Level 3D. [Store](https://assetstore.unity.com/packages/3d/environments/urban/hq-archviz-bedroom-vol-1-200329)
  - **Price:** $19.99 regular.
  - **Ratings:** 0 ratings.
  - **Pipelines:** Built-in, URP and HDRP on 2020.3.1f1. **No 6000.x listed.**
  - **Version:** v1.0, 2021-07-26. About 1.13 GB.
  - **AI field:** empty.
  - **Specs:** 31 textures from 1024 to 4096. Scene is 420k tris and 259.9k verts. 30 meshes and 29 prefabs, PBR, and a "Modular Bed". It is a "complete interior scene" of a "modern bedroom".
  - **LODs:** not stated.
- **Bedroom Pack** by POLYBOX ("Hazelwoodloft" series). [Store](https://assetstore.unity.com/packages/3d/environments/urban/bedroom-pack-38395)
  - **Price:** $34.99.
  - **Ratings:** 5 stars from 7 ratings, 1 review.
  - **Pipelines:** Built-in (`standard`) only, listed for 2020.2.1f1 and **6000.3.2f1**.
  - **Version:** v10.0, 2026-05-22.
  - **AI field:** empty.
  - **Specs:** 46 assets, "the whole pack is below 10 000 triangles", 17 textures and cubemaps. Lighting is baked externally in Mental Ray, with day and night lightmaps. Style is "minimal & modern".
- **Bedroom Items – HDRP** by Robot Skeleton. [Store](https://assetstore.unity.com/packages/3d/props/interior/bedroom-items-hdrp-199024)
  - **Price:** $9.99.
  - **Ratings:** 1 rating, 1 review.
  - **Pipelines:** Built-in and HDRP on 2020.3.0f1. **No URP.**
  - **Version:** v1.0, 2021-07-23.
  - **Contents:** 14 models from 60 to 7,998 tris. The bed (frame, mattress, sheet, 4 pillows) is 7,998 tris with 4096 maps. Also a desk, chair, side table, lamp, sideboard, laptop and others.
  - **Maps:** albedo, roughness, normal, AO, plus metallic and emission.
  - **Not included:** walls and floors.
- **Bedroom Props & Interior Pack** by ARMO Studios. [Store](https://assetstore.unity.com/packages/3d/props/interior/bedroom-props-interior-pack-372022)
  - **Price:** $11.99.
  - **Ratings:** 0 ratings.
  - **Pipelines:** URP, HDRP and custom on **6000.4.0f1**.
  - **Version:** v1.0, 2026-04-28.
  - **AI field:** empty.
  - **Specs:** 31 unique objects and only about 3 MB, with "Textures: Only included materials other than photo frame, laptop screen and watch face". The bed is just 288 polys. **Not realistic first-person quality** despite the "realistic" wording.
- **Realistic Furnitures Pack** by Pretorius Lab. [Store](https://assetstore.unity.com/packages/3d/environments/realistic-furnitures-pack-257190)
  - **Price:** $5.00.
  - **Ratings:** 1 rating.
  - **Pipelines:** URP and Built-in on 2021.3.16f1.
  - **Version:** v1.0, 2023-07-25.
  - **Specs:** 46 prefabs, average 700 polys, 2048 textures.

### Inferences
- I found no single realistic bedroom pack that is URP, Unity 6 and well rated.
- Next Level 3D is the most realistic-looking candidate on paper. Its 420k-tri scene should be treated as a source of hero props, not something to drop in as-is.
- POLYBOX depends on baked lightmaps and a Built-in-only setup. That suits a dynamic-lit URP survival game poorly.
- None of the bedroom pages mention king beds, recliners or other US-specific items. Style words are "modern" and "minimal", which suggests European or loft-style design.

### Gaps
- No bedroom pack page mentions a dresser by name except through general house packs. "Sideboard" appears in Robot Skeleton's pack.
- US-style bed sizes are unverified.
- Next Level 3D's LODs and per-item poly counts are not stated.

## Best realistic LIVING ROOM packs (and general house packs covering all rooms)?

### Takeaway
For a US suburb, the strongest picks are Finward Studios' two packs.
- **House Props & Furniture Vol. 2:** $79, 5 stars from 11 ratings, Built-in, URP and HDRP on Unity 6000.0.83, updated 2026-09-26, 350+ worn-looking objects.
- **Suburb Neighborhood House Pack (Modular):** $89, 5 stars from 127 ratings and 95 reviews, Unity 6000.0.83, v2.0.0 updated 2026-09-25. It explicitly targets suburban neighborhoods with interior furniture.

Living-room-only options:
- **Willard Artson's "Modern Furniture and Decorations for Living Room"** has the best stated budget (full LOD0–2 chains, 4K textures). Its price could not be read.
- **PackDev "Modern Living Room / 36+ Assets"** has no LODs.
- **ArchVizPRO Interior Vol.6 URP** (Unity 6, 200+ props) is high-end but **Scandinavian** in style.

### Cited Findings
- **House Props & Furniture Vol. 2** by Finward Studios. [Store](https://assetstore.unity.com/packages/3d/props/interior/house-props-furniture-vol-2-265523)
  - **Price:** $79.00 regular, not discounted when fetched.
  - **Ratings:** 5 stars from 11 ratings, 11 reviews.
  - **Pipelines:** Built-in, URP and HDRP for 2019.4.30f1, 2021.3.30f1 and **6000.0.83f1**.
  - **Version:** v1.2.0, 2026-09-26. 999 assets, about 2.1 GB.
  - **AI field:** empty.
  - **Specs:**
    - 356 meshes and 177 textures, "from 1024 to 4096 (mostly 2k and 4k)".
    - Maps: BaseColor, MaskMap, Normal and Emissive.
    - "Objects have slight wearing". Cabinets, drawers and doors are openable but not animated.
    - "LOD's only for a few most triangle heavy objects". Custom lightmap UVs.
    - About 940k tris in the demo scene.
  - Described as "Suitable also as an addition for Atmospheric House (Modular) or Suburb Neighborhood House Pack (Modular)".
  - **Reviews:** all 5-star, with titles such as "THE BEST", "High quality props" and "Unbelievable", dated 2024-02 to 2026-05. [Reviews](https://assetstore.unity.com/packages/3d/props/interior/house-props-furniture-vol-2-265523/reviews)
- **Suburb Neighborhood House Pack (Modular)** by Finward Studios. [Store](https://assetstore.unity.com/packages/3d/environments/urban/suburb-neighborhood-house-pack-modular-72712)
  - **Price:** $89.00.
  - **Ratings:** 5 stars from 127 ratings, 95 reviews.
  - **Pipelines:** Built-in, URP and HDRP listed for 2019.4.25, 2020.1.17, 2022.3.10 and **6000.0.83**.
  - **Version:** v2.0.0, 2026-09-25. About 4.5 GB.
  - **AI field:** empty.
  - **Contents:** "modular houses with exteriors and interiors… interior furniture such as beds, chairs, tables, paintings etc." The page notes "URP is default render pipeline for Unity 6".
  - **User opinion:** a search summary of reviews says users were amazed "how realistic the furniture looks" with "nice visuals even in URP". This came from a search snippet of the reviews page and was not read in full. [Reviews](https://assetstore.unity.com/packages/3d/environments/urban/suburb-neighborhood-house-pack-modular-72712/reviews)
- **Modern Furniture and Decorations for Living Room** by Willard Artson. [Store](https://assetstore.unity.com/packages/3d/props/furniture/modern-furniture-and-decorations-for-living-room-272297)
  - **Price:** **unverified**. The price object was null in the page state.
  - **Ratings:** 0 ratings.
  - **Pipelines:** Built-in, URP and HDRP listed for 2021.3.29f1. It uses the Standard shader, with conversion needed.
  - **Version:** v1.0, 2024-02-21.
  - **Textures:** 4K albedo and normal.
  - **LODs:** "Each model that contains more than 100 tris has been optimized with LODs". Examples: Sofa LOD0 5,092 / LOD1 1,636 / LOD2 868; Armchair 3,162 / 1,050 / 666; Television 508 / 220 / 124.
  - **Contents:** sideboards, sofas, armchairs, tables, shelves, TV, remote, lamps, plants, carpets and more.
- **Modern Living Room / 36+ Assets** by PackDev. [Store](https://assetstore.unity.com/packages/3d/props/modern-living-room-36-assets-226174)
  - **Price:** $14.99.
  - **Ratings:** 0 ratings.
  - **Pipelines:** Built-in, URP and custom on 2019.4.34f1.
  - **Version:** v1.0, 2022-07-28.
  - **Specs:** 36 meshes averaging 1,958 tris, textures 512–4096, 115 textures. "LODs: Not included".
  - **Related:** PackDev's mega bundle **House Prop Package / 260+ Variations** costs $49.99. It has 249 meshes averaging 4,370 tris, 960 textures, no LODs, Built-in and URP on 2019.4.34, v1.0 from 2022-07-12, and 0 ratings. [Store](https://assetstore.unity.com/packages/3d/props/house-prop-package-260-variations-226293)
- **ArchVizPRO Interior Vol.6 URP** by ArchVizPRO. [Store](https://assetstore.unity.com/packages/3d/environments/urban/archvizpro-interior-vol-6-urp-274067)
  - **Price:** $39.99.
  - **Ratings:** 1 rating.
  - **Pipelines:** URP for 2022.3.13f1 and **6000.0.48f1**.
  - **Version:** v1.1, 2025-06-12. About 4.8 GB.
  - **AI field:** empty.
  - **Contents:** "fully navigable Scandinavian house" with living room, kitchen, bedroom, studio and bathroom. "more than 200 furniture and props", 4K textures.
  - **LODs:** not stated for Vol.6. Vol.4 HDRP ($39.99, HDRP only, 2021.3.4) does list "LOD (Levels of Detail)". [Vol.4](https://assetstore.unity.com/packages/3d/environments/urban/archvizpro-interior-vol-4-hdrp-211871)
- **Living Room Furniture** by Polyvers. [Store](https://assetstore.unity.com/packages/3d/props/interior/living-room-furniture-261648)
  - **Price:** **unverified** (null price object).
  - **Pipelines:** Built-in and HDRP on 2021.3.11f1.
  - **Specs:** 11 meshes, 2048 textures, sofa 2,456 polys.
- **Casual Living Room Pack** by GoGo Creator: $16.99, URP and HDRP, 2022.3.5. It uses a palette/gradient texture approach (Albedo and Transparent only). **Stylized, not realistic.** [Store](https://assetstore.unity.com/packages/3d/props/interior/casual-living-room-pack-303174)
- **Sofa Pack** by TechLevel. [Store](https://assetstore.unity.com/packages/3d/props/interior/sofa-pack-101967)
  - **Price:** $8.00.
  - **Unity version:** 5.6.0, from 2017.
  - **Contents:** 7 sofa types and 404 prefabs, with HighPoly, LOD0, LOD1 and LOD2 plus LOD Groups.
- **Living Room props pack vol.1** by openplay. [Store](https://assetstore.unity.com/packages/3d/props/furniture/living-room-props-pack-vol-1-138422)
  - **Price:** $8.00.
  - **Unity version:** 5.6.6.
  - **Specs:** sofa about 266 tris, 1024 atlas textures. Mobile-grade.

### Inferences
- **Recommended core:** Finward Vol. 2 plus the Suburb Neighborhood House Pack.
  - Same publisher and art style.
  - Unity 6 listed with URP and HDRP.
  - Recently updated (Sept 2026).
  - The only candidates with real review volume.
  - Worn surfaces suit a post-outbreak setting.
- **LODs:** Finward includes LODs only on heavy objects, so draw-call and LOD work will be needed for open-house streaming.
- **Gap filler:** Willard Artson's pack is the best-specified option for LOD'd sofas and TVs if its price and purchasability check out.
- **Style:** ArchVizPRO is premium quality but Scandinavian and archviz-heavy. It fits poorly with a US suburb.

### Gaps
- Finward Vol. 2's itemized contents (whether it has toilets, tubs, washers, beds, recliners) are not listed on the store page. The description gives only counts. Its rooms coverage is **unverified**.
- No living room pack page mentions "recliner".
- The prices of 272297 and 261648 could not be read.

## Best realistic LAUNDRY packs?

### Takeaway
Laundry has the thinnest selection.
- **Robot Skeleton "80s Laundry Pack"** has the best stated specs: 2 washers and 2 dryers at 1.1–1.9k tris with 4K maps, plus baskets and a clothes pile. It is retro and Built-in only.
- **Rip Vertices "Laundry and Functional Washing Machine Pack"** is a modern option with Built-in, URP and HDRP, an animated washer with sound, and baskets. It **has an AI disclosure** for its script, and it lacks a dryer.
- **32cm "Washing Machine Set 3"** is a cheap single 4K PBR washer.
- POLYBOX's Laundry Pack is Unity 6 but Built-in only.
- The laundromat packs (Aligned Games, Nazanin) are commercial settings, not home laundry rooms.

### Cited Findings
- **80s Laundry Pack** by Robot Skeleton. [Store](https://assetstore.unity.com/packages/3d/props/80s-laundry-pack-189378)
  - **Price:** $6.99.
  - **Ratings:** 0 ratings.
  - **Pipelines:** Built-in on 2019.3.7f1.
  - **Version:** v1.0, 2021-02-22.
  - **AI field:** empty.
  - **Contents:** 8 models from 12 to 2,788 tris: Washing Machine 01/02 (1,850 and 1,160 tris), Dryer 01/02 (1,782 and 1,178 tris), round and square baskets, detergent and clothes pile.
  - **Textures:** 4096 maps for the machines and 2048 for the baskets. Maps are albedo, roughness, normal, occlusion and metallic.
- **Laundry and Functional Washing Machine Pack** by Rip Vertices Studio. [Store](https://assetstore.unity.com/packages/3d/props/clothing/laundry-and-functional-washing-machine-pack-318699)
  - **Price:** $19.99.
  - **Ratings:** 0 ratings.
  - **Pipelines:** Built-in, URP and HDRP on 2022.3.55f1.
  - **Version:** v1.0, 2025-05-08.
  - **AI disclosure: YES.** "The WashingMachineController script… was developed with the support of AI-based assistance."
  - **Contents:** washing machine (9,831 tris with clothes, 4,751 without), basket 1,106 tris, clothes drying rack, and clotheslines (about 43.8k tris with clothes).
  - **Textures:** up to 4096.
  - **Interactivity:** 8 animations plus sounds.
- **Washing Machine Set 3** by 32cm. [Store](https://assetstore.unity.com/packages/3d/props/furniture/washing-machine-set-3-336032)
  - **Price:** $4.99.
  - **Pipelines:** Built-in, URP, HDRP and custom on 2021.3.34f1.
  - **Version:** v1.0, 2025-10-23.
  - **Contents and specs:** 1 washer mesh with 3 texture sets, 3,500 tris in total, 4096 PBR maps plus an HDRP mask.
- **Laundry Pack** by POLYBOX (Hazelwoodloft "Wardrobe & Laundry Items"). [Store](https://assetstore.unity.com/packages/3d/props/electronics/laundry-pack-38317)
  - **Price:** $29.99.
  - **Ratings:** 0 ratings.
  - **Pipelines:** Built-in, with Unity versions listed up to **6000.3.2**.
  - **Version:** v10.0, 2026-05-22.
  - **Specs:** 35 assets under 14k tris in total, 3 textures. Style is "minimal design".
- **Modern Washing Machines** by Pixelcloud. [Store](https://assetstore.unity.com/packages/3d/props/interior/modern-washing-machines-49346)
  - **Price:** $9.99.
  - **Unity version:** 5.2.1.
  - **LODs:** included. Washer 1 LOD0 3,564 / LOD1 1,521 / LOD2 824.
  - **Textures:** 2048.
- **Laundromat environments (commercial, not home):**
  - Realistic Laundromat Asset Package by Aligned Games: $15, Unity 6000.0.33, all pipelines, textures averaging 512. [Store](https://assetstore.unity.com/packages/3d/environments/urban/realistic-laundromat-asset-package-253048)
  - Modular Laundry Interior by Nazanin: $19.90, URP only, Unity 6000.3.9, 2048 textures, no LODs, published 2026-08-18. [Store](https://assetstore.unity.com/packages/3d/environments/modular-laundry-interior-397992)
- **Casual Laundry Pack** by GoGo Creator: $29.99, palette textures. **Stylized.** [Store](https://assetstore.unity.com/packages/3d/props/exterior/casual-laundry-pack-303172)

### Inferences
- A home laundry room will probably be pieced together: Robot Skeleton's 80s washers and dryers (converted to URP), plus Rip Vertices for modern baskets and drying racks, or a washer and dryer from the general house packs.
- **Style check:** the "80s" styling may actually suit a US suburb, since older top-load washers are common in US homes. The front-load, European-looking washers in the modern packs may look less American. This needs a check against the screenshots.

### Gaps
- No laundry pack has ratings.
- Whether any pack includes a US-style top-loader with an agitator is unverified (text does not say).
- Rip Vertices does not include a dryer.

## Which look American vs European?

### Takeaway
- **US suburban:** only Finward Studios' pages explicitly position themselves that way ("Suburb Neighborhood"). So does Abstract's new American Suburb Top-Down Pack, but that pack is built for top-down cameras and has an AI disclosure.
- **European, Asian or Scandinavian signals:** several packs carry them, as listed below.

### Cited Findings
- **Finward Studios:** Suburb Neighborhood House Pack targets a "complete suburban neighborhood", and House Props Vol. 2 is marketed as its companion. [Store](https://assetstore.unity.com/packages/3d/environments/urban/suburb-neighborhood-house-pack-modular-72712)
- **American Suburb Top-Down Pack** by Abstract. [Store](https://assetstore.unity.com/packages/3d/environments/urban/american-suburb-top-down-pack-395606)
  - **Price:** $14.00 on sale from $34.99 regular.
  - **Ratings:** 5 stars from 17 ratings, 18 reviews.
  - **Unity version:** 6000.0.74. Built-in, URP and HDRP per its compatibility text.
  - **Purpose:** "realistic American suburb… interiors, props" but "designed primarily for top-down, isometric…" games.
  - **Specs:** props 4–850 polys, 2048 textures, "LOD: No".
  - **AI disclosure: YES.** "Some high-poly source models and texture elements were created with the assistance of AI tools… scripts… created with AI assistance."
- **Arigasoft Bathroom PBR Full Pack** includes a **bidet**, a European fixture. [Store](https://assetstore.unity.com/packages/3d/props/interior/bathroom-pbr-full-pack-274322)
- **Nexus Gamesoft Bathroom Pack PBR** includes a **squat toilet**. [Store](https://assetstore.unity.com/packages/3d/props/interior/bathroom-pack-pbr-75855)
- **ArchVizPRO Interior Vol.6** is a "Scandinavian house". [Store](https://assetstore.unity.com/packages/3d/environments/urban/archvizpro-interior-vol-6-urp-274067)
- **POLYBOX Bedroom and Laundry** are a "minimal & modern" loft series. [Store](https://assetstore.unity.com/packages/3d/environments/urban/bedroom-pack-38395)

### Inferences
- Finward is the safest US-suburban match.
- Arigasoft can still be used if the bidet is left out.
- Abstract's AI-assisted, top-down-oriented pack (no LODs, props of 850 polys or fewer) is unlikely to hold up at first-person distances.

### Gaps
- No pages were found mentioning king beds, recliners, US toilets or US alcove tubs.
- A visual check of screenshots is needed. This was not possible from page text.
- No Reddit or forum threads were found comparing these specific room packs.

## URP + Unity 6 support, LODs, budgets, AI labels (summary)

### Takeaway
**Unity 6 (6000.x) listed with URP:**
- Finward Vol. 2 and Suburb House Pack (6000.0.83)
- Dirty Bathroom HQ (6000.0.24)
- CoolWorks bathroom props (6000.0.40 URP)
- ArchVizPRO Vol.6 (6000.0.48)
- ARMO Bedroom (6000.4.0)
- Aligned Games public restroom and laundromat packs (6000.0.33)
- Nazanin laundromat (6000.3.9)

POLYBOX lists 6000.3.2 but Built-in only.

**Real LOD chains are stated only by:**
- CoolWorks (about 5 per model)
- Willard Artson (LOD0–2)
- TechLevel Sofa Pack
- Pixelcloud washers
- ArchVizPRO Vol.4
- Finward, partially ("only for a few" heavy objects)

**AI disclosures:** only Rip Vertices (318699, script) and Abstract (395606, source models, textures and scripts).

### Cited Findings
- See the per-pack citations above. All figures came from the live store pages fetched 2026-10-03.
- Store-wide Autumn Sale 2026 banner, seen in the page state: "Save 50% off on top sellers and 70% off new daily drops". [Store](https://assetstore.unity.com/packages/3d/props/interior/bathroom-pbr-full-pack-274322)

### Inferences
- Packs listing URP for Unity 2019–2022 only (Arigasoft, Next Level 3D, DevDen, PackDev, Rip Vertices) will probably import into Unity 6 URP with material upgrades. This is not guaranteed.
- Plan a test import for each.

### Gaps
- I did not find reliable third-party (Reddit or forum) quality opinions on any single-room pack. The only opinion signals are store reviews: Finward Vol. 2 (11) and Suburb House Pack (95).
- Dekogon, Kobra Game Studios, Craft Studio, NatureManufacture, Lowlypoly and Elcanetay showed no realistic bathroom, bedroom, living room or laundry pack in my searches. Search results tied Dekogon to Hospital Props and Shopping & Market (Gas Station) packs on Unity. I did not confirm the publisher on those pages. This was not exhaustive, and no live store search API was available.
