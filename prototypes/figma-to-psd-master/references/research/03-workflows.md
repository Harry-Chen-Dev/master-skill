# Track 03 — Workflows / SOPs: Figma → Photoshop (PSD) High-Fidelity Conversion

> Skill: converting Figma design files into Photoshop layered PSD files with high visual fidelity.
> Locale: en. Research date: 2026-06-03 (OPUS Wave-3 first-party pass, seeded by Tracks 01/02/04).
> **Field status: PRE-CANONICAL + PRACTITIONER-THIN.** There is no published "Figma→PSD SOP" anywhere.
> The workflows below are *assembled* by the researcher from (a) each tool's documented behavior + "typical use"
> (Track 02), (b) the rendering-gap facts that force specific prep steps (Track 04), (c) the one rigorous
> fidelity analyst in the field (Marc Edwards / Bjango, Track 01), and (d) first-party tool/API docs fetched
> this pass. Where a step is the researcher's synthesis rather than a sourced procedure it is marked **推断**.
> Because the source field is thin, every SOP leans on the *spec/tool-behavior* evidence rather than on any
> published expert procedure — this is a genuine domain characteristic, not a research shortfall (see Honest Boundary).

---

## Source Manifest

| source_id | url | bucket | last_checked | author/host | one-line note |
|-----------|-----|--------|--------------|-------------|---------------|
| T03-S001 | https://help.figma.com/hc/en-us/articles/360040521453-Optimize-design-files-for-developer-handoff | surrogate_primary | 2026-06-03 | Figma Help Center (vendor docs) | Pre-handoff prep: name layers/pages by ID, sections, Ready-for-dev, apply export settings |
| T03-S002 | https://help.figma.com/hc/en-us/articles/13402894554519-Export-formats-and-settings | surrogate_primary | 2026-06-03 | Figma Help Center (vendor docs) | Export DPI math (72×scale), suffix, Outline-text toggle, color-profile dropdown, slices behavior |
| T03-S003 | https://help.figma.com/hc/en-us/articles/360040028114-Export-from-Figma-Design | surrogate_primary | 2026-06-03 | Figma Help Center (vendor docs) | Multiple export settings (+ rows), per-object export, batch export-all |
| T03-S004 | https://help.figma.com/hc/en-us/articles/15023124644247-Guide-to-Dev-Mode | surrogate_primary | 2026-06-03 | Figma Help Center (vendor docs) | Dev Mode: inspect, asset export, Ready-for-dev, compare-to-previous |
| T03-S005 | https://www.figma.com/best-practices/guide-to-developer-handoff/ | secondary | 2026-06-03 | Figma (best-practices) | Designer-side handoff hygiene narrative |
| T03-S006 | https://www.photopea.com/tuts/convert-figma-to-psd/ | surrogate_primary | 2026-06-03 | Photopea / Kutskir (vendor docs) | Official .fig→PSD SOP: File→Open .fig, Save as PSD; load fonts first; vector-split + shadow-opacity quirks (sibling tracks label this verified_primary; verifier defaults photopea.com→secondary, so labeled surrogate_primary per upgrade-only rule) |
| T03-S007 | https://imagemagick.org/script/compare.php | surrogate_primary | 2026-06-03 | ImageMagick (vendor docs) | `compare -metric AE/RMSE/PSNR` CLI pixel-diff + diff image |
| T03-S008 | https://github.com/mapbox/pixelmatch | verified_primary | 2026-06-03 | Mapbox (GitHub) | JS pixel-diff; threshold 0–1 (def 0.1); antialias-aware; ~150 LOC |
| T03-S009 | https://rsmbl.github.io/Resemble.js/ | secondary | 2026-06-03 | Resemble.js | Browser image-diff w/ ignore-antialiasing; mismatch % output |
| T03-S010 | https://pdiff.sourceforge.net/ | secondary | 2026-06-03 | pdiff (SourceForge) | Perceptual (not naive) image-diff utility |
| T03-S011 | https://helpx.adobe.com/photoshop/desktop/repair-retouch/adjust-light-tone/blending-mode-descriptions.html | surrogate_primary | 2026-06-03 | Adobe Help (vendor docs) | Difference mode = subtract; identical pixels → black (overlay-diff QA basis) |
| T03-S012 | https://www.figma.com/blog/config-2024-recap/ | verified_primary | 2026-06-03 | Figma Blog | Config 2024: UI3, Figma AI, Slides, Dev Mode updates, Visual Search |
| T03-S013 | https://www.figma.com/blog/figma-adobe-abandon-proposed-merger/ | verified_primary | 2026-06-03 | Figma Blog | Figma's own merger-termination statement (2023-12-18) |
| T03-S014 | https://www.cnbc.com/2025/04/15/figma-confidentially-files-for-ipo-a-year-after-ditching-adobe-deal.html | secondary | 2026-06-03 | CNBC | Figma confidential IPO filing 2025-04; $1B break-fee context |
| T03-S015 | https://forum.figma.com/t/dev-mode-only-paid-accounts/55145 | secondary | 2026-06-03 | Figma Forum (community) | Dev Mode free beta ended; paid seat from 2024 |
| T03-S016 | https://www.figma.com/community/plugin/918334884511290351/quick-ios-export | secondary | 2026-06-03 | Figma Community (3rd-party) | Bulk per-scale (@1x/2x/3x) slice export plugin — represents the @Nx-export plugin class |
| T03-S017 | https://freebiesbooth.com/from-free-psd-to-figma-how-to-convert-old-resources-into-modern-ui-kits/ | secondary | 2026-06-03 | FreebiesBooth | "Convert if clean, rebuild if chaotic"; recreate type, never paste rasterized text |
| T03-S018 | https://www.npmjs.com/package/ag-psd | surrogate_primary | 2026-06-03 | npm (vendor pkg) | writePsd→ArrayBuffer / writePsdBuffer→Buffer; active releases |

> Manifest notes / corrections:
> - **`surrogate_primary` label**: `source_verifier.py classify` defaults `help.figma.com`, `helpx.adobe.com`,
>   `imagemagick.org`, `npmjs.com`, `photopea.com` to `secondary` because its allowlist lacks those hosts — but
>   they are genuinely first-party vendor product docs (Photopea's own official tutorial; Figma/Adobe help; the
>   ag-psd npm page). Per the Track-04 manifest precedent and the _source_id_manifest "vendor docs = verified in
>   substance, label is a tooling artifact" rule, they are marked `surrogate_primary` ("vendor docs"). Note the
>   sibling Tracks 01/02 labeled the Photopea tutorial `verified_primary`; this track keeps to the verifier's
>   upgrade-only path (secondary→surrogate_primary) rather than override to the top tier. `github.com`,
>   `figma.com/blog` ARE on the allowlist → `verified_primary`.
> - **Cross-track reuse (allowed)**: the per-method SOPs reuse Track 02 tool cards (T02-Sxxx) and Track 04 canon
>   (T04-Sxxx) as evidence; those IDs are NOT re-listed here — see 02-tools.md / 04-canon.md. New T03 sources: 18.
> - NO blacklisted sources. Medium/forum sources used only for community-consensus or to *represent a tool class*,
>   never as the sole basis for a load-bearing fidelity claim.

---

## 0. Decisive framing (read before any SOP)

**The single most important fact about this entire workflow domain:** there is no native Figma→PSD export and no
tool that yields a fully-editable, parity layered PSD (一手 consensus across Tracks 02/04, evidence:
[T02-S012, T02-S022, T02-S025, T04-S019]). Therefore the **decisive work happens *before* you run any converter** —
in Figma, deciding *which losses you accept and pre-resolving everything the converter cannot resolve for you*.
A clean pre-flight turns a 60%-fidelity dump into a 90%+ match; skipping it means no tool can save you.

This file is ordered the way a pro actually works:
1. **Pre-flight prep in Figma** (the highest-leverage section — §1)
2. **Six per-method end-to-end SOPs** (§2)
3. **The fidelity QA loop** — how you *prove* the PSD matches (§3)
4. **Beginner SOP vs senior path + convert-vs-rebuild** (§4)
5. **Recent workflow changes (last ~12 months)** (§5)
6. Overview table + Phase 2 interface (§6–7)

---

## 1. PRE-FLIGHT PREP IN FIGMA (the decisive checklist)

> **One-liner**: Before exporting/converting, normalize the Figma file so every property the target PSD *cannot
> auto-resolve* is already baked to an absolute, PSD-expressible value. This is the highest-ROI work in the whole skill.
> **Trigger**: you've decided to produce a PSD and chosen a method (§2). **Output**: a "conversion-ready" duplicate
> of the Figma file/frame. **Last_updated**: 2026-06-03. **Decay risk**: low (rooted in stable format gaps, not tooling).

**Rule 0 — work on a DUPLICATE.** Every step below is destructive to Figma editability (flatten, outline, rasterize).
Duplicate the page/frame ("Conversion copy") so the live design survives. *Skip → you destroy the working file.* (推断, universal practice)

### 1A. Structure & layer hygiene
- [ ] **Detach all component instances** (right-click → Detach instance). No PSD construct maps to Figma's
      main→instance override model; instances flatten to static layers in *every* route, and unresolved overrides
      get baked wrong. Detach so what you see is what exports. *Skip → instance overrides render unpredictably; component edits silently don't propagate.* evidence: [T02-S022, T04-S017 (C28)]
- [ ] **Flatten / "absorb" auto-layout** — auto-layout is a live constraint system with **no PSD equivalent**; it
      does not transfer. Confirm final positions are correct, then treat frames as static. (Optionally wrap an
      auto-layout frame in a plain Frame so geometry is frozen.) *Skip → nothing breaks visually, but you waste time hunting for "why my spacing moved" — it didn't transfer at all.* evidence: [T02-S022]
- [ ] **Name & organize layers** the way you want them in Photoshop — most routes (Photopea, @Nx-PNG, plugins)
      **carry layer names and positions verbatim** into the PSD; garbage names in = garbage PSD layer panel.
      Figma's own handoff guidance: name layers/components by their IDs, group with Sections. *Skip → an unnavigable PSD layer tree; downstream editor wastes hours.* evidence: [T03-S001, T02-S026]
- [ ] **Flatten boolean operations** (union/subtract/intersect/exclude) to a single vector per fill region —
      booleans are non-destructive in Figma and have no clean PS shape-layer mapping; flatten *before* PSD. *Skip → boolean result rasterizes inconsistently or splits into stray paths.* evidence: [T04-S002, T04-S009 (C26)]

### 1B. The text decision (outline vs keep-editable) — make it consciously, per text run
- [ ] **Decide the text strategy up front** — there is NO free "editable text" anywhere in this domain:
  - **Keep editable** → only via Photopea (re-rendered, fonts pre-loaded) or an in-Figma exporter plugin
    (best-effort), and ag-psd-written text triggers a Photoshop **"Update text layers?"** prompt because the
    bitmap isn't redrawn. evidence: [T02-S011, T04-S019 (C7)]
  - **Outline to vector** → SVG export with **Outline text ON** (Figma default), or the PDF→AI route. Crisp,
    portable, *not* re-typeable. evidence: [T02-S028, T03-S002, T02-S022]
  - **Rasterize** → PNG @Nx route; pixel-faithful, fully dead text.
- [ ] **Kill every AUTO line-height before export.** Figma AUTO follows OpenType metrics
      (sTypoAscender − sTypoDescender + sTypoLineGap); Photoshop "Auto" leading is a hard **120% × fontSize**.
      They disagree per font and the error *compounds down a paragraph*. Set every text run to an **explicit px
      line-height** in Figma. *Skip → multi-line text blocks drift in height and baseline; the single most common silent text-fidelity bug.* evidence: [T04-S010, T04-S012, T04-S014 (C23)]
- [ ] **Handle fonts (embed / substitute / outline):**
  - For Photopea: collect the actual **TTF/OTF** files; you must `File → Open` them into Photopea *first* so it
    redraws text in the real font, else it substitutes. This is the **only caveat on Photopea's own tutorial**. evidence: [T03-S006, T02-S012]
  - For any rasterize/outline route: fonts are baked, so substitution risk disappears (but editability is gone).
  - If a font can't be supplied at all → **outline it** in Figma so the shapes are correct regardless of the
    receiving machine's font set. evidence: [T02-S028]

### 1C. Effects, blend modes, masks — rasterize-or-not
- [ ] **Flatten any layer/group whose blend mode is outside the W3C 16.** Photoshop has 27 modes; Figma's renderer
      implements the W3C 16; ~11 PS contrast/arithmetic modes (Linear/Vivid/Pin Light, Hard Mix, Subtract, Divide,
      Linear Burn/Dodge, Darker/Lighter Color, Dissolve) have no Figma equivalent — and Figma's **"Plus darker /
      Plus lighter"** have no exact PS match either. If the effective mode won't round-trip, **rasterize that subtree
      to one pixel layer** to lock the on-screen result. *Skip → that layer composites with the wrong math; colors shift, especially at edges.* evidence: [T04-S011, T04-S016 (C13), T02-S004]
- [ ] **Rasterize background blur and any unsupported effect.** **Background/layer blur has no native Photoshop
      equivalent** — flatten it to pixels in Figma (or accept it will be approximated/dropped). Noise, texture, and
      angular/diamond gradients are likewise un-mappable → rasterize. *Skip → the blur vanishes or renders as a flat fill in the PSD.* evidence: [T02-S004, T04-S001 (C12)]
- [ ] **Note pass-through groups.** A Figma group defaults to **PASS_THROUGH**; PS has no pass-through *layer*
      blend. Preserve a group as live only if **every child mode is web-safe**; otherwise flatten the group to a
      single pixel layer — flattening a pass-through group with non-normal children changes the composite. *Skip → group compositing silently differs from Figma.* evidence: [T02-S004, T02-S025, T04-S005 (C14)]
- [ ] **Drop-shadow caveat (Photopea route):** community-reported that Photopea **resets shadow opacity to 100%**
      on import — pre-bake critical shadows into the layer art, or plan to re-set opacity in Photoshop. evidence: [T03-S006 (二手/community, also on Photopea tut)]

### 1D. Color-profile awareness (cheapest high-ROI step)
- [ ] **Align both sides to sRGB IEC61966-2.1.** Figma defaults to sRGB but can be **Display P3**; P3 colors exceed
      sRGB gamut and **clip** when exported to an sRGB PSD. If the file is P3 and the target PSD is sRGB:
      **Convert (keep appearance)** on the Figma side first — never *Assign / keep color values* — then export with
      the matching profile and let Photoshop color-manage. *Skip → reds/greens shift; "the colors look off" with no obvious cause.* evidence: [T02-S005, T04-S008, T04-S015 (C20/C21)]
- [ ] **Set the export `colorProfile` explicitly** in Figma's export panel (`Same as file / sRGB / Display P3`)
      rather than relying on the default. evidence: [T03-S002, T04-S006]

### 1E. Export geometry (slices, @Nx, resolution)
- [ ] **Decide target pixels first, then set scale.** Figma px is **DPI-less**; export `scale` just multiplies the
      pixel count (72×scale is only a metadata tag — `@2x` = DPI 144, `@3x` = DPI 216). For print, compute
      `canvasPx × scale = targetPx` (e.g. A4@300ppi = 2480×3508) and set the PSD's ppi *in Photoshop without
      resampling*. *Skip → a 1× export is a postage stamp at print size; you can't add resolution after the fact.* evidence: [T03-S002, T04-S006 (C27)]
- [ ] **For the rasterize routes, export @2x–4x even for screen** — downscale inside Photoshop (premultiplied)
      for clean edges; never re-filter straight-alpha PNGs after placement (avoids edge fringing). evidence: [T04-S027 (C17)]
- [ ] **Set up slices / multiple export rows** when you need per-asset or per-scale output: add multiple export
      settings (+ rows) with suffixes (`@1x/@2x/@3x`), or draw Slices for arbitrary regions. **Note SVG & PDF are
      1× only.** *Skip → tedious one-by-one re-export; missing/duplicated assets.* evidence: [T03-S002, T03-S003]

> **HIGHEST-LEVERAGE SINGLE STEP (if you do only one thing):** *resolve every text run's AUTO line-height to an
> explicit px value AND pre-load/outline fonts before export.* Text is where fidelity most visibly and most
> silently breaks (font substitution + the AUTO-vs-120% leading gap compounding down paragraphs), and unlike
> blend/color drift it is rarely caught by a quick eyeball check. (推断 from convergence of T04-S012/S014 + T02-S011/S012)

---

## 2. PER-METHOD END-TO-END SOPs

> Each SOP = numbered steps → "what to fix after" → fidelity caveats. All assume §1 pre-flight is done on a duplicate.
> Methods map 1:1 to the Track 02 method stack (a)–(f).

### 2(a). In-Figma exporter plugin → layered PSD

- **One-liner**: One-click, stays inside Figma, best-effort *editable* text/layers; quality capped by an
  ag-psd-class writer. **Trigger**: want a layered PSD without leaving Figma; privacy-sensitive (offline plugins exist).
  **Output**: a `.psd` with layers/groups/names, best-effort live text. **Last_updated**: 2026-06-03. **Decay risk**: medium (3rd-party plugin lifecycle).
- **SOP**:
  1. Run §1 pre-flight (esp. detach instances, resolve line-height, decide text strategy).
  2. Install an exporter plugin — e.g. *PSD Exporter & Importer* (offline; community-rated "works the best"; has
     **font mapping**) or *PSD Export* (motion/AE-oriented). evidence: [T02-S017, T02-S018]
  3. Select the frame(s) → run the plugin → choose layered/editable output → export `.psd`.
  4. Open in Photoshop.
- **What to fix after**: (1) click through the **"Update text layers?"** prompt if it appears (ag-psd-class writers
  don't redraw the text bitmap). (2) Re-check complex layer effects — vendors say effect transfer is "being
  refined." (3) Verify blend modes you flagged in §1C. evidence: [T02-S011, T02-S017, T02-S022]
- **Fidelity caveats**: auto-layout/components are gone (flattened); complex effects may not transfer; text fidelity
  across plugins is "a work in progress"; output bounded by the writer's **RGB / 8-bit, no-auto-render** ceiling. evidence: [T02-S022, T02-S011]

### 2(b). Photopea: open `.fig` → export `.psd`

- **One-liner**: Free, zero-install web app; the only tool that opens `.fig` *natively* and saves a real *layered*
  PSD — but it **rasterizes vectors**. **Trigger**: single asset/few frames, free, fast, pixel-faithful is fine.
  **Output**: layered PSD (structure preserved, vectors raster). **Last_updated**: 2026-06-03. **Decay risk**: medium (single dev + dependence on undocumented `.fig`).
- **SOP**:
  1. Run §1 pre-flight on a duplicate; **export the `.fig`** (Figma → right-click file → Save local copy / export `.fig`).
  2. In Photopea: **`File → Open` → select the `.fig`** (or drag-drop). The whole design structure loads with layers. evidence: [T03-S006, T02-S013]
  3. **Load fonts FIRST**: `File → Open` each custom **TTF/OTF**, so Photopea redraws text in the real font (else
     it substitutes — the *only* caveat on the official tutorial). evidence: [T03-S006, T02-S012]
  4. **`File → Save as PSD`** → download. evidence: [T03-S006]
- **What to fix after**: (1) **Re-merge over-split vectors** — Photopea splits one logo/SVG into many layers;
  group/merge them. (2) **Reset drop-shadow opacity** — reported to reset to 100% on import. (3) If you need CMYK,
  convert mode in Photoshop *after* (Photopea→PS is the only CMYK-capable route here). evidence: [T03-S006, T02-S014, T02-S011 (C18)]
- **Fidelity caveats**: vectors → raster is the **biggest hit** (Photopea "is not a vector software"); components
  flatten; **`.fig` is Figma's undocumented internal Kiwi format → import can break right after a Figma update** —
  re-test then. evidence: [T02-S014, T02-S015, T02-S016]

### 2(c). Export layers (SVG/PNG @Nx) → reassemble in Photoshop

- **One-liner**: Export each layer/asset from Figma, then stack at correct positions in PS — pixel-faithful and
  fully flat. **Trigger**: need correct per-layer raster (asset library, retouch handoff, AE import) where
  editability is irrelevant. **Output**: PSD with separated raster layers at right positions/names.
  **Last_updated**: 2026-06-03. **Decay risk**: low (route); the specific OSS helper (richardwhitner) is high-risk (WIP).
- **SOP**:
  1. §1 pre-flight; **name layers exactly** as you want them in PS (names carry over).
  2. In Figma, add Export settings per layer/slice: **PNG @2x–4x** (downscale later in PS) with `@Nx` suffixes;
     or **SVG** per layer for vector pieces. Use a bulk plugin (e.g. *Quick iOS Export* / *Export Options*) or
     **Dev Mode → Export all** to batch. evidence: [T03-S002, T03-S003, T03-S016, T03-S004]
  3. In Photoshop: **`File → Place Embedded`** each asset (NOT `File → Open` — that flattens). Position by the
     Figma x/y. evidence: [T02-S023]
  4. Rename/order layers; set the document ppi (no resample) for print intent. evidence: [T04-S006 (C27)]
- **What to fix after**: align placement (Figma coordinates → PS canvas); flatten/rasterize any SVG you don't need
  editable; set color profile to match §1D. (Automatable: richardwhitner's plugin emits PNGs + a companion **JSX**
  that assembles the PSD.) evidence: [T02-S026]
- **Fidelity caveats**: everything is rasterized (PNG route) → no editable text/vector/effects; tedious per-layer
  for big screens; PNG is straight-alpha so **don't re-blur/scale after placement** (edge fringing). evidence: [T02-S026, T04-S027 (C17)]

### 2(d). SVG → Place Embedded as Smart Object (single vector asset)

- **One-liner**: The only route that keeps a Figma asset as **true editable vector** inside PS — one SVG becomes
  one Smart Object. **Trigger**: a single icon/logo/component you'll keep editing, vector crispness required.
  **Output**: a resolution-independent Smart Object (edit by reopening in Illustrator). **Last_updated**: 2026-06-03. **Decay risk**: low (stable Adobe feature).
- **SOP**:
  1. In Figma, select the asset → Export as **SVG** (decide **Outline text**: ON = paths, OFF = `<text>` but
     rendering varies). evidence: [T03-S002, T02-S028]
  2. In Photoshop: **`File → Place Embedded` → select the SVG** → it lands as one Smart Object. **Never `File → Open`**
     (rasterizes to a flat layer). evidence: [T02-S023]
  3. Transform/scale freely (vector, non-destructive). Double-click the thumbnail to edit contents in Illustrator.
- **What to fix after**: if you need the SVG's internal groups as separate PS layers, **export each sub-element as
  its own SVG and Place each** — Photoshop does NOT explode one SVG into multiple PS layers. evidence: [T02-S023]
- **Fidelity caveats**: 1 SVG = 1 Smart Object only (multi-layer screens are tedious); text inside the SO is
  editable only via Illustrator, not as PS text. evidence: [T02-S023, T02-S028]

### 2(e). PDF → Illustrator → Photoshop (vector-heavy, outlined text)

- **One-liner**: The offline, vector-preserving multi-element route; text comes through as **outlines**.
  **Trigger**: vector-heavy frame, offline (no cloud upload), outlined text acceptable. **Output**: PS Smart
  Object containing the vector artwork (text as outlines). **Last_updated**: 2026-06-03. **Decay risk**: low.
- **SOP**:
  1. §1 pre-flight; in Figma export the frame as **PDF** (1× only). evidence: [T03-S002, T02-S001]
  2. Open the PDF in **Illustrator**; **ungroup** and **release/unclip** masks manually. evidence: [T02-S022]
  3. Save as `.ai`.
  4. In Photoshop: **`File → Place`** the `.ai` as a Smart Object. evidence: [T02-S023]
- **What to fix after**: re-type any text you need editable (copy strings from Figma — PDF text is outlined);
  rebuild clipping you released in AI; confirm colors (PDF drops Figma-unique **Plus darker/lighter** blend modes
  — no PDF/PS analog). evidence: [T02-S022, T02-S004]
- **Fidelity caveats**: text editability lost (outlines); masks need manual handling; 1× export only; Figma-unique
  blend modes don't survive. evidence: [T02-S022, T02-S001]

### 2(f). Programmatic / bulk: Figma REST API + ag-psd (or Photoshop UXP)

- **One-liner**: The CI/bulk route — pull node data + rendered images via REST, write PSDs with ag-psd, or assemble
  in-PS via UXP. Powerful, bounded by ag-psd's RGB/8-bit/no-redraw limits. **Trigger**: many files, automation/CI,
  engineering resource available. **Output**: PSDs generated headlessly or assembled in PS. **Last_updated**: 2026-06-03. **Decay risk**: low (all strategic/maintained).
- **SOP (Path A — headless Node):**
  1. `GET /v1/files/:key` (and `/nodes`) for the layer tree + styles; `GET /v1/images/:key` for **per-layer
     rendered PNG/SVG** (format jpg/png/svg/pdf; `scale` 0.01–4; >32 MP scaled down). You must render **every**
     layer's bitmap yourself. evidence: [T02-S002]
  2. Build the `Psd` object (layers, names, blendMode, opacity) and **attach each layer's `canvas`/`imageData`**
     (ag-psd does NOT auto-render). evidence: [T02-S011, T04-S019]
  3. `writePsd()` (→ ArrayBuffer) / `writePsdBuffer()` (→ Buffer) → write `.psd`. evidence: [T03-S018, T02-S009]
- **SOP (Path B — in-Photoshop UXP assembler):** REST exports PNGs per layer → a **UXP** plugin
  `createDocument`/`createLayer({name,opacity,blendMode})` + `batchPlay` (wrapped in `executeAsModal`) assembles
  the layered PSD natively (lets the PS runtime handle text/CMYK that OSS can't). evidence: [T02-S007]
- **What to fix after**: regenerate the **composite/thumbnail** (ag-psd won't); for any text written via ag-psd,
  expect the "Update?" prompt; convert to CMYK/16-bit **in Photoshop** (ag-psd is RGB-8bit only). evidence: [T02-S011, T04-S019 (C7/C18)]
- **Fidelity caveats**: **RGB 8-bit only**, no CMYK/16-bit write, no auto-rasterization — you supply every pixel;
  build new automation on **UXP**, not deprecated ExtendScript/CEP. evidence: [T02-S011, T02-S007, T02-S008]

---

## 3. THE FIDELITY QA LOOP (how a pro VERIFIES visual consistency)

> **One-liner**: Treat the Figma frame's PNG export as **ground truth**, flatten the PSD to a composite, and
> *diff them* — by eye (Difference blend) and by number (pixel-diff) — then spot-check fonts, color, and effects
> before sign-off. **Trigger**: any PSD produced by §2. **Output**: a pass/fail with a documented diff.
> **Last_updated**: 2026-06-03. **Decay risk**: low. (Synthesis: the field has no published QA SOP, but the
> components are all first-party — this is the researcher's assembled loop, marked 推断 where noted.)

1. **Capture ground truth**: export the **exact same Figma frame** to **PNG at the same scale** as the PSD,
   **same color profile** (§1D). This is the reference image. evidence: [T03-S002]
2. **Flatten the PSD to a composite**: in Photoshop, `Image → Duplicate → Flatten` (or export the PSD to PNG) to
   get the PSD's rendered composite at the same px size. (推断 — standard PS step)
3. **Eyeball overlay diff (manual, in Photoshop)**: paste the ground-truth PNG as a top layer over the flattened
   PSD composite, set its blend mode to **Difference**. **Identical pixels turn black; any non-black region is a
   discrepancy** (Difference subtracts the two layers). Boost with a Levels/Curves layer to amplify faint diffs. evidence: [T03-S011]
4. **Quantitative pixel-diff (tooling)** — pick one:
   - **ImageMagick**: `magick compare -metric RMSE ground.png psd.png diff.png` (or `-metric AE -fuzz 2%` to count
     differing pixels above a tolerance). Outputs a number + a visual diff image. evidence: [T03-S007]
   - **pixelmatch** (Node/JS): raw-array diff; `threshold` 0–1 (default 0.1, lower = stricter); **antialias-aware**
     (`includeAA:false` by default ignores AA edges so you don't drown in sub-pixel noise). evidence: [T03-S008]
   - **Resemble.js** (browser) for a mismatch-% with ignore-antialiasing, or **pdiff** for *perceptual* (not naive)
     differences when you only care about human-visible drift. evidence: [T03-S009, T03-S010]
5. **Font-render check**: zoom to 100%+ on text blocks — confirm the **typeface is the real font (not substituted)**,
   and that **line-height/leading matches** (the AUTO-vs-120% trap: check total text-block height, not just one
   line). Re-type from Figma if a run drifted. evidence: [T04-S012, T04-S014 (C23), T02-S012]
6. **Color-profile check**: confirm the PSD's embedded profile (Image Resources, sRGB IEC61966-2.1) matches the
   Figma export profile; sample a few brand-color pixels with the eyedropper and compare hex to Figma. A profile
   mismatch shows as a *uniform* shift in the Difference overlay. evidence: [T04-S008, T04-S015 (C20/C21)]
7. **Effect-parity spot check**: walk the layers/groups you flagged in §1C — drop/inner shadows (offset, blur,
   **opacity** — remember Photopea's 100% reset), blend modes (esp. anything near the W3C-16 boundary or
   Plus-darker/lighter), and any background blur (should be rasterized). evidence: [T02-S004, T04-S016 (C13)]
8. **Sign-off criteria (suggested, 推断 — set per project)**:
   - **Pixel-faithful jobs**: RMSE under your threshold AND Difference overlay essentially black except known
     rasterization seams; fonts correct; color hex matches. → PASS.
   - **Editable jobs**: above + "Update?" prompt resolved + every flagged blend mode/effect verified live. → PASS.
   - Any *uniform* color shift → re-check profile (§6). Any *text-block height* drift → re-check line-height (§5).
   - If diffs are structural (vector split, missing blur), fix in PS or re-do pre-flight — don't sign off.

> **QA verification method in one line**: export the Figma frame to PNG as ground truth → overlay it on the
> flattened PSD with **Difference** blend (black = match) AND run a pixel-diff (ImageMagick RMSE / pixelmatch) →
> then font + color-profile + effect spot-checks → sign off against a per-project threshold.

---

## 4. BEGINNER SOP vs SENIOR PATH (incl. convert-vs-rebuild)

### 4A. Minimum-viable beginner SOP (get *a* usable PSD, fast)
1. Open the `.fig` in **Photopea** (or run an exporter plugin).
2. Load your fonts (TTF/OTF) first.
3. `File → Save as PSD`.
4. Open in Photoshop, click through any "Update?" prompt.
That's it — ~5–15 min, accepts vector-raster + flattened components. evidence: [T03-S006, T02-S012]

### 4B. Senior path — differences (skip / optimize / add)
- **skip**: seniors **skip chasing "perfect editability"** and skip tools promising it (Magicul/Codia "100% pixel
  perfect" are unverified vendor claims). They pick the *acceptable loss* immediately instead of testing five tools. evidence: [T02-S019, T02-S020, T02-S022]
- **skip**: skip exporting at 1×; always go @2x–4x and downscale in PS. evidence: [T04-S027]
- **optimize**: seniors do the **§1 pre-flight on a duplicate** (instances detached, line-height resolved, P3→sRGB
  converted, blend modes flattened) — this single discipline does more for fidelity than any tool choice. evidence: [T04-S010, T04-S008, T04-S016]
- **optimize**: route **per-asset** — vector logo → SVG Place (2d); whole flat screen → Photopea (2b); print → CMYK
  convert in PS after; bulk → REST+ag-psd (2f). One file may use 2–3 routes. evidence: [T02-S023, T02-S011]
- **add**: seniors **run the §3 QA diff loop** (Difference overlay + pixel-diff) instead of eyeballing once. evidence: [T03-S011, T03-S008]
- **add**: seniors **decide convert-vs-rebuild before touching a converter** (below).

### 4C. Convert-vs-rebuild heuristic (the senior judgment call)
- **CONVERT** when: the Figma file is **clean and current** (well-named layers, simple shapes, web-safe blend
  modes, mostly raster/Smart-Object-able content) and you need a **pixel-faithful** deliverable or asset extraction.
  Conversion + cleanup beats rebuilding here. evidence: [T03-S017]
- **REBUILD from scratch in Photoshop** when **any** of: (1) you need **true editable, parity-faithful** text AND
  vector AND effects (no tool delivers all three — C7/C13); (2) the design is **effect-heavy / blend-heavy /
  background-blur-heavy** so most of it would rasterize anyway; (3) you need **CMYK/16-bit print** (no OSS write
  path; Figma is RGB-only); (4) the file is **chaotic** — "if a file is chaotic it can take longer to untangle than
  to rebuild." Always **recreate type layers**, never paste rasterized text. evidence: [T03-S017, T04-S019 (C7/C18), T02-S011]
- **One-line rule**: *Convert when the file is clean and you only need it to **look** right; rebuild when you need
  it to **be** right (editable text + vector + CMYK) or when the source is messier than a fresh build.*

### 4D. Per-method time / fidelity tradeoff (推断 synthesis from Track 02 decay/effort signals)
| Method | Typical time (single frame) | Editability kept | Visual fidelity ceiling | Best for |
|--------|----------------------------|------------------|-------------------------|----------|
| 2(b) Photopea | 5–15 min | layers + (re-rendered) text; vectors raster | high (raster) | fast pixel-faithful |
| 2(a) Plugin | 5–20 min | best-effort text/layers | medium–high | in-Figma, offline |
| 2(d) SVG→SO | 2–10 min/asset | full vector (via AI) | high (vector) | single icon/logo |
| 2(e) PDF→AI→PS | 20–60 min | vector, text outlined | high (vector) | vector-heavy frame |
| 2(c) PNG@Nx | 15 min–hours (per-layer) | none (raster) | high (raster) | asset lib / AE |
| 2(f) REST+ag-psd | hours setup, then bulk | none auto (you render) | medium (RGB-8bit) | CI / many files |

---

## 5. RECENT WORKFLOW CHANGES (last ~12 months)

> Mandatory time-anchored section. Each item: change → trigger event → effect on the SOP.

- **2024-01 — Dev Mode went paid (free beta ended).** Dev Mode was free in open beta through end-2023; from Jan 2024
  it requires a **paid seat** (~$12–35/seat/mo by plan). **Effect on SOP**: the convenient "Export all assets in
  Dev Mode" batch path (used in 2c) now sits behind a paid seat — beginners on free seats fall back to manual
  per-object Export settings in Design mode. Trigger: Figma pricing change. evidence: [T03-S015, T03-S004]
- **2024-06 (Config 2024) — UI3, Figma AI, Slides, Visual Search.** The Figma UI was redesigned (UI3: component-
  centered panels, new icons) and Figma AI + Visual Search shipped (beta). **Effect on SOP**: export/inspect panels
  moved (the §1E/§2 export steps are unchanged in function but live in a new UI); no new PSD export path was added.
  Trigger: product launch. evidence: [T03-S012]
- **2023-12 → 2024 — Adobe–Figma merger collapse, fully settled.** The $20 B merger was terminated 2023-12-18 (EC +
  UK CMA blockers); Figma paid Adobe the **$1 B break-up fee in early 2024**. **No joint Photoshop↔Figma technical
  roadmap was ever announced.** **Effect on SOP**: confirms the **structural gap is permanent** — no imminent
  first-party Figma→PSD path; the third-party/bridge SOPs (§2) remain the only options indefinitely. Trigger:
  M&A/regulatory event. evidence: [T03-S013, T03-S014, T02-S024]
- **2025-04 / 2025-07 — Figma confidential IPO filing → public listing.** Figma filed confidentially (Apr 2025) and
  IPO'd (mid-2025). **Effect on SOP**: none on the conversion mechanics, but Figma is now an independent public
  company with **zero incentive to build a Photoshop bridge** — reinforces "no first-party PSD export coming."
  Trigger: corporate event. evidence: [T03-S014]
- **Tooling: ag-psd actively maintained (v30.x, npm v30.1.1 @ 2026-04-10 per Track 01).** Recent work
  (v30.0.0 `useRawData`, v30.0.1 16-bit handling) is on the **READ** path; the **write limits are unchanged**
  (RGB-only, 8-bit, no auto-redraw). **Effect on SOP**: the §2(f) caveats still hold; no new write capability to
  exploit. Trigger: library release. evidence: [T03-S018, T02-S010, T01-S003 (reuse)]
- **Stable baseline (no change in ~12 mo):** Figma's export surface (PNG/JPG/SVG/PDF, no PSD), Photopea's `.fig`→PSD
  flow, the SVG/PDF→PS bridges, and the rendering-gap facts (blend/line-height/color/alpha) are **unchanged** —
  this is a legitimately steady core. Decay risk on the §2 SOP mechanics: **low**; on the §5 tooling/pricing facts: **medium**. evidence: [T02-S001, T03-S006, T04-S011]

---

## 6. 総覧 (Overview by decay risk)

### High decay (12-month-class) — 0
*(None — there is no LLM/model-driven step in this pipeline; the volatility is in pricing/corporate events, not the SOP mechanics.)*

### Medium decay — 2
| Workflow | Trigger | Output | Last_updated | 资深差异 (key) |
|----------|---------|--------|--------------|----------------|
| 2(a) In-Figma plugin → PSD | Want layered PSD, stay in Figma / offline | Layered PSD, best-effort text | 2026-06-03 | skip tool-hunting; add: resolve "Update?" + verify effects |
| 2(b) Photopea `.fig`→PSD | Fast free pixel-faithful PSD | Layered PSD (vectors raster) | 2026-06-03 | optimize: load fonts first; add: re-merge split vectors, reset shadow opacity |

### Low decay — 4 + pre-flight + QA
| Workflow | Trigger | Output | Last_updated | 资深差异 (key) |
|----------|---------|--------|--------------|----------------|
| §1 Pre-flight prep in Figma | About to convert | Conversion-ready duplicate | 2026-06-03 | optimize: detach/flatten/resolve-line-height/P3→sRGB on a copy |
| 2(c) Layers→PS reassemble | Per-layer raster needed (asset lib/AE) | Flat layered PSD | 2026-06-03 | optimize: @2x–4x + downscale in PS; add: Place not Open |
| 2(d) SVG→Place Embedded | Single vector asset | Vector Smart Object | 2026-06-03 | add: per-sub-element SVG for multi-layer; skip File→Open |
| 2(e) PDF→AI→PS | Vector-heavy, offline, outlined text OK | Vector Smart Object | 2026-06-03 | add: ungroup/unclip in AI; re-type text if needed |
| 2(f) REST+ag-psd / UXP | Bulk / CI | Programmatic PSDs | 2026-06-03 | add: render every bitmap + composite; skip ExtendScript→use UXP |
| §3 Fidelity QA loop | Any PSD produced | Pass/fail + diff | 2026-06-03 | add: Difference-overlay + pixel-diff, not eyeball-once |

---

## 7. Phase 2 提炼提示

**反复出现 ≥ 3 个 workflow 都包含的步骤 (候选 playbook 通则):**
- **"Resolve to absolute values before export"** — appears in §1 (line-height→px, P3→sRGB convert), 2(a), 2(b),
  2(f): every numeric/color/text property must be pinned to a PSD-expressible absolute *in Figma first*, because
  the converter won't resolve units, profiles, or AUTO for you. → playbook: *"If a property is tool-relative
  (AUTO line-height, P3 color, %/em tracking, live blend mode), bake it to an absolute before writing the PSD."* evidence: [T04-S010, T04-S008, T04-S016]
- **"Rasterize anything without a PSD structural equivalent"** — appears in §1C, 2(b), 2(c), and the convert-vs-
  rebuild call: blend modes outside the W3C 16, background blur, pass-through groups with non-normal children,
  open-path vectors → flatten to pixels. → playbook: *"At each node: live PSD construct or pixels? No equivalent → rasterize; fidelity over editability."* evidence: [T04-S011, T04-S001 (C12/C13)]
- **"Place Embedded, never File→Open"** — appears in 2(c), 2(d), 2(e): SVG/AI/PDF assets enter PS as Smart Objects
  via Place; Open rasterizes/flattens and kills vector. → playbook: *"Vector/PDF/AI into Photoshop = File→Place Embedded, always."* evidence: [T02-S023]
- **"Ground-truth PNG + diff"** — the QA spine (§3) and implied in every senior path. → playbook: *"Verify by
  diffing the PSD composite against the Figma PNG (Difference blend + pixel-diff), not by eyeballing."* evidence: [T03-S011, T03-S008]

**入门 SOP 和资深路径之间最大的差距 (候选心智模型):**
- Beginner SOP = ~4 steps (open→fonts→save→open). Senior path is *barely shorter in steps* but adds an entire
  **pre-flight stage (§1) and a QA stage (§3)** the beginner skips. → mental model candidate: **"In Figma→PSD, the
  expert's edge is not faster execution but front-loaded preparation + back-loaded verification — the conversion
  itself is the trivial middle."** The senior spends 80% of effort *outside* the converter. evidence: [T04-S010, T03-S011]
- The convert-vs-rebuild judgment is itself the senior mental model: **"know when NOT to convert."** Beginners
  assume a tool exists to do it; seniors know the tool's ceiling and rebuild when the requirement exceeds it. evidence: [T03-S017, T04-S019]

**近期工作流变化的根本原因 (触发事件类型分布):**
- 0 by new model / 0 by new conversion tool / **3 by corporate-or-pricing events** (Dev Mode paywall 2024-01,
  Adobe–Figma collapse + $1B fee 2024, Figma IPO 2025) / 1 by product launch (Config 2024 UI3) / 1 by library
  release (ag-psd v30, read-side only). → **Main driver = corporate/structural, NOT technical.** The conversion
  *mechanics* are stable; what changes is access (paywall) and the permanence of the gap (no Adobe bridge ever).
  This is the opposite of LLM-era skills. evidence: [T03-S015, T03-S013, T03-S014, T03-S012]

**冷僻 / 信号薄弱 (Phase 2.8 诚实边界):**
- **Workflow count ≥ 4? YES** (6 method SOPs + pre-flight + QA = 8 retained). Not a cold-protocol trigger.
- **一手 (first-hand) source ≥ 50%? BORDERLINE.** Of 18 new T03 sources: ~6 verified_primary (Photopea tut, Figma
  blog ×2, pixelmatch GH) + ~6 surrogate_primary vendor docs (Figma Help ×4, Adobe Help, ImageMagick, npm) =
  ~67% first-party-in-substance; the rest secondary. **But heavy reliance on cross-track reuse** (T02/T04) for the
  load-bearing fidelity facts — flag that the *SOPs themselves* are researcher-assembled (推断), not published
  procedures. **There is no first-party "Figma→PSD SOP" anywhere on the web** — the workflow knowledge does not
  exist as codified procedure; it had to be synthesized from tool behavior + format gaps. THIS IS THE KEY GAP.
- **资深差异点 ≥ 2 per workflow? YES** for all 8 (skip/optimize/add filled).
- **近期变化 ≥ 60% filled? YES** (§5 covers all + an explicit stable-baseline note).
- **The QA loop sign-off thresholds are 推断** — no published numeric fidelity standard exists for this domain
  (corroborates Track 02's "no neutral independent benchmark exists" gap). Users must set their own thresholds.
- **Decay shape is unusual**: not 12-month-class (no model dependency), but a structural-event tail (pricing,
  corporate). Recommend Phase 2.8 wording: *"workflow mechanics are stable (low decay); the surrounding facts
  (Dev Mode pricing, Figma corporate posture, plugin availability) shift on a ~12-mo cadence — re-check §5 + Track
  02 plugin list annually, not the core SOPs."*
