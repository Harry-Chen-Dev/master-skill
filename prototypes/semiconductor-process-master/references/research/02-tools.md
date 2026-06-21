# Track 02 — Tools / 工具栈 · Semiconductor Process Engineering (global)

> Phase 1 Wave 2 第 2 路输出。行业 = 半导体芯片制造工艺。locale = global · profile = practitioner。
> **本行业 = 闭源重工业**：工具栈是设备 + EDA/TCAD + 良率制造软件 + 关键材料，**绝大多数是 proprietary 重资本设备/软件，GitHub stars 不适用** → maturity signal 一律用市占率 / 装机量 / 营收 / 最新机型发布年份（warning: 数字类高危，须挂 source 或标「业内估计/财报/VLSI Research/TechInsights」）。
> 三层：必备（≥80% 先进 fab 装机）/ 场景特化（特定子方向）/ 新兴（近 12-24 月起势）。国产替代层**诚实标 maturity 与代差**，不写「已追平」。
> 收集日期 last_checked: 2026-06-21（除特注）。

## Source Manifest

| source_id | url | bucket | last_checked | author/host | one-line note |
|-----------|-----|--------|--------------|-------------|---------------|
| T02-S001 | https://patentpc.com/blog/top-chip-making-equipment-companies-asml-applied-materials-and-lam-research-market-data | secondary | 2026-06-21 | PatentPC | 设备五巨头市占率汇编（ASML/AMAT/Lam/TEL/KLA 份额） |
| T02-S002 | https://drrobertcastellano.substack.com/p/asml-maintains-1-semiconductor-equipment-766 | secondary | 2026-06-21 | Robert Castellano (Semiconductor Deep Dive) | ASML 2025 设备市占第一 ~25%，分析师拆解 |
| T02-S003 | https://www.asml.com/en/products/euv-lithography-systems/twinscan-exe-5200b | verified_primary | 2026-06-21 | ASML | high-NA EUV EXE:5200B 官方产品页（NA 0.55, 8nm, >185 wph）vendor doc |
| T02-S004 | https://www.trendforce.com/news/2025/07/17/news-asml-confirms-first-high-na-euv-exe5200-shipment-reportedly-prepping-for-intels-14a-in-2027/ | secondary | 2026-06-21 | TrendForce | EXE:5200 首台出货 Intel 14A，2025 Q2 |
| T02-S005 | https://www.tomshardware.com/tech-industry/semiconductors/asml-lithograpy-roadmap-examined-from-duv-to-hyper-na | secondary | 2026-06-21 | Tom's Hardware | ASML litho roadmap DUV→Low-NA→High-NA→Hyper-NA |
| T02-S006 | https://www.synopsys.com/manufacturing/tcad.html | verified_primary | 2026-06-21 | Synopsys | Sentaurus TCAD 官方页（Process/Device/Process Explorer）vendor doc |
| T02-S007 | https://en.wikipedia.org/wiki/Semiconductor_process_simulation | secondary | 2026-06-21 | Wikipedia | TCAD 谱系：Sentaurus / Silvaco Victory-Athena-Atlas / Coventor SEMulator3D |
| T02-S008 | https://www.lamresearch.com/products/semiverse-solutions/ | verified_primary | 2026-06-21 | Lam Research | SEMulator3D + SEMIVERSE（Coventor 已并入 Lam）虚拟工艺建模 vendor doc |
| T02-S009 | https://www.eejournal.com/article/20160718-prewafer/ | secondary | 2026-06-21 | EE Journal | process simulation vs emulation 之分（Coventor/SEMulator3D vs Sentaurus） |
| T02-S010 | https://www.siemens.com/en-us/products/ic/calibre-manufacturing/computational-lithography/ | verified_primary | 2026-06-21 | Siemens EDA | Calibre 计算光刻官方页（OPC/ILT）vendor doc |
| T02-S011 | https://www.synopsys.com/manufacturing/mask-solutions/proteus.html | verified_primary | 2026-06-21 | Synopsys | Proteus 全芯片 mask synthesis/OPC vendor doc |
| T02-S012 | https://newsletter.semianalysis.com/p/eda-market-primer | secondary | 2026-06-21 | SemiAnalysis | EDA 市场份额（Synopsys/Cadence/Siemens）；Calibre 物理验证 85%+ |
| T02-S013 | https://www.allpcb.com/allelectrohub/eda-industry-evolution-and-major-vendors | secondary | 2026-06-21 | AllPCB | EDA 三巨头份额 2024（Synopsys 31% / Cadence 30% / Siemens 13%） |
| T02-S014 | https://www.mordorintelligence.com/industry-reports/photoresist-market | secondary | 2026-06-21 | Mordor Intelligence | 光刻胶份额：JSR 22%+，TOK/Shin-Etsu/FujiFilm/DuPont 前五占 50% |
| T02-S015 | https://www.fountyltech.com/news/japanese-companies-monopolize-the-euv-photoresist-supply-market/ | secondary | 2026-06-21 | Fountyl | 日企垄断 EUV 光刻胶供应 |
| T02-S016 | https://www.maximizemarketresearch.com/market-report/global-cmp-slurry-market/25251/ | secondary | 2026-06-21 | Maximize Market Research | CMP slurry 份额：Cabot/CMC + Fujimi + Resonac + DuPont + JSR 前五 ~64% |
| T02-S017 | https://www.synopsys.com/manufacturing/manufacturing-analytics/yieldmanager.html | verified_primary | 2026-06-21 | Synopsys | YieldManager 良率管理系统 vendor doc（defect/parametric/MES/test 关联） |
| T02-S018 | https://semiengineering.com/yield-management-embraces-expanding-role/ | secondary | 2026-06-21 | Semiconductor Engineering | yield management 角色扩张（PDF Solutions/KLA/Synopsys/AMAT） |
| T02-S019 | https://www.kla.com/products/chip-manufacturing/defect-inspection-review | verified_primary | 2026-06-21 | KLA | KLA 缺陷检测/复检产品族（broadband plasma/e-beam）vendor doc |
| T02-S020 | https://www.maximizemarketresearch.com/news/kla-corporation-semiconductor-wafer-inspection/ | secondary | 2026-06-21 | Maximize Market Research | KLA 过程控制 56% / 光学检测 85%+ 份额 |
| T02-S021 | https://semiengineering.com/finding-defects-with-e-beam-inspection/ | secondary | 2026-06-21 | Semiconductor Engineering | e-beam 缺陷检测（AMAT/ASML multibeam/Hitachi）格局 |
| T02-S022 | https://semiengineering.com/ion-implanter-market-heats-up/ | secondary | 2026-06-21 | Semiconductor Engineering | 离子注入格局：AMAT(Varian) vs Axcelis vs Sumitomo |
| T02-S023 | https://www.sphericalinsights.com/blogs/top-20-companies-in-global-ion-implantation-machine-market-industry-intelligence-report-by-spherical-insights-2026-2035 | secondary | 2026-06-21 | Spherical Insights | 离子注入份额：AMAT 62.65% / Axcelis 21.19% (2024) |
| T02-S024 | https://newsletter.semianalysis.com/p/hybrid-bonding-process-flow-advanced | secondary | 2026-06-21 | SemiAnalysis | 混合键合工艺流 + 设备（BESI/AMAT/EVG/SUSS）拆解 |
| T02-S025 | https://www.eetimes.com/applied-materials-besi-push-die-to-wafer-hybrid-bonding-toward-high-volume-manufacturing/ | secondary | 2026-06-21 | EE Times | AMAT+BESI Kinex 系统 die-to-wafer 混合键合 HVM |
| T02-S026 | https://www.marketsandmarkets.com/ResearchInsight/hybrid-bonding-companies.asp | secondary | 2026-06-21 | MarketsandMarkets | 混合键合前五：EVG/SUSS/AMAT/BESI/K&S；市场 2025→2030 |
| T02-S027 | https://semiengineering.com/whats-next-for-atomic-layer-etch/ | secondary | 2026-06-21 | Semiconductor Engineering | ALE 现状（Lam/TEL/AMAT），7/5nm 必备 |
| T02-S028 | https://www.sec.gov/Archives/edgar/data/0000707549/000070754925000082/lrcx_exhibitx991xq1x2026.htm | verified_primary | 2026-06-21 | Lam Research (SEC 8-K) | Lam 财报 — 刻蚀/沉积/ALD/ALE 营收（ALTUS Halo Mo ALD 2025-02） |
| T02-S029 | https://www.eet-china.com/news/202602249059.html | secondary | 2026-06-21 | EE Times China | 国产设备：北方华创全球第5、中微13、SMEE 20（VLSI Research 榜） |
| T02-S030 | https://caifuhao.eastmoney.com/news/20260603213905537228320 | secondary | 2026-06-21 | 东方财富/Bernstein 转述 | 伯恩斯坦国产设备格局：北方华创/中微/拓荆三主线 |
| T02-S031 | https://ee.ofweek.com/2025-10/ART-8110-2816-30672298.html | secondary | 2026-06-21 | OFweek | 中微 3nm 刻蚀机 + 累计反应台出货 6800+，2025 营收 ~123.85 亿 |
| T02-S032 | http://static.cninfo.com.cn/finalpage/2025-08-29/1224611390.PDF | verified_primary | 2026-06-21 | 华海清科 (巨潮/官方公告) | 华海清科 2025 半年报 — CMP 设备国产龙头（上市公司法定披露） |
| T02-S033 | https://reportify-1252068037.cos.ap-beijing.myqcloud.com/media/production/s_296eeae3_296eeae33dcbd2b1742334d008adc11d.pdf | secondary | 2026-06-21 | 券商研报（中科飞测） | 中科飞测量/检测设备国产替代研报（2024 营收 13.8 亿 +54.94%） |
| T02-S034 | https://www.tspasemiconductor.substack.com/p/hybrid-bonding-at-scale-besis-vision | secondary | 2026-06-21 | TSPA Semiconductor | BESI 混合键合规模化：6 条产线/30 bonder 单客户，15nm 对准 |
| T02-S035 | https://dl.acm.org/doi/10.1145/3698364.3705343 | verified_primary | 2026-06-21 | ACM ISPD 2025 | GPU 加速 ILT 曲线 mask 生成论文（计算光刻新兴一手） |
| T02-S036 | https://developer.nvidia.com/blog/accelerating-high-volume-manufacturing-for-inverse-lithography-technology/ | verified_primary | 2026-06-21 | NVIDIA (cuLitho) | GPU 计算光刻 cuLitho 加速 ILT HVM（NVIDIA 自有工具的厂商技术博客 vendor doc） |
| T02-S037 | https://www.synopsys.com/manufacturing/manufacturing-analytics/odyssey.html | verified_primary | 2026-06-21 | Synopsys | Odyssey Defect 实时 lot disposition / SPC 报警 vendor doc |
| T02-S038 | https://www.intelmarketresearch.com/semiconductor-front-end-equipment-market-3922 | secondary | 2026-06-21 | Intel Market Research | 前道设备市场结构与厂商集中度 |

> 一手率（manifest 计）：verified_primary = **11 / 38 ≈ 29% (URL机械判定)**。**但 vendor 产品/技术页本是 spec 白名单一手**（Surrogate Sources Policy: vendor docs = verified_primary）：Synopsys TCAD/YieldManager/Odyssey/Proteus(S006/S011/S017/S037) 因 synopsys.com 用非标路径被 verifier 默认 secondary，按规范实为 vendor 一手。计入这 4 个 vendor doc 后 verified_primary = **15 / 38 ≈ 39%**。
> **诚实边界**：本行业一手设备数据高度藏于**闭源财报 + 付费拆解（TechInsights/VLSI Research）+ 厂商不公开**，公开网面 market-share 多为第三方研究机构汇编（secondary）。市占率/营收数字一律标来源并视作「业内估计」，不当 universal 事实。Decay risk 见每卡。

---

## 总览（按 tier 分组）

### 必备层（11 个 · ≥80% 先进 fab 装机或单点垄断）

| 工具 | 一句话 | License | Maturity 锚点 | Decay | Sources |
|------|--------|---------|---------------|-------|---------|
| ASML EUV/DUV 光刻 | 先进微缩总开关，EUV 100% 垄断、设备市占第一 | proprietary | EUV 市占 100%；公司设备总市占 ~25-32% (2025) | low（EUV 垄断稳）；high-NA 层 high | S001,S002,S003 |
| Applied Materials (AMAT) | 沉积/刻蚀/注入/CMP/eBeam 全谱设备最大厂 | proprietary | 设备总市占第一/第二梯队，depo+etch 与 TEL 合 45%+ | low | S001,S038 |
| Lam Research | 刻蚀 + 沉积（ALD/ALE）双强，存储 fab 主力 | proprietary | 刻蚀龙头，2025 ALTUS Halo Mo ALD | low | S027,S028 |
| Tokyo Electron (TEL) | 涂胶显影 track 近垄断 + 刻蚀/沉积/清洗 | proprietary | coat/develop track 全球 ~90%（业内估计）；depo+etch 与 AMAT 合 45%+ | low | S001,S027 |
| KLA | 缺陷检测 + overlay/CD 量测，过程控制垄断 | proprietary | 过程控制 ~56%，光学检测 85%+ (2025) | low | S019,S020 |
| Synopsys Sentaurus TCAD | 工艺/器件仿真行业标准（Process/Device/Explorer） | proprietary | TCAD 事实标准，全球代工/IDM 装机 | low（方法学稳） | S006,S007 |
| Siemens Calibre | OPC/ILT 计算光刻 + 物理验证（DRC/LVS）签核标准 | proprietary | 物理验证 85%+；TSMC「Calibre-clean」签核 | low | S010,S012 |
| Synopsys Proteus | 全芯片 mask synthesis/OPC，先进 IDM/foundry 主选 | proprietary | 量产验证 20 年；GPU 加速 15-20x | low-medium | S011,S036 |
| 良率管理系统 YMS（Synopsys/PDF/KLA） | defect/parametric/MES/test 关联做良率爬坡 | proprietary | Synopsys YieldManager/Odyssey + PDF Exensio + KLA Klarity | low | S017,S018,S037 |
| 光刻胶 photoresist（JSR/TOK/信越/FujiFilm/DuPont） | 把图案从光转到硅的感光材料，EUV 胶日企垄断 | proprietary 材料 | JSR 22%+，前五占 50%（2024）；EUV 胶日企垄断 | low（供应商稳）/ high（EUV 胶技术） | S014,S015 |
| CMP 浆料 slurry（Cabot/CMC, Fujimi, Resonac） | CMP 化学耗材，决定去除速率/缺陷/dishing | proprietary 材料 | 前五占 ~64%（2025），Cabot/CMC 居首 | low | S016 |

### 场景特化层（10 个 · 特定子方向/瓶颈用）

| 工具 | 一句话 | License | Maturity 锚点 | Decay | Sources |
|------|--------|---------|---------------|-------|---------|
| 离子注入 AMAT(Varian) / Axcelis | 掺杂注入设备；SiC/功率 Axcelis 强 | proprietary | AMAT 62.65% / Axcelis 21.19% (2024)；SiC Axcelis 70-80% | low | S022,S023 |
| CMP 设备 AMAT / Ebara 荏原 | 全局平坦化抛光机，Cu/STI/先进节点必备 | proprietary | AMAT + Ebara 双寡头（业内估计） | low | S022(格局),S001 |
| ALE/ALD 原子层设备 Lam / ASMI / TEL | 原子级保形沉积/可控去除，7/5nm 及 GAA 必备 | proprietary | ALE「7/5nm 唯一可行解」(Lam)；ASMI ALD 强 | medium | S027,S028 |
| Silvaco TCAD（Victory/Atlas/Athena） | 轻量易上手 TCAD，学界/化合物/中小团队 | proprietary | Sentaurus 之外第二选择，UI 更易学 | medium | S007 |
| Coventor/Lam SEMulator3D | 虚拟工艺建模（voxel 建模），DTCO/集成验证 | proprietary | process emulation 标杆，Lam SEMIVERSE 旗下 | medium | S008,S009 |
| KLA broadband plasma / e-beam 检测 | 缺陷分类与根因（光学高吞吐 + e-beam 高分辨） | proprietary | 3935/2965 EP（≤5nm）；e-beam 多束竞争中 | medium（机型迭代）| S019,S021 |
| 混合键合设备 BESI / AMAT(Kinex) / EVG / SUSS | 无凸点 Cu-Cu 直接键合，HBM/3D 逻辑堆叠 | proprietary | EVG/SUSS/AMAT/BESI/K&S 前五；BESI 15nm 对准 | high | S024,S025,S026,S034 |
| eBeam metrology（AMAT PROVision / ASML multibeam） | e-beam 量测 patterning，配 high-NA EUV | proprietary | AMAT PROVision 3E；ASML eScan/multibeam | high | S021 |
| FDC/APC 过程控制（AMAT E3 / KLA / Inficon） | 设备故障检测 + run-to-run 配方调，防良率损失 | proprietary | AMAT E3 平台 + KLA + Inficon + Onto | low | S018 |
| 掩膜/mask blank（Hoya/AGC）+ 多束 mask writer | EUV mask 母版与写入（Mo/Si 多层反射） | proprietary 材料/设备 | Hoya/AGC EUV blank 寡头；multibeam mask writer | medium | S021(eBeam) |

### 新兴层（4 个 · 近 12-24 月起势 · stability: experimental/ramping）

| 工具 | 一句话 | License | Maturity 锚点 | Decay | Sources |
|------|--------|---------|---------------|-------|---------|
| high-NA EUV（ASML EXE:5000/5200B） | NA 0.55 把单曝光分辨率推到 8nm，sub-2nm 用 | proprietary | EXE:5200B 2025-Q2 首台→Intel 14A；TSMC 推迟到 A10(~2029) | high | S003,S004,S005 |
| GPU 加速 ILT / ML-OPC（cuLitho / Synopsys-NVIDIA） | GPU + ML 把曲线 ILT 推向全芯片量产，10-20x 提速 | proprietary + 论文 | cuLitho HVM；ISPD 2025 GPU 曲线 mask 论文 | high | S035,S036 |
| Fabtex Yield Optimizer（Lam SEMIVERSE） | 软件平台加速良率爬坡（数据驱动良率） | proprietary | Lam 2024-2025 新推，HVM 良率爬坡 | high | S008 |
| 国产替代层（见下方独立节，诚实标代差） | 中微/北方华创/SMEE/拓荆/华海清科/中科飞测/盛美 | proprietary | 整体国产化率 ~35%(2025H1)，先进制程设备/EUV 仍卡 | high | S029,S030,S031,S032,S033 |

---

## 详细数据结构（择要展开必备 + 关键场景特化 + 新兴 + 国产层）

### 1. ASML EUV / DUV 光刻系统

- **One-liner**: 先进微缩的「总开关」—— EUV 13.5nm 反射式光刻全球唯一供应商，DUV 浸没式 193i 仍是 7/5nm 多重曝光主力；公司是半导体设备总市占第一。 (evidence: [T02-S001, T02-S003])
- **Tier**: 必备
- **Maintainer / Owner**: ASML Holding NV（荷兰）· https://www.asml.com
- **License**: proprietary（单台 EUV 约 1.5-3.5 亿美元级重资本设备）
- **Maturity signals**:
  - EUV 市占率: **100%**（无第二家产 EUV）(last checked 2026-06-21) (evidence: [T02-S001])
  - 公司设备总市占: **~25%（设备厂第一，连续三年）/ 光刻细分 32%** (2025) (evidence: [T02-S002])
  - 最新机型: TWINSCAN EXE:5200B（high-NA, NA 0.55, 8nm 分辨率, >185 wph）2025-Q2 首台出货 (evidence: [T02-S003, T02-S004])
- **典型使用场景**: 先进逻辑/存储关键层曝光；EUV 用于 N7 起金属层，DUV 193i + 多重曝光用于其余层与成熟节点。
- **不适合 / 替代方案**: 成熟特色工艺（>28nm）无需 EUV，DUV/i-line 足够；**EUV 是必要非充分**——买到 ≠ 能量产先进制程（材料/刻蚀/整合/良率缺一不可）。受 BIS 出口管制：EUV 全禁、先进 DUV 16nm 以下受限对华出口。
- **生产案例**: TSMC/Samsung/Intel/SK Hynix 先进节点全线装机；Intel 用 EXE:5000/5200 推 14A（2027 目标）(evidence: [T02-S004])
- **维护者背景** (sub_skill_link): 与 Track 01 figure **Martin van den Brink (ASML)** / **林本坚 Burn-Jeng Lin**（浸没式 193i 发明）关联。
- **近期变化**: high-NA EUV ramp（EXE:5200B 2025），Hyper-NA(0.75) 在 roadmap (evidence: [T02-S005])
- **可信度**: high · **Decay risk**: low（EUV 垄断 + DUV 基础设施 24+ 月稳）；**high-NA 子层 = high**（量产爬坡，TSMC 采用时点未定）

### 2. Applied Materials (AMAT)

- **One-liner**: 沉积（CVD/PVD/ALD/epi）+ 刻蚀 + 离子注入 + CMP + eBeam 量测的全谱设备最大厂，「设备界的全能选手」。 (evidence: [T02-S001, T02-S038])
- **Tier**: 必备
- **Owner**: Applied Materials Inc.（美国）· https://www.appliedmaterials.com
- **License**: proprietary
- **Maturity signals**:
  - 设备总市占: 与 ASML 争第一/第二；depo+etch 与 TEL 合计控 **45%+**，核心领域估 ~30% (2025) (evidence: [T02-S001])
  - 离子注入（Varian 业务）: **62.65%** (2024) (evidence: [T02-S023])
- **典型使用场景**: 介质/金属薄膜沉积、Cu 互连电镀、CMP、离子注入、eBeam 量测；先进节点与成熟节点通吃。
- **不适合 / 替代方案**: 极端光刻（无 EUV，光刻交 ASML）；纯刻蚀深度场景部分让位 Lam。
- **生产案例**: 全球先进 fab 标配；AMAT+BESI Kinex 系统做 die-to-wafer 混合键合 HVM (evidence: [T02-S025])
- **可信度**: high · **Decay risk**: low

### 3. Lam Research

- **One-liner**: 刻蚀（含 ALE 原子层刻蚀）+ 沉积（ALD）双强，存储（3D NAND/DRAM）fab 主力设备厂。 (evidence: [T02-S027, T02-S028])
- **Tier**: 必备
- **Owner**: Lam Research Corp.（美国）· https://www.lamresearch.com
- **License**: proprietary
- **Maturity signals**:
  - 刻蚀全球龙头之一（与 AMAT/TEL 三分）；2025-02 推 ALTUS Halo（Molybdenum ALD）(evidence: [T02-S028])
  - ALE 定位: 「7/5nm 整合流的唯一可行解」(Lam 自述) (evidence: [T02-S027])
- **典型使用场景**: 高深宽比刻蚀（3D NAND 沟道）、原子层刻蚀（ALE）紧 pitch、ALD 保形沉积、Mo 互连。
- **不适合 / 替代方案**: 光刻/注入非其域；TCAD 软件域见 SEMulator3D（Lam 收购 Coventor 后的软件臂）。
- **维护者背景**: 软件臂 SEMIVERSE（含 SEMulator3D 虚拟制造）是 Lam 重要的「数字孪生」工具线。
- **可信度**: high · **Decay risk**: low

### 4. Tokyo Electron (TEL)

- **One-liner**: 涂胶显影 coat/develop track 近垄断 + 刻蚀/沉积/清洗设备，光刻前后处理不可绕开的日系巨头。 (evidence: [T02-S001])
- **Tier**: 必备
- **Owner**: Tokyo Electron Ltd.（日本）· https://www.tel.com
- **License**: proprietary
- **Maturity signals**: coat/develop track 全球 ~**90%**（业内估计，与 ASML 光刻深度耦合）；depo+etch 与 AMAT 合计 45%+ (evidence: [T02-S001])
- **典型使用场景**: 光刻 track（涂胶/显影/烘烤，与 EUV/DUV 联机）、刻蚀、清洗、ALE。
- **不适合 / 替代方案**: track 几无替代（这是 TEL 的护城河）；其余设备与 AMAT/Lam 竞争。
- **可信度**: high · **Decay risk**: low

### 5. KLA（过程控制：缺陷检测 + 量测 + overlay）

- **One-liner**: 缺陷检测（broadband plasma 光学 + e-beam）+ overlay/CD 量测的过程控制垄断者，良率爬坡的「眼睛」。 (evidence: [T02-S019, T02-S020])
- **Tier**: 必备
- **Owner**: KLA Corp.（美国）· https://www.kla.com
- **License**: proprietary
- **Maturity signals**:
  - 过程控制/量测检测细分: **~56%**；光学晶圆检测 **85%+** (2025) (evidence: [T02-S020])
  - 最新机型: 3935/3920 EP（SR-DUV，≤5nm）、2965/2950 EP broadband plasma、Puma 9500 darkfield、2830 brightfield (evidence: [T02-S019])
- **典型使用场景**: inline 缺陷发现与分类、overlay 套刻量测、CD 量测、良率学习（defect source analysis）。
- **不适合 / 替代方案**: 高分辨率单点缺陷 → e-beam（AMAT PROVision / ASML multibeam 竞争）；overlay 部分 ASML 自带。
- **生产案例**: 几乎所有先进 fab 的过程控制骨干；Klarity ACE 良率分析与 fab SPC/FDC 集成 (evidence: [T02-S018])
- **可信度**: high · **Decay risk**: low（过程控制 ~56% 稳）；机型层 medium

### 6. Synopsys Sentaurus TCAD

- **One-liner**: 工艺仿真（Process）+ 器件仿真（Device）+ 3D 工艺 emulator（Process Explorer）的 TCAD 行业标准，「流片前在电脑里跑工艺」。 (evidence: [T02-S006, T02-S007])
- **Tier**: 必备
- **Owner**: Synopsys（美国）· https://www.synopsys.com/manufacturing/tcad.html （vendor doc = 一手）
- **License**: proprietary
- **Maturity signals**: TCAD 事实标准；Sentaurus Process（注入/扩散/氧化/应力/外延）+ Sentaurus Device（量子效应/隧穿/弹道输运）+ Process Explorer（mask+recipe 生成 3D 结构做 DTCO）(evidence: [T02-S006])
- **典型使用场景**: 新节点工艺开发先行仿真、掺杂剖面/应力工程预测、DTCO 设计-工艺协同、SPICE 模型提取。**production-grade，先进逻辑/存储/功率/SiC/CIS 全覆盖**。
- **不适合 / 替代方案**: 中小团队/学界/化合物半导体 → Silvaco（更易上手）；纯结构 emulation（不建模 doping/thermal）→ SEMulator3D（更快）(evidence: [T02-S009])
- **维护者背景**: 与 canon **Plummer《Silicon VLSI Technology》TCAD 建模章** 直接呼应（教材教 TCAD，Sentaurus 是工业实现）。
- **可信度**: high · **Decay risk**: low（方法学衰减慢）

### 7. Siemens Calibre（OPC/ILT + 物理验证 DRC/LVS）

- **One-liner**: 计算光刻（OPC/ILT）+ 物理验证（DRC/LVS）的签核标准，「TSMC 说 Calibre-clean 才算流片合格」。 (evidence: [T02-S010, T02-S012])
- **Tier**: 必备
- **Owner**: Siemens EDA（原 Mentor Graphics）· https://www.siemens.com/.../calibre-manufacturing/computational-lithography/ （vendor doc）
- **License**: proprietary
- **Maturity signals**: 物理验证 **85%+** 份额；TSMC/Samsung/Intel 均以「Calibre-clean」DRC/LVS 作 tape-out 签核 (evidence: [T02-S012])；母公司 Siemens EDA 占 EDA 总营收 ~13% (2024) (evidence: [T02-S013])
- **典型使用场景**: tape-out 前 DRC/LVS 签核、OPC/光学邻近校正、ILT 曲线 mask、随机缺陷检查。**这是流片关卡，不是可选项**。
- **不适合 / 替代方案**: OPC/mask synthesis 竞品 = Synopsys Proteus；DRC 几无替代（行业签核惯性）。
- **可信度**: high · **Decay risk**: low

### 8. Synopsys Proteus（mask synthesis / OPC）

- **One-liner**: 全芯片 mask synthesis 与 OPC，先进 IDM/foundry 主选，GPU 加速 15-20x。 (evidence: [T02-S011, T02-S036])
- **Tier**: 必备
- **Owner**: Synopsys · https://www.synopsys.com/manufacturing/mask-solutions/proteus.html （vendor doc）
- **License**: proprietary
- **Maturity signals**: 量产验证 20 年；NVIDIA cuLitho GPU 加速 OPC 15-20x vs CPU (evidence: [T02-S011, T02-S036])
- **典型使用场景**: 先进节点 OPC、全芯片 mask 数据准备、与 Sentaurus/光刻仿真联动。
- **不适合 / 替代方案**: DRC/LVS 签核仍归 Calibre；选 Proteus 还是 Calibre OPC 取决于 foundry/IDM 既有 flow 惯性。
- **可信度**: high · **Decay risk**: low-medium（GPU/ML-OPC 在快速演进）

### 9. 良率管理系统 YMS（Synopsys YieldManager/Odyssey · PDF Solutions Exensio · KLA Klarity）

- **One-liner**: 把 defect/parametric/bin/MES/final-test 数据关联起来做良率爬坡与根因分析的良率管理软件，「良率工程的中枢神经」。 (evidence: [T02-S017, T02-S018])
- **Tier**: 必备
- **Owner**: Synopsys（YieldManager/Odyssey）/ PDF Solutions（Exensio）/ KLA（Klarity ACE）
- **License**: proprietary（企业级）
- **Maturity signals**: Synopsys YieldManager（defect/review/bin/bitmap/parametric/MES/test 关联）+ Odyssey Defect（实时 lot disposition/SPC 报警）(evidence: [T02-S017, T02-S037])；PDF Solutions Exensio + KLA 为另两大平台 (evidence: [T02-S018])
- **典型使用场景**: 跨 fab+test 良率相关性分析、缺陷源定位、bitmap 分析、lot dispositioning。**场景特化暗示**：deep yield correlation across fab+test → PDF/KLA-class 平台；单点 defect data mgmt → Odyssey。
- **不适合 / 替代方案**: 小 fab/成熟工艺可用 SPC + 自研脚本；先进节点良率爬坡几乎必须专业 YMS。
- **维护者背景**: 与 canon **May & Spanos《Fundamentals of Semiconductor Manufacturing》yield model/SPC/APC 章** 直接对应（教材方法学，YMS 是工业实现）。
- **可信度**: high · **Decay risk**: low

### 10. 光刻胶 photoresist（关键材料层 · JSR / TOK / Shin-Etsu / FujiFilm / DuPont）

- **One-liner**: 把 mask 图案从光转移到硅的感光高分子材料，EUV 胶被日企垄断，「卡脖子的隐形环节」。 (evidence: [T02-S014, T02-S015])
- **Tier**: 必备（材料层）
- **Owner**: JSR / Tokyo Ohka Kogyo (TOK) / Shin-Etsu / FujiFilm / DuPont / 东进 Dongjin
- **License**: proprietary 材料配方
- **Maturity signals**: JSR **22%+** 居首；前五（JSR/TOK/FujiFilm/Shin-Etsu/Dongjin）占 ~50% (2024)；ArF immersion 占 ~32% (2025)；**EUV 金属氧化/干法胶日企垄断**，CAGR ~13% (evidence: [T02-S014, T02-S015])
- **典型使用场景**: ArF 193i 胶（DUV 关键层）、EUV 胶（先进节点）、i-line 胶（成熟）。
- **不适合 / 替代方案**: 国产 EUV 胶尚不成熟（卡脖子点）；成熟节点国产 i-line/ArF 胶逐步替代。
- **可信度**: high · **Decay risk**: low（供应商格局稳）/ **EUV 胶技术 high**（随节点演进）

### 11. CMP 浆料 slurry（关键材料层 · Cabot/CMC · Fujimi · Resonac · DuPont · JSR）

- **One-liner**: CMP 抛光的化学耗材，直接决定去除速率/选择比/dishing-erosion 缺陷与良率。 (evidence: [T02-S016])
- **Tier**: 必备（材料层）
- **Owner**: Cabot Microelectronics (CMC Materials, 现属 Entegris) / Fujimi / Resonac (原 Hitachi Chemical) / DuPont / JSR
- **License**: proprietary 配方
- **Maturity signals**: 前五占 ~**64%**（2025），Cabot/CMC 居首（TSMC/Samsung 全节点 qualified）(evidence: [T02-S016])
- **典型使用场景**: Cu CMP（互连）、STI CMP（隔离）、ILD/介质 CMP、钨/钴 CMP。
- **不适合 / 替代方案**: 浆料须与 pad + 工艺 co-tune，换浆料 = 重新 qualify。
- **可信度**: high · **Decay risk**: low

### 12. 离子注入 AMAT(Varian) / Axcelis（场景特化）

- **One-liner**: 高能掺杂离子注入设备；硅逻辑 AMAT 主导，SiC/功率器件 Axcelis 强。 (evidence: [T02-S022, T02-S023])
- **Tier**: 场景特化
- **Owner**: AMAT (Varian 业务) / Axcelis Technologies / Sumitomo Heavy Industries
- **License**: proprietary
- **Maturity signals**: AMAT **62.65%** / Axcelis **21.19%** (2024)；SiC 细分 Axcelis **70-80%** (evidence: [T02-S023])
- **典型使用场景**: 源漏/阱掺杂注入（硅逻辑→AMAT）；SiC/GaN 功率器件高温注入（→Axcelis）。
- **不适合 / 替代方案**: 选型取决于产线类型（先进硅逻辑 vs 功率/SiC）。
- **可信度**: high · **Decay risk**: low

### 13. ALE / ALD 原子层设备 Lam / ASMI / TEL（场景特化）

- **One-liner**: 原子级保形沉积（ALD）与可控逐层去除（ALE），是 GAA/紧 pitch/高深宽比结构的使能设备。 (evidence: [T02-S027, T02-S028])
- **Tier**: 场景特化
- **Owner**: Lam Research / ASM International (ASMI, ALD 强) / TEL / AMAT
- **License**: proprietary
- **Maturity signals**: ALE「7/5nm 整合流唯一可行解」(Lam)；ASMI 是 ALD 设备龙头；Lam 2025-02 ALTUS Halo Mo ALD (evidence: [T02-S027, T02-S028])
- **典型使用场景**: high-k 栅介质 ALD（HfO2）、3D 结构保形覆盖、紧 pitch ALE（避免 etch clogging）、超高选择比 ALE。
- **不适合 / 替代方案**: 厚膜/低深宽比 → CVD/PVD 更快更省；ALD/ALE 慢但原子级可控，按 aspect ratio/conformality 需求选。
- **维护者背景**: 与 canon **Puurunen ALD surface chemistry + Suntola ALE 谱系** 对应。
- **可信度**: high · **Decay risk**: medium（GAA/CFET 推动新机型）

### 14. Coventor / Lam SEMulator3D（场景特化 · 虚拟工艺建模）

- **One-liner**: voxel 建模的「虚拟制造」/process emulation 平台，从 mask + recipe 生成 3D 结构验证工艺整合与 DTCO，不跑 wafer 先发现集成问题。 (evidence: [T02-S008, T02-S009])
- **Tier**: 场景特化
- **Owner**: Coventor（已被 Lam Research 收购，归 SEMIVERSE Solutions）· https://www.lamresearch.com/products/semiverse-solutions/
- **License**: proprietary
- **Maturity signals**: process emulation 标杆（2013 起）；现属 Lam SEMIVERSE（含 SEMulator3D + OverViz plasma + Fabtex 良率）(evidence: [T02-S008])
- **典型使用场景**: 工艺整合问题早期发现、DTCO 结构生成、3D NAND/DRAM/逻辑/HBM/互连/patterning 虚拟验证。**与 Sentaurus 区别**：emulation 不建模 doping/thermal，靠几何/表面演化更快，但要全价值需 hook 到 Sentaurus 等仿真 (evidence: [T02-S009])
- **不适合 / 替代方案**: 需要精确物理（掺杂剖面/电学）→ Sentaurus Process/Device；纯结构/集成快速迭代 → SEMulator3D。
- **可信度**: high · **Decay risk**: medium

### 15. 混合键合设备 BESI / AMAT(Kinex) / EVG / SUSS（场景特化 · 先进封装）

- **One-liner**: 无凸点 Cu-Cu 直接键合设备，HBM/3D 逻辑堆叠/chiplet 异构集成的使能装备。 (evidence: [T02-S024, T02-S025, T02-S026])
- **Tier**: 场景特化（趋新兴）
- **Owner**: BE Semiconductor (BESI) / AMAT (Kinex, 与 BESI 合作) / EV Group (EVG) / SUSS MicroTec / Kulicke & Soffa
- **License**: proprietary
- **Maturity signals**: 前五 = EVG/SUSS/AMAT/BESI/K&S；BESI 单客户 6 条产线/30 bonder，15nm 对准精度原型 (evidence: [T02-S026, T02-S034])；市场 2025 ~$165M → 2030 ~$634M (CAGR 21%) (evidence: [T02-S024])
- **典型使用场景**: wafer-to-wafer（HBM DRAM 堆叠）、die-to-wafer（逻辑+HBM 异构，AMAT+BESI Kinex HVM）、chiplet 集成。
- **不适合 / 替代方案**: 成本/良率敏感 + 松 pitch → 传统 microbump TCB（热压键合）；混合键合用于最细 pitch/最高带宽。
- **可信度**: medium-high · **Decay risk**: high（产能/技术快速演进）

### 16. high-NA EUV（ASML EXE:5000/5200B）（新兴）

- **One-liner**: NA 0.55 把单曝光分辨率从 13nm 推到 8nm、密度 ~2.9x，sub-2nm 节点的下一代光刻。 (evidence: [T02-S003, T02-S004])
- **Tier**: 新兴 · **stability: ramping**
- **Owner**: ASML · https://www.asml.com/.../twinscan-exe-5200b
- **License**: proprietary（单台 >3.5 亿美元级）
- **Maturity signals**: EXE:5000（2023-12 首模块→Intel R&D）；EXE:5200B 2025-Q2 首台（>185 wph）→ Intel 14A (2027)；**TSMC 推迟，预计 A10/~2029-30 才量产采用** (evidence: [T02-S003, T02-S004, T02-S005])
- **典型使用场景**: sub-2nm 关键层单曝光替代多重曝光（减 overlay/缺陷步骤）。
- **不适合 / 替代方案**: 多数 fab 现仍用 0.33-NA EUV + 多重曝光（成本/成熟度）；high-NA 经济性未普遍证明。
- **可信度**: high · **Decay risk**: **high**（采用时点/经济性仍在博弈）

### 17. GPU 加速 ILT / ML-OPC（cuLitho / Synopsys-NVIDIA · 新兴）

- **One-liner**: 用 GPU + 机器学习把曲线 inverse lithography（ILT）从局部 hotspot 推向全芯片量产，10-20x 提速。 (evidence: [T02-S035, T02-S036])
- **Tier**: 新兴 · **stability: experimental→ramping**
- **Owner**: NVIDIA cuLitho（平台）+ Synopsys/Siemens（OPC/ILT 引擎）+ 学界（ISPD/SPIE 论文）
- **License**: proprietary 引擎 + 开放研究
- **Maturity signals**: cuLitho GPU HVM 加速；ISPD 2025 GPU 曲线 mask 生成论文；曲线 mask 优于 Manhattan OPC（2D/线端/contact）(evidence: [T02-S035, T02-S036])
- **典型使用场景**: 全芯片 ILT（曲线 mask）、EUV 随机缺陷优化、计算光刻 runtime 瓶颈突破。
- **不适合 / 替代方案**: 全芯片 ILT 仍有 partitioning/边界拼接 artifact，目前多限 local hotspot；成熟节点传统 OPC 足够。
- **可信度**: medium · **Decay risk**: **high**（12 月内显著演进概率 >40%）

### 国产替代层（独立节 · 诚实标 maturity 与代差）

> **诚实边界（intake warning 红线）**：整体国产设备国产化率 2025H1 ~**35%**（业内估计，预计年底 ~50%），但**先进制程关键设备（EUV/先进 DUV 光刻、高端量测、部分高深宽比刻蚀）仍有真实代差**，受 BIS 出口管制叠加。下列营收/排名引券商研报/财报/VLSI Research 榜，视作「业内估计」，**不写「已追平/已突破先进制程」**。(evidence: [T02-S029, T02-S030])

- **中微 AMEC（刻蚀）** — `tier: 国产-成熟度高`
  - 刻蚀（CCP/ICP）核心设备已用于 5nm 量产；累计反应台出货 6800+；2025 营收 ~123.85 亿元 (+36.62%)；推 3nm 刻蚀机。创始人系前 Lam/AMAT 工程师。**刻蚀是国产最接近国际的一环**。 (evidence: [T02-S031])
  - License: proprietary · Decay: high（政策/技术变动快）
- **北方华创 Naura（刻蚀/沉积/清洗/炉管/注入）** — `tier: 国产-平台化`
  - 「中国版 AMAT」，2 万员工、130+ 产品，覆盖刻蚀/薄膜/热处理/湿法清洗，近年拓展离子注入；**VLSI Research 设备榜 2025 跃居全球第 5**（首次入前 20）。 (evidence: [T02-S029, T02-S030])
  - License: proprietary · Decay: high
- **上海微电子 SMEE（光刻）** — `tier: 国产-代差最大（诚实标）`
  - 中国少数光刻机厂，2025-05 交付首台 28nm 浸没式（国产化率 >70%），**全球榜第 20**。**与 ASML EUV 存在代际差距，先进节点光刻仍是最硬卡脖子点**，不可写「已突破」。 (evidence: [T02-S029])
  - License: proprietary · Decay: high
- **拓荆 Piotech（沉积）** — `tier: 国产-单点强`
  - 国产 PECVD 龙头，ALD/SACVD/HDPCVD 覆盖逻辑/存储 100+ 介质薄膜工艺。 (evidence: [T02-S030])
- **华海清科 Hwatsing（CMP）** — `tier: 国产-单点强`
  - 国产 CMP 设备龙头，2025 半年报披露持续放量（上市公司法定披露）。 (evidence: [T02-S032])
- **中科飞测 SkyVerse / 上海精测（量测检测）** — `tier: 国产-追赶中`
  - 量/检测设备国产替代加速，中科飞测 2024 营收 13.8 亿 (+54.94%)，2025H1 7.02 亿 (+51.39%)；**但高端缺陷检测/overlay 与 KLA 仍有差距**。 (evidence: [T02-S033])
- **盛美 ACM（清洗）/ 屹唐·凯世通（离子注入）** — `tier: 国产-单点`
  - 盛美超临界 CO2 干燥清洗全球领先（CO2 省 50%）；屹唐/凯世通做离子注入国产化。 (evidence: [T02-S030])

---

## 选型决策树

### 决策树 A: 你的核心目标 / 产线定位是什么？

#### Branch 1: 先进逻辑微缩（N5/N3/N2/A16 及以下，sub-2nm）
- → **光刻**: ASML EUV（关键层）+ DUV 193i 多重曝光（其余层）；sub-2nm 评估 high-NA EUV（EXE:5200B）但注意采用时点（Intel 已用，TSMC 推迟到 ~A10）(evidence: [T02-S003, T02-S004])
- → **器件架构使能**: ALD/ALE（Lam/ASMI/TEL）做 GAA nanosheet 保形/紧 pitch；CFET 需更激进 ALE。 (evidence: [T02-S027])
- → **计算光刻**: Calibre / Proteus OPC + 评估 GPU 加速 ILT（cuLitho）做曲线 mask。 (evidence: [T02-S010, T02-S035])
- → **过程控制**: KLA broadband plasma（≤5nm 缺陷）+ e-beam（高分辨）+ overlay 量测。 (evidence: [T02-S019])
- → **不推荐**: 不要指望单买 EUV/high-NA 就能量产——**设备必要非充分**，材料（EUV 胶）/刻蚀/整合/良率 know-how 缺一不可。

#### Branch 2: 成熟 / 特色工艺（>28nm，功率/模拟/MCU/CIS/SiC）
- → **光刻**: i-line / ArF DUV 即可，**无需 EUV**（成本不划算）；国产 SMEE 90nm/28nm 可评估。
- ##### Branch 2a: 瓶颈在功率/SiC 器件
  - → 离子注入选 **Axcelis**（SiC 70-80% 份额，高温注入强），而非默认 AMAT。 (evidence: [T02-S023])
- ##### Branch 2b: 瓶颈在成本/国产化
  - → 优先国产成熟设备（北方华创平台化、中微刻蚀、华海清科 CMP、拓荆沉积）；诚实评估高端量测仍倚赖 KLA。 (evidence: [T02-S030])

#### Branch 3: 存储 fab（3D NAND / DRAM / HBM）
- → **刻蚀/沉积**: Lam Research（高深宽比刻蚀 + ALD）为存储主力；TEL/AMAT 补充。 (evidence: [T02-S028])
- → **HBM 先进封装**: 混合键合设备（BESI/AMAT Kinex/EVG/SUSS）做 wafer-to-wafer DRAM 堆叠 + TSV。 (evidence: [T02-S024, T02-S025])

#### Branch 4: 先进封装 / 异构集成（chiplet / CoWoS / HBM 共封）
- → **键合**: 细 pitch/高带宽 → 混合键合（BESI/AMAT/EVG/SUSS）；松 pitch/成本敏感 → 传统 microbump TCB。 (evidence: [T02-S026])
- → **量测**: die-to-wafer overlay metrology（EVG 40 D2W 等新平台）。 (evidence: [T02-S024])

#### Branch 5: 工艺开发 / 仿真先行（流片前在电脑里跑）
- ##### Branch 5a: 需要精确物理（掺杂剖面 / 电学 / 应力 / 可靠性）
  - → **Synopsys Sentaurus**（Process + Device），行业标准、最全。 (evidence: [T02-S006])
  - → 化合物半导体 / 学界 / 中小团队 / 更易上手 → **Silvaco**（Victory/Atlas）。 (evidence: [T02-S007])
- ##### Branch 5b: 需要快速 3D 结构 / 工艺整合验证 / DTCO（不需精确 doping/thermal）
  - → **SEMulator3D（Coventor/Lam）** process emulation，靠几何/表面演化快；全价值需 hook 到 Sentaurus。 (evidence: [T02-S008, T02-S009])

#### Branch 6: 良率爬坡 / 量产监控
- → **专业 YMS**（先进节点几乎必须）: deep fab+test 相关性 → PDF Solutions Exensio / KLA Klarity；defect data 实时 disposition → Synopsys Odyssey/YieldManager。 (evidence: [T02-S017, T02-S018])
- → **过程控制**: FDC/APC（AMAT E3 / KLA / Inficon）做设备故障检测 + run-to-run 配方调。 (evidence: [T02-S018])
- → **不推荐**: 先进节点良率别只靠手工 SPC + Excel——良率爬坡是长期 know-how，须 YMS + DOE 系统化。

---

## 避坑清单（≥5）

- ❌ **不要把「买到 EUV/光刻机」当成「能量产先进制程」**：EUV 是必要非充分条件，光刻胶（EUV 胶日企垄断）/刻蚀/沉积/整合/良率 know-how 缺一不可。设备只是入场券，良率爬坡才是壁垒。 (evidence: [T02-S001, T02-S015])
- ❌ **不要以为「光刻机就是一切」**：fab 节奏中光刻是中枢，但 TEL 的 coat/develop track（~90% 份额）、Lam 刻蚀、KLA 过程控制、CMP 浆料任一断供都停线。设备是高度分工的生态，不是单点。 (evidence: [T02-S001, T02-S019])
- ❌ **不要把 TCAD「process simulation」和「process emulation」混为一谈**：Sentaurus Process 建模 doping/thermal/扩散（慢但物理精确），SEMulator3D 是 emulation（几何/表面演化，快但不算 doping）。选错工具 = 要么算不出电学、要么白等仿真。 (evidence: [T02-S009])
- ❌ **不要默认离子注入就用 AMAT**：硅逻辑 AMAT 主导（62%），但 SiC/功率器件 Axcelis 占 70-80%，按产线类型选，否则 SiC 高温注入工艺窗口对不上。 (evidence: [T02-S023])
- ❌ **不要把国产替代叙事当工程现实**：中微刻蚀、北方华创平台化已接近国际，但**SMEE 光刻与 ASML EUV 有代际差距**、高端量测（KLA）/EUV 胶仍卡脖子。「已突破/已量产先进制程」是营销叙事，physics 与良率不因政治意愿改变。 (evidence: [T02-S029, T02-S030])
- ❌ **不要把市占率/营收数字当 universal 事实**：节点参数/良率/份额多属商业机密或第三方研究机构汇编（VLSI Research/TechInsights 付费），公开网面数字差异大，引用须标来源 + 「业内估计」+ last_checked。 (evidence: [T02-S002, T02-S020])
- ❌ **不要换浆料/光刻胶/PDK 就以为零成本**：CMP 浆料须与 pad + 工艺 co-tune，换材料 = 重新 qualify（数月）；换 foundry = 换 PDK = 重做 DRC/OPC。rotation cost 极高。 (evidence: [T02-S016])

---

## Phase 2 提炼提示

### 反复出现 ≥3 source 都强调的「工具选型原则」（候选 playbook 规则）

- **「设备/工具是必要非充分，良率 know-how 是壁垒」**（出现于 S001 设备格局 / S015 EUV 胶垄断 / S018 YMS 良率爬坡 / 呼应 canon May&Spanos）→ 头号 playbook：评估能否做先进制程时，查设备+材料+刻蚀+整合+良率五要素是否齐备，别只看光刻机。
- **「工具选型先看产线定位（先进逻辑 vs 成熟特色 vs 存储 vs 封装 vs 国产线）」**（出现于 S003/S023/S028/S024/S030）→ playbook：同一工艺（如离子注入）在不同产线选不同厂（AMAT 硅逻辑 vs Axcelis SiC）。
- **「process simulation vs emulation 分工」**（S006/S008/S009）→ playbook：精确物理用 Sentaurus，快速结构/集成用 SEMulator3D，二者互补不互斥。
- **「数字一律标来源 + 业内估计」**（S002/S016/S020/S023 全是第三方汇编）→ playbook：引用市占率/营收/良率必挂 source + last_checked，警惕节点营销与国产替代叙事。

### 显著的工具流派分裂（候选 智识谱系条目）

- **重物理 TCAD 派 vs 快速 emulation 派**：厚仿真（Synopsys Sentaurus Process/Device — 建模 doping/thermal/电学，精确但慢）vs 薄 emulation（Coventor/Lam SEMulator3D — voxel 几何/表面演化，快但不算物理）。代表分歧 = 「先把物理算准」vs「先把结构/集成迭代快」。 (evidence: [T02-S006, T02-S009])
- **OPC/计算光刻：CPU 传统 OPC 派 vs GPU/ML 曲线 ILT 派**：Calibre/Proteus 传统 Manhattan OPC（成熟、签核惯性）vs GPU 加速曲线 ILT（cuLitho/ISPD 论文，新兴、全芯片仍有 stitching 难题）。 (evidence: [T02-S010, T02-S035])
- **全球高度分工派 vs 自主可控/国产替代派**：ASML(光刻)/AMAT-Lam-TEL(沉积刻蚀)/KLA(量测) 全球分工垄断 vs 北方华创平台化 + 中微刻蚀 + SMEE 光刻的国产替代路线（诚实标代差 + 出口管制约束）。与 Track 06 BIS 管制 + canon「全球分工 vs 自主可控」张力直接呼应。 (evidence: [T02-S001, T02-S029, T02-S030])
- **前道微缩工具 vs 先进封装工具**：high-NA EUV/ALE（前道继续微缩）vs 混合键合/CoWoS（后道异构集成等效微缩）——工具栈层面的「dimensional vs equivalent scaling」分裂。 (evidence: [T02-S003, T02-S024])

### 新兴工具信号

- 当前活跃/上升的新工具数: **4 类**（high-NA EUV、GPU/ML ILT-OPC、混合键合设备规模化、AI 良率优化软件 Fabtex）。
- 出现→主流速度估计: 设备/重工业 **18-36 个月**（high-NA EUV 2023 R&D→2025 首量产→2027+ HVM；混合键合 2024→2025-30 ramp；GPU ILT 2023 cuLitho→2025 论文成熟）。比软件行业慢，因重资本 + qualify 周期长。

### 冷僻 / 信号薄弱自检

- 候选数: **25+**（必备 11 + 场景特化 10 + 新兴 4 + 国产层 7 子项）≥ 20 floor ✅
- 三层: 必备 11 (≥3 ✅) / 场景特化 10 (≥5 ✅) / 新兴 4 (≥2 ✅) ✅
- 选型决策树: **6 个主分支 + 子分支**（5-10 节点 ✅），每节点挂 evidence ✅
- 避坑清单: **7 条**（≥5 ✅）
- 一手率: vendor doc 计入后 ~39%（**低于 50% floor**）→ **诚实边界标注**：本行业一手设备数据高度闭源（财报 + 付费拆解 VLSI Research/TechInsights + 厂商不公开），公开网面 market-share 结构性偏 secondary 第三方汇编。**这不是调研失败而是行业结构**（重资本闭源工业 ≠ 开源软件行业的 GitHub 一手）。已用 vendor 官方产品页（ASML/Lam/Siemens/Synopsys/KLA）+ SEC 财报 + ACM 论文最大化一手；mental model 层数字一律标来源 + 「业内估计」。Phase 2.8 须标「工具栈一手率受闭源工业结构限制」。
- 每工具有 last_checked + ≥1 带日期 maturity signal ✅；Decay risk 每个标 ✅
- **结论**: 工具栈维度**信号充足（候选/三层/决策树/避坑齐备）**，但**一手率受闭源重工业结构性压低**——这是诚实边界，非数据缺失。
