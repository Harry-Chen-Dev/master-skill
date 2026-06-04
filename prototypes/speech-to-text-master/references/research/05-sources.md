# Track 05 — Sources：语音转文字 / ASR 应用工程（要持续追踪的活信息源）

> Research date 2026-06-04 | Locale=zh-CN（canon 全球） | Track 05 SOURCES
> **本 track 的特殊性**：ASR 是**模型/价格变化最快**的 tech 领域之一（Nova-3 / Parakeet-v3 / Slam-1 / Qwen3-ASR / Moonshine v2 都在 12 个月内起势，定价季度级调整）。所以本 track 的核心不是「订阅哪个 newsletter 听人聊天」，而是 **「选型 ground truth + 官方版本/定价 changelog」要钉死哪几页、多久刷一次**。
> **诚实判断（先说结论）**：ASR 的**专门媒体层很薄**——没有 Latent Space 级别的「ASR 专属」长访谈 podcast，也几乎没有持续的 ASR 专属 newsletter。真知识沉淀在 **① 第三方 benchmark 榜单（Open ASR Leaderboard / Artificial Analysis）② 厂商官方 changelog/pricing ③ arXiv + HF papers ④ 少数工程博客（Pete Warden / 厂商 eng blog / 自托管成本 benchmark 长稿）**。"newsletter / podcast / conference / community" 四类对本行业是**弱信号补充**，不是主力。下面分类如实标厚薄。

---

## Source Manifest

| source_id | url | bucket | last_checked | author/host | one-line note |
|-----------|-----|--------|--------------|-------------|---------------|
| T05-S001 | https://huggingface.co/spaces/hf-audio/open_asr_leaderboard | verified_primary | 2026-06-04 | Hugging Face (hf-audio) | **选型 ground truth #1**：86 系统/12 数据集 WER×RTFx 活榜 |
| T05-S002 | https://arxiv.org/abs/2510.06961 | verified_primary | 2026-06-04 | Srivastav et al (HF) | Open ASR Leaderboard 论文(v4)，多语+长音频方法论 |
| T05-S003 | https://github.com/huggingface/open_asr_leaderboard | verified_primary | 2026-06-04 | Hugging Face | 榜单 repo：评测脚本/文本归一化/可复现 |
| T05-S004 | https://artificialanalysis.ai/speech-to-text | secondary | 2026-06-04 | Artificial Analysis | **第三方 STT 横评**：准确率×速度×**价格/1000min** 三轴 |
| T05-S005 | https://paperswithcode.com/task/speech-recognition | secondary | 2026-06-04 | Papers with Code | SOTA 表 + 数据集索引(AISHELL/LibriSpeech/WenetSpeech) |
| T05-S006 | https://platform.openai.com/docs/guides/speech-to-text | verified_primary | 2026-06-04 | OpenAI | 官方 STT 文档(gpt-4o-transcribe/whisper-1) |
| T05-S007 | https://developers.deepgram.com/changelog | verified_primary | 2026-06-04 | Deepgram | **版本 changelog**：Nova-3/Flux 逐条发布(2026 仍频繁) |
| T05-S008 | https://www.assemblyai.com/changelog | secondary | 2026-06-04 | AssemblyAI | vendor changelog：Slam-1/Universal-3 Pro 发布流 |
| T05-S009 | https://www.assemblyai.com/blog | verified_primary | 2026-06-04 | AssemblyAI | 工程博客：模型评测/streaming/医疗模式长文 |
| T05-S010 | https://deepgram.com/learn | secondary | 2026-06-04 | Deepgram | 工程博客：Nova-3 WER 宣称/语言扩展(vendor 自测) |
| T05-S011 | https://huggingface.co/papers | verified_primary | 2026-06-04 | Hugging Face | 每日 papers 流(社区投票)，含 audio/ASR |
| T05-S012 | https://huggingface.co/blog?tag=audio | verified_primary | 2026-06-04 | Hugging Face | audio 官方博客(2026-05 仍更)，榜单解读/部署 |
| T05-S013 | https://arxiv.org/list/eess.AS/recent | verified_primary | 2026-06-04 | arXiv | eess.AS 最新投稿流(语音处理论文一手) |
| T05-S014 | https://arxiv.org/list/cs.CL/recent | verified_primary | 2026-06-04 | arXiv | cs.CL 最新投稿流(含 LLM-based ASR) |
| T05-S015 | https://github.com/ggml-org/whisper.cpp/releases | verified_primary | 2026-06-04 | ggml-org | whisper.cpp release(端侧版本，~月更) |
| T05-S016 | https://github.com/SYSTRAN/faster-whisper/releases | verified_primary | 2026-06-04 | SYSTRAN | faster-whisper release(自托管运行时版本) |
| T05-S017 | https://github.com/k2-fsa/sherpa-onnx | verified_primary | 2026-06-04 | k2-fsa | **端侧部署运行时**：iOS/Android/RTOS，2026 持续上新模型 |
| T05-S018 | https://github.com/moonshine-ai/moonshine | verified_primary | 2026-06-04 | Moonshine AI | 端侧低延迟 ASR repo，v2/Voice 活跃 |
| T05-S019 | https://petewarden.com/ | secondary | 2026-06-04 | Pete Warden | **端侧情报一手博客**(Moonshine 作者，2026-02 仍更) |
| T05-S020 | https://picovoice.ai/blog/ | verified_primary | 2026-06-04 | Picovoice | 端侧工程博客(Android/RN/Python STT 指南，2026 更) |
| T05-S021 | https://northflank.com/blog/best-open-source-speech-to-text-stt-model-in-2026-benchmarks | verified_primary | 2026-06-04 | Northflank | **自托管成本 benchmark 长稿**(开源 STT 横评) |
| T05-S022 | https://modal.com/blog | verified_primary | 2026-06-04 | Modal | 工程博客：开源 STT 部署/WER/RTFx/成本横评 |
| T05-S023 | https://github.com/modelscope/FunASR | verified_primary | 2026-06-04 | 阿里 DAMO | **中文 ASR 主源**：release notes(v1.3.3/Fun-ASR/Qwen3-ASR) |
| T05-S024 | https://www.modelscope.cn/models?name=asr | secondary | 2026-06-04 | 阿里 ModelScope | 中文模型库 ASR 检索(Qwen3-ASR/GLM-ASR/Paraformer) |
| T05-S025 | https://www.volcengine.com/product/asr | verified_primary | 2026-06-04 | 字节火山引擎 | 官方产品/文档页(豆包语音识别/Seed-ASR) |
| T05-S026 | https://www.xfyun.cn/services/lfasr | secondary | 2026-06-04 | 科大讯飞 | 官方产品页：语音转写(vendor docs) |
| T05-S027 | https://www.reddit.com/r/LocalLLaMA/ | reference | 2026-06-04 | Reddit | **端侧社区**：parakeet.cpp/whisper 量化实战讨论 |
| T05-S028 | https://www.reddit.com/r/MachineLearning/ | reference | 2026-06-04 | Reddit | ML 社区：论文讨论/新模型首发风向 |
| T05-S029 | https://discuss.huggingface.co/c/audio/ | secondary | 2026-06-04 | Hugging Face | HF audio 论坛(transformers/部署 Q&A) |

> **Bucket 说明**：arxiv / github / huggingface(含 spaces/papers/blog) / 各厂商**官方文档与第一方 blog**(platform.openai.com、developers.deepgram.com、assemblyai.com/blog、picovoice.ai/blog、northflank.com/blog、modal.com/blog、volcengine.com) = `verified_primary`(verifier 自动判 or 一手 vendor 升级)。
> - `artificialanalysis.ai`(S004) verifier 默认 secondary，但属**第三方独立 benchmark 机构一手发布**，按 Surrogate Policy 升 `surrogate_primary`，note 标第三方榜单。
> - `assemblyai.com/changelog`(S008)、`deepgram.com/learn`(S010)、`modelscope.cn`(S024)、`xfyun.cn`(S026)、`discuss.huggingface.co`(S029) verifier 判 secondary，保留为 secondary（vendor changelog / vendor docs / 官方论坛，仍是第一方但 verifier 路径判 secondary，不强升）。
> - Reddit(S027/S028) = `reference`(社区聚合，作风向/discovery，非真伪源)。
> - **黑名单零收录**：知乎/公众号(mp.weixin)/百度百科/CSDN/简书/掘金、G2/Capterra 全部命中即丢；中国 ASR 动态大量沉在量子位/机器之心/知乎/公众号(黑名单)——本 track 仅取 FunASR repo / ModelScope / 火山·讯飞官方 first-party，**专门媒体层中文侧尤其薄**（见末尾诚实判断）。

---

## 总览（按 type 分组）

### 基准 / 榜单（选型 ground truth）— 5 个 ★本 track 主力

| Source | Cadence | Tier | 投入产出 | 一手? | One-liner |
|--------|---------|------|---------|------|-----------|
| Open ASR Leaderboard (Space) | rolling(社区提交) | practitioner+senior | **high** | 一手 | 开源+闭源 WER×RTFx 活榜，选型第一参照 (S001) |
| Open ASR Leaderboard 论文(arXiv 2510.06961) | 版本制(v4,2025-10) | senior | high | 一手 | 评测方法论：文本归一化/多语/长音频 (S002) |
| Artificial Analysis STT | rolling(7 日中位) | practitioner | high | 一手(第三方) | 准确率×速度×**$/1000min** 三轴横评 (S004) |
| Papers with Code — Speech Recognition | rolling | mixed | medium | 二手 | SOTA 表 + 数据集 leaderboard 索引 (S005) |
| HF Open ASR Leaderboard repo | rolling | senior | medium | 一手 | 想自己跑评测/复现的脚本源 (S003) |

### 官方文档 / 定价 / changelog（要追版本与价）— 9 个 ★本 track 主力

| Source | Cadence | 一手? | 投入产出 | One-liner |
|--------|---------|------|---------|-----------|
| OpenAI STT 文档 | 不定(随模型) | 一手 | high | gpt-4o-transcribe/mini/whisper-1 能力+价 (S006) |
| Deepgram changelog | 高频(2026 月内多条) | 一手 | high | Nova-3/Flux 版本与语言扩展逐条 (S007) |
| AssemblyAI changelog | 月级 | 一手 | high | Slam-1/Universal-3 Pro/医疗模式发布流 (S008) |
| AssemblyAI blog | 月级 | 一手 | medium | 模型评测/streaming 工程长文 (S009) |
| Deepgram learn(blog) | 月级 | 一手 | medium | Nova-3 WER 宣称(vendor 自测，需校验) (S010) |
| whisper.cpp releases | ~月更 | 一手 | high | 端侧版本/量化/CoreML 更新 (S015) |
| faster-whisper releases | 季度级 | 一手 | medium | 自托管运行时版本(large-v3/turbo 支持) (S016) |
| FunASR releases | 高频(2026 活跃) | 一手 | high | 中文：v1.3.3/Fun-ASR/Qwen3-ASR/GLM-ASR (S023) |
| 火山引擎 / 讯飞 / ModelScope 官方 | 不定 | 一手 | medium | 中文 vendor 产品/定价/模型库 (S025,S026,S024) |

> **定价页**：海外(OpenAI/Deepgram/AssemblyAI/Google/Azure/AWS)与中国(腾讯/阿里/火山/讯飞)的逐档**价格表已在 `02-tools.md` Source Manifest(T02-S020~S031)收录并比价**，本 track 不重复贴；追价时以那批 vendor pricing URL + 本表 changelog 为准。**定价页建议季度刷一次**(ASR 单价季度级波动)。

### 论文流 — 4 个

| Source | Cadence | Tier | 投入产出 | One-liner |
|--------|---------|------|---------|-----------|
| arXiv eess.AS recent | 每日 | senior | medium | 语音处理论文一手投稿流 (S013) |
| arXiv cs.CL recent | 每日 | senior | medium | 含 LLM-based ASR / 多语 (S014) |
| HF papers(daily) | 每日 | practitioner | medium | 社区投票过滤过的热点论文 (S011) |
| (Open ASR 论文见榜单组 S002) | — | — | — | 方法论锚点 |

### 工程博客 / 端侧情报 — 5 个

| Source | Cadence | Host | 投入产出 | One-liner |
|--------|---------|------|---------|-----------|
| Pete Warden's blog | 不定(2026-02 活跃) | Pete Warden | high | 端侧 ASR 一手立场(Moonshine 作者) (S019) |
| Picovoice blog | 月级 | Picovoice | medium | Android/RN/Python 端侧 STT 实操指南 (S020) |
| Northflank STT benchmark | 不定(年度大稿) | Northflank | high | 自托管开源 STT 成本/WER 长稿 (S021) |
| Modal blog | 不定 | Modal | medium | 开源 STT 部署/RTFx/成本横评 (S022) |
| HF audio blog | 不定(2026-05 更) | Hugging Face | high | 榜单解读/部署/insanely-fast-whisper (S012) |

### 社区 — 3 个（弱信号 / discovery）

| Community | Platform | 投入产出 | One-liner |
|-----------|----------|---------|-----------|
| r/LocalLLaMA | Reddit | medium | 端侧实战风向(parakeet.cpp/量化)，新工具最早冒头处 (S027) |
| r/MachineLearning | Reddit | low | 论文讨论/新模型首发，信噪比低 (S028) |
| HF audio forum | discuss.huggingface.co | low | transformers/部署 Q&A，工具用法 (S029) |

### Conference — 0 专属 / Dataset — 见榜单

- **Conference**：ASR **无专属年度大会**；相关工作发表在 **Interspeech / ICASSP / ICLR / NeurIPS**(通用语音+ML 会议)，非本行业专属信息源，故不单列(诚实标 N/A)。想追前沿直接看 arXiv + HF papers 比等会议快。
- **Dataset / Benchmark**：核心评测集(LibriSpeech / AISHELL-1·2 / WenetSpeech / FLEURS / Earnings22)均**通过 Open ASR Leaderboard(S001) 与 Papers with Code(S005) 索引**，不单列。中文 CER 基准见 `02-tools.md` FireRedASR 论文表。

---

## 关键 Source 卡片（仅展开 top 信号源）

### ★ 1. Open ASR Leaderboard（Space + 论文 + repo）

- **Type**: dataset/benchmark | **URL**: https://huggingface.co/spaces/hf-audio/open_asr_leaderboard (S001)
- **Maintainer**: Hugging Face hf-audio 团队（推动者 Vaibhav Srivastav / Steveeeeeeen，见 `01-figures.md` T01-S013/S015）
- **Cadence**: rolling（社区持续提交模型）；论文版本制(v4, 2025-10)
- **Last activity**: 2026-03-27 仍在更新（86 系统/74 开源/12 数据集）；2026-05 HF 博客 "Adding Benchmaxxer Repellant" 强化**反 benchmark 刷分**机制 (evidence: [T05-S001, T05-S012])
- **One-liner**: ASR 选型的 **ground truth #1**——同一文本归一化下报 WER(准确率) + RTFx(速度)，开源与闭源 API 同台；2025-10 起新增**多语种 + 长音频**赛道，补齐了过去只测英语短音频的短板 (evidence: [T05-S001, T05-S002])
- **典型内容**: 英语短/长音频 + 多语种短音频三 track 排名；多语种 Microsoft Phi-4 Multimodal / NVIDIA Canary-1B-v2 领先(WER 3–5%)；长音频 ElevenLabs 领先，开源里 Whisper-large-v3 最高 (evidence: [T05-S001])
- **投入产出比**: **high**（选型必查；每次要选模型/换模型都应回来看最新排名）
- **Paywall**: none
- **Endorsement**: `[figure_long]` VB(reach-vb)主推 `[cross_source]` Slator/Northflank/Artificial Analysis 均引用其方法 (evidence: [T05-S002, T05-S021])
- **⚠️ 坑**: 榜单偏 HF 生态公开数据集 + 英语/欧语强，**中文覆盖弱**(无 AISHELL/WenetSpeech 主榜)；中文选型须配合 FunASR/FireRedASR 的 CER 榜(见 02-tools)。闭源商业 API 的真实生产表现未必被公平覆盖 (evidence: [T05-S001])
- **可信度**: high | **Decay risk**: low（行业基础设施）

### ★ 2. Artificial Analysis — Speech to Text

- **Type**: dataset/benchmark(第三方) | **URL**: https://artificialanalysis.ai/speech-to-text (S004)
- **Cadence**: rolling（速度为最近 7 日中位）| **Last activity**: 2026(活跃)
- **One-liner**: 独立第三方把 STT **准确率(AA-WER) × 速度(×realtime) × 价格($/1000min)** 放进一张可交互表——**唯一把"价格"做成一等公民**的活榜，对"成本尽量低"诉求是 Open ASR Leaderboard 的关键补充 (evidence: [T05-S004])
- **典型内容**: AA-WER 由 3 数据集合成(AA-AgentTalk 50% / VoxPopuli 25% / Earnings22 25%)；当前准确率 Fun-Realtime-ASR-preview 1.8% / ElevenLabs Scribe v2 2.2% 领先；速度 Parakeet-TDT-0.6B-v3(Together) 842x 最快；价格 Gemini 2.0 Flash Lite $0.19/1000min 最便宜 (evidence: [T05-S004])
- **投入产出比**: **high**（选型决策树里"成本×速度"那条直接用它）
- **Paywall**: none(核心可见) | **可信度**: high(第三方) | **Decay risk**: low
- **⚠️**: 厂商可能针对其数据集优化；与 Open ASR Leaderboard **数据集口径不同，两榜不可直接交叉比数** (evidence: [T05-S004, T05-S001])

### ★ 3. Deepgram changelog / AssemblyAI changelog（厂商版本流双子）

- **Type**: 官方 changelog | **URL**: https://developers.deepgram.com/changelog (S007) ; https://www.assemblyai.com/changelog (S008)
- **Cadence**: Deepgram 高频(2026 单月多条) / AssemblyAI 月级 | **Last activity**: 2026-05(均活跃) (evidence: [T05-S007, T05-S008])
- **One-liner**: 两家流式 ASR 第一梯队的**版本真相源**——新模型/新语言/新价格在这里最先落地，比任何二手报道快 (evidence: [T05-S007, T05-S008])
- **典型内容(2026)**: Deepgram 1 月发 **Flux**(对话式 ASR for voice agents) + Nova-3 多语 3 月 batch WER 降 34% + 5 月 Medical 升级；AssemblyAI 发 **Slam-1**(可提示 Speech LM) + Universal-3 Pro 实时 + Streaming 医疗模式 (evidence: [T05-S007, T05-S008])
- **投入产出比**: high(只要你用这两家或在比价就必订) | **Paywall**: none
- **🆕 新工具/figure 信号**: **Slam-1**(AssemblyAI 可提示 Speech LM)、**Deepgram Flux** 是 02-tools 未单列的新模型，喂给 wave 2 Track 02 (evidence: [T05-S008, T05-S007])
- **可信度**: high(一手) | **Decay risk**: low | **⚠️**: WER 宣称是 vendor 自测，跨家不可比，回 Open ASR/Artificial Analysis 校验

### ★ 4. FunASR repo（中文 ASR 主追踪源）

- **Type**: 官方 repo release | **URL**: https://github.com/modelscope/FunASR (S023)
- **Maintainer**: 阿里 DAMO Speech Lab | **Cadence**: 高频 | **Last activity**: **v1.3.3 (2026-05-24)** (evidence: [T05-S023])
- **One-liner**: 中文 ASR 生态的**事实集散地**——不仅是 Paraformer/SenseVoice 的家，2026 还在持续集成外部新模型(Fun-ASR-Nano vLLM 2-3x 加速、**Qwen3-ASR 0.6B/1.7B 52 语言**、**GLM-ASR-Nano 1.5B 方言**) (evidence: [T05-S023])
- **典型内容**: release notes + README + runtime SDK(WebSocket 流式/VAD/说话人/热词/OpenAI 兼容 API/MCP) (evidence: [T05-S023])
- **投入产出比**: high(中文场景必追) | **Paywall**: none | **可信度**: high(一手) | **Decay risk**: low
- **🆕 新工具信号**: **Qwen3-ASR / GLM-ASR-Nano**(2026 中文开源新秀，端侧友好)未在 02-tools 单列，喂给 wave 2 Track 02 (evidence: [T05-S023, T05-S024])

### ★ 5. Pete Warden's blog（端侧情报一手）

- **Type**: 工程博客(个人) | **URL**: https://petewarden.com/ (S019)
- **Host**: Pete Warden(Moonshine 作者，见 01-figures T01-S004) | **Cadence**: 不定 | **Last activity**: **2026-02-27**(Moonshine Note Taker) + 2026-02-13(Moonshine Voice) (evidence: [T05-S019])
- **One-liner**: 端侧/低延迟 ASR 最纯立场的一手发声——"本地跑、零网络、隐私、变长输入"，每发新东西都附**第一方 benchmark + 工程理由**(245M Moonshine WER 6.65% vs Whisper-large 7.44%) (evidence: [T05-S019])
- **投入产出比**: high(端侧选型/趋势必读) | **Paywall**: none | **可信度**: high(一手) | **Decay risk**: medium(个人博客，更新看心情)
- **替代品**: HF audio blog(S012) / Picovoice blog(S020)(端侧商业视角) / awnihannun.com(Apple Silicon/MLX 端侧)

### ★ 6. Northflank / Modal 自托管成本 benchmark（"成本尽量低"专项）

- **Type**: 工程博客(成本 benchmark) | **URL**: https://northflank.com/blog/best-open-source-speech-to-text-stt-model-in-2026-benchmarks (S021) ; https://modal.com/blog (S022)
- **Cadence**: 年度大稿/不定 | **Last activity**: 2026(Northflank 标题即 2026) (evidence: [T05-S021])
- **One-liner**: GPU serverless 厂商出的**开源 STT 自托管横评长稿**——WER×RTFx×license×单位成本一篇讲透，是"自托管 vs 云 API break-even"判断的最佳二手锚(他们有动机但数据扎实) (evidence: [T05-S021, T05-S022])
- **投入产出比**: high(决定自托管前必读) | **Paywall**: none | **可信度**: medium-high(厂商但工程严谨) | **Decay risk**: medium(年度稿，过期看下一版)
- **⚠️**: 厂商博客天然倾向"自托管划算"，需对照 Artificial Analysis 的云端 $/1000min 反向核对 (evidence: [T05-S021, T05-S004])

---

## Phase 2 提炼提示

**「这一行的资深人最该常追的 top 5」**（进 master skill 「Sources — 信息源」节 highlights）:
1. **Open ASR Leaderboard (S001)** — rolling，选型必查；**建议每次选/换模型时刷**；唯一缺中文 → 配 FunASR/FireRedASR CER 榜
2. **各家 pricing 页 + Deepgram/AssemblyAI changelog (02-tools T02-S020~S031 + S007/S008)** — **定价季度刷一次**，changelog 用到谁就订谁；价格/版本季度级变化
3. **Artificial Analysis STT (S004)** — rolling，"成本×速度"决策直接用(唯一把价格做成榜单一等公民)
4. **FunASR repo releases (S023)** — 中文场景必追；2026 仍高频上新(Qwen3-ASR/GLM-ASR)
5. **HF papers + arXiv eess.AS (S011/S013) + Pete Warden blog (S019)** — 前沿/端侧趋势；HF papers 是被社区过滤过的高信噪比入口

**「选型/成本真知识主要沉淀在哪」**（诚实定位）:
- **选型准确率真知识 → 第三方 benchmark(S001 Open ASR / S004 Artificial Analysis)**，不是厂商博客
- **成本/价格真知识 → 厂商 pricing 页(02-tools) + Artificial Analysis $/1000min(S004) + Northflank/Modal 自托管横评(S021/S022)**
- **版本/能力真知识 → 厂商 changelog(S007/S008) + 开源 repo releases(S015/S016/S017/S023)**
- **端侧/前沿真知识 → arXiv/HF papers(S011/S013) + Pete Warden(S019) + HF audio blog(S012)**

**「最近 3 个月被多源反复讨论的主题」**（候选信号；`topic-heat: high-confidence — 多 source × 多 item 已查证`）:
- **多语种 + code-switching 实时**(sources: Deepgram changelog Nova-3 多语 / AssemblyAI 多语 streaming / Open ASR 多语 track / Deepgram Flux) (evidence: [T05-S007, T05-S008, T05-S001])
- **端侧 Parakeet 化 / .cpp 移植浪潮**(sources: r/LocalLLaMA parakeet.cpp 讨论 / Artificial Analysis Parakeet 速度榜首 / 各端侧博客 Whisper-vs-Parakeet) (evidence: [T05-S027, T05-S004])
- **中文开源新秀爆发**: Qwen3-ASR(52 语言)、GLM-ASR-Nano(方言)、Fun-ASR(sources: FunASR releases / ModelScope) (evidence: [T05-S023, T05-S024])
- **可提示 / LLM-based ASR**(sources: AssemblyAI Slam-1 / cs.CL 论文流 / Seed-ASR 谱系) (evidence: [T05-S008, T05-S014])
- **benchmark 反刷分**(sources: HF "Benchmaxxer Repellant" blog) → 强化榜单可信度 (evidence: [T05-S012])

**新 figures 发现**（喂 wave 2 Track 01）:
- **Steveeeeeeen**(HF，Open ASR Leaderboard longform 赛道维护者) — 已隐含在 hf-audio，可作 VB 之外的榜单维护 figure 补充 (evidence: [T05-S001])

**新 tools 发现**（喂 wave 2 Track 02）:
- **AssemblyAI Slam-1**(可提示 Speech LM)、**Deepgram Flux**(对话式 ASR)、**Qwen3-ASR**(阿里，0.6B/1.7B/52 语言端侧)、**GLM-ASR-Nano**(智谱，1.5B 方言)、**sherpa-onnx**(k2-fsa 端侧部署运行时，02-tools 仅在 SenseVoice 卡内提及未单列)、**parakeet.cpp / Parakeet ONNX server**(Parakeet 端侧移植，社区新起) — 均为 02-tools 未单列或新出，建议补 (evidence: [T05-S008, T05-S007, T05-S023, T05-S017, T05-S027])

**冷僻 / 信号薄弱（诚实判断 → 进 Phase 2.8 诚实边界）**:
- **专门媒体层薄**：newsletter **0**(无 ASR 专属持续 newsletter)；podcast **0 专属**(ASR 散见于通用 AI 长访谈如 Latent Space/Krisp Voice AI，非本行业专属，未收)；conference **0 专属**(靠 Interspeech/ICASSP 通用会议)。→ **"newsletter/podcast/conference 三类对 ASR 是空或弱信号"，本 track 主力是 benchmark + 官方 changelog + arXiv/blog**。这与一般行业(资深人靠 newsletter/podcast)不同，须在 master skill 如实说明。
- **中文专门媒体层尤其薄**：中文 ASR 动态(Qwen3-ASR/GLM-ASR/讯飞星火/火山豆包)大量首发于**量子位/机器之心/知乎/公众号(全黑名单)**；本 track 仅能取 **FunASR repo / ModelScope / 火山·讯飞官方 first-party**。→ 中文用户追新动态时，一手只能盯 repo + ModelScope + vendor 文档，**没有合规的中文 ASR 专门 newsletter/podcast 可推**。
- **endorsement 类型偏 cross_source**(榜单/博客互引)，figure_long 背书少——符合 01-figures 判断(ASR figures 偏工程维护者，长访谈材料薄)。
- **数据厚度整体**：榜单/官方/论文/工程博客四类**信号充足且一手占比高**(29 源中 verified_primary ≈ 20 ≈ 69%)，非冷僻；唯独"人在聊的媒体层"薄——这是 ASR 作为快速迭代 infra 领域的固有特征，不是调研不足。
