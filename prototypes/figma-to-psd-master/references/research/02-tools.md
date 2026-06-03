# Track 02 — Tools Research: Figma → PSD High-Fidelity Conversion

> Research track for the figma-to-psd-master skill distillation.
> Goal: align Figma↔Photoshop differences so an exported PSD looks identical to the Figma source.
> last_checked: 2026-06-03 (OPUS verify/deepen pass over prior sonnet draft)

---

## Source Manifest

| source_id | url | bucket | last_checked | author/host | one-line note |
|-----------|-----|--------|--------------|-------------|---------------|
| T02-S001 | https://help.figma.com/hc/en-us/articles/13402894554519-Export-formats-and-settings | verified_primary | 2026-06-03 | Figma Help Center | Export = PNG/JPG/SVG/PDF only; no PSD |
| T02-S002 | https://developers.figma.com/docs/rest-api/file-endpoints/ | verified_primary | 2026-06-03 | Figma Developer Docs | GET images: jpg/png/svg/pdf, scale 0.01-4, 32MP cap |
| T02-S003 | https://developers.figma.com/docs/plugins/api/properties/nodes-exportasync/ | verified_primary | 2026-06-03 | Figma Developer Docs | exportAsync: PNG/SVG_STRING/JSON_REST_V1 only |
| T02-S004 | https://help.figma.com/hc/en-us/articles/360040667874-Use-blend-modes-to-create-unique-effects | verified_primary | 2026-06-03 | Figma Help Center | 19 blend modes; Pass through (group); Plus darker/lighter |
| T02-S005 | https://help.figma.com/hc/en-us/articles/360039825114-Manage-color-profiles-in-design-files | verified_primary | 2026-06-03 | Figma Help Center | sRGB default / Display P3; export uses file profile |
| T02-S006 | https://help.figma.com/hc/en-us/articles/32132100833559-Guide-to-the-Figma-MCP-server | verified_primary | 2026-06-03 | Figma Help Center | MCP: design-to-code; no PSD direction |
| T02-S007 | https://developer.adobe.com/photoshop/uxp/2022/ps_reference/ | verified_primary | 2026-06-03 | Adobe Developer | UXP PS DOM: createLayer, batchPlay, executeAsModal |
| T02-S008 | https://mapsoft.com/posts/extendscript.html | secondary | 2026-06-03 | Mapsoft | ExtendScript/ESTK deprecated 2020; UXP successor |
| T02-S009 | https://github.com/Agamnentzar/ag-psd | verified_primary | 2026-06-03 | Agamnentzar (GitHub) | JS read/write PSD; 671★/87 forks/53 issues |
| T02-S010 | https://github.com/Agamnentzar/ag-psd/blob/master/CHANGELOG.md | verified_primary | 2026-06-03 | Agamnentzar (GitHub) | Latest v30.0.1/30.1.1; 16-bit fix is READ-side |
| T02-S011 | https://github.com/Agamnentzar/ag-psd/blob/master/README.md | verified_primary | 2026-06-03 | Agamnentzar (GitHub) | Verbatim write limits: RGB-only, no 16-bit, no redraw |
| T02-S012 | https://www.photopea.com/tuts/convert-figma-to-psd/ | verified_primary | 2026-06-03 | Photopea | Official FIG→PSD tut; ONLY font caveat stated here |
| T02-S013 | https://blog.photopea.com/photopea-4-6-open-figma-files.html | verified_primary | 2026-06-03 | Photopea Blog | v4.6 (2020-01-27) added .FIG open + save PSD |
| T02-S014 | https://github.com/photopea/photopea/issues/4455 | reference | 2026-06-03 | Photopea (GitHub) | Confirms Photopea rasterizes vectors (closed, no fix) |
| T02-S015 | https://github.com/photopea/photopea/issues/4990 | reference | 2026-06-03 | Photopea (GitHub) | Figma changed .fig → Photopea import broke |
| T02-S016 | https://madebyevan.com/figma/fig-file-parser/ | verified_primary | 2026-06-03 | Evan Wallace (Figma co-founder) | .fig = unstable internal Kiwi binary; may break |
| T02-S017 | https://www.figma.com/community/plugin/1610258845845995569/psd-exporter-importer | secondary | 2026-06-03 | Figma Community (3rd-party) | "PSD Exporter & Importer": offline; font mapping |
| T02-S018 | https://www.figma.com/community/plugin/1501337808956041642/psd-export | secondary | 2026-06-03 | Figma Community (3rd-party) | "PSD Export": motion pipeline (AE/Premiere) |
| T02-S019 | https://codia.ai/psd-to-figma | secondary | 2026-06-03 | Codia AI (vendor) | Bidirectional; "pixel-perfect" = marketing-claim |
| T02-S020 | https://magicul.io/converter/figma-to-psd | secondary | 2026-06-03 | Magicul (vendor) | $94+; "100% pixel perfect" = marketing-claim |
| T02-S021 | https://magicul.io/blog/magicul-io-vs-photopea-which-is-the-best-figma-to-psd-converter | secondary | 2026-06-03 | Magicul Blog (vendor) | Self-comparison; biased; Photopea=raster admission |
| T02-S022 | https://forum.figma.com/ask-the-community-7/how-do-i-convert-a-figma-file-to-psd-layered-file-1438 | secondary | 2026-06-03 | Figma Forum (community) | Consensus: no tool keeps layers 100%; PDF→AI route |
| T02-S023 | https://helpx.adobe.com/photoshop/desktop/create-manage-layers/smart-objects/create-embedded-smart-objects.html | verified_primary | 2026-06-03 | Adobe Help | Place Embedded → 1 Smart Object; edit in Illustrator |
| T02-S024 | https://news.adobe.com/news/news-details/2023/adobe-and-figma-mutually-agree-to-terminate-merger-agreement | verified_primary | 2026-06-03 | Adobe News | Merger ended 2023-12-18; EC+UK CMA; no $ amount stated |
| T02-S025 | https://bjango.com/articles/passthroughblending/ | secondary | 2026-06-03 | Bjango (Marc Edwards) | PS has no pass-through mode; styles always pass-through |
| T02-S026 | https://github.com/richardwhitner/Figma-Export-For-Photoshop | verified_primary | 2026-06-03 | richardwhitner (GitHub) | OSS: Figma→PNG layers → PS JSX assembles PSD (WIP) |
| T02-S027 | https://avocode.com/ | secondary | 2026-06-03 | Avocode / Ceros | Avocode sunset 2023-10-01; team→Ceros |
| T02-S028 | https://developers.figma.com/docs/plugins/api/ExportSettings/ | verified_primary | 2026-06-03 | Figma Developer Docs | svg_outline_text defaults TRUE (text→paths) |
| T02-S029 | https://github.com/webtoon/psd | verified_primary | 2026-06-03 | Webtoon (GitHub) | @webtoon/psd: READ-ONLY parser; v0.4.0 (2023) |

---

## 総覧 (Overview by Tier)

**Honest framing up front (一手 consensus, evidence: [T02-S012, T02-S022, T02-S025]):** There is NO native Figma PSD export and NO tool that produces a fully-editable layered PSD with Figma parity. Every route trades among (a) text editability, (b) vector fidelity, (c) effect/blend accuracy, (d) layer structure. The choice is therefore *which loss you can tolerate*, not *which tool is best*.

### 必備層 (2 tools — anchor the two viable axes)

| 工具 | 一句话 | Decay | Sources |
|------|--------|-------|---------|
| Photopea | Free web app, opens `.fig` directly, saves layered PSD; rasterizes vectors | medium | T02-S012, T02-S013, T02-S014, T02-S022 |
| ag-psd | JS lib that *writes* PSD bytes; backbone of every code-based exporter; hard RGB/8-bit limits | low | T02-S009, T02-S010, T02-S011 |

### 場景特化層 (7 tools/routes)

| 工具 | 一句话 | Decay | Sources |
|------|--------|-------|---------|
| Plugin: PSD Exporter & Importer | In-Figma export; offline; font mapping; "works best" per community | medium | T02-S017, T02-S022 |
| Plugin: PSD Export | In-Figma export aimed at motion (After Effects/Premiere/Resolve) | medium | T02-S018 |
| SVG → PS Place Embedded | Vector-preserving bridge: 1 SVG = 1 Smart Object (edit via Illustrator) | low | T02-S023, T02-S028 |
| PDF → (Illustrator) → PS | Community offline route; text outlined; ungroup/unclip in AI then place | low | T02-S001, T02-S022 |
| PNG @Nx → PS layers | Pixel-faithful flat layers; everything rasterized (e.g. richardwhitner OSS) | low | T02-S002, T02-S026 |
| Figma REST API + ag-psd (Node) | Programmatic bulk; RGB/8-bit only; you must supply every pixel bitmap | low | T02-S002, T02-S011 |
| Photoshop UXP plugin | In-PS assembler for the above pipelines; createLayer/batchPlay | low | T02-S007, T02-S008 |

### 新興 / 実験層 (3 — `stability: experimental`)

| 工具 | 一句话 | Decay | Sources |
|------|--------|-------|---------|
| Codia AI Psd2Figma | AI bidirectional; Figma→PSD "editable/pixel-perfect" = vendor claim, unverified | high | T02-S019 |
| Magicul SaaS | Paid cloud ($94+); "100% pixel perfect" = vendor claim, unverified | high | T02-S020, T02-S021 |
| Figma MCP Server | AI design-to-code bridge; NO PSD direction (irrelevant to this skill) | high | T02-S006 |

---

## TOOL CARDS

### 1. Figma Native Export + REST API + Plugin API (reference baseline — confirmed non-options for PSD)

- **One-liner**: Figma's three export surfaces (UI panel, REST `GET images`, plugin `exportAsync`) all top out at raster/vector formats; PSD is absent from every one.
- **Tier**: 必備 (as the confirmed *floor* that forces third-party tooling)
- **Maintainer / Owner**: Figma Inc. — https://www.figma.com
- **License**: proprietary SaaS
- **Maturity**: stable; docs current 2025-2026. evidence: [T02-S001]
- **Exact format matrices** (一手, all verified this pass):
  - UI export panel: **PNG, JPG, SVG, PDF**. SVG and PDF only at **1x**; PNG/JPG take multiplier/width/height. SVG has an **"Outline text"** toggle — when on, "Text will not be editable after export." evidence: [T02-S001]
  - REST `GET /v1/images/:key`: format enum **jpg/png/svg/pdf**; `scale` **0.01–4**; images **>32 MP are scaled down**. Undocumented `svg_outline_text` defaults **true** (text→vector paths); `=false` keeps selectable `<text>` but "visual accuracy is not guaranteed" across browsers/OS. evidence: [T02-S002, T02-S028]
  - Plugin `node.exportAsync()`: **PNG, SVG_STRING, JSON_REST_V1** only — defaults to PNG @1x. (Correction vs prior draft: **PDF is NOT a plugin export format**; it exists only in the UI panel and REST API.) evidence: [T02-S003]
- **PSD support**: None on any surface. evidence: [T02-S001, T02-S002, T02-S003]
- **不适合**: Anything needing layered PSD — must go through Photopea, an exporter plugin, or a bridge route.
- **Decay risk**: low — these formats are the stable Figma export floor.
- **信頼度**: high (一手 官方 docs, all three surfaces fetched this pass)

---

### 2. Photopea

- **One-liner**: Free browser Photoshop-clone that opens `.fig` directly and saves a real *layered* `.psd` — the zero-cost bridge, but it is a raster editor and **rasterizes vectors**.
- **Tier**: 必備
- **Maintainer / Owner**: Ivan Kuckir — https://www.photopea.com (single developer)
- **License**: freemium (free w/ ads; paid ad-free)
- **Maturity**: `.fig` open shipped in **Photopea 4.6, 2020-01-27** (corrected exact date). Actively updated. evidence: [T02-S013]
- **What it genuinely produces**: a layered PSD (File → Save as PSD); "the layer structure is preserved." Non-PSD inputs are converted to PSD on save. evidence: [T02-S012, T02-S013]
- **What it loses / breaks** (re-sourced — see correction note):
  - **Fonts**: custom/brand fonts must be loaded first via File → Open (TTF/OTF), else substituted. *This is the ONLY caveat on Photopea's own tutorial page.* evidence: [T02-S012]
  - **Vectors → raster**: Photopea "is not a vector software"; vector shapes/SVG become pixel layers — confirmed by its own bug tracker (issue #4455, closed without a fix). This is the single biggest fidelity hit for UI/print. evidence: [T02-S014]
  - **Vector shape splitting** + **drop-shadow opacity reset to 100%**: widely reported quirks, but **NOT on Photopea's official tutorial** (prior draft mis-cited T02-S012). Treat as 推断/community-reported pending a first-party page. evidence: [推断, community write-ups]
  - **Components/instances**: not preserved as reusable structures (flatten to layers). evidence: [推断 from T02-S021 vendor claim + T02-S022]
  - **`.fig` parser lag**: `.fig` is Figma's *internal* format; when Figma changes it, Photopea import breaks (issue #4990 — Figma updated `.fig`, import stopped). evidence: [T02-S015, T02-S016]
- **不适合**: vector-clean/print output, component-heavy files, security-sensitive work (web-processed), or any moment soon after Figma ships a `.fig` schema change.
- **代替方案**: in-Figma exporter plugin (keeps text as text better); SVG/PDF bridge for vectors.
- **Decay risk**: medium — single-maintainer + structural dependency on an undocumented, changeable `.fig` format.
- **信頼度**: high (一手 vendor docs + 一手 project bug tracker)

---

### 3. ag-psd (JavaScript library)

- **One-liner**: The de-facto JS library for *writing* PSD bytes — the engine under most code-based exporters — but with hard limits that cap fidelity for any pipeline built on it.
- **Tier**: 必備 (infrastructure)
- **Maintainer / Owner**: Agamnentzar — https://github.com/Agamnentzar/ag-psd
- **License**: **MIT** (confirmed in package.json) evidence: [T02-S009]
- **Maturity**: **671★ / 87 forks / 53 open issues / 237 commits** (2026-06-03); latest **v30.0.1** in CHANGELOG (npm shows **30.1.1**). v30.0.1 = "Fixed handling files with **16-bit** color format" — this is on the **READ** path, not write. evidence: [T02-S009, T02-S010]
- **HARD limits (verbatim from README, the crux for fidelity)**:
  - "Does not support **writing any color modes other than RGB**" → **no CMYK / Indexed / Duotone / LAB / Multichannel** output. evidence: [T02-S011]
  - "Does not support **16 bits per channel**." → 8-bit only. evidence: [T02-S011]
  - "This library does not handle **redrawing layer and composite image data by itself** … does NOT generate new layer canvas based on layer settings, so … you also need to update `layer.canvas` or `layer.imageData`." This applies to **text, vector, and smart-object** layers. evidence: [T02-S011]
  - **Consequence (the key gotcha):** if you write a text layer without supplying a matching rendered bitmap, Photoshop shows a **warning prompt** ("update text layers?") on open, and the composite/thumbnail are invalid until regenerated. So ag-psd text layers are *technically editable* but require you to pre-render the exact pixels yourself — there is no free "editable text" lunch. evidence: [T02-S011]
  - **Smart objects**: writeable as metadata but you must still provide the pre-generated bitmap; no auto-render. evidence: [T02-S011]
- **典型使用場景**: backbone of in-Figma exporter plugins and Node batch pipelines that already have rendered PNGs per layer.
- **不适合**: CMYK or 16-bit print PSDs; any non-JS stack; any expectation that it "rasterizes layers for you."
- **Decay risk**: low — MIT, widely depended on, steady releases.
- **信頼度**: high (一手 repo + verbatim README)

---

### 4. Figma Plugin: PSD Exporter & Importer

- **One-liner**: In-Figma plugin (offline) that converts frames/layers to PSD with font mapping; community calls it the best of the breed, but it is built on the same ag-psd-class ceiling.
- **Tier**: 場景特化
- **Maintainer / Owner**: third-party (Figma Community ID 1610258845845995569)
- **License**: proprietary plugin
- **Maturity**: actively developed; runs fully offline (no cloud upload). evidence: [T02-S017]
- **What is preserved**: layers, groups, basic vector shapes, **font mapping** so custom fonts export reliably; "complex layer effects … being refined." One forum user: "Out of all the plugins for exporting to PSD, this one works the best." evidence: [T02-S017, T02-S022]
- **Reality on text/effects**: text fidelity across plugins remains "a work in progress"; complex effects may not transfer. evidence: [T02-S022]
- **典型使用場景**: in-Figma one-click PSD with best-effort editable text; privacy-sensitive client work (offline).
- **不适合**: auto-layout-heavy or effect-heavy frames expecting full fidelity.
- **Decay risk**: medium — third-party plugin lifecycle risk (abandonment).
- **信頼度**: medium (一手 Community listing + 二手 community endorsement; no independent benchmark)

---

### 5. Figma Plugin: PSD Export (motion-pipeline focus)

- **One-liner**: In-Figma exporter producing layered PSD aimed at **After Effects / Premiere / DaVinci Resolve** with text, fonts, blend modes.
- **Tier**: 場景特化
- **Maintainer / Owner**: third-party (Figma Community ID 1501337808956041642). (Prior draft's "by Creattive" attribution could NOT be verified — dropped.)
- **License**: proprietary plugin
- **Maturity**: listed/available on Figma Community; "fast and accurate support for text, fonts, and blend modes." evidence: [T02-S018]
- **典型使用場景**: motion designers handing UI to AE; video/multimedia handoff (layered PSD is AE's import sweet spot).
- **不适合**: print/CMYK; web handoff where editable vector matters.
- **Decay risk**: medium.
- **信頼度**: medium (一手 plugin page; not independently tested)

---

### 6. SVG → Photoshop via Place Embedded (vector-preserving bridge)

- **One-liner**: Export SVG from Figma, then **File → Place Embedded** in PS → each SVG becomes **one Smart Object** (vector, resolution-independent; edit by reopening in Illustrator).
- **Tier**: 場景特化
- **Maintainer / Owner**: Adobe (PS) + Figma (SVG export)
- **License**: CC subscription
- **Maturity**: stable Adobe feature. evidence: [T02-S023]
- **What is preserved**: vector paths as an editable Smart Object; double-click thumbnail edits contents in Illustrator. evidence: [T02-S023]
- **Known limitations**:
  - One SVG = **one Smart Object** — Photoshop does NOT explode the SVG's internal groups into separate PS layers; multi-layer screens need per-layer SVG export + per-layer Place. evidence: [T02-S023]
  - **`File → Open` on an SVG rasterizes it into a single flat layer** (loses vector) — must use Place Embedded/Linked. evidence: [T02-S023]
  - Text: with `svg_outline_text=true` (default) text is paths; with `=false` text stays `<text>` but rendering varies, and inside a PS Smart Object it is editable only via Illustrator, not as PS text. evidence: [T02-S028]
- **典型使用場景**: icon/single-component extraction needing crisp vector + later edits.
- **不适合**: whole multi-layer frames (tedious); PS-native editable text.
- **Decay risk**: low.
- **信頼度**: high (一手 Adobe docs)

---

### 7. PDF → (Illustrator) → Photoshop (community offline route)

- **One-liner**: The Figma-Forum-endorsed offline path: export PDF from Figma → open in Illustrator → ungroup + unclip masks → save AI → Place into PS as a Smart Object. Text comes through as outlines.
- **Tier**: 場景特化
- **Maintainer / Owner**: Figma (PDF) + Adobe (AI/PS). Route documented by community (Todd Morgan). evidence: [T02-S022]
- **License**: all proprietary
- **What is preserved / lost**: vector shape fidelity survives better than Photopea; **text becomes outlines** (re-typed by copy from Figma if editability needed); masks must be manually unclipped in AI. evidence: [T02-S022]
- **Note**: Figma PDF is 1x only and drops Figma-unique blend modes (Plus darker/lighter) since those have no PDF/PS analog. evidence: [T02-S001, T02-S004]
- **典型使用場景**: vector-heavy or multi-element handoff, offline (no cloud upload), where outlined text is acceptable.
- **不适合**: editable-text PSDs; quick single-asset jobs (SVG route is faster).
- **Decay risk**: low.
- **信頼度**: high (一手 Adobe behavior + 二手 community route)

---

### 8. PNG @Nx → PS layers (pixel-faithful flat route; e.g. richardwhitner OSS)

- **One-liner**: Export each Figma layer as a high-res PNG and stack them in PS at correct positions — visually faithful, fully flat: text/vector/effects all baked in.
- **Tier**: 場景特化
- **Maintainer / Owner**: route is generic; reference OSS = richardwhitner/Figma-Export-For-Photoshop (Figma plugin emits PNGs + companion PS **JSX** script assembles PSD). evidence: [T02-S026]
- **License**: route = N/A; the OSS example is a public repo (WIP, ~3 commits, AI-authored — low maturity). evidence: [T02-S026]
- **What is preserved / lost**: pixel appearance + layer **positions and names**; **lost**: text editability, vector, layer effects (all rasterized to PNG). evidence: [T02-S026]
- **典型使用場景**: asset libraries, retouching handoff, AE imports where editability is irrelevant and only the pixels + layer separation matter.
- **不适合**: anything needing editable text/vector/effects.
- **Decay risk**: low (route); the specific OSS tool is high-risk (WIP).
- **信頼度**: high (一手 repo)

---

### 9. Figma REST API + ag-psd programmatic pipeline (Node) + Photoshop UXP assembler

- **One-liner**: The fully programmatic route for bulk/CI: pull node data + rendered images via REST, write PSDs with ag-psd, or assemble in-PS via a UXP plugin. Powerful but bounded by ag-psd's RGB/8-bit/no-redraw limits.
- **Tier**: 場景特化
- **Maintainer / Owner**: Figma (REST), Agamnentzar (ag-psd), Adobe (UXP)
- **License**: REST proprietary (token); ag-psd MIT; UXP requires CC
- **Pipeline shapes**:
  - **Path A (headless Node):** REST `GET images` → per-layer PNG/SVG → ag-psd `writePsd()` → PSD. You must supply every layer's bitmap (ag-psd won't render). RGB/8-bit only. evidence: [T02-S002, T02-S011]
  - **Path B (in-PS):** REST exports PNGs per layer → **UXP** plugin `createLayer({name,opacity,blendMode})` + `batchPlay` (wrapped in `executeAsModal`) assembles the layered PSD; use `createDocument`/`createLayer` for common ops, batchPlay for anything not in the DOM. evidence: [T02-S007]
- **Scripting platform note**: **ExtendScript/ESTK was deprecated in 2020** (no longer ships with CC, won't run on 64-bit-only macOS); build new automation on **UXP** (batchPlay is the evolution of executeAction). Legacy `.jsx` still runs but is not the path forward. evidence: [T02-S007, T02-S008]
- **不适合**: no-code teams; CMYK/16-bit print output (ag-psd can't write it); expecting auto-rasterization.
- **Decay risk**: low (all are strategic/maintained).
- **信頼度**: high (一手 Figma + Adobe + ag-psd docs)

---

### 10. Codia AI Psd2Figma (新興 / marketing-claim)

- **One-liner**: AI-based bidirectional PSD↔Figma; the Figma→PSD direction is real per vendor copy, but "fully editable / pixel-perfect" is **self-authored marketing with no independent evidence**.
- **Tier**: 新興 / 実験 (`stability: experimental`)
- **Maintainer / Owner**: Codia AI — https://codia.ai
- **License**: freemium ("start free, upgrade")
- **Vendor claims (label: marketing-claim, NOT verified)**: "Convert PSD ↔ Figma … fully editable layers"; "text, shapes, effects, groups … preserved"; "fonts, blending modes, smart objects, layer effects … translate cleanly"; "trusted by 300,000 professionals." evidence: [T02-S019]
- **Independent evidence**: none found — page is testimonials + feature copy only; no benchmark, no technical docs. **Contradiction with community consensus** (T02-S022) that NO tool keeps full editability. evidence: [T02-S019, T02-S022]
- **不适合**: any decision that depends on the fidelity claim being true without your own test file.
- **Decay risk**: high — AI tool churn + unverified claims.
- **信頼度**: low (二手 vendor self-promotion)

---

### 11. Magicul SaaS Converter (新興 / marketing-claim)

- **One-liner**: Paid cloud converter ($94+) claiming "100% pixel perfect" Figma→PSD; the only "comparison" content is Magicul's own blog — biased and unverified.
- **Tier**: 新興 / 実験 (`stability: experimental` for our trust purposes)
- **Maintainer / Owner**: Magicul — https://magicul.io
- **License**: proprietary SaaS (from $94)
- **Vendor claims (label: marketing-claim)**: "100% pixel perfect conversion," "supports Groups & Layers," "all native Figma elements," "Full Artboard + Style support." **No limitations disclosed; no technical method; no third-party validation** (only customer logos). evidence: [T02-S020]
- **Telling self-admission**: Magicul's own comparison concedes "Photopea is not a vector software … files often end up pixelated" — useful as corroboration that the *raster problem is real*, but the piece is marketing for Magicul, so its own superiority claim stays unverified. evidence: [T02-S021]
- **不适合**: budget-sensitive work; anyone needing a verifiable fidelity guarantee; bulk (per-file cost escalates).
- **Decay risk**: high — SaaS/pricing/vendor risk; claims unverified.
- **信頼度**: low (二手 self-promotion)

---

### 12. Figma MCP Server (新興 — out of scope for PSD)

- **One-liner**: AI design-to-code bridge (Cursor/VS Code). Writes/reads Figma canvas and emits code; **no PSD direction** — listed only to rule it out.
- **Tier**: 新興 / 実験
- **Maintainer / Owner**: Figma Inc. evidence: [T02-S006]
- **Relevance to Figma→PSD**: none. evidence: [T02-S006]
- **Decay risk**: high (beta). **信頼度**: high (一手 docs) that it is *irrelevant* here.

---

### 13. @webtoon/psd (READ-ONLY — inspection, not generation)

- **One-liner**: Fast zero-dependency PSD/PSB **parser** (read only) for validating/inspecting generated PSDs; cannot write.
- **Tier**: 場景特化 (QA tooling)
- **Maintainer / Owner**: Webtoon — https://github.com/webtoon/psd
- **License**: MIT
- **Maturity**: v0.4.0 (2023); layer-effects support "work in progress"; no recent release → declining signal. evidence: [T02-S029]
- **典型使用場景**: automated diff/QA of a pipeline's PSD output (read layer tree/metadata, compare against expected).
- **不适合**: writing PSDs (use ag-psd).
- **Decay risk**: medium (stale).
- **信頼度**: high (一手 GitHub)

---

## Context: Adobe–Figma Merger Collapse (Dec 2023) and its interop effect

- Adobe and Figma **terminated the merger on 2023-12-18**, citing "no clear path to receive necessary regulatory approvals from the **European Commission and the UK Competition and Markets Authority**." evidence: [T02-S024]
- **Correction vs prior draft**: Adobe's own press release says only "the previously agreed upon termination fee" — it does **NOT state "$1 billion."** The $1B figure is from the original deal terms/media reporting, not this primary source. Treat the amount as 二手/推断 unless a deal-terms source is cited. evidence: [T02-S024]
- **Interop implication (推断, well-supported):** no joint Photoshop↔Figma technical roadmap was ever announced; the only forward-looking statement was a vague "look for ways to partner … in the future." Combined with Figma export having no PSD on any surface (T02-S001/2/3), there is **no imminent first-party Figma→PSD path**; the gap stays third-party/bridge-filled indefinitely. evidence: [T02-S024, T02-S001]

---

## Rendering Gap Inventory (Figma vs Photoshop) — the "why it won't look identical" table

| Dimension | Figma behavior | Photoshop behavior | Conversion impact | evidence |
|-----------|----------------|--------------------|--------------------|----------|
| Blend modes | **19** modes incl. **"Plus darker"/"Plus lighter"** (Figma names) | No identical "Plus darker/lighter"; nearest are Linear Burn / Linear Dodge(Add) but math differs | Per-layer manual check; Figma-unique modes drift | T02-S004 |
| Group blending | **"Pass through"** is the group/frame default | **PS has no pass-through layer blend**; layer *styles* are always pass-through; group "Normal" isolates | Flattening a group changes compositing of non-normal children | T02-S004, T02-S025 |
| Color profile | sRGB (default) or Display P3; export uses **file's profile** | Configurable ICC; sRGB IEC61966-2.1 the safe match | Align BOTH to sRGB IEC61966-2.1 or colors shift | T02-S005 |
| Vectors | True vector shapes/booleans | Vector via Smart Object only | Photopea **rasterizes**; only SVG/PDF→Place keeps vector | T02-S014, T02-S023 |
| Text | Own renderer; live text | Live text or rasterized | Plugins ≈ best-effort live text (often imperfect); SVG/PDF outline it; ag-psd needs you to supply the bitmap | T02-S011, T02-S022, T02-S001 |
| Components/instances | Master/instance system | Smart Objects (loose analog) | Instances flatten to layers in most routes | T02-S022 |
| Effects | Drop/inner shadow, layer/background blur | Layer styles; no native background blur | Background blur has **no PS equivalent** → approximate/raster | T02-S004 |
| Resolution | 72 DPI × scale (UI ≤4x; REST 0.01–4) | 300 DPI print standard | Export 3–4x PNG for screen→print bridging; or vector route | T02-S001, T02-S002 |
| Color mode/bit depth | RGB (8-bit working space) | RGB/CMYK/Lab, 8/16/32-bit | Code route via ag-psd = **RGB 8-bit ONLY**; CMYK needs Photopea→PS or manual rebuild | T02-S011 |

---

## 選型決策樹 (Tool-Selection Decision Tree)

### Q0 — Do you need EDITABLE layers, or a PIXEL-FAITHFUL flat match?

**A. PIXEL-FAITHFUL (looks identical; layers may be flat/raster)**
- Single asset / few frames, free, fastest → **Photopea** (open `.fig` → Save as PSD). Pre-load fonts (TTF/OTF) first. Accept vector→raster. evidence: [T02-S012, T02-S014]
- Need clean per-layer raster with correct names/positions (asset lib, AE) → **PNG @3–4x per layer → PS stack** (manual or richardwhitner-style JSX). evidence: [T02-S026]
- Whole multi-page file, hands-off, budget OK, claim-tolerant → **Magicul/Codia** — but run YOUR test file first; treat "pixel perfect" as unverified. evidence: [T02-S020, T02-S019]

**B. EDITABLE (text stays text / vectors stay vectors)**
- Want in-Figma one-click w/ best-effort editable text → **PSD Exporter & Importer** plugin (offline). Expect to fix some effects/text. evidence: [T02-S017, T02-S022]
- Motion handoff (After Effects/Premiere) → **PSD Export** plugin. evidence: [T02-S018]
- Single vector asset/icon you'll keep editing → **SVG → PS Place Embedded** (1 Smart Object; edit in Illustrator). Use `File→Place`, never `File→Open`. evidence: [T02-S023]
- Vector-heavy frame, offline, outlined text OK → **PDF → Illustrator (ungroup/unclip) → PS Smart Object** (re-type text from Figma if needed). evidence: [T02-S022]

### Q1 — Single asset vs whole multi-page file?
- Single/few → Photopea or SVG-Place (above). Whole file → exporter plugin (editable) or Photopea/Magicul (flat); for many files use the **REST+ag-psd / UXP** pipeline. evidence: [T02-S002, T02-S007]

### Q2 — Auto-layout-heavy / component-heavy?
- **No tool transfers auto-layout or live components.** They flatten to static groups/layers everywhere. Pick the route by Q0 and accept the flatten; don't chase a tool that "keeps auto-layout" — none exists. evidence: [T02-S022]

### Q3 — Print / CMYK / 16-bit?
- **ag-psd cannot write CMYK or 16-bit.** For CMYK go **Photopea→PS** (then convert mode in PS) or rebuild in PS. For ~300 DPI from a code route, render 4x RGB and convert in PS. evidence: [T02-S011]

### Q4 — Security / no cloud upload?
- Use the **offline PSD Exporter & Importer** plugin or the **PDF→AI→PS** route. Avoid Magicul/Codia (cloud) and note Photopea processes client-side but is still a web app. evidence: [T02-S017, T02-S022]

---

## 避坑清單 (Anti-Pattern List)

- **❌ Hunting for a native Figma "Export → PSD."** It does not exist on the UI panel, REST API, or plugin `exportAsync` (and PDF is NOT even a plugin-export format). evidence: [T02-S001, T02-S002, T02-S003]
- **❌ `File → Open` on an SVG in Photoshop.** Rasterizes to a single flat layer, killing vector. Use **Place Embedded/Linked** for a Smart Object. evidence: [T02-S023]
- **❌ Believing ag-psd gives "free" editable text.** Write a text layer without supplying matching pixels → Photoshop pops a warning and the composite is invalid. You must pre-render every text/vector/smart-object bitmap yourself. evidence: [T02-S011]
- **❌ Routing CMYK/16-bit print work through any ag-psd-based tool.** RGB 8-bit only. Use Photopea→PS or rebuild. evidence: [T02-S011]
- **❌ Taking "100% pixel perfect" (Magicul) or "fully editable / pixel-perfect" (Codia) at face value.** Both are self-authored marketing; no independent benchmark exists; community consensus says full editability is unsolved. Always test your own file. evidence: [T02-S019, T02-S020, T02-S022]
- **❌ Expecting auto-layout, live components, or background blur to survive.** None do — they flatten/rasterize in every route. evidence: [T02-S004, T02-S022]
- **❌ Assuming Figma "Plus darker/lighter" match in PS.** Figma-unique; Linear Burn/Dodge differ in math — verify per layer. evidence: [T02-S004]
- **❌ Ignoring pass-through semantics.** PS has no pass-through layer blend and treats styles as always-pass-through; flattening a Figma group with non-normal children changes the composite. evidence: [T02-S025]
- **❌ Exporting 1x PNG for print.** 72 DPI = postage stamp at print size; export 3–4x or use the vector route. evidence: [T02-S001]
- **❌ Skipping color-profile alignment.** Set BOTH Figma and PS to sRGB IEC61966-2.1 before review or colors drift. evidence: [T02-S005]
- **❌ Building new automation on ExtendScript/CEP.** ESTK deprecated 2020; use UXP (batchPlay/executeAsModal). evidence: [T02-S007, T02-S008]
- **❌ Reaching for Avocode.** Sunset 2023-10-01 (team → Ceros); all products offline. evidence: [T02-S027]
- **❌ Trusting Photopea right after a Figma update.** `.fig` is an undocumented internal Kiwi format; schema changes have broken Photopea import before. evidence: [T02-S015, T02-S016]

---

## Phase 2 提炼提示

**反复出现 ≥3 source 都强调的「工具选型原則」**:

1. **No route yields a fully-editable, parity layered PSD** — every method forces a tradeoff among text/vector/effects/structure; pick the *acceptable loss*. (出现于: T02-S012 / T02-S022 / T02-S025 / T02-S011)
2. **ag-psd's RGB-8bit-no-redraw ceiling defines the whole code-based ecosystem** — "which plugin" ≈ "which wrapper around ag-psd, and how much pixel-prerendering it does." (出现于: T02-S009 / T02-S011 / T02-S017)
3. **The structural gap is permanent** — no native PSD export on any Figma surface + a dead merger (Dec 2023, no interop roadmap) = third-party/bridge tools indefinitely. (出现于: T02-S001 / T02-S002 / T02-S003 / T02-S024)
4. **Color-profile alignment (sRGB IEC61966-2.1 both sides) is the cheapest high-ROI fidelity step** most skip. (出现于: T02-S005)
5. **Vectors are the first casualty** — Photopea rasterizes; only SVG/PDF→Place keeps them; this drives the editable-vs-faithful fork. (出现于: T02-S014 / T02-S023 / T02-S021)

**显著的工具流派分裂** (心智模型候选):
- **派 A — In-Figma plugin exporters** (PSD Exporter & Importer, PSD Export, Codia): one workflow, no extra tool; quality capped by what the dev exposes through an ag-psd-class writer; abandonment risk.
- **派 B — External converters** (Photopea, Magicul): Photopea free + opens `.fig` natively but rasters; Magicul paid w/ unverified claims.
- **派 C — Bridge routes** (SVG/PDF→PS Place, PNG@Nx→PS, REST+ag-psd+UXP): leverage existing PS import/automation; the only way to keep true vector (Smart Object) or to scale programmatically; cost = per-layer tedium or engineering.
- Underlying axis = **editability vs visual fidelity** (and **manual vs programmatic**) — the spine of the decision tree.

**新兴工具信号**:
- 上升但未验证: Codia AI (AI bidirectional), Magicul (SaaS) — both marketing-claim, no benchmark.
- AI-authored throwaway tooling appearing (richardwhitner OSS "written primarily by ChatGPT-4") — signal that the niche is now LLM-bootstrapped; expect more low-maturity entrants.
- 出现→主流 估计: plugin maturity ~12–18 mo (推断 from cadence); but the *category* is stable/stuck because of the structural gap.

**冷僻 / 信号薄弱 (Phase 2.8 诚实边界)**:
- 必備层 only 2 (Photopea + ag-psd) — reflects reality, not thin research: the problem is genuinely unsolved, so there is no dominant tool.
- **No neutral, independent benchmark of Figma→PSD converter fidelity exists** (2026-06-03) — all "comparisons" are vendor blogs. Every fidelity claim in this track for Codia/Magicul is therefore vendor-reported. **GAP, explicit.**
- Two community quirks (Photopea vector-split, shadow-opacity reset) lack a current first-party page → marked 推断.
- The "$1B" Adobe→Figma fee is media/deal-terms, not in Adobe's primary release → marked 二手.

---

*OPUS verify/deepen pass: 2026-06-03. Sources: 29 (verified_primary 18 / secondary 11 / blacklisted 0). Candidates explored ~20; retained 13 cards across 9 routes. Dropped: Zeplin/Sympli (handoff, not PSD export), html.to.design & psd.to.design (PSD→Figma or Figma→HTML, wrong direction), psd.js/meltingice (inactive). Major corrections to sonnet draft logged inline: Figma blend-mode count (24→19); plugin exportAsync formats (PDF removed); ag-psd text/composite reality (no free editable text; 16-bit fix is read-side); ag-psd version (30.0.1 / npm 30.1.1); Photopea 4.6 date (2020-01-27); Photopea caveat attribution (only fonts on tutorial; vectors via issue #4455); Adobe $1B fee not in primary source; Avocode/`.fig`-lag re-sourced to first-party; added PDF→AI→PS and PNG@Nx routes + Kiwi `.fig` format depth.*
</content>
</invoke>
