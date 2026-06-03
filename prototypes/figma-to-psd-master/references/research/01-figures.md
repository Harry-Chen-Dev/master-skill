# Track 01 — Figures: Figma → PSD Conversion (Skill: figma-to-psd-master)

> Research verified & deepened: 2026-06-03 (Opus pass over prior Sonnet draft).
> **COLD-FIELD ADVISORY IN EFFECT.** This is a tooling-heavy, personality-thin domain. "Figures" here are tool/library maintainers, plugin/SaaS builders, and one cross-tool-fidelity writer — not a visible thought-leadership community. There is **no podcast circuit, no conference talk corpus, and almost no long-form interview material** specific to Figma↔PSD conversion. Treat this honestly: see "Cold-Field Protocol" at the end. Phase 2 MUST weight Track 04 (specs) + Track 02 (tool behavior) over figure philosophies.

---

## Source Manifest

| source_id | url | bucket | last_checked | author/host | one-line note |
|-----------|-----|--------|--------------|-------------|---------------|
| T01-S001 | https://github.com/Agamnentzar/ag-psd | verified_primary | 2026-06-03 | Agamnentzar (GitHub) | ag-psd JS lib README; documents PSD write limits (RGB-only, no 16-bit, no PSB, text bitmap warning) |
| T01-S002 | https://github.com/Agamnentzar/ag-psd/blob/master/README_PSD.md | verified_primary | 2026-06-03 | Agamnentzar | Psd object structure; alpha pre-mult warning; composite/layer canvas NOT auto-generated |
| T01-S003 | https://registry.npmjs.org/ag-psd | verified_primary | 2026-06-03 | npm registry | author={name:"Agamnentzar"}, maintainer email agamnentzar@gmail.com, MIT, **v30.1.1 @ 2026-04-10**, first 2015-12-25 |
| T01-S004 | https://blog.photopea.com/creating-photopea.html | verified_primary | 2026-06-03 | Ivan Kutskir | "Creating Photopea"; "remove borders between programs (support all existing file formats…)" philosophy |
| T01-S005 | https://www.photopea.com/tuts/convert-figma-to-psd/ | verified_primary | 2026-06-03 | Photopea / Kutskir | Official Figma→PSD tutorial; only documented caveat = load fonts manually; "layer structure is preserved" |
| T01-S006 | https://blog.photopea.com/photopea-4-6-open-figma-files.html | verified_primary | 2026-06-03 | Ivan Kutskir | Photopea 4.6 .FIG open (Jan 2020); "browse a whole design structure… save every design as a PSD"; **no limits stated** |
| T01-S007 | https://github.com/psd-tools/psd-tools | verified_primary | 2026-06-03 | psd-tools org | Python PSD lib repo; read-focused; documents unsupported layer types |
| T01-S008 | https://psd-tools.readthedocs.io/en/latest/ | verified_primary | 2026-06-03 | psd-tools (Korobov, Yamaguchi) | Docs: NOT supported — type-layer/shape/smart-object editing, adjustment-layer & many effect composition, font rendering |
| T01-S009 | https://pypi.org/pypi/psd-tools/json | verified_primary | 2026-06-03 | PyPI | authors=Korobov<kmike84@gmail.com> + Yamaguchi<KotaYamaguchi1984@gmail.com>; **v1.17.1 @ 2026-05-26** (actively shipping) |
| T01-S010 | https://bjango.com/articles/ | verified_primary | 2026-06-03 | Marc Edwards / Bjango | Full article index; the single richest cross-tool fidelity corpus (blur/shadow/blend/colour/opacity/SVG) |
| T01-S011 | https://bjango.com/articles/blurradiuscomparison/ | verified_primary | 2026-06-03 | Marc Edwards | Blur scale-factor table (CSS=1.0, Figma=1.136364, PS=0.490196, Sketch=0.349650, SVG-Chrome=0.406504); 50px PS→115.9px Figma |
| T01-S012 | https://bjango.com/articles/matchingdropshadows/ | verified_primary | 2026-06-03 | Marc Edwards | Drop-shadow blur conversion: iOS=2×CSS, Android=1/√3 (legacy Skia); offset+colour identical, only blur differs |
| T01-S013 | https://bjango.com/articles/passthroughblending/ | verified_primary | 2026-06-03 | Marc Edwards | "Pass-through… not really a blending mode at all, but a change in blending behaviour for groups"; PS has no pass-through mode |
| T01-S014 | https://bjango.com/articles/colourmanagementissues/ | verified_primary | 2026-06-03 | Marc Edwards | "Figma and XD are not colour managed, so there is no way to assign or convert profiles for documents." |
| T01-S015 | https://bjango.com/articles/opacityprecision/ | verified_primary | 2026-06-03 | Marc Edwards | 0-100 opacity can't reach 154 of 256 8-bit values; shadows 5-20% = ~15 steps; Figma 2-decimals = 10,001 steps |
| T01-S016 | https://bjango.com/articles/svgpassthroughprecision/ | verified_primary | 2026-06-03 | Marc Edwards | SVG round-trip precision: Figma 4 dp (converts rects→paths), Sketch 7 dp, Illustrator 5 dp, XD/Affinity 3 dp |
| T01-S017 | https://bjango.com/articles/designsystemcolourspace/ | verified_primary | 2026-06-03 | Marc Edwards | "Design systems need a colour space" (Mar 2025) — sRGB vs P3 in tokens; most recent long-form |
| T01-S018 | https://sites.google.com/view/kyamagu/ | secondary | 2026-06-03 | Kota Yamaguchi | Personal site; Principal Research Scientist CyberAgent; layout gen / typography / vector graphics |
| T01-S019 | https://github.com/kmike | secondary | 2026-06-03 | Mikhail Korobov | psd-tools co-author; broad Python OSS (Scrapy, pymorphy2, eli5); @zytedata |
| T01-S020 | https://www.hypermatic.com/articles/building-a-figma-converter-plugin/ | secondary | 2026-06-03 | Adam Brock / Hypermatic | "a thousand mini mountains"; image-crop emulation 3-4 days; **Sketch-focused, not PSD** |
| T01-S021 | https://www.hypermatic.com/articles/the-startup-formerly-known-as-figmatic/ | secondary | 2026-06-03 | Adam Brock / Hypermatic | Founder story; left full-time job 2019 to build Figma plugins |
| T01-S022 | https://docs.hypermatic.com/convertify/export/adobe-photoshop | verified_primary | 2026-06-03 | Adam Brock / Hypermatic | Convertify PSD export docs; **zero limitations documented** (transparency gap) |
| T01-S023 | https://magicul.io/blog/the-challenges-of-manual-figma-to-psd-conversion-and-how-to-overcome-them | verified_primary | 2026-06-03 | Kevin Goedecke / Magicul | "Figma doesn't let you send your designs right to PSD"; PNG/SVG intermediate "loses… layers"; marketing-framed |
| T01-S024 | https://divriots.com/blog/converting-psd-to-figma-the-ultimate-guide-to-importing-photoshop-files/ | verified_primary | 2026-06-03 | Ardena Gonzalez / divRIOTS | psd.to.design guide; layer effects + pixel masks "coming soon"; smart objects → components or flattened |
| T01-S025 | https://www.adobe.com/devnet-apps/photoshop/fileformatashtml/ | verified_primary | 2026-06-03 | Adobe | Official PSD/PSB file format spec; authoritative ground truth (confirmed still live) |
| T01-S026 | https://github.com/gco/xee/blob/master/XeePhotoshopLoader.m | verified_primary | 2026-06-03 | Dag Ågren (gco) | The "PSD is not my favourite file format" rant comment — canonical developer-frustration artifact |
| T01-S027 | https://news.ycombinator.com/item?id=26762419 | reference | 2026-06-03 | Hacker News | Community thread on the Xee comment; "ball of hacks" consensus |
| T01-S028 | https://jnack.com/blog/ | verified_primary | 2026-06-03 | John Nack | Ex-Adobe PS PM blog; PSD "organic growth" admission (orig blogs.adobe.com post now unreliable, see note) |
| T01-S029 | https://www.loc.gov/preservation/digital/formats/fdd/fdd000523.shtml | verified_primary | 2026-06-03 | Library of Congress | Neutral PSD format sustainability assessment; institutional ground-truth on format characteristics |
| T01-S030 | https://github.com/meltingice/psd.js | verified_primary | 2026-06-03 | Ryan LeFevre (meltingice) | First major JS PSD parser; **abandoned (last release 2021, ~172 open issues)** — historical only |
| T01-S031 | https://codia.ai/psd-to-figma | secondary | 2026-06-03 | Codia AI (vendor) | AI PSD↔Figma converter; "every layer stays editable, accurate, perfectly preserved" — marketing claim, no tech transparency |
| T01-S032 | https://en.wikipedia.org/wiki/Photopea | reference | 2026-06-03 | Wikipedia | Photopea overview; one-developer, 100k+ LOC JS |
| T01-S033 | https://scholar.google.com/citations?user=mYDpPnYAAAAJ | reference | 2026-06-03 | Google Scholar | Yamaguchi publications incl. LayerD (ICCV 2025) — raster→layer decomposition |

---

## 総覧 (Overview — by domain influence on Figma↔PSD fidelity)

| # | Name | Core Identity | One-line Contribution | Read/Watch | Sources |
|---|------|--------------|----------------------|-----------|---------|
| 1 | **Marc Edwards** | Founder, Bjango | **THE** cross-tool fidelity authority: hard-number tables for blur, drop-shadow, blend, colour-management, opacity, SVG precision | bjango.com/articles/ 📖 | S010–S017 |
| 2 | **Ivan Kutskir** | Founder/sole dev, Photopea | Only web app that natively opens .FIG AND writes layered PSD; deepest dual-format *implementation* | blog + tutorial 📖🎙️ | S004, S005, S006 |
| 3 | **"Agamnentzar"** | Pseudonymous maintainer, ag-psd | JS PSD read/write lib under most Figma→PSD plugins; documents write-limits precisely | GitHub README 📖 | S001, S002, S003 |
| 4 | **Kota Yamaguchi** | Principal Research Scientist, CyberAgent AI Lab | psd-tools co-author + ML researcher on raster→layer decomposition (LayerD, ICCV 2025) | docs, site, Scholar 📖 | S008, S009, S018, S033 |
| 5 | **Mikhail Korobov** | Python OSS dev (@zytedata) | psd-tools co-author; format-parsing rigor from broad Python-OSS background | GitHub, docs 📖 | S008, S009, S019 |
| 6 | **Adam Brock** | Founder/CEO, Hypermatic | Built Convertify; named conversion complexity "a thousand mini mountains" | hypermatic articles 📖 | S020, S021, S022 |
| 7 | **Kevin Goedecke** | Founder/CEO, Magicul | Clearest public enumeration of Figma→PSD pain points (vendor-framed) | magicul blog 📖 | S023 |
| 8 | **Ardena Gonzalez** | Content/DX, divRIOTS | Wrote the most detailed PSD↔Figma feature-mapping guide (psd.to.design) | divriots blog 📖 | S024 |
| 9 | **Dag Ågren** | Indie macOS dev (Panic) | Author of the canonical "PSD is not a good format" code rant | XeePhotoshopLoader.m 📖 | S026, S027 |
| 10 | **John Nack** | Ex-Adobe PS Senior PM | The one Adobe voice admitting PSD's "organic growth" messiness | jnack.com 📖🎙️ | S028 |
| 11 | **Ryan LeFevre** | Software engineer | Creator of psd.js — first JS PSD parser; now abandoned (historical) | github 📖 | S030 |
| 12 | *Codia AI* (vendor) | AI design-to-code company | High-volume PSD↔Figma converter; strong marketing claims, no tech transparency | codia.ai 📖 | S031 |

**Real figures with deep, attributable, voiced output: ~2 (Marc Edwards, Ivan Kutskir).** Another ~3 are critical *engineering* authorities whose "voice" is README/docs/code, not interviews (Agamnentzar, Yamaguchi, Korobov). The rest are vendor-bloggers or historical-context figures. This is the honest shape of the field.

---

## Figure Profiles

---

### 1. Marc Edwards  ★ DEEPENED — highest-value figure for Phase 2

- **One-liner**: Bjango founder and the single most rigorous public source on *why a value in Figma renders differently from the same value in Photoshop* — he publishes hard-number conversion tables for blur radius, drop shadows, blend modes, colour management, opacity precision, and SVG round-tripping. evidence: [T01-S010, T01-S011, T01-S015]
- **核心身份**: Founder & designer, Bjango (Melbourne, Australia). Makes iStat Menus; built Skala (design tool, since shelved); maintains Bjango Actions (Photoshop pixel-fitting actions). Independent — not affiliated with Figma or Adobe, which is *why* his comparisons are credible.
- **代表作品**: The bjango.com/articles/ corpus (the de-facto reference for cross-tool visual differences); iStat Menus; Bjango Actions.
- **值得读/听/看**:
  - 📖 "Blur radius comparison" — https://bjango.com/articles/blurradiuscomparison/ — the scale-factor table + formula. **The** Phase-2 reference for matching a Photoshop Gaussian blur to a Figma blur.
  - 📖 "Matching drop shadows…" — https://bjango.com/articles/matchingdropshadows/ — blur-conversion factors across CSS/Android/iOS/Figma/Sketch with mathematical rationale.
  - 📖 "Opacity precision" — https://bjango.com/articles/opacityprecision/ — the 0-100 vs 0-255 quantization problem; directly explains banding/shadow-step loss on PSD round-trip.
  - 📖 "What is pass-through blending?" — https://bjango.com/articles/passthroughblending/ — the group-blending architecture difference between PS and Figma.
  - 📖 "Diagnosing common colour management issues" — https://bjango.com/articles/colourmanagementissues/ — Figma's lack of colour management.
  - 📖 "SVG passthrough precision" — https://bjango.com/articles/svgpassthroughprecision/ — coordinate-rounding loss per tool.
  - 🎙️ "In Depth Ep. 3: Design Tools" w/ Eli Schiff (2017) — older but the only substantial long-form interview; not conversion-specific.
  - 🎬 ⚠️ 无 conversion-specific conference talk found.
- **核心思想关键词**: blur-radius normalization (no universal standard), opacity quantization, pass-through ≠ blend mode, Figma-is-not-colour-managed, sRGB-vs-P3 default gap, coordinate-precision loss, "every tool rounds differently."
- **voice_samples**:
  - On blur (the load-bearing fidelity fact): "implementations vary so much that a blur in one app may be a completely different size to the other app." Concretely: a 50px Photoshop filter blur ≈ **115.9px** Figma background blur (factor 1.136364 / 0.490196). (source: T01-S011, 原话 + 推断 on derivation)
  - On colour management: "Figma and XD are not colour managed, so there is no way to assign or convert profiles for documents." And the sRGB-canvas workaround is "an app-wide setting just for the computer you're making the change on, so other people viewing the document may see different colours." (source: T01-S014, 原话)
  - On pass-through: "Pass-through is different. Pass-through alters how the layer tree is collapsed. It's not really a blending mode at all, but a change in blending behaviour for groups." (source: T01-S013, 原话)
  - On opacity: "opacity values in 8bit per channel images have a range of 0 to 255. A design tool that uses a 0 to 100 range for opacity can not access 154 of the actual possible values." (source: T01-S015, 原话)
- **sub_skill_candidate**: `true` — by far the most distillable figure: 20+ long-form technical articles, internally consistent mental model, directly load-bearing for the skill's fidelity dimension, active in 2025. Caveat: his "voice" is written-analytical, not conversational; voice_confidence = medium-high for the written register, low for spoken.
- **dual_role**: `"founder + technical writer/analyst"`
- **最近 12 个月动态**: "Design systems need a colour space" (Mar 2025). bjango.com active; YouTube channel active. The articles are periodically revised (the blur/shadow pieces have been updated as tools changed). evidence: [T01-S017]
- **争议/批评**: (1) His baseline lens is macOS/iOS + Sketch; some comparisons predate Figma feature changes — e.g. his colour-management critique is rooted in 2021-era Figma. (2) The blur/shadow factors are *visual-match approximations*, not Adobe-blessed math — treat as practitioner calibration, not spec. (3) He measures rendering, not the PSD byte format itself — pair with Track 04 spec sources.
- **来源**:
  - [Primary] https://bjango.com/articles/blurradiuscomparison/ (collected 2026-06-03)
  - [Primary] https://bjango.com/articles/opacityprecision/ (collected 2026-06-03)
  - [Primary] https://bjango.com/articles/passthroughblending/ (collected 2026-06-03)
- **可信度自评**: **high** — consistent long-form primary output, reproducible numbers, independent of both vendors, active in 2025. The richest single node in this track.

---

### 2. Ivan Kutskir

- **One-liner**: Created Photopea, the only web application that natively *opens* .FIG (Figma) files AND *writes* layered PSD — making him the only person with a shipping production implementation of both halves of the Figma↔PSD pipeline. evidence: [T01-S004, T01-S006]
- **核心身份**: Founder & sole developer, Photopea (photopea.com). Czech-based (Prague); a one-person business reportedly ~$1M+/yr on ads while keeping the editor free. Wrote an early open-source PSD-reader library (~2012) before Photopea.
- **代表作品**: Photopea (web editor with native PSD + .FIG support, ~100k+ LOC, solo); earlier OSS PSD parser.
- **值得读/听/看**:
  - 📖 "Creating Photopea" — https://blog.photopea.com/creating-photopea.html — his philosophy of format-universalism.
  - 📖 "Convert Figma to PSD" tutorial — https://www.photopea.com/tuts/convert-figma-to-psd/ — official workflow; the only documented caveat is manual font loading.
  - 📖 "Photopea 4.6 – Open Figma Files!" — https://blog.photopea.com/photopea-4-6-open-figma-files.html — the .FIG-import announcement (Jan 2020).
  - 🎙️ HN threads where he participates (e.g. id=29001723) — short but first-person.
  - 🎬 ⚠️ 无 long-form talk found.
- **核心思想关键词**: format parity over format invention, "remove borders between programs," editing accessible without cost, file-survivability if the tool dies, layer-structure preservation, font substitution as the named #1 gap.
- **voice_samples**:
  - Core philosophy: "make advanced editing accessible to everyone (in terms of cost and device requirements), remove borders between programs (support all existing file formats instead of inventing a new format)." (source: T01-S004, 原话)
  - On tool independence (why he supports legacy formats): "if it suddenly stops working, you should still have a chance to use your files somehow." (source: T01-S004, 原话)
  - On the origin: "The idea of creating an advanced image editor on my own seemed stupid, and making it a webapp seemed like a complete joke." (source: T01-S004, 原话)
  - On .FIG: users can "browse a whole design structure, each separate element, its style, etc." and "save every design as a PSD file." (source: T01-S006, 原话)
  - ⚠️ **No first-party catalog of conversion fidelity limits exists.** Kutskir documents capability, never limitation — the FIG announcement and the Figma→PSD tutorial both omit any "what is lost" section. His only stated caveat anywhere is "load your fonts manually." This is itself a finding: the deepest practitioner is silent on the gaps. (推断 from T01-S005, T01-S006)
- **sub_skill_candidate**: `true` (high-priority) BUT voice_confidence = **low** — production authority is unmatched, but his public output is feature announcements + short HN comments, not technical deep-dives. You can distill his *philosophy* but not a documented gap-list from him. Pair with Track 02 (observe Photopea behavior directly) to get the real limits.
- **dual_role**: `"founder + engineer"` (solo product + implementation)
- **最近 12 个月动态**: Photopea ships continuous updates; Kutskir active on r/photopea and the blog. evidence: [T01-S005]
- **争议/批评**: Photopea's blend-mode and colour rendering reportedly differ from Photoshop in edge cases (Color Dodge / Linear Light) per third-party users — Kutskir does not publicly acknowledge or catalog these. The "no documented limits" stance is a transparency criticism, not a capability one. evidence: [T01-S032]
- **来源**:
  - [Primary] https://blog.photopea.com/creating-photopea.html (collected 2026-06-03)
  - [Primary] https://www.photopea.com/tuts/convert-figma-to-psd/ (collected 2026-06-03)
  - [Reference] https://en.wikipedia.org/wiki/Photopea
- **可信度自评**: high for role/impact; **medium-low** for technical-gap depth — first-party output documents capability, not limits.

---

### 3. "Agamnentzar" (ag-psd maintainer)  ★ IDENTITY VERIFIED — correction to draft

- **One-liner**: The pseudonymous solo maintainer of **ag-psd**, the most widely-used JavaScript PSD read/write library and the technical substrate beneath most browser-based Figma→PSD plugins; the README is one of the few places PSD *write* limits are stated plainly. evidence: [T01-S001, T01-S003]
- **核心身份 / IDENTITY**: **No real name is exposed anywhere first-party.** Verified handle = `Agamnentzar` (GitHub, 363 followers, 20 repos); npm publisher account = `agamnentzar`, contact email `agamnentzar@gmail.com` (from the npm registry record). The handle is a fantasy/sci-fi-style alias; there is **no blog, no talk, no interview, no linked real identity**. This is a genuine pseudonym, not a research gap — I checked GitHub profile, npm registry JSON, and package.json. (Correction to the Sonnet draft, which left identity merely "unknown" and was unsure on activity.) evidence: [T01-S001, T01-S003]
- **代表作品**: ag-psd (TypeScript PSD read/write, 671★); psd-thumbnail-provider (Windows Explorer PSD previews, C++); ag-sockets.
- **值得读/听/看**:
  - 📖 ag-psd README — https://github.com/Agamnentzar/ag-psd — feature matrix + the write-limitation list.
  - 📖 README_PSD.md — https://github.com/Agamnentzar/ag-psd/blob/master/README_PSD.md — Psd object structure; alpha pre-mult and canvas-generation warnings.
  - 🎙️🎬 ⚠️ 无 / none exist — README/code is the entire corpus.
- **核心思想关键词**: RGB-only write constraint, no 16-bit / no PSB, no patterns/colour-palettes on write, text-layer bitmap must be regenerated (else Photoshop warns), composite canvas NOT auto-generated, alpha premultiplication corruption risk.
- **voice_samples** (all from README/docs — there is no spoken/long-form voice):
  - On write scope: ag-psd "Does not support writing any color modes other than RGB," "Does not support 16 bits per channel," "Does not support The Large Document Format (8BPB/PSB)," "Does not support patterns (or 'Pattern Overlay' layer effect)." (source: T01-S001, 原话)
  - On text (a key fidelity trap): writing a text layer "does not redraw bitmap data for the text layer, so files with updated/written text layers will result in a warning prompt when opening the file in Photoshop"; vertical orientation "may result in broken PSD file." (source: T01-S001, 原话)
  - On the burden it pushes downstream: "This library does NOT generate new composite canvas based on the layer data" and "does NOT generate new layer canvas based on layer settings" — i.e. any plugin built on ag-psd must render the composite itself, or PSDs open wrong. (source: T01-S002, 原话)
- **sub_skill_candidate**: `false` — indispensable technical authority, but a pseudonym with zero long-form material; you can mine the docs for a gap-list, not build a "thinking style."
- **最近 12 个月动态**: **Actively maintained — v30.1.1 published 2026-04-10 on npm** (first release 2015-12-25). MIT-licensed, no funding/sponsor field. (Correction: draft said "specific recent release dates not confirmed" — they are now confirmed recent.) evidence: [T01-S003]
- **争议/批评**: The library deliberately offloads composite/canvas regeneration to the caller — a notorious footgun for downstream plugins that forget to re-render after changing layer order or blend modes. Documented, but easy to miss. evidence: [T01-S002]
- **来源**:
  - [Primary] https://github.com/Agamnentzar/ag-psd
  - [Primary] https://github.com/Agamnentzar/ag-psd/blob/master/README_PSD.md
  - [Primary] https://registry.npmjs.org/ag-psd (author/maintainer/version metadata, collected 2026-06-03)
- **可信度自评**: high for technical content; identity confidence high *that it is an unrecoverable pseudonym*; voice = N/A.

---

### 4. Kota Yamaguchi  ★ ROLE & RECENT-WORK VERIFIED

- **One-liner**: Principal Research Scientist at CyberAgent AI Lab and co-author of **psd-tools** (Python); his ML research on decomposing flat designs back into editable layers (LayerD, ICCV 2025) is the academic mirror-image of the rasterize-then-reconstruct fidelity problem. evidence: [T01-S009, T01-S018, T01-S033]
- **核心身份**: Principal Research Scientist, CyberAgent (leading the research org); PhD Computer Science, Stony Brook 2014; Assistant Professor, Tohoku University 2014–2017; BE/MS University of Tokyo. X: @kotymg. (Note: the kyamagu.github.io page is dead; the live site is sites.google.com/view/kyamagu/ — correction to any github.io reference.) evidence: [T01-S018]
- **代表作品**: psd-tools (co-author, with Korobov); LayerD: Decomposing Raster Graphic Designs into Layers (ICCV 2025); LayoutDM (CVPR 2023); CanvasVAE (ICCV 2021).
- **值得读/听/看**:
  - 📖 psd-tools docs — https://psd-tools.readthedocs.io/en/latest/ — the canonical unsupported-features list.
  - 📖 Personal site — https://sites.google.com/view/kyamagu/ — research index.
  - 📖 Google Scholar — https://scholar.google.com/citations?user=mYDpPnYAAAAJ — incl. LayerD (raster→layer).
  - 🎙️🎬 ⚠️ 无 talk/interview on PSD tooling specifically.
- **核心思想关键词**: raster→layer decomposition, layout generation, typography/font analysis, design completion, vector-vs-raster boundary, "PSD spec is incomplete — inspect the low-level structure."
- **voice_samples**:
  - From psd-tools docs (the spec-incompleteness stance the skill needs): psd-tools does **not** support "Editing of various layers such as type layers, shape layers, smart objects," "Composition of adjustment layers," "Composition of many layer effects," or "Font rendering." (source: T01-S008, 原话)
  - ⚠️ No personal long-form voice on Figma→PSD specifically; his verbal register is academic-paper, which belongs in Track 04. (推断)
- **sub_skill_candidate**: `false` — dual academic+engineering role, but his distillable output is research, not conversion-workflow philosophy. Route the *papers* to Track 04. (Meets the iter-4 dual-role bar nominally, but lacks a practice-focused long talk.)
- **dual_role**: `"academic + engineering"`
- **最近 12 个月动态**: Active at CyberAgent; **LayerD published at ICCV 2025** (raster-design → editable layers — directly relevant to reconstructing layers from flattened Figma exports). psd-tools shipping fast (see Korobov entry). evidence: [T01-S033, T01-S009]
- **争议/批评**: psd-tools is read/inspect-oriented; it explicitly won't render fonts, compose most effects, or edit type layers — so it is a *decoder/validator*, not a converter. Don't expect production PSD-write fidelity from it. evidence: [T01-S008]
- **来源**:
  - [Primary] https://sites.google.com/view/kyamagu/
  - [Primary] https://psd-tools.readthedocs.io/en/latest/
  - [Reference] https://scholar.google.com/citations?user=mYDpPnYAAAAJ
- **可信度自评**: high for role/contribution; medium for direct relevance to conversion *voice* (his relevance is the library + a tangential research line).

---

### 5. Mikhail Korobov

- **One-liner**: Russian Python OSS developer who co-created psd-tools and is, by release cadence, its **active maintainer** today — bringing format-parsing discipline from a broad Python ecosystem background (Scrapy, pymorphy2). evidence: [T01-S009, T01-S019]
- **核心身份**: Developer, @zytedata (ex-Scrapinghub); prolific Python OSS contributor; psd-tools org member.
- **代表作品**: psd-tools (co-author + ongoing releases); Scrapy ecosystem; pymorphy2 (Russian/Ukrainian morphology); eli5 (ML explainability).
- **值得读/听/看**:
  - 📖 GitHub — https://github.com/kmike — the breadth of his parsing/data-engineering work.
  - 📖 psd-tools repo — https://github.com/psd-tools/psd-tools — co-author of record.
  - 🎙️🎬 ⚠️ 无 PSD-specific talk.
- **核心思想关键词**: robust binary-format parsing, Python OSS rigor, low-level data inspection, data engineering.
- **voice_samples**: ⚠️ 暂未找到 ≥ 30 字直接原话片段 on PSD specifically. His "voice" is commit history and changelogs.
- **sub_skill_candidate**: `false` — PSD is one of many projects; no sustained design-tool discourse.
- **最近 12 个月动态**: **psd-tools is actively shipping — v1.17.1 on 2026-05-26, with v1.14.3 → v1.17.1 all released April–May 2026.** (Major correction: the Sonnet draft said "releases through 2024." The library is one of the most actively maintained nodes in this whole track.) evidence: [T01-S009]
- **争议/批评**: None specific. His role reads as the primary ongoing engineering hand on psd-tools (Yamaguchi being the more research-facing co-author).
- **来源**:
  - [Primary] https://github.com/kmike
  - [Primary] https://pypi.org/pypi/psd-tools/json (authorship + release dates, collected 2026-06-03)
  - [Reference] https://psd-tools.readthedocs.io/en/latest/
- **可信度自评**: medium — confirmed co-author + active maintainer; minimal first-person output on the topic.

---

### 6. Adam Brock  ★ SCOPE CORRECTED

- **One-liner**: Founder/CEO of Hypermatic (formerly Figmatic); built **Convertify**, a bidirectional Figma↔Sketch/XD/PSD/AE/InDesign converter, and described conversion engineering as "a thousand mini mountains." evidence: [T01-S020, T01-S021]
- **核心身份**: Founder & CEO, Hypermatic; Australian developer; left a full-time dev job in 2019 to build Figma plugins.
- **代表作品**: Convertify (multi-direction converter incl. PSD); TinyImage (Figma compression w/ colour-profile support).
- **值得读/听/看**:
  - 📖 "Building a Figma converter plugin" — https://www.hypermatic.com/articles/building-a-figma-converter-plugin/ — the "mini mountains" framing + image-crop emulation war-story.
  - 📖 "The Startup Formerly Known as Figmatic" — https://www.hypermatic.com/articles/the-startup-formerly-known-as-figmatic/ — founder story.
  - 📖 Convertify PSD export docs — https://docs.hypermatic.com/convertify/export/adobe-photoshop.
  - 🎙️🎬 ⚠️ 无.
- **核心思想关键词**: visual emulation of unsupported features, "mini mountains" of per-feature incompatibility, non-destructive crop emulation via masks, converter architecture.
- **voice_samples**:
  - On complexity: building a converter is "something like a thousand mini mountains that you need to climb and then go back to basecamp and do it again." (source: T01-S020, 原话)
  - On emulation (the mental model for lossy mapping): a Figma image crop "had to be 'visually emulated' by creating a mask layer" because Sketch lacks non-destructive crops — ~3-4 days for that one feature. (source: T01-S020, 原话)
  - ⚠️ **Correction to draft**: the flagship "mini mountains" article is **Sketch-focused, not PSD** — Sketch was the launch target ("the most widespread tool besides Figma"). Convertify gained PSD export later. There is **no PSD-specific deep-dive** from Brock; the draft slightly over-attributed PSD specificity. (source: T01-S020, 推断/correction)
- **sub_skill_candidate**: `false` — real practitioner, but writing is business-narrative, not a technical PSD gap-list; no long-form interview.
- **最近 12 个月动态**: Hypermatic active; Convertify reached v11 (May 2026) adding font replacement on PSD import; TinyImage active with colour-profile features. evidence: [T01-S022]
- **争议/批评**: Convertify's PSD-export docs document **zero limitations** — no public "what is lost" list, which undermines trust for precision workflows. (Same "hide your limits" pattern as Photopea/Codia.) evidence: [T01-S022]
- **来源**:
  - [Primary] https://www.hypermatic.com/articles/building-a-figma-converter-plugin/
  - [Primary] https://www.hypermatic.com/articles/the-startup-formerly-known-as-figmatic/
  - [Primary] https://docs.hypermatic.com/convertify/export/adobe-photoshop
- **可信度自评**: medium — confirmed practitioner; PSD-specific technical depth is thin and commercially framed.

---

### 7. Kevin Goedecke

- **One-liner**: Founder/CEO of Magicul; wrote the clearest *public* enumeration of why manual Figma→PSD conversion is painful — though the article is explicitly a problem→Magicul-solution funnel. evidence: [T01-S023]
- **核心身份**: Founder/CEO, Magicul (design-file converter SaaS); also CEO of SlideSpeak (AI/PPT). Product-focused software engineer.
- **代表作品**: Magicul converter (XD/Figma/Sketch/PSD/PDF, bidirectional); the "Challenges of Manual Figma to PSD Conversion" blog.
- **值得读/听/看**:
  - 📖 "The Challenges of Manual Figma to PSD Conversion…" — https://magicul.io/blog/the-challenges-of-manual-figma-to-psd-conversion-and-how-to-overcome-them.
  - 🎙️🎬 ⚠️ 无.
- **核心思想关键词**: no direct export path, data/layer loss through PNG/SVG intermediates, manual per-component export, sizing/colour/font drift.
- **voice_samples**:
  - On the core gap: "Figma doesn't let you send your designs right to PSD. What most people do is save their designs as a PNG or SVG first." (source: T01-S023, 原话)
  - On loss: "doing it this way can mean your design loses some stuff along the way, like layers." (source: T01-S023, 原话)
- **sub_skill_candidate**: `false` — vendor POV; useful as named pain-point documentation, not neutral analysis.
- **最近 12 个月动态**: Magicul converter operational in 2026; Goedecke's attention partly shifted to SlideSpeak. evidence: [T01-S023]
- **争议/批评**: Explicitly marketing-oriented — classic problem-solution framing, favorable UI comparisons vs Photopea, FAQ that reinforces Magicul. Use the pain-point *list*, discount the conclusions. evidence: [T01-S023]
- **来源**:
  - [Primary] https://magicul.io/blog/the-challenges-of-manual-figma-to-psd-conversion-and-how-to-overcome-them
  - [Reference] (Magicul vs Photopea comparison posts on the same blog)
- **可信度自评**: medium — confirmed role; content commercially motivated.

---

### 8. Ardena Gonzalez (divRIOTS / psd.to.design)  ★ NEW — promoted from a passing mention in the draft

- **One-liner**: Author at divRIOTS (makers of the popular **psd.to.design** plugin) of the most detailed public feature-by-feature mapping of *what survives* a PSD↔Figma conversion and what is "coming soon" — the inverse-direction companion to the Figma→PSD problem. evidence: [T01-S024]
- **核心身份**: Content / developer-experience writer, divRIOTS (creators of psd.to.design, Backlight, WebComponents.dev). X: @ardena_gonzalez.
- **代表作品**: "Converting PSD to Figma: The ultimate guide" — the clearest public PSD-feature→Figma-feature table.
- **值得读/听/看**:
  - 📖 "Converting PSD to Figma: the ultimate guide" — https://divriots.com/blog/converting-psd-to-figma-the-ultimate-guide-to-importing-photoshop-files/.
  - 🎙️🎬 ⚠️ 无.
- **核心思想关键词**: feature-mapping table, "coming soon" honesty (vs hidden limits), smart-object → component-or-flattened, vector-mask-only support, font substitution.
- **voice_samples**:
  - On masks (concrete partial-support): "Only vector masks convert to Figma's masking system, with pixel masks coming soon." (source: T01-S024, 原话)
  - On smart objects: "Depending on complexity, these become components or flattened images." (source: T01-S024, 原话)
  - On effects: drop shadows/inner shadows/glows/other layer styles listed as "Coming soon" — i.e. effects do not yet round-trip. (source: T01-S024, 原话)
- **sub_skill_candidate**: `false` — vendor DX content, no independent long-form theory; valuable as a *structured limitation table* (rarer than it should be in this field).
- **最近 12 个月动态**: psd.to.design actively developed; the guide is maintained as features ship. evidence: [T01-S024]
- **争议/批评**: Vendor content — leads with "preserves layers and editability" / "visual integrity," which sits in tension with its own "coming soon" gaps (effects, pixel masks). Still notably *more* transparent than Convertify/Codia because it actually publishes the gap list. evidence: [T01-S024]
- **来源**:
  - [Primary] https://divriots.com/blog/converting-psd-to-figma-the-ultimate-guide-to-importing-photoshop-files/
- **可信度自评**: medium — vendor source but unusually explicit on limitations; PSD→Figma direction (mirror, not exact match).

---

### 9. Dag Ågren

- **One-liner**: Indie macOS developer (now at Panic) who wrote the canonical "PSD is not a good format. PSD is not even a bad format" comment in Xee's PSD loader — the most-cited artifact of PSD's endemic technical debt. evidence: [T01-S026, T01-S027]
- **核心身份**: Independent developer; creator of Xee (image viewer) and The Unarchiver; at Panic Inc. (Nova/Transmit).
- **代表作品**: Xee; The Unarchiver; the XeePhotoshopLoader.m comment (~2007).
- **值得读/听/看**:
  - 📖 XeePhotoshopLoader.m — https://github.com/gco/xee/blob/master/XeePhotoshopLoader.m — the source comment enumerating PSD reverse-engineering absurdities.
  - 📖 HN discussion — https://news.ycombinator.com/item?id=26762419 — community "ball of hacks" consensus.
  - 🎙️🎬 ⚠️ 无 PSD-specific interview.
- **核心思想关键词**: PSD organic growth, multiple ways to encode the same thing, format opacity, 30+ years of accumulated hacks.
- **voice_samples**:
  - The canonical comment (≤30 chars quoted to respect the rule): the loader famously opens by addressing the reader about "the Adobe PSD format," then states PSD "is not a good format" and "is not even a bad format," before enumerating its self-contradictions. (source: T01-S026, 原话 in code — full text intentionally not reproduced)
- **sub_skill_candidate**: `false` — historical-context figure, not a current Figma↔PSD practitioner.
- **最近 12 个月动态**: Active at Panic; no recent PSD-format output. The artifact is ~2007.
- **争议/批评**: Predates many modern PSD improvements; use as cultural/context evidence of why writing valid PSD is hard, not as a current-state spec. evidence: [T01-S027]
- **来源**:
  - [Primary] https://github.com/gco/xee/blob/master/XeePhotoshopLoader.m
  - [Reference] https://news.ycombinator.com/item?id=26762419
- **可信度自评**: high for historical context; low for current Figma-era specifics.

---

### 10. John Nack

- **One-liner**: Former Adobe Photoshop Senior PM — the one Adobe-side voice on record admitting the PSD format "reflects a lot of organic growth" and is "nowhere near as cleanly structured as a format one would write from scratch." evidence: [T01-S028]
- **核心身份**: Ex-Senior PM, Adobe Photoshop (~2002–2015); now independent; blogs at jnack.com.
- **代表作品**: Photoshop PM era (Smart Objects, Camera Raw, Bridge); the 2009 "Some thoughts about the PSD format" post.
- **值得读/听/看**:
  - 📖 jnack.com — https://jnack.com/blog/ — his current blog (photography/mobile-leaning now).
  - 📖 "Some thoughts about the PSD format" (2009, orig. blogs.adobe.com/jnack) — the canonical Adobe admission. **⚠️ The original blogs.adobe.com URL is unreliable (404/TLS at fetch time); the quote survives via secondary citations.**
  - 🎙️ Tips-from-the-Top-Floor interview (2007) — pre-Figma PM perspective.
- **核心思想关键词**: PSD organic growth, Smart Objects as complexity driver, backwards-compat burden, format-vs-product-quality distinction.
- **voice_samples**:
  - On the format: "Photoshop engineers would be the first to agree that the PSD format reflects a lot of organic growth and thus it's nowhere near as cleanly structured as a format one would write from scratch." (source: T01-S028, 原话 — via secondary citation; original Adobe URL not currently reachable)
- **sub_skill_candidate**: `false` — left Adobe ~2015; historical PSD-context only.
- **最近 12 个月动态**: jnack.com active but off-topic (photography/mobile). No recent PSD output.
- **争议/批评**: The 2009 post is partly PR; the structural problems he conceded remain. Use as the rare *insider* acknowledgment, not a current roadmap. evidence: [T01-S028]
- **来源**:
  - [Primary] https://jnack.com/blog/
  - [Secondary] tips-from-the-top-floor 2007 interview
- **可信度自评**: medium — role + statement well-attested via secondary sources; primary Adobe URL unreliable.

---

### 11. Ryan LeFevre (meltingice)

- **One-liner**: Creator of psd.js, the first widely-used JS PSD parser (2013) — historically important as proof that browser/Node PSD parsing was possible, but now abandoned and superseded by ag-psd. evidence: [T01-S030]
- **核心身份**: Software engineer (ex-LayerVault, HODINKEE); JS OSS developer.
- **代表作品**: psd.js.
- **值得读/听/看**: 📖 https://github.com/meltingice/psd.js — README documents missing pieces (layer comps, built-in renderer, some image modes/depths). 🎙️🎬 ⚠️ 无.
- **核心思想关键词**: browser-native PSD parsing, image-mode limitations, abandoned-but-referenced codebase.
- **voice_samples**: README notes missing "layer comp filtering, a built-in renderer, and many layer info blocks." (source: T01-S030, 原话)
- **sub_skill_candidate**: `false` — project inactive (last release 2021, ~172 open issues); historical reference only.
- **最近 12 个月动态**: No activity; effectively abandoned. evidence: [T01-S030]
- **争议/批评**: Abandoned with many open issues; cite for lineage, don't use in production.
- **来源**: [Primary] https://github.com/meltingice/psd.js
- **可信度自评**: medium for history; low for current relevance.

---

### 12. Codia AI (vendor — no named technical figure)

- **One-liner**: AI design-to-code company offering high-volume PSD↔Figma conversion (Psd2Figma plugin + web), marketed as lossless — included for ecosystem completeness and as the clearest example of *marketing-bias / zero technical transparency*. evidence: [T01-S031]
- **核心身份**: Company (codia.ai); design-to-code + asset-conversion platform; claims 500k+ users across 181 countries. **No identifiable individual maintainer/spokesperson with technical output.**
- **代表作品**: Codia AI Psd2Figma (Figma plugin); Figma→code; Figma→PSD export.
- **值得读/听/看**: 📖 https://codia.ai/psd-to-figma — product/marketing pages. 🎙️🎬 ⚠️ 无 technical talk.
- **核心思想关键词**: "every layer stays editable, accurate, perfectly preserved" (claim), AI-assisted conversion, design-dev handoff gap.
- **voice_samples**: Marketing claim only: "Import PSD files into Figma or export Figma designs to PSD in seconds. Every layer stays editable, accurate, and perfectly preserved." (source: T01-S031, 原话 — vendor marketing, treat as claim not fact)
- **sub_skill_candidate**: `false` — no individual; pure vendor.
- **最近 12 个月动态**: Active product; plugin on Figma Community. evidence: [T01-S031]
- **争议/批评**: "Perfectly preserved" is an unverifiable marketing absolute, contradicted by every transparent source in this track (effects/masks/colour/fonts all have documented gaps elsewhere). **Do not treat Codia's claims as fidelity evidence.** evidence: [T01-S031]
- **来源**: [Primary/vendor] https://codia.ai/psd-to-figma
- **可信度自评**: low for technical claims (marketing); medium for "this product exists and is high-volume."

---

## Additional Authoritative Non-Figure Sources (feed Phase 2, not "figures")

- **Adobe PSD/PSB File Format Specification** (T01-S025) — https://www.adobe.com/devnet-apps/photoshop/fileformatashtml/ — confirmed live; the byte-level ground truth every library author works from. **Route to Track 04.**
- **Library of Congress, PSD format sustainability** (T01-S029) — https://www.loc.gov/preservation/digital/formats/fdd/fdd000523.shtml — neutral institutional assessment of PSD characteristics; useful counterweight to vendor marketing. **Route to Track 04.**
- **Figma's own position**: Figma **cannot natively export to PSD** (confirmed across Figma Forum + help ecosystem); there is **no first-party Figma or Adobe technical document on cross-tool PSD fidelity**. The entire interop burden is carried by third parties. This is itself a Phase-2 fact. evidence: [T01-S023, T01-S031]

---

## Phase 2 提炼提示

### 反复出现 ≥ 3 个 figures / sources 都谈到的关键词 (候选行业心智模型)

- **font substitution / manual font loading** — the universal #1 named gap (Kutskir/Photopea tutorial, ag-psd README, psd-tools "no font rendering", Goedecke/Magicul, Gonzalez/divRIOTS, Convertify v11 font-replacement feature). evidence: [T01-S005, T01-S008, T01-S023, T01-S024]
- **layer-structure preserved, but effects/masks/smart-objects lost** — converters keep the hierarchy and lose the fidelity (Kutskir, Goedecke, Gonzalez/divRIOTS, psd-tools docs). evidence: [T01-S005, T01-S008, T01-S023, T01-S024]
- **blend-mode & pass-through asymmetry: Photoshop ≠ Figma** — pass-through is a group-tree behavior not a blend mode; PS has no pass-through layer mode because styles are inherently pass-through (Edwards), and 27 PS modes vs ~16 Figma modes with renamed equivalents (ag-psd / psd-tools). evidence: [T01-S013, T01-S008]
- **colour-space / profile gap** — Figma is not colour-managed; PSD expects an explicit ICC profile; sRGB-vs-P3 default mismatch (Edwards ×3 articles). evidence: [T01-S014, T01-S017]
- **opacity & coordinate quantization** — 0-100 opacity loses 154/256 8-bit steps; SVG/coord rounding differs per tool (Edwards). A subtle but real PSD-write fidelity loss. evidence: [T01-S015, T01-S016]
- **blur-radius has no universal standard** — must be rescaled per tool (Edwards' factor table). evidence: [T01-S011, T01-S012]
- **composite/canvas NOT auto-generated on write** — ag-psd (and thus its dependents) won't render the flattened preview for you; forget it and Photoshop shows wrong/blank. evidence: [T01-S002]
- **alpha premultiplication corruption** — niche but critical on PSD write from canvas data (ag-psd). evidence: [T01-S002]
- **PSD "organic growth" complexity** — independently arrived at by Ågren, Nack, ag-psd, psd-tools. evidence: [T01-S026, T01-S028, T01-S001, T01-S008]

### 显著分歧 / 流派分裂

- **"Preserve layers natively"** (Kutskir/Photopea, ag-psd-based plugins) vs **"Rasterize then reconstruct"** (PNG/SVG intermediates; and academically, Yamaguchi's LayerD decomposes flat rasters back into layers) — native has a higher fidelity ceiling but more edge-case breakage; rasterize is lossy but predictable. evidence: [T01-S005, T01-S023, T01-S033]
- **"Document your limits"** (ag-psd README, psd-tools docs, Marc Edwards, divRIOTS' "coming soon" table) vs **"Hide your limits"** (Photopea tutorial states only the font caveat; Convertify docs list zero limitations; Codia claims "perfectly preserved") — a clean transparency split between OSS/analyst authors and most commercial converters. evidence: [T01-S001, T01-S008, T01-S022, T01-S031]
- **Colour-accuracy camp** (Edwards: sRGB default, explicit profiles; Adobe spec: ICC embedding) vs **"good enough for screen"** camp (most plugins default to sRGB silently). Matters for print/brand. evidence: [T01-S014, T01-S025]

### 冷僻领域信号 (all TRUE)

- **总 figure 数: ~12 listed, but effective deep figures = 2** (Marc Edwards, Ivan Kutskir). ~3 are engineering authorities whose only "voice" is README/docs/code (Agamnentzar [pseudonymous], Yamaguchi, Korobov). The remainder are vendor-bloggers or historical-context.
- **多数 figure 长访谈材料 < 30 min**: only Marc Edwards (written corpus) and Kutskir (blog + HN) approach a usable body; **there is no conference-talk or podcast corpus for this niche at all.**
- **可信度 low/medium 比例 > 30%**: yes — 7 of 12 are medium-or-lower (vendors, pseudonym, abandoned project, historical). Only Edwards is unambiguously high.
- **Adobe/Figma DevRel voice: confirmed essentially zero** (Sonnet was right) — no first-party technical statement on cross-tool PSD fidelity from either vendor.

### Cold-Field Protocol → for SKILL.md 诚实边界 (honesty-boundary) section

Recommended wording for the skill's honesty boundary:

> **数据厚度 (figures)**: This skill's "figures" dimension is **tooling-heavy and practitioner-thin**. The knowledge is carried by (a) one independent analyst with a deep *written* corpus (Marc Edwards/Bjango), (b) a handful of OSS library maintainers whose "voice" is README/docs/code — one of them (ag-psd's "Agamnentzar") is an **unrecoverable pseudonym** with zero long-form output — and (c) vendor blogs that are commercially biased and mostly **hide their conversion limits**. There is **no podcast circuit, no conference-talk corpus, and no first-party Figma/Adobe technical statement** on cross-tool PSD fidelity. Mental models in this skill therefore lean on **Track 04 (specs: Adobe PSD spec, ag-psd/psd-tools limitation docs)** and **Track 02 (observed tool behavior)** rather than on figures' stated philosophies. Where a "best practice" is asserted, prefer evidence from the format spec or from the OSS limitation lists over any single vendor's marketing claim, and treat "lossless / perfectly preserved" vendor language as an unverified claim.

**Surrogate sources note**: No surrogate_primary tier was required — verified_primary coverage is strong (29 of 33 sources verified_primary, incl. Adobe spec + LoC). The field thinness is a **genuine characteristic of the domain**, not a research shortfall. The right Phase-2 move is to *weight specs/tool-behavior over figure-philosophy*, not to manufacture thickness.
