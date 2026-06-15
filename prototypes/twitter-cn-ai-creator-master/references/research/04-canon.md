# Track 04 — Canon：X 平台规则 + 推文/thread 方法论 + 核心概念

> 行业：推特(X) 中文圈 AI 自媒体博主（重点：写推文/thread、做内容）。Locale=zh-CN（canon 含英文 X 写作正典）。Research date: 2026-06-06。
>
> 行业性质判定：**Pre-canonical / 工程化 + 平台依赖型**。没有学术 textbook，canon = (1) X 官方平台规则 + 开源算法（最高权威，ground truth）+ (2) 英文「写在网上 / build in public」运动的奠基文本（David Perell / swyx / Pieter Levels / Ship30for30，这是真正被这一行从业者读过/引用的）+ (3) 中文圈「编译/信息差」打法（一手多在黑名单平台，见诚实边界）。

## Source Manifest

| source_id | url | bucket | last_checked | author/host | one-line note |
|-----------|-----|--------|--------------|-------------|---------------|
| T04-S001 | https://github.com/twitter/the-algorithm | verified_primary | 2026-06-06 | X / Twitter | 开源推荐算法主仓库 — For You 排序 ground truth |
| T04-S002 | https://github.com/twitter/the-algorithm-ml | verified_primary | 2026-06-06 | X / Twitter | Heavy Ranker ML 模型代码（projects/home/recap） |
| T04-S003 | https://github.com/igorbrigadir/awesome-twitter-algo | verified_primary | 2026-06-06 | Igor Brigadir | 算法代码逐行注解 — 引擎权重数值出处 |
| T04-S004 | https://help.x.com/en/using-x/x-premium | verified_primary | 2026-06-06 | X 官方 help | Premium 长推/Articles/功能官方说明 |
| T04-S005 | https://legal.x.com/en/creator-revenue-sharing-terms.html | verified_primary | 2026-06-06 | X 官方 legal | 创作者变现官方条款 |
| T04-S006 | https://x.com/premium/status/1855026854681624761 | reference | 2026-06-06 | X Premium 官号 | 变现规则官方公告（2024-10 改制） |
| T04-S007 | https://www.swyx.io/learn-in-public | verified_primary | 2026-06-06 | Shawn "swyx" Wang | "Learn in Public" 奠基 manifesto（作者个人站） |
| T04-S008 | https://perell.com/write-of-passage-course/ | verified_primary | 2026-06-06 | David Perell | Write of Passage — 写在网上的经典 playbook |
| T04-S009 | https://readmake.com/ | verified_primary | 2026-06-06 | Pieter Levels | MAKE: Bootstrapper's Handbook 官方站（build in public 原典） |
| T04-S010 | https://www.ship30for30.com/post/how-to-write-an-atomic-essay-a-beginners-guide | verified_primary | 2026-06-06 | Dickie Bush / Nicolas Cole | Atomic Essay 方法（screenshot essay 原型） |
| T04-S011 | https://www.ship30for30.com/post/how-to-start-writing-online-the-ship-30-for-30-ultimate-guide | verified_primary | 2026-06-06 | Ship30for30 | 写在网上系统教程（hook/结构） |
| T04-S012 | https://baoyu.io/ | verified_primary | 2026-06-06 | 宝玉 @dotey | 中文 AI 圈头部博主个人站（翻译/编译一手） |
| T04-S013 | https://github.com/JimLiu/baoyu-skills | verified_primary | 2026-06-06 | 宝玉 (JimLiu) | 宝玉公开 skill 仓库 — 编译/post-to-x 流程一手 |
| T04-S014 | https://sproutsocial.com/insights/twitter-algorithm/ | secondary | 2026-06-06 | Sprout Social | 算法运作 + 策略二手综述 |
| T04-S015 | https://www.socialmediatoday.com/news/x-limiting-the-reach-some-links-mentions-posts/690980/ | secondary | 2026-06-06 | Social Media Today | 外链/提及降权报道 |
| T04-S016 | https://www.socialmediatoday.com/news/x-formerly-twitter-updates-creator-revenue-share-program/734944/ | secondary | 2026-06-06 | Social Media Today | 变现门槛更新报道（5M imp / 2000 verified followers） |
| T04-S017 | https://www.socialmediatoday.com/news/x-formerly-twitter-open-source-algorithm-ranking-factors/759702/ | secondary | 2026-06-06 | Social Media Today / @mattnavarra | X 官方披露排序信号权重的二手汇总 |
| T04-S018 | https://techcrunch.com/2023/10/05/x-cuts-headlines-from-link-previews-as-musk-wants-users-posting-directly-on-the-platform | secondary | 2026-06-06 | TechCrunch | Musk 留住用户/砍外链标题的策略背景 |
| T04-S019 | https://socialbee.com/blog/twitter-algorithm/ | secondary | 2026-06-06 | SocialBee | quote post/dwell/bookmark 信号二手 |
| T04-S020 | https://csmapnyu.org/impact/news/what-can-we-learn-from-twitters-open-source-algorithm | secondary | 2026-06-06 | NYU CSMaP | 学界对开源算法的解读（含局限） |

---

## 行业性质前置说明（诚实边界）

- 这一行**没有学术 canon**。"正典"由三层构成：X 平台规则（一手最硬）> 英文写作运动经典（真正被读）> 中文圈打法（信号薄，多在黑名单平台）。
- **算法开源代码本身不含全部参数**：X 公开了架构但抹掉了关键 feature set / 模型权重 (evidence: [T04-S001, T04-S020])。流传的权重数值来自代码中 scoring plan 注释与第三方逐行注解 (evidence: [T04-S003])，**属一手代码注释，但 X 此后未持续公开更新，2024+ 实际权重可能已变**——保留为「方向性事实」而非精确现值。
- **中文圈"编译/信息差"方法论的一手公开复盘绝大多数在知乎/公众号（黑名单）**。本 track 用头部博主**个人站 baoyu.io + 公开 GitHub 仓库**作为可追溯一手 surrogate (evidence: [T04-S012, T04-S013])，但完整方法论的厚度因黑名单受限——见末尾缺口。

---

## 总览（按类型分组）

### 平台规则 / 算法（最高权威，必读 N=3）
| 项 | 来源 | 一句话 | Endorsement |
|---|---|---|---|
| the-algorithm 主仓库 | X 官方 | For You 排序架构 ground truth | T04-S001 / S003 / S020 |
| the-algorithm-ml (Heavy Ranker) | X 官方 | 终排神经网络 + 互动概率权重 | T04-S002 / S003 / S017 |
| 创作者变现条款 + Premium help | X 官方 | 变现门槛/长推/Articles 规则 | T04-S004 / S005 / S006 / S016 |

### 写作 Playbook（英文 canon，必读 N=4）
| 文本 | 作者 | 难度 | Endorsement | 一句话 |
|---|---|---|---|---|
| Learn in Public | swyx (Shawn Wang) | 入门 | T04-S007 + 跨多人引用 | 公开学习=最快建立受众的引擎 |
| Write of Passage | David Perell | 进阶 | T04-S008 + 媒体访谈 | Twitter 是网络城市广场，写 thread → 长文 → newsletter 漏斗 |
| MAKE: Bootstrapper's Handbook | Pieter Levels | 入门 | T04-S009 + IndieHackers | build in public 原典：晒数据/进度建信任护城河 |
| Ship30for30 / Atomic Essay | Dickie Bush & Nicolas Cole | 入门 | T04-S010 / S011 | 每日 250 字「截图小作文」=hook+结构训练 |

### 中文圈打法（surrogate 一手，N=2）
| 项 | 来源 | 一句话 |
|---|---|---|
| baoyu.io 翻译/编译实践 | 宝玉 @dotey | 英文一手课程/资讯 → 中文，建立高信噪比账号 |
| baoyu-skills 公开仓库 | 宝玉 | 把编译/发推流程工程化为可复用 skill |

### Core Concepts（27 个，见下）

---

## 平台规则 / 算法 — 详条

### 📄 1. the-algorithm — For You 排序漏斗
- **来源**: X 官方开源 (evidence: [T04-S001])，逐行注解 (evidence: [T04-S003])
- **核心架构**: 候选召回 → Light Ranker（Earlybird 初筛）→ **Heavy Ranker**（终排神经网络）→ 可见性过滤/启发式。约 **50% 候选来自 in-network**（你关注的人，Earlybird 搜索索引），其余 out-of-network 来自 Tweet Mixer / UTEG 图谱 / 关注推荐 (evidence: [T04-S001])。
- **必读理由**: 这是地球上最透明的主流社媒算法，中文圈"涨粉/爆款"认知应建在此而非玄学 (evidence: [T04-S020])。
- **局限/争议**: 代码缺关键参数与权重，X 未持续更新 (evidence: [T04-S001, T04-S020])。一手，但非完整现值。

### 📄 2. Heavy Ranker — 互动权重（核心硬事实）
- **来源**: the-algorithm-ml `projects/home/recap` (evidence: [T04-S002])，权重数值出自 scoring plan 注释 + 注解 (evidence: [T04-S003])。
- **互动权重（方向性，来自代码注释）** (evidence: [T04-S003, T04-S017])：
  - 点赞 fav = **0.5**
  - 转推 retweet = **1**
  - 点开+回复 / 点开停留 2 分钟+ = **11**
  - **回复 reply = 27**
  - **回复且被作者再回复 (reply engaged by author) = 75**（最高正向，对话>一切）
  - profile 点击+互动 = 12；视频看完 50%+ ≈ 0.005
  - 负向：隐藏/拉黑/静音 = **−74**；举报 = **−369**（一次举报抵消极大量正向）
- **乘数**: in-network 蓝V ×4；out-of-network 蓝V ×2；二度社交证明 ×0.75；同作者连续出现有「作者多样性折扣」(score 随位置衰减) (evidence: [T04-S003])。
- **一手核心事实**: 「**回复 > 转推 > 点赞**；引发作者回复的对话最值钱；举报是核弹级负信号」。Premium/蓝V 有结构性流量乘数。
- **争议**: 数值是 2023 开源快照，2024+ 改制后实际权重未公开；但「对话权重 75× 点赞」被 X 官方 2025 重申 (evidence: [T04-S017])，方向稳定。

### 📄 3. 外链降权（外链 deboost）— 已反转
- **历史事实**: 含外链/跳转出站的推被减触达 50–90%（Musk 公开说法），开源代码层面外链罚 30–50% (evidence: [T04-S015, T04-S018])。
- **经典对策**: 把链接放**首条推的回复里**而非正文（Musk 本人建议的 workaround）(evidence: [T04-S015])。
- **2025+ 反转（矛盾，保留）**: X 宣布**取消外链算法惩罚**，早期数据显示带链推触达约 8× 提升，转向「内容分发枢纽」定位 (evidence: [T04-S014/二手报道])。**判断**：写作时仍按「正文自足、链接放评论」更稳——降权政策反复横跳，不押注单一规则。属二手/推断。

### 🎓 4. Premium 长推 / Articles / 长文机制
- **来源**: X 官方 help (evidence: [T04-S004])
- **事实**: Premium 可发**最长 25,000 字**长推，正文超 ~280 字后折叠在「Show more」后——**前 ~280 字必须能独立作为 hook** (evidence: [T04-S004])。Premium 另有 Articles（带标题/加粗/排版的站内长文）。非 Premium 仅 280 字，所有人可读长推但只有 Premium 能发。
- **写作含义**: long-form 把外链降权问题绕开（内容留站内）；但 hook 前置规则不变。

### 📄 5. 创作者变现规则
- **来源**: X 官方条款/公告 (evidence: [T04-S005, T04-S006])，门槛更新二手 (evidence: [T04-S016])。
- **事实**: 收入分成门槛 = 近 3 月 **≥500 万 organic impressions** + **≥500 关注（后更新为 ≥2000 verified followers）** + 有效 Premium/Verified 订阅 (evidence: [T04-S006, T04-S016])。2024-10 改制：**分成基于 Premium(蓝V) 用户的互动而非广告**，最高分 Premium 订阅收入 25%，双周结算 (evidence: [T04-S006])。**回复多 = 赚最多**（广告出现在回复里）。
- **2026-03 更新（保留）**: 给「同地区/同语言」impressions 加权 (evidence: [T04-S016/二手])。对中文创作者：**触达本语言受众的价值被算法加权**——属二手/推断。

---

## 写作 Playbook — 详条

### 📖 6. Learn in Public — swyx (2018)
- **One-liner**: 把学习过程开源成「learning exhaust」，最大受益者是未来的你，副产品是受众与机会 (evidence: [T04-S007])。
- **核心论点**: 公开写教程/cheatsheet/直播敲代码；在公开平台答问（Stack Overflow/Reddit 而非封闭 Slack）；做你希望存在的东西。资深人会注意到真诚的学习者→导师循环。
- **读完得到什么**: 内容生产的底层动机框架——为什么"边学边发"比攒够再发更优。
- **继承关系**: build in public 运动的精神奠基之一 (evidence: [T04-S007])。

### 📖 7. Write of Passage — David Perell
- **One-liner**: Twitter 是网络的「城市广场 / 永不落幕的会议」，写作漏斗 = Twitter thread → 周更 newsletter → 长文 (evidence: [T04-S008])。
- **核心论点**: audience-first（先有受众再有产品）；写 thread 是练习「提炼想法成文字」的低成本场；先建 10k 邮件 + 20k 关注就有 0 成本启动的有机触达。
- **读完得到什么**: thread→newsletter→课程/产品的内容飞轮商业模型。
- **争议**: 课程偏付费、英文受众；中文圈可借模型不必照搬。

### 📖 8. MAKE: Bootstrapper's Handbook — Pieter Levels (@levelsio)
- **One-liner**: build in public 原典——公开晒收入/挣扎/方法，透明度本身是竞品无法复制的护城河 (evidence: [T04-S009])。
- **核心论点**: 7 阶段 Idea→Build→Launch→Grow→Monetize→Automate→Exit；执行 > 完美（12-in-12）；这本书自己也是 build in public（写完前就开卖）。
- **读完得到什么**: 个人创作者「晒进度=营销」的可操作心法。

### 📖 9. Ship30for30 / Atomic Essay — Dickie Bush & Nicolas Cole
- **One-liner**: 每日 250 字「截图小作文 (atomic essay)」——比 thread 长、比博客短的甜点位，30 天逼出 hook + 结构肌肉记忆 (evidence: [T04-S010, T04-S011])。
- **核心论点**: hook 必须回答「我为什么不划走读这条」；具体性 > 模糊（"9 周减 23 磅" 胜 "快速减肥"）；先点名受众（"如果你是 20 多岁的男人"）(evidence: [T04-S011])。
- **读完得到什么**: 可复制的 hook 公式库 + 高频出货的写作训练法。

### 中文圈 surrogate — 编译/信息差打法
### 💡 10. baoyu.io 编译实践（surrogate 一手）
- **One-liner**: 头部中文 AI 博主 宝玉 @dotey 把英文一手（课程/论文/资讯）系统翻译/编译成中文，建立高信噪比账号 (evidence: [T04-S012])。其公开 baoyu-skills 仓库把「编译→发推」流程工程化 (evidence: [T04-S013])。
- **为什么进 canon**: 中文 AI 圈跨多份榜单一致点名为头部一手源；代表「编译/信息差」打法的活样本（个人站可追溯，非黑名单）。
- **局限**: 完整方法论的公开复盘多在黑名单平台——这里只取可追溯的个人站/仓库证据。

---

## Core Concepts（27 个）

> tier-1 = 这一行人人必懂；tier-2 = 资深者熟知周边。来源标在括号。

| # | 概念 | Tier | 一句话定义 | 来源 evidence |
|---|------|------|-----------|------|
| 1 | **推文 (Tweet/Post)** | 1 | X 上最小内容单元，标准 280 字，Premium 至 25k | [T04-S004] |
| 2 | **Thread（推文串）** | 1 | 编号串联的多推，首条 hook+逻辑链+末条 CTA | [T04-S011] |
| 3 | **Hook（钩子）** | 1 | 首条/首行抓注意力，回答「我为何不划走」 | [T04-S011, T04-S010] |
| 4 | **Hook 公式** | 1 | 反直觉/具体数字/悬念缺口/点名受众/疑问式等可复制套路 | [T04-S011] |
| 5 | **Curiosity Gap（好奇缺口）** | 2 | 留知识空白逼读者继续读 | [T04-S011] |
| 6 | **CTA（行动召唤）** | 1 | 末条引导关注/转发/收藏/点链，需是价值的自然延伸 | [T04-S011] |
| 7 | **Atomic Essay（原子小作文）** | 2 | 250 字截图式短文，thread 与博客之间的甜点位 | [T04-S010] |
| 8 | **信息密度 / 短句排版** | 1 | 每条推要么教点东西要么推进，短句+留白提升可读性 | [T04-S011] |
| 9 | **For You 时间线** | 1 | 算法推荐流，~50% in-network + out-of-network 召回 | [T04-S001] |
| 10 | **Heavy Ranker（终排）** | 1 | 输出各类互动概率的神经网络，决定终排 | [T04-S002] |
| 11 | **互动权重** | 1 | reply(27)>retweet(1)>fav(0.5)；作者回复=75 | [T04-S003] |
| 12 | **转评赞（quote/reply/like）** | 1 | 三种基础互动；reply 权重远高于 like | [T04-S003] |
| 13 | **Quote Tweet（引用推）** | 2 | 带评论转发，既给原推信号又生成可独立涨粉的新推 | [T04-S019] |
| 14 | **外链降权 (link deboost)** | 1 | 含出站链接的推历史被减触达，对策：链接放评论 | [T04-S015] |
| 15 | **Dwell time（停留时长）** | 2 | 停下读完=兴趣信号，即使无显式互动 | [T04-S019] |
| 16 | **Impressions（曝光）** | 1 | 推被看到的次数；变现门槛按 organic impressions 算 | [T04-S006, T04-S019] |
| 17 | **Engagement（互动）** | 1 | 点赞/回复/转推/收藏/点击等主动行为 | [T04-S017] |
| 18 | **负向信号** | 1 | 隐藏/拉黑/静音(−74)、举报(−369)是核弹级降权 | [T04-S003] |
| 19 | **TweepCred / 作者信誉** | 2 | 账号可信度分影响其推的初始可见性 | [T04-S003] |
| 20 | **In-network vs Out-of-network** | 2 | 关注流 vs 算法发现流；蓝V有触达乘数 | [T04-S001, T04-S003] |
| 21 | **Premium / 蓝V / Turbo** | 1 | 订阅带长推/Articles + 互动/分成加权 | [T04-S004, T04-S006] |
| 22 | **Long-form / Articles** | 1 | Premium 站内长文/长推，绕开外链降权但 hook 前置不变 | [T04-S004] |
| 23 | **变现 / 收入分成** | 1 | 按 Premium 用户互动分成，回复多赚最多 | [T04-S006] |
| 24 | **Build in Public（公开构建）** | 1 | 晒进度/数据/挣扎建信任护城河 | [T04-S009] |
| 25 | **Learn in Public（公开学习）** | 1 | 把学习开源成内容，副产品是受众 | [T04-S007] |
| 26 | **信息差 / 编译** | 1 | 英文一手→中文快讯，高信噪比，跨语言搬运建账号 | [T04-S012, T04-S013] |
| 27 | **涨粉飞轮（audience-first）** | 1 | thread→newsletter→产品的内容→受众→变现循环 | [T04-S008] |

---

## Phase 2 提炼提示

**反复出现 ≥3 个 canon 都讨论的核心 idea（候选心智模型）**:
- **「对话 > 广播」**：算法 reply=27/作者回复=75 (S003) + 变现按回复 (S006) + Perell「城市广场对话」(S008) → 心智模型：写推先问「这会引发回复吗」。
- **「Hook 前置/前 280 字自足」**：Atomic Essay (S010) + Ship30 hook (S011) + Premium 长推折叠机制 (S004) → 不管多长，第一屏决定生死。
- **「公开 = 复利」**：Learn in Public (S007) + Build in Public (S009) + 编译信息差 (S012) → 持续公开输出本身是涨粉/信任引擎。

**智识谱系种子**:
- **写在网上 (Write Online) 流派** 奠基：swyx Learn in Public + Perell Write of Passage；当前代表与 Track 01 figures 关联（Perell/swyx/Dickie Bush/Nicolas Cole）。
- **Indie/Build in Public 流派** 奠基：Pieter Levels MAKE；中文映射：宝玉 @dotey 等编译型博主。
- **平台机制流派** 奠基：X the-algorithm 开源；当前理解随政策反复（外链降权反转）演化。
- **主要分歧（still-debated）**：外链降权到底罚不罚（2023 罚 vs 2025 取消，S015/S014 矛盾保留）；开源权重数值的现时有效性（S001/S003 vs 已改制）。

**核心概念 → 候选 playbook**:
- 遇到「想放链接」→ 正文留钩子、链接放第一条回复（外链降权对策）。
- 遇到「thread 写不动」→ 退回 atomic essay（250 字）先练 hook。
- 遇到「想涨粉」→ 优先制造能引发回复/作者再回复的对话，而非求赞。
- 中文 AI 内容选题 → 编译英文一手 + 时效抢跑（信息差），但注意封号避坑（住宅IP/正常作息/不蹭大V，二手 reference）。

**冷僻 / 信号薄弱**:
- 必读「书」仅 1 本真书（MAKE），其余是平台规则/课程/manifesto——符合 pre-canonical 工程行业特征，不补。
- 一手 endorsement 比例：20 源中 verified_primary = 13（含 X 官方 6 + 作者个人站/repo 7），≈65%，过线。
- **中文圈方法论缺口**：编译/信息差/涨粉的完整一手复盘**绝大多数在知乎/公众号（黑名单）**，本文件只能用 baoyu.io 个人站 + GitHub 仓库作 surrogate。SKILL.md 诚实边界节须注明：中文圈打法的厚度低于英文写作 canon，部分依赖 surrogate 与二手推断。
