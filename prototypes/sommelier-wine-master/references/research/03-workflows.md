# Track 03 — Workflows（工作流 / SOP / 方法论）：侍酒师 / 葡萄酒（Sommelier & Wine）

> Phase 1 wave 3 research subagent 输出。行业 = 葡萄酒鉴赏 + 侍酒服务的职业认知 OS。locale = global / **en+fr-primary**。
> 核心张力：**codifiable 理论层 ⇄ tacit 校准层**。本 track 是张力的「落地现场」——工作流恰恰是把 tacit 技能（盲品 / 侍酒 / 配餐）codify 成可走查 SOP 的地方。**最能体现 tacit→codified 的就是盲品演绎：把「这酒尝起来对不对劲」的本能，逼成 sight→nose→palate→结论 的可辩护网格。**
> 范围：8 个核心工作流，每个拆「入门 SOP / 资深路径（跳过·优化·额外）/ 近期变化（AI·新工具·法规·气候）」+ 冷僻自检 + 跨 track 协作 seed。

## Source Manifest

> bucket 规则（照搬前四 track 口径，已逐条跑 `source_verifier.py classify`）：只有 `.edu`/`.gov`/`.ac.uk`/`arxiv.org` 自动判 `verified_primary`（本表命中 arXiv 1 篇）。**认证机构**（wsetglobal.com / mastersommeliers.org / guildsomm.com / mastersofwine.org）→ `surrogate_primary` + note 含 `certification body`。**评论家自有站**（jancisrobinson.com / wineanorak.com / winefolly.com）→ `surrogate_primary` + note 含 `critic own publication`。**工具 / SaaS 厂商页**（coravin.com / wine-searcher.com / cellartracker.com / binwise.com 等）→ `surrogate_primary` + note 含 `vendor docs`。**法定产区 / 监管机构**（inao.gouv.fr / bordeaux.com）→ `surrogate_primary` + note 含 `regulatory body`（verifier 因 host 不在白名单判 secondary，按 Track 06 同口径升级）。trade media（sevenfifty / winespectator / wineenthusiast / vinepair / sommelierbusiness / decanter）+ wikipedia → `secondary`；论坛 / 单帖 → `reference`。
> **verifier 实跑要点（2026-06-06）**：cert body / critic / vendor docs 三类 verifier 默认全判 `secondary`，本表按 manifest 逃生阀人工升 `surrogate_primary` 并加 keyword note（合规，与 Track 01/02/04/05/06 一致）。**特别下调**：`home.binwise.com/blog/...` 与 `guildsomm.com/public_content/...` 被 verifier 误判 `verified_primary`（brand-domain `/blog`、`/public_content` 路径规则误触）——二者实为 vendor docs / 认证机构周边，**人工下调 `surrogate_primary`**（rule 3：绝不标得比真实来源高，与 Track 01 winespecific 同处理）。中文 blacklist（知乎/公众号/百度/CSDN）零进入；dead=0。

| source_id | url | bucket | last_checked | author/host | one-line note |
|-----------|-----|--------|--------------|-------------|---------------|
| T03-S001 | https://www.wsetglobal.com/knowledge-centre/wset-systematic-approach-to-tasting-sat | surrogate_primary | 2026-06-06 | WSET | certification body — SAT 品鉴网格官方页（盲品工作流一手：描述+评质，不强求猜中） |
| T03-S002 | https://www.mastersommeliers.org/wp-content/uploads/2024/03/2024-Deductive-Tasting-Initial-and-Final-Conclusions-KL.pdf | surrogate_primary | 2026-06-06 | CMS Americas | certification body — 2024 deductive tasting grid PDF（演绎盲品工作流一手：sight→nose→palate→initial/final） |
| T03-S003 | https://www.wineenthusiast.com/culture/wine/wine-tasting-grids/ | secondary | 2026-06-06 | Wine Enthusiast | trade media — SAT vs CMS 两套品鉴网格步骤对比（结论阶段差异：评质 vs 演绎到产地） |
| T03-S004 | https://www.jancisrobinson.com/articles/how-and-why-blind-taste | surrogate_primary | 2026-06-06 | Jancis Robinson MW | critic own publication — 盲品方法论长文（资深「先 structure 后产地」演绎口径） |
| T03-S005 | https://www.winearomawheel.com/ | surrogate_primary | 2026-06-06 | Ann C. Noble (InnoVinum) | certification body / method originator — Aroma Wheel（香气逼近子流程，中心→外缘 + 标准物盲闻） |
| T03-S006 | https://www.guildsomm.com/public_content/features/articles/b/guest_writer/posts/decanting | surrogate_primary | 2026-06-06 | GuildSomm | certification body 周边 — 醒酒 / decanting 实操（老酒沉淀 + 双倾倒 double-decant 工作流；verifier 误判 verified，已下调） |
| T03-S007 | https://www.decanter.com/learn/how-to-decant-wine-456358/ | secondary | 2026-06-06 | Decanter | trade media — 醒酒判断与方法（哪些酒需要醒、醒多久高度个案） |
| T03-S008 | https://www.coravin.com/pages/wine-by-the-glass-systems-for-restaurants | surrogate_primary | 2026-06-06 | Coravin | vendor docs — 不开瓶取酒系统（BTG 保存子流程，argon 保护约 4 周为厂商自报） |
| T03-S009 | https://daily.sevenfifty.com/coravin-wine-preservation-systems-are-improving-the-bottom-line-for-restaurants/ | secondary | 2026-06-06 | SevenFifty Daily | trade media — Coravin 改善 BTG 利润的非厂商验证（起泡 BTG 从一两款扩到半打） |
| T03-S010 | https://winefolly.com/wine-pairing/getting-started-with-food-and-wine-pairing/ | surrogate_primary | 2026-06-06 | Madeline Puckette (Wine Folly) | critic own publication — 配餐入门原则（congruent vs complementary，酸/脂/单宁/蛋白交互） |
| T03-S011 | https://www.winewithseth.com/winewiki/food-and-wine-pairing-principles/ | reference | 2026-06-06 | Wine with Seth (WineWiki) | 聚合 wiki — 配餐原则（地配地 / 酸配脂 / 单宁配蛋白 + 危险食材：芦笋/朝鲜蓟/醋） |
| T03-S012 | https://www.wsetglobal.com/qualifications/wset-level-4-diploma-in-wines | surrogate_primary | 2026-06-06 | WSET | certification body — Diploma D1-D6 结构（认证备考工作流：笔试+品鉴+研究论文） |
| T03-S013 | https://www.mastersofwine.org/mw-exam | surrogate_primary | 2026-06-06 | Institute of Masters of Wine | certification body — MW 考试结构（理论5卷+3×12盲品+research paper，世界最难） |
| T03-S014 | https://www.guildsomm.com/learn/study/w/study-wiki | surrogate_primary | 2026-06-06 | GuildSomm | certification body 周边 — compendium / 产区地图 / study wiki（备考事实标准学习底座） |
| T03-S015 | https://www.cellartracker.com/ | surrogate_primary | 2026-06-06 | CellarTracker (Eric LeVine) | vendor docs — 酒窖入库 / 盘点 / 适饮窗 + 众包笔记（酒窖管理工作流核心） |
| T03-S016 | https://home.binwise.com/blog/how-to-price-wine-by-the-glass | surrogate_primary | 2026-06-06 | BinWise | vendor docs — BTG 定价公式 / pour cost（4-5x markup，verifier 误判 verified，已下调） |
| T03-S017 | https://sommelierbusiness.com/en/articles/insights-1/the-economics-of-wine-by-the-glass-programs-456.htm | secondary | 2026-06-06 | Sommelier Business | trade media — BTG 项目经济学（pour cost 20-25%、毛利、周转、配额逻辑） |
| T03-S018 | https://www.wine-searcher.com/ | surrogate_primary | 2026-06-06 | Wine-Searcher | vendor docs — 全球比价 + 均价 + 评分聚合（查价 / 选酒工作流事实标准） |
| T03-S019 | https://www.wineinvestment.com/us/learn/insights/what-is-en-primeur-a-brief-history-of-bordeauxs-wine-futures-system/ | secondary | 2026-06-06 | Cult Wines | trade media — en primeur 期酒机制 + Place de Bordeaux négociant 网络 |
| T03-S020 | https://www.winespectator.com/articles/bordeaux-2025-futures-pricing-and-analysis | secondary | 2026-06-06 | Wine Spectator | trade media — Bordeaux 2025 期酒定价（Cheval Blanc €336 ex-négoce +20%；最小年份34年） |
| T03-S021 | https://en.wikipedia.org/wiki/Three-tier_system_(alcohol_distribution) | secondary | 2026-06-06 | — | 美国三级分销制（producer→distributor→retailer 强制分离，史实/法理） |
| T03-S022 | https://vinepair.com/articles/three-tier-system-explainer/ | secondary | 2026-06-06 | VinePair | trade media — 三级制对侍酒师采购的约束（不能绕开 distributor 直购产地） |
| T03-S023 | https://arxiv.org/abs/2603.12117 | verified_primary | 2026-06-06 | Brach et al. (arXiv) | SommBench（2026-03）— LLM 理论 97%、配餐 MCC 0-0.39、sensory 弱：AI 配餐硬边界 |
| T03-S024 | https://www.restaurantbusinessonline.com/food/ai-vs-sommelier-guests-cru-uncorked-compare-rate-wine-pairings | secondary | 2026-06-06 | Restaurant Business | trade media — Cru Uncorked 实测 AI vs somm 配餐（各半，冷门品种 AI 露怯） |
| T03-S025 | https://www.inao.gouv.fr/en/aop-appellation-origine-protegee | surrogate_primary | 2026-06-06 | INAO (France) | regulatory body — AOC/AOP 定义（采收 / 产地合规工作流的法理底座；verifier 判 secondary 已升级） |
| T03-S026 | https://www.bordeaux.com/us/Our-Terroir/Classifications/Grand-Cru-Classes-en-1855 | surrogate_primary | 2026-06-06 | CIVB Bordeaux | regulatory body — 1855 列级 + Saint-Émilion 重审（酒单叙事 / 估值工作流触发） |
| T03-S027 | https://www.penguinrandomhouse.com/books/201345/secrets-of-the-sommeliers-by-rajat-parr-and-jordan-mackay/ | secondary | 2026-06-06 | Parr + Mackay (Ten Speed) | 出版社页 — Secrets of the Sommeliers（资深选酒「性价比甜点区 / 抢稀缺」实战手艺） |
| T03-S028 | https://www.wineberserkers.com/t/the-myth-of-letting-wines-breathe/118176 | reference | 2026-06-06 | WineBerserkers forum | 论坛长帖 — 「拔塞透气」几乎不增氧（醒酒工作流的内行纠偏，单帖） |

> 跨 track 复用：本 track 的盲品 / 服务 / 学习 framework 与 Track 04 canon 方法节、Track 06 glossary standards 节、Track 02 tools framework 节同源（同一 source family，bucket 口径一致）。本 track 从「**怎么一步步走**」切入；Track 02 从「工具选型」、Track 04 从「读什么」、Track 06 从「术语/标准定义」切入，互补不重复。

---

### 🍷 1. 盲品演绎流程（deductive tasting）— tacit→codified 的核心化身 + 两套方法论之争

> **本行第一性张力的工作流化身**：把「这酒大概是 X」的味觉本能，逼成可走查、可被他人核对的网格。两套主流方法论**共享架构**（appearance→nose→palate→conclusion）但**结论阶段分道**——这是 WSET（知识派）vs CMS（服务派）认识论之争的硬件层。(evidence: [T03-S003], 二手对比 + [T03-S001/S002] 两机构一手)

**入门 SOP（以 CMS deductive grid 走一支红酒，最小完整任务）**
1. **Sight 看**：对白背景倾杯，记 clarity（清/浊）、concentration（色深浅）、color（红：purple/ruby/garnet/tawny —— 越偏砖红越老）、rim variation、黏度（legs，仅提示酒精度，**不提示品质**，见 Track 06 破绽 #3）。
2. **Nose 闻**：先判 clean/faulty（TCA/brett/VA/还原硫——见 Track 06）；再分级 youthful（一级果香/花/草本）vs developed（三级：皮革/蘑菇/烟）；用 **Aroma Wheel 从中心泛类（fruit/spice/floral）向外缘具体词逼近**（见工作流 1b）；判橡木有无 + 新旧。
3. **Palate 品**：按固定顺序逐项给**校准刻度词**（low / medium−/medium/medium+/high）—— sweetness（残糖）→ acid → tannin → alcohol → body → flavor intensity → finish length。**结构必须算出来**（structure calculated），不能停在「好喝」。
4. **Initial conclusion 初判**：用结构线索推 **Old World vs New World + 气候（凉/暖）+ 可能品种**。可操作化逻辑：高酸 + 轻酒体 + 无橡木 + 砖红边 → 凉气候 / 旧世界；高酒精 + 浓果 + 明显橡木 → 暖气候 / 新世界。(evidence: [T03-S002]，呼应 Track 04 playbook)
5. **Final conclusion 终判**：收敛到 **国 / 产区 / 品种 / 年份（酒龄 ±）/ 品质等级**，给出可辩护的理由链。

**资深路径（跳过 / 优化 / 额外）**
- **【优化】网格内化、并行而非串行**：资深把网格背到本能、自动化，腾出脑力真正感知；闻香+品味几乎同时形成假设，而非逐格填空。Jancis 口径：**先抓 structure（酸/单宁/酒体/酒精）这个「骨架」做演绎，香气只作佐证**——因为结构比香气更难伪装、更指向气候/产地。(evidence: [T03-S004])
- **【跳过】跳过低信息步骤**：legs/挂杯、过度纠结具体果香名（樱桃 vs 红醋栗）这类对最终产地判断低权重的步骤被资深快速带过；新手却常卡在「到底是什么果」。
- **【额外】入门看不见的动作**：① 用**反证/排除法**（「若是 X 产区，酸不该这么高 → 排除」）而非正向猜；② 调用**味觉记忆库 + 标志物锚定**（如「这种石油味 = 陈年 Riesling」「这种橡胶还原 = 某些 Syrah」）；③ 估**酒龄而非年份**（看演化程度倒推窗口，而非赌具体年）；④ 现场**追踪杯中演化**（开放 15-30 分钟后香气变化本身是线索）。
- **SAT vs deductive grid 的步骤差异（核心，反例不软化两派分歧）**：**WSET-SAT 的结论 = 先评 quality + readiness to drink，再给 grape/origin/style/production method，重点是「描述 + 评质，不强求猜中」**；**CMS-grid 的结论 = 两段式 initial（旧/新世界+气候+品种）→ final（年份/品种/国/产区/等级），重点是「逻辑演绎到具体身份，猜中是目标」**。(evidence: [T03-S003], 二手对比；[T03-S001/S002] 两机构一手) 选哪套**取决于你考哪个体系 + 目的**：教学/采购评估/写可辩护结论 → SAT；餐厅一线现场识酒/CMS 备考 → deductive grid。**两套并存、哲学分歧真实存在，不强行统一**。

**近期变化（AI / 新工具 / 法规 / 气候）**
- **AI 的硬边界（不软化）**：盲品**没有 AI/app 捷径**。arXiv SommBench（2026-03，verified_primary）：LLM 葡萄酒理论题高达 97%，但 **sensory / 配餐是死穴（配餐 MCC 仅 0-0.39，feature completion 峰值 65%）**——LLM 只从文本学、缺味觉 grounding，无法实时尝酒/评估杯中演化。扫标签查分 App = **反盲品**（盲品的全部意义是不看标签）。专业盲品训练只能靠 SAT/deductive grid + 真酒重复 + Aroma Wheel 词汇校准。(evidence: [T03-S023]，呼应 Track 02 §3)
- **气候变化重写演绎基线**：暖化使「高酒精+浓果=新世界」这类经典初判规则**置信度下降**——旧世界凉气候产区（如勃艮第、德国）近年份酒精/成熟度上升，可能被误判为新世界/暖气候。资深须把「年份气候」纳入演绎、不再死守静态地理刻板印象（呼应 Track 01 Winkler index 气候变化重订 [T01-S025]、Track 06 时效信号）。
- **认证大纲周期更新**：CMS 2024 deductive 格式为当前基准、WSET SAT 骨架稳定但 Diploma 酒单 2024/25 已更——备考者须用最新版网格。**Decay: 网格 low / 演绎基线 medium（气候侵蚀经典规则）**。

---

### 🍷 1b. 香气逼近子流程（Aroma Wheel 词汇校准）— 「闻得到说不出」的解法

> 严格说是盲品 nose 阶段的子流程，但独立成可训练 SOP（Track 02 已列为必备 framework 工具）。把 tacit 嗅觉感知转成 codifiable、可沟通的标准词。(evidence: [T03-S005])

**入门 SOP**：① 闻香 → 从轮盘**中心宽香气族**（fruity / spicy / floral / earthy…）起步；② 向**外缘逐层逼近**到具体词（fruity→citrus→lemon）；③ 落 2-4 个描述词写进 SAT/grid 的 nose 栏。
**资深路径**：**【优化】**跳过中心层、直接落外缘具体词（词汇已内化）；**【额外】**做「**神经训练 / 标准物盲闻**」——把柠檬/杏/香草/丁香/青椒等标准物加进中性基酒盲闻校准，把「词」与「真实分子」绑定（入门只用轮盘认词，不做标准物锚定）。
**近期变化**：轮盘 1984 至今基本未变（科学锚定，**Decay: low**）；官方 8 语含中文，是本行少数有中文一手的工作流工具。

---

### 🍷 2. 侍酒服务流程（floor service）— 点酒到保存的一线 tacit 走查

> 餐厅一线最 tacit 的「桌边手艺」被 codify 成可考核的服务序列（CMS Certified 起含 service 实操考）。**反例不软化贯穿全流程：醒酒/温度/「呼吸」充满被拒厂商话术。**

**入门 SOP（一支需醒的红酒，最小完整服务）**
1. **点酒确认（present）**：向点酒客人正面展示酒标，**口头复述酒庄/年份/产区**，确认是其所点（防开错瓶）。
2. **开瓶（open）**：割箔（胶帽下沿割整齐）→ 螺旋钻入中心 → 双节杠杆分两段起塞 → 检查软木塞气味/完整（判 TCA）。**起泡酒**：手始终压住木塞、瓶口斜 45°、**转瓶不转塞**、让气「叹息」而非「炮响」（防喷+安全）。**老酒**：提前直立静置数小时让沉淀沉底，开瓶动作轻。
3. **判断是否醒酒（decant decision）**：**不是所有酒都醒**（见破绽 #4）。醒两种情形——**老酒去沉淀**（轻倒、借光看瓶肩、见沉淀即停）/ **年轻封闭的高单宁酒增氧**。判错就别醒。(evidence: [T03-S007], 二手；[T03-S006] GuildSomm 实操)
4. **醒酒器 + 温度（decanter + temp）**：需要才倒进**醒酒器**（注意：拔塞「透气」瓶颈面积太小、几乎不增氧，要真醒必须倒进醒酒器——见破绽 #10 / [T03-S028]）；用红外温度计/手感确认 serving temp 落区间。**侍酒温度（约定俗成，各家不同，挂 caveat）**：起泡约 6-9°C / 43-48°F；轻白/芳香白约 7-10°C；饱满橡木白约 10-13°C；干 rosé 约 9-12°C；轻酒体红约 13-16°C；饱满红约 16-18°C（"室温" 是 18 世纪概念、低于现代室温）。(evidence: 区间为 trade 汇编 [winefolly/flask 类]，**约定俗成、各家不同 → caveat**)
5. **试酒（taste pour）**：给点酒主人倒少量（约 30ml）试——**这是查酒是否有缺陷（TCA/氧化），不是"你喜不喜欢"**（口味不对不能退，缺陷才退）。
6. **斟酒顺序（pour order）**：主人示意后，**先女宾后男宾、最后回主人**（旧世界礼仪传统，**fr/欧洲传统、现代部分场所已淡化性别顺序 → caveat**）；倒至杯肚最宽处（红约 1/3，留香空间），瓶口收尾轻转防滴。
7. **BTG / 剩酒保存（preserve）**：开瓶 BTG 用 **Coravin**（针穿木塞 + argon 加压取酒、不开瓶，剩余受 argon 保护**约 4 周**——**vendor 自报，caveat** [T03-S008]）或**充氮塞 / 真空泵**；记录开瓶时间。

**资深路径（跳过 / 优化 / 额外）**
- **【优化】读桌 + 序列流畅**：资深一眼判桌（谁是主人、场合正式度），把"展示-开瓶-试酒-斟酒"做成无停顿的连贯动作；对老酒决定**是否用滗酒篮（cradle）原瓶上桌**而非醒酒器（极老酒经不起折腾，原瓶+缓倒更稳）。
- **【跳过】跳过仪式化冗余**：休闲场所/熟客，资深会**省去全套展示话术、性别斟酒顺序**，直接高效服务——仪式是为体验服务，不是表演。
- **【额外】入门看不见的动作**：① **预判醒酒时机**（资深在客人点单时就决定醒、提前开始，让酒到桌正好；不是等客人催）；② **管理多桌节奏 + BTG 损耗经济**（哪瓶开了要在 N 天内卖完、配 Coravin 还是整瓶开，见工作流 5）；③ **缺陷的边界判断**（轻微 brett/还原是否要换瓶——低量有人爱、高量是 fault，临场拿捏）。
- **反例不软化**：「这支必须醒满 X 小时」「所有酒都要醒」「拔塞让它呼吸就够了」都是**被资深拒绝的话术**——醒多久高度个案、多数酒开瓶即饮、拔塞几乎不增氧。(evidence: [T03-S028]，呼应 Track 06 厂商话术拒绝 + 破绽 #4/#10)

**近期变化（AI / 新工具 / 法规 / 气候）**
- **Coravin 改写 BTG 服务**：非厂商验证（SevenFifty）—— 用 Coravin 的餐厅能把**起泡 BTG 从一两款扩到半打**、显著降损耗、改善利润（含起泡专用 + 螺旋盖适配迭代）。(evidence: [T03-S009])
- **数字酒单 / QR + 平板**：疫情后 contactless + 实时库存同步驱动有真实采用（卖完自动下架），改写"递纸质酒单"环节；但单店 ROI 因店而异（vendor docs 为主，见工作流 5）。
- **AI 桌边助手 = 助手不替代**：trade（Wine Spectator 2025）确认 AI 在推荐侧被多店采用，但**定位 assists not replaces**——AI 读不懂餐桌情绪、不能实时尝酒判缺陷。(evidence: [T03-S024]，呼应 Track 02 §3) **Decay: 服务礼仪 low / BTG 工具 medium**。

---

### 🍷 3. 配餐流程（food pairing）— 从经典原则到反直觉决策

> 把"什么配什么"从玄学 codify 成可推理的交互原则。两条核心策略：**congruent（一致：放大共享风味）vs complementary（互补：用对比求平衡）**。(evidence: [T03-S010], critic own publication)

**入门 SOP（给一道菜选酒，最小完整任务）**
1. **定菜的主导维度**：是脂/油重？酸高（番茄/柠檬腌渍）？甜？辣？咸鲜？蛋白结构（红肉/白肉/海鲜）？
2. **套经典交互原则**（codifiable 锚）：
   - **酸配脂**：高酸酒像"挤柠檬"，切油脂、清口（香槟配炸物、高酸白配奶油）。
   - **酸配酸**：高酸酒配酸食（番茄酱/油醋汁）才不打架——酒酸 ≥ 食酸。
   - **单宁配蛋白 / 脂**：单宁与蛋白和脂结合、被软化——这是"红酒配红肉"的科学基础（Cab 配牛排）。
   - **地配地（"grows together goes together"）**：本地酒配本地菜（Sancerre 配 Crottin 山羊奶酪、Chianti 配番茄红酱）。
   - **甜配甜**：甜酒甜度 ≥ 甜点，否则酒变寡淡（Sauternes 配甜点须更甜）。
   - **congruent vs complementary**：橡木 Chardonnay 配奶油汁 = 一致（质感互相放大）；高酸起泡配咸炸 = 互补对比。
3. **避雷危险食材**（入门必背）：芦笋 / 朝鲜蓟 / 极酸醋 / 大量辣 —— 易让酒发苦/金属感/寡淡（辣放大酒精灼热，配低酒精微甜更稳）。(evidence: [T03-S011], 聚合 wiki)
4. **给 2-3 个安全候选** + 一句体验语言推荐（对客人翻译成"这支酸度活泼、配生蚝很搭"，见 Track 06 register）。

**资深路径（跳过 / 优化 / 额外）**
- **【跳过】跳过查表**：资深不查配餐表——原则已内化成直觉，直接从酒单调取候选。
- **【优化】配"菜的整体"而非单一蛋白**：优化到配**酱汁 / 烹法 / 配菜**（同一块鱼，黄油煎 vs 清蒸配的酒完全不同——酱汁常比主料更决定配酒）。
- **【额外】反直觉配对决策（入门看不见）**：① 经典反直觉——**Sauternes 配 Roquefort 蓝纹**（甜咸对冲）、**红酒配某些鱼**（低单宁红如 Pinot 配金枪鱼/三文鱼，打破"白配鱼"）、**起泡配炸鸡/薯条**（酸+气泡解腻）；② 配"风味桥（flavor bridge）"——找酒与菜共有的香气分子做隐形纽带；③ **故意制造张力**而非一味和谐（资深知道何时用对比创造记忆点，何时求安全）；④ 顾及**整桌多道菜的酒序**（轻→重、干→甜、不可逆），而非单点最优。
- **反例不软化**：配餐没有"唯一正确答案"；"必须红配红/白配鱼"是被资深拒绝的僵化规则——反直觉配对恰是资深价值所在。

**近期变化（AI / 新工具 / 法规 / 气候）**
- **AI 配餐的真实边界（不软化）**：AI 推荐有**有限真采用**（B2B virtual sommelier），但**配餐是 LLM 的核心短板**——arXiv SommBench：配餐 MCC 仅 0-0.39；trade 实测（Restaurant Business：Cru Uncorked AI vs somm）**结果各半、冷门品种 AI 露怯**。AI 能做"安全套路配对"，做不到反直觉/读桌/实时调整。(evidence: [T03-S023, T03-S024]) **结论**：AI 配餐 = 入门脚手架/快速候选，**不是资深决策替代**。
- **无酒精 / no-low 配餐新课题**：ProWein 2026 首设 Zero Tasting Bar，无酒精配餐成新兴 SOP 缺口（呼应 Track 05 topic-heat）。**Decay: 经典原则 low / AI 配餐 high（赛道剧变）**。

---

### 🍷 4. 认证备考工作流（WSET Diploma / CMS / MW）— 入门 SOP 与资深路径分野最大

> 三条认证路径=三种"专业"定义（知识 / 服务 / 研究），备考工作流差异极大（Track 04/06 已埋取向分裂）。

**入门 SOP（以"拿到一个可执业起步证"为最小任务）**
1. **选体系对齐目标**：零售/教育/酒店 → WSET（知识+SAT）；餐厅一线服务 → CMS（服务+演绎盲品）；研究/权威 → MW（学术）。
2. **走阶梯起步级**：WSET L1→L2→L3（L1 全选择、L3 加简答+SAT 品鉴）；CMS Introductory（2 天课+理论考）→ Certified（**含 service 实操考** + 理论 + deductive 盲品三关）。
3. **建三件套学习底座**：① 教材（WSET 教材 / GuildSomm compendium）；② **抽认卡 + spaced repetition**（Anki/Quizlet/Brainscape 记产区/法规/品种海量事实）；③ **盲品网格练到本能 + 产区盲图默画**（见工作流 1、Track 02 §11）。
4. **盲品肌肉训练**：固定酒单、按 grid 走、对答案、复盘——**无捷径，只能真酒重复**。
5. **应试**：理论笔试 + （CMS）现场服务+盲品 + 提交品鉴卷。

**资深路径（跳过 / 优化 / 额外）**
- **【跳过】跳级 + 免前置**：资深常**跳过低阶**（已有 WSET Diploma 可作 MW 前置、直接备 Advanced/MS）；用既有产区知识跳过基础课。
- **【优化】靶向补弱项**：不平均用力，用 Matthew's World（WSET 向）/ GuildSomm Podcast（CMS 向）**靶向补弱项产区**；组**盲品小组 + 找 MS/MW mentor** 校准（个人闭门练易跑偏）。
- **【额外】顶级路径的额外动作（入门完全看不见）**：
  - **WSET Diploma**：D1-D6 六单元（D1 生产/D2 wine business/D3 静止酒主体/D4 起泡/D5 加强/D6 **独立研究论文**）——比起步级多了**商业 + 研究**维度。(evidence: [T03-S012])
  - **CMS Master Sommelier**：理论 + 服务 + 盲品**三关全过**（业内最难考之一，通过率极低、可单关重考累积）。
  - **MW**：理论 5 卷（栽培/酿造与瓶前/处理/wine business/当代议题）+ **3×12 款盲品** + **6000-10000 词 research paper**——公认世界最难葡萄酒考试，全球仅约 300+ MW，多年通过。(evidence: [T03-S013])
- **反例不软化（认证可信度脆弱）**：**CMS-Americas 2018 曝考试舞弊丑闻**（Advanced 盲品试题泄露、撤销当年头衔）——暴露"服务盲品派"认证的脆弱性，如实记录、不为机构洗白（呼应 Track 01 谱系①、Track 04）。

**近期变化（AI / 新工具 / 法规 / 气候）**
- **AI 生成题库/牌组**：抽认卡平台新增 AI 生成牌组/题库，但**质量参差、须自行核对**（呼应 Track 02 §11）；AI 帮记事实，**帮不了盲品感官校准**（SommBench 硬证据）。
- **气候 + 法规改写考纲事实**：WSET 大纲/CMS 格式周期更新（2024/25 已更）；德国 2021 法改产地金字塔、Saint-Émilion 2022 列级重审等**法规变动 → 考纲事实须更新**（呼应 Track 06 时效）。**Decay: 路径结构 low / 考纲事实 medium**。

---

### 🍷 5. 酒窖 / 酒单管理工作流（cellar + wine list + BTG 经济学）

> 从个人藏家入库盘点，到餐厅 wine director 构建酒单 + BTG 项目经济学（定价/周转/配额）。数字密集，**markup/pour cost 必挂 source**。

**入门 SOP（个人藏家 / 小餐厅起步）**
1. **入库录入**：用 **CellarTracker** 扫码/手录每瓶（酒庄/年份/产区/购入价/数量/存位），系统给**适饮窗（drinking window）**估计。(evidence: [T03-S015])
2. **存储校准**：恒温（约 12-14°C）、避光、横放（湿润木塞）、低震动；记录温湿度。
3. **盘点 + 适饮跟踪**：定期对账实物 vs 系统；按适饮窗排"该喝了"清单（避免放过头衰败——见破绽"越老越好"）。
4. **（餐厅）构建基础酒单**：按 BTG + 瓶装分层，覆盖价格带 + 主要风格/产区，标注与菜单的配餐逻辑。
5. **（餐厅）BTG 定价**：用公式——**批发瓶价 × markup(约 4-5x) ÷ 每瓶标准杯数（750ml 约 4-5 杯/5-6oz）**；目标 **pour cost 约 20-25%**（即 4-5x 回报）。(evidence: [T03-S016] vendor docs + [T03-S017] trade，**markup/pour cost 为行业常用基准、各店不同 → 挂 source + caveat**)

**资深路径（跳过 / 优化 / 额外）**
- **【优化】graduated pricing（阶梯加价）**：资深**不用统一 markup**——低价酒高倍率、高价酒低倍率（让贵酒更易卖、保整体毛利）；并加 **15-25% waste buffer** 覆盖开瓶卖不完/过倒。(evidence: [T03-S017])
- **【跳过】跳过手工 Excel**：用 BinWise/InVintory 类 SaaS + POS 集成，卖完自动下架（降低 "86 list" 错误：卖完还在单上），跳过人工同步。
- **【额外】wine director 的额外动作（入门看不见）**：① **周转/库存经济**——盯哪些 SKU 压资金/动不动，调整采购；② **BTG vs 整瓶决策 + Coravin 经济**（高价稀有酒上 BTG 靠 Coravin 取酒、不牺牲整瓶，扩客单价）；③ **配额 allocation 管理**——膜拜酒/抢手货厂商按历史采购量配额，资深维护与 distributor/进口商关系争配额（见工作流 6）；④ **酒单叙事 + by-the-glass 轮换**（讲产区故事、季节性换 BTG 制造新鲜感）；⑤ **毛利结构对比**——BTG 毛利（约 75-80%）远高于整瓶（约 35%），但损耗风险也高，资深平衡两者。(evidence: [T03-S017]，**毛利/pour cost 数字为 trade 基准、各店差异大 → caveat**)

**近期变化（AI / 新工具 / 法规 / 气候）**
- **数字酒单 + SaaS + AI cellar assistant**：实时库存同步、AI 配餐建议模块（InVintory 等）——但**采用数为厂商自报（vendor docs）、单店 ROI 因店而异**（呼应 Track 02 §3/§4 避坑：别把 SaaS"数千家在用"当事实）。
- **列级重审 → 酒单/估值工作流变**：Saint-Émilion 每约 10 年重审（2022 多家退出）→ 改变酒庄等级 → 影响选酒叙事与定价（呼应 Track 06 [T06-S017]）。
- **气候 → 适饮窗 + 采购重估**：暖年份酒成熟更快、适饮窗可能前移，藏家须重估窖藏曲线。**Decay: 存储原则 low / SaaS+定价 medium / 列级触发 high（Saint-Émilion）**。

---

### 🍷 6. 采购 / 查价 / 选酒工作流（Wine-Searcher + en primeur + 三级分销约束）

> 买手/somm 的选酒决策：比价 → 期酒决策 → 在美国**三级分销制**约束下采购。**期酒/三级制数字挂 source。**

**入门 SOP（选并采购一支酒，最小完整任务）**
1. **查价 + 识酒**：用 **Wine-Searcher** 查全球零售报价、历史均价、产区资料、评分聚合——判"这支贵不贵 / 大概什么水平"。(evidence: [T03-S018])
2. **判品质（看"谁打分"而非裸分）**：**不看聚合裸分**（摊平了评论家个体偏好）——查具体评论家长稿（Jancis 20 分制 / Vinous）+ 看其风格偏好是否与你客群匹配（呼应 Track 02 避坑、Track 06 厂商话术拒绝）。
3. **走合规采购渠道**：在美国，**餐厅/零售必须经持牌 distributor 采购**，不能绕开直购酒庄（三级制：producer/importer→distributor→retailer 强制分离）。联系 distributor 报价、下单。(evidence: [T03-S021, T03-S022])
4. **记录入库**（接工作流 5）。

**资深路径（跳过 / 优化 / 额外）**
- **【优化】多渠道比价 + 关系**：资深用 Wine-Searcher Pro（全部报价/历史价）+ **Liv-ex 验"作为资产"的真实 B2B 成交价**（精品酒）；并直接用**与多家 distributor/进口商的关系**拿更好价/抢配额，而非只看挂牌价。
- **【跳过】跳过零售比价**：对配额制膜拜酒/期酒，资深跳过常规比价——**靠 allocation（历史采购量决定能买多少）**，价不是主要变量、能不能拿到货才是。
- **【额外】en primeur（期酒）决策（入门完全看不见）**：
  - **机制**：顶级波尔多在采收次年春"Primeurs week"放桶样给评论家/négociant 试 → 分批（tranches）放价 → 经 **Place de Bordeaux négociant 网络**配货 → 付钱锁货、**18-24 个月后装瓶交割**。(evidence: [T03-S019])
  - **资深决策维度**：年份质量（评论家桶样分）× 放价 vs 历史 vs 二级市场预期 × 是否真"现在买更便宜"（很多年份装瓶后未涨、期酒不划算）× 配额/关系。**2025 例（挂 source）**：Cheval Blanc 2025 期酒 €336/瓶 ex-négoce（**+20%**）、美国零售约 $473/瓶（弱美元放大）；2025 是**34 年来最小年份**，但"除铁杆藏家外对更贵波尔多兴趣寥寥"——资深据此判多数酒**期酒不值得追**。(evidence: [T03-S020], trade，**价格为厂商放价/单一年份、市场判断为评论口径 → caveat**)
  - **三级制 + DTC 约束**：资深须懂各州 DTC（直邮消费者）法规差异、进口商独家代理关系——决定能采到什么、走什么渠道。
- **反例不软化**：「这支投资酒稳赚/保证升值」「越陈越值钱」是**诈骗高发话术**——二级市场波动且充满 fraud（伪造产地/超收/假瓶），期酒也可能套牢。(evidence: 呼应 Track 06 [T06-S033] 投资骗局)

**近期变化（AI / 新工具 / 法规 / 气候）**
- **精品酒市场触底回升**：Liv-ex 100 在 2025末-2026初连续 6 个月上涨、香槟领涨、勃艮第占交易额 31.8%（**平台自报指数 → caveat**）——改写买手对"现在该不该囤"的判断（呼应 Track 05 topic-heat）。
- **气候 → 年份策略 + en primeur 逻辑**：极端年份（霜冻/热浪）使产量波动加剧（2025 最小年份），期酒的"稀缺溢价 vs 真实质量"判断更难；产区边界/适种品种随暖化变（呼应 Winkler 重订）。
- **三级制改革压力**：DTC 配送法规持续博弈（各州松紧不一）——长期可能松动采购约束，但当前仍是硬约束。**Decay: 三级制法理 low / 期酒价格 high（逐年）/ 市场指数 high**。

---

### 🍷 7. 酿造决策工作流（malolactic 控制 / 采收时机 / 自然酒低干预）—（偏酿造端，侍酒师须懂以解码风格）

> 偏生产端（非侍酒师日常操作），但侍酒师/盲品者**须懂这些决策如何塑造杯中风格**，且它们是"干预 vs 放手"张力的工作流化身（Track 04 谱系③⑤）。**三条路线对立，不调和。**

**入门 SOP（理解一个酿造决策的最小框架）**
1. **采收时机（harvest timing）**：测 brix（糖度→潜在酒精）+ 尝酚类成熟度 + 看酸 → 定采收日。早采 = 高酸/低酒精/鲜爽；晚采 = 高糖/高酒精/熟果。
2. **malolactic（MLF，苹乳发酵）决策**：要奶油质感/降酸/稳定 → **走 MLF**（接种乳酸菌，苹果酸→乳酸，pH↑0.1-0.3）；要保尖锐果酸/新鲜 → **抑制 MLF**（低温/加 SO₂/过滤除菌）。（Peynaud 范式：把曾被当"病"的 MLF 变成可主动控制的过程，见 Track 01/04）
3. **干预程度（SO₂/酵母/下胶过滤）**：技术派——商业酵母 + 控温 + 下胶过滤 + 足量 SO₂（清洁、可复现）。

**资深路径（跳过 / 优化 / 额外）**
- **经典平衡派（Parr / IPOB）**：**【额外】"每年看能多早采收"**追更低酒精/更鲜酸/更纯净——反 fruit bomb（与浓郁现代派对立）。(evidence: 呼应 Track 01 [T01-S034/S035])
- **现代主义/技术派（Peynaud 谱系 + UC Davis）**：**【优化】**精准控温发酵、micro-oxygenation 软单宁、靶向 MLF——清洁科学、品质可复现。
- **自然酒 / 低干预派（Legeron / Joly）**：**【跳过 = 故意省略全部添加】"不加不减"**——原生酵母、**无添加 SO₂、不下胶、不过滤、不加酶**；生物动力种植为前提（月相/配制剂，Steiner 学说）。这是对技术派 SOP 的**正面对立**（"额外"在他们看是"污染"）。(evidence: 呼应 Track 01 [T01-S041/S044]、Track 04 谱系③)
- **反例不软化（争议真实）**：① 自然酒**无官方定义、缺陷酒（VA/brett/还原/再发酵）常被美化**为"个性"——科学派（Goode/Lewin）实打实质疑；② 生物动力的"宇宙能量"解释**未被科学接受**（其有机农艺效果与玄学解释须分开看）；③ IPOB"平衡"也被批为**另一种风格教条**（把低酒精道德化），已约 2016 解散；④ Peynaud 范式被讥"Peynaudization 同质化"。**四派批评并存，不替任一方洗白**（呼应 Track 01 五大谱系）。

**近期变化（AI / 新工具 / 法规 / 气候）**
- **气候变化重写采收窗口（最核心）**：暖化使糖分先于酚类成熟（"采收悖论"：等酚类熟则糖太高/酒精爆表，按糖采则单宁青涩）——资深重订采收策略（更早采、夜采、选凉地块/高海拔、换抗热品种）。直接侵蚀经典采收 SOP。
- **AI 生产侧有真用例**：arXiv 2025 综述——AI 在产量预测/病害监测/发酵控制有真实应用（**生产侧，非侍酒侧**，呼应 Track 02 §13）。
- **自然酒主流化 + 认证空白**：RAW WINE 全球扩张推动低干预常态化，但"自然酒"仍无统一法定定义（监管空白）。**Decay: MLF/采收原理 low / 采收窗口 medium-high（气候）/ 自然酒定义 medium（仍在演化）**。

---

### 冷僻 / 信号薄弱（→ Phase 2.8 诚实边界）

- **workflow 数 = 8（含 1b 子流程则 8）≥ 6 ✅**：盲品演绎 / 香气逼近子流程 / 侍酒服务 / 配餐 / 认证备考 / 酒窖+酒单 / 采购查价 / 酿造决策。每个含"入门 SOP + 资深路径（跳过·优化·额外≥2 类）+ 近期变化"三段 ✅。**source = 28 ≥ 18 ✅。不触发冷僻协议。**
- **bucket 现实（与前四 track 同构的结构性事实）**：**verified_primary 仅 1**（arXiv SommBench）。工作流权威 = 认证机构（cert body）+ 评论家站（critic）+ 工具厂商（vendor docs）+ 法定产区（regulatory body）—— **几乎不在 .edu/.gov**，verified_primary 占比低是行业结构性事实，非偷工。所有 cert/critic/vendor/regulatory 已诚实标 surrogate_primary + keyword note；binwise/guildsomm 被 verifier 误判 verified 的两条已**人工下调**（rule 3）。
- **中英失衡（与全行一致，头号诚实边界）**：工作流方法论 **en+fr-primary**——CMS/WSET/MW 的盲品 + 服务 + 备考 SOP 为英文一手；旧世界侍酒礼仪（斟酒顺序/醒酒/起泡开瓶）有法文/欧洲传统；en primeur / Place de Bordeaux 是法国体系。**中文一手工作流稀薄**：中文圈以 WSET 中国培训转述 + 公众号二手 SOP 为主（黑名单生态，不作工作流真伪来源），**无中文原创的盲品/服务/备考方法论**。Aroma Wheel 有官方中文版是少数例外。SKILL.md「工作流」节须明说"核心 SOP en+fr-primary，中文用户须接受方法论无中文一手"。
- **数字 caveat 已逐条挂**：侍酒温度区间（约定俗成/各家不同）、Coravin argon 约 4 周（vendor 自报）、BTG markup 4-5x / pour cost 20-25% / waste buffer 15-25% / 毛利 75-80%（trade 基准/各店不同）、Cheval Blanc 2025 €336 +20% / 34 年最小年份（厂商放价/单一年份/评论口径）、Liv-ex 指数（平台自报）、斟酒性别顺序（欧洲传统/已淡化）—— 均挂 source_id 或 caveat。
- **未深挖缺口（诚实标，非"不存在"）**：① **旧世界本土语种一手 SOP**（法 AOC cahier des charges 原文采收规则、意 DOCG disciplinare）未逐条爬取——本 track 服务/盲品 SOP 偏英美认证体系视角，对法/意/西本土酿造与服务一手覆盖薄（与 Track 04 一致缺口，Phase 1.5 可补）。② **酒厂实验室/栽培测量工作流**（折光仪/酚类分析/发酵曲线）刻意未深入——本 track 聚焦侍酒/品鉴/学习/采购侧，酿造决策（工作流 7）只到"侍酒师须懂以解码风格"的程度。③ SevenFifty BTG-economics 深稿 gated（403），BTG 数字以 sommelierbusiness + binwise + 通用 trade 基准交叉，未取到该单篇全文。

---

## 与其他 Track 的协作 seed

- **→ Track 01 figures**：工作流的方法论奠基人/代表——盲品两派（**WSET 知识派 vs CMS 服务派 Dalton/Parr**）/ **Ann Noble**（Aroma Wheel 词汇校准流程发明者）/ **Peynaud**（MLF 控制范式）/ **Parr·IPOB**（采收求平衡）/ **Legeron·Joly**（自然酒"不加不减"流程，与技术派对立）/ **Jancis**（"先 structure 后产地"盲品演绎口径）。每条工作流的"资深路径/争议"直接对应某 figure 的思维 DNA。
- **→ Track 02 tools**：工作流挂工具——盲品（SAT 网格/deductive grid/Aroma Wheel）/ 服务（侍酒刀/醒酒器/侍酒温度计/Coravin/充氮塞）/ 酒窖（CellarTracker/InVintory）/ 酒单（BinWise+POS/数字酒单）/ 查价（Wine-Searcher/Liv-ex）/ 备考（抽认卡/产区盲图）。本 track 给"怎么一步步用"，Track 02 给"选型与避坑"。
- **→ Track 04 canon**：工作流的理论底座——盲品演绎↔SAT/deductive grid 方法节；MLF/采收↔Peynaud《Knowing and Making Wine》;自然酒流程↔Legeron《Natural Wine》;配餐/选酒↔《Secrets of the Sommeliers》;认证路径↔WSET/CMS/MW 四柱。
- **→ Track 05 sources / Track 06 glossary**：stay-current（资深用 GuildSomm/Jancis/Liv-ex 跟体系与市场，改写采购/备考工作流）；术语（盲品 register、SAT/grid standards、三级制/en primeur/AOC 法规、厂商话术拒绝）直接是工作流的执行语言与纠偏点。
- **→ Phase 2.8 诚实边界（三点落地，与前四 track 共识）**：① **中英失衡**——工作流 en+fr-primary，无中文原创 SOP；② **verified_primary = 1**——工作流权威在 cert body+critic+vendor+regulatory，非 .edu/.gov，结构性偏低非偷工；③ **AI 边界 + 反例不软化已落地**——AI 配餐/盲品有 SommBench 硬证据证明不能替代人；醒酒/温度/期酒/自然酒/CMS 舞弊/IPOB 解散等负面均如实记录，未洗白。
- **一致性检查**：本 track 与 Track 02（framework 工具同源）、Track 04（方法节同源）、Track 06（SAT/grid standards + 厂商话术拒绝 + 时效信号同源）bucket 口径完全一致。若 Phase 1.5 补旧世界本土语种一手 SOP，可丰富侍酒礼仪/采收合规的法/意/西维度——但不改变"核心工作流 en+fr-primary、中文一手稀薄"的结构性结论。

## Agentic Protocol seed（→ synthesis：这行人拿到新问题按什么维度做功课）

> 喂给 Phase 2 的"行业方法论内核"——侍酒师/葡萄酒从业者面对任意新问题（一支陌生酒 / 一道难配的菜 / 一个采购决策 / 一个"该不该信"的说法）时，资深人按以下维度系统做功课：

1. **先定位地理（terroir-first）**：旧世界尤其——先问"国→产区→子产区→地块"，再谈品种/风格。地理是第一性问题（呼应 Track 04 候选心智模型①）。
2. **走结构化网格、用刻度词而非情绪词**：任何品鉴/判断都按 sight→nose→palate→结论（或 SAT 评质 / deductive 演绎）逐项给校准刻度，把 tacit 感受逼成可辩护、可被他人核对的书面结论。
3. **先抓 structure（骨架）再抓香气（血肉）做演绎**：酸/单宁/酒体/酒精比香气更难伪装、更指向气候/产地——资深从结构反推，用排除法而非正向猜。
4. **每个决策定位在张力轴上**：干预 vs 放手（酿造）/ 描述评质 vs 演绎识别（盲品）/ 量化通约 vs 风土表达（评分）/ congruent vs complementary（配餐）/ 仪式 vs 高效（服务）——先认清自己站哪、对立面是什么。
5. **看"谁打分/谁说的 + 什么偏好"，不看裸分/裸结论**：分数是评论家特定时点的主观印象、不可跨人通约；判信源先判其 bucket 与利益位置（评论独立性 / vendor 话术 / 投资骗局）。
6. **数字必挂来源或 caveat**：醒酒时间/侍酒温度/markup/配额/期酒涨幅都是"约定俗成 or 各家不同 or 单一口径"——never 当客观真理写死。
7. **挂 source + 警惕厂商话术**：遇到"必须醒 X 小时 / 自然酒不上头 / sulfites 致头疼 / 投资酒稳赚 / 越老越好"——默认是被资深拒绝的错位包装，回到机理（Track 06 破绽清单）。
8. **AI 是助手不是替代（认清边界）**：查询/推荐/运营/生产侧 AI 有真用；**盲品/桌边判断/反直觉配餐 = sensory grounding 死穴**（SommBench 硬证据），不能外包给 AI。
9. **把"近期变化"纳入**：气候（采收窗口/适饮窗/演绎基线）、法规（列级重审/产地法改）、市场（Liv-ex 指数/期酒）、工具（Coravin/数字酒单）——静态知识会被这四条侵蚀，资深持续重校准。
10. **承认 tacit 层无捷径**：盲品/服务/配餐的校准层只能靠真酒+重复+mentor 校准——理论可读，手艺必须练，两层不可互相替代（行业第一性张力的操作结论）。
