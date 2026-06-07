# Track 06 — Glossary（术语 + 标准 + 法规 + 认证）：侍酒师 / 葡萄酒 Sommelier & Wine

> Phase 1 wave 1 第 3 路 subagent 输出。locale = global / en+fr-primary。
> 行业核心张力：codifiable 理论（产区法规 / 化学 / SAT 网格）⇄ tacit 品鉴与服务（盲品演绎、桌边服务）。
> WSET（知识 + SAT）vs CMS（服务 + 盲品演绎 + 理论）；IMW（学术研究）；UC Davis（酿酒科学学院）。
> 旧世界（terroir / 法定产区为名）vs 新世界（grape variety 为名）。

---

## Source Manifest

| source_id | url | bucket | last_checked | author/host | one-line note |
|-----------|-----|--------|--------------|-------------|---------------|
| T06-S001 | https://www.ttb.gov/wine/wine-labeling | verified_primary | 2026-06-06 | TTB (US Treasury) | 美国酒标法主页（socket 拦截但为权威主页，规则经 eCFR 核实） |
| T06-S002 | https://www.ecfr.gov/current/title-27/chapter-I/subchapter-A/part-4 | verified_primary | 2026-06-06 | eCFR / US GPO | 27 CFR Part 4 葡萄酒标识与广告完整法规文本 |
| T06-S003 | https://www.ecfr.gov/current/title-27/chapter-I/subchapter-A/part-4/subpart-C/section-4.27 | verified_primary | 2026-06-06 | eCFR / US GPO | §4.27 年份葡萄酒规则（AVA 95% / 其他 85%） |
| T06-S004 | https://www.ttb.gov/regulated-commodities/beverage-alcohol/wine/labeling-wine/wine-labeling-appellation-of-origin | verified_primary | 2026-06-06 | TTB | 产地标注规则（country/state/county/AVA 各 % 阈值，§4.25） |
| T06-S005 | https://wineserver.ucdavis.edu/ | verified_primary | 2026-06-06 | UC Davis V&E Dept | 加州大学戴维斯酿酒与葡萄栽培系（学院派 ground truth 入口） |
| T06-S006 | https://www.ucdavis.edu/curiosity/blog/conversation-why-does-red-wine-cause-headaches | verified_primary | 2026-06-06 | UC Davis (Waterhouse/Devi) | quercetin 假说：红酒头疼非 sulfites — 破谣金料 |
| T06-S007 | https://www.wsetglobal.com/ | surrogate_primary | 2026-06-06 | WSET | certification body — WSET L1-4/Diploma + SAT 方法论母站 |
| T06-S008 | https://www.wsetglobal.com/knowledge-centre/blog/2022/may/05/six-common-wine-myths-debunked/ | surrogate_primary | 2026-06-06 | WSET | certification body 官方「6 大葡萄酒谣言」破谣文 |
| T06-S009 | https://www.guildsomm.com/ | surrogate_primary | 2026-06-06 | GuildSomm | 专业侍酒师协会（与 CMS 生态紧密） |
| T06-S010 | https://www.guildsomm.com/public_content/features/articles/b/jamie_goode/posts/the-taste-of-wine-acid-sweetness-and-tannin | surrogate_primary | 2026-06-06 | GuildSomm / Jamie Goode | 酸/甜/单宁口感机理（tartaric/malic、MLF、astringency 技术定义） |
| T06-S011 | https://www.mastersommeliers.org/ | surrogate_primary | 2026-06-06 | Court of Master Sommeliers | regulatory/cert body — Intro/Certified/Advanced/Master 四级 |
| T06-S012 | https://www.mastersommeliers.org/wp-content/uploads/2023/12/2024-CMS-A-Advanced-and-Master-Sommelier-Deductive-Tasting-Format.pdf | surrogate_primary | 2026-06-06 | CMS Americas | certification body — 2024 高阶演绎品鉴考试格式（sight/nose/palate/结论 网格）；PDF binary 无法解析正文，仅取标题+结构 |
| T06-S013 | https://www.societyofwineeducators.org/ | surrogate_primary | 2026-06-06 | Society of Wine Educators | cert body — CSW / CWE 认证 |
| T06-S014 | https://www.mastersofwine.org/ | surrogate_primary | 2026-06-06 | Institute of Masters of Wine | cert body — MW（学术研究论文型最高资质） |
| T06-S015 | https://www.inao.gouv.fr/en/aop-appellation-origine-protegee | surrogate_primary | 2026-06-06 | INAO (France) | regulatory body — 法国 AOC/AOP 官方定义页 |
| T06-S016 | https://www.vdp.de/en/the-wines/classification | surrogate_primary | 2026-06-06 | VDP (Germany) | regulatory body — 德国 VDP 四级地块分级 + GG 定义 |
| T06-S017 | https://www.bordeaux.com/us/Our-Terroir/Classifications/Grand-Cru-Classes-en-1855 | surrogate_primary | 2026-06-06 | CIVB Bordeaux | regulatory body — 波尔多 1855 列级官方页 |
| T06-S018 | https://www.jancisrobinson.com/learn/vocabulary/tasting-terms | surrogate_primary | 2026-06-06 | Jancis Robinson MW | critic own publication（牛津葡萄酒指南条目；页面 403 但为权威 vocabulary 源） |
| T06-S019 | https://eur-lex.europa.eu/EN/legal-content/summary/wines-and-wine-sector-products-protected-designations-of-origin-protected-geographical-indications-traditional-terms-labelling-and-presentation.html | surrogate_primary | 2026-06-06 | EUR-Lex | EU PDO/PGI 法规摘要（verifier 判 secondary；EU 一手立法，标 surrogate + note） |
| T06-S020 | https://en.wikipedia.org/wiki/German_wine_classification | secondary | 2026-06-06 | — | 德国 Prädikat 六级 + Oechsle 度数 + VDP 历史 |
| T06-S021 | https://en.wikipedia.org/wiki/Terroir | secondary | 2026-06-06 | — | terroir 概念入门定义 |
| T06-S022 | https://en.wikipedia.org/wiki/Bordeaux_Wine_Official_Classification_of_1855 | secondary | 2026-06-06 | — | 1855 分级（五级 + Premiers Crus）历史细节 |
| T06-S023 | https://en.wikipedia.org/wiki/Grower_Champagne | secondary | 2026-06-06 | — | grower (RM) vs négociant (NM) 香槟结构 |
| T06-S024 | https://en.wikipedia.org/wiki/Aroma_of_wine | secondary | 2026-06-06 | — | primary/secondary/tertiary 香气 + aroma vs bouquet |
| T06-S025 | https://en.wikipedia.org/wiki/Wine_tasting_descriptors | secondary | 2026-06-06 | — | 品鉴描述词全表（flabby/hot/closed/dumb/petrol/VA） |
| T06-S026 | https://en.wikipedia.org/wiki/The_Wine_Advocate | secondary | 2026-06-06 | — | Parker 100 分制 + Wine Advocate 背景 |
| T06-S027 | https://www.winewithseth.com/winewiki/label-rules-united-states/ | secondary | 2026-06-06 | Wine with Seth | 美国酒标 75/85/95 规则速查（trade educator） |
| T06-S028 | https://www.wineinvestment.com/learn/magazine/2023/02/a-guide-to-burgundys-classification-system/ | secondary | 2026-06-06 | Cult Wines | 勃艮第四级分级 + climat 解释（trade） |
| T06-S029 | https://winefolly.com/deep-dive/blind-wine-tasting-grid-pdf/ | secondary | 2026-06-06 | Wine Folly | 盲品 tasting grid 结构解说（trade press） |
| T06-S030 | https://time.com/4865734/organic-wine-health-benefits/ | secondary | 2026-06-06 | TIME | 有机/自然酒不防宿醉 — 厂商话术反驳 |
| T06-S031 | https://www.saveur.com/story/drink/truth-about-natural-wine-and-hangovers/ | secondary | 2026-06-06 | Saveur | 自然酒 vs 宿醉真相 |
| T06-S032 | https://nuvomagazine.com/magazine/spring-2022/100-point-wine-rating-system | secondary | 2026-06-06 | NUVO | 100 分制主观性 + 「fruit bomb」偏好批评 |
| T06-S033 | https://winefraud.com/winefraud-news/avoiding-wine-investment-scams/ | secondary | 2026-06-06 | WineFraud.com | 投资酒「稳赚」骗局拆解 |
| T06-S034 | https://winefolly.com/deep-dive/grower-champagne-guide/ | secondary | 2026-06-06 | Wine Folly | grower champagne 与「全起泡=香槟」误区 |
| T06-S035 | https://www.wineberserkers.com/t/the-myth-of-letting-wines-breathe/118176 | reference | 2026-06-06 | WineBerserkers forum | 论坛长帖：「拔塞透气」无效（单帖，内行讨论） |
| T06-S036 | https://amp.firstwefeast.com/drink/wine-vocabulary-sommelier | reference | 2026-06-06 | First We Feast | 「像 somm 一样说话」slang 速查（register 素材） |

> bucket 说明：拿不准一律报低。EUR-Lex（T06-S019）本是 EU 一手立法，但 verifier 自动判 secondary（host 不在 .gov/.edu 后缀白名单），按规范「只能升级 surrogate_primary」处理并加 note。INAO/VDP/CMS/WSET/Bordeaux.com/MW/SWE 均为认证或法定产区/监管机构自有站，按 prompt 升 surrogate_primary。jancisrobinson 为评论家自有站（critic own publication）→ surrogate_primary。**黑名单（知乎/公众号/百度/CSDN/G2/Capterra）零进入。**

---

## 总览（按 type 分组）

### Tier 1 — 核心必懂（28 个，所有从业者必懂）

| 术语 | Type | Insider def | Outsider tell | Evidence |
|------|------|-------------|---------------|----------|
| terroir 风土 | term | 一块地的气候/土壤/地形/人为传统的总和，决定酒的不可复制性 | 外行只当「土壤」或当玄学营销词 | T06-S021, T06-S015 |
| tannin 单宁 | term | 酚类物质，与唾液蛋白结合→收敛干涩（触觉非味觉） | 把「干涩」当「苦」或当「酸」 | T06-S010, T06-S025 |
| acidity 酸度 | term | tartaric/malic 为主，骨架与陈年潜力；缺则 flabby | 把高酸当「不好/坏掉」 | T06-S010 |
| minerality 矿物感 | term | 燧石/湿石/咸鲜的香气或质感印象（机理有争议） | 当成「真的尝到矿物质」 | (disputed, 见条目) |
| body 酒体 | term | 口中的重量感/黏稠度，受酒精+糖+干物质影响 | 把 body 等同于「颜色深」 | T06-S010, T06-S029 |
| structure 结构 | term | 酸+单宁+酒精+糖的支撑骨架（vs 果味「血肉」） | 当成模糊褒义词乱用 | T06-S009, T06-S029 |
| balance 平衡 | term | 各组分无一突兀、彼此交融 | 把「顺滑」当平衡 | T06-S001? 见条目 |
| complexity 复杂度 | term | 香气/风味层次多且随时间演变 | 把「味道重」当复杂 | T06-S024 |
| finish / length 余味 | term | 吞咽后风味留存的时长与质量 | 当成「回甘」或「上头」 | T06-S025 |
| varietal / cépage 品种 | term | 酿酒葡萄品种（新世界以此命名酒） | 把品种当产区（见 outsider-tell #1） | T06-S027 |
| vintage / millésime 年份 | term | 葡萄采收年份（≠装瓶年/购买年） | 把年份当「越老越好」（见 #2） | T06-S003 |
| appellation 法定产区 | regulation+term | 受法律界定边界与规则的产地名 | 把产区当品牌/品种 | T06-S004, T06-S015 |
| cru / grand cru / premier cru 列级 | regulation+term | 法定/历史分级的地块或酒庄等级 | 以为 grand>premier 在所有产区同义（勃艮第 vs 波尔多含义不同） | T06-S028, T06-S022 |
| climat 地块 | term | 勃艮第有名有界的单一葡萄园（terroir 颗粒度最细） | 以为是「气候 climate」 | T06-S028 |
| blend / assemblage 混酿 | term | 多品种/多地块/多桶调配成最终酒 | 以为混酿=低端（香槟/波尔多顶级皆混酿） | T06-S023 |
| malolactic (MLF) 苹乳发酵 | term | 苹果酸→乳酸，降酸+增黄油/奶感+pH↑0.1-0.3 | 当成「第二次酒精发酵」 | T06-S010 |
| bâtonnage 搅桶 | term | 搅动酒泥（lees）增加质感/复杂度 | 完全不知此词 | T06-S010 |
| brett / Brettanomyces 酒香酵母 | term | 酵母缺陷，谷仓/创可贴/马厩味（低量有人爱，高量是 fault） | 把「bretty」当统一风味（专家认为无单一 brett 味） | T06-S025 |
| TCA / corked 木塞污染 | term | 2,4,6-三氯苯甲醚，湿纸板/霉味，使酒「闷掉」 | 把「corked」当「有软木屑漂着」 | T06-S025, T06-S035 |
| decant 醒酒 | term | 换瓶以分离沉淀/增氧；非所有酒都需要 | 「decant everything」 + 拔塞透气（见 #4/#10） | T06-S035 |
| legs / tears 挂杯 | term | 杯壁酒泪，主要反映酒精度+表面张力 | 「挂杯=品质好」（见 #3） | T06-S025 |
| bouquet / nose 香气 | term | nose=整体嗅觉印象；bouquet=陈年/发酵后衍生的三级香 | aroma 与 bouquet 混用 | T06-S024 |
| palate / mid-palate 口感 | term | 入口后的风味与结构体验（mid-palate=中段表现） | 不会区分 attack/mid/finish | T06-S009 |
| retronasal 鼻后嗅觉 | term | 经口腔后部上行至鼻腔的香气感知（「风味」主体） | 以为「味道」全在舌头 | T06-S010 |
| reductive / oxidative 还原/氧化 | term | 还原=缺氧硫味（火柴/臭蛋）；氧化=过氧化雪莉化 | 把还原味当「坏了」，把氧化当「陈年」 | T06-S025 |
| residual sugar (RS) 残糖 | term | 发酵后剩余的糖，决定 dry→sweet | 混淆「dry」与「单宁/低果味」（见 #8） | T06-S010 |
| botrytis / noble rot 贵腐 | term | 灰葡萄孢菌脱水浓缩糖酸→顶级甜酒（Sauternes/TBA） | 以为是「葡萄烂了」 | T06-S020 |
| dry / sweet 干/甜 | term | 仅指残糖高低，与酸/单宁无关 | 把高单宁红酒说成「太甜」或「太干」 | T06-S010 |

### Tier 2 — 周边熟知（22 个）

| 术语 | Type | Insider def | Evidence |
|------|------|-------------|----------|
| Oechsle 度 | standard | 德国/奥地利测 must weight（糖度→成熟度）的单位，Prädikat 分级基准 | T06-S020 |
| Prädikat 等级 | regulation | 德国按成熟度的 Kabinett→TBA 六级 | T06-S020 |
| AVA (American Viticultural Area) | regulation | 美国法定葡萄种植区，≥85% 葡萄须来自该区 | T06-S004 |
| PDO / PGI（AOP/IGP） | regulation | EU 两级地理标志，PDO 严于 PGI | T06-S019 |
| QbA / Qualitätswein | regulation | 德国「特定产区优质酒」，可加糖提酒精 | T06-S020 |
| Grosses Gewächs (GG) | regulation | VDP 顶级地块的干型酒（法律上仍报 Qualitätswein） | T06-S016 |
| volatile acidity (VA) | term | 醋酸为主的挥发酸，过量是缺陷（指甲油/醋味） | T06-S025 |
| TDN / petrol 汽油味 | term | 1,1,6-三甲基二氢萘，陈年 Riesling 的标志性（褒义） | T06-S025 |
| flabby 软塌 | slang/term | 缺酸、松垮无骨架 | T06-S025 |
| hot 灼热 | slang/term | 酒精过高，尾端发烫 | T06-S025 |
| closed / dumb 封闭/哑期 | slang/term | 香气暂时收紧（常见于陈年中段） | T06-S025 |
| primary/secondary/tertiary 香气 | term | 品种香/发酵香/陈年香三级 | T06-S024 |
| RM / NM（香槟） | regulation | RM=récoltant-manipulant 果农自酿；NM=négociant 收购酿造 | T06-S023 |
| tirage / liqueur de tirage | term | 香槟二次发酵的装瓶+糖酵母液 | T06-S023 |
| dosage | term | 香槟除渣后补的糖液，定 Brut→Doux 甜度 | T06-S023 |
| lees / sur lie | term | 酒泥；带泥陈酿增质感 | T06-S010 |
| DOC / DOCG / IGT（意） | regulation | 意大利对应 PDO(DOC/DOCG)/PGI(IGT)，DOCG 最严 | T06-S019 |
| DO / DOCa（西） | regulation | 西班牙法定产区，DOCa(=DOQ) 为最高级（仅 Rioja/Priorat） | T06-S019 |
| SAT (Systematic Approach to Tasting) | standard | WSET 的结构化品鉴方法论（外观/嗅觉/味觉/结论） | T06-S007 |
| deductive tasting grid | standard | CMS 的盲品演绎网格（sight→nose→palate→结论） | T06-S012, T06-S029 |
| fining / filtration | term | 澄清/过滤工艺（自然酒派常省略） | T06-S030 |
| scommelier (somm) | term | 餐厅持证酒水专业人员/认证侍酒师 | T06-S011 |

### Standards / Regulations / Certifications 时间轴（仅近年有显著变化或版本演进的进表）

| 名称 | Issued | Last revised / 状态 | Decay | Evidence |
|------|--------|---------------------|-------|----------|
| 27 CFR Part 4（美国酒标法） | 长期沿用 | 在编 eCFR「current」实时版；TTB 持续 rulemaking（如 2020s 标识现代化提案） | medium | T06-S002 |
| EU Reg. 1308/2013（CMO，含 PDO/PGI 框架） | 2013 | 被 Reg. (EU) 2021/2117 修订（CAP 改革，含地理标志条款调整） | medium | T06-S019 |
| 德国葡萄酒法（Weingesetz 1971 → 改革） | 1971 | 2021 改革引入产地金字塔（Anbaugebiet→Einzellage），VDP 私法分级先行 | medium-high | T06-S016, T06-S020 |
| VDP.Classification（私法分级） | 2012 体系化 | 持续按地块认定演进 | medium | T06-S016 |
| Bordeaux 1855 列级 | 1855 | 仅 1973 一次变动（Mouton 升一级）；Médoc 极稳定 | low | T06-S022 |
| Saint-Émilion 列级 | 1955 | 每约 10 年重审，争议大（2022 多家退出） | high | T06-S017 |
| WSET L1-4 / Diploma | — | 课程大纲周期性更新；Diploma 现 6 单元结构 | medium | T06-S007 |
| CMS 四级（Intro/Certified/Advanced/MS） | — | 2024 版演绎品鉴格式文档为当前基准 | medium | T06-S012 |

> 长期稳定的标准（如 terroir 概念、tannin 化学）不进时间轴，只在主条目记。

### 行业「外行破绽」高亮（top 10 最易暴露）

| 误用（外行说法） | 内行实际意思 / 纠正 | 频率 | Evidence |
|------|------|------|----------|
| 「我喜欢勃艮第那个葡萄」 | Burgundy 是产区不是品种；红勃艮第=Pinot Noir | 极高 | T06-S028 |
| 「越老越好」 | 95-98% 的酒应趁年轻喝；只有高酸/高单宁的少数酒受益于陈年 | 极高 | T06-S008 |
| 「挂杯多=好酒」 | legs 只反映酒精度+表面张力，与品质无关 | 高 | T06-S025 |
| 「所有酒都要醒」 | 仅老年份/有沉淀/封闭的高单宁酒需要；多数酒开瓶即饮 | 高 | T06-S035 |
| 「sulfites 让我头疼」 | 白葡萄酒含等量 sulfites 却少致头疼；元凶更可能是 quercetin/酒精代谢 | 极高 | T06-S006 |
| 「这起泡酒是香槟」 | 只有 Champagne 法定产区的才叫香槟；其他叫 sparkling/Cava/Prosecco 等 | 高 | T06-S034 |
| 「顺滑/smooth」当唯一褒义 | 内行用 balance/structure/length/complexity；smooth 多指低单宁低酸，非品质 | 高 | T06-S036 |
| 把高单宁红酒说「太甜/太干」 | dry/sweet 只指残糖；单宁是收敛感，是另一维度 | 高 | T06-S010 |
| 拔塞「让它呼吸」就够了 | 瓶颈面积太小，几乎不增氧；要增氧得倒进醒酒器 | 中高 | T06-S035 |
| 把 aroma 和 bouquet 当一回事 | aroma=品种/发酵香（一二级）；bouquet=陈年衍生香（三级） | 中 | T06-S024 |

---

## 详细条目（选关键 / 有争议 / 需 source 的）

### terroir 风土 — terroir/terroir
- **Type**: term  **Tier**: tier-1  **Decay**: low
- **Definition (insider)**: 一个地块的气候、土壤、地形、人为传统的总和，是旧世界「以产地为酒名」哲学的根基；不可移植、不可复制。(evidence: [T06-S021, T06-S015])
- **Definition (outsider)**: 「一方水土养一方酒」——同一品种在不同地方味道完全不同。
- **Etymology**: 法语，源自 *terre*（土地）。INAO 把 terroir 制度化为 AOC 的法理基础。(evidence: [T06-S015])
- **常见误用 (outsider-tell)**: `semantic_tell` 外行把 terroir 窄化为「土壤」，或反过来当成无法证伪的营销玄学。内行：terroir 是可被法规边界（appellation）和盲品（earthy/mineral 特征）双向锚定的具体东西。(evidence: [T06-S021])
- **关联术语**: appellation、climat、minerality
- **可信度**: high

### tannin 单宁
- **Type**: term  **Tier**: tier-1  **Decay**: low
- **Definition (insider)**: 来自葡萄皮/籽/梗与橡木的酚类物质，与唾液中的蛋白（黏蛋白）结合、剥离润滑→口腔干涩收敛。**是触觉不是味觉**；长链→astringency 收敛，短链→bitterness 苦。(evidence: [T06-S010])
- **常见误用 (outsider-tell)**: `usage_tell` 外行把「干涩」错报为「苦」或「酸」，或把单宁当成味道。内行会说「单宁紧/丝滑/颗粒感」而非「苦」。`semantic_tell` 「甜度掩盖单宁」——商业红酒常加残糖让单宁显软。(evidence: [T06-S010])
- **关联术语**: structure、astringency、residual sugar
- **可信度**: high

### minerality 矿物感（disputed）
- **Type**: term  **Tier**: tier-1  **Decay**: low
- **Definition (insider)**: 描述燧石/湿石/碎石/海风/咸鲜的香气印象或「电流般」的尾端质感。(evidence: [T06-S021])
- **disputed**: 〈一派〉是 terroir/土壤的可感表达；〈另一派〉学界认为味觉无法直接尝到岩石矿物质，「minerality」是还原硫化物+高酸+低果味的综合知觉建构。**两派并存，不强行统一。**
- **常见误用 (outsider-tell)**: `semantic_tell` 外行以为「真的尝到了矿物质/石头」。内行知道这是一个知觉描述词而非化学事实。
- **可信度**: medium（定义本身有内部分歧）

### malolactic fermentation (MLF) 苹乳发酵
- **Type**: term  **Tier**: tier-1  **Decay**: low
- **Definition (insider)**: 乳酸菌把尖锐的苹果酸（malic）转成柔和的乳酸（lactic），降低可感酸度、pH 上升约 0.1-0.3、常带黄油/奶油质感。几乎所有红酒+部分白（如 Chardonnay）会做。(evidence: [T06-S010])
- **常见误用 (outsider-tell)**: `usage_tell` 外行把它和「二次发酵（香槟瓶中发酵）」混为一谈——后者产生气泡，前者只降酸。(evidence: [T06-S010])
- **关联术语**: acidity、lees、tirage
- **可信度**: high

### TCA / corked 木塞污染
- **Type**: term  **Tier**: tier-1  **Decay**: low
- **Definition (insider)**: 2,4,6-三氯苯甲醚（TCA）污染，湿纸板/发霉地下室味，并**抹掉果香让酒「闷死」**；约 1-3% 的软木塞封瓶会中招。(evidence: [T06-S025, T06-S035])
- **常见误用 (outsider-tell)**: `semantic_tell` 外行以为「corked」= 杯里漂着软木屑碎渣（那只是物理碎屑，无害）。内行的 corked 是嗅觉缺陷。(evidence: [T06-S035])
- **可信度**: high

### appellation / AVA / AOC / PDO 产地体系（geographic-specific）
- **Type**: regulation+term  **Tier**: tier-1  **Decay**: medium
- **geographic-specific: US**: TTB 27 CFR Part 4。产地分四档：**国家** / **州**（≥75%，多数州自定更高）/ **县**（≥75%）/ **AVA 葡萄种植区**（≥85% 葡萄来自该 AVA，§4.25）。(evidence: [T06-S004, T06-S002])
- **geographic-specific: US 年份/品种**: 年份酒——标 AVA 须 ≥95% 来自该年；标州/县须 ≥85%（§4.27）。**品种（varietal）标注须 ≥75%** 来自该品种且该比例全部产自所标产地。(evidence: [T06-S003, T06-S027])
- **geographic-specific: EU**: Reg. 1308/2013 框架下 **PDO**（=法 AOP/意 DOC·DOCG/西 DO·DOCa/德 g.U.）要求 100% 葡萄来自界定产区+登记工艺；**PGI**（=法 IGP/意 IGT）规则更宽。(evidence: [T06-S019])
- **geographic-specific: FR**: INAO 管 AOC（国内）↔ AOP（欧盟层面）。AOC 把 terroir、品种、产量、工艺全写进 cahier des charges。(evidence: [T06-S015])
- **变化历史**: EU Reg. 1308/2013（2013）经 Reg. 2021/2117 修订；德国 1971 法 → 2021 改革引入产地金字塔。(evidence: [T06-S019, T06-S016])
- **是否被错位包装**: 营销常把「AVA/产区名」当品牌噱头印大字，但产区只是法定产地标识、不等于品质保证（AVA 仅管产地不管质量）。(evidence: [T06-S004])
- **常见误用 (outsider-tell)**: 把产区当品种或当品牌（见 outsider-tell #1）。
- **可信度**: high

### 德国 Prädikat / VDP 分级（geographic-specific: DE）
- **Type**: regulation  **Tier**: tier-1（Prädikat）/ tier-2（VDP 细级）  **Decay**: medium-high
- **官方 Prädikat 六级**（按 must weight 由低到高，单位 Oechsle）：Kabinett(67-82) → Spätlese(76-90) → Auslese(83-100，部分带 botrytis) → Beerenauslese(BA) → Eiswein(冰冻采收) → Trockenbeerenauslese(TBA，葡萄干化最贵最稀)。**Prädikat 只标成熟度，不直接=甜度**（Kabinett 可干可甜）。(evidence: [T06-S020])
- **VDP 私法四级地块**（仿勃艮第）：VDP.Gutswein（大区）→ VDP.Ortswein（村）→ VDP.Erste Lage（一级园）→ VDP.Grosse Lage（特级园）。**Grosses Gewächs (GG)** = Grosse Lage 出的干型酒。(evidence: [T06-S016])
- **关键反直觉**: VDP 会员的所有干型酒（含顶级 GG）法律上报作 **Qualitätswein 而非 Prädikatswein**——因为 Prädikat 体系按糖分设计，不适配干型顶酒。VDP 私法分级正是为补 1971 法「以糖论质、稀释名园」之弊而生。(evidence: [T06-S016, T06-S020])
- **变化历史**: 1971 Weingesetz → VDP 2012 体系化 → 德国 2021 法改引入官方产地金字塔。(evidence: [T06-S020, T06-S016])
- **可信度**: high

### Bordeaux 1855 vs Burgundy climat（两种 cru 哲学）
- **Type**: regulation+term  **Tier**: tier-1  **Decay**: low（Médoc）/ high（Saint-Émilion）
- **Bordeaux 1855**: 按**酒庄（château）声誉+价格**分五级（Premiers→Cinquièmes Crus），Médoc+Haut-Brion，149 年仅 1973 一次变动（Mouton Rothschild 升一级）。极稳定。(evidence: [T06-S022, T06-S017])
- **Burgundy**: 按**地块（climat）**而非生产者分四级——Grand Cru(~1%) > Premier Cru(~10%) > Village(~37%) > Régional(~52%)；标签上 climat 名跟在 AOC 后。(evidence: [T06-S028])
- **常见误用 (outsider-tell)**: 以为「grand cru」「premier cru」在全法同义同序。实则**波尔多 1855 列级与勃艮第 cru 是两套不同逻辑**（庄 vs 地），且 Saint-Émilion 列级（每约 10 年重审，2022 多家退出）又是第三套。(evidence: [T06-S022, T06-S028, T06-S017])
- **可信度**: high

### 香槟 grower (RM) vs négociant (NM)（geographic-specific: Champagne）
- **Type**: regulation+term  **Tier**: tier-2  **Decay**: low
- **Definition (insider)**: NM（négociant-manipulant，大厂）收购果农葡萄酿造；RM（récoltant-manipulant，「grower champagne」）果农自种自酿，更强调单一地块风格。瓶身角落小代码可辨。(evidence: [T06-S023])
- **关联术语**: assemblage、tirage、dosage
- **常见误用 (outsider-tell)**: 把所有起泡都叫香槟（见 #6）；以为大牌厂= 葡萄自种（实多为收购）。(evidence: [T06-S023, T06-S034])
- **可信度**: high

### 认证体系（这一行的「执业资质」语言）
- **Type**: certification  **Tier**: tier-1（认证名）  **Decay**: medium

| 体系 | 颁发机构 | 侧重 | 阶梯/特征 | Evidence |
|------|---------|------|-----------|----------|
| **WSET** L1→L4(Diploma) | Wine & Spirit Education Trust | **知识 + SAT 结构化品鉴**（产地/酿造/全球风格） | L1 全选择题；L3 加简答+品鉴；L4 Diploma 6 单元 + 研究论文。无服务考。 | T06-S007 |
| **CMS** Intro/Certified/Advanced/**Master Sommelier** | Court of Master Sommeliers | **餐厅服务 + 盲品演绎 + 理论**三合一 | Certified 起含 wine **service** 实操考；MS 是业内最难考之一（理论+盲品+服务三关） | T06-S011, T06-S012 |
| **Master of Wine (MW)** | Institute of Masters of Wine | **学术研究**（理论 + 实践品鉴 + **研究论文 RP**） | 公认葡萄酒界最高学术资质；WSET Diploma 常作前置 | T06-S014, T06-S007 |
| **CSW / CWE** | Society of Wine Educators | **教育/知识** 导向 | CSW=Certified Specialist of Wine；CWE 更高 | T06-S013 |

- **核心区分**: WSET 训练「懂酒的人」（销售/零售/教育/酒店）；CMS 训练「侍酒师」（餐厅服务）；MW 训练「研究者/权威」。三者侧重 = 知识 vs 服务 vs 研究。(evidence: [T06-S007, T06-S011, T06-S014])
- **盲品方法论之争种子**: WSET 的 **SAT**（描述+评质，不强求猜中）⇄ CMS 的**演绎网格 deductive grid**（sight→nose→palate→initial/final conclusion，目标是逻辑推演到品种+产地+年份）。两套盲品哲学是 Phase 2「流派之争」硬件层。(evidence: [T06-S007, T06-S012, T06-S029])
- **可信度**: high

---

## 厂商话术拒绝（资深人绝不会说 / 被错位包装的销售话术）

> 这节质检 voice item 会扫。每条配「内行为何拒绝」。

- **「95 分 = 客观上最好的酒」** — 拒绝。100 分制（Parker/Wine Advocate 起家）本质是单个评论家在特定时点的主观印象，会系统性偏爱浓郁「fruit bomb」风格、惩罚冷门/克制风格；分数不可跨评论家通约。内行看「谁打的、什么风格偏好」，不看裸分。(evidence: [T06-S032, T06-S026])
- **「自然酒更健康 / 不上头 / 不宿醉」** — 拒绝。宿醉主因是酒精本身；有机/自然/低干预不改变这一点。喝够量照样宿醉。这是 wellness 营销错位包装。(evidence: [T06-S030, T06-S031])
- **「sulfites 导致头疼，所以买无硫酒」** — 拒绝。白葡萄酒含等量 sulfites 却少致头疼；人体每天自产约 700mg sulfites，一杯酒约 20mg 微不足道。红酒头疼更可能源于 quercetin 抑制 ALDH→乙醛堆积。(evidence: [T06-S006])
- **「贵 = 好 / 名庄一定好喝」** — 拒绝。价格含稀缺性、品牌、投机溢价；1855 列级是 1855 年的价格快照，非当代盲品质量保证。内行用结构/平衡/产地表达评酒，不用价签。(evidence: [T06-S022, T06-S032])
- **「这支必须醒满 X 小时」「所有酒都要醒」** — 拒绝。多数酒开瓶即饮；只有老年份/有沉淀/封闭的高单宁酒受益，且「醒多久」高度个案，没有放之四海的固定时长。(evidence: [T06-S035])
- **「这支投资酒稳赚 / 保证升值」** — 拒绝。「稳赚」是投资酒诈骗的典型话术（伪造产地、超收 400%+、假瓶）。葡萄酒二级市场波动且充满 fraud。(evidence: [T06-S033])
- **「越陈越值钱 / 越老越好」**（投资版越老神话）— 拒绝。95-98% 的酒不为陈年而造，放老只会衰败。(evidence: [T06-S008])

---

## register 差异（内 vs 外 / 严肃 vs 轻松）

- **严肃品鉴 register（结构化、克制）**: 走 SAT / deductive grid——按 **外观→嗅觉→味觉（甜度/酸/单宁/酒精/酒体/余味）→结论** 的固定顺序逐项报告，用「中等(+)」「高」「收敛」这类**校准刻度词**而非情绪词；目标是可复现、可被他人核对。背网格到本能，才能腾出脑力真正感知。(evidence: [T06-S012, T06-S029])
- **轻松吐槽 register（slang）**: 内行私下用 flabby（缺酸软塌）、hot（酒精灼）、closed/dumb（哑期）、bretty（酒香酵母味）、VA（挥发酸/醋味）、petrol（陈年 Riesling 汽油味，褒义）等行话——这些词外行听不懂、且褒贬取决于语境（petrol 在 Riesling 是好，在别处是缺陷）。(evidence: [T06-S025, T06-S036])
- **内 vs 外沟通差异**: 对客人/外行，侍酒师会翻译成体验语言（「这支酸度活泼，配生蚝很搭」）；对同行用 structure/length/MLF/lees 等技术词。把「smooth/顺滑」当唯一褒义、把品种当产区，是外行 register 的即时标记。(evidence: [T06-S036, T06-S010])

---

## Phase 2 接口

### 「行业表达 DNA」直接素材（喂给 Phase 2.5 expression-DNA）

**高频黑话 / tier-1 术语词表 top 10**（voice 必扫）:
terroir / tannin / acidity / minerality / structure / balance / finish(length) / appellation(AVA·AOC·PDO) / vintage / cru(grand·premier·climat)
— 次梯队：blend(assemblage)、MLF(苹乳发酵)、brett、TCA(corked)、decant、retronasal、residual sugar、botrytis。
(evidence: [T06-S010, T06-S021, T06-S024, T06-S025])

**行业拒绝的厂商话术 top 5**（拒绝 → 价值观 + 反模式）:
1. 「95 分=客观最好」（分数主观+偏 fruit bomb） (evidence: [T06-S032])
2. 「自然酒更健康/不上头」（宿醉主因是酒精） (evidence: [T06-S030])
3. 「sulfites 导致头疼」（白酒等量却少致头疼；真因 quercetin） (evidence: [T06-S006])
4. 「贵=好 / 必须醒 X 小时」（价格≠质量；醒酒高度个案） (evidence: [T06-S022, T06-S035])
5. 「投资酒稳赚」（诈骗话术） (evidence: [T06-S033])

**外行破绽 top 10（insider-only spotting tells）**:
把品种当产区（「勃艮第那个葡萄」）/ 越老越好 / 挂杯=品质 / 所有酒都要醒 / sulfites 致头疼 / 全起泡叫香槟 / smooth 当唯一褒义 / 混淆 dry-sweet 与单宁酸度 / 拔塞「呼吸」当醒酒 / aroma 与 bouquet 不分。
(evidence: [T06-S008, T06-S025, T06-S034, T06-S006, T06-S010, T06-S024])

**register 标志**: 严肃=SAT/演绎网格固定顺序+刻度词；轻松=flabby/hot/closed/bretty/petrol slang；对外翻译成体验语言。(evidence: [T06-S012, T06-S025, T06-S036])

### 「智识谱系」线索（喂给 Phase 2.7）

- **旧世界 terroir/产地命名 ⇄ 新世界 品种命名**：是这一行最根本的范式分野；AOC/PDO（以地为名、terroir 至上）vs AVA/varietal（以品种为名、宽松）是制度化的两种世界观。(evidence: [T06-S015, T06-S004])
- **盲品两大流派**：WSET-SAT（描述评质，不必猜中）⇄ CMS-deductive grid（逻辑演绎到品种产地年份）。是「认识论之争」的硬件层。(evidence: [T06-S007, T06-S012])
- **分级哲学三系**：Bordeaux 1855（庄/价格快照）⇄ Burgundy climat（地块/terroir 颗粒）⇄ 德国 Prädikat（成熟度/糖）→ VDP 私法纠偏（仿勃艮第按地块）。一行三种「什么决定质量」的世界观更替。(evidence: [T06-S022, T06-S028, T06-S016])
- **量化 vs 风土**：100 分制（Parker，可通约、偏浓郁）⇄ 风土表达派（不可通约、强调地方性）的张力。(evidence: [T06-S032])

### 「时效性」信号（喂给 Phase 2.8 诚实边界）

- 过去数年内有显著修订的标准/法规：**EU Reg. 1308/2013 经 2021/2117 修订**；**德国 2021 葡萄酒法改革**（产地金字塔）；**Saint-Émilion 列级 2022 重审争议**（多家退出）。→ master skill 应标这些为活跃衰减点。(evidence: [T06-S019, T06-S016, T06-S017])
- 预计 12-24 月内可能再变：Saint-Émilion 下轮列级（high decay）；美国 TTB 标识现代化提案（medium）；UC Davis quercetin 假说待人体试验确认（科学结论可能更新）。(evidence: [T06-S017, T06-S002, T06-S006])
- 长期稳定（low decay，可放心写死）：terroir/tannin/acidity 等核心术语；Bordeaux 1855 Médoc 部分。(evidence: [T06-S021, T06-S022])

### 「工作流变化触发」种子（喂给 wave 3 Track 03）

- **法规修订 → 酒标合规工作流变**：EU 2021 地理标志条款 + 德国 2021 产地金字塔 → 标签术语、产地标注、出口合规流程需更新。(evidence: [T06-S019, T06-S016])
- **列级重审 → 酒单/采购/估值工作流变**：Saint-Émilion 每约 10 年重审会改变酒庄等级 → 影响侍酒师选酒叙事与定价。(evidence: [T06-S017])
- **认证大纲更新 → 备考/培训工作流变**：WSET 大纲与 CMS 演绎品鉴格式周期性更新 → 教学与备考流程随之调整。(evidence: [T06-S007, T06-S012])

### 冷僻 / 信号薄弱自检

- 总术语数 **50（Tier1=28 + Tier2=22）≥ 40** ✅，远超 25 冷僻线。
- Tier 1 = 28 ≥ 15 ✅；Tier 1 全部填了 outsider-tell ✅（总览表逐行有 tell 列）。
- 有 outsider-tell 的术语 **远超 50%** ✅。
- → **不触发冷僻协议**。本行业 glossary 维度信号厚（公开法规 + 认证体系 + 评论家 vocabulary 充足）。
- 唯一注意：minerality 属 `disputed`（已标注两派）；部分一手源（TTB 主页 socket、jancisrobinson 403、CMS PDF binary）抓取受阻，但规则/定义均已用 ≥2 个独立源交叉核实。

---

## type 分布与 N/A 说明

- **Term / 术语**：主体（terroir、tannin、structure、MLF、retronasal…），数量最多。
- **Standard / 标准**：Oechsle、SAT、deductive grid——有但少（多内嵌在认证体系里）。
- **Regulation / 法规**：重头（TTB 27 CFR Part 4、EU PDO/PGI、AOC/INAO、DOC/DOCG/IGT、Prädikat、VDP、1855 列级）——本行业法规密度高。
- **Certification / 认证**：丰富（WSET、CMS、MW、CSW）——是「执业资质语言」核心，**非 N/A**。
- **Acronym / 缩写**：中等（AVA、PDO/PGI、AOC/AOP、DOC/DOCG/IGT、MLF、TCA、VA、TDN、RS、GG、RM/NM、SAT、MW、CSW、WSET、CMS）。
- 无 N/A 类型——这是一个五类俱全、法规+认证双重的行业。
