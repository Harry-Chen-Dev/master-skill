# Track 02 — Tools / 内容生产工具栈 — 知乎 AI 自媒体博主

> Research date: 2026-06-15 · Locale: zh-CN · 聚焦「知乎 AI 赛道怎么写文案 / 怎么制作内容」的实际工具栈
> 核心轨。本文件输出：按内容生产 4 环节(找选题→写作→配图/图表→排版/发布/数据)的工具栈 + 选型决策树 + 避坑/合规清单。
> 与小红书行业的差异锚点：知乎 = **长文 + 干货 + 逻辑/可信赖**(知乎官方写作四要素:有料/有观点/可信赖/照顾读者),工具栈更偏「深度搜证 + 长文写作 + 代码/图表/公式渲染」,而非短图文/封面美学。

## Source Manifest

| source_id | url | bucket | last_checked | author/host | note |
|-----------|-----|--------|--------------|-------------|------|
| T02-S001 | https://metaso.cn/ | verified_primary | 2026-06-15 | 上海秘塔科技 | 秘塔AI搜索官网(第一方):无广告/结构化/学术搜索/简洁-深入-研究三模式/脑图+大纲/自研MetaLLM |
| T02-S002 | https://github.com/KKKKhazix/khazix-skills | verified_primary | 2026-06-15 | 数字生命卡兹克 | 顶流AI博主开源 Skills 合集 15.2k★ MIT:含 **khazix-writer(长文风格+四层自检)** + hv-analysis(横纵分析,1-3万字PDF报告) + aihot + neat-freak + storage-analyzer |
| T02-S003 | https://github.com/KKKKhazix/khazix-skills/blob/main/khazix-writer/SKILL.md | verified_primary | 2026-06-15 | 数字生命卡兹克 | khazix-writer 一手 SKILL.md:作者写长文 voice/节奏/四层自检(结构/节奏/内容/语言) |
| T02-S004 | https://github.com/hzwer/WritingAIPaper | verified_primary | 2026-06-15 | hzwer(黄哲威,StepAI/北大) + DingXiaoH(丁霄汉) | 3.8k★ AI 会议论文写作手册:找核心idea(insight/perf/capability)+搭框架(摘要-引言-正文)+写引言(立territory-找gap-占niche)+提升可读性;**有知乎中文版** |
| T02-S005 | https://github.com/hzwer | secondary | 2026-06-15 | hzwer(黄哲威) | 学术系知乎 AI 大V GitHub 主页(RIFE/RepVGG 系),一手产出 |
| T02-S006 | https://www.46.la/tool/zhihu-hot-rank-tool | surrogate_primary | 2026-06-15 | 四六啦工具 | vendor docs 知乎实时热榜工具(前50条+热度排序,公开榜单接口),轻量免费选题监测 |
| T02-S007 | https://www.bazhuayu.com/helpcenter/docs/zhi-hu-jin-qi-re-bang-cai-ji | surrogate_primary | 2026-06-15 | 八爪鱼采集器 | vendor docs 知乎热榜采集教程(小时/日/周榜+热力值/各项增量字段,导出Excel),DIY 数据化选题 |
| T02-S008 | https://aihot.virxact.com/daily | surrogate_primary | 2026-06-15 | AI HOT 日报 | vendor docs 每日8点 AI 资讯 digest(聚合13+源),AI 选题源;卡兹克 aihot skill 即取此源 |
| T02-S009 | https://editor.mdnice.com/ | verified_primary | 2026-06-15 | mdnice(墨滴) | Markdown Nice 在线编辑器官网:一键排版知乎/公众号/掘金,主题样式+图床+脚注+公式 |
| T02-S010 | https://github.com/mdnice/markdown-nice | verified_primary | 2026-06-15 | mdnice | mdnice 开源仓库(第一方):支持主题设计的 Markdown 编辑器 |
| T02-S011 | https://carbon.now.sh/ | verified_primary | 2026-06-15 | carbon-app(开源) | Carbon 代码截图美化官网:主题/语法高亮/PNG+SVG 导出,免费,开源 |
| T02-S012 | https://github.com/carbon-app/carbon | verified_primary | 2026-06-15 | carbon-app | Carbon 开源仓库(第一方) |
| T02-S013 | https://ray.so/ | verified_primary | 2026-06-15 | Raycast | ray.so 代码美图工具官网(Raycast 出品):create beautiful images of your code |
| T02-S014 | https://mermaid.live/ | verified_primary | 2026-06-15 | Mermaid | Mermaid Live Editor 官网:文本语法生成流程图/时序图/ER图/架构图,贴 AI 生成的 mermaid 码即出图 |
| T02-S015 | https://www.drawio.com/ | verified_primary | 2026-06-15 | draw.io(JGraph) | 免费在线绘图官网:拖拽+支持 mermaid 码,流程图/架构图细调 |
| T02-S016 | https://jimeng.jianying.com/ | surrogate_primary | 2026-06-15 | 字节即梦AI | vendor docs 文生图+视频+智能画布(中文创作/局部重绘/扩图/抠图/风格保持) |
| T02-S017 | https://www.midjourney.com/ | verified_primary | 2026-06-15 | Midjourney | MJ 文生图官网(第一方):高质量审美,扩散模型,SREF 风格参考 |
| T02-S018 | https://matrix.tencent.com/ai-detect/ | verified_primary | 2026-06-15 | 腾讯朱雀 | 朱雀 AI 检测官网(第一方):登录后每日20次免费,文本/图片/视频检测,论文/普通/小说三模式 |
| T02-S019 | https://www.kimi.com/ | verified_primary | 2026-06-15 | 月之暗面 Moonshot | Kimi 官网(第一方):长文本「大海捞针」+引用链最准,K2/K2.5,自主规划(查财报/比数据/出PPT) |
| T02-S020 | https://www.deepseek.com/ | verified_primary | 2026-06-15 | 深度求索 DeepSeek | DeepSeek 官网(第一方):V3.2/R1,深度逻辑/代码/数学,开源可本地部署 |
| T02-S021 | https://www.doubao.com/ | verified_primary | 2026-06-15 | 字节 豆包 | 豆包官网(第一方):中文网感/语音/实时联网搜索,2026 DAU 第一 |
| T02-S022 | https://claude.ai/ | verified_primary | 2026-06-15 | Anthropic Claude | Claude 官网(第一方):长文档分析+复杂多步指令+代码强,英文逻辑佳,中文「知乎味」需重调 |
| T02-S023 | https://www.perplexity.ai/ | verified_primary | 2026-06-15 | Perplexity | Perplexity 官网(第一方):Deep Research(数十次搜+读数百源出报告),引用准/实时联网,Pro Search 15-30s |
| T02-S024 | https://www.geekpark.net/news/359902 | secondary | 2026-06-15 | 极客公园 | Kimi K2.5 深度实测(科技媒体,非黑名单):长文/写作能力评测 |
| T02-S025 | https://k.sina.cn/article_7879848900_1d5acf3c401902mu2a.html | secondary | 2026-06-15 | 新浪新闻(转载,降权) | 2026国产大模型排行(DeepSeek开源/Kimi长文/豆包移动)——仅作格局旁证,非核心事实源 |

> **黑名单已剔除**:CSDN / mp.weixin / 百度 / 简书 / 掘金 / 搜狐 / 知乎站内专栏(作「事实来源」时);搜索命中均未收录为核心源。**知乎站内**仅在「博主自己的工具测评/方法论」语境下可作 platform-native surrogate(本 track 未用到,均有更高 bucket 替代)。
> **bucket 判定**:工具官网首页 / 官方 GitHub / 官方 docs 根 = `verified_primary`(第一方);厂商 docs 子页 / 帮助中心 / 定价页(46.la、八爪鱼帮助、即梦官网功能页、aihot) = `surrogate_primary`(vendor docs);科技媒体实测/报道 = `secondary`。新浪转载稿降权,仅旁证。

---

## 环节 1 — 找选题 / 找资料 / 搜证

> 知乎 = 可信赖优先,**搜证能力是护城河**。本环节工具最密集。

| 工具 | 场景 | 优劣 | 一手/二手 | Decay | Sources |
|------|------|------|-----------|-------|---------|
| **秘塔 AI 搜索** | 找资料 + 搜证 + 出结构化报告(简洁/深入/**研究**三模式;**学术搜索**在数亿文献筛选);自动出大纲/脑图/事件-组织-人物表 | 国产无广告、引用源齐、结构化最强;**知乎干货长文搜证首选**。弱点:深度推理不如旗舰对话模型 | 一手(官网) | medium | [T02-S001] |
| **知乎热榜监测(四六啦)** | 开写前抓实时热榜前50+热度排序,做数据化选题 | 轻量免费、公开接口、零门槛;只给榜单不给增量趋势 | 二手(vendor docs) | medium | [T02-S006] |
| **八爪鱼 知乎热榜采集** | DIY 采集小时/日/周榜 + 热力值/各增量字段导出 Excel,自建选题库 | 字段最全、可定时;需配置、有学习成本 | 二手(vendor docs) | medium | [T02-S007] |
| **AI HOT 日报** | AI 赛道每日选题源(8:00 聚合13+源 digest) | 免 API、卡兹克 aihot skill 即取此源;聚合二手、需自筛 | 二手(vendor docs) | medium | [T02-S008] |
| **Kimi(深度搜索)** | 长文本投喂 + 大海捞针 + 引用链最准,自主规划(查财报/比数据) | 长文档检索 + 引用准确度国产最强,适合喂多篇对标拆结构;创意/网感弱 | 一手(官网) | medium | [T02-S019, T02-S024] |
| **Perplexity Deep Research** | 英文/全球源搜证,数十次搜读数百源出报告 | 引用准 + 实时联网 + Pro Search 15-30s 最快;中文源覆盖弱于秘塔 | 一手(官网) | medium | [T02-S023] |
| **GPT/Claude/豆包 深度搜索** | 各自旗舰的 deep research 模式做多步搜证 | Claude 多步指令/长文档强、豆包实时中文联网强;按手头模型用 | 一手(官网) | medium | [T02-S021, T02-S022] |

> **搜索流量词工具**:知乎站内**搜索下拉/相关问题**本身是最直接的「流量词」来源(站内一手,无第三方稳定公开 SaaS 与小红书的新红/千瓜对等);AI 赛道则用 AI HOT 日报 + 秘塔研究模式补热点词。**空白点**(给 Track 03):知乎缺一个对标小红书「千瓜热搜词」的成熟第三方词库平台,选题更依赖热榜工具 + AI 搜索。

---

## 环节 2 — 写作 / 改写 / 扩写

> 知乎核心战场。模型 + 写长文 skill + 学术写作手册三层。

| 工具 | 场景 | 优劣 | 一手/二手 | Decay | Sources |
|------|------|------|-----------|-------|---------|
| **DeepSeek** | 干货长文 / 结构化论证 / 选题脑暴 / 代码 | 深度逻辑+数学+代码强、开源可本地、极便宜;**知乎干货流主力** | 一手(官网) | medium | [T02-S020, T02-S025] |
| **Kimi** | 长文本投喂改写、把多篇爆款喂进去抽结构、出长稿 | 长文/办公流强、引用准;**长文写作 + 拆解对标**最顺手 | 一手(官网) | medium | [T02-S019, T02-S024] |
| **豆包** | 标题 / 开头钩子 / 中文「网感」改写 | 中文网感+实时联网+语音最自然;深度逻辑弱于 DeepSeek | 一手(官网) | medium | [T02-S021] |
| **Claude / GPT** | 复杂多步改写、英文逻辑、长文档分析 | Claude 长文档+指令遵循强;中文「知乎味」需重调 prompt,非中文原生网感 | 一手(官网) | medium | [T02-S022] |
| **khazix-writer(写长文 skill)** | 给 Agent 装上「卡兹克长文 voice + 节奏 + 四层自检(结构/节奏/内容/语言)」直出长稿 | **行业一手方法论可拆**、MIT、15.2k★;原 voice 偏公众号长文,迁移知乎需调口吻 | 一手(GitHub) | rolling | [T02-S002, T02-S003] |
| **hzwer WritingAIPaper(AI 论文/技术长文写作)** | 学术系/技术干货长文:找核心 idea→搭框架→写引言→提升可读性 | 3.8k★、**有知乎中文版**、学术系知乎博主直接相关;面向论文,泛技术长文需迁移 | 一手(GitHub) | rolling | [T02-S004, T02-S005] |
| **hv-analysis(横纵分析,在 khazix-skills 内)** | 自动联网做历史纵向 + 竞品横向分析,出 1-3万字 PDF 深度报告 | 选题→成稿一体,适合「行业盘点/赛道梳理」型知乎长文;输出偏报告需二次编辑 | 一手(GitHub) | rolling | [T02-S002] |
| ⚠️ **降AI味 / 去AI痕迹工具**(如实标注,**含合规风险**) | 应对平台 AI 检测,改写降「AI率」 | **机械同义替换 / 二次AI洗稿 / 故意加语病多无效或反效果**;**洗稿涉抄袭+违规风险**,知乎重「可信赖」与原创,**不建议作为方法论核心**,仅作认知 | 二手 | medium | [T02-S018] |

> **合规红线(给 Track 03 强标注)**:2026-04-01 起 AI 生成内容**强制标注**正式落地,知乎已上线「AI生成」标签;不标注会**限流/账号处罚**,合规标注反获**流量倾斜 + 信任**。降AI味≠规避标注义务;「洗稿」与知乎可信赖原则冲突。本 track 对「降AI味/洗稿」如实标注为**风险项**,不进 core 工作流。

---

## 环节 3 — 配图 / 图表 / 代码块美化

> 知乎技术长文的差异点:**代码块 + 流程/架构图 + 公式**比配图更刚需。

| 工具 | 场景 | 优劣 | 一手/二手 | Decay | Sources |
|------|------|------|-----------|-------|---------|
| **Carbon** | 把代码片段渲染成美观截图(主题/语法高亮/PNG+SVG 导出) | 免费、开源、主题多、最经典;纯静态截图,不能跑 | 一手(官网+GitHub) | low | [T02-S011, T02-S012] |
| **ray.so** | 代码美图(Raycast 出品),比 Carbon 更现代的预设 | 免费、UI 现代;主题少于 Carbon | 一手(官网) | low | [T02-S013] |
| **Mermaid Live Editor** | 文本语法→流程图/时序图/ER图/架构图;**贴 AI 生成的 mermaid 码即出图** | 与 LLM 配合无缝(让 DeepSeek/Kimi 直接吐 mermaid 码)、版本可控;复杂排版/自定义图标受限 | 一手(官网) | low | [T02-S014] |
| **draw.io** | 拖拽画图 + 支持 mermaid 码;AI 出图后细调/插自定义图标 | 完全免费、无限制、可手动精修;纯手绘效率低于 mermaid | 一手(官网) | low | [T02-S015] |
| **即梦(Jimeng)** | 中文文生图配图 + 智能画布(局部重绘/扩图/抠图/风格保持) + 视频 | 中文语义直出、字节生态、Seedream 系出图快(秒级);审美略逊 MJ | 二手(vendor docs) | medium | [T02-S016] |
| **Midjourney** | 高审美概念配图 / 封面主视觉(SREF 风格参考) | 审美天花板;需订阅、中文字渲染弱、出图慢(30-60s) | 一手(官网) | medium | [T02-S017] |
| **SD(Stable Diffusion)** | 本地批量 / 高度可控配图(LoRA/ControlNet) | 完全可控、可本地、免费;门槛最高、调参重 | 一手 | medium | (推断,行业常识) |

> **知乎专属**:代码块美化(Carbon/ray.so) + Mermaid 图 > AI 生图,是与小红书最大差异。AI 生图(即梦/MJ)主要用于**封面/题图/概念示意**,正文以代码图 + 流程图为主。

---

## 环节 4 — 排版 / 发布 / 数据

| 工具 | 场景 | 优劣 | 一手/二手 | Decay | Sources |
|------|------|------|-----------|-------|---------|
| **知乎官方编辑器** | 最终发布、回答/文章双形态、勾选「AI生成」标签合规 | 唯一发布入口 + 公式渲染原生支持;Markdown 兼容有限,故需 mdnice 中转 | 一手(平台) | low | (平台原生) |
| **mdnice(Markdown Nice)** | **Markdown→知乎**一键排版(主题/图床/脚注/**公式**),解决知乎公式与排版痛点 | 免费、多平台(知乎/公众号/掘金)、公式 OK;粘贴后部分样式仍需微调 | 一手(官网+GitHub) | low | [T02-S009, T02-S010] |
| **知乎创作中心(数据复盘)** | 阅读/赞同/收藏/涨粉数据复盘,唯一一手数据源 | 官方一手数据;无第三方那种竞品横向词库 | 一手(平台) | low | (平台原生) |
| **朱雀 AI 检测**(发布前自检) | 发布前查自己内容的「AI率」,评估限流风险 | 腾讯出品、免费(每日20次)、文/图/视频、三模式;非官方判定,仅参考 | 一手(官网) | medium | [T02-S018] |

> **知乎缺口**:无成熟对标小红书「千瓜/新红」的第三方知乎数据复盘 SaaS(选题靠热榜工具,复盘靠官方后台)。这是知乎 vs 小红书的工具生态结构差异。

---

## Phase 2 接口

### Core 工具栈(按环节,最小可用集)

1. **找选题/搜证**:秘塔AI搜索(搜证+学术) + 四六啦/八爪鱼(知乎热榜) + AI HOT 日报(AI 选题) + Kimi/Perplexity(深度搜索)。[T02-S001/S006/S007/S008/S019/S023]
2. **写作**:DeepSeek(干货逻辑) 或 Kimi(长文/对标) 为主力 + 豆包(标题/网感) 调味 + khazix-writer(长文 skill) / WritingAIPaper(学术技术长文) 作方法论层。[T02-S020/S019/S021/S003/S004]
3. **配图/图表/代码**:Carbon/ray.so(代码美图) + Mermaid+draw.io(流程/架构图) + 即梦/MJ(封面概念图)。[T02-S011/S013/S014/S015/S016/S017]
4. **排版/发布/数据**:mdnice(MD→知乎+公式) → 知乎编辑器(发布+AI标签) → 创作中心(复盘);发布前朱雀自检(可选)。[T02-S009/S018]

### 选型决策树(给 Track 03 workflow)

```
你要做哪类知乎 AI 内容?
├─ 干货/技术拆解长文
│   ├─ 搜证: 秘塔(研究模式) + Kimi(喂多篇对标抽结构)
│   ├─ 写作: DeepSeek 主力 + WritingAIPaper/khazix-writer 方法论
│   └─ 图: 代码→Carbon/ray.so;架构→Mermaid+draw.io;公式→mdnice
├─ AI 赛道资讯/盘点长文
│   ├─ 选题: AI HOT 日报 + 知乎热榜(四六啦)
│   ├─ 写作: hv-analysis(横纵盘点出报告) → 人工精修 + 豆包调网感
│   └─ 图: 即梦/MJ 题图 + Mermaid 时间线
└─ 观点/讨论型回答
    ├─ 选题: 知乎热榜(四六啦/八爪鱼) 抓正在热的问题
    ├─ 写作: 豆包(网感开头) + DeepSeek(论证) ;短则直接编辑器
    └─ 排版: mdnice 轻排 → 知乎编辑器

发布前(所有类型): 勾选「AI生成」标签(2026-04 强制) → 朱雀自检风险 → 创作中心复盘
```

### 给 Track 03 workflow 的接口
- **环节顺序固化**:选题(热榜+AI HOT)→搜证(秘塔/Kimi)→成稿(DeepSeek/Kimi + 长文skill)→图(代码/流程/公式)→排版(mdnice)→发布(知乎编辑器+AI标签)→复盘(创作中心)。
- **合规节点**:写作环节标注「降AI味/洗稿=风险项,不入 core」;发布环节强制「AI生成标签」节点(限流红线)。
- **知乎差异点喂给 workflow**:① 代码/图表/公式渲染 > 配图美学;② 缺第三方数据词库,选题更靠热榜+AI搜索;③ 长文+可信赖→搜证工具权重高。

### 新 figure 候选(给 Track 01)
- 无新增 figure(秘塔/月之暗面/字节均为公司主体);**hzwer(黄哲威)+ 丁霄汉(DingXiaoH)** 已在 Track 05/01 锚定,作为「学术系知乎 AI 博主 + 写作方法论作者」双重身份再确认。卡兹克(khazix)同。

---

## 质量自检

- [x] 工具/源数量 ≥15:**Source Manifest 25 条**,覆盖工具约 **24 个**(秘塔/四六啦/八爪鱼/AI HOT/Kimi/Perplexity/Claude/GPT/DeepSeek/豆包/khazix-writer/hv-analysis/WritingAIPaper/降AI味工具/Carbon/ray.so/Mermaid/draw.io/即梦/MJ/SD/知乎编辑器/mdnice/朱雀/创作中心)。✅
- [x] 覆盖 4 环节(选题搜证 / 写作改写 / 配图图表代码 / 排版发布数据)全。✅
- [x] Wave 1 全部种子收录并展开:khazix-writer[S002/S003]、WritingAIPaper[S004]、四六啦/八爪鱼[S006/S007]、秘塔[S001]。✅
- [x] 每条标一手/二手 + bucket + [T02-S00X] evidence。✅
- [x] 黑名单合规:无 mp.weixin/百度/CSDN/简书/掘金/搜狐作事实源;知乎站内未作事实来源。✅
- [x] 近12个月颠覆性新工具已识别:**写长文/方法论 AI Skill 生态**(khazix-skills 15.2k★、装进 Claude Code/Codex 即用)= 本赛道最大新变量;**秘塔「研究模式」+ Perplexity/Kimi Deep Research** 把「搜证」从人工变 Agent;**2026-04 AI 标识强制**重塑发布合规。✅
- [x] 商业 SaaS 官网=verified_primary,docs 子页=surrogate_primary,媒体=secondary,分级正确。✅
- [x] last_checked 全 = 2026-06-15。✅
- [⚠] **已知缺口(诚实标注)**:① 知乎无对标千瓜的第三方数据词库 SaaS;② 卡兹克/丁霄汉最厚长文方法论仍在公众号/知乎站内(黑名单边界),仅取 GitHub 非黑名单部分;③ 降AI味/洗稿类工具刻意未深挖(合规风险,标为风险项)。
