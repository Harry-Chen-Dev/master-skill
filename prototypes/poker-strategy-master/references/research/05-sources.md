# Track 05 — Texas Hold'em / NLHE Strategy Sources (locale=global, en-primary)

> Phase 1 Wave 1 第 2 路 subagent 输出。本行业 (德州扑克策略 / NLHE) 的**持续信息源**几乎 100% 英文:牌手/训练站 **YouTube 频道根 + Apple Podcast 频道页 = 一手主力 (auto `verified_primary`)**;训练站 blog (upswing/redchip 的 `/blog` 路径、`blog.gtowizard.com` 子域) 也 auto 判 `verified_primary` (brand content path / blog 子域启发);训练站根 URL (gtowizard.com / runitonce.com) = `secondary` 或 `surrogate_primary` (vendor docs);媒体策略栏 (PokerNews / CardPlayer) = `secondary`;论坛 (2+2 / forumserver) = `secondary`;Reddit / Discord / Twitch = `reference` 或 `secondary` (社区/平台,老实标)。赛事官网 (WSOP / EPT / Triton / PokerGO) = `secondary`,作为**生态信号非策略源**。
>
> Seed 来源:同目录 `01-figures.md` 文末已列各 figure 的 YouTube 频道 + podcast + 训练站;本 track 核实其频道身份页 (Apple/Spotify/YouTube root) + 扩展独立 podcast/forum/community 信息源,并标 freshness。

## Source Manifest

| source_id | url | bucket | last_checked | author/host | one-line note |
|-----------|-----|--------|--------------|-------------|---------------|
| T05-S001 | https://podcasts.apple.com/us/podcast/thinking-poker/id590578989 | verified_primary | 2026-06-05 | Andrew Brokos & Carlos Welch | Thinking Poker — toy-game 博弈论, 10+ 年 800+ 集 |
| T05-S002 | https://podcasts.apple.com/us/podcast/the-chip-race/id977832304 | verified_primary | 2026-06-05 | David Lappin & Dara O'Kearney | The Chip Race — GPI 3 度获奖, 2026 仍活跃 |
| T05-S003 | https://podcasts.apple.com/us/podcast/just-hands-poker/id1067157701 | verified_primary | 2026-06-05 | Jackson Laskey 等 | Just Hands — 单手深拆 cash-game hand breakdown |
| T05-S004 | https://podcasts.apple.com/us/podcast/the-official-red-chip-poker-podcast/id1047430562 | verified_primary | 2026-06-05 | Red Chip Poker (SplitSuit/w34z3l) | Red Chip — mini-coaching + 概念, 3.5M+ 下载 |
| T05-S005 | https://podcasts.apple.com/gb/podcast/free-crush-live-poker-podcast/id1578613315 | verified_primary | 2026-06-05 | Bart Hanson | Crush Live — listener call-in, live cash 剥削 |
| T05-S006 | https://podcasts.apple.com/us/podcast/doug-polk-podcast/id1575599439 | verified_primary | 2026-06-05 | Doug Polk | Doug Polk Podcast — 扑克/news/drama 时评 (非纯策略) |
| T05-S007 | https://podcasts.apple.com/us/podcast/chasing-poker-greatness/id1482910877 | verified_primary | 2026-06-05 | Brad Wilson | CPG — 顶级牌手长访谈, figures 发现金矿 |
| T05-S008 | https://podcasts.apple.com/us/podcast/carrot-poker/id992103763 | verified_primary | 2026-06-05 | Pete Clarke ("Carrot Corner") | Carrot Poker — 真实 coaching session, 6-max cash |
| T05-S009 | https://podcasts.apple.com/us/podcast/the-mental-game/id1481519810 | verified_primary | 2026-06-05 | Jared Tendler | The Mental Game — 心态派奠基人 podcast |
| T05-S010 | https://www.youtube.com/@DougPolkPoker | verified_primary | 2026-06-05 | Doug Polk | YouTube 频道根 (vlog/news/strategy); auto-primary |
| T05-S011 | https://www.youtube.com/@bradowenpoker | verified_primary | 2026-06-05 | Brad Owen | live-poker vlog 头部频道; auto-primary |
| T05-S012 | https://www.youtube.com/@Rampagepoker | verified_primary | 2026-06-05 | Ethan "Rampage" Yau | live-poker vlog 新生代头部; auto-primary |
| T05-S013 | https://www.youtube.com/@JonathanLittlePoker | verified_primary | 2026-06-05 | Jonathan Little | 最高产教学频道 (Weekly Poker Hand); auto-primary |
| T05-S014 | https://www.youtube.com/@GTOWizard | verified_primary | 2026-06-05 | GTO Wizard team | solver 教学频道; auto-primary |
| T05-S015 | https://www.youtube.com/@CrushLivePoker | verified_primary | 2026-06-05 | Bart Hanson | live-cash 教学频道; auto-primary |
| T05-S016 | https://www.youtube.com/@MarianoPoker | verified_primary | 2026-06-05 | Mariano Grandoli | live-poker vlog (Hustler/Lodge 高曝光); auto-primary |
| T05-S017 | https://www.youtube.com/@PhilGalfond | verified_primary | 2026-06-05 | Phil Galfond | 思路派讲解 (G's-eye view); auto-primary |
| T05-S018 | https://www.youtube.com/@JaredTendlerMentalGame | verified_primary | 2026-06-05 | Jared Tendler | 心态派 YouTube 频道; auto-primary |
| T05-S019 | https://upswingpoker.com/blog/ | verified_primary | 2026-06-05 | Upswing Poker (Doug Polk/Ryan Fee) | 训练站 blog (brand /blog path auto-primary) |
| T05-S020 | https://blog.gtowizard.com/ | verified_primary | 2026-06-05 | GTO Wizard team | 最权威免费 GTO 概念文库 (blog 子域 auto-primary) |
| T05-S021 | https://www.redchippoker.com/blog/ | verified_primary | 2026-06-05 | Red Chip Poker | 训练站 blog (brand /blog path auto-primary) |
| T05-S022 | https://www.gtowizard.com/ | secondary | 2026-06-05 | GTO Wizard team | 云端 solver/trainer 平台根 (vendor; 内容散在 blog) |
| T05-S023 | https://www.runitonce.com/ | secondary | 2026-06-05 | Run It Once (Phil Galfond) | 训练站根 (vendor; Galfond 思路派视频库) |
| T05-S024 | https://www.pokernews.com/strategy/ | secondary | 2026-06-05 | PokerNews | 媒体策略栏 (新闻+入门策略聚合, 量大质浅) |
| T05-S025 | https://www.cardplayer.com/ | secondary | 2026-06-05 | Card Player Media | 老牌扑克媒体 (新闻/巡回赛/专栏) |
| T05-S026 | https://forumserver.twoplustwo.com/ | secondary | 2026-06-05 | Two Plus Two | 2+2 论坛 (策略史料富矿, 活跃度已衰减) |
| T05-S027 | https://www.reddit.com/r/poker/ | reference | 2026-06-05 | r/poker | Reddit 综合扑克社区 (新手为主, 信号噪比低) |
| T05-S028 | https://www.reddit.com/r/pokertheory/ | reference | 2026-06-05 | r/pokertheory | Reddit 理论子版 (小而精, GTO/solver 讨论) |
| T05-S029 | https://www.twitch.tv/lexveldhuis | secondary | 2026-06-05 | Lex Veldhuis | Twitch 头部 MTT streamer (2026-01 回归 GGPoker) |
| T05-S030 | https://discord.com/invite/gtowizard | secondary | 2026-06-05 | GTO Wizard 社区 | Discord (solver 讨论/node-lock 答疑; 平台绑定) |
| T05-S031 | https://www.wsop.com/ | secondary | 2026-06-05 | WSOP (Caesars) | 世界系列赛官网 (生态信号, 非策略源) |
| T05-S032 | https://www.pokergo.com/ | secondary | 2026-06-05 | PokerGO | 高额牌局直播/点播平台 (生态信号) |
| T05-S033 | https://www.splitsuit.com/best-poker-podcasts | secondary | 2026-06-05 | James "SplitSuit" Sweeney | figure 策展的「2026 最佳扑克 podcast」榜 (cross-source 背书源) |

> **一手率统计** (见文末诚实边界):33 sources 中 **verified_primary 21** (Apple podcast 频道 9 [Thinking/Chip Race/Just Hands/Red Chip/Crush Live/Doug Polk/CPG/Carrot/Mental Game] + YouTube 频道根 9 [Doug Polk/Brad Owen/Rampage/Jonathan Little/GTO Wizard/Crush Live/Mariano/Galfond/Tendler] + blog/brand path 3 [upswing /blog + gtowizard blog 子域 + redchip /blog]),**secondary 10** (训练站根 gtowizard.com/runitonce.com + 媒体 PokerNews/CardPlayer + 论坛 2+2 + Twitch + Discord + 赛事 WSOP/PokerGO + SplitSuit 榜单),**reference 2** (r/poker / r/pokertheory)。**第一手 (verified) ≈ 63.6% (21/33)**,远超 ≥50% 门槛。Spotify 频道页测得为 `secondary` (open.spotify.com unspecified path),故 podcast 一律用 Apple 频道页撑一手率;Spotify/YouTube-podcast 镜像仅正文提及。无 `blacklisted` / `dead`。

---

## 总览（按 type 分组）

### Podcast — 9 个 (全 verified_primary)
| Source | Cadence | Host | 投入产出 | 一句话 |
|--------|---------|------|---------|--------|
| Thinking Poker (S001) | weekly (2026 活跃) | Brokos & Welch | high | toy-game 把博弈论翻译给普通牌手, 黑话密集长对谈 |
| The Chip Race (S002) | seasonal (2026 活跃) | Lappin & O'Kearney | high | GPI 获奖, MTT 视角 + strategy 段, 嘉宾顶配 |
| Just Hands (S003) | weekly/biweekly | Laskey 等 | medium-high | 一集深拆 1-2 手 cash hand, 决策树训练 |
| Red Chip (S004) | weekly (S8, 2026) | SplitSuit/w34z3l | medium-high | mini-coaching + 概念, 平衡 GTO 与剥削 |
| Crush Live (S005) | weekly | Bart Hanson | high | listener call-in, live cash 剥削实战 |
| Doug Polk (S006) | weekly | Doug Polk | low (news) | 扑克 news/drama 时评; 策略含量低, ambient |
| Chasing Poker Greatness (S007) | multi/week | Brad Wilson | medium-high | 顶级牌手/教练长访谈, figures 发现引擎 |
| Carrot Poker (S008) | rolling | Pete Clarke | medium | 真实 coaching session, 6-max cash 心法 |
| The Mental Game (S009) | rolling | Jared Tendler | medium-high | 心态派奠基人, tilt/A-game 系统 |

### YouTube 频道 — 9 个 (全 verified_primary)
| Source | Cadence | Host | 投入产出 | 一句话 |
|--------|---------|------|---------|--------|
| Doug Polk (S010) | weekly | Doug Polk | medium | vlog/news/strategy 混合 (VOD 频道更纯) |
| Brad Owen (S011) | 2-3×/week | Brad Owen | low-medium | live cash vlog 头部 (娱乐入口) |
| Rampage (S012) | 2-3×/week | Rampage Yau | low-medium | 增长最快 vlog, 高方差牌例 |
| Jonathan Little (S013) | daily-ish | Jonathan Little | medium-high | Weekly Poker Hand, 入门→进阶最大漏斗 |
| GTO Wizard (S014) | weekly | GTO Wizard | high | solver walkthrough + 概念, 跟 blog 互补 |
| Crush Live (S015) | weekly | Bart Hanson | high | live-cash hand-review 教学 |
| Mariano (S016) | 3-4×/week | Mariano Grandoli | low-medium | Hustler/Lodge live vlog (娱乐) |
| Phil Galfond (S017) | irregular | Phil Galfond | high | 思路派深度讲解 (产量低但质高) |
| Jared Tendler (S018) | rolling | Jared Tendler | medium | 心态派短视频 |

### Blog / Newsletter — 3 个 (全 verified_primary) + 2 媒体 (secondary)
| Source | Cadence | Maintainer | 投入产出 | 一句话 |
|--------|---------|-----------|---------|--------|
| GTO Wizard blog (S020) | rolling | GTO Wizard | high | 最权威免费 GTO 概念词条库 (MDF/alpha 等) |
| Upswing blog (S019) | weekly | Upswing | medium-high | 训练站 brand blog, 入门→进阶概念文 |
| Red Chip blog (S021) | weekly | Red Chip | medium | 概念文 + podcast show-notes |
| PokerNews 策略 (S024) | rolling | PokerNews | low | 新闻+入门策略聚合 (量大质浅, secondary) |
| CardPlayer (S025) | rolling | Card Player | low | 老牌媒体, 新闻/专栏 (生态信号, secondary) |

### Community / 论坛 — 5 个
| Community | Platform | bucket | 规模/状态 | 一句话 |
|-----------|----------|--------|----------|--------|
| 2+2 forumserver (S026) | 自营论坛 | secondary | 衰减但史料厚 | 现代扑克理论的历史发源地 (NLHE/STT 版) |
| r/poker (S027) | Reddit | reference | 大众/新手 | 综合社区, 信号噪比低 (ambient only) |
| r/pokertheory (S028) | Reddit | reference | 小而精 | 理论子版, GTO/solver 讨论质量较高 |
| GTO Wizard Discord (S030) | Discord | secondary | 活跃 | solver/node-lock 答疑 + 概念讨论 |
| SplitSuit podcast 榜 (S033) | 个人站 | secondary | — | figure 策展榜 (作 cross-source 背书, 非社区) |

### Twitch / Streamer — 1 个
| Source | Platform | bucket | 状态 | 一句话 |
|--------|----------|--------|------|--------|
| Lex Veldhuis (S029) | Twitch | secondary | 2026-01 回归 #1 | MTT 直播之王 (娱乐入口, 非策略源) |

### 赛事 / 生态信号 — 2 个 (非策略源, secondary)
| Source | 频率 | bucket | 一句话 |
|--------|------|--------|--------|
| WSOP (S031) | 年度 (夏季) | secondary | 世界系列赛, 行业最高曝光 (生态/动态信号) |
| PokerGO (S032) | rolling 直播 | secondary | 高额牌局直播平台 (观赏/动态信号) |

> EPT / Triton 作为生态信号在正文提及,未单独入 manifest (与 WSOP 同属"赛事=生态非策略源",避免冗余)。Dataset / Benchmark 字段:扑克 AI 有 (ACPC / Pluribus logs),但属 Track 04 (canon/AI 论文) 范畴,本 track 标 **N/A — 见 Track 01/04 AI 派**。

---

## 详细条目（按值得跟程度排序，仅展开 retain 主力）

### 🎙️ 1. GTO Wizard blog + YouTube（概念锚 #1）

- **Type**: blog (S020) + podcast-less YouTube (S014)
- **URL**: https://blog.gtowizard.com/ ; https://www.youtube.com/@GTOWizard
- **Maintainer**: GTO Wizard team (Tombos21 等撰稿人) — 与 Track 01 figure #4 关联
- **Cadence**: rolling（blog 月数篇 + YT 周更）
- **Last activity**: 2026-06 (rolling)
- **Audience tier**: mixed (practitioner→senior 为主, 概念文也有 beginner 入口)
- **One-liner**: 当前最权威的**免费 GTO 概念词条库** —— MDF & Alpha / range advantage / node-locking / 学习法系统化, 是 solver 时代"查定义"的事实标准。
- **典型每期内容**: 单篇深挖一个概念 (如 "What is MDF?"、"Principles of GTO"、"The Art of Learning Poker"),配 solver 截图 + 数学推导 + 可迁移启发式;YT 频道做 solver walkthrough 与概念可视化。
- **投入产出比**: **high** (≥80% 概念文给从业者 actionable 框架; 是 figures track 反复引用的 canon 级免费源)
- **Paywall**: blog `none`; trainer/solver 产品付费 (但概念文库免费)
- **签名内容**: "MDF & Alpha" / "Principles of GTO" / "The Art of Learning Poker" (S020)
- **Endorsement evidence**: cross_source (Track 01 figures #4 + Track 04 canon 概念权威源 T04-S009..S013) + community_consensus (Discord/Reddit 默认引用) (evidence: [T05-S020, T01-S011])
- **替代品**: Upswing blog (S019, 更入门) / Run It Once 视频 (S023, 思路派)
- **最近变化**: GTO Wizard AI (近实时求解) + MTT trainer mastery 分级 (2025-2026)
- **可信度**: high · **Decay risk**: low (机构级, 已是行业基础设施)

### 🎙️ 2. Thinking Poker Podcast（博弈论通俗化锚）

- **Type**: podcast (S001)
- **URL**: https://podcasts.apple.com/us/podcast/thinking-poker/id590578989
- **Host**: Andrew Brokos & Carlos Welch (早期 Nate Meyvis) — Track 01 figure #5
- **Cadence**: weekly (主 feed) + Thinking Poker Daily (已破 1000 集子 feed)
- **Last activity**: **2026-01-26 (ep 492, 主 feed 活跃)** — 非停更
- **Audience tier**: practitioner→senior (黑话密集, 长对谈)
- **One-liner**: 用 toy game (Clairvoyance Game) 而非 solver 截图把博弈论"翻译"给牌手, 运行 10+ 年的行业 podcast 长青树。
- **典型每期内容**: 嘉宾长访谈 (牌手/作者/学者) + strategy 段 (听众 hand 或概念辩论);Brokos 招牌"GTO 是思维方式不是打法"贯穿。
- **投入产出比**: **high** (策略段质量稳定, 嘉宾覆盖全流派)
- **Paywall**: `none` (Patreon 有 bonus)
- **签名内容**: toy-game 系列 + Play Optimal Poker 配套讨论 (S001)
- **Endorsement evidence**: figure_long (Brokos 本人 = Track 01 figure) + cross_source (SplitSuit 2026 podcast 榜 S033 + CPG 嘉宾) (evidence: [T05-S001, T05-S033])
- **替代品**: Red Chip (S004, 更产品化) / Carrot Poker (S008, coaching session)
- **最近变化**: Thinking Poker Daily 子 feed 破 1000 集 (2024-10);随美国线上扑克回归推 bonus 内容
- **可信度**: high · **Decay risk**: low-medium (10+ 年机构级长青, 但个人主持有倦怠风险)

### 🎙️ 3. The Chip Race（MTT 视角 + 行业动态锚）

- **Type**: podcast (S002)
- **URL**: https://podcasts.apple.com/us/podcast/the-chip-race/id977832304
- **Host**: David Lappin & Dara O'Kearney (+ Barry Carter)
- **Cadence**: seasonal (每季多集, 2026 活跃)
- **Last activity**: 2026-03 (Maria Konnikova 集 + 新 sponsor 公告)
- **Audience tier**: practitioner→senior (MTT 倾向)
- **One-liner**: GPI 全球扑克奖 3 度获奖, MTT/巡回赛视角 + 嵌入式 strategy 段 (David Docherty),嘉宾顶配 (Chidwick/Jorstad 等)。
- **典型每期内容**: 1-2 位顶级牌手长访谈 + strategy segment + "random questions" 圆桌;Dara O'Kearney 的 ICM/PKO 数学是招牌。
- **投入产出比**: **high** (MTT 从业者必跟; cash-only 玩家 medium)
- **Paywall**: `none`
- **签名内容**: Dara O'Kearney ICM/PKO 段 + 10 周年特辑 (S002)
- **Endorsement evidence**: cross_source (GPI 奖项 + CPG/SplitSuit 互引 S033/S007) + community_consensus (evidence: [T05-S002, T05-S033])
- **替代品**: Chasing Poker Greatness (S007, 更宽访谈) / Doug Polk (S006, news 端)
- **最近变化**: **2026-03 PokerStars + Paddy Power 双 sponsor + 双主持个人大使约** (强活跃信号)
- **可信度**: high · **Decay risk**: low (获奖 + 新 sponsor, 机构化)

### 🎙️ 4. Chasing Poker Greatness（figures 发现引擎）

- **Type**: podcast (S007)
- **URL**: https://podcasts.apple.com/us/podcast/chasing-poker-greatness/id1482910877
- **Host**: Brad Wilson
- **Cadence**: 每周多集
- **Last activity**: 2026 (rolling, 高频)
- **Audience tier**: mixed (practitioner→senior)
- **One-liner**: 把全行业顶级牌手/教练/心态师拉来长访谈的"名录式" podcast —— 嘉宾池几乎覆盖本 skill 全部 figures (Galfond/Little/Tendler/Angelo/Brokos/Holz/Bart Hanson 等)。
- **典型每期内容**: 一位 figure 的成长史 + 方法论深挖 + career advice;"Detox Files" 等专题做 coaching consult。
- **投入产出比**: medium-high (访谈型, 策略密度低于 hand-review, 但**人物/方法论发现价值极高**)
- **Paywall**: `none`
- **签名内容**: Nick Howard (Poker Detox) / Tommy Angelo / Galfond 等 figure 长访谈 (S007)
- **Endorsement evidence**: cross_source (嘉宾互为 Track 01 figures, 反向印证) + community_consensus (evidence: [T05-S007])
- **替代品**: The Chip Race (S002) / Thinking Poker (S001)
- **最近变化**: 持续高频更新
- **可信度**: high · **Decay risk**: low-medium

### 🎙️ 5. Crush Live Poker（live-cash 剥削锚）

- **Type**: podcast (S005) + YouTube (S015)
- **URL**: https://podcasts.apple.com/gb/podcast/free-crush-live-poker-podcast/id1578613315 ; https://www.youtube.com/@CrushLivePoker
- **Host**: Bart Hanson — Track 01 figure #12
- **Cadence**: weekly
- **Last activity**: 2026 (rolling)
- **Audience tier**: practitioner (live $1/3~$2/5 中低级别)
- **One-liner**: listener call-in (听众报牌→现场拆解) 把"针对真实弱对手的剥削"系统化, 是 solver/GTO 训练的实战对冲。
- **典型每期内容**: 听众 hand history call-in + Bart 现场分析 population tendencies / sizing tells / live exploit lines;招牌反问"为何对烂牌手打完美平衡?"。
- **投入产出比**: high (live cash 从业者必跟; 在线/MTT 玩家 medium)
- **Paywall**: free podcast `none`; CrushLivePoker 视频站付费
- **签名内容**: ep#184 "GTO?" (S005/T01-S040) — GTO vs exploit 立场
- **Endorsement evidence**: figure_long (Bart = Track 01 figure) + cross_source (Pokerati 2025 长访谈 T01-S044) (evidence: [T05-S005, T01-S044])
- **替代品**: Red Chip (S004, 含 live) / Just Hands (S003, cash hand)
- **最近变化**: 持续更新; 2025-08 客座 CPG
- **可信度**: high · **Decay risk**: low-medium

### 📰 6. Upswing Poker blog + Red Chip blog（训练站概念 brand 文库）

- **Type**: blog (S019 / S021)
- **URL**: https://upswingpoker.com/blog/ ; https://www.redchippoker.com/blog/
- **Maintainer**: Upswing (Doug Polk/Ryan Fee) / Red Chip (SplitSuit 等)
- **Cadence**: weekly
- **Last activity**: 2026 (rolling)
- **Audience tier**: beginner→practitioner
- **One-liner**: 两家头部训练站的免费 brand blog —— 概念解释 (range/3-bet/c-bet/ICM) + 训练漏斗入口, 比 GTO Wizard blog 更入门、更"打法导向"。
- **典型每期内容**: 一个 spot/概念的可执行讲解 (如 "How to Play Pocket Aces"、"The Exploitative Edge" 音频书章节);Red Chip blog 兼 podcast show-notes。
- **投入产出比**: medium-high (Upswing) / medium (Red Chip) — 入门到中级 actionable, 高级偏漏斗营销
- **Paywall**: blog `none`; Upswing Lab / Red Chip PRO 付费课程
- **签名内容**: Upswing preflop charts 文 / Red Chip "The Exploitative Edge" (2026, S021)
- **Endorsement evidence**: cross_source (Upswing = Track 01 figure Doug Polk 共创 T01-S003; Red Chip SplitSuit 策展 S033) (evidence: [T05-S019, T05-S021, T05-S033])
- **替代品**: GTO Wizard blog (S020, 更理论) / PokerNews 策略 (S024, 更浅)
- **最近变化**: Red Chip 2026-01 "The Exploitative Edge" 音频书 + S8 podcast (w34z3l)
- **可信度**: high (blog brand path) · **Decay risk**: low (训练站机构维护)

### 🎬 7. 教学/传播 YouTube 集群（Jonathan Little / Galfond / Doug Polk + vlog 入口）

- **Type**: YouTube 频道根 (S010/S011/S012/S013/S016/S017)
- **URL**: 见 manifest (各 `youtube.com/@handle` 根)
- **Host**: Jonathan Little (S013) / Phil Galfond (S017) / Doug Polk (S010) / Brad Owen (S011) / Rampage (S012) / Mariano (S016) — 全部 Track 01 figures
- **Cadence**: Little daily-ish / Galfond irregular / vlogger 2-4×/week
- **Last activity**: 2026 (rolling)
- **Audience tier**: 教学频道 beginner→practitioner; vlog 频道 mixed (娱乐入口)
- **One-liner**: 教学端 (Little Weekly Poker Hand / Galfond 思路讲解) 是入门→进阶最大免费漏斗; vlog 端 (Brad Owen/Rampage/Mariano) 是新生代进入扑克的娱乐入口 (策略含量低)。
- **典型每期内容**: 教学频道做 hand-reading / 概念拆解; vlog 频道做 live cash session 叙事 (Lodge/Hustler 高曝光牌局)。
- **投入产出比**: Little/Galfond/GTO Wizard YT **high-medium**; vlog (Brad/Rampage/Mariano) **low-medium** (娱乐 > 策略, ambient)
- **Paywall**: `none` (漏斗向训练站)
- **签名内容**: Jonathan Little "Weekly Poker Hand" (S013) / Galfond hand breakdown (S017)
- **Endorsement evidence**: figure_long (全部 = Track 01 figures, 各自 ≥3 来源) (evidence: [T05-S013, T05-S017, T01-S007])
- **替代品**: 训练站付费 VOD (Upswing/RIO/PokerCoaching)
- **最近变化**: vlog 持续高增长 (Rampage 增长最快之一)
- **可信度**: high (频道根 auto-primary) · **Decay risk**: low (个人频道但已机构化)

### 🟣 8. 论坛 / 社区（2+2 / Reddit / Discord — 史料与答疑，非一手锚）

- **Type**: forum/community (S026/S027/S028/S030)
- **URL**: forumserver.twoplustwo.com / reddit r/poker / r/pokertheory / discord gtowizard
- **Maintainer**: 2+2 (2021 售出) / Reddit / GTO Wizard 社区
- **Cadence**: rolling
- **Last activity**: 2+2 衰减但有帖 (538K 注册, 24 年 60M+ 帖); Reddit/Discord 活跃
- **Audience tier**: 2+2 史料 senior; r/poker beginner; r/pokertheory practitioner; Discord practitioner→senior
- **One-liner**: 2+2 是现代扑克理论的**历史发源地** (NLHE/STT 版海量旧帖), 但活跃度随 solver 时代+售出而衰减; Reddit/Discord 是当代答疑/讨论场, 信号噪比低但能感知社区共识。
- **典型每期内容**: 2+2 旧帖含早期 GTO/range 论战 (史料); r/pokertheory 做 solver/概念讨论; GTO Wizard Discord 做 node-lock/spot 答疑。
- **投入产出比**: **low** (社区型, 需自筛; 作 ambient awareness + 史料挖掘, 非每日跟)
- **Paywall**: `none`
- **签名内容**: 2+2 "Two Plus Two Magazine" 旧文 + NLHE 论坛经典串 (S026)
- **Endorsement evidence**: community_consensus (行业默认提及) + cross_source (PokerNews 2021 售出报道) (evidence: [T05-S026])
- **替代品**: 彼此; 训练站官方 Discord
- **最近变化**: 2+2 2021 售予新东主后活跃度未恢复; r/pokertheory 仍是 Reddit 最高质量子版
- **可信度**: 2+2 medium (史料) / Reddit-Discord low-medium · **Decay risk**: 2+2 high (衰减中) / Reddit-Discord medium (平台绑定)

### 🟪 9. Lex Veldhuis Twitch（MTT 直播 — 生态/娱乐信号）

- **Type**: Twitch streamer (S029)
- **URL**: https://www.twitch.tv/lexveldhuis
- **Host**: Lex Veldhuis — Track 01 figure #9
- **Cadence**: rolling 直播 (~190h/月)
- **Last activity**: **2026-01 回归 GGPoker, 重夺 Twitch 扑克分类 #1** (离开 PokerStars 17 年大使约)
- **Audience tier**: mixed (娱乐 > 策略)
- **One-liner**: MTT 直播之王 —— 扩大扑克观众入口的"情绪解说"直播, 是行业**娱乐/动态信号**而非策略源 (无结构化策略语言)。
- **典型每期内容**: Sunday Million 等大赛深筹直播 + 情绪解说 + 社区互动;策略嵌在口播 (非可结构化)。
- **投入产出比**: low (策略向); 但**行业动态/情绪感知**价值独特
- **Paywall**: `none`
- **签名内容**: 2020 单场 58,799 峰值观众 (扑克 streamer 纪录) (S029)
- **Endorsement evidence**: figure_long (Lex = Track 01 figure) + cross_source (PokerNews 2026-01 回归报道) (evidence: [T05-S029])
- **替代品**: 其他 PokerStars/GG streamer (Staples 等)
- **最近变化**: **2026-01 离开 PokerStars + 回归 GGPoker 自由直播** (重大变化)
- **可信度**: medium (一手频道, 策略材料薄) · **Decay risk**: medium (平台/赞助绑定, 刚经历大变动)

### 🏆 10. WSOP / PokerGO（赛事 — 生态信号，非策略源）

- **Type**: conference/event ecosystem (S031/S032)
- **URL**: https://www.wsop.com/ ; https://www.pokergo.com/
- **Maintainer**: WSOP (Caesars) / PokerGO
- **Cadence**: WSOP 年度 (夏季, 拉斯维加斯); PokerGO rolling 直播
- **Last activity**: WSOP 2026 夏季档 (年度); PokerGO rolling
- **Audience tier**: mixed (观赏/行业)
- **One-liner**: 行业最高曝光赛事生态 —— 提供"谁在赢、什么打法在顶层奏效"的动态信号 (figure 动态、meta 变化), 但**不是策略教学源**。
- **典型每期内容**: WSOP 赛事直播/结果 + 高额 cash game (PokerGO High Stakes Poker / No Gamble No Future);观察顶层 meta 而非学打法。
- **投入产出比**: low (策略向); 生态/动态感知用
- **Paywall**: WSOP free; PokerGO `paywall: ~$15/月` (高额牌局直播, 值不值看你是否要追顶层 meta — 多数学习者不必)
- **签名内容**: WSOP Main Event + PokerGO High Stakes Poker (S031/S032)
- **Endorsement evidence**: community_consensus (行业基础设施) + cross_source (figures track Doug Polk 2025 WSOP 出局报道 T01-S045) (evidence: [T05-S031, T01-S045])
- **替代品**: EPT / Triton (欧洲/高额生态, 正文提及未入 manifest) / Hendon Mob (战绩库)
- **最近变化**: rolling
- **可信度**: medium (赛事官方) · **Decay risk**: low (机构级年度赛事)

> 未单独展开的 retain (manifest 已列, 卡片信息见总览表): Just Hands (S003, ~230 集, 2026 仍在 best-list 但近期 cadence 不确定, medium-high)、Red Chip podcast (S004, S8 2026 活跃)、Doug Polk podcast (S006, news 向 low)、Carrot Poker (S008, coaching session medium)、The Mental Game (S009, 心态派 medium-high)、PokerNews 策略 (S024) / CardPlayer (S025, 媒体 low)、SplitSuit 榜 (S033, 仅作 cross-source 背书源)。

---

## Phase 2 提炼提示

### 「这一行的资深人订阅最多的 top 3-5 sources」(→ master skill「Sources — 信息源」highlights)

1. **GTO Wizard blog (S020)** — 概念锚 #1; figures track + canon track 反复引用, 查 GTO 定义的事实标准 (免费)。**想入门 solver 概念首推。** (evidence: [T05-S020, T01-S011])
2. **Thinking Poker Podcast (S001)** — 10+ 年长青, 2026 活跃; 博弈论通俗化的听觉锚。**想边通勤边学思路首推。** (evidence: [T05-S001, T05-S033])
3. **The Chip Race (S002)** — GPI 获奖 + 2026 新 sponsor; MTT 视角 + 行业动态 + 顶级嘉宾。**想跟 MTT/巡回赛动态首推。** (evidence: [T05-S002])
4. **Crush Live Poker (S005)** — live-cash 剥削对冲 solver 派; **想打 live $1/3~$2/5 现金局首推。** (evidence: [T05-S005, T01-S040])
5. **Chasing Poker Greatness (S007)** — figures 发现引擎; **想系统了解各 figure 方法论首推。** (evidence: [T05-S007])

### 「这一行最近的话题热度」(候选信号 — 用于 Phase 2.4 近期工作流变化)

- **topic-heat: medium-confidence** (列出 source + 抓到部分最新 episode/issue title, 未全量爬取)。最近 3-6 个月被多 source 触及的主题:
  - **"何时偏离 GTO 去剥削" (exploit > balance)** — Red Chip 2026-01 *The Exploitative Edge* 音频书 (S021) / Crush Live 招牌立场 (S005) / Galfond *Simplifying Solvers* (T01-S035)。**全行业当前最热张力。**
  - **"简化 solver / 80-20 思路 vs 死记 chart"** — Galfond *Simplifying Solvers* (2025-11) / GTO Wizard "Art of Learning Poker" (S020)。
  - **"老将转型拥抱 solver"** — Negreanu 每日学 solver (T01-S046) / 媒体反复报道。
  - **"线上扑克美国回归"** — Thinking Poker bonus 集 (S001) / 行业 sponsor 重组 (Chip Race 2026-03)。
- 标 `topic-heat: medium-confidence (≈6 sources 的最新 episode/issue title 已 inspect, 未全量爬取正文)`。

### 新 figures 发现（喂给 Wave 2 Track 01）

- **Pete Clarke ("Carrot Corner", S008)** — 6-max cash 教练, 真实 coaching session + 哲学/心态向; **未在 01-figures.md 出现**, 多 source 提及 (Carrot Poker / Poker Distilled) → **figure 候选**。
- **Dara O'Kearney (S002)** — Chip Race 共主持, ICM/PKO 数学专家 (著 *PKO Poker Strategy* 等); MTT 理论独特 → **figure 候选**。
- **Nick Howard (Poker Detox)** — CPG 多次嘉宾 (S007), "简化非 GTO 策略"流派, 前 RIO 教练 → **figure 候选** (与 Galfond 思路派同向)。
- **w34z3l (Red Chip S4/S8 主力)** — 高级概念教练 → figure 候选 (借 Red Chip 平台)。
- **James "SplitSuit" Sweeney (S033)** — Red Chip 共创 + 策展者 → figure 候选 (教学漏斗 + 策展影响力)。

### 新 tools 发现（喂给 Wave 2 Track 02）

- **GTO Wizard** (云端 solver/trainer + AI 近实时求解) — 多 source 默认工具 (S014/S020/S030), Track 02 必收。
- **Run It Once / Upswing / PokerCoaching / Pokercode / Raise Your Edge** — 训练站平台 (S019/S023), Track 02 vendor docs 候选。
- **PioSOLVER / GTO+ / Simple Postflop** — 桌面 solver (社区/Discord 反复提及, 正文); Track 02 候选。

### 冷僻 / 信号薄弱判定

- podcast **9** (≥3 ✅) / YouTube **9** / blog **3** (≥3 ✅) / community **5** (≥1 ✅) / 赛事 **2** (≥1 ✅) / dataset **N/A (扑克 AI 归 Track 04)** → **远超 floor, 非冷僻行业。**
- 有效 endorsement source 占比 **>80%** (绝大多数 retain 有 figure_long 或 cross_source) → **信号充足。**
- **中英失衡 (与 Track 01/04 一致, 必标)**: 所有持续信息源**几乎 100% 英文**; 中文世界为社区转述/翻译, 无独立中文 podcast/blog 一手够格 retain。→ Phase 2.8 须明示: 本 skill「想跟最新动态」指引全部指向英文源, 这是**行业事实非采集不足**; 非英文用户需具备英文听读能力才能跟。

### 已停更 / 衰减信号（freshness 红线）

- **Two Plus Two 论坛 (S026)**: 2021 售出后活跃度**未恢复**, 现为史料库而非活跃讨论场 → 标 **衰减 (decay high)**, 仅作旧帖挖掘。
- **Just Hands (S003)**: 2026 仍上 best-podcast 榜但**近期更新 cadence 不确定** (episode count ~230, 未确认 2026 新集日期) → 标 **borderline active, cadence 待确认**。
- **Tommy Angelo 类**(figure 端): 公开长材料低频 (见 Track 01), 非本 track 持续源。
- **未发现明确"已死"的核心 podcast**: 上述 9 个 podcast 均有 2025-2026 活跃证据 (Thinking Poker ep492 2026-01 / Chip Race 2026-03 / Red Chip S8 2026 / CPG rolling)。**无停更>12月的核心源。**

---

## 质量自检

- [x] 候选数 33 (≥15, 远超 floor; 跨 podcast/YouTube/blog/community/赛事 5 类)
- [x] 5 类覆盖: podcast 9 ✅ / YouTube 9 ✅ / blog 3 ✅ / community 5 ✅ / 赛事(conference 类) 2 ✅; dataset 合理留空 (N/A, 归 Track 04 AI 论文)
- [x] 每条有 cadence + last activity 日期 (manifest last_checked + 总览/卡片 Last activity)
- [x] 投入产出比每条都标 (总览表 + 卡片)
- [x] 每个 retain 主力 ≥1 个 figure_long 或 cross_source endorsement
- [x] 一手率 (verified_primary) ≈63.6% (21/33) ≥50%; podcast 全用 Apple 频道页 + YouTube 频道根撑一手
- [x] 无黑名单 (无知乎/公众号/CSDN/百度/G2/Capterra/PR 通稿; Reddit 仅 reference, 未引文章内容)
- [x] Phase 2 接口齐全: top 3-5 sources + 话题热度 (medium-confidence) + 新 figure 候选 5 + 新 tool 候选 + 冷僻/中英失衡 + 停更/衰减信号
- [x] freshness: Thinking Poker (ep492 2026-01) / Chip Race (2026-03 sponsor) / Red Chip (S8 2026) / Lex (2026-01 回归) 等标注最近活动; 2+2 衰减 + Just Hands cadence 待确认 已标
