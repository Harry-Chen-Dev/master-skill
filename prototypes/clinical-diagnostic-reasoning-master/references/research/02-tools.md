# Track 02 — Tools: 临床诊断思维 (Clinical Diagnostic Reasoning) — 诊断辅助器具与框架

> locale=global (en-primary canon) | profile=practitioner | focus=comprehensive | research_date: 2026-06-06
> RESUMING run: 01-figures + 04-canon 已完成, 本 track 接力。Seed 来自 04-canon 点名的工具/概念 + 01-figures 的 AI 研究人。
> **本行 "工具" 定义**: 临床医生**用来推理的** 辅助器具 / 仪器 / 框架 (决策规则、概率工具、DDx 生成器、知识库、AI 助手、思维/教学框架), **不是** 化验机器或影像设备。
> 衰减结构特殊: 决策规则/概率工具/思维框架 = 极稳 (decay low, 几十年不变); AI 辅助诊断层 = **最高 decay (high)**, 数字/产品 6-12 月即变, 全部挂 last_checked + 「截至 research_date」caveat。
> 数字纪律 (intake.warnings): 每个 %/比率/LR 必挂 source_id 或 caveat (估计/约/业内); 诊断错误率与 AI 性能数字一律 contested, 不写成铁事实; AI alone 悖论与 gestalt-vs-rule 论战双向保留, 不软化任一方。
> 网络环境: WebFetch 受限, 验证经 WebSearch 结果页 + 离线 classifier; `last_checked` = 当日经搜索确认 URL 仍被索引/存在。

## Source Manifest

| source_id | url | bucket | last_checked | author/host | one-line note |
|-----------|-----|--------|--------------|-------------|---------------|
| T02-S001 | https://en.wikipedia.org/wiki/Wells_score_(pulmonary_embolism) | secondary | 2026-06-06 | Wikipedia | Wells PE 评分结构/分层元数据 |
| T02-S002 | https://mdcalc.scholasticahq.com/article/160874-updated-review-of-the-wells-criteria-for-pulmonary-embolism | secondary | 2026-06-06 | MDCalc Evidence to Action | Wells PE 更新综述 (期刊化) |
| T02-S003 | https://journalfeed.org/article-a-day/2016/wells-score-or-gestalt-before-perc/ | secondary | 2026-06-06 | JournalFeed | gestalt vs Wells before PERC 评议 |
| T02-S004 | https://www.researchgate.net/publication/235715109 | secondary | 2026-06-06 | Penaloza et al (RG) | gestalt vs Wells vs Geneva 验前概率对比 |
| T02-S005 | https://www.mdcalc.com/about-us | secondary | 2026-06-06 | MDCalc | 工具站官方 — 80%+ 美国临床医生用 (vendor) |
| T02-S006 | https://en.wikipedia.org/wiki/MDCalc | secondary | 2026-06-06 | Wikipedia | MDCalc 元数据/规模 |
| T02-S007 | https://pmc.ncbi.nlm.nih.gov/articles/PMC8369374/ | verified_primary | 2026-06-06 | JMIR/PMC | web 决策计算器使用模式实证 (CHA2DS2-VASc 等最常用) |
| T02-S008 | https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4902203/ | verified_primary | 2026-06-06 | PMC | Fagan nomogram 演化 commentary (1975 起源) |
| T02-S009 | https://pmc.ncbi.nlm.nih.gov/articles/PMC1495095/ | verified_primary | 2026-06-06 | McGee (JGIM 2002) | Simplifying Likelihood Ratios 全文 (=T04-S021) |
| T02-S010 | https://jamaevidence.mhmedical.com/book.aspx?bookId=845 | secondary | 2026-06-06 | JAMAevidence (McGraw Hill) | Rational Clinical Examination 书平台 (vendor docs) |
| T02-S011 | https://jamanetwork.com/collections/6257/the-rational-clinical-examination | secondary | 2026-06-06 | JAMA | RCE 系列合集页 (own publication) |
| T02-S012 | https://jamaevidence.mhmedical.com/content.aspx?bookid=845&sectionid=70850921 | secondary | 2026-06-06 | JAMAevidence | RCE 验前概率+LR 表章 (vendor docs) |
| T02-S013 | https://www.isabelhealthcare.com/validation/peer-reviews/accuracy-studies | secondary | 2026-06-06 | Isabel Healthcare | Isabel DDx 厂商 accuracy 汇总 (vendor docs) |
| T02-S014 | https://pubmed.ncbi.nlm.nih.gov/12716712/ | verified_primary | 2026-06-06 | Ramnarayan et al | Isabel 儿科首次性能评估 (独立) |
| T02-S015 | https://doi.org/10.1001/jama.2023.8288 | verified_primary | 2026-06-06 | Kanjee/Crowe/Rodman (JAMA) | GPT-4 解 NEJM CPC (=T01-S037/T04-S070) |
| T02-S016 | https://ai.nejm.org/doi/full/10.1056/AIp2300031 | secondary | 2026-06-06 | NEJM AI | GPT-4 诊断复杂病例原文 (own publication) |
| T02-S017 | https://doi.org/10.1001/jamanetworkopen.2024.40969 | verified_primary | 2026-06-06 | Goh et al (JAMA Netw Open) | LLM 诊断推理 RCT — AI alone 悖论 (=T01-S054) |
| T02-S018 | https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11519755/ | verified_primary | 2026-06-06 | Goh et al (PMC) | 同上全文 (=T01-S055) |
| T02-S019 | https://www.medrxiv.org/content/10.1101/2024.08.05.24311485.full.pdf | secondary | 2026-06-06 | Goh et al (medRxiv) | LLM 管理推理 RCT preprint |
| T02-S020 | https://www.nature.com/articles/s41586-025-08866-7 | verified_primary | 2026-06-06 | Tu/Natarajan et al (Nature) | AMIE 对话诊断 AI (=T01-S053) |
| T02-S021 | https://www.nature.com/articles/s41586-025-08869-4 | verified_primary | 2026-06-06 | Google (Nature) | AMIE 准确鉴别诊断 LLM 论文 |
| T02-S022 | https://research.google/blog/amie-a-research-ai-system-for-diagnostic-medical-reasoning-and-conversations/ | verified_primary | 2026-06-06 | Google Research | AMIE 官方研究博客 |
| T02-S023 | https://www.openevidence.com/ | secondary | 2026-06-06 | OpenEvidence | 工具官网 (vendor) |
| T02-S024 | https://pmc.ncbi.nlm.nih.gov/articles/PMC12951846/ | verified_primary | 2026-06-06 | PMC | OpenEvidence 独立评述/case |
| T02-S025 | https://www.nbcnews.com/tech/tech-news/openevidence-ai-doctor-medical-physician-login-app-what-npi-uptodate-rcna341064 | secondary | 2026-06-06 | NBC News | OpenEvidence 采用率报道 (>40% US 医生) |
| T02-S026 | https://glass.health/ | secondary | 2026-06-06 | Glass Health | Glass DDx/AI 官网 (vendor) |
| T02-S027 | https://www.uptodate.com/ | secondary | 2026-06-06 | UpToDate (Wolters Kluwer) | 临床决策支持知识库官网 (vendor) |
| T02-S028 | https://pubmed.ncbi.nlm.nih.gov/23465250/ | verified_primary | 2026-06-06 | Six et al | HEART score 前瞻验证 |
| T02-S029 | https://pmc.ncbi.nlm.nih.gov/articles/PMC6005932/ | verified_primary | 2026-06-06 | PMC | HEART score ED 应用指南/c-statistic |
| T02-S030 | https://www.aafp.org/pubs/afp/issues/2013/0715/p98.html | secondary | 2026-06-06 | AAFP (Am Fam Phys) | PERC rule 临床综述 (协会期刊) |
| T02-S031 | https://pmc.ncbi.nlm.nih.gov/articles/PMC4660778/ | verified_primary | 2026-06-06 | PMC | PROPER PERC RCT 方案 (Kline 谱系) |
| T02-S032 | https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9502997/ | verified_primary | 2026-06-06 | PMC | Ottawa ankle rules meta 灵敏度 97.6% |
| T02-S033 | https://www.nature.com/articles/srep22911 | verified_primary | 2026-06-06 | Sci Reports | Expanded CURB-65 vs PSI/CURB-65 AUC |
| T02-S034 | https://pubmed.ncbi.nlm.nih.gov/21248608/ | verified_primary | 2026-06-06 | Ely/Graber/Croskerry | Checklists to Reduce Diagnostic Errors 2011 |
| T02-S035 | https://www.degruyter.com/document/doi/10.1515/dx-2015-0008/html | secondary | 2026-06-06 | Diagnosis (De Gruyter) | 防错 checklist 试点 RCT (own publication) |
| T02-S036 | https://www.cambridge.org/core/journals/canadian-journal-of-emergency-medicine/article/B768948819704516DBE325909A8D611E | secondary | 2026-06-06 | CJEM (Cambridge) | cognitive forcing 无效对照试验 (own publication) |
| T02-S037 | https://pubmed.ncbi.nlm.nih.gov/35369942/ | verified_primary | 2026-06-06 | PubMed | Diagnostic Time-Outs to Improve Diagnosis |
| T02-S038 | https://pubmed.ncbi.nlm.nih.gov/31226996/ | verified_primary | 2026-06-06 | BMC Med Educ | SNAPPS 改善临床推理 RCT |
| T02-S039 | https://pubmed.ncbi.nlm.nih.gov/36625402/ | verified_primary | 2026-06-06 | PubMed | OMP+SNAPPS 系统综述 meta-分析 |
| T02-S040 | https://pmc.ncbi.nlm.nih.gov/articles/PMC9008989/ | verified_primary | 2026-06-06 | PMC | Script Concordance Test 可接受性/效用 |
| T02-S041 | https://pmc.ncbi.nlm.nih.gov/articles/PMC12973566/ | verified_primary | 2026-06-06 | PMC | SCT 问题: 专家校准 trail (批评) |
| T02-S042 | https://www.sciencedirect.com/science/article/pii/S2666449624000410 | secondary | 2026-06-06 | Safety Science (Elsevier) | 医疗 AI automation bias Bowtie 分析 |
| T02-S043 | https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12909220/ | verified_primary | 2026-06-06 | Front Med/PMC | AI 去技能化 deskilling dilemma |
| T02-S044 | https://clinicaltrials.gov/study/NCT06963957 | verified_primary | 2026-06-06 | ClinicalTrials.gov | Physician-LLM automation bias 进行中 RCT |
| T02-S045 | https://erictopol.substack.com/p/stump-the-medical-expert | verified_primary | 2026-06-06 | Eric Topol (Ground Truths) | GPT-4 诊断 vignette→真实外推批判 (=T01 生态) |
| T02-S046 | https://psnet.ahrq.gov/issue/clinical-reasoning-toolkit | verified_primary | 2026-06-06 | AHRQ PSNet | SIDM Clinical Reasoning Toolkit 收录 (=T04-S005) |
| T02-S047 | https://www.ncbi.nlm.nih.gov/books/NBK20487/ | verified_primary | 2026-06-06 | Croskerry (AHRQ 文集) | cognitive forcing/dual-process 原典 (=T01-S006) |

**Bucket 计数**: verified_primary 27 / secondary 20 / blacklisted 0 — 一手层 **27/47 ≈ 57%** (达标 ≥55%)。secondary 多为工具厂商官网 (vendor docs, 必备工具识别用) + 期刊 own-publication 平台页 (jamanetwork/jamaevidence/degruyter/cambridge, 内容本身是一手但 classifier 默认降级) + 2 条新闻/Wikipedia 元数据。无黑名单 (知乎/公众号/CSDN/G2/Capterra 全部规避)。

---

## 总览（按 tier 分组）

### 必备层（7 个 — ≥ 大多数从业者日常用 / 教学普及）

| 工具 | 一句话 | Decay | Sources |
|------|--------|-------|---------|
| MDCalc (决策规则聚合站) | 900+ 经验证评分/计算器的临床决策支持总站, 80%+ 美国医生用 | low | T02-S005,S006,S007 |
| 临床决策规则 (Wells/PERC/HEART/CURB-65/Centor/Ottawa/NEWS2) | 把高频「该不该查/收」问题外显成可验证评分 | low | T02-S001,S028,S031,S032,S033 |
| 似然比 + Fagan nomogram (概率工具) | 验前概率 × LR → 验后概率的随身贝叶斯更新器 | low | T02-S008,S009 |
| JAMA Rational Clinical Examination (体检循证证据) | 「Does this patient have…?」给每个体征/病史标 LR | low | T02-S010,S011,S012 |
| UpToDate / DynaMed (知识库 CDS) | 主题式循证摘要 — 验前概率与 DDx 的事实底座 | low-med | T02-S027 |
| 思维框架: illness script / problem representation / schema | 把病例压成 one-liner→沿 pivot 走鉴别树 (CPSolvers 系) | low | T02-S046,S047 |
| 教学框架: SNAPPS / One-Minute Preceptor | 把汇报变成「外显推理 + 暴露不确定性」的结构 | low | T02-S038,S039 |

### 场景特化层（5 个）

| 工具 | 一句话 | Decay | Sources |
|------|--------|-------|---------|
| Isabel (DDx 生成器) | 输入特征→排序鉴别清单, 给新手「想不到的病」兜底 | medium | T02-S013,S014 |
| Ely/Graber 诊断 checklist + diagnostic timeout | 收尾前强制重审鉴别的去偏元认知动作 (效果有争议) | low | T02-S034,S035,S037 |
| cognitive forcing strategies | 针对特定偏倚的主动套用对策 (transfer 证据弱) | low | T02-S036,S047 |
| Script Concordance Test (评估工具) | 在不确定性下测临床推理的考试法 (校准依赖专家panel) | low | T02-S040,S041 |
| VINDICATE-M / 解剖定位 / can't-miss×common (病因筛框架) | 系统化穷举鉴别避免漏 + 按致命/常见双轴排序 | low | T02-S046 (=T04 概念表) |

### 新兴层（3 个 — Decay risk: HIGH, 数字截至 2026-06-06, 6-12 月内可能翻转）

| 工具 | 一句话 | Decay | Sources |
|------|--------|-------|---------|
| LLM 诊断助手 (GPT-4/o1/ChatGPT) | 鉴别诊断头脑风暴 + 推理伙伴; 「AI alone > 医生+AI」悖论 | **high** | T02-S015,S017,S018,S045 |
| OpenEvidence (AI 循证检索) | 增长最快的医生 AI, point-of-care 循证问答 (>40% US 医生) | **high** | T02-S023,S024,S025 |
| Google AMIE / Glass Health (实验性诊断 AI) | 对话式诊断 AI, 研究环境追平/超 PCP, 未临床落地 | **high** | T02-S020,S021,S022,S026 |

---

## 工具详细条目

### 1. MDCalc（决策规则聚合站）

- **One-liner**: 把 900+ 经同行验证的评分/决策规则/计算器收进一个 point-of-care 站, 已成全球最广用的临床决策支持平台之一 (evidence: [T02-S005, T02-S006])。
- **Tier**: 必备
- **Maintainer / Owner**: MDCalc (MDAware LLC), https://www.mdcalc.com — 由 board-certified 医生编写
- **License**: proprietary (免费访问 web/app)
- **Maturity signals**:
  - 采用率: 「>80% 美国临床医生 + 全球数百万」使用 (厂商自陈, vendor claim — caveat: 来源是 MDCalc 自家 about 页, 非独立审计) (evidence: [T02-S005])
  - 内容量: 近 900 个 evidence-based 评分/计算器, 50+ 专科 (last checked: 2026-06-06, vendor) (evidence: [T02-S005])
  - 独立证据: web 决策计算器使用模式实证研究显示 CHA₂DS₂-VASc / MAP / HAS-BLED / NIHSS / CHADS₂ 为最高频 (一手, evidence: [T02-S007])
- **典型使用场景**: ED/病房收治决策点 (chest pain→HEART; ?PE→Wells+PERC; pneumonia→CURB-65); 需要标准化验前概率/风险分层时。
- **不适合 / 替代方案**: 不适合做「初始鉴别诊断生成」(它是验证/分层工具, 不是 DDx 生成器 — 那是 Isabel/LLM 的活); 规则盒外人群 (rule 验证人群外的患者) 乱用会误导。替代: 各规则原始论文 / RCE。
- **生产案例**: 美国住院医培训普遍把 MDCalc 嵌入晨会/查房决策 (业内普遍, 见使用模式研究 [T02-S007])。
- **维护者背景**: 无单一 Track 01 figure (聚合站); 但收录的规则作者 (Wells/Kline/Six 等) 是本行决策规则谱系。
- **近期变化**: 持续增补 AI 时代 calculator 与 EHR 集成 (vendor, 未独立确认)。
- **来源**: [Primary] 独立使用模式研究 PMC8369374 (collected 2026-06-06); [Reference] MDCalc about (vendor); [Reference] Wikipedia 元数据。
- **可信度**: high (作为聚合站存在与广用) / medium (具体采用率数字为 vendor 自陈)
- **Decay risk**: low (24+ 月内仍是行业基础设施, 概率 <20%)

### 2. 临床决策规则 / 评分（Wells / PERC / HEART / CURB-65 / Centor / Ottawa / NEWS2）

- **One-liner**: 把高频「该不该查影像 / 该不该收住院 / 能不能安全排除」问题, 从医生脑内 gestalt 外显成可验证、可审计的加权评分。
- **Tier**: 必备
- **Maintainer / Owner**: 各规则原始研究者 (Wells PE: Philip Wells; PERC: Jeff Kline; HEART: Six/Backus; Ottawa: Ian Stiell) — 经 MDCalc 等托管
- **License**: open (学术发表, 免费使用)
- **Maturity signals / 验证强度 (每个数字挂 source)**:
  - **Wells (PE)**: 分层工具; gestalt 与 Wells 一致性差 (所有 κ <0.3); 低概率组 PE 患病率 gestalt 7.6% vs Wells 12.6%, 高概率组 72.1% vs 58.1% (evidence: [T02-S004])。Wells<2 + PERC 0 的组合灵敏度「suboptimal」, 漏过亚段 PE (evidence: [T02-S003])。
  - **PERC**: Kline 2004 派生, 2008 多中心验证: 8 项全阴 + gestalt 低概率者 PE 假阴率约 1.0%（1666 例中 15 例, 95%CI 0.6–1.6%, 低于 2% 检测阈值)(evidence: [T02-S030, T02-S031])。**关键 caveat**: PERC 设计上**先问 gestalt 低概率**才适用 — 规则不替代 gestalt, 是 gestalt 之后的二次门 (evidence: [T02-S003])。
  - **HEART**: c-statistic 约 0.83 (good-excellent 区分 MACE); HEART 0-3 排除 30 天 MACE「>98% 确定性」— 但近期研究警告 HEART=3 的 MACE 率可能高于传统 2% 低危阈值 (矛盾保留)(evidence: [T02-S028, T02-S029])。
  - **CURB-65**: 5 项 (confusion/urea>7/RR≥30/SBP<90 或 DBP≤60/age≥65); 预测 30 天死亡 AUC 约 0.756 (扩展版 0.826, PSI 0.801)(evidence: [T02-S033])。
  - **Ottawa ankle**: 27 研究 meta 灵敏度 97.6%、中位特异度 31.5%; 原始研究 100% 灵敏并减 36% X 线 (evidence: [T02-S032])。
  - **Centor / NEWS2**: Centor=咽炎链球菌验前概率四项; NEWS2=生命体征恶化早期预警评分 (本批未取到独立强验证数, 标注信号薄, 引用待补)。
- **典型使用场景**: 急诊未分化主诉的「安全排除 / 风险分层」; 减少不必要影像/抽血/收治。
- **不适合 / 替代方案**: **盒外乱用 = 头号坑** — 规则只在其验证人群内有效 (Ottawa 不能用于多发伤/醉酒; PERC 不能用于高验前概率); 致命病不能仅凭规则阴性就停 (test of treatment/safety net 仍需)。替代/互补: 资深 gestalt (见决策树)。
- **维护者背景**: 规则谱系与 Track 01 床旁/急诊派交叉; Croskerry/Sherbino 在急诊推理论战中讨论 rule-vs-gestalt。
- **来源**: [Primary] PERC PROPER PMC4660778; HEART PMC6005932; Ottawa meta PMC9502997; CURB-65 SciReports (all collected 2026-06-06)。
- **可信度**: high (验证文献丰富)
- **Decay risk**: low (核心规则 10-20 年稳定; 个别阈值会被新研究微调)

### 3. 似然比 (LR) + Fagan nomogram（概率工具）

- **One-liner**: 把贝叶斯定理变成床旁可用: 验前概率 × 似然比 → 验后概率, Fagan nomogram 是其图解直尺版 (1975 Fagan 提出)(evidence: [T02-S008])。
- **Tier**: 必备 (概念层)
- **Maintainer / Owner**: 概念 — Thomas Fagan (nomogram); McGee (LR 简化表); JAMA RCE (体征 LR 库)
- **License**: open
- **Maturity signals**:
  - Fagan 1975 起源, 持续被教学采用; 三标尺 (验前/LR/验后), 直尺连线读验后 (evidence: [T02-S008])。
  - McGee《Simplifying Likelihood Ratios》给出口算近似 (LR 2/5/10 ≈ +15/+30/+45% 验后概率增量) — 床旁心算法 (evidence: [T02-S009])。
  - **SnNout / SpPin**: 高灵敏阴性→排除 (SnNout), 高特异阳性→确诊 (SpPin) — 口诀级工具 (evidence: [T02-S009] 谱系)。
- **典型使用场景**: 解读检查结果时更新概率; 决定「这个阳性/阴性是否跨过决策阈值」; 教学中显式化「为什么这个检查在这个病人身上没用」。
- **不适合 / 替代方案**: 验前概率本身难精确 (是估计, 非测量 — 这是最大软肋); 多检查序贯时 LR 独立性假设常被违反。替代: Sox《Medical Decision Making》阈值模型 (T04 canon)。
- **维护者背景**: McGee (Track 01 figure #14, EBPD 作者); 决策科学派 (Pauker-Kassirer-Sox 谱系, T04)。
- **来源**: [Primary] PMC4902203 (Fagan 演化); [Primary] McGee JGIM 2002 (collected 2026-06-06)。
- **可信度**: high
- **Decay risk**: low (数学不变; 具体 LR 数值随新研究更新)

### 4. JAMA Rational Clinical Examination（体检/病史循证证据库）

- **One-liner**: 「Does this patient have [疾病]?」系列 — 给每个病史/体检发现标注验前概率与 LR, 把床旁体检从经验主义变循证 (evidence: [T02-S010, T02-S012])。
- **Tier**: 必备 (参考工具)
- **Maintainer / Owner**: JAMA / JAMAevidence (McGraw Hill); Simel & Rennie 编 (T04-S027)
- **License**: proprietary (机构订阅; 部分 JAMA 合集页公开)
- **Maturity signals**:
  - 每篇含「Make the Diagnosis」段: 验前概率 + 适用人群 + 最佳发现 LR 表 + 参考标准 (evidence: [T02-S012])。
  - 覆盖 bacteremia / ACS / 心衰 / 腰痛 等数十主题, 期刊长青系列 (evidence: [T02-S011])。
- **典型使用场景**: 决定「该问/查哪个体征性价比最高」; 教学时给体检发现「定价」(配 McGee EBPD)。
- **不适合 / 替代方案**: 不是 point-of-care 快查 (是综述, 读起来重); 主题覆盖有限。替代: McGee《Evidence-Based Physical Diagnosis》(更全, T04-S018)。
- **维护者背景**: 与 McGee (Track 01 #14) / Verghese 床旁运动 (Track 01 #5) 同一循证体检阵营。
- **来源**: [Reference] JAMAevidence 平台 (vendor docs); [Reference] JAMA 合集页 (own publication)(collected 2026-06-06)。
- **可信度**: high
- **Decay risk**: low

### 5. UpToDate / DynaMed（知识库 / 临床决策支持 CDS）

- **One-liner**: 主题式循证摘要库 — 临床医生查验前概率、鉴别清单、诊疗路径的事实底座 (evidence: [T02-S027])。
- **Tier**: 必备 (知识库)
- **Maintainer / Owner**: UpToDate = Wolters Kluwer; DynaMed = EBSCO
- **License**: proprietary (机构/个人订阅)
- **Maturity signals**: 行业标配 CDS; Goh RCT 中作为「conventional resources」对照臂 (evidence: [T02-S017])。
- **典型使用场景**: 已有鉴别后深入某病的诊断标准/检查路径; 验前概率/患病率查询。
- **不适合 / 替代方案**: 不生成鉴别 (你得先知道往哪查); 更新有延迟。**关键矛盾**: OpenEvidence 等 AI 检索正在蚕食其「point-of-care 快查」场景 (evidence: [T02-S025])。替代/竞争: OpenEvidence, DynaMed。
- **来源**: [Reference] 官网 (vendor); [Primary] Goh RCT 把其列为对照 (collected 2026-06-06)。
- **可信度**: high
- **Decay risk**: low-medium (产品稳, 但 AI 检索竞争可能改变其角色, 18 月内 20-40%)

### 6. 思维框架: illness script / problem representation / semantic qualifier / schema

- **One-liner**: 临床医生「用来想」的认知器具 — 把杂乱病例压成 one-liner (problem representation) → 配成对语义限定词 → 沿 pivot 症状走鉴别 schema (evidence: [T02-S046, T02-S047])。
- **Tier**: 必备 (认知框架, 见 T04 概念表)
- **Maintainer / Owner**: illness script = Schmidt/Boshuizen (T04-S048); schema 教学 = Clinical Problem Solvers (T01 #11, T04-S090/S091); SIDM Clinical Reasoning Toolkit 收录 (evidence: [T02-S046])
- **License**: open (免费教学资源 — CPSolvers schema 图库免费)
- **Maturity signals**: AHRQ PSNet 收录 SIDM toolkit 为协会级教育工具 (evidence: [T02-S046]); CPSolvers VMR 全球普及 (T01)。
- **典型使用场景**: 汇报时把病例「翻译成 one-liner」; 用 schema 把「头晕」拆成分支生成鉴别; 用 illness script 比对「这个病人像不像 X 病的典型剧本」。
- **不适合 / 替代方案**: 框架不替代知识 (Norman 派: schema 空有结构没内容=无用, context specificity); 新手套框架易僵化。替代/互补: VINDICATE 病因筛 (穷举型 vs schema 的 pivot 型)。
- **维护者背景**: Schmidt/Norman/Mamede (Track 01 教育认知派) + CPSolvers Geha/Manesh (Track 01 #11)。
- **来源**: [Primary] AHRQ PSNet toolkit; [Primary] Croskerry AHRQ 章 (collected 2026-06-06)。
- **可信度**: high
- **Decay risk**: low

### 7. 教学框架: SNAPPS / One-Minute Preceptor

- **One-liner**: 把学习者汇报从「念事实」变成「外显推理 + 主动暴露不确定性」的结构化脚本 (evidence: [T02-S038, T02-S039])。
- **Tier**: 必备 (教学工具)
- **Maintainer / Owner**: SNAPPS = Wolpaw; OMP = Neher 等
- **License**: open
- **Maturity signals**: SNAPPS = Summarize/Narrow/Analyze/Probe/Plan/Select 六步; RCT 显示 SNAPPS 组诊断假设更清晰、主动发起管理讨论多约 20% (evidence: [T02-S038]); OMP+SNAPPS 系统综述+meta 证实改善临床推理 (evidence: [T02-S039])。
- **典型使用场景**: 门诊/查房带教; 让住院医「narrow + analyze 鉴别 + probe 不确定性」而非背诵。
- **不适合 / 替代方案**: 需要 preceptor 受训; 时间压力大时退化。替代: 传统 pimping (证据弱且有争议)。
- **维护者背景**: 与 Track 01 教育派 + CPSolvers VMR 教学法呼应。
- **来源**: [Primary] BMC Med Educ SNAPPS RCT; [Primary] OMP+SNAPPS meta (collected 2026-06-06)。
- **可信度**: high
- **Decay risk**: low

### 8. Isabel（DDx 生成器）

- **One-liner**: 输入临床特征→输出排序鉴别清单, 给临床医生 (尤其新手) 一个「想不到的病」兜底网 (evidence: [T02-S013, T02-S014])。
- **Tier**: 场景特化
- **Maintainer / Owner**: Isabel Healthcare (Jason Maude 创办), https://www.isabelhealthcare.com
- **License**: proprietary
- **Maturity signals (数字一律 caveat)**:
  - 厂商内部 563 例研究: 98% 正确诊断进 top10、74% 进 top3 (vendor 自评, 内部数据集, 非独立 — caveat)(evidence: [T02-S013])。
  - 独立早期评估 (儿科, Ramnarayan 2003) 验证其作为 DDx aid 的可用性 (一手, evidence: [T02-S014])。
  - 厂商称 22+ 年验证、RCT 提升诊断准确率「up to 33%」(vendor claim — caveat: 数字来自厂商页)(evidence: [T02-S013])。
- **典型使用场景**: 鉴别诊断卡壳、担心漏诊罕见病时; 教学中对比学员鉴别 vs 生成器。**给新手获益更大** (厂商与多中心研究均指向此)(evidence: [T02-S013])。
- **不适合 / 替代方案**: 不是确诊工具 (输出是清单不是答案); 专科领域 (手外科/眼眶病) 表现更不稳 (evidence: [T02-S013])。**避坑**: 把生成器清单当最终诊断 = VOMIT/过度检查源头。替代: LLM 诊断助手 (新兴, 性能更高但 decay 高)。
- **维护者背景**: DXplain/INTERNIST-1 专家系统谱系 → Isabel → LLM 世代 (Rodman NEJM AI 百年史框架, T01-S039)。
- **近期变化**: 2024-25 推「Isabel DDx Companion」叠加 LLM (vendor)。
- **来源**: [Primary] Ramnarayan PubMed 2003; [Reference] Isabel accuracy 页 (vendor docs)(collected 2026-06-06)。
- **可信度**: medium (独立证据旧, 近期数字依赖 vendor)
- **Decay risk**: medium (被 LLM 通用模型挤压; 18-24 月内 20-40% 概率角色显著变化)

### 9. Ely/Graber 诊断 checklist + diagnostic timeout

- **One-liner**: 收尾前强制套用的「重审鉴别」清单 — 一般认知 checklist + 鉴别 checklist + 特定病陷阱 checklist (evidence: [T02-S034])。
- **Tier**: 场景特化 (去偏工具)
- **Maintainer / Owner**: John Ely + Mark Graber + Pat Croskerry (Track 01 #2/#8)
- **License**: open (发表)
- **Maturity signals / 效果矛盾 (诚实保留)**:
  - Ely 2011 提出三类 checklist (evidence: [T02-S034])。
  - diagnostic timeout = Type-2 executive override, 收尾前暂停重审 (evidence: [T02-S037])。
  - **关键矛盾**: 试点 RCT 与综述对 checklist/timeout 防错效果「mixed」, 部分研究**未证明有效** (evidence: [T02-S035, T02-S037]); cognitive forcing 对照试验显示**无效** (见条目 10)。Croskerry 阵营回应: 去偏需系统级+长期组合, 单针 RCT 难证伪 (evidence: [T02-S047])。
- **典型使用场景**: 高风险/诊断不确定病例收尾; M&M 复盘; 「最坏情况排除了吗 (worst-case scenario)」。
- **不适合 / 替代方案**: 时间压力下退化; 把 checklist 当形式 = 自动化偏倚的另一种。替代/互补: Mamede deliberate reflection (有阳性证据, T01-S030)。
- **维护者背景**: Croskerry/Graber (Track 01 偏倚派 + 诊断安全派)。
- **来源**: [Primary] Ely PubMed 21248608; [Primary] Diagnostic Time-Outs PubMed 35369942 (collected 2026-06-06)。
- **可信度**: high (工具存在) / 效果 = contested
- **Decay risk**: low (概念稳; 效果证据持续争论)

### 10. Cognitive Forcing Strategies（认知强制策略）

- **One-liner**: 针对特定偏倚 (锚定/可得性) 的主动对策 — 「想到 X 时强制问 what else」(evidence: [T02-S047])。
- **Tier**: 场景特化 (去偏工具, 效果争议大)
- **Maintainer / Owner**: Pat Croskerry (Track 01 #2)
- **License**: open
- **Maturity signals / 核心论战 (双向保留)**:
  - Croskerry 派: cognitive forcing 是元认知层 Type-2 override, 可教 (evidence: [T02-S047])。
  - **批判派实证**: 「cognitive forcing strategies 在减少诊断推理偏倚上**无效**」(对照试验, evidence: [T02-S036]); Norman/Sherbino: debiasing transfer 证据弱, 错误主因是知识缺口 (Track 01 论战, T01-S011/S012)。
  - **不可写成 settled science** — 两边都是本 skill 素材 (intake.warnings)。
- **典型使用场景**: 教学中提高偏倚意识; 个人元认知习惯。
- **不适合 / 替代方案**: 别指望它单独消除误诊 (证据弱); 替代: 练知识/样例 (Norman 派) + deliberate reflection (Mamede)。
- **维护者背景**: Croskerry vs Norman/Sherbino — 本行最核心论战 (Track 01)。
- **来源**: [Primary] CJEM 无效对照试验; [Primary] Croskerry AHRQ 章 (collected 2026-06-06)。
- **可信度**: high (工具与论战均可溯源)
- **Decay risk**: low

### 11. Script Concordance Test（SCT — 推理评估工具）

- **One-liner**: 给一串带不确定性的临床 vignette, 测学员推理是否与专家 panel 一致的考试法 (evidence: [T02-S040])。
- **Tier**: 场景特化 (评估工具)
- **Maintainer / Owner**: Charlin 等 (Montreal 谱系)
- **License**: open
- **Maturity signals / 批评**: 本科/研究生层有效性/信度/可行性证据 (evidence: [T02-S040]); **批评**: 依赖专家 panel 校准, panel 招募与训练不可低估, 校准不当损害效度 (evidence: [T02-S041])。
- **典型使用场景**: 临床推理课程的形成性/总结性评估; 配 key feature exam。
- **不适合 / 替代方案**: 评分依赖专家共识 (循环风险); 替代: key feature exam / OSCE。
- **来源**: [Primary] PMC9008989; [Primary] PMC12973566 (collected 2026-06-06)。
- **可信度**: high
- **Decay risk**: low

### 12. VINDICATE-M / 解剖定位 / can't-miss × common（病因筛框架）

- **One-liner**: 系统化穷举鉴别避免漏 (VINDICATE 病因记忆术) + 按「致命不能漏 × 常见」双轴排序 (见 T04 概念表)。
- **Tier**: 场景特化 (认知框架)
- **Maintainer / Owner**: 教材通用 (VINDICATE); Stern《Symptom to Diagnosis》(can't-miss×common, T04-S022)
- **License**: open
- **Maturity signals**: 教材级标准框架; 与 schema (pivot 型) 互补 — VINDICATE 是穷举型 (evidence: T04 概念表/S046)。
- **典型使用场景**: 担心鉴别不全时穷举病因类别; 急诊先排 can't-miss。
- **不适合 / 替代方案**: 穷举易产生 VOMIT/过度检查; 替代: schema (更聚焦)。
- **来源**: [Reference] T04 概念表 / SIDM toolkit (collected 2026-06-06)。
- **可信度**: high
- **Decay risk**: low

### 13. LLM 诊断助手（GPT-4 / o1 / ChatGPT）— 新兴, Decay HIGH

- **One-liner**: 通用大模型做鉴别诊断头脑风暴 + 推理伙伴; 在病例集上追平/超人类, 但出现「AI alone > 医生+AI」悖论 (evidence: [T02-S015, T02-S017])。
- **Tier**: 新兴 (stability: experimental)
- **Maintainer / Owner**: OpenAI 等
- **License**: proprietary
- **Maturity signals (数字截至 research_date 2026-06-06, 可能被后续翻转)**:
  - Kanjee/Rodman JAMA 2023: GPT-4 在 70 例 NEJM CPC 中, 鉴别含正确诊断 64% (45/70)、首位诊断 39% (27/70)(evidence: [T02-S015, T02-S016])。**caveat**: CPC 信息丰富, 真实世界表现可能更低 (作者自陈)。
  - Goh JAMA Netw Open 2024 RCT (50 医生): 给医生 LLM **未显著** 提升诊断推理 vs 仅常规资源; 但 **LLM 单独得分显著高于两组医生** — 「AI alone 悖论」(evidence: [T02-S017, T02-S018])。**caveat**: vignette 研究, 非真实结局; 「截至 research_date 的发现, 可能被后续研究翻转」。
- **典型使用场景**: 鉴别诊断「想不到的病」扩列; 推理质疑伙伴 (「我漏了什么」)。
- **不适合 / 替代方案**: **绝不当最终诊断** (幻觉/编造引用); vignette→真实世界外推未验证 (Topol 公开点名此缺口, evidence: [T02-S045])。**避坑**: 自动化偏倚 + 去技能化 (见条目 16)。替代: OpenEvidence (循证锚定)。
- **维护者背景**: Rodman (Track 01 #7) JAMA/Science 研究核心; Topol (Track 01 #12) 证据守门。
- **近期变化 (HIGH decay)**: o1/推理模型迭代; 医生+AI 协作设计是开放问题 (Goh 后续管理推理 RCT, evidence: [T02-S019])。
- **来源**: [Primary] JAMA 2023 doi; [Primary] Goh RCT doi/PMC; [Primary] Topol substack (collected 2026-06-06)。
- **可信度**: high (研究可溯源) / 结论 = contested
- **Decay risk**: **high** (12 月内 >40% 概率显著变化)

### 14. OpenEvidence（AI 循证检索）— 新兴, Decay HIGH

- **One-liner**: 增长最快的医生 AI — point-of-care 循证问答, 只引 PubMed/指南等同行评议源 (evidence: [T02-S023, T02-S025])。
- **Tier**: 新兴 (stability: experimental)
- **Maintainer / Owner**: OpenEvidence (Daniel Nadler 等), https://www.openevidence.com
- **License**: proprietary (对验证 US 临床医生免费)
- **Maturity signals (截至 2026-06-06, vendor/媒体, caveat)**:
  - 采用率: 报道称 >40% 美国医生每日登录、>10000 家医院、每月 +65000 新注册 (媒体/vendor, 非独立审计 — caveat)(evidence: [T02-S023, T02-S025])。
  - 2025-12 约 1800 万次咨询/月 (一年前约 300 万)(vendor 报道, caveat)(evidence: [T02-S025])。
  - 独立评述见 PMC (evidence: [T02-S024])。
- **典型使用场景**: 验前概率/诊断标准/最新证据的 point-of-care 快查 (蚕食 UpToDate 场景)。
- **不适合 / 替代方案**: 仍可能幻觉/引用错配; 不是 DDx 生成器。替代: UpToDate (人工策展, 更慢更稳)。
- **维护者背景**: 无 Track 01 figure 直接关联; Topol 等讨论 AI 检索浪潮 (T01)。
- **近期变化 (HIGH decay)**: 语音/多模态、医院集成扩张 (vendor)。
- **来源**: [Primary] PMC 评述; [Reference] 官网 (vendor); [Reference] NBC 报道 (collected 2026-06-06)。
- **可信度**: medium (存在与势头确凿; 具体采用数字为 vendor/媒体)
- **Decay risk**: **high**

### 15. Google AMIE / Glass Health（实验性诊断 AI）— 新兴, Decay HIGH

- **One-liner**: 专为诊断对话优化的 AI — 研究环境追平/超 PCP, 但未临床落地 (evidence: [T02-S020, T02-S022])。
- **Tier**: 新兴 (stability: experimental)
- **Maintainer / Owner**: AMIE = Google DeepMind/Research; Glass Health = Glass Health Inc.
- **License**: AMIE = 研究系统 (未公开产品); Glass = proprietary
- **Maturity signals (截至 2026-06-06)**:
  - AMIE Nature 2025: 与 20 名 PCP 双盲交叉, 159 案例; AMIE 在专科医生评 32 轴中 30 轴、患者评 26 轴中 25 轴占优 (evidence: [T02-S020, T02-S021])。**caveat**: 同步文字聊天非真实临床形态, 落地前需更多研究 (作者自陈, evidence: [T02-S020])。
  - Glass Health = 临床推理/DDx 生成 + plan 草拟 AI (vendor, evidence: [T02-S026])。
- **典型使用场景**: (研究/早期) 对话式问诊+鉴别生成; Glass 用于 assessment/plan 草拟。
- **不适合 / 替代方案**: AMIE 非可用产品; 真实部署证据缺。替代: GPT-4/OpenEvidence (已可用)。
- **维护者背景**: AMIE 团队曾在 Track 01 候选 (DROP-to-Track02, T01 #29)。
- **来源**: [Primary] Nature 两篇; [Primary] Google Research 博客 (collected 2026-06-06)。
- **可信度**: high (研究) / 产品成熟度 low
- **Decay risk**: **high**

---

## 选型决策树

### 决策树 A: 你现在要解决的核心诊断问题是什么？

#### Branch 1: 我已有明确鉴别, 要回答「该不该查/收/能否安全排除」(高频结构化决策点)
→ **推荐**: 该场景的**临床决策规则** (chest pain→HEART; ?PE→先 gestalt 低概率再 PERC, 或 Wells; pneumonia→CURB-65; ankle→Ottawa), 经 MDCalc 快取 (evidence: [T02-S005, T02-S028, T02-S031])
→ **前提**: 病人必须落在规则的**验证人群内** — 盒外乱用是头号坑 (evidence: [T02-S030])
→ **不推荐**: 纯靠 DDx 生成器/LLM (它们不做风险分层验证)
→ 真实模式: PERC 设计上**先问 gestalt** 再套规则 = rule 是 gestalt 的二次安全门, 不是替代 (evidence: [T02-S003])

#### Branch 2: 我要把某个检查结果转成「这病人现在多大概率有病」
→ **推荐**: **似然比 + Fagan nomogram** (验前概率 × LR → 验后); 体征 LR 查 **JAMA RCE / McGee EBPD** (evidence: [T02-S009, T02-S012])
→ **替代**: Sox 阈值模型 (要不要查/治的决策, T04 canon)
→ 软肋: 验前概率是估计非测量 — 数字别当精确 (evidence: [T02-S009])

#### Branch 3: 我卡在「想不到还能是什么病」(鉴别生成不全, 怕漏)
##### Branch 3a: 想要可溯源、低风险的扩列
→ **推荐**: schema (CPSolvers, 沿 pivot 走) 或 VINDICATE 病因筛 (穷举); DDx 生成器 **Isabel** 作兜底 (尤其新手获益, evidence: [T02-S013])
##### Branch 3b: 想要最高命中率的头脑风暴 (且你能批判性筛)
→ **推荐**: **LLM (GPT-4)** 做鉴别扩列 — 命中率高于 Isabel (evidence: [T02-S015]); **但绝不当最终诊断**, 须人工核实 (evidence: [T02-S045])
→ **避坑**: 把清单当答案 = VOMIT/过度检查 + 自动化偏倚

#### Branch 4: 我要查「这个病的诊断标准/验前概率/最新证据」(知识检索)
→ **推荐 (稳)**: **UpToDate / DynaMed** (人工策展循证) (evidence: [T02-S027])
→ **推荐 (快, 新兴)**: **OpenEvidence** (AI 循证问答, point-of-care 更快) — 但仍可能引用错配, 截至 research_date 高 decay (evidence: [T02-S023, T02-S025])

#### Branch 5: 我是带教者, 要让学员「外显推理」而非背事实
→ **推荐**: **SNAPPS / One-Minute Preceptor** (汇报结构), 配 illness script / problem representation 训练 (evidence: [T02-S038, T02-S046])
→ **评估**: Script Concordance Test (测不确定性下推理, 但需专家 panel 校准, evidence: [T02-S040])

#### Branch 6: 我担心自己/团队的认知偏倚导致误诊
→ **诚实分叉 (论战未决)**: diagnostic timeout / Ely checklist / cognitive forcing 可作元认知习惯, **但其防错 RCT 证据弱/混合** (evidence: [T02-S036, T02-S037]); 批判派主张更该投资**知识与样例库 + deliberate reflection** (Norman/Mamede, T01)
→ 不要把任一方当 settled science

### 决策树 B: 决策规则 vs 临床 gestalt — 什么时候信哪个？
- **用规则**: 高频、有强验证、盒内人群、需要可审计/沟通的决策 (PERC/Ottawa/HEART) (evidence: [T02-S028, T02-S032])
- **用 gestalt**: 规则盒外人群、信息超出规则变量、资深医生且环境反馈好 (gestalt 在高/低概率分层上有时比 Wells 更准, evidence: [T02-S004])
- **两者结合**: 多数最佳实践是 gestalt 定低概率 → 规则二次确认 (PERC 范式) (evidence: [T02-S003])
- **算法厌恶 caveat**: 资深者倾向不信规则; 但 gestalt 与规则一致性差 (κ<0.3), 二者非可互换 (evidence: [T02-S004])

### 决策树 C: AI 辅助诊断 — 用还是不用 (截至 research_date, HIGH decay)
- **用 AI 做**: 鉴别扩列、推理质疑、循证检索 (作"第二意见/认知假体")
- **绝不用 AI 做**: 最终诊断、自主决策 (vignette→真实外推未验证, evidence: [T02-S045])
- **悖论提醒**: 医生+AI ≤ AI alone (Goh 2024) — 协作界面是未解难题, 不代表该让 AI 自主行医 (evidence: [T02-S017])
- **守门**: 防自动化偏倚 + 去技能化 (见避坑清单)

---

## 避坑清单

- ❌ **规则盒外乱用**: PERC 用于高验前概率者 / Ottawa 用于多发伤·醉酒 / HEART 用于非 chest pain → 规则只在验证人群内有效, 盒外阴性会给假安心 (evidence: [T02-S030, T02-S032])
- ❌ **把 PERC/Wells 当 gestalt 替代品**: PERC 设计前提是先有 gestalt 低概率; 把规则当独立黑箱用 = 误用 (evidence: [T02-S003])
- ❌ **把 DDx 生成器 / LLM 清单当最终诊断**: Isabel/GPT-4 输出是**鉴别清单不是答案**; 当答案用 → 漏诊或过度检查 (VOMIT) (evidence: [T02-S013, T02-S045])
- ❌ **自动化偏倚 (automation bias)**: 不加批判地信 CDS/AI 输出 — 含 commission (照错建议做) 与 omission (AI 没提示就不做) 两类错误; 时间压力/疲劳放大 (evidence: [T02-S042])
- ❌ **去技能化 (deskilling)**: 长期把推理外包给 AI → 临床判断/鉴别能力萎缩, 复杂病例反受害 (evidence: [T02-S043])
- ❌ **把去偏 checklist/timeout 当万灵药**: 多个对照试验显示 cognitive forcing/checklist 防错效果弱或无效; 形式化套用反成另一种自动化 (evidence: [T02-S035, T02-S036])
- ❌ **把 vignette/CPC 上的 AI 数字当真实世界性能**: CPC 信息丰富、是干净书面病例, 真实临床的混乱数据下表现可能大幅下降 (evidence: [T02-S045], 作者自陈 [T02-S015])
- ❌ **把 SCT 分数当客观真理**: 评分依赖专家 panel 共识, panel 校准不当则效度崩 (evidence: [T02-S041])

---

## Phase 2 提炼提示

**反复出现 ≥3 source 强调的「工具选型原则」(候选 playbook 规则)**:
- **工具是 gestalt 的二次门, 不是替代** (出现于: T02-S003 / S004 / S030) — 决策规则在 gestalt 之后用, 盒内人群才有效
- **生成型工具 (Isabel/LLM) 的输出永远是鉴别清单, 不是诊断** (T02-S013 / S015 / S045) — 人工核实不可省
- **AI 数字一律 contested + vignette 外推存疑** (T02-S015 / S017 / S045) — 写进诚实边界
- **去偏工具效果未决, 不可写成 settled** (T02-S035 / S036 / S047) — 双向保留论战

**显著的工具流派分裂 (候选智识谱系条目)**:
- **结构化/规则派** (代表工具: Wells/PERC/HEART/MDCalc/Fagan/RCE; 谱系: 决策科学 Pauker-Kassirer-Sox / 循证 McGee) **vs** **gestalt/经验派** (代表: 资深模式识别 / illness script; 谱系: 床旁 Dhaliwal/Verghese, 教育认知 Norman「knowledge is the cure」)
- **去偏可教派** (工具: cognitive forcing / diagnostic timeout / Ely checklist; Croskerry) **vs** **知识为核派** (工具: deliberate reflection / 样例库 / schema; Norman/Sherbino/Mamede) — 本行最核心论战, 工具效果证据是战场
- **薄框架 (schema, pivot 聚焦) vs 厚框架 (VINDICATE 穷举病因筛)** — 前者快后者全, 互补

**新兴工具信号**:
- 当前活跃/上升的新工具数: 4 (GPT-4/o1 诊断助手、OpenEvidence、AMIE、Glass Health)
- 出现 → 主流速度估计: 极快 (OpenEvidence ~12-18 月从 0 到 >40% 美国医生采用, 据报道 [T02-S025]) — 但临床落地/监管滞后, 真实结局证据仍缺
- 全部标 Decay risk: high — master skill 更新时本节优先刷新

**冷僻 / 信号薄弱**:
- 必备层 7 个 (≥3 ✓); 场景特化 5 个 (≥5 ✓); 新兴 3 个 (≥2 ✓) — 三层均达标, **非冷僻**
- verified_primary 57% (≥55% ✓)
- 弱点: Centor/NEWS2 未取到独立强验证数据 (信号薄, 引用待补); AI 采用率数字多为 vendor/媒体 (已挂 caveat); 工具厂商页 (secondary bucket) 占比偏高但均为必备工具识别所需的 vendor docs
```