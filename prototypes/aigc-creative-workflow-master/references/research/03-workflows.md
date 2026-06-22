# Track 03 — Workflows: AIGC 创作工作流 / AIGC Creative Workflow

> locale = global · focus = operational（工作流是本行最核心）
> Phase 1 Track 03 (Workflows). 行业 = 生成式 AI 视觉创作（图像 + 视频，创作侧）。
> 每个 workflow 三段分清：入门 SOP / 资深路径（skip·optimize·add）/ 近期变化（带 Decay risk + last_updated）。
> 工作流是 master skill 衰减最快的部分；视频/工具版本类 Decay high，采样/可控生成原理类 Decay low。

## Source Manifest

| source_id | url | bucket | last_checked | author/host | one-line note |
|-----------|-----|--------|--------------|-------------|---------------|
| T03-S001 | https://docs.comfy.org/tutorials/basic/text-to-image | verified_primary | 2026-06-22 | Comfy-Org | 官方 T2I 教程：Load Checkpoint→KSampler→VAE Decode 全链 |
| T03-S002 | https://docs.comfy.org/tutorials/basic/inpaint | verified_primary | 2026-06-22 | Comfy-Org | 官方 inpaint 教程：mask + denoise |
| T03-S003 | https://docs.comfy.org/specs/workflow_json | verified_primary | 2026-06-22 | Comfy-Org | workflow JSON 规范（节点图/连接/参数序列化） |
| T03-S004 | https://github.com/Comfy-Org/workflow_templates | verified_primary | 2026-06-22 | Comfy-Org | 官方模板工作流 repo（复用基准） |
| T03-S005 | https://comfyanonymous.github.io/ComfyUI_examples/controlnet/ | secondary | 2026-06-22 | comfyanonymous | 官方示例页（github.io 个人页，降 secondary）ControlNet/T2I-Adapter 示例 |
| T03-S006 | https://github.com/comfyanonymous/ComfyUI | verified_primary | 2026-06-22 | comfyanonymous | ComfyUI 项目根（节点式范式一手） |
| T03-S007 | https://comfyui-wiki.com/en/tutorial/advanced/how-to-install-and-use-controlnet-models-in-comfyui | secondary | 2026-06-22 | ComfyUI Wiki | ControlNet 安装与权重调试教程（聚合站） |
| T03-S008 | https://stable-diffusion-art.com/controlnet/ | secondary | 2026-06-22 | Andrew (SD Art) | ControlNet 完整指南（教程站，诚实 secondary） |
| T03-S009 | https://learn.thinkdiffusion.com/flux-lora-training-with-kohya/ | secondary | 2026-06-22 | ThinkDiffusion | Flux LoRA 训练实操（厂商 learn 站，secondary） |
| T03-S010 | https://github.com/ostris/ai-toolkit | verified_primary | 2026-06-22 | Ostris | ai-toolkit 官方 repo（Flux.2/Qwen LoRA 训练主流工具一手） |
| T03-S011 | https://github.com/cubiq/ComfyUI_Workflows/blob/main/in-out_painting/README.md | verified_primary | 2026-06-22 | cubiq (Matteo) | IPAdapter 作者本人 in/out-painting workflow + 原理说明 |
| T03-S012 | https://docs.midjourney.com | verified_primary | 2026-06-22 | Midjourney | MJ 官方文档总入口 |
| T03-S013 | https://docs.midjourney.com/hc/en-us/articles/36285124473997-Omni-Reference | verified_primary | 2026-06-22 | Midjourney | Omni Reference (--oref/--ow) 官方文档 |
| T03-S014 | https://docs.midjourney.com/hc/en-us/articles/32180011136653-Style-Reference | verified_primary | 2026-06-22 | Midjourney | Style Reference (--sref/--sw) 官方文档 |
| T03-S015 | https://docs.midjourney.com/hc/en-us/articles/32162917505293-Character-Reference | verified_primary | 2026-06-22 | Midjourney | Character Reference (--cref/--cw) 官方文档 |
| T03-S016 | https://www.atlascloud.ai/blog/guides/kling-ai-video-prompt-guide | secondary | 2026-06-22 | Atlas Cloud | Kling prompt 五段结构指南（/blog SEO，lesson-37 诚实降 secondary） |
| T03-S017 | https://www.ambienceai.com/tutorials/kling-prompting-guide | secondary | 2026-06-22 | Ambience AI | Kling 2026 camera/negative prompt 指南 |
| T03-S018 | https://curiousrefuge.com/ai-filmmaking | secondary | 2026-06-22 | Curious Refuge | 全球首个 AI 影视课程（方法论originator，vendor 课程页 secondary） |
| T03-S019 | https://curiousrefuge.com/blog/ai-filmmaking-tools-for-filmmakers | secondary | 2026-06-22 | Curious Refuge | 60 AI 影视工具清单（方法论 originator 自述 pipeline） |
| T03-S020 | https://comfyui-wiki.com/en/tutorial/basic/how-to-outpaint-an-image-in-comfyui | secondary | 2026-06-22 | ComfyUI Wiki | outpaint 教程（Pad Image for Outpainting 节点） |
| T03-S021 | https://docs.comfy.org/tutorials/basic/upscale | verified_primary | 2026-06-22 | Comfy-Org | 官方 upscale/放大教程 |
| T03-S022 | https://docs.midjourney.com/hc/en-us/articles/32040250122637-Draft-Mode | verified_primary | 2026-06-22 | Midjourney | Draft Mode（半价 10× 速度）官方文档 |
| T03-S023 | https://app.klingai.com/global/quickstart/klingai-video-3-model-user-guide | secondary | 2026-06-22 | Kuaishou Kling | 可灵 Video 3.0 官方用户指南（vendor 一手；app 子域自动降 secondary）：多镜头分镜/首尾帧/运动笔刷 |

> 与前两 wave 关联：工具一手大量来自 Track 02（ComfyUI/ControlNet/IPAdapter/LoRA/Kling repo 与官方页），figure 叙事来自 Track 01（Scott Detweiler ComfyUI 教学、Caleb Ward/Curious Refuge AI 影视、Bilawal Sidhu「工具拼盘破坏 flow」、秋葉 SD 整合包）。

---

## 总览（按 decay risk 分组）

### High decay (12-month-class) — 3 个
| Workflow | Trigger | Output | Last_updated | 资深差异 |
|---------|---------|--------|-------------|---------|
| 6. 图生视频 / 文生视频（Kling/即梦/Runway） | 要把静帧变成有运镜的镜头 | 3-10s 视频 clip（含运镜/首尾帧/可选音轨） | 2026-06-22 | 先出高质量首帧再 I2V；运镜用模型内置控制而非堆 prompt；多 clip 锁同一参考保一致 |
| 7. AI 短片 / 分镜全流程（Curious Refuge 式） | 要做一支 1-3min AI 短片 | 成片（脚本→分镜→关键帧→视频→后期混音） | 2026-06-22 | 关键帧先用快模型（Z-Image）blocking；按 shot 选模型；一致性靠角色 sheet + 参考锁 |
| 8. Midjourney 闭源易用出图流（sref/cref/oref） | 要零工程门槛出高审美图 + 风格/角色一致 | 高一致性成图组 | 2026-06-22 | Draft 模式半价探方向；--sref 锁风格码 + --oref 锁角色；权重(--sw/--ow)精调 |

### Medium decay — 3 个
| Workflow | Trigger | Output | Last_updated | 资深差异 |
|---------|---------|--------|-------------|---------|
| 3. 角色/风格一致性（LoRA + IPAdapter/参考图） | 需要同一角色/画风跨多图稳定 | 可复用的 LoRA 文件 或 免训练参考链 | 2026-06-22 | 免训练优先（IPAdapter/InstantID）能不练就不练；练 LoRA 时打标质量 > step 数；底模代际配对 |
| 4. 图生图 + 局部重绘修图（I2I + inpaint + 修脸） | 出图有瑕疵 / 要改局部 / 换脸 | 修好的成图（手/脸/局部修复 + 放大） | 2026-06-22 | denoise 幅度精控；用专用 inpaint 模型；Face Detailer/换脸自动化收尾 |
| 5. ComfyUI 节点工作流搭建与复用（工程链） | 要可复现/可批产/可分享的管线 | 参数化的 workflow JSON + 批量队列产物 | 2026-06-22 | 模板起步不从零搭；subgraph 模块化；API 队列批产替手点 Queue |

### Low decay — 2 个
| Workflow | Trigger | Output | Last_updated | 资深差异 |
|---------|---------|--------|-------------|---------|
| 1. 单张精控出图（文生图 T2I 全链） | 有一个画面概念要落地成图 | 一张可交付的成图 + 可复现参数 | 2026-06-22 | 低分辨率小批量探方向再放大；负面/参数留默认少折腾；锁 seed 做变体 |
| 2. 可控生成（ControlNet 控构图/姿态/线稿） | 要让生成遵循指定构图/姿态/边缘 | 结构受控的成图 | 2026-06-22 | 选对预处理器是关键；control weight + start/end 百分比调；多 ControlNet 叠加 |

---

## Workflow 卡片

### 1. 单张精控出图（文生图 T2I 全链）(Decay risk: low) last_updated: 2026-06-22

- **One-liner**: 从一个画面概念，经选底模→写 prompt 调参数→出图筛方向→迭代→放大精修，落地成一张可交付且可复现的成图。从「脑子里的画面」到「磁盘上带参数的成图」。
- **Trigger**: 有一个具体画面概念（海报/插画/概念图）要生成；或客户给了文字 brief 要出视觉。
- **Output**: 一张成图 + 完整可复现参数（底模 / prompt / seed / CFG / 采样器 / 步数 / 放大链），供回溯与改稿。
- **入门 SOP（minimum viable steps）**:
  1. **选底模**：按需求选 checkpoint（SDXL 资产最厚 / Flux 画质与文字强 / SD1.5 低显存兜底）。Load Checkpoint 节点加载。(evidence: [T03-S001])
  2. **写 prompt**：正面 prompt（主体+风格+细节+质量词）、负面 prompt 分别进两个 CLIP Text Encode 节点。(evidence: [T03-S001])
  3. **设画布与参数**：Empty Latent 设分辨率（SDXL 用 1024 系），KSampler 设 steps（约 25 起步）、CFG（7 左右）、采样器（Euler/DPM++）、scheduler、seed、denoise=1.0。(evidence: [T03-S001])
  4. **首轮出图筛方向**：先小批量/随机 seed 跑几张，挑构图与方向对的那张（「抽卡」阶段）。
  5. **迭代收敛**：锁定满意 seed，微调 prompt 措辞/权重、CFG、采样器；逐层把随机性收掉。
  6. **放大精修**：VAE Decode 后接放大链（ESRGAN 纯放大 / Ultimate SD Upscale 分块重绘加细节 / SUPIR 重绘补细节）到交付分辨率。(evidence: [T03-S021])
  7. **留参数交付**：Save Image（PNG 内嵌工作流元数据），记录全套参数。
  - **每一步跳过的后果**：跳选底模直接用默认 → 风格/画质与需求错配，白跑后面全部步骤；跳负面/参数直接默认 → 多数情况能出图但脸/手崩、风格漂移；跳首轮筛方向直接高分辨率精修 → 在错误构图上浪费算力（一张 4K 重绘是 512 试错的 10-50 倍耗时）；跳放大直接交付 → 分辨率不足无法印刷/商用；跳留参数 → 客户要改稿时无法复现原图（lesson：闭源黑盒不可锁 seed，更要靠记录）。
- **资深路径（差异点）**：
  - **skip**：资深人**跳过**「在高分辨率上试错」—— 永远先在低分辨率（512/768）小批量探方向，方向对了才放大；也常**跳过**堆砌一长串质量词/负面 prompt（Flux/SDXL 时代很多默认即可，过度 prompt 反而过拟合）。
  - **optimize**：**优化**「seed 管理」—— 找到好构图就锁 seed，只动一个变量做 A/B（改 prompt 一处或换采样器），而非每次全随机；**优化** CFG 区间（知道 CFG>15 是 prompt 偏执、steps>50 边际递减，不盲目拉高）。(evidence: [T03-S001])
  - **add**：资深人**额外做**「分阶段放大 + 局部 detailer」（先整体放大再单独 Face Detailer 修脸），以及**额外**给交付图嵌入/归档完整参数做版本回溯。
- **近期变化（近 12 个月）**：
  - 2025-11 起，由 Flux.2（32B）/ Nano Banana Pro / Z-Image 等新底模推动，「写很长质量词 + 负面 prompt」的老 SD1.5 习惯在新底模上收益骤降，自然语言长句 prompt 遵循更好 —— 入门 SOP 的 step 2/3 正在简化。(evidence: [T03-S001])
  - 触发事件类型：新模型。当前采用率：新底模用户普遍少写负面 prompt；老 SDXL 资产用户仍保留。
- **典型耗时**：入门 SOP 约 30min–2h（含试错）；资深路径 10–30min（方向判断快、试错少）。
- **关键工具（Track 02）**：ComfyUI / Forge / A1111（必备）；SDXL/Flux 底模（必备）；ESRGAN/USDU/SUPIR 放大（必备收尾）。
- **关键人物（Track 01）**：Scott Detweiler（ComfyUI 教学，逐节点讲 KSampler 参数）；秋葉aaaki（SD 整合包，中文圈入门）。
- **常见失败模式**：
  - **在错误构图上精修浪费算力**：没先小图筛方向就 4K 放大 —— 先在 512/768 出 4-8 张筛方向，方向对再放大，省 80% 算力。
  - **CFG/steps 盲目拉满**：CFG 拉到 20+ 出油腻过曝、steps 拉到 80 纯浪费时间零收益 —— CFG 守 5-8、steps 守 20-30，画质问题先查 prompt 与放大链而非拉参数。
  - **没记参数无法复现**：交付后客户要改一处，原图 seed/参数没存 —— 用 ComfyUI PNG 内嵌元数据或建立参数台账，每张交付图存全参数。
- **来源**：
  - [Primary] ComfyUI 官方 T2I 教程: T03-S001（collected 2026-06-22）
  - [Primary] ComfyUI 官方 upscale 教程: T03-S021
  - [Reference] Scott Detweiler ComfyUI 教学频道（Track 01-S013）
- **Last_updated**: 2026-06-22 · **Decay risk**: low（采样/出图全链是范式级原理，24+ 月稳定；唯 prompt 写法随底模微调）

---

### 2. 可控生成（ControlNet 控构图/姿态/线稿）(Decay risk: low) last_updated: 2026-06-22

- **One-liner**: 用垫图经预处理器（openpose/depth/canny/lineart）抽出「结构指令」，约束扩散过程遵循指定构图/姿态/边缘。从「随机抽卡」到「锁结构出图」。
- **Trigger**: 要求生成必须遵循某个姿态/构图/线稿/透视（如锁人物动作、保产品轮廓换背景、线稿上色、建筑透视）。
- **Output**: 结构受控、内容可换风格的成图。
- **入门 SOP**:
  1. **准备垫图**：找/拍一张含目标结构的参考图（姿态参考、线稿、深度场景）。
  2. **选预处理器并预处理**：按需求选 —— 人体姿态用 OpenPose、空间结构用 Depth、保边缘用 Canny、线稿用 Lineart/Scribble。必须先跑预处理器把图转成控制图（ControlNet Apply 不会自动转）。(evidence: [T03-S005, T03-S008])
  3. **加载配对 ControlNet 模型**：ControlNetLoader 加载与底模代际匹配的 ControlNet（SDXL 底模配 SDXL ControlNet、Flux 配 Flux ControlNet）。(evidence: [T03-S005])
  4. **接入生成链**：Apply ControlNet 把控制图注入 KSampler 的条件，设 strength（控制权重）。(evidence: [T03-S007])
  5. **调控制权重出图**：从默认权重起，太松结构跑偏、太紧画质僵硬，迭代调到平衡。
  6. **放大精修交付**（同 workflow 1 收尾）。
  - **每一步跳过的后果**：跳预处理直接喂原图 → ControlNet 不识别（喂彩色图给 depth 通道得不到深度约束），控制失效；跳代际配对（SDXL ControlNet 套 Flux）→ 静默失效或报错（lesson Track 02 避坑）；跳权重调试用满权重 → 结构是锁住了但画质僵硬、细节丢失；跳放大 → 同 workflow 1。
- **资深路径（差异点）**：
  - **skip**：简单需求资深人**跳过**多 ControlNet，单一 Canny/Depth 就够；也**跳过**手动预处理（用 AIO Aux Preprocessor 一节点自动选）。
  - **optimize**：**优化**「control weight + start/end percent」组合 —— 不只调 strength，还用 start_percent/end_percent 让 ControlNet 只在去噪前段生效（锁大结构）、后段放开（保画质细节），这是入门者不知道的关键旋钮。(evidence: [T03-S008])
  - **add**：资深人**额外**叠加多 ControlNet（OpenPose 锁姿态 + Depth 锁空间 + Canny 锁边缘三层叠加），再叠风格 LoRA，做到结构与风格同时精控。(evidence: [T03-S007])
- **近期变化（近 12 个月）**：
  - 2025 起，底模生态从 SD1.5/SDXL ControlNet 向 Flux ControlNet（XLabs / InstantX / Shakker）迁移，部分控制（参考图/人脸）被 Flux 原生方案与 PuLID 接替；ControlNet 范式本身稳定，但「用哪一套权重」随底模换。(evidence: [T03-S005])
  - 触发事件类型：新底模。采用率：Flux 用户切 Flux-ControlNet，SDXL 资产用户仍用 SDXL ControlNet（资产厚）。
- **典型耗时**：入门 SOP 约 30min–1h；资深路径 15–40min（多 ControlNet 调试会更久）。
- **关键工具（Track 02）**：ControlNet（必备）；ComfyUI ControlNet Aux Preprocessors 插件；OpenPose/Depth/Canny/Lineart 预处理器。
- **关键人物（Track 01）**：Lvmin Zhang / lllyasviel（ControlNet 论文一作，ICCV2023 best paper，把可控生成从论文推到全民工具）。
- **常见失败模式**：
  - **预处理器选错**：要锁姿态却用了 Canny（锁的是边缘不是骨架），人物换姿势就跑偏 —— 锁人体动作用 OpenPose、锁空间用 Depth、保轮廓用 Canny，按「要锁什么」选预处理器。
  - **底模与 ControlNet 代际不配**：SDXL ControlNet 套 Flux 底模静默失效 —— 换底模必须换配对 ControlNet。
  - **权重一拉到底画质僵死**：strength=1.0 全程生效，结构死板、细节丢 —— 用 start/end percent 让控制只管前段大结构，后段放开补细节。
- **来源**：
  - [Secondary] ComfyUI ControlNet 官方示例: T03-S005（collected 2026-06-22）
  - [Secondary] SD Art ControlNet 完整指南: T03-S008
  - [Reference] ControlNet 论文（Lvmin Zhang, Track 01-S007）
- **Last_updated**: 2026-06-22 · **Decay risk**: low（可控生成是范式级机制；唯具体权重套件随底模迭代）

---

### 3. 角色/风格一致性（LoRA 训练 + IPAdapter/参考图）(Decay risk: medium) last_updated: 2026-06-22

- **One-liner**: 让同一角色/画风跨多张图稳定出现 —— 两条路线：免训练参考（IPAdapter/InstantID/Omni Reference）或训练 LoRA（打标→训练→应用）。从「每张脸都不一样」到「跨图同一角色」。
- **Trigger**: 系列插画/绘本/IP/电商模特需要固定角色或固定画风跨多张图一致。
- **Output**: 可复用的 LoRA 文件（训练路线）或一套免训练参考链（IPAdapter 路线）+ 一致性成图组。
- **入门 SOP（LoRA 训练路线）**:
  1. **备数据集**：收集 20-60+ 张目标角色/风格清晰图（多角度、多光照），统一裁到 1024。(evidence: [T03-S009])
  2. **打标（captioning）**：用 BLIP/WD14/Joy Caption 自动打标，**手动复核**加触发词、删无关背景描述。(evidence: [T03-S009])
  3. **设训练参数**：选工具（Flux/Flux.2/Qwen 用 ai-toolkit，SDXL/Flux 也可 Kohya）；Flux LoRA 学习率 1e-4（出问题降 5e-5）、cosine scheduler、约 1500-2500 step。(evidence: [T03-S009, T03-S010])
  4. **训练**：跑训练，定期看样本图判断是否过/欠拟合。
  5. **应用**：在 ComfyUI/Forge 用 Load LoRA 节点挂上，调 LoRA 权重（0.6-1.0），配触发词出图。
  - **入门 SOP（免训练参考路线，更快）**：参考图 → IPAdapter（风格/人脸注入）或 InstantID/PuLID（人脸一致）→ 配 prompt 出图，无需训练。(evidence: [T03-S011])
  - **每一步跳过的后果**：跳手动复核打标 → 触发词没绑定/背景被学进风格，LoRA 出图带垃圾或调不出；数据集太少/太单一 → 过拟合（只会复刻训练图、换姿势就崩）；学习率错（Flux 比 SDXL 敏感）→ 烧坏（过曝/糊）或学不进；跳样本监控直接训满 → 过拟合了才发现，整轮白训。
- **资深路径（差异点）**：
  - **skip**：资深人**优先跳过训练**—— 一次性/短期需求直接用 IPAdapter/InstantID/MJ Omni Reference 免训练搞定，「能不练 LoRA 就不练」（训练数据准备+调参成本高）。
  - **optimize**：**优化**「打标质量 > step 数」—— 资深人知道 LoRA 成败主要在数据集与打标，而非堆 step；用 reg/正则图防过拟合，分辨率/repeat/epoch 配比经验化。(evidence: [T03-S009])
  - **add**：资深人**额外**做底模代际配对检查（SDXL LoRA 不能套 Flux）、**额外**用多 LoRA 叠权重组合（角色 LoRA + 风格 LoRA 分开训再叠加），以及训练后用一组固定测试 prompt 验一致性。
- **近期变化（近 12 个月）**：
  - 2025 起，ai-toolkit（Ostris）成为 Flux.2/Z-Image/Qwen Image LoRA 训练主流工具，取代部分 Kohya 场景；免训练人脸方案（PuLID-Flux/InstantID）成熟到很多一致性需求根本不必训 LoRA。(evidence: [T03-S010])
  - 2025-04 起，Midjourney v7 用 Omni Reference（--oref）统一了角色+风格参考，老 --cref 在 v7 不兼容 —— 闭源侧一致性免训练化。(evidence: [T03-S013])
  - 触发事件类型：新工具 + 新模型。采用率：免训练参考路线在「短期/单角色」场景已成多数；长期 IP/商业批产仍训 LoRA。
- **典型耗时**：LoRA 训练路线约 半天–2 天（含数据准备+训练+验证）；免训练参考路线 30min–2h。
- **关键工具（Track 02）**：LoRA（必备）；IPAdapter（必备）；ai-toolkit / Kohya（训练）；InstantID/PuLID（人脸）；MJ Omni Reference（闭源）。
- **关键人物（Track 01）**：Lvmin Zhang（IC-Light 等控制系列）；cubiq/Matteo（IPAdapter ComfyUI 实现作者）。
- **常见失败模式**：
  - **数据集差就开练**：20 张同角度同光照图训出来只会复刻、换姿势崩 —— 先备 20-60 张多角度多光照图、手工打标加触发词，再训。
  - **能免训练却硬训 LoRA**：单角色短期需求花半天训 LoRA，IPAdapter/InstantID 几分钟能搞定 —— 先问「这是长期 IP 还是一次性」，一次性走免训练。
  - **底模代际错配**：SDXL LoRA 挂到 Flux 底模无效 —— 训练前确定目标底模，训对应代际 LoRA。
- **来源**：
  - [Secondary] ThinkDiffusion Flux LoRA + Kohya 实操: T03-S009（collected 2026-06-22）
  - [Primary] ai-toolkit 官方 repo（Ostris）: T03-S010
  - [Primary] cubiq IPAdapter workflow repo: T03-S011
- **Last_updated**: 2026-06-22 · **Decay risk**: medium（一致性方案 12-24 月持续迭代，免训练路线在快速替代训练）

---

### 4. 图生图 + 局部重绘修图（I2I + inpaint/outpaint + 修脸换脸）(Decay risk: medium) last_updated: 2026-06-22

- **One-liner**: 在已有图上做局部修复/扩展/换脸 —— 用 denoise 幅度控制改动强度，inpaint 修局部、outpaint 扩画布、Face Detailer/换脸修脸、放大超分收尾。从「一张有瑕疵的图」到「修好的成图」。
- **Trigger**: 出图有崩坏（手/脸/局部）；要改局部不重出整张；要扩画幅；要统一/替换人脸。
- **Output**: 修复/扩展/换脸后的成图 + 放大交付。
- **入门 SOP**:
  1. **载入原图 + 涂蒙版**：Load Image，在要改的区域涂 mask（手/脸/要替换的物体）。(evidence: [T03-S002])
  2. **选模式与 denoise**：inpaint 改局部（建议用专用 inpaint 底模），denoise 控改动幅度 —— 小（0.3-0.5）只微调、大（0.7-1.0）几乎重画。(evidence: [T03-S002])
  3. **写局部 prompt 出图**：针对蒙版区域写 prompt，跑出几版挑最融合的。
  4. **修脸**：远景/小脸糊用 Face Detailer（Impact Pack，自动裁脸放大重绘再贴回）；要替换成指定脸用 ReActor 换脸。
  5. **outpaint 扩画幅**（如需）：用 Pad Image for Outpainting 节点向外扩，再 inpaint 填补。(evidence: [T03-S020])
  6. **放大超分交付**（同 workflow 1 收尾）。
  - **每一步跳过的后果**：denoise 设错（修局部却用 1.0）→ 整块重画与周围接缝/风格不连续；不用专用 inpaint 模型 → 接缝生硬、补的内容跳脱（lesson：inpaint 专用 checkpoint 效果明显好）；跳 Face Detailer 直接交付小脸图 → 远景人脸糊成一团；outpaint 不渐进一次扩太多 → 新区域与原图断裂。
- **资深路径（差异点）**：
  - **skip**：资深人**跳过**「整张重出」—— 只要局部瑕疵就 inpaint 局部，不浪费时间重抽整图；也常**跳过**手动涂脸蒙版（用 Face Detailer 的自动脸检测 SEGS）。
  - **optimize**：**优化**「denoise 精控 + grow_mask」—— 按改动需求精调 denoise（去物体用高、补细节用低），并用 grow_mask_by 羽化蒙版边缘让接缝自然；用 differential diffusion 做软蒙版过渡。(evidence: [T03-S002])
  - **add**：资深人**额外**把修脸/换脸/放大串成自动化收尾链（出图→Face Detailer→可选 ReActor→放大），一次队列跑完；**额外**注意换脸的肖像权/合规风险。
- **近期变化（近 12 个月）**：
  - 2025 起，Flux Fill（专用 inpaint/outpaint 模型）让局部重绘接缝与一致性显著提升，部分取代 SD inpaint checkpoint；Nano Banana Pro / Flux.2 的「对话式编辑」让一部分局部修改可直接自然语言下指令，绕开蒙版。(evidence: [T03-S002, T03-S011])
  - 触发事件类型：新模型。采用率：精控/批产仍走 ComfyUI mask+denoise；快速单图编辑转向对话式。
- **典型耗时**：入门 SOP 约 20min–1h；资深路径 10–30min。
- **关键工具（Track 02）**：ComfyUI inpaint；Impact Pack Face Detailer；ReActor 换脸；CodeFormer/GFPGAN 修脸；SUPIR/ESRGAN 放大；Flux Fill。
- **关键人物（Track 01）**：cubiq/Matteo（in/out-painting workflow 作者）；Scott Detweiler。
- **常见失败模式**：
  - **denoise 一刀切**：所有 inpaint 都用 1.0，微调也整块重画 —— 微调用 0.3-0.5、去物体/重画用 0.7-1.0，按改动幅度配 denoise。
  - **不用专用 inpaint 模型**：拿普通 checkpoint 做 inpaint 接缝生硬 —— 用 base 名 + inpainting 的专用模型或 Flux Fill。
  - **小脸不修直接交付**：群像/远景人脸糊 —— 出图链固定接 Face Detailer 自动裁脸重绘。
- **来源**：
  - [Primary] ComfyUI 官方 inpaint 教程: T03-S002（collected 2026-06-22）
  - [Primary] cubiq in/out-painting workflow README: T03-S011
  - [Secondary] ComfyUI Wiki outpaint 教程: T03-S020
- **Last_updated**: 2026-06-22 · **Decay risk**: medium（mask+denoise 原理稳，但专用 inpaint 模型与对话式编辑在快速演进）

---

### 5. ComfyUI 节点工作流搭建与复用（工程链）(Decay risk: medium) last_updated: 2026-06-22

- **One-liner**: 把生成管线搭成可复现、可参数化、可批量、可分享的节点图 —— 从模板起步、subgraph 模块化、API 队列批产、JSON 分享复用。从「手点出一张图」到「可工程化复用的流水线」。
- **Trigger**: 要做可复现/可回溯的商业交付；要批量出几十上百张；要把工作流分享给协作者或复用别人的。
- **Output**: 参数化的 workflow JSON（含节点图/连接/参数）+ 批量队列产物。
- **入门 SOP**:
  1. **从模板起步**：用 ComfyUI 官方模板工作流或社区 JSON 起步，不从空白搭。(evidence: [T03-S004])
  2. **导入并补依赖**：拖入 workflow 图/JSON 加载节点；用 Manager 装缺失自定义节点、映射本地 checkpoint/LoRA/VAE 路径（JSON 不含模型文件与本地路径）。(evidence: [T03-S003])
  3. **连管线**：Load→CLIP Encode→（ControlNet/IPAdapter/LoRA）→KSampler→VAE Decode→放大→Save，按需求接好。
  4. **参数化关键节点**：把要反复改的值（prompt/seed/分辨率）暴露为可调输入。
  5. **批量队列**：用 batch / 多 seed / 队列 Queue 一次跑多张。
  6. **导出 JSON 分享**：导出 workflow JSON（PNG 也内嵌），交付/归档/复用。(evidence: [T03-S003])
  - **每一步跳过的后果**：不补依赖直接跑 → 红框报「missing node」/找不到模型，工作流跑不起来（复用别人工作流第一大坑）；不参数化 → 每次改值要在节点图里翻找，批产无法自动化；不导出 JSON → 工作流只在本机、无法复现/分享。
- **资深路径（差异点）**：
  - **skip**：资深人**跳过**从零搭 —— 永远在官方模板/成熟社区 JSON 上改；也**跳过**手动逐张点 Queue（用 API/脚本）。
  - **optimize**：**优化**「subgraph 模块化」—— 把常用节点组（放大链、Face Detailer 链）封装成可复用 subgraph（带 UUID），复杂图变清爽且可跨工作流复用；ComfyUI 能在仅叶子输入变化时复用 subgraph 提速。(evidence: [T03-S003])
  - **add**：资深人**额外**走 ComfyUI API（/prompt 端点 POST workflow JSON）做服务化批产、外部应用集成、实时进度追踪；**额外**做版本管理（workflow JSON 进 git）。(evidence: [T03-S003])
- **近期变化（近 12 个月）**：
  - 2025 起，ComfyUI 上线官方 Subgraph/Blueprint 系统（SubgraphManager + UUID）与官方 workflow_templates repo，让模块化复用从「社区野路子」变官方一等公民；ComfyUI Desktop 桌面版降低部署门槛。(evidence: [T03-S003, T03-S004])
  - 触发事件类型：新工具/平台升级。采用率：subgraph 在复杂工作流用户中快速普及。
- **典型耗时**：入门 SOP 约 1-3h（含补依赖踩坑）；资深路径搭好后复用近乎即时，批产按量。
- **关键工具（Track 02）**：ComfyUI（必备底座）；ComfyUI Manager；SwarmUI（友好前端）；ComfyUI API。
- **关键人物（Track 01）**：comfyanonymous（ComfyUI 作者，节点式范式奠基）；Scott Detweiler（工作流教学）。
- **常见失败模式**：
  - **复用工作流缺节点/缺模型**：拖入别人 JSON 满屏红框 —— 先看来源/格式，用 Manager 装缺失节点，再映射 checkpoint/LoRA/VAE 路径，最后才跑。
  - **不参数化导致批产手忙**：每次改 prompt 要在大图里找节点 —— 把可变输入暴露/用 primitive 节点集中管理。
  - **本机依赖未声明**：分享 JSON 给别人跑不起来 —— 附带自定义节点清单 + 模型清单，或用 Manager 的依赖快照。
- **来源**：
  - [Primary] ComfyUI workflow JSON 官方规范: T03-S003（collected 2026-06-22）
  - [Primary] Comfy-Org 官方模板 repo: T03-S004
  - [Primary] ComfyUI 项目根: T03-S006
- **Last_updated**: 2026-06-22 · **Decay risk**: medium（节点范式稳定，但 subgraph/API/桌面版等工程能力在持续演进）

---

### 6. 图生视频 / 文生视频（可灵 / 即梦 / Runway）(Decay risk: high) last_updated: 2026-06-22

- **One-liner**: 把静帧变成有运镜、有时长、可控动态的视频 clip —— 先出高质量首帧→图生视频设运镜/时长/首尾帧/动态强度→多 clip 锁一致→可选对口型配音→剪辑合成。从「一张图」到「一个会动的镜头」。
- **Trigger**: 要做短视频/广告/MV/分镜动起来；有了关键帧要变镜头。
- **Output**: 3-10s 视频 clip（含运镜，可选首尾帧过渡、原生音频/口型）。
- **入门 SOP**:
  1. **出高质量首帧**：先用图像工作流（workflow 1）出一张满意的首帧（视频质量上限基本由首帧决定）。
  2. **选模型上传首帧**：Kling（性价比/中文）/ 即梦 Seedance（多模态参考）/ Runway（精细运镜）/ Veo（原生音频），上传首帧进 image-to-video。
  3. **写运动+运镜 prompt**：I2V 模式只描述「动作 + 运镜」，不重复描述画面（模型已看到首帧）。运镜用内置 token（push/pull/pan/tilt/orbit/zoom）。(evidence: [T03-S016])
  4. **设动态强度/时长**：选 Subtle/Moderate/Dynamic 动态档，设时长。
  5. **首尾帧控制（如需）**：上传 start/end 帧让模型插值过渡（适合 before/after、可控转场）；Kling Video 3.0 官方支持首尾帧、运动笔刷（给图上指定区域刷方向矢量控运动）。(evidence: [T03-S016, T03-S023])
  6. **抽卡筛 + 重生**：视频仍是抽卡，跑几版挑动态自然、无崩坏的。
  - **每一步跳过的后果**：首帧质量差直接 I2V → 视频继承所有瑕疵且放大（脸崩在动态里更明显）；I2V 还重复描述画面内容 → 与首帧打架、动态混乱（应只描述动作+运镜）；运镜全堆 prompt 文字而不用内置控制 → 运镜不可控/抽卡；动态强度选错（人像选 Dynamic）→ 鬼畜变形。
- **资深路径（差异点）**：
  - **skip**：资深人**跳过**「在视频里反复试运镜」—— 先把首帧打磨到位（结构/光影/构图全对）再进 I2V，省大量重生成；I2V 时**跳过**冗长画面描述，只留动作+运镜。(evidence: [T03-S016])
  - **optimize**：**优化**「五段结构 prompt」—— 用 Subject / Subject Movement / Scene / Camera Language / Lighting 结构化写（I2V 砍掉前两项交给首帧），运镜与动态强度精确匹配（人像用 Subtle、动作戏用 Dynamic）。(evidence: [T03-S016, T03-S017])
  - **add**：资深人**额外**做多镜头一致性 —— 同角色/场景用同一参考图或 Kling 多镜头分镜（Kling 3.0 Multi-Shot/Custom Multi-Shot 一次生成多 cut、每 cut 独立 prompt 与时长）锁一致；**额外**用运动笔刷给指定区域精控运动方向；**额外**做对口型/配音（Veo 原生音频或外接 TTS+对口型）与负面 prompt 压崩坏。(evidence: [T03-S023])
- **近期变化（近 12 个月）**：
  - 2026-02 Kling 3.0 上原生 4K + 多镜头分镜（一次生成最多 6 cut、物理感运动），Veo 3.1 原生音频 + prompt 遵循，Seedance 2.0 多模态参考（图/视频/音/文）—— 整个 I2V 工作流从「单 clip 抽卡」向「多镜头一致 + 原生音频」跃迁。(evidence: [T03-S016])
  - ⚠️ Sora 2 web/app 计划 2026-04-26 下线（API 2026-09-24）—— 视频闭源代际半年一跳，勿单押一家（Track 02 避坑）。
  - 触发事件类型：新模型（半年一代）。采用率：多镜头/首尾帧已成头部模型标配。
- **典型耗时**：入门 SOP 约 30min–2h/clip（含抽卡）；资深路径首帧打磨后单 clip 出片更快但更重前期。
- **关键工具（Track 02）**：可灵 Kling 3.0 / 即梦 Seedance（必备国产）；Runway Gen-4.5（精细运镜）；Veo 3.1（原生音频）；Sora 2（物理真实，注意下线）；Wan 2.x（开源本地）。
- **关键人物（Track 01）**：万鹏飞（可灵负责人，DiT 视频范式）；Bilawal Sidhu（VFX 视角实操 AI 视频，揭「抽卡/工具拼盘」之痛）。
- **常见失败模式**：
  - **首帧不行就硬 I2V**：低质首帧的瑕疵在视频里被放大成动态崩坏 —— 先把首帧打磨到交付级再进 I2V。
  - **运镜靠堆 prompt 而非内置控制**：文字描述运镜不可控、每次不同 —— 用模型内置运镜 token（push/orbit/zoom）+ 动态强度档。
  - **单押一家闭源视频模型**：Sora 即将下线、代际半年一跳 —— 关键管线留开源（Wan/Hunyuan）或多供应商退路。
  - **动态强度与内容错配**：人像/产品用 Dynamic 档变鬼畜 —— 静物/人像用 Subtle，动作戏才用 Dynamic。
- **来源**：
  - [Secondary] Kling prompt 五段结构指南: T03-S016（collected 2026-06-22）
  - [Secondary] Ambience AI Kling camera/negative 指南: T03-S017
  - [Reference] 万鹏飞可灵访谈（Track 01-S021）；Bilawal Sidhu（Track 01-S024）
- **Last_updated**: 2026-06-22 · **Decay risk**: high（视频代际半年一跳，模型能力与控制方式快速改写，6 月内大概率部分过时）

---

### 7. AI 短片 / 分镜全流程（Curious Refuge 式 AI 影视）(Decay risk: high) last_updated: 2026-06-22

- **One-liner**: 做一支完整 AI 短片 —— 脚本→分镜→角色/世界设定→关键帧→逐镜头视频生成→配音音效→剪辑成片。从「一个故事 idea」到「一支可播放的短片」。
- **Trigger**: 要产出 1-3min（或更长）AI 短片/广告/预告/MV，需要叙事连贯而非单 clip。
- **Output**: 成片（含多镜头、一致角色、配音音效、剪辑节奏）。
- **入门 SOP**:
  1. **脚本**：用 AI 文本工具（或自写）生成 idea、写脚本、按制作 pipeline 格式化分场。(evidence: [T03-S018])
  2. **分镜（storyboard）**：把脚本拆成镜头，每镜头定景别/构图/运镜，用快速图像模型 blocking 出分镜帧。(evidence: [T03-S019])
  3. **角色/世界设定**：建角色 sheet（多角度参考图）+ 世界/美术风格基调，作为全片一致性锚。(evidence: [T03-S018])
  4. **逐镜头出关键帧**：按分镜用图像工作流（workflow 1 + 一致性 workflow 3）出每镜头首帧，锁角色一致。
  5. **逐镜头视频生成**：每个关键帧走 I2V（workflow 6），按 shot 选合适视频模型（控制多 cut 用 Kling，物理真实用 Sora 等）。(evidence: [T03-S019])
  6. **配音音效**：AI 配音/voice-over、音效、配乐（或 Veo 原生音频）。(evidence: [T03-S018])
  7. **剪辑成片**：剪辑软件里拼镜头、调节奏、转场、调色，输出成片。
  - **每一步跳过的后果**：跳脚本/分镜直接生成 → 镜头碎、叙事不连贯（AI 短片最大失败源）；跳角色 sheet → 每个镜头角色脸/服装变（一致性崩）；按 shot 不选对模型 → 某些镜头动态/控制达不到；跳配音音效 → 画面再好也「不像片子」；跳剪辑节奏 → 一堆 clip 堆砌不成叙事。
- **资深路径（差异点）**：
  - **skip**：资深人**跳过**「每镜头都精修关键帧」—— 用快速模型（如 Z-Image Turbo，6B、消费级硬件、95% 质量 20% 算力）先 blocking 全片再挑重点镜头精修，不平均用力。(evidence: [T03-S019])
  - **optimize**：**优化**「按 shot 选模型」—— 不同镜头用不同视频模型（需多 cut/物理感用 Kling 3.0、要原生音频用 Veo、要精细运镜用 Runway），而非全片一个模型硬扛。(evidence: [T03-S019])
  - **add**：资深人**额外**先建完整角色 sheet + 世界设定再开拍（preproduction 决定一致性），**额外**用统一参考/LoRA 锁角色跨镜头，**额外**重视剪辑节奏与声音设计（成片感主要来自后期）。
- **近期变化（近 12 个月）**：
  - 2026 起，关键帧 blocking 转向 Z-Image Turbo 等快模型（消费级、低算力），视频侧 Kling 3.0 多镜头分镜（一次 6 cut）大幅降低多镜头一致性成本；整体 pipeline 从「逐帧手搓」向「分镜驱动 + 按 shot 选模型」标准化。(evidence: [T03-S019])
  - 触发事件类型：新模型 + 方法论成熟（Curious Refuge 等课程体系化）。采用率：分镜先行已成 AI 影视社区共识。
- **典型耗时**：入门 SOP 约 数天–数周/短片；资深路径前期重（preproduction）但后期返工少。
- **关键工具（Track 02）**：图像底模 + 一致性工具（关键帧）；Kling/Runway/Veo/Sora（视频）；Z-Image（快速分镜）；剪辑软件 + AI 配音。
- **关键人物（Track 01）**：Caleb Ward（Curious Refuge 创始人，全球首个 AI 影视课程，方法论 originator）；Bilawal Sidhu（VFX 实操视角）。
- **常见失败模式**：
  - **跳过 preproduction 直接生成**：没脚本没分镜没角色 sheet，镜头碎、角色乱 —— 脚本→分镜→角色 sheet 先做完再生成第一帧。
  - **全片平均用力精修每帧**：算力/时间耗在不重要镜头 —— 快模型 blocking 全片，只精修关键镜头。
  - **一个模型扛全片**：某些镜头动态/控制达不到 —— 按 shot 需求选不同视频模型。
  - **忽视声音与剪辑**：画面好但没声音设计/剪辑节奏，不成片 —— 后期（配音/音效/剪辑）是成片感主来源。
- **来源**：
  - [Secondary] Curious Refuge AI Filmmaking 课程页（方法论 originator）: T03-S018（collected 2026-06-22）
  - [Secondary] Curious Refuge 60 AI 影视工具/pipeline 自述: T03-S019
  - [Reference] Caleb Ward（Track 01-S014/S015）；Bilawal Sidhu（Track 01-S024）
- **Last_updated**: 2026-06-22 · **Decay risk**: high（每个子环节工具半年一变，整条 pipeline 是高速演化前沿）

---

### 8. Midjourney 闭源易用出图流（sref/cref/oref 一致性）(Decay risk: high) last_updated: 2026-06-22

- **One-liner**: 零工程门槛在 Midjourney 出高审美图，并用风格/角色参考做一致性 —— Draft 探方向→prompt+参数→风格(--sref)/角色(--oref)参考锁一致→精修。从「要好看的图但不想搭环境」到「高一致性成图组」。
- **Trigger**: 非技术创作者/概念阶段要快速出高审美图；要系列图风格或角色一致但不想训 LoRA。
- **Output**: 高审美、可风格/角色一致的成图组。
- **入门 SOP**:
  1. **写 prompt**：自然语言描述主体+风格+氛围，加纵横比 --ar 等基础参数。
  2. **Draft 模式探方向**：用 Draft 模式（半价、10× 速度）快速出大量草图筛方向。(evidence: [T03-S022])
  3. **锁风格（--sref）**：找到喜欢的风格后，用 --sref + 图 URL 或风格码锁风格，--sw（0-1000，默认 100）调风格强度。(evidence: [T03-S014])
  4. **锁角色（v7 用 --oref）**：用 Omni Reference --oref + 图 URL 锁角色/物体，--ow（1-1000）调影响（25-50 偏风格化、400+ 强遵循）。注意 v7 不兼容旧 --cref。(evidence: [T03-S013, T03-S015])
  5. **Upscale 精修出图**：挑满意的 upscale 到成图分辨率。
  - **每一步跳过的后果**：不用 Draft 直接正式出图 → 探方向阶段烧 2× 算力/时间；要一致性却不用 sref/oref → 每张风格/角色漂移；v7 用 --cref → 报错或被忽略（v7 已不兼容）；--ow/--sw 不调用默认 → 一致性强度与需求错配（人物糊或风格盖过内容）。
- **资深路径（差异点）**：
  - **skip**：资深人**跳过**「正式出图试错」—— 探方向阶段全用 Draft 模式（半价），定方向才转正式；也**跳过**冗长 prompt（MJ 审美下限高，短 prompt + 强参考往往更好）。
  - **optimize**：**优化**「--sw / --ow 权重精调」—— 知道 --sw 控风格强度、--ow 25-50 偏风格化 vs 400+ 强角色遵循，按「要风格还是要角色」精调而非默认；用 --sref 风格码库复用稳定风格。(evidence: [T03-S013, T03-S014])
  - **add**：资深人**额外**组合参考（--sref 风格 + --oref 角色同时用，做到「指定角色 + 指定风格」），**额外**管理风格码/参考图库做品牌化一致性；清楚 --oref 2× GPU 成本做取舍。(evidence: [T03-S013])
- **近期变化（近 12 个月）**：
  - 2025-05 起，Midjourney v7 用 Omni Reference（--oref/--ow）统一角色+风格+物体参考，**旧 --cref 在 v7 不兼容**（报错或被忽略）—— 一致性工作流被重写。(evidence: [T03-S013, T03-S015])
  - Draft 模式（半价 10× 速度）成为探方向标准前置。(evidence: [T03-S022])
  - 触发事件类型：新模型版本（v7）。采用率：v7 用户已迁 Omni Reference。
- **典型耗时**：入门 SOP 约 15min–1h；资深路径方向判断快、10–30min。
- **关键工具（Track 02）**：Midjourney v7（必备闭源）；Draft 模式；Omni/Style/Character Reference。
- **关键人物（Track 01）**：David Holz（MJ 创始人，「想象力引擎」产品哲学，审美优先治理）。
- **常见失败模式**：
  - **v7 还用 --cref**：报错/被忽略，角色锁不住 —— v7 改用 --oref（Omni Reference）。
  - **不用 Draft 烧算力试错**：探方向用正式模式 2× 成本 —— 探方向全程 Draft，定方向才正式 upscale。
  - **闭源当可复现管线**：MJ 不可锁种子精确复现，批产/法务追溯需求 —— 这类需求改用开源 + 固定 seed 的 ComfyUI 链。
  - **--ow/--sw 默认不调**：一致性强度与需求错配 —— 按要风格 vs 要角色精调 --sw/--ow。
- **来源**：
  - [Primary] MJ Omni Reference 官方文档: T03-S013（collected 2026-06-22）
  - [Primary] MJ Style Reference 官方文档: T03-S014
  - [Primary] MJ Character Reference 官方文档: T03-S015
  - [Primary] MJ Draft Mode 官方文档: T03-S022
- **Last_updated**: 2026-06-22 · **Decay risk**: high（闭源参数/模式随版本快速迭代，v7→v8 等会再改写一致性参数）

---

## Phase 2 提炼提示

**反复出现 ≥ 3 个 workflow 都包含的步骤模式**（候选 playbook 通则）：

- **「先低成本探方向，方向对了再投入精修」**：出现于 workflow 1（低分辨率小批量再放大）/ 6（先打磨首帧再 I2V）/ 7（快模型 blocking 全片再精修关键镜头）/ 8（Draft 模式探方向再正式出图）→ 候选 playbook「如果还在探方向阶段，则用最低成本档（低分辨率/草图/快模型/Draft）抽卡，禁止在未定稿的内容上做高成本精修」。**这是本行最强的跨 workflow 通则**。
- **「随机性逐层收束」**：出现于 workflow 1（锁 seed 后逐个变量调）/ 2（control weight + start/end 收结构）/ 6（首帧+运镜+动态强度逐层锁）→ 候选 playbook「从抽卡到精控，每次只放开一个随机维度、锁住其余」。
- **「放大/超分作为固定收尾环节」**：出现于 workflow 1 / 2 / 4 → 候选 playbook「任何要交付的图，出图后固定接放大链到交付分辨率，纯放大用 ESRGAN、要补细节用 SUPIR/USDU」。
- **「底模代际配对检查」**：出现于 workflow 2（ControlNet 配代际）/ 3（LoRA 配代际）→ 候选 playbook「换底模时，ControlNet/LoRA/IPAdapter 必须换配对代际，否则静默失效」。
- **「能免训练就不训练 / 能复用模板就不从零搭」**：出现于 workflow 3（IPAdapter 优先于 LoRA）/ 5（模板优先于空白搭）/ 8（参考图优先于训练）→ 候选 playbook「先用最轻量方案（参考图/模板/免训练）满足需求，只有长期/批产/IP 级需求才升级到重方案（训练/自建工程链）」。
- **「参数/工作流可复现归档」**：出现于 workflow 1（留参数）/ 5（导出 JSON）→ 候选 playbook「交付物必须可复现：开源链锁 seed+存参数+导 JSON；闭源链建台账（因不可锁 seed）」。

**入门 SOP 和资深路径之间最大的差距**（候选 心智模型）：

- 入门 SOP 平均 5-7 步，资深路径核心差异不在「步数变少」而在 **「判断在哪一步停 / 用哪一档成本 / 何时升级方案」**。资深人最强的判断是「**这件事值不值得投入精修/训练/精控**」—— 一致性需求先问「长期 IP 还是一次性」、出图先问「方向定了没」、视频先问「首帧够好了没」。
- 推断本行资深心智模型候选：**「可控性 vs 抽卡」的成本意识** —— 知道每个环节的算力/时间成本曲线（CFG>15、steps>50、4K 放大、LoRA 训练、--oref 2× GPU 都是「贵」的动作），在便宜阶段穷尽试错、在确定后才花贵的钱。
- 第二个心智模型候选：**「底座 + 轻量约束三件套」** —— 资深人不靠换大模型解决问题，靠 ControlNet（结构）/LoRA·IPAdapter（风格角色）/inpaint·denoise（局部）这套轻量约束 + 放大链精控，把随机底座调成可控产出。

**近期工作流变化的根本原因**（触发变化的事件类型分布）：

- 8 个 workflow 中：因**新模型**变化的 = 7（T2I prompt 简化、Flux ControlNet 迁移、免训练一致性、Flux Fill、视频代际、Z-Image 分镜、MJ v7 Omni Reference）；因**新工具/平台**变化 = 2（ai-toolkit、ComfyUI subgraph/API）；因**法规** = 0（创作侧；版权诉讼属外部环境非工作流步骤本身）。
- 主要外部驱动力：**底模/视频模型半年级代际迭代** —— 这是本行工作流衰减的根本原因，Phase 2 应识别为行业「外部驱动力」第一位（影响心智模型「工具临时性」+ 反模式「单押闭源/堆大模型」）。

**冷僻 / 信号薄弱**：

- workflow 数 = 8（远超 floor 4，非冷僻行业）。
- 一手 source 占比：23 条 manifest 中 verified_primary = 12（约 52%，达标 ≥50%）；其余 secondary 多为 vendor 一手但被子域/路径自动降级（Kling app 子域、comfyanonymous github.io 个人页、Curious Refuge 课程页）+ ControlNet/LoRA 教程聚合站。即「实质一手（vendor docs/论文/官方 repo/官方课程）」覆盖率显著高于 bucket 字面 52%。
- 资深差异点：8/8 workflow 均有 ≥2 处资深差异（skip/optimize/add），100% 达标。
- 较弱处：(1) **视频侧（workflow 6/7）的「采用率」硬数据**多来自 vendor/对比文，缺权威 survey，须标「业内估计 + 来源年份」；(2) LoRA 训练具体参数（学习率/step）来自 secondary 教程站，虽与 ai-toolkit 官方 repo 交叉印证，但精确数值随工具版本会变；(3) 国产视频（即梦/Seedance）官方一手 prompt 指南公开度低于 Kling/Runway，部分依赖第三方。
- **Decay 警告（进 Phase 2.8 诚实边界）**：3 个 high-decay workflow（6 视频 / 7 AI 短片 / 8 MJ 闭源）6 个月内大概率部分过时，强烈建议每 3 个月跑 update；2 个 low-decay（1 T2I 全链 / 2 ControlNet）是范式级原理，24+ 月稳定，是本 skill 工作流模块的「稳态锚」。
