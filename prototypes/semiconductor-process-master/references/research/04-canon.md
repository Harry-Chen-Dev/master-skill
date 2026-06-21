# Track 04 — Canon / 知识正典 · Semiconductor Process Engineering (global, en-primary)

> Phase 1 Wave 1 第 1 路输出。行业 = 半导体芯片制造工艺。locale = global。
> 数据厚度: **data-rich**（IEDM/VLSI/IRPS 顶会 + 教材 canon + IRDS 路线图 + 设备/代工厂披露皆可机械验证一手），非 creative-craft 低一手率结构。
> en-primary canon（教材 + 顶会论文几乎全英文）+ zh-CN 产业/政策补充。**节点命名营销 / 国产替代叙事 / 物理极限软化** 三条红线在本文件忠实保留。

## Source Manifest

| source_id | url | bucket | last_checked | author/host | one-line note |
|-----------|-----|--------|--------------|-------------|---------------|
| T04-S001 | https://plummergriffinbook.stanford.edu/ | verified_primary | 2026-06-21 | Plummer/Deal/Griffin (Stanford) | 作者官方书页，Silicon VLSI Tech 全 PDF 免费（.edu） |
| T04-S002 | https://ocw.mit.edu/courses/6-152j-micro-nano-processing-technology-fall-2005/pages/readings/ | verified_primary | 2026-06-21 | MIT OCW 6.152J | 课程 syllabus reading list — Plummer/Campbell/Wolf/Sze 列入（course syllabus, .edu） |
| T04-S003 | https://ocw.mit.edu/courses/6-780-semiconductor-manufacturing-spring-2003/pages/readings/ | verified_primary | 2026-06-21 | MIT OCW 6.780 | 制造/良率课程 syllabus，May&Spanos 列入（course syllabus, .edu） |
| T04-S004 | https://nap.nationalacademies.org/read/12980/chapter/13 | verified_primary | 2026-06-21 | National Academies Press | Dennard 1974 论文官方重印 appendix（gov-adjacent 学术出版社一手） |
| T04-S005 | https://ieeexplore.ieee.org/document/4785534/ | verified_primary | 2026-06-21 | IEEE Xplore (Bohr) | "A 30 Year Retrospective on Dennard's MOSFET Scaling Paper" — IEEE 一手 |
| T04-S006 | https://irds.ieee.org/editions/2023/irds-2023-lithography | verified_primary | 2026-06-21 | IEEE IRDS | 2023 路线图官方 Litho 章（IRDS 官方 = 一手 roadmap，spec 白名单） |
| T04-S007 | https://irds.ieee.org/images/files/pdf/2023/2023IRDS_MM.pdf | verified_primary | 2026-06-21 | IEEE IRDS | 2023 More Moore 章 PDF — DTCO/BSPDN/CFET 路线 |
| T04-S008 | https://en.wikipedia.org/wiki/Fin_field-effect_transistor | secondary | 2026-06-21 | Wikipedia | FinFET 术语 + 1999 Hisamoto/Hu 论文谱系参考 |
| T04-S009 | https://scholar.nycu.edu.tw/en/publications/sub-50-nm-finfet-pmos | verified_primary | 2026-06-21 | NYCU scholar hub | "Sub 50-nm FinFET: PMOS" (IEDM 1999) 论文记录（.edu/学术库） |
| T04-S010 | https://spie.org/news/under-water | secondary | 2026-06-21 | SPIE news | 浸没式光刻历史科普（Burn Lin 水浸 193i 叙事，行业媒体留 secondary） |
| T04-S011 | https://www.spie.org/news/immersionlitho-intro | secondary | 2026-06-21 | SPIE news | 193nm immersion status & challenges 综述 |
| T04-S012 | https://semiengineering.com/what-will-replace-dual-damascene/ | secondary | 2026-06-21 | Semiconductor Engineering | Cu/low-k dual damascene 历史 + Edelstein/IBM 引用（行业媒体长稿） |
| T04-S013 | https://www.computerhistory.org/collections/catalog/102770822 | verified_primary | 2026-06-21 | Computer History Museum | Moore 1965 "Cramming..." 原件馆藏（博物馆一手存档） |
| T04-S014 | https://hasler.ece.gatech.edu/Published_papers/Technology_overview/gordon_moore_1965_article.pdf | verified_primary | 2026-06-21 | Georgia Tech (.edu) | Moore 1965 Electronics 原文 PDF 重刊（.edu 托管一手） |
| T04-S015 | https://global.oup.com/ushe/product/fabrication-engineering-at-the-micro--and-nanoscale-9780199861224 | verified_primary | 2026-06-21 | Oxford University Press | Campbell 教材出版社官方页（出版社 = spec 白名单一手） |
| T04-S016 | https://onlinelibrary.wiley.com/doi/book/10.1002/0471790281 | verified_primary | 2026-06-21 | Wiley/IEEE Press | May & Spanos 教材出版社官方页（出版社一手） |
| T04-S017 | https://books.google.com/books/about/Semiconductor_Manufacturing_Technology.html?id=O2eGQgAACAAJ | secondary | 2026-06-21 | Google Books | Quirk & Serda 教材书目元数据 |
| T04-S018 | https://www.tsmc.com/english/news-events/blog-article-20220615 | verified_primary | 2026-06-21 | TSMC | "What is DTCO?" 官方技术博客（代工厂一手 vendor doc） |
| T04-S019 | https://iedm23.mapyourshow.com/mys_shared/iedm23/handouts/SC1.5_IEDM_2023_DTCO_STCO_YK.pdf | verified_primary | 2026-06-21 | IEDM 2023 (Arm, YK Chong) | IEDM 2023 short course DTCO/STCO 讲义（顶会官方一手） |
| T04-S020 | https://www.asml.com/en/news/stories/2024/5-things-high-na-euv | verified_primary | 2026-06-21 | ASML | High-NA EUV 0.55NA 官方技术页（设备厂一手 vendor doc） |
| T04-S021 | https://semiengineering.com/new-transistor-structures-at-3nm-2nm/ | secondary | 2026-06-21 | Semiconductor Engineering | GAA nanosheet/CFET @3nm/2nm 综述（行业媒体） |
| T04-S022 | https://semiconductor.samsung.com/news-events/tech-blog/3nm-gaa-mbcfet-unrivaled-sram-design-flexibility/ | verified_primary | 2026-06-21 | Samsung Semiconductor | 3nm GAA MBCFET 官方技术博客（代工厂一手） |
| T04-S023 | https://www.imec-int.com/en/articles/outer-wall-forksheet-bridge-nanosheet-and-cfet-device-architectures-logic-technology | verified_primary | 2026-06-21 | imec | forksheet→CFET 器件架构路线（研究机构一手） |
| T04-S024 | https://onlinelibrary.wiley.com/doi/full/10.1002/cvde.201402012 | verified_primary | 2026-06-21 | Puurunen (Wiley/CVD) | "A Short History of ALD: Suntola's Atomic Layer Epitaxy" — ALD 谱系一手 |
| T04-S025 | https://sarjaweb.vtt.fi/julkaisut/muut/2010/Puurunen.pdf | verified_primary | 2026-06-21 | Puurunen / VTT | "Surface chemistry of ALD" 综述全文（作者本人 own publication via 研究所托管） |
| T04-S026 | https://nccavs-usergroups.avs.org/wp-content/uploads/2024/12/CMPUG1224-Ses-1.1-BeyerK-RobertsB.pdf | verified_primary | 2026-06-21 | Beyer (AVS CMP UG) | "The Inception of CMP" — CMP 发明人 Klaus Beyer 本人 talk（originator own talk） |
| T04-S027 | https://www.sciencedirect.com/science/article/abs/pii/004060909290539N | verified_primary | 2026-06-21 | IBM (Thin Solid Films) | "Integration of CMP into CMOS IC manufacturing" IBM 1992 论文（DOI 一手） |
| T04-S028 | https://semianalysis.com/dylan-patel/ | secondary | 2026-06-21 | SemiAnalysis | Dylan Patel 分析机构（专业分析 secondary，含 STEEL 拆解 lab） |
| T04-S029 | https://www.semi.org/en/connect/events/iss-speaker-bio-abstract-dylan-patel | surrogate_primary | 2026-06-21 | SEMI | 会议 speaker bio — 分析师身份佐证（会议 sponsor/speaker surrogate） |
| T04-S030 | https://dunham.ece.uw.edu/ee531/ | surrogate_primary | 2026-06-21 | U.Washington EE531 | "Physics & Modeling of Nanoscale VLSI Devices" course syllabus reading list（.edu syllabus） |
| T04-S031 | https://ia601608.us.archive.org/5/items/PhysicsOfSemiconductorDevices_855/PhysicsOfSemiconductorDevices3rdEdition-S.M.SzeAndKwokK.Ng.pdf | secondary | 2026-06-21 | Internet Archive | Sze《Physics of Semiconductor Devices》3rd 存档（书目佐证，非盗版站） |
| T04-S032 | https://archive.org/details/siliconprocessin0001wolf | secondary | 2026-06-21 | Internet Archive | Wolf & Tauber《Silicon Processing for the VLSI Era》馆藏存档 |
| T04-S033 | https://semiengineering.com/new-transistor-structures-at-3nm-2nm/ | secondary | 2026-06-21 | Semiconductor Engineering | (同 S021) short-channel effect / electrostatics 解释 |
| T04-S034 | https://www.wiley-vch.de/en/areas-interest/engineering/fundamentals-of-semiconductor-manufacturing-and-process-control-978-0-471-78406-7 | secondary | 2026-06-21 | Wiley-VCH | May & Spanos 内容目录（SPC/yield/DOE/APC 章节佐证） |

一手率（manifest 计）：verified_primary + surrogate_primary = 21 / 34 ≈ **62%** > 50% floor。

---

## 总览（按类型分组）

### Textbook / 系统性著作（必读 6 / 推荐 1）
| 书名 | 作者 | 难度 | Endorsement | 一句话 |
|------|------|------|-------------|--------|
| Silicon VLSI Technology: Fundamentals, Practice and Modeling | Plummer / Deal / Griffin | 进阶-高阶 | MIT 6.152J 主教材 + Stanford 官方书页 + 全行业引用 | 把单元工艺的物理 + TCAD 建模 + 制造实践三者缝起来的「圣经」 |
| Physics of Semiconductor Devices | S. M. Sze (& Ng) | 高阶专家 | 多课程主参考 + 器件物理标准引用 | 器件物理 ground truth：能带/输运/MOS 静电的标准本 |
| Silicon Processing for the VLSI Era (Vol 1-3) | Wolf & Tauber | 进阶（手册型） | MIT syllabus + 专利/技术文档高频引用 | 最详尽的工艺百科手册，查 recipe 细节的案头工具书 |
| Fabrication Engineering at the Micro- and Nanoscale | S. A. Campbell | 入门-进阶 | Oxford 系列 + MIT/多校 capstone 教材 | 本科/研一 fab 入门首选，单元工艺全覆盖、可读性最好 |
| Fundamentals of Semiconductor Manufacturing & Process Control | May & Spanos | 进阶 | MIT 6.780 主教材 + IEEE Press | 把 fab 当统计制造系统：SPC/yield model/DOE/APC 的唯一系统教材 |
| Semiconductor Manufacturing Technology | Quirk & Serda | 入门 | community college / 技师培训标准本 | fab 技师/操作层的术语-设备-流程入门，最低门槛 |
| Integrated Circuit Fabrication: Science and Technology | Plummer & Griffin (2023) | 进阶 | Plummer/Deal/Griffin 的现代继任 textbook | Silicon VLSI Tech 的 2023 更新，早引入 SOTA CMOS flow（部分 supersede） |

### Seminal Papers（必读 6）
| 论文 | 年 | 核心 idea | Endorsement |
|------|-----|-----------|-------------|
| Cramming More Components onto Integrated Circuits (Moore) | 1965 | 集成度 ~ 指数增长（Moore's Law 起源） | CHM 馆藏 + IEEE 重刊 + 全行业 |
| Design of Ion-Implanted MOSFETs with Very Small Physical Dimensions (Dennard et al.) | 1974 | 恒电场等比微缩（Dennard scaling） | Nat. Academies 重印 + IEEE 30 周年回顾 |
| Sub-50nm FinFET: PMOS / FinFET self-aligned double-gate (Hisamoto, Hu et al.) | 1999-2000 | 双栅鳍式抑制短沟道，scalable to 20nm | IEDM/TED + 量产采用（22nm 起） |
| Cu/low-κ dual damascene interconnect (Edelstein et al., IBM) | 1997 | Cu 大马士革替代 Al，解 RC 延迟 | IEDM 1997 + 全行业 BEOL 标准 |
| Surface chemistry of ALD (Puurunen) / Suntola ALE 历史 | 2005 / 2014 | 自限性表面反应→原子级保形薄膜 | high-k/HKMG 量产基础 + 综述高引 |
| Inception of CMP（Beyer/IBM，专利 1985 + 集成 1992） | 1985/1992 | 化学机械平坦化解多层布线 topography | 发明人本人 talk + IBM 论文 + STI/Cu 量产 |

### Courses（必看 2 / 推荐 2）
| 课程 | 讲师/机构 | 格式 | Last_updated | 一句话 |
|------|----------|------|--------------|--------|
| MIT 6.152J Micro/Nano Processing Technology | MIT EECS/MSE | 讲座+lab+reading | 2005（archived OCW） | 单元工艺理论+洁净室实操的经典 syllabus，reading list 即隐性 canon |
| MIT 6.780 Semiconductor Manufacturing | MIT EECS | 讲座+reading | 2003（archived OCW） | fab 当统计制造系统：SPC/yield/DOE/APC，配 May&Spanos |
| U.Washington EE531 Physics & Modeling of Nanoscale VLSI Devices | Dunham, UW | 讲座+reading | rolling（.edu syllabus） | 纳米器件物理+建模，衔接器件→工艺 |
| ASML / imec 公开技术 readouts（High-NA EUV, CFET, BSPDN） | ASML / imec | 技术博客+白皮书 | rolling, 2024-2025 | 前沿设备/架构的一手 vendor 路线（非课程但持续更新 canon-adjacent） |

### Core Concepts（24 个）
| 概念 | 一句话定义 | 来源 |
|------|-----------|------|
| Moore's Law | 集成度随时间指数增长的经济-技术规律 | Moore 1965 (S013/S014) |
| Dennard scaling | 恒电场等比微缩，尺寸↓则功耗密度恒定 | Dennard 1974 (S004/S005) |
| Dennard scaling 终结 | ~2005 后漏电/功耗墙使 Dennard 失效，频率停滞 | Bohr 回顾 (S005) |
| Dimensional vs Equivalent scaling | 物理尺寸微缩 vs 靠器件/材料/架构等效提升密度 | IRDS MM (S007) |
| 短沟道效应 SCE / DIBL | 栅失去对沟道静电控制，Vt roll-off + 漏致势垒降低 | S008/S033 |
| PPAC | Performance-Power-Area-Cost 四角权衡，先进节点核心评价 | TSMC/IEDM (S018/S019) |
| DTCO | 设计-工艺协同优化以提升 PPAC | TSMC/IEDM/IRDS (S018/S019/S007) |
| STCO | 系统-工艺协同（DTCO 向系统层延伸） | IEDM SC (S019) |
| DFM / 可制造性 | 设计须满足工艺窗口与良率约束 | May&Spanos (S016) |
| FEOL / MOL / BEOL | 前道器件 / 中段接触 / 后道互连三大模块 | Plummer/Wolf (S001/S032) |
| Cu/low-k 大马士革 | Cu 互连 + 低介电，解 BEOL RC 延迟 | Edelstein/IBM (S012) |
| RC 延迟 | 互连电阻×电容主导的延迟，BEOL 微缩动因 | S012 |
| 浸没式光刻 193i | 透镜与晶圆间注水提升 NA>1，延寿 193nm | SPIE (S010/S011) |
| EUV / high-NA EUV | 13.5nm 反射式 / 0.55NA 把单曝光分辨率推到 8nm | ASML (S020) |
| 多重曝光 SADP/SAQP | 自对准多重图形化突破单曝光分辨率极限 | IRDS Litho (S006) |
| OPC | 光学邻近校正，补偿衍射保真图形 | IRDS Litho (S006) |
| Overlay / 套刻 | 层间对准误差，多重曝光下成关键 budget | IRDS Litho (S006) |
| 原子层沉积 ALD | 自限性表面反应逐层成膜，high-k 基础 | Puurunen (S024/S025) |
| 原子层刻蚀 ALE | ALD 的刻蚀对偶，原子级可控去除 | IRDS / 行业 (S006/S021) |
| CMP / dishing-erosion | 化学机械平坦化；过抛形貌缺陷 dishing/erosion | Beyer (S026/S027) |
| 热预算 thermal budget | 退火/工序累积热量约束掺杂剖面与微缩 | Plummer (S001) |
| 良率 yield / D0 缺陷密度 | fab 主经济指标；缺陷密度模型预测良率 | May&Spanos (S016/S034) |
| SPC / FDC / APC | 统计过程控制 / 故障检测 / 先进过程控制 | May&Spanos (S016/S034) |
| FinFET → GAA nanosheet → CFET | 器件架构微缩路线：鳍→环栅纳米片→互补堆叠 | S008/S021/S022/S023 |
| BSPDN 背面供电 | 供电网移到晶圆背面以省正面布线面积 | IRDS MM (S007) |

> 概念 24 个 ≥ 20 floor。tier 划分见下。

---

## 详细数据结构

### 📖 1. Silicon VLSI Technology: Fundamentals, Practice and Modeling

- **Author**: James D. Plummer, Michael D. Deal, Peter B. Griffin（Stanford；与 Track 01 figures 强关联 — Plummer 是 Stanford 工艺学派代表）
- **Year**: 2000（1st & only print ed）；现代继任 *Integrated Circuit Fabrication: Science and Technology*, 2023
- **Type**: textbook（senior/graduate 一学期 fabrication 课）
- **One-liner**: 把每个单元工艺的「物理 + TCAD 计算机仿真 + 制造实践」三层缝合的工艺工程圣经。 (evidence: [T04-S001, T04-S002])
- **核心论点**: (1) 工艺 = 可建模的物理过程，氧化/扩散/注入/沉积/刻蚀都有解析+数值模型；(2) 现代工艺开发离不开 TCAD 仿真先行；(3) CMOS flow 是模块协同而非单工艺堆叠。 (evidence: [T04-S001])
- **读完得到什么**: 能把一条 CMOS 工艺流程拆成单元工艺、用模型预测掺杂剖面/氧化厚度、理解工艺窗口的物理来源。
- **难度**: 进阶-高阶
- **Endorsement evidence**:
  - `[type: course_syllabus]` MIT OCW 6.152J 列为主教材（ISBN 9780130850379）(evidence: [T04-S002])
  - `[type: figure_long]` 作者 Stanford 官方书页提供全书免费 PDF + 课程背景说明（作者本人 own publication）(evidence: [T04-S001])
  - `[type: course_syllabus]` UW EE531 等多校器件/工艺课参考 (evidence: [T04-S030])
- **superseded_by**: 部分被 *Integrated Circuit Fabrication: Science and Technology* (Plummer & Griffin, 2023) 更新（早引入 SOTA CMOS flow）。旧版仍值得读：TCAD 建模章节与工艺物理推导仍是 pre-FinFET 时代最系统的教学路径，新版偏 big-picture flow。**两版并留**。
- **替代品**: Campbell（更易入门）/ Wolf&Tauber（更详尽手册）
- **如果只读 1 章**: 氧化与扩散（Deal-Grove 模型 + 热预算）章
- **可信度**: high · **Decay risk**: low

### 📖 2. Physics of Semiconductor Devices (Sze & Ng)

- **Author**: Simon M. Sze（& Kwok K. Ng）
- **Year**: 1st 1969 / 3rd 2006（VLSI Technology 另册）
- **Type**: textbook / 器件物理标准参考
- **One-liner**: 半导体器件物理的 ground truth —— 能带、载流子输运、MOS 静电的标准引用本。 (evidence: [T04-S031, T04-S030])
- **核心论点**: (1) 器件行为可由半导体物理第一性原理推导；(2) MOS/双极/光电器件共享统一的能带-输运框架；(3) 器件物理是工艺微缩约束（短沟道、隧穿）的根源。
- **读完得到什么**: 理解为什么物理极限不可软化 —— 量子隧穿、短沟道、漏电从能带物理直接推出。
- **难度**: 高阶专家
- **Endorsement evidence**:
  - `[type: course_syllabus]` UW EE531 nanoscale VLSI devices reading list (evidence: [T04-S030])
  - `[type: course_syllabus]` MIT 6.152J 推荐 VLSI Technology (Sze, 2nd) (evidence: [T04-S002])
  - `[type: blog_secondary]` 全行业器件物理标准引用（Internet Archive 多版存档）(evidence: [T04-S031])
- **替代品**: Pierret《Semiconductor Device Fundamentals》（更易入门）
- **如果只读 1 章**: MOSFET 章（短沟道效应物理）
- **可信度**: high · **Decay risk**: low

### 📖 3. Silicon Processing for the VLSI Era (Wolf & Tauber, Vol 1-3)

- **Author**: Stanley Wolf, Richard N. Tauber（Lattice Press）
- **Year**: Vol 1 1986 / Vol 2 1990 / Vol 3 1995-2002
- **Type**: multi-volume 手册型百科
- **One-liner**: 工艺细节最详尽的案头百科 —— 查某个 unit process 的 recipe/机理就翻它。 (evidence: [T04-S032, T04-S002])
- **核心论点**: (1) 每个工艺步骤都有可查的参数空间与物理机理；(2) 工艺整合是模块间约束的求解；(3) 详尽 > 简洁，作为参考工具书。
- **读完得到什么**: 遇到具体工艺问题（某沉积台阶覆盖、某刻蚀选择比）能查到机理与典型参数。
- **难度**: 进阶（手册，非线性阅读）
- **Endorsement evidence**:
  - `[type: course_syllabus]` MIT 6.152J reading（Vol.1 ISBN 9780961672133）(evidence: [T04-S002])
  - `[type: blog_secondary]` 被誉为「最权威的半导体工艺/纳米制造指南」+ 专利高频引用 (evidence: [T04-S032])
  - `[type: course_syllabus]` 多校研究生工艺课参考 (evidence: [T04-S030])
- **superseded_by**: 无单一继任；部分内容老化（停在 ~submicron MOSFET 时代，无 FinFET/EUV）。旧版仍值得读：单元工艺物理与化学机理（CVD/刻蚀/清洗）衰减慢，仍是最详尽手册。
- **替代品**: Plummer（更现代+建模）
- **如果只读 1 章**: 按需查（手册）—— 工艺整合 Vol.2 最有体系价值
- **可信度**: high · **Decay risk**: medium（前沿架构缺失，但机理层 low）

### 📖 4. Fabrication Engineering at the Micro- and Nanoscale (Campbell)

- **Author**: Stephen A. Campbell（U.Minnesota；IEEE Fellow）
- **Year**: 4th ed 2012（Oxford Series in EE & CE）
- **Type**: textbook（本科高年级/研一）
- **One-liner**: 可读性最好的 fab 单元工艺入门教材，配套 capstone 实验课。 (evidence: [T04-S015, T04-S002])
- **核心论点**: (1) IC 制造可拆为有限的基本单元工艺；(2) 入门应先建立 unit process 直觉再谈整合；(3) 实验 capstone 与理论并重。
- **读完得到什么**: 建立从光刻→刻蚀→沉积→掺杂→CMP 的完整 unit process 框架与直觉。
- **难度**: 入门-进阶
- **Endorsement evidence**:
  - `[type: figure_long]` Oxford 出版社官方页 + 作者 NSF Nano-Link 教育中心背景（出版社一手）(evidence: [T04-S015])
  - `[type: course_syllabus]` MIT 6.152J 推荐读物（Campbell, OUP 2001）(evidence: [T04-S002])
  - `[type: blog_secondary]` 多校微电子 fab 课广泛采用 (evidence: [T04-S015])
- **替代品**: Plummer（更深+建模）/ Jaeger《Introduction to Microelectronic Fabrication》
- **如果只读 1 章**: 光刻章（最直观切入）
- **可信度**: high · **Decay risk**: low-medium

### 📖 5. Fundamentals of Semiconductor Manufacturing and Process Control (May & Spanos)

- **Author**: Gary S. May（Georgia Tech）, Costas J. Spanos（UC Berkeley）
- **Year**: 2006（Wiley/IEEE Press）
- **Type**: textbook（制造系统 + 统计）
- **One-liner**: 唯一把 fab 当「统计制造系统」系统教的书 —— SPC / yield model / DOE / APC 的 canon。 (evidence: [T04-S003, T04-S016, T04-S034])
- **核心论点**: (1) 良率是主经济指标，可用缺陷密度模型预测；(2) 工艺须用 SPC 监控、DOE 找窗口、APC/FDC 闭环；(3) 制造 = 统计+物理的联合优化。 (evidence: [T04-S034])
- **读完得到什么**: 会读 SPC 控制图、设计 DOE 找工艺窗口、用 yield model 估缺陷密度、理解 APC/FDC 闭环。
- **难度**: 进阶
- **Endorsement evidence**:
  - `[type: course_syllabus]` MIT OCW 6.780 Semiconductor Manufacturing 主教材 (evidence: [T04-S003])
  - `[type: figure_long]` Wiley/IEEE Press 官方页 + 作者（May=GT校长级器件学者, Spanos=Berkeley）(evidence: [T04-S016])
  - `[type: blog_secondary]` Wiley-VCH 目录列 yield/SPC/DOE/APC 全章 (evidence: [T04-S034])
- **替代品**: Montgomery《Statistical Quality Control》（纯统计，非半导体专用）
- **如果只读 1 章**: Yield Modeling + SPC 章
- **可信度**: high · **Decay risk**: low（方法学衰减慢）

### 📖 6. Semiconductor Manufacturing Technology (Quirk & Serda)

- **Author**: Michael Quirk, Julian Serda
- **Year**: 2001（Pearson/Prentice Hall）
- **Type**: textbook（技师/操作层入门）
- **One-liner**: fab 技师与操作层的术语-设备-流程入门，门槛最低、覆盖最全景。 (evidence: [T04-S017])
- **核心论点**: (1) fab 是设备+工艺+洁净室纪律的系统；(2) 每道工序对应具体设备与产品要求；(3) 平衡 process 与 equipment 视角。
- **读完得到什么**: 看懂 fab 全景术语（CMP/damascene/DUV/low-k）、设备类型、工序顺序，建立产业直觉。
- **难度**: 入门
- **Endorsement evidence**:
  - `[type: course_syllabus]` community college / 4-year tech program 标准本 + 企业培训用 (evidence: [T04-S017])
  - `[type: blog_secondary]` 覆盖 Cu interconnect / dual damascene / DUV sub-micron / low-k / CMP (evidence: [T04-S017])
  - `[type: blog_secondary]` 666 页全景，行业培训广泛采用 (evidence: [T04-S017])
- **替代品**: Xiao Hong 肖国勇《Introduction to Semiconductor Manufacturing Technology》（同定位，中英版皆有）
- **如果只读 1 章**: 工艺总览章
- **可信度**: medium-high · **Decay risk**: medium（设备细节老化，全景 low）

---

### 📄 1. Cramming More Components onto Integrated Circuits (Moore, 1965)

- **Authors**: Gordon E. Moore（时任 Fairchild R&D 主管）
- **Venue + Year**: Electronics Magazine, vol 38 no 8, 1965-04-19, pp.114-117
- **URL**: T04-S013 (CHM 馆藏) / T04-S014 (GT .edu PDF)
- **One-liner**: Moore's Law 的起源文本 —— 集成度以指数增长，且由经济学（每芯片最低成本元件数）驱动。 (evidence: [T04-S013, T04-S014])
- **核心 idea**: 集成度每年翻倍（后修正为约每两年）；驱动力是经济而非纯物理。
- **为什么经典**: 定义了整个行业的节奏与自我实现预言（Carver Mead 命名为「law」）。
- **如何读**: 全文仅 4 页，从头读；注意它本质是经济论证不是物理定律。
- **读完得到什么**: 理解「微缩」首先是经济命题 —— 这是后面「成本墙 vs 物理墙」之争的根。
- **Endorsement evidence**: CHM 永久馆藏 (S013) + GT/.edu 重刊 (S014) + IEEE Xplore 重印 + 全行业引用。
- **后续/扩展**: Moore 1975 修正（每两年）；Dennard 1974（微缩的物理化）。
- **可信度**: high · **Decay risk**: low

### 📄 2. Design of Ion-Implanted MOSFETs with Very Small Physical Dimensions (Dennard et al., 1974)

- **Authors**: R. H. Dennard, F. H. Gaensslen, H.-N. Yu, V. L. Rideout, E. Bassous, A. R. LeBlanc（IBM）
- **Venue + Year**: IEEE J. Solid-State Circuits 9(5):256, 1974
- **URL**: T04-S004 (Nat. Academies 重印) / T04-S005 (IEEE 30 周年回顾)
- **One-liner**: Dennard scaling —— 恒电场等比微缩，尺寸×κ⁻¹ 则同时提密度/速度/功耗。 (evidence: [T04-S004, T04-S005])
- **核心 idea**: 维持电场恒定，按比例缩尺寸/电压/掺杂，得到可预测的器件改善规则。
- **为什么经典**: 把 Moore 的经济观察变成可执行的物理工程规则，主导工业数十年。
- **如何读**: 读 scaling 表（尺寸/电压/掺杂/延迟/功耗各量纲随 κ 变化）；配 Bohr 2007 回顾理解为何 ~2005 后失效。
- **读完得到什么**: 理解为何「频率不再随节点提升」—— Dennard 终结（漏电/功耗密度墙）是物理硬约束，非政策可改。
- **Endorsement evidence**: Nat. Academies Press 官方重印 (S004) + IEEE 30 周年专门回顾 (S005) + 全行业 canon。
- **后续/扩展**: Bohr「A 30 Year Retrospective」(S005)；广义微缩（generalized scaling）。
- **可信度**: high · **Decay risk**: low

### 📄 3. FinFET: Sub-50nm FinFET & Self-Aligned Double-Gate MOSFET (Hisamoto, Hu et al., 1999-2000)

- **Authors**: D. Hisamoto, Chenming Hu, X. Huang, W.-C. Lee, C. Kuo, L. Chang, J. Kedzierski, E. Anderson, H. Takeuchi 等（UC Berkeley + Hitachi）
- **Venue + Year**: IEDM 1999（Sub-50nm FinFET: PMOS）+ IEEE TED 2000（FinFET scalable to 20nm）
- **URL**: T04-S009 (NYCU 学术库) / T04-S008 (谱系参考)
- **One-liner**: 双栅鳍式结构靠多面栅控压制短沟道效应，使平面 CMOS 微缩续命到 20nm 以下。 (evidence: [T04-S009, T04-S008])
- **核心 idea**: 把沟道立起来做成 fin，栅从多面包裹 → 静电控制强 → 抑制 DIBL/Vt roll-off。
- **为什么经典**: 直接催生 Intel 22nm（2011）量产 FinFET，是 planar→3D 器件的转折，胡正明因此封神。
- **如何读**: 看器件截面图 + 短沟道指标（Idsat/SS/DIBL）对比平面；理解「为什么 3D 栅控胜出」。
- **读完得到什么**: 理解器件架构微缩链 FinFET→GAA→CFET 的第一性逻辑 = 不断加强栅对沟道的静电控制。
- **Endorsement evidence**: IEDM/TED 顶会 + 全行业量产采用 + Wikipedia 谱系 (S008) + 多校器件课。
- **后续/扩展**: GAA nanosheet (S021/S022)；CFET / forksheet (S023)。
- **可信度**: high · **Decay risk**: low

### 📄 4. Cu/low-κ Dual Damascene Interconnect (Edelstein et al., IBM, 1997)

- **Authors**: D. Edelstein 等（IBM；CMOS 7S 工艺）
- **Venue + Year**: IEDM 1997 Tech. Digest p.773（首个 Cu 大马士革产品工艺）
- **URL**: T04-S012（历史 + 引用）
- **One-liner**: 用铜大马士革 + 低介电替代铝互连，从 BEOL 解 RC 延迟瓶颈。 (evidence: [T04-S012])
- **核心 idea**: Cu 电阻率低+抗电迁移，但难刻蚀 → 改用「大马士革」镶嵌+CMP 平坦化；配 low-k 降电容。
- **为什么经典**: 成为此后所有先进节点 BEOL 的标准平台（dual damascene + CMP）。
- **如何读**: 理解「为什么不刻 Cu 而用 damascene」+ CMP 在其中不可或缺的角色。
- **读完得到什么**: 理解 BEOL 微缩动因（RC 延迟）与 Cu/low-k/CMP 三件套的耦合。
- **Endorsement evidence**: IEDM 1997 + 全行业 BEOL 标准 + Semiconductor Engineering 历史长稿 (S012)。
- **后续/扩展**: air-gap / Ru/Co 替代 Cu / 「what will replace dual damascene」之争 (S012)。
- **可信度**: high · **Decay risk**: low-medium（替代材料在演进）

### 📄 5. Atomic Layer Deposition: Surface Chemistry (Puurunen 2005) + Suntola ALE 谱系 (Puurunen 2014)

- **Authors**: Riikka Puurunen（综述）；奠基 Tuomo Suntola（Atomic Layer Epitaxy, 1970s-80s）
- **Venue + Year**: J. Appl. Phys. 97:121301 (2005)「Surface chemistry of ALD」；Chem. Vap. Deposition 20:332 (2014) 历史综述
- **URL**: T04-S025 (Puurunen 全文) / T04-S024 (Suntola 历史)
- **One-liner**: 自限性表面反应逐层成膜，是 high-k/HKMG 与保形薄膜的化学基础。 (evidence: [T04-S025, T04-S024])
- **核心 idea**: 交替自限性半反应 → 每循环一个原子层 → 极致厚度控制与保形性（高深宽比）。
- **为什么经典**: high-k 栅介质（HfO2）量产、3D 结构保形覆盖的使能技术；Suntola 因此获 Millennium Prize。
- **如何读**: Puurunen 2005 读 TMA/H2O 案例的半反应机理；2014 读 ALE/ALD 的历史脉络。
- **读完得到什么**: 理解「为什么 ALD 能在原子尺度做保形薄膜」—— 自限性是关键，区别于 CVD。
- **Endorsement evidence**: 作者本人 own publication via VTT 托管 (S025) + Wiley CVD 历史综述 (S024) + high-k 量产采用。
- **后续/扩展**: ALE（原子层刻蚀，ALD 对偶）；area-selective ALD。
- **可信度**: high · **Decay risk**: low

### 📄 6. The Inception of CMP (Beyer/IBM, 专利 1985 + 集成 1992)

- **Authors**: Klaus D. Beyer（CMP 发明人，IBM）；集成论文多作者（IBM, Thin Solid Films 1992）
- **Venue + Year**: 首专利 1985（IBM）；「Integration of CMP into CMOS IC manufacturing」Thin Solid Films 1992
- **URL**: T04-S026（Beyer 本人 talk）/ T04-S027（IBM 集成论文 DOI）
- **One-liner**: 化学机械平坦化解决多层布线的形貌问题，是 STI 与 Cu 大马士革的使能工艺。 (evidence: [T04-S026, T04-S027])
- **核心 idea**: 化学软化 + 机械去除联合，把晶圆表面全局平坦化 → 使多层光刻聚焦可行。
- **为什么经典**: 取代 LOCOS 的 STI、Cu damascene 都依赖 CMP；它解锁了垂直微缩。
- **如何读**: 听 Beyer 本人「Inception of CMP」talk 看动机；读 IBM 1992 论文看集成（4M/16M DRAM）。
- **读完得到什么**: 理解 CMP 不是「抛光」而是微缩使能工艺，及 dishing/erosion 等过抛缺陷由来。
- **Endorsement evidence**: 发明人 originator 本人 talk (S026) + IBM 集成论文 DOI (S027) + STI/Cu 量产采用。
- **后续/扩展**: Cu CMP（S012 耦合）；slurry 化学演进。
- **可信度**: high · **Decay risk**: low

---

### 🎓 1. MIT 6.152J Micro/Nano Processing Technology

- **Lecturer**: MIT EECS / MSE 联合
- **Institution**: MIT（OCW 公开）
- **Format**: 讲座 + 洁净室 lab + reading
- **Duration**: 一学期
- **Year + 最近更新**: Fall 2005（OCW archived）
- **One-liner**: 单元工艺理论 + 洁净室实操经典，reading list 即半导体工艺隐性 canon（Plummer/Campbell/Wolf/Sze）。 (evidence: [T04-S002])
- **完整路径 vs 关键章节**: 完整 = 理论+lab；只看 readings + 光刻/刻蚀/CVD/扩散 lecture 即得 canon reading map。
- **难度/先修**: 进阶；先修器件物理
- **Endorsement evidence**: `[type: course_syllabus]` OCW 正式课程 reading list (S002) + 同系列 6.780 (S003)。
- **Last_updated**: 2005-09（archived；单元工艺基础衰减慢，前沿 EUV/GAA 不在内）
- **可信度**: high（机构）· **Decay risk**: medium（前沿缺失，基础 low）

### 🎓 2. MIT 6.780 Semiconductor Manufacturing

- **Lecturer**: MIT EECS（Spanos 体系相关）
- **Institution**: MIT（OCW）
- **Format**: 讲座 + reading
- **Year + 最近更新**: Spring 2003（OCW archived）
- **One-liner**: 把 fab 当统计制造系统教 —— SPC/yield/DOE/APC，配 May&Spanos 教材。 (evidence: [T04-S003])
- **完整路径 vs 关键章节**: 完整学制造系统方法学；只看 yield modeling + SPC + DOE 模块即核心。
- **难度/先修**: 进阶；先修概率统计
- **Endorsement evidence**: `[type: course_syllabus]` OCW reading list 列 May&Spanos (S003)。
- **Last_updated**: 2003-02（archived；方法学衰减慢）
- **可信度**: high · **Decay risk**: low

### 🎓 3. U.Washington EE531 Physics & Modeling of Nanoscale VLSI Devices

- **Lecturer**: Scott Dunham（UW）
- **Institution**: University of Washington
- **Format**: 讲座 + reading（.edu syllabus）
- **Year + 最近更新**: rolling（课程主页持续维护）
- **One-liner**: 纳米器件物理 + 建模，衔接器件物理→工艺微缩约束（reading 含 Sze/Plummer）。 (evidence: [T04-S030])
- **完整路径 vs 关键章节**: 完整建模训练；reading list 作 canon 交叉印证。
- **难度/先修**: 高阶；先修器件物理
- **Endorsement evidence**: `[type: course_syllabus]` UW .edu 课程页 reading list (S030)。
- **Last_updated**: rolling（按 .edu 课程页）
- **可信度**: high（机构）· **Decay risk**: medium

### 🎓 4. ASML / imec 公开技术 readouts（canon-adjacent, rolling）

- **Lecturer**: ASML / imec 技术团队（非传统课程）
- **Institution**: ASML（设备）/ imec（研究机构）
- **Format**: 技术博客 + 白皮书 + 公开 readout（rolling）
- **Year + 最近更新**: rolling, last key content 2024-2025: High-NA EUV (0.55NA, EXE:5000) (S020); forksheet→CFET 架构 (S023); BSPDN 背面供电路线 (IRDS S007)
- **One-liner**: 前沿设备/器件架构的一手 vendor/研究路线，弥补教材课程在 EUV/GAA/CFET/BSPDN 上的时效缺口。 (evidence: [T04-S020, T04-S023])
- **完整路径 vs 关键章节**: 按主题挑：High-NA EUV (ASML)、GAA/forksheet/CFET (imec)、roadmap (IRDS)。
- **难度/先修**: 进阶；先修单元工艺基础
- **Endorsement evidence**: `[type: conf_citation]` IEDM/IRDS 引用 (S006/S007/S019) + 厂商一手 (S020/S022/S023)。
- **Last_updated**: 2024-2025（rolling，Decay risk: high —— 前沿层）
- **可信度**: high（厂商一手，但单面之词需 ≥2 source 交叉）· **Decay risk**: high

---

## Core Concepts — Tier 划分与详情（择要展开）

### 💡 Moore's Law `tier-1`
- **One-liner**: 集成度随时间指数增长、由每芯片最低成本元件数（经济）驱动的规律。
- **来源**: `[primary]` Moore 1965 (S013/S014)；`[significant follow-up]` Moore 1975 修正
- **关联概念**: Dennard scaling（物理实现）、PPAC、成本墙
- **当前理解 vs 原始**: 原始是经济观察；今被误读为「每两年性能翻倍」。已放缓（成本/物理墙）。
- **为什么进 canon**: 定义行业节奏。
- **常见误用**: 当成物理定律 / 当成「性能」翻倍（实为「集成度/成本」）。
- **Endorsement**: S013 + S014 + IEEE 重印 + 全行业。 (evidence: [T04-S013, T04-S014])

### 💡 Dennard scaling `tier-1`
- **One-liner**: 恒电场等比微缩，按 κ 缩尺寸/电压/掺杂同时得密度+速度+功耗改善。
- **来源**: `[primary]` Dennard 1974 (S004)；`[significant follow-up]` Bohr 30 年回顾 (S005)
- **关联概念**: 短沟道效应、功耗墙、Dennard 终结
- **当前理解 vs 原始**: ~2005 后因漏电/功耗密度失效（Dennard 终结），频率停滞，转向多核+等效微缩。
- **为什么进 canon**: 把 Moore 经济观察物理化为工程规则。
- **常见误用**: 以为微缩可无限续 —— 物理硬约束（漏电/隧穿）使其终结。
- **Endorsement**: S004 + S005 + 全行业。 (evidence: [T04-S004, T04-S005])

### 💡 节点命名营销 / N3≠3nm `tier-1`（行业批判核心，红线）
- **One-liner**: 「N3/N2」是营销代号，**不等于物理栅长 3nm/2nm**；真尺度看 gate pitch / metal pitch / 逻辑密度（MTr/mm²）。
- **来源**: `[primary]` IRDS More Moore 真尺度参数 (S007)；TechInsights/分析师拆解 (S028)
- **关联概念**: PPAC、等效微缩、DTCO
- **当前理解**: 业内共识节点名脱钩物理尺寸；外行普遍误读。
- **为什么进 canon**: intake warning 明确要求拆穿此营销叙事。
- **常见误用**: 「N nm = 物理 N 纳米栅长」「数字越小越先进」（须按真尺度 + PPAC 判断）。
- **Endorsement**: IRDS 真参数 (S007) + 专业分析机构拆解共识 (S028)。 (evidence: [T04-S007, T04-S028])

### 💡 PPAC `tier-1`
- **One-liner**: Performance-Power-Area-Cost 四角权衡，先进节点核心评价框架。
- **来源**: `[primary]` TSMC DTCO blog (S018) / IEDM DTCO/STCO (S019)
- **关联概念**: DTCO、DFM、yield
- **为什么进 canon**: 替代「单看节点数字」的正确评价维度。
- **常见误用**: 只看 Performance/Area，忽略 Cost/良率（Cost 含良率）。
- **Endorsement**: S018 + S019 + IRDS。 (evidence: [T04-S018, T04-S019])

### 💡 DTCO / STCO `tier-1` / `tier-2`
- **One-liner**: 设计-工艺协同优化（DTCO）/ 系统-工艺协同（STCO）以最大化 PPAC。
- **来源**: `[primary]` TSMC (S018) + IEDM 2023 Arm SC (S019) + IRDS (S007)
- **关联概念**: PPAC、DFM、standard cell、BSPDN
- **当前理解**: 从 dimensional scaling 主导转向 DTCO/STCO 协同（等效微缩主力）。
- **为什么进 canon**: 后摩尔时代提密度的主路径。
- **常见误用**: 当成纯设计 EDA 概念（实为设计+工艺联合）。
- **Endorsement**: S018 + S019 + S007。 (evidence: [T04-S018, T04-S019, T04-S007])

### 💡 短沟道效应 SCE / DIBL `tier-1`
- **One-liner**: 沟道变短时栅失去静电控制，出现 Vt roll-off 与漏致势垒降低（DIBL），漏电激增。
- **来源**: `[primary]` Sze 器件物理 (S031) + FinFET 动因 (S009)；解释 (S033)
- **关联概念**: FinFET/GAA（解法）、Dennard scaling、热预算
- **为什么进 canon**: 是 planar→FinFET→GAA 架构演进的第一性驱动。
- **常见误用**: 以为靠工艺调参可解 —— 本质是静电几何问题，须改器件架构。
- **Endorsement**: S031 + S009 + S033。 (evidence: [T04-S031, T04-S009])

### 💡 浸没式光刻 193i / EUV / high-NA `tier-1`
- **One-liner**: 193i 注水提 NA>1 延寿 DUV；EUV 13.5nm 反射式；high-NA(0.55) 把单曝光推到 8nm。
- **来源**: `[primary]` ASML High-NA (S020) + SPIE immersion (S010/S011) + IRDS Litho (S006)
- **关联概念**: 多重曝光、OPC、overlay、mask
- **当前理解**: EUV 量产（N7/N5 起）；high-NA ramp 中；ASML EUV 实质垄断。
- **为什么进 canon**: 光刻是微缩的总开关。
- **常见误用**: 「有 EUV 就能做先进制程」—— 设备必要非充分（材料/工艺/整合/良率缺一不可）。
- **Endorsement**: S020 + S010/S011 + S006。 (evidence: [T04-S020, T04-S006])

### 💡 良率 yield / D0 缺陷密度 / SPC-FDC-APC `tier-1`
- **One-liner**: 良率是 fab 主经济指标，缺陷密度 D0 建模预测；SPC/FDC/APC 闭环监控控制工艺。
- **来源**: `[primary]` May & Spanos (S016/S034/S003)
- **关联概念**: DFM、工艺窗口、DOE、良率爬坡
- **当前理解**: 数字类高危 —— D0/yield 曲线属商业机密，个体差异大，引用须标论文/厂商或「业内估计」。
- **为什么进 canon**: 良率决定经济成败，是工程现实硬约束。
- **常见误用**: 「良率不是问题」「设备买齐就高良率」—— 良率爬坡是长期 know-how 壁垒。
- **Endorsement**: S016 + S034 + S003。 (evidence: [T04-S016, T04-S003])

### 💡 器件架构链 FinFET→GAA nanosheet→CFET `tier-1` / BSPDN `tier-2`
- **One-liner**: 栅控持续增强的架构演进（鳍→环栅纳米片→互补堆叠）；BSPDN 把供电移到背面省正面面积。
- **来源**: `[primary]` FinFET (S009) + GAA (S021/S022) + CFET/forksheet imec (S023) + BSPDN IRDS (S007)
- **关联概念**: 短沟道效应、DTCO、等效微缩
- **当前理解**: N2 起 GAA 量产（TSMC/Samsung/Intel）；CFET 为下一代；BSPDN 2025 起导入。
- **为什么进 canon**: 后 FinFET 微缩主路径。
- **常见误用**: 把架构名当节点物理尺寸。
- **Endorsement**: S009 + S021 + S022 + S023 + S007。 (evidence: [T04-S022, T04-S023, T04-S007])

### 💡 Cu/low-k 大马士革 + RC 延迟 + CMP `tier-1`
- **One-liner**: BEOL 用 Cu 镶嵌 + low-k 解 RC 延迟，靠 CMP 平坦化使能；过抛产生 dishing/erosion。
- **来源**: `[primary]` Edelstein/IBM (S012) + CMP Beyer (S026/S027)
- **关联概念**: FEOL/MOL/BEOL、热预算、缺陷
- **为什么进 canon**: BEOL 标准平台 + 微缩使能工艺。
- **常见误用**: 把 CMP 当「抛光」而非微缩使能工艺。
- **Endorsement**: S012 + S026 + S027。 (evidence: [T04-S012, T04-S027])

### 💡 ALD / ALE `tier-1`
- **One-liner**: 自限性表面反应逐层成膜（ALD）/ 去膜（ALE），高深宽比保形 + 原子级控制。
- **来源**: `[primary]` Puurunen (S025) + Suntola 历史 (S024)
- **关联概念**: high-k/HKMG、CVD（对比）、多重曝光
- **为什么进 canon**: high-k 栅介质与 3D 保形覆盖使能。
- **常见误用**: 混同 CVD —— ALD 的自限性是关键区别。
- **Endorsement**: S025 + S024 + 量产采用。 (evidence: [T04-S025, T04-S024])

### 💡 多重曝光 SADP/SAQP + OPC + overlay `tier-2`
- **One-liner**: 自对准多重图形化突破单曝光分辨率；OPC 补偿衍射；overlay 管层间对准 budget。
- **来源**: `[primary]` IRDS Litho (S006)
- **关联概念**: 浸没式、EUV、process window
- **为什么进 canon**: EUV 普及前/补充的分辨率手段，仍广泛使用。
- **常见误用**: 以为 EUV 全面取代多重曝光（成本/层次仍混用）。
- **Endorsement**: S006 + S002 (教材)。 (evidence: [T04-S006])

### 💡 FEOL/MOL/BEOL + 热预算 + 工艺窗口 `tier-2`
- **One-liner**: 前道器件/中段接触/后道互连三模块；热预算约束掺杂剖面；工艺窗口 = 良率可接受的参数空间。
- **来源**: `[primary]` Plummer (S001) + Wolf (S032) + May&Spanos 工艺窗口 (S016)
- **关联概念**: DOE（找窗口）、模块协同、SPC
- **为什么进 canon**: 工艺整合的基本词汇与约束。
- **常见误用**: 以为单模块最优 = 整体最优（须模块间 trade-off）。
- **Endorsement**: S001 + S032 + S016。 (evidence: [T04-S001, T04-S016])

> 其余 tier-2 概念（dimensional vs equivalent scaling、Dennard 终结、DFM、dishing-erosion 等）在总览表已列来源，不逐条展开。

---

## Phase 2 提炼提示

### 反复出现 ≥ 3 个 canon 都讨论的核心 idea（候选行业心智模型）
- **「物理硬约束 ⇄ 良率/成本经济约束」的双重张力**：出现于 Dennard 1974 (S004) / May&Spanos (S016) / PPAC-DTCO (S018/S019) / Sze 器件物理 (S031) → **头号候选心智模型**：任何工艺决策都是在物理可行性与良率/成本之间求解，二者皆不可让渡。
- **「微缩 = 不断加强栅对沟道的静电控制」**：出现于 Dennard (S004) / 短沟道-FinFET (S009) / GAA-CFET (S021/S023) → 候选心智模型：器件架构演进有单一第一性逻辑（栅控）。
- **「设备/工艺是必要非充分，良率爬坡是 know-how 壁垒」**：出现于 May&Spanos yield (S016) / EUV warning (S020) / Quirk 全景 (S017) → 候选心智模型：拆穿「买到 EUV 就能做先进制程」。
- **「节点名是营销，真尺度看 pitch + PPAC」**：IRDS (S007) / 分析师拆解 (S028) / DTCO (S018) → 候选 playbook：评价节点先换算真参数。

### 智识谱系种子
- **器件物理-微缩奠基派**：奠基 = Moore 1965 (S013) + Dennard 1974 (S004) + Sze 器件物理 (S031)；当前代表 = 与 Track 01 figure **Gordon Moore / Robert Dennard / 胡正明 Chenming Hu** 关联。
- **3D 器件架构派（Berkeley 系）**：奠基 = FinFET (Hisamoto/Hu, S009)；当前代表 = 胡正明 + Tsu-Jae King Liu（Track 01）+ imec CFET/forksheet (S023)。
- **统计制造/良率工程派**：奠基 = May & Spanos (S016) + IBM CMP/damascene 集成 (S027)；当前代表 = fab 良率/APC 体系。
- **光刻使能派**：奠基 = 浸没式 (Burn Lin, S010) + EUV (ASML, S020)；当前代表 = 与 Track 01 figure **林本坚 / Martin van den Brink** 关联。
- **路线图/协同优化派**：奠基 = ITRS→IRDS (S006/S007) + DTCO (S018/S019)；后摩尔时代等效微缩主张。
- **主要分歧（still-debated within canon）**：
  - 「摩尔定律已死」vs「等效微缩继续」（Dennard 终结后路线之争）
  - 前道 dimensional 微缩 vs 先进封装 chiplet 异构集成 谁是未来
  - DTCO/STCO 协同优化 vs 单模块极致优化
  - 节点命名营销化 —— 业内共识脱钩物理，但科普叙事仍混淆

### 核心概念 → 候选 playbook
- **节点评价 playbook**：遇到「N nm 节点」→ 别信数字，换算 gate pitch/metal pitch/逻辑密度 + 看 PPAC + 标 TechInsights/IRDS 来源（拆穿营销名）。
- **架构选择 playbook**：遇到短沟道/漏电问题 → 优先想器件架构（FinFET/GAA/CFET 加强栅控），而非单纯工艺调参（静电几何问题）。
- **良率诊断 playbook**：遇到良率问题 → SPC 异常诊断 → DOE 找工艺窗口 → 缺陷分类 + 根因分析（FA）→ 工艺改善；良率爬坡是长期 know-how，非一次性。
- **「能否做先进制程」playbook**：判断时检查设备+材料+工艺+整合+良率五要素是否齐备 —— 设备（如 EUV）是必要非充分条件。
- **BEOL 微缩 playbook**：互连延迟主导时 → Cu/low-k/CMP 三件套 + 考虑替代材料（Ru/Co/air-gap）。

### 冷僻 / 信号薄弱自检
- 必读书 ≥ 3？ **是（7 本，全 retain）** ✅
- paper ≥ 5？ **是（6 篇 seminal）** ✅
- 课程 ≥ 2？ **是（4 个，2 个 MIT 正式 + UW + ASML/imec rolling）** ✅
- 概念 ≥ 15？ **是（24 个，tier-1/tier-2 已标）** ✅
- Endorsement evidence ≥ 3 处的项 ≥ 50%？ **是（每本书/论文 ≥ 3，含 ≥1 course_syllabus 或 figure_long/originator talk）** ✅
- 一手 endorsement ≥ 50%？ **是（manifest verified+surrogate ≈ 62%）** ✅
- **结论：canon 维度信号充足（data-rich 行业）**。诚实边界标注：
  - **课程时效缺口**：MIT 6.152J/6.780 是 archived（2003/2005），前沿 EUV/GAA/CFET/BSPDN 不在传统课程内，靠 ASML/imec/IRDS rolling vendor 路线补 —— 这部分 Decay risk: high，须按 last_checked 刷新。
  - **中文圈 canon 偏 en**：教材+顶会论文几乎全英文（符合 intake warning）；中文教材（肖国勇/施敏中译）是入门佐证，非独立 canon 来源。zh-CN 黑名单（知乎/公众号/百度百科/CSDN）严格排除，未入 manifest。
  - **vendor 一手单面之词**：ASML/TSMC/Samsung/imec 的技术页是 verified_primary 但属厂商一面之词，mental model 层须 ≥2 source 交叉（已在 evidence 中交叉挂）。
  - **数字类高危**：节点参数/良率/市占率/成本须按 warning 标来源或「业内估计」，本 canon 文件不直接断言具体数值，留给 Track 02/05 + Phase 2 处理。
