# Track 03 — Workflows（工作流 / SOP / pipeline）：加密 / 链上交易 (Crypto & On-chain Trading)

> locale = global · 调研日 2026-06-20 · Phase 1 wave 3 第 3 路 subagent。
>
> **本行工作流特征**：(1) 衰减极快——memecoin 终端/MEV 防护 6-12 月换代，perp DEX 龙头格局 1 年剧变；(2) 流派分裂尖锐——价值长持 vs degen 速攻 vs 合约 vs 撸毛，几乎用不同的 SOP；(3) **失败成本不可逆**——丢私钥/被貔貅/杠杆爆仓/被女巫剔除都是「钱直接归零」，所以每个工作流的「风控前置」步骤跳过即可能归零，本文件刻意不把任何流程软化成「跟着做就赚」。
>
> **诚实分层**：很多「数字」（费率/清算阈值/ROI/share）是第三方观察或平台标称，口径随市场/报告波动，一律挂 source_id + caveat。文化黑话定义取业内共识口径（见 Track 06）。
>
> **seed 来源充足**：Wave 1+2（figures/tools）+ glossary/canon 贡献了 30+ workflow 片段（Track 02 子流派工具组合、Track 06「工作流变化触发」种子、Track 01 figure 叙事），本 track 把碎片拼成完整「入门 SOP + 资深路径」。

---

## Source Manifest

> bucket 由 `source_verifier.py classify` 给。**说明**：交易所/钱包厂商的官方 learn/academy 文档（CoinGlass / Coinbase / Kraken / Ledger / MetaMask）按 manifest 规范「vendor docs / 品牌官网 = verified_primary（vendor 一手）」手动升级（只升不降）；第三方教程/SEO/媒体保持 secondary。跨轨引用 T01/T02/T04/T06 的 source_id 直接复用。黑名单（知乎/公众号/百科/CSDN/付费喊单软文）一律未引。

| source_id | url | bucket | last_checked | author/host | one-line note |
|-----------|-----|--------|--------------|-------------|---------------|
| T03-S001 | https://openliquid.io/blog/token-safety-guide/ | verified_primary | 2026-06-20 | OpenLiquid | 买币前 token 安全评估流程（honeypot/LP/holders） |
| T03-S002 | https://www.market-research.uk/how-to-audit-your-tokenomics-to-spot-early-fraud-signals-and-protect-long-term-crypto-value | secondary | 2026-06-20 | market-research.uk | 代币经济学审计/早期欺诈信号 |
| T03-S003 | https://www.dextools.io/tutorials/how-to-use-axiom-solana-trading-bot-tutorial-2026 | secondary | 2026-06-20 | DEXTools | Axiom memecoin 交易流程教程(2026) |
| T03-S004 | https://www.dextools.io/tutorials/solana-memecoins-complete-guide-2026 | secondary | 2026-06-20 | DEXTools | Solana memecoin 完整 degen 流程(2026) |
| T03-S005 | https://orcabay.io/blog/airdrop-farming-strategy-and-metrics-outlook/ | verified_primary | 2026-06-20 | Orcabay | 撸毛策略/指标/监管展望(2025) |
| T03-S006 | https://www.htx.com/en-in/news/2025-airdrop-survival-rules-from-gold-everywhere-to-relying-pQH72Xka/ | secondary | 2026-06-20 | HTX Insights | 2025 撸毛生存规则(交易所媒体,利益冲突) |
| T03-S007 | https://www.coinglass.com/learn/2025-annual-report-en | verified_primary | 2026-06-20 | Coinglass | 2025 衍生品市场年报(数据方一手) |
| T03-S008 | https://www.coinglass.com/learn/funding-rates-1 | verified_primary | 2026-06-20 | Coinglass | 资金费率/热力图方法论(vendor 一手) |
| T03-S009 | https://metamask.io/news/leverage-margin-perpetual-futures-trading | verified_primary | 2026-06-20 | MetaMask | 杠杆/保证金(逐仓vs全仓)机制(vendor 一手) |
| T03-S010 | https://metamask.io/news/perpetual-futures-liquidation-mechanics | verified_primary | 2026-06-20 | MetaMask | 清算价计算/维持保证金机制(vendor 一手) |
| T03-S011 | https://onchainstandard.com/guides-education/track-whales-using-chain-analytics-tools/ | secondary | 2026-06-20 | OnchainStandard | Arkham/Nansen 巨鲸追踪流程(2025) |
| T03-S012 | https://www.ledger.com/academy/topics/crypto/how-to-track-crypto-whale-movements | verified_primary | 2026-06-20 | Ledger Academy | 巨鲸追踪 + 「signal not blueprint」(vendor 一手) |
| T03-S013 | https://financefeeds.com/follow-the-whales-smart-strategy-or-risky-move/ | secondary | 2026-06-20 | FinanceFeeds | 跟鲸风险/被狩猎反向收割 |
| T03-S014 | https://www.kraken.com/learn/finance/dollar-cost-averaging | verified_primary | 2026-06-20 | Kraken Learn | DCA/定投机制(vendor 一手) |
| T03-S015 | https://www.coinbase.com/learn/perpetual-futures/understanding-funding-rates-in-perpetual-futures | verified_primary | 2026-06-20 | Coinbase Learn | 永续/资金费率(vendor 一手) |

> **利益冲突标注**：T03-S006（HTX，交易所媒体）+ T03-S003/S004（DEXTools，工具站教程）仅作流程步骤参照，ROI/份额/速度数字不单独采信。

---

## 总览（按 decay risk 分组）

### High decay (12-month-class) — 3 个
| Workflow | Trigger | Output | Last_updated | 资深差异 |
|---------|---------|--------|-------------|---------|
| 2. 链上 degen 打新 / memecoin | 想博 100x 短线 | 一笔可承受归零的速攻仓 | 2026-06 | skip 多步、optimize 终端预设、add 钱包隔离 |
| 4. 聪明钱跟单 / 链上尽调 | 想跟 smart money | 跟单/反向决策 | 2026-06 | skip 噪音地址、optimize 自标 entity、add 反狩猎 |
| 5. 撸毛 / 空投 farming | 有 L2/新协议待空投 | 合规交互记录 + 空投 | 2026-06 | skip 多开、optimize 选项目、add 反女巫质量 |

### Medium decay — 2 个
| Workflow | Trigger | Output | Last_updated | 资深差异 |
|---------|---------|--------|-------------|---------|
| 1. 通用交易决策链 | 一轮交易从想法到落地 | 带风控的开-管-退闭环 | 2026-06 | skip 过度尽调、optimize 板块轮动、add 解锁日历 |
| 3. 合约 / 永续交易者 | 想做杠杆多空/对冲 | 带止损的杠杆仓 | 2026-06 | skip 高杠杆、optimize 费率读拥挤度、add 清算图 |

### Low decay — 2 个
| Workflow | Trigger | Output | Last_updated | 资深差异 |
|---------|---------|--------|-------------|---------|
| 6. 被动配置 / 定投 | 长期 BTC/ETH 配置 | DCA + 再平衡组合 | 2026-06 | skip 择时、optimize 自托管、add 周期止盈 |
| 7. 钱包安全 SOP | 自托管任何资产 | 冷热分层 + 授权卫生 | 2026-06 | skip 无、optimize Clear Signing、add 定期 revoke |

> 7 个 workflow，全部 ≥ 2 处资深差异。

---

## 1. 通用交易决策链（叙事判断 → 发现 → 尽调 → 风控 → 执行 → 监控 → 退出复盘）

- **One-liner**: 把「我觉得这个会涨」从冲动变成一条带风控前置的可重复管线，从「有一个想法」到「带止损/仓位/复盘记录的闭环」。
- **Trigger**: 一轮新的交易机会出现（叙事起势 / 看到标的 / 周期判断变化）。
- **Output**: 一笔有明确仓位 sizing、止损/止盈、执行场所、监控信号、退出计划 + 交易日志的持仓。

### 入门 SOP（minimum viable steps）
1. **叙事/赛道判断**：先定宏观——看 BTC.D（资金在主流还是山寨）、流动性环境、当前热门赛道（AI/RWA/DePIN/meme）轮动到哪。叙事先于基本面驱动价格 (evidence: [T06-S017, T01-S001])。
   - **跳过后果**：在熊市/流动性收缩期硬做多高 beta alt，逆周期被反复收割。
2. **标的发现**：在选定叙事里找具体标的（聪明钱在买什么 / Dexscreener 看新池 / 关注的 figure 提到的）。内行只谈「具体币 + 链 + 仓位」，不说「区块链投资」(evidence: [T06-S048])。
   - **跳过后果**：没有标的就没有交易；泛泛看好一个赛道无法落地。
3. **链上尽调 (due diligence)**：查代币经济学（分配是否集中 / VC 解锁）、解锁日历、合约审计、honeypot 检测、持仓分布（top holder >20% 警惕）、流动性是否锁仓且足额 (evidence: [T03-S001, T03-S002, T06-S039])。2025 上半年 >50% 新代币至少含一个安全红旗 (evidence: [T03-S001])。
   - **跳过后果**：买到貔貅（只能买不能卖）/ 高度集中盘被砸 / 解锁前一天高位接盘。
4. **风控前置（下单前定，不是亏了再想）**：定仓位 sizing（这笔占总资金多少 %）、最大可承受回撤、止损位（在哪里证明想法错了）、与现有持仓的相关性。仓位管理 > 选币，是生存核心 (evidence: [T06-S008, T04-S027])。
   - **跳过后果**：单标的 all-in，一次错误就重伤；无止损 = 把「扛单」当信仰直到归零。
5. **场所与执行**：选 CEX（法币腿/合规/深流动性，但托管）vs DEX（自托管，但要管滑点/MEV/gas）；选限价 vs 市价；大单考虑 TWAP 拆单。链上交易设合理滑点上限 + 开 MEV 保护 (evidence: [T02-S036, T06-S013, T06-S015])。
   - **跳过后果**：薄盘币无脑市价单吃滑点+冲击成本；链上不设滑点上限被三明治。
6. **持仓监控**：盯链上流向（巨鲸/交易所流入流出）、资金费率（永续拥挤度）、解锁日历、情绪/叙事是否退潮 (evidence: [T02-S005, T02-S043])。
   - **跳过后果**：解锁砸盘/巨鲸出货/叙事退潮你最后一个知道。
7. **退出与复盘**：分批止盈、按目标偏离再平衡、记交易日志（为什么进、为什么出、错在哪）。市场总会给新机会，要止盈 (evidence: [T01-S047])。
   - **跳过后果**：浮盈坐成浮亏；不复盘则同样的错反复犯。

### 资深路径（差异点）
- **skip**：资深人**跳过过度尽调**——对纯 meme/短线，不做「读 30 页白皮书+团队尽调」那套（那是给有基本面的项目的），meme 只看注意力+流动性+合约安全三项，省下 80% 尽调时间。给 meme 做基本面分析本身就是外行破绽 (evidence: [T06-S057])。
- **optimize**：资深人把**板块轮动**读成一套机械信号（BTC.D + 资金费率 + 链上流向交叉），不靠「感觉」判断叙事；用 figure 提到的「流动性 > 周期/叙事」当顶层框架而非追单个 KOL 喊单 (evidence: [T01-S001, T01-S006])。
- **add**：资深人**额外做解锁日历前置**——下单前先查 Token Unlocks，避开大额解锁窗口；并把「识别每个信息源的利益冲突（talk-his-book 是常态）」当固定一步 (evidence: [T02-S043, T01-S001])。

### 近期变化（近 12 个月）
- **2026-01 起**，由 Nansen 内置交易 + agentic trading 推动，「发现→执行」之间的工具链被压缩进单一界面（Nansen 对所有用户开放内置交易，Pro 0.10%/Free 0.25% 费）(evidence: [T02-S001])。触发事件类型：新工具。
- 触发事件类型：新工具 + 监管（MiCA 全面适用改变欧盟用户的合规场所选择）。
- 采用率：无精确数据；「链上数据驱动决策」已是主流派标配（Dune+Nansen+DefiLlama 三件套被反复点名）(evidence: [T02-S004])。

### 典型耗时
- 入门 SOP：单笔从想法到落地 30 分钟–数小时（尽调是瓶颈）。
- 资深路径：熟练后 10-30 分钟（机械化筛选 + 预设风控模板）。

### 关键工具（与 Track 02 关联）
- TradingView + CoinGecko（必备）、Dexscreener（发现）、Nansen/Arkham/Dune/DefiLlama（链上尽调）、Coinglass（费率/拥挤度）、Token Unlocks（解锁日历）、GoPlus/RugCheck（合约扫描）(evidence: [T02-S025, T02-S008, T02-S001])。

### 关键人物（与 Track 01 关联）
- Arthur Hayes / Lyn Alden（流动性宏观框架）；Cobie（trading the metagame 二阶思维、零信任、极少杠杆）；CryptoCred（自上而下 TA + 交易管理/失效位）；Pentoshi（止盈纪律）(evidence: [T01-S001, T01-S056, T01-S041, T01-S047])。

### 常见失败模式（CLI 化自检清单）
- **FOMO 追高**：在叙事顶部、巨鲸「买入」截图刺激下满仓追进 → 接盘出货。自检：「我是按计划进的，还是怕错过才进的？」(evidence: [T06-S051, T06-S032])。
- **不设止损/无仓位概念**：单标的 all-in、无止损扛单 → 一次错误重伤。自检：「这笔占我总资金几 %？止损在哪？」(evidence: [T06-S008])。
- **跟 KOL 喊单不 de-bias**：把 talk-his-book 当客观建议，KOL 点名标的常引跟风/出货。自检：「这个信息源持有它吗？他喊单他赚什么？」(evidence: [T01-S001, T01-S021])。
- **不查解锁就在解锁前高位接盘**：把大额解锁前一天当「价值投资」。自检：「未来 30 天有大额团队/VC 解锁吗？」(evidence: [T06-S040])。

### Last_updated: 2026-06-20
### Decay risk: medium（框架稳定，但工具链/监管 12-24 月持续优化）

---

## 2. 链上 degen 打新 / memecoin 速攻流程

- **One-liner**: 在链上 memecoin 里做「快进快出」的高死亡率博弈，从「扫到一个新币」到「一笔只投可承受归零额、过了安全闸的速攻仓」。
- **Trigger**: 想博 memecoin 短线（看到 Dexscreener/GMGN 新池起量、smart money 进场、社群叙事点火）。
- **Output**: 一笔已过 honeypot/rug 安全检查、设了滑点上限和 MEV 保护、只用可承受归零资金的快速进出仓。

### 入门 SOP（minimum viable steps）
1. **扫链/发现**：用 Dexscreener / GMGN / Photon / Axiom 按链筛新池，看流动性、买卖量、smart money 是否进场 (evidence: [T02-S008, T02-S009, T03-S004])。
   - **跳过后果**：没有发现层就没有标的；盲目从社媒链接进 = 头号钓鱼入口 (evidence: [T02-S017])。
2. **安全检查（下单前最后一道闸，不可跳）**：跑 honeypot 扫描（能不能卖出）+ 查 mint authority / freeze authority / top holder 集中度（>20% 警惕）/ dev 钱包是否还持有 / LP 是否锁仓 / 狙击钱包。多数终端内置扫描器（GMGN/Axiom/Photon/RugCheck）(evidence: [T03-S004, T02-S024, T02-S022])。
   - **跳过后果**：被貔貅（只能买不能卖，卖出收 90-100% 税）/ 被 rug（项目方抽干 LP）/ dev 砸盘 (evidence: [T06-S058, T06-S059])。
3. **设执行参数**：滑点上限设合理值（主流 3-5%、micro-cap meme 10-15%）、优先费/gas 给够、开 MEV 保护（Solana 走 Jito 私有 bundle / Jupiter dynamic slippage）(evidence: [T03-S004, T02-S035, T02-S030])。
   - **跳过后果**：高滑点 + 公共 mempool = 三明治机器人完美猎物，成交价远差于预期 (evidence: [T06-S025, T02-S035])。
4. **快速进出**：先用小额（如 $50）跑通整个流程（买入→验证成交→能卖出），第二笔才上真实资金；预设止盈/止损分批 (evidence: [T03-S004])。
   - **跳过后果**：第一笔就大额，遇到 honeypot/滑点异常直接重伤。
5. **风控边界**：只投「可以完全归零」的额度——土狗 99% 一个月归零，金狗是事后幸存者偏差 (evidence: [T06-S056, T06-S033])。
   - **跳过后果**：把 meme 仓当主仓，归零即伤筋动骨。

### 资深路径（差异点）
- **skip**：资深人对极早期/极薄盘的池子**直接跳过狙击**——不和狙击机器人抢同一秒，宁可错过也不在 dev 还持大量、LP 没锁、holder 高度集中时进（这些条件下「能不能卖」本身就是赌）(evidence: [T03-S004])。
- **optimize**：资深人把**终端预设成模板**（固定滑点档/优先费/MEV 保护/一键扫描），把每笔操作从「手动设 6 项」压到「看红绿灯一键」；并用 GMGN 的分析层（AI 合约风险 + smart money）做追踪而非用它执行 (evidence: [T02-S009, T02-S037])。
- **add**：资深人**额外做钱包隔离**——degen 速攻只用专门的「热钱包小仓」，主仓在冷钱包，且这个钱包定期 revoke 授权，避免一次恶意签名搬空全部 (evidence: [T02-S015, T02-S032])。

### 近期变化（近 12 个月）
- **memecoin 终端 ~6 个月换一代**：Axiom（2025-07 第三方称 ~73% 终端份额、日收入 ~16 万美元，交易所媒体口径，利益冲突）→ 与 GMGN/Photon/BullX Neo 持续洗牌；速度/界面/MEV 设置是竞争点 (evidence: [T02-S027, T02-S037, T03-S003])。触发事件类型：新工具。
- **2025-03 Jito 关闭公共 mempool**，掐掉最易得的抢跑嗅探源，付费私有 bundle（~$0.04/笔）成 Solana memecoin 标配 (evidence: [T02-S035])。触发事件类型：行业事件/基建变化。
- 当前采用率：份额数字本身即时效信号，6 个月后大概率重排。

### 典型耗时
- 入门 SOP：单笔分钟级（发现+扫描+执行），但学会「不被骗」要交大量学费。
- 资深路径：模板化后秒级执行，主要时间花在筛选而非操作。

### 关键工具（与 Track 02 关联）
- Dexscreener / GMGN / Photon / Axiom（发现+执行）、RugCheck / GoPlus（安全扫描）、Jito MEV Protect / Jupiter（执行防护）、Phantom（Solana 钱包）(evidence: [T02-S008, T02-S024, T02-S035])。

### 关键人物（与 Track 01 关联）
- Ansem（Solana 反身性 + UX 降摩擦，但反复劝阻 copy-trade）；⚠️ Murad（memecoin「超级周期」/tokenized cults，收录为争议案例，约 94% 跟随者亏损）(evidence: [T01-S020, T01-S033])。

### 常见失败模式（CLI 化自检清单）
- **不扫合约就裸冲新币**：买到貔貅卖不出 / 可升级合约后门增发抽干。自检：「我跑过 honeypot 扫描了吗？能确认可以卖出吗？」(evidence: [T02-S022, T06-S059])。
- **关掉滑点上限/MEV 保护**：被三明治吃掉差价还以为是行情波动。自检：「滑点上限设了吗？MEV 保护开了吗？」(evidence: [T02-S035])。
- **用 degen 钱包存大额/主仓**：一次恶意签名搬空全部。自检：「这是隔离的小仓热钱包吗？主仓在冷钱包吗？」(evidence: [T02-S015])。
- **从搜索广告/社媒链接进终端官网**：假官网 + drainer kit。自检：「我是从书签/可信聚合进的，核对了官方域名吗？」(evidence: [T02-S017])。
- **把金狗当可复制方法**：金狗是事后幸存者偏差，进场全是赌。自检：「我投的是可以完全归零的额度吗？」(evidence: [T06-S056])。

### Last_updated: 2026-06-20
### Decay risk: high（终端 6 个月换代、MEV 机制频繁变，全行业衰减最快）

---

## 3. 合约交易者流程（资金费率 → 杠杆/保证金 → 止损/清算 → 多空/对冲）

- **One-liner**: 用杠杆做多空/对冲，从「想用杠杆表达观点」到「一笔算好清算价、设了止损、选对保证金模式的杠杆仓」。
- **Trigger**: 想用永续合约做多空、对冲现货、或赚资金费率。
- **Output**: 一笔明确了杠杆倍数、保证金模式（逐仓/全仓）、止损位和清算价、并读过费率拥挤度的合约仓。

### 入门 SOP（minimum viable steps）
1. **读资金费率与清算地图**：用 Coinglass 看资金费率（多空拥挤度，正费率多头付空头）、未平仓 OI、多空比、清算热力图（找「磁吸价位」）。极端正费率 = 过热警告 (evidence: [T03-S008, T02-S005, T06-S009])。
   - **跳过后果**：在极度拥挤的一侧逆势加杠杆，被反向插针定点清算。
2. **选杠杆与保证金模式**：定杠杆倍数（越高清算价越近），选逐仓（isolated，亏损封顶在该仓保证金）vs 全仓（cross，动用全部余额抗单）(evidence: [T03-S009, T06-S011])。
   - **跳过后果**：误用全仓被一笔单连带其他持仓一起爆；100x 误以为稳赚，~1% 反向波动就归零 (evidence: [T06-S010, T06-S003])。
3. **算止损与清算价**：先算清算价（保证金不足维持要求时强平），把止损设在清算价之前（让自己主动出场而非被强平）。清算 = 损失消耗完保证金触发强制平仓 (evidence: [T03-S010, T06-S006])。
   - **跳过后果**：没算清算价就开仓，止损形同虚设，直接吃强平 + 穿仓。
4. **执行多空/对冲**：选场所（CEX 合约：深流动性但托管/KYC；Hyperliquid：链上订单簿自托管；GMX：AMM 型 retail）；对冲时用空单锁现货风险 (evidence: [T02-S011, T02-S028, T02-S029])。
   - **跳过后果**：选错场所（薄盘 perp 滑点大 / 不想 KYC 却用 CEX）。

### 资深路径（差异点）
- **skip**：资深人**跳过高杠杆**——多数老手长期用低杠杆（或几乎不用），且杠杆用于「减险/对冲」而非放大赌注（Cobie：「I use leverage close to never and typically to reduce risk」）。Su Zhu/3AC 是「信念 + 最大杠杆 = 系统性爆雷」的反面教材 (evidence: [T01-S023, T01-S043])。
- **optimize**：资深人把**资金费率读成情绪/拥挤度指标**而非成本——极端费率 + 清算热力图叠加，反向找「猎杀止损后的磁吸价位」，把别人的爆仓当自己的入场 (evidence: [T03-S008, T02-S005])。
- **add**：资深人**额外画清算热力图 + OI 突变**作为趋势/反转确认，并把「现货+永续对冲」当独立策略（赚资金费率/锁定价差）而非单边赌方向 (evidence: [T02-S005])。

### 近期变化（近 12 个月）
- **链上 perp 格局剧变**：Hyperliquid 2025 Q2 份额峰值 ~73%，到 2025 下半年因 Aster 等竞争跌到 ~38-40%（第三方观察，口径波动）；perp DEX 整体 2025 一度创 ~2tn 月量 (evidence: [T02-S034, T03-S007])。触发事件类型：行业事件/新进者。
- 触发事件类型：新工具（链上订单簿 perp 成熟，自托管杠杆体验逼近 CEX）。
- 当前采用率：份额格局 1 年内已大变，12-24 月可能再变。

### 典型耗时
- 入门 SOP：单笔 15-30 分钟（读费率 + 算清算价是瓶颈）。
- 资深路径：熟练后 5-10 分钟，主要时间在读拥挤度/清算图。

### 关键工具（与 Track 02 关联）
- Coinglass（费率/OI/清算热力图,必备）、TradingView（图表）、Hyperliquid/dYdX（订单簿 perp）/ GMX（AMM perp）、Glassnode（宏观）(evidence: [T02-S005, T02-S011, T02-S028])。

### 关键人物（与 Track 01 关联）
- Cobie（极少杠杆、用于减险）；CryptoCred（止损/失效位/交易管理）；⚠️ Su Zhu/3AC（杠杆爆雷反面教材）(evidence: [T01-S023, T01-S041, T01-S043])。

### 常见失败模式（CLI 化自检清单）
- **高杠杆 + 无止损**：~1% 反向波动爆仓归零，扛单等回本直到强平。自检：「我的清算价在哪？止损在清算价之前吗？」(evidence: [T06-S003, T06-S010])。
- **误用全仓模式**：一笔爆连带其他持仓一起爆。自检：「这是逐仓还是全仓？我清楚全仓会动用全部余额吗？」(evidence: [T06-S011])。
- **在极端费率一侧逆势加仓**：被定点猎杀止损（插针）。自检：「现在费率是不是极端？我是不是在拥挤的那一侧？」(evidence: [T03-S008, T06-S012])。
- **把对冲当方向赌**：本想锁风险却开成单边大杠杆。自检：「这笔是对冲还是裸赌方向？仓位匹配现货敞口吗？」(evidence: [T01-S023])。

### Last_updated: 2026-06-20
### Decay risk: medium（机制稳定，但场所格局 12-24 月会变）

---

## 4. 链上尽调 / 聪明钱跟单流程（标注 → 追踪 → 反狩猎）

- **One-liner**: 用链上标注追踪 smart money/巨鲸做信号参考，从「想跟聪明钱」到「一个把 smart money 当信号而非蓝图、且防被反向收割的跟单/反向决策」。
- **Trigger**: 想跟 smart money、追踪某巨鲸、或做链上尽调验证一个标的。
- **Output**: 一个基于链上 entity 行为的交易决策（跟/不跟/反向），带反狩猎防范。

### 入门 SOP（minimum viable steps）
1. **标注/识别 entity**：用 Nansen（smart money 标签 + 按胜率/盈利分类）/ Arkham（实体标注 + KOL 钱包追踪）给地址挂「实体名」，区分机构/skilled trader/VC/巨鲸 (evidence: [T03-S011, T02-S001, T02-S002])。
   - **跳过后果**：把单个地址当一个真人，不知一人控数百地址，标注是概率推断非身份证据 (evidence: [T06-S034])。
2. **设警报追踪**：对目标地址设警报，监控 swap 大小、流入/持有周期。流程：alert 触发 → 识别 entity → 确认趋势 → 跟或不跟 (evidence: [T03-S011, T03-S013])。
   - **跳过后果**：靠手动刷，错过时效；或把每个动作都当信号（噪音淹没）。
3. **交叉验证**：用 Dune/DefiLlama/Token Terminal 多源核对「真实资本流向」，不信单一 vendor 标签——Nansen 标签是私有启发式会误标 (evidence: [T02-S004, T02-S001])。
   - **跳过后果**：跟到误标地址 / 把交易所冷钱包归集当「巨鲸买入」FOMO (evidence: [T06-S032])。
4. **反狩猎防范**：把巨鲸动作当「信号而非蓝图」（signal not blueprint）——大额转移可能是对冲/内部钱包/复杂策略，不是简单买卖；警惕协调出货、跟单常接最后一棒 (evidence: [T03-S012, T03-S013, T06-S031])。
   - **跳过后果**：聪明钱出货时你跟单接盘；自己的大单暴露在公开 mempool 被反向狙击。

### 资深路径（差异点）
- **skip**：资深人**跳过绝大多数被标地址**——只盯极少数长期验证过的 entity，不追每一个「smart money 买入」推送（标注滞后、聪明钱也会被对手盘反杀）(evidence: [T06-S031])。
- **optimize**：资深人**自己在 Dune 写查询/自建 entity 标注**，不完全依赖 Nansen 的私有标签，验证「这个地址的历史真实胜率」而非信平台标签；把 smart money 当「值得研究的线索」而非「直接抄作业」(evidence: [T02-S003, T01-S031])。
- **add**：资深人**额外做反狩猎**——拆分大单/走私有 mempool 避免自己暴露；并主动识别「这个 smart money 是不是在被设局诱多」（聪明钱也会被狩猎），把 ZachXBT 式资金流追踪（地址聚类 + 链上链下交叉）当尽调标配 (evidence: [T02-S035, T01-S026])。

### 近期变化（近 12 个月）
- **2025 Arkham 上 KOL 标注系统**，追踪 100K+ 粉丝加密 KOL 的钱包；Nansen 按 entity 类型分类 + 实时胜率/盈亏，跨 30+ 链 (evidence: [T03-S011])。触发事件类型：新工具。
- **2026-02 Nansen 推 agentic / vibe trading**（内部跑 75 个 Claude agents），把「跟聪明钱」往自动化推 (evidence: [T01-S029, T02-S001])。触发事件类型：新工具/AI。
- 当前采用率：链上数据驱动已是主流派标配，但「smart money 跟单稳赚」仍是被反复证伪的外行幻觉 (evidence: [T06-S031])。

### 典型耗时
- 入门 SOP：设好警报后被动监控，单次决策分钟级。
- 资深路径：前期自建标注/查询要数小时-数天，之后高效复用。

### 关键工具（与 Track 02 关联）
- Nansen（smart money）、Arkham（实体标注,免费）、Dune（自建查询）、DefiLlama/Token Terminal（交叉验证）、DeBank（portfolio 追踪）(evidence: [T02-S001, T02-S002, T02-S003])。

### 关键人物（与 Track 01 关联）
- Alex Svanevik（smart money 标签 + agentic trading，但 vendor 立场需 de-bias）；ZachXBT（资金流追踪/地址聚类方法论）；Ansem（信息不对称衰减）(evidence: [T01-S029, T01-S026, T01-S020])。

### 常见失败模式（CLI 化自检清单）
- **把 smart money 当蓝图直接抄**：聪明钱出货时接最后一棒。自检：「这是信号还是蓝图？我有独立的进出场理由吗？」(evidence: [T03-S012, T06-S031])。
- **信单一平台标签不交叉**：跟到误标/交易所归集地址。自检：「我用第二个工具交叉验证过这个 entity 吗？」(evidence: [T02-S001])。
- **把地址当真人**：一人控数百地址，被表象误导。自检：「这是聚类后的 entity 还是单个孤立地址？」(evidence: [T06-S034])。
- **自己大单暴露在公开 mempool**：被反向狙击。自检：「我的大单拆了吗？走私有 mempool 了吗？」(evidence: [T02-S035])。

### Last_updated: 2026-06-20
### Decay risk: high（工具/标注/AI agent 12 月内显著迭代）

---

## 5. 撸毛 / 空投 farming 流程（选项目 → 交互 → 防女巫 → ROI 核算）

- **One-liner**: 通过链上交互博取未来空投，从「有协议待空投」到「一批合规、防女巫、算过 ROI 的真实交互记录」。
- **Trigger**: 有未发币的 L2/新协议、有空投预期。
- **Output**: 一批高质量、防女巫检测的交互记录 + 成本/ROI 核算（接受幸存者偏差）。

### 入门 SOP（minimum viable steps）
1. **选项目**：找无 token、高使用、有融资背景的项目（DefiLlama airdrops 板块 / L2Beat / 关注融资的协议）。选错项目 = 白干 (evidence: [T03-S005, T02-S039])。
   - **跳过后果**：交互了一堆最终零空投的项目，gas 全亏。
2. **真实交互**：做有意义的链上操作（swap/质押/桥/跨 L2），积累地址权重。2024 起转向「质量参与」而非交易量堆砌 (evidence: [T03-S005, T02-S039])。
   - **跳过后果**：机械刷量、特征雷同，被判女巫零空投。
3. **防女巫（关键）**：用单钱包/少量钱包做多样化、持续数月的真实交互，而非短期集中爆刷。「6 个月规律使用 > 6 天集中爆刷」(evidence: [T03-S005, T03-S006])。
   - **跳过后果**：多开钱包被聚类分析关联，批量剔除——85% 新空投已过滤女巫农场 (evidence: [T03-S005])。
4. **成本/ROI 核算**：算 gas 成本 + 时间成本 vs 预期空投价值，接受「大量项目最终零空投」的幸存者偏差 (evidence: [T03-S005, T06-S063])。
   - **跳过后果**：以为「撸毛免费赚钱」，实际多个项目零空投后净亏 gas。

### 资深路径（差异点）
- **skip**：资深人**跳过批量多开**——不再靠几十上百个钱包堆量（Sybil 检测会聚类剔除），转向 1-2 个钱包的深度质量参与，省下女巫被剔的风险 (evidence: [T03-S005, T02-S039])。
- **optimize**：资深人**像 VC 一样选项目**——早期识别有潜力的协议、提供真实价值、和生态建立长期关系，而非追每一个「免费空投」噪音 (evidence: [T03-S005])。
- **add**：资深人**额外做女巫规避的行为多样化**（不同时间/不同金额/真实使用路径，避免特征雷同）+ 每个钱包定期 revoke 授权（多钱包是 approval 风险放大器）(evidence: [T03-S005, T02-S032])。

### 近期变化（近 12 个月）
- **2025-26 女巫过滤成标配**：85% 新空投过滤 Sybil 农场，跳过女巫检测的多为低价值项目；ML 驱动的多钱包行为识别 + 链上聚类成主流 (evidence: [T03-S005])。触发事件类型：行业事件/反作弊升级。
- 触发事件类型：标准更新（从「交易量堆砌」到「质量参与」范式更替，2024 起）(evidence: [T02-S039])。
- 当前采用率：质量优于数量已是共识，但散户仍大量幸存者偏差地批量刷。

### 典型耗时
- 入门 SOP：数月持续小操作（不是一次性任务）。
- 资深路径：同样数月，但钱包数大减、单钱包深度增加。

### 关键工具（与 Track 02 关联）
- DefiLlama airdrops / L2Beat（标的发现）、Rabby（交易模拟）、DeBank（多钱包总览）、Revoke.cash（每钱包清授权）(evidence: [T02-S039, T02-S015, T02-S007])。

### 关键人物（与 Track 01 关联）
- 无单一 figure 主导此 workflow（撸毛是散户群体行为）；Track 02 避坑清单直接关联「不要盲目多开」(evidence: [T02-S039])。

### 常见失败模式（CLI 化自检清单）
- **批量多开被女巫剔除**：钱包间被聚类关联，零空投。自检：「我的钱包行为特征会被聚类成一组吗？」(evidence: [T03-S005])。
- **机械刷量特征雷同**：短期爆刷被判女巫。自检：「这看起来像真实长期使用，还是 snapshot 前突击？」(evidence: [T03-S005])。
- **不算 ROI 把撸毛当稳赚**：多项目零空投后净亏 gas。自检：「我算过 gas+时间成本 vs 预期空投了吗？接受幸存者偏差了吗？」(evidence: [T06-S063])。
- **多钱包留高危授权**：撸毛钱包遍布无限 approve。自检：「每个撸毛钱包定期 revoke 了吗？」(evidence: [T02-S032])。

### Last_updated: 2026-06-20
### Decay risk: high（反女巫机制 + 空投经济学持续演化）

---

## 6. 被动配置 / 定投流程（BTC/ETH 配置 + DCA + 再平衡）

- **One-liner**: 用纪律化的定投和再平衡做长期配置，从「想长期持有 BTC/ETH」到「一套去情绪的 DCA + 周期再平衡组合」。
- **Trigger**: 想做长期配置、不想盯盘、不想择时。
- **Output**: 一个自托管、按计划 DCA、按偏离再平衡的长期组合。

### 入门 SOP（minimum viable steps）
1. **定配置**：定 BTC/ETH/主流 alt 比例（一种简单起点：60-70% BTC / 20-30% ETH / 可选 10-20% 主流 alt；或分层 40% 大盘锚 / 30% 中盘 / 20% 稳定币+收益 / 10% 投机）(evidence: [T03-S014])。caveat：比例为第三方建议，随风险偏好/周期变。
   - **跳过后果**：用「数字货币」泛称不分类、风险错配（meme 当主仓）(evidence: [T06-S048])。
2. **DCA 定投**：固定金额、固定周期（周/月）买入，不管价格——去情绪、平滑成本，历史上跑赢 70-80% 择时者 (evidence: [T03-S014])。caveat：业内观察，过往不代表未来。
   - **跳过后果**：试图择时，熊市底割肉、牛市顶 FOMO，与周期反着走 (evidence: [T06-S045])。
3. **再平衡**：当某资产偏离目标 >10 个百分点时再平衡；优先用「新的 DCA 买入」调整而非卖出（避免触发应税事件）(evidence: [T03-S014])。
   - **跳过后果**：组合随单一资产暴涨/暴跌严重偏移，风险敞口失控。
4. **自托管**：长期持仓转入冷钱包，不长期锁在交易所（Not your keys, not your coins）(evidence: [T06-S019, T02-S018])。
   - **跳过后果**：交易所跑路/被黑（FTX）你没钥匙。

### 资深路径（差异点）
- **skip**：资深人**跳过择时焦虑**——明确放弃「抄底逃顶」，把 DCA 当系统而非每次都纠结「现在是不是好时机」(evidence: [T03-S014])。
- **optimize**：资深人**叠加链上宏观周期信号做再平衡触发**——用 Glassnode/CryptoQuant 的 MVRV/SOPR/HODL waves 判断周期位置（>3.5 MVRV 常预示牛市晚期派发），在周期高位分批止盈而非纯机械 (evidence: [T02-S042, T06-S035])。caveat：单一链上指标不孤立当买卖信号。
- **add**：资深人**额外把自托管做成纪律**（冷钱包 + Clear Signing + 助记词离线手写），并把「周期止盈」当 DCA 的对称动作——只买不卖会在顶部坐过山车 (evidence: [T02-S019, T01-S047])。

### 近期变化（近 12 个月）
- **现货 ETF + 稳定币立法改变入场路径**：2024-01 美国现货 BTC ETF 获批让传统资金合规入场，DCA 不一定走 CEX 自托管路径 (evidence: [T06-S070, T06-S013])。触发事件类型：法规变化。
- 触发事件类型：稳定，核心 DCA/再平衡机制 5+ 年无重大变化（最近一次显著变化是 2024 ETF 合规化）。
- 当前采用率：DCA 被广泛认为是 2025 最简单有效的长期策略 (evidence: [T03-S014])。

### 典型耗时
- 入门 SOP：初次设置 1 小时，之后每周/每月几分钟。
- 资深路径：同样轻量，多花在周期判断 + 自托管纪律上。

### 关键工具（与 Track 02 关联）
- Ledger（冷钱包）、DeBank（portfolio）、DefiLlama/Token Terminal（基本面）、Glassnode/CryptoQuant（周期指标）、Token Unlocks（解锁日历）(evidence: [T02-S018, T02-S007, T02-S042])。

### 关键人物（与 Track 01 关联）
- Lyn Alden（流动性 > 减半周期、长期货币框架）；Arthur Hayes（流动性宏观择时）；Pentoshi（止盈纪律）(evidence: [T01-S006, T01-S001, T01-S047])。

### 常见失败模式（CLI 化自检清单）
- **试图择时**：熊底割肉牛顶 FOMO。自检：「我在按计划定投，还是又在猜时机？」(evidence: [T06-S045])。
- **只买不卖（无止盈）**：周期高位坐过山车回吐。自检：「我有周期止盈计划吗，还是打算一直拿？」(evidence: [T01-S047])。
- **长期锁在交易所**：平台跑路你没钥匙。自检：「我的长期主仓在自托管冷钱包吗？」(evidence: [T06-S019])。
- **配置含大量 meme/高风险当「配置」**：风险错配。自检：「我的『被动配置』里有几成是会归零的投机仓？」(evidence: [T06-S048])。

### Last_updated: 2026-06-20
### Decay risk: low（DCA/再平衡稳态，最近显著变化是 2024 ETF 合规化）

---

## 7. 钱包安全 SOP（冷热分层 → 授权管理 → 防钓鱼/盲签）

- **One-liner**: 把自托管做成可重复的安全卫生流程，从「我要自己拿币」到「冷热分层 + 定期授权审计 + 不盲签的防御体系」。
- **Trigger**: 自托管任何资产（这是 #1/#2 工作流的安全底座，一切链上操作的根）。
- **Output**: 一套冷热分层、定期 revoke、开 Clear Signing/交易模拟、防钓鱼的安全配置。

### 入门 SOP（minimum viable steps）
1. **冷热分层**：大额/长持放硬件冷钱包（Ledger，私钥离线）；只把「交易仓」放热钱包（MetaMask/Phantom/Rabby）(evidence: [T02-S018, T02-S015])。
   - **跳过后果**：大额放热钱包 = 钓鱼/drainer 头号目标，2025 H1 钓鱼损失 >4 亿美元 (evidence: [T02-S017])。
2. **助记词离线**：助记词只离线手写，永不截图/云存/发「客服」。任何人索要 = 诈骗 (evidence: [T06-S018])。
   - **跳过后果**：助记词泄露 = 丢币不可逆。
3. **签名防御**：用 Rabby 的交易模拟（签名前看「这笔实际改变什么」）；硬件钱包开 Clear Signing（展示人类可读交易详情，不盲签 hash）(evidence: [T02-S015, T02-S019])。
   - **跳过后果**：盲签被篡改的合约调用——Bybit 14 亿被盗的直接环节就是签名者在硬件钱包上盲签了被篡改的 Safe 合约 (evidence: [T02-S019, T02-S033])。
4. **授权管理**：定期用 Revoke.cash 审计并撤销不再用的 approval（包括多年前 staking 留下的无限授权）(evidence: [T02-S020, T02-S032])。
   - **跳过后果**：钱包躺着几十个高危无限授权，合约被黑后你的钱被搬空。
5. **防钓鱼入口**：从书签/可信聚合（CoinGecko 合约地址）进官网，核对官方域名，不点搜索广告/社媒链接 (evidence: [T02-S017])。
   - **跳过后果**：进假官网 + drainer kit，几次点击批量被盗。

### 资深路径（差异点）
- **skip**：此 workflow **无可安全跳过的步骤**——安全是底座，资深人反而把每步做得更严（这是「资深 = 入门 SOP 无折扣 + 额外强化」的典型，诚实标注）。
- **optimize**：资深人**把 Clear Signing + 交易模拟当默认**而非可选——理解「冷钱包不防你亲手签恶意交易」，所以安全根是「签名层能看懂这笔交易」而非单纯冷/热之分 (evidence: [T02-S019, T02-S015])。
- **add**：资深人**额外做钱包分仓隔离**（degen 仓/金库仓/撸毛仓分开）+ 把「定期 revoke」排进日历（每月/每季），并对任何「假更新提示/假 airdrop 签名」保持默认怀疑 (evidence: [T02-S032, T02-S017])。

### 近期变化（近 12 个月）
- **2025-02-21 Bybit 14 亿美元被盗推动 Clear Signing 普及**：根因是签名者在 Ledger 上盲签了被篡改的 Safe 合约调用（设备只显示 hash 无法解码），Ledger 的应对是 Clear Signing（Ledger Stax 展示防篡改人类可读详情）(evidence: [T02-S019, T02-S033])。触发事件类型：行业事件（史上最大盗窃）。
- 触发事件类型：行业事件 + 标准更新（盲签从「不便」升级为「明确高危」共识）。
- 当前采用率：Clear Signing/交易模拟从进阶可选向「应当默认」迁移。

### 典型耗时
- 入门 SOP：初次设置 1-2 小时（买冷钱包/抄助记词/装 Rabby），之后定期 revoke 每次几分钟。
- 资深路径：同样，多花在分仓管理 + 定期审计纪律。

### 关键工具（与 Track 02 关联）
- Ledger（冷钱包 + Clear Signing）、Rabby（交易模拟）、MetaMask/Phantom（热钱包）、Revoke.cash / De.Fi（授权审计）(evidence: [T02-S018, T02-S015, T02-S020])。

### 关键人物（与 Track 01 关联）
- ZachXBT（反诈/链上取证，钓鱼链路分析的行业公共设施）；Ledger 官方复盘（Bybit 盲签事件）(evidence: [T01-S026, T02-S019])。

### 常见失败模式（CLI 化自检清单）
- **大额放热钱包**：钓鱼/drainer 头号目标。自检：「我的大额/主仓在硬件冷钱包吗？」(evidence: [T02-S017])。
- **盲签复杂交易**：签了被篡改的合约（Bybit 教训）。自检：「这笔交易我能看懂它实际改变什么吗？开 Clear Signing/交易模拟了吗？」(evidence: [T02-S019])。
- **助记词数字化**：截图/云存/发客服 = 丢币。自检：「我的助记词只在离线纸上吗？有人问就是诈骗。」(evidence: [T06-S018])。
- **从不 revoke**：钱包堆满高危无限授权。自检：「我上次 revoke 是什么时候？有躺着的无限授权吗？」(evidence: [T02-S032])。
- **点广告/社媒链接进官网**：假官网 drainer。自检：「我是从书签/核对过的官方域名进的吗？」(evidence: [T02-S017])。

### Last_updated: 2026-06-20
### Decay risk: low（安全原则稳态，工具/具体威胁形态会变；Bybit 事件是最近一次显著推动）

---

## Phase 2 提炼提示

**反复出现 ≥ 3 个 workflow 都包含的步骤**（候选 playbook 通则）:
- **「下单前风控前置」**（仓位 sizing + 止损/退出计划 + 安全扫描，先定好再执行）出现于 workflows: 1（通用决策链）/ 2（degen）/ 3（合约）/ 5（撸毛 ROI）→ 候选 playbook「**如果要建任何仓位，先定『能承受的最大损失 + 在哪证明错了』，再点确认**」。本行最强通则。
- **「钱包隔离 + 定期 revoke」** 出现于 workflows: 2（degen 小仓）/ 5（撸毛多钱包）/ 6（长持冷钱包）/ 7（安全 SOP）→ 候选 playbook「**热钱包只放交易仓，主仓冷钱包，每钱包定期清授权**」。
- **「多源交叉，不信单一 vendor/标签/数字」** 出现于 workflows: 1（尽调）/ 3（费率）/ 4（smart money 标签）/ 6（配置数字）→ 候选 playbook「**任何单一读数（TVL/标签/份额/ROI）都挂日期 + 第二源交叉**」。
- **「设滑点上限 + MEV 保护」** 出现于 workflows: 1（链上执行）/ 2（degen）→ 候选 playbook「**链上下单三件套：扫合约 + 设滑点上限 + 开 MEV 保护，缺一即裸奔**」(evidence: [T02-S035])。
- **「识别信息源利益冲突（talk-his-book 是常态）」** 出现于 workflows: 1（跟 KOL）/ 2（meme 喊单）/ 4（smart money 也带立场）→ 这是本行心智模型必带的元规则 (evidence: [T01-S001])。

**入门 SOP 和资深路径之间最大的差距**（候选 心智模型）:
- 入门 SOP 平均 ~5-7 步，资深路径主要差异**不是压缩步数，而是「在哪里克制」**：资深人普遍在「杠杆」（#3 跳过高杠杆）、「尽调深度」（#1 对 meme 跳过基本面尽调）、「钱包多开」（#5 跳过批量多开）、「择时」（#6 跳过抄底逃顶）四处**主动做减法**。→ 推断本行资深人的核心 edge = **「知道在哪里少做/不做」的克制力**，而非「比新手多做」。心智模型候选「**这一行靠活下来取胜，资深 = 知道哪些诱惑（高杠杆/FOMO/多开/择时）不碰**」。
- **例外（诚实标注）**：钱包安全 SOP（#7）资深路径**无可跳过步骤**——安全是唯一「资深 = 入门 SOP 不打折 + 额外强化」的 workflow。这本身是信号：本行最不可逆的损失（丢私钥/被盗）没有捷径。

**近期工作流变化的根本原因**（触发变化的事件类型分布）:
- **新工具/AI 驱动**（4 个 workflow）：Nansen 内置交易 + agentic trading（#1/#4）、memecoin 终端换代（#2）、Arkham KOL 标注（#4）。本行 workflow 衰减主因。
- **行业事件驱动**（3 个）：Bybit 14 亿盲签事件 → Clear Signing（#7）、Jito 关公共 mempool（#2）、Hyperliquid 份额剧变（#3）。
- **反作弊/标准更新**（1 个）：女巫过滤成标配（#5）。
- **法规驱动**（1 个）：现货 ETF + MiCA + 稳定币立法（#6 入场路径）。
- 主要驱动力 → Phase 2「外部驱动力」：**工具/AI 迭代 + 攻防螺旋（MEV/女巫/钓鱼）** 是本行 workflow 的两大持续改写源。

**时效信号（update 时优先刷的 workflow）**:
1. **#2 degen / memecoin**（high decay）—— 终端 6 个月换代，份额/速度数字本身即过期信号。
2. **#4 聪明钱跟单**（high decay）—— AI agent / 标注系统 12 月内显著迭代。
3. **#5 撸毛**（high decay）—— 反女巫机制 + 空投经济学持续演化。
4. **#3 合约**（medium）—— perp DEX 份额格局 1 年剧变。
5. **#7 安全 SOP 的「当前威胁形态」**（原则 low，但具体钓鱼/盲签手法持续变，Bybit 类事件会再推新标准）。

**冷僻 / 信号薄弱（诚实边界）**:
- workflow 数 = 7（≥ 6 目标，远超 4 floor）✅，资深差异点 100% workflow 都 ≥ 2 处 ✅，**不冷僻**。
- 一手 source 占比：本 track 15 条 manifest 中 vendor 一手（verified_primary）9 条 ≈ 60%，加上跨轨引用的大量 T01/T02 一手，整体一手占比充足 ✅。
- **诚实保留风险**：本行 workflow 的失败模式不可逆（丢私钥/被貔貅/杠杆爆仓/被女巫剔除/FOMO 接盘），每个 workflow 已标 actionable 自检清单，**未软化成「跟着做就赚」**。中文圈带单/喊单生态（杀猪盘/拉高出货）风险尤甚，Phase 2.8 须警示。
- **数字 caveat**：所有费率/清算/ROI/份额/配置比例数字均为 vendor 标称或第三方观察，口径随市场/报告波动，Phase 2 引用须保留日期 + caveat，不作精确定论。
