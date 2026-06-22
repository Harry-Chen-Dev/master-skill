# AIGC 创作工作流 / AIGC Creative Workflow — Master OS — Synthesis

> Phase 2 提炼结果。Phase 3 (skill writeup) 直接消化本文件。
> 第一性背景：**生成式视觉创作（图像 + 视频）的工程化创作流水线**。本行最尖锐的张力不是「哪个模型更强」，而是「可控性/工程化复现 ⇄ 随机性/抽卡玄学」——OS 的每个组件都在这条轴上取位。版权与训练数据争议、AI 替代创作者就业、AI 味审美趋同、玄学割韭菜**诚实保留、绝不软化**（intake warnings 硬要求）。locale=global（技术 canon/底座/可控插件/奠基论文几乎全 en 起源 + 强 zh-CN 创作实践与国产视频工具）。

---

## 1. 心智模型 (7 个)

### 1.1 可控性 ⇄ 抽卡随机（slot machine）的第一性张力

- (figures: Bilawal Sidhu / Lvmin Zhang / comfyanonymous)
- **一句话**：扩散模型本质是「抽卡机」（Bilawal Sidhu 直接命名 slot machine nature），同 prompt 多跑挑可用——生成式视觉创作的每个决策都在「可控性/工程化复现 ⇄ 随机性/抽卡玄学」这条轴上取位，资深人的全部功夫是把随机性逐层收束成可控、可复现的产出。
- **应用方式**：面对任何出图/出视频需求，先问「这一步该用抽卡还是该上控制」；能锁的维度（seed/结构/风格/角色）就锁，不把运气当能力。
- **局限**：（放大度⚠️）抽卡在「探方向 / 找灵感」阶段仍是高效手段，不是越控制越好；过早过度上控制会扼杀意外惊喜，控制力应随「方向是否定稿」递增。
- **evidence**: [T01-S025, T06-S005, T03-S001]

### 1.2 模型是地板，审美与判断是天花板

- (figures: David Holz / swyx / Bilawal Sidhu)
- **一句话**：同样的模型与参数，产出天差地别取决于人的审美判断、概念、构图、镜头语言与「在哪一步停」的判断；模型决定下限（地板），人的审美与工程判断决定上限（天花板），「换个更大的底模就行」是外行幻觉。
- **应用方式**：出图不达标先查 prompt / 控制链 / 放大链而非换底模；把人力投在审美判断与方向把控，而非堆参数堆模型堆 LoRA。
- **局限**：地板仍在抬升——底模代际跃迁（SDXL→Flux→Nano Banana Pro）确实把下限拉高，审美天花板论不否认底模能力的真实进步，只反对「以为换模型能替代审美与手艺」。
- **evidence**: [T01-S001, T02-S002, T03-S001]

### 1.3 把随机底座调成可控产出靠「底座 + 轻量约束三件套」

- (figures: Lvmin Zhang / comfyanonymous / Scott Detweiler)
- **一句话**：资深人不靠换大模型解决问题，靠 ControlNet（锁结构）/ LoRA·IPAdapter（锁风格角色）/ inpaint·denoise（改局部）这套轻量约束 + 放大链，把通用随机底座精调成确定产出。
- **应用方式**：拿到可控需求按「要锁什么」拆——结构姿态→ControlNet、风格角色一致→LoRA/IPAdapter、局部瑕疵→inpaint/denoise，组合轻量约束而非求一个万能模型。
- **局限**：三件套与底模代际强绑定（SDXL 的 ControlNet/LoRA 套不到 Flux），迁移期要换配对件；约束生态本身在快速迁移（IPAdapter 正被 PuLID/InstantX 部分接替）。
- **evidence**: [T02-S011, T02-S012, T06-S004]

### 1.4 先用最低成本探方向，方向定了再投贵资源

- (figures: Bilawal Sidhu / Caleb Ward / Scott Detweiler)
- **一句话**：每个环节都有成本曲线（CFG 拉高、步数堆满、4K 放大、LoRA 训练、Midjourney Omni Reference 约 2× GPU、视频生成都是贵动作），资深人在便宜阶段（低分辨率/草图/快模型/Draft）穷尽试错，只在方向确定后才花贵的钱精修。
- **应用方式**：任何创作任务先判断「还在探方向还是已定稿」；未定稿禁止高成本精修——低分辨率小批量出图、快模型 blocking 全片、Draft 模式探方向，方向对了才放大/精修/训练。
- **局限**：「探方向用便宜档」依赖对各环节成本曲线的经验积累；新手缺成本直觉时反而在便宜档反复打转、不敢推进到精修。
- **evidence**: [T03-S001, T03-S022, T01-S025]

### 1.5 可复现性是工程化创作的命脉

- (figures: comfyanonymous / Scott Detweiler / Robin Rombach)
- **一句话**：商业级创作的分水岭是「能不能复现」——开源链靠固定 seed + 存全参数 + 导 workflow JSON 做到一张图可回溯可改稿，闭源黑盒不可锁种子只能靠台账补；可复现把「抽到一张好图」变成「可交付可迭代的资产」。
- **应用方式**：交付前必问「客户要改一处，我能复现原图吗」；开源链锁 seed + 存全参数 + 导 JSON（ComfyUI PNG 内嵌工作流元数据），闭源链建参数台账。
- **局限**：闭源工具（Midjourney/可灵/Nano Banana Pro）结构上不可精确复现，可复现性在闭源侧只能近似（参考图 + 参数记录），不等同开源的逐像素复现。
- **evidence**: [T01-S009, T03-S003, T06-S003]

### 1.6 工具临时性：半年一代是本行第一外部驱动力

- (figures: swyx / Bilawal Sidhu / 万鹏飞)
- **一句话**：底模与视频模型半年一代（SDXL→Flux→Flux.2、可灵约半年一大版、Sora 2 已宣布下线计划），工具栈是本行衰减最快的层；选型按「这个能力会不会被下一代模型/底模 native 吃掉」判断，不押单一闭源管线。
- **应用方式**：工具选型先问「6 个月后这个能力会不会被下一代吃掉 / 这家会不会下线」；关键管线留开源（Wan/Hunyuan）或多供应商退路；OS 核心手艺（审美/可控/复现）重投入，具体工具轻投入。
- **局限**：工具临时性只适用快速迭代的应用层（视频模型/底模/UI）；对底层范式（扩散去噪、可控生成机制、审美与镜头判断）不成立——这些是 24+ 月稳态核。
- **evidence**: [T02-S023, T01-S025, T02-S014]

### 1.7 工具拼盘破坏 flow，集成/节点工作流是回应

- (figures: Bilawal Sidhu / comfyanonymous / Scott Detweiler)
- **一句话**：AIGC 创作的真实痛点是「在 N 个工具间反复横跳破坏心流且更慢」（Bilawal：tool to tool destroys your flow state），节点式集成工作流（ComfyUI）把碎片管线连成可见、可改、可复现的一张图，是对工具拼盘之痛的工程回应。
- **应用方式**：当发现自己在 Midjourney→PS→Magnific→Runway→Topaz 间反复倒腾，把可固化的环节收进一条 ComfyUI 节点链/批产管线，减少工具切换。
- **局限**：（放大度⚠️）集成节点链学习曲线陡，对纯新手 / 一次性需求多工具手动反而更快；集成的收益主要在批产 / 可复现场景兑现。
- **evidence**: [T01-S025, T01-S009, T03-S003]

---

## 2. 标准 Playbook (8 条)

1. **如果还在探方向阶段**，则用最低成本档（低分辨率/草图/快模型/Draft 模式）抽卡，禁止在未定稿内容上做高成本精修。案例：先在 512/768 出几张筛构图方向，方向对了再 4K 放大，省约 80% 算力（T03-S001）。evidence: [T03-S001, T03-S022]
2. **如果出图质量不达标**，则先查 prompt / 控制链 / 放大链再考虑换底模，别指望「换个更大的底模解决一切」。案例：弱 prompt 下 32B 的 Flux.2（官方参数）不一定胜过调好的 SDXL 工作流（T02-S002）。evidence: [T02-S001, T02-S002]
3. **如果要让生成遵循指定构图/姿态/线稿**，则上 ControlNet 按「要锁什么」选预处理器（姿态用 OpenPose、空间用 Depth、边缘用 Canny），别只靠文生图堆词。案例：锁人物动作用 OpenPose，保产品轮廓换背景用 Canny（T03-S005）。evidence: [T06-S005, T03-S005]
4. **如果需要角色/风格跨多图一致**，则先问「长期 IP 还是一次性」——一次性走免训练（IPAdapter/InstantID/Midjourney Omni Reference），长期/批产才训 LoRA。案例：单角色短期需求 IPAdapter 几分钟搞定，不必花半天训 LoRA（T03-S011）。evidence: [T02-S012, T03-S011]
5. **如果接商单要商用**，则先查模型 license——Flux dev 非商用、schnell 与 klein-4B 是 Apache 可商用、pro 走 API、Adobe Firefly 有商用赔付。案例：下载 Flux.1-dev 直接接单踩 license 红线（官方 model card，T06-S017）。evidence: [T06-S017, T02-S005]
6. **如果换底模**，则 ControlNet/LoRA/IPAdapter 必须换配对代际，否则静默失效。案例：SDXL 的 LoRA/ControlNet 套到 Flux 底模无效或报错（T02-S011）。evidence: [T02-S011, T02-S020]
7. **如果要把静帧变视频**，则先把首帧打磨到交付级再进图生视频，运镜用模型内置 token（push/pull/orbit/zoom）+ 动态强度档而非堆 prompt。案例：低质首帧的瑕疵在动态里被放大成崩坏（T03-S016）。evidence: [T03-S016, T03-S023]
8. **如果交付物要可回溯/改稿**，则开源链锁 seed + 存全参数 + 导 workflow JSON，闭源链（Midjourney/可灵不可锁种子）建参数台账。案例：ComfyUI 用 PNG 内嵌工作流元数据可复现（T03-S003）。evidence: [T03-S003, T06-S003]

---

## 3. 工具栈与选型决策树

> 直接消化 Track 02（`references/research/02-tools.md`）的三层结构 + 5 棵选型决策树，本节做一致性 sanity check。「工具」= 底模 + UI/引擎 + 可控插件 + 社区资产 + 视频模型 + 后期增强。本行图像侧成熟、视频侧半年一代际跳变，maturity 用 GitHub stars/官方发布/第三方对比综合衡量。

**工具三层 sanity：必备 11 / 场景特化 12 / 新兴 5**（共约 28 张工具卡，详见 02-tools.md）。

- **必备层（≥80% 创作者用，11 个）**：ComfyUI（节点式底座，约 11.8 万 stars，T02-S001 官方 repo 2026-06-22）、Stable Diffusion/SDXL/SD3.5（开源底模根基，T02-S019）、Flux.1 dev/schnell（开源画质标杆 + 文字渲染，T02-S002）、Midjourney v7（闭源美学天花板，T02-S006）、ControlNet（结构控制基石，T02-S011）、LoRA（轻量微调标准格式，T02-S020）、IPAdapter（参考图免训练迁移，T02-S012）、Civitai/Hugging Face（资产分发枢纽，T02-S020）、放大超分链 ESRGAN/Ultimate SD Upscale/SUPIR（固定收尾，T02-S001）、可灵 Kling（国产视频头部，T02-S021）、即梦 Seedance（字节系多模态参考视频，T02-S022）。
- **场景特化层（12 个）**：Automatic1111/Forge（表单式 webui，T02-S008）、SwarmUI（ComfyUI 后端 + 友好前端，T02-S010）、Fooocus（极简零配置，T02-S007）、AnimateDiff（SD 运动模块，T02-S001）、ReActor 换脸（注意肖像权，T02-S001）、CodeFormer/GFPGAN（人脸修复，T02-S001）、SUPIR/Magnific（重绘式超分，T02-S001）、Krea（实时画布聚合，T02-S001）、Runway Gen-4.5（专业可控视频，T02-S015）、Adobe Firefly（商用赔付保障，T02-S029）、Ideogram/Recraft（文字渲染约 90-95%/矢量品牌，T02-S027）、Hailuo/Luma/Vidu/Pika（中端性价比视频，T02-S028）。
- **新兴层（近 12 个月起势，5 个）**：Flux.2 dev/pro/klein（32B 旗舰开源图像底模，官方 T02-S002）、Nano Banana Pro / Gemini 3 Pro Image（闭源文字渲染新王，官方 T02-S018）、Kling 3.0 / Sora 2 / Veo 3.1（视频代际跃迁，T02-S023）、Wan 2.x 通义万相（开源视频底座，T02-S014）、Seedance 2.0（多模态参考视频范式，T02-S023）。
- **国产 vs 海外（诚实标差异，不捧不踩）**：图像闭源美学 Midjourney 仍领先；开源图像底模 Flux/SD 生态最厚；闭源新王（Nano Banana Pro 文字/4K/推理式编辑）当前海外领先；视频生成国产（可灵/即梦）性价比 + 中文 + 国内可用占优，海外（Veo 原生音频/Sora 物理真实）各有所长；**开源视频底座国产反而领先**（阿里 Wan / 腾讯 HunyuanVideo，T02-S013/S014）。商单选型须按交付地法务 + license 双重判断。
- **避坑清单（≥5，7 条）**：① 以为换更大底模解决一切（画质常出在 prompt/控制链/放大链）② Flux dev 系非商用却接商单（license 红线，T02-S005）③ 闭源黑盒当可复现管线（不可锁种子）④ 显存不够硬上大模型（先按显卡门槛分支，T02-S001）⑤ 插件/LoRA/ControlNet 与底模代际不匹配（静默失效，T02-S011）⑥ 把单一闭源视频模型当永久基础设施（Sora 已宣布下线，留开源/多供应商退路，T02-S023）⑦ 新模型支持指望 A1111/Forge 即时跟进（新架构普遍先在 ComfyUI 落地）。

**选型决策树（5 棵主树，摘自 02-tools.md，均挂 evidence）**：A 纯新手/只要好看不要控制（Midjourney/Nano Banana Pro/Fooocus，T02-S006）/ B 要可控可复现批产（结构→ComfyUI+ControlNet、风格角色→IPAdapter/LoRA、不学节点→Forge/SwarmUI，T02-S011）/ C 图像底模与商用 license（Firefly/schnell/klein 可商用 vs dev 非商用 vs SDXL 资产最厚，T02-S005）/ D 做视频（性价比中文→可灵/即梦、精细运镜→Runway、原生音频→Veo、开源本地→Wan，T02-S023）/ E 显存门槛兜底（<8GB SD1.5+Forge、8-12GB 量化、16GB+ Flux.2/Wan 本地，T02-S001）。

---

## 4. 工作流 / Pipeline

> 直接消化 Track 03（`references/research/03-workflows.md`）8 个 workflow，每个含入门 SOP / 资深路径（跳过·优化·额外）/ 近期变化三段。衰减分层：T2I 全链 + ControlNet 可控生成原理 `Decay risk: low`；一致性/局部重绘/ComfyUI 工程链 `Decay risk: medium`；视频/AI 短片/Midjourney 闭源参数 `Decay risk: high`。

### 4.1 单张精控出图（文生图 T2I 全链）
- **入门 SOP**：选底模 Load Checkpoint → 正/负 prompt 进 CLIP Encode → Empty Latent 设分辨率 + KSampler 设步数约 25/CFG 约 7/采样器/seed → 首轮小批量筛方向 → 锁 seed 迭代收敛 → 放大链精修 → Save 留全参数。
- **资深路径**：**跳过**在高分辨率上试错（永远先低分辨率探方向再放大）+ 跳过堆砌长串质量词（新底模过度 prompt 反过拟合）；**优化** seed 管理（锁 seed 只动一个变量做 A/B）与 CFG/步数甜区（知道 CFG>15 偏执、步数>50 边际递减）；**额外**做分阶段放大 + 局部 Face Detailer + 参数归档版本回溯。
- **近期变化**：2025-11 起 Flux.2/Nano Banana Pro 等推动「长质量词 + 负面 prompt」老习惯收益骤降，自然语言长句遵循更好，入门 SOP 正在简化（evidence T03-S001）。`last_updated`: 2026-06-22。`Decay risk: low`。

### 4.2 可控生成（ControlNet 控构图/姿态/线稿）
- **入门 SOP**：准备垫图 → 按需求选预处理器（OpenPose/Depth/Canny/Lineart）并预处理 → 加载配对代际 ControlNet → Apply ControlNet 注入条件设 strength → 调控制权重出图 → 放大精修。
- **资深路径**：**跳过**多 ControlNet（简单需求单一 Canny/Depth 就够）+ 跳过手动预处理（用 AIO Aux Preprocessor）；**优化** control weight + start/end percent 组合（让控制只管去噪前段大结构、后段放开保细节）；**额外**叠加多 ControlNet（姿态 + 空间 + 边缘）再叠风格 LoRA。
- **近期变化**：2025 起底模从 SDXL ControlNet 向 Flux ControlNet（XLabs/InstantX）迁移，范式稳定但「用哪套权重」随底模换（evidence T03-S005）。`last_updated`: 2026-06-22。`Decay risk: low`。

### 4.3 角色/风格一致性（LoRA 训练 + IPAdapter/参考图）
- **入门 SOP**：备数据集（约 20-60 张多角度图）→ 打标手动复核加触发词 → 设训练参数（Flux LoRA 学习率约 1e-4、约 1500-2500 step，T03-S009）→ 训练监控样本 → Load LoRA 调权重出图；**免训练路线**：参考图 → IPAdapter/InstantID/PuLID → 配 prompt 出图。
- **资深路径**：**跳过**训练（一次性需求优先 IPAdapter/InstantID/Omni Reference，「能不练就不练」）；**优化**「打标质量 > step 数」+ 正则图防过拟合；**额外**做底模代际配对检查 + 多 LoRA 叠权重 + 固定测试 prompt 验一致性。
- **近期变化**：2025 起 ai-toolkit 成 Flux.2/Qwen LoRA 训练主流，免训练人脸方案（PuLID-Flux/InstantID）成熟到多数一致性需求不必训 LoRA（evidence T03-S010）。`last_updated`: 2026-06-22。`Decay risk: medium`。

### 4.4 图生图 + 局部重绘修图（I2I + inpaint/outpaint + 修脸换脸）
- **入门 SOP**：载入原图涂蒙版 → 选 inpaint 模式 + denoise 控改动幅度（约 0.3-0.5 微调 / 约 0.7-1.0 重画）→ 写局部 prompt 出图 → Face Detailer 修脸或 ReActor 换脸 → outpaint 扩画幅（如需）→ 放大超分交付。
- **资深路径**：**跳过**整张重出（只 inpaint 局部）+ 跳过手动涂脸蒙版（用 Face Detailer 自动 SEGS）；**优化** denoise 精控 + grow_mask 羽化接缝 + differential diffusion 软蒙版；**额外**把修脸/换脸/放大串成自动化收尾链，注意换脸肖像权合规。
- **近期变化**：2025 起 Flux Fill 专用 inpaint 提升接缝一致性，Nano Banana Pro/Flux.2「对话式编辑」让部分局部修改可自然语言下指令绕开蒙版（evidence T03-S002）。`last_updated`: 2026-06-22。`Decay risk: medium`。

### 4.5 ComfyUI 节点工作流搭建与复用（工程链）
- **入门 SOP**：从官方模板/社区 JSON 起步 → 导入并用 Manager 补缺失节点 + 映射本地模型路径 → 连管线 → 参数化关键节点 → 批量队列 → 导出 workflow JSON 分享归档。
- **资深路径**：**跳过**从零搭（永远在模板上改）+ 跳过手动逐张点 Queue（用 API/脚本）；**优化** subgraph 模块化（把放大链/Face Detailer 链封装成可复用 subgraph）；**额外**走 ComfyUI API 做服务化批产 + workflow JSON 进 git 版本管理。
- **近期变化**：2025 起 ComfyUI 上线官方 Subgraph/Blueprint 系统 + workflow_templates repo + 桌面版，模块化复用从社区野路子变官方一等公民（evidence T03-S003）。`last_updated`: 2026-06-22。`Decay risk: medium`。

### 4.6 图生视频 / 文生视频（可灵 / 即梦 / Runway）
- **入门 SOP**：先出高质量首帧（视频上限基本由首帧决定）→ 选模型上传首帧进 I2V → 写运动 + 运镜 prompt（只描述动作 + 运镜，不重复画面）→ 设动态强度档与时长 → 首尾帧控制（如需）→ 抽卡筛 + 重生。
- **资深路径**：**跳过**在视频里反复试运镜（先把首帧打磨到位再进 I2V）+ 跳过冗长画面描述（只留动作 + 运镜）；**优化**五段结构 prompt（Subject/Movement/Scene/Camera/Lighting，I2V 砍前两项）+ 运镜与动态强度匹配（人像 Subtle、动作戏 Dynamic）；**额外**做多镜头一致性（可灵多镜头分镜锁一致）+ 运动笔刷精控 + 对口型配音。
- **近期变化**：2026-02 可灵 3.0 上原生 4K + 多镜头分镜，Veo 3.1 原生音频，Seedance 2.0 多模态参考——I2V 从「单 clip 抽卡」向「多镜头一致 + 原生音频」跃迁；Sora 2 已宣布下线计划，勿单押一家（evidence T03-S016）。`last_checked`: 2026-06-22。`Decay risk: high`。

### 4.7 AI 短片 / 分镜全流程（Curious Refuge 式 AI 影视）
- **入门 SOP**：脚本 → 分镜 storyboard（每镜头定景别/构图/运镜，快模型 blocking 分镜帧）→ 角色/世界设定 sheet（一致性锚）→ 逐镜头出关键帧 → 逐镜头 I2V 按 shot 选模型 → 配音音效 → 剪辑成片。
- **资深路径**：**跳过**每镜头都精修关键帧（用快模型 blocking 全片再挑重点精修，不平均用力）；**优化**按 shot 选模型（多 cut 用可灵、原生音频用 Veo、精细运镜用 Runway）；**额外**先建完整角色 sheet + 世界设定再开拍 + 统一参考/LoRA 锁角色 + 重视剪辑节奏与声音设计。
- **近期变化**：2026 起关键帧 blocking 转向快模型（消费级低算力），可灵多镜头分镜降低多镜头一致性成本，pipeline 从「逐帧手搓」向「分镜驱动 + 按 shot 选模型」标准化（evidence T03-S019）。`last_checked`: 2026-06-22。`Decay risk: high`。

### 4.8 Midjourney 闭源易用出图流（sref/cref/oref 一致性）
- **入门 SOP**：写自然语言 prompt + 基础参数 → Draft 模式（官方半价、约 10× 速度）探方向 → 锁风格 --sref + --sw → 锁角色 v7 用 --oref + --ow（注意 v7 不兼容旧 --cref）→ Upscale 精修出图。
- **资深路径**：**跳过**正式出图试错（探方向全用 Draft）+ 跳过冗长 prompt（MJ 审美下限高，短 prompt + 强参考更好）；**优化** --sw/--ow 权重精调（--ow 约 25-50 偏风格化、约 400+ 强角色遵循）+ 复用风格码库；**额外**组合 --sref 风格 + --oref 角色 + 清楚 --oref 约 2× GPU 成本做取舍。
- **近期变化**：2025-05 起 Midjourney v7 用 Omni Reference 统一参考，旧 --cref 在 v7 不兼容；Draft 模式成探方向标准前置（官方文档 T03-S013/T03-S022）。`last_checked`: 2026-06-22。`Decay risk: high`。

---

## 5. 表达 DNA

AIGC 创作资深人的语言是**黑话密集 + 工程化祛魅 + 审美词汇**：张口就是抽卡/炼丹/垫图/重绘幅度/锁种子/控图/工作流/首尾帧这类术语，把「咒语玄学」「换大模型就行」「一键出大片零门槛」「7天变现」等营销与玄学话术主动拆穿，谈能力必挂模型版本 + last_checked（因半年一代），强调可控生成 > 念咒、手艺 > 抽卡、合规（license/版权）是专业底线。

- **高频黑话**：抽卡 / 炼丹（训 LoRA）/ 垫图·喂图 / 控图 / 锁种子 seed / 重绘幅度 denoise / 底模 checkpoint / 咒语 prompt / 负向 / 修手·崩手 / AI 味 / 跑图·队列 / 工作流 workflow / 节点 / 文生图 T2I / 图生图 I2I / 图生视频 I2V / 首帧·尾帧 / 运镜 / 动态强度 / 一致性 / 过拟合 / 打标 / 可商用。
- **严肃 register**：谈技术用机制语言（「去噪」「latent space」「classifier-free guidance」「时序一致性」「条件控制」），谈进步克制于「真实可控产出」而非营销节点。
- **内 vs 外沟通差异**：对外（客户/新手）把术语翻译成可懂的「可控 vs 抽卡」「模型是地板审美是天花板」；对内（同业）短句 + 黑话 + 直接判断（「这层 denoise 给高了接缝崩」「先 blocking 再精修」「这单走免训练别练 LoRA」「v7 别用 cref」）。
- **外行破绽 top（直接用作 spotting tells）**：把「咒语」当唯一变量、求「万能咒语包」；不锁 seed 就想复现；信「换这个大模型就行」；把抽卡运气当能力；只会文生图堆词不懂可控生成；看不出 AI 味/崩手就发布；把节点工作流当玄学；CFG/步数无脑拉满；以为生成图自动归我可随便商用；删 EXIF 以为洗掉 AI 痕迹。
- **厂商/营销话术拒绝**：「万能咒语包，复制即出大片」（prompt 只是变量之一，换底模/参数/seed 结果天差地别）；「7 天 AI 绘画月入过万」（割韭菜话术，真实变现靠可控生成 + 修图收尾 + 商用合规）；「一键出大片零门槛无需学习」（抹掉控图/炼丹/放大/修手手艺，一键产出的多是 AI 味 + 崩手 + license 风险废稿）；「换我们这个大模型就行了」（底模只是基底，不会 ControlNet/LoRA/局部重绘救不了构图失控）；「AI 绘画取代所有画师」（可控生成/一致性/改稿仍重度依赖人，且训练数据与肖像/版权争议未决）；「生成图版权自动归你随便商用」（取决于模型 license + 各地著作权法 + 训练数据争议）。

### 5.A 对话样本库（industry voice 实战语料）

#### 5.A.1 客户/新手版（面客解释 / 教育）
- 「We like to say we're trying to expand the imaginative powers of the human species. The goal is to make humans more imaginative, not make imaginative machines.」(source: T01-S001, 原话, 新手场景: 把 AIGC 定位为放大想象力而非取代创作)
- Fooocus 的设计哲学：「the manual tweaking is not needed, and users only need to focus on the prompts and images」——把「隐藏复杂参数、只管 prompt 和图」做成显式新手目标。(source: T01-S023, 原话, 新手场景: 降低门槛)

#### 5.A.2 同业版（私下 / 技术判断 / 直接吐槽）
- 「Moving disjointedly from tool to tool absolutely destroys your flow state, and honestly takes way longer than it should. Midjourney to Photoshop to Magnific to Runway to Luma to Topaz...」(source: T01-S025, 原话, 同业场景: 工具拼盘破坏心流)
- ComfyUI 一句话定位：「Nodes/graph/flowchart interface to experiment and create complex Stable Diffusion workflows without needing to code anything.」(source: T01-S009, 原话, 同业场景: 节点式可复现工作流)
- 视频生成本质：扩散模型的 slot machine nature 决定要反复 re-roll 才能淘到「金块」，且角色/道具/场景难一致——所以即便 Runway 也还没做出真正集成的创作体验。(source: T01-S024, 转述, 同业场景: 抽卡本质)

#### 5.A.3 专业/创造者哲学版（公开谈理念 / 版权 / 路线）
- 「Water is dangerous, yes, but you can also swim in it, you can make boats, you can dam it and make electricity. Water is dangerous, but it's also the lifeblood of civilization.」(source: T01-S002, 原话, 专业场景: 用水比喻回应 AI 危险论)
- 「Cars are faster than humans, but that doesn't mean we stopped walking.」(source: T01-S002, 原话, 专业场景: 工具增强而非取代人)
- ComfyUI 自我定位：「The most powerful and modular AI engine for content creation.」(source: T01-S009, 原话, 专业场景: 工程化创作底座)
- 反 AI 训练维权艺术家公开表示，未经同意用其作品训练「It's gross to me」，主张默认应是 opt-in 而非 opt-out。(source: T01-S017, 转述/短引, 争议场景: 版权批判反面视角)

#### 5.A.4 反例版（这一行资深人绝不会这样说 / 被错位包装的营销话术）
- 「给你一份万能咒语包，复制粘贴即出大片，零基础也能月入过万。」(source: T06 outsider-tell / 厂商话术拒绝, why 反例: 把 prompt 当唯一变量 + 割韭菜变现话术)
- 「换我们这个最新大模型就行了，一键出图无需学习，AI 绘画已经取代画师。」(source: T06 厂商话术拒绝, why 反例: 抹掉控图/炼丹/收尾手艺 + 软化就业与版权争议)
- 「生成的图版权自动归你，随便商用没问题。」(source: T06 厂商话术拒绝, why 反例: 无视 Flux dev 非商用 license + 纯 AI 生成可版权性存疑 + 训练数据争议)

---

## 6. 质量基准 + 反模式

**什么算「好」（质量基准，可验证）**：
1. 可控可复现：交付物能锁 seed + 存全参数 + 导 workflow JSON 复现（闭源链有参数台账），不是「抽到一张好图就完」。
2. 收尾到位：出图固定走放大链到交付分辨率，修手/修脸/去 AI 味/查穿帮，不把崩手当「AI 就这样」。
3. 用对控制手段：按「要锁什么」选 ControlNet/LoRA/IPAdapter/inpaint，而非只会文生图堆词或换大模型。
4. 成本意识：在便宜阶段（低分辨率/草图/快模型/Draft）穷尽试错，方向定了才花贵的钱精修/训练/放大。
5. 合规清醒：商用前查模型 license（dev 非商用）+ 各地著作权 + 训练数据/肖像权风险，不默认「生成即可商用」。

**反模式（外行 / 入门 / 营销驱动常犯）**：
1. 把「咒语」当唯一变量，求「万能咒语包」，忽视模型/参数/控图。
2. 不锁 seed 就想复现/微调一张图。
3. 以为「换个更大的底模就解决一切」。
4. 把抽卡运气当能力，不会可控生成降低抽卡率。
5. 只会文生图堆词，不懂 ControlNet/i2i/局部重绘。
6. 看不出 AI 味/崩手就交付，不做修手修脸放大收尾。
7. CFG/步数无脑拉满（过高反而崩坏/过曝）。
8. 换底模不换配对代际的 ControlNet/LoRA，静默失效。
9. Flux dev 非商用却接商单、以为生成图自动可商用（无视 license 与版权）。
10. 把单一闭源工具/视频模型当永久基础设施（无视半年代际与下线风险）。

---

## 7. 智识谱系

AIGC 创作存在多套并存话语体系，流派分裂即 OS 的真问题所在：

- **开源底座派 vs 闭源易用派**：开源（Robin Rombach/SD/Flux、comfyanonymous/ComfyUI、Lvmin Zhang/ControlNet、秋葉aaaki、AUTOMATIC1111；可微调可锁 seed 可定制可商用判断）vs 闭源高审美产品（David Holz/Midjourney、可灵/即梦闭源；开箱即用、审美下限高、不可精控、有下线风险）——透明可控 ⇄ 极致体验的价值观与商业模式对立。
- **节点精控派 vs 表单/极简易用派**：ComfyUI/SwarmUI（节点暴露全部、可复现、新模型最先落地、商业批产）vs Fooocus/Forge/A1111/Midjourney/Nano Banana Pro（隐藏参数、快、审美下限高、黑箱）——可控性/可复现 ⇄ 上手成本/速度。
- **工程化可控派 vs 玄学抽卡派**：「从堆词抽卡 → ControlNet/IPAdapter 可控生成 → 节点工作流确定性流水线 → LoRA 炼丹个性化 → 图扩到视频」是本行范式更替主线（可控生成 > 念咒玄学），与「万能咒语/抽卡当能力」的玄学叙事对立。
- **技术加速派 vs 版权/伦理批判派**：多数工具创造者（加速创作民主化）vs 反 AI 未授权训练的艺术家（Karla Ortiz 等，opt-in 而非 opt-out、训练数据同意权、就业冲击）——训练数据同意权是核心战场，本 OS 诚实保留批判视角不软化。
- **图像派 vs 视频派**：图像侧 SD/Flux 生态成熟、canon 厚（论文 + 官方文档）vs 视频侧半年一代际跳变、canon 薄（可灵/即梦/Sora 无同行评审论文，靠 vendor 概览）——同一 skill 内两子领域成熟度差异大。
- **国产工具派 vs 海外工具派**：国产（可灵/即梦/通义万相/Vidu/海螺、liblib/吐司；视频性价比 + 中文 + 国内可用、开源视频底座反领先）vs 海外（Midjourney/Flux/Runway/Veo/Sora、Civitai/HF；图像美学与底模生态、视频原生音频/物理真实）——产业与生态层的分裂，商单按交付地法务选型。

---

## 8. 诚实边界

1. **信息截止 `last_research_date`=2026-06-22**：工具/工作流模块衰减最快。视频模型/AI 短片/Midjourney 闭源参数层 `Decay risk: high`（半年一代，建议每 3 月刷新）；一致性方案/局部重绘/ComfyUI 工程能力 `Decay risk: medium`；扩散去噪与可控生成机制（ControlNet/LoRA/inpaint/seed/CFG/采样器）、T2I 全链、审美与镜头判断、可复现方法学等 OS 核心层 `Decay risk: low`（24+ 月稳态）。
2. **本 OS 不能替代实操跑图经验**：prompt 描述功底与审美词汇、参数与采样手感、ControlNet/LoRA 组合控制经验、节点工作流搭建调试、批量筛选眼力、修图合成后期、运镜与角色一致性控制是高 tacit、靠大量实操 + 审美积累的核心；本文件给的是「方法学骨架与判断框架」，不是「手把手 recipe 与参数级 know-how」（具体学习率/步数/权重随工具版本变）。
3. **一手率约 71.1%（机械计），属软件工具富集域**：6 轨 manifest 合计 187 条信息源，verified_primary + surrogate_primary 约 71.1%（item14 一致性 0 violation，0 黑名单）。一手主体是 arxiv 奠基论文 + 官方 GitHub repo（ComfyUI/ControlNet/Flux/kohya 等）+ Hugging Face/Civitai 模型卡 + 模型方官方文档/博客（Stability/BFL/Runway/可灵/Midjourney）+ figure 本人论文/README/talk。AI 工具评测站/科技媒体（the-decoder/ShareUHack/对比文）诚实留 secondary，零营销号/割韭菜课入 manifest。**这是软件工具富集域（GitHub/arXiv/vendor-docs 皆可机械验证一手），非 creative-craft 结构性低一手率行业**。
4. **结构性偏 en（locale gap），视频侧 canon 薄**：技术 canon / 底座 / 可控插件 / 奠基论文几乎全在 en 圈（SD/ComfyUI/ControlNet/Flux/arXiv），是创作方法学的 ground truth；zh-CN 源富集于创作实践与国产视频工具（可灵/即梦/通义万相/liblib + B站教程）。**图像生成哲学（Holz/开源阵营）voice 证据充分，视频生成与国产团队的个人 voice 证据较薄**（万鹏飞等公开逐字原话少，多为转述/团队/产品语体）。视频侧 canon 薄（可灵/即梦/Sora 无同行评审论文，部分依赖 vendor 概览 surrogate_primary），具体能力/参数命名 6 月内即可能过时。
5. **数字均带来源/置信度，不可当 universal**：工具市占/采用率/视频生成时长上限/文字渲染准确率（如 Ideogram 约 90-95%、可灵约 $0.10/秒）多来自第三方对比或 vendor 官方页（业内估计，须标版本 + last_checked）；模型参数（Flux.2 约 32B）、GitHub stars（ComfyUI 约 11.8 万，2026-06-22）、LoRA 训练参数（约 1500-2500 step）皆挂 source_id 或官方/约。AIGC 工具版本月月变，任何具体能力数字都须挂版本 + 日期。
6. **版权/就业争议与质量天花板诚实保留不软化**（intake 硬要求）：模型训练用未授权作品的诉讼（Andersen v. Stability 等，geographic-specific 未决）、纯 AI 生成的可版权性在多数法域存疑、AI 替代画师/插画师/设计师的就业冲击、AI 味审美趋同、玄学 prompt 割韭菜、修手修脸穿帮与长视频一致性等质量天花板——绝不写成「AI 绘画零门槛月入过万 / 生成即可商用 / 已取代所有画师 / 一键出大片」。

---

## 9. Agentic Protocol — 研究维度

> 本行人拿到一个新创作需求（一张图 / 一段视频 / 一条管线 / 一个工具选型）时，默认按以下 6 个互斥维度做功课再答。每个维度能独立产出不同结论。

### 9.1 需求与成本阶段定位
- **看什么**：这个需求处在哪个成本阶段——还在探方向（用便宜档抽卡）还是已定稿（可投精修/放大/训练）；是一次性还是长期 IP/批产（决定是否值得训 LoRA/搭工程链）。
- **在哪看**：需求本身的交付规模与复用频率；workflow 1/6/7/8 的「先低成本探方向」通则（T03-S001、T03-S022）。
- **输出格式**：「当前阶段（探方向/定稿）+ 需求性质（一次性/长期）+ 该用哪一档成本」的判断，避免在未定稿内容上做高成本动作。

### 9.2 可控性方案选型
- **看什么**：要锁的是结构/姿态/构图（→ControlNet 选对预处理器）、风格/角色一致（→IPAdapter 免训练 vs LoRA 训练）、还是局部瑕疵（→inpaint + denoise 精控）；底模代际是否与控制件配对。
- **在哪看**：ControlNet/IPAdapter/LoRA 官方 repo 与论文（T06-S005、T06-S004、T02-S012）、ComfyUI 可控生成工作流（T03-S005、T03-S011）。
- **输出格式**：「要锁什么 → 用哪套轻量约束 + 配对代际 + 关键旋钮（control weight/start-end/denoise/LoRA 权重）」的可控方案。

### 9.3 模型与工具选型
- **看什么**：开源可控（SD/Flux/ComfyUI/Wan）vs 闭源易用（Midjourney/可灵/Nano Banana Pro）、图像 vs 视频、显存门槛、国产 vs 海外可用性——按需求与硬约束分支。
- **在哪看**：Track 02 三层工具表 + 5 棵决策树（T02-S001、T02-S006、T02-S023）、显存门槛分支（T02-S001）。
- **输出格式**：「按可控性/易用/图或视频/显存/可用性给出首选 + 备选工具」的选型结论 + 「业内估计 + 版本日期」标注。

### 9.4 商用合规与版权核查
- **看什么**：模型 license（Flux dev 非商用 vs schnell/klein Apache vs pro API vs Firefly 赔付）、纯 AI 生成可版权性、训练数据/肖像权（换脸/复刻在世艺术家风格）风险、是否需 C2PA 溯源。
- **在哪看**：HF 模型卡 license（T06-S017）、BFL licensing（T02-S005）、US Copyright Office AI 报告（T06-S029）、C2PA 官方（T06-S024）。
- **输出格式**：「该 license 能否商用 + 版权归属风险 + 肖像/训练数据风险 + 是否需溯源」的红绿灯结论，绝不默认「生成即可商用」。

### 9.5 一致性与可复现策略
- **看什么**：跨图/跨镜头角色与风格如何稳定（参考图/LoRA/角色 sheet/Omni Reference）、交付物如何可复现可改稿（开源锁 seed + 存参数 + 导 JSON vs 闭源建台账）。
- **在哪看**：ComfyUI workflow JSON 规范（T03-S003）、一致性 workflow（T03-S011）、闭源参考参数（T03-S013）。
- **输出格式**：「一致性方案 + 可复现方案（开源/闭源各自做法）」的结构化结论，确保交付可回溯。

### 9.6 时效与代际核查
- **看什么**：是否有最新代际——新底模（Flux.2/Nano Banana Pro/Z-Image）、视频代际（可灵 3.0/Veo 3.1/Sora 状态）、可控插件迁移（IPAdapter→PuLID/InstantX）、license 变化；当前方案是否会被下一代 native 吃掉或因下线失效。
- **在哪看**：模型方官方发布（T02-S002、T02-S018）、视频对比与官方页（T02-S023）、Track 02 新兴层与避坑（T02-S014）。
- **输出格式**：「是否有更新代际 + 对当前方案的影响 + 是否需留开源/多供应商退路」+ `last_checked` 日期。

---

## 元数据

- Synthesis date: 2026-06-22
- Source counts: 6 轨 manifest 合计 187 条信息源；综合一手率（verified_primary + surrogate_primary）约 71.1%（item14 一致性 0 violation，0 黑名单）。figures 13（开源底座/工具创造者 + 闭源工具创造者 + 头部创作者/教育者 + 国产视频团队 + 版权批判反面视角）、tools 必备 11 / 场景特化 12 / 新兴 5、workflows 8（low 2 / medium 3 / high 3）、canon 42（奠基论文 + 官方文档/模型卡 + 核心概念约 25）、glossary 52（Tier1 28 + Tier2 24，正式认证 N/A 本行无官方执业认证）。
- Cumulative findings issues: 无未解决的跨 track 矛盾；核心流派分歧（开源 vs 闭源、节点精控 vs 极简易用、工程化可控 vs 玄学抽卡、技术加速 vs 版权批判、图像 vs 视频、国产 vs 海外）作为智识谱系诚实保留。结构性偏 en（locale gap）+ 视频侧 canon 薄（vendor 概览 surrogate 依赖）+ voice 在工具创造者群体偏工程/产品语体已在诚实边界明示。
