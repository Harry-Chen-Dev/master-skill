# Track 06 — Glossary: AIGC Creative Workflow (生成式 AI 视觉创作)

> Locale = global. 覆盖图像 (Midjourney / SD / Flux / ComfyUI) + 视频 (Kling 可灵 / Jimeng 即梦 / Runway / Sora) 创作侧的术语、黑话、标准/版权框架、outsider-tell、厂商话术拒绝。

## Source Manifest

| source_id | url | bucket | last_checked | author/host | one-line note |
|-----------|-----|--------|--------------|-------------|---------------|
| T06-S001 | https://github.com/CompVis/stable-diffusion/blob/main/README.md | verified_primary | 2026-06-22 | CompVis | SD 原始 repo, latent diffusion baseline |
| T06-S002 | https://github.com/comfyanonymous/ComfyUI | verified_primary | 2026-06-22 | comfyanonymous | ComfyUI 官方 repo — node/workflow 范式权威 |
| T06-S003 | https://github.com/AUTOMATIC1111/stable-diffusion-webui | verified_primary | 2026-06-22 | AUTOMATIC1111 | A1111 webui — img2img/inpaint/denoising 参数权威 |
| T06-S004 | https://arxiv.org/abs/2106.09685 | verified_primary | 2026-06-22 | Hu et al (Microsoft) | LoRA 原始论文 (Low-Rank Adaptation) |
| T06-S005 | https://arxiv.org/abs/2302.05543 | verified_primary | 2026-06-22 | Zhang et al | ControlNet 原始论文 |
| T06-S006 | https://arxiv.org/abs/2308.06721 | verified_primary | 2026-06-22 | Ye et al | IP-Adapter 原始论文 |
| T06-S007 | https://github.com/cubiq/ComfyUI_IPAdapter_plus | verified_primary | 2026-06-22 | cubiq (Matteo) | IPAdapter ComfyUI 实现 — "1-image LoRA" 描述源 |
| T06-S008 | https://github.com/Mikubill/sd-webui-controlnet | verified_primary | 2026-06-22 | Mikubill | ControlNet webui 扩展 — preprocessor 列表 |
| T06-S009 | https://github.com/guoyww/AnimateDiff | verified_primary | 2026-06-22 | Guo et al | AnimateDiff repo — motion module 动画化 |
| T06-S010 | https://github.com/bmaltais/kohya_ss | verified_primary | 2026-06-22 | bmaltais | kohya_ss 训练 GUI — LoRA 炼丹标准工具 |
| T06-S011 | https://github.com/KohakuBlueleaf/LyCORIS | verified_primary | 2026-06-22 | KohakuBlueleaf | LyCORIS — LoCon/LoHa 等 LoRA 变体集合 |
| T06-S012 | https://github.com/sczhou/CodeFormer | verified_primary | 2026-06-22 | S-Lab NTU (Zhou et al) | CodeFormer blind face restoration |
| T06-S013 | https://github.com/TencentARC/GFPGAN | verified_primary | 2026-06-22 | Tencent ARC | GFPGAN 面部修复 (StyleGAN2 prior) |
| T06-S014 | https://github.com/xinntao/Real-ESRGAN | verified_primary | 2026-06-22 | Xintao Wang | Real-ESRGAN 超分放大 |
| T06-S015 | https://github.com/Fanghua-Yu/SUPIR | verified_primary | 2026-06-22 | Fanghua Yu et al | SUPIR diffusion-based 超分 |
| T06-S016 | https://github.com/Gourieff/sd-webui-reactor | verified_primary | 2026-06-22 | Gourieff | ReActor 换脸扩展 |
| T06-S017 | https://huggingface.co/black-forest-labs/FLUX.1-dev | verified_primary | 2026-06-22 | Black Forest Labs | Flux.1-dev model card — 非商用 license |
| T06-S018 | https://huggingface.co/black-forest-labs/FLUX.1-schnell | verified_primary | 2026-06-22 | Black Forest Labs | Flux.1-schnell — Apache 2.0 商用 |
| T06-S019 | https://huggingface.co/docs/diffusers/index | verified_primary | 2026-06-22 | Hugging Face | diffusers 官方文档 — scheduler/sampler 命名 |
| T06-S020 | https://docs.comfy.org/ | verified_primary | 2026-06-22 | Comfy Org | ComfyUI 官方文档 — node/workflow 术语 |
| T06-S021 | https://en.wikipedia.org/wiki/Stable_Diffusion | secondary | 2026-06-22 | Wikipedia | SD 概览 — checkpoint/VAE/CLIP 入门锚 |
| T06-S022 | https://en.wikipedia.org/wiki/ControlNet | secondary | 2026-06-22 | Wikipedia | ControlNet 入门定义锚 |
| T06-S023 | https://en.wikipedia.org/wiki/Content_Credentials | secondary | 2026-06-22 | Wikipedia | C2PA / Content Credentials 概览 |
| T06-S024 | https://c2pa.org/faqs/ | secondary | 2026-06-22 | C2PA Coalition | C2PA 官方 FAQ — 溯源标准范围与边界 |
| T06-S025 | https://spec.c2pa.org/specifications/specifications/2.4/explainer/Explainer.html | secondary | 2026-06-22 | C2PA | C2PA 2.4 explainer — manifest 结构 |
| T06-S026 | https://help.openai.com/en/articles/8912793-c2pa-in-chatgpt-images | secondary | 2026-06-22 | OpenAI | DALL-E/Sora 输出嵌 C2PA 凭据 |
| T06-S027 | https://openai.com/index/sora/ | verified_primary | 2026-06-22 | OpenAI | Sora — T2V/I2V 视频生成 |
| T06-S028 | https://stability.ai/license | secondary | 2026-06-22 | Stability AI | SD 商用/会员授权条款 |
| T06-S029 | https://www.copyright.gov/ai/ | verified_primary | 2026-06-22 | US Copyright Office | 美著作权局 AI 报告 — 人类作者性门槛 |
| T06-S030 | https://en.wikipedia.org/wiki/Artificial_intelligence_and_copyright | secondary | 2026-06-22 | Wikipedia | Andersen v. Stability 等训练数据诉讼概览 |
| T06-S031 | https://github.com/cubiq/ComfyUI_IPAdapter_plus/blob/main/README.md | verified_primary | 2026-06-22 | cubiq | IPAdapter 风格/构图迁移模式说明 |

## 总览（按 type 分组）

### Tier 1 — 核心必懂 (28 个)

| 术语 | Type | Insider def | Outsider tell | Last_updated |
|------|------|-------------|---------------|--------------|
| prompt / 咒语 | term | 喂给模型的文本指令，决定生成内容 | 以为"咒语越长越神""有万能咒语包" | 2026-06 |
| negative prompt / 负向 | term | 列出不想要的元素，反向引导 | 不知道有负向，或塞满无关词 | 2026-06 |
| seed / 种子 | term | 决定初始噪声的随机数，固定可复现 | 不懂锁种子，无法复现/微调一张图 | 2026-06 |
| CFG scale | acronym | 提示词遵循强度，越高越贴词但易崩 | 一律拉满，画面糊/过曝 | 2026-06 |
| sampler / 采样器 | term | 去噪算法 (Euler a / DPM++ 2M 等) | 把采样器当玄学随便选 | 2026-06 |
| steps / 步数 | term | 去噪迭代次数，多=细节多但慢 | 以为步数越高越好，无脑拉 150 | 2026-06 |
| denoising strength / 重绘幅度 | term | img2img 中输入图被改动程度 0-1 | i2i 不调重绘幅度，全改或没变化 | 2026-06 |
| checkpoint / 大模型 / 底模 | term | 完整权重的基础生成模型 (SD/SDXL/Flux) | 以为"换个大模型就解决一切" | 2026-06 |
| VAE | acronym | 潜空间↔像素的编解码器，影响色彩 | 出图发灰发糊不知是 VAE 没挂 | 2026-06 |
| LoRA | acronym | 小体积微调权重，注入风格/角色/概念 | 把 LoRA 当 checkpoint，或权重乱叠 | 2026-06 |
| ControlNet | term | 用结构图(姿势/深度/线稿)控制构图 | 只会文生图堆词，不知可控生成 | 2026-06 |
| ComfyUI / node 节点 / workflow | term | 节点式可视化生成工作流引擎 | 把节点工作流当玄学，不懂数据流 | 2026-06 |
| 抽卡 / gacha | term(黑话) | 同 prompt 多次生成挑可用的一张 | 把抽卡运气当成自己的能力 | 2026-06 |
| 炼丹 | term(黑话) | 训练 LoRA/模型，调参如炼丹 | 以为炼丹很玄/不知是训练 | 2026-06 |
| inpainting / 局部重绘 | term | 只重绘蒙版区域，修局部 | 不会局部重绘，整图重抽 | 2026-06 |
| outpainting / 扩图 | term | 向画面外扩展生成新内容 | 不知能扩图，只会裁剪 | 2026-06 |
| 高清放大 / 超分 / upscale | term | 提分辨率+补细节 (ESRGAN/SUPIR 等) | 直接拉伸像素当放大 | 2026-06 |
| 修手 / 崩手 | term(黑话) | AI 手部畸形需修复 | 把崩手当"AI 就这样"放任 | 2026-06 |
| AI 味 / AI 感 | term(黑话) | 一眼假的塑料感/对称感/油光 | 看不出 AI 味，直接出图发布 | 2026-06 |
| 文生图 / T2I | acronym | text-to-image 纯文本生成图 | 以为 AIGC 只有文生图 | 2026-06 |
| 图生图 / I2I | acronym | image-to-image 以图改图 | 不区分 t2i/i2i 流程 | 2026-06 |
| 图生视频 / I2V | acronym | image-to-video 以图驱动出视频 | 把 i2v 当文生视频 | 2026-06 |
| 首帧/尾帧 | term | 视频生成的起始/结束关键帧 | 不知可设尾帧做转场 | 2026-06 |
| 运镜 | term | 镜头运动 (推拉摇移) | 不懂用运镜提示控制镜头 | 2026-06 |
| 一致性 (角色/风格) | term | 跨帧/跨图保持同一角色/风格 | 以为换大模型就能保持一致 | 2026-06 |
| 过拟合 / overfitting | term | 训练过头，LoRA 死记训练集 | 炼丹只看 loss 不看实际泛化 | 2026-06 |
| 打标 / tagging / captioning | term | 给训练集图片写标签引导学习 | 训练不打标或乱打 | 2026-06 |
| C2PA / Content Credentials | standard | 内容溯源元数据标准，标记 AI 生成 | 以为删元数据=洗掉 AI 痕迹无风险 | 2026-06 |

### Tier 2 — 周边熟知 (24 个)

| 术语 | Type | Insider def | Last_updated |
|------|------|-------------|--------------|
| token | term | prompt 被切分的最小语义单元 (~75 限制) | 2026-06 |
| weight / 权重 | term | (prompt:1.3) 调单词强度 | 2026-06 |
| tag / 词缀 | term | 逗号分隔的关键词，danbooru 风格 | 2026-06 |
| CLIP | acronym | 文本编码器，把 prompt 变 embedding | 2026-06 |
| LyCORIS | acronym | LoRA 进阶变体集合 (LoCon/LoHa/DoRA) | 2026-06 |
| IPAdapter | term | 用参考图迁移风格/主体 ("1-image LoRA") | 2026-06 |
| T2I-Adapter | term | 轻量结构控制，ControlNet 替代 | 2026-06 |
| AnimateDiff | term | 给 SD 加 motion module 做动画 | 2026-06 |
| openpose / depth / canny / lineart | term | ControlNet 预处理器类型 | 2026-06 |
| ReActor | term | 基于 inswapper 的换脸扩展 | 2026-06 |
| CodeFormer / GFPGAN | term | 面部修复模型 (保真 vs 质量权衡) | 2026-06 |
| ESRGAN / Real-ESRGAN | acronym | GAN 超分放大模型 | 2026-06 |
| SUPIR | acronym | diffusion 超分，吃显存但细节强 | 2026-06 |
| Ultimate SD Upscale | term | 分块重绘式放大工作流 | 2026-06 |
| Magnific / Topaz | term | 商用增强/放大产品 | 2026-06 |
| hires fix / 高分辨率修复 | term | 先小图再放大重绘，省显存防崩 | 2026-06 |
| embedding / textual inversion | term | 小向量绑定新概念到一个词 | 2026-06 |
| 垫图 / 喂图 | term(黑话) | 给 i2i/IPAdapter 提供参考图 | 2026-06 |
| 跑图 / 队列 | term(黑话) | 批量执行生成任务 | 2026-06 |
| 欠拟合 / underfitting | term | 训练不足，LoRA 学不像 | 2026-06 |
| 训练集 / dataset | term | 炼丹用的图片集合 | 2026-06 |
| 对口型 / lip sync | term | 让视频人物嘴型对上音频 | 2026-06 |
| 时序一致性 / temporal consistency | term | 视频跨帧无闪烁、物体稳定 | 2026-06 |
| 动态强度 / motion strength | term | 视频生成的运动幅度参数 | 2026-06 |

### Standards / Regulations / Licenses 时间轴 (近 5 年有显著变化的)

| 名称 | Issued | Last revised | Decay |
|------|--------|--------------|-------|
| CreativeML Open RAIL-M (SD1.x) | 2022-08 | 2022-08 | low |
| CreativeML Open RAIL++-M (SDXL) | 2023-07 | 2023-07 | low |
| Flux.1-dev Non-Commercial License | 2024-08 | 2024-08 | medium |
| Flux.1-schnell (Apache 2.0) | 2024-08 | 2024-08 | low |
| C2PA Content Credentials spec | 2021 | 2.x (持续修订) | medium-high |

### 行业「外行破绽」高亮 (10 条最容易暴露的)

| 误用 | 内行实际意思 | 出现频率 |
|------|-------------|---------|
| "给我一份万能咒语包" | prompt 只是变量之一，模型/参数/控图缺一不可 | 极高 |
| 不锁 seed 就想复现一张图 | 固定 seed 才能复现+微调 | 高 |
| "换这个大模型就行了" | 底模只是基底，控图/LoRA/工作流才是手艺 | 高 |
| 把抽卡运气当能力 | senior 用可控生成降低抽卡率 | 高 |
| 只会文生图堆词 | 进阶靠 ControlNet/i2i/局部重绘可控生成 | 高 |
| 看不出 AI 味/崩手就发布 | 修手、改面部、去油光是基本收尾 | 高 |
| 把节点工作流当玄学 | workflow 是确定性数据流，可调试可复用 | 中 |
| CFG/steps 无脑拉满 | 各有甜区，过高反而崩 | 中 |
| 以为生成图自动归我版权 | 取决于模型 license + 各地著作权法 | 中 |
| 删 EXIF 以为洗掉 AI 痕迹 | C2PA 凭据是独立的，且训练数据争议另算 | 中 |

---

## 术语详条 (选填 outsider-tell 与争议)

### prompt / 咒语 — prompt / spell
- **Type**: term
- **Tier**: tier-1
- **Definition (insider)**: 喂给模型的文本描述，是生成的输入条件之一，但绝非唯一变量。
- **Definition (outsider)**: 你告诉 AI 想画什么的那段话。
- **Etymology**: 社区戏称"咒语/魔法"，因文本→图像像念咒变魔法。
- **outsider-tell**: `usage_tell` 外行把"咒语"当唯一杠杆，追求"万能咒语包"；内行知道 prompt 只占可控生成的一小部分，结构控制(ControlNet)、底模、参数同等重要。(evidence: [T06-S001, T06-S003])
- **关联术语**: negative prompt, weight, token
- **可信度**: high · **Decay risk**: low

### seed / 种子
- **Type**: term · **Tier**: tier-1
- **Definition (insider)**: 决定初始潜空间噪声的随机整数；固定 seed + 固定参数 = 可复现同一张图，是微调与 A/B 的前提。
- **Definition (outsider)**: 一个数字，决定这次随机从哪开始。
- **outsider-tell**: `usage_tell` 外行不锁种子，出了张好图却复现不出来；内行先锁 seed 再逐项调参定位变量。(evidence: [T06-S003])
- **关联术语**: CFG, sampler, 抽卡
- **可信度**: high · **Decay risk**: low

### CFG scale
- **Type**: acronym (Classifier-Free Guidance) · **Tier**: tier-1
- **Definition (insider)**: 放大"有条件预测 vs 无条件预测"的差，控制 prompt 遵循强度；过高画面僵硬/过曝，过低发散。
- **Etymology**: classifier-free guidance，扩散模型采样技术。
- **outsider-tell**: `usage_tell` 外行一律拉满以为"更听话"，结果崩坏；内行知道每个底模有甜区 (常 4-8)。`pronunciation_tell` 读 "C-F-G" 而非拼词。(evidence: [T06-S003, T06-S019])
- **关联术语**: steps, sampler, denoising strength
- **可信度**: high · **Decay risk**: low

### denoising strength / 重绘幅度
- **Type**: term · **Tier**: tier-1
- **Definition (insider)**: img2img 中先给输入图加多少噪声，决定结果偏离原图的程度 (0=不变, 1=全新)。
- **outsider-tell**: `usage_tell` 外行在 i2i 不调它，要么图没变化要么面目全非；内行用 0.3-0.5 做风格化、0.6+ 做大改。(evidence: [T06-S003])
- **关联术语**: I2I, inpainting, 垫图
- **可信度**: high · **Decay risk**: low

### LoRA
- **Type**: acronym (Low-Rank Adaptation) · **Tier**: tier-1
- **Definition (insider)**: 在底模旁注入低秩增量权重，小体积即可灌入特定风格/角色/概念，不动底模本体。
- **Etymology**: Hu et al. 2021，原为 LLM 微调技术，后用于扩散模型。
- **outsider-tell**: `usage_tell` 外行把 LoRA 当 checkpoint 单独加载，或多个 LoRA 权重乱叠互相打架；内行控权重 (常 0.6-0.9) 并注意触发词。(evidence: [T06-S004, T06-S010])
- **是否被错位包装**: 部分平台把"加载一个角色 LoRA"包装成"AI 复刻任何人"，回避肖像权与训练数据来源问题。(evidence: [T06-S010])
- **关联术语**: LyCORIS, checkpoint, 炼丹, 过拟合
- **可信度**: high · **Decay risk**: low

### ControlNet
- **Type**: term · **Tier**: tier-1
- **Definition (insider)**: 在底模上挂结构条件 (openpose 姿势 / depth 深度 / canny 线稿 / lineart),把构图/姿势/轮廓"锁死",实现可控生成。
- **Etymology**: Zhang et al. 2023，扩散模型空间条件控制网络。
- **outsider-tell**: `usage_tell` 外行只会文生图堆词,出图全靠运气;内行用 ControlNet 把姿势/构图固定,只让 AI 填内容。(evidence: [T06-S005, T06-S008])
- **关联术语**: openpose, depth, T2I-Adapter, IPAdapter
- **可信度**: high · **Decay risk**: low

### C2PA / Content Credentials
- **Type**: standard · **Tier**: tier-1
- **Definition (insider)**: 由 Adobe/微软/OpenAI/Google 等组成的 C2PA 联盟制定的内容溯源标准,用密码学签名的 manifest 记录"谁、何时、用什么工具、是否 AI 生成、每次编辑";DALL-E/Sora/Firefly 等输出已嵌入。
- **Definition (outsider)**: 一种给图片/视频盖的"防伪标签",标记它是不是 AI 做的。
- **常见误用 (outsider-tell)**: `usage_tell` 外行以为删 EXIF 就"洗掉 AI 痕迹"且无风险;内行知道 (1) C2PA 是独立 manifest,但用非 C2PA 工具另存即可剥离;(2) **没有 manifest ≠ 真实**,C2PA 不检测 deepfake,只记录签名者的声明;(3) 训练数据版权争议与溯源是两码事。(evidence: [T06-S023, T06-S024, T06-S026])
- **变化历史**: 2021 联盟成立;规范持续迭代至 2.x;2025 起 Samsung Galaxy S25 等硬件原生签名,采用加速。
- **关联术语**: SynthID, 数字水印
- **可信度**: high · **Decay risk**: medium-high (标准与采用快速演化)

### Flux 许可证 (dev vs schnell)
- **Type**: regulation/license · **Tier**: tier-1
- **Definition (insider)**: Black Forest Labs 的 Flux.1 三档:**dev = 开放权重但仅非商用** (商用需单独 license / 走 pro API);**schnell = Apache 2.0 可商用**;pro = 闭源 API。
- **常见误用 (outsider-tell)**: `usage_tell` 外行下载 Flux.1-dev 直接商用接单,踩 license 红线;内行商用走 schnell 或买 dev 商用授权 / pro API。(evidence: [T06-S017, T06-S018])
- **变化历史**: 2024-08 发布。
- **关联术语**: CreativeML OpenRAIL, checkpoint, 可商用
- **可信度**: high · **Decay risk**: medium (商用授权条款可能调整)

### IPAdapter
- **Type**: term · **Tier**: tier-2
- **Definition (insider)**: 把参考图当"视觉 prompt"注入扩散模型,迁移其风格/主体/构图,无需训练即用一张图;社区称"1-image LoRA"。支持 style only / composition only / style+composition 等模式。
- **outsider-tell**: `usage_tell` 外行把 IPAdapter 当 LoRA 去"训练",或与 ControlNet 混为一谈;内行区分:ControlNet 控结构(姿势/线稿),IPAdapter 控风格/主体外观。(evidence: [T06-S006, T06-S007, T06-S031])
- **关联术语**: ControlNet, LoRA, 垫图
- **可信度**: high · **Decay risk**: low

### 训练数据版权争议 / training-data copyright
- **Type**: regulation/dispute · **Tier**: tier-1
- **Definition (insider)**: 主流底模(SD/Midjourney 等)用网络爬取的海量受版权图训练,引发集体诉讼(Andersen v. Stability AI, 2023 起)。同时美国著作权局立场:**纯 AI 生成、缺乏人类作者性的产物不受著作权保护**,需有实质人类创作贡献才可能登记。
- **常见误用 (outsider-tell)**: `usage_tell` 外行以为"我生成的图就是我的版权,随便商用";内行知道两层风险:(1) 输出端 — 纯 AI 图可版权性在多数法域存疑;(2) 输入端 — 底模训练数据来源未决,模仿在世艺术家风格有侵权/商誉风险。(evidence: [T06-S029, T06-S030])
- **变化历史 (disputed)**: Andersen 案 2023-01 立案,2023-10 大部分 claim 被驳,2024-08 部分恢复;US Copyright Office 2025 系列报告持续更新。法域差异大 (US vs EU vs CN),标 `geographic-specific`。
- **关联术语**: C2PA, Flux license, 可商用
- **可信度**: high · **Decay risk**: high (诉讼与立法快速演进)

---

## 厂商 / 营销话术拒绝 (资深人会拆穿)

| 话术 | 内行拆穿 | evidence |
|------|---------|----------|
| "万能咒语包,复制即出大片" | prompt 只是变量之一;同样咒语换底模/参数/seed 结果天差地别,没有跨模型万能咒语 | [T06-S001, T06-S003] |
| "7 天 AI 绘画月入过万/变现" | 卖课割韭菜话术;真实变现靠可控生成+修图收尾+商用合规,非念几句咒语 | [T06-S010] |
| "一键出大片,零门槛无需学习" | 抹掉控图/炼丹/放大/修手等手艺;一键产出的恰是满是 AI 味、崩手、license 风险的废稿 | [T06-S003, T06-S008] |
| "换我们这个大模型就行了" | 底模只是基底;不会 ControlNet/LoRA/局部重绘,换什么底模都救不了构图失控 | [T06-S005] |
| "AI 绘画取代所有画师" | 营销夸张;可控生成、设定一致性、商业改稿仍重度依赖人;且训练数据与肖像/版权争议未决 | [T06-S004, T06-S030] |
| "生成的图版权自动归你,随便商用" | 版权归属取决于模型 license (Flux dev 非商用)+ 各地著作权法 (纯 AI 生成可版权性存疑)+ 训练数据争议,绝非自动可商用 | [T06-S017, T06-S029] |

---

## Phase 2 提炼提示

**「行业表达 DNA」直接素材** (喂给 Phase 2.5 expression-DNA):
- 高频黑话 top 10: 抽卡 / 炼丹 / 咒语 / 垫图 / 喂图 / 修手·崩手 / AI 味 / 跑图 / 底模 / 重绘幅度 — 黑话密度高,是创意内容类行业典型 register。
- 行业拒绝的厂商话术 top 5: 万能咒语包 / 7天变现 / 一键零门槛 / 换大模型就行 / AI 取代画师 — 反映行业价值观:**可控生成 > 念咒玄学;手艺(控图/炼丹/收尾) > 抽卡运气;合规意识(license/版权)是专业底线**。
- 外行破绽 top 10: 见上"外行破绽高亮"表 — 核心 tell = 把 prompt 当唯一变量、不锁 seed、不懂可控生成、把抽卡当能力、忽视 license。

**「智识谱系」线索** (喂给 Phase 2.7):
- 范式演进: 纯文生图堆词 → ControlNet/IPAdapter 可控生成 → 节点工作流(ComfyUI)确定性流水线 → LoRA/炼丹个性化 → 图像扩展到视频(T2V/I2V/首尾帧/时序一致性)。这条线是"从玄学抽卡到工程化可控"的范式更替。
- 流派之争硬件层: A1111(易用整合) vs ComfyUI(节点可控/可复用) 工具哲学之争;开放权重(SD/Flux-schnell) vs 闭源 API(Midjourney/Sora) 的开放性之争;license 之争(OpenRAIL 商用友好 vs Flux-dev 非商用)。

**「时效性」信号** (喂给 Phase 2.8 诚实边界):
- 高 decay: C2PA 标准与平台采用、各国生成式 AI 监管、模型 license 条款 — 12-24 月内大概率变化。
- 视频生成模型(Kling/即梦/Runway/Sora)迭代极快,具体能力/参数命名 6 月内即可能过时。
- 稳定核: prompt/seed/CFG/sampler/LoRA/ControlNet 等核心术语 5+ 年稳定。

**「工作流变化触发」种子** (喂给 wave 3 Track 03):
- license 变化(如 Flux 商用条款)直接触发商用工作流取舍。
- C2PA 强制化 / 平台水印政策 → 交付流程新增溯源/合规步骤。
- 新底模(SDXL→Flux)发布 → 触发 LoRA 重训、ControlNet 适配、workflow 迁移。

**冷僻 / 信号薄弱**:
- 总术语数 52 (>25)、Tier1 28 (>15)、outsider-tell 覆盖 Tier1 100% — 信号充足,非冷僻行业。
- 薄弱维度: 正式"认证"几乎 N/A(行业无官方执业认证);"标准"以模型 license + C2PA 为主,非传统行业标准化机构产物;zh 一手术语来源受限(知乎/CSDN/公众号黑名单),中文黑话定义靠英文官方源+社区共识反推。
