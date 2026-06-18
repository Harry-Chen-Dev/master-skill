# Track 03 — Workflows Research: Music Production & Mixing (音乐制作 / 混音)

> Wave 3 integration track. Seeded from ALL prior tracks: 01-figures (Scheps 3-bus / Brauer multing / CLA chains / Rubin subtractive / Finneas bedroom / Metro sample-driven), 02-tools (which tool at which stage + AI shifts), 04-canon (Senior/Owsinski/Katz SOP descriptions), 05-sources (Atmos / AI-mastering newsletter+podcast signals), 06-glossary (gain staging / headroom / LUFS / comping / dither defs + the "workflow-change seed" note feeding this track).
> Locale: global (en-primary, material-rich, NOT cold). Pipeline per intake (canonical, already scoped): arrangement/production → tracking/programming → editing (comping/quantize/pitch-correct/time-align) → mixing (gain staging → balance → EQ → compression → space → automation → bus/mix-bus) → mastering (loudness/EQ/limiting/dither/sequencing) → delivery (DDP/streaming spec/stems).
> **状态: COMPLETE** — 6 major pipeline-stage workflows + 1 cross-cutting (AI/stem) workflow = 7 retained. 见文件末尾质量自检。
> last_updated: 2026-06-18 · last_checked: 2026-06-18
>
> **Vendor 声明规则** (沿用 Track 02/04/06): 插件/DAW/Dolby 厂商 product/docs/learn 页统一记 `surrogate_primary` + note 含 `vendor docs` / `originator`，即便 `classify` 返回更强桶也不私自升级；标准机构 (ITU/EBU/AES) 才作 verified_primary。SEO-ish 厂商博客 (pitchinnovations 等) `classify` 返回 verified_primary 时，**主动降级 secondary**（黑名单逻辑外的诚实降级，task item6 允许）。

## Source Manifest

| source_id | url | bucket | last_checked | author/host | one-line note |
|-----------|-----|--------|--------------|-------------|---------------|
| T03-S001 | https://www.cambridge-mt.com/ms/main/ | verified_primary | 2026-06-18 | Mike Senior (Cambridge MT) | Mixing Secrets — balance-first SOP + free multitracks (sync T01-S003/T04-S001) |
| T03-S002 | https://www.soundonsound.com/techniques/vocal-comping-editing | verified_primary | 2026-06-18 | Sound On Sound | comping/editing canon — take-folder workflow (sync T06-S010) |
| T03-S003 | https://www.fabfilter.com/learn/compression/compression-techniques-bus-parallel-and-mix-bus | surrogate_primary | 2026-06-18 | FabFilter | vendor docs — bus/parallel/mix-bus 压缩工作流 (sync T04-S017/T02-S019) |
| T03-S004 | https://www.izotope.com/en/learn/mastering-for-streaming-platforms | surrogate_primary | 2026-06-18 | iZotope | vendor docs — LUFS/true-peak/平台 target 表 (sync T04-S020/T06-S017) |
| T03-S005 | https://support.spotify.com/us/artists/article/loudness-normalization/ | secondary | 2026-06-18 | Spotify for Artists | -14 LUFS normalization 官方文档 (de-facto first-party; sync T04-S021/T06-S003) |
| T03-S006 | https://www.soundonsound.com/techniques/end-loudness-war | verified_primary | 2026-06-18 | Sound On Sound | normalization 机制深度文 — 母带 target 改写 (sync T04-S008) |
| T03-S007 | https://tapeop.com/interviews/133/andrew-scheps | verified_primary | 2026-06-18 | Tape Op | Scheps 长访谈 — 3-bus/template/"less but knowing why" (sync T01-S001/T04-S022) |
| T03-S008 | https://www.puremix.com/blog/andrew-scheps-mix-template-2025-the-art-of-letting-go | verified_primary | 2026-06-18 | pureMix | Scheps 2025 极简 mix template "Art of Letting Go" (sync T01-S035) |
| T03-S009 | https://tapeop.com/interviews/165/finneas-oconnell | verified_primary | 2026-06-18 | Tape Op | Finneas #165 — 卧室 song-first 编曲/制作流程 (sync T01-S024) |
| T03-S010 | https://www.soundonsound.com/techniques/inside-track-metro-boomin-heroes-villains | verified_primary | 2026-06-18 | Sound On Sound | Metro Inside Track — sample-driven trap 编曲/programming 流程 (sync T01-S027) |
| T03-S011 | https://www.soundonsound.com/techniques/secrets-mix-engineers-michael-brauer | verified_primary | 2026-06-18 | Sound On Sound | Brauer multing/Brauerizing 总线工作流 (sync T01-S041) |
| T03-S012 | https://www.soundonsound.com/techniques/secrets-mix-engineers-chris-lord-alge | verified_primary | 2026-06-18 | Sound On Sound | CLA print-fast 摇滚混音链工作流 (sync T01-S037) |
| T03-S013 | https://www.izotope.com/en/learn/what-is-dithering-in-audio | surrogate_primary | 2026-06-18 | iZotope | vendor docs — dither apply-once 规则 (sync T06-S016) |
| T03-S014 | https://www.audiomaster.co.uk/ddp-mastering-format-explained/ | secondary | 2026-06-18 | Steve Kitch Mastering | DDP 交付格式 explainer (practitioner; sync T06-S015) |
| T03-S015 | https://www.production-expert.com/production-expert-1/2025-daw-survey-the-results | secondary | 2026-06-18 | Production Expert | 2025 DAW survey — 多 DAW 链路常态 (sync T02-S003) |
| T03-S016 | https://musictech.com/guides/buyers-guide/best-stem-separation-tools/ | secondary | 2026-06-18 | MusicTech | 9 款 stem 分离横评 — remix/sampling 改写 (sync T02-S009) |
| T03-S017 | https://www.soundonsound.com/techniques/landr-cloudbounce-future-mastering | verified_primary | 2026-06-18 | Sound On Sound | AI 在线母带的未来 — 母带 start-point 改写 (sync T02-S010) |
| T03-S018 | https://ralphsutton.com/dolby-atmos-standards-deliverables-2025/ | secondary | 2026-06-18 | Ralph Sutton | Atmos 2025 deliverables — ADM BWF / 48k-24bit / binaural metadata (practitioner) |
| T03-S019 | https://professional.dolby.com/product/dolby-atmos-content-creation/dolby-atmos-renderer/ | surrogate_primary | 2026-06-18 | Dolby | vendor docs / originator — Atmos Renderer / ADM BWF 母带链路 |
| T03-S020 | https://pitchinnovations.com/blog/can-ai-mix-assistants-replace-mix-engineers-top-ai-mixing-plugins-2025/ | secondary | 2026-06-18 | Pitch Innovations | AI mix assistant 作 mixing start-point (classify=verified_primary，主动降 secondary) |
| T03-S021 | https://www.izotope.com/en/learn/mastering-for-streaming-platforms | surrogate_primary | 2026-06-18 | iZotope | (= T03-S004) Master Assistant + 参考曲匹配起点 |

> 黑名单 URL 无。SEO-ish 厂商博客 T03-S020 主动降级 secondary，其 claim 仅作 playbook，不单独支撑 mental model。vendor docs (FabFilter/iZotope/Dolby) 标 surrogate_primary。

---

## 总览（按 decay risk 分组）

### High decay (12-month-class) — 1 个
| Workflow | Trigger | Output | Last_updated | 资深差异 |
|---------|---------|--------|-------------|---------|
| 7. AI/stem-driven 重混 + 起点生成 (cross-cutting) | 无原始多轨 / 想用 AI 起点加速 | 拆出的 stems + AI mix/master 起点供人工接管 | 2026-06-18 | skip(盲信 AI 输出) / optimize(本地引擎) / add(伪影 QC + null/A-B) |

### Medium decay — 3 个
| Workflow | Trigger | Output | Last_updated | 资深差异 |
|---------|---------|--------|-------------|---------|
| 4. Mixing (gain→balance→EQ→comp→space→auto→bus) | 编辑定稿的多轨，要做成可听成品 | 一版混音 print (stereo + 可选 stems) | 2026-06-18 | skip(模板预路由) / optimize(reference 全程/3-bus) / add(mono+多系统校验) |
| 5. Mastering (loudness/EQ/limit/dither/sequence) | 混音定稿，要做成可发行母带 | 母带文件 (按平台 target) + 排序/间隔 | 2026-06-18 | skip(过压冲响度) / optimize(校准监听 target-not-max) / add(true-peak 余量+一次 dither) |
| 6. Delivery (DDP/streaming spec/stems/Atmos) | 母带定稿，要交付到分发/压盘 | DDP image / WAV+元数据 / stems / ADM BWF | 2026-06-18 | skip(不留 dBTP 余量) / optimize(批量元数据脚本) / add(平台/Atmos 多格式 + ISRC/checksum) |

### Low decay — 3 个
| Workflow | Trigger | Output | Last_updated | 资深差异 |
|---------|---------|--------|-------------|---------|
| 1. Arrangement / Production (写到编曲定型) | 有了 idea/demo，要把歌的结构与情绪做出来 | 编曲定型的 session + scratch/参考 | 2026-06-18 | skip(过度编曲) / optimize(模板+音色库) / add(留 arrangement 空间给混音) |
| 2. Tracking / Programming (录音+编程) | 编曲定型，要把表演/音色固化成轨 | 录好的多轨 + DI + 节拍/programming | 2026-06-18 | skip(过度补录) / optimize(源头+话筒选型) / add(标注/命名/留 headroom) |
| 3. Editing (comping/quantize/pitch/time-align) | 录完原始多轨，要整理成"可混"素材 | comp 好、对齐、修音的干净多轨 | 2026-06-18 | skip(过度修音/量化) / optimize(take folder/批处理) / add(保留 pocket/人味) |

> 分组说明：本行业 pipeline **大部分稳态**（craft 几十年稳定）→ 多数 workflow decay risk = low/medium，**这是合法填法**（task 模板 iter8 修正）。唯一 high-decay 是 AI/stem 横切 workflow（模型月级迭代）。近 12 个月的真实改写集中在 **3 个注入点**：(a) streaming LUFS normalization 重写**母带 target**（已制度化、稳定，故 mastering 标 medium 而非 high）；(b) AI/stem 工具改写**重混/起点生成**（high）；(c) Dolby Atmos/沉浸式增加**第二条交付链路**（delivery 标 medium）。

---

## 详细卡片

### 1. Arrangement / Production（把 idea 做到编曲定型）

- **One-liner**: 把一个 idea / topline / beat 从"脑子里"做到"编曲结构与情绪都定型的 session"，决定这首歌要表达什么、用什么乐器/音色、各段落如何起承转合 —— 这是后续所有阶段服务的"歌"本身。(evidence: [T03-S009, T03-S010])
- **Trigger**: 有了一个动机（hook/和声/topline/loop/sample），或客户/艺人带来 demo，需要把它做成有完整结构的编曲。
- **Output**: 编曲定型的 DAW session（段落清晰：intro/verse/chorus/bridge/outro），主要乐器/音色铺好，scratch 人声或参考已就位，节拍/调性确定。
- **入门 SOP（minimum viable steps）**:
  1. **定结构 + 参考曲**: 选 1-2 首同 genre 商业 reference，定 BPM/调/段落骨架（serve-the-song 第一性，先想"这歌要什么"）。跳过 → 编曲漫无目的、各段落不连贯、后期推倒重来。(evidence: [T03-S001, T03-S009])
  2. **铺核心元素**: 鼓/节奏 + 低频(bass) + 和声(chords) + 主旋律/topline 四大件先到位，建立 groove。跳过 → 没有骨架就堆音色，得到"满但空"的编曲。(evidence: [T03-S010])
  3. **编曲填充与动态**: 加 ear-candy/transition/层次，做段落间的能量起伏（add/drop element）。跳过 → 全程一个能量，听众 30 秒就走神（Owsinski "interest" 第六要素）。
  4. **scratch 人声/参考人声**: 录或放占位人声，确认编曲给人声留了空间（negative space）。跳过 → 编曲塞满，进 tracking 才发现人声无处安放。(evidence: [T03-S009])
  5. **arrangement 定稿 + 清理**: 删掉不服务歌的元素（减法），命名/着色，导出参考 mix 给后续阶段。跳过 → 带着冗余进 tracking，浪费录音/编辑时间。
- **资深路径（差异点）**:
  - **skip（跳过）**: 资深人**跳过"把每个段落填满"** —— Rubin/Finneas 式减法，经验告诉他们"过度编曲"是最常见病，留白比加料更服务歌；资深人常**主动删轨**而非加轨。(evidence: [T03-S009], Rubin "reducer not producer" [T01-S021])
  - **optimize（优化）**: 资深人用**自建 session 模板 + 个人音色库/Splice 收藏**秒起骨架（不每次从空白 session 调音色）；trap/电子方向用 sample-driven 起点（Metro 式 sample chop → 编曲）。(evidence: [T03-S010, T03-S015])
  - **add（额外）**: 资深人**在编曲阶段就为混音预留空间** —— 频段分工（别让 5 件乐器都挤 200-500Hz mud 区）、动态留白、不在编曲里就把每轨推到顶。初学者忽略，资深人视其为"混音成功一半在编曲"。(evidence: [T03-S001])
- **近期变化（近 12 个月）**: **近 12 个月: 无重大流程变化（行业稳态）**。最近一次显著变化是 sample/loop 订阅（Splice）与 AI 生成 loop 的普及降低了"从零编曲"的门槛，但核心"定结构→铺四大件→做动态→减法"流程 5-10 年稳定。触发事件类型: 新工具（渐进式，非颠覆）。(evidence: [T03-S015, T03-S016])
- **典型耗时**:
  - 入门 SOP: 数小时 ~ 数天（单曲）
  - 资深路径: 数十分钟 ~ 1 天（模板 + 音色库加速）
- **关键工具（与 Track 02 关联）**: Ableton Live（编曲/电子，必备级场景）、FL Studio（trap/hip-hop beat，必备级场景）、Logic Pro（Mac 全能）、Splice（样本/loop 订阅，必备素材源）、Serum 2/Kontakt（音源）。
- **关键人物（与 Track 01 关联）**: Finneas（卧室 song-first，Tape Op #165 详谈）、Metro Boomin（sample-driven trap 编曲，SOS Inside Track）、Rick Rubin（减法编曲哲学）、Max Martin（"melodic math" 结构工程）。
- **常见失败模式**:
  - **过度编曲（over-arranging）**: 触发原因 = 怕"太空"而不停加层。**CLI 化暗示**: 检查项「这首歌每个段落是否都有可删的轨？删掉后歌是否更强？如果舍不得删，先静音 30% 的轨听一遍」。
  - **频段拥堵种在编曲里**: 触发原因 = 多件乐器同占 200-500Hz / 2-5kHz，到混音才发现 mud/harsh 无解。**CLI 化暗示**: 检查项「核心四大件是否各占不同频域？bass 和 kick 是否分工（一个占 sub、一个占 punch）？」。
  - **没给人声留空间**: 触发原因 = 器乐编曲塞满，topline 进来无处落位。**CLI 化暗示**: 检查项「放 scratch 人声进编曲，人声是否清晰浮在上面？还是被器乐淹没？」。
- **来源** (≥ 3):
  - [verified_primary] Finneas Tape Op #165 卧室 song-first 流程: https://tapeop.com/interviews/165/finneas-oconnell (collected: 2026-06-18) (evidence: [T03-S009])
  - [verified_primary] Metro Boomin SOS Inside Track sample-driven 编曲: https://www.soundonsound.com/techniques/inside-track-metro-boomin-heroes-villains (evidence: [T03-S010])
  - [verified_primary] Senior Mixing Secrets（编曲为混音预留空间）: https://www.cambridge-mt.com/ms/main/ (evidence: [T03-S001])
  - [secondary] 2025 DAW survey（多 DAW 编曲链路）: https://www.production-expert.com/production-expert-1/2025-daw-survey-the-results (evidence: [T03-S015])
- **Last_updated**: 2026-06-18（基于 Finneas Tape Op #165, 2025-01 为最新一手描述）
- **Decay risk**: low（编曲流程几十年稳态；工具渐变不改核心步骤）

---

### 2. Tracking / Programming（录音 + 编程把表演固化成轨）

- **One-liner**: 把编曲里的乐器/人声/节拍从"虚拟/草稿"固化成真实录音轨或编程 MIDI/采样轨 —— 这一步的源头质量直接决定混音上限（"录好源头 = 混音成功一半"）。(evidence: [T03-S001])
- **Trigger**: 编曲定型，需要把每个声部录成可用音频（话筒/DI 录音）或编程做实（鼓机/合成器/采样）。
- **Output**: 命名清晰、电平合理（留 headroom）的多轨；吉他/贝斯保留 DI 以便 reamp；编程轨量化/groove 处理就绪。
- **入门 SOP（minimum viable steps）**:
  1. **设置增益结构（gain staging）+ 监听**: 输入电平留足 headroom（峰值不撞 0 dBFS），确认监听/耳机能听清。跳过 → 录进削波/底噪过大，后期无法挽救。(evidence: [T03-S001], gain staging def T06)
  2. **话筒选型 + 摆位（录音轨）**: 按声源选话筒（U47 人声/SM7B 抗噪/SM57 万用乐器）并摆位，先调好房间/源头再录。跳过 → 录到房间反射/相位问题/不合适音色，混音里 EQ 救不回。(evidence: [T03-S001], 话筒 T02-S018)
  3. **录多 take（人声/独奏）+ 录 DI（吉他/贝斯）**: 同一段录多条供后续 comp；电吉他/贝斯同时录 DI 干信号留 reamp 余地。跳过 → 只有一条 take 没得挑；没 DI 后期想换音色无能为力。(evidence: [T03-S002])
  4. **编程节拍/合成（programming 轨）**: 用 step sequencer/piano roll 编鼓与合成（FL/Ableton），先按网格落 note。跳过 → 没有节奏骨架，其他声部无法对齐。(evidence: [T03-S010, T03-S015])
  5. **命名/标注/初步整理**: 每轨命名、着色、标记最佳 take，导出/保存 session。跳过 → 进编辑阶段面对一堆 "Audio 1/Audio 2"，效率崩塌。
- **资深路径（差异点）**:
  - **skip（跳过）**: 资深人**跳过过度补录/"再录一条保险"** —— 经验让他们知道哪条 take 已经够用（"the one"），不为完美主义无限重录；源头对了就停。(evidence: [T03-S001])
  - **optimize（优化）**: 资深人把大量精力**前移到源头**（话筒选型/摆位/演奏者状态/房间），录音时就用 Apollo 挂 UAD 建模监听（听到接近成品的声音激励表演），而非"先随便录、混音再修"。(evidence: [T03-S001], Apollo T02-S012)
  - **add（额外）**: 资深人**录音时就留 headroom + 标注 + 保 DI/reamp 余地** —— 初学者把电平推满图"响"，资深人留 -6~-12 dBFS 余量给插件甜区与后级；并系统命名/打 marker，下游省时。(evidence: [T03-S001])
- **近期变化（近 12 个月）**: **近 12 个月: 无重大流程变化（行业稳态）**。话筒/接口/gain staging/DI-reamp 是几十年稳态基本功。一个渐进信号：浮点 32-bit 录音（部分接口/录音机）让"录削波"风险下降，gain staging 的动机从"防内部削波"更偏向"插件甜区与心理稳定"（canon 已注此分化）。触发事件类型: 新工具（渐进，非颠覆）。(evidence: [T03-S001], gain staging 分化 T04 core-concept)
- **典型耗时**:
  - 入门 SOP: 数小时 ~ 数天（按编制）
  - 资深路径: 更短（源头一次到位，少返工）
- **关键工具（与 Track 02 关联）**: Pro Tools（录音棚多轨录音事实标准）、Apollo/RME（接口/转换器，录音挂 DSP）、U47/SM7B/SM57（话筒）、FL Studio/Ableton（编程）、校准监听 + 声学处理（源头判断）。
- **关键人物（与 Track 01 关联）**: Mike Senior（源头/房间优先的民主化教学）、Finneas（极简器材卧室录音）、Metro Boomin（sample/programming-driven tracking）。
- **常见失败模式**:
  - **"we'll fix it in the mix" 心态**: 触发原因 = 源头随便录、指望混音补救。**CLI 化暗示**: 检查项「这条 take 的音色/电平/相位是否已经接近你想要的成品？如果不是，先重录/换话筒摆位，别留给混音」。
  - **录进削波或电平过低**: 触发原因 = 没设 gain staging，峰值撞 0 或淹在底噪里。**CLI 化暗示**: 检查项「录音峰值是否在 -6~-12 dBFS 区间？有没有红灯削波？」。
  - **电吉他/贝斯没录 DI**: 触发原因 = 只录了过箱声，后期想换音色无 DI 可 reamp。**CLI 化暗示**: 检查项「吉他/贝斯是否同时录了 DI 干信号？」。
- **来源** (≥ 3):
  - [verified_primary] Senior Mixing Secrets（源头/房间/监听优先）: https://www.cambridge-mt.com/ms/main/ (collected: 2026-06-18) (evidence: [T03-S001])
  - [verified_primary] SOS 人声 comping/editing（多 take 录音前提）: https://www.soundonsound.com/techniques/vocal-comping-editing (evidence: [T03-S002])
  - [verified_primary] Metro Boomin Inside Track（programming/sample tracking）: https://www.soundonsound.com/techniques/inside-track-metro-boomin-heroes-villains (evidence: [T03-S010])
- **Last_updated**: 2026-06-18（Senior 3rd ed 2024 + SOS 持续教学为最新一手）
- **Decay risk**: low（话筒/接口/录音纪律几十年稳态）

---

### 3. Editing（comping / quantize / pitch-correct / time-align —— 整理成"可混"素材）

- **One-liner**: 把原始多 take 录音整理成干净、对齐、修过音、可以直接进混音的素材 —— 拼最佳表演（comping）、对齐时值（quantize/time-align）、修音高（pitch-correct），在"修到位"与"保留人味/pocket"之间取舍。(evidence: [T03-S002])
- **Trigger**: 录完原始多轨，里面有多条 take、有节奏/音高瑕疵、有需要对齐的双轨/和声。
- **Output**: 每个声部一条 comp 好的最佳表演，时值对齐（但保留 groove），音高修到位（但不过度），双轨/和声 time-align，准备进混音。
- **入门 SOP（minimum viable steps）**:
  1. **comping（拼最佳 take）**: 用 take folder/playlist 把多条 take 逐句挑出最佳片段拼成一条。跳过 → 用了带瑕疵的整条 take，或浪费了录的多条素材。(evidence: [T03-S002])
  2. **time-align / 对齐**: 对齐双轨人声、和声、多话筒鼓（相位/时值），修明显抢拍/拖拍。跳过 → 双轨发虚/相位抵消，节奏松散。(evidence: [T03-S002])
  3. **quantize（编程/鼓节奏对齐）**: 把编程或录的鼓对齐网格，但按需保留 swing/groove。跳过 → 节奏飘，但**过度**量化又会丢 pocket（见资深差异）。(evidence: [T03-S010], pocket/quantize T06)
  4. **pitch-correct（修音）**: 用 Auto-Tune（实时/音染）或 Melodyne（离线/透明/复音）修音高。跳过 → 走音留在成品；但过度修又"塑料感"。(evidence: [T03-S002], Auto-Tune/Melodyne T02-S014)
  5. **清理 + crossfade + 去呼吸/噪声**: 剪头尾、加 crossfade 防爆音、处理明显呼吸/咔哒。跳过 → 混音里到处是爆音/杂音，分心又难定位。
- **资深路径（差异点）**:
  - **skip（跳过）**: 资深人**跳过"把一切都修到完美网格/完美音高"** —— 经验告诉他们 over-quantize 会杀死 groove、over-tune 会去掉情绪，他们刻意**留瑕疵/留 pocket**（in-the-pocket ≠ on-the-grid）。(evidence: pocket def T06, [T03-S002])
  - **optimize（优化）**: 资深人用 **take folder/rating + 键盘快捷 + 批处理**极快 comp（不逐段鼠标拖）；time-align 用对齐工具批量处理多话筒鼓；Melodyne 一次拉一群音而非逐音。(evidence: [T03-S002])
  - **add（额外）**: 资深人**先听整体 feel 再决定修多少** —— 把 comp/pitch/timing 服务于"歌的情绪"而非"指标完美"；初学者一上来逐音修到死，资深人先问"这条表演哪里动人，别修没了"。(evidence: [T03-S002], serve-the-song T04)
- **近期变化（近 12 个月）**: **近 12 个月: 主要为渐进式，无颠覆**。AI/ML 让 comping/pitch 更自动（部分 DAW/插件做"自动选最佳 take"、Melodyne 复音识别更准），且 AI stem 分离让"对已混音素材做编辑"成为可能（见 workflow 7）。但核心"comp→align→quantize→tune→clean"流程稳定。触发事件类型: 新工具（AI 辅助，渐进）。(evidence: [T03-S002, T03-S016])
- **典型耗时**:
  - 入门 SOP: 单曲数小时（人声密集曲更久）
  - 资深路径: 显著更快（快捷键 + 批处理 + 少修）
- **关键工具（与 Track 02 关联）**: Pro Tools（comping/playlist 标准）、Melodyne（离线透明/复音修音）、Auto-Tune（实时/音染）、各 DAW take folder。
- **关键人物（与 Track 01 关联）**: （编辑多为无名匠活，但）Serban Ghenea/John Hanes 团队的 prep/editing 体系（"隐形"靠极致 prep）、Eyal Levi 金属对编辑精度的高要求（metal ≠ rock）。
- **常见失败模式**:
  - **过度修音（over-tuning）出塑料感**: 触发原因 = 逐音拉到 0 cent、retune speed 拉满。**CLI 化暗示**: 检查项「修完的人声还有没有情绪/呼吸？bypass A/B 一下，是不是修没了人味？」。
  - **过度量化丢 pocket**: 触发原因 = 100% quantize 到网格，groove 死掉。**CLI 化暗示**: 检查项「量化后节奏还 swing 吗？还是变得机械？需要的话调 quantize strength < 100%」。
  - **没加 crossfade / 没清理 → 爆音**: 触发原因 = comp 拼接处硬切。**CLI 化暗示**: 检查项「所有 comp 拼接点是否都有 crossfade？头尾是否清理过？」。
- **来源** (≥ 3):
  - [verified_primary] SOS 人声 comping/editing canon: https://www.soundonsound.com/techniques/vocal-comping-editing (collected: 2026-06-18) (evidence: [T03-S002])
  - [secondary] Auto-Tune vs Melodyne（修音工具分工，via Track 02）: SOS 对比 (evidence: [T03-S002])
  - [secondary] AI stem/编辑工具横评: https://musictech.com/guides/buyers-guide/best-stem-separation-tools/ (evidence: [T03-S016])
  - [reference] pocket/quantize/humanize 术语（Track 06 glossary）
- **Last_updated**: 2026-06-18
- **Decay risk**: low-medium（核心稳态；AI 辅助 comp/pitch 在渐进改进）

---

### 4. Mixing（gain staging → balance → EQ → compression → space → automation → bus/mix-bus）

- **One-liner**: 把编辑定稿的多轨平衡、塑形、布空间，做成一版有冲击力又服务歌的成品混音 —— 行业最核心、语料最厚、最易蒸 + CLI 化的 workflow。核心顺序：先 gain staging 与平衡，后逐元素塑形（EQ/压缩/空间），再自动化与总线胶水。(evidence: [T03-S001, T03-S003, T03-S007])
- **Trigger**: 编辑定稿的干净多轨到手，需要做成可听、可发行的立体声成品。
- **Output**: 一版混音 print（立体声 bounce），通常 + 导出 stems（分组子混）供母带/Atmos/客户改动。
- **入门 SOP（minimum viable steps）**:
  1. **gain staging + 路由 + 静态平衡（balance）**: 整理增益结构、建分组 bus（鼓/人声/乐器/FX aux）、用推子做静态平衡，先让"歌"在没有任何处理下就基本成立。跳过 → 一上来狂加插件，却连基本响度关系都不对，越修越乱（Senior：balance 是混音第一性）。(evidence: [T03-S001])
  2. **reference track A/B（响度匹配）**: 选商业 reference，**响度匹配后** A/B，校准自己的房间与耳朵。跳过 → 被房间谎言/耳疲劳骗，混出在别处听垮的 mix。(evidence: [T03-S001], reference T04 core-concept)
  3. **EQ（减法优先）**: 先减问题频段（mud 200-500/harsh 2-5k/boxy 300-600），清出空间，再按需小幅加色；用动态 EQ/soothe 压共振。跳过 → 频段打架、糊/刺耳，靠音量推也推不清。(evidence: [T03-S001], subtractive T04)
  4. **compression（动态）+ 并行压缩**: 用 1176/LA-2A/Pro-C 控动态，需要"加厚不压瞬态"时上**并行压缩**（NY compression：干声 + 重压副本并行）。跳过 → 动态失控（人声忽大忽小）或一压就糊、瞬态没了。(evidence: [T03-S003], 并行 T02-S019)
  5. **space（reverb/delay）**: 用混响/延时建立深度与前后景（Valhalla 等），近的干、远的湿。跳过 → 混音平、贴脸、没有空间纵深（Gibson 3D：混响=深度）。(evidence: [T03-S001], 空间 T02-S011)
  6. **automation（自动化）**: 写音量/效果随时间变化（副歌推人声、桥段开混响），让混音"活"且全程清晰。跳过 → 静态混音里人声在某些句子被淹、能量起伏丢失。
  7. **bus / mix-bus 处理（glue）**: 总线轻压（SSL bus comp "胶水"）+ 可选总线 EQ/饱和，让全混抱团；print 成品。跳过 → 各元素"各唱各的"，缺整体凝聚感（glue）。(evidence: [T03-S003])
- **资深路径（差异点）**:
  - **skip（跳过）**: 资深人**跳过"从空白 session 起步"** —— 直接套**自建混音模板**（预路由的 bus/aux、常用插件已挂、CLA 式"印好的链"、Scheps 3-bus 结构）；并且**跳过到处加处理**，默认不动、每个处理都要能说出理由（Scheps "less but knowing why"）。(evidence: [T03-S007, T03-S008, T03-S012])
  - **optimize（优化）**: 资深人**reference A/B 贯穿全程**而非偶尔对一下；用结构化总线哲学加速决策 —— Scheps **3-bus**（把全混汇到三条彩色总线分别处理）、Brauer **multing/Brauerizing**（人声分多份各走不同压缩总线再合）—— 这些是"压缩决策的模板化"，让资深人少试错。(evidence: [T03-S007, T03-S011])
  - **add（额外）**: 资深人**额外做 mono 兼容 + 多系统/小音箱 + 安静音量复核** —— 初学者只在一对监听大声听，资深人折 mono 查相位/丢失、过车载/手机/耳机、降到对话音量复核平衡（"大声听久了一切都显得好"）。(evidence: [T03-S001], mono compatibility T06)
- **近期变化（近 12 个月）**: **2024-2025 起，由 AI mix assistant + Atmos 推动**，混音的**起点**正在改变：(a) AI mix assistant（plugin/DAW 内置）分析 session 直接给一版平衡/EQ/压缩起点，初学者越来越多从 AI 起点接管而非从零（**但资深人把它当起点不当终点**，仍 reference A/B + 用耳朵校）；(b) 部分商业项目要求**同时交立体声 + Dolby Atmos 混音**，多一条沉浸式混音链路。触发事件类型: 新工具（AI 辅助）+ 标准/格式（Atmos）。当前采用率: 无硬 survey，AI mix assistant 仍以"起点工具"被采用，专业混音师主流仍手动主导（业内）。(evidence: [T03-S020, T03-S018], AI 工具 T02)
- **典型耗时**:
  - 入门 SOP: 单曲 1 ~ 数天
  - 资深路径: 数小时（模板 + reference + 决策模板化；CLA 以"快速 print"闻名）(evidence: [T03-S012])
- **关键工具（与 Track 02 关联）**: FabFilter Pro-Q（EQ）、1176/LA-2A/SSL bus comp 及复刻（压缩）、Valhalla（混响）、soothe2/3（共振）、Pro-C 2（透明压缩）、校准监听 + reference。
- **关键人物（与 Track 01 关联）**: Andrew Scheps（3-bus / 全 ITB / 极简模板 "Art of Letting Go" 2025）、Michael Brauer（multing/Brauerizing）、Chris Lord-Alge（摇滚 in-your-face / print-fast 链）、Serban Ghenea（隐形混音 / serve-the-song）、Manny Marroquin（reverb / push-pull）。
- **常见失败模式**:
  - **跳过平衡直接堆处理**: 触发原因 = 急着 "make it sound pro" 狂加插件。**CLI 化暗示**: 检查项「在加任何 EQ/压缩前，光用推子的静态平衡能不能让歌成立？如果不能，先调平衡」。
  - **没响度匹配就 A/B reference**: 触发原因 = 直接切 reference，更响的总显得更好 → 误判。**CLI 化暗示**: 检查项「A/B reference 时是否已经把两者响度匹配（gain-match）？」。
  - **到处加 EQ 不做减法**: 触发原因 = 哪里不够就 boost，越加越糊/刺耳。**CLI 化暗示**: 检查项「这次 EQ 是在减问题，还是在加色？能不能先减出空间再说？」。
  - **只在大监听大声听，不查 mono/小系统/低音量**: 触发原因 = 单一聆听环境 + 大声 = 自我欺骗。**CLI 化暗示**: 检查项「折成 mono 还成立吗？过手机/车载/耳机听过吗？降到对话音量平衡还对吗？」。
- **来源** (≥ 3):
  - [verified_primary] Senior Mixing Secrets（balance-first / reference / 监听纪律）: https://www.cambridge-mt.com/ms/main/ (collected: 2026-06-18) (evidence: [T03-S001])
  - [verified_primary] Scheps Tape Op 长访谈（3-bus / 模板 / less but knowing why）: https://tapeop.com/interviews/133/andrew-scheps (evidence: [T03-S007])
  - [verified_primary] Brauer SOS Secrets（multing 总线工作流）: https://www.soundonsound.com/techniques/secrets-mix-engineers-michael-brauer (evidence: [T03-S011])
  - [surrogate_primary] FabFilter bus/parallel/mix-bus 压缩工作流: https://www.fabfilter.com/learn/compression/compression-techniques-bus-parallel-and-mix-bus (evidence: [T03-S003])
  - [secondary] AI mix assistant 作起点（主动降级）: https://pitchinnovations.com/blog/can-ai-mix-assistants-replace-mix-engineers-top-ai-mixing-plugins-2025/ (evidence: [T03-S020])
- **Last_updated**: 2026-06-18（Scheps 2025 模板 + AI mix assistant 2025 报道为最新一手/近一手）
- **Decay risk**: medium（核心混音流程稳态；但"混音起点"被 AI assistant 改写中，故标 medium 而非 low）

---

### 5. Mastering（loudness / EQ / limiting / dither / sequencing —— 做成可发行母带）

- **One-liner**: 把混音定稿做成可发行母带 —— 全局 EQ/动态微调、命中平台响度 target（不再冲最响）、限制器控峰、降位深时一次 dither、专辑排序与曲间间隔。streaming normalization 时代这一步的**目标假设已被改写**。(evidence: [T03-S004, T03-S006])
- **Trigger**: 混音定稿（已 print）到手，需要做成跨平台安全、响度合规、可压盘/上架的母带。
- **Output**: 母带文件（按目标格式/响度），album 排序 + 曲间间隔，true-peak 合规，必要时 + DDP（压盘）。
- **入门 SOP（minimum viable steps）**:
  1. **校准监听 + reference 母带 A/B**: 在校准监听上放商业 reference 母带，响度匹配后对照。跳过 → 在没校准的系统上母带，结果在别处听垮（Katz：校准监听是母带必需不是可选）。(evidence: [T03-S004], K-System T04)
  2. **全局 EQ + 动态微调**: 对整曲做温和宽带 EQ（修整体音色平衡）+ 多段/M-S 微调，问题应尽量回混音解决而非母带补。跳过 → 整张专辑音色不统一/某频段整体过冲。(evidence: [T03-S004])
  3. **限制器命中响度 target（保动态优先）**: 用 Pro-L 2 / Ozone Maximizer 把响度推到平台 target（≈ -14 LUFS streaming / -1 dBTP），**到 target 即止，不为更响过压**。跳过 → 要么太轻被平台拉低、要么过压牺牲动态换不来响度（normalization 会回拉）。(evidence: [T03-S004, T03-S006], LUFS T06)
  4. **true-peak 余量**: 留 true-peak ≤ -1 dBTP，防 inter-sample peak 在转码时削波。跳过 → 上架/转码后出现削波失真（sample peak 设到 0 测不到 ISP）。(evidence: [T03-S004], dBTP T06)
  5. **dither（降位深时一次）**: 若降到 16-bit（如 CD），最后一次降位深时加一次 dither。跳过 → 量化失真/低电平细节丢失；**或误在浮点链路多次加 dither**（也是错）。(evidence: [T03-S013], dither T06)
  6. **排序 + 曲间间隔 + 母带级聆听**: 专辑曲序、曲间间隔/淡入淡出、整张连续听确认流畅。跳过 → 单曲都好但专辑听感断裂/响度跳变。
- **资深路径（差异点）**:
  - **skip（跳过）**: 资深母带师**跳过"为更响而过压"** —— normalization 时代他们知道过压只赔动态不赚响度，主动**留动态**（Katz 反响度战争）；也跳过"母带补混音的锅"，宁可退回让混音师改。(evidence: [T03-S006], Katz T04)
  - **optimize（优化）**: 资深人**校准监听 + 整张专辑统一处理**（一条母带链跑全专辑，保证音色/响度一致），用 reference 母带快速定 target，而非逐曲从零试。(evidence: [T03-S004])
  - **add（额外）**: 资深人**额外管 true-peak 余量 + 一次 dither + 多平台预演** —— 初学者只盯一个 LUFS 数字，资深人确保 dBTP 合规、dither 只在最后降位深加一次、并预演不同平台 normalization 后的响度（"-14 是上限触发点不是必须命中的硬目标，动态母带可更低"）。(evidence: [T03-S004, T03-S006], dither T06)
- **近期变化（近 12 个月）**: **由 streaming LUFS normalization 制度化推动（持续效应，制度本身已稳定）**，母带的**目标假设**从"推到 0 dB 最响"彻底转为"留 dBTP 余量、按平台 target（Spotify -14 / Apple -16 / Deezer -15）定响度、优先保动态"。BS.1770-5 与 EBU R128 v5.0 均 2023-11 更新（标准层活跃）。另一近期变化：AI 母带（Ozone Master Assistant / LANDR）把"母带起点"自动化 —— 独立艺人用 AI 起点 + 人工校，但**专业发行仍人工主导**，AI 输出被批偏 harsh/digital，必须 A/B。触发事件类型: 标准更新（LUFS 制度化）+ 新工具（AI 母带）。当前采用率: streaming target 已是事实通用规范（官方平台文档）；AI 母带在 demo/独立场景采用上升，重要商业发行仍人工（业内）。(evidence: [T03-S006, T03-S005, T03-S017, T03-S004])
- **典型耗时**:
  - 入门 SOP: 单曲数十分钟 ~ 数小时；专辑数天
  - 资深路径: 单曲更快（链 + reference + 校准房）；但专辑统一处理与聆听仍耗时
- **关键工具（与 Track 02 关联）**: iZotope Ozone（ITB 母带套件 + Master Assistant）、FabFilter Pro-L 2（限制器）、校准监听、reference 母带、LANDR/CloudBounce（AI 在线母带，demo 场景）。
- **关键人物（与 Track 01 关联）**: Bob Katz（K-System / 校准 / 反响度战争）、Bob Ludwig（restraint 母带，已退休 2023）、Greg Calbi（"sometimes best thing is nothing"）、Jens Bogren（金属混母一体化）。
- **常见失败模式**:
  - **为更响过压（响度战争遗毒）**: 触发原因 = 觉得"更响=更好/更专业"。**CLI 化暗示**: 检查项「你的母带 LUFS 是否已经超过平台 target？超过部分会被 normalization 拉低、只赔了动态 —— 是否该回退限制器、保动态？」。
  - **true-peak 设到 0 → 转码削波**: 触发原因 = 只看 sample peak。**CLI 化暗示**: 检查项「true-peak 表是否 ≤ -1 dBTP？（不是 sample peak）」。
  - **dither 用错（多次/浮点链乱加/降位深漏加）**: 触发原因 = 不懂 apply-once 规则。**CLI 化暗示**: 检查项「是否只在最后一次降位深（如 24→16bit）加了一次 dither？中间链路有没有误加？」。
  - **拿 AI 母带输出直接当成品发**: 触发原因 = 图省事不校。**CLI 化暗示**: 检查项「AI 母带（Ozone Assistant/LANDR）输出是否 A/B 过原始？有没有偏 harsh/digital？是否用耳朵校过？」。
- **来源** (≥ 3):
  - [verified_primary] SOS End of Loudness War（normalization 改写母带 target）: https://www.soundonsound.com/techniques/end-loudness-war (collected: 2026-06-18) (evidence: [T03-S006])
  - [surrogate_primary] iZotope mastering-for-streaming（LUFS/true-peak/平台 target 表）: https://www.izotope.com/en/learn/mastering-for-streaming-platforms (evidence: [T03-S004])
  - [secondary] Spotify -14 LUFS normalization 官方文档: https://support.spotify.com/us/artists/article/loudness-normalization/ (evidence: [T03-S005])
  - [surrogate_primary] iZotope dither apply-once: https://www.izotope.com/en/learn/what-is-dithering-in-audio (evidence: [T03-S013])
  - [verified_primary] SOS AI 在线母带的未来: https://www.soundonsound.com/techniques/landr-cloudbounce-future-mastering (evidence: [T03-S017])
- **Last_updated**: 2026-06-18（平台 target + BS.1770-5/R128 v5.0 2023-11 + AI 母带 2025 报道）
- **Decay risk**: medium（核心母带 craft + 校准/dither 稳态；但平台 target 可无公告微调、AI 母带模块迭代快）

---

### 6. Delivery（DDP / streaming spec / stems / Atmos —— 交付到分发/压盘）

- **One-liner**: 把母带定稿打包成各分发渠道要求的格式与元数据 —— streaming 上架的 WAV + 响度/dBTP 合规、压盘的 DDP image、客户/影视要的 stems、以及（近年新增的）Dolby Atmos ADM BWF 沉浸式交付。(evidence: [T03-S014, T03-S004, T03-S018])
- **Trigger**: 母带定稿，需要按目标渠道（streaming / CD 压盘 / sync/影视 / Atmos）打包交付。
- **Output**: 渠道对应的交付物 —— DDP image（压盘）/ 高解析 WAV + 元数据（streaming/分发）/ stems（客户/sync/重混）/ ADM BWF（Atmos）。
- **入门 SOP（minimum viable steps）**:
  1. **确认目标渠道与规格**: 弄清要交给谁、什么格式（采样率/位深/响度/peak/文件类型）。跳过 → 交错格式被打回，或上架后响度/削波出问题。(evidence: [T03-S004])
  2. **导出主交付文件 + 响度/peak 合规复检**: 按规格导出（如 streaming 高解析 WAV、true-peak ≤ -1 dBTP），复检响度 target。跳过 → 转码削波 / 响度被平台拉低或惩罚。(evidence: [T03-S004])
  3. **嵌入元数据（ISRC / 曲目信息）**: 嵌 ISRC（每条录音唯一码）、曲目名/艺人等。跳过 → 版税追踪断链、分发系统报错（每个录音/版本需独立 ISRC）。(evidence: [T03-S014], ISRC T06)
  4. **按渠道生成专属包**: 压盘 → DDP image + checksum + subcode（track index/ISRC/CD-Text）；客户/sync → stems（分组子混，非逐轨）；streaming → 平台规格 WAV。跳过 → 压盘厂无法接收（不是发一堆 WAV）/ stems 给成了 multitracks。(evidence: [T03-S014], stems/DDP T06)
  5. **交付前最终校验**: checksum 核对、试听整张、确认文件命名/版本。跳过 → 交了错版本/损坏文件，返工 + 信誉受损。
- **资深路径（差异点）**:
  - **skip（跳过）**: 资深人**跳过"母带阶段才想交付规格"** —— 他们在母带前就锁定 dBTP 余量与 target，交付时无需返工补救；不会"先做满再削"。(evidence: [T03-S004])
  - **optimize（优化）**: 资深人用**批量/脚本化元数据 + 模板化交付包** —— 一套流程产出 DDP + streaming WAV + stems + 备份，元数据（ISRC/CD-Text）批量嵌入，而非逐文件手填。(evidence: [T03-S014])
  - **add（额外）**: 资深人**额外做多格式/多平台 + 沉浸式 + 冗余校验** —— 同时备好立体声 + Atmos（ADM BWF），核对 ISRC/checksum，并**永远 bounce 一条立体声 master 随 ADM BWF 一起交**（兼容不支持 Atmos 的系统）；初学者只交单一立体声文件。(evidence: [T03-S018, T03-S019])
- **近期变化（近 12 个月）**: **2024-2025 起，由 Dolby Atmos / 沉浸式音频普及推动**，delivery 多出**第二条链路**：除传统立体声交付外，越来越多发行要求 **ADM BWF（Atmos 通用母带文件，48 kHz / 24-bit，含 Engineer/ISRC/Project ID 元数据）**，分发到 Apple Music Spatial Audio / Amazon Music / TIDAL / Netflix。实践共识：Atmos 交付要**有意设置 binaural metadata（人声 Near / 鼓 Mid / 氛围 Far）**否则耳机回放全挤在同一距离；且**永远附带一条立体声 master 兜底**。触发事件类型: 标准/格式（Atmos ADM BWF）。当前采用率: 主流流媒体已普遍支持/部分商业项目要求，立体声仍是基线（业内/practitioner + vendor docs）。(evidence: [T03-S018, T03-S019])
- **典型耗时**:
  - 入门 SOP: 单曲数十分钟；专辑 DDP/多格式数小时
  - 资深路径: 脚本化后显著更快（但 Atmos 额外链路增加总工时）
- **关键工具（与 Track 02 关联）**: 母带 DAW（Studio One / Sequoia / WaveLab 等做 DDP，本行常用）、iZotope Ozone（响度/peak 复检）、Dolby Atmos Renderer（ADM BWF 导出）、Pro Tools（Atmos 混音源 + Dolby Audio Bridge）。
- **关键人物（与 Track 01 关联）**: 母带师群（Katz/Ludwig/Calbi 传统）、Jens Bogren（含 Atmos 重混金属）。
- **常见失败模式**:
  - **不留 dBTP 余量 → 转码削波**: 触发原因 = 交付文件 true-peak 太高。**CLI 化暗示**: 检查项「交付文件 true-peak 是否 ≤ -1 dBTP？streaming 转码会不会削波？」。
  - **stems 给成 multitracks（或反之）**: 触发原因 = 不分清分组子混 vs 逐轨。**CLI 化暗示**: 检查项「客户要的是 stems（分组：鼓/人声/乐器子混）还是 multitracks（逐轨）？给对了吗？」。
  - **压盘只发 WAV，没 DDP**: 触发原因 = 不懂压盘要 DDP image + checksum。**CLI 化暗示**: 检查项「压盘交付是否生成了 DDP image + checksum + subcode（含 ISRC）？」。
  - **交 Atmos 不附立体声 / 没设 binaural metadata**: 触发原因 = 只导 ADM BWF。**CLI 化暗示**: 检查项「ADM BWF 是否附带了一条立体声 master 兜底？binaural metadata（Near/Mid/Far）是否有意设置过？」。
- **来源** (≥ 3):
  - [secondary] DDP 母带交付格式 explainer（practitioner）: https://www.audiomaster.co.uk/ddp-mastering-format-explained/ (collected: 2026-06-18) (evidence: [T03-S014])
  - [surrogate_primary] iZotope mastering-for-streaming（多平台规格）: https://www.izotope.com/en/learn/mastering-for-streaming-platforms (evidence: [T03-S004])
  - [secondary] Atmos 2025 deliverables（ADM BWF / 48k-24bit / binaural metadata / 附立体声）: https://ralphsutton.com/dolby-atmos-standards-deliverables-2025/ (evidence: [T03-S018])
  - [surrogate_primary] Dolby Atmos Renderer（ADM BWF originator/vendor docs）: https://professional.dolby.com/product/dolby-atmos-content-creation/dolby-atmos-renderer/ (evidence: [T03-S019])
- **Last_updated**: 2026-06-18（Atmos 2025 deliverables 为最新一手描述）
- **Decay risk**: medium（DDP/ISRC/Red Book 稳态；但 Atmos 链路与平台规格在演化）

---

### 7. AI / stem-driven 重混 + 起点生成（cross-cutting，近 12 月的真正新 workflow）

- **One-liner**: 没有原始多轨时（老歌/采样/已混音成品），用 AI stem 分离拆出 vocal/drums/bass/other，再做重混/采样/修复；或用 AI mix/master assistant 生成一个起点供人工接管 —— 这是近 12 个月**真正新增**的 workflow，横切混音/编辑/母带。(evidence: [T03-S016, T03-S020, T03-S017])
- **Trigger**: (a) 想重混/采样/remix 但**没有原始多轨**（只有立体声成品）；或 (b) 想用 AI 加速、从一个自动生成的 mix/master 起点开始而非从零。
- **Output**: 拆出的 stems（带伪影，需 QC）+ 一版 AI 生成的 mix/master 起点，供人工接管精修。
- **入门 SOP（minimum viable steps）**:
  1. **选引擎拆 stem**: 用 Logic Stem Splitter（本地）/ RipX / Moises / Lalal / RX Rebalance 从立体声拆出分轨。跳过（即"有多轨却仍用分离"）→ 引入不必要伪影（有多轨永远用多轨）。(evidence: [T03-S016])
  2. **伪影 QC（关键）**: 单听每个 stem，找水声/相位/频段残留伪影，决定能不能用。跳过 → 伪影进下游被放大，尤其进母带链。(evidence: [T03-S016])
  3. **（可选）AI mix/master assistant 起点**: 用 mix assistant / Ozone Master Assistant / LANDR 出一版起点。跳过 → 没问题，本就是可选加速步。(evidence: [T03-S020, T03-S017])
  4. **人工接管精修**: 在 AI 起点上按真实混音/母带流程（workflow 4/5）reference A/B + 用耳朵改。跳过 → 把 AI 输出当成品（最常见错误）。(evidence: [T03-S020])
  5. **null / A-B 验证**: 对照原始、A/B（响度匹配），确认 AI 处理真的更好而非"听起来不一样"。跳过 → 被"变化=改进"错觉骗。(evidence: [T03-S017], null test T06)
- **资深路径（差异点）**:
  - **skip（跳过）**: 资深人**跳过"盲信 AI 输出"** —— 把 AI stem/mix/master 一律当**起点不当终点**，且**有原始多轨时根本跳过 stem 分离**（分离永远不如原始多轨）。(evidence: [T03-S016, T03-S020])
  - **optimize（优化）**: 资深人**按素材选引擎 + 优先本地**（Logic Stem Splitter 本地几十秒、隐私好；云引擎按曲目质量挑），不只用一个引擎，知道哪种素材哪个引擎伪影最少。(evidence: [T03-S016])
  - **add（额外）**: 资深人**额外做伪影 QC + null/A-B + 不让分离 stem 进母带链** —— 初学者直接用拆出的 stem 当干净源，资深人先验伪影、母带级慎用分离结果，并用 null test 戳穿"AI 一定更好"的营销。(evidence: [T03-S016, T03-S017])
- **近期变化（近 12 个月）**: **这个 workflow 本身就是近 12 个月的变化**。2024-2025 起：Logic 11 内置**本地** Stem Splitter（Apple Silicon 3 分钟曲约 20-40 秒）、RipX 自称"首个真 AI DAW"、Moises/Lalal/AudioShake 等云引擎质量跃升、AI mix assistant 与 AI 母带（Ozone 12 ML 模块 / LANDR）成熟。直接改写：**无多轨也能重混/采样**（重写 remix/sampling 工作流）、**混音/母带起点 AI 化**。触发事件类型: 新模型/新工具（AI/ML，月级迭代）。当前采用率: stem 分离已成独立艺人/remixer/DJ 常用；专业精修仍人工主导（业内横评）。(evidence: [T03-S016, T03-S020, T03-S017])
- **典型耗时**:
  - 入门 SOP: 拆 stem 数十秒~分钟（本地）；接管精修同混音/母带耗时
  - 资深路径: 拆 + QC 更快，但精修不省（伪影越多越费）
- **关键工具（与 Track 02 关联）**: Logic Stem Splitter（本地）、RipX / Moises / Lalal / AudioShake（云）、RX Music Rebalance（修复）、AI mix assistant（plugin/DAW）、Ozone 12 Master Assistant / LANDR（AI 母带起点）。
- **关键人物（与 Track 01 关联）**: Dan Worrall（反玄学 / null test 立场，正是验证 AI 输出"是否真更好"的方法论）；Bobby Owsinski（务实 AI 怀疑，Handbook 6th ed 含 AI 章）。
- **常见失败模式**:
  - **有多轨却用 stem 分离**: 触发原因 = 图快/忘了有原始素材。**CLI 化暗示**: 检查项「你有原始多轨吗？有就别用分离 —— 分离永远有伪影，原始多轨永远更干净」。
  - **不做伪影 QC 直接用 stem**: 触发原因 = 假设拆出来就干净。**CLI 化暗示**: 检查项「每个拆出的 stem 单独听过吗？有没有水声/相位/残留伪影？这些 stem 适合进母带链吗（通常不）？」。
  - **把 AI mix/master 输出当成品**: 触发原因 = 省事 + 信营销。**CLI 化暗示**: 检查项「AI 起点是否经过 reference A/B（响度匹配）+ 人工用耳朵接管？还是直接发了？」。
- **来源** (≥ 3):
  - [secondary] MusicTech 9 款 stem 分离横评: https://musictech.com/guides/buyers-guide/best-stem-separation-tools/ (collected: 2026-06-18) (evidence: [T03-S016])
  - [secondary] AI mix assistant 作起点（主动降级）: https://pitchinnovations.com/blog/can-ai-mix-assistants-replace-mix-engineers-top-ai-mixing-plugins-2025/ (evidence: [T03-S020])
  - [verified_primary] SOS AI 在线母带的未来（起点不是终点）: https://www.soundonsound.com/techniques/landr-cloudbounce-future-mastering (evidence: [T03-S017])
- **Last_updated**: 2026-06-18
- **Decay risk**: high（AI/ML 模型月级迭代，今天最好的引擎 6 月后可能被超；本 workflow 是本 skill 衰减最快处）

---

## Phase 2 提炼提示

**反复出现 ≥ 3 个 workflow 都包含的步骤**（候选 playbook 通则）:
- **「reference track（响度匹配后）A/B 校准」** 出现于 workflows: 1(编曲) / 4(混音) / 5(母带) / 7(AI 校验) → 候选「如果不确定一个判断好不好，则响度匹配后对照商业 reference，而非信自己耳朵/房间/表」playbook。这是本行最强的跨阶段通则。(evidence: [T03-S001, T03-S006])
- **「减法优先 / 默认不处理，每个处理要能说出理由」** 出现于 workflows: 1(编曲减法) / 3(不过度修) / 4(减法 EQ) / 5(母带宁退回也不过压) → 候选「如果想加 X（轨/EQ/压缩/响度），先问能不能减/不加」playbook。(evidence: [T03-S007, T03-S001])
- **「源头/前置阶段决定下游上限」** 出现于 workflows: 1→2(编曲为混音留空间) / 2→4(录好源=混音赢一半) / 5→6(母带前锁交付规格) → 候选「如果下游难，回上游解决而非在下游补救（不要 we'll-fix-it-in-the-X）」playbook。(evidence: [T03-S001, T03-S004])
- **「AI/自动输出是起点不是终点，永远人工 A/B + 用耳朵接管」** 出现于 workflows: 4(AI mix assistant) / 5(AI 母带) / 7(全部 AI/stem) → 候选「如果用了任何 AI/自动工具，则把它当起点 + null/A-B 验证 + 人工接管」playbook。(evidence: [T03-S020, T03-S017, T03-S016])
- **「多环境/多视角复核（mono / 小系统 / 安静音量 / 多平台 / 多格式）」** 出现于 workflows: 4(mono+小系统+低音量) / 5(多平台 normalization 预演) / 6(多格式+Atmos+立体声兜底) → 候选「交付/定稿前在尽量多的真实回放环境复核」playbook。(evidence: [T03-S001, T03-S018])

**入门 SOP 和资深路径之间最大的差距**（候选 心智模型）:
- 入门 SOP 平均 5-7 步且**线性顺做**；资深路径靠 **(a) 模板化/决策模板化**（session 模板、Scheps 3-bus、Brauer multing、CLA 印好的链、母带统一链）压缩试错，**(b) 大量「跳过过度处理」**（不过度编曲/修音/量化/过压/盲信 AI）。→ 推断这一行资深人特别擅长**「知道什么不做」与「把重复决策模板化」**。
- 反复出现的资深「skip」=**对抗自己的过度欲望**（over-arrange / over-tune / over-quantize / over-compress / over-loud / over-trust-AI）→ 心智模型候选：**「最常见的错是做太多，不是做太少；克制 + 服务歌 = 资深标志」**（直通本行第一性张力 serve-the-song ⇄ technical / less-is-more ⇄ fix-it-in-the-mix）。
- 资深「add」高度集中在**外部校准/验证**（reference A/B、mono、多系统、null test、true-peak、dither apply-once）→ 心智模型候选：**「所有听感判断都要外部校准，因为耳朵、房间、AI 营销都会骗你」**（呼应 Track 04/06 同一结论）。

**近期工作流变化的根本原因**:
- 触发变化的事件类型分布（7 个 workflow）:
  - **标准更新驱动**: 1 个核心（5 母带 — LUFS normalization 制度化，已稳定）+ 波及 6 交付。
  - **新工具/新模型（AI）驱动**: 3 个（4 混音起点 / 5 AI 母带起点 / 7 AI-stem 整条新 workflow）。
  - **格式标准（Atmos）驱动**: 2 个（4 第二条混音链 / 6 ADM BWF 交付）。
  - **稳态无重大变化**: 1-3（编曲/tracking/editing 核心稳定，仅渐进）。
- 主要驱动力 → Phase 2「外部驱动力」: **(1) streaming LUFS normalization**（已制度化，重塑母带博弈，是过去 15 年最大范式翻转，现稳定）；**(2) AI/ML**（stem 分离 + mix/master assistant，月级迭代，是当前最活跃、衰减最快的驱动力）；**(3) Dolby Atmos/沉浸式**（增量第二链路，渐扩）。这三者直接影响 Phase 2 的心智模型（"AI 是起点不是终点"）与反模式（"过压冲响度已被证伪"/"盲信 AI 输出"/"有多轨却用 stem 分离"）。

**冷僻 / 信号薄弱**:
- workflow 数 < 4？ **否** — 7 个（远超 floor 4）。
- 一手 source < 50%？ **否** — verified_primary + surrogate_primary（vendor docs/originator）占 manifest 大多数（21 条中 verified_primary 9 + surrogate_primary 5 = 14/21 ≈ 67%；其余 secondary 主要用于 recency/横评，且 SEO-ish 项已主动降级且不单独支撑 mental model）。
- 资深差异点缺失 > 50% workflows？ **否** — 7/7 workflow 全部有 skip + optimize + add 三种差异点（每个 ≥ 3 处，远超"≥ 2 处"门槛）。
- → **不触发** Phase 2.8「workflow 维度信号薄弱」。本行 workflow 维度信号丰满。
- **唯一诚实边界**（与 Track 04 一致）: 本行核心是 **deep tacit listening knowledge**。本 track 能拆出"做什么/跳过什么/优化什么"的步骤骨架与失败模式，但"听出 mud 在 250Hz 还是 350Hz""这条人声修到哪算够"这类**黄金耳朵判断**靠 reference + 千小时积累，任何 SOP 都无法完全言传。CLI 化的失败模式自检（mono？响度匹配 A/B？dBTP？dither once？AI 校过没？）是把可机械化的纪律抽出来，**但不能替代耳朵训练**。Phase 2 在 workflow 节应注明此 tacit-knowledge ceiling，并把 reference-A/B 作为贯穿全 pipeline 的"代偿外部校准"核心 playbook。

---

## 质量自检

- [x] Workflow 数量 ≥ 4？ → **7 个**（1 编曲 / 2 tracking / 3 editing / 4 mixing / 5 mastering / 6 delivery + 7 AI-stem 横切）。覆盖 intake 全 pipeline 6 阶段 + 1 新兴横切。
- [x] 每个 workflow 有完整字段卡 + last_updated 日期？ → 全部含 One-liner/Trigger/Output/入门 SOP（含跳过后果）/资深路径（skip+optimize+add）/近期变化（含触发类型）/典型耗时/关键工具/关键人物/失败模式（含 CLI 化暗示）/来源 ≥3/Last_updated/Decay risk。
- [x] 入门 SOP 和资深路径分开了？≥ 80% workflows 有 ≥ 2 处资深差异点？ → **100%**：7/7 全部含 skip + optimize + add 三类，每类 ≥ 3 处差异。
- [x] 近期变化字段 ≥ 60% workflows 都填了？ → **100%**：3 个填了实质变化（4/5/6 + 7 本身即变化），3 个明确填「稳态，仅渐进」（1/2/3）—— 均为合法填法（task iter8 修正）。
- [x] 一手来源（工程师/公司/标准 + vendor docs originator）占比 ≥ 50%？ → ≈ 67%（verified_primary 9 + surrogate_primary 5 / 21）。
- [x] Decay risk 字段每个 workflow 都标了？ → 全部用 `Decay risk: low|medium|high` token：1 low / 2 low / 3 low-medium / 4 medium / 5 medium / 6 medium / 7 high。
- [x] 总览表按 decay 分组？ → 是（High 1 / Medium 3 / Low 3）。
- [x] Phase 2 接口（共同步骤 + 入门资深差距 + 变化触发分布 + 冷僻信号）填了？ → 是。
- [x] 每个数字/spec 有 source_id 或 caveat（业内/估计/约/官方/公开）？ → LUFS/dBTP/平台 target/采样率位深均挂 evidence 或标 `业内`/`官方`/`约`；无裸 `\d{2,5} sources/users` 表述。
- [x] last_updated / last_checked token 在文件头与每卡片均有。

> **结论**: workflow 维度信号丰满，7 workflow 全部 retain（completeness/traceability/入门-资深差异/时效锚点 四项均 ✅ 或 3✅）。最大衰减热点 = workflow 7（AI/stem，high）+ workflow 4/5 的"起点 AI 化"（medium）。建议 master skill 每 3 个月对 AI/stem 与平台 LUFS target 跑一次 update（SKILL.md Phase 0C）。
