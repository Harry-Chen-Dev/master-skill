# Track 02 — Tools（工具栈 + 选型决策树）：加密 / 链上交易 (Crypto & On-chain Trading)

> locale = global. 调研日期 2026-06-20. Phase 1 wave 2 第 2 路 subagent。三层结构（必备 / 场景特化 / 新兴）+ 选型决策树 + 避坑清单，供 Phase 2 整合进 skill-template 的「工具栈与选型决策树」节。
>
> **本行工具栈特征**：(1) 衰减极快——memecoin 终端 6 个月换一代，perp DEX 龙头一年内份额从 73% 跌到 ~40%；(2) 流派分裂尖锐——CEX(托管) vs DEX(自托管)、链上分析 vs CEX 撮合；(3) 利益冲突高——返佣推广软文、付费榜单遍地，本文件刻意把 vendor 一手与第三方独立观察分层，数字一律挂来源 + 日期 caveat。
>
> **bucket 说明**：`source_verifier.py` 对所有 vendor 自定义域名默认返回 `secondary`（unknown host）。按 manifest 规范「vendor docs / 品牌官网 = verified_primary（vendor 一手）」，已对官方域名 + 官方 GitHub/docs 升级为 `verified_primary`（只升不降）。第三方对比/新闻/SEO 站保持 `secondary`。mental-model 类论断不靠单一 vendor。

---

## Source Manifest

| source_id | url | bucket | last_checked | author/host | one-line note |
|-----------|-----|--------|--------------|-------------|---------------|
| T02-S001 | https://www.nansen.ai | verified_primary | 2026-06-20 | Nansen | 链上分析/smart money 平台官网（vendor 一手） |
| T02-S002 | https://www.arkm.com | verified_primary | 2026-06-20 | Arkham Intelligence | 实体标注/deanonymize 平台官网 |
| T02-S003 | https://dune.com | verified_primary | 2026-06-20 | Dune Analytics | SQL 自建链上仪表盘官网 |
| T02-S004 | https://defillama.com | verified_primary | 2026-06-20 | DefiLlama | 开源 TVL 聚合器官网 |
| T02-S005 | https://www.coinglass.com | verified_primary | 2026-06-20 | Coinglass | 衍生品数据/清算热力图官网 |
| T02-S006 | https://tokenterminal.com | verified_primary | 2026-06-20 | Token Terminal | 协议基本面/财务指标官网 |
| T02-S007 | https://debank.com | verified_primary | 2026-06-20 | DeBank | EVM 钱包总览/portfolio 官网 |
| T02-S008 | https://dexscreener.com | verified_primary | 2026-06-20 | Dexscreener | DEX 新币/行情看板官网 |
| T02-S009 | https://gmgn.ai | verified_primary | 2026-06-20 | GMGN | memecoin 终端 + 风险扫描官网 |
| T02-S010 | https://photon-sol.tinyastro.io | verified_primary | 2026-06-20 | Photon | Solana 轻量交易终端官网 |
| T02-S011 | https://app.hyperliquid.xyz | verified_primary | 2026-06-20 | Hyperliquid | 链上订单簿 perp DEX 官网 |
| T02-S012 | https://jup.ag | verified_primary | 2026-06-20 | Jupiter | Solana DEX 聚合器官网 |
| T02-S013 | https://1inch.io | verified_primary | 2026-06-20 | 1inch | EVM DEX 聚合器（Pathfinder）官网 |
| T02-S014 | https://app.uniswap.org | verified_primary | 2026-06-20 | Uniswap Labs | 最大 EVM 现货 DEX 官网 |
| T02-S015 | https://rabby.io | verified_primary | 2026-06-20 | Rabby (DeBank) | 安全优先 EVM 热钱包官网 |
| T02-S016 | https://metamask.io | verified_primary | 2026-06-20 | MetaMask (Consensys) | 最普及 EVM 热钱包官网 |
| T02-S017 | https://phantom.com | verified_primary | 2026-06-20 | Phantom | Solana 主流热钱包官网 |
| T02-S018 | https://www.ledger.com | verified_primary | 2026-06-20 | Ledger | 硬件冷钱包官网 |
| T02-S019 | https://www.ledger.com/blog-learning-from-the-bybit-safe-attack | verified_primary | 2026-06-20 | Ledger | 官方复盘 Bybit 盲签事件 → Clear Signing |
| T02-S020 | https://revoke.cash | verified_primary | 2026-06-20 | Revoke.cash | 授权(approval)撤销工具官网 |
| T02-S021 | https://github.com/RevokeCash/revoke.cash | verified_primary | 2026-06-20 | RevokeCash | 开源仓库（MIT, TypeScript） |
| T02-S022 | https://gopluslabs.io | verified_primary | 2026-06-20 | GoPlus Security | 合约/token 安全 API（30+ 链）官网 |
| T02-S023 | https://de.fi | verified_primary | 2026-06-20 | De.Fi | rug/合约扫描器 + revoke 官网 |
| T02-S024 | https://rugcheck.xyz | verified_primary | 2026-06-20 | RugCheck | Solana 原生 token 风险红绿灯官网 |
| T02-S025 | https://www.tradingview.com | verified_primary | 2026-06-20 | TradingView | 图表/技术分析平台官网 |
| T02-S026 | https://www.coingecko.com | verified_primary | 2026-06-20 | CoinGecko | 行情/市值数据聚合官网 |
| T02-S027 | https://axiom.trade | verified_primary | 2026-06-20 | Axiom | 一体化链上交易终端官网 |
| T02-S028 | https://gmx.io | verified_primary | 2026-06-20 | GMX | AMM 型 perp DEX 官网 |
| T02-S029 | https://dydx.exchange | verified_primary | 2026-06-20 | dYdX | 订单簿 perp DEX (v4 应用链) 官网 |
| T02-S030 | https://solana.com/developers/guides/advanced/mev-protection | verified_primary | 2026-06-20 | Solana / Jito | 官方 MEV 防护(Jito DontFront)指南 |
| T02-S031 | https://www.helius.dev/blog/solana-mev-report | verified_primary | 2026-06-20 | Helius | Solana MEV 数据/机制深度报告（基建方一手） |
| T02-S032 | https://github.com/RevokeCash/approval-exploit-list | verified_primary | 2026-06-20 | RevokeCash | 已知 approval 滥用 exploit 清单 |
| T02-S033 | https://www.ledgerinsights.com/bybit-hack-phishing-involved-plus-how-to-prevent-similar-hacks/ | secondary | 2026-06-20 | Ledger Insights | Bybit hack 钓鱼+盲签链路分析 |
| T02-S034 | https://www.dlnews.com/articles/defi/aster-hyperliquid-drive-2-trillion-perp-dex-volume-surge/ | secondary | 2026-06-20 | DL News | perp DEX 2tn 量 + Aster 挑战 Hyperliquid |
| T02-S035 | https://www.dlnews.com/articles/defi/solana-users-use-jito-to-stop-sandwich-attacks-and-mev/ | secondary | 2026-06-20 | DL News | Solana 用户付费 Jito 防三明治 |
| T02-S036 | https://www.ccn.com/education/crypto/1inch-vs-jupiter-vs-cowswap-defi-aggregators-comparison/ | secondary | 2026-06-20 | CCN | 聚合器执行/费率/MEV 对比 |
| T02-S037 | https://www.mexc.com/news/1031729 | secondary | 2026-06-20 | MEXC News | 链上交易终端 2026 横评(利益冲突: 交易所媒体) |
| T02-S038 | https://de.fi/blog/rug-pull-checker-scanner-exploits | verified_primary | 2026-06-20 | De.Fi | 官方 rug-pull 扫描方法论 |
| T02-S039 | https://cryptonews.com/cryptocurrency/airdrop-farming/ | secondary | 2026-06-20 | Cryptonews | 撸毛/Sybil 检测演变 |
| T02-S040 | https://github.com/RevokeCash | secondary | 2026-06-20 | RevokeCash | 组织 GitHub（活跃度信号） |
| T02-S041 | https://cryptoquant.com | verified_primary | 2026-06-20 | CryptoQuant | 交易所流/链上指标官网 |
| T02-S042 | https://glassnode.com | verified_primary | 2026-06-20 | Glassnode | 链上指标/HODL waves 官网 |
| T02-S043 | https://token.unlocks.app | verified_primary | 2026-06-20 | Token Unlocks | 解锁日历官网 |
| T02-S044 | https://coinbureau.com/review/axiom-trade-review | secondary | 2026-06-20 | Coin Bureau | Axiom 第三方评测/费率 |

> **利益冲突标注**：T02-S037（MEXC News）为交易所自营媒体的工具横评，可能偏向有合作的终端，仅作流派/功能参照，份额数字不单独采信。

---

## 总览（按 tier 分组）

### 必备（13 个 / ≥80% 从业者用）

| 工具 | 一句话 | 类别 | Decay | Sources |
|------|--------|------|-------|---------|
| TradingView | 图表/技术分析事实标准 | 图表行情 | low | T02-S025 |
| CoinGecko / CoinMarketCap | 行情/市值/合约地址查询入口 | 图表行情 | low | T02-S026 |
| Dexscreener | DEX 新币/流动性/K 线看板 | 图表行情 | medium | T02-S008 |
| DefiLlama | 开源 TVL / 协议 / 链聚合事实标准 | 链上分析 | low | T02-S004 |
| Coinglass | 资金费率/未平仓/清算热力图 | 链上分析 | low | T02-S005 |
| Nansen | smart money / 标签钱包追踪 | 链上分析 | medium | T02-S001 |
| Arkham | 实体标注/deanonymize（免费） | 链上分析 | medium | T02-S002 |
| Dune Analytics | SQL 自建链上仪表盘 | 链上分析 | low | T02-S003 |
| MetaMask | 最普及 EVM 热钱包 | 钱包安全 | low | T02-S016 |
| Phantom | Solana 主流热钱包 | 钱包安全 | low | T02-S017 |
| Rabby | 安全优先 EVM 热钱包（交易模拟） | 钱包安全 | low | T02-S015 |
| Ledger | 硬件冷钱包事实标准 | 钱包安全 | low | T02-S018 |
| Revoke.cash | 授权(approval)撤销/审计 | 钱包安全 | low | T02-S020,S021 |

### 场景特化（9 个 / 特定子流派用）

| 工具 | 一句话 | 适用流派 | Decay | Sources |
|------|--------|---------|-------|---------|
| Hyperliquid | 链上订单簿 perp DEX 龙头 | 合约交易者 | medium | T02-S011,S034 |
| GMX | AMM 型 perp，零价格冲击/简单 | 合约交易者(retail) | medium | T02-S028 |
| dYdX (v4) | 订单簿 perp 应用链 | 合约交易者(pro) | medium | T02-S029 |
| Jupiter | Solana DEX 聚合器(~95% 份额) | 链上 degen / Solana | medium | T02-S012,S036 |
| 1inch | EVM DEX 聚合器(Pathfinder) | EVM 现货 | low | T02-S013,S036 |
| Uniswap | 最大 EVM 现货 DEX(底层流动性) | EVM 现货 | low | T02-S014 |
| GoPlus / De.Fi / RugCheck | 合约/honeypot/rug 扫描 | 链上 degen（必装） | medium | T02-S022,S023,S024 |
| DeBank | EVM 多链 portfolio 总览 | 价值长持 / 撸毛 | low | T02-S007 |
| Glassnode / CryptoQuant | 链上宏观指标/交易所流 | 价值长持 / 宏观 | low | T02-S042,S041 |

### 新兴（5 个 / 近 12 月起势, stability: experimental）

| 工具 | 一句话 | Decay | Sources |
|------|--------|-------|---------|
| Axiom | 一体化链上终端(终端+perp+发现) | high | T02-S027,S044,S037 |
| GMGN / Photon / BullX Neo | 迭代极快的 memecoin 交易终端 | high | T02-S009,S010,S037 |
| Jito MEV Protect / 私有 RPC | Solana 反三明治防护 | high | T02-S030,S031,S035 |
| AI 交易 agent（链上自治） | 持币+链上决策的自治协议 | high | （见新兴层卡片，无独立一手） |
| Token Terminal / Token Unlocks / RootData | 协议基本面 + 解锁/募资数据 | medium | T02-S006,S043 |

---

## 必备层

### 1. TradingView

- **One-liner**: 加密无关的图表/技术分析事实标准，几乎所有交易者画线、设警报、看多周期 K 线的起点。
- **Tier**: 必备（图表行情）
- **Maintainer / Owner**: TradingView Inc.（https://www.tradingview.com，evidence: [T02-S025]）
- **License**: proprietary（免费档可用，Pro 档解锁多图表/更多警报/无广告）
- **Maturity signals**: 行业基础设施，跨多链多所通用；CEX/DEX 普遍内嵌其图表 widget（last checked: 2026-06-20，evidence: [T02-S025]）
- **免费 vs 付费**: 免费档够用（1 图表/有限警报）；活跃交易者多付费解锁多警报、多图表布局。
- **不适合 / 替代方案**: 不提供链上数据/撮合，只是图表层；链上原生 K 线看 Dexscreener。
- **Decay risk**: low（24+ 月稳定，3+ 年行业基建）

### 2. CoinGecko / CoinMarketCap

- **One-liner**: 行情、市值、流通量、合约地址、交易所列表的中立查询入口（CoinGecko 被视为相对更中立，CMC 属 Binance）。
- **Tier**: 必备（图表行情）
- **Maintainer / Owner**: CoinGecko（https://www.coingecko.com，evidence: [T02-S026]）；CoinMarketCap（Binance 旗下）
- **License**: proprietary（免费查询；API 付费档）
- **典型用法**: 验证「真合约地址」（防钓鱼假币）、看市值/FDV、查所在交易所——撸毛/长持也用其 Earn 区看代币空投线索（evidence: [T02-S039]）。
- **不适合**: 上所前的链上新币不在其列表，看新币用 Dexscreener。
- **Decay risk**: low

### 3. Dexscreener

- **One-liner**: DEX 新币/流动性/价格/交易量实时看板，链上 degen 发现新币的第一屏。
- **Tier**: 必备（图表行情，degen 必装）
- **Maintainer / Owner**: Dexscreener（https://dexscreener.com，evidence: [T02-S008]）
- **License**: proprietary（免费；付费档解锁高级筛选/预警）
- **典型用法**: 按链/DEX 筛新池、看流动性深度与买卖税、跳转扫描器查合约。GoPlus 安全检查已被多个看板（含 Dexscreener）内嵌（evidence: [T02-S022]）。
- **不适合**: 不是撮合执行层；不替代独立 honeypot 扫描（内嵌检查只是首过滤）。
- **Decay risk**: medium（看板形态稳定，但新币发现场景被 Axiom/GMGN 这类终端蚕食）

### 4. DefiLlama

- **One-liner**: 开源、无 token 利益的 TVL / 协议 / 链 / 收益 / 解锁聚合事实标准，DeFi 资金「真去哪了」的中立读数。
- **Tier**: 必备（链上分析）
- **Maintainer / Owner**: DefiLlama（https://defillama.com，evidence: [T02-S004]）；开源、社区驱动
- **License**: open（公开方法论 + 开源适配器）
- **典型用法**: 看协议/链 TVL 趋势判断真实采用、查收益(yields)、用其 airdrops 板块追踪无 token 高使用项目（撸毛标的，evidence: [T02-S039]）；2025 还上线了 meta DEX 聚合器(DefiLlama Swap)。
- **不适合**: TVL 会被激励/循环借贷夸大，不能单独当「真实价值」读，要交叉 Token Terminal 收入。
- **Decay risk**: low（中立性 + 开源使其难被取代）

### 5. Coinglass

- **One-liner**: 跨所衍生品聚合——资金费率、未平仓(OI)、多空比、清算热力图，合约交易者读「拥挤度/挤压区」的标配。
- **Tier**: 必备（链上分析，合约向）
- **Maintainer / Owner**: Coinglass（https://www.coinglass.com，evidence: [T02-S005]）
- **License**: proprietary（免费核心数据；付费档解锁更细历史/高级指标）
- **典型用法**: 看资金费率判断多空拥挤、用清算热力图找「磁吸价位」、OI 突变作为趋势/反转信号（evidence: [T02-S005]）。一套典型组合是「TradingView + CoinGecko + 一个链上工具(Dune) + 一个风险工具(Coinglass) + 一个 DeFi 基本面工具(DefiLlama)」。
- **不适合**: 衍生品数据 ≠ 现货链上流向，需配链上工具。
- **Decay risk**: low

### 6. Nansen

- **One-liner**: 5 亿+ 标签钱包 + smart money 追踪 + Token God Mode，「聪明钱在买什么」的付费旗舰。
- **Tier**: 必备（链上分析）
- **Maintainer / Owner**: Nansen（https://www.nansen.ai，evidence: [T02-S001]）
- **License**: proprietary（有免费档；Pro 付费档解锁 smart money/signal/God Mode）
- **近期变化（近 12 月）**: Nansen 2 上线 Signal(实时非常规链上活动告警) + Smart Segment；2026-01-21 起对所有用户开放内置交易，Pro 0.10% / Free 0.25% 交易费（平台标称，evidence: [T02-S001]）。
- **不适合 / 替代**: 对新手/休闲投资者偏贵，免费替代是 Arkham（evidence: [T02-S002]）；标签是 Nansen 私有启发式，非 ground truth，会有误标。
- **生产案例**: 「Dune + Nansen + DefiLlama 显示用户/流动性/真实资本实际去向」是被反复点名的链上三件套（evidence: [T02-S004]）。
- **Decay risk**: medium（产品迭代快，但 5 亿标签护城河使其难被快速取代）

### 7. Arkham Intelligence

- **One-liner**: 实体级标注 + 钱包 deanonymize，免费即可追踪机构/个人地址的链上情报平台。
- **Tier**: 必备（链上分析，免费向）
- **Maintainer / Owner**: Arkham Intelligence（https://www.arkm.com，evidence: [T02-S002]）
- **License**: proprietary（核心功能免费；有 INTEL token + 情报交易所）
- **典型用法**: 给地址挂「实体名」（交易所/基金/KOL）、做 entity 维度追踪——是 Nansen 之外的免费 smart money 入口（evidence: [T02-S001]）。
- **不适合**: 实体标注准确度参差，敏感操作需自行二次核对；smart money 深度功能弱于 Nansen。
- **Decay risk**: medium

### 8. Dune Analytics

- **One-liner**: 用 SQL 自建链上仪表盘的开放平台，「自己问链上数据」的工程化入口 + 社区共享 dashboard 海洋。
- **Tier**: 必备（链上分析）
- **Maintainer / Owner**: Dune（https://dune.com，evidence: [T02-S003]）
- **License**: proprietary 平台（query/dashboard 可公开共享；免费档可建/fork query）
- **典型用法**: fork 社区 dashboard 看协议指标、写 SQL 验证自己的假设、追踪具体合约的资金流（evidence: [T02-S003]）。与 Nansen/DefiLlama 并列为「真实资本流向」三件套（evidence: [T02-S004]）。
- **不适合**: 有 SQL 学习曲线；不是实时告警工具（查询有延迟），实时盯盘用 Nansen Signal/终端。
- **Decay risk**: low（已是链上分析基建）

### 9. MetaMask

- **One-liner**: 最普及的 EVM 热钱包，兼容性/dApp 接入最广——「raw compatibility 之王」。
- **Tier**: 必备（钱包安全）
- **Maintainer / Owner**: Consensys（https://metamask.io，evidence: [T02-S016]）
- **License**: 部分开源 / proprietary
- **典型用法**: 接入几乎所有 EVM dApp 的默认钱包；但需手动切网络、缺事前风险扫描（evidence: [T02-S015]）。
- **不适合 / 替代**: 安全敏感操作不如 Rabby（无交易模拟/风险标记），隐私上有数据收集争议（evidence: [T02-S015]）。大额仅热钱包持有 = 错误用法，应配硬件钱包。
- **Decay risk**: low

### 10. Phantom

- **One-liner**: Solana 生态主流热钱包（现已多链），memecoin/Solana degen 的默认入口。
- **Tier**: 必备（钱包安全，Solana 向）
- **Maintainer / Owner**: Phantom（https://phantom.com，evidence: [T02-S017]）
- **License**: proprietary
- **典型用法**: Solana 现货/memecoin 签名、内置 swap。
- **避坑提示**: 是钓鱼/drainer 的头号仿冒目标——「假更新提示/假 airdrop 站」要求签名即盗私钥；2025 H1 钓鱼损失超 4 亿美元（第三方观察，evidence: [T02-S017]）。
- **不适合**: 大额/长持仍需硬件冷钱包。
- **Decay risk**: low

### 11. Rabby

- **One-liner**: 安全优先的 EVM 热钱包——每笔交易做模拟、显示余额变化/授权/风险标记、自动切网络、内置 approval 管理。
- **Tier**: 必备（钱包安全，进阶向）
- **Maintainer / Owner**: Rabby（DeBank 团队，https://rabby.io，evidence: [T02-S015]）
- **License**: open-source
- **典型用法**: 签名前看「这笔交易实际会改变什么」（交易模拟）——这是 MetaMask 不提供的，能拦下大量恶意签名（evidence: [T02-S015]）。
- **不适合 / 替代**: dApp 兼容性偶尔不如 MetaMask（极少数站点只识别 MetaMask）。
- **Decay risk**: low

### 12. Ledger（硬件冷钱包）

- **One-liner**: 硬件冷钱包事实标准，私钥离线——长持/大额资产的「自托管底座」。
- **Tier**: 必备（钱包安全）
- **Maintainer / Owner**: Ledger（https://www.ledger.com，evidence: [T02-S018]）；同类 Trezor
- **License**: proprietary 硬件 + 部分开源固件
- **近期变化 / 关键教训**: 2025-02-21 Bybit 14 亿美元被盗，根因之一是签名者在 Ledger 上**盲签**(blind signing)——设备只显示交易 hash，无法解码被篡改的 Safe 合约调用，于是签了恶意交易（evidence: [T02-S019, T02-S033]）。Ledger 的应对是 Clear Signing（在 Ledger Stax 上展示防篡改的人类可读交易详情）（evidence: [T02-S019]）。
- **不适合**: 高频链上交易不便（每笔要物理确认）；冷钱包不防「你亲手签了恶意交易」——需 Clear Signing + 交易模拟。
- **Decay risk**: low

### 13. Revoke.cash

- **One-liner**: 审计并撤销你授权过的合约 approval/allowance（100+ 链），「定期清授权」的安全卫生工具。
- **Tier**: 必备（钱包安全）
- **Maintainer / Owner**: Revoke.cash（https://revoke.cash，evidence: [T02-S020]）
- **License**: open（MIT, TypeScript；主仓 766 stars，last checked: 2026-06-20，evidence: [T02-S021]）
- **Activity**: 组织 GitHub 活跃，维护 approval-exploit-list（已知 approval 滥用清单，evidence: [T02-S032, T02-S040]）。
- **典型用法**: 定期撤销不再用的 approval（包括多年前 staking 留下的无限授权），降低「合约被黑后你的钱被搬空」风险（evidence: [T02-S015]）。Rabby/De.Fi 也内置了同类 revoke 能力。
- **Decay risk**: low

---

## 场景特化层

> 子流派工具组合先行（供 Phase 2 + 决策树直接复用）：
> - **链上 degen（memecoin 速攻）**：Phantom + Dexscreener + GMGN/Photon/Axiom 终端 + RugCheck/GoPlus + Jito MEV Protect + Jupiter。
> - **合约交易者（永续）**：TradingView + Coinglass + Hyperliquid(链上) 或 CEX 合约 + Glassnode(宏观)。
> - **价值长持**：Ledger(冷钱包) + DeBank(portfolio) + DefiLlama/Token Terminal(基本面) + Glassnode/CryptoQuant(链上宏观) + Token Unlocks(解锁日历)。
> - **撸毛 farmer**：Rabby + DeBank(多钱包总览) + DefiLlama airdrops/L2Beat(标的发现) + Revoke.cash(每钱包清授权)。

### 14. Hyperliquid

- **One-liner**: 链上订单簿 perp DEX，给专业交易者深流动性 + 精确价格发现，是 2025 链上永续的标志性龙头。
- **Tier**: 场景特化（合约交易者）
- **Maintainer / Owner**: Hyperliquid（自有 L1，https://app.hyperliquid.xyz，evidence: [T02-S011]）
- **License**: proprietary 协议（有 HYPE token）
- **典型使用场景**: 想做永续但不想用 CEX(托管/KYC) → Hyperliquid 提供 CEX 级体验 + 自托管；builder-deployed 市场把可交易标的扩到长尾。
- **Maturity / 近期变化**: 早期 2025 Q2 份额峰值 ~73%，到 2025 下半年因 Aster 等新进者竞争跌到 ~38–40%（第三方观察，区间随报告口径波动，evidence: [T02-S034]）；perp DEX 整体 2025 一度创 ~2tn 月量（evidence: [T02-S034]）。
- **不适合 / 替代**: 极致简单/零价格冲击的 retail 体验看 GMX(AMM 型)；最深合规法币通道仍是 CEX。
- **Decay risk**: medium（龙头地位 1 年内已被显著侵蚀，竞争烈度高 → 12-24 月格局可能再变）

### 15. GMX

- **One-liner**: AMM/流动性池型 perp DEX，瞬时流动性 + 简单界面，吸引 retail 散户永续流量。
- **Tier**: 场景特化（合约交易者 retail）
- **Maintainer / Owner**: GMX（https://gmx.io，evidence: [T02-S028]）
- **License**: proprietary 协议（有 GMX token）
- **典型使用场景**: 想要「点开就能开仓、无订单簿挂单门槛」的简单永续；接受用流动性池对手盘换简单性。
- **不适合 / 替代**: 深度/价格发现不如订单簿型(Hyperliquid/dYdX)，大单冲击大（evidence: [T02-S034]）。
- **Decay risk**: medium

### 16. dYdX (v4)

- **One-liner**: 订单簿型 perp DEX，v4 迁到独立 Cosmos 应用链，面向需要订单簿撮合的 pro 交易者。
- **Tier**: 场景特化（合约交易者 pro）
- **Maintainer / Owner**: dYdX（https://dydx.exchange，evidence: [T02-S029]）
- **License**: 部分开源（v4 开源链）
- **典型使用场景**: 习惯 CEX 式订单簿 + 想要去中心化撮合；与 Hyperliquid 同属「订单簿派」（evidence: [T02-S034]）。
- **不适合**: 流动性/份额已被 Hyperliquid 大幅拉开；新标的上线速度不及。
- **Decay risk**: medium

### 17. Jupiter

- **One-liner**: Solana DEX 聚合器，~95% Solana 聚合量份额，靠链速 + 路由几乎总能给 Solana 现货最优执行。
- **Tier**: 场景特化（链上 degen / Solana 现货）
- **Maintainer / Owner**: Jupiter（https://jup.ag，evidence: [T02-S012]）；JUP token
- **License**: proprietary（路由开放接入）
- **典型使用场景**: Solana 上任何现货/memecoin swap 的默认路由层；2024-08 上线 dynamic slippage 自动优化滑点对抗三明治（evidence: [T02-S035]）。
- **不适合 / 替代**: EVM 主网看 1inch/CoW Swap；Solana = Jupiter 几乎是定式（evidence: [T02-S036]）。
- **Decay risk**: medium（份额极高但绑定 Solana 周期）

### 18. 1inch

- **One-liner**: EVM DEX 聚合器，Pathfinder 算法把单笔拆到 200+ DEX 实时寻最优，~59% 以太坊聚合量份额。
- **Tier**: 场景特化（EVM 现货）
- **Maintainer / Owner**: 1inch（https://1inch.io，evidence: [T02-S013]）；1INCH token
- **License**: 部分开源
- **典型使用场景**: 以太坊/EVM 主网大单现货，靠拆单降滑点；2025 底加了 Solana 支持（evidence: [T02-S036]）。批量 CoW(coincidence-of-wants) 命中时 CoW Swap 可能更优。
- **不适合**: Solana 原生深度不及 Jupiter；单一聚合器不保证全场景最优价（自称 best-price >90% 但因 pair 而异，evidence: [T02-S036]）。
- **Decay risk**: low

### 19. Uniswap

- **One-liner**: 最大 EVM 现货 DEX，是聚合器背后的底层流动性源，也是直连现货执行的默认场所。
- **Tier**: 场景特化（EVM 现货底座）
- **Maintainer / Owner**: Uniswap Labs（https://app.uniswap.org，evidence: [T02-S014]）；UNI token
- **License**: 协议开源
- **典型使用场景**: 直接在最深 EVM 流动性池现货 swap；多数聚合器路由最终落到 Uniswap 池子。
- **不适合**: 单池直 swap 不一定比聚合器优价（大单要走 1inch 拆单）。
- **Decay risk**: low

### 20. GoPlus / De.Fi Scanner / RugCheck（合约安全扫描三件套）

- **One-liner**: 买新币前的 honeypot / 黑名单 / mint 权 / 买卖税 / rug 风险扫描——链上 degen 的「下单前最后一道闸」。
- **Tier**: 场景特化（链上 degen 必装）
- **Maintainer / Owner**: GoPlus Security（https://gopluslabs.io）、De.Fi（https://de.fi）、RugCheck（https://rugcheck.xyz）（evidence: [T02-S022, T02-S023, T02-S024]）
- **License**: GoPlus 开放、permissionless API（30+ 链，已被 Dexscreener/Sushi/Uniswap 内嵌，evidence: [T02-S022]）；De.Fi 闭源平台；RugCheck Solana 原生
- **典型使用场景**: GoPlus 做跨链合约级首过滤(honeypot+黑名单)；RugCheck 给 Solana token「红绿灯」+ insider 网络检测(beta)；De.Fi 出综合 rug 报告（流动性抽干/增发/慢撤等模式，evidence: [T02-S038]）。Token Sniffer 用模式匹配 + clone 检测 + honeypot 模拟出 0-100 分（evidence: [T02-S022]）。
- **不适合 / 替代**: 规则型扫描有漏报，新型/可升级合约能绕过；不能只看看板内嵌检查就下单。
- **Decay risk**: medium（攻防螺旋，规则要持续更新）

### 21. DeBank

- **One-liner**: EVM 多链钱包 portfolio 总览——一屏看清某地址所有链的持仓/LP/借贷/收益。
- **Tier**: 场景特化（价值长持 / 撸毛多钱包）
- **Maintainer / Owner**: DeBank（https://debank.com，evidence: [T02-S007]）；Rabby 同团队
- **License**: proprietary
- **典型使用场景**: 盘点自己跨链净值、跟踪某 smart wallet 持仓、撸毛时管理多个农场钱包。
- **不适合**: EVM 为主，Solana 持仓覆盖弱（看 Phantom/Step）。
- **Decay risk**: low

### 22. Glassnode / CryptoQuant（链上宏观指标）

- **One-liner**: 链上宏观/周期指标（HODL waves、交易所流入流出、SOPR、MVRV）——价值长持/宏观交易者读「市场处于周期哪一段」。
- **Tier**: 场景特化（价值长持 / 宏观）
- **Maintainer / Owner**: Glassnode（https://glassnode.com）、CryptoQuant（https://cryptoquant.com）（evidence: [T02-S042, T02-S041]）
- **License**: proprietary（部分免费指标；高级指标付费）
- **典型使用场景**: Glassnode 看长期持有者行为/链上估值；CryptoQuant 看交易所储备/矿工流出判断抛压（evidence: [T02-S042]）。
- **不适合**: 偏 BTC/ETH 宏观，对 memecoin/短线无用；与衍生品数据(Coinglass)互补非替代。
- **Decay risk**: low

---

## 新兴 / 实验层（近 12 月起势，stability: experimental，6 个月后可能不存在/被取代）

### 23. Axiom

- **One-liner**: 一体化链上交易终端——token 发现(Pulse 筛选) + 钱包追踪 + X 监控 + 快速执行 + MEV 设置 + 限价单 + Hyperliquid perp 接入，全塞进一个界面。
- **Tier**: 新兴
- **Maintainer / Owner**: Axiom（https://axiom.trade，evidence: [T02-S027]）
- **License**: proprietary
- **典型使用场景**: Solana memecoin 速攻 + 想在一个界面里完成发现→风控→执行→perp 对冲。
- **Maturity（带 caveat）**: 第三方横评称 Axiom 2025-07 占链上终端 ~73% 份额、日收入 ~16 万美元（第三方观察 + 交易所媒体口径，利益冲突，evidence: [T02-S037, T02-S044]）。
- **不适合 / 替代**: EVM 支持有限（主攻 Solana）；新平台跑路/被黑/份额骤变风险高。GMGN 分析层(AI 合约风险扫描)更强、更偏「追踪」用途（evidence: [T02-S037]）。
- **Decay risk**: high（terminal 赛道 6 个月换代，份额数字本身就是时效信号）

### 24. GMGN / Photon / BullX Neo（memecoin 终端三巨头）

- **One-liner**: 迭代极快的链上 memecoin 交易终端，主打新币发现 + 一键狙击 + smart money 跟单 + MEV 设置。
- **Tier**: 新兴
- **Maintainer / Owner**: GMGN（https://gmgn.ai）、Photon（https://photon-sol.tinyastro.io）、BullX Neo（neo.bullx.io）（evidence: [T02-S009, T02-S010, T02-S037]）
- **License**: proprietary
- **典型使用场景**: GMGN = 最强分析层(AI 合约风险扫描 + smart money)，多链(Sol/Base/ETH)，更偏「追踪/分析」；Photon = 轻量多链 + Solana Jito MEV，重速度/简洁；BullX Neo = token 发现强（evidence: [T02-S037]）。GMGN 日收入虽低于 Axiom 但用户量相近 → 说明多用于「追踪」而非「执行」（第三方观察，evidence: [T02-S037]）。
- **不适合 / 替代**: 终端均为闭源、要连/授权钱包，钓鱼仿冒站极多；不要在终端里关掉滑点/MEV 保护裸冲。
- **Decay risk**: high（这是全行业衰减最快的一类工具）

### 25. Jito MEV Protect / 私有 RPC（Solana 反三明治）

- **One-liner**: Solana 上把交易走私有 bundle、避开公共 mempool，防 memecoin 高滑点交易被三明治。
- **Tier**: 新兴（机制持续演进）
- **Maintainer / Owner**: Jito（https://solana.com/developers/guides/advanced/mev-protection，evidence: [T02-S030]）
- **License**: 基建（验证者/区块引擎）
- **典型使用场景**: memecoin 交易者设高滑点最易被三明治；付小费(~$0.04/笔)走 Jito 私有 bundle，对绝大多数交易降 MEV 暴露 90%+（evidence: [T02-S035, T02-S031]）。2025-03 Jito 关闭公共 mempool，掐掉最易得的抢跑嗅探源（evidence: [T02-S035]）。配 Jupiter dynamic slippage 一起用。
- **不适合 / 替代**: 防护非 100%，仍有 Astralane 等竞争方案；不替代「设合理滑点上限」这一最有效的基础防御（evidence: [T02-S035]）。
- **Decay risk**: high（MEV 攻防螺旋，机制/收费 6-12 月会变）

### 26. AI 交易 agent（链上自治协议）

- **One-liner**: 2025 新类目——不是传统 bot/chatbot，而是「持有自己 token、链上自主决策、价值绑定其表现」的自治协议；及给 AI 消费而非人用的交易 CLI/接口。
- **Tier**: 新兴（高度实验）
- **Maintainer / Owner**: 分散（多团队）；代表信号：Kraken 2025-11 开源 Rust CLI（134 个交易命令 + 内置 MCP + paper trading，首个为 AI 系统消费而非人设计的 CLI）；OKX OnchainOS（2026-03-10，覆盖 60+ 链/500+ DEX）；BingX AI Arena（2025-11，GPT/Claude/Gemini/Grok/DeepSeek 用 $1 万虚拟金实时比赛）。
- **License**: 各异（部分开源 CLI / proprietary 平台）
- **Maturity（带 caveat）**: 第三方称至 2026 Q1 AI agent 占加密投资兴趣 62%、市值 ~153 亿美元（第三方观察，泡沫色彩浓，需 caveat）。
- **不适合 / 替代**: 自治 agent 有 prompt injection/被操纵风险，已有 agent 被骗签恶意交易致真实损失的案例；不要把自托管私钥/大额交给早期 agent。
- **Decay risk**: high（类目极新，多数项目 6-12 月内会消失或重构）
- **来源（注）**: 本卡片主要来自第三方汇总搜索（含交易所媒体），无单一可点开的中立一手，整卡可信度 low，仅作「新兴信号存在」标注。

### 27. Token Terminal / Token Unlocks / RootData（基本面 + 解锁/募资数据）

- **One-liner**: Token Terminal = 协议「收入/PE 等财务基本面」；Token Unlocks = 代币解锁日历(供给冲击预警)；RootData = 项目募资/投资方数据。
- **Tier**: 新兴/补充（数据维度较新，渗透中）
- **Maintainer / Owner**: Token Terminal（https://tokenterminal.com）、Token Unlocks（https://token.unlocks.app）、RootData（evidence: [T02-S006, T02-S043]）
- **License**: proprietary（免费 + 付费档）
- **典型使用场景**: 长持/基本面派用 Token Terminal 看协议真实收入(vs DefiLlama TVL 可被夸大)；用 Token Unlocks 提前规避大额解锁前的抛压；用 RootData 查项目背后 VC/募资判断「庄家」结构。
- **不适合**: 财务指标在 token 经济不成熟的新协议上意义有限。
- **Decay risk**: medium

---

## 选型决策树

> 节点 7 个主分支（含子分支）。每节点可追溯到证据。

### 决策树 A：要不要自托管？（钱包层 — 一切的根）

#### Branch 1: 大额 / 长持，安全 > 便利
→ **推荐**: Ledger(硬件冷钱包) 持仓 + 必须开 **Clear Signing**，不盲签复杂交易（evidence: [T02-S018, T02-S019]）。
→ **理由 / 案例**: 2025-02 Bybit 14 亿被盗正是签名者在 Ledger 上盲签了被篡改的 Safe 合约——冷钱包不防你亲手签恶意交易，Clear Signing 才防（evidence: [T02-S019, T02-S033]）。
→ **不推荐**: 仅用 MetaMask/Phantom 热钱包存大额——钓鱼/drainer 头号目标，2025 H1 钓鱼损失 >4 亿（evidence: [T02-S017]）。

#### Branch 2: 高频链上交互 / degen，便利 > 极致安全
→ **推荐**: **Rabby**(EVM, 交易模拟拦恶意签名) 或 **Phantom**(Solana)，并定期用 **Revoke.cash** 清授权（evidence: [T02-S015, T02-S020]）。
→ **理由**: Rabby 签名前模拟「这笔实际改变什么」，是 MetaMask 没有的、能拦下大量恶意签名（evidence: [T02-S015]）。
→ **混合最佳实践**: 热钱包只放「交易仓」，主仓在冷钱包；热钱包定期 revoke 旧 approval（evidence: [T02-S032]）。

### 决策树 B：现货执行在哪？

#### Branch 3: 要法币出入金 / 合规 / 最深主流币流动性 → CEX
→ **推荐**: Binance/OKX/Bybit/Coinbase（CEX，托管，需 KYC）。
→ **不推荐**: 用 DEX 做大额主流币法币通道（链上无法币腿）。
→ **权衡**: CEX = 托管(交易所跑路/被黑/冻结风险) 换流动性与法币腿。

#### Branch 4: 自托管现货 swap → 选链
##### 4a. Solana / memecoin → **Jupiter**（~95% Solana 聚合量，几乎总最优 + dynamic slippage 防三明治）（evidence: [T02-S036, T02-S035]）
##### 4b. 以太坊 / EVM 大单 → **1inch**(Pathfinder 拆 200+ DEX) 或批量命中时 **CoW Swap**；底层直 swap 落 **Uniswap**（evidence: [T02-S036, T02-S014]）
→ 原则: 没有单一聚合器全场景最优，按链选（Solana=Jupiter / EVM=1inch/CoW）（evidence: [T02-S036]）。

### 决策树 C：永续合约去哪？

#### Branch 5: 接受托管/KYC，要最深流动性 → CEX 合约
→ 但若要自托管 perp，转 Branch 6。

#### Branch 6: 要自托管永续 → 看你要订单簿还是 AMM
##### 6a. 要订单簿 + 深流动性 + pro 体验 → **Hyperliquid**（2025 链上 perp 龙头，虽份额从 ~73% 跌到 ~40%，仍最大）（evidence: [T02-S011, T02-S034]）
##### 6b. 要极简「点开就开仓」/ retail → **GMX**(AMM 型，瞬时流动性)（evidence: [T02-S028, T02-S034]）
→ **配套**: 无论哪个，盯盘配 **Coinglass**(资金费率/OI/清算热力图) + **TradingView**（evidence: [T02-S005]）。

### 决策树 D：memecoin 用哪个终端？

#### Branch 7: 链上 memecoin 速攻
→ **执行 + 发现**: **Axiom**(一体化, 2025 份额最高但 high decay) 或 **Photon**(轻量+快+Jito MEV)（evidence: [T02-S027, T02-S010, T02-S037]）。
→ **追踪 + 风控分析**: **GMGN**(最强 AI 合约风险扫描 + smart money，多用于追踪而非执行)（evidence: [T02-S009, T02-S037]）。
→ **下单前强制**: 过一遍 **RugCheck/GoPlus**(honeypot/rug 扫描) + 开 **Jito MEV Protect** + 设合理滑点上限（evidence: [T02-S024, T02-S022, T02-S035]）。
→ **不推荐**: 直接在 Phantom 裸 swap 新币不扫合约、不设滑点上限——最易吃 honeypot + 三明治（evidence: [T02-S035]）。

---

## 避坑清单（≥ 5 条）

- ❌ **不要把热钱包当冷钱包存大额**：MetaMask/Phantom 是钓鱼/drainer 头号目标，假更新提示/假 airdrop 站骗你签名即盗私钥，2025 H1 钓鱼损失 >4 亿美元；大额/长持必须硬件冷钱包（evidence: [T02-S017, T02-S018]）。

- ❌ **不要盲签(blind signing)复杂交易**：Bybit 14 亿被盗的直接环节就是签名者在硬件钱包上盲签了被篡改的 Safe 合约调用——设备只显示 hash 无法解码。冷钱包不防你亲手签恶意交易，必须开 Clear Signing + 交易模拟（evidence: [T02-S019, T02-S033]）。

- ❌ **不要不扫合约就买新币**：honeypot 让你能买不能卖、可升级合约能后门增发/抽干流动性。下单前过 GoPlus/RugCheck/De.Fi，但也别只信看板内嵌的首过滤——规则型扫描有漏报（evidence: [T02-S022, T02-S038]）。

- ❌ **不要在 memecoin 交易里关掉滑点上限 / MEV 保护裸冲**：高滑点 + 公共 mempool = 被三明治套利的完美猎物；设合理滑点上限是最有效防御，再叠 Jito 私有 RPC / Jupiter dynamic slippage（evidence: [T02-S035, T02-S031]）。

- ❌ **不要把 DEX 当法币通道 / 把 CEX 当自托管**：链上 DEX 没有法币腿，法币出入金/合规走 CEX；但 CEX 是托管，「Not your keys, not your coins」——长持别全锁在交易所（evidence: [T02-S034, T02-S018]）。

- ❌ **不要把 vendor 标签/TVL 当客观真相**：Nansen 的 smart money 标签是私有启发式会误标；DefiLlama 的 TVL 会被激励/循环借贷夸大——交叉 Token Terminal 收入 + 多源核对（evidence: [T02-S001, T02-S004, T02-S006]）。

- ❌ **不要信付费榜单/返佣推广软文选终端**：「最佳 X 终端 2025」多为交易所/终端返佣软文(利益冲突)，份额/收入数字口径混乱；看终端按你流派的功能匹配选，份额数字一律当时效信号而非定论（evidence: [T02-S037]）。

- ❌ **不要为撸毛盲目多开钱包**：LayerZero/zkSync 起协议普遍上 Sybil 检测，分析钱包间关联后批量剔除农场地址；2024 起转向「质量参与」而非交易量堆砌（evidence: [T02-S039]）。

- ❌ **不要点搜索广告/社媒链接进钱包/终端官网**：假官网 + drainer kit 几次点击就能批量生成；务必从书签/可信聚合(CoinGecko 合约地址)进，核对官方域名（evidence: [T02-S017]）。

---

## Phase 2 提炼提示

**反复出现 ≥ 3 source 都强调的「工具选型原则」**（候选 playbook 规则）:
- **多源交叉，不信单一 vendor 读数**（Nansen 标签 / DefiLlama TVL 都需 caveat）(出现于: T02-S001 / T02-S004 / T02-S006 / T02-S037)。
- **签名层是安全根**：交易模拟(Rabby) + Clear Signing(Ledger) > 单纯冷热之分；冷钱包不防盲签 (出现于: T02-S015 / T02-S019 / T02-S033)。
- **没有全场景最优工具，按链/流派分叉选**（Solana=Jupiter / EVM=1inch；订单簿 perp=Hyperliquid / AMM perp=GMX）(出现于: T02-S036 / T02-S034)。
- **下单前风控是固定步骤**：扫合约 + 设滑点上限 + MEV 保护，三步缺一即裸奔 (出现于: T02-S022 / T02-S035 / T02-S038)。

**显著的工具流派分裂**（候选 智识谱系条目）:
- **托管(CEX) vs 自托管(DEX)**：CEX(Binance/OKX/Bybit) 给流动性+法币腿但你不持私钥 vs DEX(Uniswap/Jupiter/Hyperliquid) 自托管但需自管安全/MEV。这是本行最根本的流派分裂，决定整条工具链。
- **订单簿派 vs AMM 派（永续）**：Hyperliquid/dYdX(订单簿, pro, 深流动性+价格发现) vs GMX/Gains(AMM, retail, 瞬时流动性+简单)（evidence: [T02-S034]）。
- **链上分析派 vs CEX 撮合派**：一类人活在 Dune/Nansen/DefiLlama/Arkham 的链上数据里(智识=「链上是真相」)，一类人主要在 CEX + TradingView + Coinglass 衍生品数据里。
- **付费旗舰 vs 开放中立**：Nansen(付费, 私有标签护城河) vs Arkham(免费)/DefiLlama(开源中立)/Dune(自建)——「为标签付费 vs 自己查链上」的方法论分歧。

**反复点名喂心智模型的工具**（≥3 源点到的链上三件套）:
- Dune + Nansen + DefiLlama = 「真实资本流向」黄金三件套（evidence: T02-S004 等多源）；典型盯盘组合 = TradingView + CoinGecko + 一个链上(Dune) + 一个风险(Coinglass) + 一个基本面(DefiLlama)。

**新兴工具信号**:
- 当前活跃/上升新工具数: 5 类（Axiom / memecoin 终端三巨头 / Jito MEV 防护 / AI 交易 agent / 基本面数据）。
- 出现→主流速度估计: memecoin 终端 ~6 个月换一代（最快衰减）；perp DEX 龙头格局 ~12 个月一大变（Hyperliquid 73%→~40%）；AI agent 类目极新、泡沫重、6-12 月大概率重构。

**时效信号（最快衰减的工具，update 时优先刷）**:
1. memecoin 终端（GMGN/Photon/BullX/Axiom）—— Decay high，份额数字本身即过期信号。
2. perp DEX 份额格局（Hyperliquid vs Aster vs GMX/dYdX）—— 1 年内已剧变。
3. AI 交易 agent —— 类目 < 12 月，多数项目活不过 6 个月。
4. MEV 防护机制/收费（Jito 等）—— 攻防螺旋，机制频繁变。

**冷僻 / 信号薄弱（诚实边界）**:
- 必备层 13 个、证据充分 → **不冷僻**。
- 唯一信号薄弱点: AI 交易 agent 卡片缺中立一手（多为交易所媒体/第三方汇总），可信度 low，已标注。
- 数字 caveat: 份额/收入/TVL 数字多为「第三方观察 + 平台标称」，口径随报告波动，Phase 2 引用须保留日期 + caveat，不作精确定论。
- **利益冲突密度高**是本行工具栈特征（返佣软文/付费榜单/交易所自媒体），Phase 2 应在 mental_model 里把「识别工具相关的利益冲突」本身写成一条技能。
