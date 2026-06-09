# Track 03 — Workflows 工作流研究：调香师 / 香水 (Perfumery & Fragrance)

> Phase 1 / Track 03（续跑：01 figures / 02 tools / 04 canon / 05 sources / 06 glossary 已完成，本轨补 workflows）。locale=global (en+fr-primary), profile=practitioner。
> **冷僻 + 闭源主导**：香水真实工作流（B2B 命题创作、评香师内部 loop、四大内部培养 pipeline）几乎全在四大香精公司（Givaudan / DSM-Firmenich / IFF / Symrise）墙内，公开一手稀薄。本文件沿用 **Surrogate Sources Policy** 把厚度堆回：香水学校页（note 含 `syllabus`/`课程`/`教材`/`education vendor`）、行业协会/标准机构（note 含 `association`/`协会`；标准制定方加 `originator`/`certification body`）、调香师/评香师自有出版物（note 含 `own publication`/`own site`）、供应商/香精公司 vendor 档（note 含 `vendor docs`/`supplier`）。**Fragrantica / Basenotes 一律 `secondary`，不冒充一手**。严标 surrogate_primary。
> **本轨是整合轨**：workflows 从 01 figures（调香师怎么干活）+ 02 tools（palette / Jean Carles 法 / IFRA 校验 / GC-MS 如何嵌入流程）+ 04 canon（描述的方法论）长出来，下游 merge 时与三轨交叉引用。
> **数字 caveat**：任何 % 浓度 / 留香小时 / mods 轮数 / 竞标命中率 / 训练年限 / IFRA 阈值——挂 source_id 或标 caveat（厂商自报 / 业内估 / 约定俗成各家不同 / IFRA 第 N 修订版）。本行无源精确数字尤其多（各家配比口径不同），已逐处标注。
> last_checked 统一 = **2026-06-08**。

---

## Source Manifest

| source_id | url | bucket | last_checked | author/host | one-line note |
|-----------|-----|--------|--------------|-------------|---------------|
| T03-S001 | https://www.grasse-perfumery.com/professions/evaluator/ | surrogate_primary | 2026-06-08 | GIP (Grasse Institute of Perfumery) | syllabus — 评香师职业流程官方页 (brief 解码→creative guidance→eval→feedback→panel test) |
| T03-S002 | https://oola-lab.com/blogs/notes/what-is-the-relationship-between-perfumer-and-evaluator | secondary | 2026-06-08 | Oo La Lab | perfumer⇄evaluator 协作描述 (evaluator 带回客观性, "extension of your own nose") |
| T03-S003 | https://magazine.moellhausen.com/how-to-write-a-creative-brief-for-the-fragrance-house | surrogate_primary | 2026-06-08 | Moellhausen (香精供应商) | vendor docs — incoming brief→executive brief→development 三段 + brief 必含要素 |
| T03-S004 | https://www.alphaaromatics.com/blog/how-to-write-a-fragrance-brief/ | secondary | 2026-06-08 | Alpha Aromatics | brief 是创作蓝图、传达 vision + 留创作余地 (brief 写法二手) |
| T03-S005 | https://mag.bynez.com/en/reports/reinventing-perfumery-discourse/secrets-and-lies-in-perfumery/ | surrogate_primary | 2026-06-08 | Nez (the olfactory movement) | own publication — core list(3-4 家)/ 内部竞争 / 复用 performing formula / 年度剔除 |
| T03-S006 | https://en.wikipedia.org/wiki/Perfumer | secondary | 2026-06-08 | — | perfumer 工作流综述 (brief→blending→"win the brief"→panel/AD 指导 mods→数月-数年) |
| T03-S007 | https://www.perfumerflavorist.com/fragrance/trends/news/21879382/the-juice-fragrance-evaluators-tell-their-stories | secondary | 2026-06-08 | Perfumer & Flavorist | 评香师自述系列 (行业媒体；本文取 search 摘要，正文 403/付费) |
| T03-S008 | https://www.mefragrance.com/perfume101.cfm | secondary | 2026-06-08 | Me Fragrance | 入门 SOP — top/heart/base 定义 + 起步配比 (营销页，配比仅作 caveat 锚) |
| T03-S009 | https://shop.perfumersapprentice.com/perfumersworkshop/advanced_blending.html | surrogate_primary | 2026-06-08 | The Perfumer's Apprentice | supplier — 进阶调配教学 (accord 起步、逐步加量、边调边试) |
| T03-S010 | https://www.immortalperfumes.com/blog/how-to-make-perfume-eau-de-parfum | secondary | 2026-06-08 | Immortal Perfumes | 入门 EDP 制作教程 (调香师自营博客，稀释/陈化步骤) |
| T03-S011 | https://glasspetalsmoke.blogspot.com/2013/09/the-jean-carles-method-olfactory.html | secondary | 2026-06-08 | Glass Petal Smoke | Jean Carles 嗅觉训练 charts (方法原文转录；与 T02-S035 同) |
| T03-S012 | https://boisdejasmin.com/2017/05/jean-carles-on-olfactory-training-perfumer-organ.html | surrogate_primary | 2026-06-08 | Victoria Frolova / Bois de Jasmin | critic own publication — Jean Carles 训练法 + 香风琴 (fetch 遇 bot 墙，取 search 摘要) |
| T03-S013 | https://boisdejasmin.com/2021/01/one-week-perfumery-course-jean-carles-method.html | surrogate_primary | 2026-06-08 | Victoria Frolova / Bois de Jasmin | critic own publication — 一周 Jean Carles 法课程实记 (训练 SOP) |
| T03-S014 | https://www.amazon.com/Perfumery-Training-Nose-Jean-Carles/dp/0244800316 | secondary | 2026-06-08 | Jean Carles (book) | 书目元数据 — «Perfumery: Training the Nose» (Carles 训练法原典) |
| T03-S015 | https://www.givaudan.com/fragrance-beauty/perfumery-school | surrogate_primary | 2026-06-08 | Givaudan | syllabus — 4 年内部学校 (仅员工)，先背 ~500 原料 + Carles 法骨架 |
| T03-S016 | https://www.isipca.fr/en | surrogate_primary | 2026-06-08 | ISIPCA (Versailles) | syllabus — 凡尔赛香水学校 (800 原料 + accord)，法系培养 ground truth |
| T03-S017 | https://www.grasse-perfumery.com/long-term/international-technical-degree-in-fragrance-creation-and-sensory-evaluation/ | surrogate_primary | 2026-06-08 | GIP (Grasse) | syllabus — 18 月 + 6 月实习/1200h，原料/accord/家族识别/GC-MS/法规 |
| T03-S018 | https://mag.bynez.com/en/reports/olfactory-education-how-to-cultivate-your-nose/where-to-train-as-a-perfumer/ | surrogate_primary | 2026-06-08 | Nez (the olfactory movement) | education vendor — 香水教育全景 (学费/时长/门槛 + Givaudan 年收 ~3 人/训 4 年) |
| T03-S019 | https://ifrafragrance.org/initiatives-positions/safe-use-fragrance-science/ifra-standards | surrogate_primary | 2026-06-08 | IFRA | association + certification body originator — IFRA Standards (Prohibition/Restriction/Specification), 上市前合规闸门 |
| T03-S020 | https://ifrafragrance.org/initiatives-positions/environment-health/allergens | surrogate_primary | 2026-06-08 | IFRA | association — 致敏原管理 (EU 2023/1545 标签 26→80+) |
| T03-S021 | https://eur-lex.europa.eu/legal-content/EN/TXT/PDF/?uri=CELEX:32023R1545 | verified_primary | 2026-06-08 | EU (EUR-Lex) | regulator 立法原文 Reg (EU) 2023/1545 — 致敏原扩列，2026-07 新品强制 |
| T03-S022 | https://nstperfume.com/2009/04/04/rip/ | secondary | 2026-06-08 | Now Smell This | IFRA oakmoss 限用→经典香水 reformulation (媒体) |
| T03-S023 | https://kafkaesqueblog.com/2014/05/26/the-perfume-industry-eu-regulations/ | secondary | 2026-06-08 | Kafkaesque | EU 法规对产业/reformulation 的冲击 (香评博客) |
| T03-S024 | https://scentxshop.com/en/blogs/notizie/profumi-riformulati-guida-ifra-versioni-originali | secondary | 2026-06-08 | ScentX | reformulation + IFRA + vintage vs 新版 指南 (零售博客) |
| T03-S025 | https://www.glossy.co/beauty/artificial-intelligence-is-quietly-disrupting-the-fragrance-development-process/ | secondary | 2026-06-08 | Glossy | AI 改写创作流程 (Carto/Philyra/Scentbird) + Becker "iPhone"喻 |
| T03-S026 | https://www.perfumerflavorist.com/events/event-coverage/news/21873544/givaudan-artificial-intelligence-the-future-of-fragrance | verified_primary | 2026-06-08 | Perfumer & Flavorist | Givaudan AI(Carto) 行业媒体一手会议报道 |
| T03-S027 | https://www.theartisaninsider.com/perfume/defining-niche-indie-and-artisan/ | secondary | 2026-06-08 | The Artisan Insider | niche/indie/artisan 定义 + IAO 'artisan' 三条件 (写配方/拥品牌/拥配方) |
| T03-S028 | https://www.karengilbert.co.uk/getting-into-the-fragrance-industry | surrogate_primary | 2026-06-08 | Karen Gilbert | syllabus — 进圈路径 (产业 vs indie 替代)，独立/artisan 教育视角 |
| T03-S029 | https://artandolfaction.com/reading-list/ | secondary | 2026-06-08 | Institute for Art & Olfaction | 香水教育 NGO (artisan 定义 + reading list 锚) |
| T03-S030 | https://www.iltusa.com/fragrance-stability-testing/ | surrogate_primary | 2026-06-08 | ILT (Industrial Laboratories) | vendor docs — 稳定性测试 SOP (加速/光照/冻融/实时 + 香型/色/物性) |
| T03-S031 | https://umbrex.com/resources/industry-analyses/how-to-analyze-a-cosmetics-company/fragrance-and-sensory-appeal-testing/ | secondary | 2026-06-08 | Umbrex | 感官/留香/sillage/扩散 测试 + panel testing 概述 |
| T03-S032 | https://www.whatscent.app/magazine/maceration-in-perfumery | secondary | 2026-06-08 | WhatScent | maceration/陈化对气味的影响 (静置 2 周–6 月) |
| T03-S033 | https://en.wikipedia.org/wiki/Reformulation | secondary | 2026-06-08 | — | reformulation 定义 (因法规/成本/供应 被迫重配) — 术语锚 |
| T03-S034 | https://www.benscents.com/blog/from-alchemy-to-algorithms-the-evolution-of-perfume-formulation-styles | secondary | 2026-06-08 | BenScents | 配方风格演进 (Carles Split：按挥发度/家族分类、按比例搭而非凭猜) |
| T03-S035 | https://www.perfumerflavorist.com/fragrance/fine-fragrance/article/21856054/the-juice-fragrance-evaluation-for-independent-brands-passion-above-all | secondary | 2026-06-08 | Perfumer & Flavorist | 独立品牌评香 (indie 评香师=brand↔perfumer 缺失环；正文 403，取 search 摘要) |

**bucket 计数**（共 35 条）：`verified_primary` **2**（T03-S021 EU 立法 / S026 P&F Givaudan AI 会议报道）；`surrogate_primary` **14**（GIP×3 = S001/S017 + S028... 实为 S001/S017；ISIPCA S016 / Givaudan school S015 / Nez×3 = S005/S018 含 education vendor + S012/S013 Bois de Jasmin critic own pub / IFRA×2 = S019/S020 / Karen Gilbert S028 / Moellhausen vendor S003 / PA supplier S009 / ILT vendor docs S030）；`secondary` **19**。
**粗一手率**：(2 + 14) / 35 = **16 / 35 ≈ 45.7%**。略低于 50%，是 en+fr-primary + 闭源行业的诚实反映——香水真实工作流的一手是四大墙内 SOP（不可得）+ 法/德文原典，公开一手只能靠 surrogate（学校 syllabus / IFRA 协会 / 调香师评香师自有出版物）堆。**未谎标 bucket 以凑率**：Wikipedia / 香评博客 / 零售教程 / P&F 付费正文摘要（含 S007/S035）一律 secondary；Fragrantica/Basenotes 全程未升级（本轨亦未纳入其社区帖作一手）。黑名单（知乎/公众号/百度/CSDN/G2/Capterra/内容农场）= 0 进表。所有 14 条 surrogate_primary note 均含白名单关键词（已校验）。
> 注：本轨 verified_primary 仅 2 条，与兄弟轨一致（04-canon verified=0、01-figures verified=4、02-tools verified=8 的口径差异源于各轨 source 性质：工具栈有 .edu/监管/学术命中多，工作流则几乎全靠学校页 + 行业媒体 + 调香师自述 surrogate）。**触发「冷僻/闭源诚实边界」**：真实创作工作流闭源主导，详见结尾。

---

## 总览（工作流地图）

> 本轨提炼 **retained 工作流元素 ~14 个**，按链路分 5 组：

| 组 | 工作流 | 一句话 | Decay | Sources |
|----|--------|--------|-------|---------|
| **A 入门→定稿** | 1. 入门 SOP（一支最小完整香水） | brief→palette→accord→结构 %→mods→稀释/陈化→评香→IFRA→定稿 | low | T03-S008/009/010/032/019 |
| | 2. 资深路径（大师怎么跳步/优化） | 凭嗅觉记忆从香风琴起手、心算挥发度金字塔、复用 accord 库、更少 mods | low | T03-S012/034/005 |
| **B 创作核心** | 3. B2B 四大竞标模型（核心） | core list→brief→creation→submission→mods→win/lose（消费者测试定胜负） | medium | T03-S005/003/006/001 |
| | 4. 评香师（evaluator）中间角色 | 解码 brief、每日嗅评、带回客观性、panel test、客户反馈回灌 | medium | T03-S001/002/007/035 |
| | 5. brief 怎么写/怎么 review | incoming→executive brief 双段；7 类必含要素；越早交底越快 | medium | T03-S003/004 |
| **C 流派分裂** | 6. niche / indie 工作流 | 自供原料、从灵感非命题起、直营、不走竞标、手工小批 | low | T03-S027/028/029 |
| **D 培养/传承（元工作流）** | 7. 学院 pipeline（ISIPCA/GIP） | 对外开放、800/1200h、原料+accord+化学+GC-MS+实习 | low | T03-S016/017/018 |
| | 8. 四大内部学校 + 学徒制 | 仅员工、年收个位数、训 4 年、先背 ~500 原料 | low | T03-S015/018 |
| | 9. 「the nose」tacit 校准 SOP（Jean Carles 法） | 盲嗅背料→相似/对比→deformulation 还原；半小时/日雷打不动 | low | T03-S011/012/013/014/034 |
| **E 评价/QC/法规/重配** | 10. 评价/QC 工作流 | 盲评、panel testing、稳定性（加速/光照/冻融/实时）、留香/sillage | medium | T03-S030/031/007 |
| | 11. IFRA / allergen 合规校验工作流 | 上市前硬闸门：按 category 算累积暴露 + 致敏原标签（标版本） | medium | T03-S019/020/021 |
| | 12. reformulation（重配）工作流 | 经典香水因 IFRA/EU 修订被迫重配的流程与张力（oakmoss/atranol） | medium | T03-S022/023/024/033 |
| **F 近期变化（decay 最快）** | 13. AI 配方生成改写创作流 | Carto/Philyra/Codex/Scentmate 在 brief→creation 段辅助（不决策） | high | T03-S025/026 |
| | 14. headspace 活体捕香 / captive / 发酵法 对选型的影响 | 现场捕香重建 accord、专利分子差异化、发酵分子改写"天然 vs 合成"选型 | high | T03-S030/(交叉 02-tools #16/#18) |

---

# A. 入门 → 定稿

## 1. 入门 SOP：一个新手完成「一支最小完整香水」的最少步骤链

> **链路（每步落到具体动作）**。配比数字**各家口径不同**，下列为入门教程常见起步值，仅作锚、非定律（caveat：约定俗成各家不同）。

1. **The brief（命题）**：先给自己一个命题——一种记忆/地点/情绪/家族目标（如「清新柑橘古龙」「温暖琥珀木质」）。indie/学习者常**从灵感起**而非外部 brief（与 #6 对照）(evidence: [T03-S027])。
2. **选 palette / 原料**：从一组有限的入门原料里挑（天然 EO/absolute + 合成 aroma chemicals）。新手不要一上来 500 瓶，先掌握小调色板（呼应 02-tools #1 调色板 + #7 indie 供应商 kit）。查每料气味/强度/安全用 TGSC（02-tools #4）。
3. **搭 accord 和弦**：把 2–若干个原料按比例融成一个**不可拆分的气味单位**（accord = 创作的「单词」，5–12 料，决定家族归属，见 04-canon T04-S040）。**起步只滴几滴、逐步加量、边调边试**，记录每次配比 (evidence: [T03-S009])。
4. **配方结构（top/heart/base + % 浓度）**：按挥发度把原料分进三层金字塔。入门教程常见起步配比（**全部 caveat：各家不同**）——例如「top 30% / heart 50% / base 20%」按滴数，或「base 25% / heart 45% / top 30%」等多种说法并存 (evidence: [T03-S008])。香精浓度（concentrate 占成品 %）按等级：parfum ~20–30% / EDP ~15–20% / EDT ~5–15% / EDC ~2–5%（caveat：约定俗成、各家不同，见 02-tools T02-S037）。
5. **trials / mods 试样迭代**：按**重量**称量（0.01g 起步，高效力分子先配 10% 母液再精称，见 02-tools #2/#12），做多个版本编号、闻香纸比对、调整、再称——反复。轮数无定数（入门可能十几轮；商业大作可达 **128 版**，见 04-canon T04-S031 «The Perfume Lover» 纪实）(evidence: [T03-S010])。
6. **稀释 / 陈化（maceration）**：把 concentrate 稀入乙醇（perfumer's alcohol/DPG）到目标浓度，**静置陈化**让分子融合稳定。常见 EDP 静置 **~1 个月起**、复杂配方 **1–3 月**（个别到 6 月）；陈化前后气味差异大，跳过会误判留香 (evidence: [T03-S010, T03-S032])。
7. **评香**：闻香纸 + 上皮肤 + 旁人嗅评三处评估，追踪 top→heart→base dry-down（02-tools #3）。
8. **IFRA / allergen 合规校验**：上市前用内建 IFRA 检测的软件按产品 category 算每料上限 + 出致敏原标签（见 #11）。天然 EO 不豁免 (evidence: [T03-S019])。
9. **定稿**：锁定配方版本、记录可缩放公式（相对重量/mg，可按产量复现，见 02-tools #2）。

- **可信度**：medium-high（入门 SOP 结构在多源一致；具体配比数字是教程口径、已标 caveat）。
- **Decay risk**：**low**（入门链路是行业地基，24+ 月稳）。last_checked 2026-06-08。

## 2. 资深路径：大师怎么跳步 / 优化

- **凭嗅觉记忆直接从香风琴起手**：资深调香师脑中有上千原料 + 经典香气的嗅觉记忆，可直接「想象」目标气味再翻译成配方，而非盲目试错——Kurkdjian「不是混原料，是在脑中构想再翻译成实体 / 讲故事」(01-figures T01-S013)；Ellena「能用两个原料做出一支就收手」(04-canon T04-S016)。
- **心算挥发度金字塔 / 按比例搭而非凭猜**：Jean Carles「Split」把每料按**挥发度 + 嗅觉家族**预先分类，使大师能「按比例构建、而非靠猜」、先判两料最佳平衡再逐步加料平衡 accord 间关系 (evidence: [T03-S034])。
- **更少 mods**：经验让资深者更快收敛、更早知道「何时停手」——好的 evaluator 能成为「你鼻子的延伸」，让调香师「更自信地知道何时停」(evidence: [T03-S002])。
- **从 accord 库 / performing formula 复用**：商业语境下，perfumers 常**不从零创新**，而是「找一个以前可能合适的 trial」「把各自独立开发的 accord 喂进同一配方」——尤其当 brief 偏模糊时 (evidence: [T03-S005])。
- **可信度**：medium（大师"跳步"多为其对外访谈 + 业内描述，非内部实录）。**caveat**：与「每支都是全新创作」的浪漫叙事有张力——业内真相更接近「复用 + 微调 performing formula」(evidence: [T03-S005])。
- **Decay risk**：**low**。last_checked 2026-06-08。

---

# B. 创作核心（B2B 命题创作）

## 3. B2B 四大香精公司创作模型（核心）：core list → brief → creation → submission → mods → win/lose

> 商业「fine」香水自工业化、全球化以来，此机制**数十年未变**，是本行最核心的工作流 (evidence: [T03-S005])。

1. **core list（核心供应商名单）**：品牌**不**把 brief 发给所有香精公司，只发给 **core list 上 3–4 家** accredited 香精公司——进名单靠「excellence + 财务安排（折扣 + 持续商务谈判）」，小独立厂无议价权进不去（caveat：3–4 家为业内估，各品牌不同）(evidence: [T03-S005, T03-S006])。
2. **the brief（命题下达）**：品牌（时装屋/大集团）把 brief 同时发给这几家**互相竞争**的香精公司 (evidence: [T03-S006])。
3. **creation（内部创作 + 内部竞争）**：每家公司内，**evaluator 分派多名内部 perfumer** 接同一 brief；他们**多从已有的「performing formula」骨架出发、twist 成贴 brief**；公司内部还会「互相讨论、把各自的 accord 喂进同一配方」帮彼此 (evidence: [T03-S005])。同一 brief 下多 perfumer 竞争，但「大家都希望自己团队赢」(evidence: [T03-S007])。
4. **submission（提交）**：每家公司向客户提交候选样。客户**每家香精公司保留 1–2 个提案** (evidence: [T03-S005])。
5. **mods（修改迭代）**：保留的提案在 panel/artistic director 指导下反复修改（mods），并反复**回看 client brief + 原始 moodboard** 确认方向没跑偏 (evidence: [T03-S002, T03-S006])。此过程**数月到数年**、多轮迭代，可能跨多国做消费者测试 (evidence: [T03-S006])。
6. **win / lose（竞标定胜负）**：保留提案进**多国消费者测试**，结果定**最终赢家**——赢的那家负责生产 + 交付 (evidence: [T03-S005])。
7. **经济结构（关键张力）**：香精公司**开发期不收费**，development 成本自担、不赢就没钱；classical 公司里 perfumer 是**领薪员工**、拿与「其配方产生的 turnover 挂钩的奖金」——故有强动机赢尽量多项目、做「最 consensus 的配方」(evidence: [T03-S005])。表现不佳的公司，品牌可「次年直接把它从 core list 剔除」(evidence: [T03-S005])。
- **可信度**：medium-high（Nez 是行业内出版物 own publication，描述细致；具体家数/比例为业内估，已 caveat）。
- **矛盾保留**：此「竞标 + 复用 performing formula + consensus 配方」的工业真相，与 niche/indie「作者性 + carte blanche + 不盲测」(见 #6) 是**结构性对立**；也与大师访谈里「每支都是独一无二艺术创作」的叙事有张力——**两者并存、不和稀泥**。
- **Decay risk**：**medium**（机制本身极稳；但 AI（#13）正改写 creation 段的速度与方式）。last_checked 2026-06-08。

## 4. 评香师（evaluator）在中间的角色

> evaluation 这个职业 **1970s 末**因品种/需求/趋势剧增而被引入，专门支撑 perfumer 的创作 (evidence: [T03-S007])。

- **解码 brief**：evaluator 是 client 与 perfumer 之间的**中介/「顾问」**，把 client brief「解码、翻译给 perfumer」、吃透品牌 portfolio（heritage/values/products），确保切题 (evidence: [T03-S001])。独立 evaluator 自述：「有时我是 client 用自己的话想要的东西、与 perfumer 之间那个**缺失的环**——我去翻译，但因为我懂香精公司和 perfumer 怎么运作，我翻译的方式不一样」(evidence: [T03-S035])。
- **assign + 每日嗅评**：分派 perfumer 接 brief；**每天闻前一天的 work**、和 perfumer 一起决定接下来还需做什么 work (evidence: [T03-S001, T03-S007])。
- **带回客观性**：perfumer「离开发太近」，evaluator 的核心价值是**把客观性 + 语境带回**这个「无情地主观」的创作过程；好 evaluator 能成为「你鼻子的延伸」，让 perfumer 做出更好的香、也更自信地知道**何时停手** (evidence: [T03-S002])。
- **submission 前评估**：提交客户前，会在**成品基质里**评估气味，再视产品在**水/皮肤**等条件下评估 (evidence: [T03-S007])。
- **panel testing + 反馈回灌**：组织**消费品的感官评估（panel test）**；把客户意见收集回来、传达给 creators 以指导其 work；反复回看 brief + moodboard (evidence: [T03-S001, T03-S007])。
- **其他职能**：管 reference 收藏（parfumothèque）、分析消费趋势、与 marketing 协作、确保达标 + 合规 (evidence: [T03-S001])。
- **可信度**：medium-high（GIP 学校官方页 + 行业媒体；P&F 正文 403 取 search 摘要，已标）。
- **Decay risk**：**medium**。last_checked 2026-06-08。

## 5. brief 怎么写、怎么 review

- **双段结构（incoming → executive brief）**：client 提交 **incoming brief**；香精公司 R&D 把它**「解码再重编为 executive brief」**——这份新文档在配方优化期**绑定 perfumer 与 chemist** (evidence: [T03-S003])。
- **brief 必含 7 类要素** (evidence: [T03-S003])：
  1. 产品定义（何种香品：香水/化妆品/家居）
  2. 目标消费者
  3. 品牌定位（包装/讯息/价值观）
  4. 创意灵感（情感驱动 + 感官参照，常含 moodboard）
  5. 技术规格（嗅觉 profile / dosage / 性能指标 / 法规合规）
  6. 市场策略（地域 / 渠道 / 零售形态）
  7. 项目时间线（截止日，协调各部门）
- **核心原则**：「为缩短 time-to-market，必须从一开始就共享所有可得的嗅觉 + 理化要求 + 市场/战略线索」——上游透明防延误、保证跨部门（不同专长）对齐 (evidence: [T03-S003])。
- **brief 的「黄金中间地带」**：理想 brief = 清楚传达最关键面向、**同时给 perfumer 艺术诠释留足创作余地**——太死板/太空泛都坏 (evidence: [T03-S004])。
- **可信度**：medium（Moellhausen 为香精供应商 vendor docs，结构权威；Alpha Aromatics 二手补充）。
- **Decay risk**：**medium**。last_checked 2026-06-08。

---

# C. 流派分裂

## 6. niche / indie / artisan 工作流（与 B2B 的根本差异）

- **从灵感起、非命题起**：商业香常**从 marketing brief + 消费者投射**起；独立调香师**典型从灵感起**——一段记忆/一个地方/一种情绪 (evidence: [T03-S027])。
- **自供原料 + 直营 + 不走竞标**：indie 不进 core list、不竞标；可用**小批稀有原料**、亲手称量/混合/灌装；直接面向消费者讲故事（DTC 与大牌「站同一起跑线」）(evidence: [T03-S027])。
- **更长创作周期**：niche 把重心放在嗅觉本身，单支香常投入**「有时超过一年」** (evidence: [T03-S027])。
- **IAO「artisan」三条件**（Institute for Art and Olfaction 定义）：① perfumer **本人写了初始配方**、② **拥有/共有发布该香的品牌**、③ **保有配方的法律所有权** (evidence: [T03-S027, T03-S029])。
- **进圈路径分叉**：产业路径（进四大/香精公司）vs indie 替代路径（自学 + 独立教育 + 自建品牌）——Karen Gilbert 等专门为 artisan/独立调香提供可得教育 (evidence: [T03-S028])。
- **矛盾保留（关键）**：indie「作者性 + carte blanche + 创作自由」(01-figures 关键词 7：Tauer/Aftel/Malle/Nagel) ⇄ B2B「竞标 + consensus 配方 + 复用 performing formula」(#3) 是本行**两套创作世界观**，下游 synthesis 须并置不调和。**caveat**：多位大师**横跨两端**（Ropion 同做 Malle niche 与 Lancôme 商业；Kurkdjian 既是 indie 创始人又掌 Dior）——不是非此即彼，而是同一人在不同约束下切换工作流 (01-figures Phase 2 分歧 3)。
- **可信度**：medium（定义来自 IAO/Artisan Insider；indie"自由"叙事本身亦有营销成分，见 01-figures 争议）。
- **Decay risk**：**low**。last_checked 2026-06-08。

---

# D. 培养 / 传承 pipeline（元工作流）：「the nose」是怎么一步步练出来的

## 7. 学院 pipeline（对外开放）：ISIPCA（凡尔赛）/ GIP（Grasse）

- **ISIPCA**：1970 Guerlain 创办的凡尔赛香水学校，法系最权威学府；MSc 教 **800 个原料** + key accords + 香料化学 + 香水史 + 市场 + IFF 实习；需理科背景（caveat：学费/门槛见 04-canon T04-S035）(evidence: [T03-S016, T03-S018])。
- **GIP（Grasse Institute of Perfumery）**：2002 Prodarom 创办，**对外开放**（约 12 人/班）；International Technical Degree = **18 月 + 6 月实习 / 1200 培训小时**（600h 持证调香师/专家授课 + 600h 实操 + 工厂参观）；**英文授课、无需化学背景**；系统教原料/accord/家族识别/调和/**GC-MS**/法规/功能香精 (evidence: [T03-S017, T03-S018])。
- **路径定位**：学院路径是「the nose」可得化的入口（vs 四大内部学校闭源精英路径，见 #8）。
- **可信度**：high（学校官方 syllabus + Nez 教育全景）。**Decay risk**：**low**（机构长青）。last_checked 2026-06-08。

## 8. 四大内部学校 + 学徒制（闭源精英路径）

- **Givaudan Perfumery School**：Jean Carles **1946** 于 Roure 创办的传奇内部学校，**4 年制、仅限已被录用为 Givaudan 调香师者**；先**记忆约 500 个原料**，含国际实习 + 导师制 + 原料产地考察；教学法**至今部分基于 Jean Carles method**，由 Calice Becker（J'adore）更新主理（caveat：「培养市场约 1/3 香水的调香师」「现任校长」「500 原料」为厂商自述/业内估，见 04-canon T04-S034）(evidence: [T03-S015, T03-S018])。
- **稀缺度**：Givaudan Argenteuil 学校**年均仅收约 3 名学员、训练 4 年**——极窄漏斗 (evidence: [T03-S018])。
- **其他内部学校**（IFF/Symrise/Mane/DSM-Firmenich）：**须先入职方可申请**，公开信息稀薄——这是「公开知识体无法代表行业完整 know-how」的核心证据 (evidence: [T03-S018])。
- **学徒制本质**：师从导师、在岗反复闻料 + 接真实 brief/mods，把 tacit 校准嵌进日常生产。
- **可信度**：medium-high（机构层 high；数字层 medium，已 caveat）。**Decay risk**：**low**。last_checked 2026-06-08。

## 9.「the nose」tacit 校准 SOP（Jean Carles 嗅觉训练法）

> 嗅觉**无书面记法**，唯一路径是结构化重复闻料；「任何人都能练出高度发达的嗅觉，这纯属练习问题」——职业调香师**严守每天半小时**测试自己对原料的认识 (evidence: [T03-S011])。

**三阶段训练 SOP**（Jean Carles method）：
1. **盲嗅背料（memorization）**：把一组精选必备原料（天然 + 合成）放闻香纸上**盲嗅**，日复一日，直到能**毫不犹豫即刻识别**每一个「note」；并学会区分嗅觉上相近者（不同 rose oxide / 多种合成 musk），为每料写个人笔记（character/强度/留香/独特面向）(evidence: [T03-S011])。
2. **相似 → 对比（similarity then contrast）**：先**按相似性**闻（熟悉主题与层次：如 floral 列里 rose/jasmine…），再**按对比**闻（扩大记忆容量、揭示意外互补）——研究气味间关系、扩充嗅觉词汇。经典做法：**60 个 odorants 按 class 排表**，先学 class 间对比（floral/woody…），再学 class 内对比 (evidence: [T03-S011])。
3. **deformulation 还原（deconstruction & reconstruction）**：给一支**成品香水**，只凭鼻子 + 积累的知识**重建它**——做几十个 trials、逐步精炼配方直到逼近 target (evidence: [T03-S011])。
- **香风琴（orgue）配合**：500–1500 瓶料半圆环绕工位（02-tools #13 / 04-canon T04-S039）；自底向上建香（先 base 再 heart 再 top，与挥发度金字塔对应，04-canon T04-S033）。
- **AI 不替代**：没有捷径替代反复闻料；数字嗅觉/AI（#13）能辅助但不能替代人鼻校准（02-tools #13/#17）。
- **可信度**：medium-high（方法在多源一致；Bois de Jasmin 深度页 fetch 遇 bot 墙，取 search 摘要，已标）。
- **Decay risk**：**low**（百年量级方法论）。last_checked 2026-06-08。

---

# E. 评价 / QC / 法规 / 重配

## 10. 评价 / QC 工作流（盲评 / panel / 稳定性 / 留香）

- **盲评 + panel testing**：evaluator/perfumer 盲嗅评估；组织**消费品感官评估 panel**；measure 留香（longevity）/ sillage（拖尾）/ diffusion（扩散）等性能指标——直接影响消费者满意 (evidence: [T03-S031, T03-S007])。
- **稳定性测试 SOP**（上市前）(evidence: [T03-S030]):
  1. **加速测试**：升温模拟较短期内的老化；
  2. **光照测试**：受控光源含 UV；
  3. **冻融循环**：反复冻-融评估物理变化；
  4. **实时测试**：常温放置较长期（贯穿 shelf life）。
  - 测什么：**香型 profile 变化 / 色与澄清度（spectrophotometer）/ 物性（黏度等）**；外加**微生物测试**（菌/酵母/霉）(evidence: [T03-S030, T03-S031])。
- **陈化（maceration）作为前置**：稳定性/留香判断须在 maceration 后做（新调 ≠ 陈化后，见 #1 步 6 / 02-tools #12）。
- **可信度**：medium（ILT 为检测实验室 vendor docs；性能指标口径行业通用）。
- **Decay risk**：**medium**。last_checked 2026-06-08。

## 11. IFRA / allergen 合规校验工作流（上市前硬闸门）

- **不可跳过的闸门**：按 **IFRA Standards**（Prohibition / Restriction / Specification 三类）逐料算最大用量；当前为 **IFRA 51st Amendment**（caveat：限用浓度**随修订版变**，引用必标版本号）+ QRA2 按产品 **category** 算累积暴露 (evidence: [T03-S019])。
- **致敏原标签**：EU **Reg (EU) 2023/1545** 把可申报致敏原 **26 → 80+**（约 82，含分组），**2026-07-31 新品强制、2028-07-31 旧品退市**——2026 正是落地年，直撞本 skill 时点 (evidence: [T03-S020, T03-S021])。
- **执行动作**：用内建 IFRA 检测的配方软件算某料在 Cat 4(fine fragrance)/Cat 12(candle) 等上限、生成 IFRA certificate、导出致敏原标签（02-tools #6）。**天然 EO 不豁免、与合成同等受查** (evidence: [T03-S019])。
- **可信度**：high（IFRA 协会 originator + EU 立法原文 verified）。
- **Decay risk**：**medium**（「必须做 IFRA 校验」low；版本数字 high）。last_checked 2026-06-08。

## 12. reformulation（重配）工作流——近期高频变化点

> reformulation = 因**法规 / 成本 / 供应**被迫修改既有配方 (evidence: [T03-S033])。香水这行最大压力源是 **IFRA / EU 致敏原修订**。

- **触发**：IFRA 限用某料 → 经典香水被迫重配。**oakmoss（橡苔）**：IFRA 自 **1988** 起限用、**2001** 限至成品 **0.1%**（caveat：IFRA 历次修订版本，数字按当时版本）——oakmoss 是 chypre 的灵魂 + 天然定香，限用直接动经典结构 (evidence: [T03-S022])。
- **重配流程与张力**：
  1. 识别超标料（oakmoss/atranol、某些 allergens）；
  2. 找**替代/重构原料**——Guerlain **自育并专利了符合 IFRA 皮肤学标准的 oakmoss 品种**，且**「重构 oakmoss」据称花了至少 10 年**开发（caveat：厂商自报）(evidence: [T03-S022]);
  3. 用替代料**重搭 accord**、尽量保留原香性格；
  4. 重过 IFRA/EU 校验 + 稳定性测试 + 评香。
- **经典案例**：**Chanel No.5**（原富含 oakmoss + 天然 ylang，重配后更 transparent、aldehyde 柔化、用合成 musk）；**Mitsouko**（Guerlain 约 **2007–2008** 才显著降 oakmoss，2005 瓶仍含较多、2008 瓶几无）(evidence: [T03-S022, T03-S024])。
- **核心张力**：**创作自由/经典完整性 ⇄ 安全合规** 是结构性矛盾；vintage vs reformulation 之争是社区高频议题（caveat：低-atranol 替代常挥发更快、丧失定香，故「持久」感下降，见 02-tools 避坑 T02-S039）(evidence: [T03-S023, T03-S024])。
- **可信度**：medium（媒体 + 香评博客 + 零售指南；具体年份/百分比已逐处标 caveat）。
- **Decay risk**：**medium**（reformulation 随每次 IFRA/EU 修订**持续触发**，是 decay 较快层）。last_checked 2026-06-08。

---

# F. 近期工作流变化（必写，decay 最快层，全部 Decay = high）

## 13. AI 配方生成怎么改写创作流程

- **介入位点**：AI 主要嵌在 **brief → creation** 段（不在最终评香/定稿）——加速生成候选、缩短迭代 (evidence: [T03-S025])。
- **各家系统**（四大内部、闭源，不对外）:
  - **Givaudan Carto**：在 brief→creation 段，**cross-reference 专利市场研究 + 化学 R&D + 客户数据 + 历史配方**于平板界面；会引 perfumer 走「意想不到的路径」（建议自然不会想到的原料配对）。Calice Becker 喻其为**「像 iPhone——把分散信息汇到一处，但不替 perfumer 做决定」** (evidence: [T03-S025, T03-S026])。
  - **Symrise Philyra**（与 IBM）：在 creation/ideation 段，分析公司**历史上数百位 perfumer 风格**找相似、生成新颖组合；David Apel：「Philyra 没有[人的局限]，能看遍我们雇过的数百位 perfumer……拿出新颖创作」(evidence: [T03-S025])。已产出**商业香水**（02-tools T02-S036）。
  - **IFF Codex / DSM-Firmenich Scentmate**：同类闭源 AI 辅助系统（02-tools #15）。
  - **Scentbird 等 DTC**：在 brief 段用 100 万+ 客户数据点做语义分析找偏好（不做最终决定）(evidence: [T03-S025])。
- **核心定性**：**AI 辅助、不取代「鼻子」**——最终评估/品味/accord 微调仍是人鼻 tacit 工作；行业内对「AI 是 friend or foe」仍有张力（02-tools T02-S036）。indie 几乎用不到这些闭源内部系统。
- **矛盾保留**：「AI 加速 + 复用历史配方」与「每支独一无二人手创作」叙事张力，与 #3 的「复用 performing formula」是同一条工业化主线的延伸。
- **可信度**：medium（闭源，多为厂商/媒体口径；P&F 会议报道为 verified）。
- **Decay risk**：**high**（>40%/12 月——各家系统快速迭代、命名/能力可能 12 月内变样；闭源使外部追踪难）。last_checked 2026-06-08。

## 14. headspace 活体捕香 / captive 专利分子 / 发酵法对配方选型的影响

- **headspace 活体捕香**：现场无损捕捉鲜花/活体顶空挥发物（static/dynamic headspace）→ GC 重建 accord，让「捕捉自然界不可萃取的气味」进入配方选型（与稳定性/QC 共用 GC-MS 平台，02-tools #8/#18）。底层 headspace 成熟，**AI 谱图识别**是新增量 (evidence: [T03-S030] 语境 + 交叉 02-tools #18)。
- **captive 专利分子**：四大用专利期内独占分子（Iso E Super 等历史轨迹）做**差异化签名**——选型时 pro 能用 captive、indie 用不到（02-tools #1/#15，04-canon T04-S038）。
- **发酵法可持续原料**：designer yeast 发酵造珍稀分子（檀香/ambrox/patchouli 替代，如 DSM Firsantol / Clearwood Prisma）**重写「天然 vs 合成」的成本/可持续/供应叙事**，直接影响配方选型（受气候/濒危限制的天然料被发酵分子替代）——但是否算「天然」在监管/认证（ISO 9235）上仍有分歧（02-tools #16）。
- **可信度**：medium（前沿 + 部分厂商叙事；本轨主述其**对工作流/选型的影响**，技术细节交 02-tools）。
- **Decay risk**：**high**（新分子持续出、份额数字快速变）。last_checked 2026-06-08。

---

## Phase 2 提炼提示

### 反复出现 ≥3 处都强调的「工作流原则」（候选 playbook 规则）
- **the brief → creation → mods 是商业创作的中枢循环**（出现于 T03-S003/005/006 + 04-canon Phase2 命题 4 + 01-figures Kurkdjian/Nagel）。
- **evaluator 是创作流的客观性闸门 + brief 翻译器**（出现于 T03-S001/002/007/035）——本轨新增的、被 figures/canon 低估的关键角色。
- **合规先于创作自由**：IFRA 版本 + EU 致敏原是上市前硬闸门，引用必标版本（出现于 T03-S019/020/021 + 02-tools 同结论）。
- **「the nose」靠反复闻料内化、无捷径**：Jean Carles 三阶段 + 每日半小时，AI 只辅助（出现于 T03-S011/012/034 + 02-tools #13/#17）。
- **按重量、可复现、可缩放 + 必须陈化**是配方落地的不可妥协前提（出现于 T03-S010/032 + 02-tools #2/#12）。

### 显著的工作流分裂（候选智识谱系条目，**保留不和稀泥**）
- **B2B 竞标工业流** vs **niche/indie 直营创作流**：core list + 复用 performing formula + consensus 配方 + 多国盲测定胜负 ↔ 从灵感起 + carte blanche + 不盲测 + 手工小批 + 自持配方。直通 intake「四大寡头 vs niche/indie」。**caveat：大师横跨两端**（同一人不同约束切换）。(evidence: [T03-S005 vs T03-S027])
- **AI 辅助流** vs **纯人工流**：Carto/Philyra 在 creation 段加速 + 复用历史配方 ↔ Jean Carles 反复闻料 + 人鼻最终定稿。「AI 是 friend or foe」业内未定论。(evidence: [T03-S025 vs T03-S011])
- **学院开放培养** vs **四大闭源精英培养**：ISIPCA/GIP 对外开放、1200h ↔ Givaudan 仅员工、年收 ~3 人、训 4 年。(evidence: [T03-S017 vs T03-S018])

### 新兴工作流信号（decay 最快）
- AI 配方生成（creation 段提速）~12–24 月可能显著改写迭代方式；发酵法选型 ~24–36 月（已商业化）；headspace+AI 谱图识别增量演进。基于 2024–2026 launch 节奏（02-tools 一致）。
- **reformulation 是持续触发层**：EU 2023/1545（2026-07 落地、2028 旧品退市）+ IFRA 后续修订，使重配工作流在 12–24 月内**反复被触发**——是「近期高频变化点」的实锤。

### 冷僻 / 信号薄弱（诚实边界候选）
- **触发「闭源诚实协议」**：香水**真实创作工作流**（四大墙内 brief→mods 实操 SOP、内部评香会、内部学校课表）**几乎无公开一手**——本轨 retained 14 个工作流元素**充裕**（不触发"数量不足"下限），但**一手厚度靠 surrogate**（学校 syllabus / IFRA 协会 / 调香师+评香师自有出版物 / 行业内出版物 Nez）支撑，真 verified_primary 仅 2 条（EU 立法 + P&F 会议报道）。粗一手率 = 16/35 ≈ **45.7%**，略低于 50%，**是 locale(en+fr) + 闭源双重压制的诚实反映、非数据质量问题**。
- **关键一手缺口**：① B2B 竞标的**命中率/赢单率**无可靠公开数字（只知机制，不知比例）→ 已标 caveat；② core list **家数（3–4）**、mods **轮数**、Givaudan「1/3 市场」「年收 3 人」均为业内估/厂商自报 → 逐处 caveat；③ 评香师每日 loop、内部学校课表的细节多经 GIP 学校页 + Nez + P&F（部分 403/付费墙取 search 摘要）间接观察。
- **fetch 受阻点（诚实标注）**：Bois de Jasmin（bot 墙）、P&F 部分正文（403/付费墙）未取回逐字全文，相关 claim 取 search 摘要并标——与 01-figures/04-canon 记录的同站受阻一致。
- **中文一手结构性偏薄**（intake warning）：本轨工作流 canon 几乎全 en+fr；中文世界以**培训机构/KOL 测评二手**为主（黑名单口径：知乎/公众号/百度/CSDN），**未纳入 manifest**。中文一手不是"少"，而是"几乎不存在于可引用的一手形态"——与 04-canon「30:1」失衡一致。

---

## 完成 checklist

- [x] 入门 SOP（brief→palette→accord→结构 %→mods→稀释/陈化→评香→IFRA→定稿，9 步落到具体动作）✅（#1）
- [x] 资深路径（嗅觉记忆起手 / 心算金字塔 / 复用 accord 库 / 更少 mods）✅（#2）
- [x] B2B 四大竞标模型（core list→brief→creation→submission→mods→win/lose + 经济结构）✅（#3，核心）
- [x] evaluator 中间角色（解码 brief / 每日嗅评 / 带回客观性 / panel / 反馈回灌）✅（#4）
- [x] brief 怎么写/review（incoming→executive 双段 + 7 类要素）✅（#5）
- [x] niche/indie 工作流（自供原料/直营/不竞标/从灵感起/IAO artisan 三条件）✅（#6）
- [x] 培养/传承 pipeline（学院 ISIPCA/GIP + 四大内部学校 + 学徒制 + Jean Carles tacit 校准 SOP）✅（#7/#8/#9）
- [x] 评价/QC 工作流（盲评/panel/稳定性加速·光照·冻融·实时/留香·sillage）✅（#10）
- [x] IFRA/allergen 合规校验工作流（标版本 + EU 2023/1545 落地）✅（#11）
- [x] reformulation 工作流（oakmoss/atranol、Mitsouko/Chanel No.5、张力）✅（#12）
- [x] 近期变化（AI 配方生成 / headspace 活体捕香 / captive / 发酵法选型）✅（#13/#14）
- [x] manifest ≥28 条（实得 35）+ 三 bucket 标注 + 一手率 + 黑名单 0 + Fragrantica/Basenotes 未冒充一手 ✅
- [x] 每个 surrogate_primary note 含白名单关键词（syllabus/课程/教材/education vendor/association/协会/originator/certification body/vendor docs/supplier/own publication/own site/critic own publication/regulator）✅
- [x] 数字带 source 或 caveat（配比%/浓度等级/留香/mods 轮数/竞标家数/训练年限/IFRA 版本/oakmoss 0.1% 均挂 source 或 caveat）✅
- [x] 矛盾保留不和稀泥（B2B 竞标 vs niche 直营；AI 辅助 vs 纯人工；学院 vs 闭源培养；复用 performing formula vs 独一无二叙事）✅
- [x] 与 01/02/04 交叉引用（accord/palette/Jean Carles/orgue/IFRA/GC-MS/captive/发酵法/figures 关键词）✅

---

> **给 Phase 1.5 / 主 agent 的一句话**：香水工作流的真中枢是 **B2B「core list → brief → creation → submission → mods → win/lose（多国盲测定胜负，开发期不收费、赢者制造）」+ 中间的 evaluator（brief 翻译器 + 客观性闸门）**，与 **niche/indie 直营创作流**结构性对立（大师常横跨两端）；培养侧是「**学院开放（ISIPCA/GIP 1200h）vs 四大闭源（仅员工、年收个位数、训 4 年）+ Jean Carles 三阶段 tacit 校准（盲嗅背料→相似/对比→deformulation 还原，每日半小时无捷径）**」；decay 最快层是 **reformulation（EU 2023/1545 2026-07 落地持续触发）+ AI 在 creation 段提速（Carto/Philyra「辅助不决策」）**。本轨已用 Surrogate Policy 把厚度堆到粗一手率 ~45.7%（16/35；verified 仅 2：EU 立法 + P&F 会议报道），**触发闭源诚实协议**：真实创作 SOP 在四大墙内不可得、竞标命中率等关键数字无公开源（已 caveat），中文一手结构性缺失——提炼工作流心智模型时，#3 竞标循环 / #4 evaluator / #9 Jean Carles SOP / #11 IFRA 闸门证据最硬，可优先承重。

*Generated 2026-06-08。候选探索 ~22 个工作流/SOP/pipeline，retained 14（A 入门→定稿 2 / B 创作核心 3 / C 流派 1 / D 培养传承 3 / E 评价QC法规重配 3 / F 近期变化 2）。所有 claim 带 last_checked=2026-06-08 + source_id 或 caveat。供 Phase 1.5 review。*
