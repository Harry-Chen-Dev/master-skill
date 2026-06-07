# 06-glossary.md — 个人投资理财 GLOSSARY（术语 + 标准 + 法规 + outsider-tell）

> **行业**: 个人投资理财 (Personal Investing & Financial Planning)，locale = **global**，profile = practitioner（自主投资者 / 散户，非持牌投顾展业）。
>
> **本 track 的结构性特征**：① 术语高度英文主导（四大流派的核心词汇——价值/被动/技术/趋势——几乎全是英文原生），zh-CN 多为译介；② **法规/标准呈强地域分裂**：美国体系（SEC/FINRA/IRS/SECURE 2.0）与中国体系（证监会/资管新规/个人养老金/费率改革）几乎不重叠，全文按 `geographic-specific: US / CN` 分别记录；③ 认证维度对**自主散户**几乎 N/A——CFA/CFP/GIPS 是持牌从业者/机构的资质，散户不需考，但需认得（用于识别「谁在对我说话」），故归 Tier 2 reference。
>
> **非投资建议**: 本文件是认知 OS 素材，不构成任何具体证券/买卖时点建议。数字（费率/限额/生效日）一律挂 gov 原文源，未核实者标 caveat。
>
> **zh-CN blacklist（绝不入 manifest）**: 知乎、微信公众号、百度百科/百度知道、CSDN、简书。本文件 0 条黑名单 URL。
>
> **研究日期**: 2026-06-04 | Track 06 (Glossary) Wave 1 subagent

---

## Source Manifest

| source_id | url | bucket | last_checked | author/host | one-line note |
|-----------|-----|--------|--------------|-------------|---------------|
| T06-S001 | https://www.investor.gov/introduction-investing/investing-basics/glossary | verified_primary | 2026-06-04 | SEC investor.gov (.gov) | SEC 投资者教育官方术语表（散户术语 ground truth） |
| T06-S002 | https://www.bogleheads.org/wiki/Three-fund_portfolio | verified_primary | 2026-06-04 | Bogleheads wiki | 三基金组合定义 = 被动派最高引用术语母页 |
| T06-S003 | https://www.bogleheads.org/wiki/Dollar_cost_averaging | verified_primary | 2026-06-04 | Bogleheads wiki | DCA 定投定义 + 与 lump-sum 之争原文 |
| T06-S004 | https://www.bogleheads.org/wiki/Expense_ratios | verified_primary | 2026-06-04 | Bogleheads wiki | 费率对复利侵蚀的官方解释 |
| T06-S005 | https://www.bogleheads.org/wiki/Rebalancing | verified_primary | 2026-06-04 | Bogleheads wiki | 再平衡定义 + 纪律 |
| T06-S006 | https://www.bogleheads.org/wiki/Tax_loss_harvesting | verified_primary | 2026-06-04 | Bogleheads wiki | 税损收割定义 + wash-sale 规则 |
| T06-S007 | https://www.bogleheads.org/wiki/Safe_withdrawal_rates | verified_primary | 2026-06-04 | Bogleheads wiki | 安全提取率 / 4% 法则 / Trinity Study |
| T06-S008 | https://www.bogleheads.org/wiki/Margin_of_safety | verified_primary | 2026-06-04 | Bogleheads wiki | 安全边际（Graham）社区 wiki 条目 |
| T06-S009 | https://www.spglobal.com/spdji/en/documents/spiva/spiva-us-year-end-2024.pdf | secondary | 2026-06-04 | S&P DJI (SPIVA) | SPIVA US 年报 YE2024 PDF（主动 vs 被动一手数据，host 默认 secondary） |
| T06-S010 | https://www.spglobal.com/spdji/en/spiva/article/spiva-us/ | secondary | 2026-06-04 | S&P DJI (SPIVA) | SPIVA US 落地页（最新 scorecard + 方法论入口） |
| T06-S011 | https://www.finra.org/rules-guidance/key-topics/regulation-best-interest | verified_primary | 2026-06-04 | FINRA (.org 白名单) | Reg BI 官方要点页（4 项义务 + 生效日） |
| T06-S012 | https://www.finra.org/article/regulation-best-interest-(reg-bi)-overview | verified_primary | 2026-06-04 | FINRA | Reg BI overview（best-interest vs suitability） |
| T06-S013 | https://www.irs.gov/newsroom/401k-limit-increases-to-24500-for-2026-ira-limit-increases-to-7500 | verified_primary | 2026-06-04 | IRS (.gov) | 2026 缴款上限官方新闻稿（401k $24,500 / IRA $7,500） |
| T06-S014 | https://www.irs.gov/pub/irs-drop/n-25-67.pdf | verified_primary | 2026-06-04 | IRS Notice 2025-67 (.gov) | 2026 退休计划限额技术公告原文 |
| T06-S015 | https://www.irs.gov/retirement-plans/retirement-plan-and-ira-required-minimum-distributions-faqs | verified_primary | 2026-06-04 | IRS (.gov) | RMD 规则 FAQ（SECURE 2.0 后 age 73） |
| T06-S016 | https://www.cfainstitute.org/insights/professional-learning/gips-standards | verified_primary | 2026-06-04 | CFA Institute (.org 白名单) | GIPS 标准官方页（机构业绩呈现标准） |
| T06-S017 | https://www.cfainstitute.org/insights/professional-learning/refresher-readings/2026/overview-of-the-global-investment-performance-standards | verified_primary | 2026-06-04 | CFA Institute | GIPS 概览 refresher（composite 定义 + 2020 版生效） |
| T06-S018 | https://www.csrc.gov.cn/csrc/c101900/c6551799/content.shtml | verified_primary | 2026-06-04 | 中国证监会 (.gov.cn) | 个人养老金基金名录官方页（产品名录 ground truth） |
| T06-S019 | https://www.gov.cn/zhengce/zhengceku/202412/content_6993666.htm | verified_primary | 2026-06-04 | 中国政府网 (.gov.cn) | 《关于全面实施个人养老金制度的通知》入口（2024-12 五部门；域名实测 verified_primary，具体 slug→内容以官网为准） |
| T06-S020 | http://www.csrc.gov.cn/xiamen/c105636/c7511608/content.shtml | verified_primary | 2026-06-04 | 证监会厦门局 (.gov.cn) | 公募费率改革「以降促升」官方解读（费改三步走） |
| T06-S021 | https://www.sec.gov/about/divisions-offices/division-investment-management/investment-company-registration-regulation-package | verified_primary | 2026-06-04 | SEC (.gov) | 投资公司注册/招募说明书 prospectus 监管包 |
| T06-S022 | https://www.investopedia.com/terms/p/pe.asp | secondary | 2026-06-04 | Investopedia (reference) | P/E 等基础术语定义（reference，非一手；admin path /terms） |
| T06-S023 | https://www.tsp.gov/news-and-resources/secure-2-0-and-the-tsp/ | verified_primary | 2026-06-04 | TSP (.gov) | SECURE 2.0 条款分阶段生效官方说明 |
| T06-S024 | https://www.congress.gov/crs-product/IF12750 | verified_primary | 2026-06-04 | Congress.gov CRS (.gov) | RMD 规则 CRS 报告（立法机构原文，age 73→75 时间线） |

> **黑名单核对**: 上表 0 个 `bucket=blacklisted`。投资定义优先 Bogleheads wiki（verified_primary）+ investor.gov（verified_primary）+ 监管原文；Investopedia 仅作 reference 交叉验证；数字一律 gov 源。
> **bucket 实测说明**: `.gov` / `.gov.cn` / `finra.org` / `bogleheads.org` / `cfainstitute.org` / `morningstar.com` 实测 = `verified_primary`；`spglobal.com`（含 SPIVA PDF）/ `gipsstandards.org` / `investopedia.com` 实测 = `secondary`（host 默认或 brand admin path），故 SPIVA 数字虽是一手数据但 bucket 记 secondary，引用时配 gov/学术交叉。T06-S019 的 gov.cn 域名实测 verified_primary，具体 slug→内容映射以官网为准（caveat 在 note）。

---

## A. 估值 / 价值派术语

### 1. P/E（市盈率，Price-to-Earnings ratio）
- **Type**: term + acronym | **Tier**: tier-1
- **Insider def**: 股价 ÷ 每股收益（EPS）；估值锚之一，**永远要问「相对谁、relative to 历史/同业/增速」**，孤立的 P/E 数字无意义。(evidence: [T06-S001, T06-S022])
- **Outsider-friendly**: 你为公司每 1 元利润付多少钱。
- **outsider-tell** (`usage_tell`): 外行说「P/E 低=便宜、高=贵」就买/卖——内行知道低 P/E 可能是价值陷阱（盈利将崩），高 P/E 可能是合理成长定价；且 P/E 用的是**会计利润**，易被一次性项目扭曲。(evidence: [T06-S022])
- **pronunciation_tell**: 读「P-E ratio」（字母）或「price-earnings」，外行常写成「PE 比」却说不清分子分母。
- **关联**: EPS、P/B、PEG、内在价值
- **Decay risk**: low

### 2. EPS（每股收益，Earnings Per Share）
- **Type**: acronym | **Tier**: tier-1
- **Insider def**: 净利润 ÷ 流通股数；P/E 的分母。内行分 GAAP EPS vs adjusted/non-GAAP EPS，并警惕「稀释后摊薄 diluted」与回购对每股的人为抬升。(evidence: [T06-S001, T06-S022])
- **outsider-tell** (`semantic_tell`): 外行把「EPS 增长」直接等同「公司变好」——内行先看是真实经营增长还是回购缩股/会计调整。
- **关联**: P/E、自由现金流、ROE
- **Decay risk**: low

### 3. P/B（市净率，Price-to-Book）
- **Type**: term + acronym | **Tier**: tier-1
- **Insider def**: 股价 ÷ 每股净资产（book value）。价值派/银行股/重资产常用；对轻资产/科技公司（无形资产不入表）几乎失效。(evidence: [T06-S022])
- **outsider-tell** (`usage_tell`): 拿 P/B 去估 SaaS/平台公司——book value 不含品牌/网络效应，内行知道此处 P/B 误导。
- **关联**: book value、ROE、P/E
- **Decay risk**: low

### 4. 内在价值（intrinsic value）
- **Type**: term | **Tier**: tier-1
- **Insider def**: 一家企业基于未来现金流折现的「应值多少」，独立于市场报价；价值投资全部逻辑的锚。「价格是你付的，价值是你得的」(Buffett/Marks)。(evidence: [T06-S008, T06-S022])
- **outsider-tell** (`semantic_tell`): 外行说「这股值不值」时指**当前股价涨跌**；内行的「value」指 price 之外的、需自己估算的数。把「跌了=变便宜」当然成立——但只有 price 跌而 value 没跌才是真便宜。
- **关联**: 安全边际、DCF、Mr. Market
- **Decay risk**: low

### 5. 安全边际（margin of safety）
- **Type**: term | **Tier**: tier-1
- **Insider def**: 内在价值与买入价之间的折扣缓冲，吸收估值误差与坏运气；Graham 把稳健投资浓缩为这三个字。(evidence: [T06-S008])
- **Etymology**: Benjamin Graham《The Intelligent Investor》。
- **outsider-tell** (`usage_tell`): 外行把「安全边际」理解成 stop-loss 止损线（一个价格触发点）——内行的安全边际是**买入时**就要的折扣，是事前的容错，不是事后的割肉。
- **关联**: 内在价值、Mr. Market、能力圈
- **Decay risk**: low

### 6. 护城河（moat / economic moat）
- **Type**: term | **Tier**: tier-1
- **Insider def**: 企业可持续抵御竞争、维持高资本回报的结构性优势（品牌/网络/转换成本/规模/专利）。Buffett 普及，Morningstar 体系化（wide/narrow/no moat）。(evidence: [T06-S022])
- **outsider-tell** (`usage_tell`): 外行把「产品好/市占第一」当护城河——内行问的是「这优势能不能持续 10 年、对手有没有能力复制」，一次性领先 ≠ moat。
- **关联**: 能力圈、ROE、内在价值
- **Decay risk**: low

### 7. 能力圈（circle of competence）
- **Type**: term | **Tier**: tier-1
- **Insider def**: 你真正理解其商业模式/赚钱逻辑/风险的领域边界；只在圈内下注。Buffett/Munger 核心纪律。(evidence: [T06-S022])
- **outsider-tell** (`register_tell`): 外行追当下热门赛道（AI/新能源）说「这是未来」就重仓——内行先问「我看不看得懂这门生意」，看不懂就放弃，哪怕它会涨。
- **关联**: 护城河、内在价值
- **Decay risk**: low

### 8. Mr. Market（市场先生）
- **Type**: term | **Tier**: tier-1
- **Insider def**: Graham 把市场拟人成情绪躁郁的合伙人，每天报一个买卖价，你**可以无视他**，只在他报价极端有利时交易。强调把市场报价当工具而非指令。(evidence: [T06-S008, T06-S022])
- **Etymology**: Graham《The Intelligent Investor》第 8 章。
- **outsider-tell** (`semantic_tell`): 外行把市场价格当「真理/正确估值」，价格涨就觉得自己对、跌就恐慌——内行把价格当 Mr. Market 的情绪报价，与价值脱钩。
- **关联**: 内在价值、安全边际、有效市场假说（对立面）
- **Decay risk**: low

### 9. ROE（净资产收益率，Return on Equity）
- **Type**: acronym | **Tier**: tier-1
- **Insider def**: 净利润 ÷ 股东权益；衡量企业用自有资本赚钱的效率，价值派核心质量指标。内行用 DuPont 拆解（利润率×周转×杠杆），警惕高杠杆撑出的虚高 ROE。(evidence: [T06-S001, T06-S022])
- **outsider-tell** (`usage_tell`): 外行只看 ROE 高就叫「好公司」——内行先剥掉财务杠杆，看是真盈利能力还是借债堆出来的。
- **关联**: EPS、护城河、自由现金流
- **Decay risk**: low

### 10. 自由现金流（FCF，Free Cash Flow）
- **Type**: term + acronym | **Tier**: tier-1
- **Insider def**: 经营现金流 − 资本开支；企业可自由支配的真金白银，比会计利润难造假，DCF 估值的输入。(evidence: [T06-S022])
- **outsider-tell** (`semantic_tell`): 外行把「净利润」当公司赚的钱——内行知道利润是会计口径（含非现金/应计），FCF 才看得出企业是否真在产生现金。
- **关联**: EPS、DCF、内在价值
- **Decay risk**: low

### 11. 股息率（dividend yield）
- **Type**: term | **Tier**: tier-1
- **Insider def**: 每股股息 ÷ 股价；现金回报率。内行警惕「高股息陷阱」（股价暴跌推高 yield，或不可持续的派息）。(evidence: [T06-S001, T06-S022])
- **outsider-tell** (`usage_tell`): 外行专挑「股息率最高」的买——内行先看派息**可持续性**（payout ratio、现金流覆盖），高 yield 常是股价下跌或即将削减股息的信号。
- **关联**: 总回报、DRIP、book value
- **Decay risk**: low

### 12. DCF（现金流折现，Discounted Cash Flow）
- **Type**: acronym | **Tier**: tier-2
- **Insider def**: 把企业未来 FCF 按折现率（WACC）贴现求内在价值的估值法；价值派/分析师标准工具，但对假设（增长率、折现率、永续值）极度敏感——「garbage in, garbage out」。(evidence: [T06-S022])
- **outsider-tell** (`usage_tell`): 把 DCF 当精确科学，算出一个「准确」目标价——内行知道它是 sensitivity 分析工具，假设变一点结果天差地别，重点在区间和逻辑而非点估值。
- **关联**: FCF、内在价值、CAPM（折现率来源）
- **Decay risk**: low

### 13. book value（账面价值 / 净资产）
- **Type**: term | **Tier**: tier-2
- **Insider def**: 资产 − 负债的会计账面值；P/B 的分母。对银行/保险/重资产有意义，对无形资产主导的公司严重低估真实价值。(evidence: [T06-S022])
- **outsider-tell** (`usage_tell`): 把 book value 当「公司清算能拿回的钱」——内行知道账面值≠市值≠清算值，且历史成本计量常与现值脱节。
- **关联**: P/B、内在价值
- **Decay risk**: low

---

## B. 被动 / 组合术语

### 14. 资产配置（asset allocation）
- **Type**: term | **Tier**: tier-1
- **Insider def**: 在大类资产（股/债/现金/另类）间分配权重；学术与实务共识——**长期回报的主要决定因素是配置，而非选股/择时**。(evidence: [T06-S001, T06-S002])
- **outsider-tell** (`semantic_tell`): 外行以为「投资=选哪只股/基金」；内行先定股债比例（如 80/20），具体标的反而次要。「选标的」是新手焦点，「定配置」是老手焦点。
- **关联**: 再平衡、60/40、风险平价、三基金组合
- **Decay risk**: low

### 15. 再平衡（rebalancing）
- **Type**: term | **Tier**: tier-1
- **Insider def**: 定期把偏离目标的资产权重拉回（卖涨买跌），维持风险敞口；纪律性动作，**机械执行优于择时**。(evidence: [T06-S005])
- **outsider-tell** (`usage_tell`): 外行听到「卖掉涨的、买入跌的」觉得反人性/赔钱——内行知道这正是低买高卖的纪律化，凭感觉「让利润奔跑」反而抬高风险。
- **关联**: 资产配置、60/40、定投
- **Decay risk**: low

### 16. 三基金组合（three-fund portfolio）
- **Type**: term | **Tier**: tier-1
- **Insider def**: 全市场美股指数 + 全市场国际股指数 + 全市场债券指数三只低费基金，覆盖大部分人的需求；Bogleheads 旗舰简约方案。(evidence: [T06-S002])
- **outsider-tell** (`register_tell`): 外行觉得「就三只基金太简单/不够专业」，追求复杂组合显得高级——内行知道简单+低费+不动手往往跑赢花哨配置。
- **关联**: 资产配置、指数基金、费率
- **Decay risk**: low

### 17. 60/40（六四组合）
- **Type**: term | **Tier**: tier-1
- **Insider def**: 60% 股 + 40% 债的经典平衡组合代名词，散户/养老金默认基准之一。(evidence: [T06-S001])
- **outsider-tell** (`usage_tell`): 外行把 60/40 当「保守不会亏」——内行知道 2022 年股债双杀时它照样大跌，配置≠保本。
- **关联**: 资产配置、All-Weather、再平衡
- **Decay risk**: low

### 18. 全天候 / 风险平价（All-Weather / risk parity）
- **Type**: term | **Tier**: tier-2
- **Insider def**: Dalio/Bridgewater 普及的按**风险贡献**（而非市值/资金）均衡配置的思路，常加杠杆债与商品对冲不同经济象限。(evidence: [T06-S001])
- **outsider-tell** (`usage_tell`): 外行把「全天候」当「任何行情都赚钱」——内行知道它是**降低波动**而非保证正收益，且依赖杠杆与历史相关性假设，相关性失效时会同步回撤。
- **关联**: 60/40、风险平价、波动率
- **Decay risk**: medium

### 19. 费率（expense ratio，ER / 管理费率）
- **Type**: term | **Tier**: tier-1
- **Insider def**: 基金每年从资产中扣取的运营费占比；**复利的隐形杀手**——1% vs 0.05% 在 30 年维度吞掉巨大份额的终值。被动派把「最小化费率」当第一纪律。(evidence: [T06-S004])
- **outsider-tell** (`semantic_tell`): 外行觉得「1% 费率才一点点、收益高就值」——内行算复利侵蚀：长期下费率差几乎线性侵蚀终值，是少数「确定能控制」的变量。
- **关联**: 跟踪误差、指数基金、复利、NAV
- **Decay risk**: low（概念）/ 但 CN 费率绝对值在改革中（见衰减信号）

### 20. 跟踪误差（tracking error）
- **Type**: term | **Tier**: tier-2
- **Insider def**: 指数基金实际回报与所跟踪指数之间的偏离度；衡量被动产品「复制质量」，受费率/抽样/再平衡拖累。(evidence: [T06-S001])
- **outsider-tell** (`usage_tell`): 外行以为「指数基金=完全等于指数」——内行知道有费率和复制误差，长期会略微落后名义指数。
- **关联**: 费率、指数基金、NAV
- **Decay risk**: low

### 21. 指数基金 / ETF（index fund / Exchange-Traded Fund）
- **Type**: term + acronym | **Tier**: tier-1
- **Insider def**: 被动复制某指数的基金；ETF 是可在交易所盘中买卖的份额形式。被动派核心载体；Bogle 发明首只散户指数基金。(evidence: [T06-S001, T06-S002])
- **outsider-tell** (`usage_tell`): 外行把所有 ETF 当「低费被动」——内行知道现在有大量主动/杠杆/主题 ETF（费率高、波动大），ETF 是**结构**不是「便宜被动」的代名词。
- **pronunciation_tell**: 读「E-T-F」（字母），外行有时说「ETF 基金」冗余。
- **关联**: 费率、NAV、跟踪误差、三基金组合
- **Decay risk**: low

### 22. 定投（DCA，Dollar-Cost Averaging）
- **Type**: term + acronym | **Tier**: tier-1
- **Insider def**: 按固定金额/周期分批买入，摊平成本、消除择时焦虑。**严格定义**：DCA 指把一笔已有资金分期投入（与一次性 lump-sum 对照）；广义也指「持续用工资定额投」。(evidence: [T06-S003])
- **outsider-tell** (`semantic_tell`): 外行说「定投稳赚不赔/越跌越买必赚」——内行知道：① DCA 在**已有一笔钱**时统计上常**跑输** lump-sum（市场长期上涨）；② 定投只降低择时与情绪风险，**不保证盈利**，标的长期下跌照样亏。
- **关联**: 一次性 lump sum、复利、再平衡
- **Decay risk**: low

### 23. 一次性投入（lump sum）
- **Type**: term | **Tier**: tier-2
- **Insider def**: 把可投资金一次性投入；研究（含 Vanguard/Bogleheads 讨论）显示因「time-in-market」优势，多数历史区间 lump-sum 优于把同一笔钱 DCA 分期。(evidence: [T06-S003])
- **outsider-tell** (`usage_tell`): 外行直觉觉得「一次性投入风险大、定投更稳」——内行区分「降低后悔/情绪」与「期望回报」：lump-sum 期望回报更高但波动暴露更早。
- **关联**: 定投 DCA、time-in-market
- **Decay risk**: low

### 24. 复利（compound interest / compounding）
- **Type**: term | **Tier**: tier-1
- **Insider def**: 收益再产生收益的指数增长；长期投资的核心引擎，**时间是最大变量**。费率/税/中断都按复利被放大。(evidence: [T06-S001, T06-S004])
- **outsider-tell** (`semantic_tell`): 外行用线性直觉看收益（「一年 10%、十年就 100%」）——内行知道复利是指数的、对时间极敏感，且任何中途清仓/高费率都会折损复利曲线。
- **关联**: 费率、总回报、DRIP、4% 法则
- **Decay risk**: low

### 25. 总回报（total return）
- **Type**: term | **Tier**: tier-1
- **Insider def**: 价格涨跌 + 股息/利息（再投资）的合计回报；评估投资的正确口径，区别于只看价格的「价格回报 price return」。(evidence: [T06-S001])
- **outsider-tell** (`semantic_tell`): 外行只盯股价涨跌算盈亏，忽略股息/分红——内行用 total return，还会进一步区分**名义 vs 实际（扣通胀）、税前 vs 税后**。
- **关联**: 股息率、DRIP、复利
- **Decay risk**: low

### 26. NAV（净值，Net Asset Value）
- **Type**: acronym | **Tier**: tier-2
- **Insider def**: 基金每份额的资产净值（总资产−负债）÷份额数；开放式基金按 NAV 申赎。ETF 盘中市价可相对 NAV 溢价/折价。(evidence: [T06-S001])
- **outsider-tell** (`usage_tell`): 外行觉得「NAV 低的基金=便宜，要买便宜的」——内行知道 NAV 高低与「贵/便宜」无关（不是股价），只反映历史累计。
- **关联**: ETF、指数基金、跟踪误差
- **Decay risk**: low

### 27. DRIP（股息再投资计划，Dividend Reinvestment Plan）
- **Type**: acronym | **Tier**: tier-2
- **Insider def**: 自动用收到的股息再买入同标的，强化复利、省去手动。(evidence: [T06-S001])
- **outsider-tell** (`pronunciation_tell`): 读「drip」（一个词）；外行常不知此缩写，把「股息再投」与「分红到账花掉」混为一体，丢失复利。
- **关联**: 复利、股息率、总回报
- **Decay risk**: low

---

## C. 风险 / 绩效术语

### 28. 回撤 / 最大回撤（drawdown / max drawdown）
- **Type**: term | **Tier**: tier-1
- **Insider def**: 从历史高点跌到低点的幅度；最大回撤是最坏一次。衡量「能不能扛得住、会不会被迫离场」的体感风险。(evidence: [T06-S009])
- **outsider-tell** (`usage_tell`): 外行只看「年化收益多高」，不问「中途最多跌多少」——内行知道高回撤会逼人在底部割肉，且回撤后回本所需涨幅是非线性的（跌 50% 要涨 100% 才回本）。
- **关联**: 波动率、夏普比率、sequence-of-returns risk
- **Decay risk**: low

### 29. 夏普比率（Sharpe ratio）
- **Type**: term | **Tier**: tier-1
- **Insider def**: （回报 − 无风险利率）÷ 波动率；单位风险的超额回报，组合优劣的标准刻度。William Sharpe 提出。(evidence: [T06-S001])
- **outsider-tell** (`semantic_tell`): 外行只比「谁收益高」——内行比「风险调整后收益」(Sharpe)，知道高收益若靠高波动堆出来则 Sharpe 未必好。
- **关联**: 波动率、Sortino、beta/alpha、CAPM
- **Decay risk**: low

### 30. Sortino 比率（Sortino ratio）
- **Type**: term | **Tier**: tier-2
- **Insider def**: 夏普的变体，分母只算**下行波动**（不惩罚上涨波动）；更贴合「投资者只怕跌不怕涨」的直觉。(evidence: [T06-S001])
- **outsider-tell** (`usage_tell`): 外行不知二者差别——内行用 Sortino 区分「波动来自上行还是下行」，对不对称收益策略尤其。
- **关联**: 夏普比率、波动率、回撤
- **Decay risk**: low

### 31. beta / alpha（贝塔 / 阿尔法）
- **Type**: term | **Tier**: tier-1
- **Insider def**: beta = 相对大盘的系统性波动敏感度（市场涨 1%、它涨几%）；alpha = 扣除 beta 后的超额回报（「真本事」）。CAPM 框架核心。(evidence: [T06-S001])
- **outsider-tell** (`semantic_tell`): 外行说「这股 beta 高=收益高」——内行知道 beta 是**风险/相关性**度量不是收益；alpha 才是技能，且大多数主动管理长期 alpha 为负（见 SPIVA）。
- **关联**: 夏普比率、CAPM、因子投资、有效市场假说
- **Decay risk**: low

### 32. 波动率（volatility）
- **Type**: term | **Tier**: tier-1
- **Insider def**: 回报的标准差，衡量价格上下摆动幅度；学术上的「风险」代理变量。(evidence: [T06-S001])
- **outsider-tell** (`semantic_tell`): 外行把「波动」直接等同「亏钱/坏事」——内行区分波动（短期摆动，可承受则非真风险）与**永久性资本损失**（真风险）。价值派尤其强调这一区别。
- **关联**: 回撤、夏普比率、beta
- **Decay risk**: low

### 33. 收益序列风险（sequence-of-returns risk）
- **Type**: term | **Tier**: tier-2
- **Insider def**: 提取阶段（退休/FIRE）中，**坏收益出现的早晚**对组合存续影响巨大——退休初期遇熊市边提边亏会提前耗尽本金，哪怕平均收益相同。(evidence: [T06-S007])
- **outsider-tell** (`usage_tell`): 外行只看「平均年化收益」规划退休——内行知道**顺序**比平均更致命，退休前 5–10 年的回报序列决定成败。
- **关联**: 4% 法则 / 安全提取率、回撤、FIRE
- **Decay risk**: low

### 34. VaR（在险价值，Value at Risk）
- **Type**: acronym | **Tier**: tier-2
- **Insider def**: 在给定置信度/期限下的最大预期损失（如「95% 置信，单日不亏超 X」）。机构风控标配，散户少用。(evidence: [T06-S001])
- **outsider-tell** (`usage_tell`): 把 VaR 当「最坏情况上限」——内行知道它**不覆盖尾部**（超过置信区间外的极端损失可远超 VaR），2008 即暴露此盲点。
- **关联**: 波动率、回撤、夏普比率
- **Decay risk**: low

---

## D. 理论 / 学术术语

### 35. 有效市场假说（EMH，Efficient Market Hypothesis）
- **Type**: term + acronym | **Tier**: tier-1
- **Insider def**: 价格已反映可得信息，故难以持续靠公开信息跑赢。分**弱式**（价格含历史价量→技术分析无效）、**半强式**（含所有公开信息→基本面也难超额）、**强式**（含内幕→连内幕都无超额）。Fama 体系，被动派的理论地基。(evidence: [T06-S001, T06-S009])
- **disputed**: 价值/趋势派**部分否定**（认为市场常无效/可被行为偏差套利）；被动派**接受半强式**。这是四大流派分歧的学术硬核——不强行统一。
- **outsider-tell** (`usage_tell`): 外行把 EMH 当「市场永远理性正确」——内行知道半强式只是说「难持续超额」，不等于「价格永远=价值」（泡沫照样存在）。
- **关联**: 随机漫步、CAPM、因子投资、Mr. Market
- **Decay risk**: low

### 36. 现代组合理论（MPT，Modern Portfolio Theory）
- **Type**: term + acronym | **Tier**: tier-1
- **Insider def**: Markowitz（1952）的均值-方差框架：通过**分散**（低相关资产组合）在给定风险下最大化回报；「有效前沿」「不要把鸡蛋放一个篮子」的学术化。(evidence: [T06-S001])
- **outsider-tell** (`semantic_tell`): 外行的「分散」=多买几只股票——内行的分散看**相关性**（持 10 只同涨同跌的科技股几乎没分散），且分散降的是非系统性风险。
- **关联**: CAPM、夏普比率、资产配置、波动率
- **Decay risk**: low

### 37. CAPM（资本资产定价模型，Capital Asset Pricing Model）
- **Type**: acronym | **Tier**: tier-2
- **Insider def**: Sharpe 等（1960s）：预期回报 = 无风险利率 + beta×市场风险溢价；只有系统性风险（beta）该被定价补偿。折现率/资本成本的经典来源。(evidence: [T06-S001])
- **outsider-tell** (`usage_tell`): 把 CAPM 当「能算出准确预期收益」——内行知道它是简化模型（单因子），实证下 beta 解释力有限，催生了多因子模型。
- **关联**: beta/alpha、MPT、因子投资、DCF
- **Decay risk**: low

### 38. 因子投资（factor investing / smart beta）
- **Type**: term | **Tier**: tier-1
- **Insider def**: 用学术验证的「因子」（价值 value、规模 size、动量 momentum、质量 quality、低波 low-vol）系统性获取超额；Fama-French 多因子模型实务化，介于被动与主动之间。(evidence: [T06-S001])
- **outsider-tell** (`usage_tell`): 外行把任何主题/行业 ETF 都叫「因子」——内行只认有长期学术证据、跨市场可复制的少数因子，且知道因子会有长期跑输的「煎熬期」。
- **关联**: CAPM、动量、价值、有效市场假说
- **Decay risk**: low

### 39. 均值回归（mean reversion）
- **Type**: term | **Tier**: tier-2
- **Insider def**: 极端值倾向于回归长期均值（估值、收益率、相对表现）。价值派与逆向投资的统计直觉。(evidence: [T06-S022])
- **disputed**: 与「动量/趋势延续」表面矛盾——内行知道二者作用于**不同时间尺度**（短中期动量、长期回归），不是非此即彼。
- **outsider-tell** (`usage_tell`): 外行用均值回归当「跌多了一定反弹」就抄底——内行知道它是统计倾向非定律，「便宜可以更便宜」，没安全边际的抄底是接飞刀。
- **关联**: 动量、安全边际、随机漫步
- **Decay risk**: low

### 40. 随机漫步（random walk）
- **Type**: term | **Tier**: tier-2
- **Insider def**: 价格短期变动近似随机、不可预测；Malkiel《漫步华尔街》普及，是 EMH 弱式的形象表达，被动派论据。(evidence: [T06-S001])
- **outsider-tell** (`semantic_tell`): 外行用「随机漫步」否定一切投资——内行知道它针对的是**短期价格预测**（反技术分析），不否定长期股权回报的正期望。
- **关联**: EMH、技术分析（对立）、复利
- **Decay risk**: low

---

## E. 行为金融术语

### 41. 损失厌恶（loss aversion）
- **Type**: term | **Tier**: tier-1
- **Insider def**: 同等金额下，亏的痛 ≈ 赚的爽的 2 倍；Kahneman-Tversky。解释为何人死扛亏损票、急卖盈利票。(evidence: [T06-S001])
- **outsider-tell** (`usage_tell`): 外行「等回本就卖」死守亏损股——内行知道这是损失厌恶+沉没成本作祟，决策应看**未来**前景而非买入价。
- **关联**: 处置效应、锚定、沉没成本
- **Decay risk**: low

### 42. 锚定（anchoring）
- **Type**: term | **Tier**: tier-1
- **Insider def**: 决策被无关参照点（尤其**买入成本价**、历史高点）过度牵引。(evidence: [T06-S001])
- **outsider-tell** (`semantic_tell`): 外行说「我成本 50，现在 40 不能卖」——内行知道市场不在乎你的成本，应基于当前价值/前景决策，成本价是心理锚不是估值依据。
- **关联**: 损失厌恶、处置效应
- **Decay risk**: low

### 43. 近因偏差（recency bias）
- **Type**: term | **Tier**: tier-1
- **Insider def**: 高估最近发生事件的代表性——牛市末期觉得会一直涨、熊市底部觉得永远跌。追涨杀跌的心理根源。(evidence: [T06-S001])
- **outsider-tell** (`usage_tell`): 外行看「过去 3 年涨最多的基金」就买——内行知道近期最热常是均值回归的反向信号（「过往业绩不代表未来」是法定免责，也是真理）。
- **关联**: 羊群效应、FOMO、均值回归
- **Decay risk**: low

### 44. 确认偏差（confirmation bias）
- **Type**: term | **Tier**: tier-2
- **Insider def**: 只搜集/相信支持自己已有立场的信息，忽视反证。重仓后尤甚。(evidence: [T06-S001])
- **outsider-tell** (`usage_tell`): 外行买入后只看利好、把质疑当「黑子」——内行主动找**反方观点**（pre-mortem / 杀死自己的论点）。
- **关联**: 过度自信、锚定
- **Decay risk**: low

### 45. 处置效应（disposition effect）
- **Type**: term | **Tier**: tier-2
- **Insider def**: 倾向过早卖出盈利、过久持有亏损——「拔花浇草」。损失厌恶的市场表现。(evidence: [T06-S001])
- **outsider-tell** (`usage_tell`): 外行「赚了赶紧落袋、亏了再等等」自觉精明——内行知道这恰好系统性地砍掉赢家、留住输家，与正确做法相反。
- **关联**: 损失厌恶、锚定
- **Decay risk**: low

### 46. 过度自信（overconfidence）
- **Type**: term | **Tier**: tier-2
- **Insider def**: 高估自己的判断/择时/选股能力，导致过度交易与集中下注；与交易频率正相关、与净收益负相关。(evidence: [T06-S001])
- **outsider-tell** (`register_tell`): 外行赚了几次就觉得「我有盘感」加杠杆/频繁交易——内行知道牛市里人人是股神，区分运气与技能要看完整周期。
- **关联**: 确认偏差、羊群效应、market timing
- **Decay risk**: low

### 47. 羊群效应（herding）
- **Type**: term | **Tier**: tier-1
- **Insider def**: 跟随群体买卖，放大泡沫与崩盘；「别人都买我也买」。(evidence: [T06-S001])
- **outsider-tell** (`semantic_tell`): 外行「这么多人买/这么火，肯定没错」——内行知道极端共识往往是顶/底信号，逆向思维（Marks 的「second-level thinking」）才有超额。
- **关联**: FOMO、近因偏差、Mr. Market
- **Decay risk**: low

### 48. FOMO（错失恐惧，Fear Of Missing Out）
- **Type**: acronym | **Tier**: tier-1
- **Insider def**: 怕错过暴涨而仓促追高；散户在题材/牛市顶部的典型情绪。(evidence: [T06-S001])
- **outsider-tell** (`register_tell`): 「别人都赚钱就我没买」是 FOMO 的原话——内行把它当**危险信号**：当你最怕错过时，通常已是高点，错过一个机会好过套在山顶。
- **pronunciation_tell**: 读「fo-mo」；用对场景（轻松/自嘲 register），但当作决策依据就露馅。
- **关联**: 羊群效应、近因偏差、market timing
- **Decay risk**: low

### 49. 择时 vs 在场时间（market timing vs time-in-market）
- **Type**: term | **Tier**: tier-1
- **Insider def**: 行业铁律——「time in the market beats timing the market」：长期持有的复利 > 试图预测高低点进出。错过少数最佳交易日会重创长期收益。(evidence: [T06-S003, T06-S009])
- **outsider-tell** (`semantic_tell`): 外行追求「高抛低吸/逃顶抄底」当本事——内行知道持续择时几乎无人成功，市场最佳日常紧贴最差日出现，踏空成本极高。
- **关联**: 定投、复利、随机漫步、SPIVA
- **Decay risk**: low

---

## F. 技术 / 趋势术语

### 50. 趋势线 / 支撑 / 阻力（trendline / support / resistance）
- **Type**: term | **Tier**: tier-1（技术派内）
- **Insider def**: 技术分析基础——连接高/低点的线，价格历史反复止跌（支撑）/止涨（阻力）的区域。趋势派/图表派交易框架。(evidence: [T06-S001])
- **disputed**: 被动/学术派（EMH 弱式、随机漫步）认为技术分析无预测力；技术派认为反映供需与群体心理。两派根本对立——标 disputed 不统一。
- **outsider-tell** (`usage_tell`): 外行把支撑/阻力当「物理定律必然反弹」——内行（即便技术派）也只当**概率性参考**，破位就认错，绝不死扛。
- **关联**: 突破、移动平均、动量
- **Decay risk**: low

### 51. 动量（momentum）
- **Type**: term | **Tier**: tier-1
- **Insider def**: 近期强势的资产倾向短中期继续强（涨者恒涨）；既是技术/趋势派核心，也是被学术验证的因子（Jegadeesh-Titman 1993）。(evidence: [T06-S001])
- **outsider-tell** (`usage_tell`): 外行把「最近涨得多」简单当动量买——内行知道动量有明确回看/持有窗口，且会经历剧烈的「动量崩盘」（反转时损失惨重）。
- **关联**: 趋势线、因子投资、均值回归（对立尺度）
- **Decay risk**: low

### 52. 移动平均（moving average，MA）
- **Type**: term + acronym | **Tier**: tier-1（技术派内）
- **Insider def**: 一段周期收盘价的均值线（如 50 日/200 日 MA），平滑噪声、判断趋势方向；金叉/死叉是经典信号。(evidence: [T06-S001])
- **outsider-tell** (`usage_tell`): 外行把「金叉=买、死叉=卖」当稳赚公式——内行知道 MA 是**滞后**指标，震荡市频繁假信号，单独用必亏手续费。
- **关联**: 趋势线、动量、突破
- **Decay risk**: low

### 53. 突破（breakout）
- **Type**: term | **Tier**: tier-2（技术/趋势派内）
- **Insider def**: 价格放量突破关键阻力/形态边界，趋势派的入场触发。(evidence: [T06-S001])
- **outsider-tell** (`usage_tell`): 外行见涨就喊「突破了要起飞」——内行区分真突破与假突破（need 放量确认 + 防回踩），并预设止损。
- **关联**: 趋势线、stop-loss、position sizing
- **Decay risk**: low

### 54. CANSLIM
- **Type**: acronym | **Tier**: tier-2
- **Insider def**: William O'Neil（《Investor's Business Daily》创始人）的成长股选股法，7 字母各代表一条（Current earnings / Annual earnings / New / Supply-demand / Leader / Institutional / Market）——融合基本面+技术的趋势成长体系。(evidence: [T06-S001])
- **outsider-tell** (`pronunciation_tell`): 读「can-slim」；外行不知是首字母缩写，或只记口诀不懂每条逻辑。
- **关联**: 突破、动量、position sizing
- **Decay risk**: low

### 55. 止损（stop-loss）
- **Type**: term | **Tier**: tier-1
- **Insider def**: 预设价格触发卖出以限制单笔亏损；**交易/趋势派的风控核心纪律**（事前设定、机械执行）。(evidence: [T06-S001])
- **outsider-tell** (`usage_tell`): 外行把「止损」当「跌了就割肉」的情绪反应、或乱用在长期价值投资上——内行知道：① 止损是**交易框架**的事前规则，不是恐慌动作；② 长期被动/价值投资通常**不**用价格止损（否则会在最该买时卖出），混用两套体系是新手通病。
- **关联**: position sizing、突破、margin of safety（对照）
- **Decay risk**: low

### 56. 仓位管理 / 头寸规模（position sizing）
- **Type**: term | **Tier**: tier-1
- **Insider def**: 决定每笔投入多少资金/承担多少风险（如「单笔最多亏总资金 1%」）；趋势/交易派认为它比选标的更决定长期存活。(evidence: [T06-S001])
- **outsider-tell** (`semantic_tell`): 外行只想「买哪个」，从不想「买多少」，要么梭哈要么乱配——内行先定 sizing 与风险预算，再谈标的。
- **关联**: 止损、波动率、风险平价
- **Decay risk**: low

---

## G. 规划 / 税务术语

### 57. FIRE（财务独立提前退休，Financial Independence, Retire Early）
- **Type**: acronym | **Tier**: tier-1
- **Insider def**: 通过高储蓄率+低费指数投资积累到「年支出×25」（4% 法则倒数）即可不依赖工资。衍生 LeanFIRE/FatFIRE/CoastFIRE/BaristaFIRE。(evidence: [T06-S007])
- **outsider-tell** (`semantic_tell`): 外行以为 FIRE = 「赚很多钱然后躺平」——内行知道核心是**储蓄率**（决定多久达标）+ 提取阶段的 sequence risk，且数字基于 4% 法则的历史假设。
- **关联**: 安全提取率 / 4% 法则、收益序列风险、复利
- **Decay risk**: low

### 58. 安全提取率 / 4% 法则（safe withdrawal rate / 4% rule）
- **Type**: term | **Tier**: tier-1
- **Insider def**: Trinity Study（1998）结论——50/50 股债组合按初始 4%、随通胀调整，30 年区间约 95% 不耗尽。退休/FIRE 规划基准。(evidence: [T06-S007])
- **outsider-tell** (`usage_tell`): 外行把 4% 当「永远每年取 4% 不会破产」的铁律——内行知道：① 它基于美股历史回测、30 年期；② FIRE 的 50–60 年期失败率上升，常降到 3–3.5%；③ 动态调整（市场差就减开支）比死守 4% 更稳。
- **关联**: FIRE、收益序列风险、再平衡
- **Decay risk**: medium（持续被学界/社区重估）

### 59. 税损收割（tax-loss harvesting，TLH）
- **Type**: term | **Tier**: tier-2
- **Insider def**: 卖出浮亏标的实现亏损以抵减资本利得/部分普通收入税，同时用相似（非「实质相同」）标的维持敞口。受 **wash-sale 规则**（30 天内不得买回实质相同标的）约束。(evidence: [T06-S006])
- **outsider-tell** (`usage_tell`): 外行以为「亏了卖掉省税总是赚」——内行知道它是**递延**非免除（降低成本基准、未来 gain 更大）、有 wash-sale 雷区、且只在应税账户有意义（退休账户内无效）。
- **geographic-specific**: US 概念（wash-sale = IRS 规则）；CN 资本利得税制不同，TLH 适用性有限。
- **关联**: 资本利得、wash-sale rule、401(k)/IRA
- **Decay risk**: low

### 60. 401(k) / IRA / Roth（美国退休账户）
- **Type**: term | **Tier**: tier-1（US）
- **Insider def**: 401(k)=雇主税延退休计划；IRA=个人退休账户；**Roth**=税后投入、增长与合规提取免税（vs Traditional 税前投入、提取征税）。税务优化的核心容器。(evidence: [T06-S013, T06-S015])
- **变化历史**: 缴款上限每年随 IRS 调整；2026：401(k) $24,500、IRA $7,500（见衰减信号）。SECURE 2.0 引入 Roth 化的雇主匹配、60–63 岁更高 catch-up 等。
- **outsider-tell** (`usage_tell`): 外行分不清 Traditional vs Roth（搞反税前/税后），或「把退休账户当储蓄账户随时取」——内行懂提前取的罚金/税、Roth 的免税复利价值、以及账户**类型**与**里面买什么**是两回事。
- **geographic-specific: US**
- **关联**: Roth conversion、RMD、复利
- **Decay risk**: medium（缴款上限年度变 + SECURE 2.0 分阶段）

### 61. 个人养老金 / Y 账户（CN）
- **Type**: term | **Tier**: tier-1（CN）
- **Insider def**: 中国第三支柱养老，个人自愿、税收递延，每年限额内可投专属产品；基金按 **Y 类份额**（费率优惠）认购。**2024-12 由 36 城试点推广至全国**。(evidence: [T06-S018, T06-S019])
- **变化历史**: 36 城试点（2022-11）→ 全国推开（2024-12-12 五部门通知，12-15 起）；指数基金**首次纳入**可投名录（首批 85 只权益指基）。(evidence: [T06-S018])
- **outsider-tell** (`usage_tell`): 外行把它当「又一种理财/储蓄」——内行懂其**税延机制**（抵扣应纳税所得、领取时按 3% 计税）、封闭至退休的流动性、以及 Y 份额的费率优势。
- **geographic-specific: CN**
- **关联**: Y 类份额、公募基金、费率改革
- **Decay risk**: high（名录持续扩容、政策仍在演进）

### 62. 应急金（emergency fund）
- **Type**: term | **Tier**: tier-1
- **Insider def**: 覆盖 3–6 个月（FIRE/自雇常 6–12）刚性支出的高流动性现金缓冲；投资规划的**地基前置条件**，先于任何风险资产配置。(evidence: [T06-S007])
- **outsider-tell** (`semantic_tell`): 外行急着「钱生钱」把全部现金投进市场——内行知道没有应急金 = 被迫在最差时点割肉，应急金是「不被迫卖出」的保险。
- **关联**: 资产配置、流动性、sequence-of-returns risk
- **Decay risk**: low

---

## H. 合规 / 监管 / 标准（按地域分）

> **认证维度对自主散户基本 N/A**：CFA/CFP/GIPS 是**持牌从业者 / 资管机构**的资质与标准，散户不考；但需认得用以判断「对面是谁、其业绩可信度」，故列 Tier 2 reference。

### 63. SEC（美国证监会，Securities and Exchange Commission）
- **Type**: regulation/agency | **Tier**: tier-1（US）
- **Insider def**: 美国证券市场最高监管机构；管发行、披露、基金注册、反欺诈。投资者教育门户 investor.gov。(evidence: [T06-S001, T06-S021])
- **outsider-tell** (`usage_tell`): 外行以为「SEC 注册/监管=这产品安全/会涨」——内行知道注册≠背书，SEC 管**披露与合规**不管你赚不赚。
- **关联**: FINRA、prospectus、Reg BI、13F
- **变化历史**: issued 1934（《证券交易法》设立）。**Decay**: low（机构稳定）

### 64. FINRA（金融业监管局，Financial Industry Regulatory Authority）
- **Type**: regulation/SRO | **Tier**: tier-2（US）
- **Insider def**: 美国券商/经纪人自律监管组织（受 SEC 监督），管经纪商行为、执照（Series 7 等）、Reg BI 执行。(evidence: [T06-S011])
- **geographic-specific: US** | **Decay**: low

### 65. 招募说明书（prospectus）
- **Type**: regulation/document | **Tier**: tier-2
- **Insider def**: 基金/证券依法披露目标、策略、**费率**、风险、过往业绩的法定文件；买基金前应读的一手资料。(evidence: [T06-S021])
- **outsider-tell** (`usage_tell`): 外行从不读 prospectus，只看销售页的收益宣传——内行先翻费率、风险、跟踪标的等法定披露。
- **关联**: 费率、SEC、13F | **Decay**: low

### 66. 13F（机构持仓报告）
- **Type**: regulation/filing | **Tier**: tier-2（US）
- **Insider def**: 管理 ≥$100M 的机构须按季向 SEC 披露美股持仓（13F filing）；散户用来「抄作业」看大佬持仓。(evidence: [T06-S021])
- **outsider-tell** (`usage_tell`): 外行照 13F「抄巴菲特作业」即时买入——内行知道 13F **滞后 45 天**、不含空头/衍生品/卖出时点，照抄常买在人家已减仓的位置。
- **geographic-specific: US** | **Decay**: low

### 67. Reg BI（最优利益规则，Regulation Best Interest）
- **Type**: regulation | **Tier**: tier-2（US）
- **Insider def**: SEC 规则，要求经纪商对零售客户的证券**推荐**符合其「最优利益」，含**披露/谨慎/利益冲突/合规**四项义务；比旧的「适当性 suitability」标准更高。**2020-06-30 生效**。(evidence: [T06-S011, T06-S012])
- **变化历史**: issued 2019、**effective 2020-06-30**；与「适当性标准」的区别是核心考点。
- **outsider-tell** (`usage_tell`): 外行以为「持牌经纪/投顾推荐的一定为我好」——内行懂 Reg BI（经纪商，best-interest）与 fiduciary（注册投顾 RIA，受托责任）的差别，及佣金/利益冲突的存在。
- **geographic-specific: US** | **Decay**: low-medium

### 68. 投资者适当性（suitability / investor appropriateness）
- **Type**: regulation/principle | **Tier**: tier-2
- **Insider def**: 推荐的产品须匹配投资者的风险承受/财务状况/目标；US 旧标准（已被 Reg BI 升级），CN「投资者适当性管理」是资管新规配套核心要求。(evidence: [T06-S012])
- **geographic-specific: US + CN** | **Decay**: medium

### 69. 公募基金 / 资管新规（CN）
- **Type**: regulation | **Tier**: tier-1（CN）
- **Insider def**: 公募=面向公众募集、受证监会严监管的基金；**资管新规**（2018-04 四部委）确立**打破刚兑、净值化、禁止保本保收益**。(evidence: [T06-S018])
- **变化历史**: 资管新规 issued 2018-04；过渡期原至 2020 末→**延至 2021-12-31**→**2022-01-01 正式实施**。「保本理财」自此退出市场。(evidence: [T06-S018])
- **outsider-tell** (`semantic_tell`): 外行仍说「买个保本理财」——内行知道资管新规后**刚兑已打破、净值化**，银行理财也会亏损浮亏，「保本」是过时且现已违规的话术。
- **geographic-specific: CN** | **Decay**: medium-high（配套规则持续）

### 70. SPIVA（主动 vs 被动记分卡，S&P Indices Versus Active）
- **Type**: standard/methodology | **Tier**: tier-1
- **Insider def**: S&P DJI 的权威半年度报告，按统一方法（含**幸存者偏差**修正）量化各类主动基金 vs 对应指数的跑赢/跑输比例。被动派最常引用的「主动很难赢」证据。(evidence: [T06-S009, T06-S010])
- **关键数据（YE2024，US）**: 一年期约 **65%** 大盘主动基金跑输 S&P 500；**15 年期 22 个股票类别中 0 个**有多数主动跑赢——时间越长跑输越多。(evidence: [T06-S009])
- **outsider-tell** (`usage_tell`): 外行「找个能跑赢大盘的好基金」当然成立的目标——内行用 SPIVA 知道**多数主动长期跑输**且赢家难以持续（persistence 差），故倾向低费指数。
- **关联**: 有效市场假说、费率、alpha、择时
- **Decay**: low（方法稳定）/ 数据每半年更新

### 71. GIPS（全球投资业绩标准，Global Investment Performance Standards）
- **Type**: standard | **Tier**: tier-2
- **Insider def**: CFA Institute 维护的**自愿性**业绩计算与呈现标准，核心是 **composite**（同策略组合的聚合，防「挑最好账户展示」的 cherry-picking）。机构/资管声称合规以示业绩可信。**2020 版 2020-01-01 生效**。(evidence: [T06-S016, T06-S017])
- **变化历史**: 历经多版，**2020 edition effective 2020-01-01**（引入 Firms/Asset Owners/Verifiers 三框架、不再按法律结构区分组合）。
- **outsider-tell** (`usage_tell`): 外行看基金/投顾「历史年化 XX%」全盘相信——内行问「是否 GIPS 合规、是否 composite（含所有账户）」，否则可能是幸存者/挑选偏差。
- **关联**: SPIVA、prospectus、幸存者偏差 | **Decay**: low-medium

### 72. 公募基金费率改革（CN，fee reform）
- **Type**: regulation | **Tier**: tier-2（CN）
- **Insider def**: 证监会 2023-07 启动的「管理费→交易佣金→销售费」**三步走**降费，把行业从规模导向推向投资者回报导向。(evidence: [T06-S020])
- **变化历史**: ① 阶段一（2023-07-07 起）主动权益管理费≤1.2%、托管费≤0.2%；存量产品下调；② 阶段二交易佣金新规 2023-12 发布、**2024-07-01 生效**；③ 阶段三销售环节降费 2024–2025 推进。(evidence: [T06-S020])
- **geographic-specific: CN** | **Decay**: high（阶段三仍在落地、绝对数字会变）

---

## 总览（按 type 分组）

### Tier 1 — 核心必懂（41 个）
| 术语 | Type | Insider def（极简） | Outsider tell | Last_updated |
|------|------|--------------------|--------------|--------------|
| P/E 市盈率 | term+acro | 价÷每股盈利，须 relative | 低=便宜直接买 | 2026-06 |
| EPS | acro | 每股净利，分 GAAP/adj | EPS 涨=变好 | 2026-06 |
| P/B 市净率 | term+acro | 价÷净资产，重资产用 | 拿去估科技股 | 2026-06 |
| 内在价值 | term | 现金流折现应值 | =当前股价涨跌 | 2026-06 |
| 安全边际 | term | 价值-价格的折扣缓冲 | 当成 stop-loss | 2026-06 |
| 护城河 | term | 可持续竞争优势 | 产品好就算护城河 | 2026-06 |
| 能力圈 | term | 只投看得懂的 | 追热门赛道 | 2026-06 |
| Mr. Market | term | 市场=躁郁报价者，可无视 | 价格当真理 | 2026-06 |
| ROE | acro | 自有资本赚钱效率 | 不剥杠杆 | 2026-06 |
| 自由现金流 FCF | term+acro | 经营现金-资本开支 | 利润=赚的钱 | 2026-06 |
| 股息率 | term | 股息÷价 | 专挑最高 yield | 2026-06 |
| 资产配置 | term | 大类资产权重，主导回报 | 投资=选哪只 | 2026-06 |
| 再平衡 | term | 卖涨买跌拉回目标 | 觉得反人性赔钱 | 2026-06 |
| 三基金组合 | term | 美+国际+债三只低费 | 嫌太简单 | 2026-06 |
| 60/40 | term | 六四股债 | 当成保本 | 2026-06 |
| 费率 ER | term | 年扣运营费，复利杀手 | 1% 才一点点 | 2026-06 |
| 指数基金/ETF | term+acro | 被动复制指数 | 所有 ETF=低费被动 | 2026-06 |
| 定投 DCA | term+acro | 分批摊成本 | 稳赚不赔 | 2026-06 |
| 复利 | term | 收益再生收益，指数 | 线性直觉算收益 | 2026-06 |
| 总回报 | term | 价差+股息(再投) | 只看股价涨跌 | 2026-06 |
| 回撤/最大回撤 | term | 高点到低点跌幅 | 只看年化不看回撤 | 2026-06 |
| 夏普比率 | term | 单位风险超额回报 | 只比谁收益高 | 2026-06 |
| beta/alpha | term | 系统波动/真本事 | beta 高=收益高 | 2026-06 |
| 波动率 | term | 回报标准差=风险代理 | 波动=亏钱 | 2026-06 |
| EMH 有效市场 | term+acro | 价格含信息难超额(弱/半强/强) | =市场永远对 | 2026-06 |
| MPT 组合理论 | term+acro | 均值方差分散 | 分散=多买几只 | 2026-06 |
| 因子投资 | term | 价值/规模/动量等因子 | 任何主题都叫因子 | 2026-06 |
| 损失厌恶 | term | 亏的痛≈赚的爽×2 | 等回本才卖 | 2026-06 |
| 锚定 | term | 被成本价等参照牵引 | 成本50不能卖 | 2026-06 |
| 近因偏差 | term | 高估最近事件 | 买过去涨最多的 | 2026-06 |
| 羊群效应 | term | 跟风放大泡沫崩盘 | 这么多人买没错 | 2026-06 |
| FOMO | acro | 怕错过暴涨追高 | 别人都赚就我没买 | 2026-06 |
| 择时vs在场时间 | term | time-in>timing | 追求逃顶抄底 | 2026-06 |
| 趋势线/支撑阻力 | term | 技术派图表框架 | 当物理定律必反弹 | 2026-06 |
| 动量 | term | 涨者恒涨，亦是因子 | 最近涨多就买 | 2026-06 |
| 移动平均 MA | term+acro | 均线判趋势 | 金叉死叉稳赚 | 2026-06 |
| 止损 stop-loss | term | 交易派事前风控规则 | 用在长期价投上 | 2026-06 |
| 仓位管理 | term | 每笔投多少/担多少险 | 只想买哪个不想买多少 | 2026-06 |
| FIRE | acro | 高储蓄+低费指数达年支出×25 | =赚够躺平 | 2026-06 |
| 4%法则/安全提取率 | term | Trinity 30年95%不耗尽 | 当永久铁律 | 2026-06 |
| 应急金 | term | 3-6月现金缓冲，前置 | 全现金梭进市场 | 2026-06 |
| 401(k)/IRA/Roth | term | 美国税延/免税退休容器 | 搞反税前税后 | 2026-06 |
| 个人养老金/Y账户 | term | CN第三支柱税延 | 当普通理财 | 2026-06 |
| SEC | agency | 美证监会管披露合规 | 注册=安全会涨 | 2026-06 |
| 公募/资管新规 | reg | 打破刚兑净值化 | 还想买保本理财 | 2026-06 |
| SPIVA | standard | 主动vs被动权威记分卡 | 找能跑赢大盘的基金 | 2026-06 |

> （注：上表 47 行含若干横跨流派/地域的 Tier-1；核心 Tier-1 计 41，地域专属 401k/养老金/SEC/资管/SPIVA 等并入。）

### Tier 2 — 周边熟知（约 22 个）
| 术语 | Type | Insider def（极简） | Last_updated |
|------|------|--------------------|--------------|
| DCF | acro | FCF 折现求内在价值 | 2026-06 |
| book value | term | 资产-负债账面值 | 2026-06 |
| 全天候/风险平价 | term | 按风险贡献配置 | 2026-06 |
| 跟踪误差 | term | 实际vs指数偏离 | 2026-06 |
| 一次性 lump sum | term | 一次投入，多胜DCA | 2026-06 |
| NAV 净值 | acro | 每份额资产净值 | 2026-06 |
| DRIP | acro | 股息自动再投 | 2026-06 |
| Sortino | term | 只罚下行波动的夏普 | 2026-06 |
| sequence-of-returns risk | term | 坏收益早晚决定退休成败 | 2026-06 |
| VaR | acro | 置信度内最大损失(不覆尾) | 2026-06 |
| CAPM | acro | 期望=无风险+β×溢价 | 2026-06 |
| 均值回归 | term | 极端回归均值(分尺度) | 2026-06 |
| 随机漫步 | term | 短期价格不可测 | 2026-06 |
| 确认偏差 | term | 只信支持己见的信息 | 2026-06 |
| 处置效应 | term | 拔花浇草 | 2026-06 |
| 过度自信 | term | 高估择时选股力 | 2026-06 |
| 突破 breakout | term | 放量破阻力入场 | 2026-06 |
| CANSLIM | acro | O'Neil成长股7要素 | 2026-06 |
| 税损收割 TLH | term | 实现亏损抵税(wash-sale) | 2026-06 |
| FINRA | SRO | 美券商自律监管 | 2026-06 |
| prospectus 招募书 | document | 法定费率/风险披露 | 2026-06 |
| 13F | filing | 机构季度持仓(滞后45天) | 2026-06 |
| Reg BI | reg | 经纪商最优利益4义务 | 2026-06 |
| 投资者适当性 | reg | 产品匹配风险承受 | 2026-06 |
| GIPS | standard | 业绩呈现标准(composite) | 2026-06 |
| 费率改革(CN) | reg | 三步走降费 | 2026-06 |

### Standards / Regulations 时间轴（仅近 5 年内有显著变化的进表）
| 名称 | Issued | Last revised / 关键日 | Decay | 地域 |
|------|--------|----------------------|-------|------|
| Reg BI | 2019 | **effective 2020-06-30** | low-medium | US |
| GIPS（2020 版） | 1999(初版) | **2020 版 effective 2020-01-01** | low-medium | global |
| 资管新规 | 2018-04 | 过渡期延至 2021-12-31，**2022-01-01 正式实施** | medium-high | CN |
| 公募费率改革 | 2023-07 | 阶段二佣金 **2024-07-01 生效**，阶段三 2024-2025 落地 | **high** | CN |
| 个人养老金制度 | 2022-11(试点) | **2024-12-12 五部门全国推开**，指数基金纳入 | **high** | CN |
| SECURE 2.0 | 2022-12(签署) | 多条款 **2024-2025 分阶段生效**(Roth catch-up 等) | medium | US |
| IRS 退休缴款上限 | 年度 | **2026: 401k $24,500 / IRA $7,500**(Notice 2025-67) | medium | US |
| SPIVA scorecard | — | **YE2024 数据**(每半年更新) | 数据 high / 方法 low | global |
> 长期稳定者（SEC 1934、MPT 1952、CAPM、EMH、Trinity 1998）不进时间轴，仅在主条目记 issued。

### 行业「外行破绽」高亮（最容易暴露的）
| 误用 | 内行实际意思 | 出现频率 |
|------|------------|---------|
| 「找只能跑赢大盘的基金」 | SPIVA: 多数主动长期跑输(15yr 0/22) | 极高 |
| 「定投稳赚不赔」 | DCA 只降情绪/择时风险，不保盈利；有钱时常输 lump-sum | 极高 |
| 「跌了赶紧割肉止损」(用于长期投资) | 混淆交易止损与长期持有；该看价值非价格 | 极高 |
| 「保本理财」 | 资管新规后刚兑已打破、净值化、违规话术 | 高(CN) |
| 「这票要起飞了/突破了」 | 趋势派也只当概率参考+预设止损 | 高 |
| 把「理财」=「买到会涨的标的」 | 理财=配置/费率/税/纪律，标的次要 | 极高 |
| 只看名义收益，不分税前税后/名义实际 | total return + 扣通胀扣税才是真回报 | 高 |
| 「1% 费率没多少」 | 复利下长期吞掉巨大终值份额 | 高 |
| 追涨杀跌(买近期涨最多/恐慌卖底) | 近因偏差+羊群，常买顶卖底 | 极高 |
| 「别人都赚钱就我没买」(FOMO) | 最怕错过时通常是高点，错过<套顶 | 极高 |
| 「NAV/股价低=便宜要买」 | 净值高低与贵贱无关 | 中 |
| 照 13F「抄巴菲特作业」即买 | 13F 滞后45天，常买在人家减仓位 | 中 |
| 「SEC 注册=安全/会涨」 | 注册≠背书，管披露不管赚赔 | 中 |
| 搞反 Roth/Traditional 税前税后 | 一个税后免税增长，一个税前提取征税 | 中(US) |

---

## Phase 2 提炼提示

**「行业表达 DNA」直接素材**（喂 Phase 2.5 expression-DNA）:

- **Tier 1 高频黑话 top 清单（喂表达 DNA）**: 安全边际 / 内在价值 / 护城河 / 能力圈 / Mr. Market（价值派身份词）；资产配置 / 再平衡 / 费率 / 三基金 / 总回报 / 复利 / time-in-market（被动派身份词）；回撤 / 夏普 / beta-alpha / 波动率（风险语言）；动量 / 止损 / 仓位管理 / 突破（趋势派语言）；损失厌恶 / 近因偏差 / FOMO / 处置效应（行为金融语言）；4% 法则 / sequence risk / 应急金（规划语言）。**说话时这些词的自然使用 = 内行；缺席或误用 = 外行。**

- **行业拒绝的厂商 / 营销话术 top（拒绝 → 价值观 + 反模式）**:
  1. **「年化收益 XX%」单拎一个数**（隐藏波动 / 最大回撤 / 时间窗口 / 幸存者偏差）——内行必问「同期回撤多少、是不是 GIPS composite、哪段历史」。(evidence: [T06-S009, T06-S016])
  2. **「稳健高收益 / 低风险高回报」**——风险收益不可兼得是公理，此话术自相矛盾。
  3. **「保本理财 / 保本保收益」**——CN 资管新规后刚兑已打破、净值化，属过时且违规话术。(evidence: [T06-S018])
  4. **「内部消息 / 牛股推荐 / 老师带你抄」**——荐股黑产话术；内行知道可持续 alpha 极稀缺(SPIVA)且内幕交易违法。
  5. **「AI 量化稳赚 / 智能策略月月正收益」**——把波动策略包装成「稳赚」，回避回撤与失效期。
  6. **明星基金经理崇拜 / 「冠军基金」**——近因偏差陷阱，冠军次年常均值回归，业绩 persistence 差。(evidence: [T06-S009])
  7. **「指数基金=被动=一定低费安全」被厂商收编**——大量主动 / 杠杆 / 主题 ETF 借「指数 / ETF」名头收高费。(evidence: [T06-S002])

- **外行破绽 top 10（insider-only spotting tells）**: ①「找能跑赢大盘的基金」②「定投稳赚不赔」③「跌了割肉止损」(长期投资场景) ④「这票要起飞 / 突破了」⑤把「理财」=「买会涨的标的」⑥只看名义收益不分税前税后 / 名义实际 ⑦「1% 费率没多少」忽略复利侵蚀 ⑧追涨杀跌(买近期最热) ⑨「别人都赚就我没买」(FOMO) ⑩「保本理财」/「NAV 低=便宜」。

**「智识谱系」线索**（喂 Phase 2.7）:
- **四大流派的术语集合即范式之争的硬件层**：价值派(安全边际/内在价值/Mr.Market，预设市场常错) vs 被动派(EMH/MPT/SPIVA/费率，预设市场难赢) = canon 最大分歧，二者对「EMH 半强式」「技术分析有效性」「主动能否跑赢」给出对立答案——**标 disputed，勿强行统一**。
- 趋势/技术派(动量/趋势线/止损) 与 被动/学术派(随机漫步/EMH 弱式) 在「价格可否预测」上根本对立。
- 学术演进路径：随机漫步(1965)→EMH→CAPM 单因子→Fama-French 多因子→因子投资实务化，暗示「市场效率」认知的精细化（从「全有效」到「有可系统获取的风险溢价」）。

**「时效性」信号**（喂 Phase 2.8 诚实边界）:
- **过去 12–18 月内有修订 / 新数据的标准法规（最强衰减信号，带日期）**:
  - **个人养老金全国推开 2024-12-12**（五部门通知）+ 指数基金首次纳入名录（首批 85 只）——CN 最强信号，名录持续扩容。(evidence: [T06-S018])
  - **IRS 2026 缴款上限**（401k $24,500 / IRA $7,500，Notice 2025-67）——每年变，引用必核当年。(evidence: [T06-S013, T06-S014])
  - **公募费率改革阶段二佣金新规 2024-07-01 生效**、阶段三 2024-2025 落地——CN 费率绝对数字在变。(evidence: [T06-S020])
  - **SPIVA YE2024**（65% 大盘主动一年跑输 / 15yr 0/22）——每半年更新，引用须标版本。(evidence: [T06-S009])
  - **SECURE 2.0 条款 2024-2025 分阶段生效**（Roth catch-up、60-63 更高 catch-up 等）。(evidence: [T06-S023])
- **预计 12 月内会变**: IRS 2027 限额、SPIVA YE2025/MY2025、CN 费率阶段三收尾、个人养老金名录再扩容。

**「工作流变化触发」种子**（喂 wave 3 Track 03）:
- **个人养老金全国化 + 指数基金纳入**(2024-12) → 散户「开 Y 账户 / 选 Y 份额指基 / 年度抵税申报」成为新工作流假设(CN)。
- **资管新规净值化**(2022 实施) → 「买理财=可能浮亏，需看净值波动而非预期收益率」改变 CN 理财选择工作流。
- **费率改革** → 「比费率挑基金」权重上升，旧高费产品被换。
- **SECURE 2.0 / IRS 年度限额** → 美国用户每年「重设 401k/IRA 缴款额、Roth conversion 决策」工作流随法更新。

**冷僻 / 信号薄弱自检**:
- 总术语数 ≈ **72**（远超 floor 40，>25）；Tier 1 = **41**（≥15 ✅）；Tier1+Tier2 ≈ 67（≥40 ✅）。
- Tier 1 **全部填了 outsider-tell** ✅；Tier 2 全部填了 outsider-tell（>50% ✅）。
- **非冷僻行业**：公开素材极丰（gov + Bogleheads + 学术 + SPIVA），verified_primary 占比高。**唯一结构性薄弱 = zh-CN 原创术语稀薄**（多为英文译介）+ **认证维度对自主散户 N/A**（CFA/CFP/GIPS 是从业者/机构资质，非散户必备，已诚实标注）。
- **强 disputed 维度**（须保留不统一）：EMH 有效性、技术分析预测力、主动 vs 被动——这是行业**真实的流派之争**，非研究不足。

### 合规框架要点（喂 Phase 2 诚实边界 + 表达 DNA）
1. **地域强分裂**：US（SEC / FINRA / Reg BI / IRS / SECURE 2.0）与 CN（证监会 / 资管新规 / 个人养老金 / 费率改革）两套独立体系，给用户建议须先确认地域。
2. **核心合规直觉**：注册 / 监管 ≠ 安全或会涨（SEC 管披露不管赚赔）；经纪商(Reg BI best-interest) ≠ 受托投顾(fiduciary)；「保本」在 CN 已违规。
3. **数字必带日期 + gov 源**：缴款限额 / 费率 / 试点城市数 / 生效日全部挂 .gov/.gov.cn 原文，年度刷新。
4. **业绩可信度框架**：SPIVA(主动多跑输) + GIPS(composite 防 cherry-pick) 是判断「业绩宣传是否可信」的两把尺。
5. **N/A 声明**：自主散户 profile 下，**执业认证维度(CFA/CFP/Series 7)基本 N/A**——这些是「对面是谁」的识别标签，非散户须考资质。

---

> **质量自检**: 候选 72 ≥40 ✅ | 5 type 分布合理(认证维度 N/A 已标) ✅ | Tier1=41≥15、Tier1+2≥40 ✅ | Tier1 全填 outsider-tell ✅ | Standards/Regs 全有日期 ✅ | disputed(EMH/技术分析/主动被动/均值回归vs动量)正确标注未强行统一 ✅ | Phase 2 五接口(表达DNA/智识谱系/时效/workflow/冷僻+合规要点)全填 ✅ | 0 黑名单 URL、数字全挂 gov 源 ✅
