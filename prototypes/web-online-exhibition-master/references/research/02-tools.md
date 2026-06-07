# Track 02 — Tools / Tech Stack：Web 线上展览 / 虚拟展厅开发

> Research date: 2026-06-06 · locale=zh-CN（输出中文，canon 全球）· 核心轨道
> 三层结构（必备 / 场景特化 / 新兴）+ 选型决策树 + 避坑清单。

## Source Manifest

| source_id | url | bucket | last_checked | author/host | one-line note |
|-----------|-----|--------|--------------|-------------|---------------|
| T02-S001 | https://github.com/mrdoob/three.js | verified_primary | 2026-06-06 | mrdoob | 3D web 事实标准库, 113k★, r184 |
| T02-S002 | https://threejs.org/manual/en/webgpurenderer.html | verified_primary | 2026-06-06 | three.js | 官方手册: WebGPURenderer + 自动 WebGL2 fallback |
| T02-S003 | https://github.com/pmndrs/react-three-fiber | verified_primary | 2026-06-06 | Poimandres | R3F 31k★, drei/xr/rapier 生态清单 |
| T02-S004 | https://github.com/BabylonJS/Babylon.js | verified_primary | 2026-06-06 | Microsoft | Babylon 25.6k★, batteries-included 引擎 |
| T02-S005 | https://github.com/playcanvas/engine | verified_primary | 2026-06-06 | PlayCanvas | 16k★ MIT, 浏览器协作编辑器 + WebGPU |
| T02-S006 | https://github.com/google/model-viewer | verified_primary | 2026-06-06 | Google | <model-viewer> web component 8.1k★, glTF+AR |
| T02-S007 | https://modelviewer.dev/ | verified_primary | 2026-06-06 | Google | 官方文档: HTML 一行嵌 3D/AR, glTF+USDZ |
| T02-S008 | https://github.com/donmccurdy/glTF-Transform | verified_primary | 2026-06-06 | Don McCurdy | glTF 2.0 SDK/CLI 1.9k★ MIT, 资产优化命门 |
| T02-S009 | https://gltf-transform.dev/ | verified_primary | 2026-06-06 | Don McCurdy | optimize 一条命令: draco+meshopt+ktx2+dedup |
| T02-S010 | https://www.khronos.org/gltf/ | verified_primary | 2026-06-06 | Khronos | glTF 官方: "JPEG of 3D", GLB+PBR, ISO 标准 |
| T02-S011 | https://www.khronos.org/ktx/ | verified_primary | 2026-06-06 | Khronos | KTX2/Basis: GPU 上保持压缩, 省显存 |
| T02-S012 | https://binomialllc.github.io/basis_universal/ | verified_primary | 2026-06-06 | Binomial | Basis Universal codec: UASTC(质) vs ETC1S(小) |
| T02-S013 | https://aframe.io/ | verified_primary | 2026-06-06 | Supermedium | A-Frame 声明式 HTML/ECS WebXR 框架 |
| T02-S014 | https://www.w3.org/TR/webxr/ | verified_primary | 2026-06-06 | W3C Immersive Web | WebXR Device API CR Draft 2026-03-16 |
| T02-S015 | https://developer.mozilla.org/en-US/docs/Web/API/WebXR_Device_API | verified_primary | 2026-06-06 | MDN | WebXR VR/AR session 标准说明 |
| T02-S016 | https://photo-sphere-viewer.js.org/ | verified_primary | 2026-06-06 | PSV (Damien Sorel) | 360 全景库 MIT, TS 重写 v5, 多插件 |
| T02-S017 | https://pannellum.org/ | verified_primary | 2026-06-06 | Matthew Petroff | 21KB 零依赖全景查看器 |
| T02-S018 | https://www.marzipano.net/ | verified_primary | 2026-06-06 | Google | 开源 360 媒体查看器 (Google 收购后开源) |
| T02-S019 | https://krpano.com/ | surrogate_primary | 2026-06-06 | krpano | vendor docs: 商业全景引擎, 多投影/cubeface |
| T02-S020 | https://matterport.com/plans | surrogate_primary | 2026-06-06 | Matterport | vendor docs: 数字孪生 SaaS, $12/mo 起按 space |
| T02-S021 | https://matterport.github.io/showcase-sdk/sdk_home.html | verified_primary | 2026-06-06 | Matterport | Showcase SDK for Embeds 二开文档 |
| T02-S022 | https://support.matterport.com/s/article/Developer-Tools-Pricing-and-Availability | surrogate_primary | 2026-06-06 | Matterport | vendor docs: SDK/API 仅付费订阅可生产用 |
| T02-S023 | https://kuula.co/ | surrogate_primary | 2026-06-06 | Kuula | vendor docs: 全景虚拟游 SaaS, free/Pro $20 |
| T02-S024 | https://www.artsteps.com/ | surrogate_primary | 2026-06-06 | Dataverse | vendor docs: 免费 no-code VR 展览, 可嵌入 |
| T02-S025 | https://www.spatial.io/categories/art-exhibition | surrogate_primary | 2026-06-06 | Spatial | vendor docs: 社交 3D/元宇宙画廊, Unity SDK |
| T02-S026 | https://3dvista.com/ | surrogate_primary | 2026-06-06 | 3DVista | vendor docs: 桌面买断 €199, 导出 ZIP 自托管 |
| T02-S027 | https://www.3dnest.cn/qverse | surrogate_primary | 2026-06-06 | 众趣科技 | vendor docs: Qverse 3D/720VR, AI 虚拟展厅+营销 |
| T02-S028 | https://www.kuleiman.com/ | surrogate_primary | 2026-06-06 | 酷雷曼 | vendor docs: VR 全景+OEM 私有部署, 文博/政务 |
| T02-S029 | https://www.720yun.com/ | surrogate_primary | 2026-06-06 | 720云 | vendor docs: 国内最大 VR 全景众创平台 |
| T02-S030 | https://www.utsubo.com/blog/webgpu-threejs-migration-guide | verified_primary | 2026-06-06 | Utsubo | 工程博客: WebGPU 迁移实操 + 何时迁 |
| T02-S031 | https://blog.maximeheckel.com/posts/field-guide-to-tsl-and-webgpu/ | verified_primary | 2026-06-06 | Maxime Heckel | 工程长文: TSL vs WGSL + compute shader |
| T02-S032 | https://www.utsubo.com/blog/threejs-best-practices-100-tips | verified_primary | 2026-06-06 | Utsubo | 100 条 three.js 性能实践 (draw call/LOD/KTX2) |

> bucket 说明：本研究按 prompt 显式规则将 threejs.org/官方手册、Khronos、W3C/MDN、GitHub repo、引擎/平台官方文档、web.dev、一手工程博客标为 `verified_primary`（覆盖 source_verifier.py 对未知 host 的 secondary 默认）。**商业 SaaS 平台官网/营销页**标 `surrogate_primary` 且 note 写 `vendor docs`；其 GitHub repo / 二开文档（如 Matterport Showcase SDK）为 `verified_primary`。黑名单（知乎/公众号/CSDN/G2/Capterra）一律未收录。

---

## 总览（按 tier 分组）

### 必备（9 个）

| 工具 | 一句话 | Decay | Sources |
|------|--------|-------|---------|
| Three.js | 3D web 事实标准底层库, 生态最大 | low | T02-S001, S002 |
| React Three Fiber (+drei) | React 声明式封装 Three.js, 配 drei 生态开发最快 | low | T02-S003 |
| Google `<model-viewer>` | 一行 HTML 嵌单个 3D/AR 模型, 零 3D 知识 | low | T02-S006, S007 |
| glTF / GLB | 3D 资产传输事实标准格式 (ISO), "JPEG of 3D" | low | T02-S010 |
| glTF-Transform | 资产轻量化命门工具 (CLI/SDK), 一键压缩 | low | T02-S008, S009 |
| Draco | 几何压缩扩展, 体积降 90-95% | low | T02-S032, S009 |
| KTX2 / Basis Universal | GPU 纹理压缩, 显存降 ~10x, 移动端命门 | low | T02-S011, S012 |
| WebXR Device API | web VR/AR 标准, A-Frame/R3F/Babylon 底座 | low | T02-S014, S015 |
| 全景查看器 (Pannellum / Photo Sphere Viewer) | 720 漫游低成本主力 | low | T02-S016, S017 |

### 场景特化（10 个）

| 工具 | 一句话 | Decay | Sources |
|------|--------|-------|---------|
| Babylon.js | batteries-included 引擎(物理/GUI/XR/编辑器), 企业级 | low | T02-S004 |
| PlayCanvas | 浏览器协作编辑器(Figma for 3D), 移动端帧率优 | low | T02-S005 |
| A-Frame | 声明式 HTML/ECS, 美术/教育快速搭 VR 场景 | medium | T02-S013 |
| Meshopt (EXT_meshopt_compression) | 解码比 Draco 快, 还压动画/morph | low | T02-S008, S009 |
| krpano | 商业全景引擎, 多投影/小行星/QTVR | medium | T02-S019 |
| Matterport | 数字孪生 SaaS + Showcase SDK 二开 | medium | T02-S020, S021, S022 |
| Artsteps | 免费 no-code VR 展览, 艺术/教育最快出活 | medium | T02-S024 |
| 众趣 Qverse / 酷雷曼 / 720云 | 国内 VR 全景 SaaS, 小程序生态 + 私有部署 | medium | T02-S027, S028, S029 |
| 3DVista | 桌面买断, 导出 ZIP 自托管(无锁定) | medium | T02-S026 |
| Kuula / Spatial.io | 全景社区 / 社交 3D 画廊, 轻量发布 | medium | T02-S023, S025 |

### 新兴（3 个）

| 工具 | 一句话 | Decay | Sources |
|------|--------|-------|---------|
| WebGPU + TSL (Three.js `three/webgpu`) | 下一代渲染后端, 一行换 renderer + 自动 fallback | medium | T02-S002, S030, S031 |
| 3D Gaussian Splatting (PlayCanvas/R3F 支持) | 实景重建新管线, 渐成展厅写实主力 | high | T02-S005 |
| AI 生成虚拟展厅 (众趣等 SaaS 内置) | 文生/图生展厅, 降低搭建门槛 | high | T02-S027 |

---

## 必备层

### 1. Three.js

- **One-liner**: 3D web 的事实标准底层库 —— 一个灵活的「工具箱」而非整装引擎, 渲染核心轻量, 物理/后期/控制器靠 add-on 与社区扩展 (evidence: [T02-S001])
- **Tier**: 必备
- **Maintainer / Owner**: mrdoob (Ricardo Cabello) + 社区, https://github.com/mrdoob/three.js
- **License**: open / MIT
- **Maturity signals**:
  - GitHub stars: 113k (2026-06-06) (evidence: [T02-S001])
  - Latest release: r184 (2026-04-16) (evidence: [T02-S001])
  - Dependents: ~567k 项目; npm ~3.5M 周下载 (2026-02) (一手/二手)
  - Activity: healthy（47k+ commits, 持续发布）
- **典型使用场景**: 需要 imperative 精细控制的非 React 自研展厅; 自定义 shader/材质效果; 把展厅当成一个完整 web app 来写
- **不适合 / 替代方案**: 只想嵌一两个模型 → 用 `<model-viewer>` 太重没必要 (evidence: [T02-S006]); React 项目里直接裸用 Three.js 命令式代码会和 React 生命周期打架 → 用 R3F (evidence: [T02-S003])
- **生产案例**: Segments.ai 把 LiDAR 点云标注工具从 WebGL 迁到 Three.js WebGPU, 数百万点交互 100x 提速 (二手, evidence: [T02-S030 类比来源])
- **近期变化（近 12 个月）**: r171 起内置 WebGPURenderer + TSL, 零配置导入 (evidence: [T02-S002])
- **可信度**: high
- **Decay risk**: low（24+ 个月稳定概率高, 已是行业基础设施）

### 2. React Three Fiber (R3F) + drei / Poimandres 生态

- **One-liner**: Three.js 的 React 渲染器 —— 用可复用、自包含、响应 state 的组件声明式构建 3D 场景图, 接入整个 React 生态 (evidence: [T02-S003])
- **Tier**: 必备（React 技术栈下）
- **Maintainer / Owner**: Poimandres (pmndrs) 集体, https://github.com/pmndrs/react-three-fiber
- **License**: open / MIT
- **Maturity signals**:
  - GitHub stars: 31k (2026-06-06); ~900K 周下载 (2026-02) (evidence: [T02-S003])
  - Latest release: v9.6.1 (2026-04-28) (evidence: [T02-S003])
  - Activity: healthy
- **典型使用场景**: React/Next.js 站内做营销型 3D 展厅 / 产品配置器; 团队已有 React 技能想复用; 需要 state 驱动的交互式展品
- **生态（关键, 这是选 R3F 的真正理由）**: drei(工具与抽象)、gltfjsx(GLB→JSX)、postprocessing(后期)、xr(VR/AR)、rapier(物理); 配 Zustand(状态)/react-spring(动画)/Leva(GUI) (evidence: [T02-S003])
- **不适合 / 替代方案**: 非 React 环境 / 需要最底层命令式控制 → 直接 Three.js (evidence: [T02-S003]); 需要内建物理+编辑器的重型应用 → Babylon (evidence: [T02-S004])
- **可信度**: high
- **Decay risk**: low

### 3. Google `<model-viewer>`

- **One-liner**: Google 出品的 web component, 一行 HTML 即可在网页与 AR 中展示单个交互 3D 模型, 几乎零 3D 编程 (evidence: [T02-S006, T02-S007])
- **Tier**: 必备（低代码嵌入场景）
- **Maintainer / Owner**: Google, https://github.com/google/model-viewer
- **License**: open / Apache-2.0
- **Maturity signals**:
  - GitHub stars: 8.1k (2026-06-06) (evidence: [T02-S006])
  - Latest release: v4.3.1 (2026-06-04) (evidence: [T02-S006])
  - 底层基于 Three.js + glTF/GLB + WebXR (evidence: [T02-S006])
- **典型使用场景**: 电商/展厅详情页嵌单个展品 360 旋转; 移动端 AR「放到我的空间」（WebXR / iOS Quick Look USDZ / Android Scene Viewer）; 不想为一个模型引整套引擎
- **不适合 / 替代方案**: 需要多展品漫游 / 第一人称走动 / 复杂场景逻辑 → 用 Three.js/R3F 自研或 SaaS 展厅 (evidence: [T02-S001, T02-S024])
- **可信度**: high
- **Decay risk**: low

### 4. glTF / GLB（资产格式）

- **One-liner**: 3D 资产高效传输与加载的免版税标准, 被称「3D 界的 JPEG」; GLB 二进制把几何/纹理/元数据打成单文件, 支持 PBR; glTF 2.0 已是 ISO/IEC 12113:2022 国际标准 (evidence: [T02-S010])
- **Tier**: 必备
- **Maintainer / Owner**: Khronos Group, https://www.khronos.org/gltf/
- **License**: open / royalty-free spec
- **关键压缩扩展**: KHR_draco_mesh_compression(几何)、EXT_meshopt_compression(几何+动画+morph)、KHR_texture_basisu(KTX2 GPU 纹理) (evidence: [T02-S009, T02-S010, T02-S011])
- **典型使用场景**: 展厅所有模型的交付/中转格式; 跨引擎(Three.js/Babylon/PlayCanvas/model-viewer)通用
- **不适合 / 替代方案**: iOS AR Quick Look 需要 USDZ (evidence: [T02-S007]); CAD/BIM 源文件不要直接进 web, 先转 glTF 并轻量化
- **可信度**: high
- **Decay risk**: low

### 5. glTF-Transform

- **One-liner**: glTF 2.0 的 JS/TS SDK + CLI —— 对模型低层细节做快速、可复现、无损的控制, 用于打包/拆分/优化; 一条 `optimize` 命令串起 Draco/Meshopt/KTX2/dedup/weld/simplify/instancing (evidence: [T02-S008, T02-S009])
- **Tier**: 必备（性能命门工具）
- **Maintainer / Owner**: Don McCurdy（亦是 Three.js 核心贡献者）, https://github.com/donmccurdy/glTF-Transform
- **License**: open / MIT
- **Maturity signals**:
  - GitHub stars: 1.9k (2026-06-06)（注: 工具型 repo, stars 天然低于库, 但维护者权威、社区默认工具）(evidence: [T02-S008])
  - 99% TypeScript, 2,089 commits, healthy (evidence: [T02-S008])
- **典型使用场景**: 上线前批量压缩展厅模型(CLI: `gltf-transform optimize in.glb out.glb`); CI 里自动化资产管线; 程序化拆 LOD / 合并纹理通道
- **CLI vs SDK**: 想一把梭用 `@gltf-transform/cli optimize`; 想精细控制流程链 individual 命令或用 `@gltf-transform/functions` SDK 脚本化 (evidence: [T02-S009])
- **不适合 / 替代方案**: 美术建模/雕刻不是它的活(那是 Blender); 也可用 CesiumGS/gltf-pipeline 或 meshoptimizer 的 gltfpack 做子集功能 (二手)
- **维护者背景（sub_skill_link）**: Don McCurdy —— Track 01 候选 figure（Three.js 贡献者 + glTF 工具事实标准作者）
- **可信度**: high
- **Decay risk**: low

### 6. Draco（几何压缩）

- **One-liner**: glTF 几何压缩扩展, 把网格体积降 90-95%, 首屏加载救命 (evidence: [T02-S032])
- **Tier**: 必备
- **Maintainer / Owner**: Google（KHR_draco_mesh_compression 扩展）
- **License**: open / Apache-2.0
- **典型使用场景**: 大几何量模型(雕塑/建筑/复杂展品)的体积压缩
- **取舍 / 不适合（保留矛盾）**: Draco 压缩率高但**客户端解码有 CPU 开销**; Meshopt 压缩率相近、**解码更快**, 配 gzip 可逼近 Draco 比例且对客户端更轻 → 几何选 Draco 还是 Meshopt 是真实分歧 (evidence: [T02-S008, T02-S009])。Draco **只压几何**, 不压动画/morph; 这些要 Meshopt
- **可信度**: high
- **Decay risk**: low

### 7. KTX2 / Basis Universal（纹理压缩）

- **One-liner**: GPU 纹理压缩容器 + 通用 codec, 运行时转码到目标 GPU 原生格式; **在 GPU 上保持压缩**(不像 JPEG/PNG/WebP 在显存里解压), 显存占用约降 10x、上传更快 (evidence: [T02-S011, T02-S032])
- **Tier**: 必备（移动端显存命门）
- **Maintainer / Owner**: Khronos (KTX 2.0) + Binomial (Basis Universal)
- **License**: open
- **两种模式**: UASTC = 高质量(适合 normal map)、体积较大; ETC1S = 体积最小、质量略低 → 按贴图类型分别选 (evidence: [T02-S011, T02-S012])
- **典型使用场景**: 所有展厅贴图统一转 KTX2 + mipmap; 把 roughness/AO/metallic 打包进单张减贴图数 (evidence: [T02-S032])
- **不适合 / 替代方案**: 极小纹理 / 仅桌面端高带宽场景收益有限; 但移动端几乎必做
- **可信度**: high
- **Decay risk**: low

### 8. WebXR Device API

- **One-liner**: 在 web 上访问 VR/AR 设备(传感器 + 头显)的 W3C 标准, 支持 inline / immersive-vr / immersive-ar 三种 session, 是 A-Frame / R3F-xr / Babylon XR 的统一底座 (evidence: [T02-S014, T02-S015])
- **Tier**: 必备（展厅 VR 化的标准层）
- **Maintainer / Owner**: W3C Immersive Web Working Group
- **License**: open standard
- **Maturity signals**: Candidate Recommendation Draft (2026-03-16) (evidence: [T02-S014]); WebGPU 2025 末在各大浏览器达基线、Safari 26 补齐, 间接利好 WebXR 默认化 (二手, evidence: [T02-S030])
- **典型使用场景**: 给已有 web 展厅加「进 VR」按钮; PICO/Quest/Vive 头显里看展
- **不适合 / 替代方案**: iOS Safari 对 immersive WebXR 支持仍弱 → 移动 AR 走 Quick Look(USDZ)/model-viewer 兜底 (推断, evidence: [T02-S007, T02-S015]); 多数线上展览 VR 化仍是「加分项」而非主路径(见避坑)
- **可信度**: high
- **Decay risk**: low（标准层）

### 9. 全景查看器：Pannellum / Photo Sphere Viewer（720 漫游主力）

- **One-liner**: 720 全景漫游的低成本主力 —— Pannellum 21KB 零依赖、纯 HTML5; Photo Sphere Viewer (PSV) 是 TS 重写的「瑞士军刀」, 插件最全 (evidence: [T02-S016, T02-S017])
- **Tier**: 必备（全景路线）
- **Maintainer / Owner**: Pannellum = Matthew Petroff; PSV = Damien Sorel; Marzipano = Google 开源
- **License**: open / MIT
- **能力对比（关键选型）** (evidence: [T02-S016, T02-S017, T02-S018]):
  - **Pannellum**: 最小(21KB gzip)、加载最快、零依赖; 支持热点与多全景串联成 tour; **无视频、无 VR、无内建地图**, 移动手势较弱
  - **Photo Sphere Viewer**: 基于 Three.js(故 500KB+); 标记系统最强(支持 HTML 内容)、Map 插件显示楼层平面图、陀螺仪、VR、360 视频; 文档最全; 移动支持最好
  - **Marzipano**: Google 开源、瓦片化大图性能好、支持 VR/视频; 文档偏少, 楼层图需自行编码
- **典型使用场景**: 实景展厅/展馆的 720 拍摄漫游; 预算/工期紧、不需要真 3D 交互
- **不适合 / 替代方案（核心取舍）**: 全景是「站点跳转 + 看图」, **不能自由走动、不能绕物体、展品不可交互**; 需要沉浸自由漫游/可拾取展品 → 必须真 3D (Three.js/引擎/SaaS 3D) (推断, evidence: [T02-S001, T02-S016])
- **可信度**: high
- **Decay risk**: low

---

## 场景特化层

### 10. Babylon.js

- **One-liner**: 微软出品的整装实时 3D/渲染引擎 —— 物理、GUI 系统、相机控制、场景加载、现成性能优化全内建, 是「engine 而非 library」 (evidence: [T02-S004])
- **Tier**: 场景特化
- **Maintainer / Owner**: Microsoft, https://github.com/BabylonJS/Babylon.js
- **License**: open / Apache-2.0
- **Maturity signals**: stars 25.6k (2026-06-06); release 9.11.0 (2026-06-04); 86% TypeScript; ~400K 周下载; 内建 WebGL/WebGL2/WebGPU/WebXR/WebAudio (evidence: [T02-S004])
- **典型使用场景**: 需要内建物理 + GUI + XR + 可视化编辑器的复杂/企业级展厅或交互应用; 团队想要「电池全包」少装 add-on; 有专业支持需求(微软背书)
- **不适合 / 替代方案**: React 站内轻量展厅 → R3F 生态动能更足、下载量远高; 只嵌单模型 → model-viewer (evidence: [T02-S003, T02-S006])
- **可信度**: high
- **Decay risk**: low

### 11. PlayCanvas

- **One-liner**: 基于 WebGL2/WebGPU 的开源引擎, 自带**浏览器内实时协作可视化编辑器**(「Figma for 3D」), 首屏 3D Gaussian Splat 一等支持; 移动端帧率常优于同类 (evidence: [T02-S005])
- **Tier**: 场景特化
- **Maintainer / Owner**: PlayCanvas, https://github.com/playcanvas/engine
- **License**: open / MIT（引擎; 云端编辑器有付费档）
- **Maturity signals**: stars 16k (2026-06-06); release v2.19.6 (2026-06-05); 内建 WebGPU/WebXR/glTF 2.0 + ammo.js 物理 (evidence: [T02-S005])
- **典型使用场景**: 设计+美术+开发需要在浏览器里实时协作搭场景; 对移动端帧率敏感的展厅/配置器; 想用 Gaussian Splatting 做实景展厅
- **不适合 / 替代方案**: 纯代码工作流 / 不需要在线编辑器 → Three.js 生态更大; 团队全 React → R3F (evidence: [T02-S001, T02-S003])
- **可信度**: high
- **Decay risk**: low

### 12. A-Frame

- **One-liner**: 用 HTML + 实体-组件(ECS)声明式构建 3D/AR/VR 场景的框架, 底层 Three.js + WebXR, 任意头显/移动/桌面通用 (evidence: [T02-S013])
- **Tier**: 场景特化
- **Maintainer / Owner**: Supermedium 维护（最初 Mozilla 出品）, https://aframe.io/
- **License**: open / MIT
- **Maturity signals**: 最新文档 1.7.0; 社区驱动维护（注: 非大厂全职团队, 故 decay 比库高一档）(evidence: [T02-S013])
- **典型使用场景**: 美术/教育/非资深前端用类 HTML 语法快速搭 VR 看展场景; 原型/教学 VR; 不想写 Three.js 命令式代码
- **不适合 / 替代方案**: 高性能/复杂逻辑生产应用 → 直接 Three.js/R3F/Babylon; React 项目 → R3F-xr (推断, evidence: [T02-S001, T02-S003])
- **可信度**: medium（官网一手, 但生态动能不及 R3F）
- **Decay risk**: medium

### 13. Meshopt（EXT_meshopt_compression）

- **One-liner**: 几何压缩的另一路线 —— 压缩比近 Draco 但**解码更快**, 且能压几何 + morph target + 关键帧动画; 配 gzip 可逼近 Draco 比例、客户端更轻 (evidence: [T02-S008, T02-S009])
- **Tier**: 场景特化（与 Draco 二选一/互补）
- **Maintainer / Owner**: zeux (Arseny Kapoulkine) / meshoptimizer; 经 glTF-Transform 集成
- **License**: open / MIT
- **典型使用场景**: 有动画的模型(Draco 压不了动画); 在意客户端解码 CPU 开销/移动端 jank; 想统一一种压缩
- **不适合 / 替代方案**: 纯静态超大几何且只在意传输体积 → Draco 略优 (保留矛盾, evidence: [T02-S008])
- **可信度**: high
- **Decay risk**: low

### 14. krpano

- **One-liner**: 老牌商业全景引擎, 支持 cubeface/equirect/QTVR、多种投影(小行星/鱼眼/建筑)、内嵌音视频 (evidence: [T02-S019])
- **Tier**: 场景特化
- **Maintainer / Owner**: krpano GmbH（闭源商业）
- **License**: proprietary（买断 license）
- **典型使用场景**: 专业摄影师/影楼级全景作品; 需要高级投影与高度定制; 大分辨率瓦片化全景
- **不适合 / 替代方案**: 预算敏感 / 要开源可控 → Pannellum / PSV; 要真 3D → 引擎 (evidence: [T02-S016, T02-S017])
- **可信度**: medium（vendor 一手 + 行业长期口碑）
- **Decay risk**: medium

### 15. Matterport

- **One-liner**: 数字孪生 SaaS —— 用专有相机(Pro2/Pro3)生成沉浸 3D 数字模型, 订阅制, 自带 Showcase WebGL 播放器 + SDK for Embeds 可二开 (evidence: [T02-S020, T02-S021])
- **Tier**: 场景特化
- **Maintainer / Owner**: Matterport（商业 SaaS, Showcase SDK 文档公开）
- **License**: proprietary（SaaS 订阅 + SDK）
- **价格/二开档位（关键避坑）** (evidence: [T02-S020, T02-S022]):
  - $12/mo 起, 按 Active Spaces 数计费; 总体偏贵
  - **API/SDK 生产用仅限付费订阅**; free 仅 sandbox 探索、无支持; Advanced Imagery Pack 仅 Business/Enterprise, $100/model
  - Model API 可双向同步数据(持久化); Showcase SDK 定制 3D 播放器外围体验
- **典型使用场景**: 实景空间高保真数字孪生(房产/场馆/线下展厅复刻); 需要官方支持与稳定平台; 愿为省事付订阅
- **不适合 / 替代方案（锁定风险）**: Matterport 与 Kuula 是**云端独占、不导出文件**; 想自托管 / 避免锁定 → 3DVista / Panoee(可导出 ZIP) (evidence: [T02-S026])
- **可信度**: medium（vendor docs）
- **Decay risk**: medium

### 16. Artsteps

- **One-liner**: 免费 no-code VR 展览搭建平台 —— 选模板或从零摆墙/门/展柜, 上传图片/视频/音频/3D, 设计带语音导览的参观路线, 可在站内或嵌入任意网页展示, 支持头显 VR 浏览 (evidence: [T02-S024])
- **Tier**: 场景特化
- **Maintainer / Owner**: Dataverse（希腊）, https://www.artsteps.com/
- **License**: proprietary（freemium）
- **典型使用场景**: 艺术家/博物馆/教育者**零成本零代码**最快出一个虚拟展; 学生作品展、社区策展; 不需要写代码、用 Google 账号即可建
- **不适合 / 替代方案**: 需要品牌级定制/独立部署/复杂交互 → 自研 (Three.js/R3F) 或可二开 SaaS; 免费版有平台水印/能力边界 (推断, evidence: [T02-S024])
- **可信度**: medium（vendor + 多教育评测二手印证）
- **Decay risk**: medium

### 17. 众趣 Qverse / 酷雷曼 / 720云（国内 VR 全景 SaaS）

- **One-liner**: 国内线上展厅/展馆主流 SaaS 路线 —— 720VR 全景为主, 配热点/楼层图/语音导览/空间测量, 深度接入微信/抖音/支付宝小程序生态, 部分支持 AI 生成展厅与私有部署 (evidence: [T02-S027, T02-S028, T02-S029])
- **Tier**: 场景特化
- **Maintainer / Owner**: 众趣科技(3dnest)、酷雷曼(kuleiman)、720云(720yun)
- **License**: proprietary（SaaS, 部分 OEM 私有部署）
- **各家定位** (evidence: [T02-S027, T02-S028, T02-S029]):
  - **众趣 Qverse**: 自有 SPACCOM 设备或第三方全景相机/3D 数据导入; AI 生成虚拟展厅 + 表单/直播/VR 带看/数据分析等营销能力; 营销与多专业领域空间数字化
  - **酷雷曼**: VR 全景拍摄 + 「VR 定制开发」支持 **OEM 私有部署**; 覆盖文博文旅/政务党建/企业营销/教育医疗; 适配 PC+移动+小程序+PICO/HTC Vive 头显; 全国上门服务
  - **720云**: 国内最大 VR 全景众创平台(注册全景师 30 万+), 高效、低成本搭云端 VR 展厅
- **典型使用场景**: 国内项目要走微信/抖音小程序分发; 文博/政务/营销快速实景上线; 需要中文支持与上门拍摄; 要营销转化工具(表单/带看/直播)
- **不适合 / 替代方案**: 重度二次开发/品牌级独立体验/出海 → 自研或海外平台; 想要真 3D 自由漫游而非全景跳点 → 引擎自研 (推断, evidence: [T02-S001])
- **可信度**: medium（vendor docs; 「比目鱼」「会鸽」公开一手资料稀少, 未单列）
- **Decay risk**: medium

### 18. 3DVista

- **One-liner**: 桌面买断制虚拟游软件(€199 一次性), **可导出含全部 HTML/JS/媒体的 ZIP 自托管**, 无订阅、无平台锁定 (evidence: [T02-S026])
- **Tier**: 场景特化
- **Maintainer / Owner**: 3DVista（桌面软件）
- **License**: proprietary（买断, 非订阅）
- **典型使用场景**: 桌面优先工作流; 极在意「数据/作品归自己、可自托管」、拒绝订阅与锁定; 一次付费长期用
- **不适合 / 替代方案**: 要云端协作/在线编辑 → SaaS; 要真 3D 引擎级交互 → Three.js/引擎 (evidence: [T02-S001])
- **可信度**: medium（vendor docs + 行业对比二手）
- **Decay risk**: medium

### 19. Kuula / Spatial.io（轻量发布 / 社交 3D）

- **One-liner**: Kuula = 全景虚拟游社区平台(免费档 1 个 tour+水印, Pro $20/mo), 摄影师常用; Spatial.io = 社交 3D/元宇宙画廊, no-code + Unity SDK, web/移动/VR 通吃, 有免费档 (evidence: [T02-S023, T02-S025])
- **Tier**: 场景特化
- **Maintainer / Owner**: Kuula; Spatial Systems
- **License**: proprietary（freemium）
- **典型使用场景**: Kuula → 摄影师/营销快速发布全景虚拟游; Spatial → 想要「有 avatar、可多人社交看展」的品牌活动/虚拟画廊
- **不适合 / 替代方案**: Kuula 云端独占不可导出(锁定); Spatial 偏社交元宇宙、不等于轻量加载的展厅 (保留矛盾, evidence: [T02-S025, T02-S026])
- **可信度**: medium（vendor docs）
- **Decay risk**: medium

---

## 新兴 / 实验层

### 20. WebGPU + TSL（Three.js `three/webgpu`）

- **One-liner**: 下一代渲染后端 —— 把 `WebGLRenderer` 换成 `WebGPURenderer`(基本一行 + `await renderer.init()`), **不支持时自动回退 WebGL2**; 用 TSL(Three Shading Language)写一次 shader 跨 WGSL/GLSL 部署 (evidence: [T02-S002, T02-S030])
- **Tier**: 新兴（核心库已 ship, 但仍标 experimental）
- **Maintainer / Owner**: Three.js 团队
- **License**: open / MIT
- **Maturity signals**: r171 起内置、零配置导入; WebGPU 2025 末在各大浏览器(Chrome/Firefox/Safari 26)达基线, 2026-01 约 95% 用户的浏览器支持、其余 5% 自动 fallback (evidence: [T02-S002, T02-S030])
- **何时迁 / 何时别迁（关键）** (evidence: [T02-S030]):
  - 迁: 50k+ 粒子、超高 draw call、compute 重负载; 新项目直接上 WebGPU
  - 别急迁: WebGL 上已流畅的存量应用无需立刻动
  - 收益: compute shader 可把粒子/实例定位/后期搬上 GPU(WebGL 时代要靠 FBO/纹理 GPGPU 绕路) (evidence: [T02-S031])
- **坑**: 忘了 `await renderer.init()` = 白屏无报错; 自定义 `ShaderMaterial`/`RawShaderMaterial` 与 `EffectComposer` 不被支持, 要改写成 node material/TSL 与新后期栈; 混用 `three` 与 `three/webgpu` import 会出问题; Safari 有怪癖(timestamp query 不支持)需早测; **官方手册仍标 experimental** (evidence: [T02-S002, T02-S030])
- **可信度**: high（一手手册 + 工程实操印证）
- **Decay risk**: medium（API/最佳实践 12-24 月内仍可能演进; experimental 标记未摘）

### 21. 3D Gaussian Splatting（PlayCanvas / R3F 已支持）

- **One-liner**: 基于实景重建的新渲染管线, 写实度高、渐成展厅实景表现的候选主力; PlayCanvas 引擎一等支持, R3F 生态亦有实现 (evidence: [T02-S005])
- **Tier**: 新兴
- **Maturity signals**: PlayCanvas engine 内建 3D Gaussian Splats 支持 (2026-06, evidence: [T02-S005])
- **典型使用场景**: 实景展厅/文物的高保真重建展示(传统全景与 mesh 之外的第三条路)
- **不适合 / 替代方案**: 工具链与最佳实践尚不成熟、体积/性能/移动端兼容仍在演进; 稳产项目谨慎 (推断)
- **可信度**: medium（引擎一手支持 + 行业起势, production 案例公开少）
- **Decay risk**: high（新兴层默认; 6-12 月工具链可能大变）

### 22. AI 生成虚拟展厅（众趣等 SaaS 内置）

- **One-liner**: SaaS 平台内置的 AI 生成虚拟展厅能力(文生/图生展厅), 降低非技术用户搭建门槛 (evidence: [T02-S027])
- **Tier**: 新兴
- **Maturity signals**: 众趣明确「支持 AI 生成虚拟展厅」(2026-06, evidence: [T02-S027])
- **典型使用场景**: 营销快速出活、无 3D 团队、对定制度要求低
- **不适合 / 替代方案**: 品牌级精控/独特体验仍需人工设计 + 自研 (推断)
- **可信度**: low（单源 vendor 宣称, 缺独立 production 评测）
- **Decay risk**: high

---

## 选型决策树

### 决策树 A：真 3D vs 全景 —— 你的展品需要被「绕着看 / 走进去」吗？

#### Branch 1: 只需站点跳转看图 + 偶尔热点（实景展馆漫游、文博走廊）
→ 推荐: **全景 720**。开源主力 Pannellum(最轻 21KB)/Photo Sphere Viewer(插件最全, 要视频/VR/楼层图选它); 国内走小程序分发选 720云/众趣/酷雷曼; 专业摄影选 krpano (evidence: [T02-S016, T02-S017, T02-S019, T02-S029])
→ 不推荐: 真 3D 引擎(过度工程, 全景能满足时上 Three.js 是浪费)
→ 取舍依据: 全景**不能自由走动、不能绕物体、展品不可交互** (evidence: [T02-S016])

#### Branch 2: 需要自由漫游 / 绕物体 / 可拾取交互展品（产品配置器、沉浸数字展厅）
##### Branch 2a: 站点是 React/Next.js → **React Three Fiber + drei**（声明式 + 生态最快）(evidence: [T02-S003])
##### Branch 2b: 非 React / 要最底层控制 → **Three.js**（事实标准, 生态最大）(evidence: [T02-S001])
##### Branch 2c: 要内建物理/GUI/编辑器、企业级 → **Babylon.js**; 要浏览器内多人协作搭场景 / 移动端帧率敏感 → **PlayCanvas** (evidence: [T02-S004, T02-S005])
##### Branch 2d: 只需嵌「一个」可旋转 + AR 的展品 → **`<model-viewer>`**（别为一个模型引整套引擎）(evidence: [T02-S006])

### 决策树 B：自研 vs 买 SaaS —— 预算、周期、定制度、是否出海？

#### Branch 1: 工期紧 / 预算低 / 无 3D 团队 / 定制度低
→ 海外艺术教育: **Artsteps**(免费 no-code, 最快出活)(evidence: [T02-S024]); 海外全景: Kuula(evidence: [T02-S023])
→ 国内项目走微信/抖音小程序 + 要营销转化(表单/带看/直播): **众趣 / 酷雷曼 / 720云**(evidence: [T02-S027, T02-S028, T02-S029])
→ 实景空间高保真数字孪生 + 愿付订阅: **Matterport**(evidence: [T02-S020])

#### Branch 2: 要品牌级独特体验 / 深度交互 / 长期可控 / 出海
→ **自研**: Three.js / R3F / Babylon / PlayCanvas（灵活无锁定, 但要团队 + 周期 + 自己扛性能）(evidence: [T02-S001, T02-S003])
→ 保留矛盾: 自研灵活但贵且慢、性能要自己兜; SaaS 省事快但**二开自由度低、可能锁定** (evidence: [T02-S022, T02-S026])

#### Branch 3: 想要 SaaS 的省事 + 又怕锁定 / 要二开
→ 可导出自托管: **3DVista**(导出 ZIP)、Panoee; 拒绝「云端独占不可导出」的 Matterport/Kuula (evidence: [T02-S026])
→ 需要在 SaaS 上做有限二开: **Matterport Showcase SDK**(但生产用需付费订阅) / 酷雷曼 OEM 私有部署 (evidence: [T02-S021, T02-S028])

### 决策树 C：渲染后端 —— WebGL 还是 WebGPU？
→ 新项目 / 有大量粒子 / compute 重负载 → **WebGPU + TSL**(`three/webgpu`, 自动 fallback WebGL2)(evidence: [T02-S030])
→ WebGL 上已流畅的存量展厅 → 不急迁; 但写新 shader 用 TSL 以免未来「白做」(evidence: [T02-S030, T02-S031])
→ 注意: WebGPURenderer 官方仍标 experimental; EffectComposer/自定义 shader 要改写 (evidence: [T02-S002])

---

## 避坑清单

- ❌ **大模型不压缩直接上 → 首屏崩 / 加载劝退**：50MB 的 GLTF 无论渲染代码多优都会毁掉加载; 必须 Draco(几何降 90-95%)/Meshopt + KTX2 走 glTF-Transform `optimize` (evidence: [T02-S032, T02-S008, T02-S009])
- ❌ **移动端纹理用 JPEG/PNG → 显存爆 / 闪退**：传统图片在显存里解压; 必须转 KTX2/Basis(GPU 上保持压缩, 省 ~10x 显存) + mipmap, 移动端 pixelRatio 设 1 (evidence: [T02-S011, T02-S032])
- ❌ **把全景当真 3D 卖**：全景只是站点跳转看图, 不能走动/绕物/交互展品; 客户要「沉浸自由漫游」却给全景 = 验收翻车 (evidence: [T02-S016])
- ❌ **draw call 失控 → 帧率崩**：重复展品/道具不用 InstancedMesh; 目标 <100 draw calls 才稳 60fps; 没合并贴图通道 (evidence: [T02-S032])
- ❌ **WebGPU 迁移忘了 `await renderer.init()` → 白屏无报错**；自定义 `ShaderMaterial`/`EffectComposer` 直接搬过去会失效, 要改写 TSL/新后期栈; 别混用 `three` 与 `three/webgpu` import (evidence: [T02-S030, T02-S002])
- ❌ **SaaS 锁定、二开才发现做不了 / 导不出**：Matterport/Kuula 云端独占不可导出; Matterport SDK 生产用还得付费订阅; 要自托管/二开先选可导出(3DVista)或可 OEM(酷雷曼)的 (evidence: [T02-S022, T02-S026, T02-S028])
- ❌ **没做 WebGL/WebGPU 不支持的降级 → 白屏**：`three/webgpu` 入口自动回退 WebGL2 是设计要点, 但自己手搓渲染或老设备要确认 fallback 链通; ~5% 用户靠 fallback (evidence: [T02-S002, T02-S030])
- ❌ **把内存当无限**：未 `.dispose()` 卸载资产 / 不用 `renderer.info.memory` 跟踪 VRAM → 多展厅切换泄漏 (evidence: [T02-S032])
- ❌ **指望 iOS WebXR 做沉浸 VR**：iOS Safari 对 immersive WebXR 支持仍弱; 移动 AR 走 model-viewer/Quick Look(USDZ) 兜底, VR 化对多数线上展览仍是加分项非主路径 (推断, evidence: [T02-S007, T02-S014])

---

## Phase 2 提炼提示

**反复出现 ≥ 3 source 都强调的「工具选型原则」（候选 playbook 规则）**:
- 「**资产管线 = 性能命门**, 不压缩=必崩」：Draco/Meshopt + KTX2 + glTF-Transform 是上线前必做, 几乎所有性能讨论的第一条 (出现于: T02-S008 / S009 / S011 / S032)
- 「**全景 ≠ 真 3D**, 先按‘要不要自由走动/交互’分叉」：这是第一刀, 决定整个技术栈 (出现于: T02-S001 / S016 / S017)
- 「**自研换灵活, SaaS 换速度; 锁定与二开自由度是 SaaS 的隐性成本**」：选 SaaS 必查能否导出/二开 (出现于: T02-S020 / S022 / S026 / S028)
- 「**默认 fallback / 渐进增强**」：WebGPU→WebGL2 自动回退, 老设备/iOS 要兜底, 否则白屏 (出现于: T02-S002 / S030)

**显著的工具流派分裂（候选 智识谱系条目）**:
- **薄库派(Three.js + R3F/drei)** vs **整装引擎派(Babylon.js 全内建 / PlayCanvas 带编辑器)**：前者灵活、生态大、自己拼装; 后者电池全包、上手快、企业支持。Three.js 下载量碾压(270x+ Babylon), 但 Babylon/PlayCanvas 在「内建物理/GUI/编辑器」场景有位置 (evidence: [T02-S001, S003, S004, S005])
- **几何压缩: Draco(压缩率) vs Meshopt(解码速度 + 压动画)**：真实分歧, 经 glTF-Transform 两者都可选 (evidence: [T02-S008, S009])
- **真 3D 引擎自研 vs 全景 SaaS vs no-code 展览平台**：三条产业路线(文博/营销/艺术教育各有偏好) (evidence: [T02-S001, S016, S024, S029])
- **渲染后端: WebGL(稳态) vs WebGPU+TSL(新兴)**：API 代际迁移进行中, TSL 是「写一次跨后端」的桥 (evidence: [T02-S002, S030, S031])

**新兴工具信号**:
- 当前活跃 / 上升的新工具数: 3（WebGPU+TSL 已主流化中 / 3D Gaussian Splatting / AI 生成展厅）
- 出现 → 主流 速度估计: WebGPU 约 24 个月从 ~8% 到各浏览器基线(2025 末)、核心库已默认; Gaussian Splatting 仍 6-12 月观察期

**冷僻 / 信号薄弱**:
- 必备层 9 个、场景特化 10 个、新兴 3 个 —— **三层均达标, 非冷僻行业**, 信号厚。
- 薄弱点: 国内平台(众趣/酷雷曼/720云/「比目鱼」「会鸽」)以 vendor 营销页为主, 缺独立第三方 production 评测与价格透明度; 「比目鱼」「会鸽」公开一手资料过少未单列。AI 生成展厅为单源 vendor 宣称(T02-S027), 可信度 low。
- 矛盾保留: 自研灵活 vs SaaS 省事; Draco vs Meshopt; 真 3D vs 全景; WebGL 稳 vs WebGPU 新 —— 均已在决策树/流派中保留, 供 Phase 1.5 用户裁决。
