# Track 02 — Tools Research: Music Production & Mixing (音乐制作 / 混音)

> Wave 2 track. Seeded from Wave 1: Track 04 (canon) named FabFilter/Worrall, DAWs, iZotope/LUFS, Auto-Tune/Melodyne, K-System meters, MWTM; Track 05 (sources) named FabFilter 全家桶, Dolby Atmos 链路, NAMM/AES exhibitor-as-surrogate, AI 母带/AI 混音 争论.
> Locale: global (en-primary, material-rich). Tools 维度信号厚 — vendor docs + 评测 + 论坛 null-test + 行业 survey 充足。
> **Vendor 声明规则**: 插件/DAW 厂商 product/docs 页 → 本文件统一声明 `surrogate_primary` + note 含 `vendor docs`（即便 `source_verifier.py classify` 返回 verified_primary，不私自升强桶）。AES/ITU/EBU 标准页才作 verified_primary。

## Source Manifest

| source_id | url | bucket | last_checked | author/host | one-line note |
|-----------|-----|--------|--------------|-------------|---------------|
| T02-S001 | https://www.fabfilter.com/products/pro-q-4-equalizer-plug-in | surrogate_primary | 2026-06-18 | FabFilter | vendor docs — Pro-Q 4 EQ 产品页 |
| T02-S002 | https://www.fabfilter.com/news/1733994000/fabfilter-releases-pro-q-4-equalizer-plug-in | surrogate_primary | 2026-06-18 | FabFilter | vendor docs — Pro-Q 4 发布(2024-12-12) |
| T02-S003 | https://www.production-expert.com/production-expert-1/2025-daw-survey-the-results | secondary | 2026-06-18 | Production Expert | 2025 DAW survey 结果(行业调查) |
| T02-S004 | https://www.izotope.com/en/products/ozone.html | surrogate_primary | 2026-06-18 | iZotope | vendor docs — Ozone 母带套件 |
| T02-S005 | https://www.izotope.com/pages/release-notes/ozone-advanced | surrogate_primary | 2026-06-18 | iZotope | vendor docs — Ozone 12 release notes |
| T02-S006 | https://www.soundonsound.com/reviews/izotope-ozone-11-advanced | verified_primary | 2026-06-18 | Sound On Sound | Ozone 11 Advanced 评测 |
| T02-S007 | https://www.sonible.com/smarteq4/ | secondary | 2026-06-18 | sonible | vendor — smart:EQ 4 产品页(verifier=secondary) |
| T02-S008 | https://musictech.com/reviews/sonible-smarteq-4-review-future-of-ai-mixing/ | secondary | 2026-06-18 | MusicTech | smart:EQ 4 评测 |
| T02-S009 | https://musictech.com/guides/buyers-guide/best-stem-separation-tools/ | secondary | 2026-06-18 | MusicTech | 9 款 stem 分离工具横评 |
| T02-S010 | https://www.soundonsound.com/techniques/landr-cloudbounce-future-mastering | verified_primary | 2026-06-18 | Sound On Sound | SOS 论 AI 在线母带的未来 |
| T02-S011 | https://valhalladsp.com/shop/reverb/valhalla-vintage-verb/ | surrogate_primary | 2026-06-18 | Valhalla DSP | vendor docs — VintageVerb 产品页 |
| T02-S012 | https://www.uaudio.com/ | surrogate_primary | 2026-06-18 | Universal Audio | vendor docs — UAD/Apollo 主站 |
| T02-S013 | https://www.celemony.com/en/melodyne/what-is-melodyne | surrogate_primary | 2026-06-18 | Celemony | vendor docs — Melodyne 介绍 |
| T02-S014 | https://www.soundonsound.com/reviews/auto-tune-vs-melodyne | verified_primary | 2026-06-18 | Sound On Sound | Auto-Tune vs Melodyne 对比 |
| T02-S015 | https://oeksound.com/plugins/soothe2/ | secondary | 2026-06-18 | oeksound | vendor — soothe2 页(verifier=secondary) |
| T02-S016 | https://tapeop.com/reviews/gear/138/soothe2-plug-in | verified_primary | 2026-06-18 | Tape Op | soothe2 杂志评测 |
| T02-S017 | https://splice.com/ | surrogate_primary | 2026-06-18 | Splice | vendor docs — 样本订阅 + Rent-to-Own |
| T02-S018 | https://en.wikipedia.org/wiki/Yamaha_NS-10 | secondary | 2026-06-18 | — | NS-10 监听标准史 |
| T02-S019 | https://www.fabfilter.com/learn/compression/compression-techniques-bus-parallel-and-mix-bus | surrogate_primary | 2026-06-18 | FabFilter | vendor docs — bus/parallel 压缩教学(沿用 T04-S017) |
| T02-S020 | https://www.youtube.com/watch?v=wVp4syrFkE0 | reference | 2026-06-18 | Dan Worrall | 模拟 vs 数字 summing null-test 视频 |
| T02-S021 | https://www.synthtopia.com/content/2025/09/06/izotope-ozone-12-now-available/ | secondary | 2026-06-18 | Synthtopia | Ozone 12 发布(2025-09) |
| T02-S022 | https://www.production-expert.com/home-page/2017/10/11/ai-mastering-software-shoot-out | secondary | 2026-06-18 | Production Expert | AI 母带横评(LANDR/CloudBounce/Ozone) |
| T02-S023 | https://waveinformer.com/2024/12/18/fabfilter-pro-q-4-review/ | secondary | 2026-06-18 | WaveInformer | Pro-Q 4 评测 |
| T02-S024 | https://gearspace.com/board/ | reference | 2026-06-18 | Gearspace | 论坛 — null-test/选型 共识来源(沿用 T05-S006) |

注：vendor 域(fabfilter/izotope/valhalladsp/uaudio/celemony/splice)`classify` 返回 verified_primary，按 task 规则统一记 `surrogate_primary` + note 含 `vendor docs`，不冒充更强桶；sonible/oeksound `classify` 返回 secondary，如实记 secondary。

---

## 总览（按 tier 分组）

### 必备（≥ 80% 从业者用 / 行业地基）（9 个）
| 工具 | 一句话 | Decay risk | Sources |
|------|--------|------------|---------|
| Pro Tools (DAW) | 录音棚/后期录音剪辑事实标准，session 交换通用语 | low | T02-S003 |
| FabFilter Pro-Q (EQ) | 现代 ITB 默认精密 EQ，频谱+动态+M/S 全能 | low | T02-S001, T02-S023 |
| 1176 / LA-2A / SSL bus comp（含复刻） | 三件套压缩"原型"+ UAD/Waves/PA 复刻是默认配置 | low | T02-S012, T02-S019 |
| iZotope Ozone (母带套件) | ITB 母带事实默认 + AI Master Assistant 起点 | medium | T02-S004, T02-S006 |
| Valhalla 混响（VintageVerb/Room/Plate） | $50 复刻 Lexicon/EMT，被千万 producer 当参考混响 | low | T02-S011 |
| Auto-Tune / Melodyne（修音） | 修音事实双标准：实时 vs 离线外科 | low | T02-S013, T02-S014 |
| Pro-L 2 / Ozone Maximizer（限制器） | 母带末端响度限制默认选择 | medium | T02-S005 |
| 校准近场监听（Genelec / Yamaha HS / NS-10 传统） | 任何混音的"真相参考"，房间+监听优先于插件 | low | T02-S018 |
| Apollo / RME（接口/转换器） | 录音棚级 AD/DA + 低延迟，Apollo 带 UAD DSP | low | T02-S012 |

### 场景特化（特定子方向用）（8 个）
| 工具 | 一句话 | Decay risk | Sources |
|------|--------|------------|---------|
| Ableton Live | 电子/现场/编曲 producer 的默认 DAW（Session view） | low | T02-S003 |
| FL Studio | beatmaker/trap/hip-hop 的母语 DAW（pattern + piano roll） | low | T02-S003 |
| Logic Pro | Mac 性价比全能 + 内置 Stem Splitter（本地 AI） | low | T02-S003, T02-S009 |
| oeksound soothe2/3（动态共振抑制） | 外科级压刺耳/共振，混音救火必装 | medium | T02-S015, T02-S016 |
| Serum 2 / Kontakt（音源） | EDM wavetable 合成 + 采样器事实标准 | low | T02-S017 |
| Splice（样本订阅） | credit 制免版税样本库 + Rent-to-Own 拿插件 | low | T02-S017 |
| Reaper | 轻量可定制 + 极低价，post/编辑党与预算党 | low | T02-S003 |
| U47 / SM7B / SM57（话筒） | 人声电容 vs 动圈 vs 万用动圈的源头三件套 | low | T02-S018 |

### 新兴 / 实验（近 12 个月起势）（5 个）
| 工具 | 一句话 | Decay risk | Sources |
|------|--------|------------|---------|
| FabFilter Pro-Q 4（2024-12） | Pro-Q 加 Spectral Dynamics + Character 饱和 + EQ Sketch | medium | T02-S001, T02-S002 |
| iZotope Ozone 12（2025-09） | 加 Stem EQ / Bass Control / Unlimiter + IRC 5 多段限制 | high | T02-S005, T02-S021 |
| sonible smart:EQ 4（AI EQ） | AI 按音源/风格生成 EQ 曲线 + 多轨感知 | high | T02-S007, T02-S008 |
| AI stem 分离（Logic Stem Splitter / RipX / Moises / RX Rebalance） | 从立体声成品拆 stem，本地化+快 | high | T02-S009 |
| LANDR / CloudBounce / eMastered（在线 AI 母带） | 一键云母带，独立艺人/demo 用，争议中 | high | T02-S010, T02-S022 |

---

## 详细条目

### 1. Pro Tools (Avid)
- **One-liner**: Pro Tools — 录音棚与后期(film/broadcast/game)的录音+剪辑事实标准，session 交换的行业通用语。
- **Tier**: 必备
- **Maintainer / Owner**: Avid Technology — https://www.avid.com/pro-tools
- **License**: proprietary（订阅 + 永久授权混合）
- **Maturity signals**:
  - Pro studio 采用率: 37.2%（专业棚整体），post-production 63.8%（2025 Production Expert DAW survey，last checked: 2026-06-18）(evidence: [T02-S003])
  - First public release: 1991（Sound Tools 前身 1989）
  - Activity: healthy（2025.12 版本持续发布）(evidence: [T05-S016])
- **典型使用场景**: 多人协作录音棚 tracking（session 互通）；film/TV/game 后期（Pro Tools 在 post 占 ~64%，HD 系统是行业基线）；大型多轨混音剪辑。
- **不适合 / 替代方案**: 不适合 beatmaking/电子编曲（pattern 工作流弱）→ 用 Ableton/FL；预算受限/个人 → Reaper、Logic。
- **生产案例**: 绝大多数商业录音棚以 Pro Tools 为交付格式标准；post 行业 ~64% 占有率即生产证据 (evidence: [T02-S003])。
- **近期变化（近 12 个月）**: 持续加 Dolby Atmos / 沉浸式工作流（与 T05 sources 标注的 Atmos 趋势一致）(evidence: [T05-S016])。
- **可信度**: high
- **Decay risk**: low（行业地基，30+ 年；24+ 月被取代概率 < 20%）

### 2. FabFilter Pro-Q (EQ)
- **One-liner**: Pro-Q — 现代 ITB 默认精密 EQ，频谱可视 + 动态 EQ + M/S + 线性相位全能，Dan Worrall 教程核心对象。
- **Tier**: 必备（同时 Pro-Q 4 进新兴层，见条目 12）
- **Maintainer / Owner**: FabFilter — https://www.fabfilter.com
- **License**: proprietary（永久授权，EUR 169 / USD 179，官方价 2024-12）(evidence: [T02-S002])
- **Maturity signals**:
  - Pro-Q 4 release: 2024-12-12（last checked: 2026-06-18）(evidence: [T02-S002])
  - Activity: healthy（4.02 维护更新）(evidence: [T02-S023])
- **典型使用场景**: 减法 EQ 清 mud/harsh（与 canon"subtractive"一致）；动态 EQ 控齿音/共振；母带宽窄带精修。
- **不适合 / 替代方案**: 想要硬件染色/"音色" → 用建模 EQ（SSL/API/Pultec 复刻）；想 AI 自动出曲线 → sonible smart:EQ 4。
- **维护者背景（sub_skill_link）**: Dan Worrall 曾为 FabFilter 制作官方教程（→ Track 01/05 figure，T05-S003、T04-S011 链路）。
- **可信度**: high
- **Decay risk**: low（已是 ITB EQ 默认；24+ 月稳定概率高）

### 3. 1176 / LA-2A / SSL bus compressor（原型 + 复刻生态）
- **One-liner**: 三件套压缩"原型"（FET 快/光学慢/总线胶水）+ UAD/Waves/Plugin Alliance/IK/Acustica 复刻，是几乎所有混音的默认动态配置。
- **Tier**: 必备
- **Maintainer / Owner**: 硬件 = Universal Audio (1176/LA-2A) / Solid State Logic (bus comp)；复刻 = UAD、Waves、Plugin Alliance、IK Multimedia、Black Rooster、Acustica
- **License**: proprietary（各家）
- **Maturity signals**:
  - 共识基准: UAD 1176 Classic Limiter Collection "是衡量其他 1176 插件的标准"（业内，last checked: 2026-06-18）(evidence: [T02-S024])
  - SSL bus comp: Acustica Sand / Plugin Alliance bx_townhouse(约 $30) 是常被点名的高保真复刻（业内）(evidence: [T02-S024])
- **典型使用场景**: 1176（FET）— 人声/鼓 快瞬态、并行压缩"all-buttons"；LA-2A（光学）— 人声/贝斯 平滑垫底；SSL bus comp — 总线"glue"胶水压缩（与 canon mix-bus glue 概念一致）(evidence: [T02-S019])。
- **不适合 / 替代方案**: 透明动态控制 → FabFilter Pro-C 2 / Pro-MB；不需要染色就别上建模压缩（CPU + 玄学）。
- **生产案例**: 并行压缩(NY compression)起于 1970-80s 纽约棚的 SSL/1176 重压劈分（canon T04-S018/S017 已记），复刻链是其 ITB 实现。
- **可信度**: high（基准款），复刻排名 medium（论坛共识，非盲测裁决）
- **Decay risk**: low（建模原型 50+ 年不变）

### 4. iZotope Ozone（母带套件 + AI Master Assistant）
- **One-liner**: Ozone — ITB 母带事实默认套件，AI Master Assistant 分析输入/参考曲生成 genre-specific 起点 preset。
- **Tier**: 必备（Ozone 12 进新兴层，见条目 13）
- **Maintainer / Owner**: iZotope (Native Instruments / Soundwide) — https://www.izotope.com
- **License**: proprietary（Standard/Advanced，约 $299–$499，业内常报价）(evidence: [T02-S022])
- **Maturity signals**:
  - SOS 评测 Ozone 11 Advanced "future-proof"（last checked: 2026-06-18）(evidence: [T02-S006])
  - Ozone 12 release: 2025-09（evidence: [T02-S021]）
  - Activity: healthy
- **典型使用场景**: 个人/卧室母带的全链路一站（EQ→动态→imaging→maximizer）；Master Assistant 给非母带专精者一个可 A/B 的起点；命中 LUFS/true-peak 上限（canon LUFS 概念）。
- **不适合 / 替代方案**: 顶级专业母带师仍偏 outboard + 校准房 + 手动链（Ozone 被批"有时偏 harsh/digital"，需用耳朵 A/B）(evidence: [T02-S006])；纯一键省事 → 在线 AI 母带(LANDR)。
- **生产案例**: 大量独立母带工程师/混音师把 Ozone 作 ITB 母带主链（SOS 长期评测背书）(evidence: [T02-S006])。
- **近期变化（近 12 个月）**: Ozone 12（2025-09）加 Stem EQ / Bass Control / Unlimiter + IRC 5 多段限制 + Master Assistant 自定义页（见条目 13）(evidence: [T02-S005, T02-S021])。
- **可信度**: high
- **Decay risk**: medium（AI 模块迭代快，但套件地位稳；12-24 月显著改变 20-40%）

### 5. Valhalla 混响（VintageVerb / Room / Plate / Delay）
- **One-liner**: Valhalla — $50 算法混响，复刻 Lexicon 224/EMT/AMS/Bricasti 风味，被海量 producer/混音师当作"参考混响"。
- **Tier**: 必备
- **Maintainer / Owner**: Valhalla DSP（Sean Costello）— https://valhalladsp.com
- **License**: proprietary（VintageVerb 约 $50，官方价）(evidence: [T02-S011])
- **Maturity signals**:
  - 行业认可: "成为千万 producer 与混音师的参考混响"，"无更好价值"（业内/vendor docs，last checked: 2026-06-18）(evidence: [T02-S011])
  - Activity: healthy（Valhalla DSP bundle 持续维护）
- **典型使用场景**: 人声 plate/hall；房间感 Room；复古 70-80s 数字混响色彩；替代昂贵 Lexicon PCM / Bricasti 硬件箱。
- **不适合 / 替代方案**: 顶级真实卷积空间 → Altiverb/IR；硬件 mojo 党 → Bricasti M7 实体；想要现代透明 → FabFilter Pro-R 2。
- **生产案例**: 被广泛报道可替代 Lexicon PCM、TC M3000、Eventide H3000、Bricasti 箱（业内）(evidence: [T02-S011])。
- **可信度**: high
- **Decay risk**: low（算法混响地基，价格+口碑护城河）

### 6. Auto-Tune (Antares) / Melodyne (Celemony)（修音）
- **One-liner**: 修音事实双标准 — Auto-Tune = 实时/iconic 音染快修（pop/hip-hop），Melodyne = 离线"外科"透明修 + 复音(polyphonic)。
- **Tier**: 必备
- **Maintainer / Owner**: Antares Audio (Auto-Tune) / Celemony (Melodyne) — https://www.celemony.com
- **License**: proprietary（双方均订阅+永久）
- **Maturity signals**:
  - SOS 对比定性: "Auto-Tune 仍是 pitch correction 行业标准"，"Melodyne 在透明修音/复音上多数工程师给优势"（last checked: 2026-06-18）(evidence: [T02-S014])
  - Melodyne 独占能力: 复音编辑（和声/吉他/钢琴），Auto-Tune 无法（evidence: [T02-S014]）
- **典型使用场景**: Auto-Tune — 现场/录音实时修 + T-Pain 式音染效果（hip-hop/modern pop）；Melodyne — 离线逐音修 sustained note/呼吸/复音素材（acoustic/jazz/合唱）；time-align/手动修时值。
- **不适合 / 替代方案**: 想要"听不出"修音 → Melodyne（伪影少）；要实时表演 → Auto-Tune（Melodyne 不能实时）(evidence: [T02-S014])。
- **争议接口**: 修音=艺术工具 vs 作弊（canon Auto-Tune 之争，→ Phase 2 智识谱系）。
- **可信度**: high
- **Decay risk**: low（双标准格局 10+ 年稳定）

### 7. 限制器: FabFilter Pro-L 2 / iZotope Ozone Maximizer
- **One-liner**: 母带/总线末端响度限制的默认选择 — Pro-L 2（透明、可视、多算法）与 Ozone Maximizer（IRC 系列算法）。
- **Tier**: 必备
- **Maintainer / Owner**: FabFilter (Pro-L 2) / iZotope (Maximizer) — vendor docs
- **License**: proprietary
- **Maturity signals**:
  - Ozone 12 Maximizer 加 IRC 5 四段多带限制（减少 pumping/互调失真，2025-09，last checked: 2026-06-18）(evidence: [T02-S005, T02-S021])
  - Activity: healthy
- **典型使用场景**: 命中 streaming LUFS/true-peak 上限（≈-14 LUFS / -1 dBTP，canon 概念）同时保动态；总线增益冲顶；防 true-peak 削波。
- **不适合 / 替代方案**: 重染色/胶水 → 用总线压缩而非限制器先上；超激进响度 → 但 normalization 时代不划算（见避坑）。
- **可信度**: high
- **Decay risk**: medium（限制器算法仍在迭代，IRC 5 即例）

### 8. 校准近场监听（Genelec / Yamaha HS / NS-10 传统）+ 声学处理
- **One-liner**: 任何混音的"真相参考"系统 — 校准近场监听 + 房间处理优先于任何插件（Senior 第一性教学）。
- **Tier**: 必备
- **Maintainer / Owner**: Genelec / Yamaha / Adam / Focal 等
- **License**: hardware (proprietary)
- **Maturity signals**:
  - NS-10 获 2007 Technical Grammy，"近场监听界的 SM57"，挺过 Genelec/Mackie/Focal 多轮潮流（last checked: 2026-06-18）(evidence: [T02-S018])
  - Genelec 自带 GLM 房间校准（业内）
- **典型使用场景**: NS-10 — 中频"刺耳即真相"的传统横监听校验；Genelec/HS — 现代全频+自动校准主监听；多系统 + 耳机 cross-check（canon"理解房间的谎言"）。
- **不适合 / 替代方案**: 房间未处理时贵箱无意义 → 先做声学处理 + 用 reference track；纯耳机混 → Sonarworks/校准耳机配置。
- **生产案例**: NS-10 几十年作录音棚 de-facto 中场参考（Wikipedia 史料）(evidence: [T02-S018])。
- **可信度**: high
- **Decay risk**: low（监听校准纪律是永恒基本功）

### 9. Apollo / RME（接口 / 转换器）
- **One-liner**: 录音棚级 AD/DA 转换 + 低延迟驱动 — Apollo 带板载 UAD DSP（录音时挂建模），RME 以驱动稳定/低延迟著称。
- **Tier**: 必备
- **Maintainer / Owner**: Universal Audio (Apollo) — https://www.uaudio.com / RME Audio
- **License**: hardware + proprietary DSP
- **Maturity signals**: UAD/Apollo 主站持续上新（vendor docs，last checked: 2026-06-18）(evidence: [T02-S012])
- **典型使用场景**: Apollo — 录音时 UAD DSP 实时挂 1176/LA-2A 监听；RME — 高轨数稳定录音 + TotalMix 路由；任何需要可靠时钟/低 latency 的 tracking。
- **不适合 / 替代方案**: 纯 ITB 不录音/预算紧 → Focusrite Scarlett、Audient；不需要 UAD 生态 → RME/MOTU。
- **可信度**: high（接口）；DSP 生态 medium（绑 UAD 商业模型）
- **Decay risk**: low（转换器/接口 8+ 年迭代慢）

### 10. Ableton Live（场景特化 — 电子/现场/编曲）
- **One-liner**: Ableton Live — Session view 即兴编曲 + 现场表演 + 电子制作的默认 DAW，独立/卧室 producer 偏好榜首。
- **Tier**: 场景特化
- **Maintainer / Owner**: Ableton — https://www.ableton.com
- **License**: proprietary
- **Maturity signals**: SMC 2025 study 把 Ableton 列整体偏好榜首（消费/独立群体），ProducerHive 测 Ableton+FL+Logic 合占 ~58% 消费用户基（业内，last checked: 2026-06-18）(evidence: [T02-S003])
- **典型使用场景**: 电子/EDM 编曲与 sound design；现场演出（warping/clip launching）；快速 loop-based 草图。
- **不适合 / 替代方案**: 大型多轨录音棚交付 → Pro Tools；古典/线性编辑 → 弱于 Cubase/Logic。
- **可信度**: high
- **Decay risk**: low

### 11. FL Studio（场景特化 — beatmaker / trap / hip-hop）
- **One-liner**: FL Studio — pattern + piano roll 工作流，beatmaker/trap/hip-hop producer 的"母语"DAW，终身免费升级。
- **Tier**: 场景特化
- **Maintainer / Owner**: Image-Line — https://www.image-line.com
- **License**: proprietary（lifetime free updates）
- **Maturity signals**: FL 在消费/独立 producer 群体高占有（与 Ableton/Logic 合 ~58%），In The Mix(T05-S017) 等频道默认 DAW（last checked: 2026-06-18）(evidence: [T02-S003])
- **典型使用场景**: trap/hip-hop beat 编程（step sequencer + piano roll 业内公认强）；快速 loop 制作；卧室 producer 入门。
- **不适合 / 替代方案**: 录音棚多轨录音/post → Pro Tools；线性长曲剪辑 → Logic/Cubase。
- **维护者背景（sub_skill_link）**: 与 In The Mix(Michael Wynne, FL 默认导师) 关联（T05-S017）。
- **可信度**: high
- **Decay risk**: low

### 12. Logic Pro（场景特化 — Mac 性价比 + 内置本地 AI Stem Splitter）
- **One-liner**: Logic Pro — Mac 上 $200 一次性买断的全能 DAW，Logic 11(2024) 内置本地 Stem Splitter（Apple Silicon 几十秒拆一首）。
- **Tier**: 场景特化
- **Maintainer / Owner**: Apple — https://www.apple.com/logic-pro/
- **License**: proprietary（一次性买断）
- **Maturity signals**:
  - 专业棚 12.6%（仅次 Pro Tools），消费群体高（2025 DAW survey，last checked: 2026-06-18）(evidence: [T02-S003])
  - Stem Splitter（Logic 11, 2024）本地跑，3 分钟曲约 20–40 秒（evidence: [T02-S009]）
- **典型使用场景**: Mac 全能制作（自带乐器/采样）；本地 stem 拆分（隐私+快，不上传云）；性价比卧室棚。
- **不适合 / 替代方案**: 跨平台/Windows → 无（Mac 独占）；录音棚交付 → Pro Tools。
- **可信度**: high
- **Decay risk**: low

### 13. oeksound soothe2 / soothe3（场景特化 — 动态共振抑制）
- **One-liner**: soothe — 外科级动态共振抑制器，自动盯住刺耳/共振频段按需压下，是混音"救火"的近必装。
- **Tier**: 场景特化
- **Maintainer / Owner**: oeksound — https://oeksound.com
- **License**: proprietary
- **Maturity signals**:
  - Tape Op 杂志专门评测 soothe2（last checked: 2026-06-18）(evidence: [T02-S016])
  - soothe3 加 low-latency tracking mode（可在录音/耳机混时常驻，2026 评测）(evidence: [T02-S015])
- **典型使用场景**: 压人声齿音/鼻音共振；驯 overhead/吉他的刺耳；母带宽频去 harsh（与 FabFilter Pro-Q 动态/Gullfoss 是同类竞品 — soothe=外科精准，Gullfoss=整体平衡）。
- **不适合 / 替代方案**: 想要整体音色平衡而非外科去共振 → SoundTheory Gullfoss；预算紧 → Pro-Q 4 Spectral Dynamics 部分覆盖。
- **可信度**: high
- **Decay risk**: medium（已成混音常备，但 Pro-Q 4 Spectral Dynamics 侵蚀其部分场景）

### 14. Serum 2 (Xfer) / Kontakt (NI)（场景特化 — 音源）
- **One-liner**: Serum = EDM wavetable 合成事实标准（Serum 2 加 granular/spectral/multisample）；Kontakt = 采样器/音色库平台事实标准。
- **Tier**: 场景特化
- **Maintainer / Owner**: Xfer Records (Serum) / Native Instruments (Kontakt) — Serum 经 Splice 分发
- **License**: proprietary（Serum 2 可经 Splice Rent-to-Own）
- **Maturity signals**: Serum 2 经 Splice Rent-to-Own 分发，加第三振荡器 + granular/spectral/multisample（last checked: 2026-06-18）(evidence: [T02-S017])
- **典型使用场景**: Serum — EDM/trap/pop 合成 bass/lead/pad；Kontakt — 加载商业音色库（管弦/民族/鼓）。
- **不适合 / 替代方案**: 模拟建模合成 → Diva/Pigments；轻量 → 自带 DAW 合成器。
- **可信度**: high
- **Decay risk**: low

### 15. Splice（场景特化 — 样本订阅 + 插件 Rent-to-Own）
- **One-liner**: Splice — credit 制免版税样本/loop/preset 库 + Rent-to-Own 分期拿插件，现代 beatmaker/producer 的事实素材源。
- **Tier**: 场景特化
- **Maintainer / Owner**: Splice — https://splice.com
- **License**: SaaS 订阅（credit 制）
- **Maturity signals**: "行业领先免版税样本目录"，credit 按需下载 + Rent-to-Own 拿 Serum 2 等（vendor docs，last checked: 2026-06-18）(evidence: [T02-S017])
- **典型使用场景**: 找鼓/loop/one-shot/MIDI/preset；按需付费而非买整包；分期拿贵插件。
- **不适合 / 替代方案**: 要独家/原创音色 → 自录 + sound design；一次买断包 → Loopmasters/各厂直售。
- **可信度**: high
- **Decay risk**: low

### 16. Reaper（场景特化 — 轻量可定制 + 极低价）
- **One-liner**: Reaper — 极轻量、可深度脚本定制、$60-225 授权的 DAW，post/编辑党与预算党的高性价比之选。
- **Tier**: 场景特化
- **Maintainer / Owner**: Cockos — https://www.reaper.fm
- **License**: proprietary（个人 $60，商业 $225，60 天试用宽松）
- **Maturity signals**: 专业棚 7.4%、post 与 Nuendo 并列 10.1%（2025 DAW survey），SMC 2025 把 Reaper 列偏好前列（last checked: 2026-06-18）(evidence: [T02-S003])
- **典型使用场景**: 大量音频编辑/post（脚本+宏）；预算紧的全能录音混音；自定义工作流极客。
- **不适合 / 替代方案**: 要行业 session 交换标准 → Pro Tools；要开箱即用乐器音色 → Logic/Ableton。
- **可信度**: high
- **Decay risk**: low

### 17. 话筒: U47 / SM7B / SM57（场景特化 — 源头）
- **One-liner**: 源头三件套 — U47（人声大膜片电容旗舰）/ SM7B（人声/口播动圈）/ SM57（万用动圈，乐器/鼓/吉他箱）。
- **Tier**: 场景特化
- **Maintainer / Owner**: Neumann (U47) / Shure (SM7B, SM57)
- **License**: hardware
- **Maturity signals**: SM57 "可能是世上最万用的麦"，SM7B 录 MJ《Thriller》人声成名（last checked: 2026-06-18）(evidence: [T02-S018])
- **典型使用场景**: U47 — 高端人声/复古色彩；SM7B — 嘶吼人声/口播/抗噪环境；SM57 — 军鼓/吉他箱/万用补位。
- **不适合 / 替代方案**: 预算 → SM57/SM58 起步；高解析现代人声 → 其他电容(TLM103/U87 等)。
- **可信度**: high
- **Decay risk**: low（话筒经典型号几十年不变）

### 18. FabFilter Pro-Q 4（新兴 — 2024-12）
- **One-liner**: Pro-Q 4（2024-12-12）— 业界默认 EQ 大升级，加 Spectral Dynamics（按频段超阈值压/扩）+ Character 饱和模式 + EQ Sketch 画曲线 + Instance List 多实例总览。
- **Tier**: 新兴
- **Maintainer / Owner**: FabFilter — https://www.fabfilter.com
- **License**: proprietary（EUR 169 / USD 179，官方价 2024-12）(evidence: [T02-S002])
- **Maturity signals**:
  - First release: 2024-12-12（last checked: 2026-06-18）(evidence: [T02-S002])
  - 4.02 维护更新已出（evidence: [T02-S023]）
  - Activity: healthy
- **典型使用场景**: Spectral Dynamics 替代部分 soothe2/Gullfoss 场景（动态压共振）；Character 模式给数字 EQ 加 transformer/tube 饱和；EQ Sketch 快速画目标曲线。
- **不适合 / 替代方案**: 要 AI 自动出曲线 → smart:EQ 4；纯外科去共振仍偏 soothe2/3。
- **近期变化**: 即此版本本身（2024-12）。
- **可信度**: high
- **stability**: 较稳（FabFilter 旗舰续作，非新厂；但作"近 12 月新版本"归新兴层）
- **Decay risk**: medium（版本会再迭代，但 Pro-Q 系列地位稳；12-24 月被显著改变 20-40%）

### 19. iZotope Ozone 12（新兴 — 2025-09）
- **One-liner**: Ozone 12（2025-09）— 母带套件加 Stem EQ（成品内分轨 EQ）+ Bass Control（ML 低频）+ Unlimiter（ML 恢复被压扁动态）+ Maximizer IRC 5 四段限制 + Master Assistant 可定制页。
- **Tier**: 新兴
- **Maintainer / Owner**: iZotope — https://www.izotope.com
- **License**: proprietary
- **Maturity signals**:
  - First release: 2025-09（last checked: 2026-06-18）(evidence: [T02-S021])
  - Activity: healthy（release notes 持续）(evidence: [T02-S005])
- **典型使用场景**: Stem EQ 在立体声成品上单独修人声/鼓/贝斯（免回混）；Unlimiter 救被过压的素材；IRC 5 降 pumping。
- **不适合 / 替代方案**: 顶级专业母带仍偏手动链 + outboard；纯一键 → 在线 AI 母带。
- **近期变化**: 即此版本本身。
- **可信度**: high
- **stability**: experimental-ish（ML 模块新，6-12 月内会有 patch/争议沉淀）
- **Decay risk**: high（新 AI 模块默认 high；ML 行为可能随版本显著变）

### 20. sonible smart:EQ 4（新兴 — AI EQ）
- **One-liner**: smart:EQ 4 — AI 分析音源自动生成定制 EQ 曲线（21 乐器/人声档 + 22 风格档）+ 多轨感知 + 动态模式 + auto-gain，"未来的 EQ"。
- **Tier**: 新兴
- **Maintainer / Owner**: sonible — https://www.sonible.com
- **License**: proprietary
- **Maturity signals**:
  - MusicTech 评 "a look at the future of AI mixing"，风格档由上代 14 增至 22（last checked: 2026-06-18）(evidence: [T02-S008, T02-S007])
  - 24 段 + 全局/逐段 M/S + minimal/linear phase
- **典型使用场景**: 快速给单轨出可用 EQ 起点；多轨感知避免频段打架；新手在繁忙编曲中开空间。
- **不适合 / 替代方案**: 要完全手动精控/可视频谱 → FabFilter Pro-Q 4；要外科去共振 → soothe2/3。
- **早期采用者**: MusicTech/Magnetic/Audio Plugin Guy 等独立媒体评测背书（evidence: [T02-S008]）。
- **可信度**: medium-high
- **stability**: experimental（AI EQ 类目仍在快速演进）
- **Decay risk**: high（AI 算法 + 类目竞争激烈；12 月内显著改变概率 > 40%）

### 21. AI Stem 分离（Logic Stem Splitter / RipX / Moises / RX Music Rebalance / Lalal.ai）
- **One-liner**: 从立体声成品拆出 vocal/drums/bass/other stem 的 AI 引擎群 — Logic 11 本地、RipX 买断、Moises/Lalal 云、RX Rebalance 后期修复。
- **Tier**: 新兴
- **Maintainer / Owner**: Apple (Logic Stem Splitter) / Hit'n'Mix (RipX) / Moises / iZotope RX / Lalal.ai
- **License**: 混合（Logic 内置 / RipX 买断 ~$99-299 / Moises·Lalal 订阅）
- **Maturity signals**:
  - MusicTech 横评 9 款引擎，质量随曲目/引擎差异大（last checked: 2026-06-18）(evidence: [T02-S009])
  - Logic 11 本地 stem splitter（Apple Silicon，3 分钟约 20-40 秒）(evidence: [T02-S009])
- **典型使用场景**: 无 stem 的老曲重混/采样；DJ remix；修复（拆出再单独处理）；rebalance 救混音。
- **不适合 / 替代方案**: 有原始多轨时永远用多轨（分离仍有伪影）；高保真母带级 → 慎用（伪影进母带）。
- **可信度**: medium（质量依赖素材）
- **stability**: experimental（模型月级迭代）
- **Decay risk**: high（AI 模型快速进步，今天最好的 6 月后可能被超）

### 22. 在线 AI 母带（LANDR / CloudBounce / eMastered）
- **One-liner**: 一键云母带服务，独立艺人/demo/快交付用 — 上传得母带，争议中（craft vs 自动化）。
- **Tier**: 新兴（虽 LANDR 2014 起，但 AI 母带"是否毁 craft"的争论是近年持续热点）
- **Maintainer / Owner**: LANDR / CloudBounce / eMastered
- **License**: SaaS 订阅（LANDR $4-25/月；CloudBounce $9.90/单或 $19.99/月，业内报价）(evidence: [T02-S010, T02-S022])
- **Maturity signals**:
  - SOS 专文论 LANDR/CloudBounce 与母带的未来（last checked: 2026-06-18）(evidence: [T02-S010])
  - 电子/EDM 上表现较好（处理压缩合成音），rock/metal 上 Ozone 混合法更稳（业内横评）(evidence: [T02-S022])
- **典型使用场景**: 独立艺人 demo/快速发行；批量曲；预算极紧无母带师。
- **不适合 / 替代方案**: 重要商业发行 → 人工母带师；要可控/可学 → Ozone（AI 起点 + 手调）。
- **争议接口**: AI 母带是否"毁了 craft"（canon/sources 标注的热议，→ Phase 2 智识谱系 + 诚实边界）。
- **可信度**: medium（依风格/曲目波动）
- **stability**: experimental（算法持续变）
- **Decay risk**: high

---

## 选型决策树

### 决策树 A: 你处在 pipeline 的哪一环 + 核心瓶颈是什么？

#### Branch 1: 选 DAW（你的核心制作类型是什么？）
##### Branch 1a: 录音棚多轨录音 / 要和别人交换 session / film·TV·game post
→ 推荐: **Pro Tools**（行业交换标准；post ~64% 占有率）(evidence: [T02-S003])
→ 不推荐: FL Studio（pattern 工作流不适合线性多轨录音棚交付）
→ 真实案例: post-production 行业 Pro Tools 63.8% 即选型共识 (evidence: [T02-S003])
##### Branch 1b: 电子 / 现场 / loop 编曲
→ 推荐: **Ableton Live**（Session view + warping；独立群体偏好榜首）(evidence: [T02-S003])
##### Branch 1c: trap / hip-hop beat
→ 推荐: **FL Studio**（piano roll + step sequencer 母语工作流）(evidence: [T02-S003])
##### Branch 1d: Mac 性价比全能 / 想要本地 stem 拆分
→ 推荐: **Logic Pro**（$200 买断 + 内置本地 Stem Splitter）(evidence: [T02-S003, T02-S009])
##### Branch 1e: 预算极紧 / 极客可定制 / 大量编辑
→ 推荐: **Reaper**（$60，脚本化）(evidence: [T02-S003])
> 现实: 多 DAW 工作流已常态（Ableton 编曲 → Pro Tools 录混 → Studio One 母带）(evidence: [T02-S003])。不要纠结"唯一 DAW"。

#### Branch 2: 混音阶段，主要瓶颈在哪？
##### Branch 2a: 频段问题（mud / harsh / 共振）
→ 第一性: 先**减法 EQ**（FabFilter Pro-Q）+ reference A/B（canon 共识）
→ 共振/刺耳救火: **soothe2/3**（外科）或 **Gullfoss**（整体平衡）或 **Pro-Q 4 Spectral Dynamics** (evidence: [T02-S015, T02-S001])
→ 不推荐: 一上来到处 boost（违背 subtractive 原则）
##### Branch 2b: 动态 / 厚度
→ 推荐: 1176（FET 快瞬态）/ LA-2A（光学平滑）/ SSL bus comp（总线 glue）或其 UAD/PA 复刻 (evidence: [T02-S024, T02-S019])
→ 想加厚不压扁瞬态: **并行压缩**（canon NY compression）(evidence: [T02-S019])
→ 透明控制: FabFilter Pro-C 2
##### Branch 2c: 人声修音
→ 实时/音染（pop·hip-hop）: **Auto-Tune** ；离线透明/复音（acoustic·jazz·合唱）: **Melodyne** (evidence: [T02-S014])
##### Branch 2d: 空间
→ 推荐: **Valhalla VintageVerb/Room**（$50，参考混响）(evidence: [T02-S011])

#### Branch 3: 母带阶段
##### Branch 3a: 想自己 ITB 母带 + 要可学可控
→ 推荐: **iZotope Ozone**（Master Assistant 给起点 → 手调），末端 **Pro-L 2 / Maximizer** 命中 LUFS/true-peak 上限优先保动态 (evidence: [T02-S006, T02-S005])
→ 必配: 校准监听 + reference A/B（响度匹配后）
##### Branch 3b: demo / 独立快发行 / 预算极紧
→ 推荐: **LANDR/CloudBounce**（电子风更稳），但 A/B 原始 + 知道它会偏 harsh (evidence: [T02-S010, T02-S022])
→ 不推荐: 重要商业发行只靠一键 AI（见避坑）
##### Branch 3c: 重要商业发行
→ 推荐: 人工母带师 / 校准房 + 手动链；AI 仅作起点

#### Branch 4: 录音/源头（tracking）
→ 接口/转换器: **Apollo**（要录音挂 UAD DSP）或 **RME**（要稳定低延迟）(evidence: [T02-S012])
→ 话筒: U47/电容（高端人声）· SM7B（抗噪人声）· SM57（万用乐器）(evidence: [T02-S018])
→ 第一性: 房间未处理时先做声学处理 + 校准监听，再谈贵箱 (evidence: [T02-S018])

---

## 避坑清单

- ❌ **不要为"更响"在母带过压**: normalization 时代 streaming 按 ≈-14 LUFS 回放，过压只换来动态损失不换响度（canon LUFS/响度战争；SOS 论证）(evidence: [T02-S010])。
- ❌ **不要把一键 AI 母带(LANDR/Ozone Assistant)的输出当成品直接发**: AI 母带/Assistant 是"起点"不是"终点"，被批偏 harsh/digital，必须 A/B 原始 + 用耳朵校（evidence: [T02-S006, T02-S010]）。
- ❌ **不要在没处理的房间里相信贵监听**: NS-10/Genelec 再好，房间不处理 = 听到的全是房间的谎言；先声学处理 + reference track (evidence: [T02-S018])。
- ❌ **不要迷信"模拟 summing/硬件 warmth"而忽略盲测**: Dan Worrall null-test 显示干净模拟 summing 与 ITB 在 level-match 后基本抵消；"mojo"多来自饱和/染色而非 summing 本身——别为安慰剂买单（ITB vs analog 争论）(evidence: [T02-S020, T05-S003])。
- ❌ **不要用 AI stem 分离去替代原始多轨**: 有多轨永远用多轨；分离仍有伪影，进母带链会放大（evidence: [T02-S009]）。
- ❌ **不要把 Auto-Tune 当 Melodyne 用（反之亦然）**: Auto-Tune 不能编辑复音(和声/钢琴/吉他)，要复音/透明逐音修必须 Melodyne；要实时表演必须 Auto-Tune (evidence: [T02-S014])。
- ❌ **不要堆插件代替"录好源头"**: canon 共识"录好源头 = 混音成功一半"，先 mic 选型/摆位/房间，而非 we'll-fix-it-in-the-mix（→ Track 03/04 链路）。

---

## Phase 2 提炼提示

**反复出现 ≥ 3 source 都强调的「工具选型原则」**（候选 playbook 规则）:
- **工具服从于 pipeline 阶段与瓶颈，而非"最好的工具"**: 选型先问"哪一环、什么瓶颈"再选工具（出现于决策树全树，跨 T02-S003 DAW survey 多 DAW 共存 / canon 第一性）。
- **AI/自动工具是"起点"不是"终点"，永远 A/B + 用耳朵**: Ozone Assistant / smart:EQ / LANDR / stem 分离 都需人工校（出现于: T02-S006 / T02-S008 / T02-S010 / T02-S009）。
- **源头/房间/监听优先于插件**: 录好源 + 校准监听 + reference > 后期补救（出现于: T02-S018 / canon T04-S001 / 避坑）。
- **normalization 时代保动态 > 冲响度**: 限制器命中 LUFS/true-peak 上限即可（出现于: T02-S010 / canon LUFS / T02-S005）。

**显著的工具流派分裂**（候选 智识谱系条目）:
- **ITB 全数字派**（代表工具: FabFilter/Valhalla/Ozone 全插件链；代表人物: Andrew Scheps 已基本 ITB 化、Dan Worrall 反玄学）**vs 模拟硬件 outboard 派**（代表: UA Apollo+硬件、SSL/Neve console、"mojo"/谐波染色；null-test 是其主战场）(evidence: [T02-S020, T05-S003])。
- **AI/自动化派**（smart:EQ / Ozone Assistant / LANDR / AI stem）**vs 手动 craft 派**（FabFilter 手动精控 + 人工母带师；"AI 是否毁 craft"是核心争论）(evidence: [T02-S008, T02-S010])。
- **黄金耳朵/直觉混音 vs 看表/分析仪**（与 canon 第一性张力同构：Pro-Q 频谱可视 + 校准监听 ⇄ reference A/B 用耳）。

**新兴工具信号**:
- 当前活跃 / 上升的新工具数: 5（Pro-Q 4 2024-12 / Ozone 12 2025-09 / smart:EQ 4 / AI stem 分离群 / 在线 AI 母带）。
- 12-月最显著变化: **AI 在 EQ / 母带 / stem 分离 三处同时落地**——Pro-Q 4 加 Spectral Dynamics、Ozone 12 加 ML 模块（Bass Control/Unlimiter）+ IRC 5、Logic 11 内置本地 stem splitter、sonible smart:EQ 4 多轨感知 AI。AI 从"边缘玩具"变"主流插件内置功能"。
- 出现 → 主流 速度估计: AI 辅助功能约 12-24 个月从发布到被主流套件内置（Ozone Assistant → smart:EQ → Pro-Q Spectral Dynamics 的扩散节奏）。

**冷僻 / 信号薄弱**:
- 必备层 ≥ 3? **否问题** — 9 个（远超 floor）。
- 场景特化 ≥ 5? 是 — 8 个。
- 新兴层 ≥ 2? 是 — 5 个。
- 必备层证据 ≥ 50% 采用率? 部分有硬数据（Pro Tools 37.2%/post 63.8%，DAW 多家 survey 占比），插件类多为 vendor docs + 评测 + 论坛共识（无公开"≥80% 采用率"硬 survey，本行无插件采用率官方统计——以 canon/sources 反复点名 + 评测共识替代，已如实标 caveat）。
- → **不触发** Phase 2.8「工具栈维度信号薄弱」。本行工具维度信号厚。
- **诚实边界**: 插件采用率无官方 survey（不像 DAW 有 Production Expert survey），必备层插件的"≥80%"是基于 canon 反复点名 + 多评测共识的合理推断，非硬统计；已用 `业内`/`官方价`/`约` caveat 标注。candidates explored: ~30，retained: 22。
