# Track 01 — Figures: AIGC 创作工作流 / AIGC Creative Workflow

> locale = global · focus = operational + technical
> Phase 1 Track 01 (Figures). 行业 = 生成式 AI 视觉创作（图像 + 视频，创作侧）。
> retained 目标 10-15。本文件抗中断分批 Write，下方为第一版（持续 Edit 增补）。

## Source Manifest

| source_id | url | bucket | last_checked | author/host | one-line note |
|-----------|-----|--------|--------------|-------------|---------------|
| T01-S001 | https://stratechery.com/2022/an-interview-with-midjourney-founder-david-holz-about-generative-ai-vr-and-silicon-valley/ | verified_primary | 2026-06-22 | Ben Thompson | David Holz 长访谈, Midjourney 哲学起点 |
| T01-S002 | https://blakeir.com/an-interview-with-david-holz-ceo-of-ai-image-generator-midjourney-its-an-engine-for-the-imagination | secondary | 2026-06-22 | Blake Robbins (转载 Forbes 访谈) | David Holz 访谈本人原话, 第三方博客转载托管 (诚实留 secondary 不洗 host) |
| T01-S003 | https://x.com/robrombach | reference | 2026-06-22 | Robin Rombach | BFL/Flux 创始人本人 X |
| T01-S004 | https://ee.stanford.edu/event/10-16-2024/latent-diffusion-flux-and-beyond-scaling-efficient-content-creation | verified_primary | 2026-06-22 | Stanford EE | Rombach 本人 talk: LDM→FLUX |
| T01-S005 | https://en.wikipedia.org/wiki/Flux_(text-to-image_model) | secondary | 2026-06-22 | — | FLUX/BFL 事实核对 |
| T01-S006 | https://github.com/lllyasviel | secondary | 2026-06-22 | Lvmin Zhang | 张吕敏 GitHub org 总览 |
| T01-S007 | https://openaccess.thecvf.com/content/ICCV2023/papers/Zhang_Adding_Conditional_Control_to_Text-to-Image_Diffusion_Models_ICCV_2023_paper.pdf | verified_primary | 2026-06-22 | Lvmin Zhang et al | ControlNet 论文 (ICCV2023 best paper) |
| T01-S008 | https://lllyasviel.github.io/lvmin_zhang/ | verified_primary | 2026-06-22 | Lvmin Zhang | 本人主页 |
| T01-S009 | https://github.com/comfyanonymous/ComfyUI | verified_primary | 2026-06-22 | comfyanonymous | ComfyUI 项目根, README 设计哲学 |
| T01-S010 | https://en.wikipedia.org/wiki/ComfyUI | secondary | 2026-06-22 | — | ComfyUI 事实/时间线核对 |
| T01-S011 | https://thesequence.substack.com/p/the-sequence-chat-emad-mostaque-stability | verified_primary | 2026-06-22 | TheSequence | Emad Mostaque 长访谈 open AI |
| T01-S012 | https://www.bilibili.com/video/BV1iM4y1y7oA/ | verified_primary | 2026-06-22 | 秋葉aaaki | SD 整合包教程, 本人 B站 |
| T01-S013 | https://www.youtube.com/c/scottdetweiler | verified_primary | 2026-06-22 | Scott Detweiler | Stability QA, ComfyUI 教学频道 |
| T01-S014 | https://curiousrefuge.com/ai-filmmaking | surrogate_primary | 2026-06-22 | Curious Refuge | Caleb Ward 自家公司 own site (own publication) — AI 影视课程 originator 页 |
| T01-S015 | https://www.hollywoodreporter.com/movies/movie-features/curious-refuge-ai-film-school-hollywood-1236546505/ | secondary | 2026-06-22 | THR | Caleb Ward / Curious Refuge 深度报道 |
| T01-S016 | https://news.artnet.com/art-world/artists-vs-stability-ai-lawsuit-moves-ahead-2524849 | secondary | 2026-06-22 | Artnet | Karla Ortiz 等 vs Stability 诉讼进展 |
| T01-S017 | https://www.buzzfeednews.com/article/pranavdixit/ai-art-generators-lawsuit-stable-diffusion-midjourney | secondary | 2026-06-22 | BuzzFeed News | 三位艺术家原话(版权批判反面视角) |
| T01-S018 | https://en.wikipedia.org/wiki/Wan_(text-to-video_model) | secondary | 2026-06-22 | — | 通义万相 Wan 事实核对 |
| T01-S019 | https://www.latent.space/about | verified_primary | 2026-06-22 | swyx & Alessio | Latent Space 定位/AI Engineer |
| T01-S020 | https://redmonk.com/blog/2025/07/23/shawn-swyx-wang-ai-engineer/ | secondary | 2026-06-22 | RedMonk | swyx 谈 AI Engineer 角色 |
| T01-S021 | https://www.infoq.cn/article/1HtaG3ortUO0hFb6iGkH | secondary | 2026-06-22 | InfoQ 中国 | 可灵团队/万鹏飞 深度访谈 |
| T01-S022 | https://www.ustcbj.org.cn/default.php/content/1214/ | secondary | 2026-06-22 | 中科大北京校友会 | 万鹏飞 可灵 talk 纪要 |
| T01-S023 | https://github.com/lllyasviel/Fooocus | verified_primary | 2026-06-22 | Lvmin Zhang | Fooocus README 设计哲学(逐字) |
| T01-S024 | https://www.youtube.com/@bilawalsidhu | verified_primary | 2026-06-22 | Bilawal Sidhu | AI 创作者本人 YouTube (1.5M+) |
| T01-S025 | https://x.com/bilawalsidhu/status/1808889955956957606 | reference | 2026-06-22 | Bilawal Sidhu | "tool to tool 破坏 flow"原话推文 |
| T01-S026 | https://bilawal.ai/ | secondary | 2026-06-22 | Bilawal Sidhu | 本人主页/bio |
| T01-S027 | https://www.youtube.com/c/NerdyRodent/videos | verified_primary | 2026-06-22 | Nerdy Rodent | 开源 AI 艺术教学频道 (2020起) |

---

## 总览（按行业影响力排序）

| # | 姓名 | 核心身份 | 一句话贡献 | 值得读/听/看 | 来源数 | 可信度 |
|---|------|---------|----------|------------|-------|-------|
| 1 | David Holz | Midjourney 创始人 | 把文生图做成「想象力引擎」，定义闭源高审美图像生成范式 | 📖🎙️ | 3 | high |
| 2 | Robin Rombach | Black Forest Labs 联合创始人 (前 Stability) | Latent Diffusion / Stable Diffusion 一作 → FLUX，开源底座的技术心脏 | 📖🎬 | 3 | high |
| 3 | Lvmin Zhang (张吕敏 / lllyasviel) | Stanford PhD，ControlNet/Fooocus/IC-Light 作者 | 把「可控生成」从论文推到全民工具，开源控制力之王 | 📖🎬 | 3 | high |
| 4 | comfyanonymous | ComfyUI 作者，Comfy Org | 节点式工作流范式奠基者，专业向 AIGC pipeline 标准 | 📖🎬 | 2 | medium |
| 5 | Emad Mostaque | 前 Stability AI CEO | 把「生成式 AI 是公共品」开源叙事推向主流（已离场，争议大） | 📖🎙️ | 3 | high |
| 6 | 万鹏飞 (Wan Pengfei) | 快手可灵 (Kling) 负责人 | 国产视频生成头部团队领军，DiT 视频范式落地 | 📖🎙️ | 3 | medium |
| 7 | swyx (Shawn Wang) | Latent Space 主理人 | 提出/布道「AI Engineer」，连接模型与创作工程 | 📖🎙️ | 3 | high |
| 8 | Scott Detweiler | 前 Stability QA，YouTube 教育者 | ComfyUI 教学头部，把工作流知识普及化 | 🎬 | 1 | medium |
| 9 | Caleb Ward | Curious Refuge 创始人 | 全球首个 AI 影视教育，AI filmmaking 方法论布道者 | 📖🎙️🎬 | 2 | medium |
| 10 | 秋葉aaaki | B站 UP 主，SD/ComfyUI 整合包作者 | 中文圈 SD 普及第一人，降低本地部署门槛 | 🎬 | 1 | medium |
| 11 | Bilawal Sidhu | 前 Google XR，AI 创作者/创意技术专家 (1.5M+) | 经典 VFX 视角实操 AI 视频，揭「slot machine / 工具拼盘」之痛 | 🎬📖🎙️ | 3 | medium-high |
| 12 | Karla Ortiz | 概念艺术家，反 AI 训练数据维权者 | 版权批判反面视角，艺术家维权诉讼核心原告 | 📖 | 2 | medium |
| 13 | AUTOMATIC1111 | SD WebUI 作者 | 早期最普及的 SD 图形界面，开源生态基建 | 🎬 | (待补) | low |

> 注: 国产视频工具团队（即梦/字节 Seed、通义万相 Wan）以团队形式在卡片#6 与 Phase 2 中覆盖，个人 figure 一手原话薄故未单独成卡。下方卡片持续 Edit 增补。

---

## 卡片

### 1. David Holz

- **One-liner**: Midjourney 创始人，把文生图重新定义为「人类想象力的引擎」而非「会创作的机器」，开创高审美闭源图像生成的产品范式。(evidence: [T01-S001, T01-S002])
- **核心身份**: Midjourney 创始人兼 CEO（此前 Leap Motion 联合创始人）。Midjourney 至今坚持小团队、无 VC、Discord/网页起家。
- **代表作品**: Midjourney（v1→v7，niji 动漫模型）；Midjourney「office hours」社区治理模式。
- **值得读 / 听 / 看的 3 件事**:
  - 📖 Midjourney 创始访谈（imagination vs machine creativity）: https://blakeir.com/an-interview-with-david-holz-ceo-of-ai-image-generator-midjourney-its-an-engine-for-the-imagination (T01-S002)
  - 🎙️ Stratechery 长访谈 (Ben Thompson): https://stratechery.com/2022/an-interview-with-midjourney-founder-david-holz-about-generative-ai-vr-and-silicon-valley/ (T01-S001)
  - 🎬 ⚠️ Midjourney office hours 多为社区内 Discord 语音，无稳定公开长视频链接
- **核心思想关键词**: 想象力引擎(engine for imagination) / 扩展人类而非取代人类 / 水的比喻(AI 像水，可危险可承载) / 小团队反 VC / 审美优先
- **voice_samples**:
  - 客户/大众解释样本: 「We like to say we're trying to expand the imaginative powers of the human species. The goal is to make humans more imaginative, not make imaginative machines, which I think is an important distinction.」(source: T01-S001/S002, 原话)
  - 行业争议样本（AI vs 艺术家）: 「Water is dangerous, yes, but you can also swim in it, you can make boats, you can dam it and make electricity. Water is dangerous, but it's also the lifeblood of civilization.」(source: T01-S002, 原话) —— 用水比喻回应「AI 危险论」
  - 大众样本: 「We see this technology as an engine for the imagination. So it's a very positive and humanistic thing.」(source: T01-S002, 原话)
  - 补充（产品哲学）: 「Cars are faster than humans, but that doesn't mean we stopped walking.」(source: T01-S002, 原话) —— 工具增强而非替代
- **sub_skill_candidate**: `true` — 有长访谈 + 自洽哲学（想象力优先/反 VC/审美治理）+ 行业影响力前 3 + 与创作 focus 高度对齐。
- **dual_role**: "founder + thinker"
- **最近 12 个月动态**: Midjourney 推进 v7 与视频生成（2025 进入图生视频赛道），仍坚持小团队与网页/Discord 产品形态；持续以 office hours 形式做社区治理。(evidence: [T01-S001])
- **争议 / 批评**: Midjourney 是 Andersen v. Stability/Midjourney 版权集体诉讼被告之一；训练数据来源不透明被艺术家社区批评；闭源、不发论文，与开源阵营价值观对立。(evidence: [T01-S016, T01-S017])
- **来源**:
  - [Primary] Stratechery interview, 2022, collected 2026-06-22: T01-S001
  - [Primary] "Engine for the imagination" interview, collected 2026-06-22: T01-S002
  - [Reference] Andersen v. Stability/Midjourney 诉讼报道: T01-S016
- **可信度自评**: high — 多个长访谈，原话充足，哲学清晰。

### 2. Robin Rombach

- **One-liner**: Latent Diffusion / Stable Diffusion 论文一作，离开 Stability 创办 Black Forest Labs 推出 FLUX，是开源图像生成「效率优先」路线的技术心脏。(evidence: [T01-S004, T01-S005])
- **核心身份**: Black Forest Labs (BFL) 联合创始人兼 CEO（2024 创立）；此前 Stability AI 核心研究员；师从 LMU Munich Björn Ommer。
- **代表作品**: VQGAN、Latent Diffusion Models (LDM)、Stable Diffusion (1.x/2.x/SD3)、FLUX.1 系列、FLUX.1 Kontext（in-context 编辑）。
- **值得读 / 听 / 看的 3 件事**:
  - 📖 "High-Resolution Image Synthesis with Latent Diffusion Models" (CVPR2022, LDM 原论文)
  - 🎬 Stanford EE talk: "From Latent Diffusion to FLUX and Beyond" (2024-10-16): https://ee.stanford.edu/event/10-16-2024/latent-diffusion-flux-and-beyond-scaling-efficient-content-creation (T01-S004)
  - 🎙️ ⚠️ 本人 X @robrombach 高频技术发声，但缺单篇 30min+ 中文/英文长 podcast（待补）
- **核心思想关键词**: latent space 效率 / 把生成压到普通人能跑的算力 / flow matching / 开源 vs 商业平衡 / scaling 内容创作
- **voice_samples**:
  - 同业技术样本: ⚠️ 暂未找到 ≥30 字直接原话片段（X 短帖为主，Stanford talk 暂无 transcript；待二次抓取 talk 字幕补全）
  - 行业立场样本: ⚠️ 暂未找到 ≥30 字直接原话片段（BFL 博客多为团队署名，非个人第一人称长段）
- **sub_skill_candidate**: `false` — 影响力极高，但个人长访谈/原话材料目前薄，思想以论文+产品体现而非个人布道；可作为 canon 作者交叉。若后续抓到 Stanford talk transcript 可升级为 borderline true。
- **dual_role**: "academic + engineering"
- **最近 12 个月动态**: BFL 持续迭代 FLUX（FLUX.1 Kontext 主打 in-context 编辑），与多家平台合作集成；定位「开放权重 + 商业 API」混合模式。(evidence: [T01-S005])
- **争议 / 批评**: SD 训练数据（LAION）是版权诉讼核心；BFL 的「open weight」是否真开源、商业许可限制被社区讨论。(evidence: [T01-S005, T01-S016])
- **来源**:
  - [Primary] Stanford EE talk page, collected 2026-06-22: T01-S004
  - [Primary] X @robrombach: T01-S003
  - [Reference] FLUX Wikipedia 事实核对: T01-S005
- **可信度自评**: medium — 事实与影响力 high，但 voice_samples 暂缺直接原话，降级 medium。

### 3. Lvmin Zhang (张吕敏 / lllyasviel)

- **One-liner**: ControlNet 作者（ICCV2023 best paper），又写出 Fooocus、IC-Light、Style2Paints、Forge，是把「可控生成」从论文推到全民工具的开源控制力之王。(evidence: [T01-S006, T01-S007])
- **核心身份**: Stanford CS PhD（导师 Maneesh Agrawala）；GitHub handle lllyasviel；中文圈称「张吕敏 / 控制网作者」。
- **代表作品**: ControlNet（条件控制扩散）、Fooocus（极简文生图）、IC-Light（重打光）、Forge（WebUI 性能重构）、LayerDiffuse、FramePack（视频）。
- **值得读 / 听 / 看的 3 件事**:
  - 📖 "Adding Conditional Control to Text-to-Image Diffusion Models" (ControlNet, ICCV2023): https://openaccess.thecvf.com/content/ICCV2023/papers/Zhang_Adding_Conditional_Control_to_Text-to-Image_Diffusion_Models_ICCV_2023_paper.pdf (T01-S007)
  - 🎬 lllyasviel GitHub（Fooocus/IC-Light/FramePack README，含设计哲学）: https://github.com/lllyasviel (T01-S006)
  - 🎙️ ⚠️ 极少公开长访谈/podcast，主要通过 GitHub README + issue 与 arXiv 发声
- **核心思想关键词**: 可控生成(conditional control) / 「offload 给非专家」(Fooocus 隐藏参数) / 把研究直接做成能用的工具 / 解耦控制信号 / 重打光与图层
- **voice_samples**:
  - 新手/产品设计样本（Fooocus README 逐字）: 「similar to many online image generators like Midjourney, the manual tweaking is not needed, and users only need to focus on the prompts and images」(source: T01-S023, 原话) —— 把「隐藏参数、只管 prompt 和图」做成显式设计目标
  - 产品设计样本（README 逐字）: 「Fooocus has also simplified the installation: between pressing 'download' and generating the first image, the number of needed mouse clicks is strictly limited to less than 3」(source: T01-S023, 原话) —— 极致降低门槛的工程化承诺
  - 学术样本: ⚠️ 论文写作为团队学术语体；本人口语化长访谈原话暂未找到 ≥30 字片段（发声集中于 GitHub README/issue）
- **sub_skill_candidate**: `true` — 影响力前 3，工具体系自洽（控制 / 极简 / 重打光一脉相承），与 operational+technical focus 高度对齐；唯一短板是缺长口语访谈，建议从 GitHub issue/README 提炼其设计哲学原话。
- **dual_role**: "academic + engineering"
- **最近 12 个月动态**: 2024-2025 推出 IC-Light（v2）、LayerDiffuse、FramePack（消费级显存跑长视频生成），延续「让普通显卡跑得动 + 可控」主线。(evidence: [T01-S006])
- **争议 / 批评**: 工具迭代极快但文档/维护连续性被部分用户质疑（项目多、深维护少）；学术 vs 产品身份切换。
- **来源**:
  - [Primary] ControlNet 论文 PDF, collected 2026-06-22: T01-S007
  - [Primary] lllyasviel GitHub org: T01-S006
  - [Primary] Fooocus README（逐字设计哲学）: T01-S023
  - [Primary] 本人主页 lvmin_zhang: T01-S008
- **可信度自评**: high — 一手论文/代码/README 充足，现已有 ≥2 段逐字 voice（README 第一人称设计目标）。

### 4. comfyanonymous

- **One-liner**: ComfyUI 作者，用节点式（node-based）有向图把扩散生成 pipeline 全程可见、可改、可复现，奠定专业向 AIGC 工作流范式。(evidence: [T01-S009, T01-S010])
- **核心身份**: 公开 handle comfyanonymous（不挖真实身份）；ComfyUI 创建者；2024-06 起成立 Comfy Org，此前与 Stability 有关联后结束。
- **代表作品**: ComfyUI（2023-01 GitHub 发布）、ComfyUI_examples（工作流范例库）。
- **值得读 / 听 / 看的 3 件事**:
  - 📖 ComfyUI 项目 README + examples（设计哲学：把生成做成显式图）: https://github.com/comfyanonymous/ComfyUI (T01-S009)
  - 🎬 ComfyUI_examples 工作流图: https://comfyanonymous.github.io/ComfyUI_examples/
  - 🎙️ ⚠️ 本人极少露面访谈（匿名）；行业讨论多为第三方（如 TBPN）
- **核心思想关键词**: 节点式工作流 / 反黑箱（一切步骤可见）/ 可复现性 / 模块化 / 后端 + 图接口
- **voice_samples**:
  - 产品/项目语体样本（ComfyUI README 逐字，作者署名项目）: 「Nodes/graph/flowchart interface to experiment and create complex Stable Diffusion workflows without needing to code anything.」(source: T01-S009, 原话/项目语体) —— 节点式 + 无需写代码的核心主张
  - 项目定位样本（逐字）: 「The most powerful and modular AI engine for content creation.」(source: T01-S009, 原话/项目语体)
  - 个人口语样本: ⚠️ 暂未找到 ≥30 字本人第一人称口语长原话（匿名，发声集中于 GitHub commit/issue）
- **sub_skill_candidate**: `false` — 工具范式影响极大，但以产品/代码而非个人思想布道，且匿名缺长访谈。其「节点式 = 可复现工作流」理念会进 Phase 2 心智模型，但不独立成 figure sub-skill。
- **最近 12 个月动态**: Comfy Org 推进 ComfyUI Manager、API 节点、桌面版与生态商业化；成为视频生成（Wan/可灵/Hunyuan 等）社区工作流默认枢纽。(evidence: [T01-S010])
- **争议 / 批评**: 学习曲线陡、对新手不友好（vs Fooocus/A1111 简单路线）；治理/商业化方向与「纯开源」期待间张力。
- **来源**:
  - [Primary] ComfyUI GitHub, collected 2026-06-22: T01-S009
  - [Reference] ComfyUI Wikipedia 时间线: T01-S010
- **可信度自评**: medium — 事实清晰，但匿名导致 voice 与个人观点材料薄。

### 5. Emad Mostaque

- **One-liner**: 前 Stability AI CEO，把「生成式 AI 是公共品 / 应开源」的叙事推向主流，但 2024 辞任后争议缠身。(evidence: [T01-S011])
- **核心身份**: Stability AI 联合创始人、前 CEO（2024-03 辞任）；后转向 decentralized AI（SAGE / Schelling AI）。
- **代表作品**: 推动 Stable Diffusion 发布与开源叙事；著作 *The Last Economy*（Intelligent Economics）。
- **值得读 / 听 / 看的 3 件事**:
  - 📖🎙️ TheSequence Chat: open & decentralized AI: https://thesequence.substack.com/p/the-sequence-chat-emad-mostaque-stability (T01-S011)
  - 🎙️ OpenUK fireside chat 2024
  - 🎬 ⚠️ 多为会议演讲片段
- **核心思想关键词**: AI 即公共品 / 开源民主化 / 个人 AI / decentralized / 智能经济（abundance vs scarcity）
- **voice_samples**:
  - 行业立场样本: AI 应像「道路、电力、教育」一样作为公共基础设施被个人拥有而非向公司租用（SAGE 主张）—— ⚠️ 此为转述，需核对 TheSequence 原文逐字。(source: T01-S011, 转述)
  - ⚠️ 直接 ≥30 字逐字原话待二次抓取 TheSequence transcript 补全
- **sub_skill_candidate**: `false` — 已离开核心岗位，且偏宏大叙事而非 operational 创作工作流；保留作「开源叙事 founder」单列。
- **dual_role**: "founder + evangelist"
- **最近 12 个月动态**: 推 SAGE（Sovereign AI Governance Engine）与 decentralized AI；出版 *The Last Economy*；不再主导图像生成工具线。(evidence: [T01-S011])
- **争议 / 批评**: 离任前被曝简历/陈述夸大、财务与管理质疑；被批宏大愿景多于落地。
- **来源**:
  - [Primary] TheSequence Chat, collected 2026-06-22: T01-S011
  - [Reference] 行业报道（辞任/争议）
  - [Reference] OpenUK fireside
- **可信度自评**: medium — 叙事影响 high，但已离场 + 个人争议，operational 价值有限。

### 6. 万鹏飞 (Wan Pengfei)

- **One-liner**: 快手可灵 (Kling) 负责人，带 ~10 人核心团队 3 个月做出「中国版 Sora」，国产视频生成头部团队领军人。(evidence: [T01-S021, T01-S022])
- **核心身份**: 快手视觉生成与互动中心负责人；中科大本科、港科大博士；曾任美图 MTlab 主任，2020 加入快手。
- **代表作品**: 可灵 (Kling) 视频生成大模型（DiT 架构）、Kling-Avatar 数字人。
- **值得读 / 听 / 看的 3 件事**:
  - 📖 InfoQ 中国深度访谈（可灵一年迭代 30 次）: https://www.infoq.cn/article/1HtaG3ortUO0hFb6iGkH (T01-S021)
  - 🎙️ 中科大北京校友会 AI 沙龙 talk 纪要: https://www.ustcbj.org.cn/default.php/content/1214/ (T01-S022)
  - 🎬 ⚠️ WAIC 等发布会片段为主
- **核心思想关键词**: DiT 视频范式 / 「人人能用 AI 讲好故事」/ 可控性 (controllability) / 快速迭代 / 物理规律理解
- **voice_samples**:
  - 行业愿景样本: 可灵团队主张「让人人都能用 AI 讲出好故事」—— ⚠️ 转述，需核对 InfoQ 原文逐字。(source: T01-S021, 转述)
  - ⚠️ ≥30 字本人直接原话待补（访谈多为记者转述口吻）
- **sub_skill_candidate**: `false` — 国产视频代表，但个人长访谈原话薄、偏团队/产品视角；作为「国产视频工具团队」代表保留。
- **dual_role**: "engineering + product lead"
- **最近 12 个月动态**: 可灵持续迭代（2.x），推出网页版、首尾帧控制、数字人 Kling-Avatar，海外 KlingAI 扩张。(evidence: [T01-S021])
- **争议 / 批评**: 闭源、训练数据不透明；与字节即梦/Sora 的同质竞争与营销味。
- **来源**:
  - [Secondary] InfoQ 访谈, collected 2026-06-22: T01-S021
  - [Secondary] 校友会 talk 纪要: T01-S022
  - [Reference] 行业报道
- **可信度自评**: medium — 国产视频代表性强，但一手原话与英文材料薄。

### 7. swyx (Shawn Wang)

- **One-liner**: Latent Space 主理人，提出并布道「AI Engineer」这一新角色，连接基础模型与上层创作/产品工程。(evidence: [T01-S019, T01-S020])
- **核心身份**: Latent Space newsletter/podcast 主理人（2022 起）；AI Engineer 会议发起者；前 Temporal/Airbyte DevRel。
- **代表作品**: "The Rise of the AI Engineer"（文章）、Latent Space podcast、AI Engineer Summit/World's Fair。
- **值得读 / 听 / 看的 3 件事**:
  - 📖 Latent Space about / "Rise of AI Engineer": https://www.latent.space/about (T01-S019)
  - 🎙️ Latent Space podcast（图像/视频生成嘉宾长访谈枢纽）
  - 🎬 RedMonk conversation: AI Engineer 角色: https://redmonk.com/blog/2025/07/23/shawn-swyx-wang-ai-engineer/ (T01-S020)
- **核心思想关键词**: AI Engineer（介于 ML 研究与软件工程之间）/ 模型即原料、工程即价值 / 责任在人不在模型 / 信息聚合与品味
- **voice_samples**:
  - 同业讨论样本: swyx 强调 AI Engineer「不只是 vibe，而是产出的效率与质量；如果你产出软件并造成坏后果，负责的是你，不是模型」—— (source: T01-S020, 转述，需核对 RedMonk 原文逐字)
  - ⚠️ ≥30 字逐字原话待从 latent.space 文章/RedMonk transcript 抓取核对
- **sub_skill_candidate**: `false`（对视觉创作而言）— 影响力高但偏 AI 工程通识/信息源角色，非视觉创作 operational 核心；作为「连接者/信息枢纽」保留并交叉 Track 05。
- **dual_role**: "evangelist + community builder"
- **最近 12 个月动态**: 持续运营 Latent Space 与 AI Engineer 会议，覆盖 agent/生成式创作前沿；2026 发文谈「scaling without slop」（质量与规模）。(evidence: [T01-S019])
- **争议 / 批评**: 「AI Engineer」是否真是新职业、还是营销标签，业内有分歧。
- **来源**:
  - [Primary] Latent Space about: T01-S019
  - [Secondary] RedMonk conversation: T01-S020
  - [Reference] Latent Space podcast 平台页
- **可信度自评**: high（事实/影响力），voice 待补。

### 8. Scott Detweiler

- **One-liner**: 前 Stability AI 首席 QA + 职业摄影师，YouTube 上 ComfyUI 教学头部，把专业工作流知识普及给创作者。(evidence: [T01-S013])
- **核心身份**: 前 Stability.ai Lead QA；职业摄影/修图师（威斯康星）；YouTube/Twitter @sedetweiler。
- **代表作品**: ComfyUI 教学系列（"Let's Figure it Out!"）、SDXL 内部工作流分享。
- **值得读 / 听 / 看的 3 件事**:
  - 🎬 Scott Detweiler YouTube（ComfyUI 全套教学）: https://www.youtube.com/c/scottdetweiler (T01-S013)
  - 🎬 "ComfyUI: Let's Figure it Out!" 系列
  - 📖 ⚠️ 无长文/论文，材料以视频为主
- **核心思想关键词**: 工作流可解释 / 摄影/修图审美迁移到 AI / 内部最佳实践公开 / refiner/upscale pipeline
- **voice_samples**:
  - 客户/新手解释样本: ⚠️ 暂未找到 ≥30 字直接原话片段（视频口播，需抓 YouTube 字幕逐字核对）
- **sub_skill_candidate**: `false` — 优秀教育者，但思想体系偏「最佳实践集合」而非独立框架；并入工作流/教学 playbook。
- **最近 12 个月动态**: 持续更新 ComfyUI 视频/视频生成工作流教学（含新模型集成）。(evidence: [T01-S013])
- **争议 / 批评**: 无显著争议；内容偏入门-中级，深度由观众自评。
- **来源**:
  - [Primary] YouTube 频道, collected 2026-06-22: T01-S013
  - [Reference] Twitter @sedetweiler
  - [Reference] ⚠️ 需补第 3 条独立来源
- **可信度自评**: medium — 单一手来源，待补来源与逐字 voice。

### 9. Caleb Ward

- **One-liner**: Curious Refuge 创始人，做出全球首个 AI 影视课程，是 AI filmmaking 方法论的主要布道者。(evidence: [T01-S014, T01-S015])
- **核心身份**: Curious Refuge 联合创始人兼 CEO（后被 AI studio Promise 收购）；十余年影视后期/VFX 背景。
- **代表作品**: Curious Refuge AI Filmmaking 课程；病毒视频（"Wes Anderson × Star Wars/LOTR" 系列、Barbenheimer 预告）。
- **值得读 / 听 / 看的 3 件事**:
  - 📖 THR 深度报道（Hollywood 应回炉影校）: https://www.hollywoodreporter.com/movies/movie-features/curious-refuge-ai-film-school-hollywood-1236546505/ (T01-S015)
  - 🎙️ Brand Bots podcast: AI filmmaking & advertising
  - 🎬 Curious Refuge AI Filmmaking 课程页 + 案例片: https://curiousrefuge.com/ai-filmmaking (T01-S014)
- **核心思想关键词**: AI 影视民主化 / 故事优先于工具 / prompt→animation→VFX 全流程 / 把好莱坞工艺迁移到 AI / 社区
- **voice_samples**:
  - 行业立场样本: ⚠️ 暂未找到 ≥30 字本人直接原话（THR/podcast 待抓逐字）
- **sub_skill_candidate**: `true`（borderline）— 与「视频/影视创作工作流」focus 高度对齐，有 podcast/课程长材料；若抓到其方法论原话可独立。暂标 true 待 Phase 3 评估。
- **dual_role**: "founder + educator"
- **最近 12 个月动态**: Curious Refuge 被 Promise 收购；推出 Advanced AI Filmmaking 2.0；持续用最新视频模型（可灵/Runway/Veo 等）做案例。(evidence: [T01-S015])
- **争议 / 批评**: 「AI 取代影视工作岗位」担忧的靶心之一；课程商业化与「速成」批评。
- **来源**:
  - [Primary] Curious Refuge 课程页: T01-S014
  - [Secondary] THR 报道: T01-S015
  - [Reference] Brand Bots podcast 页
- **可信度自评**: medium — 事实充足，voice 逐字待补。

### 10. 秋葉aaaki

- **One-liner**: B站头部 UP 主，SD/ComfyUI 整合包与训练工具作者，中文圈降低本地 AI 绘画部署门槛第一人。(evidence: [T01-S012])
- **核心身份**: B站 UP 主（自述「做些有意思的东西」）；SD WebUI 整合包、训练器、ComfyUI 整合包维护者。
- **代表作品**: Stable Diffusion 整合包（解压即用）、SD 训练器、ComfyUI 整合包、显存优化方案。
- **值得读 / 听 / 看的 3 件事**:
  - 🎬 SD 整合包发布/教程: https://www.bilibili.com/video/BV1iM4y1y7oA/ (T01-S012)
  - 🎬 B站 训练/汉化教程系列
  - 📖 ⚠️ 无长文，材料以 B站视频为主
- **核心思想关键词**: 解压即用 / 降低门槛 / 显存优化（防爆显存）/ 汉化普及 / 工具整合
- **voice_samples**:
  - 大众/新手解释样本: ⚠️ 暂未找到 ≥30 字直接原话（视频口播，需抓 B站 CC 字幕逐字）
- **sub_skill_candidate**: `false` — 普及贡献大，但偏工具打包/教学而非原创框架；并入中文 operational 工作流。
- **最近 12 个月动态**: 持续更新整合包（v4.x）支持新模型与 ComfyUI、视频生成工作流；继续做显存优化与汉化。(evidence: [T01-S012])
- **争议 / 批评**: 整合包便利 vs 黑箱依赖、不利于理解底层；版权/分发边界讨论。
- **来源**:
  - [Primary] B站视频, collected 2026-06-22: T01-S012
  - [Reference] ⚠️ 需补 2 条非黑名单独立来源（注意 CSDN/知乎/公众号黑名单不可用）
- **可信度自评**: medium-low — 单一手来源 + 中文圈二手多为黑名单站，取证受限。

### 11. Karla Ortiz

- **One-liner**: 概念艺术家，反 AI 未授权训练数据维权核心人物，Andersen v. Stability 集体诉讼原告之一，提供版权批判的反面视角。(evidence: [T01-S016, T01-S017])
- **核心身份**: 好莱坞概念艺术家（Doctor Strange、Black Panther 等）；Concept Art Association/反 AI 训练维权倡导者。
- **代表作品**: 概念设计作品；对 Stability/Midjourney/DeviantArt 的版权诉讼（共同原告）。
- **值得读 / 听 / 看的 3 件事**:
  - 📖 Artnet: 艺术家诉讼推进报道: https://news.artnet.com/art-world/artists-vs-stability-ai-lawsuit-moves-ahead-2524849 (T01-S016)
  - 📖 BuzzFeed: 三位艺术家原话（"It's gross to me"）: https://www.buzzfeednews.com/article/pranavdixit/ai-art-generators-lawsuit-stable-diffusion-midjourney (T01-S017)
  - 🎙️ ⚠️ 本人 X/talk 较多，待补具体长访谈链接
- **核心思想关键词**: 未经同意的数据摄取 / opt-in 而非 opt-out / 艺术家署名与同意 / 风格盗用 / 知情同意
- **voice_samples**:
  - 行业争议样本: 三位原告艺术家公开表示 AI 用其作品训练「It's gross to me」（令我作呕），主张默认应是 opt-in 而非 opt-out。⚠️ 此为转述+短引；本人 ≥30 字逐字长原话待抓。(source: T01-S017, 转述/短引)
- **sub_skill_candidate**: `false` — 作为「反面/版权批判视角」必须保留，但非创作工作流 operator；进 Phase 2 争议维度。
- **dual_role**: "artist + advocate"
- **最近 12 个月动态**: 诉讼部分主张被允许继续（2024 法官裁定直接侵权等可推进）；持续公开倡导 AI 训练数据同意权。(evidence: [T01-S016])
- **争议 / 批评**: 被 AI 阵营批为「阻碍技术进步」；诉讼多项主张被驳回，法律前景不确定。
- **来源**:
  - [Secondary] Artnet 报道: T01-S016
  - [Primary/quote] BuzzFeed 艺术家原话: T01-S017
  - [Reference] ⚠️ 待补本人 X/采访一手
- **可信度自评**: medium — 立场清晰、报道充足，本人逐字长原话待补。

### 12. AUTOMATIC1111

- **One-liner**: Stable Diffusion WebUI 作者，早期最普及的 SD 图形界面，开源生态早期基建。(evidence: 待补)
- **核心身份**: 公开 handle AUTOMATIC1111（不挖真实身份）；stable-diffusion-webui 创建者。
- **代表作品**: stable-diffusion-webui（A1111）。
- **值得读 / 听 / 看的 3 件事**:
  - 🎬 GitHub: AUTOMATIC1111/stable-diffusion-webui（待加入 manifest）
  - 📖 ⚠️ 匿名，几乎无访谈
- **核心思想关键词**: 易用图形界面 / 插件生态 / 早期普及 / 社区扩展
- **voice_samples**: ⚠️ 暂未找到 ≥30 字直接原话片段（匿名，发声集中于 GitHub）。
- **sub_skill_candidate**: `false` — 历史基建意义大，当前活跃度与个人思想材料薄。
- **最近 12 个月动态**: ⚠️ 待核（A1111 维护节奏放缓，重心转向 Forge/ComfyUI 生态，需补证）。
- **争议 / 批评**: 维护节奏、与 Forge 分叉关系；早期含敏感扩展争议。
- **来源**: ⚠️ 待补 ≥3 条（GitHub 一手 + 2 条独立）。
- **可信度自评**: low — 当前活跃度与材料不足，列为历史 founder 候选，待补证或降为 Phase 2 founders 单列。

### 13. Bilawal Sidhu

- **One-liner**: 前 Google XR/3D Maps，1.5M+ 粉丝的 AI 创作者/创意技术专家，从经典 VFX 视角实操评测 Sora/Runway/可灵等视频工具，是 AI 视频创作工作流的代表性 operator 与批判性观察者。(evidence: [T01-S024, T01-S025])
- **核心身份**: AI 创作者 / 创意技术专家；前 Google（XR、3D Maps PM）；TED AI 主持人；YouTube/X @bilawalsidhu。
- **代表作品**: YouTube AI 视频实操评测；TED talks；对 Sora/Runway/Veo/可灵的对比实测。
- **值得读 / 听 / 看的 3 件事**:
  - 🎬 Bilawal Sidhu YouTube（AI 视频工具实操）: https://www.youtube.com/@bilawalsidhu (T01-S024)
  - 📖 本人主页/bio: https://bilawal.ai/ (T01-S026)
  - 🎙️ X 长帖（AI movie making 工作流痛点）: https://x.com/bilawalsidhu/status/1808889955956957606 (T01-S025)
- **核心思想关键词**: slot machine 本质（扩散模型抽卡）/ 多工具切换破坏 flow / 一致性问题（角色/道具/场景）/ 经典 VFX「fix it in post」/ 集成创作体验缺失
- **voice_samples**:
  - 同业工作流批判样本: 「Moving disjointedly from tool to tool absolutely destroys your flow state, and honestly takes way longer than it should. Midjourney to Photoshop to Magnific to Runway to Luma to Topaz to Eleven Labs...」(source: T01-S025, 原话) —— 直指 AIGC 视频「工具拼盘」之痛
  - 技术评测样本（转述）: 指出即便 Runway 也未做出集成创作体验，部分因扩散模型的「slot machine nature」需反复 re-roll 才能淘到「金块」，且角色/道具/环境难一致。(source: T01-S024, 转述)
- **sub_skill_candidate**: `true`（borderline）— 与「视频创作工作流」focus 高度对齐，有大量长视频材料 + 直接 voice 原话 + 跨工具 operator 视角；Phase 3 可评估是否独立。
- **dual_role**: "creator + critic"
- **最近 12 个月动态**: 持续做新视频模型（Sora/Veo/可灵/即梦）的实操对比与工作流方法；强调把生成模型接进剪辑工具（如 Premiere）才能产出可用内容。(evidence: [T01-S024])
- **争议 / 批评**: 评测带 affiliate/合作色彩的可能；偏体验/实操而非底层研究。
- **来源**:
  - [Primary] YouTube 频道, collected 2026-06-22: T01-S024
  - [Primary/quote] X 长帖原话: T01-S025
  - [Secondary] 本人主页 bio: T01-S026
- **可信度自评**: medium-high — 有逐字原话 + 大量一手视频，operator 视角对 operational focus 价值高。

---

## Phase 2 提炼提示

**反复出现 ≥ 3 个 figures 都谈到的关键词**（候选行业心智模型）:
- **可控性 / controllability vs 抽卡随机（slot machine）**（出现于: Lvmin Zhang、comfyanonymous、万鹏飞、Bilawal Sidhu）—— 从「抽卡随机/re-roll」到「可控生成、一致性」是全行业最核心主线；Bilawal 直接命名「slot machine nature」
- **工具拼盘 vs 集成工作流**（Bilawal Sidhu、comfyanonymous、Scott Detweiler）—— 多工具切换破坏 flow，节点式/集成是回应
- **降低门槛 / 民主化 / 普及**（David Holz、Emad、秋葉aaaki、Caleb Ward）—— 「让普通人也能创作」是共同叙事
- **工具增强而非取代人类**（David Holz、swyx）—— 「责任在人不在模型」「扩展想象力而非造创作机器」
- **效率 / 在普通算力上跑得动**（Robin Rombach latent space、Lvmin Zhang FramePack、秋葉 显存优化）
- **可见 / 可复现工作流**（comfyanonymous 节点式、Scott Detweiler 公开内部 pipeline）

**显著分歧 / 流派分裂**:
- **开源底座阵营**（Rombach/SD、comfyanonymous、Lvmin Zhang、秋葉、A1111）vs **闭源高审美产品阵营**（David Holz/Midjourney、万鹏飞/可灵闭源）—— 价值观（透明 vs 极致体验）与商业模式对立
- **极简「隐藏参数」路线**（Fooocus/Holz）vs **节点式「暴露全部」路线**（ComfyUI）—— 易用 vs 可控的张力
- **技术加速派**（多数工具创造者）vs **版权/伦理批判派**（Karla Ortiz 等艺术家）—— 训练数据同意权是核心战场
- **国产视频闭源快迭代**（可灵/即梦）vs **开源视频**（通义万相 Wan、Hunyuan）—— 国产视频内部分裂

**冷僻领域信号**:
- 总 figure 数 = 13（retained）→ 非冷僻领域，figures 维度厚度 OK。
- **voice_samples 覆盖**：≥2 段逐字原话的有 5 位 —— David Holz（4 段，最强）、Lvmin Zhang（2 段 README 逐字）、comfyanonymous（2 段 README/项目语体）、Bilawal Sidhu（1 段口语原话 + 1 段转述，接近）；其余多为转述或待抓。多数工具创造者发声集中在论文/代码/产品而非长口语访谈，逐字口语原话需二次抓取（talk 字幕、podcast transcript）。Rombach/万鹏飞/Emad/swyx/Scott/秋葉/Caleb/Karla 的逐字原话仍偏薄。
- 中文圈（秋葉、可灵）一手取证受限于黑名单站（知乎/CSDN/公众号），需依赖 B站视频字幕 + InfoQ 等合规二手。
- **Phase 2.8 诚实边界建议**: voice DNA 在「工具创造者」群体上偏弱（多为工程/产品语体而非个人布道原话），mental_model 的 voice 一致性维度需标注：图像生成哲学（Holz/开源阵营）证据充分，视频生成与国产团队的个人 voice 证据较薄。
