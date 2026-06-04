# Track 02 — Tools / Engines：语音转文字 / ASR 应用工程

> 调研日期 2026-06-04。聚焦**选型 / 集成 / 优化**：云 API 横评 + 计费、开源模型横评、端侧/移动 SDK、选型决策树、成本优化 + 避坑。
> Locale=zh-CN（受众中文，canon 全球）。重点维度：准确率(WER/CER) × 延迟(流式/RTF) × **成本（尽量低）** × **移动端/离线**。

---

## Source Manifest

| source_id | url | bucket | last_checked | author/host | one-line note |
|-----------|-----|--------|--------------|-------------|---------------|
| T02-S001 | https://arxiv.org/abs/2510.06961 | verified_primary | 2026-06-04 | HF Audio et al | Open ASR Leaderboard 论文，WER/RTFx 标准化横评 |
| T02-S002 | https://huggingface.co/blog/open-asr-leaderboard | verified_primary | 2026-06-04 | Hugging Face | 多语种+长音频 track 趋势解读 |
| T02-S003 | https://github.com/openai/whisper | verified_primary | 2026-06-04 | OpenAI | Whisper repo，模型尺寸/参数/MIT |
| T02-S004 | https://github.com/SYSTRAN/faster-whisper | verified_primary | 2026-06-04 | SYSTRAN | CTranslate2 重实现，4x 加速+int8 |
| T02-S005 | https://github.com/ggml-org/whisper.cpp | verified_primary | 2026-06-04 | ggml-org | C/C++ Whisper，CoreML/Metal/移动/量化 |
| T02-S006 | https://github.com/huggingface/distil-whisper | verified_primary | 2026-06-04 | Hugging Face | 蒸馏 Whisper，6x 快/50%小/英语 |
| T02-S007 | https://github.com/NVIDIA/NeMo | verified_primary | 2026-06-04 | NVIDIA | NeMo，Parakeet/Canary 出处 |
| T02-S008 | https://github.com/modelscope/FunASR | verified_primary | 2026-06-04 | 阿里 ModelScope | FunASR，Paraformer/SenseVoice 工具箱 MIT |
| T02-S009 | https://github.com/FunAudioLLM/SenseVoice | verified_primary | 2026-06-04 | 阿里 FunAudioLLM | SenseVoice repo，中粤强/15x 快 |
| T02-S010 | https://huggingface.co/FunAudioLLM/SenseVoiceSmall | verified_primary | 2026-06-04 | 阿里 FunAudioLLM | SenseVoice-Small 卡片，70ms/10s |
| T02-S011 | https://github.com/FireRedTeam/FireRedASR | verified_primary | 2026-06-04 | 小红书 FireRed | 中文 SOTA 开源 ASR（含方言/歌词） |
| T02-S012 | https://arxiv.org/pdf/2501.14350 | verified_primary | 2026-06-04 | FireRed Team | FireRedASR 论文，中文 CER benchmark |
| T02-S013 | https://github.com/Picovoice/speech-to-text-benchmark | verified_primary | 2026-06-04 | Picovoice | 开源 STT WER benchmark（含模型 MB） |
| T02-S014 | https://arxiv.org/abs/2410.15608 | verified_primary | 2026-06-04 | Useful Sensors | Moonshine 论文，边缘端 5x 省算力 |
| T02-S015 | https://arxiv.org/abs/2602.12241 | verified_primary | 2026-06-04 | Moonshine AI | Moonshine v2 流式编码器，低延迟 SOTA |
| T02-S016 | https://github.com/alphacep/vosk-api | verified_primary | 2026-06-04 | Alpha Cephei | Vosk 离线 ASR，50MB/20+语言/移动 |
| T02-S017 | https://modal.com/blog/open-source-stt | verified_primary | 2026-06-04 | Modal | 开源 STT 横评（WER/RTFx/license） |
| T02-S018 | https://northflank.com/blog/best-open-source-speech-to-text-stt-model-in-2026-benchmarks | verified_primary | 2026-06-04 | Northflank | 2026 开源 STT benchmark 长稿 |
| T02-S019 | https://developer.apple.com/videos/play/wwdc2025/277/ | verified_primary | 2026-06-04 | Apple | WWDC25 SpeechAnalyzer（iOS26 端侧） |
| T02-S020 | https://deepgram.com/pricing | surrogate_primary | 2026-06-04 | Deepgram | vendor pricing — Nova-3 逐档定价 |
| T02-S021 | https://deepgram.com/learn/introducing-nova-3-speech-to-text-api | surrogate_primary | 2026-06-04 | Deepgram | vendor blog — Nova-3 WER 5.26% 宣称 |
| T02-S022 | https://www.assemblyai.com/pricing | surrogate_primary | 2026-06-04 | AssemblyAI | vendor pricing — Universal-3/2 定价 |
| T02-S023 | https://cloud.google.com/speech-to-text/pricing | surrogate_primary | 2026-06-04 | Google Cloud | vendor pricing — Chirp/STT 定价 |
| T02-S024 | https://azure.microsoft.com/en-us/pricing/details/cognitive-services/speech-services/ | surrogate_primary | 2026-06-04 | Microsoft Azure | vendor pricing — Speech STT 定价 |
| T02-S025 | https://aws.amazon.com/transcribe/pricing/ | surrogate_primary | 2026-06-04 | AWS | vendor pricing — Transcribe 阶梯定价 |
| T02-S026 | https://developers.openai.com/api/docs/pricing | surrogate_primary | 2026-06-04 | OpenAI | vendor pricing — gpt-4o-transcribe 等 |
| T02-S027 | https://cloud.tencent.com/document/product/1093/35686 | surrogate_primary | 2026-06-04 | 腾讯云 | vendor docs — ASR 资源包逐档价 |
| T02-S028 | https://help.aliyun.com/zh/isi/product-overview/billing-10 | surrogate_primary | 2026-06-04 | 阿里云 ISI | vendor docs — 智能语音交互逐档价 |
| T02-S029 | https://www.volcengine.com/theme/3774901-Y-7-1 | verified_primary | 2026-06-04 | 字节火山引擎 | vendor pricing — 语音识别资源包阶梯 |
| T02-S030 | https://www.xfyun.cn/services/lfasr | surrogate_primary | 2026-06-04 | 科大讯飞 | vendor docs — 语音转写产品页 |
| T02-S031 | https://picovoice.ai/docs/leopard/ | surrogate_primary | 2026-06-04 | Picovoice | vendor docs — Leopard/Cheetah 端侧 SDK |
| T02-S032 | https://huggingface.co/blog/open-asr-leaderboard | verified_primary | 2026-06-04 | Hugging Face | （同 S002）多语种 track 注：缺中文 |
| T02-S033 | https://arxiv.org/pdf/2311.00430 | verified_primary | 2026-06-04 | HF (Gandhi et al) | Distil-Whisper 论文，1% WER 内 |

> **Bucket 说明**：arxiv/github/huggingface/modal-blog/northflank-blog/apple-developer/volcengine 主域 = `verified_primary`（verifier 自动判定）。各厂商**官方定价/文档页**（deepgram/assemblyai/google/azure/aws/openai/腾讯/阿里/讯飞/picovoice）verifier 默认降 `secondary`，但属一手 vendor docs/pricing，按 Surrogate Policy 升 `surrogate_primary`，note 标 `vendor docs/pricing`。**未收录任何黑名单**（知乎/公众号/CSDN/百度百科/G2/Capterra 全部丢弃）。

---

## 总览（按 tier 分组）

### 必备层（8 个）

| 工具/引擎 | 一句话 | Decay | Sources |
|------|--------|-------|---------|
| OpenAI Whisper (large-v3 / turbo) | 开源多语种 ASR 事实标准，99 语言，生态最厚 | low | S001,S003,S017 |
| faster-whisper (CTranslate2) | Whisper 的 4x 加速运行时 + int8 量化，自托管默认选 | low | S004,S017 |
| whisper.cpp (+CoreML/Metal) | C/C++ Whisper，端侧/移动/量化首选 | low | S005 |
| Deepgram Nova-3 | 流式 ASR 第一梯队，延迟+准确率均衡，自托管可选 | medium | S020,S021 |
| AssemblyAI Universal | 异步批量最便宜云 API 之一（$0.15/hr），100+语言 | medium | S022 |
| OpenAI Transcribe API (gpt-4o / mini) | LLM 系 ASR，mini $0.003/min，省事接入 | medium | S026 |
| FunASR / Paraformer / SenseVoice | 中文 ASR 开源工具箱，中粤方言强、非自回归快 | low | S008,S009,S010 |
| Picovoice Leopard / Cheetah | 端侧离线 SDK，<40MB，移动/嵌入式商用 | medium | S013,S031 |

### 场景特化层（7 个）

| 工具/引擎 | 一句话 | Decay | Sources |
|------|--------|-------|---------|
| NVIDIA Parakeet (TDT 0.6B v2/v3) | 极致吞吐 RTFx~3386，离线批量神器，v3 多语种 | medium | S001,S007,S017 |
| NVIDIA Canary (Qwen 2.5B) | Open ASR 榜首 5.63% WER，高准确率（医疗/金融） | medium | S001,S007,S017 |
| distil-whisper (large-v3.5) | 蒸馏 Whisper，6x 快/50%小，1% WER 内（英语） | medium | S006,S033 |
| FireRedASR (AED/LLM 1.1B) | 中文 SOTA 开源（AISHELL/WenetSpeech），方言+歌词 | medium | S011,S012 |
| 中国云 ASR（讯飞/火山/阿里/腾讯/百度） | 中文+方言场景成熟、合规、￥0.7–3.5/hr 阶梯 | medium | S027,S028,S029,S030 |
| Apple SpeechAnalyzer / SFSpeechRecognizer | iOS 端侧免费 ASR，隐私/零成本/长音频(iOS26) | low | S019 |
| Vosk | 50MB 离线、20+语言、移动/嵌入式/老设备 | low | S016 |

### 新兴层（2 个）

| 工具/引擎 | 一句话 | Decay | Sources |
|------|--------|-------|---------|
| Moonshine v2 (Useful/Moonshine AI) | 流式编码器端侧 ASR，50ms 延迟，6x 小同精度 | high | S014,S015 |
| Deepgram Nova-3 Flux | 实时多语种 36+ 语言 + 句中 code-switching | high | S021 |

---

## 云端 ASR API 横评 + 计费（核心：成本尽量低）

> **比价口径**：尽量统一到 USD/min 与 USD/hr（中国厂商列￥/hr）。**流式(streaming/实时)** vs **批量(pre-recorded/async/录音文件)** 区分；流式普遍更贵。所有价为 list price（PAYG），未含量级折扣。

### 海外云 API 价格对比表

| 厂商/模型 | 批量(USD/min) | 批量(USD/hr) | 流式(USD/min) | 流式(USD/hr) | 免费额度 | 中文 | 端侧/自托管 | evidence |
|---|---|---|---|---|---|---|---|---|
| **AssemblyAI** Universal-2 | $0.0025 | **$0.15** | $0.0025（U-Streaming） | $0.15 | $50 credit | 100+语言 | 否 | S022 |
| **AssemblyAI** Universal-3 Pro | $0.0035 | $0.21 | $0.0075 | $0.45 | $50 credit | 100+语言 | 否 | S022 |
| **Deepgram** Nova-3 单语 | $0.0043 | $0.26 | $0.0048 | $0.29 | $200 credit | 45+语言 | **是(self-host)** | S020 |
| **Deepgram** Nova-3 多语 | — | $0.0078–0.0092* | $0.0058 | $0.35 | $200 credit | 45+语言 | 是 | S020 |
| **OpenAI** gpt-4o-mini-transcribe | **$0.003** | $0.18 | 同价(支持流式) | $0.18 | 无 | 多语种 | 否 | S026 |
| **OpenAI** gpt-4o-transcribe | $0.006 | $0.36 | $0.006 | $0.36 | 无 | 多语种 | 否 | S026 |
| **OpenAI** whisper-1 (API) | $0.006 | $0.36 | 不支持流式 | — | 无 | 99语言 | 否(=自托管开源) | S026 |
| **Google** Cloud STT (Chirp) | ~$0.016（量大→$0.004） | ~$0.96→$0.24 | ~$0.016 | ~$0.96 | 60 min/月 | 支持 | on-prem 版另计 | S023 |
| **Azure** Speech 标准 | $0.003（批量$0.18/hr） | **$0.18(批量)** | $0.0167 | **$1.00(实时)** | 5 hr/月 | 支持 | 容器版 | S024 |
| **AWS** Transcribe T1 | **$0.024** | $1.44 | $0.024 | $1.44 | 60 min/月×12月 | 支持 | 否 | S025 |
| **AWS** Transcribe T4(5M+ min) | $0.0078 | $0.47 | — | — | — | 支持 | 否 | S025 |

\* Deepgram 多语种批量页面标注单位混乱（$0.0078–0.0092 标为 "/hour" 但数量级实为 /min，按 Nova-3 量级应理解为约 $0.0078/min ≈ $0.47/hr）；以官方 pricing 页为准 (evidence: [T02-S020])。

**海外最便宜结论**：
- **批量最便宜：AssemblyAI Universal-2 $0.15/hr**（异步可接受时），其次 Azure 批量 $0.18/hr (evidence: [T02-S022, T02-S024])。
- **流式最便宜：AssemblyAI Universal-Streaming $0.15/hr**（但**按 WebSocket 开-关时长计费，含 idle**，是大坑），Deepgram 流式约 $0.29/hr 但按音频秒计、无 idle 坑 (evidence: [T02-S022, T02-S020])。
- **省事+便宜：OpenAI gpt-4o-mini-transcribe $0.003/min ($0.18/hr)**，支持流式，接入成本最低 (evidence: [T02-S026])。
- **最贵踩雷：AWS Transcribe T1 $0.024/min（$1.44/hr）**、Azure 实时 $1.00/hr——小量级别用，除非已在该云生态 (evidence: [T02-S025, T02-S024])。

### 中国云 ASR 价格对比表（￥/hr，PAYG/资源包）

| 厂商 | 实时(￥/hr) | 录音文件/批量(￥/hr) | 量级最低价 | 免费额度 | 备注 | evidence |
|---|---|---|---|---|---|---|
| **腾讯云** | 3.2(标)→1.0(30万hr包) | 1.75(标)→**0.7**(30万hr包) | 录音 0.7 | 资源包 | 极速版 2.4→1.2；一句话 ￥3/千次 | S027 |
| **阿里云 ISI** | 3.5(标)→1.0(5000hr) | 2.5(标)→**0.8**(25万hr包) | 录音 0.8 | 新用户 3 个月 | 只对语音段计费(VAD) | S028 |
| **字节火山引擎** | 3.0→**1.0**(50万hr包) | 1.7(标准版起) | 流式 1.0 | 特惠活动 | 流式 500hr￥1500 起 | S029 |
| **科大讯飞** | 实时转写另计 | 机器快转 **￥0.33/min**(≈￥20/hr) | — | 有免费额度 | 人工精转￥2.17/min 起(贵) | S030 |

**中国云最便宜结论**：
- **批量大量级最便宜：腾讯云录音文件 ￥0.7/hr（30 万小时包）/ 阿里 ￥0.8/hr**，约合 **$0.10/hr**，比海外便宜 (evidence: [T02-S027, T02-S028])。
- **流式：火山/腾讯/阿里大包均可压到 ￥1.0/hr (~$0.14/hr)** (evidence: [T02-S029, T02-S027, T02-S028])。
- **讯飞机器快转 ￥0.33/min ≈ ￥20/hr** 看似贵，但那是「听见」消费级单价；开放平台资源包另算——**面向消费者按分钟、面向开发者按资源包**两套口径，别混 (evidence: [T02-S030])。
- 阿里/腾讯均**只对 VAD 判定的语音段计费**，静音不计——天然省钱 (evidence: [T02-S028])。

### 准确率 vs 厂商宣称（保留矛盾）

- **Deepgram 官方宣称** Nova-3 批量中位 WER **5.26%**、流式 6.84%（2703 个 9 领域生产音频），称比"次优竞品 10% WER"领先 47.4% (evidence: [T02-S021])。**这是厂商自测**，第三方 Open ASR Leaderboard 上闭源 API 与开源 SOTA（Canary 5.63% 英语）量级相近，但**测试集不同不可直接比**——厂商 benchmark 用自家生产数据，学术榜用公开数据集，**矛盾保留**：不要拿 Deepgram 5.26% 直接对比 Whisper 在 LibriSpeech 的 3.7% (evidence: [T02-S021, T02-S001, T02-S013])。
- **Picovoice 自测 benchmark**（LibriSpeech test-clean）：Amazon 2.3% / Azure 2.9% / Whisper-large-v3 3.7% / Google 5.3% / Leopard 5.1% / IBM Watson 10.9% (evidence: [T02-S013])。**注意**：这是 Picovoice 自家 repo，对自家 Leopard 友好，且单一数据集；LibriSpeech 是干净朗读，真实嘈杂场景排名会变 (evidence: [T02-S013])。

---

## 开源模型横评

> 指标：WER(英语短音频，Open ASR Leaderboard) / CER(中文) / RTFx(越大越快，1 小时音频几秒转完) / 参数量 / 语言 / license。

### 英语/多语种横评（Open ASR Leaderboard，权威第三方）

| 模型 | WER% | RTFx | 参数 | 语言 | License | 流式 | evidence |
|---|---|---|---|---|---|---|---|
| **NVIDIA Canary-Qwen-2.5B** | **5.63**(榜首) | 418 | 2.5B | 英 | Apache-2.0 | 否(Conformer+LLM) | S001,S007,S017 |
| **NVIDIA Parakeet TDT 0.6B v2** | 6.05 | **3386** | 600M | 英 | CC-BY-4.0 | 流式 160ms(v3) | S001,S007,S017 |
| **NVIDIA Parakeet TDT 0.6B v3** | 6.32 | 3333 | 600M | **25 欧语** | CC-BY-4.0 | 流式 | S001,S007 |
| **IBM Granite-Speech-3.3-8B** | 5.85 | 31 | 8B | 英法德西日+中译 | Apache-2.0 | 否 | S017 |
| **distil-whisper large-v3.5** | 7.21 | 202 | ~0.8B | 英 | MIT | 否 | S001,S006 |
| **OpenAI Whisper large-v3** | 7.44(短)/6.43(长) | 145(短)/68(长) | 1.55B | **99语言** | MIT | 否(原生) | S001,S003 |
| **Whisper large-v3-turbo** | ~10–12* | 216 | 809M | 多语种 | MIT | 否 | S017,S018 |

\* turbo 的 WER：HF 官方称"large-v3 半个点以内"；第三方 Modal/Northflank 测到 10–12%（不同数据集/长音频）——**矛盾保留**，turbo 是 v3 削 4 层解码器换 6x 速度，干净短音频接近 v3，长音频/嘈杂会掉 (evidence: [T02-S017, T02-S018, T02-S001])。

### 中文横评（CER，越低越好；FireRedASR 论文，公开测试集）

| 模型 | AISHELL-1 | AISHELL-2 | WenetSpeech-net | WenetSpeech-meeting | 参数 | License | evidence |
|---|---|---|---|---|---|---|---|
| **FireRedASR-AED** | **0.55** | **2.52** | **4.88** | **4.76** | 1.1B | repo 见 license | S011,S012 |
| **SenseVoice-L** | 2.09 | 3.04 | 6.01 | 6.73 | 1.6B | — | S012 |
| **Paraformer-Large** | 1.68 | 2.85 | 6.74 | 6.97 | 0.2B | MIT(FunASR) | S008,S012 |
| Whisper-large-v3(对比) | 较高(中文非强项) | — | — | — | 1.55B | MIT | S012 |

**中文结论**：**FireRedASR 是当前公开中文 SOTA**，CER 全面优于 SenseVoice-L / Paraformer / Whisper-large-v3 (evidence: [T02-S011, T02-S012])。但**Paraformer 仅 0.2B 参数就接近 SenseVoice-L 1.6B**——小模型/部署友好 (evidence: [T02-S012])。SenseVoice-Small（234M）非自回归，**70ms 转 10s 音频、15x 快于 Whisper-large**，中粤方言强 + 带情绪/事件检测 (evidence: [T02-S009, T02-S010])。

### 工具卡片（关键开源项目）

#### 1. OpenAI Whisper

- **One-liner**: 开源多语种 ASR 事实标准，99 语言，社区生态最厚。
- **Tier**: 必备
- **Maintainer**: OpenAI — https://github.com/openai/whisper
- **License**: MIT（代码+权重）(evidence: [T02-S003])
- **Maturity**: stars **101k**(2026-06-04)，模型 tiny 39M / base 74M / small 244M / medium 769M / large-v3 1.55B / turbo 809M (evidence: [T02-S003])
- **不适合/替代**: 原生**不支持流式**（30s 滑窗批处理）；要流式/极致吞吐用 Parakeet/Nova-3；要部署用 faster-whisper/whisper.cpp 而非原版 (evidence: [T02-S003, T02-S001])
- **Decay risk**: low（行业基础设施，3+ 年稳定）

#### 2. faster-whisper

- **One-liner**: Whisper 的 CTranslate2 重实现，4x 加速、显存更省、int8 量化，**自托管默认运行时**。
- **Tier**: 必备
- **Maintainer**: SYSTRAN — https://github.com/SYSTRAN/faster-whisper
- **License**: MIT；stars **23.4k**，v1.2.1(2025-10-31) (evidence: [T02-S004])
- **关键数据**: 同精度比 openai/whisper 快 4x（large-v2 GPU 1m03s vs 2m23s；small CPU 2m37s vs 6m58s）；int8 量化 GPU 显存 2926MB vs fp16 4708MB；支持 distil-large-v3 与 turbo (evidence: [T02-S004])
- **不适合/替代**: 它**不是新模型**只是更快的运行时；要端侧/移动用 whisper.cpp；要极致吞吐用 Parakeet (evidence: [T02-S004, T02-S001])
- **Decay risk**: low

#### 3. whisper.cpp

- **One-liner**: C/C++ Whisper，CoreML/Metal/CUDA/Vulkan + 移动 iOS/Android + 量化，**端侧首选**。
- **Tier**: 必备
- **Maintainer**: ggml-org — https://github.com/ggml-org/whisper.cpp
- **License**: MIT；stars **50.4k**，v1.8.6(2026-06-02) (evidence: [T02-S005])
- **关键**: 运行时零内存分配；Apple ANE/CoreML 比纯 CPU 快 ~3x；跑通 iPhone 13 实时；支持 Q5_0 等整数量化；WebAssembly 浏览器端 (evidence: [T02-S005])
- **不适合/替代**: 大批量服务端吞吐不如 Parakeet/faster-whisper(GPU)；要免依赖 iOS 端侧也可直接用 Apple SpeechAnalyzer (evidence: [T02-S005, T02-S019])
- **Decay risk**: low

#### 4. NVIDIA NeMo — Parakeet / Canary

- **One-liner**: NVIDIA 语音工具箱，Parakeet（极致吞吐 RTFx~3386）+ Canary（Open ASR 榜首 5.63% WER）。
- **Tier**: 场景特化
- **Maintainer**: NVIDIA — https://github.com/NVIDIA/NeMo
- **License**: Apache-2.0(框架)；模型 Parakeet CC-BY-4.0 / Canary CC-BY-4.0；stars **17.3k** (evidence: [T02-S007, T02-S017])
- **典型场景**: (a) 离线大批量转写（会议/讲座/播客）→ Parakeet TDT，1 小时音频约 1 秒转完；(b) 高准确率受限领域（医疗/金融/电信）→ Canary-Qwen (evidence: [T02-S017, T02-S001])
- **不适合/替代**: Parakeet v2 **英语 only**（v3 才 25 欧语，**无中文**）；要中文用 FunASR/FireRedASR；CC-BY-4.0 模型需署名 (evidence: [T02-S001, T02-S007])
- **Decay risk**: medium

#### 5. FunASR / Paraformer / SenseVoice

- **One-liner**: 阿里开源中文 ASR 工具箱，Paraformer/SenseVoice，中粤方言强、非自回归快、带说话人分离+情绪。
- **Tier**: 必备（中文场景）
- **Maintainer**: 阿里 ModelScope / FunAudioLLM — https://github.com/modelscope/FunASR
- **License**: MIT；FunASR stars **17.1k**，2026 仍活跃(vLLM/Dynamic VAD/v1.3.3)；SenseVoice stars **8.4k**，v1.0.0(2026-05-25) (evidence: [T02-S008, T02-S009])
- **关键**: SenseVoice-Small 234M 非自回归，70ms/10s，15x 快于 Whisper-large；Paraformer-zh 220M 中英；FunASR 含 cam++ 说话人分离 + OpenAI 兼容 API server + 流式(WebSocket) (evidence: [T02-S008, T02-S010])
- **端侧**: SenseVoice 可 ONNX/Libtorch 导出，经 sherpa-onnx 部署到 iOS/Android/树莓派 (evidence: [T02-S009])
- **不适合/替代**: 纯英语场景准确率不如 Parakeet/Canary；要中文最高准确率用 FireRedASR (evidence: [T02-S012, T02-S001])
- **Decay risk**: low

#### 6. FireRedASR

- **One-liner**: 小红书开源工业级中文 ASR，公开 Mandarin benchmark 新 SOTA，支持方言 + 歌词识别。
- **Tier**: 场景特化（中文最高准确率）
- **Maintainer**: FireRedTeam(小红书) — https://github.com/FireRedTeam/FireRedASR
- **License**: 见 repo（工业级开源）；AED 1.1B / LLM 版 (evidence: [T02-S011])
- **关键**: AED CER AISHELL-1 0.55 / WenetSpeech-meeting 4.76，全面优于 SenseVoice-L/Paraformer/Whisper-large-v3；LLM 版比 Seed-ASR 再降 8.4% 相对 CER (evidence: [T02-S012])
- **不适合/替代**: 1.1B 偏重，端侧吃力→端侧用 SenseVoice-Small/Paraformer；非中文场景无优势 (evidence: [T02-S012])
- **Decay risk**: medium

#### 7. Picovoice Leopard / Cheetah

- **One-liner**: 端侧离线 STK，Leopard(批量)/Cheetah(流式)，<40MB，移动/嵌入式商用。
- **Tier**: 必备（移动/嵌入式商用）
- **Maintainer**: Picovoice — https://picovoice.ai/docs/leopard/
- **License**: proprietary（商用 SDK，免费 tier）(evidence: [T02-S031])
- **关键**: Leopard WER 5.1% / 37MB；Cheetah(流式) WER 5.4% / 34MB（LibriSpeech 自测）；支持 Linux/Win/macOS/Android/iOS/树莓派/Jetson；Whisper-tiny 需 6x 算力 vs Leopard (evidence: [T02-S013, T02-S031])
- **定价**: 免费 tier 商用 **100 小时/月**；超出付费起步约 **$999**（早期创业 75% 折扣）(evidence: [T02-S031])
- **不适合/替代**: 闭源、自定义受限；纯免费端侧用 whisper.cpp/Apple/Vosk；中文支持弱于国产 (evidence: [T02-S031, T02-S005])
- **Decay risk**: medium

#### 8. Vosk

- **One-liner**: 50MB 离线 ASR，20+ 语言，移动/嵌入式/老设备/低算力。
- **Tier**: 场景特化
- **Maintainer**: Alpha Cephei — https://github.com/alphacep/vosk-api
- **License**: Apache-2.0；模型小(50MB)，大模型 2733MB (evidence: [T02-S016, T02-S013])
- **关键**: 零延迟流式 API、可重配词表、说话人识别；Python/Java/Node/C#/C++/Rust/Go 绑定；Android/iOS/树莓派 (evidence: [T02-S016])
- **WER**: Vosk-large 流式 5.4%（2733MB，体积大）(evidence: [T02-S013])
- **不适合/替代**: 准确率落后 Whisper/Parakeet 一档；大模型体积大；要高精度端侧用 whisper.cpp + small/medium (evidence: [T02-S013, T02-S005])
- **Decay risk**: low

#### 9.（新兴）Moonshine v2

- **One-liner**: 流式编码器端侧 ASR，专为实时转写/语音命令，50ms 延迟，6x 小模型同精度。
- **Tier**: 新兴
- **Maintainer**: Useful Sensors / Moonshine AI — https://github.com/moonshine-ai/moonshine
- **License**: 宽松开源（含 ar/zh/ja/ko/uk/vi 单语模型）(evidence: [T02-S014, T02-S015])
- **关键**: v1 Tiny 比 Whisper-tiny.en 省 5x 算力、WER 不增；v2 Tiny 50ms(5.8x 快于 Whisper-tiny)、Medium 258ms(43.7x 快于 Whisper-large-v3)，标准 benchmark SOTA WER (evidence: [T02-S014, T02-S015])
- **stability: experimental**（6 个月后形态可能变）
- **不适合/替代**: 生态远不如 Whisper；长音频/高精度仍看 Whisper/Parakeet；中文模型新、验证少 (evidence: [T02-S015])
- **Decay risk**: high

---

## 端侧 / 移动 SDK 对比（"移动端" + 隐私 + 离线 + 零/低成本）

| 方案 | 离线 | 包体 | 延迟 | 中文 | 成本 | 平台 | evidence |
|---|---|---|---|---|---|---|---|
| **Apple SpeechAnalyzer**(iOS26) | 是(仅端侧) | 系统内置 | 低，长音频优化 | 支持 | **免费** | iOS/macOS | S019 |
| **Apple SFSpeechRecognizer** | 端侧可选 | 系统内置 | 低 | 支持 | **免费** | iOS10+ | S019 |
| **Android SpeechRecognizer** | 是(机型相关) | 系统内置 | 低 | 支持 | **免费** | Android | S016(ctx) |
| **whisper.cpp + CoreML** | 是 | 模型 tiny73MB–small462MB | iPhone13 实时 | 99 语言 | **免费(MIT)** | iOS/Android/全平台 | S005,S013 |
| **Picovoice Cheetah/Leopard** | 是 | <40MB | 实时(流式) | 弱 | 100hr/月免费,后付费 | iOS/Android/嵌入式 | S013,S031 |
| **SenseVoice-Small (sherpa-onnx)** | 是 | 234M 模型 | 70ms/10s | **强(中粤)** | **免费** | iOS/Android/树莓派 | S009,S010 |
| **Vosk** | 是 | 50MB(小)/2.7GB(大) | 零延迟流式 | 支持 | **免费(Apache)** | iOS/Android/嵌入式 | S016 |
| **Moonshine v2** | 是 | tiny 极小 | 50ms | 单语 zh 模型 | **免费** | 边缘/移动 | S014,S015 |

**移动端首选结论**：
- **iOS 且不要求自定义模型 → Apple SpeechAnalyzer(iOS26)/SFSpeechRecognizer**：系统内置、端侧、免费、隐私最佳；iOS26 的 SpeechAnalyzer 专为长音频(讲座/会议)优化 (evidence: [T02-S019])。
- **跨平台 + 要 Whisper 级精度 + 免费 → whisper.cpp + CoreML/Metal**：iPhone 13 即可实时，MIT 可商用 (evidence: [T02-S005])。
- **中文移动端最佳 → SenseVoice-Small（经 sherpa-onnx）**：中粤强、70ms 极快、免费 (evidence: [T02-S009, T02-S010])。
- **要商用 SLA + 极小包体 + 嵌入式 → Picovoice**：<40MB，免费 100hr/月，但中文弱、闭源 (evidence: [T02-S031])。
- **超低算力老设备/语音命令 → Vosk 或 Moonshine v2**：50MB / 50ms (evidence: [T02-S016, T02-S015])。

---

## 选型决策树

### 决策树 A：你的核心约束是什么？（准确率 × 延迟 × 成本 × 移动/离线）

#### Branch 1: 必须端侧/离线（隐私、无网、零边际成本）
- **iOS 原生、不要自定义** → **Apple SpeechAnalyzer / SFSpeechRecognizer**（免费、系统内置、隐私）(evidence: [T02-S019])
- **跨平台、要 Whisper 级精度** → **whisper.cpp + CoreML/Metal**（MIT、iPhone13 实时）(evidence: [T02-S005])
- **中文为主** → **SenseVoice-Small（sherpa-onnx）**（中粤强、70ms）(evidence: [T02-S009, T02-S010])
- **商用 SLA + 极小包体 + 嵌入式** → **Picovoice Leopard/Cheetah**（<40MB，但闭源/中文弱）(evidence: [T02-S031])
- **超低算力/语音命令** → **Vosk(50MB)** 或 **Moonshine v2(50ms)** (evidence: [T02-S016, T02-S015])
- **不推荐**: 云 API（违背离线前提，且有边际成本）

#### Branch 2: 服务端、成本敏感、量大（"成本尽量低"）
##### Branch 2a: 能接受异步/批量
- **自有 GPU/愿自托管** → **faster-whisper(int8)** 或 **Parakeet TDT**（一旦量大边际成本≈电费，最便宜）(evidence: [T02-S004, T02-S001])
- **不想运维、海外** → **AssemblyAI Universal-2 $0.15/hr** 或 **OpenAI mini $0.18/hr** (evidence: [T02-S022, T02-S026])
- **中文、不想运维** → **腾讯云录音 ￥0.7/hr / 阿里 ￥0.8/hr（大资源包）** (evidence: [T02-S027, T02-S028])
##### Branch 2b: 需要实时/流式
- **海外** → **Deepgram Nova-3**（按秒计、无 idle 坑、流式强）；预算极紧用 AssemblyAI Streaming $0.15/hr 但**警惕 WebSocket idle 计费** (evidence: [T02-S020, T02-S022])
- **中文** → **火山/腾讯/阿里流式 ￥1.0/hr（大包）** (evidence: [T02-S029, T02-S027])
- **自托管流式** → **NeMo Parakeet 流式(160ms)** 或 FunASR 流式 (evidence: [T02-S007, T02-S008])

#### Branch 3: 准确率优先（医疗/金融/法务，错一个字代价高）
- **英语** → **NVIDIA Canary-Qwen-2.5B（5.63% WER 榜首）** 自托管，或云端 Deepgram Nova-3 / OpenAI gpt-4o-transcribe (evidence: [T02-S001, T02-S021, T02-S026])
- **中文** → **FireRedASR（公开 CER SOTA）** 自托管 (evidence: [T02-S011, T02-S012])
- **不推荐**: turbo/tiny/mini 这类省钱档（准确率换速度/成本，高风险场景不划算）(evidence: [T02-S017])

#### Branch 4: 离线大批量吞吐（几千小时归档/字幕）
- **英语** → **Parakeet TDT 0.6B（RTFx~3386，1hr 音频~1s）** (evidence: [T02-S001, T02-S017])
- **中文** → **Paraformer-Large / SenseVoice（15x 快于 Whisper）** (evidence: [T02-S008, T02-S010])
- **不推荐**: 原版 Whisper（慢且不流式）；至少换 faster-whisper (evidence: [T02-S003, T02-S004])

#### Branch 5: 快速验证/demo，先跑起来
- → **OpenAI gpt-4o-mini-transcribe**（$0.003/min、一个 API key、多语种）或本地 faster-whisper(turbo)（evidence: [T02-S026, T02-S004]）
- **不推荐**: 一上来自建 GPU 集群 / 自训模型（过早优化）

---

## 成本优化清单（"成本尽量低"专项）

- **端侧 = 边际成本归零**：能端侧就端侧。Apple/whisper.cpp/SenseVoice/Vosk **完全免费**，移动端无服务器账单 (evidence: [T02-S019, T02-S005, T02-S009])。
- **VAD 裁静音再送识别**：阿里/腾讯**只对语音段计费**，自己上传前用 VAD（如 Silero）裁掉静音，按时长计费的云 API（AWS/Google/OpenAI）能直接省钱 (evidence: [T02-S028])。
- **批量优先于流式**：同厂商批量普遍比流式便宜（Azure $0.18 vs $1.00/hr；AssemblyAI $0.15 vs Pro 流式 $0.45）。不需要实时就走异步 (evidence: [T02-S024, T02-S022])。
- **量级折扣/资源包**：AWS T1→T4 从 $0.024→$0.0078/min；中国云大资源包腰斩（腾讯 ￥1.75→0.7）。预估年用量直接买大包 (evidence: [T02-S025, T02-S027])。
- **int8/ggml 量化**：自托管用 faster-whisper int8（显存 2926 vs 4708MB）或 whisper.cpp Q5——同卡塞更多并发、降单位成本 (evidence: [T02-S004, T02-S005])。
- **小模型够用就别上大模型**：Paraformer 0.2B 接近 SenseVoice-L 1.6B；mini-transcribe 是 transcribe 的半价。准确率达标即止 (evidence: [T02-S012, T02-S026])。
- **自托管 break-even 估算**：云 API 约 $0.15–0.36/hr。自托管 Parakeet/faster-whisper 在单 GPU 上 RTFx 数百~数千，一张 L4/A10（约 $0.5–1/hr 云 GPU）每小时能转数百小时音频→**当月用量超过约几百小时、且有运维能力时，自托管单位成本低于云 API**；量小则云 API 更划算（无固定成本）。注：精确 break-even 取决于 GPU 单价与并发，公开 benchmark 未给统一公式，此为基于 RTFx 的推断 (evidence: [T02-S001, T02-S017]) `[推断]`。

---

## 避坑清单

- ❌ **不要只看跑分榜选型而忽略中文/流式**：Open ASR Leaderboard 榜首 Canary/Parakeet **英语 only 或仅 25 欧语，无中文**；中文要看 FireRedASR/Paraformer 的 CER 榜，是两套世界 (evidence: [T02-S001, T02-S007, T02-S012])。
- ❌ **不要忽略 AssemblyAI 流式的 WebSocket idle 计费**：按 open-to-close 时长计费，连接闲置 5 分钟=5 分钟账单。流式按"会话时长"而非"音频时长"是隐形成本 (evidence: [T02-S022])。
- ❌ **不要把 turbo/distil 当成 large-v3 等价物**：turbo 削解码器换 6x 速度，干净短音频接近、嘈杂/长音频 WER 掉到 10–12%；高风险场景别图快 (evidence: [T02-S017, T02-S001])。
- ❌ **不要忽略静音也计费**：按时长计费的云 API（AWS/Google/Azure/OpenAI）不裁静音=为空白付钱；阿里/腾讯才默认只算语音段 (evidence: [T02-S025, T02-S028])。
- ❌ **不要端侧无脑塞大模型导致包体/内存爆炸**：Whisper-large 1.5GB、Vosk 大模型 2.7GB 上移动端不现实；端侧用 tiny/base/SenseVoice-Small/Picovoice(<40MB) (evidence: [T02-S013, T02-S016])。
- ❌ **不要忽略 license 坑**：Parakeet/Canary 是 **CC-BY-4.0（需署名）**，Picovoice 闭源商用要付费；Whisper/faster-whisper/whisper.cpp/FunASR 才是 MIT/Apache 可放心商用 (evidence: [T02-S007, T02-S031, T02-S003, T02-S008])。
- ❌ **不要拿厂商自测 WER 跨家直接比**：Deepgram 5.26% 用自家生产数据、Picovoice benchmark 偏向 Leopard、Open ASR 用公开集——测试集不同不可比，要在**你自己的数据**上跑 A/B (evidence: [T02-S021, T02-S013, T02-S001])。
- ❌ **不要把原版 openai/whisper 直接上生产**：慢且不流式；服务端换 faster-whisper(GPU)/Parakeet，端侧换 whisper.cpp (evidence: [T02-S003, T02-S004, T02-S005])。

---

## Phase 2 提炼提示

**反复出现 ≥ 3 source 都强调的「工具选型原则」**（候选 playbook 规则）:
- **端侧能解决就端侧——边际成本归零 + 隐私**（出现于 S005 / S019 / S009 / S031）
- **准确率/速度/成本/多语种是四方权衡，没有全能王，按约束选**（出现于 S001 / S017 / S018）
- **中文与英语是两套榜单两套最优解，别用英语跑分指导中文选型**（出现于 S001 / S012 / S011）
- **厂商宣称 WER 不可跨家比，必须在自有数据上 A/B**（出现于 S021 / S013 / S001）
- **批量比流式便宜、量大买资源包、VAD 裁静音——三件套省钱**（出现于 S022 / S024 / S027 / S028）

**显著的工具流派分裂**（候选智识谱系条目）:
- **自托管开源派**（faster-whisper / whisper.cpp / NeMo / FunASR / FireRedASR；量大后单位成本最低、可控、隐私）**vs 云 API 托管派**（Deepgram / AssemblyAI / OpenAI / 三大云；零运维、按量付费、起步快）——决策轴是**用量规模 × 运维能力 × 隐私要求**。
- **架构分裂**：Encoder-Decoder(Whisper) vs CTC/TDT(Parakeet，极速) vs Conformer+LLM(Canary/FireRedASR-LLM，高精度) vs 非自回归(Paraformer/SenseVoice，快)——速度↔精度的帕累托前沿 (evidence: [T02-S001])。

**新兴工具信号**:
- 当前活跃/上升的新工具数: 2（Moonshine v2 流式端侧、Deepgram Nova-3 Flux 多语种实时 code-switching）
- 出现→主流速度估计: ~6–12 个月（ASR 模型迭代极快，turbo/Nova-3/Parakeet-v3/FireRedASR 都在 12 个月内起势）

**冷僻/信号薄弱**:
- 必备层 ≥ 8、场景特化 ≥ 7、新兴 ≥ 2，**信号充足，非冷僻行业**。
- 数据厚度强：arxiv/github/HF 一手 + 各厂商官方定价页齐全。
- 唯一薄弱点：**中国厂商官方定价页多为 JS 渲染，WebFetch 取不到**，部分￥价来自官方页搜索摘要（已标 surrogate_primary / vendor docs），建议 Phase 2 用时对火山引擎/讯飞具体档位做二次核对。
- 保留的核心矛盾：厂商自测 WER（Deepgram 5.26% / Picovoice 自家友好）vs 第三方 Open ASR Leaderboard，**测试集不同不可直接比**——SKILL.md 选型节须提醒"在自己数据上 A/B"。
