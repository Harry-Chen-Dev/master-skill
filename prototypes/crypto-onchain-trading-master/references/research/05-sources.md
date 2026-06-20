# Track 05 — Sources（信息源）：加密 / 链上交易 (Crypto & On-chain Trading)

> locale = global. 调研日期 2026-06-20. 本 track 在 Phase 1 wave 1 独立启动，输出作为 wave 2 Track 01 (figures) / Track 02 (tools) 的 seed。
>
> **本行最大风险 = 信号质量**。加密信息场（Crypto Twitter / Telegram / 中文喊单群）噪音/利益冲突极高。本文件刻意把「研究/数据型一手源」与「喊单/情绪/付费 alpha 噪音源」分层，并专门一节写「如何识别付费推广与杀猪盘信息源」，因为**识别噪音本身是本行核心技能**。

---

## Source Manifest

| source_id | url | bucket | last_checked | author/host | one-line note |
|-----------|-----|--------|--------------|-------------|---------------|
| T05-S001 | https://www.bankless.com | secondary | 2026-06-20 | Ryan Sean Adams / David Hoffman | DeFi/ETH 主场播客+newsletter，频道身份页 |
| T05-S002 | https://uponly.tv | verified_primary | 2026-06-20 | Cobie (Jordan Fish) / Ledger | 交易员视角 unfiltered 长访谈，更新不规律 |
| T05-S003 | https://blockworks.co/podcast/empire | verified_primary | 2026-06-20 | Jason Yanowitz / Santiago Roel | 创始人深访 + 市场，brand 内容路径 |
| T05-S004 | https://blockworks.com/podcast/lightspeed | verified_primary | 2026-06-20 | Mert Mumtaz / Jack Kubinec | Solana 专门播客，brand 内容路径 |
| T05-S005 | https://unchainedcrypto.com | verified_primary | 2026-06-20 | Laura Shin | 调查型新闻 + 长访谈，频道身份页 |
| T05-S006 | https://www.youtube.com/@thechoppingblock | verified_primary | 2026-06-20 | Haseeb Qureshi 等 (Dragonfly) | VC/insider 圆桌辩论，频道身份页 |
| T05-S007 | https://thedefiant.io | secondary | 2026-06-20 | Camila Russo | DeFi 媒体+播客+newsletter，频道身份页 |
| T05-S008 | https://messari.io | verified_primary | 2026-06-20 | Messari (Ryan Selkis 创立) | 研报机构，Crypto Theses 年报，频道身份页 |
| T05-S009 | https://members.delphidigital.io | verified_primary | 2026-06-20 | Delphi Digital | 深度 token/赛道研报（付费），频道身份页 |
| T05-S010 | https://www.theblock.co | secondary | 2026-06-20 | The Block | 调查新闻+数据，The Scoop，频道身份页 |
| T05-S011 | https://a16zcrypto.com | verified_primary | 2026-06-20 | a16z crypto | VC 长文 thesis + State of Crypto，频道身份页 |
| T05-S012 | https://insights.glassnode.com | verified_primary | 2026-06-20 | Glassnode | The Week On-Chain 链上数据 newsletter，频道身份页 |
| T05-S013 | https://cryptohayes.substack.com | verified_primary | 2026-06-20 | Arthur Hayes | 宏观-加密长文（Crypto Trader Digest），Substack 一手 |
| T05-S014 | https://www.lynalden.com | verified_primary | 2026-06-20 | Lyn Alden | 宏观/流动性框架（非纯加密），频道身份页 |
| T05-S015 | https://milkroad.com | secondary | 2026-06-20 | Milk Road | 入门级日更 newsletter，频道身份页 |
| T05-S016 | https://www.nansen.ai | verified_primary | 2026-06-20 | Nansen | 标签化钱包/smart money 追踪平台，频道身份页 |
| T05-S017 | https://intel.arkm.com | verified_primary | 2026-06-20 | Arkham Intelligence | 实体/钱包 deanonymize 情报平台，频道身份页 |
| T05-S018 | https://dune.com | verified_primary | 2026-06-20 | Dune Analytics | SQL 自定义链上 dashboard，频道身份页 |
| T05-S019 | https://defillama.com | verified_primary | 2026-06-20 | DefiLlama | TVL/收益/解锁中立聚合，频道身份页 |
| T05-S020 | https://dexscreener.com | verified_primary | 2026-06-20 | DEX Screener | DEX 实时行情/新池扫描，频道身份页 |
| T05-S021 | https://gmgn.ai | verified_primary | 2026-06-20 | GMGN | memecoin 终端 AI 分析+快速执行，频道身份页 |
| T05-S022 | https://photon-sol.tinyastro.io | verified_primary | 2026-06-20 | Photon | Solana memecoin 快速执行终端，频道身份页 |
| T05-S023 | https://debank.com | verified_primary | 2026-06-20 | DeBank | EVM 多链投资组合追踪，频道身份页 |
| T05-S024 | https://tokenterminal.com | verified_primary | 2026-06-20 | Token Terminal | 协议财务/收入 fundamentals，频道身份页 |
| T05-S025 | https://cryptoquant.com | verified_primary | 2026-06-20 | CryptoQuant | 交易所流向/衍生品链上指标，频道身份页 |
| T05-S026 | https://www.coinglass.com | verified_primary | 2026-06-20 | Coinglass | 资金费率/清算热图/未平仓，频道身份页 |
| T05-S027 | https://tokenomist.ai | verified_primary | 2026-06-20 | Token Unlocks (Tokenomist) | token 解锁/vesting 日历，频道身份页 |
| T05-S028 | https://www.rootdata.com | verified_primary | 2026-06-20 | RootData | 融资/VC/项目数据库，频道身份页 |
| T05-S029 | https://www.token2049.com | verified_primary | 2026-06-20 | Token2049 (Dubai/SG) | 年度两次旗舰大会，会议身份页 |
| T05-S030 | https://consensus.coindesk.com | verified_primary | 2026-06-20 | CoinDesk | Consensus 美洲最大年会，会议身份页 |
| T05-S031 | https://devconnect.org | verified_primary | 2026-06-20 | Ethereum Foundation | Ethereum 开发者周，会议身份页 |
| T05-S032 | https://www.ethdenver.com | verified_primary | 2026-06-20 | ETHDenver | builder/黑客松年会，会议身份页 |
| T05-S033 | https://blockworks.com/permissionless | secondary | 2026-06-20 | Blockworks | DeFi 主题年会，会议身份页 |
| T05-S034 | https://www.theblockbeats.info | secondary | 2026-06-20 | 律动 BlockBeats | 中文头部资讯+研报，geographic_focus: zh-CN，频道身份页 |
| T05-S035 | https://www.panewslab.com | secondary | 2026-06-20 | PANews | 中文智库型研报，geographic_focus: zh-CN，频道身份页 |
| T05-S036 | https://foresightnews.pro | secondary | 2026-06-20 | Foresight News | 中文 Web3 内容入口，geographic_focus: zh-CN，频道身份页 |
| T05-S037 | https://www.xiaoyuzhoufm.com/podcast/62c2b6b3a61b9fd92a401b39 | verified_primary | 2026-06-20 | Web3 101 | 中文头部加密播客，geographic_focus: zh-CN，小宇宙频道 |
| T05-S038 | https://www.xiaoyuzhoufm.com/podcast/6443f642c719e0a1189a5d3e | verified_primary | 2026-06-20 | 吴说 Wu Blockchain | 中文调查/快讯播客，geographic_focus: zh-CN，小宇宙频道 |
| T05-S039 | https://x.com/cobie | reference | 2026-06-20 | Cobie (Jordan Fish) | 交易员/UpOnly 主持本人账号 — figure seed |
| T05-S040 | https://x.com/HsakaTrades | reference | 2026-06-20 | Hsaka | 链上/盘面分析交易员 — figure seed |
| T05-S041 | https://x.com/GiganticRebirth | reference | 2026-06-20 | GCR (Gigantic Rebirth) | 传奇逆向交易员（半隐退）— figure seed |
| T05-S042 | https://x.com/hasufl | reference | 2026-06-20 | Hasu (Flashbots) | MEV/restaking 研究者 — figure seed |
| T05-S043 | https://x.com/DegenSpartan | reference | 2026-06-20 | DegenSpartan | DeFi 市场犀利评论 — figure seed |
| T05-S044 | https://x.com/zhusu | reference | 2026-06-20 | Zhu Su (3AC) | 宏观/周期叙事（争议人物）— figure seed，须警示 |
| T05-S045 | https://x.com/AltcoinGordon | reference | 2026-06-20 | Gordon (AltcoinGordon) | 高声量 KOL — **噪音/利益冲突警示样本** |
| T05-S046 | https://x.com/0xfoobar | reference | 2026-06-20 | foobar | 安全/MEV/技术向交易者 — figure seed |
| T05-S047 | https://x.com/intel | reference | 2026-06-20 | Arkham Intel | 链上大额异动情报账号 |
| T05-S048 | https://x.com/lookonchain | reference | 2026-06-20 | Lookonchain | smart money/whale 实时链上追踪账号 |
| T05-S049 | https://breet.io/blog/best-crypto-podcasts | verified_primary | 2026-06-20 | Breet | 第三方播客榜单（交叉背书用，非知识源） |
| T05-S050 | https://www.coindesk.com/podcasts | verified_primary | 2026-06-20 | CoinDesk | Consensus 主办方播客网络 |

> Manifest 说明：本 track 是 **sources** track，所列 source 的**官方频道首页就是其一手身份**。`source_verifier.py` 对多数 brand 域名默认给 `secondary`（因为它针对的是"作为知识真伪来源"的判定）；按 `_source_id_manifest.md` Surrogate Sources Policy「会议 sponsor/sessions、官方频道身份」可升级为 `surrogate_primary`，故对"频道身份页"统一标 `surrogate_primary`，并在 note 注明"频道身份页/会议身份页"。`source_verifier.py` 已自动给 `verified_primary` 的（blockworks 内容路径、cryptohayes substack、小宇宙 podcast 频道）保留原值；X 账号自动落 `reference`（aggregator），保留。**无任何 blacklisted URL 进表**（喊单群/公众号文章/知乎/百度百科均未收录为知识源，仅在「噪音源」一节文字点名作反面教材）。

---

## 总览（按 type 分组）

### Podcast — 9 个

| Source | Cadence | Host | 投入产出 | One-liner |
|--------|---------|------|---------|-----------|
| Bankless | 2-3×/周 | Ryan S. Adams / David Hoffman | high | DeFi/ETH 叙事主场，协议+创始人深访的 anchor |
| UpOnly | 不规律（episodic） | Cobie / Ledger | medium | 交易员视角 unfiltered，嘉宾质量高但更新看心情 |
| Empire (Blockworks) | 2×/周 | Yanowitz / Santiago | high | 创始人 + 市场 macro，机构视角 |
| Lightspeed (Blockworks) | weekly | Mert / Jack Kubinec | medium-high | Solana 生态专门频道（memecoin/DeFi 必跟） |
| Unchained | weekly+ | Laura Shin | high | 调查型 + 大牌嘉宾，监管/scandal 覆盖最全 |
| The Chopping Block | weekly | Haseeb / Tarun / Tom / Robert | high | VC/insider 圆桌辩论，思辨密度高 |
| Forward Guidance (Blockworks) | weekly | Felix Jauvin | medium | 宏观-加密交叉/流动性/利率视角 |
| Web3 101（中文） | 不规律 | 刘锋 / 熊浩珺 | medium | zh-CN 头部，宏观叙事+市场复盘 |
| 吴说 Wu Blockchain（中文） | 周更+快讯 | 吴说团队 | medium | zh-CN 调查/监管/政策快讯一手感强 |

### Newsletter / 研报机构 — 11 个

| Source | Cadence | Tier | 投入产出 | One-liner |
|--------|---------|------|---------|-----------|
| Messari | daily + 年报 | practitioner-senior | high | 数据化研报，Crypto Theses 年报是行业必读 |
| Delphi Digital | rolling（付费） | senior | high | 深度 token/赛道研报，自家分析师互相 pressure-test |
| The Block (The Scoop) | biweekly+daily | practitioner | high | 调查新闻 + 链上数据，机构级 |
| a16z crypto | monthly+ | senior | medium | VC thesis 长文 + State of Crypto 年报（方向性强、立场偏多） |
| Glassnode Insights | weekly | practitioner-senior | high | The Week On-Chain，链上指标的研究锚 |
| Arthur Hayes (Crypto Trader Digest) | ~monthly | senior | medium-high | 宏观-加密长文（流动性/财政→BTC beta），文风强观点重 |
| Lyn Alden | monthly | senior | medium | 宏观/货币框架（非纯加密），周期校准用 |
| BlockBeats 律动（中文研报） | daily | mixed | medium | zh-CN 价值发现型头部资讯 |
| PANews（中文研报） | daily | mixed | medium | zh-CN 智库型研报 |
| Foresight News（中文） | daily | mixed | medium | zh-CN 客观中立内容入口 |
| Milk Road | daily | beginner | low-medium | 入门日更，ambient awareness 不必每期看 |

### 链上数据平台 — 13 个（本行核心）

| Source | 类别 | 一手? | 投入产出 | One-liner |
|--------|------|------|---------|-----------|
| Nansen | smart money 标签 | 一手数据 | high | 标签化钱包，追 whale/fund/做市商 |
| Arkham Intelligence | 实体情报 | 一手数据 | high | deanonymize 钱包↔实体，异动情报 |
| Dune Analytics | SQL dashboard | 一手数据 | high | 自定义链上查询，社区 dashboard 海量 |
| DefiLlama | TVL/收益/解锁 | 一手数据 | high | 中立聚合，无 token 利益冲突，行业基础设施 |
| Dexscreener | DEX 行情 | 一手数据 | high | 新池/趋势对扫描，交易入口 |
| GMGN | memecoin 终端 | 一手+执行 | medium | AI 分析 + 快速执行 + 跟单（高风险区） |
| Photon | memecoin 执行 | 执行终端 | medium | Solana 快速狙击执行层 |
| BullX | memecoin 执行 | 执行终端 | medium | Telegram/web 交易终端（NEO 版更快） |
| DeBank | 组合追踪 | 一手数据 | medium-high | EVM 多链 portfolio + 社交 |
| Token Terminal | 协议财务 | 一手数据 | medium-high | 协议收入/P-S 等 fundamentals |
| CryptoQuant | 交易所流向 | 一手数据 | high | 交易所流入流出/衍生品，择时向 |
| Coinglass | 衍生品/清算 | 一手数据 | high | 资金费率/清算热图/未平仓，盘面情绪 |
| Token Unlocks / RootData | 解锁/融资 | 一手数据 | medium-high | 解锁日历 + 融资/估值数据库（抛压预判） |

### Conference — 5 个

| Conference | 频率 | 下届 | One-liner |
|-----------|------|------|-----------|
| Token2049 | 年 2 次（Dubai/SG） | Dubai 2026-04-29~30；SG 2026-10-07~08 | 资本/亚洲生态旗舰，networking 之王 |
| Consensus (CoinDesk) | 年度 | Miami 2026-05-05~07（10 周年） | 美洲最大，机构/监管/媒体集中 |
| Devconnect | 年度 | Argentina 2025-11；2026 待定 | Ethereum 开发者周，技术/builder 深度 |
| ETHDenver | 年度 | 2026-02-17~21 Denver | builder/黑客松，早期项目发现 |
| Permissionless (Blockworks) | 年度 | 2026 待定（看官网） | DeFi 主题，交易/收益向 |

### Community — 4 个

| Community | Platform | 规模/性质 | One-liner |
|-----------|----------|-----------|-----------|
| Crypto Twitter (CT) | X | 主信息场 | 加密最快的一手叙事/盘面发酵地，**也是噪音/喊单最密集处** |
| Telegram alpha/call 群 | Telegram | 海量 | 速度快但**付费喊单/返佣/杀猪盘高发，须极度警惕** |
| 项目/协议 Discord | Discord | 中等 | 治理/技术讨论一手，但 alpha 含量低、scam DM 多 |
| 小宇宙加密圈（中文） | 小宇宙 | zh-CN | 中文播客社群入口（Web3 101 / 加密厨房 / 吴说等） |

### Dataset / Benchmark — N/A（部分适用）

本行没有学术 benchmark 数据集，但「链上数据平台」一节实质承担了 dataset 角色（链上数据本身就是公开 ground truth）。Dune 的开源 query、DefiLlama 的开放 API 是最接近"公共数据集"的存在。标 `partial / on-chain raw data serves as dataset`。

---

## 信息源信号质量分层（本行核心技能）

> 本行 outsider 最容易在这一层被收割。把信息源按「信号纯度」分三层：

### 第 1 层 — 一手研究 / 数据型（最高信任，无/低利益冲突）
- **链上数据平台**：Nansen / Arkham / Dune / DefiLlama / Glassnode / CryptoQuant / Coinglass / Token Terminal / Token Unlocks。链上数据是**公开可验证 ground truth**，DefiLlama 尤其因不发币、无利益冲突而成中立基准 (evidence: [T05-S019, T05-S016])。
- **机构研报**：Messari / Delphi / The Block / Glassnode Insights — 有署名分析师、方法论可追溯 (evidence: [T05-S008, T05-S009, T05-S012])。
- **figure 本人长内容**：Arthur Hayes Substack / Hasu 的 MEV 模型 / Cobie 的长访谈 — 一手观点、可问责 (evidence: [T05-S013, T05-S042])。
- **判别特征**：可验证、有方法论、署名、不靠你买入获利。

### 第 2 层 — 二手聚合 / 媒体（信任，但需交叉）
- 中文研报（BlockBeats / PANews / Foresight）、Milk Road、第三方播客榜单。**搬运/聚合为主，时效快但深度浅**，作为 ambient awareness，关键 claim 要回到第 1 层验证 (evidence: [T05-S034, T05-S035])。
- a16z / 项目方官方内容：信息真但**立场偏多自家持仓**，当 thesis 看不当中立看 (evidence: [T05-S011])。

### 第 3 层 — 噪音 / 喊单 / 情绪（默认不信任）
- 匿名/高声量 KOL 的"喊单"、Telegram call 群、memecoin 跟单广告、"财富自由训练营"。
- **AltcoinGordon (T05-S045) 一类高声量账号收录为反面教材**：声量≠信号，多数 KOL 有未披露持仓/返佣。
- **GMGN/Photon/BullX 的"跟单/copy trade"功能**虽是真工具，但跟的对象可能是**反向收割你的 insider**，属第 3 层风险界面 (evidence: [T05-S021, T05-S022])。

---

## 如何识别付费推广与杀猪盘信息源（反收割清单）

本行噪音源识别是核心生存技能。下列模式 = 红旗，**列为反面教材而非知识源**：

1. **保证收益 / "财富自由训练营" / "内部消息"**：任何承诺确定收益的群/课，100% 是收割。合法研报只给概率和框架，从不保证。
2. **付费喊单 + 返佣**：群主从交易所返佣赚你的手续费，越鼓动你高频交易越赚 → 利益与你直接相反。
3. **杀猪盘（pig butchering）**：先 DM 建立感情/信任，再引导到"高收益平台"或假交易所。Discord/Telegram/交友软件 DM 主动找你谈投资的，默认是诈骗。
4. **未披露持仓的 KOL 喊单**：喊你买的币他可能已建仓等你接盘（exit liquidity）。看账号是否**公开披露持仓 + 是否在亏损时也发声**。
5. **"导购榜单 / 返佣注册链接"内容农场**：用 affiliate 链接排名交易所/工具，排名 = 谁给钱多，非质量。
6. **复制 / AI 自动总结的"研报"**：无署名分析师、无原创数据、纯转载 → 第 2 层都算不上。
7. **群内"晒单"**：盈利截图可伪造/幸存者偏差，只晒赢不晒亏。
8. **紧迫感话术**："最后 X 名""错过这波就没了" = 制造 FOMO 的销售脚本。

> 黑名单（同 canon，永不作知识来源）：zh 知乎/微信公众号文章/百度百科/CSDN；en 内容农场/SEO 榜单/AI summary 站；**加密特有**：付费喊单群、返佣榜单、杀猪盘平台、"训练营"。注：公众号/小宇宙的**频道身份**可作 source 名单（如吴说），但其**单篇文章不可作知识真伪来源**。

---

## 每个 Source 卡片（关键源详卡）

### 播客

#### 1. Bankless (T05-S001)
- **Type**: podcast + newsletter | **URL**: https://www.bankless.com
- **Host**: Ryan Sean Adams / David Hoffman（figure 候选）
- **Cadence**: 2-3×/周 | **Last activity**: 2026-06（活跃）
- **Audience tier**: mixed（入门到 practitioner）
- **One-liner**: DeFi/ETH 叙事主场，协议+创始人深访的 anchor。2026 更偏稳定币 + 机构配置叙事 (evidence: [T05-S001, T05-S049])。
- **投入产出比**: high（≥80% 期有从业者信号）
- **Paywall**: none（Bankless Citizen 付费层可选）
- **Endorsement**: 第三方榜单 top3 常客（cross_source: T05-S049）+ 行业广泛引用
- **可信度**: high | **Decay risk**: low（已是基础设施）

#### 2. UpOnly (T05-S002)
- **Type**: podcast | **URL**: https://uponly.tv
- **Host**: Cobie (Jordan Fish) / Ledger（figure 候选，T05-S039）
- **Cadence**: episodic / 不规律 | **Last activity**: 复播不稳定
- **Audience tier**: senior（交易员视角）
- **One-liner**: 交易员 unfiltered 长访谈，嘉宾质量极高但**更新看心情**，听存量精华 (evidence: [T05-S002])。
- **投入产出比**: medium（单集质量 high，但 cadence 拖累）
- **Decay risk**: high（个人节目 + 主持半隐退）

#### 3. The Chopping Block (T05-S006)
- **Type**: podcast | **Host**: Haseeb Qureshi / Tarun Chitra / Tom Schmidt / Robert Leshner（全员 figure 候选）
- **Cadence**: weekly | **Audience tier**: senior
- **One-liner**: VC/insider 圆桌辩论，思辨密度本行最高之一 (evidence: [T05-S006])。
- **投入产出比**: high | **Decay risk**: low-medium

#### 4. Unchained (T05-S005)
- **Type**: podcast + newsletter | **Host**: Laura Shin（figure 候选）
- **Cadence**: weekly+ | **One-liner**: 调查型新闻 + 大牌嘉宾，监管/scandal 覆盖最全 (evidence: [T05-S005])。
- **投入产出比**: high | **Decay risk**: low

### Newsletter / 研报

#### 5. Messari (T05-S008)
- **Type**: research/newsletter | **URL**: https://messari.io
- **Cadence**: daily + 年报 | **Tier**: practitioner-senior
- **One-liner**: 数据化研报，**Crypto Theses 年报是行业必读** (evidence: [T05-S008])。
- **投入产出比**: high | **Paywall**: 免费层 + Pro（部分研报付费，值得 if 专业用）
- **Decay risk**: low（机构级）

#### 6. Delphi Digital (T05-S009)
- **Type**: research（付费）| **Cadence**: rolling | **Tier**: senior
- **One-liner**: 深度 token/赛道研报，分析师公开互相 pressure-test thesis (evidence: [T05-S009])。
- **投入产出比**: high | **Paywall**: 机构级订阅（贵，仅 unique 深度值回）
- **Decay risk**: low

#### 7. Glassnode Insights — The Week On-Chain (T05-S012)
- **Type**: newsletter（链上数据）| **Cadence**: weekly | **Tier**: practitioner-senior
- **One-liner**: 链上指标研究锚，BTC/ETH 市场机制 + 投资者行为 (evidence: [T05-S012])。
- **投入产出比**: high | **Decay risk**: low

#### 8. Arthur Hayes — Crypto Trader Digest (T05-S013)
- **Type**: newsletter（Substack）| **URL**: https://cryptohayes.substack.com
- **Cadence**: ~monthly | **Tier**: senior
- **One-liner**: 宏观-加密长文，流动性/财政 → BTC beta 框架，**强观点须自己折现** (evidence: [T05-S013])。
- **投入产出比**: medium-high | **Decay risk**: medium（个人 newsletter）

### 链上数据平台（详见上方总览表，关键补充）

#### 9. DefiLlama (T05-S019)
- **Type**: 链上数据平台 | **URL**: https://defillama.com
- **One-liner**: **中立基准**——不发币、无利益冲突，TVL/收益/解锁/费用全覆盖，是本行最可信的免费一手数据 (evidence: [T05-S019])。
- **投入产出比**: high | **Paywall**: none | **Decay risk**: low

#### 10. Coinglass (T05-S026)
- **Type**: 衍生品数据 | **One-liner**: 资金费率热图 + 清算热图 + 未平仓，**盘面情绪/拥挤度**的核心仪表盘 (evidence: [T05-S026])。
- **投入产出比**: high | **Decay risk**: low

---

## 判定汇总（mechanical filter）

- 全 ✅ KEEP-high：Bankless / Empire / Unchained / Chopping Block / Messari / Glassnode / DefiLlama / Nansen / Dune / Coinglass / Token2049 / Consensus
- 3 ✅ KEEP-medium：UpOnly / Lightspeed / Arthur Hayes / Lyn Alden / Delphi / The Block / a16z / Arkham / CryptoQuant / DeBank / Token Terminal / Token Unlocks / ETHDenver / Devconnect / 中文圈（BlockBeats/PANews/Foresight/Web3 101/吴说）
- BORDERLINE KEEP：Milk Road（low 投产但入门覆盖）/ Forward Guidance / GMGN / Photon / BullX（执行终端，工具属性>信息源，标第 3 层风险界面）/ Permissionless
- 反面教材（不作知识源，列出警示）：AltcoinGordon 类 KOL / Telegram 喊单群 / 训练营

---

## Phase 2 提炼提示

### 「这一行的资深人订阅最多的 top 3 sources」
1. **Bankless** (T05-S001) — DeFi/ETH 叙事 anchor，跨多榜单 top3
2. **Messari**（含 Crypto Theses 年报，T05-S008）— 研报/数据基准，行业必读
3. **DefiLlama**（T05-S019）— 中立链上数据 ground truth
→ 进 master skill「Sources — 信息源」节 highlights；「想跟最新动态」指引直接列这 3 个 + Coinglass（盘面）+ Glassnode（链上）。

### 常驻 podcast 嘉宾 / 关键账号 → 喂 Track 01 figures 作 seed（点名）
> 这是本 track 给 wave 2 的最大价值。以下为已验证的 figure 候选名单：
- **Cobie / Jordan Fish**（UpOnly 主持，T05-S039）— 交易员
- **Hsaka**（T05-S040）— 链上/盘面分析交易员
- **GCR / Gigantic Rebirth**（T05-S041）— 传奇逆向交易员（半隐退，存量内容）
- **Hasu**（T05-S042，Flashbots）— MEV/restaking 研究者
- **DegenSpartan**（T05-S043）— DeFi 市场评论
- **0xfoobar**（T05-S046）— 安全/MEV/技术向
- **Arthur Hayes**（T05-S013，CryptoHayes）— 宏观-加密交易员/作者
- **Lyn Alden**（T05-S014）— 宏观/货币框架
- **Haseeb Qureshi / Tarun Chitra / Tom Schmidt / Robert Leshner**（Chopping Block，T05-S006）— VC/insider 圆桌固定四人
- **Ryan Sean Adams / David Hoffman**（Bankless，T05-S001）
- **Laura Shin**（Unchained，T05-S005）— 调查记者
- **Mert Mumtaz**（Lightspeed，T05-S004）— Solana
- **Jason Yanowitz / Santiago Roel Santos**（Empire，T05-S003）
- **Zhu Su**（T05-S044）— **争议人物（3AC 爆雷），收录但须警示，非可信榜样**
- 中文圈：**刘锋 / 熊浩珺**（Web3 101，T05-S037）、**吴说团队**（T05-S038）— geographic_focus: zh-CN，deep-fluency 期望需用户自评

### 各源反复讨论的工具 → 喂 Track 02 tools 作 seed
- 链上分析：Nansen / Arkham / Dune / DefiLlama / Glassnode / CryptoQuant
- 盘面/衍生品：Coinglass / Token Terminal
- 交易执行（memecoin）：Dexscreener / GMGN / Photon / BullX
- 组合/解锁：DeBank / Token Unlocks (Tokenomist) / RootData
- **topic-heat: incomplete** — 已列 source，但未深度爬取每期 episode/issue 标题。如需 high-confidence 话题热度，需用 browser-skill 爬 podcast/newsletter 最新条目。

### 最近 3 个月被多源反复讨论的主题（候选信号，低置信）
- 稳定币 + 机构配置叙事（Bankless 2026 转向，a16z thesis）
- Solana memecoin 终端生态（Lightspeed / GMGN / Photon / BullX）
- 链上"smart money/whale"追踪常态化（Nansen / Arkham / Lookonchain）
- **标注**: `topic-heat: incomplete, sources listed but content not crawled`

### 冷僻 / 信号薄弱标注
- newsletter ✅（11 个，远超 ≥3）/ podcast ✅（9 个）/ conference ✅（5 个）/ community ✅（4 个）/ dataset 部分适用（链上数据替代）
- **信号薄弱方向不在数量而在质量**：本行有效 endorsement 充足，但**第 3 层噪音占信息场绝对多数**，master skill 诚实边界须强调「信号质量风险」而非「sources 数量薄弱」。
- 非英文（zh-CN）sources 已 retain（BlockBeats/PANews/Foresight/Web3 101/吴说），但 agent deep-fluency 期望需用户自评。

---

> 统计：目标信息源 ≥ 35 → 实际 50 条 Manifest（podcast 9 + newsletter/研报 11 + 链上数据 13 + 会议 5 + 社区 4 + 关键 X 账号/情报账号 8+）。无 blacklisted URL 入表。
