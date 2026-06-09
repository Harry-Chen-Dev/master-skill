# Track 04 — Canon（知识正典）：调香师 / 香水（Perfumery & Fragrance）

> Phase 1 wave 1 research subagent 输出。行业 = 香水创作 + 香气调配的职业认知 OS。locale = global / **en+fr-primary**，profile = practitioner。
> 核心张力：codifiable 理论层（原料知识 / 香料化学 / 嗅觉家族分类 / accord 和弦 / 配方结构 % / 挥发度金字塔 / IFRA 法规）⇄ tacit 校准层（嗅觉记忆 / 闻香训练 /「the nose」/ 创作直觉 / 盲嗅识别）。
> 范围：必读书 + 技术教科书 + 教育 / 认证体系（学校 + 香精公司内部学校）+ 20-30 个核心概念 + 智识谱系（法系天然传统派 ⇄ 分子合成派；嗅觉科学之争）。
>
> **中英失衡警告（贯穿全文，Phase 2.8 诚实边界必用）**：香水一手 canon 几乎全部英文 + 法文。经典原著（Roudnitska / Ellena / Jean Carles method）原文为法文；技术教科书为英 / 德文（Ohloff 原德文）。法系传统（Grasse / ISIPCA / haute parfumerie）核心语境为法文。**中文世界几乎无原创一手 canon** —— 现存中文文本是 ① 译本（Ellena《香水：气味的炼金术》《调香师日记》有中译）+ ② 少数国产应用型技术教材（《调香术》《天然香料主成分手册》，偏日化香精工艺）+ ③ KOL / 社区测评二手。所有中文原创讨论几乎全部沉淀在黑名单平台（知乎 / 公众号 / 豆瓣 UGC），**不入 manifest**。本 track source 中英 + 法比 ≈ 30:1（详见末尾「中英失衡判断」）。
>
> **冷僻 + 闭源警告**：核心创作 know-how 藏在四大香精公司（Givaudan / DSM-Firmenich / IFF / Symrise）内部学校 + 调香师个人脑中，公开一手稀薄。本 track 大量使用 **Surrogate Sources Policy**：教育机构 / 香精公司学校（note 含 `perfumery school`）、标准 / 协会（IFRA，note 含 `standards body`）、调香师个人长访谈 / 自述（note 含 `perfumer own publication`）升级 `surrogate_primary`；香评社区（Fragrantica / Basenotes / Goodreads）仅作 `secondary` 元数据，**不冒充 verified_primary**。

## Source Manifest

> **bucket 规则提醒**：`source_verifier.py classify` 自动判定 → 只能人工**升级** `surrogate_primary`，不私自降级、不跳黑名单。本行业几乎无 .edu/.gov/arxiv 命中（香水学院 ISIPCA/GIP 为私立 .fr/.com 域，非 .edu），故 verified_primary 极少。香水**学校 + 香精公司内部学校**（ISIPCA/GIP/Givaudan School/Cinquième Sens/PerfumersWorld/Karen Gilbert）按 Surrogate Policy 标 `surrogate_primary` + note `perfumery school`；**IFRA** 标准机构标 `surrogate_primary` + note `standards body`；**调香师 / 原创者自述站**（fragrancesoftheworld = Michael Edwards 官方）标 `surrogate_primary` + note `own publication`。出版社页（Wiley/Springer/RSC/Rizzoli/OUP）+ 严肃香水媒体（Nez/Now Smell This/CaFleureBon/Perfumer&Flavorist）+ Wikipedia = `secondary`。Gutenberg/archive 公版书记录 = `secondary`（仅元数据，**不存全本**）。
>
> **黑名单泄漏处理（重要）**：`zhuanlan.zhihu.com` classify=`blacklisted` → **拒入 manifest**（已剔除）。`book.douban.com` 被 classifier 误判 verified_primary，但豆瓣是中文 UGC 书评平台（与知乎 / Goodreads 同质，应视 secondary/黑名单临界）→ 为保 manifest 干净，**整条 URL 弃用不引**，中文失衡仅以 search 层面 finding 记录、不挂问题 URL。同理 `thefragrancefoundry.com`（香水用品店商品页）、`4160tuesdays.com`（个人博客）被误判 verified_primary → **弃用不引**，相关 claim 改挂出版社页 / Wikipedia。
> **source_verifier 合规结论**：进表 URL 中 blacklisted=0（zhihu 已剔）、dead=0；verified_primary=0（无 .edu/.gov/arxiv 真命中，诚实反映行业闭源 + en/fr-primary）；surrogate_primary 为 manifest 人工升级，合规。

| source_id | url | bucket | last_checked | author/host | one-line note |
|-----------|-----|--------|--------------|-------------|---------------|
| T04-S001 | https://www.isipca.fr/en | surrogate_primary | 2026-06-07 | ISIPCA (Versailles) | perfumery school — 1970 Guerlain 创办的凡尔赛香水学校, MSc 800 原料 + accord, 法系 canon ground truth |
| T04-S002 | https://www.iff.com/scent/isipca-masters/ | surrogate_primary | 2026-06-07 | IFF × ISIPCA | perfumery school — IFF 与 ISIPCA 合办英文 MSc, 教 800 原料 + key accords + 香料化学 |
| T04-S003 | https://www.grasse-perfumery.com/long-term/international-technical-degree-in-fragrance-creation-and-sensory-evaluation/ | surrogate_primary | 2026-06-07 | GIP (Grasse) | perfumery school — 2002 Prodarom 创办, 18 月 + 6 月实习, 1200h, 原料/accord/家族识别/GC-MS, 英文授课 |
| T04-S004 | https://www.givaudan.com/fragrance-beauty/perfumery-school | surrogate_primary | 2026-06-07 | Givaudan | perfumery school — Jean Carles 1946 于 Roure 创办的传奇内部学校(仅员工), 4 年制 |
| T04-S005 | https://www.givaudan.com/fragrance-beauty/perfumery-school/hall-of-fame | surrogate_primary | 2026-06-07 | Givaudan | perfumery school — 名人堂列 Jean Carles 等奠基调香师, 谱系一手锚点 |
| T04-S006 | https://www.cinquiemesens.com/en/corporate-clients/training/ | surrogate_primary | 2026-06-07 | Cinquième Sens | perfumery school — 1976 Monique Schlienger(Jean Carles 弟子)创办, 开放招生, 香水配方 126h/嗅觉专家 203h |
| T04-S007 | https://www.perfumersworld.com/about-us.php | surrogate_primary | 2026-06-07 | PerfumersWorld (S. Dowthwaite) | perfumery school — Stephen Dowthwaite 5 日浸入式 + 函授, 「ABCs of Perfumery」教学法, 培训 6000+ 学员 |
| T04-S008 | https://www.karengilbert.co.uk/courses | surrogate_primary | 2026-06-07 | Karen Gilbert | perfumery school — 独立 / artisan 在线香水课(1 年自主进度), 面向小众独立调香师 |
| T04-S009 | https://ifrafragrance.org/initiatives-positions/safe-use-fragrance-science/ifra-standards | surrogate_primary | 2026-06-07 | IFRA | standards body — 香料安全用量标准(Prohibited/Restricted/Specified 三类), 与 RIFM 合作, 行业 ground truth |
| T04-S010 | https://ifrafragrance.org/initiatives-positions/environment-health/allergens | surrogate_primary | 2026-06-07 | IFRA | standards body — 致敏原管理, EU 2023/1545 致敏原标签 26→80+ 扩列 |
| T04-S011 | https://www.fragrancesoftheworld.com/ | surrogate_primary | 2026-06-07 | Michael Edwards | own publication — Fragrances of the World 官方站, 年度香水分类圣经 + fragrance wheel(14 家族) |
| T04-S012 | https://en.wikipedia.org/wiki/Edmond_Roudnitska | secondary | 2026-06-07 | — | Roudnitska 生平 + 著作(Le Parfum/L'Esthétique)+ Diorissimo/Eau Sauvage(史实/谱系) |
| T04-S013 | https://nstperfume.com/2006/06/12/perfume-books-le-parfum-by-edmond-roudnitska/ | secondary | 2026-06-07 | Now Smell This | 严肃香水媒体 — Le Parfum 书评(「应是每个调香学徒必读」endorsement) |
| T04-S014 | https://nstperfume.com/perfumers-l-to-s/edmond-roudnitska/ | secondary | 2026-06-07 | Now Smell This | 严肃香水媒体 — Roudnitska 调香师档案(美学派/纯嗅觉极简) |
| T04-S015 | https://en.wikipedia.org/wiki/Jean-Claude_Ellena | secondary | 2026-06-07 | — | Ellena 生平 + 著作(Diary of a Nose/Alchemy of Scent)+ Hermès 专属调香师(2004-16)(史实) |
| T04-S016 | https://cafleurebon.com/interview-with-jean-claude-ellena/ | secondary | 2026-06-07 | CaFleureBon | 严肃香水媒体 — Ellena 长访谈, 极简哲学「两个原料就停手」自述 |
| T04-S017 | https://en.wikipedia.org/wiki/Perfumes:_The_Guide | secondary | 2026-06-07 | — | Perfumes: The Guide 出版史(1992 法版→2008 英版→2018 版)+ 评分体系(史实) |
| T04-S018 | https://www.fragrantica.com/news/Perfumes-The-Guide-2018-by-Luca-Turin-and-Tanya-Sanchez-11058.html | secondary | 2026-06-07 | Fragrantica | 香评社区(仅元数据)— Perfumes: The Guide 2018 版介绍 |
| T04-S019 | https://en.wikipedia.org/wiki/Luca_Turin | secondary | 2026-06-07 | — | Luca Turin 生平 + 振动理论 + The Secret of Scent(嗅觉科学之争一方, 史实) |
| T04-S020 | https://www.amazon.com/Secret-Scent-Adventures-Perfume-Science/dp/0061133841 | secondary | 2026-06-07 | HarperCollins / L. Turin | 书目元数据 — The Secret of Scent(振动理论科普, 2006) |
| T04-S021 | https://www.amazon.com/Essence-Alchemy-Natural-History-Perfume/dp/1586857029 | secondary | 2026-06-07 | Mandy Aftel (Gibbs Smith) | 书目元数据 — Essence and Alchemy(天然香水圣经, 2001/2022 修订, 16 语种, Solomon 奖) |
| T04-S022 | https://artandolfaction.com/reading-list/ | secondary | 2026-06-07 | Institute for Art & Olfaction | 香水教育 NGO 推荐书单 — 分「文化/历史」「科学/技术」两类的权威 reading list |
| T04-S023 | https://www.amazon.com/Perfect-Scent-Inside-Perfume-Industry/dp/1400136571 | secondary | 2026-06-07 | Chandler Burr (Holt) | 书目元数据 — The Perfect Scent(NYT 香评人卧底巴黎/纽约香水业一年) |
| T04-S024 | https://en.wikipedia.org/wiki/Michael_Edwards_(fragrance_expert) | secondary | 2026-06-07 | — | Michael Edwards 生平 + Perfume Legends(访谈 150 人)+ fragrance wheel 1992 发明史(史实) |
| T04-S025 | https://perfumebottles.org/article/perfume-legends-ii-by-michael-edwards/ | secondary | 2026-06-07 | Int'l Perfume Bottle Assoc. | 协会刊评 — Perfume Legends II 评介(经典香水逐支解构) |
| T04-S026 | https://www.amazon.com/Perfume-Flavor-Materials-Natural-Origin/dp/195168205X | secondary | 2026-06-07 | Steffen Arctander | 书目元数据 — Perfume & Flavor Materials of Natural Origin(天然原料圣经, 1960, 500+ monograph) |
| T04-S027 | https://pubs.rsc.org/en/content/ebook/978-0-85404-528-0 | secondary | 2026-06-07 | RSC / Charles Sell | 出版社页 — The Chemistry of Fragrances(RSC 香料化学教科书, 多版) |
| T04-S028 | https://www.wiley.com/en-us/Perfumery:+Practice+and+Principles-p-9780471589341 | secondary | 2026-06-07 | Wiley / Calkin & Jellinek | 出版社页 — Perfumery: Practice and Principles(1994, 实务+伟大香水结构剖析) |
| T04-S029 | https://link.springer.com/book/10.1007/978-94-009-1567-1 | secondary | 2026-06-07 | Springer / Paul Jellinek | 出版社页 — The Psychological Basis of Perfumery(1951, J.S.Jellinek 译编 4th ed) |
| T04-S030 | https://www.fragrantica.com/news/A-Legend-on-Legends-Michael-Edwards-on-His-Life-s-Legacy-on-Perfume-How-Perfume-Leaves-a-Legacy-Of-Us-Part-I-20080.html | secondary | 2026-06-07 | Fragrantica | 香评社区(仅元数据)— Michael Edwards 长访谈(fragrance wheel 由来) |
| T04-S031 | https://www.amazon.com/Perfume-Lover-Personal-History-Scent/dp/125002501X | secondary | 2026-06-07 | Denyse Beaulieu (St. Martin's) | 书目元数据 — The Perfume Lover(与 Duchaufour 共创 Séville à l'Aube, 128 版迭代纪实) |
| T04-S032 | https://en.wikipedia.org/wiki/Denyse_Beaulieu | secondary | 2026-06-07 | — | Beaulieu 生平 + The Perfume Lover 创作合作史实 |
| T04-S033 | https://shop.perfumersapprentice.com/perfumersworkshop/carles2.pdf | secondary | 2026-06-07 | Perfumer's Apprentice (Carles 译文) | Jean Carles「A Method of Creation in Perfumery」英译 PDF — 方法论一手文本(原文 1961) |
| T04-S034 | https://www.perfumerflavorist.com/fragrance/fine-fragrance/article/21856193/the-juice-inside-givaudan-perfumery-school | secondary | 2026-06-07 | Perfumer & Flavorist | 行业期刊 — Givaudan 学校内幕(403 阻断未取全文, 仅标题/检索佐证) |
| T04-S035 | https://mag.bynez.com/en/reports/olfactory-education-how-to-cultivate-your-nose/where-to-train-as-a-perfumer/ | secondary | 2026-06-07 | Nez (olfactory mag) | 严肃嗅觉媒体 — 香水教育全景(ISIPCA/GIP/Cinquième Sens/内部学校 学费/时长/门槛对照) |
| T04-S036 | https://en.wikipedia.org/wiki/George_William_Septimus_Piesse | secondary | 2026-06-07 | — | Piesse 生平 + The Art of Perfumery(1857)+ odophone「notes」概念发明史(史实) |
| T04-S037 | https://www.gutenberg.org/ebooks/16378 | secondary | 2026-06-07 | Project Gutenberg | 公版书记录(仅元数据)— Piesse《The Art of Perfumery》全文公版(1857, notes 概念源头) |
| T04-S038 | https://en.wikipedia.org/wiki/Captive_odorant | secondary | 2026-06-07 | — | captive(专利分子)定义 — 四大公司独占策略(术语) |
| T04-S039 | https://en.wikipedia.org/wiki/Perfume_organ | secondary | 2026-06-07 | — | 调香师的「香风琴」orgue 定义 — 半圆阶梯式原料台(术语) |
| T04-S040 | https://blog.delacourte.com/en/the-accord/ | secondary | 2026-06-07 | Sylvaine Delacourte | 调香师教育页 — accord 定义(5-12 原料组合, 决定家族归属) |
| T04-S041 | https://www.sylvaine-delacourte.com/en/guide/the-olfactive-pyramid | surrogate_primary | 2026-06-07 | Sylvaine Delacourte | perfumer own publication — 调香师自有站教育页, 嗅觉金字塔 top/heart/base 挥发度结构 |
| T04-S042 | https://www.goodreads.com/book/show/13847.Essence_and_Alchemy | secondary | 2026-06-07 | Goodreads | UGC 书评(仅元数据/endorsement 计数)— Essence and Alchemy 读者评价基数 |
| T04-S043 | https://www.amazon.com/Scent-Chemistry-Molecular-World-Odors/dp/3527348557 | secondary | 2026-06-07 | Ohloff/Pickenhagen/Kraft (Wiley-VCH) | 书目元数据 — Scent and Chemistry(德文原 Riechstoffe…, 香料化学家圣经, 2022 2nd ed) |
| T04-S044 | https://www.fragrancesoftheworld.com/AboutUs | surrogate_primary | 2026-06-07 | Michael Edwards | own publication — Fragrances of the World 关于页(分类法权威性自述) |

---

## 总览（按类型分组）

### Textbook / 系统性著作（必读 5 / 推荐 3）

| 书名 | 作者 | 难度 | Endorsement | 一句话 |
|------|------|------|-------------|--------|
| Perfume and Flavor Materials of Natural Origin | Steffen Arctander | 高阶专家 | IAO 书单 + 业内通称「原料圣经」+ 多校教学引用 | 天然原料逐条 monograph(500+)，调香师查原料的字典 |
| The Chemistry of Fragrances | Charles Sell (RSC) | 进阶 | RSC 出版 + IAO 书单 + Flavour&Fragrance J. 书评 | 从香料到消费品的香料化学系统教科书 |
| Perfumery: Practice and Principles | Calkin & Jellinek | 进阶 | Wiley + 业内「成为职业调香师必读」+ 伟大香水结构剖析 | 实务技法 + 经典香水配方结构分析的桥梁书 |
| The Psychological Basis of Perfumery | Paul Jellinek | 进阶 | Springer + 4 版译编(J.S.Jellinek)+ 长青引用 | 香气-情绪-生理效应的奠基理论(1951) |
| An Introduction to Perfumery | Tony Curtis & David Williams | 入门-进阶 | IAO 科学书单 + 学院常用入门 | 香料工业 + 创作的标准入门教科书 |
| Scent and Chemistry | Ohloff / Pickenhagen / Kraft | 高阶专家 | Wiley-VCH +「香料化学家的圣经」(原德文) | 气味分子-结构-合成的分子级权威 |
| Le Parfum / L'Esthétique en question | Edmond Roudnitska | 高阶专家(法文) | NST「每个学徒必读」+ 学院引用 | 把香水当艺术的美学奠基论(法文一手) |
| 调香术 / 天然香料主成分手册 | 国产编著(中文) | 入门-进阶 | 中文应用型教材(日化香精偏向) | 中文世界少数原创技术教材，偏工艺非艺术(见中英失衡) |

### Popular / Memoir / 评论（必读 4 / 推荐 2）

| 书名 | 作者 | 类型 | Endorsement | 一句话 |
|------|------|------|-------------|--------|
| The Diary of a Nose / Perfume: The Alchemy of Scent | Jean-Claude Ellena | 调香师自述 | Hermès 调香师本人 + IAO 书单 + 多媒体长评 | 当代极简派调香师的创作日记 + 香气世界观 |
| Perfumes: The Guide (2008/2018) | Luca Turin & Tania Sanchez | 评论 | Wikipedia + Guardian 评 +「香水批评作为艺术」共识 | 上千支香水星级评论，确立香水批评文体 |
| The Secret of Scent | Luca Turin | 科普 | TED + Wikipedia + Kirkus 评 | 振动理论 vs 形状理论的嗅觉科学之争(少数派一方) |
| Essence and Alchemy | Mandy Aftel | 历史 / 实务 | IAO 书单 + 16 语种 + Solomon 奖 | 天然香水派的历史 + 实务奠基 |
| The Emperor of Scent / The Perfect Scent | Chandler Burr | 纪实 | IAO 书单(两本)+ NYT 香评人 | 香水业内幕纪实(Turin 之争 / SJP×Ellena 创作) |
| The Perfume Lover | Denyse Beaulieu | 纪实 / 回忆 | 出版社 + Wikipedia + 创作合作纪实 | 一支香水 128 版迭代的创作过程纪实 |

### 参考工具书 / 分类法（必备 2）

| 书名 | 作者 | 类型 | Endorsement | 一句话 |
|------|------|------|-------------|--------|
| Fragrances of the World | Michael Edwards | 年度分类参考 | 业内「香水圣经」+ fragrance wheel 行业标准 | 全球香水按家族分类的年度参考 + 14 家族香轮 |
| Perfume Legends (I/II) | Michael Edwards | 历史 / 解构 | 访谈 150 人 + 香水瓶协会评 | 法系经典香水逐支访谈式解构 |

### 教育 / 认证体系（必看 4 / 推荐 3）

| 机构 / 课程 | 主办 | 格式 | Last_updated | 一句话 |
|------------|------|------|--------------|--------|
| ISIPCA | 凡尔赛(1970, Guerlain) | 2-3 年 MSc / 多课程 | 2026(在招) | 法系香水最权威学府, 教 800 原料 + accord |
| Givaudan Perfumery School | Givaudan(1946, Jean Carles) | 4 年(仅员工) | 2026(在招) | 行业传奇内部学校, 据称培养了市场约 1/3 香水的调香师 |
| GIP (Grasse Institute) | Prodarom(2002) | 18 月 + 6 月实习, 1200h | 2026(在招) | 对外开放(12 人/班)的技术学位, 英文授课, 无需化学背景 |
| Cinquième Sens | Monique Schlienger(1976) | 配方 126h / 嗅觉专家 203h | 2026(在招) | Jean Carles 弟子创办, 开放招生的法系嗅觉教育 |
| PerfumersWorld | Stephen Dowthwaite | 5 日浸入 + 函授 | 2026(在招) | 「ABCs of Perfumery」教学法, 面向全球自学/独立调香 |
| Karen Gilbert Online | Karen Gilbert | 在线 1 年自主进度 | 2026(在招) | 面向 artisan / 独立小众调香师的在线课 |
| 香精公司内部学校(IFF/Symrise/Mane/DSM-Firmenich) | 各公司 | 多年(仅员工) | 2026 | 闭源精英培养, 须先入职方可申请 |

### Core Concepts（28 个）

| 概念 | 一句话定义 | 来源 |
|------|-----------|------|
| Olfactory / fragrance families（嗅觉家族） | 按主导气味把香水归类的分类体系(Floral/Chypre/Fougère/Oriental-Amber/Woody…) | T04-S011, T04-S024 |
| Fragrance wheel（香轮） | Michael Edwards 1992 提出的环形家族分类, 现 14 家族, 零售/教育标准 | T04-S011, T04-S024 |
| Notes pyramid（香调金字塔） | top/heart/base 三层按挥发度组织的结构思维 | T04-S041, T04-S035 |
| Top notes（前调） | 高挥发分子, 喷洒最初数秒-数分钟的第一印象 | T04-S041 |
| Heart notes（中调） | 香水「心脏」, accord 核心, 持续约 2-3 小时 | T04-S041 |
| Base notes（基/后调） | 低挥发分子, 留香最久(8-10h)的骨架 | T04-S041 |
| Accord（和弦） | 5-12 个原料融合成的不可拆分气味单位, 是创作的「单词」, 决定家族归属 | T04-S040 |
| Fixative（定香剂） | 降低整体挥发、延长留香的原料(树脂/麝香/某些 base) | T04-S028, T04-S041 |
| Sillage（香迹/拖尾） | 法语「wake」, 人离开后留在空气中的香气轨迹 | T04-S035(术语), 业内通用 |
| Projection（扩散） | 静止时香气从身体向外辐射的范围(「香气泡」) | 业内通用 + T04-S027 语境 |
| Longevity（留香时长） | 香水在皮肤上可感知的持续时间 | 业内通用 + T04-S028 语境 |
| Volatility / evaporation rate（挥发度） | 原料蒸发速度, 决定其落入 top/heart/base 哪层 | T04-S033(Carles 方法核心) |
| Naturals（天然原料） | 精油/原精/CO2/酊剂等动植物来源香材 | T04-S026, T04-S027 |
| Aroma chemicals（合成香料分子） | 已知结构、稳定、廉价、可定向操控的合成香材 | T04-S027, T04-S043 |
| Captive（专利分子/独占分子） | 香精公司专利、仅供内部使用的独占合成分子(护城河) | T04-S038 |
| Four chemical families（四大化学族） | 香料化学常按结构分类(萜类 terpenoids 为最大族, 含醛/酮/酯/醇等) | T04-S027, T04-S043 |
| Jean Carles method（让·卡尔方法） | 从 base 往 top 自底向上构建 + 系统化原料/accord 记忆训练法 | T04-S033, T04-S004 |
| Coeurs / bases（预制基) | Carles 创的预混 accord 半成品, 提升调香速度与一致性 | T04-S033 |
| The nose / le nez（鼻子） | 对调香师的代称, 也指 tacit 的嗅觉识别与创作能力 | T04-S015, T04-S035 |
| Olfactory memory（嗅觉记忆） | 识记上千原料 + 经典香气的极致 tacit 技能, 学校核心训练目标 | T04-S004, T04-S001 |
| Perfumer's organ / orgue（香风琴） | 半圆阶梯式原料工作台(现多被称重机+电脑取代) | T04-S039 |
| The brief（命题/简报） | 品牌给调香师的创作命题, B2B 创作起点(brief→creation→mods) | T04-S027(以虚拟 brief 贯穿全书) |
| Mods / trials（试样迭代） | 围绕 brief 反复称量-调整的版本迭代 | T04-S031(128 版纪实) |
| Concentration grades（浓度分级） | parfum/EDP/EDT/EDC 按香精在酒精中 % 浓度分级 | 业内通用 + T04-S027 语境 |
| IFRA Standards（法规标准） | 香料安全用量上限(Prohibited/Restricted/Specified 三类), 按消费品类设阈 | T04-S009 |
| Allergen labelling（致敏原标签） | EU 强制标注的香料致敏原(2023/1545 从 26 扩至 80+) | T04-S010 |
| Reformulation（重配） | 因法规(如橡苔/atranol 限用)被迫修改经典配方 | T04-S009, T04-S010 |
| Vibration vs shape theory（振动 vs 形状理论） | 嗅觉机制之争: Turin 振动理论(少数派) vs 主流形状/受体理论 | T04-S019, T04-S020 |

---

## 各 Canon 详述

### 📖 1. Perfume and Flavor Materials of Natural Origin — Steffen Arctander

- **Author**: Steffen Arctander（丹麦化学家）
- **Year**: 1960（多次重印 / 复刻）
- **Type**: 参考工具书（reference）
- **One-liner**: 天然香材的逐条字典 —— 调香师查一个精油 / 原精「从哪来、长什么样、闻起来怎样、怎么用、常见掺假」的第一去处。
- **核心论点 / 内容**: 第一部分讲提取 / 精制工艺；第二部分 500+ 篇天然原料 monograph，每条含来源 / 生产 / 外观 / 气味 - 风味型 / 评估 / 应用 / 可获得性 / 主要成分 / 替代品 / 常见掺假物；附录按香气分类 + 全球产量数据。(evidence: [T04-S026, T04-S022])
- **读完得到什么**: 不是通读，是查阅 —— 建立天然原料的系统认知地图。
- **难度**: 高阶专家（工具书）
- **Endorsement evidence**:
  - `[type: course_syllabus]` IAO 科学 / 技术书单收录 (evidence: [T04-S022])
  - `[type: blog_secondary]` 业内通称「天然原料圣经」(evidence: [T04-S026])
  - `[type: conf_citation]` 多校 / 培训课程作原料参考引用（GIP/ISIPCA 原料模块基石，见 [T04-S003, T04-S001]）
- **可信度**: high ｜ **Decay risk**: low（天然原料知识极稳定）

### 📖 2. The Chemistry of Fragrances — Charles Sell (ed., RSC)

- **Author**: Charles Sell 主编（多作者，均出自 Quest International）
- **Year**: 1st 1999 / 2nd 2006（RSC）
- **Type**: 教科书
- **One-liner**: 从「一个虚拟 brief」出发，把香料化学 + 创作 + 消费者研究 + 毒理 + 电子鼻串成一条线的行业标准化学教科书。
- **核心论点 / 内容**: 香水史 + 天然原料 → 最长一章讲香料分子（尤其萜类 terpenoid）合成 → 围绕虚拟 brief 展开化学家与创意调香师的分工、消费者研究、毒理与电子鼻。(evidence: [T04-S027])
- **读完得到什么**: 理解「香料分子怎么来的、为什么这样设计」，打通化学与创作。
- **难度**: 进阶
- **Endorsement evidence**:
  - `[type: course_syllabus]` IAO 科学书单收录 (evidence: [T04-S022])
  - `[type: blog_secondary]` RSC 官方出版 + Flavour & Fragrance Journal 书评 (evidence: [T04-S027])
  - `[type: conf_citation]` 香料化学课程标准引用
- **替代品 / 互补**: Ohloff《Scent and Chemistry》（更偏分子级、更难）(evidence: [T04-S043])
- **可信度**: high ｜ **Decay risk**: low-medium（合成法会更新，框架稳定）

### 📖 3. Perfumery: Practice and Principles — Robert Calkin & J. Stephan Jellinek

- **Authors**: Robert R. Calkin、J. Stephan Jellinek
- **Year**: 1994（Wiley-Interscience）
- **Type**: 教科书 / 参考
- **One-liner**: 把「实务技法」与「经典香水的结构剖析」放在一本里 —— 想成为职业调香师的桥梁书。
- **核心论点 / 内容**: GC/MS 等分析技术 + 香水开发的美学与技法 + 各国安全法规 + 环境影响 + **对若干世界级伟大香水的结构深度拆解**；兼讲物理 / 化学 / 心理物理学基础。(evidence: [T04-S028])
- **读完得到什么**: 理解一支成品香水「为什么这样搭」，把原料知识升到结构 / 配方层。
- **难度**: 进阶
- **Endorsement evidence**:
  - `[type: blog_secondary]` 业内「成为职业调香师必读」(evidence: [T04-S028])
  - `[type: conf_citation]` Wiley 专业参考 + 学院引用 (evidence: [T04-S028])
  - `[type: course_syllabus]` 与 Curtis & Williams 并列为常见教科书组合（见 [T04-S022] 同类收录）
- **可信度**: high ｜ **Decay risk**: low（结构分析方法长青；法规部分需配 IFRA 最新版）

### 📖 4. The Psychological Basis of Perfumery — Paul Jellinek

- **Author**: Paul Jellinek（4th ed. 由 J. Stephan Jellinek 译编）
- **Year**: 原 1951 / 英译 4th ed. 1997（Blackie / Springer）
- **Type**: 理论奠基著作
- **One-liner**: 把香气与情绪 / 生理效应（如「erogenous」「refreshing」「narcotic」轴）系统理论化的早期奠基作。
- **核心论点 / 内容**: 香气的心理 - 生理效应分类，是「香水为何令人愉悦 / 兴奋」理论思考的源头之一。(evidence: [T04-S029])
- **难度**: 进阶 ｜ **可信度**: high（历史奠基）｜ **Decay risk**: low
- **Endorsement evidence**: Springer 学术出版 + 4 版译编续命 + Flavour & Fragrance Journal 书评 (evidence: [T04-S029]) + 长青引用

### 📖 5. Le Parfum / L'Esthétique en question — Edmond Roudnitska（法文一手）

- **Author**: Edmond Roudnitska（法国大师调香师，Diorissimo / Eau Sauvage 作者）
- **Year**: Le Parfum 1980；L'Esthétique en question（Introduction à une esthétique de l'odorat）
- **Type**: 美学 / 哲学论著（法文）
- **One-liner**: 把香水当成与绘画 / 音乐并列的艺术，从美学高度追问「香水是什么」—— 法系 haute parfumerie 的思想宪法。
- **核心论点**: 区分嗅觉「感知 perception」与「感觉 sensation」、「材料 materials」与「物质 matter」；主张香水是需要法律 / 制度承认的高级艺术。(evidence: [T04-S012, T04-S013])
- **读完得到什么**: 法系「调香师 = 艺术家」世界观的第一手来源；理解极简 / 纯嗅觉美学的根。
- **难度**: 高阶专家（法文，非易读）
- **Endorsement evidence**:
  - `[type: blog_secondary]` Now Smell This：「应是每个训练成为调香师的人的必读」(evidence: [T04-S013])
  - `[type: conf_citation]` Wikipedia 记载其著作影响 + 高级香水法律承认之争 (evidence: [T04-S012])
  - `[type: course_syllabus]` 法系学院（ISIPCA 语境）美学引用基石 (evidence: [T04-S001])
- **中文可得性**: 无成熟中译（中英失衡关键证据）｜ **可信度**: high ｜ **Decay risk**: low

### 📖 6. The Diary of a Nose / Perfume: The Alchemy of Scent — Jean-Claude Ellena

- **Author**: Jean-Claude Ellena（Hermès 专属调香师 2004-2016；Roudnitska 弟子）
- **Year**: Diary of a Nose（Journal d'un parfumeur）2011 / 英 2012；Alchemy of Scent 2011
- **Type**: 调香师自述 / 随笔
- **One-liner**: 当代极简派调香师的「一年创作日记」+ 香气世界观 —— 把 tacit 的「the nose」工作翻译成可读文字。
- **核心论点**: 自称用「嗅觉色彩」写作；强调减法美学（「能用两个原料做出一支香水那天我就收手」）；五感皆入创作。(evidence: [T04-S015, T04-S016])
- **读完得到什么**: 理解当代极简派的创作哲学与日常；是少数有**中译本**的一手著作。
- **难度**: 入门-进阶 ｜ **可信度**: high ｜ **Decay risk**: low
- **Endorsement evidence**:
  - `[type: figure_long]` Hermès 调香师本人长篇自述 + CaFleureBon 长访谈印证哲学 (evidence: [T04-S016])
  - `[type: course_syllabus]` IAO 文化 / 历史书单收录两本 (evidence: [T04-S022])
  - `[type: blog_secondary]` Perfume Society / 多家长评 (evidence: [T04-S015])

### 📖 7. Perfumes: The Guide / The Secret of Scent — Luca Turin & Tania Sanchez

- **Authors**: Luca Turin（生物物理学家）& Tania Sanchez（香评人，二人为夫妻）
- **Year**: The Guide 法版 1992 → 英版 2008 → A–Z 2009 → 全新 2018；The Secret of Scent 2006（Turin 独著）
- **Type**: 评论（The Guide）/ 科普（Secret of Scent）
- **One-liner**: The Guide 以上千支香水的星级短评，确立了「香水批评作为一门艺术」；The Secret of Scent 是嗅觉机制之争（振动 vs 形状）的科普一手。
- **核心论点**:
  - The Guide：开篇讲调香基础，随后逐支 1-5 星 + 署名短评（LT/TS），主张评论本身是更高的艺术。(evidence: [T04-S017, T04-S018])
  - The Secret of Scent：Turin 主张「振动理论」(分子振动决定气味) vs 主流「形状 / 受体理论」。**振动理论是少数派**，2004 Keller-Vosshall 有反驳 —— 保留分歧、不站队。(evidence: [T04-S019, T04-S020])
- **难度**: The Guide 入门-进阶；Secret of Scent 进阶
- **Endorsement evidence**:
  - `[type: blog_secondary]` Guardian「夫妇俩令人眼花缭乱的纲要，真正的乐趣在于为香水批评作为更高艺术辩护」(evidence: [T04-S017])
  - `[type: figure_short]` TED 演讲（Turin 振动理论）(evidence: [T04-S019])
  - `[type: course_syllabus]` IAO 科学书单收录 Secret of Scent (evidence: [T04-S022])
- **可信度**: high（The Guide 评论权威）｜ **争议**: Secret of Scent 的振动理论学界主流不接受，须标 caveat (evidence: [T04-S019]) ｜ **Decay risk**: The Guide medium（逐版更新）/ Secret of Scent low（科学之争格局稳定）

### 📖 8. Essence and Alchemy — Mandy Aftel

- **Author**: Mandy Aftel（artisan 天然调香师，30 年）
- **Year**: 2001 / 2022 修订
- **Type**: 历史 + 实务
- **One-liner**: 天然香水派的奠基读物 —— 把从香料贸易到炼金术的香气史，和天然调香实务（含配方）合一。
- **核心论点 / 内容**: 香水演化的社会 / 形而上脉络（香料贸易→炼金术追寻）+ 天然原料制作实务 + 配方。(evidence: [T04-S021])
- **读完得到什么**: 天然 / artisan 派的历史认同 + 入门实务。
- **难度**: 入门-进阶 ｜ **可信度**: high ｜ **Decay risk**: low
- **Endorsement evidence**:
  - `[type: course_syllabus]` IAO 文化 / 历史书单收录（Aftel 另一本 Fragrant 也在列）(evidence: [T04-S022])
  - `[type: blog_secondary]` 16 语种 + The Sense of Smell Institute 的 Richard B. Solomon 奖 (evidence: [T04-S021])
  - `[type: blog_secondary]` Goodreads 大量读者基数（仅作 endorsement 计数）(evidence: [T04-S042])

### 📖 9. The Emperor of Scent / The Perfect Scent — Chandler Burr

- **Author**: Chandler Burr（前 NYT 香评人）
- **Year**: Emperor 2003；Perfect Scent 2008
- **Type**: 纪实
- **One-liner**: 香水业的两本卧底纪实 —— Emperor 写 Luca Turin 与嗅觉科学之争，Perfect Scent 跟拍两支香水（SJP / Ellena）的诞生。
- **核心论点 / 内容**: Emperor of Scent =「香水与执念的真实故事」（Turin 振动理论之争）；Perfect Scent = 在巴黎 / 纽约香水业一年，跟拍 Sarah Jessica Parker 与 Jean-Claude Ellena 各一支香水从 brief 到上市。(evidence: [T04-S023])
- **读完得到什么**: 外部视角理解香水业的运作、政治与创作现实。
- **难度**: 入门 ｜ **可信度**: medium-high（纪实，有作者立场）｜ **Decay risk**: low
- **Endorsement evidence**:
  - `[type: course_syllabus]` IAO 文化 / 历史书单**同时收录两本** (evidence: [T04-S022])
  - `[type: blog_secondary]` NYT 香评人身份背书 (evidence: [T04-S023])
  - `[type: blog_secondary]` 与 Aftel / Ellena 并列为「入门必读三件套」常见组合 (evidence: [T04-S021, T04-S022])

### 📖 10. Fragrances of the World / Perfume Legends — Michael Edwards

- **Author**: Michael Edwards（香水分类学家 / 历史学家）
- **Year**: Fragrances of the World 年度更新（前身 The Fragrance Manual 1984；fragrance wheel 1992）；Perfume Legends I 1996 / II 后续
- **Type**: 年度分类参考（FotW）/ 历史解构（Legends）
- **One-liner**: FotW 是「全球香水按家族分类」的年度圣经 + 14 家族 fragrance wheel（零售 / 教育行业标准）；Legends 以访谈 150 人逐支解构法系经典。
- **核心论点 / 内容**:
  - fragrance wheel（1992）首创环形家族分类，比旧的线性家系更适合零售导航，解释 14 家族间的关系。(evidence: [T04-S024, T04-S011])
  - Perfume Legends：6 年访谈约 150 位调香师 / 设计师 / 高管 + 私人 / 企业档案，逐支拆解经典。(evidence: [T04-S024, T04-S025])
- **难度**: FotW 参考工具；Legends 进阶 ｜ **可信度**: high ｜ **Decay risk**: FotW high（须年度更新）/ Legends low
- **Endorsement evidence**:
  - `[type: blog_secondary]` 业内通称「香水圣经」+ fragrance wheel 成零售标准 (evidence: [T04-S024])
  - `[type: figure_long]` Fragrantica 长访谈（创作由来）(evidence: [T04-S030])
  - `[type: conf_citation]` 国际香水瓶协会刊评 Perfume Legends II (evidence: [T04-S025])

### 📖 11. The Perfume Lover — Denyse Beaulieu

- **Author**: Denyse Beaulieu（香评人 / 作家）
- **Year**: 2012 ｜ **Type**: 纪实 / 回忆
- **One-liner**: 一支香水（L'Artisan「Séville à l'Aube」）历经 **128 版** 迭代诞生的全过程纪实 —— 把 brief→mods→成品的创作迭代写成故事。
- **核心论点 / 内容**: Beaulieu 把个人记忆（塞维利亚圣周的橙花 + 乳香）交给调香师 Bertrand Duchaufour，记录 128 个版本到成品；穿插香水史与人物。(evidence: [T04-S031, T04-S032])
- **读完得到什么**: 直观感受「mods / trials 迭代」的真实创作节奏。
- **难度**: 入门 ｜ **可信度**: medium-high ｜ **Decay risk**: low
- **Endorsement evidence**:
  - `[type: blog_secondary]` 出版社 / 多家书评 (evidence: [T04-S031])
  - `[type: conf_citation]` Wikipedia 记载创作合作 (evidence: [T04-S032])
  - `[type: blog_secondary]` 与 Burr / Ellena 并列「香水创作纪实」常见推荐

### 📖 12.（历史源头）The Art of Perfumery (1857) — G. W. Septimus Piesse

- **Author**: George William Septimus Piesse（英国化学家 / 调香师 1820-1882）
- **Year**: 1857（多版；1862 版加入通感论）｜ **Type**: 历史奠基（公版）
- **One-liner**: 提取 / 调和方法学的早期奠基书；**首创「notes」概念**（把气味类比音阶 / odophone），是今天「香调」语言的源头。
- **核心论点**: 嗅觉可类比七声音阶；创「odaphone」按八度给气味分级排序 —— notes 概念至今通用。(evidence: [T04-S036, T04-S037])
- **读完得到什么**: 理解「香调 / notes」隐喻的历史由来；公版可免费读（Gutenberg）。**不存全本，仅记录元数据。**
- **难度**: 入门（历史读物）｜ **可信度**: high（一手史料）｜ **Decay risk**: low
- **Endorsement evidence**:
  - `[type: course_syllabus]` IAO 科学书单标为 foundational classic (evidence: [T04-S022])
  - `[type: conf_citation]` Wikipedia 记载 notes 概念发明史 (evidence: [T04-S036])
  - `[type: blog_secondary]` Project Gutenberg 公版收录（长青可得性）(evidence: [T04-S037])

### 🎓 教育 / 认证体系详述

#### 🎓 13. ISIPCA（Institut Supérieur International du Parfum, de la Cosmétique et de l'Aromatique alimentaire）

- **Institution**: 凡尔赛，1970 由 Jean-Jacques Guerlain 创办（1984 起 Versailles 商会接管）
- **Format**: 多学位 / 课程；含英文 MSc Creation & Development of Perfumes, Cosmetics and Flavours（2016 起，与 IFF 合作）
- **Duration**: 2-3 年；学费约 €8,200-€21,200（需理科背景 Bac+2 起）(evidence: [T04-S035])
- **One-liner**: 法系香水最权威学府 —— 教 **800 个原料** + key accords + 香料化学 + 香水史 + 市场 + IFF 实习。(evidence: [T04-S002, T04-S001])
- **关键章节 vs 完整路径**: 完整 MSc 含原料 / 创作 / 化学 / 市场 + 实习；核心价值在原料 + accord 系统训练。
- **Last_updated**: 2026（官网在招）｜ **可信度**: high ｜ **Decay risk**: low（机构长青）
- **Endorsement evidence**: 官方 [T04-S001] + IFF 合办页 [T04-S002] + Nez 教育全景 [T04-S035]

#### 🎓 14. Givaudan Perfumery School

- **Institution**: Givaudan（**Jean Carles 于 1946 在 Roure 创办**，Roure 1991 并入 Givaudan）
- **Format**: 4 年制单一课程，**仅限已被录用为 Givaudan 调香师者**（内部精英培养）
- **Duration**: 4 年；先记忆约 **500 个原料**，含国际实习 + 导师制 + 原料产地考察（普罗旺斯薰衣草 / 摩洛哥含羞草）(evidence: [T04-S004, T04-S035])
- **One-liner**: 行业传奇内部学校 —— 据称培养了市场上**约 1/3 香水**的调香师；教学法至今**部分基于 Jean Carles method**，由 Calice Becker（J'adore 作者）更新主理。(evidence: [T04-S004, T04-S005])
  > 注：「1/3 市场」「Calice Becker 现任校长」「500 原料」「Carles 1946 创办」主要来自 Nez [T04-S035] 与 Givaudan 自述 [T04-S004, T04-S005]；Givaudan 官网原文较简，Perfumer&Flavorist 深度文 [T04-S034] 403 阻断未取全文。数字为**业内估 / 厂商自述**，引用挂 caveat。
- **Last_updated**: 2026（在招；2015 起增设新加坡校区）｜ **可信度**: high（机构）/ 数字 medium ｜ **Decay risk**: low
- **Endorsement evidence**: Givaudan 官方 [T04-S004, T04-S005] + Nez [T04-S035] + Perfumer&Flavorist 标题佐证 [T04-S034]

#### 🎓 15. GIP — Grasse Institute of Perfumery

- **Institution**: Grasse，2002 由 Prodarom 创办
- **Format**: International Technical Degree in Fragrance Creation and Sensory Evaluation，**对外开放**（约 12 人/班）
- **Duration**: 18 个月课程 + 6 个月实习；1,200 培训小时（600h 持证调香师 / 专家授课 + 600h 实操 + 工厂参观）；**英文授课，无需化学背景**；学费约 €12,900 (evidence: [T04-S003, T04-S035])
- **One-liner**: 面向国际、对外开放的技术学位 —— 系统教原料 / accord / 家族识别 / 调和 / GC-MS / 法规 / 功能香精应用。(evidence: [T04-S003])
- **Last_updated**: 2026（在招）｜ **可信度**: high ｜ **Decay risk**: low
- **Endorsement evidence**: 官方 [T04-S003] + Nez [T04-S035]

#### 🎓 16. Cinquième Sens

- **Institution**: 1976 由 Monique Schlienger（**Jean Carles 弟子**、ISIPCA 教授）创办；巴黎 / 迪拜 / 上海 / 巴西
- **Format**: 开放招生（无正式资格门槛）；香水配方 126h / 嗅觉专家 203h 等 (evidence: [T04-S006, T04-S035])
- **One-liner**: Jean Carles 教学血统的对外嗅觉教育 —— 系统训练嗅觉词汇 + 创作入门。
- **Last_updated**: 2026（在招）｜ **可信度**: high ｜ **Decay risk**: low
- **Endorsement evidence**: 官方 [T04-S006] + Fragrance Foundation 课程页（见 manifest 检索）+ Nez [T04-S035]

#### 🎓 17. PerfumersWorld（Stephen Dowthwaite）& Karen Gilbert（独立 / artisan 路径）

- **PerfumersWorld**: Stephen Dowthwaite（1971 入行，UK Picot 实验室受训）；5 日浸入式（30-50 人）+ 函授；**「ABCs of Perfumery」教学法**；累计培训 6,000+ 学员。面向全球自学 / 转行 / 独立调香。(evidence: [T04-S007])
- **Karen Gilbert**: 著《Perfume: The Art & Craft of Fragrance》；在线课程 1 年自主进度，面向 artisan / 独立小众调香师。(evidence: [T04-S008])
- **One-liner**: 不在香精公司体系内、面向独立 / artisan 调香者的可得教育路径（与四大内部学校的闭源精英路径互补）。
- **Last_updated**: 2026（在招）｜ **可信度**: medium-high ｜ **Decay risk**: low
- **Endorsement evidence**: 官方 [T04-S007, T04-S008] + Nez 教育全景 [T04-S035]

#### 🎓 18. 香精公司内部学校（IFF / Symrise / Mane / DSM-Firmenich）

- **One-liner**: 闭源精英培养 —— **须先入职香精公司方可申请**；公开信息稀薄，是行业「公开 canon 无法代表完整知识体」的核心证据。(evidence: [T04-S035])
- **Last_updated**: 2026 ｜ **可信度**: medium（公开信息有限）｜ **Decay risk**: low
- **Endorsement evidence**: Nez 教育全景明确列举各内部学校仅对员工开放 [T04-S035] + Givaudan 例证 [T04-S004]

---

## Phase 2 接口

### ① Canon 反复强调的核心命题（候选心智模型）

跨 ≥3 来源 / 多轨反复出现的 idea：

1. **codifiable 原料 / 结构 ⇄ tacit 嗅觉记忆是这行的第一性张力**。学校先让学徒「记忆 500-800 个原料」（Givaudan 500 / ISIPCA 800）—— 这套是可背诵的；但「成为 the nose」靠的是不可言传的嗅觉记忆与品味。(evidence: [T04-S004, T04-S001, T04-S015]) → **候选核心心智模型**。
2. **Accord 是创作的「单词」**：5-12 个原料融合成不可拆分的气味单位，决定香水家族归属 —— 创作不是堆原料而是搭 accord。(evidence: [T04-S040, T04-S003, T04-S033]) → **候选创作单位心智模型**。
3. **Notes pyramid 的结构思维**：top/heart/base 按挥发度组织 —— Jean Carles method 明确「自底向上」先搭 base 再到 top。挥发度是把原料组织进结构的物理坐标。(evidence: [T04-S041, T04-S033]) → **候选结构思维**。
4. **The brief → creation → mods 的 B2B 创作循环**：香水（尤其商业线）是从品牌命题出发、反复称量迭代（128 版纪实）到成品。(evidence: [T04-S027, T04-S031]) → **候选工作流心智模型**（喂 Track 03）。
5. **法规即创作约束（IFRA / 致敏原 / reformulation）**：经典香水因 IFRA 限用（橡苔 / atranol 等）被迫重配 —— 创作自由 ⇄ 安全合规是结构性张力。(evidence: [T04-S009, T04-S010]) → **候选约束心智模型**。
6. **天然 ⇄ 合成不是优劣而是世界观**：天然（Grasse / 精油 / artisan）vs 合成（aroma chemicals / captives / 顶空）是两套「香水是什么」的世界观，各有奠基文本（Aftel vs Sell/Ohloff）。(evidence: [T04-S021, T04-S027, T04-S038]) → **候选张力轴**。

### ② 奠基人 → 当代代表的谱系线索（供 Track 01 / 智识谱系）

**主干线 A — 方法论谱系（Jean Carles 学派）**：
- 奠基：**Jean Carles**（1892-1966，Roure；Shocking / Miss Dior / Ma Griffe）→ 创「A Method of Creation」+ coeurs 预制基 + 1946 创 Roure/Givaudan 香水学校。(evidence: [T04-S033, T04-S004])
- 传承：Givaudan 学校至今部分用 Carles method，由 **Calice Becker**（J'adore）更新主理；**Monique Schlienger**（Carles 弟子）创 Cinquième Sens。(evidence: [T04-S004, T04-S006])
- → Track 01 figures 候选：Jean Carles、Calice Becker、Monique Schlienger。

**主干线 B — 美学 / 极简谱系（法系艺术派）**：
- 奠基：**Edmond Roudnitska**（Diorissimo 1955 / Eau Sauvage 1966 用 Hedione；著 Le Parfum / L'Esthétique）→ 主张香水是艺术、纯嗅觉极简。(evidence: [T04-S012, T04-S014])
- 传承：其弟子 **Jean-Claude Ellena**（Hermès 2004-16）延续极简（Terre d'Hermès / Jour d'Hermès；「两个原料就停手」）。(evidence: [T04-S015, T04-S016])
- → Track 01 figures 候选：Edmond Roudnitska、Jean-Claude Ellena。

**主干线 C — 分类 / 批评谱系**：
- 分类奠基：**G. W. Septimus Piesse**（1857，notes 概念 / odophone）→ **Michael Edwards**（1992 fragrance wheel / Fragrances of the World / Perfume Legends）。(evidence: [T04-S036, T04-S024])
- 批评奠基：**Luca Turin & Tania Sanchez**（Perfumes: The Guide，确立香水批评文体）+ **Chandler Burr**（业内纪实）。(evidence: [T04-S017, T04-S023])
- → Track 01 figures 候选：Michael Edwards、Luca Turin、Tania Sanchez、Chandler Burr、Mandy Aftel（天然派代表）、Denyse Beaulieu。

**主干线 D — 香料化学谱系**：
- **Paul Jellinek**（心理生理基础 1951）→ **Charles Sell**（RSC 化学）/ **Günther Ohloff**（分子级，原德文）—— 把香水接到有机化学。(evidence: [T04-S029, T04-S027, T04-S043])
- → Track 01 figures 候选 + Track 02 tools（GC-MS、headspace）。

**主要分歧（still-debated within canon）**：
- 嗅觉机制：**振动理论（Turin，少数派）vs 形状 / 受体理论（主流）** —— 保留分歧不站队。(evidence: [T04-S019, T04-S020])
- 天然纯粹派 vs 合成实用派；haute parfumerie / niche 艺术派 vs mass designer 商业派；「鼻子=艺术家」vs「调香师=香气工程师」。(evidence: [T04-S021, T04-S027])

### ③ 中英失衡程度（结构性边界）

- **极度失衡，约 30:1（en+fr : zh 原创一手）**。本 track 进 manifest 的 44 条 source **0 条**为中文原创一手 canon。
- **原创一手 canon 全是英 / 法 / 德文**：Roudnitska（法）、Ellena（法，但有中译）、Jean Carles method（法）、Ohloff（德）、Sell / Calkin&Jellinek / Turin（英）。
- **中文世界的香水文本 = ① 译本（Ellena《香水：气味的炼金术》《调香师日记》有中译）+ ② 少数国产应用型技术教材（《调香术》《天然香料主成分手册》，偏日化香精工艺、非 haute parfumerie 艺术 / 创作）+ ③ KOL / 社区测评二手**。
- **结构性边界**：所有中文原创讨论几乎全部沉淀在**黑名单平台**（知乎 zhuanlan.zhihu.com classify=blacklisted 已剔 / 公众号 / 豆瓣 UGC book.douban.com 被 classifier 误判 verified_primary、按 UGC 性质弃用不引）→ **无法以合规 URL 进 manifest**。这本身就是中英失衡的硬证据：中文一手不是「少」，而是「几乎不存在于可引用的一手形态」。
- **Phase 2.8 诚实边界必写**：「香水 canon 维度中文一手结构性缺失。提炼出的心智模型几乎全部来自英 / 法 / 德文一手 + 法系学院体系；中文使用者面对的是译介 + 应用型工艺教材 + 社区测评，与法系 haute parfumerie 的艺术 / 美学一手之间存在结构性断层。」

### ④ 冷僻信号

- 必读书 **充裕**（核心必读 9 + 工具书 2 + 历史源头 1 = 12 本，远超 floor 3）；**不冷**在 canon 文本维度。
- 课程 / 教育体系 **充裕**（6 个具名学校 / 课程 + 内部学校群，超 floor 2）。
- 核心概念 **28 个**（超 20-30 目标区间下沿，达标）。
- **真正的冷 / 薄在三处**，须 Phase 2.8 标注：
  1. **闭源主导**：核心创作 know-how 在四大公司内部学校 + 调香师脑中，**仅员工可入**（Givaudan/IFF/Symrise/Mane/DSM-Firmenich）→ 公开 canon **不能代表行业完整知识体**。本 track 已用 Surrogate Policy（学校 / IFRA / 调香师自述）堆厚度，但 surrogate 比例高。
  2. **verified_primary = 0**：本行业无 .edu/.gov/arxiv 真命中（香水学院为私立 .fr/.com；无主流学术期刊收录创作 canon）→ 44 条中 surrogate_primary 7 条 + secondary 37 条，**0 条 verified_primary**。这是「专业 / 闭源 / 区域性」冷僻行业的典型签名，**非数据质量问题**。
  3. **中文一手结构性缺失**（见 ③）。
- **Endorsement ≥3 处达标率**：所有 12 本书 / 6 个教育体系均挂 ≥3 endorsement，且每条均含 ≥1 个 `course_syllabus`（IAO 书单 / 学校官方）或 `figure_long`（调香师本人长访谈）→ **一手 endorsement 占比 ≥ 50% 达标**（IAO 书单 + 学校 syllabus + 调香师自述构成主力）。
- **first-hand（verified+surrogate_primary）占比估计 ≈ 16%**（7 surrogate_primary / 44）。**偏低**，但这是 en+fr-primary + 闭源行业的诚实反映：一手创作 canon 是法 / 德文原著（只能挂出版社 secondary 页）+ 闭源学校（已尽量 surrogate 升级）。**须在诚实边界明示 first-hand 占比受 locale + 闭源双重压制**。

---

## 质量自检

- [x] 候选数 ≥ 20（12 书 + 6 教育 + 28 概念，远超）
- [x] 4 类型齐全（book ✅ / 技术教科书 ✅ / course ✅ / concept ✅；paper 维度——香水创作 canon 无学术 paper 传统，已在冷僻信号说明，符合「行业过于工程化 / 闭源」失败处理）
- [x] 每本 book ≥3 endorsement evidence（含 ≥1 syllabus 或 figure_long）
- [x] 每个 course 有 last_updated（均 2026 在招）
- [x] 每个 concept 有「来源」字段
- [x] 一手 endorsement（IAO 书单 / 学校 syllabus / 调香师自述）≥ 50% ✅（但 surrogate_primary URL 占比仅 ~16%，已诚实标注受 locale+闭源压制）
- [x] Phase 2 接口（核心命题 + 谱系 + 中英失衡 + 冷僻信号）已填
- [x] 黑名单泄漏处理（zhihu 剔除；douban/foundry/4160tuesdays 误判弃用）+ source_verifier 合规结论已写
