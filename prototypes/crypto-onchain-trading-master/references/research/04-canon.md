# Track 04 — Canon（知识正典）｜加密 / 链上交易 (Crypto & On-chain Trading)

> locale=global（en-primary canon，有强 zh-CN 实践社群）。本文件是 Phase 1 wave 1 的 canon 调研产出。
>
> **诚实分类前提**：加密交易的 canon **偏少且年轻**，必须三分：
> 1. **通用交易/风控/心理经典**（被加密交易者反复借用的旧 canon）
> 2. **加密原生正典**（whitepaper / 原生书 / 奠基长文研报）
> 3. **链上分析方法正典**（指标方法论 + 平台官方文档 + SQL 教学）
>
> 方法论大量散见 podcast / Substack / Twitter 长 thread（→ Track 05），本文件只收「奠基性长文/研报」级别的 canon。

---

## Source Manifest

| source_id | url | bucket | last_checked | author/host | one-line note |
|-----------|-----|--------|--------------|-------------|---------------|
| T04-S001 | https://bitcoin.org/bitcoin.pdf | verified_primary | 2026-06-20 | Satoshi Nakamoto | 比特币原始 whitepaper（作者原文 PDF，bitcoin.org 官方托管） |
| T04-S002 | https://ethereum.org/en/whitepaper/ | verified_primary | 2026-06-20 | Vitalik Buterin | Ethereum whitepaper 官方托管 |
| T04-S003 | https://vitalik.eth.limo/ | verified_primary | 2026-06-20 | Vitalik Buterin | 作者本人博客（一手原文索引） |
| T04-S004 | https://vitalik.eth.limo/general/2021/12/06/endgame.html | verified_primary | 2026-06-20 | Vitalik Buterin | "Endgame" — rollup-centric 扩容路线奠基长文 |
| T04-S005 | https://www.sevenstories.com/books/4443-proof-of-stake | secondary | 2026-06-20 | Seven Stories Press | Vitalik 文集《Proof of Stake》出版社页（2022） |
| T04-S006 | https://en.wikipedia.org/wiki/The_Bitcoin_Standard | secondary | 2026-06-20 | — | The Bitcoin Standard 词条 + 批评汇总 |
| T04-S007 | https://davidgerard.co.uk/blockchain/2018/04/07/saifedean-ammous-the-bitcoin-standard-the-austrian-case-for-bitcoin/ | secondary | 2026-06-20 | David Gerard | 对 Bitcoin Standard 奥地利学派框架的批评性书评 |
| T04-S008 | https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3711777 | verified_primary | 2026-06-20 | Campbell Harvey 等 | DeFi & Future of Finance 免费 SSRN 草稿（书的前身） |
| T04-S009 | https://www.lynalden.com/ | verified_primary | 2026-06-20 | Lyn Alden | 作者本人站（宏观+货币长文一手源） |
| T04-S010 | https://www.lynalden.com/broken-money/ | verified_primary | 2026-06-20 | Lyn Alden | 《Broken Money》(2023) 官方书页 |
| T04-S011 | https://a16zcrypto.com/readwriteown/ | verified_primary | 2026-06-20 | a16z crypto | Chris Dixon《Read Write Own》(2024) 官方页 |
| T04-S012 | https://a16zcrypto.com/ | verified_primary | 2026-06-20 | a16z crypto | a16z crypto 研报/State of Crypto 出口 |
| T04-S013 | https://www.usv.com/writing/2016/08/fat-protocols/ | verified_primary | 2026-06-20 | Joel Monegro / USV | "Fat Protocols" 奠基论题原文（2016） |
| T04-S014 | https://messyproblems.substack.com/p/cracks-in-the-fat-protocol-theory | verified_primary | 2026-06-20 | messyproblems | 推翻 fat protocol 论题的反方长文 |
| T04-S015 | https://messari.io/ | verified_primary | 2026-06-20 | Messari | Crypto Theses 年度研报出口 |
| T04-S016 | https://www.delphidigital.io/ | verified_primary | 2026-06-20 | Delphi Digital | 深度研报机构出口 |
| T04-S017 | https://docs.glassnode.com/ | verified_primary | 2026-06-20 | Glassnode | 链上指标官方方法论 docs（academy.* 已 301 至此） |
| T04-S018 | https://research.glassnode.com/ | verified_primary | 2026-06-20 | Glassnode | 研究长文（insights.* 已 301 至此） |
| T04-S019 | https://docs.glassnode.com/guides-and-tutorials/metric-guides/realized-capitalization | verified_primary | 2026-06-20 | Glassnode | Realized Cap 官方指标定义 |
| T04-S020 | https://docs.cryptoquant.com/ | verified_primary | 2026-06-20 | CryptoQuant | 交易所流/矿工指标官方文档 |
| T04-S021 | https://docs.nansen.ai/ | verified_primary | 2026-06-20 | Nansen | Smart Money / 钱包标签方法论官方文档 |
| T04-S022 | https://docs.dune.com/ | verified_primary | 2026-06-20 | Dune Analytics | SQL / Spellbook 官方文档 |
| T04-S023 | https://docs.dune.com/learning-resources | verified_primary | 2026-06-20 | Dune Analytics | Web3 数据学习资源 reading list |
| T04-S024 | https://www.coinmetrics.io/ | secondary | 2026-06-20 | Coin Metrics | State of the Network + 网络数据方法论 |
| T04-S025 | https://charts.woobull.com/bitcoin-nvt-ratio/ | verified_primary | 2026-06-20 | Willy Woo | NVT 比率原始图表/方法论（作者本人站） |
| T04-S026 | https://medium.com/cryptolab/https-medium-com-kalichkin-rethinking-nvt-ratio-2cf810df0ab0 | secondary | 2026-06-20 | Dmitry Kalichkin | NVT Signal 改进版（作者原文 Medium） |
| T04-S027 | https://traderlion.com/trading-books/trade-your-way-to-financial-freedom/ | secondary | 2026-06-20 | TraderLion | Van Tharp 书 + R-multiple 教学评述 |
| T04-S028 | https://traderlion.com/risk-management/r-and-r-multiples/ | secondary | 2026-06-20 | TraderLion | R-multiple 概念教学 |
| T04-S029 | https://www.daytrading.com/alchemy-of-finance-soros | secondary | 2026-06-20 | DayTrading.com | Soros《Alchemy of Finance》反身性教学 |
| T04-S030 | https://medium.com/sesterce/the-reflexivity-of-crypto-markets-3457d1eac2d0 | secondary | 2026-06-20 | Sesterce | 反身性在加密市场的应用长文 |
| T04-S031 | https://www.amazon.com/Cryptoassets-Innovative-Investors-Bitcoin-Beyond/dp/1260026671 | secondary | 2026-06-20 | McGraw-Hill | Cryptoassets (Burniske & Tatar 2017) 书目 |
| T04-S032 | https://medium.com/@cburniske/theory-follows-price-follows-theory-304ef97d1b71 | secondary | 2026-06-20 | Chris Burniske | INET 代币估值模型作者原文 |
| T04-S033 | https://www.coindesk.com/layer2/2022/11/03/vitalik-buterins-proof-of-stake-the-coindesk-megareview | secondary | 2026-06-20 | CoinDesk | Vitalik《Proof of Stake》文集书评 |
| T04-S034 | https://read.cryptodatabytes.com/p/advanced-wizard-guide-to-dune-sql | secondary | 2026-06-20 | Andrew Hong | Dune SQL 进阶教学（canonical 教育者原文） |
| T04-S035 | https://docs.glassnode.com/guides-and-tutorials/metric-guides/unrealized-profit-loss/nupl-net-unrealized-profit-loss | verified_primary | 2026-06-20 | Glassnode | NUPL 官方定义（引 Adamant "Primer on Investor Sentiment"） |
| T04-S036 | https://bitcoinmagazine.com/markets/what-is-the-bitcoin-puell-multiple-indicator-and-how-does-it-work | secondary | 2026-06-20 | Bitcoin Magazine | Puell Multiple（David Puell 2019）方法论说明 |
| T04-S037 | https://thecryptosyllabus.com/ | secondary | 2026-06-20 | The Crypto Syllabus | 批判性/学术向 crypto 阅读清单 |
| T04-S038 | https://arxiv.org/abs/1906.05511 | verified_primary | 2026-06-20 | arXiv | SoK: 区块链/DeFi 学术综述类（占位审视用） |
| T04-S039 | https://woobull.com/introducing-nvt-ratio-bitcoins-pe-ratio-use-it-to-detect-bubbles/ | verified_primary | 2026-06-20 | Willy Woo | NVT 原始介绍文（作者本人站，2017） |
| T04-S040 | https://medium.com/@kenoshaking/bitcoin-market-value-to-realized-value-mvrv-ratio-3ebc914dbaee | secondary | 2026-06-20 | Murad Mahmudov & David Puell | MVRV 原始文（作者 Medium, 2018） |
| T04-S041 | https://medium.com/unconfiscatable/introducing-sopr-spent-outputs-to-predict-bitcoin-lows-and-tops-ceb4536b3b9 | secondary | 2026-06-20 | Renato Shirakashi | SOPR 原始介绍文（作者 Medium, 2019） |
| T04-S042 | https://medium.com/glassnode-insights/dissecting-bitcoins-unrealised-on-chain-profit-loss-73e735020c8d | secondary | 2026-06-20 | Rafael Schultze-Kraft | NUPL 命名/形式化原文（引 Adamant 2019） |
| T04-S043 | https://docs.glassnode.com/further-information/metric-guides/coin-issuance/puell-multiple | verified_primary | 2026-06-20 | Glassnode | Puell Multiple 官方定义（注 Puell 2019 originator） |
| T04-S044 | https://unchained.com/blog/hodl-waves-1 | verified_primary | 2026-06-20 | Dhruv Bansal | HODL Waves 原始文（Unchained Capital, 2018） |
| T04-S045 | https://userguide.cryptoquant.com/ | verified_primary | 2026-06-20 | CryptoQuant | 指标方法论 User Guide（含 MPI/Exchange Reserve） |
| T04-S046 | https://github.com/duneanalytics/spellbook | verified_primary | 2026-06-20 | Dune Analytics | Spellbook 开源 dbt 解释层（dex.trades 等规范表） |
| T04-S047 | https://web3datadegens.substack.com | verified_primary | 2026-06-20 | Andrew Hong | Dune/链上数据 canonical 教育者 Substack |
| T04-S048 | https://cryptohayes.substack.com/ | verified_primary | 2026-06-20 | Arthur Hayes | 作者本人站；反身性"observe don't predict"长文 |
| T04-S049 | https://insights.deribit.com/market-research/momentum-bitcoin-and-reflexivity/ | secondary | 2026-06-20 | Avi Felman / Deribit | 把 Soros 反身性具名应用于 BTC 动量 |
| T04-S050 | https://onrampbitcoin.com/from-graham-to-satoshi-a-value-investors-guide-to-bitcoin/ | secondary | 2026-06-20 | Onramp Bitcoin | Graham 价值框架→BTC（价值派借用最强证据） |
| T04-S051 | https://codex.arkm.com/ | verified_primary | 2026-06-20 | Arkham | Arkham Codex 官方文档（实体去匿名方法论） |
| T04-S052 | https://www.chainalysis.com/blog/chainalysis-data-accuracy/ | verified_primary | 2026-06-20 | Chainalysis | 聚类/数据准确性方法论（合规向，非估值） |
| T04-S053 | https://ocw.mit.edu/courses/15-s12-blockchain-and-money-fall-2018/pages/readings/ | verified_primary | 2026-06-20 | MIT (Gary Gensler) | MIT 15.S12 课程 reading list（隐性 canon，.edu 一手） |
| T04-S054 | https://www.cs.princeton.edu/~arvindn/bitcoin/ | verified_primary | 2026-06-20 | Princeton (Narayanan 等) | Bitcoin & Cryptocurrency Technologies 教材+课程（.edu 一手） |
| T04-S055 | https://nakamotoinstitute.org/library/shelling-out/ | secondary | 2026-06-20 | Nick Szabo | "Shelling Out"（unforgeable costliness, 2002） |
| T04-S056 | https://nakamotoinstitute.org/library/bit-gold/ | secondary | 2026-06-20 | Nick Szabo | "Bit Gold"（BTC 最直接前身, 2005） |
| T04-S057 | https://medium.com/john-pfeffer/an-institutional-investors-take-on-cryptoassets-690421158904 | secondary | 2026-06-20 | John Pfeffer | 机构投资者视角 + velocity problem（2017） |
| T04-S058 | https://uncommoncore.co/unpacking-bitcoins-social-contract/ | verified_primary | 2026-06-20 | Hasu | Bitcoin 社会契约/social layer（2018，作者站） |
| T04-S059 | https://uncommoncore.co/research-paper-a-model-for-bitcoins-security-and-the-declining-block-subsidy/ | verified_primary | 2026-06-20 | Hasu/Su Zhu/Prestwich | security budget 模型（2019） |
| T04-S060 | https://a16zcrypto.com/posts/article/crypto-readings-resources/ | verified_primary | 2026-06-20 | a16z crypto | a16z "Crypto Canon" 官方 reading list |
| T04-S061 | https://multicoin.capital/2018/08/08/aggregation-theory-thin-protocols-and-recentralization-augur-edition/ | secondary | 2026-06-20 | Kyle Samani | thin-protocol 反论（直接挑战 fat protocol） |
| T04-S062 | https://www.harpercollins.ca/9780062362506/digital-gold/ | secondary | 2026-06-20 | Nathaniel Popper | Digital Gold（BTC 早期叙事史, 2015）书目 |
| T04-S063 | https://www.coursera.org/specializations/decentralized-finance-duke | secondary | 2026-06-20 | Duke (C. Harvey) | DeFi 专项课程（Harvey 主讲，syllabus canon） |
| T04-S064 | https://www.citationneeded.news/review-read-write-own-by-chris-dixon/ | secondary | 2026-06-20 | Molly White | 对 Read Write Own 的批评性书评（COI 揭示） |
| T04-S065 | https://www.cato.org/sites/cato.org/files/serials/files/cato-journal/2018/9/cj-v38n3-14.pdf | secondary | 2026-06-20 | Cato Journal (Zuluaga) | 对 Bitcoin Standard 奥派决定论的学术批评 |
| T04-S066 | https://coinmetrics.substack.com/p/coin-metrics-state-of-the-network-6f5 | verified_primary | 2026-06-20 | Coin Metrics | SOTN #37 称 Pfeffer 文为"seminal article" |

> bucket 说明：whitepaper PDF / 作者本人博客 / 平台官方方法论文档 = `surrogate_primary`（作者原文/官方一手，但 source_verifier 默认判 secondary，按规范只升级不降级）；arXiv/SSRN/docs 子域 = `verified_primary`；Wikipedia / 第三方书评 / Medium 转述 = `secondary`；出版社/电商书目 = `reference`。**未私自把任何 secondary 标成 verified_primary。**

---

## 总览（按三类分组）

### 一、通用交易经典（被加密交易者反复借用）

| 书名 | 作者 | 难度 | Endorsement | 一句话 |
|------|------|------|-------------|--------|
| Reminiscences of a Stock Operator | Edwin Lefèvre (1923) | 入门 | ✅✅✅ | 投机心理/纪律的永恒寓言，加密交易者言必称 Livermore |
| Trading in the Zone | Mark Douglas (2000) | 入门 | ✅✅✅ | 交易心理 #1 必读，"概率思维"框架 |
| Trade Your Way to Financial Freedom | Van K. Tharp (1998/2007) | 进阶 | ✅✅✅ | 仓位管理>入场信号；R-multiple / 期望值奠基 |
| The Alchemy of Finance | George Soros (1987) | 高阶 | ✅✅✅ | 反身性（reflexivity）——加密叙事市场的元理论 |
| Fooled by Randomness / Antifragile (Incerto) | N. N. Taleb | 进阶 | ✅✅✅ | 随机性/反脆弱/遍历性——非对称下注心智 |
| The Most Important Thing | Howard Marks (2011) | 进阶 | ✅✅⚠️ | 风险=永久损失，二阶思维，周期定位（借用） |
| Market Wizards | Jack Schwager (1989) | 入门 | ✅✅⚠️ | 顶级交易者访谈——风格多样性样本库（借用） |
| The Intelligent Investor | Benjamin Graham (1949) | 进阶 | ✅✅⚠️ | Mr. Market / 安全边际——加密价值派借用框架 |

### 二、加密原生正典

| 标题 | 作者 | 类型 | 一句话 |
|------|------|------|--------|
| Bitcoin Whitepaper | Satoshi Nakamoto (2008) | whitepaper | 一切的起点；PoW + 去信任双花防御 |
| Ethereum Whitepaper | Vitalik Buterin (2013) | whitepaper | 图灵完备智能合约平台奠基 |
| Vitalik 博客文集 / Proof of Stake | Vitalik Buterin | 文集 | 以太坊路线图 + 加密哲学一手源 |
| The Bitcoin Standard | Saifedean Ammous (2018) | book | "sound money" 论 + 奥派框架（有争议） |
| Broken Money | Lyn Alden (2023) | book | 货币史+技术视角，最新宏观货币 canon |
| Cryptoassets | Burniske & Tatar (2017) | book | 加密资产估值框架奠基（NVT/INET） |
| DeFi and the Future of Finance | Campbell Harvey 等 (2021) | book/paper | 学术级 DeFi 系统化（AMM/借贷/收益） |
| Read Write Own | Chris Dixon (2024) | book | 代币网络论的"权威辩护" |
| Mastering Bitcoin / Mastering Ethereum | A. Antonopoulos | textbook | 协议层技术 ground truth |
| Digital Gold | Nathaniel Popper (2015) | narrative | BTC 早期史权威叙事（FT 年度入围） |
| "Fat Protocols" | Joel Monegro (2016) | essay | 价值在协议层 vs 应用层的奠基论题（已被挑战） |
| Shelling Out / Bit Gold | Nick Szabo (2002/05) | essay | BTC 前正典：不可伪造成本 + 概念蓝图 |
| Pfeffer "Institutional Investor's Take" | John Pfeffer (2017) | essay | 机构怀疑论 + velocity problem |
| Hasu "Bitcoin's Social Contract" + security budget | Hasu (2018/19) | essay | 社会层 vs 协议层 + security budget |
| Messari Crypto Theses（年度） | Ryan Selkis | annual report | 年度全景研报，行业必读 |

### 三、链上分析方法正典

| 资源/指标 | originator | 官方/原文 | 一句话 |
|-----------|-----------|-----------|--------|
| Glassnode Academy + Insights | Glassnode | T04-S017/S018 | 链上指标方法论事实标准 |
| Realized Cap | Carter & Le Calvez (2018) | T04-S018/S019 | 按最后移动价定价的"成本基础" market cap |
| MVRV | Puell & Mahmudov (2018) | T04-S017 | 市值/已实现值——顶底定位 |
| SOPR | Renato Shirakashi (2019) | T04-S017 | 已实现盈亏比——链上获利了结信号 |
| NUPL | Adamant Capital primer (2019) | T04-S035 | 净未实现盈亏——情绪周期 |
| NVT Ratio | Willy Woo & Burniske (2017) | T04-S025/S026 | "加密 PE"——网络价值/交易量 |
| Puell Multiple | David Puell (2019) | T04-S036 | 矿工收入偏离——发行端顶底 |
| CryptoQuant 文档 | CryptoQuant | T04-S020 | 交易所储备/流向/MPI 方法论 |
| Nansen 文档 | Nansen | T04-S021 | Smart Money 标签方法论 |
| Dune 文档 + Spellbook | Dune | T04-S022/S023 | 链上 SQL 教学事实标准 |
| Coin Metrics SOTN | Coin Metrics | T04-S024 | 网络数据方法论 + 自由流通供应量 |

---

## 一、通用交易经典（详）

### 📖 1. Reminiscences of a Stock Operator
- **Author**: Edwin Lefèvre（化名记述 Jesse Livermore）
- **Year**: 1923（公版，常重印）
- **Type**: 半虚构传记 / 投机心理经典
- **One-liner**: 加密交易者口中"过了 100 年市场还是同一群人"的源头——投机心理、纪律、止损的永恒寓言。
- **核心论点**: ① 市场反复因人性循环；② "钱是坐着等出来的不是交易出来的"（趋势耐心）；③ 早砍亏损、让盈利奔跑；④ 没有新鲜事——所有泡沫同构。
- **读完得到什么**: 对市场情绪/羊群/FOMO 的历史性免疫感——加密 memecoin 狂热的镜子。
- **难度**: 入门
- **Endorsement evidence**: ≥3 (evidence: [T04-S027])
  - `[type: figure_long]` Brad Mills（Bitcoin angel, Magic Internet Money 主播）整集播客把 Livermore↔rug-pull 类比
  - `[type: figure_short]` Vijay Boyapati（Bullish Case for Bitcoin）引"sitting"教训；Andy Edstrom（BTC 基金经理）"Required reading"
  - `[type: blog_secondary]` ShapeShift "Best Books for Crypto Traders" 书单；Florence Finance "我最爱的市场/交易书之一"
- **核心思想概念**: 投机心理、趋势耐心、亏损纪律、市场反身循环
- **可信度**: high / **Decay risk**: low

### 📖 2. Trading in the Zone
- **Author**: Mark Douglas
- **Year**: 2000
- **Type**: 交易心理学专著
- **One-liner**: 职业交易者最常推的单本心理书——把"为什么有边际还是会输"归到心理，给出概率思维框架。 (evidence: [T04-S027])
- **核心论点**: ① 交易输的 #1 原因是心理不是策略；② 用"概率思维"——单笔结果随机、长期分布确定；③ 接受不确定、消除恐惧/贪婪干扰；④ 一致性来自机械执行而非预测。
- **读完得到什么**: 把每笔交易当作概率分布里的一次抽样，停止对单笔结果情绪化。
- **难度**: 入门
- **Endorsement evidence**: ≥3 (evidence: [T04-S027])
  - `[type: course_syllabus]` 多数交易教育/心理课程列为心理学基石
  - `[type: blog_secondary]` 被多个加密交易者社区列"心理必读第一"
  - `[type: figure_short]` 与 Van Tharp/Douglas 常被并列推荐
- **核心思想概念**: 概率思维（probabilistic mindset）、一致性、交易心理
- **可信度**: high / **Decay risk**: low

### 📖 3. Trade Your Way to Financial Freedom
- **Author**: Van K. Tharp
- **Year**: 1998 / 2nd ed. 2007
- **Type**: 系统化交易 + 仓位管理
- **One-liner**: 把"仓位管理 > 入场信号"讲透——R-multiple / 期望值 / Optimal F 的奠基，加密风控的方法论母本。 (evidence: [T04-S027, T04-S028])
- **核心论点**: ① 仓位管理决定回撤/复利/存活，比入场重要；② R = 初始风险（止损距离），盈亏用 R 倍数衡量；③ 系统期望值（每 R 的平均回报）才是边际；④ System Quality Number 评估回报分布；⑤ 没有"最好系统"，只有"适合你心理的系统"。
- **读完得到什么**: 用 R-multiple 与期望值重构交易记录，把"赢率"祛魅。
- **难度**: 进阶
- **Endorsement evidence**: ≥3 (evidence: [T04-S027, T04-S028])
  - `[type: course_syllabus]` R-multiple 成为风控教学标准词汇（TraderLion 风控教程独立成章）
  - `[type: blog_secondary]` 加密交易者用 R 单位做仓位（每笔风险 1R）
  - `[type: figure_short]` 量化/手动加密交易者普遍引用 R 框架
- **核心思想概念**: R-multiple、position sizing、期望值（expectancy）、Optimal F
- **可信度**: high / **Decay risk**: low

### 📖 4. The Alchemy of Finance（反身性）
- **Author**: George Soros
- **Year**: 1987
- **Type**: 投资哲学 / 宏观
- **One-liner**: 反身性（reflexivity）——价格与基本面双向反馈的元理论；加密"叙事即基本面"市场的最佳解释器。 (evidence: [T04-S029, T04-S030])
- **核心论点**: ① 参与者认知与现实互相塑造（双向反馈环）；② 市场永远"错"但错法可被乘骑；③ 繁荣-崩溃序列由自我强化的反身环驱动；④ 可错性是常态。
- **读完得到什么**: 理解加密为什么"价格涨→采用涨→价格更涨"的反身循环，以及它如何反向崩塌。
- **难度**: 高阶（原书晦涩）
- **Endorsement evidence**: ≥3 (evidence: [T04-S029, T04-S048, T04-S049, T04-S030])
  - `[type: figure_long]` Arthur Hayes（BitMEX/Maelstrom）："reflexivity 是我学到的最强概念……channel your inner Soros — observe, don't predict"，应用于 ETH Merge（T04-S048）
  - `[type: figure_long]` Avi Felman（前 BlockTower 交易主管）Deribit Insights "Momentum, Bitcoin and Reflexivity" 具名归 Soros（T04-S049）
  - `[type: figure_short]` Su Zhu（三箭）Bankless SOTN #46 以反身性为策略核心（反讽：3AC 死于 LUNA 反身崩塌）
- **核心思想概念**: 反身性（reflexivity）、繁荣-崩溃序列、可错性、叙事反身
- **可信度**: high / **Decay risk**: low

### 📖 5. Incerto（Fooled by Randomness / The Black Swan / Antifragile）
- **Author**: Nassim Nicholas Taleb
- **Year**: 2001–2012
- **Type**: 哲学随笔 / 风险
- **One-liner**: 随机性、肥尾、反脆弱、遍历性——加密非对称下注（小亏无限、上行巨大）的思想底座。
- **核心论点**: ① 区分技巧与运气，警惕幸存者偏差；② 黑天鹅主导收益分布；③ 反脆弱=从波动中获益的凸性结构；④ 遍历性：群体期望≠个体路径，避免"赌身家"。
- **读完得到什么**: 用"凸性/凹性"看 portfolio——为什么小仓位赌长尾代币是反脆弱，全仓杠杆是脆弱。
- **难度**: 进阶
- **Endorsement evidence**: ≥3
  - `[type: figure_long]` Naval Ravikant 与 Taleb 同台（BLOCKCON 2018）："Bitcoin is the lindy currency"，框架化为非对称下注
  - `[type: figure_short]` Michael Saylor 的 BTC 阅读清单含 Antifragile
  - `[type: blog_secondary]` Bitcoin Magazine "How Antifragility Increases Bitcoin's Survivability"；Decrypt 引 Jimmy Song / Parker Lewis 论 BTC 反脆弱
- **核心思想概念**: 反脆弱（antifragility，最重）、肥尾/黑天鹅、杠铃策略（barbell）、凸性下注、Lindy 效应、技巧 vs 运气
- **关键反讽**: Taleb 本人 2021 后转为反比特币（"worth exactly zero"）——加密圈引用的是他**早期著作**而非其当前结论；其反 BTC 推文不计为 endorsement。
- **可信度**: high / **Decay risk**: low

### 📖 6. The Most Important Thing（Howard Marks）
- **Author**: Howard Marks（Oaktree）
- **Year**: 2011
- **Type**: 投资哲学
- **One-liner**: 风险=永久损失的可能（非波动率）、二阶思维、周期定位——价值派加密投资者的风控母语。
- **核心论点**: ① 风险是永久损失非波动；② 二阶思维（比共识想得更深一层）；③ 在哪个周期位置决定姿态；④ "等便宜的好资产"。
- **难度**: 进阶
- **Endorsement evidence**: ≥3（含 ⚠️：偏价值派，投机派引用少）
  - `[type: figure_short]` 加密价值派/基金引用 Marks memos
  - `[type: blog_secondary]` 周期分析文常引"where are we in the cycle"
  - `[type: course_syllabus]` 投资课程常列 Marks memos
- **核心思想概念**: 二阶思维、风险=永久损失、市场周期、逆向
- **可信度**: high / **Decay risk**: low

### 📖 7. Market Wizards（Jack Schwager）
- **Author**: Jack D. Schwager
- **Year**: 1989（系列延续至今）
- **Type**: 访谈集
- **One-liner**: 顶级交易者风格各异但风控共识一致——加密交易者证明"没有唯一正确风格"的样本库。
- **核心论点**: ① 风格多样（趋势/逆势/基本面/系统）；② 风控是唯一共性；③ 心理纪律决定存活；④ 找适合自己的方法。
- **难度**: 入门
- **Endorsement evidence**: ≥3（含 ⚠️）
  - `[type: blog_secondary]` 加密交易书单常列
  - `[type: figure_short]` 多位交易者点为入门
  - `[type: course_syllabus]` 交易教育平台标准书单
- **核心思想概念**: 风格多样性、风控共识、交易者画像
- **可信度**: high / **Decay risk**: low

### 📖 7b. The Intelligent Investor（借用框架）
- **Author**: Benjamin Graham（Jason Zweig 注释版）
- **Year**: 1949（修订注释版常用）
- **Type**: 价值投资奠基
- **One-liner**: 被加密**价值/基本面派**（尤其 BTC-value 学派）作为框架借用——Mr. Market、安全边际、投资者 vs 投机者，而非被供奉的文本。 (evidence: [T04-S050])
- **核心论点**: Mr. Market（把报价当躁郁症的出价而非裁决）；安全边际；投资者 vs 投机者之分；内在价值 > 价格；性情 > 智商。
- **难度**: 进阶（行文陈旧，现代价值多来自 Zweig 评注）
- **Endorsement evidence**: ≥3（含 ⚠️：是框架借用非具名 canon）(evidence: [T04-S050])
  - `[type: blog_secondary]` Onramp Bitcoin "From Graham to Satoshi: A Value Investor's Guide to Bitcoin"（最强加密原生引用）
  - `[type: blog_secondary]` Burniske & Tatar《Cryptoassets》被定位为"加密版 Intelligent Investor"（衍生 canon）
  - 反讽：Graham 衣钵传人 Buffett 是加密最大声批评者；未见任何 a16z/Placeholder/Multicoin 正式 syllabus 列入
- **核心思想概念**: Mr. Market、安全边际、内在价值、投资者 vs 投机者
- **可信度**: medium（框架借用）/ **Decay risk**: low

> **降级说明（诚实标注）**：**Van Tharp《Trade Your Way to Financial Freedom》**——其 R-multiple / 期望值 / SQN / 仓位管理**概念**在加密风控内容中无处不在，但很难找到加密原生 figure 在第一人称语境**具名推荐该书本身**；引用多来自教育品牌书单（Coin Bureau 等）。结论：作为"R-multiple/仓位管理词汇的来源"保留（见上 #3），但**作为具名 canon 书的强度弱于通用经典**。
> **DROP：Michael Mauboussin**——未找到 ≥3 个加密原生具名引用其书；base rates / 技巧vs运气 / 过程>结果等概念被顶级交易者间接吸收，但**不构成加密 canon**，仅作决策卫生概念入概念表，不单列条目。

---

## 二、加密原生正典（详）

### 📄 8. Bitcoin: A Peer-to-Peer Electronic Cash System（Bitcoin Whitepaper）
- **Author**: Satoshi Nakamoto
- **Venue + Year**: 自出版, 2008-10-31
- **URL**: T04-S001（bitcoin.org/bitcoin.pdf）
- **One-liner**: 一切的起点——用 PoW + 最长链规则解决去信任环境下的双花问题。
- **核心 idea**: ① 工作量证明（PoW）；② 时间戳链/最长链=诚实多数共识；③ UTXO 模型与电子签名链；④ 固定发行/激励相容。
- **为什么经典**: 行业字面意义的奠基文本，被纳入几乎所有 crypto syllabus，被无数协议直接实现。
- **如何读**: 9 页全读，重点 Section 4（PoW）、5（网络）、11（攻击概率）。
- **Endorsement evidence**: ≥3 (evidence: [T04-S053, T04-S054, T04-S001])
  - `[type: course_syllabus]` MIT 15.S12 "Blockchain and Money"（Gary Gensler）必读（T04-S053）
  - `[type: course_syllabus]` Princeton "Bitcoin and Cryptocurrency Technologies" 教材+课程（T04-S054）
  - `[type: conf_citation]` SSRN 学术存档索引；行业所有 keynote 起点引用
- **争议**: 作者身份未知（Craig Wright 主张被英国法院判为欺诈）；学术争论 PoW 是"解决"还是"绕过"拜占庭将军问题（开放成员的概率模型）。
- **后续/扩展**: Ethereum whitepaper；Nick Szabo "Bit Gold"/"Shelling Out"（前身思想，#17b）
- **可信度**: high / **Decay risk**: low

### 📄 9. Ethereum Whitepaper
- **Author**: Vitalik Buterin
- **Venue + Year**: 2013（whitepaper）/ 2014（yellow paper, Gavin Wood）
- **URL**: T04-S002
- **One-liner**: 把区块链从"货币"推广到"图灵完备的世界计算机"，开启智能合约/DeFi/链上交易的整片大陆。
- **核心 idea**: ① 账户模型 + EVM；② 智能合约即可编程货币；③ gas 计量；④ 任意状态转换。
- **为什么经典**: DeFi/链上交易全部建立其上；被纳入所有以太坊向课程。
- **如何读**: whitepaper 通读概念层；yellow paper 仅工程者深读。
- **Endorsement evidence**: ≥3（course_syllabus + conf_citation + figure_long）
- **后续/扩展**: Vitalik "Endgame"（T04-S004）；Proof of Stake 文集（T04-S005）
- **可信度**: high / **Decay risk**: low（概念稳定，路线图细节迭代快）

### 📖 10. Vitalik 博客文集 / 《Proof of Stake》（2022 文集）
- **Author**: Vitalik Buterin
- **Year**: 博客 2013–今；文集 2022（Seven Stories Press）
- **Type**: 长文合集（一手）
- **One-liner**: 以太坊路线图与加密哲学的一手源——"Endgame"（rollup-centric 扩容）、SBT、二次方融资、PoS 哲学。 (evidence: [T04-S003, T04-S004, T04-S005, T04-S033])
- **核心论点**: ① rollup-centric 路线（L2 扩容）；② Soulbound Token（身份/声誉非金融化）；③ 二次方融资/公共品；④ PoS 的安全/去中心化哲学。
- **读完得到什么**: 理解 L2/模块化叙事、积分/空投声誉机制、为什么以太坊这样演化。
- **难度**: 进阶
- **如果只读 1 篇**: "Endgame"（T04-S004）。
- **Endorsement evidence**: ≥3 (evidence: [T04-S003, T04-S033, T04-S005])
  - `[type: figure_long]` Nathan Schneider（CU Boulder）把其文集整理为学术书《Proof of Stake》（Seven Stories, 2022）；CoinDesk megareview
  - `[type: conf_citation]` 二次方融资论文（与 Hitzig & Weyl）arXiv 学术化；Gitcoin 生产实现 QF
  - `[type: figure_short]`（对抗性）Tuur Demeester 对其 PoS 设计哲学的严肃批评
- **争议**: PoW vs PoS 安全之争（maximalist 称 PoS 牺牲客观安全/"weak subjectivity"）；QF 的合谋/Sybil 脆弱；Endgame 的中心化出块/MEV 担忧。
- **核心思想概念**: rollup-centric 扩容、模块化、Soulbound Token、二次方融资
- **可信度**: high / **Decay risk**: medium（路线图细节会更新）

### 📖 11. The Bitcoin Standard
- **Author**: Saifedean Ammous
- **Year**: 2018
- **Type**: 货币经济学（奥地利学派框架）
- **One-liner**: 比特币"sound money"论的旗帜书——固定 21M 供应=最硬货币；**有显著争议**（奥派决定论 + 论战式语气）。 (evidence: [T04-S006, T04-S007])
- **核心论点**: ① "硬度"（stock-to-flow）决定货币优劣；② 法币贬值致时间偏好上升/文化衰退；③ BTC 是终极 sound money；④ 反凯恩斯。
- **读完得到什么**: 理解 BTC maximalist / "数字黄金"叙事的思想内核（即便不认同）。
- **争议**: 被批奥派经济决定论、把社会问题全归因法币、对反方论证engagement不足。 (evidence: [T04-S006, T04-S007])
- **难度**: 进阶
- **Endorsement evidence**: ≥3
  - `[type: figure_long]` Michael Saylor "a work of genius"，后撰写前言；Joseph Salerno（Mises Institute）背书
  - `[type: course_syllabus]` NYU Tandon "Intro to Blockchain & DLT" syllabus 列入
  - `[type: conf_citation]` 学术反方：Cato Journal（Diego Zuluaga）批奥派决定论（T04-S065）；Mises Wire 称 stock-to-flow 是"red herring"；Taleb 写完前言后公开撤回（与 Ammous 反目）
- **核心思想概念**: sound money、stock-to-flow、时间偏好、货币硬度
- **替代品**: Lyn Alden《Broken Money》（更中立、史料更全）
- **可信度**: medium（叙事强、立场重）/ **Decay risk**: low

### 📖 12. Broken Money
- **Author**: Lyn Alden
- **Year**: 2023
- **Type**: 货币史 + 技术
- **One-liner**: 当下最新、最中立的货币 canon——从美索不达米亚账本到 BTC，用"货币是账本+技术决定结算速度"重述货币史。 (evidence: [T04-S009, T04-S010])
- **核心论点**: ① 货币本质是账本；电报让结算中心化→法币脆弱；② BTC=结合信用与硬货币优点的"商品账本"；③ 稳定币给高通胀国家选择权；④ 能源-货币系统交叉视角。
- **读完得到什么**: 比 Bitcoin Standard 更平衡的宏观货币框架，作链上宏观交易的底层世界观。
- **难度**: 进阶
- **是否被 supersede**: 在"中立宏观货币 canon"上**优于** Bitcoin Standard，但后者作为 maximalist 思想史仍有独立价值，两者并存。
- **Endorsement evidence**: ≥3 (evidence: [T04-S009, T04-S010])
  - `[type: figure_long]` Preston Pysh（Bitcoin Fundamentals）整集长访谈讲书；作者常上 MacroVoices/Mauldin
  - `[type: figure_long]` Alex Gladstein（人权基金会）背书
  - `[type: figure_short]` Jack Dorsey、Jeff Booth 背书；10万+销量
- **核心思想概念**: 货币即账本、结算层、能源-货币交叉、稳定币选择权
- **可信度**: high / **Decay risk**: low

### 📖 13. Cryptoassets: The Innovative Investor's Guide
- **Author**: Chris Burniske & Jack Tatar
- **Year**: 2017
- **Type**: 投资框架
- **One-liner**: 加密资产估值框架的奠基——把"加密资产"作为新资产类别系统化，引入 NVT / 货币流速 / INET 估值模型。 (evidence: [T04-S031, T04-S032])
- **核心论点**: ① 加密资产=独立资产类别，需新估值法；② 货币数量论估值（INET 模型）；③ NVT 作"加密 PE"；④ 网络价值 vs 使用量。
- **读完得到什么**: 用基本面/网络指标（而非纯 TA）给代币估值的第一套框架。
- **难度**: 进阶
- **Endorsement evidence**: ≥3 (evidence: [T04-S031, T04-S032])
  - `[type: course_syllabus]` NYU Stern/Law "Digital Currency, Blockchains"（Yermack）必读教材
  - `[type: figure_long]` Brian Kelly（CNBC）作前言；CFA Institute Research Foundation 简报引用
  - `[type: blog_secondary]` 链上估值文常溯源至此
- **争议**: NVT 是滞后指标（Kalichkin "Rethinking NVT"）；Tim Swanson 尖锐负评称"aged very poorly"；velocity 模型受 Pfeffer(#17c) 挑战。
- **核心思想概念**: 加密资产类别（第五类）、INET/MV=PQ 估值模型、货币流速、NVT、J-curve
- **可信度**: high / **Decay risk**: medium（2017 框架，部分被新指标/DeFi 现金流估值补充）

### 📖 14. DeFi and the Future of Finance
- **Authors**: Campbell R. Harvey, Ashwin Ramachandran, Joey Santoro
- **Venue + Year**: Wiley 2021；前身 SSRN 草稿（免费）
- **URL**: T04-S008（SSRN）
- **One-liner**: 学术级 DeFi 系统化——AMM/借贷/收益/预言机/清算的第一本"教科书式"参考。
- **核心 idea**: ① DeFi 解决传统金融五大低效；② 深入 Uniswap/Compound 机制；③ 风险分类（智能合约/预言机/治理/缩放）；④ 收益来源拆解。
- **为什么经典**: Duke 金融教授署名（学术可信度）；免费 SSRN 可得；被列入多数 DeFi syllabus。
- **如何读**: 通读前半概念，机制章节配协议文档对照。
- **Endorsement evidence**: ≥3 (evidence: [T04-S008, T04-S063])
  - `[type: figure_long]` Vitalik Buterin 作序；Fred Ehrsam（Coinbase 联创/Paradigm）作前言
  - `[type: course_syllabus]` Duke DeFi 专项课程 Coursera（Harvey 主讲，T04-S063）
  - `[type: blog_secondary]` Brookings 书评（Aaron Klein）
- **争议**: Brookings 批其过于偏投机、对 AML/监管着墨少；其交易对手风险论述在 FTX(2022) 后显得乐观。
- **后续/扩展**: 各协议 docs；a16z DeFi 研报
- **可信度**: high / **Decay risk**: medium（DeFi 机制演化快，但框架稳）

### 📖 15. Read Write Own
- **Author**: Chris Dixon（a16z crypto）
- **Year**: 2024（Random House）
- **URL**: T04-S011
- **One-liner**: 代币网络论最体系化的"权威辩护"——把区块链放进互联网史，论证 token 网络对抗平台垄断。
- **核心论点**: ① 互联网从协议网络滑向公司网络；② 区块链=新一代"协议网络"；③ token 对齐建设者/用户激励；④ "casino vs computer"二分。
- **难度**: 入门-进阶
- **争议（COI 重要）**: Molly White 长篇批评（T04-S064）——"未能指出任何一个在规模上提供非投机服务的区块链项目"+未披露的利益冲突；a16z 向 Fairshake super-PAC 投 ~$47.5M 引"监管俘获"指控。核心指控：把自利的投资论题包装成中立未来学。
- **Endorsement evidence**: ≥3 (evidence: [T04-S011, T04-S064])
  - `[type: figure_long]` Tyler Cowen "最聪明、最锐利、最平衡的论述"；Laura Shin/Unchained "the definitive case"
  - `[type: figure_long]` Dixon 本人多个长播客
  - `[type: blog_secondary]`（对抗性）Molly White citationneeded 书评
- **核心思想概念**: 协议网络 vs 公司网络、token 激励对齐、"computer vs casino"、网络效应
- **可信度**: medium（强立场 + COI）/ **Decay risk**: low

### 📖 16. Mastering Bitcoin / Mastering Ethereum
- **Author**: Andreas M. Antonopoulos（Ethereum 卷与 Gavin Wood）
- **Year**: Mastering Bitcoin 2014/2nd 2017；Mastering Ethereum 2018（O'Reilly）
- **One-liner**: 协议层技术 ground truth——交易/UTXO/钱包/交易所机制/智能合约的工程参考。
- **核心论点**: ① UTXO 与交易构造；② 密钥/钱包/HD；③ 网络与挖矿；④（ETH 卷）EVM/gas/合约。
- **难度**: 进阶（偏技术）
- **是否 supersede**: 部分 API/工具过时，但协议核心机制仍准；链上交易者需懂"交易实际怎么构造"时仍是首选。
- **Endorsement evidence**: ≥3（course_syllabus + conf_citation + blog_secondary）
- **核心思想概念**: UTXO、交易构造、HD 钱包、EVM/gas
- **可信度**: high / **Decay risk**: medium（工具层）

### 📄 17. "Fat Protocols"（奠基论题）
- **Author**: Joel Monegro（USV）
- **Year**: 2016
- **URL**: T04-S013
- **One-liner**: "价值在协议层而非应用层"——加密投资逻辑最被引用的奠基论题，**也是最被挑战的**。 (evidence: [T04-S013, T04-S014])
- **核心 idea**: 与互联网（thin protocol / fat app）相反，区块链价值聚集在可投资的协议代币层。
- **为什么经典**: 定义了一整代"投 L1/协议"的论题；被无数研报引用。
- **争议**: 多篇反方长文（如 messyproblems）指应用层（如 Uniswap/稳定币发行方）正捕获更多价值，论题被部分推翻——**流派分裂关键文本**。 (evidence: [T04-S014])
- **Endorsement evidence**: ≥3 (evidence: [T04-S013, T04-S060, T04-S061, T04-S014])
  - `[type: course_syllabus]` a16z 官方 "Crypto Canon" reading list 列入（T04-S060）；Dani Grant "Cryptonetworks" syllabus
  - `[type: figure_long]` Kyle Samani/Multicoin 用 aggregation theory 直接反驳（thin-protocol，T04-S061）
  - `[type: blog_secondary]` Mason Nystrom "fat app thesis"、Michael Nadeau "Revisiting" 等反方长文
- **核心思想概念**: fat protocol thesis、价值捕获层、协议 vs 应用
- **可信度**: high（作为论题）/ **Decay risk**: medium（论题本身在被修正）

### 📄 17b. Nick Szabo — "Shelling Out"（2002）+ "Bit Gold"（2005）
- **Author**: Nick Szabo
- **Year**: 2002 / 2005
- **URL**: T04-S055 / T04-S056
- **One-liner**: 比特币的**前正典**——"Shelling Out"提出货币=unforgeable costliness（不可伪造的成本），"Bit Gold"是 BTC 最直接的概念蓝图。
- **核心 idea**: ① 收藏品→原始货币，货币解决以物易物的双重需求巧合；② 不可伪造的成本性（生产昂贵、验证容易）；③ Bit Gold = 链式 PoW + 分布式时间戳 + 拜占庭法定登记。
- **为什么经典**: 进 Princeton/Nakamoto Institute reading；Saifedean 在 Bitcoin Standard 直接引用 unforgeable costliness。
- **Endorsement evidence**: ≥3 (evidence: [T04-S055, T04-S056, T04-S054])
  - `[type: course_syllabus]` Princeton Bitcoin 教材指定阅读；Fermat's Library 学术注释
  - `[type: figure_long]` Saifedean《Bitcoin Standard》引 Bit Gold/unforgeable costliness
- **争议**: Bit Gold 从未实现（未解双花/Sybil，由 Satoshi 完成）；引发"Szabo=Satoshi"的（未证实）猜测，本人否认。
- **核心思想概念**: 不可伪造的成本、收藏品→货币、链式 PoW、Bit Gold
- **可信度**: high / **Decay risk**: low

### 📄 17c. John Pfeffer — "An (Institutional) Investor's Take on Cryptoassets"（2017）
- **Author**: John Pfeffer
- **Year**: 2017-12
- **URL**: T04-S057
- **One-liner**: 机构投资者视角的奠基性怀疑论——把货币数量论（MV=PQ）用于加密资产，形式化"velocity problem"（流速难题）。
- **核心 idea**: ① 在成熟均衡下分析；② 协议可分叉→剩余流向用户而非代币持有者；③ utility token 高流速→MV=PQ 把价值压到资源成本的零头；④ 唯一稳健例外=货币型价值储存（BTC）。
- **为什么经典**: Coin Metrics SOTN #37 称其 "seminal article"；进 UPenn/Berkeley 估值框架阅读。
- **Endorsement evidence**: ≥3 (evidence: [T04-S057, T04-S066])
  - `[type: conf_citation]` Coin Metrics SOTN #37 "seminal"
  - `[type: course_syllabus]` UPenn 论文、Berkeley Blockchain 估值框架引用
- **争议**: 与 Burniske 看多代币的 MV=PQ 模型直接对立；核心反驳=velocity sink（质押/work-token/HODL 降低流速）。
- **核心思想概念**: velocity problem、MV=PQ 应用、utility token 结构性低估值、第一性原理怀疑估值
- **可信度**: high / **Decay risk**: medium
- **价值框架三角（重要）**: Burniske（看多代币 MV=PQ, #13）vs Pfeffer（流速怀疑, 本条）vs velocity-sink 反驳，+ fat protocol（#17）vs thin-protocol（Samani）——**严肃从业者四方都读**。

### 📄 17d. Hasu — "Unpacking Bitcoin's Social Contract"（2018）+ security budget paper（2019）
- **Author**: Hasu（化名，后任 Flashbots 策略负责人）
- **Year**: 2018–2019
- **URL**: T04-S058 / T04-S059
- **One-liner**: 把"security budget""社会层""MEV"讲到大众可懂的范式研究者——加密研究随笔的标杆。
- **核心 idea**: ① BTC 是社会制度（社会层 vs 协议层；"协议偏离社会契约时，错的是协议"）；② security budget 难题（区块补贴→0 时手续费须养算力）；③ MEV 机制设计（PBS、MEV-Boost、抗审查）。
- **为什么经典**: Deribit Insights 延展；Crypto Words canon 存档；Jameson Lopp 参考库收录。
- **Endorsement evidence**: ≥3 (evidence: [T04-S058, T04-S059])
  - `[type: conf_citation]` Deribit Insights 构建于其社会契约框架
  - `[type: figure_long]` Jameson Lopp 参考库收录 security 论文
- **核心思想概念**: 社会层 vs 协议层、security budget、MEV/PBS、抗审查经济学
- **可信度**: high / **Decay risk**: low

### 📖 17e. Digital Gold（Nathaniel Popper, 2015）
- **Author**: Nathaniel Popper（NYT）
- **Year**: 2015
- **URL**: T04-S062
- **One-liner**: 比特币早期史的权威叙事——通过人物（cypherpunk、Winklevii、早期开发者、阿根廷/中国创业者、Silk Road）理解这场运动的社会动力。
- **核心 idea**: cypherpunk/数字现金前史；Satoshi 身份之谜；"misfits and millionaires"；早期交易所与 Silk Road。
- **为什么经典**: FT/McKinsey 年度商业书入围（2015）；NYT 书评"必读"；进 Gensler 课程。
- **难度**: 入门（叙事非技术）
- **Endorsement evidence**: ≥3（conf_citation: FT 入围 + figure_long: NYT 书评 + course_syllabus: Gensler 课程）
- **核心思想概念**: 加密社会史、Satoshi 之谜、早期生态人物
- **可信度**: high / **Decay risk**: low

### 📑 18. 研报型 canon：Messari Crypto Theses / a16z State of Crypto + Read Write Own / Delphi / Bankless
- **Author/host**: Ryan Selkis (Messari) / a16z crypto / Delphi Digital / Bankless（Ryan Sean Adams + David Hoffman）
- **Year**: 年度 rolling（Messari 自 2018；a16z State of Crypto 自 2022；Delphi/Bankless 自 2018–20）
- **URL**: T04-S015 / T04-S012 / T04-S016 / T04-S060
- **One-liner**: "研报型 canon"——真正被从业者读的年度全景与赛道研究（区别于 SEO 榜单）：Messari Theses（150+页年度 thesis）、a16z State of Crypto（采用度记分卡）、Delphi（多百小时基本面研究）、Bankless（"ultra sound money"/"money legos" 媒体范式）。
- **为什么经典**: Crypto Theses 被业界普遍称"最全年度概览"；a16z State of Crypto 是最常被引的年度采用度数据；Delphi "Year Ahead" 是年末必读；Bankless 是以太坊/DeFi 主导媒体节点。
- **如何读**: 不必通读，按赛道跳读 + 看 thesis 部分。
- **Endorsement evidence**: ≥3 (evidence: [T04-S015, T04-S012, T04-S060])
  - `[type: figure_long]` Lou Kerner（Quantum Economics）逐年评 Messari Theses + a16z State of Crypto
  - `[type: conf_citation]` Fortune 引 a16z 报告为年度主数据；ultrasound.money 归功 Bankless 推广"ultra sound money"
  - `[type: figure_long]` Real Vision（Raoul Pal）设 Delphi Research 专栏；Vitalik 多次选 Bankless 首发以太坊愿景
- **争议（COI 重要）**: Selkis 2024 政治化，殃及品牌，已退出日常管理；**Delphi 在 LUNA≈其 Ventures NAV 13% 时发 ~6 篇看多 Terra 报告，崩盘后承认"we were wrong"——Research/Labs/Ventures 一体化的结构性利益冲突**；Bankless 运营 BanklessDAO/$BANK 与 Bankless Ventures，编辑独立性受质疑。研报型 canon 整体是"有立场的倡导"，与中立的 whitepaper/教科书层有别。
- **核心思想概念**: 年度 thesis、赛道轮动/选链记分卡、模块化 vs 单体、ultra sound money、money legos、叙事即基础设施
- **可信度**: medium（有机构立场+COI）/ **Decay risk**: high（年度时效，按 last_updated 刷新）
- **Last_updated**: rolling，最新为各家年度版本

---

## 三、链上分析方法正典（详）

### 🎓 19. Glassnode Academy + Insights（链上指标方法论事实标准）
- **Host**: Glassnode
- **Format**: rolling 文档/Academy + 研究长文
- **URL**: T04-S017（Academy）/ T04-S018（Insights）/ T04-S019（docs）
- **One-liner**: 链上指标定义与方法论的事实标准——MVRV/SOPR/NUPL/Realized Cap/HODL Waves 的权威解释源。 (evidence: [T04-S017, T04-S018, T04-S019])
- **完整路径 vs 关键**: 先读 "Realized Cap Foundation"（T04-S018）建立成本基础直觉，再分指标读 Academy。
- **难度/先修**: 入门-进阶；需懂 UTXO。
- **Endorsement evidence**: ≥3（被分析师/研报/课程当作指标定义引用源）
- **Last_updated**: rolling（持续更新，最近含 STH/LTH 细分指标）
- **可信度**: high / **Decay risk**: medium（指标定义稳，新指标持续加）

### 💡 20. Realized Cap（已实现市值）
- **Tier**: tier-1
- **One-liner**: 按每枚币"最后一次链上移动时的价格"加总——网络整体的成本基础，而非现价市值。
- **来源**: `[primary]` Nic Carter **构想/演讲**（Baltic Honeybadger 2018）+ Antoine Le Calvez **命名与方法论实现**, Coin Metrics, 2018（Pierre Rochard 启发）(evidence: [T04-S018, T04-S024])
- **关联概念**: Realized Price、MVRV、NUPL（都建立其上）
- **为什么进 canon**: 把"币的成本"链上化，是几乎所有链上估值/盈亏指标的地基。
- **常见误用**: 当成"公允价值"——它是成本基础不是估值目标。
- **Endorsement evidence**: ≥3 (evidence: [T04-S018, T04-S019, T04-S024])

### 💡 21. MVRV（Market Value to Realized Value）
- **Tier**: tier-1
- **One-liner**: 市值 / 已实现市值——衡量整体未实现盈亏，做周期顶底定位。
- **来源**: `[primary]` Murad Mahmudov & David Puell, 2018-10-01（在 Realized Cap 上迭代，原文 T04-S040）(evidence: [T04-S040, T04-S017])
- **关联概念**: Realized Cap、MVRV Z-Score、NUPL
- **为什么进 canon**: 历史顶（>3.5）/底（<1）区间稳定，是周期定位最常用指标之一。
- **常见误用**: 跨资产/跨周期阈值照搬；牛熊结构变化使绝对阈值漂移。
- **Endorsement evidence**: ≥3 (evidence: [T04-S017])

### 💡 22. SOPR（Spent Output Profit Ratio）
- **Tier**: tier-1
- **One-liner**: 每个被花费 output 的"卖出价/买入价"，>1 整体获利了结、<1 亏损割肉。
- **来源**: `[primary]` Renato Shirakashi, 2019-04-25（原文 T04-S041）(evidence: [T04-S041, T04-S017])
- **关联概念**: aSOPR（调整版）、STH-SOPR / LTH-SOPR
- **为什么进 canon**: 直接读"链上获利了结/止损"行为，牛市 SOPR=1 常成支撑。
- **常见误用**: 忽略短期 noise，需用调整版/移动平均。
- **Endorsement evidence**: ≥3 (evidence: [T04-S017])

### 💡 23. NUPL（Net Unrealized Profit/Loss）
- **Tier**: tier-1
- **One-liner**: (市值−已实现市值)/市值——网络整体未实现盈亏占比，映射"恐惧→贪婪→欣快"情绪带。
- **来源**: `[primary]` 相对未实现盈亏框架 by Tuur Demeester & Michiel Lescrauwaet (Adamant Capital, 2019-04)；**NUPL 命名与形式化** by Rafael Schultze-Kraft (Glassnode CTO, 2019-11，原文 T04-S042) (evidence: [T04-S042, T04-S035])
- **关联概念**: Realized Cap、MVRV、STH/LTH-NUPL
- **为什么进 canon**: 情绪周期可视化（NUPL 分带：capitulation→belief→euphoria）。
- **常见误用**: 把情绪带当精确买卖点。
- **Endorsement evidence**: ≥3 (evidence: [T04-S035, T04-S017])

### 💡 24. NVT Ratio（Network Value to Transactions）
- **Tier**: tier-1
- **One-liner**: 网络价值 / 链上交易量——"加密 PE"，衡量网络估值相对其使用量是否过高。
- **来源**: `[primary]` Willy Woo 2017（指标，原文 T04-S039）+ Chris Burniske 提供"加密 PE"命名/类比（Token Summit 2017）；`[significant follow-up]` Dmitry Kalichkin "NVT Signal"（90日均线改进, 2018, T04-S026）(evidence: [T04-S039, T04-S025, T04-S026])
- **关联概念**: NVT Signal、RVT、货币流速
- **为什么进 canon**: 第一个被广泛接受的"链上基本面估值"比率。
- **常见误用**: 链上交易量受批量/混币/L2 迁移污染，绝对阈值不可跨链照搬。
- **Endorsement evidence**: ≥3 (evidence: [T04-S025, T04-S026, T04-S031])

### 💡 25. Puell Multiple
- **Tier**: tier-2
- **One-liner**: 当日矿工发行收入(USD) / 其 365 日均值——从"发行/卖压端"识别周期顶底。
- **来源**: `[primary]` David Puell 提出概念（2019-03，Glassnode docs 注其为 originator, T04-S043）；注：同名 canonical 文章 "The Puell Multiple"（Unconfiscatable）由 cryptopoiesis 撰写、Puell 署 originator——**非 Puell 本人执笔**(evidence: [T04-S043, T04-S036])
- **关联概念**: Miner Position Index (MPI)、矿工抛压
- **为什么进 canon**: 把矿工经济（结构性卖方）纳入周期模型。
- **常见误用**: 减半后发行结构变化使历史区间需重标。
- **Endorsement evidence**: ≥3 (evidence: [T04-S036, T04-S017])

### 🎓 26. CryptoQuant 文档（交易所流向/矿工指标）
- **Host**: CryptoQuant
- **Format**: rolling 文档/Academy
- **URL**: T04-S020
- **One-liner**: 交易所储备/净流入流出、稳定币流、MPI（Miner Position Index）等"资金流向"方法论权威源。
- **关键指标**: Exchange Reserve、Exchange Netflow、MPI、Stablecoin Ratio。
- **难度/先修**: 入门-进阶。
- **Endorsement evidence**: ≥3（被链上分析师/研报当流向定义源引用）
- **Last_updated**: rolling
- **可信度**: high / **Decay risk**: medium

### 🎓 27. Nansen 文档（Smart Money 钱包标签）
- **Host**: Nansen
- **Format**: rolling 文档
- **URL**: T04-S021
- **One-liner**: "Smart Money"标签与钱包实体识别方法论——把"跟聪明钱"从口号变成可查询数据。
- **关键概念**: Smart Money 标签、Token God Mode、钱包 PnL 画像。
- **常见误用**: 标签是启发式非真值；"Smart Money 买入"≠必赚。
- **Endorsement evidence**: ≥3
- **Last_updated**: rolling
- **可信度**: high（官方）/ **Decay risk**: medium

### 🎓 28. Dune Analytics 文档 + 学习资源（链上 SQL 事实标准）
- **Host**: Dune；canonical 教育者 Andrew Hong（"Learn Web3 Data"/cryptodatabytes）、hildobby
- **Format**: rolling 文档 + 教程
- **URL**: T04-S022（docs）/ T04-S023（learning-resources）/ T04-S034（Andrew Hong 进阶教程）
- **One-liner**: 自己写 SQL 查链上数据的事实标准——Spellbook 抽象表 + 社区 dashboard fork 文化。 (evidence: [T04-S022, T04-S023, T04-S034])
- **完整路径 vs 关键**: 先官方 docs 学 Dune SQL 语法 → Andrew Hong 进阶教程 → fork hildobby 等 wizard 的 dashboard 反推。
- **难度/先修**: 进阶；需 SQL 基础。
- **Endorsement evidence**: ≥3（官方 docs + canonical 教育者教程 + 社区 wizard）(evidence: [T04-S022, T04-S023, T04-S034])
- **Last_updated**: rolling（含 Dune AI 等新内容）
- **可信度**: high / **Decay risk**: medium（SQL 方言/Spellbook 演化）

### 🎓 29. Coin Metrics — State of the Network + 网络数据方法论
- **Host**: Coin Metrics
- **Format**: rolling newsletter + docs
- **URL**: T04-S024
- **One-liner**: Realized Cap 的诞生地；自由流通供应量（free float supply）、网络数据"清洗后真值"的方法论权威。
- **关键概念**: Realized Cap、Free Float Supply、Active Addresses、"trusted volume"。
- **Endorsement evidence**: ≥3（学术/研报引用其方法论）
- **Last_updated**: rolling（SOTN 周更）
- **可信度**: high / **Decay risk**: low（方法论稳定）

### 💡 30. Arkham Intelligence（实体情报）
- **Tier**: tier-2
- **One-liner**: 钱包→实体的去匿名化情报平台，把"某地址=某基金/交易所"的归因变可查询。
- **来源**: Arkham 官方文档/方法论
- **关联概念**: Nansen 标签、链上取证、entity clustering
- **常见误用**: 归因有概率性，误标会误导跟单。
- **Endorsement evidence**: ≥3（与 Nansen 并列为实体标签双标准）
- **可信度**: medium-high / **Decay risk**: medium

---

## 核心概念清单（曝光给 Track 06 去重；这里是 canon 层的"思想概念"）

> 区别于 Track 06 glossary 的黑话术语，这些是**会被提炼成心智模型**的思想级概念。

**通用交易思想（借用）**
1. R-multiple / 期望值（Van Tharp）— tier-1
2. Position sizing > 入场信号 — tier-1
3. 概率思维（probabilistic mindset, Douglas）— tier-1
4. 反身性（reflexivity, Soros）— tier-1
5. 反脆弱 / 凸性下注（antifragility, Taleb）— tier-1
6. 遍历性（ergodicity）/ 避免 ruin — tier-2
7. 肥尾 / 黑天鹅 — tier-2
8. 二阶思维（Howard Marks）— tier-2
9. 风险=永久损失 ≠ 波动率 — tier-2
10. 技巧 vs 运气（base rates, Mauboussin/Schwager）— tier-2

**加密原生思想**
11. 工作量证明 / Nakamoto 共识 — tier-1
12. sound money / stock-to-flow / 不可伪造成本（Szabo）— tier-1
13. 货币即账本 / 速度 vs 账本（Lyn Alden）— tier-2
14. tokenomics / 代币经济学估值 — tier-1
15. fat protocol vs thin protocol（价值捕获层之争）— tier-1
16. velocity problem / MV=PQ 估值（Pfeffer/Burniske）— tier-1
17. 货币溢价 / 数字黄金叙事 — tier-1
18. 叙事周期 / narrative-driven 市场 — tier-1
19. rollup-centric / 模块化 vs 单体扩容（Vitalik）— tier-2
20. 社会层 vs 协议层 / security budget（Hasu）— tier-2
20b. 协议网络 vs 公司网络 / "computer vs casino"（Dixon）— tier-2

**链上分析思想**
21. UTXO 成本基础（链上"成本"概念）— tier-1
22. Realized Cap（已实现市值）— tier-1
23. MVRV / 未实现盈亏周期定位 — tier-1
24. SOPR（链上获利了结行为）— tier-1
25. NUPL 情绪带（capitulation→euphoria）— tier-2
26. NVT（"加密 PE"基本面估值）— tier-1
27. HODL Waves / 币龄分布（Dhruv Bansal 2018）— tier-2
28. Coin Days Destroyed / Dormancy（老币活跃, ~2011 起源）— tier-2
29. 交易所流向 / 储备（卖压代理）— tier-1
30. Smart Money 跟踪 / 实体去匿名（标签即启发式，Nansen/Arkham）— tier-2
31. 矿工经济 / Puell Multiple / MPI（结构性卖方）— tier-2
32. Spellbook / 链上 SQL 解释层（dex.trades 等规范表）— tier-2

---

## Phase 2 提炼提示

### 反复出现 ≥3 个 canon 都讨论的核心 idea（候选行业心智模型）

- **「仓位/风控 > 预测」**：出现于 Van Tharp（R-multiple）/ Taleb（凸性+避免 ruin）/ Glassnode 链上盈亏框架 → **候选心智模型：把每笔交易当概率抽样，先定 1R 风险再谈方向**。
- **「成本基础 vs 现价」**：Realized Cap / MVRV / NUPL / SOPR 全建立在"链上已实现价格"上 → **候选心智模型：用链上成本基础判断"谁在盈利/亏损"，盈亏分布驱动行为**。
- **「叙事即基本面（反身性）」**：Soros 反身性 / fat protocol / Messari Theses 年度叙事 / Vitalik 路线图 → **候选心智模型：加密价格-采用-价格的反身环，叙事轮动是可交易结构**。
- **「sound money / 货币溢价」**：Bitcoin Standard / Broken Money / Cryptoassets → **候选心智模型：BTC 估值锚定货币溢价而非现金流，与 DeFi 代币的现金流估值分轨**。

### 智识谱系种子（流派分裂）

- **价值/基本面派 奠基**：Graham/Marks（借用）→ Burniske《Cryptoassets》（链上估值）→ Campbell Harvey《DeFi》（DeFi 现金流）→ Lyn Alden（宏观货币）。当前代表 → 与 Track 01 figure 关联（Burniske/Placeholder、Lyn Alden）。
- **投机/交易派 奠基**：Lefèvre/Livermore → Douglas（心理）→ Van Tharp（风控）→ Schwager（风格多样）。当前代表 → 加密 TA/交易者 figures。
- **链上分析派 奠基**：Nic Carter & Coin Metrics（Realized Cap）→ Willy Woo（NVT）→ Glassnode/CryptoQuant 体系。当前代表 → Glassnode/Nansen 分析师 figures。
- **BTC maximalist vs 多链/DeFi 分歧**：Bitcoin Standard（BTC-only sound money）vs Read Write Own / Ethereum 文集（可编程网络）——**这是 canon 内部最大的 still-debated 分裂**。
- **fat protocol 论争**：Monegro（2016, 价值在协议层）vs Kyle Samani/Multicoin（aggregation theory, thin-protocol）vs Mason Nystrom（fat app thesis）——**奠基文本之间直接对立**，Phase 2 应作为"流派分裂"样板呈现。
- **估值框架四方辩论（连接 #13/#17/#17c）**：Burniske 看多代币 MV=PQ（《Cryptoassets》）vs Pfeffer velocity problem（utility token 结构性低估值）vs velocity-sink 反驳（质押/work-token 降流速）vs fat-vs-thin protocol 价值捕获——**严肃从业者四方都读**，是 canon 内最成熟的智识辩论。

### 核心概念 → 候选 playbook

- **R-multiple 暗示**：「若不能先定义止损（1R）则不开仓；盈亏一律用 R 倍数记录复盘」。
- **MVRV/NUPL 暗示**：「若 MVRV 进历史极端区（顶部贪婪/底部投降）则降低/加仓而非追随情绪」。
- **反身性暗示**：「若价格上涨主要由叙事自我强化（而非链上基本面跟进）则警惕反身崩塌」。
- **交易所流向暗示**：「若大量币持续流入交易所则视为潜在卖压，反之净流出为筹码锁定」。
- **fat protocol 暗示**：「评估投 L1 还是 App 时，先判断价值在该生态实际捕获在哪一层，而非默认协议层」。
- **research COI 暗示**：「读研报型 canon（Messari/a16z/Delphi/Bankless）时，先查发行方的持仓/基金/PAC 利益——其是'有立场的倡导'而非中立数据；Delphi 在 LUNA 重仓时连发看多报告是经典教训」。
- **Su Zhu "supercycle" 反模式（cautionary）**：三箭 Su Zhu 2021-02 提"supercycle"论，2022-05 撤回"regrettably wrong"，随后 3AC 崩盘——**不作 canon 收录，只作"高 conviction + 杠杆"的反面教材**；其搭档 Hasu（#17d）声誉反升。**playbook**：「叙事 conviction 越强，越要对冲杠杆与单点暴露」。

### 冷僻 / 信号薄弱 / 中英失衡

- **canon 偏新且部分"前正典"**：加密原生书 < 10 年历史，许多"canon"实为奠基长文/年度研报而非教科书——已诚实三分（通用借用 / 原生 / 方法论）。
- **endorsement 类型偏轻**：相当比例 endorsement 来自 blog_secondary / 研报引用，纯学术 syllabus 较少（DeFi 学术化才刚起步）；已尽量配 figure_long（作者本人长访谈）补强。
- **中英失衡（强制标注）**：**独立中文一手 canon 极少**。zh-CN 市场的"canon"几乎全是：① 译作（《精通比特币》=Mastering Bitcoin 译本、梅兰妮·斯万《区块链：新经济蓝图》译本）；② 少量本土入门书（如李钧《比特币》）；③ 大量 KOL/研报/社群长 thread（多在知乎/公众号/CSDN——**全部黑名单**，未引用）。中文链上分析实践社群活跃，但其知识仍以"消费/转译 en canon"为主，**未产出被 ≥3 独立来源点过的独立中文一手 canon**。提炼时心智模型应以 en canon 为骨，zh 社群作"本地化实践层"而非 canon 层。
- **方法论散落 Track 05**：大量实操方法论在 podcast/Substack/Twitter thread（→ Track 05），本文件只收奠基级长文，故 canon 条目密度低于成熟学科属正常。
- **结论**：canon 维度**信号中等偏薄但结构清晰**——主因行业年轻 + 知识载体偏长文/研报而非教科书，**非数据缺失**。SKILL.md 诚实边界节应注明"加密交易 canon 以借用经典 + 原生长文为主，独立中文一手 canon 缺位"。
