# Track 03 — Workflows / SOPs：语音转文字 / ASR 应用工程

> Research date: 2026-06-04 · Locale: zh-CN（canon 全球）· Profile: practitioner（移动端 / 快速 / 低成本）
> 范围：**把 Track 02 的选型/工具落地成可执行 SOP** —— 选型决策 SOP + 三条集成 SOP（云/端侧/自托管）+ 移动端专章 + 成本优化 playbook + 后处理流水线 + WER 评测环。
> Seed 复用：Track 02（引擎/API/定价/端侧）、Track 04（WER/RTF/VAD/diarization/ITN 概念）、Track 01（端侧免费 vs 云立场）。本 track 引用 seed 时直接挂 `T02-Sxxx`/`T04-Sxxx`/`T01-Sxxx`。

---

## Source Manifest

| source_id | url | bucket | last_checked | author/host | one-line note |
|-----------|-----|--------|--------------|-------------|---------------|
| T03-S001 | https://github.com/m-bain/whisperX | verified_primary | 2026-06-04 | Max Bain (m-bain) | WhisperX — VAD→批量转写→wav2vec2 对齐→diarization 全链路, 70x |
| T03-S002 | https://github.com/MahmoudAshraf97/whisper-diarization | verified_primary | 2026-06-04 | Mahmoud Ashraf | whisper + NeMo MSDD diarization 流水线（另一实现） |
| T03-S003 | https://github.com/snakers4/silero-vad | verified_primary | 2026-06-04 | Silero | Silero VAD repo — <1ms/chunk, 流式分块/裁静音 SOP 基石 |
| T03-S004 | https://github.com/pyannote/pyannote-audio | verified_primary | 2026-06-04 | Hervé Bredin | pyannote.audio — diarization 事实标准, 需 HF token |
| T03-S005 | https://github.com/jitsi/jiwer | verified_primary | 2026-06-04 | jitsi | jiwer — WER/CER/MER 计算 + Compose 归一化变换 |
| T03-S006 | https://github.com/SYSTRAN/faster-whisper | verified_primary | 2026-06-04 | SYSTRAN | faster-whisper — BatchedInferencePipeline + 内置 Silero VAD |
| T03-S007 | https://github.com/k2-fsa/sherpa-onnx | verified_primary | 2026-06-04 | k2-fsa | sherpa-onnx — 离线端侧部署引擎(Android/iOS/RN/嵌入式) |
| T03-S008 | https://k2-fsa.github.io/sherpa/onnx/sense-voice/index.html | surrogate_primary | 2026-06-04 | k2-fsa | 项目 docs — SenseVoice 经 sherpa-onnx 端侧集成步骤 |
| T03-S009 | https://github.com/XDcobra/react-native-sherpa-onnx | verified_primary | 2026-06-04 | XDcobra | RN TurboModule — sherpa-onnx 跨平台离线 STT/VAD/diarization |
| T03-S010 | https://developer.apple.com/documentation/speech/speechanalyzer | verified_primary | 2026-06-04 | Apple | SpeechAnalyzer 官方 API 文档（iOS26 端侧, 长音频） |
| T03-S011 | https://developer.apple.com/documentation/speech/sfspeechrecognizer | verified_primary | 2026-06-04 | Apple | SFSpeechRecognizer 文档（requiresOnDeviceRecognition / 1min 限制） |
| T03-S012 | https://www.callstack.com/blog/on-device-speech-transcription-with-apple-speechanalyzer | verified_primary | 2026-06-04 | Callstack (eng blog) | SpeechAnalyzer+SpeechTranscriber 落地步骤 + AssetInventory |
| T03-S013 | https://developer.android.com/reference/android/speech/SpeechRecognizer | verified_primary | 2026-06-04 | Google Android | SpeechRecognizer 官方 API（createOnDeviceRecognizer） |
| T03-S014 | https://developer.android.com/reference/android/speech/RecognizerIntent | verified_primary | 2026-06-04 | Google Android | RecognizerIntent — EXTRA_PREFER_OFFLINE 等参数（API23+） |
| T03-S015 | https://developers.openai.com/api/docs/guides/speech-to-text | verified_primary | 2026-06-04 | OpenAI | STT 指南 — 25MB 限制 / chunking / prompt / 文件格式 |
| T03-S016 | https://developers.openai.com/api/docs/guides/realtime-transcription | verified_primary | 2026-06-04 | OpenAI | Realtime 转写 — WebSocket/WebRTC, chunking_strategy(VAD) |
| T03-S017 | https://developers.deepgram.com/docs/audio-keep-alive | verified_primary | 2026-06-04 | Deepgram | KeepAlive — 每3-5s防10s超时(NET-0001)，省 idle 计费 |
| T03-S018 | https://developers.deepgram.com/docs/understand-endpointing-interim-results | verified_primary | 2026-06-04 | Deepgram | endpointing + interim_results + utterance_end_ms 配置 |
| T03-S019 | https://developers.deepgram.com/docs/recovering-from-connection-errors-and-timeouts-when-live-streaming-audio | verified_primary | 2026-06-04 | Deepgram | 流式断线恢复/重连 SOP（Finalize/CloseStream） |
| T03-S020 | https://developer.nvidia.com/blog/accelerating-leaderboard-topping-asr-models-10x-with-nvidia-nemo/ | verified_primary | 2026-06-04 | NVIDIA | NeMo 批量推理优化 10x — Parakeet 自托管批量吞吐 SOP |
| T03-S021 | https://developer.apple.com/videos/play/wwdc2025/277/ | verified_primary | 2026-06-04 | Apple WWDC25 | SpeechAnalyzer 发布 session（端侧/长音频/多模块） |

> **bucket 说明**：github project root / arxiv = `verified_primary`；各厂商 `developer.*` / `developers.*` 官方开发者文档（OpenAI/Deepgram/Apple/Android/NVIDIA）经 verifier `engineering/blog subdomain heuristic` 判 `verified_primary`（一手 vendor docs）。`k2-fsa.github.io` 项目文档站 verifier 判 secondary（unknown host），但属 k2-fsa 官方项目 docs，按 Surrogate Policy 升 `surrogate_primary`，note 标「项目 docs」。**未收录任何黑名单**（知乎/公众号/百度百科/CSDN/简书/掘金；G2/Capterra；media.ai 榜单农场均丢弃）。比价/榜单类二手聚合站（softcery/nextlevel/futureagi 等）仅用于交叉印证、**不进 manifest**，硬数回到 Track 02 的 vendor pricing 一手。

---

## 总览（按 decay risk 分组）

### High decay (12-month-class) — 3 个

| Workflow | Trigger | Output | Last_updated | 资深差异 |
|---------|---------|--------|-------------|---------|
| W1 选型决策 SOP | 新项目要接 ASR / 现方案成本或精度不达标 | 锁定云API/端侧/自托管 + 具体引擎 | 2026-06-04 | skip 跑分迷信; add 自有数据 A/B + 中英分流 |
| W2a 云 API 集成（流式+批量） | 要托管、不想运维、起步快 | 生产可用的上传/流式/计费/重试链路 | 2026-06-04 | skip 自写 retry(用SDK); optimize VAD裁静音; add idle/断线防护 |
| W8 近期变化驱动的流程改写 | 评估是否切到新模型/新框架 | 升级决策 + 迁移计划 | 2026-06-04 | （本身即变化追踪） |

### Medium decay — 3 个

| Workflow | Trigger | Output | Last_updated | 资深差异 |
|---------|---------|--------|-------------|---------|
| W3 自托管批量转写（GPU） | 量大/隐私/算 break-even 后自建 | 高吞吐离线转写服务 | 2026-06-04 | optimize 批量+量化; add VAD前置+并发调度; skip 原版whisper |
| W6 后处理流水线 | 原始转写不可直接用（无标点/无说话人/数字乱） | 带标点/ITN/说话人/时间戳的成品 | 2026-06-04 | optimize 合并模型; add 热词+幻觉过滤; skip 不需要的环节 |
| W7 WER/CER 评测 + QA 环 | 选型/上线前要量化对比 + 防回归 | 自有数据上的 WER×RTF×成本 对比表 | 2026-06-04 | add 文本归一化+分层切片; optimize CI回归; skip 信厂商自报 |

### Low decay — 1 个

| Workflow | Trigger | Output | Last_updated | 资深差异 |
|---------|---------|--------|-------------|---------|
| W2b/W4 端侧·移动集成 | 隐私/离线/零边际成本/移动 App | App 内嵌离线转写 | 2026-06-04 | skip 云回退(纯离线); optimize 量化+模型尺寸; add 权限/电量/降级 |

> 说明：端侧移动集成的**底层范式**（量化 + 模型嵌入 + 麦克风→帧→VAD→解码）稳态，故 decay low；但**具体 API**（Apple SpeechAnalyzer 2025 新出、sherpa 模型版本）在动，单点变化进 W8。

---

## W1. 选型决策 SOP（准确率 × 延迟 × 成本 × 移动/离线/隐私）

- **One-liner**: 从「要接 ASR」到「锁定一个具体引擎 + 部署形态」，避免拍脑袋选型和跑分迷信。
- **Trigger**: 新项目要接语音转文字；或现有方案成本爆/精度不够/延迟不达标要换。 (evidence: [T02-S001, T04-S011])
- **Output**: 一句话结论「{语言赛道} 用 {引擎} 以 {云API/端侧/自托管} 形态，因为 {主约束}」，附 fallback。

### 入门 SOP（minimum viable steps）

1. **定四个硬约束的优先级**：准确率(WER/CER) / 延迟(要不要流式) / 成本 / 移动端·离线·隐私。**先问两个一票否决问题**：(a) 必须离线/隐私吗？是 → 直接进端侧分支，云 API 出局；(b) 必须实时流式吗？是 → 排除原版 Whisper(enc-dec 非流式)。 (evidence: [T04-S001, T04-S005, T02-S001])
   - *跳过后果*：不定优先级直接挑「最准的」，会选到英语榜首 Canary/Parakeet 却发现**不支持中文/不支持流式**，整套返工。 (evidence: [T02-S001, T02-S007])
2. **中文 vs 英文分流**：英文/多语 → 看 Open ASR Leaderboard（WER+RTFx）；中文 → 看 AISHELL/WenetSpeech 的 **CER**（FireRedASR/Paraformer/SenseVoice），**两套榜单两套最优解**。 (evidence: [T02-S012, T04-S015, T02-S011])
   - *跳过后果*：用英文跑分指导中文选型 → Whisper-large 中文 CER 偏高、Parakeet 根本没中文，线上准确率塌。 (evidence: [T02-S012])
3. **按主约束走决策树**（落到 Track 02 决策树 A）：
   - 离线/隐私/零边际成本 → 端侧（iOS=Apple SpeechAnalyzer/SFSpeech；跨平台=whisper.cpp+CoreML；中文=SenseVoice via sherpa-onnx；嵌入式商用=Picovoice）。 (evidence: [T02-S019, T02-S005, T02-S009, T02-S031])
   - 成本敏感+量大+可异步 → 自托管 faster-whisper(int8)/Parakeet，或云批量 AssemblyAI $0.15/hr / 中文腾讯录音 ￥0.7/hr。 (evidence: [T02-S004, T02-S022, T02-S027])
   - 实时流式 → Deepgram Nova-3（按秒计无 idle 坑）/中文火山·腾讯流式 ￥1.0/hr / 自托管 Parakeet 流式。 (evidence: [T02-S020, T02-S029, T02-S007])
   - 准确率优先（医疗/金融/法务）→ 英 Canary-Qwen / 中 FireRedASR 自托管。 (evidence: [T02-S001, T02-S011])
4. **快速验证（先跑起来再优化）**：拿 OpenAI gpt-4o-mini-transcribe（$0.003/min，一个 key）或本地 faster-whisper 跑通端到端，**不要一上来自建 GPU 集群**。 (evidence: [T02-S026, T02-S004])
5. **在自有数据上 A/B（出 W7）**：选 2-3 个候选，用你自己的真实音频跑 WER/CER + RTF + 单位成本，**不信厂商自报 WER**。 (evidence: [T04-S011, T04-S030])
   - *跳过后果*：信 Deepgram 自报 5.26% 直接上线，真实嘈杂数据上可能 ~18%，体验崩。 (evidence: [T04-S029, T04-S030])

### 资深路径（差异点）
- **skip**：资深**跳过盲目刷 Open ASR Leaderboard 榜首**——他们知道榜单是干净英文短音频，真实场景排名会变，直接按「语言赛道 + 流式与否 + 部署形态」三刀切到 2-3 个候选再 A/B。 (evidence: [T04-S013, T04-S030])
- **add**：资深**额外算 break-even**（量大才自托管）+ **额外查 license**（Parakeet/Canary 是 CC-BY-4.0 需署名，Picovoice 闭源收费）——初学者选完模型才发现不能商用。 (evidence: [T02-S007, T02-S031])
- **optimize**：资深把「中英分流」前置到第一步而非中途发现，省一轮返工。 (evidence: [T02-S012])

### 近期变化（近 12 个月）
- **2025 起，gpt-4o-transcribe / Apple SpeechAnalyzer / Parakeet-v3 / SenseVoice / Deepgram Nova-3 同期成熟**，决策树新增分支：iOS 长音频端侧从「只能 SFSpeech 1分钟」变成「SpeechAnalyzer 无限长」；中文端侧从「凑合用 Whisper」变成「SenseVoice 首选」。详见 W8。触发类型：**新模型 + 新平台 API**。
- **典型耗时**：入门 1-2 天（含一轮 A/B）；资深 半天。
- **关键工具**：Open ASR Leaderboard、jiwer（A/B 用）、各候选引擎。 (evidence: [T04-S011, T03-S005])
- **关键人物**：Vaibhav Srivastav（WER×RTFx 评测方法论）、Scott Stephenson（准确率×速度×成本三角）。 (evidence: [T01-S013, T01-S025])
- **常见失败模式**：
  - **跑分迷信**：选了英文榜首却不支持中文/流式 → 按语言赛道 + 流式与否先筛，别只看 WER 数字。 (evidence: [T02-S001])
  - **信厂商自报 WER 跨家比**：Deepgram 5.26% / Picovoice 自家友好 / Open ASR 公开集口径全不同 → 必须自有数据 A/B。 (evidence: [T04-S029, T04-S030])
  - **过早自建**：量小就上 GPU 集群，固定成本压垮 → 量小用云按量，过了 break-even 再自托管。 (evidence: [T02-S004])
- **Last_updated**: 2026-06-04 · **Decay risk**: high（模型每 6-12 月迭代，决策树分支随之变）

---

## W2a. 云 API 集成 SOP（上传 / 流式 / 计费 / 重试）

- **One-liner**: 从「拿到 API key」到「生产可用的转写链路」，覆盖批量上传、实时流式、计费防坑、错误重试。
- **Trigger**: 选定云 API（OpenAI/Deepgram/AssemblyAI/中国云），要接进生产。 (evidence: [T03-S015, T03-S017])
- **Output**: 稳定的转写服务：批量走文件、实时走 WebSocket，带重试/幂等/成本护栏。

### 入门 SOP — 批量（pre-recorded / async）

1. **预处理 + 切分到限额内**：转单声道 16kHz；OpenAI 单文件 **≤25MB**，超限要先切片（按 VAD 静音点切，别硬切词中间）。 (evidence: [T03-S015])
   - *跳过后果*：>25MB 直接 413 失败；硬切到词中间 → 边界词被腰斩，WER 升。
2. **VAD 裁静音再上传**：用 Silero VAD 删掉静音段只送有声段——按时长计费的 API（OpenAI/AWS/Google/Azure）直接省钱。 (evidence: [T03-S003, T02-S028])
3. **调用 + 带 prompt/热词**：OpenAI transcribe 支持 `prompt` 注入领域词/上一段上下文提升专名识别；要早出结果用 `stream=True` 边转边收。 (evidence: [T03-S015])
4. **异步轮询/回调**：长音频用各家 async/webhook 模式拿结果，别同步阻塞。 (evidence: [T03-S015])
5. **落地计费护栏**：记录每次音频秒数 × 单价，设月度上限告警。

### 入门 SOP — 流式（实时 WebSocket）

1. **建立流式会话**：OpenAI Realtime 用 WebSocket(服务端)/WebRTC(浏览器) + `type:"transcription"` 会话；Deepgram 用 listen WebSocket。 (evidence: [T03-S016, T03-S017])
2. **配置分段/断句**：OpenAI 设 `chunking_strategy`（auto 或 VAD），**输入 >30s 必须配**；Deepgram 配 `endpointing` + `interim_results` + `utterance_end_ms`（设 ≥1000ms，因 interim 每秒一发）。 (evidence: [T03-S016, T03-S018])
3. **拼接 final 文本**：interim(`is_final:false`) 只做实时预览，遇 `is_final:true`/`speech_final` 才追加进正式稿。 (evidence: [T03-S018])
4. **KeepAlive 防超时**：Deepgram 静默时每 **3-5s** 发一个 KeepAlive **文本帧**（发二进制无效），否则 10s 超时触发 NET-0001 断连。 (evidence: [T03-S017])
   - *跳过后果*：用户停顿几秒 → 连接被服务端关掉，下一句丢失。
5. **断线重连 + 收尾**：捕获 NET/DATA/WS 错误，指数退避重连；结束时发 Finalize/CloseStream 把缓冲区残留 flush 出来。 (evidence: [T03-S019])
   - *跳过后果*：网络抖动直接丢整段；不发 Finalize → 最后半句永远拿不到。

### 资深路径（差异点）
- **skip**：资深**跳过手写 retry/backoff**，直接用官方 SDK 自带的重连与限流处理（自写易漏边界）。 (evidence: [T03-S019])
- **optimize**：资深**全程 VAD 裁静音 + 客户端先做 endpointing**，既省按时长的钱，又减少流式 idle 帧。 (evidence: [T03-S003, T02-S028])
- **add**：资深**额外防两个隐形计费坑**：(1) AssemblyAI 流式按 **WebSocket 开-关时长**计费（含 idle），用完立刻关连接；(2) Deepgram KeepAlive 是「暂停不计音频」但仍占会话——按需开关。还会**额外做幂等**（同一音频去重，避免重试重复计费）。 (evidence: [T02-S022, T03-S017])

### 近期变化（近 12 个月）
- **2025-03 起 gpt-4o-transcribe / mini-transcribe 上线**，OpenAI 流式从「whisper-1 不支持流式」变成「transcribe API + Realtime 双路径」；mini 把省事接入价压到 $0.003/min。触发类型：**新模型 API**。 (evidence: [T02-S026, T03-S016])
- **典型耗时**：入门 批量半天 / 流式 1-2 天；资深 数小时。
- **关键工具**：各家官方 SDK、Silero VAD、jiwer（验收）。 (evidence: [T03-S003])
- **关键人物**：Scott Stephenson（Deepgram <500ms 实时立场）、Dylan Fox（AssemblyAI Audio Intelligence 一次调用出摘要/实体）。 (evidence: [T01-S025, T01-S026])
- **常见失败模式**：
  - **AssemblyAI 流式 idle 计费**：连接闲置 5 分钟=5 分钟账单 → 不用立刻关 WebSocket，别长开空连。 (evidence: [T02-S022])
  - **Deepgram 静默断连**：不发 KeepAlive → 10s 超时 NET-0001 → 静默期每 3-5s 发文本帧 KeepAlive。 (evidence: [T03-S017])
  - **>25MB / >30s 未分段**：OpenAI 批量 413、流式不配 chunking_strategy 报错 → 预先切片/配 VAD 分段。 (evidence: [T03-S015, T03-S016])
  - **重试导致重复计费**：无幂等键，超时重发 → 同段算两次钱 → 加幂等去重。 (evidence: [T03-S019])
- **Last_updated**: 2026-06-04 · **Decay risk**: high（云 API 定价/参数频繁调整）

---

## W2b / W4. 端侧 · 移动集成 SOP（"移动端"专章：iOS / Android / 跨平台）

- **One-liner**: 把 ASR 嵌进移动 App 端侧运行——离线、隐私、零边际成本，权衡包体/电量/延迟。
- **Trigger**: App 要语音转文字且要离线/隐私/零云账单（或弱网场景）。 (evidence: [T02-S019, T01-S004])
- **Output**: App 内嵌的离线转写能力（系统 API 或嵌入模型）。

### 路径 A — iOS 原生（首选，零包体增长）

1. **选 API 按 iOS 版本与场景**：
   - **iOS 26+ 且要长音频（讲座/会议）→ SpeechAnalyzer + SpeechTranscriber**：端侧专用，**无 1 分钟限制**，不增加 App 体积/内存（系统模型，自动更新），号称比 Whisper-large-v3-turbo 快 ~2x。 (evidence: [T03-S010, T03-S012, T03-S021])
   - **短指令/听写 或 需兼容旧系统 → SFSpeechRecognizer**，设 `requiresOnDeviceRecognition = true` 强制端侧；注意**单次 ~1 分钟硬限制**。SpeechAnalyzer 体系里对应模块是 DictationTranscriber。 (evidence: [T03-S011])
2. **SpeechAnalyzer 落地步骤**（iOS26）：创建 `SpeechTranscriber(locale:)` → 检查 locale 支持 → 经 **AssetInventory** 按需下载语言模型（超过同时支持上限时 deallocate 旧的腾位）→ 把音频喂给 analyzer 拿结果流；支持 mid-stream 语种切换。 (evidence: [T03-S012, T03-S010])
   - *跳过 AssetInventory 检查后果*：目标语言未下载 → 直接失败/空结果。 (evidence: [T03-S012])
3. **权限**：Info.plist 加麦克风 + 语音识别权限文案；运行时申请授权。 (evidence: [T03-S011])

### 路径 B — Android 原生

1. **用 SpeechRecognizer**：优先 `createOnDeviceRecognizer()` 走端侧；或 RecognizerIntent 传 `EXTRA_PREFER_OFFLINE=true`（API 23+）请求离线引擎。 (evidence: [T03-S013, T03-S014])
   - *坑*：**端侧可用性依赖机型/厂商实现**，`EXTRA_PREFER_OFFLINE` 在某些实现上**无效**，且默认引擎质量参差——必须真机测试 + 准备回退。 (evidence: [T03-S014])
2. **不满足就上跨平台引擎**（路径 C），别赌系统引擎。

### 路径 C — 跨平台 / 自定义模型（whisper.cpp 或 sherpa-onnx）

1. **选引擎**：要 Whisper 级精度 + 全平台 → **whisper.cpp**（iOS CoreML/Metal，iPhone13 实时，MIT）；要**中文最佳 + 极快** → **SenseVoice-Small 经 sherpa-onnx**（中粤强、70ms/10s）；要 RN/Flutter 绑定 → sherpa-onnx 有 React Native TurboModule。 (evidence: [T02-S005, T02-S009, T03-S007, T03-S009])
2. **选模型尺寸 + 量化**：端侧只塞 tiny/base 或 SenseVoice-Small（234M）；用 int8/ggml Q5 量化压包体与内存，**别塞 Whisper-large(1.5GB)/Vosk 大模型(2.7GB)**。 (evidence: [T02-S005, T02-S013, T04-S019])
3. **集成 sherpa-onnx**（中文路径示例）：下载 SenseVoice int8 onnx 模型 → Android 用预编译 AAR/APK 选「中英粤日韩 + sense_voice」模型；iOS 需从源码 build C++ 库 + Xcode 集成 → 调离线识别 API。 (evidence: [T03-S008, T03-S007])
4. **接 VAD 做流式/分块**：sherpa-onnx 自带 VAD，麦克风流 → VAD 切有声段 → 送识别，省算力/电量。 (evidence: [T03-S007, T03-S003])
5. **真机测延迟/发热/内存**：端侧最大风险是发热降频与内存峰值，必须在目标机型实测。

### 资深路径（差异点）
- **skip**：纯离线 App 资深**跳过任何云回退**（违背隐私前提）；iOS 资深在 iOS26 项目里**跳过 SFSpeech 长音频 hack**，直接 SpeechAnalyzer。 (evidence: [T03-S010])
- **optimize**：资深**先量化再选尺寸**——能用 SenseVoice-Small/base+int8 达标就不上 small/medium，省一半包体内存；iOS 优先系统 API（零包体增长）而非嵌 whisper.cpp。 (evidence: [T04-S019, T03-S010])
- **add**：资深**额外做三件**：(1) 权限拒绝/模型未下载的**降级 UI**；(2) **电量/发热预算**（长转写分段 + 后台限制）；(3) Android 因系统引擎不可靠，**默认带一个 sherpa-onnx 回退**而非只赌 SpeechRecognizer。 (evidence: [T03-S014, T03-S007])

### 近期变化（近 12 个月）
- **2025-06 (WWDC25) Apple SpeechAnalyzer 发布**：iOS 端侧从「SFSpeech 1 分钟 + 偏短句」跃迁到「无限长音频 + 端侧专用模型 + 自动多语」，长音频转写不再需要切 1 分钟片段 hack。触发类型：**新平台 API**。 (evidence: [T03-S021, T03-S010])
- **2025 SenseVoice / sherpa-onnx 模型更新**（如 2025-09 SenseVoice int8 多语包），中文端侧首选稳固。触发类型：**新模型**。 (evidence: [T03-S008])
- **典型耗时**：iOS 系统 API 1-2 天；跨平台嵌模型 3-5 天（含真机调优）。
- **关键工具**：SpeechAnalyzer、SFSpeechRecognizer、whisper.cpp、sherpa-onnx、Silero VAD。 (evidence: [T02-S005, T03-S007])
- **关键人物**：Georgi Gerganov（whisper.cpp 端侧）、Pete Warden（端侧极致/反 30s 定长）、Daniel Povey（sherpa/k2 端侧栈）。 (evidence: [T01-S001, T01-S004, T01-S007])
- **常见失败模式**：
  - **端侧塞大模型**：Whisper-large 上手机 → 包体爆/OOM/发热降频 → 用 tiny/base/SenseVoice-Small + int8。 (evidence: [T02-S013])
  - **赌 Android 系统引擎**：`EXTRA_PREFER_OFFLINE` 在部分机型无效、质量参差 → 默认带 sherpa-onnx 回退 + 真机矩阵测试。 (evidence: [T03-S014])
  - **忘记 AssetInventory 下载**：SpeechAnalyzer 目标语言未下载就调用 → 空结果 → 先查支持再下载。 (evidence: [T03-S012])
  - **iOS26 仍用 SFSpeech 切 1 分钟**：长音频被 1 分钟限制逼着切片拼接、丢上下文 → 改用 SpeechAnalyzer。 (evidence: [T03-S011, T03-S010])
- **Last_updated**: 2026-06-04 · **Decay risk**: low（底层范式稳态；具体 API 版本变化进 W8）

---

## W3. 自托管批量转写 SOP（faster-whisper / NeMo Parakeet + GPU）

- **One-liner**: 从「一堆音频文件」到「高吞吐离线转写服务」，量大时单位成本压到接近电费。
- **Trigger**: 用量过了 break-even / 隐私要求不能出云 / 要归档几千小时字幕。 (evidence: [T02-S004, T02-S001])
- **Output**: GPU 上的批量转写管线（API server 或 batch job），RTFx 数百~数千。

### 入门 SOP

1. **选引擎按语言**：英语/多语极致吞吐 → **NeMo Parakeet TDT**（RTFx~3386，1hr 音频~1s）；通用/中文 + 要 MIT → **faster-whisper**（CTranslate2，比原版快 4x）；中文最高精度 → FireRedASR/Paraformer。 (evidence: [T02-S007, T02-S004, T02-S011])
2. **量化**：faster-whisper 用 `compute_type=int8`/int8_float16，显存 ~2926MB vs fp16 4708MB，同卡塞更多并发。 (evidence: [T02-S004, T04-S019])
3. **VAD 前置**：转写前 Silero VAD 裁静音，省算力 + 减少长静音段的 Whisper 幻觉。 (evidence: [T03-S003, T04-S023])
4. **批量推理**：faster-whisper 用 `BatchedInferencePipeline` 提升吞吐（fp16 batch=1→8 吞吐 ~80x→228x，batch=8 后 GPU 饱和收益递减）；Parakeet 用 NeMo 批量接口。 (evidence: [T03-S006, T03-S020])
5. **拿词级时间戳**：开 `word_timestamps=True`（faster-whisper）或 Parakeet 时间戳输出，供字幕/检索/对齐。 (evidence: [T03-S006, T04-S025])
6. **封装服务**：上 FastAPI/队列，按 GPU 并发数限流。

### 资深路径（差异点）
- **skip**：资深**跳过原版 openai/whisper**（慢且不流式），自托管一律 faster-whisper/Parakeet。 (evidence: [T02-S003, T02-S004])
- **optimize**：资深**调 batch_size 到 GPU 饱和点附近**（不是越大越好，TDT 解码 padding 开销会反噬）+ **int8 量化** + 选对卡（L4 ~238-258x RTFx，低功耗高性价比）。 (evidence: [T03-S020, T03-S006])
- **add**：资深**额外做 VAD 前置 + 并发调度 + 监控 RTFx/显存**；并**额外估 break-even**：云 API ~$0.15-0.36/hr，单 L4/A10($0.5-1/hr 云 GPU)每小时转数百小时音频→月用量超约几百小时且有运维能力才自托管划算。 (evidence: [T02-S001, T02-S017]) `[推断]`
- **skip(license)**：资深**先确认 license**——Parakeet/Canary CC-BY-4.0 需署名才用。 (evidence: [T02-S007])

### 近期变化（近 12 个月）
- **2025 起 Parakeet TDT v2/v3 + NeMo 批量优化(10x) 成熟**，自托管批量从「faster-whisper 是唯一选择」变成「极致吞吐选 Parakeet、要中文/MIT 选 faster-whisper」双轨。触发类型：**新模型 + 框架优化**。 (evidence: [T02-S007, T03-S020])
- **典型耗时**：入门 1-2 天；资深 数小时（已有模板）。
- **关键工具**：faster-whisper、NeMo、Silero VAD、Parakeet/Canary。 (evidence: [T03-S006, T03-S020, T03-S003])
- **关键人物**：Guillaume Klein（CTranslate2/faster-whisper）、Boris Ginsburg/NeMo 团队（Parakeet GPU 吞吐）。 (evidence: [T01-S020, T01-S022])
- **常见失败模式**：
  - **不量化跑 fp16 撑爆显存**：并发上不去、单位成本高 → int8 量化。 (evidence: [T02-S004])
  - **batch 无脑调大**：过 GPU 饱和点后 padding 开销反噬吞吐 → 压到饱和点附近。 (evidence: [T03-S020])
  - **不裁静音**：长静音段既费算力又诱发 Whisper 幻觉 → VAD 前置。 (evidence: [T04-S023, T04-S010])
  - **忽略 CC-BY 署名**：商用 Parakeet/Canary 不署名 → license 违规。 (evidence: [T02-S007])
- **Last_updated**: 2026-06-04 · **Decay risk**: medium（模型换代，但自托管范式稳定）

---

## W6. 后处理流水线 SOP（VAD → ASR → 标点 → ITN → diarization → 时间戳）

- **One-liner**: 把「原始转写（常无标点、无说话人、数字口语化）」加工成「可直接用的成品稿」。
- **Trigger**: 原始 ASR 输出不能直接交付（要带标点/说话人/书面数字/字幕时间）。 (evidence: [T04-S020, T03-S001])
- **Output**: 带标点、ITN 规整、说话人标签、词级时间戳的结构化转写。

### 入门 SOP（WhisperX 是事实标准实现）

1. **VAD 分段**：Silero/pyannote VAD 切有声段——既省算力，又**抑制 Whisper 在静音/长音频上的幻觉**。WhisperX v3 默认开 VAD。 (evidence: [T03-S001, T03-S003, T04-S010])
   - *跳过后果*：长音频整段喂 Whisper → 静音处编造句子（幻觉），且慢。 (evidence: [T04-S010])
2. **转写**：faster-whisper 批量转写有声段（WhisperX 用此后端，large-v2 达 70x 实时）。 (evidence: [T03-S001, T03-S006])
3. **强制对齐拿词级时间戳**：用**语言专属 wav2vec2** 模型做 forced alignment，得到精确词级 start-end。 (evidence: [T03-S001, T04-S025])
   - *坑*：含非词典字符的 token（如 "2014." / "£13.60"）对不齐、拿不到时间戳。 (evidence: [T03-S001])
4. **标点恢复 + ITN**：ASR 原始流常无标点 → 补标点（FunASR 用 CT-Transformer）；ITN 把「一百二十三」→「123」、「百分之五」→「5%」。**标点恢复 ≠ ITN，是两件事**。 (evidence: [T04-S020])
5. **说话人分离 (diarization)**：pyannote.audio 切「谁在何时说」，按词级时间戳把说话人标签贴回转写。需 **HF token + 接受用户协议**。 (evidence: [T03-S001, T03-S004])
   - *跳过后果*：会议/访谈稿没有说话人区分，可读性差。
6. **拼装输出**：合并成 SRT/VTT/JSON（词级时间戳 + speaker + 标点 + ITN 文本）。

### 资深路径（差异点）
- **skip**：资深**按需砍环节**——单人语音命令不需要 diarization；纯字幕不需要 ITN；实时场景跳过离线对齐。能砍则砍。 (evidence: [T03-S001])
- **optimize**：中文资深直接用 **FunASR 一站式**（VAD+标点+ITN+热词+diarization 全内置），省去拼多个模型；或用 whisper-diarization(NeMo MSDD) 作 WhisperX 替代。 (evidence: [T04-S020, T03-S002])
- **add**：资深**额外做热词 biasing**（人名/品牌/术语表偏置解码）+ **幻觉过滤**（VAD 之外再用置信度/重复检测清洗）+ **数字/单位 ITN 的领域定制**。 (evidence: [T04-S022, T04-S010])

### 近期变化（近 12 个月）
- **近 12 个月：相对稳态**。WhisperX(VAD→转写→对齐→diarization)管线 2023 成型后无范式级变化；最近变化是 **diarization 仍卡在重叠语音/换 HF 模型版本**这类增量。AssemblyAI 把后处理(摘要/实体/PII)做成 API flag，云端用户可整段省掉自建流水线（2025）。触发类型：**新工具（托管化）**。 (evidence: [T03-S001, T01-S026])
- **典型耗时**：入门 1 天（拼 WhisperX）；资深 数小时。
- **关键工具**：WhisperX、Silero VAD、pyannote.audio、FunASR、whisper-diarization。 (evidence: [T03-S001, T03-S003, T03-S004, T04-S020, T03-S002])
- **关键人物**：Hervé Bredin（pyannote diarization）、Zhifu Gao/DAMO（FunASR 全链路）。 (evidence: [T01-S016, T03-S004])
- **常见失败模式**：
  - **不开 VAD 直接转长音频**：静音段幻觉 + 慢 → VAD 前置。 (evidence: [T04-S010])
  - **对齐对非词典 token 失败**：数字/货币符号拿不到时间戳 → 容错处理这些 token。 (evidence: [T03-S001])
  - **diarization 缺 HF token/协议**：pyannote 加载报错 → 先去 HF 接受协议拿 token。 (evidence: [T03-S004])
  - **把标点恢复当 ITN**：以为补了标点数字就规整了 → 两个独立环节都要。 (evidence: [T04-S020])
  - **重叠语音 diarization 错配**：多人抢话标签乱 → 已知难点，重叠多的场景需人工校或专用模型。 (evidence: [T03-S001])
- **Last_updated**: 2026-06-04 · **Decay risk**: medium（diarization/对齐仍在改进，主链路稳定）

---

## W7. WER / CER 评测 + QA 环 SOP（在自有数据上 A/B，不信厂商自报）

- **One-liner**: 从「几个候选引擎」到「自有数据上的 WER×RTF×成本 对比表 + 上线后防回归」。
- **Trigger**: 选型最后一步要量化对比；或上线前/模型升级前要防准确率回归。 (evidence: [T04-S011, T04-S030])
- **Output**: 候选 × {WER/CER, RTF, $/hr} 对比表 + CI 里的回归基线。

### 入门 SOP

1. **建评测集**：从**你自己的真实场景**采样（含口音/噪声/术语/口语数字），人工转写做 ground truth；**别只用 LibriSpeech**（干净朗读已饱和，不代表真实场景）。 (evidence: [T04-S013, T04-S030])
   - *跳过后果*：在干净公开集上测得 3% WER，真实嘈杂数据线上 ~18%。 (evidence: [T04-S030])
2. **文本归一化（最关键、最常被漏）**：ref 和 hyp 都过同一套归一化再算——`jiwer.Compose([ToLowerCase, RemovePunctuation, RemoveMultipleSpaces, Strip])`，否则大小写/标点差异虚高 WER。 (evidence: [T03-S005])
   - *跳过后果*：只因标点/大小写不同，同一份转写 WER 凭空高几个点，A/B 排名失真。
3. **算指标**：英文用 `jiwer.wer()`/`process_words()`（出 WER+MER+WIL + 对齐块）；**中文用 `jiwer.cer()`/`process_characters()`**（中文无词界，必须 CER 不是 WER）。 (evidence: [T03-S005, T04-S015])
4. **同时测 RTF + 成本**：每个候选记转写耗时/音频时长(RTF)和 $/hr，**三轴一起看**（准确率不是唯一）。 (evidence: [T04-S011, T01-S013])
5. **出对比表 + 选型**：WER/CER × RTF × 成本 三列对比，结合 W1 约束拍板。

### 资深路径（差异点）
- **skip**：资深**跳过厂商自报 WER 和单一公开集**——直接上自有数据 + 统一归一化。 (evidence: [T04-S029, T04-S030])
- **add**：资深**额外分层切片评测**（按噪声/口音/领域/时长分桶看 WER，而非一个平均数）+ **看对齐块定位错在哪**（jiwer 的 AlignmentChunk 出替换/删除/插入位置）+ **把评测塞进 CI**（每次换模型/参数自动跑，WER 回退超阈值就 block）。 (evidence: [T03-S005])
- **optimize**：资深**复用 Open ASR Leaderboard 的归一化口径**做初筛，再用自有数据终选，两段式省力。 (evidence: [T04-S011])

### 近期变化（近 12 个月）
- **2025-10 Open ASR Leaderboard 正式论文 + 多语/长音频赛道**，统一了归一化与 RTFx 口径，成为初筛 ground truth；终选仍须自有数据。触发类型：**标准/方法论更新**。 (evidence: [T04-S011, T04-S012])
- **典型耗时**：入门 半天-1 天（含建集）；资深 数小时（脚本化 + CI）。
- **关键工具**：jiwer、Open ASR Leaderboard、各候选引擎。 (evidence: [T03-S005, T04-S011])
- **关键人物**：Vaibhav Srivastav（WER×RTFx 可复现评测方法论）。 (evidence: [T01-S013])
- **常见失败模式**：
  - **不归一化算 WER**：大小写/标点差异虚高 → 统一 jiwer.Compose 归一化。 (evidence: [T03-S005])
  - **中文误用 WER**：中文无词界用 WER 数字无意义 → 用 CER。 (evidence: [T04-S015])
  - **信厂商自报/只看一个公开集**：口径不同不可比 + 干净集不代表真实 → 自有数据 A/B。 (evidence: [T04-S030])
  - **只看平均 WER**：掩盖了在嘈杂/特定口音上的塌方 → 分层切片看。 (evidence: [T04-S011])
- **Last_updated**: 2026-06-04 · **Decay risk**: medium（方法稳定，榜单/工具滚动更新）

---

## 成本优化 Playbook（"成本尽量低"专项 · 跨 workflow 抽取）

> 落地 Track 02 成本清单为可执行顺序，按**杠杆从高到低**排。

1. **能端侧就端侧 → 边际成本归零（最高杠杆）**：Apple SpeechAnalyzer/SFSpeech、whisper.cpp、SenseVoice(sherpa-onnx)、Vosk 全免费，移动端无服务器账单。这是「成本尽量低」的第一性答案。 (evidence: [T02-S019, T02-S005, T02-S009])
2. **VAD 裁静音再送识别（次高杠杆，对云 API 立竿见影）**：上传前 Silero VAD 删静音，按时长计费的 API（OpenAI/AWS/Google/Azure）直接少付空白时间的钱；阿里/腾讯本就只对语音段计费。 (evidence: [T03-S003, T02-S028])
3. **批量优先于流式**：同厂商批量普遍便宜（Azure $0.18 vs 实时 $1.00/hr；AssemblyAI $0.15 vs Pro 流式 $0.45），不需要实时就走异步。 (evidence: [T02-S024, T02-S022])
4. **量级折扣/资源包**：AWS T1→T4 $0.024→$0.0078/min；中国云大包腰斩（腾讯 ￥1.75→0.7）。预估年用量直接买大包。 (evidence: [T02-S025, T02-S027])
5. **int8/ggml 量化**：自托管 faster-whisper int8（显存腰斩）/ whisper.cpp Q5——同卡塞更多并发降单位成本。 (evidence: [T02-S004, T04-S019])
6. **小模型够用别上大模型**：Paraformer 0.2B 接近 SenseVoice-L 1.6B；mini-transcribe 是 transcribe 半价。准确率达标即止。 (evidence: [T02-S012, T02-S026])
7. **缓存/去重 + 幂等**：相同音频哈希命中直接返缓存；重试带幂等键避免重复计费。 (evidence: [T03-S019])
8. **按用量阶梯切换方案 + 自托管 break-even**：量小用云按量（无固定成本），月用量超约几百小时且有运维能力切自托管（边际≈电费）。云 ~$0.15-0.36/hr，单 L4/A10 每小时可转数百小时音频。 (evidence: [T02-S001, T02-S017]) `[推断]`
9. **流式防 idle 计费**：AssemblyAI 按 WebSocket 开-关时长计费→用完即关；Deepgram 静默用 KeepAlive 暂停而非空跑。 (evidence: [T02-S022, T03-S017])

---

## W8. 近期 12 个月变化（流程改写汇总 · 高 decay）

> 本节是 Track 03 的时效锚点：哪些新模型/新平台在近 12 个月**改写了上面的 SOP**。

| 变化 | 时间 | 改写了哪条 SOP | 触发类型 | evidence |
|---|---|---|---|---|
| **gpt-4o-transcribe / mini-transcribe** | 2025-03 | W2a：OpenAI 从「whisper-1 不支持流式」→「transcribe API + Realtime 双路径」；mini $0.003/min 成省事接入默认；W1 快速验证首选 | 新模型 | [T02-S026, T03-S016] |
| **Apple SpeechAnalyzer (WWDC25)** | 2025-06 | W4：iOS 长音频端侧从「SFSpeech 1 分钟切片 hack」→「无限长 + 端侧专用模型 + 自动多语」；W1 iOS 分支重写 | 新平台 API | [T03-S021, T03-S010] |
| **NVIDIA Parakeet TDT v2/v3 + NeMo 10x 批量** | 2025 | W3：自托管批量从「faster-whisper 唯一」→「极致吞吐选 Parakeet」双轨；W1 离线大批量分支 | 新模型 + 框架优化 | [T02-S007, T03-S020] |
| **SenseVoice (sherpa-onnx int8 多语包)** | 2024-2025 | W4：中文移动端从「凑合用 Whisper」→「SenseVoice-Small 首选(70ms/中粤强)」 | 新模型 | [T02-S009, T03-S008] |
| **Moonshine v2（流式端侧 50ms）** | 2025-26 | W4：超低延迟语音命令/边缘新增候选；experimental，6 月后形态可能变 | 新模型(新兴) | [T02-S014, T02-S015] |
| **Deepgram Nova-3 / Flux** | 2025 | W2a：流式从「按会话防 idle」→ Nova-3 按秒计 + sub-300ms + 多语 code-switching；Flux「对话式」 | 新模型 | [T02-S020, T01-S025] |
| **AssemblyAI Universal-3 + Audio Intelligence** | 2025 | W6：云端后处理（摘要/实体/PII）做成 API flag，可整段省掉自建后处理流水线 | 新工具(托管化) | [T02-S022, T01-S026] |

- **资深视角**：资深此刻的升级判据 = (1) iOS 端侧长音频项目 **立刻迁 SpeechAnalyzer**；(2) 中文端侧 **默认 SenseVoice**；(3) 实时云首选 **Deepgram Nova-3**（按秒无 idle 坑）；(4) 省事云首选 **gpt-4o-mini-transcribe**；(5) 自托管极致吞吐 **Parakeet**。但**每次切换都要回 W7 用自有数据复测**，不信发布会数字。 (evidence: [T04-S030])
- **Decay risk**: high — 本节预计 6-12 个月内需刷新（ASR 模型迭代极快）。

---

## Phase 2 提炼提示

**反复出现 ≥ 3 个 workflow 都包含的步骤**（候选 playbook 通则）：
- **VAD 裁静音/分段** 出现于 W2a(云批量) / W3(自托管) / W4(端侧) / W6(后处理) → 候选「如果按时长计费或长音频，则先 VAD 裁静音」**几乎是全行业第一步**。 (evidence: [T03-S003, T02-S028, T04-S010])
- **中英分流 + 自有数据 A/B** 出现于 W1 / W7（且 W3/W4 选型都依赖它）→ 候选「不要用英文跑分指导中文选型；不要信厂商自报 WER」。 (evidence: [T02-S012, T04-S030])
- **量化(int8/ggml) + 小模型够用** 出现于 W3 / W4 / 成本 playbook → 候选「先量化再选尺寸，准确率达标即止」。 (evidence: [T02-S004, T04-S019])
- **词级时间戳 + 拼装** 出现于 W3 / W6 → 候选「要字幕/检索/diarization 就开 word_timestamps」。 (evidence: [T03-S006, T04-S025])

**入门 SOP 和资深路径之间最大的差距**（候选心智模型）：
- 入门平均 5-6 步，资深通过「**按需砍环节**」（W6 砍 diarization/ITN）+「**用 SDK 替手写逻辑**」（W2a 跳 retry）+「**前置分流**」（W1 中英先分）压到 3-4 步 → 心智模型候选「**ASR 工程的资深=知道哪些环节对当前场景不必要**」（不是会更多技巧，是会减法）。
- 资深的共性「add」是**防隐形成本/隐形失败**：idle 计费、KeepAlive、AssetInventory 下载、CC-BY 署名、对齐非词典 token、Android 系统引擎不可靠——这些都是文档深处的坑，初学者必踩 → 心智模型「**ASR 的坑在计费口径和平台边界，不在模型本身**」。

**近期工作流变化的根本原因**：
- 触发事件类型分布：**新模型 5** (gpt-4o-transcribe, Parakeet v2/v3, SenseVoice, Moonshine v2, Nova-3) / **新平台 API 1** (Apple SpeechAnalyzer) / **新工具(托管化) 1** (AssemblyAI Audio Intelligence) / **标准更新 1** (Open ASR Leaderboard 论文)。
- 主要驱动力 → **端侧模型成熟（SenseVoice/Moonshine/SpeechAnalyzer）+ 云 API 同质化压价（mini-transcribe/Nova-3）**双向挤压，把「成本尽量低 + 移动端」从难题变成有现成答案。Phase 2 外部驱动力 = 「端侧能力爆发 + 云价格战」。

**冷僻 / 信号薄弱自检**：
- workflow 数 = **8**（W1/W2a/W2b·W4/W3/W6/W7/W8，floor 4 ✅，远超阈值）。
- 一手 source 占比：manifest 21 源中 **verified_primary 20 + surrogate_primary 1 = 一手 100%**（github/官方开发者文档/WWDC），二手聚合站未进 manifest ✅。
- 资深差异点缺失：**0/8** workflow 缺（每条均 ≥2 处 skip/optimize/add）✅。
- 时效锚点：每条 workflow 均有 last_updated + 近期变化字段（W6 明确标稳态）✅。
- **诚实边界**：(1) 自托管 break-even 无统一公式，基于 RTFx 推断，已标 `[推断]`；(2) 中国云的流式/批量具体参数（重连/KeepAlive 机制）一手开发者文档多为 JS 渲染，本 track 的流式 SOP 细节以 OpenAI/Deepgram 一手文档为骨架，国产云按「同类机制」类推，落地需对照各家文档；(3) Apple SpeechAnalyzer 是 2025 新 API，本 track 步骤基于官方文档 + 工程博客，iOS26 实际行为可能随版本微调。
