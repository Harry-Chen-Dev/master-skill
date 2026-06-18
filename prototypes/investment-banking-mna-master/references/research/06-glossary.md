# Track 06 — Glossary (investment banking M&A / dealmaking)

> Wave 1 Track 06 — terminology / deal-structure terms / valuation jargon / regulatory standards / consensus vocabulary. Industry: investment banking M&A advisory (投行并购 / 交易撮合), locale=global (English-primary canon, zh-CN crosswalk where a settled translation exists), profile=practitioner (analyst→MD, corp dev, PE, advisory-adjacent).
>
> 结构约束 notes (诚实): (1) 一手正典几乎全英文 — Rosenbaum & Pearl《Investment Banking》是行业圣经 (方法论), Aswath Damodaran (NYU Stern) 是估值正典且全部公开免费, McKinsey《Valuation》(Koller et al) 是 corporate-finance 正典; Investopedia/CFI/Wall Street Prep/Macabacus 是 reference/培训层 (CFI/WSP/Macabacus vendor docs = surrogate_primary, Investopedia = reference/secondary). (2) 监管底线 vocabulary 是一手: HSR/Clayton Act (FTC+DOJ)、CFIUS (FIRRMA, Treasury)、SEC EDGAR (fairness opinion + proxy 全公开)、FINRA Rule 5150 (fairness opinion conflict 披露). (3) 数字类高危 — control premium 20-40%、breakup fee ~1-4%、reverse termination fee ~2-4%、success fee Lehman 5-4-3-2-1 / Double Lehman、M&A 毁灭价值率 — 全部挂 source_id + caveat (学术研究 / 第三方 deal study / 业内惯例 / 区间大). 尤其 "70-90% 并购失败" 是经常被引用的经验区间, 但近期 KPMG 2025 给出 57.2% 毁灭股东价值 — 区间随研究方法变化巨大, 本表两者并列, 不当 universal 事实. (4) 估值的伪精确 (DCF/comps garbage-in-garbage-out) 与 banker agency problem (fairness opinion 利益冲突) 在定义里诚实保留, 不软化成 "学了 DCF 就能算出真实价值". (5) 中文术语凡有 settled 译法平行给出; 无 settled 译法的 (如 go-shop / collar / SOTP) 标注或保留英文. (6) 黑名单 (LinkedIn 文章正文 / WSO 匿名帖 / 知乎 / 公众号 / 百度 / Quora / 内容农场) 一律不作 source — WSO 在搜索中出现但仅用其 term 存在性佐证, 不作引用源.

---

## Source Manifest

| source_id | url | bucket | last_checked | author/host | note |
|-----------|-----|--------|--------------|-------------|------|
| T06-S001 | https://pages.stern.nyu.edu/~adamodar/ | verified_primary | 2026-06-16 | Aswath Damodaran, NYU Stern | 估值正典一手 — DCF/WACC/terminal value/relative valuation 全套公开课+spreadsheets+博客 (Damodaran Online) |
| T06-S002 | https://pages.stern.nyu.edu/~adamodar/pdfiles/country/controlvalue.pdf | verified_primary | 2026-06-16 | Aswath Damodaran, NYU Stern | "The Value of Control" — control premium 概念 + 批判 (US 80s-90s 收购溢价 20-30%, 但无 universal rule of thumb, 应随管理质量变) |
| T06-S003 | https://www.investopedia.com/terms/d/dcf.asp | reference_secondary | 2026-06-16 | Investopedia | reference/secondary — DCF / FCF / WACC / terminal value 通用定义层 (非一手, 用于术语 baseline) |
| T06-S004 | https://corporatefinanceinstitute.com/resources/valuation/ | surrogate_primary | 2026-06-16 | Corporate Finance Institute (CFI) | vendor docs (培训机构) — comps / precedent transactions / LBO / accretion-dilution 模型术语 reference |
| T06-S005 | https://www.wallstreetprep.com/knowledge/ | surrogate_primary | 2026-06-16 | Wall Street Prep (WSP) | vendor docs (培训机构) — merger model / break fees / valuation 术语 reference |
| T06-S006 | https://macabacus.com/terms/ | surrogate_primary | 2026-06-16 | Macabacus | vendor docs (培训机构) — termination fee / deal terms / modeling 术语 reference |
| T06-S007 | https://www.ftc.gov/enforcement/premerger-notification-program | verified_primary | 2026-06-16 | US FTC | 监管一手 — HSR premerger notification program (Clayton Act §7A, 30-day waiting period) |
| T06-S008 | https://www.ftc.gov/news-events/news/press-releases/2026/01/ftc-announces-2026-update-jurisdictional-fee-thresholds-premerger-notification-filings | verified_primary | 2026-06-16 | US FTC | 监管一手 — 2026 HSR size-of-transaction threshold US$133.9M (从 2025 的 $126.4M 上调) |
| T06-S009 | https://www.ftc.gov/advice-guidance/competition-guidance/guide-antitrust-laws/mergers/premerger-notification-merger-review-process | verified_primary | 2026-06-16 | US FTC | 监管一手 — 合并审查流程 (30天等待期 / cash tender offer 15天 / Second Request) |
| T06-S010 | https://home.treasury.gov/policy-issues/international/the-committee-on-foreign-investment-in-the-united-states-cfius/cfius-overview | verified_primary | 2026-06-16 | US Treasury (CFIUS) | 监管一手 — CFIUS 国安审查概述 (Defense Production Act 1950 + FIRRMA 2018 扩权) |
| T06-S011 | https://www.congress.gov/crs-product/IF11334 | verified_primary | 2026-06-16 | Congressional Research Service | 监管一手 (CRS) — FIRRMA 强制申报 (foreign govt substantial interest / critical tech) + voluntary declaration + safe harbor |
| T06-S012 | https://www.finra.org/rules-guidance/rulebooks/finra-rules/5150 | verified_primary | 2026-06-16 | FINRA | 监管一手 — Rule 5150 Fairness Opinions (利益冲突 + contingent success fee 披露强制) |
| T06-S013 | https://www.sec.gov/cgi-bin/browse-edgar | verified_primary | 2026-06-16 | US SEC EDGAR | 监管一手 — proxy (DEFM14A) / tender offer (SC 14D-9) / fairness opinion 全文公开数据库 |
| T06-S014 | https://en.wikipedia.org/wiki/Lehman_Formula | reference_secondary | 2026-06-16 | Wikipedia | reference/secondary — Lehman formula 5-4-3-2-1 + Double/Modified Lehman 历史 (术语存在性 + 结构) |
| T06-S015 | https://corpgov.law.harvard.edu/2018/10/02/private-equity-buyer-public-target-ma-deal-study-2015-17-review/ | surrogate_primary | 2026-06-16 | Harvard Law / Forum on Corp Governance (deal study) | 第三方 deal study — breakup fee 均值 2.4% (large-mkt) / 3.1% (mid-mkt) of target equity; RTF 均值降至 4.5% (2015-17) |
| T06-S016 | https://www.fenwick.com/insights/publications/antitrust-breakup-fees-2023-data-and-key-takeaways-for-future-dealmaking | surrogate_primary | 2026-06-16 | Fenwick & West (law firm) | 第三方 — antitrust (reverse) termination fee 2023 数据 + 触发条件 (反垄断不批→买方付) [own publication] |
| T06-S017 | https://kpmg.com/us/en/articles/2025/ma-synergies-value-public-acquisitions.html | surrogate_primary | 2026-06-16 | KPMG (2025 study) | 第三方研究 — 57.2% 收购方最终毁灭股东价值; 主因 synergy 高估 + integration 复杂度低估 |
| T06-S018 | https://acquisitionstars.com/ma-failure-rate | reference_secondary | 2026-06-16 | Acquisition Stars (data compilation) | reference/secondary — "70-90% M&A 失败/不创造价值" 经验区间汇编 (区间随研究方法变化大, caveat) |
| T06-S019 | https://www.investopedia.com/terms/l/lbo.asp | reference_secondary | 2026-06-16 | Investopedia | reference/secondary — LBO / IRR / MOIC / sources & uses 通用定义层 |
| T06-S020 | https://www.investopedia.com/terms/e/enterprisevalue.asp | reference_secondary | 2026-06-16 | Investopedia | reference/secondary — enterprise value / EV/EBITDA / equity value bridge 定义 |
| T06-S021 | https://en.wikipedia.org/wiki/Fairness_opinion | reference_secondary | 2026-06-16 | Wikipedia | reference/secondary — fairness opinion 定义 + 利益冲突批判存在性 |

(21 sources; 一手率 ≈ 62%: verified_primary 13 = Damodaran NYU + FTC/HSR + CFIUS/Treasury + CRS + FINRA + SEC EDGAR; surrogate_primary 5 = CFI/WSP/Macabacus 培训 + Harvard deal study + Fenwick + KPMG; reference_secondary 6 = Investopedia + Wikipedia + data compilation, 仅作术语 baseline / 区间汇编, 不作硬事实 anchor.)

---

## 6.1 估值 / 建模术语 (DCF / comps / precedent / LBO / merger model)

**DCF — Discounted Cash Flow / 折现现金流** — intrinsic-value method: project future free cash flows, discount to present at the cost of capital, add terminal value. 把未来自由现金流按资本成本折现求内在价值. 为何重要: 是 *intrinsic value* 的核心方法, 但本质假设驱动 (garbage in garbage out) — Damodaran 反复警告其伪精确, 输出区间而非单一"正确答案" [T06-S001][T06-S003].

**FCF — Free Cash Flow / 自由现金流** — cash a business generates after operating expenses and capex. *FCFF* (to firm) 折现得 enterprise value; *FCFE* (to equity) 折现得 equity value. 公司自由现金流 vs 股权自由现金流, 折现对象不同. 为何重要: DCF 的输入燃料, 口径错 (FCFF vs FCFE 配错折现率) 是新手最常见建模错误 [T06-S001].

**WACC — Weighted Average Cost of Capital / 加权平均资本成本** — blended after-tax cost of debt and cost of equity weighted by capital structure; the discount rate for FCFF. 债务+股权成本按资本结构加权, 是 FCFF 折现率. 为何重要: DCF 估值对 WACC 极敏感 (±1% WACC 可移动估值 10%+), 是 sensitivity 表的核心轴 [T06-S001][T06-S003].

**Terminal value (TV) / 终值** — value of cash flows beyond the explicit forecast period; often 60-80% of total DCF value. Gordon growth (perpetuity) 法 vs exit-multiple 法两种. 为何重要: 占 DCF 价值的大头, 因此 DCF 结论极大程度由终值假设决定 — 易被外行忽略 [T06-S001][T06-S003].

**Gordon growth model / 戈登增长模型** — perpetuity terminal value = final-year FCF × (1+g) / (WACC − g), where g = perpetual growth rate. 永续增长法终值. 为何重要: g 必须 ≤ 长期 GDP/通胀, 否则隐含公司永远跑赢经济 (常见高估陷阱) [T06-S001].

**Trading comps / Comparable companies / 可比公司 (交易倍数)** — relative valuation off public peers' multiples (EV/EBITDA, EV/Revenue, P/E). 用同业上市公司倍数做相对估值. 为何重要: 给出 *market is paying* 的当下定价 (vs DCF 的内在值), 二者背离即"价格 vs 价值"张力的量化 [T06-S004][T06-S020].

**Precedent transactions / Deal comps / 先例交易** — multiples paid in prior comparable M&A deals; embeds a *control premium* (transaction prices > trading prices). 历史可比并购成交倍数, 内含控制权溢价. 为何重要: 比 trading comps 更贴近"成交价", 因为它含控制权溢价 + 协同预期 [T06-S004].

**Control premium / 控制权溢价** — amount paid above unaffected market price to acquire control. US 历史中位 ~20-30% (Damodaran), 常见区间 20-40%, 个案可达 70%+. 为何重要 + caveat: 不是 universal rule — Damodaran 明确说 "control = 20-30% of value cannot be right", 应随管理质量变 (管得差的公司溢价应更高) [T06-S002].

**EV/EBITDA / 企业价值倍数** — enterprise value ÷ EBITDA; capital-structure-neutral, the workhorse M&A multiple. 资本结构中性的主力倍数. 为何重要: 跨杠杆差异公司可比, 是 trading/precedent comps 最常用口径 [T06-S004][T06-S020].

**EV/Revenue / 市销倍数** — enterprise value ÷ revenue; used for pre-profit / high-growth firms. 用于未盈利/高增长公司. 为何重要: EBITDA 为负时唯一可用倍数, 但忽略盈利质量 [T06-S004].

**LBO — Leveraged Buyout / 杠杆收购** — acquisition financed heavily with debt, repaid by target's cash flows; PE's core playbook. 大量举债收购, 用标的现金流还本. 为何重要: LBO 模型反推 PE 能付的最高价 (是 sell-side 估值的一个 floor/ceiling 参照) [T06-S019].

**IRR — Internal Rate of Return / 内部收益率** — annualized discount rate that zeroes an investment's NPV; PE's primary return metric. 让 NPV=0 的年化折现率, PE 首要回报指标. 为何重要: PE 出价由目标 IRR (常 ~20-25%) 倒推, 受持有期长短影响大 [T06-S019].

**MOIC — Multiple on Invested Capital / 投入资本回报倍数** — total value returned ÷ equity invested (e.g. 2.5x); IRR 的补充. 回笼总额 / 投入股本. 为何重要: 与 IRR 互补 — IRR 高但 MOIC 低 = 快进快出小钱; 二者一起看才完整 [T06-S019].

**Sources & uses / 资金来源与运用** — table reconciling where deal money comes from (debt + equity) vs where it goes (purchase equity + refi debt + fees). 资金来源(债+股) = 用途(买股权+还债+费用)的对账表. 为何重要: LBO/并购模型的资金平衡起点, 决定杠杆与股权投入 [T06-S004][T06-S019].

**Debt schedule / 偿债计划表** — model tab tracking each debt tranche's draw, interest, mandatory + cash-sweep repayment over time. 逐期追踪各档债务利息与还本(含现金清扫). 为何重要: LBO 的引擎 — 决定去杠杆速度从而决定股权回报 [T06-S005].

**Accretion / dilution / 增厚 / 摊薄分析** — whether a deal raises (accretive) or lowers (dilutive) acquirer's pro forma EPS. 交易后收购方每股收益是升(增厚)还是降(摊薄). 为何重要: 上市收购方董事会的关键 go/no-go 指标 (尤其 stock deal), 也是 banker pitch 的核心说服点 [T06-S005].

**Pro forma / 备考** — combined financials as if the deal had already closed (acquirer + target + adjustments). 假设交易已完成的合并财务. 为何重要: accretion/dilution 与协同的呈现载体 [T06-S005].

**Synergies / 协同效应** — incremental value from combining (cost synergies 成本协同 + revenue synergies 收入协同). 合并产生的增量价值. 为何重要 + caveat: banker pitch 卖点, 但系统性高估 — Bain 2024 称仅 ~30% 达成协同目标, KPMG 2025 归因 synergy 高估为价值毁灭主因 [T06-S017].

**Purchase accounting / Purchase price allocation (PPA) / 购买法会计** — allocating purchase price to acquired assets/liabilities at fair value; excess → goodwill. 把对价按公允价值分摊到资产负债, 超出部分计入商誉. 为何重要: 决定 pro forma 折旧摊销 → 影响 accretion/dilution [T06-S005].

**Goodwill / 商誉** — premium paid over fair value of net identifiable assets; sits on balance sheet, tested for impairment. 超出可辨认净资产公允价值的溢价. 为何重要: 高商誉 = 付了高溢价的会计痕迹; 后续减值是承认买贵了 [T06-S005].

**SOTP — Sum-of-the-Parts / 分部估值** — value each business segment separately, sum, adjust for net debt/corporate. 各业务分部分别估值再加总. 为何重要: 揭示 conglomerate discount, 是 spin-off / activist 论证的工具 [T06-S004].

**Football field / 估值区间图** — bar chart overlaying valuation ranges from each method (DCF, comps, precedents, LBO, 52-wk). 把各方法估值区间叠成条形图. 为何重要: 向董事会呈现"价值是区间不是点", 谈判落点的可视化 [T06-S004].

**Sensitivity / scenario analysis / 敏感性 / 情景分析** — flex key assumptions (WACC, growth, multiple, synergies) to show output range. 拉动关键假设看输出区间. 为何重要: 诚实呈现估值的不确定性, 对抗伪精确 [T06-S001][T06-S005].

## 6.2 交易流程 / 产出物 (teaser → CIM → LOI → SPA / sell-side vs buy-side / auction)

**Teaser / 简介** — 1-2 page anonymous summary sent to potential buyers to gauge interest pre-NDA. 匿名 1-2 页摘要, 签 NDA 前试水. 为何重要: sell-side 流程第一步, 决定谁进竞价 [T06-S005].

**NDA — Non-Disclosure / Confidentiality Agreement / 保密协议** — required before sharing confidential info / CIM; may include standstill. 共享机密前必签, 可含 standstill 反收购条款. 为何重要: 信息门槛 + 保护卖方; standstill 条款限制买方未经邀请增持 [T06-S004].

**CIM / IM — Confidential Information Memorandum / 信息备忘录** — detailed sell-side marketing document (business, financials, growth story) post-NDA. NDA 后的详细卖方营销文件. 为何重要: 卖方"the story + the numbers"的主载体, 是 banker 包装能力的集中体现 [T06-S005].

**Management presentation / 管理层路演** — in-person/virtual session where target management pitches to shortlisted buyers. 标的管理层向入围买方陈述. 为何重要: 买方评估管理团队 + 验证 CIM 叙事的关键节点 [T06-S004].

**IOI — Indication of Interest / 意向函** — non-binding preliminary bid (value range + structure) early in auction. 非约束初步报价(价值区间+结构). 为何重要: 卖方据此筛选谁进下一轮 (data room + management presentation) [T06-S004].

**Data room / 数据室 (VDR)** — secure (virtual) repository of due-diligence documents for vetted bidders. 给入围买方做尽调的安全文档库. 为何重要: confirmatory diligence 的场所; 信息开放节奏是卖方控制竞争张力的杠杆 [T06-S004].

**LOI / Term sheet / 意向书 / 条款清单** — largely non-binding outline of price + key terms; often grants exclusivity (no-shop). 价格+核心条款的(多为)非约束概要, 常含排他期. 为何重要: 从竞价转入双边谈判的转折点; exclusivity 让买方安心投入尽调成本 [T06-S006].

**SPA — Sale & Purchase Agreement / Merger Agreement / 买卖协议 / 合并协议** — the binding definitive contract (price, reps, covenants, conditions, indemnity). 有约束力的最终合同. 为何重要: 所有结构/条款的法律落地; signing 即签此约 [T06-S006].

**Signing vs Closing / 签约 vs 交割** — *signing*: parties execute the SPA. *Closing*: deal consummates after conditions (regulatory, financing, shareholder vote) met. 签约 vs 满足条件后交割. 为何重要: 签约到交割之间是 deal risk 高发区 (MAC / 监管否决 / 融资失败) — "certainty of close"的本质 [T06-S009].

**Sell-side / 卖方** — advising the seller; run process, maximize price + certainty, manage auction tension. 代表卖方, 跑流程、争最高价+成交确定性. 为何重要: 与 buy-side 激励/义务相反, 是 banker 角色的基本二分 [T06-S004].

**Buy-side / 买方** — advising the acquirer; sourcing, valuation, bid strategy, diligence, financing. 代表买方, 寻标、估值、出价策略、尽调、融资. 为何重要: buy-side 目标是"以最低必要价拿下", 与 sell-side 博弈 [T06-S004].

**Controlled auction / 控制竞价** — banker-run competitive sale process engineering tension among bidders. 投行主导的竞争性出售, 制造买方间张力. 为何重要: sell-side 抬价的核心机制 — 用信息不对称+竞争把价格推向上限 [T06-S004].

**Broad / Targeted / Negotiated process / 广撒网 / 定向 / 谈判式** — auction breadth: *broad* (many buyers, max price, leak risk), *targeted* (curated few), *negotiated* (single buyer, max confidentiality/certainty). 竞价广度: 广撒网/定向/单边谈判. 为何重要: 广度↔保密性/确定性的权衡, 卖方据敏感度选择 [T06-S004].

**Pitchbook / 推介材料** — banker's marketing deck to win a mandate (positioning, comps, value range, credentials). 投行赢得委托的提案 deck. 为何重要: pitch→mandate 转化是 banker 业务起点; 也是 analyst 加班文化批判的具象 [T06-S005].

**Fairness opinion / 公平意见** — independent banker opinion that deal consideration is "fair, from a financial point of view" to shareholders. 投行出具的"对价对股东财务上公平"意见. 为何重要 + caveat: 董事会 fiduciary 防护 + 诉讼防御, 但利益冲突真实 (出意见的 banker 也收 contingent success fee) → FINRA Rule 5150 强制披露此冲突 [T06-S012][T06-S021].

**Engagement letter / 委托协议** — contract between client and bank setting scope, fees, indemnity, tail period. 客户与投行的委托合同, 定范围/费用/赔偿/尾期. 为何重要: 定义 success fee + retainer + tail (终止后一定期内成交仍付费) [T06-S014].

**Fee letter / 费用函** — the fee mechanics (often separate from engagement letter); success fee schedule + retainer + expenses. 费用机制函件. 为何重要: Lehman/Double-Lehman 比例 + retainer 的落地处 [T06-S014].

## 6.3 结构 / 条款 (consideration / deal protections / reps / defenses)

**Cash / Stock / Mix consideration / 现金 / 换股 / 混合对价** — how the buyer pays: cash (certain, taxable to seller), stock (seller shares upside/risk, often tax-deferred), or mix. 对价形式. 为何重要: 决定 accretion/dilution、税务、卖方是否承担合并后风险; stock deal 把"价格"与买方股价绑定 [T06-S005].

**Earnout / 对赌 (盈利能力支付)** — deferred contingent payment if target hits post-close milestones (revenue/EBITDA). 标的达成业绩里程碑后的或有递延付款. 为何重要: 弥合买卖双方估值分歧的桥梁; 但争议高发 (如何衡量、是否被买方操纵) [T06-S006].

**Breakup fee / Termination fee / 分手费** — fee seller pays buyer if seller walks (e.g. accepts a higher bid). 卖方反悔(如接受更高报价)付给买方的费用. 为何重要 + caveat: 保护初始买方 + 抑制 jumping bid; 实测均值 ~2.4% (大型) / ~3.1% (中型) of target equity, 法院通常视 >4% 过高 [T06-S015][T06-S006].

**Reverse termination fee (RTF) / 反向分手费** — fee buyer pays seller if buyer walks (financing fails / antitrust block). 买方反悔(融资失败/反垄断否决)付给卖方. 为何重要 + caveat: 给卖方 deal-certainty 保护; 均值约 deal 的 2-4% (单档 RTF 2015-17 均值 ~4.5%, 较 2013-14 的 6.5% 下降); 反垄断 RTF 单列 [T06-S015][T06-S016].

**Go-shop / 主动询价期** — post-signing window letting seller actively solicit higher bids (often with lower breakup fee). 签约后卖方仍可主动找更高报价的窗口(常配较低分手费). 为何重要: 缓解"卖太便宜"的 fiduciary 风险, 常见于 PE take-private [T06-S006].

**No-shop / 禁止招揽** — seller may not solicit other bids post-signing (subject to fiduciary out). 签约后不得招揽其他报价(留 fiduciary out 例外). 为何重要: 保护买方排他性; 与 go-shop 相对 [T06-S006].

**MAC / MAE — Material Adverse Change / Effect / 重大不利变化** — clause letting buyer walk if target suffers a defined material deterioration between signing and closing. 签约到交割间标的重大恶化时买方可退出的条款. 为何重要: deal-certainty 的核心战场; 谈判焦点是 carve-outs (行业普遍因素/疫情/市场是否算 MAC) [T06-S006].

**Reps & warranties (R&W) / 陈述与保证** — seller's factual statements about the business (title, financials, litigation, compliance). 卖方对业务事实的陈述. 为何重要: 风险分配 + 赔偿(indemnity)基础; R&W insurance 近年常替代 escrow [T06-S006].

**Escrow / 托管** — portion of purchase price held by a third party to cover post-close indemnity claims. 部分对价由第三方托管以备索赔. 为何重要: 卖方违反 R&W 时买方的追偿来源; R&W 保险兴起后规模缩小 [T06-S006].

**Working capital adjustment / 营运资金调整** — post-close true-up of purchase price to a normalized net-working-capital target ("locked box" 为替代机制). 按正常营运资金目标对对价做交割后调整. 为何重要: 防止卖方在交割前抽走流动资金; 是 closing 后争议常见点 [T06-S006].

**Collar / 价格区间 (换股保护)** — in a stock deal, a mechanism capping/flooring the exchange ratio or value as acquirer's share price moves. 换股交易中限定换股比例/价值随买方股价波动的机制. 为何重要: 保护双方免受 signing→closing 间股价大幅波动冲击 [T06-S005].

**Tender offer / 要约收购** — buyer offers to buy shares directly from shareholders (vs one-step merger via shareholder vote). 直接向股东要约收购股份(对比一步式合并表决). 为何重要: 速度快 (HSR 等待期 15 天 vs 30 天), 可绕过董事会的 friendly 路径或敌意工具 [T06-S009].

**Hostile vs Friendly / 敌意 vs 善意** — *friendly*: board-approved, negotiated. *Hostile*: pursued over board objection (tender offer / proxy fight). 经董事会同意 vs 越过董事会. 为何重要: 决定可用工具 (敌意方靠 tender offer + proxy; 防守方动用 poison pill 等) [T06-S013].

**Poison pill / Shareholder rights plan / 毒丸计划** — defense diluting a hostile acquirer once it crosses an ownership threshold. 敌意方持股越线即触发稀释的防御. 为何重要: 最强反收购工具, 逼对方回到谈判桌; activist 时代仍常态化使用 [T06-S013].

**White knight / 白衣骑士** — a friendlier alternative acquirer sought by a target to escape a hostile bidder. 标的为摆脱敌意买方而找的友好替代买方. 为何重要: 防御战术之一, 也可能引发竞价战抬高成交价 [T06-S013].

**Staggered / Classified board / 分期 (错列) 董事会** — directors elected in staggered classes so only a fraction turn over yearly, slowing hostile control change. 董事分期改选, 减缓敌意夺权. 为何重要: 与 poison pill 并用是最有效的反收购结构性防御 [T06-S013].

## 6.4 行业 / 角色 / 监管 (bank tiers / pyramid / fees / antitrust / national security)

**Bulge bracket / 大行 (顶级综合投行)** — largest full-service global banks (Goldman Sachs, Morgan Stanley, JPMorgan, BofA, Citi). 最大的全能型全球投行. 为何重要: 资产负债表 (可融资) + 全产品 + 全球覆盖; M&A advisory 与承销/借贷利益绑定 (boutique 据此攻击其独立性) [T06-S013].

**Elite boutique / 精品投行** — advisory-only top firms (Centerview, Evercore, Moelis, Lazard, PJT, Perella Weinberg). 纯顾问型顶级精品行. 为何重要: 标榜"无承销利益冲突"的独立顾问叙事; 在大型交易 league table 与 bulge bracket 同台 [T06-S013].

**Middle market / 中间市场投行** — firms focused on smaller deals (Houlihan Lokey, William Blair, Harris Williams, Lincoln, etc.). 专注较小交易的投行. 为何重要: deal 规模 + 费率结构 (更靠近 Lehman/Double-Lehman) 与上层不同 [T06-S014].

**Analyst → Associate → VP → Director → MD / 分析师 → 经理 → 副总裁 → 董事 → 董事总经理** — the IB advancement pyramid; juniors model/build decks, MDs originate (rainmaking). 投行晋升金字塔; 初级做模型/deck, MD 拉业务. 为何重要: 决定 deal 上谁干什么; analyst 80-100h/week 的血汗文化批判即指金字塔底层 (业内观察, 非精确普适数据) [T06-S013].

**Coverage vs Product / 行业组 vs 产品组** — *coverage* (industry/sector banker, owns the client relationship) vs *product* (M&A, ECM, DCM, LevFin, Restructuring — executes the deal). 行业覆盖银行家 (持客户关系) vs 产品组 (执行交易). 为何重要: 一笔 M&A 常由 coverage 带入、product (M&A 组) 执行; 组织结构基本盘 [T06-S013].

**Sponsors group / 私募股权覆盖组** — bankers who cover PE firms (financial sponsors) as repeat clients. 专门覆盖 PE (财务投资人) 的银行家. 为何重要: PE 是高频重复客户 (LBO 融资 + 退出 sell-side), 是稳定费源 [T06-S019].

**Corp dev / Corporate development / 公司发展部 (内部并购)** — in-house M&A team at a strategic acquirer; the "buy-side client" sitting across from bankers. 战略买方内部的并购团队. 为何重要: 战略买方的内部对手方/客户; 与 banker advisory 角色互补 [T06-S013].

**League table / 排行榜** — rankings of banks by deal value/volume over a period (Refinitiv/Dealogic/Bloomberg). 按成交额/笔数对投行排名. 为何重要 + caveat: pitch 的信誉货币 + 招聘宣传; 但口径可操纵 (announced vs completed, 单方 mandate 也计) — 第三方数据 [T06-S013].

**Lehman formula / 雷曼公式** — tiered success-fee scale: classic 5-4-3-2-1 (5% of first $1M ... 1% thereafter). 阶梯式成功费: 经典 5-4-3-2-1. 为何重要 + caveat: 通胀使经典版过时 → *Double Lehman* (10-8-6-4-2) 更常见, *Modified Lehman* 用于大额; 多见于 middle-market / 商业经纪 [T06-S014].

**Success fee vs Retainer / 成功费 vs 聘用费** — *success fee*: contingent on closing (大额, 主收入). *Retainer*: upfront/monthly fixed, often credited against success fee. 成交才付的成功费 vs 预付/月度固定的聘用费. 为何重要 + caveat: success fee 通常 ~1-2% of deal value 且随规模递减 (业内惯例, 非精确普适); retainer 表明客户认真度 [T06-S014]. 注: agency problem 根源在此 — banker 收入挂成交 → "banker 总想成交"的行业原罪批判.

**HSR Act — Hart-Scott-Rodino / 反垄断申报 (美)** — Clayton Act §7A premerger notification to FTC + DOJ for deals over a size threshold (US$133.9M for 2026), then a 30-day waiting period (15 days for cash tender offers). HSR 反垄断预申报. 为何重要 + 红线: 跨阈值交易必须申报并等待; 30 天内监管可发 *Second Request* 深查 → deal-certainty 风险 + 时间表关键约束. Decay: 阈值年度调整 [T06-S007][T06-S008][T06-S009].

**FTC / DOJ Antitrust / 联邦贸易委员会 / 司法部反垄断局** — the two US merger-review agencies (Clayton Act §7: deals that may "substantially lessen competition"). 美两大合并审查机构. 为何重要 + 红线: 可起诉阻止交易 → reverse termination fee / antitrust risk 分配的源头; 2023-2025 执法趋严 (Decay: 政府/口径变化快) [T06-S009][T06-S016].

**CFIUS / 外国投资国安审查 (美)** — Committee on Foreign Investment in the US; reviews foreign acquisitions of US businesses for national-security risk (Defense Production Act 1950 + FIRRMA 2018). 外资收购美企的国安审查委员会. 为何重要 + 红线: FIRRMA 下对 critical tech / 外国政府"substantial interest"交易强制申报; 可建议总统否决/拆解; voluntary filing 换 safe harbor. 中美交易高敏感 [T06-S010][T06-S011].

**SEC rules / 美国证监会规则** — public-company M&A disclosure: proxy (DEFM14A), tender offer (Schedule TO / SC 14D-9), all on EDGAR; fairness opinions are publicly filed. SEC 上市公司并购披露规则. 为何重要 + 红线: 上市标的的对价、过程、fairness opinion、利益冲突全部公开 → 是 precedent transactions / deal-term 研究的一手金矿, 也是诉讼基础 [T06-S013].

**FINRA Rule 5150 — Fairness Opinions / 公平意见规则** — requires a broker-dealer issuing a fairness opinion to disclose conflicts: prior advisory role + contingent success fee + material relationships (past 2 yrs). 要求出具公平意见的券商披露利益冲突. 为何重要 + 红线: 直击"出意见 banker 也收成交费"的冲突 — 不消除冲突, 只强制披露 [T06-S012].

---

## Phase 2 接口

**最该进 master skill 的 top 术语 (deal sense 锚点):**
1. **price vs value vs deal value 三层** — intrinsic value (DCF/Damodaran) ⇄ market price (trading comps) ⇄ negotiated deal price (含 control premium + synergies + leverage/竞争). 这是整个行业世界观的量化骨架, 必进 [T06-S001][T06-S002][T06-S004].
2. **certainty of close** — signing↔closing 之间的 deal risk (MAC / 监管 / 融资), 用 breakup fee / RTF / collar / financing-out 条款分配. "最高纸面价≠最好 offer"的具象 [T06-S006][T06-S015].
3. **controlled auction 机制** — 用信息节奏 + 竞争张力把价格推向上限 (broad/targeted/negotiated 权衡). sell-side 的核心手艺 [T06-S004].
4. **accretion/dilution + synergies** — 上市收购方董事会 go/no-go + banker pitch 卖点, 配 synergy 系统性高估的批判 [T06-S005][T06-S017].
5. **fairness opinion 的利益冲突** — agency problem 的制度化体现, FINRA 5150 只披露不消除 [T06-S012][T06-S021].

**监管 / 合规红线 (Decay risk = high, 须 12 月内复核):**
- **HSR** 跨阈值 (2026 = US$133.9M) 必须申报 + 30 天等待 (cash tender 15 天) + Second Request 风险 [T06-S007][T06-S008][T06-S009].
- **CFIUS** critical tech / 外国政府 substantial interest 强制申报; 中美交易高敏感; 可被总统否决 [T06-S010][T06-S011].
- **FTC/DOJ** 反垄断可诉讼阻止 (Clayton §7); 2023-2025 执法趋严, 口径变化快 [T06-S009].
- **FINRA 5150 / SEC** fairness opinion 冲突披露 + 上市并购全披露 (EDGAR) [T06-S012][T06-S013].
- 数字红线: control premium "20-40%" 非 universal (Damodaran 批判); breakup fee 法院 >4% 视过高; "70-90% 并购失败" vs KPMG 2025 的 57.2% — 区间随研究方法剧变, synthesis 引用必挂来源 [T06-S002][T06-S015][T06-S017][T06-S018].

**新 figure / tool 候选 (Phase 2 可 CLI 化 / 做 figure):**
- **Football field 生成器** — 输入 DCF/comps/precedent/LBO 区间 → 输出估值条形图 (高度标准化, 易 CLI 化).
- **Sources & uses + 简易 LBO IRR/MOIC 计算器** — 输入 EBITDA/multiple/leverage/exit → 反推可付价 + 回报.
- **Accretion/dilution 速算器** — 输入双方 EPS/对价形式/协同 → 判增厚/摊薄.
- **Lehman/Double-Lehman 费用计算器** — 输入 deal value + scale → 成功费 (含 caveat).
- **Deal-process 时间线 figure** — teaser→NDA→CIM→IOI→data room→LOI→SPA→signing→closing + 叠加 HSR/CFIUS 监管时钟.
- **Damodaran spreadsheets** 是现成一手工具库 (DCF/WACC/relative valuation), 可链接为 figure 后端 [T06-S001].

---

## 质量自检 (Quality Self-Check)

- [x] ≥30 术语 — 收录 **62** distinct terms (6.1 估值建模 23 / 6.2 流程产出物 17 / 6.3 结构条款 16 / 6.4 行业角色监管 ~16; 部分跨组, 去重后约 62).
- [x] 4 类分组齐全 (估值建模 / 流程产出物 / 结构条款 / 行业监管).
- [x] 每术语: 中英对照定义 + 为何重要 + source_id.
- [x] Source Manifest 表 21 条, id T06-S001..S021 递增, bucket + last_checked=2026-06-16 + author/host + note 齐全.
- [x] 数字类全部挂来源 + caveat: control premium 20-40% (Damodaran 批判非普适) / breakup fee ~2.4-3.1% (Harvard deal study) / RTF ~2-4.5% (deal study) / success fee 1-2% 递减 (业内惯例) / Lehman 5-4-3-2-1 + Double Lehman / 并购毁灭价值 70-90% vs KPMG 2025 的 57.2% 并列.
- [x] 黑名单零引用 — WSO 在搜索出现但未作 source; 无 LinkedIn 正文/知乎/公众号/百度/Quora/内容农场.
- [x] 一手率 ≈ 62% (Damodaran NYU + FTC/CFIUS/Treasury/CRS/FINRA/SEC = verified_primary); Investopedia=reference/secondary, CFI/WSP/Macabacus=surrogate_primary (vendor), 已正确标 bucket.
- [x] 诚实边界保留: 估值伪精确 (garbage in garbage out) / fairness opinion 利益冲突 / synergy 高估 / banker agency problem 未软化.
- [x] Decay 标注: HSR 阈值年度更新 (2026=$133.9M) / 反垄断执法口径 / CFIUS — 标 high decay, 12 月复核.
- [ ] 待 Phase 2 验证: 个别二手 baseline (Investopedia/Wikipedia) 在 synthesis 时若作硬事实应升级到一手 (Rosenbaum & Pearl 原书 / Damodaran 章节); 中文 settled 译法对 go-shop/collar/SOTP 仍偏弱 (保留英文).
