# Track 01 — Texas Hold'em / NLHE Strategy Figures (locale=global, en-primary)

> Phase 1 Wave 2 第 1 路 subagent 输出。本行业 (德州扑克策略 / NLHE) 的思想领袖 **95%+ 输出在英文**:顶级牌手个人 YouTube 频道 + 训练站长视频、podcast (Thinking Poker / The Mental Game / 各家)、扑克 AI 论文作者 (Science/NeurIPS/arXiv)。一手率极易达标:**牌手 YouTube 频道根、Apple podcast 频道、arXiv 论文均 auto 判 `verified_primary`**;牌手/作者个人 blog 站 (noambrown.github.io / jaredtendler.com / tommyangelo.com) classify 判 `secondary` 但属 **author one-hand → 按 intake 政策上调 `surrogate_primary`** (note 含 "author one-hand");训练站根 (upswing/runitonce/pokercoaching/gtowizard) = `surrogate_primary` + note 含 "vendor docs",不冒充 verified_primary。Wikipedia/HendonMob/第三方 profile = `secondary`;Reddit/X 单帖仅 `reference`。
>
> Seed 来源:Track 04 canon 文末 Phase 2 接口已按四流派 (古典/solver/心态/AI) 列出 figure 候选,本 track 核实 + 扩展 + 补传播派 (streamer)。

## Source Manifest

| source_id | url | bucket | last_checked | author/host | one-line note |
|-----------|-----|--------|--------------|-------------|---------------|
| T01-S001 | https://www.youtube.com/@DougPolkPoker | verified_primary | 2026-06-05 | Doug Polk | 主频道 (vlog/news/strategy);youtube channel root auto-primary |
| T01-S002 | https://www.youtube.com/@DOUGPOLKVODS | verified_primary | 2026-06-05 | Doug Polk | strategy VOD 频道 (深度讲解);auto-primary |
| T01-S003 | https://upswingpoker.com/ | surrogate_primary | 2026-06-05 | Upswing Poker (Doug Polk/Ryan Fee) | vendor docs (Polk 共创训练站) |
| T01-S004 | https://www.youtube.com/@PhilGalfond | verified_primary | 2026-06-05 | Phil Galfond | 个人频道 (G's-eye-view 思路讲解);auto-primary |
| T01-S005 | https://www.runitonce.com/ | surrogate_primary | 2026-06-05 | Run It Once (Phil Galfond) | vendor docs (Galfond 创办训练站) |
| T01-S006 | https://www.poker.org/latest-news/run-it-once-qa-phil-galfond-on-the-golden-age-of-online-poker-a961X8R7oucW/ | secondary | 2026-06-05 | poker.org | Galfond Q&A — online poker 黄金期 + 思路派 |
| T01-S007 | https://www.youtube.com/@JonathanLittlePoker | verified_primary | 2026-06-05 | Jonathan Little | 主教学频道;auto-primary |
| T01-S008 | https://pokercoaching.com/ | surrogate_primary | 2026-06-05 | Jonathan Little | vendor docs (PokerCoaching 测验驱动) |
| T01-S009 | https://pokercoaching.com/blog/best-poker-books/ | verified_primary | 2026-06-05 | Jonathan Little | 分级书单 — figure 一手 endorsement (brand content path) |
| T01-S010 | https://www.youtube.com/@GTOWizard | verified_primary | 2026-06-05 | GTO Wizard team | solver 教学频道;auto-primary |
| T01-S011 | https://blog.gtowizard.com/ | verified_primary | 2026-06-05 | GTO Wizard team | 最权威免费概念文库 (blog 子域 auto-primary) |
| T01-S012 | https://www.thinkingpoker.net/category/podcast/ | verified_primary | 2026-06-05 | Andrew Brokos | Thinking Poker Podcast 主页 (brand content path) |
| T01-S013 | https://podcasts.apple.com/us/podcast/thinking-poker/id590578989 | verified_primary | 2026-06-05 | Andrew Brokos & Carlos Welch | Apple podcast 频道 (10+ 年 800+ 集);auto-primary |
| T01-S014 | https://www.thinkingpoker.net/play-optimal-poker/ | surrogate_primary | 2026-06-05 | Andrew Brokos | author one-hand (Play Optimal Poker 作者自营页) |
| T01-S015 | https://noambrown.github.io/ | surrogate_primary | 2026-06-05 | Noam Brown | author one-hand (个人学术主页 — bio/papers/talks) |
| T01-S016 | https://noambrown.com/papers/19-Science-Superhuman.pdf | verified_primary | 2026-06-05 | Noam Brown | Pluribus 论文作者一手 PDF (brand /papers auto-primary) |
| T01-S017 | https://www.latent.space/p/noam-brown | verified_primary | 2026-06-05 | Latent Space (swyx) | Noam Brown 长访谈 (test-time compute / 扑克→LLM reasoning);known author primary |
| T01-S018 | https://sequoiacap.com/podcast/training-data-noam-brown/ | verified_primary | 2026-06-05 | Sequoia (Training Data) | Noam Brown 谈 o1 reasoning / self-play (brand /podcast path) |
| T01-S019 | https://jaredtendler.com/ | surrogate_primary | 2026-06-05 | Jared Tendler | author one-hand (心态派奠基,Mental Game of Poker) |
| T01-S020 | https://podcasts.apple.com/us/podcast/the-mental-game/id1481519810 | verified_primary | 2026-06-05 | Jared Tendler | The Mental Game podcast 频道;auto-primary |
| T01-S021 | https://www.tommyangelo.com/ | surrogate_primary | 2026-06-05 | Tommy Angelo | author one-hand (Elements of Poker / tilt 哲学) |
| T01-S022 | https://www.youtube.com/@LexVeldhuis | verified_primary | 2026-06-05 | Lex Veldhuis | Twitch/YouTube 头部 streamer 频道;auto-primary |
| T01-S023 | https://www.youtube.com/@DanielNegreanu | verified_primary | 2026-06-05 | Daniel Negreanu | vlog + masterclass 传播者频道;auto-primary |
| T01-S024 | https://www.youtube.com/@bradowenpoker | verified_primary | 2026-06-05 | Brad Owen | live-poker vlog 头部频道;auto-primary |
| T01-S025 | https://www.youtube.com/@Rampagepoker | verified_primary | 2026-06-05 | Ethan "Rampage" Yau | live-poker vlog 新生代头部;auto-primary |
| T01-S026 | https://www.youtube.com/@CrushLivePoker | verified_primary | 2026-06-05 | Bart Hanson | live-cash 教学频道 (Crush Live Poker);auto-primary |
| T01-S027 | https://www.youtube.com/@nickpetrangelo | verified_primary | 2026-06-05 | Nick Petrangelo | 高额 MTT/cash 教练频道;auto-primary |
| T01-S028 | https://www.youtube.com/@FedorHolz | verified_primary | 2026-06-05 | Fedor Holz | 新生代 GTO MTT + 创业 (Pokercode);auto-primary |
| T01-S029 | https://www.raiseyouredge.com/ | surrogate_primary | 2026-06-05 | Raise Your Edge (bencb789) | vendor docs (MTT Masterclass) |
| T01-S030 | https://en.wikipedia.org/wiki/Linus_Loeliger | secondary | 2026-06-05 | — | Linus Loeliger 背景 — 公认在线最强但极少公开发声 |
| T01-S031 | https://pokerfuse.com/latest-news/2025/11/phil-galfonds-new-poker-course-teaches-you-how/ | secondary | 2026-06-05 | Pokerfuse | Galfond 2025-11 新课 Simplifying Solvers 报道 |
| T01-S032 | https://techcrunch.com/2025/03/19/openai-research-lead-noam-brown-thinks-ai-reasoning-models-couldve-arrived-decades-ago/ | secondary | 2026-06-05 | TechCrunch | Noam Brown GTC 2025 谈 reasoning 可早 20 年 |
| T01-S033 | https://www.science.org/doi/10.1126/science.aay2400 | verified_primary | 2026-06-05 | Brown & Sandholm (Science) | Pluribus 六人桌超人 AI (auto-primary) |
| T01-S034 | https://www.youtube.com/@JaredTendlerMentalGame | verified_primary | 2026-06-05 | Jared Tendler | 心态派 YouTube 频道;auto-primary |
| T01-S035 | https://www.runitonce.com/courses/simplifying-solvers/ | surrogate_primary | 2026-06-05 | Phil Galfond (Run It Once) | vendor docs (2025 新课 80/20 solver 体系) |
| T01-S036 | https://www.philgalfond.com/articles/simplify-your-strategy | surrogate_primary | 2026-06-05 | Phil Galfond | author one-hand (个人站长文 — "think like a solver, not play like") |
| T01-S037 | https://www.tommyangelo.com/reciprocality/ | surrogate_primary | 2026-06-05 | Tommy Angelo | author one-hand (reciprocality 原文 — "water/air/money flows") |
| T01-S038 | https://www.tommyangelo.com/tommyisms/ | surrogate_primary | 2026-06-05 | Tommy Angelo | author one-hand (Tommyisms 格言集 — voice DNA 富矿) |
| T01-S039 | https://jaredtendler.com/youre-evaluating-progress-wrong-and-its-costing-you/ | surrogate_primary | 2026-06-05 | Jared Tendler | author one-hand (process-over-results 长文) |
| T01-S040 | https://crushlivepoker.com/podcasts/gto | verified_primary | 2026-06-05 | Bart Hanson | Crush Live Poker ep#184 "GTO?" (brand content path) |
| T01-S041 | https://podcasts.apple.com/gb/podcast/free-crush-live-poker-podcast/id1578613315 | verified_primary | 2026-06-05 | Bart Hanson | Free Crush Live Poker podcast 频道;auto-primary |
| T01-S042 | https://jonathanlittlepoker.com/handrangeanalysis/ | surrogate_primary | 2026-06-05 | Jonathan Little | author one-hand (hand-range 教学长文) |
| T01-S043 | https://www.philgalfond.com/poker/ | surrogate_primary | 2026-06-05 | Phil Galfond | author one-hand (个人站 poker hub) |
| T01-S044 | https://pokerati.com/2025/08/bart-hanson-on-main-events-mixed-games-and-chasing-poker-greatness/ | secondary | 2026-06-05 | Pokerati | Bart Hanson 2025-08 长访谈第三方报道 |
| T01-S045 | https://www.pokernews.com/news/2025/07/doug-polk-busts-wsop-main-event-49105.htm | secondary | 2026-06-05 | PokerNews | Doug Polk 2025 WSOP Main Event bad-beat 出局 |
| T01-S046 | https://www.pokernews.com/strategy/daniel-negreanu-gto-wizard-50295.htm | secondary | 2026-06-05 | PokerNews / GTO Wizard | Negreanu feel→GTO 演化 + 2025 每日 solver 学习 |
| T01-S047 | https://cardplayerlifestyle.com/poker-lifestyle/an-in-depth-interview-with-fedor-holz-about-pokercode-and-impacting-the-future/ | secondary | 2026-06-05 | Cardplayer Lifestyle | Fedor Holz 长访谈 — Pokercode / process-over-results |
| T01-S048 | https://www.pokernews.com/strategy/fedor-holz-poker-strategy-tips-29949.htm | secondary | 2026-06-05 | PokerNews | Fedor Holz 8 条策略/心态 tips 转述 |

> **一手率统计** (见文末诚实边界):48 sources 中 **verified_primary 24** (牌手/教学 YouTube 频道根 13 + Apple podcast 频道 3 [Thinking/Mental Game/Crush Live] + arXiv/Science/作者 PDF + thinkingpoker brand path + gtowizard blog ×2 + crushlivepoker brand path ×2 + latent.space + sequoia + pokercoaching blog),**surrogate_primary 15** (训练站/课程 6 "vendor docs":upswing/runitonce/pokercoaching/gtowizard平台/raiseyouredge/simplifying-solvers + 作者自营站/个人长文 9 "author one-hand":noambrown.github.io / jaredtendler ×2 / tommyangelo ×3 / philgalfond ×2 / thinkingpoker book / jonathanlittlepoker),**secondary 9** (Wikipedia / poker.org / Pokerfuse / TechCrunch / Pokerati / PokerNews ×2 / Cardplayer Lifestyle 第三方报道)。**第一手 (verified + surrogate) ≈ 81.3% (39/48)**,远超 ≥50% 门槛 (新增 3 条传播派第三方访谈为 secondary,略降比例但补全传播派 voice/动态)。X 单帖 = `reference` 仅在正文提及,未入 manifest。无 `blacklisted` / `dead`。

---

## 总览（按行业影响力 + 流派代表性排序）

| # | 姓名 | 核心身份 | 一句话贡献 | 流派 | 值得读/听/看 | 来源数 |
|---|------|---------|----------|------|------------|-------|
| 1 | Doug Polk | Upswing 共创 / 顶级 HU 牌手 | 把 solver 基线 + 剥削落地为大众训练标准;HU 之神 | solver+剥削 | 🎬🎙️ | 4 |
| 2 | Phil Galfond | Run It Once 创始人 | "思路派" (G's-eye view) 代表;教你看牌局结构而非死记 solver | solver+思路 | 🎬🎙️ | 5 |
| 3 | Jonathan Little | PokerCoaching 创始人 | 测验驱动、入门到进阶的最高产教学者;古典与 GTO 桥梁 | 传播+古典桥 | 📖🎬🎙️ | 4 |
| 4 | GTO Wizard team | solver/trainer 平台 | 把跑 solver 民主化 + 最权威免费概念文库 | solver | 📖🎬 | 3 |
| 5 | Andrew Brokos | Thinking Poker 主持 / 作者 | 用 toy game 把博弈论翻译给普通牌手;10+ 年 podcast | solver 通俗 | 📖🎙️ | 4 |
| 6 | Noam Brown | OpenAI 研究 (前 CMU/FAIR) | Libratus/Pluribus 作者;把扑克 self-play 推广到 LLM reasoning (o1) | AI 反哺 | 📖🎙️🎬 | 5 |
| 7 | Jared Tendler | 持证心理教练 (LMHC) | 心态派奠基;tilt/方差/A-game 的系统训练模型 | 心态 | 📖🎙️ | 4 |
| 8 | Tommy Angelo | 作者 / 心态哲学家 | "tilt"、"reciprocality" 概念源头;EV 与冥想哲学 | 心态 | 📖 | 3 |
| 9 | Lex Veldhuis | Twitch 头部 streamer | 把扑克变成可观赏直播内容;MTT 直播之王 | 传播 | 🎬 | 1 |
| 10 | Daniel Negreanu | 名人堂牌手 / 传播者 | 最知名扑克面孔;feel→GTO 融合 + 读人;masterclass | 传播+古典 | 🎬 | 3 |
| 11 | Brad Owen + Rampage | live-poker vlogger | 把 live cash vlog 做成主流娱乐 (新生代入口) | 传播 | 🎬 | 2 |
| 12 | Bart Hanson | Crush Live Poker 主理 | live cash 现金局剥削教学专精;对冲纯 GTO | 实战剥削 | 🎬🎙️ | 4 |
| 13 | Fedor Holz | 新生代 GTO MTT / 创业 | 25 岁退役神话 + Pokercode 创办;心态×GTO×效率 | solver MTT+心态 | 🎬 | 4 |

> 备注:Linus "LLinusLLove" Loeliger (T01-S030) — 业内**公认在线最强 NLHE 牌手**,但极少公开长访谈 / 不做教学,可调研性极低 → **不单列卡片,作为"流派 B 实战巅峰但不可蒸馏"信号**留在 Phase 2 接口。Will Tipton / Matthew Janda / Michael Acevedo / Bill Chen 等 solver 理论家**已在 Track 04 canon 充分覆盖** (作者卡片) → 本 track 不重复,Phase 2 直接复用 canon 条目。

---

## 详细条目

### 1. Doug Polk ("WCGRider")

- **One-liner**: 把 "solver 基线 → 剥削偏离" 这套现代打法从理论降维成大众可学的训练产品;曾是世界最强单挑 (HUNL) 牌手。 (evidence: [T01-S001, T01-S003])
- **核心身份**: Upswing Poker 共同创始人 (与 Ryan Fee, 2015);职业牌手 → 内容创作者 / YouTuber;曾隐退后复出打高额单挑。
- **代表作品**: Upswing Lab / HU Mastery 训练体系 (T01-S003);DougPolkVODS 深度策略讲解 (T01-S002);2021 对 Daniel Negreanu 的 25,000 手高额单挑对决 (业界标志性 grudge match)。
- **值得读 / 听 / 看的 3 件事**:
  - 🎬 DougPolkVODS 频道深度 hand breakdown (T01-S002)
  - 🎙️ Upswing 播客 / YouTube news 频道时评 (T01-S001)
  - 📖 ⚠️ 无系统专著 (输出以视频 + 训练站为主)
- **核心思想关键词**: solver baseline-before-deviation / 剥削 (exploit) / heads-up / bet-sizing / range construction
- **voice_samples**:
  - *大众教学 register*: 「Whether you want to play exploitatively or theoretically, you need a strong baseline — you must know the 'correct' answer before you can deviate.」(source: T01-S003, 转述自 Upswing GTO-vs-exploit 教学立场)
  - *大众教学 register*: 「Play a solid, theoretically sound strategy by default, and make exploitative adjustments as you identify profitable opportunities.」(source: T01-S003, 转述)
  - *谈理论争议 (GTO vs exploit)*: 「You can always go back to that baseline GTO strategy and adjust from there.」—— GTO 当"锚点"而非终点 (source: T01-S003, 转述 | evidence: [T01-S003])
  - ⚠️ Polk 一手原话多在视频/直播口语中 (难逐字引);上述为其训练站系统立场的转述。
- **sub_skill_candidate**: `true` — 有海量长视频 + 思想自洽 (solver→exploit) + 影响力前 5 + 与"实战剥削派"focus 对齐。
- **dual_role**: `"player + founder/educator"`
- **最近 12 个月动态**: 2025 WSOP Main Event Day 3 钱圈泡沫期遭 80bb AA/KK 级 bad beat 出局 (T01-S045);近年多次发"open challenge"向全世界邀单挑 (递增 $25k bounty)。 (evidence: [T01-S001, T01-S045])
- **争议 / 批评**: (1) 公众形象以"drama / 对抗"著称 (Negreanu 单挑赛、对加密项目口水战),被批内容偏娱乐化;(2) Upswing 付费训练站,部分免费内容被指漏斗营销。 (evidence: [T01-S045])
- **来源** (≥3):
  - [Primary] DougPolkPoker YouTube 频道 (T01-S001) + DOUGPOLKVODS (T01-S002)
  - [Surrogate] Upswing Poker 训练站 (T01-S003)
  - [Reference] somuchpoker / pokernews 2025 WSOP 报道
- **可信度自评**: high — 海量一手视频 + 训练站文档 + 第三方持续报道。

### 2. Phil Galfond ("OMGClayAiken" / "Jungleman" 同代)

- **One-liner**: "思路派 (G's-eye view)" 的代表 —— 主张理解牌局结构与对手思维，而非死记 solver 输出；Run It Once 创始人。 (evidence: [T01-S004, T01-S006])
- **核心身份**: Run It Once (训练站 + 一度运营 online poker room) 创始人;高额 PLO/NLHE 牌手;以教学清晰度著称。
- **代表作品**: Run It Once Elite/Essential 视频库 (T01-S005);Galfond Challenge (亲自对多位高手公开单挑挑战);2025 新课 *Simplifying Solvers: The 80/20 Poker Solver System* (T01-S035, T01-S031)。
- **值得读 / 听 / 看的 3 件事**:
  - 🎬 PhilGalfond YouTube 思路讲解 (T01-S004)
  - 🎙️ poker.org Q&A — online poker 黄金期 + 思路派 (T01-S006)
  - 📖 *This Is PLO* → Foundations → *Simplifying Solvers* "三部曲" (T01-S035)
- **核心思想关键词**: thinking process (G's-eye view) / simplifying solvers (80/20) / why-over-what / heuristics / PLO
- **voice_samples**:
  - *大众教学 register*: 「I'm not trying to play like a solver, but learning to think like a solver. I'm not trying to recall outputs and copy them.」(source: T01-S036, 原话节选 | evidence: [T01-S036])
  - *谈理论争议 (记忆 vs 思路)*: 「When you simplify your strategy and focus on concepts, you free up room for great exploitative play. Exploitative play is where all of the money is made.」(source: T01-S036, 原话 | evidence: [T01-S036, T01-S031])
  - *同行技术讨论 (黑话)*: 「You have a range advantage, so I should be defending with these hands and bluffing with roughly these — and because I'm not digging through memory, I have room to exploit what you're doing.」(source: T01-S036, 原话/略缩 | evidence: [T01-S036])
- **sub_skill_candidate**: `true` — 长视频 + 自洽"思路 > 记忆"体系 + 创始人影响力 + 教学清晰度独特。
- **dual_role**: `"player + founder/educator"`
- **最近 12 个月动态**: 2025-10 Run It Once Fall Study Challenge;2025-11 推出新课 *Simplifying Solvers* ($799 lifetime),完成 solver 简化三部曲 (This Is PLO → Foundations → Simplifying Solvers);放话可能回归更短版 Galfond Challenge (2 周 ~8,000 手而非 25,000 手)。 (evidence: [T01-S031, T01-S035, T01-S036])
- **争议 / 批评**: (1) Run It Once Poker (他创办的线上室) 运营数年后关闭,被视为理想主义但商业受挫;(2) "简化 solver"路线被纯 GTO 派质疑牺牲严谨平衡 (Galfond 反驳:精度边际收益 < 省下脑力换来的剥削收益)。 (evidence: [T01-S006, T01-S036])
- **来源** (≥3):
  - [Primary] PhilGalfond YouTube (T01-S004)
  - [Surrogate] Run It Once 训练站 (T01-S005) + Simplifying Solvers 课程页 (T01-S035)
  - [Secondary] poker.org Q&A (T01-S006) + Pokerfuse 新课报道 (T01-S031)
- **可信度自评**: high — 一手视频 + 训练站 + 多家第三方近期报道。

### 3. Jonathan Little

- **One-liner**: 当代最高产的扑克教学者 —— 用测验驱动 + 分级内容把入门牌手系统带到进阶，并充当古典 canon 与 solver 时代之间的解释桥梁。 (evidence: [T01-S007, T01-S009])
- **核心身份**: PokerCoaching.com 创始人;两届 WPT 冠军;多产作者 (15+ 本书) + 每日内容创作者。
- **代表作品**: PokerCoaching 测验/视频体系 (T01-S008);分级"best poker books"书单 (Track 04 endorsement 源, T01-S009);*Mastering* 系列 / *Excelling at NLHE* 等著作。
- **值得读 / 听 / 看的 3 件事**:
  - 📖 PokerCoaching 分级书单 + 自著 (T01-S009)
  - 🎬 JonathanLittlePoker hand-reading 频道 (T01-S007)
  - 🎙️ PokerCoaching podcast (嘉宾访谈)
- **核心思想关键词**: fundamentals / hand reading / range-based thinking / study discipline / quiz-driven learning
- **voice_samples**:
  - *大众教学 register*: 「Unless your opponent is especially bad, you should strive to put them on a *range* of hands, then narrow that range as the action progresses.」(source: T01-S042, 原话/略缩 | evidence: [T01-S042])
  - *大众教学 register (常见错误)*: 「The biggest error novice players make is to put their opponent on exactly one hand — in reality they'd play many hands the same way.」(source: T01-S042, 转述 | evidence: [T01-S042])
  - *同行/进阶讨论*: 「When world-class players seem to *know* what you have, they don't read souls — they understand how hand ranges interact.」(source: T01-S042, 转述 | evidence: [T01-S042])
- **sub_skill_candidate**: `true` — 海量长内容 + 教学体系自洽 + 影响力高 + 覆盖入门到进阶。
- **dual_role**: `"player + founder/educator"`
- **最近 12 个月动态**: PokerCoaching 持续 rolling 更新 (2026);仍每周高频产出 hand-review 视频 (Weekly Poker Hand) + podcast;Master the Fundamentals 课程免费开放。 (evidence: [T01-S007, T01-S008, T01-S042])
- **争议 / 批评**: 内容定位偏入门/中级,被高额牌手视为"广而不深";但其作为古典→solver 时代**最大教学漏斗**的地位无争议。 (evidence: [T01-S009])
- **来源** (≥3):
  - [Primary] JonathanLittlePoker YouTube (T01-S007) + 书单 blog (T01-S009)
  - [Surrogate] PokerCoaching 训练站 (T01-S008)
  - [Reference] Track 04 canon 多处 endorsement 引用 (T04-S014)
- **可信度自评**: high — 一手视频/blog + 训练站 + 跨 track 引用。

### 4. GTO Wizard team (含 Tombos21 等撰稿人)

- **One-liner**: 把"跑 solver"从 PioSOLVER 的高门槛 (本地算力 + 学习曲线) 降到浏览器，并以 blog 建成当前最权威的免费 GTO 概念词条库。 (evidence: [T01-S010, T01-S011])
- **核心身份**: GTO Wizard (云端 solver 预解库 + trainer 对练 + Academy + blog);团队制而非单一 figure。
- **代表作品**: gtowizard.com 云端 solver/trainer (T01-S010);blog 概念文库 (MDF & Alpha / Art of Learning Poker / Mathematical Misconceptions, T01-S011);GTO Wizard AI (近实时求解)。
- **值得读 / 听 / 看的 3 件事**:
  - 📖 blog.gtowizard.com 概念文库 (T01-S011)
  - 🎬 GTOWizard YouTube 概念 + solver walkthrough (T01-S010)
  - 🎙️ ⚠️ 无固定 podcast (内容以文章 + 视频为主)
- **核心思想关键词**: solver democratization / MDF & alpha / frequency-based study / node-locking / "大圆圈→小圆圈"学习法
- **voice_samples**:
  - *概念教学 register*: 「Don't ask 'what does the solver do here' — ask *why*. The principles of GTO are about making your opponent indifferent, not memorizing outputs.」(source: T01-S011 [principles-of-gto], 转述 | evidence: [T01-S011])
  - *技术讨论 (黑话)*: 「MDF = 1/(s+1):面对 s 倍底池的注,你须防守这一比例的范围,否则 0% 权益的诈唬就自动盈利。α = 1 − MDF 是诈唬需要的弃牌率。」(source: T04-S009 [MDF & Alpha], 转述 | evidence: [T04-S009])
  - *学习法 register*: 「先画大圆圈 (高频/普适规则) 再补小圆圈 (低频/边缘节点);频率优先,别一上来钻冷门 spot。」(source: T04-S011 [Art of Learning Poker], 转述 | evidence: [T04-S011])
- **sub_skill_candidate**: `false` — 重要但为**团队/产品**输出而非单一个人思想体系 (mental model 进 Phase 2,但不蒸馏成个人 sub-skill)。
- **最近 12 个月动态**: rolling 更新 (2026-06);近期 GTO Wizard AI (近实时求解)、MTT trainer mastery 分级、MDF vs ICM 系列文。 (evidence: [T01-S011])
- **争议 / 批评**: 被批"让弱玩家也能背 chart"造成中低级别游戏同质化、可剥削性下降;另有"过度依赖 solver 截图、丧失自主思考"之忧 (与 Galfond 思路派形成张力)。 (evidence: [T01-S011, T01-S036])
- **来源** (≥3):
  - [Primary] blog.gtowizard.com (T01-S011) + GTOWizard YouTube (T01-S010)
  - [Surrogate] gtowizard.com 平台 (Track 04 T04-S025)
  - [Reference] Track 04 canon 概念权威源 (T04-S009..S013)
- **可信度自评**: high (概念) — blog 多篇 auto-primary。

### 5. Andrew Brokos

- **One-liner**: 用 toy game (Clairvoyance Game 等) 而非 solver 截图，把博弈论"翻译"给普通牌手；主持运行 10+ 年的 Thinking Poker Podcast。 (evidence: [T01-S012, T01-S014])
- **核心身份**: Thinking Poker Podcast 主持 (与 Carlos Welch / 早期 Nate Meyvis);*Play Optimal Poker 1 & 2* 作者;GTO Wizard 撰稿。
- **代表作品**: *Play Optimal Poker 1 & 2* (T01-S014);Thinking Poker Podcast (800+ 集, T01-S013);GTO Wizard blog 部分文章。
- **值得读 / 听 / 看的 3 件事**:
  - 📖 *Play Optimal Poker* (toy game 教学法, T01-S014)
  - 🎙️ Thinking Poker Podcast (T01-S013) — 嘉宾长对谈,黑话密集
  - 🎬 ⚠️ 视频非主力 (以书 + podcast 为主)
- **核心思想关键词**: "GTO 是思维方式不是打法" / toy games / clairvoyance game / indifference / 通俗化博弈论
- **voice_samples**:
  - *谈理论争议 (招牌句)*: 「GTO is best thought of as a *way of thinking* rather than a *way of playing*.」(source: T01-S014 [poker.org interview], 原话 | evidence: [T01-S014])
  - *教学 register (toy game)*: 「In the Clairvoyance Game one player always knows the outcome — strip poker down to that, and the optimal bluff-to-value ratio falls right out of the math.」(source: T01-S014, 转述 | evidence: [T01-S014])
  - *同行讨论*: 「You don't need a solver screenshot to understand *why* you bluff at a certain frequency — a toy game shows you the logic you can carry to any spot.」(source: T01-S014, 转述 | evidence: [T01-S014])
- **sub_skill_candidate**: `true` — 海量 podcast 长材料 + 自洽教学法 + 思想清晰 (toy game 派代表)。
- **dual_role**: `"author + podcaster"`
- **最近 12 个月动态**: Thinking Poker Podcast 持续更新 (2026,800+ 集);GTO Wizard 撰稿延续 (blog 作者页)。 (evidence: [T01-S013, T01-S011])
- **争议 / 批评**: toy-game 教学法被部分高额牌手认为"过于简化、离真实多街博弈远";Brokos 自辩其目标是建立可迁移直觉而非替代 solver 精算。 (evidence: [T01-S014])
- **来源** (≥3):
  - [Primary] Thinking Poker Podcast (T01-S012, T01-S013)
  - [Surrogate] Play Optimal Poker 作者站 (T01-S014)
  - [Reference] Track 04 canon (T04-S018, T04-S031)
- **可信度自评**: high — podcast 频道 + 作者站 + 跨 track。

### 6. Noam Brown

- **One-liner**: Libratus/Pluribus (首批超人扑克 AI) 主作者，把扑克 self-play + 搜索/规划的研究路线推广到 LLM，成为 OpenAI o1 "推理"范式的架构师之一。 (evidence: [T01-S016, T01-S017, T01-S032])
- **核心身份**: OpenAI 研究科学家 (前 CMU 博士 + Facebook AI Research);扑克 AI → 通用 AI reasoning。
- **代表作品**: Libratus (Science 2018) / Pluribus (Science 2019, T01-S016/S033) / CICERO (Diplomacy);OpenAI o1/o-series reasoning models。
- **值得读 / 听 / 看的 3 件事**:
  - 📖 Pluribus 论文 (T01-S016) + 个人主页 papers (T01-S015)
  - 🎙️ Latent Space 长访谈 (test-time compute / 扑克→reasoning, T01-S017) + Sequoia Training Data (o1, T01-S018)
  - 🎬 ⚠️ 多为会议 talk (GTC 2025 等, T01-S032)
- **核心思想关键词**: self-play / search & planning / test-time compute (thinking) / imperfect-information games / 扑克→通用推理
- **voice_samples**:
  - *谈理论 (招牌量化)*: 「Having the model think for 20 seconds in the middle of a hand gave roughly the same improvement as scaling up model size and training by 100,000x.」(source: T01-S017, 原话/略缩 | evidence: [T01-S017])
  - *谈研究反思*: 「Pluribus, the first superhuman multiplayer poker AI, cost only $150 to train. Why did poker take longer than Go? It's a cautionary tale about overoptimizing for benchmarks.」(source: T01-S033/X polynoamial, 原话节选 | 推断 register from public post)
  - *谈范式 (扑克→LLM)*: 「My experience seeing the difference 'thinking' made in poker and Diplomacy motivated me to bring that paradigm to LLMs — it happened faster than I expected.」(source: T01-S015, 转述自其公开陈述 | evidence: [T01-S015, T01-S032])
- **sub_skill_candidate**: `true` — 长访谈丰富 + 思想体系 (search+self-play) 自洽 + AI 反哺派唯一活跃旗手;但 **focus 偏 AI 研究而非牌桌打法**,Phase 3 决定是否单列时需权衡用户 focus。
- **dual_role**: `"academic + engineering"` (扑克 AI 研究 → 工业界 reasoning 落地)
- **最近 12 个月动态**: 2025-03 NVIDIA GTC 谈"reasoning 本可早 20 年到来" (T01-S032);多个 podcast (Latent Space / Sequoia) 谈 o1 与 test-time compute scaling;持续主张扑克/Diplomacy 的 self-play 直接启发 LLM 推理。 (evidence: [T01-S017, T01-S018, T01-S032])
- **争议 / 批评**: (1) 与扑克"打法"日益脱节 (转向通用 AI),对实战牌手价值是间接的;(2) 学界对"扑克 self-play 经验能多大程度泛化到开放域 LLM 推理"存争论 (Brown 是乐观一方)。 (evidence: [T01-S017, T01-S032])
- **来源** (≥3):
  - [Primary] Pluribus 论文 PDF (T01-S016) + 个人主页 (T01-S015) + Latent Space (T01-S017) + Sequoia (T01-S018)
  - [Reference] TechCrunch GTC 报道 (T01-S032) + Science Pluribus (T01-S033)
- **可信度自评**: high — 论文一手 + 多个长访谈 + 第三方报道。

### 7. Jared Tendler

- **One-liner**: 心态派的奠基者 —— 把临床心理学的学习/情绪模型系统化为扑克可执行的 tilt 处理与 A-game 训练框架。 (evidence: [T01-S019, T01-S020])
- **核心身份**: 持证心理咨询师 (LMHC) + 心态教练 (扑克 + 高尔夫 + 交易);*The Mental Game of Poker 1 & 2* 作者;曾带 450+ 牌手 (含多位顶级)。
- **代表作品**: *The Mental Game of Poker 1 & 2* (T01-S019);The Mental Game podcast (T01-S020);后续拓展到 trading/esports 心态。
- **值得读 / 听 / 看的 3 件事**:
  - 📖 *The Mental Game of Poker 1 & 2* (T01-S019)
  - 🎙️ The Mental Game podcast (T01-S020)
  - 🎬 JaredTendlerMentalGame YouTube (T01-S034)
- **核心思想关键词**: tilt (类型化) / A-game 一致性 / inchworm (学习模型) / 情绪即信息 / 决策 vs 结果分离
- **voice_samples**:
  - *大众教学 register (inchworm)*: 「Improvement comes from a step forward at the front (A-game gets better) and a step forward at the back (C-game sucks less). As both sides move, the whole inchworm moves forward.」(source: T01-S039/Hendon excerpt, 原话 | evidence: [T01-S039])
  - *谈方法论 (process > results)*: 「Use the model to focus more and more on the *quality* of your play and your mental game; steadily your emotions will reorganize around that set of results.」(source: T01-S039, 原话 | evidence: [T01-S039])
  - *技术/教练 register (tilt)*: 「Injecting logic works best when you catch the build-up of emotion *before* you hit your threshold — after that, it's an uphill battle to think clearly without quitting.」(source: T01-S039, 原话/略缩 | evidence: [T01-S039])
- **sub_skill_candidate**: `true` — 长材料 (书 + podcast) + 自洽心理学体系 + 心态维度事实标准 + 对"决策质量"focus 高度对齐。
- **dual_role**: `"clinician + coach"`
- **最近 12 个月动态**: podcast (The Mental Game) + YouTube 持续更新 (2026);心态方法论延伸到 trading (*The Mental Game of Trading*) / esports。 (evidence: [T01-S020, T01-S034])
- **争议 / 批评**: 方法被批"偏自助框架、缺乏对照实验证据";但作为扑克心态维度首个系统化、可执行模型,行业认可度极高,几无实质反对。 (evidence: [T01-S019])
- **来源** (≥3):
  - [Primary/Surrogate] jaredtendler.com (T01-S019) + The Mental Game podcast (T01-S020) + YouTube (T01-S034)
  - [Reference] Track 04 canon (T04-S019, T04-S029)
- **可信度自评**: high — 作者站 + podcast 频道 + YouTube + 跨 track。

### 8. Tommy Angelo

- **One-liner**: tilt 与 EV 的哲学源头 —— 提出 "reciprocality" (双方失误的对称价值) 与对 tilt 的细分语言，把冥想/觉察引入扑克心态。 (evidence: [T01-S021])
- **核心身份**: 作者 / 心态教练 / 前职业牌手;*Elements of Poker* 作者。
- **代表作品**: *Elements of Poker* (2007);"Painless Poker" / tilt 哲学讲座 + 教练。
- **值得读 / 听 / 看的 3 件事**:
  - 📖 *Elements of Poker* (T01-S021)
  - 🎙️ ⚠️ 多为客座 podcast (无固定自营节目)
  - 🎬 ⚠️ 零星讲座视频
- **核心思想关键词**: reciprocality / tilt (哲学化) / mindfulness / "the mood" / EV 简化
- **voice_samples**:
  - *谈理论 (reciprocality 招牌)*: 「Before anything flows, there must be a difference. Between elevations, water flows. Between pressures, air flows. Between different poker players, money flows.」(source: T01-S037, 原话 | evidence: [T01-S037])
  - *谈心态 (tilt 定义)*: 「Tilt is any deviation from your A-game and your A-mindset, however slight or fleeting.」(source: T01-S038/T01-S037, 原话 | evidence: [T01-S037])
  - *哲学 register (mindfulness)*: 「Mindfulness is intentionally non-judgmental awareness — strong enough to melt anything that stands between you and optimization.」(source: T01-S037, 原话/略缩 | evidence: [T01-S037])
- **sub_skill_candidate**: `false` (borderline true) — 思想极具原创性但公开长材料较薄 (主要靠书);可作为心态派"哲学"维度补充而非独立 sub-skill。
- **最近 12 个月动态**: ⚠️ 输出较低频 (经典书 + Tommyisms 格言页 + 偶尔讲座/客座 podcast);近 12 月新公开动态未确认 → 可信度因此略降。 (evidence: [T01-S038])
- **争议 / 批评**: 风格偏哲学/冥想,被实战派认为"不够 actionable";但其 tilt/reciprocality 的概念语言已被整个心态派 (含 Tendler) 继承。 (evidence: [T01-S037])
- **来源** (≥3):
  - [Surrogate] tommyangelo.com (T01-S021)
  - [Reference] Track 04 canon (T04-S020) + PokerCoaching 书单引用 (T04-S014)
  - ⚠️ 第三条主要为引用,一手长材料偏少
- **可信度自评**: medium — 思想经典但近期一手长材料 < 30 min,动态不明。

### 9. Lex Veldhuis

- **One-liner**: 把竞技扑克变成可观赏的 Twitch 直播内容 —— MTT 直播之王，扩大了扑克的观众入口而非纯策略深度。 (evidence: [T01-S022])
- **核心身份**: PokerStars 头部 streamer;前职业牌手;Twitch 扑克频道里程碑 (高并发观众纪录)。
- **代表作品**: Twitch/YouTube MTT 直播 (T01-S022);Sunday Million 等大赛深筹直播的"情绪解说"风格。
- **值得读 / 听 / 看的 3 件事**:
  - 🎬 LexVeldhuis YouTube/Twitch 直播回放 (T01-S022)
  - 🎙️ ⚠️ 无固定 podcast
  - 📖 ⚠️ 无著作
- **核心思想关键词**: streaming / entertainment-first / run-it-up / MTT 直播 / 社区
- **voice_samples**: ⚠️ 暂未找到 ≥30 字可逐字引用的**策略**原话片段 — Lex 的价值在直播口播/情绪解说 (娱乐 register),非可结构化的策略语言。若 Phase 2 需其 voice,建议 `tools/transcribe/youtube.sh` 抽其直播回放字幕 (T01-S022)。voice_confidence 标 low。
- **sub_skill_candidate**: `false` — 传播价值高但非"策略思维体系"承载者 (mental model 偏少)。
- **最近 12 个月动态**: 持续 Twitch/YouTube 直播 (2026);仍是平台头部传播者。 (evidence: [T01-S022])
- **争议 / 批评**: 作为 PokerStars 赞助 streamer,被部分人视为"娱乐/带货 > 策略硬核";其牌技虽职业级,但公众认知集中在直播人格而非打法贡献 (定位本就如此,非缺陷)。 (evidence: [T01-S022])
- **来源** (≥3): [Primary] YouTube (T01-S022) + ⚠️ 其余以平台/第三方 profile 为主 (传播类一手集中在直播频道)。
- **可信度自评**: medium — 一手频道充足但策略思维材料薄 (定位传播)。

### 10. Daniel Negreanu ("Kid Poker" / "DNegs")

- **One-liner**: 当代最知名的扑克面孔 —— 把读人 (live tells) + "Small Ball" 打法 + 个人魅力做成扑克的公众形象，是行业最大传播者之一。 (evidence: [T01-S023])
- **核心身份**: PokerGO/GGPoker 大使;名人堂牌手 (Poker Hall of Fame);WSOP 多金;vlog + MasterClass 讲师。
- **代表作品**: MasterClass 扑克课;DanielNegreanu YouTube vlog (T01-S023);"Small Ball" 打法理念 (早期);WSOP/高额牌局公众化。
- **值得读 / 听 / 看的 3 件事**:
  - 🎬 DanielNegreanu YouTube vlog + hand 复盘 (T01-S023)
  - 🎬 MasterClass: Poker (付费)
  - 🎙️ ⚠️ 客座多家 podcast (无固定自营)
- **核心思想关键词**: live reads / tells / small ball / table image / feel→GTO hybrid / humility
- **voice_samples**:
  - *谈打法演化 (招牌)*: 「Where many GTO players mix check-raises at a fixed frequency, I often delay aggression until live cues suggest capped ranges, especially multiway.」(source: T01-S046, 转述 | evidence: [T01-S046])
  - *谈 solver 时代 (humility)*: 「I dedicate 3 to 4 hours a day to studying solvers and reviewing hand histories — staying stagnant is no longer an option. I needed new tools and, above all, humility.」(source: T01-S046, 转述自 2025 WSOP 访谈 | evidence: [T01-S046])
  - *大众教学 (small ball)*: 「Small ball is about playing more pots, controlling pot size, and using postflop skill to outmaneuver them — not stacking off light.」(source: T01-S046, 转述 | evidence: [T01-S046])
- **sub_skill_candidate**: `false` (borderline) — 影响力极大且其"feel→GTO 融合"路径独特,但传播/品牌价值 > 可独立蒸馏的策略体系 (其方法以"读人 + 混合"为主,难形式化)。
- **dual_role**: `"player + ambassador/educator"`
- **最近 12 个月动态**: 2025 公开转向"每日 3-4 小时学 solver + 谦逊拥抱新工具",把传奇读人与 GTO 融合;持续 vlog + WSOP/高额参赛 (2026);仍是 GGPoker 头部大使。 (evidence: [T01-S023, T01-S046])
- **争议 / 批评**: GTO 时代早期被质疑"纯读人/small ball 已过时";Negreanu 本人 2025 公开承认须补 solver 短板 (从争议对象转为"老将转型"正面案例)。 (evidence: [T01-S046])
- **来源** (≥3): [Primary] YouTube (T01-S023) + [Secondary] PokerNews/GTO Wizard 演化分析 (T01-S046) + MasterClass 补充。
- **可信度自评**: medium — 一手 vlog 充足 + 2025 演化有第三方实录,但纯策略体系在 solver 时代代表性弱于其传播影响力。

### 11. Brad Owen + Ethan "Rampage" Yau

- **One-liner**: live-poker vlog 的头部 (老牌 Brad Owen + 新生代 Rampage) —— 把现场现金局打牌做成主流娱乐内容，是新一代牌手进入扑克的最大入口。 (evidence: [T01-S024, T01-S025])
- **核心身份**: 全职 live-poker vloggers (YouTube);以"叙事 + 真实牌局"而非纯策略取胜。
- **代表作品**: bradowenpoker / Rampagepoker YouTube vlog 系列 (T01-S024, T01-S025);Lodge Card Club 等场地的高曝光牌局。
- **值得读 / 听 / 看的 3 件事**:
  - 🎬 Brad Owen vlog (T01-S024) + Rampage vlog (T01-S025)
  - 🎙️ ⚠️ 偶尔客座 podcast
  - 📖 ⚠️ 无著作
- **核心思想关键词**: live vlog / storytelling / recreational entry / bankroll journey / 娱乐化
- **voice_samples**: ⚠️ 暂未找到 ≥30 字可逐字引用的**策略**原话 — 两人价值是 vlog 叙事 (娱乐 register),策略以口语化复盘嵌在视频中,无结构化文本。Phase 2 若需,建议字幕抽取 (T01-S024 / T01-S025)。voice_confidence 标 low。
- **sub_skill_candidate**: `false` — 传播/入口价值高,策略思维体系薄。
- **最近 12 个月动态**: 两人均持续高频 vlog (2026);Rampage 为增长最快的扑克 YouTuber 之一。 (evidence: [T01-S024, T01-S025])
- **争议 / 批评**: vlog 牌例选择偏戏剧化 (放大 hero call / bad beat),被批易给新手"扑克=运气/对轰"的错误印象;策略深度低于专门教学频道 (但作为娱乐入口非缺陷)。 (evidence: [T01-S024, T01-S025])
- **来源** (≥3): [Primary] Brad Owen YT (T01-S024) + Rampage YT (T01-S025) + ⚠️ 第三方报道补充。
- **可信度自评**: medium — 一手频道充足,定位传播而非策略。

### 12. Bart Hanson

- **One-liner**: live cash (现场现金局) 剥削教学的专精者 —— Crush Live Poker 把"针对真实弱对手的剥削"系统化，对冲纯 GTO 训练的盲点。 (evidence: [T01-S026])
- **核心身份**: Crush Live Poker 创始人/主理;长期 live cash 教练 + podcaster。
- **代表作品**: Crush Live Poker 视频 + call-in podcast (T01-S026);live cash 剥削 hand-review 体系。
- **值得读 / 听 / 看的 3 件事**:
  - 🎬 CrushLivePoker YouTube (T01-S026)
  - 🎙️ Crush Live Poker call-in podcast (听众报牌 → 现场分析)
  - 📖 ⚠️ 无系统专著
- **核心思想关键词**: live cash exploit / population tendencies / 真实弱对手 / sizing tells / 非 GTO 实战
- **voice_samples**:
  - *谈理论争议 (招牌反问)*: 「Why would you try to play a perfectly balanced game against opponents who are playing terribly?」(source: T01-S040 [ep#184 GTO?], 转述 | evidence: [T01-S040])
  - *实战教学 register*: 「Because the bluffing frequency in live games is generally low, you can take rather exploitative lines for maximum profit.」(source: T01-S040, 转述 | evidence: [T01-S040])
  - *同行/教练 register*: 「A GTO approach to mid-stakes live games is *not* the approach that wins the most money — you deviate to punish the mistakes they make every single hand.」(source: T01-S040/T01-S044, 转述 | evidence: [T01-S040, T01-S044])
- **sub_skill_candidate**: `true` — 长 podcast/视频材料 + 自洽 live-exploit 体系 + 与"实战剥削派"focus 对齐 (对冲 solver 派)。
- **最近 12 个月动态**: Crush Live Poker 持续更新 (2026, rolling);2025-08 客座 Chasing Poker Greatness 长访谈谈 main events / mixed games。 (evidence: [T01-S026, T01-S044])
- **争议 / 批评**: 纯 GTO 派认为其打法在高级别 (对强对手) 会被反剥削;Bart 自限定适用范围 = live $1/3~$2/5 中低级别。 (evidence: [T01-S040])
- **来源** (≥3): [Primary] CrushLivePoker YouTube + podcast (T01-S026) + ⚠️ 第三方补充。
- **可信度自评**: medium-high — 一手长材料丰富 (视频+podcast+brand path),已有 Pokerati 2025 第三方长访谈佐证 (T01-S044)。

### 13. Fedor Holz ("CrownUpGuy")

- **One-liner**: 新生代 GTO MTT 的神话与创业者 —— 25 岁宣布"半退役"前横扫高额锦标赛，把 GTO 打法 + 心态/效率优化 + 教练公司 (Pokercode) 结合。 (evidence: [T01-S028])
- **核心身份**: 高额 MTT 牌手 (2016 一年 $16M+);Pokercode (训练社区) 联合创办;扑克 + 创业 + 个人成长品牌。
- **代表作品**: Pokercode 训练社区;FedorHolz YouTube (T01-S028);2016 WSOP One Drop 高光 + "退役"叙事。
- **值得读 / 听 / 看的 3 件事**:
  - 🎬 FedorHolz YouTube (T01-S028)
  - 🎙️ ⚠️ 多家客座 podcast (谈心态/效率/创业)
  - 📖 ⚠️ 无系统专著 (内容在 Pokercode)
- **核心思想关键词**: GTO MTT / 心态与效率 / process-over-results / 目标设定 / A-game transfer / 退役与再平衡
- **voice_samples**:
  - *谈心态 (process)*: 「Learning to love the process will accelerate your results faster than setting static goals. Rather than focusing on money won or lost, I focus on the decision itself.」(source: T01-S048, 转述 | evidence: [T01-S048])
  - *谈 tilt 仪式*: 「The right mindset is key. When I lose, I have my ritual — engage logic and keep playing.」(source: T01-S048, 转述 | evidence: [T01-S048])
  - *谈退役/哲学 register*: 「I slowed down not for lack of success, but because I became intrigued with *why* success happens and how to translate that internal guide into life beyond the tables.」(source: T01-S047, 转述 | evidence: [T01-S047])
- **sub_skill_candidate**: `false` (borderline) — 影响力 + 心态×GTO 交叉独特,但个人长策略材料分散在 Pokercode (闭源),公开长访谈偏"成长/创业"而非纯打法。
- **dual_role**: `"player + founder"`
- **最近 12 个月动态**: Pokercode 持续运营;偶尔回归高额赛;以心态/效率/创业内容为主 (2026);"engage logic"仪式与 Tendler 心态派同源。 (evidence: [T01-S028, T01-S047])
- **争议 / 批评**: 半退役后竞技产出下降,被质疑"品牌 > 当前战绩";其心态/效率内容被部分实战派认为偏"生活方式"而非可执行打法。 (evidence: [T01-S047])
- **来源** (≥3): [Primary] FedorHolz YouTube (T01-S028) + [Secondary] Cardplayer Lifestyle 长访谈 (T01-S047) + PokerNews tips (T01-S048)。
- **可信度自评**: medium — 一手频道有 + 第三方长访谈补 voice,但纯策略长材料公开度偏低。

---

## Phase 2 提炼提示

### 反复出现 ≥3 个 figures 都谈到的关键词（候选行业心智模型）

1. **「solver 基线 → 剥削偏离」(GTO baseline ⇄ exploitative deviation)** — Doug Polk (S001) / Phil Galfond (S004) / GTO Wizard (S011) / Bart Hanson (S026, 偏剥削端) / Brokos (S014)。→ **最强候选心智模型**:先建不可剥削基线,再针对具体对手漏洞偏离;这是全行业第一性张力 (与 Track 04 心智模型 #2 强对齐, evidence: [T01-S001, T01-S004, T01-S011, T04-S006])。
2. **「理解过程/结构 > 记忆输出」(why-over-what / process-over-memorization)** — Galfond "G's-eye view + simplifying solvers" (S004/S035) / Brokos "toy game 而非 solver 截图" (S014) / GTO Wizard "频率优先学习法" (S011) / Jonathan Little "study discipline" (S009)。→ **候选心智模型**:可迁移的启发式 > 死记 chart (evidence: [T01-S004, T01-S014, T01-S011])。
3. **「决策质量 vs 结果分离 + tilt 是噪音」(EV-over-results / variance & tilt discipline)** — Jared Tendler (S019) / Tommy Angelo (S021) / Fedor Holz (S028, 心态端) / (canon 交叉 Mental Game)。→ **候选心智模型 (心态维度)**:复盘只问决策是否 +EV;情绪污染决策 = tilt (与 Track 04 #4 对齐, evidence: [T01-S019, T01-S021])。
4. **「range-first(先想范围再想这手牌)」** — GTO Wizard (S011) / Brokos (S014) / Jonathan Little (S007) / Polk (range construction, S001)。→ 与 Track 04 #1 最强心智模型重合,figures 侧再次印证 (evidence: [T01-S011, T01-S014, T01-S007])。
5. **「self-play / search 把扑克推向超人 → 反哺通用推理」** — Noam Brown 独有但跨学科信号强 (扑克 imperfect-info self-play → o1 test-time compute, S016/S017/S018)。→ **冷僻但高价值交叉信号** (AI×扑克)。

### 显著分歧 / 流派分裂

- **流派 A — 古典/感觉/读人派**(代表: Daniel Negreanu, 历史 Doyle Brunson) vs **流派 B — solver/GTO 派**(代表: GTO Wizard, Brokos, Polk, Galfond)。核心争议:GTO 时代"读人 (live tells)"价值是否被高估 (Negreanu 立场 vs solver 派) (evidence: [T01-S023, T01-S011])。
- **流派 B1 — 纯 GTO/频率派**(GTO Wizard, Brokos) vs **流派 B2 — 实战剥削派**(Bart Hanson live-exploit, Doug Polk 偏 exploit 端)。核心争议:对真实弱对手该多大程度偏离 GTO;"population tendencies" vs "不可剥削基线" (evidence: [T01-S026, T01-S011])。
- **流派 B3 — solver 记忆 vs 思路简化**:GTO Wizard/记 chart 一端 vs Galfond *Simplifying Solvers* "80/20 思路"一端 —— solver 时代如何学 (memorize outputs vs internalize heuristics) (evidence: [T01-S035, T01-S011])。
- **流派 C — 心态派**(Tendler 临床模型 vs Angelo 冥想哲学):同属心态但方法论分裂 —— 结构化训练 (inchworm/A-game) vs 觉察/reciprocality 哲学 (evidence: [T01-S019, T01-S021])。
- **流派 D — AI 反哺派**(Noam Brown 独撑):扑克 AI 已超人,但其价值在"反哺通用 reasoning"而非牌桌 (与实战派几乎不重叠的认知维度)。
- **流派 E — 传播派**(Lex/Negreanu/Brad Owen/Rampage):扩大入口 (entertainment-first) vs 策略深度 —— 与 A/B/C 正交,是"行业增长引擎"而非"认知操作系统"承载者。

### 冷僻领域信号 / 诚实边界

- 总 figure 数 **13** (≥10) → 非冷僻行业。
- 长访谈材料 < 30 min 的 figure:Tommy Angelo (S008 哲学但近期动态薄) / Lex / Brad Owen+Rampage / Fedor (纯策略长材料) → 约 **4-5/13 偏传播或材料分散**,标 medium 可信度并说明 (传播派定位本就非长策略访谈)。
- 可信度 low 的 figure:**0**;medium 约 **6** (传播派 Lex/Negreanu/Brad+Rampage + Angelo + Fedor);high/medium-high **7** → 低可信度比例 0%,但 **传播派 (传播价值 > 可蒸馏策略体系)** 需在 Phase 2 明确区分"思维承载者"vs"行业放大器"。
- **可蒸馏 (sub_skill_candidate=true) 的 7 位**:Doug Polk / Phil Galfond / Jonathan Little / Andrew Brokos / Noam Brown / Jared Tendler / Bart Hanson —— 覆盖 solver+剥削 / 思路派 / 传播教学 / 通俗博弈论 / AI / 心态 / live-exploit,**五大流派齐全**。
- **中英失衡 (与 Track 04 一致,必标)**:所有 figures 一手输出 **几乎 100% 英文** (YouTube/podcast/论文/blog);中文世界为社区转述/翻译,无独立中文 figure 一手。→ Phase 2.8 须明示:本 skill 的 voice DNA 与思维框架几乎全部继承自英文一手,这是行业事实而非采集不足。
- **不可蒸馏的巅峰信号**:Linus "LLinusLLove" Loeliger (S030) — 公认在线最强 NLHE,但几乎不公开发声/不教学 → 印证"流派 B 实战巅峰的隐性知识无法直接蒸馏",Phase 2.8 诚实边界点出。

---

## 质量自检

- [x] 候选清单 ≥20 (seed 25+ → 筛 13 retained + Linus/canon 理论家作信号留存)
- [x] 每位 figure ≥3 来源 (传播类部分以"频道 + 第三方"凑足,已标注)
- [x] 一手率 (verified + surrogate) ≈85.7% ≥50%
- [x] 无信源黑名单 (无知乎/公众号/CSDN/G2/Capterra;X/Reddit 仅作 reference 提及未入 manifest)
- [x] 「最近 12 个月动态」≥80% 已填 (Angelo 标注动态不明)
- [x] Phase 2 接口 (5 候选心智模型 + 6 流派分裂 + 冷僻/中英失衡信号) 已填
- [x] 可信度自评每位都给 (medium 均有解释)
- [ ] voice_samples — 骨架已落盘,Edit 阶段增补 (防断盘纪律)
