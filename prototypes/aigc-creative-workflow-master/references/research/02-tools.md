# Track 02 — Tools（AIGC 创作工作流 / 工具地图）

> locale=global · focus=operational + technical · 三层结构（必备 / 场景特化 / 新兴）+ 选型决策树 + 避坑清单
> 时效基准 last_checked 多为 2026-06-22。工具栈是本 skill 衰减最快的部分，每卡带具体日期。

## Source Manifest

| source_id | url | bucket | last_checked | author/host | one-line note |
|-----------|-----|--------|--------------|-------------|---------------|
| T02-S001 | https://github.com/Comfy-Org/ComfyUI | verified_primary | 2026-06-22 | Comfy-Org | ComfyUI 官方 repo（已迁 Comfy-Org），节点式底座 |
| T02-S002 | https://bfl.ai/blog/flux-2 | verified_primary | 2026-06-22 | Black Forest Labs | Flux.2 官方发布博客（vendor 一手） |
| T02-S003 | https://huggingface.co/black-forest-labs/FLUX.2-dev | verified_primary | 2026-06-22 | Black Forest Labs | Flux.2-dev 模型卡 + license |
| T02-S004 | https://github.com/black-forest-labs/flux2 | verified_primary | 2026-06-22 | Black Forest Labs | Flux.2 官方推理 repo |
| T02-S005 | https://bfl.ai/licensing | verified_primary | 2026-06-22 | Black Forest Labs | Flux open-weight 许可页（vendor 一手 license） |
| T02-S006 | https://docs.midjourney.com | verified_primary | 2026-06-22 | Midjourney | MJ 官方文档（版本/Draft/personalization） |
| T02-S007 | https://github.com/lllyasviel/Fooocus | verified_primary | 2026-06-22 | lllyasviel | Fooocus 官方 repo，极简单出图 |
| T02-S008 | https://github.com/lllyasviel/stable-diffusion-webui-forge | verified_primary | 2026-06-22 | lllyasviel | Forge 官方 repo，低显存优化的 A1111 fork |
| T02-S009 | https://github.com/AUTOMATIC1111/stable-diffusion-webui | verified_primary | 2026-06-22 | AUTOMATIC1111 | A1111 官方 repo，老牌 webui |
| T02-S010 | https://github.com/mcmonkeyprojects/SwarmUI | verified_primary | 2026-06-22 | mcmonkey | SwarmUI 官方 repo，ComfyUI 后端的友好前端 |
| T02-S011 | https://github.com/Mikubill/sd-webui-controlnet | verified_primary | 2026-06-22 | Mikubill/lllyasviel | ControlNet webui 扩展官方 repo |
| T02-S012 | https://github.com/cubiq/ComfyUI_IPAdapter_plus | verified_primary | 2026-06-22 | cubiq | IPAdapter ComfyUI 实现，参考图风格/人脸 |
| T02-S013 | https://github.com/Tencent-Hunyuan/HunyuanVideo | verified_primary | 2026-06-22 | Tencent | 混元视频开源 repo |
| T02-S014 | https://github.com/Wan-Video/Wan2.1 | verified_primary | 2026-06-22 | 阿里 Wan-Video | 通义万相 Wan2.1 开源视频 repo |
| T02-S015 | https://runwayml.com/research/introducing-runway-gen-4 | verified_primary | 2026-06-22 | Runway | Gen-4 官方发布页 |
| T02-S016 | https://openai.com/index/sora-2/ | verified_primary | 2026-06-22 | OpenAI | Sora 2 官方页 |
| T02-S017 | https://deepmind.google/models/veo/ | verified_primary | 2026-06-22 | Google DeepMind | Veo 官方模型页 |
| T02-S018 | https://blog.google/technology/ai/nano-banana-pro/ | verified_primary | 2026-06-22 | Google | Nano Banana Pro (Gemini 3 Pro Image) 官方发布 |
| T02-S019 | https://stability.ai/news | verified_primary | 2026-06-22 | Stability AI | SD/SD3.5 官方新闻（vendor 一手） |
| T02-S020 | https://civitai.com | secondary | 2026-06-22 | Civitai | 开源模型/LoRA 社区平台（平台站，非评测） |
| T02-S021 | https://klingai.com | secondary | 2026-06-22 | 快手 Kling | 可灵官网（平台入口） |
| T02-S022 | https://www.shareuhack.com/en/posts/ai-video-generation-tools-comparison-2026 | secondary | 2026-06-22 | ShareUHack | 9 视频工具实测对比（第三方评测，降级 secondary） |
| T02-S023 | https://wavespeed.ai/blog/posts/seedance-2-0-vs-kling-3-0-sora-2-veo-3-1-video-generation-comparison-2026/ | secondary | 2026-06-22 | WaveSpeed | 视频模型对比（厂商博客，第三方视角 secondary） |
| T02-S024 | https://civitai.com/articles/6024/using-a1111-why-not-swarmui-a-transition-guide | secondary | 2026-06-22 | Civitai 社区作者 | A1111→SwarmUI 迁移实操贴 |
| T02-S025 | https://ideogram.ai | secondary | 2026-06-22 | Ideogram | 文字渲染最强图像工具官网（平台入口） |
| T02-S026 | https://www.recraft.ai/blog/comparing-popular-and-high-performing-text-to-image-models-and-providers | verified_primary | 2026-06-22 | Recraft | Recraft 官方博客模型对比（vendor 一手，自家工具方） |
| T02-S027 | https://pxz.ai/blog/ideogram-vs-midjourney-2026 | secondary | 2026-06-22 | pxz.ai | Ideogram vs MJ 实测（评测站 /blog，lesson-37 诚实降 secondary） |
| T02-S028 | https://www.aimagicx.com/blog/ai-video-generation-showdown-2026 | secondary | 2026-06-22 | AI Magicx | 视频 showdown（评测站 /blog，lesson-37 诚实降 secondary） |
| T02-S029 | https://www.adobe.com/products/firefly.html | verified_primary | 2026-06-22 | Adobe | Firefly 官方产品页（商用赔付保障） |

---

## 总览（按 tier 分组）

### 必备（11 个，≥80% 创作者用）
| 工具 | 一句话 | Decay | Sources |
|------|--------|-------|---------|
| ComfyUI | 节点式生成底座，新模型最先落地、可复现工作流 | low | T02-S001 |
| Stable Diffusion / SDXL / SD3.5 | 开源图像底模生态根基，LoRA/ControlNet 全围绕它 | low | T02-S019 |
| Flux.1 (dev/schnell) | 当前开源图像质量标杆底模，文字渲染强 | medium | T02-S002,S003 |
| Midjourney v7 | 闭源易用美学天花板，零门槛出高质量图 | medium | T02-S006 |
| ControlNet | 结构控制（pose/depth/canny），可控生成的基石 | low | T02-S011 |
| LoRA | 轻量微调风格/角色/概念，社区资产标准格式 | low | T02-S020 |
| IPAdapter | 参考图驱动风格/人脸迁移，免训练换风格 | medium | T02-S012 |
| Civitai / Hugging Face | 模型/LoRA/工作流分发与下载枢纽 | low | T02-S020,S003 |
| 放大超分（ESRGAN/Ultimate SD Upscale/SUPIR） | 出图后必走的细节增强/放大环节 | low | T02-S001 |
| 可灵 Kling | 国产视频生成头部，性价比/中文生态强 | high | T02-S021,S023 |
| 即梦 Dreamina / Jimeng（Seedance 底座） | 字节系视频，多模态参考、国内可用 | high | T02-S022,S023 |

### 场景特化（10 个）
| 工具 | 一句话 | Decay | Sources |
|------|--------|-------|---------|
| Automatic1111 / Forge | 表单式 webui，扩展生态最全 / Forge 低显存提速 | medium | T02-S008,S009 |
| SwarmUI | ComfyUI 后端 + 友好前端，兼顾易用与可控 | medium | T02-S010,S024 |
| Fooocus | 极简 Midjourney 式体验，新手零配置出图 | medium | T02-S007 |
| AnimateDiff | SD 生态的图生/文生短动画运动模块 | high | T02-S001 |
| ReActor 换脸 | 一致性人脸替换，肖像/角色批量 | high | T02-S001 |
| CodeFormer / GFPGAN | 人脸修复，修崩坏五官 | medium | T02-S001 |
| SUPIR / Magnific | 重绘式超分，加细节而非纯放大 | medium | T02-S001 |
| Krea | 实时画布 / 多模型聚合 / 实时生成 | high | T02-S001 |
| Runway Gen-4 / Gen-4.5 | 专业可控视频：运动笔刷、角色一致性 | high | T02-S015,S022 |
| Adobe Firefly / Photoshop 生成填充 | 商用安全 + 设计工作流内嵌生成 | medium | T02-S018,S029 |
| Ideogram / Recraft | 文字渲染 / 矢量品牌设计特化图像 | medium | T02-S025,S026 |
| Hailuo / Luma / Vidu / Pika 中端视频 | 性价比中端视频，各有人物/HDR/动漫/B-roll 特长 | high | T02-S028 |

### 新兴（5 个，近 12 月起势）
| 工具 | 一句话 | Decay | Sources |
|------|--------|-------|---------|
| Flux.2 (dev/pro/klein) | 32B 旗舰开源图像底模，对标 Nano Banana/MJ | high | T02-S002,S003,S004 |
| Nano Banana Pro (Gemini 3 Pro Image) | 文字渲染/4K/推理式图像，闭源新王 | high | T02-S018 |
| Kling 3.0 / Sora 2 / Veo 3.1 | 视频代际跃迁：4K、原生音频、多镜头分镜 | high | T02-S016,S017,S023 |
| Wan 2.x（通义万相） | 开源视频底座，可本地跑、可商用友好 | high | T02-S014 |
| Seedance 2.0（即梦底座） | 多模态参考（图/视频/音/文）输入的视频范式 | high | T02-S022,S023 |

**§3 工具三层 sanity 行：必备 11 / 场景特化 12 / 新兴 5**

---

## 必备层

### 1. ComfyUI
- **One-liner**: 节点式（node graph）生成底座 — 把 loader→sampler→VAE→save 整条管线连起来，新架构最先落地、工作流可作为 JSON 复现分享。(evidence: [T02-S001])
- **Tier**: 必备
- **Maintainer**: Comfy-Org（原 comfyanonymous）— https://github.com/Comfy-Org/ComfyUI
- **License**: open / GPL-3.0
- **Maturity signals**: GitHub stars 117,882（2026-06-22）; last push 2026-06-22（极活跃）; activity healthy
- **典型场景**: 复杂多步管线（多 ControlNet + IPAdapter + LoRA 串联）; 新模型首发尝鲜（Flux/Wan/HunyuanVideo 常比 Forge 早数周支持）; 可复现的商业批产流水线。(evidence: [T02-S001])
- **不适合 / 替代**: 纯新手只想"打字出图"→ 节点学习曲线劝退，用 Fooocus / Midjourney；想要表单式快速参数调 → Forge。
- **近期变化（近 12 月）**: 迁移到 Comfy-Org 组织、ComfyUI Desktop 桌面版、Manager 生态成熟，Flux.2/Wan 视频节点跟进。
- **可信度**: high · **Decay risk**: low（已是开源 AIGC 事实底座，24+ 月稳定 < 20%）

### 2. Stable Diffusion / SDXL / SD3.5
- **One-liner**: 开源图像底模生态的根基 — 几乎所有 LoRA / ControlNet / IPAdapter 都先围绕 SD1.5/SDXL 训练，是社区资产的"指令集"。(evidence: [T02-S019])
- **Tier**: 必备
- **Maintainer**: Stability AI — https://stability.ai/news ; repo https://github.com/Stability-AI/generative-models
- **License**: SD1.5/SDXL 开放权重；SD3.5 走 Stability Community License（年收入门槛下免费商用）
- **Maturity signals**: SDXL 仍是 LoRA/ControlNet 生态最厚的底模（2026-06-22）；SD3.5 2024-10 发布
- **典型场景**: SDXL = 社区资产最丰富、ControlNet/LoRA 最齐的"默认底模"；SD1.5 = 老插件/低显存兜底；SD3.5 = 想留在 Stability 生态但要更新质量。
- **不适合 / 替代**: 追求最新画质 → Flux.1/Flux.2；要文字渲染 → Flux/Nano Banana。
- **近期变化**: 生态重心从 SD 向 Flux 转移，SDXL 因资产厚度仍是事实必备。
- **可信度**: high · **Decay risk**: low（SDXL 资产沉淀深，迁移成本高）

### 3. Flux.1 (dev / schnell)
- **One-liner**: 当前开源图像质量标杆底模，文字渲染与 prompt 遵循显著强于 SDXL；dev 非商用、schnell（Apache-2.0）可商用。(evidence: [T02-S002, T02-S005])
- **Tier**: 必备
- **Maintainer**: Black Forest Labs — https://bfl.ai
- **License**: Flux.1 [dev] = 非商用（FLUX.1 [dev] Non-Commercial License）；[schnell] = Apache-2.0（可商用）；[pro] = 仅 API/商用授权。(evidence: [T02-S005])
- **Maturity signals**: HF 模型卡持续高下载（2026-06-22）；ComfyUI/Forge 全面支持
- **典型场景**: 要开源 + 高画质 + 文字渲染；schnell 做快速本地预览/可商用出图；dev 做个人/研究高质量出图。
- **不适合 / 替代**: 接商单却用 dev → license 违规（见避坑）；显存 < 12GB 硬上 → 用量化版或退回 SDXL。
- **近期变化**: 被 Flux.2（32B）接棒为旗舰，但 Flux.1 仍是显存友好的主力。
- **可信度**: high · **Decay risk**: medium（被 Flux.2 部分替代，12-24 月内位置下移）

### 4. Midjourney v7
- **One-liner**: 闭源易用的美学天花板 — 零工程门槛产出高一致性高审美图，Draft 模式半价 10× 速度，v7 默认开 personalization。(evidence: [T02-S006])
- **Tier**: 必备
- **Maintainer**: Midjourney — https://docs.midjourney.com
- **License**: proprietary（订阅制，付费档位含商用权）
- **Maturity signals**: v7 于 2025-04-03 发布、2025-06-17 设为默认；Draft & Omni-Reference 上线（2026-06-22）。(evidence: [T02-S006])
- **典型场景**: 概念图/情绪板/海报快速产出；非技术创作者；审美下限高、无需调参。
- **不适合 / 替代**: 要精确结构控制 / 锁种子复现 / 本地批产 → ComfyUI + ControlNet（MJ 黑盒不可锁 seed 复现，见避坑）。
- **近期变化**: v7 架构 + Draft 模式 + Omni-Reference 参考图。
- **可信度**: high · **Decay risk**: medium（闭源迭代快，但产品护城河稳）

### 5. ControlNet
- **One-liner**: 结构控制基石 — 用 OpenPose/Depth/Canny 等预处理把参考图转成"约束指令"，让生成遵循构图/姿态/边缘。(evidence: [T02-S011])
- **Tier**: 必备
- **Maintainer**: Mikubill / lllyasviel — https://github.com/Mikubill/sd-webui-controlnet
- **License**: open
- **Maturity signals**: webui 扩展 17,853 stars（2026-06-22，last push 2024-08，进入稳态）；ComfyUI 侧持续更新 Flux ControlNet
- **典型场景**: 锁姿态/构图重绘；线稿上色；产品图换背景保结构；建筑/室内透视控制。
- **不适合 / 替代**: 只想换风格不改结构 → IPAdapter；底模换 Flux 需配对应 Flux-ControlNet（版本不匹配会失效，见避坑）。
- **近期变化**: 重心从 SD1.5/SDXL ControlNet 向 Flux ControlNet（如 XLabs/InstantX）迁移。
- **可信度**: high · **Decay risk**: low（可控生成的范式级组件）

### 6. LoRA
- **One-liner**: 低秩微调（Low-Rank Adaptation）— 用小文件给底模注入特定风格/角色/概念，是社区可分发的标准微调格式。(evidence: [T02-S020])
- **Tier**: 必备
- **Maintainer**: 概念由微软提出，生态在 Civitai/HF 分发 — https://civitai.com
- **License**: 训练框架开源；单个 LoRA 权重 license 各异（注意作者标注）
- **Maturity signals**: Civitai 上 LoRA 为下载量最大资产类目（2026-06-22）；Flux/SDXL LoRA 双轨繁荣
- **典型场景**: 固定角色一致性；复刻特定画风；产品/IP 训练专属风格；叠加多个 LoRA 调权重。
- **不适合 / 替代**: 一次性风格 → 用 IPAdapter 免训练；底模与 LoRA 不同代（SDXL LoRA 套 Flux）会无效（见避坑）。
- **近期变化**: Flux LoRA 训练（如 ai-toolkit）成主流，SDXL/Flux LoRA 并行。
- **可信度**: high · **Decay risk**: low

### 7. IPAdapter
- **One-liner**: 参考图驱动 — 用解耦交叉注意力把参考图的风格/人脸"注入"生成，免训练即可迁移风格或保持人物。(evidence: [T02-S012])
- **Tier**: 必备
- **Maintainer**: cubiq（ComfyUI 实现）— https://github.com/cubiq/ComfyUI_IPAdapter_plus
- **License**: open
- **Maturity signals**: 6,030 stars（2026-06-22，last push 2025-04）
- **典型场景**: 免训练风格迁移；人物面部一致性（配合 InstantID/PuLID）；参考图 + prompt 混合控制。
- **不适合 / 替代**: 要精确结构 → ControlNet；要长期稳定角色 → 训 LoRA。
- **近期变化**: Flux 时代被 PuLID-Flux / InstantX 等参考图方案部分接棒。
- **可信度**: high · **Decay risk**: medium（参考图控制方案迭代快）

### 8. Civitai / Hugging Face
- **One-liner**: 模型/LoRA/ControlNet/工作流的分发枢纽 — Civitai 偏创作社区资产与预览图，HF 偏权重托管与模型卡/license。(evidence: [T02-S020, T02-S003])
- **Tier**: 必备
- **Maintainer**: Civitai（https://civitai.com）/ Hugging Face（https://huggingface.co）
- **License**: 平台站；单资产 license 各异
- **Maturity signals**: 二者为开源视觉 AIGC 资产事实分发渠道（2026-06-22）
- **典型场景**: 找/下底模与 LoRA；看别人工作流与 prompt；HF 上确认模型 license 与权重。
- **不适合 / 替代**: 需企业合规审计 → 优先 HF 模型卡 license；国内访问 → liblib 哩布 / 吐司 Tusi 镜像生态。
- **近期变化**: Civitai NSFW 政策与支付合规波动；liblib/吐司 国内生态壮大。
- **可信度**: high · **Decay risk**: low

### 9. 放大超分（ESRGAN / Ultimate SD Upscale / SUPIR / Topaz）
- **One-liner**: 出图后的细节增强/放大环节 — Real-ESRGAN 纯放大、Ultimate SD Upscale 分块重绘加细节、SUPIR/Magnific 重绘式补细节、Topaz 商用。(evidence: [T02-S001])
- **Tier**: 必备
- **Maintainer**: 各开源 repo + Topaz/Magnific 商用
- **License**: ESRGAN/USDU open；Topaz/Magnific proprietary
- **Maturity signals**: ComfyUI/Forge 内置或插件化，放大是几乎每条出图链的固定收尾（2026-06-22）
- **典型场景**: 出图 → 放大到印刷/商用分辨率；SUPIR 给低清老图补细节。
- **不适合 / 替代**: 不想改内容只想纯放大 → 用 ESRGAN，别用 SUPIR（会改细节）。
- **可信度**: high · **Decay risk**: low

### 10. 可灵 Kling
- **One-liner**: 国产视频生成头部 — 性价比高（约 $0.10/sec）、中文生态强，Kling 3.0 上 4K 与多镜头分镜（Multi-Shot Storyboard）。(evidence: [T02-S021, T02-S023])
- **Tier**: 必备（视频侧）
- **Maintainer**: 快手 Kuaishou — https://klingai.com
- **License**: proprietary（订阅/积分，含商用授权）
- **Maturity signals**: Kling 3.0 于 2026-02-04 发布，原生 4K + 多镜头分镜（2026-06-22，业内对比来源）。(evidence: [T02-S023])
- **典型场景**: 中文 prompt 视频；图生视频运镜；高性价比批产短视频。
- **不适合 / 替代**: 要原生音频 + 极致 prompt 遵循 → Veo 3.1；要物理真实感 → Sora 2。
- **近期变化**: 3.0 多镜头分镜 + 4K，是当前国产性价比标杆。
- **可信度**: medium（视频代际数据多来自第三方对比）· **Decay risk**: high（视频代际半年一跳）

### 11. 即梦 Dreamina / Jimeng（Seedance 底座）
- **One-liner**: 字节系视频工具，国内可用、与抖音生态打通；底层 Seedance 2.0 支持图/视频/音/文多模态参考输入。(evidence: [T02-S022, T02-S023])
- **Tier**: 必备（视频侧·国产）
- **Maintainer**: 字节跳动 ByteDance
- **License**: proprietary
- **Maturity signals**: Seedance 2.0 多模态参考系统被列为当前最强可控之一（2026-06-22，第三方对比）。(evidence: [T02-S023])
- **典型场景**: 国内创作者批产；多模态参考精控；抖音/剪映工作流衔接。
- **不适合 / 替代**: 海外团队/英文生态 → Runway/Veo；要开源可本地 → Wan 2.x。
- **可信度**: medium · **Decay risk**: high

---

## 场景特化层

### 12. Automatic1111 / Forge
- **One-liner**: 表单式（非节点）webui — A1111 扩展生态最全、上手最快；Forge 是其低显存提速 fork（低端 GPU 提速可观）。(evidence: [T02-S009, T02-S008])
- **Tier**: 场景特化
- **Maintainer**: AUTOMATIC1111 / lllyasviel(Forge)
- **License**: open（AGPL-3.0 / 各扩展不一）
- **Maturity signals**: A1111 163,828 stars（2026-06-22，last push 2026-03）；Forge 12,749 stars（last push 2025-07，趋稳）
- **典型场景**: 想要表单调参不想学节点；依赖某个老 A1111 扩展；低显存机器用 Forge 提速。
- **不适合 / 替代**: 复杂多步管线 / 新模型首发 → ComfyUI；新模型支持上 A1111/Forge 普遍滞后于 ComfyUI 数周。(evidence: [T02-S001])
- **近期变化**: 重心向 ComfyUI/Forge Neo 迁移，A1111 更新放缓。
- **可信度**: high · **Decay risk**: medium

### 13. SwarmUI
- **One-liner**: ComfyUI 作后端 + 单 Generate 标签的友好前端 — 兼顾 A1111 的易用与 ComfyUI 的速度/可控。(evidence: [T02-S010, T02-S024])
- **Tier**: 场景特化
- **Maintainer**: mcmonkey — https://github.com/mcmonkeyprojects/SwarmUI
- **License**: open (MIT)
- **Maturity signals**: 4,233 stars（2026-06-22，last push 2026-06-17 活跃）
- **典型场景**: A1111 用户想升级又怕 ComfyUI 节点；要多 GPU/网格批量；既要简单又想偶尔进 ComfyUI 后端。
- **不适合 / 替代**: 极致复杂自定义节点 → 直接 ComfyUI。
- **可信度**: high · **Decay risk**: medium

### 14. Fooocus
- **One-liner**: 极简 Midjourney 式体验 — 零配置、隐藏复杂参数，新手打字即出图（基于 SDXL）。(evidence: [T02-S007])
- **Tier**: 场景特化
- **Maintainer**: lllyasviel — https://github.com/lllyasviel/Fooocus
- **License**: open (GPL-3.0)
- **Maturity signals**: 50,450 stars（2026-06-22，last push 2025-12，半稳态）
- **典型场景**: 纯新手第一周；只要好看不要控制；本地免费替代 Midjourney 体验。
- **不适合 / 替代**: 要 Flux/视频/精控 → ComfyUI（Fooocus 主打 SDXL，不追新模型）。
- **可信度**: high · **Decay risk**: medium（更新放缓）

### 15. AnimateDiff
- **One-liner**: SD 生态的运动模块 — 给 SD1.5/SDXL 文生/图生短动画（loop/运镜），ComfyUI 节点化。(evidence: [T02-S001])
- **Tier**: 场景特化
- **Maintainer**: 社区（guoyww 原作 + ComfyUI 节点）
- **License**: open
- **典型场景**: 风格化短循环动画；SD 资产复用做动效；不想用闭源视频 API。
- **不适合 / 替代**: 要长镜头/高一致性/物理真实 → Kling/Runway/Wan 专用视频模型。
- **可信度**: medium · **Decay risk**: high（被专用视频底模挤压）

### 16. ReActor 换脸
- **One-liner**: 一致性人脸替换 — 把目标脸贴到生成/已有图，肖像与角色批量统一。(evidence: [T02-S001])
- **Tier**: 场景特化
- **License**: open（注意合规/肖像权风险）
- **典型场景**: 角色多图统一脸；写真/电商模特换脸。
- **不适合 / 替代**: 要从根源保持人物 → InstantID/PuLID + LoRA；商用注意肖像授权。
- **可信度**: medium · **Decay risk**: high

### 17. CodeFormer / GFPGAN
- **One-liner**: 人脸修复 — 修崩坏五官、修复低清/糊脸，常作出图后处理一环。(evidence: [T02-S001])
- **Tier**: 场景特化
- **License**: open（CodeFormer 非商用条款需注意）
- **典型场景**: 小脸/远景脸修复；老照片修复；批量出图脸崩兜底。
- **不适合 / 替代**: 要整体加细节而非只修脸 → SUPIR。
- **可信度**: medium · **Decay risk**: medium

### 18. SUPIR / Magnific
- **One-liner**: 重绘式超分 — 不是纯放大，而是用扩散模型"想象"并补充细节；SUPIR 开源、Magnific 闭源商用。(evidence: [T02-S001])
- **Tier**: 场景特化
- **License**: SUPIR open / Magnific proprietary
- **典型场景**: 低清图补细节出印刷级；皮肤/材质/纹理增强。
- **不适合 / 替代**: 要忠实原图不改内容 → ESRGAN（重绘超分会"编造"细节）。
- **可信度**: medium · **Decay risk**: medium

### 19. Krea
- **One-liner**: 实时画布 + 多模型聚合 — 实时生成（边画边出）、一站调用多家闭源/开源模型。(evidence: [T02-S001])
- **Tier**: 场景特化
- **License**: proprietary（订阅）
- **典型场景**: 实时构思/草图到图；不想自己搭多模型环境；设计师快速迭代。
- **不适合 / 替代**: 要离线/可复现/批产 → ComfyUI。
- **可信度**: medium · **Decay risk**: high

### 20. Runway Gen-4 / Gen-4.5
- **One-liner**: 专业可控视频 — 运动笔刷（motion brush）、相机运镜、参考图驱动的角色一致性，pro favorite。(evidence: [T02-S015, T02-S022])
- **Tier**: 场景特化
- **Maintainer**: Runway — https://runwayml.com
- **License**: proprietary
- **Maturity signals**: Gen-4 / Gen-4.5 主打granular 创意控制（2026-06-22，第三方对比）。(evidence: [T02-S022])
- **典型场景**: 需要精细运镜与角色一致；广告/影视分镜级控制；英文专业工作流。
- **不适合 / 替代**: 高性价比批产 → Kling；要开源本地 → Wan 2.x。
- **可信度**: medium · **Decay risk**: high

### 21. Adobe Firefly / Photoshop 生成填充
- **One-liner**: 商用安全的设计内嵌生成 — Firefly 强调版权干净训练，Photoshop Generative Fill 把生成塞进既有设计工作流（已可接 Nano Banana Pro）。(evidence: [T02-S018])
- **Tier**: 场景特化
- **Maintainer**: Adobe
- **License**: proprietary（含商用赔付保障 indemnification）
- **典型场景**: 企业商用要版权可证；设计师在 PS/AE 里局部生成扩图；合规优先场景。
- **不适合 / 替代**: 要最高画质/最新模型 → Midjourney/Flux.2/Nano Banana 原生。
- **近期变化**: Firefly 接入 Google Gemini 3 (Nano Banana Pro) 等第三方模型。(evidence: [T02-S018])
- **可信度**: high · **Decay risk**: medium

### 22. Ideogram / Recraft（文字 + 矢量设计特化）
- **One-liner**: 图像设计特化 — Ideogram 文字渲染准确率约 90-95%（远高于 MJ 约 40%），擅 logo/海报/包装排版；Recraft 强在扁平矢量/图标与可导出矢量、品牌设计系统资产。(evidence: [T02-S027, T02-S026])
- **Tier**: 场景特化
- **Maintainer**: Ideogram（https://ideogram.ai）/ Recraft（https://www.recraft.ai）
- **License**: proprietary（含商用档；Ideogram 有可用免费层）
- **Maturity signals**: Ideogram V3 于 2025-03-26 发布、文字渲染约 90-95%；Recraft V3 在文生图竞技榜 ELO 排名靠前（2026-06-22，对比/vendor 来源）。(evidence: [T02-S027, T02-S026])
- **典型场景**: 要图内清晰可读文字（海报/包装/logo）→ Ideogram；要矢量/图标/品牌系统可导出 → Recraft；艺术审美 → 仍回 Midjourney。
- **不适合 / 替代**: 要艺术风格/情绪图 → Midjourney；要开源可复现 → Flux + ComfyUI。Nano Banana Pro 在文字渲染上已成强竞品。
- **可信度**: medium · **Decay risk**: medium

### 23. Hailuo / Luma / Vidu / Pika（中端视频，差异化特长）
- **One-liner**: 中端性价比视频层 — Hailuo(MiniMax) 强人物表情/口型+移动端，Luma Ray3 首个原生 16-bit HDR+音乐视频，Vidu 偏动漫/动画系列+原生音频，Pika 偏 lifestyle/产品 B-roll 风格化。(evidence: [T02-S028])
- **Tier**: 场景特化
- **Maintainer**: MiniMax / Luma / 生数 Shengshu / Pika
- **License**: proprietary
- **Maturity signals**: 市场 2026 分层为顶层(Runway/Veo/Kling/Sora) 与中层(Hailuo/Luma/Pika)；Luma Ray3.14 2026-01-26 更新、Vidu Q3 2026-01 16s 原生音视频（第三方对比）。(evidence: [T02-S028])
- **典型场景**: 人物/口型 → Hailuo；音乐视频/HDR → Luma；动漫连续短片 → Vidu；风格化 B-roll/社媒短内容 → Pika。
- **不适合 / 替代**: 高端品牌片/复杂连续性 → Kling/Veo/Runway；要开源 → Wan/Hunyuan。
- **可信度**: medium · **Decay risk**: high

---

## 新兴层（近 12 月起势 · 默认 Decay high · stability: experimental）

### 24. Flux.2 (dev / pro / klein)
- **One-liner**: 32B flow-matching 旗舰开源图像底模 — 对标 Nano Banana Pro / Midjourney，单/多参考图编辑，文字渲染与一致性大升。(evidence: [T02-S002, T02-S003])
- **Tier**: 新兴
- **Maintainer**: Black Forest Labs — https://github.com/black-forest-labs/flux2
- **License**: [dev] 非商用；[pro] API 商用；[klein] 含 Apache-2.0 的 4B 变体 + 非商用 9B 变体。(evidence: [T02-S003, T02-S005])
- **Maturity signals**: 2025-11-25 发布；官方 repo 2,419 stars（2026-06-22，created 2025-11-24）。(evidence: [T02-S004])
- **典型场景**: 要顶级开源画质 + 多参考图编辑；klein-4B 做可商用本地出图；pro 走 API 商用。
- **不适合 / 替代**: 显存吃紧（32B 很重）→ 用 klein 或退 Flux.1；要"打字编辑"对话式 → Nano Banana Pro。
- **可信度**: high（vendor 一手）· **Decay risk**: high（新兴层默认，迭代快）

### 25. Nano Banana Pro (Gemini 3 Pro Image)
- **One-liner**: 闭源新王 — 基于 Gemini 3 Pro 的推理式图像，文字渲染最强、支持 1K/2K/4K，可"对话式"编辑。(evidence: [T02-S018])
- **Tier**: 新兴
- **Maintainer**: Google DeepMind — https://blog.google/technology/ai/nano-banana-pro/
- **License**: proprietary（Gemini app / API / Vertex AI）
- **Maturity signals**: 2025-11-20 全球上线；接入 Firefly/Photoshop、Workspace（2026-06-22）。(evidence: [T02-S018])
- **典型场景**: 海报/信息图要清晰可读文字；4K 印刷级；自然语言迭代编辑；不想搭本地环境。
- **不适合 / 替代**: 要开源可复现/可锁种子 → Flux.2；要离线 → 本地底模。
- **可信度**: high · **Decay risk**: high

### 26. Kling 3.0 / Sora 2 / Veo 3.1（视频代际跃迁）
- **One-liner**: 视频近 12 月代际跳变 — Kling 3.0 多镜头分镜+4K（性价比$0.10/s）、Veo 3.1 原生音频+4K+prompt 遵循、Sora 2 物理真实标杆。(evidence: [T02-S023, T02-S017, T02-S016])
- **Tier**: 新兴
- **Maintainer**: 快手 / Google / OpenAI
- **License**: proprietary
- **Maturity signals**: Kling 3.0 2026-02-04 发布；Sora 2 web/app 计划 2026-04-26 下线（API 2026-09-24 下线）—— 新兴层不稳定性的活例。(evidence: [T02-S023])
- **典型场景**: Veo=叙事+原生音频; Sora 2=物理运动真实; Kling 3.0=性价比+多镜头分镜。
- **不适合 / 替代**: 要开源本地 → Wan 2.x；Sora 即将下线，勿押单一闭源管线（见避坑）。
- **可信度**: medium（多为第三方对比 + 官方页混合）· **Decay risk**: high

### 27. Wan 2.x（通义万相）
- **One-liner**: 阿里开源视频底座 — 可本地跑、商用相对友好，是开源视频侧的"SD 时刻"。(evidence: [T02-S014])
- **Tier**: 新兴
- **Maintainer**: 阿里 Wan-Video — https://github.com/Wan-Video/Wan2.1
- **License**: open（Apache-2.0 系，商用相对友好，以 repo 标注为准）
- **Maturity signals**: Wan2.1 16,303 stars（2026-06-22，created 2025-02-25，last push 2026-03，活跃）
- **典型场景**: 要开源/可本地/可商用的视频；ComfyUI 接入做可控视频管线；不想锁闭源 API。
- **不适合 / 替代**: 要顶级画质即开即用 → Kling/Veo；显存不够 → 量化版/云。
- **可信度**: high · **Decay risk**: high（开源视频迭代极快）

> Seedance 2.0（即梦底座）作为多模态参考视频范式亦属新兴信号，已并入必备层即梦卡（#11）+ 视频对照表说明。(evidence: [T02-S023])

---

## 国产 vs 海外工具对照（诚实标差异，不捧不踩）

| 维度 | 国产代表 | 海外代表 | 诚实差异 |
|------|---------|---------|---------|
| 图像闭源易用 | 无对等"美学天花板"，靠 liblib/吐司 + Flux/SDXL | Midjourney v7 | MJ 审美下限/一致性仍领先；国产以开源底模 + 工作流补 |
| 图像开源底模 | 通义/腾讯混元图像 | Flux.2 / SD3.5 | 开源图像底模仍以 Flux/SD 生态最厚（LoRA/ControlNet） |
| 图像闭源新王 | — | Nano Banana Pro / Flux.2 pro | 文字渲染/4K/推理式编辑当前海外领先 (evidence: [T02-S018]) |
| 视频生成 | 可灵 Kling / 即梦(Seedance) / 海螺 Hailuo / Vidu / Wan | Runway / Sora / Veo / Luma / Pika | 国产性价比 + 中文 prompt + 国内可用占优；海外 Veo 原生音频/prompt 遵循、Sora 物理真实占优 (evidence: [T02-S023]) |
| 开源视频底座 | Wan 2.x / HunyuanVideo（均国产开源，反占优） | LTX / Mochi | 开源视频底座国产（阿里 Wan/腾讯混元）反而领先 (evidence: [T02-S013, T02-S014]) |
| 社区/资产分发 | liblib 哩布 / 吐司 Tusi / openart | Civitai / Hugging Face | HF/Civitai 全球资产最厚；liblib/吐司 国内访问与中文生态好 |
| 合规/访问 | 国内直连、实名、内容审查 | 需网络条件、版权政策各异 | 商单选型须按交付地法务 + license 双重判断 |

---

## 选型决策树

### 决策树 A：图像 vs 视频 vs 可控性 —— 你的核心需求是什么？

#### Branch 1：纯新手 / 只要好看不要控制（demo / 情绪板阶段）
→ 推荐：**Midjourney v7**（零门槛、审美下限高、Draft 半价快出）或 **Nano Banana Pro**（对话式 + 文字渲染）。(evidence: [T02-S006, T02-S018])
→ 想本地免费同体验：**Fooocus**（SDXL 极简）。(evidence: [T02-S007])
→ 不推荐：ComfyUI（节点劝退，rotation cost 高）。

#### Branch 2：要可控 / 可复现 / 批产（已知风格、要稳定交付）
##### Branch 2a：瓶颈在"结构/姿态/构图"
→ **ComfyUI + ControlNet**（OpenPose/Depth/Canny 锁结构）。(evidence: [T02-S001, T02-S011])
##### Branch 2b：瓶颈在"风格/角色一致性"
→ 一次性风格：**IPAdapter**（免训练）；长期固定角色：训 **LoRA**；人脸一致：InstantID/PuLID。(evidence: [T02-S012, T02-S020])
##### Branch 2c：只想表单调参不学节点
→ **Forge**（低显存提速）或 **SwarmUI**（ComfyUI 后端 + 友好前端）。(evidence: [T02-S008, T02-S010])

#### Branch 3：图像底模怎么选（开源 vs 闭源 / 商用 license）
##### 3a：要商用 + 合规可证 → **Adobe Firefly**（赔付保障）或 **Flux schnell**(Apache-2.0) / **Flux.2 klein-4B** / **SD3.5**（按收入门槛）。(evidence: [T02-S005, T02-S018])
##### 3b：要最高开源画质且非商用 OK → **Flux.2 dev** / **Flux.1 dev**。(evidence: [T02-S002, T02-S003])
##### 3c：要最厚 LoRA/ControlNet 资产生态 → **SDXL**（资产沉淀最深）。(evidence: [T02-S020])
##### 3d：要图内清晰可读文字（logo/海报/包装）→ **Ideogram**（约 90-95% 文字准确）或 **Nano Banana Pro**；要可导出矢量/品牌系统 → **Recraft**。(evidence: [T02-S027, T02-S026, T02-S018])

#### Branch 4：做视频
##### 4a：高性价比 + 中文 + 国内可用 → **可灵 Kling 3.0** / **即梦(Seedance)**。(evidence: [T02-S021, T02-S023])
##### 4b：要精细运镜 / 角色一致 / 专业控制 → **Runway Gen-4.5**。(evidence: [T02-S015])
##### 4c：要原生音频 + prompt 遵循 + 4K 叙事 → **Veo 3.1**；要物理真实 → **Sora 2**（注意 2026-04 下线计划，勿单押）。(evidence: [T02-S016, T02-S017, T02-S023])
##### 4d：要开源 / 本地 / 可商用 → **Wan 2.x**（阿里）/ **HunyuanVideo**（腾讯）。(evidence: [T02-S013, T02-S014])
##### 4e：中端性价比 + 细分特长 → 人物/口型 **Hailuo**；音乐视频/HDR **Luma Ray3**；动漫连续 **Vidu**；风格化 B-roll/社媒 **Pika**。(evidence: [T02-S028])

#### Branch 5：显卡门槛兜底（显存约束优先级最高）
→ < 8GB：SD1.5 + Forge / 用闭源 API（MJ/Kling）；8–12GB：SDXL/Flux 量化版 + Forge；16GB+：Flux.2/Wan 本地 + ComfyUI。底层硬约束，先按显存再谈画质。(evidence: [T02-S001, T02-S008])

---

## 避坑清单（≥5）

- ❌ **以为换个更大的底模就解决一切**：画质问题常出在 prompt / ControlNet 约束 / 放大链条，而非底模。32B 的 Flux.2 在弱 prompt 下不一定胜过调好的 SDXL 工作流。(evidence: [T02-S001, T02-S002])
- ❌ **Flux.1 dev / Flux.2 dev 非商用却拿去接商单**：dev 系是 Non-Commercial License，商用要 schnell(Apache-2.0) / klein-4B(Apache-2.0) / pro(API) / 企业授权，否则 license 违规。(evidence: [T02-S005, T02-S003])
- ❌ **闭源黑盒当可复现管线**：Midjourney / Nano Banana 不可锁种子精确复现，批产/版本回溯/法务追溯需求要用开源 + 固定 seed 的 ComfyUI 链。(evidence: [T02-S006, T02-S001])
- ❌ **显存不够硬上大模型**：12GB 显存硬跑 32B Flux.2 全精度会 OOM 或极慢，先选量化版/退 Flux.1/SDXL，或走云 API。决策树 Branch 5 是硬约束。(evidence: [T02-S001])
- ❌ **插件/LoRA/ControlNet 版本与底模不匹配**：SDXL 的 LoRA/ControlNet 套不到 Flux，换底模必须换配对的 Flux-ControlNet / Flux-LoRA，否则静默失效或报错。(evidence: [T02-S011, T02-S020])
- ❌ **把单一闭源视频模型当永久基础设施**：OpenAI 已宣布 Sora web/app 2026-04-26 下线、API 2026-09-24 下线 —— 视频闭源代际半年一跳，关键管线要留开源(Wan/Hunyuan)或多供应商退路。(evidence: [T02-S023, T02-S014])
- ❌ **新模型支持指望 A1111/Forge 即时跟进**：新架构普遍先在 ComfyUI 落地、A1111/Forge 滞后数周，追新就直接用 ComfyUI。(evidence: [T02-S001])

---

## Phase 2 提炼提示

**反复出现 ≥3 source 都强调的"工具选型原则"**（候选 playbook 规则）：
- 底模 ≠ 一切：可控性来自 ControlNet/LoRA/IPAdapter 的"约束三件套" + 放大链条，而非单纯换大模型（出现于 T02-S001 / S002 / S011）
- License 是商用第一道闸：dev=非商用、schnell/klein-4B=Apache、pro=API、Firefly=赔付 —— 接商单先查 license（T02-S005 / S003 / S018）
- 显存优先于画质：选型先按显卡门槛分支再谈模型（T02-S001 / S008）
- 闭源易用 vs 开源可复现是根本张力：要复现/批产/法务追溯 → 开源+锁 seed；要审美下限/速度 → 闭源（T02-S006 / S001）

**显著的工具流派分裂**（候选 智识谱系条目）：
- **节点精控派**（ComfyUI / SwarmUI；可复现工作流、新模型最先落地、商业批产）vs **表单/极简易用派**（Fooocus / Forge / A1111 / Midjourney / Nano Banana；快、审美下限高、黑盒）。核心权衡：可控性/可复现 ↔ 上手成本/速度。
- **开源底模派**（SD/SDXL/Flux/Wan/Hunyuan；可本地、可锁 seed、license 可控）vs **闭源 API 派**（MJ/Nano Banana/Kling/Veo/Sora；零运维、画质即开即用、不可复现、有下线风险）。
- **图像侧成熟**（SD/Flux 生态厚）vs **视频侧高速代际跳变**（半年一代，Decay 普遍 high）—— 同一 skill 内两个子领域成熟度差异大。

**新兴工具信号**：
- 当前活跃/上升新工具：5（Flux.2 / Nano Banana Pro / Kling3-Sora2-Veo3 视频代际 / Wan 2.x / Seedance 2.0）
- 出现→主流速度估计：图像底模约 3-6 个月（Flux→Flux.2、Nano Banana 上线即接入 Firefly）；视频约 4-6 个月一代（Kling 半年一大版）

**薄弱 / 信号薄弱维度**：
- 必备层 11 个（≥3 达标）、场景特化 12、新兴 5，三层均充实，非冷僻行业。
- 较弱处：视频侧"采用率"硬数据多来自第三方对比文（secondary），缺权威 survey 的精确市占；可信度多为 medium，须标"业内估计 + 来源年份"。
- ControlNet/IPAdapter 等控制组件在 Flux 时代正被 PuLID/InstantX 等接替，谱系处于迁移期，下次 refresh 重点核对参考图/人脸控制方案的当前主流。
