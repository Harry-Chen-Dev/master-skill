# Track 04 — Canon：语音转文字 / ASR (Speech-to-Text) 应用工程

> Research date: 2026-06-04 · Locale: zh-CN（canon 全球）· Profile: practitioner（移动端 / 快速 / 低成本）
> 范围：**应用工程视角**的奠基论文 + 决定选型的基准/榜单 + 核心指标 + 端侧/量化 canon。不含模型训练科研深水区、TTS、声纹验证。

## Source Manifest

| source_id | url | bucket | last_checked | author/host | one-line note |
|-----------|-----|--------|--------------|-------------|---------------|
| T04-S001 | https://arxiv.org/abs/2212.04356 | verified_primary | 2026-06-04 | Radford et al (OpenAI) | Whisper 原论文 — 弱监督 680k 小时, 零样本鲁棒 |
| T04-S002 | https://arxiv.org/abs/2005.08100 | verified_primary | 2026-06-04 | Gulati et al (Google) | Conformer — CNN+Transformer, 流式 ASR 主力编码器 |
| T04-S003 | https://arxiv.org/abs/2006.11477 | verified_primary | 2026-06-04 | Baevski et al (Meta) | wav2vec 2.0 — 自监督, 低资源语音表征 |
| T04-S004 | https://www.cs.toronto.edu/~graves/icml_2006.pdf | verified_primary | 2026-06-04 | Graves et al | CTC 原论文 (ICML 2006) — 无对齐序列标注奠基 |
| T04-S005 | https://arxiv.org/abs/1211.3711 | verified_primary | 2026-06-04 | Alex Graves | RNN-Transducer (RNN-T) — 流式 ASR 主导架构奠基 |
| T04-S006 | https://arxiv.org/abs/1508.01211 | verified_primary | 2026-06-04 | Chan et al (Google) | Listen, Attend & Spell — attention seq2seq ASR 开山 |
| T04-S007 | https://arxiv.org/abs/2206.08317 | verified_primary | 2026-06-04 | Gao et al (Alibaba DAMO) | Paraformer — 非自回归(NAR), 10x 提速, 中文 |
| T04-S008 | https://arxiv.org/abs/2407.04051 | verified_primary | 2026-06-04 | An et al (Alibaba) | FunAudioLLM/SenseVoice — 多语+情感+事件, 低延迟 |
| T04-S009 | https://arxiv.org/abs/2410.15608 | verified_primary | 2026-06-04 | Jeffries et al (Useful Sensors) | Moonshine — 端侧/实时, 变长音频, 5x 省算力 |
| T04-S010 | https://arxiv.org/abs/2311.00430 | verified_primary | 2026-06-04 | Gandhi et al (HF) | Distil-Whisper — 知识蒸馏, 5.8x 快, <1% WER 差 |
| T04-S011 | https://huggingface.co/spaces/hf-audio/open_asr_leaderboard | verified_primary | 2026-06-04 | hf-audio (HuggingFace) | Open ASR Leaderboard — WER+RTFx 选型 ground truth |
| T04-S012 | https://arxiv.org/abs/2510.06961 | verified_primary | 2026-06-04 | Srivastav et al (HF/NVIDIA) | Open ASR Leaderboard 正式论文(2025), 三赛道方法论 |
| T04-S013 | https://www.danielpovey.com/files/2015_icassp_librispeech.pdf | secondary | 2026-06-04 | Panayotov/Povey | LibriSpeech 原论文 (host 非主域, 内容一手) |
| T04-S014 | https://arxiv.org/abs/1912.06670 | verified_primary | 2026-06-04 | Ardila et al (Mozilla) | Common Voice — 众包多语 CC0 语料/基准 |
| T04-S015 | https://arxiv.org/abs/1709.05522 | verified_primary | 2026-06-04 | Bu et al (AISHELL) | AISHELL-1 — 中文 ASR 标准基准 (CER) |
| T04-S016 | https://arxiv.org/abs/2205.12446 | verified_primary | 2026-06-04 | Conneau et al (Google) | FLEURS — 102 语种多语基准 (gpt-4o-transcribe 用它自评) |
| T04-S017 | https://en.wikipedia.org/wiki/Word_error_rate | secondary | 2026-06-04 | — | WER 定义 (S+D+I)/N, Levenshtein, CER 类比 |
| T04-S018 | https://github.com/ggml-org/whisper.cpp | verified_primary | 2026-06-04 | Georgi Gerganov | whisper.cpp — ggml/CoreML/Metal 端侧推理, int8 量化 |
| T04-S019 | https://github.com/SYSTRAN/faster-whisper | verified_primary | 2026-06-04 | SYSTRAN | faster-whisper — CTranslate2, 4x 快, int8, 工程默认 |
| T04-S020 | https://github.com/modelscope/FunASR | verified_primary | 2026-06-04 | ModelScope (Alibaba DAMO) | FunASR — 中文工业级, VAD+标点+热词+diarization 全链 |
| T04-S021 | https://github.com/snakers4/silero-vad | verified_primary | 2026-06-04 | Silero | Silero VAD — <1ms/chunk, 2MB, VAD 事实标准 |
| T04-S022 | https://github.com/pyannote/pyannote-audio | verified_primary | 2026-06-04 | pyannote (Hervé Bredin) | pyannote.audio — 开源 diarization 事实标准 |
| T04-S023 | https://github.com/kaldi-asr/kaldi | verified_primary | 2026-06-04 | Daniel Povey et al | Kaldi — 经典开源 ASR 工具链 (WFST/HMM) 传统 |
| T04-S024 | https://github.com/k2-fsa/icefall | verified_primary | 2026-06-04 | k2-fsa (Daniel Povey) | icefall/k2/lhotse — 次世代 Kaldi, RNN-T/zipformer + sherpa 端侧 |
| T04-S025 | https://huggingface.co/nvidia/parakeet-tdt-0.6b-v2 | verified_primary | 2026-06-04 | NVIDIA | Parakeet TDT 0.6B — 榜首速度王 RTFx 3386, WER 6.05% |
| T04-S026 | https://huggingface.co/nvidia/canary-1b | verified_primary | 2026-06-04 | NVIDIA | Canary-1B — FastConformer 多语 ASR+翻译, WER 6.67% |
| T04-S027 | https://arxiv.org/abs/2509.14128 | verified_primary | 2026-06-04 | NVIDIA NeMo | Canary-1B-v2 / Parakeet-v3 技术报告 (多语高效) |
| T04-S028 | https://openai.com/index/introducing-our-next-generation-audio-models/ | verified_primary | 2026-06-04 | OpenAI | gpt-4o-transcribe 官方 — 自报 ~35% 低于 Whisper WER (403, 经检索佐证) |
| T04-S029 | https://deepgram.com/learn/speech-to-text-benchmarks | secondary | 2026-06-04 | Deepgram | 厂商自报基准 (Nova-3 内部 WER ~5.26%) — 一面之词 |
| T04-S030 | https://artificialanalysis.ai/speech-to-text | secondary | 2026-06-04 | Artificial Analysis | 第三方 STT 榜 — Nova-3 实测 ~18.3% (矛盾源) |

> 黑名单核查：30 源全部跑过 `source_verifier.py classify`，无 `blacklisted`（知乎/公众号/百度百科/CSDN/内容农场均未收录）。`isca-archive.org` / `danielpovey.com` 被 verifier 判 `secondary`（unknown host），但内容是一手论文，故 LibriSpeech 用 danielpovey.com 镜像并标 secondary。OpenAI 官方 blog WebFetch 返回 403，但其自报 WER 口径经 WebSearch 多源佐证保留。

---

## 总览（按类型分组）

### Seminal Papers — 架构奠基（必读 7 / 扩展若干）

| 论文 | 年 | 核心 idea | 对"应用工程"的意义 | Endorsement |
|------|----|-----------|---------------------|-------------|
| CTC (Graves) | 2006 | 无对齐序列标注 + blank token | 端到端 ASR 的起点；流式 CTC 解码极快 → 速度派 | ✅✅✅ |
| RNN-T (Graves) | 2012 | 序列转导 = encoder+prediction+joint | **流式/端侧 ASR 主导架构**（Google/Apple 听写） | ✅✅✅ |
| LAS | 2015 | listener(enc)+speller(attn-dec) | attention seq2seq ASR 开山 → Whisper 谱系祖先 | ✅✅✅ |
| Conformer | 2020 | CNN(局部)+self-attn(全局) | 现代 ASR **主力编码器**；NVIDIA/icefall 均用 | ✅✅✅ |
| wav2vec 2.0 | 2020 | 自监督 + 对比学习 | 低资源/小语种可行性；预训练表征范式 | ✅✅✅ |
| Whisper | 2022 | 弱监督 680k 小时 enc-dec | **应用层默认通用模型**（非流式、鲁棒、多语） | ✅✅✅ |
| Paraformer | 2022 | 非自回归(NAR) 单步并行 | 中文工业 ASR 主力；比 AR 快 >10x → 成本派 | ✅✅✅ |

### Benchmarks / Leaderboards — 选型 ground truth（必读 6）

| 基准 | 年 | 语言/范围 | 指标 | 决策意义 | Endorsement |
|------|----|-----------|------|----------|-------------|
| **Open ASR Leaderboard** | 2023→2025 | 英/多语/长音频三赛道 | **WER + RTFx** | 选型唯一活的横评（86 模型/12 数据集） | ✅✅✅ |
| LibriSpeech | 2015 | 英文有声书 ~1000h | WER (test-clean/other) | 学术 WER 第一锚点（已接近饱和） | ✅✅✅ |
| Common Voice | 2019 | 众包多语 CC0 | WER/CER | 真实噪声 + 小语种训练/评测 | ✅✅✅ |
| AISHELL-1 | 2017 | 中文普通话 ~170h | **CER** | **中文 ASR 标准锚点** | ✅✅✅ |
| FLEURS | 2022 | 102 语种 | WER/CER | 多语横评；gpt-4o-transcribe 自评用它 | ✅✅✅ |
| 厂商自报 vs 第三方 | 2025-26 | 云 API | WER | 选型陷阱：口径差 3x（见矛盾节） | ✅✅⚠️ |

### Engineering Canon — 端侧/工具链事实勘误（README 作 ground truth）

| 项目 | 维护者 | 角色 | 对"移动端/低成本"的意义 | Endorsement |
|------|--------|------|------------------------|-------------|
| whisper.cpp | G. Gerganov | ggml C/C++ 端侧推理 | iOS/Android/树莓派离线 + int8/4bit 量化 | ✅✅✅ |
| faster-whisper | SYSTRAN | CTranslate2 推理 | 同精度 4x 快 + int8，**自托管工程默认** | ✅✅✅ |
| Distil-Whisper | HuggingFace | 蒸馏小模型 | 5.8x 快 / 少 51% 参数，端侧友好 | ✅✅✅ |
| Moonshine | Useful Sensors | 端侧专用模型 | 变长音频，5x 省算力，**voice command/实时** | ✅✅✅ |
| FunASR | Alibaba DAMO | 中文全链路工具箱 | VAD+标点+ITN+热词+diarization 一站式 | ✅✅✅ |
| Silero VAD | Silero | 轻量 VAD | 裁静音省算力/成本 + endpointing，2MB | ✅✅✅ |
| pyannote.audio | H. Bredin | diarization | 开源"谁在何时说"事实标准 | ✅✅✅ |
| Kaldi | D. Povey | 经典 ASR 框架 | WFST/HMM 传统；老系统仍在跑 | ✅✅✅ |
| k2/icefall/sherpa | D. Povey (k2-fsa) | 次世代 Kaldi | RNN-T/zipformer + sherpa-onnx 端侧部署 | ✅✅✅ |

### Core Concepts（25 个，见下方详表）

| 概念 | 一句话 | 来源 |
|------|--------|------|
| WER | (S+D+I)/N 词错率 | T04-S017 |
| CER | 字错率（中文/无词界语言） | T04-S015,S017 |
| RTF / RTFx | 实时率 / 实时倍数（速度口径） | T04-S011,S012 |
| 流式 vs 非流式 | 边说边出 vs 整段后出 | T04-S005,S001 |
| Endpointing | 判断"说完了"的断句 | T04-S021 |
| VAD | 语音活动检测/裁静音 | T04-S021 |
| Diarization | 说话人分离 | T04-S022 |
| ITN | 逆文本规整（"一百二"→120） | T04-S020 |
| 标点恢复 | 无标点流→带标点文本 | T04-S020 |
| CTC | 无对齐序列标注 + blank | T04-S004 |
| RNN-T | 流式转导架构 | T04-S005 |
| Conformer | CNN+attention 编码器 | T04-S002 |
| TDT | token+duration 转导器（更快） | T04-S025 |
| Attention seq2seq | enc-dec + 注意力（Whisper 谱系） | T04-S006,S001 |
| NAR（非自回归） | 并行出 token，省时 | T04-S007 |
| 自监督预训练 | 无标注音频学表征 | T04-S003 |
| 弱监督 | 大规模带噪转录监督 | T04-S001 |
| 知识蒸馏 | 大模型教小模型 | T04-S010 |
| 量化 int8/ggml/gguf | 降精度省内存/提速 | T04-S018,S019 |
| 端侧/on-device | 模型跑在手机/边缘 | T04-S018,S009 |
| Beam search | 解码搜索宽度 | T04-S006 |
| 热词 biasing | 偏置专有名词识别 | T04-S020 |
| 幻觉(hallucination) | 模型编造不存在的话 | T04-S010 |
| 时间戳 | 词/段级 start-end | T04-S025 |
| 自托管 break-even | 量本盈亏平衡点 | T04-S019,S018 |

---

## Seminal Papers 详卡

### 📄 1. Connectionist Temporal Classification (CTC)
- **Authors / Venue**: A. Graves, S. Fernández, F. Gomez, J. Schmidhuber · ICML 2006
- **URL**: https://www.cs.toronto.edu/~graves/icml_2006.pdf
- **One-liner**: 不需要逐帧对齐就能训练序列→序列，引入 **blank token** 折叠重复帧。
- **核心 idea**: 输出层每帧给字符分布（含 blank），用前向-后向算法对所有合法对齐求和；解码时去 blank、合并重复 → 文本。(evidence: [T04-S004]) [一手]
- **为什么经典 / 对应用工程的意义**: 端到端 ASR 的真正起点；**CTC 解码无自回归、极快**，是"速度派/流式"的根。许多端侧/工业模型仍用 CTC 头。(evidence: [T04-S004, T04-S012]) [一手+推断]
- **如何读**: 读 §2-3（CTC 定义 + 前向后向）即可，实验可略。
- **后续 / 扩展**: RNN-T (S005) 直接在 CTC 之上加 prediction network 解决条件独立假设。
- **可信度 high / Decay low**。

### 📄 2. Sequence Transduction with RNNs (RNN-Transducer / RNN-T)
- **Authors / Venue**: A. Graves · ICML 2012 Workshop
- **URL**: https://arxiv.org/abs/1211.3711
- **One-liner**: 在 CTC 基础上加 **prediction network + joint network**，去掉输出 token 间的条件独立假设。
- **核心 idea**: encoder（声学）+ prediction（语言，类似 RNN-LM）+ joint 融合 → 可流式逐帧增量解码。(evidence: [T04-S005]) [一手]
- **为什么经典 / 对应用工程的意义**: **设备端流式 ASR 的主导架构**（Google/Apple 手机听写、低延迟实时字幕的事实标准），因为天然支持 online、增量、低延迟。论文本身只在 TIMIT 上做了音素实验，"主导地位"是后续工业采纳形成的。(evidence: [T04-S005, T04-S012]) [一手claim弱 + 行业推断]
- **如何读**: 抓住"三网络"结构图即可，不必啃推导。
- **后续 / 扩展**: TDT (token-and-duration transducer，S025/S027) 是 RNN-T 的提速变体，预测 token + 时长跳步。
- **可信度 high / Decay low**。

### 📄 3. Listen, Attend and Spell (LAS)
- **Authors / Venue**: W. Chan, N. Jaitly, Q. Le, O. Vinyals · 2015 (arXiv) / ICASSP 2016
- **URL**: https://arxiv.org/abs/1508.01211
- **One-liner**: 第一个有竞争力的 **attention 编码器-解码器** ASR：listener(金字塔 RNN 编码) + speller(注意力解码出字符)。
- **核心 idea**: 端到端联合学习，无 HMM、无独立性假设；Google Voice Search 14.1% WER（无 LM）。(evidence: [T04-S006]) [一手]
- **为什么经典 / 对应用工程的意义**: 确立 attention-seq2seq 为 ASR 可行路线 → **Whisper（enc-dec Transformer）正是这一谱系的工业放大版**。理解 LAS = 理解 Whisper 为什么非流式、为什么会"幻觉"。(evidence: [T04-S006, T04-S001]) [一手+推断]
- **后续**: Conformer(S002) 把 encoder 升级；Whisper(S001) 把它 scale 到 680k 小时。
- **可信度 high / Decay low**。

### 📄 4. Conformer: Convolution-augmented Transformer
- **Authors / Venue**: A. Gulati et al (Google) · INTERSPEECH 2020
- **URL**: https://arxiv.org/abs/2005.08100
- **One-liner**: Transformer 抓全局 + CNN 抓局部，合成 ASR 的**主力编码器**。
- **核心 idea**: Conformer block = FFN + 多头自注意 + 卷积模块 + FFN（macaron）。LibriSpeech **2.1%/4.3%（无 LM）、1.9%/3.9%（有 LM）**。(evidence: [T04-S002]) [一手]
- **为什么经典 / 对应用工程的意义**: 几乎所有现代高准确率 ASR（NVIDIA FastConformer/Parakeet/Canary、icefall zipformer、各家流式系统）都以 Conformer 或其变体为 encoder。**选型时"Conformer 系"≈ 准确率天花板**。Open ASR 论文实证：Conformer-encoder + Transformer-decoder 取得最佳平均 WER。(evidence: [T04-S002, T04-S012, T04-S025]) [一手×2]
- **如何读**: 看 §2 block 结构图 + LibriSpeech 表。
- **可信度 high / Decay low**。

### 📄 5. wav2vec 2.0
- **Authors / Venue**: A. Baevski, H. Zhou, A. Mohamed, M. Auli (Meta) · NeurIPS 2020
- **URL**: https://arxiv.org/abs/2006.11477
- **One-liner**: 自监督——先在海量**无标注**音频上学表征，再用极少标注微调。
- **核心 idea**: 在 latent 空间 mask + 对比任务 + 量化表征。**10 分钟标注**即得 4.8/8.2 WER（配 53k 小时无标注预训练）。(evidence: [T04-S003]) [一手]
- **为什么经典 / 对应用工程的意义**: 解锁**低资源/小语种 ASR**——没有几千小时标注也能做。是 Whisper 之外另一条范式（自监督 vs 弱监督），也是很多非英语开源模型的底座。(evidence: [T04-S003]) [一手]
- **后续**: HuBERT、Common Voice(S014) 提供了配套小语种语料。
- **可信度 high / Decay low**。

### 📄 6. Whisper — Robust Speech Recognition via Large-Scale Weak Supervision
- **Authors / Venue**: A. Radford, J.W. Kim, et al (OpenAI) · 2022
- **URL**: https://arxiv.org/abs/2212.04356
- **One-liner**: **应用层最常被默认调用的通用 ASR**——680k 小时弱监督训练的 enc-dec Transformer，零样本、多语、抗噪。
- **核心 idea**: 不追单基准 SOTA，追"开箱即用的鲁棒性"；多任务格式（转写/翻译/语种 ID/时间戳）。摘要未给具体 WER，强调接近人类鲁棒性。(evidence: [T04-S001]) [一手]
- **为什么经典 / 对应用工程的意义**: 定义了"开源默认基线"。**关键工程取舍**：(a) **非流式**（30s 窗口、enc-dec），不适合低延迟实时；(b) 长音频易**幻觉**；(c) 衍生整条端侧生态（whisper.cpp / faster-whisper / distil-whisper）。移动端/低成本场景几乎都从 Whisper 变体起步。(evidence: [T04-S001, T04-S018, T04-S010]) [一手+推断]
- **如何读**: 读 §2(方法) + §3.8(鲁棒性/long-form) + Fig 长尾语言图。
- **后续**: large-v3、distil-whisper(S010)、gpt-4o-transcribe(S028)。
- **可信度 high / Decay low**（架构稳定，但已被自家 gpt-4o-transcribe 在云端 supersede 一部分场景）。

### 📄 7. Paraformer — Fast and Accurate Parallel Transformer (NAR)
- **Authors / Venue**: Z. Gao, S. Zhang, et al (Alibaba DAMO) · INTERSPEECH 2022
- **URL**: https://arxiv.org/abs/2206.08317
- **One-liner**: **非自回归(NAR)** ASR——一步并行出所有 token，比自回归(Whisper 式)快 **>10x**。
- **核心 idea**: continuous integrate-and-fire 预测 token 数 + glancing LM sampler 补 token 间依赖 + MWER 训练，解决 NAR 的独立性假设缺陷。AISHELL 上达 AR-SOTA 同档准确率。(evidence: [T04-S007]) [一手]
- **为什么经典 / 对应用工程的意义**: **中文 ASR 工业主力**（FunASR 默认引擎），是"成本/速度派"的代表——同精度下吞吐远超 Whisper。移动端/批量转写场景的关键备选。(evidence: [T04-S007, T04-S020]) [一手+推断]
- **后续**: SenseVoice(S008) 在 FunAudioLLM 框架下进一步多任务化。
- **可信度 high / Decay low**。

### 📄 8（扩展）. SenseVoice / FunAudioLLM
- **URL**: https://arxiv.org/abs/2407.04051 · Alibaba · 2024（标注 work-in-progress）
- **One-liner**: SenseVoice-Small **低延迟**多语 ASR（5 语）+ Large 高精度（50+ 语），附情感识别/音频事件。(evidence: [T04-S008]) [一手]
- **应用意义**: 中文端侧/快速场景的新选项；摘要未给 RTF/WER 具体数（一手数据偏弱）。归入"中文 + 端侧"备选。

### 📄 9（扩展）. Moonshine
- **URL**: https://arxiv.org/abs/2410.15608 · Useful Sensors (Pete Warden 等) · 2024
- **One-liner**: 端侧专用 enc-dec（RoPE 位置编码），**按音频实际长度处理（不 zero-pad）**，10s 片段比 Whisper-tiny 省 **5x 算力且 WER 不升**。(evidence: [T04-S009]) [一手]
- **应用意义**: 直击本 skill 核心场景——**移动端、实时、voice command、低算力**。

### 📄 10. Distil-Whisper
- **URL**: https://arxiv.org/abs/2311.00430 · Gandhi et al (HuggingFace) · 2023
- **One-liner**: 大规模伪标注 + WER 启发式筛选做**知识蒸馏**：**5.8x 快、少 51% 参数、OOD <1% WER 差**，且更少幻觉。可与 Whisper 做投机解码再 2x 提速。(evidence: [T04-S010]) [一手]
- **应用意义**: "想要 Whisper 质量但要更快更小"的标准答案；端侧/低成本必备。

---

## Benchmarks / Leaderboards 详卡

### 🏆 Open ASR Leaderboard（最权威的活的选型 ground truth）
- **Host / 论文**: hf-audio (HuggingFace) · 正式论文 Srivastav et al, arXiv 2510.06961 (2025)
- **URL**: https://huggingface.co/spaces/hf-audio/open_asr_leaderboard · https://arxiv.org/abs/2510.06961
- **是什么**: 在多个公开数据集上统一横评 ASR 的**准确率(Average WER)与速度(RTFx)**。截至 2025-11 覆盖 **86 个开源+闭源系统、18 机构、11-12 数据集**，分**英文短/英文长/多语**三赛道。(evidence: [T04-S011, T04-S012]) [一手]
- **关键发现（直接指导选型）**:
  - **Conformer-encoder + Transformer-decoder 取得最佳平均 WER**；**CTC / TDT 解码器 RTFx 更高**（更适合长音频/批量）。→ 经典的**准确率 vs 速度二分**。(evidence: [T04-S012]) [一手]
  - 实测数据点：**Parakeet-TDT-0.6B** WER **6.05%** / RTFx **3386**（batch128，≈1 小时音频 ~1 秒转完）；**Canary-1B** WER **6.67%**（多语+翻译）。(evidence: [T04-S025, T04-S026]) [一手]
- **如何用**: 选型第一站——按 WER 和 RTFx 两轴 + 你的语言赛道筛候选，再用自己数据复测。
- **可信度 high / Decay medium**（榜单滚动更新，模型每月变）。**Last_updated: 2025-11**。

### 📊 LibriSpeech
- **URL**: https://www.danielpovey.com/files/2015_icassp_librispeech.pdf · Panayotov, Chen, Povey, Khudanpur · ICASSP 2015
- **是什么**: ~1000 小时英文有声书朗读（LibriVox/Gutenberg），分 **test-clean（干净）/ test-other（更难）**。
- **应用意义**: **英文 WER 的第一历史锚点**，几乎每篇论文都报。注意：已**接近饱和**（顶模型 test-clean <2%），不能区分"真实噪声场景"的好坏——别只看 LibriSpeech 选型。(evidence: [T04-S013, T04-S002, T04-S025]) [一手] · 可信度 high / Decay low。

### 📊 Common Voice
- **URL**: https://arxiv.org/abs/1912.06670 · Ardila et al (Mozilla) · 2019
- **是什么**: 众包、多语、CC0 朗读语料（首发 2500h/29 语，持续增长），既是训练集也是基准。
- **应用意义**: 比 LibriSpeech **更接近真实口音/设备噪声**，且覆盖小语种；gpt-4o-transcribe 等用它自评。(evidence: [T04-S014, T04-S028]) [一手] · 可信度 high / Decay low（语料持续增长）。

### 📊 AISHELL-1（中文必读锚点）
- **URL**: https://arxiv.org/abs/1709.05522 · Bu, Du, Na, Wu, Zheng · 2017
- **是什么**: ~170 小时开源普通话语料 + Kaldi recipe。**中文 ASR 评测用 CER（字错率）而非 WER**（中文无明确词界）。
- **应用意义**: **中文选型的标准基准**；做中文/方言场景必看 AISHELL（及 AISHELL-2/4）上的 CER。(evidence: [T04-S015, T04-S017]) [一手] · 可信度 high / Decay low。

### 📊 FLEURS
- **URL**: https://arxiv.org/abs/2205.12446 · Conneau et al (Google) · 2022
- **是什么**: 102 语种 n-way 平行语音（基于 FLoRes-101），每语 ~12h。
- **应用意义**: **多语/小语种横评标准**；OpenAI 用 FLEURS 宣称 gpt-4o-transcribe 多语 WER 优于 Whisper。(evidence: [T04-S016, T04-S028]) [一手] · 可信度 high / Decay low。

---

## ⚠️ 矛盾保留：自报 WER vs 第三方 WER（选型最大陷阱）

ASR canon 里**最该警惕的事实分歧**——厂商自报 vs 独立横评口径差到 ~3x：

| 主张 | 数值 | 来源 | 类型 |
|------|------|------|------|
| Deepgram Nova-3（自报，干净英文） | WER **~5.26%**；"比 Whisper 低 36%" | Deepgram 内部 | 二手/厂商一面之词 (S029) |
| Deepgram Nova-3（第三方实测） | WER **~18.3%** | Artificial Analysis | 第三方 (S030) |
| gpt-4o-transcribe（自报） | Common Voice/FLEURS **~35% 低于 Whisper** WER | OpenAI 官方 | 厂商一面之词 (S028) |
| Whisper large-v3（第三方，LibriSpeech-clean） | WER **~2.8%** | 第三方汇总 | 二手 (S029/S030) |
| AssemblyAI Universal-2（第三方，LibriSpeech-clean） | WER **~2.1%** | 第三方 | 二手 (S029/S030) |

**裁决**:（1）**永远不要直接信厂商自报 WER 做选型**——它通常在自家干净数据上测；(evidence: [T04-S029, T04-S030]) (2) **数据集 = 一切**：LibriSpeech-clean（~2-3%）和真实噪声（~15-18%）差一个数量级；(3) 唯一可信路径 = **Open ASR Leaderboard 统一口径 + 拿你自己的音频复测**。(evidence: [T04-S011, T04-S012, T04-S030]) [推断，跨源一致]

---

## Core Concepts 详卡（25 个，Tier 标注）

### 💡 1. WER (Word Error Rate) — `tier-1`
- 定义：**WER = (S + D + I) / N**（替换+删除+插入 / 参考词数），源自 Levenshtein 编辑距离。0=完美，可 >1。
- 来源：[primary] 语音识别社区通用，定义见 T04-S017。
- 常见误用：跨数据集比 WER 无意义（口径不同）；中文用 WER 而非 CER 是错的。(evidence: [T04-S017]) [一手]

### 💡 2. CER (Character Error Rate) — `tier-1`
- 字符级错误率，**中文/日文等无词界语言的标准指标**（AISHELL 用 CER）。
- 来源：[primary] T04-S015。常见误用：拿中文 CER 和英文 WER 直接比大小。(evidence: [T04-S015, T04-S017]) [一手]

### 💡 3. RTF / RTFx (Real-Time Factor) — `tier-1`
- **RTF = 处理时长 / 音频时长**（越小越快，<1 才能实时）；**RTFx = 1/RTF = 实时倍数**（榜单用，越大越快，Parakeet 达 3386x）。
- 来源：[primary] Open ASR Leaderboard 标准指标 T04-S011/S012。(evidence: [T04-S011, T04-S025]) [一手]

### 💡 4. 流式 vs 非流式 (streaming vs offline) — `tier-1`
- **流式**：边说边出字（低延迟，RNN-T/CTC），实时字幕/语音输入；**非流式**：整段音频后出（Whisper enc-dec，准确率高但有延迟）。
- 来源：[primary] T04-S005(流式)、T04-S001(非流式)。这是**选型第一分叉**。(evidence: [T04-S005, T04-S001]) [一手+推断]

### 💡 5. Endpointing（断点检测/收尾判定）— `tier-1`
- 判断用户"说完了"的时机，决定何时结束一次识别（影响交互延迟与体验）。常与 VAD 联用。
- 来源：[primary] 工程概念，VAD 工具支撑 T04-S021。(evidence: [T04-S021]) [推断]

### 💡 6. VAD (Voice Activity Detection) — `tier-1`
- 检测哪段有人声 → **裁掉静音**：省算力/省云端按时长计费的成本、做分块与 endpointing。Silero VAD（<1ms/chunk, 2MB）是事实标准。
- 来源：[primary] T04-S021。**低成本 playbook 核心一招**。(evidence: [T04-S021, T04-S019]) [一手]

### 💡 7. Diarization（说话人分离）— `tier-1`
- "谁在何时说"——把转写按说话人切分。pyannote.audio 是开源事实标准，常与 Whisper 拼成带说话人转写（whisperX）。
- 来源：[primary] T04-S022。(evidence: [T04-S022]) [一手]

### 💡 8. ITN（逆文本规整 Inverse Text Normalization）— `tier-1`
- 把口语规整成书面：「一百二十三」→「123」、「百分之五」→「5%」、日期/货币格式化。
- 来源：[primary] FunASR 内置 T04-S020。常见误用：把 ITN 和"标点恢复"混为一谈（两件事）。(evidence: [T04-S020]) [一手]

### 💡 9. 标点恢复 (Punctuation Restoration) — `tier-2`
- ASR 原始输出常无标点 → 后处理模型补逗号句号（FunASR 用 CT-Transformer）。
- 来源：[primary] T04-S020。(evidence: [T04-S020]) [一手]

### 💡 10. CTC — `tier-1`
- 见论文卡 1。无对齐序列标注 + blank token；解码极快，速度派根基。
- 来源：[primary] Graves 2006, T04-S004。(evidence: [T04-S004]) [一手]

### 💡 11. RNN-T (Transducer) — `tier-1`
- 见论文卡 2。**流式 ASR 主导架构**；encoder+prediction+joint。
- 来源：[primary] Graves 2012, T04-S005。(evidence: [T04-S005]) [一手]

### 💡 12. Conformer — `tier-1`
- 见论文卡 4。CNN+attention 编码器，准确率天花板。
- 来源：[primary] Gulati 2020, T04-S002。(evidence: [T04-S002, T04-S012]) [一手]

### 💡 13. TDT (Token-and-Duration Transducer) — `tier-2`
- RNN-T 提速变体：同时预测 token 和其时长，跳过冗余帧 → 极高 RTFx（Parakeet-TDT 用它）。
- 来源：[primary] NVIDIA, T04-S025/S027。(evidence: [T04-S025]) [一手]

### 💡 14. Attention seq2seq (enc-dec) — `tier-1`
- LAS→Whisper 谱系；注意力对齐声学与文本。准确率高但通常非流式、长音频易幻觉。
- 来源：[primary] LAS T04-S006, Whisper T04-S001。(evidence: [T04-S006, T04-S001]) [一手]

### 💡 15. 非自回归 NAR — `tier-2`
- 并行出 token（Paraformer），不逐字生成 → >10x 提速，成本派代表。
- 来源：[primary] T04-S007。常见误用：以为 NAR 一定不如 AR 准（Paraformer 反驳了）。(evidence: [T04-S007]) [一手]

### 💡 16. 自监督预训练 — `tier-2`
- 无标注音频学表征（wav2vec2/HuBERT），解锁低资源语言。
- 来源：[primary] T04-S003。(evidence: [T04-S003]) [一手]

### 💡 17. 弱监督 (weak supervision) — `tier-2`
- 用海量带噪互联网转录做监督（Whisper），换鲁棒性与零样本。
- 来源：[primary] T04-S001。区别于自监督（无标注）。(evidence: [T04-S001]) [一手]

### 💡 18. 知识蒸馏 — `tier-2`
- 大模型(teacher)教小模型(student)，distil-whisper 5.8x 快 / <1% WER 差。端侧/低成本核心。
- 来源：[primary] T04-S010。(evidence: [T04-S010]) [一手]

### 💡 19. 量化 int8 / ggml / gguf — `tier-1`
- 把权重从 fp16/32 降到 int8/4bit，省内存提速，端侧关键（whisper.cpp 用 ggml/gguf；faster-whisper int8）。
- 来源：[primary] T04-S018, T04-S019。**移动端落地必备**。(evidence: [T04-S018, T04-S019]) [一手]

### 💡 20. 端侧 / on-device — `tier-1`
- 模型跑在手机/边缘（whisper.cpp + CoreML/Metal、Moonshine、sherpa-onnx）：离线、隐私、零云成本。
- 来源：[primary] T04-S018, T04-S009, T04-S024。**本 skill 核心场景**。(evidence: [T04-S018, T04-S009]) [一手]

### 💡 21. Beam search — `tier-2`
- 解码时保留 top-k 候选路径搜最优转写；beam 越宽越准但越慢（速度↔准确率旋钮）。
- 来源：[primary] seq2seq/ASR 通用，LAS T04-S006。(evidence: [T04-S006]) [一手+推断]

### 💡 22. 热词 / biasing (contextual biasing) — `tier-1`
- 给定专有名词/术语表，偏置解码使其更易被正确识别（人名、品牌、行话）。FunASR 支持 hotword。
- 来源：[primary] T04-S020。**生产化关键**（默认模型识别专名差）。(evidence: [T04-S020]) [一手]

### 💡 23. 幻觉 hallucination — `tier-1`
- ASR（尤其 Whisper 类 enc-dec 在长音频/静音段）**编造不存在的话**；distil-whisper 声称更少幻觉。
- 来源：[primary] T04-S010, T04-S001。常见误用：把幻觉当"识别错"——它是无中生有，需 VAD/分段缓解。(evidence: [T04-S010, T04-S001]) [一手]

### 💡 24. 时间戳 (timestamps) — `tier-2`
- 词级/段级 start-end 时间，用于字幕对齐、检索、diarization 拼接。Parakeet/Whisper 都支持。
- 来源：[primary] T04-S025, T04-S001。(evidence: [T04-S025]) [一手]

### 💡 25. 自托管 break-even（量本盈亏平衡）— `tier-2`
- 决策：当转写量超过某阈值，自托管开源(faster-whisper/whisper.cpp)的边际成本低于云 API 按分钟计费 → 该自建。
- 来源：[primary] 工程概念，工具支撑 T04-S019/S018。**低成本 playbook 决策点**。(evidence: [T04-S019, T04-S018]) [推断]

---

## Phase 2 提炼提示

### 反复出现 ≥ 3 个 canon 都讨论的核心 idea（候选心智模型）
- **准确率 × 速度(RTF) × 成本 三角，没有免费午餐**：出现于 Open ASR 论文(S012, Conformer 准但慢 / CTC-TDT 快)、Paraformer(S007, NAR 换速度)、distil-whisper(S010, 蒸馏换速度/体积)、Moonshine(S009) → **核心心智模型**。(evidence: [T04-S012, T04-S007, T04-S010])
- **流式(RNN-T/CTC) vs 非流式(Whisper enc-dec) 是第一性分叉**：RNN-T(S005)、LAS/Whisper(S006/S001)、Open ASR 三赛道(S012) → 心智模型「先问要不要实时」。(evidence: [T04-S005, T04-S001, T04-S012])
- **不要信自报 WER，要用统一榜单 + 自有数据复测**：自报vs第三方(S028/S029/S030) + Open ASR 统一口径(S011/S012) + LibriSpeech 饱和警告(S013) → playbook。(evidence: [T04-S030, T04-S012])
- **端侧 = 量化 + 蒸馏 + VAD 裁静音 的组合拳**：whisper.cpp(S018)、distil-whisper(S010)、Silero VAD(S021)、Moonshine(S009) → 低成本/移动端 playbook。(evidence: [T04-S018, T04-S010, T04-S021])

### 智识谱系种子
- **流派 A：流式/转导派（速度·端侧·实时）** — 奠基 CTC(Graves 2006, S004) → RNN-T(Graves 2012, S005) → 工业 TDT/zipformer(NVIDIA/k2, S025/S024)。代表工具 icefall/sherpa(S024)、Parakeet(S025)。关联 Track 01 figure：**Alex Graves**(奠基)、**Daniel Povey**(Kaldi/k2 工程传统, S023/S024)。
- **流派 B：attention seq2seq 通用大模型派（准确率·鲁棒·多语·非流式）** — 奠基 LAS(Chan 2015, S006) → Conformer encoder(Gulati 2020, S002) → **Whisper**(Radford 2022, S001) → gpt-4o-transcribe(S028)。关联 figure：**Alec Radford**(Whisper)、Google Brain 语音组。
- **流派 C：自监督表征派（低资源/小语种）** — wav2vec 2.0(Baevski 2020, S003)/HuBERT。关联 figure：**Alexei Baevski / Michael Auli (Meta)**。
- **流派 D：中文/工业 NAR 派（成本·中文·全链路）** — Paraformer(Gao 2022, S007) → SenseVoice/FunAudioLLM(S008) → FunASR 生态(S020)。关联 figure：**Zhifu Gao / Shiliang Zhang (Alibaba DAMO)**。
- **主要分歧 (still-debated)**：(1) 云 API vs 端侧自托管；(2) 通用大模型(Whisper) vs 专用流式(RNN-T/Conformer)；(3) 自报 WER 口径战争；(4) 英文优先 vs 中文 ASR 谁是基准。

### 核心概念 → 候选 playbook
- 遇到「要实时/低延迟」→ 选流式 RNN-T/CTC（Parakeet/sherpa/Deepgram），**不要**用 Whisper enc-dec。(evidence: [T04-S005, T04-S025])
- 遇到「移动端/离线/隐私/零云成本」→ whisper.cpp(CoreML/Metal) 或 Moonshine 或 sherpa-onnx + int8 量化 + Silero VAD。(evidence: [T04-S018, T04-S009, T04-S021])
- 遇到「中文/方言/要标点+ITN+热词」→ FunASR(Paraformer/SenseVoice) 全链路，看 AISHELL CER 而非 WER。(evidence: [T04-S020, T04-S015])
- 遇到「成本爆炸」→ 先上 VAD 裁静音，再考虑量化/蒸馏，量大则算自托管 break-even。(evidence: [T04-S021, T04-S010, T04-S019])
- 遇到「厂商报超低 WER」→ 不信，去 Open ASR Leaderboard 对统一口径 + 用自有噪声样本复测。(evidence: [T04-S012, T04-S030])
- 遇到「长音频 Whisper 出现莫名其妙的句子」→ 那是幻觉，加 VAD 分段 / 换 distil-whisper。(evidence: [T04-S010, T04-S001])

### 与其他 Track 的 seed
- **→ Track 01 figures**：Alex Graves、Daniel Povey、Alec Radford、Alexei Baevski/Michael Auli、Zhifu Gao/Shiliang Zhang、Georgi Gerganov(whisper.cpp)、Sanchit Gandhi(HF, distil/leaderboard)、Hervé Bredin(pyannote)、Pete Warden(Moonshine)。
- **→ Track 02 tools**：whisper.cpp / faster-whisper / FunASR / Silero VAD / pyannote / icefall+sherpa-onnx / NeMo(Parakeet,Canary) / Deepgram / AssemblyAI / gpt-4o-transcribe API。
- **→ Track 03 workflows**：VAD 裁静音→分块→ASR→标点/ITN→diarization→时间戳 这条后处理流水线（FunASR 体现）。

### 冷僻 / 信号薄弱自检
- 必读 paper **10**（≥5 ✅）；benchmark **6**（✅）；工程 canon 项 **9**（✅）；核心概念 **25**（≥20 ✅）。**信号充沛，非冷僻行业**。
- 一手 endorsement 比例：30 源中 **24 verified_primary（arXiv/HF/github/官方）= 80%** ≥50% ✅。
- **诚实边界**：(1) 本 track 偏"应用工程 canon"，刻意略过纯训练/声学建模科研深水区；(2) RNN-T"主导流式"的工业地位是行业推断（原论文只做 TIMIT 音素），非单论文一手；(3) SenseVoice/部分厂商缺公开 WER/RTF 硬数；(4) 自报 WER 口径矛盾未解（这是行业现状，非数据缺陷）；(5) 课程维度本 track 未深挖——ASR 的 canon 以论文+开源 README 为主，正规课程少（CMU 11-751 / 各家 NeMo·icefall tutorial 可作 surrogate），Track 02/05 可补。
