# Track 03 — Workflows / SOP / Pipeline（产品设计 / UX 设计）

> Phase 1 Wave 3 最后一轨。行业 = 产品设计 / UX 设计，locale=global，profile=practitioner。
> 本文件综合 Wave 1 (01-figures / 04-canon / 06-glossary) + Wave 2 (02-tools / 05-sources) 全部 seed，
> 把碎片拼成「入门 SOP + 资深路径 + 近期变化」的完整 workflow 卡片。

## Source Manifest

| source_id | url | bucket | last_checked | author/host | one-line note |
|-----------|-----|--------|--------------|-------------|---------------|
| T03-S001 | https://www.producttalk.org/opportunity-solution-trees/ | verified_primary | 2026-06-19 | Teresa Torres | OST + continuous discovery 周节奏一手（作者本人站） |
| T03-S002 | https://www.producttalk.org/2021/05/continuous-discovery-habits/ | verified_primary | 2026-06-19 | Teresa Torres | CDH 书页（与 T04-S010 同源） |
| T03-S003 | https://www.nngroup.com/articles/usability-testing-101/ | verified_primary | 2026-06-19 | NN/g | 可用性测试 101 标准步骤（Nielsen/Norman 自家组织一手） |
| T03-S004 | https://www.nngroup.com/articles/unmoderated-usability-testing/ | verified_primary | 2026-06-19 | NN/g | 无人值守测试 6 步流程 |
| T03-S005 | https://www.nngroup.com/articles/why-you-only-need-to-test-with-5-users/ | verified_primary | 2026-06-19 | Jakob Nielsen / NN/g | 「5 用户」经验法则原文（与 T04-S005 同源） |
| T03-S006 | https://www.nngroup.com/articles/journey-mapping-101/ | verified_primary | 2026-06-19 | NN/g | Journey map 制作步骤一手 |
| T03-S007 | https://www.designcouncil.org.uk/our-resources/the-double-diamond/ | verified_primary | 2026-06-19 | UK Design Council | Double Diamond 原创机构（与 T04-S023 同源） |
| T03-S008 | https://www.thesprintbook.com/ | verified_primary | 2026-06-19 | Jake Knapp et al | Sprint 官方书站（与 T04-S008/T01-S018 同源） |
| T03-S009 | https://www.designsprint.academy/blog/design-sprints-in-2025-the-questions-enterprise-teams-are-really-asking | verified_primary | 2026-06-19 | Design Sprint Academy | Sprint 2.0/3.0 + 远程 + AI 2025 现状 |
| T03-S010 | https://www.figma.com/blog/the-designers-handbook-for-developer-handoff/ | verified_primary | 2026-06-19 | Figma | 开发交付 handbook 一手（Dev Mode 流程） |
| T03-S011 | https://www.figma.com/best-practices/guide-to-developer-handoff/ | verified_primary | 2026-06-19 | Figma | Dev Mode handoff best practices |
| T03-S012 | https://atomicdesign.bradfrost.com/ | verified_primary | 2026-06-19 | Brad Frost | Atomic Design 全书在线（设计系统构建法） |
| T03-S013 | https://bradfrost.com/blog/post/the-design-system-ecosystem/ | verified_primary | 2026-06-19 | Brad Frost | 设计系统是「生态」非「组件库」一手论 |
| T03-S014 | https://dovetail.com/blog/dovetail-2025-spring-launch/ | verified_primary | 2026-06-19 | Dovetail | Magic insights/summaries AI 研究合成 2025 发布 |
| T03-S015 | https://www.w3.org/WAI/WCAG22/quickref/ | verified_primary | 2026-06-19 | W3C WAI | WCAG 2.2 quickref — a11y ground truth（与 T04-S015 同源） |
| T03-S016 | https://www.w3.org/WAI/test-evaluate/ | verified_primary | 2026-06-19 | W3C WAI | WAI 无障碍评估方法（自动扫描+人工审查） |
| T03-S017 | https://accessibility.ec.europa.eu/ | verified_primary | 2026-06-19 | European Commission | 欧盟无障碍法 EAA 官方门户（2025-06-28 deadline） |
| T03-S018 | https://www.figma.com/make/ | verified_primary | 2026-06-19 | Figma | Figma Make — prompt→可交互 UI 原生 vibe-coding（Config 2025） |
| T03-S019 | https://v0.dev | verified_primary | 2026-06-19 | Vercel | v0 — prompt→React+Tailwind 生成 UI（与 T02-S014 同源） |
| T03-S020 | https://config.figma.com/ | secondary | 2026-06-19 | Figma | Config 大会 — 工具/流程风向标（与 T05-S014 同源） |
| T03-S021 | https://www.svpg.com/articles/ | verified_primary | 2026-06-19 | Marty Cagan / SVPG | product discovery / empowered teams（与 T01-S007 同源） |
| T03-S022 | https://mule.design/ | verified_primary | 2026-06-19 | Erika Hall / Mule Design | Just Enough Research — 研究够用即可（与 T01-S012 同源） |
| T03-S023 | https://www.optimalworkshop.com | verified_primary | 2026-06-19 | Optimal Workshop | 卡片分类/树测试 vendor（IA 验证，与 T02-S007 同源） |
| T03-S024 | https://leanuxbook.com/ | verified_primary | 2026-06-19 | Jeff Gothelf & Josh Seiden | Lean UX — 假设驱动、轻交付（与 T04-S009 同源） |
| T03-S025 | https://www.maze.co | verified_primary | 2026-06-19 | Maze | Figma 原型上的远程测试主导（与 T02-S004 同源） |

> **一手说明**: NN/g (nngroup.com) 经 verifier 默认归 secondary，但 NN/g 是 Jakob Nielsen + Don Norman 自家组织、由其专家亲笔署名的一手 UX 研究流程，沿用 04-canon 同一约定归 `verified_primary`。
> **一手占比**: 25 source 中 verified_primary = 24（仅 T03-S020 config.figma.com 子域归 secondary）≈ 96%，达标（目标 ≥50%）。多为作者本人站 / vendor 一手 / 标准机构。

---

## 总览（按 decay risk 分组）

### High decay (12-month-class) — 3 个
| Workflow | Trigger | Output | Last_updated | 资深差异 |
|---------|---------|--------|-------------|---------|
| 4. AI 生成 → 设计师精炼 UI（prompt-to-UI） | 要快速出可点 UI / 探索方向 | 可交互高保真 / 可用代码骨架 | 2026-06 | optimize+add（用 AI 起草，人做品味与系统对齐） |
| 5. handoff / 设计→开发交付 | 设计 ready 进开发 | Dev Mode 规格 + token + 代码映射 | 2026-06 | skip+optimize（持续连接取代「扔过墙」） |
| 1. 用户研究 → 洞察（含 AI 合成） | 不知道用户卡在哪 / 要验证假设 | persona / journey / 带证据的洞察 | 2026-06 | skip+optimize+add（AI 合成 + 够用研究） |

### Medium decay — 2 个
| Workflow | Trigger | Output | Last_updated | 资深差异 |
|---------|---------|--------|-------------|---------|
| 2. Design Sprint（5 天冲刺） | 高风险大赌注要快速验证 | 真人测过的高保真原型 + go/no-go | 2026-06 | skip+optimize（2.0/3.0、远程、AI 提速） |
| 6. Continuous Discovery（持续探索） | 团队想从瀑布研究转持续 | OST + 每周访谈节奏 + 实验 | 2026-06 | optimize+add（每周节奏取代项目制研究） |

### Low decay — 2 个
| Workflow | Trigger | Output | Last_updated | 资深差异 |
|---------|---------|--------|-------------|---------|
| 3. 可用性测试（usability testing） | 原型/上线品要验真实可用 | 问题清单 + 严重度 + 修复建议 | 2026-06 | skip+optimize（折扣可用性、5 用户） |
| 7. 设计系统搭建（design system） | 多产品/多人不一致、复用低 | token + 组件库 + 文档 + 治理 | 2026-06 | optimize+add（生态/治理 > 组件库本身） |
| 8. 无障碍合规（accessibility / WCAG） | 法规要求 / 包容性目标 | WCAG 2.2 AA 符合 + 审计报告 | 2026-06 | add（设计阶段内建，非事后补救） |

> 注：低 decay 列含 3 个（可用性测试、设计系统、无障碍）。合计 **8 个独立 workflow**。

---

### 1. 用户研究 → 洞察（user research to insight，含 AI 合成）

- **One-liner**: 从「不知道用户为什么这么做 / 要不要做某功能」到「有证据支撑的、可指导设计决策的洞察（persona / journey map / 痛点优先级）」。
- **Trigger**: 进入新问题域、要验证一个产品假设、利益相关者拍脑袋下需求、或上线后指标异常需归因。 (evidence: [T03-S021, T03-S022])
- **Output**: 研究报告 / 洞察卡 + persona + journey map / 服务蓝图 + 优先级化的痛点&机会清单，存入研究库（research repository）可被团队复用。 (evidence: [T03-S006, T03-S014])
- **入门 SOP（minimum viable steps）**:
  1. **定研究问题 + 选方法**: 先写「我们想知道什么」「这个决定取决于什么」，再选定性（访谈/可用性观察）还是定量（问卷/分析）。跳过→做了一堆访谈却答不了真正的决策问题，研究变摆设。 (evidence: [T03-S022])
  2. **招募 + 筛选**: 用 screener 找到目标用户群（5-8 人/段足够定性覆盖）。跳过→招到非目标用户，洞察偏差，结论不可信。 (evidence: [T03-S003, T03-S005])
  3. **执行（访谈 / 观察 / 测试）**: 问行为不问意见（"上次你怎么做的"而非"你喜欢吗"），录音/录屏。跳过→拿到的是自陈偏好（stated）而非真实行为（revealed），违背行业第一性。 (evidence: [T03-S022])
  4. **合成（synthesis）**: 转录 → 高亮关键句 → 按主题打标（affinity / 主题分析）→ 提炼 pattern。跳过→一堆原始素材没变成可行动洞察，等于没研究。 (evidence: [T03-S014])
  5. **可视化 + 交付**: 产出 persona / journey map / 洞察报告，标优先级，讲给团队。跳过→洞察停在研究员脑里，不影响产品决策。 (evidence: [T03-S006])
- **资深路径（差异点）**：
  - **skip**: 资深人对成熟问题域**跳过**正式 persona / 大样本 — Erika Hall「Just Enough Research」：研究是为决策服务，匹配风险即可，不为做而做。低风险决策直接靠已有研究库 + 一两个快速访谈。 (evidence: [T03-S022])
  - **optimize**: 资深人把 step 4 合成用 **AI 工具（Dovetail Magic insights/summaries）**做首轮主题提取，自己只做校验与升华；transcribe 全自动。把原本数天的合成压到数小时。 (evidence: [T03-S014])
  - **add**: 资深人**额外建/维护研究库（research repository）**，让每次研究可被检索复用、避免重复研究；并在交付时绑定到产品决策（而非交一份 PDF）。 (evidence: [T03-S014, T03-S021])
- **近期变化**（近 12 个月）:
  - 2024–2025 起，由 **AI 合成成熟**（Dovetail Magic、Notably 等）触发，原 step 4「人工逐条转录+打标」变为「AI 首轮合成 + 人校验」，研究员角色从「打标工」上移到「提问与判断」。触发事件类型: 新工具。 (evidence: [T03-S014])
  - 采用率: AI-assisted 访谈分析在 2024-2025 已从 gimmick 变 genuine leverage（业界普遍观察，无精确百分比）。 (evidence: [T03-S014])
- **典型耗时**: 入门 SOP 1-2 周（招募是瓶颈）；资深路径 2-4 天（AI 合成 + 复用库）。
- **关键工具**: Dovetail（研究库+AI 合成，必备）、Maze / UserTesting（执行）、Optimal Workshop（IA 研究）、Hotjar/Clarity（行为数据）。 (evidence: [T03-S014, T03-S025, T03-S023])
- **关键人物**: Erika Hall《Just Enough Research》(T01-S012)、Teresa Torres、Marty Cagan(discovery)、NN/g 研究团队。 (evidence: [T03-S022, T03-S021])
- **常见失败模式**:
  - 问意见而非行为: 访谈里问"你喜不喜欢 X"得到的是礼貌假象。改为问"上一次遇到 Y 你做了什么"。 (evidence: [T03-S022])
  - 研究做了不落地: 交完报告团队照旧拍脑袋。把每条洞察绑定到一个具体待决策问题再交付。 (evidence: [T03-S021])
  - 过度研究: 低风险决策做大样本研究，拖慢交付。先评估「这个决定错了代价多大」再决定研究深度。 (evidence: [T03-S022])
- **来源**: [Primary] T03-S022 (mule.design / Just Enough Research, 2026-06-19); [Primary] T03-S014 (Dovetail 2025 launch, 2026-06-19); [Primary] T03-S006 (NN/g journey mapping 101, 2026-06-19); [Reference] T03-S021 (SVPG discovery).
- **Last_updated**: 2026-06-19
- **Decay risk**: high（AI 合成工具迭代快，合成步骤 12 月内会再变）

---

### 2. Design Sprint（5 天冲刺）

- **One-liner**: 从「有个高风险大赌注，不确定值不值得建」到「5 天内得到真人测过的高保真原型 + go/no-go 决策」，跳过数月辩论。
- **Trigger**: 重大方向决策、新产品/新功能下注大、团队卡在无休止讨论里、或需要快速对齐跨职能利益相关者。 (evidence: [T03-S008])
- **Output**: 可点高保真原型 + 5 名真实用户测试结果 + 明确的下一步决定（build / pivot / kill）。 (evidence: [T03-S008])
- **入门 SOP（minimum viable steps，Knapp 经典 5 天）**:
  1. **周一 Map（理解+定目标）**: 画长期目标、流程地图、采访专家、选一个 sprint 靶点。跳过→后面四天没有共同焦点，原型散乱。 (evidence: [T03-S008])
  2. **周二 Sketch（构思）**: 找灵感（lightning demos）+ 每人独立画方案（crazy 8s / solution sketch）。跳过→只剩 HiPPO 的点子，丧失方案多样性。 (evidence: [T03-S008])
  3. **周三 Decide（决策）**: 投票（dot voting）+ Decider 拍板 + 画 storyboard。跳过→无收敛，周四不知道原型造什么。 (evidence: [T03-S008])
  4. **周四 Prototype（造原型）**: 用 Figma 等做「门面（facade）」级高保真假象，只做被测路径。跳过→周五没东西可测。 (evidence: [T03-S008])
  5. **周五 Test（测试）**: 1:1 访谈式测 5 个目标用户，团队观看，归纳模式得结论。跳过→等于又做了一个没验证的方案。 (evidence: [T03-S008, T03-S005])
- **资深路径（差异点）**：
  - **skip**: 资深引导师用 **Sprint 2.0（AJ&Smart，4 天）**，砍掉周一部分专家访谈、利益相关者仅按需进场；甚至 1-2 天 mini-sprint 解决聚焦问题。 (evidence: [T03-S009])
  - **optimize**: 资深人用 **AI 提速**：AI 生成访谈脚本、storyboard、用 Uizard/Figma Make 加速周四原型；远程 sprint 拆成 2-3 小时短块跨 2 周，配 Miro/FigJam。但 AI 只当「研究助理」不当「决策者」。 (evidence: [T03-S009, T03-S018])
  - **add**: 资深人加 **Sprint 3.0 的「问题框定（Problem Framing）」前置环节**，确保赌注本身值得 sprint，避免高效解决错的问题。 (evidence: [T03-S009])
- **近期变化**（近 12 个月）:
  - 远程/混合常态化 → 经典「同屋 5 天」拆成跨 2 周的短块（2-3h）；2025 起 AI（ChatGPT/Uizard/Figma Make）进入构思与原型环节加速但不替代决策。触发事件类型: 行业事件（远程）+ 新工具（AI）。 (evidence: [T03-S009, T03-S018])
- **典型耗时**: 入门 SOP 5 个工作日（全员）；资深路径 4 天（2.0）或拆块 2 周（远程）。
- **关键工具**: Figma/FigJam、Miro（远程白板）、Maze（远程测试）、Uizard/Figma Make（AI 原型）。 (evidence: [T03-S009, T03-S025, T03-S018])
- **关键人物**: Jake Knapp《Sprint》(T01-S018)；AJ&Smart（2.0/3.0 推广者）。 (evidence: [T03-S008, T03-S009])
- **常见失败模式**:
  - 对低风险问题用 sprint: 杀鸡用牛刀，浪费全团队一周。先问「这值得 5 个人停一周吗」。 (evidence: [T03-S009])
  - 原型做太真: 想做完整产品级原型，周四做不完。只做被测路径的「门面」，其余假装。 (evidence: [T03-S008])
  - 跳过周五测试: 时间紧就砍测试 — 那 sprint 就退化成普通 workshop，验证为 0。测试是不可跳的核心。 (evidence: [T03-S008])
- **来源**: [Primary] T03-S008 (thesprintbook.com, 2026-06-19); [Primary] T03-S009 (Design Sprint Academy 2025, 2026-06-19); [Reference] T03-S018 (Figma Make).
- **Last_updated**: 2026-06-19
- **Decay risk**: medium（核心 5 天框架稳态，但 AI/远程优化路径 12-24 月持续演化）

---

### 3. 可用性测试（usability testing）

- **One-liner**: 从「我们以为这个设计好用」到「看真人真实使用，发现他们实际卡在哪」，把意见之争变成观察证据。
- **Trigger**: 有线框/原型/已上线产品要验证可用性；指标显示某流程转化低；上线前的最后把关。 (evidence: [T03-S003])
- **Output**: 按严重度排序的可用性问题清单 + 修复建议 + （定量时）SUS/任务完成率/出错率。 (evidence: [T03-S003])
- **入门 SOP（minimum viable steps）**:
  1. **定目标 + 写任务**: 明确测什么流程，写真实场景的任务（"给朋友买张生日礼券"而非"用搜索功能"）。跳过→测了无关紧要的东西，或任务诱导了答案。 (evidence: [T03-S003, T03-S004])
  2. **选方法**: 有主持（moderated，能追问，适合早期探索）vs 无主持（unmoderated，快、量大，适合验证）。跳过→方法错配研究目标，浪费。 (evidence: [T03-S003, T03-S004])
  3. **招募 ~5 名/段目标用户**: Nielsen「5 用户能发现约 85% 问题」经验法则。跳过→样本太少漏问题，或太多边际收益递减浪费钱。 (evidence: [T03-S005])
  4. **pilot（试跑 1 人）**: 先跑一个，校验任务清晰度和工具。跳过→正式测试才发现任务有歧义，全部数据作废。 (evidence: [T03-S004])
  5. **执行 + 观察**: 让用户出声思考（think-aloud），主持人少干预，记录卡点。跳过→只看结果不看过程，不知道"为什么"卡。 (evidence: [T03-S003])
  6. **分析 + 报告**: 按严重度归纳问题，给可行动修复建议。跳过→发现问题但不修，测试白做。 (evidence: [T03-S004])
- **资深路径（差异点）**：
  - **skip**: 资深人对小改动**跳过正式招募+大流程**，做 Krug 式「折扣可用性 / 走廊测试」— 抓 3 个大致符合的人，一上午测完当天讨论。 (evidence: [T03-S005])
  - **optimize**: 资深人用 **Maze/UserTesting 无主持远程**，几小时内收几十上百份；用工具自动算任务完成率/热点，自己只读异常。 (evidence: [T03-S004, T03-S025])
  - **optimize**: 资深主持人**问得更少**，忍住不提示，让真实卡点暴露；新手容易"救场"污染数据。 (evidence: [T03-S003])
- **近期变化**（近 12 个月）: **无重大变化（行业稳态）**。可用性测试方法学自 Nielsen 1990s「折扣可用性」+ 2000「5 用户」起 20+ 年稳定，最近一次显著变化是远程无主持工具（Maze/UserTesting）让执行更快，但流程逻辑不变。触发事件类型: 工具（非方法）。 (evidence: [T03-S003, T03-S005])
- **典型耗时**: 入门 SOP 1-2 周（招募慢）；资深路径 1-3 天（折扣测试当天 / 无主持几小时）。
- **关键工具**: Maze、UserTesting、Lookback（主持远程）、Optimal Workshop（IA 测试）。 (evidence: [T03-S025, T03-S023])
- **关键人物**: Jakob Nielsen（5 用户/折扣可用性）、Steve Krug《Rocket Surgery Made Easy》、NN/g。 (evidence: [T03-S005, T03-S003])
- **常见失败模式**:
  - 主持人引导用户: "你想点哪个？是不是这里？"污染数据。坐后面闭嘴，让用户自己撞墙。 (evidence: [T03-S003])
  - 把测试当作品 demo: 向用户推销设计而非观察其使用。 (evidence: [T03-S003])
  - 拿喜好当可用性: 问"好看吗"而非看"能不能完成任务"。可用性测能力，不是测审美偏好。 (evidence: [T03-S003])
- **来源**: [Primary] T03-S003 (NN/g usability 101, 2026-06-19); [Primary] T03-S004 (NN/g unmoderated, 2026-06-19); [Primary] T03-S005 (NN/g 5 users, 2026-06-19).
- **Last_updated**: 2026-06-19
- **Decay risk**: low（方法学稳态 20+ 年）

---

### 4. AI 生成 → 设计师精炼 UI（prompt-to-UI）

- **One-liner**: 从「一句话需求 / 草图」到「可点的高保真 UI（或可用前端代码骨架）」，用 AI 起草、设计师做品味与系统对齐的精炼。
- **Trigger**: 要快速出多个方向探索、做 demo、给工程一个起点、或一个人要同时担设计+前端（design engineer）。 (evidence: [T03-S018, T03-S019])
- **Output**: 可交互高保真原型（Figma frames，带 auto-layout/组件）或 React+Tailwind 代码骨架。 (evidence: [T03-S018, T03-S019])
- **入门 SOP（minimum viable steps）**:
  1. **写 prompt（描述意图）**: 描述屏幕、内容、状态、风格约束。跳过/写糊→生成出通用 AI 味、不贴需求的界面。 (evidence: [T03-S018])
  2. **生成（Figma Make / v0）**: AI 出可交互 UI / 代码；Figma Make 在画布上原生生成可编辑 frame，v0 出 React+Tailwind。跳过→回到从零手画，慢。 (evidence: [T03-S018, T03-S019])
  3. **筛选方向**: 从多个生成结果挑一个可用骨架。跳过→在烂骨架上死磕，不如重 prompt。 (evidence: [T03-S018])
  4. **导入 + 精炼（设计师 craft）**: 接进 Figma，套设计系统 token、调字体/间距/网格、规范组件复用。跳过→AI 草稿停在「能看不能用」，不一致、不可维护。 (evidence: [T03-S018])
  5. **验证 + 交付**: 走可用性/系统一致性检查后交付。跳过→把 AI 幻觉的交互/无障碍坑直接带进产品。 (evidence: [T03-S015])
- **资深路径（差异点）**：
  - **optimize**: 资深人把 **AI 当「riff 伙伴」做发散**（ChatGPT→v0→Figma 链路快速试 N 个方向），自己专注收敛与品味判断；prompt engineering 成为核心技能。 (evidence: [T03-S019, T03-S018])
  - **add**: 资深人**强制让生成结果对齐已有设计系统 token**（而非接受 AI 自造一套），并人工补无障碍（对比度/语义/键盘）— AI 默认不保证 WCAG。 (evidence: [T03-S015, T03-S018])
  - **skip（新手别学）**: 资深人**不**把 AI 输出当成品直接 ship；新手最大坑是省掉 step 4 精炼。
- **近期变化**（近 12 个月）:
  - 2025-05 Config 起，**Figma Make 作为原生 vibe-coding 进入画布**（无需插件 prompt→可交互 UI）；v0 持续迭代 prompt→code。整条「先画线框再做高保真」的瀑布在探索阶段被「先生成再精炼」取代。触发事件类型: 新工具/新模型。 (evidence: [T03-S018, T03-S020])
  - 2026 起出现 design↔code 双向连接（如 MCP 连 Figma 与代码生成工具），进一步模糊设计与实现边界。触发事件类型: 新工具。 (evidence: [T03-S010])
  - 采用率: 仍在早期高速采用，质量参差，业界共识是「AI 起草 + 人精炼」而非全自动。 (evidence: [T03-S018])
- **典型耗时**: 入门 SOP 数小时（生成）+ 数小时到 1 天（精炼）；资深路径分钟级探索多方向 + 半天精炼。
- **关键工具**: Figma Make（原生）、v0 by Vercel、Uizard、Cursor（design engineer），Locofy/Anima（Figma→code）。 (evidence: [T03-S018, T03-S019])
- **关键人物**: Figma（Config 发布者）；design engineer 兴起的从业群体；Luke Wroblewski（AI 产品）。 (evidence: [T03-S020])
- **常见失败模式**:
  - 把 AI 草稿当成品 ship: 生成的界面有通用 AI 味、不一致、无障碍坑。**用 AI 起草，但留出半天做 token 对齐 + 无障碍 + craft 精炼，否则技术债转移到工程。** (evidence: [T03-S018, T03-S015])
  - AI 自造一套设计语言: 生成结果不复用现有 token/组件，破坏一致性。**生成后第一步就映射到现有设计系统，别让 AI 平行造轮子。** (evidence: [T03-S013, T03-S018])
  - prompt 太糊: 没给状态/约束/内容，得到占位 lorem 界面。**prompt 写明真实内容、空/错/加载态与品牌约束。** (evidence: [T03-S018])
- **来源**: [Primary] T03-S018 (Figma Make, 2026-06-19); [Primary] T03-S019 (v0.dev, 2026-06-19); [Reference] T03-S020 (Config 2025).
- **Last_updated**: 2026-06-19
- **Decay risk**: high（AI 工具 6-12 月内大改，本卡最易过时）

---

### 5. handoff / 设计 → 开发交付

- **One-liner**: 从「设计在 Figma 里 ready」到「工程拿到精确规格（尺寸/token/状态/交互）并实现得一致」，让「设计的」与「建出来的」尽量重合。
- **Trigger**: 设计稿评审通过准备进开发；或工程在实现中需要规格澄清。 (evidence: [T03-S010])
- **Output**: Dev Mode 标注 + 测量 + design token / 变量 + 代码片段映射 + 状态&边界条件说明 + 与工单（Jira 等）关联。 (evidence: [T03-S010, T03-S011])
- **入门 SOP（minimum viable steps）**:
  1. **整理设计文件**: 命名规范、用 auto-layout、组件化、把变量/token 接好，标 ready-for-dev。跳过→工程看不懂哪版是终稿，靠猜，返工。 (evidence: [T03-S011])
  2. **标注规格 + 边界状态**: 在 Dev Mode 标注交互、空/错/加载态、响应式断点、可访问性要求。跳过→工程只实现 happy path，边界态各写各的。 (evidence: [T03-S010])
  3. **绑定 token / 变量**: 让间距/颜色/字号引用变量而非硬编码值，工程映射到代码 token。跳过→工程手抄魔法数字，设计系统失效。 (evidence: [T03-S011, T03-S013])
  4. **交付会 + 关联工单**: 与工程过一遍，把设计关联到 Jira 等工单。跳过→「扔过墙」，问题攒到上线前爆发。 (evidence: [T03-S010])
  5. **实现后 QA（design review）**: 设计师对照检查实现一致性。跳过→产品上线与设计有可见偏差，体验打折。 (evidence: [T03-S010])
- **资深路径（差异点）**：
  - **skip**: 资深团队**跳过「一次性大交付会」**，改为**持续协作**：设计与工程从早期就同步，handoff 退化为「确认」而非「移交」。 (evidence: [T03-S010])
  - **optimize**: 资深人用 **Dev Mode + 变量/token + 工单集成**让规格自动可读，少写人肉 redline 文档；并维护「设计↔代码」同一 token 真值源。 (evidence: [T03-S011, T03-S013])
  - **add**: 资深 design engineer **自己写部分前端**，handoff 边界进一步消失（「the great design handoff」论的极端）。 (evidence: [T03-S010])
- **近期变化**（近 12 个月）:
  - 2024 起 Figma **Dev Mode 出 beta**（标注/测量/代码连接），2025-2026 design↔code 双向连接兴起（MCP 连 Figma 与代码生成），handoff 从「离散事件」转向「持续连接」，设计系统初始搭建从资深设计师 2-4 周缩到 1 天有可信起点。触发事件类型: 新工具。 (evidence: [T03-S010, T03-S011])
  - 采用率: Dev Mode 已成 Figma 团队默认交付方式；design engineer 角色快速增长。 (evidence: [T03-S011])
- **典型耗时**: 入门 SOP 1-2 天准备 + 交付会；资深路径近实时（持续协作，无独立 handoff 阶段）。
- **关键工具**: Figma Dev Mode（必备）、Tokens Studio / Supernova（token 自动化）、Storybook（组件对齐）、Zeplin/蓝湖(zh-CN)。 (evidence: [T03-S010, T03-S013])
- **关键人物**: Figma（Dev Mode）；Brad Frost（token/设计系统对齐）；design engineer 群体。 (evidence: [T03-S011, T03-S013])
- **常见失败模式**:
  - 「扔过墙」式交付: 设计完丢链接给工程就不管。**从早期就拉工程进设计评审，把 handoff 变成确认而非移交。** (evidence: [T03-S010])
  - 硬编码值不用 token: 工程手抄间距/颜色数字，下次改 token 全乱。**设计端先把变量/token 接好，让工程映射而非手抄。** (evidence: [T03-S013, T03-S011])
  - 没标边界状态: 只给 happy path，空/错/加载态工程乱猜。**交付前补齐空/错/加载/响应式四类状态。** (evidence: [T03-S010])
- **来源**: [Primary] T03-S010 (Figma handoff handbook, 2026-06-19); [Primary] T03-S011 (Figma Dev Mode best practices, 2026-06-19); [Reference] T03-S013 (Brad Frost ecosystem).
- **Last_updated**: 2026-06-19
- **Decay risk**: high（Dev Mode / design↔code 连接 / design engineer 角色 12 月内仍快速演化）

---

### 6. Continuous Discovery（持续探索）

- **One-liner**: 从「项目制、瀑布式的一次性研究」到「团队每周与客户接触的持续节奏」，让产品决策始终绑在最新证据上。
- **Trigger**: 团队想摆脱「研究→交付→几个月不碰用户」的瀑布；想让 PM+设计+工程「product trio」共同拥有 discovery。 (evidence: [T03-S001, T03-S002])
- **Output**: 持续更新的机会解决方案树（Opportunity Solution Tree, OST）+ 每周访谈节奏 + 小型快速实验 + 证据驱动的优先级。 (evidence: [T03-S001])
- **入门 SOP（minimum viable steps）**:
  1. **定 desired outcome（业务结果）**: 锁定一个可度量的产品结果作为 OST 根。跳过→discovery 漫无目的，访谈拿一堆无关洞察。 (evidence: [T03-S001])
  2. **建 OST**: 把 outcome → 机会（用户需求/痛点）→ 解决方案 → 实验，可视化连接。跳过→隐含假设不外显，团队各想各的。 (evidence: [T03-S001])
  3. **每周访谈节奏**: 每周固定与 1+ 客户做小型接触（不是攒到季度做大研究）。跳过→证据陈旧，回到拍脑袋。 (evidence: [T03-S002])
  4. **嵌入式合成**: 几次访谈后就更新 OST，让树始终基于证据而非愿望。跳过→OST 变成一次性海报，与现实脱节。 (evidence: [T03-S001])
  5. **小实验验证假设**: 拆小机会→小方案→快实验。跳过→直接造大功能，赌注大、反馈慢。 (evidence: [T03-S001, T03-S024])
- **资深路径（差异点）**：
  - **optimize**: 资深 trio 把访谈招募**自动化**（产品内拦截/持续招募池），消除「每周找人」的摩擦，让节奏可持续。 (evidence: [T03-S002])
  - **add**: 资深人**额外做 assumption mapping**（区分 desirability/viability/feasibility/usability 假设），优先测最危险假设而非随机实验。 (evidence: [T03-S021, T03-S024])
  - **add**: 资深人用 **AI 辅助 discovery**（Torres 2025 谈 AI product discovery）做合成与机会归纳，但坚持每周真人接触不可替代。 (evidence: [T03-S001])
- **近期变化**（近 12 个月）:
  - 2024-2025 持续推进「continuous discovery 取代项目制瀑布研究」成为现代产品团队默认范式；Torres 2025 起公开谈 AI 如何嵌入 discovery（合成/机会归纳），但强调每周真人节奏不变。触发事件类型: 方法论扩散 + 新工具（AI）。 (evidence: [T03-S001, T03-S002])
- **典型耗时**: 不是一次性项目，是**持续每周节奏**；建首个 OST 约 1-2 天，之后每周数小时滚动。
- **关键工具**: Dovetail（研究库+合成）、Maze（快实验）、FigJam/Miro（OST 可视化）、产品内拦截招募。 (evidence: [T03-S014, T03-S025])
- **关键人物**: Teresa Torres《Continuous Discovery Habits》(T01-S009/T04-S010)；Marty Cagan（product discovery / empowered teams）；Jeff Gothelf（Lean UX 假设驱动）。 (evidence: [T03-S001, T03-S021, T03-S024])
- **常见失败模式**:
  - OST 当一次性海报: 画完挂墙不更新。**规定每几次访谈就更新 OST，否则它与现实脱节。** (evidence: [T03-S001])
  - 没有真人每周节奏: 退回季度大研究。**把每周客户接触排进日历当固定仪式，没素材也要触达。** (evidence: [T03-S002])
  - 直接跳到大方案: 跳过机会拆解直接造大功能。**先把大机会拆成可快速测的小机会再做。** (evidence: [T03-S001])
- **来源**: [Primary] T03-S001 (producttalk OST, 2026-06-19); [Primary] T03-S002 (producttalk CDH, 2026-06-19); [Reference] T03-S021 (SVPG); [Reference] T03-S024 (Lean UX).
- **Last_updated**: 2026-06-19
- **Decay risk**: medium（框架稳态，AI 嵌入路径 12-24 月演化）

---

### 7. 设计系统搭建（design system）

- **One-liner**: 从「多产品/多人界面不一致、组件不复用、改一处要改十处」到「一套 token + 组件库 + 文档 + 治理流程」，让一致性可规模化。
- **Trigger**: 团队/产品线扩张导致 UI 漂移、设计与工程对不齐、新功能重复造轮子、品牌改版要全局生效。 (evidence: [T03-S013])
- **Output**: design token（变量层）+ 组件库（Figma + 代码 Storybook）+ 使用文档（zeroheight 等）+ 贡献/治理流程。 (evidence: [T03-S012, T03-S013])
- **入门 SOP（minimum viable steps）**:
  1. **接口审计 / 库存（interface inventory）**: 截图现有所有 UI 元素，找出有多少种按钮/输入框等，暴露不一致。跳过→在没摸清现状的地基上盖系统，漏掉真实用例。 (evidence: [T03-S012])
  2. **定 token（subatomic）**: 抽颜色/间距/字号/圆角等为变量，作单一真值源。跳过→组件硬编码值，无法全局换肤/改版。 (evidence: [T03-S012, T03-S013])
  3. **按原子层级建组件（atomic）**: atoms→molecules→organisms→templates→pages，从小到大组合。跳过→直接做大组件，复用性差、难维护。 (evidence: [T03-S012])
  4. **写文档 + 用法规范**: 每个组件给「何时用/不用/可访问性」。跳过→有库无文档，团队各用各的，系统形同虚设。 (evidence: [T03-S013])
  5. **建治理 + 贡献流程（生态）**: 谁维护、怎么提需求、怎么版本化、设计↔代码怎么同步。跳过→系统上线即腐烂，分叉成多套。 (evidence: [T03-S013])
- **资深路径（差异点）**：
  - **optimize**: 资深人**从一个能用的简单系统起步再演化**（Frost：复杂系统必由可用的简单系统演化而来），不一次造大而全。 (evidence: [T03-S013])
  - **add**: 资深人把重心放在 **step 5 治理/人际/流程（"design system ecosystem"）** 而非组件本身 — 组件库存在 ≠ 成功，编排人/流程/技术才是。 (evidence: [T03-S013])
  - **add**: 资深人**自动化 design↔code token 同步**（Tokens Studio / Supernova），让设计变量与代码 token 单一真值源。 (evidence: [T03-S013])
- **近期变化**（近 12 个月）: 多为稳态（atomic design 自 2013、token 自 2016+ 已成熟）。近期增量：**AI 与设计系统结合**（Frost 等 2025 课程/talk）加速 token 生成与组件文档；design↔code 双向连接让初始搭建从 2-4 周缩到 1 天起点。触发事件类型: 新工具（AI / Dev Mode）。 (evidence: [T03-S013, T03-S010])
- **典型耗时**: 入门 SOP 数周到数月（取决于产品规模）；资深路径：先 1 周小可用系统 + 持续演化（治理是长期的）。
- **关键工具**: Figma 变量、Tokens Studio、Supernova、Storybook（代码组件）、zeroheight（文档）。 (evidence: [T03-S013, T03-S012])
- **关键人物**: Brad Frost《Atomic Design》(T01-S013)；Nathan Curtis（token）；Alla Kholmatova。 (evidence: [T03-S012, T03-S013])
- **常见失败模式**:
  - 当成「组件库」而非「生态」: 只建库不建治理/流程，系统上线即腐烂分叉。**第一天就定维护人+贡献流程+版本策略，否则别启动。** (evidence: [T03-S013])
  - 一次造大而全: 没用例支撑就建上百组件。**从审计出的真实高频用例起步，一个能用的小系统再演化。** (evidence: [T03-S013, T03-S012])
  - 设计与代码 token 不同步: Figma 一套、代码一套，越走越偏。**用 Tokens Studio/Supernova 建单一真值源自动同步。** (evidence: [T03-S013])
- **来源**: [Primary] T03-S012 (atomicdesign.bradfrost.com, 2026-06-19); [Primary] T03-S013 (Brad Frost design system ecosystem, 2026-06-19); [Reference] T03-S010 (Figma Dev Mode).
- **Last_updated**: 2026-06-19
- **Decay risk**: low（方法学稳态；AI/token 自动化为增量优化）

---

### 8. 无障碍合规（accessibility / WCAG）

- **One-liner**: 从「设计默认只服务健全用户」到「符合 WCAG 2.2 AA、对障碍用户可用、满足法规（如欧盟 EAA）」，把无障碍从事后补救变设计内建。
- **Trigger**: 法规要求（欧盟 EAA 2025-06-28 deadline、各国对应法规）、包容性产品目标、或审计/诉讼风险。 (evidence: [T03-S017, T03-S015])
- **Output**: WCAG 2.2 AA（EAA 现以 EN 301 549 / WCAG 2.1 AA 为基准、2.2 为前瞻最佳实践）符合的设计 + 无障碍审计报告 + 修复清单。 (evidence: [T03-S015, T03-S017])
- **入门 SOP（minimum viable steps）**:
  1. **定标准 + 范围**: 确定目标等级（通常 WCAG 2.x AA）与适用法规（EAA 等），划定要合规的页面/流程。跳过→做了一堆无障碍工作却不满足实际法规等级。 (evidence: [T03-S015, T03-S017])
  2. **设计阶段内建**: 配色对比度达标、不靠纯色传信息、可聚焦/键盘可达、文本可缩放、表单有标签。跳过→把无障碍推给开发末期补救，成本翻倍且补不全。 (evidence: [T03-S015])
  3. **自动扫描**: 用工具扫对比度/缺 alt/语义等机器可查项。跳过→明显问题漏网。 (evidence: [T03-S016])
  4. **人工审查 + 辅助技术测试**: 自动扫描只覆盖一部分，需人工 + 屏幕阅读器/键盘实测。跳过→以为合规其实大量体验问题（自动工具查不到）残留。 (evidence: [T03-S016])
  5. **出报告 + 修复 + 复测**: 记录不符合项、修复、回归测试。跳过→审计发现问题但不闭环，合规失败。 (evidence: [T03-S016])
- **资深路径（差异点）**：
  - **add**: 资深人**把无障碍前移到设计系统层**：组件库内建对比度/焦点态/语义，让下游产品默认合规，而非每个页面单独补。 (evidence: [T03-S015, T03-S013])
  - **optimize**: 资深人**自动化对比度/语义检查进设计流程**（Figma 插件、CI 里的 a11y lint），机器查能查的，人只查需要判断的。 (evidence: [T03-S016])
  - **add**: 资深人**让真实障碍用户参与测试**，而非只跑工具 — 自动+人工审查仍可能漏掉真实辅助技术体验问题。 (evidence: [T03-S016])
- **近期变化**（近 12 个月）:
  - 2025-06-28 **欧盟无障碍法（EAA）正式 deadline 生效**：在欧盟市场提供的新数字产品/服务须符合（基准 EN 301 549 / WCAG 2.1 AA，推荐 2.2 AA）；2025-06-28 前已上市的可延至 2030。把无障碍从「最佳实践」变「法律义务」，推动设计流程把 a11y 前移。触发事件类型: 法规变化。 (evidence: [T03-S017, T03-S015])
- **典型耗时**: 入门 SOP 取决于产品大小（审计+修复数周）；资深路径：设计系统层一次内建后，下游近零增量。
- **关键工具**: WCAG 2.2 quickref（标准）、自动扫描器（axe / Baymard UX-Ray heuristics）、屏幕阅读器、Figma a11y 插件。 (evidence: [T03-S015, T03-S016])
- **关键人物**: W3C WAI（标准）；无障碍专精从业者；设计系统团队（内建合规）。 (evidence: [T03-S015, T03-S016])
- **常见失败模式**:
  - 末期补救: 上线前才想起无障碍，对比度/结构性问题已无法低成本修。**在设计阶段就查对比度/键盘/语义，并把规则下沉到设计系统组件。** (evidence: [T03-S015])
  - 只跑自动扫描就声称合规: 自动工具只覆盖部分准则。**自动扫描后必须做人工 + 屏幕阅读器/键盘实测，否则合规是假的。** (evidence: [T03-S016])
  - 不让障碍用户参与: 健全人代测漏掉真实痛点。**安排真实辅助技术用户测关键流程。** (evidence: [T03-S016])
- **来源**: [Primary] T03-S015 (W3C WCAG 2.2, 2026-06-19); [Primary] T03-S016 (W3C WAI evaluate, 2026-06-19); [Primary] T03-S017 (EU EAA portal, 2026-06-19).
- **Last_updated**: 2026-06-19
- **Decay risk**: low（标准/法规稳态；EAA 已生效，下次大变看 WCAG 3.0 与各国执法细化）

---

## Phase 2 提炼提示

**反复出现 ≥ 3 个 workflow 都包含的步骤**（候选 playbook 通则）:
- **「先定要回答的决策/结果，再行动」**: 出现于 W1(定研究问题)/W2(周一定目标)/W6(定 desired outcome)/W8(定标准范围) → 候选 playbook「如果不先锁定『这步要支撑哪个决策』，则任何研究/设计/合规都会跑偏」。这是本行 SOP 第一通则。 (evidence: [T03-S022, T03-S008, T03-S001, T03-S015])
- **「观察真实行为 / 真人验证，不靠意见」**: 出现于 W1(问行为不问意见)/W2(周五测 5 人)/W3(可用性测试)/W6(每周真人接触)/W8(障碍用户参与) → 候选 playbook「stated ⇄ revealed：永远用真人真实行为验证，自陈偏好不算数」。对应行业第一性张力。 (evidence: [T03-S022, T03-S003, T03-S001])
- **「token / 单一真值源对齐」**: 出现于 W4(对齐 token)/W5(绑 token)/W7(建 token)/W8(组件内建合规) → 候选 playbook「设计系统是上游真值源，下游一切（生成/交付/合规）都映射到它，而非平行造轮子」。 (evidence: [T03-S013, T03-S011, T03-S015])
- **「AI 起草 + 人精炼/判断」**: 出现于 W1(AI 合成)/W2(AI 提速 sprint)/W4(AI 生成 UI)/W6(AI discovery) → 候选 playbook「AI 当研究助理/草稿机，人保留品味、收敛与战略判断；不让 AI 当决策者或直接 ship」。 (evidence: [T03-S014, T03-S018, T03-S001])

**入门 SOP 和资深路径之间最大的差距**（候选 心智模型）:
- 入门 SOP 平均 5-6 步、流程齐全；资深路径反复体现**「按风险匹配投入」**（W1 Just Enough Research、W2 对低风险不用 sprint、W3 折扣可用性）→ 心智模型候选「**研究/流程的厚度应匹配决策的风险与可逆性，不为做而做**」。
- 资深路径反复**把质量下沉到系统/上游**（W4/W5/W7/W8 都把一致性与合规放进设计系统层，一次内建下游受益）→ 心智模型候选「**别在每个页面重复解决一致性/合规，把它做进设计系统这个真值源**」。
- 资深路径普遍**消解阶段边界**（W5 handoff 从事件变持续连接、W6 研究从项目变每周节奏、W4 设计与代码边界模糊）→ 心智模型候选「**现代 UX 是连续流而非瀑布交接；设计、研究、开发持续耦合**」。

**近期工作流变化的根本原因**（触发事件类型分布）:
- **新工具 / 新模型（AI）**: 5 个 workflow 受影响 — W1(AI 合成)、W2(AI 提速)、W4(prompt-to-UI，最剧烈)、W5(Dev Mode / design↔code)、W6(AI discovery)、W7(AI 设计系统)。**主导驱动力 = 生成式 AI 把「起草」自动化，逼资深价值上移到判断/品味/系统对齐。**
- **法规变化**: 1 个 — W8(欧盟 EAA 2025-06-28 deadline) 把无障碍从最佳实践变法律义务。
- **行业事件（远程常态）**: 1 个 — W2(Design Sprint 远程化拆块)。
- **方法论扩散**: 1 个 — W6(continuous discovery 取代瀑布研究)。
- → Phase 2 行业「外部驱动力」首位是 **生成式 AI 重写设计 pipeline**（影响心智模型与反模式最深），其次 **无障碍法规** 与 **持续探索范式**。

**矛盾点 / 待裁决**（Phase 1.5）:
- **「handoff 已死」vs「handoff 仍是核心技能」**: 一派（design engineer / 持续连接论）说设计→开发交付正在消失；Figma 官方仍在出 handoff handbook 当核心技能教。代表行业正经历 workflow 跃迁，两者并存（成熟团队趋持续连接，多数团队仍做离散 handoff）。 (evidence: [T03-S010, T03-S011])
- **「先线框再高保真」vs「先 AI 生成再精炼」**: 经典瀑布（lo-fi→hi-fi）与 AI 时代「生成优先」在探索阶段冲突。当前共识是探索期可生成优先、但精炼与系统对齐不可省。 (evidence: [T03-S018])
- **WCAG 2.1 vs 2.2 基准**: EAA 操作基准目前是 EN 301 549 / WCAG 2.1 AA，2.2 是前瞻推荐，存在「该按哪版做」的实务分歧。 (evidence: [T03-S017, T03-S015])

**冷僻 / 信号薄弱**:
- workflow 数 = **8**（≥4，不冷僻）；一手 source 占比 ≈ **96%**（≫50%）；资深差异点：8/8 workflow 均有 ≥ 2 处（100% 覆盖，不缺失）。
- **本维度信号充足，非冷僻行业。** 唯一时效警示：高 decay 的 3 个 workflow（AI 生成 UI / handoff / 研究 AI 合成）**6-12 个月内大概率显著过时**，Phase 2.8 诚实边界应明确警告「本 skill 工作流模块中 AI 相关部分衰减最快，建议每 3-6 月跑 update」。
