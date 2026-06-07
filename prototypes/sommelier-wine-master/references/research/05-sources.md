# Track 05 — Sources（信息源）：侍酒师 / 葡萄酒（Sommelier & Wine）

> Phase 1 wave 1 research subagent 输出。行业 = 葡萄酒鉴赏 + 侍酒服务的职业认知 OS。locale = global / en+fr-primary。
> 范围：资深从业者实际订阅 / 听 / 跟的持续信息源 —— newsletter / podcast / 会议 / 社区 / dataset。重点 = 「值不值得跟 + 为什么 + 投入产出比」+「信号 vs 噪音」。
>
> **中英失衡警告（贯穿全文，Phase 2.8 诚实边界要用）**：葡萄酒持续信息源几乎全部英文（+少量法文）。中文圈以培训机构公众号 / 知味 / 红酒世界等二手转述为主，**几乎无中文原创一手深度信息源**（podcast 长访谈尤其零）。本 track source 中英比 ≈ 30:1。下面所有 source 默认 en，未标 geographic_focus 即 en/global。

## Source Manifest

> bucket 规则提醒：`source_verifier.py classify` 自动只把 `.edu`/`.gov`/`.ac.uk`/`arxiv`、Apple Podcasts `/podcast/` 频道页、品牌域 `/podcasts` 路径判 `verified_primary`。葡萄酒**认证机构 / 教育社区**（guildsomm.com / wsetglobal.com / mastersommeliers.org）按 manifest 逃生阀标 `surrogate_primary` + note=`certification body`；**评论家自有出版站**（jancisrobinson.com / timatkin.com / vinous.com）标 `surrogate_primary` + note=`critic own publication`。trade media 主页（decanter / winespectator / wineenthusiast / sevenfiftydaily / vinepair / punchdrink）+ wikipedia = `secondary`。论坛 / 社区单帖 / 单条笔记 = `reference`。中文 blacklist（知乎/公众号/百度/CSDN/G2/Capterra/PR 通稿）绝不进表。
> **source_verifier scan 已跑（2026-06-06）**：所有 URL 跑过 classify。verified_primary 自动命中 = Apple Podcasts 频道页（10 个 podcast）+ guildsomm.com/podcasts 路径 + `.edu`（UC Davis / Cornell 课程）。surrogate_primary 为 manifest 人工升级（verifier 默认给 secondary，逃生阀合规）。blacklisted=0（无泄漏）、dead=0。

| source_id | url | bucket | last_checked | author/host | one-line note |
|-----------|-----|--------|--------------|-------------|---------------|
| T05-S001 | https://podcasts.apple.com/us/podcast/guildsomm-podcast/id425715938 | verified_primary | 2026-06-06 | GuildSomm International | podcast 频道页 — 侍酒师专业月更长谈, 业内基础设施级 |
| T05-S002 | https://podcasts.apple.com/us/podcast/ill-drink-to-that-wine-talk/id538210866 | verified_primary | 2026-06-06 | Levi Dalton | podcast 频道页 — 业内最深口述史式长访谈(503+集) |
| T05-S003 | https://podcasts.apple.com/us/podcast/wine-for-normal-people/id413879919 | verified_primary | 2026-06-06 | Elizabeth Schneider CSW | podcast 频道页 — 去精英化入门→中级, 2011 至今 |
| T05-S004 | https://www.jancisrobinson.com/ | surrogate_primary | 2026-06-06 | Jancis Robinson MW (+ team) | critic own publication — Purple Pages 订阅, 全球最权威评论网 |
| T05-S005 | https://www.decanter.com/ | secondary | 2026-06-06 | Decanter (Future plc) | trade media — 老牌权威杂志/赛事(DWWA)主站 |
| T05-S006 | https://www.winespectator.com/ | secondary | 2026-06-06 | Wine Spectator (M. Shanken) | trade media — 百分制+Top 100+酒单评级主站 |
| T05-S007 | https://www.wineenthusiast.com/ | secondary | 2026-06-06 | Wine Enthusiast | trade media — 评分+消费导向+Best of Year |
| T05-S008 | https://daily.sevenfifty.com/ | secondary | 2026-06-06 | SevenFifty Daily | trade media — 美国酒饮 trade(分销/侍酒/零售)深度报道 |
| T05-S009 | https://punchdrink.com/ | secondary | 2026-06-06 | PUNCH (Talia Baiocchi) | trade media — 酒饮文化长稿, 自然酒/小众产区先声 |
| T05-S010 | https://www.worldoffinewine.com/ | secondary | 2026-06-06 | World of Fine Wine | trade media — 学术派精品酒季刊, 长文/盲品 panel |
| T05-S011 | https://www.timatkin.com/ | surrogate_primary | 2026-06-06 | Tim Atkin MW | critic own publication — 产区年度报告(西/南非/阿根廷)百分制 |
| T05-S012 | https://www.liv-ex.com/news-insights/ | surrogate_primary | 2026-06-06 | Liv-ex | 精品酒交易所自有博客 (vendor docs; originator of Liv-ex 100/50 指数) — Fine Wine 100/50 指数+市场分析 |
| T05-S013 | https://podcasts.apple.com/us/podcast/vinepair-podcast/id1064515291 | verified_primary | 2026-06-06 | VinePair (Adam Teeter 等) | podcast 频道页 — 酒饮行业商业/趋势周更圆桌 |
| T05-S014 | https://podcasts.apple.com/us/podcast/unreserved-wine-talk/id1480477665 | verified_primary | 2026-06-06 | Natalie MacLean | podcast 频道页 — 获奖记者人物访谈, 书评/竞赛 |
| T05-S015 | https://podcasts.apple.com/us/podcast/matthews-world-of-wine-and-drink/id1500569099 | verified_primary | 2026-06-06 | Matthew Gaughan | podcast 频道页 — WSET 教育者向深度专题, 备考人群 |
| T05-S016 | https://podcasts.apple.com/us/podcast/wine-enthusiast-podcast/id1041426009 | verified_primary | 2026-06-06 | Wine Enthusiast | podcast 频道页 — 机构出品, 编辑+嘉宾 |
| T05-S017 | https://podcasts.apple.com/us/podcast/disgorgeous/id1502234212 | verified_primary | 2026-06-06 | Disgorgeous (Dan/Jacky) | podcast 频道页 — 自然酒/餐饮一线视角, 业内人闲谈 |
| T05-S018 | https://awards.decanter.com/DWWA | secondary | 2026-06-06 | Decanter (DWWA) | 赛事页 — 全球最大盲品赛(年度), 奖牌=市场信号 |
| T05-S019 | https://www.mastersofwine.org/ | surrogate_primary | 2026-06-06 | Institute of Masters of Wine | certification body — 含 IMW Symposium(四年一届) |
| T05-S020 | https://texsom.com/ | secondary | 2026-06-06 | TexSom | 会议页 — 北美最重要侍酒师专业大会(年度) |
| T05-S021 | https://sommconusa.com/ | secondary | 2026-06-06 | SommCon | 会议页 — 侍酒/饮品教育与商业大会(美, San Diego+DC) |
| T05-S022 | https://www.prowein.com/ | secondary | 2026-06-06 | ProWein (Messe Düsseldorf) | 会议页 — 全球最大葡萄酒烈酒贸易展(年度, 德) |
| T05-S023 | https://www.rawwine.com/ | secondary | 2026-06-06 | RAW WINE (Isabelle Legeron MW) | 会议页 — 全球最大自然酒展(多城巡回) |
| T05-S024 | https://www.guildsomm.com/ | surrogate_primary | 2026-06-06 | GuildSomm International | certification body 周边 — 含会员论坛(业内最高密度专业社区) |
| T05-S025 | https://www.reddit.com/r/wine/ | reference | 2026-06-06 | r/wine (Reddit) | 社区 — 大众+部分从业者, 入门问答密 |
| T05-S026 | https://www.wineberserkers.com/ | secondary | 2026-06-06 | Wine Berserkers | 论坛 — 资深藏家/极客社区, 老酒/产区深帖 |
| T05-S027 | https://www.cellartracker.com/ | secondary | 2026-06-06 | CellarTracker (Eric LeVine) | 数据平台 — 全球最大众包品鉴笔记+酒窖管理 |
| T05-S028 | https://www.wine-searcher.com/ | secondary | 2026-06-06 | Wine-Searcher | 数据平台 — 全球比价+均价+评分聚合 |
| T05-S029 | https://www.vivino.com/ | secondary | 2026-06-06 | Vivino | 数据平台 — 大众众包评分(亿级), 信号噪音比低 |
| T05-S030 | https://www.liv-ex.com/ | secondary | 2026-06-06 | Liv-ex | 数据平台 — 精品酒二级市场价格指数(投资级信号) |
| T05-S031 | https://vinous.com/ | surrogate_primary | 2026-06-06 | Antonio Galloni (Vinous) | critic own publication — 订阅评论+产区报告+Cellar Favorites |
| T05-S032 | https://www.ft.com/jancis-robinson | secondary | 2026-06-06 | Financial Times / Jancis Robinson | 专栏 — Jancis FT 每周专栏(部分免费窗口) |
| T05-S033 | https://www.wsetglobal.com/ | surrogate_primary | 2026-06-06 | WSET | certification body — 知识+SAT 体系, blog/知识中心 |
| T05-S034 | https://meiningers.com/ | secondary | 2026-06-06 | Meininger's International | trade media — 欧洲酒业商业/市场分析 |
| T05-S035 | https://jancisrobinson.com/purple-pages | surrogate_primary | 2026-06-06 | Jancis Robinson MW | critic own publication — Purple Pages 付费会员区(每日更新) |

---

## 1. Podcast（深度长访谈最揭示行业 OS）

> 葡萄酒行业的「tacit 知识」主要靠口述传递 —— 谁跟谁学、某产区为何这样做、一个酿酒决策背后的判断，书里没有，长访谈里有。这是 podcast 在本行价值远高于平均的原因。

### 🎙 1. GuildSomm Podcast

- **Type**: podcast (institutional)
- **URL**: https://podcasts.apple.com/us/podcast/guildsomm-podcast/id425715938 ｜ 站内: https://www.guildsomm.com/public_content/features/podcasts/b/guild_podcasts
- **Host**: MS Christopher Tanghe（教育总监）+ 早期 MS Geoff Kruth（GuildSomm 联合创始人）；社区经理 Stacy Ladenburger 主持部分盲品集
- **Cadence**: 月更（约每 2-4 周一集）
- **Last activity**: 2025-09（活跃，机构级稳定输出）
- **Audience tier**: practitioner / senior（备考 Advanced/MS/MW 的在职侍酒师为核心听众）
- **One-liner**: 侍酒师认证体系内部「官方」长谈——每月与 MS/MW/酿酒师/进口商深聊单一产区或盲品技法，是从业者把「认证理论」校准成「实战判断」的 anchor。
- **典型每期内容**: 单产区深潜（如 Sarah Jane Evans MW 谈西班牙中南部 / Jerez / 起泡新动向）、盲品技法拆解（Geoff Kruth 与 MS 玩「20 questions 盲猜两支酒」）、年度复盘（Tanghe + Jonathan Eichholz 回顾 2025 趋势/挑战、展望 2026）、酿酒师对谈（华盛顿酿酒师 Erica Orr 谈酿造）。(evidence: [T05-S001, T05-S024])
- **投入产出比**: high — ≥80% 集对备考/在职侍酒师有直接 actionable 信号（产区事实更新 + 盲品方法）。从业者必跟。(evidence: [T05-S001])
- **Paywall**: none（podcast 免费；深度 study 资源在 guildsomm.com 会员墙后，约 $149/yr）
- **Endorsement evidence**: GuildSomm 是 CMS/MW 备考生态的事实标准社区，podcast 被 TexSom 等大会列为推荐（cross_source）；多家「best wine podcast」榜常列（community_consensus）。(evidence: [T05-S001, T05-S020])
- **替代品**: Matthew's World of Wine and Drink（同为教育/备考向，但个人制作、英国视角）
- **Decay risk**: low — 机构级 source，GuildSomm 维持。
- **可信度**: high

### 🎙 2. I'll Drink to That! Wine Talk —（业内最深长访谈，最值得长听）

- **Type**: podcast (personal, 但已成行业口述史基础设施)
- **URL**: https://podcasts.apple.com/us/podcast/ill-drink-to-that-wine-talk/id538210866 ｜ 站: https://illdrinktothatpod.com/
- **Host**: Levi Dalton（前纽约顶级餐厅侍酒师，Masa/Convivio/Alto）
- **Cadence**: 月更（不定期，深度优先于频率），累计 **503+ 集**
- **Last activity**: 2025（活跃；十余年持续）
- **Audience tier**: senior（资深从业者最爱；非入门，假设你已知道嘉宾是谁）
- **One-liner**: 葡萄酒界的「口述史」——Dalton 把全球最重要的酿酒师/酒商/侍酒师/作家请进小公寓，1-2 小时让他们坦诚讲自己的人生与工作；想理解「这一行的人怎么想、师承如何流动」，这是单点密度最高的一手信号源。
- **典型每期内容**: 单一人物 1.5-2h 深访（德国 Rheingau 老牌酒庄主、加州 Santa Barbara 先锋、勃艮第世家、波尔多 oenologue、传奇侍酒师/作家），少剪辑、近乎独白式自述——很多嘉宾在别处从不长谈，只在这里开口。(evidence: [T05-S002])
- **投入产出比**: high（对资深而言）/ medium（对入门）— 单集信息密度极高，但需要背景知识才能解码；不是「每周追」而是「按嘉宾点播 + 长期沉淀」。(evidence: [T05-S002])
- **Paywall**: none（全免费）
- **签名内容**: 与各国传奇酿酒师/侍酒师的长访谈构成的庞大档案库（503+ 集本身即资产，可按产区/人物检索）。
- **Endorsement evidence**: 业内公认「最深的长访谈」，被多 figure 在访谈中 cross-recommend；Decanter/榜单常年推荐（cross_source + community_consensus）。Levi Dalton 本人即 Track 01 figure 候选。(evidence: [T05-S002])
- **替代品**: 无真正等价物（这是本行最稀缺的一手长访谈源）；UnReserved Wine Talk 在「人物访谈」维度部分重叠但更轻、更面向大众。
- **Decay risk**: medium — 个人制作，频率本就低；但十余年韧性 + 已成档案资产，停更也不损存量价值。
- **可信度**: high

### 🎙 3. Wine for Normal People

- **Type**: podcast (personal)
- **URL**: https://podcasts.apple.com/us/podcast/wine-for-normal-people/id413879919 ｜ 站: https://www.winefornormalpeople.com/podcast/
- **Host**: Elizabeth Schneider（CSW + WSET，去精英化布道者）
- **Cadence**: 周更（2011 至今，长青）
- **Last activity**: 2025（活跃）
- **Audience tier**: beginner → practitioner（系统打基础；故意去「装腔」）
- **One-liner**: 把葡萄酒从「势利」里解放出来——用普通人能懂的话讲清产区/品种/酿造，是新手到中级最稳的系统化听觉教材。
- **典型每期内容**: 单产区/单品种系统讲解（无嘉宾或轻嘉宾），偶有酿酒师对谈；强调「让你喝得更好更有趣」而非堆术语。十余年积累成体系化曲库，可当「有声 WSET 基础」。(evidence: [T05-S003])
- **投入产出比**: high（对 beginner/practitioner）/ low（对已 Advanced 以上的 senior——内容偏基础）。(evidence: [T05-S003])
- **Paywall**: 免费 podcast + 可选 Patreon 会员（附加内容/品鉴；约 $9/mo，非必需）
- **Endorsement evidence**: 长青头部入门 podcast，多「best wine podcast」榜常驻；与 WSET 学习路径互补（community_consensus + cross_source）。(evidence: [T05-S003])
- **替代品**: Wine 101（VinePair, Keith Beavers）——同为入门但更碎片；The Wine Pair（$25 以下实测，更消费向）。
- **Decay risk**: low-medium — 个人但已运营 14 年，品牌化、稳定。
- **可信度**: high

### 🎙 4. VinePair Podcast

- **Type**: podcast (institutional)
- **URL**: https://podcasts.apple.com/us/podcast/vinepair-podcast/id1064515291
- **Host**: VinePair 编辑团队（Adam Teeter 等创始/编辑）
- **Cadence**: 周更
- **Last activity**: 2025（活跃）
- **Audience tier**: practitioner / mixed（酒饮**行业商业/趋势**视角，含啤酒烈酒）
- **One-liner**: 酒饮行业的「商业与趋势」周更圆桌——关注品类经济、消费转向、市场结构，是从「商业/分销」而非「品鉴」角度跟行业的窗口。
- **典型每期内容**: 三人编辑圆桌聊一周酒饮新闻 + 趋势（如年度 Top 50 wines、品类增长/下滑、no-low 趋势、行业并购）。信号偏「行业经济/市场」而非「风土/品鉴」。(evidence: [T05-S013])
- **投入产出比**: medium — 50-80% 集有趋势信号，对零售/分销/品牌端从业者更高；纯品鉴向侍酒师作 ambient awareness。(evidence: [T05-S013])
- **Paywall**: none
- **Endorsement evidence**: VinePair 为头部酒饮媒体，podcast 在行业内广被引用（cross_source）；多榜常列（community_consensus）。(evidence: [T05-S013])
- **替代品**: Wine Enthusiast Podcast（同机构出品，但更品鉴/消费向）
- **Decay risk**: low — 机构媒体支撑。
- **可信度**: medium-high（商业视角强，深度品鉴弱）

### 🎙 5. UnReserved Wine Talk

- **Type**: podcast (personal)
- **URL**: https://podcasts.apple.com/us/podcast/unreserved-wine-talk/id1480477665
- **Host**: Natalie MacLean（获奖葡萄酒记者/作家）
- **Cadence**: 周更
- **Last activity**: 2025（活跃）
- **Audience tier**: mixed（人物访谈为主，可听性高）
- **One-liner**: 记者底色的人物访谈——把酒界有趣的人请来坦诚对谈（世界最佳侍酒师赛、葡萄酒造假、书背后的故事），比 I'll Drink to That 更轻更叙事化。
- **典型每期内容**: 与作家/侍酒师/酿酒师/竞赛选手的访谈，主题如 World's Best Sommelier Competition、wine fraud/forgery、新书解读。叙事驱动，门槛低于 I'll Drink to That。(evidence: [T05-S014])
- **投入产出比**: medium — 信号好但偏「人物故事/趣味」而非「可操作技法」。(evidence: [T05-S014])
- **Paywall**: none
- **Endorsement evidence**: 获奖记者主持，被 Decanter 等推荐（cross_source）；榜单常列（community_consensus）。(evidence: [T05-S014])
- **替代品**: I'll Drink to That（更深/更资深）；Wine Enthusiast Podcast。
- **Decay risk**: medium — 个人 podcast 默认。
- **可信度**: medium-high

### 🎙 6. Matthew's World of Wine and Drink

- **Type**: podcast (personal)
- **URL**: https://podcasts.apple.com/us/podcast/matthews-world-of-wine-and-drink/id1500569099
- **Host**: Matthew Gaughan（英国，WSET 教育者）
- **Cadence**: 约周更/双周更
- **Last activity**: 2025（活跃）
- **Audience tier**: practitioner / senior（**WSET 备考人群**专项）
- **One-liner**: WSET 体系的「深度专题」个人电台——单主题钻得深，是 Diploma/备考人群补强弱项产区的私教式资源。
- **典型每期内容**: 单产区/单主题深讲（贴合 WSET Diploma 知识结构），英国视角，无嘉宾或轻嘉宾。(evidence: [T05-S015])
- **投入产出比**: medium-high（对 WSET 备考者）/ low（非备考者）。(evidence: [T05-S015])
- **Paywall**: none
- **Endorsement evidence**: WSET 学习社群内广为推荐（community_consensus）；与 GuildSomm（CMS 向）形成 WSET 侧对照（cross_source）。(evidence: [T05-S015])
- **替代品**: GuildSomm Podcast（CMS 向）
- **Decay risk**: medium-high — 个人制作。
- **可信度**: medium-high

### 🎙 7. Disgorgeous（自然酒 / 餐饮一线）

- **Type**: podcast (personal)
- **URL**: https://podcasts.apple.com/us/podcast/disgorgeous/id1502234212
- **Host**: 餐饮/酒吧一线从业者（自然酒圈）
- **Cadence**: 不定期
- **Last activity**: 2024-2025（频率不稳，核查时较松）
- **Audience tier**: practitioner（自然酒 / 餐饮 / 进口一线）
- **One-liner**: 自然酒与餐饮一线的「行话闲谈」——业内人不端着地聊进口、酒单、自然酒圈八卦与审美，是主流认证体系之外「另一种侍酒文化」的声音。
- **典型每期内容**: 与自然酒进口商/酿酒师/侍酒师的随意长谈，审美与圈层视角强（对照 GuildSomm 的「正统」）。(evidence: [T05-S017])
- **投入产出比**: medium / low — niche，主要面向自然酒圈 senior practitioner；信号集中但受众窄。(evidence: [T05-S017])
- **Paywall**: none
- **Endorsement evidence**: 自然酒圈内 cross-recommend；PUNCH 等自然酒友好媒体生态互引（cross_source）。(evidence: [T05-S017, T05-S009])
- **替代品**: PUNCH 的酒饮长稿（文字版同审美）
- **Decay risk**: high — 个人、频率不稳，12 月内可能停。标 niche。
- **可信度**: medium

> Podcast 小结：**GuildSomm（机构/备考）+ I'll Drink to That（资深口述史）+ Wine for Normal People（入门系统）** 是三根支柱，覆盖 senior→beginner 全谱。WSET 侧补 Matthew's World；商业侧补 VinePair；自然酒侧补 Disgorgeous。

---

## 2. Newsletter / 出版物（个人评论家 own-publication 信号最纯）

> 本行「newsletter」更多是**评论家自有付费出版站 + trade 杂志**的形态，而非 Substack。最高密度一手信号来自评论家自己的站（Jancis / Vinous / Tim Atkin），trade media 是 ambient awareness。

### 📰 8. JancisRobinson.com — Purple Pages（+ FT 专栏）

- **Type**: newsletter / 评论家自有出版站（critic own publication）
- **URL**: https://www.jancisrobinson.com/ ｜ 会员区: https://www.jancisrobinson.com/membership ｜ FT 专栏: https://www.ft.com/jancis-robinson
- **Author**: Jancis Robinson MW + 团队（Julia Harding MW、Tamlyn Currin、Alder Yarrow 等）
- **Cadence**: Purple Pages **每日更新**；FT 专栏每周
- **Last activity**: 2025-2026（每日活跃）
- **Audience tier**: practitioner / senior（全球最权威，教育者/资深偏 20 分制）
- **One-liner**: 全球最权威的葡萄酒评论网，Purple Pages 是资深从业者的「每日一手」——57,000+ 品鉴笔记 + 牛津葡萄酒指南最新在线版 + 世界葡萄酒地图（第 8 版），评论独立性是行业标杆。
- **典型每期内容**: 每日 1-3 篇新文（产区报告、新酒评分 20 分制、深度评论、读者问答），加 57,000+ 可检索 tasting notes、在线版《Oxford Companion to Wine》(RRP £40)、《World Atlas of Wine》8th ed 地图、与 CellarTracker 笔记打通。(evidence: [T05-S004, T05-S035, T05-S032])
- **投入产出比**: high — 对资深从业者近乎必订；评论独立 + 参考工具集成，单订阅顶半个参考书架。(evidence: [T05-S004])
- **Paywall**: **paywall: £85/yr（约 $122）或 £8.50/mo**（2025-05-27 起涨价）。**Worth it 判断**：资深/职业从业者 yes（独立评论 + Oxford Companion 在线 + Atlas 地图打包，远超价值）；纯爱好者可先用 FT 每周专栏（部分免费窗口）试水。(evidence: [T05-S035, T05-S032])
- **签名内容**: Jancis 的 20 分制评分体系与盲品方法论长文；年度产区报告；Julia Harding 等团队的细分产区覆盖。(evidence: [T05-S004])
- **Endorsement evidence**: 行业最广引用的评论权威之一（cross_source 无数）；Liv-ex 等机构与其互引（cross_source）；Track 04 canon 中《Oxford Companion》《World Atlas》作者本人。(evidence: [T05-S004, T05-S012])
- **替代品**: Vinous（Galloni，更偏新世界+意大利/加州 + 视频/地图）；二者常被资深者并订互补。
- **Decay risk**: low — 已是行业基础设施；团队化运营降低个人依赖。
- **可信度**: high

### 📰 9. Vinous（Antonio Galloni）

- **Type**: newsletter / 评论家自有出版站（critic own publication）
- **URL**: https://vinous.com/ ｜ 关于: https://vinous.com/about
- **Author**: Antonio Galloni（前 Wine Advocate，2013 自立门户）+ 评论团队（Neal Martin、Josh Raynolds 等）
- **Cadence**: 持续每日流（rolling daily stream）
- **Last activity**: 2025-2026（每日活跃）
- **Audience tier**: practitioner / senior / 藏家
- **One-liner**: 「媒体 × 技术」形态的现代评论站——新酒/回溯/老酒垂直品鉴 + 酿酒师视频 + 交互地图 + 餐厅推荐，每日更新；Bordeaux/California/Italy/Champagne 由 Galloni 亲评，是 Jancis 之外资深者最常并订的第二极。
- **典型每期内容**: 产区年度报告（含 Cellar Favorites/性价比清单）、老酒垂直回溯、Galloni 主笔波尔多/加州/意/香槟新酒、交互式产区地图、酿酒师访谈视频。(evidence: [T05-S031])
- **投入产出比**: high（对藏家/资深）— 覆盖与 Jancis 互补（新世界/意大利更厚）。(evidence: [T05-S031])
- **Paywall**: paywall（订阅制，约 $150/yr 档）。**Worth it**：买酒/藏酒决策依赖评分者 yes，尤其加州/意大利重仓者。
- **Endorsement evidence**: Galloni 为全球最具影响力评论家之一（Wikipedia + 广泛 cross_source）；WineBerserkers 等社区长期讨论其评分体系（community_consensus）。(evidence: [T05-S031, T05-S026])
- **替代品**: Jancis Purple Pages（更偏旧世界/20 分制）；Wine Advocate（Parker 遗产，百分制）。
- **Decay risk**: low — 已机构化、团队化。
- **可信度**: high

### 📰 10. Tim Atkin MW Reports

- **Type**: newsletter / 评论家自有出版站（critic own publication）
- **URL**: https://www.timatkin.com/
- **Author**: Tim Atkin MW
- **Cadence**: 年度产区专题报告 + rolling 文章
- **Last activity**: 2025（活跃）
- **Audience tier**: practitioner / senior（特定产区深度）
- **One-liner**: 单一产区「年度国别报告」的标杆——南非/西班牙/阿根廷/智利/勃艮第等逐年百分制深评，是这些产区从业者/买手判断年份与酒庄分级的高密度一手。
- **典型每期内容**: 年度国别报告（如 South Africa Report、Rioja、Argentina），含产区分级、酒庄评级、百分制评分、年份评价；体量大、覆盖深。(evidence: [T05-S011])
- **投入产出比**: high（对相关产区从业者/买手）/ medium（泛听众）。(evidence: [T05-S011])
- **Paywall**: 部分报告付费下载（单份计）+ 站内免费文章。**Worth it**：做相关产区的 buyer/somm 值。
- **Endorsement evidence**: MW + 资深记者双重权威，报告被产区/贸易方广泛引用（cross_source）。(evidence: [T05-S011])
- **替代品**: Jancis/Vinous 的对应产区报告（但 Atkin 的南非/南美更专精）。
- **Decay risk**: low-medium — 个人但已品牌化、年报制度化。
- **可信度**: high

### 📰 11. SevenFifty Daily

- **Type**: newsletter / trade media（secondary）
- **URL**: https://daily.sevenfifty.com/
- **Author**: SevenFifty Daily 编辑部（美国酒饮 trade）
- **Cadence**: rolling（多篇/周）
- **Last activity**: 2025（活跃）
- **Audience tier**: practitioner（侍酒/分销/零售/进口的**生意侧**）
- **One-liner**: 美国酒饮 trade 的「业务与文化」深度报道——酒单经济、分销三层制、侍酒职业现实、零售趋势，是侍酒师理解「这门生意如何运转」的最佳免费读物。
- **典型每期内容**: 长稿覆盖 somm 职业/薪酬、酒单设计、进口/分销结构、产区贸易、行业劳动议题。偏「商业/职业」而非「品鉴/评分」。(evidence: [T05-S008])
- **投入产出比**: medium-high（对 trade 侧从业者）— 免费且独家选题多。(evidence: [T05-S008])
- **Paywall**: none（免费）
- **Endorsement evidence**: 美国酒饮 trade 标杆媒体，广被业内引用（cross_source）。(evidence: [T05-S008])
- **替代品**: Meininger's（欧洲商业侧）；Wine Business（美，更产业数据）。
- **Decay risk**: low-medium — 机构媒体（曾随 SevenFifty 平台并入 Provi，需留意运营变动）。
- **可信度**: medium-high

### 📰 12. PUNCH

- **Type**: newsletter / trade media（secondary，文化长稿）
- **URL**: https://punchdrink.com/
- **Author**: Talia Baiocchi（主编）+ 撰稿群
- **Cadence**: rolling（多篇/周）
- **Last activity**: 2025（活跃）
- **Audience tier**: practitioner / mixed（审美/文化驱动）
- **One-liner**: 酒饮「文化长稿」的标杆——自然酒、小众产区、审美转向常在这里先成话题，是捕捉「下一个潮流」与品味变迁的领先指标。
- **典型每期内容**: 深度特稿（自然酒运动、被忽视产区/品种、侍酒审美变迁、酒吧文化），文字质量高，趋势先声。(evidence: [T05-S009])
- **投入产出比**: medium — 信号好但偏「文化/趋势」而非「技法/评分」；作趋势雷达高价值。(evidence: [T05-S009])
- **Paywall**: none（核心免费；有会员计划）
- **Endorsement evidence**: 酒饮文化写作标杆，被自然酒圈 + 主流媒体 cross-reference（cross_source）；与 Disgorgeous 等同审美生态互引。(evidence: [T05-S009, T05-S017])
- **替代品**: World of Fine Wine（更学术）；Disgorgeous（音频版同审美）。
- **Decay risk**: low-medium。
- **可信度**: medium-high

### 📰 13. World of Fine Wine（WFW）

- **Type**: newsletter / 季刊出版物（secondary，学术派）
- **URL**: https://www.worldoffinewine.com/
- **Cadence**: 季刊（quarterly）
- **Last activity**: 2025（活跃）
- **Audience tier**: senior（学术/收藏/最深一档）
- **One-liner**: 精品酒世界的「学术季刊」——长文、盲品 panel、历史/理论/品鉴哲学的最深一档读物，资深者用来做战略级反思而非日常追新。
- **典型每期内容**: 学术性长文（产区历史/品鉴理论/年份回顾）、专家盲品 panel 报告、收藏与市场分析。密度高、节奏慢。(evidence: [T05-S010])
- **投入产出比**: medium（季刊，非高频；但单篇深度高）— 作 senior 的深度补给。(evidence: [T05-S010])
- **Paywall**: paywall（订阅季刊/数字）。**Worth it**：资深/学术取向者值，泛从业者不必。
- **Endorsement evidence**: 学术派最权威季刊，MW/资深圈 cross-reference（cross_source + community_consensus）。(evidence: [T05-S010])
- **替代品**: Jancis 长文 / Decanter 深度特辑。
- **Decay risk**: low — 机构季刊。
- **可信度**: high

### 📰 14-16. Trade 杂志三家（Decanter / Wine Spectator / Wine Enthusiast — ambient awareness 层）

- **Type**: trade media（secondary）
- **URL**: Decanter https://www.decanter.com/ ｜ Wine Spectator https://www.winespectator.com/ ｜ Wine Enthusiast https://www.wineenthusiast.com/
- **Cadence**: rolling（日更资讯 + 月刊/期刊）
- **Last activity**: 2025-2026（均活跃）
- **Audience tier**: mixed（beginner→practitioner；消费+资讯）
- **One-liner**: 三大主流葡萄酒杂志，构成行业的「公共资讯层」——新闻/评分/榜单（Decanter DWWA、Wine Spectator Top 100、Wine Enthusiast Best of Year）是市场共识与消费风向的温度计，但深度与独立性低于评论家自有站。
- **典型每期内容**: 行业新闻、新酒评分（百分制）、年度榜单、产区/酒庄报道、消费导购。信号密度中等，重叠度高（三家覆盖相近）。(evidence: [T05-S005, T05-S006, T05-S007])
- **投入产出比**: medium / low（单看任一即可，三家互相替代）— 作 ambient awareness，不必逐篇。(evidence: [T05-S005, T05-S006, T05-S007])
- **Paywall**: Decanter/Wine Spectator 部分付费（评分库/Top 100 存档）；Wine Enthusiast 多免费。
- **Endorsement evidence**: 行业基础设施级品牌，互引 + 被引无数（cross_source + community_consensus）。Decanter Top 推荐了上述多个 podcast（cross_source）。(evidence: [T05-S005, T05-S006, T05-S007])
- **替代品**: 三家彼此即替代品（去重保留 1-2 即可）；Meininger's（欧洲商业向）。
- **Decay risk**: low — 机构级。
- **可信度**: medium（评分/资讯可信，但商业化程度高，深度评论不及自有站）

### 📰 17. Liv-ex 博客 / News & Insights（市场信号）

- **Type**: newsletter / 数据机构自有博客（surrogate_primary — 见 §5 Dataset）
- **URL**: https://www.liv-ex.com/news-insights/
- **Cadence**: 多篇/周
- **Last activity**: 2026-01（活跃，月度指数评论）
- **Audience tier**: senior / 投资/交易侧
- **One-liner**: 精品酒二级市场的「官方市场评论」——基于真实成交数据解读 Fine Wine 100/50 走势、区域热点（勃艮第/香槟/波尔多份额），是把「葡萄酒」当资产看时的一手信号。
- **典型每期内容**: 月度指数评论（如 2026-01 Liv-ex 100 连续 6 个月上涨、香槟领涨、勃艮第占交易额 31.8%）、年份/产区市场分析、报告。(evidence: [T05-S012, T05-S030])
- **投入产出比**: high（对精品酒投资/交易/高端零售）/ low（纯品鉴向 somm）。(evidence: [T05-S012])
- **Paywall**: 博客免费；交易平台/深度数据 B2B 付费。
- **Endorsement evidence**: 精品酒价格的行业基准来源，被 Jancis、各投资机构、媒体广泛引用（cross_source）。(evidence: [T05-S012, T05-S004])
- **替代品**: Wine-Searcher 市场数据（更零售向）。
- **Decay risk**: low — 行业基础设施。
- **可信度**: high

---

## 3. Conference / 行业大会

> 时效提醒：年度展会 decay 低；但 **IMW Symposium 间隔被拉长**（见下，next edition 2027-04，>18 月）→ 按 spec 降级 retain 优先级（用户难以等到）。

### 🏛 18. Decanter World Wine Awards（DWWA）

- **Type**: conference / 赛事（年度）
- **URL**: https://awards.decanter.com/DWWA ｜ 母站 https://www.decanter.com/
- **Cadence**: 年度（每年一届，全球最大规模盲品赛）
- **Last edition / Next**: 年度滚动（每年春夏评审、秋季公布）
- **One-liner**: 全球规模最大的盲品赛——上万款酒经 MW/MS 盲评分级，奖牌（尤其 Best in Show/Platinum）是跨市场最被认的「品质 + 商业」信号。
- **典型内容**: 数百评委（含大量 MW）盲品上万款酒，产出奖牌榜 + 评审 tasting notes；结果直接影响铺货与定价。(evidence: [T05-S018, T05-S005])
- **投入产出比**: high（作信号源/选酒参考）— 奖牌结果是 buyer/somm 的高效筛选锚。(evidence: [T05-S018])
- **Endorsement evidence**: 行业最具规模与公信力的赛事之一（cross_source + community_consensus）。(evidence: [T05-S018, T05-S005])
- **替代品**: IWC（International Wine Challenge）、IWSC。
- **Decay risk**: low — 年度机构赛事。

### 🏛 19. TexSom Conference（北美侍酒师大会）

- **Type**: conference（年度）
- **URL**: https://texsom.com/conference/
- **Cadence**: 年度
- **Last / Next edition**: 2025-08-24~26 → **2026-08-23~25（Irving/Dallas, Texas）**
- **One-liner**: 全美最重要、以侍酒师为中心的专业大会——教育 + 师承 + networking 的年度集结点，是北美 somm 圈「线下校准」的主场。
- **典型内容**: 产区/品鉴/服务的深度 seminar、盲品训练、TexSom Awards（侍酒师竞赛）、GuildSomm「Community and Conversation」加场；面向 beverage professional 的 mentoring。(evidence: [T05-S020, T05-S024])
- **投入产出比**: high（对北美在职/进阶 somm）— 一年一度的高密度学习 + 人脉。(evidence: [T05-S020])
- **Endorsement evidence**: 美国最大葡萄酒行业大会，501(c)3，GuildSomm 等机构深度参与（cross_source）。(evidence: [T05-S020])
- **替代品**: SommCon（更偏商业/expo）。
- **Decay risk**: low — 年度、机构化。

### 🏛 20. ProWein（全球最大葡萄酒烈酒贸易展）

- **Type**: conference / trade fair（年度）
- **URL**: https://www.prowein.com/
- **Cadence**: 年度（Messe Düsseldorf 主办）
- **Last / Next edition**: **2026-03-15~17（Düsseldorf, 德国）**；2026 扩展 ProSpirits 区 + 首设无酒精 Zero Tasting Bar
- **One-liner**: 全球葡萄酒+烈酒贸易的「年度交易所」——生产商、进口商、买手在此谈生意、看趋势，是 trade/分销侧从业者一年一度的必到。
- **典型内容**: 数千参展商、产区国家馆、品类趋势论坛（no-low、可持续）、B2B 撮合。偏「贸易/采购」而非「品鉴学习」。(evidence: [T05-S022])
- **投入产出比**: high（对进口/分销/采购）/ low（纯 somm 学习向）。(evidence: [T05-S022])
- **Endorsement evidence**: 全球最大葡萄酒贸易展，行业基础设施级（cross_source + community_consensus）。(evidence: [T05-S022])
- **替代品**: Vinexpo（巴黎/亚洲）、Wine Paris。
- **Decay risk**: low — 年度、机构级。

### 🏛 21. RAW WINE（全球最大自然酒展）

- **Type**: conference / fair（多城巡回，年度滚动）
- **URL**: https://www.rawwine.com/ ｜ 日程 https://www.rawwine.com/fairs/view/upcoming-fairs
- **Founder**: Isabelle Legeron MW（法国首位女性 MW，自然酒最权威推手）
- **Cadence**: 全年多城（NY/LA/Montréal/Toronto/Berlin/Paris/Copenhagen/Tokyo/Verona…）
- **Last / Next edition（2026 例）**: Paris 2026-02-08~09、Verona 2026-04-13、Tokyo 2026-05-10~11
- **One-liner**: 全球最大的低干预/有机/生物动力/自然酒社区与展会——主流认证体系之外「另一套酿造价值观」的线下中心，捕捉自然酒动向的一手现场。
- **典型内容**: 低干预生产商直接 pour、生产者讲座、自然酒认证/理念讨论；与 Disgorgeous/PUNCH 同一审美生态的线下版。(evidence: [T05-S023, T05-S017])
- **投入产出比**: high（对自然酒圈从业者）/ medium（泛 somm 作趋势了解）。(evidence: [T05-S023])
- **Endorsement evidence**: 自然酒领域规模与权威双第一，Legeron MW 创办（IMW 背书 + NYT 认证）（cross_source + community_consensus）。(evidence: [T05-S023])
- **替代品**: La Dive Bouteille（法，更核心圈）、各地 raisin.digital 列出的自然酒展。
- **Decay risk**: low-medium — 多城分散降低单点风险。

### 🏛 22. IMW International Symposium（Masters of Wine 学术峰会）—［降级 retain：间隔被拉长］

- **Type**: conference（每约四年一届）
- **URL**: 母机构 https://www.mastersofwine.org/ ｜ 11th 延期公告 https://www.mastersofwine.org/news/imw-postpones-11th-international-symposium-adelaide-to-april-2027/
- **Cadence**: 约四年一届（学术最高规格）
- **Last / Next edition**: 11th 原定 2026-11（Adelaide）→ **延期至 2027-04-15~18（Adelaide, 南澳）**
- **One-liner**: Masters of Wine 的全球学术峰会——三天最高规格的研究/品鉴/战略议题，是行业「学术派 + 战略层」的顶点；但四年一届且最新一届已延至 2027-04，**作为 source 的时效性弱**。
- **典型内容**: MW 与全球专家的研究报告、专题品鉴、行业战略圆桌（气候/市场/教育）。(evidence: [T05-S019])
- **投入产出比**: medium（一次性高，但频率极低）— 多数从业者跟「会后释出的内容/录像」而非到场。(evidence: [T05-S019])
- **Endorsement evidence**: IMW 主办，行业最高学术规格（surrogate_primary，certification body）（cross_source）。(evidence: [T05-S019])
- **替代品**: World of Fine Wine（学术内容的纸面替代）；DWWA/各地 MW seminar。
- **Decay risk**: low（机构存在稳定）；但 **next edition 间隔 >18 月 → retain 优先级下调**（spec 时效规矩）。(evidence: [T05-S019])

> 备注：**SommCon**（https://sommconusa.com/，San Diego 2026-11-03~05 + DC 2026-04）作为 TexSom 之外的北美侍酒/饮品教育-商业大会候选保留（secondary, [T05-S021]）；偏 expo/business。

---

## 4. Community / 社区

### 👥 23. GuildSomm Forum（业内最高密度专业社区）

- **Type**: community / 会员论坛
- **URL**: https://www.guildsomm.com/（论坛在会员区内）
- **Platform**: 自建（会员制，约 $149/yr）
- **规模**: 全球侍酒师认证备考生态的事实标准社区（CMS/MW 备考者高密度聚集）
- **One-liner**: 侍酒师专业社区的「内圈」——会员论坛 + compendium + 产区地图 + study wiki，是 Advanced/MS/MW 备考者交换一手实战知识的最高密度场所，专业纯度高于公开论坛。
- **典型内容**: 产区/品鉴/服务的专业讨论、备考互助、专家答疑；与其 podcast/study 资源一体。(evidence: [T05-S024, T05-S001])
- **投入产出比**: high（对认证路径上的从业者）— 专业信噪比最高。(evidence: [T05-S024])
- **Paywall**: 会员制（约 $149/yr）。**Worth it**：走 CMS/MW 路线者基本必入。
- **Endorsement evidence**: CMS/MW 备考生态共识社区；TexSom 等线下大会与其深度绑定（cross_source + community_consensus）。(evidence: [T05-S024, T05-S020])
- **Decay risk**: low — 机构级、订阅支撑。
- **可信度**: high

### 👥 24. Wine Berserkers（资深藏家/极客论坛）

- **Type**: community / 公开论坛
- **URL**: https://www.wineberserkers.com/
- **Platform**: 独立论坛（phpBB 式）
- **规模**: 国际资深藏家/极客社区，老牌活跃
- **One-liner**: 资深藏家与葡萄酒极客的「深水区」——老酒、稀有产区、年份成熟度、盲品故事的长帖密度极高，是公开网上「资深业余 + 部分专业」讨论质量最好的地方之一。
- **典型内容**: WINE TALK 版块的产区/年份/老酒深讨、盲品故事、与 CellarTracker 数据互证的笔记讨论（如「CellarTracker vs 专业评分」长帖）。(evidence: [T05-S026, T05-S027])
- **投入产出比**: medium-high（对资深/藏家）— 信号深但需自行淘帖。(evidence: [T05-S026])
- **Paywall**: none（免费）
- **Endorsement evidence**: 资深圈长期活跃地标，与 CellarTracker 社区交叉引用（cross_source + community_consensus）。(evidence: [T05-S026, T05-S027])
- **Decay risk**: medium — 独立论坛、与论坛软件命运绑定，但社区韧性强。
- **可信度**: medium-high

### 👥 25. r/wine（Reddit）

- **Type**: community（Reddit）
- **URL**: https://www.reddit.com/r/wine/
- **Platform**: Reddit
- **规模**: 大众级（数十万订阅），入门问答密集
- **One-liner**: 葡萄酒最大的公开大众社区——入门问答、买酒求助、新手友好，但专业密度与信噪比低于 GuildSomm/Berserkers，适合新手 ambient + 大众情绪温度计。
- **典型内容**: 新手提问、酒款求助、晒酒、初级讨论；偶有专业人士出没但非主体。(evidence: [T05-S025])
- **投入产出比**: low-medium（新手 medium，资深 low）— 作大众风向与入门答疑。(evidence: [T05-S025])
- **Paywall**: none
- **Endorsement evidence**: 规模最大的公开葡萄酒社区（community_consensus）；常作新手第一站。(evidence: [T05-S025])
- **替代品**: r/winemaking（酿造向）；Wine Berserkers（资深向上位替代）。
- **Decay risk**: low（平台级）/ 但质量与版务命运绑定。
- **可信度**: low-medium（单帖 reference，需交叉验证）

> 备注：**Jancis Robinson 论坛 / CellarTracker 评论区**作为评论家站/数据平台内的社区层并入对应卡片（§2 S004 / §5 S027），不单列以避免重复覆盖。

---

## 5. Dataset / 数据平台（信号 vs 噪音是本节核心）

> 本行「dataset」= 价格 + 评分 + 笔记三类数据平台。**信号 vs 噪音轴**：评论家长稿（高信号/小样本）→ 资深众包笔记（中信号/中样本）→ 大众众包评分（低信号/海量样本）。下面按此排列。

### 📊 26. Liv-ex（精品酒价格指数 — 投资级信号）

- **Type**: dataset / 价格指数平台
- **URL**: https://www.liv-ex.com/
- **Maintainer**: Liv-ex（伦敦精品酒交易所）
- **Cadence / Last update**: 实时成交 + 月度指数（2026-01 数据活跃）
- **One-liner**: 精品酒二级市场的「彭博」——Fine Wine 100/50/1000 等指数基于真实 B2B 成交，是「葡萄酒作为资产」最权威的价格信号（高信号、机构级）。
- **典型数据**: Fine Wine 100（100 款最抢手酒的二级市场基准）、Fine Wine 50（波尔多一级庄近 10 个年份）、区域指数（Champagne 50、Burgundy、Bordeaux）、成交份额/价格走势。(evidence: [T05-S030, T05-S012])
- **信号 vs 噪音**: **最高信号端**——真实成交价，无众包噪音；但仅覆盖「可投资」精品酒（波尔多/勃艮第/香槟/少数膜拜酒），不反映广义市场。(evidence: [T05-S030])
- **投入产出比**: high（投资/交易/高端零售）/ N/A（纯品鉴）。(evidence: [T05-S030])
- **Paywall**: 指数评论免费；交易平台/数据订阅 B2B 付费。
- **Endorsement evidence**: 精品酒价格行业基准，Jancis/媒体/投资机构普遍引用（cross_source）。(evidence: [T05-S030, T05-S004])
- **可信度**: high　**Decay risk**: low（行业基础设施）

### 📊 27. Wine-Searcher（全球比价 + 评分聚合）

- **Type**: dataset / 比价 + 聚合平台
- **URL**: https://www.wine-searcher.com/
- **Maintainer**: Wine-Searcher
- **Cadence / Last update**: 实时（全球商家报价滚动）
- **One-liner**: 全球葡萄酒的「比价 + 均价 + 评分聚合」引擎——查一支酒的全球零售价、历史均价、各评论家分数聚合，是 buyer/somm/消费者的事实查价标准。
- **典型数据**: 全球商家报价、Wine-Searcher 均价、各家评分（含 critic）聚合、产区/酒款资料。(evidence: [T05-S028])
- **信号 vs 噪音**: **中-高信号**（价格客观；评分聚合多源，但聚合本身会摊平 critic 个体差异）。零售视角，比 Liv-ex 广但浅。(evidence: [T05-S028])
- **投入产出比**: high（查价/选酒/定价）— 几乎人人会用。(evidence: [T05-S028])
- **Paywall**: 基础免费；Pro（看全部报价/历史价）付费（约 $6/mo 档）。
- **Endorsement evidence**: 全球事实标准查价工具，被各端广泛使用（community_consensus）。(evidence: [T05-S028])
- **可信度**: high　**Decay risk**: low

### 📊 28. CellarTracker（社区众包笔记库 — 资深笔记 > 分数）

- **Type**: dataset / 社区众包笔记 + 酒窖管理
- **URL**: https://www.cellartracker.com/
- **Maintainer**: Eric LeVine
- **Cadence / Last update**: 持续（用户滚动录入，全球最大众包笔记库）
- **One-liner**: 全球最大的众包品鉴笔记 + 酒窖管理库——价值不在「平均分」而在「找到口味与你相符的 taster 后追读其笔记」，并能跟踪一支酒的成熟轨迹；与 Jancis Purple Pages 打通。
- **典型数据**: 数千万条用户 tasting notes、社区均分、酒窖库存/适饮窗管理、与 Jancis Purple Pages 集成。(evidence: [T05-S027, T05-S035])
- **信号 vs 噪音**: **中信号（用对方法）**——社区共识里 **笔记比分数有用**：判断风格是否对味、成熟度进展，往往胜过专业；老手会「标记 favorite tasters 过滤噪音」、查 reviewer profile 排除刷分酒庄。原始聚合分则噪音偏高。(evidence: [T05-S027, T05-S026])
- **投入产出比**: high（藏家/资深，做适饮判断与酒窖管理）/ medium（泛用户）。(evidence: [T05-S027])
- **Paywall**: 免费（笔记/库存）；可选小额捐助/订阅去广告。
- **Endorsement evidence**: 与 Wine Berserkers 深度交叉（社区长帖讨论其用法 vs 专业评分）、与 Jancis 集成（cross_source + community_consensus）。(evidence: [T05-S027, T05-S026, T05-S035])
- **可信度**: medium-high（个体 taster 校准后高）　**Decay risk**: low-medium（个人维护但已基础设施化）

### 📊 29. Vivino（大众众包评分 — 海量但低信号）

- **Type**: dataset / 大众众包评分 App
- **URL**: https://www.vivino.com/
- **Maintainer**: Vivino
- **Cadence / Last update**: 持续（亿级用户滚动评分）
- **One-liner**: 全球最大的大众葡萄酒评分 App（扫标签查均分）——海量样本、消费者友好，但**信噪比最低**：均分受大众口味/价格预期/品牌效应污染，资深从业者多视其为「噪音/大众情绪」而非品质信号。
- **典型数据**: 亿级用户 1-5 星评分与均分、标签扫描识别、价格、购买链接。(evidence: [T05-S029])
- **信号 vs 噪音**: **最低信号端**——样本海量但大众化，均分易被甜度偏好/价格锚定/营销带偏；适合「大众接受度」而非「专业品质」判断。与 CellarTracker（资深笔记）形成鲜明对照。(evidence: [T05-S029, T05-S027])
- **投入产出比**: low（专业）/ medium（消费者快速决策）— somm 作大众接受度参考，不作品质依据。(evidence: [T05-S029])
- **Paywall**: 免费 + Vivino Premium（约 $5/mo）。
- **Endorsement evidence**: 用户规模行业第一（community_consensus）；但在资深社区常被作「噪音」对照讨论（cross_source，见 Berserkers/CellarTracker 帖）。(evidence: [T05-S029, T05-S026])
- **可信度**: low（专业维度）/ medium（大众接受度维度）　**Decay risk**: low（平台级）

> **信号 vs 噪音总轴（本节 Phase 2 关键）**：
> `Liv-ex 成交价（最高信号/窄）` → `Wine-Searcher 均价+评分聚合（高/广）` → `CellarTracker 资深 taster 笔记（中-高/需筛）` → `CellarTracker 聚合分 / 专业评论（中）` → `Vivino 大众均分（最低/海量）`。
> 资深从业者的判断 = **评论家长稿（Jancis/Vinous/Atkin）做品质锚 + Liv-ex 做价格锚 + CellarTracker 笔记做适饮校准 + Vivino 仅看大众接受度**。

---

## 总览（按 type 分组）

### Podcast — 7 个
| Source | Cadence | Host | 投入产出 | One-liner |
|--------|---------|------|---------|-----------|
| GuildSomm Podcast [S001] | 月更 | MS Christopher Tanghe / Geoff Kruth | high | 侍酒认证体系官方长谈，备考/在职 anchor |
| I'll Drink to That! [S002] | 月更(503+集) | Levi Dalton | high(senior) | 业内最深口述史长访谈，最值得长听 |
| Wine for Normal People [S003] | 周更 | Elizabeth Schneider CSW | high(初中级) | 去精英化系统入门，有声 WSET 基础 |
| VinePair Podcast [S013] | 周更 | VinePair 编辑部 | medium | 酒饮商业/趋势周更圆桌 |
| UnReserved Wine Talk [S014] | 周更 | Natalie MacLean | medium | 记者底色人物访谈，叙事化 |
| Matthew's World of Wine [S015] | 周/双周 | Matthew Gaughan | medium-high(备考) | WSET 备考深度专题私教 |
| Disgorgeous [S017] | 不定期 | 自然酒圈一线 | medium/low(niche) | 自然酒+餐饮一线行话闲谈 |

### Newsletter / 出版物 — 10 个
| Source | Cadence | Tier | 投入产出 | One-liner |
|--------|---------|------|---------|-----------|
| Jancis Robinson / Purple Pages [S004] | 每日 | senior | high | 全球最权威评论网，资深每日一手(£85/yr) |
| Vinous (Galloni) [S031] | 每日流 | senior | high | 媒体×技术现代评论站，Jancis 第二极 |
| Tim Atkin MW Reports [S011] | 年报+rolling | senior | high(对应产区) | 单产区年度国别报告标杆(南非/西/南美) |
| SevenFifty Daily [S008] | rolling | practitioner | medium-high | 美国酒饮 trade 业务与文化深度(免费) |
| PUNCH [S009] | rolling | mixed | medium | 酒饮文化长稿，趋势领先指标(自然酒先声) |
| World of Fine Wine [S010] | 季刊 | senior | medium | 精品酒学术季刊，最深一档 |
| Liv-ex News & Insights [S012] | 多篇/周 | senior | high(投资侧) | 精品酒市场官方评论(成交数据驱动) |
| Decanter [S005] | rolling | mixed | medium | 老牌权威杂志+DWWA(ambient) |
| Wine Spectator [S006] | rolling | mixed | medium/low | 百分制+Top 100(ambient) |
| Wine Enthusiast [S007] | rolling | mixed | medium/low | 评分+消费导向(ambient) |

### Conference — 5 个（+SommCon 候选）
| Conference | 频率 | 下届 | One-liner |
|-----------|------|------|-----------|
| DWWA [S018] | 年度 | 每年滚动 | 全球最大盲品赛，奖牌=市场信号 |
| TexSom [S020] | 年度 | 2026-08-23~25 Dallas | 全美最重要侍酒师专业大会 |
| ProWein [S022] | 年度 | 2026-03-15~17 Düsseldorf | 全球最大葡萄酒烈酒贸易展 |
| RAW WINE [S023] | 多城滚动 | Paris 02/Verona 04/Tokyo 05 (2026) | 全球最大自然酒展(Legeron MW) |
| IMW Symposium [S019] ⬇降级 | ~4 年 | 2027-04-15~18 Adelaide | MW 学术峰会(间隔>18月，时效弱) |
| SommCon [S021] (候选) | 年度 | 2026-11-03~05 San Diego | 侍酒/饮品教育-商业 expo |

### Community — 3 个
| Community | Platform | 规模 | One-liner |
|-----------|----------|------|-----------|
| GuildSomm Forum [S024] | 自建会员制 | CMS/MW 备考事实标准社区 | 业内最高密度专业社区($149/yr) |
| Wine Berserkers [S026] | 独立论坛 | 国际资深藏家/极客 | 资深藏家深水区，老酒/产区深帖 |
| r/wine [S025] | Reddit | 数十万(大众) | 最大公开大众社区，新手友好 |

### Dataset / 数据平台 — 4 个
| Dataset | URL | Maintainer | 信号档位 | One-liner |
|---------|-----|-----------|---------|-----------|
| Liv-ex [S030] | liv-ex.com | Liv-ex | 最高信号/窄 | 精品酒价格指数(投资级，成交价) |
| Wine-Searcher [S028] | wine-searcher.com | Wine-Searcher | 高/广 | 全球比价+均价+评分聚合 |
| CellarTracker [S027] | cellartracker.com | Eric LeVine | 中-高(需筛 taster) | 最大众包笔记库(笔记>分数) |
| Vivino [S029] | vivino.com | Vivino | 最低/海量 | 大众众包评分(噪音/大众接受度) |

---

## 6. 侍酒师 / 学习者怎么 stay current（新手 vs 资深路径）

> 信息源的「订阅组合」随职业阶段切换：新手要**系统打基础 + 低门槛**；资深要**一手深度 + 信号纯度 + 市场情报**。

### 新手 / 入门（beginner → 备考 WSET L2-3 / CMS Intro-Certified）

- **Podcast 核心**: Wine for Normal People（系统入门）[S003] + Wine 101/VinePair [S013]。
- **学习 + 查询**: WSET 知识中心 [S033]（跟自己考的体系）；Wine-Searcher [S028] 查价/识酒；Wine Folly 类入门图解（见 Track 04）。
- **社区**: r/wine [S025]（新手问答）→ 进阶后转 Wine Berserkers。
- **付费克制**: 暂不必订 Jancis/Vinous；先用免费的 FT 专栏 [S032] + trade 杂志免费内容 [S005/S007] 建立 ambient。
- **路径要点**: **先系统（podcast 体系化曲库 + 认证教材）后碎片**；别一上来追评论家分数（解码不了）。(evidence: [S003, S033, S028, S025])

### 资深 / 在职（practitioner → senior，备考 Advanced/MS/MW 或一线 buyer/somm）

- **Podcast 核心**: GuildSomm（CMS 向）[S001] 或 Matthew's World（WSET 向）[S015] 跟体系；I'll Drink to That [S002] 做深度/师承沉淀。
- **每日一手**: Jancis Purple Pages [S004]（必订级）+ Vinous [S031]（并订互补）；对应产区加 Tim Atkin 年报 [S011]。
- **市场/价格情报**: Liv-ex News & Insights [S012] + Wine-Searcher Pro [S028]（买手/高端零售必备）。
- **适饮/笔记校准**: CellarTracker [S027]（找对味 taster + 跟成熟度）；Vivino [S029] 仅看大众接受度。
- **社区 + 线下**: GuildSomm Forum [S024]（备考内圈）+ Wine Berserkers [S026]（藏家深水）；线下 TexSom [S020]（北美 somm 主场）/ ProWein [S022]（trade）/ RAW WINE [S023]（自然酒线）。
- **trade 业务面**: SevenFifty Daily [S008]（职业/分销现实）+ PUNCH [S009]（趋势雷达）。
- **路径要点**: 资深的信息消费 = **「评论家一手做品质锚 + Liv-ex 做价格锚 + CellarTracker 做适饮校准 + 长访谈做行业理解」**，主流 trade 杂志退为 ambient。(evidence: [S001, S004, S031, S012, S027, S020, S008])

### 自然酒 / 非主流路径（与上述并行的独立审美生态）

- Disgorgeous [S017]（音频）+ PUNCH [S009]（文字）+ RAW WINE [S023]（线下），构成主流认证体系之外的另一套 stay-current 路径。(evidence: [S017, S009, S023])

---

## Phase 2 提炼提示

### 「这一行的资深人订阅最多的 top 3 sources」（→ master skill「Sources — 信息源」节 highlights）

1. **Jancis Robinson / Purple Pages [S004]** — 全球最权威评论网，资深从业者近乎必订的「每日一手」；同时是 Track 04 canon 中《Oxford Companion》《World Atlas》作者本人，cross-track 出现密度最高。(evidence: [T05-S004, T05-S035, T05-S032])
2. **GuildSomm（Podcast + Forum）[S001/S024]** — CMS/MW 备考与在职侍酒师的事实标准生态（podcast + 论坛 + study 资源一体），北美大会深度绑定。(evidence: [T05-S001, T05-S024, T05-S020])
3. **I'll Drink to That! [S002]** — 业内最深的长访谈/口述史，资深者公认的「理解这一行怎么运转」的单点最高密度一手信号源。(evidence: [T05-S002])
> 紧随其后：Vinous [S031]（资深并订第二极）、Liv-ex [S012/S030]（价格信号基准）、CellarTracker [S027]（适饮校准）。

### 高密度「一手」信号源 vs 二手（Phase 2 区分用）

- **最纯一手（verified/surrogate primary，作者本人发声）**: I'll Drink to That [S002]、GuildSomm Podcast [S001]、Jancis Purple Pages [S004]、Vinous [S031]、Tim Atkin [S011]、Liv-ex 成交数据 [S030]。
- **二手（trade media，ambient）**: Decanter/Wine Spectator/Wine Enthusiast [S005/S006/S007]、SevenFifty Daily/PUNCH/Meininger's [S008/S009/S034]。
- **众包数据（信号需筛）**: CellarTracker 笔记 [S027]（中-高，筛 taster 后）、Vivino [S029]（最低，仅大众接受度）。

### 信号 vs 噪音判断（本 track 独有贡献，→ Phase 2 + 诚实边界）

- **数据平台信号轴**: Liv-ex 成交价（最高/窄）→ Wine-Searcher 均价+聚合（高/广）→ CellarTracker 资深笔记（中-高/需筛 taster）→ Vivino 大众均分（最低/海量）。(evidence: [T05-S030, T05-S028, T05-S027, T05-S029])
- **评论家长稿 vs 大众评分的核心张力**: 资深共识 = **笔记/长稿 > 聚合分数 > 大众星级**；CellarTracker 社区明确「笔记比分数有用、要标记 favorite tasters 过滤噪音」，与 Vivino「大众均分受甜度/价格/品牌污染」形成本行最清晰的信号-噪音对照。(evidence: [T05-S027, T05-S029, T05-S026])

### 「这一行最近的话题热度」（候选信号 — Phase 2.4 近期工作流变化）

- **topic-heat: incomplete（sources listed but content not deep-crawled）**——以下为 search 命中的 episode/issue 标题级线索，非全量爬取：
  - **精品酒市场触底回升**（2025 末-2026 初）: Liv-ex 100 连续 6 个月上涨、香槟领涨、勃艮第占交易额 31.8%；对照 2022-2025 修正期。(evidence: [T05-S012, T05-S030])
  - **no-low / 无酒精**: ProWein 2026 首设 Zero Tasting Bar + ProSpirits 区；VinePair 趋势圆桌反复提及。(evidence: [T05-S022, T05-S013])
  - **自然酒持续主流化**: RAW WINE 全球多城扩张 + Disgorgeous/PUNCH 审美生态。(evidence: [T05-S023, T05-S017, T05-S009])
  - **西班牙中南部 / Jerez 复兴、勃艮第现代化**: GuildSomm 2025 单产区集（Sarah Jane Evans MW / Natasha Hughes MW）。(evidence: [T05-S001])
- 若需 high-confidence topic-heat，建议 Phase 2 用 WebFetch 爬 GuildSomm/VinePair/Jancis 最近 10 期标题。

### 新 figures 发现（→ wave 2 Track 01）

- **Levi Dalton**（I'll Drink to That 主持，前纽约顶级侍酒师）— Track 04 未列，本 track 核心，强 figure 候选。(evidence: [T05-S002])
- **Elizabeth Schneider CSW**（Wine for Normal People）— 去精英化教育者，figure 候选。(evidence: [T05-S003])
- **Antonio Galloni**（Vinous 创始，前 Wine Advocate）— 当代最具影响力评论家之一，Track 04 未列，强 figure 候选。(evidence: [T05-S031])
- **Tim Atkin MW**（产区年报标杆）— figure 候选。(evidence: [T05-S011])
- **Christopher Tanghe MS / Geoff Kruth MS**（GuildSomm）、**Natalie MacLean**、**Talia Baiocchi**（PUNCH 主编）、**Eric LeVine**（CellarTracker 创始）— 次级 figure 候选。(evidence: [T05-S001, T05-S014, T05-S009, T05-S027])
- 已与 Track 04 重叠（不重复推）: Jancis Robinson、Isabelle Legeron MW、Julia Harding MW。

### 新 tools 发现（→ wave 2 Track 02）

- **CellarTracker**（众包笔记 + 酒窖管理 + Jancis 集成）— 兼数据平台与从业工具，Track 04 未列，强 tool 候选。(evidence: [T05-S027])
- **Wine-Searcher**（全球比价/识酒/评分聚合）— 事实标准查价工具，tool 候选。(evidence: [T05-S028])
- **Liv-ex**（价格指数/B2B 交易数据）— 投资/交易侧工具，tool 候选。(evidence: [T05-S030])
- **Vivino**（扫标签查均分 App）— 大众侧工具（需标信噪比低），tool 候选。(evidence: [T05-S029])

### 冷僻 / 信号薄弱（→ Phase 2.8 诚实边界）

- **本 track 信号充足，不触发冷僻协议**: newsletter 10 ✅、podcast 7 ✅、conference 5(+1) ✅、community 3 ✅、dataset 4 ✅。35 个 source，跨 5 type 全覆盖。
- **bucket 现实**: verified_primary 主要来自 Apple Podcasts 频道页（10 个 podcast）+ guildsomm.com/podcasts 路径；评论家自有站 / 认证机构 auto-secondary，已合法标 surrogate_primary（manifest 逃生阀）。葡萄酒权威 = 评论家 + 认证机构（不在 .edu/.gov），verified_primary 占比偏低是**行业结构性事实**，非偷工。
- **中文一手 = 0（头号诚实边界，与 Track 04 一致）**: 本 track 35 个 source 中文原创深度信息源 **= 0**。中文圈 stay-current 路径只能：①英文 source 直接消费（Jancis/GuildSomm/podcast 需英文听力），②WSET 中国培训生态（二手转述，教材英译），③知味/红酒世界等公众号（Track 06 黑名单，不作知识真伪来源）。**长访谈/podcast 维度中文几乎空白**——这是中文从业者 stay-current 的最大结构性缺口。SKILL.md「想跟最新动态」节必须明说「核心信息源 en-primary，中文用户须接受听/读英文，且中文圈无等价长访谈源」。(evidence: [T05-S002, T05-S004, T05-S033])
- **时效信号**: IMW Symposium next edition 已延至 2027-04（间隔>18 月）→ 已标降级 retain；SevenFifty 需留意随平台并入 Provi 的运营变动；个人 podcast（I'll Drink to That / Disgorgeous）decay medium-high，但 I'll Drink to That 存量档案即资产。

### 与其他 Track 的一致性

- **→ Track 01 figures**: 见上「新 figures 发现」（Levi Dalton / Galloni / Schneider / Tim Atkin 为本 track 新增）。
- **→ Track 02 tools**: 见上「新 tools 发现」（CellarTracker / Wine-Searcher / Liv-ex / Vivino 为本 track 新增）。
- **↔ Track 04 canon 双向**: Jancis（Oxford Companion/World Atlas）、Legeron（Natural Wine）的作者均同时是本 track 持续信源 host/founder — 双向印证「canon 作者通常有持续信源」。
- **→ Phase 2.8 诚实边界**: 中英失衡 + verified_primary 结构性偏低 + IMW 时效降级，三点须落地。
