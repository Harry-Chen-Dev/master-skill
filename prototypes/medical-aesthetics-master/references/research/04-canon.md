# Track 04 — 知识正典（Canon）：医疗美容 / 注射美容（locale=zh-CN）

> 医美 canon 横跨「医学专业」（临床循证、注射解剖、专家共识、注射方法学）与「行业实务 / 强监管 / 产业」两层。本行第一性背景：医疗本质 + 强监管 + 消费属性三重叠加，所以 canon 必须同时覆盖 **临床指南共识 + 监管法规原文 + 专业期刊 + 行业研究报告 + 核心概念**。监管原文（gov 域名）= 本行 ground truth = verified_primary；临床注射解剖 / 方法学有大量 global 一手。
>
> 数据厚度判断：医美是 data-rich 行业（监管 + 厂商 + 临床 + 上市公司四支柱皆可机械验证一手）。本文件一手（verified_primary + 合理 surrogate_primary）占比估计 ~70%。

---

## Source Manifest

| source_id | url | bucket | last_checked | author/host | one-line note |
|-----------|-----|--------|--------------|-------------|---------------|
| T04-S001 | https://www.nhc.gov.cn/wjw/c100221/202201/d7e8fa33a26b425da98d69fb04191699.shtml | verified_primary | 2026-06-21 | 国家卫健委 | 《医疗美容服务管理办法》原文 — 行业根本法规 |
| T04-S002 | https://www.gov.cn/zhengce/zhengceku/2021-11/04/content_5648772.htm | verified_primary | 2026-06-21 | 市场监管总局/中国政府网 | 《医疗美容广告执法指南》原文 — 容貌焦虑/对比图监管 |
| T04-S003 | https://www.nmpa.gov.cn/xxgk/fgwj/xzhgfxwj/20221114155641144.html | verified_primary | 2026-06-21 | 国家药监局 NMPA | 2022年103号公告 — 医用透明质酸钠按三类械管理 |
| T04-S004 | https://www.nmpa.gov.cn/wwwroot/gyx02302/flml.htm | verified_primary | 2026-06-21 | 国家药监局 NMPA | 医疗器械分类目录 — 一/二/三类分类 ground truth |
| T04-S005 | https://www.beijing.gov.cn/zhengce/zhengcefagui/201905/t20190522_60470.html | verified_primary | 2026-06-21 | 北京市政府 | 医疗美容主诊医师专业备案管理通知 — 备案制度落地 |
| T04-S006 | https://rs.yiigle.com/cmaid/1194162 | verified_primary | 2026-06-21 | 中华医学会/中华医学美学美容杂志 | 《中国人群中面部年轻化治疗专家共识》原文(学会期刊平台) |
| T04-S007 | https://www.huasan.net/wp-content/uploads/2025/03/中国人群中面部年轻化治疗专家共识.pdf | secondary | 2026-06-21 | 厂商转载PDF | 同上共识全文PDF — 一手核对用,bucket留secondary(非官方host) |
| T04-S008 | https://www.medsci.cn/guideline/show_article.do?id=312e61c003a2290d | secondary | 2026-06-21 | MedSci(指南聚合) | 《中国人群面部年轻化透明质酸填充剂应用指南》索引页 |
| T04-S009 | https://www.medjournals.cn/journalContribute/getJournalInfo.do?journalId=121 | secondary | 2026-06-21 | 中华医学会杂志社 | 中华医学美学美容杂志刊物信息(ISSN/CN/创刊) |
| T04-S010 | http://manu52.magtech.com.cn/Jwk_mrzx/CN/column/column4715.shtml | secondary | 2026-06-21 | 中国美容整形外科杂志编辑部 | 期刊官网简介(ISSN1673-7040/月刊/1990创刊) |
| T04-S011 | https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8012343/ | verified_primary | 2026-06-21 | de Maio (PMC全文) | MD Codes 方法学奠基论文(2021, 全文开放) |
| T04-S012 | https://www.tandfonline.com/doi/full/10.2147/CCID.S430747 | verified_primary | 2026-06-21 | de Maio 等(T&F/Dove) | MD Codes 治疗情绪/社交属性 retrospective case study |
| T04-S013 | https://pubmed.ncbi.nlm.nih.gov/28027232/ | verified_primary | 2026-06-21 | Scheuer et al (PRS) | "Anatomy of the Facial Danger Zones" 注射危险区解剖经典 |
| T04-S014 | https://academic.oup.com/asjopenforum/article/3/4/ojab034/6374028 | verified_primary | 2026-06-21 | ASJ Open Forum | 高产出注射靶点与危险区(ASJ 期刊文章) |
| T04-S015 | https://www.sciencedirect.com/science/article/pii/S2352587822000729 | verified_primary | 2026-06-21 | Elsevier/期刊 | 填充剂减少血管风险的解剖图解综述 |
| T04-S016 | https://shop.elsevier.com/books/procedures-in-cosmetic-dermatology-botulinum-toxin/carruthers/978-0-323-83116-1 | surrogate_primary | 2026-06-21 | Elsevier(出版社官页) | Carruthers《Botulinum Toxin》第5版 — 肉毒美容奠基教材 |
| T04-S017 | https://shop.elsevier.com/books/procedures-in-cosmetic-dermatology-soft-tissue-augmentation/carruthers/978-0-323-83075-1 | surrogate_primary | 2026-06-21 | Elsevier(出版社官页) | Carruthers《Soft Tissue Augmentation》第5版 — 填充教材 |
| T04-S018 | https://books.ipmph.com/books/detail/2047703.shtml | surrogate_primary | 2026-06-21 | 人民卫生出版社 | 《整形外科学》人卫教材(出版社官页) |
| T04-S019 | https://www.pmphmall.com/gdsdetail/614727-289325 | surrogate_primary | 2026-06-21 | 人民卫生出版社商城 | 《皮肤性病学》第9版(本科规划教材) |
| T04-S020 | https://www.fda.gov/medical-devices/aesthetic-cosmetic-devices/dermal-fillers-soft-tissue-fillers | verified_primary | 2026-06-21 | FDA | 填充剂监管/血管栓塞致盲警示(global 一手) |
| T04-S021 | https://www.fda.gov/consumers/consumer-updates/dermal-filler-dos-and-donts-wrinkles-lips-and-more | verified_primary | 2026-06-21 | FDA | 填充剂 Do's/Don'ts 消费者警示 |
| T04-S022 | https://stockn.xueqiu.com/SZ300896/20240319092889.pdf | secondary | 2026-06-21 | 爱美客年报PDF(雪球转载host) | 爱美客2023年报 — 毛利率/产品营收 数字源(非官方host留secondary) |
| T04-S023 | https://www.qianzhan.com/analyst/detail/220/240807-74cf381b.html | secondary | 2026-06-21 | 前瞻产业研究院 | 玻尿酸三巨头经营分析 — 行业研究二手 |
| T04-S024 | https://zhongzhihui.oss-cn-beijing.aliyuncs.com/industryPdf/艾瑞咨询：2022年中国医疗美容行业研究报告.pdf | secondary | 2026-06-21 | 艾瑞咨询 | 艾瑞医美行业研究报告(行业研究二手) |
| T04-S025 | https://pmc.ncbi.nlm.nih.gov/articles/PMC11745296/ | verified_primary | 2026-06-21 | (PMC narrative review) | 肉毒+填充面部不良反应叙述性综述(并发症循证) |
| T04-S026 | https://academic.oup.com/asj/pages/about | surrogate_primary | 2026-06-21 | ASJ/Oxford(期刊官页) | Aesthetic Surgery Journal 简介(IF 3.9, 整形美容期刊第一) |

> 黑名单已剔除：知乎(zhuanlan.zhihu.com,出现在多次搜索结果但未入表)、百度百科(baike.baidu)、CSDN。consensus 全文以学会期刊平台(yiigle, 中华医学会)为一手锚点；厂商/雪球转载PDF诚实留 secondary 仅作数字核对。

---

## 候选总览（按类型分组）

### A. 临床指南 / 专家共识（本行 canon 核心，必读）

| 共识/指南 | 发布机构 | 一句话 | evidence |
|------|------|------|------|
| 中国人群中面部年轻化治疗专家共识 | 中国整形美容协会面部年轻化/抗衰老/医美线分会 | 中国人脸老化评估 + 注射/光电/线雕/手术分层治疗的国内权威共识 | T04-S006, T04-S007 |
| 中国人群面部年轻化透明质酸填充剂应用指南 | 中华医学会相关分会 | 玻尿酸在中国人脸上的分区/层次/剂量循证指南 | T04-S008 |
| 肉毒毒素注射在皮肤美容中应用的专家共识(2023版) | 中国医师协会皮肤科分会 | 国内肉毒美容应用的权威临床指导 | T04-S009(刊载于中华医学美学美容杂志) |
| 面部注射软组织填充剂的安全性专家共识 | 中国整形美容协会微创与皮肤美容分会 | 强调玻尿酸是唯一可被透明质酸酶特异降解/可逆的填充材料 | T04-S008 |

### B. Textbook / 系统性著作（必读 4）

| 书名 | 作者 | 难度 | 一句话 |
|------|------|------|------|
| Botulinum Toxin (Procedures in Cosmetic Dermatology, 5th ed) | Alastair & Jean Carruthers | 进阶 | 肉毒美容的奠基双人组写的标准操作教材 |
| Soft Tissue Augmentation (同系列, 5th ed) | Carruthers 等 | 进阶 | 填充剂注射的系统性临床教材 |
| 整形外科学(人卫规划教材) | 人卫/学会组织 | 入门-进阶 | 中国整形外科学科体系的统一教材 |
| 皮肤性病学(第9版,人卫本科教材) | 人卫规划 | 入门 | 皮肤科医生的学科底座(医美皮肤侧根基) |

### C. Seminal Papers（必读 4）

| 论文 | 年 | 核心 idea | evidence |
|------|------|------|------|
| MD Codes™: A Methodological Approach... HA Fillers | 2021 | 把全脸切成编码亚单位,每码给深度/工具/剂量/危险结构 | T04-S011 |
| Anatomy of the Facial Danger Zones (PRS) | 2017 | 系统定义注射致盲/坏死的面部危险区解剖 | T04-S013 |
| High Yield Injection Targets and Danger Zones (ASJ) | 2021 | 高产出靶点 vs 危险区的对照 | T04-S014 |
| Adverse effects of botulinum toxin & dermal fillers (review) | 2024 | 肉毒+填充不良反应的循证综述(并发症谱) | T04-S025 |

### D. 监管法规原文（强监管行业 ground truth — verified_primary）

| 法规 | 发布机构 | 一句话 | evidence |
|------|------|------|------|
| 医疗美容服务管理办法 | 国家卫健委 | 机构/主诊医师/诊疗范围的根本法规 | T04-S001 |
| 医疗美容广告执法指南 | 市场监管总局 | 禁制造容貌焦虑/疗效保证/对比图/代言 | T04-S002 |
| 医疗器械监督管理条例 + 分类目录 | 国家药监局 NMPA | 玻尿酸/再生类作为三类械的注册与管理 | T04-S003, T04-S004 |
| 医疗美容主诊医师备案制度 | 卫健委/地方 | 美容外科6年/牙5年/中医皮肤3年临床经历门槛 | T04-S005 |

### E. 专业期刊（追踪 canon 的入口）

| 期刊 | 一句话 | evidence |
|------|------|------|
| 中华医学美学美容杂志 | 国内医美学术最高位之一,共识多在此刊发 | T04-S009 |
| 中国美容整形外科杂志 | 国内整形美容外科核心期刊(1990创刊,月刊) | T04-S010 |
| Aesthetic Surgery Journal (ASJ) | 整形美容期刊 IF 第一(3.9),global 一手 | T04-S026 |
| Plastic & Reconstructive Surgery (PRS) | 整形外科旗舰刊,危险区解剖经典发于此 | T04-S013 |
| JAMA Dermatology / Dermatologic Surgery | 皮肤外科/皮肤美容循证主战场 | (期刊层,见正文) |

### F. 行业研究 / 上市公司披露（数字 ground truth）

| 来源 | 一句话 | evidence |
|------|------|------|
| 弗若斯特沙利文 / 艾瑞医美报告 | 市场规模/增速/渗透率的业内估计来源 | T04-S023, T04-S024 |
| 爱美客年报/招股书 | 嗨体/濡白天使营收、~95%毛利率的一手披露 | T04-S022 |

---

## 详细条目

### 共识 / 指南

#### 1. 中国人群中面部年轻化治疗专家共识
- **发布**: 中国整形美容协会面部年轻化分会 + 抗衰老分会 + 医美线技术分会，刊于中华医学美学美容杂志
- **One-liner**: 中国人脸的老化评估 + 注射/光电/美塑/线雕/脂肪/手术分层治疗的国内权威共识。
- **核心论点**: ①中国人面部老化以中面部容积缺失为关键；②按微创注射/光电/埋线/脂肪填充/手术分级方案；③强调评估先行、个体化。
- **必读理由**: 国内临床做面部年轻化方案设计的权威参照系，非营销叙事。 evidence: [T04-S006, T04-S007]
- **争议**: 与「网红改造派/欧式大平行」审美取向相对，共识偏循证保守自然。 evidence: [T04-S006]
- **继承关系**: 把 global 容积理论(Volumizing)本土化到中国人脸解剖。 evidence: [T04-S006, T04-S011]
- **可信度**: high / **Decay risk**: medium（共识有版本更新）

#### 2. 肉毒毒素注射在皮肤美容中应用的专家共识(2023版)
- **发布**: 中国医师协会皮肤科分会，2023-11，刊于中华医学美学美容杂志
- **One-liner**: 国内肉毒美容（除皱/瘦脸/瘦肩等）的应用、剂量、点位与安全的权威指导。
- **必读理由**: 肉毒是单位(U)/扩散/中毒高危药，国内合规操作以此共识为准。 evidence: [T04-S009]
- **可信度**: high / **Decay risk**: medium

#### 3. 面部注射软组织填充剂安全性专家共识 / 玻尿酸应用指南
- **One-liner**: 填充剂安全操作 + 玻尿酸是唯一可被透明质酸酶特异降解、具可逆性的填充材料。
- **核心论点**: 注射量宁少勿多、速度宁慢勿快、避免局部张力过大、优选浅层/真皮深层；血管栓塞24h内用透明质酸酶溶解，组织耐缺血窗约72h。 evidence: [T04-S008]
- **必读理由**: 血管栓塞致盲/坏死急救流程的国内一手依据。 evidence: [T04-S008]
- **可信度**: high / **Decay risk**: low（解剖避险原则稳定）

### Textbook

#### 4. Botulinum Toxin / Soft Tissue Augmentation (Carruthers, Procedures in Cosmetic Dermatology, 5th ed)
- **Author**: Alastair Carruthers & Jean Carruthers（1987 年首创 BOTOX 美容应用的双人组，与 Track 01 figures 直接关联）
- **Year**: 第5版（最新），系列长期更新
- **Type**: 临床操作教材（含 step-by-step + 视频）
- **One-liner**: 肉毒/填充美容「方法论 + 循证 + 操作」的全球标准教材，奠基者亲著。
- **核心论点**: 神经调节剂作用机制；分区注射决策；填充剂选择与层次；evidence-based 操作。
- **读完得到什么**: 能讲清肉毒/填充每个适应区的剂量、层次、避险与决策逻辑。
- **难度**: 进阶 / **Endorsement**: `[type: figure_long]` 作者本人即领域奠基(T04-S016)；`[type: conf_citation]` MD Codes 论文引用其方法学脉络(T04-S011)；`[type: course_syllabus]` 皮肤美容 fellowship 标准参考。
- **可信度**: high / **Decay risk**: medium（每版更新产品与术式）
- evidence: [T04-S016, T04-S017]

#### 5. 整形外科学 / 皮肤性病学(人卫规划教材)
- **One-liner**: 中国整形外科与皮肤科学科体系的统一教材，医美医生的学科底座。
- **必读理由**: 主诊医师备案要求整形外科/皮肤科临床背景，这两本是该背景的知识地基。 evidence: [T04-S018, T04-S019, T04-S005]
- **难度**: 入门-进阶 / **可信度**: high / **Decay risk**: low
- evidence: [T04-S018, T04-S019]

### Papers

#### 6. MD Codes™: A Methodological Approach to Facial Aesthetic Treatment with Injectable HA Fillers (de Maio, 2021)
- **Authors**: Mauricio de Maio（与 Track 01 figures 关联，注射方法学 originator）
- **Venue**: 开放全文 (PMC8012343)
- **One-liner**: 把全脸切成编码亚单位（颊/颞/颏/下颌/鼻唇/木偶纹/泪沟/唇/鼻），每个 code 给出深度、工具（钝针 vs 锐针）、安全技法、需避开的危险结构、产生可见可复现效果的最小剂量。
- **核心 idea**: 把「徒手手艺」变成「可教、可审计、可复现的方法」；配合 MD ASA 多维评估（H1–H5 层级）。 evidence: [T04-S011]
- **为什么经典**: 全球最广泛采用的面部评估/注射框架之一，被无数 fellowship 与厂商培训采纳。 evidence: [T04-S011, T04-S012]
- **如何读**: 先读分区编码逻辑与评估层级，再对照 case study。
- **后续/扩展**: MD Codes 治疗情绪/社交属性的 case study(2024)。 evidence: [T04-S012]
- **可信度**: high / **Decay risk**: low

#### 7. Anatomy of the Facial Danger Zones (PRS, 2017) + High Yield Targets & Danger Zones (ASJ, 2021)
- **One-liner**: 系统定义注射致盲/坏死的面部危险区（眉间/前额、鼻部、鼻唇、颞区、眶下、唇、颏）及其与眼动脉系统的连通解剖。
- **核心 idea**: 危险源于动脉与眼动脉系统的直接/间接吻合 + 部分区域侧支循环不足；2D 分布 + 3D 深度解剖是安全注射前提。 evidence: [T04-S013, T04-S014, T04-S015]
- **为什么经典**: 注射避险（危险三角、回抽、钝针、缓慢推注）的解剖学依据。
- **可信度**: high / **Decay risk**: low
- evidence: [T04-S013, T04-S014]

### 监管法规（详见 Manifest D 组 — gov 原文）

- 《医疗美容服务管理办法》：机构须《医疗机构基本标准》达标；主诊医师备案分美容外科/牙科/皮肤科/中医科，每人一个专业；美容外科主诊须6年以上整形/美容外科临床经历。 evidence: [T04-S001, T04-S005]
- 《医疗美容广告执法指南》：重点打击「制造容貌焦虑」「疗效保证性承诺」「诊疗前后效果对比图」「广告代言人推荐」「软文/伪科普变相发布」。 evidence: [T04-S002]
- NMPA：注射真皮层改善皮肤状态的医用透明质酸钠按**第三类医疗器械**管理（最严）。 evidence: [T04-S003, T04-S004]

### 行业研究 / 上市公司（数字均挂 caveat）

- 市场规模：2024 中国医美市场约 3120 亿元、增速约 14.8%（沙利文/行业研究口径，业内估计，须随年份更新）。 evidence: [T04-S023, T04-S024]
- 爱美客：2023 销售毛利率约 95%；2024 嗨体营收约 17.44 亿、濡白天使约 12.16 亿（上市公司年报披露）。 evidence: [T04-S022]
- caveat：行业报告与单家公司数据不可当 universal 事实；黑医美比例/并发症率属个体差异大的业内估计。

---

## Core Concepts（25 个）

| 概念 | tier | 一句话定义 | 来源 |
|------|------|------|------|
| 注射层次（皮内/真皮/皮下/SMAS/骨膜上） | tier-1 | 不同材料/部位对应不同注射深度，错层=并发症 | T04-S006, T04-S016 |
| 面部老化容积理论(Volumizing) | tier-1 | 老化核心是容积缺失而非仅松弛，填充补容积 | T04-S006, T04-S011 |
| MD Codes | tier-1 | 全脸分区编码的注射方法学 | T04-S011 |
| MD ASA 多维评估(H1–H5) | tier-2 | MD Codes 配套的层级化全脸评估流程 | T04-S011 |
| 危险三角 / 面部危险区 | tier-1 | 与眼动脉吻合、栓塞致盲/坏死高风险的解剖区 | T04-S013, T04-S014 |
| 血管栓塞 / 栓塞致盲 | tier-1 | 填充误入血管的最严重急症，可致盲/坏死/脑栓塞 | T04-S008, T04-S020 |
| 透明质酸酶（溶解酶） | tier-1 | 唯一可特异降解玻尿酸、栓塞急救核心药 | T04-S008 |
| 组织耐缺血窗(~72h) | tier-2 | 栓塞后抢救时间窗，24h内溶解效果最佳 | T04-S008 |
| 回抽 / 钝针 vs 锐针 / 缓慢推注 | tier-1 | 注射避险三件套 | T04-S008, T04-S013 |
| 适应证 / 禁忌证 | tier-1 | 该做/不该做的医学判断，劝退伦理基础 | T04-S001, T04-S006 |
| 知情同意 + 术前照留存 | tier-1 | 医疗+法律双重要求，风险逐项告知 | T04-S001, T04-S002 |
| Fitzpatrick 皮肤分型 | tier-1 | 按晒后反应分型，决定光电参数与色沉风险 | T04-S019 |
| 丁达尔现象 | tier-2 | 玻尿酸过浅注射呈青蓝色调的光学并发症 | T04-S008 |
| 结节 / 肉芽肿 | tier-2 | 填充后异物反应/感染性肿块 | T04-S025 |
| 单位(U) / 支(1ml) | tier-1 | 肉毒按 U、玻尿酸按支(ml)计量 | T04-S009 |
| 三庭五眼 / 黄金比例 | tier-2 | 中国传统面部审美量化框架 | T04-S006 |
| 苹果肌/泪沟/法令纹/木偶纹/卧蚕/颞部 | tier-1 | 注射方案的标准解剖审美分区命名 | T04-S006, T04-S011 |
| 再生材料(童颜针PLLA/少女针PCL) | tier-1 | 刺激自体胶原再生的填充类 | T04-S003, T04-S006 |
| 线雕(PPDO/PCL) | tier-2 | 埋线提升术式 | T04-S006 |
| 联合治疗 / 全脸设计 | tier-1 | 注射+光电+手术的整体方案设计 | T04-S006 |
| 械字号 / 国械注准 vs 妆字号 | tier-1 | 三类械合规标识 vs 化妆品标识(辨真伪) | T04-S003, T04-S004 |
| 三非 / 黑医美 / 水货 | tier-1 | 非法机构/药械/行医 + 走私货 | T04-S001, T04-S002 |
| BDD（体象障碍）/ 容貌焦虑 | tier-1 | 面诊须筛查的心理高危,过度医美/劝退伦理触发点 | T04-S002, T04-S006 |
| 过度医美 / 科技脸 | tier-2 | 反复叠加致面部失自然的批判性概念 | T04-S006 |
| 主诊医师备案 / 诊疗范围 | tier-1 | 合规执业的资质门槛 | T04-S001, T04-S005 |

---

## Phase 2 提炼提示

### 反复出现 ≥3 个 canon 都讨论的核心 idea（候选心智模型）
- **「解剖避险优先于效果」**：危险区解剖(T04-S013) + 安全性共识(T04-S008) + Carruthers教材(T04-S016) + FDA警示(T04-S020) 一致——注射决策的第一约束是血管/层次安全，不是美学最大化。 → 候选心智模型「先安全后审美」。
- **「容积思维 + 全脸分区设计」**：面部年轻化共识(T04-S006) + MD Codes(T04-S011) 都从「容积缺失 + 分区编码」出发 → 候选心智模型「不是头痛医头，是全脸结构性评估」。
- **「合规是医疗行为的前置条件」**：管理办法(T04-S001) + 广告指南(T04-S002) + 器械分类(T04-S003) 三条 gov 原文共同界定「正规 vs 三非」边界 → 候选心智模型「资质/械字号/知情同意是入场券」。
- **「可逆性 = 玻尿酸的安全优势」**：填充安全共识(T04-S008) + FDA(T04-S020) 都点透明质酸酶可逆 → playbook：选材料时把「出事能不能溶」纳入决策。

### 智识谱系种子
- **注射方法学派**奠基：de Maio MD Codes(T04-S011)；Carruthers 夫妇肉毒/填充教材(T04-S016/17)。当前代表 → 与 Track 01 figure 关联。
- **注射解剖避险派**奠基：Facial Danger Zones 系列(T04-S013/14/15)。
- **中国循证本土化派**奠基：中华医学会/中国整形美容协会专家共识(T04-S006/08/09)，把 global 方法学本土化到中国人脸 + 中国监管。
- **监管 ground truth 谱系**：卫健委/NMPA/市场监管总局原文(T04-S001~005)——本行独有的「法规即 canon」特征。
- **主要分歧（canon 内仍 debated）**：自然保守派 vs 网红改造派审美；「产品论」(认正品)vs「医生论」(技术决定效果)；劝退伦理 vs 满足需求/升单。共识偏循证保守，但消费营销侧并不受共识约束——这是本行 canon 与实务的结构性张力。

### 核心概念 → 候选 playbook
- 遇到「填充注射前」→ 先按危险区解剖 + 回抽/钝针/缓慢推注/宁少勿多（解剖避险三件套）。
- 遇到「疑似血管栓塞」→ 立即停针 + 24h 内透明质酸酶溶解，把握 ~72h 耐缺血窗。
- 遇到「求美者诉求异常强烈/反复」→ 筛查 BDD/容貌焦虑，触发劝退伦理而非升单。
- 遇到「选机构/选产品」→ 先验《医疗机构执业许可证》+ 主诊医师备案 + 械字号(国械注准)，三类械才合规。

### 冷僻 / 信号薄弱
- 不冷僻：共识/指南 ≥4、papers ≥4、textbook ≥4、监管原文 ≥4、concepts 25，远超 floor 20。
- 诚实边界：①部分国内共识全文锚定在中华医学会期刊平台(yiigle, 标 surrogate_primary)，非 gov 域名但属学会一手；②市场规模/毛利率等数字来自行业报告/上市公司年报，已挂 caveat，不可当 universal 事实；③临床注射手感/审美/急救决断是高 tacit，canon 只能给原则，真功夫靠规范化培训 + 大量实操 + 并发症处理经验，且医疗安全红线不可让渡。
- 一手占比估计 ~70%（gov 法规 + FDA + PMC/PRS 全文 + 出版社官页 + 学会共识为一手主体；行业报告/上市公司转载PDF诚实留 secondary）。
