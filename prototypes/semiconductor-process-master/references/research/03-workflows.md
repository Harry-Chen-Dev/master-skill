# Track 03 — Workflows / 工作流·SOP · Semiconductor Process Engineering (global)

> Phase 1 Wave 3 输出。行业 = 半导体芯片制造工艺。locale = global · profile = practitioner。
> 本 track 从 Wave 1+2 seed（01-figures / 02-tools / 04-canon / 06-glossary）抽取 workflow 片段，拼成「入门 SOP + 资深路径 + 近期变化 + 时效锚点」。
> **本行业 workflow 特点**：多数核心工艺流程（单元工艺配方开发、良率爬坡方法学、SPC/DOE 闭环、FA 根因）是 **5-10 年稳态的方法学**（low decay），少数受 EUV/GAA/high-NA/先进封装/计算光刻ML 驱动的流程是 high decay。
> 收集日期 last_checked: 2026-06-21（除特注）。
> **一手说明**：本行业 workflow 一手 = 工程师/代工厂/设备厂技术白皮书 + 顶会 short course + 教材方法学（canon）+ 发明人本人 talk。市场分析与媒体长稿留 secondary。

## Source Manifest

| source_id | url | bucket | last_checked | author/host | one-line note |
|-----------|-----|--------|--------------|-------------|---------------|
| T03-S001 | https://semiengineering.com/systematic-yield-issues-now-top-priority-at-advanced-nodes/ | secondary | 2026-06-21 | Semiconductor Engineering | 先进节点系统性良率问题成首要；Pareto/commonality/逐层定位方法 |
| T03-S002 | https://blogs.sw.siemens.com/tessent/2023/04/21/a-new-way-to-solve-systematic-failures-and-boost-yield/ | surrogate_primary | 2026-06-21 | Siemens EDA Tessent | vendor docs：volume scan diagnosis + pattern family 做系统性失效根因（own publication） |
| T03-S003 | https://www.semiconductors.org/wp-content/uploads/2018/09/Yield.pdf | surrogate_primary | 2026-06-21 | SIA / ITRS Yield Enhancement | 协会/路线图 SOP：yield enhancement 章（defect budget / inspection strategy） |
| T03-S004 | https://iedm23.mapyourshow.com/mys_shared/iedm23/handouts/SC1.5_IEDM_2023_DTCO_STCO_YK.pdf | surrogate_primary | 2026-06-21 | IEDM 2023 / YK Chong (Arm) | 顶会 short course（own publication）：DTCO 三阶段 Technology→Design Enablement(PDK)→Design |
| T03-S005 | https://spectrum.ieee.org/future-fab | secondary | 2026-06-21 | IEEE Spectrum | fab 工艺开发与 ramp 的 TD→HVM 叙事 |
| T03-S006 | https://www.electronicsweekly.com/news/business/p-pdks-to-restore-academias-role-in-process-development-2025-11/ | secondary | 2026-06-21 | Electronics Weekly | 2025-11 P-PDK：学界工艺开发与 PDK 角色（近期变化锚） |
| T03-S007 | https://www.orcalean.com/article/inside-intel's-lean-manufacturing:-how-the-semiconductor-giant-stays-ahead-of-the-competition | secondary | 2026-06-21 | OrcaLean | Intel Copy Exactly! + virtual factory + BKM 复制方法学 |
| T03-S008 | https://wiki.nanofab.ucsb.edu/wiki/ICP_Etching_Recipes | verified_primary | 2026-06-21 | UCSB Nanofab (.edu) | 学界 nanofab ICP 刻蚀 recipe wiki（.edu 一手 SOP，选择比/profile 调参） |
| T03-S009 | https://semiengineering.com/hybrid-bonding-makes-strides-toward-manufacturability/ | secondary | 2026-06-21 | Semiconductor Engineering | 混合键合迈向可制造性：RMS<0.2nm/dishing/activation/anneal 工艺要点 |
| T03-S010 | https://www.imec-int.com/en/articles/wafer-wafer-hybrid-bonding-pushing-boundaries-400nm-interconnect-pitch | verified_primary | 2026-06-21 | imec | imec wafer-to-wafer 混合键合 400nm pitch（研究机构一手） |
| T03-S011 | https://semiengineering.com/single-vs-multi-patterning-advancements-for-euv/ | secondary | 2026-06-21 | Semiconductor Engineering | EUV 单曝 vs 多重曝光；high-NA 单曝替代 SADP/SAQP 的临界点 |

> **跨 track 复用 source（同 ID，引自 Wave1/2 manifest）**：
> T04-S034/S016/S003 (May & Spanos《Fundamentals of Semiconductor Manufacturing & Process Control》— SPC/yield/DOE/APC canon) · T04-S019 / T06 (IEDM DTCO/STCO) · T04-S018 (TSMC "What is DTCO?" vendor blog) · T04-S007/T06-S001 (IRDS More Moore) · T04-S001 (Plummer《Silicon VLSI Technology》工艺整合/TCAD) · T02-S006 (Sentaurus TCAD) · T02-S017/S037 (Synopsys YieldManager/Odyssey YMS) · T02-S019 (KLA defect inspection) · T02-S027/S028 (Lam ALE/ALD) · T02-S010/S035/S036 (Calibre/cuLitho 计算光刻) · T02-S024/S025 (混合键合工艺流) · T01-S001 (胡正明 oral history) · T01-S017 (Dylan Patel/Jon Y：良率/效率差距、tacit apprentice 知识) · T01-S029 (魏哲家 N2 ramp "good yield").

> **一手率（本 track manifest 计）**：verified_primary(含 surrogate_primary vendor/协会/顶会/own-publication) = S002+S003+S004+S008 = 4，加跨 track 复用的 canon/IEDM/vendor 一手（May&Spanos / IRDS / Plummer / TSMC DTCO / Sentaurus / IEDM DTCO / 胡正明 oral history 等 ≥8 个 verified_primary）→ workflow claim 的一手覆盖 **≥55%**。市场/媒体（S001/S005/S006/S007）诚实留 secondary。

---

## 总览（按 decay risk 分组）

### Low decay（稳态方法学，5-10 年无重大变化）— 4 个

| Workflow | Trigger | Output | Last_updated | 资深差异 |
|---------|---------|--------|-------------|---------|
| 2. 单元工艺配方开发（DOE 找工艺窗口）| 新结构/新材料/新设备需要可量产 recipe | 锁定的量产配方 + 工艺窗口 + SPC limits | 2026-06-21 | skip 全因子→筛选 DOE；add 边缘晶圆/loading split；optimize RSM/中心点 |
| 3. 良率爬坡（缺陷分类→commonality→根因→改善→SPC固化）| 新节点/新产品良率低于量产目标 | 良率达量产目标 + 缺陷 Pareto 关闭 + SPC 固化 | 2026-06-21 | skip 全检→采样+inline；add WAT/PCM 电性 commonality；optimize ML/spatial signature |
| 4. 失效分析 FA / 缺陷根因闭环（电性定位→物理 deprocess→FA→改工艺）| 出现 yield bin / 客户退货 / 可靠性 fail | 根因报告 + 工艺/设计 corrective action | 2026-06-21 | skip 直接 FIB→先 scan diagnosis 缩范围；add 非破坏先行；optimize fault isolation 工具链 |
| 6. 工艺移植 / Copy-Exactly（TD→HVM、fab→fab 量产移交）| 工艺从研发线转量产线 / 扩到新 fab | 新 fab 良率/参数匹配源 fab + 量产 ramp | 2026-06-21 | skip 重新优化→严格 copy；add 设备指纹比对；optimize BKM 反向回流 |

### Medium decay（受 GAA/CFET/先进封装/ML 持续推动）— 2 个

| Workflow | Trigger | Output | Last_updated | 资深差异 |
|---------|---------|--------|-------------|---------|
| 1. 新节点/新工艺导入（PPAC→整合PDK→单元工艺DOE→量测SPC→良率爬坡→量产）| 新技术节点立项 / 客户新产品要求 | 可量产工艺平台 + PDK + 量产移交 | 2026-06-21 | skip pathfinding 走捷径；add DTCO/TCAD 先行；optimize 并行 ramp |
| 5. DTCO 设计-工艺协同优化（pathfinding→规则→PDK→co-opt 迭代）| 单纯 dimensional scaling 收益不足，需协同提 PPAC | 协同后的设计规则 + 标准单元 + PDK | 2026-06-21 | skip 纯 dimensional；add 系统级 STCO；optimize 自动 pathfinding |

### High decay（12-月级，受 EUV/high-NA/计算光刻ML 驱动）— 1 个

| Workflow | Trigger | Output | Last_updated | 资深差异 |
|---------|---------|--------|-------------|---------|
| 7. 光刻层 patterning 方案开发（曝光条件→OPC/计算光刻→overlay→多重曝光分解）| 关键层需要在给定光刻能力下成像合格 | patterning 方案（mask + OPC + 分解 + overlay 预算）| 2026-06-21 | skip 多重曝光（EUV 单曝代替）；add 随机缺陷预算；optimize GPU ILT 曲线 mask |

---

## 详细数据结构

### 1. 新节点 / 新工艺导入（PPAC 定义 → 工艺整合+PDK → 单元工艺 DOE → 量测 SPC → 良率爬坡 → 量产移交）

- **One-liner**: 从「一个新技术节点立项（如 N2、A16）或客户新产品工艺要求」到「一个可量产、有 PDK、良率达标、已移交量产的工艺平台」。这是 fab 工艺工程的总流程，套住其余所有子 workflow。 (evidence: [T03-S004, T03-S005])
- **Trigger**: 公司路线图启动新节点 / 大客户要求新工艺平台 / 现有节点需要 derivative（如 N2P、背面供电变体）。
- **Output**: 可量产工艺平台（一整套锁定的单元工艺 + 整合流程）+ 给客户的 PDK（器件模型/标准单元库/DRC/RC 模型）+ 量产移交（copy-exactly 到 HVM fab）。
- **入门 SOP（minimum viable steps）**:
  1. **器件目标与 PPAC 定义**：定义节点的 Power/Performance/Area/Cost 目标与器件架构（FinFET→GAA nanosheet→CFET），用 IRDS 路线图与 TCAD 先评估可行性。 (evidence: [T03-S004, T04-S007])
  2. **工艺整合方案 + 早期 PDK**：把目标拆成 FEOL/MOL/BEOL 模块，定整合流程与模块间 trade-off，用 SEMulator3D/TCAD 先在电脑里验证整合，产出早期设计规则与 PDK。 (evidence: [T03-S004, T02-S006, T02-S008])
  3. **单元工艺开发（DOE 找窗口）**：对每个关键单元工艺（光刻/刻蚀/沉积/CMP/注入）跑 DOE 开发配方（= workflow 2）。 (evidence: [T04-S034])
  4. **量测建立 + SPC**：为每个工艺建量测方法（CD-SEM/OCD/overlay）与 SPC 控制限。 (evidence: [T02-S019])
  5. **良率爬坡**：流片测试结构与产品，做缺陷分类→commonality→根因→改善（= workflow 3）。 (evidence: [T03-S001])
  6. **量产移交（copy-exactly）**：把锁定工艺与 PDK 移交 HVM fab，严格复制（= workflow 6），客户拿 PDK 设计流片。 (evidence: [T03-S007])
  - **每一步如果跳过会发生什么**:
    - 跳 step1（PPAC/TCAD 先行）→ 选了物理上做不出或经济上不划算的目标，烧掉数亿研发费才发现。
    - 跳 step2（整合+早 PDK）→ 单元工艺各自最优但整合不起来（模块间 trade-off 冲突），且 PDK 太晚导致客户设计与工艺脱节。
    - 跳 step4（量测+SPC）→ 工艺无监控基线，良率爬坡时无法判定漂移源。
    - 跳 step6（copy-exactly）→ HVM fab 与研发线参数不匹配，量产良率塌方。
- **资深路径（差异点）**：
  - **skip**：资深团队**跳过部分 pathfinding 穷举**，用上代节点经验 + DTCO 先收敛架构选项，不把所有候选都做实验。 (evidence: [T03-S004])
  - **add**：资深团队**额外把 DTCO + TCAD 仿真前置到立项早期**，初学者先做工艺再回填设计规则，资深人知道设计-工艺必须协同（DTCO），否则返工。 (evidence: [T03-S004, T04-S018])
  - **optimize**：资深团队**并行而非串行 ramp** —— 量测/SPC 与单元工艺开发并行，良率爬坡与 PDK 成熟并行，压缩节点导入周期。 (evidence: [T03-S005])
- **近期变化**（近 12 个月）：
  - **medium decay**：架构层在变 —— FinFET→**GAA nanosheet（2025 Q4 TSMC N2 量产）**→CFET（>1nm 路线），**背面供电 BSPDN（A16）** 改变 BEOL 整合流程。 (evidence: [T01-S029, T04-S007])
  - 2025-11 **P-PDK（学界可访问 PDK）** 让工艺开发方法学外溢到学界。触发事件类型：新器件架构（GAA/CFET/BSPDN）+ 标准更新（IRDS）。 (evidence: [T03-S006])
- **典型耗时**: 入门/全流程一个新节点导入 = **数年**（路线图级）；资深团队用 DTCO 前置 + 并行 ramp 仍需 2-3 年但风险更可控。
- **关键工具（与 Track 02 关联）**：TCAD Sentaurus + SEMulator3D（整合验证）+ Calibre/Proteus（计算光刻）+ KLA（量测缺陷）+ YMS（良率）+ 全套设备。 (evidence: [T02-S006, T02-S008, T02-S010, T02-S017, T02-S019])
- **关键人物（与 Track 01 关联）**：胡正明（器件架构 FinFET→GAA 奠基）；魏哲家（N2 GAA 量产官方）；Mark Bohr（工艺架构整合 + 节点真密度）。 (evidence: [T01-S001, T01-S029, T01-S020])
- **常见失败模式**:
  - **单元工艺各自最优、整合却失败**：每个 unit process 调到最好但模块间 trade-off 冲突（如热预算 vs 掺杂剖面），整合不起来 —— 必须 step2 用 SEMulator3D/TCAD 先验整合，DTCO 协同。
  - **PDK 给得太晚**：客户拿不到稳定 PDK 无法设计，节点空转 —— PDK 与工艺开发并行（DTCO design enablement 阶段）。
  - **「买齐设备就能导入节点」**：EUV/设备只是必要非充分，材料+整合+良率 know-how 缺一不可，国产替代叙事尤其须诚实拆穿 —— 五要素（设备+材料+工艺+整合+良率）齐备才算能导入。 (evidence: [T01-S017])
  - **研发线良率好、HVM 塌方**：没严格 copy-exactly，HVM 设备指纹与研发线不同 —— step6 严格复制 + 设备指纹比对。
- **来源** (≥3): [Surrogate-Primary] T03-S004 IEDM 2023 DTCO/STCO short course（顶会 own publication）/ [Primary] T04-S007 IRDS More Moore（标准机构）/ [Primary] T04-S018 TSMC DTCO blog（vendor doc）/ [Secondary] T03-S005 IEEE Spectrum / [Secondary] T03-S006 Electronics Weekly。
- **Last_updated**: 2026-06-21
- **Decay risk**: **medium**（总流程骨架稳，但器件架构层 GAA/CFET/BSPDN 在 12-24 月持续演进）

---

### 2. 单元工艺配方开发（DOE 找工艺窗口）— 以刻蚀/沉积/CMP 为代表

- **One-liner**: 从「一个新结构/新材料/新设备没有可用配方」到「锁定一个有足够工艺窗口、可量产、可被 SPC 监控的 recipe」。这是工艺工程师最高频的日常 workflow，刻蚀/沉积/CMP/光刻通用。 (evidence: [T03-S008, T04-S034])
- **Trigger**: 新器件结构（如 GAA nanosheet）/ 新材料（如 Mo 互连、high-k）/ 新设备上线 / 现有 recipe 工艺窗口太窄导致良率波动，需要开发或重调一个单元工艺配方。
- **Output**: 一份锁定的量产配方（气体配比/功率/压力/温度/时间等参数）+ 量化的工艺窗口（参数容差范围）+ 对应的 SPC 控制限与量测点。
- **入门 SOP（minimum viable steps）**:
  1. **定义目标与量测指标**：明确 CD / profile（侧壁角）/ 选择比 selectivity / 去除速率 / 均匀性 / 缺陷 等可量测验收标准，并先建立对应量测方法（CD-SEM/OCD/椭偏）。
  2. **识别关键参数与基线**：列出该工艺的主导参数（刻蚀：气体配比/RF 功率/压力/温度；沉积：前驱体/温度/循环数；CMP：下压力/转速/浆料），从供应商/文献/类似工艺取基线配方。 (evidence: [T03-S008])
  3. **设计 DOE 找工艺窗口**：用筛选 DOE（如两水平正交矩阵）扫主因子，再用响应面 RSM / 中心点定窗口；不要 OFAT（一次一因子）漏掉交互作用。 (evidence: [T04-S034])
  4. **跑实验并量测**：在 split wafer 上跑 DOE 矩阵，量测各 response，建立参数→response 的响应面。
  5. **选工作点并验证窗口宽度**：选位于窗口中心、对参数漂移最不敏感的工作点；工艺窗口宽 = 可制造性好。 (evidence: [T03-S008])
  6. **设 SPC 限并移交**：把工作点参数与量测点写成 SPC 控制图、APC run-to-run 规则，移交量产并持续监控。 (evidence: [T04-S034])
  - **每一步如果跳过会发生什么**:
    - 跳 step1（量测先行）→ 无可量化验收标准，DOE 结果无法判优劣，等于盲调。
    - 跳 step3（DOE）→ 用 OFAT 调参会漏掉参数交互（如刻蚀气体×功率），找到的「窗口」可能是局部假窗口，量产后随设备漂移崩塌。
    - 跳 step5（窗口宽度验证）→ 选了一个良率高但工艺窗口极窄的点，量产中设备微漂即超规，良率周期性掉。
    - 跳 step6（SPC 固化）→ 配方无监控，漂移无人察觉，excursion 批量报废才发现。
- **资深路径（差异点）**：
  - **skip**：资深人**跳过全因子 DOE**，直接用经验把 5-7 个候选因子砍到 2-3 个主因子做筛选 DOE —— 经验告诉他们哪些参数对该 response 不敏感（如某些刻蚀里温度对 profile 影响远小于 polymer 化学）。 (evidence: [T03-S008])
  - **add**：资深人**额外加 loading-effect split 与边缘晶圆/晶圆内均匀性 split** —— 初学者只在图形密度均匀的测试片上调，资深人知道 loading effect（开口面积影响 ER/选择比）和 wafer edge 是量产翻车高发区，必须在 DOE 里就覆盖。 (evidence: [T03-S008])
  - **optimize**：资深人用**响应面 RSM + 中心点重复**估曲率与噪声，而非只跑两水平角点，能更准定出窗口中心而不是边缘。 (evidence: [T04-S034])
- **近期变化**（近 12 个月）：
  - 多数为**稳态**：DOE/工艺窗口/SPC 方法学 5-10 年无重大变化（行业稳态，最近一次方法学级显著变化是统计 DOE/RSM 的标准化与 May&Spanos 教材体系化）。 (evidence: [T04-S034])
  - 增量信号：2024-2025 起 **ML/贝叶斯优化 + few-shot recipe generation** 开始辅助缩短 DOE 迭代（仍属辅助、未取代 DOE 范式）。触发事件类型：新工具（ML 配方优化）。 (evidence: [T03-S008])
- **典型耗时**: 入门 SOP 数周-数月（含设备时间 + 量测周期）；资深路径砍因子后可压到 1-数周。
- **关键工具（与 Track 02 关联）**：DOE/统计软件 + CD-SEM/OCD 量测（KLA）+ TCAD 预仿（Sentaurus，可减实验次数）+ 刻蚀/沉积/CMP 设备（Lam/AMAT/TEL）。 (evidence: [T02-S006, T02-S019, T02-S027])
- **关键人物（与 Track 01 关联）**：Jon Y (Asianometry) 反复强调单元工艺第一性与 tacit/apprentice 知识（配方调试 know-how 藏在公司内）。 (evidence: [T01-S017])
- **常见失败模式**:
  - **OFAT 调参漏交互**：只一次调一个参数找到的窗口是假窗口，量产随设备漂移崩 —— 必须用筛选 DOE 至少覆盖主因子的两两交互。
  - **只在均匀测试片调、不做 loading/edge split**：量产真实图形密度不均，开口大处选择比掉、边缘 CD 漂，良率周期性掉 —— DOE 阶段就加 loading 与 edge split。
  - **选窗口中心遗漏 = 选了高良率但窄窗口点**：上量产后设备微漂即超规 —— 用 RSM 选对参数漂移最不敏感的工作点。
- **来源** (≥3): [Primary] T03-S008 UCSB nanofab ICP recipe wiki（.edu 一手选择比/profile 调参）/ [Primary] T04-S034 May & Spanos（DOE/工艺窗口/SPC canon）/ [Reference] T01-S017 Jon Y（单元工艺 tacit 知识）。
- **Last_updated**: 2026-06-21
- **Decay risk**: **low**（DOE/工艺窗口/SPC 方法学稳态；ML 辅助为增量非颠覆）

---

### 3. 良率爬坡 Yield Ramp（缺陷采集→分类→commonality→根因→改善→SPC固化）

- **One-liner**: 从「新节点/新产品良率远低于量产目标」到「良率爬到量产目标、缺陷 Pareto 主项关闭、SPC 固化」。这是 fab 最核心也最 know-how 密集的 workflow，决定一个节点能否赚钱。 (evidence: [T03-S001, T04-S034])
- **Trigger**: 新节点导入 / 新产品流片回来 / 量产中良率突然跌（excursion），实际良率 < 目标良率，需要系统性找出并消除良率限制因子。
- **Output**: 良率达到量产目标曲线 + 缺陷 Pareto 前几项根因关闭 + 对应工艺改善固化进 SPC/APC，并形成 BKM。
- **入门 SOP（minimum viable steps）**:
  1. **缺陷与良率数据采集**：inline defect inspection（KLA 光学/e-beam）逐层扫 + 终测 bin map + WAT/PCM 电性参数，建立良率与缺陷数据库。 (evidence: [T02-S019, T03-S003])
  2. **缺陷分类与 Pareto**：把 fail 按 bin / 缺陷类型排 Pareto（通常前三 bin 占 >70% 良率损失），先打最大的。 (evidence: [T03-S001])
  3. **Commonality / 逐层定位**：用 commonality analysis（哪台设备/哪一层/哪个时间段的 lot 共性 fail）+ 逐层 inline 数据，把良率损失定位到具体工艺步骤/设备。 (evidence: [T03-S001, T03-S002])
  4. **根因分析（FA）**：对定位到的缺陷做物理 FA（SEM/TEM/FIB）或 volume scan diagnosis 找系统性 vs 随机根因。 (evidence: [T03-S002])
  5. **工艺改善验证**：针对根因改配方/设备/设计，用 split lot 验证良率提升与无副作用。
  6. **SPC 固化 + BKM**：把改善固化进 SPC 限/APC 规则，写成 BKM 防复发并复制到同类产线。 (evidence: [T03-S007, T04-S034])
  - **每一步如果跳过会发生什么**:
    - 跳 step1（电性 WAT/PCM）→ 只看物理缺陷会漏掉「无可见缺陷的参数型良率损失」（如阈值漂移、漏电），根因找错方向。
    - 跳 step2（Pareto）→ 不排优先级会把精力耗在小 bin 上，良率爬坡周期拖长数月。
    - 跳 step3（commonality）→ 不做设备/层共性会陷入「逐片救火」，找不到系统性根因。
    - 跳 step4（FA 根因）→ 只改表象不找根因，问题换个形式复发。
    - 跳 step6（SPC 固化）→ 改善不固化，量产中同问题反复 excursion。
- **资深路径（差异点）**：
  - **skip**：资深人**跳过全晶圆全检**，改用采样 + 关键层重点 inline + spatial signature 直接锁定嫌疑层 —— 经验让他们看 wafer map 的空间签名（edge/center/scratch/cluster）就能猜到工艺源，不必全检。 (evidence: [T03-S001])
  - **add**：资深人**额外把 WAT/PCM 电性数据与 inline 缺陷做 commonality 交叉** —— 初学者只看物理缺陷，资深人知道很多良率损失是「电性 fail 但无可见缺陷」的系统性问题，必须电性+物理双轨 commonality。 (evidence: [T03-S001, T03-S002])
  - **optimize**：资深人用 **ML/spatial pattern recognition + volume scan diagnosis（pattern family）** 自动化缺陷 Pareto 与系统性失效定位，比纯人工逐层快数倍。 (evidence: [T03-S001, T03-S002])
- **近期变化**（近 12 个月）：
  - 2023 起 **systematic（系统性）良率问题在先进节点超过 random 缺陷成首要**，根因从「找 particle」转向「找 design-process 交互的系统性 pattern」。 (evidence: [T03-S001])
  - 2023-2025 **ML-based defect Pareto + pattern family + volume scan diagnosis** 成为先进节点良率分析标配（Siemens Tessent / yieldWerx 等）。触发事件类型：新工具（ML 良率分析）+ 行业事件（节点微缩使 systematic 主导）。 (evidence: [T03-S001, T03-S002])
- **典型耗时**: 入门 SOP / 新节点良率爬坡数月到数年（intake 红线：ramp 是数月-数年 know-how 壁垒）；资深路径用 ML+commonality 可显著缩短单个 excursion 闭环（天-周级）。
- **关键工具（与 Track 02 关联）**：缺陷检测 KLA（inline + e-beam）+ YMS（Synopsys YieldManager/Odyssey、PDF Exensio、KLA Klarity）做 fab+test 关联 + FDC/APC（AMAT E3）。 (evidence: [T02-S017, T02-S019, T02-S037])
- **关键人物（与 Track 01 关联）**：梁孟松「14nm FinFET 良率 298 天爬到 95%」是良率爬坡 know-how 的标志案例；魏哲家 N2 "good yield" 官方披露；Dylan Patel 强调良率/效率差距是真正壁垒。 (evidence: [T01-S017, T01-S028, T01-S029])
- **常见失败模式**:
  - **只看物理缺陷、不看电性 WAT/PCM**：漏掉无可见缺陷的参数型良率损失（阈值漂移/漏电），根因找错，浪费数周追错缺陷 —— 电性 + 物理双轨 commonality。
  - **不排 Pareto 就逐片救火**：精力分散在小 bin，良率爬坡拖几个月 —— 先 Pareto，前三 bin 占 >70% 损失，集中打最大的。
  - **改善不做 split 验证就上线**：以为改对了，结果引入新副作用或根因没关闭，良率再次跌 —— 必须 split lot 验证提升且无副作用再固化。
  - **改善不固化进 SPC/BKM**：同一 excursion 在不同 lot/不同 fab 反复发生 —— 固化进 SPC 限 + APC + BKM 复制。
- **来源** (≥3): [Primary] T04-S034 May & Spanos（yield model/SPC canon）/ [Surrogate-Primary] T03-S002 Siemens Tessent（volume scan diagnosis own publication）/ [Surrogate-Primary] T03-S003 SIA/ITRS Yield Enhancement（协会 SOP）/ [Secondary] T03-S001 Semiconductor Engineering（systematic yield）。
- **Last_updated**: 2026-06-21
- **Decay risk**: **low**（爬坡方法学骨架稳态：采集→Pareto→commonality→FA→改善→固化；ML 工具层为增量优化，骨架不变）

---

### 4. 失效分析 FA / 缺陷根因闭环（电性定位→物理 deprocess→FA→反馈改工艺）

- **One-liner**: 从「一个 die fail（yield bin / 客户退货 / 可靠性 fail）」到「找到物理根因并反馈改工艺/设计的 corrective action」。FA 不修单片，而是逆向找根因闭环改善。 (evidence: [T06-glossary FA, T03-S002])
- **Trigger**: 出现无法用 inline 数据直接解释的 yield bin / 客户 RMA 退货 / 可靠性测试（IRPS 类）fail，需要逆向定位物理根因。
- **Output**: 根因报告（物理/电学/材料层面）+ 明确的工艺或设计 corrective action + 验证关闭。
- **入门 SOP（minimum viable steps）**:
  1. **失效复现与电性定位**：先用电性测试（ATE/参数测试）确认 fail 模式，用 fault isolation（scan diagnosis / 光发射 EMMI / OBIRCH 热点）把 fail 缩到具体 net/区域。 (evidence: [T03-S002])
  2. **非破坏分析先行**：X-ray / 声学扫描 SAM / 红外，避免一上来就破坏样品丢信息。
  3. **物理 deprocess + FA**：逐层去层（deprocess）后用 SEM/TEM/FIB 看缺陷物理形貌，做材料分析（EDX/SIMS）。
  4. **根因判定**：判定是工艺缺陷（particle/桥接/空洞）、设计弱点（marginal layout）还是材料/可靠性问题。
  5. **反馈 corrective action + 验证**：把根因反馈到对应工艺步骤/设计规则/设备，split 验证后关闭。 (evidence: [T03-S007])
  - **每一步如果跳过会发生什么**:
    - 跳 step1（电性定位）→ 在整个 die 上盲目 FIB 切，命中率极低，烧掉昂贵样品和数周。
    - 跳 step2（非破坏先行）→ 一上来破坏 deprocess，丢失原始失效证据（如可移动离子、空洞充填物）。
    - 跳 step4（根因判定）→ 把表象当根因（看到 particle 就说是 particle），改了仍复发。
    - 跳 step5（反馈验证）→ FA 报告不闭环到工艺改善，等于白做。
- **资深路径（差异点）**：
  - **skip**：资深人在有 volume scan diagnosis 数据时**跳过逐点 EMMI/OBIRCH 物理 isolation**，直接用 diagnosis 缩小到候选 net 再 FIB —— 大幅减少物理定位时间。 (evidence: [T03-S002])
  - **add**：资深人**额外坚持非破坏分析 + 多样品统计**，初学者拿到一个 fail die 就切，资深人知道单样品可能是 outlier，要先非破坏 + 多样品确认失效是否 systematic。
  - **optimize**：资深人用 **fault isolation 工具链组合（scan diagnosis + EMMI + nanoprobing）** 而非单一手段，按 fail 类型选最快路径。 (evidence: [T03-S002])
- **近期变化**（近 12 个月）：
  - **稳态为主**：FA 物理方法（deprocess/SEM/TEM/FIB）5-10 年稳态。增量：**volume scan diagnosis + ML pattern family** 让「电性定位→物理 FA」之间的环节越来越数据驱动，减少盲切（2023-2025）。触发事件类型：新工具（scan diagnosis/ML）。 (evidence: [T03-S002])
- **典型耗时**: 入门 SOP 单 case 数天-数周（含 deprocess + FA 设备排队）；资深用 scan diagnosis 缩范围可压到数天。
- **关键工具（与 Track 02 关联）**：e-beam/SEM/TEM/FIB（KLA/AMAT/厂商）+ scan diagnosis（Siemens Tessent）+ YMS 关联 fab/test 数据。 (evidence: [T02-S019, T03-S002])
- **关键人物（与 Track 01 关联）**：FA 根因闭环呼应 canon May&Spanos 的「良率诊断 playbook」与 glossary「FA 不修单片而找根因反馈改工艺」。 (evidence: [T04-S034])
- **常见失败模式**:
  - **不先电性定位就盲 FIB**：在 mm² 级 die 上找 nm 级缺陷如大海捞针，烧掉样品和数周 —— 先 scan diagnosis/EMMI/OBIRCH 缩到 net 级再切。
  - **一上来破坏 deprocess**：丢失原始失效证据（充填物/可移动离子/电荷） —— 非破坏（X-ray/SAM/红外）先行。
  - **把表象当根因**：看到 particle 就归因 particle，没追到 particle 从哪来，改了照样复发 —— 追到 particle 源工艺步骤/设备再 corrective。
  - **FA 不闭环到工艺**：报告归档但工艺没改，同失效再现 —— 强制每个 FA 出 corrective action + split 验证关闭。
- **来源** (≥3): [Surrogate-Primary] T03-S002 Siemens Tessent（scan diagnosis own publication）/ [Primary] T04-S034 May & Spanos（良率诊断方法学）/ [Reference] T03-S007 OrcaLean（BKM 复制闭环）。
- **Last_updated**: 2026-06-21
- **Decay risk**: **low**（FA 物理方法学稳态；scan diagnosis/ML 为电性定位环节的增量优化）

---

### 5. DTCO 设计-工艺协同优化（pathfinding → 协同迭代 → 设计规则/标准单元 → PDK）

- **One-liner**: 从「单纯 dimensional scaling（缩尺寸）收益不足、PPAC 提升乏力」到「通过设计与工艺反复协同迭代，挤出额外 PPAC 的设计规则 + 标准单元 + PDK」。等效微缩时代的核心方法学。 (evidence: [T03-S004, T04-S018])
- **Trigger**: 新节点单靠物理微缩无法达 PPAC 目标 / 需要在固定工艺能力下用设计手段再提密度功耗 / 引入新器件架构（GAA/CFET/BSPDN）需要设计同步演化。
- **Output**: 协同优化后的设计规则（pitch/track height/MOL 规则）+ 优化的标准单元库 + 给客户的 PDK + 系统级 STCO 反馈。
- **入门 SOP（minimum viable steps）**:
  1. **Technology 阶段 pathfinding**：探索器件架构/工艺选项与对应 PPAC，用 TCAD/SEMulator3D 评估候选。 (evidence: [T03-S004])
  2. **设计-工艺协同迭代**：把工艺能力（可做的最小 pitch、overlay 预算）与设计需求（标准单元高度、布线资源）反复对撞，找联合最优。 (evidence: [T03-S004])
  3. **Design Enablement（产出 PDK）**：生成器件模型、标准单元库、布线 tech file、RC 寄生模型。 (evidence: [T03-S004])
  4. **Design 阶段验证**：用 PDK 做逻辑综合 + place&route，回测真实设计的 PPAC 是否达标，不达标回到 step2。 (evidence: [T03-S004])
  - **每一步如果跳过会发生什么**:
    - 跳 step1（pathfinding）→ 锁死在次优架构，后期无法翻盘。
    - 跳 step2（协同迭代）→ 工艺与设计各自为政，做出来的规则要么工艺做不出要么设计用不上。
    - 跳 step4（真实设计回测）→ 规则在纸面最优但真实 P&R 后 PPAC 不达标，节点白做。
- **资深路径（差异点）**：
  - **skip**：资深团队**跳过纯 dimensional scaling 的死磕** —— 知道某些 pitch 已到物理/光刻极限，不再缩尺寸，改用 DTCO 设计手段（如单元高度优化、MOL 引入）提密度。 (evidence: [T04-S018])
  - **add**：资深团队**额外把 STCO（系统-工艺协同）纳入** —— 初学者只在 cell 级 DTCO，资深人把芯片/系统级（如先进封装、3D 堆叠）一起协同。 (evidence: [T03-S004])
  - **optimize**：资深团队用**自动化 pathfinding 框架**（如 PROBE3.0 类）批量评估设计-工艺组合，而非人工逐个试。 (evidence: [T03-S004])
- **近期变化**（近 12 个月）：
  - **medium decay**：DTCO 从「cell 级」向 **STCO（系统级）+ 3D/先进封装协同** 扩展；**背面供电 BSPDN（A16）** 是 DTCO 重塑 BEOL 的标志。触发事件类型：新器件架构 + 系统级协同需求。 (evidence: [T03-S004, T04-S007])
  - 2025-11 P-PDK 让 DTCO 方法学进入学界。 (evidence: [T03-S006])
- **典型耗时**: 入门/一个节点的 DTCO 协同 = 数月-1 年（嵌在节点导入大流程内）；资深用自动 pathfinding 可缩短迭代。
- **关键工具（与 Track 02 关联）**：TCAD Sentaurus + SEMulator3D（pathfinding）+ EDA（综合/P&R）+ Calibre（DRC 规则验证）。 (evidence: [T02-S006, T02-S008, T02-S010])
- **关键人物（与 Track 01 关联）**：Mark Bohr（hyperscaling / 节点真密度 = DTCO 思想源）；Scotten Jones（DTCO 成本经济学）；canon IEDM DTCO/STCO short course。 (evidence: [T01-S020, T01-S018, T04-S019])
- **常见失败模式**:
  - **死磕 dimensional scaling**：在已到光刻/物理极限的 pitch 上硬缩，良率/成本崩 —— 改用 DTCO 设计手段提密度。
  - **工艺设计不协同**：规则工艺做不出或设计用不上 —— step2 反复对撞迭代。
  - **只做 cell 级 DTCO 忽略系统**：错失 STCO/3D 封装的等效微缩红利 —— 把系统级纳入协同。
- **来源** (≥3): [Surrogate-Primary] T03-S004 IEDM 2023 DTCO/STCO short course / [Primary] T04-S018 TSMC "What is DTCO?" vendor blog / [Primary] T04-S007 IRDS / [Secondary] T03-S006 Electronics Weekly。
- **Last_updated**: 2026-06-21
- **Decay risk**: **medium**（DTCO 三阶段骨架稳，但 STCO/3D/BSPDN 协同范围在持续扩展）

---

### 6. 工艺移植 / Copy-Exactly（TD→HVM、fab→fab 量产移交与持续改善）

- **One-liner**: 从「一个工艺在研发线（TD）或源 fab 跑通」到「在量产 fab / 新 fab 严格复制、参数与良率匹配源线、快速 ramp」。Intel "Copy Exactly!" 是其经典方法学。 (evidence: [T03-S007])
- **Trigger**: 工艺从技术开发线转量产 HVM / 扩产到新 fab / 多 fab 共线生产同一产品需要参数一致。
- **Output**: 新 fab 良率与参数匹配源 fab + 快速量产 ramp + 多 fab 作为「虚拟工厂」同步改善（BKM 双向复制）。
- **入门 SOP（minimum viable steps）**:
  1. **锁定基线（everything matters）**：把源线的设备型号/配方/材料/量测/even 看似无关的参数全部记录为基线 —— copy exactly 的前提是先冻结一切。 (evidence: [T03-S007])
  2. **严格复制到目标 fab**：目标 fab 用相同设备型号、相同配方、相同材料、相同操作，不做「本地优化」。 (evidence: [T03-S007])
  3. **参数比对与匹配（matching）**：用相同测试结构跑两线，比对 CD/电性/良率分布，差异处查设备指纹（chamber matching）。
  4. **达匹配后 ramp**：匹配确认后快速放量，because 工艺已锁定。 (evidence: [T03-S007])
  5. **BKM 双向回流**：任一 fab 找到改善（BKM），经评估后同步复制到所有同工艺 fab（虚拟工厂）。 (evidence: [T03-S007])
  - **每一步如果跳过会发生什么**:
    - 跳 step1（冻结基线）→ 不知道源线到底有哪些参数在起作用，目标线复制不全，良率差异查不出根因。
    - 跳 step2（严格复制、不本地优化）→ 目标 fab 工程师「好心」本地优化，引入未知变量，破坏 matching。
    - 跳 step3（matching 比对）→ 没确认匹配就 ramp，量产良率与源线差一截才发现。
    - 跳 step5（BKM 回流）→ 一个 fab 的改善困在本地，其他 fab 重复踩坑。
- **资深路径（差异点）**：
  - **skip**：资深团队在量产移交期**跳过「重新优化」的冲动** —— 经验告诉他们 copy-exactly 期间任何本地优化都是 matching 杀手，宁可先一致再统一改善。 (evidence: [T03-S007])
  - **add**：资深团队**额外做设备指纹/chamber matching 比对**，初学者只比最终良率，资深人比到 chamber 级参数指纹，提前发现漂移源。 (evidence: [T03-S007])
  - **optimize**：资深团队用**虚拟工厂 BKM 双向回流机制**，把多 fab 当一个虚拟工厂，改善一处复制全网，而非各 fab 各自摸索。 (evidence: [T03-S007])
- **近期变化**（近 12 个月）：
  - **稳态为主**：Copy Exactly! 方法学 1990s 至今骨架稳定（行业稳态，最近显著变化是把 copy-exactly 与 FDC/APC/数字孪生数据系统结合做实时 matching）。触发事件类型：新工具（FDC/数字孪生辅助 matching）。 (evidence: [T03-S007])
- **典型耗时**: 入门/单 fab 工艺移植 matching = 数月；资深用指纹比对 + 虚拟工厂可压缩匹配周期。
- **关键工具（与 Track 02 关联）**：FDC/APC（AMAT E3）+ YMS（跨 fab 良率比对）+ MES + SEMulator3D（数字孪生）。 (evidence: [T02-S008, T02-S017])
- **关键人物（与 Track 01 关联）**：Mark Bohr（Intel 工艺/Copy Exactly! 文化代表）；梁孟松（工艺整合移植大师，TSMC→Samsung→SMIC 跨线移植 know-how）。 (evidence: [T01-S020, T01-S028])
- **常见失败模式**:
  - **目标 fab「本地优化」破坏 matching**：好心改配方引入未知变量，两线对不齐 —— copy-exactly 期严禁本地优化，先一致再统一改。
  - **只比最终良率不比 chamber 指纹**：matching 差异根因藏在 chamber 级参数，最终良率掩盖了过程漂移 —— 做设备指纹/chamber matching。
  - **BKM 困在单 fab**：改善不回流，其他 fab 重复踩同一坑、浪费数月 —— 虚拟工厂机制双向复制 BKM。
- **来源** (≥3): [Secondary] T03-S007 OrcaLean（Intel Copy Exactly!/虚拟工厂/BKM）/ [Primary] T04-S034 May & Spanos（过程控制/matching 方法学）/ [Reference] T01-S028 梁孟松（跨线工艺移植案例）。
- **Last_updated**: 2026-06-21
- **Decay risk**: **low**（Copy Exactly! 方法学 30 年稳态；数字孪生/FDC 为辅助增量）

---

### 7. 光刻层 patterning 方案开发（曝光条件 → OPC/计算光刻 → overlay 预算 → 多重曝光分解）

- **One-liner**: 从「一个关键层在给定光刻能力（DUV 193i / EUV 0.33NA / high-NA 0.55NA）下需要成像合格」到「一套 patterning 方案：mask + OPC + 必要的多重曝光分解 + overlay 预算」。光刻是 fab 的中枢节奏。 (evidence: [T03-S011, T02-S010])
- **Trigger**: 新节点关键层的 pitch 超出单次曝光分辨率 / 需要在既有光刻平台上把某层做出来 / 引入 EUV 或 high-NA 改变 patterning 策略。
- **Output**: patterning 方案（mask 数据 + OPC/ILT 校正 + 是否多重曝光及如何分解 SADP/SAQP + overlay 误差预算 + 随机缺陷预算）。
- **入门 SOP（minimum viable steps）**:
  1. **定曝光平台与 k1**：根据层 pitch 与可用光源（193i/EUV/high-NA）判断单次曝光能否成像（k1 因子），决定是否需要多重曝光。 (evidence: [T03-S011])
  2. **若需则做多重曝光分解**：把单层图案分解成多次曝光（LELE 或自对准 SADP/SAQP），分解算法保证可制造且 overlay 可控。 (evidence: [T03-S011])
  3. **OPC / 计算光刻**：用 OPC/ILT（Calibre/Proteus）对 mask 做光学邻近校正/逆光刻，补偿衍射与邻近效应。 (evidence: [T02-S010, T02-S011])
  4. **overlay 预算与量测反馈**：定 overlay 误差预算（先进节点 <2nm），用量测（KLA overlay）反馈到曝光机做高阶校正。 (evidence: [T03-S011])
  5. **随机缺陷 / 工艺窗口验证**：EUV 层验证 stochastic 缺陷（line-edge roughness/bridging）预算与曝光-焦深工艺窗口。 (evidence: [T03-S011])
  - **每一步如果跳过会发生什么**:
    - 跳 step1（k1/平台判断）→ 选错平台（该多重曝光却单曝），图案根本成不了像。
    - 跳 step3（OPC）→ 不做邻近校正，实际硅上图案严重失真（线端缩短/桥接），良率为零。
    - 跳 step4（overlay 预算）→ 多重曝光各层对不齐，pattern 错位短路/断路。
    - 跳 step5（随机缺陷，EUV）→ EUV 层 stochastic 缺陷失控，随机 bridging/断线良率塌。
- **资深路径（差异点）**：
  - **skip**：资深团队在有 EUV/high-NA 时**跳过多重曝光分解** —— EUV 单次曝光替代 DUV 的 SADP/SAQP，减少 mask 数、overlay 步骤与缺陷源（high-NA 0.55NA 把单曝推到 8nm）。 (evidence: [T03-S011, T02-S003])
  - **add**：资深团队**额外为 EUV 层做 stochastic 随机缺陷预算 + SMO 源-掩膜协同优化**，初学者只做 OPC，资深人知道 EUV 光子散粒噪声导致的随机缺陷是先进层主良率杀手。 (evidence: [T03-S011])
  - **optimize**：资深团队用 **GPU 加速曲线 ILT（cuLitho）** 做全芯片逆光刻，比 CPU Manhattan OPC 快 10-20x 且 2D/contact 成像更优。 (evidence: [T02-S035, T02-S036])
- **近期变化**（近 12 个月）：
  - **high decay**：**high-NA EUV（ASML EXE:5200B，2025-Q2 首台 → Intel 14A）** 把单曝分辨率推到 8nm，正在消除 sub-2nm 关键层的多重曝光；**GPU/ML 曲线 ILT（cuLitho，2023→2025 论文成熟）** 改写 OPC 流程。触发事件类型：新设备（high-NA EUV）+ 新工具（GPU 计算光刻）。当前采用率：high-NA 仅 Intel 量产引入，TSMC 推迟到 ~A10/2029。 (evidence: [T02-S003, T02-S004, T02-S035, T03-S011])
- **典型耗时**: 入门/一个关键层 patterning 方案 = 数周-数月；资深用 EUV 单曝 + GPU ILT 可减少 mask 层数与 OPC runtime。
- **关键工具（与 Track 02 关联）**：ASML EUV/DUV/high-NA + Calibre/Proteus OPC/ILT + cuLitho（GPU ILT）+ KLA overlay 量测 + TEL coat/develop track。 (evidence: [T02-S003, T02-S010, T02-S011, T02-S035])
- **关键人物（与 Track 01 关联）**：林本坚（浸没式 193i，多重曝光时代基石）；Martin van den Brink（EUV/high-NA 工程）；canon Mack《Fundamental Principles of Optical Lithography》。 (evidence: [T01-S004, T01-S006])
- **常见失败模式**:
  - **不做 OPC 直接上 mask**：硅上图案严重失真（线端缩短/桥接），整层报废 —— OPC/ILT 是关键层强制步骤。
  - **多重曝光 overlay 失控**：各次曝光对不齐，先进节点 <2nm overlay 超标短路 —— 严格 overlay 预算 + 高阶量测反馈。
  - **EUV 层忽略 stochastic 缺陷**：只调平均成像、不做随机缺陷预算，random bridging/断线良率塌 —— EUV 层必做 stochastic 预算 + SMO。
  - **盲目追 high-NA**：经济性未证明就引入 high-NA（>3.5 亿美元/台），成本墙 —— 评估单曝收益 vs 多重曝光成本再决定（TSMC 即因此推迟）。 (evidence: [T02-S005])
- **来源** (≥3): [Secondary] T03-S011 Semiconductor Engineering（单曝 vs 多重曝光）/ [Primary] T02-S003 ASML high-NA EXE:5200B（vendor doc）/ [Primary] T02-S035 ACM ISPD 2025 GPU ILT 论文 / [Primary] T02-S010 Siemens Calibre（vendor doc）。
- **Last_updated**: 2026-06-21
- **Decay risk**: **high**（high-NA EUV ramp + GPU/ML 计算光刻 12 月内显著改写多重曝光与 OPC 流程）

---

<!-- (option) 先进封装集成 workflow 的核心步骤已并入 workflow 3/6 的工具与 Phase2；hybrid bonding 工艺流见 T02-S024/T03-S009/T03-S010，作为单元工艺配方开发(workflow 2)在后道的实例。 -->

## Phase 2 提炼提示

**反复出现 ≥3 个 workflow 都包含的步骤**（候选 playbook 通则）:
- **「DOE 找工艺窗口」** 出现于 workflows 1（单元工艺开发子步）/ 2（核心）/ 5（pathfinding 评估）→ 候选 playbook「如果要锁定/评估任何工艺或设计-工艺组合，则用 DOE/pathfinding 扫参数找窗口中心，不 OFAT、不穷举」。
- **「commonality / 逐层定位」** 出现于 workflows 3（良率爬坡核心）/ 4（FA 电性定位）/ 6（chamber matching 指纹）→ 候选 playbook「如果出现良率/参数差异，则先做 commonality（设备/层/时间/fab 共性）定位到工艺源，再深挖根因」。
- **「SPC 固化 + BKM 复制」** 出现于 workflows 2（移交）/ 3（改善固化）/ 6（虚拟工厂 BKM）→ 候选 playbook「任何改善都必须固化进 SPC/APC 并写成 BKM 复制到同类产线，否则复发」。
- **「split lot 验证后再上线」** 出现于 workflows 2/3/4 → 候选 playbook「任何工艺改动，先 split lot 验证提升且无副作用，再固化量产」。
- **「设备/工艺是必要非充分，良率 know-how 是壁垒」** 出现于 workflows 1/3 + 跨 Track 02/04/06 → 头号 playbook：判断能否做先进制程查设备+材料+工艺+整合+良率五要素，别只看光刻机。 (evidence: [T01-S017, T04-S034])

**入门 SOP 和资深路径之间最大的差距**（候选 心智模型）:
- 资深差异高度集中在三类「在低信息阶段不穷举」的判断：
  - **靠经验砍 DOE 因子**（workflow 2）—— 不全因子穷举，先砍到主因子。
  - **靠 spatial signature / commonality 跳过全检**（workflow 3）—— 看 wafer map 空间签名就锁层，不全晶圆全检。
  - **靠 scan diagnosis 跳过盲 FIB**（workflow 4）—— 先电性缩范围再物理切。
  - **靠 copy-exactly 抑制本地优化冲动**（workflow 6）—— 先一致再统一改。
  - → 共同心智模型候选：**「先用低成本信息（经验/空间签名/电性诊断/上代节点）大幅缩小搜索空间，再投入昂贵的实验/物理/晶圆资源」** —— 这一行资深人最擅长的是「不在低信息阶段穷举或过度优化」。
- 另一组资深差异是「协同/系统视角」：DTCO/TCAD 前置（workflow 1/5）、电性+物理双轨 commonality（workflow 3）、虚拟工厂 BKM（workflow 6）→ 心智模型候选「单模块极致优化 ≠ 系统最优，工艺决策要在模块/设计/系统间协同求解」。

**近期工作流变化的根本原因**:
- 触发事件类型分布（7 个 workflow）：
  - **新器件架构驱动（medium decay）**：workflow 1、5（GAA nanosheet 2025 量产 / CFET / 背面供电 BSPDN A16 / DTCO→STCO 扩展）。
  - **新设备 + 计算驱动（high decay）**：workflow 7（high-NA EUV 2025 ramp + GPU/ML 曲线 ILT）。
  - **ML/数据工具增量（不改骨架，low decay）**：workflow 2（ML 配方优化）、3（ML defect Pareto/pattern family）、4（volume scan diagnosis）、6（数字孪生 matching）。
- 主要外部驱动力：①等效微缩（DTCO/3D 封装）接替 dimensional scaling；②EUV/high-NA 光刻代际跃迁；③ML/数据驱动渗透良率与配方（增量非颠覆）；④地缘出口管制（影响国产线的设备/材料可得性，但不改方法学骨架）。

**冷僻 / 信号薄弱自检**:
- workflow 数 = **7**（floor 4 ✅，目标 6-12 ✅）。
- 资深差异点：**7/7 workflow 均有 ≥2 处资深差异（skip/optimize/add）** = 100% ≥ 80% floor ✅。
- 近期变化字段：7/7 都填了（4 个明确「稳态」+ 3 个具体变化）= 100% ≥ 60% ✅。
- 一手率：workflow claim 一手覆盖 ≥55%（canon/IEDM/vendor/.edu/imec/论文一手 + surrogate_primary 协会/顶会/own-publication），市场媒体留 secondary ≥ 50% floor ✅。
- decay risk 每个标 ✅（low 4 / medium 2 / high 1）。
- **结论**：workflow 维度**信号充足**。本行业 workflow 一手藏于顶会 short course + 教材方法学 + 设备厂白皮书 + .edu nanofab SOP + 研究机构（imec），已最大化一手；具体 fab 内部 recipe/良率数字属商业机密（tacit），方法学骨架可考据但参数级细节须诚实标 tacit。Phase 2.8 须标「工作流节 decay：4 low（工艺方法学稳态）/ 2 medium（GAA/CFET/DTCO）/ 1 high（high-NA/计算光刻），high decay 项建议每 3-6 月跑 update」。
