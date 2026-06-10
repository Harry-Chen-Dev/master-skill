# Track 03 — Workflows / SOP — 管理咨询 (Management Consulting)

> locale = global (en-primary) | last_updated = 2026-06-09 | Phase 1 wave 3, Track 03 (工作流 / pipeline).
> 行业 NOT cold — 公开材料丰富，verified_primary 占比高。
> **本 track 灵魂**：每个 workflow 拆「入门 SOP（怎样能把事做完）」+「资深路径（怎样少做几步且更好）」+「近期变化（时效锚点）」+「失败模式自检」。
> **时效核心变量**：GenAI（Lilli / Deckster / ChatGPT Enterprise）正在重写**初级分析师**的 research / 综合 / 做 deck / market sizing 工作流 → 标 decay HIGH。这是本 skill 衰减最快的一节。
>
> Wave 1 + Track 02 seed 极厚：canon 给出 McKinsey 5 步 + Bulletproof 7 步 + ghost-deck 流 + 案例面试流；glossary 给出流程黑话（Day-1 answer / 80-20 / boil-the-ocean / so-what / SteerCo / readout）；tools 给出每个工具的「典型使用场景」直接对应 SOP 步骤 + GenAI 冲击 + 幻觉事故。本 track 把碎片拼成完整 SOP。

---

## Source Manifest

| source_id | url | bucket | last_checked | author/host | one-line note |
|-----------|-----|--------|--------------|-------------|---------------|
| T03-S001 | https://www.amazon.com/McKinsey-Way-Ethan-M-Rasiel/dp/0070534489 | secondary | 2026-06-09 | Amazon (Rasiel) | The McKinsey Way 元数据 — 定义→根因→假设→分析→建议 5 步 |
| T03-S002 | https://caseinterview.com/issue-tree | verified_primary | 2026-06-09 | Victor Cheng | issue tree / hypothesis-driven 解题流官方教学 |
| T03-S003 | https://caseinterview.com/case-in-point | verified_primary | 2026-06-09 | Victor Cheng | 案例面试解题流 + market sizing |
| T03-S004 | https://caseinterview.com/personal-experience-interview | verified_primary | 2026-06-09 | Victor Cheng | PEI / fit 行为面流程 |
| T03-S005 | https://www.barbaraminto.com/ | verified_primary | 2026-06-09 | Barbara Minto | 金字塔/SCQA → storyline → deck 沟通流 |
| T03-S006 | https://www.mckinsey.com/capabilities/strategy-and-corporate-finance/our-insights/inside-the-strategy-room-podcast | verified_primary | 2026-06-09 | Sean Brown / McKinsey | partner+CEO 谈真实战略制定流程（engagement 叙事） |
| T03-S007 | https://www.mckinsey.com/capabilities/tech-and-ai/how-we-help-clients/rewiring-the-way-mckinsey-works-with-lilli | verified_primary | 2026-06-09 | McKinsey & Company | Lilli GenAI 重写 research/综合/做 deck 流（72% 员工 / ~30% 省时）|
| T03-S008 | https://www.computerworld.com/article/3491334/bcg-execs-ai-across-the-company-increased-productivity-employee-joy.html | secondary | 2026-06-09 | Computerworld | BCG Deckster 造 deck 流 + Review This 自检 rubric（450K+ 次）|
| T03-S009 | https://fortune.com/2025/11/25/deloitte-caught-fabricated-ai-generated-research-million-dollar-report-canada-government/ | secondary | 2026-06-09 | Fortune | Deloitte AI 幻觉伪造引用事故 → 「人是 last verifier」失败模式 |
| T03-S010 | https://hbr.org/2021/02/are-you-doing-the-swot-analysis-backwards | verified_primary | 2026-06-09 | HBR | framework-as-theater 失败模式（套框架不推 so-what）|
| T03-S011 | https://bulletproofproblemsolving.com/ | secondary | 2026-06-09 | Conn & McLean (官方) | Bulletproof 7 步官方站（书/课）— 配合 [T04-S035] 锚定 7 步 |
| T03-S012 | https://www.lek.com/industries/private-equity-pe/commercial-due-diligence-cdd | verified_primary | 2026-06-09 | L.E.K. Consulting | CDD 专精 boutique 一手：市场吸引力/竞争位势/客户/增长可持续性 |
| T03-S013 | https://www.oliverwyman.com/our-expertise/capabilities/mergers-and-acquisitions/buy-side-due-diligence.html | verified_primary | 2026-06-09 | Oliver Wyman | buy-side 战略尽调一手（精品所流程口径）|
| T03-S014 | https://umbrex.com/resources/mckinsey-problem-solving/ | secondary | 2026-06-09 | Umbrex (ex-McKinsey network) | 独立顾问网络（多前麦）整理的 McKinsey 7 步 + workplan 四列 |
| T03-S015 | https://strategyu.co/consulting-presentations/ | secondary | 2026-06-09 | StrategyU (Paul Millerd, ex-BCG/McKinsey) | ex-MBB 作者拆 deck 五步（ghost deck → 数据 → review）|

> **分类说明**：caseinterview.com（Victor Cheng 本人站，ex-McKinsey，已在 source_verifier PRIMARY 白名单）/ barbaraminto.com / mckinsey.com / hbr.org / lek.com / oliverwyman.com = `verified_primary`（framework 原作者 + firm/精品所一手；后两者经 `source_verifier.py classify` 确认在 PRIMARY 白名单）。Amazon / bulletproofproblemsolving.com（作者官方但 verifier 判 unknown host）/ Umbrex / StrategyU = `secondary`（前麦/前 BCG 从业者整理，质量较高但非 firm 一手，**不 solo-anchor 心智模型**，仅作 SOP 步骤佐证 + 配合 Wave 1 一手 [T04-S035/S037] 使用）。Computerworld / Fortune = `secondary`（一手事件转述）。**无知乎/公众号/百度/CSDN/Quora/SEO 站/AI 摘要站/LinkedIn 帖入表**。本 track 大量复用 Wave 1（[T04-Sxxx] / [T06-Sxxx]）+ Track 02（[T02-Sxxx]）已落盘 source 作为跨轨 evidence（同 URL 跨 track 共用 ID 合规）。

> **一手 vs 二手 caveat（诚实边界）**：本 track 的 engagement-lifecycle / 周节奏等「项目运作」细节，firm 官方很少公开**完整流程图**（属 know-how）；可得的最佳一手是 ① 方法论书（Minto/Rasiel/Bulletproof，[T04-S001/S037/S035]）② Victor Cheng 案例面试站（[T03-S002/S003/S004]，反映 firm 解题流）③ firm 官方谈 GenAI 如何改流程（[T03-S007], [T02-S003]）。流程的「运作层」细节（SteerCo 节奏 / SOW 模板）多靠 ex-MBB 从业者整理（Umbrex/StrategyU = secondary）+ 通用项目治理实践佐证。**verified_primary 锚定方法论内核，secondary 补运作细节** —— 已在每条 claim 的 evidence 标注。

---

## 总览（按 decay risk 分组）

### High decay (12-month-class) — 见各 workflow「近期变化」字段
| Workflow | 受 GenAI 冲击的步骤 | 触发 | Last_updated |
|---------|---------------------|------|-------------|
| (1) Engagement 全流程 | research / 综合 / 做 deck 子步 | Lilli/Deckster/ChatGPT (2023-2025) | 2026-06-09 |
| (2) 假设驱动问题解决 | research/分析子步加速 | 同上 | 2026-06-09 |
| (3) Deck / storyline | 造初稿 + 美化 + Review 自检 | Deckster 2024-03 | 2026-06-09 |

### Low / Medium decay（方法论内核稳定）
| Workflow | Trigger | Output | Last_updated | Decay |
|---------|---------|--------|-------------|-------|
| (1) Engagement 全流程 | RFP / 客户问题 | 建议 deck + 汇报 (+ 落地) | 2026-06-09 | medium（节奏变，骨架稳）|
| (2) 假设驱动问题解决 | 模糊大问题 | 验证过的 so-what + 建议 | 2026-06-09 | low（方法论内核）|
| (3) Deck / storyline | 要跟高管沟通 | 一句话结论 deck | 2026-06-09 | medium（手艺稳，造稿被 AI 改写）|
| (4) Case interview | 求职/招聘 | offer / ding | 2026-06-09 | low（面试形式稳）|
| (5) 客户/项目管理 | 项目进行中 | 对齐 + readout 节奏 | 2026-06-09 | medium（远程节奏变）|
| (6) Commercial DD | PE 投前 | 投/不投 view | 2026-06-09 | low（流程稳，研究子步被 AI 加速）|

---

## Workflow 详细卡片

<!-- 骨架先行；每个 ### 含 One-liner / Trigger / Output / 入门 SOP（每步跳过后果）/ 资深路径（skip/optimize/add ≥2）/ 近期变化 / 典型耗时 / 关键工具 / 关键人物 / 常见失败模式 / Last_updated / Decay risk -->

### 1. 项目交付全流程（engagement / case lifecycle）

- **One-liner**: 从客户问题（或 RFP）到交付建议（+ 落地）的完整闭环 —— 把一个模糊的商业难题，经「卖项目 → 定问题 → 搭假设 → 做分析 → 综合 → 讲故事 → 汇报」变成客户能据以决策/行动的产出。这是咨询「the case / study / engagement」的母流程，其它所有 workflow（2/3/5/6）都是它的子环节或并行支线。
- **Trigger**: 客户发 RFP（招标书）/ partner BD 谈下一个机会 / 客户高管带着一个「增长停滞、要不要进某市场、成本太高」的问题上门。(evidence: [T06-S019, T03-S006])
- **Output**: 一份建议 deck（金字塔结构 + action title）+ 现场 readout 汇报 + 通常一个 Excel 模型；战略落地型项目还含 implementation roadmap / 交接。(evidence: [T04-S001, T06-S019])
- **入门 SOP（minimum viable steps）**:
  1. **提案 (RFP → proposal → SOW)**：响应 RFP 或主动提案，写 proposal（问题 + 范围 + 方法 + 团队 + 报价 + 时间线），赢单后落 SOW（scope of work，界定边界/交付物/排期）。proposal 本身常就是一份 deck。(evidence: [T03-S015scope:RFP→SOW 业内通识], [T06-S019])
     - *跳过后果*：无 SOW = scope creep（范围无限膨胀），客户中途加需求无依据拒绝，团队做到死还被嫌没交付到位。
  2. **Kickoff（启动会）**：与客户高管 + SteerCo 对齐项目目标、「什么算成功」、关键利益相关方、数据访问、节奏。(evidence: [T03-S006steerco-kickoff], 周节奏见 workflow 5)
     - *跳过后果*：团队跟客户对「要解决什么」理解错位，两周后 readout 才发现做的是另一个问题，返工。
  3. **问题定义（最关键 — 真问题 vs 表象问题）**：把模糊主诉收敛成一个**具体、有边界、可验证**的问题陈述（problem statement）；区分客户**说**的问题（表象）和**真正**该解的问题（根因）。McKinsey/Bulletproof 都把这步列为「整个项目最重要的一步，它是后续所有工作的导航」。(evidence: [T04-S035, T03-S014])
     - *跳过后果*：问题定义错 = 整个项目方向错。「漂亮地解决了错误的问题」是咨询头号灾难；后面分析做得再精也无效。
  4. **假设树 / issue tree（结构化）**：把问题 MECE 地拆成可分析的子问题（issue tree）或可证伪的子假设（hypothesis tree）—— 见 workflow 2。同时立 **Day-1 初步假设答案**。(evidence: [T03-S002, T04-S037])
     - *跳过后果*：没有结构 → 团队各查各的、分析重叠又漏关键分支，最后拼不成一个完整论证。
  5. **Workplan（工作计划）**：给每个优先 issue/假设排「分析内容 / 终产品（end product）/ 数据源 / 时间与负责人」四列。(evidence: [T03-S014workplan-4col, T04-S035])
     - *跳过后果*：工时失控、deadline 前发现关键分析没人做；boil the ocean（什么都分析、没重点）。
  6. **分析 + 建模 + 专家访谈（execute）**：跑分析验证/证伪假设 —— Excel 建模（driver tree / market sizing）、secondary research（行业数据库）、primary research（专家网络 expert call）、客户访谈。(evidence: [T02-S009expert-call, T02-S013data, 见 Track 02])
     - *跳过后果*：假设没有事实支撑 = 凭直觉拍脑袋的建议，经不起 SteerCo 追问，客户不买账（fact-based 是底线）。
  7. **综合 (synthesis)**：把零散分析「所以呢 (so-what)」成一个统领性洞见（governing thought）—— 不是罗列发现，是提炼出对决策意味着什么。(evidence: [T04-S041synthesis, T06-S009so-what])
     - *跳过后果*：交一堆「我们发现了 X、Y、Z」的数据，客户问「所以我该干嘛？」答不出 —— 这是分析员和咨询师的分水岭。
  8. **建议 deck + 汇报 (storyline → readout)**：用金字塔/SCQA 搭 storyline → ghost deck → 填数据 → 现场向 SteerCo readout —— 见 workflow 3 + 5。(evidence: [T04-S001, T03-S015])
     - *跳过后果*：洞见再好，沟通失败（结论埋在第 40 页、没 action title）= 高管 get 不到、决策不了，项目白做。
  9. **落地 / 交接 (implementation / handoff)**（视项目）：战略+落地两速型项目交 implementation roadmap、建能力、交接给客户团队。(evidence: [T06-S019implementation])
     - *跳过后果*：纯 deck 交付、不管落地 = 「借表读时间」的批评坐实；建议躺在抽屉里，客户下次不续约。
- **资深路径（差异点）**：
  - **skip — 资深人跳过「穷举式 research 再归纳」**：不从 step 6 的海量数据出发，而是 Day-1 就基于经验给出**初步假设答案 (Day-1 answer)**，用 80/20 直接锁定 2-3 个最可能驱动分支，**只分析能验证/证伪假设所需的最小数据**（~80% 把握即止，bias for speed over 100% certainty）。新人倾向「先把所有数据查全再说」→ boil the ocean。(evidence: [T03-S002, T06-S009, T04-S037])
  - **optimize — 把 step 3 问题定义 + step 8 storyline 在项目极早期就做**：资深 EM/partner 在 kickoff 后几天内就先写出「假想的最终 deck storyline」（一句句 action title 串成的论证），让后续分析**反向服务于故事线**，而非分析完才想怎么讲。这把 step 4-8 从串行压成「目标驱动」。(evidence: [T03-S015, T04-S001])
  - **add — 资深人额外做「随时 kill 假设 + so-what 自检」**：每轮分析后主动问「这个证据是不是在证伪我的假设？我是不是只在找支持证据（confirmation bias）？」+ 「这页的 so-what 是什么」。新人容易只找支持证据、把假设当结论硬凑。(evidence: [T06-S009hypothesis-discipline, T04-S033confirmation-bias])
  - **add — 资深人额外管「client impact / 利益相关方」**：不只解智识问题，还在过程中持续对齐 SteerCo、管好客户高管的预期与政治（见 workflow 5），确保建议**能被采纳并落地**，而非交一份漂亮但没人执行的 deck。(evidence: [T03-S006, T06-S019])
- **近期变化**（近 12 个月，decay HIGH 的子步）:
  - **2023-2025 起，由 GenAI（McKinsey Lilli / BCG Deckster / ChatGPT Enterprise 全员）触发**：step 6（research/综合）+ step 8（造 deck 初稿）被部分自动化。McKinsey 官方称 Lilli 检索 10 万+ 内部文档、72% 员工活跃、报最高 ~30% research/综合时间节省；BCG Deckster 已造/改 450K+ slide。→ **初级分析师在 engagement 中「查资料 + 综合 + 出 deck 初稿」的杠杆角色被重构**。(evidence: [T03-S007, T03-S008], 交叉 [T02-S003, T02-S007])
  - **当前采用率（firm 自报）**: Lilli 72% 员工活跃 / 500K+ prompts 月（McKinsey 一手，标 caveat）；ChatGPT Enterprise 已铺到 Bain/BCG/PwC 全员。(evidence: [T03-S007])
  - **远程/混合改写经典「周一到周四驻场」节奏**（疫情后）：传统「咨询师周一飞到客户现场、周四飞回」的驻场模型已部分被远程/混合取代，kickoff/readout 仍倾向现场但日常分析远程化（影响 workflow 5 的节奏）。触发：2020 疫情，已固化为新常态。(decay medium，行业结构性变化)
  - **向 implementation / digital transformation 倾斜（两速：战略 + 落地）**：纯「给建议 deck 就走」的交付减少，step 9（落地）权重上升，MBB 也建数字/落地单元（BCG X）。触发：客户要 ROI 不要 PPT + Big Four 落地能力竞争。(decay medium)
- **典型耗时**:
  - 入门 SOP: 一个标准 engagement 6-12 周（MBB 战略项目典型）；问题定义 + workplan 占头 1-2 周。
  - 资深路径: 流程不变但「无效工时」大幅压缩 —— Day-1 假设 + 80/20 让资深团队用同样时间做更深、或更快收敛。
- **关键工具（与 Track 02 关联）**:
  - PowerPoint + think-cell（deck，必备）/ Excel（建模，必备）/ 专家网络 GLG·AlphaSights（primary research，必备）/ 行业数据库 Capital IQ·IBISWorld（secondary，必备）/ GenAI Lilli·Deckster·ChatGPT（新兴，HIGH）。(evidence: [T02-S001, T02-S009, T02-S013, T02-S003])
- **关键人物（与 Track 01 / 04 关联）**:
  - Ethan Rasiel《The McKinsey Way》详述 5 步（定义→根因→假设→分析→建议）[T04-S037]；Conn & McLean《Bulletproof Problem Solving》详述 7 步 [T04-S035]；McKinsey "Inside the Strategy Room" podcast 中 partner + CEO 谈真实 engagement [T03-S006]。
- **常见失败模式**:
  - **漂亮地解决了错误的问题**：跳过/草率做 step 3，把客户的表象主诉当真问题。触发：急着进分析、不敢花时间在问题定义上。避免：kickoff 后用 1-2 天专门压问题陈述，向客户确认「我们解的是这个，对吗」。**actionable 自检**：「我能用一句话写出有边界、可验证的问题陈述吗？客户签字认可了吗？」
  - **Boil the ocean（把海煮干）**：没立 Day-1 假设 + 没用 80/20，试图分析所有分支到 100% 精度，deadline 前崩盘。避免：先立初步假设答案，砍掉对结论无影响的长尾分析。**自检**：「这个分析如果做了，会改变我的建议吗？不会就别做。」
  - **Confirmation bias（先射箭后画靶的暗面）**：假设驱动滥用成「只找支持自己假设的证据」。避免：每轮主动找**证伪**证据，准备好 kill 假设换靶。**自检**：「我上一个被数据推翻的假设是哪个？如果一个都没有，我可能在自我确认。」
  - **交分析不交综合（答不出 so-what）**：step 7 缺失，交一堆 what 没有 so-what。避免：每个 exhibit/页强制写 action title（结论句）。**自检**：「把所有 action title 连起来读，是不是一个完整的『所以你该这么做』的论证？」
  - **纯 deck 交付、不管落地**：跳过 step 9，建议无法执行。避免：建议里带 owner + timeline + 预期影响，必要时帮客户建落地能力。**自检**：「这份建议，客户明天能照着动手吗？谁负责？」
- **Last_updated**: 2026-06-09（方法论内核 last-anchored 至 Minto 1978 / Rasiel 1999 / Bulletproof 2018；GenAI 子步 anchored 至 2024-2025 firm 披露）
- **Decay risk**: **medium**（骨架流程结构性稳定 40+ 年 = low；但 step 6/8 的 research/做 deck 子步受 GenAI 改写 = HIGH；远程节奏 + 落地倾斜 = medium。**整体标 medium，GenAI 子步单独 HIGH**）

### 2. 假设驱动问题解决（hypothesis-driven problem solving）

- **One-liner**: 咨询的「思考引擎」—— 把一个模糊大问题，经「定义 → MECE 拆 issue tree → 立可证伪假设 → 设计分析验证/证伪 → 迭代」收敛成有事实支撑的答案。这是 workflow 1 的核心子流程，也是案例面试（workflow 4）考的东西，是这一行最可标准化、最易蒸出高质量的方法论。
- **Trigger**: 拿到一个「为什么利润下滑 / 要不要进这个市场 / 怎么把成本降 20%」的模糊商业问题，且不能靠穷举所有数据来答（时间/成本不允许）。(evidence: [T03-S002, T06-S009])
- **Output**: 一个被事实**验证或证伪**的答案（governing thought）+ 支撑它的 MECE 论据结构，可直接喂给 synthesis（workflow 1 step 7）和 deck（workflow 3）。(evidence: [T04-S037])
- **入门 SOP（minimum viable steps）**:
  1. **定义问题**：写出具体、有边界、可验证的问题陈述（同 workflow 1 step 3）。(evidence: [T04-S035, T03-S014])
     - *跳过后果*：拆出来的树是「针对错误问题的完美结构」，全盘无效。
  2. **MECE 拆 issue tree（结构化）**：把核心问题逐层向右拆成**相互独立、完全穷尽**的子问题，每个叶子能 yes/no 或量化验证。常用 driver tree（利润 = 量 × 价 − 成本…）做定量骨架。(evidence: [T03-S002, T06-S004, T06-S007])
     - *跳过后果*：没结构 → 漏掉关键分支（CE 失败）或重复分析（ME 失败），论证有洞、客户能戳破。
  3. **提假设（hypothesis）**：对每个关键分支立一个**可证伪**的假设（「我猜利润下滑主因是低端机型萎缩」）；项目级别立 Day-1 答案假设。(evidence: [T04-S037, T03-S002])
     - *跳过后果*：退化成「无目标地把每个分支都查一遍」= boil the ocean，慢且没重点。
  4. **设计分析去验证/证伪**：为每个假设设计**最小必要分析**（哪个数据/模型/专家访谈能 kill 或 confirm 它），而非穷举。(evidence: [T03-S002, T06-S009])
     - *跳过后果*：做了一堆和假设无关的分析，工时浪费；或分析设计不当，证不了也证伪不了。
  5. **跑分析 + 迭代**：执行分析，看证据。假设被证伪 → 回到 tree 换一个分支/假设重来；被支持 → 深挖并锁定。循环到收敛。(evidence: [T04-S037, T04-S035])
     - *跳过后果*：第一个假设错了却不迭代，硬往错方向走到底。
- **资深路径（差异点）**：
  - **skip — 资深人跳过「自下而上穷举」**：不从数据归纳（bottom-up），直接 top-down 立 Day-1 假设，**只做能验证假设的分析**，~80% 把握即收手（bias for speed）。新人偏 bottom-up「数据齐了才敢有观点」。McKinsey 顾问明确 bias toward top-down。(evidence: [T06-S009, T03-S002])
  - **optimize — 资深人用 80/20 剪枝 issue tree**：拆完树后立刻砍掉对结论影响小的分支（prune the tree，Bulletproof step 3），只在 2-3 个高杠杆分支上投入。新人倾向把每个分支都拆深、都分析。(evidence: [T04-S035, T06-S009])
  - **add — 资深人额外「主动证伪自己」**：经验告诉他们最大风险是 confirmation bias，所以**刻意去找能 kill 假设的证据**、随时准备换靶。这是「假设驱动的纪律」对「假设驱动的滥用」的关键分野。新人把假设当结论、只找支持证据。(evidence: [T06-S009, T04-S033])
  - **add — 资深人额外做 "quick-and-dirty" 先验证再深挖**：对一个假设先用 back-of-envelope / 一两个专家 call 做粗略验证，确认方向对了再投入精细分析，避免在错误方向上精雕细琢。(evidence: [T03-S002, T06-S009])
- **近期变化**（近 12 个月）:
  - **2023-2025，GenAI 加速「设计分析 + 跑分析」子步**：Lilli/ChatGPT 用于检索既往 case、生成市场 research 初稿、综合多文档要点，把 step 4-5 的信息搜集环节从天级压到分钟级。但**方法论内核（定义→MECE→假设→证伪→迭代）不变** —— GenAI 改的是「执行分析有多快」，不是「怎么思考」。(evidence: [T03-S007], 交叉 [T02-S003])
  - **新增风险环节**：GenAI 会幻觉（Lilli 曾引用不存在的法规），所以「用 AI 跑分析」后**必须人工核验数字/引用落到可追溯来源**才算数 —— 这是假设验证流程里新加的一道闸（见失败模式）。(evidence: [T03-S009], 交叉 [T06-S021])
  - **方法论本体 decay: low** —— MECE / issue tree / hypothesis-driven 稳定 40+ 年，是 master skill 最硬的内核（intake warning b：最标准化、最易蒸高质量）。
- **典型耗时**:
  - 入门 SOP: 一个完整 issue tree + 首轮假设验证 ~几天到 1-2 周（取决于分析复杂度）。
  - 资深路径: Day-1 假设 + 80/20 剪枝让首个可信答案出现得快得多（quick-and-dirty 验证可能 1-2 天就定方向）。
- **关键工具（与 Track 02 关联）**:
  - issue tree / MECE / driver tree（概念工具，必备）/ Excel（建模验证）/ 专家网络（primary 验证）/ 行业数据库（secondary）/ GenAI（检索综合，HIGH）。(evidence: [T02-S013, T02-S009])
- **关键人物（与 Track 01 / 04 关联）**:
  - Victor Cheng（caseinterview.com，hypothesis-driven + issue tree 事实标准教学）[T03-S002]；Ethan Rasiel《McKinsey Way》（IH 初始假设 + 事实基础）[T04-S037]；Conn & McLean《Bulletproof》（7 步含 disaggregate/prioritize/prune）[T04-S035]。
- **常见失败模式**:
  - **拆桶重叠又漏项（MECE 失败）**：issue tree 的子项互相打架或漏掉关键分支。避免：每层拆完检查「这些桶有重叠吗？合起来穷尽吗？」**自检**：「把这层所有桶加起来，等于上一层吗？有没有哪个东西能同时归两个桶？」
  - **把 issue tree 做成发散 mind map**：每支不指向可验证假设，沦为头脑风暴图。避免：强制每个叶子写一个能 yes/no 或量化检验的假设。**自检**：「这个叶子节点，我能设计一个分析去证伪它吗？不能就不是 issue tree。」
  - **Confirmation bias（先有结论硬凑证据）**：把假设当既定结论，只找支持证据。避免：每个假设都主动设计一个能证伪它的分析。**自检**：「如果我的假设是错的，会是什么数据告诉我？我去找那个数据了吗？」
  - **Boil the ocean（不会 80/20）**：不剪枝、每个分支都查到底。避免：拆完树立刻 prune，只攻 2-3 个高杠杆分支。**自检**：「这个分支就算分析出来，会改变最终建议吗？不会就剪掉。」
  - **GenAI 跑出的分析不核验就用**：AI 幻觉的数字/引用直接进结论。避免：AI 输出的每个 claim 落到可追溯原始来源才采信。**自检**：「这个数字/引用，我能点到原始来源吗？还是只是 AI 说的？」(evidence: [T03-S009])
- **Last_updated**: 2026-06-09（方法论 anchored Minto/Rasiel/Cheng/Bulletproof；AI 加速子步 anchored 2024-2025）
- **Decay risk**: **low**（方法论内核 40+ 年稳定；仅「执行分析的工具」受 GenAI 改写，思考框架不变）

### 3. Deck / storyline 构建（核心手艺）

- **One-liner**: 把分析结论变成高管能秒懂、能决策的 deck —— 经「定 governing thought → SCQA 开场 → 搭 ghost deck 骨架 → 写 action title（每页一句话结论）→ 填数据图 → so-what 自检 → review」。deck 是咨询的母语，这是这一行最核心、最难替代的手艺。
- **Trigger**: 分析做到一定程度、要向客户高管/SteerCo 汇报或交付建议。**注意资深做法是更早触发**（见 optimize）。(evidence: [T04-S001, T03-S015])
- **Output**: 一份金字塔结构 deck —— 一句话总结论（governing thought）领头，下挂 MECE 分组论据，每页一个 action title，exec summary 装下全部建议；executive 只读 action title 就能 get 整个论证（titles test）。(evidence: [T04-S001, T03-S015])
- **入门 SOP（minimum viable steps）**:
  1. **定 governing thought（统领思想）**：先确定整个 deck 要传达的那**一句话核心结论 / 建议**（金字塔塔尖）。(evidence: [T04-S001])
     - *跳过后果*：deck 没有中心论点，沦为「数据页的集合」，高管读完不知道你到底建议什么。
  2. **SCQA 搭开场故事线**：用 Situation（情境）→ Complication（冲突）→ Question（疑问）→ Answer（回答 = governing thought）框住「为什么现在要解决这个、答案是什么」。(evidence: [T04-S001, T06-S015])
     - *跳过后果*：开头直接堆背景、没有 complication，高管 get 不到「关我什么事 / 为什么紧迫」，注意力流失。
  3. **搭 ghost deck（鬼影稿 / 骨架先行）**：做一份 ~20% 完成度的骨架 —— 只写每页的 action title + 占位空白 exhibit，**先把整条论证逻辑（storyline）跑通并对齐**，再碰数据和美化。「never open PowerPoint until your logic is flawless」。(evidence: [T03-S015, T06-S015])
     - *跳过后果*：一上来做精美成品页，storyline 一改，几十页全部重做 —— 返工灾难。
  4. **写 action title（每页一句话结论）**：每页标题写成**完整结论句**（「收入因低端机型萎缩下滑 12%」）而非主题词（「收入分析」），一页一条信息。(evidence: [T04-S001, T06-S015])
     - *跳过后果*：标题是主题词 → 高管得自己从图里猜结论，titles test 失败，论证链断裂。
  5. **填数据图（exhibit）**：每页配一个支撑该 action title 的图表（waterfall / Marimekko / 趋势图），think-cell 一键生成 + 链 Excel。(evidence: [T02-S001])
     - *跳过后果*：action title 是断言但没有证据支撑 = 「凭空结论」，SteerCo 一问数据就崩。
  6. **so-what 自检**：逐页问「这页的 so-what 是什么 / 对决策意味着什么」；把所有 action title 串起来读，检查是不是一条完整论证 = 这就是 executive summary。(evidence: [T06-S009, T04-S001])
     - *跳过后果*：交一堆 what 没 so-what，高管问「所以呢」答不出 —— 咨询师 vs 分析员的分水岭。
  7. **Review（EM/partner 审）**：资深人按「storyline 通不通 / action title 是不是结论句 / 图表卫生 / so-what 够不够硬」过一遍，反复打磨。(evidence: [T03-S008review-rubric, T03-S015])
     - *跳过后果*：逻辑漏洞/低级错误带到客户面前，损害团队信誉。
- **资深路径（差异点）**：
  - **skip — 资深人跳过「分析完才想怎么讲」**：不等分析全做完，**项目早期就先写假想 storyline（ghost deck）**，让分析反向服务故事线。新人是「先把分析做完，再坐下来想这个 deck 怎么组织」—— 顺序反了，导致大量分析最后用不上、关键论点缺数据。(evidence: [T03-S015, T04-S001])
  - **optimize — 资深人把 storyline 当「思考工具」而非「汇报工具」**：写 action titles 串起来 = 倒逼自己检查论证是否完整、有没有逻辑跳跃 —— deck 在分析阶段就用来发现论证漏洞，而不只是最后包装。(evidence: [T04-S001, T03-S015])
  - **add — 资深人额外做「action titles 连读 = exec summary」自检**：把全 deck 的 action title 抽出来连读，必须自成一篇「所以你该这么做」的完整论证；读不通就说明 storyline 有断点。新人不做这一步，页对了但整体不连贯。(evidence: [T04-S001])
  - **add — 资深人额外守「一页一信息 + titles test」**：刻意控制每页只讲一件事，并用 titles test（只读标题能否懂全文）做硬门槛。新人一页塞多个论点、标题写主题词。(evidence: [T06-S015, T03-S015])
- **近期变化**（近 12 个月，decay HIGH）:
  - **2024-03 起，BCG Deckster（GenAI 造 deck 工厂）改写「填数据图 + 美化 + review」子步**：「One-Click Draft」吃 outline/prompt 出成品 slide；「Review This」按 BCG 设计 rubric（MECE 结构 / 标题清晰 / 图表卫生）自动打分 + 行内建议，把资深 associate 的格式反馈变成「always-on coach」。已造/改 450K+ slide。→ step 5（填图）+ step 7（review 的格式层）被部分自动化。(evidence: [T03-S008], 交叉 [T02-S007, T02-S008])
  - **但 step 1-3 + 6（governing thought / SCQA / storyline / so-what 跳跃）仍需人脑**：自动美化 ≠ 自动产生洞见；GenAI 能把 outline 变 slide，但「这个 so-what 对不对、storyline 通不通」是 AI 短期替代不了的核心手艺。(evidence: [T03-S008])
  - **当前采用率**: Deckster 450K+ 次使用（BCG 一手），是 firm 内部最快扩张的内部 app 之一；外部团队用 ChatGPT/Copilot 出 outline + Copilot 在 PPT 内生成草稿。(evidence: [T03-S008], 交叉 [T02-S007])
- **典型耗时**:
  - 入门 SOP: 一份汇报 deck 从 storyline 到成品数天（反复 review）；新人常因 step 3 没做好而返工翻倍。
  - 资深路径: ghost-deck-first + GenAI 造初稿让「出第一版可看 deck」快得多；但打磨 so-what/storyline 的时间不省。
- **关键工具（与 Track 02 关联）**:
  - PowerPoint + think-cell（事实标准，必备）/ Mekko·UpSlide（Mac/预算替代）/ BCG Deckster·ChatGPT·M365 Copilot（GenAI 造 deck，HIGH）。(evidence: [T02-S001, T02-S007])
- **关键人物（与 Track 01 / 04 关联）**:
  - Barbara Minto《The Pyramid Principle》（结论先行 + SCQA + action title 的发明者，咨询沟通圣经）[T04-S001, T03-S005]；StrategyU（ex-BCG/McKinsey）拆 deck 五步 [T03-S015]。
- **常见失败模式**:
  - **先做精美页、后想 storyline（不用 ghost deck）**：方向一改几十页全废。避免：storyline/ghost deck 没敲定前不碰美化。**自检**：「我现在的 PPT，逻辑链跑通了吗？还是在没想清楚时就开始排版？」
  - **action title 写成主题词而非结论句**：「市场概览」而非「该市场年增 18%、值得进入」。避免：每个标题强制写成有主谓宾的断言。**自检**：「只读这页标题，读者知道我的结论吗？还是只知道这页『讲什么』？」
  - **结论埋在最后（违背结论先行）**：按分析/时间顺序讲，把 answer 放第 40 页。避免：金字塔 —— governing thought 开头就给。**自检**：「高管只看前 3 页 exec summary，能拿到全部建议吗？」
  - **填了一堆图但答不出 so-what**：exhibit 漂亮但没洞见跳跃。避免：每页过 so-what 自检。**自检**：「这页的图说明了什么 → 所以客户该做什么？答不出就删或重做。」
  - **action titles 连读不成一篇论证**：单页对、整体散。避免：抽出所有 action title 连读，补断点。**自检**：「把所有标题抄下来连读，是不是一篇完整的『诊断 → 所以建议 X』？」
  - **GenAI 造的 slide 数据没核验就交**（新增，decay HIGH）：Deckster/Copilot 出的图表数字可能是幻觉。避免：AI 生成内容人工核验落到来源（Deloitte 退款殷鉴）。**自检**：「这张 AI 生成的图，数字我对过原始数据了吗？」(evidence: [T03-S009])
- **Last_updated**: 2026-06-09（金字塔/SCQA/action title anchored Minto 1978；GenAI 造 deck anchored Deckster 2024-03）
- **Decay risk**: **medium**（核心手艺 governing thought/storyline/so-what 稳定 = low；填图/美化/格式 review 子步被 GenAI 改写 = HIGH。**整体 medium，AI 造 deck 子步单独 HIGH**）

### 4. Case interview（招聘 / 入行）

- **One-liner**: 进咨询的「守门流程」—— 面试官给一个商业问题，候选人当场「复述+澄清 → 搭 MECE 结构 → 分析 → market sizing → recommendation」，考的就是 workflow 2（假设驱动问题解决）+ workflow 3（结论先行沟通）的现场压缩版；外加 fit/PEI 行为面。
- **Trigger**: 申请 MBB / Big Four 战略臂 / 精品所，过网申+笔试后进入面试轮。(evidence: [T03-S003, T06-S008])
- **Output**: offer 或 ding（被拒）；面试官评估候选人是否具备 structure（MECE）+ 量化（market sizing）+ so-what（洞见）+ 沟通 + fit。(evidence: [T03-S003, T06-S008])
- **入门 SOP（minimum viable steps）**:
  1. **听题 + 复述 + 澄清**：拿到 case prompt，复述确认理解，问 2-3 个澄清问题（目标是什么？范围？成功标准？）。(evidence: [T03-S003])
     - *跳过后果*：理解错题目就开始答，结构再漂亮也是解错问题；面试官直接判负。
  2. **搭结构（MECE issue tree）**：花 30-60 秒在纸上搭一个 MECE 的拆解结构（资深做法是 hypothesis-driven 而非死套框架）；讲给面试官听，对齐路径。(evidence: [T03-S002, T06-S007])
     - *跳过后果*：无结构地东想西想 = 暴露「不会结构化模糊问题」，这是 case 最核心的考点，必挂。
  3. **分析（按结构推进）**：沿结构逐支分析，要数据就向面试官要，边算边说思路；遇定量分支做计算。(evidence: [T03-S003])
     - *跳过后果*：跳来跳去没逻辑主线，面试官跟不上你的思路。
  4. **Market sizing（估算题，常嵌入）**：用结构化假设（人口 × 渗透率 × 单价 / 自上而下或自下而上）+ 心算估算市场规模，讲清每个假设。(evidence: [T03-S003, T06-S008])
     - *跳过后果*：上来乱拍数 / 不会拆结构 = 暴露估算能力缺失，market sizing 是 case 必考子题。
  5. **Recommendation（结论先行）**：最后用金字塔结构给一句话建议 + 2-3 个支撑理由 + 风险/next step；结论先行，不复述分析过程。(evidence: [T04-S001, T03-S003])
     - *跳过后果*：把分析过程从头复述一遍、结论埋最后 = so-what 没出来，「会分析不会综合」的印象。
  6. **Fit / PEI（行为面）**：与 case 权重相当 —— McKinsey PEI 对**单个 story 深挖 10-25 个追问**，考 Connection/Drive/Leadership/Growth；很多人栽在 PEI 而非 case。(evidence: [T03-S004, T06-S008])
     - *跳过后果*：只练 case 不准备 PEI，行为面被追问到细节露馅 = 一样 ding。
- **资深路径（差异点）**（这里「资深」= 备考充分/有咨询经验的候选人 vs 裸面新手）：
  - **skip — 老手跳过「死套框架」**：不机械套 Cosentino 的 Ivy Case System / 现成框架，而是**当场针对这道题 hypothesis-driven 地搭定制结构**（Victor Cheng 路线）。套框架的新手一眼被看穿「在背框架」；老手的结构是为这道题量身定的。(evidence: [T03-S002, T03-S003])
  - **optimize — 老手用 Day-1 假设 + 80/20 直接锁定关键分支**：搭完结构立刻说「我先看最可能的 X 分支」，不平均用力把每支都走一遍 —— 模拟真实咨询的 top-down。新手平均铺开、时间不够。(evidence: [T03-S002, T06-S009])
  - **add — 老手额外做「每一步主动 so-what + 阶段小结」**：每分析完一支主动说「所以这告诉我们……」并阶段性 synthesize，而非等到最后；展示综合能力。新手只报发现不提炼。(evidence: [T06-S009])
  - **add — 老手额外认真准备 PEI/fit**：把 2-3 个深度 story 打磨到能扛 10-25 个追问（STAR + 量化结果），不裸面。新手只磨 case。(evidence: [T03-S004])
- **近期变化**（近 12 个月）:
  - **AI 改变备考侧，但面试形式相对稳定**：候选人开始用 ChatGPT 做 mock case 陪练 / 生成练习题；但 firm 的现场 case interview（考结构化思维 + 沟通 + fit）形式没有被 GenAI 改写 —— 因为它考的正是「人怎么实时结构化思考与沟通」，恰是 AI 难替代的核心能力。(decay low；备考工具变，面试本体稳)
  - **行业入口收缩信号（ambient）**：GenAI 冲击初级分析师杠杆 + 部分 firm 缩招 → 案例面试竞争更激烈（社区信号，标 ambient，非确证数字）。(交叉 [T02-S003 GenAI-on-analyst])
  - **方法论本体 decay: low** —— MECE / hypothesis-driven / market sizing / 结论先行 是 40+ 年稳定考点。
- **典型耗时**:
  - 入门 SOP（单场面试）: 一个 case ~20-40 分钟 + PEI/fit 一段；一轮面试通常多个 case。
  - 备考周期: 新手系统备考 1-3 个月（练 30-50+ cases + PEI）；老手/有经验者更短。
- **关键工具（与 Track 02 / 05 关联）**:
  - caseinterview.com / LOMS（Victor Cheng，方法论事实标准）/ PrepLounge（同伴 mock）/ RocketBlocks（市场估算/图表分项练）/ Case in Point（入门 + market sizing 章）。(evidence: [T03-S003], 交叉 [T05-S017, T05-S019, T05-S020])
- **关键人物（与 Track 01 / 04 / 05 关联）**:
  - Victor Cheng（Case Interview Secrets / LOMS，hypothesis-driven 路线）[T03-S002, T03-S003]；Marc Cosentino（Case in Point，入门 + Ivy Case System，框架部分偏旧）[T04-S026]；Jenny Rae Le Roux（Management Consulted）[T05-S015]。
- **常见失败模式**:
  - **不澄清就开答**：理解错题目方向。避免：复述 + 问 2-3 个澄清问题再动手。**自检**：「我确认过目标、范围、成功标准了吗？」
  - **死套框架（frameworks-as-theater）**：机械套五力/3C 不管贴不贴题。避免：针对这道题 hypothesis-driven 搭定制结构。**自检**：「这个结构是为这道题搭的，还是我背的现成框架硬套？」
  - **结构不 MECE**：拆桶重叠/漏项。避免：拆完检查不重不漏。**自检**：「我这几个桶有重叠吗？合起来穷尽吗？」
  - **market sizing 乱拍数**：不拆结构、假设没逻辑。避免：人口 × 渗透率 × 单价式拆解，每个假设讲清理由。**自检**：「我每个估算假设，都说得出为什么取这个数吗？」
  - **不给 so-what / 结论埋最后**：复述分析、不提炼建议。避免：结论先行的 recommendation + 阶段小结。**自检**：「面试官只听我最后 30 秒，能拿到我的建议吗？」
  - **裸面 PEI**：只练 case 忽略行为面。避免：打磨 2-3 个能扛深挖的 story。**自检**：「我的 story 能扛住 15 个『然后呢/你具体做了什么』的追问吗？」(evidence: [T03-S004])
- **Last_updated**: 2026-06-09（方法论 anchored Cheng/Cosentino；备考工具 AI 化 anchored 2024-2025）
- **Decay risk**: **low**（case interview 形式 + 考点 40+ 年稳定；仅备考工具受 AI 改写，面试本体不变）

### 5. 客户 / 项目管理（SteerCo / stakeholder 对齐 / 周节奏）

- **One-liner**: 让 engagement「不翻车」的运作流 —— 经「定治理结构（SteerCo）→ 定节奏（周/双周对齐 + 阶段 readout）→ 管利益相关方与预期 → 中途纠偏」确保分析做对的同时**建议能被采纳、不踩客户政治雷**。这是 EM/partner 的核心活，区别于纯做分析。
- **Trigger**: engagement kickoff 之后、整个项目周期内持续运行（与 workflow 1 并行）。(evidence: [T03-S006, T06-S019])
- **Output**: 持续对齐的客户关系 + 定期 readout（阶段汇报）+ 没有 surprise 的最终汇报（结论已在过程中被 SteerCo 逐步「预热」认可）。(evidence: [T03-S006])
- **入门 SOP（minimum viable steps）**:
  1. **定治理结构**：明确客户侧 SteerCo（高管指导委员会）+ 关键 stakeholder（谁拍板、谁影响、谁配合数据）+ 客户项目对接人。(evidence: [T06-S019steerco, T03-S006])
     - *跳过后果*：不知道谁拍板/谁会反对，最后建议被某个没对齐过的高管一票否决。
  2. **定节奏（cadence）**：约定周/双周内部 + 客户对齐节奏 + 阶段性 readout 时点（项目活跃期常双周 SteerCo，团队内部更频）。(evidence: 通用项目治理实践 + [T03-S006])
     - *跳过后果*：闷头做几周才汇报，方向早就偏了却无人纠正，readout 当天大翻车。
  3. **每周/双周对齐 + readout**：定期向客户/SteerCo 汇报进展、初步发现、需要的决策/数据；逐步「预热」最终结论。(evidence: [T03-S006readout])
     - *跳过后果*：最终汇报抛出客户没有心理准备的结论 = surprise，高管抵触、不采纳（咨询忌讳「最后才 reveal」）。
  4. **管利益相关方与预期**：识别客户内部不同声音/政治，单独对齐关键反对者，确保建议落地路径上的人都被 buy-in。(evidence: [T06-S019stakeholder])
     - *跳过后果*：建议技术上对，但忽略客户内部政治，落地时被相关方消极抵制。
  5. **中途纠偏**：根据 readout 反馈 + SteerCo 指示调整 scope/方向/重点。(evidence: [T03-S006])
     - *跳过后果*：客户需求/优先级变了还按原计划走，交付的不是客户现在要的。
- **资深路径（差异点）**：
  - **add — 资深 EM/partner 额外做「无 surprise 原则」**：刻意在过程中通过 readout 把最终结论**逐步预先暴露**给关键决策者，让最终汇报变成「确认」而非「揭晓」。新人/junior 把汇报当一次性大 reveal，结果高管措手不及而抵触。(evidence: [T03-S006])
  - **optimize — 资深人把客户关系当「持续 BD」**：在交付当前项目时同步识别客户下一个痛点、积累信任，为续约/扩展埋线（finder 视角）。新人只盯当前 scope 把活干完。(evidence: [T06-S019leverage, T03-S006])
  - **add — 资深人额外读「客户政治地图」**：谁和谁不合、谁的 KPI 受这建议影响、谁是隐性反对者，据此调整沟通策略。新人只对接「对接人」一个声音，漏掉真正拍板/能搅黄的人。(evidence: [T06-S019])
- **近期变化**（近 12 个月）:
  - **远程/混合改写「周一到周四驻场」节奏（疫情后）**：传统「咨询师周一飞客户现场、周四飞回」的高强度驻场已部分被远程/混合取代 —— kickoff/关键 readout 仍倾向现场，但日常对齐转线上（Teams/Slack/Mural workshop）。触发：2020 疫情，已固化。(decay medium，结构性变化；交叉 [T02-S025 Mural workshop])
  - **运作层 decay: medium** —— SteerCo / readout / stakeholder 对齐的逻辑稳定，但「在哪做、用什么工具协作」被远程化改写。
- **典型耗时**: 与 engagement 同周期（6-12 周持续运行）；SteerCo 双周一次为常见节奏。
- **关键工具（与 Track 02 关联）**:
  - PowerPoint（readout deck）/ Teams·Slack·SharePoint（协作基建）/ Miro·Mural（远程 workshop / journey mapping / stakeholder 共创）/ Qualtrics（客户调研）。(evidence: [T02-S025], 交叉 [T02-S024])
- **关键人物（与 Track 01 / 05 关联）**:
  - McKinsey "Inside the Strategy Room" podcast（partner + 企业高管谈真实战略制定与客户协作）[T03-S006]；Bain「结果导向 + 与客户深绑」气质（NPS / CEO Sessions）[T05-S007]。
- **常见失败模式**:
  - **最终汇报才 reveal 结论（surprise）**：高管措手不及而抵触。避免：过程中 readout 逐步预热结论。**自检**：「最终 readout 上的核心结论，关键决策者之前听过/认可过吗？」
  - **没识别真正的拍板人/反对者**：只对接对接人。避免：早期画 stakeholder/政治地图。**自检**：「谁能一票否决这个建议？我对齐过 ta 吗？」
  - **scope creep（范围蔓延）**：客户不断加需求无边界。避免：SOW 划界 + 变更走正式流程。**自检**：「这个新需求在 SOW 里吗？不在就要么正式扩 scope 要么礼貌拒绝。」
  - **闷头做、不定期对齐**：方向偏了无人纠。避免：固定 cadence 的 readout。**自检**：「我上次跟客户对齐方向是几天前？超过一周就该同步了。」
- **Last_updated**: 2026-06-09（运作逻辑长期稳定；远程节奏 anchored 2020 疫情后固化）
- **Decay risk**: **medium**（治理/对齐逻辑稳定 = low，但驻场→远程节奏 + 协作工具被改写 = medium）

### 6. 商业尽调（commercial DD / CDD）

- **One-liner**: PE 投前的快节奏「这笔投资值不值」尽调 —— 经「定投资命题 → 市场吸引力 → 竞争位势 → 客户视角 → 增长可持续性 → 形成 go/no-go view」在极紧时间窗（常 2-6 周）验证标的商业计划是否站得住。是 workflow 1/2 的高压特化版，Bain/L.E.K./精品所的核心业务线。
- **Trigger**: PE/投资方在收购/投资某标的前，委托咨询所做商业层面尽调（验证 deal thesis）。(evidence: [T03-S012, T03-S013])
- **Output**: 一份 CDD 报告（deck）给出**投/不投 view** + 对标的商业计划假设的验证 + 关键风险 + 上行/下行情景；常含市场模型。(evidence: [T03-S012])
- **入门 SOP（minimum viable steps）**:
  1. **定投资命题 / deal thesis**：与 PE 客户对齐「这笔投资的核心赌注是什么」（市场会增长？标的能扩份额？协同？），把它拆成可验证的关键假设。(evidence: [T03-S012, T03-S013])
     - *跳过后果*：不知道投资方在赌什么，尽调发散、答非所问，PE 拿不到决策依据。
  2. **市场吸引力（market attractiveness）**：研究市场规模、增长率、结构性吸引力（常用五力 / 市场细分）。(evidence: [T03-S012])
     - *跳过后果*：标的再好但市场在萎缩/无吸引力 = 投资逻辑塌陷，漏掉这层是致命遗漏。
  3. **竞争位势（competitive position）**：标的 vs 竞品的份额、差异化、可防御性。(evidence: [T03-S012])
     - *跳过后果*：高估标的地位，没看到它在竞争中其实在失血。
  4. **客户视角（customer view）**：通过客户访谈/调研验证需求真实性、留存、转换风险（常重度用专家网络 + 客户 survey）。(evidence: [T03-S012], 交叉 [T02-S009])
     - *跳过后果*：只看二手数据、没听到真实客户声音，错判需求/留存（CDD 最有价值的恰是 primary customer view）。
  5. **增长可持续性（growth sustainability）**：验证标的商业计划里的增长假设现实吗、可持续吗。(evidence: [T03-S012])
     - *跳过后果*：照单全收标的自己画的增长曲线（卖方一面之词），PE 高价买进幻觉。
  6. **综合成 go/no-go view + 风险**：把各层综合成对投资命题的整体判断 + 关键风险 + 情景。(evidence: [T03-S012, T04-S041])
     - *跳过后果*：交一堆分析不给明确 view，PE 投委会无法据以拍板。
- **资深路径（差异点）**：
  - **skip — 资深人跳过「均匀铺开所有分析」**：在极紧时间窗内，直接锁定**最可能 kill deal 的 2-3 个假设**（deal-breaker hypotheses）优先验证，~80% 把握即给方向。新人想把市场/竞争/客户/财务每层都做全做深，时间根本不够。(evidence: [T03-S012, T06-S009])
  - **add — 资深人极早、极重地用专家网络**：CDD 时间窗内 48h 就约 5-10 个行业专家 call 建立 primary view，不等 secondary 数据慢慢来。新人偏赖公开数据库、错过 primary 洞见。(evidence: [T02-S009], 交叉 [T02-S012])
  - **add — 资深人额外守 MNPI 合规红线**：涉上市标的，专家 call 绝不套重大非公开信息（MNPI），否则触发内幕交易。这是 CDD/专家网络使用的硬红线，新人易踩。(evidence: [T02-S028])
  - **optimize — 资深人对「卖方故事」保持职业怀疑**：默认标的商业计划是 optimistic 的卖方叙事，刻意找证伪它的证据（confirmation-bias 反向应用）。新人容易被精美的 CIM/管理层故事带跑。(evidence: [T06-S009, T03-S012])
- **近期变化**（近 12 个月）:
  - **GenAI 加速 CDD 的 research / 综合子步**：用 AI 做市场 research 初稿、综合专家 call 转录、快速扫行业。但**幻觉核验闸门尤其关键** —— CDD 报告的数字直接影响数百万/数十亿投资决策，AI 编造的引用/数据进报告是已发生的真实事故（Deloitte 退款案）。(evidence: [T03-S009], 交叉 [T02-S003])
  - **专家网络形态变化**：transcript library 模式（Tegus/Third Bridge）+ AI 转录冲击纯 call 模式，CDD 的 primary research 获取方式在演化。(交叉 [T02-S011])
  - **流程本体 decay: low** —— 市场/竞争/客户/增长四层 + go/no-go 的 CDD 骨架稳定；仅研究子步被 AI 加速。
- **典型耗时**:
  - 入门 SOP: 一个 CDD 常 2-6 周（PE 交易时间窗压得很紧）。
  - 资深路径: deal-breaker-first + 极早专家 call 让关键 view 更快成形。
- **关键工具（与 Track 02 关联）**:
  - 专家网络 GLG·AlphaSights·Third Bridge（primary customer/行业 view，CDD 核心）/ 行业数据库 IBISWorld·PitchBook·Capital IQ（市场/交易/财务）/ Excel（市场模型）/ Qualtrics（客户调研）/ GenAI（research 加速，HIGH，需核验）。(evidence: [T02-S009, T02-S013, T02-S015, T02-S024])
- **关键人物 / 机构（与 Track 01 / 02 关联）**:
  - L.E.K. Consulting（CDD 专精精品所，一手流程口径）[T03-S012]；Oliver Wyman（buy-side 战略尽调）[T03-S013]；Bain「PE 关系深绑」气质 [T05-S006]。
- **常见失败模式**:
  - **照单全收卖方增长故事**：把标的自画的曲线当真。避免：默认怀疑，找证伪证据。**自检**：「这个增长假设，有没有独立于标的之外的证据支撑？」
  - **漏掉 primary customer view**：只看二手数据。避免：CDD 必做客户访谈/专家 call。**自检**：「我真的听到目标客户怎么说了吗，还是只看了报告？」
  - **踩 MNPI 合规红线**：专家 call 套上市公司内幕。避免：明确合规边界、不问不接受 MNPI。**自检**：「这个专家要说的，是公开可得的行业知识，还是某上市公司的内幕？后者立刻打住。」(evidence: [T02-S028])
  - **均匀铺开、时间窗内做不完**：不优先 deal-breaker。避免：先攻最可能 kill deal 的 2-3 个假设。**自检**：「如果只剩 3 天，哪个假设错了会让 PE 不投？先验证它。」
  - **AI 生成数据进 CDD 报告没核验**（decay HIGH）：幻觉数字影响投资决策。避免：每个 AI 数字/引用核验到源（Deloitte 殷鉴）。**自检**：「报告里这个关键数字，我对到原始来源了吗？」(evidence: [T03-S009])
- **Last_updated**: 2026-06-09（CDD 四层骨架长期稳定；AI 加速 + 专家网络形态变化 anchored 2024-2025）
- **Decay risk**: **low**（市场/竞争/客户/增长 + go/no-go 流程稳定；研究子步受 GenAI 加速但流程不变）

---

## Phase 2 提炼提示

### 反复出现 ≥3 个 workflow 都包含的步骤（候选 playbook 通则）

- **「先定义真问题（具体/有边界/可验证），区分表象 vs 根因」** 出现于 workflows 1 / 2 / 6（+ 4 的澄清步）→ **强候选 playbook**：「遇到模糊大问题 → 先花时间把它收敛成一句话可验证的问题陈述，再动手；问题定义错则全盘错」。这是跨所有 workflow 最一致的「第一步」。
- **「MECE 拆 issue tree / driver tree → 立 Day-1 可证伪假设 → 只做验证假设的最小分析」** 出现于 workflows 1 / 2 / 4 / 6 → **核心 playbook**：top-down 假设驱动 + 80/20 剪枝，避免 boil the ocean。
- **「结论先行（金字塔/SCQA）+ action title + so-what 自检」沟通** 出现于 workflows 1 / 3 / 4（recommendation）/ 5（readout）→ **核心 playbook**：任何输出都「一句话结论 + MECE 支撑」，所有 action title 连读 = exec summary。
- **「随时准备 kill 假设、主动找证伪证据（防 confirmation bias）」** 出现于 workflows 1 / 2 / 6 → **playbook + 反模式**：假设驱动的纪律面（双面讲，对照其滥用面）。
- **「GenAI 加速 research/综合/做 deck，但人是 last verifier（核验幻觉到源）」** 出现于 workflows 1 / 2 / 3 / 6 → **GenAI 时代新铁律 playbook**：跨 4 个 workflow 一致，是近 12 月最一致的新增步骤。
- **「专家网络做 primary research，但守 MNPI 合规红线」** 出现于 workflows 1 / 6 → playbook（research 分层 + 合规）。

### 入门 SOP 和资深路径之间最大的差距（候选 心智模型）—— 本 track 灵魂

跨 6 个 workflow 统计，**入门 vs 资深差异最锐利的两点**：

1. **【最锐利】「先射箭（Day-1 假设 + 80/20 top-down）vs 先穷举数据（bottom-up boil the ocean）」**：这是所有 workflow（1/2/4/6 全部）的共同分野，也是 intake 第一性张力（假设驱动 ⇄ 数据驱动）的直接投影。
   - 入门 SOP：倾向「把所有相关数据查全、每个分支分析到底，才敢有观点」→ 工时失控、抓不住重点。
   - 资深路径：Day-1 就基于经验立初步假设答案，用 80/20 锁定 2-3 个高杠杆分支，~80% 把握即收手（bias for speed over certainty），随时准备 kill 假设换靶。
   - → **候选心智模型**：「先有可证伪的答案当地图，再定向验证 —— 但地图随时准备重画；不要在错误方向上精雕细琢，也不要在没有假设时穷举大海」。**必须双面讲**（纪律 vs confirmation-bias 滥用，对照 intake warning #5 + Track 04/06 的反例）。

2. **【次锐利】「故事线先行（ghost deck / storyline 在分析前/早期就搭）vs 分析完才想怎么讲」**：workflows 1 / 3 / 5 共同体现。
   - 入门 SOP：先把分析做完，再坐下来想 deck 怎么组织 → 大量分析白做、关键论点缺数据、临交付狂返工。
   - 资深路径：项目极早期先写假想 storyline（action titles 串成的论证），让分析**反向服务故事线**；storyline 还被当「思考工具」倒查论证漏洞。
   - → **候选心智模型**：「先想清楚要讲什么故事（结论 + 论证链），再让分析去填它 —— deck 不是最后的包装，是从一开始就驱动工作的骨架」。

> 其余资深差异（add 类）反复出现：①管 client impact / 利益相关方政治（不只解智识问题）②无 surprise 原则（结论过程中预热）③GenAI 输出必核验。**差异类型分布**：6 个 workflow 共记录 ~24 处资深差异点，其中 skip ~6、optimize ~7、add ~11 —— **add 类最多**，说明本行资深性更多体现在「初学者忽略但资深人绝不跳的额外动作」（管政治、防偏误、核验、无 surprise），而非单纯少做几步。

### 近期工作流变化的根本原因（触发事件类型分布）

- **由新工具（GenAI）触发 = 绝对主导**：6 个 workflow 中 5 个（1/2/3/6 直接、4 的备考侧）的近期变化都源于 GenAI（McKinsey Lilli 2023-07 / BCG Deckster 2024-03 / ChatGPT Enterprise 全员铺开 2023-2024）。冲击集中在**初级分析师的 research / 综合 / 做 deck / market sizing**（杠杆模型底层）。
- **由行业事件触发**：远程/混合改写驻场节奏（2020 疫情后固化，影响 workflow 1/5）。
- **由市场/客户需求触发**：向 implementation / digital transformation 倾斜、两速交付（影响 workflow 1）。
- **主要驱动力 → Phase 2 识别的行业「外部驱动力」**：GenAI 对杠杆模型（leverage model）底层的结构性冲击，是本行当前第一外部驱动力，直接影响「初级分析师角色重构」「卖洞见 vs 卖工时」张力（intake (g) + Track 05 当前第一热点）。

### GenAI 对工作流的最大改写 + decay 强度（喂 Phase 2.8 诚实边界）

- **decay HIGH（12 月内大概率显著改写，强烈建议每 3 月跑 update）**：所有 workflow 中**「research / 综合 / 做 deck 初稿 / market sizing 辅助」这些子步**。具体：workflow 1 step 6/8、workflow 2 step 4-5、workflow 3 step 5/7、workflow 6 step 2-5 的研究环节。采用率（firm 自报）：Lilli 72% 员工 / Deckster 450K+ slide / ChatGPT Enterprise 全员（Bain/BCG/PwC）。**这是本 skill 工作流模块衰减最快的部分**。
- **decay medium**：engagement 整体节奏（远程化）、向落地倾斜、客户管理的协作工具层、专家网络形态（transcript library + AI 转录）。
- **decay low（master skill 最硬内核，5-10 年稳定）**：所有 workflow 的**方法论骨架** —— 问题定义 / MECE issue tree / hypothesis-driven / 结论先行（金字塔/SCQA）/ so-what / 80-20 / 案例面试考点 / CDD 四层。GenAI 改的是「执行有多快」，**没有改「怎么思考、怎么沟通」**。
- **关键判断喂 Phase 2.8**：本 skill 工作流节是「**稳定内核 + 高速外壳**」结构 —— 方法论内核可放心用 5+ 年，但「初级分析师每天具体怎么用工具干活」的外壳 6-12 月会大变。诚实边界应明写：「方法论（怎么想问题、怎么讲故事）decay low；但 GenAI 正在重写初级执行层，杠杆模型底层在结构性收缩，工具/角色细节请每 3 月校验」。

### 冷僻 / 信号薄弱自检

- **workflow 数 = 6 ✅**（≥4，floor 通过；核心 4 个全覆盖 + 客户管理 + CDD 两个可选）。
- **每个 workflow 有完整 12 字段卡 + last_updated ✅**。
- **入门 vs 资深分开 + ≥2 处资深差异**：6/6 workflow 都有 ≥2 处（多数 3-4 处）skip/optimize/add 差异 ✅（≥80% 达标）。
- **近期变化字段填充率**：6/6 都填了（5 个 GenAI 变化 + 远程节奏 + 落地倾斜；方法论本体明确标 decay low/稳态）✅（≥60% 达标）。
- **一手来源占比**：⚠️ **中等偏结构性 caveat**。verified_primary 锚定**方法论内核**（Minto/Cheng/McKinsey/HBR/L.E.K./Oliver Wyman + Wave 1 Rasiel/Bulletproof canon），但**「项目运作层」细节**（engagement-lifecycle 完整流程图、SteerCo 节奏、SOW 模板）firm 很少公开（属 know-how），只能靠 ex-MBB 从业者整理（Umbrex/StrategyU = secondary）+ 通用项目治理实践佐证。→ **方法论部分一手充足；运作部分一手偏薄、靠 ex-firm secondary 补**。已在 manifest「一手 vs 二手 caveat」如实标注。这是本行真实特征（流程 know-how 不公开），非调研失败。
- **decay risk 字段**：6/6 都标 ✅（整体 + GenAI 子步分别标注）。
- **总览表按 decay 分组 ✅**。
- **GenAI 子步 decay HIGH 全程标注 ✅**（intake warning h 核心要求）。

---

## 质量自检（提交前）

- [x] Workflow 数量 = 6（≥4，核心 4 个全覆盖）✅
- [x] 每个 workflow 完整 12 字段卡 + last_updated ✅
- [x] 入门 SOP 与资深路径分开；6/6 workflow ≥2 处资深差异（skip/optimize/add）✅
- [x] 近期变化字段 6/6 填了（GenAI / 远程 / 落地；方法论稳态明确标注）✅
- [x] 一手来源：方法论内核 verified_primary 充足；运作层一手偏薄已诚实标注 caveat ⚠️→标注合规
- [x] Decay risk 6/6 都标（整体 + GenAI 子步分别）✅
- [x] 总览表按 decay 分组 ✅
- [x] Phase 2 接口（共同步骤 6 条 / 入门-资深差距 2 条最锐利 / 变化触发分布 / GenAI decay 强度 / 冷僻信号）全填 ✅
- [x] Source Manifest 在最前，黑名单合规（无知乎/公众号/百度/CSDN/Quora/SEO 站/AI 摘要站/LinkedIn 帖；caseinterview/lek/oliverwyman 经 source_verifier 确认 verified_primary）✅
- [x] 每个 workflow 的关键 claim 挂 evidence；大量复用 Wave 1 [T04/T06] + Track 02 [T02] 跨轨 evidence ✅
- [x] 每个 workflow 失败模式 actionable（带 yes/no 自检问句，供 cli_writer 抽 workflow 自检环节）✅
