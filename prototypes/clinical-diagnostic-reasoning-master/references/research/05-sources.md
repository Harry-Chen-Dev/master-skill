# Track 05 — Sources: 临床诊断思维 (Clinical Diagnostic Reasoning) — 持续追踪的活信息源

> locale=global (en-primary canon) | profile=practitioner | focus=comprehensive | research_date: 2026-06-06
> 行业判定: **非冷僻 (媒体层很厚)** — 本行是医学教育显学, 沉淀渠道极丰: NEJM/JAMA 长青案例系列 + 开放获取 med-ed 期刊 (Diagnosis/Acad Med/JGIM/BMJ Q&S/Med Educ) + 免费全转录 podcast (CPSolvers/Core IM Hoofbeats/Bedside Rounds) + .gov/.org 官方报告 (NAM 2015 / AHRQ / SIDM 遗产) + AI 前沿 arXiv/Substack。诊断推理真知识主要沉淀在 **期刊长青案例系列 + 免费 podcast 全转录 + 官方报告** 三处, 不在社媒。
> seed: 复用 T01 figures (NEJM/CPSolvers/Bedside Rounds/AHRQ/Diagnosis/Topol) + T02 tools 的 AI 研究源; 本 track 补齐期刊系列/专门期刊/会议/教学课程层。
> 网络环境: WebSearch 结果页验证 + source_verifier classify; `last_checked` = 当日经搜索确认 URL 被索引/存在。
> bucket 约定 (依本 track prompt): 期刊一手 / nejm·jama 域名 / .gov / podcast·society 自营站 = verified_primary 或 surrogate_primary (own publication / 自营站, 内容本身一手但 classifier 默认降级时人工标 surrogate_primary, 不私自降为 secondary)。**黑名单 (知乎/公众号/百度/CSDN/KevinMD 转载/SEO/G2/Capterra) 0 收录。**

## Source Manifest

| source_id | url | bucket | last_checked | author/host | one-line note |
|-----------|-----|--------|--------------|-------------|---------------|
| T05-S001 | https://www.nejm.org/browse/specialty/clinical-problem-solving | verified_primary | 2026-06-06 | NEJM | Clinical Problem-Solving 系列入口 — 渐进披露+大师推理出声 |
| T05-S002 | https://www.massgeneral.org/pathology/education-and-training/case-records | surrogate_primary | 2026-06-06 | Mass General Pathology | Case Records (CPC) 官方教学页 — NEJM CPC 出处 (1924-, own institution) |
| T05-S003 | https://www.nejm.org/doi/abs/10.1056/NEJMe030079 | verified_primary | 2026-06-06 | NEJM | CPC 自我反思社论 "Continuing to Learn from the Patient" |
| T05-S004 | https://jamanetwork.com/journals/jama/pages/jamaevidence-the-rational-clinical-examination | surrogate_primary | 2026-06-06 | JAMA | Rational Clinical Examination 系列主页 (own publication; 2024/25 仍更新) |
| T05-S005 | https://jamanetwork.com/collections/6257/the-rational-clinical-examination | surrogate_primary | 2026-06-06 | JAMA | RCE 合集页 — "Does this patient have…?" 全集 (own publication) |
| T05-S006 | https://www.degruyterbrill.com/journal/key/dx/html | surrogate_primary | 2026-06-06 | Diagnosis (De Gruyter) | SIDM 会刊《Diagnosis》主页 (publisher own publication) |
| T05-S007 | https://www.improvediagnosis.org/diagnosis-journal/ | surrogate_primary | 2026-06-06 | SIDM/CIDM | Diagnosis 期刊学会侧介绍页 (society own page) |
| T05-S008 | https://clinicalproblemsolving.com/ | surrogate_primary | 2026-06-06 | CPSolvers (Geha/Manesh) | The Clinical Problem Solvers 自营站 — 播客+schema 库+VMR 总站 |
| T05-S009 | https://clinicalproblemsolving.com/reasoning-content/ | surrogate_primary | 2026-06-06 | CPSolvers | 免费 schema/diagnostic frameworks 库 (按 pivot 分专科, 开放获取) |
| T05-S010 | https://www.rlrcpsolvers.com/ | surrogate_primary | 2026-06-06 | RLR (Geha & Manesh) | RLR 实时推理节目自营站 (own site) |
| T05-S011 | https://www.coreimpodcast.com/category/podcast/hoofbeats/ | verified_primary | 2026-06-06 | Core IM (Hwang/Fang) | Hoofbeats 临床推理栏目 — 全转录, 2026 仍更新 |
| T05-S012 | https://bedside-rounds.org/ | surrogate_primary | 2026-06-06 | Adam Rodman | Bedside Rounds 医学史×推理播客自营站 (ACP 联名, own site) |
| T05-S013 | https://www.acponline.org/cme-moc/internal-medicine-cme/internal-medicine-podcasts/annals-on-call-podcast | surrogate_primary | 2026-06-06 | ACP / Annals | Annals On Call — 把 Annals 论文转成讨论 (协会 own page) |
| T05-S014 | https://www.nationalacademies.org/our-work/diagnostic-error-in-health-care | surrogate_primary | 2026-06-06 | NAM (IOM) | 《Improving Diagnosis in Health Care》2015 报告项目页 (机构一手) |
| T05-S015 | https://www.ahrq.gov/diagnostic-safety/index.html | verified_primary | 2026-06-06 | AHRQ | 诊断安全与质量项目官方门户 (.gov 一手) |
| T05-S016 | https://psnet.ahrq.gov/diagnostic-safety | verified_primary | 2026-06-06 | AHRQ PSNet | PSNet 诊断安全主题流 — perspective/案例/月度精选 (.gov) |
| T05-S017 | https://www.improvediagnosis.org/ | surrogate_primary | 2026-06-06 | SIDM/CIDM | 诊断改进学会主站 (2011-2024 SIDM 遗产 → CIDM 后继, society 一手) |
| T05-S018 | https://erictopol.substack.com/ | verified_primary | 2026-06-06 | Eric Topol (Ground Truths) | 医疗 AI 证据守门人 newsletter (Substack 作者一手) |
| T05-S019 | https://arxiv.org/abs/2505.14107 | verified_primary | 2026-06-06 | DiagnosisArena (arXiv) | 诊断推理 LLM benchmark — AI 前沿活跃源样本 (arxiv.org) |

**Bucket 计数**: verified_primary 6 / surrogate_primary 13 / secondary 0 / blacklisted 0 — 19 源。surrogate_primary 多为期刊 own-publication 平台页 (jamanetwork/degruyter) + 播客·学会自营站 (本 track prompt 明示 podcast 自营站按一手处理) + 机构报告页, 内容本身一手, classifier 默认降级时人工标 surrogate_primary。无黑名单 (KevinMD 转载/知乎/公众号/SEO 农场全规避)。

---

## 总览（按 type 分组）

### 期刊长青案例系列 — 3 个（本行最厚的一手沉淀层）

| Source | Cadence | Tier | 投入产出 | One-liner |
|--------|---------|------|---------|-----------|
| NEJM Clinical Problem-Solving | rolling (月度级) | mixed | high | 渐进披露病例 + 大师 discussant 把推理过程**出声**, 全行 anchor (evidence: [T05-S001]) |
| NEJM Case Records / CPC (MGH) | weekly | senior | high | 百年 (1924-) clinicopathological conference, 病理确诊收尾的诊断谜题正典 (evidence: [T05-S002, T05-S003]) |
| JAMA Rational Clinical Examination | rolling | practitioner | high | "Does this patient have…?" 给每个体征/病史标 LR, 2024/25 仍更新 (evidence: [T05-S004, T05-S005]) |

### 专门期刊 — 2 个（+ T01/T02 已收录的 BMJ Q&S / Acad Med / JGIM）

| Source | Cadence | Tier | 投入产出 | One-liner |
|--------|---------|------|---------|-----------|
| Diagnosis (De Gruyter, SIDM 会刊) | quarterly | senior | high | 本领域唯一专刊 — 诊断如何推进/教/失败, 误诊科学主阵地 (evidence: [T05-S006, T05-S007]) |
| BMJ Quality & Safety + Academic Medicine + JGIM | rolling | senior | medium | debiasing 论战 + 误诊流行病学正典常在此对垒 (evidence: [T01-S021, T01-S013, T01-S035]) |

### Podcast — 4 个（全转录/免费, 本行知识沉淀重地）

| Source | Cadence | Host | 投入产出 | One-liner |
|--------|---------|------|---------|-----------|
| The Clinical Problem Solvers (+VMR/RLR) | weekly+ | Geha & Manesh 等 | high | 把诊断推理教学全球平民化: schema 教学 + virtual morning report 实况推理 (evidence: [T05-S008, T05-S010]) |
| Core IM — Hoofbeats | rolling | Hwang/Fang (Core IM) | high | "Dissecting clinical reasoning" — 难诊病例逐步拆解推理, 2026 仍更新 (evidence: [T05-S011]) |
| Bedside Rounds | rolling (~月度) | Adam Rodman | medium | 医学史×认知×诊断 AI 的叙事播客, ACP 联名 (evidence: [T05-S012]) |
| Annals On Call | rolling | ACP / Annals | medium | 把 Annals of IM 论文转成临床讨论, 含诊断推理主题 (evidence: [T05-S013]) |

### 机构 / 官方报告 — 4 个

| Source | 类型 | 下届/状态 | One-liner |
|--------|------|----------|-----------|
| NAM《Improving Diagnosis in Health Care》(2015) | 报告 | 已发布 (奠基) | 把诊断错误从盲区变国家议程的奠基报告 (evidence: [T05-S014]) |
| AHRQ Diagnostic Safety 门户 | .gov 项目 | rolling | 诊断安全研究/工具/资助的官方枢纽 (evidence: [T05-S015]) |
| AHRQ PSNet 诊断安全流 | .gov 月度 | rolling | perspective + 案例 + 月度精选, 跟踪领域脉搏 (evidence: [T05-S016]) |
| SIDM/CIDM (improvediagnosis.org) | 学会 | SIDM 2011-2024 落幕 → 遗产移交 | 把领域做成学会/期刊/会议 (DEM); 现追后继 CIDM (evidence: [T05-S017]) |

### Conference — 1 个

| Conference | 频率 | 状态 | One-liner |
|-----------|------|------|-----------|
| Diagnostic Error in Medicine (DEM) | annual | SIDM 2024 落幕, DEM 遗产移交后继组织 (需确认下届主办方) | 诊断错误科学的年度聚会 — 研究/教育/患者参与同台 (evidence: [T05-S017]) |

### AI 诊断前沿源 — 2 个（Decay risk: HIGH, 截至 research_date）

| Source | 类型 | One-liner |
|--------|------|-----------|
| Eric Topol — Ground Truths (Substack) | newsletter | 医疗 AI 实施/证据守门人, vignette→真实世界外推批判 (evidence: [T05-S018]) |
| arXiv 诊断推理 benchmark (DiagnosisArena 等) | preprint 流 | LLM 诊断能力评测前沿; 配 Rodman/AMIE 官方渠道 (T01/T02) 一起追 (evidence: [T05-S019]) |

### 教学 / 课程 — 1 个

| Source | 类型 | One-liner |
|--------|------|-----------|
| CPSolvers schema/frameworks 库 | 开放教学资源 | 免费 schema 图库 (按 pivot 分专科) + VMR, 临床推理教学事实标准 (evidence: [T05-S009]) |

---

## Source 详细条目

### 📰 1. NEJM Clinical Problem-Solving

- **Type**: 期刊系列 (案例)
- **URL**: https://www.nejm.org/browse/specialty/clinical-problem-solving
- **Author / Host**: NEJM 编辑部; discussant 多为 Track 01 figures (Dhaliwal/Tierney/CPSolvers 系)
- **Cadence**: rolling (月度级新案例) | **Last activity**: 2026 (持续刊出)
- **Audience tier**: mixed (学员到大师皆读)
- **One-liner**: 把病例信息**分段渐进披露**给一位专家 discussant, 让其**把诊断推理过程出声写出来** — 全行学习「专家怎么想」的 anchor。
- **典型每期内容**: 一例真实/改编病例, 临床信息分块给出, discussant 每块后更新鉴别与问题表征, 末尾揭晓 + 教学点评。是 problem representation / illness script / 鉴别排序的活教材。
- **投入产出比**: high — 几乎每篇都给从业者 actionable 推理示范 (evidence: [T05-S001])
- **Paywall**: paywall (NEJM 订阅; 机构常有; 部分免费) — worth it: 是诊断推理一手正典, 值。
- **Endorsement**: figure_long (Dhaliwal/CPSolvers 等以解 CPC/CPS 成名, T01-S004/S037); cross_source (GPT-4 评测拿它当 benchmark, T01-S037/T05-S019)
- **替代品**: CPSolvers 播客 (口播版, 免费); Core IM Hoofbeats
- **可信度**: high | **Decay risk**: low (机构级长青系列)

### 📰 2. NEJM Case Records of the MGH (Clinicopathological Conference / CPC)

- **Type**: 期刊系列 (案例)
- **URL**: https://www.massgeneral.org/pathology/education-and-training/case-records (出处) → 刊于 NEJM
- **Author / Host**: Massachusetts General Hospital Pathology + NEJM
- **Cadence**: weekly | **Last activity**: 2026 (持续, 含 online "Case Challenge" quiz)
- **Audience tier**: senior (信息密度高)
- **One-liner**: 1924 年起的 clinicopathological conference — discussant 仅凭病史+初步检查给鉴别与最终诊断, 最后由病理**确诊**收尾, 是诊断谜题的黄金标准格式。
- **典型每期内容**: 复杂未分化病例展示 → 资深 discussant 公开推理给最可能诊断 → 病理/最终诊断揭晓 → 讨论。近百年仍是 CPC 教学法源头。
- **投入产出比**: high — 但信息量大、阅读重, 适合定期精读而非速览 (evidence: [T05-S002, T05-S003])
- **Paywall**: paywall (NEJM) — worth it for senior practitioner / educator。
- **Endorsement**: cross_source (Sequential Diagnosis Benchmark/DiagnosisArena 等 AI 评测把 NEJM-CPC 当 ground truth, T05-S019); figure (CPC discussant 即大师 figure 池)
- **替代品**: CPSolvers / Hoofbeats 的口播难诊病例
- **可信度**: high | **Decay risk**: low

### 📰 3. JAMA Rational Clinical Examination

- **Type**: 期刊系列 (循证体检/病史)
- **URL**: https://jamanetwork.com/journals/jama/pages/jamaevidence-the-rational-clinical-examination
- **Author / Host**: JAMA; David Simel & Drummond Rennie 编 (配套 JAMAevidence 播客)
- **Cadence**: rolling | **Last activity**: 2025-01 (如 "Does This Patient Have Alcohol Use Disorder?")
- **Audience tier**: practitioner
- **One-liner**: "Does this patient have [疾病]?" 系列 — 给每个病史/体检发现标验前概率与 LR, 把床旁体检从经验主义变循证。
- **典型每期内容**: 一个诊断问题, 系统综述各体征/病史/检查的灵敏度·特异度·LR, 含 "Make the Diagnosis" 段 (验前概率+最佳发现+参考标准)。配同名 JAMAevidence 播客。
- **投入产出比**: high — 给体检发现「定价」, 直接改临床决策 (evidence: [T05-S004, T05-S005])
- **Paywall**: paywall (JAMA / JAMAevidence 订阅; 播客部分免费)
- **Endorsement**: cross_source (与 McGee EBPD 互引, T01-S035/T02-S012); 教学界标配
- **替代品**: McGee《Evidence-Based Physical Diagnosis》(更全, 书)
- **可信度**: high | **Decay risk**: low

### 📰 4. Diagnosis (De Gruyter, SIDM 会刊)

- **Type**: 专门期刊
- **URL**: https://www.degruyterbrill.com/journal/key/dx/html
- **Author / Host**: De Gruyter 出版; SIDM (Society to Improve Diagnosis in Medicine) 会刊; 创刊 2014-01, PubMed 索引
- **Cadence**: quarterly | **Last activity**: 2025 (如 SIDM legacy 论文 dx-2025-0120)
- **Audience tier**: senior (研究者为主)
- **One-liner**: 本领域**唯一专刊** — 专注诊断如何推进、如何教、如何及为何失败, 误诊科学与诊断质量的主阵地。
- **典型每期内容**: 诊断推理/误诊/诊断安全的原创研究、改进倡议、观点与论战 (single-anonymized 同行评审)。debiasing 论战、measurement、AI 诊断常在此发表。
- **投入产出比**: high (研究者) / medium (一线临床) — 偏研究, 临床医生选读 (evidence: [T05-S006, T05-S007])
- **Paywall**: hybrid (部分 OA, 部分订阅)
- **Endorsement**: figure_long (Graber/Singh/Newman-Toker/Durning 在此高频发表, T01-S027/S033/S058); SIDM 官方背书
- **替代品**: BMJ Quality & Safety (诊断安全外溢); Academic Medicine (教育认知)
- **可信度**: high | **Decay risk**: low-medium (SIDM 2024 落幕后会刊归属需留意, 但期刊本身由 De Gruyter 续办)

### 📰 5. BMJ Quality & Safety + Academic Medicine + JGIM（专门期刊群, 已在 T01/T02 收录）

- **Type**: 专门期刊 (跨刊)
- **URL**: 见 T01-S021 (BMJ Q&S) / T01-S013 (Acad Med) / T01-S035 (JGIM)
- **Cadence**: rolling | **Last activity**: 2025
- **Audience tier**: senior
- **One-liner**: 不是专刊但**承载本行核心论战与流行病学**: BMJ Q&S = 误诊 burden + cognitive debiasing 论文; Academic Medicine = "Causes of Errors" 等教育认知对垒; JGIM = LR/床旁循证。
- **投入产出比**: medium — 信号分散在普通刊中, 靠主题订阅/RSS 过滤 (evidence: [T01-S021, T01-S013, T01-S035])
- **Paywall**: 混合 (多有 OA)
- **Endorsement**: cross_source (Croskerry/Norman/Newman-Toker 论战论文出处)
- **可信度**: high | **Decay risk**: low

### 🎙️ 6. The Clinical Problem Solvers (+ VMR / RLR)

- **Type**: podcast (+教学社区)
- **URL**: https://clinicalproblemsolving.com/ ; RLR: https://www.rlrcpsolvers.com/
- **Author / Host**: Rabih Geha & Reza Manesh 及团队 (Track 01 #11); 受 Dhaliwal mentorship 启发
- **Cadence**: weekly+ (含 VMR 直播) | **Last activity**: 2026 (450+ 集自 2018-12)
- **Audience tier**: mixed (学员到主治)
- **One-liner**: 把诊断推理教学全球平民化的旗舰 — schema 教学法 + virtual morning report 实况推理 + RLR 二人实时解题, **全免费 + 转录/schema 图库开放**。
- **典型每期内容**: 难诊病例由嘉宾实时推理, 主持人逼出 problem representation、illness script、schema 分支; VMR 是全球学员投稿病例的现场晨会; RLR 是 Geha/Manesh 双人即兴解一例。
- **投入产出比**: high — 本行最高性价比的免费推理训练源 (evidence: [T05-S008, T05-S010])
- **Paywall**: none (核心免费; 部分课程/APP 收费)
- **Endorsement**: figure_long (CPSolvers 创始人是 T01 figure; 团队页自述受 Dhaliwal 影响, T01-S043); community_consensus (全球住院医普遍听)
- **替代品**: Core IM Hoofbeats; NEJM CPS
- **可信度**: high | **Decay risk**: low-medium (个人/团队运营, 但已机构化, 9 年稳定)

### 🎙️ 7. Core IM — Hoofbeats

- **Type**: podcast
- **URL**: https://www.coreimpodcast.com/category/podcast/hoofbeats/
- **Author / Host**: Core IM 团队 (Hoofbeats: John Hwang / Cindy Fang 等; Shreya Trivedi 总舵)
- **Cadence**: rolling | **Last activity**: 2026 (Core IM 整体 2026-06 仍发新集)
- **Audience tier**: practitioner
- **One-liner**: "Dissecting clinical reasoning" — 拿一例难诊病例, 让临床医生边读边推理, 拆解 schema、rule of thumb、认知节点。
- **典型每期内容**: 一个诊断困难病例分块披露, 多位临床医生现场反应, 复盘哪一步推理对/错、用了什么框架, 收尾给可迁移的推理 pearl。
- **投入产出比**: high — 短小且每集聚焦一个推理动作 (evidence: [T05-S011])
- **Paywall**: none
- **Endorsement**: figure_short (Core IM 团队为 T01 候选, T01-S059); cross_source (与 CPSolvers 同被推荐为推理双子星)
- **替代品**: CPSolvers
- **可信度**: high | **Decay risk**: low-medium

### 🎙️ 8. Bedside Rounds

- **Type**: podcast
- **URL**: https://bedside-rounds.org/
- **Author / Host**: Adam Rodman (Track 01 #7); ACP 联名
- **Cadence**: rolling (~月度) | **Last activity**: 2025-01 (持续)
- **Audience tier**: mixed
- **One-liner**: 医学史 × 认知 × 诊断 AI 的叙事播客 — 用历史故事讲清「我们今天为什么这样诊断」, 诊断 AI 百年史的口播版。
- **典型每期内容**: 一个医学史/诊断认识论故事 (从 INTERNIST-1 到 LLM、从听诊器到 CDS), 串起诊断思维的演化与争议。
- **投入产出比**: medium — 思想厚度高但非每集直接 actionable, 适合 ambient awareness (evidence: [T05-S012])
- **Paywall**: none (ACP CME 可选)
- **Endorsement**: figure_long (主播是 AI 诊断研究核心 figure, T01-S040/S041)
- **替代品**: Annals On Call (论文向)
- **可信度**: high | **Decay risk**: medium (个人运营播客)

### 🎙️ 9. Annals On Call

- **Type**: podcast
- **URL**: https://www.acponline.org/cme-moc/internal-medicine-cme/internal-medicine-podcasts/annals-on-call-podcast
- **Author / Host**: ACP / Annals of Internal Medicine
- **Cadence**: rolling | **Last activity**: 2025 (持续)
- **Audience tier**: practitioner
- **One-liner**: 把 Annals 重要论文 (含诊断推理/诊断检验) 转成主持人+作者的讨论, 帮临床医生把证据落到决策。
- **典型每期内容**: 选一篇 Annals 论文, 主持与作者/专家讨论临床意义, 含诊断检验、验前概率、决策阈值类主题。
- **投入产出比**: medium — 诊断推理只是其中一类主题 (evidence: [T05-S013])
- **Paywall**: none (ACP)
- **Endorsement**: institutional (ACP 官方)
- **替代品**: Bedside Rounds; The Curbsiders (后者 T01-S002 已收 Dhaliwal 集)
- **可信度**: high | **Decay risk**: low (机构运营)

### 🏛️ 10. NAM《Improving Diagnosis in Health Care》(2015)

- **Type**: 机构报告 (奠基文献)
- **URL**: https://www.nationalacademies.org/our-work/diagnostic-error-in-health-care
- **Author / Host**: National Academy of Medicine (原 IOM)
- **Cadence**: one-time (2015 发布, 奠基) | **Last activity**: 2015 (持续被引为领域起点)
- **Audience tier**: senior / policy
- **One-liner**: 把诊断错误从「患者安全盲区」抬成国家议程的奠基报告 — 重定义诊断错误、提出「多数人一生至少经历一次诊断错误」、患者入诊断团队。
- **典型内容**: 诊断过程模型、误诊定义、系统×认知共因、八大改进建议。是后续所有诊断安全工作的引用原点。
- **投入产出比**: high (作为一次性奠基读物) (evidence: [T05-S014])
- **Paywall**: none (NAP 免费在线阅读)
- **Endorsement**: figure_long (Graber 推动立项, T01-S027); 全行引用基线
- **可信度**: high | **Decay risk**: low (历史文献, 不衰减)

### 🏛️ 11. AHRQ Diagnostic Safety 门户 + PSNet 诊断安全流

- **Type**: 机构 (.gov 持续源)
- **URL**: https://www.ahrq.gov/diagnostic-safety/index.html ; https://psnet.ahrq.gov/diagnostic-safety
- **Author / Host**: Agency for Healthcare Research and Quality (AHRQ)
- **Cadence**: rolling (PSNet 月度精选) | **Last activity**: 2026 (持续)
- **Audience tier**: mixed (研究/质改/临床)
- **One-liner**: 诊断安全研究、工具 (SAFER Dx / 患者参与 toolkit)、资助与文献监测的官方枢纽; PSNet 是跟踪领域脉搏的月度雷达。
- **典型内容**: AHRQ = 项目/工具/issue briefs; PSNet = perspective 长访谈 (Graber/Singh 等)、案例 + commentary、月度新文精选。
- **投入产出比**: high (PSNet 月度精选省去自己刷期刊) (evidence: [T05-S015, T05-S016])
- **Paywall**: none (.gov)
- **Endorsement**: figure_long (PSNet 收录 Graber/Singh/Newman-Toker 访谈, T01-S022/S026/S057)
- **可信度**: high | **Decay risk**: low — **caveat**: 2025 业内有 AHRQ 经费被裁警告 (Newman-Toker 公开示警, T01-S024), 监测其资源是否缩减。

### 🏛️ 12. SIDM / CIDM (improvediagnosis.org) + DEM 会议

- **Type**: 学会 + 年度会议
- **URL**: https://www.improvediagnosis.org/
- **Author / Host**: Society to Improve Diagnosis in Medicine (SIDM, 2011-2024) → 遗产移交后继组织 (CIDM 等)
- **Cadence**: 学会 rolling; DEM 会议 annual | **Last activity**: SIDM 2024 落幕; DEM 系列遗产移交 (下届主办方需确认)
- **Audience tier**: senior
- **One-liner**: 把诊断错误从冷门做成有学会、有期刊 (Diagnosis)、有年会 (DEM) 的领域的组织; 现处遗产移交期, 追踪谁接棒。
- **典型内容**: Clinical Reasoning Toolkit、患者参与资源、DEM 年会研究 (研究/教育/患者同台)。
- **投入产出比**: medium — 资源价值高但组织在转型, 需确认后继 (evidence: [T05-S017])
- **Paywall**: none
- **Endorsement**: figure_long (Graber 创始, Trowbridge 曾任会长, T01-S027)
- **可信度**: high (历史) / medium (现状归属待确认) | **Decay risk**: **medium-high** — SIDM 2024 落幕是本 track 最大不确定点, master skill update 时优先核实 DEM/Diagnosis/toolkit 的新归属。

### 🤖 13. Eric Topol — Ground Truths (Substack)

- **Type**: newsletter (Substack) — Decay HIGH
- **URL**: https://erictopol.substack.com/
- **Author / Host**: Eric Topol (Track 01 #12), Scripps Research
- **Cadence**: ~weekly | **Last activity**: 2026-05 (如 "paradox of medical AI implementation")
- **Audience tier**: mixed
- **One-liner**: 医疗 AI 最大公共声量的证据守门人 — 对「GPT-4 超医生」类 vignette→真实世界外推持续公开批判。
- **典型每期内容**: 一篇医疗 AI / 基因组 / 数字医学长文, 带原始论文链接与批判性解读; 诊断 AI 主题高频。
- **投入产出比**: high (AI 维度) — 帮你把 AI 诊断数字放进诚实边界 (evidence: [T05-S018])
- **Paywall**: 部分免费 + paywall ($X/月, 免费层已够追主线) — worth it 视投入。
- **Endorsement**: figure_long (本人即 figure, T01-S051); cross_source (T02-S045 引其 vignette 外推批判)
- **替代品**: Adam Rodman NEJM AI / Bedside Rounds (临床侧)
- **可信度**: high | **Decay risk**: high (个人 newsletter + AI 主题双高 decay)

### 🤖 14. AI 诊断前沿: arXiv benchmark 流 + AMIE/OpenEvidence 官方渠道

- **Type**: preprint 流 + vendor/research 官方 — Decay HIGH
- **URL**: https://arxiv.org/abs/2505.14107 (DiagnosisArena 样本); 配 AMIE 官方博客 (T02-S022) / OpenEvidence 官网 (T02-S023) / Rodman NEJM AI (T01-S039)
- **Author / Host**: 多机构 (Google Research/各高校); Rodman/Manrai 等
- **Cadence**: rolling (preprint 高频) | **Last activity**: 2025-2026 (DiagnosisArena 2025-05; Sequential Diagnosis Benchmark 用 NEJM-CPC)
- **Audience tier**: senior (研究/产品)
- **One-liner**: LLM 诊断能力评测前沿 — benchmark 用 NEJM-CPC/期刊病例做 ground truth, 6-12 月即翻新, 追前沿的活源。
- **典型内容**: 诊断推理 benchmark (DiagnosisArena/MedXpertQA/Sequential Diagnosis)、对话诊断 AI (AMIE Nature)、point-of-care AI (OpenEvidence) 的论文与官方发布。
- **投入产出比**: medium — 信号多但噪声大, 靠 Topol/Rodman 二次过滤 (evidence: [T05-S019])
- **Paywall**: none (arXiv 免费; 期刊版部分付费)
- **Endorsement**: cross_source (T01-S037/S053/S054, T02-S015-S022 同一 AI 诊断证据网)
- **替代品**: Ground Truths / NEJM AI (经过策展)
- **可信度**: high (preprint 未评审, 数字一律 contested) | **Decay risk**: **high** (本 track 更新时本节优先刷新)

### 🎓 15. CPSolvers schema / diagnostic frameworks 库

- **Type**: 教学课程 / 开放资源
- **URL**: https://clinicalproblemsolving.com/reasoning-content/
- **Author / Host**: The Clinical Problem Solvers (Geha/Manesh 团队)
- **Cadence**: rolling (持续增补) | **Last activity**: 2026 (持续)
- **Audience tier**: beginner-practitioner
- **One-liner**: 免费 schema 图库 (按 pivot 症状分专科: 心/神/消化/肾/感染等) + thought-train + VMR — 临床推理教学的事实标准教具。
- **典型内容**: 每个主诉/异常 (如黄疸、晕厥、AMS) 一张 schema 分支图, 教学员沿 pivot 走鉴别; 配 APP "Schemas in Your Pocket"。
- **投入产出比**: high — 免费、可直接用于带教与自学 (evidence: [T05-S009])
- **Paywall**: none (核心免费)
- **Endorsement**: figure_long (CPSolvers; AHRQ PSNet 收录 SIDM Clinical Reasoning Toolkit 同类, T02-S046); community_consensus
- **替代品**: 大学 clinical reasoning 课程公开页 (散见 .edu, 如 Stanford Medicine 25 床旁侧 T01-S018); VINDICATE/解剖定位等教材框架
- **可信度**: high | **Decay risk**: low-medium

---

## Phase 2 提炼提示

**「这一行的资深人订阅最多的 top 5 sources」** (最该常追):
1. **NEJM Clinical Problem-Solving + Case Records/CPC** — rolling/weekly, 诊断推理出声的一手正典 anchor (evidence: [T05-S001, T05-S002])
2. **The Clinical Problem Solvers (+VMR/RLR)** — weekly+, 全免费 schema 教学 + 实况推理, 全球住院医标配 (evidence: [T05-S008])
3. **Diagnosis (SIDM 会刊)** — quarterly, 本领域唯一专刊, 误诊科学 + debiasing 论战主阵地 (evidence: [T05-S006])
4. **AHRQ PSNet 诊断安全流** — 月度精选, .gov 一手, 省去自刷期刊的领域雷达 (evidence: [T05-S016])
5. **Core IM Hoofbeats + Bedside Rounds** — 免费推理/史学播客, 短小聚焦单个推理动作 (evidence: [T05-S011, T05-S012])
→ 进入 master skill 「Sources — 信息源」节 highlights; 诚实边界「想跟最新动态」直接列此 5 处 + (AI 维度) Topol Ground Truths。

**「这一行最近的话题热度」** (topic-heat: medium-confidence, ~6 sources × episode/issue titles inspected via search):
- **LLM 诊断推理评测与「AI alone 悖论」** (Topol Ground Truths / arXiv DiagnosisArena+Sequential Dx / NEJM AI / Bedside Rounds) — 2025-2026 主热点
- **诊断安全 20 年回顾 + SIDM 落幕/遗产移交** (Diagnosis dx-2025-0120 / PSNet / improvediagnosis.org)
- **AHRQ 经费风险** (Newman-Toker 公开示警, 监测对 PSNet/资助的影响)

**新 figures 发现** (喂给 Track 01): 无新增 — 本 track 出现的 host (Geha/Manesh/Hwang/Fang/Rodman/Topol/Newman-Toker/Graber/Simel) 均已在 T01 收录或为已标候选 (Core IM 团队 T01-S059; David Simel 为 RCE 编者, 可作 canon 候选)。

**新 tools 发现** (喂给 Track 02): 无新增 — arXiv benchmark (DiagnosisArena/Sequential Diagnosis/MedXpertQA) 可作 T02 AI 评测层补充候选; AMIE/OpenEvidence/Glass 已在 T02。

**冷僻 / 信号薄弱** (诚实判断):
- **媒体层很厚 (非冷僻)**: 期刊系列 3 + 专门期刊 2 群 + podcast 4 + 机构报告 4 + AI 前沿 2 + 教学 1, 五类型全部超 floor (newsletter/AI: Topol; podcast ≥4; conference ≥1; community 经 CPSolvers/SIDM 体现)。诊断推理真知识主要沉淀在 **期刊长青案例系列 (NEJM/JAMA) + 免费全转录 podcast (CPSolvers/Core IM) + 官方报告 (NAM/AHRQ)**, 而非社媒/SEO。
- **缺口**: (1) **SIDM 2024 落幕** → DEM 会议/Diagnosis 期刊/Clinical Reasoning Toolkit 的后继归属未完全确认, 是最大不确定点 (Decay medium-high), update 时优先核实; (2) **中文一手源缺位** (locale gap) — 中文诊断推理沉淀多在人卫《诊断学》教材 + 规培课 + 黑名单平台 (公众号/知乎), 无独立中文一手 newsletter/podcast 可收, 须在诚实边界明示「本行一手正典几乎全英文」; (3) **AI 层 Decay HIGH** — arXiv/Substack/vendor 数字 6-12 月翻新, 全标 contested + last_checked; (4) community 维度无独立 Discord/论坛 (经 CPSolvers VMR 全球社区 + SIDM 体现, 但无单独平台)。
