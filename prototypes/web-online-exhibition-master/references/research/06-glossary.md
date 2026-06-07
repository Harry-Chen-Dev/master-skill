# Track 06 — Glossary + 流派分歧矩阵：Web 线上展览 / 虚拟展厅开发

> Research date: 2026-06-06 · Locale: zh-CN（canon 全球）· OPUS subagent
> 本 track = **术语标准 + 学派对照**。本行核心分歧明确集中在三刀：**自研 vs SaaS**、**真 3D vs 全景**、**mesh vs 辐射场(高斯泼溅/NeRF)**。
> 这是一个**工程化、规范驱动、几乎无学术 textbook** 的领域 —— 术语主体是 Khronos/W3C 一手规范 + 顶级开源项目文档里的概念，"外行易错"集中在「把全景当 3D / 把 draw call 当帧率 / 把 SaaS 可导出当可二开 / 6DoF 混 3DoF」。
> **诚实判断**：术语维度**信号厚**（≥30 个，Tier 1 全部有 outsider-tell）；分歧矩阵**异常清晰**（figures 已给 7 组立场光谱，canon 已给 5 条 still-debated 矛盾，本 track 收敛为 7 轴 + 4 张关键差异对照）。薄弱点：国内 SaaS（众趣/酷雷曼/720云）一手术语定义被黑名单（知乎/公众号/CSDN）垄断，只能用 vendor docs surrogate。

## Source Manifest

| source_id | url | bucket | last_checked | author/host | one-line note |
|-----------|-----|--------|--------------|-------------|---------------|
| T06-S001 | https://developer.mozilla.org/en-US/docs/Web/API/WebXR_Device_API/Fundamentals | verified_primary | 2026-06-06 | MDN | 3DoF/6DoF/inline-vs-immersive 权威定义 + "WebXR 不是渲染技术" |
| T06-S002 | https://developer.mozilla.org/en-US/docs/Web/API/WebGPU_API | verified_primary | 2026-06-06 | MDN | WebGPU 定义 + 对 WebGL 差异 + compute + WGSL(Rust-like) |
| T06-S003 | https://www.w3.org/TR/WGSL/ | verified_primary | 2026-06-06 | W3C | WebGPU Shading Language 规范（WGSL 一手） |
| T06-S004 | https://developer.mozilla.org/en-US/docs/Web/API/InstancedMesh | verified_primary | 2026-06-06 | MDN | InstancedMesh：一次 draw call 画多份相同几何 |
| T06-S005 | https://threejs.org/manual/en/cleanup.html | verified_primary | 2026-06-06 | three.js | dispose 一手："three.js 无法自动回收, 责任交还给你"（官方 manual） |
| T06-S006 | https://threejs.org/docs/#api/en/renderers/WebGLRenderer.setPixelRatio | verified_primary | 2026-06-06 | three.js | setPixelRatio / devicePixelRatio API（官方 docs） |
| T06-S007 | https://iiif.io/api/presentation/3.0/ | verified_primary | 2026-06-06 | IIIF Consortium | IIIF Presentation API 3.0 + Manifest 定义（标准机构一手） |

> bucket 说明：沿用 Wave-1（T02/T04）已确立约定 —— `source_verifier.py classify` 对 `threejs.org` / `iiif.io` / `gpuweb.github.io` / `web.dev` 默认给 `secondary`（unknown host），但 brief bucket 定义把 **官方项目文档 / 标准机构 spec / web.dev** 上调 `verified_primary` 并在 note 标官方身份；MDN / W3C / GitHub repo root 由 verifier 直接判 `verified_primary`。商业 SaaS 营销页（Matterport/众趣/酷雷曼/720云/krpano/3DVista 等）一律 `surrogate_primary` note=`vendor docs`，见 T02 manifest（本 track 不重复收，evidence 直接引 T02-S0xx）。**黑名单（知乎/公众号/百度百科/CSDN/简书/掘金/G2/Capterra）零收录**。
> **跨轨复用**：本 track 大量 evidence 直接引 Wave-1 source_id（`T01-Sxxx` figures / `T02-Sxxx` tools / `T04-Sxxx` canon）—— 术语定义与流派立场的一手出处已在 Wave-1 落表，本 track 复用而非重抓。新增 7 个源专补「Wave-1 未单独落表」的术语点（3DoF/6DoF 定义原文、WGSL spec、InstancedMesh、dispose manual、pixelRatio、IIIF Presentation API、WebGPU 概念页）。

---

## 总览（按 type 分组）

> 本行 type 分布（按行业类型）：**Term / 术语 极多、Standard 多（规范驱动）、Acronym 中、Regulation 少（仅文博数字化国标 + 无障碍）、Certification ≈ N/A**（web 开发无强制执业认证；这是技术/工程类行业的典型形态，见 Track 06 prompt「LLM agent infra 几乎无认证」同构）。

### Tier 1 — 核心必懂（22 个）

| 术语 | Type | Insider def | Outsider tell | Last_updated |
|------|------|-------------|---------------|--------------|
| glTF / GLB | term+standard | 3D 资产传输/运行时格式, "JPEG of 3D"; GLB=单文件二进制 | 把它当"建模格式"想在里面雕模型（它是末端传输格式, 建模在 Blender） | ISO 2022 |
| Draco | term | KHR 几何压缩, 体积降 90-95%, 但客户端解码有 CPU 开销 | 以为"压缩=只有好处"（解码吃 CPU, 移动端可能 jank） | 稳定 |
| KTX2 / Basis Universal | term+standard | GPU 纹理压缩容器, **在显存里保持压缩**, 省 ~10x VRAM | 用 JPEG/PNG 当"已经压缩了"（它们在显存里解压、爆显存） | 稳定 |
| Meshopt (EXT_meshopt_compression) | term+standard | 顶点/索引压缩, 保 GPU cache 顺序, 解码快、能压动画 | 与 Draco 混为一谈（二者是真实分歧, 不是同一个东西） | 稳定 |
| glTF-Transform | term | glTF 优化管线 SDK/CLI, 一条 `optimize` 串起 draco+ktx2+dedup | 以为"上线直接传原始 GLB 就行"（不压必崩） | rolling |
| LOD（细节层次） | term+acronym | Level Of Detail, 按距离切模型精度, 远处低面数 | 读成"洛德"/不知是 L-O-D 三字母; 以为"高模到处用更真" | 稳定 |
| draw call | term | 一次 GPU 绘制提交; 过多=CPU 瓶颈, 目标 <100 才稳 60fps | **把 draw call 当帧率指标**（它是 CPU 提交次数, 不是 fps） | 稳定 |
| instancing（实例化） | term | 几何只上传一次、GPU 复用多份, 一次 draw call 画一片 | 以为"复制 100 棵树 = 100 个 mesh 没问题"（draw call 爆） | 稳定 |
| frustum culling（视锥剔除） | term | 不绘制相机视锥外的物体, 引擎默认开 | 以为"看不见的也在渲染拖慢"（默认已剔除; 真瓶颈常是 draw call） | 稳定 |
| 显存 / VRAM | term+acronym | GPU 内存, 按纹理像素数算, 移动端是**硬上限** | 把 VRAM 当系统 RAM; 以为"内存够大就行"（移动端 VRAM 远小） | 稳定 |
| 全景 / panorama / 720 | term | 拍摄拼接的 360° 图像漫游, 站点跳转 + 看图 | **把全景当真 3D 卖**（不能走动/绕物/交互展品） | 稳定 |
| 真 3D | term | 可自由漫游 + 绕物体 + 拾取交互的实时渲染场景 | 以为"720 全景 = 3D"（全景是图、真 3D 是实时几何） | 稳定 |
| 6DoF vs 3DoF | term+acronym | 6DoF=旋转+平移(可走动); 3DoF=仅旋转(roll/pitch/yaw) | **把 3DoF 当 6DoF**（全景/手机陀螺仪是 3DoF, 不能位移） | 稳定 |
| WebGL | term+acronym | 浏览器无插件 3D 现役底座, 基于 OpenGL ES, 兼容性王 | 以为已被 WebGPU 取代（仍是兼容性底线、fallback 目标） | 稳定 |
| WebGPU | term+acronym | 下一代 GPU API, 对齐 Vulkan/Metal/D3D12, 有 compute | 以为"WebGPU=WebGL2 升级版"（规范明说与 WebGL 无关） | medium |
| WebXR | term+acronym | web 访问 VR/AR 硬件的 W3C API; **本身不做渲染** | 以为 WebXR 负责画 3D（它只管时序/视点/输入, 渲染靠 Three.js） | medium |
| 高斯泼溅 3DGS | term+acronym | 3D Gaussian Splatting, 各向异性高斯做实时真实感重建 | 以为"扫一扫就能像 mesh 一样编辑/换材质"（splat 编辑难） | high |
| NeRF | term+acronym | Neural Radiance Field, 神经隐式场新视角合成 | 读成"纳夫"/不知是 NeRF; 以为 NeRF=实时（原版慢, 3DGS 才实时） | high |
| 热点 hotspot | term | 3D/全景中可交互标注点(图文/语音/跳转), 锚在空间坐标 | 以为是"网页热区 image-map"（它锚在 3D 位置, 随视角动） | 稳定 |
| 首屏 / 首帧可交互 | term | 加载优先派第一性指标: 多久能看到/转动场景 | 只看"总加载完成", 忽略首屏（用户在首屏前就跑了） | 稳定 |
| 降级 / fallback | term | WebGPU→WebGL2→全景/低配的渐进退路, 不支持时不白屏 | 不做 fallback, ~5% 用户/旧设备/iOS 直接白屏 | 稳定 |
| IIIF | standard+acronym | 文博图像互操作框架(Image+Presentation API), 深缩放/标注 | 读不出 "triple-eye-eff"; 以为"就是个图片 CDN"（是元数据+互操作标准） | 稳定 |

### Tier 2 — 周边熟知（11 个）

| 术语 | Type | Insider def | Last_updated |
|------|------|-------------|--------------|
| TSL（Three Shading Language） | term+acronym | Three.js node 材质 shader 语言, 写一次跨 WGSL/GLSL 编译 | rolling |
| WGSL | standard+acronym | WebGPU Shading Language, "Rust-like" 低层着色语言 | medium |
| pixelRatio / devicePixelRatio | term | 渲染分辨率倍率; 移动端常 cap 到 1-2 防显存/性能爆 | 稳定 |
| dispose | term | 手动释放 geometry/material/texture; three.js **不自动回收** | 稳定 |
| 数字孪生（digital twin） | term | 实体空间/文物的高保真可量测数字镜像 | 稳定 |
| 动线设计 | term | 策展引导的参观路径/视角序列(展览叙事的空间编排) | 稳定 |
| CDN 流式 / 渐进加载 | term | 模型经 CDN 分块/LOD 流式下发, 先低质代理后高质 | medium |
| PBR（基于物理渲染） | term+acronym | 物理正确材质/光照, glTF 默认材质体系 | 稳定 |
| Mipmap | term | 纹理多级缩略, 省带宽+抗闪烁, ~30% 显存开销 | 稳定 |
| batching / 合批 | term | 合并多次绘制为更少更大 draw call | 稳定 |
| USDZ | term+standard | iOS AR Quick Look 用的苹果系 3D 格式(glTF 之外的兜底) | 稳定 |

### Standards / Regulations 时间轴（仅近 5 年内有显著变化的进表）

| 名称 | 制定者 | Issued | 状态(2026-06) | Decay |
|------|--------|--------|--------------|-------|
| WebGPU | W3C | CR Draft | Candidate Recommendation Draft 2026-05（铺开中, 2025 末各浏览器达基线）(evidence: [T04-S002, T02-S030]) | medium |
| WGSL | W3C | 随 WebGPU | 与 WebGPU 同步推进 (evidence: [T06-S003]) | medium |
| WebXR Device API | W3C | CR Draft | CR Draft 2026-03-16, 推 PR 需 ≥2 互操作实现 (evidence: [T04-S003]) | medium |
| glTF Gaussian Splatting 扩展 | Khronos | 2025 | Khronos 已发 glTF 高斯泼溅扩展, mesh/辐射场开始收敛 (evidence: [T01-S037, T01-S038]) | high |
| glTF 2.0 | Khronos | 2017→ISO 2022 | ISO/IEC 12113:2022 定稿（极稳定）(evidence: [T04-S001]) | low |
| DB11/T 1922-2021 文物三维数字化 器物 | 北京市文物局 | 2021(2022-04 实施) | 现行（文博考据派 ground truth）(evidence: [T04-S021]) | low |
| 可移动文物数字化采集 行标 | 国家文物局 | 现行 | 全国文保标委归口 (evidence: [T04-S022]) | low |

> **Certification = N/A**：web 前端/3D 开发**无强制执业/产品认证**（不像医疗/金融）。唯一沾边的是 WCAG 无障碍合规与文博采集国标的"成果验收"门槛——属 Regulation 而非 Certification。Phase 2 应明确报「本行 Certification 维度 N/A，属技术工程行业常态」。

### 行业「外行破绽」高亮（最容易暴露的 10 条 insider-only spotting tells）

| 误用 | 内行实际意思 | 频率 |
|------|------------|------|
| "做个 3D 展厅"指着 720 全景 | 全景 ≠ 真 3D; 不能走动/绕物/拾取（这是第一刀分叉）(evidence: [T02-S016, T04-S016 概念16]) | 极高 |
| "draw call 多少？"当帧率问 | draw call = CPU 提交次数, 不是 fps; <100 才稳 60fps (evidence: [T02-S032]) | 高 |
| "SaaS 能导出, 所以能二开" | 可导出 ≠ 可二次开发; Matterport 可 iframe 嵌但内容锁云、断订阅即下线 (evidence: [T02-S022, T02-S026]) | 高 |
| "我们要 VR 沉浸"但只给 3DoF | 6DoF(可走动) ≠ 3DoF(仅转头); 全景/手机陀螺仪是 3DoF (evidence: [T06-S001]) | 高 |
| "模型传上去就行"不压缩 | 不走 glTF-Transform 压缩三件套, 50MB GLB 首屏崩 (evidence: [T02-S008, T02-S032]) | 高 |
| "WebGPU 是 WebGL 升级版" | 规范明说"与 WebGL 无关、不针对 OpenGL ES"; 是全新 API (evidence: [T04-S002]) | 中 |
| "WebXR 来渲染 3D" | WebXR 不是渲染技术, 只管视点/时序/输入, 渲染靠 Three.js/引擎 (evidence: [T06-S001]) | 中 |
| 用 JPEG/PNG 纹理"反正压过了" | 传统图在显存里解压、爆 VRAM; 要 KTX2 在 GPU 上保持压缩 (evidence: [T02-S011]) | 中 |
| "高斯泼溅扫一扫就能像 mesh 改" | splat/辐射场编辑难、与 glTF 管线整合尚早 (evidence: [T01-S037, T04-S019]) | 中 |
| IIIF 读不出 / 当"图片 CDN" | "triple-eye-eff", 是图像互操作+元数据标准, 不是单纯图床 (evidence: [T06-S007, T04-S018]) | 中(文博圈) |

---

## 术语详述（仅挑 Wave-1 未充分定义 / 易错点密集的，其余见上表 + 引 Wave-1 source）

### 6DoF vs 3DoF — 六自由度 vs 三自由度
- **Type**: term + acronym · **Tier**: tier-1
- **Insider def**: 6DoF = 旋转(roll/pitch/yaw) + 平移(前后/左右/上下), 能在空间里**走动**; 3DoF = 只有三个旋转轴, 只能**转头看**不能位移 (evidence: [T06-S001], 一手)
- **Outsider-friendly**: 3DoF 像"站着不动转头"(全景/早期 VR 盒子); 6DoF 像"在房间里走来走去"(Quest/PICO 真 VR)
- **常见误用 (outsider-tell)**:
  - `semantic_tell`: 客户说"要 VR 沉浸自由漫游"却接受全景方案 —— 全景本质 3DoF, 给不了 6DoF 的走动; 验收必翻车 (evidence: [T06-S001], 一手)
  - `pronunciation_tell`: 念 "六-dof"/"three-dee-of"; 内行说 "six-dee-oh-eff" / "three-dof"
  - `usage_tell`: 把"手机陀螺仪转视角"当 6DoF（那是 3DoF）
- **关联**: WebXR, 全景, 真 3D · **可信度**: high · **Decay**: low

### draw call — 绘制调用
- **Type**: term · **Tier**: tier-1
- **Insider def**: CPU 向 GPU 提交"画这一批"的一次命令; 数量过多 → CPU 成瓶颈, 行业经验目标 **<100 draw calls** 才稳 60fps (evidence: [T02-S032], 一手)
- **常见误用 (outsider-tell)**:
  - `semantic_tell`: **把 draw call 当帧率/性能直接指标** —— 它是 CPU 侧提交次数, 高 draw call 拖 CPU 但和 GPU 像素负载是两回事; 降 draw call 靠 instancing/合批/合并贴图 (evidence: [T06-S004, T02-S032])
  - `usage_tell`: 重复展品/道具直接复制成 N 个 mesh（应 InstancedMesh 一次画一片）(evidence: [T06-S004])
- **关联**: instancing, batching, frustum culling · **可信度**: high · **Decay**: low

### WebXR — web 端 XR
- **Type**: term + acronym · **Tier**: tier-1
- **Insider def**: 让 web 访问 VR/AR 硬件(传感器+头显)的 W3C API, 分 inline / immersive-vr / immersive-ar session; **关键: 它本身不渲染** (evidence: [T06-S001, T04-S003], 一手)
- **Etymology**: Web + XR(eXtended Reality); 前身 WebVR
- **常见误用 (outsider-tell)**:
  - `semantic_tell`: 以为"用 WebXR 来画 3D 模型" —— MDN 原文: *"WebXR is not a rendering technology and does not provide features for managing 3D data or rendering it"*; 它只管时序/视点/输入, 渲染要 WebGL/Three.js/Babylon (evidence: [T06-S001], 一手)
  - `usage_tell`: 指望 iOS Safari 的 immersive WebXR 做沉浸 VR（支持仍弱, 移动 AR 走 model-viewer/USDZ 兜底）(evidence: [T02-S007, T02-S014])
- **关联**: 6DoF, WebGPU, A-Frame · **可信度**: high · **Decay**: medium

### dispose / VRAM / pixelRatio — 性能命门三件（外行最易漏）
- **Type**: term · **Tier**: tier-1(VRAM) / tier-2(dispose, pixelRatio)
- **dispose insider def**: three.js **不会自动回收** GPU 资源; 官方 manual 原文: *"three.js can not automatically clean these resources up... it's up to you to manage them. This is an issue of how WebGL is designed"* —— 不手动 `.dispose()` geometry/material/texture, 多展厅切换必泄漏 (evidence: [T06-S005], 一手)
- **pixelRatio insider def**: `renderer.setPixelRatio(devicePixelRatio)` 控渲染分辨率倍率; 高 DPI 手机若不 cap(常设 1-2), 像素翻数倍直接爆显存/掉帧 (evidence: [T06-S006, T02-S032])
- **VRAM 常见误用**: 把 VRAM 当系统 RAM; 移动端 VRAM 远小, 一张未压缩 1024² 纹理吃 4-6MB, 不转 KTX2 几张就爆 (evidence: [T06-S005, T02-S011])
- **关联**: KTX2, draw call, fallback · **可信度**: high · **Decay**: low

### 高斯泼溅 3DGS / NeRF — 辐射场两兄弟
- **Type**: term + acronym · **Tier**: tier-1
- **Insider def**: 3DGS = 用各向异性 3D 高斯 + 可见性感知光栅化, ≥30fps@1080p **实时**真实感重建, **非神经网络**; NeRF = 神经隐式辐射场, 是 3DGS 的前驱、原版慢 (evidence: [T04-S019, T04-S020], 一手)
- **常见误用 (outsider-tell)**:
  - `semantic_tell`: 以为"高斯泼溅扫一扫就能像 mesh 一样编辑/换材质/做碰撞" —— splat 编辑难、与 glTF 管线整合尚早(虽 Khronos 2025 已出扩展开始收敛)(evidence: [T01-S037, T01-S038])
  - `pronunciation_tell`: NeRF 念 "纳夫"/不知是 N-e-R-F(Neural Radiance Field)
  - `usage_tell`: 把 NeRF 当实时方案（实时主力是 3DGS, 不是原版 NeRF）(evidence: [T04-S019, T04-S020])
- **关联**: mesh, 数字孪生, glTF · **可信度**: high · **Decay**: high

---

## 流派分歧矩阵（framework 甜区 —— **保留分歧, 不强行统一**）

> 每轴：各派主张 / 代表人物或方案 / 适用场景 / 核心分歧。立场出处见 figures 7 组光谱(T01 Phase2)+canon 5 矛盾(T04 Phase2)。

### 轴 1 — 自研(Three.js/R3F/Babylon) vs SaaS 平台(Matterport/众趣/酷雷曼/720云)
| 维度 | 自研派 | SaaS 平台派 |
|------|--------|------------|
| 主张 | 品牌级独特体验、深度交互、长期可控、无锁定、可出海 | 工期/预算/无 3D 团队下最快出活, 自带营销/分发 |
| 代表 | mrdoob(Three.js) / Paul Henschel(R3F) / Bruno Simon / David Catuhe(Babylon) (evidence: [T01-S001, T01-S012, T01-S022]) | Matt Bell(Matterport) / 众趣高翔 / 酷雷曼 / 720云 (evidence: [T01-S044, T01-S045, T02-S027]) |
| 适用 | 产品配置器、沉浸数字展厅、品牌活动、出海 | 国内走微信/抖音小程序、文博/政务/营销快速实景上线 |
| **核心分歧** | 自研**灵活但贵且慢、性能要自己兜**; SaaS**省事快但二开自由度低、可能锁定**（断订阅即下线、内容锁云）(evidence: [T02-S022, T02-S026]) | 折中: 可导出自托管(3DVista 导 ZIP)/可 OEM(酷雷曼) (evidence: [T02-S026, T02-S028]) |

### 轴 2 — 真 3D 重场景 vs 720 全景轻量
| 维度 | 真 3D 派 | 全景 720 派 |
|------|----------|------------|
| 主张 | 自由漫游 + 绕物 + 可拾取交互展品才叫"沉浸" | 实景展馆站点跳转看图足够, 成本/工期碾压 |
| 代表 | Three.js/R3F/引擎自研; PlayCanvas (evidence: [T01-S001, T02-S005]) | Pannellum/Photo Sphere Viewer/krpano/720云 (evidence: [T02-S016, T02-S017, T02-S019]) |
| 适用 | 产品/数字展厅/需交互 | 实景展厅漫游/文博走廊/预算工期紧 |
| **核心分歧** | 全景**不能自由走动/绕物/交互展品**(本质 3DoF 图像); 真 3D **重、贵、性能挑战大**。客户要"沉浸自由漫游"却给全景 = 验收翻车(第一刀分叉) (evidence: [T02-S016, T06-S001]) | |

### 轴 3 — 命令式(Three.js) vs 声明式(React Three Fiber)
| 维度 | 命令式 vanilla 派 | 声明式组件化派 |
|------|------------------|---------------|
| 主张 | 手写 Three.js 极致掌控/性能, 不被抽象层挡 | 用 React 组件声明场景图、可组合、复用、接 React 生态 |
| 代表 | Bruno Simon(vanilla 偏好) / SimonDev (evidence: [T01-S007, T01-S031]) | Paul Henschel(R3F/drei) / Maxime Heckel (evidence: [T01-S012, T01-S029]) |
| 适用 | 非 React / 要最底层控制 / 极致性能 | React/Next.js 站内 / 团队已有 React 技能 |
| **核心分歧** | 批评者: R3F 抽象层在极致性能/复杂场景**不如手写 vanilla 可控**; 拥护者: 声明式可组合性 + 生态(drei/gltfjsx)开发更快 (evidence: [T01-S007, T01-S012]) | |

### 轴 4 — WebGL(稳) vs WebGPU/TSL(新)
| 维度 | WebGL 稳态派 | WebGPU/TSL 新兴派 |
|------|------------|------------------|
| 主张 | 兼容性王、十年验证、是 fallback 底线 | 现代 GPU API + compute、性能未来; TSL 写一次跨后端 |
| 代表 | 存量项目 / 兼容性优先 (evidence: [T04-S004]) | mrdoob(`three/webgpu`+TSL) / Maxime Heckel (evidence: [T01-S005, T01-S030, T02-S030]) |
| 适用 | WebGL 上已流畅的存量展厅 | 新项目 / 50k+ 粒子 / compute 重负载 |
| **核心分歧** | WebGPU 规范明说"与 WebGL 无关、不针对 OpenGL ES"(S002)、仍 CRD; **TSL/WebGPU 迁移社区有反弹**——为 WebGL 写的材质在 WebGPU 全废、要维护两套, EffectComposer/自定义 shader 要改写 (evidence: [T04-S002, T01-S006, T02-S002]) | |

### 轴 5 — 网格 mesh vs 辐射场(高斯泼溅/NeRF) 做展品/场景重建
| 维度 | 网格几何派 | 辐射场/泼溅派 |
|------|-----------|--------------|
| 主张 | glTF mesh 成熟可控、可编辑/换材质/碰撞、管线完整 | 实景"扫描即展厅"真实感碾压、跳过繁重建模 |
| 代表 | Don McCurdy/Patrick Cozzi(glTF 标准体系) (evidence: [T01-S018, T01-S036]) | Mark Kellogg(GaussianSplats3D) / Will Eastcott(SuperSplat) (evidence: [T01-S032, T01-S034]) |
| 适用 | 需交互/可改/跨引擎的展品 | 高保真实景/文物原貌重建展示 |
| **核心分歧** | 3DGS **真实感强但体积大、编辑难、与 glTF 整合尚早、移动端兼容仍演进**; mesh 成熟但建模成本高、真实感受限。2025 起 Khronos 扩展令两派**开始收敛** (evidence: [T01-S037, T01-S038, T04-S019]) | |

### 轴 6 — 文博考据派 vs 营销转化派（目标/验收完全不同）
| 维度 | 文博考据派 | 营销转化派 |
|------|-----------|-----------|
| 主张 | 高保真、合规采集、可量测、忠于原物(数字博物馆) | 转化/留资/分发优先、埋点带看直播(商业云展厅) |
| 代表 | IIIF + 国家文物局国标 + Amit Sood(Google A&C gigapixel) (evidence: [T04-S018, T04-S021, T01-S039]) | 众趣 Qverse/酷雷曼营销能力(表单/带看/直播/数据分析) (evidence: [T02-S027, T02-S028]) |
| 验收 | 采集精度/色彩/合规(DB11/T 1922、行标) | 停留/转化/线索数/小程序分发 |
| **核心分歧** | **两套质量标准互不通约**: 考据派的"忠实/合规"vs 转化派的"埋点/ROI"; 考据派常忽视转化, 转化派常忽视采集合规门槛 (evidence: [T04-S018, T04-S021, T02-S027]) | |

### 轴 7 — 沉浸优先 vs 加载优先（性能不可能三角）
| 维度 | 沉浸优先派 | 加载优先派 |
|------|-----------|-----------|
| 主张 | 高模/高纹理/后期/真 3D 体验质感拉满 | 先算显存预算 + draw call 预算 + 首屏, 再谈沉浸 |
| 代表 | 视觉/shader 工艺(部分 Maxime Heckel) (evidence: [T01-S029]) | MDN/web.dev 性能 canon + Bruno Simon("四分之一算力、各设备能跑") (evidence: [T04-S016, T01-S010]) |
| 适用 | 旗舰展厅、桌面高带宽 | 移动端、大众分发、首屏留存敏感 |
| **核心分歧** | "**画质 × 性能 × 加载速度**"三者不可能同时拉满的不可能三角; Bruno Simon 处中间（既要视觉又强调性能约束）(evidence: [T01-S010, T04-S016]) | |

---

## 关键差异对照（4 张决策表）

### 对照 A — 全景 vs 真 3D
| 维度 | 720 全景 | 真 3D |
|------|---------|-------|
| 成本 | 低（拍摄+拼接） | 高（建模+开发+优化） |
| 工期 | 短（天级） | 长（周-月级） |
| 沉浸 | 3DoF, 站点跳转看图 | 6DoF, 自由漫游绕物 |
| 性能 | 轻（图像, Pannellum 仅 21KB） | 重（几何/纹理/显存挑战） |
| 交互 | 热点跳转/图文, 展品**不可拾取** | 可拾取/可配置/可触发逻辑 |
| 结论 | 实景漫游/预算紧/不需交互 → 全景; 需走动+交互 → 真 3D（**第一刀分叉**）(evidence: [T02-S016, T06-S001]) | |

### 对照 B — 自研 vs SaaS
| 维度 | 自研(Three.js/R3F/引擎) | SaaS(Matterport/众趣等) |
|------|------------------------|------------------------|
| 灵活/定制 | 高（任意体验） | 低-中（平台框架内） |
| 成本 | 高（团队+周期） | 低-中（订阅/买断） |
| 周期 | 长 | 短（最快当天上线） |
| 锁定 | 无 | 有（Matterport/Kuula 云端独占不可导出, 断订阅即下线） |
| 二开 | 完全自由 | 受限（Matterport SDK 生产用需付费订阅; **可导出 ≠ 可二开**） |
| 折中 | — | 可导出: 3DVista(ZIP)/Panoee; 可 OEM: 酷雷曼私有部署 |
| 结论 | 品牌级/出海/深交互 → 自研; 快/省/小程序分发 → SaaS; 怕锁定要二开 → 选可导出/可 OEM (evidence: [T02-S022, T02-S026, T02-S028]) | |

### 对照 C — web vs 原生 VR App
| 维度 | web(WebGL/WebGPU/WebXR) | 原生 VR App(Unity/Unreal) |
|------|------------------------|--------------------------|
| 触达 | 链接即开、无需安装、跨设备（"web 即 metaverse"）(evidence: [T01-S027]) | 需下载安装、应用商店审核 |
| 性能上限 | 受浏览器/显存约束（"约四分之一算力"）(evidence: [T01-S010]) | 更高、可榨硬件 |
| iOS immersive VR | 弱（Safari 支持差, 走 model-viewer/USDZ 兜底）(evidence: [T02-S007]) | 平台原生支持 |
| 永久性 | web 标准"今天能跑十年后还能跑"(evidence: [T01-S027]) | 依赖引擎版本/平台 |
| 结论 | 大众触达/分发/线上展览主路径 → web; 极致性能/重度 VR → 原生 | |

### 对照 D — mesh vs 高斯泼溅
| 维度 | mesh(glTF) | 高斯泼溅 3DGS |
|------|-----------|--------------|
| 建模成本 | 高（人工建模/雕刻） | 低（拍照→重建, "扫描即展厅"） |
| 真实感 | 受建模/材质水平限 | 高（实景级写实） |
| 性能 | 成熟可控（压缩三件套） | 体积大、移动端兼容仍演进 |
| 可编辑/交互 | 强（换材质/碰撞/拾取） | 弱（编辑难、整合 glTF 尚早） |
| 成熟度 | 高（ISO 标准+完整生态） | 新兴（2025 Khronos 扩展起收敛）(evidence: [T01-S037, T01-S038]) |
| 结论 | 需交互/可改/跨引擎 → mesh; 高保真实景原貌 → 3DGS（两派 2025 起收敛）(evidence: [T04-S019, T01-S038]) | |

---

## Phase 2 提炼提示

**「行业表达 DNA」直接素材**:
- **高频黑话 top 10**: glTF/GLB、draw call、Draco、KTX2、LOD、instancing、首屏、显存/VRAM、6DoF/3DoF、高斯泼溅(3DGS)
- **行业拒绝的厂商话术 top 5**（拒绝 → 价值观/反模式）:
  1. 把"720 全景"营销成"3D/沉浸 VR"（拒: 全景是 3DoF 图像, 不是真 3D）(evidence: [T02-S016])
  2. SaaS"可导出/可嵌入"暗示"可二开/无锁定"（拒: 可导出 ≠ 可二开; 嵌 iframe 内容仍锁云）(evidence: [T02-S022, T02-S026])
  3. "WebGPU = WebGL 升级"（拒: 规范明说与 WebGL 无关）(evidence: [T04-S002])
  4. "AI 一键生成虚拟展厅"当品牌级方案（拒: 单源 vendor 宣称、品牌精控仍需人工+自研）(evidence: [T02-S027])
  5. 数字孪生/扫描营销成"随便扫扫即可量测合规"（拒: 文博有 DB11/国标采集门槛）(evidence: [T04-S021])
- **外行破绽 top 10**: 见上「外行破绽高亮」表（全景当 3D / draw call 当帧率 / 可导出当可二开 / 3DoF 当 6DoF / 不压缩直接传 / WebGPU=WebGL2 / WebXR 来渲染 / JPEG 纹理 / splat 当 mesh 可编辑 / IIIF 当图床）

**「智识谱系」线索**:
- 标准演变暗示范式更替: **WebGL→WebGPU**(GPGPU/compute 进 web)、**NeRF→3DGS**(神经隐式→显式高斯实时)、**mesh→glTF 高斯泼溅扩展**(2025 两派收敛)、**glTF 2.0→ISO 2022**(从事实标准到国际标准)
- 多 framework 竞争 = 流派之争硬件层: 薄库(Three.js+R3F) vs 整装引擎(Babylon/PlayCanvas); 命令式 vs 声明式; 自研 vs SaaS vs no-code —— 见 7 轴矩阵

**「时效性」信号**（喂诚实边界）:
- 近 12 月有变动: WebGPU 各浏览器达基线(2025 末)+ 仍 CRD; Khronos glTF 高斯泼溅扩展(2025); WebGPURenderer 官方仍标 experimental → 这些条目 Decay=medium-high, master skill 需 12-24 月复查
- 预计 12 月内会变: 3DGS 工具链(high)、WebGPU 最佳实践/API(medium)、TSL 生态适配(medium)

**「工作流变化触发」种子**（喂 Track 03）:
- WebGPU 达基线 + experimental 摘帽 → 渲染后端默认从 WebGL2 切 WebGPU 的工作流拐点
- Khronos glTF 高斯泼溅扩展落地 → "扫描即展厅"进 glTF 标准管线, 改变资产管线工作流
- 文博国标(DB11/T 1922、行标)= 文博项目采集/验收工作流的合规触发源

**冷僻 / 信号薄弱**:
- 总术语数 33（≥25 ✅）; Tier 1 = 22（≥15 ✅）; 有 outsider-tell 的 Tier 1 = 22/22（100% ✅）→ **glossary 维度信号厚, 非冷僻**
- 薄弱点诚实标注: ① 国内 SaaS（众趣/酷雷曼/720云/比目鱼/会鸽）一手术语定义被黑名单（知乎/公众号/CSDN）垄断, 仅 vendor docs surrogate（见 T02 manifest）; ② Certification 维度 N/A（技术工程行业常态, 非缺漏）; ③ 部分新兴术语(3DGS/TSL/WebGPU)定义仍演进, Decay high/medium
- 矛盾全部保留（7 轴 + 4 对照表）, 供 Phase 1.5 用户裁决, 未强行统一
