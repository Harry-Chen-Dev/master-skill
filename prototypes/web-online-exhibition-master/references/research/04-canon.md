# Track 04 — Canon：Web 线上展览 / 虚拟展厅开发

> 重点：开发工程 + 性能 + 自研 vs SaaS。Research date 2026-06-06。Locale zh-CN（canon 全球）。
> profile=practitioner（工程视角）。本行 canon 是**规范 + 文档 + 课程**三件套，而非传统教科书 —— 这是一个工程化、规范驱动、几乎没有学术 textbook 的领域，canon 主体是 Khronos/W3C 一手规范 + 顶级开源项目文档 + 一门事实标准课程。

## Source Manifest

| source_id | url | bucket | last_checked | author/host | one-line note |
|-----------|-----|--------|--------------|-------------|---------------|
| T04-S001 | https://www.khronos.org/gltf/ | verified_primary | 2026-06-06 | Khronos Group | glTF 2.0 官方主页，"JPEG of 3D"，ISO/IEC 12113:2022（标准制定者一手） |
| T04-S002 | https://www.w3.org/TR/webgpu/ | verified_primary | 2026-06-06 | W3C | WebGPU 规范，CRD 2026-05-21，现代 GPU API |
| T04-S003 | https://www.w3.org/TR/webxr/ | verified_primary | 2026-06-06 | W3C | WebXR Device API，CRD 2026-03-16，3DoF/6DoF 定义 |
| T04-S004 | https://www.khronos.org/api/webgl | verified_primary | 2026-06-06 | Khronos Group | WebGL 官方，基于 OpenGL ES，WebGL1=ES2.0 / WebGL2=ES3.0 |
| T04-S005 | https://threejs.org/manual/#en/fundamentals | verified_primary | 2026-06-06 | three.js | 官方 manual，Scene/Camera/Renderer/Mesh 场景图基础 |
| T04-S006 | https://threejs.org/docs/ | verified_primary | 2026-06-06 | three.js | 官方 API 文档（一手项目文档） |
| T04-S007 | https://threejs-journey.com/ | secondary | 2026-06-06 | Bruno Simon | Three.js Journey 课程平台页（66 课/93h，事实标准课程） |
| T04-S008 | https://discoverthreejs.com/ | verified_primary | 2026-06-06 | Lewy Blue（核心贡献者） | 《Discover three.js》免费在线书，现代 three.js |
| T04-S009 | https://r3f.docs.pmnd.rs/getting-started/introduction | verified_primary | 2026-06-06 | Poimandres (pmndrs) | React Three Fiber 官方文档（一手项目文档） |
| T04-S010 | https://doc.babylonjs.com/ | verified_primary | 2026-06-06 | Babylon.js (Microsoft 社区) | Babylon.js 官方文档，全功能 3D 引擎，WebGL2+WebGPU |
| T04-S011 | https://github.com/google/draco | verified_primary | 2026-06-06 | Google | Draco 网格压缩库 + KHR_draco_mesh_compression |
| T04-S012 | https://github.com/BinomialLLC/basis_universal | verified_primary | 2026-06-06 | Binomial LLC | Basis Universal 超压缩 GPU 纹理 + KTX2 |
| T04-S013 | https://github.com/zeux/meshoptimizer | verified_primary | 2026-06-06 | Arseny Kapoulkine (zeux) | meshoptimizer + EXT_meshopt_compression，保 GPU 顺序 |
| T04-S014 | https://gltf-transform.dev/ | verified_primary | 2026-06-06 | Don McCurdy | glTF-Transform：glTF 2.0 SDK/CLI，压缩+优化管线 |
| T04-S015 | https://github.com/KhronosGroup/glTF/tree/main/extensions/2.0/Khronos | verified_primary | 2026-06-06 | Khronos Group | glTF 扩展注册表，确认三大压缩扩展 |
| T04-S016 | https://developer.mozilla.org/en-US/docs/Web/API/WebGL_API/WebGL_best_practices | verified_primary | 2026-06-06 | MDN | WebGL 性能最佳实践（draw call/批处理/显存/纹理压缩） |
| T04-S017 | https://modelviewer.dev/ | verified_primary | 2026-06-06 | Google | <model-viewer> web component，一行 HTML 看 glTF + AR |
| T04-S018 | https://iiif.io/get-started/how-iiif-works/ | verified_primary | 2026-06-06 | IIIF Consortium | IIIF Image+Presentation API，文博图像互操作事实标准 |
| T04-S019 | https://arxiv.org/abs/2308.04079 | verified_primary | 2026-06-06 | Kerbl, Kopanas et al. (Inria) | 3D Gaussian Splatting，SIGGRAPH 2023，实时辐射场 |
| T04-S020 | https://arxiv.org/abs/2003.08934 | verified_primary | 2026-06-06 | Mildenhall et al. (UC Berkeley) | NeRF，ECCV 2020，神经隐式场景重建奠基 |
| T04-S021 | https://wwj.beijing.gov.cn/bjww/362690/bzh/21232722/index.html | verified_primary | 2026-06-06 | 北京市文物局 | DB11/T 1922-2021《文物三维数字化技术规范 器物》（gov 一手） |
| T04-S022 | https://std.samr.gov.cn/hb/search/stdHBDetailed?id=1B22F5F2ACB2D349E06397BE0A0AD387 | verified_primary | 2026-06-06 | 国家市场监督管理总局 | 全国标准信息平台：可移动文物数字化采集行业标准（gov 一手） |

**buckets**：verified_primary 21 / secondary 1（threejs-journey 为付费课程平台页，按 brief「课程平台页」归 secondary）/ 0 blacklisted。
**一手比例**：21/22 ≈ 95%（远超 50% 门槛）。Khronos/W3C/MDN/arXiv/gov.cn 直接命中 verified_primary；threejs.org/iiif.io/modelviewer.dev/gltf-transform.dev/babylonjs/r3f/discoverthreejs verifier 默认 secondary，但均为**一手项目/规范/标准官方文档**，按 brief bucket 定义（含 threejs.org/web.dev/IIIF.io）上调 verified_primary，note 已标。无黑名单命中（知乎/CSDN/公众号一律未收）。

---

## 总览（按类型分组）

### 规范 / 标准（Specs —— 本行真正的"必读"，必读 5 / 推荐 2）

| 规范 | 制定者 | 状态(2026-06) | Endorsement | 一句话 |
|------|--------|--------------|-------------|--------|
| **glTF 2.0** | Khronos | ISO/IEC 12113:2022 已定稿 | S001,S005,S014,S017 | 3D 资产传输/运行时格式的事实+ISO 标准，"JPEG of 3D" |
| **WebGL 1/2** | Khronos | 稳定（ES2.0/3.0） | S004,S005,S016 | 浏览器无插件 3D 的现役底座，10+ 年兼容性王者 |
| **WebGPU** | W3C | Candidate Recommendation Draft | S002,S010,S016 | 下一代 GPU API，对齐 Vulkan/Metal/D3D12，含 compute |
| **WebXR Device API** | W3C | Candidate Recommendation Draft | S003,S010 | web 端访问 VR/AR 硬件，定义 3DoF/6DoF/reference space |
| **KTX2 / Basis Universal** | Khronos / Binomial | 稳定，KHR_texture_basisu | S001,S012,S014,S016 | 超压缩 GPU 纹理，省显存+省下载，转码到 ETC/BC/ASTC |
| **DB11/T 1922-2021** | 北京市文物局 | 现行（2022-04 实施） | S021 | 文博器物三维数字化官方流程规范（中国地方标准） |
| **可移动文物数字化采集** 行标 | 国家文物局 | 行业标准 | S022 | 全国文保标委归口，文物 2D/3D 采集加工国标层 |

### Textbook / 系统性著作（本行近乎空白；以"书形态文档"替代，必读 1 / 推荐 1）

| 书 | 作者 | 难度 | Endorsement | 一句话 |
|----|------|------|-------------|--------|
| **Discover three.js** | Lewy Blue（核心贡献者） | 入门→进阶 | S008,S005 | 免费在线书，系统讲现代 three.js + glTF 加载 |
| **three.js 官方 manual** | three.js team | 入门→进阶 | S005,S006 | 官方教程，等价于这一行的"教科书章节" |

> 诚实标注：本行**没有传统意义的学术 textbook / monograph**（无 O'Reilly/MIT Press 级权威专著垄断）。系统性知识由"官方 manual + 免费在线书 + 一门付费课程"承载 —— 典型的"过度工程化、规范驱动"行业 canon 形态。

### Seminal Papers（适度，scene-capture 前沿 2）

| 论文 | 年 | 核心 idea | Endorsement |
|------|----|-----------|-------------|
| **3D Gaussian Splatting** | 2023 (SIGGRAPH) | 各向异性 3D 高斯 + 可见性感知光栅化，>=30fps@1080p 实时辐射场 | S019 |
| **NeRF** | 2020 (ECCV oral) | 5D 神经隐式场 + 体渲染做新视角合成 | S020 |

### Courses（必看 1）

| 课程 | 讲师 | 格式 | Last_updated | 一句话 |
|------|------|------|--------------|--------|
| **Three.js Journey** | Bruno Simon | 视频 66 课 / 93h | rolling（持续更新，含 R3F/shaders/性能章） | 事实标准课程，three.js 作者背书，5w+ 学员 |

### Core Concepts（25 个，见下）

| # | 概念 | 一句话定义 | 来源 |
|---|------|-----------|------|
| 1 | glTF / GLB | 3D 资产运行时传输格式，GLB 是单文件二进制封装 | S001 |
| 2 | Draco | Google 网格几何压缩，省下载、增 CPU 解码 | S011 |
| 3 | KTX2 / Basis Universal | 超压缩 GPU 纹理容器，转码到原生格式，省显存 | S012 |
| 4 | Meshopt（EXT_meshopt_compression） | 保 GPU 缓存顺序的顶点/索引压缩 | S013 |
| 5 | glTF-Transform | glTF 优化管线 SDK/CLI（压缩+简化+去重） | S014 |
| 6 | Draw call | 一次 GPU 绘制提交；过多=CPU 瓶颈 | S016 |
| 7 | Instancing | 一次 draw call 画多份相同几何 | S010,S016 |
| 8 | Batching / 合批 | 合并多次绘制为更少更大的 draw call | S016 |
| 9 | Frustum culling | 视锥剔除，不画看不见的物体 | S010 |
| 10 | LOD（细节层次） | 按距离切换模型精度，远处用低面数 | S016,S010 |
| 11 | Mipmap | 纹理多级缩略，省带宽+抗闪烁，~30% 显存开销 | S016 |
| 12 | 显存 / VRAM 预算 | 按像素数算的 GPU 内存上限，移动端是硬约束 | S016 |
| 13 | 首屏（首帧可交互） | 加载优先派的第一性指标 | S016,S008 |
| 14 | 降级 / fallback | WebGL 不可用/弱机时退到全景或低配 | S004,S016 |
| 15 | WebGL vs WebGPU | 现役底座 vs 下一代 GPU API（含 compute） | S002,S004 |
| 16 | 全景 vs 真 3D | 720 全景轻量 vs 重场景 mesh，两条技术路线 | intake,S017 |
| 17 | 3DoF vs 6DoF | 仅旋转 vs 旋转+平移，决定沉浸/漫游能力 | S003 |
| 18 | WebXR session / reference space | immersive/inline 会话 + 坐标参考系 | S003 |
| 19 | 数字孪生 | 实体空间/文物的高保真数字镜像 | intake,S021 |
| 20 | 热点 hotspot | 3D/全景中的可交互标注点（图文/语音/跳转） | intake,S017 |
| 21 | 动线设计 | 策展引导的参观路径/视角序列 | intake |
| 22 | IIIF | 文博高清图像互操作框架（Image+Presentation API） | S018 |
| 23 | 高斯泼溅 3DGS | 用 3D 高斯做实时真实感场景重建/扫描 | S019 |
| 24 | NeRF | 神经隐式辐射场新视角合成（扫描前沿） | S020 |
| 25 | PBR（基于物理渲染） | 物理正确的材质/光照模型，glTF 默认材质体系 | S010,S008 |

---

## 规范 / 标准详述

### 📄 1. glTF 2.0（Khronos）—— 本行第一规范

- **制定者**: Khronos Group
- **状态**: glTF 2.0；2022 年成为 **ISO/IEC 12113:2022** 国际标准
- **One-liner**: 3D 场景与模型高效传输/加载的免版税规范，被官方称为 "the JPEG of 3D"（evidence: [T04-S001]，一手）
- **核心 idea**: JSON 描述场景结构 + 二进制 buffer 存几何/纹理；可打包成单一 **.glb** 二进制文件；目标是"最小化资产体积 + 最小化运行时解包成本"（evidence: [T04-S001]，一手）
- **关键扩展（压缩三件套）**：glTF 扩展注册表确认存在
  - **KHR_draco_mesh_compression** —— Draco 网格压缩（evidence: [T04-S011, T04-S015]，一手）
  - **KHR_texture_basisu** —— KTX2 / Basis Universal 纹理超压缩（evidence: [T04-S001, T04-S015]，一手）
  - **meshopt 压缩** —— 见下方矛盾标注（evidence: [T04-S013, T04-S015]，一手）
- **为什么经典**: 被 three.js / Babylon.js / model-viewer / gltf-transform 直接实现为默认导入格式；ISO 背书（evidence: [T04-S005, T04-S010, T04-S014, T04-S017]，一手，≥3 源）
- **如何读**: 不必从头读规范；先看官网 overview 理解 GLB + 扩展模型，工程上直接用 gltf-transform 处理资产
- **可信度**: high / **Decay risk**: low（ISO 标准，极稳定）

⚠️ **保留矛盾（扩展命名）**：glTF 扩展目录页抓取显示为 `KHR_meshopt_compression`（evidence: [T04-S015]），但 meshoptimizer 仓库与业界通行名是 **`EXT_meshopt_compression`**（多厂商 EXT 前缀）（evidence: [T04-S013]）。推断：实际 ratified 名为 `EXT_meshopt_compression`，抓取页可能为目录索引措辞差异，使用时以 `EXT_` 为准。标记 待 Phase 2 二次确认。

### 📄 2. WebGL（Khronos）—— 现役底座

- **One-liner**: 跨平台免版税的低层 3D 图形 web 标准，基于 **OpenGL ES**，经 HTML5 Canvas 暴露给 JS（evidence: [T04-S004]，一手）
- **核心**: 基于着色器（GLSL）；**WebGL 1.0 = OpenGL ES 2.0**，**WebGL 2.0 = OpenGL ES 3.0** 特性集（evidence: [T04-S004]，一手）
- **为什么经典**: 是 three.js / Babylon.js 的默认渲染后端，是过去十年所有 web 3D 的地基，兼容性覆盖最广（evidence: [T04-S005, T04-S016]，一手）
- **可信度**: high / **Decay risk**: low（短期内仍是兼容性底线，被 WebGPU 渐进取代但不会消失）

### 📄 3. WebGPU（W3C）—— 下一代

- **状态**: **Candidate Recommendation Draft，2026-05-21**（evidence: [T04-S002]，一手）
- **One-liner**: 暴露 GPU 渲染与计算能力的现代 web API（evidence: [T04-S002]，一手）
- **核心**: 从零设计以高效映射到 **2014 年后的原生 GPU API**（Vulkan/Metal/D3D12）；规范明确 **"WebGPU is not related to WebGL and does not explicitly target OpenGL ES"**（evidence: [T04-S002]，一手）；带来 compute shader 等 WebGL 拿不到的能力
- **为什么经典**: Babylon.js 已支持双后端，three.js 推 WebGPURenderer，是性能派的未来方向（evidence: [T04-S010, T04-S016]，一手）
- **可信度**: high / **Decay risk**: medium（仍在 CR 阶段、浏览器铺开中，"现状"判断会随时间变）

### 📄 4. WebXR Device API（W3C）

- **状态**: **Candidate Recommendation Draft，2026-03-16**；推进到 PR 需 ≥2 个独立可互操作实现（evidence: [T04-S003]，一手）
- **One-liner**: 让 web 访问 VR/AR 硬件、构建跨多种硬件形态的沉浸式应用（evidence: [T04-S003]，一手）
- **核心概念**: immersive(VR/AR) vs inline session；**3DoF**（仅旋转）vs **6DoF**（旋转+平移）；reference space（viewer/local/local-floor/bounded-floor/unbounded）（evidence: [T04-S003]，一手）
- **OpenXR 关系**: 规范本身不直接讨论 OpenXR，聚焦 web API 设计独立于底层平台实现（evidence: [T04-S003]，一手）。OpenXR 是 Khronos 原生 XR 跨厂商标准，WebXR 是其 web 端对应物（点到，推断）
- **可信度**: high / **Decay risk**: medium

### 📄 5. KTX2 / Basis Universal（Khronos / Binomial）

- **One-liner**: 开源"超压缩 LDR/HDR GPU 纹理交换系统"，可快速转码到几乎任意 GPU 纹理格式（ETC1S/UASTC/BC/ASTC），大幅降低 **VRAM + 下载体积**（evidence: [T04-S012]，一手）
- **为什么进 canon**: glTF 通过 KHR_texture_basisu 标准化它；是解决"显存爆 + 移动端纹理"的核心手段（evidence: [T04-S001, T04-S016]，一手）
- **可信度**: high / **Decay risk**: low

### 📄 6-7. 中国文博数字化标准（gov 一手 surrogate canon）

- **DB11/T 1922-2021《文物三维数字化技术规范 器物》**：北京市文物局发布（北京市市场监督管理局批准），首部器物类可移动文物三维数字化地方标准，规定**工作流程、前期准备、数据采集、数据加工、数字化成果**，9 章正文+6 附录，2022-04-01 实施（evidence: [T04-S021]，一手 gov）
- **可移动文物 2D/3D 数字化采集与加工 行业标准**：全国文物保护标准化技术委员会归口、国家文物局主管，规定文物影像/三维采集加工流程与成果提交（evidence: [T04-S022]，一手 gov）
- **为什么进 canon**: 文博考据派的 ground truth —— 决定"高清文物/数字孪生"的合规采集与质量门槛，是营销转化派常忽视的一手依据
- **可信度**: high / **Decay risk**: low（标准更新慢）

---

## Books / 文档详述

### 📖 Discover three.js（Lewy Blue）

- **Author**: Lewy Blue（three.js core contributor，与 Track 01 figures 关联）
- **Type**: 免费在线书（interactive book）
- **One-liner**: 系统教现代 three.js 的免费在线书，从场景基础到 glTF 模型加载、动画、PBR、响应式（evidence: [T04-S008]，一手）
- **核心论点**: 动画循环 / 基于物理渲染 / 变换 / 响应式设计 / glTF 加载 / 内置动画系统 / 相机控制（evidence: [T04-S008]，一手）
- **读完得到什么**: 能从零搭出一个加载外部 glTF、可交互、响应式的 three.js 应用
- **难度**: 入门→进阶
- **Endorsement evidence**: [type: blog_secondary] 官方文档体系内引用一致（S005）；[type: figure_long] 作者本人是核心贡献者，内容与官方 manual 互补（S008）；社区长期作为 three.js 入门首选书
- **可信度**: high / **Decay risk**: medium（three.js API 偶有破坏性更新，需看维护状态）

### 📖 three.js 官方 manual + docs

- **One-liner**: 官方教程，定义本行场景图心智模型 —— Scene（容器）/ Camera（视点）/ Renderer（绘制）/ Mesh（Geometry+Material）/ Light（evidence: [T04-S005]，一手）
- **核心**: three.js 是 **WebGL/WebGPU 库**；一个 three.js app 的根本结构是 Scene + Camera + Renderer 三件 + 物体树（evidence: [T04-S005]，一手）
- **Endorsement**: [type: course_syllabus] Three.js Journey 全程基于官方 API（S007）；[type: blog_secondary] Discover three.js 与之互补（S008）；官方一手（S005,S006）
- **可信度**: high / **Decay risk**: medium（docs 随版本走，需 last_checked）

---

## Courses 详述

### 🎓 Three.js Journey（Bruno Simon）—— 事实标准课程

- **Lecturer**: Bruno Simon（法国 creative developer，WebGL 7+ 年教学；与 Track 01 figures 强关联）
- **Format**: 视频 + 文字 + 字幕 + quiz/认证
- **Duration**: **66 课 / 93 小时**，7 章
- **完整路径 vs 关键章节**: 完整=Basics→Classic→Advanced→**Shaders(GLSL)**→Extra(post-processing+**性能优化**)→Portal Scene(Blender 烘焙)→**React Three Fiber**。线上展览工程最相关：Advanced（模型导入/Blender/代码结构）+ Extra 性能章 + R3F 章（evidence: [T04-S007]，一手课程页）
- **难度 / 先修**: 入门可进，需 JS 基础；进阶到 shader/性能
- **Endorsement evidence**: [type: figure_long] **three.js 作者本人背书**；5w+ 学员；[type: course_syllabus] 课程本身即业界事实标准 reading path（evidence: [T04-S007]）
- **Last_updated**: rolling（持续更新，已含 R3F/shaders/性能 现代内容）
- **可信度**: high / **Decay risk**: low-medium（rolling 更新，但付费门槛 $95，可获取性略低于免费资源）

---

## Seminal Papers 详述

### 📄 3D Gaussian Splatting for Real-Time Radiance Field Rendering

- **Authors**: Bernhard Kerbl, Georgios Kopanas, Thomas Leimkühler, George Drettakis（Inria / MPI）
- **Venue + Year**: ACM TOG 42(4)，SIGGRAPH 2023
- **arXiv**: https://arxiv.org/abs/2308.04079
- **One-liner**: 用各向异性 3D 高斯 + 可见性感知光栅化，实现 **>=30fps@1080p 实时**新视角合成（evidence: [T04-S019]，一手）
- **核心 idea**: 从稀疏 SfM 点初始化 3D 高斯，优化协方差，**非神经网络**表示，跳过空白空间（evidence: [T04-S019]，一手）
- **为什么对展览扫描重要**: 3DGS 让"扫一个真实空间/文物→可实时漫游的 web 场景"在质量+速度上首次实用化，是真 3D 重场景派的新范式（推断，基于 [T04-S019]）
- **如何读**: 看 abstract + method 概念即可，工程上关注其在 web viewer 中的落地
- **可信度**: high / **Decay risk**: medium（前沿，工具链快速演进）

### 📄 NeRF: Representing Scenes as Neural Radiance Fields

- **Authors**: Mildenhall, Srinivasan, Tancik, Barron, Ramamoorthi, Ng（UC Berkeley 等）
- **Venue + Year**: ECCV 2020（oral）
- **arXiv**: https://arxiv.org/abs/2003.08934
- **One-liner**: 用 5D 坐标(x,y,z,θ,φ)→密度+辐射的神经隐式场 + 体渲染做新视角合成（evidence: [T04-S020]，一手）
- **为什么经典**: 神经隐式场景重建的奠基作，3DGS 的直接前驱；对展览=可从少量照片重建场景（evidence: [T04-S020]，一手）
- **如何读**: 点到为止 —— 理解"隐式场 vs 显式 mesh"的范式差异即可
- **可信度**: high / **Decay risk**: medium（被 3DGS 在速度上超越，但概念奠基地位不衰）

---

## Phase 2 提炼提示

**反复出现 ≥ 3 个 canon 都讨论的核心 idea**（候选心智模型）：
- **"传输/运行时格式与建模格式分离"**：glTF 定位为传输格式（S001）+ gltf-transform 做离线优化（S014）+ model-viewer 直接吃 GLB（S017）→ 心智模型「资产管线 = 建模软件 → glTF 优化 → 运行时」
- **"draw call / 显存 是 web 3D 第一性约束"**：MDN 性能（S016）+ Babylon/Three 的 instancing(S010) + 课程性能章(S007)→ 心智模型「加载优先：先算显存预算和 draw call 预算，再谈沉浸」
- **"压缩三件套各有取舍"**：Draco(几何，省体积增 CPU，S011) vs Meshopt(保 GPU 顺序，S013) vs KTX2(纹理省显存，S012)→ 心智模型「按瓶颈选压缩：下载瓶颈用 Draco，渲染瓶颈用 Meshopt，显存瓶颈用 KTX2」
- **"3DoF/6DoF 决定形态"**：WebXR(S003) + 全景 vs 真 3D(intake)→ 心智模型「先定自由度，再定技术栈：3DoF→全景轻量，6DoF→真 3D 重场景」

**智识谱系种子**：
- **3D web 工程流派**奠基：Khronos glTF/WebGL 规范（S001,S004）；当前代表：three.js（Mr.doob）+ Bruno Simon（课程，S007）+ Don McCurdy（管线，S014）；声明式分支：React Three Fiber / Poimandres（S009）
- **全功能引擎流派**：Babylon.js（Microsoft 社区，S010）—— 与 three.js"库 vs 引擎"的长期分野
- **性能/加载优先流派**：MDN/web.dev 性能 canon（S016）+ 课程性能章 —— 与"沉浸优先"对立
- **文博考据流派**：IIIF（S018，图像互操作）+ 中国文物数字化国标（S021,S022）—— 与"营销转化派"对立
- **场景重建前沿**：NeRF（S020）→ 3D Gaussian Splatting（S019）的代际更替
- **主要分歧（still-debated）**：见下"保留矛盾"

**核心概念 → 候选 playbook**：
- 遇到"模型太大/首屏慢"→ 走 gltf-transform 压缩三件套 + LOD + instancing + frustum culling（S014,S016,S010）
- 遇到"移动端崩/白屏"→ 先查显存预算（KTX2 纹理）+ WebGL fallback 降级（S016,S004）
- 遇到"要不要上 WebGPU"→ 看是否需要 compute / 大规模实例；兼容性优先则 WebGL（S002,S004）
- 遇到"扫真实空间做展厅"→ 评估 3DGS（实时）vs 传统 mesh 摄影测量（S019）
- 遇到"高清文物/合规"→ 对齐 IIIF + 国家文物局采集标准（S018,S021,S022）

**冷僻 / 信号薄弱（诚实边界）**：
- **无传统学术 textbook**：本行 canon 由"规范 + 官方文档 + 1 门课 + 免费在线书"承载，非教科书形态 → Phase 2.8 应标「canon 以工程规范/文档为主体，因领域过度工程化、规范驱动、年轻（核心规范多为 2017 后）」
- **课程仅 1 门达事实标准**（Three.js Journey，且付费）→ courses 维度信号偏薄但质量极高
- **自研 vs SaaS 选型 几乎无中立一手 canon**：SaaS 平台（Matterport/众趣/酷雷曼等）只有 vendor docs，brief 已要求标 surrogate；本 Track 未收 vendor 营销页（留给 Track 02 tools）→ 选型判断需跨 Track 02 补
- **中文一手 canon 稀缺**：除 gov 标准外，中文 3D web 优质一手内容多在黑名单平台（知乎/CSDN/掘金），已一律排除；canon 主体为英文规范/文档（locale 本就 canon 全球，符合预期）

**保留的核心矛盾（供 Phase 2 直接用作"学派分歧"）**：
1. **WebGL vs WebGPU 现状**：WebGPU 规范明确"与 WebGL 无关、不针对 OpenGL ES"（S002），但仍处 CRD、浏览器铺开中；WebGL 仍是兼容性底线（S004）→ 现役 vs 未来之争，无定论
2. **3DGS vs 传统 mesh**：3DGS 实时真实感强（S019）但生态/编辑/兼容仍新；传统 glTF mesh 成熟可控（S001）→ 扫描重建派 vs 工程可控派
3. **Draco vs Meshopt**：Draco 压缩率高但打乱 GPU 顶点顺序、渲染效率低；Meshopt 保 cache 友好顺序、兼顾渲染（S013）→ 体积优先 vs 渲染优先，明确取舍
4. **沉浸/加载优先**：性能 canon（S016）暗示"加载优先（首屏/显存）"，与"真 3D 重场景沉浸优先"对立（intake 学派分歧印证）
5. **文博考据 vs 营销转化**：IIIF + 国标（S018,S021,S022 考据合规）vs 营销云展厅（埋点/转化，intake）—— 两套质量标准
