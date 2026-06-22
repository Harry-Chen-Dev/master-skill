# Track 04 — Canon（知识正典）: AIGC 创作工作流 / AIGC Creative Workflow

> locale=global · focus=operational+technical · 蒸馏侧重创作侧（图像 + 视频生成的工程化创作流水线）
> Canon 的衰减比 tools/workflows 慢。论文 = low decay；官方文档/课程 = medium decay（注 last_updated）。

## Source Manifest

| source_id | url | bucket | last_checked | author/host | one-line note |
|-----------|-----|--------|--------------|-------------|---------------|
| T04-S001 | https://arxiv.org/abs/2006.11239 | verified_primary | 2026-06-22 | Ho, Jain, Abbeel (UC Berkeley) | DDPM — 现代扩散模型奠基论文 |
| T04-S002 | https://arxiv.org/abs/2112.10752 | verified_primary | 2026-06-22 | Rombach et al (CompVis/LMU) | Latent Diffusion / Stable Diffusion 底座 (CVPR 2022) |
| T04-S003 | https://arxiv.org/abs/2212.09748 | verified_primary | 2026-06-22 | Peebles & Xie (UC Berkeley/NYU) | DiT — Diffusion Transformer，SD3/Sora/Flux 的架构祖先 |
| T04-S004 | https://arxiv.org/abs/2302.05543 | verified_primary | 2026-06-22 | Zhang, Rao, Agrawala (Stanford) | ControlNet — 空间可控生成奠基 |
| T04-S005 | https://arxiv.org/abs/2106.09685 | verified_primary | 2026-06-22 | Hu et al (Microsoft) | LoRA — 低秩微调，社区定制模型标准方法 |
| T04-S006 | https://arxiv.org/abs/2208.12242 | verified_primary | 2026-06-22 | Ruiz et al (Google) | DreamBooth — 主体一致性微调 |
| T04-S007 | https://arxiv.org/abs/2208.01618 | verified_primary | 2026-06-22 | Gal et al (Tel Aviv/NVIDIA) | Textual Inversion — embedding 学新概念 |
| T04-S008 | https://arxiv.org/abs/2108.01073 | verified_primary | 2026-06-22 | Meng et al (Stanford) | SDEdit — 图生图/重绘的理论基础 |
| T04-S009 | https://arxiv.org/abs/2308.06721 | verified_primary | 2026-06-22 | Ye et al (Tencent) | IP-Adapter — 图像提示/风格&角色参考 |
| T04-S010 | https://arxiv.org/abs/2311.15127 | verified_primary | 2026-06-22 | Blattmann et al (Stability AI) | Stable Video Diffusion — 开源视频扩散奠基 |
| T04-S011 | https://arxiv.org/abs/2207.12598 | verified_primary | 2026-06-22 | Ho & Salimans (Google) | Classifier-Free Guidance (CFG) — 提示强度核心机制 |
| T04-S012 | https://arxiv.org/abs/2010.02502 | verified_primary | 2026-06-22 | Song, Meng, Ermon (Stanford) | DDIM — 确定性快速采样器 |
| T04-S013 | https://arxiv.org/abs/2206.00364 | verified_primary | 2026-06-22 | Karras et al (NVIDIA) | EDM — 采样器设计统一框架 (Karras schedule) |
| T04-S014 | https://arxiv.org/abs/2011.13456 | verified_primary | 2026-06-22 | Song et al (Stanford) | Score-based SDE — 扩散的连续时间统一视角 |
| T04-S015 | https://arxiv.org/abs/2403.03206 | verified_primary | 2026-06-22 | Esser et al (Stability AI) | SD3 / Rectified Flow + MM-DiT (ICML 2024) |
| T04-S016 | https://arxiv.org/abs/2307.01952 | verified_primary | 2026-06-22 | Podell et al (Stability AI) | SDXL 技术报告 |
| T04-S017 | https://arxiv.org/abs/1505.04597 | verified_primary | 2026-06-22 | Ronneberger et al | U-Net — SD1.x/SDXL 的去噪骨干 |
| T04-S018 | https://arxiv.org/abs/2304.08818 | verified_primary | 2026-06-22 | Blattmann et al (NVIDIA) | Video LDM — 时序层 inflation 视频扩散 |
| T04-S019 | https://openai.com/index/video-generation-models-as-world-simulators/ | verified_primary | 2026-06-22 | OpenAI | Sora 技术报告 — DiT 视频生成 + world simulator |
| T04-S020 | https://github.com/comfyanonymous/ComfyUI | verified_primary | 2026-06-22 | comfyanonymous | ComfyUI 节点图引擎主仓 |
| T04-S021 | https://docs.comfy.org/ | verified_primary | 2026-06-22 | Comfy Org | ComfyUI 官方文档 |
| T04-S022 | https://github.com/comfyanonymous/ComfyUI_examples | verified_primary | 2026-06-22 | comfyanonymous | ComfyUI 官方示例工作流 canon |
| T04-S023 | https://huggingface.co/docs/diffusers/index | verified_primary | 2026-06-22 | Hugging Face | diffusers 库官方文档 |
| T04-S024 | https://huggingface.co/learn/diffusion-course | verified_primary | 2026-06-22 | Hugging Face | 官方 Diffusion Models 课程 |
| T04-S025 | https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0 | verified_primary | 2026-06-22 | Stability AI | SDXL base 模型卡 |
| T04-S026 | https://huggingface.co/stabilityai/stable-diffusion-3-medium | verified_primary | 2026-06-22 | Stability AI | SD3 medium 模型卡 |
| T04-S027 | https://huggingface.co/black-forest-labs/FLUX.1-dev | verified_primary | 2026-06-22 | Black Forest Labs | Flux.1-dev 模型卡 |
| T04-S028 | https://docs.midjourney.com/ | verified_primary | 2026-06-22 | Midjourney | Midjourney 官方文档 |
| T04-S029 | https://github.com/CompVis/stable-diffusion | verified_primary | 2026-06-22 | CompVis | 原版 SD 参考实现仓 |
| T04-S030 | https://github.com/Stability-AI/generative-models | verified_primary | 2026-06-22 | Stability AI | SDXL/SVD 官方实现仓 |
| T04-S031 | https://github.com/lllyasviel/ControlNet | verified_primary | 2026-06-22 | lllyasviel (张吕敏) | ControlNet 官方实现仓 |
| T04-S032 | https://github.com/AUTOMATIC1111/stable-diffusion-webui | verified_primary | 2026-06-22 | AUTOMATIC1111 | A1111 WebUI — 早期社区事实标准 GUI |
| T04-S033 | https://arxiv.org/abs/2302.08453 | verified_primary | 2026-06-22 | Mou et al (Tencent) | T2I-Adapter — 轻量可控生成（ControlNet 同期对手） |
| T04-S034 | https://arxiv.org/abs/2310.00426 | verified_primary | 2026-06-22 | Chen et al (HuaWei/HKU) | PixArt-α — 早期开源 DiT T2I |
| T04-S035 | https://arxiv.org/abs/2204.06125 | verified_primary | 2026-06-22 | Ramesh et al (OpenAI) | DALL·E 2 / unCLIP |
| T04-S036 | https://arxiv.org/abs/2205.11487 | verified_primary | 2026-06-22 | Saharia et al (Google) | Imagen — 大 T5 文本编码器 + 级联扩散 |
| T04-S037 | https://arxiv.org/abs/2211.09800 | verified_primary | 2026-06-22 | Brooks et al (UC Berkeley) | InstructPix2Pix — 指令式图像编辑 |
| T04-S038 | https://arxiv.org/abs/1503.03585 | verified_primary | 2026-06-22 | Sohl-Dickstein et al | 扩散概率模型的最初提出 (2015) |
| T04-S039 | https://klingai.com/docs/technical-overview | surrogate_primary | 2026-06-22 | Kuaishou 可灵 | 可灵 vendor docs 官方技术概览 originator（DiT+3D VAE+全注意力） |
| T04-S040 | https://jimeng.jianying.com/ | surrogate_primary | 2026-06-22 | 字节 即梦 | vendor 官方平台（豆包/Seedance 视频生成） |
| T04-S041 | https://arxiv.org/abs/2105.05233 | verified_primary | 2026-06-22 | Dhariwal & Nichol (OpenAI) | Diffusion Models Beat GANs — classifier guidance 起源 |
| T04-S042 | https://huggingface.co/papers/2311.15127 | verified_primary | 2026-06-22 | Hugging Face | SVD paper page（社区讨论/引用入口） |

---

## 总览（按类型分组）

### Seminal Papers（必读，扩散底座 + 可控 + 视频）

| 论文 | 年 | 核心 idea | source |
|------|----|-----------|--------|
| DDPM | 2020 | 去噪扩散概率模型，奠定现代 diffusion 训练目标 | T04-S001 |
| Latent Diffusion (SD) | 2022 | 在 VAE 潜空间做扩散，让大图生成可负担 | T04-S002 |
| DiT | 2022 | 用 Transformer 替代 U-Net 做扩散骨干 | T04-S003 |
| ControlNet | 2023 | 复制可训练分支注入空间条件（边缘/姿态/深度） | T04-S004 |
| LoRA | 2021 | 低秩适配器微调，社区定制模型基础 | T04-S005 |
| DreamBooth | 2022 | 少量图微调绑定主体 token，主体一致性 | T04-S006 |
| Textual Inversion | 2022 | 仅学新 embedding 表示新概念 | T04-S007 |
| SDEdit | 2021 | 加噪再去噪实现引导式图生图/重绘 | T04-S008 |
| IP-Adapter | 2023 | 解耦交叉注意力注入图像提示 | T04-S009 |
| Stable Video Diffusion | 2023 | 三阶段训练的开源潜空间视频扩散 | T04-S010 |
| Classifier-Free Guidance | 2022 | 无需分类器的引导，CFG scale 机制 | T04-S011 |
| DDIM | 2020 | 非马尔可夫确定性采样，少步快采样 | T04-S012 |
| EDM (Karras) | 2022 | 统一采样器设计空间，Karras 噪声调度 | T04-S013 |
| SD3 (Rectified Flow + MM-DiT) | 2024 | 整流流 + 多模态 DiT，新一代 T2I 架构 | T04-S015 |
| Video LDM | 2023 | 给图像模型 inflate 时序层做视频扩散 | T04-S018 |
| Sora 技术报告 | 2024 | DiT 视频生成 + 时空 patch + world simulator 框架 | T04-S019 |

### 官方文档 / 模型卡 canon

| 文档 | 主体 | 用途 | source |
|------|------|------|--------|
| ComfyUI 主仓 + 文档 | Comfy Org | 节点图工作流引擎事实标准 | T04-S020, T04-S021 |
| ComfyUI examples | Comfy Org | 官方可复现工作流模板 | T04-S022 |
| diffusers 文档 | Hugging Face | Python 调用扩散模型的官方库 | T04-S023 |
| SDXL 模型卡 | Stability AI | 双阶段 base+refiner 工程细节 | T04-S025 |
| SD3 medium 模型卡 | Stability AI | MM-DiT 推理参数 | T04-S026 |
| Flux.1-dev 模型卡 | Black Forest Labs | 当前开源 SOTA T2I（蒸馏/dev/pro） | T04-S027 |
| Midjourney 文档 | Midjourney | 闭源谱系参数体系（--ar/--sref/--cref/--v） | T04-S028 |
| 可灵技术概览 | Kuaishou | DiT+3D VAE+全注意力视频架构 | T04-S039 |

### Courses（必看）

| 课程 | 讲师/机构 | 格式 | last_updated | 一句话 | source |
|------|-----------|------|--------------|--------|--------|
| HF Diffusion Models Course | Hugging Face | 互动 notebook + 阅读 | 见下节注 | 从零实现扩散到用 diffusers 微调 | T04-S024 |
| ComfyUI examples（自学路径） | Comfy Org | 可复现工作流 | rolling | 官方工作流即课程，照搬即学 | T04-S022 |

### Core Concepts（25 个，见下方详表）

| 概念 | 一句话定义 | 来源 |
|------|-----------|------|
| 扩散去噪 (denoising diffusion) | 从纯噪声逐步预测并去除噪声生成图像 | T04-S001 |
| 前向加噪 / 反向去噪 | 训练时加噪、推理时反向去噪的两个过程 | T04-S038, T04-S001 |
| Latent space 潜空间 | 在 VAE 压缩的低维空间做扩散以省算力 | T04-S002 |
| VAE 变分自编码器 | 图像↔潜空间的编解码器，视频额外需 3D VAE | T04-S002, T04-S039 |
| U-Net | SD1.x/SDXL 去噪骨干，带跳连接的编解码网络 | T04-S017 |
| DiT (Diffusion Transformer) | 用 Transformer 替代 U-Net 的扩散骨干 | T04-S003 |
| MM-DiT | 文本与图像分流的多模态 DiT（SD3/Flux） | T04-S015 |
| CFG (classifier-free guidance) | 控制提示遵循强度的引导系数 | T04-S011 |
| Sampler 采样器 | 反向去噪的数值求解器（Euler/DPM++/DDIM） | T04-S012, T04-S013 |
| Steps 步数 | 采样迭代次数，影响质量与速度 | T04-S012 |
| Noise schedule 噪声调度 | 各步噪声水平安排（Karras 等） | T04-S013 |
| Denoising strength 重绘幅度 | 图生图中保留原图程度的系数 | T04-S008 |
| Seed 随机种子 | 决定初始噪声，固定可复现 | T04-S001 |
| CFG/score guidance | 用条件-无条件预测之差放大语义 | T04-S011, T04-S041 |
| ControlNet 条件控制 | 用边缘/深度/姿态等空间图约束构图 | T04-S004 |
| T2I-Adapter | 轻量空间条件注入（ControlNet 同期对手） | T04-S033 |
| LoRA 低秩微调 | 注入低秩矩阵微调风格/角色 | T04-S005 |
| DreamBooth | 少量图绑定主体 token 做一致性微调 | T04-S006 |
| Textual Inversion | 学一个新 embedding 表示概念 | T04-S007 |
| IP-Adapter | 图像提示注入风格/角色参考 | T04-S009 |
| Inpainting / Outpainting | 局部重绘 / 画面外扩 | T04-S008 |
| SDEdit 图生图 | 加噪到中段再去噪实现引导编辑 | T04-S008 |
| Latent upscale / hires fix | 潜空间放大再二次去噪提分辨率 | T04-S016 |
| 角色一致性 (character consistency) | 跨图保持同一角色（DreamBooth/IP-Adapter/--cref） | T04-S006, T04-S009, T04-S028 |
| 视频扩散 / 时序一致性 / 首尾帧 | 视频生成的时序连贯与首尾帧控制 | T04-S018, T04-S010, T04-S039 |

---

## 详表

### 📄 1. DDPM — Denoising Diffusion Probabilistic Models

- **Authors**: Jonathan Ho, Ajay Jain, Pieter Abbeel
- **Venue + Year**: NeurIPS 2020
- **arXiv**: https://arxiv.org/abs/2006.11239
- **One-liner**: 现代扩散生成模型的奠基论文，把 2015 年的扩散思想做成可训练、可生成高质量图像的范式。 (evidence: [T04-S001])
- **核心 idea**: 用简化的 ε-预测（预测噪声）目标训练去噪网络；前向逐步加高斯噪声，反向逐步去噪采样。
- **为什么经典**: 后续所有 SD/Imagen/DALL·E 2/视频扩散都建立在 DDPM 的训练目标之上；被几乎所有扩散课程列为第一篇。 (evidence: [T04-S001, T04-S024])
- **如何读**: 重点读 Sec 3（forward/reverse process）+ Eq. 简化训练目标；数学推导可跳。
- **后续/扩展**: improved DDPM、DDIM (T04-S012)、score-based SDE (T04-S014)。
- **可信度 / Decay risk**: high / low

### 📄 2. Latent Diffusion / Stable Diffusion (LDM)

- **Authors**: Robin Rombach, Andreas Blattmann, Dominik Lorenz, Patrick Esser, Björn Ommer
- **Venue + Year**: CVPR 2022
- **arXiv**: https://arxiv.org/abs/2112.10752
- **One-liner**: 把扩散搬到 VAE 潜空间，使消费级 GPU 能跑高分辨率文生图——整个开源 AIGC 创作生态的物理底座。 (evidence: [T04-S002])
- **核心 idea**: VAE 压缩到潜空间 + U-Net 扩散 + 交叉注意力注入文本条件（CLIP）。
- **为什么经典**: Stable Diffusion 1.x/2.x/SDXL 都是它的产品化；ComfyUI/A1111/LoRA/ControlNet 全部围绕它。 (evidence: [T04-S002, T04-S029, T04-S032])
- **如何读**: 读 Sec 3 潜空间扩散 + 交叉注意力条件机制。
- **后续/扩展**: SDXL (T04-S016)、SD3 (T04-S015)。
- **可信度 / Decay risk**: high / low

### 📄 3. DiT — Scalable Diffusion Models with Transformers

- **Authors**: William Peebles, Saining Xie
- **Venue + Year**: ICCV 2023
- **arXiv**: https://arxiv.org/abs/2212.09748
- **One-liner**: 证明 Transformer 能替代 U-Net 做扩散骨干并良好 scale——SD3/Flux/Sora/可灵的共同架构祖先。 (evidence: [T04-S003])
- **核心 idea**: 把图像潜表示切 patch，用标准 Transformer + AdaLN 条件化做去噪。
- **为什么经典**: 2024 后所有 SOTA 图像/视频模型（SD3 MM-DiT、Sora、可灵）都转向 DiT 架构。 (evidence: [T04-S003, T04-S015, T04-S019, T04-S039])
- **如何读**: 读架构图 + AdaLN-Zero 部分 + scaling 曲线。
- **后续/扩展**: PixArt-α (T04-S034)、SD3 MM-DiT (T04-S015)、Sora (T04-S019)。
- **可信度 / Decay risk**: high / low

### 📄 4. ControlNet

- **Authors**: Lvmin Zhang (张吕敏), Anyi Rao, Maneesh Agrawala
- **Venue + Year**: ICCV 2023
- **arXiv**: https://arxiv.org/abs/2302.05543
- **One-liner**: 让扩散模型接受边缘/姿态/深度/线稿等空间条件，把"抽卡"变成可控构图——创作工程化的关键拐点。 (evidence: [T04-S004])
- **核心 idea**: 冻结原模型，复制一份可训练编码器分支，通过零初始化卷积逐步注入条件。
- **为什么经典**: 商业插画/产品图/换装/线稿上色全靠它；ComfyUI/A1111 必装。 (evidence: [T04-S004, T04-S031, T04-S020])
- **如何读**: 读 zero-convolution 设计 + 各 condition 类型示例。
- **后续/扩展**: T2I-Adapter (T04-S033)、ControlNet for SDXL/Flux。
- **可信度 / Decay risk**: high / low

### 📄 5. LoRA — Low-Rank Adaptation

- **Authors**: Edward Hu et al (Microsoft)
- **Venue + Year**: ICLR 2022（原为 LLM 提出）
- **arXiv**: https://arxiv.org/abs/2106.09685
- **One-liner**: 用低秩矩阵旁路微调，让普通用户能以几十张图训练专属画风/角色 LoRA——社区生态的核心货币。 (evidence: [T04-S005])
- **核心 idea**: 冻结原权重，只训练注入的低秩 ΔW=BA，省显存、文件小、可叠加。
- **为什么经典**: Civitai 上数十万社区模型几乎都是 LoRA；ComfyUI/diffusers 原生支持。 (evidence: [T04-S005, T04-S023])
- **如何读**: 读低秩分解动机 + rank 选择；扩散里关注注入位置（注意力层）。
- **后续/扩展**: DreamBooth+LoRA、LyCORIS/LoHa、DoRA。
- **可信度 / Decay risk**: high / low

### 📄 6. DreamBooth

- **Authors**: Nataniel Ruiz et al (Google)
- **Venue + Year**: CVPR 2023
- **arXiv**: https://arxiv.org/abs/2208.12242
- **One-liner**: 用 3-5 张图微调把特定主体绑定到唯一标识 token，实现主体一致性生成。 (evidence: [T04-S006])
- **核心 idea**: rare-token 标识 + 类先验保持损失（防过拟合/语言漂移）。
- **为什么经典**: 角色/产品一致性的奠基方法，常与 LoRA 组合（DreamBooth-LoRA）。 (evidence: [T04-S006, T04-S023])
- **如何读**: 读 prior preservation loss 设计。
- **后续/扩展**: LoRA-DreamBooth、IP-Adapter（免训练替代）。
- **可信度 / Decay risk**: high / low

### 📄 7. Textual Inversion

- **Authors**: Rinon Gal et al (Tel Aviv Univ / NVIDIA)
- **Venue + Year**: ICLR 2023
- **arXiv**: https://arxiv.org/abs/2208.01618
- **One-liner**: 不动模型权重，只学一个新词向量 (embedding) 来表示新概念/风格。 (evidence: [T04-S007])
- **核心 idea**: 在文本编码器词嵌入空间优化一个新 token 的向量。
- **为什么经典**: 最轻量的概念注入法（几 KB 的 embedding 文件），与 LoRA/DreamBooth 并列三大定制法。 (evidence: [T04-S007, T04-S005, T04-S006])
- **如何读**: 读优化目标 + 与 DreamBooth 的容量对比。
- **后续/扩展**: 
- **可信度 / Decay risk**: high / low

### 📄 8. SDEdit — Guided Image Synthesis and Editing

- **Authors**: Chenlin Meng et al (Stanford)
- **Venue + Year**: ICLR 2022
- **arXiv**: https://arxiv.org/abs/2108.01073
- **One-liner**: "加噪到中段再去噪" 的图生图/草图变成品理论基础——denoising strength 滑杆背后的原理。 (evidence: [T04-S008])
- **核心 idea**: 把输入图加噪到某 t，再用扩散模型反向去噪，t 越大越偏离原图。
- **为什么经典**: img2img、inpainting、草图上色全部是 SDEdit 的应用；重绘幅度参数直接源于此。 (evidence: [T04-S008])
- **如何读**: 读 noise level ↔ 编辑强度的 trade-off 曲线。
- **后续/扩展**: InstructPix2Pix (T04-S037)、inpainting 专用模型。
- **可信度 / Decay risk**: high / low

### 📄 9. IP-Adapter

- **Authors**: Hu Ye et al (Tencent AI Lab)
- **Venue + Year**: 2023
- **arXiv**: https://arxiv.org/abs/2308.06721
- **One-liner**: 免训练地把一张参考图当"图像提示"注入，做风格/角色参考（"一张图定风格"）。 (evidence: [T04-S009])
- **核心 idea**: 解耦的交叉注意力——为图像特征单独加一路 cross-attn，与文本提示并行。
- **为什么经典**: 角色一致性/风格迁移的免训练主力，ComfyUI 工作流标配；FaceID 变体做人脸一致。 (evidence: [T04-S009, T04-S020])
- **如何读**: 读 decoupled cross-attention 结构图。
- **后续/扩展**: IP-Adapter FaceID、InstantID。
- **可信度 / Decay risk**: high / low

### 📄 10. Stable Video Diffusion (SVD)

- **Authors**: Andreas Blattmann, Tim Dockhorn, ..., Robin Rombach (Stability AI)
- **Venue + Year**: 2023
- **arXiv**: https://arxiv.org/abs/2311.15127
- **One-liner**: 开源的潜空间视频扩散模型，给出"图像预训练→视频预训练→高质量微调"的三阶段配方。 (evidence: [T04-S010])
- **核心 idea**: 在图像 LDM 上加时序层，强调数据策展（captioning + filtering）对视频质量的决定性。
- **为什么经典**: 第一个可商用的开源 image-to-video 基座；后续开源视频工作的对比基线。 (evidence: [T04-S010, T04-S042, T04-S030])
- **如何读**: 读三阶段训练 + 数据策展 pipeline。
- **后续/扩展**: 闭源可灵/Sora（DiT 路线，T04-S019, T04-S039）。
- **可信度 / Decay risk**: high / medium（开源视频迭代快）

### 📄 11. Classifier-Free Guidance (CFG)

- **Authors**: Jonathan Ho, Tim Salimans (Google)
- **Venue + Year**: NeurIPS Workshop 2021 / 2022
- **arXiv**: https://arxiv.org/abs/2207.12598
- **One-liner**: 不训分类器、用条件与无条件预测之差放大语义遵循——所有创作者天天调的 "CFG scale"。 (evidence: [T04-S011])
- **核心 idea**: 训练时随机丢弃条件，推理时 ε = ε_uncond + s·(ε_cond − ε_uncond)。
- **为什么经典**: 提示遵循度的核心旋钮；过高会过曝/伪影，理解它=理解抽卡。 (evidence: [T04-S011, T04-S041])
- **如何读**: 读 guidance scale 公式即可。
- **后续/扩展**: CFG rescale、dynamic thresholding、distilled-CFG（Flux dev）。
- **可信度 / Decay risk**: high / low

### 📄 12. DDIM — Denoising Diffusion Implicit Models

- **Authors**: Jiaming Song, Chenlin Meng, Stefano Ermon (Stanford)
- **Venue + Year**: ICLR 2021
- **arXiv**: https://arxiv.org/abs/2010.02502
- **One-liner**: 非马尔可夫确定性采样，几十步出图、可复现、可插值——采样器谱系的起点。 (evidence: [T04-S012])
- **核心 idea**: 重构反向过程为确定性 ODE，大幅减少采样步数。
- **为什么经典**: "采样步数"与"采样器选择"两个创作参数的源头；DPM++/Euler 都是其后裔。 (evidence: [T04-S012, T04-S013])
- **如何读**: 读 deterministic sampling + 与 DDPM 步数对比。
- **后续/扩展**: DPM-Solver / DPM++、EDM (T04-S013)。
- **可信度 / Decay risk**: high / low

### 📄 13. EDM — Elucidating the Design Space of Diffusion Models

- **Authors**: Tero Karras et al (NVIDIA)
- **Venue + Year**: NeurIPS 2022
- **arXiv**: https://arxiv.org/abs/2206.00364
- **One-liner**: 把扩散的噪声调度/预处理/采样器拆成可独立调的设计模块——ComfyUI 里的 "Karras" 调度即出自此。 (evidence: [T04-S013])
- **核心 idea**: 统一框架解释采样器与 schedule，提出 Karras sigma 调度。
- **为什么经典**: 解释了为什么不同 sampler/schedule 出图差异，是进阶调参的理论。 (evidence: [T04-S013, T04-S012])
- **如何读**: 读设计空间表 + Karras schedule 定义。
- **可信度 / Decay risk**: high / low

### 📄 14. SD3 — Scaling Rectified Flow Transformers (MM-DiT)

- **Authors**: Patrick Esser et al (Stability AI)
- **Venue + Year**: ICML 2024
- **arXiv**: https://arxiv.org/abs/2403.03206
- **One-liner**: 用 rectified flow + 多模态 DiT（文本/图像双流）做新一代文生图，显著改善文字渲染与提示遵循。 (evidence: [T04-S015])
- **核心 idea**: rectified flow 直线化采样轨迹 + MM-DiT 双流注意力 + 多文本编码器。
- **为什么经典**: 当前主流开源 T2I 架构（SD3.5/Flux 同谱系）；理解 flow-matching 入口。 (evidence: [T04-S015, T04-S026, T04-S027])
- **如何读**: 读 rectified flow 动机 + MM-DiT 双流图。
- **后续/扩展**: Flux.1 (T04-S027)、SD3.5。
- **可信度 / Decay risk**: high / low

### 📄 15. Video LDM — Align Your Latents

- **Authors**: Andreas Blattmann et al (NVIDIA/LMU)
- **Venue + Year**: CVPR 2023
- **arXiv**: https://arxiv.org/abs/2304.08818
- **One-liner**: 给预训练图像 LDM "inflate" 时序注意力层即可做视频生成，开源视频扩散的早期范式。 (evidence: [T04-S018])
- **核心 idea**: 冻结/复用图像潜扩散权重，仅训新增时序层对齐潜表示。
- **为什么经典**: SVD/AnimateDiff 等的思想前驱；解释"时序一致性"如何被约束。 (evidence: [T04-S018, T04-S010])
- **如何读**: 读 temporal layer inflation 部分。
- **可信度 / Decay risk**: high / medium

### 📄 16. Sora 技术报告 — Video generation models as world simulators

- **Authors**: OpenAI
- **Venue + Year**: 2024-02（技术博客/报告）
- **URL**: https://openai.com/index/video-generation-models-as-world-simulators/
- **One-liner**: 用 DiT + 时空 patch 在大规模视频上训练，提出"视频生成模型即世界模拟器"的范式叙事。 (evidence: [T04-S019])
- **核心 idea**: 将视频压缩为时空 latent patch 当作 token，DiT 在其上扩散；变分辨率/时长/宽高比训练。
- **为什么经典**: 定义了闭源长视频生成的标杆与话语；可灵/即梦/Veo 等都对标其叙事。 (evidence: [T04-S019, T04-S039, T04-S003])
- **如何读**: 通读全博客（无公式），关注 patch 化与 scaling 段落。
- **可信度 / Decay risk**: high / medium（产品迭代，但范式稳定）

### 📄 17–20. 周边奠基 / 谱系论文（速览）

- **U-Net** (T04-S017, https://arxiv.org/abs/1505.04597)：SD1.x/SDXL 去噪骨干的网络结构源头。 (evidence: [T04-S017, T04-S002])
- **SDXL 技术报告** (T04-S016, https://arxiv.org/abs/2307.01952)：双阶段 base+refiner、size/crop 条件化，开源创作主力一代。 (evidence: [T04-S016, T04-S025])
- **Diffusion Models Beat GANs** (T04-S041, https://arxiv.org/abs/2105.05233)：classifier guidance 起源（CFG 的前身）。 (evidence: [T04-S041, T04-S011])
- **Score-based SDE** (T04-S014, https://arxiv.org/abs/2011.13456)：用 SDE/ODE 统一扩散的连续时间视角，进阶必读。 (evidence: [T04-S014, T04-S013])
- **DALL·E 2 / unCLIP** (T04-S035) 与 **Imagen** (T04-S036)：闭源大厂文生图谱系，提供 CLIP-latent 与大文本编码器两条对照路线。 (evidence: [T04-S035, T04-S036])
- **InstructPix2Pix** (T04-S037)：自然语言指令式图像编辑，编辑类工作流前驱。 (evidence: [T04-S037, T04-S008])
- **T2I-Adapter** (T04-S033) / **PixArt-α** (T04-S034)：可控生成与开源 DiT 的同期重要分支。 (evidence: [T04-S033, T04-S034])

### 🎓 Courses & 官方文档 canon

#### 🎓 Hugging Face — Diffusion Models Course (T04-S024)

- **Lecturer/Institution**: Hugging Face（Jonathan Whitaker @ answer.ai + Lewis Tunstall @ HF）
- **Format**: 4 units，每 unit = 理论 + 2 个实操 notebook
- **One-liner**: 唯一同时讲"扩散数学原理"和"diffusers 工程调用"的官方免费课。 (evidence: [T04-S024, T04-S023])
- **完整 vs 关键章节**: Unit 1 扩散原理 + Unit 3 Stable Diffusion/文本条件是核心；Unit 2 finetuning&guidance、Unit 4 进阶可选。
- **难度/先修**: 进阶（需 PyTorch 基础）
- **Last_updated**: BibTeX 标注 2022（课程主体内容仍以 2022 写就，diffusers API 已演进——使用时需对照当前 diffusers 文档 T04-S023）
- **可信度 / Decay risk**: high / medium（随 diffusers 迭代）

#### 📘 ComfyUI 文档 + 官方示例 (T04-S021, T04-S022)

- **One-liner**: ComfyUI 的官方 examples 仓本身就是"工作流教科书"——每类任务（txt2img/img2img/inpaint/ControlNet/LoRA/SDXL/Flux/video）给可直接拖入的 JSON 工作流。 (evidence: [T04-S022, T04-S020, T04-S021])
- **Format**: rolling 文档 + 可复现工作流
- **Last_updated**: rolling（跟随 ComfyUI 发布）
- **可信度 / Decay risk**: high / medium

#### 📘 diffusers 官方文档 (T04-S023)

- **One-liner**: 用 Python 程序化调用所有主流扩散模型（SD/SDXL/SD3/Flux/ControlNet/LoRA/视频）的标准库文档。 (evidence: [T04-S023])
- **可信度 / Decay risk**: high / medium

#### 📘 模型卡 canon（SDXL / SD3 / Flux.1）(T04-S025, T04-S026, T04-S027)

- **One-liner**: 模型卡是每代底座的一手"使用说明书"——推荐分辨率、采样步数、CFG、许可证、能力边界都在此。 (evidence: [T04-S025, T04-S026, T04-S027])
- **可信度 / Decay risk**: high / medium

#### 📘 Midjourney 官方文档 (T04-S028)

- **One-liner**: 闭源谱系的参数体系 canon——`--ar`/`--stylize`/`--sref`(风格参考, v7 含 `--sv`/`--sw`)/`--chaos`/`--v` 的权威定义；角色参考在 v6 为 `--cref`+`--cw`，**v7 起由 Omni Reference 取代 `--cref`**（用 `--cref` 会报错/被忽略）。 (evidence: [T04-S028])
- **可信度 / Decay risk**: high / medium（版本快速演进）

#### 📘 可灵 / 即梦 vendor 官方（T04-S039, T04-S040）

- **One-liner**: 国产视频谱系的一手能力说明——可灵技术概览给出 DiT+3D VAE+全注意力架构；即梦/Seedance 给首尾帧、运镜、对口型等创作参数。 (evidence: [T04-S039, T04-S040])
- **标注**: bucket=surrogate_primary（vendor 官方一手，但带产品营销，mental model 需 ≥2 源交叉）。
- **可信度 / Decay risk**: medium / high（闭源、产品迭代极快）

---

## Phase 2 提炼提示

**反复出现 ≥ 3 个 canon 都讨论的核心 idea（候选行业心智模型）**:
- **"在潜空间逐步去噪"是一切的物理底层**：出现于 DDPM(T04-S001)/LDM(T04-S002)/SVD(T04-S010) → 候选心智模型「生成 = 受控去噪，每个参数都是在调'怎么去噪'」。
- **"可控性是工程化的命门"**：ControlNet(T04-S004)/IP-Adapter(T04-S009)/DreamBooth(T04-S006) 都在解"如何把抽卡变成可指定" → 候选心智模型「创作流水线 = 把随机性逐层收束（构图→风格→角色→时序）」。
- **"少量数据定制 = 社区生态货币"**：LoRA(T04-S005)/DreamBooth(T04-S006)/Textual Inversion(T04-S007) → 候选心智模型「底座通用 + 轻量微调专属化」三件套。
- **"采样是质量/速度的旋钮"**：DDIM(T04-S012)/EDM(T04-S013)/CFG(T04-S011) → 候选 playbook「步数/采样器/CFG 三参数协同调」。
- **"架构正从 U-Net 收敛到 DiT"**：DiT(T04-S003)→SD3 MM-DiT(T04-S015)→Sora/可灵(T04-S019,S039) → 候选心智模型「新底座=DiT+flow matching」。

**智识谱系种子（流派分裂）**:
- **开源 SD 谱系（CompVis/Stability）**：奠基 LDM(T04-S002)→SDXL(T04-S016)→SD3(T04-S015)；可控/定制生态（ControlNet/LoRA/IP-Adapter）全部寄生于此；工具事实标准 ComfyUI(T04-S020)。当前代表底座：Flux.1(T04-S027)。开放、可微调、可拼装。
- **闭源 MJ 谱系（Midjourney）**：审美优先、参数化交互(`--sref`/`--cref`)、不可微调；canon 是官方文档(T04-S028)而非论文。
- **图像 vs 视频分裂**：图像侧 canon 成熟（论文密集）；视频侧分两支——开源 SVD/Video LDM(T04-S010,S018) vs 闭源 DiT 系 Sora/可灵/即梦(T04-S019,S039,S040)，后者无公开论文，canon 以技术博客/vendor 概览为主 → **视频侧 canon 信号偏弱、surrogate 依赖高**。
- **大厂闭源大模型谱系（OpenAI/Google）**：DALL·E 2(T04-S035)/Imagen(T04-S036)/Sora(T04-S019) 提供对照路线但不进创作者日常工具链。

**核心概念 → 候选 playbook**:
- 遇到"出图不可控/构图飘" → 上 ControlNet(T04-S004)/T2I-Adapter 锁结构。
- 遇到"角色跨图不一致" → DreamBooth/LoRA 训练(T04-S005,S006) 或免训练 IP-Adapter(T04-S009)/MJ `--cref`(T04-S028)。
- 遇到"提示不遵循/过曝" → 调 CFG scale(T04-S011)、换采样器/步数(T04-S012,S013)。
- 遇到"图生图改太多/太少" → 调 denoising strength(T04-S008)。
- 遇到"视频时序闪烁" → 理解时序层约束(T04-S018)，选首尾帧/可灵全注意力路线(T04-S039)。

**冷僻 / 信号薄弱**:
- 图像侧 canon 充实（论文 + 官方文档一手占比高，>50%）。
- **视频生成侧 canon 薄弱**：闭源主导（可灵/即梦/Sora 无同行评审论文），需用 vendor 概览(surrogate_primary)补；Phase 2.8 应标注"视频创作侧 mental model 部分基于 vendor 一面之词，需交叉校验"。
- **课程维度偏弱**：除 HF diffusion course 外，缺独立第三方系统课程进入一手 canon（多数实操教程在 YouTube/B站，非可机械验证一手）；ComfyUI examples 充当 surrogate 课程。
- HF course 的精确 last_updated 月份待二次核验。
