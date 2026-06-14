# Track 06 — Glossary + 流派分歧矩阵: 临床诊断思维 (Clinical Diagnostic Reasoning)

> locale=global (en-primary canon) | profile=practitioner | focus=comprehensive | research_date: 2026-06-06
> SEED-FIRST: 本 track 复用 Track 01/02/04 的 source_id (T01-/T02-/T04-Sxxx), 仅为缺口术语补 ~17 个新源 (T06-Sxxx)。
> 本行业 glossary 的特殊形态: **几乎无 certification/standard 类术语** (临床推理本身不发证, 执业资格属医师执照范畴, 见文末 N/A 说明); 重心在 **term (认知/概率/教学/偏倚词汇)**。法规类只有 NAM 2015 报告级"软标准"。
> 数字纪律 (intake.warnings): 误诊率/AI 性能/LR 数值一律挂 source + caveat (估计/约/contested); debiasing 论战双方诚实保留, 不写 settled science; dual-process 二分局限写进定义; AI 层标 high decay。
> 黑名单规避: 知乎/公众号/百度/CSDN/KevinMD 转载/SEO 农场/G2/Capterra 全部未收录。LITFL (开放 EM 词典) 作 secondary 收录 (非黑名单, 急诊圈公认术语参考)。

## Source Manifest

| source_id | url | bucket | last_checked | author/host | one-line note |
|-----------|-----|--------|--------------|-------------|---------------|
| T06-S001 | https://ajronline.org/doi/full/10.2214/AJR.08.1330 | secondary | 2026-06-06 | AJR (期刊) | "Gestalt: Radiology's Aunt Minnie" — Aunt Minnie 起源/定义 |
| T06-S002 | https://litfl.com/hickams-dictum/ | secondary | 2026-06-06 | LITFL eponym lib | Hickam's dictum 出处/原话 (开放 EM 词典) |
| T06-S003 | https://pubmed.ncbi.nlm.nih.gov/29090995/ | verified_primary | 2026-06-06 | Cleve Clin J Med | "Occam's Razor versus Hickam's Dictum" 综述 |
| T06-S004 | https://www.amjmed.com/article/S0002-9343(20)30801-9/fulltext | surrogate_primary | 2026-06-06 | Am J Med (own pub) | 复杂病人: parsimony or plenitude — Occam→Hickam 渐变 |
| T06-S005 | https://meded.ucsf.edu/resource/clinical-teaching-tools-omp-and-snapps | verified_primary | 2026-06-06 | UCSF Med Ed (.edu) | OMP+SNAPPS 教学工具说明 |
| T06-S006 | https://pubmed.ncbi.nlm.nih.gov/36625402/ | verified_primary | 2026-06-06 | Intern Med J (PubMed) | OMP+SNAPPS 改善临床推理 meta (=T02-S039) |
| T06-S007 | https://www.cebm.ox.ac.uk/resources/ebm-tools/sppin-and-snnout | verified_primary | 2026-06-06 | Oxford CEBM (.ac.uk) | SpPin/SnNout 定义 + Sackett 出处 |
| T06-S008 | https://pmc.ncbi.nlm.nih.gov/articles/PMC2704350/ | verified_primary | 2026-06-06 | PMC | "Beyond SpPIN and SnNOUT" — 口诀局限警告 (Pewsner 谱系) |
| T06-S009 | https://www.aamc.org/resource-library/constructing-optimal-learning-environments-collection/vindicated-mnemonic | surrogate_primary | 2026-06-06 | AAMC (协会) | VINDICATE(D) 病因记忆术教学卡 |
| T06-S010 | https://litfl.com/cognitive-dispositions-to-respond/ | secondary | 2026-06-06 | LITFL | CDR / 偏倚定义集 (Croskerry 谱系转述) |
| T06-S011 | https://www.annemergmed.com/article/S0196-0644(12)01718-0/fulltext | surrogate_primary | 2026-06-06 | Ann Emerg Med (own pub) | gestalt vs Wells vs Geneva 验前概率对比 (=T02-S004 谱系) |
| T06-S012 | https://link.springer.com/article/10.1007/s43678-026-01134-1 | surrogate_primary | 2026-06-06 | CJEM (own pub) | 2026 CJEM 辩论: gestalt 该教还是该约束 (最新论战) |
| T06-S013 | https://www.ncbi.nlm.nih.gov/books/NBK543763/ | verified_primary | 2026-06-06 | NCBI Bookshelf (CBCR) | illness script 三段/四段结构定义 (开放获取全本) |
| T06-S014 | https://www.ncbi.nlm.nih.gov/books/NBK543757/ | verified_primary | 2026-06-06 | NCBI Bookshelf (CBCR) | 临床推理多视角理论概览 — semantic qualifier/context specificity |
| T06-S015 | https://pubmed.ncbi.nlm.nih.gov/30398597/ | verified_primary | 2026-06-06 | Cook et al (PubMed) | "Diagnostic vs Management Reasoning" 区分 |
| T06-S016 | https://journals.lww.com/academicmedicine/fulltext/2019/09000/management_reasoning__implications_for_health.19.aspx | surrogate_primary | 2026-06-06 | Acad Med (own pub) | Management Reasoning 教育含义+研究议程 (Cook/Durning) |
| T06-S017 | https://bjgp.org/content/69/678/e70 | surrogate_primary | 2026-06-06 | Br J Gen Pract (own pub) | safety netting 定义/证据综述 |
| T06-S018 | https://pmc.ncbi.nlm.nih.gov/articles/PMC1126156/ | verified_primary | 2026-06-06 | BMJ (Hayward, PMC) | VOMIT (victims of modern imaging technology) 出处 |
| T06-S019 | https://pubmed.ncbi.nlm.nih.gov/39773455/ | verified_primary | 2026-06-06 | Boyle/Durning (PubMed) | context specificity 超越诊断 (=T01-S034) |

**Bucket 计数 (新源 19)**: verified_primary 10 / surrogate_primary 6 / secondary 3 / blacklisted 0 — 一手层 10/19 ≈ 53%; 含跨轨复用源 (T01/T02/T04) 后整体一手占比远超 55%。surrogate 多为期刊 own-publication 页 (lww/amjmed/bjgp/springer) + AAMC 协会教学卡。无黑名单。

---

## 总览（按 type 分组）

### Tier 1 — 核心必懂 (18 个)

| 术语 | Type | Insider def | Outsider tell | Last_updated |
|------|------|-------------|---------------|--------------|
| illness script 疾病脚本 | term | 病在脑中的三段结构 (enabling conditions / fault / consequences) | 外行当"病历模板"或"剧本台词" | 1990 (稳定) |
| problem representation 问题表征 | term | 把病例蒸成一句抽象概括 (one-liner 的认知动作) | 当成"主诉复述" | 2006 (稳定) |
| semantic qualifier 语义限定词 | term | 成对抽象限定 (急/慢, 局灶/弥漫) | 当成普通形容词 | 1991 (稳定) |
| one-liner | term | 年龄+关键风险+综合征的一句话总结 | 当成"一句话病史" | 2006 (稳定) |
| pretest probability 验前概率 | term | 查之前这病的概率 (估计非测量) | 当成"检查准确率" | 1980 (稳定) |
| likelihood ratio (LR) 似然比 | term+acronym | 检查结果对赔率 (odds) 的乘子 | 把 LR 当概率/百分比 | 稳定 (数值更新) |
| Fagan nomogram | term | 验前×LR→验后的图解直尺 | 当成"诊断流程图" | 1975 (稳定) |
| test/treatment threshold 阈值模型 | term | 检查与治疗的双决策阈值 | 当成"正常值范围" | 1980 (稳定) |
| dual-process (System 1 / System 2) | term | S1 直觉模式识别 vs S2 分析推理 (连续谱, 非二分) | 当成"快=错, 慢=对"非黑即白 | 2011→医学化 (disputed 局限) |
| hypothetico-deductive 假设演绎 | term | 接诊几分钟内生成 3-5 假设再定向检验 | 当成"先查全再想" | 1978 (稳定) |
| pattern recognition / Aunt Minnie | term | 一眼认出的整体 gestalt 识别 (难言说) | 当成"猜" | 稳定 |
| anchoring 锚定 | term | 钉死首个印象不随新证据修正 | 与"先入为主"等同但其实更具体 | 2003 (稳定) |
| premature closure 过早闭合 | term | 鉴别没排完就收尾 (最高频误诊因素) | 当成"下结论太快"泛指 | 2003 (稳定) |
| availability bias 可得性 | term | 凭易想起 (近期/印象深) 高估概率 | 当成"信息不足" | 1974/稳定 |
| can't-miss diagnosis 致命不能漏 | term | 概率低但漏了会死/残的诊断 (须主动排除) | 当成"最可能的病" | 稳定 |
| Occam's razor vs Hickam's dictum | term | 一元解释 vs "病人想得几个病就几个" | 把两者当对立而非互补/年龄渐变 | 稳定 |
| diagnostic schema | term | 按 pivot 症状走分支的鉴别树 | 当成"流程图/SOP" | 稳定 |
| context/case specificity 情境特异性 | term | 推理高度内容绑定、不可通用迁移 | 当成"经验不够" | 1978→2025 (稳定+活跃) |

### Tier 2 — 周边熟知 (16 个)

| 术语 | Type | Insider def | Last_updated |
|------|------|-------------|--------------|
| base-rate neglect 基础率忽视 | term | 忽视患病率只看检查结果 (PPV 误算) | 1978 (稳定) |
| diagnostic momentum 诊断动量 | term | 标签随转诊滚雪球固化 | 2003 (稳定) |
| search satisficing 搜索满足 | term | 找到一个 (骨折/异物) 就停搜 | 2003 (稳定) |
| confirmation bias 确认偏倚 | term | 只找支持证据、不找反证 | 稳定 |
| affective bias 情感偏倚 | term | 喜欢/讨厌病人影响判断 | 2003 (稳定) |
| calibration 校准 | term | 自信度与实际准确率的吻合 | 2008 (稳定) |
| cognitive forcing strategy 认知强制策略 | term | 想到 X 时强制问 "还能是什么" | 2003 (效果 contested) |
| diagnostic timeout 诊断暂停 | term | 收尾前刻意暂停重审鉴别 | 稳定 (效果 contested) |
| VINDICATE 病因筛 | acronym | 按病因类别穷举鉴别的记忆术 | 稳定 |
| SnNout / SpPin | acronym | 高灵敏阴性排除 / 高特异阳性确诊口诀 | Sackett 谱系 (有局限警告) |
| script concordance test (SCT) | term+acronym | 测不确定下推理与专家 panel 一致度的考试 | 稳定 (依赖 panel 校准) |
| cognitive forcing / SNAPPS / OMP | term | 学习者外显推理的结构化汇报脚本 | OMP 1992 / SNAPPS 2003 |
| management reasoning 管理推理 | term | 治疗/随访/检查/资源的决策 (多解、随时间演化) | 2018 (新兴, 活跃) |
| safety netting / red flags 安全网/红旗 | term | 交代红旗症状+复诊时机以兜不确定性 | 稳定 |
| test of time / test of treatment | term | 用时间观察/试验性治疗作诊断手段 | 稳定 |
| VOMIT / incidentaloma 过度影像 | acronym/term | 影像偶然发现引发的瀑布式过度检查 | 2003 (稳定) |
| NAM 2015 "Improving Diagnosis" | regulation(软) | 把诊断错误定义为系统问题的国家级报告 | 2015 (基准) |

### Standards / Regulations / Certifications 时间轴

| 名称 | Issued | Last revised | Decay |
|------|--------|--------------|-------|
| NAM/IOM《Improving Diagnosis in Health Care》(国家级报告, 非强制法规) | 2015 | — (无修订) | low (基准文献) |
| AHRQ Diagnostic Safety 项目 (联邦教学/测量模块) | 2020 起 rolling | 2024-2025 | medium (政策驱动, 2025 经费被裁威胁, evidence: [T01-S024]) |

> **本行业 certification/standard 类基本 N/A**: 临床诊断推理本身不发独立证书 (能力评估嵌在 USMLE/规培里程碑/SCT/key-feature exam, 见 Tier 2); 无 ISO 式标准。强监管在"医师执照"层, 不属本 skill 元认知范畴。

### 行业「外行破绽」高亮 (top 10 最易暴露)

| 误用 | 内行实际意思 | 出现频率 |
|------|-------------|---------|
| 把 LR 说成"准确率/概率" | LR 是 odds 的乘子, 需配验前概率才出验后概率 (evidence: [T04-S021]) | 极高 |
| 把 dual-process 当"快=错、慢=对" | S1 不是错误之源; 资深≠更用 S2, 是脚本库更大 (evidence: [T01-S011, T04-S060]) | 极高 |
| 把 bias 标签当误诊原因 | 偏倚多是 hindsight 马后炮标签, 真因常是知识缺口 (disputed, evidence: [T04-S064]) | 高 |
| 把 Occam 和 Hickam 当对立 | 互补; 随年龄/共病从 parsimony 渐变 plenitude (evidence: [T06-S003, T06-S004]) | 高 |
| 把决策规则当 gestalt 替代 | PERC/Wells 是 gestalt 之后的二次门, 盒内人群才有效 (evidence: [T02-S003]) | 高 |
| 把 DDx 生成器/LLM 清单当最终诊断 | 输出是鉴别清单不是答案 (evidence: [T02-S013, T02-S045]) | 高 |
| 把"误诊率 79.5 万/年"当铁事实 | contested 外推估计, 区间 4 万–400 万 (evidence: [T01-S021, T01-S023]) | 中 |
| 把 SnNout/SpPin 当万能口诀 | 极端值才成立, 临界 sens/spec 会误导 (evidence: [T06-S007, T06-S008]) | 中 |
| 把 illness script 当"病历模板" | 是脑内三段记忆结构 (诱因/故障/后果), 不是文书 (evidence: [T06-S013]) | 中 |
| 把 Aunt Minnie 当"瞎猜" | 是经验沉淀的 gestalt 识别, 难言说但非随机 (evidence: [T06-S001]) | 中 |

---

## Glossary — 详细条目 (缺口/易错术语精选)

> Tier-1 概念中已在 Track 04 概念表给足定义的 (illness script/problem representation/pretest prob 等), 此处只补 **outsider-tell + 论战钩子**; 缺口术语给完整条目。

### 1. likelihood ratio (LR) 似然比 — 检查结果对 odds 的乘子

- **Type**: term + acronym | **Tier**: tier-1
- **Definition (insider)**: 某检查结果在"有病"vs"无病"人群中出现的概率之比; 验前 odds × LR = 验后 odds (evidence: [T04-S021, T02-S009])。
- **Definition (outsider)**: 一个检查结果"把患病概率往上/往下推多少"的力度。
- **常见误用 (outsider-tell)**:
  - `semantic_tell`: 外行说"这检查 LR 高"= 以为检查准; 内行: LR>10 才强确诊、<0.1 才强排除, 且**必须先有验前概率才有意义** (单独 LR 不告诉你患病概率)。
  - `usage_tell`: 把 LR 当 sensitivity/specificity 混用; LR 是由二者算出的二级量。
- **关联**: pretest probability, Fagan nomogram, SnNout/SpPin
- **可信度**: high | **Decay risk**: low (数学不变, 具体数值随研究更新)

### 2. dual-process (System 1 / System 2) 双过程 — 直觉 vs 分析 (连续谱)

- **Type**: term | **Tier**: tier-1
- **Definition (insider)**: S1 = 快速自动模式识别 (illness script/gestalt); S2 = 慢速费力分析推理 (假设演绎/Bayes)。源自 Kahneman, 经 Croskerry 医学化 (evidence: [T04-S041, T01-S007])。
- **常见误用 (outsider-tell)**:
  - `semantic_tell`: 外行 (和不少入门者) 当成"S1=危险/草率, S2=安全/严谨"非黑即白; 内行: 资深医生**靠 S1 更准** (脚本库大), S1 非错误之源 (evidence: [T01-S011])。
  - `usage_tell`: 把 S1/S2 当可分离的两个开关; 批判派指其是**连续谱、难实证分离、近乎不可证伪** (disputed, evidence: [T04-S060])。
- **disputed**: 二分模型的实证地位本身是论战焦点 (见论战②)。
- **关联**: pattern recognition, hypothetico-deductive, cognitive forcing
- **可信度**: high (框架普及) / medium (二分实证) | **Decay risk**: low

### 3. Aunt Minnie / pattern recognition 模式识别

- **Type**: term | **Tier**: tier-1
- **Definition (insider)**: 一个"经验老手一眼几乎确诊"的整体构型 (gestalt), 像在人群里一眼认出自己的 Minnie 姨妈 —— 看过很多次、却难向新手系统化解释 (evidence: [T06-S001])。源出波士顿儿童医院放射科 (Neuhauser 谱系)。
- **常见误用 (outsider-tell)**: 外行当成"瞎猜/运气"; 内行: 是高度压缩的经验沉淀, 但**只在高规律性+有反馈的环境里可靠** (反馈差的科室 gestalt 校准差, evidence: [T04-S041])。
- **关联**: illness script, dual-process (S1), gestalt-vs-rule 论战
- **可信度**: high | **Decay risk**: low

### 4. Occam's razor vs Hickam's dictum 简约 vs 多病并存

- **Type**: term | **Tier**: tier-1
- **Definition (insider)**: Occam = 尽量用单一诊断解释全部表现 (parsimony); Hickam = "病人爱得几个病就得几个病" (patients can have as many diseases as they damn well please), 警惕为了简约而过早闭合 (evidence: [T06-S002, T06-S003])。
- **常见误用 (outsider-tell)**: 外行/入门当成"哪个对"的二选一; 内行: **互补**, 随年龄/共病增加从 parsimony 渐变 plenitude —— 老年/虚弱/多病者更该用 Hickam (evidence: [T06-S004])。
- **关联**: premature closure, can't-miss, diagnostic schema
- **可信度**: high | **Decay risk**: low

### 5. can't-miss diagnosis 致命不能漏 (× common 双轴)

- **Type**: term | **Tier**: tier-1
- **Definition (insider)**: 验前概率可能不高、但漏诊导致死亡/重残的诊断 (PE/主动脉夹层/脑膜炎/SAH), 鉴别须按"常见 × 致命不能漏"双轴排序、主动排除致命项 (evidence: [T04-S022])。
- **常见误用 (outsider-tell)**: 外行以为诊断=找"最可能的病"; 内行: 先确保致命项被主动 rule-out, 即使它不是最可能。
- **关联**: VINDICATE, safety netting, search satisficing
- **可信度**: high | **Decay risk**: low

### 6. context/case specificity 情境/病例特异性 (对"通用推理课"的根本批判)

- **Type**: term | **Tier**: tier-1
- **Definition (insider)**: 同一医生在不同病例上的推理表现相关性很低 —— 诊断能力高度绑定**具体内容知识**, 不是可单独训练的通用"推理肌肉" (evidence: [T04-S060, T06-S014, T06-S019])。Elstein 1978 发现, Norman/Eva 命名。
- **常见误用 (outsider-tell)**: 外行/教育产品当成"经验不够、多练通用思维就好"; 内行 (批判派): 这正是**"教通用临床推理课"产业的根本软肋** —— 推理不可跨内容迁移, 该堆样例与知识 (evidence: [T01-S011])。
- **是否被错位包装**: "批判性思维通用课程"常把推理包装成可迁移技能 —— context specificity 文献是对该包装的直接反例 (evidence: [T04-S060])。
- **关联**: hypothetico-deductive, illness script, debiasing 论战
- **可信度**: high | **Decay risk**: low

### 7. SnNout / SpPin — 排除/确诊口诀

- **Type**: acronym | **Tier**: tier-2
- **Definition (insider)**: SnNout = 高 **S**e**n**sitivity 检查阴性 (**N**egative) 可**rule out**; SpPin = 高 **Sp**ecificity 检查阳性 (**P**ositive) 可**rule in**。Sackett 推广 (evidence: [T06-S007])。
- **常见误用 (outsider-tell)**:
  - `usage_tell`: 当成万能口诀; 只在 sens/spec **接近极端 (>95%)** 时成立, 临界值会误导 (evidence: [T06-S008])。
  - `pronunciation_tell`: 读作 "snout / spin" (一个词), 非逐字母。
- **关联**: likelihood ratio, pretest probability
- **可信度**: high | **Decay risk**: low

### 8. VINDICATE 病因筛 (穷举型框架)

- **Type**: acronym | **Tier**: tier-2
- **Definition (insider)**: 按病因类别穷举鉴别的记忆术 —— Vascular/Infectious/Neoplastic/Degenerative-Drugs/Iatrogenic-Idiopathic/Congenital/Autoimmune/Traumatic/Endocrine (变体 VINDICATE-M/VINDICATED) (evidence: [T06-S009])。
- **常见误用 (outsider-tell)**: 外行当成"诊断清单/答案"; 内行: 是**穷举防漏的脚手架** (与 schema 的 pivot 聚焦型互补), 套太满会催生 VOMIT/过度检查。
- **关联**: diagnostic schema, can't-miss, VOMIT
- **可信度**: high | **Decay risk**: low

### 9. management reasoning 管理推理 (诊断之外的新兴维度)

- **Type**: term | **Tier**: tier-2
- **Definition (insider)**: 关于治疗/随访/进一步检查/资源分配的决策推理。与诊断推理本质不同: **多个合理解、随时间演化、必须纳入患者偏好与情境约束、更不确定** (Cook & Durning, evidence: [T06-S015, T06-S016])。
- **常见误用 (outsider-tell)**: 外行把"诊断"和"管理"混为一谈; 内行: 诊断可判对错且不该受患者偏好影响, 管理几乎总要权衡偏好/资源, 二者推理结构不同。
- **是否错位包装**: 多数"临床推理"教学只教诊断侧, 把 management reasoning 当"知道指南就行"—— Cook/Durning 指出它同样有 script、同样需专门教 (evidence: [T06-S016])。
- **关联**: context specificity, illness script
- **可信度**: high | **Decay risk**: medium (新兴活跃领域)

### 10. safety netting / red flags / test of time / test of treatment 安全网

- **Type**: term | **Tier**: tier-2
- **Definition (insider)**: safety netting = 在不确定下显式交代红旗症状 (red flags)、预期病程与复诊时机, 以兜住误诊风险; test of time = 用时间观察作诊断手段; test of treatment = 试验性治疗的反应作诊断线索 (evidence: [T06-S017])。
- **常见误用 (outsider-tell)**: 外行当成"叮嘱几句"; 内行: 是结构化的**诊断不确定性管理动作** (而非礼貌话), 是 working diagnosis 的标准配套。
- **关联**: can't-miss, working diagnosis, calibration
- **可信度**: high | **Decay risk**: low

### 11. VOMIT / incidentaloma 过度影像受害者

- **Type**: acronym + term | **Tier**: tier-2
- **Definition (insider)**: VOMIT = Victims Of Modern Imaging Technology —— 影像偶然发现 (incidentaloma) 引发的瀑布式过度检查/创伤性追查, 最终对无害病灶无益甚至致害 (Hayward 2003, evidence: [T06-S018])。
- **常见误用 (outsider-tell)**: 外行/患者把"查得越多越安全"; 内行: 把它当"穷尽式排查 (rule-out everything)"与防御性医疗的反模式标签。
- **关联**: base-rate neglect, pretest probability, defensive medicine
- **可信度**: high | **Decay risk**: low

### 12. SNAPPS / One-Minute Preceptor (OMP) 教学脚本

- **Type**: term + acronym | **Tier**: tier-2
- **Definition (insider)**: OMP = Neher 1992 五步微技能带教 (get commitment / probe for evidence / teach general rule / reinforce / correct); SNAPPS = Wolpaw 2003 学习者主导六步 (Summarize/Narrow/Analyze/Probe/Plan/Select) —— 把汇报从"念事实"变成"外显推理+主动暴露不确定性" (evidence: [T06-S005, T06-S006])。
- **常见误用 (outsider-tell)**: 外行把 SNAPPS 当"汇报模板"; 内行: 核心是让学员**Narrow + Analyze 鉴别 + Probe 自己的不确定性**, 不是背诵格式。
- **关联**: problem representation, script concordance test, morning report
- **可信度**: high | **Decay risk**: low

---

## 流派分歧矩阵 (framework 甜区 — 保留分歧不软化)

> intake 谱系的 6 派对照。轴 = 主张 / 奠基人·代表 / 适用 / 核心分歧。**两边都是本 skill 素材, 不写成谁全胜。**

| 流派 | 核心主张 | 奠基人 → 当代代表 | 最适用场景 | 与他派的核心分歧 |
|------|---------|-----------------|-----------|----------------|
| **决策科学 · Bayesian 派** | 诊断=条件概率更新; 检查只为跨越决策阈值; 不确定性须显式量化 | Ledley-Lusted 1959 → Elstein / Kassirer / Sox-Pauker / Eddy → Brush (evidence: [T04-S042, T04-S043, T04-S007]) | 检查取舍、阈值决策、概率沟通 | 被批"理想化"——真实临床验前概率难精确、医生不天然算 Bayes; 与 gestalt 派在"规则 vs 直觉"对立 |
| **认知心理 · 双过程/去偏派** | 误诊源于可分类的认知偏倚; dual-process 框架; **去偏可教** (cognitive forcing/timeout/checklist) | Kahneman-Tversky → Croskerry / Graber (evidence: [T04-S053, T01-S006, T01-S007]) | 偏倚意识教学、M&M 复盘、元认知习惯 | **被教育认知派正面驳斥**: 偏倚是 hindsight 标签、不可证伪; 去偏 RCT 证据弱 (见论战①) |
| **教育认知 · illness-script 派** | 专长=知识结构与样例库, 非通用推理或偏倚规避; **knowledge is the cure** | Schmidt-Boshuizen 1990 → Norman / Eva / Mamede / Durning (evidence: [T04-S048, T04-S064, T01-S011]) | 课程设计、刻意练习、样例堆叠、反思推理 | 被去偏派批"把 debiasing 阴性结果过度外推为不可教"; Mamede 的 deliberate reflection 阳性证据是内部张力 |
| **诊断安全 · 系统派** | 误诊=系统×认知共因; 须测量 (e-trigger/SAFER Dx) + 流行病学量化 + 组织化 advocacy | NAM 2015 → Newman-Toker / Hardeep Singh / Graber-SIDM (evidence: [T01-S021, T01-S025, T01-S027]) | 质量改进、政策、误诊负担测量、安全网设计 | 与认知派在"个人去偏 vs 系统重设计"侧重不同; 其误诊数字本身 contested (见论战⑦数字) |
| **床旁临床派** | 病史+循证体检为王; 诊断是手艺+刻意练习; 在场与体检是诊断兼关系现场 | Osler → Tierney / Verghese / McGee / Dhaliwal / Saint (evidence: [T01-S016, T01-S001, T01-S035]) | 一线问诊、体检定价、床旁教学、master 展演 | 被批"浪漫主义/不可规模化/缺硬终点 RCT"; "大师展演"被 context-specificity 派质疑可迁移性 |
| **AI · 计算派** | 诊断可计算; 从专家系统到 LLM 追平/超人类; AI 作"第二意见/认知假体" | INTERNIST-1 → Isabel → LLM 世代 Rodman / Topol / AMIE (evidence: [T01-S037, T01-S039, T02-S020]) | 鉴别扩列、推理质疑、循证检索、疑难病例 | "AI 超医生"被批 hype (vignette→真实外推未验证, Topol); 自动化偏倚/去技能化风险; "AI alone 悖论"(见论战⑥) |

---

## 核心论战 (逐条正反方 + 保留未决)

### 论战 ① 【本行第一对垒】去偏可教 ⇄ 知识才是解药

- **正方 (去偏可教 · Croskerry/Graber)**: 偏倚是真实可观察现象; cognitive forcing/diagnostic timeout/Ely checklist 是元认知层 Type-2 override, 可教; 去偏需系统级+教育级长期组合, 单针 RCT 难证伪 (evidence: [T01-S006, T01-S010, T04-S081])。
- **反方 (知识为核 · Norman/Sherbino/Monteiro/Pelaccia)**: (a) 偏倚清单是马后炮标签、不可证伪 (同一错误可贴多个矛盾偏倚名); (b) "Debiasing strategies have proven ineffective, regardless of specialty and level of training" (AEM 2025 原话); (c) 错误主因是知识缺口而非过程缺陷 (evidence: [T01-S011, T01-S012, T04-S064])。cognitive forcing 对照试验显示**无效** (evidence: [T02-S036])。
- **未决/桥**: Mamede 团队 deliberate reflection 有阳性证据, 是对"干预全无效"的部分反例 (evidence: [T04-S076])。**结论: 不写成 settled science, 双方均保留为素材。**

### 论战 ② dual-process 二分被批 (连续谱 / 不可证伪)

- **正方**: S1/S2 是组织临床直觉 vs 分析的有用语言 (Croskerry, evidence: [T01-S007])。
- **反方**: 二分过度简化、是连续谱、难实证分离、近乎不可证伪; 且"快≠错"——资深者 S1 更准 (Norman/Eva, evidence: [T04-S060, T01-S011])。**写进模型局限。**

### 论战 ③ 决策规则 ⇄ 临床 gestalt (算法厌恶)

- **正方 (规则)**: Wells/PERC/HEART 可验证、可审计、盒内人群安全排除 (evidence: [T02-S028, T02-S031])。
- **反方 (gestalt)**: 资深 gestalt 在 PE 高/低概率分层上有时比 Wells 更准, 且 clinical aids "未能持续优于医生判断" (evidence: [T06-S011, T02-S004])。**2026 CJEM 辩论专题: gestalt 该教还是该约束, 仍公开未决** (evidence: [T06-S012])。
- **共识**: 多数最佳实践是 gestalt 定低概率 → 规则二次确认 (PERC 范式), 二者一致性差 (κ<0.3), 非可互换 (evidence: [T02-S003])。

### 论战 ④ Occam's razor ⇄ Hickam's dictum

- 一元简约 vs 多病并存; **互补而非对立**, 随年龄/共病从 parsimony 渐变 plenitude (evidence: [T06-S003, T06-S004])。

### 论战 ⑤ 床旁体检复兴 ⇄ 影像替代

- **正方 (复兴 · Verghese/McGee)**: 体检是诊断+医患仪式, 该按 LR 循证保留 (evidence: [T01-S017, T01-S035])。
- **反方**: 缺"更多体检→更好结局"硬终点 RCT; RVU/效率下不可规模化; 浪漫主义批评 (evidence: [T01-S017])。AI 派反向引用: ambient AI 若"把时间还给床旁"恰是其议程的技术实现。

### 论战 ⑥ AI alone > physician+AI 悖论 (Goh)

- Goh 2024 RCT: 给医生 LLM **未显著**提升诊断推理 vs 常规资源, 但 **LLM 单独得分显著高于两组医生** (evidence: [T02-S017, T01-S054])。
- **caveat**: vignette 研究、非真实结局; "截至 research_date 的发现, 可能被后续研究翻转"; 不代表该让 AI 自主行医 —— 协作界面是未解难题 (evidence: [T02-S045])。

### 论战 ⑦ 推理 case-specificity 不可通用迁移 (对"教通用推理课"的根本批判)

- Elstein 1978 起、Norman/Eva 命名: 同一医生跨病例表现相关性低, 推理高度内容绑定 (evidence: [T04-S060, T06-S019])。**直接挑战"教一门通用临床推理/批判性思维课就能提升诊断力"的产业假设** —— 批判派主张堆样例与知识 (evidence: [T01-S011])。
- **附: 误诊数字之争**: "79.5 万/年美国严重伤害" (Newman-Toker 2023) 是外推估计, 区间 4 万–400 万; "约 5% 门诊误诊" (Singh 2014)、"10-15% 经典估计"均 contested。**本 skill 一律标 contested estimate + 区间** (evidence: [T01-S021, T01-S023, T01-S056])。

---

## 关键差异对照 (本 skill 边界)

| 维度 | 临床诊断思维 (本 skill) | 具体专科诊疗 | 中医辨证 | EBM 文献评价 |
|------|----------------------|-------------|---------|------------|
| **核心对象** | 医生"怎么想病"的**元认知操作系统** (症状→诊断的推理过程) | 某病的具体治疗/手术方案与剂量 | 以阴阳/八纲/脏腑辨证求"证型" | 怎样批判性评读一篇研究/指南的证据强度 |
| **产出物** | one-liner / 鉴别 / 验前概率 / working diagnosis + 安全网 | 处方 / 术式 / 随访计划 | 证型 + 方剂 | 证据等级 / 偏倚风险评估 / GRADE |
| **本体论** | 概率 + 病理生理的西医诊断框架; illness script/Bayes | 病种知识与操作技能 | 整体观/辨证论治, 非疾病实体映射 | 研究方法学 (RCT/系统综述/统计) |
| **与本 skill 关系** | —— | 互补但更下游 (本 skill 是上游元认知) | 平行体系 (另有 skill, 不混) | 相邻工具 (本 skill 用 EBM 产出的 LR/患病率, 但不聚焦文献评价方法学) |
| **易混点** | —— | 把"诊断思维"等同"会治某病" | 把"临床思维"误当中西医通用 | 把"诊断推理"误当"会查证据/读 meta" |

> **安全边界 (本行业特有)**: 本 skill 是面向临床专业人士/医学生的**思维教练**, 不替代真实临床判断与执业医师诊疗, 不面向患者提供医疗建议; 对话样本不得把 AI 输出当最终诊断; 病例一律去标识化/虚构化。

---

## Phase 2 提炼提示

**「行业表达 DNA」直接素材**:
- 高频黑话 top 10: one-liner / problem representation / illness script / 验前概率 (pretest) / LR / DDx / can't-miss / pivot (schema) / VINDICATE / "what else could it be"
- 行业拒绝的厂商话术 top 5: ① 把 LLM/Isabel 清单包装成"AI 诊断答案" (内行: 永远是鉴别清单不是诊断); ② 把"AI 超医生"vignette 数字当真实性能; ③ 把 debiasing checklist 当"消除误诊万灵药"; ④ "通用批判性思维课提升诊断力" (违背 context specificity); ⑤ 把决策规则当 gestalt 替代黑箱。
- 外行破绽 top 10: 见上"外行破绽高亮"表 (LR 当概率 / dual-process 非黑即白 / bias 当因果 / Occam-Hickam 对立 / 规则替代 gestalt / 清单当诊断 / 误诊数字当铁事实 / SnNout 滥用 / illness script 当模板 / Aunt Minnie 当瞎猜)。

**「智识谱系」线索**:
- 范式更替路径: 决策科学/Bayes (1959) → 教育认知/illness script (1990) → 双过程/去偏 (2003) → 诊断安全/系统 (2015) → AI/计算 (2023-) —— 每代未取代前代, 而是叠加+互相批判。
- 多流派竞争而非收敛: 去偏派 vs 知识派的对垒是"硬件层"分歧 (教什么、怎么评估), 至今未决 = 本行最尖锐张力。
- gestalt 派 (床旁) ⇄ 规则派 (决策科学) 是另一条平行裂缝, 2026 仍在 CJEM 公开辩论 (evidence: [T06-S012])。

**「时效性」信号**:
- AI 层 (LLM/AMIE/OpenEvidence/Goh 悖论) = **high decay**, 6-12 月可翻转, master skill 更新优先刷此节。
- management reasoning = 新兴活跃 (medium decay), 术语定义仍在沉淀。
- 误诊率数字全 contested, 须随新流行病学研究更新。
- 核心认知/概率术语 (illness script/LR/threshold) = low decay, 30+ 年稳定。

**「工作流变化触发」种子 (喂 Track 03)**:
- AI 辅助诊断落地 + 自动化偏倚/去技能化 guardrails = 工作流最大变量 (evidence: [T02-S042, T02-S043])。
- NAM 2015 报告 → 触发诊断安全测量/安全网/closed-loop follow-up 工作流。
- ambient AI scribe 若兑现"把时间还给床旁" → 体检/问诊工作流重配。

**冷僻 / 信号薄弱**:
- 总术语数 34 (Tier1 18 + Tier2 16) ≥ 25 ✓; Tier1 ≥ 15 ✓; 全部 Tier1 填 outsider-tell ✓ —— **非冷僻**。
- 弱点: certification/standard 类基本 N/A (本行不发独立证, 已说明, 非缺漏); 独立中文一手 glossary 薄 (人卫《诊断学》「临床思维方法」章为教材类例外, 其余沉淀在黑名单平台) —— 诚实边界须明示中文 canon 失衡 (evidence: [T04-S036])。
