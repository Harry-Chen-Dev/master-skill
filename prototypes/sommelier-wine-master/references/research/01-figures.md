# Track 01 — Figures（行业大佬 / thought leaders）：侍酒师 / 葡萄酒（Sommelier & Wine）

> Phase 1 wave 2 research subagent 输出。行业 = 葡萄酒鉴赏 + 侍酒服务的职业认知 OS。locale = global / **en+fr-primary**。
> 核心张力：codifiable 理论层（产区/品种/酒法/风土/酿造）⇄ tacit 校准层（味觉记忆/盲品/侍酒服务）。本 track 把这层张力落到「人」上 —— 每个流派的奠基人与当前代表。
> 范围：top 18 figures（逐人：思维 DNA + 头衔 + 代表作 + 读/听/看 3 件 + 争议立场 + 近 12 月动态 + 流派）+ 5 组流派智识谱系（奠基人→当前代表→核心分歧）。
>
> **中英失衡警告（贯穿全文，Phase 2.8 诚实边界要用）**：葡萄酒 thought leaders 几乎全部英文（+法文）。**中文原创一手 figure ≈ 0**：中文世界以 WSET 中国讲师 / 公众号大号转述为主，无一人在英文 canon / 评论 / 长访谈生态里被多源点名为奠基人或当前代表。下面 18 位无一以中文为一手语言。**本 track 不为凑数编造中文 figure**（见结尾自检）。

## Source Manifest

> bucket 规则（照搬 Wave 1 口径）：只有 `.edu`/`.gov`/`.ac.uk`/`arxiv` 自动判 `verified_primary`。**认证机构**（mastersofwine.org / mastersommeliers.org / wsetglobal.com / guildsomm.com）→ `surrogate_primary` + note 含 `certification body`。**评论家 / figure 自有出版站**（jancisrobinson.com / vinous.com / timatkin.com / wineanorak.com / winefolly.com / winespeed.com / rawwine.com / illdrinktothatpod.com / winefornormalpeople.com / josevouillamoz.com / winespecific.com / content.robertparker.com / coulee-de-serrant.com）→ `surrogate_primary` + note 含 `critic own publication`。trade media（decanter / winespectator / punchdrink / vinepair / worldoffinewine / drinksint）+ wikipedia → `secondary`。论坛 / 单帖 → `reference`。中文 blacklist（知乎/公众号/百度/CSDN）零进入。
> **source_verifier classify 已逐条跑（2026-06-06）**：所有 critic-own-site / 认证机构 verifier 默认判 `secondary`，本表按 manifest 逃生阀人工升级 `surrogate_primary` 并加 keyword note（合规，与 Track 04/05/06 一致）。**例外标注**：`winespecific.com/about`（Lewin 个人博客）verifier 误判 `verified_primary`（疑似路径规则误触）—— 它是 critic own publication，**不是** .edu/.gov 真一手，故**人工下调为 `surrogate_primary`**（绝不标得比真实来源高，rule 3）。blacklisted=0、dead 链未发现。

| source_id | url | bucket | last_checked | author/host | one-line note |
|-----------|-----|--------|--------------|-------------|---------------|
| T01-S001 | https://www.jancisrobinson.com/how-we-score | surrogate_primary | 2026-06-06 | Jancis Robinson MW (+team) | critic own publication — 20 分制评分哲学官方页（一手立场） |
| T01-S002 | https://www.jancisrobinson.com/articles/how-to-score-wine | surrogate_primary | 2026-06-06 | Jancis Robinson MW | critic own publication — 「如何给酒评分」长文（反百分制论证一手） |
| T01-S003 | https://www.mastersofwine.org/jancis-robinson-obe-mw | surrogate_primary | 2026-06-06 | Institute of Masters of Wine | certification body — Jancis MW 简介（首位非酒商出身 MW） |
| T01-S004 | https://www.mastersofwine.org/julia-harding-mw | surrogate_primary | 2026-06-06 | Institute of Masters of Wine | certification body — Julia Harding MW 简介（2004 MW, Mondavi 奖） |
| T01-S005 | https://www.mastersofwine.org/isabelle-legeron-mw | surrogate_primary | 2026-06-06 | Institute of Masters of Wine | certification body — Legeron MW 简介（法国首位女 MW） |
| T01-S006 | https://www.jancisrobinson.com/team | surrogate_primary | 2026-06-06 | JancisRobinson.com | critic own publication — 团队页（Harding/Currin/Yarrow 等编制） |
| T01-S007 | https://en.wikipedia.org/wiki/Robert_Parker_(wine_critic) | secondary | 2026-06-06 | — | Parker 生平 + 100 分制 + Parkerization 批评（史实/二手） |
| T01-S008 | https://content.robertparker.com/the-truth-about-parkerization | surrogate_primary | 2026-06-06 | Robert Parker / Wine Advocate | critic own publication — Parker 阵营反驳「Parkerization」（一手自辩，反例不软化） |
| T01-S009 | https://punchdrink.com/articles/robert-parker-wine-parkerization/ | secondary | 2026-06-06 | PUNCH (Talia Baiocchi 编) | trade media — 「葡萄酒文化误读了 Parker」重估长稿 |
| T01-S010 | https://vinepair.com/articles/robert-parker-wine-critic-legacy/ | secondary | 2026-06-06 | VinePair | trade media — Parker 遗产重估（同质化批评史实） |
| T01-S011 | https://www.decanter.com/wine-news/robert-parker-retires-from-the-wine-advocate-414067/ | secondary | 2026-06-06 | Decanter | trade media — Parker 2019 退休 Wine Advocate（时间锚） |
| T01-S012 | https://en.wikipedia.org/wiki/Antonio_Galloni | secondary | 2026-06-06 | — | Galloni 生平（前 Wine Advocate→2013 创 Vinous）（史实） |
| T01-S013 | https://vinous.com/ | surrogate_primary | 2026-06-06 | Antonio Galloni (Vinous) | critic own publication — Vinous 主站（产区报告+视频+地图，每日流） |
| T01-S014 | https://wineanorak.com/2021/05/04/the-wine-critics-what-are-we-to-make-of-vinous-preview/ | surrogate_primary | 2026-06-06 | Jamie Goode (wineanorak) | critic own publication — 批 Vinous Preview「站到 trade 一边」（争议一手） |
| T01-S015 | https://en.wikipedia.org/wiki/Hugh_Johnson_(wine_writer) | secondary | 2026-06-06 | — | Hugh Johnson 生平（World Atlas/Pocket Book，4M+ 册）（史实） |
| T01-S016 | https://www.amazon.com/Hugh-Johnsons-Pocket-Wine-Book/dp/1784729590 | secondary | 2026-06-06 | Hugh Johnson / Octopus | 书目元数据 — Pocket Wine Book 2025（48 年连续年更） |
| T01-S017 | https://wineanorak.com/jamie-goode/ | surrogate_primary | 2026-06-06 | Jamie Goode | critic own publication — wineanorak about（PhD 植物学→科学派） |
| T01-S018 | https://www.amazon.com/Taste-Red-Science-Tasting-Wine/dp/0520292243 | secondary | 2026-06-06 | Jamie Goode (UC Press) | 书目元数据 — I Taste Red（品鉴=大脑建构，2016） |
| T01-S019 | https://josevouillamoz.com/ | surrogate_primary | 2026-06-06 | José Vouillamoz | critic/expert own site — 葡萄基因学家官网（Wine Grapes 共著） |
| T01-S020 | https://www.decanter.com/interviews/wine-to-five-jose-vouillamoz-grape-geneticist-author-and-lecturer-474443/ | secondary | 2026-06-06 | Decanter | trade media — Vouillamoz 访谈（DNA 谱系方法论） |
| T01-S021 | https://en.wikipedia.org/wiki/%C3%89mile_Peynaud | secondary | 2026-06-06 | — | Peynaud 生平 + malolactic 控制 + 「Peynaudization」批评（史实） |
| T01-S022 | https://www.worldoffinewine.com/news-features/emile-peynaud | secondary | 2026-06-06 | World of Fine Wine | trade media — Peynaud「酿酒学巨人」深度评价 |
| T01-S023 | https://en.wikipedia.org/wiki/Maynard_Amerine | secondary | 2026-06-06 | — | Amerine 生平（UC Davis 感官科学+20 分制+气候区）（史实） |
| T01-S024 | https://en.wikipedia.org/wiki/Albert_J._Winkler | secondary | 2026-06-06 | — | Winkler 生平（UC Davis 葡萄栽培奠基）（史实） |
| T01-S025 | https://en.wikipedia.org/wiki/Winkler_index | secondary | 2026-06-06 | — | Winkler index 五气候区（Region I-V）定义+气候变化重订（术语） |
| T01-S026 | https://en.wikipedia.org/wiki/Ann_C._Noble | secondary | 2026-06-06 | — | Ann Noble 生平 — Aroma Wheel 1984 + V&E 首位女教授（史实） |
| T01-S027 | https://www.winearomawheel.com/ | surrogate_primary | 2026-06-06 | Ann C. Noble (InnoVinum) | critic/originator own site — Wine Aroma Wheel 官方站（1984 一手） |
| T01-S028 | https://en.wikipedia.org/wiki/Karen_MacNeil | secondary | 2026-06-06 | — | Karen MacNeil 生平（Wine Bible 1M+ 册，唯一获全英语大奖美国人）（史实） |
| T01-S029 | https://winespeed.com/ | surrogate_primary | 2026-06-06 | Karen MacNeil | critic own publication — WineSpeed 周更 e-letter（50k+ 订阅） |
| T01-S030 | https://en.wikipedia.org/wiki/Kevin_Zraly | secondary | 2026-06-06 | — | Kevin Zraly 生平（Windows on the World Wine School 40 年）（史实） |
| T01-S031 | https://en.wikipedia.org/wiki/Wine_Folly | secondary | 2026-06-06 | — | Wine Folly 史（Puckette 2011 创，infographic 入门流量入口）（史实） |
| T01-S032 | https://iwsc.net/news/iwsc/wine-folly-co-founder-madeline-puckette-unveiled-as-iwsc-wine-communicator-of-the-year | secondary | 2026-06-06 | IWSC | trade body 新闻 — Puckette 获 IWSC Wine Communicator of the Year 2019 |
| T01-S033 | https://wineindustryadvisor.com/2026/05/14/wine-folly-co-founder-madeline-puckette-to-speak-at-vine-to-mind-symposium-at-uc-davis/ | secondary | 2026-06-06 | Wine Industry Advisor | trade media — Puckette 2026 UC Davis Vine to Mind 演讲（近 12 月动态） |
| T01-S034 | https://en.wikipedia.org/wiki/Rajat_Parr | secondary | 2026-06-06 | — | Rajat Parr 生平（侍酒师→酿酒师，IPOB 2011 创办）（史实） |
| T01-S035 | https://www.winespectator.com/articles/rajat-parrs-star-rises-in-santa-barbara-46582 | secondary | 2026-06-06 | Wine Spectator | trade media — Parr 在 Santa Barbara 越来越早采收求平衡 |
| T01-S036 | https://illdrinktothatpod.com/ | surrogate_primary | 2026-06-06 | Levi Dalton | critic own publication — I'll Drink to That 口述史 podcast（503+ 集） |
| T01-S037 | https://www.winefornormalpeople.com/ | surrogate_primary | 2026-06-06 | Elizabeth Schneider CSW | critic own publication — Wine for Normal People（去精英化，10M+ 收听） |
| T01-S038 | https://www.amazon.com/Wine-Normal-People-Guide-Snobbery/dp/1452171343 | secondary | 2026-06-06 | Elizabeth Schneider (Chronicle) | 书目元数据 — Wine for Normal People（2019, 反 snobbery 指南） |
| T01-S039 | https://winespecific.com/about/ | surrogate_primary | 2026-06-06 | Benjamin Lewin MW | critic own publication — Lewin on Wine 个人站（**verifier 误判 verified_primary，人工下调**） |
| T01-S040 | https://us.amazon.com/Wine-Myths-Reality-Benjamin-Lewin/dp/0983729263 | secondary | 2026-06-06 | Benjamin Lewin MW | 书目元数据 — Wine Myths & Reality（数据 myth-buster, terroir 章） |
| T01-S041 | https://www.rawwine.com/pages/isabelle-legeron | surrogate_primary | 2026-06-06 | Isabelle Legeron MW (RAW WINE) | critic own publication — Legeron 传记页（自然酒运动旗手） |
| T01-S042 | https://www.amazon.com/Natural-Wine-introduction-biodynamic-naturally/dp/1782498990 | secondary | 2026-06-06 | Isabelle Legeron MW | 书目元数据 — Natural Wine（自然酒派宣言） |
| T01-S043 | https://www.decanter.com/premium/nicolas-joly-decanter-hall-of-fame-2025-565729/ | secondary | 2026-06-06 | Decanter | trade media — Joly 入选 Decanter Hall of Fame 2025（近 12 月动态） |
| T01-S044 | https://coulee-de-serrant.com/en/nicolas-joly-speaks-godfather-of-biodynamic-wine/ | surrogate_primary | 2026-06-06 | Nicolas Joly (Coulée de Serrant) | producer own publication — Joly「true wine」生物动力宣言（争议一手） |
| T01-S045 | https://www.wineanorak.com/biodynamic5.htm | surrogate_primary | 2026-06-06 | Jamie Goode (wineanorak) | critic own publication — Goode 实访 Joly（科学派对生物动力的审视一手） |
| T01-S046 | https://www.timatkin.com/ | surrogate_primary | 2026-06-06 | Tim Atkin MW | critic own publication — 产区年度报告（南非/西/南美，百分制） |
| T01-S047 | https://specialprojects.news24.com/south-africa-2025-special-report-by-tim-atkin-mw/index.html | secondary | 2026-06-06 | News24 / Tim Atkin MW | trade media 托管 — Tim Atkin 2025 南非报告（300+ 页，近 12 月动态） |
| T01-S048 | https://drinksint.com/news/fullstory.php/aid/9710/Jancis_Robinson_MW_sells_website_to_U.S._media_company.html | secondary | 2026-06-06 | Drinks International | trade media — Jancis 2021 卖站给 Recurrent Ventures（所有权变更史实） |
| T01-S049 | https://global.oup.com/academic/product/the-oxford-companion-to-wine-9780198871316 | secondary | 2026-06-06 | OUP / Robinson+Harding+Thomas | 出版社页 — Oxford Companion 5th ed（2023），Harding 50% 编辑 |
| T01-S050 | https://www.amazon.com/Wine-Grapes-Complete-Varieties-Including/dp/0062206362 | secondary | 2026-06-06 | Robinson/Harding/Vouillamoz | 书目元数据 — Wine Grapes（1368 品种 DNA 圣经，2012） |

---

## 详条（按影响力与流派覆盖排序）

### 🍷 1. Jancis Robinson MW（OBE）— 评论独立性 + 20 分制散文派旗手

- **核心一句话（思维 DNA）**: 「评分是用筛子捞云」——评分是**酒与品鉴者之间互动**的产物、不是酒的固有属性；把复杂感官压成单一数字会损害葡萄酒文化，所以宁可用刻度粗、半分制的 20 分让分数「不假装精确」。 (evidence: [T01-S001, T01-S002], 一手)
- **头衔/角色**: 英国葡萄酒作家/评论家；**首位非酒商出身的 MW**（1984）；FT 葡萄酒专栏（1989 至今）；JancisRobinson.com 创办（2000）。多次被评全球最具影响力评论家。 (evidence: [T01-S003], surrogate_primary)
- **代表作品**: 《The Oxford Companion to Wine》（编，5th ed 2023）[T01-S049]；《The World Atlas of Wine》（与 Hugh Johnson）[T01-S015]；《Wine Grapes》（与 Harding/Vouillamoz）[T01-S050]；JancisRobinson.com Purple Pages（每日，57,000+ tasting notes）。
- **值得读/听/看 3 件**: ① 「How we score」+「How to score wine」——理解她为何抵制百分制 (evidence: [T01-S001, T01-S002])；② Oxford Companion 任意词条（行业事实层最高单一权威）；③ FT 每周专栏（部分免费窗口，看她的散文式评酒 register）。
- **争议立场/非主流观点**: 长年公开抵制 Parker 式百分制（认为不可跨评论家通约、把酒物化）；坦承「若职业生涯里从不被要求打分会快乐得多」，但仍打分只因读者需要 en primeur/横向品鉴的速记 shorthand——**这是「被迫打分的反对者」的拧巴立场**，非纯粹反分数姿态。 (evidence: [T01-S001, T01-S002], 一手)
- **近 12 个月动态**: 网站所有权链已多次易手——2021 卖给美国 Recurrent Ventures [T01-S048]，2024 转至原买家之一 Lance Johnson，**现由 Eisenhower Flagstaff 持有**，计划增加加州覆盖与技术升级；Jancis 本人仍主笔、团队化运营降低个人依赖。 (evidence: [T01-S048] + search 二手，**所有权细节为 trade media 二手，公司名以最新检索为准**)
- **所属流派**: ④ **Jancis 20 分制散文派**（奠基级当前代表）；同时是 ② 旧世界风土派的事实层底座（Oxford/Atlas）。

### 🍷 2. Robert Parker — 百分制点评派奠基人（争议靶心）

- **核心一句话（思维 DNA）**: 把 50-100 分制推成全球消费者通用语言——主张分数给小众酒庄出头机会、打破旧世界种姓；偏爱**浓郁、果味驱动、强萃取**的风格，这一偏好经市场放大成「国际风格」。 (evidence: [T01-S007, T01-S008], 一手自辩 + 二手批评)
- **头衔/角色**: 退休美国葡萄酒评论家；《The Wine Advocate》创办人；**全球最广为人知、影响力最大的评论家**（其评分系统性影响美国乃至全球买酒与酿造）。2019 年 71 岁正式从 Wine Advocate 退休。 (evidence: [T01-S007, T01-S011], 二手)
- **代表作品**: 《The Wine Advocate》newsletter（百分制起家）；early Bordeaux/Rhône 评分（尤以 1982 波尔多年份预言奠定权威）。
- **值得读/听/看 3 件**: ① Wikipedia「Parkerization」段——理解「同质化」批评的来龙去脉 (evidence: [T01-S007])；② Parker 阵营自辩长文「The Big Parkerization Lie」——听他这边怎么反驳 (evidence: [T01-S008])；③ 纪录片《Mondovino》（Jonathan Nossiter, 2004）——把 Parker + 飞行酿酒师 Michel Rolland 当全球化威胁 terroir 的靶子（**该片即一份「反 Parker 论辩状」，非中立**）。 (evidence: search 二手)
- **争议立场/非主流观点（反例不软化）**: 「Parkerization / 国际风格」批评指其口味偏好**实质性改变了全球酿造**——大果味、软单宁（micro-oxygenation）、高酒精、重橡木的同质化；批评者（含自然酒派、风土派）视其为元凶。Parker 本人坚决否认同质化、反以「给无名酒庄机会」自豪。**两边并存，本笔记不替任一方洗白**：同质化效应有大量从业者实证体感，Parker 的自辩也是一手立场。 (evidence: [T01-S007, T01-S009, T01-S010, T01-S008])
- **近 12 个月动态**: 已退休多年，无新评分活动；其遗产仍是「百分制 vs 风土表达」张力的历史原点，PUNCH（2024-2025 重估稿）等持续重新评价其影响。 (evidence: [T01-S009], 二手)
- **所属流派**: ④ **Parker 百分制点评派奠基人**；同时是 ⑤ 浓郁现代派酿造审美的市场放大器（与经典平衡派对立）。

### 🍷 3. Antonio Galloni — 现代「媒体×技术」评论派 / Parker 体系的继承+转向

- **核心一句话（思维 DNA）**: 评论不该是孤立打分，而是「媒体平台」——产区垂直报告 + 酿酒师视频 + 交互地图 + 老酒回溯一体化；继承百分制但把它嵌进更厚的语境。 (evidence: [T01-S012, T01-S013], 一手平台 + 二手)
- **头衔/角色**: 美国评论家；Vinous 创办人兼 CEO，亲评 Bordeaux/California/Italy/Champagne。2006-2013 在 Parker 的 Wine Advocate 任品鉴成员，2013 自立门户创 Vinous。 (evidence: [T01-S012], 二手)
- **代表作品**: Vinous（每日流，产区年度报告 + Cellar Favorites + 酿酒师视频 + 交互产区地图）[T01-S013]；Vinous Top 100 Wines（年度榜，2025 续出）。
- **值得读/听/看 3 件**: ① Vinous 任一产区年度报告（看现代评论站形态）；② Vinous 交互产区地图 + 酿酒师视频（区别于纯文字评论家）；③ Jamie Goode 对「Vinous Preview」的批评文——理解 trade vs consumer 之争 (evidence: [T01-S014])。
- **争议立场/非主流观点（反例不软化）**: **Vinous Preview** 服务让订户提前 48 小时拿到分数 + 提交日历外送评酒，被 Jamie Goode 等批为「把 Vinous 摆到 trade（酒商）而非 consumer（消费者）一边」——即评论独立性向商业倾斜的质疑；这是当代评论家商业模式的核心争议，**如实记录而非软化**。 (evidence: [T01-S014], 一手批评)
- **近 12 个月动态**: 2025 发布 Vinous Top 100 Wines；持续每日产区评论流，机构化/团队化（Neal Martin、Josh Raynolds 等）。 (evidence: [T01-S013] + search 二手)
- **所属流派**: ④ **百分制点评派当前代表**（Parker 体系的继承者，但平台化转向）。

### 🍷 4. Hugh Johnson — 旧世界风土/地理派奠基写手

- **核心一句话（思维 DNA）**: 葡萄酒**首先是地理问题**——把世界产区第一次「认真地画成地图」，让风土从玄学变成可在地图上指认的具体空间。 (evidence: [T01-S015], 二手)
- **头衔/角色**: 公认「在世最重要的葡萄酒写作者」；27 岁即以《Wine》（1966）成名。 (evidence: [T01-S015], 二手)
- **代表作品**: 《The World Atlas of Wine》（1971 初版，被 INAO 主任称「葡萄酒文献的重大事件」，译 14 语、销 400 万+ 册，现与 Jancis 合编）[T01-S015]；《Hugh Johnson's Pocket Wine Book》（1977 起，**48 年连续年更**，全球最畅销年度酒指南，2025 版含 Pinot Noir 专辑）[T01-S016]。
- **值得读/听/看 3 件**: ① World Atlas of Wine（建立全球产区空间地图）；② Pocket Wine Book 最新版（年度产区快照 + 气候变化对 Pinot 影响）[T01-S016]；③ 自传《A Life Uncorked》（理解 20 世纪葡萄酒写作如何成形）。
- **争议立场/非主流观点**: 相对低争议——属「叙事-地理-愉悦」传统，对评分体系刻意保持距离（Pocket Book 用 1-4 星而非百分制，与 Parker 量化派分道）；其「风土即地图」框架本身是对「品种/技术派」无地理根的隐性反对。 (evidence: [T01-S015, T01-S016])
- **近 12 个月动态**: Pocket Wine Book 维持年更（2025 版）；本人已高龄，近年新书多由 Margaret Rand 等接续编纂[T01-S016]。 (evidence: [T01-S016], 二手)
- **所属流派**: ② **旧世界风土派奠基写手**（地理优先）；与 Jancis 共同构成行业事实层双核。

### 🍷 5. Julia Harding MW — Oxford Companion 现任主编 / 编纂权威

- **核心一句话（思维 DNA）**: 葡萄酒知识可被严谨百科化，但需要「编辑之手」持续重写与校准——她是把名家署名背后的事实层做扎实的人。 (evidence: [T01-S004, T01-S049], surrogate_primary + 二手)
- **头衔/角色**: MW（2004，获 Robert Mondavi 最佳理论卷奖 + Tim Derouet 纪念奖）；JancisRobinson.com 资深编辑（2005 至今）。 (evidence: [T01-S004], certification body)
- **代表作品**: 《The Oxford Companion to Wine》5th ed（**负责 50% 编辑，与 Jancis 并列 lead editor**）[T01-S049]；《World Atlas of Wine》8th ed 制图编辑；《Wine Grapes》共著[T01-S050]。
- **值得读/听/看 3 件**: ① Oxford Companion 5th ed（看她主导的栽培/酿造/品种词条）；② JancisRobinson.com 她的产区 tasting notes（细分产区覆盖）；③ IMW 对她的简介（理解 MW 论文卷的学术标准）[T01-S004]。
- **争议立场/非主流观点**: 低争议、属「严谨编纂」而非「立场宣示」型 figure；价值在事实层把关而非观点输出——但正因如此，她代表「百科可信度 > 个人评分秀」的取向，与评分秀文化形成对照。 (evidence: [T01-S004, T01-S049])
- **近 12 个月动态**: 2025 获 **67 Pall Mall Global Wine Communicator（长文写作）奖**；持续在 JancisRobinson.com 主笔。 (evidence: search 二手；奖项为 trade 二手)
- **所属流派**: ② 旧世界风土派事实层（Oxford/Atlas/Wine Grapes 编纂核心）；跨 ④ Jancis 20 分制阵营团队。

### 🍷 6. José Vouillamoz — 品种 DNA 谱系派（葡萄基因学权威）

- **核心一句话（思维 DNA）**: 品种身份不是传说而是**基因事实**——用 DNA 亲子鉴定终结同义词混乱与起源神话，让「这是什么葡萄」可被科学厘清。 (evidence: [T01-S019, T01-S020], 一手 + 二手)
- **头衔/角色**: 瑞士葡萄基因学家，**全球品种起源/亲缘 DNA 鉴定的领军权威**；师从 UC Davis 的 Carole Meredith 教授。 (evidence: [T01-S019], surrogate_primary)
- **代表作品**: 《Wine Grapes》（与 Robinson/Harding，2012，1368 品种 DNA 家谱）[T01-S050]；《Swiss Grape Varieties: Origins and History》（厘清 300 个瑞士品种、94 个本土品种谱系）[T01-S019]。
- **值得读/听/看 3 件**: ① Wine Grapes（品种学唯一权威参考）；② 他官网/Decanter「Wine to 5」访谈——理解古典 ampelography（形态学）与 DNA 如何互补 (evidence: [T01-S020])；③ OUPblog「Wine and DNA profiling」——看 DNA 如何推翻误称。
- **争议立场/非主流观点**: 反「浪漫起源叙事」——很多产区引以为豪的「古老本土品种起源故事」被 DNA 证伪（如某些品种实为外来或杂交）；这对依赖「身世营销」的产区是 inconvenient truth。属数据/科学派对传说的祛魅。 (evidence: [T01-S019, T01-S020])
- **近 12 个月动态**: 持续做品种 DNA 咨询与讲座（Académie Internationale du Vin 成员）；瑞士本土品种研究为其近年重心。 (evidence: [T01-S019], 一手站点)
- **所属流派**: ③ 数据/科学派（品种维度）；与 ② 旧世界风土派交叉（DNA 解释品种-产地迁徙），但祛魅其神话层。

### 🍷 7. Émile Peynaud — 现代酿酒学之父 / 经典-现代主义酿造派奠基

- **核心一句话（思维 DNA）**: 酿酒应从经验/迷信变成**可控科学**——把曾被当作「病」的 malolactic 苹乳发酵重新定义为应主动鼓励与控制的过程，奠定「干净、健康、技术可控」的现代范式。 (evidence: [T01-S021, T01-S022], 二手 + 史实)
- **头衔/角色**: 法国酿酒学家/研究者（1912-2004，波尔多大学）；公认「现代酿酒学之父」，20 世纪下半叶革新酿酒。 (evidence: [T01-S021], 二手)
- **代表作品**: 《Knowing and Making Wine》（奠基教科书）；《The Taste of Wine》（品鉴可训练/系统化的配套）。
- **值得读/听/看 3 件**: ① Knowing and Making Wine（现代酿酒范式源头）；② World of Fine Wine「Giant of Enology」纪念长文 (evidence: [T01-S022])；③ Wine for Normal People「Wine Legends: Émile Peynaud」播客集（入门级解码他的影响，search 命中）。
- **争议立场/非主流观点（反例不软化）**: 1950-60 年代被怀疑者讥为「**Peynaudization** of Bordeaux」——指其方法让酒趋同；当代自然酒派进一步把他当「现代主义干预 = 全世界酒喝起来一样」的反对靶子。**如实记录**：当年「Peynaudization」批评因其酒质普遍更优而一度平息（[T01-S021]），但「现代清洁主义同质化」的更深层批评在自然酒运动中重新点燃，未被平息。 (evidence: [T01-S021], 二手史实)
- **近 12 个月动态**: 已故（2004）；其范式仍是「干预 vs 放手」张力的历史原点，2025 仍被播客/长文重访。 (evidence: [T01-S022])
- **所属流派**: ⑤ **经典/现代主义酿造派奠基人**（清洁、科学、控制）；是 ③ 学院科学派落地酿造的源头之一，也是自然酒派（③ 自然/低干预）的头号对立面。

### 🍷 8. Maynard Amerine & Albert Winkler — UC Davis 学院科学派双奠基

- **核心一句话（思维 DNA）**: 葡萄酒是**可量化的硬科学**——用生长积温（degree-days）把气候分成 Region I-V 五区、用 20 分制把品鉴标准化，让「哪里该种什么、酒好不好」可测量、可复现。 (evidence: [T01-S023, T01-S024, T01-S025], 二手 + 史实)
- **头衔/角色**: UC Davis V&E 教授。**Winkler** = 葡萄栽培奠基（系主任级）；**Amerine** = 感官科学 + 酿造 + 气候区。二人 1934-1942 近十年研究，数据记在数千张索引卡上。 (evidence: [T01-S023, T01-S024, T01-S025], 二手)
- **代表作品**: **Winkler index / 气候区分类**（Region I-V，growing degree-days）[T01-S025]；20 分制品鉴评分（UC Davis scale，1959，教育界校准标准）；合著《General Viticulture》。
- **值得读/听/看 3 件**: ① Winkler index 词条（理解气候区如何指导种植决策）[T01-S025]；② UC Davis V&E 课程目录（看学院派把酒拆成生物/化学/微生物，见 Track 04 T04-S001/S002）；③ Amerine 的 20 分制 vs Parker 百分制对照（评分谱系两极）。
- **争议立场/非主流观点**: 学院科学派对「terroir 玄学」与「评分秀」都保持距离——主张可测量、可复现；但其 20 分制 + 气候区被批「过度还原论」，把不可量化的 tacit 风味也试图框进网格。**时效 caveat**：Winkler index 因气候变化已被 UC Davis 团队（Winiarski 捐助）重新修订，原五区划分对当代凉/暖区边界已不完全适用。 (evidence: [T01-S025], 二手；气候变化修订为近年事实)
- **近 12 个月动态**: 二人均已故；**Winkler index 的气候变化重订是活跃议题**（UC Davis 图书馆用其档案更新这项 seminal 研究）。 (evidence: [T01-S025], 二手)
- **所属流派**: ③ **新世界/学院科学派奠基人**（UC Davis）；④ 评分谱系中 20 分制学术校准制的源头（早于 Jancis）。

### 🍷 9. Ann C. Noble — Aroma Wheel 发明者 / tacit→codifiable 的桥

- **核心一句话（思维 DNA）**: 人人都闻得到，只是**缺词汇**——把模糊的「earthy/泥土味」按相似度分组成轮盘，给 tacit 嗅觉感知一套标准化、可沟通的词表。 (evidence: [T01-S026, T01-S027], 二手 + 一手站)
- **头衔/角色**: 感官化学家，UC Davis V&E 退休教授；**1974 年该系首位女性教职**（2002 退休，2003 名誉教授）。 (evidence: [T01-S026], 二手)
- **代表作品**: **Wine Aroma Wheel**（1984，winearomawheel.com 官方站）[T01-S027]——从中心宽香气族（果/花/香料）到外圈具体香（樱桃/柠檬/胡椒）。
- **值得读/听/看 3 件**: ① Aroma Wheel 本体（按它练 1 次盲品立刻体会「词汇先于感知」）[T01-S027]；② Wine Enthusiast「How Ann Noble Revolutionized the Industry」(evidence: search 二手)；③ 她强调「教学生评酒时发现他们闻得到但说不出」的访谈（理解工具的起源动机，[T01-S026]）。
- **争议立场/非主流观点**: 反「神秘化品鉴」——主张品鉴词汇应**去精英化、可教**，任何人都能学会说出闻到什么；这与「品鉴是天赋/神秘直觉」的精英叙事对立。低争议但立场鲜明。 (evidence: [T01-S026, T01-S027])
- **近 12 个月动态**: 已退休多年；Aroma Wheel 仍是 WSET/CMS/UC Davis 的基础教具（经久不衰，decay 极低）。 (evidence: [T01-S027])
- **所属流派**: ③ 学院科学派（感官维度，UC Davis）；是「codifiable 理论 ⇄ tacit 校准」桥梁的工具化身（→ Track 02 tools 核心）。

### 🍷 10. Benjamin Lewin MW — 数据怀疑派 / myth-buster

- **核心一句话（思维 DNA）**: 很多「人尽皆知」的葡萄酒常识缺实证——用**数据与图表**（罕见于葡萄酒书写）去检验 terroir、国际风格、分级的浪漫叙事，问「terroir 真的重要吗？」 (evidence: [T01-S039, T01-S040], 一手 + 二手)
- **头衔/角色**: MW；**科学期刊《Cell》创刊编辑**（生物学背景）→ 转葡萄酒。 (evidence: [T01-S039, T01-S040], surrogate_primary + 二手)
- **代表作品**: 《Wine Myths and Reality》（含「The Mystique of Terroir」章，问 terroir/国际风格/全球变暖三大问）[T01-S040]；《What Price Bordeaux?》（同法剖析 en primeur 与酒评家影响力）；Lewin on Wine（winespecific.com 个人站）[T01-S039]。
- **值得读/听/看 3 件**: ① Wine Myths and Reality terroir 章（看「received wisdom」如何被数据检视）[T01-S040]；② What Price Bordeaux?（理解评论家如何影响价格）；③ winespecific.com 博客（持续的数据派评论）[T01-S039]。
- **争议立场/非主流观点**: 直接挑战「terroir 至上」浪漫叙事与「贵=好」——主张许多 terroir 主张缺可证伪证据、新旧世界差异可被数据检视；这让风土派与 1855 列级拥趸不适。属健康怀疑论，但有时被批「数据也无法完全解释品鉴的 tacit 层」。 (evidence: [T01-S040, T01-S039])
- **近 12 个月动态**: 持续在 Lewin on Wine 发数据派分析；产区深著（Bordeaux/Burgundy 等）陆续更新。 (evidence: [T01-S039], 一手站)
- **所属流派**: ③ **数据怀疑派**（与 Jamie Goode 同阵营）；横跨 ② vs ① 之争（用数据质疑 terroir 与认证体系的浪漫层）。

### 🍷 11. Jamie Goode — 科学派桥梁 / 品鉴是大脑建构

- **核心一句话（思维 DNA）**: 「**分数不是酒的属性，而是酒与品鉴者互动的属性**」——品鉴是大脑的建构（感官+心理+哲学+风味化学），不是对客观真值的测量；葡萄酒科学该公开可读，不是酿酒师黑箱。 (evidence: [T01-S017, T01-S018], 一手 + 二手；此句被 Jancis 引用见 T01-S002)
- **头衔/角色**: 伦敦葡萄酒作家/讲师/评审；**植物学 PhD**、前科学编辑；wineanorak.com（最早一批葡萄酒博客之一）；International Wine Challenge 联合主席。2005-2025 任 Sunday Express 专栏。 (evidence: [T01-S017], surrogate_primary)
- **代表作品**: 《The Science of Wine》《I Taste Red》（品鉴的感官科学，2016）[T01-S018]、《Authentic Wine》《Flawless》《Regenerative Viticulture》《The New Viticulture》（共 6 本）；wineanorak.com。
- **值得读/听/看 3 件**: ① I Taste Red（理解「品鉴=知觉建构」）[T01-S018]；② wineanorak.com「the science of wine」长文体系 (evidence: [T01-S017])；③ 他对 Vinous Preview 的批评 [T01-S014] + 对 Nicolas Joly 的实访 [T01-S045]（看科学派如何同时质疑评论商业化与生物动力玄学）。
- **争议立场/非主流观点（反例不软化）**: **同时怀疑两边**——既对自然酒「无定义/缺陷酒被美化」存疑，又认真对待「authentic wine」值得科学研究；对生物动力法（Joly）持「实证审视、不照单全收」态度；对 Vinous Preview 商业化公开批评。属「科学怀疑论」中间派，因此两边都可能不满。 (evidence: [T01-S017, T01-S014, T01-S045])
- **近 12 个月动态**: 2025 结束 20 年 Sunday Express 专栏[T01-S017]；近年转向 Regenerative Viticulture（再生农业）主题写作与讲座。 (evidence: [T01-S017], 一手站)
- **所属流派**: ③ **数据/科学派当前代表**（与 Lewin 同阵营）；在 ③ 自然酒之争中是「科学审视」中间立场。

### 🍷 12. Isabelle Legeron MW — 自然酒/低干预派旗手

- **核心一句话（思维 DNA）**: 葡萄酒应「如自然本意」——有机/生物动力种植为最低门槛、酒窖「不加不减」（原生酵母、无添加 SO₂、不下胶、不过滤、不加酶），是对 Peynaud 式现代清洁主义的正面对立。 (evidence: [T01-S041, T01-S042], 一手 + 二手)
- **头衔/角色**: **法国首位女性 MW**；RAW WINE 创办人（2012，全球最大低干预/有机/生物动力/自然酒生产者社区）；被 Drinks Business 列「葡萄酒界最有权势 50 女性」之一。 (evidence: [T01-S005, T01-S041], certification body + surrogate_primary)
- **代表作品**: 《Natural Wine: An introduction to organic and biodynamic wines made naturally》（自然酒派宣言/定义）[T01-S042]；RAW WINE 全球巡回展（NY/Paris/Tokyo 等，见 Track 05 T05-S023）。
- **值得读/听/看 3 件**: ① Natural Wine（理解自然酒派的辩护与自定义）[T01-S042]；② RAW WINE 展（线下感受「另一套酿造价值观」）；③ Wine Blast 播客「On Natural Wine」集（听她答辩争议，search 命中）。
- **争议立场/非主流观点（反例不软化）**: 自然酒**无官方定义**，她给出自己的严格定义——但这恰是争议核心。批评者（含书评）指其叙事把「每个自然酿酒师都无可指摘、体系被一个'要害死他们的反派'人格化」，**需打个折扣读**；科学派（Goode/Lewin）质疑「缺陷酒被美化、无定义难证伪」。**如实记录该书被批的护教倾向，不软化。** (evidence: [T01-S042] 书评二手, [T01-S041] 一手)
- **近 12 个月动态**: RAW WINE 持续全球多城扩张（2026 Paris/Verona/Tokyo 等，见 Track 05）；自然酒持续主流化。 (evidence: [T01-S041] + Track 05 T05-S023)
- **所属流派**: ③ **自然酒/低干预派当前旗手**（当代文本与运动领袖）；Peynaud（⑤ 现代主义）的头号对立面。

### 🍷 13. Nicolas Joly — 生物动力法教父（自然酒派的精神源头之一）

- **核心一句话（思维 DNA）**: 「**真酒（true wine）不一定好喝或好看，但有打动你的内在**」——生物动力农法是唯一能「捕捉一地的生命力与原创性、装进瓶子」的方式；评分/技术化是「冷聪明（cold cleverness）」。 (evidence: [T01-S044, T01-S043], 一手 + 二手)
- **头衔/角色**: 卢瓦尔 Savennières 的 Coulée de Serrant 庄主；**「生物动力教父」**；前纽约/伦敦投资银行家，回乡接手家族酒庄、1984 获完整生物动力认证（全球最早之一）。 (evidence: [T01-S043, T01-S044], 二手 + 一手)
- **代表作品**: Coulée de Serrant（12 世纪 Cistercian 修士所植 Chenin Blanc 单一园）；著《Wine from Sky to Earth》《Biodynamic Wine Demystified》；创办 Renaissance des Appellations（生物动力生产者联盟）。
- **值得读/听/看 3 件**: ① 他的「true wine vs cold cleverness」演讲/文章（理解生物动力的哲学，[T01-S044]）；② Jamie Goode 对他的实访——看科学派如何审视他（一手对话，[T01-S045]）；③ Decanter Hall of Fame 2025 报道（行业如何盖棺定位他，[T01-S043]）。
- **争议立场/非主流观点（反例不软化）**: 主张月相/牛角配制剂等 Steiner 学说，1980 年代被广泛斥为「怪人」（其父母八年间接到「他在毁葡萄园」的电话，[T01-S043]）；科学派至今认为生物动力的「能量/宇宙力」缺实证、效果难与「单纯认真做有机」区分。**如实记录**：生物动力的农艺效果（健康土壤）有支持，但其玄学解释框架未被科学接受——两点不混为一谈。 (evidence: [T01-S043, T01-S044, T01-S045])
- **近 12 个月动态**: **2025 入选 Decanter Hall of Fame**——标志生物动力从「异端」到被主流追认的转折。 (evidence: [T01-S043], 二手)
- **所属流派**: ③ **自然酒/低干预派的精神源头**（生物动力分支，落地 Steiner 学说）；⑤ 经典平衡 vs 浓郁现代 之外的「第三条路」（反技术主义）。

### 🍷 14. Rajat Parr — In Pursuit of Balance / 经典平衡派当前代表（侍酒师→酿酒师）

- **核心一句话（思维 DNA）**: 反「fruit bomb」——加州酒该走**优雅、精细、平衡**而非高熟高酒精；用「每年看能多早采收」来追求更低酒精、更鲜酸、更纯净的风味。 (evidence: [T01-S034, T01-S035], 二手)
- **头衔/角色**: 印裔美国侍酒师转酿酒师；曾掌 Michael Mina 餐饮集团酒水（师从传奇侍酒师 Larry Stone）；Sandhi、Domaine de la Côte（Santa Barbara）联合创办人；2011 与 Jasmine Hirsch 共创 **In Pursuit of Balance（IPOB）**。 (evidence: [T01-S034, T01-S035], 二手)
- **代表作品**: 《Secrets of the Sommeliers》（与 Jordan Mackay，2011 James Beard Award，侍酒师怎么想怎么喝，见 Track 04 T04-S025）；《The Sommelier's Atlas of Taste》；IPOB 运动。
- **值得读/听/看 3 件**: ① Secrets of the Sommeliers（tacit 服务/选酒层入口，Track 04）；② IPOB 的理念资料（看「平衡 vs 成熟度」如何重塑加州 Pinot 对话，[T01-S034]）；③ The Sommelier's Atlas of Taste（按风味/结构而非产区组织的品鉴地图）。
- **争议立场/非主流观点（反例不软化）**: IPOB「平衡」主张被批评为**另一种风格教条**——反对者认为它把「低酒精=更高级」道德化、贬低了正当的暖气候浓郁风格（即「反 Parker」也可能矫枉过正）。IPOB 已于约 2016 解散，部分因「使命已达成」、部分因「balance 一词被过度政治化」。**如实记录该运动的争议与落幕，不美化。** (evidence: [T01-S034, T01-S035] + search 二手)
- **近 12 个月动态**: 专注 Sandhi/Domaine de la Côte 与俄勒冈项目的 site-specific、低干预酿造；持续被引为「侍酒师转酿酒师」的范式。 (evidence: [T01-S034], 二手)
- **所属流派**: ⑤ **经典平衡派当前代表**（与 Parker 浓郁现代派对立）；① CMS 服务派出身（侍酒师背景）；与 ③ 低干预派审美重叠。

### 🍷 15. Levi Dalton — 口述史长访谈派 / 行业 tacit 知识的档案者

- **核心一句话（思维 DNA）**: 这一行的真知靠**口述传递**——把全球最重要的酿酒师/酒商/侍酒师/作家请进小公寓，1-2 小时让他们坦诚自述，做出书里没有的「师承如何流动」的一手档案。 (evidence: [T01-S036], surrogate_primary)
- **头衔/角色**: 前纽约顶级餐厅侍酒师（Restaurant Daniel/Masa/Alto）；**I'll Drink to That! 主持**（全球最多人听的葡萄酒 podcast）。 (evidence: [T01-S036], 一手)
- **代表作品**: 《I'll Drink to That!》podcast（503+ 集，口述史档案库，见 Track 05 T05-S002）[T01-S036]。
- **值得读/听/看 3 件**: ① 按你关心的产区/人物点播 IDTT 单集（单点信息密度最高的一手长访谈）；② 与各国传奇酿酒师/侍酒师的集（很多嘉宾只在这里长谈）；③ IDTT 作为「理解这一行怎么运转」的入口（非追新，是长期沉淀）。
- **争议立场/非主流观点**: 反「剪辑化/碎片化」内容——坚持近乎无剪辑的长独白形式，对抗注意力经济；不打分、不评级，纯做人物与师承。属对「评分秀」与「短内容」的双重反动。 (evidence: [T01-S036])
- **近 12 个月动态**: 个人制作、频率本低（深度优先于频率），2025 仍活跃；503+ 集存量本身即资产（停更也不损价值，见 Track 05）。 (evidence: [T01-S036] + Track 05 T05-S002)
- **所属流派**: ① CMS 服务派出身（侍酒师背景）；**跨流派的「档案者」**——其访谈对象覆盖全部 5 组流派，是流派谱系的一手口述来源。

### 🍷 16. Karen MacNeil — 美国去精英化教育派（叙事型百科）

- **核心一句话（思维 DNA）**: 把专家知识写成**「读得下去」的叙事**——让葡萄酒成为可分享的文化与愉悦，而非势利俱乐部的入场券。 (evidence: [T01-S028, T01-S029], 二手 + 一手)
- **头衔/角色**: 美国作家/演讲者/顾问；**唯一囊括所有英语世界主要葡萄酒大奖的美国人**；TIME 称其「美国葡萄酒传教士」。 (evidence: [T01-S028], 二手)
- **代表作品**: 《The Wine Bible》（销 100 万+ 册，3rd ed 2022，美国侍酒入门最常读的叙事型大部头，Track 04 列必读）[T01-S028]；WineSpeed（周更 e-letter，50,000+ 订阅）[T01-S029]。
- **值得读/听/看 3 件**: ① The Wine Bible（叙事型入门百科）；② WineSpeed 周更（每周五的速读 wine intel，[T01-S029]）；③ 她的 Substack「Wine Bible(ing)」（看第 4 版研究幕后，search 命中）。
- **争议立场/非主流观点**: 反「葡萄酒势利」、主张大众沟通——这本身在精英评论圈算「过于亲民」的取向（被某些资深者视为入门脚手架而非专家终点）。2024 发起「Come Over October」运动，针对**新禁酒主义（neo-prohibition）/健康话语对葡萄酒的打压**做正面辩护——这是当下争议十足的立场（公共卫生界正收紧饮酒建议）。 (evidence: [T01-S028, T01-S029])
- **近 12 个月动态**: 「Come Over October」+ 姊妹运动「Share & Pair Sundays」2025 触达 20 亿 UVM（**该数字为运动方自报，平台触达指标，非独立审计 → caveat**）；正研究下一版 Wine Bible + 一本个人书。 (evidence: [T01-S028], 二手；触达数为自报)
- **所属流派**: ① 教育普及派（美国侧，与 WSET 知识体系互补的叙事路线）；价值观上与去精英化阵营（Schneider/Puckette）同侧。

### 🍷 17. Madeline Puckette（Wine Folly）— 视觉化入门派 / 最大流量入口

- **核心一句话（思维 DNA）**: 把复杂葡萄酒科学**翻译成清晰、美、可及的 infographic**——服务于「想懂酒但不知从哪开始」的人，是当代入门最大流量入口。 (evidence: [T01-S031, T01-S032], 二手)
- **头衔/角色**: Wine Folly 联合创办人（2011，与开发者 Justin Hammack）；CalArts 平面设计背景（前电子音乐制作人/设计师）；**IWSC 2019 年度葡萄酒传播者**、James Beard 获奖作者。 (evidence: [T01-S031, T01-S032], 二手)
- **代表作品**: winefolly.com（infographic + 课程，Track 04 列入门必读）；《Wine Folly: The Essential Guide to Wine》（2015，NYT 畅销）；《Wine Folly: Magnum Edition》（2018）[T01-S031]。
- **值得读/听/看 3 件**: ① Wine Folly 经典 infographic（如「How to Choose Wine」、品种地图）；② Magnum Edition（视觉化入门百科）；③ 她在 2026 UC Davis Vine to Mind Symposium 的演讲（看入门传播者进入学院语境，[T01-S033]）。
- **争议立场/非主流观点**: 「视觉化/简化」路线被部分资深者批为「过度简化、牺牲细微差别」——但她坚持可及性 > 完备性，认为入门门槛才是行业增长瓶颈。属去精英化阵营对「专家话语壁垒」的正面挑战。 (evidence: [T01-S031, T01-S032])
- **近 12 个月动态**: **2026-05 受邀在 UC Davis「Vine to Mind」研讨会演讲**——入门传播者与学院科学派的罕见交汇。 (evidence: [T01-S033], 二手)
- **所属流派**: ① 教育普及派（视觉化入门，与 Schneider 去精英化、MacNeil 叙事化同阵营）；与 WSET 系统知识派形成「图解 vs 课程」入门两路。

### 🍷 18. Elizabeth Schneider（Wine for Normal People）+ Tim Atkin MW（合条：去精英化播客 / 产区年报标杆）

- **Elizabeth Schneider** — **核心一句话**：把葡萄酒从「snobbery（势利）」里解放出来，用普通人能懂的话讲清产区/品种/酿造。**头衔**：Certified Sommelier + CSW + MBA；Wine for Normal People 创办（2011，收听 10M+）。**代表作**：同名 podcast（Track 05 T05-S003 三大支柱之一）[T01-S037] + 书《Wine for Normal People: A Guide for Real People Who Like Wine, but Not the Snobbery》（2019）[T01-S038]。**争议立场**：明确反「装腔作势的精英俱乐部」文化——对评分秀与术语壁垒持批判，主张系统但去精英的有声教材。**所属流派**：① 教育普及/去精英化派（与 MacNeil/Puckette 同阵营，podcast 形态）。 (evidence: [T01-S037, T01-S038])
- **Tim Atkin MW** — **核心一句话**：用**单一产区「年度国别报告」**做高密度一手——逐年百分制深评南非/西班牙/南美，建立这些产区的年份与酒庄分级权威。**头衔**：英国作家/记者/MW；南非葡萄酒「最重要评论者」。**代表作**：timatkin.com 年度报告[T01-S046]；2025 第 13 份《South Africa Special Report》（300+ 页）[T01-S047]。**争议立场（反例不软化）**：用百分制（与 Jancis 20 分制对立阵营），但其报告把「南非分级」做成事实上的私人列级体系——**有人质疑单一评论家给整个产区分级的权力集中**。其 2024 报告里有「南非第 6 支 100 分酒、217 支 95+ 分」——**这些是 Atkin 个人主观刻度 + 单一评论家口径，非客观/跨评论家可通约，引用须挂此 caveat**。**所属流派**：④ 百分制点评派当前代表（产区报告子类）；② 关注旧世界外的「新兴产区」（南非/南美），介于风土派与新世界派之间。 (evidence: [T01-S046, T01-S047])

---

## 智识谱系（5 组流派分裂：奠基人 → 当前代表 → 核心分歧）

> 对应 prompt 的 5 组学派分裂。每组标注一手 vs 二手依据。流派间有交叉（同一人可跨多组），交叉处已注明。

### 谱系 ① WSET 知识体系派 vs CMS 服务盲品派

- **WSET 知识派** — **奠基/机构**：Wine & Spirit Education Trust（英，L1-L4 Diploma + SAT 系统化品鉴）。**当前代表（人）**：Matthew Gaughan（WSET 教育播客，Track 05）、各 Diploma 讲师生态；**Madeline Puckette / Elizabeth Schneider / Karen MacNeil** 在「知识普及」侧与之同向（图解/播客/叙事三种入门形态）。**取向**：知识广度 + 可写出的书面品鉴结论（SAT 网格），不考服务。 (evidence: Track 06 T06-S007；本 track T01-S037, T01-S031, T01-S029)
- **CMS 服务盲品派** — **奠基/机构**：Court of Master Sommeliers（服务 + 演绎法盲品 + 理论三合一，MS = 侍酒师金标）。**当前代表（人）**：**Levi Dalton（侍酒师出身，口述史档案）、Rajat Parr（侍酒师→酿酒师）**；GuildSomm 生态（Christopher Tanghe MS / Geoff Kruth MS，Track 05）。**取向**：餐厅一线服务手艺 + 现场演绎盲品。 (evidence: Track 06 T06-S011, T06-S012；本 track T01-S036, T01-S034)
- **核心分歧**：「专业 = 知识广度（WSET 笔试）」vs「专业 = 一线服务手艺 + 现场演绎（CMS）」。**盲品认识论之争**（硬件层）：WSET-SAT（描述+评质，不必猜中）⇄ CMS deductive grid（逻辑演绎到品种/产地/年份）。**反例不软化**：CMS-Americas 2018 曝考试舞弊丑闻（盲品试题泄露、撤销当年 Advanced 头衔），暴露「服务盲品派」的认证可信度脆弱——如实记录（→ Track 03 / Phase 2.8）。 (evidence: Track 06 T06-S007/S012；Track 04 注 CMS 丑闻)

### 谱系 ② 旧世界风土派 vs 新世界品种/技术派

- **旧世界风土派** — **奠基写手**：**Hugh Johnson《World Atlas of Wine》（1971，地理优先）**[T01-S015] + INAO/AOC terroir 法理（Track 06 T06-S015）。**当前代表**：**Jancis Robinson / Julia Harding**（Oxford Companion / Atlas 事实层双核，[T01-S003/S004]）；制度化身 = 法 AOC / 意 DOCG / 德 VDP（按地块）。**取向**：以产地为酒名，terroir 不可复制。 (evidence: [T01-S015]；Track 06 T06-S015/S016/S022)
- **新世界品种/技术派** — **奠基**：**UC Davis（Amerine + Winkler）**——气候区（Region I-V）指导「哪里种什么」、把酿造当技术[T01-S023/S024/S025]。**当前代表**：AVA 体系（只圈地不管品种/产量）+ 加州/澳新技术派酿造；AWRI（澳，tannin/rotundone 实证，Track 04）。**取向**：以品种命名、技术与气候数据驱动。 (evidence: [T01-S023, T01-S025]；Track 06 T06-S004)
- **核心分歧**：「地理/产区先于品种」（旧世界，AOC）⇄「品种/技术先于地理」（新世界，AVA + varietal 标签）。**José Vouillamoz（③）在此交叉**：用 DNA 解释品种-产地迁徙，既支持品种科学、又祛魅旧世界的「本土起源神话」[T01-S019]。**Tim Atkin（④）**关注新兴产区（南非/南美），介于两派之间[T01-S046]。 (evidence: [T01-S019, T01-S046])

### 谱系 ③ 自然酒/低干预派 vs 传统技术派（与 ⑤ 部分重叠，此处聚焦「干预 vs 放手」轴）

- **自然酒/低干预派** — **精神源头**：生物动力 = **Rudolf Steiner 学说**，经 **Nicolas Joly（Coulée de Serrant，1984 认证，「生物动力教父」）落地葡萄酒**[T01-S043/S044]。**当代旗手/文本**：**Isabelle Legeron MW《Natural Wine》+ RAW WINE**[T01-S041/S042]。**取向**：有机/生物动力种植 + 酒窖「不加不减」（原生酵母、无添加 SO₂、不下胶过滤）。
- **传统技术派/科学审视方** — **奠基**：**Émile Peynaud（⑤，现代酿酒学之父，清洁科学控制）**[T01-S021] + UC Davis 学院科学。**审视中间派**：**Jamie Goode + Benjamin Lewin（数据/科学怀疑派）**——不照单全收自然酒的护教叙事，要求实证[T01-S017/S039/S045]。**取向**：可控、可复现、卫生科学。
- **核心分歧**：「最低干预 = 捕捉地方生命力/真实」（Joly/Legeron）⇄「干预 = 卫生科学品质保障」（Peynaud/学院派）⇄「两边都要实证审视」（Goode/Lewin）。**反例不软化**：自然酒「无定义、缺陷酒被美化」是科学派的实打实质疑[T01-S042 书评]；生物动力的「能量/宇宙力」解释框架未被科学接受（其有机农艺效果与玄学解释须分开看，[T01-S043/S045]）。 (evidence: [T01-S043, T01-S041, T01-S021, T01-S017])

### 谱系 ④ Parker 百分制点评派 vs Jancis 20 分制散文派

- **百分制派** — **奠基人**：**Robert Parker（50-100 分制，《Wine Advocate》，消费者友好、偏浓郁果味）**[T01-S007]。**当前代表**：**Antonio Galloni（Vinous，Parker 体系继承+平台化）**[T01-S013]、**Tim Atkin MW（产区年报百分制）**[T01-S046]、Wine Spectator/Wine Enthusiast。**取向**：百分制可通约、给消费者明确锚点。
- **20 分制散文派** — **奠基/学术源头**：**UC Davis 20 分制（Amerine 1959，学术校准）**[T01-S023]；**当前旗手 = Jancis Robinson MW（20 分制 + 散文式独立评论）**[T01-S001/S002]。**取向**：分数刻度粗、不假装精确，重散文语境与评论独立。
- **核心分歧**：「分数可跨评论家通约、是消费速记」（Parker/Galloni）⇄「分数是酒与品鉴者的互动、不可通约、宁可粗」（Jancis，引 Goode「分数不是酒的属性」[T01-S002]）。**反例不软化**：① Parker 的「Parkerization 同质化」批评有大量从业者体感（[T01-S007/S009/S010]），其本人自辩亦是一手立场（[T01-S008]）；② 百分制评分（含 Atkin 的 100 分/95+ 数字）是**主观刻度 + 单一评论家口径**，引用须挂 caveat（[T01-S047]）；③ Jancis 是「被迫打分的反对者」，立场本身拧巴（[T01-S001]）。 (evidence: [T01-S007, T01-S008, T01-S001, T01-S002, T01-S047])

### 谱系 ⑤ 经典平衡派 vs 浓郁现代派酿造（含 Peynaud → 现代酿酒学，Joly → 生物动力对立面）

- **经典平衡派** — **奠基张力源**：**Émile Peynaud** 既是现代酿酒学之父（清洁科学）、又因「Peynaudization 同质化」成为后世反思对象——**他是这条轴的双重原点**[T01-S021]。**当前代表**：**Rajat Parr + In Pursuit of Balance（IPOB，加州反 fruit bomb，求优雅/低酒精/鲜酸）**[T01-S034/S035]。**取向**：平衡、克制、可陈年、site-specific。
- **浓郁现代派** — **市场放大器**：**Robert Parker（偏好大果味/高酒精/重橡木，经市场成「国际风格」）**[T01-S007]。**当前代表**：暖气候浓郁风格酿造 + 飞行酿酒师（Michel Rolland 等，micro-oxygenation 软单宁）。**取向**：浓郁、即饮愉悦、高分导向。
- **第三条路（反技术主义）**：**Nicolas Joly 生物动力**——既反 Peynaud 现代主义、也不属浓郁现代派，主张「真酒 vs 冷聪明」[T01-S044]。
- **核心分歧**：「优雅/平衡/克制」（经典平衡派，IPOB）⇄「浓郁/果味/即饮高分」（浓郁现代派，Parker 放大）。**反例不软化**：IPOB 的「平衡」主张也被批为**另一种风格教条**（把低酒精道德化、贬低正当的暖气候风格），且 IPOB 已约 2016 解散（部分因 balance 一词被过度政治化）——如实记录该运动的争议与落幕[T01-S034]。 (evidence: [T01-S021, T01-S034, T01-S007, T01-S044])

---

### 冷僻 / 信号薄弱（→ Phase 2.8 诚实边界）

- **figures 数量充足**：本 track 详条 18 位（含合条 Schneider/Atkin），≥ 12 门槛达标；5 组流派谱系奠基人→当前代表→核心分歧全部齐全 ✅。**不触发冷僻协议。**
- **中文原创一手 figure ≈ 0（头号诚实边界，与 Track 04/05/06 一致）**：本 track 18 位 thought leaders **无一人以中文为一手语言**，无一人在英文 canon / 评论 / 长访谈 / 认证生态里被多源点名为奠基人或当前代表。中文世界的「葡萄酒大佬」主要是：① WSET 中国体系讲师/培训机构创办人（二手转述英文教材，非原创思维体系）；② 公众号大号（知味葡萄酒杂志、红酒世界等——属 Track 06 黑名单衍生生态，**不作 figure 真伪来源**）；③ 个别华人 MW（如李志延 Jeannie Cho Lee MW、赵凤仪等亚洲 MW，**其一手输出仍主要为英文**，且本轮 search 未做亚洲华人 MW 专项深挖 → 标为**未展开缺口**，Phase 1.5 可补）。**结论**：中文从业者要接触一手 figure 思维，结构性地必须经英文（+法文）；SKILL.md「行业大佬」节须明说「本维度严重 en+fr-primary，无中文原创奠基人，中文用户须经英文获取」。 (evidence: 全 manifest 无中文一手源)
- **bucket 现实（与前三 track 同构）**：本 track **真 verified_primary = 0**（无 .edu/.gov/.ac.uk/arxiv 命中——figures 维度权威 = 评论家自有站 + 认证机构 + wikipedia 史实，结构性地不在学术域）。critic-own-site / 认证机构全部 verifier 默认 `secondary`，按 manifest 逃生阀人工升 `surrogate_primary` + keyword note（合规）。**特别标注**：`winespecific.com/about`（Lewin 个人博客）被 verifier 误判 `verified_primary`，已**人工下调 surrogate_primary**（rule 3：绝不标高于真实来源）。verified_primary 占比为 0 是行业结构性事实，非数据偷工——Phase 2.8 应如实说明。
- **数字 caveat 已挂**：Karen MacNeil「Come Over October 触达 20 亿 UVM」= 运动方自报平台指标（非审计）；Tim Atkin「南非第 6 支 100 分 / 217 支 95+」= 单一评论家主观刻度（不可跨评论家通约）；Wine Grapes「1368 品种」、Pocket Book「48 年/400 万册」= 出版方/书目元数据。均已就近标 caveat 或挂 source_id。
- **亚洲华人 MW 未深挖**：本轮聚焦英美法主轴 figure，对亚洲华人 MW（Jeannie Cho Lee MW 等）未做专项 search → 诚实标为「未展开」，非「不存在」；但即便补上，其一手输出语言仍主要为英文，不改变「中文原创一手 figure ≈ 0」结论。

---

## 与其他 Track 的协作 seed

- **→ Track 02 tools**：① **Wine Aroma Wheel**（Ann Noble，[T01-S027]）= 本 track 唯一「figure 即工具发明者」，tacit→codifiable 桥的工具化身，必入 Track 02。② **Winkler index / 气候区**（Amerine+Winkler，[T01-S025]）= 学院派核心工具（注气候变化重订）。③ **20 分制（Amerine/Jancis）vs 100 分制（Parker/Galloni/Atkin）评分表**（[T01-S001/S007/S046]）= 两套评分工具。④ **SAT 网格（WSET）vs deductive grid（CMS）**= 两套盲品工具（Track 06 已列）。⑤ **CellarTracker / Wine-Searcher / Liv-ex / Vivino**（Track 05 已列，figure 维度补：Galloni 的 Vinous Preview 是「评分提前获取」工具化争议，[T01-S014]）。
- **→ Track 03 workflows**：① **盲品演绎流程**（CMS sight→nose→palate→结论 vs WSET SAT）——两派 figure（Dalton/Parr 服务派 vs WSET 知识派）的方法论分歧落到流程。② **Aroma Wheel 词汇校准流程**（Noble）= 品鉴词汇训练 workflow。③ **采收时机决策**（Parr/IPOB「每年多早采收求平衡」[T01-S035]）= 经典平衡派的酿造 workflow。④ **malolactic 控制决策**（Peynaud 范式 [T01-S021]）= 现代主义酿造 workflow。⑤ **自然酒「不加不减」酒窖流程**（Legeron/Joly [T01-S041/S044]）= 低干预派酿造 workflow（与 ④ 对立）。⑥ **产区年度报告生产流程**（Tim Atkin [T01-S047]）= 评论家的产区评级 workflow。
- **→ Phase 2.8 诚实边界（三点落地，与前三 track 共识）**：① **中英失衡**：figures 维度 en+fr-primary，中文原创一手 figure ≈ 0，须明写。② **verified_primary = 0**：figures 权威结构性不在 .edu/.gov（在评论家站 + 认证机构 + wikipedia），非偷工。③ **反例不软化已落地**：Parker 同质化、Peynaudization、CMS 2018 舞弊、IPOB 解散争议、Legeron 书的护教倾向、Joly 生物动力玄学未被科学接受、Galloni Vinous Preview 商业化质疑——七处负面均如实记录，未用「但他其实……」洗白。
- **↔ Track 04 canon 双向印证**：本 track 18 位中，**12 位是 Track 04 canon 作者/奠基人**（Jancis/Hugh Johnson/Harding/Vouillamoz/Peynaud/Goode/Lewin/MacNeil/Zraly→见 Track 04/Puckette/Parr/Legeron/Noble）——双向印证「canon 作者通常就是 figure」。本 track 新增非 canon 作者的 figure：**Robert Parker（评分原点）、Antonio Galloni（当代评论第二极）、Levi Dalton（口述史）、Elizabeth Schneider（去精英化播客）、Nicolas Joly（生物动力教父）、Amerine+Winkler（学院奠基）、Tim Atkin（产区年报）**——这 7+ 位是 figures 维度对 canon 的关键补充。
- **一致性检查**：若 Phase 1.5 补**亚洲华人 MW**（Jeannie Cho Lee MW 等）或**法/意/西本土一手 figure**（如 Burgundy/Barolo 名酿、波尔多 oenologue 当代代表），可丰富 ② 旧世界风土派当前代表与中文可及性——但不改变「中文原创一手 figure ≈ 0、核心 figure en+fr-primary」的结构性结论。
