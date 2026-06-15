# Track 02 — Tools / 内容生产工具栈 — 小红书 AI 自媒体博主

> Research date: 2026-06-06 · Locale: zh-CN · 聚焦「怎么写文案、怎么制作内容」的工具栈
> 核心轨。本文件输出三层结构（必备 / 场景特化 / 新兴）+ 选型决策树 + 避坑清单。

## Source Manifest

| source_id | url | bucket | last_checked | author/host | note |
|-----------|-----|--------|--------------|-------------|------|
| T02-S001 | https://creator.xiaohongshu.com/ | verified_primary | 2026-06-06 | 小红书官方 | 创作服务平台一站式后台 |
| T02-S002 | https://creator.xiaohongshu.com/publish/publish | verified_primary | 2026-06-06 | 小红书官方 | 图文/视频发布入口 |
| T02-S003 | https://pgy.xiaohongshu.com/help/home | verified_primary | 2026-06-06 | 小红书蒲公英 | 商单/合作平台帮助中心 |
| T02-S004 | https://github.com/Kwai-Kolors/Kolors | verified_primary | 2026-06-06 | 快手 Kolors | 中文文生图开源模型 4.6k★ |
| T02-S005 | https://jimeng.jianying.com/ | surrogate_primary | 2026-06-06 | 字节即梦AI | vendor docs 文生图/视频官网 |
| T02-S006 | https://www.gaoding.com/features-red-book-hot | surrogate_primary | 2026-06-06 | 稿定设计 | vendor docs 小红书封面模板库 |
| T02-S007 | https://www.gaoding.com/features-xiaohongshu-pictures | surrogate_primary | 2026-06-06 | 稿定设计 | vendor docs 3:4 配图生成器 |
| T02-S008 | https://www.canva.cn/rednote/ | surrogate_primary | 2026-06-06 | Canva可画 | vendor docs 小红书图文创作 |
| T02-S009 | https://www.canva.cn/learn/xiaohongshu-note-cover/ | surrogate_primary | 2026-06-06 | Canva可画 | vendor docs 封面设计套路 |
| T02-S010 | https://www.heygen.com/ | surrogate_primary | 2026-06-06 | HeyGen | vendor docs 数字人/多语言口播 |
| T02-S011 | https://xh.newrank.cn/ | surrogate_primary | 2026-06-06 | 新榜新红 | vendor docs 选题/热词/爆款笔记 |
| T02-S012 | https://www.qian-gua.com/ | surrogate_primary | 2026-06-06 | 千瓜数据 | vendor docs 历史数据/热搜词付费SaaS |
| T02-S013 | https://www.qian-gua.com/information/detail/807 | secondary | 2026-06-06 | 千瓜数据 | 热搜词底层逻辑(厂商长文) |
| T02-S014 | https://www.chanxiaohong.com/ | surrogate_primary | 2026-06-06 | 蝉妈妈蝉小红 | vendor docs 蓝海词/爆文榜 |
| T02-S015 | https://finance.eastmoney.com/a/202602123649416010.html | secondary | 2026-06-06 | 东方财富 | 小红书AI标识新规报道 |
| T02-S016 | https://m.ebrun.com/597045.html | secondary | 2026-06-06 | 亿邦动力 | AI标识不可删改隐匿+操作路径 |
| T02-S017 | https://finance.sina.com.cn/tech/discovery/2026-02-12/doc-inhmqmqc3769912.shtml | secondary | 2026-06-06 | 新浪科技 | 薯管家AI标识公告原报道 |
| T02-S018 | https://www.digitaling.com/articles/905106.html | secondary | 2026-06-06 | 数英网 | 小红书数据平台白嫖横评 |
| T02-S019 | https://www.niaogebiji.com/article-151233-1.html | secondary | 2026-06-06 | 鸟哥笔记 | 四大数据平台横向测评 |
| T02-S020 | https://www.niaogebiji.com/article-478679-1.html | secondary | 2026-06-06 | 鸟哥笔记 | 小红书必备网站/工具盘点 |
| T02-S021 | https://www.woshipm.com/operate/5498171.html | secondary | 2026-06-06 | 人人都是产品经理 | 100+热门标题→标题公式 |
| T02-S022 | https://www.yunyingpai.com/news/934715.html | secondary | 2026-06-06 | 运营派 | 爆文套路/结构公式 |
| T02-S023 | https://cn.technode.com/post/2024-08-06/bytedance-jimeng-ai/ | secondary | 2026-06-06 | 动点科技 | 即梦AI发布报道 |
| T02-S024 | https://www.infoq.cn/article/uguhq4s40lfguxgu7i8v | secondary | 2026-06-06 | InfoQ | Kolors可图应用实践长文 |
| T02-S025 | https://help.reditorapp.com/content/260129小红书推流机制.html | reference | 2026-06-06 | 红薯编辑器Reditor | 推流机制/5秒AI初审说明(厂商) |

> 黑名单已剔除：CSDN / 知乎 / 公众号(mp.weixin) / 百度 / 搜狐 / 简书 / 掘金。搜索中命中均未收录。
> bucket 说明：`creator.xiaohongshu.com`、`pgy.xiaohongshu.com`、`github.com` = verified_primary；数据/设计/数字人商业 SaaS 官网 = surrogate_primary (note: vendor docs)；行业媒体长报道 = secondary。

---

## 总览（按 tier 分组）

### 必备（7 个）
| 工具 | 一句话 | Decay | Sources |
|------|--------|-------|---------|
| 小红书创作服务平台 | 官方后台：发布/数据/笔记灵感/违规自查，唯一一手数据源 | low | T02-S001/S002 |
| 豆包(Doubao) | 中文「网感」最强的文案模型，平台适配标题/正文/脚本 | medium | T02-S020 |
| DeepSeek | 深度逻辑/结构化文案，干货长文与选题脑暴 | medium | T02-S020 |
| 即梦(Jimeng) | 字节文生图+视频+数字人一体，中文直出封面 | medium | T02-S005/S023 |
| 剪映(CapCut) | 口播/教程视频剪辑+智能字幕+数字人事实标准 | low | — |
| 稿定/Canva(二选一) | 模板化封面/大字报排版，3:4 一键出图 | low | T02-S006/S008 |
| 新红 OR 千瓜(数据平台二选一) | 选题/热搜词/对标爆款/复盘的第三方数据底座 | medium | T02-S011/S012 |

### 场景特化（8 个）
| 工具 | 一句话 | Decay | Sources |
|------|--------|-------|---------|
| Kimi | 长文本投喂/对标拆解(把多篇爆款喂进去抽结构) | medium | T02-S020 |
| 通义千问 | 中文写作均衡，阿里生态联动 | medium | T02-S020 |
| Claude / GPT | 英文逻辑与复杂改写强，但中文「小红书味」需重调 | medium | (推断) |
| 可图 Kolors | 开源中文文生图，本地批量/中文字渲染封面 | medium | T02-S004/S024 |
| MidJourney | 高审美概念图/插画风封面，中文字弱 | low | T02-S024 |
| HeyGen | 高质量数字人口播+多语言翻译，出海/真人替身 | high | T02-S010 |
| 蝉小红 | 蓝海词(近7天笔记少)抢位 + 爆文方向 | medium | T02-S014 |
| 灰豚数据 | 关键词抓取笔记+热度曲线，多平台监测 | medium | T02-S019/S020 |

### 新兴（3 个）
| 工具 | 一句话 | Decay | Sources |
|------|--------|-------|---------|
| 即梦数字人/口播一体流 | 即梦出形象+对口型→剪映成片的全AI口播链 | high(experimental) | T02-S005 |
| 蒲公英(商单侧工具) | 接商单/品牌合作的官方撮合，影响选题方向 | medium | T02-S003 |
| 违禁词/AI味检测工具(火兔等) | 发布前查违禁词+敏感表达，规避5秒AI初审限流 | high | T02-S025 |

---

## 工具卡片

### 1. 小红书创作服务平台（含笔记灵感 / 数据 / 违规自查）
- **One-liner**: 官方一站式后台——发布、账号/受众数据、笔记灵感选题、违规与限流自查。是唯一的一手数据源。
- **Tier**: 必备
- **Maintainer / Owner**: 小红书官方 (creator.xiaohongshu.com) (T02-S001)
- **License**: proprietary（免费，部分高阶功能需粉丝量/内容达标解锁）
- **Maturity signals**: 官方持续运营，2026-06-06 可访问；含「创作百科」「帮助与客服」(T02-S001)
- **典型使用场景**: 发图文/视频笔记 (T02-S002)；看本账号阅读/赞藏/受众画像复盘；用「笔记灵感」拿官方选题任务；发布时勾选「内容类型声明→笔记含AI合成内容」做AI标识 (evidence: [T02-S001, T02-S016])
- **不适合 / 替代**: 不做跨账号对标/竞品分析（要靠新红/千瓜/蝉小红）；不生成内容。
- **Decay risk**: low（官方基础设施，3+年稳定）

### 2. 豆包 Doubao（AI 文案 · 网感首选）
- **One-liner**: 字节国民级 AI，中文「网感」最强，针对小红书/抖音优化内容结构，写标题/正文/口播脚本。
- **Tier**: 必备
- **License**: proprietary（免费 + 会员）
- **典型使用场景**: 生成口语化标题/开头钩子；写种草正文；改写「人话化」降AI味；选题脑暴 (evidence: [T02-S020])
- **矛盾/坑**: 同质化——同主题多篇重复度偏高，直接套用易撞稿/触发原创度判定 (evidence: [T02-S020]，二手，标注为待验证)。
- **不适合 / 替代**: 深度逻辑长文不如 DeepSeek；需要长文本投喂对标用 Kimi。
- **Decay risk**: medium（模型迭代快，但厂商稳定）

### 3. DeepSeek（AI 文案 · 逻辑/干货）
- **One-liner**: 深度思考+联网，结构化干货长文、选题逻辑推演、文案框架搭建。
- **Tier**: 必备
- **License**: proprietary（免费 / API）
- **典型使用场景**: 知识干货类笔记的论证结构；把模糊主题拆成选题矩阵；标题公式套用后的逻辑校验 (evidence: [T02-S020])
- **不适合 / 替代**: 纯口语化「网感」不如豆包，输出常需二次「人话化」。
- **Decay risk**: medium

### 4. 即梦 Jimeng（AI 生图/封面/视频/数字人）
- **One-liner**: 字节剪映团队的一站式 AI 创作平台——文生图、图生图、AI 视频、智能画布，中文直出能力强，适合自媒体封面。
- **Tier**: 必备
- **Maintainer**: 字节跳动/剪映 (T02-S005)；2024-05 由「剪映 Dreamina」更名「即梦」(T02-S023)
- **License**: proprietary（免费额度+会员）
- **典型使用场景**: 文生图出封面主图/插画 (T02-S005)；图生图换背景/风格；智能画布一键扩图做 3:4 封面；AI 视频/数字人口播片段 (evidence: [T02-S005, T02-S023])
- **不适合 / 替代**: 精修排版/加大字报文字层不如稿定/Canva；高审美概念图可叠 MidJourney。
- **Decay risk**: medium

### 5. 剪映 CapCut（口播/教程剪辑 · 数字人）
- **One-liner**: 字节免费全能剪辑，智能字幕/智能抠像/数字人/一键成片，AI 教程与口播类视频的事实标准。
- **Tier**: 必备
- **License**: proprietary（免费 + 会员）
- **典型使用场景**: 口播视频加智能字幕；录屏教程剪辑；即梦出形象→剪映对口型成数字人；一键成片快速产资讯/合集 (evidence: [T02-S020])
- **不适合 / 替代**: 高端数字人质感不如 HeyGen；纯静态图文不需要。
- **Decay risk**: low（生态垄断级）

### 6. 稿定设计 / Canva 可画（封面排版 · 大字报）
- **One-liner**: 模板化在线设计，3:4 小红书封面/大字报/对比图一键排版，海量可商用模板。
- **Tier**: 必备（二选一）
- **Maintainer**: 稿定 (gaoding.com) / Canva 可画 (canva.cn)
- **License**: proprietary（免费 + 会员素材）
- **Maturity signals**: 稿定 10万+ 小红书专属模板、3:4 比例智能模板库 (T02-S006/S007)；Canva 搜「小红书」自动套 3:4(1242×1660) (T02-S008/S009)
- **典型使用场景**: 「大字报」封面（大标题+情绪词压在主图上）；前后对比图；图文干货的多页排版；探店图文拼图 (evidence: [T02-S006, T02-S009])
- **选型分界**: 电商/带货风、追求模板量与中文热点日历→稿定 (T02-S006)；小众/国际审美、纯浏览器协作→Canva (T02-S009)
- **不适合 / 替代**: AI 直接生成主图用即梦/可图；纯文字图也可即梦中文字渲染。
- **Decay risk**: low

### 7. 新红（数据 · 选题/热词/爆款）
- **One-liner**: 新榜旗下小红书数据工具，选题、热词、爆款笔记、达人、品类榜单、笔记分析全维度。
- **Tier**: 必备（数据平台二选一/二选多）
- **Maintainer**: 新榜有数 (xh.newrank.cn) (T02-S011)
- **License**: proprietary（部分免费 + 付费）
- **典型使用场景**: 24 大垂类榜单找选题；热词云+转化曲线找关键词；对标爆款笔记拆结构 (evidence: [T02-S011, T02-S018])
- **Decay risk**: medium（曾有平台与第三方数据方的法律摩擦风险，见避坑）

### 8. 千瓜数据（数据 · 历史深挖/热搜词）
- **One-liner**: 历史数据深度挖掘见长，热门笔记/热搜词排行/创作灵感，付费 SaaS。
- **Tier**: 必备（数据平台二选一）
- **License**: proprietary（会员制，预估数据需付费且有保密协议）(T02-S012)
- **典型使用场景**: 按标题/评论查热门笔记并看其热搜词+粉丝画像 (T02-S012)；热搜词排行榜抢推荐位 (T02-S013)；「创作灵感」没思路时看热门内容 (evidence: [T02-S012, T02-S013])
- **不适合 / 替代**: 蓝海词(近7天笔记少) 蝉小红更直接；轻量免费看可用新红免费部分。
- **Decay risk**: medium

### 9. Kimi（场景特化 · 长文本对标）
- **One-liner**: 长文本之王，把多篇爆款笔记/竞品长文投喂进去抽结构、做对标拆解。
- **Tier**: 场景特化
- **典型使用场景**: 喂 10 篇同赛道爆款→抽公共结构/钩子套路；长访谈/资料压缩成选题 (evidence: [T02-S020])
- **不适合 / 替代**: 口语化生成不如豆包；逻辑推演不如 DeepSeek。
- **Decay risk**: medium

### 10. 可图 Kolors（场景特化 · 开源中文文生图）
- **One-liner**: 快手开源中文文生图大模型，首个原生支持中文字符渲染（无需 ControlNet），中文海报/封面强。
- **Tier**: 场景特化
- **Maintainer**: 快手 (Kwai-Kolors) (T02-S004)
- **License**: open，Apache-2.0（MAU≤3亿自动获商用授权，超出需申请）(T02-S004)
- **Maturity signals**: GitHub 4.6k★ / 354 forks，2024-11 仍有新模型发布 (T02-S004, last checked 2026-06-06)；FlagEval 主观综合第二、仅次 DALL·E 3 (T02-S024)
- **典型使用场景**: 本地/批量出中文字封面；中文复杂字符渲染；系列封面统一风格 (evidence: [T02-S004, T02-S024])
- **不适合 / 替代**: 非技术博主直接用即梦更省事（即梦底层亦含强中文直出）；高审美用 MidJourney。
- **Decay risk**: medium

### 11. MidJourney（场景特化 · 高审美概念图）
- **One-liner**: 顶级审美概念图/插画风封面，氛围感强；中文字渲染弱、需付费、有门槛。
- **Tier**: 场景特化
- **License**: proprietary（订阅）
- **典型使用场景**: 高审美氛围封面/插画号；与 Kolors/即梦对比作审美上限锚 (evidence: [T02-S024])
- **不适合 / 替代**: 要中文大字封面→可图/即梦；要批量快出→即梦。
- **Decay risk**: low

### 12. HeyGen（场景特化 · 数字人口播）
- **One-liner**: 高质量数字人视频，照片定制形象、多语言克隆与翻译、对口型同步，出海/真人替身。
- **Tier**: 场景特化
- **Maintainer**: HeyGen (heygen.com) (T02-S010)
- **License**: proprietary（订阅）
- **典型使用场景**: 不想露脸的口播账号；一条内容翻译成多语种出海；上传照片做个人数字分身 (evidence: [T02-S010])
- **不适合 / 替代**: 国内免费/中文场景即梦+剪映数字人够用；纯图文不需要。
- **Decay risk**: high（数字人赛道竞争与平台AI标识政策双重变量，见避坑）

### 13. 蝉小红（场景特化 · 蓝海词/爆文方向）
- **One-liner**: 蝉妈妈旗下，找蓝海词（近7天笔记少的关键词）抢位 + 爆文方向 + 达人/笔记数据。
- **Tier**: 场景特化
- **Maintainer**: 蝉妈妈 (chanxiaohong.com) (T02-S014)
- **典型使用场景**: 热搜词搜索找近7天笔记少的蓝海词做选题布局；看爆文榜方向 (evidence: [T02-S014])
- **Decay risk**: medium

### 14. 灰豚数据（场景特化 · 关键词抓取/热度曲线）
- **One-liner**: 按关键词抓取并分类小红书笔记，可视化热度/关注度曲线，多平台(抖/红/快)监测。
- **Tier**: 场景特化
- **典型使用场景**: 抓某关键词全部笔记看分布；产品/品牌热度时间曲线复盘 (evidence: [T02-S019, T02-S020])
- **Decay risk**: medium

### 15. 蒲公英（新兴/特化 · 商单侧·影响选题）
- **One-liner**: 小红书官方品牌合作撮合平台，博主接商单/品牌合作的入口，反向影响选题方向。
- **Tier**: 新兴/特化
- **Maintainer**: 小红书官方 (pgy.xiaohongshu.com) (T02-S003)
- **典型使用场景**: 达标后接品牌商单；看品牌需求反推可做的种草选题 (evidence: [T02-S003])
- **Decay risk**: medium

### 16. 违禁词 / AI 味检测工具（新兴 · 发布前合规）
- **One-liner**: 发布前扫违禁词+敏感表达+AI 味，规避「发后5秒AI初审」限流。
- **Tier**: 新兴，`stability: experimental`
- **典型使用场景**: 笔记定稿后查违禁词；检查AI痕迹过重的段落 (evidence: [T02-S025])
- **不适合 / 替代**: 最终以小红书官方违规自查/标识为准 (T02-S001)。
- **Decay risk**: high（第三方工具更替快）

---

## 选型决策树

### 决策树 A：你这条内容是什么类型？

#### Branch 1: 图文干货（知识/教程截图/清单）
→ 文案: **DeepSeek** 搭结构 + **豆包**「人话化」开头钩子 (evidence: [T02-S020])
→ 封面: **稿定/Canva** 做「大字报」多页排版 (evidence: [T02-S006, T02-S009])
→ 选题: **新红/千瓜** 热搜词 + 创作灵感 (evidence: [T02-S011, T02-S012])

#### Branch 2: 测评/种草（产品对比/好物）
→ 文案: **豆包**（网感+痛点+种草话术）(evidence: [T02-S020])
→ 封面: **稿定** 前后对比图模板 + **即梦/可图** 出主图 (evidence: [T02-S006, T02-S005])
→ 数据: **蝉小红** 蓝海词抢位 / **灰豚** 关键词热度 (evidence: [T02-S014, T02-S019])

#### Branch 3: 口播/教程视频（露脸 or 数字人）
→ 真人口播: **豆包/DeepSeek** 写脚本 + **剪映** 智能字幕成片 (evidence: [T02-S020])
→ 数字人(不露脸): 国内/中文 → **即梦出形象 + 剪映对口型**；出海/高质感 → **HeyGen** (evidence: [T02-S005, T02-S010])
→ 必须发布时勾选 AI 标识，否则限流 (evidence: [T02-S001, T02-S016])

#### Branch 4: 资讯/合集（快产、量大）
→ **Kimi** 投喂多源长文压缩 → **豆包** 改写 → **剪映一键成片**（视频）(evidence: [T02-S020])
→ 高撞稿/搬运风险 → 必须人工重写+查原创度（见避坑）

### 决策树 B：AI 全自动 vs 精做？（核心矛盾）

#### Branch 1: 全自动批量（豆包写+即梦图+剪映成片）
→ 优点: 量大、快
→ 风险: AI 味重→限流、同质化→撞稿、未标识AI→限制分发 (evidence: [T02-S020, T02-S015, T02-S016])
→ 适合: 起号测方向阶段、资讯合集类；**不适合** 想做人设/长期账号

#### Branch 2: 精做（AI 辅助+人工重写+真实素材）
→ AI 只做选题脑暴/结构/初稿，正文用「人话」重写，封面用真实拍摄/亲测图
→ 投入产出比最高的「合规护城河」打法 (evidence: [T02-S021, T02-S022])
→ 适合: 人设号、商单号、长期主义

### 决策树 C：数据/选题工具选哪家？
→ 想要免费+多垂类榜单 → **新红**(部分免费) (evidence: [T02-S011, T02-S018])
→ 历史数据深挖+热搜词排行 → **千瓜**(付费) (evidence: [T02-S012, T02-S013])
→ 找蓝海词抢蓝海 → **蝉小红** (evidence: [T02-S014])
→ 关键词级笔记抓取/曲线 → **灰豚** (evidence: [T02-S019])
→ 自己账号复盘(唯一一手) → **创作服务平台** (evidence: [T02-S001])

---

## 避坑清单

- ❌ 不要把 AI 初稿直接发布：豆包等同主题多篇重复度偏高，易撞稿/触发原创度判定；AI 直出文本被判限流甚至违规 (evidence: [T02-S020, T02-S015])。精做派一律人工「人话化」重写。
- ❌ 不要忘记勾 AI 标识：2026-02 起小红书要求 AI 生成/合成内容主动标识（发布→设置→内容类型声明→勾「含AI合成内容」），未标识自动加标并**限制分发**，多次违规降权/封号；标识不可删改隐匿 (evidence: [T02-S015, T02-S016, T02-S017])。
- ❌ 不要搬运/洗稿做资讯合集：平台自动检测重复内容判「抄袭」，限流+处罚；Kimi 压缩多源后必须重组重写 (evidence: [T02-S022], 推断)。
- ❌ 不要忽视违禁词：发后约 5 秒 AI 初审筛违禁/标签，过不了直接零曝光；发布前用违禁词工具+官方自查 (evidence: [T02-S025, T02-S001])。
- ❌ 不要数字人廉价感/仿冒：低质数字人+未标识=新规重点打击（仿冒公众人物被点名）；即梦数字人也要标 AI、配真实信息密度 (evidence: [T02-S017, T02-S016])。
- ❌ 不要封面同质化：稿定/Canva 模板直接套→满屏一个样；用即梦/可图出差异化主图，大字报标题用自己的钩子 (evidence: [T02-S006, T02-S009])。
- ❌ 不要押注单一第三方数据平台：平台与第三方数据方曾有法律摩擦，数据口径/可用性有政策风险；交叉用新红+蝉小红+自家创作平台 (evidence: [T02-S018, T02-S019])。
- ❌ 不要用 MidJourney 出中文大字封面：中文字渲染弱；中文字封面用可图(Kolors 原生中文字)或即梦 (evidence: [T02-S004, T02-S024])。

---

## Phase 2 提炼提示

**反复出现 ≥ 3 source 强调的工具选型原则**（候选 playbook 规则）:
- 「AI 出初稿、人写终稿」：AI 只到选题/结构/初稿，正文与封面必须人工注入真实感与差异化，否则限流/撞稿 (出现于: T02-S020 / T02-S015 / T02-S021)。
- 「合规前置」：AI 标识 + 违禁词 + 原创度是发布前三道闸，工具栈必须含「自查」环节 (出现于: T02-S015 / T02-S016 / T02-S025)。
- 「数据驱动选题」：开写前先用数据平台找热搜/蓝海词对标爆款，不是凭感觉 (出现于: T02-S011 / T02-S012 / T02-S014)。
- 「字节生态闭环」：豆包(写)+即梦(图/视频/数字人)+剪映(剪) 是低成本默认链，但越闭环越要防同质化 (出现于: T02-S005 / T02-S020 / T02-S023)。

**显著的工具流派分裂**（候选 智识谱系条目）:
- **AI 全自动派**（豆包+即梦+剪映一键成片，量取胜）vs **AI 辅助精做派**（AI 仅脑暴/初稿，人工重写+真实素材，人设/合规取胜）。核心矛盾贯穿全文 (evidence: [T02-S020, T02-S021, T02-S015])。
- **数字人派** vs **真人出镜派**：数字人省事但有廉价感+新规标识/仿冒红线；真人出镜信任度高但产能低 (evidence: [T02-S010, T02-S017])。
- **封面流派**：模板排版派(稿定/Canva，大字报/对比图) vs AI 直出派(即梦/可图/MJ，主图生成)，实战常组合用 (evidence: [T02-S006, T02-S004])。

**新兴工具信号**:
- 当前活跃/上升: 即梦数字人一体流、违禁词/AI味检测工具、AI标识合规工具链——均由 2026-02 新规催生。
- 出现→主流速度估计: ~3-6 个月（政策驱动型，落地极快）。

**冷僻 / 信号薄弱**:
- 不冷僻。必备层 7 个 > 3，三层齐全；verified_primary 占比偏低（主因数据/设计/数字人 SaaS 按规范标 surrogate_primary「vendor docs」），但小红书官方(creator/pgy)与 GitHub(Kolors) 为硬一手锚点。
- 矛盾保留: AI 全自动 vs 精做、数字人 vs 真人——未强行收敛，留给 Phase 1.5/2 裁决。
- 待验证(二手): 豆包「同主题重复度 27%」「脚本完读率高18%」等具体数字来自二手评测，标注为待一手验证。

---

## 质量自检
- [x] 候选 ≥ 20（探索 ~20+，retained 16 张卡 + 数据平台4 + 文案模型5）
- [x] 三层齐全（必备 7 / 场景特化 8 / 新兴 3）
- [x] 每工具有 last_checked + maturity signal（Kolors 带 stars+日期）
- [x] 决策树 3 棵共 >10 节点，每节点挂 evidence
- [x] 避坑 8 条
- [x] 一手锚点: 小红书官方(S001-S003) + GitHub Kolors(S004) verified_primary；其余 SaaS 标 surrogate_primary(vendor docs)
- [x] Decay risk 每工具已标
- [x] Phase 2 接口已填
