# Track 05 — Sources：AIGC 创作工作流（生成式 AI 视觉创作）

> locale=global · focus=operational + technical
> 覆盖：图像（Midjourney / SD / Flux / ComfyUI）+ 视频（可灵 Kling / 即梦 Jimeng / Runway / Sora）创作侧。
> 信息源 = newsletter / 博客 · podcast / YouTube / B站 频道 · 社区 / 平台 · 会议 · dataset。

## Source Manifest

| source_id | url | bucket | last_checked | author/host | one-line note |
|-----------|-----|--------|--------------|-------------|---------------|
| T05-S001 | https://bfl.ai/blog/flux-2 | verified_primary | 2026-06-22 | Black Forest Labs | FLUX 模型方官方博客，每次模型发布的一手信源 |
| T05-S002 | https://huggingface.co/blog | verified_primary | 2026-06-22 | Hugging Face | HF 官方博客 + diffusers 团队，开源生成模型集散一手 |
| T05-S003 | https://huggingface.co/black-forest-labs | verified_primary | 2026-06-22 | Black Forest Labs | BFL 在 HF 的模型主页（FLUX.1/.2 权重 + card） |
| T05-S004 | https://stability.ai/news | secondary | 2026-06-22 | Stability AI | SD/SDXL/SD3 官方新闻（机构博客） |
| T05-S005 | https://www.latent.space/podcast | verified_primary | 2026-06-22 | swyx / Latent Space | AI engineering 长访谈，含 videogen/视觉生成专题 |
| T05-S006 | https://www.youtube.com/c/NerdyRodent | verified_primary | 2026-06-22 | Nerdy Rodent | 本地 AI 开源工作流头部 up（ComfyUI/Flux/WAN） |
| T05-S007 | https://www.youtube.com/@sedetweiler | verified_primary | 2026-06-22 | Scott Detweiler | Stability QA 本人，ComfyUI 系统课头部 |
| T05-S008 | https://www.youtube.com/@pixaroma | verified_primary | 2026-06-22 | Pixaroma | ComfyUI from scratch 全课 + 设计向 AI 工作流 |
| T05-S009 | https://www.youtube.com/@MattVidPro | verified_primary | 2026-06-22 | MattVidPro AI | AI 视频/图像工具横评，新模型第一时间上手 |
| T05-S010 | https://www.youtube.com/@TheoreticallyMedia | verified_primary | 2026-06-22 | Theoretically Media | AI 视频创作向（Runway/Kling/Sora）实操频道 |
| T05-S011 | https://www.youtube.com/@mreflow | verified_primary | 2026-06-22 | Matt Wolfe | AI 工具发现头部 + Future Tools newsletter |
| T05-S012 | https://www.youtube.com/@comfyuitutorial | verified_primary | 2026-06-22 | ComfyUI Tutorial | 专注 ComfyUI 节点工作流教学 |
| T05-S013 | https://civitai.com/ | secondary | 2026-06-22 | Civitai | 最大 SD/Flux 模型 + LoRA 分享社区 |
| T05-S014 | https://openart.ai/ | secondary | 2026-06-22 | OpenArt | ComfyUI 工作流模板社区 + 比赛 |
| T05-S015 | https://www.liblib.art/ | secondary | 2026-06-22 | LiblibAI 哩布哩布 | 国内最大 AI 绘画模型社区（zh-CN） |
| T05-S016 | https://tusi.cn | secondary | 2026-06-22 | 吐司 TusiArt | 国内在线生图 + 模型社区（zh-CN，无显卡可用） |
| T05-S017 | https://www.reddit.com/r/StableDiffusion/ | reference | 2026-06-22 | r/StableDiffusion | 开源图像生成最大讨论社区 |
| T05-S018 | https://www.reddit.com/r/comfyui/ | reference | 2026-06-22 | r/comfyui | ComfyUI 工作流专属社区 |
| T05-S019 | https://space.bilibili.com/ | verified_primary | 2026-06-22 | 秋葉aaaki (B站) | 国内 SD/ComfyUI 整合包 + 教程头部 up（zh-CN） |
| T05-S020 | https://laion.ai/ | secondary | 2026-06-22 | LAION | 训练数据集（LAION-5B），有版权/伦理争议 |
| T05-S021 | https://www.youtube.com/runwayml | reference | 2026-06-22 | Runway | Runway 官方频道 + Gen 系列发布/教程 |
| T05-S022 | https://aif.runwayml.com/ | secondary | 2026-06-22 | Runway | AI Film Festival (AIFF)，年度 AI 影像活动 |
| T05-S023 | https://discord.com/invite/midjourney | secondary | 2026-06-22 | Midjourney | 官方 Discord（1800万+），MJ 创作即在此发生 |
| T05-S024 | https://jimeng.jianying.com/ | verified_primary | 2026-06-22 | 字节跳动 即梦 | 即梦 AI 官方（图+视频创作平台，zh-CN） |
| T05-S025 | https://app.klingai.com/ | secondary | 2026-06-22 | 快手 可灵 Kling | 可灵 AI 官方（视频生成，已全球开放） |
| T05-S026 | https://curiousrefuge.com/ | secondary | 2026-06-22 | Curious Refuge | AI 电影制作教育 + 社区（首个 AI filmmaking 课） |
| T05-S027 | https://www.youtube.com/@CuriousRefuge | verified_primary | 2026-06-22 | Curious Refuge | AI 影视工作流频道（行业访谈 + 制作流） |
| T05-S028 | https://www.youtube.com/@TaoPrompts | verified_primary | 2026-06-22 | Tao Prompts | AI 影像 prompting（角色一致性/运镜/i2v） |
| T05-S029 | https://www.youtube.com/@pixaroma | verified_primary | 2026-06-22 | Pixaroma | ComfyUI 全课 + 设计向 AI 工作流（与 S008 同） |
| T05-S030 | https://huggingface.co/datasets/laion/laion2B-en | verified_primary | 2026-06-22 | LAION | LAION-2B-en 数据集页（diffusion 预训练基底） |
| T05-S031 | https://blog.comfy.org/ | verified_primary | 2026-06-22 | Comfy Org | ComfyUI 官方博客（节点更新/模型支持公告） |
| T05-S032 | https://www.theneuron.ai/ | secondary | 2026-06-22 | The Neuron | 日更 AI newsletter（700K+），含创作工具动态 |
| T05-S033 | https://www.xiaoyuzhoufm.com/podcast/5e5c52c9418a84a04625e6cc | verified_primary | 2026-06-22 | 硅谷101 | 小宇宙 zh-CN 播客，AIGC 特辑（生成式视觉） |
| T05-S034 | https://www.youtube.com/@Aitrepreneur | verified_primary | 2026-06-22 | Aitrepreneur | 本地 AI 安装/LoRA 训练/动画实操头部频道 |
| T05-S035 | https://www.youtube.com/@OliviaGodici | verified_primary | 2026-06-22 | Olivia Godici | ComfyUI 创意工作流频道（标信号：需二次确认活跃度） |

## 总览（按 type 分组）

### Newsletter / 博客 — 8 个

| Source | Cadence | Tier | 投入产出 | One-liner |
|--------|---------|------|---------|-----------|
| BFL Blog (T05-S001) | per-release | practitioner/senior | high | FLUX 系列模型一手发布 + 技术报告 |
| Hugging Face Blog (T05-S002) | weekly+ | practitioner | high | diffusers/开源生成模型生态枢纽 |
| ComfyUI Blog (T05-S031) | per-release | practitioner | high | ComfyUI 节点/模型支持官方公告 |
| Stability AI News (T05-S004) | per-release | mixed | medium | SD 系官方新闻 |
| Future Tools (Matt Wolfe) (T05-S011) | 2x/week | beginner/practitioner | medium | AI 工具发现，覆盖创作工具 |
| Civitai Blog (T05-S013) | rolling | practitioner | medium | 社区模型动态 + 平台公告 |
| The Neuron (T05-S032) | daily | beginner | low | 宽口径 AI 日报，创作工具为 ambient awareness |
| Bakz T. Future / Multimodal | weekly | practitioner | medium | 多模态 AI substack + podcast |

### Podcast / YouTube / B站 频道 — 14 个

| Source | Cadence | Host | 投入产出 | One-liner |
|--------|---------|------|---------|-----------|
| Latent Space (T05-S005) | weekly | swyx | high | AI 工程长访谈，含 videogen 专题 |
| Nerdy Rodent (T05-S006) | 2-3x/week | Nerdy Rodent | high | 本地开源工作流（ComfyUI/Flux/WAN） |
| Scott Detweiler (T05-S007) | weekly | Scott Detweiler | high | Stability QA 本人，ComfyUI 系统课 |
| Pixaroma (T05-S008) | weekly | Pixaroma | high | ComfyUI from scratch 全课 |
| MattVidPro AI (T05-S009) | 2-3x/week | MattVidPro | medium | AI 视频/图像新工具横评 |
| Theoretically Media (T05-S010) | 2-3x/week | Tim Simmons | high | AI 视频创作实操（Runway/Kling/Sora） |
| ComfyUI Tutorial (T05-S012) | weekly | — | medium | ComfyUI 节点工作流教学 |
| 秋葉aaaki B站 (T05-S019) | weekly | 秋葉aaaki | high | 国内 SD/ComfyUI 整合包头部（zh-CN） |
| Matt Wolfe (T05-S011) | 2x/week | Matt Wolfe | medium | AI 工具发现频道（900K+ 订阅） |
| Curious Refuge (T05-S027) | weekly | Curious Refuge | high | AI 影视工作流 + 行业访谈 |
| Tao Prompts (T05-S028) | weekly | Tao Prompts | high | AI 影像 prompting（角色一致/运镜/i2v） |
| Aitrepreneur (T05-S034) | weekly | Aitrepreneur | medium | 本地 AI 安装/LoRA 训练/动画实操 |
| 硅谷101 (T05-S033) | weekly | 硅谷101 | medium | zh-CN 播客 AIGC 特辑（生成式视觉） |
| Runway 官方频道 (T05-S021) | per-release | Runway | medium | Gen 系列发布 + 创作教程 |

### Community / 平台 — 7 个

| Community | Platform | 规模 | One-liner |
|-----------|----------|------|-----------|
| Civitai (T05-S013) | Web | 巨型 | 最大 SD/Flux 模型 + LoRA 社区 |
| OpenArt (T05-S014) | Web | 大 | ComfyUI 工作流模板 + 比赛 |
| LiblibAI 哩布哩布 (T05-S015) | Web | 国内最大 | zh-CN AI 绘画模型社区 |
| 吐司 TusiArt (T05-S016) | Web | 大 | zh-CN 在线生图 + 模型分享 |
| r/StableDiffusion (T05-S017) | Reddit | 巨型 | 开源图像生成讨论中心 |
| r/comfyui (T05-S018) | Reddit | 大 | ComfyUI 工作流专属 |
| Midjourney Discord (T05-S023) | Discord | 1800万+ | MJ 创作主战场 + 社区挑战 |

### Conference / 活动 — 1 个

| Conference | 频率 | 下届 | One-liner |
|------------|------|------|-----------|
| Runway AI Film Festival / AIFF (T05-S022) | 年度 | 2026（第四届+） | 生成式 AI 影像创作旗舰活动，覆盖 Film/Design/New Media |

### Dataset / Benchmark — 2 个

| Dataset | URL | Maintainer | One-liner |
|---------|-----|------------|-----------|
| LAION (T05-S020) | https://laion.ai/ | LAION | 大规模图文训练集，有版权/伦理争议 |
| LAION-2B-en (T05-S030) | https://huggingface.co/datasets/laion/laion2B-en | LAION | diffusion 预训练基底，争议同上 |

---

## 详细卡片

### 📰 1. Black Forest Labs Blog (T05-S001)
- **Type**: 博客（模型方官方）
- **URL**: https://bfl.ai/blog/
- **Author**: Black Forest Labs（原 Stability 核心团队，FLUX 系列）
- **Cadence**: per-release（每次模型发布）
- **Last activity**: 2025-11（FLUX.2 发布）
- **Audience tier**: practitioner / senior
- **One-liner**: FLUX 系列（.1 dev/schnell、Kontext、.2）的一手发布 + 技术细节，创作侧顶级开源图像模型的源头。
- **投入产出比**: high — 发布稀但每篇都是该领域的事件级信息 (evidence: [T05-S001, T05-S003])
- **Paywall**: none
- **可信度**: high · **Decay risk**: low（机构级）

### 📰 2. Hugging Face Blog (T05-S002)
- **Type**: 博客（平台官方）
- **URL**: https://huggingface.co/blog
- **Cadence**: weekly+
- **Last activity**: 2026-06（持续）
- **Audience tier**: practitioner
- **One-liner**: diffusers 团队 + 社区开源生成模型动态，从模型卡到推理优化的一手枢纽。
- **投入产出比**: high (evidence: [T05-S002])
- **可信度**: high · **Decay risk**: low

### 🎙️ 3. Latent Space Podcast (T05-S005)
- **Type**: podcast + newsletter
- **URL**: https://www.latent.space/podcast
- **Host**: swyx (Shawn Wang) + Alessio
- **Cadence**: weekly
- **Last activity**: 2026-06
- **Audience tier**: senior
- **One-liner**: AI 工程长访谈（1h+），2025-2026 多期专攻 videogen「会成为 AI 前端」、Grok Imagine、视频世界模型，是创作侧技术趋势的 anchor。
- **投入产出比**: high — 嘉宾覆盖模型方 founders + 工程师 (evidence: [T05-S005])
- **可信度**: high · **Decay risk**: low

### 🎬 4. Nerdy Rodent (T05-S006)
- **Type**: YouTube 频道
- **URL**: https://www.youtube.com/c/NerdyRodent
- **Cadence**: 2-3x/week
- **Last activity**: 2026-06
- **Audience tier**: practitioner
- **One-liner**: 2020 起专注本地开源 AI 工作流（ComfyUI / Flux / Z-Image / Qwen / WAN Video），「AI Open Sourcery」头部，配 GitHub 实操资源。
- **投入产出比**: high (evidence: [T05-S006])
- **可信度**: high · **Decay risk**: medium（个人频道）

### 🎬 5. Scott Detweiler (T05-S007)
- **Type**: YouTube 频道
- **URL**: https://www.youtube.com/@sedetweiler
- **Cadence**: weekly
- **Last activity**: 2026-06
- **Audience tier**: beginner → practitioner
- **One-liner**: Stability AI 的 lead QA 本人 + 专业摄影/修图师，ComfyUI 系统课（5h+）头部，节点工作流权威讲解。
- **投入产出比**: high — 内部视角 + 系统课 (evidence: [T05-S007])
- **可信度**: high · **Decay risk**: medium

### 🎬 6. 秋葉aaaki B站 (T05-S019)
- **Type**: B站 频道（zh-CN）
- **URL**: https://space.bilibili.com/12566101（秋葉aaaki）
- **Cadence**: weekly
- **Last activity**: 2026-06
- **Audience tier**: beginner → practitioner
- **One-liner**: 国内 SD/ComfyUI 整合包（启动器）+ 教程事实标准，几乎所有中文 SD 用户的入门起点。
- **geographic_focus**: zh-CN
- **投入产出比**: high (evidence: [T05-S019])
- **可信度**: high · **Decay risk**: low（国内基础设施级）

### 🌐 7. Civitai (T05-S013)
- **Type**: community / 平台
- **URL**: https://civitai.com/
- **Cadence**: rolling（实时）
- **Audience tier**: mixed
- **One-liner**: 全球最大 SD/Flux checkpoint + LoRA + 工作流分享社区，模型生态风向标。
- **投入产出比**: high — 找模型/LoRA 必去 (evidence: [T05-S013])
- **可信度**: medium（UGC，质量参差）· **Decay risk**: low

### 🌐 8. r/StableDiffusion (T05-S017)
- **Type**: community
- **URL**: https://www.reddit.com/r/StableDiffusion/
- **Cadence**: rolling
- **Audience tier**: mixed
- **One-liner**: 开源图像生成最大讨论社区，新模型/新技术第一时间在此发酵。
- **投入产出比**: high — topic-heat 风向标 (evidence: [T05-S017])
- **可信度**: medium · **Decay risk**: low

### 🎬 9. Curious Refuge (T05-S026 / T05-S027)
- **Type**: YouTube 频道 + 教育社区
- **URL**: https://www.youtube.com/@CuriousRefuge · https://curiousrefuge.com/
- **Cadence**: weekly
- **Last activity**: 2026-06
- **Audience tier**: practitioner → senior
- **One-liner**: 「世界首个 AI filmmaking 课」运营方，频道做 AI 影视工作流 + 行业访谈，把 Runway/Kling/Veo 串成完整制作流，创作侧（视频）的方法论 anchor。
- **投入产出比**: high — 工作流而非单点工具 (evidence: [T05-S026, T05-S027])
- **Paywall**: 频道免费；深度课程付费（filmmaking/VFX 课，几百刀级，影视从业者 worth it）
- **可信度**: high · **Decay risk**: low

### 🎬 10. 即梦 / 可灵 官方（T05-S024 / T05-S025）
- **Type**: 平台官方（创作工具）
- **URL**: https://jimeng.jianying.com/ （即梦，字节）· https://app.klingai.com/ （可灵，快手）
- **Cadence**: per-release
- **Audience tier**: mixed
- **geographic_focus**: zh-CN（均已出海，可灵 Kling 全球版）
- **One-liner**: 国产 AI 视频双雄官方入口，新模型/新功能一手；创作侧中文用户的主力视频工具。
- **投入产出比**: high — 工具本体即信源 (evidence: [T05-S024, T05-S025])
- **可信度**: high（vendor 一手，但能力宣称需 ≥2 source 交叉）· **Decay risk**: low

### 🎪 11. Runway AI Film Festival / AIFF (T05-S022)
- **Type**: conference / 年度活动
- **URL**: https://aif.runwayml.com/
- **Cadence**: 年度（2022 起，2026 为第四届+）
- **Last edition**: 2026 · **Next edition**: ~年度（间隔 < 12 月，retain 优先级高）
- **One-liner**: 生成式 AI 影像创作旗舰活动，从 AI 短片扩到 Film/Design/New Media/Fashion，是创作侧（视频）作品风向 + 头部创作者聚集地。
- **投入产出比**: medium — 年度信号但密度高 (evidence: [T05-S022])
- **可信度**: high · **Decay risk**: low

### 🗄️ 12. LAION (T05-S020 / T05-S030)
- **Type**: dataset
- **URL**: https://laion.ai/ · https://huggingface.co/datasets/laion/laion2B-en
- **Maintainer**: LAION e.V.
- **Last update**: 数据集稳定，维护偶发
- **One-liner**: LAION-5B/2B 是 SD 等开源 diffusion 模型的训练基底；**争议**：版权 + 内容安全（曾因不良内容下架重整），创作者需知其伦理边界。
- **投入产出比**: low（非日常跟，但理解模型来源必知）(evidence: [T05-S020, T05-S030])
- **可信度**: high · **Decay risk**: low

---

## Phase 2 提炼提示

**top 3 sources（资深人订阅最多 — 进 master skill「想跟最新动态」highlights）**:
- 图像侧：Civitai (T05-S013) — 模型/LoRA 生态枢纽 + r/StableDiffusion (T05-S017) topic-heat
- 工作流侧：Scott Detweiler / Nerdy Rodent / Pixaroma (ComfyUI 三巨头) + ComfyUI 官方博客 (T05-S031)
- 视频侧 + 趋势：Curious Refuge (T05-S027) + Latent Space (T05-S005)
- zh-CN：秋葉aaaki B站 (T05-S019) + LiblibAI (T05-S015)

**新 figures 候选（喂 Wave 2 Track 01 — 头部创作者名单）**:
- **swyx / Shawn Wang** (Latent Space) — AI engineering 视角
- **Scott Detweiler** — Stability QA 本人 + ComfyUI 教学权威
- **Nerdy Rodent** — 本地开源工作流头部
- **秋葉aaaki** — 国内 SD/ComfyUI 整合包事实标准（zh-CN）
- **Pixaroma** — ComfyUI 系统课
- **Curious Refuge 团队** — AI 影视方法论
- **Tao Prompts** — AI 影像 prompting（角色一致性/运镜）
- **Matt Wolfe** — AI 工具发现（创作者经济）
- **Bakz T. Future** — 多模态 AI
- **Aitrepreneur** — LoRA 训练/动画实操

**新 tools 候选（喂 Wave 2 Track 02）**:
- 图像：FLUX.1/.2 (BFL)、SDXL/SD3 (Stability)、Qwen-Image、Seedream 4.0、Midjourney
- 视频：可灵 Kling、即梦 Jimeng/Dreamina、Runway Gen-4、Sora 2（注：2026-04 standalone 已停）、WAN Video (Wan 2.1/2.2)、LTX Video、Mochi 1、Veo 3.1
- 工作流引擎：ComfyUI、SwarmUI、A1111/Forge
- 社区/平台：Civitai、OpenArt、LiblibAI、TusiArt、Hugging Face

**「最近话题热度」候选信号**:
- 国产视频模型崛起（可灵 / 即梦）vs Sora（Sora standalone 2026-04 停） — sources: 多 (theankler/bloomberg 类 + 创作者横评)
- FLUX.2 (2025-11) 开源 32B 图像编辑模型
- WAN 2.x 本地视频生成进 ComfyUI
- topic-heat: incomplete — sources listed, content NOT deep-crawled（默认行为）。要高置信需爬具体 episode/issue title。

**冷僻 / 信号薄弱**:
- newsletter ✅ (8) · podcast/频道 ✅ (14) · conference ⚠️ (仅 1，AIFF；本行业大会少，AI 艺术多为社区比赛/线上活动而非传统会议) · community ✅ (7) · dataset ✅ (2)
- 有效 endorsement: 多数靠 cross_source / community_consensus，figure_long 背书偏弱（创作侧 figures 互推不如学术圈正式）
- **诚实边界建议**：conference 维度薄（生成式视觉创作圈缺机构级年度大会，AIFF 是少数）；zh-CN 频道 deep-fluency 期望 agent 可能不达标，用户自评。
