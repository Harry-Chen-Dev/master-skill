# Track 06 — Texas Hold'em / NLHE Glossary・术语 + 标准 + 行话 (locale=global, en-primary)

> Phase 1 Wave 1 第 3 路 subagent 输出。德州扑克策略 (NLHE) 是一个**几乎无监管标准、但行话密度极高**的行业 —— 术语 + 缩写 + register 占绝对大头,正式 "标准/认证" 几乎为零 (无执业认证、无 ISO、规则由各牌房私订)。因此本文件按 prompt 的「技术 + 创意混合」适配:**Term/Acronym 占 ~85%,Standard = 事实惯例 (de-facto conventions) 而非官方标准,Regulation/Certification = N/A**。
>
> **机械验证要点**:术语权威定义的一手来源是 `blog.gtowizard.com/*`(被 `source_verifier.py classify` **auto 判 verified_primary**,blog 子域启发式)+ 扑克 AI 论文 (Track 04 复用)。牌手/作者自营站 (jaredtendler.com / tommyangelo.com / thinkingpoker.net / philgalfond.com) classify 判 `secondary`,但属**作者一手讲术语 → 按 intake `surrogate_domain_whitelist_preemptive` 政策标 `surrogate_primary`**(note 含 "author one-hand")。训练站 glossary 页 (upswingpoker.com / pokernews.com / cardplayer.com / pokerstrategy.com)、Wikipedia 词条 = 老实标 `secondary`(术语入门定义,非一手生产)。
>
> Seed:Track 04 canon 30 核心概念 + Track 01 figures 高频黑话 + voice_samples 直接复用,本 track 补 outsider-tell / 厂商话术拒绝 / 事实惯例。

## Source Manifest

| source_id | url | bucket | last_checked | author/host | one-line note |
|-----------|-----|--------|--------------|-------------|---------------|
| T06-S001 | https://blog.gtowizard.com/poker-glossary/ | verified_primary | 2026-06-05 | GTO Wizard | 官方术语词条总表 (blog 子域 auto-primary) |
| T06-S002 | https://blog.gtowizard.com/mdf-alpha/ | verified_primary | 2026-06-05 | GTO Wizard | MDF & Alpha 权威定义 (1/(s+1)) |
| T06-S003 | https://blog.gtowizard.com/mathematical-misconceptions-in-poker/ | verified_primary | 2026-06-05 | GTO Wizard | pot odds/equity/MDF 常见外行误用源 (outsider-tell 金矿) |
| T06-S004 | https://blog.gtowizard.com/mdf-vs-icm-rethinking-bluffing-defense-strategies-in-mtts/ | verified_primary | 2026-06-05 | GTO Wizard | ICM 如何扭曲 MDF/防守 — cash vs MTT 分野 |
| T06-S005 | https://blog.gtowizard.com/the-art-of-learning-poker/ | verified_primary | 2026-06-05 | GTO Wizard | "频率优先 / 大圆圈→小圆圈" 学习法 register |
| T06-S006 | https://blog.gtowizard.com/spr-stack-to-pot-ratio/ | verified_primary | 2026-06-05 | GTO Wizard | SPR 定义与承诺度门槛 |
| T06-S007 | https://blog.gtowizard.com/understanding-board-texture/ | verified_primary | 2026-06-05 | GTO Wizard | wet/dry/connected board texture 定义 |
| T06-S008 | https://blog.gtowizard.com/the-theory-of-blockers/ | verified_primary | 2026-06-05 | GTO Wizard | blockers/removal 权威定义 |
| T06-S009 | https://blog.gtowizard.com/range-morphology/ | verified_primary | 2026-06-05 | GTO Wizard | polarized/condensed/merged/linear range 形态学 |
| T06-S010 | https://blog.gtowizard.com/run-it-twice/ | verified_primary | 2026-06-05 | GTO Wizard | run it twice 方差降低惯例 (不改 EV) |
| T06-S011 | https://blog.gtowizard.com/what-is-rake-in-poker/ | verified_primary | 2026-06-05 | GTO Wizard | rake 结构 (pot rake/time/cap) 与赢率侵蚀 |
| T06-S012 | https://blog.gtowizard.com/leveling-in-poker/ | verified_primary | 2026-06-05 | GTO Wizard | leveling / level-0..N 多层心理博弈 |
| T06-S013 | https://blog.gtowizard.com/the-fundamentals-of-poker-variance/ | verified_primary | 2026-06-05 | GTO Wizard | variance / bb/100 / 标准差 / 下行风险 |
| T06-S014 | https://blog.gtowizard.com/the-theory-of-poker-fundamental-theorem/ | verified_primary | 2026-06-05 | GTO Wizard | 基本定理 + 决策 vs 结果分离 |
| T06-S015 | https://blog.gtowizard.com/how-to-study-gto-solutions/ | verified_primary | 2026-06-05 | GTO Wizard | node-locking / exploitability / 如何读 solver |
| T06-S016 | https://www.science.org/doi/10.1126/science.aao1733 | verified_primary | 2026-06-05 | Brown & Sandholm (Science) | Libratus — exploitability/mbb/hand 口径一手 (复用 T04) |
| T06-S017 | https://papers.nips.cc/paper/3306-regret-minimization-in-games-with-incomplete-information | verified_primary | 2026-06-05 | Zinkevich et al (NeurIPS 2007) | CFR/Nash equilibrium 原始定义 (复用 T04) |
| T06-S018 | https://jaredtendler.com/youre-evaluating-progress-wrong-and-its-costing-you/ | surrogate_primary | 2026-06-05 | Jared Tendler | author one-hand — tilt/A-game/C-game/process-over-results 原话 |
| T06-S019 | https://www.tommyangelo.com/tommyisms/ | surrogate_primary | 2026-06-05 | Tommy Angelo | author one-hand — tilt/reciprocality 概念源 voice DNA |
| T06-S020 | https://www.philgalfond.com/articles/simplify-your-strategy | surrogate_primary | 2026-06-05 | Phil Galfond | author one-hand — "think like a solver, not play like" register |
| T06-S021 | https://www.thinkingpoker.net/play-optimal-poker/ | surrogate_primary | 2026-06-05 | Andrew Brokos | author one-hand — toy game / indifference / "GTO 是思维方式" |
| T06-S022 | https://en.wikipedia.org/wiki/Glossary_of_poker_terms | secondary | 2026-06-05 | — | 通用术语入门定义 (cooler/donk/nit/fish 等口语) |
| T06-S023 | https://en.wikipedia.org/wiki/Independent_Chip_Model | secondary | 2026-06-05 | — | ICM 术语入门定义 + 历史 |
| T06-S024 | https://upswingpoker.com/poker-terms-glossary/ | secondary | 2026-06-05 | Upswing Poker | 训练站术语表 (3-bet/c-bet/GII 等用法对照) |
| T06-S025 | https://www.pokernews.com/poker-terms/ | secondary | 2026-06-05 | PokerNews | 行业媒体术语库 (stakes 命名/buy-in 口语对照) |

> **一手率统计** (见文末诚实边界):25 sources 中 **verified_primary 17** (GTO Wizard blog 15 auto-primary + 扑克 AI 论文 2),**surrogate_primary 4** (作者自营站 "author one-hand": Tendler/Angelo/Galfond/Brokos),**secondary 4** (Wikipedia ×2 / Upswing glossary / PokerNews 术语库 — 均术语入门定义而非一手生产)。**第一手 (verified + surrogate) = 21/25 ≈ 84%**,远超 ≥50% 门槛。无 `blacklisted` (未碰知乎/公众号/百度/CSDN/Quora/Medium farm) / 无 `dead`。

---

## 总览（按 type 分组）

> **本行业 type 分布说明**:Term/Acronym 极多;**Standard = 事实惯例 (de-facto convention) 而非官方标准**;**Regulation = N/A**(博彩牌照法规属"开赌场"范畴,非"打牌策略";策略本身无监管);**Certification = N/A**(扑克无任何执业/教练认证,这本身就是一条 outsider-tell — 见 §B)。

### Tier 1 — 核心必懂 (18 个，目标 ≥16)

| 术语 (中文) | Type | Insider def (1 句) | Outsider tell | evidence |
|------|------|------|------|------|
| range 范围 | term | 某节点对手所有可能持牌的概率分布,不是单张牌 | 外行"把对手放在一张具体牌上" | T06-S001 |
| equity 权益/胜率 | term | 当前牌对某范围摊牌的胜率份额 (%) | 与 pot odds 混为一谈 | T06-S003 |
| EV 期望值 | acronym | 某决策长期平均收益 (bb/$),决策好坏的唯一标尺 | 用单局输赢评判决策对错 | T06-S014 |
| pot odds 底池赔率 | term | 跟注额÷(底池+跟注)=跟注所需最低胜率 | 当成"赢的概率"而非"所需胜率门槛" | T06-S003 |
| GTO / Nash 均衡 | acronym | 双方都无法单方面偏离获利的不可剥削策略 | 当成"无脑跟注/不会输的必胜法" | T06-S017 |
| exploitative 剥削 | term | 针对对手具体漏洞偏离均衡以最大化 EV | 不知道 GTO 与 exploit 是两种模式 | T06-S015 |
| polarized 极化范围 | term | 范围只含强牌(价值)+诈唬,无中等牌 | 不懂极化↔下注尺度的绑定关系 | T06-S009 |
| c-bet 持续下注 | acronym | 翻前加注者在翻牌继续下注 | 以为是"运气好才下注" | T06-S024 |
| 3-bet 再加注 | term | 翻前第三个加注动作 (4-bet/5-bet 类推) | 读成 "three bets" / 不懂层级语义 | T06-S024 |
| MDF 最低防守频率 | acronym | =1/(s+1),须防守此比例使 0% 权益诈唬无利 | 不知道有"该弃多少"的数学门槛 | T06-S002 |
| blockers 阻断牌 | term | 自己持牌减少对手某些组合的概率(removal) | 不懂"我这张牌让他更少有坚果" | T06-S008 |
| board texture 牌面结构 | term | 公共牌的湿/干/连张/同花面对范围交互的影响 | 只看自己成牌,不看牌面"打谁的范围" | T06-S007 |
| SPR 筹码底池比 | acronym | 有效筹码÷底池,决定承诺度与翻后策略 | 不知道 SPR 决定"能不能弃牌" | T06-S006 |
| ICM 独立筹码模型 | acronym | 把筹码换算为锦标赛奖金期望,扭曲 risk 取舍 | 把 MTT 当 cash 打,不懂泡沫期弃牌 | T06-S004 |
| variance 方差 | term | 短期结果围绕 EV 的波动 (扑克极高方差) | 把短期赢钱当"实力",输钱当"运气差" | T06-S013 |
| bankroll 资金盘 | term | 专用打牌资金 + 按级别的 buy-in 倍数底线 | 不懂破产风险,用生活费打 | T06-S013 |
| rake 抽水 | term | 牌房/平台抽成,直接侵蚀边际赢率 | 算 EV 时完全忽略 rake | T06-S011 |
| tilt | term | 任何偏离 A-game 的情绪化打法(哪怕轻微) | 以为 tilt 只是"上头梭哈" | T06-S019 |

### Tier 2 — 周边熟知 (20 个，目标 30-70 → 本行业术语集中,retained 20)

| 术语 (中文) | Type | Insider def | evidence |
|------|------|------|------|
| implied odds 隐含赔率 | term | 计入后续街可赢额外筹码的"有效赔率" | T06-S001 |
| 4-bet / 5-bet | term | 翻前第四/第五个加注 (5-bet 常 all-in 级) | T06-S024 |
| alpha (α) | term | 诈唬需对手弃牌的最低频率;α=1−MDF | T06-S002 |
| condensed / merged range 浓缩/合并范围 | term | 中等牌为主(浓缩) / 价值连续无明显诈唬(合并) | T06-S009 |
| linear range 线性范围 | term | 从最强到中强连续、无极化缺口的范围 | T06-S009 |
| range advantage 范围优势 | term | 整体范围更强(均权益更高) | T06-S001 |
| nut advantage 坚果优势 | term | 坚果/超强组合占比更高(允许 overbet) | T06-S009 |
| bluff-to-value 诈唬价值比 | term | 极化下注中诈唬︰价值的最优配比(随 sizing 变) | T06-S002 |
| indifference 无差异 | term | 均衡让对手某些牌在两动作间 EV 相等 | T06-S021 |
| overbet 超池下注 | term | 超过底池的注;极化+坚果优势时用 | T06-S009 |
| donk bet | term | 非翻前侵略方在被动位先下注(打破主动权) | T06-S001 |
| float 漂浮 | term | 弱牌跟注、计划后续街夺池 | T06-S024 |
| barrel 连续开火 | term | 连续多街持续下注施压(double/triple barrel) | T06-S001 |
| bubble / pay jump 泡沫/名次跳 | term | 钱圈泡沫期 / 奖金跳变,ICM 压力最大处 | T06-S004 |
| bb/100 赢率口径 | acronym | 每 100 手赢得的大盲数(行业统一赢率单位) | T06-S013 |
| GII (get it in) | acronym | 把筹码全押入池(常指"该不该 all-in") | T06-S001 |
| node-locking | term | 在 solver 中锁死对手某节点策略以求剥削解 | T06-S015 |
| leveling 层级博弈 | term | "我想他想我想…"的多层心理(level 0..N) | T06-S012 |
| run it twice (RIT) | term | 摊牌后发两次公共牌、各分半池以降方差(不改 EV) | T06-S010 |
| A-game / C-game | term | 最佳/最差状态打法;进步=拉高 A、抬高 C | T06-S018 |
| wet / dry board 湿/干牌面 | term | 听牌多(湿)/听牌少(干)的牌面 | T06-S007 |
| cooler | term | 双方都打对、但强牌撞更强牌的"必输局" | T06-S022 |

> Tier-2 实际列出 22 个 (含 wet/dry、cooler),超 floor。Tier-1 (18) + Tier-2 (22) = **40 个术语**,达上限。

### Standards / Conventions（事实惯例时间轴 — 本行业无官方标准/法规/认证）

| 名称 | 类型 | 何时成惯例 | Decay | evidence |
|------|------|-----------|-------|---------|
| bb/100 赢率口径 | de-facto convention | 在线扑克 tracker (PokerTracker/HM) 普及后(~2007+)成统一单位 | low | T06-S013 |
| stakes 命名 (NL50/NL200/NL500…) | de-facto convention | 在线现金局按 100bb buy-in 的 $ 额命名,长期稳定 | low | T06-S025 |
| buy-in / bankroll 倍数惯例 | de-facto convention | cash 20-40 buy-in、MTT 100-300 buy-in 的资金管理共识 | low | T06-S013 |
| run it twice (RIT) | de-facto convention | 高额桌降方差惯例;多数线上/线下高额局支持 | low | T06-S010 |
| solver 精度口径 (exploitability / pot distance) | de-facto convention | solver 普及后用 mbb/手 或 % pot 衡量"离均衡多远" | medium | T06-S016, T06-S015 |
| 牌房规则差异 (禁/允 HUD、匿名桌、rake 结构) | platform-specific | 各牌房私订,无统一标准(见 §D) | medium | T06-S011 |

> **Regulation 字段 = N/A**:扑克策略本身无监管(博彩牌照属"运营赌场"法规,与"如何打牌"无关)。**Certification 字段 = N/A**:扑克无任何官方执业/教练/选手认证 —— "持证扑克教练"不存在,谁声称有"扑克认证"即外行破绽 (见 §B)。

### 行业「外行破绽」高亮 (12 条最容易暴露的，详见 §B)

| 误用 | 内行实际意思 | 出现频率 |
|------|------------|---------|
| "GTO = 无脑跟注/不会输的必胜法" | GTO = 不可剥削**均衡基线**,对弱对手剥削 EV 更高 | 极高 |
| "我靠读牌天赋/读心术赢" | edge 主要来自范围+频率+选场+心态,读人是边际增量 | 极高 |
| 把对手放在"一张具体牌" | 内行想"范围分布",再随行动收窄 | 极高 |
| 不分离"决策对/结果错" | EV 是唯一标尺;单局输赢是方差噪音 | 极高 |
| 算 EV 时忽略 rake | rake 常吃掉中低级别一大块赢率,决定选场 | 高 |
| 把 cash 思路套 MTT (无视 ICM) | 泡沫/名次跳时该弃的牌远多于 cash | 高 |
| "solver/HUD = 作弊器" | solver 是离线学习工具;实时用才违规 | 高 |
| 把短期上分当"实力" | 高方差下样本不足,bb/100 要数万手才显著 | 高 |
| 混淆 pot odds 与 equity | 一个是"所需胜率门槛",一个是"实际胜率" | 中-高 |
| "MDF 必须严格执行" | 短筹/多人/ICM 下应主动偏离 MDF | 中 |
| 把 tilt 当"梭哈上头" | tilt = 任何偏离 A-game 的情绪化(含过紧/弃强牌) | 中 |
| 声称有"扑克认证/段位" | 扑克无官方认证;结果(赢率/战绩)才是凭据 | 中 |

---

## A. 高频术语详条 (按 tier，核心黑话含 register/etymology)

### range
- **tier-1**。**Type**: term。**中文**: 范围 / 手牌范围。
- **Insider def**: 一个玩家在某决策节点**所有可能持牌的概率分布**(含每种组合的频率),是扑克决策的"原子单位"。内行说话默认主语是 range 而非单张牌:"他这条线的 range 很 capped"。
- **Outsider-tell** (`usage_tell`):外行"把对手 put on a hand(放在一张具体牌)";内行 put on a *range*,再随每条街的行动**收窄**。Jonathan Little:"新手最大的错是把对手精确放在一手牌 —— 现实里他会用很多手牌打出同样的线" (evidence: [T06-S001, T06-S024])。
- **关联**: equity / range advantage / polarized / board texture。
- **可信度**: high / **Decay**: low (核心术语极慢)。

### equity
- **tier-1**。**Type**: term。**中文**: 权益 / 胜率份额。
- **Insider def**: 你的牌(或范围)对抗对手范围**摊牌时的胜率份额 (%)**;"我有 60% equity"= 全压摊牌长期赢 60%。
- **Outsider-tell** (`semantic_tell`):外行把 equity 与 **pot odds** 混为同一个数 —— 实则 equity = 我**实际**赢的概率,pot odds = 我跟注**所需**的最低胜率门槛;二者比较才决定跟不跟 (evidence: [T06-S003])。
- **关联**: pot odds / equity realization / EV。
- **可信度**: high / **Decay**: low。

### EV (expected value)
- **tier-1**。**Type**: acronym (full form: expected value)。**中文**: 期望值 / 期望收益。
- **Insider def**: 某决策的**长期平均收益**(以 bb 或 $ 计)。内行的世界观核心:"+EV 的决策长期必赢,哪怕这把输"。决策质量 = EV 正负,与单局结果**解耦**。
- **Outsider-tell** (`usage_tell`):外行用**单局输赢**评判决策对错("你跟了还输,所以你跟错了");内行问的是"这个跟注 +EV 吗",输赢只是方差。基本定理 (Sklansky) 的现代表述就是围绕 EV 而非结果 (evidence: [T06-S014])。
- **关联**: variance / pot odds / tilt (tilt = 让结果污染 EV 决策)。
- **可信度**: high / **Decay**: low。

### pot odds
- **tier-1**。**Type**: term。**中文**: 底池赔率。
- **Insider def**: 跟注额 ÷ (当前底池 + 你的跟注) = **跟注所需的最低胜率**。面对半池注需 ~25% equity 才能跟。
- **Outsider-tell** (`semantic_tell`):外行把 pot odds 当成"我赢的概率"或只会背"3:1"却不知拿来**和自己 equity 比**;还常忽略 **implied odds**(后续街能多赢的筹码)。GTO Wizard 专列此为"数学误用 top" (evidence: [T06-S003])。
- **关联**: equity / implied odds / MDF。
- **可信度**: high / **Decay**: low。

### GTO / Nash equilibrium
- **tier-1**。**Type**: acronym (Game Theory Optimal) / term (Nash 均衡)。**中文**: 博弈论最优 / 纳什均衡。
- **Insider def**: 一套**不可剥削的均衡策略** —— 双方都无法通过单方面偏离来提高自己的 EV。它是"基线/锚点",不是"必胜法":对**会犯错的对手**,剥削打法 EV 更高。
- **Outsider-tell** (`semantic_tell` + `register_tell`):**这一行最大的外行破绽**。外行把 GTO 理解成"无脑跟注 / 不会输 / 任何情况的最优打法";内行知道 GTO 只保证"不被剥削",对弱对手主动偏离 (exploit) 才赚最多。Doug Polk/Galfond 反复强调"GTO 是你回得去的锚点,不是终点";Bart Hanson 招牌反问:"对打得稀烂的对手,你干嘛要打完美平衡?" (evidence: [T06-S015, T06-S017])。
  - `pronunciation_tell`:读字母 "G-T-O" (✓) ;把它当一个产品名/某个"必胜公式"(✗)。
- **关联**: exploitative / indifference / MDF / node-locking。
- **可信度**: high / **Decay**: low (定义稳定;CFR/Nash 数学不过时)。

### exploitative play
- **tier-1**。**Type**: term。**中文**: 剥削打法 / 针对性打法。
- **Insider def**: 在读到对手**具体漏洞**(弃牌太多/跟注太松/诈唬不够)时,**偏离 GTO 均衡**以最大化 EV。与 GTO 是一对"基线↔偏离"的张力,不是对立面。
- **Outsider-tell** (`usage_tell`):外行不知道 GTO 与 exploit 是**两种可切换的模式**,以为"打好牌"只有一种;也常把"瞎激进"当 exploit。内行:exploit 必须基于**可观察的对手/人群倾向 (population tendencies)**,无证据的偏离是漏洞 (evidence: [T06-S015])。
- **关联**: GTO / node-locking / population tendencies / leveling。
- **可信度**: high / **Decay**: low。

### polarized range (vs condensed / merged)
- **tier-1**。**Type**: term。**中文**: 极化范围(对 浓缩/合并范围)。
- **Insider def**: 下注范围**只含强价值牌 + 诈唬**、几乎无中等牌 = polarized;此形态才"配得上"大注/overbet。浓缩 (condensed) = 中等牌为主;合并/线性 (merged/linear) = 从强到中连续。
- **Outsider-tell** (`usage_tell`):外行不懂**范围形态 ↔ 下注尺度**的绑定 —— 用大注却带一堆中等牌(该浓缩小注),或有坚果优势却小注(该极化 overbet)。Brokos 的 Clairvoyance Game 就是教极化的最小模型 (evidence: [T06-S009, T06-S021])。
- **关联**: overbet / bluff-to-value / nut advantage / range morphology。
- **可信度**: high / **Decay**: low。

### c-bet (continuation bet)
- **tier-1**。**Type**: acronym (continuation bet)。**中文**: 持续下注 / c 注。
- **Insider def**: 翻前的**加注方**在翻牌继续下注(延续翻前的主动权),是翻后最高频动作之一;频率/尺度随 board texture + range advantage 变。
- **Outsider-tell** (`pronunciation_tell` + `usage_tell`):内行说 "c-bet"(一个音"see-bet");外行说全称或当成"运气好才下注"。内行 c-bet 的决策依据是**整条范围在这个牌面的优势**,不是自己这手成没成牌 (evidence: [T06-S024, T06-S007])。
- **关联**: board texture / range advantage / barrel / float。
- **可信度**: high / **Decay**: low。

### 3-bet / 4-bet / 5-bet
- **tier-1**。**Type**: term。**中文**: 3-bet=再加注 / 4-bet=反再加 / 5-bet=(常)全下级加注。
- **Insider def**: 翻前加注的**层级**:开池(open)是第 1 个 bet → 第 2 次加注 = 3-bet → 4-bet → 5-bet(常 all-in)。"3-bet" 既是名词也是动词("I 3-bet him")。
- **Outsider-tell** (`semantic_tell`):外行把 "3-bet" 误读成"下注三次/three bets",不懂这是**翻前加注计数**(且从 bet 而非 raise 起算,易反直觉);也不知 3-bet **range** 该是极化(强牌+诈唬)还是线性。
- **关联**: range / polarized / 4-bet bluff / GII。
- **可信度**: high / **Decay**: low。

### MDF (minimum defense frequency)
- **tier-1**。**Type**: acronym (minimum defense frequency)。**中文**: 最低防守频率。
- **Insider def**: 面对 s 倍底池的下注,你须**继续(跟/加)的最低范围比例 = 1/(s+1)**,低于此则对手用 0% 权益的牌诈唬都自动盈利。配套 α = 1−MDF = 诈唬需要的弃牌率。
- **Outsider-tell** (`usage_tell`):外行根本不知道"该弃多少有个数学下限";或反过来把 MDF 当**铁律严格执行** —— 内行知道 MDF 是面对**极化**范围的防守上限工具,**短筹/多人/ICM 下应主动偏低于 MDF** (evidence: [T06-S002, T06-S004])。
- **关联**: alpha / indifference / pot odds / ICM。
- **可信度**: high / **Decay**: low (1/(s+1) 是恒等式)。

### blockers / removal
- **tier-1**。**Type**: term。**中文**: 阻断牌 / 去除效应。
- **Insider def**: 你**自己持有的牌**会减少对手拿到某些组合的概率(card removal)。"我有 A 阻断他的 AA 和 AK"→ 让诈唬/抓诈唬的选牌更优。
- **Outsider-tell** (`usage_tell`):外行只看自己牌力,不会**反推"我这张牌让对手少了哪些组合"**;高手选诈唬牌优先选"阻断对手坚果、不阻断对手诈唬"的牌 (evidence: [T06-S008])。
- **关联**: range / bluff-to-value / indifference。
- **可信度**: high / **Decay**: low。

### board texture
- **tier-1**。**Type**: term。**中文**: 牌面结构 / 公牌质地。
- **Insider def**: 公共牌的**质地** —— wet/湿(听牌多、连张、同花面) vs dry/干(彩虹、隔张),决定哪一方有 range/nut advantage、c-bet 频率与尺度。
- **Outsider-tell** (`usage_tell`):外行只问"我成牌没",内行先问"**这个牌面打谁的范围**"(谁的范围在这块牌更强)。不懂 texture → 在对自己范围不利的牌面乱开火 (evidence: [T06-S007])。
- **关联**: range advantage / c-bet / wet/dry board / SPR。
- **可信度**: high / **Decay**: low。

### SPR (stack-to-pot ratio)
- **tier-1**。**Type**: acronym (stack-to-pot ratio)。**中文**: 筹码底池比。
- **Insider def**: 翻牌时**有效筹码 ÷ 底池**。SPR 决定承诺度:低 SPR(<3)= 顶对都该全压、几乎弃不掉;高 SPR = 需要更强牌才承诺。是翻前 sizing 与翻后计划的桥梁。
- **Outsider-tell** (`usage_tell`):外行不知道 SPR 决定"**这手牌能不能弃**";常在低 SPR 时还想"控池",或高 SPR 用一对就梭。"commitment threshold(承诺门槛)"是内行词 (evidence: [T06-S006])。
- **关联**: pot odds / GII / board texture。
- **可信度**: high / **Decay**: low。

### ICM (Independent Chip Model)
- **tier-1**。**Type**: acronym (Independent Chip Model)。**中文**: 独立筹码模型。
- **Insider def**: 把**锦标赛筹码量换算成奖金期望 ($EV)** 的模型 —— 因奖池结构,筹码的边际价值递减,导致泡沫/名次跳时**该弃的牌远多于 cash**,MDF 等 cash 直觉失效。
- **Outsider-tell** (`semantic_tell`):**混淆 cash 与 MTT** 是核心外行破绽 —— 外行用现金局的"按 chipEV 全压"思路打锦标赛泡沫期,无视奖金跳变下的 risk premium。内行:"ICM 让你在泡沫期弃掉 cash 里必跟的牌" (evidence: [T06-S004, T06-S023])。
- **关联**: bubble / pay jump / MDF / risk premium。
- **可信度**: high / **Decay**: low。

### variance
- **tier-1**。**Type**: term。**中文**: 方差 / 波动。
- **Insider def**: 短期结果围绕 EV 的**波动**。扑克是**高方差**游戏:即使 +EV,数千手内也可能输;赢率 (bb/100) 要**数万手**才有统计显著性。
- **Outsider-tell** (`semantic_tell`):外行**把运气当实力** —— 短期赢钱归功于"水平高",输钱归咎"运气差",完全不懂样本量。内行:"你这 500 手的上分是噪音,给我看 50k 手的 bb/100" (evidence: [T06-S013])。
- **关联**: EV / bb/100 / bankroll / tilt / downswing。
- **可信度**: high / **Decay**: low。

### bankroll
- **tier-1**。**Type**: term。**中文**: 资金盘 / 牌资。
- **Insider def**: 专门用于打牌的**独立资金**,按级别有 buy-in 倍数底线(cash ~20-40 buy-in、MTT ~100-300 buy-in)以扛住方差不破产。"bankroll management (BRM)" 是生存前提。
- **Outsider-tell** (`usage_tell`):外行不懂**破产风险 (risk of ruin)**,用生活费打、赢了就升级别、输了就梭 —— 内行的 bankroll 是与生活账户严格隔离的"打牌弹药库" (evidence: [T06-S013])。
- **关联**: variance / bb/100 / stakes / risk of ruin。
- **可信度**: high / **Decay**: low。

### rake
- **tier-1**。**Type**: term。**中文**: 抽水 / 抽成。
- **Insider def**: 牌房/平台从每个底池(或按时)抽取的**佣金**(常 5% 封顶 cap)。它**直接侵蚀边际赢率**,是选场 (game selection) 的核心变量:高 rake 场会把本来小赢的玩家变成输家。
- **Outsider-tell** (`usage_tell`):外行算 EV / 谈赢率时**完全忽略 rake**,以为"打平 = 不输";内行知道 rake + 方差让"打平的玩家其实在缓慢失血",选低 rake 场 / 拿 rakeback 是赢率的一部分 (evidence: [T06-S011])。
- **关联**: bb/100 / game selection / rakeback / winrate。
- **可信度**: high / **Decay**: medium (各平台 rake 结构会调整)。

### tilt
- **tier-1**。**Type**: term。**中文**: 上头 / 情绪失控 (无精确中译,圈内直接说 "tilt")。
- **Insider def**: **任何偏离你 A-game 的情绪化打法,哪怕极其轻微**(Tommy Angelo 定义)。不止"上头梭哈" —— 还包括赢钱后松懈、怕输而过紧、报复性诈唬、弃掉该跟的牌。
- **Outsider-tell** (`semantic_tell`):外行以为 tilt 只是"输急了乱梭";内行知道 tilt 有**类型**(injustice tilt / revenge tilt / winner's tilt / 怕输 tilt),且"在情绪累积到阈值**之前**注入逻辑"才有效。"engage logic / inject logic" 是心态派内行词 (evidence: [T06-S019, T06-S018])。
- **关联**: A-game/C-game / variance / EV / reciprocality。
- **可信度**: high / **Decay**: low (心理学不随 solver 过时)。

---

### implied odds
- **tier-2**。**Type**: term。**中文**: 隐含赔率。
- **Insider def**: 在 pot odds 之外,**计入后续街还能从对手赢到的额外筹码**后的"有效赔率";听牌击中后能榨多少决定现在跟不跟。
- **Outsider-tell** (`usage_tell`):外行只算当前 pot odds 拒绝听牌,或反过来用"隐含赔率"合理化任何 loose call(忽略 reverse implied odds = 击中也可能输更多) (evidence: [T06-S003])。
- **关联**: pot odds / equity / reverse implied odds。**可信度**: high / **Decay**: low。

### alpha (α)
- **tier-2**。**Type**: term。**中文**: alpha / 诈唬所需弃牌率。
- **Insider def**: 诈唬要**即时盈利**所需对手弃牌的最低频率;α = 1 − MDF = s/(s+1)(面对 s 倍底池注)。与 MDF 是同一枚硬币两面。
- **Outsider-tell**:外行只凭"感觉他会弃"诈唬,不知有**量化门槛**;混淆 α(诈唬方视角)与 MDF(防守方视角) (evidence: [T06-S002])。
- **关联**: MDF / bluff-to-value / indifference。**可信度**: high / **Decay**: low。

### condensed / merged / linear range
- **tier-2**。**Type**: term。**中文**: 浓缩 / 合并 / 线性范围。
- **Insider def**: 范围**形态学** —— condensed=中等牌为主(缺顶端缺底端);merged/linear=从最强到中强连续无极化缺口。形态决定该用什么 sizing。
- **Outsider-tell**:外行只有"强/弱"二分,没有"形态"维度;不懂为何同样下注、不同形态要配不同尺度 (evidence: [T06-S009])。
- **关联**: polarized / nut advantage / overbet。**可信度**: high / **Decay**: low。

### range advantage / nut advantage
- **tier-2**。**Type**: term。**中文**: 范围优势 / 坚果优势。
- **Insider def**: range advantage=整体范围均权益更高;nut advantage=超强组合(坚果)占比更高。**nut advantage 是 overbet 的许可证**(只有坚果更多的一方才能用大注极化)。
- **Outsider-tell**:外行不区分"整体更强"与"坚果更多";没坚果优势却 overbet = 送钱 (evidence: [T06-S009, T06-S007])。
- **关联**: overbet / polarized / board texture。**可信度**: high / **Decay**: low。

### bluff-to-value ratio
- **tier-2**。**Type**: term。**中文**: 诈唬价值比。
- **Insider def**: 极化下注中**诈唬︰价值**的最优配比,使对手抓诈唬**无差异 (indifferent)**;比例随下注尺度变(注越大、诈唬可越多)。河牌经典:半池注 ≈ 2 价值 : 1 诈唬。
- **Outsider-tell**:外行要么从不诈唬(被打成透明),要么诈唬过多(被抓);不懂尺度↔比例的数学绑定 (evidence: [T06-S002])。
- **关联**: alpha / indifference / overbet / blockers。**可信度**: high / **Decay**: low。

### indifference
- **tier-2**。**Type**: term。**中文**: 无差异 / 漠然点。
- **Insider def**: 均衡的**本质机制** —— 通过精确的频率,让对手某些边缘牌在"跟/弃"(或"诈唬/放弃")之间 **EV 完全相等**,使其怎么选都不亏不赚,从而无法剥削你。
- **Outsider-tell**:外行不理解"让对手无差异"这一目标,以为博弈论是"算出唯一正确动作";内行知道均衡常是**混合策略**(同一手牌按比例跟/弃) (evidence: [T06-S021])。
- **关联**: GTO / MDF / bluff-to-value / mixed strategy。**可信度**: high / **Decay**: low。

### overbet
- **tier-2**。**Type**: term。**中文**: 超池下注。
- **Insider def**: 下注额**超过底池**(如 1.5×、2× pot)。solver 时代被证明是**极化范围 + 坚果优势**下的最优件;Janda(2013 前)主流视其为"业余动作"。
- **Outsider-tell**:外行 overbet 当"虚张声势吓人",随便用;内行只在有 nut advantage 的极化节点用,且诈唬含量随尺度提高 (evidence: [T06-S009])。
- **关联**: polarized / nut advantage / bluff-to-value。**可信度**: high / **Decay**: low。

### donk bet
- **tier-2**。**Type**: term。**中文**: donk / 反主动下注。
- **Insider def**: **非翻前侵略方**(上一条街的跟注方)在被动位**抢先下注**,打破"加注方先 c-bet"的常规主动权。名字源于 "donkey"(早期被视为鱼的动作),solver 平反了部分场景。
- **Outsider-tell** (`register_tell`):外行不知道这词带历史贬义,也不知现代 solver 在特定牌面(对跟注方范围有利的转牌)认可低频 donk;乱 donk 仍是漏洞 (evidence: [T06-S001])。
- **关联**: c-bet / board texture / range advantage。**可信度**: high / **Decay**: low。

### float
- **tier-2**。**Type**: term。**中文**: 漂浮 / 浮动跟注。
- **Insider def**: 用**弱牌/听牌跟注**,计划在后续街(对方放弃主动权时)**夺池**,利用位置 + 对手 c-bet 后的高放弃率。
- **Outsider-tell**:外行"跟着看看"无后续计划 = 不是 float;float 是**有夺池剧本**的跟注 (evidence: [T06-S024])。
- **关联**: barrel / c-bet / position / equity realization。**可信度**: high / **Decay**: low。

### barrel (double / triple barrel)
- **tier-2**。**Type**: term。**中文**: 开火 / 连续下注。
- **Insider def**: 连续多街持续下注施压;double barrel=翻牌+转牌连下,triple barrel=三街全下。诈唬 barrel 靠 board/equity 演变 + blockers 选牌。
- **Outsider-tell** (`usage_tell`):外行 barrel = "一路诈唬到底赌他弃",不挑 board/不挑牌;内行的 barrel 是**有 equity 或 blocker 支撑的施压** (evidence: [T06-S001, T06-S008])。
- **关联**: c-bet / float / blockers / bluff-to-value。**可信度**: high / **Decay**: low。

### bubble / pay jump
- **tier-2**。**Type**: term。**中文**: 泡沫期 / 名次奖金跳。
- **Insider def**: MTT 中**钱圈泡沫 (bubble)** = 再淘汰一人就进钱;**pay jump** = 名次上升带来的奖金跳变。两处 **ICM 压力最大**,大筹码可加压、短筹须自保。
- **Outsider-tell**:外行泡沫期照常激进(无视别人为保命过紧)、或自己短筹乱梭;不懂"泡沫期是施压套利窗口" (evidence: [T06-S004])。
- **关联**: ICM / risk premium / MDF。**可信度**: high / **Decay**: low。

### bb/100 (winrate)
- **tier-2**。**Type**: acronym (big blinds per 100 hands)。**中文**: 每百手大盲赢率。
- **Insider def**: 行业**统一赢率单位** —— 每 100 手赢得的大盲数。在线现金局 5bb/100 已是强赢率,2-3bb/100 算稳赢;**需数万手样本**才统计显著。
- **Outsider-tell**:外行用"赢了多少钱/赢了几次"谈水平,不知道跨级别可比的单位是 bb/100,也不懂样本量门槛 (evidence: [T06-S013])。
- **关联**: variance / bankroll / rake / sample size。**可信度**: high / **Decay**: low。

### GII (get it in)
- **tier-2**。**Type**: acronym (get it in)。**中文**: 全押入池 / 上车。
- **Insider def**: 把**筹码全押进底池**;"GII equity" = 全压那一刻的胜率。讨论"该不该 all-in"时的简写:"你这手 GII 好不好?"
- **Outsider-tell** (`pronunciation_tell`):内行说字母 "G-I-I" 或 "get it in";外行不识这缩写,把 all-in 决策只当"梭不梭",不算 GII equity vs 对手范围 (evidence: [T06-S001])。
- **关联**: equity / SPR / commitment threshold。**可信度**: high / **Decay**: low。

### node-locking
- **tier-2**。**Type**: term。**中文**: 节点锁定。
- **Insider def**: 在 solver 里**人为锁死对手在某节点的策略**(如"假设他这里从不诈唬"),让 solver 算出**针对该漏洞的剥削解** —— solver 时代"用 GTO 工具做 exploit"的标准方法。
- **Outsider-tell**:外行以为 solver 只能给"GTO 答案";不知 node-locking 把均衡工具变成剥削工具(GTO↔exploit 的技术桥) (evidence: [T06-S015])。
- **关联**: exploitative / GTO / population tendencies。**可信度**: high / **Decay**: low (medium: 工具能力演进)。

### leveling
- **tier-2**。**Type**: term。**中文**: 层级博弈 / 心理博弈。
- **Insider def**: "我想他想我想…"的**多层推理**(level 0 = 只看自己牌;level 1 = 想对手的牌;level 2 = 想对手怎么想我…)。"leveling war / over-leveling(想太多层把自己绕进去)"。
- **Outsider-tell** (`register_tell`):外行把 leveling 当"读心术"神化;内行知道**对弱对手别 over-level**(他根本没在想第 2 层,你想太多反而错) (evidence: [T06-S012])。
- **关联**: exploitative / population tendencies / GTO (反 leveling 锚)。**可信度**: high / **Decay**: low。

### run it twice (RIT)
- **tier-2**。**Type**: term / convention。**中文**: 发两次 / 跑两次。
- **Insider def**: 双方 all-in 摊牌后,**剩余公共牌发两次**(各打半个池),用于**降低方差而不改变 EV**(长期期望完全相同,只是结果更平滑)。高额桌常见礼节。
- **Outsider-tell** (`semantic_tell`):外行以为 RIT "增加赢的机会"或"对优势方不利";内行知道它 **EV 中性**,纯为降方差 / 控制波动 (evidence: [T06-S010])。
- **关联**: variance / EV / all-in。**可信度**: high / **Decay**: low。

### A-game / C-game
- **tier-2**。**Type**: term。**中文**: A 状态打法 / C 状态打法。
- **Insider def**: A-game=你**最佳状态**下的打法上限;C-game=最差状态下限。Tendler "inchworm" 模型:进步 = **同时拉高 A-game 上限 + 抬高 C-game 下限**(消除最差表现比追求最佳更值钱)。
- **Outsider-tell**:外行只想"打出神之一手"(拔高 A),忽视**C-game 才是输钱主因**;内行的核心功夫是"少打烂牌局"而非"多打神牌局" (evidence: [T06-S018])。
- **关联**: tilt / variance / mental game。**可信度**: high / **Decay**: low。

### wet / dry board
- **tier-2**。**Type**: term。**中文**: 湿 / 干牌面。
- **Insider def**: wet=**听牌密集**(连张、两同花、易成顺/花)的牌面,范围交互复杂、需保护;dry=听牌稀少(彩虹隔张)、领先方可慢打。board texture 的口语二分。
- **Outsider-tell**:外行只看自己牌,不读 wet/dry → 在湿面慢打被反超、在干面过度保护 (evidence: [T06-S007])。
- **关联**: board texture / range advantage / c-bet。**可信度**: high / **Decay**: low。

### cooler
- **tier-2**。**Type**: term (口语/slang)。**中文**: 撞车 / 必输局。
- **Insider def**: 双方**都打对了**、但强牌**撞上更强牌**(如 AA vs KK、葫芦 vs 四条)导致大量筹码易手的"无解局" —— 没人犯错,纯运气。区别于 bad beat(领先被听牌反超)。
- **Outsider-tell** (`semantic_tell` + `register_tell`):外行把**所有输钱**都叫 cooler/bad beat 来逃避复盘;内行严格区分 cooler(真无解,不该自责)vs 自己打错(该复盘),不拿 cooler 当借口 (evidence: [T06-S022])。
- **关联**: bad beat / variance / EV-over-results。**可信度**: high / **Decay**: low。

---

## B. Outsider-tell（外行破绽 top 12 — insider-only spotting tells）

> 这些是内行一听就知道"这人不是圈里的"的破绽。**喂 Phase 2.5 表达 DNA 的核心素材**:每条都对应一个内行的反向价值观。

1. **把 GTO 当"无脑跟注/不会输的必胜法"** — 内行:GTO 是**不可剥削的均衡基线/锚点**,对会犯错的对手**剥削 (exploit) EV 更高**;GTO 只保证"不被打爆",不保证"赚最多"。把 GTO 当万能必胜公式 = 没真懂它 (evidence: [T06-S015, T06-S017])。
2. **"我靠读牌天赋/读心术/微表情赢钱"当主要 edge** — 内行:长期 edge 主要来自**范围思维 + 频率 + 选场 + 心态 + 资金管理**;live tells 是边际增量(线上根本没有)。把读人当核心 = 古典感觉派的过时叙事(连 Negreanu 都 2025 转向每日学 solver) (evidence: [T06-S015])。
3. **不懂 range,只想"对手到底有哪张牌"** — 内行的决策原子是**范围分布**,把对手 put on a *range* 再随行动收窄;put on a single hand 是新手最大的错 (evidence: [T06-S001])。
4. **把运气当实力(不分离决策与结果)** — 内行:**+EV 决策即正确,单局输赢是方差噪音**;短期上分不是水平证明。"你跟了还输所以你跟错"是典型外行因果倒置 (evidence: [T06-S014, T06-S013])。
5. **算赢率/EV 时完全忽略 rake** — 内行:**rake 吃掉中低级别一大块赢率**,"打平"的玩家其实在缓慢失血;选低 rake 场 + rakeback 是赢率的一部分。不谈 rake = 没真打过钱 (evidence: [T06-S011])。
6. **混淆 cash 与 MTT/ICM** — 内行:锦标赛泡沫/名次跳时 **ICM 让你弃掉 cash 里必跟的牌**;用 chipEV 思路打 MTT 泡沫期是大漏。把两种游戏当一回事 = 外行 (evidence: [T06-S004])。
7. **以为 solver / HUD 是"作弊器"** — 内行:**solver 是离线学习工具**(赛后复盘、研究均衡),合规;**实时**用 solver/RTA 才违规。把"用 solver 学习"等同作弊 = 不懂这一行怎么进步的 (evidence: [T06-S015])。
8. **把短期样本当统计结论** — 内行:bb/100 赢率要**数万手**才显著,几百上千手是纯噪音。"我这周赢爆了所以我打得好"暴露不懂方差与样本量 (evidence: [T06-S013])。
9. **混淆 pot odds 与 equity** — 内行:pot odds = 跟注**所需的最低胜率门槛**,equity = 我**实际**赢的概率,二者**比较**才决定跟不跟。当成同一个数 = 数学没入门 (evidence: [T06-S003])。
10. **把 MDF 当必须严格执行的铁律** — 内行:MDF=1/(s+1) 是**对极化注的防守上限工具**,**短筹/多人/ICM 下应主动偏低**;机械套 MDF 反被剥削 (evidence: [T06-S002, T06-S004])。
11. **把 tilt 理解成"输急了梭哈"** — 内行:tilt = **任何偏离 A-game 的情绪化**(含赢钱松懈、怕输过紧、报复诈唬、弃掉该跟的牌);且要在情绪到阈值**之前**注入逻辑。只认"上头梭哈"= 不懂心态派 (evidence: [T06-S019, T06-S018])。
12. **声称自己有"扑克认证/段位/职称"** — 内行:扑克**无任何官方执业/教练/选手认证**;唯一凭据是**长期赢率 (bb/100) + 战绩样本**。一开口"我是认证扑克教练 / 我有 X 段"就露馅(行业不存在这套) (evidence: [T06-S013])。

**附加微破绽 (register tells)**:把 "3-bet" 读成"下注三次";把 cooler/bad beat 当所有输钱的万能借口逃避复盘;把 overbet/donk 当"吓唬人"随便用;over-leveling(对根本没在想的弱鱼想到第三层);说 "GTO 牌" 当某种具体打法而非"均衡策略"。

---

## C. 这一行拒绝的话术（厂商 / 营销 / 骗局话术 — rejected vendor speak）

> 下游 item 7 机械抓本节。每条 = 资深人**为什么拒绝**。这些话术违背行业"EV/方差/诚实样本"的核心价值观,听到即警惕。

1. **"保证盈利 / 稳赚不赔 / 包赢"** — **拒绝理由**:扑克是**高方差**游戏,任何短期"保证盈利"承诺都违背方差的数学本质;真正的赢率要数万手才显著。承诺"稳赚"的训练站/私教/staking 一定在骗 —— 资深人第一反应是"他不懂方差,或在割韭菜" (evidence: [T06-S013])。
2. **"学会 GTO 就无敌 / GTO 让你打遍天下无敌手"** — **拒绝理由**:GTO 只给**不可剥削基线**,对弱对手**剥削 EV 更高**;且人类无法在牌桌完美执行 GTO。把 GTO 包装成"必胜按钮"是对它的根本误解,资深人(Polk/Galfond/Bart Hanson)反复打这个脸 (evidence: [T06-S015, T06-S017])。
3. **"我的私教 / 课程让你三个月打上 NL500 / 高级别"** — **拒绝理由**:升级别受**bankroll(资金扛方差)+ 真实赢率样本**双重约束,无法靠"上课"在固定时间跳级;承诺具体级别/时间表 = 漏斗营销话术。资深人:进步是非线性的,且要先有 bankroll 撑得住 (evidence: [T06-S013, T06-S005])。
4. **"读心术 / 微表情 / 微反应必胜 / 教你看穿对手底牌"** — **拒绝理由**:线上**根本没有微表情**;线下 live tells 是**边际增量**而非核心 edge。把"读心"当主要盈利来源是古典感觉派的过时神话(连 Negreanu 都转向 solver)。卖"读心必胜"= 卖玄学 (evidence: [T06-S015])。
5. **出千 / 作弊工具 / 实时辅助 (RTA) 营销("AI 帮你实时出牌")** — **拒绝理由**:这是**作弊**(违反所有牌房规则、可没收资金封号、甚至违法),且摧毁游戏生态。资深社区对 RTA/bot/标记牌零容忍 —— 把"实时 solver 辅助"包装成"科技助力"是给作弊洗白 (evidence: [T06-S015])。
6. **Staking 骗局话术("投我稳定回报 / 我已稳赢只差本金 / 保本分成")** — **拒绝理由**:正规 staking 有**makeup(欠账追平)机制 + 透明手数记录 + 可验证赢率**;承诺"稳定回报/保本"违背方差,是典型 staking 骗局(卷本金跑路或虚报战绩)。资深人要的是长期 graph + 第三方 tracker 数据,不是口头"我稳赢" (evidence: [T06-S013])。
7. **"背下这套 chart / range 表就能赢" (chart 万能论)** — **拒绝理由**:死记 solver 输出**不可迁移**(换 sizing/牌面/对手就失效),且制造可被反剥削的同质化打法。资深人(Galfond *Simplifying Solvers*、Brokos toy game)主张**理解 why 而非记 what**:"learning to think like a solver, not to recall outputs" (evidence: [T06-S020, T06-S021])。
8. **"花钱买经验值 / 段位 / 认证证书证明牌技"** — **拒绝理由**:扑克**无官方认证体系**,唯一凭据是赢率 + 战绩。任何卖"扑克段位/教练证/等级认证"的都是无中生有(蹭其它行业的认证心智) (evidence: [T06-S013])。

---

## D. 标准 / 惯例（de-facto conventions — 本行业无监管标准 / 无认证 / 无法规）

> 扑克策略本身**无官方标准、无执业认证、无策略监管**(博彩牌照是"开赌场"的法规,与"如何打牌"无关)。但行业有大量**事实惯例 (de-facto conventions)**,资深人默认遵守。

### bb/100 赢率口径
- **惯例**:用**每 100 手赢得的大盲数 (bb/100)** 作跨级别可比的统一赢率单位。在线现金局 ~5bb/100 = 强;~2-3bb/100 = 稳赢;需**数万手**样本才统计显著(标准差极大)。tracker 软件 (PokerTracker / Hold'em Manager) 普及后(~2007+)成事实标准。**Decay**: low。(evidence: [T06-S013])

### stakes 命名 (NL50 / NL200 / NL500…)
- **惯例**:在线现金局按 **100bb buy-in 的美元额**命名 —— NL50 = $0.25/$0.50 盲、$50 满买;NL200 = $1/$2、$200 满买;NL500、NL1k 类推。MTT 按 buy-in 额(如 $109、$1k)。说 "我打 NL200" 内行秒懂级别。**Decay**: low。(evidence: [T06-S025])

### buy-in / bankroll 倍数惯例
- **惯例**:**cash ~20-40 个 buy-in、MTT ~100-300 个 buy-in**(MTT 方差远高需更厚 bankroll)是资金管理共识下限,用以把 risk of ruin 压到可接受。激进者下探、保守者上浮,但"用生活费打/不隔离"被一致视为外行。**Decay**: low。(evidence: [T06-S013])

### run it twice (RIT)
- **惯例**:高额桌 all-in 后**发两次公共牌、各分半池**以降方差(EV 中性)。多数高额线上/线下局支持;是否 RIT、发几次属桌规礼节。**Decay**: low。(evidence: [T06-S010])

### solver 精度口径 (exploitability / pot distance)
- **惯例**:用 **exploitability(可剥削度,mbb/手 或 % pot)** 衡量一个策略"离纳什均衡多远" —— 数值越低越接近 GTO。solver 收敛常报"距均衡 < X% pot"。学术侧 Libratus/DeepStack 用 **mbb/hand** 报对人优势。是 solver 时代讨论"解多准"的通用刻度。**Decay**: medium(工具与口径演进)。(evidence: [T06-S016, T06-S015])

### 牌房规则差异 (platform-specific，无统一标准)
- **惯例(实为各家私订,无统一标准)**:各牌房在以下维度差异巨大,资深人选场前必查 ——
  - **是否禁 HUD / 第三方软件**:部分房(如近年 PokerStars 限制、GG/部分房禁 HUD)vs 允许;
  - **是否匿名桌 (anonymous tables)**:匿名桌无法长期建对手数据库 → 削弱剥削、利好娱乐玩家;
  - **rake 结构**:pot rake(按底池%+cap)vs time rake(线下按时收)vs rakeback/奖励力度,直接决定赢率;
  - **RTA / bot 政策**:实时辅助一律禁(违者没收+封号),各房稽查力度不同。
  - 这些**无行业统一标准**,是 platform-specific 变量。**Decay**: medium。(evidence: [T06-S011])

> **Regulation = N/A**:无策略层监管。**Certification = N/A**:无任何官方执业/教练/选手认证 —— 这条"空"本身是 §B #12 的外行破绽来源。

---

## Phase 2 提炼提示

### 「行业表达 DNA」直接素材（喂 Phase 2.5 expression-DNA）

- **高频黑话 top 10**(内行 register 标志):range / equity / EV / GTO / exploit / MDF (1/(s+1)) / polarized / c-bet / 3-bet / SPR / ICM / bb/100 / tilt / GII。说话默认主语是 **range**、默认标尺是 **EV**、默认追问 **why-over-what**。
- **行业拒绝的厂商话术 top 5**(→ 反映价值观 + 反模式):①"保证盈利/稳赚"(违背方差) ②"学会 GTO 就无敌"(误解均衡只是基线) ③"三个月打上高级别"(无视 bankroll+样本) ④"读心术/微表情必胜"(玄学化边际 edge) ⑤ RTA/作弊"科技助力"洗白(伦理红线)。**拒绝逻辑统一指向**:尊重方差、GTO≠必胜、理解>记忆、诚实样本、零容忍作弊。
- **外行破绽 top 10**(insider-only spotting tells):见 §B 全表 —— 核心三条 ① GTO=必胜误解 ② 运气当实力(不分离决策/结果) ③ 把对手放在单张牌而非 range。

### 「智识谱系」线索（喂 Phase 2.7 智识谱系）

**术语层硬分裂(= 喂智识谱系的流派之争硬件层)**:
- **GTO/均衡 vs exploit/剥削**:`MDF / indifference / node-locking`(均衡派词汇)↔ `population tendencies / live exploit / leveling`(剥削派词汇)。这是全行业第一性张力,术语本身就分裂成两套(与 Track 04 心智模型 #2、Track 01 流派 B1/B2 对齐)。
- **cash vs MTT/ICM**:`bb/100 / rake / game selection`(cash 词汇)↔ `ICM / bubble / pay jump / risk premium`(MTT 词汇);MDF 在 ICM 下失效是两派的硬分界 (evidence: [T06-S004])。
- **记忆 vs 思路(solver 时代学习法之争)**:`chart / solver output / node`(记忆派)↔ `toy game / heuristic / why-over-what / simplifying solvers`(思路派,Galfond/Brokos)。术语取向暴露学习哲学 (evidence: [T06-S020, T06-S021])。
- **数学/EV 派 vs 心态派**:`EV / variance / bb/100`(数学派)↔ `tilt / A-game / C-game / reciprocality / inchworm`(心态派)。心态派自成一套术语(Tendler/Angelo),是与 solver 派正交的维度。
- **AI 反哺派(独立硬件层)**:`CFR / Nash / exploitability / regret / self-play`(扑克 AI 论文术语)→ 反哺 LLM reasoning,是术语层的跨学科桥(Noam Brown)。

### 「时效性」信号（喂 Phase 2.8 诚实边界）

- **过去 12 月有变化的"标准/惯例":0 个正式标准**(本行业无官方标准/法规/认证 → 无法规驱动的刷新触发)。
- **medium decay 项**(预计 24 月内可能演化):①rake 结构(各平台调整)②solver 精度口径(GTO Wizard AI 等近实时求解工具演进,改变"解多准"的口径)③node-locking 工具能力 ④牌房 HUD/匿名/RTA 政策(平台政策驱动)。这些不是"术语定义变",而是**工具/平台惯例变**。
- 核心术语(range/equity/EV/GTO/MDF…)**decay 全 low**,定义 5+ 年稳定,CFR/Nash 数学不过时。

### 「工作流变化触发」种子（喂 wave 3 Track 03）

- 本行业**无法规/标准修订**作为 workflow 触发源(不同于强监管行业)。真正的 workflow 变化触发是 **solver/工具能力跃迁**:PioSOLVER(本地)→ GTO Wizard(云端民主化)→ GTO Wizard AI(近实时),每一跳改变"如何学/如何复盘"的工作流。
- **平台政策变化**(禁 HUD / 匿名桌 / RTA 稽查)是选场 (game selection) 工作流的触发事件。
- Track 03 应把"工具能力升级"和"平台政策"当作本行业 workflow 变化的等价物(替代其它行业的"法规修订")。

### 冷僻 / 信号薄弱

- 术语数 **40**(Tier-1 **18** ≥16 ✓;Tier-1+Tier-2=40 ≥40 ✓),outsider-tell 覆盖:**Tier-1 全部 18 个有 tell**(100%),Tier-2 多数有 tell(≥50% ✓)。→ **非冷僻,信号充足**。
- **type 分布诚实标注**:Term/Acronym 占 ~85%,Standard = 事实惯例(非官方),**Regulation = N/A,Certification = N/A**。这不是采集不足,而是**行业事实**:扑克策略无监管、无认证 —— "认证扑克教练"不存在(本身是外行破绽 §B#12)。
- **中英失衡(与 Track 04/01 一致,必标)**:术语正典 **几乎 100% 英文一手**(GTO Wizard blog / 扑克 AI 论文 / 作者自营站)。中文世界为社区转述/翻译,且多落黑名单(知乎/公众号/百度/CSDN)→ 无独立中文术语一手进入正典。中文常用说法多为英文术语的音译/意译(GTO/range/bluff 常直接说英文)。Phase 2.8 须明示:本 skill 的术语层与 register 几乎全部继承自英文一手,这是行业事实而非采集缺口。

---

## 质量自检

- [x] 术语数 40 ≥ 40 floor(Tier-1 18 ≥16,Tier-2 22)
- [x] 5 type 按行业类型合理分布(Term/Acronym 主导;Standard=事实惯例;Regulation/Certification 明确标 N/A 而非缺漏)
- [x] Tier-1 全部 18 个填了 outsider-tell;Tier-2 ≥50% 填了
- [x] outsider-tell ≥10(实 12 条主 + 微破绽附录)
- [x] 厂商话术拒绝节齐全(8 条,标题含「rejected vendor speak」+「厂商话术拒绝」)
- [x] 标准/惯例节(6 条 de-facto conventions + 日期/decay 字段)
- [x] Source Manifest 在最前;每 URL 跑 source_verifier classify;无 declared>auto(GTO Wizard blog=verified_primary auto;作者站 secondary→surrogate_primary 仅按 intake author-one-hand 政策上调,note 标注;Wikipedia/训练站 glossary 老实 secondary)
- [x] 每条 claim 挂 evidence: [T06-Sxxx];last_checked=2026-06-05
- [x] Manifest 无 blacklisted(未碰知乎/公众号/百度/CSDN/Quora/Medium farm/G2/Capterra)/ 无 dead
- [x] Phase 2 接口(表达 DNA / 智识谱系术语硬分裂 / 时效信号 / workflow 触发 / 冷僻+中英失衡)已填
- [x] disputed 术语:MDF"是否严格执行"、donk"是否合理"已在条目内标注两派理解,未强行统一
