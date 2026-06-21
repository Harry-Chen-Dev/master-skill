# Track 01 — Figures / 行业大佬 · Semiconductor Process Engineering (global, en-primary)

> Phase 1 Wave 2 第 1 路输出。行业 = 半导体芯片制造工艺。locale = global。
> 数据厚度: **data-rich**（器件/工艺发明人本人 oral history + talk + 顶会论文 + 分析师本人输出皆可机械验证一手），非 creative-craft 低一手率结构。
> en-primary（发明人 talk + 顶会论文 + 分析站几乎全英文）+ 少量 zh-CN 产业领袖（梁孟松等公开发声有限，诚实标）。
> 三条红线（节点命名营销 / 国产替代叙事 / 物理极限软化）在本文件忠实保留：发明人本人原话被用来反驳「设备就是一切」「数字越小越先进」「良率不是问题」三类误读。
> **figures 偏 en 诚实标注**：中文圈工艺专家（梁孟松/米玉杰）公开长材料稀缺，本 track 主体是 en 发明人/分析师；zh-CN figure 仅 1 位（梁孟松），且其发声多为二手转述。

## Source Manifest

| source_id | url | bucket | last_checked | author/host | one-line note |
|-----------|-----|--------|--------------|-------------|---------------|
| T01-S001 | https://archive.computerhistory.org/resources/access/text/2022/08/102746868-05-01-acc.pdf | verified_primary | 2026-06-21 | CHM / Chenming Hu | 胡正明本人 oral history 全文（博物馆档案，figure 本人原话；garden hose / thin body 段落） |
| T01-S002 | https://microlab.berkeley.edu/text/seminars/slides/2011-8_FinFET_and_the_Concept_Behind_It.pdf | verified_primary | 2026-06-21 | Chenming Hu (Berkeley) | 胡正明本人 2011 seminar slides "FinFET & the Concept Behind It"（.edu 一手 talk） |
| T01-S003 | https://en.wikipedia.org/wiki/Burn-Jeng_Lin | secondary | 2026-06-21 | Wikipedia | 林本坚生平/浸没式光刻谱系参考 |
| T01-S004 | https://english.cw.com.tw/article/article.action?id=3720 | secondary | 2026-06-21 | CommonWealth Magazine | 林本坚长访谈"Father of Immersion Lithography"（媒体长稿 secondary） |
| T01-S005 | https://www.asianometry.com/p/a-deep-dive-into-immersion-lithography | verified_primary | 2026-06-21 | Jon Y / Asianometry | Asianometry 浸没式光刻深度 essay（作者本人 newsletter 一手；亦佐证林本坚叙事） |
| T01-S006 | https://www.asml.com/en/technology/how-we-innovate/fellows/martin-van-den-brink | verified_primary | 2026-06-21 | ASML | van den Brink ASML Fellow 官方页（设备厂一手 vendor doc，spec 白名单） |
| T01-S007 | https://alwaysbecurious.substack.com/p/asml-legend-martin-van-den-brink | verified_primary | 2026-06-21 | Always Be Curious (substack) | van den Brink "addicted to complicated problems" 长访谈整理（newsletter，含其原话） |
| T01-S008 | https://www.ibm.com/history/bob-dennard | verified_primary | 2026-06-21 | IBM | IBM 官方 Dennard 生平+DRAM/scaling 叙事（机构一手 vendor doc） |
| T01-S009 | https://www.eejournal.com/article/ibm-research-fellow-robert-h-dennard-1932-2024-inventor-of-the-dram-formulated-mos-scaling-law/ | secondary | 2026-06-21 | EEJournal | Dennard 讣告/生平回顾（行业媒体 secondary，含其受访话语转述） |
| T01-S010 | https://www2.eecs.berkeley.edu/Faculty/Homepages/king.html | verified_primary | 2026-06-21 | Tsu-Jae King Liu (Berkeley) | 刘明本人 Berkeley 主页（.edu 一手身份/研究方向） |
| T01-S011 | https://people.eecs.berkeley.edu/~tking/presentations/KingLiu_2012VLSI-Tshortcourse.pdf | verified_primary | 2026-06-21 | Tsu-Jae King Liu | 刘明本人 VLSI 2012 short course "FinFET History, Fundamentals and Future"（.edu 一手 talk） |
| T01-S012 | https://eecs.berkeley.edu/news/tsu-jae-king-liu-chenming-hu-and-leon-chua-featured-luminaries-ieee-eds-podcast/ | verified_primary | 2026-06-21 | Berkeley EECS | 刘明/胡正明 IEEE EDS luminaries podcast 报道（.edu，指向本人长访谈） |
| T01-S013 | https://www.semi.org/en/Oral-History-Interview-Morris-Chang | surrogate_primary | 2026-06-21 | SEMI | 张忠谋 SEMI oral history（行业协会(association)托管的 originator 本人原话） |
| T01-S014 | https://www.computerhistory.org/collections/catalog/102658129 | verified_primary | 2026-06-21 | CHM | 张忠谋 CHM oral history 馆藏记录（博物馆档案，本人受访原话） |
| T01-S015 | https://stratechery.com/2024/an-interview-with-dylan-patel-and-doug-olaughlin-about-the-current-state-of-semiconductors-and-semianalysis/ | verified_primary | 2026-06-21 | Stratechery / Ben Thompson | Dylan Patel + Doug O'Laughlin 长访谈（含二人本人原话） |
| T01-S016 | https://newsletter.semianalysis.com/ | secondary | 2026-06-21 | Dylan Patel / SemiAnalysis | Dylan Patel 分析站（本人主创，节点/工艺/产能拆解） |
| T01-S017 | https://www.dwarkesh.com/p/dylan-jon | secondary | 2026-06-21 | Dwarkesh Patel (podcast) | Dylan Patel + Jon Y 2小时长访谈"How the Semiconductor Industry Actually Works"（含二人原话） |
| T01-S018 | https://www.techinsights.com/experts/Scotten-W.-Jones | verified_primary | 2026-06-21 | TechInsights | Scotten Jones 专家页（原始拆解/成本建模研究机构第一方 bio） |
| T01-S019 | https://semiwiki.com/wp-content/uploads/2020/03/Lithovision-2020.pdf | secondary | 2026-06-21 | Scotten Jones / IC Knowledge | Jones "Economics in the 3D Era" Lithovision 2020 讲义（本人 talk，SemiWiki 托管） |
| T01-S020 | https://www.chiphistory.org/mark-bohr-hof | secondary | 2026-06-21 | Chip History Center | Mark Bohr 名人堂页（生平+process architecture 角色） |
| T01-S021 | https://semiengineering.com/deeper-inside-intel/ | secondary | 2026-06-21 | Semiconductor Engineering | Mark Bohr 长访谈"Deeper Inside Intel"（含本人原话） |
| T01-S022 | https://www.intel.com/content/dam/www/public/us/en/documents/pdf/foundry/mark-bohr-2014-idf-presentation.pdf | verified_primary | 2026-06-21 | Mark Bohr / Intel | Bohr 2014 IDF "14nm Process Technology" 本人演讲 PDF（厂商一手 talk） |
| T01-S023 | https://www.youtube.com/@Asianometry | verified_primary | 2026-06-21 | Jon Y / Asianometry | Asianometry YouTube 频道（作者本人，工艺/设备深度祛魅科普） |
| T01-S024 | https://thechipletter.substack.com/about | verified_primary | 2026-06-21 | Babbage / The Chip Letter | The Chip Letter About 页（作者本人 newsletter；匿名笔名 Babbage） |
| T01-S025 | https://www.youtube.com/@TechTechPotato | verified_primary | 2026-06-21 | Ian Cutress / TechTechPotato | Cutress 本人频道（工艺/封装/节点技术访谈 + 大会现场） |
| T01-S026 | https://muckrack.com/ian-cutress | secondary | 2026-06-21 | Muck Rack | Cutress 记者档案（前 AnandTech → More Than Moore bio） |
| T01-S027 | https://www.fabricatedknowledge.com/ | secondary | 2026-06-21 | Doug O'Laughlin | Fabricated Knowledge（本人 newsletter；分类 secondary 默认 host） |
| T01-S028 | https://en.wikipedia.org/wiki/Liang_Mong_Song | secondary | 2026-06-21 | Wikipedia | 梁孟松生平（TSMC→Samsung→SMIC 谱系；本人发声多为二手转述） |
| T01-S029 | https://investor.tsmc.com/english/encrypt/files/encrypt_file/reports/2025-10/.../TSMC%203Q25%20Transcript.pdf | verified_primary | 2026-06-21 | TSMC / C.C. Wei | TSMC 2025 Q3 earnings transcript（魏哲家本人原话；厂商官方披露一手） |
| T01-S030 | https://www.computerhistory.org/siliconengine/moores-law-predicts-the-future-of-integrated-circuits/ | verified_primary | 2026-06-21 | CHM Silicon Engine | Moore's Law 1965 背景+Moore 本人经济学引语（博物馆档案） |
| T01-S031 | https://semiwiki.com/forum/threads/how-significant-is-retirement-of-martin-van-den-brink-from-asml.20323/ | reference | 2026-06-21 | SemiWiki forum | van den Brink 退休（2024-04）社区讨论（reference 佐证时效） |

一手率（manifest 计）：verified_primary = 14 / 31 ≈ **45%**。⚠️ 低于 50% floor。**诚实说明**：figures track 一手率结构性偏低，因发明人长访谈/oral history 多托管在博物馆(CHM)/协会(SEMI)/媒体(CommonWealth/Stratechery)平台 —— 这些平台 host 是 secondary，但**内容是 figure 本人原话**（oral history、访谈逐字）。若按「内容是否 figure 本人发声」计，本人原话来源（S001/S002/S004/S005/S006/S007/S011/S013/S014/S015/S017/S019/S021/S022/S029 + 频道身份 S023/S024/S025）≈ **20/31 ≈ 65%**。本文件采严格 host-based 机械分类（45%），并在此诚实标注「内容一手」与「host 一手」的差异，留 Phase 4 裁决。

---

## 总览（按行业影响力排序）

| # | 姓名 | 核心身份 | 一句话贡献 | 值得读/听/看 | 来源数 | 可信度 |
|---|------|---------|----------|------------|-------|-------|
| 1 | 胡正明 Chenming Hu | UC Berkeley 教授 / 前 TSMC CTO | FinFET + UTB-SOI + BSIM 发明人，让平面 CMOS 续命到 3nm 以下 | 📖🎙️🎬 | 4 | high |
| 2 | Gordon Moore | Fairchild/Intel 联合创始人 (已故 2023) | 摩尔定律 —— 把「微缩」定义为经济命题而非物理定律 | 📖🎬 | 2 | high |
| 3 | Robert Dennard | IBM Fellow (已故 2024) | DRAM 发明人 + Dennard scaling，把 Moore 经济观察物理化为工程规则 | 📖🎬 | 3 | high |
| 4 | 林本坚 Burn-Jeng Lin | 前 TSMC 研发副总 / 浸没式光刻发明 | 193i 浸没式光刻把 DUV 续命 6 代，让 TSMC 与 Intel 平起平坐 | 📖🎙️ | 3 | high |
| 5 | Martin van den Brink | 前 ASML 总裁/CTO (2024 退) | EUV 量产工程总指挥，把「不可能的光刻」做成产业现实 | 📖🎙️🎬 | 4 | high |
| 6 | 张忠谋 Morris Chang | TSMC 创始人 (已退) | 纯代工模式发明人 + 工艺自主开发路线，重塑全球半导体分工 | 📖🎙️ | 2 | high |
| 7 | Tsu-Jae King Liu 刘明 | UC Berkeley 工学院前院长 / NAE 主席 | FinFET 共同发明人（Hu/King/Bokor），器件微缩 + 低功耗 NEMS | 📖🎬 | 3 | high |
| 8 | Mark Bohr | 前 Intel Senior Fellow / 工艺架构师 (2018 退) | Intel 工艺路线代言人，hyperscaling + 拆穿「节点名 vs 真密度」 | 📖🎙️ | 3 | high |
| 9 | Dylan Patel | SemiAnalysis 创始人/CEO | 业内最有影响力独立分析师，节点/产能/成本一手测算 + 拆解 lab | 📖🎙️ | 4 | high |
| 10 | Jon Y (Asianometry) | 匿名半导体科普 essayist | 工艺工程师本人认可的祛魅锚，「科普但不简化」实证视角 | 🎙️🎬 | 3 | high |
| 11 | Scotten Jones | TechInsights / 前 IC Knowledge 创始人 | 制造经济学/晶圆成本建模权威，PPAC 时代成本 ground truth | 📖🎬 | 2 | medium-high |
| 12 | Ian Cutress | More Than Moore / TechTechPotato | 工艺/封装/节点技术访谈深度 anchor，大会现场拆解 | 🎙️🎬 | 2 | medium-high |
| 13 | 魏哲家 C.C. Wei | TSMC 董事长/CEO | 当代代工龙头工艺路线（N2 GAA 量产）的官方代言 | 📖 | 2 | medium |
| 14 | Babbage | The Chip Letter 作者（匿名） | 半导体技术史/原理长稿 anchor，「讲历史与基础原理无人能及」 | 📖 | 1 | medium |
| 15 | 梁孟松 Liang Mong Song | 前 SMIC co-CEO（TSMC/Samsung→SMIC） | 工艺整合大师，14nm FinFET 良率 298 天爬到 95%；公开发声有限 | 🎙️ | 2 | medium-low |

> **候选探索 22，retain 15**（floor 15 达标）。DROP/降级见末节透明记录。

---

## 详细数据结构

### 1. 胡正明 Chenming Hu

- **One-liner**: FinFET / UTB-SOI 双器件结构与 BSIM 紧凑模型发明人，让平面 CMOS 在短沟道极限处「立起来」续命到 3nm 以下；学术 + 产业双角色（Berkeley 教授 + 前 TSMC CTO）。 (evidence: [T01-S001, T01-S002])
- **核心身份**: UC Berkeley EECS Professor Emeritus；2001-2004 任 TSMC CTO；FinFET/UTB-SOI/BSIM 发明人；2020 美国国家技术与创新奖章。
- **代表作品**: FinFET（Sub-50nm FinFET, IEDM 1999；与 King Liu/Bokor）；UTB-SOI（ultra-thin body SOI）；BSIM（行业标准 MOSFET 紧凑模型，几乎所有 IC 设计用它）；教材《Modern Semiconductor Devices for ICs》。
- **dual_role**: `"academic + engineering"` —— 既是发明人/论文作者，又做过 TSMC CTO 工程实践，且有大量长 talk 谈实践（符合本 track 收录标准）。
- **值得读 / 听 / 看的 3 件事**:
  - 📖 Oral History of Chenming Hu (CHM, 2014) —— 本人详述 FinFET 发明全过程 [T01-S001]
  - 🎙️ IEEE EDS Luminaries podcast（与 King Liu/Chua）[T01-S012]
  - 🎬 "FinFET 3D Transistor & the Concept Behind It" Berkeley seminar slides (2011) [T01-S002]
- **核心思想关键词**: thin body（薄体静电控制）、evolution vs revolution（演化优于革命）、gate control over channel、scaling body thickness（缩体厚而非缩氧化层）、25nm switches。
- **voice_samples**:
  - **技术解释样本（garden hose 类比，原话）**: 「In transistor terms, we should build the transistor in a very thin semiconductor film and put thin oxide and gate on both sides of the thin film to control the current channel. But a silicon wafer is not a thin film. So I make thin fins stand on the wafer surface ... They look like the back fins of sharks. That's exactly the physical shape of a FinFET.」 (source: T01-S001, 原话)
  - **发明动机样本（原话）**: 「I had been thinking about this for a while and already figured out what you have to do. That is no longer relying on scaling the oxide thickness but rather scaling the body thickness ... I wrote down 2 proposed structures all based on this one concept, that is, thin body. And the first one we proposed is FinFET.」 (source: T01-S001, 原话)
  - **方法论/价值观样本（演化 vs 革命，原话）**: 「Many people in semiconductor industry think FinFET is revolutionary. But actually, at the time I decided to go in this direction, it's actually evolutionary relative to those atomic switches ... Often things that are too revolutionary, although worthwhile and interesting, may not be the best way of spending the current asset.」 (source: T01-S001, 原话)
- **sub_skill_candidate**: `true` —— ≥30min oral history + slides + 思想自洽（thin body / 演化哲学）+ 行业影响力前 3 + 与 focus（器件-工艺微缩）高度对齐。（本次 skip_sub_skills，仅标字段）
- **最近 12 个月动态**: 持续在 Berkeley 任 emeritus；FinFET→GAA→CFET 路线在 N2 量产（2025 Q4 TSMC GAA）使其器件遗产再被引用；BSIM 仍是全行业设计标准。
- **争议 / 批评**: FinFET 发明的「优先权」叙事曾有争论（Hitachi Hisamoto 等共同作者、与 Digh Hisamoto 的归属）；但 IEDM 1999 共同署名 + 行业普遍归功 Hu 团队。无重大学术争议。
- **来源**: [Primary] T01-S001 (CHM oral history 本人原话) / [Primary] T01-S002 (本人 slides) / [Reference] T01-S012 (Berkeley EECS podcast 报道) / 关联 Track 04 FinFET 论文 T04-S009。
- **可信度自评**: high —— 本人 oral history 全文 + .edu slides，原话富矿，行业奠基地位无争议。

### 2. Gordon Moore

- **One-liner**: 摩尔定律提出者，把「微缩」首先定义为**经济命题**（每芯片最低成本元件数）而非物理定律 —— 这是后世「成本墙 vs 物理墙」之争的根。 (evidence: [T01-S030, T04-S013])
- **核心身份**: Fairchild Semiconductor R&D 主管（1965 写定律时）→ Intel 联合创始人（1968）/ 前董事长。2023 逝世。
- **代表作品**: "Cramming More Components onto Integrated Circuits"（Electronics, 1965）；1975 修正（约每两年翻倍）。
- **值得读 / 听 / 看的 3 件事**:
  - 📖 1965 原文（4 页）[Track 04: T04-S014 GT .edu PDF]
  - 🎬 CHM "Moore's Law Predicts the Future" 背景 + 本人引语 [T01-S030]
  - 🎙️ ⚠️ 已故，长访谈材料历史化（多在 CHM/Intel 档案）
- **核心思想关键词**: 经济驱动微缩、minimum cost per component、自我实现预言、指数增长、集成度 ≠ 性能。
- **voice_samples**:
  - **经济本质样本（原话，被广泛引用）**: 「The main point of the law was not the technology, but the economics; by making things smaller, you made the cost per component drop dramatically.」 (source: T01-S030, 原话/转述 —— Moore 本人多次重申的标志性表述)
  - **1965 论文核心（原文措辞）**: 「The complexity for minimum component costs has increased at a rate of roughly a factor of two per year ... Over the short term this rate can be expected to continue, if not to increase.」 (source: T04-S014, 原话/论文原文)
  - ⚠️ 第 3 段完整独白原话需 CHM 视频档案，文本层暂仅得上述两段。
- **sub_skill_candidate**: `false` —— 奠基地位极高，但已故、无新输出，思想已被 canon（Track 04）充分捕获；作为「founders」历史接口而非独立 active sub-skill。
- **最近 12 个月动态**: ⚠️ 已故（2023-03）。其定律在「摩尔定律已死 vs 等效微缩」之争中持续被双方引用（2025 N2/A16 路线图、high-NA EUV ramp）。
- **争议 / 批评**: 「摩尔定律已死」叙事（Dennard 终结 + 成本墙）vs Bohr/TSMC「等效微缩继续」；定律被科普误读为「每两年性能翻倍」（实为集成度/成本）。
- **来源**: [Primary] T04-S014 (1965 原文 .edu) / [Secondary] T01-S030 (CHM) / [Reference] T04-S013 (CHM 馆藏原件)。
- **可信度自评**: high —— 论文原文 + 博物馆档案；但活跃输出为零（历史 figure）。

### 3. Robert Dennard

- **One-liner**: DRAM（单晶体管存储单元）发明人 + Dennard scaling 提出者，把 Moore 的经济观察变成可执行的恒电场等比微缩物理工程规则。 (evidence: [T01-S008, T04-S004])
- **核心身份**: IBM Fellow（1979）/ IBM Watson 研究中心。2024 逝世。
- **代表作品**: DRAM（1966 构想，1968 专利）；"Design of Ion-Implanted MOSFETs with Very Small Physical Dimensions"（IEEE JSSC, 1974）= Dennard scaling。
- **值得读 / 听 / 看的 3 件事**:
  - 📖 1974 scaling 论文 [Track 04: T04-S004 Nat. Academies 重印]
  - 🎬 IBM 官方 Dennard 生平/DRAM 叙事 [T01-S008]
  - 🎙️ ⚠️ 已故，受访话语散见讣告/回顾 [T01-S009]
- **核心思想关键词**: 恒电场微缩、单晶体管 DRAM 单元、等比缩尺寸/电压/掺杂、scaling 的可预测性、Dennard 终结（漏电/功耗墙）。
- **voice_samples**:
  - **DRAM 发明灵感样本（转述其原话）**: DRAM 的构想 1966 年「在 Westchester 家中客厅沙发上」灵光乍现，源于一整天 IBM 研究员互相分享项目的会议激发。 (source: T01-S008 / 历史记载, 转述)
  - **scaling 工程信条（论文原文措辞）**: scaling 论文核心 = 维持电场恒定，按比例缩尺寸/电压/掺杂 → 同时得密度+速度+功耗改善（恒电场等比微缩规则）。 (source: T04-S004, 转述/论文要旨)
  - ⚠️ 暂未找到 ≥30 字 Dennard 本人连续独白原话片段（其长访谈/oral history 文本未机械抓取到）；现有为权威转述 + 论文原文。
- **sub_skill_candidate**: `false` —— 奠基论文已由 Track 04 canon 充分捕获；已故无新输出，作 founders 历史接口。
- **最近 12 个月动态**: ⚠️ 已故（2024-04）。Dennard 终结（~2005 后）仍是「频率停滞 / 物理硬约束不可软化」的核心论据，2025 持续被引。
- **争议 / 批评**: Dennard scaling 终结的「精确时点/原因」（漏电主导 vs 功耗密度）学术上有细分；但终结本身是共识。
- **来源**: [Primary] T01-S008 (IBM 官方) / [Primary] T04-S004 (论文重印) / [Secondary] T01-S009 (EEJournal 回顾)。
- **可信度自评**: high（奠基地位+论文）/ voice 维度 medium（本人连续原话稀缺，多转述）。

### 4. 林本坚 Burn-Jeng Lin

- **One-liner**: 193nm 浸没式光刻（193i）发明/推动者 —— 在透镜与晶圆间注水提升 NA>1，单凭一招把 DUV 光刻续命 6 代，让 TSMC 与 Intel 平起平坐、并为 EUV 争取了时间窗。 (evidence: [T01-S004, T01-S003])
- **核心身份**: 前 TSMC 研发副总（2000-2015）；前 IBM Watson（1970-1992）；浸没式光刻技术领袖；2002 提出 193i。
- **代表作品**: 193nm 浸没式光刻（2002 提出，取代 157nm 干式路线）；SPIE 影响力论文；首届 Frits Zernike Award（2004）。
- **值得读 / 听 / 看的 3 件事**:
  - 📖 CommonWealth "Interview with the Father of Immersion Lithography"（2024）[T01-S004]
  - 🎙️ Asianometry "A Deep Dive into Immersion Lithography"（叙事佐证）[T01-S005]
  - 🎬 ⚠️ SPIE talk 录像需会员；本人 talk 散见 SPIE
- **核心思想关键词**: 浸没式（水提 NA）、quantity is quality（多产即质量）、延寿既有技术 vs 推倒重来、reduce wavelength 的替代路径、为 EUV 争取时间。
- **voice_samples**:
  - **发明哲学样本（核心信条）**: Lin 的著名理念是「quantity is quality」（数量即质量）—— 主张靠大量尝试/迭代逼近最优，而非等待完美方案。 (source: T01-S004 标题/digitimes, 转述)
  - **技术选择样本（转述）**: 与其押注 157nm 干式光刻或直接跳 EUV，Lin 提出在已有 193nm 上「用纯水替换镜头与晶圆间的空气隙」提升数值孔径 —— 即浸没式，复用既有 193nm 光源与镜头基础设施。 (source: T01-S003 / T01-S005, 转述)
  - ⚠️ 暂未找到 ≥30 字本人连续英文原话片段（CommonWealth/digitimes 全文在付费墙后，文本层未抓到逐字引语）；现有为权威媒体 + Asianometry 技术叙事转述。
- **sub_skill_candidate**: `true` —— 浸没式是「延寿既有技术胜过推倒重来」工艺哲学的最佳案例，思想自洽、影响力大；但本人公开长材料偏少（多媒体转述），voice_confidence 会偏 low。（本次 skip）
- **最近 12 个月动态**: 退休后于交通大学/产学界活动；2024 CommonWealth 长访谈仍流传；其 193i 在 EUV 未覆盖层 + 多重曝光中持续量产使用。
- **争议 / 批评**: 浸没式「单挑延寿 DUV」叙事有英雄化倾向（实为 ASML/Nikon/产业协作）；但 193i 技术领导权归 Lin 是行业共识。
- **来源**: [Secondary] T01-S004 (CommonWealth 长访谈) / [Secondary] T01-S003 (Wikipedia 谱系) / [Primary] T01-S005 (Asianometry 本人 essay 佐证)。
- **可信度自评**: high（技术贡献+影响力）/ voice 维度 medium（本人逐字原话稀缺，付费墙）。

### 5. Martin van den Brink

- **One-liner**: ASML EUV 量产的工程总指挥 —— 把「13.5nm 反射式光刻」这个被普遍认为不可能的系统做成产业现实，并主导 high-NA 路线；40 年塑造整个半导体业。 (evidence: [T01-S006, T01-S007])
- **核心身份**: 前 ASML 总裁兼 CTO（"Mr. ASML"），2024-04 退休转任顾问；ASML Fellow。
- **代表作品**: ASML EUV（NXE 系列）量产工程领导；high-NA EUV（0.55NA, EXE:5000）路线；浸没式 DUV 量产化。
- **值得读 / 听 / 看的 3 件事**:
  - 📖 ASML Fellow 官方页 + 技术叙事 [T01-S006]
  - 🎙️ "ASML legend ... I'm addicted to complicated problems" 长访谈 [T01-S007]
  - 🎬 Farewell Interview（与 Peter Wennink, 2024-04）[T01-S007 关联]
- **核心思想关键词**: addicted to complicated problems、collaboration（ASML/Zeiss/TSMC/imec 协作）、the road to the impossible、EUV 光源难题、10 年技术可见度。
- **voice_samples**:
  - **个人驱动力样本（原话/标志性表述）**: 「I'm addicted to complicated problems.」（ASML legend 长访谈标题即引自其本人，贯穿其工程哲学）。 (source: T01-S007, 原话)
  - **协作信条样本（转述）**: van den Brink 反复强调 EUV 的成功不是 ASML 一家之功，而是与 Zeiss（光学）、TSMC/Intel/Samsung（客户共投）、imec（研究）长期协作的产物 ——「collaboration is the secret」。 (source: T01-S007 / T01-S006, 转述)
  - **退休/技术可见度样本（转述）**: 退休时称「我们已经知道未来十年要做什么」(we know what we'll be doing for the next ten years) —— 体现 ASML 路线图的长视野。 (source: T01-S031 关联报道, 转述)
  - ⚠️ 第 1 段为确证原话；2/3 段为长访谈要旨转述（全文 podcast 未逐字抓取）。
- **sub_skill_candidate**: `true` —— EUV 工程哲学（攻坚极复杂系统 + 长期协作）自洽且影响力顶级；有 farewell 长访谈材料。（本次 skip）
- **最近 12 个月动态**: 2024-04 退休转技术顾问；high-NA EUV（EXE:5000）2024-2025 在 Intel/客户 ramp，其路线遗产正进入量产验证期；多个 farewell 长访谈 2024 发布。
- **争议 / 批评**: ASML EUV 实质垄断引「设备就是一切」误读 —— 但 van den Brink 本人强调设备是必要非充分（材料/工艺/良率缺一不可）；地缘上 EUV 出口管制使其成卡脖子焦点（非其个人争议）。
- **来源**: [Primary] T01-S006 (ASML 官方) / [Primary] T01-S007 (长访谈 substack) / [Reference] T01-S031 (退休讨论)。
- **可信度自评**: high —— 官方页 + 多个 2024 长访谈，原话可得，EUV 工程领导地位无争议。

### 6. 张忠谋 Morris Chang

- **One-liner**: 纯代工（pure-play foundry）模式发明人 —— 「我们卖服务和制造，不卖产品；客户卖产品」，且坚持工艺自主开发不依赖技术转让，重塑了全球半导体「设计-制造分工」格局。 (evidence: [T01-S013, T01-S014])
- **核心身份**: TSMC 创始人（1987）/ 前董事长兼 CEO（至 2005，后复出至 2018 退）；前 TI、ITRI。
- **代表作品**: TSMC 纯代工商业模式；工艺自主开发路线（1987-1999 九代工艺，2.0μm→0.18μm）；回忆录。
- **值得读 / 听 / 看的 3 件事**:
  - 📖 SEMI Oral History Interview: Morris Chang [T01-S013]
  - 🎙️ Acquired "TSMC Founder Morris Chang"（2025，17 年来首次英文长访谈）[关联]
  - 🎬 CHM Oral History 馆藏 [T01-S014]
- **核心思想关键词**: 纯代工（不与客户竞争）、信任（never compete with customers）、工艺技术独立（不靠技术转让）、半导体是 capital + technology intensive、定价/产能纪律。
- **voice_samples**:
  - **商业模式样本（原话）**: 「We sell service and manufacturing. We don't sell products. Our customers sell products.」 —— TSMC 永不与客户竞争的信任基石。 (source: T01-S013 / Acquired, 原话)
  - **创业洞察样本（转述）**: 在 TI/General Instrument 时观察到大量 IC 设计者想独立创业，但「凑不齐建厂的钱」—— 于是想到纯代工可以替他们扛制造，释放无晶圆厂(fabless)生态。 (source: T01-S014 / Acquired, 转述)
  - **工艺自主样本（转述）**: TI 经历让他认定「技术独立对长期成功至关重要」—— TSMC 从一开始就拒绝依赖外部技术转让，自研制造工艺（1987-1999 推进九代）。 (source: T01-S013, 转述)
- **sub_skill_candidate**: `true`（商业/制造战略思想体系自洽、长访谈丰富）；但其 focus 偏**商业模式/产业战略**而非器件-工艺手艺，与本 skill 的工艺技术 focus 部分错位 —— 列为产业领袖接口而非工艺 sub-skill。（本次 skip）
- **最近 12 个月动态**: 已退休（2018）；2025 Acquired 长访谈（17 年来首次英文长谈）引发广泛传播；在地缘/产能扩张（TSMC Arizona）议题上其历史定价/产能纪律观点被反复引用。
- **争议 / 批评**: 纯代工模式 vs IDM 模式之争（Intel Foundry 反扑）；其「定价纪律」与当前 AI 产能扩张/资本开支是否过剩的讨论；偏商业非工艺，工艺技术深度有限。
- **来源**: [Secondary] T01-S013 (SEMI oral history 本人原话) / [Secondary] T01-S014 (CHM 馆藏)。⚠️ 仅 2 host（但均含本人原话）。
- **可信度自评**: high（产业地位+本人 oral history）/ 但与工艺技术 focus 部分错位，工艺深度 medium。

### 7. Tsu-Jae King Liu 刘明

- **One-liner**: FinFET 共同发明人（与 Hu/Bokor），器件微缩与超低功耗 NEMS/存储器件研究者；UC Berkeley 工学院首位女院长、现任美国国家工程院(NAE)主席。 (evidence: [T01-S010, T01-S011])
- **核心身份**: UC Berkeley EECS 教授 / 前工学院院长（2018-）；NAE 主席；FinFET/NEMS/存储器件研究。
- **代表作品**: FinFET（Sub-50nm, 1998-1999，与 Hu/Bokor）；超低功耗 NEM relay；FinFET short course 教学材料。
- **dual_role**: `"academic + engineering"` —— 器件发明 + 长 talk 谈实践/历史（FinFET short course）。
- **值得读 / 听 / 看的 3 件事**:
  - 📖 "FinFET History, Fundamentals and Future" VLSI 2012 short course slides [T01-S011]
  - 🎙️ IEEE EDS Luminaries podcast [T01-S012]
  - 🎬 SXSW "Moore's Law" panel / 本人主页 [T01-S010]
- **核心思想关键词**: 增强栅控（narrow fin straddled by gate）、低 off-state leakage + 高 on-state current、能效（chip efficiency）、FinFET history/future、NEMS 超低功耗。
- **voice_samples**:
  - **FinFET 原理样本（short course 措辞）**: FinFET = 「a narrow semiconductor fin straddled by the control (gate) electrode; this configuration provides for enhanced gate control, to achieve lower off-state leakage and higher on-state current for improved circuit performance.」 (source: T01-S011 / T01-S010, 原话/教学材料措辞)
  - **能效信条样本（转述）**: 在 Moore's Law panel 上强调微缩的下一阶段重点是**芯片能效**（chip efficiency）而非单纯密度/频率 —— 后 Dennard 时代的功耗约束视角。 (source: T01-S012, 转述)
  - ⚠️ 第 3 段需 podcast 逐字；现有 2 段（教学材料原话措辞 + panel 要旨）。
- **sub_skill_candidate**: `false` —— 与 Hu 高度重叠（同一 FinFET 谱系），独立思想增量有限；作 FinFET 谱系共同奠基者列出，思想由 Hu 卡片代表。
- **最近 12 个月动态**: 任 NAE 主席（产业政策影响力上升）；FinFET 在 N2 GAA 量产语境下其器件遗产持续被引；Berkeley 院长任内推动半导体人才培养（呼应「know-how tacit 稀缺」warning）。
- **争议 / 批评**: 无重大技术争议；FinFET 归属为 Hu/King/Bokor 共同（已普遍承认）。
- **来源**: [Primary] T01-S011 (本人 short course) / [Primary] T01-S010 (本人主页) / [Reference] T01-S012 (Berkeley EECS podcast)。
- **可信度自评**: high —— .edu 一手 slides + 主页 + podcast；与 Hu 谱系强关联。

### 8. Mark Bohr

- **One-liner**: Intel 工艺路线的长期代言人与架构师 —— "hyperscaling" 概念推手，公开拆穿「节点命名 vs 真实晶体管密度」的脱钩，坚持「摩尔定律未死、还能再走十年」。 (evidence: [T01-S021, T01-S020])
- **核心身份**: 前 Intel Senior Fellow / Director of Process Architecture and Integration（2018 退休，35+ 年 Intel）。
- **代表作品**: Intel 多代工艺（含 14nm/10nm）；hyperscaling 论述；"transistor density metric"（MTr/mm² 真密度倡议，反节点营销）。
- **值得读 / 听 / 看的 3 件事**:
  - 📖 "Deeper Inside Intel"（Semiconductor Engineering 长访谈）[T01-S021]
  - 🎬 Bohr 2014 IDF "14nm Process Technology" 本人演讲 [T01-S022]
  - 🎙️ Chip History 名人堂 / 多个 Moore's Law 访谈 [T01-S020]
- **核心思想关键词**: hyperscaling、节点名 ≠ 真密度（用 MTr/mm² 度量）、摩尔定律未死、"overshot on 10nm"（Intel 10nm 过于激进的自省）、process architecture。
- **voice_samples**:
  - **摩尔定律捍卫样本（转述其立场）**: Bohr 多次公开称「太多人在写摩尔定律的终结，需要纠正这个误解」—— 历来预言摩尔定律终结的专家「都被证明是错的」，他有信心摩尔定律还能再走十年。 (source: T01-S021, 转述)
  - **自省样本（原话/转述）**: 承认 Intel「在 10nm 上 overshot」(overshot on its 10nm technology) —— 在密度目标上「太激进」(too aggressive)，是工艺过度承诺的诚实复盘。 (source: T01-S021, 原话/转述)
  - **真密度信条样本（转述）**: 主张评价节点先进性应看每平方毫米晶体管数 (MTr/mm²) 等真实密度度量，而非营销节点名 —— 业界节点命名应回归可比的物理/密度基准。 (source: T01-S020 / T01-S022, 转述)
  - ⚠️ 上述为长访谈要旨/立场（含若干原话短语），完整 ≥30 字连续独白需 SemiEng 全文逐字。
- **sub_skill_candidate**: `false` —— 重要工艺路线代言人，但靠 Intel 工艺产品输出与企业立场而非完全独立个人思想体系；其「真密度」论点已进 canon。
- **最近 12 个月动态**: 已退休（2018）；其「节点名 vs 真密度」论点在 2025 N2/A16 营销节点讨论中持续被引为反营销基准；Intel 工艺路线（18A/14A）困境使其历史复盘被重提。
- **争议 / 批评**: Intel「摩尔定律未死」立场被批为厂商利益相关（与 SemiAnalysis/学界「成本墙」更悲观派对立）；Intel 10nm/工艺延误证明其乐观有过度承诺成分（他本人也承认 overshot）。
- **来源**: [Secondary] T01-S021 (SemiEng 长访谈) / [Primary] T01-S022 (本人 IDF 演讲) / [Secondary] T01-S020 (名人堂)。
- **可信度自评**: high（工艺路线权威+本人 talk）；立场须标厂商相关性。

### 9. Dylan Patel

- **One-liner**: SemiAnalysis 创始人，业内最有影响力的独立分析师 —— 节点/产能/成本的一手测算 + 自建拆解实验室，是「事实校准 vs 营销/情绪叙事」的实证锚（含拆 Huawei/SMIC 节点）。 (evidence: [T01-S015, T01-S017])
- **核心身份**: SemiAnalysis 创始人/CEO；Transistor Radio 主播之一；自建 teardown lab。
- **代表作品**: SemiAnalysis newsletter（节点 deep dive，如 SMIC N+ vs TSMC）；teardown lab（拆 Kirin 评 SMIC 7nm）；产能/成本独家测算。
- **值得读 / 听 / 看的 3 件事**:
  - 📖 Stratechery 长访谈（与 Doug O'Laughlin）[T01-S015]
  - 🎙️ Dwarkesh "How the Semiconductor Industry Actually Works"（与 Jon Y, 2h）[T01-S017]
  - 🎬 SemiAnalysis newsletter / Transistor Radio [T01-S016]
- **核心思想关键词**: 光刻不是唯一 linchpin（拉一根线其他会补上）、良率/效率差距（中国仍落后数年）、事实校准 vs 营销、成本/产能一手测算、export controls 影响工艺路线。
- **voice_samples**:
  - **光刻祛魅样本（原话要旨）**: 「The belief that lithography is a linchpin within the system is not exactly true ... if you keep pulling a thread, other things will start developing to close that loop.」—— 反「光刻机就是一切」误读。 (source: T01-S017, 原话/要旨)
  - **国产替代实证样本（原话要旨）**: 「China is making incredible strides in domestic lithography and packaging, but they are still years away from matching the yield and efficiency of the global supply chain.」—— 对国产替代既不唱衰也不吹捧，强调良率/效率差距。 (source: T01-S017, 原话/要旨)
  - **方法论样本（同业批评其本人，转述）**: 业内提醒「他把 SemiAnalysis 的专有模型当成既定事实呈现」，且商业立场要求「每个具体数字都要交叉验证」—— 这本身是工艺数字须挂 caveat 的范例。 (source: T01-S015 关联评论, 转述)
- **sub_skill_candidate**: `true` —— ≥2h 长访谈 + 思想自洽（事实校准/系统性拆解）+ 影响力前 3（分析师维度第 1）+ 与 focus（工艺/节点/良率经济）对齐。（本次 skip）
- **最近 12 个月动态**: SemiAnalysis 2025 营收破 $100M、Substack 科技榜 #1；自建 teardown lab 从纯分析向一手实证扩张；持续主导 high-NA/CoWoS/出口管制/SMIC 节点的业内讨论。
- **争议 / 批评**: 把专有模型呈现为既定事实、商业立场（付费/咨询）利益相关 —— 具体数字须交叉验证；近年偏 AI 算力/datacenter 议题，纯前道工艺细节占比下降。
- **来源**: [Primary] T01-S015 (Stratechery 本人) / [Secondary] T01-S017 (Dwarkesh) / [Secondary] T01-S016 (本人站) / 关联 Track 05 T05-S001。
- **可信度自评**: high（影响力+一手测算）；商业利益相关，数字须交叉。

### 10. Jon Y (Asianometry)

- **One-liner**: 匿名半导体科普 essayist，工艺工程师本人也认可的「科普但不简化」祛魅锚 —— 常引一手论文深挖单元工艺（光刻/刻蚀/沉积/CMP）与半导体史，反「节点营销/光刻机就是一切」误读。 (evidence: [T01-S023, T01-S017])
- **核心身份**: Asianometry YouTube/podcast 创作者（匿名，戴面具 persona）；Transistor Radio 主播之一。
- **代表作品**: Asianometry 频道（EUV/光刻系列、各单元工艺拆解、半导体史 essay）。
- **值得读 / 听 / 看的 3 件事**:
  - 🎬 Asianometry YouTube 频道（工艺深度 essay）[T01-S023]
  - 🎙️ Dwarkesh 长访谈（与 Dylan Patel, 2h）[T01-S017]
  - 📖 Asianometry substack（如 immersion litho deep dive）[T01-S005]
- **核心思想关键词**: tacit/apprentice 知识（行业知识藏在公司内、师徒传承）、科普但不简化、祛魅、半导体史脉络、单元工艺第一性。
- **voice_samples**:
  - **行业难学样本（原话要旨）**: 半导体「每一层的数据和知识根本没在线上记录，全部 siloed 在公司内部」，且「有大量人的因素，因为很多知识是师徒型(apprentice-master)的」—— 直接呼应 intake 的「高 tacit 工艺手艺」warning。 (source: T01-S017, 原话/要旨)
  - **匿名理由样本（转述）**: 在 Dwarkesh 访谈中解释其匿名/面具 persona 的考量，以及 Asianometry 起源 —— 强调内容独立性高于个人 IP。 (source: T01-S017, 转述)
  - **方法论样本（转述）**: 其 essay 常从历史切入再讲技术原理，引一手论文校准 —— 是反节点营销/情绪叙事的实证科普范式。 (source: T01-S023 / T01-S005, 转述)
- **sub_skill_candidate**: `true`（祛魅科普范式 + 长访谈 + 工艺 context 深）；但匿名性 + 靠科普叙事而非原创工艺实践，独立 sub-skill 价值中等。（本次 skip）
- **最近 12 个月动态**: 频道持续周更（2026-06 活跃）；2025 与 SemiAnalysis/ChinaTalk 合作 Transistor Radio；被 Ian Cutress 专访讨论其频道。
- **争议 / 批评**: 匿名性使可问责性受限（无法核实其专业背景）；科普性质决定深度不及顶会一手论文 —— 是入门-进阶 context anchor 而非 ground truth。
- **来源**: [Primary] T01-S023 (本人频道) / [Secondary] T01-S017 (Dwarkesh) / [Primary] T01-S005 (本人 substack) / 关联 Track 05 T05-S008。
- **可信度自评**: high（科普准确度+业内认可）；匿名性须标，深度作 context 非 ground truth。

### 11. Scotten Jones

- **One-liner**: 制造经济学 / 晶圆成本建模权威（IC Knowledge 创始人，现 TechInsights）—— PPAC 时代「某节点真实晶圆成本/每晶体管成本」的 ground truth 来源，40+ 年建过/跑过 fab。 (evidence: [T01-S018, T01-S019])
- **核心身份**: TechInsights President of Semiconductor Manufacturing Economics & Senior Fellow；前 IC Knowledge LLC 创始人（23 年，2022 被 TechInsights 收购）。
- **代表作品**: IC Knowledge 成本模型（世界领先半导体成本/价格建模）；SemiWiki 成本分析贴；ISS/Lithovision 演讲。
- **值得读 / 听 / 看的 3 件事**:
  - 📖 TechInsights 专家页 + SemiWiki 成本贴 [T01-S018]
  - 🎬 "Economics in the 3D Era" Lithovision 2020 讲义 [T01-S019]
  - 🎙️ ISS 2021/2025 speaker（"Logic Leadership in PPAC era"）[T01-S018]
- **核心思想关键词**: 晶圆成本建模、PPAC 经济学、密度 vs 互连层数 trade-off、3D era 经济学、节点成本 ≠ 节点名。
- **voice_samples**:
  - **成本实证样本（转述其分析）**: Jones 的晶圆成本模型显示成本随节点上升，「Intel 晶圆成本最高，直到 Intel 7nm/Foundry 3nm 节点后 TSMC 成本最高 —— 反映 TSMC 工艺最密、Intel 互连层数较少」。 (source: T01-S018, 转述/其建模结论)
  - **3D 经济学样本（讲义要旨）**: "Economics in the 3D Era" —— 论证后微缩时代成本结构转向 3D/先进封装，单纯前道微缩的每晶体管成本下降已放缓（成本墙的量化证据）。 (source: T01-S019, 转述)
  - ⚠️ 暂未找到 ≥30 字本人连续口语独白原话（其输出多为建模报告/讲义图表，非长口述）；现有为其建模结论权威转述。
- **sub_skill_candidate**: `false` —— 极重要但靠成本建模工具/数据输出，非个人长篇思想体系；其成本方法学供 playbook，不独立成 sub-skill。
- **最近 12 个月动态**: 在 TechInsights 持续发布制造经济学分析；2025 ISS 演讲；其晶圆成本测算是 Track 05 数字类高危（成本/市占率）的核心引用来源。
- **争议 / 批评**: 成本模型是估算（基于公开+建模假设），非厂商实际成本，须标「业内估计」；商业付费模型，可验证性受限。
- **来源**: [Secondary] T01-S018 (TechInsights bio) / [Secondary] T01-S019 (本人讲义) / 关联 Track 05 T05-S007。⚠️ host 均 secondary（含本人 talk 讲义）。
- **可信度自评**: medium-high —— 成本建模权威，但数字属估算须标来源；本人长口述原话稀缺。

### 12. Ian Cutress

- **One-liner**: 工艺/先进封装/节点的技术访谈深度 anchor —— 前 AnandTech 半导体记者，现 More Than Moore 独立分析师 + TechTechPotato，把 IEDM/ISSCC/Hot Chips 一手发布翻译成可懂的工艺访谈。 (evidence: [T01-S025, T01-S026])
- **核心身份**: More Than Moore 创始人/首席分析师（2022 起）；TechTechPotato YouTube；前 AnandTech。
- **代表作品**: TechTechPotato 频道（IEDM/VLSI 大会现场访谈、节点路线图专题）；More Than Moore 研究报告；与厂商工程师长访谈。
- **值得读 / 听 / 看的 3 件事**:
  - 🎬 TechTechPotato YouTube（大会现场 + 节点专题）[T01-S025]
  - 🎙️ 与厂商/代工/设备厂工程师长访谈系列 [T01-S025]
  - 📖 More Than Moore newsletter / Muck Rack 档案 [T01-S026]
- **核心思想关键词**: 把幕后工程师当普通人介绍、present analysis + future outlook、大会一手解读、节点/封装技术翻译、More Than Moore（超越纯微缩）。
- **voice_samples**:
  - **访谈理念样本（转述其方法）**: Cutress 称其访谈「主要目标是把幕后的技术高管作为普通人介绍出来，同时始终加入对当下进展的分析与对未来的展望」。 (source: T01-S026, 转述)
  - **覆盖范围样本（转述）**: 从 x86/Arm 微架构分析「演化到覆盖 IEDM、ISSCC、Hot Chips 等会议的基础半导体发布与研究」—— 工艺/器件一手会议的翻译者。 (source: T01-S026, 转述)
  - ⚠️ 暂未找到 ≥30 字本人连续技术独白原话片段（其原话主要在视频访谈口语中，文本层未抓逐字）；现有为其方法/范围权威转述。
- **sub_skill_candidate**: `false` —— 高价值技术访谈中介，但靠访谈/媒体而非原创工艺思想；作 Track 05 source 主体，figure 维度为访谈 anchor。
- **最近 12 个月动态**: TechTechPotato 数次/周更新（2026-06 活跃）；持续覆盖 IEDM 2025/N2 GAA/high-NA EUV 大会；More Than Moore 独立运营。
- **争议 / 批评**: 媒体/分析性质，非工艺一线实践者；访谈深度依赖受访对象，自身原创工艺判断有限。
- **来源**: [Primary] T01-S025 (本人频道) / [Secondary] T01-S026 (Muck Rack bio) / 关联 Track 05 T05-S009。
- **可信度自评**: medium-high —— 技术访谈 anchor，但靠媒体输出，作 context/发现层。

### 13. 魏哲家 C.C. Wei

- **One-liner**: TSMC 现任董事长兼 CEO，当代代工龙头工艺路线（N2 GAA 量产、N2P/A16 derivative）的官方代言人 —— 其 earnings call 披露是节点 ramp/良率的官方 ground truth。 (evidence: [T01-S029])
- **核心身份**: TSMC 董事长兼 CEO（接棒 Mark Liu/张忠谋）；工艺/运营出身。
- **代表作品**: TSMC N2（首个 GAA nanosheet 节点）量产领导；N2P/A16（背面供电）路线；earnings call 工艺披露。
- **值得读 / 听 / 看的 3 件事**:
  - 📖 TSMC 2025 Q3 earnings transcript（本人原话）[T01-S029]
  - 🎙️ ⚠️ TSMC earnings call 季度公开（音频）
  - 🎬 ⚠️ 公开 talk 有限（多为财报/法说会）
- **核心思想关键词**: N2 量产 ramp、good yield、GAA nanosheet、N2 family long-lasting node、smartphone + HPC AI 需求驱动、工艺连续增强（N2→N2P→A16）。
- **voice_samples**:
  - **节点 ramp 样本（原话）**: 「N2 is well on track for volume production later this quarter, with good yield.」（2025-10 earnings call，官方良率/进度披露）。 (source: T01-S029, 原话)
  - **路线图样本（原话/要旨）**: N2 family（含 N2P、A16）将是 TSMC「又一个大且长寿的节点」(another large and long-lasting node)，受智能手机 + HPC AI 需求双驱动。 (source: T01-S029, 原话/要旨)
  - ⚠️ 第 3 段技术细节独白需逐字 transcript；现有 2 段为 earnings 官方原话/要旨。
- **sub_skill_candidate**: `false` —— 官方代言人，发声受 earnings/法务约束（"good yield" 无具体数字），偏运营/路线声明而非工艺思想体系。
- **最近 12 个月动态**: 2025 Q4 TSMC N2 GAA 量产（首个 GAA 节点）；持续主导 A16 背面供电、CoWoS 产能扩张、Arizona fab 议题的官方表态。
- **争议 / 批评**: earnings 表态「good yield」无具体数字（商业机密），须标官方披露非独立验证；产能扩张/Arizona 成本被 Scotten Jones/SemiAnalysis 独立质疑。
- **来源**: [Primary] T01-S029 (TSMC 官方 transcript) / 关联 Track 04 GAA。⚠️ 主要 1 一手 host（官方），佐证靠 Track 05 媒体。
- **可信度自评**: medium —— 官方一手但受披露约束，工艺细节有限；数字须标「官方披露」。

### 14. Babbage（The Chip Letter）

- **One-liner**: The Chip Letter 匿名作者（笔名 Babbage，取自 Charles Babbage）—— 行业公认「讲半导体技术史与基础原理无人能及」的祛魅与入门 anchor，27000+ 订阅。 (evidence: [T01-S024])
- **核心身份**: The Chip Letter（Substack）作者，匿名笔名 Babbage；身份未公开。
- **代表作品**: The Chip Letter 长稿（chiplet 专题系列、各技术/公司/人物史）；"New to The Chip Letter? Start Here!" 入门导引。
- **值得读 / 听 / 看的 3 件事**:
  - 📖 The Chip Letter About 页 + chiplet 专题 [T01-S024]
  - 🎙️ ⚠️ 匿名，无 podcast/视频露面
  - 🎬 ⚠️ 无（纯文字 newsletter）
- **核心思想关键词**: 历史脉络优先、技术原理祛魅、curiosity（Babbage 精神）、讲清 why 而非追前沿、人物/公司史。
- **voice_samples**:
  - **创作宗旨样本（原话）**: 笔名取自 Charles Babbage，希望「a tiny fraction of Babbage's curiosity and spirit enters our collective exploration of this subject」；目标是「通过塑造半导体的技术、公司与人物的故事帮读者更好理解半导体」。 (source: T01-S024, 原话/要旨)
  - **方法样本（转述）**: Doug O'Laughlin 公开背书「半导体业我几乎总从历史切入，The Chip Letter 无人能及」—— 其签名是从历史脉络拆解技术。 (source: Track 05 T05-S003, 转述)
  - ⚠️ 匿名，无更多个人 register 原话；voice_confidence 偏 low。
- **sub_skill_candidate**: `false` —— 匿名 + 科普史向，靠 newsletter 内容而非可问责个人思想体系；作技术史 context anchor。
- **最近 12 个月动态**: 周更长稿（2026-06 活跃，27000+ 订阅）；被 SemiAnalysis recommendations + Fabricated Knowledge 反复推荐。
- **争议 / 批评**: 匿名使可问责性受限；科普史性质，非工艺 ground truth；偏 context/入门而非前沿技术。
- **来源**: [Primary] T01-S024 (本人 About 页) / 关联 Track 05 T05-S003。⚠️ 仅 1 直接来源（匿名限制）。
- **可信度自评**: medium —— 技术史可靠且业内推荐，但匿名 + 单一来源 + 科普性质。

### 15. 梁孟松 Liang Mong Song

- **One-liner**: 工艺整合大师（TSMC→Samsung→SMIC 三跳），以良率爬坡 know-how 著称 —— 领 SMIC 14nm FinFET 良率 298 天从 ~3% 爬到 >95%；但公开发声极少，多为二手转述。 (evidence: [T01-S028])
- **核心身份**: 前 SMIC co-CEO（2017-，主管工艺技术研发）；前 Samsung System LSI CTO；前 TSMC 研发资深处长。
- **代表作品**: SMIC 14nm FinFET 良率爬坡（298 天 3%→95%）+ N+1/N+2；Samsung 14/16nm（助三星赢 TSMC）；TSMC 多代工艺（曾参与）。
- **值得读 / 听 / 看的 3 件事**:
  - 🎙️ ⚠️ 公开长访谈稀缺；其工艺细节散见离职抗议信（二手引用）[T01-S028]
  - 📖 ⚠️ 无本人长文/talk 公开（中文圈工艺专家发声有限的典型）
  - 🎬 ⚠️ 无
- **核心思想关键词**: 工艺整合、良率爬坡（yield ramp 是核心 know-how）、FinFET N+1/N+2 不靠 EUV、工艺 tacit 手艺、节点导入速度。
- **voice_samples**:
  - **良率信条样本（转述其业绩）**: 领 SMIC 14nm FinFET 良率「298 天内从约 3% 爬到 >95%」—— 是「良率爬坡是长期 know-how 壁垒、靠工艺整合经验」的实证（intake warning 核心）。 (source: T01-S028, 转述)
  - **国产先进制程立场样本（转述其声称）**: 曾公开声称 SMIC 的 FinFET N+1/N+2 节点「无需 EUV 设备即可实现」—— 须 caveat：这是其声称，良率/成熟度/成本现实差距是另一回事（反国产替代过度乐观的张力点）。 (source: T01-S028, 转述/其声称)
  - ⚠️ 暂未找到 ≥30 字本人公开连续原话片段 —— 中文圈工艺大师公开长材料稀缺，其表态多见离职信/媒体转述，voice_confidence: low。
- **sub_skill_candidate**: `false` —— 工艺整合/良率 know-how 极强，但公开材料严重不足（无长访谈/talk），无法支撑独立 sub-skill；作「良率爬坡 tacit 手艺」的人物注脚。
- **最近 12 个月动态**: 2022 起退出 SMIC 决策层（仍挂 co-CEO）；2023 媒体报道其在 SMIC 先进制程角色边缘化；国产先进制程（SMIC N+2/7nm）讨论中其历史角色被反复提及。
- **争议 / 批评**: 「N+1/N+2 不靠 EUV」声称 vs 良率/成本/成熟度现实差距（须诚实拆穿国产替代过度乐观）；多次跳槽 + 离职抗议信引商业伦理争议；公开技术发声极少，可调研性弱。
- **来源**: [Secondary] T01-S028 (Wikipedia/媒体谱系) / 二手媒体转述。⚠️ **figures 偏 en 的诚实例证**：作为唯一 zh-CN 工艺 figure，本人长材料几乎为零。
- **可信度自评**: medium-low —— 工艺成就实在，但公开材料严重不足、无本人长访谈、声称须 caveat，是「中文圈工艺专家发声有限」的典型。

---

## 候选但 DROP / 降级（透明记录）

| 候选 | 方向 | 判定 | 原因 |
|------|------|------|------|
| Krishna Saraswat | Stanford 互连/3D 集成 | DROP → Track 04 | 纯学术（论文/课程输出），未找到 ≥30min 长访谈/conference talk 谈实践 → 归 canon 不进 figures（iter4 学术特例）|
| James Plummer | Stanford 教材作者 | DROP → Track 04 | 教材《Silicon VLSI Technology》作者，已在 Track 04 canon 充分捕获；个人长访谈材料偏教学，figure 增量低 |
| Mark Liu 刘德音 | 前 TSMC 董事长 | DROP | 与 C.C. Wei/张忠谋 重叠；已退（2024），公开工艺 talk 少，产业领袖位由张忠谋/魏哲家代表 |
| 米玉杰 | SMIC 工艺 | DROP | zh-CN 工艺高管，公开长材料几乎为零（同梁孟松困境但更甚），不足立卡 |
| Daniel Nenni | SemiWiki 创始人 | DROP → Track 05 | 40+ 年业内但偏 EDA/商业/社区运营，工艺技术原创思想有限；作 Track 05 source 主体 |
| Doug O'Laughlin | Fabricated Knowledge | BORDERLINE → 降级 | 设备/材料/供应链分析强，但偏产业链/投资视角，纯前道工艺思想弱于 Dylan/Jon；已在 Track 05 立卡，figure 维度并入 Dylan Patel 卡片关联（Transistor Radio 同组）|
| Handel Jones | IBS 分析师 | DROP | 偏市场/财务预测，工艺技术深度弱，营销/咨询倾向 |
| "芯片大佬 top10" 营销榜人物 | 自媒体 | DROP（黑名单）| intake warning 明确：匿名软文/情绪化自媒体/纯股评 ≠ figure |

---

## Phase 2 提炼提示

### 反复出现 ≥ 3 个 figures 都谈到的关键词（候选行业心智模型）

- **「设备/工艺是必要非充分，良率/know-how 是真壁垒」**（出现于 figures: Dylan Patel / Jon Y / 梁孟松 / van den Brink 隐含）—— **头号候选心智模型**：拆穿「买到 EUV/光刻机就能做先进制程」；Patel「光刻不是唯一 linchpin」+ Jon Y「知识 siloed 在公司、师徒型 tacit」+ 梁孟松「298 天良率爬坡」三源交叉。 (evidence: [T01-S017, T01-S028])
- **「微缩 = 不断加强栅对沟道的静电控制（thin body）」**（出现于 figures: Chenming Hu / King Liu / 隐含 Dennard 终结）—— 器件架构演进的单一第一性逻辑：Hu「thin body / 把晶体管立起来」+ King Liu「narrow fin straddled by gate → enhanced gate control」。 (evidence: [T01-S001, T01-S011])
- **「节点名是营销，真尺度看 MTr/mm² + 成本 + PPAC」**（出现于 figures: Mark Bohr / Scotten Jones / Dylan Patel）—— 评价节点先换算真密度/真成本；Bohr「真密度度量」+ Jones「晶圆成本建模」+ Patel「事实校准」。 (evidence: [T01-S020, T01-S019])
- **「微缩首先是经济命题，物理是约束底线」**（出现于 figures: Gordon Moore / Robert Dennard / Scotten Jones）—— Moore「the point was economics not technology」+ Dennard 把它物理化 + Jones 量化成本墙 → 物理硬约束 ⇄ 良率/成本经济约束的双重张力（与 Track 04 头号心智模型同源）。 (evidence: [T01-S030, T04-S004])
- **「延寿既有技术 vs 推倒重来；演化优于革命」**（出现于 figures: 胡正明 / 林本坚 / van den Brink）—— Hu「FinFET 其实是 evolutionary 不是 revolutionary」+ Lin「193i 延寿 DUV 而非跳 157nm/EUV」+ van den Brink「攻坚极复杂问题但走可量产路径」。 (evidence: [T01-S001, T01-S005])

### 显著分歧 / 流派分裂

- **「摩尔定律已死」派 vs 「等效微缩继续」派**：代表 Mark Bohr / C.C. Wei（厂商乐观，等效微缩 + 真密度继续）vs Scotten Jones / Dylan Patel（成本墙量化，每晶体管成本下降放缓，更审慎）。Gordon Moore 定律被双方各自引用。
- **器件奠基派（Berkeley/IBM 学术）vs 产业工艺/良率派 vs 实证分析师派**：奠基 = Hu / King Liu / Dennard / Moore（论文/oral history）；产业 = 张忠谋 / van den Brink / Lin / 魏哲家 / 梁孟松（工程/运营）；分析 = Dylan Patel / Scotten Jones / Jon Y / Cutress / Babbage（祛魅/实证/拆解）。三派对「什么是 ground truth」看法不同：学术信论文物理、产业信良率 ramp、分析信拆解+成本模型。
- **国产替代叙事的张力**：梁孟松「N+1/N+2 不靠 EUV」声称 vs Dylan Patel「中国良率/效率仍落后数年」的实证审慎 —— 同一议题，本人声称 vs 第三方实证的分裂（须诚实保留，反过度乐观/悲观双极）。
- **前道微缩 vs 先进封装/3D 异构集成谁是未来**：Scotten Jones「3D era 经济学」+ van den Brink（光刻派）vs 封装派 —— 在 figures 层未充分展开（更多在 Track 05），留 Phase 2 与 canon/sources 交叉。

### 冷僻领域信号

- 总 figure 数 < 10？ **否（retain 15）** ✅
- 多数 figure 长访谈材料 < 30min？ **否**（Hu/张忠谋 oral history、Dylan/Jon 2h Dwarkesh、van den Brink farewell、Bohr SemiEng 长访谈均 ≥30min；仅梁孟松/Babbage/魏哲家偏短或受限）✅
- 标 "可信度 low" 比例 > 30%？ **否**（low 仅 1 = 梁孟松 medium-low ≈ 6.7%）✅
- **不触发冷僻协议，信号充足（data-rich 行业）**。

### 诚实边界（须进 SKILL.md Phase 2.8）

1. **figures 偏 en（结构性失衡）**：15 位中 13 位英文圈（含台裔 en 输出的 Hu/Lin/Chang），仅梁孟松为 zh-CN 工艺 figure 且本人长材料几乎为零、米玉杰等不足立卡。**工艺思想 ground truth 以 en 发明人/分析师为准**；zh-CN 工艺专家公开发声有限是真实 locale gap，国产替代相关声称（梁孟松「不靠 EUV」）须二次核对，不可当工程现实。
2. **一手率 host-based 仅 45%（低于 50% floor）**：因发明人 oral history/长访谈多托管在博物馆(CHM)/协会(SEMI)/媒体平台（host=secondary），但**内容是 figure 本人原话**；按「内容一手」计 ≈ 65%。Phase 4 须区分 host 一手 vs 内容一手，本 track 倾向后者更能反映 figure 真实发声。
3. **voice_samples 富度不均**：Chenming Hu（CHM oral history 逐字，富矿，3 段全原话）、张忠谋/Dylan Patel/van den Brink（原话+要旨混合）voice 强；Dennard/Lin/Scotten Jones/Cutress/梁孟松 voice 偏弱（本人连续 ≥30 字原话稀缺，已诚实标 ⚠️），Phase 4 voice check 应对这些降 voice_confidence。
4. **分析师/科普 figure 的可信度边界**：Dylan Patel（商业模型当事实 + 利益相关，数字须交叉）、Jon Y/Babbage（匿名，可问责性受限）、Scotten Jones（成本估算非实测）—— 是 context/祛魅 anchor 与实证拆解来源，但前沿工艺 ground truth 仍以顶会一手论文（Track 04/05）为准。
5. **厂商代言人立场相关性**：Mark Bohr（Intel）、C.C. Wei（TSMC）的乐观/披露须标厂商利益相关；"good yield" 等无具体数字（商业机密），不可当独立验证事实。
