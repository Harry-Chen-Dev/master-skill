# Track 05 — Sources：小红书 AI 自媒体博主（持续追踪的活信息源）

> Research date: 2026-06-06 · Locale: zh-CN · 聚焦「文案 + 内容制作」博主要持续追的活源
> **诚实前置**：本行业的「专门媒体层」很薄。中文 AI 自媒体的一手深度内容（方法论、实测、复盘）绝大多数沉淀在**被黑名单的平台**（公众号 mp.weixin / 知乎 / CSDN）+ **付费社群**（知识星球、X 付费圈）。本 track 能合法收录的活源主要是三类：① 小红书官方一手后台/规则；② 第三方数据/选题 SaaS（surrogate_primary，vendor docs）；③ 头部博主的**非黑名单一手发声渠道**（B站空间 / 个人站 / GitHub / X）。行业媒体（36氪/虎嗅/品玩/极客公园/数英/亿邦）只能作 secondary 的「偶发深稿」，**没有稳定的「小红书 AI 自媒体」专栏条线**——是按选题零散出稿，不是持续 newsletter。

## Source Manifest

| source_id | url | bucket | last_checked | author/host | note |
|-----------|-----|--------|--------------|-------------|------|
| T05-S001 | https://creator.xiaohongshu.com/ | verified_primary | 2026-06-06 | 小红书官方 | 创作服务平台后台，唯一一手账号数据/笔记灵感/违规自查 |
| T05-S002 | https://creator.xiaohongshu.com/creator/college | verified_primary | 2026-06-06 | 小红书官方 | 创作学院/官方创作课 + 创作百科入口 |
| T05-S003 | https://creator.xiaohongshu.com/publish/publish | verified_primary | 2026-06-06 | 小红书官方 | 发布入口，发布时勾选 AI 标识/内容声明 |
| T05-S004 | https://pgy.xiaohongshu.com/help/home | verified_primary | 2026-06-06 | 小红书蒲公英 | 商单/合作官方平台帮助中心+规则，反推选题 |
| T05-S005 | https://xh.newrank.cn/ | surrogate_primary | 2026-06-06 | 新榜新红 | vendor docs 选题/热词/对标爆款数据平台(部分免费) |
| T05-S006 | https://www.qian-gua.com/ | surrogate_primary | 2026-06-06 | 千瓜数据 | vendor docs 历史数据深挖/热搜词排行(付费) |
| T05-S007 | https://www.chanxiaohong.com/ | dead | 2026-06-06 | 蝉妈妈蝉小红 | 2026-06-06 连接被拒+无法注册，疑停服，待替换 |
| T05-S008 | https://www.huitun.com/ | surrogate_primary | 2026-06-06 | 灰豚数据 | vendor docs 关键词抓笔记+热度曲线，千瓜平价替代 |
| T05-S009 | https://www.guizang.ai/ | surrogate_primary | 2026-06-06 | 歸藏(op7418) | 博主本人 AI 资讯站(快讯/深度)，figure 一手 voice |
| T05-S010 | https://space.bilibili.com/1741797/ | verified_primary | 2026-06-06 | 歸藏的AI工具箱 | B站一手主页，看工具测评一手作品 |
| T05-S011 | https://github.com/op7418 | secondary | 2026-06-06 | 歸藏(op7418) | 博主 GitHub(含 PPT Skill 等开源)，一手代码产出 |
| T05-S012 | https://space.bilibili.com/313468110/ | verified_primary | 2026-06-06 | 数字生命卡兹克 | 卡兹克 B站一手主页(非黑名单发声渠道) |
| T05-S013 | https://github.com/KKKKhazix/khazix-skills | verified_primary | 2026-06-06 | 数字生命卡兹克 | 卡兹克开源 AI Skills(14.9k★,MIT)，一手工作流 |
| T05-S014 | https://36kr.com/ | secondary | 2026-06-06 | 36氪 | 行业深稿(AI 起号实录等)，按选题零散出稿 |
| T05-S015 | https://www.huxiu.com/ | secondary | 2026-06-06 | 虎嗅 | AI 自媒体现象深稿+歸藏专栏聚合(m.huxiu.com/club/1044) |
| T05-S016 | https://www.pingwest.com/ | secondary | 2026-06-06 | 品玩 PingWest | AI 博主人物深稿(那珂/灵琪具名) |
| T05-S017 | https://www.geekpark.net/ | secondary | 2026-06-06 | 极客公园 | AI 产品/测评深稿(转载歸藏长文) |
| T05-S018 | https://www.digitaling.com/ | secondary | 2026-06-06 | 数英 digitaling | 营销/AI 涨粉拆解长稿 |
| T05-S019 | https://www.ebrun.com/ | secondary | 2026-06-06 | 亿邦动力 | 电商/平台政策条线(AI 标识新规等) |
| T05-S020 | https://www.aicpb.com/news | surrogate_primary | 2026-06-06 | AI产品榜 | vendor docs 每日AI早报(9:30更新)，给博主找 AI 选题 |
| T05-S021 | https://news.daheiai.com/ | surrogate_primary | 2026-06-06 | 大黑AI速报 | vendor docs 每4小时更新 AI 快讯，AI 赛道选题源 |

> 黑名单已显式剔除并丢弃所有命中：mp.weixin(公众号) / zhihu(知乎) / 百度 / CSDN / 简书 / 掘金 / 搜狐。歸藏一手最厚的「AIGC 周刊」与卡兹克核心爆文都在公众号(黑名单)——**故只收其 B站/个人站/GitHub/X 等非黑名单渠道作 voice surrogate**。
> bucket 说明：`creator/pgy.xiaohongshu.com`(平台一手) + `github.com 项目根` + `bilibili creator space` = verified_primary；数据/选题/AI资讯 SaaS 官网 = surrogate_primary(vendor docs)；博主本人个人站 = surrogate_primary(figure 一手 voice)；行业媒体 = secondary；`x.com` verifier 判 reference 故未单列收录(歸藏 X @op7418 仅作旁证)。
> `T05-S007 蝉小红` 标 `dead`：2026-06-06 WebFetch 连接被拒(ECONNREFUSED) + 多源称无法注册，与 02-tools 收录时状态不一致，**Phase 4 提示核实/替换为灰豚**。

---

## 总览（按 type 分组）

> 本行业 source 类型分布与典型「en 行业(newsletter/podcast/conference 三足鼎立)」**不同**：没有成规模的中文「小红书 AI 自媒体」podcast / conference / 公开 community。主力是「官方后台 + 数据平台 + 博主主页 + AI 资讯流」。以下按本 track 任务的 5 分类（官方 / 数据平台 / 行业媒体 / 博主主页 / 选题源）组织。

### 官方（小红书一手）— 4 个
| Source | URL | Cadence | 一手 | 用途 / One-liner |
|--------|-----|---------|------|------------------|
| 创作服务平台 | T05-S001 | rolling(日) | 一手 | 唯一一手账号数据 + 笔记灵感(每周五20点更新) + 违规自查 |
| 创作学院/创作课 | T05-S002 | rolling | 一手 | 官方教学课 + 创作百科，规则与玩法权威解释 |
| 发布/AI 标识入口 | T05-S003 | rolling | 一手 | 发布即勾 AI 标识，合规第一现场 |
| 蒲公英帮助中心 | T05-S004 | rolling | 一手 | 商单规则/流程，反推可做的种草选题方向 |

### 数据 / 选题平台（第三方 SaaS）— 4 个（含 1 dead）
| Source | URL | Cadence | 一手 | 用途 / One-liner |
|--------|-----|---------|------|------------------|
| 新红 | T05-S005 | rolling(日) | 二手 | 24 垂类榜 + 热词云 + 对标爆款，部分免费起步 |
| 千瓜 | T05-S006 | rolling(日) | 二手 | 历史数据深挖 + 热搜词排行(付费) |
| 灰豚 | T05-S008 | rolling(日) | 二手 | 关键词抓笔记 + 热度曲线，千瓜平价替代 |
| ~~蝉小红~~ | T05-S007 | — | — | **疑停服(dead)**，原用于蓝海词；用灰豚/新红替代 |

### 行业媒体（深度长稿，secondary，按选题零散出稿）— 6 个
| Source | URL | Cadence | 一手 | 用途 / One-liner |
|--------|-----|---------|------|------------------|
| 36氪 | T05-S014 | 不定(无固定专栏) | 二手 | 一手 AI 起号实录 + 平台治理边界深稿 |
| 虎嗅 | T05-S015 | 不定 | 二手 | AI 自媒体现象深稿 + 歸藏专栏聚合页 |
| 品玩 | T05-S016 | 不定 | 二手 | AI 博主人物深稿(那珂/灵琪具名) |
| 极客公园 | T05-S017 | 不定 | 二手 | 产品/测评深稿(转载歸藏长文) |
| 数英 | T05-S018 | 不定 | 二手 | 营销侧 AI 涨粉拆解 |
| 亿邦动力 | T05-S019 | 不定 | 二手 | 电商/平台政策条线(AI 标识新规等) |

### 博主主页（头部 figure 一手，非黑名单渠道）— 5 个
| Source | URL | Cadence | 一手 | 用途 / One-liner |
|--------|-----|---------|------|------------------|
| 歸藏 AI 资讯站 | T05-S009 | weekly+(快讯/深度) | 一手 | 博主本人站，测评方法论 + 行业判断一手 voice |
| 歸藏 B站 | T05-S010 | 不定 | 一手 | 工具测评一手视频(空间 1741797) |
| 歸藏 GitHub | T05-S011 | rolling | 一手 | 开源 PPT Skill 等，一手产出可拆 |
| 卡兹克 B站 | T05-S012 | 不定 | 一手 | 顶流博主非黑名单一手渠道(空间 313468110) |
| 卡兹克 AI Skills(GitHub) | T05-S013 | rolling | 一手 | 14.9k★ 开源他每天在用的 AI 工作流(MIT) |

### 选题源（AI 资讯流，给博主找 AI 赛道选题）— 2 个
| Source | URL | Cadence | 一手 | 用途 / One-liner |
|--------|-----|---------|------|------------------|
| AI产品榜 早报 | T05-S020 | daily(9:30) | 二手聚合 | 每日 AI 头条，AI 赛道博主快速选题 |
| 大黑AI速报 | T05-S021 | 每4小时 | 二手聚合 | 高频 AI 快讯，抢首发时效用 |

### Newsletter / Podcast / Conference / Community
- **Podcast**: N/A —— 无成规模的中文「小红书 AI 自媒体方法论」播客。卡兹克偶有播客嘉宾出镜(如 Apple Podcasts 单集)，但非稳定可追的节目，不单列。
- **Conference**: N/A —— 无该垂类年度大会。最接近的是小红书官方 WILL 商业大会/创作者大会(品牌侧为主)、新榜大会(数据侧)，均非「文案/内容制作」方法论导向，**信号薄，不作核心追踪源**。
- **Community**: 主力一手社群(歸藏 AIGC 周刊订阅圈、卡兹克知识星球、各 AI 起号付费群)均**付费 + 半封闭**，公开 URL 不稳定 / 涉黑名单聚合页，**不收录**。即刻(jike) AI 圈是少数公开半社区(卡兹克即刻主页一手碎片)，但平台命运绑定、信号噪比低，仅作旁证不单列。
- **Newsletter**: 中文该垂类的「newsletter」事实形态 = 公众号(黑名单) + 个人站。合法可追的仅歸藏个人站(T05-S009)；其余均落黑名单。

---

## Phase 2 提炼提示

**「这一行的人最该常追的 top 5 活源」**（含频率，给 master skill「想跟最新动态去这几处」节）:
1. **小红书创作服务平台**(T05-S001，日级 rolling，笔记灵感每周五20点更新)——唯一一手数据 + 选题 + 合规自查，**每条内容发布前后必看** (evidence: [T05-S001])。
2. **新红 / 千瓜(数据平台二选一)**(T05-S005/S006，日级)——**每次开写前**先查热搜/蓝海词 + 对标爆款，数据驱动选题 (evidence: [T05-S005, T05-S006])。
3. **小红书创作学院 + 蒲公英帮助中心**(T05-S002/S004，rolling)——**规则/玩法变动时追**，平台一手 ground-truth(尤其 AI 标识政策) (evidence: [T05-S002, T05-S004])。
4. **歸藏 AI 资讯站 + B站**(T05-S009/S010，周级+)——AI 工具测评方法论一手 voice，**每周追**抢工具/选题红利 (evidence: [T05-S009, T05-S010])。
5. **AI产品榜早报 / 大黑AI速报**(T05-S020/S021，日级/4h)——**每天扫一遍**给 AI 赛道找选题、抢首发时效 (evidence: [T05-S020, T05-S021])。

**内容/选题真知识沉淀在哪（诚实定位）**:
- **一手数据 + 选题灵感**：小红书官方后台(T05-S001) + 第三方数据平台(T05-S005/S006/S008)——这是「写什么」的根。
- **方法论/测评/复盘**：博主一手在 B站/个人站/GitHub(T05-S009~S013)能拿到**非黑名单**部分；但**最厚的方法论沉淀在公众号(黑名单)+ 付费社群**，本 track 拿不到，须 Phase 2.8 诚实标注。
- **合规 ground-truth**：小红书官方规则/创作学院(T05-S002/S004) + 行业媒体对新规的报道(T05-S019/S014)。
- **AI 赛道前沿选题**：AI 资讯流(T05-S020/S021) + 歸藏/卡兹克一手。

**媒体层厚薄诚实判断**:
- **薄**。中文「小红书 AI 自媒体（文案/内容制作）」**没有专门媒体条线**：36氪/虎嗅/品玩/极客公园/数英/亿邦都只在选题命中时零散出深稿，**不可订阅、无固定 cadence**。Newsletter / Podcast / Conference / 公开 Community **四类基本空缺**(N/A 或仅 1)，因为一手生态长在黑名单平台 + 付费社群里。本 track 的真实重心被迫压到「官方后台 + 数据 SaaS + 博主非黑名单主页 + AI 资讯流」四类「rolling 工具型源」，而非传统「定期长稿型源」。

**新 figure 候选（喂 wave 2 / 已在 Track 01 覆盖，作交叉确认）**:
- 歸藏(op7418)、卡兹克——已在 Track 01；本 track 补其**非黑名单一手渠道 URL**(B站空间 ID + GitHub 仓库 + 个人站)，提升 voice_confidence 可锚性。
- 花叔(Huashu Design)——在歸藏 B站合作视频(「体验开源PPT Skills - 歸藏 + 花叔」)出现，AI 设计/PPT 方向，**Track 01 未收**，标记为 figure 候选(信号弱，单点)。

**新 tool 候选（喂 wave 2 Track 02 / 交叉确认）**:
- 灰豚数据(huitun.com)——已在 02-tools；本 track 确认其作蝉小红停服后的**蓝海词替代**地位上升。
- 卡兹克开源 AI Skills(khazix-skills, 14.9k★) + 歸藏开源 PPT/CodePilot——**Skills/工作流类工具**，02-tools 未单列，标记为 tool/workflow 候选。

**topic-heat**: `incomplete, sources listed but content not crawled` —— 仅抽检了源的存活与定位，未系统爬每个源最新 N 条标题做话题热度统计。可低置信度观察：2026 上半年跨源(官方规则 + 亿邦/新浪 + 数据平台)反复出现的主题是 **「AI 标识新规 + 限流」**(evidence: [T05-S004, T05-S019]) 与 **「社区公约 2.0/AI 辅助须标识」**(evidence: [T05-S001])。

**冷僻 / 信号薄弱**:
- newsletter < 3(仅 1 合法)、podcast = 0(N/A)、conference = 0(N/A)、公开 community = 0(均付费/黑名单)——**4 个 type 触发薄弱信号**。
- 但「rolling 工具型活源」充足(官方 4 + 数据 3 活 + 博主主页 5 + AI 资讯 2 = 14 个可追)，floor 15 基本达标(含 dead 的蝉小红计 15)。
- **结论 → Phase 2.8 诚实边界**：sources 维度「定期长稿型源(newsletter/podcast/conference/公开社区)」严重稀薄，本质因一手生态长在黑名单平台 + 付费社群。master skill「想跟最新动态」节应明确告诉用户：**追源 = 盯官方后台 + 数据平台 + 博主 B站/个人站 + AI 日报**，并坦白「最深的方法论在你得自己去关注的公众号/付费星球里，本 skill 不能替你订阅」。

---

## 质量自检
- [x] 候选/收录 ≥ 15（21 条 manifest，其中 1 dead；有效活源 ~14-20）
- [x] 5 分类覆盖（官方4 / 数据平台3活 / 行业媒体6 / 博主主页5 / 选题源2）
- [x] 每条标 用途 + 更新频率(cadence) + 是否一手
- [x] 每源有 last_checked 日期(2026-06-06，agent 实访)
- [x] 商业平台 docs 标 surrogate_primary + note vendor docs
- [x] 黑名单零收录（公众号/知乎/百度/CSDN/简书/掘金命中即丢，已显式说明）
- [x] dead 源标注(蝉小红) + Phase 4 替换提示
- [x] Phase 2 接口：top 5 + 知识沉淀定位 + 媒体层厚薄诚实判断 + 新 figure/tool 候选 + 冷僻信号
- [x] 媒体层厚薄诚实判断已写明(newsletter/podcast/conference/community 四类稀薄根因)
