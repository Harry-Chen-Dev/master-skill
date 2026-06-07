# Track 01 — Figures：Web 线上展览 / 虚拟展厅开发（重点：开发工程）

> Research date: 2026-06-06 · Locale: zh-CN（canon 全球）· OPUS subagent
>
> **figure 稀薄度诚实判断（先说结论）**：这是 tech 领域，"思想领袖"本质上是 **开源库作者 + 教育布道者 + 开放标准推动者**，不是传统意义的"行业大佬"。真 figure 偏冷但**质量很高**——大量第一方 GitHub / 个人站 / conference talk / 长 podcast 可拿。
> 关键结论：figures 维度**不薄反厚**，但**重心明显偏"工具创造者 + 方法论教育者"**，而非"展览业务/策展思想家"。可独立蒸馏成 sub-skill 的方法论者集中在 **Bruno Simon（教学法）/ mrdoob（库设计哲学）/ Paul Henschel（声明式 3D 范式）** 三人。文博 / 商业平台一侧 figure 真人发声稀薄（多为 vendor PR + 黑名单中文站），已用 surrogate（官网 vendor docs / TED talk）补，诚实标注。
> **Phase 2 权重建议**：figures 主要贡献"立场光谱"（自研 vs SaaS、命令式 vs 声明式、性能 vs 沉浸、网格 vs 辐射场），canon/tools/workflows 承载主体方法论。

---

## Source Manifest

| source_id | url | bucket | last_checked | author/host | one-line note |
|-----------|-----|--------|--------------|-------------|---------------|
| T01-S001 | https://github.com/mrdoob/three.js | verified_primary | 2026-06-06 | Ricardo Cabello (mrdoob) | Three.js 主仓库，事实标准 3D web 库 |
| T01-S002 | https://ricardocabello.com/ | secondary | 2026-06-06 | mrdoob | 个人作品集站（2026 仍在更新 Draco/Doom port） |
| T01-S003 | https://jsconf.jp/2024/talk/mrdoob/ | secondary | 2026-06-06 | JSConf JP | mrdoob 2024 talk「Three.js WebGL→WebGPU」 |
| T01-S004 | https://www.realtimerendering.com/blog/interview-with-three-js-creator/ | verified_primary | 2026-06-06 | Real-Time Rendering | mrdoob 长访谈（demoscene 出身、Google Data Arts） |
| T01-S005 | https://github.com/mrdoob/three.js/wiki/Three.js-Shading-Language | verified_primary | 2026-06-06 | Three.js | TSL 官方 wiki — node 材质 / WebGPU 范式 |
| T01-S006 | https://github.com/mrdoob/three.js/issues/30849 | reference | 2026-06-06 | Three.js | TSL Roadmap issue — 社区迁移争议现场 |
| T01-S007 | https://bruno-simon.com/ | secondary | 2026-06-06 | Bruno Simon | 经典 3D 作品集（开卡丁车逛简历），R3F 前 vanilla 范本 |
| T01-S008 | https://threejs-journey.com/lessons/introduction | secondary | 2026-06-06 | Bruno Simon | Three.js Journey 课程导论 — 教学法原文 |
| T01-S009 | https://github.com/brunosimon | secondary | 2026-06-06 | Bruno Simon | 作品集 + folio 源码（MIT，含 Blender 文件） |
| T01-S010 | https://www.mux.com/blog/3d-web-development-and-beyond-a-chat-with-bruno-simon | verified_primary | 2026-06-06 | Mux | Bruno Simon 长访谈（performance/学习观直接引语） |
| T01-S011 | https://www.youtube.com/watch?v=xumMbH29NO8 | reference | 2026-06-06 | YouTube | Bruno Simon 视频访谈「building 3D websites」2024 |
| T01-S012 | https://github.com/pmndrs/react-three-fiber | verified_primary | 2026-06-06 | Paul Henschel / Poimandres | R3F 主仓库 — 声明式 Three.js 渲染器 |
| T01-S013 | https://github.com/drcmda | secondary | 2026-06-06 | Paul Henschel (0xca0a) | R3F/drei/zustand/react-spring 作者主页 |
| T01-S014 | https://opencollective.com/drcmda | secondary | 2026-06-06 | Paul Henschel | Poimandres 集体资助页 — 治理/资金立场 |
| T01-S015 | https://www.telerik.com/react-wednesdays/react-three-fiber-with-paul-henschel | secondary | 2026-06-06 | Telerik | Paul Henschel 长访谈（R3F 设计动机） |
| T01-S016 | https://pmnd.rs/blog/introducing-the-poimandres-blog | verified_primary | 2026-06-06 | Poimandres | PMNDRS 集体官博 — 60+ repo 生态宣言 |
| T01-S017 | https://www.donmccurdy.com/ | secondary | 2026-06-06 | Don McCurdy | glTF/Three.js loader 作者个人站 |
| T01-S018 | https://github.com/donmccurdy/glTF-Transform | verified_primary | 2026-06-06 | Don McCurdy | glTF 优化/管线核心库 |
| T01-S019 | https://gltf-transform.dev/ | secondary | 2026-06-06 | Don McCurdy | glTF Transform 文档站（vendor docs） |
| T01-S020 | https://cesium.com/blog/2025/11/20/advancing-3d-tiles-and-gltf-in-an-open-ecosystem/ | verified_primary | 2026-06-06 | Cesium | 2025 glTF/3D Tiles 演进 + McCurdy 转 Bentley 任开放标准总监 |
| T01-S021 | https://github.com/google/model-viewer | verified_primary | 2026-06-06 | Google | `<model-viewer>` web component — 零门槛 3D/AR |
| T01-S022 | https://github.com/BabylonJS/Babylon.js | verified_primary | 2026-06-06 | David Catuhe et al / Microsoft | Babylon.js 引擎主仓库 |
| T01-S023 | https://doc.babylonjs.com/ | secondary | 2026-06-06 | Microsoft | Babylon.js 官方文档（vendor docs） |
| T01-S024 | https://medium.com/open-at-microsoft/david-founder-of-babylon-js-and-principal-program-manager-microsoft-3dd387a37949 | secondary | 2026-06-06 | Microsoft Open Source | David Catuhe 自述（Babylon 起源 + 角色） |
| T01-S025 | https://github.com/aframevr/aframe | verified_primary | 2026-06-06 | Diego Marcos / Supermedium | A-Frame 主仓库 — HTML 写 WebXR |
| T01-S026 | https://github.com/dmarcos | secondary | 2026-06-06 | Diego Marcos | A-Frame 共同作者主页 |
| T01-S027 | https://www.uploadvr.com/diego-marcos-interview-webxr/ | secondary | 2026-06-06 | UploadVR | Diego Marcos 长访谈（"web 就是 metaverse"立场） |
| T01-S028 | https://voicesofvr.com/1475-a-frames-diego-marcos-on-webxr-momentum-and-integrations-with-open-source-ai/ | secondary | 2026-06-06 | Voices of VR | Diego Marcos 2024 podcast（WebXR+开源 AI） |
| T01-S029 | https://blog.maximeheckel.com/ | verified_primary | 2026-06-06 | Maxime Heckel | R3F/shader 高质量技术博客 |
| T01-S030 | https://blog.maximeheckel.com/posts/field-guide-to-tsl-and-webgpu/ | verified_primary | 2026-06-06 | Maxime Heckel | TSL+WebGPU 实战指南（最新趋势教学） |
| T01-S031 | https://simondev.io/ | secondary | 2026-06-06 | SimonDev | 资深图形工程师教育站（性能/底层向） |
| T01-S032 | https://github.com/mkkellogg/GaussianSplats3D | verified_primary | 2026-06-06 | Mark Kellogg | Three.js 3D Gaussian Splatting 渲染器 |
| T01-S033 | https://github.com/playcanvas/engine | verified_primary | 2026-06-06 | Will Eastcott / PlayCanvas | PlayCanvas 引擎（WebGL2/WebGPU/WebXR） |
| T01-S034 | https://github.com/playcanvas/supersplat | verified_primary | 2026-06-06 | Will Eastcott / PlayCanvas | SuperSplat — 浏览器内开源高斯泼溅编辑器 |
| T01-S035 | https://www.buildingtheopenmetaverse.org/episodes/revolutionizing-game-development | verified_primary | 2026-06-06 | Building the Open Metaverse | Will Eastcott 长访谈（web 游戏引擎/开放 metaverse） |
| T01-S036 | https://cesium.com/team/patrick-cozzi/ | verified_primary | 2026-06-06 | Cesium | Patrick Cozzi 简介 — glTF 共同创始 / 3D Tiles |
| T01-S037 | https://www.khronos.org/blog/have-gaussian-splats-arrived-in-the-standardization-sweet-spot | verified_primary | 2026-06-06 | Khronos | 2025 高斯泼溅标准化分析（官方 blog） |
| T01-S038 | https://www.khronos.org/news/press/gltf-gaussian-splatting-press-release | secondary | 2026-06-06 | Khronos | glTF 高斯泼溅扩展正式发布（重大 12 月动态） |
| T01-S039 | https://www.ted.com/talks/amit_sood_every_piece_of_art_you_ve_ever_wanted_to_see_up_close_and_searchable | verified_primary | 2026-06-06 | Amit Sood / TED | Google A&C 负责人 TED 2016（gigapixel 数字展愿景） |
| T01-S040 | https://www.ted.com/talks/amit_sood_building_a_museum_of_museums_on_the_web | verified_primary | 2026-06-06 | Amit Sood / TED | Amit Sood TED 2011「web 上的博物馆之博物馆」 |
| T01-S041 | https://blog.google/outreach-initiatives/arts-culture/art-camera-cultural-institute/ | verified_primary | 2026-06-06 | Google | Art Camera gigapixel 数字化（文博线上化技术原文） |
| T01-S042 | https://iiif.io/ | secondary | 2026-06-06 | IIIF 社区 | 文博图像互操作开放标准（深缩放/标注） |
| T01-S043 | https://krpano.com/ | secondary | 2026-06-06 | Klaus (krpano) | 全景虚拟漫游事实标准引擎（vendor docs） |
| T01-S044 | https://matterport.com/ | secondary | 2026-06-06 | Matt Bell / Matterport | 3D 空间捕获/数字孪生 SaaS 平台派代表 |
| T01-S045 | https://www.realsee.com/ | secondary | 2026-06-06 | 如视 Realsee（贝壳） | 国内三维重建/VR 看房，单目深度估计派（vendor docs） |
| T01-S046 | https://www.kuleiman.com/ | secondary | 2026-06-06 | 酷雷曼 | 国内 3DVR 全景营销 SaaS（vendor docs） |
| T01-S047 | https://www.720yun.com/ | secondary | 2026-06-06 | 720云 | 国内全景/XR/数字孪生内容创作平台（vendor docs） |

> **黑名单已剔除**：知乎专栏 / 搜狐 / 界面 / CSDN / VR陀螺 等所有中文二手稿（众趣/realsee 一节大量命中），仅保留 vendor 官网作 surrogate。`bucket` 全部按 `source_verifier.py classify` 实跑结果落表，未私自升级。

---

## 总览（按对"线上展览开发"相关度 + 行业影响力排序）

| # | 姓名 | 核心身份 | 一句话贡献 | 立场标签 | 值得读/听/看 | 来源数 |
|---|------|---------|----------|---------|------------|-------|
| 1 | Ricardo Cabello (mrdoob) | Three.js 创始人 | 把 WebGL 封装成全行业事实标准 3D 库 | 自研开源派 · 性能/底层 | 📖🎬 | 6 |
| 2 | Bruno Simon | Three.js Journey 创始人 + 创意开发者 | 最具方法论可蒸馏的 3D web 教育者 | 自研派 · 沉浸/创意 | 📖🎙️🎬 | 5 |
| 3 | Paul Henschel (0xca0a/drcmda) | R3F + Poimandres 创始人 | 把 Three.js 带进声明式/组件化 React 范式 | 声明式派 · 生态协作 | 📖🎙️ | 5 |
| 4 | Don McCurdy | glTF/Three.js loader 作者，Bentley 开放标准总监 | 资产管线与 glTF 优化的事实权威 | 开放标准派 · 工程 | 📖 | 4 |
| 5 | Patrick Cozzi | glTF 共同创始人 / 3D Tiles 创建者 / Cesium | 把 3D web 资产做成跨厂商开放标准 | 开放标准派 · 地理/海量 | 🎙️ | 3 |
| 6 | David Catuhe (+ David Rousset) | Babylon.js 创始人 / Microsoft | 一体化全功能引擎路线的代表 | 大厂引擎派 · 全功能 | 📖🎙️ | 3 |
| 7 | Will Eastcott | PlayCanvas + SuperSplat 创始人 | web 游戏引擎 + 高斯泼溅编辑工具化 | SaaS+开源派 · 性能 | 📖🎙️ | 3 |
| 8 | Diego Marcos | A-Frame 共同作者 / Supermedium | 用 HTML 标签民主化 WebXR | 开放 web/沉浸派 | 🎙️🎬 | 4 |
| 9 | Mark Kellogg (mkkellogg) | GaussianSplats3D 作者 | 把高斯泼溅带进 Three.js 生态 | 辐射场新派 · 真实感 | 📖 | 2 |
| 10 | Maxime Heckel | 创意工程师 / 技术博主 | R3F+shader+TSL 最佳实践写作者 | 声明式派 · shader 工艺 | 📖 | 2 |
| 11 | SimonDev | 资深图形工程师 / 教育者 | 底层图形/性能深挖的硬核教育者 | 自研派 · 性能/底层 | 📖🎬 | 1 |
| 12 | Amit Sood | Google Arts & Culture 负责人 | gigapixel 数字展/"博物馆之博物馆"愿景 | 文博数字化派 | 🎬🎬 | 3 |
| 13 | Klaus (krpano) | krpano 作者 | 全景虚拟漫游的事实标准引擎 | 全景/工具派 | 📖 | 1 |
| 14 | Matt Bell | Matterport 创始人 | 3D 空间捕获/数字孪生 SaaS 模式开创 | SaaS 平台派 · 捕获 | 📖 | 1 |
| 15 | 高翔 / 如视团队 (代理) | 众趣科技 / 如视 Realsee | 国内三维重建+VR 空间商业化代表 | 国内 SaaS 平台派 | ⚠️surrogate | 3 |

---

## Figure 详细卡片

### 1. Ricardo Cabello（mrdoob）

- **One-liner**: Three.js 创始人，把 WebGL 这种难写的底层 API 封装成全行业可用的事实标准 3D 库——所有线上展览/虚拟展厅的 web 端 90% 直接或间接踩在他的代码上 (evidence: [T01-S001, T01-S004]，一手)
- **核心身份**: Three.js 创始人 + 主维护者；demoscene 出身（1996 起），曾在 Google Data Arts Team 做创意编码 (evidence: [T01-S004]，一手)
- **代表作品**: Three.js (2010 至今)；近期个人实验 Draco.js / Three.js Doom port / Bandcamp Cast (evidence: [T01-S001, T01-S002])
- **值得读/听/看**:
  - 📖 Three.js 主仓库 + TSL wiki：https://github.com/mrdoob/three.js · https://github.com/mrdoob/three.js/wiki/Three.js-Shading-Language (evidence: [T01-S001, T01-S005])
  - 📖 Real-Time Rendering 长访谈（demoscene→Three.js 的来龙去脉）：https://www.realtimerendering.com/blog/interview-with-three-js-creator/ (evidence: [T01-S004])
  - 🎬 JSConf JP 2024 talk「Three.js from WebGL to WebGPU」：https://jsconf.jp/2024/talk/mrdoob/ (evidence: [T01-S003])
- **核心思想关键词**: WebGPU/TSL 迁移、node 材质、tree-shaking、开放可访问、创意实验优先
- **voice_samples**: ⚠️ 暂未找到 ≥ 30 字直接原话片段（mrdoob 公开发声偏代码/demo，少长篇独白）。立场可从行动推断：长期坚持 Three.js MIT 开源 + 主导 WebGPU 重写以追新标准 (evidence: [T01-S001, T01-S005]，推断)
- **sub_skill_candidate**: `true` — 库设计哲学（最小封装 + 跟标准演进）自洽且影响整行；但本人长访谈材料偏少，蒸馏需多靠 commit/issue 行为证据
- **最近 12 个月动态**: 主推 **WebGPURenderer + TSL node 材质**；r171（2025-09）起 WebGPU 标"production-ready"，Safari 26（2025-09）补齐最后一个浏览器；TSL 可同时编译 WGSL/GLSL (evidence: [T01-S005, T01-S006]，一手)
- **争议/批评**: TSL/WebGPU 双轨迁移在社区有显著反弹——"为 WebGL 写的材质在 WebGPU 全废，要维护两套"被批增加迁移成本；NodeMaterial 目前仅 WebGPURenderer 支持，库生态适配滞后 (evidence: [T01-S006]，一手 issue 现场)
- **来源**: [Primary] T01-S001/S005；[Secondary] T01-S002/S003；[Reference] T01-S004/S006
- **可信度自评**: high — 第一方 repo + 多个独立访谈/talk

### 2. Bruno Simon

- **One-liner**: Three.js Journey 创始人，全网最具方法论可蒸馏的 3D web 教育者——他的"开卡丁车逛简历"作品集 + 系统课程几乎定义了"如何学会做沉浸式 3D 网站" (evidence: [T01-S007, T01-S008]，一手)
- **核心身份**: 法国自由创意开发者；7+ 年教 WebGL（700+ 真实学生 + 多个法国硕士项目）；前 Immersive Garden (evidence: [T01-S008, S010]，一手)
- **代表作品**: bruno-simon.com 交互式 3D 作品集（MIT 开源含 Blender 文件）；Three.js Journey 课程 (evidence: [T01-S007, S009])
- **值得读/听/看**:
  - 📖 Three.js Journey 课程导论（教学法原文）：https://threejs-journey.com/lessons/introduction (evidence: [T01-S008])
  - 🎙️ Mux 长访谈（performance / 学习观直接引语）：https://www.mux.com/blog/3d-web-development-and-beyond-a-chat-with-bruno-simon (evidence: [T01-S010])
  - 🎬 YouTube「building 3D websites and creative web development」2024：https://www.youtube.com/watch?v=xumMbH29NO8 (evidence: [T01-S011])
- **核心思想关键词**: 边做边学（starter 文件）、不急于求成、性能优先（"四分之一算力"约束）、数学不好也能做、公开分享作品
- **voice_samples**:
  - 客户/学生解释样本（原话）：「If you know nothing about WebGL and Three.js but want to create cool 3D websites, you've come to the right place」「You don't need to be good at maths. I'm terrible at it, and still, I manage to create cool WebGL experiences」(source: T01-S008, 原话)
  - 同业/职业观样本（原话）：「If it's hard to learn, it's a valuable knowledge... not everybody can do it. So you will have less competitors... you need to struggle just long enough」(source: T01-S010, 原话)
  - 性能/技术判断样本（原话）：「Currently it's a matter mostly of performance... we have maybe like a quarter of the power... it needs to work regardless of the device」(source: T01-S010, 原话)
- **sub_skill_candidate**: `true` — **最佳独立蒸馏候选**：长访谈 + 课程 syllabus 充足、教学法自洽、行业影响力前 3、与"开发工程 focus"高度对齐
- **最近 12 个月动态**: Three.js Journey 持续加 R3F + WebGPU/TSL 章节；2024 公开访谈仍强调"资源多了 100 倍但复杂度高了 1000 倍" (evidence: [T01-S010, S011]，一手)
- **争议/批评**: 未找到实质批评；潜在反主流点是他对 vanilla Three.js 的偏好（作品集是手写而非 R3F），与声明式派形成隐性张力 (evidence: [T01-S007]，推断)
- **来源**: [Primary] T01-S007/S008/S009；[Secondary] T01-S010；[Reference] T01-S011
- **可信度自评**: high — 第一方课程 + 多篇直接引语访谈

### 3. Paul Henschel（0xca0a / drcmda）

- **One-liner**: React Three Fiber + Poimandres 创始人，把命令式的 Three.js 重塑成声明式/组件化的 React 范式——线上展览若用 React 技术栈，他是绕不开的一极 (evidence: [T01-S012, S013]，一手)
- **核心身份**: 德国开发者；R3F 主维护者；Poimandres (PMNDRS) 开源集体创始人（drei / zustand / react-spring 等同出其手） (evidence: [T01-S013, S016]，一手)
- **代表作品**: react-three-fiber、drei、zustand、react-spring；Poimandres 集体（2024 已 60+ repo / 近 60 维护者） (evidence: [T01-S012, S016])
- **值得读/听/看**:
  - 📖 R3F 主仓库 + Poimandres 官博：https://github.com/pmndrs/react-three-fiber · https://pmnd.rs/blog/introducing-the-poimandres-blog (evidence: [T01-S012, S016])
  - 🎙️ Telerik React Wednesdays 长访谈（R3F 设计动机）：https://www.telerik.com/react-wednesdays/react-three-fiber-with-paul-henschel (evidence: [T01-S015])
  - 📖 Open Collective drcmda（资助/治理立场）：https://opencollective.com/drcmda (evidence: [T01-S014])
- **核心思想关键词**: 声明式 3D、组件复用、生态协作（集体而非个人）、状态管理（zustand）、可组合性
- **voice_samples**: ⚠️ 暂未找到 ≥ 30 字直接原话片段（访谈为视频，未取文字稿）。立场可从 Poimandres 宣言推断：「让开发者加入互助、资助并推广项目」的集体主义开源观 (source: T01-S016, 转述)
- **sub_skill_candidate**: `true` — 声明式 3D 范式自洽且影响 React 阵营整体；但个人长文/文字访谈少，蒸馏偏靠生态文档
- **最近 12 个月动态**: R3F 持续跟进 Three.js WebGPU；Poimandres 生态扩张（drei 仍是 R3F 标配 helper 库） (evidence: [T01-S012, S016]，一手)
- **争议/批评**: 声明式 vs 命令式之争——批评者认为 R3F 抽象层在极致性能/复杂场景下不如手写 vanilla Three.js 可控（与 Bruno Simon/SimonDev 的 vanilla 偏好成光谱两端） (evidence: [T01-S007, S031]，推断)
- **来源**: [Primary] T01-S012/S016；[Secondary] T01-S013/S014/S015
- **可信度自评**: high — 第一方 repo + 集体官博 + 视频访谈

### 4. Don McCurdy

- **One-liner**: Three.js 官方 glTF loader 作者 + glTF-Transform 作者，资产管线与 glTF 优化的事实权威——线上展览的模型怎么导出/压缩/管线化，标准很大程度由他塑造 (evidence: [T01-S017, S018, S020]，一手)
- **核心身份**: glTF/3D Formats working group 前共同主席；曾 Google（Project Sunroof）6 年 → CARTO → **2025 入 Bentley 任开放标准 senior director**；A-Frame 维护者之一 (evidence: [T01-S020, S025]，一手)
- **代表作品**: Three.js GLTFLoader、glTF-Transform（优化/管线框架）、gltf.report、three-gltf-viewer (evidence: [T01-S018, S019])
- **值得读/听/看**:
  - 📖 glTF-Transform 仓库 + 文档：https://github.com/donmccurdy/glTF-Transform · https://gltf-transform.dev/ (evidence: [T01-S018, S019])
  - 📖 个人站技术文章（如「Generating glTF programmatically」）：https://www.donmccurdy.com/ (evidence: [T01-S017])
  - 📖 Cesium 2025「Advancing 3D Tiles and glTF」(含其立场)：https://cesium.com/blog/2025/11/20/advancing-3d-tiles-and-gltf-in-an-open-ecosystem/ (evidence: [T01-S020])
- **核心思想关键词**: glTF 是"高效末端传输格式"、资产优化（Draco/meshopt）、开放标准治理、可扩展 extensions
- **voice_samples**:
  - 标准/专业讨论样本（转述）：glTF 应守住「efficient, last-mile transmission to runtime」核心使命，随能力演进但不偏离 (source: T01-S020, 转述)
- **sub_skill_candidate**: `false` — 极重要但贡献是工程产品 + 标准治理，不够独立成"思维方式"sub-skill；其知识更适合进 tools/canon track
- **最近 12 个月动态**: 2025 入职 Bentley 主管开放标准；推动 glTF / 3D Tiles 1.1 收敛（Batched/Instanced Model 并入 glTF extensions） (evidence: [T01-S020]，一手)
- **争议/批评**: 未找到实质批评（标准派人物，争议多在格式之争层面而非个人）
- **来源**: [Primary] T01-S018/S020；[Secondary] T01-S017/S019
- **可信度自评**: high — 第一方 repo + 行业新闻

### 5. Patrick Cozzi

- **One-liner**: glTF 共同创始人 + 3D Tiles 创建者 + Cesium 创始人，把 3D web 资产做成跨厂商（微软/Google/NVIDIA 均采纳）的开放标准，并主持 metaverse 标准互操作 (evidence: [T01-S036]，一手)
- **核心身份**: Cesium 创始人；Metaverse Standards Forum 3D 资产互操作组共同主席；Khronos 3D Formats 工作组前主席；「Building the Open Metaverse」podcast 共同主持 (evidence: [T01-S036]，一手)
- **代表作品**: glTF（共同创始）、3D Tiles（OGC 社区标准，海量地理 3D 流式）、CesiumJS (evidence: [T01-S036])
- **值得读/听/看**:
  - 🎙️ Building the Open Metaverse podcast（他主持，几乎所有 3D web 关键人都上过）：https://www.buildingtheopenmetaverse.org/ (evidence: [T01-S035, S036])
  - 📖 Cesium 团队页 + 2025 glTF 演进 blog：https://cesium.com/team/patrick-cozzi/ · https://cesium.com/blog/2025/11/20/advancing-3d-tiles-and-gltf-in-an-open-ecosystem/ (evidence: [T01-S036, S020])
- **核心思想关键词**: 开放标准互操作、3D Tiles 流式海量数据、metaverse 不靠单一厂商、glTF 生态
- **voice_samples**: ⚠️ 暂未找到 ≥ 30 字直接原话片段（podcast 未取文字稿）。立场清晰：开放/跨厂商互操作优先于专有平台 (source: T01-S036, 推断)
- **sub_skill_candidate**: `false` — 偏地理/海量数据，与"展厅"focus 略偏；但作为 podcast 主持人是 Track 05 sources 的核心节点
- **最近 12 个月动态**: 持续主持 Metaverse Standards Forum 3D 互操作；2025 glTF/3D Tiles 收敛 (evidence: [T01-S020, S036]，一手)
- **争议/批评**: 未找到实质批评
- **来源**: [Primary] T01-S036/S020；[Reference] T01-S035
- **可信度自评**: high — 第一方团队页 + 长 podcast 系列

### 6. David Catuhe（+ David Rousset）

- **One-liner**: Babylon.js 创始人（Microsoft），代表"一体化全功能 web 3D 引擎"路线——相对 Three.js 的极简内核，Babylon 走开箱即用的全栈引擎，是 SaaS/大厂派的工程范本 (evidence: [T01-S022, S024]，一手)
- **核心身份**: David Catuhe = Microsoft 首席项目经理，写引擎核心；David Rousset = 高级项目经理（法国），补 WebVR/Web Audio/gamepad/IndexedDB 离线 (evidence: [T01-S024]，一手)
- **代表作品**: Babylon.js（2013 起，Apache 2.0）；Babylon.js 6.0 性能改进 (evidence: [T01-S022, S024])
- **值得读/听/看**:
  - 📖 Babylon.js 仓库 + 官方文档：https://github.com/BabylonJS/Babylon.js · https://doc.babylonjs.com/ (evidence: [T01-S022, S023])
  - 📖 Microsoft Open Source「David, founder of Babylon.js」自述：https://medium.com/open-at-microsoft/... (evidence: [T01-S024])
  - 🎙️ Voices of VR #760「Web-Based 3D with Babylon.js & glTF」：https://voicesofvr.com/760-... (evidence: [T01-S024])
- **核心思想关键词**: 全功能引擎、开箱即用、性能（6.0）、glTF 一等支持、社区运营（"不只是写代码还要让它有吸引力"——Rousset）
- **voice_samples**:
  - 同业/开源运营样本（转述）：David Rousset——驱动开源项目"不只是写代码，更是让它有吸引力" (source: T01-S024, 转述)
- **sub_skill_candidate**: `false` — 重要但属工程产品路线；与 mrdoob 形成"全功能引擎 vs 极简内核"光谱，价值在立场对比
- **最近 12 个月动态**: Babylon 持续跟进 WebGPU；与 Three.js 同步进入 WebGPU 时代（两家均已 production WebGPU） (evidence: [T01-S022]，一手)
- **争议/批评**: Babylon vs Three.js 路线之争——批评 Babylon 体积大/抽象重，Three.js 阵营更大更"开放社区"；Babylon 被视为"微软系" (evidence: [T01-S022, S001]，推断)
- **来源**: [Primary] T01-S022；[Secondary] T01-S023/S024
- **可信度自评**: high — 第一方 repo + 官方自述

### 7. Will Eastcott

- **One-liner**: PlayCanvas 创始人 + SuperSplat 作者，既做 web 游戏引擎（WebGL2/WebGPU/WebXR）又把高斯泼溅做成浏览器内开源编辑器——SaaS 协作 + 开源工具两手抓 (evidence: [T01-S033, S034]，一手)
- **核心身份**: PlayCanvas 共同创始人 + CEO（2011 伦敦，2014 引擎 MIT 开源） (evidence: [T01-S033, S035]，一手)
- **代表作品**: PlayCanvas 引擎（云端协作编辑器 + runtime）；**SuperSplat 1.0**（2024+，当前最流行的高斯泼溅编辑器） (evidence: [T01-S033, S034])
- **值得读/听/看**:
  - 📖 PlayCanvas 引擎 + SuperSplat 仓库：https://github.com/playcanvas/engine · https://github.com/playcanvas/supersplat (evidence: [T01-S033, S034])
  - 🎙️ Building the Open Metaverse「Revolutionizing Game Development with Will Eastcott」：https://www.buildingtheopenmetaverse.org/episodes/revolutionizing-game-development (evidence: [T01-S035])
- **核心思想关键词**: web-first 实时图形、云端协作编辑、高斯泼溅工具化、WebGPU、开源 + SaaS 双模式
- **voice_samples**: ⚠️ 暂未找到 ≥ 30 字直接原话片段（podcast 未取文字稿）
- **sub_skill_candidate**: `false` — 工程/产品贡献为主；但 SuperSplat 让他成为"辐射场进入生产工作流"的关键人
- **最近 12 个月动态**: SuperSplat 成为高斯泼溅事实编辑器；与 Spark / mkkellogg 渲染器共同推动 web 端 splat 生态 (evidence: [T01-S034]，一手)
- **争议/批评**: PlayCanvas 商业模式（编辑器闭源 SaaS，引擎开源）vs 纯开源派的张力 (evidence: [T01-S033]，推断)
- **来源**: [Primary] T01-S033/S034/S035
- **可信度自评**: high — 第一方 repo + 长 podcast

### 8. Diego Marcos

- **One-liner**: A-Frame 共同作者（前 Mozilla VR，现 Supermedium），用 HTML 标签民主化 WebXR——"web 已经是 metaverse，我们只需把它 3D 化"是其核心立场 (evidence: [T01-S025, S027]，一手)
- **核心身份**: A-Frame 主开发/维护者；Mozilla 时期推动 WebVR→WebXR 标准；2018 共同创办 Supermedium（VR 浏览器/WebXR showcase） (evidence: [T01-S025, S027]，一手)
- **代表作品**: A-Frame（HTML 写 VR，无需懂 WebGL）；Moon Rider（性能验证作） (evidence: [T01-S025, S027])
- **值得读/听/看**:
  - 🎙️ UploadVR 长访谈（"web 就是 metaverse"立场，多条直接引语）：https://www.uploadvr.com/diego-marcos-interview-webxr/ (evidence: [T01-S027])
  - 🎙️ Voices of VR #1475（WebXR momentum + 开源 AI 集成，2024）：https://voicesofvr.com/1475-... (evidence: [T01-S028])
  - 🎬 同访谈 YouTube 版：https://www.youtube.com/watch?v=wLNpec9gnhc (evidence: [T01-S027])
- **核心思想关键词**: web 即 metaverse、无需许可（no gatekeeping）、链接即分享、web 标准永久性（"今天能跑的 10 年后还能跑"）、赋能既有 web 开发者
- **voice_samples**:
  - 监管/标准立场样本（原话）：「The web is already the metaverse, we just have to make it 3D」「Anything that works today is going to work in 10 years」(source: T01-S027, 原话)
  - 同业/布道样本（原话）：「You don't have to ask for permission and you don't have to pass a curation process」「Our goal was not that much as convincing people that do native to come to the web, but enabling people that are already on the web」(source: T01-S027, 原话)
- **sub_skill_candidate**: `false`（边缘 true）— WebXR/沉浸式展厅若是 focus 则可考虑；A-Frame 的"HTML 声明式 VR"哲学自洽，有充足直接引语
- **最近 12 个月动态**: 2024 Voices of VR 谈 WebXR 势头 + 与开源 AI 集成；A-Frame 仍由 Supermedium（Marcos/Kevin Ngo）+ Google（Don McCurdy）共同维护 (evidence: [T01-S028, S025]，一手)
- **争议/批评**: WebXR 长期"叫好不叫座"——硬件普及慢、Apple 早期对 WebXR 冷淡；批评 A-Frame 抽象在复杂交互下受限 (evidence: [T01-S027]，推断)
- **来源**: [Primary] T01-S025；[Secondary] T01-S026/S027/S028
- **可信度自评**: high — 第一方 repo + 多个长访谈直接引语

### 9. Mark Kellogg（mkkellogg）

- **One-liner**: GaussianSplats3D 作者，把 3D 高斯泼溅（辐射场真实感重建）带进 Three.js 生态——线上展览"真实场景扫描即展厅"路线的关键开源实现 (evidence: [T01-S032]，一手)
- **核心身份**: 开源开发者；Three.js-based 3D Gaussian Splatting 渲染器作者 (evidence: [T01-S032]，一手)
- **代表作品**: GaussianSplats3D（支持 .ply/.splat/.ksplat/.spz，NPM 包 + demo） (evidence: [T01-S032])
- **值得读/听/看**:
  - 📖 GaussianSplats3D 仓库 + 在线 demo：https://github.com/mkkellogg/GaussianSplats3D (evidence: [T01-S032])
- **核心思想关键词**: 高斯泼溅、辐射场、Three.js 集成、压缩格式（.ksplat/.spz）、web 端实时渲染
- **voice_samples**: ⚠️ 暂未找到 ≥ 30 字直接原话片段（贡献为代码，无长访谈）
- **sub_skill_candidate**: `false` — 单一技术贡献者；但在"网格派 vs 辐射场派"光谱中是辐射场一侧的 Three.js 代表
- **最近 12 个月动态**: 与 SuperSplat / Spark 并列 2026 最佳浏览器高斯泼溅查看器；社区讨论是否将 splat 直接并入 Three.js 核心 (evidence: [T01-S032, S037]，一手)
- **争议/批评**: 高斯泼溅 vs 传统网格之争——体积大、编辑难、与 glTF 管线整合尚早（虽 Khronos 2025 已出扩展） (evidence: [T01-S037, S038]，一手)
- **来源**: [Primary] T01-S032；[Reference] T01-S037/S038
- **可信度自评**: medium — 第一方 repo 充分，但无长访谈材料（< 30 min 输出，按规则标 medium）

### 10. Maxime Heckel

- **One-liner**: 创意工程师 + 技术博主，R3F + shader + TSL/WebGPU 最佳实践的高质量写作者——线上展览要做高级视觉效果（焦散/折射/粒子/后处理）几乎必读其博客 (evidence: [T01-S029, S030]，一手)
- **核心身份**: 自由/在职创意前端工程师；blog.maximeheckel.com 作者（深度 3D/shader 系列） (evidence: [T01-S029]，一手)
- **代表作品**: 「The Study of Shaders with React Three Fiber」「Field Guide to TSL and WebGPU」「Caustics/Refraction/Dithering/Moebius」系列 (evidence: [T01-S029, S030])
- **值得读/听/看**:
  - 📖 博客（含交互式 3D 场景讲解）：https://blog.maximeheckel.com/ (evidence: [T01-S029])
  - 📖「Field Guide to TSL and WebGPU」(最新趋势实战)：https://blog.maximeheckel.com/posts/field-guide-to-tsl-and-webgpu/ (evidence: [T01-S030])
- **核心思想关键词**: shader 工艺、R3F、TSL/WebGPU、render targets、stylized post-processing、可交互教学
- **voice_samples**: ⚠️ 暂未找到 ≥ 30 字直接对话原话（博客为技术写作，非对话 register）
- **sub_skill_candidate**: `false` — 优秀技术写作者但偏单一领域（shader/视效）；更适合作 canon/sources 节点
- **最近 12 个月动态**: 紧跟 TSL+WebGPU 出实战指南；持续更新 stylized shader 系列 (evidence: [T01-S030]，一手)
- **争议/批评**: 未找到实质批评
- **来源**: [Primary] T01-S029/S030
- **可信度自评**: high — 第一方深度博客，内容可验证

### 11. SimonDev

- **One-liner**: 20+ 年资深图形工程师（前 Xbox/PS2 图形程序员 + 7 年 Google Chrome 团队），底层图形/性能深挖的硬核教育者——线上展览要"性能优先 + 理解底层"的反面教科书对照 (evidence: [T01-S031]，一手)
- **核心身份**: 资深图形工程师 + YouTube 教育者（21 万+ 订阅）+ 课程作者（simondev.io） (evidence: [T01-S031]，一手)
- **代表作品**: YouTube 深度图形系列（shaping functions / AAA 草地 / 粒子系统 / GPU 驱动效果）；Three.js & GameDev 课程 (evidence: [T01-S031])
- **值得读/听/看**:
  - 📖🎬 个人站 + YouTube 频道：https://simondev.io/ (evidence: [T01-S031])
- **核心思想关键词**: 实时图形底层、性能优化、shader 数学、从零造引擎、GPU 驱动
- **voice_samples**: ⚠️ 暂未找到 ≥ 30 字直接原话文字稿（内容为 YouTube 视频，未抓字幕）
- **sub_skill_candidate**: `false` — 教育者但偏游戏/底层图形，与"展厅业务"focus 略偏；在性能/底层一侧是与 Bruno Simon（应用层）互补的光谱
- **最近 12 个月动态**: 持续产出底层图形/性能深挖视频；课程更新 (evidence: [T01-S031]，一手)
- **争议/批评**: 立场偏"理解底层 > 用框架抽象"，与声明式/R3F 易用派形成隐性张力 (evidence: [T01-S031]，推断)
- **来源**: [Primary] T01-S031
- **可信度自评**: medium — 第一方站点确认，但仅 1 条机械可验证来源（YouTube 字幕未抓）

### 12. Amit Sood

- **One-liner**: Google Arts & Culture 负责人，gigapixel 数字化 + "web 上的博物馆之博物馆"愿景的代表人物——文博线上化/虚拟展览在全球范围最有影响力的产品愿景发声者 (evidence: [T01-S039, S040]，一手)
- **核心身份**: Google Cultural Institute / Arts & Culture 总监；联合 1000+ 博物馆/70+ 国家把文化遗产搬上 web (evidence: [T01-S039, S041]，一手)
- **代表作品**: Google Art Project / Arts & Culture 平台；Art Camera（机器人 gigapixel 相机，全球 20 台分发给美术馆）；ML × 艺术实验 (evidence: [T01-S041])
- **值得读/听/看**:
  - 🎬 TED 2016「Every piece of art you've ever wanted to see -- up close and searchable」：https://www.ted.com/talks/amit_sood_every_piece_of_art_... (evidence: [T01-S039])
  - 🎬 TED 2011「Building a museum of museums on the web」：https://www.ted.com/talks/amit_sood_building_a_museum_of_museums_on_the_web (evidence: [T01-S040])
  - 📖 Art Camera gigapixel 技术原文（Google blog）：https://blog.google/outreach-initiatives/arts-culture/art-camera-cultural-institute/ (evidence: [T01-S041])
- **核心思想关键词**: gigapixel 深缩放、可访问性（人人可近距离看名画）、博物馆之博物馆、ML×文化、数字化民主化
- **voice_samples**: ⚠️ 暂未找到 ≥ 30 字精确文字稿引语（TED 有官方 transcript 可深挖，本轮未逐句取）。立场明确：让任何人不离开椅子就能近距离看遍世界名馆 (source: T01-S039, 转述)
- **sub_skill_candidate**: `false` — 产品/愿景领袖而非开发工程方法论；但在"文博数字展"这条业务线是不可替代的愿景锚点
- **最近 12 个月动态**: Google A&C 持续扩 ML×文化实验（本轮未取到 2025-2026 具体新发言，建议 Phase 4 freshness 复查） (evidence: [T01-S041]，一手但偏旧)
- **争议/批评**: gigapixel/虚拟看展是否削弱实地观展体验、版权与商业化质疑（"From Pixels to Profits"类讨论） (evidence: [T01-S039]，推断)
- **来源**: [Primary] T01-S039/S040/S041
- **可信度自评**: high — 两个 TED 一手 talk + Google 官方技术 blog

### 13. Klaus（krpano）

- **One-liner**: krpano 作者，全景虚拟漫游（360°/720° pano tour）的事实标准引擎——大量国内外虚拟展厅/虚拟看房的全景部分底层是 krpano（Panotour Pro 也以它为核心） (evidence: [T01-S043]，一手 vendor docs)
- **核心身份**: krpano 独立开发者（论坛中以 "Klaus" 身份长期答疑） (evidence: [T01-S043]，一手)
- **代表作品**: krpano viewer + tools（cubefaces/equirect/QTVR，HTML5，嵌音视频） (evidence: [T01-S043])
- **值得读/听/看**:
  - 📖 krpano 官网 + 论坛：https://krpano.com/ (evidence: [T01-S043])
- **核心思想关键词**: 全景漫游、高性能 viewer、跨设备、配置驱动、轻量嵌入
- **voice_samples**: ⚠️ 暂未找到 ≥ 30 字结构化原话（仅论坛技术答疑，非思想性长篇）
- **sub_skill_candidate**: `false` — 工具作者，贡献是软件而非方法论
- **最近 12 个月动态**: ⚠️ 未找到明确 2025-2026 公开动态（krpano 为成熟工具，迭代低调；建议 Phase 4 复查版本/photogrammetry 支持进展） (evidence: [T01-S043]，一手但偏旧)
- **争议/批评**: 全景"伪 3D"（图像拼接而非真三维）vs 真三维重建（Matterport/realsee）的路线之争 (evidence: [T01-S043, S044]，推断)
- **来源**: [Primary] T01-S043
- **可信度自评**: low — 仅 vendor 官网一手，作者真实身份信息稀薄、无长访谈（按规则 < 30 min 材料标 low）

### 14. Matt Bell

- **One-liner**: Matterport 创始人（Stanford + 前 Google 工程师），3D 空间捕获/数字孪生 SaaS 模式的开创者——"扫描真实空间即生成可漫游展厅"的商业派代表，与开源自研派形成对照 (evidence: [T01-S044]，一手 vendor)
- **核心身份**: Matterport 联合创始人（2011，与 David Gausebeck/Michael Beebe）；计算机视觉背景 (evidence: [T01-S044]，一手)
- **代表作品**: Matterport 相机 + 平台（毫米级 3D 重建，全球最大扫描空间数据集 100 亿+ 平方英尺；2021 上市，2025 被 CoStar 收购） (evidence: [T01-S044])
- **值得读/听/看**:
  - 📖 Matterport 官网 + 数字孪生介绍：https://matterport.com/ (evidence: [T01-S044])
- **核心思想关键词**: 数字孪生、3D 空间捕获、SaaS 平台、毫米级重建、空间数据集规模
- **voice_samples**: ⚠️ 暂未找到 ≥ 30 字结构化原话（公开发声多为公司博客/上市材料，非个人思想长篇）
- **sub_skill_candidate**: `false` — 商业创始人，贡献是产品/模式
- **最近 12 个月动态**: 2025 Matterport 被 CoStar 收购（重大归属变动） (evidence: [T01-S044]，一手 vendor)
- **争议/批评**: SaaS 锁定（数据托管在 Matterport 云）vs 自托管开源方案的自主权之争；专有捕获硬件成本 (evidence: [T01-S044]，推断)
- **来源**: [Primary] T01-S044
- **可信度自评**: low — 仅 vendor 官网一手 + 维基类二手（已剔除），无个人长访谈

### 15. 高翔 / 如视 Realsee 团队（surrogate 代理条目）

- **One-liner**: 国内三维重建 + VR 空间商业化代表（众趣科技 CEO 高翔 / 贝壳如视团队），单目深度估计 + SLAM 重建的"国内 SaaS 平台派"——与 Matterport 同路线的本土化对照 (evidence: [T01-S045, S046, S047]，surrogate vendor)
- **核心身份**: 高翔 = 众趣科技创始人/CEO（天津大学三维形态学博士，前华为/Thomson）；如视 = 贝壳旗下三维重建团队 (evidence: [T01-S045]，⚠️ 一手中文报道全部命中黑名单，仅 vendor 官网可用)
- **代表作品**: 众趣 SPACCOM 扫描设备 + Qverse 云平台；如视 Poincaré 手持扫描仪 + Galois（激光雷达 + 单目深度估计，号称 8 百万+ 房源全球最大 VR 房产库） (evidence: [T01-S045])
- **值得读/听/看**:
  - 📖 如视官网（vendor docs）：https://www.realsee.com/ (evidence: [T01-S045])
  - 📖 酷雷曼 / 720云（国内全景营销 SaaS 对照）：https://www.kuleiman.com/ · https://www.720yun.com/ (evidence: [T01-S046, S047])
- **核心思想关键词**: 三维重建、单目深度估计、SLAM、VR 看房、数字孪生、空间数据库规模
- **voice_samples**: ⚠️ 暂未找到合规 ≥ 30 字原话——高翔访谈原文均刊于知乎/搜狐/界面/VR陀螺（黑名单），未收录。立场可从 vendor 官网推断："三维信息是比二维文字/图片更高维的信息载体" (source: T01-S045, 推断)
- **sub_skill_candidate**: `false` — 商业团队，且一手发声渠道几乎全在黑名单，材料合规性不足
- **最近 12 个月动态**: 2025 众趣与中原地产共建房产数字化生态（来源命中黑名单，仅作存在性提示，不引为 claim 证据） (evidence: [T01-S045]，⚠️ 二手不可引)
- **争议/批评**: 国内全景/VR 看房同质化严重、单目深度估计精度争议、SaaS 数据归属 (evidence: [T01-S045]，推断)
- **来源**: [Primary/surrogate] T01-S045/S046/S047（均 vendor 官网）
- **可信度自评**: low — **诚实标注**：国内这条业务线真人一手发声被黑名单（知乎/公众号/CSDN）垄断，仅能用 vendor 官网作 surrogate，**未直接听到 figure 公开发声**，立场多为推断

---

## Phase 2 提炼提示

### 反复出现 ≥ 3 个 figures 都谈到的关键词（候选行业心智模型）

- **WebGPU / TSL 迁移**（出现于 figures: mrdoob / Maxime Heckel / Bruno Simon / Will Eastcott / David Catuhe）——2025-2026 全行业最大技术拐点，所有引擎在重写渲染管线 (evidence: [T01-S005, S030, S010, S033, S022])
- **glTF 作为资产事实标准**（Don McCurdy / Patrick Cozzi / Google model-viewer / David Catuhe）——线上展览模型交换的通用语 (evidence: [T01-S018, S036, S021, S022])
- **性能优先 / 跨设备约束**（Bruno Simon / SimonDev / mrdoob）——"四分之一算力、必须各设备能跑" (evidence: [T01-S010, S031, S001])
- **高斯泼溅 / 辐射场**（mkkellogg / Will Eastcott / Khronos）——真实场景"扫描即展厅"新范式，2025 Khronos 已出 glTF 扩展 (evidence: [T01-S032, S034, S038])
- **开放 web / 无需许可**（Diego Marcos / Patrick Cozzi / mrdoob）——链接即分享、标准永久性、反平台锁定 (evidence: [T01-S027, S036, S001])
- **可访问性 / 民主化**（Bruno Simon / Diego Marcos / Amit Sood / Google model-viewer）——降低门槛让更多人做/看 3D (evidence: [T01-S008, S027, S039, S021])

### 显著分歧 / 流派分裂（线上展览开发的"立场光谱"——figures 的主要价值所在）

1. **自研开源派 vs SaaS 平台派**：mrdoob/Bruno Simon/Paul Henschel/SimonDev（手写代码、完全掌控） vs Matterport(Matt Bell)/如视/众趣/酷雷曼（买设备买平台、快但锁定） (evidence: [T01-S001, S044, S045])
2. **命令式 vanilla vs 声明式组件化**：Bruno Simon/SimonDev（vanilla Three.js，极致性能/掌控） vs Paul Henschel/Maxime Heckel（R3F，React 组件化/可组合） (evidence: [T01-S007, S012, S031])
3. **极简内核 vs 全功能引擎**：mrdoob 的 Three.js（最小封装跟标准） vs David Catuhe 的 Babylon.js（开箱即用全栈） vs Will Eastcott 的 PlayCanvas（云端协作 SaaS+开源引擎） (evidence: [T01-S001, S022, S033])
4. **网格几何派 vs 辐射场/高斯泼溅派**：传统 glTF 网格（McCurdy/Cozzi 标准体系） vs 高斯泼溅真实感重建（mkkellogg/Eastcott SuperSplat），2025 起两派经 Khronos 扩展开始收敛 (evidence: [T01-S018, S032, S038])
5. **全景"伪 3D"派 vs 真三维重建派**：krpano（图像拼接全景漫游，轻量） vs Matterport/如视（真三维点云重建，重但可量测） (evidence: [T01-S043, S044, S045])
6. **沉浸 WebXR 派 vs 普通 web 3D 派**：Diego Marcos（A-Frame，赌 VR/沉浸） vs 主流 Three.js/R3F（屏幕内 3D 优先，WebXR 为可选） (evidence: [T01-S025, S012])
7. **性能优先 vs 视觉/沉浸优先**：SimonDev/mrdoob（底层性能） vs Bruno Simon/Maxime Heckel（视觉效果/shader 工艺，但 Bruno 同时强调性能约束，处于中间） (evidence: [T01-S031, S029, S010])

### 冷僻领域信号（诚实评估）

- **总 figure 数 < 10？** ❌ 否 — 找到 14 个真 figure（+1 surrogate 代理条目），floor 15 基本达标
- **多数 figure 长访谈材料 < 30 min？** ⚠️ 部分 — mrdoob/Bruno Simon/Paul Henschel/Diego Marcos/Catuhe/Eastcott/Cozzi/Amit Sood 有充足长材料（8 人）；mkkellogg/Maxime Heckel/SimonDev 偏文字/视频无长访谈；krpano/Matt Bell/国内团队材料薄
- **标 "可信度 low" 比例 > 30%？** ⚠️ 临界 — 4/15 标 low（krpano / Matt Bell / 国内团队 / 部分），约 27%，集中在**商业平台 + 文博业务侧**，**开发工程核心侧（库作者/教育者）几乎全 high**
- **结论**：figures 维度对"**开发工程**"focus **充分丰满**（库作者 + 教育者一侧质量极高、第一方材料丰富）；但对"**展览业务 / 文博策展 / 国内商业平台**"一侧**偏薄**（真人一手发声稀缺，中文优质源被黑名单垄断，多靠 vendor docs/TED surrogate）。

### Phase 2 权重建议（执行 STEP 1 指令的诚实判断）

- **figures 不需压权重**——开发工程侧 figure 厚且高质，可正常承载方法论（尤其 Bruno Simon 教学法 / mrdoob 库设计 / Paul Henschel 声明式范式三人可深蒸）
- **但 figures 的最大价值是"立场光谱"**（上面 7 组分歧），而非单一权威方法论——Phase 2 应把这些光谱做成 SKILL.md 的"技术选型决策框架"骨架
- **业务/文博/国内平台侧**：建议权重压向 **tools（引擎/格式/平台对比）+ canon（glTF/WebGPU 规范、Three.js 文档）+ workflows（建模→优化→部署管线）**，figures 在这一侧仅作立场参考
- **缺口（移交 Phase 1.5 / 其他 track 补）**：
  1. 国内开发者 figure 几乎为零（合规一手源被黑名单垄断）——建议 tools track 直接抓 vendor 官网技术文档补
  2. 文博/策展"内容侧"思想家缺失（本轮聚焦开发工程，未深挖 IIIF 核心人/数字策展人）——若 focus 含策展可补
  3. WebXR/沉浸侧仅 Diego Marcos 一人撑——若 focus 重 VR 展厅需补 Kevin Ngo（A-Frame）/ Brandon Jones（WebXR 规范）等
  4. voice_samples 整体偏薄：仅 Bruno Simon / Diego Marcos 有充足直接引语；其余多为推断/转述——Phase 4 voice check 会因此对多数 figure 降 voice_confidence
