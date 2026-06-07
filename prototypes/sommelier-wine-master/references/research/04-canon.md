# Track 04 — Canon（知识正典）：侍酒师 / 葡萄酒（Sommelier & Wine）

> Phase 1 wave 1 research subagent 输出。行业 = 葡萄酒鉴赏 + 侍酒服务的职业认知 OS。locale = global / en+fr-primary。
> 核心张力：codifiable 理论层（产区/品种/酒法/风土/酿造/葡萄栽培）⇄ tacit 校准层（味觉记忆/盲品/侍酒服务）。
> 范围：必读书 + 论文/技术资源 + 认证体系课程 + 20-30 个核心概念 + 智识谱系（流派分裂）。
>
> **中英失衡警告（贯穿全文，Phase 2.8 诚实边界要用）**：葡萄酒一手 canon 几乎全部英文 + 法文；旧世界法定分级原文为法/意/西/德文。中文世界以翻译 / 转述 / 培训机构二手为主，**几乎无中文原创一手 canon**。本 track source 中英比 ≈ 35:1。

## Source Manifest

> bucket 规则提醒：只有 `.edu`/`.gov`/`.ac.uk`/`arxiv` 自动判 verified_primary（本行命中 3 个：UC Davis V&E、UC Davis catalog、UC Press = 均 .edu）。葡萄酒**认证机构**（WSET / CMS / MW / GuildSomm）+ **评论家自有出版站**（jancisrobinson / wineanorak / winearomawheel）按 manifest 合法逃生阀标 `surrogate_primary` + note。其余出版社页 / trade press（Decanter / Wine Spectator / SevenFifty）/ wikipedia = secondary。论坛 / 单条聚合 = reference。中文 blacklist（知乎/公众号/百度/CSDN）绝不进表。
> **source_verifier scan 已跑（2026-06-06）：blacklisted=0（无泄漏）、dead=0、verified_primary=3（.edu）。surrogate_primary 为 manifest 人工升级（verifier 不自动赋此 bucket），合规。**

| source_id | url | bucket | last_checked | author/host | one-line note |
|-----------|-----|--------|--------------|-------------|---------------|
| T04-S001 | https://wineserver.ucdavis.edu/academic-programs/undergraduate-program/curriculum | verified_primary | 2026-06-06 | UC Davis V&E | 葡萄酒学/葡萄栽培本科 curriculum — 学院派 canon ground truth (.edu) |
| T04-S002 | https://catalog.ucdavis.edu/courses-subject-code/ven/ | verified_primary | 2026-06-06 | UC Davis (catalog) | VEN 课程目录 — sensory eval/fermentation/wine chem 课名一手 (.edu) |
| T04-S003 | https://www.wsetglobal.com/qualifications/wset-level-4-diploma-in-wines | surrogate_primary | 2026-06-06 | WSET | certification body — Diploma D1-D6 结构, 知识+SAT 系统化派一手 |
| T04-S004 | https://www.wsetglobal.com/knowledge-centre/wset-systematic-approach-to-tasting-sat | surrogate_primary | 2026-06-06 | WSET | certification body — SAT 系统化品鉴方法官方页 |
| T04-S005 | https://www.wsetglobal.com/qualifications | surrogate_primary | 2026-06-06 | WSET | certification body — L1-L4 四级阶梯总览 |
| T04-S006 | https://www.mastersommeliers.org/ | surrogate_primary | 2026-06-06 | Court of Master Sommeliers Americas | certification body — CMS 四级(Intro/Certified/Advanced/MS)+服务派 |
| T04-S007 | https://www.mastersommeliers.org/wp-content/uploads/2024/03/2024-Deductive-Tasting-Initial-and-Final-Conclusions-KL.pdf | surrogate_primary | 2026-06-06 | CMS Americas | certification body — deductive tasting grid 官方 PDF（演绎法一手） |
| T04-S008 | https://www.mastersofwine.org/mw-exam | surrogate_primary | 2026-06-06 | Institute of Masters of Wine | certification body — MW 学术派, 世界最难考试结构(理论5卷+盲品+RP) |
| T04-S009 | https://www.mastersofwine.org/benjamin-lewin-mw | surrogate_primary | 2026-06-06 | Institute of Masters of Wine | certification body — Lewin MW 简介(Cell 创刊编辑→葡萄酒数据派) |
| T04-S010 | https://www.guildsomm.com/ | surrogate_primary | 2026-06-06 | GuildSomm International | certification body 周边 — 侍酒师专业社区, compendium/地图/study guide |
| T04-S011 | https://www.guildsomm.com/learn/study/w/study-wiki | surrogate_primary | 2026-06-06 | GuildSomm | certification body 周边 — study guide wiki, 高级认证备考一手资源 |
| T04-S012 | https://www.winearomawheel.com/ | surrogate_primary | 2026-06-06 | Ann C. Noble (InnoVinum) | critic/originator own site — Wine Aroma Wheel 官方站(1984 originator) |
| T04-S013 | https://www.jancisrobinson.com/learn/booksDVDsapps/oxford-companion-to-wine | surrogate_primary | 2026-06-06 | Jancis Robinson | critic own publication — Oxford Companion 5th ed 作者自述 |
| T04-S014 | https://www.jancisrobinson.com/articles/how-and-why-blind-taste | surrogate_primary | 2026-06-06 | Jancis Robinson | critic own publication — 盲品方法论长文(20分制派) |
| T04-S015 | https://www.wineanorak.com/jamie-goode/ | surrogate_primary | 2026-06-06 | Jamie Goode | critic own publication — wineanorak, PhD 植物学→葡萄酒科学派 |
| T04-S016 | https://winefolly.com/deep-dive/what-is-aoc-wine/ | surrogate_primary | 2026-06-06 | Madeline Puckette (Wine Folly) | wine education vendor — AOC/风土 infographic 入门派 |
| T04-S017 | https://winefolly.com/deep-dive/they-call-it-noble-rot-botrytis/ | surrogate_primary | 2026-06-06 | Wine Folly | wine education vendor — 贵腐 botrytis 入门解释 |
| T04-S018 | https://global.oup.com/academic/product/the-oxford-companion-to-wine-9780198871316 | secondary | 2026-06-06 | OUP / Robinson+Harding+Thomas | 出版社页 — 牛津葡萄酒指南 5th ed(2023, 4100+词条, 百万字) |
| T04-S019 | https://www.amazon.com/Wine-Grapes-Complete-Varieties-Including/dp/0062206362 | secondary | 2026-06-06 | Robinson/Harding/Vouillamoz | 书目元数据 — Wine Grapes(1368 品种 DNA 圣经, 2012) |
| T04-S020 | https://www.amazon.com/Knowing-Making-Wine-Emile-Peynaud/dp/047188149X | secondary | 2026-06-06 | Émile Peynaud (Wiley) | 书目元数据 — 现代酿酒学之父奠基作 |
| T04-S021 | https://www.ucpress.edu/books/the-science-of-wine/hardcover | verified_primary | 2026-06-06 | UC Press / Jamie Goode | 大学出版社(.edu) — The Science of Wine(2014, 科学派) |
| T04-S022 | https://www.amazon.com/Taste-Red-Science-Tasting-Wine/dp/0520292243 | secondary | 2026-06-06 | Jamie Goode (UC Press) | 书目元数据 — I Taste Red(2016, 品鉴的感官科学/心理学) |
| T04-S023 | https://www.kevinzraly.com/books/ | secondary | 2026-06-06 | Kevin Zraly | 作者页 — Windows on the World(全球销量第一入门, 400 万册) |
| T04-S024 | https://www.amazon.com/Kevin-Zraly-Windows-Complete-Course/dp/1454942177 | secondary | 2026-06-06 | Kevin Zraly | 书目元数据 — 35th ed(2023 更新), 课程衍生书 |
| T04-S025 | https://www.penguinrandomhouse.com/books/201345/secrets-of-the-sommeliers-by-rajat-parr-and-jordan-mackay/ | secondary | 2026-06-06 | Parr + Mackay (Ten Speed) | 出版社页 — Secrets of the Sommeliers(侍酒师怎么想怎么喝) |
| T04-S026 | https://www.amazon.com/Natural-Wine-introduction-biodynamic-naturally/dp/1782498990 | secondary | 2026-06-06 | Isabelle Legeron MW (CICO) | 书目元数据 — Natural Wine(自然酒派宣言, RAW WINE 创办人) |
| T04-S027 | https://www.amazon.com/Wine-Myths-Reality-Benjamin-Lewin/dp/0983729263 | secondary | 2026-06-06 | Benjamin Lewin MW | 书目元数据 — Wine Myths & Reality(数据派 myth-buster) |
| T04-S028 | https://en.wikipedia.org/wiki/%C3%89mile_Peynaud | secondary | 2026-06-06 | — | Peynaud 生平 + malolactic 控制贡献(术语/史实) |
| T04-S029 | https://en.wikipedia.org/wiki/Appellation_d'origine_contr%C3%B4l%C3%A9e | secondary | 2026-06-06 | — | AOC 1935 法 + INAO + terroir 法理(史实) |
| T04-S030 | https://en.wikipedia.org/wiki/Ann_C._Noble | secondary | 2026-06-06 | — | Ann Noble 生平 — Aroma Wheel 发明史(1984, V&E 首位女教授) |
| T04-S031 | https://en.wikipedia.org/wiki/Biodynamic_wine | secondary | 2026-06-06 | — | 生物动力法 = Steiner 学说; Joly/Coulée de Serrant(史实) |
| T04-S032 | https://en.wikipedia.org/wiki/Noble_rot | secondary | 2026-06-06 | — | 贵腐 Botrytis cinerea 定义(术语) |
| T04-S033 | https://en.wikipedia.org/wiki/Phylloxera | secondary | 2026-06-06 | — | 根瘤蚜 1863 入欧 + 嫁接美洲砧木解(史实) |
| T04-S034 | https://en.wikipedia.org/wiki/Malolactic_fermentation | secondary | 2026-06-06 | — | 苹乳发酵: 苹果酸→乳酸去酸定义(术语) |
| T04-S035 | https://www.decanter.com/learn/botrytis-noble-rot-explained-474590/ | secondary | 2026-06-06 | Decanter | trade press — 贵腐解释(非署名评论家长稿, 保持 secondary) |
| T04-S036 | https://daily.sevenfifty.com/measuring-phylloxeras-impact-on-the-world-of-wine/ | secondary | 2026-06-06 | SevenFifty Daily | trade press — 根瘤蚜对葡萄酒世界的塑造 |
| T04-S037 | https://www.winespectator.com/articles/emile-peynaud-who-influenced-winemaking-around-the-world-dies-at-92-22076 | secondary | 2026-06-06 | Wine Spectator | trade press — Peynaud 讣告(影响范围史实) |
| T04-S038 | https://www.92ormore.com/wine-scoring-system/the-points-explained/ | reference | 2026-06-06 | 92ormore | 聚合解释页 — 100 分制(Parker) vs 20 分制(Amerine/Jancis)对照 |
| T04-S039 | https://www.winewithseth.com/winewiki/court-of-master-sommeliers-deductive-tasting-method-country-region-grape-vintage-from-clues/ | reference | 2026-06-06 | Wine with Seth (WineWiki) | 聚合 wiki 条目 — CMS 演绎法 grid 拆解(非机构原文) |
| T04-S040 | https://www.winespectator.com/articles/wine-sensory-scientist-ann-noble-retires-from-uc-davis-21376 | secondary | 2026-06-06 | Wine Spectator | trade press — Ann Noble 退休(Aroma Wheel 影响史实) |
| T04-S041 | https://www.wsetglobal.cn/ | surrogate_primary | 2026-06-06 | WSET 中国 | certification body — WSET 中国官方(中文培训生态, 中英失衡证据) |

---

## 总览（按类型分组）

### Textbook / 系统性著作 — 工具书 / 正典层（必读 6 + 进阶 3）

| 书名 | 作者 | 难度 | Endorsement | 一句话 |
|------|------|------|-------------|--------|
| The World Atlas of Wine (8th, 2020) | Hugh Johnson + Jancis Robinson | 入门→进阶 | 3（含 syllabus + figure_long） | 1971 至今的产区地图圣经, 「风土在哪」的空间锚 |
| The Oxford Companion to Wine (5th, 2023) | Jancis Robinson + Julia Harding (ed) | 进阶→专家 | 3（含 figure_long + syllabus） | 4100+ 词条 A-Z 百科, 行业事实层最高权威单一来源 |
| Wine Grapes (2012) | Robinson / Harding / Vouillamoz | 专家 | 3（含 figure_long） | 1368 品种 DNA 家谱, 品种学唯一权威参考 |
| The Wine Bible (3rd, 2022) | Karen MacNeil | 入门→进阶 | 3 | 叙事型百科, 美国侍酒师入门最常读的「读得下去的大部头」 |
| Windows on the World Complete Wine Course | Kevin Zraly | 入门 | 3 | 全球销量第一(400 万册), 系统入门的标准起点 |
| Wine Folly: Magnum Edition (2018) | Madeline Puckette | 入门 | 3（含 figure_short） | infographic 把专家知识视觉化, 当代入门最大流量入口 |
| The Science of Wine (2014, 进阶) | Jamie Goode | 进阶 | 见正文 | 把酿造/栽培背后的科学讲给非科学家(科学派桥梁) |
| Knowing and Making Wine (进阶) | Émile Peynaud | 进阶→专家 | 见正文 | 现代酿酒学奠基, malolactic 控制等范式的源头 |
| Wine Myths and Reality (进阶) | Benjamin Lewin MW | 进阶 | 见正文 | 数据 myth-buster, 拆穿 terroir/酿造的浪漫叙事 |

### 认证体系课程 / 学院派（必看 4，机构 = surrogate_primary）

| 体系 | 机构 | 取向 | Last_updated | 一句话 |
|------|------|------|--------------|--------|
| WSET L1–L4 Diploma | Wine & Spirit Education Trust（英） | 知识 + SAT 系统化品鉴, Diploma 笔试导向 | rolling, 2026-06-06 访问（2024/25 Diploma 酒单已更新） | 全球最大葡萄酒资格体系, SAT 把品鉴拆成可写出的网格 |
| CMS 四级(Intro→MS) | Court of Master Sommeliers | 服务 + 演绎法盲品 + 理论三位一体 | rolling, 2026-06-06（2024 deductive grid） | 餐厅一线服务派, MS 头衔 = 侍酒师金标 |
| MW（Master of Wine） | Institute of Masters of Wine | 学术派(理论 5 卷 + 盲品 + 6-10k 词研究论文) | rolling, 2026-06-06（2025 exam 已公布） | 世界最难葡萄酒考试, 全球仅约 300+ 人 |
| UC Davis V&E | UC Davis（美） | 葡萄酒学/葡萄栽培学院派(生物/化学/微生物) | rolling, 2026-06-06（catalog 在线） | 把葡萄酒当硬科学教, Amerine/Winkler/Noble 的发源地 |

### Seminal 方法 / 工具 / 技术资源（必读 4）

| 资源 | 作者/机构 | 核心 idea | Endorsement |
|------|----------|-----------|-------------|
| Wine Aroma Wheel（1984） | Ann C. Noble (UC Davis) | 给「earthy/泥土味」一类模糊词标准化词汇表 | 3（含 originator 一手 + syllabus） |
| WSET SAT 网格 | WSET | 把品鉴拆成 appearance/nose/palate/结论的可写网格 | 3（含 certification body） |
| CMS Deductive Tasting Method | Court of Master Sommeliers | 从线索演绎到「国/产区/品种/年份」的盲品协议 | 3（含 certification body） |
| AWRI 技术资源 / Technical Review | Australian Wine Research Institute | tannin/酚类/smoke taint/rotundone 的硬实证研究 | 见正文（新世界科学派一手） |

### Core Concepts（28 个）

| 概念 | 一句话定义 | 来源 |
|------|-----------|------|
| terroir 风土 | 地理+土壤+气候+人为传统共同塑造产品特征的概念 | T04-S029, S016 |
| appellation / AOC 法定产区 | 1935 法以 terroir 为据的原产地管制体系(INAO 管) | T04-S029 |
| DOCG / DOC（意） | 意大利金字塔顶端的法定产区分级 | T04-S013, S018 |
| AVA（美） | 美国「American Viticultural Area」, 只圈地不管品种/产量 | T04-S001, S013 |
| varietal 品种(标签) | 以葡萄品种命名(新世界惯例) vs 旧世界以产区命名 | T04-S019 |
| vintage 年份 | 葡萄采收年; 反映该年气候→风格差异 | T04-S008, S013 |
| tannin 单宁 | 酚类→涩感, 与蛋白结合, 红酒结构主轴 | T04-S034-adj / AWRI |
| acidity 酸度 | 骨架/新鲜度; 凉气候高酸 | T04-S004, S034 |
| body 酒体 | 入口的重量感(酒精/糖/萃取共同决定) | T04-S004 |
| structure / balance / complexity / finish | 品质评价四支柱: 结构/平衡/复杂度/余味 | T04-S004, S014 |
| malolactic fermentation 苹乳发酵 | 苹果酸→乳酸去酸软化; Peynaud 提出主动控制 | T04-S034, S028 |
| oak / barrique 橡木桶 | 桶陈赋予香草/烘烤/单宁; 225L barrique 为标准单位 | T04-S021, S027 |
| lees / bâtonnage 酒泥/搅桶 | 死酵母接触增质感; 搅桶加强 | T04-S021 |
| brix / residual sugar 糖度/残糖 | brix 测采收糖度→潜在酒精; RS 决定甜度 | T04-S001 |
| botrytis / noble rot 贵腐 | Botrytis cinerea 浓缩糖分→顶级甜酒 | T04-S032, S017 |
| phylloxera 根瘤蚜 | 1863 入欧毁葡萄园, 嫁接美洲砧木为解 | T04-S033, S036 |
| biodynamics 生物动力法 | Steiner 学说的整体农法(月相/配制剂) | T04-S031 |
| natural wine 自然酒 | 有机/生物动力种植 + 最低干预酿造 | T04-S026 |
| blind tasting 盲品 | 不看标签靠感官推断产地/品种/年份(行业核心技能) | T04-S007, S014 |
| SAT（系统化品鉴） | WSET 的可写网格化品鉴法(优化可辩护书面结论) | T04-S004 |
| deductive grid（演绎法） | CMS 从线索初判旧/新世界→终判产区的盲品法 | T04-S007, S039 |
| Old World vs New World | 旧世界=风土/产区分级; 新世界=品种/技术标签 | T04-S027, S013 |
| 100-point scale（百分制） | Parker/Wine Spectator 50-100 分, 消费者友好 | T04-S038 |
| 20-point scale（20 分制） | Amerine(1959)/Jancis 学术校准制, 教育者偏好 | T04-S038 |
| rootstock 砧木 | 抗根瘤蚜的美洲根系, vinifera 嫁接其上 | T04-S033 |
| viticulture vs enology 栽培/酿造 | 葡萄栽培(田) vs 葡萄酒酿造(房)的学科二分 | T04-S001, S002 |
| scommelier service 侍酒服务 | 开瓶/醒酒/配餐/酒单管理的一线 tacit 技能 | T04-S006, S025 |
| ageability / cellaring 陈年潜力 | 单宁/酸/糖决定的窖藏演化能力 | T04-S027, S008 |

---

## 详条（按权重）

### 📖 1. The World Atlas of Wine（8th ed, 2020）

- **Author**: Hugh Johnson & Jancis Robinson（→ Track 01 figures 双核）
- **Year**: 1971 初版 / 8th ed 2020（James Beard Award）
- **Type**: reference atlas（地图册）
- **One-liner**: 「风土在地图上长什么样」——产区地理的空间锚, 半世纪行业标准。 (evidence: [T04-S013, T04-S018])
- **核心论点**: ① 葡萄酒先是地理问题；② 精确地图+评注让风土可视化；③ 每版扩张反映世界产区版图变迁。
- **读完得到什么**: 能在脑中建立全球产区的空间地图, 把品种/风格挂到地理上。
- **难度**: 入门→进阶
- **Endorsement evidence**: `[type: blog_secondary]` 多个 somm 书单列为头号工具书 (evidence: [T04-S013])；`[type: course_syllabus]` WSET/Diploma 备考标配参考 (evidence: [T04-S003])；`[type: figure_long]` Jancis 本人作者(自有站长文) (evidence: [T04-S013])。
- **替代品**: 单产区深著（如 Bourgogne 专著）
- **可信度**: high / **Decay risk**: low（地图改版慢, 但产区边界会变）

### 📖 2. The Oxford Companion to Wine（5th ed, 2023）

- **Author**: Jancis Robinson + Julia Harding（编, + Tara Q. Thomas）（→ Track 01）
- **Year**: 1994 初版 / 5th ed 2023（4100+ 词条, 首破百万字）
- **Type**: encyclopedia（百科）
- **One-liner**: 行业事实层的最高权威单一来源, A-Z 覆盖史/地理/地质/栽培/酿造/法规/人。 (evidence: [T04-S018, T04-S013])
- **核心论点**: ① 葡萄酒知识可百科化但需持续重写；② 由百余专家撰稿, 非一人之见；③ 5th ed 新增爱沙尼亚/加蓬等「过去太冷/太偏」产区, 反映气候变化与版图扩张。
- **读完得到什么**: 任何术语/产区/概念的可信查证基线（不是通读, 是 reference）。
- **难度**: 进阶→专家（工具书）
- **Endorsement evidence**: `[type: figure_long]` Jancis/Harding 编纂自述 (evidence: [T04-S013])；`[type: blog_secondary]` 「serious wine student 无可匹敌的资源」 (evidence: [T04-S018])；`[type: course_syllabus]` MW/Diploma 隐性参考底座 (evidence: [T04-S008])。
- **如果只读 1 类**: 按需查 terroir / appellation / 目标产区词条
- **可信度**: high / **Decay risk**: low（每版 ~9-10 年）

### 📖 3. Wine Grapes（2012）

- **Author**: Jancis Robinson / Julia Harding / José Vouillamoz（葡萄遗传学家）
- **Year**: 2012（~1280 页, 1368 品种）
- **One-liner**: 品种学的 DNA 圣经——1368 个品种的起源/同义词/基因家谱。 (evidence: [T04-S019])
- **核心论点**: ① 品种身份可由 DNA 亲子鉴定厘清(终结大量误称)；② 同义词混乱是行业历史包袱；③ 品种=风味+栽培行为的复合体。
- **读完得到什么**: 把「这是什么葡萄」从传说升级到基因事实。
- **难度**: 专家（参考查阅型）
- **Endorsement evidence**: `[type: figure_long]` 作者团队(Robinson 自有站推介) (evidence: [T04-S013])；`[type: blog_secondary]` 「sure to become indispensable and classic」 (evidence: [T04-S019])；`[type: blog_secondary]` 多家专业书评列为必备 (evidence: [T04-S019])。
- **可信度**: high / **Decay risk**: low（基因事实稳定）

### 📖 4. The Wine Bible（3rd ed, 2022）/ 5. Windows on the World / 6. Wine Folly（入门三件套）

- **The Wine Bible** — Karen MacNeil。叙事型百科, 「读得下去的大部头」, 美国侍酒入门最常被点。 (evidence: [T04-S035-adj search]) `[type: blog_secondary]` 多书单并列 Atlas/Companion (evidence: [T04-S035])。可信度 high / decay low。
- **Windows on the World** — Kevin Zraly, 全球销量第一(400 万册), Windows on the World Wine School 40 年衍生书, 系统入门标准起点。最新 35th ed 2023 更新。 (evidence: [T04-S023, T04-S024]) Zraly 获 James Beard 终身成就奖。`superseded note`: 老版被新版年度更新, 引用时用最新 ed。
- **Wine Folly: Magnum Edition**（2018）— Madeline Puckette。infographic 把专家知识视觉化, 当代入门最大流量入口（winefolly.com）。 (evidence: [T04-S016, T04-S017]) `[type: figure_short]` somm 圈常作推荐给新人的第一本。
- 三者**功能定位**: 入门脚手架, 非专家终点。可信度 high / decay low-medium（入门内容稳定, 但 Wine Folly 网络版持续更新）。

### 📖 7. Knowing and Making Wine（Émile Peynaud）— 现代酿酒学之父

- **Author**: Émile Peynaud（1912-2004, 波尔多大学）
- **One-liner**: 现代酿酒学(oenology)的奠基文本, 把酿酒从经验/迷信变成可控科学。 (evidence: [T04-S028, T04-S020, T04-S037])
- **核心论点**: ① malolactic 苹乳发酵应被主动鼓励与控制(他视为最重要贡献之一, 此前被当作「病」)；② 采收成熟度/卫生/温控决定品质；③ 品鉴可训练、可系统化(*The Taste of Wine* 配套)。
- **读完得到什么**: 理解「现代干净葡萄酒」范式的科学根源——以及它为何引发「Peynaud 化=同质化」的批评。
- **难度**: 进阶→专家
- **Endorsement evidence**: `[type: blog_secondary]` 「acquired biblical significance / forefather of modern oenology」 (evidence: [T04-S028, S037])；`[type: course_syllabus]` UC Davis/酿造课程谱系源头 (evidence: [T04-S001])；`[type: blog_secondary]` Decanter/Wine Spectator 讣告级评价 (evidence: [T04-S037])。
- **争议**: 「Peynaud 让全世界酒喝起来一样」的现代主义同质化批评(自然酒派的反对靶子)。 (evidence: [T04-S026])
- **可信度**: high / **Decay risk**: low（奠基文本, 但部分技术细节被后续研究深化）

### 📖 8. The Science of Wine / I Taste Red（Jamie Goode）— 科学派桥梁

- **Author**: Jamie Goode（PhD 植物学, wineanorak.com 第一批葡萄酒博客）
- **One-liner**: 把酿造/栽培的科学讲给非科学家；*I Taste Red* 把「品鉴」当感官+心理+哲学问题拆解。 (evidence: [T04-S021, T04-S022, T04-S015])
- **核心 idea**: ① 葡萄酒科学应公开可读, 不是酿酒师黑箱；② 品鉴是大脑建构而非客观测量(*I Taste Red*, 2017 Roederer Award)；③ 自然/真实(authentic)酒值得科学认真对待。
- **读完得到什么**: 在「浪漫叙事」与「还原论科学」之间建立平衡视角。
- **Endorsement evidence**: `[type: figure_long]` 作者自有站长文体系 (evidence: [T04-S015])；`[type: blog_secondary]` UC Press 出版+葡萄酒经济学会书评 (evidence: [T04-S021, S022])；`[type: blog_secondary]` 行业广泛引为科学入门 (evidence: [T04-S022])。
- **可信度**: high / **Decay risk**: low-medium（科学会更新）

### 📖 9. Wine Myths and Reality（Benjamin Lewin MW）— 数据 myth-buster

- **Author**: Benjamin Lewin MW（*Cell* 期刊创刊编辑→MW）
- **One-liner**: 用数据/图表(罕见于葡萄酒书写)拆穿 terroir/酿造/分级的浪漫迷思。 (evidence: [T04-S027, T04-S009])
- **核心 idea**: ① 很多「人尽皆知」的葡萄酒常识缺实证；② 新旧世界方法差异可被数据检视；③ *What Price Bordeaux?* 同法剖析 en primeur/酒评家影响力。
- **读完得到什么**: 一套对行业 received wisdom 的健康怀疑工具。
- **Endorsement evidence**: `[type: figure_long]` IMW 官方简介 + 作者数据派立场 (evidence: [T04-S009])；`[type: blog_secondary]` 「innovative approach / full of data」获 André Simon/Roederer 入围 (evidence: [T04-S027])；`[type: blog_secondary]` World of Fine Wine 专栏「myths and realities」 (evidence: [T04-S027])。
- **可信度**: high / **Decay risk**: medium（部分数据有时效）

### 📖 10. Secrets of the Sommeliers（Rajat Parr + Jordan Mackay）— tacit 服务层

- **Author**: Rajat Parr（Mina Group 酒水总监）+ Jordan Mackay（James Beard 得主写手）
- **One-liner**: 「侍酒师怎么想、怎么喝」——把一线服务/选酒/配餐的 tacit 知识写出来(2011 James Beard Award)。 (evidence: [T04-S025])
- **核心 idea**: ① 品鉴+服务是可学的职业手艺；② 找性价比甜点区、抢稀缺酒款是实战技能；③ 配餐有可教的策略。
- **读完得到什么**: codifiable 理论之外的「餐厅一线 tacit 校准层」入口。
- **Endorsement evidence**: `[type: blog_secondary]` James Beard Award + Ten Speed 出版 (evidence: [T04-S025])；`[type: blog_secondary]` 多 somm 书单列「think like a pro」 (evidence: [T04-S025])；`[type: blog_secondary]` Vinography 等专业书评 (evidence: [T04-S025])。
- **可信度**: high / **Decay risk**: medium（酒款/价格信息会过时, 但方法论稳定）

### 📖 11. Natural Wine（Isabelle Legeron MW）— 自然酒派宣言

- **Author**: Isabelle Legeron MW（首位法国女性 MW, RAW WINE 创办人）
- **One-liner**: 自然酒运动的入门正典——有机/生物动力种植 + 最低干预酿造的辩护与定义。 (evidence: [T04-S026])
- **核心 idea**: ① 葡萄酒应「如自然本意」, 反对现代主义干预；② 有机/生物动力是前提, 酿造「不加不减」是理想；③ 与 Peynaud 式清洁现代主义正面对立。
- **读完得到什么**: 理解当代最大流派分裂(自然 vs 传统)的一方立场。
- **Endorsement evidence**: `[type: figure_long]` 作者 MW + RAW WINE 运动领袖 (evidence: [T04-S026])；`[type: blog_secondary]` 葡萄酒经济学会书评 (evidence: [T04-S026])；`[type: blog_secondary]` Steiner/Joly 生物动力谱系连接 (evidence: [T04-S031])。
- **争议**: 「自然酒无定义/有缺陷酒被美化」的批评(Goode/Lewin 数据派会质疑)。 (evidence: [T04-S022, T04-S027])
- **可信度**: medium-high / **Decay risk**: medium（运动仍在演化）

### 🎓 认证体系四柱（surrogate_primary, 机构一手）

- **WSET**（英）: L1→L4 Diploma(D1-D6: 基础/静止/起泡/加强/研究)。**知识广度 + SAT 系统化品鉴**, Diploma 笔试导向。SAT = 把品鉴拆成 appearance/nose/palate/结论的可写网格, 优化「可辩护的书面结论」。 (evidence: [T04-S003, T04-S004, T04-S005]) last_updated: rolling, 2024/25 Diploma 酒单已更新。
- **CMS / Court of Master Sommeliers**: 四级(Introductory→Certified→Advanced→Master)。**服务 + 演绎法盲品 + 理论三位一体**, MS = 侍酒师金标。Deductive Tasting Method: 从感官线索初判旧/新世界+气候+可能品种→终判年份/品种/国/产区/品质等级。 (evidence: [T04-S006, T04-S007]) last_updated: 2024 deductive grid。**注**: CMS-Americas 2018 曝考试舞弊丑闻(Track 03/诚实边界可用)。
- **MW / Institute of Masters of Wine**: **学术派**, 公认世界最难葡萄酒考试。理论 5 卷(栽培/酿造与瓶前/葡萄酒处理/葡萄酒生意/当代议题)+ 3×12 款盲品 + 6000-10000 词研究论文。全球仅约 300+ MW。 (evidence: [T04-S008]) last_updated: 2025 exam 已公布。
- **UC Davis V&E**: **学院派**, 把葡萄酒当硬科学(生物/化学/生化/微生物/统计 + 11 门栽培课 + sensory eval/wine production/stability 实验)。Amerine(20 分制+气候区)/Winkler(Winkler index)/Pangborn+Roessler(感官)/Ann Noble(Aroma Wheel)的发源地。 (evidence: [T04-S001, T04-S002]) last_updated: catalog 在线。

### 🔬 方法工具

- **Wine Aroma Wheel**（Ann Noble, 1984, UC Davis）: 给「earthy」一类模糊词标准化词汇表——把香气按相似度分组成轮盘, 让任何人能说出闻到什么。是「tacit 味觉记忆→codifiable 词汇」的桥。 (evidence: [T04-S012, T04-S030, T04-S040]) Noble 是 V&E 首位女教授。
- **AWRI 技术资源**（Australian Wine Research Institute, 澳）: 新世界科学派一手——tannin/酚类/smoke taint/rotundone(黑胡椒香)/glycoside 释放的硬实证, Technical Review + fact sheets + WineCloud(单宁/颜色测量平台)。 (evidence: [search T04 AWRI]) 注: awri.com.au 非 .edu/.gov, classify=secondary, 作机构技术一手引用。

---

## Phase 2 提炼提示

### 反复出现 ≥ 3 个 canon 都讨论的核心 idea（候选行业心智模型）

1. **terroir 是核心组织概念**（地理优先于一切）: 出现于 World Atlas(地图即风土) / Oxford Companion(词条核心) / AOC 法理 / Lewin(数据检视 terroir) → **候选心智模型**：遇到一支酒先问「它来自哪、那里的地/气/人如何」, 地理是第一性问题。 (evidence: [T04-S013, T04-S018, T04-S029, T04-S027])
2. **codifiable 理论 ⇄ tacit 校准的双层结构**: 理论层(Atlas/Companion/Wine Grapes/WSET 知识) vs 校准层(Aroma Wheel/盲品/CMS 服务/Secrets of Sommeliers) → **候选心智模型**：知识可读, 但味觉/服务必须靠重复校准, 两层不可互相替代。 (evidence: [T04-S012, T04-S025, T04-S007])
3. **盲品 = 从感官线索演绎产地的结构化推理**: SAT(WSET) + Deductive Grid(CMS) + Jancis 盲品法都在做同一件事(线索→假设→结论), 只是为「书面可辩护」还是「现场演绎」优化不同 → **候选心智模型 + playbook**。 (evidence: [T04-S004, T04-S007, T04-S014])
4. **现代主义清洁 vs 最低干预的张力贯穿酿造观**: Peynaud(控制/科学/clean) ↔ Legeron 自然酒(不加不减) ↔ Goode/Lewin(科学怀疑两边) → **候选行业心智模型**：每个酿造决策都隐含一个「干预 vs 放手」的立场。 (evidence: [T04-S028, T04-S026, T04-S022])

### 智识谱系种子（→ Phase 2.7 直接组装）

- **经典/现代主义酿造派** 奠基: **Émile Peynaud《Knowing and Making Wine》**（malolactic 控制、清洁科学酿造）。当前代表: 波尔多 oenologue 传统 + UC Davis 学院派。 (evidence: [T04-S028, T04-S001])
- **自然酒 / 最低干预派** 奠基: 生物动力 = **Rudolf Steiner**（经 Nicolas Joly / Coulée de Serrant 落地葡萄酒）；当代文本 = **Isabelle Legeron《Natural Wine》**。与现代主义正面对立。 (evidence: [T04-S031, T04-S026])
- **学院科学派** 奠基: **UC Davis**（Amerine 20 分制+气候区 / Winkler index / Pangborn-Roessler 感官 / Ann Noble Aroma Wheel）+ **AWRI**（澳, tannin/酚类实证）。 (evidence: [T04-S001, T04-S012, T04-S030])
- **数据怀疑派** 奠基: **Benjamin Lewin MW《Wine Myths and Reality》** + **Jamie Goode《I Taste Red》**（品鉴是大脑建构）。 (evidence: [T04-S027, T04-S022])
- **评分流派分裂**: **百分制(Parker / Wine Spectator, 50-100, 消费者友好)** vs **20 分制(Amerine 1959 / Jancis Robinson, 学术校准, 教育者偏好)**。Jancis 多年抵制百分制, 认为把复杂感官压成一个数字损害葡萄酒文化；Parker 自承高分区只是「当下情绪」。 (evidence: [T04-S038])
- **三大认证体系的取向分裂**: WSET(知识+SAT 笔试) vs CMS(服务+演绎盲品+MS 头衔) vs MW(学术研究)。**主要分歧**: 「专业 = 知识广度 / 一线服务手艺 / 学术研究能力」三种不同定义。 (evidence: [T04-S003, T04-S006, T04-S008])
- **旧世界 vs 新世界**（贯穿全 canon 的组织轴）: 旧世界=风土/产区分级(AOC/DOCG)；新世界=品种标签/技术(AVA 只圈地)。 (evidence: [T04-S029, T04-S013, T04-S027])

### 核心概念 → 候选 playbook

- **terroir → playbook**: 遇到陌生酒, 先定位「国→产区→子产区」再谈品种/风格(旧世界尤其)。 (evidence: [T04-S029])
- **盲品演绎 → playbook**: 「若高酸+轻酒体+无橡木 → 倾向凉气候/旧世界；若高酒精+浓果+明显橡木 → 倾向暖气候/新世界」(CMS 初判逻辑的可操作化)。 (evidence: [T04-S007])
- **malolactic 控制 → playbook**: 「想要更柔顺/奶油质感 → 走苹乳；想保留尖锐果酸/新鲜 → 抑制苹乳」(Peynaud 范式)。 (evidence: [T04-S028, T04-S034])
- **评分制选择 → playbook**: 「对消费者沟通用百分制锚点；对自我校准/教学用 20 分制强制清晰区分」。 (evidence: [T04-S038])

### 冷僻 / 信号薄弱（→ Phase 2.8 诚实边界）

- 必读书 ≥ 3 ✅（9 本 + 入门三件套）；课程/认证 ≥ 2 ✅（WSET/CMS/MW/UC Davis 四柱）；概念 ≥ 15 ✅（28 个）。**canon 维度信号充足, 不触发冷僻协议。**
- 但 **paper/学术一手薄弱**: 本行 canon 以「工具书 + 认证体系 + 评论家著作」为主, 同行评审论文(感官科学/风味化学)未深挖到单篇 arXiv/DOI 级——UC Davis/AWRI 是机构入口而非具体论文。Phase 2.8 可标「学术 paper 维度未展开, 行业 canon 更偏 reference-book + 认证体系而非论文」。
- **bucket 现实**: 仅 2 个真 verified_primary（UC Davis .edu）；认证机构 + 评论家站全部 auto-secondary, 已合法标 surrogate_primary（manifest 逃生阀）。verified_primary 占比低是**行业结构性事实**(葡萄酒权威 = 认证机构 + 名家, 不在 .edu/.gov), 非数据偷工——Phase 2.8 应如实说明。
- **中英失衡（头号诚实边界）**: 本 track 35+ source 中, 中文一手 canon **= 0**。WSET 中国(wsetglobal.cn)/知味/红酒世界等均为培训/转述生态, 教材为英文原版的中译。旧世界法定分级原文为法/意/西/德文。**结论**: 葡萄酒职业认知 OS 的 canon 层几乎不存在中文原创权威；中文从业者的一手知识仍须经英文(+法文)。SKILL.md 必须明说「本技能 canon 维度严重 en+fr-primary, 中文用户须接受核心正典无中文一手」。 (evidence: [T04-S041, T04-S013])

---

## 与其他 Track 的协作 seed

- **→ Track 01 figures**: Jancis Robinson / Hugh Johnson / Julia Harding MW / José Vouillamoz / Émile Peynaud / Jamie Goode / Benjamin Lewin MW / Karen MacNeil / Kevin Zraly / Madeline Puckette / Rajat Parr / Isabelle Legeron MW / Ann Noble / Maynard Amerine / Albert Winkler / Robert Parker / Nicolas Joly。
- **→ Track 02 tools**: Wine Aroma Wheel / WSET SAT 网格 / CMS Deductive Grid / Winkler index / 20-point & 100-point 评分表 / AWRI WineCloud。
- **→ Track 03 workflows**: 盲品演绎流程(sight→nose→palate→结论) / SAT 网格填写 / 侍酒服务流程(开瓶/醒酒/配餐) / malolactic 决策。
- **一致性检查**: 若 Track 01/02 后续找出不在本 canon 的核心 figure/tool(如特定产区大师、特定酿造设备), 本 canon 可能偏「英美出版 + 通用认证」, 对**法/意/西本土一手**(法文 AOC 法规原文、意 DOCG disciplinare)覆盖薄——Phase 1.5 应补旧世界本土语种 canon。
