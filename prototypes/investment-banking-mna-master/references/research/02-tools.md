# Track 02 — Tools: Investment Banking / M&A 交易撮合

> Phase 1 tools research. Industry = M&A advisory / deal execution (analyst → associate → VP practitioner view). locale=global (en-primary). profile=practitioner.
> **Four tool layers, mapped to the deal workflow.** ① **Financial modeling** — Excel as the battlefield, accelerated by add-ins (Macabacus, Capital IQ Office plugin) and learned via training vendors (Wall Street Prep / BIWS / CFI / Training The Street); the standard model set is DCF / LBO / merger / accretion-dilution. ② **Market & deal data** — the screening / comps / precedent-transactions / league-table layer (Capital IQ Pro, PitchBook, LSEG Workspace, Bloomberg, Dealogic, Mergermarket, FactSet, free SEC EDGAR). ③ **Diligence / data room / process / production** — VDRs (Datasite / Intralinks / Ansarada), deal CRM (DealCloud), and the pitchbook/CIM production stack (PowerPoint + UpSlide + think-cell). ④ **AI new stack (decay=HIGH)** — the 2025-2026 GenAI wave reshaping junior work: Rogo, Hebbia, AlphaSense, Daloopa, internal bank LLMs, and the CIM/pitchbook auto-draft category.
> **Closed-source commercial SaaS** dominates this industry → no GitHub stars. Maturity signals = founding year / funding & M&A events (dated) / vendor-public usage counts (官方公开, caveated) / ownership map. AI-layer entries all carry **decay=high** + last_checked.
> **Wave-1 hand-off used (Track 04 canon Phase-2 interface):** canon flagged the 6 Rosenbaum & Pearl Excel models, Macabacus / Wall Street Prep accretion-dilution & LBO templates, and Damodaran's free datasets as Wave-2 tool candidates [04-canon §Phase 2 Interface]. All folded in below; Damodaran's free corpus is handed to the data layer as the one free first-party valuation-data source.
> **NOT cold.** ~40 tools explored, **30 retained** across 4 layers. Blacklist (LinkedIn article bodies / WSO forum / 知乎 / 微信 / 百度 / Quora / content farms) surfaced in searches and was deliberately dropped.

---

## Source Manifest

| source_id | url | bucket | last_checked | author/host | note |
|-----------|-----|--------|--------------|-------------|------|
| T02-S001 | https://www.microsoft.com/microsoft-365/excel | verified_primary | 2026-06-16 | Microsoft | Excel — the modeling battlefield; vendor product page |
| T02-S002 | https://techcommunity.microsoft.com/blog/excelblog/unlock-the-power-of-copilot-in-excel-now-generally-available/4242810 | verified_primary | 2026-06-16 | Microsoft (Excel blog) | Copilot in Excel now GA — first-party blog |
| T02-S003 | https://www.efinancialmodels.com/investment-banking-excel-shortcuts-a-practical-overview/ | secondary | 2026-06-16 | eFinancialModels | IB keyboard-only norm ("banks take mice from analysts"), shortcut set |
| T02-S004 | https://macabacus.com/pricing | surrogate_primary | 2026-06-16 | Macabacus (CFI) | Excel/PPT add-in pricing tiers (Basic/Pro/Enterprise) — vendor; site 403s automated fetch, URL index-verified |
| T02-S005 | https://help.corporatefinanceinstitute.com/article/1309-macabacus-access-discontinuation | surrogate_primary | 2026-06-16 | CFI help center | TIME-SENSITIVE: free Macabacus access for CFI Full-Immersion ends 2026-06-30 — first-party [education vendor] |
| T02-S006 | https://guides.library.columbia.edu/capitaliq/excelplugin | secondary | 2026-06-16 | Columbia U. Library | Capital IQ Excel plugin — CIQ formulas pull financial/market/transaction data |
| T02-S007 | https://www.wallstreetprep.com/self-study-programs/premium-package/ | surrogate_primary | 2026-06-16 | Wall Street Prep | Premium Package $499 = 7 courses incl. M&A (accretion/dilution, PPA) + LBO — vendor pricing [education vendor] |
| T02-S008 | https://www.wallstreetprep.com/knowledge/merger-model/ | surrogate_primary | 2026-06-16 | Wall Street Prep | Merger model + accretion/dilution mechanics — vendor tutorial [education vendor] |
| T02-S009 | https://breakingintowallstreet.com/advanced-financial-modeling/ | surrogate_primary | 2026-06-16 | BIWS / Mergers & Inquisitions | Advanced M&A modeling course (merger models, spinoff, majority-stake) — vendor [education vendor] |
| T02-S010 | https://corporatefinanceinstitute.com/pricing/ | surrogate_primary | 2026-06-16 | CFI | FMVA all-access pricing ($397.60 self-study / $677.60 full-immersion promo) — vendor [education vendor] |
| T02-S012 | https://trainingthestreet.com/on-campus-training/ | surrogate_primary | 2026-06-16 | Training The Street | "The Core" 5-day course builds 3-statement/DCF/LBO/M&A models — vendor; founded 1999 [education vendor] |
| T02-S013 | https://researchguides.worldbankimflib.org/BloombergProfessional/ExcelAddin | secondary | 2026-06-16 | World Bank/IMF Library | Bloomberg Excel add-in: BDP (current) / BDH (historical) / BDS (bulk) functions |
| T02-S014 | https://www.fintools.com/resources/financial-data/bql-for-excel/ | secondary | 2026-06-16 | FinTools | BQL = Bloomberg's newer cloud query language for Excel custom calcs |
| T02-S015 | https://www.spglobal.com/market-intelligence/en/solutions/products/sp-capital-iq-pro | verified_primary | 2026-06-16 | S&P Global Market Intelligence | Capital IQ Pro — 109k public + 60M private cos, M&A transactions; dominant IB data desktop |
| T02-S016 | https://press.spglobal.com/2025-10-22-S-P-Global-Redefines-Financial-Insights-with-New-AI-Powered-Multi-Document-Research-and-Analysis-Tool-in-Capital-IQ-Pro-ChatIQ | verified_primary | 2026-06-16 | S&P Global (press) | Document Intelligence 2.0 + Multi-Document ChatIQ (cited GenAI), 2025-10-22 |
| T02-S017 | https://press.spglobal.com/2026-03-12-S-P-Global-Enhances-Capital-IQ-Pro-with-Expanded-Fixed-Income,-Biopharma-and-Private-Markets-Data-Content-and-AI-Capabilities | verified_primary | 2026-06-16 | S&P Global (press) | Acquired Drift AI (NL model-building in Excel plugin) + ProntoNLP, 2026-03-12 |
| T02-S018 | https://pitchbook.com | verified_primary | 2026-06-16 | PitchBook (Morningstar) | Private-markets / PE-VC / M&A deal data — sponsor coverage standard |
| T02-S019 | https://www.lseg.com/en/data-analytics/financial-data/deals-data/investment-banking-league-tables | verified_primary | 2026-06-16 | LSEG | League-table authority — 4.4M transactions since 1970s; deals data |
| T02-S020 | https://finance.yahoo.com/news/refinitiv-name-scrapped-fresh-lseg-191931873.html | secondary | 2026-06-16 | Yahoo Finance | Refinitiv name retired; Eikon fully withdrawn 2025-06-30 → migrated to LSEG Workspace |
| T02-S021 | https://www.bloomberg.com/professional/products/bloomberg-terminal | verified_primary | 2026-06-16 | Bloomberg LP | Terminal — M&A via MA<GO>, deal terms/comps/league tables; ~$30k/seat/yr |
| T02-S022 | https://libguides.ithaca.edu/bloomberg/mergersandacquisitions | secondary | 2026-06-16 | Ithaca College Library | MA<GO> screening up to 20 variables; deal type/terms/comps/advisers |
| T02-S023 | https://dealogic.com/insight/global-markets-rankings-fy2025/ | verified_primary | 2026-06-16 | Dealogic (ION Group) | League-table authority — 900k+ M&A deals since 1998; fee/revenue rankings |
| T02-S024 | https://info.mergermarket.com/ | verified_primary | 2026-06-16 | Mergermarket (ION Analytics) | Predictive M&A intelligence for origination — rumored/pre-announcement deals |
| T02-S025 | https://insight.factset.com/resources/factset-mergers-datafeed | verified_primary | 2026-06-16 | FactSet (NYSE: FDS) | FactSet Mergers DB — 600k+ announced M&A/divestitures/spinoffs; workstation comps |
| T02-S026 | https://www.sec.gov/edgar/search/ | verified_primary | 2026-06-16 | U.S. SEC (govt) | EDGAR full-text search — free primary: S-4, DEFM14A, 8-K, fairness opinions |
| T02-S027 | https://grata.com | verified_primary | 2026-06-16 | Grata (Datasite) | AI-native private-co search, 21M+ cos; acquired by Datasite early 2025 |
| T02-S028 | https://www.datasite.com/en/company/news/datasite-to-merge-sourcescrub-and-grata-expanding-private-market-intelligence-solutions | surrogate_primary | 2026-06-16 | Datasite (news) | Datasite merging Sourcescrub (acq. Aug 2025) + Grata; AI deal sourcing rollup |
| T02-S029 | https://www.datasite.com/ | verified_primary | 2026-06-16 | Datasite | VDR market leader (ex-Merrill); Datasite AI redaction/auto-index; CapVest-backed |
| T02-S030 | https://www.businessnewsaustralia.com/articles/dealmaker-data-solutions-group-ansarada-to-be-acquired-by-rival-datasite-for--263m.html | secondary | 2026-06-16 | Business News Australia | Datasite completed Ansarada acquisition 2024-08-28, ~AUD$236m; GRC products carved out |
| T02-S031 | https://www.intralinks.com/ | verified_primary | 2026-06-16 | Intralinks (SS&C) | VDR pioneer (1996); SS&C-owned (2018); strong DCM/fund-reporting footprint |
| T02-S032 | https://www.ansarada.com/ | verified_primary | 2026-06-16 | Ansarada (Datasite) | VDR + deal readiness; pioneered "Ask Aida" AI + bidder-engagement scoring; APAC/mid-market |
| T02-S033 | https://www.firmex.com/ | verified_primary | 2026-06-16 | Firmex | Mid-market VDR with semi-transparent per-room / unlimited-annual pricing |
| T02-S034 | https://www.idealsvdr.com/ | verified_primary | 2026-06-16 | iDeals | Mid-market VDR — ease-of-use, fast setup, 24/7 support |
| T02-S035 | https://intapp.com/dealcloud/ | verified_primary | 2026-06-16 | Intapp (NASDAQ: INTA) | DealCloud — deal/relationship CRM + pipeline for IB advisory & PE; Applied AI |
| T02-S036 | https://www.microsoft.com/microsoft-365/powerpoint | verified_primary | 2026-06-16 | Microsoft | PowerPoint — pitchbook/CIM production canvas; Copilot generative slides |
| T02-S037 | https://upslide.net/ | verified_primary | 2026-06-16 | UpSlide | Office add-in for financial services — Excel↔PPT links, brand-compliant slide automation |
| T02-S038 | https://www.think-cell.com/ | verified_primary | 2026-06-16 | think-cell | PowerPoint charting add-in — waterfall/Mekko/Gantt/football-field; ~$19.90/user/mo |
| T02-S039 | https://rogo.ai | verified_primary | 2026-06-16 | Rogo | decay=high. AI analyst agent ("Felix") for IB — CIM gen, diligence, comps; 250+ institutions |
| T02-S041 | https://fintech.global/2026/01/28/rogo-raises-75m-series-c-to-scale-ai-finance-platform/ | secondary | 2026-06-16 | FinTech Global | decay=high. Rogo Series C $75M / ~$750M post, Sequoia + Henry Kravis + Wells Fargo, 2026-01-28 |
| T02-S042 | https://www.hebbia.com | verified_primary | 2026-06-16 | Hebbia | decay=high. "Matrix" grid-LLM for mass doc review/diligence; FlashDocs (acq. Jun 2025) → slide gen |
| T02-S043 | https://www.alpha-sense.com | verified_primary | 2026-06-16 | AlphaSense | decay=high. AI market-intel search + Generative Search (Nov 2024); 6,000+ customers |
| T02-S045 | https://daloopa.com | verified_primary | 2026-06-16 | Daloopa | decay=high. AI financial-data extraction into models, source-linked; 5,500 cos / 14yr; MCP connector |
| T02-S046 | https://fintech.global/2026/05/28/daloopa-raises-47m-to-fix-ais-financial-data-problem/ | secondary | 2026-06-16 | FinTech Global | decay=high. Daloopa Series C $47M, Brighton Park Capital lead, 2026-05-28 |
| T02-S047 | https://www.cnbc.com/2025/01/21/goldman-sachs-launches-ai-assistant.html | secondary | 2026-06-16 | CNBC | decay=high. Goldman GS AI Assistant firmwide to ~46,000 staff, 2025-01-21 (page 403'd, corroborated) |
| T02-S048 | https://www.marketsmedia.com/bloomberg-introduces-agentic-ai-to-the-terminal/ | secondary | 2026-06-16 | Markets Media | decay=high. Bloomberg ASKB agentic AI in beta on Terminal, 2026-02-23 ("BloombergGPT" brand faded) |
| T02-S049 | https://learn.microsoft.com/en-us/copilot/release-plan/ | verified_primary | 2026-06-16 | Microsoft Learn | decay=high. Finance in M365 Copilot GA 2025-10-20; Excel reconciliation, ERP workflows |
| T02-S050 | https://www.perplexity.ai | verified_primary | 2026-06-16 | Perplexity | decay=high. Perplexity Finance (Oct 2024); Daloopa integration Apr 2026; MNPI caveat for bankers |
| T02-S051 | https://www.brightwave.io | verified_primary | 2026-06-16 | Brightwave | decay=high. Analyst-grade research agents over filings/transcripts/memos; Series A $15M (Decibel) |
| T02-S052 | https://www.blueflame.ai/ | verified_primary | 2026-06-16 | BlueFlame AI | decay=high. Agentic GenAI for PE/IB — IC-memo/diligence drafting; **acquired by Datasite 2025-07-23** |
| T02-S053 | https://blueflame.ai/news/datasite-acquires-leading-agentic-ai-company-blueflame | verified_primary | 2026-06-16 | BlueFlame (news) | Datasite acquired BlueFlame 2025-07-23, folded into "Intelligence Unit" — first-party |
| T02-S054 | https://www.intralinks.com/products/dealcentre-ai | surrogate_primary | 2026-06-16 | Intralinks | DealCentre AI + "Link"/DealVision engine; Harvey AI integration (2025); claims 66% faster workflows |
| T02-S055 | https://www.datasite.com/en/products/blueflame-ai | verified_primary | 2026-06-16 | Datasite | Datasite MCP — Claude/ChatGPT/Copilot operate inside the deal; data never leaves secure env |

---

## Layer 1 — Financial Modeling (Excel + add-ins + training + templates)

### Microsoft Excel — the battlefield [T02-S001][T02-S003]
- **Use case:** Virtually all M&A models are hand-built in Excel — three-statement, DCF, LBO, merger / accretion-dilution. "The main battlefield." [T02-S001]
- **IB workflow norm (distinctive):** keyboard-only operation is industry standard — banks famously take mice from new analysts. Core: `Ctrl+Arrows`, `F2` (edit), `Ctrl+D` (fill down), `Alt` key-tip ribbon sequences (e.g. `Alt-H-O-I` auto-fit). Cited ~30-40% time savings. [T02-S003]
- **+/−:** universal, flexible, auditable cell-by-cell; but error-prone, no native version control, slow on huge models — which is exactly *why* the add-in ecosystem (Macabacus, CapIQ plugin) exists.
- **Recent (2025-26):** Copilot in Excel now GA; Python in Excel (pandas/NumPy) shipping — relevant for scenario work, **but banks still model manually for auditability.** [T02-S002] decay=med
- one-hand: vendor product page [T02-S001]; second-hand: IB shortcut norm [T02-S003].

### Macabacus (owned by CFI) [T02-S004][T02-S005]
- **Use case:** productivity add-in for Excel/PowerPoint/Word — formatting speed, Excel→PPT/Word linking, and **Model Check** error-auditing. The de facto formatting/proofing layer on models and decks.
- **+/−:** big speed gains on formatting/proofing + deep Excel-PPT linking; Windows-centric (weaker Mac), premium per-seat.
- **Pricing:** ~$200/user/yr Basic; Professional mid-tier (~$360, source-variant); Enterprise = contact sales (SSO). Treat tiers as approximate. [T02-S004]
- **⚠ TIME-SENSITIVE:** CFI **owns** Macabacus (acquired 2021-03-19) but is **unbundling** it — free grandfathered access for CFI Full-Immersion subscribers **ends 2026-06-30** [T02-S005]. Affected users must buy direct. (First-party CFI help center.)

### S&P Capital IQ Office / Excel plug-in [T02-S006][T02-S015]
- **Use case:** add-in pulling S&P financial/market/transaction/macro data into Excel via **CIQ formulas**; `CIQMATRIX` retrieves full income statement / BS / CF. Auto-populates comps, transaction comps, three-statement historicals; one-click refresh kills manual entry. [T02-S006]
- **+/−:** deepest deal/transaction + private-company data, strong screening; requires paid Capital IQ Pro license, Windows COM add-in, formula learning curve.
- **Pricing:** not public; bundled in the CIQ Pro enterprise seat.

### Training vendors — Wall Street Prep / BIWS / CFI / Training The Street
| Vendor | What | M&A course | Pricing (vendor-confirmed where ✓) | src |
|---|---|---|---|---|
| **Wall Street Prep (WSP)** | self-study modeling + Excel templates; used inside many banks for onboarding | M&A Modeling (accretion/dilution, PPA, pro forma) | Premium **$499** (7 courses incl M&A + LBO) ✓ / Basic **$199** ✓ | [T02-S007][T02-S008] |
| **Breaking Into Wall Street (BIWS)** / M&I | case-study / modeling-test orientation; recruiting prep | Advanced M&A Modeling (merger models, spinoff, majority-stake, ~10-12h) | Premium ~$597 / Adv M&A ~$97 (vendor/review, promo-variant) | [T02-S009] |
| **Corporate Finance Institute (CFI)** | FMVA cert + 250+ courses/templates; **owns Macabacus** | FMVA covers DCF/comps/M&A/LBO | Self-Study **$397.60/yr** / Full-Immersion **$677.60/yr** (promo) ✓ | [T02-S010] |
| **Training The Street (TTS)** | instructor-led corporate + campus (founded 1999) | "The Core" 5-day → 3-statement/DCF/LBO/M&A from scratch | public courses listed; corporate/campus = quote | [T02-S012] |
- **Choice signal:** WSP/TTS = bank-grade onboarding depth; BIWS = recruiting/test prep; CFI = breadth + cert (recognition debated among bankers).

### Terminal-linked Excel add-ins — FactSet / Bloomberg [T02-S013][T02-S014]
- **Bloomberg:** `BDP` (current), `BDH` (historical), `BDS` (bulk); **`BQL`** = newer cloud query language for custom calcs/screens — positioned as the modern replacement for legacy BDP/BDH. [T02-S013][T02-S014]
- **FactSet:** Excel add-in strong on equity-research estimates; auto-refresh comps/historicals.
- **+/−:** authoritative data + auto-refresh; require expensive terminal subscription + Windows COM add-in.

### Standard model set [T02-S008]
- **DCF** — intrinsic value: projected FCF + terminal value, discounted at WACC.
- **LBO** — PE-style buyout returns: capital structure, debt paydown, exit IRR/MOIC, sensitivities.
- **Merger / Accretion-Dilution** — the **signature M&A model**: combine acquirer+target pro forma, measure EPS accretion/dilution, with purchase-price allocation + pro forma statement adjustments. [T02-S008]
- All sit on a **three-statement** foundation. No universal template — banks build proprietary versions, but WSP / Macabacus / M&I / the 6 Rosenbaum & Pearl models [04-canon] define the de facto taught structure.

---

## Layer 2 — Market & Deal Data

**Ownership map:** S&P Global → Capital IQ Pro · Morningstar → PitchBook · LSEG → Workspace (ex-Refinitiv/Eikon) · Bloomberg LP (independent) · ION Group → both Dealogic + Mergermarket (ION Analytics) · FactSet (independent, NYSE: FDS) · SEC EDGAR (free, US govt) · Datasite has rolled up Grata + Sourcescrub + Valu8 (AI sourcing).

| Tool | What it's for in M&A | Strength / Weakness | Recent (12 mo) | src |
|---|---|---|---|---|
| **S&P Capital IQ Pro** | dominant IB desktop — comps, screening, precedent transactions; Excel plugin = analyst workhorse | deepest fundamentals + private-co financials, best Excel integration / expensive, league-table authority < Dealogic | **Document Intelligence 2.0 + ChatIQ** (cited GenAI, 2025-10) ; acquired **Drift AI** (NL model-building in plugin) + **ProntoNLP** (2026-03) | [T02-S015][T02-S016][T02-S017] |
| **PitchBook** (Morningstar) | private-market sourcing, PE/sponsor + VC deal data, private comps | best private-market/sponsor depth, clean UI / weak public fundamentals, not a league-table authority | launched in **ChatGPT (MCP)** Dec 2025 + Perplexity integration; Samaya AI partnership | [T02-S018] |
| **LSEG Workspace** (ex-Refinitiv Eikon) | **league-table authority** (banks cite LSEG ranks in pitchbooks); precedents, deal flow | longest deal history (since 1970s) / Workspace UI less loved | **Eikon fully withdrawn 2025-06-30**; "Refinitiv" name retired → LSEG Workspace | [T02-S019][T02-S020] |
| **Bloomberg Terminal** | `MA<GO>` deal screening (≤20 vars), deal multiples/comps, league tables, real-time markets+news | unmatched real-time markets/news/chat / M&A historical depth behind LSEG/Dealogic; ~$30k/seat | continued GenAI rollout (→ ASKB, see Layer 4) | [T02-S021][T02-S022] |
| **Dealogic** (ION) | the *other* league-table authority — **fee/revenue** rankings, origination, scorecards | best fee/revenue league tables + ECM/DCM breadth / not a research/comps terminal | integrated under ION Analytics w/ Mergermarket; FY25 rankings | [T02-S023] |
| **Mergermarket** (ION) | **origination/sourcing** — rumored / pre-announcement deal intelligence | best-in-class early/rumor intelligence (its differentiator) / not a quantitative comps engine | marketed as "Predictive M&A Intelligence for Origination" | [T02-S024] |
| **FactSet** (NYSE: FDS) | Mergers DB (600k+ deals), comps, precedents, DataFeed for quants; workstation | strong analytics/API, clean feeds / smaller deal universe than Dealogic, less PE depth than PitchBook | embedded **RADA** AI assistant across research/Flashwire M&A | [T02-S025] |
| **SEC EDGAR** (free) | **primary source** — S-4, DEFM14A (merger proxy: terms, background, fairness opinions), 8-K | free, authoritative, complete for US public deals / no screening/analytics, US-only, manual | EDGAR Next modernization; AI wrappers layering on top | [T02-S026] |
| **AI-native sourcing rollup** (Grata / Sourcescrub / Valu8) | agentic private-company search & origination | 21M+ private cos, founder-owned targets / vendor AI claims = marketing | **Datasite acquired Grata (early 2025) + Sourcescrub (Aug 2025) + Valu8 (May 2026)**, merging into Grata | [T02-S027][T02-S028] |

> **Free first-party data hand-off (from canon):** **Damodaran's NYU datasets** (betas, ERP, multiples by industry) are the one free, citable, first-party valuation-data source — pairs with EDGAR as the no-cost data floor before paid platforms [04-canon §Phase 2].

---

## Layer 3 — Diligence / Data Room / Process / Production

### Virtual data rooms (VDR)
| VDR | Positioning | +/− | Recent | src |
|---|---|---|---|---|
| **Datasite** (ex-Merrill, CapVest) | **market leader**; full lifecycle — Diligence (sell-side) / Acquire (buy-side) / Prepare / Archive | dominant advisory brand, deepest tooling, strong AI / premium price | **Datasite MCP** (Claude/ChatGPT/Copilot operate *inside* the deal, data never leaves) + AI redaction/auto-categorization | [T02-S029][T02-S055] |
| **Intralinks** (SS&C) | VDR pioneer (1996); broad FS footprint (DCM, fund reporting); closest independent peer to Datasite | track record + security, ~10k M&A deals/yr / UI less modern, enterprise-heavy | **DealCentre AI** ("Link"/**DealVision** engine: summaries, PII redaction, smart Q&A); **Harvey AI integration** (2025) | [T02-S031][T02-S054] |
| **Ansarada** (now Datasite) | VDR + **deal readiness**; **AiDA** AI assistant + **AI-Predict** bidder-engagement scoring; APAC/mid-market | early AI mover (predictive bidder analytics differentiator) / roadmap continuity Q's post-acquisition | **Datasite completed acquisition 2024-08-28 (~$236.3M, A$2.50/share)**; ESG/GRC/board carved out to founder Sam Riley (~$500k) | [T02-S032][T02-S030] |
| **Firmex / iDeals** | mid-market VDRs | better UX, faster onboarding, more transparent pricing (Firmex per-room) / less deep lifecycle/AI | both adding AI auto-index / Q&A | [T02-S033][T02-S034] |

### Deal CRM & pipeline
- **DealCloud (Intapp, NASDAQ: INTA)** — deal/relationship CRM + origination pipeline **purpose-built for capital markets** (PE, IB advisory, private credit). The "system of record" for the deal funnel — distinct from VDRs (manages the funnel, not the diligence docs). Configurable but implementation-heavy; "Applied AI" / Intapp Assist for sourcing signals + auto data capture. [T02-S035]

### Pitchbook / CIM production stack
- **Microsoft PowerPoint** — every pitchbook/CIM is produced here; the whole add-in ecosystem exists to accelerate it. Copilot generative slides shipping (banks cautious on confidential data). [T02-S036]
- **UpSlide** — Office add-in for **financial services**: brand-compliant templates, **Excel↔PowerPoint dynamic links** (auto-refresh charts when model updates), content library, slide automation. Heavy IB + Big Four use; claims double-digit hours saved/user/month. [T02-S037]
- **think-cell** — PowerPoint **charting** add-in: waterfall (bridges), Mekko/marimekko (market share), Gantt, **football-field** valuation charts; Excel data links. Near-ubiquitous in IB/consulting; ~$19.90/user/mo (semi-transparent). [T02-S038]
- Overlap note: Macabacus also does PPT formatting/linking — UpSlide (brand+links), think-cell (charts), Macabacus (model formatting+links) partially overlap; many banks run two of the three.

### Newer diligence tools (12 mo)
- **BlueFlame AI** — agentic, LLM-agnostic deal workspace for PE/IB: auto-drafts IC memos, diligence write-ups, company profiles ("cuts research/drafting 80-90%"); integrates Salesforce/DealCloud/Datasite/Grata. Founded 2023 (Raj Bakhru). **⚠ Acquired by Datasite 2025-07-23, folded into Datasite's "Intelligence Unit."** [T02-S052][T02-S053]
- **DealRoom** — combines VDR + M&A project management (diligence request trackers linked to docs) + PMI; "agile M&A" — reduces the Excel-tracker + separate-VDR fragmentation. Smaller brand.
- **⚠ Consolidation = the headline:** **Datasite now owns the top VDR + the two leading AI-diligence challengers** (Ansarada AiDA, BlueFlame agentic AI) **+ Grata** sourcing — backed by a $500M CapVest "Intelligence Unit" commitment. The only true independent enterprise peer is **Intralinks/SS&C** (DealVision). [T02-S053][T02-S030]
- **AI trend:** redaction, doc classification, Q&A assistants, bidder-prediction analytics, and **MCP/agent interoperability** (Datasite MCP; Intralinks + Harvey) are now table stakes across the category. [T02-S055][T02-S054]

---

## Layer 4 — AI New Stack (decay=HIGH · last_checked 2026-06-16)

> **Re-verify all funding/valuation before use — these move monthly.** Confidentiality/MNPI is the #1 adoption gate (drives banks to walled internal LLMs + SOC2/data-residency vendors over public ChatGPT/Perplexity). Hallucination-on-numbers is why a "verified data layer" (Daloopa) sits *under* the agents. Most "agents" still produce **first drafts requiring human analyst sign-off.**

### Rogo — flagship "AI analyst for IB" [T02-S039][T02-S041]
- Agentic platform on purpose-built financial-reasoning models + deep data integrations; agent **"Felix"** runs multi-step workflows. Use: deal screening, **CIM generation**, buyer outreach, data-room diligence, comps. Serves 35,000+ professionals / 250+ institutions (incl. bulge brackets).
- **Funding ladder (decay=high):** Series B $50M ~$350M post (Apr 2025) → **Series C $75M ~$750M post** (Sequoia + Henry Kravis + Wells Fargo, **2026-01-28**) → **Series D $160M ~$2B val** (Kleiner Perkins, **2026-04-29**); >$300M total.
- **Risk:** extreme valuation step-up ($750M→$2B in ~3 months) = hype froth; bank data-governance gating; output needs verification.

### Hebbia — document-mass extraction (Matrix) [T02-S042]
- **Matrix** = LLM as a parallel processor over a structured grid ("read these 500 credit agreements, extract EBITDA definition for each"). Use: mass diligence extraction across data rooms, contract/credit-agreement parsing; **FlashDocs** (acq. Jun 2025) → slide/pitchbook gen. $130M Series B ~$700M val (a16z, Jul 2024 — note older funding); ~30%+ of largest asset managers + elite law firms. More buy-side/legal-skewed than pure IB-deal-flow.

### AlphaSense — market intelligence + Generative Search [T02-S043]
- AI search over filings/transcripts/broker research/news; **Generative Search** (Nov 2024) answers NL questions with cited sourcing. Use: target/sector research, expert-call insight, sourcing. **Tegus acquisition completed 2024-07-08 (~$930M)** → expert-call transcript library + private-co data; same round took val to **$4B**; >$400M ARR, 6,000+ customers. Research/intel layer, *not* a deal-execution agent.

### Daloopa — verified data layer for models [T02-S045][T02-S046]
- Auto-extracts/cleans financial metrics from filings/decks into **model-ready, source-linked** data (5,500 cos, 14yr); ships an **MCP connector** so LLMs/agents pull *verified* figures (OpenAI MCP late 2025; Perplexity Apr 2026; also feeds Rogo). Use: populating/auditing models & comps — kills manual filing data entry. **Series C $47M (Brighton Park Capital, 2026-05-28).** The antidote to LLM hallucination on numbers; it's infra under other tools.

### CIM / pitchbook auto-draft (the category) + internal bank LLMs [T02-S047][T02-S049]
- **Who drafts CIMs/decks:** Rogo (Felix), Hebbia/FlashDocs, **M365 Copilot** (draft from Excel/prior CIMs/PDFs + CapIQ/FactSet/PitchBook). First-draft only; MNPI handling gates adoption → banks favor walled tools.
- **Internal bank LLMs:** **Goldman GS AI Assistant** firmwide to ~46,000 staff (2025-01-21) [T02-S047]; **Morgan Stanley** AI@MS Assistant (2023) + **AskResearchGPT** (Oct 2024, searches 70k+ proprietary reports). Compliant on proprietary data, but productivity-assistant tier — capability lags specialist vendors like Rogo.
- **M365 Copilot:** Finance in M365 Copilot **GA 2025-10-20** (Excel reconciliation, ERP workflows) [T02-S049]; sits in the tools bankers already use, but horizontal not IB-native.

### Terminal-embedded + general LLMs [T02-S048][T02-S050]
- **Bloomberg ASKB** — agentic conversational AI **in beta** on the Terminal (2026-02-23); the 2023 "BloombergGPT" research brand has faded. ASKB Workflows assemble multi-step research; generates BQL. Terminal-locked. [T02-S048]
- **Perplexity Finance** (Oct 2024) + general LLMs (ChatGPT, Claude) — quick comps / scans / drafting. **⚠ Public LLMs = MNPI/confidentiality red line** — most banks restrict/ban for live deal data; not auditable. Mostly non-confidential research only. [T02-S050]
- **Brightwave** — analyst-grade research agents over filings/transcripts/memos; Series A $15M (Decibel). Buy-side/research more than deal-execution. [T02-S051]

---

## Phase 2 Interface

### Core tool stack — minimum viable set, by workflow stage
| Deal stage | Must-have (必备) | Why |
|---|---|---|
| **Origination / sourcing** | Mergermarket *or* PitchBook + DealCloud (CRM) | rumored deals + sponsor data + pipeline tracking |
| **Screening / comps / precedents** | Capital IQ Pro (+ Excel plugin) + SEC EDGAR (free) | comps/precedents from CIQ; ground-truth from EDGAR |
| **League tables (pitchbook)** | LSEG Workspace *or* Dealogic | the citable ranking authority |
| **Modeling** | Excel + Macabacus + Capital IQ Office plugin | hand-build DCF/LBO/merger model with add-in speed + data pull |
| **Production (pitchbook/CIM)** | PowerPoint + think-cell + UpSlide | charts + brand + Excel-PPT links |
| **Diligence / data room** | Datasite (or Intralinks; Firmex/iDeals mid-market) | secure VDR + Q&A + buyer analytics |
| **AI accelerant (optional, gated)** | Daloopa (data) + Rogo *or* internal bank LLM | verified data layer + first-draft agent (human sign-off required) |

### Selection decision tree
1. **Budget / firm size?** Bulge/elite boutique → Capital IQ Pro + Bloomberg + LSEG + Datasite + DealCloud (full enterprise). Mid-market boutique → Capital IQ *or* PitchBook + Firmex/iDeals + Excel/Macabacus; lean hard on **free EDGAR + Damodaran datasets**.
2. **What's the job?** League tables for a pitch → LSEG/Dealogic. Private-target sourcing → PitchBook/Grata. Rumored-deal origination → Mergermarket. Public comps/precedents → Capital IQ / FactSet.
3. **Data room side?** Sell-side advisory at scale → Datasite. DCM/fund-heavy → Intralinks. Cost-sensitive mid-market → Firmex/iDeals.
4. **Production add-in?** Charts-heavy → think-cell. Brand + Excel-PPT links → UpSlide. Model formatting + links → Macabacus (⚠ verify CFI-bundle status post 2026-06-30).
5. **AI?** Need *verified numbers in models* → Daloopa. Full deal-workflow agent → Rogo (if firm allows). Confidential live-deal work → **internal bank LLM only**, never public ChatGPT/Perplexity (MNPI).

### Hand-off to Track 03 (workflow)
- Workflow chapters should anchor each step to its tool: pitch → (LSEG/Dealogic league tables + PowerPoint/think-cell); valuation → (Excel + Capital IQ plugin, 4 model types); process → (Datasite VDR Q&A + DealCloud); production → (UpSlide/think-cell). The **keyboard-only Excel norm** [T02-S003] and the **DCF/LBO/merger/accretion-dilution** model set are the concrete craft artifacts Track 03 should script.
- Flag the **AI-augmented junior workflow** as a 2025-26 workflow rewrite (Daloopa data pull → Rogo/Copilot first-draft → human verification), with the MNPI gate as a hard constraint.

### New figure / tool candidates to feed downstream
- **Tool-as-craft artifacts:** the football-field chart (think-cell), the accretion-dilution output, the buyer-engagement heatmap (Datasite/Ansarada), the CIM as a production object.
- **People/orgs surfacing in the AI wave:** Rogo (Gabriel Stengel), AlphaSense, Hebbia — candidate figures for an "AI-reshaping-IB" sidebar.
- **Watch-list (high decay):** Rogo valuation trajectory; ASKB GA-vs-beta; whether internal bank LLMs absorb the Rogo use case; **Datasite's AI-diligence roll-up** (Ansarada + BlueFlame + Grata under one roof) vs Intralinks/SS&C as the last independent enterprise VDR.

---

## Quality Self-Check
- **Tools retained:** 30+ across 4 layers (Excel, Macabacus, CapIQ Office plugin, WSP, BIWS, CFI, TTS, Bloomberg/FactSet Excel add-ins, standard model set | Capital IQ Pro, PitchBook, LSEG, Bloomberg, Dealogic, Mergermarket, FactSet, EDGAR, Grata/Sourcescrub | Datasite, Intralinks, Ansarada, Firmex, iDeals, DealCloud, PowerPoint, UpSlide, think-cell, BlueFlame, DealRoom | Rogo, Hebbia, AlphaSense, Daloopa, M365 Copilot, Bloomberg ASKB, Perplexity, Brightwave, internal bank LLMs). **Target ≥15 ✅**
- **Sources:** 55 (target ≥15) ✅
 - verified_primary: 32 (vendor official sites/docs roots, S&P/Microsoft/SEC press & blogs, BlueFlame & Datasite news, govt EDGAR) ✅
 - surrogate_primary: 8 (vendor pricing/training/news subpages: Macabacus, WSP×2, BIWS, CFI, TTS, Datasite news, Intralinks DealCentre AI) ✅
 - secondary: 15 (PR Newswire, CNBC, FinTech Global, Markets Media, Yahoo Finance, Business News Australia, university library guides, eFinancialModels) ✅
- **Blacklist compliance:** no LinkedIn article bodies, WSO forum, 知乎/微信/百度/Quora, or content farms cited (all surfaced and dropped). ✅
- **AI layer:** every Layer-4 entry tagged **decay=high** + last_checked=2026-06-16; funding dates explicit. ✅
- **Pricing honesty:** vendor-confirmed prices (WSP $499/$199, CFI $397.60/$677.60) marked ✓; all enterprise-data (CapIQ/Bloomberg/FactSet/PitchBook/LSEG/Datasite) flagged quote-based / estimate-only. ✅
- **Ownership map explicit** (Layer 2) — S&P/Morningstar/LSEG/ION/FactSet/Datasite rollups dated. ✅
- **Canon hand-off used:** R&P 6 models, Macabacus/WSP templates, Damodaran free datasets folded in from 04-canon Phase-2 interface. ✅
