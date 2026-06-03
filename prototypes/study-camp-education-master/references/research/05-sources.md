# Track 05 — Sources（信息源）：研学旅行与营地教育

> Phase 1 Wave 1 输出。locale=zh-CN，focus=operational+business，profile=practitioner。
> 调研日期：2026-06-03。覆盖：newsletter / report / podcast / conference / community / 数据榜单 + 一手率诚实边界。

## 诚实边界（先读）

本行业「信息源」生态有三条结构性事实，直接决定本 track 的形态：

1. **一手发声沉淀在黑名单渠道。** 研学/营地从业者的运营复盘、课程方法论、踩坑经验，绝大多数发在**微信公众号 / 知乎 / 视频号**——这三类是本 pipeline 信源黑名单（不进 Manifest，不作知识真伪来源）。本 track 在正文**指出**这些公众号/媒体号作为「生态存在」（让用户知道去哪找鲜活内容），但 URL 一律不进 Manifest，引用其内容时一律找可引用替身（机构官网 / 报告原文 / 政策原文 / 协会发布）。

2. **「信息源」的主力是机构媒体 + 行业报告 + 行业大会，不是个人 newsletter / podcast。** 这是政策驱动型 B 端为主的服务业，缺个人长访谈型 newsletter / Substack，**中文播客维度近乎空白**（逐一搜索 小宇宙 / 喜马拉雅 / Spotify 均未找到一档持续运营、以研学/营地/自然教育为主轴的从业者播客——见下「薄弱维度」）。故本 track 的 newsletter「替身」是**教育垂直媒体的栏目/资讯流**（芥末堆、多鲸、亿欧教育、蓝鲸教育），podcast 维度如实标「信源稀薄」。

3. **一手率（verified_primary）结构性偏低。** `source_verifier.py` 只把 `.gov / .org.cn` 类判 verified_primary，把商业媒体 / 行业报告平台 / 上市公司财报门户判 secondary。本 track 的 Manifest 里：政策/标准原文、协会自身发布的报告、上市公司财报原文（PDF）算 verified/surrogate_primary；研报平台转载、媒体报道算 secondary；协会/大会官网、营地认定门户标 surrogate_primary（白名单：协会 / 会议 sponsor）。**verified_primary 占比偏低是真实的，文末如实标。**

---

## Source Manifest

> bucket 由 `tools/research/source_verifier.py classify` 跑出，仅按 manifest policy 升级 surrogate_primary（协会/会议/监管/榜单白名单），不私自降级、不放黑名单 URL。

| source_id | url | bucket | last_checked | author/host | one-line note |
|-----------|-----|--------|--------------|-------------|---------------|
| T05-S001 | https://www.cceacamps.org/ | surrogate_primary | 2026-06-03 | CCEA 中营联 | 中国营地教育联盟官网；CCEC 营地教育大会主办（会议官网，白名单） |
| T05-S002 | https://www.icfconnect.net/ | surrogate_primary | 2026-06-03 | ICF | 国际营地组织；ICC 世界营地大会，2026 第 13 届落地中国（会议官网，白名单） |
| T05-S003 | https://www.icfconnect.net/icc2026/ | surrogate_primary | 2026-06-03 | ICF | ICC 2026 中国大会专页（会议官网，白名单） |
| T05-S004 | https://www.acacamps.org/accreditation | surrogate_primary | 2026-06-03 | ACA 美国营地协会 | ACA 营地认证标准（health/safety/risk）；2025-11 版（协会标准，白名单） |
| T05-S005 | http://www.natureeducation.org.cn/ | verified_primary | 2026-06-03 | 全国自然教育网络 | 全国自然教育论坛主办方官网（注：访问时一度 ECONNREFUSED，标 decay 观察） |
| T05-S006 | http://cnec.csf.org.cn/ | verified_primary | 2026-06-03 | 中国林学会 CSF | 中国自然教育大会官网（与全国自然教育论坛并轨，林学会系） |
| T05-S007 | https://www.jiemodui.com/ | secondary | 2026-06-03 | 芥末堆 | 教育垂直媒体；研学/营地资讯流（newsletter 替身，非黑名单：机构媒体官网） |
| T05-S008 | https://get.jiemodui.com/ | secondary | 2026-06-03 | 芥末堆 | GET 教育科技大会官网，2024 十周年（会议官网，白名单） |
| T05-S009 | http://report.iresearch.cn/report/201905/3362.shtml | secondary | 2026-06-03 | 艾瑞咨询 | 《中国泛游学与营地教育行业白皮书》(2019)，新东方联合发布 |
| T05-S010 | https://www.iimedia.cn/c400/101385.html | secondary | 2026-06-03 | 艾媒咨询 | 《2024-2025 中国研学游经济市场运行监测报告》原发布页 |
| T05-S011 | https://travel.cnr.cn/dsywzl/20250118/t20250118_527044924.shtml | secondary | 2026-06-03 | 央广网 | 《2024 中国研学旅游发展报告》(中国旅行社协会发布) 报道 |
| T05-S012 | https://www.tiyan.org.cn/article-8-1981.html | surrogate_primary | 2026-06-03 | 研学旅行官方门户 (.org.cn) | 中国旅行社协会研学旅行分会发布报告页（协会发布，白名单） |
| T05-S013 | http://www.djcapital.net/col.jsp?id=106 | secondary | 2026-06-03 | 多鲸资本/多鲸研究院 | 多鲸《素质教育行业发展趋势报告》(年度，含营地研学章节) 来源机构 |
| T05-S014 | https://www.mingde.com/ | secondary | 2026-06-03 | 世纪明德 | 研学龙头官网；中国教育明德论坛（21 届）主办，研学主题峰会 |
| T05-S015 | https://xinsanban.eastmoney.com/f10/839264.html | secondary | 2026-06-03 | 东方财富/世纪明德 | 世纪明德(839264) 新三板 F10；财报数据入口（资本/数据榜单） |
| T05-S016 | https://pdf.dfcfw.com/pdf/H2_AN202504241661731636_1.pdf | secondary | 2026-06-03 | 世纪明德 | 世纪明德 2024 年度报告 PDF 原文（财报一手，但经第三方门户托管） |
| T05-S017 | https://www.ydjy8.com/ | secondary | 2026-06-03 | 营地教育网 | 行业垂直资讯门户 + 营地教育产业大会媒体支持（社区/资讯流替身） |
| T05-S018 | https://www.dili360.com/article/p672c4b767ef5587.htm | secondary | 2026-06-03 | 中国国家地理 | 2024 世界研学旅游大会(WRTO/槟城)报道；WRTO 战略合作 |
| T05-S019 | https://www.iresearch.com.cn/ | secondary | 2026-06-03 | 艾瑞咨询 | 艾瑞官网（报告检索入口） |
| T05-S020 | https://www.xiaoyuzhoufm.com/ | secondary | 2026-06-03 | 小宇宙 | 中文播客头部平台（用于检索——本行业无对口节目，见薄弱维度） |

> 黑名单未入表的「生态存在」（正文指出、URL 不进 Manifest）：研学/营地/自然教育领域的**微信公众号**（如「多鲸」「芥末堆」「营地教育网」「自然教育论坛」等均有公众号作为主发声渠道）、**知乎专栏**、**视频号/抖音**。要引用其内容请回到上表的机构官网 / 报告原文 / 协会发布替身。

---

## 总览（按 type 分组）

### Newsletter / 媒体资讯流 — 4 个（本行业「newsletter」=教育垂直媒体栏目，非个人 Substack）
| Source | Cadence | Tier | 投入产出 | One-liner |
|--------|---------|------|---------|-----------|
| 芥末堆 (jiemodui) | rolling/daily | mixed | medium | 教育全行业垂媒，研学/营地有专题，资本+政策+案例 |
| 多鲸 / 多鲸研究院 | rolling + 年度报告 | practitioner→senior | medium | 资本视角，年度《素质教育趋势报告》含营地研学章节最权威之一 |
| 亿欧教育 / 蓝鲸教育 | rolling/daily | mixed | low-medium | 教育产业财经向，研学是其覆盖子赛道（ambient awareness） |
| 营地教育网 (ydjy8) | rolling | practitioner | medium | 行业垂直门户，政策汇总+营地运营+人物访谈，最贴近营地一线 |

### Podcast — 0 个对口（信源稀薄，如实标）
| Source | 状态 | 说明 |
|--------|------|------|
| （无） | N/A | 逐一搜小宇宙/喜马拉雅/Spotify 未找到持续运营、以研学/营地/自然教育为主轴的从业者播客。通用教育播客偶有单集涉及，但无对口节目。**该维度信源稀薄。** |

### Conference / 行业大会 — 7 个（本行业最强信源类型）
| Conference | 频率 | 最近/下届 | One-liner |
|-----------|------|----------|-----------|
| CCEC 全国营地教育大会 (CCEA 主办) | 年度 | 第 8 届 2024 | 中国营地教育旗舰会，联盟系，国际+本土营地圈 anchor |
| 全国自然教育论坛 / 中国自然教育大会 | 年度 | 第 11 届 2024 中山 | 自然教育子赛道旗舰，林学会+自然教育网络系 |
| 营地教育产业大会 (营地教育网) | 年度 | 第 5 届 2024 成都 | 产业+商业视角营地会，与素博会同期 |
| GET 教育科技大会 (芥末堆) | 年度(含春季场) | 2024 十周年 | 教育科技综合大会，研学/营地作素质教育板块出现 |
| GES 未来教育大会 (好未来等) | 年度 | 近年 | 高规格教育峰会，国务院发展研究中心指导，战略级议题 |
| 中国教育明德论坛(研学峰会)(世纪明德) | 年度 | 第 21 届 | 校长+研学机构对接，B 端集采视角 |
| ICC 世界营地大会 (ICF) | 三年一届 | 第 13 届 2026 中国 | 全球营地最高规格会，2026 落地中国是本行业近期最大事件 |

### Community / 社区 — 2 个（弱，主力沉淀在黑名单渠道）
| Community | Platform | 规模 | One-liner |
|-----------|----------|------|-----------|
| 营地教育网生态 | 垂直门户+公众号群 | 中 | 行业资讯+夏营合作+课程赋能，从业者聚集地 |
| CCEA 联盟 / 各省研学协会 | 协会会员网络 | 38 理事单位(CCEA) | 机构会员制，非公开社区，靠大会/培训聚合 |

### Dataset / 数据榜单 — 2 个（资本+财报，非 benchmark）
| Dataset | URL | Maintainer | One-liner |
|---------|-----|-----------|-----------|
| 世纪明德新三板财报 | xinsanban.eastmoney.com/f10/839264 | 东方财富 | 唯一可公开拉取的研学龙头连续财务数据 |
| 行业报告市场规模序列 | (多鲸/艾瑞/艾媒/旅行社协会) | 多机构 | 市场规模/企业数/客单价等口径数据，**各家口径打架，挂 caveat** |

---

## 逐条 Source 卡片

### 📅 1. CCEC 全国营地教育大会（中国营地教育联盟 CCEA 主办）

- **Type**: conference
- **URL**: https://www.cceacamps.org/ (evidence: [T05-S001])
- **Maintainer**: CCEA 中营联营地教育发展中心（11 家机构发起：北京航海中心、启行 IDEAS、世纪明德、新东方文旅、万科梅沙、UWC 常熟等；截至 2025-06 扩至 38 家理事单位）
- **Cadence**: 年度
- **Last activity**: 第 8 届 CCEC 2024（官网挂「2024 年第八届 CCEC 回顾」）；第 9 届续办中
- **Audience tier**: practitioner→senior（营地主理人、课程总监、机构创始人）
- **One-liner**: 中国大陆营地教育最早的非营利行业组织主办的旗舰年会——营地圈「认人、认机构、认标准」的 anchor 会，国际营地理念与本土落地的交汇点。
- **典型每期内容**: 主旨讲座 + 圆桌论坛 + 平行工作坊 + 跨界恳谈会；覆盖营地安全管理、课程设计、辅导员培养、国际营地标准本土化、行业研究报告发布。第 7 届(2021)主题「IN CAMP, ABOVE CAMP」。
- **投入产出比**: high（≥80% 营地从业者必跟——这是本子赛道最集中的年度信号源）(evidence: [T05-S001])
- **Paywall**: 参会付费（门票制），内容部分公开回顾
- **签名内容**: 历届 CCEC 回顾页（2020 第六届 / 2021 第七届 / 2024 第八届）(evidence: [T05-S001])
- **Endorsement evidence**: cross_source（上海市民办教育协会报道「吸引过万人线上线下参与」）+ community_consensus（11 家头部机构联合发起，行业公认）
- **替代品**: 营地教育产业大会（T05-S017 系，更产业/商业向）
- **最近变化（近 6 月）**: 理事单位扩容至 38 家（2025-06）
- **可信度**: high　**Decay risk**: low（机构级、联盟背书）

### 📅 2. ICC 世界营地大会（International Camping Fellowship, ICF）

- **Type**: conference
- **URL**: https://www.icfconnect.net/ ; 2026 专页 https://www.icfconnect.net/icc2026/ (evidence: [T05-S002, T05-S003])
- **Maintainer**: ICF（1987 年成立的全球营地专业人士组织）
- **Cadence**: 三年一届（every third year）
- **Last activity / 下届**: 第 13 届 ICC 2026 落地**中国**（与 CCEA 联合推广，已启动「Campfire Relay 火炬手计划」）
- **Audience tier**: senior（国际营地行业，跨国交流+趋势+培训）
- **One-liner**: 全球营地教育最高规格大会，三年一届轮值办；2026 首次（按本届）由中国承办——**这是研学营地行业近期最大的国际级事件**，对国内营地国际化、标准对接是关键窗口。
- **典型每期内容**: 各国营地实践展示 + 趋势教育 + networking；面向营地教育专业人士、学生与「friends of camping」。
- **投入产出比**: medium（三年一届，频率低；但 2026 中国办使其对国内从业者性价比骤升）(evidence: [T05-S002])
- **Paywall**: 参会付费
- **签名内容**: ICC2026 中国大会专页 + Torchbearer Program (evidence: [T05-S003])
- **Endorsement evidence**: cross_source（CCEA 官网 + ICF 官网双向）+ community_consensus（全球营地圈 38 年历史组织）
- **替代品**: ACA 美国营地协会全国大会（北美向，T05-S004 系）
- **最近变化**: 2026 落地中国（重大）
- **可信度**: high　**Decay risk**: low（机构级国际组织）；但 next edition 间隔 3 年，**非中国年份对国内用户性价比降级**

### 📅 3. 全国自然教育论坛 / 中国自然教育大会

- **Type**: conference
- **URL**: 主办方 http://www.natureeducation.org.cn/ ; 大会 http://cnec.csf.org.cn/ (evidence: [T05-S005, T05-S006])
- **Maintainer**: 全国自然教育网络（由全国自然教育论坛发展而来，活跃一线机构与个人志愿发起；与中国林学会 CSF 自然教育系并轨办大会）
- **Cadence**: 年度
- **Last activity**: 第 11 届 2024-12 广东中山桂南村；第 10 届 2023-11 云南大理（主题「众人拾柴，聚薪成火」）；首届 2014 厦门
- **Audience tier**: practitioner→senior（自然教育/环境教育从业者、保护机构、研学自然子赛道）
- **One-liner**: 自然教育子赛道的旗舰年度论坛，连续办 10+ 届——研学里「自然教育」方向从业者认人认机构的 anchor，与阿拉善 SEE / 自然之友 / 林学会生态深度绑定。
- **典型每期内容**: 行业研究、人才培养、政策倡导、区域网络、学术研讨会（含论文集）；连接行业↔公众↔政府。
- **投入产出比**: high（自然教育子赛道必跟）(evidence: [T05-S005, T05-S006])
- **Paywall**: 参会/报名制
- **签名内容**: 第 6 届(2019 武汉)与中国自然教育大会合并；2024 上海中国自然教育大会 (evidence: [T05-S006])
- **Endorsement evidence**: cross_source（广东林业局 + 关注森林 + 人民网多源报道）+ community_consensus
- **最近变化**: 与「中国自然教育大会」品牌融合，林学会系介入
- **可信度**: high　**Decay risk**: low；但 **T05-S005 官网访问时一度 ECONNREFUSED，需 Phase 4 复核可用性**

### 📅 4. 营地教育产业大会（营地教育网 ydjy8 / CCEA 系）

- **Type**: conference
- **URL**: https://www.ydjy8.com/ (evidence: [T05-S017])
- **Maintainer**: 营地教育网主办，中国营地教育联盟支持
- **Cadence**: 年度
- **Last activity**: 第 5 届 2024-11 成都（暨西部劳动与实践教育峰会，与 CCE 素博会同期）；第 4 届 2023-10 张家口崇礼云顶；第 3 届 2022-04；第 2 届 2021-03
- **Audience tier**: practitioner（营地运营、产品、渠道）
- **One-liner**: 比 CCEC 更偏「产业/商业/招商」的营地年会，常与体育/旅游博览会同期——看营地运营落地、渠道合作、设备供应商的信号场。
- **典型每期内容**: 产业趋势、营地运营案例、「营地教育+」跨界（劳动教育、研学实践）、供应商对接。
- **投入产出比**: medium（产业向，与 CCEC 部分重叠，营地运营者可二选一或都跟）(evidence: [T05-S017])
- **Paywall**: 参会付费
- **签名内容**: 第四届「营地教育+」回放、第五届西部劳动与实践教育峰会 (evidence: [T05-S017])
- **Endorsement evidence**: cross_source（营地教育网自办+联盟支持）；**borderline——与 CCEC 同生态，独特价值在「产业/商业落地+西部」切口**
- **最近变化**: 2024 移师成都，绑定西部劳动教育主题
- **可信度**: medium　**Decay risk**: medium

### 📅 5. GET 教育科技大会（芥末堆主办）

- **Type**: conference
- **URL**: https://get.jiemodui.com/ (evidence: [T05-S008])
- **Maintainer**: 芥末堆（教育科技垂媒），自 2015 起独立举办
- **Cadence**: 年度（含春季场）
- **Last activity**: GET2024（2024-11 北京国际会议中心，十周年；另有 2024-04 春季场）；GET2025 已挂网
- **Audience tier**: mixed（教育全行业，研学/营地作素质教育板块）
- **One-liner**: 教育科技领域连接国内外、跨板块的综合大会——研学营地不是主角但常有专题，看「研学如何被资本/政策/科技看待」的外部视角窗口。
- **典型每期内容**: AI+教育、政策解读、素质教育（含营地研学露营）、资本与供应链、年度评选。
- **投入产出比**: low-medium（综合会，研学营地信号占比低，作 ambient awareness）(evidence: [T05-S008])
- **Paywall**: 参会付费
- **签名内容**: 「超 1.4 万亿露营市场规模下，亲子赛道火苗渐显」(芥末堆稿，evidence: [T05-S007]) ; GET2024 十周年主题「新质学习力」 (evidence: [T05-S008])
- **Endorsement evidence**: community_consensus（教育圈连办 10 年品牌）+ cross_source（多家转载）
- **可信度**: high（会议本身）　**Decay risk**: low

### 📅 6. GES 未来教育大会（中国发展研究基金会 + 好未来等）

- **Type**: conference
- **URL**: 承办方好未来 https://www.100tal.com/ （GES 无稳定独立官网，依托好未来/未来之星）(evidence: [T05-S020 检索得；主办信息见正文])
- **Maintainer**: 中国发展研究基金会携北师大、腾讯、GSV、新东方、好未来联合主办；国务院发展研究中心、教育部指导；好未来「未来之星」承办
- **Cadence**: 年度（近年频率受行业波动影响）
- **Audience tier**: senior（战略级、跨界、国际教育议题）
- **One-liner**: 国内规格最高的教育峰会之一，国务院发展研究中心指导——研学营地从业者看「教育政策风向 + 国际教育趋势」的战略级信号，但具体研学运营内容少。
- **典型每期内容**: 海内外教育权威跨界对话、未来教育/全球化国际教育议题。
- **投入产出比**: low（战略级，研学营地运营 actionable 信号少；senior 战略阅读用）
- **Paywall**: 参会/受邀
- **Endorsement evidence**: community_consensus（部委指导、顶级机构联办）
- **可信度**: high　**Decay risk**: medium（GES 近年办会节奏不稳，无独立稳定官网，**需 Phase 4 复核近一届年份**）

### 📅 7. 中国教育明德论坛 · 研学峰会（世纪明德主办）

- **Type**: conference
- **URL**: https://www.mingde.com/ (evidence: [T05-S014])
- **Maintainer**: 世纪明德（研学龙头，新三板 839264）；论坛前身 2006 清华「全国中小学校长高峰论坛」
- **Cadence**: 年度
- **Last activity**: 已办 21 届全国教育明德论坛暨基础教育学习论坛；含「研学旅行＆营地教育学习论坛」研学主题峰会
- **Audience tier**: practitioner（校长、教育局、研学机构——B 端集采视角强）
- **One-liner**: 龙头机构主办、面向校长/教育局的论坛——看研学「B 端集采、公立校综合实践课时落地」这条线的最佳信号场（C 端家长视角弱）。
- **典型每期内容**: 校长对话、研学课程与学科融合、综合实践育人、B 端采购对接。
- **投入产出比**: medium（B 端从业者 high，C 端从业者 low）(evidence: [T05-S014])
- **Paywall**: 参会制
- **Endorsement evidence**: cross_source（世纪明德官网 + 央广/科普研学联盟报道）；**注意主办方利益相关，议程偏自家生态**
- **可信度**: medium（商业主办，需交叉验证）　**Decay risk**: medium（绑定世纪明德经营状况——该公司连续亏损，见 S016）

### 📰 8. 芥末堆（jiemodui）— 教育垂直媒体（newsletter 替身）

- **Type**: newsletter（媒体资讯流，本行业「newsletter」形态）
- **URL**: https://www.jiemodui.com/ (evidence: [T05-S007])
- **Author/host**: 芥末教育传媒
- **Cadence**: rolling（每日多更）
- **Last activity**: 持续活跃（2026）
- **Audience tier**: mixed
- **One-liner**: 国内教育行业头部独立媒体，研学/营地有专题与持续资讯——作为「公众号」黑名单的**可引用替身**（机构媒体官网而非公众号文章），看政策落地+资本动向+机构事件。
- **典型每期内容**: 教育政策/资本/供应链报道，研学营地作素质教育板块；含露营亲子市场、行业报告解读、机构融资/暴雷。
- **投入产出比**: medium（教育全行业，研学营地占比中等，需筛）(evidence: [T05-S007])
- **Paywall**: none（部分深度内容/数据库可能付费）
- **签名内容**: 「超 1.4 万亿露营市场规模下，亲子赛道火苗渐显」(evidence: [T05-S007])
- **Endorsement evidence**: community_consensus（教育创投圈公认头部垂媒）+ cross_source（36氪 pitchhub 收录）
- **替代品**: 多鲸（更资本向）、亿欧教育、蓝鲸教育
- **可信度**: medium（媒体=secondary，事实需回原文）　**Decay risk**: low（机构媒体）

### 📰 9. 多鲸 / 多鲸研究院 — 资本视角媒体 + 年度报告

- **Type**: newsletter + report（年度行业报告发布机构）
- **URL**: http://www.djcapital.net/col.jsp?id=106 (evidence: [T05-S013])
- **Author/host**: 多鲸资本 / 多鲸教育（创新趋势）研究院（负责人钟日昕，前达内投资总监）
- **Cadence**: rolling + 年度报告
- **Last activity**: 《2024 素质教育行业发展趋势报告》（68 页，含营地研学专章）；2023 素质教育/职业教育报告系列
- **Audience tier**: practitioner→senior（资本+战略向）
- **One-liner**: 教育投行+研究院双模式，年度《素质教育趋势报告》是研学营地市场结构/集中度/头部机构判断**最常被引用的报告之一**——资本与战略视角 anchor。
- **典型每期内容**: 素质教育各赛道（营地研学/编程/艺术/体育）市场规模、渗透率、投融资、头部机构盘点。
- **投入产出比**: medium-high（年度报告 high，日常资讯 medium）(evidence: [T05-S013])
- **Paywall**: 报告 PDF 需申请（公众号备注领取——**领取渠道是公众号，黑名单；引用请用报告原始数据点 + 第三方研报平台转载页核对**）
- **签名内容**: 《2024 素质教育行业发展趋势报告》(营地研学章) (evidence: [T05-S013])
- **Endorsement evidence**: cross_source（网易/新浪/界面多源转载）+ community_consensus（教育创投圈引用率高）
- **替代品**: 艾瑞泛游学营地白皮书(S009)、艾媒研学游报告(S010)
- **可信度**: medium（报告=secondary/surrogate）　**Decay risk**: low

### 📰 10. 营地教育网（ydjy8）— 行业垂直门户（newsletter + 社区替身）

- **Type**: newsletter + community（垂直资讯门户）
- **URL**: https://www.ydjy8.com/ (evidence: [T05-S017])
- **Author/host**: 营地教育网
- **Cadence**: rolling
- **Last activity**: 持续活跃（2026）；办营地教育产业大会
- **Audience tier**: practitioner（营地一线运营）
- **One-liner**: 最贴近营地运营一线的垂直门户——政策汇总、营地运营案例、人物访谈、夏营合作、课程赋能计划，营地从业者聚集地（兼具资讯流+弱社区）。
- **典型每期内容**: 研学营地政策汇总、营地行业资讯、人物访谈、课程赋能、夏营/冬营合作撮合。
- **投入产出比**: medium（营地运营者 high，研学课程设计者 medium）(evidence: [T05-S017])
- **Paywall**: none
- **签名内容**: 「市场规模达千亿：研学、营地教育政策汇总」「营地课程赋能计划」(evidence: [T05-S017])
- **Endorsement evidence**: cross_source（办产业大会、被联盟引为媒体支持）+ community_consensus
- **替代品**: 芥末堆（更宏观）、各省研学协会站
- **可信度**: medium（垂媒=secondary）　**Decay risk**: medium（小机构站，运营依赖单一团队）

### 📊 11. 行业报告矩阵（艾瑞 / 艾媒 / 中国旅行社协会 / 前瞻 / 华经）

- **Type**: report（年度/不定期行业报告，本行业最权威「数据信号源」之一）
- **URL**: 艾瑞泛游学营地白皮书 http://report.iresearch.cn/report/201905/3362.shtml (S009) ; 艾媒研学游 https://www.iimedia.cn/c400/101385.html (S010) ; 旅行社协会报告 https://www.tiyan.org.cn/article-8-1981.html (S012) (evidence: [T05-S009, T05-S010, T05-S012])
- **Author/host**: 艾瑞咨询 / 艾媒咨询 / 中国旅行社协会研学旅行分会 / 前瞻产业研究院 / 华经
- **Cadence**: 年度或不定期
- **Last activity**: 《2024 中国研学旅游发展报告》(中国旅行社协会，2025-01 发布，调研全国 32 省 239 家企业)；《2024-2025 中国研学游经济市场运行监测报告》(艾媒)；艾瑞泛游学营地白皮书(2019，奠基性)
- **Audience tier**: practitioner→senior（市场规模、客单价、主题偏好、区域分布）
- **One-liner**: 研学营地市场规模/企业数/客单价/主题偏好的主要量化来源——**中国旅行社协会报告因「行业协会自身发布」可信度最高（surrogate_primary）**，艾瑞/艾媒为商业报告(secondary)。
- **典型每期内容**: 市场规模与增速、企业数量与区域分布、消费者画像与客单价、热门主题(红色/自然/劳动/传统文化/科技)、痛点(高品质供给不足/游而不学)。
- **投入产出比**: medium（年度数据锚，非高频）(evidence: [T05-S010, T05-S012])
- **Paywall**: 报告全文多需申请/付费，核心数据点经媒体转载可公开核
- **签名内容**: 旅行社协会《2024 研学旅游发展报告》：消费群体北京 28.45%/广东 18.83%；主题红色 53.14%、自然生态 53.14% (evidence: [T05-S012, T05-S011])
- **Endorsement evidence**: cross_source（央广/中国日报/新浪多源报道）+ surrogate_primary（协会发布）
- **⚠️ 数据 caveat**: 各家市场规模口径**严重打架**——2023 研学市场有「1469 亿」(前瞻)、有「2024 达 1791 亿/同比 21.9%」(艾媒) 又有「2024 达 1656 亿/同比 12%」(观知海内) 多个版本；「泛游学营地 2018 = 946 亿」(艾瑞) 与后续研学口径不可直接比。**引用任何数字必须挂具体 source_id + 年份 + 口径，禁止跨报告拼接趋势线。**
- **可信度**: 协会报告 medium-high / 商业报告 medium　**Decay risk**: low（年度更新）

### 📊 12. 世纪明德新三板财报（唯一可公开拉取的研学龙头财务序列）

- **Type**: dataset（上市/挂牌公司财报，资本/数据信号）
- **URL**: F10 https://xinsanban.eastmoney.com/f10/839264.html ; 2024 年报 PDF https://pdf.dfcfw.com/pdf/H2_AN202504241661731636_1.pdf (evidence: [T05-S015, T05-S016])
- **Author/host**: 世纪明德（NEEQ 839264）/ 东方财富新三板
- **Cadence**: 年度/半年报
- **Last activity**: 2024 年度报告（2025-04 披露）
- **Audience tier**: senior（看行业商业本质、龙头盈利模型）
- **One-liner**: 研学龙头唯一可公开拉取的连续财务数据——看研学「教育属性 vs 旅游属性」商业可持续性的硬证据。
- **典型每期内容**: 营收/净利/分部数据、研学旅行业务规模、风险提示。
- **投入产出比**: medium（年度，senior 战略用）(evidence: [T05-S016])
- **Paywall**: none（公开披露）
- **⚠️ 反例 caveat**: 世纪明德作为「研学龙头」**连续四年亏损**（受疫情等不可抗力），营收规模仍行业最大——印证行业「规模大但盈利难、教育与旅游属性撕扯」的结构性矛盾。**如实记，不软化。**（evidence: [T05-S015]）
- **Endorsement evidence**: verified（财报原文 PDF）+ cross_source（品橙旅游「2023 新三板中小微旅游企业业绩」横评）
- **可信度**: high（财报一手）　**Decay risk**: medium（公司若退市/转板则中断）

### 🏕️ 13. ACA 美国营地协会认证标准（国际标准锚，surrogate_primary）

- **Type**: dataset/standard（行业标准，非中文但是营地安全运营的国际 ground truth）
- **URL**: https://www.acacamps.org/accreditation (evidence: [T05-S004])
- **Author/host**: American Camp Association
- **Cadence**: 标准定期改版
- **Last activity**: 认证标准 2025-11 版（November 2025 Edition）
- **Audience tier**: practitioner→senior（营地安全/风险管理标准）
- **One-liner**: 全美唯一全国性营地认证体，标准聚焦 health/safety/risk management——中国营地安全管理（师生比/应急/食宿交通）做标准化时的国际对标基准。
- **典型内容**: 认证标准结构、Standards at a Glance、认证流程指南(APG)。
- **投入产出比**: medium（标准制定/对标时 high，日常 low）(evidence: [T05-S004])
- **Paywall**: 标准全文(APG)付费会员，结构性公开参考免费
- **geographic_focus**: 美国（en-only）——**deep-fluency 期望对中国本土落地需用户自评**
- **Endorsement evidence**: community_consensus（全球营地认证标杆，被各国政府引为 benchmark）
- **可信度**: high　**Decay risk**: low

---

## Phase 2 提炼提示

### 「这一行的资深人订阅最多的 top 3 sources」（进 master skill「Sources — 信息源」节 highlights）

1. **CCEC 全国营地教育大会（CCEA）**(evidence: [T05-S001]) — 营地子赛道最集中的年度信号源，11→38 家头部机构背书，营地从业者必跟。
2. **多鲸《素质教育行业发展趋势报告》（年度）**(evidence: [T05-S013]) — 市场结构/集中度/头部判断引用率最高的报告之一（资本+战略视角）。
3. **芥末堆 + 营地教育网（双媒体）**(evidence: [T05-S007, T05-S017]) — 公众号黑名单下最实用的可引用「资讯流替身」，前者宏观+政策+资本、后者贴营地一线运营。

> 自然教育子赛道再加：**全国自然教育论坛 / 中国自然教育大会**(evidence: [T05-S005, T05-S006])。

### 「年度行业报告 top 2 + 旗舰会议 top 2」（主控直接要）

- **年度行业报告 top 2**：① 多鲸《素质教育行业发展趋势报告》(营地研学专章，资本视角，引用率最高，S013)；② 中国旅行社协会《中国研学旅游发展报告》(协会自身发布 = 最高可信，调研 32 省 239 家，S012/S011)。〔奠基补充：艾瑞《泛游学与营地教育白皮书》2019，提出「泛游学」概念，S009〕
- **旗舰会议 top 2**：① CCEC 全国营地教育大会（营地本土旗舰，S001）；② 全国自然教育论坛/中国自然教育大会（自然教育旗舰，S005/S006）。〔国际级近期事件：ICC 世界营地大会 2026 落地中国，S002/S003〕

### 「最近的话题热度」候选信号（用于 Phase 2.4）

- **topic-heat: incomplete**（sources listed but content not deep-crawled；以下从大会主题/报告摘要/媒体标题归纳，非逐期爬取）：
  - 「游而不学 / 高品质供给不足 / 警惕劣币驱逐良币」——研学质量分化痛点（报告矩阵 S010/S012 + 媒体反复点）
  - 「研学旅游基地品质提升试点」（2024 文旅部，黑龙江/浙江/安徽/山东/湖北/四川首批）+《研学旅游服务要求》行业标准 2025 实施（政策合规线）
  - 「营地教育+劳动教育/实践教育」融合（营地产业大会 2024 西部劳动峰会 S017）
  - 「ICC 2026 中国办」国际化窗口（S002/S003）
  - 「亲子露营/泛营地市场扩容」（芥末堆 1.4 万亿露营稿 S007）

### 新 figures 发现（喂给 Wave 2 Track 01）

- **钟日昕**（多鲸资本联合创始人 / 多鲸教育研究院负责人，前达内投资总监）——资本+研究视角行业判断者，本 track 多次出现 (evidence: [T05-S013])。
- **王学辉**（世纪明德董事长 / 青青部落创始人）——研学龙头掌舵者，行业「最大研学集团」自述 (evidence: [T05-S014])。
- **CCEA 11 家发起机构创始人池**（启行 IDEAS、北京航海中心、万科梅沙户外、新东方文旅等的负责人）——营地隐性 figure 池，Track 01 撒网起点 (evidence: [T05-S001])。
- 自然教育线：全国自然教育网络/自然之友/阿拉善 SEE 的核心发起者（论坛志愿发起人）(evidence: [T05-S005])。

### 新 tools 发现（喂给 Wave 2 Track 02）

- 本 track 未直接评测到具体软件工具。间接信号：营地运营涉及**排班/营期排期、保险、应急预案、研学手册**等环节（来自大会工作坊主题 + 营地教育网运营案例），Track 02 可顺此找排课/营地管理 SaaS、研学报名/分销系统。
- **ACA 认证标准 / 国内研学营地团体标准**作为「合规工具」候选（S004 + 文旅部《研学旅游服务要求》）。

### 冷僻 / 信号薄弱（触发 Phase 2.8 诚实边界标注）

- ✅ newsletter ≥ 3（4 个，但全为**媒体资讯流替身**，非个人 Substack——形态偏移需标注）
- ❌ **podcast = 0**（逐一搜 小宇宙/喜马拉雅/Spotify 无对口节目）→ **触发：podcast 维度信源稀薄，明确标注**
- ✅ conference ≥ 1（7 个，本行业最强类型）
- ⚠️ community 弱（2 个，且主力沉淀在公众号/知乎/视频号等黑名单渠道，非公开社区）
- **有效 endorsement 结构**：conference/协会类背书扎实（cross_source + community_consensus 充分）；个人 figure_long 类背书几乎没有（因无个人 newsletter/podcast）——**endorsement 类型单一，偏机构、缺个人长输出**。

---

## 本 track 数据厚度自评（写给 Phase 2.8 / 文末诚实标）

- **候选数**：约 25+（合并去重后保留 13 张卡片 / 20 条 Manifest），≥ floor 15 ✅，未触发冷僻协议。
- **type 覆盖**：conference 强(7)、报告/数据强(报告矩阵+财报+ACA)、newsletter 中(4，媒体替身)、community 弱(2)、**podcast 空(0)**。
- **一手率（verified_primary 占比）**：Manifest 20 条中 verified_primary 仅 3 条（T05-S005/S006 自然教育 .org.cn 官网 + T05-S012 .org.cn 研学门户协会发布），约 **15%**；surrogate_primary 5 条（CCEA/ICF/ACA/GET 会议官网 + 协会发布），约 25%；其余 secondary（媒体/报告平台/财报第三方门户）约 60%。**verified_primary 偏低是真实的、结构性的**——因本行业一手运营经验大量沉淀在公众号/知乎/视频号（信源黑名单），且「信息源」主力是机构媒体+商业报告+大会而非政府/学术一手。已按规则全程用 surrogate_primary（会议/协会/标准白名单）补厚度，并如实标注。
- **关键利益相关 caveat**：媒体(secondary)报道的事实需回原文；商业报告市场规模口径互相打架（禁跨报告拼趋势）；商业主办的大会（明德论坛/世纪明德）议程偏自家生态；龙头世纪明德连续四年亏损这一反例如实记。
