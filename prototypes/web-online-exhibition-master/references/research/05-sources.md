# Track 05 — Sources：Web 线上展览 / 虚拟展厅开发（要持续追踪的活信息源）

> Research date: 2026-06-06 · Locale: zh-CN（canon 全球）· OPUS subagent · 轨道焦点：3D web 技术变化快，重点追**版本/规范/changelog**
>
> **专门媒体层厚薄诚实判断（先说结论）**：这一行**没有传统意义的「行业 newsletter / 深度访谈 podcast」专门媒体层**——它是一个**「官方文档 + GitHub changelog + 个人教育博客 + 开放标准组织」驱动**的工程领域。真知识不沉淀在媒体里，而沉淀在 **① 官方文档与 release notes（threejs.org / 各引擎 docs / Khronos 规范）② 维护者个人技术博客（Maxime Heckel / Bruno Simon / SimonDev）③ 社区论坛实时问答（discourse.threejs.org / Babylon forum / 各 Discord）**。专门「文博数字展」媒体几乎不存在（多为 vendor PR + 中文黑名单站），只能用 IIIF 社区 / Google Arts & Culture / 会议作 surrogate。因此本 track 的 source 类型分布**偏向 docs/changelog + community + 教育博客**，而非 prompt 默认模板的 newsletter/podcast——这是**领域真实形态**，已诚实标注。
>
> **追踪铁律**：3D web 的最大 decay 来自**版本演进**（WebGPU/TSL 迁移、glTF 新扩展），所以「要追版本」的 ① 类源 decay risk 低（机构级基础设施）但**内容更新快**，必须定期看 changelog；而个人博客 decay risk 中高（作者倦怠）。

---

## Source Manifest

| source_id | url | bucket | last_checked | author/host | one-line note |
|-----------|-----|--------|--------------|-------------|---------------|
| T05-S001 | https://github.com/mrdoob/three.js/releases | verified_primary | 2026-06-06 | mrdoob / Three.js | **最该常追**：r184 (2025-04), ~2-3 月一版, 每版 breaking change |
| T05-S002 | https://threejs.org/docs/ | verified_primary | 2026-06-06 | Three.js | 官方文档 + manual; WebGPURenderer/TSL 章节是新栈权威 |
| T05-S003 | https://r3f.docs.pmnd.rs/getting-started/introduction | verified_primary | 2026-06-06 | Poimandres (pmndrs) | R3F 官方文档 + drei/xr/rapier/postprocessing 生态清单 |
| T05-S004 | https://doc.babylonjs.com/ | verified_primary | 2026-06-06 | Microsoft / Babylon.js | Babylon 官方文档, 含 changelog + What's New |
| T05-S005 | https://registry.khronos.org/glTF/ | verified_primary | 2026-06-06 | Khronos Group | glTF 2.0 规范 registry + 扩展注册表(权威 spec) |
| T05-S006 | https://www.khronos.org/news/ | verified_primary | 2026-06-06 | Khronos Group | **要追**：glTF Gaussian Splatting 扩展 (2026-02-03 announce) |
| T05-S007 | https://gltf-transform.dev/ | verified_primary | 2026-06-06 | Don McCurdy | glTF 优化 SDK/CLI 文档 + changelog(npm 发版, 非 GH Releases) |
| T05-S008 | https://www.w3.org/TR/webgpu/ | verified_primary | 2026-06-06 | W3C GPU for the Web WG | WebGPU 规范(追浏览器基线 + API 演进) |
| T05-S009 | https://developer.mozilla.org/en-US/docs/Web/API/WebGPU_API | verified_primary | 2026-06-06 | MDN | WebGPU/WebXR API 跨浏览器兼容性权威说明 |
| T05-S010 | https://web.dev/ | verified_primary | 2026-06-06 | Google Chrome team | 性能/WebGPU/图形工程文章(Chrome 团队一手) |
| T05-S011 | https://modelviewer.dev/ | verified_primary | 2026-06-06 | Google | <model-viewer> 文档; 版本追 github.com/google/model-viewer/releases |
| T05-S012 | https://discourse.threejs.org/ | secondary | 2026-06-06 | Three.js community | **最该常追(社区)**：官方论坛, 日更, 2026-06 仍活跃, showcase+问答 |
| T05-S013 | https://forum.babylonjs.com/ | secondary | 2026-06-06 | Babylon.js community | 官方论坛, 20.7k+ Q 主题, 维护者亲自答 |
| T05-S014 | https://discord.com/invite/three-js-685241246557667386 | reference | 2026-06-06 | Three.js Discord | 官方 Discord 18.2k 成员, 实时问答 |
| T05-S015 | https://discord.com/invite/poimandres | reference | 2026-06-06 | Poimandres | pmndrs Discord 10.6k 成员, R3F/drei 生态总部 |
| T05-S016 | https://github.com/KhronosGroup/glTF/discussions | reference | 2026-06-06 | Khronos glTF | glTF 规范/扩展讨论现场(splat 扩展辩论在此) |
| T05-S017 | https://www.reddit.com/r/threejs/ | reference | 2026-06-06 | r/threejs | 入门+作品分享, 信号比论坛稀但覆盖广 |
| T05-S018 | https://threejs-journey.com/ | secondary | 2026-06-06 | Bruno Simon | **教育锚**：66 课/93h/5万学员, $95 买断, 年更含 R3F 章 |
| T05-S019 | https://blog.maximeheckel.com/ | verified_primary | 2026-06-06 | Maxime Heckel | shader/R3F/TSL+WebGPU 实战长文(创意视效必读) |
| T05-S020 | https://simondev.io/ | secondary | 2026-06-06 | SimonDev | 底层图形/性能硬核教育(YouTube 21万订阅 + 课程) |
| T05-S021 | https://tympanus.net/codrops/ | secondary | 2026-06-06 | Codrops | **创意前端风向标**：2-3 篇/周, Three.js/WebGL 教程多 |
| T05-S022 | https://observablehq.com/ | secondary | 2026-06-06 | Observable | 可交互数据可视化 notebook(D3 生态, 展陈数据可视化) |
| T05-S023 | https://iiif.io/community/ | secondary | 2026-06-06 | IIIF Consortium | 文博图像互操作标准社区(定期 Zoom call + newsletter) |
| T05-S024 | https://artsandculture.google.com/ | secondary | 2026-06-06 | Google Arts & Culture | 文博数字展事实标杆(gigapixel/线上展案例源) |
| T05-S025 | https://s2026.siggraph.org/ | surrogate_primary | 2026-06-06 | ACM SIGGRAPH | 会议 sponsor/sessions: 2026 LA 7/19-23, 含 web3d/实时图形 |
| T05-S026 | https://web3d.siggraph.org/2025/ | surrogate_primary | 2026-06-06 | Web3D Consortium | 会议: Web3D 2025 Siena 9/9-10, 年度, web3D 学术专场 |
| T05-S027 | https://www.awwwards.com/ | secondary | 2026-06-06 | Awwwards | 创意 web 获奖榜(看沉浸式展厅/3D 站点趋势, 非技术深度) |
| T05-S028 | https://www.3dnest.cn/qverse | surrogate_primary | 2026-06-06 | 众趣科技 | vendor docs: 国内 VR 全景/虚拟展厅 SaaS 开发者页 |
| T05-S029 | https://www.kuleiman.com/ | surrogate_primary | 2026-06-06 | 酷雷曼 | vendor docs: 国内 VR 全景 + OEM 私有部署(文博/政务) |
| T05-S030 | https://support.matterport.com/s/ | surrogate_primary | 2026-06-06 | Matterport | vendor docs: 数字孪生 SaaS + Showcase SDK 更新追踪 |

> **bucket 说明**：沿用 02-tools.md / 01-figures.md precedent + manifest 规范。官方文档/规范/GitHub repo/Chrome 团队 web.dev/维护者一手工程博客标 `verified_primary`（覆盖 `source_verifier.py` 对未知 host 的 secondary 默认）。**论坛/Discord/Reddit** 是社区讨论渠道，按 verifier 实跑结果保留 `secondary`(discourse/babylon forum/threejs-journey/codrops/simondev/observable/IIIF/G A&C/awwwards 这类 host 默认 secondary) 或 `reference`(reddit/discord/GH discussions/comment)，**未私自升级**。**会议**(SIGGRAPH/Web3D) 标 `surrogate_primary` note「会议 sponsor」。**商业 SaaS 平台 docs** 标 `surrogate_primary` note `vendor docs`。**黑名单（知乎/公众号/百度百科/CSDN/简书/掘金；G2/Capterra）一律未收录**——文博数字展中文优质源大量命中黑名单，已诚实弃。

---

## 总览（按 type 分组）

### 官方文档与 changelog（要追版本）— 11 个

| Source | Cadence | Tier | 投入产出 | One-liner |
|--------|---------|------|---------|-----------|
| Three.js Releases (S001) | ~2-3 月/版 | mixed | **high** | r184 起每版可能 breaking, WebGPU/TSL 演进主战场 |
| threejs.org docs/manual (S002) | rolling | mixed | **high** | API 真相 + WebGPURenderer 手册, 随版本同步 |
| R3F docs (pmndrs) (S003) | rolling | practitioner | high | R3F + 整个 drei/xr 生态入口清单 |
| Babylon.js docs (S004) | rolling | mixed | medium | 全功能引擎权威 + What's New changelog |
| Khronos glTF registry (S005) | spec 版次 | senior | high | glTF 2.0 spec + 扩展注册表(资产格式 ground truth) |
| Khronos news (S006) | 多条/月 | senior | high | 新扩展/标准动态(splat 扩展 2026-02 在此发) |
| glTF-Transform docs (S007) | 跟随 npm 发版 | practitioner | high | 资产优化 CLI/SDK 文档 + changelog |
| W3C WebGPU spec (S008) | rolling | senior | medium | WebGPU 规范本体(深, 多数人看 MDN 即可) |
| MDN WebGPU/WebXR (S009) | rolling | practitioner | high | 跨浏览器兼容性 + API 用法权威 |
| web.dev (S010) | 不定期 | practitioner | medium | Chrome 团队性能/WebGPU/图形一手文 |
| model-viewer (S011) | ~数月/版 | beginner | medium | 低代码嵌 3D/AR 文档 + GH releases 追版本 |

### 社区（Community）— 6 个

| Community | Platform | 规模 | 投入产出 | One-liner |
|-----------|----------|------|---------|-----------|
| Three.js forum (S012) | Discourse | 日更/大 | **high** | 官方论坛, 2026-06 仍活跃, 问答+showcase+jobs |
| Babylon.js forum (S013) | Discourse | 20.7k+ Q | medium | 官方论坛, 维护者亲自答, 工程问题深 |
| Three.js Discord (S014) | Discord | 18.2k | medium | 实时问答, 比论坛快但不留存 |
| Poimandres Discord (S015) | Discord | 10.6k | high | R3F/drei 生态总部, 维护者出没 |
| Khronos glTF Discussions (S016) | GitHub | 中 | medium | 规范/扩展辩论现场(splat 扩展在此成形) |
| r/threejs (S017) | Reddit | 中 | low | 入门+作品分享, 信号稀但广 |

### 教育 / 博客（Education）— 5 个

| Source | Cadence | Tier | 投入产出 | One-liner |
|--------|---------|------|---------|-----------|
| Three.js Journey (S018) | 年更 | beginner→adv | high | Bruno Simon 系统课, 入门到 R3F 的事实标准路径 |
| Maxime Heckel blog (S019) | 月级不定 | practitioner→senior | high | shader/TSL/WebGPU 实战长文, 视效工艺 |
| SimonDev (S020) | 不定期 | practitioner→senior | medium | 底层图形/性能深挖(YouTube+课程) |
| Codrops (S021) | 2-3/周 | practitioner | medium | 创意前端教程风向标, Three.js/WebGL 多 |
| Observable (S022) | rolling | practitioner | low | 数据可视化 notebook(展陈数据/交互图表场景) |

### 文博源（文博 / 展览数字化）— 2 个

| Source | URL | Maintainer | 投入产出 | One-liner |
|--------|-----|-----------|---------|-----------|
| IIIF community (S023) | iiif.io/community | IIIF Consortium | medium | 文博图像互操作标准社区(call+newsletter+Slack) |
| Google Arts & Culture (S024) | artsandculture.google.com | Google | medium | 文博数字展事实标杆 + 线上展案例库 |

### 会议 / 资讯（Conference）— 3 个

| Conference | 频率 | 下届/最近 | One-liner |
|-----------|------|----------|-----------|
| SIGGRAPH (S025) | 年度 | 2026 LA, 7/19-23 | 实时图形顶会, web3d/WebGPU 专场看趋势 |
| Web3D Conference (S026) | 年度 | 2025 Siena 9/9-10 | ACM SIGGRAPH 协办, web 3D 学术专场 |
| Awwwards (S027) | rolling | — | 创意 web 获奖榜, 看沉浸式 3D 站点设计趋势 |

### 平台 docs（vendor，surrogate）— 3 个

| Source | URL | Maintainer | One-liner |
|--------|-----|-----------|-----------|
| 众趣 Qverse (S028) | 3dnest.cn/qverse | 众趣科技 | 国内 VR 全景/虚拟展厅 SaaS 开发者页 |
| 酷雷曼 (S029) | kuleiman.com | 酷雷曼 | 国内 VR 全景 + OEM 私有部署 |
| Matterport support/SDK (S030) | support.matterport.com | Matterport | 数字孪生 SDK 更新 + 二开文档 |

> Dataset / Benchmark：**N/A for this industry**（3D web 工程无标准 benchmark dataset；最接近的是各引擎自带 demo 与 glTF-Sample-Assets，已隐含在 docs 源中，不单列）。

---

## Source 详细卡片（按追踪优先级）

### 官方文档与 changelog（要追版本）

#### S001. Three.js GitHub Releases ★最该常追

- **Type**: 官方 changelog（repo releases）
- **URL**: https://github.com/mrdoob/three.js/releases
- **Author / Host**: mrdoob (Ricardo Cabello) + 社区（Track 01 figure #1）
- **Cadence**: ~每 2-3 个月一个 rNNN 版本（r182 2024-12 / r183 2025-02 / r184 2025-04）(evidence: [T05-S001]，一手)
- **Last activity**: r184 (2025-04-16)，repo 持续高频 commit (evidence: [T05-S001])
- **Audience tier**: mixed
- **One-liner**: 整个 web 3D 栈的地基版本源——每个 rNNN 都可能含 breaking change（尤其 WebGPU/TSL 重写期），不看 release notes 升级必踩坑
- **典型每期内容**: 渲染器改动、WebGPURenderer/node 材质演进、loader 修复、deprecation 通知、breaking changes 列表。WebGL→WebGPU 双轨迁移的所有动作都先落在这里
- **投入产出比**: **high**——这是该领域 #1 必追源，升级前必读 (evidence: [T05-S001])
- **Paywall**: none
- **Endorsement**: `figure_long`（mrdoob 本人维护，Track 01 #1）+ `cross_source`（Bruno Simon 课程/Maxime Heckel 博客均追其版本）(evidence: [T05-S001, 见 01-figures T01-S001])
- **替代品**: threejs.org migration guide（迁移专页）
- **可信度**: high · **Decay risk**: low（行业基础设施）但**内容更新快**，须定期刷

#### S005 + S006. Khronos glTF Registry + News ★最该常追

- **Type**: 官方规范 registry + 标准组织 news
- **URL**: https://registry.khronos.org/glTF/ · https://www.khronos.org/news/
- **Author / Host**: Khronos Group（glTF/KTX/3D Commerce 工作组）
- **Cadence**: registry 按 spec 版次更新；news 多条/月（2026-05 至少 5 条）(evidence: [T05-S006])
- **Last activity**: **glTF Gaussian Splatting 扩展 2026-02-03 announce**；3D Commerce 新成员 2026-04-29 (evidence: [T05-S006]，一手)
- **Audience tier**: senior
- **One-liner**: 3D 资产格式的 ground truth——新扩展（splat/材质变体/压缩）首发地，决定未来展厅能用什么
- **典型每期内容**: glTF 核心 + 扩展注册表更新、新 KHR_/EXT_ 扩展提案与批准、3D Commerce 认证、Gaussian Splatting 标准化进展
- **投入产出比**: high——追「资产格式未来」唯一权威源；splat 扩展正是 02-tools 标 high-decay 的新兴管线，标准化动态必追 (evidence: [T05-S006，见 01-figures T01-S038])
- **Paywall**: none
- **Endorsement**: `figure_long`（Don McCurdy / Patrick Cozzi 均在此体系，Track 01 #4/#5）+ `cross_source` (evidence: [T05-S006])
- **替代品**: github.com/KhronosGroup/glTF/discussions（S016，辩论现场）
- **可信度**: high · **Decay risk**: low（机构级）

#### S007. glTF-Transform docs ★工具命门追踪

- **Type**: 工具文档 + changelog
- **URL**: https://gltf-transform.dev/
- **Author / Host**: Don McCurdy（Track 01 figure #4，现 Bentley 开放标准总监）
- **Cadence**: 跟随 npm 发版（注：GitHub Releases 标签页空/报错，发版走 npm + 文档 changelog，须从 npm 或文档查版本）(evidence: [T05-S007]，一手)
- **Last activity**: 持续维护（99% TS，2089 commits，见 02-tools T02-S008）
- **Audience tier**: practitioner
- **One-liner**: 资产轻量化命门工具的版本源——`optimize` 一条命令串 Draco/Meshopt/KTX2，是上线前必做管线
- **投入产出比**: high（性能命门工具，几乎所有展厅项目都用）(evidence: [T05-S007])
- **Paywall**: none
- **Endorsement**: `figure_long`（McCurdy 本人）+ `cross_source`（02-tools 多处引为性能命门）
- **可信度**: high · **Decay risk**: low
- **追踪注意**：版本不在 GH Releases 页，去 npm `@gltf-transform/core` 或文档 changelog 看

#### S002/S003/S004. 引擎官方文档（Three.js manual / R3F / Babylon）

- **Type**: 官方文档（rolling）
- **URL**: https://threejs.org/docs/ · https://r3f.docs.pmnd.rs/ · https://doc.babylonjs.com/
- **Cadence**: rolling，随各自版本同步
- **Audience tier**: mixed（Three.js/Babylon）/ practitioner（R3F）
- **One-liner**: 三大引擎 API 真相——Three.js manual 的 WebGPURenderer 章是新栈唯一权威；R3F docs 自带整个 drei/xr/rapier/postprocessing 生态清单（选型时的 ecosystem 地图）(evidence: [T05-S002, T05-S003，一手确认 R3F docs 由 pmndrs 维护且含 Ecosystem 节])
- **投入产出比**: Three.js docs/R3F high；Babylon docs medium（用 Babylon 才追）
- **Paywall**: none
- **可信度**: high · **Decay risk**: low（更新快须随版本回看）

#### S008/S009/S010. 标准与平台（W3C WebGPU / MDN / web.dev）

- **Type**: 规范 + 兼容性文档 + Chrome 团队博客
- **URL**: https://www.w3.org/TR/webgpu/ · https://developer.mozilla.org/.../WebGPU_API · https://web.dev/
- **Cadence**: spec/docs rolling；web.dev 不定期
- **One-liner**: WebGPU/WebXR 的标准与浏览器落地真相——W3C spec 是本体（深，多数人看 MDN 够），MDN 给跨浏览器兼容性，web.dev 是 Chrome 团队的图形/性能一手实践 (evidence: [T05-S008, T05-S009, T05-S010])
- **投入产出比**: MDN high（兼容性查询高频）；W3C spec medium（深但少看）；web.dev medium
- **Paywall**: none
- **可信度**: high（机构一手）· **Decay risk**: low

#### S011. Google model-viewer

- **Type**: 官方文档 + GH releases
- **URL**: https://modelviewer.dev/（版本：github.com/google/model-viewer/releases）
- **Cadence**: ~每数月一版（最新 v4.3.1，与 02-tools T02-S006 一致 2026-06-04；注：WebFetch 对 releases 页解析出 2024 年份疑似缓存/解析误差，版本号 v4.3.1 一致，以 GH releases 实查为准）(evidence: [T05-S011]，需复核年份)
- **Audience tier**: beginner
- **One-liner**: 低代码嵌单个 3D/AR 模型——电商/展品详情页主力，版本追 GH releases
- **投入产出比**: medium（嵌单模型场景才追）
- **可信度**: high · **Decay risk**: low

---

### 社区（Community）

#### S012. Three.js Forum (Discourse) ★最该常追（社区）

- **Type**: community（官方论坛）
- **URL**: https://discourse.threejs.org/
- **Author / Host**: Three.js 社区（官方 discourse）
- **Cadence**: 日更（rolling）
- **Last activity**: **2026-06 仍每日多帖**（showcase / questions / resources / jobs 全活跃）(evidence: [T05-S012]，一手确认)
- **Audience tier**: mixed
- **One-liner**: 该领域工程问题的实时知识库——「怎么做 X / 为什么白屏 / 这个效果如何实现」的第一去处，showcase 区是看真实作品水平的窗口
- **典型每期内容**: shader/geometry 技术问答、作品 showcase（如实时音频可视化、模拟器）、资源发布、招聘
- **投入产出比**: **high**（社区类 #1；问题驱动学习 + 趋势嗅探）(evidence: [T05-S012])
- **Paywall**: none
- **Endorsement**: `community_consensus`（官方论坛）+ `cross_source`
- **替代品**: Three.js Discord（S014，更快但不留存）
- **可信度**: high · **Decay risk**: low

#### S013-S017. 其余社区（Babylon forum / Discord×2 / glTF Discussions / Reddit）

- **Babylon forum (S013)**：官方 Discourse，20.7k+ Q 主题，维护者亲自答，用 Babylon 才追 (evidence: [T05-S013]，一手确认主题数)
- **Three.js Discord (S014)**：18.2k 成员，实时问答快但不留存 (evidence: [T05-S014]，一手确认规模)
- **Poimandres Discord (S015)**：10.6k 成员，R3F/drei 生态总部，维护者出没——R3F 用户必进 (evidence: [T05-S015]，一手确认规模)
- **Khronos glTF Discussions (S016)**：规范/扩展辩论现场，Gaussian Splatting 扩展在此成形 (evidence: [T05-S016])
- **r/threejs (S017)**：入门 + 作品分享，信号稀（投入产出 low）但覆盖广 (evidence: [T05-S017])
- **投入产出比**: Poimandres Discord high；Babylon forum/Three.js Discord/glTF Discussions medium；Reddit low
- **可信度**: high（S013-S016）/ medium（S017）· **Decay risk**: medium（与 platform 命运绑定）

---

### 教育 / 博客（Education）

#### S018. Three.js Journey (Bruno Simon) ★教育锚

- **Type**: 教育（付费课程）
- **URL**: https://threejs-journey.com/
- **Author / Host**: Bruno Simon（Track 01 figure #2，最佳可蒸馏教育者）
- **Cadence**: 年度多次更新（依赖更新 + 新课）；课程本体 rolling (evidence: [T05-S018]，一手确认)
- **Last activity**: 持续更新（66 课 / 93h / 50,393 学员）(evidence: [T05-S018])
- **Audience tier**: beginner → advanced
- **One-liner**: 「如何学会做 3D 网站」的事实标准路径——从 WebGL 基础到 R3F（专章 14 课 24h），新人入行近乎必经
- **典型每期内容**: 7 章——基础 / 经典技术 / 高级技术 / shader / 移植 / 可移植性能 / React Three Fiber；含 Blender 建模 + 性能优化
- **投入产出比**: high（系统性最强的单一学习源）(evidence: [T05-S018])
- **Paywall**: **$95 USD 一次性买断**（含终身更新 + 私有 Discord + 证书）——worth it：唯一系统覆盖入门到 R3F 的课，比拼凑免费教程效率高得多 (evidence: [T05-S018])
- **Endorsement**: `figure_long`（Bruno Simon 本人）+ `community_consensus`（社区公认入门标准）
- **替代品**: SimonDev 课程（更底层/游戏向）；官方 docs（免费但无体系）
- **可信度**: high · **Decay risk**: low（已是行业基础设施级教育）
- **注**：当前内容未明确含 WebGPU/TSL 章（fetch 未见），但 R3F 章充分；TSL 实战看 Maxime Heckel (S019)

#### S019. Maxime Heckel blog

- **Type**: 教育（个人技术博客）
- **URL**: https://blog.maximeheckel.com/
- **Author / Host**: Maxime Heckel（Track 01 figure #10）
- **Cadence**: 月级不定期
- **Audience tier**: practitioner → senior
- **One-liner**: 高级视觉效果（焦散/折射/粒子/后处理）与 **TSL+WebGPU 实战**的最佳长文写作者——做展厅高级视效几乎必读
- **签名内容**: 「Field Guide to TSL and WebGPU」「The Study of Shaders with React Three Fiber」(evidence: [T05-S019]，一手)
- **投入产出比**: high（追新栈 shader 工艺的顶级源）
- **Paywall**: none · **可信度**: high · **Decay risk**: medium（个人博客默认）

#### S020/S021/S022. SimonDev / Codrops / Observable

- **SimonDev (S020)**：底层图形/性能硬核教育（YouTube 21万订阅 + 课程），「理解底层 > 框架抽象」立场，与 Bruno 互补；投入产出 medium，偏游戏/底层 (evidence: [T05-S020])
- **Codrops (S021)**：**创意前端风向标**，2-3 篇/周，2026-06 活跃，Three.js/WebGL 教程多（如「Scroll-Reactive 3D Gallery with Three.js」）；看「沉浸式站点怎么做」的趋势源；投入产出 medium (evidence: [T05-S021]，一手确认 cadence)
- **Observable (S022)**：可交互数据可视化 notebook（D3 生态），展陈数据/交互图表场景才用；投入产出 low (evidence: [T05-S022])
- **可信度**: medium（S020/S021）/ medium（S022）· **Decay risk**: medium

---

### 文博源（文博 / 展览数字化）

#### S023. IIIF Community

- **Type**: community（开放标准社区）
- **URL**: https://iiif.io/community/
- **Author / Host**: IIIF Consortium
- **Cadence**: 定期 Zoom group call + newsletter + Slack（rolling）(evidence: [T05-S023]，一手确认)
- **Audience tier**: practitioner（GLAM 文博技术侧）
- **One-liner**: 文博「高质量图像在线交付互操作」的标准社区——深缩放/标注/跨馆图像复用的事实标准，文博数字化项目绕不开
- **投入产出比**: medium（做文博线上展、要接馆藏图像时 high；纯 3D 展厅 low）
- **Paywall**: none
- **Endorsement**: `community_consensus`（GLAM 行业标准社区）+ `cross_source`（01-figures T01-S042 引为文博标准）
- **可信度**: high · **Decay risk**: low（机构级标准社区）

#### S024. Google Arts & Culture

- **Type**: 文博案例库 + 产品愿景源
- **URL**: https://artsandculture.google.com/
- **Author / Host**: Google（Amit Sood，Track 01 figure #12）
- **Cadence**: rolling（持续上新展）
- **Audience tier**: mixed
- **One-liner**: 全球文博数字展事实标杆——gigapixel 深缩放 + 在线策展 + ML×文化实验，是「文博线上展能做到什么程度」的参照系与案例库
- **投入产出比**: medium（看案例/趋势 high；技术细节不公开）
- **Paywall**: none
- **Endorsement**: `figure_long`（Amit Sood 两个 TED talk，01-figures T01-S039/S040）
- **可信度**: high · **Decay risk**: low

> **文博媒体层诚实判断**：除 IIIF（标准社区）+ Google A&C（案例标杆）外，**「文博数字展」专门媒体/newsletter/podcast 在合规源里几乎不存在**——中文文博数字化深度内容大量沉淀在知乎/公众号/CSDN（全黑名单），英文侧分散在博物馆个体博客与学术会议（如 MCN / Museums and the Web，本轮未单列，可 Phase 4 补）。**这是该 track 最薄的一层**。

---

### 会议 / 资讯（Conference）

#### S025. SIGGRAPH

- **Type**: conference（surrogate：sponsor/sessions list）
- **URL**: https://s2026.siggraph.org/
- **Cadence**: 年度
- **Last/Next edition**: **2026 Los Angeles，7/19-23**（2025 在 Vancouver）(evidence: [T05-S025]，一手)
- **One-liner**: 实时图形顶会——WebGPU/web3d/实时渲染前沿 talk + Real-Time Live，看「12-24 月后会进 web」的技术
- **投入产出比**: medium（年度信号密集但学术/影视为主，web3d 是子集）
- **Endorsement**: `surrogate_primary`（会议 sponsor/sessions）+ figure 关联（mrdoob 在 JSConf 等讲，Cozzi 主持 Open Metaverse podcast）
- **可信度**: high · **Decay risk**: low（机构级，年度稳定）

#### S026. Web3D Conference

- **Type**: conference（surrogate）
- **URL**: https://web3d.siggraph.org/2025/
- **Cadence**: 年度
- **Last edition**: **Web3D 2025，Siena 意大利，9/9-10**（ACM SIGGRAPH 协办 + Web3D Consortium + Eurographics 支持）(evidence: [T05-S026]，一手)
- **One-liner**: web 3D 的专门学术会议——比 SIGGRAPH 更聚焦 web3D/X3D/glTF/沉浸 web，规模小但对口
- **投入产出比**: low-medium（学术向，从业者价值在趋势嗅探）
- **Endorsement**: `surrogate_primary`（Web3D Consortium 主办）
- **可信度**: high · **Decay risk**: low（年度，但需复核 2026 是否如期，next edition 间隔须留意）

#### S027. Awwwards（+ FWA 同类）

- **Type**: 资讯（获奖榜/趋势）
- **URL**: https://www.awwwards.com/
- **Cadence**: rolling
- **One-liner**: 创意 web 获奖榜——看沉浸式 3D 站点/虚拟展厅的**设计与体验趋势**（非技术深度），FWA 同类
- **投入产出比**: low（趋势灵感源，非 actionable 技术）
- **可信度**: medium（设计趋势，非工程权威）· **Decay risk**: low

---

### 平台 docs（vendor surrogate）

#### S028-S030. 国内/商业 SaaS docs（众趣 / 酷雷曼 / Matterport）

- **Type**: vendor docs（surrogate_primary）
- **URL**: https://www.3dnest.cn/qverse · https://www.kuleiman.com/ · https://support.matterport.com/s/
- **Cadence**: rolling（产品更新）
- **One-liner**: 国内 VR 全景/虚拟展厅 SaaS（众趣/酷雷曼）+ 数字孪生 SDK（Matterport）的功能与二开更新——走 SaaS 路线/国内小程序分发/做二开时追
- **投入产出比**: low-medium（仅相关项目追；vendor 一面之词，须 ≥2 source 交叉）
- **Endorsement**: `surrogate_primary`（vendor docs，note `vendor docs`）
- **可信度**: medium（vendor docs）· **Decay risk**: medium
- **诚实标注**：国内平台**独立第三方深度评测/动态几乎全在黑名单**（知乎/公众号/CSDN/VR陀螺），只能用 vendor 官网作 surrogate，**未直接听到独立声音**

---

## Phase 2 提炼提示

### 「这一行的资深人订阅最多的 top sources」（→ master skill「Sources — 信息源」节 highlights）

按**追踪频率 + 跨源背书**排序的 **top 5 最该常追**：

1. **Three.js GitHub Releases (S001)** — ~2-3 月/版，每版可能 breaking，WebGPU/TSL 迁移主战场。**升级前必读 release notes**。该领域 #1 必追源 (evidence: [T05-S001])
2. **Khronos glTF Registry + News (S005/S006)** — 资产格式 ground truth；新扩展首发地（Gaussian Splatting 扩展 2026-02 在此 announce）。news 多条/月，registry 按 spec 版次 (evidence: [T05-S006])
3. **Bruno Simon / Three.js Journey (S018)** — 入门到 R3F 的事实标准学习路径，年度更新，$95 买断；新人/带新人必经 (evidence: [T05-S018])
4. **Three.js Forum / Discourse (S012)** — 社区 #1，日更，2026-06 活跃；工程问题实时知识库 + 趋势嗅探 (evidence: [T05-S012])
5. **glTF-Transform (S007) + Maxime Heckel blog (S019)** 并列 — 前者资产优化命门工具（追 npm 发版），后者 TSL/WebGPU shader 工艺顶级实战长文 (evidence: [T05-S007, T05-S019])

> 补充常追：R3F docs (S003，含整个生态清单) / Poimandres Discord (S015) / MDN WebGPU (S009，兼容性查询)。

### 「这一行最近的话题热度」（候选信号 — Phase 2.4 近期工作流变化）

- `topic-heat: medium-confidence`（部分 source 爬了具体 item：Khronos news / Codrops / Three.js forum / Three.js releases 已查最新条目；多数 docs/community 未逐帖爬取）
- 最近被多源反复出现的主题：
  1. **WebGPU + TSL 迁移**（S001 Three.js releases / S019 Maxime Heckel「Field Guide to TSL」/ S002 manual WebGPURenderer 章 / S004 Babylon WebGPU）——全行业最大技术拐点，2025 末浏览器达基线
  2. **3D Gaussian Splatting 标准化**（S006 Khronos 2026-02-03 glTF splat 扩展 announce / S016 discussions 辩论 / 02-tools 标 high-decay 新兴）——「扫描即展厅」管线从实验走向标准
  3. **创意 3D 站点/scroll 交互**（S021 Codrops「Scroll-Reactive 3D Gallery」等 2-3/周 / S027 Awwwards）——沉浸式 web 展陈设计持续热

### 新 figures 发现（喂 wave 2 Track 01）

- 本 track sources 的作者**已全部在 01-figures 覆盖**（mrdoob/Bruno Simon/Paul Henschel/Don McCurdy/Maxime Heckel/SimonDev/Amit Sood/David Catuhe/Will Eastcott）——无新增 figure 候选。**反向确认 01-figures 的 figure 池与 source 池高度自洽**（健康信号：该领域 figure = source 作者）
- 潜在补充（本轮未深挖，Phase 4 可选）：**Brandon Jones**（WebGPU/WebXR 规范 W3C 编辑，是 S008 背后的人）；**Kevin Ngo**（A-Frame 共同维护者）——若 focus 含 WebXR/规范层可补

### 新 tools 发现（喂 wave 2 Track 02）

- 无显著新工具——本 track docs/changelog 指向的工具（Three.js/R3F/Babylon/glTF-Transform/model-viewer/WebGPU）**已全部在 02-tools 覆盖**
- 轻信号：**Observable/D3**（S022）作为「展陈数据可视化」工具，02-tools 未单列（其聚焦 3D/全景，数据可视化是边缘场景）——如展厅含数据展陈维度可补

### 冷僻 / 信号薄弱（诚实评估）

- **专门媒体层（newsletter/podcast）薄**：该领域**几乎无传统行业 newsletter / 深度访谈 podcast 专门媒体**——这不是调研不足，是**领域真实形态**：知识沉淀在 ① 官方 docs/changelog ② 维护者个人博客 ③ 社区论坛/Discord 实时问答，而非媒体。prompt 模板的 newsletter/podcast 字段对本领域**结构性偏空**，已用 docs/changelog + community + 教育博客填满（共 30 源，远超 floor 15）
- **文博源最薄**：合规文博数字展深度源仅 IIIF + Google A&C 两个机构级源；中文文博数字化优质内容**大量命中黑名单**（知乎/公众号/CSDN/VR陀螺），英文侧分散在博物馆个体博客 + MCN/Museums and the Web 会议（本轮未单列）。**真知识在这一层确实稀薄**
- **国内平台侧**：仅 vendor docs surrogate，独立第三方评测全在黑名单，**未直接听到独立声音**
- **podcast 个例**：Patrick Cozzi 主持的「Building the Open Metaverse」podcast（01-figures T01-S035）是该领域最接近「深度访谈 podcast」的源（嘉宾覆盖多数 3D web 关键人），但偏 metaverse/标准而非展厅工程，本 track 未单列为主源，Phase 4 可考虑补入教育/资讯层
- **结论**：sources 对**开发工程侧极厚**（docs/changelog/community/教育博客四线全满，质量高、第一方丰富）；对**专门媒体 + 文博内容侧结构性偏薄**（领域本身就没有厚媒体层 + 中文优质源被黑名单垄断）。**真知识主要沉淀在官方 changelog（追版本）+ 维护者个人博客（方法论）+ 社区论坛（实时问答）三处，而非任何媒体层**——这是该 track 最重要的诚实判断。

### 缺口（移交 Phase 1.5 / Phase 4）

1. **文博内容媒体层**：MCN（Museum Computer Network）/ Museums and the Web 会议 + newsletter 未单列，若 focus 重文博策展应补
2. **WebXR/规范层 podcast/newsletter**：Voices of VR（已在 01-figures 作 figure 来源）可作沉浸侧资讯源，本 track 未单列
3. **model-viewer 版本年份需复核**：WebFetch 对 GH releases 页解析出 2024 年份，与 02-tools 的 2026-06-04 不一致，疑似缓存/解析误差，Phase 4 freshness 直查 GH releases 确认
4. **glTF-Transform 版本追踪路径**：发版走 npm 而非 GH Releases 页（页空/报错），update 流程须指向 npm `@gltf-transform/core` 或文档 changelog
