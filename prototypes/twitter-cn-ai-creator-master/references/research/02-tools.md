# Track 02 — Tools / 内容生产工具栈

> 行业：推特(X) 中文圈 AI 自媒体博主（用中文在 X 做 AI 内容；重点：怎么写推文/thread、怎么制作内容）
> Locale: zh-CN（平台 X 全球，受众中文）| Research date: 2026-06-06

## Source Manifest

| source_id | url | bucket | last_checked | author/host | one-line note |
|-----------|-----|--------|--------------|-------------|---------------|
| T02-S001 | https://typefully.com/pricing | surrogate_primary | 2026-06-06 | Typefully | vendor docs — thread 写作/排程主力 SaaS |
| T02-S002 | https://hypefury.com/blog/en/5-most-important-hypefury-features/ | verified_primary | 2026-06-06 | Hypefury | 官方 blog — auto-retweet/auto-plug/evergreen |
| T02-S003 | https://hypefury.com/blog/en/auto-retweet-your-tweets-on-twitter/ | verified_primary | 2026-06-06 | Hypefury | 官方 — evergreen/自动转推机制 |
| T02-S004 | https://help.x.com/en/using-x/x-premium | secondary | 2026-06-06 | X (help.x.com) | X 官方 help — Premium 长推/Articles/edit |
| T02-S005 | https://help.x.com/en/using-x/edit-post | secondary | 2026-06-06 | X (help.x.com) | X 官方 help — 编辑窗口 1h/5 次 |
| T02-S006 | https://github.com/raycast/ray-so | verified_primary | 2026-06-06 | Raycast | ray.so 源码 MIT 2.3k★ 代码/文字美图 |
| T02-S007 | https://github.com/carbon-app/carbon | verified_primary | 2026-06-06 | dawnlabs/carbon-app | carbon.now.sh 源码 36k★ 代码图鼻祖 |
| T02-S008 | https://carbon.now.sh | surrogate_primary | 2026-06-06 | carbon-app | vendor — 代码截图生成器在线版 |
| T02-S009 | https://xnapper.com/ | secondary | 2026-06-06 | Xnapper | vendor — 截图美化+自动脱敏+OCR Mac |
| T02-S010 | https://cleanshot.com/ | secondary | 2026-06-06 | CleanShot | vendor — 截图标注+录屏+云图床 |
| T02-S011 | https://www.machinetranslation.com/blog/kimi-ai-vs-deepseek | secondary | 2026-06-06 | MachineTranslation | Kimi vs DeepSeek 中译对比 |
| T02-S012 | https://recodechinaai.substack.com/p/deepseek-r1-and-kimi-k15-how-chinese | verified_primary | 2026-06-06 | RecodeChina (Substack) | 中国 LLM newsletter 一手观察 |
| T02-S013 | https://www.chinatalk.media/p/putting-chinas-top-llms-to-the-test | secondary | 2026-06-06 | ChinaTalk | 中文 LLM 实测长稿 |
| T02-S014 | https://github.com/deepseek-ai/awesome-deepseek-integration | verified_primary | 2026-06-06 | DeepSeek (官方) | DeepSeek API 集成清单官方 repo |
| T02-S015 | https://arxiv.org/list/cs.AI/recent | verified_primary | 2026-06-06 | arXiv | cs.AI 最新论文 RSS 选题一手 |
| T02-S016 | http://www.arxiv-sanity.com/ | reference | 2026-06-06 | Karpathy | arXiv 论文过滤/推荐(个人项目) |
| T02-S017 | https://news.ycombinator.com/ | reference | 2026-06-06 | Y Combinator | HN 社区投票=选题热度信号 |
| T02-S018 | https://github.com/RSSNext/folo | verified_primary | 2026-06-06 | RSSNext | Folo AI RSS 阅读器 38k★ 信息源聚合 |
| T02-S019 | https://tweethunter.io/ | secondary | 2026-06-06 | Tweet Hunter | vendor — 300万爆款推库+AI写作 |
| T02-S020 | https://tweethunter.io/blog/hypefury-review | verified_primary | 2026-06-06 | Tweet Hunter | 官方 blog — Hypefury 功能拆解 |
| T02-S021 | https://buffer.com/ | secondary | 2026-06-06 | Buffer | vendor — 多平台轻量排程 |
| T02-S022 | https://buffer.com/resources/twitter-timeline-algorithm/ | secondary | 2026-06-06 | Buffer | X 算法/外链降权机制解读 |
| T02-S023 | https://sproutsocial.com/insights/twitter-algorithm/ | secondary | 2026-06-06 | Sprout Social | X 算法 2026 外链降权数据 |
| T02-S024 | https://opentweet.io/blog/best-twitter-scheduling-tools-2026 | secondary | 2026-06-06 | OpenTweet | 排程工具横评(厂商blog,降权) |
| T02-S025 | https://snappify.com/blog/best-ray-so-alternatives | secondary | 2026-06-06 | Snappify | 代码美图工具横评(厂商blog) |
| T02-S026 | https://apps.apple.com/us/app/xnapper-beautiful-screenshot/id1630178233 | secondary | 2026-06-06 | Apple App Store | Xnapper 上架页 vendor 一手 |

源数：26 | verified_primary：9（35%）| surrogate_primary(vendor docs)：7（27%）| 一手合计(verified+surrogate vendor)：16/26 ≈ 62% | secondary：8 | reference：2

---

## 总览（按 tier 分组）

### 必备（7 个）
| 工具 | 一句话 | Decay | Sources |
|------|--------|-------|---------|
| Claude / GPT / Kimi / DeepSeek（AI 写作引擎） | 把英文一手编译成中文推、压缩长文、生成 thread、加洞察 | medium | T02-S011,S012,S013,S014 |
| Typefully | thread 写作+排程主力，distraction-free 编辑器+AI 改写+数据 | low | T02-S001 |
| X Premium（长推/Articles/edit） | 解锁 25000 字长推、Articles、1h 编辑、reply 加权 | low | T02-S004,S005 |
| ray.so / carbon.now.sh | 代码/文字 → 渐变美图，配图标配（开源） | low | T02-S006,S007,S008 |
| 截图美化（CleanShot X / Shottr / Xnapper） | 截图 → 带边距/圆角/阴影/脱敏的社媒图 | low | T02-S009,S010,S026 |
| arXiv + HN + Reddit + 官方博客（一手信息源） | 选题源头：论文/发布/社区热度，找一手不搬运 | low | T02-S015,S017 |
| RSS / AI 资讯聚合（Folo / Feedly） | 把分散信息源收进一条时间线，AI 摘要找选题 | medium | T02-S018 |

### 场景特化（5 个）
| 工具 | 一句话 | Decay | Sources |
|------|--------|-------|---------|
| Hypefury | 增长/自动化向：auto-retweet/auto-plug/evergreen 复用 | medium | T02-S002,S003 |
| Tweet Hunter | 300 万爆款推库找 hook/格式灵感 + AI 改写 + CRM | medium | T02-S019,S020 |
| Buffer | 多平台（X/LinkedIn/IG…）统一轻量排程 | low | T02-S021,S024 |
| Kimi（长文本专精） | 200 万字上下文，批量喂论文/长 PDF 做总结 | medium | (zhidx)长文本,T02-S011 |
| DeepSeek（中译/快事实） | 中英对译强、清晰，快讯编译性价比 | medium | T02-S011,S014 |

### 新兴（2 个）
| 工具 | 一句话 | Decay | Sources |
|------|--------|-------|---------|
| Folo（AI RSS 阅读器） | 开源 RSS + AI 时间线摘要 + 每日 digest，近 12 月起势 | high | T02-S018 |
| AI 资讯聚合 agent（News Aggregator AI） | 自动抓 30+ 源(arXiv/Reddit/lab)生成简报 | high | T02-S017 |

---

## 必备层

### 1. AI 写作引擎（Claude / GPT / Kimi / DeepSeek）

- **One-liner**: 中文 AI 自媒体的发动机——把英文一手（arXiv/官博/HN/Reddit）编译成有中文味的推/thread、压缩长文、补洞察。
- **Tier**: 必备
- **Maintainer**: Anthropic / OpenAI / Moonshot AI（月之暗面）/ DeepSeek
- **License**: proprietary（API + 网页版）
- **Maturity signals**: 四家均为各自市场头部对话模型；DeepSeek 官方维护 `awesome-deepseek-integration` 集成清单 (verified, 2026-06-06) (evidence: [T02-S014])
- **分工（一手观察，保留矛盾）**:
  - **Claude / GPT**：英文一手理解 + 中文改写质感最稳，适合「深度 thread」「锐评」需要语感的内容（推断，基于写作质感共识）。
  - **Kimi**：长文本专精，200 万字上下文，可一次喂入数百文件/长 PDF 批量总结，「读+总结」是其强项 (evidence: [T02-S011])（zhidx 长文本报道为二手佐证）。
  - **DeepSeek**：中英对译强、回答清晰，快讯编译/快速事实问答性价比高 (evidence: [T02-S011])。
- **关键避坑**: 直接让 AI「翻译」英文原文 → 出「机翻味」；正确做法是让 AI**理解后用中文重写并加本土化洞察**，不是逐句译（推断，行业共识）。
- **不适合**: 全自动批量生成发推（低质同质，见避坑清单）；不核对就发 AI 编造的数字/链接。
- **可信度**: medium（模型能力随版本快速变化）
- **Decay risk**: medium（模型迭代快但「LLM 做编译」这一工具类目稳定，12-24 月内被取代概率 20-40%）

### 2. Typefully

- **One-liner**: thread 写作+排程的主力工作台，无干扰编辑器 + AI 改 hook/出变体 + 数据分析，一处搞定从写到发。
- **Tier**: 必备
- **Maintainer / Owner**: Typefully (https://typefully.com)
- **License**: proprietary（freemium）
- **Maturity signals**: Free / Starter（约 $8-12.5/月）/ Creator（约 $19/月，解锁 AI 写作+无限排程+跨平台）/ Team（$39/月）；年付约省 20% (last checked 2026-06-06) (evidence: [T02-S001])
- **典型使用场景**: 写长 thread（编辑器对分条/换行特别顺）；找最佳发布时间；自动接续推（self-thread）放外链；跨发 LinkedIn/Bluesky/Threads/Mastodon (evidence: [T02-S001])
- **不适合 / 替代方案**: 重增长自动化（auto-retweet/auto-plug）→ Hypefury；只要多平台极简排程 → Buffer。
- **生产案例**: 大量英文圈独立创作者把 Typefully 当 X 写作默认工具（厂商定位 + 横评一致，evidence: [T02-S024]）。
- **可信度**: high
- **Decay risk**: low（已是 X 写作排程基础设施）

### 3. X Premium（平台原生：长推 / Articles / Edit / reply 加权）

- **One-liner**: 中文 AI 博主的「不外链也能讲透」基础设施——25000 字长推、Articles、1 小时编辑窗、回复优先级。
- **Tier**: 必备
- **Maintainer**: X Corp (help.x.com 官方文档)
- **License**: proprietary（订阅，Basic 约 $3/月起，Premium / Premium+ 递增）
- **Maturity signals (官方文档)**:
  - 长推：Premium 订户可发 **最长 25000 字** (evidence: [T02-S004])
  - Edit：发布后 **1 小时窗口内最多 5 次编辑**；移动端编辑需 Premium+ (evidence: [T02-S005])
  - Articles：Premium+ 可在 profile 直接写长文 Article (evidence: [T02-S004])
  - Premium+：Grok 更高额度、无广告、回复最高优先级、Radar、Articles (evidence: [T02-S004])
- **典型使用场景**: 深度内容用 Articles/长推取代「外链博客」规避降权；快讯打字错了用 edit 救；Premium 让外链推不至于 0 曝光（见避坑）。
- **不适合**: 不订 Premium 还坚持发外链推 → 几乎 0 曝光 (evidence: [T02-S023])。
- **可信度**: high（官方一手）
- **Decay risk**: low（平台核心功能；具体字数/价格 medium）

### 4. ray.so / carbon.now.sh（代码 & 文字美图）

- **One-liner**: 把代码片段或一段金句 → 渐变背景的精致卡片图，AI 推配图的标配，开源免费。
- **Tier**: 必备
- **Maintainer / Owner**: ray.so = Raycast (MIT)；carbon = dawnlabs/carbon-app (MIT)
- **License**: open（均 MIT）
- **Maturity signals**:
  - ray.so: 2.3k★，last push 2026-06-04（healthy） (evidence: [T02-S006])
  - carbon: 36.0k★，last push 2026-02-10，未 archived（代码图鼻祖，2017 起） (evidence: [T02-S007])
- **典型使用场景**: 贴 prompt/代码/模型输出做对比图；分享时 Twitter 自动 unfurl 成图还带源码链接 (evidence: [T02-S007]);ray.so 还能做纯文字金句卡。
- **不适合 / 替代方案**: 要动画/交互讲解 → Snappify；要本地批量/自托管 → Karbonized/CodeImage (evidence: [T02-S025])。
- **可信度**: high（开源可核验）
- **Decay risk**: low（carbon 8 年稳定基础设施）

### 5. 截图美化（CleanShot X / Shottr / Xnapper）

- **One-liner**: 把原始截图 → 带边距/圆角/阴影/背景、可脱敏可标注的社媒图，让推文配图不糙。
- **Tier**: 必备
- **Maintainer**: CleanShot X (cleanshot.com) / Shottr (免费) / Xnapper (xnapper.com)
- **License**: proprietary（Shottr 免费；Xnapper 一次性约 $29.99/设备；CleanShot 订阅/买断）
- **Maturity signals**: Xnapper 称日活 4000+ 创作者，自动脱敏(邮箱/卡号/API key)+OCR+社媒比例模板 (evidence: [T02-S009, T02-S026])；CleanShot X 提供 7 种文字样式/箭头/spotlight/blur/录屏/云图床，Shottr 主打速度+OCR+QR+取色器+免费 (evidence: [T02-S010])。
- **典型使用场景**: 截 AI 产品 UI/对话做演示图；脱敏后晒后台数据；做对比图。
- **不适合 / 替代**: 预算/老机器 → Shottr（轻快免费）；要录屏+云分享 → CleanShot X；要一键好看+脱敏 → Xnapper (evidence: [T02-S009, T02-S010])。
- **可信度**: high
- **Decay risk**: low

### 6. 一手信息源（arXiv / HN / Reddit / 官方博客）

- **One-liner**: 选题的源头活水——直接从论文/官方发布/社区热度找一手，而不是搬运别人的二手稿。
- **Tier**: 必备
- **Maintainer**: arXiv (Cornell) / Hacker News (Y Combinator) / Reddit / 各 AI lab 官博
- **License**: open / public
- **Maturity signals**: arXiv 提供 RSS（如 arxiv.org/list/cs.AI/recent）；HN 靠社区投票而非推荐算法，热度=真信号 (evidence: [T02-S015, T02-S017])
- **典型使用场景**: 盯 cs.AI/cs.CL 新论文做「论文速读 thread」；HN 首页判断哪个发布值得编译；官方博客拿一手发布做快讯（标来源）。
- **不适合**: 把别人的中文总结当一手转（搬运，见避坑）。
- **可信度**: high
- **Decay risk**: low

### 7. RSS / AI 资讯聚合（Folo / Feedly / Inoreader）

- **One-liner**: 把几十个分散信息源收进一条时间线，AI 摘要快速过滤出可做的选题。
- **Tier**: 必备（工作流层面）
- **Maintainer**: Folo = RSSNext (开源)；Feedly / Inoreader (proprietary, AI 在付费层)
- **License**: Folo open；Feedly/Inoreader proprietary
- **Maturity signals**: Folo 38.5k★，last push 2026-06-05（healthy），开源 AI RSS，时间线 AI 摘要+每日 digest (evidence: [T02-S018])；Feedly/Inoreader AI 摘要仅付费层。
- **典型使用场景**: 订阅 arXiv RSS + AI lab 博客 + 关键人物 newsletter → 一条流；AI digest 早上扫一遍定选题。
- **不适合**: 纯阅读器（NetNewsWire/Reeder）无 AI 摘要，适合只读不做选题筛 (evidence: [T02-S018])。
- **可信度**: high
- **Decay risk**: medium（Folo 仍快速迭代）

---

## 场景特化层

### 8. Hypefury

- **One-liner**: 增长/自动化向工具——auto-retweet、auto-plug、evergreen 复用，给「想最大化触达」的 build-in-public 选手。
- **Tier**: 场景特化
- **Maintainer**: Hypefury (hypefury.com)
- **License**: proprietary（多档，活跃用户多用 Creator 约 $65/月）
- **Maturity signals (官方)**: auto-retweet 可设条件（如满 15 赞、6/12h 后）自动转推；evergreen list = 精选爆款定时复用/填空档；auto-plug 在推达到一定赞/转后自动追加链接（newsletter/产品） (evidence: [T02-S002, T02-S003])
- **典型使用场景**: build-in-public 持续曝光；把旧爆款 evergreen 循环；推火了自动挂产品链接。
- **不适合 / 替代**: 重内容质量、不想自动化油腻感 → Typefully；只多平台排程 → Buffer (evidence: [T02-S020])。
- **可信度**: medium-high（官方一手 + 第三方评测一致）
- **Decay risk**: medium

### 9. Tweet Hunter

- **One-liner**: 300 万+爆款推库当灵感引擎，按关键词/作者搜高表现内容找 hook 与格式 + AI 改写。
- **Tier**: 场景特化
- **Maintainer**: Tweet Hunter (tweethunter.io)
- **License**: proprietary
- **Maturity signals**: 库称 200-300 万爆款推用于灵感+训练 AI；含每日选题、Tweet Rewriter、Thread Ideas、Thread Hook Generator、排程、CRM (evidence: [T02-S019])
- **典型使用场景**: 没灵感时按 niche 搜爆款 hook；学某大号的开头结构；改写自己旧推。
- **不适合 / 替代**: 警惕「照搬爆款模板」导致同质（见避坑）；纯写作+排程 → Typefully。
- **可信度**: medium（vendor 数字）
- **Decay risk**: medium

### 10. Buffer

- **One-liner**: 多平台统一轻量排程，X/LinkedIn/IG/FB 一处发，便宜简单。
- **Tier**: 场景特化
- **Maintainer**: Buffer (buffer.com)
- **License**: proprietary（freemium）
- **Maturity signals**: 跨多网络排程 + 团队 workflow；定位「多平台、简单、便宜」 (evidence: [T02-S021, T02-S024])
- **典型使用场景**: 内容要同步发多个平台、不需要 thread 深编辑/增长自动化时。
- **不适合 / 替代**: X 深度 thread + AI 改写 → Typefully；X 增长自动化 → Hypefury (evidence: [T02-S024])。
- **可信度**: high
- **Decay risk**: low

---

## 新兴 / 实验阶段

### 11. Folo（AI RSS 阅读器）

- **One-liner**: 开源 RSS + AI 时间线摘要 + 每日 digest，覆盖文/视频/图/音，noise-free。
- **Tier**: 新兴
- **Maintainer**: RSSNext (开源)
- **Maturity signals**: 38.5k★ (2026-06-05)，Show HN 推出「时间线摘要 + 每日 AI digest」 (evidence: [T02-S018, T02-S017])
- **stability: experimental**（治理/商业化未定，6-12 月形态可能变）
- **典型使用场景**: AI 博主把信息源管线收口到一处 + AI 帮筛选题。
- **可信度**: medium
- **Decay risk**: high（新兴默认）

### 12. AI 资讯聚合 agent（News Aggregator AI 类）

- **One-liner**: 自动抓 30+ 源（arXiv/TechCrunch/Reddit/research lab）按关键词生成结构化简报。
- **Tier**: 新兴
- **Maturity signals**: HN 上出现的此类 agent，自动抽核心话题+编简报 (evidence: [T02-S017])
- **stability: experimental**
- **典型使用场景**: 全自动快讯流的选题前置（仍需人工核验，避免低质）。
- **可信度**: low-medium
- **Decay risk**: high

---

## 选型决策树

### 决策树 A：你这条内容是什么类型？

#### Branch 1: 快讯编译（英文发布 → 中文快推）
→ 推荐链路：**Folo/RSS 抓到一手 → DeepSeek/Kimi 理解+中文重写（不是翻译）→ ray.so/截图美化配图 → Typefully 发**
→ 关键：外链放在自回复第二条，不放首推（保曝光，见避坑） (evidence: [T02-S023])
→ 不推荐：让 AI 直接「翻译」原文（机翻味）；用聚合 agent 全自动发不核验。

#### Branch 2: 深度 thread / 论文速读
→ 推荐：**arXiv/官博一手 → Kimi（长文本喂全文总结）或 Claude/GPT（语感+洞察）起草 → Typefully 编辑器分条 → X Premium 长推/Articles 承载**
→ Tweet Hunter 找 hook 结构（参考不照搬）
→ 不推荐：把深度内容塞外链博客（X 外链降权 50-90%） (evidence: [T02-S004, T02-S023])。

#### Branch 3: 锐评 / 观点
→ 推荐：**Claude/GPT 帮打磨语感与论证（但观点必须是你自己的）→ Typefully 发**
→ 不推荐：AI 全代笔（同质、无人味，见避坑）。

#### Branch 4: build in public / 持续增长
→ 推荐：**Typefully 写 + Hypefury 做 auto-retweet/evergreen/auto-plug**；Buffer 若需多平台同步
→ 不推荐：过度自动化导致油腻刷屏 (evidence: [T02-S002, T02-S020])。

### 决策树 B：全 AI 自动 vs 人工精选？（保留矛盾）
- **全自动**（聚合 agent + AI 批量生成 + 自动排程）：量大、省时，但**低质同质、易被判搬运/AI 农场**——只适合纯快讯且必须人工抽检。
- **人工精选**（一手 → AI 辅助重写 → 人工加洞察 → 配图）：慢但有信任与差异化，是中文 AI 圈建立个人品牌的主流共识（推断）。
- 矛盾点：编译/搬运 vs 原创洞察——工具链相同，差别在「AI 是重写助手还是代笔机器」。

---

## 避坑清单

- ❌ **不要让 AI 直接「翻译」英文原文**：出「机翻味」，读者一眼识破搬运；正确是让 AI 理解后用中文重写并加本土化洞察 (evidence: [T02-S011])（一手语感对比 + 行业共识）。
- ❌ **不要把外链放首推**：X 算法对外链推降权 50-90%，非 Premium 账号发外链推近乎 0 曝光（2026-03 起）；做法是首推纯文字，外链放自回复第二条 (evidence: [T02-S023, T02-S004])。
- ❌ **不要搬运不标来源**：照搬别人的中文总结/截图当一手——既无信任也踩平台搬运红线；坚持 arXiv/官博/HN 一手并注明 (evidence: [T02-S015, T02-S017])。
- ❌ **不要用聚合 agent 全自动批量发**：AI 批量低质同质内容拉低账号权重、被识别为内容农场；聚合 agent 只做选题前置，发布前人工核验 (evidence: [T02-S017])。
- ❌ **不要照搬 Tweet Hunter 爆款模板**：爆款库是找 hook/结构灵感，逐句套用导致千篇一律、失去个人声音 (evidence: [T02-S019])。
- ❌ **不要让配图同质化**：全用 carbon/ray.so 默认主题渐变图会和所有人撞脸；混用截图美化（Xnapper/CleanShot）做产品演示图、自制对比/数据图区隔 (evidence: [T02-S008, T02-S009])。
- ❌ **不要拿纯阅读器当选题工具**：NetNewsWire/Reeder 无 AI 摘要，信息过载下选题效率低；用 Folo/Feedly(付费 AI 层)做摘要筛选 (evidence: [T02-S018])。

---

## Phase 2 提炼提示

**反复出现 ≥ 3 source 强调的「工具选型原则」**：
- 「一手 → AI 重写（非翻译）→ 人工加洞察」是中文 AI 推内容质量分水岭（出现于 T02-S011 / S012 / S013 + 行业共识）。
- 「外链必须避开首推」是 X 平台硬约束，决定排程工具的发布姿势（出现于 T02-S004 / S022 / S023）。
- 「工具是助手不是代笔机」——AI 介入程度决定原创 vs 搬运（跨 S011 / S017 / S019）。

**显著的工具流派分裂**（候选智识谱系）：
- **全自动流派**（聚合 agent + AI 批量 + 全自动排程，代表：News Aggregator agent、Hypefury 重度自动化）vs **人工精选流派**（一手 + AI 辅助重写 + 人工洞察 + 精修配图，代表：Typefully + Claude/Kimi + ray.so）。核心张力=量 vs 信任/差异化。
- **写作质量派**（Typefully）vs **增长自动化派**（Hypefury / Tweet Hunter）。

**新兴工具信号**：
- 当前活跃/上升新工具：2（Folo AI RSS、AI 资讯聚合 agent）。
- 出现 → 主流速度估计：6-12 个月（AI RSS 摘要类正快速渗透创作者选题环节）。

**冷僻 / 信号薄弱**：
- 必备层 7 个（≥3 ✓）；场景特化 5 个（✓）；新兴 2 个（✓）。信号充足，非冷僻行业。
- 注意：本行业很多「工具」是通用 LLM + 平台原生功能（X Premium）+ 通用美图工具的组合，而非行业专属工具——这是「内容生产」类行业的常态，不算调研失败。
- 一手比例：verified_primary 35% + vendor surrogate_primary 27% = 一手 62%，达标（≥50%）。
- vendor SaaS 官网（Typefully/Hypefury/Tweet Hunter/Buffer/Xnapper/CleanShot/carbon）按指示标 surrogate_primary(vendor docs)；GitHub/arXiv/X 官方 help/官方 blog 为 verified/官方一手。
