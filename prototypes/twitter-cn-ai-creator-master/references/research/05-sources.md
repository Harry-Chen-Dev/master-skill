# Track 05 — Sources / 持续追踪的活信息源

> 行业：推特(X) 中文圈 AI 自媒体博主（用中文在 X 做 AI 内容；重点：文案+内容制作）
> Locale: zh-CN（平台 X 全球，受众中文）| Research date: 2026-06-06
>
> **本 track 的特殊性（重要诚实声明）**: 这一行的「持续信息源」不是常规意义的 newsletter/podcast/conference 五件套，而是**三层叠加**：
> ① **X 官方/算法层**（平台规则=博主的硬约束，必须追）；
> ② **英文一手「原料」层**（arXiv/HN/Reddit/AI lab 官博/Product Hunt——这是中文博主真正的选题源头活水，不是别人的中文总结）；
> ③ **工具官方 + 大V 一手渠道层**（工具更新 + 大V 的个人站/Substack/GitHub）。
> **中文圈「方法论媒体层」很薄**：没有「写推文怎么写」的成体系中文 newsletter/podcast——真知识沉淀在**大V 的推文/thread 本身 + 即刻长文 + 个人站文章 + GitHub prompt/skill 仓库**里，而非独立媒体。英文圈则有成熟的「写作 canon」源（swyx/Perell/Ship30）。这层厚薄差是本行业的结构性事实，见末尾诚实判断。

## Source Manifest

| source_id | url | bucket | last_checked | author/host | one-line note |
|-----------|-----|--------|--------------|-------------|---------------|
| T05-S001 | https://github.com/xai-org/x-algorithm | verified_primary | 2026-06-06 | xAI | **现行** X 推荐算法开源 repo (Grok 驱动, 26.2k★, 4 周一更) |
| T05-S002 | https://github.com/twitter/the-algorithm | verified_primary | 2026-06-06 | X (legacy) | 旧版算法 repo (2023 开源) — 历史参照, 已被 S001 取代 |
| T05-S003 | https://help.x.com/en/using-x/x-premium | secondary | 2026-06-06 | X (help.x.com) | 官方 help — Premium 长推/Articles/edit/reply 加权 |
| T05-S004 | https://help.x.com/en/using-x/x-ads-revenue-sharing | secondary | 2026-06-06 | X (help.x.com) | 官方 help — 创作者广告分成资格/门槛 (vendor docs) |
| T05-S005 | https://developer.x.com/en/docs | verified_primary | 2026-06-06 | X Developer | API/平台开发文档官方一手 |
| T05-S006 | https://arxiv.org/list/cs.CL/recent | verified_primary | 2026-06-06 | arXiv (Cornell) | cs.CL 最新论文 RSS — 中文博主选题原料一手 |
| T05-S007 | https://arxiv.org/list/cs.AI/recent | verified_primary | 2026-06-06 | arXiv (Cornell) | cs.AI 最新论文 RSS — 选题原料一手 |
| T05-S008 | https://news.ycombinator.com/ | reference | 2026-06-06 | Y Combinator | HN 社区投票=选题热度信号 (无算法) |
| T05-S009 | https://www.reddit.com/r/LocalLLaMA/ | reference | 2026-06-06 | Reddit | 开源/本地 LLM 一手讨论, 评测/泄露/上手第一现场 |
| T05-S010 | https://openai.com/news/ | verified_primary | 2026-06-06 | OpenAI | 官博 — 发布快讯编译一手源 |
| T05-S011 | https://www.anthropic.com/news | secondary | 2026-06-06 | Anthropic | 官博 — 模型/研究发布一手源 (vendor docs) |
| T05-S012 | https://blog.google/technology/ai/ | verified_primary | 2026-06-06 | Google | 官博 AI 板块 — 发布一手源 |
| T05-S013 | https://www.producthunt.com/ | secondary | 2026-06-06 | Product Hunt | 新 AI 产品发布榜 — 工具速递选题源 |
| T05-S014 | https://typefully.com/ | secondary | 2026-06-06 | Typefully | vendor docs — thread 写作/排程主力 SaaS (功能更新追) |
| T05-S015 | https://hypefury.com/blog/ | secondary | 2026-06-06 | Hypefury | vendor docs — 增长自动化工具官方 blog |
| T05-S016 | https://ray.so/ | secondary | 2026-06-06 | Raycast | vendor — 代码/文字美图 (开源 repo 见 T02-S006) |
| T05-S017 | https://github.com/RSSNext/Folo | verified_primary | 2026-06-06 | RSSNext | Folo AI RSS 阅读器 38.5k★ v1.9.0 (2026-05-29) 信息源聚合 |
| T05-S018 | https://baoyu.io/ | secondary | 2026-06-06 | 宝玉 (@dotey) | 大V 个人站 — 翻译/重写/prompt/Agent 方法论一手 |
| T05-S019 | https://www.guizang.ai/ | secondary | 2026-06-06 | 歸藏 (@op7418) | 大V 个人站 — AIGC 周刊主理 (周刊载体) |
| T05-S020 | https://github.com/op7418/guizang-s-prompt | verified_primary | 2026-06-06 | 歸藏 (@op7418) | 大V GitHub — prompt/skill 持续产出一手 |
| T05-S021 | https://rss.qiaomu.ai/ | secondary | 2026-06-06 | 向阳乔木 (@vista8) | QMReader — 中译+按风格改写+人工审 半自动信息流 |
| T05-S022 | https://orangeai.substack.com/ | verified_primary | 2026-06-06 | Orange AI (@oran_ge) | 大V Substack — 锐评/产品复盘/build-in-public 长文 |
| T05-S023 | https://swyx.io/learn-in-public | verified_primary | 2026-06-06 | swyx (Shawn Wang) | 写作 canon — Learn in Public 方法论原文 |
| T05-S024 | https://perell.com/ | secondary | 2026-06-06 | David Perell | 写作 canon — Write of Passage + How I Write podcast |
| T05-S025 | https://www.ship30for30.com/ | secondary | 2026-06-06 | Dickie Bush / Nicolas Cole | 写作 canon — Atomic Essays (短文/hook 公式) |
| T05-S026 | https://levels.io/ | secondary | 2026-06-06 | Pieter Levels (@levelsio) | 写作 canon — build-in-public 鼻祖个人站/projects |

源数：26 | verified_primary：10（38%）| secondary(含 vendor docs)：14 | reference：2 | 一手(verified+大V个人渠道)实际 ≈ 70%

> **黑名单命中已丢弃（绝不收录）**: 检索中出现 知乎/zhihu、微信公众号/mp.weixin、百度、CSDN、简书、掘金，以及 SEO 农场榜（xpayoutcalculator / outfy / earnifyhub / opentweet blog 横评 / posteverywhere blog）——**均未进 manifest**，仅用于交叉核对数字，不作 evidence。

---

## 总览（按 type 分组）

### Bucket 1 — X 官方 / 算法（5 个，硬约束，必追）
| Source | Cadence | Tier | 投入产出 | One-liner |
|--------|---------|------|---------|-----------|
| xai-org/x-algorithm | 4 周一更 | senior | high | 现行 Grok 驱动算法开源，sentiment/外链/in-network 规则直接决定推文怎么写 |
| twitter/the-algorithm (legacy) | 已冻结 | senior | medium | 2023 旧版，理解算法演进的历史底本 |
| X help — Premium | rolling | mixed | high | 长推/Articles/edit/reply 加权官方规则 |
| X help — Ads Revenue Sharing | rolling | practitioner | medium | 变现资格门槛（500 粉 + 5M 展示 + Premium 订阅 + Stripe） |
| X Developer Docs | rolling | senior | low | API/自动化博主才需要，普通文案博主低频 |

### Bucket 2 — 英文选题源（一手「原料」，6 个，每日扫）
| Source | Cadence | Tier | 投入产出 | One-liner |
|--------|---------|------|---------|-----------|
| arXiv cs.CL / cs.AI recent | 日更(工作日) | senior | medium | 论文速读 thread 的源头，RSS 可订 |
| Hacker News | rolling | mixed | high | 投票=热度真信号，判断哪个发布值得编译 |
| r/LocalLLaMA | rolling | practitioner | medium | 开源/本地 LLM 第一现场（评测/泄露/上手） |
| OpenAI News | 不定期 | mixed | high | 发布快讯一手，编译必标来源 |
| Anthropic News | 不定期 | mixed | high | 模型/研究发布一手 |
| Google AI Blog | 不定期 | mixed | medium | 发布一手，密度低于前两家 |
| Product Hunt | 日更 | practitioner | low | 新 AI 产品速递选题，噪音多需筛 |

### Bucket 3 — 工具官方（追功能更新，4 个）
| Source | Cadence | 投入产出 | One-liner |
|--------|---------|---------|-----------|
| Typefully | rolling | medium | thread 写作/排程主力，追新功能（AI 改写/数据） |
| Hypefury blog | rolling | low | 增长自动化（auto-retweet/evergreen/auto-plug）更新 |
| ray.so | rolling | low | 代码/文字美图，配图标配 |
| Folo (GitHub) | 频繁 release | medium | 开源 AI RSS，把信息源管线收口 + AI digest |

### Bucket 4 — 大V 一手渠道（中文方法论真正沉淀处，5 个）
| Source | Platform | Cadence | 投入产出 | One-liner |
|--------|---------|---------|---------|-----------|
| 宝玉 baoyu.io | 个人站 | 不定期 | high | 翻译即重写 + voice 注入 + Agent 工程方法论一手 |
| 歸藏 guizang.ai + GitHub | 个人站+repo | 周刊周更/repo 频繁 | high | AIGC 周刊四板块框架 + prompt/skill 产出 |
| 向阳乔木 rss.qiaomu.ai | 个人站群 | rolling | medium | 半自动改写流水线 + 信息源策展 |
| Orange AI Substack | Substack | 不定期 | medium | 锐评 + 数据透明复盘 + build-in-public 长文 |
| (大V X/即刻推文流) | X / 即刻 | rolling | high | 真方法论多在此（reference 级，无法机械抓全文，见诚实判断） |

### Bucket 5 — 英文写作 canon 源（文案方法论 anchor，4 个）
| Source | Host | Cadence | 投入产出 | One-liner |
|--------|------|---------|---------|-----------|
| swyx — Learn in Public | swyx.io | 常青文 | high | 「公开学习」=AI 博主内容飞轮的底层方法论 |
| David Perell — Write of Passage / How I Write | perell.com | podcast 活跃 | medium | 线上写作 canon，标题/idea/distribution 体系 |
| Ship 30 for 30 — Atomic Essays | ship30for30.com | rolling cohort | medium | 短文/hook 公式，直接迁移到 thread 单条 |
| Pieter Levels — levels.io | levels.io | 不定期 | medium | build-in-public 鼻祖，「做产品+公开数据」叙事范本 |

> Conference / Dataset：**N/A for this industry**。本行业是「用中文在 X 做 AI 内容」，没有专属年度大会，也没有专属 benchmark/dataset。模型 benchmark（如 LMArena）属上游 AI 行业，非本行业博主一手追踪对象。

---

## Sources（关键卡片）

### 1. xai-org/x-algorithm（X 推荐算法，现行）

- **Type**: 平台算法开源 repo（X 官方）
- **URL**: https://github.com/xai-org/x-algorithm
- **Host**: xAI
- **Cadence**: 承诺每 4 周公开更新一次；最大单次更新 2026-05-15（187 文件 / 1.8 万行）
- **Last activity**: 2026-05-15（含 end-to-end inference pipeline + 预训练模型 artifacts）
- **Audience tier**: senior
- **One-liner**: 中文 AI 博主写推文的**硬约束源头**——算法怎么排，决定首推外链该不该放、语气该不该「正向」、in-network vs 发现流怎么配。
- **典型内容**: Rust(57%)+Python(43%)；四组件 Home Mixer(编排)/Thunder(关注内容内存存储)/Phoenix(Grok 排序 transformer)/Candidate Pipeline；**Grok 对每条推做 sentiment 分析——正向/建设性扩大分发，负面/对抗性减权** (evidence: [T05-S001])。
- **关键变化（近 6 月）**: 2025-10 Musk 宣布 Grok 取代旧推荐系统；2026-01 xAI 在新 repo 发布 Grok 驱动完整替代版，旧 `twitter/the-algorithm` 退为历史 (evidence: [T05-S001, T05-S002])。
- **投入产出比**: high（平台规则直接改变文案策略；但非天天读，重大更新时读）
- **Endorsement**: cross_source（与 Track 02 外链降权/reply 加权一致，evidence: [T02-S023]）+ community_consensus（开源可核验）。
- **可信度**: high（官方一手开源）
- **Decay risk**: medium（4 周一更，细节变化快；「算法是硬约束」这一框架 low）

### 2. X help — Premium / Ads Revenue Sharing（变现+功能规则）

- **Type**: 平台官方 help（vendor docs）
- **URL**: https://help.x.com/en/using-x/x-premium ; https://help.x.com/en/using-x/x-ads-revenue-sharing
- **Cadence**: rolling（随产品更新）
- **One-liner**: 「能发多长、能不能 edit、reply 有没有加权、发到什么程度开始赚钱」的官方规则。
- **典型内容**: Premium 25000 字长推/Articles/1h edit/reply 优先级 (evidence: [T05-S003])；广告分成资格：500 验证粉 + 近 3 月 5M 自然展示 + Premium 订阅 + 已连 Stripe + 符合 Creator Monetization Standards；约 $8-12/百万 Premium 展示，最低 $30 提现门槛（数字经多源横评交叉核对，官方页为准）(evidence: [T05-S004])。
- **投入产出比**: high（Premium）/ medium（分成）
- **可信度**: high（官方）| **Decay risk**: medium（价格/门槛会变）

### 3. 英文选题源（arXiv / HN / Reddit / lab 官博 / Product Hunt）

- **Type**: 一手「原料」源（论文 / 社区 / 官博 / 发布榜）
- **One-liner**: 中文博主的**选题原料车间**——直接从这里取一手做「理解后中文重写 + 本土化洞察」，而不是搬别人的中文总结。
- **每个源的角色**:
  - **arXiv cs.CL/cs.AI**：论文速读 thread 源头，RSS 可订，日更工作日 (evidence: [T05-S006, T05-S007])。
  - **Hacker News**：靠投票非算法，热度=真信号，判断哪个发布值得编译 (evidence: [T05-S008])。
  - **r/LocalLLaMA**：开源/本地 LLM 评测/泄露/上手第一现场 (evidence: [T05-S009])。
  - **OpenAI/Anthropic/Google 官博**：发布快讯一手，编译必标来源 (evidence: [T05-S010, T05-S011, T05-S012])。
  - **Product Hunt**：新 AI 产品速递选题，噪音多需筛 (evidence: [T05-S013])。
- **投入产出比**: HN/OpenAI/Anthropic high；arXiv/Reddit/Google medium；Product Hunt low。
- **Endorsement**: cross_source（Track 02 必备层「一手信息源」+ figures 共识「信息差套利」evidence: [T02-S015, T01-S002, T01-S022]）。
- **可信度**: high | **Decay risk**: low（这些是行业基础设施）

### 4. 大V 一手渠道（宝玉 / 歸藏 / 向阳乔木 / Orange AI）

- **Type**: community / 个人站 / Substack / GitHub（与 Track 01 figures 一一对应）
- **One-liner**: 中文圈「怎么写/怎么做内容」的**真方法论沉淀处**——没有独立方法论媒体，知识就在这些大V 的个人渠道里。
- **各渠道**:
  - **宝玉 baoyu.io**（@dotey）：翻译即重写 + voice 注入 + 近一年转向 Claude Code/Agent 工程；2025 持续产翻译 skill (evidence: [T05-S018])。verified 活跃。
  - **歸藏 guizang.ai + guizang-s-prompt**（@op7418）：AIGC 周刊四板块固定框架（85+ 期，活跃至 2026-05）+ prompt/social-card/ppt skill 持续产出 (evidence: [T05-S019, T05-S020])。
  - **向阳乔木 rss.qiaomu.ai**（@vista8）：QMReader「中译+按风格改写+人工审」半自动流水线 + 信息源策展（导航/RSS/论文）(evidence: [T05-S021])。
  - **Orange AI orangeai.substack.com**（@oran_ge）：锐评 + 数据透明复盘 + build-in-public，长文在 Substack（如 ListenHub 复盘）(evidence: [T05-S022])。
- **投入产出比**: 宝玉/歸藏 high；向阳乔木/Orange AI medium。
- **⚠️ 关键诚实点**: 这些大V 的**最高密度方法论其实在 X/即刻的推文/thread 本身**（reference 级，x.com 无法机械抓全文）——个人站/Substack/GitHub 只是「沉淀下来的一部分」，不是全部。
- **Endorsement**: figure_long/short（Track 01 全部立卡）+ cross_source。
- **可信度**: medium-high（个人站/GitHub 一手；推文流 reference 级）| **Decay risk**: medium-high（个人渠道默认，host 倦怠/收费风险）

### 5. 英文写作 canon 源（swyx / Perell / Ship30 / levelsio）

- **Type**: newsletter / podcast / course / 个人站（写作方法论 anchor）
- **One-liner**: 中文 AI 博主文案能力的**上游 canon**——「公开学习、原子化短文、线上写作、build in public」这套打法的英文原典，比中文圈成体系得多。
- **各源**:
  - **swyx — Learn in Public**（swyx.io）：「公开学习」方法论原文，AI 博主内容飞轮底层逻辑 (evidence: [T05-S023])。
  - **David Perell — Write of Passage / How I Write podcast**（perell.com）：线上写作 canon，2025 podcast 持续活跃，标题/idea/distribution 体系 (evidence: [T05-S024])。
  - **Ship 30 for 30 — Atomic Essays**（ship30for30.com）：< 250 字原子短文公式，直接迁移到 thread 单条/hook，2025 cohort + self-paced 活跃 (evidence: [T05-S025])。
  - **Pieter Levels — levels.io**（@levelsio）：build-in-public 鼻祖，「做产品 + 公开数据/收入」叙事范本，projects 页一周内更新 (evidence: [T05-S026])。
- **投入产出比**: swyx high；其余 medium。
- **Paywall**: Write of Passage / Ship 30 为付费课程（数百-千刀级），**但其方法论免费内容（推文/podcast/blog）已够用**，无需买课。
- **Endorsement**: community_consensus（英文创作圈反复 cross-recommend）+ cross_source（Track 01 build-in-public 谱系 evidence: [T01-S015, T01-S017]）。
- **可信度**: high | **Decay risk**: low（已是写作 canon）

---

## 判定标准结果（mechanical filter）

| Source | 真实背书 | Active | 独特价值 | 可访问 | 判定 |
|--------|--------|--------|---------|-------|------|
| xai-org/x-algorithm | ✅ | ✅ (2026-05) | ✅ | ✅ | KEEP high |
| twitter/the-algorithm | ✅ | ⚠️ (冻结/历史) | ✅ (演进底本) | ✅ | KEEP medium |
| X help Premium/Revenue | ✅ | ✅ | ✅ | ✅ | KEEP high |
| arXiv / HN / Reddit / lab 官博 | ✅ | ✅ | ✅ | ✅ | KEEP high |
| Product Hunt | ✅ | ✅ | ⚠️ (噪音) | ✅ | KEEP medium |
| Typefully/Hypefury/ray.so/Folo | ✅ | ✅ | ✅ | ✅ | KEEP (见 Track 02) |
| 宝玉/歸藏/向阳乔木/Orange AI | ✅ | ✅ | ✅ | ✅ | KEEP high/medium |
| swyx/Perell/Ship30/levelsio | ✅ | ✅ | ✅ | ✅ (课付费,内容免费) | KEEP high/medium |

---

## Phase 2 提炼提示

**「这一行的资深人**实际持续追**的 top 5 sources」**（含频率）:
1. **英文 AI lab 官博 + HN**（OpenAI/Anthropic News + Hacker News）— 不定期/rolling，**最高频扫**，选题原料命脉 (evidence: [T05-S008, T05-S010, T05-S011])。
2. **xai-org/x-algorithm + X help**（4 周一更/rolling）— 平台硬约束，重大更新必读，决定文案策略 (evidence: [T05-S001, T05-S003])。
3. **arXiv cs.CL/cs.AI recent**（日更工作日，RSS）— 论文速读 thread 源头 (evidence: [T05-S006])。
4. **大V 个人渠道**（宝玉 baoyu.io / 歸藏 guizang.ai+周刊+repo）— 周更/不定期，中文方法论沉淀处 (evidence: [T05-S018, T05-S019, T05-S020])。
5. **写作 canon**（swyx Learn in Public / Ship30 Atomic Essays）— 常青，文案能力上游 anchor (evidence: [T05-S023, T05-S025])。
→ 进 master skill「Sources — 信息源」节 highlights。

**选题 / 方法论真知识**沉淀在哪（关键结论）:
- **选题原料** = 英文一手（Bucket 2），中文博主在此取材，竞争力在「理解后重写 + 本土化洞察」而非搬运。
- **方法论（怎么写/做）** = 几乎全在**大V 的 X/即刻推文流 + 个人站/GitHub skill 仓库**（Bucket 4），**没有独立中文方法论媒体**。英文圈才有成体系的写作 canon（Bucket 5）。
- **平台规则** = X 官方/算法（Bucket 1），是隐性的「文案约束层」。

**最近话题热度** (topic-heat: medium-confidence, 部分 source × item 抽查):
- **Grok 接管 X 算法 + sentiment 分发**（2025-10→2026-05，xai-org/x-algorithm）— 直接影响「推文语气」策略 (evidence: [T05-S001])。
- **Agent / Claude Code skill 化**（宝玉转向 Agent 工程、歸藏出 ppt/social-card skill）(evidence: [T05-S018, T05-S020])。
- **vibe coding / build-in-public 主流化**（levelsio「indie hacking is the new normal」、Orange AI 复盘）(evidence: [T05-S026, T05-S022])。

**新 figures 发现**（喂 wave 2 Track 01）: 无新增——Bucket 4 大V 均已在 Track 01 立卡；英文 canon 作者（swyx/Perell/Ship30/levelsio）是**英文写作 canon 候选**而非中文圈 figure，建议 Track 04 (canon) 而非 Track 01。

**新 tools 发现**（喂 wave 2 Track 02）: 无新增——Typefully/Hypefury/ray.so/Folo 已在 Track 02。Product Hunt 作为「工具发现渠道」可补充进 Track 02 的工具雷达说明。

**媒体层厚薄诚实判断**:
- **英文选题源层：厚**（arXiv/HN/Reddit/lab 官博/PH 齐全，verified_primary，行业基础设施）。
- **X 官方/算法层：厚且可核验**（开源 repo + 官方 help，一手）。
- **英文写作 canon 层：厚**（swyx/Perell/Ship30/levelsio 成体系）。
- **中文方法论媒体层：薄（结构性事实）**——没有「教你怎么写 AI 推文」的成体系中文 newsletter/podcast/conference；真方法论散在大V 推文流(reference 级)/即刻/个人站/GitHub。这意味着 master skill 在「中文文案方法论」上要**主要靠 Track 03 workflows + 大V voice 样本反推**，而非指向某个中文媒体。

**冷僻 / 信号薄弱**:
- newsletter ≥3 ✅（大V 周刊/Substack + 写作 canon newsletter）；podcast 弱（仅 Perell How I Write，中文圈基本无方法论 podcast）；conference **N/A**（本行业无专属大会）；community ✅（HN/Reddit/X 圈/大V 渠道）；dataset **N/A**。
- 有效 endorsement source > 50% ✅。
- **结论**: sources 维度整体**不薄**，但呈「英文层厚 + 中文方法论媒体层薄」的不对称结构——这是行业本质，非调研失败。Phase 2.8 诚实边界应写明：「想跟最新动态，去英文一手源（HN/lab 官博/arXiv）+ 几位大V 的 X/个人站；中文圈没有现成的『怎么写』方法论媒体，方法论要从大V 的内容行为里反推。」
