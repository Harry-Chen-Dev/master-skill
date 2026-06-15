# Track 01 — Figures: 推特(X) 中文圈 AI 自媒体博主

> Research date: 2026-06-06 · Locale: zh-CN · Focus: **怎么写推文/thread、怎么制作内容**（内容方法论 + 立场光谱）。
>
> **figure 稀薄度诚实声明（重要）**: 本 track 的「人」存在且活跃，但其一手输出主要散落在 **推文/thread 本身**（x.com=reference 级，无法机械抓全文）、**个人站/Substack/即刻/GitHub** 和媒体长稿里。没有「正典作者 + 30min 长访谈」那种成体系的 figure 材料。因此本文件的真正价值在于 **内容方法论 + 立场光谱**（编译 vs 原创、快讯 vs 深度、build in public、全 AI 自动 vs 人工精选），而非「思想体系承载者」。**建议 Phase 2 把权重压向 workflows / tools / canon，figures 仅供方法论与 voice 提取。** 多数 figure 卡片可信度 medium（一手在推文/个人站，长访谈材料 < 30min）。

## Source Manifest

| source_id | url | bucket | last_checked | author/host | one-line note |
|-----------|-----|--------|--------------|-------------|---------------|
| T01-S001 | https://baoyu.io/ | surrogate_primary | 2026-06-06 | 宝玉 (@dotey) | 个人站 — 翻译/原创/prompt 方法论一手 |
| T01-S002 | https://x.com/dotey | reference | 2026-06-06 | 宝玉 (@dotey) | X 主页 — 翻译 prompt / AI 三阶段 thread |
| T01-S003 | https://x.com/dotey/status/2029969547927658673 | reference | 2026-06-06 | 宝玉 | 单条: AI 翻译三阶段(提示词→推理→Agent) |
| T01-S004 | https://x.com/dotey/status/1707478347553395105 | reference | 2026-06-06 | 宝玉 | 单条: 告别「机翻感」翻译 prompt 原帖 |
| T01-S005 | https://www.guizang.ai/ | surrogate_primary | 2026-06-06 | 歸藏 (@op7418) | 个人站「歸藏的 AI 资讯」— 周刊主理 |
| T01-S006 | https://github.com/op7418/guizang-s-prompt | verified_primary | 2026-06-06 | 歸藏 (@op7418) | 提示词仓库 — 一手 prompt 产出 |
| T01-S007 | https://github.com/op7418/guizang-social-card-skill | verified_primary | 2026-06-06 | 歸藏 | 社交卡片/封面 skill — 排版方法论一手 |
| T01-S008 | https://x.com/op7418/status/1688843818773430272 | reference | 2026-06-06 | 歸藏 | 单条: 推特算法倾斜/涨粉规则 thread |
| T01-S009 | https://unifuncs.com/s/fJGtJy62 | secondary | 2026-06-06 | U深搜 | 歸藏深度解析(粉丝/变现/voice 数据) |
| T01-S010 | https://www.qiaomu.ai/ | surrogate_primary | 2026-06-06 | 向阳乔木 (@vista8) | 个人站矩阵(导航/RSS/论文/书) |
| T01-S011 | https://x.com/vista8 | reference | 2026-06-06 | 向阳乔木 (@vista8) | X 主页 — AI 产品/工作流/趋势 |
| T01-S012 | https://x.com/vista8/status/1733509609959379094 | reference | 2026-06-06 | 向阳乔木 | 单条: 推荐中文 X 圈 AI 优秀账号 |
| T01-S013 | https://gorden-sun.notion.site/527689cd2b294e60912f040095e803c5 | secondary | 2026-06-06 | Gorden Sun (@Gorden_Sun) | AI 资讯日报 Notion 库 — 个人聚合 |
| T01-S014 | https://x.com/imxiaohu | reference | 2026-06-06 | 小互 (@imxiaohu) | X 主页 — AI 快讯/工具速递 |
| T01-S015 | https://x.com/oran_ge | reference | 2026-06-06 | Orange AI (@oran_ge) | X 主页 — AI 创业者视角/锐评 |
| T01-S016 | https://github.com/alchaincyf/cursor-rules-huasheng | verified_primary | 2026-06-06 | AI进化论-花生 (@AlchainHust) | AI 编程 rules 一手仓库 |
| T01-S017 | https://x.com/AlchainHust/status/1876886863962574950 | reference | 2026-06-06 | 花生/花叔 | 单条: 「我不会编程，只会AI编程」争议帖 |
| T01-S018 | https://www.uisdc.com/lijigang-interview | secondary | 2026-06-06 | 优设网 | 李继刚长访谈(prompt=表达的艺术/Lisp) |
| T01-S019 | https://github.com/DennisThink/awesome_twitter_CN | verified_primary | 2026-06-06 | DennisThink | 中文 X 优质账号清单 — 候选网 |
| T01-S020 | https://www.liamding.com/posts/top-20-must-follow-ai-tech-x-twitter-accounts-for-real-insights/ | verified_primary | 2026-06-06 | Liam DING | X 圈 20 个 AI 账号精读 — 候选网+定位 |
| T01-S021 | https://github.com/justlovemaki/CloudFlare-AI-Insight-Daily | verified_primary | 2026-06-06 | justlovemaki | 全 AI 自动 AI 日报(Gemini 摘要) — 自动派代表 |
| T01-S022 | https://github.com/joeseesun/ai-blog-res | verified_primary | 2026-06-06 | 向阳乔木 (joeseesun) | AI 博客资源精读指南 — 一手信息源观 |

> **黑名单命中已丢弃**: 检索过程中出现 知乎(zhihu.com/zhuanlan.zhihu.com)、CSDN(blog.csdn.net)、微信公众号、虎嗅(m.huxiu.com)、infoq、cnblogs、tradesmax(SEO 农场榜) — 均**未进 manifest**，仅用于发现候选名字，不作 evidence。

---

## 总览（按内容方法论代表性排序）

| # | 名字 / handle | 核心身份 | 一句话定位 | 立场象限 | 值得看 | 源数 |
|---|------|---------|----------|---------|--------|-------|
| 1 | 宝玉 @dotey | prompt 工程师/译者 | 编译派天花板：把英文一手 + AI 翻译做成「带个人 voice 的深度搬运」 | 编译·深度·人工精选 | 📖🎙️ | 4 |
| 2 | 歸藏 @op7418 | 产品设计师 | 周刊/保姆级教程派：高产 + 跨平台矩阵 + 付费订阅变现样板 | 编译+原创实测·快讯+深度·人工 | 📖🎙️🎬 | 5 |
| 3 | 向阳乔木 @vista8 | 前字节 AI PM | 资源整理派：个人站矩阵(导航/RSS/论文/书) + AI 改写自媒体 | 编译+整理·混合·半自动 | 📖🎬 | 4 |
| 4 | 小互 @imxiaohu | AI 快讯搬运 | 快讯派：第一时间产品速递、信息密度高、社群日报变现 | 编译·快讯·人工(高频) | 🎙️ | 2 |
| 5 | Gorden Sun @Gorden_Sun | AI 资讯日报 | 聚合派：Notion 日报 + 一手信息源筛选 | 编译·快讯·半自动 | 📖 | 2 |
| 6 | 李继刚 @lijigang_com | prompt 艺术家 | 原创洞察派：prompt=表达的艺术，用 Lisp/汉语极致压缩 | 原创·深度·人工 | 🎙️ | 1 |
| 7 | Orange AI @oran_ge | AI 创业者 | 锐评+build in public：产品发布/行业判断/真实痛点叙事 | 原创锐评·深度·人工 | 🎬 | 1 |
| 8 | AI进化论-花生/花叔 @AlchainHust | AI Native Coder | 课程+人设派：AI 编程实操 + 强人设 + 直球争议营销 | 原创实操·混合·人工 | 🎬 | 2 |
| 9 | 王川 @Svwang1 | 深度长推作者 | 长推派(参照系)：历史/商业/科技认知，原创深度长 thread | 原创·深度·人工 | 📖 | 1 |
| 10 | justlovemaki (项目) | 自动化日报 | **全 AI 自动派代表(对照组)**：Gemini 自动摘要 → 自动发布 | 编译·快讯·全自动 | 📖 | 1 |

---

## Figures

### 1. 宝玉 / @dotey

- **One-liner**: 中文 AI 圈编译派天花板——把英文一手文章/访谈/字幕用 AI 翻译 + 个人写作风格做成「带 voice 的深度搬运」，并公开整套翻译 prompt 方法论。(evidence: [T01-S001, T01-S003])
- **核心身份**: prompt 工程师 / 译者 / 软件工程与工程管理内容创作者；个人站 baoyu.io。
- **代表作品**: ①《一个简单的 Prompt 大幅提升 ChatGPT 翻译质量，告别"机翻感"》(刷屏帖)；② AI 翻译三阶段框架；③ 大量 OpenAI/Anthropic/NVIDIA 高管访谈 + 论文 + GTC/吴恩达视频字幕的中译。(evidence: [T01-S004, T01-S003])
- **内容方法论（核心）**:
  - **选题 = 英文一手信息差**: 系统追英文一手(论文/高管访谈/会议视频)，翻译成中文填信息差；自陈翻译是「爱好不是生意」，学习之余顺手分享。(evidence: [T01-S002])
  - **翻译即重写**: 方法论从「翻译」演进到「重写」——多角色 prompt(「一个英文老师直译，两个中文老师按不同风格意译，校长融合」)，再到 Agent 阶段先分析术语/文化隐喻/背景知识，人工确认关键节点。(evidence: [T01-S003, T01-S004])
  - **用「写作风格 Skill」注入个人 voice**: 翻译/访谈整理后再过一道「风格 skill」，让产出带上他的表达习惯、注释方式、读者意识——这是他区别于纯机翻搬运的关键。(evidence: [T01-S001])
  - **标题手法**: 反问/对比式标题（"为啥…还不推出""…之后写代码的价值在下降"）。(evidence: [T01-S001])
- **voice_samples**:
  - 同业/自述样本: 「翻译字幕做好其实是很有技术含量的一件事，因为你要考虑到上下文去整体翻译字幕，要借助 LLM…」(source: T01-S002, 原话片段-推文)
  - 原创判断样本: 「别再用提示词去 AI 味了，方向就是错的」(source: T01-S002, 原话-推文标题)
  - 工程务实样本: 「Vibe Coding 并没有那么神奇，没有谁能不懂代码就做出成熟的产品。」(source: T01-S002, 原话片段-推文)
- **核心思想关键词**: 信息差、翻译即重写、个人 voice 注入、人在关键节点(human-in-the-loop)、工程务实。
- **sub_skill_candidate**: `false` — 影响力前 3，但一手成体系材料仍是「推文 + 个人站文章」而非长访谈；适合作为「编译派 workflow + voice 样本」喂 Phase 2，不够独立成 sub-skill。
- **最近 12 个月动态**: 2025-2026 重心转向 Claude Code / Agent 工程（多智能体协作指南、翻译 Agent 用 Claude Code 开发）；提出「工程师角色从写代码→管理 Agent」。(evidence: [T01-S001])
- **争议 / 批评**: 编译派共性争议——「高质量搬运英文一手」被部分人视为依赖信息差而非原创洞察；他本人对「翻译是不是生意」的质疑做过公开回应。(evidence: [T01-S002])
- **可信度自评**: medium — 一手丰富但分散在推文/个人站，无单篇 30min+ 长访谈作框架支撑。

### 2. 歸藏(guizang.ai) / @op7418

- **One-liner**: 「周刊 + 保姆级教程」派样板——产品设计师背景，高产、跨平台矩阵分发、付费订阅变现，AIGC(绘画/视频/设计)垂类头部。(evidence: [T01-S005, T01-S009])
- **核心身份**: 产品/模型设计师、独立开发者（自陈「不会写代码」）；主理「AIGC 周刊 / 歸藏的 AI 工具箱」，人设「藏师傅」。
- **代表作品**: ① AIGC 周刊(85+ 期，"新闻+评测+学术"四板块固定结构)；②「藏师傅系列」原创实测教程(如 Nano Banana 生图比例、云端部署 SD)；③ GitHub 提示词仓库 + social-card-skill(排版/封面工具)。(evidence: [T01-S006, T01-S007, T01-S009])
- **内容方法论（核心）**:
  - **固定栏目框架**: 每期周刊四板块——上周核心发布 / 融资产品迭代 / 优质视觉案例 / 重要论文解读，「新闻+评测+学术」混合保深度与广度。(evidence: [T01-S009])
  - **保姆级 + 原创实测**: 手把手教程 + 自己实测报告，强调「实战价值高于理论」；直球测评（如「Sora 不值得花 200 美元」）建「真诚测评者」而非「推广者」人设。(evidence: [T01-S009])
  - **涨粉=算法顺应+矩阵分发**: 公开转述推特算法倾斜规则——**多回复 > 多转发**（回复更易被推时间线 + 引发讨论）、多媒体内容加权；内容沿 周刊→播客→微博→知乎→即刻 重复曝光做跨平台渗透。(evidence: [T01-S008, T01-S009])
  - **排版即产品**: 专门做 social-card-skill（小红书图文 + 公众号封面，28 布局/10 主题，单文件 HTML→PNG），把「配图/排版」工程化。(evidence: [T01-S007])
  - **高产人设**: 「最肝的人之一」，熬夜输出作为个人品牌标签。(evidence: [T01-S009])
- **voice_samples**:
  - 测评样本（转述）: 「Sora 不值得花 200 美元」式的直球评价 — 建真诚测评者形象。(source: T01-S009, 转述)
  - 自我定位样本（转述）: 强调「不会代码的独立开发者」身份，反而增强可信度——证明 AI 工具易用到非技术背景也能掌握。(source: T01-S009, 转述)
  - ⚠️ 暂未取得 ≥30 字直接原话片段（X 全文 reference 级未抓取）。
- **核心思想关键词**: 固定栏目框架、保姆级教程、算法顺应(多回复)、跨平台矩阵、排版工程化、付费订阅。
- **变现（数据）**: AIGC 周刊付费订阅(年费 ¥199)，quail 6,037 订阅 + 小报童 1,300+；合伙人计划(推荐 20% 返利) + 多家 AI 产品顾问。粉丝：X 9 万+ / 微博 26 万 / 即刻 24k。(evidence: [T01-S009]) — 注: 单一二手源，数字需二次校验。
- **sub_skill_candidate**: `false` — 影响力高，但价值是「可复制的周刊运营+排版 workflow」而非个人思想体系；最适合喂 Track 02/03。
- **最近 12 个月动态**: 持续做 Claude Code / Codex skill(social-card、Humanizer-zh 去 AI 味汉化)；OpenAI 总裁曾主动转发其内容。(evidence: [T01-S007, T01-S009])
- **争议 / 批评**: 公开记录未见重大争议；隐性风险是过度依赖付费订阅 + 内容时效性 + 平台算法变动。(evidence: [T01-S009])
- **可信度自评**: medium — 个人站/GitHub 一手 + 一篇结构化二手深度解析，数据来自单一二手源。

### 3. 向阳乔木 / @vista8

- **One-liner**: 资源整理派——前字节 AI PM，把「AI 信息源整理」做成个人站矩阵(导航/RSS/论文/书/课程)，并用「AI 翻译+按自己风格改写+人工审」的半自动流水线产内容。(evidence: [T01-S010, T01-S011])
- **核心身份**: 前字节跳动高级产品经理(飞书/大力教育/TikTok)、连续创业者；主理「向阳乔木推荐看」+ qiaomu.ai 站群。
- **代表作品**: ① qiaomu.ai 站群(daohang 导航 / rss 阅读器 / paper 论文学习 / book 群聊电子书)；② AI 博客资源精读指南(joeseesun/ai-blog-res，汇总国际顶级 AI 研究者博客)；③ AI 写作软件 + 零基础 AI 课程(500+ 学员)。(evidence: [T01-S010, T01-S022])
- **内容方法论（核心）**:
  - **信息源 > 信息本身**: 核心打法是「帮你找到并整理一手信息源」——整理全球顶级 AI 研究者博客/学习资源，推荐中文 X 圈优质账号。(evidence: [T01-S012, T01-S022])
  - **半自动改写流水线**: QMReader RSS 提供「中文翻译 + 按他的风格改写 + 人工审核 + 文章讨论」——介于全自动与纯人工之间。(evidence: [T01-S010])
  - **工具自建**: Markdown AI 写作软件、一键复制网页 Chrome 插件——内容创作者自己造工具。(evidence: [T01-S010])
- **voice_samples**:
  - 自我标签样本: 「爱钓鱼、喜欢听摇滚乐、每天洗冷水澡的 PM」(source: T01-S011, 转述-X 简介)
  - ⚠️ 暂未取得 ≥30 字 register 化原话片段。
- **核心思想关键词**: 信息源整理、精读指南、半自动改写、工具自建、零基础可学。
- **sub_skill_candidate**: `false` — 价值在「信息源策展 workflow」，喂 Track 05(sources) 更合适。
- **最近 12 个月动态**: 持续扩 qiaomu.ai 站群(2026 世界杯日历订阅等边缘产品)、推 AI 课程；活跃于 Vibe Coding / 工作流话题。(evidence: [T01-S010])
- **争议 / 批评**: 整理/改写派共性——「AI 改写」与原创边界、二次分发版权；未见点名争议。(evidence: [T01-S010])
- **可信度自评**: medium — 个人站矩阵一手充分，方法论描述部分来自站点/搜索摘要。

### 4. 小互 / @imxiaohu

- **One-liner**: 快讯派代表——第一时间搬运/速递全球 AI 新产品与动态，信息密度高，靠「XiaoHu.AI 日报」社群沉淀变现。(evidence: [T01-S014])
- **核心身份**: AI 新闻/工具资讯创作者(早期「互联网的那点事」)；X @imxiaohu + 微博 + 社群日报。
- **代表作品**: XiaoHu.AI 日报(每晚 11 点后在社群发布)；大量「新工具一句话功能拆条」式速递推文。(evidence: [T01-S014])
- **内容方法论（核心）**:
  - **速度优先 + 功能清单体**: 推文模板化——产品名 + 一句定位 + 功能 bullet（对象移除/风格转移/一致性角色…）+ 链接，便于快速消费。(evidence: [T01-S014])
  - **社群作护城河**: 公开推文做引流，深度日报放社群(固定时段)，把流量转成留存。(evidence: [T01-S014])
- **voice_samples**:
  - 速递样本: 「Jaaz：Lovart AI 本地开源替代…对象移除：删除图像中不需要的元素。风格转移：改变图像的艺术风格。一致性角色生成：保持角色外观的一致性。」(source: T01-S014, 原话-推文 bullet 体)
  - ⚠️ 缺同业/监管 register 样本(快讯账号语体单一)。
- **核心思想关键词**: 速度、功能清单体、模板化、社群留存、信息密度。
- **sub_skill_candidate**: `false` — 纯快讯搬运，方法论价值在「推文模板」而非思想。
- **最近 12 个月动态**: 持续高频更新工具速递(2025 多条本地开源/图像工具)；扩 Instagram 等渠道。(evidence: [T01-S014])
- **争议 / 批评**: 快讯搬运派共性争议——速递常不深究、易蹭热点、原创度低、来源标注被诟病(行业普遍现象，非单点实锤)。(evidence: [T01-S020])
- **可信度自评**: medium — 一手仅 X 主页(reference 级)+ 候选网定位，缺深度材料。

### 5. Gorden Sun / @Gorden_Sun

- **One-liner**: 聚合派——把每日 AI 资讯整理成结构化 Notion 库(AI 资讯日报)，强调一手信息源筛选，半自动产出。(evidence: [T01-S013])
- **核心身份**: AI 资讯日报主理人；X @Gorden_Sun + gorden-sun.notion.site。
- **代表作品**: 「AI 资讯日报」Notion 库(行业新闻/开源项目/论文/大 V 言论分栏)，每日推文挂 Notion 链接。(evidence: [T01-S013])
- **内容方法论（核心）**:
  - **Notion 即产品**: 用 Notion 数据库做可检索/可订阅的日报载体，而非长推文。(evidence: [T01-S013])
  - **多类目聚合**: 行业新闻 + 热门开源 + 前沿论文 + 科技大 V 社媒言论四类聚合——典型「人工精选 + 半自动」打法（对照 justlovemaki 的全自动版本，见 #10）。(evidence: [T01-S013, T01-S021])
- **voice_samples**: ⚠️ 暂未找到 ≥30 字直接原话片段（推文多为「日期 + 链接」式，语体极简）。
- **核心思想关键词**: 结构化聚合、Notion 载体、一手信息源、可订阅。
- **sub_skill_candidate**: `false` — 聚合工具属性强，喂 Track 05。
- **最近 12 个月动态**: 持续日更 AI 资讯日报(2025-2026 连续)。(evidence: [T01-S013])
- **争议 / 批评**: 聚合派与「全 AI 自动日报」同质化竞争，区分度依赖人工筛选质量。(evidence: [T01-S021])
- **可信度自评**: medium-low — 仅 Notion 一手 + 单条推文，方法论靠推断。

### 6. 李继刚 / @lijigang_com

- **One-liner**: 原创洞察派/「prompt 艺术家」——把 prompt 当「表达的艺术」，用 Lisp 语法和汉语做极致语义压缩，「汉语新解」刷屏，代表 prompt 圈的人文/压缩流派。(evidence: [T01-S018])
- **核心身份**: prompt 探索者/创作者，AI 思考与创意应用方法论。
- **代表作品**: ①「汉语新解」prompt(刷屏)；② 系列高密度 Lisp 风格 prompt；③ 优设网长访谈《提示词的本质是表达的艺术》。(evidence: [T01-S018])
- **内容方法论（核心）**:
  - **prompt = 表达的艺术 / 压缩**: 核心是「理解人类意图」，把复杂信息压缩到最本质概念（例：一本 314 页定位书 → 一句「占据用户心智」）；反对「prompt 越复杂越好」「prompt 万能」两个误区。(evidence: [T01-S018])
  - **用 Lisp 写 prompt**: 选 Lisp 因其能在「极致压缩到关键词」原则下清晰表达想法；为 AI 而设计的语言 + 十年 Emacs(Lisp 配置)经验。(evidence: [T01-S018])
- **voice_samples**:
  - 方法论样本(转述): 「提示词的本质是理解人类意图…不是越复杂越好，也不是能解决所有问题。」(source: T01-S018, 转述-访谈)
  - 压缩观样本(转述): 「一本 314 页讲定位的书，最终就是一个概念——占据用户心智。」(source: T01-S018, 转述-访谈)
  - ⚠️ 原话片段受访谈站 403 限制，未取得逐字原文。
- **核心思想关键词**: 表达的艺术、语义压缩、理解意图、Lisp、人文 prompt。
- **sub_skill_candidate**: `true`(弱) — 唯一带「自洽思想体系 + 长访谈」的 figure，原创度最高；若用户 focus 在 prompt 写作，可考虑独立蒸馏。但访谈材料一篇、可调研性中等，标弱。
- **最近 12 个月动态**: 持续产 prompt + 在 WaytoAGI 等社区作 prompt 最佳实践分享。(evidence: [T01-S018])
- **争议 / 批评**: 「Lisp prompt 是否实用 vs 表演性」有争论——部分人认为对普通用户门槛过高、观赏 > 实用。(evidence: [T01-S018])
- **可信度自评**: medium — 有一篇成体系长访谈(但站点 403，靠摘要)+ 公开 prompt 作品。

### 7. Orange AI / @oran_ge (orange.ai)

- **One-liner**: 原创锐评 + build in public 派——AI 创业者视角，发布自家产品(FlowSpeech 等)同时输出行业判断/真实痛点叙事，擅长「教程帖引爆 + 数据复盘」。(evidence: [T01-S015])
- **核心身份**: AI 创业者/产品人；X @oran_ge。
- **代表作品**: ① 自家产品发布帖(FlowSpeech 书面语转口语 TTS)；② 2025「最爆教程帖」复盘(172 万曝光→309 订阅，公开转化漏斗)；③ 行业观察帖(湾区财富分化等)。(evidence: [T01-S015])
- **内容方法论（核心）**:
  - **教程帖 + 数据透明复盘**: 用实用教程获大曝光，再公开「曝光→转化」真实比例（千分之二）做二次内容，强化执行力叙事。(evidence: [T01-S015])
  - **真实痛点 > 概念炒作**: 产品叙事刻意反「吹概念/追模型/卷 Agent」，强调「基于真实用户真实痛点的有用小产品」。(evidence: [T01-S015])
  - **build in public**: 边做产品边公开发布/迭代/反思。(evidence: [T01-S015])
- **voice_samples**:
  - 锐评样本: 「为什么在行业都在吹概念，追模型，卷 Agent…它却是基于我们真实的用户的真实痛点所做的有用的小产品。」(source: T01-S015, 原话片段-推文)
  - 复盘样本: 「从 172 万曝光，到 309 人真的订阅，比例仅千分之二…你的执行力已经超过了 99.8% 的人。」(source: T01-S015, 原话片段-推文)
- **核心思想关键词**: build in public、真实痛点、数据透明复盘、反概念炒作、执行力叙事。
- **sub_skill_candidate**: `false` — 立场鲜明但材料是推文流，价值在「build-in-public 内容公式」，喂 Track 03。
- **最近 12 个月动态**: 2025-2026 密集发产品(FlowSpeech、QQ 机器人接入等) + 行业锐评。(evidence: [T01-S015])
- **争议 / 批评**: 锐评+自家产品绑定→「内容服务于带货」的边界质疑(创业者内容共性)。(evidence: [T01-S015])
- **可信度自评**: medium — X 一手丰富(但 reference 级)，有可引原话片段。

### 8. AI进化论-花生 / 花叔 / @AlchainHust

- **One-liner**: 课程+强人设派——AI Native Coder(自陈「不会编程，只会 AI 编程」)，靠 AI 编程实操 + 直球争议营销涨粉，前阿里/美团增长背景。(evidence: [T01-S016, T01-S017])
- **核心身份**: AI Native Coder / 独立开发者 / AI 编程课讲师(领英·微软 AI 课签约讲师)；X @AlchainHust，多平台(B 站/YouTube/小红书/即刻)。
- **代表作品**: ① cursor-rules-huasheng(AI 编程 rules 仓库)；② AI 编程课程 + GPTs(AI 使用助手)；③ 用 AI 编程做的 app 上过免费榜 TOP20。(evidence: [T01-S016, T01-S017])
- **内容方法论（核心）**:
  - **争议即流量**: 主动用对立话术制造讨论——「我不会编程，只会 AI 编程，我在卖 AI 编程的课…你会编程，你做出啥了？」公开承认蹭争议引流。(evidence: [T01-S017])
  - **结果背书人设**: 用「app 上榜/月入」等可验证结果给「非技术背景也能做产品」的叙事背书。(evidence: [T01-S017])
  - **增长打法迁移**: 前大厂用户增长经验直接套到自媒体起号。(evidence: [T01-S016])
- **voice_samples**:
  - 争议营销样本: 「对的，我不会编程，我只会 AI 编程，我在卖 AI 编程的课…不爽的人可能还是需要忍一忍。」(source: T01-S017, 原话片段-推文)
  - 结果背书样本: 「我在只会 AI 编程的情况下，一个 app 上了免费分类榜 TOP20，和 YouTube、Instagram、Canva 排在一起。」(source: T01-S017, 原话片段-推文)
- **核心思想关键词**: AI Native Coding、争议营销、结果背书、人设运营、增长迁移。
- **sub_skill_candidate**: `false` — 方法论价值在「人设+争议起号公式」，但争议色彩重，谨慎；喂 Track 03 作反面/对照案例。
- **最近 12 个月动态**: 持续推 AI 编程课 + cursor rules + GPTs(2025-2026)。(evidence: [T01-S016])
- **争议 / 批评**: 「卖课导向 + 蹭争议」是其最大标签；「不会编程教编程」的资质质疑被本人主动当卖点。(evidence: [T01-S017])
- **可信度自评**: medium — GitHub 一手 + 可引争议原话推文。

### 9. 王川 / @Svwang1

- **One-liner**: 深度长推派（参照系/对照）——历史/商业/科技/认知的原创深度长 thread，代表中文 X「慢内容·重思考」与 AI 快讯派的另一极。(evidence: [T01-S020])
- **核心身份**: 投资人/思考者，深度长推作者。
- **代表作品**: 系列商业/科技/认知长 thread(非围绕单一 AI 产品，而是跨学科思辨)。(evidence: [T01-S020])
- **内容方法论（核心）**:
  - **长 thread 立论**: 用多条相连推文展开一个论点(历史类比→商业逻辑→当下推论)，反速食。(evidence: [T01-S020])
  - **原创认知输出**: 几乎不搬运，靠个人认知框架。(evidence: [T01-S020])
- **voice_samples**: ⚠️ 暂未取得 ≥30 字直接原话片段(X 全文未抓)。
- **核心思想关键词**: 深度长推、跨学科、认知框架、慢内容、原创。
- **sub_skill_candidate**: `false` — 列入主要为「立场光谱另一极」参照，AI 垂直度不高。
- **最近 12 个月动态**: 持续活跃于长推(被多份 X 推荐清单列为深度长推代表)。(evidence: [T01-S020])
- **争议 / 批评**: 长推门槛高、更新偏散；属「广义认知」非纯 AI。(evidence: [T01-S020])
- **可信度自评**: low-medium — 仅候选网二手定位，无单独一手抓取。

### 10. justlovemaki / CloudFlare-AI-Insight-Daily（项目，全自动派对照组）

- **One-liner**: **全 AI 自动派代表(对照组)**——基于 Cloudflare Workers 自动聚合 AI 新闻/开源/论文/大 V 言论，用 Gemini 智能摘要后**自动发布**成日报，是「人工精选 vs 全自动」轴上人工派的反面。(evidence: [T01-S021])
- **核心身份**: 开源自动化 AI 日报项目(非个人 figure，作为立场坐标列入)。
- **代表作品**: CloudFlare-AI-Insight-Daily(GitHub) — 内容聚合 + Gemini 生成 + GitHub Pages 自动发布全流水线。(evidence: [T01-S021])
- **内容方法论（核心）**:
  - **零人工流水线**: 每日自动抓取 → Gemini 摘要 → 自动发布，把小互/Gorden Sun 的「人工日报」彻底自动化。(evidence: [T01-S021, T01-S013])
  - **意义**: 证明「快讯/聚合」这一层正被自动化吞噬——人工派的护城河被迫上移到「观点/实测/人设」。(evidence: [T01-S021])
- **voice_samples**: N/A（机器生成，无个人 voice）。
- **核心思想关键词**: 全自动、聚合、Gemini 摘要、护城河上移。
- **sub_skill_candidate**: `false` — 工具/立场坐标，非 figure。
- **最近 12 个月动态**: 开源活跃(2025-2026)。(evidence: [T01-S021])
- **争议 / 批评**: 全自动内容 = 「AI 数字泔水/文字泡沫」批评的典型对象(模板话术、无核实、挤压原创)。(evidence: [T01-S021])
- **可信度自评**: medium — GitHub 一手明确，作对照组而非人物卡。

---

## Phase 2 提炼提示

### 反复出现 ≥3 个 figures 都谈到的关键词（候选行业心智模型）

- **信息差套利**（编译英文一手填中文空白）: 宝玉 / 向阳乔木 / Gorden Sun / 小互 (evidence: [T01-S002, T01-S012, T01-S013, T01-S014])
- **固定栏目/模板化推文**（功能清单体、四板块周刊、教程公式）: 歸藏 / 小互 / Orange AI (evidence: [T01-S009, T01-S014, T01-S015])
- **个人 voice / 人设运营**（写作风格 skill、藏师傅、花叔人设）: 宝玉 / 歸藏 / 花生 (evidence: [T01-S001, T01-S009, T01-S017])
- **算法顺应**（多回复>转发、多媒体加权、跨平台矩阵分发）: 歸藏（公开转述规则）+ 花生/向阳乔木实践 (evidence: [T01-S008, T01-S010])
- **保姆级实测 > 理论**（手把手 + 真实测评）: 歸藏 / 花生 / Orange AI (evidence: [T01-S009, T01-S015, T01-S016])
- **付费订阅/社群变现**（周刊订阅、社群日报、卖课）: 歸藏 / 小互 / 花生 / 向阳乔木 (evidence: [T01-S009, T01-S014])

### 显著分歧 / 流派分裂（立场光谱 — 本 track 最高价值产出）

- **编译搬运 vs 原创洞察**: 编译派（宝玉/小互/Gorden Sun/向阳乔木）vs 原创派（李继刚/Orange AI/王川）。宝玉用「翻译即重写+voice 注入」横跨两端，是中间样板。(evidence: [T01-S001, T01-S018])
- **快讯/速度 vs 深度/慢思考**: 快讯（小互/Gorden Sun）vs 深度长推（王川/李继刚/宝玉访谈翻译）。(evidence: [T01-S014, T01-S020])
- **build in public vs 纯内容**: build in public（Orange AI/花生）vs 纯内容创作者（宝玉/歸藏的周刊/向阳乔木）。(evidence: [T01-S015, T01-S017])
- **全 AI 自动 vs 人工精选**: 全自动（justlovemaki 项目，机器流水线）vs 人工精选（小互/Gorden Sun/歸藏）。半自动改写（向阳乔木 QMReader）居中。**这条轴决定 figures 护城河正从「聚合速度」上移到「观点/实测/人设/voice」。**(evidence: [T01-S021, T01-S013, T01-S010])
- **争议营销 vs 真诚专业**: 争议起号（花生/花叔）vs 真诚测评（歸藏「Sora 不值 200 刀」/宝玉工程务实）。(evidence: [T01-S017, T01-S009])

### 冷僻领域信号（figure 稀薄度判定）

- 总 figure 数: **9 人 + 1 项目对照** ≥10，不触发冷僻协议；但「真 figure」(有体系材料) 实际偏少。
- **多数 figure 长访谈材料 < 30min**: ✅ 为真 — 仅李继刚有 1 篇成体系长访谈（且站点 403），其余一手都是推文/个人站/即刻碎片。
- 标「可信度 low / low-medium」比例: 2/10 (王川、Gorden Sun)，约 20%，未过 30% 红线但接近。
- **结论**: figures 维度信息**中等偏薄**。一手主要在 x.com(reference 级，无法机械抓全文) + 个人站/GitHub(surrogate_primary)。**Phase 2 应把权重压向 workflows(怎么写推文/排版/分发)、tools(翻译/排版/聚合工具栈)、canon(代表 thread/prompt 作品)，figures 仅贡献「内容方法论 + 立场光谱 + voice 样本」。** SKILL.md 诚实边界节须写明：本行业「人」的认知 OS 一致性弱，mental model 多从可观察的内容行为反推，而非从 figure 长篇自述直接听到。

### 缺口（建议后续 track 补）

1. **X 全文未抓**: 多条代表 thread 因 x.com=reference + 402/JS 限制只有标题/摘要，缺逐字原文与排版细节 → Track 03/Track 04 需用 threadreaderapp / 截图 / 二手转录补「推文结构样本」。
2. **涨粉/算法方法论仅 1 个公开源**（歸藏转述）→ Track 03 应补更多「起号/算法」一手（即刻长文、X 自述帖）。
3. **变现数字单一二手源**（歸藏的订阅/收入数字来自一篇 U深搜解析）→ 需二次校验，勿当 ground truth。
4. **女性/小众垂类 figure 缺位**: Berryxia.AI、早见 Hayami、海辛(AI 视频) 等候选未深挖，AIGC 视觉派可在 Track 02/03 补。
