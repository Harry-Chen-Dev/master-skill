# Track 06 — Glossary (术语 + 标准 + 法规 + 认证)

> 行业: Semiconductor Process Engineering / 半导体芯片制造工艺 · locale=global · profile=practitioner
> 数据厚度: data-rich（IEDM/VLSI/IRPS 论文 + 教材 canon + IRDS 路线图 + 设备/代工厂官方技术页 + gov 管制原文皆可机械验证一手）。本 track verified_primary 比例稳过阈值。
> 收集日期: 2026-06-21

## Source Manifest

| source_id | url | bucket | last_checked | author/host | one-line note |
|-----------|-----|--------|--------------|-------------|---------------|
| T06-S001 | https://irds.ieee.org/images/files/pdf/2024/2024IRDS_MM.pdf | verified_primary | 2026-06-21 | IEEE IRDS | 2024 More Moore 路线图原文 — 标准机构官方 spec, gate pitch G / metal pitch M / DTCO / CFET / BSPDN 定义 |
| T06-S002 | https://irds.ieee.org/images/files/pdf/2024/2024IRDS_MET.pdf | verified_primary | 2026-06-21 | IEEE IRDS | 2024 Metrology 章 — BSPDN 量测需求, overlay/CD 量测路线 |
| T06-S003 | https://www.federalregister.gov/documents/2023/10/25/2023-23049/export-controls-on-semiconductor-manufacturing-items | verified_primary | 2026-06-21 | BIS / Federal Register | 2023-10 SME 出口管制原文, ECCN 3B001/3B002, 16nm DUV 门槛 |
| T06-S004 | https://www.asml.com/en/products/euv-lithography-systems/twinscan-exe-5200b | verified_primary | 2026-06-21 | ASML | high-NA EUV (NA 0.55) EXE:5200B 官方技术页, 8nm 分辨率 |
| T06-S005 | https://en.wikipedia.org/wiki/3_nm_process | secondary | 2026-06-21 | Wikipedia | N3 节点命名 vs 物理尺度脱钩, N3 CPP 45nm / MMP 23nm |
| T06-S006 | https://en.wikipedia.org/wiki/2_nm_process | secondary | 2026-06-21 | Wikipedia | N2 命名脱钩, 20A=Intel 命名, CPP 45 / MMP 20nm |
| T06-S007 | https://semiengineering.com/a-node-by-any-other-name/ | secondary | 2026-06-21 | Semiconductor Engineering | 节点命名营销化业内长稿 |
| T06-S008 | https://en.wikichip.org/wiki/technology_node | secondary | 2026-06-21 | WikiChip | technology node 定义 + 历史脱钩 |
| T06-S009 | https://spectrum.ieee.org/a-better-way-to-measure-progress-in-semiconductors | secondary | 2026-06-21 | IEEE Spectrum | 用密度/MTr/mm² 取代节点名衡量进步 |
| T06-S010 | https://en.wikipedia.org/wiki/Multiple_patterning | secondary | 2026-06-21 | Wikipedia | SADP/SAQP/LELE/LELELE 定义, 76nm 单曝光极限, SAQP 到 19nm pitch |
| T06-S011 | https://en.wikipedia.org/wiki/Photomask | secondary | 2026-06-21 | Wikipedia | photomask/reticle 定义, EUV 反射式 Mo/Si 多层 |
| T06-S012 | https://www.photomaskportal.com/terminology.html | secondary | 2026-06-21 | Photomask Portal | mask/reticle/CD/photoresist 术语表 |
| T06-S013 | https://corial.plasmatherm.com/en/technologies/ale-atomic-layer-etching | verified_primary | 2026-06-21 | Plasma-Therm (vendor) | ALE 循环自限定 vendor 技术页 |
| T06-S014 | https://plasma.oxinst.com/technology/atomic-layer-etching | verified_primary | 2026-06-21 | Oxford Instruments (vendor) | ALE 表面改性+去除两步, 选择比 vendor 页 |
| T06-S015 | https://www.veteksemicon.com/news/what-is-dishing-and-erosion-in-the-cmp-process.html | secondary | 2026-06-21 | Vetek | CMP dishing/erosion 定义 |
| T06-S016 | https://pubs.aip.org/aip/apr/article/6/2/021302/570185/Conformality-in-atomic-layer-deposition-Current | verified_primary | 2026-06-21 | AIP Applied Physics Reviews | ALD conformality / step coverage 综述论文 |
| T06-S017 | https://en.wikipedia.org/wiki/Ion_implantation | secondary | 2026-06-21 | Wikipedia | 离子注入 dose/energy 定义 |
| T06-S018 | https://www.sciencedirect.com/topics/engineering/dopant-activation | verified_primary | 2026-06-21 | ScienceDirect/Elsevier | dopant activation, RTA/spike/laser anneal 热预算 |
| T06-S019 | https://yieldwerx.com/blog/statistical-yield-limits-semiconductor-production/ | secondary | 2026-06-21 | yieldWerx | D0 Murphy 良率模型, SPC 统计良率上限 |
| T06-S020 | https://www.semiconductors.org/wp-content/uploads/2018/08/YieldEnhanc2003.pdf | surrogate_primary | 2026-06-21 | SIA (industry assoc) | 良率增强方法学, 行业协会(association)自有发布 |
| T06-S021 | https://orbitskyline.com/blog/advanced-process-control-apc-reducing-variability-in-semiconductor-manufacturing/ | secondary | 2026-06-21 | Orbit&Skyline | APC run-to-run / feedforward-feedback 定义 |
| T06-S022 | https://semiconductorx.com/packaging-cowos.html | secondary | 2026-06-21 | SemiconductorX | CoWoS 三层堆叠 (chip-on-wafer-on-substrate) 定义 |
| T06-S023 | https://anysilicon.com/cowos-package/ | secondary | 2026-06-21 | AnySilicon | CoWoS interposer + TSV 结构 |
| T06-S024 | https://www.wevolver.com/article/what-is-hbm-high-bandwidth-memory-deep-dive-into-architecture-packaging-and-applications | secondary | 2026-06-21 | Wevolver | HBM stacked DRAM + TSV + 2.5D 共封 |
| T06-S025 | https://newsletter.semianalysis.com/p/the-future-of-the-transistor | secondary | 2026-06-21 | SemiAnalysis | FinFET→GAA→CFET 演进, 器件路线 |
| T06-S026 | https://www.synopsys.com/blogs/chip-design/what-are-gate-all-around-gaa-transistors.html | verified_primary | 2026-06-21 | Synopsys (vendor) | GAA nanosheet 环绕栅定义 |
| T06-S027 | https://www.imec-int.com/en/articles/performance-boosters-scale-monolithic-cfet-across-multiple-logic-technology-nodes | verified_primary | 2026-06-21 | imec | CFET N/P 垂直堆叠, 单片 CFET 多节点 |
| T06-S028 | https://mys.mapyourshow.com/mys_shared/iedm23/handouts/29-6_Wed_29111.pdf | verified_primary | 2026-06-21 | IEDM 2023 (Intel) | CFET demonstration 顶会论文 handout |
| T06-S029 | https://www.14644.dk/semiconductor-manufacturing-and-cleanroom-requirements | secondary | 2026-06-21 | 14644.dk | ISO 14644 洁净室级别 (Class 1-9) 用于 fab |
| T06-S030 | https://www.federalregister.gov/documents/2023/10/25/2023-23049/export-controls-on-semiconductor-manufacturing-items | verified_primary | 2026-06-21 | BIS | (同 S003) entity list / SME ECCN |
| T06-S031 | https://www.congress.gov/crs-product/R48642 | verified_primary | 2026-06-21 | Congress CRS | 美对华先进半导体出口管制综述 (gov 立法机构) |
| T06-S032 | https://semianalysis.com/2023/02/04/a-century-of-moores-law/ | secondary | 2026-06-21 | SemiAnalysis | 摩尔定律演化分析 |
| T06-S033 | https://www.imec-int.com/en/semiconductor-education-and-workforce-development/microchips/moores-law/moores-law-dead | verified_primary | 2026-06-21 | imec | "摩尔定律已死?" 等效微缩科普, dimensional vs equivalent |
| T06-S034 | https://en.wikipedia.org/wiki/Process_design_kit | secondary | 2026-06-21 | Wikipedia | PDK = foundry 提供的工艺模型文件集 |
| T06-S035 | https://semiengineering.com/a-guide-to-advanced-process-design-kits/ | secondary | 2026-06-21 | Semiconductor Engineering | PDK/DFM/DTCO 进阶指南 |
| T06-S036 | https://semiengineering.com/metrology-options-increase-as-device-needs-shift/ | secondary | 2026-06-21 | Semiconductor Engineering | OCD/scatterometry/CD-SEM/ellipsometry 对比 |
| T06-S037 | https://tsi.com/electronics-manufacturing/learn/main-sources-of-particle-shedding-and-possible-impacts-on-yield | secondary | 2026-06-21 | TSI | particle 颗粒源 + 良率影响 |
| T06-S038 | https://www.wevolver.com/article/reactive-ion-etching | secondary | 2026-06-21 | Wevolver | RIE/ICP-RIE 等离子刻蚀机理 |
| T06-S039 | https://www.tomshardware.com/tech-industry/tsmc-says-it-doesnt-care-if-moores-law-is-alive-or-dead-if-technology-keeps-scaling-3d-chip-packaging-fuels-continued-advances | secondary | 2026-06-21 | Tom's Hardware | TSMC VP 原话: 不在乎死活, 只要 scaling 继续 (含 3D 封装) |
| T06-S040 | https://newsroom.intel.com/intel-foundry/intel-foundry-opens-new-frontier-chipmaking | verified_primary | 2026-06-21 | Intel (vendor) | Intel 收 high-NA EUV, 用于 14A |

---

## 总览（按 type 分组）

### Tier 1 — 核心必懂（22 个）

| 术语 | Type | Insider def | Outsider tell | Last_updated |
|------|------|-------------|---------------|--------------|
| 制程节点 process node | term | 一代工艺平台的营销名（密度/性能/功耗代际），**不是**物理尺寸 | "N3=物理 3nm 栅长" — 错，真尺度看 CPP/MMP/MTr/mm² | 2026 |
| 流片 tape-out | term | 设计冻结、版图交付给 fab 进 mask/制造的里程碑事件 | 当成"打印一次"；其实是不可逆的高成本节点，错一版掩膜成本巨大 | low decay |
| 良率 yield | term | 单位晶圆上合格 die 占比，主经济指标 | 当成"质检通过率"；fab 里它是成本/竞争力本身，good die per wafer | low |
| 缺陷密度 D0 | term/acronym | 单位面积随机致命缺陷数，Murphy 模型里 Y=e^(−D0·A) 的核心参数 | 以为"越低越好就行"；它是良率建模与商业机密的硬核数字 | low |
| 关键尺寸 CD | term/acronym | wafer 上目标最小特征宽度，CD-SEM 量测 | 当成"芯片大小"；CD 是单个特征的线宽/孔径 | low |
| 套刻 overlay | term | 上下层图案的对准误差（不是单层 CD） | 与"分辨率/CD"混用；overlay 是层间对准，多重曝光下是良率杀手 | low |
| 掩膜 reticle / mask | term | 存图案的母版，光刻投影到 wafer；EUV 是反射式 | reticle 与 wafer 混；EUV mask 是 Mo/Si 多层反射镜不是透光玻璃 | low |
| 光刻 lithography | term | 把 mask 图案曝光转移到光刻胶的步骤；fab 节奏中枢 | "光刻机就是一切" — 刻蚀/沉积/CMP/量测/良率缺一不可 | low |
| EUV | acronym | 13.5nm 极紫外, 反射式光学, ASML 独家 | 读 "ee-you-vee" 字母 vs 内行也说字母但知道≠万能 | medium |
| DUV | acronym | 深紫外(193nm ArF)，浸没式 193i 是先进 DUV 主力 | 以为 DUV 过时；多重曝光+193i 仍是 7/5nm 主力工序 | low |
| 多重曝光 multi-patterning | term | 用多次曝光/spacer 突破单次光刻分辨率极限(SADP/SAQP/LELE) | 以为"曝一次搞定"；单 193i 极限 ~76nm pitch，要拆成多步 | low |
| FinFET | acronym/term | 立体鳍式栅(三面包栅)，胡正明发明，22nm 起主流 | 以为是"新封装"；它是器件架构，2011 量产至今 | low |
| GAA / nanosheet | acronym/term | 环绕栅纳米片，栅四面包沟道，N2 起接替 FinFET | "比 FinFET 小一号"；是栅控架构换代不是单纯缩小 | medium |
| 工艺窗口 process window | term | 配方参数能稳定产出合格结果的容差范围 | 以为"设好就行"；找窗口靠 DOE，窗口宽窄=可制造性 | low |
| 刻蚀选择比 selectivity | term | 刻目标材料 vs 刻掩膜/底层的速率比 | 与"刻蚀速率"混；选择比决定 profile 和 stop 控制 | low |
| 原子层刻蚀 ALE | acronym | 循环自限定逐原子层刻蚀（改性+去除两步），选择比可>1000:1 | 与 ALD 混（一个刻一个镀）；ALE 是刻不是镀 | medium |
| CMP | acronym | 化学机械抛光，全局平坦化，铜互连必备 | 当成"打磨光滑"；CMP 是工艺整合关键, dishing/erosion 是它的缺陷 | low |
| FEOL / MOL / BEOL | acronym | 前道(器件)/中道(接触)/后道(互连)三大整合段 | 以为只有"前道后道"；MOL 是先进节点新增的关键段 | low |
| 工艺整合 process integration | term | 把单元工艺串成可量产模块、管模块间 trade-off | 以为"按步骤跑就行"；整合 know-how 是 tacit 核心 | low |
| 良率爬坡 yield ramp | term | 新节点从低良率到量产良率的长期工程过程 | 以为"调好就量产"；ramp 数月到数年，是壁垒所在 | medium |
| 失效分析 FA | acronym | 对失效 die 做根因定位(物理/电学/材料)的逆向诊断 | 以为是"返修"；FA 是找根因反馈改工艺，不修单片 | low |
| BIS 出口管制 (EAR/Entity List) | regulation | 美商务部对华先进 SME/EUV/先进 DUV/AI 芯片的出口禁令体系 | 以为"只禁 EUV"；先进 DUV(16nm 及以下)、量测、entity list 全覆盖 | high |

### Tier 2 — 周边熟知（30 个）

| 术语 | Type | Insider def | Last_updated |
|------|------|-------------|--------------|
| 浸没式光刻 immersion (193i) | term | 镜头与 wafer 间充水提高有效 NA 的 193nm DUV | low |
| OPC | acronym | 光学邻近修正，预畸变 mask 图案补偿衍射 | low |
| high-NA EUV | term | NA 0.55 (vs 0.33) EUV，分辨率到 8nm，ASML EXE:5200B | high (S004,S040) |
| SADP / SAQP | acronym | 自对准双/四重曝光，spacer 工艺翻倍/四倍 pitch 密度 | low |
| LELE / LELELE | acronym | litho-etch litho-etch (双/三重曝光) 多步分解 | low |
| 光刻胶 photoresist (PR) | term | 感光高分子, 曝光后显影成图案掩蔽层 | low |
| RIE / ICP | acronym | 反应离子/电感耦合等离子刻蚀, 各向异性 profile | low |
| loading effect | term | 刻蚀速率随图案密度/开口面积变化的负载效应 | low |
| profile | term | 刻蚀/沉积后侧壁形貌(垂直度/锥角/底切) | low |
| CVD / PECVD / LPCVD | acronym | 化学气相沉积(及等离子/低压增强变体) | low |
| ALD | acronym | 原子层沉积, 自限定逐层, 近完美 step coverage | low |
| PVD / sputtering | acronym | 物理气相沉积(溅射), 方向性强 step coverage 差 | low |
| 外延 epitaxy (epi) | term | 单晶有序生长的薄膜(如 SiGe 源漏、Si epi) | low |
| 台阶覆盖 step coverage | term | 沟槽底/顶膜厚比, 衡量 conformality | low |
| 离子注入 ion implant | term | 高能掺杂离子打入硅(dose 剂量 + energy 能量) | low |
| 退火 anneal / RTA / laser anneal | term | 激活掺杂+修复晶格, 越短热预算越浅结(spike/laser) | low |
| 热预算 thermal budget | term | 工艺累计的温度×时间总量, 限制结深与扩散 | low |
| dishing / erosion | term | CMP 缺陷: 宽铜凹陷(dishing) / 密集区整体过抛(erosion) | low |
| SPC | acronym | 统计过程控制, 区分常规波动 vs 异常 | low |
| FDC | acronym | 故障检测与分类, 实时监设备状态防 yield 损失 | low |
| APC | acronym | 先进过程控制, run-to-run 前馈+反馈调配方 | low |
| DOE | acronym | 实验设计, 少量实验找工艺窗口与参数敏感度 | low |
| WAT / PCM | acronym | 晶圆验收测试/过程控制监测, scribe line 测试结构电参 | low |
| CD-SEM | acronym | 电镜量 top CD, 精度高但慢、半破坏、缺 profile | low |
| OCD / scatterometry | acronym | 光学 CD(散射术), 建模反演, 快、可测 profile/trench | low |
| CFET | acronym | 互补 FET, N/P 器件垂直堆叠, GAA 之后的 3D 路线 | high (S027,S028) |
| BSPDN | acronym | 背面供电网络, 供电挪到 wafer 背面释放正面布线 | high (S001) |
| DTCO / STCO | acronym | 设计-工艺/系统-工艺协同优化, 等效微缩抓手 | medium |
| PPAC | acronym | 性能-功耗-面积-成本四角权衡 | low |
| PDK / DFM | acronym | 工艺设计套件 / 面向可制造性设计 | low |

### Standards / Regulations / Certifications 时间轴（仅近 5 年有显著变化的）

| 名称 | Issued | Last revised | Decay | evidence |
|------|--------|--------------|-------|----------|
| BIS 半导体出口管制（EAR / Entity List） | 2022-10-07 (10/7 规则) | 2023-10-17 SME 规则 + 2024-12 扩大 | **high**（政策驱动, 12 月内常更新） | T06-S003, T06-S031 |
| IRDS（IRDS 接替 ITRS 2016, 年度更新） | 2016 (首版) | 2024 Update（More Moore / Metrology） | medium（年更, 大方向稳） | T06-S001, T06-S002 |
| ISO 14644-1 洁净室级别 | 1999 | 2015（现行版） | low（已稳定） | T06-S029 |
| high-NA EUV 商用导入（非标准, 设备代际事件） | 2024 (首台交付 Intel) | 2025-2026 量产爬坡 | high | T06-S004, T06-S040 |

> 长期稳定的 SEMI standards（E/F 系列）、JEDEC（封装/可靠性 JESD）只在主条目记发布机构, 不进时间轴。
> Certifications: 半导体工艺**无个人执业认证体系**（不像医师/CPA）。资质体现为 fab 内部 qualification + 设备/工艺 PCM 合格 + 客户 audit。本行业 Certification 类 ≈ **N/A**（标 N/A 而非缺漏）。

### 行业「外行破绽」高亮（最容易暴露的 10 条）

| 误用 | 内行实际意思 | 出现频率 |
|------|-------------|---------|
| "N3 = 物理 3 纳米栅长" | 节点名是营销代际, N3 实际 CPP≈45nm / MMP≈23nm | 极高 (S005,S006,S007) |
| "买到 EUV 就能做先进制程" | EUV 是必要非充分, 材料/刻蚀/整合/良率缺一不可 | 极高 (S033) |
| "光刻机就是一切" | fab 节奏中光刻是中枢但刻蚀/沉积/CMP/量测/良率并重 | 高 |
| "摩尔定律已死/没死" 二元 | dimensional scaling 放缓 ≠ 等效微缩(DTCO/3D)停止 | 高 (S033,S039) |
| "ALE 和 ALD 一回事" | 一个刻(etch)一个镀(deposition), 反向工艺 | 中 |
| "良率不是问题/很快追平" | yield ramp 数月到数年, D0 是商业机密硬约束 | 高 |
| "chiplet/先进封装是造假绕过微缩" | 是等效微缩的正统路线之一, 非作弊 | 中 (S039) |
| "GAA 就是更小的 FinFET" | 是栅控架构换代(环绕栅), 不是单纯缩小 | 中 (S025,S026) |
| "纳米数字越小越先进" | 真尺度看 MTr/mm² 密度/CPP/MMP, 不是节点名 | 极高 (S009) |
| "国产已突破/已量产先进制程" | EUV 管制下设备/材料/EDA/良率/成熟度有真实差距 | 高 (S003,S031) |

---

## Glossary 详条（Tier 1 全填 outsider-tell；Tier 2 关键条补填）

### 1. 制程节点 process node — technology node
- **Type**: term
- **Tier**: tier-1
- **Definition (insider)**: 一代工艺平台的营销代际标签（综合密度/性能/功耗相对上一代提升），**已与任何单一物理尺寸脱钩**。 (evidence: [T06-S005, T06-S007, T06-S008])
- **Definition (outsider-friendly)**: 像"第几代"的版本号，数字越小代表更新更密，但不是芯片上任何一根线的实际宽度。
- **Etymology**: 早期确实约等于栅长/半节距，约 22nm 之后被各代工厂营销化, 三家(TSMC/Intel/Samsung)同名节点参数不一致。 (evidence: [T06-S005])
- **常见误用 (outsider-tell)**:
  - `semantic_tell`: 外行说"3nm"指物理 3 纳米; 内行知道 N3 实际 CPP≈45nm, 最紧 MMP≈23nm。 (evidence: [T06-S005])
  - `usage_tell`: 拿节点名直接比不同厂"谁更先进"; 内行比 MTr/mm² 逻辑密度、CPP、MMP。 (evidence: [T06-S009])
- **关联术语**: CPP/gate pitch, metal pitch (MMP), MTr/mm², 等效微缩
- **是否被错位包装**: 是 — 代工厂用节点名做营销代际, 业内媒体明确批"a node by any other name"。 (evidence: [T06-S007])
- **Source**: [Primary] WikiChip technology_node (T06-S008); [Secondary] IEEE Spectrum (T06-S009)
- **可信度**: high · **Decay risk**: low（命名脱钩已是行业共识）

### 2. 流片 tape-out
- **Type**: term · **Tier**: tier-1
- **Definition (insider)**: 设计/版图冻结, OPC 处理后把 mask 数据交付制造的不可逆里程碑。 (evidence: [T06-S034])
- **Definition (outsider-friendly)**: 芯片设计"定稿付印"的那一刻, 之后进 fab 造实物。
- **Etymology**: 早期版图数据用磁带(tape)交付, 字面"把带子拉出来"。
- **常见误用 (outsider-tell)**: `semantic_tell` 外行以为"打印/制造一次试试"; 内行知道一版 mask set 成本极高, 错一版重做代价巨大, 流片是高赌注事件。
- **关联术语**: mask/reticle, PDK, OPC
- **Source**: [Secondary] PDK Wikipedia (T06-S034); [Secondary] SemiEngineering PDK 指南 (T06-S035)
- **可信度**: high · **Decay risk**: low

### 3. 良率 yield + 缺陷密度 D0
- **Type**: term/acronym · **Tier**: tier-1
- **Definition (insider)**: yield = 每片晶圆 good die 占比, 主经济指标; D0 = 单位面积随机致命缺陷数, Murphy 模型 Y = e^(−D0·A_crit)。 (evidence: [T06-S019])
- **Definition (outsider-friendly)**: 一片晶圆能切出多少颗好芯片; D0 衡量"每平方厘米平均有几个致命瑕疵"。
- **常见误用 (outsider-tell)**: `semantic_tell` 外行把 yield 当普通"质检合格率"; fab 里良率直接 = 成本与竞争力, good die per wafer 是经济命脉。`usage_tell` 把 D0 当"越低越好的简单指标"; 它是良率建模参数且属商业机密。
- **是否被错位包装**: 否 — D0/yield 定义稳定无营销收编。
- **变化历史**: Murphy 模型 1964 至今稳定。
- **Source**: [Secondary] yieldWerx (T06-S019); [Primary] SIA 良率增强白皮书 (T06-S020)
- **可信度**: high · **Decay risk**: low

### 4. 关键尺寸 CD + 套刻 overlay
- **Type**: term · **Tier**: tier-1
- **Definition (insider)**: CD = wafer 上目标最小特征宽度(CD-SEM 量); overlay = 上下层图案对准误差(与 CD 是两个独立维度)。 (evidence: [T06-S012, T06-S036])
- **常见误用 (outsider-tell)**: `usage_tell` 外行把 CD、overlay、分辨率混为一谈; 内行: CD 是单层线宽, overlay 是层间对准, 多重曝光下 overlay 是良率杀手。
- **关联术语**: CD-SEM, OCD, 多重曝光, 量测
- **Source**: [Secondary] Photomask Portal (T06-S012); SemiEngineering metrology (T06-S036)
- **可信度**: high · **Decay risk**: low

### 5. 掩膜 reticle / mask + 光刻 lithography
- **Type**: term · **Tier**: tier-1
- **Definition (insider)**: mask/reticle = 存图案母版, 投影到 wafer; **EUV mask 是 Mo/Si 多层反射镜**(非透光玻璃), 吸收层 TaBN。 (evidence: [T06-S011])
- **常见误用 (outsider-tell)**: `semantic_tell` 外行以为 EUV mask 像幻灯片透光; 内行: EUV 波长被几乎所有材料吸收, 必须全反射式光学+反射 mask。`usage_tell` "光刻机就是一切" — 内行: 刻蚀/沉积/CMP/量测/良率缺一不可。 (evidence: [T06-S033])
- **是否被错位包装**: 否。
- **Source**: [Secondary] Photomask Wikipedia (T06-S011); imec (T06-S033)
- **可信度**: high · **Decay risk**: low

### 6. EUV / DUV / high-NA EUV
- **Type**: acronym · **Tier**: tier-1 (EUV/DUV), tier-2 (high-NA)
- **Definition (insider)**: EUV=13.5nm 反射式(ASML 独家); DUV=193nm ArF, 浸没式 193i 是先进 DUV 主力; high-NA EUV=NA 0.55(vs 0.33), 分辨率 8nm, EXE:5200B。 (evidence: [T06-S004, T06-S010])
- **常见误用 (outsider-tell)**:
  - `pronunciation_tell`: 三者都念字母("ee-you-vee"/"dee-you-vee"); 但外行常误以为 DUV 已淘汰。
  - `semantic_tell`: "买到 EUV 就能做先进制程" — 内行: EUV 是必要非充分, 单 high-NA EUV 单次曝光不解决 overlay/缺陷/整合。 (evidence: [T06-S033, T06-S004])
  - `usage_tell`: 以为 7/5nm 全靠 EUV; 实际大量层仍用 193i + 多重曝光。
- **是否被错位包装**: 否（EUV/DUV 是物理定义）。
- **变化历史**: high-NA EUV 2024 首台交付 Intel, 2025-26 量产爬坡。 (evidence: [T06-S040])
- **Source**: [Primary] ASML EXE:5200B (T06-S004), Intel newsroom (T06-S040); [Secondary] Multiple patterning Wikipedia (T06-S010)
- **可信度**: high · **Decay risk**: EUV/DUV low, high-NA **high**

### 7. 多重曝光 multi-patterning (SADP / SAQP / LELE / LELELE)
- **Type**: term/acronym · **Tier**: tier-1 (总), tier-2 (各变体)
- **Definition (insider)**: 单次 193i 极限约 76nm pitch; 用 spacer 自对准(SADP/SAQP)或多次 litho-etch(LELE/LELELE)突破; SAQP 可达 ~19nm pitch。 (evidence: [T06-S010])
- **常见误用 (outsider-tell)**: `semantic_tell` 外行以为先进节点"曝一次成像"; 内行: 关键层要拆成 2-4 次曝光/spacer 工艺, 成本/缺陷/overlay 风险随之上升。
- **关联术语**: pitch, overlay, EUV(可减曝光次数)
- **Source**: [Secondary] Multiple patterning Wikipedia (T06-S010)
- **可信度**: high · **Decay risk**: low

### 8. 刻蚀选择比 selectivity + ALE + RIE/ICP + loading effect + profile
- **Type**: term/acronym · **Tier**: tier-1 (selectivity, ALE), tier-2 (其余)
- **Definition (insider)**: selectivity = 刻目标 vs 刻掩膜/底层速率比; ALE = 循环自限定逐原子层(改性+去除两步), 选择比可 >1000:1; RIE/ICP = 等离子各向异性刻蚀, ICP 独立调等离子密度与离子能量; loading effect = 刻蚀速率随开口密度变化; profile = 侧壁形貌。 (evidence: [T06-S013, T06-S014, T06-S038])
- **常见误用 (outsider-tell)**:
  - `semantic_tell` (ALE): 与 ALD 混淆 — ALE 是**刻**, ALD 是**镀**, 反向工艺。
  - `usage_tell` (selectivity): 与"刻蚀速率"混; 内行关心的是选择比(对底层/掩膜的相对速率)决定 stop 控制和 profile。
- **是否被错位包装**: 否。
- **Source**: [Primary-vendor] Plasma-Therm ALE (T06-S013), Oxford Instruments ALE (T06-S014); [Secondary] RIE Wevolver (T06-S038)
- **可信度**: high · **Decay risk**: ALE medium, 其余 low

### 9. CMP + dishing / erosion
- **Type**: acronym/term · **Tier**: tier-1 (CMP), tier-2 (dishing/erosion)
- **Definition (insider)**: CMP = 化学(slurry)+机械(pad)联合全局平坦化, 铜互连/low-k 多层必备; dishing = 宽铜(>5µm)凹陷; erosion = 密集图案区整体过抛, 均为 pattern-dependent 缺陷。 (evidence: [T06-S015])
- **常见误用 (outsider-tell)**: `semantic_tell` 外行把 CMP 当"打磨光滑"; 内行: CMP 是工艺整合关键步, 它**制造**的 dishing/erosion 缺陷本身是良率挑战, 要靠 slurry 化学+图案密度协同控。
- **是否被错位包装**: 否。
- **Source**: [Secondary] Vetek CMP (T06-S015)
- **可信度**: high · **Decay risk**: low

### 10. 沉积族 CVD/PECVD/LPCVD/ALD/PVD/epi + step coverage
- **Type**: acronym/term · **Tier**: tier-2
- **Definition (insider)**: CVD 气相反应成膜(介质层主力); ALD 自限定逐层, 近完美 step coverage 但慢; PVD(溅射)方向性强 step coverage 差; epi 单晶有序生长(SiGe 源漏); step coverage = 沟底/顶膜厚比, 衡量 conformality。 (evidence: [T06-S016])
- **常见误用 (outsider-tell)**: `usage_tell` 外行以为"沉积就是镀一层均匀膜"; 内行按 aspect ratio/conformality 需求选 CVD/ALD/PVD, high-AR 结构 ALD 不可替代。
- **Source**: [Primary] AIP ALD conformality 综述 (T06-S016)
- **可信度**: high · **Decay risk**: low

### 11. 离子注入 ion implant + 退火 anneal/RTA/laser + 热预算
- **Type**: term · **Tier**: tier-2 (注入/退火), tier-1 概念关联 (热预算)
- **Definition (insider)**: 注入 = 高能掺杂离子打入硅(dose 剂量 + energy 能量决定结深); 退火激活掺杂+修复晶格; RTA(秒级 1000-1200°C)/spike(毫秒)/laser anneal(纳秒熔融再结晶)越短热预算越浅结、激活率可 >99%。 (evidence: [T06-S017, T06-S018])
- **常见误用 (outsider-tell)**: `usage_tell` 外行以为"掺杂=注入完成"; 内行: 注入后必须退火激活, 且热预算约束(扩散 vs 激活)是浅结工程核心 trade-off。
- **Source**: [Secondary] Ion implant Wikipedia (T06-S017); [Primary] ScienceDirect dopant activation (T06-S018)
- **可信度**: high · **Decay risk**: low

### 12. 良率方法学 SPC / FDC / APC / DOE / WAT / PCM
- **Type**: acronym · **Tier**: tier-2
- **Definition (insider)**: SPC 区分常规波动 vs 异常; FDC 实时监设备状态、超差停机防 yield 损失; APC 用 run-to-run 前馈+反馈调配方; DOE 少量实验找工艺窗口/敏感度; WAT(=PCM)在 scribe line 测试结构上电学验收每片 wafer。 (evidence: [T06-S019, T06-S021])
- **常见误用 (outsider-tell)**: `usage_tell` 外行把 SPC/APC/FDC 当一回事; 内行: SPC 是监控统计, FDC 是设备故障检测, APC 是主动调配方(run-to-run), 层次不同。`semantic_tell` 把 WAT 当成品测试; 它是 fab 出货前 scribe line 电参监测不是封测。
- **Source**: [Secondary] yieldWerx (T06-S019), Orbit&Skyline APC (T06-S021)
- **可信度**: high · **Decay risk**: low

### 13. 量测族 CD-SEM / OCD(scatterometry) / overlay / ellipsometry / defect inspection
- **Type**: acronym/term · **Tier**: tier-2 (CD-SEM/OCD), tier-1 overlay 已列
- **Definition (insider)**: CD-SEM 量 top CD(精度高但慢、半破坏、缺 profile); OCD/scatterometry 光学建模反演(快、测 profile/trench, 非直接测); ellipsometry 椭偏测膜厚/折射率; defect inspection 缺陷检测(光学/e-beam)。 (evidence: [T06-S036])
- **常见误用 (outsider-tell)**: `usage_tell` 外行以为"量测=用尺子量"; 内行: OCD 是间接建模反演不是直接量, CD-SEM 与 OCD 各有盲区(top vs bottom CD)。
- **Source**: [Secondary] SemiEngineering metrology (T06-S036)
- **可信度**: high · **Decay risk**: low

### 14. 器件架构 FinFET / GAA-nanosheet / CFET + FEOL/MOL/BEOL + BSPDN
- **Type**: acronym/term · **Tier**: tier-1 (FinFET/GAA/FEOL-MOL-BEOL), tier-2 (CFET/BSPDN)
- **Definition (insider)**: FinFET 三面包栅(胡正明发明, 22nm 起); GAA nanosheet 环绕栅四面包沟道(N2 起接替); CFET N/P 器件垂直堆叠(GAA 之后 3D 路线); FEOL/MOL/BEOL = 前道器件/中道接触/后道互连; BSPDN 背面供电网络(供电挪背面释放正面布线)。 (evidence: [T06-S025, T06-S026, T06-S027, T06-S001])
- **常见误用 (outsider-tell)**:
  - `semantic_tell` (GAA): "GAA 是更小的 FinFET" — 是栅控架构换代(环绕栅 vs 三面栅)不是单纯缩小。 (evidence: [T06-S026])
  - `usage_tell` (FinFET): 误以为是封装技术; 它是 2011 量产至今的器件架构。
  - `usage_tell` (MOL): 外行只知"前道后道"; MOL 是先进节点新增的接触整合关键段。
- **是否被错位包装**: 否（器件架构定义在 IEDM/IRDS 稳定）。
- **变化历史**: FinFET 2011→GAA N2(~2025)→CFET(研发/路线图)。 (evidence: [T06-S028])
- **Source**: [Primary] imec CFET (T06-S027), IEDM 2023 CFET (T06-S028), IRDS MM (T06-S001), Synopsys GAA (T06-S026); [Secondary] SemiAnalysis transistor (T06-S025)
- **可信度**: high · **Decay risk**: FinFET/FEOL-MOL-BEOL low; GAA/CFET/BSPDN **high**

### 15. 先进封装 CoWoS / HBM / hybrid bonding / chiplet / TSV
- **Type**: term/acronym · **Tier**: tier-2
- **Definition (insider)**: CoWoS = TSMC 2.5D, chip-on-wafer-on-substrate 三层(逻辑 die + HBM stack 坐硅 interposer + TSV, 再坐基板); HBM = 堆叠 DRAM + TSV, 与逻辑共封缩短互连; hybrid bonding = 超细 pitch 铜-铜直接键合(无凸点); chiplet = 模块化小芯片互连; TSV = 硅通孔垂直互连。 (evidence: [T06-S022, T06-S023, T06-S024])
- **常见误用 (outsider-tell)**: `semantic_tell` 外行把 chiplet/先进封装当"造假绕过微缩"; 内行: 是**等效微缩**正统路线(性能靠封装/3D/异构集成继续 scale), 非作弊。 (evidence: [T06-S039])
- **是否被错位包装**: CoWoS 是 TSMC 自有产品名(verified by vendor), 通用概念叫 2.5D interposer; 提及时区分通用 vs TSMC 命名。 (evidence: [T06-S022])
- **变化历史**: CoWoS 随 AI/HBM 需求扩产; hybrid bonding 替代部分 3D 逻辑堆叠; HBM4 在研。 (evidence: [T06-S024])
- **Source**: [Secondary] SemiconductorX CoWoS (T06-S022), AnySilicon (T06-S023), Wevolver HBM (T06-S024)
- **可信度**: medium-high · **Decay risk**: high

### 16. 工艺整合 / 工艺窗口 / 良率爬坡 / 失效分析 FA / particle / 洁净室
- **Type**: term · **Tier**: tier-1 (工艺窗口/yield ramp/FA), tier-2 (particle/cleanroom)
- **Definition (insider)**: 工艺窗口 = 配方参数稳定产出合格结果的容差(靠 DOE 找); yield ramp = 新节点从低良率到量产良率的长期工程(数月到数年); FA = 对失效 die 逆向找根因反馈改工艺; particle = 颗粒污染(随尺寸缩小影响放大); cleanroom = ISO 14644 Class 1/3/5(光刻/刻蚀/沉积最严)。 (evidence: [T06-S029, T06-S037, T06-S019])
- **常见误用 (outsider-tell)**: `semantic_tell` 外行以为"调好配方就量产/良率不是问题"; 内行: yield ramp 是数月到数年的 know-how 壁垒, FA 不修单片而是找根因。`usage_tell` 以为洁净室"无尘"; 内行: 是 ppb 级控制且永不可能零颗粒, AMC(分子污染)与人/设备 shedding 是持续战。
- **是否被错位包装**: 否。
- **Source**: [Secondary] 14644 cleanroom (T06-S029), TSI particle (T06-S037), yieldWerx (T06-S019)
- **可信度**: high · **Decay risk**: low

### 17. BIS 出口管制 (EAR / Entity List / EUV-DUV SME 管制) — geographic-specific: US→CN
- **Type**: regulation · **Tier**: tier-1
- **Definition (insider)**: 美商务部 BIS 通过 EAR 管制对华先进半导体制造设备(SME, ECCN 3B001/3B002)、EUV(全禁)、先进 DUV(16nm 及以下能力)、先进计算 IC, 配 Entity List 实体清单点名。 (evidence: [T06-S003, T06-S031])
- **Definition (outsider-friendly)**: 美国限制把最先进的造芯片设备和工具卖给中国的法律体系。
- **常见误用 (outsider-tell)**: `semantic_tell` 外行以为"只禁 EUV"; 内行: 先进 DUV(193i 16nm 以下)、量测设备、零部件、entity list 软件/服务全覆盖, 是体系性封锁。`usage_tell` 以为"封了就完全造不了"或"很快完全国产替代"二元; 现实是设备/材料/EDA/良率/成熟度有真实差距, physics 不因政治改变。
- **是否被错位包装**: 否（gov 原文）。
- **变化历史**: 2022-10-07 首规 → 2023-10-17 SME 规则细化 → 2024-12 扩大 entity list/HBM/SME。 (evidence: [T06-S003, T06-S031])
- **geographic-specific**: US 立法管制 CN; 瓦森纳协定为多边框架基础; CN 侧大基金/国产化政策为对应回应(zh 视角)。
- **Source**: [Primary] Federal Register 2023 SME rule (T06-S003), Congress CRS (T06-S031)
- **可信度**: high · **Decay risk**: **high**（12 月内常修订, master skill 刷新触发源）

### 18. 摩尔定律 / 等效微缩 / dimensional vs equivalent scaling / PPAC / DTCO-STCO
- **Type**: term/acronym · **Tier**: tier-1 概念 (摩尔定律/等效微缩), tier-2 (PPAC/DTCO)
- **Definition (insider)**: dimensional scaling(几何缩小)放缓且成本墙/功耗墙逼近; equivalent scaling(等效微缩)用 DTCO(设计-工艺协同)/STCO(系统-工艺协同)/3D/封装继续提密度; PPAC = 性能-功耗-面积-成本四角权衡。 (evidence: [T06-S033, T06-S001])
- **disputed**: 「摩尔定律是否已死」内部有派别 — **微缩放缓派**(dimensional scaling 经济性走到头) vs **等效微缩继续派**(DTCO/3D/chiplet 让密度/性能继续 scale)。两派都承认 dimensional scaling 在放缓, 分歧在"是否算摩尔定律继续"。TSMC VP 原话: "不在乎死活, 只要技术继续 scaling"。 (evidence: [T06-S033, T06-S039, T06-S032])
- **常见误用 (outsider-tell)**: `semantic_tell` 外行用"摩尔定律已死/没死"做简单二元判断; 内行区分 dimensional(放缓)vs equivalent(继续)两个独立命题, 拒绝二元。
- **是否被错位包装**: 部分 — 厂商常把 equivalent scaling 包装成"摩尔定律永生"做营销, 业内分析(SemiAnalysis)做祛魅。 (evidence: [T06-S032])
- **Source**: [Primary] imec Moore's law dead (T06-S033), IRDS MM (T06-S001); [Secondary] SemiAnalysis (T06-S032), Tom's Hardware TSMC VP (T06-S039)
- **可信度**: high · **Decay risk**: low（争议本身稳定）

### 19. PDK / DFM / OPC / DTCO（设计-工艺交界）
- **Type**: acronym · **Tier**: tier-2
- **Definition (insider)**: PDK = foundry 提供的工艺模型文件/规则/器件库, 连接 EDA 与制造; DFM = 面向可制造性设计(sub-40nm 起关键); OPC = 光学邻近修正, 预畸变 mask 补偿衍射; DTCO = 设计与工艺协同优化抓密度/功耗/成本。 (evidence: [T06-S034, T06-S035])
- **常见误用 (outsider-tell)**: `usage_tell` 外行把 PDK 当"设计软件"; 内行: PDK 是 foundry 的工艺契约文件集, 是设计-制造的接口, 换 foundry 就换 PDK。
- **是否被错位包装**: 否。
- **Source**: [Secondary] PDK Wikipedia (T06-S034), SemiEngineering PDK 指南 (T06-S035)
- **可信度**: high · **Decay risk**: low

### 20. 洁净室级别 / ISO 14644 / SEMI standards
- **Type**: standard · **Tier**: tier-2
- **Definition (insider)**: ISO 14644-1 定 Class 1(最净)-9, 按每 m³ 颗粒数; fab 光刻/刻蚀/沉积区常 Class 1/3/5; SEMI E/F 系列补充 AMC(分子污染)等设备/材料标准。 (evidence: [T06-S029])
- **常见误用 (outsider-tell)**: `usage_tell` 外行以为"无尘室=完全无尘"; 内行: 是分级 ppb 颗粒控制, 永不可能零颗粒, ISO 级别+AMC 控制+人/设备纪律共同决定。
- **变化历史**: ISO 14644-1 现行 2015 版; SEMI standards 持续小更。
- **Source**: [Secondary] 14644 cleanroom (T06-S029)
- **可信度**: high · **Decay risk**: low

---

## Phase 2 提炼提示

**「行业表达 DNA」直接素材**（喂给 Phase 2.5 expression-DNA 提炼）:

- **高频黑话 top 10**: 流片 tape-out / 良率 yield + D0 缺陷密度 / 工艺窗口 process window / overlay 套刻 / yield ramp 良率爬坡 / 选择比 selectivity / step coverage 台阶覆盖 / 多重曝光 multi-patterning / DOE 找窗口 / FEOL-MOL-BEOL 整合段。（内行张口就是 CPP/MMP/D0/ramp/window, 用缩写+量化, 拒绝节点营销名当物理值）
- **行业拒绝的厂商话术 top 5**:
  1. "N3=物理 3nm" 节点营销名当物理尺度（拒绝 → 价值观: 真尺度看 MTr/mm²·CPP·MMP, 诚实于物理）(evidence: [T06-S005,S007,S009])
  2. "买到 EUV/光刻机就能做先进制程"（拒绝 → 反模式: 设备决定论, 内行知整合/良率/材料缺一不可）(evidence: [T06-S033])
  3. "摩尔定律永生"式 equivalent scaling 营销（拒绝 → 区分 dimensional 放缓 vs equivalent 继续, 拒二元/拒永生话术）(evidence: [T06-S032])
  4. "国产已突破/已量产先进制程" 软文（拒绝 → 诚实于设备/材料/EDA/良率/成熟度差距）(evidence: [T06-S003,S031])
  5. "良率不是问题/很快追平"（拒绝 → ramp 是数月到数年 know-how 壁垒, D0 是硬约束）(evidence: [T06-S019])
- **外行破绽 top 10** (见上"外行破绽高亮"表): 节点名当物理尺寸 / EUV 万能论 / 光刻机决定论 / 摩尔定律二元 / ALE-ALD 混淆 / 良率乐观 / chiplet=作弊 / GAA=小 FinFET / 纳米数字越小越先进 / 国产已突破。

**「智识谱系」线索**（喂给 Phase 2.7 智识谱系）:
- 器件架构演进 planar → FinFET(胡正明 2011) → GAA nanosheet(N2) → CFET(3D 堆叠) 反映"靠静电控制对抗短沟道效应"的范式延续, 每代换栅控架构而非单纯缩小。(evidence: [T06-S025,S027,S028])
- scaling 哲学分裂: dimensional scaling(几何, Dennard/Moore 谱系) vs equivalent scaling(DTCO/STCO/3D/封装, imec/TSMC 谱系) — 是流派之争的硬件层。(evidence: [T06-S001,S033])
- 前道微缩 vs 先进封装异构集成(chiplet/CoWoS/hybrid bonding) 两条等效微缩路线竞争 = 范式更替信号。(evidence: [T06-S039,S022])

**「时效性」信号**（喂给 Phase 2.8 诚实边界）:
- 高 decay 簇: BIS 出口管制(12 月内常修订, 2022→2023→2024 三次扩大)、high-NA EUV 量产爬坡(2024 首台→2025-26)、GAA/CFET/BSPDN 器件导入、先进封装(HBM4/CoWoS 产能/hybrid bonding)。
- 预计 12 月内会变: BIS entity list/SME 管制细则、high-NA EUV ramp 进度、N2/A16 量产时点、HBM4 导入。
- 低 decay(OS 核心): 单元工艺物理化学原理、良率方法学(SPC/FDC/APC/DOE/D0)、器件微缩基本原理、节点命名脱钩共识。

**「工作流变化触发」种子**（喂给 wave 3 Track 03）:
- BIS 管制修订(2022/2023/2024) → 直接改变设备采购/材料供应链/EDA 可用性 workflow 假设(国产替代 fab 的工具栈选择)。(evidence: [T06-S003,S031])
- high-NA EUV 导入 → 改变光刻分解/多重曝光策略 workflow(单次曝光可减 multi-patterning 步)。(evidence: [T06-S004])
- GAA/CFET/BSPDN 器件换代 → 改变工艺整合(FEOL/MOL/BEOL)、量测(背面/3D 结构)、PDK/DTCO workflow。(evidence: [T06-S001,S002])

**冷僻 / 信号薄弱自检**:
- 总候选 52(Tier1 22 + Tier2 30) ≥ 40 floor ✅; Tier1 22 ≥ 15 ✅; Tier1+Tier2 = 52 ≥ 40 ✅。
- Tier1 全部填 outsider-tell ✅; Tier2 关键条(≥50%)填 outsider-tell ✅。
- 有 outsider-tell 的术语 > 50% ✅。**非冷僻行业**, 信号充足。
- type 分布: term/acronym 极丰富, standard 中等(ISO 14644/SEMI/IRDS), regulation 重(BIS/EAR/瓦森纳), **certification = N/A**(本行业无个人执业认证, 资质=fab qualification + 客户 audit)。
- disputed 正确标注: 「摩尔定律已死」按两派(微缩放缓 vs 等效微缩继续)并列不强行统一 ✅。
- locale 失衡诚实标注: 技术 canon/标准/管制几乎全 en(IRDS/SEMI/JEDEC/BIS/ASML/IEDM), zh-CN 主要是产业/政策视角(国产替代/大基金), Track 06 偏 en-primary, 已在 manifest 体现。
