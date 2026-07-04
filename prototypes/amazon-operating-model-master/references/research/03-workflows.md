# Track 03 — 工作流 / SOP（把亚马逊机制串成可走查的流程）

> 本轨把前几轨定义过的机制（Working Backwards、PR/FAQ、6-pager、WBR、OP1/OP2 + S-Team goals、Bar Raiser、COE + 5 Whys、input/output metrics、Type1/Type2）**组装成一步步能跑的工作流**。每个工作流写三层：
> - **入门 SOP**：新手照着走的最少必要步骤。
> - **资深路径**：老手跳过 / 优化 / 额外做的环节。
> - **近期变化 / 失败模式**：AI/工具/规模/远程带来的改写 + 这个流程最常见的翻车方式。
>
> 来源标注：**一手** = 官方(aboutamazon/amazon.jobs/AWS)或《Working Backwards》两位作者(Colin Bryar & Bill Carr)或亲历者长文(Dave Anderson=Scarlet Ink / Cedric Chin=Commoncog / Ethan Evans=Level Up)；**二手** = 转述/综合；**推断** = 我基于机制逻辑补的。

---

## 工作流 1 — 用 Working Backwards 发起一个新产品/新功能（PR/FAQ）

**一句话**：不先写代码、不先做 PPT，而是先写「产品发布那天的新闻稿 + FAQ」，从客户体验倒推该造什么，反复评审到想清楚再动手。

### 入门 SOP（新手照着走）

1. **一个作者，几小时先出草稿**。PR/FAQ 由**单一作者**（通常是 PM）起草，第一版只花几小时。核心心态：产品探索是**漏斗不是隧道**（funnel, not a tunnel）——先快速写多个想法，便宜地筛掉大部分。〔一手 workingbackwards.com〕
2. **写「新闻稿」部分（Press Release，≤1 页）**，用未来某个发布日期、以客户能看懂的大白话，像产品已经上线一样宣布它。必含五块：
   - **标题 + 副标题**：标题给产品起个朴素的名字；副标题点明**具体客户段 + 关键收益**（"精确描述客户在这里至关重要"）。
   - **摘要段**：城市、媒体、真实的发布日期，然后产品概述 + 好处。
   - **问题段**：**站在客户视角**讲痛点；这个问题要对应**足够大的 TAM**（有足够多、愿意付费的客户）。
   - **解决方案段**：讲清楚怎么解决，并**承认现有替代方案**、说明凭什么明显更好。
   - **引言 + 上手**：一句公司发言人 + 一句假想客户的话，加"怎么开始用"。
3. **写「FAQ」部分（≤5 页）**，分两块：
   - **External FAQ**（客户/媒体会问）：多少钱？怎么用？哪买？怎么找客服？
   - **Internal FAQ**（内部各部门会问，这里才是硬核）：客户现在用什么替代？凭什么更好/更便宜/更快？竞品是谁？TAM 和需求多大？最难啃的技术/运营问题是什么？要新建什么能力？有哪些第三方依赖？有没有法律/合规问题？单位经济模型和回本时间？**要成功必须成立的假设是什么？**以及**这事最可能失败的三个原因**。〔一手 workingbackwards.com〕
4. **逐级评审、反复重写**：作者 → 直属经理 + 同级 → ~10 人跨职能小组 → 高管。每轮都据反馈重写。
5. **评审会**（见工作流 2 的开会法）：60 分钟制，**前 15–20 分钟静默阅读 + 批注**，后 40 分钟讨论；作者记录所有问题与反馈。评审的是**7 个维度**：客户清不清楚？问题讲清楚没？方案对得上问题吗？客户会不会为它改变行为？凭什么更好/更便宜/更快？TAM 和回本够不够大？还有哪些约束/难题要解决？
6. **Go / No-Go 决策**。No-Go 的典型理由：跟现有产品差异不够大、TAM 太小、前期投入大但回报不清、有没解决的技术/运营障碍、优先级被别的事压过。Go 就按 FAQ 里写的资源和时间线启动。〔一手 workingbackwards.com〕

**PR/FAQ 里必答的几个"要害问题"**（背下来）：谁是客户？解决什么问题？凭什么明显更好（faster/easier/cheaper）？要成功哪些假设必须为真？最可能失败的三个原因？——如果新闻稿描述的产品没有"阶跃式变好"，那就**不值得造**。〔一手 aboutamazon.com〕

### 资深路径（老手跳过 / 优化 / 额外做）

- **老手起草更快、砍得更狠**：资深 PM 敢在几小时内写完就拿去 review，且更早地对自己的想法说 No——把 PR/FAQ 当"杀想法的工具"而不是"卖想法的工具"。心态是 truth-seeking（求真）不是 selling（推销）。〔一手 workingbackwards.com〕
- **额外投入时间是常态**：一个 Amazon 团队写 **10 版以上 PR/FAQ、跟高管碰 5 次以上**很正常。AWS 在正式发布 S3/EC2（2006）前，花了**一年多**打磨 PR/FAQ——用前期规划时间换后期执行速度（"velocity over speed"）。〔一手 aboutamazon.com / workingbackwards.com〕
- **资深评审者读法不同**：不纠结文笔，直接找**逻辑裂缝**和**被藏起来的假设**——尤其盯"最可能失败的三个原因"和单位经济模型是否自洽。
- **额外加码**：老手会主动写**"我们明确不做什么"**、把最尖锐的反对意见自己先写进 Internal FAQ（预答难题），避免评审会被一个没想到的问题打穿。

### 近期变化 / 失败模式

- **生成式 AI 辅助写 PR/FAQ**：现在大量团队用 LLM 快速生成第一版新闻稿和 FAQ 骨架、跑竞品/TAM 检索、扮演"挑刺评审者"预答 Internal FAQ。风险：AI 生成的稿子**读着顺但客户和痛点是编的**，把"漏斗筛想法"变成"批量产出看似合理的假需求"。〔推断 + 行业观察〕
- **失败模式 · 造假需求（working backwards from a solution）**：最常见翻车——团队心里已经想好要造某个东西，然后**倒着编一个客户和痛点**来合理化它。PR/FAQ 本该"从客户倒推方案"，被做成"从方案倒推客户"。识别信号：问题段空洞、"客户"是抽象群体而非具体人、TAM 靠拍脑袋。〔二手 / 推断〕
- **失败模式 · 写成营销稿**：新闻稿写得像真营销文案（形容词堆砌、夸张），而不是冷静地陈述"客户得到什么、我们要付出多大代价"。
- **失败模式 · 评审会变成"批准会"**：本该 truth-seeking 的会开成走过场盖章，没人真读、没人真挑刺——见工作流 2 的失败模式。

**来源**：
- The Amazon Working Backwards PR/FAQ Process — workingbackwards.com（Colin Bryar & Bill Carr，《Working Backwards》作者，前 Amazon 高管）〔一手〕 https://workingbackwards.com/concepts/working-backwards-pr-faq-process/
- An insider look at Amazon's culture and processes — aboutamazon.com〔一手 官方〕 https://www.aboutamazon.com/news/workplace/an-insider-look-at-amazons-culture-and-processes
- PR/FAQ Instructions & Template — workingbackwards.com〔一手〕 https://workingbackwards.com/resources/working-backwards-pr-faq/

---

## 工作流 2 — 写并评审一份 6-pager narrative（叙事备忘录）

**一句话**：用不超过 6 页的**叙事文**（不是 PPT）承载一个决策/提案；开会前 20–30 分钟全场**静默阅读**，然后逐段讨论——用"写作"逼出"思考"，用"静默阅读"保证每个人都真读过。

### 入门 SOP（新手照着走）

1. **确认这是叙事文，不是 slide**。Bezos 2004 年下令用 6-pager 取代 PowerPoint，因为幻灯片会**掩盖逻辑漏洞、简化复杂问题**；完整句子和段落写成的叙事会把逻辑缺口逼到明面上。〔一手 aboutamazon / CNBC 2019 引 Bezos〕
2. **搭结构**（常见骨架，按需增删）：
   - **Introduction / 开场**：简要点出核心挑战或机会。
   - **Goals / 目标**：要达成的关键目标与预期结果。
   - **Tenets / 原则**：指导这个提案的几条信条（当各方吵起来时用来裁决优先级）。
   - **正文**：现状 → 分析 → **建议（先给结论，再用证据支撑，自上而下）** → 数据/指标 → 风险 → 时间线。
   - **Appendix / 附录**：所有表格、明细数据、FAQ 塞附录，正文保持 6 页。
3. **反复写、放一放、再改**。好 memo 是**写了又写**：写完给同事、请他们改、**搁两天**、换清醒的脑子再编辑。"没法一两天写完。"〔一手 引 Amazon 内部说法〕
4. **开评审会**：
   - **前 20–30 分钟：全场静默阅读**（silent reading），每个人**读完整篇 + 做批注**。这样保证讨论时"每个人都真读过全论证"，而不是边听边被牵着走。
   - **然后逐段讨论**：作者团队接住所有问题和反馈并记录。资深与会者往往边读边在文档上留 comment，讨论时按 comment 走。
5. **收尾**：明确决策/下一步 + owner + 时间线。

### 资深路径（老手跳过 / 优化 / 额外做）

- **老手把"结论前置"做到极致**：像顶级咨询的金字塔结构——第一段就给建议，后面全是支撑证据，而不是"娓娓道来最后才揭晓"。让读者 30 秒抓住主张。
- **团队分工写、一人定调**：大 memo 常拆给多人各写一段，但**由一个人统稿定文风**，否则读起来像拼盘、逻辑接不上。〔二手〕
- **额外做"预答 FAQ"**：资深作者把评审会上必被问的尖锐问题提前写进附录 FAQ，把讨论时间省下来聊真正有分歧的地方。
- **老手会砍数据**：把 6 页正文里所有"证明我很努力"的图表挪进附录，正文只留支撑主张必需的那几个数。
- **静默阅读的资深玩法**：老板级读者常在静默阅读阶段就用批注把 memo"改成血红"（这也是 Scarlet Ink 名字的由来意象）——讨论时直接按批注密度定位薄弱段。

### 近期变化 / 失败模式

- **远程/异步的改写**：疫情后大量 6-pager 评审转线上，静默阅读改成**共享文档（如 Google Docs/Quip）里实时批注**，甚至"预读"提前一天发、会上只讨论。工具让批注可追踪，但也稀释了"同一时间同一房间一起沉默读"的专注强制力。〔推断 + 行业观察〕
- **生成式 AI 辅助**：LLM 用来生成 memo 初稿、压缩到 6 页、扮演评审者预测反对意见、检查逻辑跳跃。风险见下条。
- **失败模式 · 6-pager 写成 PPT 的文字版**：最经典翻车——把幻灯片要点用完整句子重写一遍，还是 bullet 思维、没有叙事逻辑链，等于换皮 PPT，逼思考的作用全失。〔二手 / 推断〕
- **失败模式 · AI 味 memo**：LLM 生成的 memo 读着通顺、结构工整，但**没有真实数据、没有作者自己的判断**，评审时一问细节就穿。写作本该暴露"作者到底想清楚没有"，AI 代写把这个信号污染了。
- **失败模式 · 没人真读 / 静默阅读走过场**：与会者跳过静默阅读（或假装读），讨论变成作者单方面讲、其他人凭印象发言——退化成它想取代的那种 PPT 会。
- **失败模式 · 塞成 12 页**：正文超页、把该进附录的东西堆进正文，读者 20 分钟读不完，静默阅读机制崩掉。

**来源**：
- An insider look at Amazon's culture and processes — aboutamazon.com〔一手 官方〕 https://www.aboutamazon.com/news/workplace/an-insider-look-at-amazons-culture-and-processes
- Jeff Bezos: This is the 'smartest thing we ever did' at Amazon — CNBC 2019（引 Bezos 原话）〔一手引述〕 https://www.cnbc.com/2019/10/14/jeff-bezos-this-is-the-smartest-thing-we-ever-did-at-amazon.html
- Working Backwards: Dave Limp on Amazon's Six Page Memo — amazonchronicles.substack.com〔二手 亲历转述〕 https://amazonchronicles.substack.com/p/working-backwards-dave-limp-on-amazons

---

## 工作流 3 — 跑一场 WBR（Weekly Business Review 周业务评审）

**一句话**：每周固定时间、固定一份静态 deck，按"客户体验 → 业务表现 → 是否达标"的顺序**先看可控 input 指标再看 output**，只讨论异常（exception），追根因、不追随机波动。

### 入门 SOP（新手照着走）

1. **定节奏与范围**：固定每周同一时间（Amazon 高管层是每周三，60 分钟；旺季 90 分钟），评审代表业务的一大批指标（Amazon 高管 WBR 达 **400–500 个指标**）。〔二手 Commoncog（Cedric Chin，综合前 Amazon 人访谈）〕
2. **排 deck 的因果顺序**（关键）：**可控 input 指标在前，紧跟对应的 output 指标**；每个业务/部门一组 input→output，如此重复；**财务指标放最后**。核心信条：output（营收、留存、现金流）是结果、WBR 上**只用于报告不深挖**；真正讨论的是你能直接拉动的 **input 杠杆**。〔二手 Commoncog / 一手 Colin Bryar 引述〕
3. **会前准备**（分布式）：周日午夜后指标自动生成 → 周一各**指标 owner 自查**自己的数 → 周二各部门先开自己的 WBR，owner 调查任何异常波动，**必须能说出根因，或明确说"我不知道，在查"**。〔二手 Commoncog〕
4. **deck 呈现规范**：静态 deck（最早是打印纸），无仪表盘加载延迟；横排每页 4 张图；presenter 之间近乎无缝切换（交接常<2 秒）。最常见图是 **6-12 图**：左侧近 6 周（放大看），右侧近 12 个月（月粒度），数字直接标在线上，淡粉线=去年同期，绿三角=周目标。〔二手 Commoncog〕
5. **会上怎么开**：
   - Finance 主持人先过上周的 follow-up。
   - 指标 owner 依次过图，**只做异常驱动的讨论**：正常波动就一句"nothing to see here"（没啥好看的）快速翻过；异常波动才触发追问，owner 解释根因或声明在查。
   - **禁止就地聊战略**：主持人会当场打断跑偏成战略讨论的话题，挪到线下/S-team 会解决。〔二手 Commoncog〕
6. **客户之声（Voice of the Customer）**：客服挑一条有代表性的真实客户反馈（不一定是最高频的，而是最能说明问题的），常单独做一页读出来——**anecdote（轶事）与 metric（指标）并置**：指标告诉你"发生了"，轶事告诉你"为什么、痛在哪"。经典例子：一位顾客给孩子买药时信用卡被误拒，追下去发现是一个罕见的预授权 bug 牵出邻近系统问题。〔二手 Commoncog〕

### 资深路径（老手跳过 / 优化 / 额外做）

- **老手主导"该不该讨论这个指标"**：WBR 上最常出现的三个问题——① 这指标值得讨论吗（区分 output vs input，output 别浪费时间）；② 这是对的 input 指标吗（在几个代理指标里挑）；③ 这数是怎么测的（要求埋点透明）。资深 owner 会主动删掉不受控、不可预测的指标，只留"已被控制住、可预测"的进 WBR。〔二手 Commoncog〕
- **老手用 WBR 当"施压杠杆"而非单纯复盘**：把某指标放进 WBR 本身就是在给团队信号"这事重要"。经典：Bezos 曾把**招聘**拉进 WBR 审视，因为招聘瓶颈卡住了商品目录更新——一放进 WBR，全组注意力集中，危机解掉。〔二手 Commoncog〕
- **老手会动态换指标**：input 指标不是永久的——当你还在驱动它、但它对 output 不再有影响（失效/被 Goodhart 化）时，就换掉它、加新的。"我们本来能追踪什么、就能避免这次事故？"——这句话通常直接产出下周 WBR 的新指标。〔二手 Commoncog〕
- **资深主持维持"高标准 + 心理安全"的平衡**：既要极高标准、又要让人敢谈错误。最资深的人负责每周会议的 decorum（会风），压住指责式提问。〔二手 Commoncog〕

### 近期变化 / 失败模式

- **AI 做指标异常检测**：现在越来越多团队用自动异常检测/预测区间给 400–500 个指标做初筛，AI 先标出"哪些是真异常、哪些是随机波动"，人只看被标红的——省掉人肉扫图。风险：AI 误报把随机波动当异常，反而助长"追 blip（图上的小突刺）"这个老毛病。〔推断 + 行业观察〕
- **静态 deck → 实时仪表盘的诱惑**：工具让人想把静态 deck 换成实时 BI 仪表盘，但 Amazon 坚持静态是为了**无加载延迟 + 全场看同一版数**；换成实时看板容易变成"各看各屏、边开会边刷数"。〔二手 / 推断〕
- **失败模式 · WBR 变成甩锅会 / 批斗会**：指标一红就质问 owner，气氛变对抗、指责式提问——人就开始藏数、美化、报喜不报忧，truth-seeking 崩掉。解药是"高标准 + 心理安全"并存。〔二手 Commoncog 明列〕
- **失败模式 · 追随机波动（chasing blips）**：把统计上的正常波动当成信号去追根因，浪费全场时间。前提没做好——指标还在"定义/测量/分析"阶段就硬塞进 WBR 去"改进"。〔二手 Commoncog 明列〕
- **失败模式 · 参会名单膨胀**：越来越多人旁听，焦点稀释、owner 表演给听众看。应只留 owner 和关键干系人。〔二手 Commoncog 明列〕
- **失败模式 · 只看 output**：只盯营收/留存这些结果指标，不看可控 input——等于开车只看后视镜，发现问题时已经晚了。

**来源**：
- The Amazon Weekly Business Review (WBR) — commoncog.com（Cedric Chin，综合多位前 Amazon 人 + Colin Bryar 引述）〔二手 高质量综合〕 https://commoncog.com/the-amazon-weekly-business-review/
- How Amazon Measures Itself — holistics.io〔二手〕 https://www.holistics.io/blog/how-amazon-measures/

---

## 工作流 4 — Bar Raiser 招聘 loop（招聘拔高者）

**一句话**：每个招聘 loop 里塞一个**受过训练、来自目标团队之外、有一票否决权**的资深面试官（Bar Raiser），确保这次录用的人**高于该岗位现有员工的中位数**（raise the bar），用结构化行为面试 + 独立书面反馈 + 由 BR 主持的 debrief，压住招聘经理的"急着补人"偏差。

### 入门 SOP（新手照着走）

1. **组 loop（5–7 人）**：1 个招聘经理 + 1 个 Bar Raiser + 3–5 个同组/邻组同事。Bar Raiser 是**唯一不属于目标团队**的人，且**不能是招聘经理的下属或隔级下属**（避免偏袒）；BR 本人级别 ≥ 该岗位。BR 可以是管理者也可以是 IC。〔一手 workingbackwards.com / 一手 Dave Anderson〕
2. **BR 做 pre-brief（预对齐）**：开面之前，BR 拉招聘经理和所有面试官对齐岗位画像、**把 Leadership Principles 分派下去**（每个面试官负责考 2–3 条 LP，避免重复/遗漏），并评估面试官够不够格。〔二手 + 一手〕
3. **每个面试官跑行为面试（STAR）**：不问假设题，问"跟我讲一个你……的时候"（Tell me about a time when…），沿 **Situation → Task → Action → Result** 追问，挖真实行为不是漂亮说辞。BR 通常问**跨岗位通用**的题（领导力、沟通、冲突、项目管理），把领域技术评估留给其他 4 个 slot 的专家。〔一手 Dave Anderson〕
4. **各自独立写书面反馈（debrief 前提交）**：必含——明确 hire / no-hire 一票 + 支撑例子、所负责的 LP、相对每条 LP 的强项弱项、**逐题的"逐字记录"而非"总结"**（transcript not summary，捕捉未过滤的细节）、每题后的小结。**必须独立写**，不许开会时才拍脑袋。〔一手 workingbackwards.com〕
5. **BR 主持 debrief（24–48 小时内）**：不是招聘经理、不是 recruiter，而是 **Bar Raiser 主持**以保证无偏、数据驱动。四步：
   - ① **静默读**所有人的书面反馈 10–15 分钟；
   - ② **重新投票**（interviewer 读完全部材料后常改票）；
   - ③ **讨论**：BR 框定"哪些 LP 达标、哪些不达标"，用**苏格拉底式提问**引导，找证据支撑的共识；
   - ④ **拍板**：BR 极少动用显式否决，多靠把讨论引到结论。〔一手 workingbackwards.com〕
6. **投票不是公式**：4-3 这种分裂票要靠招聘经理和 BR 一起判断——"强项够不够亮、弱项够不够轻"？**只要两人有一个不确定，正确答案就是不招。**〔一手 workingbackwards.com〕

### 资深路径（老手跳过 / 优化 / 额外做）

- **资深 BR 提前读反馈找模式**：BR 会**在 debrief 前就把书面反馈读一遍**，识别 pattern、准备策略——比如察觉"四个面试官都写了 meh（还行但没亮点）"，就知道这是**凑合招（desperation hiring）**的信号。〔一手 Dave Anderson · "Connor" 案例〕
- **老手把否决当"核选项"，几乎不用**：一位 BR 做过 **700+ 场面试从没否决过**招聘经理；否决是 nuclear option。真正的作用是**这把否决权存在本身**就压住了急招偏差——多数情况下 BR 靠主持把大家引到对的结论，而不是砸否决。〔二手 IGotAnOffer / 一手 Dave Anderson〕
- **额外守则 · "fail high, not low"**：老 BR 的信条是"招不到人也好过招个平庸的"（hiring nobody beats hiring someone mediocre）。团队缺人时容易把"最近这批弱鸡里最好的一个"重新框成"够格了"，资深 BR 专门拦这个。经典案例：Dave Anderson 顶着团队缺人的压力否了 Connor，招聘经理逐级上告，最后**领导层站 Bar Raiser 机制**——这机制的全部意义就是**能压过局部招聘压力**。〔一手 Dave Anderson〕
- **BR 的养成也是流程**：Bar Raiser Core（资深 BR）通过 shadowing（跟着看）/ reverse-shadowing（被看着做）带新 BR，是一套自我复制的师徒制。〔一手 workingbackwards.com〕

### 近期变化 / 失败模式

- **AI/工具带来的改写**：远程面试常态化后 debrief 多在线上开、书面反馈进共享系统；越来越多团队用工具做面试排期与 pipeline 指标追踪防止拖延。也有用 LLM 辅助整理面试逐字记录、检查 LP 覆盖是否完整。风险：AI 整理的"逐字记录"若失真，会污染 debrief 赖以决策的原始证据。〔推断 + 行业观察〕
- **失败模式 · 写成 summary 不是 transcript**：书面反馈只写"他沟通不错"这种总结、没有逐字例子，debrief 时无从复核，退化成凭印象投票。〔一手 workingbackwards.com 明列〕
- **失败模式 · 行为题问砸 / 不追 STAR**：没经验的面试官问无效的行为题、或不往下追 Action/Result，导致某条 LP 数据不足——**需要补面本身就是面试官的流程失败**。〔一手 workingbackwards.com 明列〕
- **失败模式 · desperation hiring（急招凑合）**：团队缺人 → 把"矮子里拔将军"合理化成"达标"。这是 Bar Raiser 机制存在的头号敌人。〔一手 Dave Anderson〕
- **失败模式 · 走过场**：BR 不 pre-brief、不主持、不静默读，debrief 变成招聘经理一言堂——整套防偏机制空转。

**来源**：
- Bar Raiser Hiring — workingbackwards.com（Bryar & Carr）〔一手〕 https://workingbackwards.com/concepts/bar-raiser-hiring/
- Three Tales from an Amazon Bar Raiser — Dave Anderson / Scarlet Ink（前 Amazon GM，亲历）〔一手〕 https://www.scarletink.com/three-tales-from-an-amazon-bar-raiser/
- Memoirs of an Amazon Bar Raiser — Carlos Arguelles / Medium（亲历，做过 700+ 面试）〔一手〕 https://medium.com/geekculture/memoirs-of-an-amazon-bar-raiser-718e36241310
- Amazon Bar Raiser Interview — IGotAnOffer〔二手〕 https://igotanoffer.com/blogs/tech/amazon-bar-raiser-interview

---

## 工作流 5 — 年度规划 OP1 → S-Team goals → OP2

**一句话**：夏天 CEO/CFO 先下**自上而下的投资信封**（收入/人头/成本的框），各团队秋天写**自下而上的 OP1 六页叙事 + 巨型附录**详细计划，高管评审时把其中约 15% 挑成 **S-Team goals**（跨团队的叫 S-2），年底对 Q4 实绩微调成 **OP2** 定稿，全年用 WBR 执行。

### 入门 SOP（新手照着走）

1. **6 月 · 自上而下下框（top-down guidance）**：CEO + CFO 花约两周给出 **"Investment Envelope"（投资信封）**——收入、人头、成本、重点方向的目标起点，防止各团队报出资源需求超盘的幻想计划。〔一手 workingbackwards.com〕
2. **7–8 月 · （可选）愿景务虚会**：2–3 天 offsite 定 vision 文档。
3. **9–10 月 · 各 BU/职能写 OP1（约 4 周）**。**OP1 = 一份 6 页叙事 + 一个巨大的附录**。四块内容：
   - **Metrics**：8–15 个 input + output 指标，带去年实绩、今年预测、明年目标；目标要拆到**年 / 季 / 月、甚至周**。
   - **Initiatives**：所有计划的活儿，每条标 **baseline（现有资源能干）还是 incremental（需额外拨款）**，且必须 **SMART**，带负责人、时间线、资源、对指标的影响。
   - **Resources**：人头增减 + 非人头成本（OPEX/CAPEX），按角色拆、现有 vs 计划。
   - **Org Structure**：为执行计划需要的组织/领导层调整。〔一手 workingbackwards.com / 一手 Dave Anderson〕
4. **10–11 月 · 分部级 OP1 评审** → **11–12 月 · 高管+CEO 评审**：用 6-pager 静默阅读那套开会法，逐个 BU 上来讲、被追问、砍预算。
5. **挑 S-Team goals**：评审中 CEO/S-Team 把约 **15% 的指标/初始项**指定为 **S-Team goals**（最重要、要重点盯的）。**跨职能、需要多团队协作的**标成 **"S-2 goals"**——这个标记自带社会压力，确保各部门的本位目标不会盖过更重要的跨部门目标。〔一手 workingbackwards.com〕
6. **12 月 · 上董事会**。
7. **1 月 · OP2 微调**：Q4 实绩结账后，比对预测 vs 实际的差异，高管 1 月初开会定修订版；OP2 本质是回答**"OP1 之后你实际做成了啥、对比当初计划如何"**。到**1 月底 OP2 成为全年的"record plan"（基准计划）**。〔一手 workingbackwards.com〕
8. **全年执行靠评审节奏**：WBR（周）执行 + MBR（月）+ QBR（季）追 OP 目标进度。中途要改 OP 目标或加资源，**得 S-Team/CEO 批**（故意加的摩擦，防止随意漂移）。

**S-Team goals 的特征**（记住）：高可见、高问责；季度过进度；**目标定得激进——预期只有约 75% 能全达成**；Finance 独立用绿/黄/红追踪。2010 年 Amazon 有 **452 个带 owner/交付物/完成日期的详细目标**；S-Team 会议约 **75% 的时间在过 S-Team goals**。〔一手 workingbackwards.com 引 Bezos〕

### 资深路径（老手跳过 / 优化 / 额外做）

- **老手懂"报价的博弈"**：中层经理写 OP1 时会像**薪资谈判一样虚报**——要 40% 增长明知拿不到、故意 pad（灌水）估算、把低优先级项目标在 **"below the line"（线下）**免得显得不现实。资深评审者也懂这套，所以**很少当场否掉初稿，而是靠预算约束一轮轮往下压**，而不是往上加指导。〔一手 Dave Anderson〕
- **老手不信日历**：TPM 会发一张提交/评审的日期表，但老 Amazon 人"知道大部分日期很快就作废"。资深玩法是盯真正的卡点（Finance review、VP review、S-Team review、CEO review——CEO 只看重要组织），而不是排期表。〔一手 Dave Anderson〕
- **额外做 · 先给约束再收表**：老手带团队做 OP1 会**先给一份全部门项目清单和约束**再让大家填，而不是无约束地收一堆 spreadsheet——"没有约束或部门级项目清单，收上来大概率是一团乱。"〔一手 Dave Anderson〕
- **老手分清 effort-hours vs calendar-time**：常见误区是把"日历时间估算"和"实际工时"混为一谈；资深规划者会把两者拆开估。〔一手 Dave Anderson〕

### 近期变化 / 失败模式

- **AI 辅助规划**：LLM 用来起草 OP1 叙事、汇总各团队 spreadsheet、跑情景/敏感度分析、把去年 WBR 数据自动喂进明年目标推演。风险：AI 生成的"看着很全"的计划稀释了规划过程本该逼出的**真实取舍与判断**。〔推断 + 行业观察〕
- **失败模式 · 名字游戏 / 走形式**：Dave Anderson 直言评审有点"戏剧化（theatrical）"——OP2 常"只是个命名约定"，真价值在前面的辩论，若团队把它当成填表交差，规划就空转。〔一手 Dave Anderson〕
- **失败模式 · 计划做完就锁死**：OP 本该是活的——WBR/PR-FAQ 全年会发现新机会，用现有资源加新 initiative 是允许的（只要不危及 S-Team goals）。把 OP 当成"年初签了就不许动"会错失机会；反过来，随意改又会破坏对齐——所以才有"改目标要 S-Team 批"这个平衡阀。〔一手 workingbackwards.com〕
- **失败模式 · 本位目标压过跨部门目标**：各 BU 只顾自己的 KPI、不管更重要的跨团队 S-2 目标——S-2 标记 + 社会压力就是为治这个而设。
- **失败模式 · 目标不够激进 or 过度激进**：定得太保、100% 能达成 = 没拉伸；定得太狂、全线飘红 = 失去信号。Amazon 校准在"约 75% 达成"。〔一手 workingbackwards.com〕

**来源**：
- The Amazon Operating Cadence — workingbackwards.com（Bryar & Carr）〔一手〕 https://workingbackwards.com/concepts/amazon-operating-cadence/
- A Few Days of OP1 — Perspectives From Middle Management — Dave Anderson / Scarlet Ink〔一手 亲历〕 https://www.scarletink.com/p/few-days-of-op1-perspectives-from-middle-management
- Amazon 2010 Shareholder Letter（Bezos 谈 452 个目标 / goal-setting）〔一手 官方引述〕

---

## 工作流 6 — 事故复盘 Correction of Errors（COE）+ 5 Whys

**一句话**：事故**先止血、再写 COE**；用 5 Whys 一路问到**系统性根因（基础设施/配置/流程），绝不停在"某人犯了错"**；产出 6–8 条带 owner/优先级/截止日的行动项并闭环。COE 的目的是**暴露最该改的地方，不是找谁背锅（blameless）**。

### 入门 SOP（新手照着走）

1. **先止血再复盘**：COE 在事故发生**之后**启动，但"必须先把负面影响缓解掉，才开始 COE 流程"——保证焦点在修复而非甩锅。〔一手 AWS Cloud Operations Blog〕
2. **写 COE 文档（6 块）**：
   - **Incident Summary（事故摘要）**：**最后写**，交代谁受影响、何时、如何——"要写成能作为一封邮件发给公司主要干系人"的样子。
   - **Impact（影响）**：量化业务和客户影响——多少客户受影响、严重度（超收/声誉损失）、受损的非功能需求（安全/可靠/性能）。
   - **Timeline（时间线）**：从**第一个相关事件到系统恢复正常**的逐条时间线；**超过 10–15 分钟的空档必须解释**（否则说明监控/响应有盲区）。
   - **Metrics（指标）**：影响怎么度量、怎么监控；**缺指标本身就是红旗**。
   - **Incident Questions（事故问题）**：围绕**发现 / 诊断 / 缓解 / 预防**四个环节逐一追问。
   - **Action Items（行动项）+ 相关项**：每条带**优先级、owner、截止日**。〔一手 AWS Cloud Operations Blog / workingbackwards.com〕
3. **用 5 Whys 挖根因**：对问题连问 5 次"为什么"，每个答案成为下一个"为什么"的起点，问到你确信挖出了完整因果链为止。**铁律**：若链条冒出"人为失误"，**必须继续问"为什么这个人为失误是可能发生的"**——暴露的是系统缺口，不是个人。Amazon 明确要求 **5-why 链要触达基础设施/配置/流程**；如果你的链条停在"工程师犯了个错"，**这份 COE 会被打回、判定为未完成**。〔一手 AWS / 二手 blog.mischel.com〕
4. **收敛行动项并闭环**：目标 **6–8 条行动项**，典型**内部 14 天 SLA**，要求"具体且可达成"；每条对应 5 Whys 挖出的一个根因；配上新加的监控指标做持续防复发。〔一手 AWS Cloud Operations Blog〕

### 资深路径（老手跳过 / 优化 / 额外做）

- **老手把 timeline 当侦查工具**：资深复盘者盯的是**时间线里的空档和"我们多久才发现"**——检测延迟往往比故障本身更值得修。他们会主动把"发现→诊断→缓解"各段耗时拆出来，找可自动化的环节。〔推断 + 一手 AWS 结构〕
- **老手让 5 Whys 分叉不只线性**：真实事故常有多条根因链；有经验的人不会硬凑成单一线性 5 步，而是每个"why"允许多个答案、并行往下挖（fishbone 式），避免过早收敛到一个假根因。〔推断 + 二手〕
- **额外做 · 行动项分类**：老手把行动项按**预防 / 诊断 / 缓解**三类平衡（不是全堆在"预防"），并给每条标清优先级和真实 owner，防止 14 天 SLA 到期时一堆"待办"无人认领。〔一手 AWS〕
- **老手用 COE 当组织学习资产**：好 COE 会被跨团队传阅、进 correction-of-errors 库，别的团队据此自查同类隐患——单次事故变成全组免疫。

### 近期变化 / 失败模式

- **AI 起草 COE**：AWS 官方（re:Inforce 2024 ARC221 + Cloud Ops 博客）演示用 **Amazon Bedrock/LLM 把事故"事实"变成 COE 初稿**——自动串时间线、汇总影响、生成 5 Whys 草稿，省人力、加速定位与记录。人再复核补判断。〔一手 AWS〕
- **AI 反过来制造事故（重要的近期反转）**：2025 下半年起，Amazon 内部多起**"高爆炸半径（high blast radius）"事故被归因于 GenAI 辅助的代码改动**——生成式编码工具"最佳实践和护栏尚未完全建立"导致不安全实践。回应：Amazon 要求**资深工程师复核初级员工用 GenAI 做的生产改动**、加强制 peer review + 培训（如 12 月 Kiro 工具事故后）。这直接改写了"改动→事故→COE"的前置流程：**AI 写的代码要过人这关**。〔二手 Tom's Hardware / The New Stack，源自内部备忘〕
- **失败模式 · 5-why 停在"人为失误"**：把根因写成"某工程师手滑/没注意"就收尾——违背 blameless 原则，且这份 COE 会被打回。真正的根因是"为什么系统允许这个手滑造成事故"。〔一手 AWS 明列〕
- **失败模式 · COE 变批斗/追责会**：一旦复盘变成找人背锅，团队就会**藏事故、缩小影响、不上报**——COE"最大化暴露待改进处"的目的彻底反转。〔一手 AWS：目的是可见性不是 blame〕
- **失败模式 · 行动项写完不闭环**：6–8 条行动项没 owner、没截止日、SLA 到期无人跟——写了个漂亮 COE，下次同样的事再炸一遍。
- **失败模式 · 没止血就开复盘 / 时间线有黑洞**：影响还没缓解就急着开会复盘；或时间线里大段空白不解释，掩盖了监控和响应的真实盲区。

**来源**：
- Why you should develop a Correction of Error (COE) — AWS Cloud Operations Blog〔一手 官方〕 https://aws.amazon.com/blogs/mt/why-you-should-develop-a-correction-of-error-coe/
- Creating a Correction of Errors document — AWS Cloud Operations Blog〔一手 官方〕 https://aws.amazon.com/blogs/mt/creating-a-correction-of-errors-document/
- Streamlining the COE process using Amazon Bedrock — AWS Cloud Operations Blog〔一手 官方，AI 起草 COE〕 https://aws.amazon.com/blogs/mt/streamlining-the-correction-of-errors-process-using-amazon-bedrock/
- Responding to errors at Amazon — Jim Mischel（亲历转述，5 Whys 须触达基础设施）〔二手〕 https://blog.mischel.com/2018/01/24/responding-to-errors-at-amazon/
- Amazon calls engineers to address GenAI-assisted incidents — Tom's Hardware / The New Stack（2025，内部备忘转述）〔二手 近期〕 https://www.tomshardware.com/tech-industry/artificial-intelligence/amazon-calls-engineers-to-address-issues-caused-by-use-of-ai-tools-report-claims-company-says-recent-incidents-had-high-blast-radius-and-were-allegedly-related-to-gen-ai-assisted-changes

---

## 跨工作流的连结（一图流）

这 6 个工作流不是孤立的，它们咬合成一个操作系统：

- **OP1/OP2（工作流 5）** 定下全年的 S-Team goals 和 input/output 指标 → **WBR（工作流 3）** 每周执行、盯这些指标的异常。
- **WBR** 里"我们本该追踪什么就能避免这次事故"的追问，常直接来自 **COE（工作流 6）** 的行动项，也反过来给下周 WBR 加新指标。
- **Working Backwards / PR-FAQ（工作流 1）** 发起的新业务，其评审用的正是 **6-pager 静默阅读那套开会法（工作流 2）**；PR/FAQ 本身就是一种特殊的叙事文。
- 所有这些流程要跑得动，靠 **Bar Raiser（工作流 4）** 招进来的、真正"高于中位数"的人来撑——招聘质量是整个操作系统的地基。
- 贯穿始终的判断底座：**Type 1（不可逆，慎重）vs Type 2（可逆，快跑）** 决定每个流程该走多重的评审——新产品的 Go/No-Go、招聘的录用、事故的止血，都在问"这是哪型决策"。

> **可复用的元结构**：几乎每个工作流都长这样——① **先写、后议**（PR/FAQ、6-pager、书面反馈、COE、OP1 都是"写作先于开会"）；② **静默阅读**（评审会、debrief 都先沉默读）；③ **input 优先 / 根因优先**（WBR 看 input、COE 挖根因、OP1 定 input 目标）；④ **单一 owner + 明确问责**（每份文档一个作者、每条指标/行动项一个 owner）；⑤ **truth-seeking 而非 selling**（求真不是推销，是所有评审的共同底色）。抓住这五条，任何一个工作流都能自己推导出来。

## Source Manifest

| source_id | url | bucket | last_checked | author/host | note |
|-----------|-----|--------|--------------|-------------|------|
| T03-S001 | https://workingbackwards.com/concepts/working-backwards-pr-faq-process/ | verified_primary | 2026-07-04 | Bryar & Carr | authors' own concept site (originator) |
| T03-S002 | https://www.aboutamazon.com/news/workplace/an-insider-look-at-amazons-culture-and-processes | verified_primary | 2026-07-04 | Amazon (official) | Amazon 官方一手 |
| T03-S003 | https://workingbackwards.com/resources/working-backwards-pr-faq/ | verified_primary | 2026-07-04 | Bryar & Carr | authors' own concept site (originator) |
| T03-S004 | https://www.cnbc.com/2019/10/14/jeff-bezos-this-is-the-smartest-thing-we-ever-did-at-amazon.html | secondary | 2026-07-04 | CNBC | media/analysis about Amazon (secondary) |
| T03-S005 | https://amazonchronicles.substack.com/p/working-backwards-dave-limp-on-amazons | verified_primary | 2026-07-04 | amazonchronicles.substack.com | first-hand |
| T03-S006 | https://commoncog.com/the-amazon-weekly-business-review/ | secondary | 2026-07-04 | Cedric Chin | media/analysis about Amazon (secondary) |
| T03-S007 | https://www.holistics.io/blog/how-amazon-measures/ | verified_primary | 2026-07-04 | holistics.io | first-hand |
| T03-S008 | https://workingbackwards.com/concepts/bar-raiser-hiring/ | verified_primary | 2026-07-04 | Bryar & Carr | authors' own concept site (originator) |
| T03-S009 | https://www.scarletink.com/three-tales-from-an-amazon-bar-raiser/ | verified_primary | 2026-07-04 | Dave Anderson (ex-Amazon) | figure/originator own publication |
| T03-S010 | https://medium.com/geekculture/memoirs-of-an-amazon-bar-raiser-718e36241310 | secondary | 2026-07-04 | medium.com | media/analysis about Amazon (secondary) |
| T03-S011 | https://igotanoffer.com/blogs/tech/amazon-bar-raiser-interview | verified_primary | 2026-07-04 | igotanoffer.com | first-hand |
| T03-S012 | https://workingbackwards.com/concepts/amazon-operating-cadence/ | verified_primary | 2026-07-04 | Bryar & Carr | authors' own concept site (originator) |
| T03-S013 | https://www.scarletink.com/p/few-days-of-op1-perspectives-from-middle-management | verified_primary | 2026-07-04 | Dave Anderson (ex-Amazon) | figure/originator own publication |
| T03-S014 | https://aws.amazon.com/blogs/mt/why-you-should-develop-a-correction-of-error-coe/ | verified_primary | 2026-07-04 | AWS (official) | Amazon 官方一手 |
| T03-S015 | https://aws.amazon.com/blogs/mt/creating-a-correction-of-errors-document/ | verified_primary | 2026-07-04 | AWS (official) | Amazon 官方一手 |
| T03-S016 | https://aws.amazon.com/blogs/mt/streamlining-the-correction-of-errors-process-using-amazon-bedrock/ | verified_primary | 2026-07-04 | AWS (official) | Amazon 官方一手 |
| T03-S017 | https://blog.mischel.com/2018/01/24/responding-to-errors-at-amazon/ | verified_primary | 2026-07-04 | blog.mischel.com | first-hand |
| T03-S018 | https://www.tomshardware.com/tech-industry/artificial-intelligence/amazon-calls-engineers-to-address-issues-caused-by-use-of-ai-tools-report-claims-company-says-recent-incidents-had-high-blast-radius-and-were-allegedly-related-to-gen-ai-assisted-changes | secondary | 2026-07-04 | tomshardware.com | media/analysis about Amazon (secondary) |
