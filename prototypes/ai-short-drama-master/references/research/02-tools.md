# Track 02 — Tools (AI 短剧 / AI 微短剧)

> 调研日期 2026-06-04 | locale=zh-CN（主战场中国 + 出海）| Track 02 = 本主题核心轨。
> 本文件按 master-skill Track 02 规范：总览表（按 tier）+ 工具卡片（含 last_checked / maturity）+ 选型决策树 + 避坑清单 + Phase 2 接口。
> **时效警告**：AI 视频工具是衰减最快的一节。本主题工具几乎每 2-3 个月一次大版本（Kling 3.0 / Seedance 2.0 / Wan2.6 都在 2025-12 ~ 2026-02 三个月内发布）。**每张卡片的 last_checked 都是 2026-06-04**，超过 3 个月需重刷视频生成模型节。

---

## Source Manifest

| source_id | url | bucket | last_checked | author/host | one-line note |
|-----------|-----|--------|--------------|-------------|---------------|
| T02-S001 | https://www.minimaxi.com/news/minimax-hailuo-23 | verified_primary | 2026-06-04 | MiniMax 官方 | Hailuo 2.3 发布(2025.10.28)，加量不加价 |
| T02-S002 | https://www.minimaxi.com/news/minimax-hailuo-02 | verified_primary | 2026-06-04 | MiniMax 官方 | Hailuo 02(2025.06.18)，1080p/NCR/极限物理 |
| T02-S003 | https://www.vidu.cn/ | verified_primary | 2026-06-04 | 生数科技 官方 | Vidu 参考生，最多 7 主体，首尾帧 |
| T02-S004 | https://www.shengshu.com/zh/vidu | dead | 2026-06-04 | 生数科技 | 404（官网改版，已被 vidu.cn 取代） |
| T02-S005 | https://www.volcengine.com/article/43436 | verified_primary | 2026-06-04 | 火山引擎(字节) | Seedance 2.0 专业版功能解析 |
| T02-S006 | https://www.volcengine.com/article/41267 | verified_primary | 2026-06-04 | 火山引擎(字节) | 即梦 Seedance 2.0 入口/全能参考 |
| T02-S007 | https://www.volcengine.com/product/tts | verified_primary | 2026-06-04 | 火山引擎(字节) | 豆包语音合成大模型产品页 |
| T02-S008 | https://ir.kuaishou.com/news-releases/news-release-details/kling-ai-launches-30-model-ushering-era-where-everyone-can-be/ | verified_primary | 2026-06-04 | 快手 IR 官方 | Kling 3.0 官方发布(2026.02.05) |
| T02-S009 | https://www.genaintel.com/guides/kling-3-0-kling-o3-release-features-2026 | secondary | 2026-06-04 | GenAIntel | Kling 3.0 功能/10图参考/2K4K 细节 |
| T02-S010 | https://docs.midjourney.com/hc/en-us/articles/32162917505293-Character-Reference | verified_primary | 2026-06-04 | Midjourney 官方文档 | Character Reference / V7 Omni(--oref) |
| T02-S011 | https://tongyi.aliyun.com/wan/ | verified_primary | 2026-06-04 | 阿里通义 官方 | 通义万相产品页 |
| T02-S012 | https://tongyi.aliyun.com/news?id=pxwhvf/suodqg/usofpg66drzae5s1 | verified_primary | 2026-06-04 | 阿里通义 官方 | Wan2.5 Preview(2025.12.02) 音画同步 |
| T02-S013 | https://www.heygen.com/pricing | verified_primary | 2026-06-04 | HeyGen 官方 | Avatar IV / 175+ 语言对口型 / 定价 |
| T02-S014 | https://pixverse.ai/en | verified_primary | 2026-06-04 | PixVerse 官方 | V5 原生音频+角色参考+多镜头 |
| T02-S015 | https://elevenlabs.io/blog/eleven-v3 | verified_primary | 2026-06-04 | ElevenLabs 官方 | Eleven v3(2025.06.03 GA) 70+ 语言 |
| T02-S016 | https://sensortower-china.com/zh-CN/blog/state-of-short-drama-apps-2025-report-CN | verified_primary | 2026-06-04 | Sensor Tower | 短剧出海 2025Q1 内购近 7 亿美元 |
| T02-S017 | https://lumalabs.ai/ray | verified_primary | 2026-06-04 | Luma 官方 | Ray3(2025.09.18)+Ray3.14(2026.01.26) HDR |
| T02-S018 | https://fal.ai/models/fal-ai/pika/v2.2/pikaframes | verified_primary | 2026-06-04 | fal.ai (Pika 托管) | Pika 2.2 Pikaframes 最多 5 关键帧 |
| T02-S019 | https://openai.com/index/sora-2/ | verified_primary | 2026-06-04 | OpenAI 官方 | Sora 2(2025.09.30) cameo/同步音频 |
| T02-S020 | https://36kr.com/p/3804766402698759 | secondary | 2026-06-04 | 36氪 | 即梦vs可灵长稿：月活/成本/一致性实测 |
| T02-S021 | https://www.tmtpost.com/7983893.html | secondary | 2026-06-04 | 钛媒体 | 即梦/可灵能否接住 AI 短剧风口 |
| T02-S022 | https://chatglm.cn/video | verified_primary | 2026-06-04 | 智谱 官方 | 清影(CogVideoX) 10s/4K/60帧/带音效 |
| T02-S023 | https://www.capcut.cn/ | verified_primary | 2026-06-04 | 剪映(字节) 官方 | 剪映：对口型/数字人/文本朗读/成片 |
| T02-S024 | https://www.ofweek.com/ai/2025-12/ART-201700-8110-30676614.html | secondary | 2026-06-04 | OFweek | 对话巨日禄：成本400元/分钟，播放破亿 |
| T02-S025 | https://www.yicai.com/news/102237108.html | secondary | 2026-06-04 | 第一财经 | 昆仑万维 SkyReels 一站式 AI 短剧平台 |
| T02-S026 | https://www.zhonglun.com/research/articles/9625.html | verified_primary | 2026-06-04 | 中伦律师事务所 | AIGC 生成内容版权归属：各产品用户协议梳理 |
| T02-S027 | https://docs.dev.runwayml.com/guides/pricing/ | verified_primary | 2026-06-04 | Runway 官方文档 | Runway API 计费 |
| T02-S028 | https://www.bilibili.com/video/BV1915v6bEcs/ | secondary | 2026-06-04 | 生数 B站官方号 | Vidu Q3 参考生升级实测：7 主体+镜头控制 |
| T02-S029 | https://www.volcengine.com/docs/6561/1167802 | verified_primary | 2026-06-04 | 火山引擎(字节) | 豆包声音复刻下单：~150元/年/音色 |

> **Bucket 分布**：verified_primary 21 / secondary 7 / dead 1（共 29，去重后有效 28）。一手占比 ≈ 75%（达标 ≥50%）。
> **黑名单已剔除**（搜到但未收录）：知乎(zhuanlan.zhihu.com / zhihu.com)、CSDN(blog.csdn.net)、百度百科(baike.baidu.com)、博客园(cnblogs.com)、SegmentFault 转载、microsoft news 农场、各 *.ai 评测内容农场(toolhatch/aitop100/devtk/somake 等)。命中即丢。
> **bucket 说明**：厂商官网/官方文档/官方 IR 按 master-skill「Surrogate Sources Policy → vendor docs = verified_primary（vendor 一手）」标 verified_primary（source_verifier 默认把未知 host 打 secondary，此处按规范人工升级，因为这些是厂商对自己产品的一手陈述）。行业媒体长稿(36氪/钛媒体/第一财经/OFweek/GenAIntel)保持 secondary。**一手 vendor 声称的画质/一致性需与二手实测交叉验证**（见下方矛盾保留）。

---

## 总览（按 tier 分组）

### 必备层（≥80% AI 短剧从业者会用到其中之一/组合）

| 工具 | 一句话 | Tier 内角色 | Decay | Sources |
|------|--------|------------|-------|---------|
| **即梦 Seedance（字节）** | 国内月活第一(1352万)、C 端创意爆破首选；全能参考(9图+3视频+3音频)+首尾帧+音画同步，成片率实测最高、成本最低 | 视频生成·量产派 | high | T02-S005,S006,S020,S021 |
| **可灵 Kling（快手）** | 专业级质感天花板、B 端影视制作首选；3.0 多模态(2K/4K/原生音频)、Image 3.0 支持 10 图参考、omni 解决"脸盲" | 视频生成·画质派 | high | T02-S008,S009,S020,S021 |
| **豆包 LLM / DeepSeek**（脚本） | 写剧本/分镜脚本/对白的 LLM 底座；豆包接即梦生态，DeepSeek 性价比 | 脚本 | medium | T02-S020,S024 |
| **即梦生图 / 可图 / Midjourney**（生图） | 角色定妆照/分镜首帧的来源；Midjourney V7 Omni Reference(--oref) 90%+ 角色一致 | 生图/角色锚定 | medium | T02-S010,S020 |
| **豆包语音 / 火山 TTS**（配音） | 中文短剧配音事实标准；声音复刻 5 秒克隆、相似度 97.5%、~150元/年/音色 | 配音 | low | T02-S007,S029 |
| **剪映 CapCut（字节）**（剪辑） | AI 短剧后期事实标准；已整合 Seedance 2.0，自带对口型/数字人/文本朗读/一键成片 16 项 AI | 剪辑+对口型 | low | T02-S023 |

### 场景特化层（特定子方向/出海/特定瓶颈）

| 工具 | 一句话 | 适合场景 | Decay | Sources |
|------|--------|---------|-------|---------|
| **Vidu（生数科技）** | 参考生视频，最多 7 主体一致性，首尾帧，4分/秒极致性价比 | 多角色/多道具一致性、低成本量产 | high | T02-S003,S028 |
| **海螺 Hailuo（MiniMax）** | 极限物理表现、运动稳定，2.3 强化肢体动作/微表情，性价比高 | 强物理/动作镜头、卡通插画风 | high | T02-S001,S002 |
| **通义万相 Wan（阿里）** | Wan2.6 是首个"角色扮演"视频模型：参考视频形象+音色生多角色合拍 15s | 角色扮演/真人音色复刻/多镜头叙事 | high | T02-S011,S012 |
| **Runway Gen-4/4.5 + Act-Two** | 角色参考+Act-Two 动作捕捉(手机录表演迁移到角色)，付费即商用 | 出海/表演驱动/动作迁移 | medium | T02-S027 |
| **OpenAI Sora 2** | cameo(录一次到处出演)+同步音频+多镜头一致；用户全权商用 | 出海高质量/欧美审美/IP cameo | high | T02-S019,S026 |
| **Luma Ray3 / Ray3.14** | 全球首个工作室级 HDR；单图角色参考+关键帧编辑 | 出海/电影级调色/HDR 交付 | medium | T02-S017 |
| **PixVerse V5.x** | 原生音频+对口型+多镜头+单图角色参考，覆盖 177 国 | 出海轻量量产/带音视频一体 | high | T02-S014 |
| **Pika 2.2 Pikaframes** | 关键帧串联(最多 5 帧)做 mini timeline，成本可预测 | 首尾帧/多段转场叙事 | high | T02-S018 |
| **智谱清影（CogVideoX）** | 10s/4K/60帧+自带音效，开源底座(CogVideoX) | 开发者自建/二开/学术 | medium | T02-S022 |
| **HeyGen（Avatar IV）** | 数字人口播+175+语言对口型译制，行业最佳对口型 | 出海译制/口播短剧/数字人主播 | medium | T02-S013 |
| **ElevenLabs v3**（配音） | 70+语言、最具表现力 TTS、audio tags 情绪标签、$5 起含商用 | 出海多语种配音/情绪化对白 | medium | T02-S015 |

### 新兴层（近 12 个月出现/起势的一站式工作流平台）

| 工具 | 一句话 | stability | Decay | Sources |
|------|--------|-----------|-------|---------|
| **SkyReels / SkyAnime（昆仑万维）** | 全球首款一站式 AI 短剧平台：剧本(SkyScript)+分镜(StoryboardGen)+3D+WorldEngine 一键成剧；2026 推 Agent 漫剧量产 SkyAnime | experimental | high | T02-S025 |
| **巨日禄（杭州巨日禄）** | AI 漫剧/真人剧一站式：剧本+绘画+分镜+配音配乐全流程，导出剪映；漫剧 400-700元/分钟，真人剧压到 1000元/分钟 | experimental | high | T02-S024 |

> **新兴层口径说明**：一站式平台仍是 experimental（厂商主导、版本快速迭代、6 个月后形态可能大变）。当前 AI 短剧实际生产主力仍是「单点工具手工串联」（脚本→生图→视频→配音→对口型→剪辑），一站式平台尚未取代手工链路（见决策树 D）。

---

## 工具卡片（核心工具详表）

### 1. 即梦 Seedance（字节跳动 / 火山引擎）

- **One-liner**：国内 AI 短剧 C 端量产首选 —— 多模态全能参考 + 首尾帧 + 音画同步，成片率与性价比业内最强，但长叙事(>1分钟)与多主体一致性是短板。
- **Tier**：必备（视频生成·量产派）
- **Maintainer**：字节跳动（消费端=即梦 jimeng.jianying.com / Dreamina；企业端 API=火山引擎 Seedance）(evidence: [T02-S006])
- **License**：proprietary，会员积分制
- **Maturity signals**：
  - Seedance 2.0 发布于 2026 年初（即梦平台上线，会员可用）(evidence: [T02-S006])
  - 月活：一季度 1352.5 万，春节峰值 4500 万（国内第一）(evidence: [T02-S020])
  - last_checked: 2026-06-04
- **核心能力**（厂商一手）：
  - **全能参考(omni-reference)**：可混合最多 **9 张图片 + 3 段视频(共 15s) + 3 段音频**，用 `@` 指派素材用途 → 生成 4-15s 视频 (evidence: [T02-S006])
  - **首尾帧**：上传首帧+尾帧，AI 补中间过渡 (evidence: [T02-S006])
  - **角色一致性**：上传人物图 1:1 复刻五官/服装/微表情；"首帧+尾帧+中间补帧"+多图融合+三维锚定机制 (evidence: [T02-S006, T02-S020])
  - **音画同步**：S2V 语音/口型同步，已成熟应用 (evidence: [T02-S020])
- **价格/积分**：会员积分制，基础年费会员约 **4.58 元/15s 视频**；火山引擎 API 约 **15.8 元/15s 1080P**；fast 模式省 30-50% 积分。月卡从 299 涨到 499 元（频繁涨价被吐槽）(evidence: [T02-S020])
- **商用授权**：成片无水印、商用级，宣称可直接用于广告/短剧/电商 (evidence: [T02-S006])
- **不适合/替代**：长叙事(>1分钟)短板明显、**不支持真人人脸参考与 IP 形象生成**、多人物互动易"主体崩坏"、高峰排队 8-10 小时 → 专业影视/真人 IP 用可灵，多主体用 Vidu (evidence: [T02-S020])
- **生产案例**：《霍去病》算力成本仅 3000 元；《万兽独尊》5 人 8 天完成 60 集 (evidence: [T02-S020])
- **可信度**：high（厂商一手 + 36氪/钛媒体二手交叉）
- **Decay risk**：high（>40%/12 月被改变 —— 字节迭代极快，Seedance 2.x 仍在快速演进）

### 2. 可灵 Kling（快手）

- **One-liner**：专业级质感天花板，B 端影视制作首选 —— 3.0 原生多模态(文/图/音/视一体)、2K/4K、Image 3.0 支持 10 图参考、omni 版从几秒视频提取主角建库解决"脸盲"。
- **Tier**：必备（视频生成·画质派）
- **Maintainer**：快手（klingai.com / kling.ai）(evidence: [T02-S008])
- **License**：proprietary，会员"灵感值"积分制
- **Maturity signals**：
  - **Kling 3.0 发布 2026-02-05**（Video 3.0 / Video 3.0 Omni / Image 3.0 / Image 3.0 Omni）(evidence: [T02-S008])
  - 截至 2025-12 全球 4500 万用户，生成 1.68 亿视频 / 3.44 亿图，ARR 破 1 亿美元，B 端客户 2 万+ (evidence: [来自快手 2025-12 数据，see note])
  - 月活：一季度 119.1 万（远低于即梦，主打 P 端高 ARPU）(evidence: [T02-S020])
  - last_checked: 2026-06-04
- **核心能力**：
  - **统一多模态架构**：文生视频/图生视频/参考生视频/视频内编辑一体；原生 2K/4K；原生多语言/方言/口音音频 (evidence: [T02-S008, T02-S009])
  - **多图参考**：Image 3.0 支持最多 **10 张参考图**（主体轮廓+色调识别、风格迁移、角色参考、多图融合）(evidence: [T02-S009])
  - **视频时长**：最长 15s (evidence: [T02-S009])
  - **omni 角色一致性**：从几秒视频提取主角建库，后续生成"主角永远是那张脸，绝对不穿帮" (evidence: [T02-S020])
  - **分镜能力**：自动拆解出含不同景别的多个分镜，保持主体一致性 (evidence: [T02-S020])
- **价格/灵感值**（国内月卡）：黄金 66 元(660 灵感值/~66 视频) / 铂金 266 元(3000/~300) / 钻石 666 元(8000/~800)；年卡 396/1596/3996 元。全球版 $10/$37/$92。会员独享：**首尾帧、视频延长、大师运镜、去水印** (evidence: [来自快手会员体系数据，see note])
- **商用授权**：B 端开放 API（广告/影视/电商），强调生成内容版权保护机制；**去水印是会员专属权益**（免费层有水印）。具体"用户拥有生成内容版权"条款页(klingai.com/app/docs/user-policy) JS 渲染未抓到原文 → **VERIFY GAP**，需人工确认 (evidence: [T02-S020, T02-S026])
- **不适合/替代**：算力基础薄弱依赖第三方云、并发压力大；C 端量产速度/成本不及即梦 → 高频量产用即梦 (evidence: [T02-S020])
- **生产案例**：参与《太平年》《大卫王朝》等剧集制作 (evidence: [T02-S020])
- **可信度**：high
- **Decay risk**：high（3.0 刚发，后续 omni/视频内编辑仍在快速演进）

> note：可灵 4500 万用户/ARR/会员价格来自快手公开披露与会员体系报道（搜索聚合），属厂商一手数据但本轮未逐条 WebFetch 官方页验证，标 medium-confidence 数字。

### 3. Vidu（生数科技 + 清华）

- **One-liner**：多主体一致性专家 —— 参考生视频支持最多 7 个主体（人物+道具+场景）同框一致，首尾帧，4 分钱/秒极致性价比，10 秒级出片。
- **Tier**：场景特化（多角色/多道具一致性）
- **Maintainer**：北京生数科技（vidu.cn / shengshu.com）(evidence: [T02-S003])
- **License**：proprietary
- **Maturity signals**：Vidu Q3 参考生升级(最多 7 主体+镜头控制+情绪演绎)；Vidu 2.0 降至 4 分/秒、10 秒级出片(较 1.5 提速 3 倍)(evidence: [T02-S003, T02-S028])；last_checked 2026-06-04
- **核心能力**：参考生视频(上传 3+ 图或多角度同主体图)；多主体一致性(最多 7 主体)；首尾帧(自动补过渡)；文生/图生/参考生三模式 (evidence: [T02-S003, T02-S028])
- **价格**：低至 4 分/秒(Vidu 2.0)；有免费额度 (evidence: [T02-S003])
- **不适合/替代**：综合画质质感不及可灵 3.0；单主体高质量镜头用即梦/可灵更稳
- **可信度**：high（官方 + B站官方实测视频）
- **Decay risk**：high

### 4. 海螺 Hailuo（MiniMax）

- **One-liner**：物理/运动稳定担当 —— Hailuo 02 极限物理表现(体操等)宣称全球唯一，2.3 强化肢体动作/微表情/风格化，加量不加价。
- **Tier**：场景特化（强物理/动作/卡通插画）
- **Maintainer**：MiniMax（minimaxi.com / hailuoai.com）(evidence: [T02-S002])
- **Maturity signals**：Hailuo 02 = **2025-06-18**(1080p, 768p-6s/768p-10s/1080p-6s, NCR 架构, 效率↑2.5×, 参数 3×/数据 4×, AA Video Arena 全球第二)(evidence: [T02-S002])；Hailuo 2.3 = **2025-10-28**(动态表现升级, 风格化扩展, 价格不变)(evidence: [T02-S001])；last_checked 2026-06-04
- **核心能力**：极限物理表现；复杂人物肢体/微表情；风格化(动漫/插画/水墨/游戏CG)；2.3 Fast 批量省 50% (evidence: [T02-S001, T02-S002])
- **角色一致性**：官方发布稿**未提**多主体一致性/参考图功能（S2V 主体参考能力 85% 还原率系第三方说法，需验证）(evidence: [T02-S001, T02-S002])
- **价格**：宣称"业内最优价格"，2.3 维持 02 定价；API(Atlas Cloud)约 $0.08/秒 (evidence: [T02-S001])
- **不适合/替代**：角色长程一致性方案不如即梦/可灵/Vidu 明确 → 一致性敏感场景配合外部锚定
- **可信度**：high(官方) / 一致性还原率为推断
- **Decay risk**：high

### 5. 通义万相 Wan（阿里）

- **One-liner**：角色扮演开创者 —— Wan2.6 号称全球首个支持"角色扮演"的视频模型，基于参考视频形象+音色生成多角色合拍、多镜头叙事 15s，声画同步、智能分镜。
- **Tier**：场景特化（角色扮演/真人音色复刻/多镜头）
- **Maintainer**：阿里巴巴通义（tongyi.aliyun.com / 阿里云百炼 API）(evidence: [T02-S011])
- **Maturity signals**：**Wan2.5 Preview = 2025-12-02**(首次音画同步, 1080P/24fps, 5s→10s)(evidence: [T02-S012])；**Wan2.6 = 2025-12-26**(角色扮演, 多人对话, 更长时长, 15s)(evidence: [T02-S012])；last_checked 2026-06-04
- **核心能力**：音画同步(人声+音效+BGM 匹配口型)；角色扮演(参考视频形象+音色→多角色合拍)；多镜头叙事+智能分镜 (evidence: [T02-S012])
- **价格/商用**：阿里云百炼 API 调用 / 通义官网体验；截至 2026-04 **未确认 Wan2.5/2.6 本体开源**（早期 Wan2.1 等有开源版本，但 2.5/2.6 走 API）(evidence: [T02-S011, T02-S012])
- **不适合/替代**：国内短剧圈渗透率/案例数不及即梦可灵 → 主流量产仍首选双巨头，Wan 作"角色扮演"特化补充
- **可信度**：high(官方)
- **Decay risk**：high

### 6. Runway Gen-4/4.5 + Act-Two（出海）

- **One-liner**：出海表演驱动首选 —— 角色参考保一致 + Act-Two 动作捕捉(手机录一段表演迁移到目标角色)，付费即拥有商用版权。
- **Tier**：场景特化（出海/表演迁移/动作捕捉）
- **Maintainer**：Runway（runwayml.com）
- **Maturity signals**：Act-Two 发布 **2025-07**；Gen-4.5 文生视频 + Gen-4 图生视频 + Act-Two + Veo 集成；2026 定价 Standard $15/mo(年付 $12)(evidence: [T02-S027])；last_checked 2026-06-04
- **核心能力**：角色参考保一致；Act-Two(上传驱动表演视频+角色参考图→迁移面部/肢体/手势/头转)；Aleph 视频编辑
- **商用授权**：**付费计划(Standard/Unlimited/Enterprise)拥有完全商用版权**；免费层不含商用 (evidence: [T02-S026])
- **不适合/替代**：国内访问/支付不便，中文审美与即梦可灵有差 → 国内项目用国产，出海/动作迁移用 Runway
- **可信度**：high(官方文档 + 中伦法律分析)
- **Decay risk**：medium

### 7. OpenAI Sora 2（出海）

- **One-liner**：出海高质量 + IP cameo —— 录一次自己即可在任意视频出演(外观+声音准确)，同步音频/对白、多镜头一致，用户全权商用。
- **Tier**：场景特化（出海欧美审美/cameo IP）
- **Maintainer**：OpenAI（openai.com）
- **Maturity signals**：**Sora 2 = 2025-09-30**(美/加首发, invite-only app)；同步对白+音效、更强物理与世界建模、多镜头一致；默认 10s 竖屏 (evidence: [T02-S019])；last_checked 2026-06-04
- **核心能力**：cameo(经同意把自己/朋友插入 AI 视频, 外观+声音准确)；同步音频；多镜头一致 (evidence: [T02-S019])
- **商用授权**：**OpenAI 把 outputs 全部 rights/title/interest 转移给用户**，可商用(广告/产品/服务)；Disney 授权角色另有条款 (evidence: [T02-S026, T02-S019])
- **风险**：消费端 app 与 API 形态多次调整（搜索显示 2026 内有 app/API 变动传闻）→ 长期可得性需关注；国内不可直接访问
- **可信度**：high(OpenAI 官方)
- **Decay risk**：high(产品形态/可得性变动频繁)

### 8. 配音层：豆包语音(火山) / ElevenLabs

- **豆包语音合成大模型（火山引擎，国内事实标准）**：
  - TTS 2.0 + 声音复刻 2.0 = **2025-10** 发布，LLM 架构(理解后情绪表达)；声音复刻 **5 秒克隆、相似度 97.5%**；适用场景**明确含"短视频短剧配音"** (evidence: [T02-S007])
  - 价格：一个音色约 **150 元/年** + 1 元/月存储；新用户免费额度起 10 万字符 (evidence: [T02-S029])
  - Tier：必备(配音)；Decay：low(基础设施级)
- **ElevenLabs v3（出海）**：
  - **2025-06-03 GA**，70+ 语言(含中文)，audio tags 情绪标签([excited]/[whispers])，Text-to-Dialogue 多角色对话端点 (evidence: [T02-S015])
  - 价格：Starter $5/mo(含商用授权+即时声音克隆) / Creator $22/mo(专业声音克隆)；即时克隆 30 秒音频、专业克隆 3 分钟+ (evidence: [T02-S015])
  - Tier：场景特化(出海多语种)；Decay：medium

### 9. 对口型/数字人层：剪映 / HeyGen / 即梦 / 可灵

- **剪映 CapCut（字节，国内后期+对口型事实标准）**：AI 对口型(图/视频人物按音频或文字朗读)、数字人、文本朗读、音色克隆、一键成片等十余项；**2026 核心功能深度整合 Seedance 2.0，共 16 项 AI**。对口型在多语言/方言时口型同步"不够自然" (evidence: [T02-S023])。Tier 必备(剪辑+对口型)；Decay low
- **HeyGen（出海数字人/译制）**：Avatar IV 全身动捕数字人 + **175+ 语言对口型译制**(替换原音+调口型)，行业最佳对口型；Creator $29/mo / Pro $49/mo / Business $149/mo，Avatar IV 20 credits/分钟 (evidence: [T02-S013])。Tier 场景特化；Decay medium
- **可灵/即梦自带对口型**：可灵 3.0 / 即梦 S2V 均内置口型同步，单工具闭环时优先用其原生能力（省去导入导出）(evidence: [T02-S008, T02-S020])

### 10. 一站式平台：SkyReels（昆仑万维）/ 巨日禄

- **SkyReels / SkyAnime（昆仑万维）**：
  - 全球首款集成视频大模型+3D 大模型的 AI 短剧平台，集**剧本生成(SkyScript)+角色定制+分镜(StoryboardGen)+剧情+对白/BGM+影片合成**于一体，"一键成剧"；含 3D 生成(Sky3DGen)+WorldEngine(AI 3D 引擎与视频大模型融合) (evidence: [T02-S025])
  - 2025 起开源/发布 SkyReels V1/V2/A1/A2/A3；2026 推 Agent 网页端一站式 AI **漫剧**量产工具 **SkyAnime**；制作周期周级→小时级，一人成剧 (evidence: [T02-S025])
  - 出海：2026-02 官宣千万美金 + 百万扶持政策加持海外 AI 短剧；旗下出海产品 DramaWave (evidence: [T02-S025])
  - Tier 新兴(experimental)；Decay high
- **巨日禄（杭州巨日禄科技）**：
  - 垂直 AI **漫剧**起家(2023-10 上线)，一站式集成 **AI 剧本+AI 绘画+AI 分镜+AI 配音配乐** 全流程，**支持导出剪映二次编辑**；数字资产库(角色/道具/场景)可共用 (evidence: [T02-S024])
  - 成本：2D 漫剧综合成本压到 **400-700 元/分钟**(一年前传统 2000-5000)；2026-01 重点布局 **AI 真人剧**，真人短剧成本压到约 **1000 元/分钟**(80 分钟剧总成本 8-10 万，传统实拍 1/10)；熟练 1 人/天产 1-2 分钟，15 人 3 天产一部 (evidence: [T02-S024])
  - 生产案例：成本四百、播放破亿 (evidence: [T02-S024])
  - Tier 新兴(experimental)；Decay high

---

## 选型决策树

### 决策树 A：国内 vs 出海？（第一分叉，决定整条工具链）

- **国内（抖音/快手/红果短剧 等）** → 视频用 **即梦 / 可灵 / Vidu**（国产、可商用、可付费、可接生态）；配音 **豆包语音/火山 TTS**；剪辑+对口型 **剪映**。
- **出海（ReelShort/DramaBox 系，2025Q1 内购近 7 亿美元、同比~300%）**(evidence: [T02-S016]) → 视频可加 **Runway/Sora 2/Luma/PixVerse**（欧美审美 + 明确商用授权）；配音 **ElevenLabs**；译制对口型 **HeyGen(175+语言)**。

### 决策树 B：你的核心目标/阶段是什么？

#### Branch 1：快速验证想法 / demo（个人/小团队）
→ 推荐：**即梦 Seedance**（全能参考 + 成片率最高 + 成本最低 + 接剪映生态，C 端创意爆破首选）(evidence: [T02-S006, T02-S020])
→ 出海 demo：**PixVerse V5**（原生音频+对口型+角色参考一体，177 国，轻量）(evidence: [T02-S014])
→ 不推荐：一开始就上 SkyReels/巨日禄一站式（学习成本+平台锁定，先用单点工具跑通流程再说）

#### Branch 2：要专业级画质 / 进影视工业管线（B 端）
→ 推荐：**可灵 Kling 3.0**（专业视觉艺术家可过眼、自动分镜保主体一致、2K/4K、B 端 API）(evidence: [T02-S008, T02-S020])
→ 出海高端：**Sora 2**（多镜头一致+cameo+全权商用）或 **Luma Ray3**（工作室级 HDR 交付）(evidence: [T02-S019, T02-S017])

#### Branch 3：瓶颈在「角色/场景一致性」（行业第一性难题）
##### Branch 3a：单主角跨镜头一致 → **可灵 omni**（视频提取主角建库，"绝对不穿帮"）或 **即梦角色参考**(1:1 复刻五官) (evidence: [T02-S020, T02-S006])
##### Branch 3b：多角色/多道具同框一致 → **Vidu 参考生**（最多 7 主体）—— 即梦在多主体复杂场景易崩坏 (evidence: [T02-S028, T02-S020])
##### Branch 3c：要真人形象+音色复刻演角色 → **通义万相 Wan2.6 角色扮演** 或 **Runway Act-Two**（即梦明确不支持真人人脸参考）(evidence: [T02-S012, T02-S027, T02-S020])
##### Branch 3d：风格化角色定妆/分镜首帧 → **Midjourney V7 Omni Reference(--oref)**（90%+ 一致，单参考图）→ 再喂给视频模型做首帧 (evidence: [T02-S010])

#### Branch 4：瓶颈在「成本/积分烧钱」要极致性价比量产
→ 推荐：**Vidu(4分/秒)** + **即梦 fast 模式(省30-50%)** + **巨日禄漫剧线(400-700元/分钟)** (evidence: [T02-S003, T02-S006, T02-S024])
→ 配音用 **豆包声音复刻(150元/年/音色 摊薄到几乎免费)** (evidence: [T02-S029])

### 决策树 C：用什么形态做？真人短剧 vs 漫剧（AI 动画）
- **AI 漫剧（2D 动画风，当前 ROI 最高、成本最低）** → **巨日禄**(漫剧专精) 或 **SkyAnime**(Agent 量产) 一站式 + Midjourney 定角色 (evidence: [T02-S024, T02-S025])
- **AI 真人短剧（写实，难度更高、一致性更难）** → 即梦/可灵 + Wan2.6/Runway Act-Two(真人形象) + 剪映/HeyGen 对口型；巨日禄/SkyReels 也在布局真人线 (evidence: [T02-S024, T02-S027])

### 决策树 D：一站式平台 vs 手工串联？
- **要可控、要画质、要不被锁定** → **手工串联**（脚本 LLM → 生图 → 视频模型 → TTS → 对口型 → 剪映），当前专业产能主力。
- **要极致效率/团队协作/资产库复用/量产漫剧** → **一站式(SkyReels/巨日禄)**，但接受 experimental(平台快速变、画质受平台模型限制)。

---

## 避坑清单

- ❌ **不要默认"一个视频模型搞定一切"**：当前没有任何单一模型同时拿下「画质 + 多主体一致性 + 长叙事 + 真人形象 + 低成本」。即梦成片率/成本最好但长叙事弱+不支持真人脸；可灵画质好但成本/并发承压；Vidu 多主体强但质感一般 → **必须组合**。(evidence: [T02-S020, T02-S006, T02-S028])
- ❌ **不要忽视免费层的商用授权坑**：Midjourney 免费层只给 CC-BY-NC（非商用），**付费会员才拥有资产**；Runway 免费层不含商用；可灵**去水印是会员专属**。短剧要发布变现，必须用付费层并确认商用条款。(evidence: [T02-S026, T02-S020])
- ❌ **不要把"宣称的角色一致性"当成"实测稳定"**：厂商发布稿都说能保一致，但实测即梦"人物动作时灵时不灵、情绪表达看 AI 心情"、多人物互动易主体崩坏；海螺官方根本没提多主体一致性 → **以连续多次抽卡的成片率为准**(即梦实测 100 次约 95 次商用可用)。(evidence: [T02-S020])
- ❌ **不要低估"成片率/抽卡烧积分"**：AI 短剧真实成本不是单段价格，而是 `单段价 ÷ 成片率`。选成片率高的(即梦 95%、抽卡效率宣称提升 10×)能显著省积分，否则反复重生成把积分烧光。(evidence: [T02-S020])
- ❌ **不要忽略高峰排队/降智**：即梦高峰排队 8-10 小时、出现"降智"；可灵并发压力大 → 量产排期要预留 buffer，或备双工具切换。(evidence: [T02-S020])
- ❌ **不要用错对口型工具**：多语言/方言时剪映对口型"不够自然"；出海多语种译制对口型用 **HeyGen(175+语言)** 更稳；单工具闭环时优先用可灵/即梦原生 S2V 省去导入导出。(evidence: [T02-S023, T02-S013])
- ❌ **不要把一站式平台当成"画质保障"**：SkyReels/巨日禄解决的是"效率/串联/资产复用"，画质受其底层模型限制；对画质有高要求的镜头仍需回到可灵/Sora 单独生成再合成。(evidence: [T02-S024, T02-S025])

---

## Phase 2 提炼提示

**反复出现 ≥3 source 都强调的「工具选型原则」**（候选 playbook 规则）：
- **组合优先、没有银弹**：画质/一致性/成本/真人四难全占不可能，必须按瓶颈组合 (出现于 T02-S020 / S006 / S028)
- **成片率 = 真实成本**：选工具看 `单段价÷成片率` 而非单段标价，成片率高=省积分 (出现于 T02-S020 / S006 / S024)
- **付费层才有商用权**：免费层普遍非商用/带水印，变现必须付费并确认条款 (出现于 T02-S026 / S020 / S027)
- **国内/出海是第一分叉**：决定整条链(视频/配音/对口型/支付/审美)，不能混用 (出现于 T02-S016 / S013 / S015)

**显著的工具流派分裂**（候选 智识谱系条目）：
- **量产派(C 端/低成本/高成片率)** —— 代表：即梦 Seedance、Vidu、巨日禄漫剧线；目标"一人/小团队高频出片" vs **画质派(B 端/影视工业/质感)** —— 代表：可灵 Kling、Sora 2、Luma Ray3；目标"过专业艺术家眼睛"。两派对应不同变现模型(C 端走量 vs B 端高 ARPU)。
- **一站式平台派(SkyReels/巨日禄/SkyAnime)** vs **手工串联派(单点工具自由组合)**：效率/锁定 vs 可控/画质 的经典权衡。

**新兴工具信号**：
- 当前活跃/上升的新工具/版本数：视频模型近 9 个月密集大版本(Sora 2 9月、Hailuo 2.3 10月、Wan2.5/2.6 12月、Ray3.14 1月、Kling 3.0 2月)；一站式平台 2 个(SkyReels/巨日禄)在 experimental。
- 出现→主流速度：视频生成模型「发布→被短剧团队采用」≈ 1-3 个月(极快)；一站式平台尚未到主流(手工串联仍是主力)。

**冷僻/信号薄弱**：
- **不冷**：必备层 6 项均有 ≥3 source 与多个真实量产案例(《霍去病》《太平年》等)，verified_primary 占比 ~75%。
- **薄弱点 / VERIFY GAP**：(1) **可灵用户协议"生成内容版权归属"原文**未抓到(页面 JS 渲染)，仅有二手"去水印=会员/B端 API 商用"——商用条款需人工确认；(2) **海螺 S2V 85% 角色还原率** 系第三方说法，官方未证实；(3) **可灵 4500 万用户/会员价格** 为搜索聚合的厂商数据，未逐条 WebFetch 官方页验证，数字标 medium-confidence。
- **保留的矛盾（厂商宣称 vs 实测）**：即梦官方称"1:1 复刻五官/微表情、商用级稳定" vs 36氪实测"动作时灵时不灵、多主体易崩坏"；海螺官方称"极限物理全球唯一" vs 这是单点能力、不代表叙事/一致性可用。**一致性是行业第一性难题，所有厂商宣称都需以实际成片率打折看待。**
