# Track 02 — Tools 研究输出：个人投资理财 (Personal Investing & Financial Planning)

> locale = **global**（英文 canon 母语区 + zh-CN 散户实践层）。自主投资者管理自己组合的工具栈。
> 调研日期 2026-06-04。四大流派分叉：价值 / 被动指数 / 技术 / 趋势跟踪。
> **非投资建议**：本文是工具栈认知图谱，不构成任何具体证券或买卖时点的建议。

## Source Manifest

| source_id | url | bucket | last_checked | author/host | one-line note |
|-----------|-----|--------|--------------|-------------|---------------|
| T02-S001 | https://investor.vanguard.com | verified_primary | 2026-06-04 | Vanguard | 低费率指数基金/ETF 鼻祖券商，成本至上派 |
| T02-S002 | https://www.fidelity.com | verified_primary | 2026-06-04 | Fidelity | 全能券商，zero-ER 指数基金 + 研究 + 分数股 |
| T02-S003 | https://www.schwab.com/intelligent-portfolios | verified_primary | 2026-06-04 | Charles Schwab | robo 自动投资官方页（基础版无顾问费） |
| T02-S004 | https://www.schwab.com/direct-indexing | verified_primary | 2026-06-04 | Charles Schwab | Schwab Personalized Indexing 直接指数化官方页 |
| T02-S005 | https://www.interactivebrokers.com | verified_primary | 2026-06-04 | Interactive Brokers | 跨国多市场券商，分数股+低保证金利率 |
| T02-S006 | https://www.morningstar.com | verified_primary | 2026-06-04 | Morningstar | 基金评级/Portfolio X-Ray/风格箱/Medalist |
| T02-S007 | https://www.morningstar.com/help-center/portfolio/xray | verified_primary | 2026-06-04 | Morningstar | X-Ray 官方帮助文档：持仓穿透+overlap |
| T02-S008 | https://www.morningstar.com/funds/direct-indexing-landscape-3-charts | verified_primary | 2026-06-04 | Morningstar | 直接指数化市场规模/格局独立分析 |
| T02-S009 | https://www.portfoliovisualizer.com/ | secondary | 2026-06-04 | Portfolio Visualizer | 回测/Monte Carlo/因子回归/优化（vendor 一手） |
| T02-S010 | https://testfol.io/ | secondary | 2026-06-04 | testfol.io (solo dev) | 日频回测+sim 基金延长历史（vendor 一手） |
| T02-S011 | https://www.gurufocus.com/ | secondary | 2026-06-04 | GuruFocus | 价值派数据/DCF/F-Score/Z-Score（数据源 Morningstar） |
| T02-S012 | https://pages.stern.nyu.edu/~adamodar/New_Home_Page/data.html | verified_primary | 2026-06-04 | Aswath Damodaran (NYU Stern) | 估值数据集：ERP/beta/WACC/multiples，每年初更新 |
| T02-S013 | https://fred.stlouisfed.org/ | verified_primary | 2026-06-04 | St. Louis Fed | 84 万+宏观时间序列，免费，含 Excel add-in |
| T02-S014 | https://www.bogleheads.org/wiki/Three-fund_portfolio | verified_primary | 2026-06-04 | Bogleheads wiki | 三基金组合 canonical 定义+各券商对应 ticker |
| T02-S015 | https://www.bogleheads.org/wiki/ETFs_for_Bogleheads | verified_primary | 2026-06-04 | Bogleheads wiki | 核心宽基 ETF 选择（VTI/VXUS/BND/VT） |
| T02-S016 | https://www.bogleheads.org/wiki/Mutual_funds_for_Bogleheads | verified_primary | 2026-06-04 | Bogleheads wiki | 各券商低费率指基对比（VG/Fido/Schwab） |
| T02-S017 | https://www.lixinger.com/ | secondary | 2026-06-04 | 理杏仁 | A/港股估值数据(PE/PB 分位)+财报，价值派 zh-CN（vendor 一手） |
| T02-S018 | https://www.tradingview.com/ | secondary | 2026-06-04 | TradingView | 图表/形态/指标，技术派主力（vendor 一手） |
| T02-S019 | https://www.tradingview.com/pine-script-docs/welcome/ | secondary | 2026-06-04 | TradingView | Pine Script v6：策略回测+组合级计算 docs |
| T02-S020 | https://stockcharts.com/ | secondary | 2026-06-04 | StockCharts | 点数图/Kagi/市场宽度，专业图表派（vendor 一手） |
| T02-S021 | https://www.empower.com/investment-checkup | secondary | 2026-06-04 | Empower (原 Personal Capital) | 免费净值追踪+费用分析器+投资体检（vendor 一手） |
| T02-S022 | https://www.betterment.com | secondary | 2026-06-04 | Betterment | robo 鼻祖，目标导向+TLH（vendor 一手） |
| T02-S023 | https://www.wealthfront.com | secondary | 2026-06-04 | Wealthfront | robo，直接指数化+TLH 自动化（vendor 一手） |
| T02-S024 | https://etfdb.com/screener/ | secondary | 2026-06-04 | ETF Database | 2000+ ETF 多维筛选（vendor 一手） |
| T02-S025 | https://www.etf.com/etfanalytics/etf-screener | secondary | 2026-06-04 | etf.com | 4000+ ETF 筛选+对比，免费无需开户（vendor 一手） |
| T02-S026 | https://www.irs.gov/newsroom/401k-limit-increases-to-24500-for-2026-ira-limit-increases-to-7500 | verified_primary | 2026-06-04 | IRS | 2026 401(k)/IRA 缴费上限官方公告 |
| T02-S027 | https://www.irs.gov/pub/irs-drop/n-25-67.pdf | verified_primary | 2026-06-04 | IRS | Notice 2025-67：2026 退休账户限额 ground truth |
| T02-S028 | https://www.csrc.gov.cn/csrc/c101900/c6551799/content.shtml | verified_primary | 2026-06-04 | 中国证监会 | 个人养老金基金名录（截至 2026-03-31）官方 |
| T02-S029 | https://www.efunds.com.cn/lm/grd/grylj/ | secondary | 2026-06-04 | 易方达基金 | 个人养老金 Y 份额产品页（基金公司一手） |
| T02-S030 | https://qieman.com/ | secondary | 2026-06-04 | 且慢（盈米） | 基金组合+长盈计划投顾（vendor 一手） |
| T02-S031 | https://danjuanapp.com/ | secondary | 2026-06-04 | 蛋卷基金（雪球） | 指数估值+组合定投（vendor 一手） |
| T02-S032 | https://www.investmentnews.com/ria-news/as-schwab-shutters-hybrid-robo-josh-brown-declares-the-robo-advice-era-is-over/263663 | secondary | 2026-06-04 | InvestmentNews | Schwab 关停混合 robo Premium（2026 Q1）行业评论 |
| T02-S033 | https://www.fidelity.com/learning-center/personal-finance/401k-catch-up-contributions-high-earners | verified_primary | 2026-06-04 | Fidelity | 2026 Roth catch-up 高收入新规解读 |
| T02-S034 | https://www.tradingview.com/pricing/ | secondary | 2026-06-04 | TradingView | 订阅分层定价（vendor 一手） |
| T02-S035 | https://www.schwab.com/automated-investing/faqs | verified_primary | 2026-06-04 | Charles Schwab | Intelligent Portfolios FAQ：$5000 起、无顾问费 |

> 黑名单说明：知乎 / 公众号 / 百度百科 / CSDN / G2 / Capterra / Gartner / PR 通稿一律未入表。搜索过程中 zh-CN 结果大量来自知乎专栏 / 雪球长文 / 新浪财经转载，**均已剔除**，zh-CN 工具事实只采信厂商官网（理杏仁/且慢/蛋卷/易方达）+ 监管官方（证监会）。`advisors.vanguard.com` 子域被 verifier 判 secondary（非 investor.vanguard.com 主域），直接指数化的「democratization」claim 改挂 Morningstar 独立分析 [T02-S008]。

---

## 总览（按 tier 分组）

### 必备（5 个，≥80% 自主投资者会用）

| 工具 | 一句话 | Decay | Sources |
|------|--------|-------|---------|
| 一个低费率券商（Vanguard / Fidelity / Schwab） | 持有宽基指数 + 0 佣金股票/ETF 的执行层 | low | T02-S001,002,003,016 |
| 一支宽基指数 ETF/基金（VTI/VOO/VT/VTSAX + BND；CN: 沪深300/标普500 QDII） | 被动核心持仓，成本至上 | low | T02-S014,015 |
| Portfolio Visualizer | 回测/资产配置/因子/Monte Carlo 的事实标准 | low | T02-S009 |
| Morningstar | 基金尽调：评级/X-Ray 持仓穿透/费用/风格箱 | low | T02-S006,007 |
| 一个组合/净值追踪器（Empower 或 表格） | 跨账户聚合 + 费用分析 + 资产配置体检 | medium | T02-S021 |

### 场景特化（8 个，特定流派/场景用）

| 工具 | 一句话 | 流派/场景 | Decay | Sources |
|------|--------|-----------|-------|---------|
| Interactive Brokers (IBKR) | 跨国多市场 + 分数股 + 低保证金，活跃/海外标的 | 跨境/活跃 | low | T02-S005 |
| GuruFocus | DCF/内在价值/F-Score/Z-Score，美股价值尽调 | 价值派 | medium | T02-S011 |
| 理杏仁 lixinger | A/港股 PE/PB 历史分位 + 财报对比 | 价值派 zh-CN | medium | T02-S017 |
| Damodaran online data (NYU) | ERP/beta/WACC/行业 multiples 估值锚 | 价值派/估值 | low | T02-S012 |
| TradingView | 图表/形态/指标/Pine Script 回测 | 技术/趋势派 | low | T02-S018,019 |
| StockCharts | 点数图/Kagi/市场宽度，纯图表深度 | 技术派 | medium | T02-S020 |
| FRED | 宏观时间序列（利率/CPI/就业），趋势/择时背景 | 宏观/趋势 | low | T02-S013 |
| ETF 筛选器 (etf.com / ETFdb) | 按费率/规模/持仓筛选 ETF | 选品 | medium | T02-S024,025 |
| 税优账户类型（401k/IRA/Roth/HSA；CN 个人养老金 Y） | 「工具=账户结构」，税后收益最大杠杆 | low | T02-S026,027,028 |
| Robo-advisor (Betterment/Wealthfront；CN 帮你投/且慢) | 自动配置+再平衡+TLH，懒人托管 | 自动化 | medium | T02-S022,023,030 |

### 新兴（3 个，近 12 月起势）

| 工具 | 一句话 | Stability | Decay | Sources |
|------|--------|-----------|-------|---------|
| 直接指数化下沉零售 (Fidelity FidFolios $5k / Schwab Personalized Indexing) | 持有成分股而非 ETF，逐股 TLH + 定制 | emerging | high | T02-S004,008 |
| testfol.io | 日频回测 + sim 基金延长历史，社区新宠替代 PV | experimental | high | T02-S010 |
| AI 投顾 / 人机混合 (Robinhood Strategies / Vanguard Digital Advisor 升级) | LLM 驱动多场景投顾，robo 2.0 | experimental | high | T02-S032 |

---

## 必备层（详细卡片）

### 1. 低费率券商：Vanguard / Fidelity / Charles Schwab

- **One-liner**: 自主投资者的执行底座 —— 持有低费率宽基指数、0 佣金股票/ETF 交易、持有税优账户的容器。三家任一都够用，是「个人偏好问题」。
- **Tier**: 必备
- **Maintainer / Owner**: Vanguard (investor.vanguard.com) / Fidelity (fidelity.com) / Charles Schwab (schwab.com)
- **License**: proprietary（券商平台）
- **Maturity signals**: 三家均为行业基础设施，运营数十年；Bogleheads wiki 长期把三家并列为首选 (last checked: 2026-06-04) evidence: [T02-S016]
- **典型使用场景**:
  - Vanguard：低费率指数基金/ETF 选择最广，连主动基金费率也低；适合纯被动 buy-and-hold 长持 evidence: [T02-S016]
  - Fidelity：提供 zero-ER 指数基金 + 取消最低投资额 + 分数股 + 强研究；适合一站式全能 + 现金管理 evidence: [T02-S016]
  - Schwab：自家指基 + 接入他家基金（部分有交易费，除非在免交易费网络内）；界面对新手更友好 evidence: [T02-S016]
- **数字 caveat**: 三家美股股票/ETF 已普遍 0 佣金，宽基核心 ETF 费率已压到极低水平（以官网当前披露为准，**不要硬记具体 bps**）evidence: [T02-S016]
- **不适合 / 替代方案**: 需要大量海外市场（欧/澳/港/A 股）、分数股覆盖广、或低保证金利率 → 转 IBKR（见场景层）evidence: [T02-S005]
- **生产案例**: Bogleheads 社区（数十万被动投资者）默认在这三家之一开户做三基金组合 evidence: [T02-S014, T02-S016]
- **维护者背景** (sub_skill_link): Vanguard = John Bogle 创立，成本至上+市场组合+定投理念的机构载体，与 Track 01「Bogle / 被动指数派」直接关联
- **近期变化**: 持续的费率竞赛把核心宽基 ER 压到趋零；各家加码直接指数化（见新兴层）evidence: [T02-S004, T02-S008]
- **来源**:
  - [Primary] Vanguard 官网 evidence: [T02-S001]
  - [Primary] Bogleheads wiki 各券商对比 evidence: [T02-S016]
- **可信度**: high
- **Decay risk**: low（24+ 月稳定，行业基础设施；< 20% 被显著改变）

### 2. 宽基指数 ETF / 基金（核心持仓本身）

- **One-liner**: 被动派的「产品=工具」—— 一支全市场宽基指数 + 一支债券，就是 ≥80% 个人组合的核心。
- **Tier**: 必备
- **Maintainer / Owner**: 各发行商（Vanguard / iShares / 国内基金公司）
- **License**: proprietary（基金产品）
- **典型使用场景**:
  - 三基金组合：美国全市场（VTI / VTSAX）+ 国际（VXUS）+ 债券（BND / VBTLX）；或单支全球 VT 一把梭 evidence: [T02-S014, T02-S015]
  - S&P 500 代表：VOO / IVV / SPLG / SPY（注意 SPY 费率明显高于 VOO/IVV/SPLG，**以官网当前 ER 为准**）evidence: [T02-S015]
  - zh-CN：沪深300 / 中证500 / 标普500 QDII ETF + 宽基指数基金 evidence: [T02-S017]
- **数字 caveat**: 「宽基美股 ETF 费率已极低、彼此差距微小」是社区共识；具体 bps 以发行商官网披露为准，**不要编「0.03%」这类精确值**当事实 evidence: [T02-S015]
- **不适合 / 替代方案**: 主题/行业/杠杆 ETF 费率显著更高且偏离「低成本宽基」原则 → 非核心仓位慎用（见避坑）evidence: [T02-S025]
- **维护者背景** (sub_skill_link): 指数基金作为产品由 Bogle/Vanguard 推向大众，与 Track 01 被动派关联
- **可信度**: high
- **Decay risk**: low（产品形态成熟；费率只会更低不会更高）

### 3. Portfolio Visualizer（回测 / 资产配置 / 因子）

- **One-liner**: 个人投资者做「资产配置回测 + Monte Carlo + 因子归因」的事实标准网页工具，被动/趋势/配置派都用。
- **Tier**: 必备
- **Maintainer / Owner**: Portfolio Visualizer (portfoliovisualizer.com)
- **License**: proprietary，有免费层 + 付费高级层（**具体定价以官网为准**，第三方观察其核心回测免费可用）evidence: [T02-S009]
- **典型使用场景**:
  - 资产配置回测：可回溯到 1972（asset-class 级别），比较多组合的风险/收益/回撤/滚动收益 evidence: [T02-S009]
  - 因子回归：Fama-French + Carhart（市场/规模/价值/动量）对单资产或组合做归因 evidence: [T02-S009]
  - 组合优化：mean-variance / CVaR / 最大回撤 / Black-Litterman + 有效前沿 evidence: [T02-S009]
  - 战术配置：基于移动均线/动量/估值/波动率目标的择时模型（趋势跟踪派回测信号）evidence: [T02-S009]
  - Monte Carlo：退休提取率/组合存活率模拟 evidence: [T02-S009]
- **不适合 / 替代方案**: 需要日频粒度回撤/更长 sim 历史 → testfol.io（新兴层）；只想要持仓穿透/基金评级 → Morningstar X-Ray evidence: [T02-S010, T02-S007]
- **生产案例**: Bogleheads / DIY 配置社区把它当回测默认工具，反复在组合讨论中引用 evidence: [T02-S009, T02-S010]
- **近期变化**: 部分高级功能曾移到付费墙后（**以官网当前为准**），催生 testfol.io 等免费替代 evidence: [T02-S010]
- **可信度**: high
- **Decay risk**: low（DIY 回测基础设施，地位稳固；但有免费新晋挑战者，故非「极低」）

### 4. Morningstar（基金尽调 / X-Ray / 评级）

- **One-liner**: 基金/ETF 尽职调查的行业标准 —— 看费率、持仓穿透、风格箱、星级（回看）+ Medalist 评级（前瞻）。
- **Tier**: 必备
- **Maintainer / Owner**: Morningstar (morningstar.com)
- **License**: proprietary，免费层 + Premium/Investor 付费（解锁完整分析师报告、X-Ray、高级筛选；**具体月费以官网为准**）evidence: [T02-S006]
- **典型使用场景**:
  - Portfolio X-Ray：多基金/ETF 组合的持仓穿透，看资产类别/地区/风格的 overweight/underweight 与重叠 evidence: [T02-S007]
  - 星级 vs Medalist：星级**回看**（过去风险调整后表现，5 星=同类前 10%）；Medalist（Gold/Silver/Bronze/Neutral/Negative）**前瞻**，重费率影响 —— 正确用法是星级缩小范围，再看 Medalist+费率+经理任期 evidence: [T02-S006]
  - 风格箱（style box）：市值 × 价值/成长 九宫格定位基金风格 evidence: [T02-S006]
- **不适合 / 替代方案**: 深度估值/DCF/内在价值 → GuruFocus / Damodaran；A 股估值分位 → 理杏仁 evidence: [T02-S011, T02-S017]
- **生产案例**: Vanguard Digital Advisor 被 Morningstar 评为顶级 robo —— Morningstar 评级本身是行业引用基准 evidence: [T02-S006]
- **可信度**: high
- **Decay risk**: low（基金评级机构地位稳固）

### 5. 组合 / 净值追踪器（Empower 或 表格）

- **One-liner**: 跨账户聚合净值 + 费用分析器 + 资产配置体检，回答「我整体到底持有什么、付了多少费、配置是否跑偏」。
- **Tier**: 必备
- **Maintainer / Owner**: Empower（原 Personal Capital, empower.com）/ 或自建 Google Sheets / Excel
- **License**: Empower 免费追踪工具（付费为可选财富管理）；表格自建 evidence: [T02-S021]
- **典型使用场景**:
  - 净值聚合：自动同步 checking/储蓄/信用卡/贷款/投资(401k/IRA)/房贷，实时净值快照 evidence: [T02-S021]
  - 费用分析器（Fee Analyzer）：算出所有关联账户的 ER + 顾问费 + 其他成本，并投影复利侵蚀 —— 这是「揪出高费率基金」的杀手锏 evidence: [T02-S021]
  - 投资体检（Investment Checkup）：当前资产配置 vs 目标配置对比 evidence: [T02-S021]
- **数字 caveat**: Empower 付费财富管理顾问费起点（按账户规模递减）**以官网当前披露为准**，免费工具部分本身不收费 evidence: [T02-S021]
- **不适合 / 替代方案**: 重隐私/不愿绑定账户 → Google Sheets/Excel 手动模板（雪球/且慢也提供组合再平衡视图）；预算+投资一体新晋 → Monarch Money / Boldin（第三方观察其可用性更佳）evidence: [T02-S021, T02-S030]
- **可信度**: high（免费工具）/ medium（其投顾业务一面之词）
- **Decay risk**: medium（第三方观察其工具数年未大改，被 Monarch/Boldin 等追近，12-24 月格局可能变）evidence: [T02-S021]

---

## 场景特化层（详细卡片）

### 6. Interactive Brokers (IBKR)

- **One-liner**: 跨国多市场 + 广分数股 + 低保证金利率的券商，给需要美/加/欧/港/A 多市场或活跃交易的投资者。
- **Tier**: 场景特化
- **Maintainer / Owner**: Interactive Brokers (interactivebrokers.com)
- **License**: proprietary
- **典型使用场景**:
  - 多市场覆盖：可在美/加/欧等交易所买 ~11,000 只股票/ETF 的分数股；比 Schwab Stock Slices（仅 S&P 500 ~500 只、$5 起）覆盖广得多 evidence: [T02-S005]
  - 低成本活跃交易：IBKR Lite 美股 0 佣金；分层定价对期权/期货成本更低；保证金利率显著低于一般券商（**具体利率以官网为准**）evidence: [T02-S005]
- **不适合 / 替代方案**: 纯被动美股 buy-and-hold + 不碰海外 → Vanguard/Fidelity/Schwab 界面更友好够用；平台复杂度对新手偏高 evidence: [T02-S005]
- **生产案例**: 第三方对比一致把 IBKR 列为「活跃交易者 + 国际市场最佳」 evidence: [T02-S005]
- **可信度**: high（能力）/ medium（具体费率随时变，以官网为准）
- **Decay risk**: low（多市场基础设施）

### 7. GuruFocus（美股价值尽调）

- **One-liner**: 价值投资者的财报+估值数据中心 —— DCF 内在价值、F-Score/Z-Score、guru 持仓，数据底层来自 Morningstar。
- **Tier**: 场景特化
- **Maintainer / Owner**: GuruFocus (gurufocus.com)；公司基本面数据由 Morningstar 提供
- **License**: proprietary，付费为主（**定价以官网为准**）evidence: [T02-S011]
- **典型使用场景**:
  - 基本面筛选：P/E、股息率、市值 + Altman Z-Score（破产风险）+ Piotroski F-Score（财务质量）+ PEG / P/FCF evidence: [T02-S011]
  - DCF 计算器：估内在价值；Excel Add-In / Google Sheets API 取数 evidence: [T02-S011]
  - guru 跟踪：知名价值投资者持仓变动 evidence: [T02-S011]
- **不适合 / 替代方案**: 被动指数派完全用不上（不需选股）；A/港股估值 → 理杏仁；学术级估值参数 → Damodaran evidence: [T02-S017, T02-S012]
- **维护者背景** (sub_skill_link): GuruFocus 大量收录 Damodaran 估值方法论内容，与 Track 01「价值/估值派 Damodaran」关联 evidence: [T02-S011]
- **可信度**: medium（vendor 一手 + 第三方评测）
- **Decay risk**: medium

### 8. 理杏仁 lixinger（A/港股估值数据，zh-CN）

- **One-liner**: 为中小投资者打造的 A/港股估值数据中心 —— PE/PB 历史分位、指数估值、财报对比，「不推荐、不预测、只给数据」。
- **Tier**: 场景特化
- **Maintainer / Owner**: 理杏仁 (lixinger.com)，SaaS
- **License**: proprietary，免费 + 付费两档（新用户有试用；**定价以官网为准**）evidence: [T02-S017]
- **典型使用场景**:
  - 指数估值分位：用 PE/PB 历史分位 + 颜色档判断宽基指数贵/便宜（被动派定投择「位」、价值派择「点」都用）evidence: [T02-S017]
  - 个股/行业财报对比：同行业竞品财务数据并排，增长率高亮 evidence: [T02-S017]
  - 市场覆盖：A 股 + 港股完整，美股数据仍在完善 evidence: [T02-S017]
- **不适合 / 替代方案**: 只投美股 → GuruFocus/Morningstar；只做纯被动定投不看估值 → 不必付费 evidence: [T02-S011]
- **生产案例**: zh-CN 价值/指数定投社区把它当 A 股估值分位的事实数据源（注意：社区背书多见于知乎/雪球长文，**已按黑名单剔除**，此处只采信厂商官网功能描述）evidence: [T02-S017]
- **可信度**: medium（vendor 一手，社区背书源黑名单剔除后证据偏薄）
- **Decay risk**: medium

### 9. Damodaran online data (NYU Stern)

- **One-liner**: 「估值院长」Damodaran 免费公开的估值数据集 —— 股权风险溢价、行业 beta、WACC、各行业 multiples，DCF 假设的权威锚。
- **Tier**: 场景特化
- **Maintainer / Owner**: Aswath Damodaran, NYU Stern (pages.stern.nyu.edu/~adamodar)
- **License**: 免费公开（.edu 学术）evidence: [T02-S012]
- **典型使用场景**:
  - DCF 输入参数：取行业 ERP、unlevered/levered beta、cost of capital 作为估值假设的市场基准 evidence: [T02-S012]
  - multiples 对标：按行业/地区查 PE/EV-EBITDA 等倍数中位 evidence: [T02-S012]
- **Maturity signals**: 数据每年初前两周更新一次（最近一次 2026-01-09），部分数据集更频繁 (last checked: 2026-06-04) evidence: [T02-S012]
- **不适合 / 替代方案**: 要单只公司即取即用的成品估值 → GuruFocus（Damodaran 现已不提供公司级数据下载）；不做估值的被动派用不上 evidence: [T02-S012, T02-S011]
- **维护者背景** (sub_skill_link): Damodaran 本人是 Track 01「估值/价值派」核心 figure，此数据集是其公开输出
- **可信度**: high（学术一手）
- **Decay risk**: low（年度更新机制稳定运行多年）

### 10. TradingView（技术/趋势派主力图表）

- **One-liner**: 技术派的图表+形态+指标+脚本回测一体平台，覆盖股/ETF/外汇/期货/加密，3000 万+用户。
- **Tier**: 场景特化
- **Maintainer / Owner**: TradingView (tradingview.com)，2011 创立
- **License**: proprietary，免费层 + Plus/Premium 付费（**定价以官网为准**，第三方观察 Plus 档约为多数活跃零售的甜点）evidence: [T02-S018, T02-S034]
- **典型使用场景**:
  - 图表/形态/指标：400+ 内置指标 + 20 万+社区脚本，一键加载 evidence: [T02-S018]
  - Pine Script v6 策略回测：内置 Strategy Tester，支持复杂策略 + 组合级计算 + 表盘，无需外部 IDE evidence: [T02-S019]
  - 多触发警报：价格/指标/画线/自定义 Pine 条件，推送/邮件/SMS/webhook —— 趋势跟踪派的信号触发 evidence: [T02-S018]
- **不适合 / 替代方案**: 纯被动 buy-and-hold 完全不需要（择时 ≠ 被动）；点数图/Kagi/市场宽度深度 → StockCharts evidence: [T02-S020]
- **生产案例**: 零售技术分析社区事实标准（多家独立横评把 TradingView 列为综合图表第一）evidence: [T02-S018, T02-S020]
- **可信度**: high
- **Decay risk**: low（技术派图表基础设施）

### 11. StockCharts（专业图表深度）

- **One-liner**: 老牌专业图表工具，点数图/Kagi/市场宽度（market breadth）是其拿手，教育内容由数十年市场老兵撰写。
- **Tier**: 场景特化
- **Maintainer / Owner**: StockCharts (stockcharts.com)
- **License**: proprietary，付费会员（**定价以官网为准**）evidence: [T02-S020]
- **典型使用场景**:
  - 点数图/Kagi 形态扫描：付费会员可扫蜡烛 + 点数图形态 evidence: [T02-S020]
  - 市场宽度研究：breadth 指标判断大盘内部强弱（趋势派宏观择时）evidence: [T02-S020]
- **不适合 / 替代方案**: 要多资产 + 脚本生态 + 社区 + 更现代 UI → TradingView（横评在大多数维度胜出）evidence: [T02-S020]
- **可信度**: medium
- **Decay risk**: medium（TradingView 蚕食其综合场景，专业细分仍有位置）

### 12. FRED（宏观数据）

- **One-liner**: 圣路易斯联储免费宏观数据库，84 万+时间序列（利率/CPI/就业/货币供应），趋势/择时/资产配置的宏观背景层。
- **Tier**: 场景特化
- **Maintainer / Owner**: Federal Reserve Bank of St. Louis (fred.stlouisfed.org)
- **License**: 免费官方 evidence: [T02-S013]
- **典型使用场景**:
  - 宏观背景：利率/CPI/就业/货币供应 + 全量修订历史，自定义单位/频率/叠加 evidence: [T02-S013]
  - Excel Add-In：84 万+序列直接拉进 Excel（BEA/BLS/Census/OECD 源）evidence: [T02-S013]
- **不适合 / 替代方案**: 微观个股/基金数据 → Morningstar/GuruFocus；纯被动派一般只需偶尔看（不做宏观择时）evidence: [T02-S006]
- **可信度**: high（联储一手）
- **Decay risk**: low（官方公共基础设施）

### 13. ETF 筛选器（etf.com / ETFdb）

- **One-liner**: 按费率/规模/持仓/收益筛选与对比 ETF 的免费工具，选品环节用。
- **Tier**: 场景特化
- **Maintainer / Owner**: etf.com / ETF Database (etfdb.com)
- **License**: proprietary，有免费筛选 evidence: [T02-S024, T02-S025]
- **典型使用场景**:
  - etf.com 筛选器：4000+ ETF 搜索/筛选/对比，免费且无需开户 evidence: [T02-S025]
  - ETFdb：2000+ ETF 按股息率/费率/投资目标等数十维度筛 evidence: [T02-S024]
- **数字 caveat**: 「核心宽基 ER 趋零、差异主要在主题/行业 ETF」是横评观察（第三方）；具体某 ETF 费率以发行商官网为准 evidence: [T02-S025]
- **不适合 / 替代方案**: 持仓穿透/重叠 → Morningstar X-Ray；A 股场内/场外基金 → 蛋卷/天天基金 evidence: [T02-S007, T02-S031]
- **可信度**: medium
- **Decay risk**: medium

### 14. 税优账户类型（工具 = 账户结构）

- **One-liner**: 「账户类型就是工具」—— 选对税优容器（401k/IRA/Roth/HSA；CN 个人养老金 Y）对税后长期收益的杠杆，常大于选基金。
- **Tier**: 场景特化（但对有资格者近乎必备）
- **Maintainer / Owner**: US: IRS（规则）/ 各券商（载体）；CN: 证监会+各基金公司
- **License**: 监管规则（一手 = gov）
- **典型使用场景 / 2026 关键数字（官方源，有具体日期）**:
  - **US 2026 限额**（IRS Notice 2025-67, evidence: [T02-S027]）：401(k)/403(b)/457(b) 员工 $24,500，50+ catch-up $8,000，60–63 增强 catch-up $11,250；传统/Roth IRA $7,500，50+ catch-up $1,100；HSA 自己 $4,400 / 家庭 $8,750，55+ catch-up $1,000 evidence: [T02-S026, T02-S027]
  - **2026 新规**：有 Roth 选项计划、上一年在该雇主工资 > $150,000 者的 catch-up 必须以 Roth 形式缴 evidence: [T02-S033]
  - **Roth IRA 收入 phase-out 2026**：单身 $153,000–$168,000；已婚合并 $242,000–$252,000 evidence: [T02-S026]
  - 通用顺序原则：先拿满 401k 雇主匹配 → HSA（三重免税）→ IRA/Roth → taxable brokerage；taxable 账户做 tax-loss harvesting evidence: [T02-S027]
  - **CN 个人养老金 Y 份额**：须开通个人养老金账户才能申购 Y 份额；分养老目标基金 + 指数型基金两类；证监会发布官方《个人养老金基金名录》（截至 2026-03-31）evidence: [T02-S028]
  - CN 缴费/税优：每人每年缴费上限及对应税优**以当年财税/人社部门口径为准**（本调研未取到税务部门一手公告，标 caveat 不编具体减税额）evidence: [T02-S028]
- **不适合 / 替代方案**: 短期要用的钱别锁进退休账户（流动性/罚金）；超额缴费有罚则 —— 限额以 IRS/监管当年公告为准 evidence: [T02-S027]
- **可信度**: high（US，IRS 一手）/ medium-high（CN，证监会名录一手，但税额口径需补人社/财税源）
- **Decay risk**: medium（限额每年微调，规则结构稳定 —— master skill 每年初需刷新数字）

### 15. Robo-advisor / 自动定投（Betterment / Wealthfront；CN 帮你投 / 且慢）

- **One-liner**: 算法自动配置 + 再平衡 + 税损收割的托管层，给「不想自己动手 + 资产够触发 TLH」的人。
- **Tier**: 场景特化
- **Maintainer / Owner**: Betterment (betterment.com) / Wealthfront (wealthfront.com)；CN: 蚂蚁「帮你投」(× Vanguard) / 且慢「长盈计划」(盈米)
- **License**: proprietary
- **典型使用场景 / 数字 caveat**:
  - 费率：Betterment / Wealthfront 数字层均年化 0.25% 顾问费（**叠加在基金 ER 之上**，双重收费要算清，见避坑）；Betterment Premium 0.65% + $100k 起含真人 CFP evidence: [T02-S022, T02-S023]
  - 门槛：Betterment $0 起；Wealthfront $500 起 evidence: [T02-S022, T02-S023]
  - TLH / 直接指数化：两家应税账户都日频 TLH；Wealthfront 在 $100k+ 提供直接指数化（持成分股而非 ETF），其自家数据宣称直接指数化额外 +1.8% 税后年化、标准 TLH +0.77%（**厂商一面之词，标 vendor claim**）evidence: [T02-S023]
  - **CN 帮你投**：蚂蚁 × Vanguard 全权委托（「全委托免打理」），收 0.5% 年化投顾费，调仓不需用户逐次确认 evidence: [T02-S030]
  - **CN 且慢长盈计划**：非全权委托，要求用户参与度更高，不能当甩手掌柜 evidence: [T02-S030]
- **不适合 / 替代方案**: 资产小 / 税收敏感度低 → 顾问费不值，直接自持宽基 ETF 更省；想要直接指数化但已有大 taxable → Fidelity FidFolios（$5k，见新兴层）evidence: [T02-S022, T02-S004]
- **维护者背景** (sub_skill_link): 帮你投背后是 Vanguard → 与 Track 01 Bogle/被动派关联
- **可信度**: medium（费率/门槛第三方一致，TLH 增益为 vendor claim）
- **Decay risk**: medium（robo 行业正在洗牌 —— 见新兴/避坑）

---

## 新兴 / 实验层（近 12 月，stability: experimental）

### 16. 直接指数化（Direct Indexing）下沉零售

- **One-liner**: 不买宽基 ETF 而是直接持有指数成分股，从而逐股做税损收割 + ESG/个股定制 —— 曾是超高净值专属，2022 起 Fidelity/Schwab 把门槛打到零售级。
- **Tier**: 新兴
- **Maintainer / Owner**: Fidelity (FidFolios) / Charles Schwab (Personalized Indexing) / Vanguard（advisor 端）
- **License**: proprietary
- **Stability**: emerging（产品在快速演化、门槛/费率仍在下探）
- **典型使用场景 / 数字（官方+独立源）**:
  - 规模：直接指数化资产 2022 年底约 $462B，预计 2026 年底超 $800B（Morningstar 独立分析）evidence: [T02-S008]
  - **Fidelity FidFolios**：$5,000 起（市场最低门槛之一），日频 TLH + 分数复制 evidence: [T02-S008]
  - **Schwab Personalized Indexing**：$100,000 起，4 个起始策略可定制，TLH 由其代管；费率随规模递减（**具体费率以官网为准**）evidence: [T02-S004]
  - **Vanguard**：零售端门槛仍高（advisor 渠道为主），尚未对小额零售开放（Morningstar 预期未来民主化）evidence: [T02-S008]
  - 费率区间：美国大盘指数直接指数化多在 0.20%–0.40% 起、随规模降（Morningstar 观察）evidence: [T02-S008]
- **不适合 / 替代方案**: taxable 账户小 / 不在乎逐股 TLH / 怕复杂 → 一支宽基 ETF 仍然更简单更便宜（避坑：别为 TLH 边际收益买复杂度）evidence: [T02-S008]
- **可信度**: high（Fidelity/Schwab 一手 + Morningstar 独立）
- **Decay risk**: high（门槛/费率/参与者 12 月内大概率继续显著变 —— 新兴层默认 high）

### 17. testfol.io（社区新宠回测器）

- **One-liner**: solo 开发者维护的免费回测器，日频数据 + sim 基金延长历史（如 BNDSIM 把 BND 数据延到 1986），Reddit/Bogleheads 上正取代 Portfolio Visualizer 部分场景。
- **Tier**: 新兴
- **Maintainer / Owner**: testfol.io（个人开发者）
- **License**: 免费（核心）evidence: [T02-S010]
- **Stability**: experimental（单人维护，"6 个月后可能形态大变"）
- **典型使用场景**:
  - 日频回测：drawdown/波动率粒度比 PV 的月频更细 evidence: [T02-S010]
  - sim 基金：用模拟序列把 ETF 数据延到 inception 之前，做更长周期策略测试 evidence: [T02-S010]
  - 再平衡规则 + 定投/提取建模 + 滚动收益/相关性/提取结果 evidence: [T02-S010]
- **不适合 / 替代方案**: 要因子回归(Fama-French)/Black-Litterman 优化 → Portfolio Visualizer 仍更全；退休 Monte Carlo → PV 或 PortfolioMetrics evidence: [T02-S009, T02-S010]
- **生产案例**: Bogleheads 论坛专门讨论各回测器（PV/Testfol/ValueInvesting/PortfolioMetrics）数据准确性，testfol.io 被点名为「社区最爱、免费、活跃开发」evidence: [T02-S010]
- **可信度**: medium（社区采用明确，但单人维护风险）
- **Decay risk**: high（单人项目 + 新兴）

### 18. AI 投顾 / 人机混合（robo 2.0）

- **One-liner**: LLM 驱动的新一代投顾，能处理远多于「20 个 ETF 篮子问卷」的场景（如重仓股票期权、为购房规划组合）；同时传统纯数字 robo 在 2026 经历洗牌。
- **Tier**: 新兴
- **Maintainer / Owner**: Robinhood (Strategies) / Vanguard (Digital Advisor) / 各家 AI 工具
- **License**: proprietary
- **Stability**: experimental（监管/可信度/产品形态都在动）
- **典型使用场景 / 信号**:
  - LLM 投顾 vs 旧 robo：旧 robo 靠问卷塞进 ~20 个 ETF 篮子；新一代能 account for 期权集中、购房计划等复杂场景（Fortune 行业观察）evidence: [T02-S032]
  - **Robinhood Strategies**：AI 工具 + 真人顾问引导，25 万付费用户、人均约 $250/年（人机混合范式）evidence: [T02-S032]
  - **Vanguard Digital Advisor**：被 Morningstar 评为顶级 robo（$100 起、低费、优质组合构建）evidence: [T02-S006]
  - **行业洗牌信号（重要）**：Schwab 2026 Q1 关停其混合 robo「Intelligent Portfolios Premium」（曾 $300 一次性 + $30/月），保留无顾问费的基础版（$5,000 起）；JPMorgan/US Bank/UBS 的 robo 也相继关停 —— 评论员 Josh Brown 称「the robo-advice era is over」evidence: [T02-S032, T02-S035, T02-S003]
- **不适合 / 替代方案**: 别把 LLM 聊天输出当投资建议执行（幻觉/无 fiduciary）；纯被动长持仍是「一支宽基 + 定投」最稳 evidence: [T02-S032]
- **可信度**: medium（行业趋势明确，单个 AI 工具效果未经长测）
- **Decay risk**: high（AI 投顾 12 月内必然剧变）

---

## 选型决策树

> 节点 8 个。每个分支可从上面卡片追溯证据。**非投资建议**，是工具选型逻辑。

### 决策树 A：你的核心投资取向是什么？

#### Branch 1：被动指数 / buy-and-hold（≥80% 个人的最优默认）
→ 推荐执行层：低费率券商三选一（Vanguard 选择最广 / Fidelity 全能 zero-ER / Schwab 新手友好）+ 一支宽基指数 ETF（VTI/VT/VOO + BND；CN 沪深300/标普500 QDII）evidence: [T02-S001, T02-S014, T02-S016]
→ 推荐分析层：Portfolio Visualizer（配置回测）+ Morningstar（基金尽调/X-Ray）evidence: [T02-S009, T02-S007]
→ **不推荐**：TradingView / StockCharts / GuruFocus（择时与选股工具，被动派用不上，徒增复杂度）evidence: [T02-S018, T02-S011]
→ 真实案例：Bogleheads 社区数十万人的默认栈正是「三家券商之一 + 三基金组合 + PV/Morningstar」evidence: [T02-S014, T02-S016]

#### Branch 2：主动价值选股
##### Branch 2a：美股
→ 推荐：GuruFocus（DCF/F-Score/Z-Score）+ Damodaran data（ERP/beta/WACC 锚）+ Morningstar（基本面+Medalist）evidence: [T02-S011, T02-S012, T02-S006]
##### Branch 2b：A 股 / 港股
→ 推荐：理杏仁 lixinger（PE/PB 历史分位 + 财报对比）evidence: [T02-S017]
→ 替代：天天基金/蛋卷看场外基金；估值分位也可用韭圈儿（**zh-CN 社区背书源黑名单剔除，工具能力以厂商官网为准**）evidence: [T02-S017, T02-S031]

#### Branch 3：技术 / 趋势跟踪（择时派）
→ 推荐：TradingView（图表+指标+Pine 回测+警报，综合第一）evidence: [T02-S018, T02-S019]
→ 替代：StockCharts（点数图/Kagi/市场宽度深度，但生态/UI 不如 TV）evidence: [T02-S020]
→ 趋势宏观背景：FRED（利率/宏观序列）；趋势信号回测也可用 Portfolio Visualizer 战术配置模块（移动均线/动量）evidence: [T02-S013, T02-S009]
→ **警告**：技术回测极易过拟合，见避坑 evidence: [T02-S009]

### 决策树 B：你想自己动手到什么程度？

#### Branch 4：完全托管（懒人）
→ 资产小 / 想最省：直接自持宽基 ETF + 设自动定投（券商内置），**不要**叠加 robo 顾问费 evidence: [T02-S022]
→ 愿付 ~0.25% 换自动化 + 想要 TLH：Betterment（$0 起、目标导向、可选真人 CFP）/ Wealthfront（$500 起、TLH 强、$100k+ 直接指数化）evidence: [T02-S022, T02-S023]
→ CN：蚂蚁「帮你投」(× Vanguard，全权委托 0.5%) / 且慢「长盈计划」(半委托、要参与) evidence: [T02-S030]
→ **风险提示**：robo 行业 2026 洗牌（Schwab/JPM/UBS 关停高端 robo），选龙头+基础档 evidence: [T02-S032]

#### Branch 5：半自动（自己配置 + 工具追踪）
→ 追踪/费用体检：Empower（免费聚合 + Fee Analyzer）或自建 Google Sheets evidence: [T02-S021]
→ 再平衡：表格阈值法 / Empower / 雪球·且慢组合视图 evidence: [T02-S021, T02-S030]

### 决策树 C：账户结构（先于选具体产品！）
#### Branch 6：美国纳税人
→ 顺序：401(k) 拿满雇主匹配 → HSA（三重免税）→ IRA/Roth → taxable brokerage（taxable 才做 TLH/直接指数化）evidence: [T02-S027]
→ 2026 高收入注意：工资 > $150k 的 catch-up 强制 Roth 形式 evidence: [T02-S033]
#### Branch 7：中国大陆投资者
→ 税优容器：开个人养老金账户 → 申购 Y 份额（养老目标 FOF 或指数型，证监会名录内）evidence: [T02-S028]
→ 跨境美/港股：开户门槛 2026 收紧（部分中资券商对内地客户停止/限制开户，**以券商当前政策为准**，本调研未取到券商官方公告，标 caveat）；可考虑 IBKR 等多市场券商 evidence: [T02-S005]

### 决策树 D：要不要上直接指数化？（新兴，节点 8）
#### Branch 8：有较大 taxable 账户 + 想逐股 TLH/定制
→ 门槛最低：Fidelity FidFolios（$5,000）；$100k+ 可看 Schwab Personalized Indexing / Wealthfront evidence: [T02-S004, T02-S008, T02-S023]
→ **否则**：taxable 小或图省事 → 一支宽基 ETF 仍最优，别为边际 TLH 收益买复杂度 evidence: [T02-S008]

---

## 避坑清单（≥5）

- ❌ **不要被高费率主动基金 / 申购费坑**：Empower 的 Fee Analyzer 反复揭示费用复利侵蚀；同类指基费率已趋零，长期 1%+ 的费差吃掉巨量复利。用 Morningstar 看 ER + Medalist（重费率），别只看星级（星级是回看的过去表现，未必重复）evidence: [T02-S021, T02-S006]
- ❌ **不要用复杂工具替代「低成本宽基 + 定投」**：被动派上 TradingView/GuruFocus/直接指数化只是徒增复杂度与出错面；≥80% 个人的最优解就是一支宽基 + 自动定投 + 偶尔再平衡 evidence: [T02-S014, T02-S008]
- ❌ **不要迷信回测 / 技术信号过拟合**：Portfolio Visualizer/testfol.io 的战术配置和 Pine 策略回测极易在历史上调参到漂亮曲线，样本外失效；回测是理解工具不是预测工具。Bogleheads 专门讨论各回测器数据口径差异（同一组合不同工具结果不同）evidence: [T02-S009, T02-S010]
- ❌ **不要让 robo 顾问费叠加基金 ER 双重收费而不自知**：Betterment/Wealthfront 的 ~0.25% 顾问费是**加在**底层 ETF 费率之上的；资产小或税收不敏感时，直接自持宽基更省。robo 的 TLH 增益（如「+0.77%」「+1.8%」）是 vendor 自家口径，别当保证 evidence: [T02-S022, T02-S023]
- ❌ **不要把 LLM/AI 投顾输出当投资建议直接执行**：新一代 AI 投顾能力提升但有幻觉、无 fiduciary 义务；且 robo 行业 2026 正洗牌（Schwab/JPM/UBS 关停高端 robo），别把钱压在可能停运的产品上 evidence: [T02-S032]
- ❌ **A 股/港股不要频繁交易吃摩擦成本**：佣金+平台费+印花税长期累积侵蚀收益（雪球用户长帖常吐槽佣金，**该源黑名单剔除**，但摩擦成本逻辑成立）；跨境券商对内地客户开户 2026 收紧，开户前先确认资格 evidence: [T02-S005]
- ❌ **不要把税优账户当短期资金池**：401k/IRA/个人养老金有流动性锁定/提前取出罚金；短期要用的钱放 taxable/活期。US 超额缴费有罚则，限额每年微调以 IRS 当年公告为准 evidence: [T02-S027]
- ❌ **不要为直接指数化的边际收益买不必要的复杂度**：直接指数化（持几百只成分股）TLH 收益在大 taxable 账户才显著；小账户/图省事用一支宽基 ETF 更优，门槛费率仍在变（新兴，high decay）evidence: [T02-S008]

---

## Phase 2 提炼提示

**反复出现 ≥3 source 都强调的「工具选型原则」**（候选 playbook 规则）:
- **成本至上**：低费率券商 + 趋零 ER 宽基 + 警惕顾问费叠加，是贯穿券商/基金/robo/Empower 费用分析的第一原则（出现于: T02-S001/S015/S016/S021/S022）
- **账户结构先于产品选择**：选对税优容器（401k/IRA/Roth/HSA；个人养老金 Y）的杠杆常大于选基金（出现于: T02-S026/S027/S028/S033）
- **工具按流派分叉，不存在通用栈**：被动派只需「券商+宽基+PV+Morningstar」，价值/技术/趋势各有专用层；给被动派塞选股/择时工具是反模式（出现于: T02-S014/S011/S018）
- **回测是理解工具不是预测工具**：过拟合警告跨 PV/testfol.io/Pine 反复出现（出现于: T02-S009/S010/S019）

**显著的工具流派分裂**（候选 智识谱系条目，直接喂 Phase 2.1 心智模型）:
- **被动指数派（成本至上 / time in market）**：券商三家 + 宽基 ETF + Portfolio Visualizer + Morningstar + Empower；代表人物 Bogle（→ Vanguard，含蚂蚁帮你投）。核心信条：选对配置与容器、压低成本、别择时。
- **价值派（基本面 / 内在价值 / 安全边际）**：GuruFocus + Damodaran data + 理杏仁 + Morningstar；代表人物 Graham/Buffett·Munger/Damodaran（→ GuruFocus 收录其方法论）。核心信条：价格 ≠ 价值，估值数据找折价。
- **技术/趋势派（价格已反映信息 / 动量择时）**：TradingView + StockCharts + FRED + PV 战术模块；核心信条：跟趋势、信号驱动。
- 三派对「主动 vs 被动、基本面 vs 技术面、择时 vs 持有」的分歧直接对应工具分叉 —— 这是本行业最有价值的智识谱系，工具栈是其物化。

**新兴工具信号**:
- 当前活跃 / 上升的新工具数: 3（直接指数化下沉、testfol.io、AI/人机投顾）
- 反向信号：传统纯数字 robo 高端档**在收缩**（Schwab/JPM/UBS/US Bank 关停），"robo-advice era is over" 论调（Josh Brown）—— 不是工具增多而是 robo 范式向「基础档免费 + AI/人机混合高端」两极分化
- 出现 → 主流 速度估计: 直接指数化已从超高净值（>10 年专属）下沉到 $5k 零售约用 3–4 年（2022→2026）；AI 投顾 12–18 个月内形态会再变

**给 Track 01（figures）的工具开发者反馈**（候选 figures / 已关联）:
- **John Bogle → Vanguard**（券商 + 宽基指数基金 + 蚂蚁帮你投合作方），被动派物化载体
- **Aswath Damodaran → NYU online data + GuruFocus 方法论收录**，估值派
- Graham / Buffett·Munger（价值派思想）→ 物化于 GuruFocus / 理杏仁的估值筛选逻辑（工具实现其「安全边际」）
- 这些已大概率在 Track 01 retained 列表内；若未，提交 Track 01 重新 walk。

**冷僻 / 信号薄弱**:
- 必备层 5 个（≥3 ✅）；场景特化 10 个（≥5 ✅）；新兴 3 个（≥2 ✅）—— 数量门槛全部通过
- **诚实边界（须进 Phase 2.8）**：
  1. **zh-CN 工具证据偏薄**：理杏仁/且慢/蛋卷/韭圈儿的社区背书几乎全在知乎/雪球/新浪（黑名单），已剔除后仅剩厂商官网一手 + 证监会名录，zh-CN 工具的「采用率/优劣」claim 可信度低于英文工具（英文有 Bogleheads wiki + 独立横评 + 厂商官网三重交叉）。
  2. **券商/robo/工具厂商官网被 verifier 判 secondary**（非 primary 白名单），本文按「vendor docs = vendor 一手」处理并明确标注，但 mental model 级 claim 已尽量靠 ≥2 source（如券商对比靠 Bogleheads wiki，直接指数化靠 Morningstar 独立分析），未仅凭厂商一面之词。
  3. **具体数字策略**：美股费率/佣金一律标「以官网当前披露为准」未编精确 bps；US 退休限额用 IRS Notice 2025-67 一手实数；CN 个人养老金税额口径未取到人社/财税一手，标 caveat 未编。
  4. **跨境券商开户限制**：「部分中资券商对内地客户停止开户」信号强但本调研未取到券商官方公告（搜索命中多为黑名单源），标 caveat、决策树 Branch 7 仅作提示。

---

## 质量自检

- [x] 候选数 ≥ 20：探索 ~28 个候选（券商×3、宽基产品、PV、Morningstar、Empower、IBKR、GuruFocus、理杏仁、Damodaran、TradingView、StockCharts、FRED、ETF 筛选×2、税优账户、Betterment、Wealthfront、帮你投、且慢、蛋卷、天天基金、直接指数化×3 家、testfol.io、AI/robo 洗牌、Vanguard Digital Advisor、Robinhood Strategies…），retained 18 张卡片
- [x] 三层都有：必备 5 / 场景特化 10 / 新兴 3
- [x] 每工具有 last_checked（manifest 2026-06-04）+ maturity signal（Damodaran 2026-01-09 更新、testfol.io BNDSIM→1986、Schwab robo 2026 Q1 关停等带具体日期）
- [x] 选型决策树 8 节点（A 取向×3 + B 动手程度×2 + C 账户结构×2 + D 直接指数化×1），每节点挂 evidence
- [x] 避坑清单 8 条（≥5）
- [x] 一手来源 ≥ 50%：35 source 中 verified_primary 15（含 IRS/CSRC/FRED/Bogleheads/Morningstar/Damodaran/Vanguard/Fidelity/Schwab 官方），其余为 vendor 一手（secondary）；无任何 blacklisted
- [x] Decay risk 每卡都标
- [x] Phase 2 接口已填（选型原则 / 流派分裂 / 新兴信号 / Track 01 反馈 / 诚实边界）
