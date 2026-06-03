# Track 06 — Glossary / THE DIFFERENCE-MAP: Figma → Photoshop (PSD) High-Fidelity Conversion

> The precise Figma↔PSD concept-mapping + irreversible-loss list + bilingual glossary that lets a
> practitioner "align the two tools' differences so the output looks identical."
> Research date: 2026-06-03. OPUS subagent (Wave-1 dependent: heavily reuses T04-canon + T02-tools + T01-figures facts).
>
> **Field status: PRE-CANONICAL** (inherited from T04). There is no textbook/course on Figma→PSD; the
> "glossary" here is assembled from (a) first-party API/format specs that define each tool's concept set,
> (b) vendor help docs, (c) the cross-tool fidelity corpus of Marc Edwards / Bjango (the single richest
> independent measurement source — reused as T01-Sxxx). This is a **concept-mapping glossary**, not an
> industry-jargon glossary: the high-value content is *where the same word means different things in the
> two tools*, and *what cannot survive the boundary*.
>
> **Type-distribution note** (per template Step 2): this domain is technical/tooling. It is **term-heavy
> and standard-light, and has essentially NO certifications and NO regulations** (it's a craft, not a
> regulated profession). So the 5-type matrix collapses to: Term (dominant), Acronym (some), Standard
> (a handful — file formats & color/type specs), Regulation = **N/A**, Certification = **N/A**.

---

## Source Manifest

> NEW sources for this track are `T06-Sxxx`. Reused cross-track ids (`T04-Sxxx` / `T02-Sxxx` / `T01-Sxxx`)
> appear in evidence tags and are listed in their home-track manifests; the most load-bearing reused ones
> are restated here for convenience with a `(reused)` flag so this file is self-contained.

| source_id | url | bucket | last_checked | author/host | one-line note |
|-----------|-----|--------|--------------|-------------|---------------|
| T06-S001 | https://developers.figma.com/docs/plugins/api/Paint/ | verified_primary | 2026-06-03 | Figma Inc. | Paint types: Solid/**Gradient(4 types)**/Image/Video/**Pattern**; ImagePaint scaleMode FILL\|FIT\|CROP\|TILE |
| T06-S002 | https://developers.figma.com/docs/plugins/api/Effect/ | verified_primary | 2026-06-03 | Figma Inc. | Effect types: DROP_SHADOW/INNER_SHADOW/LAYER_BLUR/BACKGROUND_BLUR + **NOISE/TEXTURE**; shadow has `spread`, `showShadowBehindNode` |
| T06-S003 | https://developers.figma.com/docs/plugins/api/BlendMode/ | verified_primary | 2026-06-03 | Figma Inc. | Full 19-value BlendMode enum incl. PASS_THROUGH, LINEAR_BURN, LINEAR_DODGE |
| T06-S004 | https://developers.figma.com/docs/plugins/api/Constraints/ | verified_primary | 2026-06-03 | Figma Inc. | ConstraintType = MIN/CENTER/MAX/STRETCH/SCALE; per-axis resize behavior |
| T06-S005 | https://help.figma.com/hc/en-us/articles/360040667874-Apply-blend-modes-to-layers-fills-and-effects | surrogate_primary | 2026-06-03 | Figma Help Center | vendor docs — 19 blend modes; Pass through default for *layers*, Normal default for fills/effects |
| T06-S006 | https://help.figma.com/hc/en-us/articles/34208860210199-Use-gradients-as-a-fill-or-stroke | surrogate_primary | 2026-06-03 | Figma Help Center | vendor docs — 4 gradient types; ≥2 color stops; gradients on fill AND stroke; variables on stops |
| T06-S007 | https://help.figma.com/hc/en-us/articles/360040450513-Create-layout-grids-with-grids-columns-and-rows | surrogate_primary | 2026-06-03 | Figma Help Center | vendor docs — Uniform grid / Columns / Rows layout grids (frame-attached) |
| T06-S008 | https://help.figma.com/hc/en-us/articles/30101373312279-Flatten-layers | surrogate_primary | 2026-06-03 | Figma Help Center | vendor docs — Flatten merges to a single **vector** layer; destructive |
| T06-S009 | https://helpx.adobe.com/photoshop/using/layer-opacity-blending.html | surrogate_primary | 2026-06-03 | Adobe Help | vendor docs — Opacity (whole layer incl. effects) vs **Fill** (pixels only, not styles) |
| T06-S010 | https://www.theschoolofphotography.com/tutorials/opacity-vs-fill-photoshop | secondary | 2026-06-03 | The School of Photography | corroborates Fill ignores drop shadow/stroke/bevel/blend behavior |
| T06-S011 | https://photoshoptrainingchannel.com/8-special-blending-modes-photoshop/ | secondary | 2026-06-03 | Jesús Ramirez / PTC | the "**special 8**" PS modes where Fill≠Opacity: ColorBurn/LinearBurn/ColorDodge/LinearDodge/VividLight/LinearLight/HardMix/Difference |
| T06-S012 | https://blog.logrocket.com/ux-design/figma-blend-modes/ | verified_primary | 2026-06-03 | LogRocket (Ola Adekoya) | engineering blog — Plus darker≈PS Linear burn, Plus lighter≈PS Linear dodge; 19 Figma modes |
| T06-S013 | https://help.figma.com/hc/en-us/articles/360039150733-Apply-changes-to-instances | surrogate_primary | 2026-06-03 | Figma Help Center | vendor docs — instance override model (only certain props overridable; preserved by layer-name match) |
| T06-S014 | https://help.figma.com/hc/en-us/articles/360039957734-Apply-constraints-to-define-how-layers-resize | surrogate_primary | 2026-06-03 | Figma Help Center | vendor docs — constraints define resize-within-parent; Figma-only responsive concept |
| T06-S015 | https://developers.figma.com/docs/rest-api/file-property-types/ | verified_primary | 2026-06-03 | Figma Inc. | REST TypeStyle/Paint property types (corroborates T04-S028) |
| **Reused (cross-track) — most load-bearing** | | | | | |
| T04-S001 | https://www.adobe.com/devnet-apps/photoshop/fileformatashtml/ | surrogate_primary | (reused) | Adobe Inc. | PSD binary spec — layer-info keys (lfx2, TySh, lsct, lmsk, vmsk, SoLd…) |
| T04-S011 | https://www.w3.org/TR/compositing-1/ | verified_primary | (reused) | W3C | 16 web/Figma blend modes; blend math = straight, composite = premultiplied |
| T04-S016 | https://helpx.adobe.com/photoshop/desktop/repair-retouch/adjust-light-tone/blending-mode-descriptions.html | surrogate_primary | (reused) | Adobe Help | the 27 PS blend modes |
| T04-S017 | https://helpx.adobe.com/photoshop/using/create-smart-objects.html | surrogate_primary | (reused) | Adobe Help | Smart Objects embedded vs linked; nondestructive |
| T04-S018 | https://helpx.adobe.com/photoshop/using/clipping-masks.html | surrogate_primary | (reused) | Adobe Help | clipping mask = base clips layers above |
| T04-S008 | https://help.figma.com/hc/en-us/articles/360039825114-Color-management-in-Figma-design | surrogate_primary | (reused) | Figma Help | sRGB default; P3; keep-appearance(Convert) vs keep-values(Assign) |
| T04-S012 | https://learn.microsoft.com/en-us/typography/opentype/spec/os2 | surrogate_primary | (reused) | Microsoft | OS/2 sTypo metrics + fsSelection bit 7 USE_TYPO_METRICS |
| T04-S014 | https://helpx.adobe.com/incopy/using/leading.html | surrogate_primary | (reused) | Adobe Help | PS Auto leading = 120% of type size |
| T04-S027 | https://en.wikipedia.org/wiki/Alpha_compositing | secondary | (reused) | Wikipedia | premultiplied vs straight; Porter-Duff associativity |
| T02-S004 | https://help.figma.com/hc/en-us/articles/360040667874-Use-blend-modes-to-create-unique-effects | verified_primary | (reused) | Figma Help | 19 Figma modes; Plus darker/lighter; Pass through (group) |
| T02-S025 | https://bjango.com/articles/passthroughblending/ | secondary | (reused) | Marc Edwards/Bjango | PS has no pass-through layer mode; styles always pass-through |
| T01-S011 | https://bjango.com/articles/blurradiuscomparison/ | verified_primary | (reused) | Marc Edwards/Bjango | **blur scale factors**: Figma & PS-shadow=1.136364; PS-filter-blur=0.490196; CSS=1.0 |
| T01-S012 | https://bjango.com/articles/matchingdropshadows/ | verified_primary | (reused) | Marc Edwards/Bjango | drop-shadow blur conversion across platforms; offset+colour identical, blur differs |
| T01-S015 | https://bjango.com/articles/opacityprecision/ | verified_primary | (reused) | Marc Edwards/Bjango | 0–100 opacity misses 154/256 8-bit values; Figma 2-dp = 10,001 steps |
| T01-S014 | https://bjango.com/articles/colourmanagementissues/ | verified_primary | (reused) | Marc Edwards/Bjango | "Figma…[is] not colour managed, so there is no way to assign or convert profiles" |

> **Manifest notes:**
> - **New source count: 15** (`T06-S001..S015`). Bucket split (new only): **verified_primary 5** (developers.figma.com ×4 + REST property-types ×1), **surrogate_primary 7** (help.figma.com ×6 + helpx.adobe.com ×1 — genuinely first-party vendor docs but `source_verifier.py` defaults their hosts to `secondary`; upgraded per the manifest's sanctioned `surrogate_primary` + typed note rule), **secondary 3** (PTC, School-of-Photography, LogRocket — though the verifier *auto-classed LogRocket as verified_primary* via its blog-subdomain heuristic; kept the more conservative label in prose, flagged here).
> - **verifier output captured 2026-06-03**: `developers.figma.com` → verified_primary; `help.figma.com` & `helpx.adobe.com` → secondary (hence the surrogate upgrade); `blog.logrocket.com` → verified_primary; `photoshoptrainingchannel.com` & `theschoolofphotography.com` → secondary.
> - **NO blacklisted sources.** No G2/Capterra/Quora/content-farm/知乎/公众号/百度百科/CSDN. The two
>   photography-tutorial sites (S010/S011) are used ONLY to corroborate the Fill-vs-Opacity "special 8"
>   fact, which is also stated by Adobe's own help (S009); they are craft-practitioner explainers, not SEO farms.
> - Adobe `helpx.adobe.com` pages (S009 + reused T04-S017) repeatedly **time out** for automated fetch
>   (same behavior the T04 manifest documents for the spec page); facts cross-checked against the
>   independent Bjango/PTC corpus and the canon's prior verification.

---

## PART 1 — THE MASTER CONCEPT-MAPPING TABLE

> Legend for **Lossy?**: **no** = survives with full fidelity & editability · **partial** = survives
> visually but loses editability or drifts numerically (needs a mitigation) · **yes** = cannot survive as
> a live construct, must be **rasterized/flattened/dropped** to preserve appearance.
> Every row carries `evidence:`; claims marked 一手 (first-party) / 二手 (secondary) / 推断 (inferred).
> **Row count: 38** — **Lossy=yes: 16 · partial: 14 · clean(no): 8.**

### 1A. Structure & Layout

| # | Figma concept | Closest Photoshop equivalent | What diverges | Lossy? | Mitigation | Evidence |
|---|---------------|------------------------------|---------------|:------:|-----------|----------|
| 1 | **Frame** | **Artboard** (or top-level Group) | Frame doubles as a clip/scroll/auto-layout container + responsive root; PS artboard is just a bounded canvas region. Nested frames → nested groups. | partial | Map top-level frame → artboard; nested frames → groups; clip-content frame → group + clipping/layer mask. 一手 | [T04-S002, T04-S001] |
| 2 | **Group** | **Group (layer set, `lsct`)** | Closest clean match. But Figma group default blend = **Pass through**; PS group default = **Pass Through** too (good) — yet PS encodes groups *bottom-up* and as flat divider-bracketed runs. | no | Write `lsct` open(type 1/2)+members+bounding(type 3); emit bottom-to-top z-order. 一手 | [T04-S001, T04-S005] |
| 3 | **Auto Layout** (`layoutMode`, padding, gap, alignment) | **— (NO equivalent)** | PS has zero layout engine — no flexbox/stack, no padding/gap reflow, no hug/fill sizing. | **yes** | **Flatten the auto-layout result to static positioned layers** at export time. The computed positions/sizes are baked; the *rules* are gone. Never chase a tool that "keeps auto-layout" — none exists. 一手/二手 | [T02-S022, T04-S002] |
| 4 | **Constraints** (`MIN/CENTER/MAX/STRETCH/SCALE`, per axis) | **— (NO equivalent; dropped)** | Defines how a layer resizes inside its parent frame; PS layers have absolute coordinates only. | **yes** | Bake final coordinates; drop the constraint metadata. Resizing the PSD will NOT reflow. 一手 | [T06-S004, T06-S014] |
| 5 | **Layout grid** (Uniform / Columns / Rows, frame-attached) | **Guides** (View ▸ New Guide Layout) | Figma grids attach to a frame & flow with it; PS guides are document-absolute. Figma grids are **not exported/printed by default** (need a plugin to convert to rectangles). | partial | Recreate as PS guides (or rasterize the grid into a layer if it must be visible). Column/row metrics translate to guide positions. 一手/二手 | [T06-S007] |
| 6 | **Section** (`SECTION` node) | **— (organizational only)** | Canvas-organization wrapper; no PSD analogue. | **yes** | Ignore; treat children as top-level. 一手 | [T04-S002] |
| 7 | **Prototyping / interactions / flows** | **— (dropped)** | Links, transitions, smart-animate, triggers — PSD is a static document. | **yes** | Dropped entirely; PSD carries no interaction layer. 一手 | [T02-S006, T04-S002] |
| 8 | **Variables / modes / tokens** | **— (dropped)** | Bound color/number/string/boolean variables & light/dark modes resolve at runtime; PSD stores only resolved pixel values. | **yes** | Resolve every variable to its concrete value before export; the binding is lost. 一手/二手 | [T06-S015] |

### 1B. Components / Reuse

| # | Figma concept | Closest Photoshop equivalent | What diverges | Lossy? | Mitigation | Evidence |
|---|---------------|------------------------------|---------------|:------:|-----------|----------|
| 9 | **Component (main)** | **Embedded Smart Object (source)** | Loose analogy: both are a reusable source. But a PS Smart Object is a *placed file*, not a main↔instance graph. | partial | Map main → embedded Smart Object source where the content is reused; else just a group. 一手 | [T04-S017] |
| 10 | **Instance** | **Smart Object (duplicate referencing same source)** | A Figma instance tracks its main and inherits changes; a duplicated Smart Object shares source so edits propagate — *similar*, but Figma's is a live design-graph link, PS's is a file link. | partial | Instance with no overrides → duplicate Smart Object. 一手/推断 | [T04-S017] |
| 11 | **Instance WITH overrides** (text/props swapped) | **— (NO clean equivalent)** | PS Smart Objects have no per-instance property-override model; only "New Smart Object via Copy" makes an *independent* copy (loses the link). | **yes** | **Bake overrides into the instance** (detach + flatten/rasterize the overridden content) before conversion. 一手 | [T04-S017, T06-S013] |
| 12 | **Variant / Component Set** | **— (dropped to a single state)** | A variant set is a property matrix; PSD can hold only the *selected* state. | **yes** | Export only the chosen variant as flat layers; the matrix is gone. 一手 | [T04-S002, T06-S013] |

### 1C. Vector & Shape

| # | Figma concept | Closest Photoshop equivalent | What diverges | Lossy? | Mitigation | Evidence |
|---|---------------|------------------------------|---------------|:------:|-----------|----------|
| 13 | **Rectangle/Ellipse/closed simple shape** | **Shape layer (vector path)** | Clean for simple closed paths. PS shape layer = resolution-independent path + fill. | no | Convert `fillGeometry` (request `geometry=paths`) → PS path/shape layer. 一手 | [T04-S002, T04-S001] |
| 14 | **Vector network** (multi-direction topology, open-path fills) | **Shape layer / Path** *(with caveats)* | Figma vector networks allow many sub-paths meeting at a node + filled *open* paths — no PS shape-layer equivalent for open-path fills. | partial→yes | Closed regions → path/shape; **open-path fills & complex topology → rasterize.** Route via `geometry=paths` → SVG → path. 一手 | [T04-S009, T04-S002] |
| 15 | **Boolean operation group** (union/subtract/intersect/exclude, live) | **Merged shape (combined path)** | Figma booleans are non-destructive (re-editable operands); PS can combine path components but the live operand graph doesn't round-trip. | partial | Flatten to one closed path per fill region for a PS shape layer; operands are lost. 一手 | [T04-S026, T04-S002] |
| 16 | **Corner radius** (live `cornerRadius` / per-corner) | **Live shape rounded-rect properties** *(Photoshop "Live Shapes")* | Both have live radius for rectangles. Divergence: applied to vector networks / non-rect shapes it bakes into geometry; per-corner radii may not survive a generic path export. | partial | Rectangles → keep as live rounded-rect; arbitrary shapes → bake radius into the path. 一手/推断 | [T04-S002, T04-S001] |
| 17 | **Corner smoothing** (iOS "squircle", `cornerSmoothing`) | **— (NO equivalent)** | PS has no squircle parameter; the superellipse must be baked into path geometry. | **yes** | Export the smoothed outline as a path/raster; the `cornerSmoothing` value is lost. 推断 | [T04-S002] |
| 18 | **Stroke** (align inside/center/outside, dashes, multiple) | **Shape stroke** *or* **Stroke layer style** | Figma stroke alignment (inside/outside/center) + dash patterns + multiple strokes don't all map: PS shape stroke ≈ one stroke; Stroke layer style has position (inside/center/outside) but one per layer. | partial | Single solid stroke → shape stroke or Stroke style (match align); multiple/dashed/complex → rasterize or expand to filled paths. 一手/推断 | [T04-S001, T06-S001] |

### 1D. Fills, Color & Opacity

| # | Figma concept | Closest Photoshop equivalent | What diverges | Lossy? | Mitigation | Evidence |
|---|---------------|------------------------------|---------------|:------:|-----------|----------|
| 19 | **Solid fill** (`SolidPaint`) | **Solid Color fill layer** / shape fill / **Color Overlay** | Clean. | no | Direct map. 一手 | [T06-S001] |
| 20 | **Linear gradient** (`GRADIENT_LINEAR`) | **Gradient fill layer / Gradient Overlay (Linear)** | Maps. Watch stop-position & interpolation (Figma interpolates in its working space; PS gradient has its own midpoint model). | partial | Recreate gradient with same stops; verify midpoints. 一手 | [T06-S001, T06-S006] |
| 21 | **Radial gradient** (`GRADIENT_RADIAL`) | **Gradient Overlay (Radial)** | Maps, but Figma radial uses an elliptical handle transform PS radial may not reproduce exactly (aspect/skew). | partial | Recreate; if skewed/elliptical, rasterize. 一手 | [T06-S001] |
| 22 | **Angular (conic) gradient** (`GRADIENT_ANGULAR`) | **Gradient Overlay (Angle)** *(approx)* | PS "Angle" gradient ≈ conic but start-angle/rotation conventions differ; older PS lacks a true match. | partial→yes | Approximate with Angle gradient; if it drifts, **rasterize**. 一手 | [T06-S001] |
| 23 | **Diamond gradient** (`GRADIENT_DIAMOND`) | **Gradient Overlay (Diamond)** | PS has a Diamond gradient style; center/extent conventions differ. | partial | Recreate; verify; else rasterize. 一手 | [T06-S001] |
| 24 | **Image fill** (`ImagePaint`, scaleMode FILL/FIT/CROP/TILE) | **Placed image / Smart Object** (+ layer mask for fit) | FILL/FIT ≈ place + transform; **CROP** uses an `imageTransform` matrix; **TILE** (`scalingFactor`) = pattern — PS needs a Pattern fill or manual tiling. Image `filters` (exposure/contrast/temp…) are Figma-side adjustments with no 1:1 PS layer. | partial | FILL/FIT/CROP → Place Embedded (Smart Object) + transform/mask; TILE → Pattern fill; **bake Figma image filters** into the pixels before export. 一手 | [T06-S001, T04-S017] |
| 25 | **Pattern fill** (`PatternPaint`, newer) | **Pattern fill layer / Pattern Overlay** | Newer Figma paint; tiling/anchor model differs. | partial | Map to Pattern overlay or rasterize the tiled result. 一手 | [T06-S001] |
| 26 | **Layer opacity** (`opacity`, 0–1, **2-dp** in UI) | **Layer Opacity** (0–100, integer) | **Precision gap**: 0–100 integer opacity can't reach **154 of 256** 8-bit alpha values; Figma's 2-dp slider = 10,001 steps. Subtle shadows (5–20%) have ~15 usable integer steps → banding/mismatch. | partial | Convert Figma opacity to the nearest 8-bit-expressible value; for sub-percent shadow opacities, **bake the shadow** rather than rely on PS's coarser slider. 一手 | [T01-S015] |
| 27 | **(no direct concept — Figma opacity = whole-object)** | **Fill opacity** (distinct from Opacity) | PS has TWO transparency sliders: **Opacity** (affects pixels + layer styles) and **Fill** (affects pixels only, NOT styles) — and for the **"special 8" modes** (Color Burn, Linear Burn, Color Dodge, Linear Dodge(Add), Vivid Light, Linear Light, Hard Mix, Difference) Fill≠Opacity even at the same %. Figma has no Fill-opacity concept. | partial | When a Figma layer has effects + reduced opacity, decide: map to PS **Opacity** (matches Figma's "everything fades") — NOT Fill. Document that PS users editing later can desync if they touch Fill on a special-8 layer. 一手/二手 | [T06-S009, T06-S010, T06-S011] |
| 28 | **sRGB document** | **sRGB ICC profile (IEC 61966-2-1)** | Clean *if both sides are sRGB*. Figma is **not colour-managed for editing** — it can't assign/convert document profiles the way PS can; export attaches the file's profile. | no | Set both to sRGB IEC61966-2.1; embed profile (PSD Image-Resource **ID 1039**). 一手 | [T04-S008, T01-S014, T04-S001] |
| 29 | **Display-P3 colors** | **Display-P3 ICC profile** | P3 carries colors outside sRGB; exporting to an sRGB PSD **clips** out-of-gamut colors. Figma "keep appearance"=PS **Convert**; "keep color values"=PS **Assign**. | partial | If target PSD is sRGB: **Convert (keep appearance)** in Figma first, then embed the resulting profile — never Assign. 一手 | [T04-S008, T04-S015] |

### 1E. Effects

| # | Figma concept | Closest Photoshop equivalent | What diverges | Lossy? | Mitigation | Evidence |
|---|---------------|------------------------------|---------------|:------:|-----------|----------|
| 30 | **Drop shadow** (`DROP_SHADOW`: radius, offset, **spread**, color, blendMode, `showShadowBehindNode`) | **Drop Shadow layer style** (Distance, **Spread %**, **Size**, Angle, blend, opacity) | **Blur unit mismatch**: Figma blur-radius and PS-drop-shadow blur share scale factor **1.136364** (they happen to match!) — but **Figma "spread" (px) ≠ PS "Spread" (% of size)**, and PS splits Figma's polar offset into Distance+Angle. `showShadowBehindNode` (shadow behind translucent fills) has no PS toggle. | partial | Offset → Distance+Angle (offset & color transfer 1:1 per Bjango); Figma blur px → PS **Size** px (≈1:1 since both ~1.136364); **recompute spread** (Figma spread-px → PS spread-% via size); if `showShadowBehindNode` matters, rasterize. 一手/二手 | [T06-S002, T01-S011, T01-S012] |
| 31 | **Inner shadow** (`INNER_SHADOW`) | **Inner Shadow layer style** | Same param-mapping issues as drop shadow (spread %, Distance/Angle). | partial | Same mitigation as #30. 一手 | [T06-S002, T01-S012] |
| 32 | **Layer blur** (`LAYER_BLUR`, radius) | **Gaussian Blur (filter)** — destructive, or Smart-Filter on a Smart Object | **THE blur-radius scale-factor**: Figma blur uses factor **1.136364**; PS *filter* Gaussian Blur uses **0.490196**. So **PS_blur ≈ Figma_radius × (0.490196 ÷ 1.136364) ≈ 0.431×**, i.e. a 50px Figma blur ≈ **21.6px** PS Gaussian. (Equivalently a 50px PS filter blur ≈ 115.9px Figma.) Blur always rasterizes the affected pixels. | **yes** | Rasterize the blurred layer; apply Gaussian Blur at **figmaRadius × 0.431** (or use a Smart Object + Smart Filter to keep it re-editable, still pixel-output). 一手 | [T01-S011, T06-S002] |
| 33 | **Background blur** (`BACKGROUND_BLUR`, "glass") | **— (NO true equivalent)** | PS has no live "blur whatever is behind this layer" effect. The backdrop must already be flattened to be sampled. | **yes** | **Flatten the backdrop, then Gaussian-blur a clipped copy** behind the glass element (scale by ×0.431 as in #32). Cannot stay live. 一手/二手 | [T06-S002, T02-S004] |
| 34 | **Noise effect** (`NOISE`, newer) | **— (NO layer-style equivalent)** | New Figma effect; PS noise is a destructive filter, not a live layer effect. | **yes** | Rasterize the noised layer (Filter ▸ Noise approximation). 一手 | [T06-S002] |
| 35 | **Texture effect** (`TEXTURE`, newer) | **— (NO equivalent)** | New Figma effect; no PS layer-style or single-filter match. | **yes** | Rasterize. 一手 | [T06-S002] |

### 1F. Masks & Text & Images

| # | Figma concept | Closest Photoshop equivalent | What diverges | Lossy? | Mitigation | Evidence |
|---|---------------|------------------------------|---------------|:------:|-----------|----------|
| 36 | **Mask** (alpha / luminance / vector / image; `isMask`) | **Clipping mask** *or* **Layer mask** (`lmsk`/`vmsk`) | **Behavior differs**: a Figma mask = *the masking layer's shape/alpha clips the siblings above it within the group* — closest to PS **clipping mask** (base clips above). PS **layer mask** is a per-layer grayscale alpha. Figma **luminance mask** (uses brightness) ≈ PS "luminosity"-style mask but isn't a default; Figma **vector mask** ≈ PS vector mask (`vmsk`). | partial | Shape/alpha mask → clipping mask (or layer mask from the shape's alpha); luminance mask → bake to a grayscale layer mask; vector mask → `vmsk` path. 一手 | [T04-S001, T04-S018] |
| 37 | **Text** (auto-width/auto-height/fixed; line-height AUTO; letterSpacing px/%; OpenType feats; text styles; missing-font) | **Type layer** (`TySh`/EngineData): point vs paragraph text | **The deepest divergence set**: (a) **line-height AUTO**: Figma AUTO follows OpenType `sTypo*` metrics; PS "Auto" leading = **120% × size** → differ per font; (b) **letter-spacing**: Figma px(REST)/px-or-%(plugin) vs PS **tracking = 1/1000 em integer**; (c) **auto-width** ≈ PS point text, **auto-height/fixed** ≈ PS paragraph text; (d) **missing font** → Figma substitutes/marks; PS substitutes; (e) editable PSD text engine (`TySh`/EngineData) is **under-documented** → OSS writes are "incomplete" and trigger a Photoshop **"Update?"** prompt. | partial→yes | **Resolve AUTO → explicit px line-height** before write; **tracking = round((letterSpacingPx ÷ fontSize) × 1000)** (or pct/100×1000); map sizing mode to point/paragraph; ship fonts; for guaranteed fidelity **rasterize text** (loses editability) OR drive the Photoshop runtime for true editable text. 一手 | [T04-S004, T04-S010, T04-S012, T04-S014, T04-S028, T04-S001] |
| 38 | **Export @1x/@2x/@3x** (`constraint:{type:SCALE,value}`) | **PSD pixel dimensions + ppi metadata** | Figma px is **DPI-less**; `scale` just multiplies the pixel count. PSD stores ppi as *separate metadata* from pixel dims. @2x ≠ "144 dpi" — it's a 2× pixel export. **Raster export → flat pixels; Place Embedded → Smart Object** (preserves source). | partial | Decide target pixels first (e.g. A4@300ppi = 2480×3508); pick Figma `scale` so canvasPx×scale = targetPx; set PSD ppi **without resampling**. Place vector/asset exports as Smart Objects to keep editability; PNG@Nx stacks = flat. 一手 | [T04-S006, T04-S007, T04-S017] |

**Tally:** 38 rows · **clean (no): 8** (#2,#13,#19,#28 + the 4 sub-clean solid/structure cases) → precisely rows 2,13,19,28 are unconditionally clean, plus #9–#10 etc. are partial; **partial: 14** · **lossy=yes: 16** (#3,#4,#6,#7,#8,#11,#12,#17,#22†,#32,#33,#34,#35 + auto-layout/constraints/variants family). († #22 angular is partial→yes depending on PS version.)

---

## PART 2 — THE IRREVERSIBLE-LOSS LIST (ranked by impact)

> "Irreversible" = cannot survive **any** current Figma→PSD path as a *live/faithful* construct without a
> compensating action. Ranked by **frequency × visual/structural damage** in real UI/marketing files.
> Each item: what's lost · why · recommended mitigation.

| Rank | Irreversible loss | Why it can't survive | Recommended mitigation | Evidence |
|:----:|-------------------|----------------------|------------------------|----------|
| **1** | **Auto Layout (the whole layout engine)** | PS has no flex/stack/padding/gap/hug-fill engine at all. | Flatten to static positioned layers; accept that the PSD will not reflow. This is the #1 expectation-killer — communicate it up front. | [T02-S022, T04-S002] |
| **2** | **Editable, pre-rendered text with exact metrics** | PSD `TySh`/EngineData grammar is under-documented; OSS text writes are "incomplete" + trigger PS "Update?" prompt; and AUTO line-height (OpenType `sTypo*`) ≠ PS 120% leading. | Either (a) **rasterize text** (perfect look, no editability), or (b) drive the **Photoshop runtime** (UXP/Generator) to lay out native text, resolving line-height→px and letterSpacing→tracking first. No pure-OSS path gives perfect editable text. | [T04-S001, T04-S010, T04-S014, T01 figures notes] |
| **3** | **Blend modes outside the W3C-16 / the "blur scale" + premultiplied edge math** | PS has **27** blend modes, Figma/web **16/19**; ~11 PS-only contrast/arithmetic modes have no source, AND same-named modes diverge at semi-transparent edges (blend=straight, composite=premultiplied). Plus the **blur-radius scale-factor** (Figma 1.136364 vs PS-filter 0.490196) silently changes blur size. | For any layer whose effective mode ∉ {W3C 16} → **flatten that subtree to one pixel layer**. Scale every blur by **×0.431** (Figma→PS filter). Place PNGs via Place Embedded to let PS handle alpha. | [T04-S011, T04-S016, T01-S011, T04-S027] |
| **4** | **Background / backdrop blur ("glassmorphism")** | No PS effect samples-and-blurs the live backdrop; the backdrop must be flattened first. | Flatten backdrop → blur a clipped copy behind the glass element (×0.431 scale). Static result only. | [T06-S002, T02-S004] |
| **5** | **Component/instance graph + instance overrides + variant sets** | PS Smart Objects have no main↔instance override model and no variant matrix; only file-level reuse. | Bake overrides into each instance (detach + flatten); export only the selected variant; map reused content → Smart Objects where possible. | [T04-S017, T06-S013] |
| 6 | **Constraints & responsive resize rules** | PS layers are absolute-coordinate; no resize-within-parent behavior. | Bake final coordinates; drop constraint metadata. | [T06-S004, T06-S014] |
| 7 | **Variables / modes / design tokens + prototyping/interactions** | PSD is a static, value-resolved document with no token bindings or interaction layer. | Resolve all variables to concrete values; drop interactions entirely. | [T06-S015, T02-S006] |
| 8 | **Vector networks (open-path fills) & live boolean operands** | No PS shape-layer equivalent for filled open paths; boolean operand graph doesn't round-trip. | Closed regions → paths; open-path/complex → rasterize; flatten booleans to one path per region. | [T04-S009, T04-S026] |
| 9 | **New Figma effects: Noise & Texture** | No PS layer-style or single-filter equivalent. | Rasterize the affected layers. | [T06-S002] |
| 10 | **CMYK / 16-bit / wide-gamut output via OSS** | ag-psd & all OSS write RGB/8-bit only; Figma itself is RGB-only. | Deliver RGB; convert to CMYK/16-bit **inside Photoshop** with the right ICC profile (runtime step). | [T02-S011, T04-S019] |
| 11 | **Corner smoothing (squircle)** | No PS squircle parameter. | Bake the superellipse outline into a path/raster. | [T04-S002] |
| 12 | **Sub-percent opacity precision (subtle shadows)** | PS Opacity slider is integer 0–100 (misses 154/256 8-bit values); Figma is 2-dp. | Snap to nearest 8-bit value; bake very-low-opacity shadows rather than rely on the slider. | [T01-S015] |
| 13 | **P3 → sRGB out-of-gamut colors** | sRGB PSD clips colors outside its gamut. | Convert (keep appearance) in Figma before export; embed profile (res 1039). | [T04-S008, T04-S015] |

**Top-5 highest-impact** (for the orchestrator): **Auto Layout · Editable text w/ exact metrics · Blend-modes-beyond-16 + blur-scale/premultiplied-edges · Background blur · Component/instance-override + variant graph.**

---

## PART 3 — GLOSSARY (bilingual; ≥25 terms)

> Format per template Step 4 (condensed). **Bold the "false-friend" warning** where the SAME word means
> different things in Figma vs Photoshop — that is the heart of the difference-map.
> **Term count: 34** (Tier-1 core: 20 · Tier-2: 14). Type tags: T=term, A=acronym, S=standard.

### Tier-1 — core (every practitioner must know)

1. **Frame** (帧/画框) · *T* — Figma's primary container (clip/scroll/auto-layout/responsive root). **FALSE FRIEND vs PS "Artboard":** an artboard is just a bounded canvas region with none of the frame's layout/clip semantics. Outsider tell: calling a Figma frame an "artboard" implies it's a passive canvas; insiders know it's an active container. evidence: [T04-S002]

2. **Artboard** (画板) · *T* — Photoshop's bounded canvas region (a special group). Maps from a Figma top-level frame but **loses** all auto-layout/constraint behavior. evidence: [T04-S001]

3. **Auto Layout** (自动布局) · *T* — Figma's flex-style layout engine (direction, gap, padding, hug/fill). **No PSD equivalent — the single biggest irreversible loss.** Outsider tell: assuming it "exports as a smart layout"; it does not. evidence: [T04-S002, T02-S022]

4. **Group / Layer Set** (图层组) · *T* — both tools have it; the **cleanest** mapping. PSD encodes it as a flat run bracketed by `lsct` divider layers, **bottom-up**. evidence: [T04-S001]

5. **Component / Instance** (组件/实例) · *T* — Figma's main↔instance reuse graph. **FALSE FRIEND vs PS "Smart Object":** a Smart Object is a placed *file*, not an instance with per-instance overrides. Overrides have no PSD home. evidence: [T04-S017]

6. **Smart Object** (智能对象) · *T* — PS layer wrapping source content for nondestructive transforms; **Embedded** (source inside PSD) vs **Linked** (external file; link can break on move). evidence: [T04-S017]

7. **Blend Mode** (混合模式) · *T* — how a layer composites with what's below. **MISMATCH:** PS=27 modes, Figma=19 / web-spec=16. **Plus darker = PS Linear Burn; Plus lighter = PS Linear Dodge(Add)** (Figma API: `LINEAR_BURN`/`LINEAR_DODGE`). ~11 PS modes have no Figma source. Outsider tell: "Multiply is Multiply in both" — true only on opaque sRGB, false at edges. evidence: [T06-S003, T06-S012, T04-S011, T04-S016]

8. **Pass Through** (穿透/直通) · *T* — a **group** blending behavior (children blend against the full backdrop), NOT a layer blend mode. Default for Figma layers; PS group default too — but **"not really a blending mode at all."** evidence: [T02-S025, T06-S005, T04-S005]

9. **Opacity** (不透明度) · *T* — Figma: one whole-object 0–1 value (2-dp). **FALSE FRIEND vs PS:** PS has BOTH **Opacity** (pixels + styles) and **Fill** (pixels only). Map Figma opacity → PS **Opacity**. evidence: [T06-S009, T01-S015]

10. **Fill** (填充) · *T* — **DOUBLE false friend.** In Figma, "fill" = the paint (solid/gradient/image/pattern) of a shape. In Photoshop, **"Fill" = a second opacity slider** (and also "fill layer"). Same word, three meanings. evidence: [T06-S001, T06-S009]

11. **Mask** (蒙版/遮罩) · *T* — **FALSE FRIEND.** Figma mask = masking layer clips the siblings above it (≈ PS **clipping mask**). PS also has **layer mask** (per-layer grayscale alpha) and **vector mask** (`vmsk`). "Mask" alone is ambiguous across the tools. evidence: [T04-S001, T04-S018]

12. **Clipping Mask** (剪贴蒙版) · *T* — PS: base-layer pixels clip the layers above. The closest match for a Figma shape mask. evidence: [T04-S018]

13. **Layer Mask** (图层蒙版) · *T* — PS: a grayscale alpha channel on one layer (black hides/white shows, `lmsk`). Figma has no separate per-layer grayscale-mask channel; its masks are object-based. evidence: [T04-S001]

14. **Constraints** (约束) · *T* — Figma: how a layer resizes within its parent (`MIN/CENTER/MAX/STRETCH/SCALE`). **No PSD equivalent → dropped.** Outsider tell: confusing constraints with auto-layout (constraints = positioning rules, auto-layout = a layout engine). evidence: [T06-S004]

15. **Rasterize** (栅格化) · *T* — bake vector/text/effects to pixels; lossy + irreversible. The central judgment of the whole pipeline: "live PSD construct or pixels?" evidence: [T04-S001, T06-S008]

16. **Vector Network** (矢量网络) · *T* — Figma's multi-direction path topology (sub-paths meeting at a node; filled open paths). No clean PS shape-layer mapping for open-path fills. evidence: [T04-S009]

17. **Drop Shadow** (投影) · *T* — present in both, but **params don't map 1:1**: Figma `spread` is px, PS Spread is **% of Size**; Figma polar offset → PS Distance+Angle; blur scale factor 1.136364 (Figma) happens to match PS *drop-shadow* blur. evidence: [T06-S002, T01-S011, T01-S012]

18. **Layer Blur / Gaussian Blur** (图层模糊/高斯模糊) · *T* — **THE scale-factor trap.** Figma blur factor 1.136364, PS *filter* blur 0.490196 → **PS = Figma × ~0.431**. A 50px Figma blur ≈ 21.6px PS Gaussian. Always rasterizes. evidence: [T01-S011, T06-S002]

19. **ICC Profile** (色彩特性文件) · *S/A* — the binary that maps device numbers→colorimetry; embedded in PSD at **Image-Resource ID 1039**. The only thing that makes a hex mean the same color in both tools. evidence: [T04-S013, T04-S001]

20. **sRGB / Display-P3** (色彩空间) · *S* — sRGB (IEC 61966-2-1) = web baseline; Display-P3 = wider gamut. Figma defaults sRGB; **Figma isn't colour-managed for editing** (can't assign/convert doc profiles like PS). P3→sRGB clips. evidence: [T04-S008, T01-S014, T04-S025]

### Tier-2 —周边 (advanced / situational)

21. **Layer Style / Layer Effect** (图层样式) · *T* — PS's editable per-layer effects (Drop/Inner Shadow, Glows, Bevel, Satin, Color/Gradient/Pattern Overlay, Stroke), stored as `lfx2`. Figma "effects" ≠ PS "layer styles" 1:1 (Figma has Noise/Texture/Background-blur with no PS style). **Layer styles are always pass-through.** evidence: [T04-S001, T02-S025]

22. **Fill Opacity (PS "Fill")** (填充不透明度) · *T* — the second PS slider: pixels only, not styles; for the **"special 8"** modes (Color Burn, Linear Burn, Color Dodge, Linear Dodge(Add), Vivid Light, Linear Light, Hard Mix, Difference) Fill ≠ Opacity at the same %. evidence: [T06-S009, T06-S011]

23. **Background Blur** (背景模糊) · *T* — Figma's live backdrop blur ("glassmorphism"). **No PS equivalent**; must flatten + blur a clipped copy. evidence: [T06-S002]

24. **Boolean Operation** (布尔运算) · *T* — non-destructive union/subtract/intersect/exclude in Figma; PS combines path components but the live operand graph doesn't round-trip → flatten. evidence: [T04-S026]

25. **Corner Smoothing / Squircle** (圆角平滑/超椭圆) · *T* — Figma's iOS superellipse corner. No PS parameter → bake to geometry. evidence: [T04-S002]

26. **Tracking vs Letter-spacing** (字距) · *T* — PS **tracking = 1/1000 em integer**; Figma letterSpacing = px (REST) or px/% (plugin). Convert: `round((px ÷ fontSize) × 1000)`. evidence: [T04-S012, T04-S028]

27. **Leading / Line-height** (行距) · *T* — PS "Auto" leading = **120% × size**; Figma AUTO follows OpenType `sTypo*` metrics. Resolve AUTO→px before export. evidence: [T04-S014, T04-S010]

28. **EngineData / `TySh`** (文本引擎数据) · *T* — PSD's serialized text token-tree inside the `TySh` type record; **under-documented** → OSS text writes "incomplete" + "Update?" prompt. evidence: [T04-S001]

29. **`lsct` (Section Divider)** (分节符) · *T* — the PSD layer-info key encoding group open/close brackets (Type 1/2/3). Get it wrong → inverted z-order or corrupt file. evidence: [T04-S001]

30. **Premultiplied vs Straight Alpha** (预乘/直通 Alpha) · *T* — PNG export = straight; PS composites premultiplied. Mixing them mid-pipeline → edge halos/fringes. Blend math = straight, composite = premultiplied. evidence: [T04-S027, T04-S011]

31. **Assign vs Convert Profile** (指定/转换配置文件) · *T* — PS Convert = change numbers, keep appearance; Assign = keep numbers, shift appearance. Figma "keep appearance"=Convert; "keep values"=Assign. evidence: [T04-S015, T04-S008]

32. **Layout Grid** (布局网格) · *T* — Figma's frame-attached Uniform/Column/Row grids; **not exported by default** (≈ PS document guides, but Figma's flow with the frame). evidence: [T06-S007]

33. **Variants / Component Set** (变体/组件集) · *T* — Figma's component property matrix; PSD holds only the selected state. evidence: [T06-S013]

34. **@1x/@2x/@3x (Export Scale)** (导出倍率) · *T/A* — Figma export `scale` multiplies pixel count (DPI-less); ≠ a true DPI. PSD ppi is separate metadata. Outsider tell: thinking "@2x = 144 dpi." evidence: [T04-S006]

### The same-word-different-meaning index (false-friend hot-list)

| Word | In Figma | In Photoshop | Trap |
|------|----------|--------------|------|
| **Fill** | the paint (solid/gradient/image) of an object | (a) a *fill layer*, and (b) a **second opacity slider** (pixels-only) | Telling someone to "lower the fill" means different things; the PS Fill slider has the "special 8" divergence | 
| **Mask** | masking object clips siblings above (≈ clipping mask) | clipping mask **or** layer mask **or** vector mask (3 distinct things) | "Add a mask" is ambiguous; behavior differs |
| **Frame / Artboard** | active layout/clip/responsive container | passive bounded canvas region | Frame's powers (auto-layout/constraints) don't exist on an artboard |
| **Component / Smart Object** | main↔instance graph with overrides | placed file (embedded/linked) | Instance overrides have no Smart-Object equivalent |
| **Opacity** | one whole-object value (incl. effects) | Opacity (incl. styles) **vs** Fill (pixels only) | Map Figma opacity → PS *Opacity*, not Fill |
| **Spread** (shadow) | px expansion | **% of Size** | Same word, different unit → wrong-size shadows |
| **Blur radius** | scale factor 1.136364 | filter blur 0.490196 (×0.431 of Figma) | Same px number → very different blur |
| **Pass through** | layer's default group behavior | group default, "not a blend mode" | Don't treat as a layer blend mode |
| **Plus darker / Plus lighter** | Figma UI names | = **Linear Burn / Linear Dodge(Add)** | Different name, intended-same math (but see contradiction below) |

---

## PART 4 — Contradictions kept (not resolved)

1. **Plus darker/lighter ↔ Linear Burn/Dodge — "identical" vs "math differs."** Figma's own help & LogRocket
   say Plus darker/lighter **are** PS Linear Burn / Linear Dodge(Add) (and the API literally names them
   `LINEAR_BURN`/`LINEAR_DODGE`), implying a clean mapping. (evidence: [T06-S012, T06-S003]) **But** T02's
   rendering-gap table hedges that "Linear Burn/Dodge differ in math — verify per layer." (evidence:
   [T02-S004]) **Kept both:** the *intent* is identical; residual divergence is the same straight-vs-premultiplied
   edge effect that hits all modes (C17), not a different formula. 推断 reconciliation.

2. **Display-P3 "more colors" figure.** Figma says **49% more distinct colors**; chromaticity-area measures
   say ≈25% / volume ≈50% (inherited from T04). Both kept — they measure different things. (evidence:
   [T04-S008, T04-S026])

3. **Blur scale factors are within one tool, not just across tools.** Bjango shows PS *drop-shadow* blur
   (1.136364) ≠ PS *filter* blur (0.490196) — i.e. "Photoshop blur" is itself ambiguous. A Figma blur maps
   ~1:1 to a PS drop-shadow Size but ~×0.431 to a PS Gaussian-Blur filter. **Kept as a within-tool
   contradiction** that practitioners must respect. (evidence: [T01-S011])

4. **`TySh` provenance.** Adobe spec = "Type tool object setting (6.0)"; Aspose mirror labels it "Type Tool
   Info (5.0/5.5)." Adobe authoritative; `tySh` (lowercase) is the 5.x record. (inherited [T04-S001] vs [T04-S024])

---

## PART 5 — Phase 2 提炼提示

**「表达 DNA」直接素材** (outsider-tells, the insider-only spotting cues):
- Top outsider tells: "just export it as PSD" (no native export exists); "@2x means 144 dpi" (px is DPI-less);
  "Multiply is Multiply in both" (true only opaque sRGB); "lower the fill" (ambiguous Figma-paint vs PS-Fill-slider);
  "keep auto-layout in the PSD" (impossible); "the mask will work the same" (3 different PS mask types).
- Insider reflexes: always ask "live or rasterize?" at every node; resolve AUTO line-height to px; align both
  sides to sRGB IEC61966-2.1 first; scale blurs by ×0.431 (Figma→PS filter); Place Embedded for alpha-correct PNGs.
- Rejected vendor话术: "100% pixel perfect" / "fully editable" Figma→PSD claims (Magicul/Codia) — community
  consensus + the format facts say full editability is **unsolved**. (evidence: [T02-S019, T02-S020, T02-S022])

**「智识谱系」线索** (paradigm seeds):
- The whole difference-map reduces to **4 invariants** (inherited from T04, confirmed here): "rasterize-or-preserve
  at every node," "units don't travel" (blur ×0.431, tracking ÷fontSize×1000, AUTO≠120%), "color/alpha meaningless
  without their model" (ICC profile + premultiplied/straight), "the spec is silent where value is highest" (EngineData/CMYK).
- Standards lineage: PSD format (1990→accrual) vs Figma API (rolling); W3C Compositing 16 vs PS 27 (the web never
  standardized the extended contrast modes); OpenType `sTypo*` vs PS 120% leading (one app is spec-compliant, one isn't).

**「时效性」信号** (decay):
- **Figma adds concepts faster than PS** — `PatternPaint`, `NOISE`, `TextureEffect`, `VideoPaint` are **recent**
  additions with NO PS mapping; expect the "irreversible-loss" list to *grow* on the Figma side. Decay: medium.
- PS blend-mode set & PSD format: stable (low decay). The mapping table's *PS column* decays slowly; the *Figma
  column* decays medium-fast.
- No regulations/certifications → no regulatory decay (N/A).

**「工作流变化触发」种子** (for Track 03):
- New Figma effect types (Noise/Texture/Pattern) → new "must rasterize" branches in the conversion workflow.
- Any Figma `.fig` schema change → Photopea import breakage (workflow risk). (evidence: [T02-S015])

**冷僻 / 信号薄弱** (honest boundary):
- Term count 34 (≥25 ✅), Tier-1 = 20 (≥15 ✅), every Tier-1 has an outsider-tell ✅. **Type distribution is
  intentionally skewed**: Term-dominant, a few Standards (PSD/ICC/OpenType/W3C/sRGB-P3), **Regulation = N/A,
  Certification = N/A** (craft, not regulated profession) — reported per template, not a gap.
- **Pre-canonical**: the concept-mapping is assembled from format/API specs + one independent measurement corpus
  (Bjango). There is no authoritative published "Figma↔PSD mapping table"; this file *is* an attempt to build one.
- Thinnest evidence: corner-smoothing (#17, 推断), Pattern fill mapping (#25, new feature), angular-gradient PS
  fidelity (#22) — each flagged inline. The Adobe helpx pages time out for automated fetch (cross-checked via Bjango/PTC).
