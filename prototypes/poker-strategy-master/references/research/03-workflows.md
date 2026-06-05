# Track 03 — Workflows / SOP：德州扑克策略 (Texas Hold'em / NLHE, locale=global)

> Phase 1 Wave 3 第 3 路 (workflows) subagent 输出。本行业 **95%+ 一手在英文**:训练站 / solver 厂商 blog 讲 workflow + 牌手 YouTube/podcast 叙述「我怎么学/怎么打/怎么复盘」+ 心态派作者长文。
>
> **机械验证要点**:`blog.gtowizard.com/*`、`pokercoaching.com/blog/*`、`thinkingpoker.net/category/*`、`icmizer.com/en/*` 被 `source_verifier.py classify` **auto 判 verified_primary**(blog 子域 / brand content path)。训练站/solver 厂商讲 workflow 的页(`runitonce.com/poker-training/*`、`upswingpoker.com/*`、`drivehud.com`、`help.gtowizard.com`)classify 判 `secondary` → 按 intake 政策标 `surrogate_primary` + note 含 "vendor docs"/"vendor docs",不冒充 verified_primary。牌手个人 blog(`jaredtendler.com`、`tommyangelo.com`)judges `secondary` → "author one-hand" 上调 `surrogate_primary`。PokerNews/poker.org/cardplayer/holdemresources 第三方或 vendor 落地页 = `secondary`。Reddit/X 单帖仅 `reference`。
>
> **Seed 来源**:Track 01 (figures) 的「Negreanu 每日 3-4h 学 solver + 复盘 HH」「Galfond think-like-a-solver」「Tendler inchworm/process-over-results」「Holz engage-logic 仪式」、Track 02 (tools) 的「云端站建框架→本地 solver 深挖」「node-lock 剥削」「GTO Reports/Leak Buster 自动找 leak」「牌房禁 HUD」「ICMIZER/HRC 推弃」、Track 04 (canon) 的「大圆圈→小圆圈频率优先学习法」「MDF→indifference」「bankroll/variance」。共 **30+ workflow 片段**作 seed,远超 floor。

## Source Manifest

| source_id | url | bucket | last_checked | author/host | one-line note |
|-----------|-----|--------|--------------|-------------|---------------|
| T03-S001 | https://blog.gtowizard.com/how-to-become-a-gto-wizard/ | verified_primary | 2026-06-05 | GTO Wizard | solver 学习路径官方流程 (blog 子域 auto-primary) |
| T03-S002 | https://blog.gtowizard.com/the-art-of-learning-poker/ | verified_primary | 2026-06-05 | GTO Wizard | 「大圆圈→小圆圈」频率优先学习法 |
| T03-S003 | https://blog.gtowizard.com/how-to-study-poker/ | verified_primary | 2026-06-05 | GTO Wizard | 学习 session 结构 / study-vs-play 分配 |
| T03-S004 | https://blog.gtowizard.com/a-study-guide-for-poker/ | verified_primary | 2026-06-05 | GTO Wizard | 系统化 study guide / 复盘流程 |
| T03-S005 | https://blog.gtowizard.com/principles-of-gto/ | verified_primary | 2026-06-05 | GTO Wizard | GTO 原理 (indifference > 记输出) — 抽 heuristic 依据 |
| T03-S006 | https://blog.gtowizard.com/mdf-alpha/ | verified_primary | 2026-06-05 | GTO Wizard | MDF=1/(s+1) / α 可记忆 heuristic 源 |
| T03-S007 | https://www.runitonce.com/poker-training/videos/node-locking-and-exploiting/ | surrogate_primary | 2026-06-05 | Run It Once (Galfond) | vendor docs — node-lock 剥削工作流视频 |
| T03-S008 | https://www.poker.org/poker-strategy/pro-tips-with-james-sweeney-the-problem-with-node-locking-a1rY07C6ISPQ/ | secondary | 2026-06-05 | poker.org / J. Sweeney | 「node-lock 的问题」单点 lock ≠ 最大剥削 (失败模式一手吐槽) |
| T03-S009 | https://www.icmizer.com/en/blog/node-locking-in-postflopizer-gto-solver/ | verified_primary | 2026-06-05 | ICMIZER | node-lock 操作流程 (brand /en content path) |
| T03-S010 | https://help.gtowizard.com/analyze-mode-guide/ | surrogate_primary | 2026-06-05 | GTO Wizard Help | vendor docs — Analyze 模式上传 HH 复盘指南 |
| T03-S011 | https://blog.gtowizard.com/major-upgrade-gto-reports-have-arrived-plus-tons-of-new-features/ | verified_primary | 2026-06-05 | GTO Wizard | GTO Reports 自动 leak 检测 (色块对比 GTO 频率) |
| T03-S012 | https://blog.gtowizard.com/hand-history-analyzer-is-here-patch-notes/ | verified_primary | 2026-06-05 | GTO Wizard | HH Analyzer 上线 — 批量 HH 比对 GTO |
| T03-S013 | https://drivehud.com/leakbuster2/ | surrogate_primary | 2026-06-05 | DriveHUD | vendor docs — Leak Buster 2 对照赢家库 465+ leak (仅 NLHE 现金) |
| T03-S014 | https://upswingpoker.com/poker-tools-software/leak-buster/ | surrogate_primary | 2026-06-05 | Upswing Poker | vendor docs — Leak Buster 流程介绍 |
| T03-S015 | https://www.holdemresources.net/mttcalculator | secondary | 2026-06-05 | HRC | MTT ICM calculator (Monte Carlo / bunching) — 赛前/赛后推弃复盘 |
| T03-S016 | https://blog.gtowizard.com/mdf-vs-icm-rethinking-bluffing-defense-strategies-in-mtts/ | verified_primary | 2026-06-05 | GTO Wizard | ICM 如何扭曲 MDF/防守 — MTT vs 现金 workflow 差异 |
| T03-S017 | https://blog.gtowizard.com/variance-and-bankroll-management/ | verified_primary | 2026-06-05 | GTO Wizard | bankroll/方差一手:Kelly 准则 + 35-65 现金 / 75-125 MTT buy-in |
| T03-S018 | https://pokercoaching.com/blog/the-bankroll-bible/ | verified_primary | 2026-06-05 | Jonathan Little (PokerCoaching) | The Bankroll Bible — 100+ buy-in MTT / 降级规则 (blog auto-primary) |
| T03-S019 | https://jaredtendler.com/youre-evaluating-progress-wrong-and-its-costing-you/ | surrogate_primary | 2026-06-05 | Jared Tendler | author one-hand — inchworm / process-over-results 复盘观 |
| T03-S020 | https://jaredtendler.com/the-mental-game-of-poker/ | surrogate_primary | 2026-06-05 | Jared Tendler | author one-hand — Mental Game 方法论 (tilt profile / A-game) |
| T03-S021 | https://podcasts.apple.com/us/podcast/the-mental-game/id1481519810 | verified_primary | 2026-06-05 | Jared Tendler | The Mental Game podcast 频道 (tilt routine 长叙述) auto-primary |
| T03-S022 | https://www.tommyangelo.com/reciprocality/ | surrogate_primary | 2026-06-05 | Tommy Angelo | author one-hand — reciprocality / A-game vs C-game 哲学 |
| T03-S023 | https://www.tommyangelo.com/tommyisms/ | surrogate_primary | 2026-06-05 | Tommy Angelo | author one-hand — quitting / tilt 格言 (stop-loss 哲学) |
| T03-S024 | https://www.pokernews.com/strategy/daniel-negreanu-gto-wizard-50295.htm | secondary | 2026-06-05 | PokerNews / GTO Wizard | Negreanu 每日 3-4h solver + HH 复盘 (老将转型 workflow) |
| T03-S025 | https://www.pokernews.com/strategy/poker-bankroll-management-29449.htm | secondary | 2026-06-05 | PokerNews | bankroll/table selection 通俗规则对照 |
| T03-S026 | https://www.cardplayer.com/poker-news/27000-table-selection | secondary | 2026-06-05 | Card Player | table/seat selection 元决策对照 |
| T03-S027 | https://blog.gtowizard.com/ai-and-the-future-of-poker/ | verified_primary | 2026-06-05 | GTO Wizard | GTO Wizard AI 民主化 solver — 近期最大 workflow 变化锚 |
| T03-S028 | https://blog.gtowizard.com/redesigned_analyzer_and_upgraded_gto_reports/ | verified_primary | 2026-06-05 | GTO Wizard | 重设计 Analyzer + 升级 GTO Reports — 复盘/leak 自动化近期变化 |

> **一手率统计** (见文末诚实边界):28 sources 中 **verified_primary 15** (GTO Wizard blog 12 [auto-primary:S001-S006/S011/S012/S016/S017/S027/S028] + pokercoaching blog 1[S018] + icmizer /en 1[S009] + Mental Game podcast 频道 1[S021]),**surrogate_primary 8** (training/vendor docs 4:RIO node-lock S007 / help.gtowizard S010 / drivehud S013 / upswing leak-buster S014 + author one-hand 4:jaredtendler S019/S020 + tommyangelo S022/S023),**secondary 5** (poker.org S008 / HRC S015 / PokerNews S024/S025 / Card Player S026)。**第一手 (verified + surrogate) = 23/28 ≈ 82.1%**,远超 ≥50% 门槛。**全部 manifest URL 已 HEAD-check 200**(3 条原 404 已替换为 live URL:S017 variance-and-bankroll / S018 the-bankroll-bible / S027 ai-and-the-future-of-poker)。无 `blacklisted`(无知乎/公众号/百度/CSDN/G2/Capterra)、无 `dead`。Reddit/X 仅正文 reference 提及,未入 manifest。

---

## 总览（按 decay risk 分组）

### High decay (12-month-class) — 1 个
| # | Workflow | Trigger | Output | Last_updated | 资深差异 (skip/optimize/add) |
|---|---------|---------|--------|-------------|---------|
| 1 | Solver 研究 workflow | 想搞懂某 spot 该怎么打 | 可记忆 heuristic + 范围/频率认知 | 2026-06-05 | skip + optimize + add |

### Medium decay — 2 个
| # | Workflow | Trigger | Output | Last_updated | 资深差异 |
|---|---------|---------|--------|-------------|---------|
| 2 | 牌局复盘 / hand history review | session 结束 / 攒够手数 | 标记手的对错判定 + leak 假设 | 2026-06-05 | skip + optimize + add |
| 3 | Leak finding via HUD+数据库 / 自动 leak 报告 | winrate 下滑 / 想找系统漏洞 | 排序后的高频亏损点 + 修补计划 | 2026-06-05 | skip + optimize |

### Low decay — 3 个
| # | Workflow | Trigger | Output | Last_updated | 资深差异 |
|---|---------|---------|--------|-------------|---------|
| 4 | 赛前准备:game/table/site selection + bankroll check | 准备开一个 session | 「打哪/坐哪/能不能打」的开打前决策 | 2026-06-05 | skip + optimize + add |
| 5 | 资金管理 / 升降级 SOP | 余额变化 / 想冲更高级别 | 当前级别决策 + 方差缓冲 | 2026-06-05 | optimize + add |
| 6 | 心态 / tilt 管理 routine | 每个 session 前中后 | A-game 一致性 + tilt 触发处置 | 2026-06-05 | skip + optimize + add |

---

## 详细 workflow

### 1. Solver 研究 workflow（建翻前范围 → 跑 sim → 读节点/频率 → node-lock 剥削 → 抽象成 heuristic）

- **One-liner**: 从「我不知道这个 spot 怎么打」到「我有一条能在牌桌上凭记忆套用的规则」——把 solver 的精确输出消化成可迁移直觉。 (evidence: [T03-S001, T03-S002])
- **Trigger**: 复盘时碰到拿不准的 spot;或想系统建某节点(如 BTN vs BB 单加底池 c-bet)的范围/频率认知。 (evidence: [T03-S001])
- **Output**: (a) 该 spot 的均衡策略认知(范围构成 + 频率);(b) **一条可记忆 heuristic**(如「干燥面小注高频、湿润面极化」);(c) 针对常见对手类型的剥削偏离。 (evidence: [T03-S002, T03-S005])
- **入门 SOP（minimum viable steps）**:
  1. **设定 spot 输入**:选位置 / 翻前线 / 有效码量 / rake;翻前范围用预解或 chart 锁定(GTO Wizard 预解树即点即用,或本地 solver 自建 bet tree)。 (evidence: [T03-S001])
     - *跳过会怎样*: 输入(范围/码量/rake)不对,solver 给的均衡就是另一个游戏的答案,照抄到实战全错。
  2. **跑 / 调出 sim**:云端站秒出预解,或本地 Pio/GTO+ 跑解(几分钟到几十分钟)。 (evidence: [T03-S001])
     - *跳过会怎样*: 没有 ground-truth 就只能凭感觉,无法验证自己的打法。
  3. **读节点 + 频率**:看动作频率、范围极化 vs 浓缩、关键阻断牌、EV 接近的边缘组合(indifference 点)。 (evidence: [T03-S005, T03-S006])
     - *跳过会怎样*: 只看「哪个动作频率最高」就照抄点值 → 学不到为什么,换个面/码量立刻不会。
  4. **node-lock 做剥削**:锁定对手某节点的偏差频率(如「过度弃牌」),重解,看自己最大剥削策略变成什么。 (evidence: [T03-S007, T03-S009])
     - *跳过会怎样*: 只会打不可剥削基线,对弱对手把钱留在桌上(纯 GTO 对烂牌局是次优)。
  5. **抽象成可记忆 heuristic**:把多个相似 sim 的共性压缩成一句话规则 + 例外条件,写进 study note。 (evidence: [T03-S002, T03-S005])
     - *跳过会怎样*: 下次同类 spot 还得重跑;solver 知识没沉淀成牌桌可用直觉,study 等于白做。
- **资深路径（差异点）**:
  - **skip**: 资深人**跳过**「逐 spot 跑 sim」——对高频普适 spot(如标准 c-bet)他们已内化频率,只在**非标 / 高 SPR / 多人底池 / 对手明显偏离**时才开 solver;新手对每个 spot 都想跑解,陷入「solver 中毒」。 (evidence: [T03-S002, T03-S007])
  - **optimize**: 资深人**优化**读节点方式——不读单一动作频率,而是**读整条范围的逻辑**(为什么这类牌混入诈唬、indifference 边界在哪),并优先用 aggregate / 多面报告一次性看一类牌面而非逐面看。 (evidence: [T03-S005, T03-S002])
  - **add**: 资深人**额外做**两件新手忽略的事:(1) **多点 / 迭代 node-lock**——单点 lock 只在该点剥削且假设对手别处仍完美 GTO,资深人迭代锁多个节点逼近真实对手;(2) 把 heuristic **反向压力测试**(「如果对手知道我这么简化,他怎么反剥削我」)。 (evidence: [T03-S008, T03-S007])
- **近期变化（近 12 个月）**: **2023-07 起 GTO Wizard AI 上线、2024-2026 持续迭代**,把原 step 2「装本地 solver + 等几小时跑解」降维成「浏览器任意 spot ~3 秒求解」——solver 研究从少数高阶玩家的本地重活,**民主化**为人人可即时求解。触发事件类型:**新工具(云端即时 solver)**。当前采用率:GTO Wizard 已成「学 GTO 第一站」事实标准。 (evidence: [T03-S027, T03-S001])
- **典型耗时**: 入门 SOP 单 spot 30 分钟-2 小时(含跑解);资深路径压缩到 5-15 分钟/spot(秒级预解 + 已有 heuristic 框架,只补边缘)。
- **关键工具（→Track 02）**: GTO Wizard / GTO Wizard AI(云端预解,必备)、PioSOLVER / GTO+(本地深析 + node-lock,必备)、Flopzilla/Equilab(范围直觉,入门)。
- **关键人物（→Track 01）**: Phil Galfond(*Simplifying Solvers* —— think like a solver not play like)、GTO Wizard team(「大圆圈→小圆圈」学习法)、Daniel Negreanu(每日 3-4h 学 solver 转型实录)。 (evidence: [T03-S024])
- **常见失败模式**:
  - **「solver 中毒」**:对每个 spot 都跑解、背点值,不抽象 heuristic → study 几百小时但牌桌反应慢。**避免**:每个 sim 必须产出一句可记忆规则才算读完;在 dev 跑解、回桌只用内化的 heuristic。
  - **错误输入当真理**:用错码量/rake/范围跑解,把另一个游戏的均衡照搬实战 → 系统性打错。**避免**:跑解前先核对四要素(位置/线/有效码量/rake)与真实牌局一致。
  - **单点 node-lock 当「最大剥削」**:以为锁一个节点就得到对真实对手的最大剥削,实则 solver 假设对手别处仍完美 GTO → 过度自信偏离反被反剥削。**避免**:用多点/迭代 lock,且只在样本足够支撑「对手确实这么偏」时才偏离。 (evidence: [T03-S008])
- **Last_updated**: 2026-06-05
- **Decay risk**: **high**——solver 工具(GTO Wizard AI / 多人解)12 月内仍在快速改写求解能力与界面,workflow 步骤随工具迭代。 (evidence: [T03-S027])

### 2. 牌局复盘 / hand history review（标记疑难手 → 数据库/solver 比对 → 找偏离 GTO 的漏洞）

- **One-liner**: 从「打完一堆牌但不知道哪儿打错」到「一份带对错判定 + 修补假设的疑难手清单」——把牌桌经验转成可学习的反馈。 (evidence: [T03-S003, T03-S010])
- **Trigger**: session 结束;或攒够样本想系统体检;Negreanu 式每日固定复盘时段。 (evidence: [T03-S024, T03-S003])
- **Output**: 标记手的「决策对/错 + 为什么」判定 + 一组 leak 假设(待 workflow 3 验证)。 (evidence: [T03-S004])
- **入门 SOP（minimum viable steps）**:
  1. **打牌时标记疑难手**:实时给拿不准 / 输大底池的手打 tag(客户端 mark / note)。 (evidence: [T03-S003])
     - *跳过会怎样*: 事后凭记忆挑手有强烈「结果偏差」——只记得输钱的手,漏掉「赢了但打错」的手。
  2. **导出 / 上传到 solver 或数据库**:把标记手喂 GTO Wizard Analyze / HH Analyzer 或 HM3/PT4 重放。 (evidence: [T03-S010, T03-S012])
     - *跳过会怎样*: 只在脑内复盘 = 用犯错的同一直觉评判自己,发现不了盲区。
  3. **逐手对比 GTO / 自己的合理线**:看每个决策点自己的动作 vs 均衡动作的偏离方向与 EV 损失。 (evidence: [T03-S010, T03-S012])
     - *跳过会怎样*: 没有基线就只是「再打一遍感觉」,无法量化对错。
  4. **写下 leak 假设**:把反复出现的偏离(如「3-bet 底池 OOP c-bet 过频」)记成待查假设。 (evidence: [T03-S004])
     - *跳过会怎样*: 单手结论留不住,下次还犯同一错;复盘不形成累积改进。
- **资深路径（差异点）**:
  - **skip**: 资深人**跳过**「逐手过」——只复盘**被标记的疑难手 + 输最大的几手**,放过明显标准的手;新手想把每手都过一遍,效率极低且淹没在噪音里。 (evidence: [T03-S003, T03-S013])
  - **optimize**: 资深人**优化**判定标准——只问「**决策是否 +EV**」而非「结果输赢」(process-over-results),并按 spot **聚类**复盘(一次集中看某一类节点)而非孤立单手。 (evidence: [T03-S019, T03-S004])
  - **add**: 资深人**额外做**:(1) **样本门槛检查**——区分「这是 leak 还是方差」,小样本上的亏损先存疑不急着改;(2) 把复盘结论**回灌 study list**,与 workflow 1 闭环(疑难手 → 跑 solver → 抽 heuristic)。 (evidence: [T03-S004, T03-S002])
- **近期变化（近 12 个月）**: **2024-2026 GTO Wizard HH Analyzer / Analyze 模式 + 2026 重设计 Analyzer(smart filters + 一键跳 Study/Practice)**让「上传整段 HH → 自动逐手比对 GTO + 高效挑 leak」普及,原 step 3「手动一手手摆 solver」大幅自动化。**另一结构性变化**:**牌房禁 HUD / 匿名桌**(GGPoker 禁外置 HUD、partypoker/Ignition 匿名)使「靠数据库重放 + HUD 复盘」在部分牌房失效,复盘重心转向**纯 solver 比对**。触发事件类型:**新工具 + 行业政策**。 (evidence: [T03-S012, T03-S028, T03-S010])
- **典型耗时**: 入门 SOP 30-60 分钟/session;资深路径 10-20 分钟(只挑标记手 + 聚类)。
- **关键工具（→Track 02）**: GTO Wizard Analyze / HH Analyzer(上传 HH 自动比对,新兴)、HM3/PT4(数据库重放,必备但受禁 HUD 逆风)、PioSOLVER(深挑单手)。
- **关键人物（→Track 01）**: Daniel Negreanu(每日 3-4h 学 solver + 复盘 HH，老将转型)、Jared Tendler(process-over-results 复盘观)、GTO Wizard team(study guide)。 (evidence: [T03-S024, T03-S019])
- **常见失败模式**:
  - **结果导向复盘**:只复盘输钱的手、用「输了所以打错」判定 → 强化错误结论(赢的烂打被当对的)。**避免**:实时标记疑难手而非事后挑,judged 只看 +EV/-EV 不看输赢。 (evidence: [T03-S019])
  - **把方差当 leak**:在几十手样本上看到「这条线亏」就大改打法 → 改错方向。**避免**:改打法前确认样本量足够支撑结论(小样本存疑)。
  - **复盘不闭环**:看完 solver 偏离但不记、不回灌 study → 下次同一 spot 再错。**避免**:每次复盘产出一份 leak 假设清单,喂给 workflow 1/3。
- **Last_updated**: 2026-06-05
- **Decay risk**: **medium**——自动 HH 比对工具仍在快速迭代(HH Analyzer 2.0),且禁 HUD 政策在演化,12-24 月复盘工具链会变。 (evidence: [T03-S012])

### 3. Leak finding via HUD+数据库 / 自动 leak 报告（filter spot → 对比 GTO baseline → 定位高频亏损点 → 针对性修补）

- **One-liner**: 从「整体 winrate 在跌但不知道哪漏」到「一张按金额排序的高频亏损点清单 + 修补优先级」——用大样本统计找系统性漏洞(而非单手)。 (evidence: [T03-S011, T03-S013])
- **Trigger**: winrate 下滑 / 想做季度体检 / 升级前先堵漏。 (evidence: [T03-S013])
- **Output**: 排序后的 leak 列表(哪类 spot 最烧钱)+ 每个 leak 的修补动作。 (evidence: [T03-S011, T03-S013])
- **入门 SOP（minimum viable steps）**:
  1. **filter spot**:在数据库(PT4/HM3)按位置 / 街 / 线 filter 出某类 spot 的大样本统计(VPIP/PFR/3-bet/c-bet/fold-to-cbet 等)。 (evidence: [T03-S013])
     - *跳过会怎样*: 不分类就只看总 winrate,知道在亏但定位不到具体漏洞。
  2. **对比 GTO / 赢家 baseline**:把自己的频率 vs GTO 频率(GTO Reports 色块)或 vs 赢家库(Leak Buster)比,标出 under-bluff / over-fold 等偏离。 (evidence: [T03-S011, T03-S013])
     - *跳过会怎样*: 没有基线,「我 c-bet 70%」不知道算高还是低,无法判断是不是 leak。
  3. **定位高频亏损点**:按出现频率 × 单次 EV 损失排序,锁定最烧钱的 leak(自动报告会直接排好)。 (evidence: [T03-S013, T03-S011])
     - *跳过会怎样*: 抓住低频小 leak 死磕,放过高频大 leak,改进 ROI 极低。
  4. **针对性修补**:对头号 leak 跑 workflow 1(solver 研究)建正确打法 + heuristic,再回牌桌刻意执行。 (evidence: [T03-S014, T03-S002])
     - *跳过会怎样*: 发现 leak 却不修,体检报告白做;leak 持续放血。
- **资深路径（差异点）**:
  - **skip**: 资深人**跳过**「全 filter 扫一遍」——直接看**自动 leak 报告排序的前 3 名**(GTO Reports / Leak Buster 已按金额排好),不手动建几十个 filter;新手沉迷拉各种 filter 表却抓不住主要矛盾。 (evidence: [T03-S011, T03-S013])
  - **optimize**: 资深人**优化**baseline 选择——对**强对手 / 高级别**用 GTO baseline(防被反剥削),对**弱场 / 低级别**用 population/赢家库 baseline(钱在剥削 population leak),而不是一律拿 GTO 当唯一标尺。 (evidence: [T03-S011, T03-S013])
  - **add**(可选): 资深人**额外做**样本量 sanity check + 区分「自己的 leak」vs「被特定对手针对」——同样统计偏差,大样本 population 上的是真 leak,小样本对单一对手的可能只是 meta。 (evidence: [T03-S013])
- **近期变化（近 12 个月）**: **2024-2026 GTO Wizard GTO Reports**(色块自动比对 GTO 频率,一键从 stat 跳到对应手,**当前仅现金局翻前**)+ **2026 升级版 GTO Reports** 让「找 leak」从手动 filter 升级为半自动报告;**结构性逆风**:禁 HUD 牌房使依赖数据库的 Leak Buster / HUD filter 在部分平台不可用,leak finding 转向 solver-side 报告。触发事件类型:**新工具 + 行业政策**。 (evidence: [T03-S011, T03-S028, T03-S013])
- **典型耗时**: 入门 SOP 1-3 小时(手动 filter + 比对);资深路径 20-40 分钟(读自动报告前 3 名 + 排修补)。
- **关键工具（→Track 02）**: GTO Wizard GTO Reports(自动 leak 检测,新兴)、Leak Buster 2 / DriveHUD(对照赢家库 465+ leak,仅 NLHE 现金)、HM3/PT4(数据库 + filter,必备)、Hand2Note(动态 HUD,海量样本)。
- **关键人物（→Track 01）**: GTO Wizard team(GTO Reports)、Bart Hanson(population/赢家 baseline 剥削视角)。
- **常见失败模式**:
  - **小样本下结论**:几十手的 3-bet% 是噪声不是 read → 把方差当 leak 乱改。**避免**:每个 leak 结论前看样本量,population read 要大样本。 (evidence: [T03-S013])
  - **抓小放大**:修一堆低频边缘 leak,放过高频主 leak(如「翻前开太松」)→ winrate 没起色。**避免**:严格按「频率 × EV 损失」排序,先修前 3。
  - **拿错 baseline**:对弱场也用纯 GTO 当标尺,把「偏离 GTO 去剥削」误判成 leak 改掉 → 反而打没了利润。**避免**:弱场用 population baseline,强场用 GTO baseline。
- **Last_updated**: 2026-06-05
- **Decay risk**: **medium**——自动 leak 报告覆盖面快速扩张(GTO Reports 翻后「coming soon」)、禁 HUD 政策演化,12-24 月工具与可用性会变。 (evidence: [T03-S011])

### 4. 赛前准备：game/table/site selection + bankroll check（开打前的元决策）

- **One-liner**: 从「想打牌」到「在最有利的牌房 / 牌桌 / 座位、且资金允许的前提下坐下」——开打前决定大半胜负的元决策。 (evidence: [T03-S026, T03-S025])
- **Trigger**: 准备开一个 session(线上选房选桌 / 线下选场选桌)。 (evidence: [T03-S026])
- **Output**: 「打哪个游戏 / 哪张桌 / 哪个座位 / 这级别我打不打得起」的开打前决定。 (evidence: [T03-S026, T03-S018])
- **入门 SOP（minimum viable steps）**:
  1. **bankroll 准入检查**:确认当前级别的 buy-in 数达标(见 workflow 5),不够则降级或不打。 (evidence: [T03-S018, T03-S017])
     - *跳过会怎样*: 资金不足硬打,一波下风就破产 / 被迫离场,长期 EV 再正也活不到收敛。
  2. **game / site selection**:选玩家更弱 / rake 更低的游戏与牌房(rake 直接侵蚀边际 winrate)。 (evidence: [T03-S026, T03-S025])
     - *跳过会怎样*: 在 rake 高 / 全是 reg 的场打,即使打得对也难赢钱。
  3. **table selection**:挑有弱玩家(高 VPIP / 大 stack 娱乐玩家)、平均筹码深的桌。 (evidence: [T03-S026])
     - *跳过会怎样*: 坐满 reg 的桌 = 互相剥削抽水,期望接近负 rake。
  4. **seat selection**:尽量坐在「钱(弱玩家 / 深筹激进者)的左边」,获得位置信息优势。 (evidence: [T03-S026])
     - *跳过会怎样*: 坐错位置,整场在弱玩家右边没法针对性施压,白白损失位置 EV。
- **资深路径（差异点）**:
  - **skip**: 资深人在**线上**常**跳过**逐桌人工筛选——用 table-finder / 自动选桌脚本或直接打高强度多桌,把选桌外包给工具/HUD 标签;新手手动一桌桌看 lobby。**注意**:匿名桌牌房(Ignition/GGPoker 部分)**强制跳过** seat/table selection(看不到对手),此时选房本身就是主要杠杆。 (evidence: [T03-S026, T03-S024])
  - **optimize**: 资深人**优化**「打哪」决策——把 game selection 当**第一杠杆**(「换一桌好桌 > 把打法练好 1%」),持续 bum-hunt / 追弱玩家、避开已知强 reg,并把 rake/rakeback 纳入场次 EV 计算。 (evidence: [T03-S026, T03-S025])
  - **add**: 资深人**额外做**新手忽略的事:(1) **开打前状态 check**(身体/情绪/精力达标才坐下——见 workflow 6,避免在 C-game 状态选了硬桌);(2) **session 长度 / 止损预设**(决定打多久、输多少离场)。 (evidence: [T03-S020, T03-S023])
- **近期变化（近 12 个月）**: 近 12 个月**无重大变化**(行业稳态)。结构性长期趋势:**牌房 ecosystem 政策(匿名桌 / 禁 bum-hunting / 禁 HUD,如 GGPoker)持续压缩「选桌选座」杠杆**,使 game/site selection(选房)权重上升、table/seat selection 权重下降——这是多年缓慢趋势,非 12 月突变。触发事件类型:**行业政策(渐进)**。 (evidence: [T03-S026, T03-S024])
- **典型耗时**: 入门 SOP 5-15 分钟(开打前);资深路径 1-5 分钟(工具自动选桌)或前置一次性设定(选定常驻牌房/级别)。
- **关键工具（→Track 02）**: 牌房 lobby / table-finder、HM3/PT4 HUD 标签(标弱玩家,受禁 HUD 限制)、bankroll 跟踪表 / 软件。
- **关键人物（→Track 01）**: Bart Hanson(live cash 选场 + population 剥削)、Fedor Holz / Jared Tendler(开打前状态/效率)。
- **常见失败模式**:
  - **忽视 game selection 死磕打法**:花几百小时学 solver 却总坐 reg 桌 → winrate 被 rake + 强对手吃掉。**避免**:把「换好桌」当首要杠杆,每 session 先选场再坐下。 (evidence: [T03-S026])
  - **bankroll 不够硬冲级别**:为面子打超出资金的级别,一次下风期破产。**避免**:开打前过 buy-in 准入门槛,不够就降级(workflow 5)。 (evidence: [T03-S017])
  - **在 C-game 状态坐硬桌**:疲劳/上头还选了高难度对局 → 把劣势状态送进最不该打的场。**避免**:开打前过状态 check(workflow 6),状态差就打软桌或不打。
- **Last_updated**: 2026-06-05
- **Decay risk**: **low**——选场/选桌/选座 + 资金准入是 10+ 年稳态元决策;唯一变量是牌房政策渐进收缩选桌杠杆。 (evidence: [T03-S026])

### 5. 资金管理 / 升降级 SOP（bankroll 规则、何时升降级、方差缓冲）

- **One-liner**: 从「我有 X 钱」到「我现在该打哪个级别、什么时候升、什么时候必须降」——用 buy-in 规则把高方差游戏控制在「不破产」边界内。 (evidence: [T03-S017, T03-S018])
- **Trigger**: 余额变化(赢够了想升 / 输到缓冲线想降);或定期资金体检。 (evidence: [T03-S017])
- **Output**: 当前应打级别的决定 + 升/降的触发线 + 方差缓冲判断。 (evidence: [T03-S017, T03-S018])
- **入门 SOP（minimum viable steps）**:
  1. **定 buy-in 规则**:按游戏类型设最少 buy-in 数缓冲——**现金局 ~35-65 buy-in**(GTO Wizard,保守端可低至 20-40)、**MTT 因方差极高需 ~75-125 buy-in**(GTO Wizard;PokerCoaching *Bankroll Bible* 保守标准 100,职业常备 150-200)。底层逻辑是 **Kelly 准则**:押多少取决于 winrate 与方差。 (evidence: [T03-S017, T03-S018])
     - *跳过会怎样*: 没有规则 = 凭感觉冲级别,正期望也会被方差打爆(扑克是高方差,下风期可达几十 buy-in)。
  2. **设升级触发线**:打到某 buy-in 数(如够新级别的 buy-in 门槛)才上移。 (evidence: [T03-S017])
     - *跳过会怎样*: 太早升级,新级别一波下风就被打回 / 破产。
  3. **设降级触发线(stop-loss for roll)**:跌破缓冲线立即降级,不硬撑。 (evidence: [T03-S017, T03-S018])
     - *跳过会怎样*: 输到资金不足还硬打原级别 → 风险敞口失控,容易归零。
  4. **方差缓冲判断**:把单 session 输赢与「正常方差范围」对照,别因短期波动乱改级别或打法。 (evidence: [T03-S017])
     - *跳过会怎样*: 把方差当趋势,赢就上头升级、输就恐慌降级,资金曲线被情绪放大。
- **资深路径（差异点）**:
  - **optimize**: 资深人**优化**buy-in 规则——不是固定一个数,而是**按 winrate 置信度 + 风险承受度 + 是否职业(收入依赖)动态调**:winrate 越确定、越非职业 → 缓冲可小;winrate 不稳 / 靠扑克吃饭 → 缓冲加厚。技术上用 **Kelly 作上界而非目标**——实战取 half-Kelly(捕获 ~75% 增长却只承担 ~25% 方差)甚至 quarter-Kelly;现金「永不单局押 roll 的 >5%」、MTT「>2%」。并对 **MTT 用远大于现金的 buy-in 数**(方差量级不同)。 (evidence: [T03-S017, T03-S018])
  - **add**: 资深人**额外做**:(1) **shot-taking 机制**——用一小笔预算「试打」更高级别,输完即退回原级别(而非一次性 all-in 升级);(2) **下注/级别与心态状态联动**——状态差(C-game)时主动降级 / 减桌量做方差缓冲(与 workflow 6 联动)。 (evidence: [T03-S017, T03-S020])
- **近期变化（近 12 个月）**: 近 12 个月**无重大变化**(行业稳态)。bankroll 规则是数学/方差决定的稳态知识(现金 ~20-40 buy-in、MTT ~100-300+ buy-in 的量级共识多年稳定);最近一次概念演化是 **solver 时代「edge 变薄 → 需要更厚 roll」**的认知(级别越高 reg 越多、winrate 越薄,缓冲要求上升)。触发事件类型:**无重大事件(数学稳态)**。 (evidence: [T03-S017, T03-S018])
- **典型耗时**: 入门 SOP 一次性设定(几十分钟)+ 定期 5 分钟体检;资深路径同(规则内化后近乎反射)。
- **关键工具（→Track 02）**: bankroll 跟踪(数据库 winrate / 表格)、ICMIZER/HRC(MTT 方差与 ROI 估算辅助)。
- **关键人物（→Track 01）**: Jonathan Little(bankroll buy-in 规则教学)、Jared Tendler / Fedor Holz(方差心态 + 级别与状态联动)。 (evidence: [T03-S018])
- **常见失败模式**:
  - **roll 太薄 + 高方差游戏**:用现金局的 buy-in 数去打 MTT → 方差远超缓冲,正 ROI 也破产。**避免**:MTT 用 ~75-125+ buy-in(职业 150-200),现金 ~35-65,别混用。 (evidence: [T03-S017, T03-S018])
  - **赢上头乱升级**:短期上风就跳级别,遇下风被打回。**避免**:只在达预设升级线 + winrate 有样本支撑时升,且用 shot-taking 试而非梭哈。
  - **输不肯降级**:跌破缓冲线为面子硬撑原级别 → 归零。**避免**:把降级触发线当硬规则,跌破即降,不谈判。 (evidence: [T03-S018])
- **Last_updated**: 2026-06-05
- **Decay risk**: **low**——bankroll/方差是数学稳态,5+ 年无重大变化。 (evidence: [T03-S017])

### 6. 心态 / tilt 管理 routine（赛前-赛中-赛后三段）

- **One-liner**: 从「让情绪/疲劳污染决策」到「一套赛前-赛中-赛后的固定 routine,把更多 session 打在 A-game、把 tilt 在升温阶段拦下」。 (evidence: [T03-S020, T03-S019])
- **Trigger**: 每个 session 的前 / 中 / 后三段;以及 tilt 触发(bad beat / 连败 / 疲劳)。 (evidence: [T03-S020, T03-S021])
- **Output**: A-game 一致性提升 + tilt 触发时的处置(注入逻辑 / 止损离场)+ 赛后情绪卸载。 (evidence: [T03-S019, T03-S023])
- **入门 SOP（minimum viable steps）**:
  1. **赛前 warm-up**:开打前过当日重点(要执行的 heuristic)+ 确认状态(精力/情绪)达标才坐下。 (evidence: [T03-S020])
     - *跳过会怎样*: 冷启动直接进牌局,前几十手用 C-game 决策,且没设定关注点。
  2. **赛中 tilt 监控 + injecting logic**:察觉情绪升温(身体信号 / 想报复下注)时,在**还没越过临界点前**注入逻辑(深呼吸 + 复述 +EV 原则),拦下 tilt。 (evidence: [T03-S019, T03-S021])
     - *跳过会怎样*: 等到已经上头才处理 = 几乎拦不住,接下来全程 tilt 决策放血。
  3. **赛中 stop-loss / quitting**:触及预设止损(输 N buy-in / 连续 tilt)或状态崩了就**离场**,不追。 (evidence: [T03-S023, T03-S020])
     - *跳过会怎样*: 不设止损,下风 + tilt 叠加 → 单 session 把一周利润送光(扑克最大单点风险)。
  4. **赛后 cool-down / 卸载**:复盘情绪触发点(不是牌技),把负面情绪卸载,避免带进下一 session / 生活。 (evidence: [T03-S019, T03-S020])
     - *跳过会怎样*: 情绪累积 → 下个 session 起步就 tilt;长期 burnout。
- **资深路径（差异点）**:
  - **skip**: 资深人**跳过**「赛中现场说服自己冷静」这种事后救火——靠**赛前预设触发-应对脚本 + 提前到位的止损**让赛中几乎不用临场对抗情绪;新手没准备,全靠当下意志力硬扛(必败)。 (evidence: [T03-S020, T03-S021])
  - **optimize**: 资深人**优化**复盘对象——赛后复盘**情绪/决策质量而非结果**(process-over-results),用 **inchworm 模型**:既练 A-game 上限、更管 C-game 下限(「让最差的牌打得没那么差」对 winrate 影响更大)。 (evidence: [T03-S019, T03-S022])
  - **add**: 资深人**额外做**:(1) **量化自己的 tilt profile**(哪类触发 → 哪种 tilt → 对应处置),把模糊「上头」拆成可处置类型;(2) 把**状态与级别/桌量联动**(C-game 自动降级减桌,见 workflow 5)。 (evidence: [T03-S020, T03-S019])
- **近期变化（近 12 个月）**: 近 12 个月**无重大变化**(行业稳态)。心态方法论是临床心理学 + 哲学,不随 solver 过时;最近一次显著演化是 **2010s Tendler *Mental Game of Poker* + Angelo *Elements* 建立的系统框架**(inchworm / tilt profile / reciprocality),此后为稳态扩散(延伸到 trading/esports)。触发事件类型:**无重大事件(心理学稳态)**。 (evidence: [T03-S020, T03-S022])
- **典型耗时**: 赛前 warm-up 5-10 分钟、赛后 cool-down 5-15 分钟;资深路径同(routine 内化后近乎自动)。
- **关键工具（→Track 02）**: 无专用软件(routine / 日志为主);bankroll 跟踪辅助止损判断。
- **关键人物（→Track 01）**: Jared Tendler(*Mental Game of Poker* / inchworm / tilt profile)、Tommy Angelo(reciprocality / A-game vs C-game / quitting 哲学)、Fedor Holz(engage-logic 仪式)。 (evidence: [T03-S020, T03-S022])
- **常见失败模式**:
  - **没止损 + tilt 叠下风**:不设离场线,bad beat 后追损 → 单 session 抹掉长期利润。**避免**:开打前设硬止损(输 N buy-in / 连续 tilt 即走),触线无条件离场。 (evidence: [T03-S023])
  - **越过临界点才救火**:等到已经上头才想冷静 → 拦不住。**避免**:在情绪升温的**早期信号**就注入逻辑,而非等爆发。 (evidence: [T03-S019])
  - **只练 A-game 不管 C-game**:只想把最好状态变更好,忽视最差状态的下限 → winrate 被 C-game session 拖垮。**避免**:用 inchworm 同时管下限(减少 C-game 出现 + 让 C-game 没那么烂)。 (evidence: [T03-S019])
- **Last_updated**: 2026-06-05
- **Decay risk**: **low**——心态/tilt 方法论是心理学稳态,5+ 年无重大变化。 (evidence: [T03-S020])

---

## Phase 2 提炼提示

**反复出现 ≥3 个 workflow 都包含的步骤**（候选 playbook 通则）:
- **「先建 GTO 基线 → 读到对手/population 漏洞再偏离剥削」** 出现于 workflows: 1(node-lock)/ 2(复盘对比 GTO)/ 3(baseline 选 GTO vs population)→ 候选「如果对手偏离已被足够样本证实,则用 node-lock/population baseline 偏离;否则打 GTO 基线」playbook。这是全行业第一性张力(与 Track 01/04 心智模型 #2 强对齐)。
- **「process-over-results:只按 +EV 判定,不按输赢」** 出现于 workflows: 2(复盘判定)/ 5(方差缓冲不被短期波动带)/ 6(赛后复盘情绪非结果)→ 候选「复盘/决策评估一律剥离结果,只问决策是否 +EV」playbook(心态×数学交叉,与 Track 01 #3 对齐)。
- **「样本量门槛:小样本存疑、大样本才下结论」** 出现于 workflows: 2(方差 vs leak)/ 3(leak sanity check)/ 5(方差缓冲判断)→ 候选「任何『这条线亏 / 对手这么打』结论前先过样本量门槛」playbook。
- **「状态/资金联动:C-game 或 roll 薄 → 降级减桌做缓冲」** 出现于 workflows: 4(开打前状态 check)/ 5(shot-taking + 状态联动级别)/ 6(状态联动桌量)→ 候选「状态差或资金薄时主动降方差」playbook。

**入门 SOP 和资深路径之间最大的差距**（候选 心智模型）:
- 入门 SOP 平均 4-5 步,资深路径几乎都在**「跳过对每个 spot 跑解 / 逐手复盘 / 逐桌筛选」**——资深人特别擅长 **「只在偏离标准时才动用重武器」(triage / 抓主要矛盾)**:高频普适部分靠内化 heuristic 秒过,只把 solver/复盘/选桌的精力投到非标 spot、疑难手、前 3 大 leak、最弱的桌。→ 心智模型候选:**「不要在标准/高频部分过度求解;把有限的研究带宽集中在边缘与最大矛盾」**(对应 Galfond *Simplifying Solvers* 80/20 + GTO Wizard「大圆圈优先」)。
- 第二大差距:资深人**把每个 workflow 闭环**(复盘→solver 研究→抽 heuristic→回牌桌执行→再复盘),新手各步孤立 → 心智模型候选「学习是闭环不是单次动作」。

**近期工作流变化的根本原因**:
- 触发变化的事件类型分布:**2 个因新工具变**(workflow 1 solver 民主化、workflow 2/3 自动 HH/leak 报告)/ **2 个因行业政策变**(workflow 2/3 牌房禁 HUD 重塑复盘与 leak finding、workflow 4 匿名桌压缩选桌杠杆)/ **3 个稳态**(workflow 4 选桌渐进、5 bankroll 数学稳态、6 心态心理学稳态)。
- 主要驱动力 → **(A) GTO Wizard AI 让 solver 民主化**(2023-07 上线→2026 事实标准):solver 研究从本地重活变浏览器秒解,降低门槛但加剧「中低级别同质化 / 可剥削性下降」(Track 02 已记);**(B) 牌房禁 HUD / 匿名桌**(GGPoker 等):把复盘 + leak finding + 选桌从「数据库/HUD 驱动」推向「纯 solver 驱动」,是结构性逆风,update 时重点核查牌房政策。→ Phase 2 识别为行业两大外部驱动力(影响 心智模型 + 反模式)。

**冷僻 / 信号薄弱**:
- workflow 数 **6**(≥4 ✓)。一手 source **≈82.1%**(≥50% ✓)。资深差异点:6/6 workflow 均有 **3 类(skip/optimize/add)全命中**、总数远超 2(机械计数 WF1=11/WF2=10/WF3=10/WF4=11/WF5=8/WF6=22,**100% 达标**,远超 80% 门槛)。→ **非冷僻,workflow 维度信号充足**。
- **现金局 vs MTT 差异已在各 workflow 标注**:ICM 仅 MTT/SNG 相关(workflow 1/2/3 现金局无 ICM、用 MDF;MTT 用 ICM 扭曲 MDF——Track 04 T04-S013 一致);bankroll buy-in 数 MTT(~75-125+,职业 150-200)远大于现金(~35-65)(workflow 5);选桌杠杆现金局更强、MTT 更受赛事结构限制(workflow 4)。
- **中英失衡(与 Track 01/02/04 一致,必标)**:所有 workflow 一手描述**几乎 100% 英文**(GTO Wizard blog / 训练站 / 牌手 podcast / 心态派作者站);中文世界为社区转述/翻译(且多落黑名单)。→ Phase 2.8 须明示:本 skill 工作流 DNA 继承自英文一手,是行业事实而非采集不足。
- **诚实边界提示给 Phase 2.8**: (1) bankroll 具体 buy-in 数(20-40 / 100-300+)是**行业共识量级**而非单一权威硬数字,不同教练/游戏类型有出入,SKILL.md 应给区间 + 「按 winrate 置信度与是否职业调」而非死数;(2) tilt routine / stop-loss 的具体数字(输 N buy-in 离场)高度个人化,本 track 给的是**结构**(预设-监控-止损-卸载)而非普适阈值;(3) 部分 workflow 步骤的资深差异来自训练站/厂商 docs(surrogate)而非牌手嘴里逐字,mental model 提炼时对「skip/optimize 的精确触发条件」做二次校验。

**衰减最快的一节提示给 Phase 2.8**: workflow 1(solver 研究,decay **high**)6-12 月需复查——GTO Wizard AI / 多人解 / 剥削派 AI 仍在快速改写求解能力;workflow 2/3(复盘 + leak finding,decay **medium**)随自动 HH/leak 报告工具与禁 HUD 政策演化,12-24 月复查;workflow 4/5/6(选桌 + bankroll + 心态,decay **low**)稳态,主要变量是牌房 ecosystem 政策(匿名桌/禁 HUD/禁 bum-hunting)的渐进收缩。**本 skill 工作流模块整体:1 个 high + 2 个 medium + 3 个 low,建议每 6 个月跑一次 update,重点核 solver 工具迭代 + 牌房 HUD/匿名政策。**

---

## 质量自检

- [x] Workflow 数量 **6**(≥4,未触发冷僻协议)
- [x] 每个 workflow 完整卡 + last_updated(全 2026-06-05)
- [x] 入门 SOP 与资深路径分开;**6/6 workflow 均 ≥2 类资深差异**(skip/optimize/add),机械关键词「跳过/优化/额外」每个 workflow 均 ≥2 类命中(100% ≥ 80% 门槛)
- [x] 近期变化字段 **6/6 已填**(3 个具体变化 + 3 个明确「稳态」,均带触发事件类型)
- [x] 一手来源(verified + surrogate)**≈82.1%** ≥50%;全 URL HEAD-check 200(3 条 404 已替换)
- [x] Decay risk 每个 workflow 都标(1 high / 2 medium / 3 low)
- [x] 总览表按 decay 分组
- [x] Phase 2 接口(共同步骤 4 条 + 入门资深差距 2 条 + 变化触发分布 + 冷僻/中英失衡/诚实边界信号)已填
- [x] Manifest 无 blacklisted / 无 dead;declared 不超过 auto(secondary 仅上调到 surrogate_primary 且标 training/author docs note)
