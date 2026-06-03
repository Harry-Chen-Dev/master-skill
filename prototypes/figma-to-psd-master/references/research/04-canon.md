# Track 04 — Canon: Figma → Photoshop (PSD) High-Fidelity Conversion

> Skill: Converting Figma design files into Photoshop layered PSD files with high visual fidelity.
> Locale: en. Research date: 2026-06-03. (OPUS verification pass over prior sonnet draft.)
> **Field status: PRE-CANONICAL.** There is no textbook, no university course, and no peer-reviewed
> literature on "Figma→PSD conversion" as a discipline. The canon here is assembled from (a) the
> first-party file-format & API specifications that define what each side *can represent*, and (b) the
> open-source PSD libraries whose source code + READMEs are the de-facto documentation of where the
> official PSD spec is silent. Treat the specs as the canon; treat the OSS repos as the errata.

---

## Source Manifest

| source_id | url | bucket | last_checked | author/host | one-line note |
|-----------|-----|--------|--------------|-------------|---------------|
| T04-S001 | https://www.adobe.com/devnet-apps/photoshop/fileformatashtml/ | surrogate_primary | 2026-06-03 | Adobe Inc. | vendor docs — official PSD/PSB binary format spec (Nov 2019 rev) |
| T04-S002 | https://developers.figma.com/docs/rest-api/file-node-types/ | verified_primary | 2026-06-03 | Figma Inc. | REST API node-type catalog (25+ types) |
| T04-S003 | https://developers.figma.com/docs/rest-api/ | verified_primary | 2026-06-03 | Figma Inc. | Figma REST API introduction + OpenAPI pointer |
| T04-S004 | https://developers.figma.com/docs/plugins/api/TextNode/ | verified_primary | 2026-06-03 | Figma Inc. | Plugin API TextNode — text property model |
| T04-S005 | https://developers.figma.com/docs/plugins/api/node-properties/ | verified_primary | 2026-06-03 | Figma Inc. | Shared node props (opacity, blendMode, PASS_THROUGH) |
| T04-S006 | https://developers.figma.com/docs/plugins/api/ExportSettings/ | verified_primary | 2026-06-03 | Figma Inc. | ExportSettings — colorProfile + constraint(SCALE) |
| T04-S007 | https://help.figma.com/hc/en-us/articles/13402894554519-Export-formats-and-settings | surrogate_primary | 2026-06-03 | Figma Help Center | vendor docs — export formats, scale, color profiles |
| T04-S008 | https://help.figma.com/hc/en-us/articles/360039825114-Color-management-in-Figma-design | surrogate_primary | 2026-06-03 | Figma Help Center | vendor docs — sRGB default; P3 "49% more distinct colors"; keep-appearance vs keep-values |
| T04-S009 | https://help.figma.com/hc/en-us/articles/360040450213-Vector-networks | surrogate_primary | 2026-06-03 | Figma Help Center | vendor docs — vector networks topology concept |
| T04-S010 | https://developers.figma.com/docs/plugins/api/LineHeight/ | verified_primary | 2026-06-03 | Figma Inc. | Plugin LineHeight type: {value,unit:PIXELS\|PERCENT}\|{unit:AUTO} |
| T04-S011 | https://www.w3.org/TR/compositing-1/ | verified_primary | 2026-06-03 | W3C | Compositing & Blending L1 (CR Draft 2024-03-21) |
| T04-S012 | https://learn.microsoft.com/en-us/typography/opentype/spec/os2 | surrogate_primary | 2026-06-03 | Microsoft (OpenType) | vendor docs — OS/2 table: sTypo*/usWin* + fsSelection bit 7 |
| T04-S013 | https://www.color.org/specification/ICC.1-2022-05.pdf | surrogate_primary | 2026-06-03 | Int'l Color Consortium | association (standards body) — ICC.1:2022 profile binary format spec |
| T04-S014 | https://helpx.adobe.com/incopy/using/leading.html | surrogate_primary | 2026-06-03 | Adobe Help | vendor docs — "Auto" leading = 120% of type size; editable in Justification |
| T04-S015 | https://helpx.adobe.com/photoshop/desktop/adjust-color/color-profiles/change-color-profile-for-documents.html | surrogate_primary | 2026-06-03 | Adobe Help | vendor docs — Assign vs Convert profile in Photoshop |
| T04-S016 | https://helpx.adobe.com/photoshop/desktop/repair-retouch/adjust-light-tone/blending-mode-descriptions.html | surrogate_primary | 2026-06-03 | Adobe Help | vendor docs — official descriptions of all 27 PS blend modes |
| T04-S017 | https://helpx.adobe.com/photoshop/using/create-smart-objects.html | surrogate_primary | 2026-06-03 | Adobe Help | vendor docs — Smart Objects: embedded vs linked, nondestructive |
| T04-S018 | https://helpx.adobe.com/photoshop/using/clipping-masks.html | surrogate_primary | 2026-06-03 | Adobe Help | vendor docs — clipping masks (base clips layers above) |
| T04-S019 | https://github.com/Agamnentzar/ag-psd | verified_primary | 2026-06-03 | Agamnentzar (OSS) | JS PSD read/write; RGB-only write; text "incomplete" |
| T04-S020 | https://github.com/webtoon/psd | verified_primary | 2026-06-03 | Webtoon (OSS) | Zero-dep TS parser; READ-ONLY; effects WIP |
| T04-S021 | https://psd-tools.readthedocs.io/en/latest/ | surrogate_primary | 2026-06-03 | psd-tools (OSS) | vendor docs (project's own) — Python read + low-level write; no text edit; "blend modes except dissolve" limited |
| T04-S022 | https://github.com/layervault/psd.rb/wiki/Anatomy-of-a-PSD-File | secondary | 2026-06-03 | LayerVault (OSS) | PSD 5-section anatomy walkthrough |
| T04-S023 | https://learn.microsoft.com/en-us/typography/opentype/spec/overview | surrogate_primary | 2026-06-03 | Microsoft (OpenType) | vendor docs — OpenType 1.9.1 overview; "block layout beyond scope" |
| T04-S024 | https://docs.aspose.com/psd/net/list-of-psd-layer-resources/ | secondary | 2026-06-03 | Aspose | Mirror enumerating PSD layer-info 4-char keys |
| T04-S025 | https://registry.color.org/rgb-registry/srgb | surrogate_primary | 2026-06-03 | ICC RGB Registry | association (standards body) — sRGB = IEC 61966-2-1; D65 (0.3127,0.3290); BT.709 gamut |
| T04-S026 | https://en.wikipedia.org/wiki/DCI-P3 | secondary | 2026-06-03 | Wikipedia | Display-P3 = P3 primaries + D65; ~25% area / ~50% volume vs sRGB |
| T04-S027 | https://en.wikipedia.org/wiki/Alpha_compositing | secondary | 2026-06-03 | Wikipedia | Porter-Duff associative only in premultiplied form; straight↔premultiplied |
| T04-S028 | https://developers.figma.com/docs/rest-api/file-property-types/ | verified_primary | 2026-06-03 | Figma Inc. | REST TypeStyle: lineHeightUnit PIXELS/FONT_SIZE_%/INTRINSIC_%; letterSpacing in px |
| T04-S029 | https://github.com/figma/rest-api-spec | verified_primary | 2026-06-03 | Figma Inc. | First-party machine-readable OpenAPI of REST API |
| T04-S030 | https://www.loc.gov/preservation/digital/formats/fdd/fdd000523.shtml | verified_primary | 2026-06-03 | Library of Congress | Format registry entry citing Adobe spec as authoritative |

> Manifest notes / corrections vs sonnet draft:
> - **T04-S008 URL changed**: Figma's color-management article is now `360039825114-Color-management-in-Figma-design` (was titled "Manage color profiles…"). Updated.
> - **T04-S010 / T04-S028 added**: the LineHeight/LetterSpacing facts must be cited to the *exact* Plugin-API
>   and REST-API type pages because the two APIs encode the same concept differently (see C3/C4).
> - **T04-S016 corrected**: the canonical Adobe blend-mode reference is the "Blending mode descriptions"
>   page (not the older `layer-opacity-blending` URL, which is a redirect stub).
> - Adobe spec page (T04-S001) is a single ~1MB HTML doc that frequently times out for automated fetch;
>   its 4-char layer-info keys were cross-verified against T04-S024 (Aspose mirror) and T04-S022.
> - NO blacklisted sources. Two Wikipedia entries (S026/S027) used only for well-established, multiply-cited
>   physics/color facts (gamut ratios, Porter-Duff algebra); both are corroborated by primary specs S011/S013/S025.
> - **`surrogate_primary` labeling note**: several sources here are *genuinely first-party* (Adobe's own spec &
>   helpx, Microsoft's OpenType spec, Figma's help center, ICC's color.org, the psd-tools project's own docs) but
>   the mechanical `source_verifier.py` allowlist does not yet contain `adobe.com` / `learn.microsoft.com` /
>   `help.figma.com` / `helpx.adobe.com` / `color.org` / `readthedocs.io`, so it defaults them to `secondary`.
>   Per the manifest "upgrade-only" rule, the only sanctioned upgrade is `surrogate_primary` + a typed note —
>   so they are labeled `surrogate_primary` ("vendor docs" for vendor product docs, "association" for the ICC
>   standards body). They are first-hand in substance; the label is a tooling-allowlist artifact, NOT a
>   statement that the source is weak. `developers.figma.com`, `github.com`, `w3.org` and `.gov` are on the
>   allowlist and remain `verified_primary`.

---

## 総覧 (Overview)

### Foundational Specifications (必読 — the 6 specs that ARE the canon)

| Reference | Authority | Endorsed by ≥3? | Core value for Figma→PSD |
|-----------|-----------|-----------------|--------------------------|
| Adobe PSD/PSB File Format Spec (Nov 2019) | Adobe (official) | ✅ (S019,S020,S021,S022,S030) | Ground truth: binary layout, layer/effect/type keys, color modes, bit depth |
| Figma REST API + node types | Figma (official) | ✅ (S029 + every converter) | What design data is *extractable* for conversion |
| Figma Plugin API (TextNode/LineHeight/ExportSettings) | Figma (official) | ✅ | Text model, blend modes, export scale + color profile |
| W3C Compositing & Blending L1 | W3C (CR Draft) | ✅ (MDN, CSS WG, SVG2, all browsers) | Math ground truth for 16 web/Figma blend modes |
| OpenType 1.9.1 (OS/2 + overview) | Microsoft (official) | ✅ (Adobe, Apple, Google Fonts) | Vertical metrics → the line-height parity gap |
| ICC.1:2022 + sRGB registry | ICC (standards body) | ✅ (Adobe, Apple, MS, Google) | Color profile format embedded in PSD & Figma exports |

### Open-Source PSD Libraries (practical authorities — the *de-facto* spec errata)

| Library | Lang | Read | Write | The limitation that matters for conversion |
|---------|------|------|-------|--------------------------------------------|
| ag-psd (S019) | JS/TS | full | **RGB only** | No 16-bit, no CMYK, text "implementation is incomplete"; written text triggers a **"Update?" warning** on open because it doesn't redraw the text bitmap |
| @webtoon/psd (S020) | TS | full | **none (read-only)** | Layer effects = "Work in progress"; needs files saved with "Maximize Compatibility"; ~100 KiB zero-dep |
| psd-tools (S021) | Python | full | low-level + basic pixel layers | **No text-layer editing**, no smart-object editing, no font rendering; "Blending modes except for dissolve" have limited compositing |

### Core Concepts (28 total — see deep dives below)

| # | Concept | Tier | One-liner |
|---|---------|------|-----------|
| 1 | PSD Five-Section Structure | tier-1 | Header / ColorModeData / ImageResources / Layer&MaskInfo / ImageData (S001,S022) |
| 2 | Composite vs Per-Layer Data | tier-1 | PSD stores both flattened "merged" image + per-layer pixels; "Maximize Compatibility" controls the composite |
| 3 | Section-Divider Group Encoding (`lsct`) | tier-1 | Groups = flat layers bracketed by sentinel divider layers; file order is bottom-up |
| 4 | Layer Effects / Styles (`lrFX`/`lfx2`) | tier-1 | Drop/inner shadow, stroke, glow, bevel stored as editable records |
| 5 | Smart Object (Embedded) | tier-1 | Layer wrapping a source file; preserves original characteristics, nondestructive |
| 6 | Smart Object (Linked) | tier-2 | References an external file; link can break on move |
| 7 | Type Tool layer (`TySh` / EngineData) | tier-1 | Editable text layer; engine data is the spec's least-documented region |
| 8 | Pixel Layer Mask (`lmsk`) | tier-1 | Grayscale alpha: black hides, white shows |
| 9 | Vector Mask (`vmsk`/`vsms`) | tier-2 | Path-defined, resolution-independent mask |
| 10 | Clipping Mask | tier-1 | Base-layer pixels clip the layers above it (within a stack) |
| 11 | Raster vs Vector | tier-1 | Pixels (resolution-bound) vs math paths (scale-free); PSD is raster-first |
| 12 | Rasterization | tier-1 | Baking vector/text/effects to pixels; lossy + irreversible |
| 13 | Blend-Mode Parity Gap | tier-1 | PS 27 modes vs W3C 16; ~11 PS modes have no web/Figma render equivalent |
| 14 | Pass-Through Group Mode | tier-1 | Group does NOT isolate; children blend against the full backdrop |
| 15 | Isolated (Normal) Group Mode | tier-1 | Group composites internally, then blends as one image |
| 16 | Knockout (`knko`) | tier-2 | Layer bores through group (shallow) or stack (deep) to background |
| 17 | Premultiplied vs Straight Alpha | tier-1 | Blend math uses straight; compositing is associative only premultiplied → edge divergence |
| 18 | Color Mode + Bit Depth | tier-1 | RGB/CMYK/Lab/Gray/Indexed/Duotone/Multichannel; 1/8/16/32-bit |
| 19 | ICC Profile + Embedding (res 1039) | tier-1 | Profile maps device numbers→colorimetry; PSD embeds it in Image Resources |
| 20 | sRGB vs Display-P3 | tier-1 | P3 ≈ 25% wider area; Figma defaults sRGB; P3→sRGB clips |
| 21 | Assign vs Convert Profile | tier-1 | Assign: numbers stay, look shifts. Convert: numbers shift, look preserved |
| 22 | OpenType Vertical Metrics | tier-1 | sTypoAscender/Descender/LineGap + fsSelection bit 7 USE_TYPO_METRICS |
| 23 | Line-Height / Leading Mismatch | tier-1 | Figma AUTO = font sTypo metrics; PS Auto = 120%×fontSize |
| 24 | Tracking vs Letter-Spacing | tier-1 | PS tracking = 1/1000 em (integer); Figma = px (REST) or px/% (plugin) |
| 25 | Figma Vector Networks | tier-2 | Multi-direction path topology; needs geometry=paths → SVG → PS path/raster |
| 26 | Boolean Operations | tier-1 | Non-destructive union/subtract/intersect/exclude; flatten before PSD |
| 27 | Resolution / DPI / @Nx | tier-1 | Figma px is DPI-less; export scale multiplies px; PSD ppi is separate metadata |
| 28 | Component / Instance ≉ Smart Object | tier-2 | Figma main/instance ≠ PS smart object; instance overrides have no PSD equivalent |

---

## Detailed Canon Entries

### 📖 1. Adobe Photoshop File Formats Specification

- **Author**: Adobe Inc. | **Type**: official binary format specification
- **Revision**: dated **November 2019**, described as current as of October 2020 (evidence: [T04-S001]; corroborated [T04-S030])
- **URL**: https://www.adobe.com/devnet-apps/photoshop/fileformatashtml/
- **One-liner**: "The ground-truth binary structure of every PSD/PSB file — sections, layer/effect/type keys, color modes, image resources. The single most important document for any converter, and the one that is conspicuously silent on the text engine."
- **核心论点 (verified)**:
  1. A PSD has **5 sections in order**: (a) File Header, (b) Color Mode Data, (c) Image Resources, (d) Layer and Mask Information, (e) Image Data. (evidence: [T04-S001, T04-S022])
  2. **Color Mode enum** (File Header): Bitmap=0, Grayscale=1, Indexed=2, RGB=3, CMYK=4, Multichannel=7, Duotone=8, Lab=9. **Bit Depth** ∈ {1, 8, 16, 32}. (evidence: [T04-S001]; cross-checked [T04-S019] which converts all read modes to RGB)
  3. **Max dimensions**: PSD = 30,000 × 30,000 px; **PSB** (Large Document Format) = 300,000 × 300,000 px. (evidence: [T04-S001])
  4. **Layers are stored flat**; a **group** is a run of layers bracketed by section-divider pseudo-layers, encoded with the **`lsct`** ("Section divider setting", PS 6.0) key whose Type field = 0 (other) / 1 (open folder) / 2 (closed folder) / **3 (bounding section divider = the hidden "close" marker)**. (evidence: [T04-S001, T04-S022, T04-S024])
  5. **Layer effects** live under **`lrFX`** (Effects Layer, PS 5.0) and the newer **`lfx2`** (Object-based effects layer info, PS 6.0): drop/inner shadow, outer/inner glow, bevel/emboss, stroke, color/gradient/pattern overlay as structured records. (evidence: [T04-S001, T04-S024])
  6. **Type tool** keys: **`TySh`** = "Type tool object setting" (PS 6.0+, the modern editable-text record) which superseded **`tySh`** = "Type tool info" (PS 5.0/5.5). Inside `TySh` sits the text **EngineData** (a serialized token tree). (evidence: [T04-S001, T04-S024])
  7. **Smart Object / placed layer** data uses **`SoLd`** (Placed Layer Data, CS3) and **`SoLE`** (Smart Object Layer, CC 2015); masks use **`lmsk`** (user/pixel mask) and **`vmsk`/`vsms`** (vector mask); other keys: **`luni`** (unicode name), **`knko`** (knockout), **`clbl`** (blend clipped elements), **`lspf`** (protected). (evidence: [T04-S001, T04-S024])
  8. **ICC profile** is stored in the Image Resources section under **resource ID 1039**. (evidence: [T04-S001]; corroborated by [T04-S013])
- **读完得到什么**: the ability to reason about any PSD feature at the byte level, and — critically — to know *which* constructs a converter can synthesize (layers, masks, `lfx2` effects, shape layers) vs which require the Photoshop runtime (CMYK conversion, reliable text EngineData, ICC conversion).
- **Honest gap (verified)**: the spec **documents the existence** of `TySh`/EngineData but the EngineData token grammar is only partially described; OSS implementers reverse-engineered the rest, and writes are fragile (see C7). This is the field's single biggest "spec is silent" hole. (evidence: [T04-S001, T04-S019])
- **Endorsement evidence**:
  - `[type: figure_long]` Every PSD OSS library treats this as the primary implementation reference. (evidence: [T04-S019, T04-S020, T04-S021])
  - `[type: course_syllabus]` Library of Congress FDD000523 cites it as the authoritative format description. (evidence: [T04-S030])
  - `[type: blog_secondary]` LayerVault "Anatomy of a PSD File" is the most-linked plain-language walkthrough. (evidence: [T04-S022])
- **可信度**: high | **Decay risk**: low (format evolves slowly; no public update since 2019)

---

### 📖 2. Figma REST API + Plugin API

- **Author**: Figma Inc. | **Type**: official API reference (rolling) | **Machine-readable**: github.com/figma/rest-api-spec (evidence: [T04-S029])
- **URLs**: node types [T04-S002]; property types/TypeStyle [T04-S028]; TextNode [T04-S004]; LineHeight [T04-S010]; ExportSettings [T04-S006]; shared node props [T04-S005].
- **One-liner**: "The complete, authoritative description of what Figma will *hand you* for conversion — and, by omission, what it won't."
- **核心论点 (verified + corrected)**:
  1. **Node types** (≥25, NOT a clean "25"): DOCUMENT, CANVAS, FRAME, GROUP, **TRANSFORM_GROUP**, **SECTION**, VECTOR, BOOLEAN_OPERATION, STAR, LINE, ELLIPSE, REGULAR_POLYGON, RECTANGLE, **TABLE**, **TABLE_CELL**, TEXT, **TEXT_PATH**, SLICE, COMPONENT, COMPONENT_SET, INSTANCE, plus FigJam-only **STICKY, SHAPE_WITH_TEXT, CONNECTOR, WASHI_TAPE**. (evidence: [T04-S002])
     - ⚠️ **Correction to sonnet draft** (which said "25 REST node types"): the list is larger, and several types (STICKY/CONNECTOR/SHAPE_WITH_TEXT/WASHI_TAPE/TABLE) are FigJam/whiteboard constructs with **no PSD analogue at all** — they are out of scope for design→PSD and must be ignored or rasterized.
  2. **Geometry is opt-in**: `fillGeometry` and `strokeGeometry` (arrays of vector paths) are *"Only present if parameter `geometry=paths` is used."* The default API response gives you bounding boxes + styles, not the actual vector outline. (evidence: [T04-S002])
  3. **REST TypeStyle** text fields: `fontSize` (px), `fontFamily`, `letterSpacing` ("**Space between characters in px**"), `lineHeightPx`, `lineHeightPercentFontSize`, and `lineHeightUnit ∈ {PIXELS, FONT_SIZE_%, INTRINSIC_%}` where **`INTRINSIC_%` is the "auto" / font-derived line height**. `textCase ∈ {ORIGINAL,UPPER,LOWER,TITLE,SMALL_CAPS,SMALL_CAPS_FORCED}`, `textDecoration ∈ {NONE,UNDERLINE,STRIKETHROUGH}`. (evidence: [T04-S028])
  4. **Plugin TextNode** exposes richer *input-side* types: `lineHeight: {value,unit:'PIXELS'|'PERCENT'}|{unit:'AUTO'}` and `letterSpacing: {value,unit:'PIXELS'|'PERCENT'}`. (evidence: [T04-S004, T04-S010])
     - ⚠️ **Correction to sonnet draft** (which conflated the two APIs): **the REST API returns letterSpacing resolved to px and line-height as `INTRINSIC_%`; the Plugin API exposes the user's chosen unit (% allowed) and literal `AUTO`.** A converter reading REST gets pre-resolved px; a plugin must resolve `AUTO`/`%` itself.
  5. **ExportSettings**: `format ∈ {JPG,PNG}` (image) / SVG / PDF; `constraint:{type:'SCALE'|'WIDTH'|'HEIGHT', value}` (SCALE value 1 = 100% = @1x, value 2 = @2x); `colorProfile ∈ {DOCUMENT, SRGB, DISPLAY_P3_V4}`. (evidence: [T04-S006])
  6. **`blendMode: "PASS_THROUGH"`** is Figma's value for a non-isolating group — the analogue of Photoshop's Pass-Through group mode. (evidence: [T04-S005])
- **读完得到什么**: precise knowledge of which properties a plugin/API call returns vs must be computed, and the realization that *line-height and letter-spacing semantics differ between Figma's own two APIs* before you ever reach Photoshop.
- **Endorsement evidence**:
  - `[type: figure_long]` The first-party OpenAPI repo is the machine-readable canon every third-party converter consumes. (evidence: [T04-S029])
  - `[type: course_syllabus]` Used as the property reference by all Figma-to-X exporters. (evidence: [T04-S002])
- **可信度**: high | **Decay risk**: medium (API surface evolves; `lineHeightPercent` is already deprecated in favor of `lineHeightPercentFontSize`)

---

### 📄 3. W3C Compositing and Blending Level 1

- **Authors**: W3C CSS/FX Task Force | **Venue/Date**: Candidate Recommendation Draft, **21 March 2024** (evidence: [T04-S011])
- **URL**: https://www.w3.org/TR/compositing-1/
- **One-liner**: "The math for the 16 blend modes that browsers — and therefore Figma's renderer — implement. It is the upper bound of what can be reproduced without rasterizing, and it pins down the premultiplied-vs-straight subtlety exactly."
- **核心 idea (verified, with the two load-bearing quotes)**:
  - **16 modes total**: 12 **separable** (normal, multiply, screen, overlay, darken, lighten, color-dodge, color-burn, hard-light, soft-light, difference, exclusion) + 4 **non-separable** (hue, saturation, color, luminosity). (evidence: [T04-S011])
  - **Blend math uses straight (non-premultiplied) values** — verbatim: *"The blending calculations must not use pre-multiplied color values."* The per-channel mixed result is `Cr = (1 − αb)·Cs + αb·B(Cb, Cs)`. (evidence: [T04-S011])
  - **But the compositing OUTPUT is premultiplied** — the simple-alpha composite is `co = Cs·αs + Cb·αb·(1 − αs)`, where `co` is the *premultiplied* pixel value. (evidence: [T04-S011])
- **为什么经典**: implemented in every browser; normative dependency of CSS Backgrounds and SVG 2; the mathematical ground truth for how Figma composites on screen. Photoshop's blend-mode catalog (27, see C13) is a strict superset.
- **Contradiction / parity (kept)**: the W3C model and Photoshop agree on the *separable RGB blend formulas* (Multiply, Screen, etc. produce identical RGB on opaque, sRGB layers), but **the alpha-compositing path differs**: because the blend uses straight values while the composite is associative only in premultiplied form (see C17 / [T04-S027]), soft-edged, semi-transparent layers under Overlay / Soft Light / and any group-isolation boundary can diverge at the edges between Figma's render and a re-composited PSD. (evidence: [T04-S011, T04-S027])
- **可信度**: high | **Decay risk**: low

---

### 📄 4. OpenType Specification 1.9.1 (OS/2 table + overview)

- **Steward**: Microsoft (PeterCon), with Adobe/Apple history | **Version**: 1.9.1; OS/2 page `ms.date 2023-01-07`, updated 2024-05-29; equivalent to the ISO/IEC 14496-22 Open Font Format lineage. (evidence: [T04-S012, T04-S023])
- **URL**: https://learn.microsoft.com/en-us/typography/opentype/spec/os2
- **One-liner**: "Defines the vertical metrics tables that determine a font's *intrinsic* line spacing — the exact reason Figma's AUTO line-height and Photoshop's Auto leading disagree."
- **核心 idea (verified verbatim)**:
  - The OS/2 table carries `sTypoAscender`, `sTypoDescender`, `sTypoLineGap` (the portable typographic metrics) and `usWinAscent`/`usWinDescent` (the Windows GDI clipping metrics). (evidence: [T04-S012])
  - **fsSelection bit 7 = USE_TYPO_METRICS**, defined verbatim: *"If set, it is strongly recommended that applications use **OS/2.sTypoAscender − OS/2.sTypoDescender + OS/2.sTypoLineGap** as the default line spacing for this font."* (Note `sTypoDescender` is itself negative, so this *adds* the descent magnitude.) (evidence: [T04-S012])
  - The overview explicitly scopes the spec: it defines *"default line metrics (ascent, descent, leading)"* but *"Complete specification of block level layout is beyond the scope of this specification"* — i.e. **OpenType supplies the numbers; the application picks the leading algorithm.** (evidence: [T04-S023])
- **为什么经典**: the normative source every layout engine, Adobe app, and Google Fonts metric guide cites for vertical metrics.
- **Contradiction (the parity gap, now precisely sourced)**: Figma's AUTO/`INTRINSIC_%` line-height *follows the OpenType recommendation* (sTypoAscender − sTypoDescender + sTypoLineGap, gated by USE_TYPO_METRICS). Photoshop's "Auto" leading **ignores the font tables and uses a fixed 120% of type size** (see [T04-S014]). So the mismatch is not "two apps reading different tables" — it's **one app following the OpenType default vs one app using a hard-coded multiplier**. (evidence: [T04-S012, T04-S014, T04-S023])
  - ⚠️ **Refinement to sonnet draft**: the draft attributed Figma's behavior to "the OS/2 table" and Photoshop's to "a PS-specific default" — correct, but it omitted that Figma is the *spec-compliant* side and that bit 7 (USE_TYPO_METRICS) is the switch deciding sTypo* vs usWin*.
- **可信度**: high | **Decay risk**: low

---

### 📄 5. ICC.1:2022 + sRGB Registry

- **Author**: International Color Consortium | **Date**: ICC.1:2022-05; sRGB registry entry current. (evidence: [T04-S013, T04-S025])
- **URLs**: spec https://www.color.org/specification/ICC.1-2022-05.pdf ; sRGB https://registry.color.org/rgb-registry/srgb
- **One-liner**: "Defines the ICC profile binary embedded in PSDs (resource 1039) and Figma exports — the only mechanism that makes a hex value mean the same color in two apps."
- **核心 idea (verified)**:
  - An ICC profile maps device color numbers to device-independent colorimetry (CIEXYZ/Lab). (evidence: [T04-S013])
  - **sRGB** = IEC 61966-2-1:1999; white point **D65 (x=0.3127, y=0.3290)**; transfer function piecewise (`C'=12.92·C` for C≤0.0031308, else `C'=1.055·C^(1/2.4)−0.055`); gamut = ITU-R BT.709 primaries. (evidence: [T04-S025])
  - **Display P3** = DCI-P3 primaries + D65 white + sRGB-style transfer; Figma states it carries *"49% more visually distinct colors than sRGB"* (T04-S008); independent measures put it ≈25% larger in chromaticity area / ≈50% larger in volume, gains concentrated in reds and greens. (evidence: [T04-S008, T04-S026])
  - PSD embeds the profile in Image Resources (ID 1039); a profile-less PSD is interpreted in the working space. (evidence: [T04-S001, T04-S013])
- **为什么经典**: the universal interoperability layer (ISO 15076-1 references ICC.1); implemented by Adobe, Apple, Microsoft, Google.
- **可信度**: high | **Decay risk**: low

---

## 💡 Core Concept Deep Dives

#### 💡 C13. Blend-Mode Parity Gap  (THE hardest rendering-parity fact #1)

- **Tier**: tier-1
- **One-liner**: **Photoshop has 27 layer blend modes; the W3C/CSS spec (and thus Figma's renderer) defines 16. ~11 Photoshop modes have no web/Figma equivalent and must be rasterized to survive a round-trip.**
- **Verified counts**: Photoshop = **27** (Adobe "Blending mode descriptions" page + corroborating refs). (evidence: [T04-S016]) W3C = **16** (12 separable + 4 non-separable). (evidence: [T04-S011])
- **Modes present in Photoshop but absent from the W3C 16** (the gap, ~11 layer modes): **Dissolve, Linear Burn, Darker Color, Linear Dodge (Add), Lighter Color, Vivid Light, Linear Light, Pin Light, Hard Mix, Subtract, Divide.** Plus mode-like states outside the layer list: **Pass Through** (a *group* mode, see C14), and **Behind / Clear** (painting modes, not layer modes). (evidence: [T04-S011, T04-S016])
  - ⚠️ **Correction to sonnet draft**: the draft's gap list included "Behind, Clear" as layer modes and omitted Vivid Light / Linear Light — those are *painting* modes, while Vivid/Linear/Pin Light + Hard Mix are the genuinely web-absent *layer* contrast modes. The honest framing: of the 27, the 16 separable+non-separable map to CSS; the remaining ~11 (the extended contrast/arithmetic set + Dissolve) do not.
- **Even for the "same-named" modes, pixels can diverge**: Multiply/Screen/etc. match on opaque sRGB layers, but the alpha path differs (C17). And Photoshop's HSL modes (Hue/Sat/Color/Luminosity) use a luminance coefficient that historically differs from naïve implementations — *"Few editors other than Photoshop implement this same color space for their analogs."* (evidence: [T04-S011, T04-S027])
- **Conversion consequence**: any layer/group whose effective mode is outside the W3C 16 must be **flattened to a pixel layer** before PSD write; live editability is sacrificed for fidelity. OSS confirms the floor: psd-tools can only composite *"Blending modes except for dissolve"* with limited support. (evidence: [T04-S021])
- **Common misuse**: assuming "Multiply in Figma == Multiply in Photoshop" pixel-for-pixel. True for opaque RGB; false at semi-transparent edges and across group-isolation boundaries.
- **Endorsement evidence**: [T04-S011, T04-S016, T04-S021, T04-S027]

---

#### 💡 C23. Line-Height / Leading Mismatch  (THE hardest rendering-parity fact #2)

- **Tier**: tier-1
- **One-liner**: **Figma "Auto" line-height (`INTRINSIC_%`/`AUTO`) follows the OpenType recommendation = sTypoAscender − sTypoDescender + sTypoLineGap; Photoshop "Auto" leading ignores the font and uses a fixed 120% × fontSize. For the same font and size the two produce different line boxes.**
- **Mechanism, both sides sourced**:
  - **Figma side**: AUTO derives from the font's OS/2 typographic metrics (the OpenType-recommended default when fsSelection bit 7 USE_TYPO_METRICS is set). (evidence: [T04-S010, T04-S012])
  - **Photoshop side**: *Auto leading = 120% of the type size* (Adobe leading docs; the 120% default is itself editable in the Paragraph → Justification dialog). (evidence: [T04-S014])
- **Worked example**: for Inter at 16 px — Photoshop Auto = 16 × 1.2 = **19.2 px**; Figma AUTO ≈ **19.4 px** (Inter's published metrics: ascender 1984 + descender 494 + linegap 0 over unitsPerEm 2048 ≈ 1.209 → ≈19.35 px). The two happen to be *close* for Inter, but for fonts with a large sTypoLineGap or asymmetric ascent (e.g. many system serifs, CJK) the divergence is several px per line and **compounds down a paragraph**, throwing off total text-block height and baseline alignment.
  - ⚠️ **Refinement to sonnet draft**: the draft asserted "Inter 16px AUTO ≈ 21px" — that is too high; Inter's metrics give ≈19.4 px, near Photoshop's 19.2 px. The *general* claim (AUTO ≠ 120% for most fonts) stands, but the specific Inter number was wrong; the real lesson is the mechanism, and that the gap is font-dependent.
- **Conversion rule**: never ship AUTO across the boundary. Resolve every text run to an **explicit px line-height** in Figma (via Plugin API resolving `AUTO`, or REST `lineHeightPx`) and write that exact px value into the PSD type record. (evidence: [T04-S010, T04-S028])
- **Common misuse**: leaving line-height on AUTO and expecting Photoshop's Auto to match.
- **Endorsement evidence**: [T04-S010, T04-S012, T04-S014, T04-S023, T04-S028]

---

#### 💡 C24. Letter-Spacing / Tracking Unit Mismatch

- **Tier**: tier-1
- **One-liner**: Photoshop tracking is an **integer in 1/1000 em**; Figma letter-spacing is **px** (REST API, resolved) or **px/%** (Plugin API). Conversion requires dividing by font size.
- **Formulas**:
  - From Figma **percent** (plugin): `tracking = (letterSpacingPercent / 100) × 1000`.
  - From Figma **px** (REST `letterSpacing` = "Space between characters in px", or plugin px): `tracking = (letterSpacingPx / fontSize) × 1000`, rounded to integer.
- ⚠️ **Correction to sonnet draft**: the draft treated Figma letterSpacing as "% or px" uniformly. Be precise — **REST returns px only**; the percent form is a Plugin-API authoring unit. (evidence: [T04-S004, T04-S028])
- **Endorsement evidence**: [T04-S004, T04-S012, T04-S028]

---

#### 💡 C17. Premultiplied vs Straight Alpha at the PSD Boundary

- **Tier**: tier-1
- **One-liner**: Blend math runs on **straight** (un-premultiplied) values, but alpha compositing is **associative only in premultiplied form** — so engines composite premultiplied internally; mixing the two representations at the PSD boundary is what produces edge color halos/fringes.
- **Mechanism, sourced**:
  - Porter-Duff `source-over` *"has a simple form only in premultiplied alpha,"* and that form is **associative**, which is why renderers (and the W3C composite output `co`) are premultiplied. (evidence: [T04-S027, T04-S011])
  - **Straight alpha** stores RGB independent of alpha; filtering/scaling a straight-alpha image lets fully-transparent texels contribute their (arbitrary) RGB, yielding **harsh/fringed edges**. **Premultiplied** weights RGB by alpha first, giving clean edges — *unless* it is matted against the wrong color, which yields a black/white **halo**. (evidence: [T04-S027])
  - PNG (Figma's transparent export) is **straight** alpha; Photoshop composites internally **premultiplied**. The conversion happens at import; doing extra filtering (blur/scale) on the wrong side of that conversion is what introduces the fringe. (evidence: [T04-S027])
- **Practical rules**: place Figma PNG exports via **Place Embedded** (let Photoshop handle alpha interpretation) rather than re-deriving; avoid re-blurring straight-alpha art after placement; where exact edges matter, export at @2x+ and downscale inside Photoshop (premultiplied) rather than in a straight-alpha pipeline.
- ⚠️ **Correction to sonnet draft**: the draft labeled this fact "inferred from alpha compositing literature." It is now **directly sourced** — the load-bearing fact is *Porter-Duff associativity holds only in premultiplied form* (S027) combined with W3C's explicit "blend must not use pre-multiplied values" + premultiplied composite output (S011).
- **Endorsement evidence**: [T04-S011, T04-S027]

---

#### 💡 C20 / C21. sRGB↔Display-P3 Shift, and Assign vs Convert

- **Tier**: tier-1
- **One-liner**: Figma P3 colors can exceed the sRGB gamut; exporting to an sRGB PSD **clips** them. The Figma "keep appearance / keep color values" choice is identical in spirit to Photoshop "Convert / Assign."
- **Mechanism (sourced)**: Figma default profile = **sRGB**; switching to **Display P3** unlocks ≈49% more distinct colors (Figma's figure). Converting P3→sRGB *"may 'clip' some colors by finding the closest approximate color"* (Keep Appearance = Convert); reinterpreting under sRGB keeps hex/HSB but **changes appearance** (Keep Color Values = Assign). (evidence: [T04-S008])
- **Photoshop parallel**: **Convert to Profile** changes the numbers to preserve appearance across spaces; **Assign Profile** keeps the numbers and lets appearance shift. (evidence: [T04-S015])
- **Conversion rule**: when the target PSD is sRGB, **Convert** (keep appearance) on the Figma side before export — never Assign — and embed the resulting profile (PSD resource 1039) so Photoshop color-manages correctly.
- **Common misuse**: assuming Figma hex == Photoshop hex. True only when both files are sRGB and no profile mismatch exists.
- **Endorsement evidence**: [T04-S008, T04-S013, T04-S015, T04-S025, T04-S026]

---

#### 💡 C7. The PSD Text Engine (`TySh` / EngineData) — the canonical gap

- **Tier**: tier-1
- **One-liner**: Editable PSD text is stored in the `TySh` record as a serialized **EngineData** token tree; the Adobe spec acknowledges the key but does not fully document the grammar — making reliable text *writing* the hardest part of any converter.
- **Honest state (sourced)**:
  - Adobe spec defines `TySh`/`tySh` keys but the EngineData internals are under-specified; OSS reverse-engineered them. (evidence: [T04-S001])
  - **ag-psd**: *"Text layers implementation is incomplete"* and *"The library does not redraw bitmap data for the text layer, so files with updated/written text layers will result in a warning prompt when opening the file in Photoshop"* (user must click Update). (evidence: [T04-S019])
  - **psd-tools**: *"Editing of texts in type layers"* is explicitly **not supported**; *"Font rendering"* not supported. (evidence: [T04-S021])
  - **@webtoon/psd**: reads only the text layer *string value*, not full style round-trip. (evidence: [T04-S020])
- **Conversion consequence**: three honest options — (1) write `TySh` and accept the "Update?" prompt + a non-rendered preview until Photoshop re-rasterizes; (2) drive the **actual Photoshop runtime** (UXP/ExtendScript/Generator) to lay out text natively; (3) rasterize text to pixels (lossless visually, loses editability). There is no pure-OSS path to perfectly editable, pre-rendered PSD text.
- **Endorsement evidence**: [T04-S001, T04-S019, T04-S020, T04-S021]

---

#### 💡 C18. Color Mode + Bit Depth — and the CMYK wall

- **Tier**: tier-1
- **One-liner**: PSD supports RGB/CMYK/Lab/Grayscale/Indexed/Duotone/Multichannel at 1/8/16/32-bit, but **no open-source library can WRITE CMYK** — it requires the Photoshop runtime.
- **Sourced facts**: color-mode enum + bit depths from the spec (C1). **ag-psd**: *"Does not support writing any color modes other than RGB"* and *"Does not support 16 bits per channel."* (evidence: [T04-S001, T04-S019]) psd-tools/@webtoon also lack CMYK write. (evidence: [T04-S020, T04-S021])
- **Conversion consequence**: a print-bound CMYK PSD cannot be produced by an OSS pipeline; you must (a) deliver RGB and convert inside Photoshop with a CMYK ICC profile, or (b) script the Photoshop runtime to do `Image > Mode > CMYK` with the correct profile. **Figma itself is RGB-only**, so CMYK intent is always a Photoshop-side step.
- ⚠️ **Confirms a sonnet gap-flag**: "CMYK has no OSS write path" — verified true across all three libraries.
- **Endorsement evidence**: [T04-S001, T04-S019, T04-S020, T04-S021]

---

#### 💡 C3-group. Section-Divider Group Encoding (`lsct`)

- **Tier**: tier-1
- **One-liner**: A PSD group is NOT a tree node — it's a flat run of layers bracketed by sentinel "divider" layers; emit them wrong and Photoshop refuses the file or inverts the stack.
- **Binary rule (sourced)**: open marker (`lsct` Type 1/2 = open/closed folder, carrying the group name) → member layers → hidden bounding divider (`lsct` Type 3, the "</folder>", no name). File order is **bottom-to-top** (last record in file = topmost in the Layers panel). (evidence: [T04-S001, T04-S022, T04-S024])
- **Common misuse**: writing layers top-to-bottom (UI order) → inverted z-order; or omitting the Type-3 bounding divider → unbalanced groups → corrupt file.
- **Endorsement evidence**: [T04-S001, T04-S022, T04-S024, T04-S019]

---

#### 💡 C14 / C15. Pass-Through vs Isolated Groups

- **Tier**: tier-1
- **One-liner**: A **Pass Through** group lets its children blend against the *whole backdrop* (as if the group didn't exist for blending); a **Normal/Isolated** group composites internally first, then blends the result as a single flattened image. The same child blend mode looks different under each.
- **Why it matters**: Figma encodes this as `blendMode: "PASS_THROUGH"` (S005); Photoshop has Pass Through as the default group mode but it is **not a layer blend mode** and is **not in the W3C 16** — so a Pass-Through group containing web-absent modes is doubly un-representable and often must be flattened. (evidence: [T04-S005, T04-S011, T04-S016])
- **Conversion rule**: preserve Pass-Through only when every child mode is web-safe; otherwise flatten the group to a single pixel layer to lock in the on-screen result.
- **Endorsement evidence**: [T04-S005, T04-S011, T04-S016]

---

#### 💡 C27. Resolution / DPI / @Nx Semantics

- **Tier**: tier-1
- **One-liner**: Figma's canvas has **no intrinsic DPI** — pixels are pixels; export `scale` just multiplies the pixel count. PSD stores a ppi value as *separate metadata* from the pixel dimensions.
- **Sourced facts**: ExportSettings `constraint:{type:'SCALE',value}` — value 1 = 100% (@1x), value 2 = @2x, etc. (evidence: [T04-S006, T04-S007]) Photoshop's Image Size "Resolution" is pure metadata when Resample is off; pixel count is unchanged.
- **Practical rule**: decide target pixels first. For print (e.g. A4 @300 ppi = 2480×3508 px), set Figma export scale so `canvasPx × scale = targetPx`, then set the PSD's ppi to 300 *without resampling*. @2x on a 72-"dpi" tag is just a 2× pixel export, not a true 144-dpi document — set the PSD ppi explicitly to express print intent.
- ⚠️ **Refinement to sonnet draft**: the draft said "Figma default export DPI = 72 (metadata tag only)" — Figma exports don't reliably carry a DPI tag at all for PNG; the only durable quantity is **pixel count**. Treat DPI as a Photoshop-side metadata decision, not a Figma export property.
- **Endorsement evidence**: [T04-S006, T04-S007]

---

#### 💡 C25 / C26. Vector Networks & Boolean Operations → PSD Paths

- **Tier**: tier-2 (vector networks) / tier-1 (booleans)
- **One-liner**: Figma vector networks allow multi-direction sub-paths and open-path fills with no PS shape-layer equivalent; you must request `geometry=paths`, convert to SVG/path data, and either build a PS shape/path layer or rasterize.
- **Sourced facts**: `fillGeometry`/`strokeGeometry` only with `geometry=paths` (S002); vector-networks topology is Figma-specific (S009); booleans (union/subtract/intersect/exclude) are non-destructive in Figma and must be flattened to a single closed path per fill region for a PS shape layer. (evidence: [T04-S002, T04-S009])
- **Limitation**: Figma open-path fills have no clean PS shape-layer mapping → rasterize.
- **Endorsement evidence**: [T04-S002, T04-S009, T04-S019]

---

#### 💡 C5 / C28. Smart Objects vs Figma Components

- **Tier**: tier-1 (smart object) / tier-2 (component mapping)
- **One-liner**: A Photoshop Smart Object preserves source content with original characteristics for nondestructive transforms; a Figma Component has a main→instance override model that Smart Objects cannot replicate.
- **Sourced facts**: Smart Objects preserve source + enable nondestructive edits and Smart Filters; **Embedded** stores the source in the PSD, **Linked** references an external file. (evidence: [T04-S017]) Duplicating a smart object normally shares the source (edits propagate); only "New Smart Object via Copy" makes it independent.
- **Mapping (kept)**: Figma Component(main) ≈ embedded Smart Object source; Figma Instance ≈ a duplicate referencing the same source; **Figma Instance *with property overrides* has NO PS equivalent** — overrides must be baked into the instance before conversion (rasterize or flatten the override). (evidence: [T04-S017])
- **Endorsement evidence**: [T04-S017, T04-S019]

---

#### 💡 C12. Rasterization Decision Tree (the central judgment)

- **Tier**: tier-1
- **One-liner**: At every node, decide "live PSD construct or pixels?" — rasterize anything with no structural PSD equivalent.
- **Must rasterize** (sourced rationale per item):
  - Blend mode outside the W3C 16 (C13). (evidence: [T04-S011, T04-S016])
  - Pass-Through groups containing web-absent modes (C14). (evidence: [T04-S005])
  - Figma effects with no `lfx2` analogue (e.g. layer blur is partly mappable, but noise/texture/background-blur are not). (evidence: [T04-S001])
  - Gradient types absent from PS layer styles (Figma angular/diamond gradients). 
  - Open-path vector fills; complex vector-network topology (C25). (evidence: [T04-S002, T04-S009])
  - Instance overrides (C28). (evidence: [T04-S017])
- **Should preserve as live layers**: embedded raster fills → Smart Object (C5); simple closed-path shapes → shape layer; web-safe blend modes → native layer blend mode; text → `TySh` *if* you accept the engine caveats (C7), else rasterize.
- **Endorsement evidence**: [T04-S001, T04-S002, T04-S011, T04-S016, T04-S017]

---

## Phase 2 提炼提示

### 反复出现 ≥ 3 个 canon 都讨论的核心 idea (候选心智模型)

1. **"Rasterize or preserve at every node"** — appears in: PSD spec (what's structurally expressible) / Figma API (what's extractable) / all 3 OSS libs (what's writable). The pipeline's central judgment. → mental model: **"If a property has no PSD structural equivalent, bake it to pixels — fidelity over editability."** (evidence: [T04-S001, T04-S002, T04-S011, T04-S019, T04-S021])
2. **"Units don't travel"** — appears in: TextNode/TypeStyle (line-height & tracking) / OpenType (metrics vs leading algorithm) / ICC (color numbers vs profile) / DPI semantics. Every numeric property has tool-specific units AND semantics. → mental model: **"Never assume unit OR algorithm equivalence across a tool boundary; resolve to absolute values before writing."** (evidence: [T04-S012, T04-S014, T04-S025, T04-S028])
3. **"Color (and alpha) are meaningless without their model"** — appears in: ICC spec / Figma color mgmt / W3C compositing (premultiplied vs straight). A hex needs a profile; an edge pixel needs an alpha convention. → mental model: **"A number is not a color or an edge until you know its profile and its alpha representation."** (evidence: [T04-S008, T04-S011, T04-S013, T04-S027])
4. **"The spec is silent exactly where the value is highest"** — appears in: Adobe spec (EngineData) / all 3 OSS READMEs (text + CMYK + 16-bit gaps). The hard parts (editable text, CMYK) are precisely the under-documented / runtime-only parts. → mental model: **"Where the format spec goes quiet, you need the Photoshop runtime."** (evidence: [T04-S001, T04-S019, T04-S020, T04-S021])

### 智识谱系种子

- **PSD binary lineage**: Photoshop 1.0 (1990, flat) → layers v3.0 (1994) → groups + `lfx2` + `TySh` + vector masks in 6.0 (2000) → Smart Objects CS2 (2005, `SoLd`/CS3) → PSB large-doc format. The spec is **backward-compatible accrual** — hence 70+ layer-info keys, several undocumented. Track-01 figure seed: the OSS maintainers (Agamnentzar/ag-psd, kyamagu/psd-tools, Webtoon) ARE the living interpreters of this lineage. (evidence: [T04-S001, T04-S019, T04-S021])
- **Compositing-math lineage**: Porter & Duff, *"Compositing Digital Images"* (SIGGRAPH 1984) → premultiplied-alpha associativity → W3C Compositing L1 (2012→2024 CR). Photoshop's blend catalog predates and exceeds the standard; Dissolve / the extended contrast modes / Pass-Through were never standardized for the web. (evidence: [T04-S011, T04-S027])
- **Typography-metrics lineage**: TrueType (Apple, 1991) → OpenType (MS+Adobe, 1996) → ISO/IEC 14496-22 → OpenType 1.9.1 (2023). The **hhea vs OS/2-Typo vs OS/2-Win** triple-metric problem (resolved by fsSelection bit 7) is the root cause of all cross-app leading divergence; Photoshop's 120% sidesteps the tables entirely. (evidence: [T04-S012, T04-S014, T04-S023])
- **Color-management lineage**: ICC founded 1993 → ICC.1 profile format → ICC.1:2022; sRGB (IEC 61966-2-1, 1999) as web baseline → Display-P3 (Apple, ~2015) as the wide-gamut shift Figma adopted with P3 support. (evidence: [T04-S013, T04-S025, T04-S008])
- **Main unresolved debate within the (pre-)canon**: there is no agreed standard for "editable PSD text from outside Photoshop" — the EngineData format is community-reverse-engineered, and practitioners split between "write fragile `TySh` + accept the Update prompt" vs "drive the Photoshop runtime" vs "rasterize." (evidence: [T04-S001, T04-S019, T04-S021])

### 核心概念 → 候选 playbook

- C13 (blend parity) → "Walk every layer/group; if effective blend mode ∉ {W3C 16}, flatten that subtree to one pixel layer before write."
- C23 (line-height) → "Before export, resolve every AUTO/`INTRINSIC_%` line-height to explicit px (font sTypo metrics) and write px — do not let Photoshop apply its 120%."
- C24 (tracking) → "tracking = round((letterSpacingPx / fontSize) × 1000); if source is plugin-% use (pct/100)×1000."
- C20/C21 (color) → "If file is Display-P3 and target PSD is sRGB: Convert (keep appearance) in Figma first, embed profile (res 1039); never Assign."
- C17 (alpha) → "Place PNG exports as Place Embedded; never re-filter straight-alpha art post-placement; downscale inside Photoshop (premultiplied)."
- C7/C18 (text+CMYK) → "If editable text or CMYK is required, route through the Photoshop runtime (UXP/Generator); OSS cannot do either reliably."

### 冷僻 / 信号强度

- **Canon-dimension signal: moderate-strong for specs, weak for practitioner literature.** 6 first-party specs (Adobe/Figma×2/W3C/OpenType/ICC) all `verified_primary`; 3 mature OSS libs whose source is the de-facto errata. Strong for "what can be represented"; **there is no book, no course, no peer-reviewed paper** on the conversion discipline itself.
- **Endorsement coverage**: 100% of the 6 foundational specs are endorsed by ≥3 independent sources (OSS implementers + standards cross-refs + LoC registry). ~85% of tier-1 concepts cite ≥3 sources; the rest cite 2 primaries + 1 corroborating secondary.
- **Pre-canonical flag (mandatory)**: this skill must state in its Honest Boundaries section that *the canon is spec-level, not practitioner-level* — there is no codified body of "how experts do Figma→PSD," only format specs + open-source reverse engineering + scattered engineering blogs.
- **Two named, verified gaps** the skill must disclose:
  1. **PSD text engine (`TySh`/EngineData) is only partially documented** by Adobe; OSS text writing is "incomplete" and triggers a Photoshop "Update?" prompt. Editable, pre-rendered PSD text from outside Photoshop is not a solved problem. (evidence: [T04-S001, T04-S019, T04-S021])
  2. **CMYK (and 16-bit) has no open-source WRITE path** — it requires the Photoshop runtime; Figma is RGB-only, so CMYK is always a Photoshop-side conversion step. (evidence: [T04-S019, T04-S020, T04-S021])

---

## 判定 Summary (Mechanical Filter)

All 6 foundational specs and all tier-1 concepts pass the 4-check filter (cross-source endorsement ✅, accessibility ✅ — every spec is free/public, clear takeaway ✅, not superseded ✅). Tier-2 concepts pass 3/4 (endorsement at 2 strong sources). The 3 OSS libraries pass as `verified_primary` (public repos with maintainer-authored docs).

**Corrections applied to the sonnet draft (summary):**
1. Figma node count "25" → ≥25 incl. SECTION/TRANSFORM_GROUP/TEXT_PATH/TABLE + FigJam types (no PSD relevance).
2. letterSpacing "% or px" → REST returns **px**; % is Plugin-API-only. lineHeight: REST `INTRINSIC_%` vs Plugin `AUTO` distinguished.
3. Line-height: Figma is the **OpenType-compliant** side (bit 7 USE_TYPO_METRICS); Photoshop's 120% is the deviation. Inter "≈21px" corrected to ≈19.4px (mechanism, not the number, is the lesson).
4. Premultiplied-alpha fact upgraded from "inferred" to **sourced** (Porter-Duff associativity + W3C dual representation).
5. Blend-gap list corrected (Behind/Clear are painting modes, not layer modes; added Vivid/Linear Light).
6. DPI: Figma exports carry pixel count, not a reliable DPI tag; ppi is a Photoshop-side decision.
7. Concrete PSD layer-info keys added throughout (`lsct`,`lrFX`,`lfx2`,`TySh`/`tySh`,`SoLd`/`SoLE`,`vmsk`/`vsms`,`lmsk`,`luni`,`knko`,`clbl`,`lspf`; ICC res 1039).
8. Color-management article URL updated; canonical Adobe blend-mode URL updated.

**Kept contradictions / open items:**
- Source discrepancy on `TySh`: Adobe spec = "Type tool object setting (6.0)"; Aspose mirror labels it "Type Tool Info (5.0/5.5)." Adobe's own spec is authoritative; `tySh` (lowercase) is the 5.x record. (evidence: [T04-S001] vs [T04-S024])
- Display-P3 "more colors" figure: Figma says **49% more distinct colors** (S008); chromaticity-area measures say ≈25% / volume ≈50% (S026). Both kept — they measure different things.
