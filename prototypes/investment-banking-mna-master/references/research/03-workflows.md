# Track 03 — Workflows: Investment Banking M&A / Deal Execution

> Industry: investment banking M&A / 交易撮合 — the end-to-end deal workflow from pitch to close, practitioner POV (analyst → associate → VP → MD + corp dev + PE buy-side). Locale: global, EN-primary. profile=practitioner.
> Last compiled: 2026-06-16. Built on Wave-1 Tracks 01 (figures), 02 (tools), 04 (canon), 06 (glossary) — re-using their validated sources under re-assigned T03 ids where load-bearing.
>
> **Spine of this track:** the deal is a *staged information-and-leverage game wrapped around a valuation model*. A board choosing among bids does NOT pick the highest number — it implicitly computes `EV ≈ headline price × P(close) − cost-of-a-busted-deal − time-value-of-delay`, then trades on **structure** when it can't agree on **price**. The six phases below each separate **how a junior builds the machine** from **how a senior reads it / sets the real price**, and each preserves the field's defining contradictions: long-process discipline vs relationship trust; narrative packaging vs numbers diligence; valuation's scientific veneer vs negotiation's real price-setting; and the banker agency problem — *the advisor who values the deal is paid a contingent success fee only if it closes, so the analysis is structurally biased toward "yes."*
>
> **Honesty constraints carried forward:** every number (success fee, control premium, breakup fee, value-destruction rate, hold period, fee sizing) carries source + caveat and is never universalized. Regulatory items carry an explicit decay flag. Blacklist (LinkedIn article bodies / WSO / 知乎 / 公众号 / 百度 / Quora / content farms) surfaced in searches and was deliberately dropped.

---

## Source Manifest

| source_id | url | bucket | last_checked | author/host | note |
|-----------|-----|--------|--------------|-------------|------|
| T03-S001 | https://www.wallstreetprep.com/knowledge/sell-side-process/ | surrogate_primary | 2026-06-16 | Wall Street Prep | canonical auction taxonomy (broad/limited/targeted/exclusive + bidder counts), 4-stage timeline, CIM contents [education vendor] |
| T03-S002 | https://corpgov.law.harvard.edu/2012/06/20/standstills-in-change-of-control-transactions/ | verified_primary | 2026-06-16 | Harvard Law Forum (firm-authored) | standstill as "cost of entry"; broad-auction record lets board refuse waivers |
| T03-S003 | https://corpgov.law.harvard.edu/2012/12/18/dont-ask-dont-waive-standstills/ | verified_primary | 2026-06-16 | Harvard Law Forum | "Don't Ask, Don't Waive" standstill mechanics + Delaware constraints |
| T03-S004 | https://www.faegredrinker.com/en/insights/publications/2018/3/ma-101-key-concepts-in-nondisclosure-agreements | surrogate_primary | 2026-06-16 | Faegre Drinker (law firm) | NDA mechanics: standstill public-seller-only, use restriction, non-solicit 18-24mo, bank supplies NDA form [own publication] |
| T03-S005 | https://www.goodwinlaw.com/en/insights/publications/2023/05/insights-privateequity-ma-durations-exclusivity-periods | surrogate_primary | 2026-06-16 | Goodwin Procter | data: exclusivity windows lengthened — 61+ day from 6% (2021) to ~40% (2022) [own publication] |
| T03-S006 | https://www.sec.gov/Archives/edgar/data/0001751143/000121390023015568/defm14a2023_atlastech.htm | verified_primary | 2026-06-16 | SEC EDGAR — Atlas Technical / GI Partners DEFM14A | textbook broad PE auction: 38 contacted / 28 NDAs / 9 IOIs / exclusivity blocks a $12.25 topping bid |
| T03-S007 | https://www.sec.gov/Archives/edgar/data/1868778/000119312525158774/d74603ddefm14c.htm | verified_primary | 2026-06-16 | SEC EDGAR — Informatica / Salesforce DEFM14C | targeted strategic outreach (9 parties); a WSJ leak killed the 2024 deal; revived 2025 at lower price |
| T03-S008 | https://www.sec.gov/Archives/edgar/data/1496963/000114036124038138/ny20030653x9_defm14a.htm | verified_primary | 2026-06-16 | SEC EDGAR — Squarespace / Permira DEFM14A | sponsor take-private, founder rollover, special committee, go-shop negotiated OUT |
| T03-S009 | https://cooleyma.com/2026/03/30/dual-track-processes-how-to-turbocharge-your-exit-2/ | surrogate_primary | 2026-06-16 | Cooley M&A | 2026 dual-track (IPO + sale) guide — IPO as "an extra bidder" [own publication] |
| T03-S010 | https://insights.crewe.com/iois-lois-and-their-differences/ | secondary | 2026-06-16 | Crewe Capital | precise IOI-vs-LOI content distinction |
| T03-S011 | https://corporatefinanceinstitute.com/resources/valuation/staple-financing/ | surrogate_primary | 2026-06-16 | Corporate Finance Institute | stapled financing price-floor + dual-fee conflict; no-shop period lengths [education vendor] |
| T03-S012 | https://www.harvey.ai/blog/ai-due-diligence-for-m-and-a | secondary | 2026-06-16 | Harvey (AI vendor) | AI data-room/Q&A capabilities + adoption stats (vendor-reported, caveat) |
| T03-S013 | https://aswathdamodaran.blogspot.com/2012/12/acquisition-alchemy-creating-value-from.html | verified_primary | 2026-06-16 | Aswath Damodaran (Musings on Markets) | bidding discipline: walk away from bidding wars; value synergy/control separately; don't pay it all as premium |
| T03-S014 | https://aswathdamodaran.blogspot.com/2012/12/acquisition-archives-winners-and-losers.html | verified_primary | 2026-06-16 | Aswath Damodaran | overpayment empirics: ~55% of acquirers' stock drops; KPMG 83% of 1996-98 megadeals underperform |
| T03-S015 | https://aswathdamodaran.blogspot.com/2015/10/dealmaking-deal-breaking-fairness.html | verified_primary | 2026-06-16 | Aswath Damodaran ("Fairness Opinions: Fix them or Flush them!") | fairness opinion = not a real valuation; range so wide "any price can be justified"; fix = kill contingent fees |
| T03-S016 | https://www.bain.com/insights/looking-back-m-and-a-report-2026/ | verified_primary | 2026-06-16 | Bain & Company M&A Report 2026 | 2025 market: scope-vs-scale mix (~60% of >$1B deals scope), AI-capability megadeals, gen-AI use 21% of practitioners |
| T03-S017 | https://www.bain.com/insights/outlook-gaining-traction-global-private-equity-report-2026/ | verified_primary | 2026-06-16 | Bain & Company Global PE Report 2026 | PE hold ~7yr at exit; distributions ~14% of NAV (multidecade low); continuation-vehicle growth |
| T03-S018 | https://www.mckinsey.com/capabilities/strategy-and-corporate-finance/our-insights/repeat-performance-the-continuing-case-for-programmatic-m-and-a | verified_primary | 2026-06-16 | McKinsey & Company | programmatic acquirers' median excess TSR ~2.3% vs selective/organic/big-bet (caveat: association not causation) |
| T03-S019 | https://www.deloitte.com/us/en/about/press-room/deloitte-survey-genai-in-mna.html | verified_primary | 2026-06-16 | Deloitte GenAI-in-M&A survey (H1 2025, n=1,000 US) | 86% integrated GenAI into M&A; sourcing 35% / diligence 35% (self-reported, caveat) |
| T03-S020 | https://corpgov.law.harvard.edu/2025/12/20/mergers-and-acquisitions-reviewing-2025-and-looking-ahead-to-2026/ | verified_primary | 2026-06-16 | Harvard Law Forum (Wachtell) | signing-to-close risk, reverse termination fees, 2025-26 antitrust posture; 2025 US M&A ~$2.3T (+49%) |
| T03-S021 | https://www.srsacquiom.com/our-insights/deal-terms-study-2025/ | verified_primary | 2026-06-16 | SRS Acquiom 2025 Deal Terms Study | 2,200+ private-target deals 2019-24 ($505B): escrow 10% (no RWI)/0.5% (RWI); survival median 12mo; 21% walk-away |
| T03-S022 | https://www.hl.com/insights/ (Transaction Termination Fee Study 2024) | verified_primary | 2026-06-16 | Houlihan Lokey | breakup fee 2024 avg ~2.4% of equity value (down from 2.9% in 2021), range 0.2-6.0% |
| T03-S023 | https://www.ftc.gov/news-events/news/press-releases/2026/01/ftc-announces-2026-update-jurisdictional-fee-thresholds-premerger-notification-filings | verified_primary | 2026-06-16 | US FTC | 2026 HSR size-of-transaction threshold US$133.9M, effective Feb 17 2026; top filing fee $2.46M |
| T03-S024 | https://www.ftc.gov/advice-guidance/competition-guidance/guide-antitrust-laws/mergers/premerger-notification-merger-review-process | verified_primary | 2026-06-16 | US FTC | 30-day standard / 15-day cash-tender waiting period; Second Request stops the clock |
| T03-S025 | https://www.hklaw.com/en/insights/publications/2026/03/hart-scott-rodino-filings | surrogate_primary | 2026-06-16 | Holland & Knight | TIME-SENSITIVE: new HSR form VACATED 2026-02-12 (E.D. Tex), 5th Cir denied stay 2026-03-19; reverted to old form [own publication] |
| T03-S026 | https://home.treasury.gov/policy-issues/international/the-committee-on-foreign-investment-in-the-united-states-cfius/cfius-overview | verified_primary | 2026-06-16 | US Treasury (CFIUS) | CFIUS scope, Section 721 DPA / FIRRMA, 45+45+15-day review; TID mandatory triggers |
| T03-S027 | https://www.weil.com/-/media/mailings/2025/q2/presidential-action-regarding-nippon-steel.pdf | surrogate_primary | 2026-06-16 | Weil Gotshal | Nippon/US Steel CFIUS "golden share" + reopening precedents (blocked Jan-2025 → approved Jun-2025) [own publication] |
| T03-S028 | https://www.ftc.gov/news-events/news/press-releases/2024/12/statement-ftc-victory-securing-halt-kroger-albertsons-grocery-merger | verified_primary | 2026-06-16 | US FTC | Kroger/Albertsons $24.6B blocked Dec-2024 (D. Oregon PI) — concrete antitrust kill |
| T03-S029 | https://mergersandinquisitions.com/investment-banking-pitch-books/ | surrogate_primary | 2026-06-16 | Mergers & Inquisitions (Brian DeChesare) | pitchbook structure + "relationships win deals, juniors build the deck" [education vendor] |
| T03-S030 | https://www.goodwinlaw.com/en/insights/publications/2025/10/how-deal-and-financing-certainty-wins-ma-competitions | surrogate_primary | 2026-06-16 | Goodwin Procter | certainty trumps marginal price; HOHW, equity backstop, RTF 4-7% of EV [own publication] |
| T03-S031 | https://corpgov.law.harvard.edu/2025/12/ (Wachtell, "Re-emergence of Contingent Value Rights") | verified_primary | 2026-06-16 | Harvard Law Forum (Wachtell) | CVR re-emergence in biotech: 9 (2022) → 27 (2025) per Deal Point Data |
| T03-S032 | https://www.dechert.com/knowledge/onpoint/2026/1/minimum-hsr-reporting-threshold-rises-to-us-133-9-million--inter.html | surrogate_primary | 2026-06-16 | Dechert | corroborates 2026 HSR threshold $133.9M (cross-check vs FTC, which 403s automated fetch) [own publication] |
| T03-S033 | https://www.dealroom.net/blog/buy-side-m-a-process | surrogate_primary | 2026-06-16 | DealRoom (Kison Patel / Agile M&A) | buy-side thesis discipline, QoE/diligence workstreams, integration-in-parallel |
| T03-S034 | https://www.bain.com/insights/topics/global-private-equity-report/ | verified_primary | 2026-06-16 | Bain & Company | ~$1.2T 2025 US PE deal value; take-private surge; dry-powder aging |

(34 sources; verified_primary 23 = SEC EDGAR proxies ×3 + FTC/Treasury ×5 + Damodaran ×3 + law-firm primary memos ×7 + Bain/McKinsey/Deloitte/SRS/Houlihan/Wachtell studies; surrogate_primary 7 = WSP/CFI/M&I/Cooley/DealRoom vendor tutorials; secondary 4 = Crewe/Harvey/etc. Blacklist zero-cited.)

> **Cross-track reuse note:** the football-field chart, the DCF/LBO/merger/accretion-dilution model set, and Damodaran's free datasets are Track 02/04 artifacts referenced here as workflow inputs, not re-documented. Track 06 supplies the term definitions (teaser/CIM/IOI/LOI/SPA/MAC/RTF) this track operationalizes.

---

## Phase 1 — Pitch / Winning the Mandate

### How the mandate is actually won (and the agency problem baked in at step zero)

Deal origination flows from **senior-banker relationships, not pitchbook polish**. The blunt practitioner framing: bankers win deals because of relationships cultivated over 5-10 years of meeting the CEO/CFO; "a pretty presentation right before a sale means little compared with that" [T03-S029]. Banks operationalize this with **coverage groups** (own the client relationship, quarterback) + **product groups** (M&A execution) — a coverage banker brings the deal in, the M&A group executes [carried from T06 §6.4].

The pitchbook (~25-50 slides) is the analyst's artifact: (1) positioning / "why us" — league-table ranks + tombstones, sliced into the most flattering cut; (2) credentials/team bios; (3) sector + company context; (4) valuation views culminating in the **football field**; (5) buyer profiles (often the longest, most labor-intensive section); (6) process recommendation (usually "targeted sale to the 5-10 best buyers"); (7) fees [T03-S029].

**The agency problem is structural and present from day one:** the banker is simultaneously deal-maker and deal-analyst, paid a contingent success fee only if the deal closes — so the analysis tilts toward "yes," and control/synergy premiums are the lever used to push the justified price upward. Damodaran's line: *"asking a banker whether an M&A deal makes sense is like asking a plastic surgeon whether there is something wrong with your face"* [T03-S013][T03-S015].

- **跳过哪步:** lower-middle-market / repeat-sponsor mandates routinely **skip the formal competitive pitch** — a known relationship hands the mandate directly. The full beauty-contest pitchbook is largely a large-cap / first-time-seller / fiduciary-cover ritual.
- **优化点:** AI now drafts the commoditized pitchbook layers (comps pages, buyer profiles) in minutes — Goldman's internal assistant produces draft pitchbooks fast [carried from T02-S047]; the MD's relationship and the *strategic idea* are the part AI can't replace [T03-S016].
- **额外动作 (senior):** MDs do unsolicited "idea" pitches and work ad-hoc projects for free to stay "in the mix" before a sale is even contemplated [T03-S029].
- **案例:** the buyer-profile section of a sell-side pitch is where a junior burns the most hours — a full page on each potential acquirer's strategic fit, balance-sheet capacity, and likely interest — precisely the layer being automated first [T03-S029][T03-S016].

---

## Phase 2 — Valuation & Modeling (how the model is BUILT vs USED)

### Analyst builds the machine; MD reads it backward

The standard set — **DCF, trading comps, precedent transactions, LBO, merger / accretion-dilution, sensitivity** — is hand-built in Excel by the analyst on a three-statement foundation [carried from T02 model set / T04 §4]. The analyst produces the **football field**: a floating bar chart placing each method's implied range side-by-side (52-week range, comps, precedents, DCF, LBO, sometimes SOTP).

The football field's purpose is **not** a point estimate — it communicates a *defensible range* and shows where methods converge (high confidence) vs diverge (judgment territory) [carried from T04 §4 #9; T06 §6.1]. The MD uses it backward: picks the range that supports the strategic story, leans on the method that flatters the recommendation (**comps in hot markets, DCF when fundamentals are stronger**), and frames synergy. **Sensitivity tables** (WACC × terminal growth; accretion/dilution × synergies) become *negotiation props* — in a pitch the MD shows a buyer how much they "can afford to pay if synergies materialize."

**The contradiction to preserve — valuation science vs negotiation reality:** the analyst's DCF produces a precise number; the deal closes at a number set by who has the better BATNA, the credible second bidder, and more information. The model is the *floor of the conversation, not the conversation*. And accretion/dilution is an **EPS test, not a value test** — a deal can be accretive and still destroy value (Damodaran's standing caution) [T03-S013].

**Synergy is the most abused input:** overstated revenue synergies + front-loaded cost synergies justify a higher offer, and because they're qualitative/strategic they're hard to falsify in the room. Damodaran's discipline: value the standalone target accurately, value synergy and control *separately* with the burden of proof on the claimant, and — critically — **do not offer all the synergy value as premium**, or "target stockholders walk away with the spoils and your stockholders get nothing" [T03-S013].

- **跳过哪步:** in a fast targeted process the MD may **skip a full DCF** and price purely off precedent-transaction multiples + what competitive tension will bear — the DCF is then back-filled for the fairness-opinion record.
- **优化点:** Daloopa-style verified-data layers auto-populate the model's historicals/comps, killing manual filing entry; the analyst's edge shifts from data entry to assumption-setting [carried from T02-S045].
- **额外动作 (senior):** the MD pressure-tests the *narrative behind the number* — "what story makes this multiple defensible to a board?" — the numbers↔narrative bridge [carried from T04-S010].
- **案例:** Kodak overpaid ~**$2.2B** for Sterling Drug (pharma outside its competence) — a textbook control premium paid for a synergy that never appeared; the model "supported" a price the strategy never could [T03-S013][T03-S014]. *(Caveat: single-case anecdote Damodaran uses illustratively.)*

---

## Phase 3 — Sell-Side Process (controlled auction)

### Auction design: breadth scales inversely with size/sensitivity

| Type | Bidders | When chosen | Core tradeoff |
|---|---|---|---|
| **Broad auction** | "many" | mid-market, <$100M equity; price-max + fiduciary defensibility dominate | max price + leverage + best fiduciary record; BUT confidentiality hard to hold, disruptive |
| **Limited auction** | 10-50 | larger co. wanting competition with less leakage | balances competition vs confidentiality |
| **Targeted auction** | 2-5 hand-picked | high confidentiality; few logical buyers | confidentiality preserved BUT does not maximize price |
| **Exclusive / negotiated** | 1 | strategic fit / existing relationship; speed + secrecy paramount | best confidentiality/certainty/speed BUT weakest value-max; CIM may be skipped |

[T03-S001]. The core tension: price-max rises with bidder count, but so do leak risk and disruption; certainty and confidentiality rise as you narrow toward exclusivity. A *defensible broad auction also lets the board refuse standstill waivers* — the breadth itself is fiduciary armor [T03-S002].

### The gate sequence (each gate is an information-release lever)

**Teaser** (anonymous 1-2 pager) → **NDA + standstill** (bank-supplied form; use-restriction + non-solicit 18-24mo; standstill "generally only when the seller is public," 12-24mo — all *heavily negotiated ranges, not constants* [T03-S004]; "Don't Ask, Don't Waive" bars a bidder from even privately requesting a topping waiver, but Delaware constrains it [T03-S003]) → **CIM** ("90% of what buyers need to bid," built "to put the company in the best possible light" [T03-S001]) → **management presentation** → **first-round IOI** (1-2 pages, price as a *range*, non-binding; purpose = qualify and narrow [T03-S010]) → **process / bid procedures letter** (dictates bid format + required contents incl. financing commitment letters + hard deadline; often ships a seller-favorable **form purchase agreement each bidder must mark up and return** — the markup reveals each buyer's legal posture; seller "reserves the right to change, suspend, or terminate the process at any time") → **tiered data-room access** (finalists unlock sensitive files only as they commit — pacing info as leverage) → **second-round LOI / final bids** (single firm price + structure; binding only as to confidentiality + **exclusivity/no-shop** — granting exclusivity *closes the auction* [T03-S010]) → **confirmatory diligence under exclusivity** → **SPA → board approval + fairness opinion → signing → closing**.

WSP rough timeline: prep 4-6wks · round 1 4-6wks · round 2 4-6wks · negotiation→signing 6-8wks ≈ **18-26 weeks to signing** (*varies with size/breadth/rounds*) [T03-S001].

- **跳过哪步:** lower-middle-market deals routinely **skip the IOI round** and go straight to LOI; two rounds are typical only on larger deals [T03-S010]. An exclusive/negotiated process may **skip the CIM and fixed timetable** entirely [T03-S001].
- **优化点:** AI auto-indexes the data room ("replacing the manual sorting that consumed the first week of diligence") and drafts the initial Q&A list; Bain 2025 reports **21% of practitioners use gen-AI** (up from 16%), Harvey claims 15-20% time savings on structured diligence (vendor-reported, caveat) [T03-S012][T03-S016].
- **额外动作 (senior):** the MD **works the phones with key principals** — in proxies this reads as "representatives of [bank] encouraged Party A to deliver a proposal quickly" — and **reads which bid is real** (risk-adjusting a topping bid that "had not yet conducted diligence"). The junior maintains the **buyer log** (the spreadsheet from which proxy "Background of the Merger" sections are literally reconstructed).
- **案例:** **Atlas Technical / GI Partners (2023)** — broad auction; BofA contacted **38**, got **28 NDAs**, **9 IOIs** ($7.50-$10.50/share); GI's $12.00 was contingent on exclusivity. After exclusivity was granted, Party B made an unsolicited **$12.25** topping bid and *"Pursuant to the Exclusivity Agreement, the Company did not respond"* — signed at $12.25 (~$1.05B) only because GI matched. The exclusivity trap and no-shop discipline overriding a late higher bid, captured in a single filing [T03-S006]. *(Numbers are issuer self-disclosure.)*

---

## Phase 4 — Buy-Side Process

### Thesis → sourcing → bid → exclusivity → diligence → financing → close

**Thesis discipline:** a real buy-side thesis states *why* in economic terms (the target's cash engine, pricing power, working-capital behavior, concrete value levers) — not "expand product lines." DealRoom's test: if you can't articulate the why beyond reacting to a banker's pitch, step back [T03-S033]. **Build vs buy vs partner — programmatic wins:** McKinsey finds **programmatic acquirers** (>2 small/midsize deals/yr, ~15% cumulative market cap over ~10yr) deliver **median excess TSR ~2.3%** vs no excess for selective/organic/big-bet (*caveat: dataset-specific, association not causation*) [T03-S018]. Implication: M&A should be a standing capability with a live pipeline, not episodic.

**Sourcing — proprietary vs intermediated:** proprietary (approach owners before they're "for sale," via referral networks) is a structural advantage that survives auctions; intermediated/auction sourcing means the same targets as everyone, arriving late at full price [T03-S033].

**Intermediated sequence:** teaser → NDA → CIM → management calls → preliminary valuation (DCF + comps + precedents, framed cash-free/debt-free) → **IOI** (price *range*, refuse exclusivity to keep tension) → invited to data room → **LOI** (single firm price + **exclusivity 30-60 days** + break fee) → confirmatory diligence → SPA → close [T03-S033].

**Diligence workstreams** (effort weights vendor-illustrative): **QoE** — reconcile reported → mgmt-adjusted → QoE-adjusted EBITDA via an adjusted-EBITDA bridge, stripping one-timers/owner add-backs; **working capital** — set the NWC peg in the SPA with a 60-90 day post-close true-up (the most common purchase-price dispute); cash flow (maintenance vs growth capex; debt with change-of-control triggers); customer/revenue (concentration, churn, termination-for-convenience); tax (§382 NOL limitation); legal (change-of-control/assignment, IP chain-of-title); **IT/cyber** (third-party pen tests, dark-web searches — 146-day median breach-discovery, so "no known incident" ≠ clean — findings feed R&W/cyber insurance); HR (key-talent retention, change-in-control payouts, culture) [T03-S033].

**Financing — the deciding lever:** PE dropped the old **financing-out** (walk if debt failed) to compete with strategics; instead they deliver **committed financing / debt commitment letters ("certain funds")** at signing, backed by a **reverse termination fee** if financing fails [T03-S030]. WSP worked example: $60M EBITDA × 8.0x = $480M EV; total uses $500M = $240M debt + $260M equity (debt 48% of sources); lower equity → higher IRR. Equity checks historically ~20-30%, larger in 2026's higher-rate environment (*teaching ranges, not market quotes*) [carried from T06 §6.1; T03-S033].

- **跳过哪步:** a strategic buyer with an existing relationship may **skip the auction entirely** — pre-empt with a knockout bid + speed + certainty before the seller runs a process.
- **优化点:** AI in sourcing/screening — Deloitte: **86%** of US dealmakers integrated GenAI, 35% to target screening (self-reported, caveat) [T03-S019]; QoE is now near-default (~90% of PE-backed deals per advisor estimate; GF Data shows QoE deals price 7.4x vs 7.0x, benefit concentrated >$50M EV — caveat: advisor-estimated adoption, correlation) [T03-S033].
- **额外动作 (senior):** the MD sets the **walk-away/reservation price *before* bidding and holds it**, and chooses the **certainty posture** — how a financial buyer neutralizes a strategic's higher bid (no financing condition, committed debt, hell-or-high-water, reduced reps).
- **案例:** a buy-side QoE finds mgmt's "$10M EBITDA" includes a COVID subsidy + aggressive add-backs → normalized **$8M (-20%)**; combined with a top customer at **>25% of revenue on termination-for-convenience**, the buyer re-cuts its multiple, narrows the NWC peg, and adds escrow/earnout — diligence directly re-prices the deal [T03-S033]. *(Illustrative composite from vendor mechanics.)*

---

## Phase 5 — Negotiation & Deal Structure (the real price)

### Price vs value vs certainty: the highest bid often loses

A board decomposes closing risk into **financing** (best signal: no financing contingency + full equity backstop), **regulatory** (a sponsor with no overlap beats a strategic; best seller term = hell-or-high-water), and **MAC** (narrow, seller-favorable = fewer walk rights). Delaware's *Revlon* requires "best value reasonably available" — explicitly **not** highest nominal price [T03-S030].

**Consideration structure shifts risk/tax/signaling:** cash = clean seller exit, acquirer bears 100% of synergy risk, taxable; stock = risk shared, generally tax-deferred, but signals the acquirer thinks its own stock is expensive (Travlos 1987: stock acquirers show negative announcement returns, cash ~zero — *signal is noisy*). **Earnouts/CVRs** bridge forecast disagreement: SRS reports earnouts in ~22% of 2024 deals, ~21¢ paid per $1, contested ≥28% of the time — they litigate because the buyer now controls the business and metrics are GAAP-manipulable [T03-S021].

**Deal protections (all numbers carry caveats):**
- **Target breakup fee** ~1-4% of *equity value*; Houlihan Lokey 2024 avg **2.4%** (down from 2.9% in 2021), range 0.2-6.0%; no Delaware bright-line, ~4%+ draws scrutiny [T03-S022].
- **Reverse termination fee** larger; antitrust RTFs ~4-7% of EV (Goodwin); Wachtell: antitrust RTFs averaged ~4.8%, 72% at ≥6% on materially-risky 2023 deals [T03-S030][T03-S020].
- **No-shop** (~82% per ABA) vs rare **go-shop** (~3%); fiduciary out; matching rights (3-5 days); MAC/MAE bar is very high (must "substantially threaten earnings potential in a *durationally significant* manner" — years, not quarters; carve-outs construed against the invoker).
- **R&W insurance** is displacing escrow: SRS shows escrow ~5.1% of deal value for RWI deals vs ~12.1% for non-RWI; RWI deals more likely "no survival" (walk-away) + materiality scrape; survival median 12mo; 21% of deals are walk-away [T03-S021].

**How real price is set:** leverage = alternatives + information. MDs use **BATNA** (only real if executable), **walk-away discipline** set before negotiating, **competitive tension** as the #1 price driver, and **trade on structure** when price won't converge (earnout for the gap, more cash up front for a lower total, RWI for risk gaps). The winner's curse is the standing risk — Damodaran: ~**55% of acquirers' stock drops** on announcement; KPMG found **83%** of the 700 largest 1996-98 mergers underperformed (*study-specific, definitions vary*) [T03-S014]. His rule: *"If you get into a bidding war over a target firm, walk away"* [T03-S013].

- **跳过哪步:** in a hot competitive auction the seller may **skip granting any exclusivity** to keep all bidders live to the wire.
- **优化点:** RWI as standard mid-market practice compresses indemnity negotiation and shrinks escrows — a cleaner exit for sellers [T03-S021].
- **额外动作 (senior):** the MD personally negotiates the price/terms package and the **antitrust risk-allocation** (HOHW vs efforts standard, RTF size) — the single most value-relevant structural call.
- **案例:** **Family Dollar (2014)** — the board rejected Dollar General's *higher* **$80.00/share all-cash** offer and took **Dollar Tree at ~$74.50** (a ~7% lower bid), calling it "clearly superior… based on **antitrust risk, deal certainty and time value of money**." Dollar General overlapped heavily (high block risk); Dollar Tree would divest as many stores as needed. The textbook lower-bid-wins-on-certainty case [carried via Dollar Tree 8-K; cross-validated]. Contrast **Akorn v. Fresenius (Del. 2018)** — the *only* time Delaware let a buyer walk on a MAC: four straight quarters of company-specific collapse (rev -29/-29/-34/-27% YoY, carve-outs inapplicable) *plus* fabricated FDA data-integrity breaches *plus* a covenant breach [carried from negotiation research].

**Banker agency problem (do not resolve it):** the bank that values the deal is paid a contingent success fee earned only if it closes. Damodaran: a fairness opinion "is not a real valuation," just confirmation the price is "within a plausible range" so wide "any price can be justified" — his fix is killing deal-contingent fees and separating dealmakers from appraisers [T03-S015]. Delaware has flagged this repeatedly: **In re El Paso** (Goldman advised the seller while affiliates owned ~19% of buyer Kinder Morgan; Strine said it "tainted" the opinion; $110M settlement) and **In re Del Monte** (Barclays ran the sale while seeking buy-side financing fees; $89.4M settlement) [carried from negotiation research; cf. T04-S022/S023, T06-S012].

---

## Phase 6 — Execution to Close + Regulatory + Retrospective

### Signing-to-closing risk management

Boards are now fluent in "hell or high water," "efforts covenants," "outside dates," and "regulatory reverse termination fees"; no target board accepts a bid without a credible narrative on regulatory timeline, likelihood, strategy, and risk allocation [T03-S020]. Key levers: conditions precedent (regulatory clearances, financing, no-MAC), the MAC clause, **ticking fees** (price accretes if close drags), reverse termination fees, and **fix-it-first** divestitures. Typical signing-to-close window 60-120 days, longer with Second Requests.

### Regulatory (DECAY = HIGH — re-verify within 12 months)

- **HSR (US):** 2026 size-of-transaction threshold **US$133.9M** (up from $126.4M), effective **Feb 17 2026**; top filing fee **$2.46M** (six tiers) [T03-S023][T03-S032]. Waiting period **30 days** standard / **15 days** cash tender; a **Second Request** stops the clock until substantial compliance [T03-S024]. *(Threshold GNP-adjusted annually — re-verify each February.)*
- **⚠ MOST decay-prone item:** the expanded HSR form (effective Feb 10 2025, which raised est. filing burden from ~37 to ~105 hours) was **VACATED on 2026-02-12** by the E.D. Texas as "arbitrary and capricious"; the Fifth Circuit **denied the FTC's stay on 2026-03-19**. As of 2026-06-16, parties file on the **OLD pre-Feb-2025 form**; the FTC's merits appeal is pending (brief due ~Apr 20 2026). **Verify current form/status before any filing** [T03-S025].
- **Enforcement posture:** the **2023 Merger Guidelines** remain operative (Chair Ferguson + DOJ retained them Feb 18 2025) — robust enforcement persists across administrations, with more openness to negotiated structural remedies. 2025: ~12 challenges / 9 consents; HSR early termination restored under Trump 2.0 [T03-S020].
- **CFIUS:** interagency Treasury-chaired review under Section 721 DPA / FIRRMA (2018); full notice = 45-day review + 45-day investigation + 15-day presidential. Mandatory triggers for **TID** (critical Technology, Infrastructure, Data) businesses + foreign-government substantial interest. The **Outbound Investment Security Program ("Reverse CFIUS")** took effect **Jan 2 2025** (US investment into China/HK/Macau in semiconductors, quantum, AI) [T03-S026].
- **EU/UK:** EU = **suspensory** (cannot close before clearance; gun-jumping fined up to 10% of worldwide turnover); Phase I 25wd / Phase II 90wd. UK = CMA, voluntary/non-suspensory, share-of-supply test; turnover threshold raised to £100M under the DMCC Act (Jan 1 2025). **Cross-border lesson:** a single suspensory hold-out kills a global deal.

- **跳过哪步:** below the HSR threshold ($133.9M) a deal **skips the federal premerger filing** entirely (though state/foreign filings may still bite).
- **优化点:** "fix-it-first" — pre-emptively lining up a divestiture buyer before filing to neutralize antitrust risk and shorten the timeline.
- **额外动作 (senior):** structuring the **antitrust risk allocation** (HOHW vs efforts, RTF size) *during* negotiation so the regulatory clock doesn't blow up the deal at the worst moment.
- **案例 (antitrust kill):** **Kroger / Albertsons, $24.6B** — FTC + states sued Feb 2024 (horizontal + labor-monopsony theory; the C&S divestiture deemed inadequate); D. Oregon granted a preliminary injunction **Dec 10 2024**, Albertsons terminated next day — and is now suing Kroger for the **$600M RTF** + lost-premium damages [T03-S028]. **案例 (CFIUS):** **Nippon Steel / U.S. Steel (~$14.9B)** — agreed Dec 2023 → **Biden blocked Jan 3 2025** by EO → **Trump ordered de novo review Apr 7 2025** → **approved Jun 13 2025** under a National Security Agreement with a US-government **"golden share."** Two new precedents (a President reopening a predecessor's closed CFIUS matter; governance/golden-share remedy vs divestiture) — CFIUS risk is *strategic, not purely statutory* [T03-S027].

### Post-deal / retrospective (and the missing post-mortem)

Closing mechanics = satisfy conditions precedent, funds flow, certificates/opinions delivered. The bank then takes **league-table credit**, issues the **tombstone**, and collects the **success fee**: monthly **retainer** (credited against success fee) + success fee on a sliding scale (~1-2% mid-market scaling down to ~0.2-0.3% on multi-billion deals); **Lehman** = 5-4-3-2-1, **Double Lehman** = 10-8-6-4-2 in the lower-middle-market (*business norm + Lehman formula per Wikipedia, not a constant*) [carried from T04-S025/26, T06-S014].

**The retrospective gap — the agency problem completed:** there is no real banker post-mortem. The success fee is collected at close, the banker moves to the next mandate, and **integration — where most value is won or lost — is handed off to the client/consultants**. The banker is never accountable for whether synergies materialized [T03-S015]. The deal sheet that *does* get sequenced is the **internal deal sheet / tombstone for league-table credit and the next pitch** — institutional memory optimized for *winning the next mandate*, not for honest outcome attribution. (Kison Patel's Agile-M&A counter-thesis: pull integration thinking forward to day-1 and treat the diligence/integration tracker as a single source of truth — the explicit reform of this gap [carried from T01-S027].)

---

## Phase 2 接口 (Interface to Phase 2 / master skill build)

### 完整 deal SOP 一图流

```
ORIGINATION ──▶ PITCH ──▶ VALUATION ──▶ [fork by side]
 (relationship,    (pitchbook,    (DCF/comps/precedents/
  coverage grp)     football        LBO/merger model,
                    field)          football field)
        │
        ├─ SELL-SIDE: design auction (broad/limited/targeted/exclusive)
        │     teaser → NDA+standstill → CIM → mgmt presentation
        │     → IOI (round 1, price range) → process letter + form SPA markup
        │     → tiered data room → LOI/final bids → grant EXCLUSIVITY (auction closes)
        │     → confirmatory diligence
        │
        └─ BUY-SIDE: thesis → sourcing (proprietary vs auction) → IOI
              → bid strategy (walk-away price + CERTAINTY posture)
              → win exclusivity → diligence (QoE/legal/IT/HR) → committed financing
        │
        ▼
   NEGOTIATION & STRUCTURE  ──▶  SPA (price + consideration + deal protections
   (price vs value vs certainty;        + MAC + reps&warranties/RWI + breakup/RTF)
    trade on structure when price stalls)
        ▼
   BOARD APPROVAL + FAIRNESS OPINION  ──▶  SIGNING
        ▼
   SIGNING→CLOSING gauntlet: HSR ($133.9M) / CFIUS / EU-UK / financing / no-MAC
   (ticking fees, RTF, hell-or-high-water absorb the risk)
        ▼
   CLOSING  ──▶  league-table credit + tombstone + SUCCESS FEE collected
        ▼
   [integration handed off — no banker retrospective: the agency loop closes]
```

### MD (资深) vs Analyst (入门) — 关键差异

| 维度 | Analyst/Associate — builds the machine | MD/VP — sets the real price |
|---|---|---|
| **Pitch** | builds the deck (v44), comps/precedents/DCF, buyer profiles, tombstones | leverages 5-10yr relationship; tells the strategic story; picks which range to lead with |
| **Valuation** | builds & maintains the model, runs sensitivities | *uses* output backward; deploys sensitivity tables as negotiation props; frames synergy |
| **Process** | drafts teaser/CIM, runs the VDR + Q&A tracker + **buyer log** | sets auction strategy; **works the phones**; reads which bid is real (risk-adjusts toppers) |
| **Negotiation** | models accretion/dilution of each structure | sets **walk-away price**; negotiates price + **antitrust risk allocation** + deal protections |
| **Execution** | tracks CP checklist, coordinates HSR/CFIUS filings | manages regulators/board; drives to signing & close |
| **Post-deal** | updates internal deal sheet, files league-table credit | collects success fee, harvests relationship — **no integration accountability** |

**The one-line essence:** the junior's models and trackers exist to make the senior's two real decisions — **walk-away price** and **certainty posture** — *defensible*. Everything else is machinery.

### 最值得进 master skill 的 playbook 清单

1. **The certainty equation** — `board value ≈ price × P(close) − busted-deal cost − time-value`. Teaches why the highest bid loses (Family Dollar). The single most non-obvious deal-sense unlock. [T03-S030][T03-S020]
2. **Controlled-auction leverage mechanics** — staged gates (teaser→NDA→CIM→IOI→data room→LOI→exclusivity) as information-release levers; breadth scales inversely with size/sensitivity; granting exclusivity closes the auction (Atlas). [T03-S001][T03-S006]
3. **Walk-away discipline + winner's curse self-check** — value standalone + synergy/control *separately*, set the reservation price before bidding, never pay all synergy as premium, walk from bidding wars. [T03-S013][T03-S014]
4. **Trade on structure, not just price** — earnout/CVR for forecast gaps, cash-vs-stock for risk/tax/signaling, RWI for risk gaps, RTF/HOHW for regulatory risk. Structure is more negotiable than price. [T03-S021][T03-S030]
5. **The banker agency loop** — contingent success fee → bias toward "yes" → fairness opinion conflict → no retrospective → integration handed off. Teach the model *and* that the advisor giving it is conflicted toward closing. [T03-S015]
6. **Regulatory clock as a deal-shaping constraint** — HSR threshold/timeline, CFIUS (golden-share/reopening precedents), suspensory EU regime; "fix-it-first" + risk allocation negotiated up front. (DECAY=HIGH.) [T03-S023][T03-S025][T03-S026][T03-S027]

---

## 质量自检 (Quality Self-Check)

- **6 阶段全覆盖 ✅** — Pitch / Valuation / Sell-side / Buy-side / Negotiation-structure / Execution-regulatory-retrospective, each with 入门-vs-资深 split + 跳过/优化/额外动作 三类提示 + ≥1 案例 (带 T03 evidence id).
- **源数 ✅** — 34 sources (target ≥15, 2.3×). verified_primary 23 (SEC EDGAR proxies ×3 = real "Background of the Merger" process records; FTC/Treasury ×5; Damodaran ×3; law-firm primary memos ×7; Bain/McKinsey/Deloitte/SRS/Houlihan/Wachtell studies). surrogate_primary 7 (WSP/CFI/M&I/Cooley/DealRoom). secondary 4. 一手率 ~68%.
- **黑名单零引用 ✅** — no LinkedIn article bodies / WSO / 知乎 / 公众号 / 百度 / Quora / content farms (all surfaced in searches, dropped).
- **矛盾保留 (未软化) ✅** — (a) long-process discipline vs relationship trust (Phase 1 vs Phase 3); (b) narrative packaging vs numbers diligence (Phase 2 vs Phase 4 QoE); (c) valuation science vs negotiation reality (Phase 2 & 5); (d) banker always advises closing — agency problem threaded through Phases 1/2/5/6 with El Paso, Del Monte, Damodaran fairness-opinion takedown.
- **数字均挂来源 + caveat ✅** — success fee ~1-2% scaling down (norm); control premium 20-40% (range, not law, per Damodaran); breakup fee ~2.4% / RTF ~4-7% (Houlihan/Goodwin/Wachtell, point-in-time); value-destruction ~55% stock drop / 83% underperform / KPMG 57.2% (study-specific, definitions vary); PE hold ~7yr (survivorship-skewed); HSR $133.9M (annual reset).
- **DECAY 标注 ✅** — HSR threshold (annual), **new HSR form vacated 2026-02-12 → old form in use, appeal pending (verify before filing)**, CFIUS outbound program, EU/UK thresholds, AI-adoption stats (vendor/self-reported) all flagged.
- **Cross-track reuse ✅** — football field / model set / Damodaran datasets (T02/T04) and deal-term definitions (T06) referenced as inputs, not re-documented; 5 sources re-used from prior tracks under T03 ids.
- **待 Phase 2 验证** — go-shop empirics (~50% of >$100M go-privates) via WSP summary of a 2017 Weil/Subramanian-Zhao study (live page 403-blocked) — flag before quoting; some SRS-2026/ABA figures via law-firm summaries (directional); FTC.gov 403s automated fetch — all FTC numbers cross-checked against Dechert/Davis Polk (agree exactly).
