# Track 02 — Tools (工具栈与选型决策树) · 产品设计 / UX 设计

> locale=global, profile=practitioner. **last_checked 全部 = 2026-06-19。**
> 行业判定 = **NOT cold**（公开材料极丰富）。工具栈是 master skill 衰减最快的部分 —— AI 层 Decay risk 普遍 high。
>
> **bucket 判定说明**：vendor 官网 / 官方 docs = `verified_primary`（厂商一手发声，per `_source_id_manifest.md` Surrogate Sources Policy 表）。
> `source_verifier.py` 默认把未知 host 判 `secondary`，本表按 manifest 规范把 vendor 官网升级为 `verified_primary` 并在 note 标注。
> 第三方对比 / listicle / Medium / survey 聚合 = `secondary`。GitHub repo root = `verified_primary`。
> 黑名单（知乎/公众号/百度/CSDN/G2/Capterra 评分页）= 0 条进表。
> ⚠️ mental-model / 市场份额类 claim 不靠单一 vendor 一面之词，均挂 ≥2 源。

## Source Manifest

| source_id | url | bucket | last_checked | author/host | one-line note |
|-----------|-----|--------|--------------|-------------|---------------|
| T02-S001 | https://www.figma.com | verified_primary | 2026-06-19 | Figma | vendor 官网，绝对主导设计工具 |
| T02-S002 | https://uxtools.co/survey/ | secondary | 2026-06-19 | UX Tools (Taylor Palmer & Jordan Bowman) | Design Tools Survey，行业最权威采用率调查 (2,220 resp) |
| T02-S003 | https://github.com/storybookjs/storybook | verified_primary | 2026-06-19 | Storybook (Chromatic) | 组件 workshop，设计系统开发侧标准 |
| T02-S004 | https://www.maze.co | verified_primary | 2026-06-19 | Maze | vendor 官网，Figma 原型测试主导 |
| T02-S005 | https://dovetail.com | verified_primary | 2026-06-19 | Dovetail | vendor 官网，研究库 (research repository) 主导 |
| T02-S006 | https://www.usertesting.com | verified_primary | 2026-06-19 | UserTesting | vendor 官网，视频可用性测试 + 百万级 panel |
| T02-S007 | https://www.optimalworkshop.com | verified_primary | 2026-06-19 | Optimal Workshop | vendor 官网，卡片分类/树测试 (OptimalSort/Treejack) |
| T02-S008 | https://clarity.microsoft.com | verified_primary | 2026-06-19 | Microsoft | vendor 官网，完全免费热图/会话回放 |
| T02-S009 | https://www.hotjar.com | verified_primary | 2026-06-19 | Hotjar (Contentsquare) | vendor 官网，热图 + 反馈，行业老牌 |
| T02-S010 | https://penpot.app | verified_primary | 2026-06-19 | Penpot (Kaleidos) | vendor 官网，开源 Figma 替代，500k+ 用户 |
| T02-S011 | https://www.framer.com | verified_primary | 2026-06-19 | Framer | vendor 官网，高保真原型 → 建站转向 |
| T02-S012 | https://www.sketch.com | verified_primary | 2026-06-19 | Sketch | vendor 官网，macOS 原生老牌，已衰退 |
| T02-S013 | https://www.protopie.io | verified_primary | 2026-06-19 | ProtoPie | vendor 官网，高级微交互/传感器原型 |
| T02-S014 | https://v0.dev | verified_primary | 2026-06-19 | Vercel | vendor 官网，prompt→React+Tailwind 生成 UI |
| T02-S015 | https://zeroheight.com | verified_primary | 2026-06-19 | zeroheight | vendor 官网，设计系统文档平台，满意度第一 |
| T02-S016 | https://tokens.studio | verified_primary | 2026-06-19 | Tokens Studio | vendor 官网，Figma design tokens 插件 |
| T02-S017 | https://www.supernova.io | verified_primary | 2026-06-19 | Supernova | vendor 官网，design→code token 自动化 |
| T02-S018 | https://miro.com | verified_primary | 2026-06-19 | Miro | vendor 官网，协作白板老牌 |
| T02-S019 | https://baymard.com/ux-ray | verified_primary | 2026-06-19 | Baymard Institute | vendor 官网，UX-Ray 2.0 AI 启发式扫描器 (154 heuristics) |
| T02-S020 | https://www.qualtrics.com/articles/strategy-research/ux-research-tools/ | secondary | 2026-06-19 | Qualtrics | 2026 UX 研究工具综述 |
| T02-S021 | https://greatquestion.co/blog/best-user-research-tools-in-2026-10-platforms-compared | secondary | 2026-06-19 | Great Question | 2026 研究工具对比 (各工具职责分界) |
| T02-S022 | https://news.adobe.com/news/news-details/2023/adobe-and-figma-mutually-agree-to-terminate-merger-agreement | verified_primary | 2026-06-19 | Adobe | Adobe-Figma 收购终止官方声明 (2023-12-18) |
| T02-S023 | https://mapsoft.com/adobe-xd-end-of-life/ | secondary | 2026-06-19 | Mapsoft | Adobe XD 维护模式/停更状态 (2026) |
| T02-S024 | https://artofstyleframe.com/blog/best-ui-design-tools-2026-compared/ | secondary | 2026-06-19 | Art of Styleframe | 2026 UI 工具三层市场结构分析 |
| T02-S025 | https://report.zeroheight.com/ | verified_primary | 2026-06-19 | zeroheight | Design Systems Report 2026 (行业调查) |
| T02-S026 | https://flowstep.ai/blog/best-ai-ui-design-tools/ | secondary | 2026-06-19 | Flowstep | 2026 AI UI 工具对比 (Figma Make/v0/Galileo) |
| T02-S027 | https://www.codercops.com/blog/figma-ai-design-tools-2026 | secondary | 2026-06-19 | Codercops | Figma AI (First Draft/Make) 2026 状态 |
| T02-S028 | https://getperspective.ai/blog/best-ai-ux-research-tools-2026-ranked-by-stage | secondary | 2026-06-19 | Perspective AI | AI 研究工具按研究阶段分类 |
| T02-S029 | https://principleformac.com/ | verified_primary | 2026-06-19 | Principle | vendor 官网，单人公司微交互工具 (仍活跃, v5.6) |
| T02-S030 | https://config.figma.com/ | verified_primary | 2026-06-19 | Figma | Config 大会 (工具风向标，wave1 T05-S014 复用) |

---

## 总览（按 tier 分组）

### 必备（9 个 · ≥80% 或核心管线刚需）
| 工具 | 一句话 | Decay | Sources |
|------|--------|-------|---------|
| Figma | 设计 + 原型 + 协作的事实标准，~80% 主导 | low | T02-S001, S002, S024 |
| FigJam | Figma 内置协作白板，研究/构思 workshop | low | T02-S001, S002 |
| Maze | Figma 原型的无主持可用性测试 + 任务流分析 | medium | T02-S004, S021 |
| Dovetail | 研究库 (repository)，AI 转录/标签/主题归纳 | medium | T02-S005, S021 |
| Storybook | 组件 workshop，设计系统开发侧文档/测试标准 | low | T02-S003 |
| Microsoft Clarity | 完全免费热图 + 会话回放，行为分析入门 | low | T02-S008 |
| Optimal Workshop | 卡片分类 (OptimalSort) + 树测试 (Treejack) IA 验证 | low | T02-S007 |
| Miro | 协作白板老牌，跨团队 workshop / journey map | low | T02-S018 |
| Amplitude / Mixpanel | 产品分析 / 北极星指标度量 (二选一) | low | T02-S020(类) |

### 场景特化（8 个）
| 工具 | 一句话 | Decay | Sources |
|------|--------|-------|---------|
| Framer | 高保真原型 + 真实建站发布，已转向 website builder | medium | T02-S011, S024 |
| ProtoPie | 复杂微交互 / 传感器 / 多设备高级原型 | medium | T02-S013 |
| Principle | macOS 上轻量时间轴动效原型 (单人公司) | high | T02-S029 |
| UserTesting | 已上线产品的视频可用性测试 + 百万级 panel | medium | T02-S006 |
| Hotjar | 热图 + 调研问卷 (付费, 比 Clarity 更全功能) | medium | T02-S009 |
| zeroheight | 设计系统文档平台 (设计↔代码双向同步) | medium | T02-S015, S025 |
| Tokens Studio | Figma design tokens 管理 (W3C 标准) | medium | T02-S016, S025 |
| Penpot | 开源 / 自托管 Figma 替代 (无 feature gate) | medium | T02-S010, S024 |

### 新兴（5 个 · 近 12 月，Decay high）
| 工具 | 一句话 | Decay | Sources |
|------|--------|-------|---------|
| Figma Make | Figma 内 prompt→可运行原型 (First Draft 后继) | high | T02-S026, S027 |
| v0 by Vercel | prompt→React+Tailwind 代码 UI，agentic | high | T02-S014, S026 |
| Google Stitch (前 Galileo AI) | prompt→可编辑 Figma 图层，2025 被 Google 收购 | high | T02-S026 |
| Uizard (Miro 旗下) | 草图/截图→可编辑设计，Autodesigner 多屏生成 | high | T02-S026 |
| Baymard UX-Ray 2.0 | AI 启发式扫描 (154 heuristics) 自动可用性审查 | high | T02-S019 |

---

## 必备层

### 1. Figma
- **One-liner**: 设计 + 原型 + 实时协作 + Dev Mode 交付的一体化平台，数字产品设计事实标准。
- **Tier**: 必备
- **Maintainer / Owner**: Figma, Inc.（https://www.figma.com）
- **License**: proprietary（免费层 + Professional/Organization 订阅）
- **Maturity signals**:
  - 市场份额：UX Tools 调查口径 ~80%+ 主导（"最彻底的工具坍缩"）；6sense 检测口径 ~40%；tech 公司 ~70% (last checked 2026-06-19) (evidence: [T02-S002, T02-S024])
  - 企业渗透：S-1 披露 95% 财富 500 强使用 (evidence: [T02-S002])
  - 生态：5,000+ 插件 (evidence: [T02-S002])
- **不适合 / 替代方案**: 需开源 / 自托管 / 数据主权 → Penpot；macOS 原生离线 → Sketch；高级动效 → ProtoPie。
- **生产案例**: 财富 500 强 95%、绝大多数 tech 公司主设计工具 (evidence: [T02-S002])
- **维护者背景**: Dylan Field (CEO)；Config 大会是行业最大风向标 (Track 05 T05-S014 / 本表 T02-S030)
- **近期变化**: 2023-12-18 Adobe $20B 收购因欧盟/英国监管终止，Adobe 付 $1B 分手费，Figma 保持独立 (evidence: [T02-S022])；推出 Figma Make / First Draft AI 层 (见新兴)。
- **来源**: [Primary] figma.com (T02-S001) · [Secondary] UX Tools Survey (T02-S002), Art of Styleframe (T02-S024) · [Primary] Adobe 终止声明 (T02-S022)
- **可信度**: high
- **Decay risk**: low（已是行业基础设施，3+ 年稳定；AI 冲击在其内部消化而非取代它）

### 2. FigJam
- **One-liner**: Figma 内置的协作白板，用于研究综合、亲和图、journey map、构思 workshop。
- **Tier**: 必备
- **Maintainer / Owner**: Figma, Inc.
- **License**: proprietary（含于 Figma 订阅）
- **Maturity signals**: 与 Figma 同生态，digital whiteboarding 类 UX Tools 调查领先项之一 (2026-06-19) (evidence: [T02-S002])
- **不适合 / 替代方案**: 已用 Miro/Mural 企业版的团队、需更重项目管理 → Miro。
- **生产案例**: Figma 用户默认白板入口 (evidence: [T02-S001])
- **近期变化**: AI 整理便利贴 / 自动归类。
- **来源**: [Primary] figma.com (T02-S001) · [Secondary] UX Tools (T02-S002)
- **可信度**: high · **Decay risk**: low

### 3. Maze
- **One-liner**: 与 Figma 紧耦合的无主持原型测试 + 任务流分析 —— 「checkout 流程用户能不能走通」的工具。
- **Tier**: 必备
- **Maintainer / Owner**: Maze（https://www.maze.co）
- **License**: proprietary（免费层 + 付费）
- **Maturity signals**: 「因紧密 Figma 集成 + 任务流分析占据原型验证」(evidence: [T02-S021])；Maze Future of User Research Report 2026 称 69% 研究者已在部分项目用 AI（同比 +19 点）(evidence: [T02-S021])
- **典型使用场景**: 未完成设计阶段的无主持可用性测试；A/B 原型对比；快速量化任务成功率。
- **不适合 / 替代方案**: 已上线产品的真人视频观察 → UserTesting；深度有主持访谈 → Lookback；纯 IA 验证 → Optimal Workshop。
- **生产案例**: 设计驱动团队原型验证标准 (evidence: [T02-S021])
- **来源**: [Primary] maze.co (T02-S004) · [Secondary] Great Question (T02-S021)
- **可信度**: high · **Decay risk**: medium（AI 研究工具赛道激烈，紧 Figma 集成是护城河）

### 4. Dovetail
- **One-liner**: AI 驱动的研究库 (research repository) —— 集中、转录、标签、归纳跨访谈/测试/支持的用户洞察。
- **Tier**: 必备
- **Maintainer / Owner**: Dovetail（https://dovetail.com）
- **License**: proprietary（Professional $20/user/mo + Enterprise）
- **Maturity signals**: 「a repository」类目代表工具；AI 语义搜索/自动摘要/dashboard (2026-06-19) (evidence: [T02-S005, T02-S021])
- **典型使用场景**: 多来源定性数据沉淀为可检索知识库；用 tag 跨研究找模式；团队共享洞察避免重复研究。
- **不适合 / 替代方案**: 只做单次原型测试不需要库 → Maze 自带；预算敏感小团队 → Notion/表格临时替代。
- **生产案例**: 企业研究团队中央洞察库 (evidence: [T02-S021])
- **近期变化**: 转型「customer intelligence platform」，AI synthesis 加强。
- **来源**: [Primary] dovetail.com (T02-S005) · [Secondary] Qualtrics (T02-S020), Great Question (T02-S021)
- **可信度**: high · **Decay risk**: medium（AI synthesis 类竞争激烈，但 repository 沉淀有粘性）

### 5. Storybook
- **One-liner**: 隔离环境中构建、文档化、测试 UI 组件的「行业标准 workshop」—— 设计系统开发侧落地标准。
- **Tier**: 必备（设计系统 / design engineer 场景）
- **Maintainer / Owner**: Storybook（Chromatic 团队，https://github.com/storybookjs/storybook）
- **License**: open（MIT）
- **Maturity signals**:
  - GitHub stars: 90.4k (2026-06-19) (evidence: [T02-S003])
  - Latest release: v10.4.6, 2026-06-16 (evidence: [T02-S003])
  - Activity: healthy（release 仅 3 天前）
- **典型使用场景**: 组件库孤立开发/视觉回归测试；设计↔工程的组件真实状态对照；交付时的活文档。
- **不适合 / 替代方案**: 纯设计师无代码场景 → zeroheight（文档平台）；仅 token 管理 → Tokens Studio。
- **生产案例**: 设计系统/前端团队组件 workshop 默认；与 design system 必绑。
- **维护者背景**: 与 Track 01 设计系统派 (Brad Frost Atomic Design / Nathan Curtis tokens) 工作流互补。
- **来源**: [Primary] GitHub repo (T02-S003)
- **可信度**: high · **Decay risk**: low（90k stars + 周级 release，前端基础设施）

### 6. Microsoft Clarity
- **One-liner**: 完全免费的行为分析 —— 无限会话回放 + 热图，「付费工具 80% 的功能，0% 的价格」。
- **Tier**: 必备（行为分析入门刚需）
- **Maintainer / Owner**: Microsoft（https://clarity.microsoft.com）
- **License**: proprietary（完全免费）
- **Maturity signals**: 无限会话回放 + 热图免费（数据留存有限）(2026-06-19) (evidence: [T02-S008])
- **典型使用场景**: 上线产品真实行为观察；rage click / dead click 诊断；零预算团队的热图入口。
- **不适合 / 替代方案**: 需 scroll/attention 热图 + 反馈问卷 + 调研 → Hotjar；需产品指标分析 → Amplitude/Mixpanel。
- **生产案例**: 大量团队作为免费行为分析底座 (evidence: [T02-S008])
- **来源**: [Primary] clarity.microsoft.com (T02-S008) · [Secondary] Clarity vs Hotjar 对比 (T02-S008 搜索)
- **可信度**: high · **Decay risk**: low（微软免费产品，行业稳态）

### 7. Optimal Workshop
- **One-liner**: 信息架构研究套件 —— 卡片分类 (OptimalSort)、树测试 (Treejack)、首次点击 (Chalkmark)。
- **Tier**: 必备（IA 场景刚需，canon 反复点名）
- **Maintainer / Owner**: Optimal Workshop（新西兰，https://www.optimalworkshop.com）
- **License**: proprietary（订阅）
- **Maturity signals**: 卡片分类基于用户心智模型定 IA；树测试验证 IA 直觉性 (2026-06-19) (evidence: [T02-S007])
- **典型使用场景**: 导航/IA 重构前用卡片分类挖心智模型；上线前用树测试验证能否找到内容；首次点击测试关键路径。
- **不适合 / 替代方案**: 通用原型测试 → Maze；廉价替代 → UXtweak。
- **生产案例**: IA 工作流标准工具，Track 04 canon「card sorting/tree testing」直接对应。
- **来源**: [Primary] optimalworkshop.com (T02-S007)
- **可信度**: high · **Decay risk**: low（IA 方法本身稳定）

### 8. Miro
- **One-liner**: 协作白板老牌 —— 跨团队 workshop、亲和图、journey map、design sprint 画布。
- **Tier**: 必备（白板，FigJam 之外的企业选择）
- **Maintainer / Owner**: Miro（https://miro.com）
- **License**: proprietary（免费层 + 付费）
- **Maturity signals**: digital whiteboarding 类 UX Tools 调查领先项 (2026-06-19) (evidence: [T02-S002])
- **典型使用场景**: 非 Figma 生态团队的 workshop；大型 design sprint；含产品/工程的跨职能协作。
- **不适合 / 替代方案**: 已重度用 Figma → FigJam（同生态省切换）；轻量 → Mural。
- **生产案例**: 企业 design sprint / 远程 workshop 主力 (evidence: [T02-S002])
- **近期变化**: 收购 Uizard（AI 生成 UI，见新兴）。
- **来源**: [Primary] miro.com (T02-S018) · [Secondary] UX Tools (T02-S002)
- **可信度**: high · **Decay risk**: low

### 9. Amplitude / Mixpanel（产品分析，二选一）
- **One-liner**: 产品行为分析平台，承载北极星指标 / HEART 框架的量化度量。
- **Tier**: 必备（度量阶段刚需）
- **Maintainer / Owner**: Amplitude, Inc. / Mixpanel, Inc.
- **License**: proprietary（均有免费层）
- **Maturity signals**: 产品分析两大主流，与 intake「Amplitude/Mixpanel/北极星」一致 (2026-06-19) (evidence: [T02-S020 类])
- **典型使用场景**: 设计改动后的留存/转化/漏斗度量；北极星指标看板；A/B 实验结果分析。
- **不适合 / 替代方案**: 仅需热图/回放 → Clarity；需 session-level 行为 → 二者皆可。
- **生产案例**: 产品/设计团队北极星度量标准栈。
- **来源**: [Secondary] Qualtrics 综述及 intake 工具栈 (T02-S020 类)
- **可信度**: medium（本 track 未做深度采用率核验，依 intake + 行业共识）· **Decay risk**: low

---

## 场景特化层

### 10. Framer
- **One-liner**: 高保真交互原型 + 直接发布真实网站 —— 已从纯原型工具转向 website builder。
- **Tier**: 场景特化
- **Maintainer / Owner**: Framer（https://www.framer.com）
- **License**: proprietary
- **Maturity signals**: 「Framer 因交互性获胜」「已转向建站，远离传统设计/原型工具」(2026-06-19) (evidence: [T02-S024])
- **典型使用场景**: 需要带真实交互/动效的高保真原型；marketing/landing page 设计即发布；设计师做无代码建站。
- **不适合 / 替代方案**: 团队级产品设计协作 → Figma；纯组件交付 → Storybook。
- **生产案例**: 设计师独立建站 + 高保真营销页 (evidence: [T02-S024])
- **近期变化**: 战略转向 website builder（影响其在「产品设计原型」语境的定位）。
- **来源**: [Primary] framer.com (T02-S011) · [Secondary] Art of Styleframe (T02-S024)
- **可信度**: high · **Decay risk**: medium（定位漂移中）

### 11. ProtoPie
- **One-liner**: 高级微交互 / 传感器 / 多设备原型 —— Figma 静态原型搞不定的复杂交互。
- **Tier**: 场景特化
- **Maintainer / Owner**: ProtoPie（https://www.protopie.io）
- **License**: proprietary
- **Maturity signals**: intake 工具栈锚点「ProtoPie 微交互」(2026-06-19) (evidence: 本表 intake)
- **典型使用场景**: 复杂条件逻辑/状态机原型；硬件传感器（陀螺仪/麦克风）联动；跨设备（手机↔手表↔车机）原型。
- **不适合 / 替代方案**: 基础点击流原型 → Figma 自带（无需引入）；时间轴动效 → Principle。
- **生产案例**: 车载/IoT/硬件交互团队高保真原型。
- **来源**: [Primary] protopie.io (T02-S013)
- **可信度**: medium · **Decay risk**: medium

### 12. Principle
- **One-liner**: macOS 上轻量时间轴动效原型工具（单人公司维护，仍活跃）。
- **Tier**: 场景特化
- **Maintainer / Owner**: Principle（单人公司，https://principleformac.com）
- **License**: proprietary（macOS 买断）
- **Maturity signals**: 「单人公司」「v5.6 可用，重设计组件事件路由 UI」「网站/支持仍活跃」(2026-06-19) (evidence: [T02-S029])
- **典型使用场景**: macOS 设计师快速做时间轴/驱动型动效原型。
- **不适合 / 替代方案**: 复杂逻辑 → ProtoPie；团队协作 → Figma；跨平台 → 不适用（仅 macOS）。
- **生产案例**: macOS 个人设计师动效原型（小众）。
- **近期变化**: 单人维护，bus factor 高 —— 故 Decay risk high。
- **来源**: [Primary] principleformac.com (T02-S029)
- **可信度**: medium · **Decay risk**: high（单人公司，随时可能停更）

### 13. UserTesting
- **One-liner**: 已上线产品的视频可用性测试 + 百万级参与者 panel + 面部表情捕捉。
- **Tier**: 场景特化
- **Maintainer / Owner**: UserTesting（https://www.usertesting.com）
- **License**: proprietary（企业级，credit 制）
- **Maturity signals**: 「凭百万+ panel 与面部表情捕捉占据已上线产品的视频可用性」(2026-06-19) (evidence: [T02-S021])
- **典型使用场景**: 需要真人出声思考视频的可用性研究；快速从外部 panel 招募目标用户；高管要看「真实用户脸」时。
- **不适合 / 替代方案**: 原型快速量化 → Maze；自带用户库的深访 → Lookback；预算紧 → User Interviews 仅招募。
- **避坑**: 「credit 会过期、swimlane 限制并发研究数」(evidence: [T02-S021])
- **生产案例**: 企业研究团队 panel 招募 + 视频测试主力 (evidence: [T02-S021])
- **来源**: [Primary] usertesting.com (T02-S006) · [Secondary] Great Question (T02-S021)
- **可信度**: high · **Decay risk**: medium

### 14. Hotjar
- **One-liner**: 热图（含 scroll/attention）+ 会话回放 + 反馈问卷 —— 比 Clarity 功能全的付费方案。
- **Tier**: 场景特化
- **Maintainer / Owner**: Hotjar（Contentsquare 旗下，https://www.hotjar.com）
- **License**: proprietary（免费层 + $32–$500+/mo）
- **Maturity signals**: 「比 Clarity 多 scroll/attention 热图 + 反馈工具」，按会话量计价 (2026-06-19) (evidence: [T02-S009])
- **典型使用场景**: SMB/中端团队需要热图 + 反馈 + 调研问卷一体；需 Clarity 没有的 scroll/attention 热图。
- **不适合 / 替代方案**: 零预算 → Microsoft Clarity（免费拿 80%）；企业级 session replay → FullStory。
- **生产案例**: SMB/中端市场行为分析 + VoC (evidence: [T02-S009])
- **来源**: [Primary] hotjar.com (T02-S009) · [Secondary] Clarity vs Hotjar 对比 (T02-S008/S009 搜索)
- **可信度**: high · **Decay risk**: medium（免费 Clarity 持续蚕食低端）

### 15. zeroheight
- **One-liner**: 设计系统文档平台 —— 设计↔代码双向实时同步的单一真相源，满意度行业第一。
- **Tier**: 场景特化（设计系统）
- **Maintainer / Owner**: zeroheight（https://zeroheight.com）
- **License**: proprietary
- **Maturity signals**: 「Design Systems Report 2026 满意度第一，79% 正面」「采用率与设计系统信任度更高」(2026-06-19) (evidence: [T02-S025])
- **典型使用场景**: 设计师 + 工程师 + PM 共享的设计系统文档门户；设计↔代码自动同步；多受众单一真相源。
- **不适合 / 替代方案**: 纯开发组件文档 → Storybook；含 token 自动产出 + design engineering → Supernova。
- **生产案例**: 有 design system 的团队文档门户 (evidence: [T02-S025])
- **来源**: [Primary] zeroheight.com (T02-S015), Design Systems Report 2026 (T02-S025)
- **可信度**: high · **Decay risk**: medium

### 16. Tokens Studio
- **One-liner**: Figma 内 design tokens 管理插件，输出 W3C 标准 token 格式。
- **Tier**: 场景特化（设计系统）
- **Maintainer / Owner**: Tokens Studio（https://tokens.studio）
- **License**: proprietary（免费 + Pro）
- **Maturity signals**: 「design token 采用在企业加速，受多品牌/多平台需求驱动」「与 Supernova 合作成主要输出层」(2026-06-19) (evidence: [T02-S025])
- **典型使用场景**: 多品牌/多平台的 token 化设计系统；Figma 变量 → 代码 token 管道；与 Supernova 联用做 design→code。
- **不适合 / 替代方案**: 简单单品牌系统 → Figma 原生变量足够；不需 W3C 格式 → 跳过。
- **生产案例**: 企业多品牌设计系统 token 层 (evidence: [T02-S025])
- **维护者背景**: 关联 Track 01 design tokens 派 (Nathan Curtis / W3C Design Tokens CG, 见 Track 04 T04-S012/S015)。
- **来源**: [Primary] tokens.studio (T02-S016), Design Systems Report 2026 (T02-S025)
- **可信度**: high · **Decay risk**: medium

### 17. Penpot
- **One-liner**: 开源 / 可自托管的 Figma 替代 —— 浏览器实时协作，免费层无 feature gate。
- **Tier**: 场景特化（开源 / 数据主权场景）
- **Maintainer / Owner**: Penpot（Kaleidos，https://penpot.app）
- **License**: open（MPL-2.0）
- **Maturity signals**: 「从开源实验成长为生产工具，500,000+ 活跃用户」「最佳免费 Figma 替代」(2026-06-19) (evidence: [T02-S010, T02-S024])
- **典型使用场景**: 需要数据主权/自托管的组织（政府/合规/反厂商锁定）；预算为零的团队；开源原教旨团队。
- **不适合 / 替代方案**: 需成熟插件生态/AI 层/全行业互通 → Figma；个人 macOS → Sketch。
- **生产案例**: 500k+ 活跃用户，自托管组织采用 (evidence: [T02-S010])
- **来源**: [Primary] penpot.app (T02-S010) · [Secondary] Art of Styleframe (T02-S024)
- **可信度**: high · **Decay risk**: medium（上升中，但 Figma 引力强）

---

## 新兴层（近 12 个月 · stability: experimental · Decay risk high）

### 18. Figma Make
- **One-liner**: Figma 内的 prompt→可运行原型 / 代码生成（First Draft 的后继 AI 层）。
- **Tier**: 新兴 · **stability: experimental**
- **Maintainer / Owner**: Figma, Inc.
- **License**: proprietary（含于 Full $20/mo，免费层有限 credit）
- **Maturity signals**: 「仅含于 Full 套餐 $20/mo 起」「Figma AI: First Draft、AI Grid 改变了 handoff」(2026-06-19) (evidence: [T02-S026, T02-S027])
- **典型使用场景**: 设计师在 Figma 内直接生成首版 UI / 可运行原型，省去手搭。
- **不适合 / 替代方案**: 需输出生产 React 代码 → v0；导入 Figma 可编辑图层 → Google Stitch。
- **早期采用者**: Figma 自家 Config 反复演示，付费用户早期试用 (evidence: [T02-S027])
- **来源**: [Secondary] Codercops (T02-S027), Flowstep (T02-S026)
- **可信度**: medium · **Decay risk**: high（12 月内被显著改变概率 >40%，AI 功能迭代极快）

### 19. v0 by Vercel
- **One-liner**: prompt→React+Tailwind UI 组件生成，带 agentic（搜索/调试/一键部署）能力。
- **Tier**: 新兴 · **stability: experimental**
- **Maintainer / Owner**: Vercel（https://v0.dev）
- **License**: proprietary（免费 credit + 付费）
- **Maturity signals**: 「生成可运行 React+Tailwind，agentic：web 搜索/实时检查/错误调试/一键部署」(2026-06-19) (evidence: [T02-S014, T02-S026])
- **典型使用场景**: design engineer / 设计师直接产出可部署前端；从设计稿快速到代码原型；Tailwind 栈团队。
- **不适合 / 替代方案**: 非 React/Tailwind 栈 → 不适用；纯视觉设计不需代码 → Figma Make。
- **早期采用者**: Tailwind 生态团队、design engineer 群体广泛试用；Config 提及 (evidence: [T02-S030])
- **来源**: [Primary] v0.dev (T02-S014) · [Secondary] Flowstep (T02-S026)
- **可信度**: medium · **Decay risk**: high

### 20. Google Stitch（前 Galileo AI）
- **One-liner**: prompt→可编辑设计，直接导入 Figma 成可编辑图层 + auto-layout；2025 被 Google 收购改名。
- **Tier**: 新兴 · **stability: experimental**
- **Maintainer / Owner**: Google（前 Galileo AI）
- **License**: proprietary
- **Maturity signals**: 「Google 2025 收购 Galileo AI 改名 Stitch」「生成可编辑屏幕直接导入 Figma 图层」(2026-06-19) (evidence: [T02-S026])
- **典型使用场景**: 设计师快速探索多个设计方向，再在 Figma 上继续编辑。
- **不适合 / 替代方案**: 需代码输出 → v0；Figma 内闭环 → Figma Make。
- **早期采用者**: Google 生态 + 探索性设计师 (evidence: [T02-S026])
- **来源**: [Secondary] Flowstep (T02-S026)
- **可信度**: medium · **Decay risk**: high（被收购/改名/整合不确定性高）

### 21. Uizard（Miro 旗下）
- **One-liner**: 草图/截图/线框→可编辑数字设计；Autodesigner 从 prompt + 主题生成多屏可编辑 mockup。
- **Tier**: 新兴 · **stability: experimental**
- **Maintainer / Owner**: Miro（收购 Uizard）
- **License**: proprietary
- **Maturity signals**: 「把手绘草图/线框转数字设计」「Autodesigner 多屏可编辑生成」(2026-06-19) (evidence: [T02-S026])
- **典型使用场景**: 把白板草图/截图快速数字化；非设计师/PM 快速出多屏 mockup。
- **不适合 / 替代方案**: 高保真精修 → Figma；代码 → v0。
- **早期采用者**: Miro 生态 + 早期低保真团队 (evidence: [T02-S026])
- **来源**: [Secondary] Flowstep (T02-S026)
- **可信度**: medium · **Decay risk**: high

### 22. Baymard UX-Ray 2.0
- **One-liner**: AI 启发式扫描器（154 heuristics）自动扫描页面给可用性问题清单。
- **Tier**: 新兴 · **stability: experimental**
- **Maintainer / Owner**: Baymard Institute（https://baymard.com/ux-ray）
- **License**: proprietary（企业订阅）
- **Maturity signals**: 「UX-Ray 2.0，154 heuristics 的 AI 启发式评估」，基于 Baymard 700+ guideline / 20w+ 测试小时 (2026-06-19) (evidence: [T02-S019]，wave1 T05-S022)
- **典型使用场景**: 电商/转化页的自动化启发式审查；缺研究资源时的快速 heuristic evaluation 补充。
- **不适合 / 替代方案**: 真实用户行为 → Clarity/真人测试；非电商场景覆盖有限。
- **早期采用者**: Baymard 企业订阅客户、电商团队 (evidence: [T02-S019])
- **来源**: [Primary] baymard.com/ux-ray (T02-S019) · wave1 (T05-S022)
- **可信度**: medium · **Decay risk**: high（AI 评估准确度 + 方法论争议未定）

---

## 已废弃 / 衰退（不进任何层，仅作避坑参照）

- **Adobe XD** —— 维护模式，不再开发新功能、不向新客户单售；2023 Adobe-Figma 收购流产后 Adobe 明确不再投资。**不要给新项目选 XD。** (evidence: [T02-S022, T02-S023])
- **Sketch** —— 衰退中：macOS-only 限制跨平台团队，插件生态小于 Figma，仅守 macOS solo / 工作室基本盘。 (evidence: [T02-S024])
- **InVision** —— 已关停（其遗产 Design Better 内容仍在，见 Track 04/05）。

---

## 选型决策树

### 决策树 A: 你处在产品设计管线的哪一步？

#### Branch 1: 设计 + 原型 + 协作（主战场）
→ 推荐: **Figma**（事实标准，团队协作 + Dev Mode 交付一体）(evidence: [T02-S002])
→ 需开源/自托管/数据主权: **Penpot**（500k+ 用户，无 feature gate）(evidence: [T02-S010])
→ macOS 个人/离线: **Sketch**（但已衰退，新团队慎入）(evidence: [T02-S024])
→ 不推荐: **Adobe XD**（维护模式，已死，新项目零选择理由）(evidence: [T02-S023])
   - 真实案例: 财富 500 强 95% + 多数 tech 公司用 Figma (evidence: [T02-S002])

#### Branch 2: 你需要的「原型」复杂度？
##### Branch 2a: 基础点击流验证概念
→ **Figma 自带原型** 足够，别引入额外工具（避免 rotation cost）。
##### Branch 2b: 高保真交互 / 营销页即发布
→ **Framer**（交互性 + 真实建站，注意它已转向 website builder）(evidence: [T02-S024])
##### Branch 2c: 复杂逻辑 / 传感器 / 多设备（车载/IoT）
→ **ProtoPie**（条件逻辑 + 硬件传感器 + 跨设备）(evidence: [T02-S013])
##### Branch 2d: macOS 上轻量时间轴动效
→ **Principle**（但单人公司，bus factor 高，Decay high）(evidence: [T02-S029])

#### Branch 3: 你的核心目标是「用户研究」—— 哪个研究阶段？
> 「企业研究团队平均用 8–12 个工具，做得好的压到 2–4 个」——别堆工具。 (evidence: [T02-S021])
##### Branch 3a: 验证未完成设计的原型可用性
→ **Maze**（紧 Figma 集成 + 任务流分析）(evidence: [T02-S021])
##### Branch 3b: 已上线产品的真人视频可用性
→ **UserTesting**（百万 panel + 面部表情；注意 credit 过期 + swimlane 限制）(evidence: [T02-S021])
##### Branch 3c: 信息架构（导航/分类）研究
→ **Optimal Workshop**（卡片分类挖心智模型 → 树测试验证 IA）(evidence: [T02-S007])
##### Branch 3d: 沉淀跨研究的洞察知识库
→ **Dovetail**（research repository，AI 转录/标签/主题）(evidence: [T02-S005])
##### Branch 3e: 上线产品的真实行为观察（热图/回放）
→ 零预算: **Microsoft Clarity**（免费拿 80% 功能）(evidence: [T02-S008])
→ 需 scroll/attention 热图 + 反馈问卷: **Hotjar**（付费）(evidence: [T02-S009])

#### Branch 4: 你在做「设计系统 / 交付」
##### Branch 4a: 开发侧组件 workshop / 视觉回归
→ **Storybook**（90k stars，前端基础设施）(evidence: [T02-S003])
##### Branch 4b: 跨受众（设计/工程/PM）文档门户
→ **zeroheight**（满意度第一，设计↔代码双向同步）(evidence: [T02-S025])
##### Branch 4c: 多品牌/多平台 token 化
→ **Tokens Studio**（W3C token）+ **Supernova**（design→code 输出层）(evidence: [T02-S025])

#### Branch 5: 你想用 AI 加速「设计 → 代码 / 原型」（高风险层，先验证再依赖）
##### Branch 5a: 想留在 Figma 内闭环
→ **Figma Make**（First Draft 后继）(evidence: [T02-S027])
##### Branch 5b: 要输出可部署 React+Tailwind 代码
→ **v0 by Vercel**（agentic，一键部署）(evidence: [T02-S014])
##### Branch 5c: 要导入 Figma 可编辑图层探索方向
→ **Google Stitch**（前 Galileo AI）(evidence: [T02-S026])
##### Branch 5d: 把草图/截图快速数字化
→ **Uizard**（Autodesigner 多屏生成）(evidence: [T02-S026])
> ⚠️ 整个 Branch 5 的工具 Decay risk = high，「6–12 月后可能不存在 / 大改」，**不要把生产管线建在单一 AI 工具上**。

---

## 避坑清单

- ❌ **不要给新项目选 Adobe XD**：已进维护模式、不再开发新功能、不向新客户单售，2023 收购流产后 Adobe 明确放弃投资。 (evidence: [T02-S022, T02-S023])
- ❌ **不要把 Maze 当成 UserTesting 用（反之亦然）**：Maze 是未完成设计的无主持原型量化测试；UserTesting 是已上线产品的真人视频观察。混用会得错误信号。 (evidence: [T02-S021])
- ❌ **不要堆 8–12 个研究工具**：企业研究团队平均用 8–12 个、做得好的压到 2–4 个；工具碎片化反而稀释洞察。先选 repository（Dovetail）+ 1 个测试工具。 (evidence: [T02-S021])
- ❌ **不要为热图付费如果零预算够用**：Microsoft Clarity 免费给「付费工具 80% 的功能」，多数早期/中小团队无需上 Hotjar 付费层。 (evidence: [T02-S008])
- ❌ **不要把 Principle 押进团队关键管线**：单人公司维护，bus factor 极高，随时可能停更；macOS-only 也排除跨平台团队。 (evidence: [T02-S029])
- ❌ **不要把生产管线建在单一 AI 生成工具上**：Figma Make / v0 / Stitch / Uizard 全是 Decay high，迭代/被收购/改名风险大（Galileo→Google Stitch 就是先例），当加速器而非依赖。 (evidence: [T02-S026])
- ❌ **不要忽视设计↔代码同步的集成裂缝**：从业者反映最大缺口不是缺工具，而是设计/代码/文档同步仍靠手工、易错；选 zeroheight/Supernova 这类双向同步工具时先验证同步实际生效。 (evidence: [T02-S025])
- ❌ **不要混淆 Framer 的「原型工具」与「建站工具」定位**：Framer 已战略转向 website builder，若团队要的是产品设计协作而非建站，Figma 仍是答案。 (evidence: [T02-S024])

---

## Phase 2 提炼提示

**反复出现 ≥ 3 source 都强调的「工具选型原则」**（候选 playbook 规则）:
- **少工具，按研究阶段精选而非全堆**（出现于: T02-S021 「8–12 压到 2–4」/ S020 / S028 研究阶段分类）
- **AI 设计工具是加速器不是基础设施，Decay risk 一律高**（出现于: T02-S026 / S027 / S014，Galileo→Stitch 被收购改名为锚点）
- **Figma 是底座，其余工具围绕其集成而活**（出现于: T02-S002 / S004 Maze 紧集成 / S016 Tokens Studio 插件 / S001）
- **设计↔代码↔文档同步是真正瓶颈，不是缺工具**（出现于: T02-S025 / 设计系统报告）

**显著的工具流派分裂**（候选 智识谱系条目）:
- **闭源生态主导派**（Figma 一统：设计+原型+AI+交付一体，厂商锁定但生态最厚）vs **开源/数据主权派**（Penpot 自托管、无 feature gate、反厂商锁定）—— 对应 intake「一致性/规范 ⇄ 创新/自由」张力的工具投射。
- **设计师产物 = 像素图（Figma 出图）** vs **设计师产物 = 可运行代码（v0 / design engineer / Figma Make）** —— 对应 intake「designer 该不该 code」争论，Branch 5 整层就是这条裂缝的工具化。
- **量化无主持测试派**（Maze，快/可规模化/Figma 集成）vs **质化有主持观察派**（UserTesting/Lookback，真人视频/深度但慢/贵）—— 对应 intake「用户说的 ⇄ 用户做的」「数据 ⇄ 直觉」张力。

**工具开发者 → 喂 Track 01 figures**:
- Storybook（Chromatic 团队）、Tokens Studio（关联 Nathan Curtis / W3C Design Tokens CG，Track 04 已点名）—— design tokens 派可补 figure。
- Dylan Field（Figma CEO，Config keynote）—— 工具领袖型 figure 候选。

**工具暗示的工作流 → 喂 Track 03**:
- 研究阶段链：卡片分类(Optimal)→树测试(Optimal)→原型测试(Maze)→洞察沉淀(Dovetail)→上线行为观察(Clarity/Hotjar)→度量(Amplitude) —— 直接是一条 SOP。
- 设计系统链：Figma 变量 → Tokens Studio → Supernova/zeroheight → Storybook —— design-to-code 管道 SOP。

**新兴工具信号**:
- 当前活跃 / 上升的新工具数: 5（Figma Make / v0 / Google Stitch / Uizard / Baymard UX-Ray 2.0）
- 出现 → 主流 速度估计: AI 设计生成层约 6–12 个月一轮洗牌（Galileo 2024 起势 → 2025 被 Google 收购改名 Stitch，约 12–18 月）。

**冷僻 / 信号薄弱**:
- 必备层 9 个（远超 3）✅；必备层证据含 ~80% 采用率 survey ✅；新兴层 5 个（远超 2）✅。
- **本 track 信号厚，无冷僻问题。** 唯一弱项：Amplitude/Mixpanel 采用率未做本 track 独立深度核验（依 intake + 行业共识，标 medium 可信度）；产品分析归属 PM/设计交界，可在 Phase 2 注明。

---

## 质量自检

- [x] 候选数 ≥ 20？ —— 22 个 retained（探索 ~28，含 Mural/Lookback/dscout/User Interviews/Lyssna/Supernova/Galileo 等未单列或并入）✅
- [x] 三层都有内容？必备 9（≥3）/ 场景特化 8（≥5）/ 新兴 5（≥2）✅
- [x] 每个工具有 last_checked + ≥1 个带日期 maturity signal？✅（全部 2026-06-19；Storybook stars/release 带精确日期）
- [x] 选型决策树 5–10 节点？—— 5 主分支 + 多子分支（A1–A5，含 2a–2d/3a–3e/4a–4c/5a–5d）✅
- [x] 避坑清单 ≥ 5 条？—— 8 条 ✅
- [x] 一手来源 ≥ 50%？—— 30 源中 verified_primary 20 个 = 67% ✅
- [x] Decay risk 每个工具都标？✅
- [x] Phase 2 接口填了？✅
