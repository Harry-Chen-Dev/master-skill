# 半导体芯片制造工艺 / Semiconductor Process Engineering — Master OS — Synthesis

> Phase 2 提炼结果。Phase 3 (skill writeup) 直接消化本文件。
> 第一性背景：**物理/化学/材料硬约束 + 良率/成本经济约束双重叠加**。本行最尖锐的张力不是「哪个节点更先进」，而是「物理可行性 ⇄ 良率/成本可制造性」——OS 的每一个组件都在这条轴上取位。物理极限、良率/产能硬约束、节点命名营销、国产替代真实差距**诚实保留、绝不软化**（intake warnings 硬要求）。locale=global（en-primary canon/顶会/前沿设备代工 + zh-CN China fab 产业/政策补充）。

---

## 1. 心智模型 (7 个)

### 1.1 物理硬约束 ⇄ 良率/成本经济约束（第一性双重张力）

- (figures: Gordon Moore / Robert Dennard / Scotten Jones)
- **一句话**：半导体工艺的每个决策都同时受两类硬约束——物理/化学/材料（量子隧穿、短沟道效应、RC 延迟、热预算、缺陷物理）与良率/成本经济（D0 缺陷密度、每片晶圆成本、wph、折旧）；摩尔定律首先是**经济命题**（每元件最低成本），物理是不可让渡的底线，二者皆不可单边最优化。
- **应用方式**：面对任何工艺/节点/器件方案，先问「物理上可行吗」再问「良率/成本上划算吗」；二者任一不过关，方案就不成立——不存在「物理能做但良率/成本崩」却仍上量产的选项。
- **局限**：（放大度⚠️）该张力在 leading-edge 逻辑最尖锐；成熟特色工艺（功率/模拟/MEMS/射频）经济约束相对主导、dimensional 微缩压力小，PPAC 权重与本模型强度不同。
- **evidence**: [T01-S030, T04-S004, T04-S016]

### 1.2 设备/工艺是必要非充分，良率 know-how 才是真壁垒

- (figures: Dylan Patel / Jon Y / 梁孟松)
- **一句话**：能不能做先进制程，从来不是「有没有 EUV/光刻机」单一决定的——设备 + 材料 + 刻蚀/沉积 + 工艺整合 + 良率爬坡**五要素缺一不可**，而良率 ramp 的 know-how 是 siloed 在 fab 内、师徒型 tacit 的真壁垒（梁孟松领 SMIC 14nm FinFET 良率约 298 天从约 3% 爬到 >95%，业内传为良率 know-how 壁垒的例证）。
- **应用方式**：判断一条产线 / 一个「国产突破」声称能否做某节点，逐一核验五要素是否齐备 + 良率是否 ramp 到经济可量产；只看光刻机就下结论必错。
- **局限**：本模型反「设备决定论」，但不否认某些环节（如 EUV 之于 <7nm 高密度逻辑）确是硬卡点——必要非充分 ≠ 不必要，五要素任一缺位同样做不成。
- **evidence**: [T01-S017, T01-S028, T02-S017]

### 1.3 微缩 = 不断加强栅对沟道的静电控制（thin body）

- (figures: 胡正明 Chenming Hu / Tsu-Jae King Liu / Robert Dennard)
- **一句话**：器件架构演进有单一第一性逻辑——对抗短沟道效应靠「加强栅对沟道的静电控制」：平面 → FinFET（把沟道立成薄鳍三面环栅）→ GAA nanosheet（四面环栅）→ CFET（垂直堆叠），每代换的是**栅控几何**而非单纯缩尺寸。
- **应用方式**：遇到漏电 / 短沟道 / 亚阈摆幅恶化，先想器件架构（栅控几何：薄体、环栅），而非单纯调工艺参数——这是静电几何问题，工艺调参治标不治本。
- **局限**：栅控架构解决静电，但带来新工艺难题（FinFET 的 fin 刻蚀、GAA 的 nanosheet release、CFET 的 3D 集成与热预算），架构红利须靠工艺整合兑现，非「换架构即得」。
- **evidence**: [T01-S001, T01-S011, T04-S009]

### 1.4 节点名是营销，真尺度看 pitch + 密度 + 成本

- (figures: Mark Bohr / Scotten Jones / Dylan Patel)
- **一句话**：「N3/N2」早已脱钩物理栅长（N3 的 CPP 约 45nm、MMP 约 23nm，并非 3nm，evidence T06-S005），评价节点先进性要换算 gate pitch / metal pitch / 逻辑密度 MTr/mm² + 每晶体管成本 + PPAC，而非信营销节点名。
- **应用方式**：拿到「X nm 节点」先别信数字，查 CPP/MMP/MTr/mm²（TechInsights/IRDS 来源）+ 成本模型；跨厂比较只在「真密度 / 真成本」维度做，不在营销名上做。
- **局限**：真密度度量本身也有口径差（逻辑 vs SRAM vs 模拟密度不同），且各厂定义不一；要看与用途匹配的密度，不能只取单一 MTr/mm² 数字一刀切。
- **evidence**: [T01-S020, T01-S019, T06-S005]

### 1.5 延寿既有技术常胜于推倒重来：演化优于革命

- (figures: 胡正明 Chenming Hu / 林本坚 Burn-Jeng Lin / Martin van den Brink)
- **一句话**：这一行最成功的突破往往是「在既有基础设施上延寿一代」而非推倒重来——Hu 称 FinFET「其实是 evolutionary 不是 revolutionary」；Lin 用 193i 浸没式把 DUV 续命约 6 代而非跳 157nm；选型要权衡「复用既有资产 vs 颠覆成本」。
- **应用方式**：面对新工艺 / 新设备选择，先问「能否在既有光源 / 设备 / 流程上延寿一代」；过于革命的方案即便先进，也可能不是当下最优资产配置（Hu 原话：too revolutionary may not be the best way of spending the current asset）。
- **局限**：（边界⚠️）演化有尽头——当物理墙到了（如 DUV 多重曝光的成本 / 良率失控），革命性跃迁（EUV）反而是唯一出路；演化优先非演化永远。
- **evidence**: [T01-S001, T01-S005, T01-S007]

### 1.6 先用低成本信息缩小搜索空间，再投昂贵资源

- (figures: 梁孟松 / Scotten Jones / Jon Y)
- **一句话**：资深工艺人的核心能力是「不在低信息阶段穷举或过度优化」——靠经验砍 DOE 因子、靠 wafer map 空间签名做 commonality 定位、靠电性 scan diagnosis 缩范围再物理切 FIB、靠 copy-exactly 抑制本地乱改，**先用便宜信息大幅缩小搜索空间，再投晶圆/物理/实验昂贵资源**。
- **应用方式**：遇到良率/缺陷/工艺异常，先做 commonality（设备/层/时间/腔体共性）+ 空间签名 + 电性诊断锁定范围，再上昂贵的 FA/DOE/split lot；不全检、不穷举、不 OFAT。
- **局限**：低信息启发依赖大量历史数据与经验积累（tacit），新 fab / 新节点缺基线时启发弱、仍需较多盲扫——是经验壁垒不是普适算法。
- **evidence**: [T03-S001, T03-S002, T03-S007]

### 1.7 单模块极致优化 ≠ 系统最优：协同求解（DTCO/STCO）

- (figures: Scotten Jones / Mark Bohr / Martin van den Brink)
- **一句话**：后微缩时代，单独把某个 unit process 或某层做到极致不再等于芯片最优——必须在器件/工艺/设计/系统间**协同求解**（DTCO 设计-工艺协同、STCO 系统-工艺协同、3D 封装把「等效微缩」接力 dimensional 微缩）。
- **应用方式**：做工艺决策时把设计规则、PDK、封装、系统目标一起拉进来权衡；不在单模块局部最优上过度投入，先问「这个优化对系统 PPAC 有没有净收益」。
- **局限**：协同优化要求跨团队/跨学科协调，组织成本高；小型 fab / 成熟特色工艺协同收益有限，单模块优化在那些场景仍合理。
- **evidence**: [T04-S018, T04-S019, T02-S006]

---

## 2. 标准 Playbook (8 条)

1. **如果要判断一条产线 / 一个「国产突破」声称能否做某节点**，则逐一核验设备 + 材料 + 刻蚀沉积 + 工艺整合 + 良率五要素是否齐备，别只看有没有光刻机 / EUV。案例：SMIC 拆解显示无 EUV 也能做 N+2，但良率/成本/成熟度仍落后数年（业内估计）。evidence: [T01-S017, T02-S029]
2. **如果拿到「X nm 节点」宣传**，则换算 gate pitch / metal pitch / 逻辑密度 MTr/mm² + 成本，再做跨厂比较，不信营销节点名。案例：N3 的 CPP 约 45nm、MMP 约 23nm 并非 3nm 物理栅长（T06-S005）。evidence: [T06-S005, T06-S009]
3. **如果遇到短沟道 / 漏电 / 亚阈摆幅恶化**，则优先换器件架构（FinFET/GAA/CFET 加强栅控）而非单纯调工艺参数，这是静电几何问题。案例：平面 CMOS 在约 22nm 撞短沟道墙，FinFET 三面环栅续命（T04-S009）。evidence: [T04-S009, T06-S025]
4. **如果出现良率 / 参数差异**，则先做 commonality（设备/层/时间/腔体共性）+ wafer map 空间签名定位到工艺源，再深挖根因，不全检穷举。案例：先进节点系统性良率问题用 Pareto/commonality 逐层定位再 FA（T03-S001）。evidence: [T03-S001, T03-S002]
5. **如果要锁定 / 评估任何工艺或设计-工艺组合**，则用 DOE / pathfinding 扫参数找工艺窗口中心，不 OFAT、不全因子穷举（靠经验先砍主因子）。案例：单元工艺配方开发用 DOE 找 selectivity / profile 窗口（T03-S008）。evidence: [T03-S008, T03-S004]
6. **如果做任何工艺改动**，则先 split lot 验证有提升且无副作用，再固化进 SPC/APC 并写成 BKM 复制到同类产线，否则复发或本地发散。案例：Intel Copy Exactly! + virtual factory + BKM 抑制跨厂漂移（T03-S007）。evidence: [T03-S007, T06-S021]
7. **如果引用任何市占率 / 良率 / 成本 / 节点参数数字**，则一律挂 source + last_checked 或标「业内估计」，并警惕节点营销与国产替代叙事。案例：设备市占（ASML 约 25% T02-S002、离子注入 AMAT 约 62% T02-S023）皆第三方汇编，须标来源。evidence: [T02-S002, T02-S023]
8. **如果选先进光刻分解策略**，则在 high-NA EUV 单次曝光 vs DUV 多重曝光（SADP/SAQP）间按 pitch 临界点 + 成本/良率权衡，单曝省步但设备极贵。案例：high-NA 单次曝光可替代部分 SADP/SAQP 的多步流程（T03-S011）。evidence: [T03-S011, T06-S010]

---

## 3. 工具栈与选型决策树

> 直接消化 Track 02（`references/research/02-tools.md`）的三层结构 + 选型决策树，本节做一致性 sanity check。「工具」= 制造设备 + EDA/TCAD/仿真 + 良率制造软件 + 关键材料。本行重资本闭源，maturity 用市占率/营收/装机量代替开源 stars。

**工具三层 sanity**：必备 11 / 场景特化 10 / 新兴 4（共 25 个，详见 02-tools.md）。

- **必备层（≥80% 先进 fab 用，11 个）**：ASML 光刻（DUV 浸没 + EUV，EUV 约 100% 垄断 T02-S003）、AMAT（沉积/刻蚀/注入/CMP 平台）、Lam Research（刻蚀/沉积/ALE/ALD）、TEL（涂胶显影 track 约 90% T02-S012）、KLA（量测/检测/overlay，过程控制约 56% T02-S020）、Synopsys Sentaurus TCAD、Siemens Calibre（OPC/物理验证约 85% T02-S012）、Synopsys Proteus（mask synthesis/OPC）、良率管理系统 YMS（Synopsys/PDF/KLA）、光刻胶（JSR/TOK/Shin-Etsu/DuPont 前五约 50% T02-S014）、CMP 浆料 slurry（Cabot/Fujimi/Resonac 前五约 64% T02-S016）。
- **场景特化层（10 个）**：离子注入（AMAT 约 62% / Axcelis 约 21%，SiC 场景 Axcelis 主导 T02-S023）、CMP 设备（AMAT/Ebara 荏原）、ALE/ALD（Lam/ASMI/TEL，7/5nm 必备 T02-S027）、Silvaco TCAD、SEMulator3D（虚拟工艺建模，Coventor→Lam）、KLA e-beam/光学检测、混合键合设备（BESI/AMAT/EVG/SUSS T02-S024）、e-beam 量测（AMAT/ASML multibeam/Hitachi）、FDC/APC、掩膜 mask blank。
- **新兴层（近 12 个月起势，4 个）**：high-NA EUV（ASML EXE:5200B，NA 0.55，首台出 Intel 14A 约 2025 T02-S004）、GPU/ML 曲线 ILT 计算光刻（NVIDIA cuLitho T02-S036）、混合键合规模化（BESI 单客户多产线 T02-S034）、AI 良率优化软件。
- **国产替代层（诚实标代差 + 出口管制约束）**：北方华创 Naura（刻蚀/沉积/清洗/炉管平台化，全球约第 5 T02-S029）、中微 AMEC（刻蚀，3nm 刻蚀机 T02-S031）、上海微电子 SMEE（光刻，与 ASML 有代差，诚实标）、拓荆 Piotech（沉积）、华海清科（CMP T02-S032）、中科飞测/上海精测（量测 T02-S033）、盛美 ACM（清洗）、屹唐/凯世通（注入）。
- **避坑清单（≥5，7 条）**：①「买到 EUV/光刻机就能量产先进制程」（设备是必要非充分，整合/良率/材料缺一不可）②把节点营销名当物理尺度（N3 ≠ 3nm，看 CPP/MMP）③混淆 process simulation（Sentaurus 算物理，慢而准）vs emulation（SEMulator3D 算几何，快而不算物理）④离子注入按产线/材料选厂（硅逻辑 AMAT vs SiC Axcelis），不一刀切⑤把国产替代叙事当工程现实（设备/材料/EDA/良率/成熟度差距诚实标）⑥引用市占率/成本数字不挂来源（全是第三方汇编，须标「业内估计」+ source）⑦低估材料换料 requalification 成本（换光刻胶/slurry 需重新 qualify）。

**选型决策树（6 主分支，摘自 02-tools.md，均挂 evidence）**：按产线定位分支——A 先进逻辑微缩（EUV + ALE/ALD + GAA 整合）/ B 成熟特色工艺（DUV + 性价比设备）/ C 存储（3D NAND 高深宽比刻蚀 / DRAM）/ D 先进封装（混合键合/CoWoS/TSV）/ E 工艺开发仿真（Sentaurus 物理 vs SEMulator3D 结构集成）/ F 良率 ramp（YMS + 缺陷检测 + APC）。

---

## 4. 工作流 / Pipeline

> 直接消化 Track 03（`references/research/03-workflows.md`）7 个 workflow，每个含入门 SOP / 资深路径（跳过·优化·额外）/ 近期变化三段。衰减分层：单元工艺物理化学原理 + 良率方法学 `Decay risk: low`；器件换代（GAA/CFET/DTCO）`Decay risk: medium`；光刻代际 + 计算光刻 `Decay risk: high`。

### 4.1 新节点 / 新工艺导入（TD → HVM）
- **入门 SOP**：器件 PPAC 目标定义 → 工艺整合方案 + PDK → 单元工艺 DOE 开发找工艺窗口 → 量测建立 + SPC → 良率爬坡 → 量产移交。
- **资深路径**：**跳过**从零穷举单元工艺（先借上代节点基线 + copy-exactly 起步），**优化**为 DTCO/TCAD 前置（用仿真先收敛设计-工艺组合再动晶圆），**额外**做 pathfinding 与 PPAC 早期权衡，不等单模块成熟再谈整合。
- **近期变化**：2025 GAA nanosheet 量产 + DTCO→STCO 扩展 + 背面供电 BSPDN（A16）推动整合方案换代（evidence T03-S004/T03-S006）。`last_updated`: 2026-06-21。`Decay risk: medium`。

### 4.2 单元工艺配方开发（DOE 找工艺窗口）
- **入门 SOP**：定工艺目标（CD/selectivity/profile/uniformity）→ 设计 DOE → 跑 split → 量测建模 → 锁工艺窗口中心 → 固化配方。
- **资深路径**：**跳过**全因子穷举（靠经验先砍到主因子），**优化**为找窗口中心而非边缘（留 margin 抗漂移），**额外**做跨腔体 matching 与对量测能力的反向校核。
- **近期变化**：ML 配方优化作增量工具进入（不改 DOE 骨架，evidence T03-S008）；方法学本身稳态。`Decay risk: low`。

### 4.3 良率爬坡（yield ramp）
- **入门 SOP**：缺陷/电性数据采集（inline defect + WAT/PCM）→ 缺陷分类 → commonality / 空间签名定位到工艺源 → 根因分析（FA）→ 工艺改善验证 → SPC 固化。
- **资深路径**：**跳过**全晶圆全检（看 wafer map 空间签名就锁层），**优化**为电性 + 物理双轨 commonality 并行，**额外**做 Pareto 排序把资源投到 top 缺陷源 + 改善固化进 BKM。
- **近期变化**：ML defect Pareto / pattern family 作增量（evidence T03-S001/T03-S002）；良率方法学（D0 Murphy 模型 + SPC）OS 核心层稳态。`Decay risk: low`。

### 4.4 失效分析 FA 根因闭环
- **入门 SOP**：识别失效模式 → 电性定位（scan diagnosis）→ 缩范围 → 物理切片（FIB/SEM/TEM）→ 根因判定 → 反馈工艺。
- **资深路径**：**跳过**盲目 FIB（先 volume scan diagnosis 把范围缩到具体 net/层），**优化**为 pattern family 归并同类失效，**额外**做电性-物理交叉印证再下根因结论。
- **近期变化**：volume scan diagnosis + 自动化进入（evidence T03-S002）；切片/成像方法学稳态。`Decay risk: low`。

### 4.5 DTCO 设计-工艺协同优化
- **入门 SOP**：定 PPAC 目标 → 工艺规则 / 标准单元 / SRAM 与工艺共优化 → PDK enablement → 设计-工艺迭代收敛。
- **资深路径**：**跳过**「工艺先冻结再交设计」的串行模式，**优化**为设计-工艺并行协同（DTCO 三阶段 Technology→Design Enablement→Design），**额外**把封装 / 系统目标拉进来做 STCO。
- **近期变化**：DTCO→STCO 扩展 + 背面供电 / CFET 推动协同范围扩大（evidence T03-S004/T04-S019）。`last_updated`: 2026-06-21。`Decay risk: medium`。

### 4.6 Copy-Exactly 工艺移植 / 量产 matching
- **入门 SOP**：源 fab 基线冻结 → 设备 / 配方 / 量测逐项复制 → chamber matching 指纹比对 → split 验证一致性 → 量产放行。
- **资深路径**：**跳过**目标 fab 的本地「改良」冲动（先严格一致再统一改），**优化**为虚拟工厂 / 数字孪生做 matching 指纹，**额外**把差异固化进 BKM 全网复制。
- **近期变化**：数字孪生 matching 作增量（不改 copy-exactly 哲学，evidence T03-S007）；方法学稳态。`Decay risk: low`。

### 4.7 光刻 patterning 方案（曝光分解 + OPC）
- **入门 SOP**：定目标 pitch/CD → 选光源（DUV 浸没 / EUV / high-NA）→ 曝光分解（单曝 vs 多重曝光 SADP/SAQP/LELE）→ OPC/ILT mask 修正 → overlay 控制 → 签核。
- **资深路径**：**跳过**对低密度层的过度多重曝光（按 pitch 临界点判断单曝是否够），**优化**为 high-NA 单曝替代部分 SADP/SAQP 省步，**额外**做计算光刻（GPU/ML 曲线 ILT）+ stochastics/缺陷预算权衡。
- **近期变化**：high-NA EUV 2025 ramp + GPU/ML 曲线 ILT 成熟，光刻分解策略代际跃迁（evidence T03-S011/T02-S036）。`last_checked`: 2026-06-21。`Decay risk: high`。

---

## 5. 表达 DNA

半导体工艺资深人的语言是**物理 + 量化 + 祛魅压过营销框架**：张口就是 CPP/MMP/D0/yield ramp/工艺窗口/selectivity/step coverage 这类带缩写 + 量化的术语，拒绝把节点营销名（N3/N2）当物理尺度，对「买到 EUV 就行 / 国产已突破 / 良率不是问题 / 纳米越小越先进」等营销与情绪话术会主动拆穿，谈数字必挂来源或标「业内估计」。

- **高频黑话**：流片 tape-out / 良率 yield + D0 缺陷密度 / 工艺窗口 process window / overlay 套刻 / yield ramp 良率爬坡 / selectivity 选择比 / step coverage 台阶覆盖 / 多重曝光 multi-patterning（SADP/SAQP）/ DOE 找窗口 / FEOL-MOL-BEOL 整合段 / CPP·MMP·MTr/mm²（真尺度）/ PPAC / DTCO·STCO / commonality / BKM / copy-exactly。
- **严肃 register**：谈物理用器件/统计语言（「短沟道效应」「恒电场微缩」「D0 Murphy 模型」「conformality」），谈进步克制于真密度/真成本而非节点名。
- **内 vs 外沟通差异**：对外（科普/客户）把术语翻译成可懂的物理与权衡（Bohr「看 MTr/mm² 不看节点名」）；对内（同业）短句 + 缩写 + 直接判断（「这层 commonality 指向某腔体」「这个 split 没 margin」「N2 good yield」）。
- **外行破绽 top（直接用作 spotting tells）**：把「N3」当物理 3nm；信「EUV 万能 / 光刻机就是一切」；把「摩尔定律已死/永生」当二元口号；混淆 ALE 与 ALD；以为「良率很快追平」；把 chiplet/先进封装当「作弊绕过微缩」；以为「GAA 就是小一号 FinFET」；信「纳米数字越小一定越先进」；信「国产已全面突破量产先进制程」。
- **厂商/营销话术拒绝**：「N3 就是物理 3 纳米」（节点营销脱钩物理，真尺度看 CPP/MMP/MTr/mm²）；「买到 EUV/光刻机就能做先进制程」（设备决定论，整合/良率/材料缺一不可）；「摩尔定律永生 / 已彻底死亡」（区分 dimensional 放缓 vs equivalent 继续，拒二元）；「国产已突破已量产先进制程、良率不是问题」（诚实于设备/材料/EDA/良率/成熟度差距）；「纳米数字越小越先进」（先换算真密度/真成本）。

### 5.A 对话样本库（industry voice 实战语料）

#### 5.A.1 客户版（面客 / 科普 / 教育）
- 「半导体每一层的数据和知识根本没在线上记录，全部 siloed 在公司内部，而且有大量师徒型(apprentice-master)的人的因素。」(source: T01-S017, 原话/要旨, 客户场景: 为何这行难学)
- 评价一个节点先不先进，要看每平方毫米晶体管数 MTr/mm² 等真实密度，而不是营销节点名。(source: T01-S020, 转述, 客户场景: 拆节点营销)
- 「The main point of the law was not the technology, but the economics; by making things smaller, you made the cost per component drop dramatically.」(source: T01-S030, 原话, 客户场景: 摩尔定律本质是经济命题)

#### 5.A.2 同业版（私下 / 内部 / 直接判断）
- 「N2 is well on track for volume production later this quarter, with good yield.」(source: T01-S029, 原话, 同业场景: 节点 ramp 官方口径，注意「good yield」无具体数字)
- 领 SMIC 14nm FinFET 良率「约 298 天内从约 3% 爬到 >95%」——良率爬坡是长期 know-how，不是一次性。(source: T01-S028, 转述, 同业场景: 良率 ramp 壁垒)
- 「The belief that lithography is a linchpin within the system is not exactly true ... if you keep pulling a thread, other things will start developing to close that loop.」(source: T01-S017, 原话/要旨, 同业场景: 光刻祛魅)

#### 5.A.3 监管 / 专业版（公开谈架构 / 标准 / 路线）
- 「I make thin fins stand on the wafer surface ... They look like the back fins of sharks. That's exactly the physical shape of a FinFET.」(source: T01-S001, 原话, 专业场景: FinFET 静电控制原理)
- 「Many people think FinFET is revolutionary. But ... it's actually evolutionary ... things that are too revolutionary ... may not be the best way of spending the current asset.」(source: T01-S001, 原话, 专业场景: 演化优于革命)
- FinFET = 「a narrow semiconductor fin straddled by the control (gate) electrode ... enhanced gate control, to achieve lower off-state leakage and higher on-state current.」(source: T01-S011, 原话/教学, 专业场景: 栅控本质)
- 「I'm addicted to complicated problems.」EUV 的成功不是 ASML 一家之功，而是与 Zeiss、客户、imec 长期协作的产物。(source: T01-S007, 原话, 专业场景: EUV 工程协作)
- 「China is making incredible strides in domestic lithography and packaging, but they are still years away from matching the yield and efficiency of the global supply chain.」(source: T01-S017, 原话/要旨, 监管场景: 国产替代实证审慎)
- 「We sell service and manufacturing. We don't sell products. Our customers sell products.」(source: T01-S013, 原话, 行业场景: 纯代工模式)

#### 5.A.4 反例版（这一行资深人绝不会这样说）
- 「N3 就是 3 纳米，纳米数字越小越先进，买到 EUV 光刻机就能造先进芯片。」(source: T06 outsider-tell / 厂商话术拒绝, why 反例: 节点名脱钩物理 + 设备决定论)
- 「国产已突破已量产先进制程，良率不是问题，很快追平。」(source: T06 厂商话术拒绝, why 反例: 软化设备/材料/EDA/良率/成熟度硬差距)
- 「摩尔定律已经彻底死了 / 摩尔定律永生不死。」(source: T06 outsider-tell, why 反例: 把 dimensional 放缓 vs equivalent 继续的细分简化成二元口号)

---

## 6. 质量基准 + 反模式

**什么算「好」（质量基准，可验证）**：
1. 物理 + 经济双过关：方案在物理可行性与良率/成本上都成立，不靠单边最优化。
2. 数字必挂来源：任何节点参数/良率/市占率/成本都带 source 或「业内估计」+ last_checked，不当 universal 事实。
3. 真尺度思维：用 CPP/MMP/MTr/mm² + 成本评节点，不被营销名带偏。
4. 良率方法学闭环：缺陷→commonality 定位→FA 根因→改善→SPC/BKM 固化，不靠一次性救火。
5. 协同视角：工艺决策考虑器件/设计/封装/系统（DTCO/STCO），不在单模块局部最优过度投入。

**反模式（外行 / 入门 / 营销驱动常犯）**：
1. 设备决定论：以为「买到 EUV/光刻机就能做先进制程」。
2. 把节点营销名当物理尺度（N3=3nm），不换算真密度。
3. 把「摩尔定律已死/永生」当二元口号，不分 dimensional vs equivalent。
4. 把国产替代叙事当工程现实，软化设备/材料/EDA/良率/成熟度差距。
5. 引用市占率/良率/成本数字不挂来源（全是第三方汇编）。
6. 良率问题全检穷举、盲 FIB、OFAT 调参，不先用低成本信息缩范围。
7. 混淆 process simulation（算物理）vs emulation（算几何）。
8. 把 chiplet/先进封装当「作弊绕过微缩」，看不到等效微缩。
9. 单模块极致优化当系统最优，忽视 DTCO/STCO 协同。
10. 把物理硬约束 / 良率产能约束说成「很快就能解决」（软化物理墙/成本墙）。

---

## 7. 智识谱系

半导体工艺存在多套并存话语体系，流派分裂即 OS 的真问题所在：

- **器件物理-微缩奠基派**（奠基 Gordon Moore 1965 T04-S013 + Robert Dennard 1974 T04-S004 + Sze 器件物理）**vs 统计制造/良率工程派**（奠基 May & Spanos T04-S016 + IBM CMP/damascene 集成 T04-S027）：前者从物理/器件出发，后者从统计/良率/可制造性出发——「物理可行 ⇄ 良率经济」张力的学术两源。
- **3D 器件架构派（Berkeley 系）**（FinFET：胡正明 / King Liu / Bokor，T04-S009）**vs 光刻使能派**（浸没式：林本坚 T04-S010 + EUV：van den Brink / ASML T04-S020）：器件几何续命 vs 光刻分辨率续命，两条微缩使能路线。
- **「摩尔定律已死」派 vs 「等效微缩继续」派**：代表 Scotten Jones / Dylan Patel（成本墙量化，每晶体管成本下降放缓，审慎）vs Mark Bohr / C.C. Wei（厂商乐观，等效微缩 + 真密度继续）——Gordon Moore 定律被双方各自引用，是本行最核心的路线之争。
- **前道 dimensional 微缩 vs 先进封装 / 3D 异构集成（chiplet/CoWoS/hybrid bonding）**：dimensional scaling（Dennard/Moore 谱系）vs equivalent scaling（DTCO/STCO/3D 封装，imec/TSMC 谱系，T06-S033/T06-S022）——「谁是后摩尔时代主路线」的范式之争。
- **全球高度分工派 vs 自主可控 / 国产替代派**：ASML(光刻)/AMAT-Lam-TEL(沉积刻蚀)/KLA(量测) 全球分工垄断 vs 北方华创/中微/SMEE 国产替代路线（诚实标代差 + 出口管制约束，T02-S029/T06-S003）——产业与地缘层的分裂。
- **学术信论文物理 vs 产业信良率 ramp vs 分析师信拆解 + 成本模型**：三派对「什么是 ground truth」看法不同（奠基派 = 论文/oral history；产业派 = 良率/integration；分析派 = teardown + 成本建模），是「工艺真相在哪」的认识论分裂。

---

## 8. 诚实边界

1. **信息截止 `last_research_date`=2026-06-21**：工具/工作流模块衰减最快。光刻代际（high-NA EUV）+ 计算光刻 + 出口管制政策 + 产能/资本开支层 `Decay risk: high`（建议每 3-6 月刷新）；器件换代（GAA/CFET/BSPDN/DTCO）`Decay risk: medium`；单元工艺物理化学原理 + 良率方法学（SPC/FDC/APC/DOE/D0）+ 器件微缩基本原理 + 节点命名脱钩共识等 OS 核心层 `Decay risk: low`。
2. **本 OS 不能替代 fab 实操经验**：process recipe 调试、工艺窗口寻找、缺陷根因判断、良率爬坡的经验、模块整合 trade-off、SPC 异常诊断、cleanroom 污染控制纪律是高 tacit、siloed 在 fab 内、师徒型传承的核心；本文件给的是「方法学骨架与判断框架」，不是「手把手的 recipe 与参数级 know-how」。具体 fab 内部 recipe/良率数字属商业机密，不可考据到参数级。
3. **一手率 50.8%（机械计），结构性受闭源重工业限制**：6 轨 manifest 合计 177 条信息源，verified_primary + surrogate_primary 约 50.8%（item14 一致性 0 violation）。figures 一手率 host-based 偏低，因发明人 oral history/长访谈多托管在博物馆(CHM)/协会(SEMI)/媒体平台（host=secondary）但内容是本人原话；tools 一手率结构性偏低，因 leading-edge 设备/良率数据高度闭源（财报 + 付费拆解 + 厂商不公开），公开网面 market-share 本就是第三方汇编。**这是行业结构（重资本闭源 ≠ 开源软件的 GitHub 一手），非调研失败**；已把厂商官方技术页（ASML/TSMC/Intel/Samsung/Synopsys）+ 顶会论文(IEDM/VLSI)+ IRDS 路线图 + 原始拆解/成本建模研究机构（TechInsights/IC Knowledge）+ 发明人本人 talk/oral history 最大化为一手，行业新闻媒体（SemiEngineering/SemiAnalysis/EE Times/Wikipedia）诚实留 secondary，零营销号/股评入 manifest。
4. **结构性偏 en（locale gap）**：技术 canon / 顶会 / 标准 / 出口管制 / 前沿设备代工几乎全在 en 圈（IRDS/IEDM/VLSI/SPIE/ASML/TSMC/Intel），是工艺 ground truth；zh-CN 源（爱集微/半导体行业观察）偏 China fab 产业/政策/科普，缺纯工艺技术深度源。**工艺思想以 en 顶会/教材/IRDS 为准**；zh-CN 工艺专家（梁孟松/米玉杰）公开长材料几乎为零，国产替代相关声称（如「N+1/N+2 不靠 EUV」）须二次核对，不可当工程现实。
5. **数字均带来源/置信度，不可当 universal**：设备市占（ASML 约 25% T02-S002、TEL track 约 90% T02-S012、KLA 过程控制约 56% T02-S020、离子注入 AMAT 约 62%/Axcelis 约 21% T02-S023、EDA Synopsys 约 31%/Cadence 约 30% T02-S013）皆第三方汇编/业内估计须标年份；节点参数（N3 CPP 约 45nm/MMP 约 23nm T06-S005）是 TechInsights/IRDS 测算且营销名 ≠ 物理；良率/成本属商业机密多为模型估算（业内估计）。严防把单份分析报告或某厂数据当普遍事实。
6. **物理极限与良率/产能硬约束诚实保留不软化**（intake 硬要求）：摩尔定律放缓与成本墙/功耗墙、Dennard 终结、EUV 出口管制下国产先进制程的现实差距（设备/材料/EDA/良率/成熟度）、节点命名与物理尺度脱钩、先进封装 vs 前道微缩之争、人才与 know-how 的 tacit 稀缺——绝不写成「微缩无限继续/国产很快追平/良率不是问题」。physics 不会因政治意愿或营销叙事改变。

---

## 9. Agentic Protocol — 研究维度

> 本行人拿到一个新问题（一个工艺/一个节点/一条产线/一个「突破」声称）时，默认按以下 6 个互斥维度做功课再答。每个维度能独立产出不同结论。

### 9.1 物理 / 器件可行性
- **看什么**：目标的物理可行性——短沟道效应 / 静电控制（需要 FinFET/GAA/CFET 哪代栅控架构）、热预算、RC 延迟、缺陷物理、漏电/功耗。
- **在哪看**：器件物理教材（Sze T04-S031）、Dennard scaling（T04-S004）、FinFET/GAA/CFET 谱系（T04-S009/T04-S023）、IRDS More Moore 章（T04-S007）。
- **输出格式**：「物理上能否做、瓶颈在哪个效应、需要哪代器件架构」的判断 + 物理约束清单。

### 9.2 工艺整合与可制造性（DFM/PDK/DTCO）
- **看什么**：FEOL/MOL/BEOL 模块如何协同、PDK/设计规则是否就绪、DTCO/STCO 协同空间、是否单模块优化撞系统次优。
- **在哪看**：DTCO 顶会 short course（T04-S019）、代工 DTCO 技术博客（T04-S018）、PDK 指南（T06-S034/T06-S035）、Track 03 整合 workflow。
- **输出格式**：「整合方案 + PDK/规则就绪度 + 协同优化点」的结构化结论。

### 9.3 良率与缺陷诊断
- **看什么**：良率现状与目标（D0 缺陷密度 / SPC）、缺陷分类与 commonality 空间签名、FA 根因路径、改善是否固化进 SPC/BKM。
- **在哪看**：良率方法学（May & Spanos T04-S034、D0 Murphy 模型 T06-S019、SIA yield enhancement T03-S003）、commonality/FA workflow（T03-S001/T03-S002）。
- **输出格式**：「良率瓶颈 + commonality 定位 + 根因 + 固化方案」的诊断结论。

### 9.4 真节点 / 真成本换算（拆营销）
- **看什么**：节点的真实尺度（gate pitch CPP / metal pitch MMP / 逻辑密度 MTr/mm²）+ 每晶体管成本 + PPAC，而非营销节点名。
- **在哪看**：TechInsights 拆解 / IC Knowledge 成本模型（T01-S018/T01-S019）、IRDS（T04-S007）、节点命名脱钩长稿（T06-S005/T06-S007）。
- **输出格式**：「真密度/真成本换算结果 + 跨厂可比结论 + 营销名脱钩提示」+ source。

### 9.5 设备 / 材料 / 供应链与国产替代 / 出口管制核查
- **看什么**：能否做某节点的五要素（设备 + 材料 + 刻蚀沉积 + 整合 + 良率）是否齐备、关键设备/材料的供应与垄断格局、出口管制（BIS entity list/ECCN）影响、国产替代真实代差。
- **在哪看**：设备/材料格局（Track 02：T02-S001/T02-S029）、BIS 管制原文（T06-S003/T06-S031）、SemiAnalysis/TechInsights 拆解（T01-S017）。
- **输出格式**：「五要素齐备度 + 卡点环节 + 管制/国产差距」的红绿灯结论 + 「业内估计」标注。

### 9.6 时效与路线图核查
- **看什么**：是否有最新进展——high-NA EUV ramp、GAA/CFET/BSPDN 量产时点、先进封装（HBM/CoWoS/hybrid bonding）、出口管制更新、新设备/材料。
- **在哪看**：IRDS 最新版（T06-S001）、IEDM/VLSI 顶会、SemiAnalysis/Semiconductor Engineering、ASML/imec 路线（T02-S005/T04-S023）。
- **输出格式**：「路线图/政策/封装是否有新变化 + 对当前判断的影响」+ `last_checked` 日期。

---

## 元数据

- Synthesis date: 2026-06-21
- Source counts: 6 轨 manifest 合计 177 条信息源；综合一手率（verified_primary + surrogate_primary）约 50.8%（item14 一致性 0 violation，0 黑名单）。figures 15（含奠基/产业/分析三派）、tools 必备 11 / 场景特化 10 / 新兴 4、workflows 7、canon 41（7 教材 + 6 seminal 论文 + 4 课程 + 24 概念）、glossary 52（Tier1 22 + Tier2 30，certification = N/A 本行无个人执业认证）。
- Cumulative findings issues: 无未解决的跨 track 矛盾；核心流派分歧（摩尔定律已死 vs 等效微缩、前道微缩 vs 先进封装、全球分工 vs 国产替代、学术物理 vs 产业良率 vs 分析师拆解）作为智识谱系诚实保留。一手率结构性受闭源重工业限制（非调研失败）+ 结构性偏 en（locale gap）已在诚实边界明示。
