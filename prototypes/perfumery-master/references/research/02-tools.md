# Track 02 — Tools 工具栈研究：调香师 / 香水 (Perfumery & Fragrance)

> Phase 1 wave 2 / Track 02. locale=global (en+fr-primary), profile=practitioner。
> **冷僻 + 闭源主导**：核心创作 know-how 藏在四大香精公司 (Givaudan / DSM-Firmenich / IFF / Symrise) 内部 + 调香师个人。公开一手稀薄，本文件用 **Surrogate Sources Policy** 堆厚度，严标 `surrogate_primary` 不冒充 `verified_primary`。
> **本行最核心的「工具」不是软件，而是「原料调色板 (the palette) + 方法框架 (Jean Carles 法 / 香风琴) + 嗅觉记忆 (the nose)」**。软件/仪器是辅助层。
> last_checked 统一 = **2026-06-07**。Wave 1 seed：references/research 为空（wave 1 尚未落盘），本轨独立撒网完成；下游 merge 时可回填 seed 交叉引用。

---

## Source Manifest

| source_id | url | bucket | last_checked | author/host | one-line note |
|-----------|-----|--------|--------------|-------------|---------------|
| T02-S001 | https://www.thegoodscentscompany.com/ | surrogate_primary | 2026-06-07 | The Good Scents Company | originator 官方原料数据库 (2972 aromachemicals, CAS/IFRA/odor) |
| T02-S002 | https://www.perfumeryschool.com/tools-and-equipment | surrogate_primary | 2026-06-07 | School of Creative Perfumery | perfumery school — 官方必备工具/设备清单 (scale/blotter/beaker) |
| T02-S003 | https://www.perfumersworld.com/students-raw-materials-training-kit.php | surrogate_primary | 2026-06-07 | PerfumersWorld | supplier 官方训练原料 kit (调色板入门) |
| T02-S004 | https://pellwall.com/ | surrogate_primary | 2026-06-07 | Pell Wall | supplier 官方 (UK/EU 小量 aroma chemicals + naturals) |
| T02-S005 | https://shop.perfumersapprentice.com/ | surrogate_primary | 2026-06-07 | The Perfumer's Apprentice | supplier 官方 (US 小量原料 + 课程 + kit) |
| T02-S006 | https://eng.hekserij.nl/fragrance-materials/ | surrogate_primary | 2026-06-07 | Hekserij (De Hexerij) | supplier 官方 (NL，极小量供应 hobbyist) |
| T02-S007 | https://artandolfaction.com/suppliers/ | secondary | 2026-06-07 | Institute for Art and Olfaction | 第三方策展的全球 supplier 列表 (含 Eden Botanicals 等) |
| T02-S008 | https://www.perfumeworkbench.com/ | surrogate_primary | 2026-06-07 | Perfume Workbench | vendor docs (indie 配方软件，内建 IFRA limit 检测) |
| T02-S009 | https://formulair.app/ | surrogate_primary | 2026-06-07 | Formulair | vendor docs (Apple-native 配方软件，含 IFRA/cost) |
| T02-S010 | https://www.jbparfum.com/ | surrogate_primary | 2026-06-07 | Perfumers Vault (JB Parfum) | vendor docs (开源免费配方软件，import IFRA xls 校验) |
| T02-S011 | https://getperfumelab.com/ | surrogate_primary | 2026-06-07 | PerfumeLab | vendor docs (配方软件，内嵌 IFRA Cat 4/12 limit) |
| T02-S012 | https://www.selerant.com/formula-based-product-lifecycle-management-software/product-formulation/ | surrogate_primary | 2026-06-07 | Selerant / Trace One | vendor docs (企业级 PLM，B2B 香精公司用) |
| T02-S013 | https://www.coptis.com/resources/cosmetic-formulation/ | surrogate_primary | 2026-06-07 | Coptis | vendor docs (cosmetic/fragrance PLM + 法规) |
| T02-S014 | https://www.sciencedirect.com/science/article/abs/pii/S0165993602008075 | secondary | 2026-06-07 | TrAC / Elsevier | GC & GC-MS 在香水分析的核心地位 (学术综述, abstract) |
| T02-S015 | https://onlinelibrary.wiley.com/doi/10.1002/ffj.3564 | secondary | 2026-06-07 | Flavour & Fragrance Journal | perfume deformulation 色谱识别难点 (Truan 2020) |
| T02-S016 | https://www.innovatechlabs.com/newsroom/1145/unraveling-scent-perfume-makers-gcms-analysis/ | secondary | 2026-06-07 | Innovatech Labs | GC/MS + headspace (static/dynamic) 实操说明 |
| T02-S017 | https://www.fragrancesoftheworld.com/FragranceWheel | surrogate_primary | 2026-06-07 | Michael Edwards | originator 官方 Fragrance Wheel + 60k+ 分类数据库 |
| T02-S018 | https://en.wikipedia.org/wiki/Fragrances_of_the_World | secondary | 2026-06-07 | — | Fragrances of the World 沿革/订阅/规模 二手核对 |
| T02-S019 | https://www.fragrantica.com/news/Olfactory-Pyramid-or-Perfumer-s-Nightmare-8810.html | secondary | 2026-06-07 | Fragrantica | 香调金字塔=营销小说 vs 实际气味 (社区一手吐槽) |
| T02-S020 | https://basenotes.com/community/threads/differences-in-fragrance-notes-from-one-database-to-another.461055/ | secondary | 2026-06-07 | Basenotes forum | Basenotes vs Fragrantica note 来源差异 (社区讨论) |
| T02-S021 | https://ifrafragrance.org/initiatives-positions/safe-use-fragrance-science/ifra-standards | surrogate_primary | 2026-06-07 | IFRA | standards body 官方 (51st Amendment, Prohibition/Restriction/Specification, QRA2) |
| T02-S022 | https://eur-lex.europa.eu/legal-content/EN/TXT/PDF/?uri=CELEX:32023R1545 | verified_primary | 2026-06-07 | EU (EUR-Lex) | 立法原文 Reg (EU) 2023/1545 — 致敏原 26→80+，2026-07 截止 |
| T02-S023 | https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9076902/ | verified_primary | 2026-06-07 | NCBI PMC | essential oil 致敏潜力 DPRA 评估 (天然≠无致敏 学术证据) |
| T02-S024 | https://achs.edu/blog/aromatherapy-safety-basics/ | verified_primary | 2026-06-07 | ACHS | .edu 学院发布 — 「天然=安全」是危险 myth (essential oil 安全) |
| T02-S025 | https://theperfumery.com/company/news/ifra-standards-explained-for-essential-oil-and-fragrance-users/ | secondary | 2026-06-07 | The Perfumery | IFRA 对天然/合成一视同仁 (避坑佐证) |
| T02-S026 | https://www.osmo.ai/blog/science-paper-shows-osmo-ai-passes-the-sniff-test | verified_primary | 2026-06-07 | Osmo | Principal Odor Map (GNN) 嗅觉预测 — 厂商一手 blog |
| T02-S027 | https://cloud.google.com/blog/products/ai-machine-learning/how-osmo-is-bringing-ai-to-aromas | verified_primary | 2026-06-07 | Google Cloud | Osmo 数字嗅觉 spun out of Google Research |
| T02-S028 | https://www.perfumerflavorist.com/events/event-coverage/news/21873544/givaudan-artificial-intelligence-the-future-of-fragrance | verified_primary | 2026-06-07 | Perfumer & Flavorist | Givaudan AI(Carto) 行业媒体一手会议报道 |
| T02-S029 | https://perfumerflavorist.com/fragrance/research/Biological-Scent-Design-382261041.html | verified_primary | 2026-06-07 | Perfumer & Flavorist | 生物科技/合成生物造香分子 行业研究 |
| T02-S030 | https://www.givaudan.com/fragrance-beauty/biotechnology | surrogate_primary | 2026-06-07 | Givaudan | vendor docs (发酵法/cultured ingredient 官方) |
| T02-S031 | https://cen.acs.org/business/specialty-chemicals/flavor-fragrance-industry-embracing-biotechnology/99/i5 | secondary | 2026-06-07 | C&EN (ACS) | F&F 行业拥抱生物科技综述 (designer yeast 发酵) |
| T02-S032 | https://www.scento.com/blog/biotech-innovations-fragrance-production | verified_primary | 2026-06-07 | Scento | (verifier auto: brand /blog) 精密发酵替代 sandalwood/oud/musk + DSM Firsantol |
| T02-S033 | https://mag.bynez.com/en/reports/olfactory-education-how-to-cultivate-your-nose/where-to-train-as-a-perfumer/ | surrogate_primary | 2026-06-07 | Nez (the olfactory movement) | perfumer own publication — ISIPCA/Givaudan school 训练 |
| T02-S034 | https://www.isipca.fr/en/formations/perfume | surrogate_primary | 2026-06-07 | ISIPCA | perfumery school 官方 (凡尔赛香水学校课程) |
| T02-S035 | https://glasspetalsmoke.blogspot.com/2013/09/the-jean-carles-method-olfactory.html | secondary | 2026-06-07 | Glass Petal Smoke | Jean Carles 嗅觉训练法 charts (方法框架原文转录) |
| T02-S036 | https://aiadopters.club/p/ai-in-the-fragrance-industry | secondary | 2026-06-07 | Kamil Banc | Symrise+IBM Philyra / Firmenich Scentmate / IFF 综述 |
| T02-S037 | https://www.whatscent.app/magazine/maceration-in-perfumery | secondary | 2026-06-07 | WhatScent | maceration/陈化对气味的影响 (静置 2 周–6 月) |
| T02-S038 | https://basenotes.com/threads/reverse-engineering-in-perfumery-is-it-possible.379232/ | secondary | 2026-06-07 | Basenotes forum | 业内讨论 GC-MS 逆向工程的边界 |
| T02-S039 | https://nstperfume.com/2009/04/04/rip/ | secondary | 2026-06-07 | Now Smell This | IFRA/oakmoss 限用导致经典香水 reformulation |
| T02-S040 | https://www.fragrancesoftheworld.info/ | surrogate_primary | 2026-06-07 | Michael Edwards | originator 官方付费数据库入口 (订阅制) |
| T02-S041 | https://en.wikipedia.org/wiki/Iso_E_Super | secondary | 2026-06-07 | — | Iso E Super captive→通用 合成分子代表 二手定义 |

**first-hand 占比估计**：41 source 中，`verified_primary` 8 (T02-S022 立法 / S023 NCBI / S024 .edu / S026 Osmo / S027 Google / S028 P&F / S029 P&F / S032 verifier 自动判 brand/blog) + `surrogate_primary` 17 (vendor docs / supplier / originator / standards body / perfumery school / perfumer own publication) = **25 / 41 ≈ 61%** 算 first-hand（按 Surrogate Policy「vendor docs / 监管原文为一手」口径 + verifier 自动判定）。达标 ≥ 50%。其余 16 为 secondary（学术 abstract / 社区一手吐槽 / 行业媒体 / 百科核对），无 blacklisted（zhihu/公众号/prnewswire 等已剔除）。
> 注：S024 (achs.edu)、S032 (scento.com/blog) 由 `source_verifier.py` 自动判为 verified_primary（.edu 域 / brand-domain /blog 路径），按「不私自降级」规范保留 verifier 结果；S032 实为编辑性博客，引用其商业化数字时仍按「业内综述/厂商转述」加 caveat，**不**因 bucket 高就当强一手。

---

## 总览（按 tier 分组）

> **数量**：必备 **6** / 场景特化 **8** / 新兴 **4**。

### 必备层（6 个，≥80% 认真从业/学习者用）
| 工具 | 一句话 | Decay | Sources |
|------|--------|-------|---------|
| 1. 原料调色板 (the palette) | 天然 EO/absolute/CO2 + 合成 aroma chemicals/captives，调香师的「字母表」 | low | T02-S001/003/004/041 |
| 2. 精密电子秤 (0.001–0.01g) | 配方按重量计量、可复现可缩放的物理前提 | low | T02-S002 |
| 3. 闻香纸 mouillettes + 稀释方案 | 评估 top→heart→base 演化、迭代 mods 的眼睛 | low | T02-S002/037 |
| 4. TGSC 原料数据库 | 2972 种 aroma chemical 的 CAS/odor/IFRA/供应商免费查询站 | medium | T02-S001 |
| 5. 配方管理（电子表格 / indie 软件 / pro PLM） | 记录 %、缩放、版本、成本——配方的「源代码」 | medium | T02-S008/009/010/012 |
| 6. IFRA 合规计算器 / 配方校验 | 上市前不可跳过的安全/法规闸门（限用浓度按修订版变） | medium | T02-S008/010/011/021 |

### 场景特化层（8 个）
| 工具 | 一句话 | Decay | Sources |
|------|--------|-------|---------|
| 7. indie 供应商套件 (PA/Pell Wall/Hekserij/Eden) | 小量买料 + 入门 kit，独立调香的供应命脉 | medium | T02-S003/004/005/006/007 |
| 8. GC-MS / headspace 分析仪 | 成分鉴定、QC、逆向工程、活体捕香 | low | T02-S014/015/016/038 |
| 9. 企业级配方软件 (Selerant DevEX / Coptis PLM) | 香精公司 B2B 全生命周期 + 多法域法规自动化 | medium | T02-S012/013 |
| 10. Fragrantica / Basenotes 数据库 | 查香、note pyramid、社区情报（≠配方依据） | medium | T02-S018/019/020 |
| 11. Michael Edwards Fragrances of the World | 60k+ 香水按 Fragrance Wheel 分类的「香水圣经」 | low | T02-S017/018/040 |
| 12. 稀释/陈化/称量设备套件 | 10% 母液、移液、maceration 静置、过滤 | low | T02-S002/037 |
| 13. 方法框架：Jean Carles 法 + 香风琴 (orgue) | 系统化学料 + 工位组织——非软件但核心「工具」 | low | T02-S033/035 |
| 14. 评论 canon 作评估标尺 (Turin/Sanchez《Perfumes: The Guide》) | 校准品味与历史坐标的评香参考 | low | T02-S018 |

### 新兴层（4 个，Decay risk high — 12 月可能剧变）
| 工具 | 一句话 | Decay | Sources |
|------|--------|-------|---------|
| 15. AI 配方生成 (Philyra / Carto / Scentmate / Codex) | 大数据扫配方 + 实时可视化辅助调香师 | high | T02-S028/036 |
| 16. 生物科技/可持续合成分子 (发酵法 sandalwood/ambrox/patchouli) | designer yeast 造珍稀分子，重塑「天然 vs 合成」 | high | T02-S029/030/031/032 |
| 17. AI 香气预测 / 数字嗅觉 (Osmo POM) | 由分子结构预测气味的 GNN 地图 | high | T02-S026/027 |
| 18. headspace 新技术 / 活体捕香迭代 | 现场无损捕捉花香顶空再 GC 重建 | high | T02-S016 |

---

# 必备层（6 个）

## 1. 原料调色板 (the palette / orgue 的内容物)

- **One-liner**：天然原料（essential oils / absolutes / CO2 萃取 / 净油）+ 合成 aroma chemicals / captives（如 Iso E Super / Hedione / Ambroxan / Galaxolide / Cashmeran）构成调香师的「字母表」——这是本行**最核心的「工具」**，软件只是记账。
- **Tier**：必备
- **Maintainer / Owner**：无单一所有者；天然由 Grasse / Robertet / 各产地供应，合成由四大 + Iso E Super(原 IFF captive→通用) 等。代表分子见 (evidence: [T02-S041])。
- **License**：原料本身无 license；captives = 专利期内由单家香精公司专有 (proprietary)，专利过期后成通用 aroma chemical（Iso E Super 即典型轨迹） (evidence: [T02-S041])。
- **Maturity signals**：
  - 行业约定俗成的「workhorse」分子（Hedione/Iso E Super/Ambroxan/Galaxolide）已用数十年，是基础设施级 (last checked: 2026-06-07)。
  - TGSC 收录 2972 种 aroma chemical 可作调色板规模锚 (evidence: [T02-S001])。
- **典型使用场景**：构建 accord 和弦；搭挥发度金字塔（top/heart/base）；用 captive 做差异化签名。
- **不适合 / 替代方案**：纯天然派会刻意排除合成分子；但**「天然=安全/无致敏」是误区**——天然 EO 含 limonene/linalool/citral/eugenol 等高致敏成分且批次/氧化波动大 (evidence: [T02-S023, T02-S024])。
- **生产案例**：Iso E Super 从 IFF captive 走向行业通用、并催生 Escentric Molecules「单分子香水」品类 (evidence: [T02-S041])。
- **维护者背景** (sub_skill_link)：captive 分子背后是四大香精公司研发；与 Track 01 figures（合成派代表人物）关联。
- **近期变化**：发酵法/生物科技分子正进入调色板（见新兴层 #16），冲击天然 vs 合成的成本与可持续叙事 (evidence: [T02-S030, T02-S032])。
- **来源**：[Primary] TGSC 原料库 (T02-S001, 2026-06-07)；[Primary] PerfumersWorld 训练 kit (T02-S003)；[Secondary] Iso E Super 百科 (T02-S041)。
- **可信度**：high
- **Decay risk**：**low**（调色板作为概念是行业地基，24+ 月稳定；单个分子可被发酵法替代但「调色板」本身不动）。last_checked 2026-06-07。

## 2. 精密电子秤 (0.001g 理想 / 0.01g 实用底线)

- **One-liner**：配方按**重量**而非体积计量、从而可精确复现与按比例放大的物理前提。
- **Tier**：必备
- **Maintainer / Owner**：通用实验室器材（无行业专属厂商绑定）。
- **License**：n/a（硬件）。
- **Maturity signals**：行业共识——「0.01g 是专业起步，0.001g 理想但贵且非必须」 (evidence: [T02-S002], 2026-06-07)。
- **典型使用场景**：称取 trial / mods；配母液稀释；按公式缩放生产批。
- **不适合 / 替代方案**：纯体积/滴数计量在专业语境**不可接受**——无法复现、无法缩放。
- **生产案例**：配方「以相对重量/毫克写、可按产量缩放、保证每次完全一致复现」是行业标准实践 (evidence: [T02-S002])。
- **近期变化**：无颠覆（成熟硬件）。
- **来源**：[Primary] School of Creative Perfumery 设备清单 (T02-S002, 2026-06-07)。
- **可信度**：high
- **Decay risk**：**low**（成熟硬件，3+ 年稳定）。last_checked 2026-06-07。

## 3. 闻香纸 mouillettes / blotters + 稀释方案

- **One-liner**：吸墨纸条蘸稀释液、溶剂挥发后由训练过的鼻子评估——这是调香师评估 top→heart→base 演化与迭代 mods 的「眼睛」。
- **Tier**：必备
- **License**：n/a（耗材）。
- **Maturity signals**：blotter 评估是行业标准评香动作（纸条蘸液、挥发后嗅评） (evidence: [T02-S002], 2026-06-07)；母液常配 1–10%（乙醇/DPG）以便评估 (evidence: [T02-S037])。
- **典型使用场景**：不必每版上身即可比对多版 trial；追踪 dry-down；盲嗅训练载体。
- **不适合 / 替代方案**：最终仍需上皮肤 + 旁人嗅评（blotter ≠ 皮肤表现）；blotter 不能替代 maceration 后的真实留香判断 (evidence: [T02-S037])。
- **生产案例**：「纸条 + 皮肤 + 周围人」三处评估是标准流程 (evidence: [T02-S037])。
- **近期变化**：无颠覆。
- **来源**：[Primary] 设备清单 (T02-S002)；[Secondary] 稀释/陈化 (T02-S037)。
- **可信度**：high
- **Decay risk**：**low**。last_checked 2026-06-07。

## 4. The Good Scents Company (TGSC) 原料数据库

- **One-liner**：免费、无注册墙的 aroma chemical / 天然原料百科——2972 种带 CAS、FEMA、气味描述、IFRA 安全数据、密度/闪点/推荐用量、建议供应商。
- **Tier**：必备
- **Maintainer / Owner**：The Good Scents Company（originator 官方站） (evidence: [T02-S001])。
- **License**：proprietary 站点但免费公开访问、无 paywall (evidence: [T02-S001])。
- **Maturity signals**：收录 **2972** 种 aroma chemical，全部免费可查 (last checked: 2026-06-07) (evidence: [T02-S001])；站点形态多年稳定、被社区当默认查料站。
- **典型使用场景**：查某分子气味/强度/安全/在不在自然界存在；按 odor/CAS/FEMA/化妆功能检索；找供应商线索。
- **不适合 / 替代方案**：气味描述是文字、不能替代实闻；安全数据须以现行 IFRA/EU 原文为准（见 #6、T02-S021/022）。Fragrantica 查的是「成品香水」，TGSC 查的是「原料」，二者不互替 (evidence: [T02-S019])。
- **生产案例**：indie/学习者把 TGSC 当「按 odor 浏览 naturals + synthetics、查 polarity/flash point/推荐 odor strength」的默认参考 (evidence: [T02-S001])。
- **近期变化**：站点本身缓慢更新（站长个人维护风格），存在「单点维护、若停更则数据冻结」的风险。
- **来源**：[Primary] TGSC 官方 (T02-S001, 2026-06-07)。
- **可信度**：high
- **Decay risk**：**medium**（数据内容稳，但单人维护站有停更/失访风险；20–40%/24 月）。last_checked 2026-06-07。

## 5. 配方管理（pro=企业 PLM / indie=电子表格 or 专用软件）

- **One-liner**：记录配方 %、按重量缩放、追踪版本/成本/供应商的「源代码控制」——分裂为 pro 内部 PLM 与 indie 电子表格/轻量 app 两条线。
- **Tier**：必备（**流派分裂明显**，见 Phase 2 接口）
- **Maintainer / Owner**：pro→Selerant/Trace One DevEX、Coptis、各公司内部系统；indie→Excel/Google Sheets 或 Perfume Workbench/Formulair/Perfumers Vault/PerfumeLab (evidence: [T02-S008/009/010/011/012/013])。
- **License**：从 proprietary 企业 license (Selerant/Coptis) 到免费开源 (Perfumers Vault) 全谱 (evidence: [T02-S010/012])。
- **Maturity signals**：indie 轻量 app 这一两年密集冒头（Perfume Workbench/Formulair/PerfumeLab 均内建 IFRA 检测） (last checked: 2026-06-07) (evidence: [T02-S008/009/011])。
- **典型使用场景**：indie——单人管几十–几百配方 + IFRA 校验 + 成本/g；pro——多团队、多 brief、多法域、SDS 自动生成 (evidence: [T02-S012])。
- **不适合 / 替代方案**：indie 不需要企业 PLM（太重/太贵）；pro 不能用裸 Excel（无法规自动化、无审计链）。电子表格的坑是**无 IFRA 自动校验**，易漏限用。
- **生产案例**：Selerant DevEX 作为 SAP 集成的 composite app，给香精厂提供 formulation + 多语种 SDS/GHS 自动化 (evidence: [T02-S012])。
- **维护者背景**：indie 软件多为单一开发者/小团队（如 Formulair 的 Apple-native 单体）。
- **近期变化**：indie 软件赛道升温、且把 IFRA 检测做成标配卖点（与 #6 融合中）。
- **来源**：[Primary] Perfume Workbench (T02-S008)、Formulair (T02-S009)、Perfumers Vault (T02-S010)、Selerant (T02-S012)、Coptis (T02-S013)。
- **可信度**：high
- **Decay risk**：**medium**（indie app 赛道流动性高、个别会消失；PLM 稳。整体 20–40%/24 月）。last_checked 2026-06-07。

## 6. IFRA 合规计算器 / 配方校验

- **One-liner**：上市前不可跳过的安全/法规闸门——按 IFRA Standards（Prohibition/Restriction/Specification）+ EU 致敏原标签核算每种料的最大用量。
- **Tier**：必备
- **Maintainer / Owner**：标准 originator = IFRA（standards body）(evidence: [T02-S021])；EU 致敏原 = 立法 (EUR-Lex)(evidence: [T02-S022])；执行工具内建于配方软件 (evidence: [T02-S008/010/011])。
- **License**：IFRA 标准库公开；执行工具随软件 license。
- **Maturity signals**：当前为 **IFRA 51st Amendment**，三类标准 + QRA2（IDEA 项目）按产品 category 算累积暴露 (last checked: 2026-06-07) (evidence: [T02-S021])。EU Reg 2023/1545 把可申报致敏原由 26 扩到 80+（约 82，含分组），**2026-07-31 起新品强制、2028-07-31 旧品退市** (evidence: [T02-S022])。
- **典型使用场景**：算某 EO/分子在 Cat 4(fine fragrance)/Cat 12(candle) 的上限；生成 IFRA certificate；导出致敏原标签 (evidence: [T02-S010/011])。
- **不适合 / 替代方案**：**不能**靠记忆或旧版限值——IFRA 限用浓度随修订版变，引用须标版本 (evidence: [T02-S021])；天然 EO 不豁免、与合成同等受查 (evidence: [T02-S025])。
- **生产案例**：Perfumers Vault 可 import IFRA xls 数据库校验并生成 IFRA 认证 (evidence: [T02-S010])；PerfumeLab 把 Cat 4/12 限值嵌进原料库 (evidence: [T02-S011])。
- **近期变化**：**EU 2023/1545 致敏原 26→80+ 是近年最大合规变动，2026 年正是落地年**（直接撞上本 skill 时点）；IFRA 修订版持续推进 (evidence: [T02-S022, T02-S021])。
- **来源**：[Primary] IFRA 标准 (T02-S021)；[Primary] EUR-Lex 立法原文 (T02-S022)；[Primary] 软件内建 (T02-S010/011)。
- **可信度**：high
- **Decay risk**：**medium**（标准内容随版本变是常态，但「必须做 IFRA 校验」这件事 low；版本数字 high）。last_checked 2026-06-07。

---

# 场景特化层（8 个）

## 7. indie 原料供应商套件 (Perfumer's Apprentice / Pell Wall / Hekserij / Eden Botanicals)

- **One-liner**：能小量购料 + 入门 kit 的供应商——独立/学习者调香的供应命脉（四大公司不零售给个人）。
- **Tier**：场景特化
- **Maintainer / Owner**：PA(US) / Pell Wall(UK) / Hekserij(NL) / Eden Botanicals(US, 天然) 等独立供应商 (evidence: [T02-S004/005/006/007])。
- **License**：n/a（电商）。
- **Maturity signals**：PA 转售 Givaudan/Firmenich/IFF/Robertet 的料 + 开课/卖 kit (last checked: 2026-06-07) (evidence: [T02-S005])；Pell Wall 服务 EU 小量需求、附慷慨样品 (evidence: [T02-S004])；Hekserij 以「极小量供应私人」著称 (evidence: [T02-S006])。
- **典型使用场景**：
  - US 工作室、要便宜 workhorse aroma chemicals → PA (evidence: [T02-S005])。
  - EU/UK 要小量 + 好天然 + 客服 → Pell Wall (evidence: [T02-S004])。
  - 极小量试 hobbyist → Hekserij (evidence: [T02-S006])。
  - 天然 carrier/原料 → Eden Botanicals (evidence: [T02-S007])。
- **不适合 / 替代方案**：要工业量/captive 专利分子 → 只能走四大 B2B（个人买不到）；跨境买致敏/危化料受运输与海关限制。
- **生产案例**：Institute for Art and Olfaction 维护的全球 supplier 列表是 indie 选料的事实标准导航 (evidence: [T02-S007])。
- **近期变化**：供应商不时调整 catalog；EU 致敏原新规可能压缩部分天然料的可售形态 (evidence: [T02-S022])。
- **来源**：[Primary] Pell Wall (T02-S004)、PA (T02-S005)、Hekserij (T02-S006)；[Secondary] IAO supplier 列表 (T02-S007)。
- **可信度**：high
- **Decay risk**：**medium**（个别供应商会变/停业，但「indie 走小量供应商」模式稳）。last_checked 2026-06-07。

## 8. GC-MS / headspace 分析仪

- **One-liner**：气相色谱-质谱 + 顶空进样——成分鉴定、QC、逆向工程竞品、活体花香捕香的行业标准分析平台。
- **Tier**：场景特化
- **Maintainer / Owner**：通用分析仪器（Agilent/Shimadzu 等），方法学是行业积累。
- **License**：n/a（仪器）。
- **Maturity signals**：GC & GC-MS「数十年来是香水行业最重要的分析技术」（多数原料 apolar/半挥发） (last checked: 2026-06-07) (evidence: [T02-S014])。
- **典型使用场景**：
  - 逆向工程竞品成分骨架 (evidence: [T02-S016])。
  - 静态 headspace（密封加热取顶空）/ 动态 headspace（purge & trap）捕活体花香 (evidence: [T02-S016])。
  - 配方稳定性 / 包材-香料相互作用研究 (evidence: [T02-S014])。
- **不适合 / 替代方案**：**GC-MS 不是「一键复制」按钮**——天然原料本身是复杂混合物、痕量料/captive 难定量、识别仍多靠手工 molecular marker、主观且不可靠 (evidence: [T02-S015, T02-S038])；难挥发组分要配 LC-MS (evidence: [T02-S016])。
- **生产案例**：deformulation 用色谱谱图识别拆解复杂混合物（Truan 2020 学术方法） (evidence: [T02-S015])。
- **近期变化**：GC-IMS、py-GC-MS 等变体 + AI 辅助谱图识别在演进（与新兴层 #18 有交集）。
- **来源**：[Secondary] TrAC 综述 (T02-S014)；[Secondary] FFJ deformulation (T02-S015)；[Secondary] Innovatech headspace (T02-S016)。
- **可信度**：high
- **Decay risk**：**low**（GC-MS 是地基级分析平台，3+ 年稳；AI 谱图识别是增量不是替代）。last_checked 2026-06-07。

## 9. 企业级配方软件 (Selerant DevEX / Coptis PLM)

- **One-liner**：香精公司 B2B 全生命周期管理——配方 + 成本模拟 + 多法域法规/SDS 自动化 + 团队协作。
- **Tier**：场景特化
- **Maintainer / Owner**：Selerant / Trace One（DevEX）、Coptis (evidence: [T02-S012/013])。
- **License**：proprietary 企业 license。
- **Maturity signals**：DevEX 作为 SAP NetWeaver 集成的 composite app，服务 food/flavor/fragrance/cosmetics 等流程制造 (last checked: 2026-06-07) (evidence: [T02-S012])。
- **典型使用场景**：B2B 命题创作（the brief → creation → mods）下的多项目管控；自动生成多语种 GHS SDS；法规模块跨数十法域 (evidence: [T02-S012])。Coptis 集中数据 + 成本模拟 + 协作 (evidence: [T02-S013])。
- **不适合 / 替代方案**：indie/个人**不该上**企业 PLM（太重、license 贵）→ 用 #5 的轻量 app/电子表格。
- **生产案例**：Selerant 列香精为其服务的流程制造行业之一，提供 fragrance 定制视图 (evidence: [T02-S012])。
- **近期变化**：PLM 持续整合 AI/法规更新（含 EU 2023/1545 致敏原扩列的自动化需求）。
- **来源**：[Primary] Selerant (T02-S012)、Coptis (T02-S013)。
- **可信度**：medium（厂商自述为主，社区独立评测少；闭源 B2B）。
- **Decay risk**：**medium**。last_checked 2026-06-07。

## 10. Fragrantica / Basenotes 数据库（查询用，**非配方依据**）

- **One-liner**：成品香水的 note pyramid + 社区评价 + 发行情报的众包数据库——查香、定位、追风向用，但**不是配方还原**。
- **Tier**：场景特化
- **Maintainer / Owner**：Fragrantica、Basenotes（社区平台） (evidence: [T02-S019/020])。
- **License**：n/a（公开站，本文件按 secondary 处理，不冒充 verified_primary，符合 intake warning）。
- **Maturity signals**：两站是 enthusiast/从业者查香的事实标准（Basenotes 列官方 note triangle；Fragrantica 混厂商文案 + 读者投票，并有「按强度的第二金字塔」） (last checked: 2026-06-07) (evidence: [T02-S019/020])。
- **典型使用场景**：查某香水 note/perfumer/年代；竞品定位；追品类风向；Edwards 体系外的快速检索。
- **不适合 / 替代方案**：**不要把 note pyramid 当配方/recipe**——金字塔常是营销小说（"sunny notes by optic tech" 之类纯虚构），且众包 note 常漏官方 note 或加从没人描述过的 note (evidence: [T02-S019])；两站 note 来源口径不同会打架 (evidence: [T02-S020])。配方还原要靠 GC-MS（#8）而非读金字塔。
- **生产案例**：Fragrantica 用户投票强度生成第二金字塔，被认为「常比文字评论更客观」但 pyramid 整体准确性参差 (evidence: [T02-S019])。
- **近期变化**：社区数据持续增长；AI 生成 note 描述渗入需警惕。
- **来源**：[Secondary] Fragrantica 金字塔批评 (T02-S019)；[Secondary] Basenotes vs Fragrantica (T02-S020)；[Secondary] FotW 百科 (T02-S018)。
- **可信度**：medium。
- **Decay risk**：**medium**。last_checked 2026-06-07。

## 11. Michael Edwards «Fragrances of the World» + Fragrance Wheel

- **One-liner**：把 60,000+ 香水按 14 香型 Fragrance Wheel 逐一分类的「香水圣经」——行业标准的香型坐标与检索库（付费订阅）。
- **Tier**：场景特化
- **Maintainer / Owner**：Michael Edwards 及团队（分类法 originator，香气分类学家/史学家） (evidence: [T02-S017/018])。
- **License**：proprietary，在线数据库 2004 起按付费订阅 (evidence: [T02-S018])。
- **Maturity signals**：1984 首版（原名 The Fragrance Manual），1992 引入 Fragrance Wheel，已分类 **60,000+** 香水、**14** 香型 (last checked: 2026-06-07) (evidence: [T02-S017/018])。
- **典型使用场景**：给新作定香型坐标；按 family/note/sub-note + 发行年/调香师/瓶设计师检索；零售导购（Wheel 比线性谱系更适合零售） (evidence: [T02-S018])。
- **不适合 / 替代方案**：要查「成品社区情绪」→ Fragrantica（#10）；要查「原料」→ TGSC（#4）。Wheel 是分类工具、非创作配方工具。
- **生产案例**：被业界尊为「Fragrance Bible」、标准百科参考 (evidence: [T02-S018])。
- **维护者背景** (sub_skill_link)：Michael Edwards 本人是 Track 01 候选 figure（分类学派代表）。
- **近期变化**：数据库持续年更扩列（14 香型框架稳定）。
- **来源**：[Primary] Fragrance Wheel 官方 (T02-S017)、付费库入口 (T02-S040)；[Secondary] 百科 (T02-S018)。
- **可信度**：high
- **Decay risk**：**low**（行业标准分类法，3+ 年稳）。last_checked 2026-06-07。

## 12. 稀释 / 陈化 / 称量设备套件 (beakers / pipettes / 母液 / maceration)

- **One-liner**：把配方从「纸面 %」变成「可评估液体」的物理工具链——硼硅烧杯、移液管、10% 母液、过滤、maceration 静置。
- **Tier**：场景特化
- **License**：n/a（实验耗材/器材）。
- **Maturity signals**：标准实验室套件 + 评估前常配 1–10% 母液 (last checked: 2026-06-07) (evidence: [T02-S002/037])。
- **典型使用场景**：配高效力分子的稀释母液（便于精称与评估）；trial 稀入乙醇做浓度分级（parfum 20–30% / EDP 15–20% / EDT 5–15% / EDC 2–5%） (evidence: [T02-S037])；maceration 静置 2–4 周（复杂配方 1–3 月、个别可到 6 月）使分子融合稳定 (evidence: [T02-S037])。
- **不适合 / 替代方案**：跳过 maceration 直接评判留香会误判（新调 ≠ 陈化后） (evidence: [T02-S037])；纯天然/树脂料需特殊溶解（非所有料溶于乙醇）。
- **生产案例**：浓度分级与陈化是从「concentrate→成品」的标准工序 (evidence: [T02-S037])。
- **近期变化**：无颠覆。
- **来源**：[Primary] 设备清单 (T02-S002)；[Secondary] 稀释/陈化 (T02-S037)。
- **可信度**：high
- **Decay risk**：**low**。last_checked 2026-06-07。

## 13. 方法框架：Jean Carles 法 + 香风琴 (orgue)（非软件，但本行核心「工具」）

- **One-liner**：系统化建立嗅觉记忆的训练法（Jean Carles）+ 把 500–1500 瓶料半圆环绕工位的物理组织（the perfumer's organ）——把 tacit 的「鼻子」工程化的脚手架。
- **Tier**：场景特化（**方法即工具**，呼应 intake「核心工具=方法框架」）
- **Maintainer / Owner**：Jean Carles 法（Roure 调香学校经典教法）；orgue 是行业通用工位形态 (evidence: [T02-S033/035])。
- **License**：n/a（公共方法/工艺）。
- **Maturity signals**：Jean Carles 两步法（先按相似性分组闻单体掌握主题/层次，再学搭配）至今是训练范式 (last checked: 2026-06-07) (evidence: [T02-S035])；orgue 典型 500–1500 瓶 (evidence: [T02-S033])。
- **典型使用场景**：学习者按 family 系统闻料、在不同浓度反复闻同一料直至条件反射式识别（嗅觉无书面记法，只能重复内化） (evidence: [T02-S033])；ISIPCA/Givaudan 内部学校的训练骨架 (evidence: [T02-S033/034])。
- **不适合 / 替代方案**：**没有捷径替代反复闻料**——AI/数字嗅觉（#17）能辅助但不能替代人鼻校准 (evidence: [T02-S033])。
- **生产案例**：Givaudan Argenteuil 学校年均仅收约 3 名学员、训练 4 年；ISIPCA 1970 由 Jean-Jacques Guerlain 创办、与凡尔赛大学合作授学位 (evidence: [T02-S033/034])。
- **维护者背景** (sub_skill_link)：Jean Carles / ISIPCA 体系与 Track 01 figures（法系传承）+ Track 03 workflows（训练 SOP）强关联。
- **近期变化**：方法稳定；线上课（ISIPCA online）扩大可及性 (evidence: [T02-S034])。
- **来源**：[Primary] Nez 训练报告 (T02-S033)、ISIPCA 官方 (T02-S034)；[Secondary] Jean Carles charts (T02-S035)。
- **可信度**：high
- **Decay risk**：**low**（百年量级方法论，极稳）。last_checked 2026-06-07。

## 14. 评论 canon 作评估标尺（Turin & Sanchez «Perfumes: The Guide» / «The Secret of Scent»）

- **One-liner**：用权威香评/历史坐标校准自己的品味与判断——评香师/学习者的「评估参考工具」。
- **Tier**：场景特化（评估维度工具，与 Track 04 canon 交叉）
- **Maintainer / Owner**：Luca Turin & Tania Sanchez（评论 canon 作者）。
- **License**：n/a（出版物）。
- **Maturity signals**：被 intake 列为行业评论 ground truth；与 Fragrances of the World 并列为行业参考 (last checked: 2026-06-07) (evidence: [T02-S018]，交叉 intake (g) 节)。
- **典型使用场景**：建立「好/坏香水」的历史与批评坐标；理解 vintage vs reformulation 之争；校准盲嗅判断。
- **不适合 / 替代方案**：**别把香评网均分当配方依据**（与 #10 同坑）；Turin 的振动理论是嗅觉科学**少数派**（2004 Keller-Vosshall 反驳形状/受体主流），引用须标分歧、不当主流 (evidence: 交叉 intake warning)。
- **近期变化**：评论 canon 稳定；社区评分文化与之并存。
- **来源**：[Secondary] FotW/行业参考语境 (T02-S018)；交叉 Track 04 canon。
- **可信度**：medium（本轨主查工具栈，评论 canon 细节交由 Track 04）。
- **Decay risk**：**low**。last_checked 2026-06-07。

---

# 新兴层（4 个，全部 Decay risk = high，12 月可能剧变）

## 15. AI 配方生成（IFF Codex / Givaudan Carto / DSM-Firmenich Scentmate / Symrise(IBM) Philyra）

- **One-liner**：用 AI 扫数千配方 + 市场数据生成/优化方案、实时可视化复杂香料组合，辅助（非取代）调香师。
- **Tier**：新兴（`stability: experimental`）
- **Maintainer / Owner**：四大各自的系统——Givaudan **Carto**、DSM-Firmenich **Scentmate**、IFF **Codex**、Symrise+IBM **Philyra** (evidence: [T02-S028/036])。
- **License**：proprietary 内部工具（不对外开放）。
- **Maturity signals**：Philyra 已用于商业香水创作（扫数千配方 + 市场数据生成）；Carto 实时可视化 scent 组合、减少 formulation 错误；四大均把 AI 视为「不可或缺的未来基础」 (last checked: 2026-06-07) (evidence: [T02-S028/036])。
- **典型使用场景**：从 brief 快速生成候选配方骨架；优化已有配方；辅助新手调香师缩短迭代。
- **不适合 / 替代方案**：**AI 不取代「鼻子」**——最终评估、品味、accord 微调仍是人鼻 tacit 工作（#13）；行业内对「AI 是 friend or foe」仍有张力 (evidence: [T02-S036])。indie 几乎用不到这些闭源内部系统。
- **生产案例**：Symrise×IBM Philyra 已产出商业香水 (evidence: [T02-S036])；Givaudan 在行业会议公开 Carto 路线 (evidence: [T02-S028])。
- **维护者背景** (sub_skill_link)：四大研发团队；与 Track 01 figures（分子/工程派）关联。
- **近期变化**：**高速演进**——各家系统持续迭代、命名/能力可能 12 月内变样；闭源使外部追踪难。
- **来源**：[Primary] Perfumer & Flavorist Givaudan AI (T02-S028)；[Secondary] AI in fragrance 综述 (T02-S036)。
- **可信度**：medium（闭源，多为厂商/媒体口径）。
- **Decay risk**：**high**（>40%/12 月被显著改变；新兴层默认 high）。last_checked 2026-06-07。

## 16. 生物科技 / 可持续合成分子（发酵法 sandalwood / ambrox / patchouli 等）

- **One-liner**：用 designer yeast 发酵造珍稀/濒危香料分子（檀香/沉香/麝香替代），把「天然 vs 合成」的成本、可持续、供应链叙事整个重写。
- **Tier**：新兴（`stability: experimental`，但商业化在加速）
- **Maintainer / Owner**：Givaudan（cultured ingredient）、DSM-Firmenich（Firsantol/Clearwood Prisma）、Ginkgo Bioworks×Robertet、Evolva、Amyris (evidence: [T02-S029/030/031/032])。
- **License**：proprietary 分子/菌株（专利）。
- **Maturity signals**：cultured ingredient「像酿啤酒一样」由设计酵母发酵产出 (last checked: 2026-06-07) (evidence: [T02-S030/031])；合成生物 2025 是增长最快子段（约 27.3% 份额，多基因通路/无细胞生物合成） (evidence: [T02-S029/032])；DSM Firsantol（生物合成檀香分子）、Clearwood Prisma（2025，符合 ISO 9235 天然标准的木质-广藿香） (evidence: [T02-S032])。
- **典型使用场景**：替代受气候/地缘/濒危限制的天然料（檀香 Santalum album / oud / 天然麝香）并提稳定性与留香 (evidence: [T02-S032])；降低农药/废弃/碳/土地水耗 (evidence: [T02-S032])。
- **不适合 / 替代方案**：天然纯粹派可能拒认发酵分子为「天然」（监管/认证口径分歧，如是否符 ISO 9235） (evidence: [T02-S032])；成本随规模化波动，早期可能贵于天然。
- **生产案例**：Ginkgo×Robertet 2015 起工程化酵母产桃/杏/椰香、并宣布商业规模发酵成功 (evidence: [T02-S031, 注: 商业化里程碑由厂商自报])。
- **维护者背景** (sub_skill_link)：合成生物公司 + 四大研发；与 Track 01 figures（可持续/分子派）关联。
- **近期变化**：**2024–2025 密集出新分子**（Clearwood Prisma 等），商业化年增；是「天然 vs 合成」心智模型的当下震中。
- **来源**：[Primary] Perfumer & Flavorist 生物造香 (T02-S029)、Givaudan biotech (T02-S030)；[Secondary] C&EN (T02-S031)、Scento (T02-S032)。
- **可信度**：medium（部分商业化里程碑为厂商自报，须 caveat）。
- **Decay risk**：**high**（>40%/12 月——新分子持续出、份额数字快速变）。last_checked 2026-06-07。

## 17. AI 香气预测 / 数字嗅觉（Osmo Principal Odor Map）

- **One-liner**：用图神经网络从分子结构预测气味的「气味地图」——把嗅觉「数字化」，并已据此设计出全新香气分子。
- **Tier**：新兴（`stability: experimental`）
- **Maintainer / Owner**：Osmo（spun out of Google Research，与 Google Cloud 合作） (evidence: [T02-S026/027])。
- **License**：proprietary（研究 + 商业化）。
- **Maturity signals**：Principal/Primary Odor Map (POM) 基于 GNN、训练于 ~5000 已知 odorant，在 53% 测试分子上优于平均人类评审 (last checked: 2026-06-07) (evidence: [T02-S026])；已发表 Science 论文、launch 三款全 AI 设计分子（Glossine/Fractaline/Quasarine） (evidence: [T02-S026])。
- **典型使用场景**：由结构预测气味、筛选 500k 假想分子；为「设计性气味分子」提供候选；长期指向数字气味传输/AR (evidence: [T02-S026/027])。
- **不适合 / 替代方案**：**预测 ≠ 调香**——POM 给单分子气味预测，复杂 accord 的协同/审美仍需人鼻（#13）；当前更偏研究/工具供应商，非 indie 日常工具。
- **生产案例**：Osmo 与 Google Cloud 合著技术博客披露落地 (evidence: [T02-S027])；三款 AI 分子已 launch (evidence: [T02-S026])。
- **维护者背景** (sub_skill_link)：Osmo 创始团队（Google Research 出身）；潜在 Track 01 figure（数字嗅觉派）。
- **近期变化**：**快速推进**——从 POM 论文到 AI 分子 launch 到「olfactory teleportation」概念，12 月内料持续突破。
- **来源**：[Primary] Osmo blog (T02-S026)、Google Cloud (T02-S027)。
- **可信度**：medium（前沿、部分为厂商叙事）。
- **Decay risk**：**high**。last_checked 2026-06-07。

## 18. headspace 新技术 / 活体捕香迭代（含 AI 谱图识别）

- **One-liner**：现场无损捕捉鲜花/活体顶空挥发物再 GC 重建——配合 AI 谱图识别，让「捕捉自然界不可萃取气味」更快更准。
- **Tier**：新兴（`stability: experimental`；底层 headspace 成熟，但 AI+新探头组合是新势头）
- **Maintainer / Owner**：仪器厂 + 香精公司方法学；AI 谱图识别为学术/初创推进 (evidence: [T02-S015/016])。
- **License**：仪器/方法混合。
- **Maturity signals**：static/dynamic headspace 是成熟取样法 (last checked: 2026-06-07) (evidence: [T02-S016])；deformulation 的色谱谱图自动识别仍在「减少手工 marker 主观性」的学术演进中 (evidence: [T02-S015])。
- **典型使用场景**：活体花香（不可蒸馏/萃取的鲜花）顶空捕捉→重建 accord；竞品快速拆解；QC 提速。
- **不适合 / 替代方案**：仍受「天然复杂混合物 + 痕量料难定量」限制（与 #8 同坑） (evidence: [T02-S015])；AI 识别尚不能全自动可靠拆配方。
- **生产案例**：headspace + GC/MS 组合用于活体捕香与配方-包材相互作用研究 (evidence: [T02-S014/016])。
- **近期变化**：AI 辅助谱图识别 + 便携 headspace 探头是当前增量方向。
- **来源**：[Secondary] FFJ deformulation (T02-S015)、Innovatech headspace (T02-S016)、TrAC (T02-S014)。
- **可信度**：medium。
- **Decay risk**：**high**（AI 识别这层快速变；底层 headspace 本身 low）。last_checked 2026-06-07。

---

## 选型决策树

> 节点数 **9**（在 5–10 区间）。轴 = **目的（学习/创作/分析/合规）× 身份（pro/indie）× 天然 vs 合成**。

### 决策树 A：你的核心目的是什么？

#### Branch 1：学习 / 建立嗅觉记忆（学习者）
→ 推荐：**Jean Carles 法 + 训练原料 kit**（按 family 反复闻单体，先掌握主题层次）+ **TGSC** 查料 + 闻香纸（#13/#3/#4/#7）。理由：嗅觉无书面记法，唯一路径是结构化重复闻料 (evidence: [T02-S033/035])。
→ 不推荐：一上来买企业 PLM 或迷信 AI（#9/#15）——重、贵、且替代不了人鼻校准 (evidence: [T02-S033])。
→ 真实案例：ISIPCA / Givaudan Argenteuil 学校均以「长年反复闻料」为骨架（Givaudan 年收约 3 人、训 4 年） (evidence: [T02-S033/034])。

#### Branch 2：创作配方
##### Branch 2a：你是 indie / 独立调香
→ 推荐：indie 供应商小量购料（PA/Pell Wall/Hekserij/Eden，#7）+ **轻量配方软件含 IFRA 检测**（Perfume Workbench / Formulair / Perfumers Vault，#5/#6）+ 闻香纸 + 0.01g 秤 + maceration（#3/#2/#12）。理由：个人买不到四大 captive，小量供应商 + 自带 IFRA 校验的便宜工具最务实 (evidence: [T02-S004/005/008/010])。
→ 不推荐：企业 PLM（#9，太重太贵）；裸 Excel 无 IFRA 校验（易漏限用） (evidence: [T02-S008])。
##### Branch 2b：你是 pro / 香精公司在职
→ 推荐：公司内部调色板（含 captives）+ **企业 PLM（Selerant DevEX / Coptis）**（#9）+ 内部 AI 工具（Carto/Codex/Scentmate/Philyra，#15）。理由：B2B brief→creation→mods 需多团队/多法域/SDS 自动化 + AI 加速 (evidence: [T02-S012/028])。
→ 替代：小项目可用轻量工具，但审计链/法规自动化是 PLM 不可替代点 (evidence: [T02-S012])。

#### Branch 3：分析 / 逆向工程 / QC
→ 推荐：**GC-MS + headspace（static/dynamic）**（#8/#18）。理由：成分鉴定、捕活体花香、拆竞品骨架的行业标准 (evidence: [T02-S014/016])。
→ 重要 caveat：**不是一键复制**——天然混合物 + 痕量/captive 难定量、识别仍多手工 (evidence: [T02-S015/038])；难挥发组分要 LC-MS (evidence: [T02-S016])。
→ 不推荐：靠读 Fragrantica/Basenotes note pyramid 来「还原配方」（那是营销小说，不是配方） (evidence: [T02-S019])。

#### Branch 4：合规 / 上市
→ 推荐：**IFRA 计算器（标版本！）+ EU 致敏原校验**（#6）。理由：51st Amendment + EU 2023/1545（26→80+ 致敏原，2026-07 强制）是硬闸门 (evidence: [T02-S021/022])。
→ 必做：天然 EO 同样受查、不豁免 (evidence: [T02-S025])；引用限值必标 IFRA 修订版号 (evidence: [T02-S021])。

#### Branch 5：天然 vs 合成 的横切选择（贯穿 2a/2b）
→ 若追求可持续/珍稀料替代且能接受新分子 → 关注**发酵法生物科技分子**（Firsantol/Clearwood Prisma，#16） (evidence: [T02-S030/032])。
→ 若坚持天然纯粹 → 用天然供应商（Eden 等，#7），但**别假设天然=安全**（高致敏成分 + 批次/氧化波动） (evidence: [T02-S023/024])。
→ 决策锚：发酵分子是否算「天然」在监管/认证上仍有分歧（ISO 9235 口径），按目标市场标签法规定 (evidence: [T02-S032])。

#### Branch 6：定位 / 香型坐标 / 查香
→ 推荐：原料查 **TGSC**（#4）；成品香型分类查 **Michael Edwards Fragrances of the World / Fragrance Wheel**（#11）；社区情绪/note 查 **Fragrantica/Basenotes**（#10，仅参考）。理由：三者分工不同、不互替 (evidence: [T02-S001/017/019])。

---

## 避坑清单（≥ 6，实得 8 条）

- ❌ **不要以为「天然=安全/无致敏」**：天然 EO 含 limonene/linalool/citral/eugenol 等高致敏成分，且批次/氧化波动大、会随时间氧化升高致敏风险；IFRA 对天然与合成一视同仁 (evidence: [T02-S023, T02-S024, T02-S025])。
- ❌ **不要迷信「24 小时持久」营销**：留香受 maceration、fixative、IFRA 限用（如 oakmoss/atranol 限用使低-atranol 替代挥发快、丧失定香）共同决定；「持久」常是营销话术而非配方事实 (evidence: [T02-S037, T02-S039])。
- ❌ **不要把香评网均分 / note pyramid 当配方依据**：金字塔常是营销小说（"sunny notes" 之类纯虚构）、众包 note 漏官方料或加杜撰料、两站口径还互相打架；配方还原要 GC-MS 不是读金字塔 (evidence: [T02-S019, T02-S020])。
- ❌ **不要跳过 IFRA / EU 合规校验**：51st Amendment + EU 2023/1545（致敏原 26→80+，2026-07-31 新品强制）是硬性闸门，裸 Excel 无自动校验最易漏限用——用内建 IFRA 检测的软件 (evidence: [T02-S021, T02-S022, T02-S008])。
- ❌ **不要把香基/分子浓度当随意**：配方必须按**重量**精确计量（0.01g 起步），高效力分子要先配 10% 母液再精称，否则不可复现、不可缩放 (evidence: [T02-S002, T02-S037])。
- ❌ **不要把 essential oil 当「therapeutic-grade」噱头**：「治疗级/疗愈级」是营销标签、无统一监管定义；安全取决于物质本身+浓度+用法，不取决于「天然」标签 (evidence: [T02-S024])。
- ❌ **不要以为 GC-MS 是「一键复制」按钮**：天然原料是复杂混合物、痕量料/captive 难定量、识别仍多靠手工 molecular marker（主观不可靠），难挥发组分还得配 LC-MS——逆向工程有真实边界 (evidence: [T02-S015, T02-S016, T02-S038])。
- ❌ **不要 indie 上企业 PLM、也别 pro 用裸 Excel**：身份错配工具——个人用 Selerant 太重太贵、香精厂用裸表格则缺法规自动化/审计链 (evidence: [T02-S012, T02-S008])。

---

## Phase 2 提炼提示

### 反复出现 ≥ 3 source 都强调的「工具选型原则」（候选 playbook 规则）
- **「鼻子」不可被工具替代，工具只是脚手架**：嗅觉记忆靠反复闻料内化，AI/数字嗅觉只能辅助（出现于 T02-S033 / T02-S015 / T02-S026 隐含 + intake 第一性张力）。
- **合规先于创作自由**：IFRA 版本 + EU 致敏原是硬闸门，任何上市配方都要过；引用限值必标版本（出现于 T02-S021 / T02-S022 / T02-S025）。
- **工具按身份分层**：indie 轻量自带 IFRA / pro 企业 PLM / 学习者方法+kit——身份错配是常见坑（出现于 T02-S008 / T02-S012 / T02-S005）。
- **数据库分工不互替**：原料(TGSC) / 成品分类(Edwards) / 社区情绪(Fragrantica) 各司其职，混用 = 误用（出现于 T02-S001 / T02-S017 / T02-S019）。
- **按重量、可复现、可缩放**是配方的不可妥协前提（出现于 T02-S002 / T02-S037 + intake (e) 节）。

### 显著的工具流派分裂（候选 智识谱系条目）
- **闭源 B2B 寡头工具栈** vs **开源/轻量 indie 工具栈**：四大公司内部调色板(含 captives)+ 企业 PLM + 内部 AI（Carto/Codex/Philyra）↔ indie 小量供应商 + 免费/廉价 app（Perfume Workbench/Perfumers Vault）+ 公开 TGSC。代表分裂直通 intake「四大寡头 vs niche/indie」。(evidence: [T02-S012/015 vs T02-S004/008/010])
- **天然传统派工具** vs **分子/合成派工具**：天然供应商(Eden/Grasse 体系)+ 学徒制方法 ↔ aroma chemicals/captives + GC-MS/headspace + 发酵法生物分子。与 Track 01 figures 的法系 vs 分子派强关联。(evidence: [T02-S007/033 vs T02-S016/030])
- **人鼻校准派** vs **AI/数字嗅觉派**：Jean Carles 反复闻料 ↔ Osmo POM 结构预测 + AI 配方生成。「the nose=艺术家」vs「调香师=气味工程师」之争的工具投影（intake 学派分歧）。(evidence: [T02-S033 vs T02-S026/028])

### 新兴工具信号
- 当前活跃 / 上升的新工具数：**4**（AI 配方生成 / 生物科技分子 / 数字嗅觉 / headspace+AI）。
- 出现 → 主流 速度估计：**生物科技分子 ~24–36 月**（已商业化、年增），**AI 辅助 ~12–24 月**（四大已内部部署但闭源），**数字嗅觉 POM ~36 月+**（尚偏研究）。基于 2024–2026 的 launch 节奏。

### 冷僻 / 信号薄弱（诚实边界候选）
- **必备层 6 个、新兴层 4 个，均达标**——不触发冷僻协议的下限。
- 但 **first-hand 约 61%、且 25 个 first-hand 中 17 个是 surrogate_primary（vendor docs/supplier/originator/standards/school/perfumer publication）**，真 verified_primary 仅 8 个（监管立法 + NCBI/.edu 学术 + Osmo/Google/P&F 媒体 + 1 个 verifier 自动判的 brand/blog）。→ **Phase 2.8 须标注：工具栈维度「闭源主导、surrogate 偏高」**，核心创作工具（四大内部调色板/AI/学校教法）多经 surrogate 间接观察，未直接听到调香师本人公开拆解其私有工具栈。
- **数字类 caveat 已挂**：IFRA 51st / EU 2023/1545(82 含分组) / 浓度分级 % / 60k+ 香水 / 2972 aroma chemicals / 商业化里程碑——分别标了版本号、立法编号、约定俗成、originator 自报、厂商自报。Phase 2 引用时须保留 caveat。
- **中文一手结构性偏薄**（intake warning）：本轨工具栈 canon 几乎全 en+fr，中文世界以培训机构/KOL 测评二手为主，未纳入（黑名单口径）。

---

*Generated 2026-06-07. 候选探索 ~30 个工具/原料/方法，retained 18（必备 6 / 场景特化 8 / 新兴 4）。所有 maturity signal 与 claim 带 last_checked=2026-06-07 + source_id。供 Phase 1.5 review。*
