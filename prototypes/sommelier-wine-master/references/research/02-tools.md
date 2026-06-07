# Track 02 — Tools（工具地图）：侍酒师 / 葡萄酒（Sommelier & Wine）

> Phase 1 wave 2 research subagent 输出。行业 = 葡萄酒鉴赏 + 侍酒服务的职业认知 OS（从业者 / 侍酒师 / 学习者视角）。locale = global / en+fr-primary。
> 核心张力：**codifiable 理论层 ⇄ tacit 校准层**。本行「工具」横跨三类——① **方法论框架工具**（品鉴网格 SAT / 演绎网格 deductive grid / 香气轮 aroma wheel / 气候分类 Winkler index）；② **软件 / 平台**（查价 Wine-Searcher、酒窖管理 CellarTracker、餐厅酒单 SaaS、投资数据 Liv-ex）；③ **物理 / 测量工具**（侍酒刀 / 醒酒器 / 侍酒温度计 / Coravin 取酒系统）。
> **中英失衡（贯穿全文，Phase 2.8 用）**：工具生态几乎全 en-primary，少数 framework 工具有官方多语版（如 Aroma Wheel 8 语含中文）。中文一手工具文档稀薄；查价 / 酒窖 / 酒单 SaaS 的中文等价物未在专业语境形成事实标准。本 track source 中英比 ≈ all-en（中文 blacklist 零进入）。

---

## Source Manifest

> bucket 规则提醒：`source_verifier.py classify` 自动只把 `.edu`/`.gov`/`.ac.uk`/`arxiv.org` 判 `verified_primary`（本表命中 3 个：UC Davis V&E `.edu` + 2 篇 arXiv）。**认证机构 / 方法 originator**（wsetglobal.com / mastersommeliers.org / guildsomm.com / winearomawheel.com）→ `surrogate_primary` + note 含 `certification body`。**评论家自有站**（jancisrobinson.com）→ `surrogate_primary` + note 含 `critic own publication`。**纯商业 SaaS / 工具厂商页**（cellartracker / wine-searcher / vivino / liv-ex / coravin / binwise / invintory / preferabli / eprovenance / atelierduvin）→ **诚实标 `surrogate_primary`** + note **必含 `vendor docs`**（厂商自有文档，非中立一手，不冒充 verified_primary，也不因是厂商而丢弃）。trade media（SevenFifty / Wine Spectator / Wine Enthusiast / Restaurant Business）+ Cambridge Core 期刊 + wikipedia → `secondary`。论坛 / 单帖 → `reference`。
> **source_verifier scan 已跑（2026-06-06）**：所有 URL 跑过 classify。verified_primary 自动命中 = UC Davis `.edu` + arXiv 2 篇；surrogate_primary 为 manifest 人工升级（verifier 默认给 secondary，逃生阀合规——cert body / critic / vendor docs 三类逃生阀均按 prompt 规则加 note）。blacklisted=0（无知乎/公众号/百度/CSDN/G2/Capterra/PR 通稿泄漏）、dead=0。

| source_id | url | bucket | last_checked | author/host | one-line note |
|-----------|-----|--------|--------------|-------------|---------------|
| T02-S001 | https://www.wsetglobal.com/knowledge-centre/wset-systematic-approach-to-tasting-sat | surrogate_primary | 2026-06-06 | WSET | certification body — SAT 系统化品鉴网格官方页（必备 framework 工具一手） |
| T02-S002 | https://www.mastersommeliers.org/wp-content/uploads/2024/03/2024-Deductive-Tasting-Initial-and-Final-Conclusions-KL.pdf | surrogate_primary | 2026-06-06 | CMS Americas | certification body — deductive tasting grid 官方 PDF（演绎法工具一手） |
| T02-S003 | https://www.winearomawheel.com/ | surrogate_primary | 2026-06-06 | Ann C. Noble (InnoVinum) | certification body / method originator — Wine Aroma Wheel 官方站（1984 originator，标准化香气词汇工具） |
| T02-S004 | https://www.guildsomm.com/learn/study/w/study-wiki | surrogate_primary | 2026-06-06 | GuildSomm International | certification body 周边 — study wiki / compendium / 产区地图，备考事实标准学习工具 |
| T02-S005 | https://www.wine-searcher.com/ | surrogate_primary | 2026-06-06 | Wine-Searcher | vendor docs — 全球比价 + 均价 + 评分聚合引擎，事实标准查价工具 |
| T02-S006 | https://www.cellartracker.com/ | surrogate_primary | 2026-06-06 | CellarTracker (Eric LeVine) | vendor docs — 全球最大众包品鉴笔记 + 酒窖 / 库存管理，与 Jancis 集成 |
| T02-S007 | https://www.liv-ex.com/ | surrogate_primary | 2026-06-06 | Liv-ex | vendor docs — 精品酒二级市场价格指数（Fine Wine 100/50），投资 / 交易侧工具 |
| T02-S008 | https://www.vivino.com/ | surrogate_primary | 2026-06-06 | Vivino | vendor docs — 扫标签查均分大众 App（亿级样本，专业信噪比低，见避坑节） |
| T02-S009 | https://www.coravin.com/pages/wine-by-the-glass-systems-for-restaurants | surrogate_primary | 2026-06-06 | Coravin | vendor docs — 针穿木塞 + argon 取酒系统，BTG 不开瓶取酒（餐厅产品页） |
| T02-S010 | https://home.binwise.com/ | surrogate_primary | 2026-06-06 | BinWise | vendor docs — 餐厅酒单 / 饮品库存 SaaS（50+ POS 集成），wine director 向（/blog/wine-program 详述） |
| T02-S011 | https://invintory.com/ | surrogate_primary | 2026-06-06 | InVintory | vendor docs — 高端数字酒窖管理 + AI cellar assistant（含 AI 配餐建议，需 caveat） |
| T02-S012 | https://preferabli.com/ | surrogate_primary | 2026-06-06 | Preferabli | vendor docs — B2B AI 口味推荐 / virtual sommelier（采用证据见 §3，自报需 caveat） |
| T02-S013 | https://www.eprovenance.com/ | surrogate_primary | 2026-06-06 | eProvenance (Eric Vogt) | vendor docs — RFID/NFC 温度监测 + 区块链溯源（fine wine provenance，验证度见 §3） |
| T02-S014 | https://us.atelierduvin.com/product-category/wine-tools/ | surrogate_primary | 2026-06-06 | L'Atelier du Vin (FR) | vendor docs — 法国侍酒物理工具厂（侍酒刀 / 醒酒器 / 品鉴套装），fr-primary 物理工具 |
| T02-S015 | https://wineserver.ucdavis.edu/ | verified_primary | 2026-06-06 | UC Davis V&E Dept | 学院派 ground truth（.edu）— Winkler index / 20-point scale / Aroma Wheel 发源地 |
| T02-S016 | https://arxiv.org/abs/2603.12117 | verified_primary | 2026-06-06 | Brach et al. (arXiv) | SommBench（2026-03）— LLM 葡萄酒理论 97%、配餐 MCC 0-0.39，sensory 弱：AI 不能替代盲品的硬证据 |
| T02-S017 | https://arxiv.org/abs/2507.21098 | verified_primary | 2026-06-06 | arXiv (AI for wine industry) | AI 驱动栽培 / 酿造 / 酒旅管理综述（2025-07）— AI 在生产 / 运营侧的真实用例 vs 品鉴侧 |
| T02-S018 | https://daily.sevenfifty.com/coravin-wine-preservation-systems-are-improving-the-bottom-line-for-restaurants/ | secondary | 2026-06-06 | SevenFifty Daily | trade media — Coravin 改善餐厅 BTG 利润的非厂商验证（从一两款扩到半打起泡） |
| T02-S019 | https://www.winespectator.com/articles/ai-impact-restaurants-wine-sommeliers-diners-2025 | secondary | 2026-06-06 | Wine Spectator | trade media — 2025 AI 对侍酒 / 酒单影响（assists not replaces，emerging 验证锚） |
| T02-S020 | https://www.restaurantbusinessonline.com/food/ai-vs-sommelier-guests-cru-uncorked-compare-rate-wine-pairings | secondary | 2026-06-06 | Restaurant Business | trade media — Cru Uncorked 实测 AI vs somm 配餐（结果各半，冷门品种 AI 露怯） |
| T02-S021 | https://www.wineenthusiast.com/culture/wine/blockchain-wine-fraud/ | secondary | 2026-06-06 | Wine Enthusiast | trade media — 区块链防伪现实评估（潜力 vs 采用差距，去营销化） |
| T02-S022 | https://www.cambridge.org/core/journals/journal-of-wine-economics/article/crowdsourcing-the-assessment-of-wine-quality-vivino-ratings-professional-critics-and-the-weather/FE61BAFB8D167CD960BB260777189231 | secondary | 2026-06-06 | Journal of Wine Economics (Cambridge) | 学术 — Vivino 均分与专业评分相关但更弱（业余重即时愉悦，专业看陈年潜力） |
| T02-S023 | https://en.wikipedia.org/wiki/Vintages_climate_classification | secondary | 2026-06-06 | — | Winkler index / GDD（生长度日）气候区 I-V 分类法（术语 / 史实备份） |
| T02-S024 | https://www.brainscape.com/subjects/guild-of-sommelier | secondary | 2026-06-06 | Brainscape | trade educator — 备考抽认卡平台（spaced repetition），与 Quizlet/Anki 同类 |
| T02-S025 | https://www.jancisrobinson.com/learn/booksDVDsapps/oxford-companion-to-wine | surrogate_primary | 2026-06-06 | Jancis Robinson MW | critic own publication — Oxford Companion 在线版（与 CellarTracker / Purple Pages 集成的参考工具） |
| T02-S026 | https://www.wineberserkers.com/ | reference | 2026-06-06 | Wine Berserkers forum | 论坛 — 资深藏家讨论 CellarTracker 用法 vs 专业评分 / Vivino 噪音（单帖级 caveat 源） |

> 跨 track 复用提示：本 track 的 framework 工具（SAT / deductive grid / Aroma Wheel / Winkler / UC Davis）与 Track 04 canon 的方法工具节、Track 06 glossary 的 standards 节直接对应（同一 source family，bucket 口径一致）。数据平台四件套（Liv-ex / Wine-Searcher / CellarTracker / Vivino）与 Track 05 sources 的 Dataset 节同源——本 track 从「**工具怎么用 + 选型**」角度切入，Track 05 从「**信息源信噪比**」角度切入，互补不重复。

---

## 1. 必备工具（≥ 80% 从业者用）— 框架 + 查价 + 学习参考

> 必备 = 几乎所有认真的从业者 / 备考者都会用，且无之难以执业 / 备考。本行必备工具的特殊性：**最核心的工具不是软件，而是「方法论框架」**（品鉴网格、香气轮）——它们是把 tacit 味觉转成 codifiable 书面结论的脚手架。

### 🧭 1. WSET SAT 网格（Systematic Approach to Tasting）— 必备品鉴框架工具

- **是什么 / 用什么场景**：把品鉴拆成 **外观（appearance）→ 嗅觉（nose）→ 味觉（palate：甜度 / 酸 / 单宁 / 酒精 / 酒体 / 风味强度 / 余味）→ 结论** 的固定网格，每项用校准刻度词（low / medium(-) / medium / medium(+) / high）填写。场景 = **WSET 体系学习 / 备考 + 任何需要「可辩护、可复现的书面品鉴结论」**（教学、采购评估、自我校准）。(evidence: [T02-S001])
- **相对优劣**：✅ 强制结构化，让品鉴可被他人核对、可写进考卷；标准化刻度词消除「好喝 / 不好喝」的模糊。❌ 偏「描述 + 评质」，**不强求猜中产地 / 品种**——纯靠 SAT 不训练盲品演绎能力（那是 CMS grid 的活）。
- **近 12 个月变化**：framework 稳定；WSET 大纲 / Diploma 酒单周期性更新（2024/25 已更），网格本身骨架未变。**Decay: low**。

### 🧭 2. CMS Deductive Tasting Grid（演绎品鉴网格）— 必备盲品框架工具

- **是什么 / 用什么场景**：CMS 的盲品演绎协议——从 sight → nose → palate 的线索做 **initial conclusion（旧 / 新世界、气候、可能品种）→ final conclusion（国 / 产区 / 品种 / 年份 / 品质等级）**。场景 = **CMS 体系备考（Certified 起）+ 一切盲品训练**。可操作化逻辑：高酸 + 轻酒体 + 无橡木 → 凉气候 / 旧世界；高酒精 + 浓果 + 明显橡木 → 暖气候 / 新世界。(evidence: [T02-S002])
- **相对优劣**：✅ 目标是**逻辑演绎到具体产地 / 品种 / 年份**，是侍酒师盲品的核心引擎；网格背到本能后，腾出脑力真正感知。❌ 服务 / 演绎导向，理论广度补强要靠 GuildSomm compendium / canon。
- **SAT vs deductive grid 之争**（→ Track 06 已埋）：WSET-SAT（描述评质、不必猜中）⇄ CMS-grid（逻辑演绎到品种产地年份）是本行「盲品认识论」的两套硬件——选哪个取决于你考哪个体系。
- **近 12 个月变化**：2024 版演绎品鉴格式文档为当前基准；framework 稳定。**Decay: low-medium**（认证大纲周期更新）。

### 🧭 3. Wine Aroma Wheel（Ann Noble, 1984, UC Davis）— 必备香气词汇工具

- **是什么 / 用什么场景**：把香气按相似度组织成三层轮盘（80+ 词，由中心「fruit/spice/floral」泛词向外缘具体词收敛），给「earthy / 泥土味」一类模糊感受一套标准化词汇。**用法**：从中心泛类起步向外缘逼近落词；进阶用「神经训练」——把柑橘 / 杏 / 香草 / 丁香 / 青椒等标准物加进中性基酒，盲闻校准。场景 = **任何阶段的香气识别训练 + 教学**。(evidence: [T02-S003, T02-S015])
- **相对优劣**：✅ 「tacit 味觉记忆 → codifiable 词汇」的经典桥梁；官方 8 语版（**含中文**，是本 track 少数有中文一手的工具）。❌ 是词汇脚手架不是评分 / 演绎工具；只解决「说出闻到什么」，不解决「这是哪 / 值多少」。
- **近 12 个月变化**：1984 至今基本未变（科学锚定的词汇分类稳定）。**Decay: low**。

### 🔎 4. Wine-Searcher — 必备查价 / 识酒 / 评分聚合工具

- **是什么 / 用什么场景**：全球葡萄酒的「比价 + 均价 + 评分聚合」引擎——查一支酒的全球零售报价、历史均价、各评论家分数聚合、产区资料。场景 = **buyer / somm / 学习者 / 消费者的事实查价标准**（定价、选酒、判断一支酒贵不贵、查冷门酒资料）。几乎人人会用。(evidence: [T02-S005])
- **相对优劣**：✅ 价格客观、覆盖广（全球商家滚动报价）；评分聚合多源便于快速参照。❌ 评分**聚合本身会摊平 critic 个体差异**（不知道是谁、什么风格偏好打的分）；零售视角比 Liv-ex 广但浅（不反映 B2B 成交真实价）。
- **Paywall**：基础免费；Pro（全部报价 / 历史价）约 $6/mo 档。(estimate / vendor 自报价档，caveat)
- **近 12 个月变化**：成熟工具，无颠覆性变化。**Decay: low**。

### 📚 5. GuildSomm compendium + 产区地图 + study wiki — 必备学习 / 参考工具

- **是什么 / 用什么场景**：会员制学习平台——**compendium**（产区法规 / 分级 / 气候 / 产量 / 栽培酿造 / 鸡尾酒数据库）+ **study guides**（带复习题，比员工培训深）+ **产区地图** + **盲品 / 备考资源**。场景 = **CMS / MW / Advanced 备考的事实标准学习底座**（GuildSomm 内容直接被 Certified 考试采用）。(evidence: [T02-S004])
- **相对优劣**：✅ 备考生态事实标准，专业纯度高，内容滚动更新。❌ 偏 CMS 生态（WSET 备考者更靠 WSET 教材 + Matthew's World）；会员墙后（约 $149/yr 全会员，或 $7.99/mo 仅 compendium——vendor 自报价，caveat）。
- **近 12 个月变化**：机构级稳定输出，内容持续更新。**Decay: low**。

> **必备工具 top 5 小结**：**SAT 网格 + CMS deductive grid + Aroma Wheel（三大 framework 工具）+ Wine-Searcher（查价）+ GuildSomm（学习参考）**。注意本行「必备」的反直觉：**前三都不是软件而是方法论框架**——这是 codifiable/tacit 张力在工具层的直接体现（工具首先是「把味觉写出来 / 演绎出来」的脚手架，其次才是 app）。

---

## 2. 场景特化工具

> 按职业场景分化：酒窖 / 库存管理、餐厅酒单与 BTG、投资 / 交易数据、侍酒物理工具、备考工具。

### 🗄 6. CellarTracker — 酒窖 / 库存管理 + 众包笔记（藏家 / 资深特化）

- **是什么 / 用什么场景**：全球最大众包品鉴笔记库 + 个人酒窖 / 库存 / 适饮窗管理；与 Jancis Purple Pages / Oxford Companion 在线版打通。场景 = **藏家 / 资深做酒窖管理 + 追踪一支酒的成熟轨迹 + 找对味 taster 追读其笔记**。(evidence: [T02-S006, T02-S025])
- **相对优劣**：✅ 价值不在「平均分」而在「标记 favorite tasters 过滤噪音后追读笔记」+ 成熟度跟踪 + 库存管理；老手用法见 §4。❌ 原始聚合分噪音偏高（需筛 taster）；个人维护（Eric LeVine）但已基础设施化。
- **Paywall**：免费（笔记 / 库存）；可选小额订阅去广告。
- **近 12 个月变化**：成熟平台，无颠覆性变化。**Decay: low-medium**。

### 🍷 7. Coravin（取酒系统）— BTG / 高端侍酒物理工具（餐厅特化）

- **是什么 / 用什么场景**：细针穿过软木塞，注入 argon 惰性气体加压把酒压出，拔针后木塞回弹自封——**不开瓶取一杯**，剩余酒受 argon 保护可存约 4 周（vendor 自报，caveat）。场景 = **餐厅 by-the-glass 项目（尤其高价 / 稀有酒）+ 侍酒师 / 藏家想尝一杯老酒而不牺牲整瓶**。(evidence: [T02-S009, T02-S018])
- **相对优劣**：✅ 显著降损耗、扩 BTG 选择——SevenFifty Daily（trade，非厂商）实证：用 Coravin 测试的餐厅能把起泡 BTG 从一两款扩到半打，改善利润。❌ 设备 + 气瓶成本；对极脆弱老塞 / 螺旋盖适配有限。
- **近 12 个月变化**：成熟产品线（含起泡专用 + 螺旋盖适配迭代），无颠覆性变化。**Decay: low**。

### 📋 8. 餐厅酒单 / BTG 项目软件（BinWise / InVintory 等）— 酒单运营特化

- **是什么 / 用什么场景**：云端饮品库存 + 数字酒单 SaaS——库存盘点、采购下单、合规 / 供应商管理、**与 50+ POS 集成自动同步**（卖完自动从酒单下架）、生成 web/tablet 酒单。场景 = **wine director / beverage manager 运营餐厅酒单与 BTG 项目**。(evidence: [T02-S010, T02-S011])
- **相对优劣**：✅ 把酒单从「手工 Excel + 印刷菜单」升级到实时同步、降低 86 list 错误（卖完还在单上）；BinWise 主打库存 / POS，InVintory 主打高端数字酒窖 + 可视化。❌ 厂商自报功能（vendor docs），实际 ROI 因店而异；订阅成本；细分赛道厂商多（BlackBox、SevenRooms 等周边），无单一事实标准。
- **近 12 个月变化**：该赛道在加 AI 配餐 / 数字菜单模块（见 §3，多为厂商自报）。**Decay: medium**（SaaS 厂商迭代快 / 并购多）。

### 📈 9. Liv-ex — 精品酒价格指数 / B2B 交易数据（投资 / 交易特化）

- **是什么 / 用什么场景**：精品酒二级市场的「彭博」——Fine Wine 100/50/1000 等指数基于真实 B2B 成交。场景 = **投资 / 交易 / 高端零售判断「葡萄酒作为资产」的价格 + 年份 / 产区市场热点**。(evidence: [T02-S007])
- **相对优劣**：✅ 最高信号端——真实成交价、无众包噪音、行业价格基准（Jancis / 媒体 / 投资机构普遍引用）。❌ 仅覆盖「可投资」精品酒（波尔多 / 勃艮第 / 香槟 / 少数膜拜酒），不反映广义市场；纯品鉴向 somm 用不上。
- **Paywall**：指数评论免费；交易平台 / 深度数据 B2B 付费。
- **近 12 个月数字**：2026-01 Liv-ex 100 连续 6 个月上涨、香槟领涨、勃艮第占交易额 31.8%（平台自报指数，caveat：平台数据 / 仅精品酒覆盖）。(evidence: [T02-S007]，与 Track 05 [T05-S012/S030] 同源)
- **近 12 个月变化**：成熟基础设施，无颠覆性变化（数字随市场波动）。**Decay: low**。

### 🔧 10. 侍酒物理工具套装（侍酒刀 / 醒酒器 / 侍酒温度计 / 充氮塞）— 一线服务特化

- **是什么 / 用什么场景**：**侍酒刀 / wine key**（扁平折叠式，含割箔刀 + 双节杠杆 + 螺旋钻，一线开瓶事实标准，Laguiole / Pulltap's 等）/ **醒酒器（decanter）**（分离沉淀 + 增氧，注意：拔塞「透气」几乎不增氧，要真醒得倒进醒酒器——见 Track 06 破绽 #10）/ **侍酒温度计**（红外一秒测瓶温，确保 serving temp）/ **充氮塞 / 真空泵 / Coravin**（保存）。场景 = **餐厅一线侍酒服务 + 品鉴会**。(evidence: [T02-S014])
- **相对优劣**：✅ tacit 服务层的硬件载体；侍酒刀是身份符号 + 效率工具。❌ 醒酒 / 温度高度个案（无放之四海固定时长 / 温度，Track 06 已埋「这支必须醒 X 小时」是被拒厂商话术）；醒酒器 / 充氮等周边易被过度营销（aerator 噱头 > 实效）。
- **fr-primary 备注**：物理工具的高端一手厂多为法国 / 欧洲（L'Atelier du Vin 等），是本 track 少数 fr-primary 维度。
- **近 12 个月变化**：成熟器物，无颠覆性变化。**Decay: low**。

### 🃏 11. 备考工具（抽认卡 Quizlet / Anki / Brainscape + 产区盲图 + tasting grid 模板）— 备考特化

- **是什么 / 用什么场景**：**抽认卡 + spaced repetition**（Quizlet / Anki / Brainscape，被 CMS/WSET 备考社群官方推荐为高效记忆法，有专家策划的 somm 牌组）+ **产区盲图记忆**（印一张无字大地图练默画 + 一张全标注小图参照；描图练习）+ **tasting grid 模板**（把 SAT / deductive grid 练到本能）。场景 = **CMS / WSET / MW 备考的记忆 + 盲品肌肉训练**。(evidence: [T02-S024], grid 见 [T02-S001/S002])
- **相对优劣**：✅ spaced repetition 对海量产区 / 法规 / 品种事实记忆高效；盲图默画是产区空间记忆的标配训练。❌ 抽认卡只解决「事实回忆」，解决不了「盲品感官校准」（那必须靠真酒重复，无工具捷径——AI 也不行，见 §3）。
- **近 12 个月变化**：工具成熟；新增 AI 生成牌组 / 题库（质量参差，需自行核对）。**Decay: low-medium**。

---

## 3. 新兴 / 实验工具（近 12 个月）— 严格区分「真采用」vs「营销未验证」

> **口径（强制）**：只在能找到**从业者 / 机构实际使用证据**时才列「有限采用」，否则归「实验 / 营销未验证」并标 caveat。AI / 区块链类是本节重灾区——大量厂商页 / crypto 媒体 / PR 通稿把「营销词」当「采用」。

### 🤖 12. AI 配餐 / AI virtual sommelier（如 Preferabli / InVintory AI assistant / Sippd）— 有限采用，重 caveat

- **是什么 / 用什么场景**：AI 口味推荐引擎——B2B 给酒店 / 餐厅 / 零售做「虚拟侍酒师」个性化推荐（Preferabli），或消费侧扫餐厅酒单按个人口味 1-100 排序（Sippd），或数字酒窖里 AI 配餐建议（InVintory）。(evidence: [T02-S012, T02-S011, T02-S019])
- **采用证据（真，但需 caveat）**：Preferabli 有**真实 B2B 部署**——Napa Valley Marriott Hotel & Spa 经 Tastefuli app 上线 AI 口味推荐；厂商自报生态覆盖「数千家酒庄 / 餐厅 / 酒店」（**vendor 自报覆盖数，caveat：部分已部署、部分仍在导入，非全量在用**）。trade（Wine Spectator 2025）确认 AI 在酒单 / 推荐侧**正被多店采用**，但定位是 **assists, not replaces**。(evidence: [T02-S012, T02-S019])
- **硬边界（不软化）**：① **arXiv SommBench（2026-03，verified_primary）**：LLM 葡萄酒**理论题高达 97%**，但**配餐 MCC 仅 0-0.39、feature completion 峰值 65%**——「sensory 判断」是核心短板，因 LLM 只从文本学、缺 grounding；人类专家在味觉 / 香气配对的演绎推理上**显著胜过**当前 LLM。② trade 实测（Restaurant Business：Cru Uncorked AI vs somm）结果各半，**冷门品种 AI 露怯**；AI 不能实时尝酒 / 评估杯中演化 / 读懂餐桌情绪。(evidence: [T02-S016, T02-S020, T02-S019])
- **结论**：**AI = 查询 / 推荐 / 运营侧的助手工具（有限真采用），不是品鉴 / 盲品工具**。专业盲品训练与桌边判断不能靠它。**Decay: high**（赛道 12 月内剧变 / 厂商洗牌）。

### 🌱 13. AI 驱动栽培 / 酿造 / 酒旅运营（生产侧）— 真用例，但非侍酒侧

- **是什么 / 用什么场景**：AI 在**葡萄园 / 酒厂 / 酒旅**的管理用例（产量预测、病害监测、发酵控制、酒旅个性化）。arXiv 2025-07 综述梳理这是 AI 在本行**相对成熟的真实应用面**——但属生产 / 运营侧，非侍酒师 / 品鉴侧。(evidence: [T02-S017])
- **caveat**：与侍酒师 master skill 的核心场景（品鉴 / 服务 / 选酒）关系弱；列此是为**划清「AI 在哪真有用 vs 在哪是营销」的边界**——生产侧有真用例，品鉴侧（§12）受 sensory grounding 限制。**Decay: medium**。

### 📲 14. 数字酒单 / QR 酒单（BinWise SproutQR / SevenRooms 等模块）— 部分采用

- **是什么 / 用什么场景**：餐厅把酒单数字化（tablet / QR），与库存 / POS 实时同步、卖完自动下架。(evidence: [T02-S010])
- **采用证据**：是 §8 酒单 SaaS 的延伸模块，**疫情后 contactless 趋势 + 实时库存同步**驱动有真实采用（厂商自报 + trade 提及）；但「数字酒单」本身是功能而非独立颠覆工具。**caveat**：vendor docs 为主，单店 ROI 因店而异。**Decay: medium**。

### ⛓ 15. 区块链溯源 / NFC 防伪（dVIN / eProvenance / ZATAP-Identiv 等）— 实验 / 营销未验证为主

- **是什么 / 宣称场景**：用区块链 + NFC/RFID 标签做 fine wine 防伪 / 溯源 / 温度链监测，宣称解决 counterfeit 问题（厂商引用「假酒占流通 20% / 损失 $70B」等吓人数——**这些数字多来自厂商 / crypto 媒体，未经独立核实，重 caveat**）。(evidence: [T02-S021, T02-S013])
- **真伪判定（按 prompt 口径，不把营销当采用）**：① 大量来源是**厂商页 / crypto 媒体 / PR 通稿**（dVIN Labs、Blaize、Osiz、Cointelegraph、London Blockchain）——**不作采用证据**。② **eProvenance** 是真实存在的较老技术（Eric Vogt 创办，RFID/NFC 温度链监测 + provenance），但核心是**运输 / 仓储温度监测**而非消费级区块链防伪，且非侍酒师日常工具。③ trade（Wine Enthusiast）的去营销化评估：区块链防伪**有潜力但采用零散、未成行业标准**，从业者日常并不用。
- **结论**：**区块链溯源 = 实验 / 营销未验证为主**（少数真实 NFC 温度链如 eProvenance，但非品鉴 / 侍酒工具）。侍酒师层面**无证据广泛采用**。**Decay: high**（高度 hype 驱动）。

> **新兴工具小结（Phase 2.8 诚实边界用）**：近 12 个月唯一**有真采用证据**的新兴侍酒侧工具 = **AI 推荐 / virtual sommelier（assists 定位，sensory 不能替代人）**；生产侧 AI 有真用例但非侍酒场景；**区块链 / NFC 防伪 = 营销 > 采用，侍酒师层面未验证**。AI 配餐 app / 数字酒单 / 区块链溯源**都不能替代盲品训练**（arXiv SommBench 硬证据：LLM 理论强、sensory 弱）。

---

## 4. 避坑清单（外行 / 新手容易选错的工具）

> 每条配「内行为何拒绝」。本节与 Track 06「厂商话术拒绝」节呼应（同一价值观在工具层的落地）。

- **❌ 把 Vivino 均分当权威品质信号** → **拒绝**。Vivino 是**最低信号端**：亿级大众样本，均分受甜度偏好 / 价格锚定 / 品牌效应污染。学术（Journal of Wine Economics）：Vivino 与专业评分**相关但更弱**——业余重「即时愉悦」，专业看「陈年潜力」；2025 另有 Vivino reputation inflation 研究。**内行用法**：Vivino 仅看「大众接受度 / 大概好不好喝」，**绝不作专业品质依据**。专业品质锚要用评论家长稿（Jancis/Vinous）+ Liv-ex 价格 + CellarTracker 筛选后的笔记。(evidence: [T02-S008, T02-S022, T02-S026])
- **❌ 用消费 App（Vivino / 扫标签）替代盲品训练** → **拒绝（不软化）**。**盲品是感官肌肉，必须靠真酒重复校准，无 app 捷径**。看标签查分 = 反盲品（盲品的全部意义是不看标签）。连 AI 都做不到（arXiv SommBench：LLM 配餐 MCC 0-0.39，sensory 是死穴）——**专业盲品训练不能靠任何消费 App / AI**，只能靠 SAT/deductive grid + 真酒 + Aroma Wheel 词汇校准。(evidence: [T02-S016, T02-S008])
- **❌ 把 critic 评分聚合（Wine-Searcher 聚合分 / 裸分）当客观真理** → **拒绝**。聚合摊平了「谁打的、什么风格偏好」；100 分制本质是单个评论家特定时点的主观印象，系统性偏爱浓郁 fruit bomb、惩罚克制风格，**不可跨评论家通约**。内行看「谁打的 + 风格偏好」，不看裸分。(evidence: [T02-S005], 呼应 Track 06 厂商话术拒绝)
- **❌ 把酒单 SaaS / AI 配餐厂商的「采用数」当事实** → **拒绝**。SaaS / AI 厂商页（vendor docs）自报「数千家在用」混合了「已部署 + 仍在导入」；G2 / Capterra / PR 通稿不作工具真伪来源。判断真采用要看 trade media 独立报道 + 实际部署案例。(evidence: [T02-S012, T02-S019])
- **❌ 被区块链 / NFC 防伪的「假酒占 20% / $70B 损失」吓单买入** → **拒绝**。这些数字多来自厂商 / crypto 媒体未经独立核实；区块链防伪侍酒师层面未广泛采用。投资酒「稳赚 / 保真」更是诈骗高发话术（呼应 Track 06「投资酒稳赚」）。(evidence: [T02-S021], 呼应 Track 06 [T06-S033])
- **❌ 迷信醒酒器 / aerator / 充氮塞「神效」** → **拒绝**。多数酒开瓶即饮；拔塞「透气」几乎不增氧（瓶颈面积太小，要真醒得倒进醒酒器）；「这支必须醒 X 小时」无放之四海固定时长。物理工具买基础款（好侍酒刀 + 一个醒酒器）即可，别为营销噱头加价。(evidence: [T02-S014], 呼应 Track 06 [T06-S035])

---

## 5. 工具选型决策树（按场景：学习 / 查价 / 盲品训练 / 酒窖管理 / 投资）

> 给「该用什么」的可操作分诊。每条挂场景 → 工具 + 一句话理由。

```
你的目标是？
├─ 【学习 / 备考】
│   ├─ 考 CMS / 走侍酒师路线 → GuildSomm compendium + study wiki + 产区地图 [S004]（事实标准）
│   │                          + CMS deductive grid 练到本能 [S002] + 抽认卡(Anki/Quizlet) [S024]
│   ├─ 考 WSET / Diploma → WSET 教材 + SAT 网格 [S001] + Matthew's World podcast(Track 05) + 抽认卡 [S024]
│   ├─ 任何阶段练香气词汇 → Wine Aroma Wheel [S003]（中心向外缘逼近 + 标准物盲闻校准）
│   └─ 查任何术语 / 产区事实 → Oxford Companion 在线 [S025] / GuildSomm compendium [S004]
│
├─ 【查价 / 选酒 / 定价】
│   ├─ 查一支酒全球零售价 / 均价 / 资料 → Wine-Searcher [S005]（事实标准，几乎人人用）
│   ├─ 判断品质（要看「谁打分」）→ 评论家长稿 Jancis/Vinous(Track 05)，不看 Vivino 裸分
│   └─ 查精品酒「作为资产」的真实成交价 → Liv-ex [S007]（投资侧）
│
├─ 【盲品训练】
│   └─ ⚠ 无 app / AI 捷径 → SAT 或 deductive grid [S001/S002] + 真酒重复 + Aroma Wheel 词汇 [S003]
│       （消费 App 扫标签是反盲品；AI sensory 是死穴 [S016]）
│
├─ 【酒窖 / 库存管理】
│   ├─ 个人藏家（笔记 + 适饮窗 + 跟成熟度）→ CellarTracker [S006]（标记 favorite tasters 过滤噪音）
│   │                                       高端可视化 → InVintory [S011]
│   └─ 餐厅酒单 / BTG 运营（库存 + POS + 数字酒单）→ BinWise / InVintory 类 SaaS [S010/S011]
│       BTG 高价 / 稀有酒不开瓶取酒 → Coravin [S009]
│
├─ 【投资 / 交易】
│   ├─ 价格指数 / 市场热点 / 成交数据 → Liv-ex [S007]（最高信号，仅精品酒覆盖）
│   └─ 零售比价补充 → Wine-Searcher Pro [S005]
│
└─ 【一线侍酒服务】
    └─ 物理工具：侍酒刀(wine key) + 醒酒器(decanter，需要才用) + 侍酒温度计 + 充氮塞/Coravin [S014/S009]
        （别迷信 aerator 噱头；醒酒高度个案）

⛔ 任何场景都别做的：把 Vivino 均分当品质权威 [S008] / 用扫标签 App 替代盲品 [S016] /
   把 critic 裸分当客观真理 [S005] / 信区块链「保真稳赚」[S021]
```

**决策树一句话总纲**：**学习靠 GuildSomm/WSET + 框架工具；查价靠 Wine-Searcher；品质靠看「谁打分」的评论家长稿；盲品只能靠真酒 + 网格（无捷径）；酒窖靠 CellarTracker；投资靠 Liv-ex；服务靠基础物理工具。AI 是助手不是替代，区块链是营销不是采用。**

---

### 冷僻 / 信号薄弱（→ Phase 2.8 诚实边界）

- **工具数 = 15 类 / 条目（远超 20 tools 若按具体工具计：SAT、deductive grid、Aroma Wheel、Wine-Searcher、GuildSomm、CellarTracker、Coravin、BinWise、InVintory、Liv-ex、侍酒刀、醒酒器、侍酒温度计、充氮塞、抽认卡 Quizlet/Anki/Brainscape、产区盲图、Oxford Companion 在线、AI Preferabli、Sippd、AI cellar assistant、数字酒单、区块链 eProvenance/dVIN ≈ 22+ 具体工具）✅**；source = 26 ✅；四象限 + 决策树齐全 ✅。**不触发冷僻协议。**
- **bucket 现实（与 Track 04/05/06 一致的结构性事实）**：verified_primary 仅 3（UC Davis `.edu` + 2 篇 arXiv）；framework 工具的权威 = 认证机构（cert body 逃生阀）、数据 / SaaS 工具的文档 = 厂商自有（vendor docs 逃生阀）——**葡萄酒工具权威几乎不在 .edu/.gov**，verified_primary 占比低是行业结构性事实，非偷工。所有 vendor docs 已诚实标注（不冒充中立一手）。
- **AI / 区块链「采用 vs 营销」边界（本 track 独有诚实边界）**：AI 推荐有**有限真采用**（Preferabli B2B 部署 + trade 确认），但 sensory / 盲品**有 arXiv 硬证据证明 AI 不能替代**；区块链防伪**侍酒师层面无广泛采用证据**（来源多为厂商 / crypto 媒体 / PR）。Phase 2.8 应明说：**别把 AI/区块链营销词当从业者采用**。
- **中英失衡（与全行一致）**：工具生态 all-en（少数 framework 工具如 Aroma Wheel 有官方中文版）；查价 / 酒窖 / 酒单 SaaS 的中文等价物未在专业语境成事实标准；中文一手工具文档稀薄。SKILL.md 工具节应标「核心工具 en-primary，中文用户须直接用英文工具 / 文档」。
- **物理工具 fr-primary**：高端侍酒物理工具一手厂偏法国 / 欧洲（L'Atelier du Vin 等），是本 track 少数 fr 维度，但器物本身语言依赖低。
- **数字深度未全量爬取**：SaaS 厂商的具体功能 / 价格档 / 采用数为厂商自报（vendor docs），已逐条加 caveat；Liv-ex 指数数字为平台自报。需 high-confidence 采用率 / 价格时，Phase 2 应补独立 trade 报道 / 实际部署案例核实。

---

## 与其他 Track 的协作 seed

- **→ Track 01 figures**：工具 originator / 维护者作为 figure 候选——**Ann C. Noble**（Aroma Wheel originator，UC Davis 首位女教授，已在 Track 04）/ **Eric LeVine**（CellarTracker 创始，Track 05 已埋次级候选）/ **Maynard Amerine + Albert Winkler**（20-point scale + Winkler index，UC Davis 学院派，Track 04 已埋）。新增微弱候选：Preferabli / Coravin 创始人（工具厂创始，但 figure 价值弱，不强推）。
- **→ Track 03 workflows**：工具直接挂工作流——**SAT 网格填写流程**（外观→嗅觉→味觉→结论）/ **CMS 演绎盲品流程**（sight→nose→palate→initial/final conclusion）/ **Aroma Wheel 香气逼近流程**（中心→外缘 + 标准物盲闻校准）/ **侍酒服务流程**（侍酒刀开瓶→判断是否醒酒→醒酒器→侍酒温度→Coravin/充氮保存）/ **酒窖管理流程**（CellarTracker 录入→标记 taster→跟踪适饮窗）/ **酒单运营流程**（SaaS 库存同步→POS→数字酒单卖完下架）/ **查价选酒流程**（Wine-Searcher 查价→看「谁打分」而非裸分→Liv-ex 验资产价）。
- **→ Phase 2.8 诚实边界**：三点须落地——① **AI/区块链「采用 vs 营销」边界**（AI 推荐有限真采用、sensory 不能替代人[arXiv 硬证据]；区块链侍酒侧未验证）；② **verified_primary 结构性偏低**（工具权威在 cert body + vendor docs，不在 .edu/.gov）；③ **中英失衡**（工具 all-en，仅 Aroma Wheel 等少数有中文版）。
- **一致性检查**：本 track 与 Track 05（Dataset 节四件套同源，工具视角 vs 信噪比视角互补）、Track 04（方法工具节同源）、Track 06（standards 节 SAT/grid/Aroma Wheel + 厂商话术拒绝节同源）bucket 口径完全一致。若 Track 03 后续发现本 track 未列的产区 / 酿造专用设备（如折光仪 refractometer 量 brix、实验室分析仪——偏酿造端非侍酒端），可补「酿造 / 栽培测量工具」子类（本 track 聚焦侍酒 / 品鉴 / 学习侧，刻意未深入酒厂实验室设备）。
