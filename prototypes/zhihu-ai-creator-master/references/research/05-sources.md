# Track 05 — Sources：知乎 AI 自媒体博主（持续追踪的活信息源）

> Research date: 2026-06-15 · Locale: zh-CN · 聚焦「在知乎做 AI 赛道、写文案 + 做内容」的博主要持续追的活源
> **诚实前置（两层）**：
> ① 和小红书姊妹行业一样，中文 AI 自媒体的一手深度方法论（实测/复盘/起号心法）绝大多数沉淀在**被黑名单的平台**（公众号 mp.weixin / **知乎站内长文本身** / CSDN）+ **付费社群**（知识星球 / 课程）。本 track 能合法收录的活源主要四类：知乎官方一手后台/规则；第三方数据/选题 SaaS（surrogate_primary）；头部博主的**非黑名单一手渠道**（GitHub / B站 / 个人站 / X / 即刻）；AI 资讯流。
> ② **知乎特有的尴尬**：知乎站内的回答/专栏长文是这个行业**最厚的内容载体**，但按黑名单规则「知乎作其他主题事实来源」要丢——**只有知乎官方页（创作中心/热榜/创作手册/规范公告）和博主本人的知乎主页可作 platform-native 收录（surrogate_primary）**。这意味着本 track 拿到的「深度方法论活源」比小红书还薄一层，因为连承载它的主平台都在黑名单边界上。
> ③ **第三方数据 SaaS 比小红书明显更薄**：小红书有新红/千瓜/灰豚一整条「专业商业数据」赛道；知乎**没有同等成熟的专业数据 SaaS**——新榜不主推知乎、千瓜/灰豚不覆盖知乎。知乎的「数据/选题」活源退化为「通用热榜聚合器 + 轻量热榜工具 + 采集器 + 官方后台」。如实记录，给 Phase 2.8。

## Source Manifest

| source_id | url | bucket | last_checked | author/host | note |
|-----------|-----|--------|--------------|-------------|------|
| T05-S006 | https://www.aicpb.com/news | surrogate_primary | 2026-06-15 | AI产品榜(李榜主) | vendor docs 每日 AI 早报(每日9:30更新),给 AI 赛道博主找选题 |
| T05-S007 | https://aihot.virxact.com/daily | surrogate_primary | 2026-06-15 | AI HOT 日报 | vendor docs 每日8点 AI 资讯digest(聚合13+源),AI 选题源;卡兹克 aihot skill 即取此源 |
| T05-S008 | https://www.newrank.cn/ | surrogate_primary | 2026-06-15 | 新榜 | vendor docs 新媒体数据/榜单平台。**注意:主推公众号/抖音/小红书,知乎覆盖弱**,只作通用热文/AI 文案工具用 |
| T05-S009 | https://www.46.la/tool/zhihu-hot-rank-tool | surrogate_primary | 2026-06-15 | 四六啦工具 | vendor docs 知乎实时热榜工具(前50条+热度排序,公开榜单接口),轻量免费选题监测 |
| T05-S010 | https://www.bazhuayu.com/helpcenter/docs/zhi-hu-jin-qi-re-bang-cai-ji | surrogate_primary | 2026-06-15 | 八爪鱼采集器 | vendor docs 知乎热榜采集教程(小时/日/周榜+热力值/各项增量字段,导出Excel),DIY 数据化选题 |
| T05-S011 | https://www.huxiu.com/ | secondary | 2026-06-15 | 虎嗅 | 科技商业深度媒体(实访 OK):AI 产品/AI 自媒体现象深稿(含卡兹克开源 skill 报道),按选题零散出稿 |
| T05-S012 | https://36kr.com/ | secondary | 2026-06-15 | 36氪 | AI 商业化/起号实录深稿(含知乎周源 AI 观点),无固定知乎-AI 专栏 |
| T05-S013 | https://www.latepost.com/ | secondary | 2026-06-15 | 晚点LatePost | 深度科技商业长报道(实访 OK):大厂 AI 战略/人物对话,深度高更新稳但非垂类 |
| T05-S014 | https://www.pingwest.com/ | secondary | 2026-06-15 | 品玩 PingWest | AI 博主/产品人物深稿,按选题零散出稿 |
| T05-S015 | https://www.geekpark.net/ | secondary | 2026-06-15 | 极客公园 | AI 产品/测评深稿,常转载头部博主长文 |
| T05-S016 | https://www.guizang.ai/ | surrogate_primary | 2026-06-15 | 歸藏(op7418) | 博主本人 AI 资讯站(实访 OK,快讯+深度+AIGC周刊),figure 一手 voice |
| T05-S017 | https://space.bilibili.com/1741797/ | verified_primary | 2026-06-15 | 歸藏的AI工具箱 | B站一手主页,工具测评一手视频(非黑名单发声渠道) |
| T05-S018 | https://github.com/KKKKhazix/khazix-skills | verified_primary | 2026-06-15 | 数字生命卡兹克 | 顶流博主开源 AI Skills 合集:含 **khazix-writer(写长文/稿子风格 skill)** + hv-analysis(横纵分析法) + aihot,一手内容方法论(可拆) |
| T05-S019 | https://space.bilibili.com/313468110/ | verified_primary | 2026-06-15 | 数字生命卡兹克 | 卡兹克 B站一手主页(非黑名单一手渠道) |
| T05-S020 | https://github.com/hzwer | secondary | 2026-06-15 | hzwer(黄哲威,StepFun) | 知乎 AI 学术大V GitHub 主页,**WritingAIPaper(3.8k★) AI 论文写作方法论**,一手产出 |
| T05-S021 | https://github.com/hzwer/WritingAIPaper | verified_primary | 2026-06-15 | hzwer(黄哲威) | 3.8k★ AI 会议论文写作手册:找核心 idea/搭框架/写引言/提升可读性——学术系知乎 AI 博主直接相关一手方法论 |
| T05-S022 | https://www.huasheng.ai/insights/ai-content-trends-2025-2026/ | surrogate_primary | 2026-06-15 | 花叔(Alchain) | 博主个人站洞察栏(实访 OK):AI 自媒体趋势/方法论分析,figure 一手 voice(同时运营 B站/X/YouTube) |
| T05-S023 | https://www.okjike.com/ | reference | 2026-06-15 | 即刻 jike | 公开半社区,「AI 探索站」圈 11万+人(卡兹克等即刻碎片一手)。匿名可读受限+信号噪比低,仅作旁证不作核心追踪 |

> **黑名单已显式剔除并丢弃所有命中**：mp.weixin(公众号) / 百度 / CSDN / 简书 / 掘金 / 内容农场 / 无原文 AI 摘要站。
> **知乎特殊处理**：知乎站内的回答/专栏长文(zhuanlan.zhihu.com/p/... 等)作「AI/起号方法论事实来源」**一律丢弃**(命中黑名单「知乎作其他主题事实来源」);**仅**知乎官方功能页(创作中心 S001 / 创作手册 S002 / 热榜 S003 / 知学堂 S004 / 好物话题 S005)与博主本人知乎主页可作 platform-native artifact 收录(标 surrogate_primary/verified_primary + note)。
> **bucket 说明**：知乎官方功能页 + 博主本人 GitHub 仓库/B站空间 = verified_primary；数据/选题/AI 资讯 SaaS 官网 + 博主个人站 = surrogate_primary(vendor docs / figure voice)；行业媒体 = secondary；即刻(公开但受限) = reference。
> **403 说明**：S001/S003(zhihu.com/creator、/billboard)匿名 WebFetch 返回 403 Forbidden(知乎反爬,需登录态),**非 dead**——URL 由搜索结果交叉确认为现行官方入口,真实从业者登录后即可用。S002/S005(/knowledge-plan/manual、/topic/...)匿名可访,作存活锚点。
> **本批 dead 源：0 条**(所有非 403 源均 WebFetch 实访 200;403 为反爬不计 dead)。
> **figure 一手最厚处仍在黑名单**：卡兹克/歸藏核心爆文在公众号(黑名单);hzwer 等学术大V 核心内容在知乎站内长文(黑名单边界)——**故只收其 GitHub/B站/个人站等非黑名单渠道作 voice surrogate**。

---

## 总览（按 type 分组）

> 本行业 source 类型分布与「en 行业(newsletter/podcast/conference 三足鼎立)」**完全不同**,也比姊妹行业小红书更薄一档(知乎缺成熟专业数据 SaaS)。主力是「官方后台 + 热榜聚合/采集 + 博主非黑名单主页 + AI 资讯流」。以下按本 track 任务的 5 分类组织。

### ① 知乎官方一手 — 5 个
| Source | URL | Cadence | 一手 | 用途 / One-liner |
|--------|-----|---------|------|------------------|
| 创作中心 | T05-S001 | rolling(日) | 一手 | 唯一一手账号数据/内容分析/收益/创作权益(需登录,403 反爬) |
| 创作者手册 | T05-S002 | rolling | 一手 | 四形态创作 + 变现矩阵 + 新手选题/标题/传播官方指引 |
| 知乎热榜 | T05-S003 | rolling(实时) | 一手 | 官方选题热度第一现场(需登录,403 反爬) |
| 知学堂 | T05-S004 | rolling | 一手 | 官方学习/知识服务入口(最接近「创作者学院」) |
| 好物推荐话题/规则 | T05-S005 | rolling | 一手 | 带货/盐选会员购返佣合规第一现场(等级>4/极限词禁用等) |

> **AI 标识/社区规范**：知乎已按国家《人工智能生成合成内容标识办法》(2025-09-01 施行)更新用户协议要求显著标识 AI 生成内容,违者限流/下架。该规范的**权威 ground-truth 是国家网信办法规 + 知乎社区规范页**(社区规范公告页同在 zhihu.com 官方域,作 S001/S002 同源官方一手追踪;法规原文在网信办官网,作 reference)。

### ② 数据 / 选题平台（第三方 SaaS）— 4 个 · vendor docs
| Source | URL | Cadence | 一手 | 用途 / One-liner |
|--------|-----|---------|------|------------------|
| AI产品榜早报 | T05-S006 | daily(9:30) | 二手聚合 | 每日 AI 头条,AI 赛道快速选题(同小红书 track) |
| AI HOT 日报 | T05-S007 | daily(8:00) | 二手聚合 | 聚合13+源 AI digest,选题源;卡兹克 skill 直取 |
| 新榜 | T05-S008 | rolling(日) | 二手 | **知乎覆盖弱**;仅作通用热文榜 + AI 文案工具,非知乎专项数据 |
| 四六啦知乎热榜工具 | T05-S009 | rolling(实时) | 二手 | 知乎热榜前50+热度排序,公开接口轻量免费监测 |
| 八爪鱼知乎热榜采集 | T05-S010 | rolling | 二手 | DIY 采集小时/日/周榜+各项增量字段导出 Excel,数据化选题 |

> **诚实标注**：知乎**没有**小红书新红/千瓜/灰豚那样的专业商业数据 SaaS 赛道。本类活源退化为「通用热榜聚合/采集 + AI 资讯流」,专业度与可订阅性弱于小红书 track。

### ③ 行业媒体（深度长稿,secondary,按选题零散出稿）— 5 个
| Source | URL | Cadence | 一手 | 用途 / One-liner |
|--------|-----|---------|------|------------------|
| 虎嗅 | T05-S011 | 不定(无固定专栏) | 二手 | AI 自媒体现象深稿(卡兹克开源 skill 报道等) |
| 36氪 | T05-S012 | 不定 | 二手 | AI 商业化/起号实录(含周源 AI 观点) |
| 晚点LatePost | T05-S013 | 不定(更新稳/深度高) | 二手 | 大厂 AI 战略 + 人物对话长报道,深度最佳但非垂类 |
| 品玩 | T05-S014 | 不定 | 二手 | AI 博主/产品人物深稿 |
| 极客公园 | T05-S015 | 不定 | 二手 | AI 产品/测评深稿(常转载头部博主长文) |

> 五家均**无稳定「知乎 AI 内容/知乎商业化/AI 自媒体」专栏条线**,按选题命中零散出稿,不可订阅、无固定 cadence。

### ④ 头部博主非黑名单一手渠道（figure voice）— 7 个
| Source | URL | Cadence | 一手 | 用途 / One-liner |
|--------|-----|---------|------|------------------|
| 歸藏 AI 资讯站 | T05-S016 | weekly+(快讯/深度) | 一手 | 测评方法论 + 行业判断一手 voice + AIGC 周刊 |
| 歸藏 B站 | T05-S017 | 不定 | 一手 | 工具测评一手视频(空间 1741797) |
| 卡兹克 GitHub skills | T05-S018 | rolling | 一手 | **khazix-writer 写长文 skill** + 横纵分析法 + aihot,内容方法论可拆 |
| 卡兹克 B站 | T05-S019 | 不定 | 一手 | 顶流博主非黑名单一手渠道(空间 313468110) |
| hzwer GitHub | T05-S020 | rolling | 一手 | 知乎 AI 学术大V 一手代码/论文方法论产出 |
| hzwer WritingAIPaper | T05-S021 | rolling | 一手 | 3.8k★ AI 论文写作手册,学术系知乎博主直接相关 |
| 花叔个人站洞察 | T05-S022 | 不定 | 一手 | AI 自媒体趋势/方法论一手分析(同运营 B站/X/YT) |

> 知乎博主本人**知乎主页**(zhihu.com/people/...)亦可作 platform-native surrogate_primary,但本批未逐一锚定具名 URL(留 Wave 2 由 Track 01 figure 名单回填),因匿名 403 + 需先确权账号身份。

### ⑤ AI 赛道选题源（AI 资讯流,给博主找选题）— 见 ②(S006/S007)
| Source | URL | Cadence | 一手 | 用途 / One-liner |
|--------|-----|---------|------|------------------|
| AI产品榜早报 | T05-S006 | daily(9:30) | 二手 | 每日 AI 头条快速选题 |
| AI HOT 日报 | T05-S007 | daily(8:00) | 二手 | 高频聚合 AI 动态,抢首发时效 |

### Newsletter / Podcast / Conference / Community
- **Podcast**: **N/A** —— 无成规模的中文「知乎 AI 自媒体方法论」播客。最接近的是泛科技媒体播客(如「科技媒体这十年:36氪/虎嗅/品玩」单集)与卡兹克偶发嘉宾出镜,非稳定可追节目,不单列。**根因**:垂类太窄 + 一手生态在文字平台(知乎/公众号)沉淀,无音频化动力。
- **Conference**: **N/A** —— 无该垂类年度大会。最接近的是新榜大会(数据/新媒体侧,非知乎-AI 方法论导向)。**根因**:知乎自身无对标小红书 WILL 那样的创作者大会条线,AI 内容创作无独立行业会议。
- **Community**: 公开半社区仅**即刻「AI 探索站」**(T05-S023,11万+人,卡兹克等碎片一手),但匿名可读受限 + 信号噪比低,仅作旁证(reference)。核心一手社群(歸藏 AIGC 周刊圈 / 卡兹克知识星球 / 各 AI 起号付费群)均**付费+半封闭**,公开 URL 不稳/涉黑名单聚合,**不收录**。**根因**:深度方法论被作者刻意圈进付费墙变现。
- **Newsletter**: 中文该垂类的「newsletter」事实形态 = 公众号(黑名单) + **知乎专栏长文(黑名单边界)** + 个人站。合法可追的仅歸藏个人站(S016,含 AIGC 周刊) + 花叔个人站(S022) + AI 日报两家(S006/S007 准 newsletter)。**根因**:承载长文订阅的主平台(公众号/知乎)都在黑名单上。

---

## Phase 2 提炼提示

**「这一行的人最该常追的 top 5 活源」**（含频率,给 master skill「想跟最新动态去这几处」节）:
1. **知乎创作中心 + 热榜**(T05-S001/S003,日级/实时)——唯一一手账号数据 + 官方选题热度,**每条内容发布前后必看**(需登录;evidence: [T05-S001, T05-S003])。
2. **知乎热榜工具/采集(四六啦/八爪鱼)**(T05-S009/S010,实时/rolling)——**每次开写前**抓热榜+热度增量做数据化选题,补官方后台之外的监测(evidence: [T05-S009, T05-S010])。
3. **知乎创作者手册 + 好物/盐选规则**(T05-S002/S005,rolling)——**规则/变现/AI 标识变动时追**,平台一手 ground-truth(evidence: [T05-S002, T05-S005])。
4. **歸藏 AI 站 + 卡兹克 GitHub skills + hzwer WritingAIPaper**(T05-S016/S018/S021,周级+/rolling)——非黑名单一手方法论(测评/写长文 skill/论文写作),**按内容方向取一两个长期追**(evidence: [T05-S016, T05-S018, T05-S021])。
5. **AI产品榜早报 / AI HOT 日报**(T05-S006/S007,日级)——**每天扫一遍**给 AI 赛道找选题、抢首发时效(evidence: [T05-S006, T05-S007])。

**内容/选题真知识沉淀在哪（诚实定位）**:
- **一手数据 + 选题热度**:知乎官方后台/热榜(S001/S003) + 热榜工具/采集(S009/S010)——「写什么」的根;但知乎无专业商业数据 SaaS,数据化能力弱于小红书。
- **方法论/测评/复盘**:博主一手在 GitHub/B站/个人站(S016~S022)能拿**非黑名单**部分(尤其 khazix-writer 写长文 skill + WritingAIPaper 论文写作);但**最厚的方法论沉淀在公众号(黑名单)+ 知乎站内长文(黑名单边界)+ 付费星球**,本 track 拿不到,须 Phase 2.8 诚实标注。
- **合规 ground-truth**:知乎官方规则/手册(S002/S005) + 国家《AI 生成合成内容标识办法》(2025-09-01)——AI 标识是当前最硬的合规线。
- **AI 赛道前沿选题**:AI 资讯流(S006/S007) + 歸藏/卡兹克/花叔一手。

**媒体层厚薄诚实判断**:
- **比小红书更薄**。两点根因:① 与小红书共有的——中文「AI 自媒体(文案/内容制作)」无专门媒体条线(虎嗅/36氪/晚点/品玩/极客公园只在选题命中时零散出深稿,不可订阅、无固定 cadence);newsletter/podcast/conference/公开 community 四类基本空缺,因一手生态长在黑名单平台 + 付费社群。② **知乎独有的双重黑名单挤压**——知乎站内长文本身是这行最厚的内容载体却落在黑名单边界(只官方页/博主主页可收),且知乎**缺小红书新红/千瓜/灰豚级别的专业数据 SaaS**(新榜不主推知乎、千瓜灰豚不覆盖)。结果:本 track 真实重心被压到「官方后台 + 热榜聚合/采集 + 博主非黑名单主页 + AI 资讯流」,且数据层比小红书弱一档。

**新 figure 候选（喂 Wave 2 / Track 01 交叉确认）**:
- 歸藏(op7418)、卡兹克——已在 Track 01(姊妹行业);本 track 确认其非黑名单一手渠道在知乎赛道同样适用。
- **hzwer(黄哲威,StepFun,RepVGG/RIFE 作者)**——知乎 AI **学术系**大V,WritingAIPaper 3.8k★,**Track 01 若未收应补**(知乎 AI 赛道学术/干货流的代表,信号强)。
- **丁霄汉**(清华博士,RepVGG 作者,字节豆包,学术写作/审稿/CV)、**白小鱼**(上交,联邦学习转 LLM)、**王小惟 Weixun**(天大,多智能体 RL/RLHF)——搜索反复出现的知乎 AI 学术大V,**Track 01 候选**(学术系信号,需 Wave 2 锚定非黑名单一手 URL)。
- **花叔(Alchain)**——AI Native Coder/独立开发者,个人站 huasheng.ai 有 AI 自媒体趋势洞察,**Track 01 若未收应补**(content-creation 方法论方向)。

**新 tool 候选（喂 Wave 2 Track 02 / 交叉确认）**:
- **卡兹克开源 khazix-skills**(尤其 khazix-writer 写长文 skill、hv-analysis 横纵分析法、aihot)——**Skills/工作流类工具**,Track 02 若未单列应补(MIT 开源、直接是「怎么写长文」方法论)。
- **hzwer WritingAIPaper**——AI 论文写作手册,学术系知乎博主的「写作工具」,Track 02 候选。
- 四六啦知乎热榜工具 / 八爪鱼知乎热榜采集——知乎专项「热榜监测/采集」工具,Track 02 若未收应补(填知乎数据工具空白)。

**topic-heat**: `incomplete, sources listed but content not crawled` —— 仅抽检源的存活与定位,未系统爬每源最新 N 条标题做热度统计。低置信度观察:2026 上半年跨源反复出现的主题是 **「AI 标识新规(2025-09 施行)+ 平台限流」**(evidence: [S002, S005, 国家网信办法规]) 与 **「AI 内容从『聊天』转向『干活』、头部 AI 自媒体分化为教学/实验/深度分析三型」**(evidence: [S022 花叔洞察])。

**冷僻 / 信号薄弱**:
- newsletter < 3 合法(歸藏站 + 花叔站 + 2 家 AI 日报算准 newsletter)、podcast = 0(N/A)、conference = 0(N/A)、公开 community = 1 且受限(即刻,reference)——**4 个 type 触发薄弱信号**。
- 但「rolling 工具型活源」充足(官方 5 + 数据/选题 5 + 博主主页 7 + AI 资讯 2[与数据重叠] = ~17 个可追)。
- **结论 → Phase 2.8 诚实边界**:sources 维度「定期长稿型源」严重稀薄 + **知乎数据层比小红书更弱**。master skill「想跟最新动态」节应明确告诉用户:**追源 = 盯知乎创作中心/热榜 + 热榜工具 + 博主 GitHub/B站/个人站 + AI 日报**,并坦白「这行最深的方法论在你得自己关注的公众号/知乎付费专栏/付费星球里,且知乎站内长文本身就是大头——本 skill 不能替你订阅黑名单平台」。

---

## 质量自检
- [x] 候选/收录 ≥ 15(23 条 manifest,0 dead;有效活源 ~21,403 反爬 2 条仍属现行官方源)
- [x] 5 分类覆盖(官方5 / 数据选题5 / 行业媒体5 / 博主主页7 / 选题源2[与数据重叠])
- [x] 每条标 用途 + 更新频率(cadence) + 是否一手
- [x] 每源有 last_checked 日期(2026-06-15,agent 实访;403 标注反爬非 dead)
- [x] 商业平台 docs 标 surrogate_primary + note vendor docs;博主个人站标 surrogate_primary(figure voice);知乎主页/官方页标 platform-native
- [x] 黑名单零收录(公众号/百度/CSDN/简书/掘金命中即丢;**知乎站内长文作他题事实来源亦丢**,仅官方页/博主主页作 platform-native,已显式说明)
- [x] dead 源:0 条(403 为反爬不计 dead,已说明)
- [x] Phase 2 接口:top 5 + 知识沉淀定位 + 媒体层厚薄诚实判断 + 新 figure/tool 候选 + 冷僻信号
- [x] 媒体层厚薄诚实判断已写明(newsletter/podcast/conference/community 四类稀薄根因 + **知乎特有的双重黑名单挤压 + 数据 SaaS 比小红书更薄**两条独有根因)
