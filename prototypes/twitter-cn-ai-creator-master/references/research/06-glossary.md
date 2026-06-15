# Track 06 — Glossary + 流派分歧矩阵 — 推特(X) 中文圈 AI 自媒体博主（重点：文案 + 内容制作）

> Research date: 2026-06-06 · Locale: zh-CN（平台 X 全球，受众中文；术语含英文 X 写作正典 + 中文圈编译黑话）。
> 行业类型 = **创意/内容 + 平台机制依赖型**：黑话 + register + 平台机制术语占绝对大头；标准/认证 N/A；法规仅 AIGC 标识一类（且 X 国内不可直接访问，AIGC 监管对 X 中文博主弱约束，见诚实边界）。
> seed 复用：T04-canon 已给 27 核心概念（平台机制 + 写作 playbook），本 track 直接吸收作 tier-1 seed；T02-tools 给工具语境；T01-figures 给流派代表人。再用 web 补 2026 算法新机制（bookmark 跃升为最高信号 / Phoenix Transformer）+ Premium 三档新结构 + 流派分歧矩阵。
> **诚实前置**：(1) X 平台机制是最硬一手（开源算法 + 官方 help），但**互动权重数值跨年份漂移大**——2023 开源快照（reply=27/作者回复=75/fav=0.5）与 2026 重披露（bookmark≈10×like、retweet≈20×like、reply≈13.5×like、quote≈10-15×、Phoenix Transformer）**口径不同**，二者**都保留**并标矛盾，不强行统一。(2) 中文圈「编译/信息差」黑话的完整一手复盘 ~85% 在黑名单平台（知乎/公众号/CSDN）——本 track 用头部博主个人站 + GitHub + 英文 X 写作 canon 三角印证，单源不立。

## Source Manifest

| source_id | url | bucket | last_checked | author/host | one-line note |
|-----------|-----|--------|--------------|-------------|---------------|
| T06-S001 | https://sproutsocial.com/insights/twitter-algorithm/ | secondary | 2026-06-06 | Sprout Social | 2026 算法横评：retweet≈20×like / reply≈13.5× / bookmark≈10× / Premium 2-4× / 外链罚 50-90% / 6h 半衰 |
| T06-S002 | https://socialbee.com/blog/twitter-algorithm/ | secondary | 2026-06-06 | SocialBee | 2026 quote/bookmark/dwell 信号二手综述 |
| T06-S003 | https://tweethunter.io/blog/twitter-blue-vs-x-premium | secondary | 2026-06-06 | Tweet Hunter | Premium 三档(Basic/Premium/Premium+) 定价 + reply 优先级阶梯 |
| T06-S004 | https://hypefury.com/twitter/x-account-types-and-prices/ | surrogate_primary | 2026-06-06 | Hypefury | X 账号类型/价格清单(vendor docs) |
| T06-S005 | https://en.wikipedia.org/wiki/Timeline_of_X_(social_network) | secondary | 2026-06-06 | Wikipedia | X 功能/政策时间线(长推/编辑/算法开源节点) |
| T06-S006 | https://www.tweetarchivist.com/how-to-quote-tweet-guide | secondary | 2026-06-06 | Tweet Archivist | quote tweet 2026 机制：被算法当原创内容、可独立涨粉 |
| T06-S007 | https://nealschaffer.com/twitter-blue/ | secondary | 2026-06-06 | Neal Schaffer | X Premium 2026 是否值：创作者视角 ROI |

> **复用前轨 source（不重复跑 verifier，直接引）**：
> T04-S001(the-algorithm 开源主仓) · T04-S002(Heavy Ranker) · T04-S003(awesome-twitter-algo 权重注解) · T04-S004(X help Premium 长推/Articles) · T04-S005/S006(创作者变现条款) · T04-S007(swyx Learn in Public) · T04-S008(Perell Write of Passage) · T04-S009(Levels MAKE/build in public) · T04-S010/S011(Atomic Essay/hook) · T04-S012/S013(宝玉 baoyu.io + skills) · T04-S015(外链降权报道) · T04-S017(X 官方披露排序信号) · T04-S019(quote/dwell/bookmark 二手)。
> T02-S004/S005(X Premium help 长推/edit) · T02-S023(外链降权数据)。
> T01-S001(宝玉) · T01-S005/S008(歸藏 + 算法 thread) · T01-S010(向阳乔木) · T01-S014(小互) · T01-S015(Orange AI) · T01-S018(李继刚) · T01-S021(justlovemaki 全自动对照)。
> **黑名单命中即丢未入表**：检索过程中出现 zhihu.com / zhuanlan.zhihu.com / cloud.tencent.com(developer 社区/SEO 农场性质) / mp.weixin / 百度 / CSDN / 简书 / 掘金 / sspai(少数派为优质但本批仅作发现，不入 evidence) — 均**未作 evidence**。
> bucket 说明：X 官方 help / 开源 repo / 官方变现条款 = verified_primary（在 T04/T02 已收）；社媒营销长稿(Sprout/SocialBee/Tweet Hunter/Neal Schaffer/Tweet Archivist) = secondary；Hypefury 账号类型清单 = surrogate_primary(vendor docs)；Wikipedia timeline = secondary。本 track 新增 7 源（secondary 5 + surrogate_primary 1 + Wikipedia 1），一手厚度主要靠复用 T04 的 verified_primary（X 开源算法 + 官方 help + 作者个人站）。

---

## 总览（按 type 分组）

行业 type 分布：**Term/平台机制黑话占绝对大头（写作技法 + 算法机制 + 编译打法）；Acronym 少量（CTA/CTR）；Regulation 仅 AIGC 标识一类且对 X 中文博主弱约束；Standard / Certification = N/A**（创意内容 + 海外平台特征）。

### Tier 1 — 核心必懂（18，所有 X 中文 AI 博主必懂）

| 术语 | Type | Insider def（内行实义） | Outsider tell（外行破绽） | Last_updated |
|------|------|------------------------|--------------------------|-------------|
| 推文 (Tweet/Post) | term | X 最小内容单元，标准 280 字，Premium 至 25k | 外行叫「微博/动态」，不知 280 字硬限制 + 前 280 字必须自足做 hook | 2026-06 |
| Thread（推文串/长推） | term | 编号串联多推：首条 hook + 逻辑链 + 末条 CTA | 外行写一长段塞一条推，不懂分条节奏 + 每条要能独立成立 | 2026-06 |
| Hook（钩子） | term | 首条/首行抓注意力，回答「我为何不划走」（反直觉/具体数字/悬念缺口/点名受众） | 外行写「大家好今天分享」式平铺开头，无钩子=没人读 | 2026-06 |
| Quote Tweet（引用推/引用锐评） | term | 带评论转发，**2026 算法当原创内容给独立触达**，既给原推信号又生成可独立涨粉的新推 | 外行把 quote 当「转发(repost)」，不知带评论的引用是涨粉利器、纯转推几乎无权重 (evidence: [T06-S006, T06-S002]) | 2026-06 |
| 转评赞 (quote/reply/like) | term | 三种基础互动；**reply 权重远高于 like**（中文圈把「点赞/转发/评论」合称转评赞） | 外行盯点赞数，不懂 reply ≫ like、quote ≫ 纯转推 | 2026-06 |
| 互动权重 | term | Heavy Ranker 对各互动赋分；**reply > retweet > like，引发作者回复最值钱** | 外行只追赞；**忽略「作者回复」权重**(2023 开源=75，2026 仍是高信号)是命门 (evidence: [T04-S003, T06-S001]) | 2026-06 |
| 外链降权 (link deboost) | term | 含出站链接的推被减触达；对策=链接放首条**自回复**而非正文 | 外行外链直发正文，非 Premium 账号近乎 0 曝光 (evidence: [T06-S001, T02-S023]) | 2026-06 |
| Dwell time（停留时长） | term | 停下读完=兴趣信号（即使无显式互动），长推/视频的核心权重；详情页 15s+、profile 20s+ 是阈值 | 外行只看「点赞/转发数」，不知「读完不互动」也被算法看见 (evidence: [T06-S002]) | 2026-06 |
| Impressions（曝光/展示） | term | 推被看到次数；变现门槛按 organic impressions 算（近 3 月 ≥500 万） | 外行把 impressions 当「阅读量」或与「互动」混；不知曝光≠有人真读 (evidence: [T04-S006]) | 2026-06 |
| Premium / 蓝V / Premium+ | term | 订阅三档(Basic\$3 / Premium\$8 / Premium+\$40)：解锁长推/Articles/编辑 + **reply 优先级阶梯 + 2-4× 触达乘数** | 外行以为蓝V只是「认证打钩」，不知它是结构性流量乘数 + 变现入场券 (evidence: [T06-S003, T06-S001]) | 2026-06 |
| Long-form 长推 / Articles | term | Premium 站内长文/长推(至 25000 字)，绕开外链降权把内容留站内；**前 ~280 字仍折叠前自足** | 外行把深度内容塞外链博客→被降权；或写长推不管前 280 字 hook (evidence: [T04-S004, T02-S004]) | 2026-06 |
| CTA（行动召唤） | term+acronym | 末条/末行引导关注/转发/收藏/点链，需是价值的自然延伸 | 外行硬塞「求关注求转发」无价值铺垫；或全程无 CTA 浪费流量 (evidence: [T04-S011]) | 2026-06 |
| build in public（公开构建） | term | 边做产品/项目边公开晒进度/数据/挣扎，透明度即信任护城河 | 外行只发成品广告，不懂「晒过程」本身是涨粉/信任引擎；或晒到油腻刷屏 (evidence: [T04-S009, T01-S015]) | 2026-06 |
| 信息差 | term | 英文一手与中文受众间的认知时间差，中文 AI 博主的核心红利来源 | 外行不知道红利来自「跨语言时效套利」，以为靠原创天赋；信息差正被全自动日报压缩 (evidence: [T04-S012, T01-S021]) | 2026-06 |
| 编译（非翻译/重写） | term | 理解英文一手后用中文**重写并加本土化洞察**，不是逐句直译 | 外行机翻直发当编译，「机翻味」一眼被识破搬运；以为编译=翻译 (evidence: [T04-S012, T01-S001]) | 2026-06 |
| 涨粉飞轮 (audience-first) | term | thread→newsletter/社群→产品/课的内容→受众→变现循环；先有受众再有产品 | 外行先做产品再找人，或只发不沉淀；不懂内容是漏斗顶端 (evidence: [T04-S008]) | 2026-06 |
| 蹭热点 | term | 围绕当下热门发布/争议快速产出蹭算法流量（中文圈快讯派核心动作） | 外行慢半拍蹭过气热点；或无差异化纯跟风=同质淹没 (evidence: [T01-S014]) | 2026-06 |
| AI 味 | term | AI 直出文案的同质化/书面腔/空话特征（反「人味/活人感」） | 外行把 AI 初稿直接发，AI 味重→撞稿、无个人 voice (evidence: [T01-S001]) | 2026-06 |

### Tier 2 — 周边熟知（11，资深者熟知）

| 术语 | Type | Insider def | Outsider tell | Last_updated |
|------|------|-------------|---------------|-------------|
| For You 时间线 | term | 算法推荐流，~50% in-network + out-of-network 召回 | 外行以为只有关注的人能看到自己的推 (evidence: [T04-S001]) | 2026-06 |
| Heavy Ranker（终排） | term | 输出各类互动概率的神经网络做终排；2026 称 Phoenix Transformer 多任务预测 15+ 行为 | 外行把 X 排序当「时间倒序」或玄学，不知有 ML 模型打分 (evidence: [T04-S002, T06-S002]) | 2026-06 |
| in-network vs out-of-network | term | 关注流 vs 算法发现流；蓝V对 out-network 有触达乘数 | 外行不分两类流量，不知爆款主要靠 out-network 破圈 (evidence: [T04-S001, T04-S003]) | 2026-06 |
| 蓝V乘数 / Premium boost | term | Premium 账号触达约 **2-4×** 非 Premium + reply 顶置 | 外行以为认证只是虚荣标识，低估其流量杠杆 (evidence: [T06-S001, T04-S003]) | 2026-06 |
| 作者回复权重 | term | 「回复且被作者再回复」是最高正向信号（2023 开源=75）；对话>广播 | 外行发完不回评论，浪费最值钱的互动信号 (evidence: [T04-S003]) | 2026-06 |
| Bookmark（收藏/书签） | term | **2026 跃升为最高价值信号之一(≈10×like)**，代表「值得存下回看」的实用价值 | 外行只看赞，不知 2026 收藏权重超点赞、是长青内容指标 (evidence: [T06-S001, T06-S002]) | 2026-06 |
| Curiosity Gap（好奇缺口） | term | hook 技法：留知识空白逼读者继续读 | 外行把全部信息塞进首句，无悬念=无继续读动力 (evidence: [T04-S011]) | 2026-06 |
| Atomic Essay（原子小作文） | term | 250 字「截图式短文」，thread 与博客之间的甜点位，练 hook+结构 | 外行不知有这种中间形态，要么一句话要么长博客 (evidence: [T04-S010]) | 2026-06 |
| Learn in Public（公开学习） | term | 把学习过程开源成内容，副产品是受众与机会 | 外行「攒够再发」完美主义，错过复利 (evidence: [T04-S007]) | 2026-06 |
| 负向信号（举报/拉黑/静音） | term | 隐藏/拉黑/静音(2023≈−74)、举报(≈−369)是核弹级降权 | 外行为流量发争议内容招举报，一次举报抵消大量正向 (evidence: [T04-S003]) | 2026-06 |
| 全自动发 vs 人工精选 | term | 全 AI 抓取+摘要+自动发(机器流水线) vs 一手→AI 重写→人工加洞察 | 外行用聚合 agent 全自动批量发，被判内容农场降权 (evidence: [T01-S021]) | 2026-06 |

### Standards / Regulations / Certifications 时间轴（仅近 5 年有显著变化的进表）

| 名称 | Type | Issued | Last revised | Decay | 备注 |
|------|------|--------|--------------|-------|------|
| X 互动权重开源快照 | （非法规，平台机制基线） | 2023-03 开源 | 2023（未持续更新） | high | reply=27/作者回复=75/fav=0.5/举报=−369；2024+ 改制后实际权重未公开 (evidence: [T04-S003]) |
| X 互动权重 2026 重披露 | （平台机制更新） | 2026-01 算法再开源 | 2026 | high | retweet≈20×like / reply≈13.5× / bookmark≈10× / quote≈10-15×；Phoenix Transformer；与 2023 口径不同**矛盾保留** (evidence: [T06-S001, T06-S002]) |
| X 创作者变现改制 | （平台政策） | 2024-10 | 2024-10 | medium | 分成基于 Premium 用户互动而非广告，回复多赚最多；门槛 ≥500 万 imp + ≥2000 verified followers (evidence: [T04-S006]) |
| X Premium 三档结构 | （平台政策/定价） | 2024 改名 X | 2026 | medium | Basic\$3 / Premium\$8 / Premium+\$40；Articles 仅 Premium+ (evidence: [T06-S003, T06-S004]) |
| 外链降权政策（反复横跳） | （平台机制） | 2023 罚 50-90% | 2025 宣称取消→2026 二手仍报 50-90% | high | **disputed**：政策反复，写作时仍按「链接放评论」更稳 (evidence: [T06-S001, T02-S023, T04-S015]) |
| 《AI 生成合成内容标识办法》(中国国标) | regulation | 2025-09-01 执行 | 2025 | high | 对 X(海外平台,国内不可直接访问)**弱约束**；中文 AI 博主若同步国内平台才硬触发 (evidence: [T04-S006]) |
| **Standard / Certification** | — | — | — | **N/A** | 内容创作行业无产品/执业认证；X 无官方「博主资质」，唯一「资质」是蓝V订阅(付费非资格审核) |

> **disputed 标注**：
> - **互动权重数值**：`disputed` — 2023 开源(reply=27/作者回复=75/like=0.5，绝对分值) vs 2026 重披露(以 like 为 1 的相对倍数：retweet≈20×/reply≈13.5×/bookmark≈10×/quote≈10-15×)。两套口径不同(绝对 vs 相对)且年份不同，**方向一致**(对话/收藏/转推 ≫ 点赞)但**精确值都不该当 ground truth** (evidence: [T04-S003, T06-S001])。
> - **外链是否降权**：`disputed` — 2023 罚 vs 2025 X 宣称取消 vs 2026 二手仍报 50-90%。保守策略：链接放自回复 (evidence: [T04-S015, T06-S001])。
> - **bookmark 权重**：2026 二手广传「bookmark 跃升最高信号(≈10×like)」，但 2023 开源中 bookmark 权重不显著——属**新增信号**，标推断/二手 (evidence: [T06-S001, T06-S002])。

### 行业「外行破绽」高亮（top 10 insider-only tells）

| 误用 | 内行实际意思 | 频率 |
|------|-------------|------|
| 把「机翻直发」当编译 | 编译=理解后中文**重写+本土化洞察**，机翻味=搬运露馅 | 高 |
| 外链直接发正文 | 外链放**首条自回复**，正文留 hook（否则降权/0 曝光） | 高 |
| 把粉丝数当影响力 | 影响力看 impressions/互动质量/作者回复，僵粉无意义 | 高 |
| 忽略「作者回复」权重 | 发完去回评论引发二次对话=最值钱信号 | 高 |
| 把 quote tweet 当「纯转发」 | 带评论引用=算法当原创给独立触达，纯 repost 几无权重 | 高 |
| 只追点赞数 | 2026 bookmark/quote/reply 权重 ≫ like | 高 |
| 把 thread 写成一长段 | thread 要分条+每条独立成立+末条 CTA | 中 |
| 蓝V当「虚荣打钩」 | Premium 是 2-4× 触达乘数 + 变现入场券 | 中 |
| 用聚合 agent 全自动批量发 | 被判内容农场降权；agent 只做选题前置，发布前人工核验 | 中 |
| 把深度内容塞外链博客 | 用 long-form/Articles 留站内，绕开外链降权 | 中 |

---

## 流派分歧矩阵（framework 甜区 — 本 track 最高价值产出，保留分歧不软化）

> 引 T01 figures 提炼的 5 轴立场光谱（不软化、保留矛盾）。每轴：主张 / 代表 / 适用 / 核心分歧。

### 轴 1：编译搬运（英文一手翻译）vs 原创洞察

- **A 派（编译搬运）主张**：信息差是中文圈最大红利——英文一手→中文快/深，高信噪比建账号，「编译即重写」可带个人 voice。
- **B 派（原创洞察）主张**：信息差会被全自动日报和翻译工具碾平，护城河只能是原创认知；搬运无论多精致仍是寄生英文圈。
- **代表**：编译派=宝玉 @dotey（天花板，「翻译即重写+voice 注入」横跨两端）/ 小互 @imxiaohu / Gorden Sun / 向阳乔木；原创派=李继刚 @lijigang_com（prompt 艺术/语义压缩）/ 王川 @Svwang1（认知长推）/ Orange AI @oran_ge（行业锐评）。
- **适用**：编译适合冷启动/快建信噪比/无英文产品经验者；原创适合有独特认知/想建长期个人品牌护城河者。
- **核心分歧**：**「AI 是重写助手还是代笔机器」+「信息差红利还能吃多久」**。宝玉用「多角色 prompt 直译→意译→融合 + 风格 skill」把编译做到原创边界，证明二者非二元对立 (evidence: [T01-S001, T01-S018, T01-S021])。

### 轴 2：快讯资讯 vs 深度长推

- **A 派（快讯/速度）主张**：第一时间速递=信息差最大化，功能清单体+模板化推文便于高频消费，速度即护城河。
- **B 派（深度/慢思考）主张**：快讯被全自动吞噬，留下的价值是「读透+判断」；深度长推/论文速读建专业权威。
- **代表**：快讯派=小互 @imxiaohu（产品速递功能清单体）/ Gorden Sun（Notion 日报）；深度派=王川 @Svwang1（认知长 thread）/ 宝玉（高管访谈/论文深译）/ 李继刚（prompt 长文）。歸藏 @op7418 用「周刊四板块」横跨（新闻+评测+学术）。
- **适用**：快讯适合高频起号/社群引流变现；深度适合低频高信任/课程/订阅变现。
- **核心分歧**：**「速度 vs 信任」+「快讯层是否已被自动化吃掉」**。justlovemaki 全自动 Gemini 日报证明纯快讯/聚合正被机器流水线吞噬，人工护城河被迫上移到观点/实测 (evidence: [T01-S014, T01-S020, T01-S021])。

### 轴 3：锐评玩梗/争议营销 vs 严肃干货

- **A 派（锐评/争议）主张**：争议即流量，对立话术制造讨论=引发 reply(算法最爱)，鲜明立场建人设记忆点。
- **B 派（严肃干货）主张**：争议透支信任、招举报(核弹级负信号)；真诚测评/扎实干货才是长期复利。
- **代表**：锐评/争议派=花生/花叔 @AlchainHust（「我不会编程只会 AI 编程」主动蹭争议）/ Orange AI（行业锐评，但绑真实痛点）；严肃干货派=歸藏（「Sora 不值 200 刀」真诚测评者人设）/ 宝玉（工程务实）/ 向阳乔木（资源整理）。
- **适用**：争议适合冷启动快速起量/卖课导向；严肃适合 B 端/专业受众/长期品牌。
- **核心分歧**：**「争议起量 vs 信任复利」+「reply 是真讨论还是骂战」**。争议引发的 reply 算法加权，但举报(−369)和拉黑(−74)是核弹级反噬——争议是双刃 (evidence: [T01-S017, T01-S009, T04-S003])。

### 轴 4：build in public vs 纯内容

- **A 派（build in public）主张**：边做产品边公开晒进度/数据/挣扎，透明度=竞品无法复制的护城河，内容与产品互相导流。
- **B 派（纯内容）主张**：内容创作者专注内容质量本身，不绑产品避免「内容服务于带货」的信任损耗。
- **代表**：build in public 派=Orange AI @oran_ge（172万曝光→309订阅公开转化漏斗）/ 花生（app 上榜结果背书）；奠基=Pieter Levels(MAKE) / swyx(Learn in Public)；纯内容派=宝玉（自陈翻译是爱好非生意）/ 歸藏周刊 / 向阳乔木整理。
- **适用**：build in public 适合独立开发者/创业者「做+营销」一体；纯内容适合译者/策展人/无产品者。
- **核心分歧**：**「内容是否该绑产品」+「晒数据是真诚还是表演」**。build in public 易滑向「内容为带货服务」的信任质疑，纯内容则放弃了产品反哺的飞轮 (evidence: [T01-S015, T01-S017, T04-S009, T04-S007])。

### 轴 5：全 AI 自动发 vs 人工精选

- **A 派（全自动）主张**：量大省时，聚合 agent + AI 批量生成 + 自动排程可规模化覆盖快讯层。
- **B 派（人工精选）主张**：全自动=低质同质，被判内容农场降权；一手→AI 重写→人工加洞察→精修配图才有信任与差异化。
- **代表**：全自动派=justlovemaki / CloudFlare-AI-Insight-Daily（Gemini 自动摘要→自动发布，对照组）；人工精选派=小互/Gorden Sun（人工日报）/ 宝玉/歸藏（人工加洞察）；半自动居中=向阳乔木 QMReader（AI 翻译+按风格改写+人工审）。
- **适用**：全自动适合纯快讯聚合/可接受低质换量；人工精选适合建个人品牌/差异化护城河。
- **核心分歧**：**「量 vs 信任/差异化」+「AI 介入到哪一步算搬运」**。这条轴决定护城河从「聚合速度」上移到「观点/实测/人设/voice」——快讯/聚合层正被自动化吞噬 (evidence: [T01-S021, T01-S013, T01-S010])。

> **矩阵交叉读法**：宝玉 = 编译×深度×纯内容×人工精选（编译派天花板，但靠 voice 注入逼近原创）；小互 = 编译×快讯×纯内容×人工(高频)；Orange AI = 原创×深度×build in public×人工；花生 = 原创×混合×build in public×争议×人工；justlovemaki = 编译×快讯×纯内容×全自动（人工派的反面坐标）。**五轴不正交**——多数博主在多轴上有组合立场，且护城河整体随自动化推进向「原创/深度/人设」一端漂移。

---

## 关键差异对照

### 对照 1：本 skill（X 中文 AI 博主）vs 姊妹 skill「小红书 AI 自媒体博主」

> 数据来源：本 track + `xiaohongshu-ai-creator-master/references/research/06-glossary.md`（同日蒸馏）。

| 维度 | X 中文 AI 博主 | 小红书 AI 博主 | 核心差异 |
|------|----------------|----------------|---------|
| **核心权重信号** | reply / 作者回复 / quote / bookmark（**对话 > 一切**）；2026 bookmark 跃升 | 收藏率 / 完读率 / 完播率（**利他·存下回看 > 一切**） | X 看「能否引发对话」；小红书看「是否值得收藏用」——reply vs 收藏是两个平台的命门 |
| **流量来源** | For You 推荐流(~50% in-network + out-network 破圈) + 关注流 | 搜推互通，**约 60-70% 来自搜索**(SEO/蓝海词) | X 是「广场推荐」，小红书是「搜索社区」——X 几乎不做 SEO，小红书布词是命脉 |
| **外链/链接** | **外链降权**(放自回复)；用 long-form/Articles 留站内 | 笔记内**不可挂外链**，导流靠主页/私信/评论暗号 | X 有外链但被罚；小红书直接禁外链，导流姿势完全不同 |
| **作者互动** | **回复且被作者再回复=最高信号(75/2023)**，主动回评涨权重 | 评论权重高(CES 评×4)，但无「作者回复」专项加权机制 | X 把「作者参与对话」单独重赏，小红书重「评论数」本身 |
| **voice/语气** | 锐评 / 信息差 / 工程务实 / 争议(可玩梗) | 种草 / 利他 / 活人感 / 真诚分享（**禁叫卖**） | X 容忍甚至奖励锐评争议(引 reply)；小红书种草要「信任不叫卖」，争议易限流 |
| **选题来源** | **英文一手编译**(arXiv/官博/HN 信息差) | **本地化痛点**(中文用户场景/消费决策) | X 吃跨语言时效套利；小红书吃本地生活痛点共鸣 |
| **变现** | 创作者分成(按 Premium 互动) + newsletter/社群/课 | 蒲公英品牌合作(唯一合规) + 私域 + 带货 | X 靠平台分成+导流外部；小红书靠站内品牌合作平台 |
| **AIGC 标识约束** | **弱**(X 海外平台，国内国标不直接管) | **强**(2026-02 平台强制标识，未标限流+自动加标) | 小红书 AIGC 监管硬约束，X 中文博主几乎不受国内 AIGC 标识法直接管 |
| **配图/排版** | 代码美图(carbon/ray.so) + 截图美化 + 数据图 | 封面三秒/大字报(小眼睛点击率) + social-card | X 配图服务「证据/演示」；小红书封面是「点击率生死线」 |

**一句话**：X = 对话广场 + 外链受限 + 英文编译信息差 + 锐评容错；小红书 = 搜索社区 + 禁外链 + 本地痛点种草 + 利他高于一切。**同一批头部博主(歸藏/向阳乔木)做跨平台矩阵时，必须为两套机制改写而非搬运**(歸藏 social-card-skill 专做「小红书图文+公众号封面」即此佐证) (evidence: [T01-S007])。

### 对照 2：本 skill（X 中文 AI 博主）vs 英文 AI Twitter 圈

> 英文圈是中文圈**信息差红利的来源**——理解英文圈 = 理解上游。

| 维度 | 英文 AI Twitter 圈 | X 中文 AI 博主 | 关系 |
|------|--------------------|----------------|------|
| **角色定位** | 一手生产者(研究者/创始人/产品方第一手发布) | **下游编译者/二次传播**(把英文一手搬给中文受众) | 中文圈靠「英文圈发布→中文受众接收」的时间差套利 |
| **canon 归属** | swyx(Learn in Public) / Perell(Write of Passage) / Levels(MAKE) / Ship30(Atomic Essay) = **方法论原典** | 借用英文 canon 方法 + 叠加「编译/信息差」中文打法 | 中文圈的写作 playbook **直接继承英文圈**，无独立 canon |
| **信息差方向** | 无信息差(本就是源头) | **吃英文→中文的时效+语言差** | 红利本质=英文圈与中文受众间的认知延迟 |
| **风险** | 红利会随中文受众英文能力↑ + AI 翻译普及 + 全自动日报而**收窄** | 同上——信息差是**正在折旧的资产** | 中文圈护城河被迫从「翻译速度」上移到「洞察/voice/人设」 |

**一句话**：中文 X AI 博主 = 英文圈的**下游编译节点**，方法论师承英文 canon，红利源于跨语言信息差——而这层红利正被 AI 翻译 + 全自动聚合双向挤压，倒逼从「搬运」转向「原创/洞察」(对应流派轴 1 和轴 5 的漂移方向) (evidence: [T04-S007, T04-S008, T04-S012, T01-S021])。

---

## Phase 2 提炼提示

**「行业表达 DNA」直接素材**（喂给 Phase 2.5 expression-DNA 提炼）:
- **高频黑话 top 10**：hook / thread / quote tweet 引用锐评 / 转评赞 / 互动权重 / 作者回复 / 外链降权 / build in public / 信息差 / 编译(非翻译)。
- **行业拒绝的厂商/外行话术 top 5**：① 把「机翻」叫「翻译/编译」② 把「转发(repost)」与「引用(quote)」混用 ③ 把「粉丝数」当影响力(内行看 impressions/互动质量) ④ 把「认证打钩」当蓝V全部价值(忽视 2-4× 触达乘数) ⑤ 把「全自动 AI 日报」当内容创作(内行视为内容农场/文字泡沫)。
- **外行破绽 top 10 (insider-only spotting tells)**：见上「外行破绽高亮」表——机翻当编译 / 外链直发正文 / 粉丝数当影响力 / 忽略作者回复权重 / quote 当纯转发 / 只追点赞 / thread 写成一长段 / 蓝V当虚荣 / 全自动批量发 / 深度内容塞外链博客。

**「智识谱系」线索**（喂给 Phase 2.7 智识谱系）:
- **方法论师承单向**：中文圈写作 playbook 全盘继承英文 canon(swyx/Perell/Levels/Ship30)，无独立原典——智识谱系上中文圈是英文「写在网上(Write Online)+build in public」运动的下游分支。
- **5 轴流派分歧**(见矩阵)，最尖锐三条：① 编译 vs 原创(信息差还能吃多久) ② 全自动 vs 人工精选(AI 介入到哪步算搬运) ③ 锐评争议 vs 严肃干货(reply 红利 vs 举报反噬)。这三条共享一个底层张力：**自动化/AI 把「速度/搬运/量」打到地板，护城河被迫上移到「原创/洞察/人设/voice」**——流派坐标整体向「原创·深度·人设」一端漂移。

**「时效性」信号**（喂给 Phase 2.8 诚实边界）:
- **互动权重数值高度不稳**：2023 开源快照与 2026 重披露口径不同(绝对分值 vs 相对 like 倍数)，且 X 政策反复横跳(外链降权 罚→取消→仍报罚)——**任何精确数值都标方向性事实而非现值**，12 月内极可能再变。
- **bookmark 跃升、Phoenix Transformer** 是 2026 新信号，定义未稳定(二手为主)，high decay。
- **中文圈黑话一手 ~85% 在黑名单平台**：编译/起号/算法的完整复盘多在知乎/公众号，本 track 靠英文 canon + 头部博主个人站/GitHub 三角印证，**中文圈打法厚度低于英文写作 canon**。

**「工作流变化触发」种子**（喂给 wave 3 Track 03）:
- **2026-01 X 算法再开源 + Phoenix Transformer + bookmark 权重跃升** → 选题/写作要从「求赞」转向「求收藏/求对话」，影响 CTA 设计与内容「长青化」。
- **外链降权政策反复** → 排程工具的「链接放自回复」姿势是硬约束，但需随政策跟踪。
- **全自动聚合日报普及**(justlovemaki 类) → 快讯/聚合 workflow 被吞噬，人工 workflow 必须上移到洞察/实测/voice 注入环节。

**冷僻 / 信号薄弱**:
- 总术语数 = **29**(Tier 1=18 + Tier 2=11) ≥25 ✅；Tier 1=18 ≥15 ✅；有 outsider-tell 的术语：Tier 1 全部 18/18 ✅，Tier 2 全部 11/11 ✅，覆盖率 100% ≥50% ✅。
- **不触发冷僻协议**，但有两处弱信号需在 SKILL.md 诚实边界注明：① 互动权重数值矛盾(2023 vs 2026)且政策反复，精确值不可当 ground truth；② 中文圈黑话一手受黑名单限制，部分定义靠英文 canon + 个人站 surrogate 推断。
- 一手厚度：本 track 新增 7 源(secondary 5 + surrogate 1 + Wikipedia 1)偏二手，**但通过复用 T04 的 verified_primary(X 开源算法 + 官方 help + 作者个人站)补足一手底座**——平台机制术语有硬一手，写作/编译黑话有 canon + surrogate 三角，整体达标。
