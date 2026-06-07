# Track 03 — Workflows / SOPs：Web 线上展览 / 虚拟展厅开发

> Research date: 2026-06-06 · locale=zh-CN（输出中文，canon 全球）· Wave 3 OPUS subagent
> 重点：开发工程。端到端制作 SOP + 两条主路线对比 + 真3D/全景差异 + **性能优化 playbook（命门）** + 跨端 QA 环 + 入门 vs 资深 + 近 12 月变化。
> Seed 复用：Track 02（工具/资产管线）、Track 04（glTF/性能/WebXR 规范）、Track 01（Bruno Simon/Don McCurdy 方法论）。evidence 跨轨引用 `T0x-Sxxx`。
> **时效硬规矩**：每个 workflow 卡有 `last_updated` + 近期变化字段 + 触发事件类型。

## Source Manifest

| source_id | url | bucket | last_checked | author/host | one-line note |
|-----------|-----|--------|--------------|-------------|---------------|
| T03-S001 | https://www.utsubo.com/blog/threejs-best-practices-100-tips | verified_primary | 2026-06-06 | Utsubo | 100 条 three.js 生产实践（draw call/LOD/KTX2/dispose/监控数值） |
| T03-S002 | https://www.utsubo.com/blog/webgpu-threejs-migration-guide | verified_primary | 2026-06-06 | Utsubo | WebGL→WebGPU 迁移 step-by-step + 何时迁 + 工期 + 坑 |
| T03-S003 | https://gltf-transform.dev/ | verified_primary | 2026-06-06 | Don McCurdy | glTF-Transform 文档：optimize 一键 + 各 individual 命令/flag（官方一手，verifier 默认 secondary 已上调） |
| T03-S004 | https://developer.mozilla.org/en-US/docs/Web/API/WebGL_API/WebGL_best_practices | verified_primary | 2026-06-06 | MDN | WebGL 最佳实践：context loss/fallback/precision/MAX_TEXTURE_SIZE/dPR（跨端 QA 命门） |
| T03-S005 | https://modelviewer.dev/ | verified_primary | 2026-06-06 | Google | <model-viewer> 官方站：低代码嵌单展品 SOP（官方一手，已上调） |
| T03-S006 | https://modelviewer.dev/examples/annotations/index.html | verified_primary | 2026-06-06 | Google | model-viewer 注解/热点官方示例（slot=hotspot-* / data-position / data-normal / data-surface） |
| T03-S007 | https://www.khronos.org/news/press/gltf-gaussian-splatting-press-release | verified_primary | 2026-06-06 | Khronos | glTF 高斯泼溅扩展新闻稿（官方一手，已上调） |
| T03-S008 | https://github.com/KhronosGroup/glTF/blob/main/extensions/2.0/Khronos/KHR_gaussian_splatting/README.md | verified_primary | 2026-06-06 | Khronos | KHR_gaussian_splatting 规范 README — **Status: Release Candidate**（一手，纠正"已正式发布"） |
| T03-S009 | https://www.khronos.org/blog/have-gaussian-splats-arrived-in-the-standardization-sweet-spot | verified_primary | 2026-06-06 | Khronos | 高斯泼溅标准化分析 + SPZ 提案 + 捕获到 web 链路 |
| T03-S010 | https://www.thefuture3d.com/blog/state-of-gaussian-splatting-2026/ | verified_primary | 2026-06-06 | The Future 3D | 2026 高斯泼溅工具/格式现状综述（注：分析型博客，二手质量，verifier 给 primary） |
| T03-S011 | https://blog.bentley.com/insights/why-gaussian-splats-could-change-infrastructure/ | verified_primary | 2026-06-06 | Bentley (Don McCurdy 所在) | 开放标准视角看 GS 进 glTF 的意义 |
| T03-S012 | https://www.agisoftmetashape.com/how-to-reduce-model-size-in-agisoft-metashape-without-losing-detail/ | verified_primary | 2026-06-06 | Agisoft (vendor) | 摄影测量减面/出 web glTF（vendor 一手） |
| T03-S013 | https://www.thegnomonworkshop.com/tutorials/complete-photogrammetry-workflow | secondary | 2026-06-06 | Gnomon Workshop | 完整摄影测量管线教程（solve→retopo→bake，二手） |
| T03-S014 | https://github.com/playcanvas/supersplat | verified_primary | 2026-06-06 | Will Eastcott / PlayCanvas | SuperSplat 浏览器内高斯泼溅编辑器（清洗/裁剪/压缩） |

> **bucket 说明**：沿用 Track 02/04 约定 —— 官方文档/规范/GitHub repo/MDN/web 工程博客标 `verified_primary`；其中 modelviewer.dev / gltf-transform.dev / khronos.org/news 经 `source_verifier.py` 默认 secondary，但均为**第一方官方文档/规范/新闻稿**，按 brief bucket 定义上调 verified_primary 并在 note 标注。SaaS/工具 vendor 文档（agisoft）按 surrogate policy 计 vendor 一手 = verified_primary。thefuture3d.com 经 verifier 给 verified_primary，但实为**分析型综述（二手质量）**，引用时降权、不作单源 mental model 依据。**黑名单（知乎/公众号/百度百科/CSDN/简书/掘金；G2/Capterra）全程未收录**。Track 03 自有新源 14 个 + 大量复用 T01/T02/T04 seed。

---

## 总览（按 decay risk 分组）

### High decay (12-month-class) — 1 个
| Workflow | Trigger | Output | Last_updated | 资深差异 |
|---------|---------|--------|-------------|---------|
| W7 高斯泼溅「实景扫描即展厅」管线 | 要photoreal实景且不接受全景平面感 | 可web漫游的splat场景(.ply/.spz/.sog) | 2026-02 | skip手工建模/optimize清洗压缩/add fallback |

### Medium decay — 3 个
| Workflow | Trigger | Output | Last_updated | 资深差异 |
|---------|---------|--------|-------------|---------|
| W1 端到端线上展览制作（自研真3D） | 客户要品牌级沉浸展厅 | 上线的可漫游3D展厅 | 2026-06 | skip过早后期/optimize资产管线/add性能预算与埋点 |
| W4 性能优化 playbook（命门） | 首屏慢/移动端崩/掉帧 | 达标的首屏+稳定帧率+不崩 | 2026-06 | skip盲目优化/optimize按瓶颈下手/add显存预算+监控 |
| W8 WebGL→WebGPU/TSL 迁移 | 撞性能墙/新项目/大量粒子compute | WebGPU渲染+自动WebGL2 fallback | 2026-01 | skip存量流畅项目/optimize先audit/add跨浏览器(Safari)测 |

### Low decay — 4 个
| Workflow | Trigger | Output | Last_updated | 资深差异 |
|---------|---------|--------|-------------|---------|
| W2 SaaS 平台快速搭建（众趣/酷雷曼/Matterport） | 工期紧/预算低/无3D团队 | 上线的全景或数字孪生展厅 | 2026-06 | skip自写代码/optimize模板复用/add锁定与导出尽调 |
| W3 全景720 漫游制作 | 实景漫游、不需真3D交互 | 多全景串联+热点tour | 2026-06 | skip真3D建模/optimize拍摄一次到位/add补光与拼接质检 |
| W5 单展品 model-viewer 嵌入 | 详情页嵌一个可旋转+AR展品 | 一行HTML的3D/AR展品 | 2026-06 | skip引整套引擎/optimize poster+lazy/add USDZ兜底 |
| W6 跨端兼容 / 上线验收 QA 环 | 展厅"能不能上线"判定 | 通过验收判据的可发布版本 | 2026-06 | skip只测自己机器/optimize清单化/add低端真机+context loss |

> 7 个 workflow（W1-W8 中 W7 为 high）。资产优化（glTF-Transform）作为 **跨 W1/W2/W3/W5/W7 的共同子步骤**，在 W4 playbook 详述，不单列为 workflow（它是 micro-pipeline / 性能节的核心，按边界判定属"贯穿步骤"）。

---

## Workflow 详细卡片

### 1. 端到端线上展览制作（自研真 3D 全流程）

- **One-liner**: 从「客户要个沉浸式线上展厅」到「一个 CDN 上能漫游、能交互、移动端不崩的 3D web 展厅」的完整闭环——这是自研路线的主干 SOP。
- **Trigger**: 客户/项目方要品牌级独特体验、深度交互、长期可控或要出海；全景/SaaS 满足不了（业务触发）(evidence: [T02-S001, T02-S003])
- **Output**: 部署上线、跨端可访问的真 3D 虚拟展厅（含资产、场景、交互、埋点）
- **入门 SOP（minimum viable steps）**:
  1. **需求 / 策展定位**：明确「要不要自由走动 / 绕物 / 拾取交互」（这一刀决定真 3D vs 全景，是整条管线的总开关）；定目标设备（移动占比？低端机？）、首屏预算、转化目标 (evidence: [T04-S016, T02-S016])
     - **跳过后果**：方向错——把全景当真 3D 卖，或为只需看图的需求上重型引擎，验收必翻车 (evidence: [T02-S016])
  2. **内容采集**：按展品性质选 —— 数字建模（Blender/DCC）/ 全景拍摄 / 3D 扫描·摄影测量（Metashape/RealityCapture）/ 高斯泼溅（见 W7）。文物类要对齐采集合规 (evidence: [T03-S012, T03-S013, T04-S021])
     - **跳过后果**：无内容无展厅；采集质量不足后期补不回（贴图糊、网格脏）
  3. **资产优化（命门，详见 W4 §资产管线）**：源模型先在 DCC/MeshLab 减面到 web 量级（摄影测量常减到 100k–500k 面），再走 glTF-Transform `optimize`：Draco/Meshopt 压几何 + KTX2 压纹理 + dedup/weld/prune (evidence: [T03-S001, T03-S003, T03-S012])
     - **跳过后果**：50MB 的 GLTF 无论渲染代码多优都毁掉首屏，加载劝退 (evidence: [T03-S001, T02-S032])
  4. **场景搭建**：React/Next 站内 → R3F + drei（gltfjsx 把 GLB 转 JSX）；非 React/要底层控制 → 裸 Three.js；要内建物理/编辑器 → Babylon/PlayCanvas。布光、相机、环境贴图、PBR 材质 (evidence: [T02-S003, T02-S001, T04-S005])
     - **跳过后果**：没有可渲染场景
  5. **交互 / 动线 / 热点 / 讲解**：第一人称或轨道相机控制；动线引导（视角序列/路径）；热点（图文/语音/跳转）；语音导览 (evidence: [T04-S020 概念, T02-S024])
     - **跳过后果**：用户进场即迷路，展品不可读，沦为「能转的空房子」
  6. **性能调优（命门，整套见 W4）**：draw call / 显存 / 移动端 / 首屏分级加载 / 降级链 (evidence: [T03-S001, T03-S004])
     - **跳过后果**：移动端崩 / 掉帧 / 白屏，上不了线
  7. **部署**：资产上 CDN；流式 / 分级加载；跨端兼容（WebGL2 fallback、iOS 兜底）(evidence: [T03-S001, T03-S004])
     - **跳过后果**：加载慢 / 部分设备白屏
  8. **数据埋点 · 线索转化**：停留/点击/热点曝光埋点；表单/预约/带看等转化钩子（营销型展厅核心 KPI）(evidence: [T02-S027])
     - **跳过后果**：花大钱做的展厅无法证明 ROI，无线索沉淀
- **资深路径（差异点）**：
  - **skip**：资深人**跳过早期后期/视效堆叠**——先把「资产能加载 + 场景能跑 + 移动端不崩」拉通（灰模 + 占位），最后才加 shader/后期；不在性能没兜住前做炫光焦散 (evidence: [T01-S010] Bruno Simon「先性能、四分之一算力、各设备能跑」)
  - **optimize**：把**资产优化做成 CI 自动化**（glTF-Transform `@gltf-transform/functions` 脚本进流水线），而非手工逐个压；gltfjsx 自动生成组件 (evidence: [T03-S003, T02-S009])
  - **add**：开工即**先立性能预算**（draw call <100 / 首屏体积上限 / 目标显存）再选技术栈；从 day 1 加 `renderer.info` + stats-gl 监控；埋点设计前置 (evidence: [T03-S001])
- **近期变化（近 12 个月）**：
  - 2025-09 起（r171 + Safari 26 补齐），新自研项目可直接选 `three/webgpu`（自动 fallback WebGL2），渲染后端默认值在迁移中 (evidence: [T03-S002], 触发：标准/工具更新)
  - 2026-02 起，photoreal 采集多一条高斯泼溅支线（见 W7），部分实景展厅从「摄影测量 mesh」转向「splat」(evidence: [T03-S007], 触发：标准更新)
- **典型耗时**：入门 SOP 2–6 周（单展厅）；资深路径 1–3 周（有 starter/管线复用，但性能/埋点更扎实）
- **关键工具**：Three.js / R3F+drei（必备）、glTF-Transform（必备）、Draco/KTX2/Meshopt（必备）、Babylon/PlayCanvas（场景特化）(evidence: [T02-S001, S003, S008])
- **关键人物**：Bruno Simon（Three.js Journey，Advanced/性能/R3F 章即此管线教学；"边做边学 + 性能优先"）；Don McCurdy（资产管线权威）(evidence: [T01-S008, T01-S018])
- **常见失败模式**：
  - 大模型不压缩直接上 → 首屏崩：必须先 DCC 减面 + glTF-Transform optimize，别把 50MB GLTF 丢上线 (evidence: [T03-S001])
  - 把展厅当普通网页写、不立性能预算 → 后期推倒重来：day 1 定 draw call/首屏/显存预算再选栈 (evidence: [T03-S001])
  - 动线/热点缺失 → 用户迷路：先用灰模走通动线再美化 (evidence: [T02-S024])
  - 忘了埋点 → 无法证明 ROI：转化钩子和埋点设计要前置 (evidence: [T02-S027])
- **来源**：[Primary] T03-S001/S003；[Reference] T01-S008/S010/S018；[seed] T02-S001/S003
- **Last_updated**: 2026-06-06
- **Decay risk**: medium（栈与渲染后端 12–24 月仍在演进，但「采集→优化→搭建→调优→部署」骨架稳定）

---

### 2. SaaS 平台快速搭建（众趣 / 酷雷曼 / Matterport / Artsteps）

- **One-liner**: 从「工期紧、没 3D 团队」到「几天内上线一个全景或数字孪生展厅」——买平台换速度的主干 SOP。
- **Trigger**: 工期紧 / 预算低 / 无 3D 团队 / 定制度低；国内要走微信·抖音小程序分发 + 营销转化（业务触发）(evidence: [T02-S027, T02-S024])
- **Output**: 平台托管（或私有部署）的全景/数字孪生展厅，自带热点/导览/分发
- **入门 SOP**:
  1. **选平台 + 尽调锁定**：海外艺术教育→Artsteps（免费 no-code）；国内营销→众趣/酷雷曼/720云；高保真数字孪生→Matterport。**先查能否导出 / 二开 / 私有部署**（Matterport/Kuula 云端独占不可导出）(evidence: [T02-S024, S027, S020, S026])
     - **跳过后果**：上线后才发现数据导不出 / 二开做不了 / 被平台锁定，迁移成本极高 (evidence: [T02-S022, S026])
  2. **内容采集**：平台自有设备（Matterport Pro / 众趣 SPACCOM）或第三方全景相机拍摄；或导入已有 3D 数据 (evidence: [T02-S020, S027])
     - **跳过后果**：无空间数据，平台空壳
  3. **平台内搭建**：选模板 / 摆墙·展柜（Artsteps）；上传图文/视频/音频/3D；自动生成漫游 (evidence: [T02-S024])
     - **跳过后果**：无展厅结构
  4. **加热点 / 导览 / 转化工具**：图文热点、语音导览、楼层图、空间测量；营销表单/直播/VR 带看 (evidence: [T02-S027, S024])
     - **跳过后果**：只是个能转的空间，无内容深度、无线索
  5. **发布 / 嵌入 / 分发**：站内发布或 iframe 嵌入官网；国内绑小程序生态 (evidence: [T02-S024, S029])
     - **跳过后果**：做完没人看，触达为零
- **资深路径（差异点）**：
  - **skip**：完全**跳过写代码**（这是选 SaaS 的全部意义）；不纠结像素级定制
  - **optimize**：建模板库 + 拍摄 SOP 复用，批量出活；用可二开档（Matterport Showcase SDK / 酷雷曼 OEM）做有限定制 (evidence: [T02-S021, S028])
  - **add**：资深人**合同/选型阶段就把"导出权 + 数据归属 + SDK 生产授权"写死**——Matterport SDK 生产用需付费订阅、free 仅 sandbox (evidence: [T02-S022, S026])
- **近期变化（近 12 个月）**：2026 多家 SaaS 内置「AI 生成虚拟展厅」（文生/图生），进一步降搭建门槛（单源 vendor 宣称，可信度 low）(evidence: [T02-S027], 触发：新工具/AI)
- **典型耗时**：入门 1–5 天（含拍摄）；资深路径 数小时–2 天（模板复用）
- **关键工具**：众趣 Qverse / 酷雷曼 / 720云 / Matterport / Artsteps / 3DVista（场景特化，多为 vendor）(evidence: [T02-S027, S028, S029, S020, S024, S026])
- **关键人物**：Matt Bell（Matterport，数字孪生 SaaS 模式开创者）(evidence: [T01-S044])
- **常见失败模式**：
  - 选了云端独占平台才发现导不出 → 永久锁定：选型即查导出能力，要自托管选 3DVista，要二开选可 OEM 的 (evidence: [T02-S026, S028])
  - 以为 SDK 免费能商用 → 上线被卡：Matterport SDK 生产用需付费订阅，先确认授权档 (evidence: [T02-S022])
  - 只发布不分发 → 零触达：国内必绑小程序生态，海外靠链接/嵌入 (evidence: [T02-S029])
- **来源**：[seed/Primary] T02-S020/S024/S027；[Reference] T01-S044
- **Last_updated**: 2026-06-06
- **Decay risk**: low（SaaS 流程稳态，最近变化是 2026 AI 生成功能；锁定/导出这类坑多年不变）

---

### 3. 全景 720 漫游制作

- **One-liner**: 从「要实景漫游但不需要真 3D 交互」到「多张全景串联成带热点的虚拟游」——最低成本主力路线。
- **Trigger**: 实景展馆/走廊漫游，只需站点跳转看图 + 偶尔热点；预算/工期紧（业务触发）(evidence: [T02-S016, S017])
- **Output**: 多全景节点串联的 tour（含热点跳转、可选楼层图/语音/360 视频）
- **入门 SOP**:
  1. **拍摄规划 + 全景采集**：定点位（节点密度决定漫游连贯度）；全景相机/鱼眼拼接拍 equirect；保证曝光一致 (evidence: [T02-S016, S019])
     - **跳过后果**：点位太疏跳转跳跃感强；曝光不一拼接处明显接缝
  2. **拼接 / 后处理**：HDR、去三脚架、补光、统一白平衡 (evidence: [T03-S013 类比])
     - **跳过后果**：画面脏、三脚架穿帮、明暗跳变
  3. **搭 viewer + 串联**：开源选 Pannellum（最轻 21KB）/ Photo Sphere Viewer（要视频/VR/楼层图/陀螺仪选它）；商业选 krpano；节点间建跳转 (evidence: [T02-S016, S017, S019])
     - **跳过后果**：单张全景不成「游」，无法在空间中移动
  4. **加热点 / 导览 / 楼层图**：图文/音频热点、平面图定位、语音讲解 (evidence: [T02-S016])
     - **跳过后果**：展品无说明，导览价值低
  5. **发布 / 嵌入**：自托管或平台；移动端手势/陀螺仪验收 (evidence: [T02-S016, S017])
     - **跳过后果**：移动端体验差（PSV 移动支持最好，Pannellum 手势弱）
- **资深路径（差异点）**：
  - **skip**：完全跳过真 3D 建模/优化管线（全景本质是图，不碰 mesh）
  - **optimize**：拍摄一次到位（点位 + 曝光 + HDR 现场定），减少返工；大图用瓦片化（Marzipano/krpano）保性能 (evidence: [T02-S018, S019])
  - **add**：补光与拼接质检环节（接缝、鬼影、天顶/地补）——初学者常忽略 (evidence: [T03-S013])
- **近期变化（近 12 个月）**：无重大变化（全景路线稳态）。增量是高斯泼溅在「要更强空间感」时开始替代部分全景（见 W7），但 720 因极低成本仍是主力 (evidence: [T03-S010], 触发：新技术，渐进)
- **典型耗时**：入门 1–3 天；资深 数小时（拍摄一次到位 + viewer 模板）
- **关键工具**：Pannellum / Photo Sphere Viewer / Marzipano / krpano（必备-全景）(evidence: [T02-S016, S017, S018, S019])
- **关键人物**：Klaus（krpano，全景事实标准引擎作者）(evidence: [T01-S043])
- **常见失败模式**：
  - 点位太疏 → 漫游跳跃：按空间复杂度加密节点，转角/门口必设点 (evidence: [T02-S016])
  - 曝光不一致 → 接缝/明暗跳：现场统一白平衡 + 后期 HDR (evidence: [T03-S013])
  - 把全景当真 3D 卖 → 验收翻车：合同明确"全景=看图跳点，不能走动/绕物/交互" (evidence: [T02-S016])
- **来源**：[seed/Primary] T02-S016/S017/S019；[Secondary] T03-S013；[Reference] T01-S043
- **Last_updated**: 2026-06-06
- **Decay risk**: low（成熟稳态路线）

---

### 4. 性能优化 Playbook（命门 — 单列）

- **One-liner**: 从「首屏慢 / 移动端崩 / 掉帧」到「首屏达标 + 帧率稳定 + 各端不崩」——这是线上展览的生死线，几乎所有项目的真正难点。
- **Trigger**: 首屏加载劝退 / 移动端闪退或白屏 / 帧率掉到卡顿 / 显存爆（技术触发）(evidence: [T03-S001, T03-S004])
- **Output**: draw call 受控、显存在预算内、首屏分级加载、低端机有降级、监控在位的可发布版本
- **入门 SOP（按瓶颈分层）**:
  1. **① 资产管线压缩（第一刀，收益最大）**：
     - 几何：`gltf-transform draco model.glb out.glb --method edgebreaker`（降 90–95%）；有动画/morph 或在意解码 CPU → `gltf-transform meshopt --level medium` (evidence: [T03-S001, T03-S003])
     - 纹理：转 KTX2/Basis（**GPU 上保持压缩，省 ~10x 显存**）；法线/hero 贴图用 UASTC（`--slots "{normalTexture,...}" --level 4 --rdo`），环境/次要用 ETC1S（`--quality 255`）；合并 roughness/AO/metallic 进单图 (evidence: [T03-S001, T03-S003, T02-S011])
     - 一键：`gltf-transform optimize in.glb out.glb --texture-compress ktx2 --compress draco`；客户端配 `dracoLoader.setDecoderPath` + `ktx2Loader.setTranscoderPath` (evidence: [T03-S001, T03-S003])
     - **跳过后果**：单 4K 贴图 = 64MB+ 显存；50MB GLTF 毁首屏 (evidence: [T03-S001])
  2. **② draw call / instancing / 合批**：目标 **<100 draw calls/帧** 才稳 60fps；重复物体用 `InstancedMesh`（1000 棵树 1000→1 call；实测案例 9000→300）；异几何同材质用 `BatchedMesh`；静态合并 `mergeGeometries`；共享材质 + 纹理 atlas (evidence: [T03-S001])
     - **跳过后果**：draw call 失控，CPU 瓶颈，帧率崩
  3. **③ LOD / frustum culling**：按距离切精度（drei `<Detailed distances={[0,50,100]}>`，大场景提帧 30–40%）；保证 bounding box 准确让视锥剔除生效 (evidence: [T03-S001])
     - **跳过后果**：远处高模白烧 GPU；剔除失效画看不见的东西
  4. **④ 首屏分级加载**：先加载 `low.glb` 立即可交互，后台换 `high.glb`；`<link rel="preload" as="fetch">` 预载关键资产；R3F `<Suspense>` + 占位低模盒；按相机邻近度流式加载分区；Web Worker 卸载重活；代码分割 loader (evidence: [T03-S001])
     - **跳过后果**：白屏等全量加载，用户流失
  5. **⑤ 移动端显存 / pixelRatio**：移动 `pixelRatio` 限到 1（或半分辨率渲染再上采样可翻倍帧率）；阴影贴图移动 512–1024、桌面 1024–2048；mediump（移动快 2x）；varying < 3；避免分支用 `mix()/step()` (evidence: [T03-S001, T03-S004])
     - **跳过后果**：移动端显存爆 / 闪退 / 卡死
  6. **⑥ 显存释放 / 防泄漏**：用完 `geometry/material/texture/renderTarget.dispose()`；GLTF 的 ImageBitmap 要 `texture.source.data.close?.()`；多展厅切换用对象池 + 卸载 (evidence: [T03-S001])
     - **跳过后果**：多展厅切换显存只增不减，最终崩
  7. **⑦ WebGL 降级链**：`three/webgpu` 入口自动回退 WebGL2；手搓渲染要 `canvas.getContext('webgl2')||getContext('webgl')` 判空兜底；扩展按可选优雅降级 (evidence: [T03-S002, T03-S004])
     - **跳过后果**：~5% 不支持的设备 / 老机白屏
  8. **⑧ 监控（draw call / FPS / 帧时间）**：`renderer.info.render.calls / .triangles`、`renderer.info.memory.geometries/.textures`（数值只增=泄漏）；stats-gl 看 FPS/CPU/GPU（兼容 WebGL+WebGPU）；Spector.js 抓帧逐 draw call；Chrome Performance 看帧时间/GC (evidence: [T03-S001])
     - **跳过后果**：盲飞，不知道瓶颈在哪、有没有泄漏
- **资深路径（差异点）**：
  - **skip**：资深人**跳过盲目全局优化**——先用 `renderer.info` + Spector.js **定位真瓶颈**（是 draw call？显存？首屏体积？fill rate？），只打那一处，不在非瓶颈处过度优化 (evidence: [T03-S001])
  - **optimize**：把压缩管线 CI 化；按 canon「按瓶颈选压缩」——**下载瓶颈用 Draco、渲染瓶颈用 Meshopt、显存瓶颈用 KTX2**（这是 ≥3 源共识）(evidence: [T04-S011, S013, S012, T03-S003])
  - **add**：资深人**先算预算后建场景**——按 `窗口像素 × 每像素 VRAM 预算` 估显存上限，定 draw call 预算，再反推可用面数/贴图数；从 day 1 挂监控 (evidence: [T03-S004, T03-S001])
- **近期变化（近 12 个月）**：2025-09 起 WebGPU compute shader 可把粒子/实例定位/后期搬上 GPU（WebGL 时代要 FBO/GPGPU 绕路），50k+ 粒子级场景性能天花板抬高；stats-gl 已统一支持 WebGL+WebGPU 监控 (evidence: [T03-S002, T02-S031], 触发：标准/工具更新)
- **典型耗时**：入门 SOP 数天（逐层套）；资深路径 数小时–1 天（直击瓶颈）
- **关键工具**：glTF-Transform / Draco / KTX2 / Meshopt（必备）；stats-gl / Spector.js / renderer.info（监控）；three-mesh-bvh（raycast 加速）(evidence: [T03-S001, S003])
- **关键人物**：Bruno Simon（"四分之一算力、各设备能跑"性能哲学）；SimonDev（底层性能深挖）；Don McCurdy（资产管线）(evidence: [T01-S010, S031, S018])
- **常见失败模式**（CLI 化友好写法）：
  - 不压缩直接上 50MB GLTF → 首屏崩：上线前必跑 `gltf-transform optimize`，体积过阈值（如 >5–10MB）卡门 (evidence: [T03-S001])
  - 移动端纹理用 JPEG/PNG → 显存爆闪退：所有贴图转 KTX2 + mipmap，移动 pixelRatio=1 (evidence: [T03-S001, T03-S004])
  - 重复物体不用 InstancedMesh → draw call 破千：盘点重复展品/道具，>100 draw call 必合批 (evidence: [T03-S001])
  - 不 dispose → 多展厅泄漏：每次切场景跑 dispose + 查 `renderer.info.memory` 是否回落 (evidence: [T03-S001])
  - 不挂监控盲优化 → 白费力：先 Spector.js/renderer.info 定位再动手 (evidence: [T03-S001])
- **来源**：[Primary] T03-S001/S003/S004；[Reference] T01-S010/S018/S031；[canon] T04-S011/S012/S013/S016
- **Last_updated**: 2026-06-06
- **Decay risk**: medium（核心原则（压缩/draw call/显存）稳态 low，但 WebGPU compute 带来的新优化路径 12–24 月演进）

---

### 5. 单展品 model-viewer 嵌入

- **One-liner**: 从「详情页要嵌一个可旋转 + AR 的展品」到「一行 HTML 的 3D/AR 展品」——零 3D 编程的最快出活路线。
- **Trigger**: 电商/展厅详情页只需嵌单个展品 360 看 + 移动端 AR「放到我的空间」；不想为一个模型引整套引擎（业务触发）(evidence: [T02-S006, S007])
- **Output**: 一个 `<model-viewer>` 标签，桌面可旋转、移动端可 AR、带热点说明
- **入门 SOP**:
  1. **准备资产**：模型转 GLB + 走 glTF-Transform 压缩；iOS AR 额外出 USDZ（`ios-src`）(evidence: [T02-S007, T03-S003])
     - **跳过后果**：模型过大首屏慢；无 USDZ → iOS AR 不可用
  2. **嵌标签 + 基础属性**：`<model-viewer src poster camera-controls auto-rotate environment-image shadow-intensity exposure>`；`poster` 给首屏占位图、`loading="lazy"` + `reveal` 控制首屏性能 (evidence: [T03-S005, T03-S006])
     - **跳过后果**：无交互/无光照/首屏空白
  3. **配 AR**：`ar ar-modes="webxr scene-viewer quick-look"`——Android 走 Scene Viewer、iOS 走 Quick Look（USDZ）(evidence: [T03-S006, T02-S007])
     - **跳过后果**：移动端「放进现实」失效
  4. **加热点 / 注解**：子元素 `slot` 以 `hotspot` 开头即为热点，配 `data-position` + `data-normal`（或动画模型用 `data-surface`）；编辑器里点选生成坐标，或 `updateHotspot({name,position,normal})` 动态更新 (evidence: [T03-S006])
     - **跳过后果**：展品无图文说明点
  5. **嵌入页面 / 验收**：iframe 或直接组件；移动端 AR 真机测 (evidence: [T03-S005])
     - **跳过后果**：跨端 AR 不可用未被发现
- **资深路径（差异点）**：
  - **skip**：跳过引整套 Three.js/引擎——单展品别上重型栈，model-viewer 足够 (evidence: [T02-S006])
  - **optimize**：用 `poster` + `loading="lazy"` + `reveal="interaction"` 把首屏成本降到最低；模型预压缩 (evidence: [T03-S005, T03-S001])
  - **add**：资深人**必出 USDZ 兜底 iOS**（iOS immersive WebXR 弱，AR 走 Quick Look），并用官方编辑器拖热点拿精确坐标而非手填 (evidence: [T02-S007, T03-S006])
- **近期变化（近 12 个月）**：model-viewer 持续小版本迭代（2026-06 v4.3.x），底层跟 Three.js + WebXR；功能稳态 (evidence: [T02-S006], 触发：工具更新，渐进)
- **典型耗时**：入门 1–3 小时；资深 <1 小时
- **关键工具**：Google model-viewer（必备-低代码）+ glTF-Transform（必备）(evidence: [T02-S006, S007, T03-S003])
- **关键人物**：Google model-viewer 团队（零门槛 3D/AR 路线）(evidence: [T01-S021])
- **常见失败模式**：
  - 没出 USDZ → iOS AR 不可用：iOS 必备 `ios-src` USDZ (evidence: [T02-S007])
  - 模型没压缩 → 详情页首屏慢：嵌入前必压 + 用 poster/lazy (evidence: [T03-S001, T03-S005])
  - 热点坐标手填错位 → 飘在模型外：用编辑器点选生成 data-surface/data-position (evidence: [T03-S006])
- **来源**：[Primary] T03-S005/S006；[seed] T02-S006/S007；[Reference] T01-S021
- **Last_updated**: 2026-06-06
- **Decay risk**: low（成熟 web component，API 稳定）

---

### 6. 跨端兼容 / 上线验收 QA 环

- **One-liner**: 从「展厅做完了」到「判定它到底能不能上线」——一套可勾选的验收判据，回答「移动端不崩 / 首屏达标 / 交互可用 / 低端机降级 / 多浏览器通过」。
- **Trigger**: 展厅功能完成、准备发布前的 go/no-go 判定（流程触发）(evidence: [T03-S004])
- **Output**: 通过验收清单、可发布的版本（或一份阻塞项清单）
- **入门 SOP（= 验收判据清单）**:
  1. **首屏达标**：在目标网络（如 4G）下首帧可交互时间达标；首屏资产体积在预算内（preload 关键资产、分级加载生效）(evidence: [T03-S001, T03-S004])
     - **跳过后果**：上线即高跳出率
  2. **移动端不崩**：真机（含中低端 Android）跑无闪退；显存在预算内（KTX2 + pixelRatio=1 生效）；查 `renderer.info.memory` 不持续上涨 (evidence: [T03-S001, T03-S004])
     - **跳过后果**：占比最大的移动用户直接崩溃
  3. **多浏览器**：Chrome / Firefox / Safari（macOS 与 **iOS 分开测**）；WebGPU 项目尤其测 Safari（timestamp query 不支持等怪癖）(evidence: [T03-S002, T03-S004])
     - **跳过后果**：某浏览器白屏/错位无人发现
  4. **低端机降级 / fallback 链通**：WebGL2 不可用→回退；`navigator.gpu` 判空→WebGL2；扩展可选降级；`MAX_TEXTURE_SIZE` 等 limit 查询后再用功能（最小安全值 4096 / 8 sampler）(evidence: [T03-S004, T03-S002])
     - **跳过后果**：老设备/弱机白屏，无兜底
  5. **交互可用**：动线/相机/热点/导览在触屏与鼠标都可用；AR（如有）真机通；context loss 可恢复（监听 `webglcontextlost`/`webglcontextrestored`，`event.preventDefault()` + 重建资源）(evidence: [T03-S004, T03-S006])
     - **跳过后果**：切后台/GPU 重置后永久黑屏
  6. **零 WebGL 错误**：生产构建控制台无 WebGL error（Firefox 32 个后停止描述性报错）(evidence: [T03-S004])
     - **跳过后果**：隐藏的渲染错误/兼容雷
- **资深路径（差异点）**：
  - **skip**：资深人**绝不只测自己的高配机**——这是头号验收陷阱（"在我机器上好的"）(evidence: [T03-S004])
  - **optimize**：把上面 6 条做成**可复用 checklist / 自动化**（Lighthouse 首屏、真机农场、`renderer.info` 断言进 CI）
  - **add**：资深人**额外测 context loss 恢复 + 低端真机 + iOS 单独一轮**——初学者几乎都漏 context loss 和 iOS 差异 (evidence: [T03-S004])
- **近期变化（近 12 个月）**：2025 末 WebGPU 各浏览器达基线后，QA 多一项「WebGPU 路径 + 自动 fallback 双跑验证」；Safari 26 补齐但仍需单测 (evidence: [T03-S002], 触发：标准更新)
- **典型耗时**：入门 0.5–2 天；资深 数小时（清单化 + 部分自动化）
- **关键工具**：stats-gl / Spector.js / renderer.info / Chrome DevTools / Lighthouse（监控-QA）(evidence: [T03-S001, S004])
- **关键人物**：（工程通则，无单一 figure）
- **常见失败模式**：
  - 只测自己高配机 → 上线移动端崩：必须中低端真机 + iOS 单独测 (evidence: [T03-S004])
  - 没处理 context loss → 切后台黑屏：监听 webglcontextlost/restored 并重建 (evidence: [T03-S004])
  - 无 fallback → 弱机白屏：确认 WebGPU→WebGL2 链通，扩展可选降级 (evidence: [T03-S002, T03-S004])
  - precision 默认 highp → 老移动 GPU 渲染损坏：`GL_FRAGMENT_PRECISION_HIGH` 检测后再用 highp (evidence: [T03-S004])
- **来源**：[Primary] T03-S004/S002；[Reference] T03-S001/S006
- **Last_updated**: 2026-06-06
- **Decay risk**: low（QA 判据稳态；增量是 WebGPU 双跑）

---

### 7. 高斯泼溅「实景扫描即展厅」管线（新兴）

- **One-liner**: 从「要 photoreal 实景、又不接受全景的平面感」到「可在 web 漫游的 3D 高斯泼溅场景」——2024–2026 兴起的第三条实景路线（全景与摄影测量 mesh 之外）。
- **Trigger**: 文物/空间要高保真写实重建，传统全景太平、摄影测量 mesh 出不来反光/细密结构（技术触发）(evidence: [T03-S009, T01-S032])
- **Output**: 清洗压缩后的 splat 场景（.ply/.spz/.ksplat/.sog）+ web viewer 集成
- **入门 SOP**:
  1. **采集**：手机视频 / 多角度照片 / 无人机绕拍（覆盖全、视差足、曝光稳）；Niantic Scaniverse、Polycam 等移动 app 可一站采集 (evidence: [T03-S009, T03-S010])
     - **跳过后果**：覆盖不足→空洞/漂浮高斯；视差不够→重建糊
  2. **处理 / 训练**：SfM（COLMAP）求相机位姿 → 训练高斯（postshot/brush/nerfstudio 类）；从草稿到高质量大场景分档 (evidence: [T03-S009, T03-S010])
     - **跳过后果**：无重建结果
  3. **清洗 / 编辑**：用 **SuperSplat**（浏览器内开源编辑器）裁掉漂浮物、背景、地面噪点，框定展示范围 (evidence: [T03-S014, T01-S034])
     - **跳过后果**：满场漂浮高斯 + 杂乱背景，不可展示
  4. **压缩 / 导出**：导出 web 友好格式——Niantic **SPZ**（开源、为渐进 web 传输优化）/ .ksplat / .sog 压缩；原始 .ply 太大需压 (evidence: [T03-S009, T03-S010])
     - **跳过后果**：原始 splat 体积巨大，首屏/移动端不可用
  5. **web viewer 集成 + 兜底**：PlayCanvas（一等支持）/ Spark / mkkellogg GaussianSplats3D（Three.js）/ Babylon 渲染；移动端性能与低端机降级要测 (evidence: [T01-S032, S033, T03-S010])
     - **跳过后果**：高端能跑、移动/低端崩
- **资深路径（差异点）**：
  - **skip**：跳过手工 3D 建模/UV/烘焙（splat 不需要传统 mesh 管线）(evidence: [T03-S010])
  - **optimize**：采集即按重建质量布点（环绕 + 多高度），减少训练返工；优先 SPZ/压缩格式做流式 (evidence: [T03-S009])
  - **add**：资深人**额外做清洗（SuperSplat 裁噪）+ 移动端/低端机降级方案 + 兼容兜底**——splat 编辑难、体积大、跨浏览器一致性仍是坑 (evidence: [T03-S009, T03-S014])
- **近期变化（近 12 个月，本 workflow 即"新变化"本身）**：
  - 2026-02 Khronos 宣布 **KHR_gaussian_splatting** glTF 扩展（存 position/rotation/scale/opacity/球谐），让 splat 进 glTF 容器、跨引擎可移植——**贡献方 Cesium/Niantic/Nvidia/Autodesk/Huawei/Esri** (evidence: [T03-S007, T03-S008], 触发：标准更新)
  - ⚠️ **保留矛盾**：扩展状态 —— Track 01 早前记为"glTF 高斯泼溅扩展**正式发布**"(T01-S038)；但官方规范 README 明确 **"Status: Release Candidate"**，新闻稿与综述称**2026-Q2 目标 ratify、仍开放反馈**；另有独立的 **SPZ 流式扩展**作为前瞻基建在规划中 (evidence: [T03-S008, T03-S007, T03-S010])。**结论：截至 2026-06 为 RC 候选，未正式 ratified**——使用时勿当稳定标准依赖
  - 工具链快速演进：SuperSplat 成事实编辑器；mkkellogg/Spark/PlayCanvas 并列 web 端主流查看器 (evidence: [T01-S034, S032, S033])
- **典型耗时**：入门 数小时–1 天（小场景，移动 app 采集）；资深 视场景规模，大场景训练可数小时–数天
- **关键工具**：Scaniverse/Polycam（采集）、COLMAP/postshot（训练）、SuperSplat（编辑，新兴）、PlayCanvas/GaussianSplats3D/Spark（渲染，新兴）(evidence: [T03-S009, S010, S014, T01-S032, S033])
- **关键人物**：Will Eastcott（PlayCanvas + SuperSplat）；Mark Kellogg（GaussianSplats3D，Three.js 集成）(evidence: [T01-S033, S034, S032])
- **常见失败模式**：
  - 采集覆盖/视差不足 → 重建糊/空洞：环绕 + 多高度 + 稳曝光，宁多拍 (evidence: [T03-S009])
  - 不清洗直接上 → 满场漂浮高斯：SuperSplat 裁噪、框范围后再发布 (evidence: [T03-S014])
  - 原始 .ply 直接上 web → 体积爆/移动崩：导 SPZ/.ksplat 压缩 + 测低端机 (evidence: [T03-S009, T03-S010])
  - 当成 ratified 标准做长期依赖 → 规范变动返工：KHR_gaussian_splatting 仍 RC，留迁移余地 (evidence: [T03-S008])
- **来源**：[Primary] T03-S007/S008/S009；[Secondary] T03-S010；[Reference] T01-S032/S033/S034；[seed] T04-S019
- **Last_updated**: 2026-06-06（基于 Khronos RC 新闻稿 2026-02 + 综述）
- **Decay risk**: high（新兴层默认；工具链 + 格式 + 标准 6–12 月可能大变，扩展 ratify 在即）

---

### 8. WebGL → WebGPU / TSL 迁移

- **One-liner**: 从「WebGL 撞性能墙 / 想用 compute」到「WebGPU 渲染 + 自动 WebGL2 fallback」——2025–2026 全行业渲染后端代际迁移。
- **Trigger**: 撞性能墙（50k+ 粒子、超高 draw call、compute 重负载）；新项目想直接上下一代；或 kiosk/装置可控硬件（技术触发）(evidence: [T03-S002])
- **Output**: 跑在 WebGPURenderer 上、不支持时自动回退 WebGL2 的展厅；shader 用 TSL 跨后端
- **入门 SOP**:
  1. **Audit 现状**：确认 Three.js ≥ r171；清点自定义 GLSL shader 与后期依赖（这些是迁移成本所在）(evidence: [T03-S002])
     - **跳过后果**：盲目升级后 shader/后期全挂找不到原因
  2. **升级 + 换 import/renderer**：`npm i three@latest`；`import * as THREE from 'three/webgpu'` + `new THREE.WebGPURenderer()`（该入口含 renderer/材质/灯光，自动 fallback WebGL2）(evidence: [T03-S002])
     - **跳过后果**：用错 import，混用报错
  3. **处理异步初始化（关键）**：`await renderer.init()` 后才能 setSize/渲染 (evidence: [T03-S002])
     - **跳过后果**：**白屏且无报错**（头号坑）
  4. **改写后期**：EffectComposer/旧后期 → TSL-native 或逐 pass 验证兼容 (evidence: [T03-S002])
     - **跳过后果**：后期效果直接失效
  5. **GLSL → TSL**：自定义 shader 改写 Three Shading Language（一次编译跨 WGSL/GLSL）(evidence: [T03-S002, T02-S031])
     - **跳过后果**：GLSL 在 WebGPU 上下文编译失败
  6. **fallback 检测 + 跨浏览器测**：查 `navigator.gpu` 优雅回退；Chrome/Firefox/Safari（macOS+iOS 分测），Safari 有 timestamp query/纹理格式怪癖 (evidence: [T03-S002])
     - **跳过后果**：Safari/旧机白屏未发现
- **资深路径（差异点）**：
  - **skip**：资深人**跳过迁移存量已流畅的项目**——WebGL 上跑得好、无新需求就不动；但新 shader 用 TSL 以免未来白做 (evidence: [T03-S002])
  - **optimize**：先 audit 再动手，按"标准材质→自定义 shader→后期"风险递增顺序迁；用 compute shader 把粒子/实例/后期搬 GPU (evidence: [T03-S002, T02-S031])
  - **add**：资深人**额外早测 Safari**（怪癖最多）+ 全程验证 fallback 双跑 (evidence: [T03-S002])
- **近期变化（近 12 个月，本 workflow 即变化本身）**：2025-09 r171 起 WebGPURenderer 内置、Safari 26 补齐最后一个浏览器；**2026-01 约 95% 用户浏览器支持、其余 5% 自动 fallback**；官方手册仍标 experimental (evidence: [T03-S002, T02-S002], 触发：标准/工具更新)
- **典型耗时**：简单项目（标准材质无自定义 shader）1–2 小时；有 GLSL shader 1–2 天 TSL 转换；大型应用含测试 1–2 周 (evidence: [T03-S002])
- **关键工具**：Three.js `three/webgpu` + TSL（新兴）；stats-gl（监控）(evidence: [T03-S002, T02-S002, S031])
- **关键人物**：mrdoob（主推 WebGPURenderer + TSL）；Maxime Heckel（TSL/WebGPU 实战指南）(evidence: [T01-S005, S030])
- **常见失败模式**：
  - 忘 `await renderer.init()` → 白屏无报错：init 必 await (evidence: [T03-S002])
  - 混用 `three` 与 `three/webgpu` import → 出错：统一用 `three/webgpu` (evidence: [T03-S002])
  - 自定义 ShaderMaterial/EffectComposer 直接搬 → 失效：改写 TSL/新后期栈 (evidence: [T03-S002])
  - 不测 Safari → 上线 Safari 崩：Safari 怪癖最多，早测 (evidence: [T03-S002])
- **来源**：[Primary] T03-S002；[seed] T02-S002/S030/S031；[Reference] T01-S005/S030
- **Last_updated**: 2026-01（基于迁移指南最新 first-hand 描述）
- **Decay risk**: medium（API/最佳实践 12–24 月仍演进，experimental 标未摘）

---

## Phase 2 提炼提示

**反复出现 ≥ 3 个 workflow 都包含的步骤**（候选 playbook 通则）:
- **「资产先压缩再上线」**（glTF-Transform: Draco/Meshopt + KTX2）出现于 W1/W4/W5/W7（摄影测量减面同源）→ 候选「如果模型要进 web，则上线前必跑 `gltf-transform optimize`，几何 Draco/Meshopt、纹理 KTX2，否则首屏必崩」(evidence: [T03-S001, S003, T03-S012])
- **「按瓶颈下手而非盲优化」**出现于 W4/W6/W8 → 候选「如果性能不达标，则先用 renderer.info/Spector.js 定位是 draw call / 显存 / 首屏体积 / fill rate 中的哪一个，只打那一处」(evidence: [T03-S001, S004])
- **「默认 fallback / 渐进增强」**出现于 W4/W6/W8 → 候选「如果用 WebGPU 或新特性，则必须验证 WebGL2/老设备/iOS 兜底链通，~5% 用户靠 fallback」(evidence: [T03-S002, S004])
- **「选型/合同阶段查锁定与导出」**出现于 W2（强）/W5（USDZ 兜底）→ 候选「如果走 SaaS，则选型即查导出权/二开授权/数据归属」(evidence: [T02-S022, S026])
- **「先定自由度（真3D vs 全景）再定栈」**贯穿 W1/W2/W3 的总开关 → 候选「如果需求不含自由走动/绕物/拾取交互，则全景720 足够，别上真 3D 引擎」(evidence: [T02-S016, T04-S016])

**入门 SOP 和资深路径之间最大的差距**（候选 心智模型）:
- 入门 SOP 普遍是「**功能驱动**」（先把场景搭出来、效果做炫），资深路径是「**约束驱动**」（先立性能/显存/首屏预算 + 挂监控，再反推可用面数/贴图/draw call）→ 心智模型候选「**性能预算前置**：线上展览不是先做炫再优化，是先定预算再在预算内做炫」(evidence: [T01-S010] Bruno Simon「四分之一算力、各设备能跑」, T03-S001/S004)
- 资深差异高频集中在三处：**skip 过早后期/视效**、**optimize 资产管线 CI 化 + 按瓶颈**、**add 显存预算 + 监控 + 跨端(尤其 iOS/低端机) 验收**——说明这一行资深人特别擅长「**克制（不过早优化也不过度堆效果）+ 量化（先测后做）**」

**近期工作流变化的根本原因**（触发事件类型分布）:
- **标准/工具更新驱动**（绝对主力）：5/8 workflow（W1/W4/W6/W7/W8）的近期变化都源于 WebGPU 基线化（2025-09 r171 + Safari 26）或 KHR_gaussian_splatting（2026-02 RC）——**渲染后端代际迁移 + 高斯泼溅标准化是本行两大外部驱动力**
- **AI 驱动**：1/8（W2，SaaS 内置 AI 生成展厅，2026，可信度 low）
- **稳态**：2/8（W3 全景 / W5 model-viewer 嵌入）明确无重大变化
- → Phase 2 应把「WebGPU/TSL 迁移」与「3DGS 标准化」列为本行心智模型/反模式的外部驱动力

**保留的核心矛盾**（供 Phase 1.5 / mental model 用）:
1. **高斯泼溅 glTF 扩展状态**：Track 01「正式发布」vs 官方 README「Release Candidate」(2026-Q2 目标 ratify) —— **以 README 一手为准：RC 未 ratified**，勿当稳定标准 (evidence: [T03-S008] vs [T01-S038])
2. **几何压缩 Draco vs Meshopt**：压缩率 vs 解码速度+压动画，按瓶颈选（沿 Track 02/04）(evidence: [T03-S003, T04-S013])
3. **自研 vs SaaS**：灵活无锁定但慢且贵、性能自扛 vs 快省事但锁定/二开受限（W1 vs W2）(evidence: [T02-S022, S026])
4. **WebGL 稳态 vs WebGPU 新兴**：存量不急迁 vs 新项目直接上（W8）(evidence: [T03-S002])
5. **实景三路线**：全景720（轻/平）vs 摄影测量 mesh（可控/出不来反光）vs 高斯泼溅（photoreal/编辑难体积大）(evidence: [T02-S016, T03-S012, S009])

**冷僻 / 信号薄弱（诚实边界）**:
- workflow 数 = 7（≥4，达标，非冷僻）；一手 source 占比高（T03 新源 14 个中 verified_primary 12 个，~86%，≥50% 达标）
- **资深差异点覆盖**：8/8 workflow 均有 ≥2 处（skip/optimize/add），100% 达标
- **薄弱点诚实标注**：
  1. **生产案例一手 narrative 稀缺**：三 js 论坛 showcase 多是「成品展示」而非工程复盘（如在线 3D 展厅作者仅说"Kotlin/JS on three.js，不算厉害"），缺中国语境下完整 case study（优质中文复盘多在黑名单平台，已排除）——本 track 的 SOP 主要由「工具典型场景 + 工程博客通则 + 规范」拼成，**非来自单一权威生产复盘**
  2. **高斯泼溅细节部分受限**：thefuture3d 综述页多次 429 限流未取全，GS 训练工具/压缩比具体数值依赖 Khronos + 搜索摘要，标 medium 可信
  3. **国内 SaaS 工作流**：以 vendor 营销页 + Track 02 seed 为主，缺第三方独立流程评测与价格透明度（沿 Track 01/02 诚实标注）
  4. **耗时数据**：除 W8 有 utsubo 明确小时/天/周数据外，其余为基于工具复杂度的工程经验推断（标 推断），非统计
