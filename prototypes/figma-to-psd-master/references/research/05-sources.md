# Track 05 — Sources: Figma → PSD High-Fidelity Conversion (Skill: figma-to-psd-master)

> Living information sources a practitioner should monitor. The tool landscape here changes fast (plugins ship monthly, `.fig` is an undocumented internal format, no native PSD export exists), so "what to watch" matters more than in a settled field.
> last_checked: 2026-06-03 (OPUS, Track 05 fresh pass; seeded from 02-tools + 01-figures).
>
> **COLD-FIELD ADVISORY (dedicated-media layer):** There is **no newsletter, podcast, conference, or community dedicated to Figma↔PSD interop**. The closest dedicated media is the broader **design-tools** beat (UX Tools, Figmalion, Design Details). The *actual* fidelity knowledge does not live in media at all — it lives in **GitHub CHANGELOGs/issues, library READMEs, one practitioner blog (Bjango), and forum threads.** This track is honest about that: most retained sources are **changelogs-to-watch + official docs**, not "media."

---

## Source Manifest

| source_id | url | bucket | last_checked | author/host | one-line note |
|-----------|-----|--------|--------------|-------------|---------------|
| T05-S001 | https://github.com/Agamnentzar/ag-psd/blob/master/CHANGELOG.md | verified_primary | 2026-06-03 | Agamnentzar (GitHub) | ag-psd changelog — the real release feed (Releases tab is EMPTY); latest v30.0.1 |
| T05-S002 | https://www.npmjs.com/package/ag-psd?activeTab=versions | verified_primary | 2026-06-03 | npm | ag-psd version+date feed (changelog has no dates); v30.1.1 @ 2026-04-10 |
| T05-S003 | https://github.com/psd-tools/psd-tools/releases | verified_primary | 2026-06-03 | psd-tools org (GitHub) | psd-tools GitHub releases — actively shipping |
| T05-S004 | https://pypi.org/project/psd-tools/ | secondary | 2026-06-03 | PyPI | psd-tools release feed; v1.17.1 @ 2026-05-26, multiple/month |
| T05-S005 | https://github.com/webtoon/psd/releases | verified_primary | 2026-06-03 | Webtoon (GitHub) | @webtoon/psd releases; STALE — last v0.4.0 @ 2023-06-27 |
| T05-S006 | https://blog.photopea.com/ | verified_primary | 2026-06-03 | Ivan Kutskir | Photopea changelog blog; IRREGULAR (latest post 2024-04-22, v5.6) |
| T05-S007 | https://github.com/photopea/photopea/issues | reference | 2026-06-03 | Photopea (GitHub) | Photopea issue tracker — where .fig/PSD-export breakage is reported & confirmed |
| T05-S008 | https://www.figma.com/community/plugin/1610258845845995569/psd-exporter-importer | secondary | 2026-06-03 | 3rd-party (Figma Community) | "PSD Exporter & Importer" — MOST-ACTIVE dedicated exporter; v10 @ 2026-05-30 |
| T05-S009 | https://www.figma.com/community/plugin/1580712765592303644/publicis-sapient-figma-to-psd-exporter-beta | secondary | 2026-06-03 | Publicis Sapient (Figma Community) | NEW Figma→PSD exporter (Beta) — watch but unproven |
| T05-S010 | https://www.figma.com/community/plugin/1418190299890697167/codia-ai-psd2figma-import-and-export-photoshop-psd | secondary | 2026-06-03 | Codia AI (Figma Community) | Codia AI Psd2Figma plugin listing — vendor changelog (claims unverified) |
| T05-S011 | https://developers.figma.com/docs/rest-api/changelog/ | verified_primary | 2026-06-03 | Figma Developer Docs | REST API changelog (image/export endpoint changes); latest 2026-03-25 |
| T05-S012 | https://developers.figma.com/docs/plugins/updates/ | verified_primary | 2026-06-03 | Figma Developer Docs | Plugin API updates (exportAsync/node export surface); latest 2026-05-22 (Update 126) |
| T05-S013 | https://helpx.adobe.com/photoshop/desktop/whats-new/whats-new-in-adobe-photoshop-on-desktop.html | verified_primary | 2026-06-03 | Adobe | Photoshop desktop "What's new" release notes; updated 2026-05-26; PS 2026 / v27.x |
| T05-S014 | https://developer.adobe.com/photoshop/uxp/ | verified_primary | 2026-06-03 | Adobe Developer | UXP plugin platform docs hub (batchPlay/DOM) — successor to ExtendScript |
| T05-S015 | https://help.figma.com/hc/en-us | verified_primary | 2026-06-03 | Figma Help Center | Official help hub incl. export/blend/color-profile articles + monthly release-notes roundup |
| T05-S016 | https://developers.figma.com/docs/ | verified_primary | 2026-06-03 | Figma Developer Docs | Dev docs hub (REST + Plugin API export surfaces) |
| T05-S017 | https://www.adobe.com/devnet-apps/photoshop/fileformatashtml/ | verified_primary | 2026-06-03 | Adobe | Official PSD/PSB byte-format spec — ground truth for any writer |
| T05-S018 | https://bjango.com/articles/ | verified_primary | 2026-06-03 | Marc Edwards / Bjango | THE cross-tool fidelity blog (blur/shadow/blend/colour/opacity); active (latest Mar 2025) |
| T05-S019 | https://www.uxtools.co/ | secondary | 2026-06-03 | Taylor Palmer & Jordan Bowman | "Insider News for Design Tools" — weekly newsletter + annual Design Tools Survey + podcast |
| T05-S020 | https://figmalion.com/ | secondary | 2026-06-03 | Eugene Fedorenko | Weekly Figma + design-tools roundup; #251 @ 2026-05-30 (independent) |
| T05-S021 | https://designdetails.fm/ | secondary | 2026-06-03 | Brian Lovin & Marshall Bock | Weekly design craft/culture podcast; touches tooling, NOT interop-specific |
| T05-S022 | https://forum.figma.com/ | secondary | 2026-06-03 | Figma (official forum) | First-party forum; "no PSD export" + plugin-fidelity consensus lives here |
| T05-S023 | https://www.reddit.com/r/FigmaDesign/ | reference | 2026-06-03 | Reddit community | Figma users; plugin/export questions; de-facto Q&A |
| T05-S024 | https://www.reddit.com/r/photoshop/ | reference | 2026-06-03 | Reddit community | PS users; import/Smart-Object/file-format Q&A |
| T05-S025 | https://www.reddit.com/r/photopea/ | reference | 2026-06-03 | Reddit community | Photopea community (Kutskir participates); .fig-import + save-PSD issues |
| T05-S026 | https://news.ycombinator.com/item?id=26762419 | reference | 2026-06-03 | Hacker News | Canonical "PSD is a ball of hacks" thread — why valid PSD write is hard |

---

## 総覧（按 type 分组）

### Newsletter / Substack — 2 个 (+ 1 first-party roundup)

| Source | Cadence | Tier | 投入产出 | One-liner |
|--------|---------|------|----------|-----------|
| UX Tools (T05-S019) | weekly | practitioner/senior | medium | Only dedicated *design-tools* media; tool comparisons + annual survey |
| Figmalion (T05-S020) | weekly (Tue) | practitioner | medium | Curated Figma + tooling roundup; cheapest way to catch plugin/feature churn |
| Figma Help "Release notes roundup" (in T05-S015) | monthly | mixed | medium | First-party monthly feature roundup (also a livestream) |

### Podcast — 1 个 (honest: thin, none interop-specific)

| Source | Cadence | Host | 投入产出 | One-liner |
|--------|---------|------|----------|-----------|
| Design Details (T05-S021) | weekly | Lovin & Bock | low | Design craft/culture; occasional tooling; **never** PSD-interop. Ambient only |
| (UX Tools podcast, part of T05-S019) | ~weekly | designertom | low-medium | Tooling-focused interviews; better topical fit than Design Details |

### Conference — 0 个 (N/A)

No conference covers Figma↔PSD interop. Figma's own **Config** exists but is product-marketing, not interop. **GAP — explicit.**

### Community — 5 个

| Community | Platform | 规模 (推断) | One-liner |
|-----------|----------|------------|-----------|
| Figma Forum (T05-S022) | Figma (official) | large, posts/min | First-party; "no PSD export" + plugin-fidelity consensus |
| Photopea GitHub issues (T05-S007) | GitHub | active | Where .fig/PSD-export breakage is reported AND triaged by Kutskir |
| r/FigmaDesign (T05-S023) | Reddit | ~600k+ | Figma export/plugin Q&A |
| r/photoshop (T05-S024) | Reddit | ~1M+ | PS import/Smart-Object/format Q&A |
| r/photopea (T05-S025) | Reddit | smaller | Photopea-specific; dev participates |

### Changelogs-to-watch — 9 个 (the core of this track)

| Source | Channel | Cadence | Watch for |
|--------|---------|---------|-----------|
| ag-psd (T05-S001 + T05-S002) | CHANGELOG.md + npm | irregular, ~monthly | write-side limit changes (RGB/8-bit/text-bitmap) |
| psd-tools (T05-S003 + T05-S004) | GitHub releases + PyPI | multiple/month | parser/decoder coverage (validation tooling) |
| @webtoon/psd (T05-S005) | GitHub releases | STALE (2023) | any revival; else assume frozen |
| Photopea (T05-S006 + T05-S007) | blog + GitHub issues | irregular blog; rolling issues | new version features; .fig-import breakage |
| PSD Exporter & Importer (T05-S008) | Figma Community | ~monthly (v10 May 2026) | font-mapping / effect fidelity improvements |
| Publicis Sapient exporter (T05-S009) | Figma Community | new/beta | whether it matures into a real option |
| Codia Psd2Figma (T05-S010) | Figma Community | active | vendor changes (treat claims as unverified) |
| Figma REST API changelog (T05-S011) | dev docs | ~monthly | `GET images` format/scale/cap changes |
| Figma Plugin API updates (T05-S012) | dev docs | ~monthly | `exportAsync` / export surface changes |
| Adobe PS release notes (T05-S013) | helpx | ~monthly | Smart Object / file-format / UXP changes |

### Official-docs hubs — 6 个

| Source | Owner | Good for |
|--------|-------|----------|
| Figma Help Center (T05-S015) | Figma | export/blend/color-profile behavior + release roundups |
| Figma Developer Docs (T05-S016) | Figma | REST + Plugin export surfaces (the confirmed "no PSD" floor) |
| Adobe PS "What's new" (T05-S013) | Adobe | current PS version + feature deltas |
| Adobe UXP docs (T05-S014) | Adobe | in-PS automation (assembler plugins) — successor to ExtendScript |
| Adobe PSD/PSB spec (T05-S017) | Adobe | byte-format ground truth for any PSD writer |
| Bjango articles (T05-S018) | Marc Edwards | the only deep cross-tool *fidelity* reference (semi-official by reputation) |

---

## SOURCE CARDS

### 📰 1. UX Tools — uxtools.co  ★ best dedicated-media fit

- **Type**: newsletter (+ podcast + annual survey)
- **URL**: https://www.uxtools.co/
- **Author / Host**: Taylor Palmer & Jordan Bowman ("designertom") — independent.
- **Cadence**: weekly newsletter. **Last activity**: current through 2026-05 (verified). evidence: [T05-S019]
- **Audience tier**: practitioner → senior.
- **One-liner**: The single closest thing to *dedicated* design-tooling media — "data-backed design insights, **tool comparisons**, and workflow deep dives," 100K+ readers, and the publisher of the **annual Design Tools Survey** (the field's only longitudinal tool-popularity data). evidence: [T05-S019]
- **典型每期内容**: curated design-tool news, hands-on tool reviews/comparisons, workflow deep-dives; periodic survey data (Design Tools, Prototyping).
- **投入产出比**: **medium** — broad design-tools coverage; Figma↔PSD interop appears only occasionally, but this is where you'd first hear of a new converter or a Figma/PS feature that affects handoff. ~50-70% of issues carry a practitioner-level signal for *this* niche's adjacent context. evidence: [T05-S019]
- **Paywall**: none (free newsletter; some content/surveys gated by email).
- **签名内容**: the annual **Design Tools Survey** results (tool market-share + sentiment).
- **Endorsement evidence**: appears across design-tooling search results as the reference design-tools outlet (`cross_source`); testimonials from Figma-affiliated readers (`community_consensus`). evidence: [T05-S019]
- **替代品**: Figmalion (Figma-leaning); Design Details (podcast).
- **最近变化**: continues newsletter + podcast + surveys into 2026.
- **可信度**: high (independent, long-running, data-backed). **Decay risk**: low-medium.

---

### 📰 2. Figmalion — figmalion.com

- **Type**: newsletter + curated resource base
- **URL**: https://figmalion.com/
- **Author / Host**: Eugene Fedorenko (author of *Designing in Figma*) — independent (endorsed by Figma leadership, not official).
- **Cadence**: weekly (Tuesdays). **Last activity**: **Issue #251 @ 2026-05-30** (verified). evidence: [T05-S020]
- **Audience tier**: practitioner.
- **One-liner**: A weekly curated roundup of Figma + the broader design-tools community — the cheapest single channel to catch plugin releases, Figma feature changes, and tooling discourse that touch the handoff problem. evidence: [T05-S020]
- **典型每期内容**: links to new Figma features, notable community plugins, design-system/AI items, occasional tool deep-dives.
- **投入产出比**: **medium** — Figma-centric (covers the *source* side of Figma→PSD); the PSD destination is rarely the focus, but exporter-plugin launches surface here. evidence: [T05-S020]
- **Paywall**: none.
- **签名内容**: weekly issue archive (#249–#251, Apr–May 2026).
- **Endorsement evidence**: endorsed by Dylan Field/Figma advocates (`figure_short`); cross-listed with UX Tools as the two design-tooling newsletters (`cross_source`). evidence: [T05-S019, T05-S020]
- **替代品**: UX Tools (tool-comparison angle); Figma Blog/Newsroom (first-party).
- **最近变化**: steady; no host change.
- **可信度**: high. **Decay risk**: medium (single-curator personal newsletter).

---

### 🎙️ 3. Design Details — designdetails.fm  (honest: thin fit)

- **Type**: podcast
- **URL**: https://designdetails.fm/
- **Host**: Brian Lovin & Marshall Bock.
- **Cadence**: weekly. **Last activity**: active in 2026 (467 episodes; still posting new episodes). evidence: [T05-S021]
- **Audience tier**: practitioner (design craft/culture).
- **One-liner**: The most established active design podcast that *sometimes* discusses design tools — but it is craft/culture/process oriented and has **no Figma↔PSD interop content**; include for ambient awareness only. evidence: [T05-S021]
- **典型每期内容**: interface critiques, product/design-process conversations, occasional "design tools today / AI grab bag" rounds.
- **投入产出比**: **low** for this niche — <50% of episodes touch tooling, and ~0% touch PSD interop. Treat as ambient, not required. evidence: [T05-S021]
- **Paywall**: free (Patreon-gated "Sidebar" bonus segment).
- **签名内容**: periodic "Design Tools" theme episodes.
- **Endorsement evidence**: long-running with large listenership across Spotify/Apple (`community_consensus`); surfaced as the top design-tools podcast in search (`cross_source`). evidence: [T05-S021]
- **替代品**: the **UX Tools podcast** (T05-S019) is a closer topical fit (tooling interviews).
- **最近变化**: host lineup has shifted over the years; currently Lovin & Bock.
- **可信度**: high (real, active). **Decay risk**: medium. **Honest note**: there is **no PSD-interop podcast**; this is the least-load-bearing retained source.

---

### 🔄 4. ag-psd CHANGELOG.md + npm versions  ★ top changelog-to-watch

- **Type**: changelog (the de-facto release feed for the engine under every code-based exporter)
- **URL**: https://github.com/Agamnentzar/ag-psd/blob/master/CHANGELOG.md  (+ dates: https://www.npmjs.com/package/ag-psd?activeTab=versions)
- **Maintainer**: Agamnentzar (pseudonymous).
- **Cadence**: irregular (~monthly bursts). **Last activity**: changelog top = **v30.0.1**; **npm v30.1.1 @ 2026-04-10**. evidence: [T05-S001, T05-S002]
- **Audience tier**: senior/engineering.
- **One-liner**: ag-psd is the JS PSD-writer beneath most Figma→PSD plugins, so its changelog is the **single highest-leverage feed** — a change to its write limits (RGB-only, 8-bit, text-bitmap requirement) ripples through the whole ecosystem. evidence: [T05-S001]
- **典型每期内容**: read/write fixes (e.g. v30.0.1 = 16-bit *read* fix; v30.0.0 = `useRawData` read option; v29.1.0 = ABR import). Note pattern: recent work is **read-side**; the write ceiling is stable.
- **投入产出比**: **high** for the engineering audience — when this moves, downstream exporter fidelity can move. evidence: [T05-S001]
- **CRITICAL watch-note (一手, corrects a natural assumption)**: the GitHub **Releases tab is EMPTY** ("There aren't any releases here") — do NOT watch `/releases`. The real feed is **CHANGELOG.md** (no dates) cross-referenced with **npm versions** (dates). evidence: [T05-S001, T05-S002]
- **替代品**: psd-tools (Python, read-focused) for validation; @webtoon/psd (read-only, stale).
- **可信度**: high (一手 repo). **Decay risk**: low (MIT, widely depended on, steady).

---

### 🔄 5. psd-tools — GitHub releases + PyPI

- **Type**: changelog (Python PSD read/inspect library)
- **URL**: https://github.com/psd-tools/psd-tools/releases  (+ https://pypi.org/project/psd-tools/)
- **Maintainer**: Mikhail Korobov + Kota Yamaguchi.
- **Cadence**: **multiple releases/month**. **Last activity**: **v1.17.1 @ 2026-05-26**. evidence: [T05-S003, T05-S004]
- **Audience tier**: senior/engineering.
- **One-liner**: The most-actively-shipping PSD library in the stack — best used as a **validator/decoder** of generated PSDs (it won't render fonts/most effects, so it's QA, not a converter). evidence: [T05-S003, T05-S004]
- **典型每期内容**: parser coverage, layer/effect decoding, descriptor fixes.
- **投入产出比**: **medium-high** for engineering (QA tooling for a pipeline); low for non-coders. evidence: [T05-S004]
- **替代品**: @webtoon/psd (JS read-only) — but stale; ag-psd (read+write).
- **可信度**: high. **Decay risk**: low (very active).

---

### 🔄 6. PSD Exporter & Importer (Figma Community plugin)  ★ most-active dedicated exporter

- **Type**: changelog (Figma Community plugin listing = the changelog channel)
- **URL**: https://www.figma.com/community/plugin/1610258845845995569/psd-exporter-importer
- **Maintainer**: third-party (Figma Community).
- **Cadence**: ~monthly. **Last activity**: **Version 10 @ 2026-05-30** (just days before this pass). evidence: [T05-S008]
- **Audience tier**: practitioner.
- **One-liner**: The most-actively-maintained dedicated Figma→PSD exporter (offline, font-mapping), and its update notes are a live read on **where exporter fidelity is actually improving** (v10 = multi-weight font fix, PostScript-name mapping, fully offline/no CDN). evidence: [T05-S008]
- **典型每期内容**: font-handling fixes, layer/group/vector-shape fidelity, "complex layer effects being refined."
- **投入产出比**: **high** for anyone choosing an exporter — it's the de-facto reference plugin and its changelog telegraphs the field's frontier. evidence: [T05-S008]
- **替代品**: PSD Export (motion-focused); Publicis Sapient exporter (beta); Codia (vendor).
- **可信度**: medium (一手 listing; no independent benchmark). **Decay risk**: medium (3rd-party plugin lifecycle). **Note**: the listing page blocks automated fetch (403) and needs a browser; verified via search snippet.

---

### 🔄 7. Figma REST API Changelog + Plugin API Updates

- **Type**: changelog (first-party developer platform)
- **URL**: https://developers.figma.com/docs/rest-api/changelog/  +  https://developers.figma.com/docs/plugins/updates/
- **Maintainer**: Figma Inc.
- **Cadence**: ~monthly each. **Last activity**: REST **2026-03-25**; Plugin **2026-05-22 (Update 126)**. evidence: [T05-S011, T05-S012]
- **Audience tier**: senior/engineering.
- **One-liner**: The authoritative feeds for the **export surfaces** that bound every programmatic pipeline — watch for any change to `GET images` (format/scale/32MP cap) or `exportAsync` (the surfaces that today top out at PNG/SVG/PDF, never PSD). evidence: [T05-S011, T05-S012]
- **典型每期内容**: new endpoints/scopes, node-property additions, rate-limit changes; recent entries are non-export (grids, oEmbed) — confirming the export floor is stable.
- **投入产出比**: **medium** — most entries don't touch export, but this is the only place a *native PSD path* (or an export-format expansion) would first appear. evidence: [T05-S011]
- **替代品**: Figma Blog/Newsroom + Help Center release-notes roundup (product-level).
- **可信度**: high (一手). **Decay risk**: low (institutional).

---

### 🔄 8. Adobe Photoshop "What's new" / desktop release notes

- **Type**: changelog + official docs
- **URL**: https://helpx.adobe.com/photoshop/desktop/whats-new/whats-new-in-adobe-photoshop-on-desktop.html
- **Maintainer**: Adobe.
- **Cadence**: ~monthly with each PS update. **Last activity**: page **updated 2026-05-26**; PS **2026 / v27.x**. evidence: [T05-S013]
- **Audience tier**: mixed.
- **One-liner**: The destination side of the pipeline — watch for Smart-Object, file-format, color-engine, or UXP changes that alter how an imported/assembled PSD behaves. evidence: [T05-S013]
- **投入产出比**: **medium** — most PS releases are AI/photo features irrelevant to interop, but format/Smart-Object/UXP deltas matter directly. evidence: [T05-S013]
- **替代品**: companion "release notes" page (known issues/fixes); Adobe UXP docs (T05-S014) for automation surface.
- **可信度**: high (一手). **Decay risk**: low. **Note**: page is JS-heavy (fetch timed out twice); confirmed live + dated via search.

---

### 📚 9. Official docs hubs (Figma + Adobe) — reference set

- **Figma Help Center** (T05-S015, https://help.figma.com/hc/en-us): export formats, blend modes, color-profile management, + a **monthly release-notes roundup/livestream**. First-party behavior reference. evidence: [T05-S015]
- **Figma Developer Docs** (T05-S016, https://developers.figma.com/docs/): REST + Plugin export surfaces — the confirmed "no PSD on any surface" floor. evidence: [T05-S016]
- **Adobe UXP docs** (T05-S014, https://developer.adobe.com/photoshop/uxp/): the supported in-PS automation platform (batchPlay/DOM) for assembler plugins; successor to deprecated ExtendScript. evidence: [T05-S014]
- **Adobe PSD/PSB File Format Spec** (T05-S017, https://www.adobe.com/devnet-apps/photoshop/fileformatashtml/): the byte-level ground truth every PSD writer reverse-engineers against. evidence: [T05-S017]
- **投入产出比**: docs are reference, not feeds — **low** churn, **high** value when a changelog points you here. 可信度 high. Decay risk low.

---

### 📖 10. Bjango articles — Marc Edwards  ★ the fidelity knowledge base

- **Type**: practitioner blog (semi-canonical by reputation)
- **URL**: https://bjango.com/articles/
- **Author**: Marc Edwards (Bjango) — independent of both vendors.
- **Cadence**: occasional/irregular. **Last activity**: "Design systems need a colour space" **Mar 2025**; blog active into 2026. evidence: [T05-S018]
- **Audience tier**: senior.
- **One-liner**: The **only deep public source on *why* a value renders differently between Figma and Photoshop** — hard-number tables for blur radius, drop-shadow conversion, blend modes, color management, opacity precision, SVG rounding. This is where converter-*fidelity* knowledge actually lives. evidence: [T05-S018]
- **典型每期内容**: long-form, reproducible cross-tool comparisons with formulas (e.g. 50px PS blur ≈ 115.9px Figma).
- **投入产出比**: **high** per article — low volume, but each piece is directly load-bearing for matching a PSD to its Figma source. evidence: [T05-S018]
- **Paywall**: none.
- **Endorsement evidence**: cited across the design-tooling community as the cross-tool reference (`community_consensus`); independent of vendors (`cross_source`). evidence: [T05-S018]
- **替代品**: none equivalent — this is unique. Pair with the Adobe spec (T05-S017) for byte-format.
- **可信度**: high. **Decay risk**: medium (single-author blog, but durable archive).

---

### 💬 11. Communities — where converter-fidelity discussion actually happens

- **Figma Forum** (T05-S022, https://forum.figma.com/): **first-party**, very active (posts every few minutes), with Figma staff ("Figmate") replies. The canonical "how do I convert Figma → layered PSD?" threads and the **community consensus that no tool keeps layers 100%** live here. evidence: [T05-S022]
- **Photopea GitHub issues** (T05-S007, https://github.com/photopea/photopea/issues): where `.fig`-import breakage and vector-rasterization behavior are reported AND triaged by the developer — the de-facto bug-knowledge base for the free route. evidence: [T05-S007]
- **r/FigmaDesign** (T05-S023) / **r/photoshop** (T05-S024) / **r/photopea** (T05-S025): Reddit Q&A on export/import, Smart Objects, plugin recommendations; r/photopea is small but the developer participates. evidence: [T05-S023, T05-S024, T05-S025]
- **Hacker News "PSD is a ball of hacks" thread** (T05-S026, id=26762419): the cultural ground-truth on *why writing valid PSD is hard* — context, not how-to. evidence: [T05-S026]
- **投入产出比**: **medium** — high noise, but for a pre-canonical field these threads + GitHub issues ARE the knowledge base; expect to dig. 可信度: forum/issues medium-high; Reddit/HN reference-tier. Decay risk: low (platforms durable).

---

## Phase 2 提炼提示

**「这一行的资深人订阅最多的 top sources」** (monitor these — ranked by signal density for *this* niche):

1. **ag-psd CHANGELOG.md + npm** (T05-S001/S002) — the engine; changes ripple to every code-based exporter. *Cadence: ~monthly.*
2. **PSD Exporter & Importer plugin listing** (T05-S008) — the most-active dedicated exporter; its notes telegraph the fidelity frontier. *Cadence: ~monthly (v10 May 2026).*
3. **Bjango / Marc Edwards** (T05-S018) — the only deep fidelity reference; consult per-dimension (blur/shadow/blend/colour). *Cadence: occasional.*
4. **Figma Forum + Photopea GitHub issues** (T05-S022 + T05-S007) — where real-world breakage and consensus surface. *Cadence: rolling.*
5. **UX Tools + Figmalion** (T05-S019 + T05-S020) — the design-tools media layer; weekly ambient awareness of feature/plugin churn. *Cadence: weekly.*

(Runners-up to watch quarterly: psd-tools releases [QA], Figma REST/Plugin changelogs [the only place a native PSD path would appear], Adobe PS release notes [Smart-Object/format deltas].)

**「这一行最近的话题热度」** `topic-heat: medium-confidence (changelog/feed dates inspected for ~10 sources; full issue/thread bodies NOT crawled)`:
- **Exporter font fidelity** — multi-weight/PostScript-name mapping is the active frontier (PSD Exporter & Importer v10, May 2026). evidence: [T05-S008]
- **AI-assisted conversion churn** — Codia + new "AI design-to-code" entrants; claims still unverified. evidence: [T05-S010]
- **New beta exporters appearing** — e.g. Publicis Sapient Figma→PSD (Beta) — signal the niche is attracting fresh attempts. evidence: [T05-S009]
- **Figma export floor unchanged** — recent REST/Plugin changelog entries (grids, oEmbed, rate limits) confirm **no native PSD path is coming**. evidence: [T05-S011, T05-S012]

**新 figures 发现** (feed to Track 01):
- **Taylor Palmer & Jordan Bowman** (UX Tools) — design-tools analysts; run the annual Design Tools Survey (the field's only longitudinal tool data). evidence: [T05-S019]
- **Eugene Fedorenko** (Figmalion; *Designing in Figma* author) — Figma-ecosystem curator. evidence: [T05-S020]
- (Marc Edwards / Ivan Kutskir / Agamnentzar / Korobov / Yamaguchi already in Track 01.)

**新 tools 发现** (feed to Track 02):
- **Publicis Sapient "Figma to PSD Exporter (Beta)"** (Figma Community, ID 1580712765592303644) — NOT in Track 02; a newer dedicated exporter to evaluate. evidence: [T05-S009]
- **Codia AI Psd2Figma Figma-Community plugin** (ID 1418190299890697167) — Track 02 had codia.ai web page (T02-S019) but not the in-Figma plugin listing; the plugin is the changelog-able surface. evidence: [T05-S010]

**冷僻 / 信号薄弱 (Phase 2.8 诚实边界)** — all TRUE:
- **newsletter = 2** (+1 first-party roundup) — at floor; both are *design-tools*-broad, neither interop-specific.
- **podcast = 1** (Design Details, low fit; UX Tools podcast as adjunct) — **below the ≥3 threshold; effectively a GAP.** No PSD-interop podcast exists.
- **conference = 0** — **explicit GAP**; no event covers this niche.
- **The dedicated-media layer is genuinely thin**: there is no newsletter, podcast, or conference about Figma↔PSD conversion specifically. The closest media is the broader design-tools beat (UX Tools, Figmalion).
- **Where fidelity knowledge actually lives** (the honest answer for SKILL.md "想跟最新动态"): **(1) GitHub CHANGELOGs/issues** (ag-psd, psd-tools, Photopea), **(2) one practitioner blog** (Bjango/Marc Edwards), **(3) plugin Community update notes** (PSD Exporter & Importer), **(4) the Adobe PSD spec**, and **(5) Figma Forum threads** — NOT in media. evidence: [T05-S001, T05-S007, T05-S008, T05-S017, T05-S018, T05-S022]
- **No neutral, independent benchmark of converter fidelity exists** (consistent with Track 02) — all vendor "pixel-perfect" claims remain unverified; the Design Tools Survey (UX Tools) is popularity, not fidelity.
- **Fetch-access caveats (honesty)**: Figma Community plugin pages (S008/S009/S010) return 403 to automated fetch (need a browser; verified via search). Reddit (S023–S025) not fetchable from this environment; member counts marked 推断. Adobe pages (S013/S017) are JS-heavy and timed out but confirmed live + dated via search and the Track-01 prior pass.

---

*OPUS Track 05 pass: 2026-06-03. Sources: 26 (verified_primary 13 / secondary 8 / reference 5 / blacklisted 0). Seeded from 02-tools + 01-figures; ~30 candidates explored, 26 retained across newsletters(2) / podcasts(1) / communities(5) / changelogs(10) / official-docs(6) [overlap: docs double as feeds]. Key corrections vs naive assumptions: ag-psd Releases tab is EMPTY (watch CHANGELOG.md + npm, not /releases); Figma "developers changelog" is split into REST-changelog + Plugin-updates (the singular /changelog/ 404s); Photopea blog lags (latest 2024-04) so pair with GitHub issues; the PSD Exporter & Importer plugin is freshly active (v10, 2026-05-30). New for downstream tracks: Publicis Sapient exporter (beta) + Codia plugin listing → Track 02; UX Tools founders + Eugene Fedorenko → Track 01. Honest edges: dedicated-media layer is thin (no interop newsletter/podcast/conference); fidelity knowledge lives in changelogs/issues/Bjango/spec, not media.*
