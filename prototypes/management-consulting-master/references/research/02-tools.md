# Track 02 — Tools / 工具地图 — 管理咨询 (Management Consulting)

> locale = global (en-primary) | last_updated = 2026-06-09
> 行业定性：NOT cold — 工具栈公开材料丰富。但**关键认知前提**：管理咨询的「工具」不是软件目录，而是**双层栈** ——
> (1) **软件/数据工具**（PowerPoint+think-cell / Excel / 专家网络 / 行业数据库 / BI / GenAI），多为 **proprietary 闭源**，无 GitHub stars 可锚；
> (2) **框架工具**（MECE / 五力 / 2x2 / BCG 矩阵 / driver tree）—— 概念工具，与 Track 06 glossary / canon 交叉，本 track 只做「工具化清单 + 何时用 + 滥用风险」，深度留给 synthesis。
> **时效核心变量**：GenAI 工具栈（Lilli / Deckster / ChatGPT Enterprise）是本行近 12 月最大颠覆，对初级分析师工作冲击直接，全程标 decay HIGH。

---

## 维度特殊说明（为何不套 GitHub-stars 阈值）

通用 Track 02 模板用「GitHub stars 中位数 ×2」作必备层阈值。**管理咨询工具栈几乎全是 proprietary 商业软件**（PowerPoint / think-cell / Capital IQ / GLG / Lilli），无开源 repo、无 stars 数据。因此本 track 的必备层判定改用模板允许的另两条标准：
- **≥ 3 个独立 source 点名 + 行业「人手一个」共识**（如「世界前 10 咨询所全用 think-cell」evidence: [T02-S001]）；
- **firm 官方披露的内部采用率**（如 Lilli「72% 员工活跃」evidence: [T02-S003]）。

`Maturity signals` 字段改记录：**vendor 自报用户/公司数 + firm 官方采用率 + 成立/发布年份 + last_checked**，而非 stars/commit。这是模板「主流工具背后是闭源/不公开」失败处理分支的标准做法。

---

## Source Manifest

| source_id | url | bucket | last_checked | author/host | one-line note |
|-----------|-----|--------|--------------|-------------|---------------|
| T02-S001 | https://www.think-cell.com/en/ | surrogate_primary | 2026-06-09 | think-cell GmbH | vendor docs（供应商官方）：35,000+ 公司、世界前 10 咨询所全用、40+ 图表类型 |
| T02-S002 | https://www.think-cell.com/en/company/overview | surrogate_primary | 2026-06-09 | think-cell GmbH | vendor docs（供应商官方公司史）：2002 Berlin 创立，co-founder Arno Schödl ex-McKinsey/MS Research |
| T02-S003 | https://www.mckinsey.com/capabilities/tech-and-ai/how-we-help-clients/rewiring-the-way-mckinsey-works-with-lilli | verified_primary | 2026-06-09 | McKinsey & Company | Lilli 官方页：72% 员工活跃、500K+ prompts/月、~30% 时间节省 |
| T02-S004 | https://www.bain.com/about/media-center/press-releases/2024/bain-and-company-announces-expanded-partnership-with-openai-to-accelerate-delivery-of-ai-solutions-and-meet-fast-growing-client-needs/ | verified_primary | 2026-06-09 | Bain & Company | Bain×OpenAI 扩展合作官方稿 (2024-10-17)：CoE + ChatGPT Enterprise 全员 |
| T02-S005 | https://www.bain.com/vector-digital/partnerships-alliance-ecosystem/openai-alliance/ | verified_primary | 2026-06-09 | Bain & Company | Bain×OpenAI 联盟落地页 (2022 起合作) |
| T02-S006 | https://www.bcg.com/x | verified_primary | 2026-06-09 | BCG (BCG X) | BCG X 官方页：AI/数字化建造单元 |
| T02-S007 | https://www.computerworld.com/article/3491334/bcg-execs-ai-across-the-company-increased-productivity-employee-joy.html | secondary | 2026-06-09 | Computerworld | BCG 高管访谈：Deckster 450K+ 次造/改 slide、6,000+ 自建 GPT |
| T02-S008 | https://baileyherb.com/deckster | secondary | 2026-06-09 | Bailey Herbstreit (BCG designer) | Deckster 设计者作品集：One-Click Draft / Review This 功能拆解 |
| T02-S009 | https://glginsights.com/ | surrogate_primary | 2026-06-09 | GLG (Gerson Lehrman Group) | vendor docs（供应商官方站），最大专家网络，1M+ 专家 |
| T02-S010 | https://www.alphasights.com/ | surrogate_primary | 2026-06-09 | AlphaSights | vendor docs（供应商官方站），服务驱动快周转专家网络，咨询所偏好 |
| T02-S011 | https://www.thirdbridge.com/en-us/about-us/media/perspectives/glg-alternatives | surrogate_primary | 2026-06-09 | Third Bridge | vendor docs（供应商官方对比）：分析师主导访谈 + transcript library 差异化 |
| T02-S012 | https://www.silverlightresearch.com/blog/what-are-the-big-five-expert-networks | secondary | 2026-06-09 | Silverlight Research | 专家网络行业 landscape：Big 5 (GLG/AlphaSights/Guidepoint/Third Bridge/Coleman) |
| T02-S013 | https://www.spglobal.com/marketintelligence/en/ | verified_primary | 2026-06-09 | S&P Global Market Intelligence | Capital IQ vendor 官方：公司财务/transcript/筛选 |
| T02-S014 | https://www.ibisworld.com/ | surrogate_primary | 2026-06-09 | IBISWorld | vendor docs（供应商官方），行业市场 research：700+ US + 60 全球行业报告 |
| T02-S015 | https://pitchbook.com/ | surrogate_primary | 2026-06-09 | PitchBook (Morningstar) | vendor docs（供应商官方），PE/VC/M&A 私募市场数据 |
| T02-S016 | https://www.statista.com/ | surrogate_primary | 2026-06-09 | Statista | vendor docs（供应商官方），聚合统计/市场数据 |
| T02-S017 | https://www.alteryx.com/ | surrogate_primary | 2026-06-09 | Alteryx | vendor docs（供应商官方），数据准备/ETL/自动化 |
| T02-S018 | https://www.tableau.com/ | surrogate_primary | 2026-06-09 | Tableau (Salesforce) | vendor docs（供应商官方），数据可视化 |
| T02-S019 | https://powerbi.microsoft.com/ | surrogate_primary | 2026-06-09 | Microsoft | vendor docs（供应商官方），Power BI 商业智能 |
| T02-S020 | https://www.preplounge.com/consulting-forum/does-mbb-use-alteryx-tableau-or-power-bi-10762 | secondary | 2026-06-09 | PrepLounge forum | 在职/备考讨论：MBB 按项目用 Alteryx/Tableau/Power BI/Python |
| T02-S021 | https://deckary.com/blog/pillar-powerpoint-add-ins-guide | secondary | 2026-06-09 | Deckary | PowerPoint 咨询插件生态对比 (think-cell/Mekko/UpSlide/Power-user) |
| T02-S022 | https://deckary.com/blog/mekko-graphics-review | secondary | 2026-06-09 | Deckary | Mekko Graphics：Marimekko 专精，$399/yr，2007 创立 (insightsoftware) |
| T02-S023 | https://capitalizeconsulting.com/comparing-alteryx-tableau-and-power-bi/ | secondary | 2026-06-09 | Capitalize Analytics | Alteryx(准备) vs Tableau(可视化) vs Power BI(BI) 分工对比 |
| T02-S024 | https://www.qualtrics.com/ | surrogate_primary | 2026-06-09 | Qualtrics | vendor docs（供应商官方），企业级 survey/NPS/体验管理 |
| T02-S025 | https://www.mural.co/blog/tools-for-consulting-workshops | secondary | 2026-06-09 | Mural | 咨询 workshop 白板用例 + 客户协作模板 |
| T02-S026 | https://fortune.com/2025/11/25/deloitte-caught-fabricated-ai-generated-research-million-dollar-report-canada-government/ | secondary | 2026-06-09 | Fortune | Deloitte 加拿大 ~$1.6M 报告 AI 幻觉伪造引用 (2025-11) |
| T02-S027 | https://futurism.com/future-society/deloitte-government-ai-hallucinations | secondary | 2026-06-09 | Futurism | Deloitte 澳洲 $291K 退款：AI 幻觉假引用/假判词 |
| T02-S028 | https://www.proskauer.com/blog/sec-risk-alert-highlights-renewed-focus-on-insider-trading-and-mnpi-policies-and-procedures-for-fund-managers | verified_primary | 2026-06-09 | Proskauer Rose LLP | SEC Risk Alert：专家网络 call 的 MNPI/内幕交易合规要求（律所一手解读） |
| T02-S029 | https://hbr.org/2021/02/are-you-doing-the-swot-analysis-backwards | verified_primary | 2026-06-09 | HBR | SWOT 被批 + 正确用法（框架滥用风险一手）|
| T02-S030 | https://strategizefm.com/10-common-problems-with-financial-models/ | secondary | 2026-06-09 | Strategize FM | 财务模型十大问题：over-engineering / 复杂度即风险 |
| T02-S031 | https://openai.com/index/bain/ | verified_primary | 2026-06-09 | OpenAI | OpenAI 侧 Bain 联盟说明（第二方一手） |

> **Bucket 判定说明**（按 `source_manifest.check_bucket_consistency` 规则对齐）：
> - **vendor 官方产品/公司页 = `surrogate_primary`（note 标 `vendor docs`）**：`source_verifier.py classify` 对这些 host 返回「unknown host → default secondary」，**升级到一手 tier 的唯一合规路径是 `surrogate_primary` + note 声明 surrogate 类型**（Surrogate Policy 明列「供应商/vendor docs（品牌官网）」为可接受 surrogate）。直接标 verified_primary 会触发 item-14 「manifest UPGRADE」违规。`surrogate_primary` **仍计入 item-13 first-hand tier 比率**。涉及 think-cell / GLG / AlphaSights / Third Bridge / IBISWorld / PitchBook / Statista / Alteryx / Tableau / Power BI / Qualtrics（S001/S002/S009/S010/S011/S014/S015/S016/S017/S018/S019/S024）。**mental model 类 claim 不靠 vendor 一面之词**，要 ≥2 source consensus。
> - **firm 官方 + 专业一手（auto=verified_primary）= `verified_primary`**（共 8）：McKinsey/Bain/BCG 谈自家工具（S003/S004/S005/S006）+ S&P Capital IQ（S013）+ Proskauer 律所 SEC 解读（S028）+ HBR（S029）+ OpenAI（S031）。
> - **第三方对比/新闻/论坛/评测 blog（auto=secondary，declared=secondary）= `secondary`**（共 11，declared==auto 合规）：Computerworld/baileyherb/Silverlight/PrepLounge/Deckary×2/Capitalize/Mural/Fortune/Futurism/StrategizeFM（S007/S008/S012/S020/S021/S022/S023/S025/S026/S027/S030）。
> - **黑名单合规**：`source_verifier.py` 判 **gartner.com 与 g2.com 为 `blacklisted`** → **均未进 manifest**（HARD RULE：blacklisted 不可用 surrogate 救）。Gartner / Forrester 在正文仅作「行业数据源类别名」提及，不引其站为 source。**未引用**知乎/公众号/百度/CSDN/Quora/SEO 榜单/PR 通稿/LinkedIn 帖。
> - **First-hand tier（verified_primary 8 + surrogate_primary 12）= 20/31 = 64.5%**，符合 NOT-cold 行业 ≥55% 目标。零 manifest-UPGRADE 违规（item-14 通过）。

---

## 总览（按 tier 分组）

### 必备层（≥80% 从业者用）— 6 类

| 工具/类别 | 一句话 | Decay | Sources |
|------|--------|-------|---------|
| **PowerPoint + think-cell** | 咨询母语是 deck；think-cell 是 THE 图表插件，世界前 10 所全用 | low (think-cell) | T02-S001, T02-S002, T02-S021 |
| **Excel** | 财务/运营/market sizing 建模硬通货，driver tree 落地处 | low | T02-S020, T02-S023, T02-S030 |
| **专家网络 (GLG/AlphaSights/Third Bridge/Guidepoint)** | 按小时买专家访谈做 primary research，咨询特有 | medium | T02-S009, T02-S010, T02-S011, T02-S012 |
| **行业数据库 (Capital IQ/PitchBook/IBISWorld/Statista/Euromonitor)** | 市场规模/公司财务/PE 数据的订阅源 | low | T02-S013, T02-S014, T02-S015, T02-S016 |
| **协作/沟通 (Teams/Slack/SharePoint)** | 内部协作 + 文件库，咨询基建（从业共识，未单列卡片）| low | — (ambient) |
| **分析框架工具箱 (MECE/五力/2x2/BCG 矩阵/driver tree)** | 概念工具，结构化思考的脚手架（与 Track 06 交叉）| low | T02-S029（滥用风险）|

### 场景特化层（特定子方向用）— 6 类

| 工具 | 一句话 | Decay | Sources |
|------|--------|-------|---------|
| **Tableau** | 高级数据可视化「金标准」，重数据交付/dashboard 项目 | low | T02-S018, T02-S023 |
| **Power BI** | 微软生态 BI，成本低、与 Excel/Azure 深绑 | low | T02-S019, T02-S023 |
| **Alteryx** | 数据准备/清洗/自动化 ETL，无代码连 Python/R | medium | T02-S017, T02-S023 |
| **Python / R** | 大数据/统计建模/自动化，新晋数据分析（DDD/advanced analytics 项目）| low | T02-S020 |
| **Mekko Graphics / UpSlide** | think-cell 的替代/补充：Mekko 专精 Marimekko；UpSlide 重财务报表自动化 | medium | T02-S021, T02-S022 |
| **Qualtrics / SurveyMonkey + Miro/Mural** | survey/NPS（Qualtrics）+ workshop 白板（Miro/Mural），客户调研/共创 | medium | T02-S024, T02-S025 |

### 新兴层（近 12 月，decay HIGH — intake warning h）— 5 个

| 工具 | 一句话 | Decay | Sources |
|------|--------|-------|---------|
| **McKinsey Lilli** | 内部 GenAI 知识助手：检索 10 万+ 文档、起草 research/deck，72% 员工用 | **high** | T02-S003 |
| **BCG Deckster** | GenAI 造 deck 工厂：One-Click Draft + Review This 评分，450K+ 次使用 | **high** | T02-S007, T02-S008 |
| **BCG GENE** | GPT-4o 对话 brainstorm/内容生成助手 | **high** | T02-S007 |
| **ChatGPT Enterprise (Bain/BCG/PwC 全员)** | 通用 GenAI 做研究综合/草稿，已铺到全员 | **high** | T02-S004, T02-S007, T02-S031 |
| **Microsoft 365 Copilot** | Office 内嵌 GenAI（PPT/Excel/Word/Teams），生态铺开 | **high** | T02-S007（ambient）|

---

## 必备层工具卡片

### 1. PowerPoint + think-cell（咨询交付母语 + THE 图表插件）

- **One-liner**: think-cell — PowerPoint 插件，自动化生成咨询级复杂图表（waterfall / Marimekko-Mekko / Gantt），把 PPT 从「画图工具」变成「数据驱动 deck 引擎」。咨询的交付物 90% 是 deck，think-cell 是这一层的事实标准。
- **Tier**: 必备
- **Maintainer / Owner**: think-cell GmbH（Berlin，2002 创立；co-founder Arno Schödl 曾任职 McKinsey + Microsoft Research）(evidence: [T02-S002])
- **License**: proprietary（商业订阅，floating/named license；咨询所批量采购）
- **Maturity signals**（proprietary，无 stars）:
  - Vendor 自报：35,000+ 公司使用，「**世界前 10 咨询所全部使用** think-cell」，40+ 图表类型，250+ slide 模板 (last checked: 2026-06-09) (evidence: [T02-S001])
  - 成立：2002-04（Berlin StartUp award）(evidence: [T02-S002])
  - 第三方独立证实：列为 MBB + Goldman 等标配 (evidence: [T02-S021])
- **典型使用场景**:
  - 做 waterfall（利润桥/成本拆解）、Marimekko（市场规模 × 份额二维）、Gantt（项目计划）—— 这三类原生 PPT 极难做，think-cell 一键生成且**链接 Excel 数据自动更新**。
  - action title + exhibit 占位的 ghost deck → think-cell 填图阶段。
- **不适合 / 替代方案**:
  - **Mac 用户**：think-cell 对 Mac 支持历史弱（咨询所多发 Windows）→ 替代 Mekko Graphics / Deckary。(evidence: [T02-S021])
  - **预算敏感/非每日用**：Mekko Graphics ($399/yr) 或 Deckary ($49-119/yr) 在 Marimekko/waterfall 上输出「几乎无差别」，仅高频日用者值 think-cell 全价。(evidence: [T02-S022])
- **生产案例**: McKinsey / BCG / Bain 全员级使用（vendor 客户 + 第三方均证实「前 10 所全用」）(evidence: [T02-S001, T02-S021])
- **维护者背景** (sub_skill_link): co-founder Arno Schödl（ex-McKinsey）— 解释为何产品「为咨询工作流而生」；非 Track 01 retained figure。
- **近期变化**: 2024 Cinven（PE）控股 + 新 CEO Alexander von Fritsch（公司治理变化，产品定位稳定）。
- **来源**:
  - [Primary] think-cell 官方站 (collected 2026-06-09): https://www.think-cell.com/en/ (evidence: [T02-S001])
  - [Primary] think-cell 公司史: https://www.think-cell.com/en/company/overview (evidence: [T02-S002])
  - [Secondary] Deckary 插件生态对比: https://deckary.com/blog/pillar-powerpoint-add-ins-guide (evidence: [T02-S021])
- **可信度**: high
- **Decay risk**: **low** — 24+ 月内被取代概率 <20%。咨询「deck 母语」结构性稳定；think-cell 20+ 年事实标准。唯一变量是 GenAI 造 deck（Deckster/Copilot）从下游蚕食「填图/美化」，但 think-cell 的精确图表语法短期不可替代。

### 2. Excel（财务/运营/market-sizing 建模硬通货）

- **One-liner**: Excel — 咨询所有定量分析的底座：财务模型、敏感性分析、driver tree、market sizing（人口×渗透率×单价）都在 Excel 落地。「能不能搭干净的模型」是 analyst 硬技能门槛。
- **Tier**: 必备
- **Maintainer / Owner**: Microsoft
- **License**: proprietary（Microsoft 365）
- **Maturity signals**: 行业 ubiquitous（无需 stars；从业共识 + MBB 论坛证实按项目重度用）(last checked: 2026-06-09) (evidence: [T02-S020])
- **典型使用场景**: 利润树/成本模型、商业尽调（CDD）的市场模型、敏感性/情景分析、market sizing 估算、数据透视清洗。
- **不适合 / 替代方案**:
  - **大数据量（>百万行）/ 可重复 ETL** → Alteryx / Python（Excel 卡顿、易出错）。(evidence: [T02-S023])
  - **交互式 dashboard 交付** → Tableau / Power BI（Excel 图表不够「活」）。(evidence: [T02-S023])
- **生产案例**: 全行业基础设施（每个 case 的建模层）。MBB 论坛证实「大多数咨询公司用 Excel + Python/SQL 等」(evidence: [T02-S020])
- **近期变化**: Microsoft 365 Copilot 进 Excel（GenAI 写公式/分析）—— 见新兴层；Python-in-Excel 渐普及。
- **来源**:
  - [Secondary] PrepLounge MBB 工具讨论: https://www.preplounge.com/consulting-forum/does-mbb-use-alteryx-tableau-or-power-bi-10762 (evidence: [T02-S020])
  - [Secondary] 财务模型常见问题（over-engineering 警示）: https://strategizefm.com/10-common-problems-with-financial-models/ (evidence: [T02-S030])
- **可信度**: high
- **Decay risk**: **low** — 咨询建模底座，GenAI 是增强非替代。

### 3. 专家网络（GLG / AlphaSights / Third Bridge / Guidepoint）— 咨询特有，极重要

- **One-liner**: 专家网络（expert network）— 按小时付费接通行业专家做电话访谈，是咨询/PE 做 **primary research** 的核心渠道（glossary 里的「expert call」）。GLG 最大、AlphaSights 最快、Third Bridge 重 transcript。
- **Tier**: 必备
- **Maintainer / Owner**: GLG (Gerson Lehrman Group) / AlphaSights / Third Bridge / Guidepoint / Coleman（Big 5）(evidence: [T02-S012])
- **License**: proprietary（企业订阅 + 按 call 计费）
- **Maturity signals**（vendor/landscape 自报）:
  - GLG：1M+ 专家、19 全球办公室、收入 >$400M，合规重/多市场最强 (evidence: [T02-S012])
  - AlphaSights：1,200+ 员工、9 办公室，**数小时内匹配专家**，咨询所偏好快周转 (evidence: [T02-S010, T02-S012])
  - Third Bridge：1.5M 专家、分析师主导访谈 + **transcript library** (evidence: [T02-S011])
  - Guidepoint：1M+ 专家、14 办公室，医疗/科技专精 (evidence: [T02-S012])
  - (last checked: 2026-06-09)
- **典型使用场景**:
  - 商业尽调（CDD）48h 内要对一个 niche 市场建立 primary view → 约 5-10 个行业专家 call。
  - 客户问题涉及陌生地域/技术 → 买专家访谈补 secondary research 盲区。
  - **选型分界**：合规重/多市场/复杂 → GLG；well-scoped 快周转 → AlphaSights；要可复用 transcript/分析师代访 → Third Bridge；医疗/科技垂直 → Guidepoint。(evidence: [T02-S011, T02-S012])
- **不适合 / 替代方案**:
  - 公开数据能答的问题别浪费 expert call 预算 → 先 IBISWorld/Statista/Capital IQ。
  - **合规红线**：涉上市公司 MNPI（重大非公开信息）→ 任何网络都不能用来套内幕，见避坑清单。(evidence: [T02-S028])
- **生产案例**: 咨询 + PE/对冲基金为专家网络主力客户（landscape 明示「咨询所典型评估 GLG/AlphaSights/Third Bridge」）(evidence: [T02-S012])
- **近期变化**: Tegus（2024 被 AlphaSights 收购）等整合；transcript library 模式（Tegus/Third Bridge）冲击纯 call 模式；GenAI 开始用于 expert call 转录/检索。
- **来源**:
  - [Primary] GLG 官方: https://glginsights.com/ (evidence: [T02-S009])
  - [Primary] AlphaSights 官方: https://www.alphasights.com/ (evidence: [T02-S010])
  - [Primary] Third Bridge GLG-alternatives 对比: https://www.thirdbridge.com/en-us/about-us/media/perspectives/glg-alternatives (evidence: [T02-S011])
  - [Secondary] Silverlight Big 5 landscape: https://www.silverlightresearch.com/blog/what-are-the-big-five-expert-networks (evidence: [T02-S012])
- **可信度**: high
- **Decay risk**: **medium** — 渠道结构稳定，但 vendor 整合（Tegus 并购）+ GenAI 转录/检索 + transcript-library 替代 call 在重塑形态（12-24 月）。

### 4. 行业数据库（Capital IQ / PitchBook / IBISWorld / Statista / Euromonitor）

- **One-liner**: 付费数据/情报源 — secondary research 的弹药库：公司财务（Capital IQ）、PE/VC/M&A（PitchBook）、行业市场报告（IBISWorld）、聚合统计（Statista）、消费/全球市场（Euromonitor Passport）。
- **Tier**: 必备（整类；具体订哪几个按 firm/项目）
- **Maintainer / Owner**: S&P Global（Capital IQ）/ Morningstar（PitchBook）/ IBISWorld / Statista / Euromonitor International
- **License**: proprietary（高价企业订阅，常按 seat）
- **Maturity signals**:
  - Capital IQ：公司财务 + earnings transcript + 筛选器（S&P 一手）(evidence: [T02-S013])
  - IBISWorld：700+ US + 60 全球行业报告，每篇含市场分割/竞争/展望 (evidence: [T02-S014])
  - PitchBook：私募市场全周期（VC/PE/M&A）(evidence: [T02-S015])
  - Statista：聚合数千来源统计/图表 (evidence: [T02-S016])
  - (last checked: 2026-06-09)
- **典型使用场景**:
  - market sizing 找锚点数 → IBISWorld / Statista / Euromonitor。
  - 标的/竞品财务 + 可比公司 → Capital IQ。
  - PE 尽调看交易/估值/投资人 → PitchBook。
- **不适合 / 替代方案**:
  - niche/前沿市场无现成报告 → 回退专家网络（primary）。
  - 数字别照搬：第三方估计有口径差异，**交叉验证**多源（数据 caveat，对应 intake warning）。
- **生产案例**: 咨询/投行/PE 标配研究订阅（行业 ubiquitous）。
- **近期变化**: 各家叠 AI 检索/摘要（如 Capital IQ Pro）；GenAI 改变「查数」工作流。
- **来源**:
  - [Primary] S&P Capital IQ: https://www.spglobal.com/marketintelligence/en/ (evidence: [T02-S013])
  - [Primary] IBISWorld: https://www.ibisworld.com/ (evidence: [T02-S014])
  - [Primary] PitchBook: https://pitchbook.com/ (evidence: [T02-S015])
  - [Primary] Statista: https://www.statista.com/ (evidence: [T02-S016])
- **可信度**: high
- **Decay risk**: **low** — 数据源是研究基建（厂商可能换名/并购但功能稳定）。
- **注**: **Gartner / Forrester**（IT/科技行业研究）是同类常用数据源，但其官网经 `source_verifier.py` 判为 **blacklisted**（G2/Capterra 式评测站归类），故**不入 manifest**，仅在此作类别名提及——需要 Gartner 数据时引行业一手或客户许可的报告，勿引 gartner.com 作 source。

### 5. 分析框架工具箱（概念工具 — 与 Track 06 交叉）

> **本 track 只做「工具化清单 + 何时用 + 滥用风险」**；框架的定义/谱系深度在 Track 06 glossary + canon，synthesis 整合。咨询把框架当**结构化思考的脚手架**，不是答案。

| 框架工具 | 适用场景（何时拿出来） | 被滥用 / 失效风险 |
|---------|---------------------|------------------|
| **MECE 树 / issue tree** | 任何问题拆解的底层语法：把核心问题 MECE 拆成可验证子问题 | 拆桶重叠又漏项；做成发散 mind map 没验证纪律 |
| **Porter 五力** | 判断**行业**盈利结构/进入吸引力 | 套到单公司战略/快变市场；只填表不推 so-what (evidence: [T02-S029] 同源批判逻辑) |
| **价值链 (value chain)** | 找企业内部竞争优势来源（primary/support 活动）| 当成供应链流程图 |
| **2x2 矩阵** | 快速结构化/优先级排序（2 轴 4 象限）| 把任意东西硬塞 2x2 凑「框架感」 |
| **BCG 增长-份额矩阵** | 多业务组合的现金流配置 | 静态、忽略协同/能力，机械套四象限 |
| **driver tree / profit tree** | 把利润/KPI 拆到可干预驱动因子（量×价−成本）| 拆到财务报表层就停，没到可操作杠杆 |
| **7S / 3C / 4P / PESTEL / Ansoff** | 组织诊断 / 市场扫描 / 营销 / 宏观 / 增长策略 | 当 checklist 填，无洞见 |
| **SWOT** | 入门级速览（资深人很少单用）| **业内视为低阶/无洞见**；HBR 教「倒着做」才有用 (evidence: [T02-S029]) |

- **Tier**: 必备（概念工具层）
- **核心原则**: **框架只是脚手架，必须推出 so-what 才有价值**。「套框架剧场（frameworks-as-theater）」是行业自我批判（Mintzberg / Matthew Stewart《The Management Myth》，见 Track 06）。
- **来源**: [Primary] HBR SWOT 批判: https://hbr.org/2021/02/are-you-doing-the-swot-analysis-backwards (evidence: [T02-S029])；其余框架定义见 Track 06 glossary (T06-S001/S002/S006/S020/S022)。
- **Decay risk**: **low** — 方法论内核稳定 40+ 年。

---

## 场景特化层工具卡片

### 6. Tableau（数据可视化「金标准」）

- **One-liner**: Tableau — 高级交互式数据可视化/dashboard 工具，重数据型项目（运营分析、客户分群、KPI 监控）的交付层。
- **Tier**: 场景特化
- **Maintainer / Owner**: Tableau（Salesforce 旗下）
- **License**: proprietary（Creator/Explorer/Viewer 分级订阅）
- **Maturity signals**: 第三方公认「数据可视化金标准」(last checked 2026-06-09) (evidence: [T02-S023])；MBB 按项目使用 (evidence: [T02-S020])
- **典型使用场景**: 客户要可交互 dashboard（非静态 PPT）；探索大数据集找模式；运营/数字化项目的数据呈现。
- **不适合 / 替代方案**:
  - 客户**只要 PPT 决策 deck** → 别上 Tableau（见避坑：炫技但客户只看 deck）。
  - 微软重生态 + 成本敏感 → Power BI。(evidence: [T02-S023])
  - 上游数据脏/要 ETL → 先 Alteryx 再 Tableau。(evidence: [T02-S023])
- **生产案例**: MBB 在数据重项目用（论坛证实「按项目用 Tableau/Power BI」）(evidence: [T02-S020])
- **来源**: [Primary] Tableau 官方: https://www.tableau.com/ (evidence: [T02-S018])；[Secondary] Capitalize 三工具分工: https://capitalizeconsulting.com/comparing-alteryx-tableau-and-power-bi/ (evidence: [T02-S023])
- **可信度**: high
- **Decay risk**: **low**。

### 7. Power BI（微软生态 BI）

- **One-liner**: Power BI — 微软商业智能工具，与 Excel/SQL Server/Azure/Teams 深度集成，成本低于 Tableau，企业部署友好。
- **Tier**: 场景特化
- **Maintainer / Owner**: Microsoft
- **License**: proprietary（Power BI Pro / Premium）
- **Maturity signals**: 与 Microsoft 生态无缝、支持 Python/R 脚本，企业采用广 (last checked 2026-06-09) (evidence: [T02-S019, T02-S023])
- **典型使用场景**: 客户已在 Microsoft 365 生态；要可持续维护的企业 dashboard；预算/IT 约束下的 BI。
- **不适合 / 替代方案**: 极致可视化美学/探索性分析 Tableau 略强；纯一次性 deck 用 Excel+think-cell 即可。
- **生产案例**: MBB + Big Four 按项目用 (evidence: [T02-S020])
- **来源**: [Primary] Power BI 官方: https://powerbi.microsoft.com/ (evidence: [T02-S019])；[Secondary] 同 T02-S023。
- **可信度**: high
- **Decay risk**: **low**。

### 8. Alteryx（数据准备/自动化 ETL）

- **One-liner**: Alteryx — 无代码数据准备/清洗/混合/自动化平台，连 Tableau/Power BI 做可视化、连 Python/R 做高级分析；解决「Excel 处理不动的脏数据」。
- **Tier**: 场景特化
- **Maintainer / Owner**: Alteryx, Inc.
- **License**: proprietary（Designer 按 seat，较贵）
- **Maturity signals**: 数据准备/ETL 主流，平滑连第三方可视化 + Python/R (last checked 2026-06-09) (evidence: [T02-S017, T02-S023])
- **典型使用场景**: 多源数据合并清洗（>Excel 量级）；可重复的数据 pipeline；advanced analytics 前的数据工程。
- **不适合 / 替代方案**:
  - 一次性小数据 → Excel 足够（Alteryx overkill）。
  - 团队有工程能力/要灵活度 → Python（pandas）。(evidence: [T02-S020])
- **生产案例**: MBB 数据重 workstream（论坛点名）(evidence: [T02-S020])
- **来源**: [Primary] Alteryx 官方: https://www.alteryx.com/ (evidence: [T02-S017])；[Secondary] 同 T02-S023。
- **可信度**: high
- **Decay risk**: **medium** — 数据准备赛道受 Python/GenAI code-gen + 云数据平台挤压。

### 9. Python / R（新晋数据分析）

- **One-liner**: Python（+R）— 大数据/统计建模/自动化/ML 的编程层，咨询「advanced analytics / data science」项目的硬核工具；近年从 MBB 数据团队扩散到主流。
- **Tier**: 场景特化
- **Maintainer / Owner**: open source（Python Software Foundation / R Foundation）
- **License**: **open**（唯一开源条目；PSF License / GPL）
- **Maturity signals**: MBB 普遍用（论坛证实「大多数咨询公司用 Python/SQL 等」）(last checked 2026-06-09) (evidence: [T02-S020])
- **典型使用场景**: 数百万行数据处理、统计/预测建模、爬虫/自动化、ML POC；超出 Excel/Alteryx 能力时。
- **不适合 / 替代方案**:
  - 纯 deck 型战略项目（无大数据）→ Excel 即可，别为炫技上 Python。
  - 团队无编程能力 + 要快 → Alteryx（无代码）。
- **生产案例**: MBB advanced analytics / DDD 实践（论坛点名）(evidence: [T02-S020])
- **来源**: [Secondary] PrepLounge MBB 工具讨论: https://www.preplounge.com/consulting-forum/does-mbb-use-alteryx-tableau-or-power-bi-10762 (evidence: [T02-S020])
- **可信度**: medium-high（开源 ubiquity 公认；具体 MBB 渗透率为论坛/从业观察）
- **Decay risk**: **low** — 编程层基础设施稳定。

### 10. Mekko Graphics / UpSlide（PowerPoint 插件替代/补充）

- **One-liner**: think-cell 之外的 PPT 插件：**Mekko Graphics** 专精 Marimekko（市场规模×份额，咨询常用），**UpSlide** 重 Excel/Word/PPT 跨件财务报表自动化。
- **Tier**: 场景特化
- **Maintainer / Owner**: Mekko Graphics（insightsoftware 旗下，2007 创立）/ UpSlide
- **License**: proprietary（Mekko ~$399/yr）
- **Maturity signals**: Mekko 2007 起、Marimekko 专精、$399/yr ($299 续费)；UpSlide 宣称例行任务快 5×、月省 12h (last checked 2026-06-09) (evidence: [T02-S022, T02-S021])
- **典型使用场景**: Mac 团队（think-cell 弱）；预算敏感/非每日做图；UpSlide 适合金融/PE 重财务文档自动化的团队。
- **不适合 / 替代方案**: 已标准化 think-cell 的所/重度日用者 → think-cell 仍是事实标准。
- **生产案例**: insightsoftware 客户 + Deckary 实测「输出与 think-cell 几乎无差别」(evidence: [T02-S022])
- **来源**: [Secondary] Deckary 插件生态: https://deckary.com/blog/pillar-powerpoint-add-ins-guide (evidence: [T02-S021])；[Secondary] Mekko review: https://deckary.com/blog/mekko-graphics-review (evidence: [T02-S022])
- **可信度**: medium（vendor + 评测 blog）
- **Decay risk**: **medium** — 同受 GenAI 造 deck 挤压。

### 11. Qualtrics / SurveyMonkey + Miro / Mural（调研 + workshop 协作）

- **One-liner**: 客户调研与共创层：**Qualtrics**（企业级 survey/NPS/体验）、**SurveyMonkey**（轻量 survey）做量化调研；**Miro / Mural**（在线白板）做 workshop / journey mapping / 利益相关方共创。
- **Tier**: 场景特化
- **Maintainer / Owner**: Qualtrics / SurveyMonkey（Momentive）/ Miro / Mural
- **License**: proprietary（订阅）
- **Maturity signals**: Qualtrics 可收 NPS/定价/市场调研 (evidence: [T02-S024])；Miro/Mural 为咨询 workshop top 白板、Mural 有咨询专用模板 (last checked 2026-06-09) (evidence: [T02-S025])
- **典型使用场景**: 客户员工/消费者调研（Qualtrics NPS）；远程/混合 workshop 与客户共创战略（Miro/Mural）；定性发现可视化归类。
- **不适合 / 替代方案**: 小样本内部投票 → SurveyMonkey/Teams polls 即可，别上 Qualtrics 全套；面对面 workshop 白板/便利贴仍可用。
- **生产案例**: Mural 官方载咨询 workshop 用例 + 客户工作坊模板 (evidence: [T02-S025])
- **来源**: [Primary] Qualtrics 官方: https://www.qualtrics.com/ (evidence: [T02-S024])；[Secondary] Mural 咨询 workshop: https://www.mural.co/blog/tools-for-consulting-workshops (evidence: [T02-S025])
- **可信度**: medium-high
- **Decay risk**: **medium** — 协作/调研 SaaS 竞争激烈，工具可替换。

---

## 新兴层工具卡片（decay HIGH — 近 12 月最大变量）

> **intake warning (h)**：GenAI 对咨询工具栈的冲击是本行近一年最大变量，**对初级分析师工作冲击直接**（research / 做 deck / market sizing 正是 analyst 金字塔底层活）。全部标 `stability: experimental` 级别的快速演化，**6-12 月后形态可能大变**。

### 12. McKinsey Lilli（内部 GenAI 知识助手）

- **One-liner**: Lilli — McKinsey 自建 GenAI 平台，检索 10 万+ 内部文档/专家知识，起草 research、综合洞见、辅助做 deck；目标是把「找知识 + 综合」从天级压到分钟级。
- **Tier**: 新兴（firm 内部已规模化，但对行业是新形态）
- **Maintainer / Owner**: McKinsey & Company（内部）
- **License**: proprietary（内部，不对外）
- **Maturity signals**（firm 官方一手）:
  - **72% 员工活跃**在平台上；**500K+ prompts/月**（增长中）；报告**最高 ~30% 搜索/综合时间节省** (last checked 2026-06-09) (evidence: [T02-S003])
  - 2023-07 全员铺开（WebSearch 证实 ~70%+ of 45,000 顾问、约 17×/周使用）
- **典型使用场景**: 项目启动期检索 firm 既往相关 case/专家；market/行业 research 初稿；综合多文档要点。
- **不适合 / 替代方案 + 风险**:
  - **会幻觉**：Track 06 记录 Lilli 曾「引用不存在的法规」→ 输出**必须人工核验**才进 deck（见避坑清单）。(交叉 [T06-S021])
  - 客户敏感/保密语境：内部工具不能外泄客户数据。
- **生产案例**: McKinsey 全员（官方页自述）(evidence: [T02-S003])
- **近期变化**: 持续迭代（接入更多内部知识 + agent 化）；是「GenAI 重塑 leverage model」论的核心样本。
- **来源**: [Primary] McKinsey Lilli 官方页: https://www.mckinsey.com/capabilities/tech-and-ai/how-we-help-clients/rewiring-the-way-mckinsey-works-with-lilli (evidence: [T02-S003])
- **可信度**: high（firm 一手；但采用率/节省%为 firm 自报，标 caveat）
- **Decay risk**: **HIGH** — 12 月内功能/形态显著变化概率 >40%（GenAI 演进 + agent 化）。

### 13. BCG Deckster（GenAI 造 deck 工厂）

- **One-liner**: Deckster — BCG 内部 GenAI 造/改 slide 工具（GPT-4o + BCG 知识库 + 800-900 个 firm 模板）：「One-Click Draft」吃 outline/ChatGPT prompt 出成品 slide；「Review This」按 BCG 设计 rubric（MECE 结构/标题清晰/图表卫生）打分 + 行内建议——把资深 associate 反馈变成「always-on coach」。
- **Tier**: 新兴
- **Maintainer / Owner**: BCG（内部，BCG X 体系）(evidence: [T02-S006])
- **License**: proprietary（内部）
- **Maturity signals**:
  - 2024-03 全球上线（2023 起 beta）；**450K+ 次造/改 slide**，firm 最快扩张内部 app 之一 (last checked 2026-06-09) (evidence: [T02-S007])
  - 运行于 GPT-4o + 800-900 个 firm-approved 模板 (evidence: [T02-S008])
- **典型使用场景**: outline → 一键出 BCG 品牌格式 slide；用 Review This 自检 slide 质量（替代部分 EM/AP 的格式反馈）。
- **不适合 / 替代方案 + 风险**: 战略 storyline 的 so-what 跳跃仍需人脑；自动美化 ≠ 自动产生洞见；输出需核验数据/逻辑。
- **生产案例**: BCG 全员（高管访谈披露 450K+ 次）(evidence: [T02-S007])
- **近期变化**: 与 ChatGPT Enterprise（2023-10 全员）+ 6,000+ 自建 GPT 组成 BCG GenAI 栈 (evidence: [T02-S007])
- **来源**: [Secondary] Computerworld BCG 高管访谈: https://www.computerworld.com/article/3491334/... (evidence: [T02-S007])；[Secondary] Deckster 设计者拆解: https://baileyherb.com/deckster (evidence: [T02-S008])；[Primary] BCG X: https://www.bcg.com/x (evidence: [T02-S006])
- **可信度**: high（多源 + 设计者一手）
- **Decay risk**: **HIGH**。

### 14. BCG GENE（GPT-4o 对话助手）

- **One-liner**: GENE — BCG 的 GPT-4o 对话 AI（刻意「机器人声线」），用于 brainstorm、内容生成、团队互动，可调语气；起于「Imagine This」podcast 共同主持，后扩为通用助手。
- **Tier**: 新兴
- **Maintainer / Owner**: BCG（内部）
- **License**: proprietary
- **Maturity signals**: GPT-4o；记忆库装 BCG 顶级分析师的 GenAI research/洞见 (last checked 2026-06-09) (evidence: [T02-S007])
- **典型使用场景**: 头脑风暴对话伙伴、内容初稿、团队协作问答。
- **不适合 / 替代方案**: 通用对话能力与 ChatGPT 重叠；定位偏「品牌化内部 chatbot」。
- **生产案例**: BCG 内部（高管访谈提及）(evidence: [T02-S007])
- **来源**: [Secondary] 同 T02-S007。
- **可信度**: medium-high
- **Decay risk**: **HIGH**。

### 15. ChatGPT Enterprise（Bain / BCG / PwC 全员铺开 + 通用 GenAI 综合）

- **One-liner**: 通用 GenAI（ChatGPT Enterprise / Claude）做研究综合、市场估算辅助、草稿生成——已从「个人偷偷用」变成 firm 全员正式部署。Bain×OpenAI、BCG ChatGPT Enterprise 全员、PwC 大规模采用是标志。
- **Tier**: 新兴
- **Maintainer / Owner**: OpenAI（Bain/BCG/PwC 部署）；Anthropic（Claude，企业用于长文档/结构化综合/财务分析）
- **License**: proprietary（企业订阅）
- **Maturity signals**:
  - **Bain×OpenAI**：2022 起合作、2023 初全球联盟、2024-10-17 扩展（成立 OpenAI Center of Excellence，先做零售 + 医疗生命科学），ChatGPT Enterprise 全员可用 (evidence: [T02-S004, T02-S005, T02-S031])
  - **BCG**：ChatGPT Enterprise 全员（2023-10）+ 6,000+ 自建 GPT (evidence: [T02-S007])
  - **PwC**：被报道为「OpenAI 最大企业客户」(WebSearch 佐证)
  - (last checked 2026-06-09)
- **典型使用场景**: 多文档研究综合、初稿/邮件/纪要、market sizing 假设脚手架、代码/公式辅助；Claude 偏长文档/尽调/财务结构化综合。
- **不适合 / 替代方案 + 风险**: **幻觉进 deck** 是已发生的真实事故（见避坑：Deloitte 退款案）；客户保密数据不可投喂非企业版/未授权模型。
- **生产案例**: Bain 13,000 顾问（WebSearch）/ BCG 全员 / PwC 大规模（多源）(evidence: [T02-S004, T02-S007])
- **来源**: [Primary] Bain×OpenAI 官方稿: https://www.bain.com/about/media-center/press-releases/2024/... (evidence: [T02-S004])；[Primary] OpenAI 侧: https://openai.com/index/bain/ (evidence: [T02-S031])；[Secondary] BCG: T02-S007。
- **可信度**: high
- **Decay risk**: **HIGH** — 模型/部署/价格月级变动。

### 16. Microsoft 365 Copilot（Office 内嵌 GenAI，ambient）

- **One-liner**: Microsoft 365 Copilot — 在 PPT/Excel/Word/Teams 内嵌 GenAI（生成 slide 草稿、Excel 公式/分析、会议纪要），随 Office 生态自然渗透咨询日常。
- **Tier**: 新兴（ambient，未单独深挖）
- **Maintainer / Owner**: Microsoft
- **License**: proprietary（M365 Copilot 附加订阅）
- **Maturity signals**: 早期赢家集中在金融/咨询；与咨询 Office-centric 工作流天然契合 (last checked 2026-06-09) (evidence: [T02-S007] 同 GenAI 栈语境)
- **典型使用场景**: Excel 内 GenAI 分析、PPT 草稿、Teams 会议总结、Word 报告起草。
- **不适合 / 替代方案**: 与 firm 自建工具（Lilli/Deckster）功能部分重叠；同样有幻觉/保密风险。
- **来源**: [Secondary] GenAI 栈语境 T02-S007；通用采用见 WebSearch（Copilot 早期赢家在咨询/金融）。
- **可信度**: medium（行业方向明确，具体咨询渗透率未单独核实）
- **Decay risk**: **HIGH**。

---

## 选型决策树

> 7 节点（在 5-10 区间）。从「你当前的核心任务是什么」分支。每节点挂 evidence。

### 决策树：你这一步的核心任务是什么？

#### Branch 1: 我要做**交付物 deck**（咨询最高频任务）
→ **推荐**：PowerPoint + **think-cell**（waterfall/Marimekko/Gantt 一键 + Excel 链接），事实标准、世界前 10 所全用。(evidence: [T02-S001])
→ **Mac / 预算敏感**：Mekko Graphics 或 Deckary（输出几乎无差别，价格 1/3）。(evidence: [T02-S022])
→ **想 GenAI 加速初稿**：BCG 内部用 Deckster（One-Click Draft）；外部团队用 ChatGPT/Copilot 出 outline，**但成品必须人工核验**（见避坑）。(evidence: [T02-S007])
→ **不推荐**：上来做 Tableau 炫酷 dashboard——若客户只要决策 deck，是 over-engineering。(evidence: [T02-S023])

#### Branch 2: 我要**建模/算数**（财务模型 / market sizing / driver tree）
→ **推荐**：Excel（硬通货），driver tree + 敏感性分析的落地处。(evidence: [T02-S020])
→ **数据量 >Excel 处理能力 / 要可重复 pipeline**：
##### Branch 2a: 团队无编程能力 + 要快 → **Alteryx**（无代码 ETL）。(evidence: [T02-S023])
##### Branch 2b: 团队有工程能力 / 要灵活 + ML → **Python/R**。(evidence: [T02-S020])
→ **不推荐**：把 Excel 模型 over-engineer 成谁都看不懂的巨兽（复杂度=模型风险，客户要答案不要复杂度）。(evidence: [T02-S030])

#### Branch 3: 我要**做 primary research**（公开数据答不出的洞见）
→ **推荐**：专家网络。**合规重/多市场/复杂** → GLG；**well-scoped 快周转** → AlphaSights；**要可复用 transcript/分析师代访** → Third Bridge；**医疗/科技垂直** → Guidepoint。(evidence: [T02-S011, T02-S012])
→ **合规红线**：涉上市公司，专家不得透露 MNPI（重大非公开信息）——任何 call 都不能用来套内幕，否则触 SEC 内幕交易（见避坑）。(evidence: [T02-S028])

#### Branch 4: 我要**找市场规模 / 公司财务 / 行业数据**（secondary research）
→ **市场规模/行业报告** → IBISWorld / Statista / Euromonitor。(evidence: [T02-S014, T02-S016])
→ **公司财务 + 可比公司 + earnings** → Capital IQ。(evidence: [T02-S013])
→ **PE/VC/M&A 交易与估值** → PitchBook。(evidence: [T02-S015])
→ **不推荐**：niche/前沿市场没现成报告还硬等 secondary → 回退 Branch 3 专家网络。

#### Branch 5: 我要**交互式 dashboard / 数据呈现**（非静态 deck）
→ **微软生态 + 成本敏感** → Power BI。(evidence: [T02-S019, T02-S023])
→ **极致可视化 + 探索性分析** → Tableau（金标准）。(evidence: [T02-S018, T02-S023])
→ **上游数据脏** → 先 Alteryx 清洗再可视化。(evidence: [T02-S023])
→ **判断前提**：先确认客户**真要 dashboard** 而非 PPT；否则别上（见避坑）。

#### Branch 6: 我要**做客户调研 / workshop 共创**
→ **量化调研 / NPS** → Qualtrics（企业级）/ SurveyMonkey（轻量）。(evidence: [T02-S024])
→ **远程/混合 workshop / journey mapping** → Miro / Mural（Mural 有咨询专用模板）。(evidence: [T02-S025])

#### Branch 7: 我要**结构化思考一个商业问题**（方法论层）
→ **拆问题** → MECE issue tree（底层语法）；**行业盈利结构** → 五力；**内部优势来源** → 价值链；**优先级** → 2x2；**利润拆解** → driver tree。
→ **铁律**：框架是脚手架，**必须推出 so-what**；SWOT 仅入门级速览，资深人很少单用（HBR 教倒着做）。(evidence: [T02-S029])

---

## 避坑清单（≥5，实际 8）

- ❌ **不要把 GenAI 输出（Lilli/ChatGPT/Copilot）不核验就放进 deck**：会幻觉。Deloitte 因 AI 生成的**伪造学术引用 + 假法院判词**，被加拿大 ~$1.6M 报告曝光、澳洲 $291K 报告**退款**；McKinsey Lilli 曾引用不存在的法规。**AI 的数字/引用/claim 必须落到可核验原始来源**才能出门。(evidence: [T02-S026, T02-S027], 交叉 [T06-S021])
- ❌ **不要用专家网络 call 套上市公司 MNPI（重大非公开信息）**：触发 SEC/FCA 内幕交易，单次失误罚款可达数百万 + 长审计。SEC Risk Alert 明确要求 log calls / 审 call notes / 监控相关行业交易。合规是专家网络使用的红线。(evidence: [T02-S028])
- ❌ **不要 over-engineer Excel 模型**：复杂≠专业。PwC 建模准则强调 simplicity；过度复杂公式制造最严重的电子表格陷阱，且别人无法核验/操作。**客户要的是答案，不是一座没人看得懂的模型巨兽**。(evidence: [T02-S030])
- ❌ **不要用 Tableau/Power BI 炫技但客户只要 PPT**：数据重项目才上 BI；若交付物是决策 deck，硬塞交互 dashboard 是 over-engineering，浪费时间还偏离客户需求——先确认客户真要 dashboard。(evidence: [T02-S023])
- ❌ **不要把 framework 当答案直接套出来交差**：五力/2x2/SWOT 是**脚手架不是结论**。只填框架不推 so-what = 「frameworks-as-theater 套框架剧场」，是行业最大破绽（Mintzberg / Matthew Stewart 批判）。SWOT 尤其被业内视为入门级，单用即露怯，HBR 教「倒着做」才有用。(evidence: [T02-S029])
- ❌ **不要让 Mac/think-cell 兼容问题拖死交付**：think-cell 对 Mac 历史支持弱；Mac 团队提前换 Mekko Graphics/Deckary，别到交付前夜才发现图做不出来。(evidence: [T02-S021, T02-S022])
- ❌ **不要把公开数据能答的问题浪费在 expert call**：专家访谈贵且有合规开销；先穷尽 IBISWorld/Statista/Capital IQ secondary，再用专家网络补盲区。(evidence: [T02-S012, T02-S014])
- ❌ **不要把第三方数据库数字当 ground truth 照搬**：IBISWorld/Statista/Euromonitor 口径不同，估计有差异；market sizing 关键数要**多源交叉验证**并标来源（对应 intake 数字 caveat warning）。(evidence: [T02-S014, T02-S016])

---

## Phase 2 提炼提示

### 反复出现 ≥3 source 都强调的「工具选型原则」（候选 playbook 规则）

- **「deck 是母语，think-cell 是事实标准」**：交付物默认 PowerPoint + think-cell，工具服务于「一页一结论 + action title」的故事线，不是反过来（出现于 T02-S001 / T02-S021 / T02-S022）。
- **「工具匹配交付物，别 over-engineer」**：客户要决策 deck 就别上 Tableau/复杂模型；复杂度是风险不是专业（出现于 T02-S023 / T02-S030 + 避坑共识）。
- **「primary 用专家网络、secondary 用数据库，按需分层，合规优先」**：research 工具按「公开能否答」分层，专家网络是 last-mile，但 MNPI 是不可越的红线（出现于 T02-S012 / T02-S028 / T02-S011）。
- **「GenAI 加速但人是 last verifier」**：GenAI 可做初稿/检索/综合，但**幻觉必须人工核验**才进交付物——这是 GenAI 时代的新铁律（出现于 T02-S003 / T02-S026 / T02-S027）。

### 显著的工具流派分裂（候选 智识谱系条目）

- **厚框架派（framework-first）vs 薄框架派（answer-first / first-principles）**：传统咨询以经典框架（五力/BCG 矩阵/7S）为脚手架 vs 批判派（Mintzberg planning-school 批判、Matthew Stewart《The Management Myth》「frameworks-as-theater」）主张框架是表演、真洞见靠 first-principles。**与 Track 01 figures / Track 06 glossary 强关联**——SWOT 被贬为入门级是这条分裂的具体投影。(evidence: [T02-S029])
- **传统手工栈 vs GenAI 增强栈**：think-cell 手做精确图表 + Excel 手搭模型 + 人读文档综合 ⇄ Deckster 一键造 deck + Lilli 检索综合 + ChatGPT 初稿。**正在发生的范式扰动**，直接冲击 leverage model 底层（analyst 的 research+做 deck 被自动化）。

### 新兴工具信号

- **当前活跃/上升的新工具数**: 5（Lilli / Deckster / GENE / ChatGPT Enterprise 全员 / M365 Copilot），全部 GenAI 系。
- **出现 → 主流速度估计**: **极快，~12-18 个月**。Deckster 2024-03 上线到 450K+ 次使用、Lilli 2023-07 到 72% 员工活跃——firm 内部「出现即规模化」。但**对行业整体（中小所/独立顾问）的渗透仍在早期**，形态 6-12 月可能大变。
- **decay 强度**: 新兴层**全部 HIGH**（12 月内显著变化概率 >40%）；必备层 think-cell/Excel/数据库为 low；专家网络 medium（vendor 整合 + GenAI 转录）。

### 冷僻 / 信号薄弱

- **必备层 ≥3**？✅ 6 类（远超）。**新兴层 ≥2**？✅ 5 个。**场景特化 ≥5**？✅ 6 类。
- **非冷僻**：工具栈公开材料丰富，first-hand tier（verified_primary 8 + surrogate_primary 12）= 20/31 = 64.5%。**注**：vendor 官方站按 manifest 规则标 `surrogate_primary`（非 verified_primary），但仍属一手 tier；synthesis 引用 vendor 自报数据时按 surrogate 处理 + 标 caveat。
- **唯一结构性 caveat**：咨询工具几乎全 **proprietary 闭源**，无 GitHub stars/commit 可锚 → maturity 靠 vendor 自报 + firm 官方采用率（已在「维度特殊说明」标注，非调研失败，是行业特征）。GenAI 内部工具（Lilli/Deckster）的采用率/时间节省%为 **firm 自报**，synthesis 引用须标 caveat。
- **数字 caveat**（对应 intake）：think-cell「前 10 所全用」、Lilli「72%/30% 节省」、Deckster「450K 次」、专家网络规模数 —— 均 vendor/firm 自报或第三方估计，引用挂 source_id + 标「官方自报/约/业内估计」。

---

## 质量自检

- [x] 候选数 ≥ 20？—— **探索 ~30+ 候选**（含框架工具箱 8 个 + 软件 22+），retained 16 张卡片（含合并类目）。
- [x] 三层都有内容？必备 ≥3（6）/ 场景特化 ≥5（6）/ 新兴 ≥2（5）✅
- [x] 每个工具有 `last_checked` + ≥1 maturity signal 带日期？✅（proprietary 用 vendor 自报数 + firm 采用率 + 成立年，全标 2026-06-09）
- [x] 选型决策树 5-10 节点？—— **7 个主 branch + 子分支**，每节点挂 evidence ✅
- [x] 避坑清单 ≥5？—— **8 条** ✅
- [x] 一手来源 ≥50%？—— first-hand tier (verified_primary 8 + surrogate_primary 12) **20/31 = 64.5%** ✅
- [x] Decay risk 每个工具都标？✅（新兴全 HIGH / think-cell·Excel·数据库 low / 专家网络·BI·插件 medium）
- [x] Phase 2 接口填了？—— 选型原则 4 / 流派分裂 2 / 新兴信号 / 冷僻自检 全填 ✅
- [x] Source Manifest 在最前，黑名单合规（gartner.com / g2.com 判 blacklisted，**未进表**；无知乎/公众号/百度/CSDN/Quora/SEO 榜单/PR 通稿/LinkedIn）✅
- [x] Bucket 一致性（item-14）：vendor 站全部 `surrogate_primary` + note 标 `vendor docs`，零 manifest-UPGRADE 违规 ✅
