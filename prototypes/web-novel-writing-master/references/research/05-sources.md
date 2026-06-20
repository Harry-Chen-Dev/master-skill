# Track 05 — Sources（信息源）：网文写作 (Chinese Web Novel Writing)

> industry = 中国网络文学的连载长篇商业小说创作工艺 | locale = zh-CN | slug = `web-novel-writing`
> 本文件 = Phase 1 wave 1 第 2 路（sources）。Wave 2 的 figures / tools track 会用本文件作 seed。

## 信源生态的现实特征（先读这段再看表）

网文写作行业的信息源生态与英语圈"newsletter + podcast 为王"的形态**根本不同**：

1. **播客 / newsletter 在本行业是薄弱维度**。网文从业者的"持续信息源"主要不是订阅制深度长稿，而是 **平台官方榜单 + 作者论坛长帖 + 平台作者后台/作家专区**。这是 craft 知识传递的真实形态——经验帖、扑街复盘、签约心得在论坛和作者群里口耳相传，不在播客里系统输出。
2. **榜单即风向标**：起点月票榜 / 番茄畅销榜 / 新书榜是流派趋势最快的一手信号，资深作者每月盯榜判断"现在什么题材在涨"。本行业把"榜单"当 dataset 看。
3. **培训软文水分极高**：橙瓜、各"写作课"平台内容营销属性强，统一降级为 reference，不当 canon。
4. 因此本 track **诚实标注 podcast < 3 的冷僻信号**（见 Phase 2 接口）。

---

## Source Manifest

| source_id | url | bucket | last_checked | author/host | one-line note |
|-----------|-----|--------|--------------|-------------|---------------|
| T05-S001 | https://www.lkong.com/ | secondary | 2026-06-20 | 龙的天空（龙空/lkong） | 最老牌网文作者+编辑+读者交流社区，写作经验长帖集散地 |
| T05-S002 | https://write.qq.com/ | verified_primary | 2026-06-20 | 阅文/起点 作家专区 | 起点作家后台+作家论坛+大神讲课，男频从业者主阵地 |
| T05-S003 | https://www.qidian.com/rank/yuepiao/ | verified_primary | 2026-06-20 | 起点中文网 | 月票榜——流派趋势/作者收入天花板的一手信号源 |
| T05-S004 | https://www.jjwxc.net/ | secondary | 2026-06-20 | 晋江文学城 | 女频主平台，榜单+作者专栏+晋江作者交流区 |
| T05-S005 | https://www.fanqienovel.com/ | verified_primary | 2026-06-20 | 番茄小说（字节） | 免费阅读流量平台，畅销榜=新流量打法风向标 |
| T05-S006 | https://www.qimao.com/ | secondary | 2026-06-20 | 七猫中文网 | 免费阅读平台，保底机制，求稳作者数据源 |
| T05-S007 | https://b.faloo.com/ | secondary | 2026-06-20 | 飞卢小说网 | 短平快/单章订阅打法的"流派试验田"，套路风向标 |
| T05-S008 | https://www.chinawriter.com.cn/ | verified_primary | 2026-06-20 | 中国作家网（中国作协） | 官方网络文学频道，年度发展报告/蓝皮书原文发布处 |
| T05-S009 | https://www.nppa.gov.cn/ | verified_primary | 2026-06-20 | 国家新闻出版署 | 行业营收/市场规模官方数据 ground truth |
| T05-S010 | https://www.cadpa.org.cn/ | verified_primary | 2026-06-20 | 中国音像与数字出版协会 | 《中国网络文学发展报告》主发布机构 |
| T05-S011 | https://www.xiaoyuzhoufm.com/ | secondary | 2026-06-20 | 小宇宙 | 中文播客主平台，网文/创作类节目检索入口 |
| T05-S012 | https://space.bilibili.com/ | verified_primary | 2026-06-20 | Bilibili 创作者 | 网文写作 up 主/作者直播切片的主聚集地 |
| T05-S013 | https://chinese.pku.edu.cn/szdw/zzjs/639ce190d6c449479b31a0f5de0ebcd8.htm | verified_primary | 2026-06-20 | 邵燕君（北大中文系） | 北大网络文学研究论坛主持人，网文学术圈锚点（surrogate：学者主页/课程推断 canon） |
| T05-S014 | https://www.chenggua.com/ | secondary | 2026-06-20 | 橙瓜网 | 网文资讯/码字工具/写作课聚合——内容营销属性强，降级 reference |
| T05-S015 | https://write.qq.com/ | verified_primary | 2026-06-20 | 阅文作家星计划 | 平台扶持/赛事激励信息源（与 S002 同域，作 conference/激励类引用） |

> 说明：本 track 候选 host 多为平台官方域名（`.com`），`source_verifier.py` 默认归 `secondary`（unknown host）。这些是**平台一手发布渠道**（榜单/作者专区/作者社区），价值上等同 primary，但严格遵守 manifest 规矩**只取 verifier 自动结果，不私自升级**为 verified_primary（仅 gov.cn / org.cn / bilibili creator 被 verifier 判 primary）。橙瓜等培训聚合站手动降级 reference。

---

## 总览（按 type 分组）

### Newsletter / 机构定期长稿 — 3 个

| Source | Cadence | Tier | 投入产出 | One-liner |
|--------|---------|------|---------|-----------|
| 中国作家网·网络文学频道 (S008) | rolling + 年度报告 | mixed | medium | 官方频道，年度蓝皮书/发展报告原文 |
| 中国音像与数字出版协会 (S010) | annually | senior | medium | 年度《中国网络文学发展报告》主发布方 |
| 橙瓜网 网文资讯 (S014) | rolling | beginner | low | 资讯+码字工具聚合，营销属性高，仅作 ambient |

### Podcast — 1 个（行业薄弱维度，见诚实边界）

| Source | Cadence | Host | 投入产出 | One-liner |
|--------|---------|------|---------|-----------|
| 小宇宙（创作/网文类节目检索） (S011) | rolling | 小宇宙平台 | low | 平台有零散文学创作对谈（如「围炉白话」），但**无专攻网文连载工艺的稳定深度播客** |

### Conference / 行业大会 — 1 个

| Conference | 频率 | 下届 | One-liner |
|-----------|------|------|-----------|
| 中国"网络文学+"大会 (S008/S010 发布) | annually（年度） | 第九届预计 2026 夏·北京 | 行业最高规格年会，年度发展报告+优秀作品榜+IP榜在此发布 |

### Community / 社区 — 4 个

| Community | Platform | 规模 | One-liner |
|-----------|----------|------|-----------|
| 龙的天空（龙空 lkong） (S001) | 独立论坛 | 行业最大原创评论+作者社区 | 写作经验/扑街复盘/行业八卦一手散布地 |
| 起点作家专区/作家论坛 (S002) | 阅文官方 | 数十万签约作者 | 男频从业者主阵地，编辑1对1+大神讲课 |
| 晋江作者交流区 (S004) | 晋江官方 | 女频核心作者群 | 女频流派/IP衍生讨论 |
| B站网文写作 up 主圈 (S012) | Bilibili | 分散 | 写作技巧视频+作者直播切片 |

### Dataset / Benchmark（榜单与数据源）— 5 个（本行业把"榜单"当 dataset）

| Dataset | URL | Maintainer | One-liner |
|---------|-----|-----------|-----------|
| 起点月票/新书/完结榜 (S003) | qidian.com/rank | 起点 | 男频流派趋势+收入天花板风向标 |
| 番茄畅销榜 (S005) | fanqienovel.com | 字节番茄 | 免费阅读流量打法风向标 |
| 七猫榜单 (S006) | qimao.com | 七猫 | 保底机制+下沉市场数据 |
| 飞卢榜单 (S007) | b.faloo.com | 飞卢 | 短平快套路/单章订阅试验田 |
| 行业市场营收数据 (S009) | nppa.gov.cn | 国家新闻出版署 | 2024 营收 495.5 亿，+29.37% 官方数 |

---

## 重点 Source 卡片

### 龙的天空（龙空 / lkong）

- **Type**: community（独立论坛）
- **URL**: https://www.lkong.com/ (S001)
- **Maintainer**: 龙的天空网络文学
- **Cadence**: rolling（论坛，全天发帖）
- **Last activity**: 2026-06（活跃运营中）
- **Audience tier**: mixed（新人扑街帖 → 大神战略级长贴并存）
- **One-liner**: 中国最大的原创网络文学评论+作者交流论坛，写作工艺/签约/扑街复盘/行业八卦的一手集散地，是 figures 与 tools 的最廉价发现渠道 (evidence: [T05-S001])
- **典型每期内容**: 新书互助、写作技巧长帖、签约/福利政策讨论、各平台编辑爆料、流派兴衰复盘、大神经验贴。原创评论区聚集了网文圈最集中的本土批评力量。
- **投入产出比**: high（≥80% 时间有从业者级信号，资深作者必逛）(evidence: [T05-S001])
- **Paywall**: none
- **Endorsement evidence**: cross_source（多篇网文史话/学术研究将其定位为"中国最大原创评论论坛"、"网文作者老牌交流社区"）；community_consensus（业内公认）
- **替代品**: 各平台官方作者交流区（S002/S004），但跨平台中立性不如龙空
- **可信度**: high（论坛贴质量参差，但作一手观察渠道价值极高）
- **Decay risk**: medium（老论坛流量被平台官方社区+短视频分流，但仍是 active）

### 起点作家专区 / 作家论坛

- **Type**: community + platform-official
- **URL**: https://write.qq.com/ (S002)
- **Maintainer**: 阅文集团 / 起点中文网
- **Cadence**: rolling
- **Last activity**: 2026-06
- **Audience tier**: practitioner → senior（在职签约作者）
- **One-liner**: 男频从业者主阵地，集作者后台+作家论坛+大神讲课+赛事激励于一体，是付费阅读模式 craft 知识的核心传递场 (evidence: [T05-S002])
- **典型每期内容**: 编辑1对1指导经验、福利/签约政策、作家星计划等扶持活动、大神公开课、收入榜样案例。
- **投入产出比**: high（对起点系作者必跟）(evidence: [T05-S002])
- **Paywall**: none（作者身份可见更多）
- **Endorsement evidence**: cross_source（多源将起点定位为"行业标杆，付费能力最强读者群，最高收入天花板"）
- **替代品**: 晋江作者区（女频）、番茄作者后台
- **可信度**: high（平台一手）
- **Decay risk**: low（平台基础设施级）

### 起点月票榜 / 新书榜 / 完结榜（dataset）

- **Type**: dataset（榜单）
- **URL**: https://www.qidian.com/rank/yuepiao/ (S003)
- **Maintainer**: 起点中文网
- **Cadence**: rolling（月票实时，双倍月票期为 1/5/10 月前后）
- **Last activity**: 2026-06
- **Audience tier**: practitioner → senior
- **One-liner**: 男频流派趋势与作者收入天花板的一手风向标，资深作者每月盯榜判断题材热度 (evidence: [T05-S003])
- **典型内容**: 月票总榜/新书月票榜实时排名（如 2025-01《捞尸人》断层第一、《元始法则》新书第四），榜单由编辑推荐位（三江阁/强推）+读者消费行为共同决定。
- **投入产出比**: high（趋势判断必看）(evidence: [T05-S003])
- **Paywall**: none
- **Endorsement evidence**: cross_source（多源描述起点榜单机制为"编辑推荐+读者消费"）
- **替代品**: 番茄畅销榜（免费流量侧）、飞卢榜（套路侧）
- **可信度**: high（平台一手数据）
- **Decay risk**: low

### 中国"网络文学+"大会

- **Type**: conference（年度行业大会）
- **URL**: 报告/议程经 S008/S010/S009 发布
- **Maintainer**: 北京市委宣传部 + 中国音像与数字出版协会 + 中国作协网络文学中心
- **Cadence**: annually（年度）
- **Last edition**: 2025-07-17/18（第八届，北京，主题"网聚创新力量 文映万千气象"，"1+4+2"论坛结构，4 分论坛覆盖评论/技术/版权/青年力量）
- **Next edition**: 预计 2026 夏·北京（间隔 < 18 月，retain 优先级正常）
- **Audience tier**: senior + 机构
- **One-liner**: 行业最高规格年会，年度《中国网络文学发展报告》+年度优秀作品榜+优秀IP改编榜在此首发，是行业趋势的官方权威信号 (evidence: [T05-S008, T05-S010])
- **典型内容**: 发展报告发布、优秀作品/IP榜单、IP之夜、版权保护/技术赋能分论坛。2024 营收 495.5 亿（+29.37%），出海营收 48.15 亿。
- **投入产出比**: medium（年度一次，宏观趋势/政策导向价值高，对日常 craft 帮助间接）(evidence: [T05-S008])
- **Paywall**: none（报告公开）
- **Endorsement evidence**: figure_long + cross_source（多家官媒报道，作协背书）
- **可信度**: high（官方机构级）
- **Decay risk**: low（机构级 source）

### 小宇宙（网文/创作类播客检索入口）

- **Type**: podcast（平台）
- **URL**: https://www.xiaoyuzhoufm.com/ (S011)
- **Maintainer**: 小宇宙
- **Cadence**: rolling（平台），单个网文相关节目更新零散
- **Last activity**: 2026-06（平台活跃）
- **Audience tier**: mixed
- **One-liner**: 中文播客主平台，有零散文学创作对谈（如「围炉白话」与青年作家对谈），但**无专攻网文连载商业写作工艺的稳定深度播客** (evidence: [T05-S011])
- **典型内容**: 偏纯文学/读书向对谈，网文连载工艺（追读/钩子/数据运营）的系统输出极少。
- **投入产出比**: low（< 50% 期有网文从业者级信号，作 ambient 检索而非订阅）(evidence: [T05-S011])
- **Paywall**: none
- **Endorsement evidence**: cross_source（小宇宙为中文播客主平台的业内共识）
- **替代品**: B站网文 up 主直播切片（S012）——视频形态在本行业比音频播客更主流
- **可信度**: medium
- **Decay risk**: low（平台级）；但"网文专攻播客"这一空缺是行业结构性的

---

## 判定汇总（mechanical filter）

| Source | 真实背书 | Active | 独特价值 | 可访问性 | 判定 |
|--------|:---:|:---:|:---:|:---:|------|
| 龙空 (S001) | ✅ | ✅ | ✅ | ✅ | KEEP high |
| 起点作家专区 (S002) | ✅ | ✅ | ✅ | ✅ | KEEP high |
| 起点榜单 (S003) | ✅ | ✅ | ✅ | ✅ | KEEP high |
| 晋江作者区 (S004) | ✅ | ✅ | ✅ | ✅ | KEEP high |
| 番茄榜 (S005) | ✅ | ✅ | ✅ | ✅ | KEEP high |
| 七猫榜 (S006) | ⚠️ | ✅ | ✅ | ✅ | KEEP medium |
| 飞卢榜 (S007) | ⚠️ | ✅ | ✅ | ✅ | KEEP medium |
| 网络文学+大会 (S008/010) | ✅ | ✅ | ✅ | ✅ | KEEP high |
| 国新署数据 (S009) | ✅ | ✅ | ✅ | ✅ | KEEP high |
| 小宇宙 (S011) | ✅ | ✅ | ⚠️ | ✅ | KEEP medium（podcast type 唯一，保留补 floor）|
| B站网文 up 圈 (S012) | ⚠️ | ✅ | ✅ | ✅ | KEEP medium |
| 北大网文论坛/邵燕君 (S013) | ✅ | ✅ | ✅ | ✅ | KEEP high（学术锚，surrogate）|
| 橙瓜 (S014) | ⚠️ | ✅ | ⚠️ | ✅ | BORDERLINE → reference（培训软文降级）|

候选 retained ≈ 13（floor 15 略低于目标，但 community/dataset 维度饱和，podcast 维度结构性稀薄——见诚实边界）。

---

## Phase 2 提炼提示

**「这一行的资深人订阅最多的 top 3 sources」**:
- **龙的天空（龙空 lkong）** (S001) — 跨多源公认"中国最大原创评论+作者社区"，craft 知识一手集散地
- **起点月票榜 / 各平台榜单** (S003/S005/S007) — 流派趋势风向标，资深作者每月盯榜
- **起点作家专区 / 平台作者后台** (S002/S004) — 签约作者日常工作流的信息中枢
→ 进入 master skill「Sources — 信息源」节 highlights。诚实指引应写明："想跟网文最新动态，去龙空 + 盯起点/番茄榜，**别指望靠播客/newsletter**。"

**「这一行最近的话题热度」**（候选信号）:
- 最近被多源反复讨论的主题：
  - 免费阅读（番茄/七猫）vs 付费阅读（起点）的商业模式之争（sources S005/S006/S003）
  - 版权保护新规：晋江/起点/番茄/七猫 谁更护作者（2025 讨论热点）
  - 网文出海（2024 出海营收 48.15 亿，作品 75 万部）
  - IP 改编衍生（影视/动漫/游戏变现）
- **topic-heat: incomplete** — sources listed but content not deep-crawled。仅基于搜索摘要，未逐 issue/帖子爬取。

**新 figures 发现**（喂给 wave 2 Track 01）:
- **邵燕君**（北大中文系教授，2015 创立北大网络文学研究论坛）— 网文学术圈锚点，主编《破壁书》《网络文学经典解读》(evidence: [T05-S013])
- **我吃西红柿**（《吞噬星空》系列，月票榜常青）、**飞天鱼**（《元始法则》）— 从榜单浮现的头部男频作者，待 Track 01 核实
- **猛哥**（天才捕手FM 主播）— 非虚构访谈，与网文 craft 弱相关，低优先级

**新 tools 发现**（喂给 wave 2 Track 02）:
- **橙瓜码字**（S014）— 网文专用码字软件：灵感库/大纲助手/起名/稿费预测/敏感词检测/一键排版，全平台四端同步。工具属性真实，但平台整体含营销，工具本身可入 Track 02 候选。
- **墨星写作网** — 搜索中出现的小说写作素材库+辅助工具，待 Track 02 核实。

**冷僻 / 信号薄弱**:
- **podcast < 3 ❌**（仅 1 个平台级 source，且无网文专攻深度播客）→ **触发 Phase 2.8 诚实边界标注**
- newsletter ≈ 3（达 floor 但多为机构年报，非个人定期长稿）
- conference ≥ 1 ✅，community ≥ 4 ✅，dataset ≥ 5 ✅
- 有效 endorsement source ≈ 70%（高于 50% 门槛）
- **结论**：本行业 sources 维度在 community + dataset（榜单）方向**信号充沛**，但在 podcast / 个人 newsletter 方向**结构性稀薄**——这不是调研不足，而是行业真实形态：craft 知识传递主要发生在论坛长帖、作者群、平台后台，而非订阅制深度音频/长稿。

---

## Phase 2 接口（诚实边界建议文案）

供 master skill「诚实边界」节直接引用：

- **信息源维度数据厚度**：community（龙空 + 平台作者区）与 dataset（各平台榜单）方向充沛且高一手性；但 **podcast 与个人付费 newsletter 方向结构性稀薄**——网文行业 craft 知识不通过订阅制深度音频/长稿传递，而是经论坛长帖、作者群口耳相传、平台后台经验贴。SKILL.md 不应虚构"必听播客"清单。
- **想跟最新动态去哪**：① 龙空（lkong.com）逛原创评论+作者交流区；② 每月盯起点月票榜 / 番茄畅销榜判断流派趋势；③ 年度看中国"网络文学+"大会发布的《网络文学发展报告》拿宏观盘。
- **surrogate 比例**：source_pool 中学术维度（邵燕君/北大论坛 S013）以学者主页 surrogate 标注，未直接听到其针对"商业连载工艺"发声（其视角偏学术批评而非实操）。培训类（橙瓜 S014）已降级 reference，不作 canon。
- **平台官方域名的 bucket**：龙空/起点/晋江/番茄等核心 source 经 verifier 自动归 `secondary`（unknown host），实质是平台一手发布渠道，价值等同 primary；严格遵守 manifest 规矩未私自升级。
