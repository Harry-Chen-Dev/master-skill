# Track 03 — Workflows / SOPs: 临床诊断思维 (Clinical Diagnostic Reasoning)

> locale=global (en-primary canon) | profile=practitioner | focus=comprehensive | research_date: 2026-06-06
> Wave 3 接力: 复用 T01-figures / T02-tools / T04-canon 全部产出做 seed; 本 track 把碎片拼成「核心诊断推理 SOP」+「入门 vs 资深路径」+「教学工作流」+「去偏/元认知工作流」+「AI 增强工作流」+「诊断质检环」。
> **本行 "工作流" 定义**: 不是疾病的诊疗路径 (那是临床指南), 而是医生「怎么想病」的认知操作链 — 从一个数据状态推进到一个诊断状态的连续动作, 以及把这套动作教出去/查它做得好不好/用 AI 增强它的流程。
> 衰减结构特殊: 核心推理 SOP 与教学工作流 = 极稳 (decay low, 30+ 年文体未变); **AI 增强工作流 = 最高 decay (high)**, 6-12 月即变, 全部挂 last_checked + 「截至 research_date」caveat。
> 数字纪律 (intake.warnings): 每个 %/比率/LR 必挂 source_id 或 caveat (估计/约/业内); 诊断错误率与 AI 性能数字一律 contested, 不写成铁事实; **去偏工作流证据弱要诚实标 (Croskerry vs Norman 双向保留)**; AI alone 悖论不软化任一方。
> 医疗安全边界: 本 skill 是面向临床专业人士/医学生的**思维教练**, 不替代真实临床判断与执业医师诊疗, 不面向患者; 任何 AI 增强工作流均显式标「AI 不当最终诊断」。
> 网络环境: WebFetch 受限, 验证经 WebSearch 结果页; `last_checked` = 当日经搜索确认 URL 仍被索引/存在。本环境 source_verifier.py 不可用, bucket 沿用 T01/T02/T04 已确立约定 (PMC/.gov/doi=verified_primary; 期刊 own-publication 平台页=surrogate_primary; NEJM AI/vendor/新闻=secondary)。

## Source Manifest

| source_id | url | bucket | last_checked | author/host | one-line note |
|-----------|-----|--------|--------------|-------------|---------------|
| T03-S001 | https://www.nejm.org/doi/abs/10.1056/NEJMra054782 | verified_primary | 2026-06-06 | NEJM (Bowen) | problem representation/one-liner/script 教学 SOP 母文 (=T04-S055) |
| T03-S002 | https://pmc.ncbi.nlm.nih.gov/articles/PMC1494926/ | verified_primary | 2026-06-06 | JGIM (Bordage) | 语义限定词/问题表征实证 (=T04-S082) |
| T03-S003 | https://www.nejm.org/clinical-problem-solving | verified_primary | 2026-06-06 | NEJM | Clinical Problem-Solving 渐进披露文体 (=T04-S085) |
| T03-S004 | https://clinicalproblemsolving.com/dx-schema/ | surrogate_primary | 2026-06-06 | CPSolvers | 免费 schema 图库 — schema 走法 (=T04-S091) |
| T03-S005 | https://clinicalproblemsolving.com/ | surrogate_primary | 2026-06-06 | CPSolvers | VMR/schema 教学体系主站 (=T04-S090) |
| T03-S006 | https://www.youtube.com/@CPSolvers | verified_primary | 2026-06-06 | CPSolvers | VMR 全集免费视频 — think-aloud 范式 (=T04-S092) |
| T03-S007 | https://www.tandfonline.com/doi/abs/10.1080/10401334.2023.2226661 | surrogate_primary | 2026-06-06 | Teach Learn Med | Virtual Morning Report 国际社群化研究 (期刊 own pub) |
| T03-S008 | https://pmc.ncbi.nlm.nih.gov/articles/PMC1495095/ | verified_primary | 2026-06-06 | McGee (JGIM 2002) | Simplifying Likelihood Ratios — LR 定向检验 (=T02-S009/T04-S021) |
| T03-S009 | https://www.nejm.org/doi/full/10.1056/NEJM198005153022003 | verified_primary | 2026-06-06 | NEJM (Pauker/Kassirer) | threshold approach — 检查/治疗阈值决策 (=T04-S043) |
| T03-S010 | https://pubmed.ncbi.nlm.nih.gov/21248608/ | verified_primary | 2026-06-06 | Ely/Graber/Croskerry | Checklists to Reduce Diagnostic Errors 2011 (=T02-S034) |
| T03-S011 | https://pubmed.ncbi.nlm.nih.gov/35369942/ | verified_primary | 2026-06-06 | PubMed | Diagnostic Time-Outs to Improve Diagnosis (=T02-S037) |
| T03-S012 | https://www.cambridge.org/core/journals/canadian-journal-of-emergency-medicine/article/B768948819704516DBE325909A8D611E | secondary | 2026-06-06 | CJEM | cognitive forcing 无效对照试验 (=T02-S036) |
| T03-S013 | https://doi.org/10.1097/ACM.0000000000001421 | verified_primary | 2026-06-06 | Acad Med (Norman) | 2017 Causes of Errors — debiasing 干预证据弱 (=T04-S064) |
| T03-S014 | https://jamanetwork.com/journals/jama/fullarticle/186585 | surrogate_primary | 2026-06-06 | JAMA (Mamede) | 反思推理纠 availability bias RCT (=T04-S062) |
| T03-S015 | https://pmc.ncbi.nlm.nih.gov/articles/PMC6684533/ | verified_primary | 2026-06-06 | Mamede (AHSE) | deliberate reflection 程序最完整开放全文 (=T01-S030) |
| T03-S016 | https://pmc.ncbi.nlm.nih.gov/articles/PMC10083910/ | verified_primary | 2026-06-06 | PMC (Mamede/Schmidt) | deliberate reflection 奠基思想+实证综述 (founding ideas) |
| T03-S017 | https://pmc.ncbi.nlm.nih.gov/articles/PMC6265413/ | verified_primary | 2026-06-06 | PMC (Lambe et al) | guided reflection 对学生诊断准确率无效 — 去偏反方 |
| T03-S018 | https://pubmed.ncbi.nlm.nih.gov/31226996/ | verified_primary | 2026-06-06 | BMC Med Educ | SNAPPS 改善临床推理 RCT (=T02-S038) |
| T03-S019 | https://pubmed.ncbi.nlm.nih.gov/36625402/ | verified_primary | 2026-06-06 | PubMed | OMP+SNAPPS 系统综述 meta (=T02-S039) |
| T03-S020 | https://bmcmededuc.biomedcentral.com/articles/10.1186/s12909-023-04762-8 | surrogate_primary | 2026-06-06 | BMC Med Educ | chief resident 行为→有效 morning report 多中心质性研究 |
| T03-S021 | https://pubmed.ncbi.nlm.nih.gov/24742777/ | verified_primary | 2026-06-06 | Singh et al (BMJ QS) | 门诊误诊 ~5% 估计 + missed opportunity (=T01-S056) |
| T03-S022 | https://psnet.ahrq.gov/perspective/conversation-hardeep-singh-md-mph | verified_primary | 2026-06-06 | AHRQ PSNet | Singh 访谈 — SAFER Dx/e-trigger 测量哲学 (=T01-S057) |
| T03-S023 | https://www.ahrq.gov/diagnostic-safety/index.html | verified_primary | 2026-06-06 | AHRQ | 联邦诊断安全项目 .gov — SAFER Dx/工具母站 (=T04-S100) |
| T03-S024 | https://nap.nationalacademies.org/catalog/21794/improving-diagnosis-in-health-care | surrogate_primary | 2026-06-06 | NASEM/NAM | 2015 报告 — 诊断流程定义+反馈闭环 (=T04-S035) |
| T03-S025 | https://www.tamingthesru.com/blog/grand-rounds/cognitive-autopsy | verified_primary | 2026-06-06 | Univ of Cincinnati EM | Croskerry 亲讲 cognitive autopsy — M&M 升级版 (=T04-S010) |
| T03-S026 | https://pmc.ncbi.nlm.nih.gov/articles/PMC8815710/ | verified_primary | 2026-06-06 | JGIM | 内科版 cognitive autopsy 系统化提案 (=T04-S011) |
| T03-S027 | https://news.vt.edu/articles/2022/11/dhaliwalpreview_fralinbiomed_110422.html | verified_primary | 2026-06-06 | Virginia Tech | Dhaliwal 讲座原话 — follow-up 是免费教练/校准 (=T01-S005) |
| T03-S028 | https://dxexscholars.nam.edu/podcast/cognition-and-clinical-reasoning-with-dr-gurpreet-dhaliwal/ | verified_primary | 2026-06-06 | NAM DxEx Scholars | Dhaliwal 播客 — 资深=脚本库+校准 (=T01-S003) |
| T03-S029 | https://doi.org/10.1001/jama.2023.8288 | verified_primary | 2026-06-06 | JAMA (Kanjee/Rodman) | GPT-4 解 NEJM CPC (=T01-S037/T02-S015) |
| T03-S030 | https://doi.org/10.1001/jamanetworkopen.2024.40969 | verified_primary | 2026-06-06 | Goh et al (JAMA Netw Open) | LLM 诊断 RCT — AI alone 悖论 (=T01-S054/T02-S017) |
| T03-S031 | https://erictopol.substack.com/p/stump-the-medical-expert | verified_primary | 2026-06-06 | Eric Topol (Ground Truths) | GPT-4 vignette→真实外推批判 (=T02-S045) |
| T03-S032 | https://ai.nejm.org/doi/full/10.1056/AIdbp2500120 | secondary | 2026-06-06 | NEJM AI | 21 个前沿 LLM 临床推理 benchmark — DDx 最弱 (own pub) |
| T03-S033 | https://pmc.ncbi.nlm.nih.gov/articles/PMC13077515/ | verified_primary | 2026-06-06 | PMC | LLM 临床推理任务表现 — 早期诊断推理仍受限 |
| T03-S034 | https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11975833/ | verified_primary | 2026-06-06 | PMC | ambient AI 文档对认知负荷影响实证 |
| T03-S035 | https://pmc.ncbi.nlm.nih.gov/articles/PMC12973079/ | verified_primary | 2026-06-06 | PMC | ambient AI scribe 技术/影响/落地 narrative review 2025 |
| T03-S036 | https://www.openevidence.com/ | secondary | 2026-06-06 | OpenEvidence | AI 循证检索官网 (vendor, =T02-S023) |
| T03-S037 | https://www.degruyter.com/document/doi/10.1515/dx-2019-0019/html | surrogate_primary | 2026-06-06 | Diagnosis (Newman-Toker) | Big Three — can't-miss 优先级证据 (=T04-S073) |
| T03-S038 | https://www.mdcalc.com/about-us | secondary | 2026-06-06 | MDCalc | 决策规则聚合站 — 定向检验落地 (=T02-S005) |
| T03-S039 | https://ucsdim.com/wp-content/uploads/2019/11/clinical-reasoning-curriculum-diagnostic-schema-and-illness-scripts-handout.pdf | surrogate_primary | 2026-06-06 | UCSD IM Residency | 住院医推理 curriculum 讲义 — schema+illness script SOP (=T04-S040) |

**Bucket 计数**: verified_primary 24 / surrogate_primary 8 / secondary 7 = 39 条 (新引入约 6 条非种子源: S007/S016/S017/S020/S032/S033/S034/S035; 其余复用前三 track 已验证源)。一手层 24/39 ≈ 62% (达标 ≥55%)。无黑名单 (知乎/公众号/CSDN/KevinMD/G2/Capterra 全规避)。

---

## 总览（按 decay risk 分组）

### High decay (12-month-class) — 2 个

| Workflow | Trigger | Output | Last_updated | 资深差异 |
|---------|---------|--------|-------------|---------|
| WF6. AI 增强诊断推理工作流 | 卡在鉴别/想要第二意见/查证据/释放文档带宽 | 更全的 DDx 候选 + 循证锚定 + 更多认知带宽, **AI 不作最终诊断** | 2026-05 | 资深把 AI 当「假想反方」而非答案机; 用 guardrails 防自动化偏倚 |
| WF7. 诊断 AI 在临床落地的评估/采纳工作流 | 团队/机构要不要把某 AI 诊断工具纳入流程 | 采纳/拒绝决策 + 监测计划 | 2026-05 | 资深要求真实前瞻结局证据, 不被 vignette 数字说服 |

### Medium decay — 1 个

| Workflow | Trigger | Output | Last_updated | 资深差异 |
|---------|---------|--------|-------------|---------|
| WF5. 诊断质检 / 校准反馈环 | 一次诊断推理结束后, 想知道「做得好不好」 + 系统级找漏诊 | 推理质量判据评分 + missed opportunity 清单 + 个人校准 | 2025 (SAFER Dx/e-trigger 工具持续迭代) | 资深主动建反馈回路 (closed-loop follow-up), 不等坏结局来教育自己 |

### Low decay — 4 个

| Workflow | Trigger | Output | Last_updated | 资深差异 |
|---------|---------|--------|-------------|---------|
| WF1. 核心诊断推理 SOP (床旁单病例) | 接诊一个未分化主诉的病人 | working diagnosis + assessment&plan + 安全网 | 2006 (Bowen 文体, 30 年稳态) | 资深前几分钟生成定向假设, 跳过穷举式数据采集, 直接驱动针对性病史 |
| WF2. 教学工作流: morning report 渐进披露 | 带教/晨会要训练一群学员的推理 | 学员练成 one-liner→schema→DDx 标准动作 | 2023 (VMR 全球化) | 资深主持者控制信息披露节奏, 在 labs 前逼出鉴别 |
| WF3. 带教单兵工作流: SNAPPS / One-Minute Preceptor | 门诊/查房, 一个学员汇报一个病人 | 学员外显推理 + 暴露不确定性 + 当场反馈 | 2019 (meta 证据) | 资深用 OMP 一分钟给出微教学 + 纠错, 不接管病例 |
| WF4. 去偏 / 元认知工作流 (诚实: 证据弱) | 高风险/不确定病例收尾前, 想防认知误诊 | 重审过的鉴别 + (或) 修正的诊断 | 2017-2021 (论战未决) | 资深更投资知识/样例库, 把「反思」用在复杂/被误导的病例而非每例 |

---

## 工作流详细条目

### WF1. 核心诊断推理 SOP（床旁单病例 — 本 skill 的中枢工作流）

- **One-liner**: 从「一个有未分化主诉的病人坐在你面前」推进到「一个有安全网的 working diagnosis + assessment & plan」的六步认知操作链 — 这是临床推理的主干, 其余工作流都是它的教学版/质检版/AI 增强版。
- **Trigger**: 接诊任一新病人 (尤其全科/急诊/大内科以未分化主诉为生的场景)。
- **Output**: one-liner (problem representation) + prioritized DDx + 假设定向检验结果 + working diagnosis + 显式安全网 (red flags 交代 / test of time / test of treatment) + 反馈校准计划。
- **入门 SOP（minimum viable steps）**:
  1. **数据采集**: 病史为王 (主诉+HPI+针对性 ROS) → 循证体检 (按 LR 选高产体征, 非全套) → 针对性检验/影像。inputs=病人主诉; outputs=结构化临床发现。(evidence: [T03-S001, T03-S008])
     - **跳过后果**: 漏关键病史/红旗 (如 chest pain 不问放射/活动相关) → 后续整条推理链建在错误数据上, 是误诊的上游源头 (evidence: [T03-S001])
  2. **问题表征 (problem representation)**: 把杂乱病例压成一句 **one-liner** — 年龄/性别 + 关键风险背景 + 用**成对语义限定词** (急/慢, 局灶/弥漫, 单发/多发) 抽象化的综合征。inputs=临床发现; outputs=一句话病人。(evidence: [T03-S001, T03-S002])
     - **跳过后果**: 不抽象成 one-liner → 鉴别诊断生成失焦, 抓不住 pivot, 学员直接背一长串病名 (Bordage 实证: 用语义限定词者诊断更准) (evidence: [T03-S002])
  3. **鉴别诊断生成 (DDx)**: 沿 one-liner 的 pivot 走 **schema** (CPSolvers 按 pivot 症状分支) 或用 **VINDICATE-M / 解剖定位法**穷举病因, 然后按 **「常见 × 致命不能漏 (can't-miss)」双轴排序**。inputs=one-liner; outputs=排序 DDx。(evidence: [T03-S004, T03-S037])
     - **跳过后果**: 不系统生成→漏诊 (尤其漏 can't-miss: Big Three=血管事件/感染/肿瘤占严重伤害约 75% [估计, Newman-Toker])(evidence: [T03-S037]); 只想一个病→premature closure / search satisficing
  4. **假设定向检验**: 按 **似然比 (LR)** 选「最能改变验后概率」的检查 (不是把能查的都查), 用 **阈值决策** (Pauker-Kassirer test/treatment threshold) 判断是否跨过检查阈值/治疗阈值。inputs=排序 DDx; outputs=检查结果+更新的概率。(evidence: [T03-S008, T03-S009])
     - **跳过后果**: 不按 LR 选→ VOMIT (Victim Of Medical Imaging Technology) / incidentaloma 瀑布 / 过度检查; 不算阈值→「会查但不会停」(evidence: [T03-S009])
  5. **Working diagnosis + 安全网**: 给出当前最可能诊断 + 显式安全网三件套: red flags 交代 (「出现 X 立刻回来」) / **test of time** (时间是诊断工具, 安排复诊看演变) / **test of treatment** (经验性治疗的反应本身是诊断信息)。inputs=检验结果; outputs=诊断+计划+不确定性沟通。(evidence: [T03-S021, T03-S024])
     - **跳过后果**: 不留安全网→ 把诊断不确定性当确定性, 病人带着未识别的恶化风险离开 = missed opportunity 的高发点 (evidence: [T03-S021])
  6. **反馈校准**: 安排 closed-loop follow-up; 把诊断结果与最初判断对照 (我对了吗? 哪步偏了?); 错例进 M&M / diagnostic timeout / cognitive autopsy。inputs=随访结局; outputs=个人校准+脚本库更新。(evidence: [T03-S027, T03-S028])
     - **跳过后果**: 没有反馈环→直觉永远校准不好 (Kahneman: 专家直觉只在「高规律性+有反馈」环境可信); 资深医生最痛恨的就是「不知道病人后来怎么样了」(evidence: [T03-S027])
- **资深路径（差异点）**:
  - **skip**: 资深**跳过穷举式数据采集** — 接诊前几分钟 (Elstein: hypothetico-deductive) 就生成 3-5 个假设, 之后病史/体检全是**定向**采集 (为检验假设), 而非按教科书 ROS 逐项问 → 同样信息量, 时间减半 (evidence: [T03-S001], Elstein 谱系 T04-S001)
  - **skip**: 资深对典型病 (aunt Minnie / 一眼认出) 直接走 System 1 模式识别, **跳过显式 schema 走法** — illness script 库大, 脚本匹配即诊断 (evidence: [T03-S028])
  - **optimize**: 资深的 DDx 排序更准 — 不是想得更多, 而是**校准更好** (验前概率估得准, can't-miss 优先级判得准)。这是「资深≠更会分析, 而是脚本库更大+校准更好」的核心 (evidence: [T03-S028])
  - **add**: 资深**主动建反馈环** — Dhaliwal:「follow-up 是免费的教练」, 刻意追踪自己诊断的结局来校准直觉; 新手往往诊断完就忘 (evidence: [T03-S027])
  - **add**: 资深在收尾前对**高风险/不确定**病例做 diagnostic timeout (「最坏情况排除了吗?」), 但对典型病不做 (节省认知资源) (evidence: [T03-S011])
- **近期变化**（近 12 个月）: 核心 SOP 文体自 Bowen 2006 NEJM 起 **近 20 年无重大变化 (行业稳态)**; 最近一次显著外部冲击是 AI 增强 (见 WF6), 但它叠加在此 SOP 之上而非替代。`decay risk: low`
- **典型耗时**: 入门 SOP 单病例数十分钟 (含查 LR/规则); 资深路径几分钟 (脚本匹配)。
- **关键工具 (Track 02)**: 似然比+Fagan nomogram (必备) / 临床决策规则 via MDCalc (必备) / JAMA RCE (体征 LR) / schema (CPSolvers) / VINDICATE / can't-miss×common 双轴。
- **关键人物 (Track 01)**: Dhaliwal (SOP 整体范式 + 反馈校准); Bowen (problem representation 教学); Pauker-Kassirer (阈值); McGee (LR 定向检验); Newman-Toker (can't-miss/Big Three)。
- **常见失败模式 (CLI 化, actionable)**:
  - **病史采集偷工 → 整条链崩**: 不问关键红旗就跳到检查 — 自检「我问够了驱动鉴别所需的病史吗?」
  - **跳过 one-liner 直接列病名**: 不抽象成 problem representation → DDx 失焦; 自检「我能用一句话+成对语义限定词概括这个病人吗?」
  - **DDx 只想 common 漏 can't-miss**: 没过一遍致命轴 — 自检「这个综合征的 can't-miss (血管/感染/肿瘤) 我排了吗?」
  - **把能查的都查 (VOMIT)**: 不按 LR 选检查 → incidentaloma 瀑布; 自检「这个检查的结果会改变我的下一步行动吗? (阈值检验)」
  - **不留安全网就放病人走**: 把不确定性当确定性 — 自检「我交代红旗了吗? 安排复诊/经验性治疗反应观察了吗?」
  - **诊断完就忘 (无反馈)**: 不追踪结局 → 直觉永不校准; 自检「我会知道这个病人后来怎么样吗?」
- **来源 (≥3)**: [Primary] Bowen NEJM 2006 (T03-S001); [Primary] Bordage JGIM (T03-S002); [Primary] McGee LR (T03-S008); [Primary] Pauker-Kassirer 阈值 (T03-S009); [Reference] Dhaliwal 讲座/播客 (T03-S027, T03-S028)。
- **Last_updated**: 2026-06-06 (文体本身 2006; AI 增强层 2026)
- **Decay risk**: low (核心 SOP 30 年稳态; can't-miss 名单/LR 数值随研究微调)

---

### WF2. 教学工作流: Morning Report 渐进披露 / Virtual Morning Report / CPC

- **One-liner**: 把一个真实病例**按信息块逐步披露** (主诉→HPI→体检→labs→影像), 让一群学员在每个披露点出声推理, 在拿到 labs 前就被逼出鉴别 — 训练 WF1 推理动作的群体教学版。
- **Trigger**: 晨会/查房/CPC 要训练一批学员的诊断推理 (不是教某个病的知识, 是教「怎么想」)。
- **Output**: 学员练成「听到一段→更新 one-liner→调 schema→压 can't-miss」的标准动作; 一个被集体推理过的病例。
- **入门 SOP（minimum viable steps）**:
  1. **选案 + 定学习目标**: chief resident 选一个推理价值高 (非罕见炫技) 的近期病例, 写明这堂课要练的推理点 (如 base-rate / 某 schema)。(evidence: [T03-S020])
     - **跳过后果**: 选了「奇病炫技」案 → 学员学到的是「记住这个罕见病」而非可迁移的推理动作 (evidence: [T03-S020])
  2. **渐进披露设计**: 把病例切成块, 物理上让学员先拿到 HPI/ROS/PE, 在 labs/影像之前就要承诺一个 DDx。(evidence: [T03-S020], 渐进披露=NEJM CPS 文体 T03-S003)
     - **跳过后果**: 一次给全部信息 → 学员后视偏倚 (看到答案再倒推), 没练到「信息不全时怎么推」(evidence: [T03-S003])
  3. **每个披露点逼出推理**: 主持者在每块后问「你的 one-liner? 你的鉴别? 下一步想要什么信息?」— think-aloud。(evidence: [T03-S005, T03-S006])
     - **跳过后果**: 学员被动听 → 没有外显推理就没有可纠正的推理 (evidence: [T03-S006])
  4. **收尾点评**: 揭晓诊断, 复盘「哪步推理对/偏」, 提炼可带走的 schema/script。
     - **跳过后果**: 不复盘 → 病例变成 trivia, 推理点没沉淀
- **资深路径（差异点）**:
  - **optimize**: 资深主持者**精控信息披露节奏** — 知道在哪一块停下来逼鉴别最有教学张力 (通常在 labs 之前), 把「dots connect」的悬念用到位 (CPSolvers RLR 范式) (evidence: [T03-S005])
  - **add**: 资深主持者营造**心理安全** — 让学员敢说错的鉴别 (chief resident 行为研究: facilitation + safe environment 是有效晨会四主题之一) (evidence: [T03-S020])
  - **add (VMR 全球化)**: CPSolvers 把晨会搬上线 (Virtual Morning Report), 用 schema 图实时标注, 形成 30+ 国际团队的社群化推理学习 (evidence: [T03-S005, T03-S007])
- **近期变化**（近 12 个月）: 2020 起 (COVID 推动) **Virtual Morning Report 全球化**, 2023 研究确认其形成跨国推理社群 (evidence: [T03-S007]); 渐进披露文体本身 (NEJM CPS/CPC) 数十年稳态。`decay risk: low`
- **典型耗时**: 单场 45-60 分钟。
- **关键工具 (Track 02)**: schema (CPSolvers 免费图库) / problem representation 训练 / NEJM CPS+CPC 作为渐进披露病例源。
- **关键人物 (Track 01)**: Geha & Manesh (CPSolvers VMR/schema, RLR 实时推理秀); Kassirer (NEJM CPS 渐进披露文体母本); CPC = MGH 百年正典。
- **常见失败模式 (actionable)**:
  - **炫技选案**: 选罕见病博眼球 — 自检「这个案教的是可迁移推理动作还是一个孤立冷知识?」
  - **信息一次给全**: 失去渐进披露价值 — 自检「我在 labs 前逼学员承诺 DDx 了吗?」
  - **主持者自己讲完**: 学员没 think-aloud — 自检「每个披露点我让学员先说了吗?」
  - **羞辱式 pimping**: 心理不安全, 学员不敢猜 — 自检「学员敢在这里说错吗?」
- **来源 (≥3)**: [Primary] chief resident 行为研究 BMC (T03-S020); [Primary] NEJM CPS 文体 (T03-S003); [Reference] CPSolvers VMR 主站+视频 (T03-S005, T03-S006); [Primary] VMR 国际社群研究 (T03-S007)。
- **Last_updated**: 2026-06-06 (VMR 全球化 2020-2023; 渐进披露文体数十年)
- **Decay risk**: low

---

### WF3. 带教单兵工作流: SNAPPS / One-Minute Preceptor (OMP)

- **One-liner**: 把「一个学员向你汇报一个病人」从「念事实」改造成「外显推理 + 主动暴露不确定性 + 当场微教学」的结构化脚本 — 门诊/查房高频的一对一带教工作流。
- **Trigger**: 门诊或查房, 学员汇报一个他接诊的病人, 时间紧 (几分钟)。
- **Output**: 学员暴露了自己的推理与不确定点; 带教者给出针对性反馈; 病例推进。
- **入门 SOP（SNAPPS 六步, 学员主导）**:
  1. **S**ummarize: 学员简要总结病史与发现 (→ 练 problem representation)
  2. **N**arrow: 把鉴别**收窄到 2-3 个**最可能/最该排的 (→ 练 DDx 排序)
  3. **A**nalyze: 逐一比较这几个鉴别 (→ 练假设检验思维)
  4. **P**robe: 学员**主动向带教者提问**自己不确定/不懂的点 (→ 暴露知识缺口)
  5. **P**lan: 提出管理计划
  6. **S**elect: 选一个自学议题带走
  - **跳过后果 (整体)**: 退回传统「学员念全套病史→带教者直接给答案」→ 学员的推理与不确定性永远不可见, 带教者无从纠正 (SNAPPS RCT: SNAPPS 组诊断假设更清晰、主动发起管理讨论多约 20%)(evidence: [T03-S018])
- **入门 SOP（One-Minute Preceptor 五步, 带教者主导, 用于学员汇报后）**:
  1. 让学员先**承诺一个诊断/计划** (get a commitment)
  2. **问支持依据** (probe for supporting evidence)
  3. 教**一条通则** (teach a general rule)
  4. **正反馈** (reinforce what was done well)
  5. **纠错** (correct mistakes)
  - **跳过后果**: 不先要 commitment 就直接讲 → 学员没暴露思路, 微教学打不准 (OMP+SNAPPS meta: 二者均改善临床推理)(evidence: [T03-S019])
- **资深路径（差异点）**:
  - **optimize**: 资深带教者把 OMP 压到**真的一分钟** — 一句通则切中学员当下缺口, 不展开长讲 (evidence: [T03-S019])
  - **skip**: 资深**不接管病例** — 抵住「我来问病人」的冲动, 让学员承担推理 (新手带教者最容易犯的就是越俎代庖)
  - **add**: 资深在 Probe 环节**主动追问学员的不确定性** ("what doesn't fit?"), 把暴露盲区变成习惯 (evidence: [T03-S018])
- **近期变化**（近 12 个月）: **无重大变化 (稳态)**; SNAPPS (Wolpaw) / OMP (Neher) 是 1990s-2000s 工具, 2019 meta 确认有效后进入稳态。`decay risk: low`
- **典型耗时**: 单次 1-5 分钟。
- **关键工具 (Track 02)**: SNAPPS / OMP (教学框架, 必备层)。
- **关键人物 (Track 01)**: 教育认知派生态 (与 Bowen 教学法、CPSolvers think-aloud 呼应)。
- **常见失败模式 (actionable)**:
  - **带教者接管病例**: 自检「我是在让学员推理, 还是在替他推理?」
  - **不要 commitment 直接给答案**: 自检「学员承诺一个诊断了吗?」
  - **通则讲太长**: OMP 退化成讲座 — 自检「我的通则一句话说得完吗?」
  - **跳过 Probe/不确定性**: 学员盲区没暴露 — 自检「我问了 what doesn't fit 吗?」
- **来源 (≥3)**: [Primary] SNAPPS RCT BMC (T03-S018); [Primary] OMP+SNAPPS meta (T03-S019); [Reference] Track 02 教学框架条目。
- **Last_updated**: 2026-06-06 (工具 1990s-2000s; meta 证据 2019)
- **Decay risk**: low

---

### WF4. 去偏 / 元认知工作流（诚实标注: 干预证据弱 — 本行最核心论战）

- **One-liner**: 在诊断收尾前刻意插入一个元认知动作 (暂停/反思/套清单) 来对抗认知误诊 — **但这套工作流的防错效果在对照试验中弱/混合, 是 Croskerry「去偏可教」派 vs Norman/Sherbino「知识才是解药」派的核心战场, 双方证据都必须诚实保留**。
- **Trigger**: 高风险或诊断不确定的病例收尾前; 怀疑自己/团队有锚定/可得性/过早闭合。
- **Output**: 重审过的鉴别清单; 有时是被修正的诊断; 个人/团队的偏倚意识。
- **入门 SOP（候选动作, 注意每个的证据强度不同）**:
  1. **Diagnostic timeout**: 收尾前刻意暂停, 问「最坏情况 (worst-case / can't-miss) 排除了吗? 有什么不符合 (what doesn't fit)? 会不会不止一个病 (Hickam)?」— Type-2 executive override。(evidence: [T03-S011])
     - **证据**: 概念合理, 但 timeout/checklist 防错 RCT「mixed」, 部分未证明有效 (evidence: [T03-S011])
  2. **Ely 三类 checklist**: 通用认知 checklist + 鉴别 checklist + 特定病陷阱 checklist。(evidence: [T03-S010])
     - **证据**: Ely 2011 提出; 试点 RCT 效果混合 (evidence: [T03-S010])
  3. **Cognitive forcing strategy**: 针对特定偏倚的主动对策 (「想到 X 时强制问 what else」)。(evidence: [T03-S012])
     - **证据 (反方硬)**: 对照试验显示 cognitive forcing 在减少推理偏倚上**无效** (evidence: [T03-S012]); Norman 2017: debiasing 干预证据弱, 错误主因是知识缺口 (evidence: [T03-S013])
  4. **Deliberate reflection (Mamede 程序 — 证据最强的一项)**: 结构化对照反思, **不是泛泛「多想想」**: (a) 列出当前诊断的支持/反对证据 → (b) 生成替代诊断 → (c) 对每个替代逐一列支持/反对 → (d) 再综合决定。(evidence: [T03-S014, T03-S015, T03-S016])
     - **证据 (正方最硬)**: Mamede RCT 证明 deliberate reflection 能纠正实验诱导的 availability bias, **尤其在复杂病例/被偏倚误导时显效** (evidence: [T03-S014, T03-S016]); **但** 对简单病例无增益, 且对医学生的 guided reflection 有阴性结果 (evidence: [T03-S017])
  - **跳过后果 (整体)**: 对高风险病例完全不做任何重审 → premature closure / anchoring 直接导致误诊。**但 caveat**: 机械套用反而可能成另一种形式化/自动化 (evidence: [T03-S013])
- **资深路径（差异点）**:
  - **optimize**: 资深**选择性使用** reflection — 只在复杂/不确定/被误导的病例上做 deliberate reflection (那是它唯一有证据显效的场景), 对典型病不浪费认知资源 (evidence: [T03-S015, T03-S016])
  - **skip**: 成熟资深/批判派**不依赖偏倚清单** — Norman/Sherbino 处方: 与其教 30 种偏倚名, 不如**堆知识 + mixed practice + 全病例分析** (knowledge is the cure) (evidence: [T03-S013])
  - **add**: 资深把反思**做成结构化程序** (列证据→生成替代→逐一对照) 而非「再想想」, 因为只有结构化版本有证据 (evidence: [T03-S015])
- **近期变化**（近 12 个月）: **论战未决, 是稳态的张力** — 最近一次显著节点: Norman 2017 把 debiasing 批判定型, Mamede 团队 2020-2023 持续产出 deliberate reflection 阳性 RCT (复杂病例) 作为部分反例。**没有一方"赢"**。`decay risk: low (概念稳, 效果证据持续争论)`
- **典型耗时**: timeout 数十秒-几分钟; deliberate reflection 单病例几分钟。
- **关键工具 (Track 02)**: diagnostic timeout / Ely checklist / cognitive forcing (效果争议) / deliberate reflection (证据最强)。
- **关键人物 (Track 01)**: Croskerry (去偏可教派 + cognitive autopsy); Norman/Sherbino (批判派, knowledge is the cure); Mamede (deliberate reflection 实证奠基); Graber (诊断错误科学)。
- **常见失败模式 (actionable)**:
  - **把去偏清单当万灵药**: 多个 RCT 显示 checklist/forcing 防错弱或无效 — 自检「我是把它当唯一保险还是众多动作之一?」
  - **泛泛"再想想"冒充 deliberate reflection**: 没有结构就没有证据 — 自检「我列了替代诊断并逐一对照证据了吗?」
  - **对每个病都做 timeout**: 认知资源耗尽 + 形式化 — 自检「这个病例真的复杂/高风险到需要 override 吗?」
  - **以为背熟偏倚名就不会犯**: 偏倚是后视标签, 不可证伪 — 自检「我是在补知识缺口还是只在贴偏倚标签?」
- **来源 (≥3)**: [Primary] Diagnostic Time-Outs (T03-S011); [Primary] Ely checklist (T03-S010); [Primary] cognitive forcing 无效 RCT (T03-S012); [Primary] Norman 2017 (T03-S013); [Primary] Mamede deliberate reflection (T03-S014, T03-S015, T03-S016); [Primary] guided reflection 阴性 (T03-S017)。
- **Last_updated**: 2026-06-06 (Norman 2017 / Mamede 2020-2023; 论战持续)
- **Decay risk**: low (概念稳, 但证据持续争论 — 是本 skill 必须诚实保留的张力)

---

### WF5. 诊断质检 / 校准反馈环（怎么判断一次诊断推理"做得好"+ 系统找漏诊）

- **One-liner**: 两个尺度的质检 — **个人尺度**: 用一组判据评一次诊断推理是否做得好; **系统尺度**: 用 SAFER Dx / e-trigger / M&M / cognitive autopsy 找出错失的诊断机会并反哺校准。
- **Trigger**: 一次诊断推理结束想自评; 或机构要系统性发现漏诊 (不等坏结局自己冒出来)。
- **Output**: 推理质量评分 + missed opportunity 清单 + 个人/团队校准。
- **入门 SOP（个人尺度: 一次推理"做得好"的判据 — 直接对应 WF1 六步）**:
  1. **Problem representation 准不准**: one-liner 抓住 pivot 了吗? 语义限定词对吗? (evidence: [T03-S001, T03-S002])
  2. **DDx 有没有漏 can't-miss**: 致命轴 (Big Three: 血管/感染/肿瘤) 过了吗? (evidence: [T03-S037])
  3. **检验是否按 LR / 阈值**: 开的检查会改变行动吗? 还是 VOMIT? (evidence: [T03-S008, T03-S009])
  4. **是否留安全网**: red flags 交代 + test of time/treatment 安排了吗? (evidence: [T03-S021])
  5. **是否反馈闭环**: 安排了能知道结局的 follow-up 吗? (evidence: [T03-S027])
  - **跳过后果**: 不自评 → 「我感觉诊断对了」无法验证, 直觉校准停滞
- **入门 SOP（系统尺度: 找漏诊）**:
  1. **e-trigger 筛查**: 用 EHR 数据跑算法找「异常返诊/异常未随访/红旗未跟进」模式 (Singh 方法核心)。(evidence: [T03-S022])
  2. **SAFER Dx 回溯评审**: 对触发的病例回溯病历, 判定是否存在「missed opportunity (可干预的错失诊断机会)」。(evidence: [T03-S021, T03-S023])
  3. **M&M / cognitive autopsy**: 错例不只问「错在哪一步流程」, 升级到「错在哪一个**认知动作**」(Croskerry cognitive autopsy)。(evidence: [T03-S025, T03-S026])
  4. **反哺**: 把发现的模式回灌到个人校准与系统改进 (NAM 2015: 诊断流程必须有反馈回路)。(evidence: [T03-S024])
  - **跳过后果**: 等病人投诉/诉讼/尸检才知道漏诊 → 学习滞后且样本有偏 (只看到伤害严重的)
- **资深路径（差异点）**:
  - **add**: 资深**主动建 closed-loop follow-up** — Dhaliwal:「follow-up 是免费教练」, 不等系统推送, 自己追结局来校准 (evidence: [T03-S027, T03-S028])
  - **optimize**: 资深做 M&M 时用 **cognitive autopsy** (定位到具体认知动作/偏倚) 而非只问流程, 复盘更深 (evidence: [T03-S025])
  - **add**: 资深关注**校准 (calibration)** 而非只看准确率 — 自信度与实际正确率的吻合度, 是「资深≠更会分析而是校准更好」的可测量面 (evidence: [T03-S028])
- **近期变化**（近 12 个月）: SAFER Dx / e-trigger / AHRQ 诊断安全工具**持续迭代** (2025 Singh 团队发 20 年综述定路线图); cognitive autopsy 2022 被内科系统化提案接力。`decay risk: medium (测量工具与算法持续演进)`
- **典型耗时**: 个人自评单病例几分钟; 系统 e-trigger+回溯评审=机构级项目。
- **关键工具 (Track 02)**: SAFER Dx / e-trigger (Singh); Ely checklist / diagnostic timeout (重审); cognitive autopsy 模板。
- **关键人物 (Track 01)**: Singh (SAFER Dx/e-trigger/missed opportunity); Graber (诊断错误分类); Croskerry (cognitive autopsy); Dhaliwal (个人校准/follow-up); Newman-Toker (Big Three 优先级)。
- **常见失败模式 (actionable)**:
  - **只看准确率不看校准**: 自检「我自信度和实际正确率吻合吗?」
  - **M&M 只问流程不问认知**: 错失偏倚级复盘 — 自检「我定位到具体认知动作了吗 (cognitive autopsy)?」
  - **等坏结局来教育**: 学习样本有偏 — 自检「我有不依赖伤害发生的找漏诊机制吗 (e-trigger)?」
  - **e-trigger 假阳性淹没**: 审计负担 — caveat: missed opportunity 判定有 hindsight bias, 不可全消 (evidence: [T03-S021])
- **来源 (≥3)**: [Primary] Singh ~5%/missed opportunity (T03-S021); [Reference] Singh 测量哲学访谈 (T03-S022); [Primary] AHRQ 诊断安全 (T03-S023); [Primary] cognitive autopsy (T03-S025, T03-S026); [Reference] Dhaliwal 校准 (T03-S027, T03-S028)。
- **Last_updated**: 2026-06-06 (SAFER Dx 持续迭代; 2025 Singh 20 年综述)
- **Decay risk**: medium

---

### WF6. AI 增强诊断推理工作流（2023-2026 — Decay risk: HIGH, 数字截至 2026-06-06）

- **One-liner**: 把 LLM/AI 嵌入 WF1 的特定环节做「认知假体」— 鉴别头脑风暴、推理质疑反方、循证检索、ambient scribe 释放文档带宽 — 在 guardrails 下增强而非替代医生推理; **明确: AI 不当最终诊断**。
- **Trigger**: 鉴别卡壳想扩列; 想要一个「假想反方」质疑自己; point-of-care 查证据; 文档负担挤占问诊/思考带宽。
- **Output**: 更全的 DDx 候选 (人工筛) + 循证锚定答案 + 更多认知带宽; **不是**一个由 AI 拍板的诊断。
- **入门 SOP（minimum viable steps + 每步的 guardrail）**:
  1. **鉴别头脑风暴**: 给 LLM (GPT-4 等) one-liner, 让它扩列「我可能漏了什么」。guardrail: 输出是**清单不是答案**, 逐条人工核实。(evidence: [T03-S029, T03-S031])
     - **跳过后果**: 不用→ 新手 DDx 漏罕见/想不到的病 (LLM 命中率在病例集上高于人, 但 caveat 见下)
  2. **推理质疑 (devil's advocate)**: 让 AI 当反方挑战你的 working diagnosis ("what argues against this?")。guardrail: 用它**对抗自己的锚定**, 不是找背书。(evidence: [T03-S031])
  3. **循证检索 (OpenEvidence 等)**: point-of-care 查验前概率/诊断标准/最新证据, 只引同行评议源。guardrail: 仍可能引用错配, **核对原文**。(evidence: [T03-S036])
  4. **Ambient scribe**: AI 自动记录问诊, 医生从打字解放, 把认知带宽还给倾听与推理。guardrail: 必须**核对 AI 笔记的准确性** (AI 笔记 thoroughness/organization 优于人, 但 succinctness/accuracy/一致性更差)。(evidence: [T03-S034, T03-S035])
     - **跳过后果**: 文档负担持续挤占问诊→ 倾听质量降→ 诊断质量降 (实证: 94% 临床医生报告 ambient scribe 降低就诊时认知负荷, 97% 报告文档负担下降 [估计, 单研究])(evidence: [T03-S034, T03-S035])
  5. **人工综合 + 留安全网**: 医生整合 AI 输入与自己的推理, 做最终判断, 接 WF1 step5/6。guardrail: **AI 绝不拍板**。
     - **跳过后果**: 把 AI 输出当最终诊断→ 幻觉/编造引用直接进病历; 长期外包推理→ 去技能化 (deskilling)
- **资深路径（差异点）**:
  - **optimize**: 资深把 AI 当**假想反方/认知假体**而非答案机 — 用它扩鉴别/挑漏洞, 但保留判断权 (evidence: [T03-S031])
  - **add**: 资深主动设 **guardrails 防自动化偏倚** — 不因 AI 没提示就不查 (omission bias), 不因 AI 建议就照做 (commission bias)
  - **skip**: 资深对典型病**跳过 AI** — 脚本匹配已够, AI 增量为零且引入幻觉风险
  - **add (悖论意识)**: 资深知道「医生+AI ≤ AI alone」(Goh 2024) 是**协作界面问题**, 不代表该让 AI 自主行医 — 不被悖论误导成「让开给 AI」(evidence: [T03-S030])
- **近期变化**（近 12 个月, HIGH decay, last_checked 2026-06-06）:
  - **2025 起 ambient scribe 主流化**: 从实验走向规模部署, 认知负荷/文档负担下降实证累积 (narrative review 2025)(evidence: [T03-S035])
  - **2025-2026 LLM 推理模型迭代**: reasoning-optimized 模型 (o1 类) 在临床推理 benchmark 得分最高, **但鉴别诊断 (DDx) 仍是最弱环节**, 早期诊断推理不能无监督用于患者面对面决策 (NEJM AI 2025 / PMC 2025)(evidence: [T03-S032, T03-S033])
  - **OpenEvidence 等检索类爆发**: 据报道 >40% 美国医生使用 (vendor/媒体, caveat)(evidence: [T03-S036])
  - 触发事件类型: 新模型 (o1/reasoning) + 新产品 (ambient scribe 规模化) + 新证据 (benchmark)
  - 当前采用率: 检索/scribe 类采用快; **诊断拍板类未临床落地** (监管+前瞻证据缺口)
- **典型耗时**: 每个增强点几秒-几分钟 (叠加在 WF1 上)。
- **关键工具 (Track 02, 全 high decay)**: LLM 诊断助手 (GPT-4/o1); OpenEvidence (循证检索); AMIE/Glass Health (实验); ambient scribe。
- **关键人物 (Track 01)**: Rodman (临床侧 AI 研究核心, JAMA 2023→Science 2026); Topol (证据守门, 「没前瞻证据别上临床」); Goh (AI alone 悖论)。
- **常见失败模式 (actionable)**:
  - **把 AI 清单/输出当最终诊断**: 幻觉/编造引用进病历 — 自检「我逐条核实了吗? AI 是建议还是答案?」
  - **自动化偏倚 (automation bias)**: 照错建议做 (commission) 或 AI 没提示就不做 (omission) — 自检「我会独立想到这个吗?」
  - **去技能化 (deskilling)**: 长期外包推理致判断力萎缩 — 自检「典型病我还会自己推吗?」
  - **把 vignette/CPC 数字当真实性能**: CPC 是干净书面病例, 真实混乱数据下表现可能大降 (作者自陈 + Topol 批判)(evidence: [T03-S029, T03-S031])
  - **不核对 ambient 笔记**: AI 笔记简洁性/准确性/一致性弱于人 — 自检「我核对了这份 AI 笔记吗?」
- **来源 (≥3)**: [Primary] Kanjee/Rodman JAMA (T03-S029); [Primary] Goh RCT (T03-S030); [Primary] Topol 批判 (T03-S031); [Secondary] NEJM AI benchmark (T03-S032); [Primary] LLM 推理任务 PMC (T03-S033); [Primary] ambient 认知负荷 (T03-S034, T03-S035)。
- **Last_updated**: 2026-06-06
- **Decay risk**: **high** (12 月内 >40% 概率显著改写; master skill 更新时本节优先刷新)

---

### WF7. 诊断 AI 在临床落地的评估 / 采纳工作流（Decay risk: HIGH）

- **One-liner**: 当团队/机构面对「要不要把某 AI 诊断工具纳入流程」时, 一套不被 vignette 数字诱惑、要求真实前瞻结局证据、并配监测计划的采纳决策工作流。
- **Trigger**: 一个新 AI 诊断/检索/scribe 工具进入视野, 有人主张采纳。
- **Output**: 采纳/拒绝/试点决策 + 部署后监测计划。
- **入门 SOP（minimum viable steps）**:
  1. **看证据级别**: 是 vignette/CPC 上的数字, 还是真实临床前瞻结局? guardrail: vignette→真实外推**未验证** (Topol 公开点名缺口)。(evidence: [T03-S031])
     - **跳过后果**: 被「AI 在 CPC 上超医生」忽悠, 真实环境表现可能大降 (evidence: [T03-S029])
  2. **定角色边界**: 这工具是认知假体 (扩鉴别/检索/scribe) 还是想拍板诊断? guardrail: **拍板类不上临床** (监管+证据缺)。(evidence: [T03-S030, T03-S033])
  3. **设 guardrails**: 防自动化偏倚 (commission/omission) + 防去技能化的监测指标。(evidence: [T03-S034])
  4. **试点 + 监测**: 小范围试点, 监测真实结局与未预期伤害, 再决定推广。
     - **跳过后果**: 全量上线无监测 → 自动化偏倚/幻觉错误规模化
- **资深路径（差异点）**:
  - **optimize**: 资深直接问「**有真实前瞻结局证据吗?**」一句话筛掉绝大多数只有 vignette 数字的产品 (evidence: [T03-S031])
  - **skip**: 资深**跳过「AI alone > 医生」营销话术** — 知道那是协作界面问题, 不是让 AI 自主行医的理由 (evidence: [T03-S030])
  - **add**: 资深要求**部署后监测去技能化** — 不只看上线效率, 看长期是否侵蚀临床判断 (evidence: [T03-S034])
- **近期变化**（近 12 个月, HIGH decay）: 检索/scribe 类已大规模落地; 诊断拍板类仍卡在前瞻证据+监管 (2025-2026 benchmark 显示 DDx 仍弱)。触发: 产品爆发速度 >> 监管/证据速度。`decay risk: high`
- **典型耗时**: 机构级决策数周-数月。
- **关键工具 (Track 02)**: 同 WF6 (全 high decay)。
- **关键人物 (Track 01)**: Topol (证据守门); Rodman (临床侧研究); Goh (悖论)。
- **常见失败模式 (actionable)**:
  - **被 vignette 数字说服上线**: 自检「有真实前瞻结局证据吗?」
  - **让 AI 拍板诊断**: 自检「这工具的角色是假体还是决策者?」
  - **上线后不监测去技能化**: 自检「我有监测长期临床判断侵蚀的指标吗?」
- **来源 (≥3)**: [Primary] Topol (T03-S031); [Primary] Goh (T03-S030); [Primary] LLM 推理 benchmark (T03-S032, T03-S033); [Primary] automation bias/认知负荷 (T03-S034)。
- **Last_updated**: 2026-06-06
- **Decay risk**: **high**

---

## Phase 2 提炼提示

**反复出现 ≥3 个 workflow 都包含的步骤**（候选 playbook 通则）:
- **「先把病例压成 one-liner / problem representation」** 出现于: WF1 / WF2 / WF3 / WF5 → 候选 playbook「如果开始推理, 则先用一句话+成对语义限定词概括病人 (不要直接列病名)」
- **「DDx 必过 can't-miss 致命轴」** 出现于: WF1 / WF4 / WF5 → 候选 playbook「如果生成鉴别, 则按『常见 × 致命不能漏』双轴排序, 显式问『Big Three (血管/感染/肿瘤) 排了吗』」
- **「按 LR / 阈值选检查, 不穷举」** 出现于: WF1 / WF5 → 候选 playbook「如果要开检查, 则问『结果会改变下一步行动吗』, 否则不开 (防 VOMIT)」
- **「留安全网 + 反馈闭环」** 出现于: WF1 / WF5 / WF6 → 候选 playbook「如果给出 working diagnosis, 则交代 red flags + test of time/treatment + 安排能知道结局的 follow-up」
- **「外显推理 / think-aloud」** 出现于: WF2 / WF3 / WF6 (AI 当反方) → 候选 playbook「把推理说出声/外化, 才有可纠正的推理」

**入门 SOP 和资深路径之间最大的差距**（候选心智模型）:
- 入门 SOP = 穷举式数据采集 + 显式走 schema + 想得多; 资深路径 = **前几分钟定向假设生成 + 脚本匹配 (skip 穷举) + 校准更好 (不是想得多, 是排序准)** → 心智模型候选: **「资深≠更会分析, 而是 illness script 库更大 + 验前概率/can't-miss 校准更好」** (本行第一性张力 S1⇄S2 的实操结论)
- 资深普遍 **add 反馈环** (Dhaliwal「follow-up 是免费教练」) → 心智模型候选「直觉只在有反馈的环境里才能校准, 主动建反馈回路是资深的隐藏功课」
- 去偏工作流的资深差异是**选择性使用 + 结构化** (只对复杂/被误导病例做 deliberate reflection) → 心智模型候选「元认知动作要花在刀刃上, 机械套清单是另一种自动化」

**近期工作流变化的根本原因**（触发事件类型分布）:
- 7 个 workflow 中: **WF1/WF3 = 稳态 (无重大变化)**; WF2 = 因事件 (COVID→VMR 全球化); WF4 = 因学术论战持续 (Norman 2017 vs Mamede 2020-23); WF5 = 因新工具 (SAFER Dx/e-trigger 迭代); **WF6/WF7 = 因新模型+新产品+新证据 (LLM/ambient scribe, HIGH decay)**
- 主要驱动力: **AI (LLM + ambient scribe)** 是当前唯一的高速外部驱动力 → Phase 2 时识别为行业「外部驱动力」, 直接影响心智模型 (人机互补) + 反模式 (自动化偏倚/去技能化/把 AI 当答案)

**冷僻 / 信号薄弱**:
- workflow 数 7 (≥4 ✓, 非冷僻); 一手 source 62% (≥50% ✓); 资深差异点: 7/7 workflow 均有 ≥2 处 (✓)
- 弱点: (a) AI 增强工作流的采用率数字多为 vendor/媒体/单研究 (已挂 caveat); (b) 去偏工作流证据本身弱/矛盾 (这是行业事实, 不是调研缺漏 — 已诚实双向保留); (c) ambient scribe 认知负荷数字来自单研究, 需更多验证 (已标 [估计])
- **诚实边界提示**: WF6/WF7 整体 6-12 月内大概率显著过时, 强烈建议 master skill 每 3 月跑 update; WF4 的「证据弱」状态不能在 Phase 2 被软化成「这些方法有效」。
