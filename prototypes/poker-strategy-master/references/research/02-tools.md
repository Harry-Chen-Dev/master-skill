# Track 02 — Tools 工具地图：德州扑克策略 (Texas Hold'em / NLHE, locale=global)

> Phase 1 wave 2 第 2 路 subagent 输出。三层结构（必备 / 场景特化 / 新兴）+ 选型决策树 + 避坑清单。
> last_checked 全部 = 2026-06-05。Wave 1 seed 文件本次为空（research dir 仅有本文件），故主要从 intake.json 的 figures/canon/glossary 线索 + 自有调研撒网。

## Source Manifest

| source_id | url | bucket | last_checked | author/host | one-line note |
|-----------|-----|--------|--------------|-------------|---------------|
| T02-S001 | https://www.science.org/doi/10.1126/science.aao1733 | verified_primary | 2026-06-05 | Brown & Sandholm (Science) | Libratus 论文：HUNL 首个超人 AI，CFR 三段式，120k 手 |
| T02-S002 | https://www.science.org/doi/10.1126/science.aay2400 | verified_primary | 2026-06-05 | Brown & Sandholm (Science) | Pluribus 论文：6-max 超人 AI，<128GB / 2×CPU 推理 |
| T02-S003 | https://noambrown.com/papers/17-Science-Superhuman.pdf | verified_primary | 2026-06-05 | Noam Brown | Libratus 作者本人 PDF 镜像（figure 一手） |
| T02-S004 | https://blog.gtowizard.com/introducing-gto-wizard-ai/ | verified_primary | 2026-06-05 | GTO Wizard | GTO Wizard AI 官宣 2023-07-19；并购 Ruse；19bb/100 vs Slumbot |
| T02-S005 | https://blog.gtowizard.com/gto-wizard-ai-explained/ | verified_primary | 2026-06-05 | GTO Wizard | AI solver 架构解释（CFR / 云端 / 求解精度） |
| T02-S006 | https://blog.gtowizard.com/gto_wizard_ai_3_way_benchmarks/ | verified_primary | 2026-06-05 | GTO Wizard | 3-way 多人解 benchmark + bunching effect 支持 |
| T02-S007 | https://blog.gtowizard.com/now_live_3_way_solving_nodelocking_2_0_and_50k_icm_ft_sims/ | verified_primary | 2026-06-05 | GTO Wizard | 3-way 解 / Nodelocking 2.0 / 50k+ ICM FT 上线 |
| T02-S008 | https://blog.gtowizard.com/major-upgrade-gto-reports-have-arrived-plus-tons-of-new-features/ | verified_primary | 2026-06-05 | GTO Wizard | GTO Reports：自动 leak 检测（色块对比 GTO 频率） |
| T02-S009 | https://blog.gtowizard.com/hand-history-analyzer-is-here-patch-notes/ | verified_primary | 2026-06-05 | GTO Wizard | Hand History Analyzer 上线 patch notes |
| T02-S010 | https://github.com/bupticybee/TexasSolver | verified_primary | 2026-06-05 | bupticybee | 开源 NLHE/短牌 solver，跨平台；stars 2429 |
| T02-S011 | https://github.com/b-inary/postflop-solver | verified_primary | 2026-06-05 | b-inary (Wakui) | Rust DCFR postflop solver，唯一开源支持 bunching；stars 354；开发暂停 |
| T02-S012 | https://github.com/b-inary/wasm-postflop | verified_primary | 2026-06-05 | b-inary (Wakui) | 浏览器端开源 GTO solver (WASM)；stars 573 |
| T02-S013 | https://github.com/google-deepmind/open_spiel | verified_primary | 2026-06-05 | Google DeepMind | 博弈 RL 研究库，含 poker CFR 环境；stars 5255 |
| T02-S014 | https://github.com/ericgjackson/slumbot2019 | verified_primary | 2026-06-05 | Eric Jackson | Slumbot CFR 实现（AI 对战 benchmark 对手）；stars 170 |
| T02-S015 | https://arxiv.org/abs/2106.06068 | verified_primary | 2026-06-05 | Brown et al. | "Subgame solving without common knowledge"——node-lock 理论根基 |
| T02-S016 | https://arxiv.org/abs/2509.23747 | verified_primary | 2026-06-05 | (arXiv 2025) | "Beyond GTO: Profit-Maximizing Poker Agents"——剥削派 AI 新论文 |
| T02-S017 | https://www.piosolver.com/ | surrogate_primary | 2026-06-05 | PioSOLVER | vendor docs——本地 postflop solver 厂商官网 |
| T02-S018 | https://www.gtowizard.com/ | surrogate_primary | 2026-06-05 | GTO Wizard | vendor docs——训练/查询站官网（10M+ 预解树） |
| T02-S019 | https://hand2note.com/Help/hand2note-vs-other-tools | surrogate_primary | 2026-06-05 | Hand2Note | vendor docs——H2N vs HM3/PT4 厂商对比（含 import speed 基准） |
| T02-S020 | https://www.holdemresources.net/mttcalculator | surrogate_primary | 2026-06-05 | HRC | vendor docs——MTT ICM calculator，Monte Carlo / bunching |
| T02-S021 | https://www.icmizer.com/en/blog/node-locking-in-postflopizer-gto-solver/ | surrogate_primary | 2026-06-05 | ICMIZER | vendor docs——ICMIZER/Postflopizer node-lock 说明 |
| T02-S022 | https://upswingpoker.com/poker-tools-software/leak-buster/ | surrogate_primary | 2026-06-05 | Upswing Poker | vendor docs——Leak Buster 介绍 |
| T02-S023 | https://drivehud.com/leakbuster2/ | surrogate_primary | 2026-06-05 | DriveHUD | vendor docs——Leak Buster 2 集成（465+ leak，仅 NLHE 现金） |
| T02-S024 | https://www.pokernews.com/poker-tools/ | secondary | 2026-06-05 | PokerNews | 第三方工具总览（solver/HUD/calc 横评） |
| T02-S025 | https://www.mypokercoaching.com/holdem-manager-2-poker-tracker-4/ | secondary | 2026-06-05 | MyPokerCoaching | HM3 vs PT4 横评（Mac 原生支持差异） |
| T02-S026 | https://www.pokernews.com/news/2026/02/gto-wizard-launches-multiway-preflop-solver-50550.htm | secondary | 2026-06-05 | PokerNews | 报道：GTO Wizard 多人翻前解 up to 9 players（2026-02） |
| T02-S027 | https://pokerfuse.com/learn-poker/tools/poker-solvers/ | secondary | 2026-06-05 | Pokerfuse | solver 入门指南（Pio/GTO+/Monker 定位 + 定价） |
| T02-S028 | https://www.runitonce.com/poker-training/videos/node-locking-and-exploiting/ | secondary | 2026-06-05 | Run It Once | node-lock 教学视频（Pio 剥削工作流） |
| T02-S029 | https://www.poker.org/poker-strategy/pro-tips-with-james-sweeney-the-problem-with-node-locking-a1rY07C6ISPQ/ | secondary | 2026-06-05 | poker.org / J. Sweeney | "node-lock 的问题"——单点 lock ≠ 最大剥削（避坑一手吐槽） |
| T02-S030 | https://www.pokerstrategy.com/news/content/Solvers-show-you-how-to-exploit-too_124027/ | secondary | 2026-06-05 | PokerStrategy | solver 也能教剥削（GTO vs exploit 论点） |
| T02-S031 | https://help.gtowizard.com/analyze-mode-guide/ | secondary | 2026-06-05 | GTO Wizard Help | Analyze 模式上传 HH 指南 |
| T02-S032 | https://handhistorypoker.com/blog/software-en/pokersnowie-artificial-intelligence/ | secondary | 2026-06-05 | HisHands | PokerSnowie 神经网 AI 介绍 |
| T02-S033 | https://gtosensei.com/ | surrogate_primary | 2026-06-05 | GTO Sensei | vendor docs——移动端 vs AI 实战 GTO trainer |

> Manifest 说明：GTO Wizard 的 `blog.` 子域被 classifier 判 verified_primary（vendor-engineering blog 内容路径），按模板「厂商 /blog/ 内容路径优先取 verified_primary」保留；厂商**产品落地页 / Help admin 页**（piosolver.com、gtowizard.com 根、hand2note `/Help`、icmizer `/blog`、drivehud、gtosensei、upswing）一律降标 `surrogate_primary` + note 含 "vendor docs"，不冒充一手。G2/Capterra/Gartner/知乎/公众号/CSDN 全程未引用（硬黑名单）。verified_primary 占比 ≈ 16/33 ≈ 48%（接近 50% 红线；缺口因 poker 工具核心是闭源商业软件，一手以 arXiv AI 论文 + 厂商 blog + 开源 GitHub 撑起）。

---

## 总览（按 tier 分组）

### 必备（5 个 | 阈值：≥80% 认真牌手在用）

| 工具 | 一句话 | Decay | Sources |
|------|--------|-------|---------|
| PioSOLVER | 本地 postflop GTO solver，深析 / node-lock 的高阶事实标准，elite pros 主用 | low | T02-S017, T02-S027 |
| GTO Wizard | 浏览器训练/查询站 + 云端 AI solver，10M+ 预解树，已成「上手即用」事实标准 | low | T02-S004, T02-S018, T02-S026 |
| GTO+ | 最高性价比本地 solver（$75 一次性），NLHE+PLO4，速度近 Pio | low | T02-S027 |
| Hold'em Manager 3 / PokerTracker 4 | HUD + 手牌数据库，复盘 / 找 leak / 实时 HUD 的两大标准（PT4 唯一原生 Mac） | low | T02-S025, T02-S024 |
| Flopzilla / Equilab | 范围 vs 牌面纹理 + 权益计算，翻前/翻后范围直觉的入门必装（Equilab 免费） | low | T02-S024 |

### 场景特化（7 个 | 不同子方向用不同的）

| 工具 | 一句话 | 适合场景 | Decay | Sources |
|------|--------|---------|-------|---------|
| ICMIZER 3 | SNG/MTT 的 ICM + 推弃分析，还会扫你的 push/fold 历史指错 | MTT/SNG 后期、泡沫推弃 | low | T02-S021 |
| HoldemResources Calculator (HRC) | MTT ICM 计算，Monte Carlo + 全 bunching/blocker 还原 | 多人 ICM、决赛桌精算 | low | T02-S020 |
| PokerSnowie | 神经网（非穷举）poker AI，实时反馈 + 移动端学 GTO 直觉 | 无 solver 经验者建直觉、随时练 | medium | T02-S032 |
| Hand2Note | 动态/位置化 HUD，import 速度最快，重度多桌 grinder 取向 | 海量手数据库、动态 HUD | low | T02-S019 |
| Leak Buster 2 (DriveHUD) | 对照千万手赢家库扫 465+ leak，自动排最贵手复盘 | NLHE 现金自动找漏洞 | medium | T02-S022, T02-S023 |
| DTO / GTO Sensei / Postflop+ (移动 trainer) | 手机端 GTO drill，对 AI 实战 + 实时纠错 | 通勤/碎片时间练 spot | medium | T02-S033 |
| TexasSolver (开源) | 免费跨平台 NLHE/短牌 solver，预算敏感者的 Pio 替身 | 零预算自跑解、学解树 | medium | T02-S010 |

### 新兴（3 个 | 近 12-24 月起势）

| 工具 | 一句话 | Decay | Sources |
|------|--------|-------|---------|
| GTO Wizard AI（云端即时求解） | 任意 spot 秒级求解 + 偏差报告，2023-2025 把「自跑解」民主化 | medium | T02-S004, T02-S005 |
| GTO Wizard 多人/3-way 解 + GTO Reports | 多人翻前解 up to 9 人 + bunching；GTO Reports 自动 leak 检测 | high | T02-S006, T02-S007, T02-S008, T02-S026 |
| AI 辅助复盘 / 剥削派 AI（HH Analyzer 2.0、Profit-Max agents） | 上传 HH 自动比对 GTO 找 leak；学界从纯 GTO 转向 profit-max 剥削 agent | high | T02-S009, T02-S016 |

---

## 必备层（≥80% 认真牌手在用）

### 1. PioSOLVER

- **One-liner**: 本地运行的 postflop GTO solver——自定义范围 / 下注尺度 / rake，产出 EV 与频率，高阶版含 node-locking 做剥削测试；是高额局 elite pros 的事实标准。
- **Tier**: 必备
- **Maintainer / Owner**: PioSolver（piosolver.com，闭源商业）
- **License**: proprietary（$249 / $549 按版本；Edge 版含翻前）
- **Maturity signals**:
  - 行业地位：「the solver used by a lot of elite high-level pros」(T02-S027)
  - 与 GTO Wizard AI 对照：0.12% pot distance（GTO Wizard 自报，以 Pio 为精度基准）(T02-S004)
  - Activity: healthy（商业持续维护；GTO Wizard 3-way benchmark 仍以 Pio 为对照基线 T02-S006）
- **典型使用场景**: (a) 单一翻后 spot 深析（自定义 bet tree，读极化 vs 浓缩）；(b) node-lock 对手错误频率算最大剥削策略（T02-S028）；(c) 跑 aggregate report 看一类牌面的整体策略。
- **不适合 / 替代方案**: 不适合零预算 / 只想上手即用者（学习曲线陡、界面不友好）→ 上手用 GTO Wizard，预算敏感用 GTO+ 或开源 TexasSolver；不适合 PLO 多人 → 用 MonkerSolver。
- **生产案例**: GTO Wizard AI 研发把 PioSolver 当**求解精度金标准**对照（0.12% pot distance）(evidence: [T02-S004])。
- **近期变化（近 12 个月）**: 本地 solver 赛道整体被云端 AI（GTO Wizard AI）分流，但深度自定义 + node-lock 仍是 Pio 的护城河。
- **可信度**: high
- **Decay risk**: low（24+ 月仍是高阶本地 solver 基础设施，被显著取代概率 <20%）

### 2. GTO Wizard

- **One-liner**: 浏览器端 GTO 训练 / 查询站 + 云端 AI solver，10,000,000+ 预解博弈树即点即用——已成「认真学 GTO 第一站」的事实标准。
- **Tier**: 必备
- **Maintainer / Owner**: GTO Wizard（gtowizard.com；2023 并购 Ruse AI solver 团队）
- **License**: proprietary（订阅制）
- **Maturity signals**:
  - 「by far the most powerful in-browser poker solver…over 10,000,000 pre-solved game trees」(T02-S004, T02-S018)
  - 「the number one tool in the industry for learning GTO…used by beginners and professional poker players worldwide」(T02-S018)
  - GTO Wizard AI：up to 200bb、任意 bet size，平均 ~3 秒/街求解 (T02-S004)
  - Activity: healthy（2023-2026 持续上新：AI solver→3-way→多人翻前→GTO Reports）
- **典型使用场景**: (a) 查任意翻前/翻后 spot 的均衡策略（预解树秒出）；(b) Trainer 模式对 GTO drill；(c) 上传 HH 用 Analyze/GTO Reports 自动找 leak（T02-S008, T02-S031）。
- **不适合 / 替代方案**: 重度自定义解树 / 极端 SPR / 学术级精度 → 仍需本地 Pio；纯离线无网环境 → 本地 solver。
- **生产案例**: GTO Wizard AI 在 150k 手对 Slumbot 达 19bb/100；并发布 API portal 邀研究者复测（透明度）(evidence: [T02-S004])。
- **近期变化（近 12 个月）**: 3-way 解 + Nodelocking 2.0 + 50k+ ICM FT sims 上线（T02-S007）；多人翻前解扩到 9 人（2026-02，T02-S026）；GTO Reports 自动 leak 检测（T02-S008）。
- **可信度**: high
- **Decay risk**: low（已是行业基础设施；产品本身高速迭代但「站」的地位稳）

### 3. GTO+

- **One-liner**: 最高性价比的本地 solver（$75 一次性），覆盖 NLHE + PLO4，本地求解速度在同等硬件上接近 PioSolver，界面比 Pio 更友好。
- **Tier**: 必备
- **Maintainer / Owner**: GTO+（商业，闭源）
- **License**: proprietary（$75 一次性）
- **Maturity signals**:
  - 「best price-to-performance ratio in the market at $75 one-time…speed comparable to PioSolver on equivalent hardware」(T02-S027)
  - Activity: healthy（持续商业维护）
- **典型使用场景**: (a) 预算有限但想要本地 solver 全功能（自定义解树 + node-lock）；(b) 入门者从 Pio 的陡峭界面退一步；(c) 同时碰 PLO4 的玩家。
- **不适合 / 替代方案**: 需要 PLO 多人 / 翻前大树 → MonkerSolver；想完全免费 → TexasSolver / wasm-postflop。
- **生产案例**: WASM Postflop / PioSOLVER / GTO+ 三者测试结果近乎一致（社区横评，说明 GTO+ 求解精度达标）(evidence: [T02-S027])。
- **可信度**: high
- **Decay risk**: low（性价比定位稳固，本地 solver 长期需求在）

### 4. Hold'em Manager 3 (HM3) / PokerTracker 4 (PT4)

- **One-liner**: HUD + 手牌数据库追踪的两大标准——实时桌上 HUD 显示对手统计、桌下复盘找 leak；PT4 是唯一原生支持 Mac 的。
- **Tier**: 必备
- **Maintainer / Owner**: Hold'em Manager / PokerTracker（各自商业）
- **License**: proprietary（HM3 小注 $60 / 全注 $100；PT4 价位几乎一致）
- **Maturity signals**:
  - 「the industry standards for most players remain Poker Tracker 4 (PT4) and Hold'em Manager 3 (HM3)」(T02-S024, T02-S025)
  - PT4：「the industry standard for a decade」「native Mac support」(T02-S025)
  - HM3：自带内置数据库简化安装、降后台占用 (T02-S025)
  - Activity: healthy（两者均长期商业维护）
- **典型使用场景**: (a) 实时 HUD 显示对手 VPIP/PFR/3-bet 等做剥削决策；(b) 桌下复盘 session 找自己 leak；(c) 攒大样本数据库做 population read。
- **不适合 / 替代方案**: 动态/位置化 HUD + 最快 import → Hand2Note；自动 leak 排序 → 叠 Leak Buster；**禁 HUD 的牌房**（GGPoker 禁外挂 HUD、partypoker/Ignition 匿名桌）→ HUD 失效，转纯 solver 学习 (T02-S024)。
- **生产案例**: Leak Buster 2 直接读 PT4 / HM3 数据库做 leak 分析（生态依赖）(evidence: [T02-S023])。
- **近期变化（近 12 个月）**: 行业「HUD-less」趋势（保护娱乐玩家）；GGPoker 等强禁外置 HUD，压缩 HUD 适用面 (T02-S024)。
- **可信度**: high
- **Decay risk**: medium（工具本身稳，但**牌房禁 HUD 政策**是结构性逆风，12-24 月适用场景持续收缩——这是 decay 来源，非软件本身）

### 5. Flopzilla / Equilab（范围 + 权益工具）

- **One-liner**: 把范围摆到具体牌面上看「这个范围在这块 flop 上命中什么」+ 算权益——建立翻前/翻后范围直觉的入门必装（Equilab 免费）。
- **Tier**: 必备
- **Maintainer / Owner**: Flopzilla（商业，~$25）/ Equilab（PokerStrategy.com，免费）
- **License**: Flopzilla proprietary；Equilab 免费（proprietary freeware）
- **Maturity signals**:
  - 「Flopzilla…understand hand ranges and board textures…visualize hand distributions, calculate equities, examine hand type frequencies」(T02-S024)
  - 「Equilab is available for free for equity calculations…good option for budget-conscious players」(T02-S024)
  - 「most effective poker training software includes…Flopzilla for equity calculations」(T02-S024)
  - Activity: healthy（行业长青入门工具）
- **典型使用场景**: (a) 看一个范围在某 flop 的命中分布（顶对/听牌/空气比例）；(b) 快速算两手/两范围的权益对抗；(c) Equilab 的 range trainer 练读范围。
- **不适合 / 替代方案**: 需要均衡策略（不止权益）→ solver / GTO Wizard；多人 ICM 权益 → HRC。
- **生产案例**: 业内通用研究栈「PT/HM 追踪 + Flopzilla 权益 + PokerSnowie AI 反馈」三件套被反复点名 (evidence: [T02-S024])。
- **可信度**: high
- **Decay risk**: low（权益/范围基本工具，3+ 年稳定）

---

## 场景特化层（特定子方向用）

### 6. ICMIZER 3

- **One-liner**: SNG/MTT 的 ICM + 推弃（push/fold）分析器，用 ICM 与 ChipEV 模型；ICMIZER 3 还会扫你的 push/fold 手牌历史告诉你哪里该改。
- **Tier**: 场景特化
- **Maintainer / Owner**: ICMIZER（商业；首版 2012，迭代到 v3）
- **License**: proprietary（订阅）
- **Maturity signals**: 「around for over a decade…ICMIZER 3 studies your push/fold hand history and tells you where to improve」「first edition 2012」(T02-S021)；Activity: healthy。
- **典型使用场景**: MTT/SNG **后期短码推弃决策**、泡沫期 fold equity 计算、复盘历史推弃失误。
- **不适合 / 替代方案**: 多人复杂 ICM + bunching 精算 → HRC（Monte Carlo 更强）；现金局翻后 → Pio/GTO Wizard（ICM 在现金局无关）。
- **生产案例**: 「ICMizer & HRC used for analyzing late-stage MTT play and push-fold scenarios」(evidence: [T02-S021])。
- **可信度**: high | **Decay risk**: low（MTT 推弃刚需，10+ 年稳态）

### 7. HoldemResources Calculator (HRC)

- **One-liner**: MTT/SNG 的赛后 ICM 分析程序，多桌模式高精度 ICM（典型 ±0.01%），Monte Carlo 模式可算 >3 人且全还原 bunching / blocker。
- **Tier**: 场景特化
- **Maintainer / Owner**: HoldemResources（holdemresources.net，商业）
- **License**: proprietary
- **Maturity signals**: 「high-precision MTT ICM…within +/- 0.01%…Monte Carlo mode…takes into account all card-blocking effects, including fold ranges」(T02-S020)；Activity: healthy。
- **典型使用场景**: **多人 ICM 精算**（决赛桌、>3 人 all-in spot）、考虑 bunching 的现实化 MTT 分析。
- **不适合 / 替代方案**: 想要即点即用云端 + 训练一体 → GTO Wizard 的 ICM FT sims（50k+，T02-S007）；纯现金局 → 不需要 ICM 工具。
- **生产案例**: HRC 的多桌高精度 ICM 是 MTT 后期决策的业内基准工具 (evidence: [T02-S020])。
- **可信度**: high | **Decay risk**: low（MTT ICM 精算刚需）

### 8. PokerSnowie

- **One-liner**: 用神经网络（在数十亿手上训练，**非穷举** solver）打全 NLHE 的 poker AI，实时反馈 + 指出 leak 并给修正；含移动端，适合无 solver 经验者建 GTO 直觉。
- **Tier**: 场景特化
- **Maintainer / Owner**: PokerSnowie（商业）
- **License**: proprietary（订阅）
- **Maturity signals**: 「neural networks…trained on billions of hands to play comprehensive no-limit poker」「real-time feedback…fixes to leaks based on its GTO AI database」「2025 版加 MTT 训练 + ICM」(T02-S032)；Activity: healthy。
- **典型使用场景**: (a) 无 solver 基础者用 AI 对战 + 即时纠错建直觉；(b) 移动端碎片练；(c) 整局而非单 spot 的 GTO 近似反馈。
- **不适合 / 替代方案**: 要精确均衡频率 / 自定义解树 → Pio/GTO Wizard（Snowie 是神经网近似，非精确 solver）；高阶 node-lock 剥削 → Pio。
- **生产案例**: 业内研究栈把 PokerSnowie 列为「AI-driven real-time feedback」标准组件之一 (evidence: [T02-S024], [T02-S032])。
- **可信度**: medium（厂商/第三方介绍为主，精确度逊于穷举 solver）| **Decay risk**: medium（被 GTO Wizard AI 这类精确云解挤压，12-24 月地位可能下滑）

### 9. Hand2Note

- **One-liner**: 动态 / 位置化 HUD，import 速度业内最快（基准 "very high" vs PT4 "low" / HM3 "medium"），面向重度多桌 grinder。
- **Tier**: 场景特化
- **Maintainer / Owner**: Hand2Note（商业；2019-09 起基础版永久免费）
- **License**: proprietary（基础免费 + 付费档）
- **Maturity signals**: 「import speed rated 'very high'…PT4 'low'…HM3 'medium'」「positional and dynamic HUD options」(T02-S019)；Activity: healthy。
- **典型使用场景**: (a) 海量手数据库（import 速度成瓶颈时）；(b) 动态/位置化 HUD 做精细 population read；(c) 多桌高强度 grind。
- **不适合 / 替代方案**: Mac 用户 → 只能 PT4（H2N 仅 Windows）；只要稳定拖拽 HUD 不要复杂度 → PT4。
- **生产案例**: Hand2Note 自身横评以 import 速度 + 动态 HUD 作为对 HM3/PT4 的差异化卖点（vendor docs，需 ≥2 source 佐证，此处佐证为社区横评提及 H2N 为现代竞品 T02-S025）(evidence: [T02-S019], [T02-S025])。
- **可信度**: medium（核心基准来自 vendor docs）| **Decay risk**: medium（同样受牌房禁 HUD 逆风）

### 10. Leak Buster 2（集成于 DriveHUD）

- **One-liner**: 对照「数千万手赢家」库自动扫你 465+ 潜在 leak，按最贵手排序供一键复盘；**仅 NLHE 现金**。
- **Tier**: 场景特化
- **Maintainer / Owner**: DriveHUD / Leak Buster（商业）
- **License**: proprietary
- **Maturity signals**: 「compares to tens of millions of hands from winning players…465+ potential leaks…auto-sorting most costly hands」「integrated into DriveHUD…supports DriveHUD 2, PT4, HM2, HM3」(T02-S022, T02-S023)；Activity: healthy。
- **典型使用场景**: (a) NLHE 现金自动定位最烧钱的 leak；(b) 不想手动建 filter 的玩家；(c) 配 90+ 教学视频做针对性学习。
- **不适合 / 替代方案**: MTT / PLO → 不支持（仅 NLHE 现金 T02-S023）；要精确 GTO 偏差报告 → GTO Wizard GTO Reports。
- **生产案例**: Leak Buster 直接挂在 PT4/HM3 数据库上做 population-relative leak 分析 (evidence: [T02-S023])。
- **可信度**: medium | **Decay risk**: medium（被 GTO Wizard 自带 GTO Reports / HH Analyzer 蚕食）

### 11. DTO / GTO Sensei / Postflop+（移动端 GTO trainer）

- **One-liner**: 手机端 GTO drill app——直接对按 solver 最优策略行动的 AI 实战，所有动作实时分析并指错；DTO 偏 MTT/SNG 场景且可自定义码量/位置。
- **Tier**: 场景特化
- **Maintainer / Owner**: DTO Poker / GTO Sensei / ThinkGTO(Postflop+)（各自商业）
- **License**: proprietary（多为订阅 / 内购）
- **Maturity signals**: 「DTO…detailed MTT and SNG scenarios…control over stack sizes and table position」「GTO Sensei…play against AI playing GTO solver-based strategies…all actions analyzed in real-time」「ThinkGTO…trusted by over 15,000 active players」(T02-S033)；Activity: healthy。
- **典型使用场景**: (a) 通勤/碎片时间练 spot；(b) MTT/SNG 特定码量场景反复 drill（DTO）；(c) 移动端建肌肉记忆，回家再用桌面 solver 深挖。
- **不适合 / 替代方案**: 深度自定义解树 → 桌面 Pio/GTO+；要看完整 aggregate report → GTO Wizard 桌面。
- **生产案例**: 移动 trainer 群体（DTO/GTO Sensei/Postflop+）被列为 2025 主流移动 GTO 训练套件 (evidence: [T02-S033])。
- **可信度**: medium | **Decay risk**: medium（移动 trainer 赛道更替快，单个 app 易被替代）

### 12. TexasSolver（开源）

- **One-liner**: 完全免费、开源、跨平台（Win/macOS/Linux）的 NLHE + 短牌(6+) solver——预算敏感者的 Pio/GTO+ 替身，也用于学解树原理。
- **Tier**: 场景特化
- **Maintainer / Owner**: bupticybee（GitHub，开源）
- **License**: open（GitHub 开源；另有 TexasSolverGPU 分支 53 stars）
- **Maturity signals**:
  - GitHub stars: 2429（2026-06-05）
  - Last push: 2026-03-31（T02-S010）
  - First created: ~2021（社区长期维护）
  - Activity: healthy（仍在更新，且有 GPU 分支）
- **典型使用场景**: (a) 零预算自跑翻后解；(b) 学习 solver 解树 / CFR 机制；(c) 短牌(6+) 求解（小众变体）。
- **不适合 / 替代方案**: 求解速度 / 内存效率敏感 → 横评指 TexasSolver 「slow execution / poor memory efficiency」，转 Pio/GTO+/wasm-postflop (T02-S010 社区横评)；要 GUI 友好 + 云端 → GTO Wizard。
- **生产案例**: 「TexasSolver…completely free, open-source…NLHE and Short Deck…Windows/macOS/Linux」社区横评 (evidence: [T02-S010])。
- **可信度**: high（GitHub 元数据可核）| **Decay risk**: medium（开源维护活跃但性能落后商业 solver）

---

## 新兴层（近 12-24 月起势）

### 13. GTO Wizard AI（云端即时求解）

- **One-liner**: 任意 poker spot 秒级云端求解 + 偏差报告（前身 Ruse AI），2023-07 上线，把「自己跑 solver」从「装本地软件 + 等几小时」民主化为「浏览器秒出」。
- **Tier**: 新兴
- **Maintainer / Owner**: GTO Wizard（2023 并购 Ruse）
- **License**: proprietary（订阅）
- **Maturity signals**:
  - First public: 2023-07-19 announced（T02-S004）
  - 性能：up to 200bb、任意 bet size、~3 秒/街；19bb/100 vs Slumbot（150k 手）；0.12% pot distance vs PioSolver（T02-S004）
  - SPR 上限 125 保精度（T02-S004）
  - Activity: healthy（持续迭代到多人 / GTO Reports）
- **典型使用场景**: (a) 现场/赛后即时求解非标 spot（自定义范围/码量/bet tree）；(b) 用 AIVAT 等技术做低方差 benchmark；(c) 通过 API portal 让研究者复测（透明度）。
- **不适合 / 替代方案**: 完全离线 / 学术级可复现自定义 → 本地 Pio；极端 SPR>125 → 精度下降，转本地。
- **生产案例**: GTO Wizard AI 在公开 benchmark 击败顶级 LLM（GPT/Grok 等），19.4bb/100，用深度 RL + AIVAT (evidence: [T02-S004], [T02-S005])。
- **可信度**: high | **Decay risk**: medium（技术领先但迭代极快，18 月后形态可能大变，>20% 概率被自身新版显著改写）

### 14. GTO Wizard 多人/3-way 解 + GTO Reports

- **One-liner**: 多人翻前解扩到 9 人（2026-02）+ 3-way 解全还原 bunching effect；GTO Reports 自动比对你的统计与 GTO 频率，色块标 under-bluff/over-fold 等 leak。
- **Tier**: 新兴
- **Maintainer / Owner**: GTO Wizard
- **License**: proprietary（订阅）
- **Maturity signals**:
  - 3-way solving / Nodelocking 2.0 / 50k+ ICM FT sims 上线（T02-S007）
  - 多人翻前解 up to 9 players，full ring/short-handed/HU（2026-02，T02-S026）
  - 3-way 支持非对称码、side-pot、任意 rake、bunching effect（T02-S006）
  - GTO Reports：色块对比 GTO 频率，一键从 stat 跳到对应手；**当前仅现金局翻前**（T02-S008）
  - Activity: healthy（2025-2026 高频上新）
- **典型使用场景**: (a) 多人底池（multiway）翻前策略——历史空白区，刚被工具覆盖；(b) 决赛桌 ICM 海量 sim；(c) 自动 leak 报告（翻前现金）。
- **不适合 / 替代方案**: 多人翻后精细 + bunching → 开源 postflop-solver（唯一开源支持 bunching，但慢，T02-S011）；翻后 leak 报告 → 暂缺（GTO Reports 仅翻前现金，postflop「coming soon」T02-S008）。
- **生产案例**: GTO Wizard 3-way benchmark 公开报告求解质量（含 bunching）(evidence: [T02-S006], [T02-S007])。
- **可信度**: high | **Decay risk**: high（功能新、覆盖面还在快速扩，12 月内边界会大幅变化）

### 15. AI 辅助复盘 / 剥削派 AI（HH Analyzer 2.0、Profit-Max agents）

- **One-liner**: 上传 hand history 自动比对 GTO 标准找 leak（GTO Wizard HH Analyzer 2.0）；学界从「纯 GTO 均衡」转向「profit-maximizing 剥削 agent」(arXiv 2025)——AI 反哺人类剥削打法。
- **Tier**: 新兴
- **Maintainer / Owner**: GTO Wizard（HH Analyzer）/ 学界（arXiv 2509.23747）
- **License**: mixed（产品 proprietary；论文开放）
- **Maturity signals**:
  - HH Analyzer 上线 + 2.0「Redefining Precision」迭代（T02-S009）
  - "Beyond GTO: Profit-Maximizing Poker Agents for No-Limit Holdem"（arXiv 2025-09，T02-S016）——剥削派 AI 方向
  - Activity: healthy / 学界活跃
- **典型使用场景**: (a) 批量上传 session HH 自动定位最大 leak；(b) 研究/进阶者读 profit-max agent 论文理解「GTO 之外如何被剥削」。
- **不适合 / 替代方案**: 要人类可解释的针对性诊断 + 教学视频 → Leak Buster；纯均衡基线 → GTO Wizard 标准解。
- **生产案例**: GTO Wizard HH Analyzer 2.0 patch notes 公布上传 HH 自动 leak 流程 (evidence: [T02-S009]); arXiv profit-max agents 代表学界剥削转向 (evidence: [T02-S016])。
- **可信度**: medium（产品成熟但「AI 自动 leak」整体仍在早期；论文为方向信号非成品）| **Decay risk**: high（赛道最早期，6-12 月形态未定）

---

## 选型决策树

> 从「你打什么牌型 / 什么目的 / 预算与平台」分支。每节点挂 evidence。节点数 = 8。

### 决策树 A：你的核心目的是什么？

#### Branch 1: 我要**建立 GTO 直觉 / 上手即用、不想折腾本地软件**
→ 推荐: **GTO Wizard**（浏览器 10M+ 预解树秒查 + Trainer drill；行业「学 GTO 第一站」事实标准）(evidence: [T02-S004], [T02-S018])
→ 备选（无 solver 经验 / 想对 AI 整局练）: **PokerSnowie**（神经网近似 + 实时纠错）(evidence: [T02-S032])
→ 不推荐: 一上来就 **PioSOLVER**（界面陡、要自己搭解树，初学者劝退）(evidence: [T02-S027])

#### Branch 2: 我要**深度自定义求解 / node-lock 做剥削 / 学术级精度**
##### Branch 2a: 预算充足 + 要高阶 node-lock + aggregate report
→ 推荐: **PioSOLVER**（Edge 版含翻前；elite pros 主用；GTO Wizard AI 以它为精度金标准 0.12% pot distance）(evidence: [T02-S004], [T02-S027])
##### Branch 2b: 预算敏感但仍要本地全功能
→ 推荐: **GTO+**（$75 一次性，速度近 Pio，界面更友好，含 PLO4）(evidence: [T02-S027])
##### Branch 2c: 零预算 / 想学解树原理 / 要短牌
→ 推荐: **TexasSolver**（开源跨平台，stars 2429）或 **wasm-postflop**（浏览器开源），代价是速度/内存逊于商业 solver (evidence: [T02-S010], [T02-S012])

#### Branch 3: 我打的是 **MTT / SNG（有 ICM）** 而非现金局
##### Branch 3a: 后期短码推弃 + 想被指错历史
→ 推荐: **ICMIZER 3**（ICM+ChipEV，扫 push/fold 历史）(evidence: [T02-S021])
##### Branch 3b: 多人 ICM 精算 + 要 bunching / 决赛桌
→ 推荐: **HRC**（Monte Carlo，±0.01% ICM，全 blocker/bunching）或 **GTO Wizard 50k+ ICM FT sims**(evidence: [T02-S020], [T02-S007])
→ 注意: 现金局**完全不需要** ICM 工具（ICM 只在筹码有非线性价值时成立）

#### Branch 4: 我要**复盘找自己的 leak / 桌上看对手统计（HUD）**
##### Branch 4a: 标准 HUD + 数据库，且我用 **Mac**
→ 推荐: **PokerTracker 4**（唯一原生 Mac；十年标准）(evidence: [T02-S025])
##### Branch 4b: Windows + 要最快 import / 动态位置化 HUD
→ 推荐: **Hand2Note**（import "very high"，动态 HUD）(evidence: [T02-S019])
##### Branch 4c: 想要**自动**排 leak（NLHE 现金）
→ 推荐: **Leak Buster 2**（挂 PT4/HM3，465+ leak 自动排序）或 **GTO Wizard GTO Reports**（色块比对 GTO 频率，仅翻前现金）(evidence: [T02-S023], [T02-S008])
→ ⚠️ 前置检查: 你的牌房**是否禁 HUD**？GGPoker 禁外置 HUD、partypoker/Ignition 匿名桌 → HUD 失效，跳过 4a/4b，改纯 solver 学习 (evidence: [T02-S024])

#### Branch 5: 我主要在**手机上碎片时间练**
→ 推荐: **DTO**（MTT/SNG 场景，自定义码量/位置）/ **GTO Sensei** / **Postflop+**（对 AI 实战 + 实时纠错）(evidence: [T02-S033])
→ 工作流: 移动端 drill 建肌肉记忆 → 回桌面用 Pio/GTO Wizard 深挖具体 spot

#### Branch 6: 我要建**翻前/翻后范围直觉**（不必到求解级）
→ 推荐: **Flopzilla**（范围 × 牌面纹理可视化）+ **Equilab**（免费权益计算 + range trainer）(evidence: [T02-S024])
→ 升级路径: 范围直觉成形后 → GTO Wizard 看均衡频率

#### Branch 7: 我打**多人底池（multiway）/ 想要 bunching 还原**
→ 推荐: **GTO Wizard 多人/3-way 解**（翻前 up to 9 人 + bunching）(evidence: [T02-S006], [T02-S026])
→ 翻后多人 + 开源: **postflop-solver**（唯一开源支持 bunching，最多 4 个 folded player，但开启 bunching 显著变慢，且开发暂停）(evidence: [T02-S011])
→ 标注: 多人解是**历史空白区**，2024-2026 才被工具覆盖，decay high

#### Branch 8: 我想理解 **AI 如何超越人类 / GTO 的理论边界**（研究向）
→ 推荐: 读 **Libratus**(Science aao1733) + **Pluribus**(Science aay2400) 论文 + Noam Brown 主页 (evidence: [T02-S001], [T02-S002], [T02-S003])
→ 进阶: **OpenSpiel**（DeepMind 博弈 RL 库，stars 5255）跑 CFR；**arXiv profit-max agents** 看剥削派 AI 转向 (evidence: [T02-S013], [T02-S016])

---

## 避坑清单

- ❌ **不要把 solver 输出当死记硬背的「标准答案」背下来**：solver 给的是**针对特定输入假设**的均衡，换范围/码量/rake 全变；要学的是「为什么」（极化逻辑、MDF、阻断牌），不是「这手 flop 下注 33% 频率 0.62」这种点值。(evidence: [T02-S027], [T02-S030])
- ❌ **不要盲信 GTO 而无视对手**：GTO 是不可剥削基线，但真实利润来自剥削对手 leak；纯 GTO 对弱对手是「把钱留在桌上」。solver 也能教剥削——用 node-lock。学界已从纯 GTO 转向 profit-maximizing agent。(evidence: [T02-S016], [T02-S030])
- ❌ **不要以为单个 node-lock 就能得到「最大剥削」策略**：solver 假设对手在**其他所有节点仍打完美 GTO**，所以单点 lock 只在该点剥削且自身不被反剥削，不等于真实对手的整体最大剥削。多点/迭代 lock 才接近。(evidence: [T02-S029], [T02-S015])
- ❌ **不要 HUD 样本不足就下结论**：几十手的 VPIP/3-bet 是噪声不是 read；population read 要攒大样本（这也是 Hand2Note import 速度、HM/PT 数据库存在的意义）。小样本上「他 3-bet 100%」往往是 2/2 手。(evidence: [T02-S019], [T02-S024])
- ❌ **不要无视牌房禁 HUD 政策就买 HUD**：GGPoker 禁外置 HM/PT HUD、partypoker/Ignition 匿名桌——买了也用不上，且违规有封号风险；这类生态下重心应放 solver 学习而非实时 HUD。(evidence: [T02-S024])
- ❌ **不要在现金局套用 ICM 工具 / 在 MTT 后期用纯 ChipEV**：ICM 只在筹码价值非线性（锦标赛跳台/泡沫）时成立，现金局筹码=现金，用 ICMIZER/HRC 是错配；反之 MTT 泡沫期只看 ChipEV 不看 ICM 会过度冒险。(evidence: [T02-S021], [T02-S020])
- ❌ **不要付了高端 solver 却不会读结果**：买 PioSOLVER Edge 但只会看「哪个动作频率高」就照抄，等于浪费——价值在读懂范围构成、对比 node-lock 前后 EV 差。先用 GTO Wizard 的预解 + 教学建框架再上本地 solver。(evidence: [T02-S004], [T02-S027])
- ❌ **不要用过时 / 低精度工具下硬结论**：PokerStove 是历史工具（已被 Equilab/Flopzilla 取代）；TexasSolver 等开源 solver 横评有「执行慢、内存效率差」，跑大树/对精度敏感时结果可能不可靠，关键决策用商业 solver 复核。(evidence: [T02-S010], [T02-S024])
- ❌ **不要把神经网 AI（PokerSnowie）当精确 solver**：它是数十亿手训练的**近似**，给方向和直觉很好，但精确频率/边缘 spot 不如穷举 solver；要精确均衡用 Pio/GTO Wizard。(evidence: [T02-S032])

---

## Phase 2 提炼提示

**反复出现 ≥3 source 都强调的「工具选型原则」**（候选 playbook 规则）:
- **「上手即用云端站 → 本地深挖 solver」的双层学习栈**：GTO Wizard（建框架/查解）打底，PioSOLVER/GTO+（自定义/node-lock）深挖；几乎所有横评都把这两层并列推荐 (出现于: T02-S004 / T02-S018 / T02-S027)。
- **「学逻辑而非背点值」**：solver 是理解工具不是记忆库，跨多 source 一致 (出现于: T02-S027 / T02-S030 / T02-S029)。
- **「GTO 基线 + 剥削偏离」二元**：必备工具天然分两类——均衡求解（Pio/GTO Wizard）vs 剥削发现（HUD+Leak Buster+node-lock），二者缺一不可 (出现于: T02-S024 / T02-S030 / T02-S016)。

**显著的工具流派分裂**（候选 智识谱系条目）:
- **流派 A：solver 纯学院派 / GTO 自上而下**（代表工具: PioSOLVER、GTO+、GTO Wizard 解树、OpenSpiel；代表人物: Noam Brown / Sandholm 的 Libratus-Pluribus 谱系，Track 01 关联）——从博弈均衡出发，求不可剥削基线，信「先学对的，再学偏」。
  vs
- **流派 B：实战感觉 / 剥削自下而上**（代表工具: HUD(HM3/PT4/Hand2Note)、Leak Buster、node-lock 工作流、PokerSnowie 直觉、arXiv profit-max agents；代表人物: 牌局自下而上的剥削派 grinder）——从对手 leak 与真实 population 出发，信「GTO 是地板，钱在剥削里」。
  **张力**: GTO 派批剥削派「易被反剥削、样本噪声」；剥削派批 GTO 派「把钱留桌上、对弱场过度严谨」。node-lock 是两派的技术握手点（用 solver 算剥削）。

**新兴工具信号**:
- 当前活跃 / 上升的新工具数: 3（GTO Wizard AI 云解 / 多人-3way 解+GTO Reports / AI 辅助复盘+剥削派 AI）
- 出现 → 主流速度估计: ~12-24 个月（GTO Wizard AI 2023-07 上线，到 2025-2026 已成事实标准，约 18-24 月；多人解 2024→2026 进入产品，约 12-18 月）

**冷僻 / 信号薄弱自检**:
- 必备层 5 个（≥3 ✓）；场景特化 7 个（≥5 ✓）；新兴 3 个（≥2 ✓）——**三层全部达量**，工具栈维度**信号充足，非冷僻**。
- verified_primary 占比 ≈48%（略低于 50%）：因 poker 核心工具是**闭源商业软件**，一手主要靠 arXiv AI 论文 + 厂商 engineering blog + 开源 GitHub repo 撑起；厂商产品落地页一律标 surrogate_primary（vendor docs）未冒充一手。
- **诚实边界提示给 Phase 2.8**: (1) 工具对比的「采用率/份额」缺乏行业大型 survey 硬数据，多为横评定性描述（「industry standard」「elite pros use」），属 surrogate 共识非统计；(2) 闭源 solver 无 GitHub 客观指标，maturity 靠厂商自报 benchmark（如 GTO Wizard AI 19bb/100、0.12% pot distance 均为厂商发布）+ 第三方横评佐证；(3) 中文一手工具讨论极薄，本 track 全用英文一手（GitHub/arXiv/厂商 blog/英文横评），与 intake warning 一致。

**衰减最快的一节提示**: 新兴层（GTO Wizard 多人解 / GTO Reports / AI 辅助复盘）decay=high，6-12 月需复查；必备层（Pio/GTO Wizard/HM-PT/Flopzilla）decay=low，但 **HUD 类受牌房禁 HUD 政策结构性逆风**，适用场景在收缩——这是 decay 来源而非软件本身衰退，update 时重点核查牌房政策变化。
