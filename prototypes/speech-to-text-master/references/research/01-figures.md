# Track 01 — Figures: 语音转文字 / ASR (Speech-to-Text) 应用工程

> Research date: 2026-06-04 | Locale: zh-CN (canon 全球) | Track: 01 FIGURES
> **冷僻度判定**: tech / 开源工程领域。**figures 维度中等偏薄** —— "figures" 多为开源维护者、模型论文作者、厂商技术负责人，**单个有 30min+ 长访谈材料的人不多**（多数靠 repo/paper/talk 而非个人思想体系输出）。诚实标注：本 track 的主要价值是**立场光谱**（端侧免费派 vs 云 API 派 vs 中文专用派），而非"思想领袖名片"。建议 Phase 2 权重压向 tools/canon/workflows，figures 主要贡献**立场坐标系**。

## Source Manifest

| source_id | url | bucket | last_checked | author/host | one-line note |
|-----------|-----|--------|--------------|-------------|---------------|
| T01-S001 | https://github.com/ggml-org/whisper.cpp | verified_primary | 2026-06-04 | Georgi Gerganov | whisper.cpp 主仓 — 端侧推理基石 |
| T01-S002 | https://changelog.com/podcast/532 | verified_primary | 2026-06-04 | Changelog | Gerganov 长访谈 "bring Whisper/LLaMA to the masses" |
| T01-S003 | https://ggerganov.com/ | secondary | 2026-06-04 | Georgi Gerganov | 个人主页 (项目列表，无 manifesto) |
| T01-S004 | https://petewarden.com/2024/10/21/introducing-moonshine-the-new-state-of-the-art-for-speech-to-text/ | secondary | 2026-06-04 | Pete Warden | Moonshine 发布博文 (本人一手，但 verifier 判 secondary) |
| T01-S005 | https://github.com/usefulsensors/moonshine | verified_primary | 2026-06-04 | Useful Sensors / Pete Warden | Moonshine 主仓 — 移动/边缘 ASR |
| T01-S006 | https://www.eetimes.com/pete-warden-speech-to-intent-is-the-missing-piece-for-ai-agents/ | secondary | 2026-06-04 | EE Times | Warden 访谈 "speech-to-intent" 立场 |
| T01-S007 | https://github.com/k2-fsa/icefall | verified_primary | 2026-06-04 | k2-fsa (Povey et al) | next-gen Kaldi recipes — 开源 ASR 工程 |
| T01-S008 | https://scholar.google.com/citations?user=y_-5FWAAAAAJ&hl=en | verified_primary | 2026-06-04 | Daniel Povey | Povey scholar (Kaldi/k2 引用) |
| T01-S009 | https://www.youtube.com/watch?v=y6CJLFQlmhc | reference | 2026-06-04 | YouTube | "Speech Recognition with Next-gen Kaldi" talk |
| T01-S010 | https://awnihannun.com/ | secondary | 2026-06-04 | Awni Hannun | 个人站 (MLX/Deep Speech，本人一手) |
| T01-S011 | https://github.com/ml-explore/mlx | verified_primary | 2026-06-04 | ml-explore (Hannun et al) | MLX — Apple Silicon 端侧框架 |
| T01-S012 | https://arxiv.org/abs/2212.04356 | verified_primary | 2026-06-04 | Radford, Kim et al (OpenAI) | Whisper 论文 — 弱监督大规模 ASR |
| T01-S013 | https://arxiv.org/abs/2510.06961 | verified_primary | 2026-06-04 | Srivastav et al (HF) | Open ASR Leaderboard 论文 (2025-10) |
| T01-S014 | https://github.com/huggingface/open_asr_leaderboard | verified_primary | 2026-06-04 | Hugging Face | 开源 ASR 评测榜 repo |
| T01-S015 | https://huggingface.co/reach-vb | verified_primary | 2026-06-04 | Vaibhav Srivastav | VB 的 HF 主页 (audio/on-device DevRel) |
| T01-S016 | https://github.com/modelscope/FunASR | verified_primary | 2026-06-04 | 阿里 DAMO Speech Lab | FunASR 工业级 ASR 工具箱 |
| T01-S017 | https://arxiv.org/abs/2305.11013 | verified_primary | 2026-06-04 | Zhifu Gao et al (DAMO) | FunASR 论文 — Paraformer 等 |
| T01-S018 | https://github.com/FunAudioLLM/SenseVoice | verified_primary | 2026-06-04 | 阿里 FunAudioLLM | SenseVoice 端侧多语 ASR+情感 |
| T01-S019 | https://huggingface.co/funasr/paraformer-zh | verified_primary | 2026-06-04 | 阿里 DAMO | Paraformer 中文非自回归模型 |
| T01-S020 | https://github.com/SYSTRAN/faster-whisper | verified_primary | 2026-06-04 | SYSTRAN / G. Klein | faster-whisper (CTranslate2 后端) |
| T01-S021 | https://github.com/guillaumekln | secondary | 2026-06-04 | Guillaume Klein | CTranslate2/faster-whisper 作者 GH |
| T01-S022 | https://github.com/NVIDIA-NeMo/NeMo | verified_primary | 2026-06-04 | NVIDIA | NeMo — Parakeet/Canary 出处 |
| T01-S023 | https://developer.nvidia.com/blog/pushing-the-boundaries-of-speech-recognition-with-nemo-parakeet-asr-models/ | verified_primary | 2026-06-04 | NVIDIA | Parakeet ASR 工程博文 (vendor eng blog) |
| T01-S024 | https://voice-ai-newsletter.krisp.ai/p/100k-parallel-conversations-scott | secondary | 2026-06-04 | Krisp Voice AI | Stephenson 访谈 (延迟/规模经济) |
| T01-S025 | https://siliconangle.com/2026/01/13/real-time-voice-ai-unicorn-deepgram-raises-130m-streamline-human-machine-interactions/ | secondary | 2026-06-04 | SiliconANGLE | Deepgram 2026-01 融资 + 500ms 立场 |
| T01-S026 | https://voice-ai-newsletter.krisp.ai/p/promptable-speech-language-models | secondary | 2026-06-04 | Krisp Voice AI | Dylan Fox 访谈 (可提示语音 LM) |
| T01-S027 | https://www.unite.ai/dylan-fox-ceo-founder-of-assemblyai-interview-series/ | secondary | 2026-06-04 | Unite.AI | Fox 访谈 (AssemblyAI 起源/愿景) |
| T01-S028 | https://www.youtube.com/watch?v=DTghLFSUZ0A | reference | 2026-06-04 | YouTube/FirstMark | Fox talk "Generative AI for Speech Recognition" |
| T01-S029 | https://picovoice.ai/platform/leopard/ | surrogate_primary | 2026-06-04 | Picovoice | vendor docs — Leopard 端侧 STT (Kenarsari 立场) |
| T01-S030 | https://medium.com/picovoice/20-mb-is-all-you-need-for-speech-to-text-7e701b7f6bfc | secondary | 2026-06-04 | A. Kenarsari (Picovoice) | "20MB is all you need" — 本人一手立场文 |
| T01-S031 | https://bytedancespeech.github.io/seedasr_tech_report/ | secondary | 2026-06-04 | ByteDance Seed | Seed-ASR 技术报告页 |
| T01-S032 | https://arxiv.org/abs/2407.04675 | verified_primary | 2026-06-04 | ByteDance Seed Team | Seed-ASR 论文 (LLM-based ASR, 2024-07) |
| T01-S033 | https://www.xfyun.cn/doc/asr/voicedictation/Android-SDK.html | surrogate_primary | 2026-06-04 | 讯飞开放平台 | vendor docs — 讯飞 ASR Android SDK |
| T01-S034 | https://huggingface.co/UsefulSensors/moonshine-base | verified_primary | 2026-06-04 | Useful Sensors | Moonshine-base 模型卡 |

> **bucket 说明**: 个人博客/独立 newsletter (petewarden.com / awnihannun.com / krisp.ai) verifier 默认判 `secondary`，但内容多为 figure 本人一手或一手访谈，正文中按"一手/二手"另行标注。Picovoice / 讯飞 官网按指令作 `surrogate_primary` note `vendor docs`。

---

## 总览（按 mobile/低成本 relevance + 影响力排序）

| # | 姓名 | 核心身份 | 一句话贡献 | 立场 | 值得读/听/看 | 来源数 |
|---|------|---------|----------|------|------------|-------|
| 1 | Georgi Gerganov | ggml.ai 创始人 | whisper.cpp/ggml — 把 Whisper 塞进 CPU/手机，端侧推理事实标准 | **端侧免费派** | 📖🎙️ | 3 |
| 2 | Pete Warden | Useful Sensors CEO | Moonshine — 为边缘/实时重新设计的 ASR，反 Whisper 30s 定长 | **端侧免费派(极致)** | 📖🎬 | 4 |
| 3 | Daniel Povey | 小米首席语音科学家 | Kaldi → k2/icefall，ASR 开源教父，专用流式(RNN-T/CTC)阵营 | **开源专用流式派** | 🎬📖 | 3 |
| 4 | Awni Hannun | Anthropic(原 Apple/MLX) | MLX — Apple Silicon 端侧训练/推理框架；Deep Speech 共同作者 | **端侧 + 学术** | 📖🎙️ | 3 |
| 5 | Vaibhav Srivastav (VB) | HF Head of DevX | Open ASR Leaderboard 推动者 + Insanely Fast Whisper，端侧/开源布道 | **开源评测/布道派** | 📖🎬 | 3 |
| 6 | Zhifu Gao + Shiliang Zhang | 阿里 DAMO Speech Lab | FunASR/Paraformer/SenseVoice — 中文 ASR 开源工业标杆 | **中文专用 + 开源** | 📖 | 4 |
| 7 | Alireza Kenarsari | Picovoice CEO | 端侧 STT(Cheetah/Leopard)，"20MB 足够"，隐私+零延迟商业派 | **端侧商业派** | 📖 | 3 |
| 8 | Scott Stephenson | Deepgram CEO | 自建 ASR 模型，实时<500ms，规模经济(10x 便宜)，云 API 派 | **云 API 派(实时)** | 🎙️📖 | 3 |
| 9 | Dylan Fox | AssemblyAI CEO | 把 ASR 当"语音 LM"基础设施，可提示/语义理解，云 API 派 | **云 API 派(语音 LM)** | 🎙️🎬 | 4 |
| 10 | Alec Radford (+ Jong Wook Kim) | 原 OpenAI | Whisper 论文一作 — 弱监督大规模，开启通用大模型 ASR 时代 | **通用大模型派(奠基)** | 📖 | 1 |
| 11 | Boris Ginsburg (NeMo 团队) | NVIDIA | NeMo/Parakeet/Canary — GPU 端高吞吐专用流式 ASR | **专用流式 + GPU** | 📖🎬 | 2 |
| 12 | Guillaume Klein | 原 SYSTRAN | faster-whisper/CTranslate2 — Whisper 量化/4x 加速的工程化 | **开源效率派** | — | 2 |
| 13 | ByteDance Seed (火山语音) | 字节 | Seed-ASR — LLM-based 中文 ASR，上下文增强 | **中文 + LLM-based** | 📖 | 2 |
| 14 | 讯飞 (刘庆峰/语音团队) | 科大讯飞 | 中文 ASR 老牌厂商，云+端 SDK，方言/热词工程化 | **中文云 API 派(老牌)** | (vendor docs) | 1 |

---

## Figures 详细卡片

### 1. Georgi Gerganov（格奥尔基·盖尔加诺夫）

- **One-liner**: whisper.cpp / ggml 作者 —— 把 Whisper 用纯 C/C++ 跑在 CPU 和 Apple Silicon 上，成为端侧 ASR 推理的事实标准；llama.cpp 的同一人 (evidence: [T01-S001, T01-S002])
- **核心身份**: ggml.ai 创始人；whisper.cpp / llama.cpp / ggml 作者
- **代表作品**: whisper.cpp (T01-S001)、ggml 张量库、llama.cpp
- **值得读 / 听 / 看的 3 件事**:
  - 📖 whisper.cpp repo + README/discussions: https://github.com/ggml-org/whisper.cpp (T01-S001)
  - 🎙️ Changelog #532 "Bringing Whisper and LLaMA to the masses": https://changelog.com/podcast/532 (T01-S002)
  - 🎬 ⚠️ 无独立 conference keynote（主要靠 repo + podcast 发声）
- **核心思想关键词**: 端侧推理 (on-device)、零依赖 (minimal/no third-party deps)、Apple Silicon (NEON/Accelerate/ANE)、量化 (ggml/int)、社区自治 (community stewardship)
- **voice_samples**:
  - 同业/工程讨论样本: 「I prefer things to be super-minimal and without any third-party dependencies」—— 设计哲学：clone、`make`、run，降低门槛 (source: T01-S002, 原话)
  - 立场样本: 「being able to run them on consumer hardware is something that sounds definitely interesting」—— 把强模型放到普通硬件上 (source: T01-S002, 原话)
  - 推断样本: ggml 最初是纯张量代数 hobby，Whisper 发布后他发现 transformer 结构和自己的 GPT-2 实现相似，遂移植到 C/C++ 做 CPU 推理；他不想做长期 maintainer，希望社区接管 (source: T01-S002, 转述)
- **sub_skill_candidate**: `false` —— 极重要但属"靠工程产品输出而非个人思想体系"，长访谈材料仅 1 篇 podcast，不够独立成 sub-skill；其立场("端侧免费")应进 Phase 2 心智模型
- **最近 12 个月动态**: ggml.ai 持续作为 whisper.cpp/llama.cpp 的承载组织；whisper.cpp 仓库迁至 `ggml-org` org，持续 release (evidence: [T01-S001])
- **争议 / 批评**: whisper.cpp 长期落后于上游 Whisper 的某些特性（如部分语言/时间戳精度）；纯 CPU 路线在超大模型/超低延迟流式上不如 GPU 专用栈；"零依赖"哲学有时牺牲可维护性。
- **来源**:
  - [Primary] whisper.cpp repo: T01-S001 (collected 2026-06-04)
  - [Primary/访谈] Changelog #532: T01-S002
  - [Reference] 个人主页: T01-S003
- **可信度自评**: high —— repo 一手 + 一篇深度 podcast，立场清晰。

### 2. Pete Warden

- **One-liner**: Useful Sensors CEO，Moonshine 作者 —— 为边缘/实时**重新设计** ASR，公开反对 Whisper 的 30 秒定长输入与 RAM 占用，端侧极致派 (evidence: [T01-S004, T01-S005, T01-S006])
- **核心身份**: Useful Sensors 创始人/CEO；Stanford；前 Google TensorFlow Lite for Microcontrollers 核心
- **代表作品**: Moonshine 模型族 (tiny 26M / base 54M)；Moonshine v2 (ergodic streaming-encoder)
- **值得读 / 听 / 看的 3 件事**:
  - 📖 "Introducing Moonshine, the new SOTA for speech to text" (本人博客): https://petewarden.com/2024/10/21/... (T01-S004)
  - 📖 Moonshine repo + 模型卡: https://github.com/usefulsensors/moonshine (T01-S005)
  - 🎬 EE Times 访谈 "Speech-to-Intent is the Missing Piece for AI agents": (T01-S006)
- **核心思想关键词**: 端侧/离线 (run everything locally, no network)、低延迟 (latency = voice 不普及的根因)、变长输入 (variable-length window)、隐私、microcontroller/embedded、speech-to-intent
- **voice_samples**:
  - 客户/科普解释样本: 把 2 秒延迟类比"打字时每个键要 2 秒才出现"——解释为何语音界面没普及 (source: T01-S004, 转述)
  - 立场样本: 「run everything locally on the device, without any network connection, safeguarding privacy and letting us run anywhere in the world, instantly」(source: T01-S004, 原话)
  - 工程批评样本: 「Even the smallest Whisper model requires at least 30MB of RAM」—— 因大动态激活层无法存进 flash，是 MCU 的致命限制；Whisper 固定 30 秒 chunk，短语音也要 zero-pad，浪费算力 (source: T01-S004, 原话+转述)
- **sub_skill_candidate**: `false` —— 立场鲜明且有博客+访谈，但仍偏"产品+工程"输出，单人思想体系深度不足以独立 sub-skill；其"端侧极致/反定长"观点进 Phase 2。
- **最近 12 个月动态**: Moonshine v2（流式 encoder，滑窗自注意力，有界低延迟）发布；扩展多语模型卡（ko/vi 等 tiny 版） (evidence: [T01-S005])
- **争议 / 批评**: Moonshine 主打英文/小语种短音频，长音频与多语广度不及 Whisper-large；"边缘优先"在需要最高准确率的云场景不适用。
- **来源**:
  - [Primary] 本人博客: T01-S004
  - [Primary] Moonshine repo: T01-S005
  - [Secondary] EE Times 访谈: T01-S006
- **可信度自评**: high —— 一手博客+repo+访谈，立场是"端侧/低成本"的最纯代表。

### 3. Daniel Povey（丹尼尔·波维）

- **One-liner**: Kaldi 之父，next-gen Kaldi (k2/icefall/Lhotse) 主创 —— ASR 开源工程的奠基者，专用流式(RNN-T/CTC/CR-CTC)阵营的学术+工程双角色 (evidence: [T01-S007, T01-S008])
- **核心身份**: 小米 (Xiaomi) 首席语音科学家 (2019 起，离开 JHU)；k2-fsa 组织
- **代表作品**: Kaldi (老一代)；k2 (C++ FST/lattice 核心)、icefall (recipes)、Lhotse (数据准备)；CR-CTC (ICLR 2025)
- **值得读 / 听 / 看的 3 件事**:
  - 🎬 "Speech Recognition with Next-Generation Kaldi (k2/Lhotse/icefall)": https://youtube.com/watch?v=y6CJLFQlmhc (T01-S009)
  - 📖 icefall recipes repo: https://github.com/k2-fsa/icefall (T01-S007)
  - 📖 Google Scholar (Kaldi/k2 高引): T01-S008
- **核心思想关键词**: 开源 recipe 文化、FST/lattice、专用流式 (RNN-T/CTC/Conformer/Zipformer)、可复现、端到端 e2e ASR、效率 (CR-CTC)
- **voice_samples**: ⚠️ 暂未找到 ≥ 30 字稳定可引用的直接原话片段（主要发声为 talk + repo issue + 论文；个人不爱长访谈）。next-gen Kaldi 的官方定位（转述）：「k2 是一堆 C++ 核心算法，含 lattice 和 FST；icefall 是 recipes，大部分精力在这里；Lhotse 管数据准备」(source: T01-S007 / next-gen Kaldi 介绍，转述)
- **sub_skill_candidate**: `false` —— 影响力极大但属 Track 04 canon 取向（论文/recipe 为主，长访谈材料 <30min），dual_role 标注后立场进 Phase 2。
- **dual_role**: `"academic + engineering"`（学术高产 + 小米工业部署 + 开源 recipe 维护）
- **最近 12 个月动态**: CR-CTC 论文 2025-02 被 ICLR 接收；k2/icefall 持续迭代 Zipformer 等流式架构 (evidence: [T01-S007])
- **争议 / 批评**: Kaldi/k2 学习曲线极陡，工程上手成本远高于 whisper.cpp / faster-whisper；"recipe 文化"对非研究者不友好；在"通用大模型 vs 专用"之争中代表与 Whisper 路线相反的专用流式阵营。
- **来源**:
  - [Primary] icefall repo: T01-S007
  - [Primary] Scholar: T01-S008
  - [Reference] next-gen Kaldi talk: T01-S009
- **可信度自评**: medium —— 影响力 high，但**个人 voice 材料薄**（无长访谈），故降一档。

### 4. Awni Hannun

- **One-liner**: MLX 共同作者（Apple Silicon 端侧训练/推理框架），Deep Speech (Baidu, Andrew Ng 门下) 共同作者 —— 端侧 + 学术双角色，2026-02 离开 Apple 加入 Anthropic (evidence: [T01-S010, T01-S011])
- **核心身份**: Anthropic 技术成员 (2026-02 起)；原 Apple ML 研究科学家 (MLX 共同创建)；曾在 Zoom / FAIR / Baidu SVAIL
- **代表作品**: MLX (T01-S011)、mlx-examples (含 Whisper 端侧实现)；Deep Speech / Deep Speech 2 (ICML 2016，中英文 e2e)
- **值得读 / 听 / 看的 3 件事**:
  - 📖 个人站 + 博客 (MLX Whisper benchmark): https://awnihannun.com/ (T01-S010)
  - 📖 MLX repo: https://github.com/ml-explore/mlx (T01-S011)
  - 🎙️ ⚠️ 长访谈较少；X (@awnihannun) 高频技术更新
- **核心思想关键词**: 端侧 (on-device LLM/ASR)、Apple Silicon (M 系列统一内存)、e2e 语音 (Deep Speech 谱系)、开源框架、本地微调 (LoRA/RLHF on device)
- **voice_samples**:
  - 立场样本: 「A ~2 year old Macbook using Whisper is almost as fast as the fastest [consumer] graphics card」—— MLX 端侧 Whisper benchmark 的核心卖点 (source: awnihannun X/blog via T01-S010, 原话)
  - 推断样本: 强调 MLX 让 LLM/VLM/Whisper "run on device"、本地微调；他从 Baidu Deep Speech 的"大规模端到端"路线一路走到 Apple 端侧 (source: T01-S010/T01-S011, 转述)
  - ⚠️ 监管/标准 register 样本未找到（其发声集中在工程/框架）
- **sub_skill_candidate**: `false` —— dual_role 价值高，但长访谈材料不足，立场（端侧 e2e）进 Phase 2。
- **dual_role**: `"academic + engineering"`（Deep Speech 学术 + MLX 工程）
- **最近 12 个月动态**: **2026-02-28 离开 Apple**，加入 Anthropic；MLX 社区 contributors 破百，Swift 端侧示例/文档完善 (evidence: [T01-S010])
- **争议 / 批评**: MLX 仅限 Apple Silicon 生态，跨平台性不如 ggml/llama.cpp；离开 Apple 后 MLX 的长期治理存疑。
- **来源**:
  - [Primary] 个人站: T01-S010
  - [Primary] MLX repo: T01-S011
  - [Reference] Deep Speech 谱系 (见 canon)
- **可信度自评**: medium-high —— 一手站点+repo 清晰，但 ASR 专项长访谈少。

### 5. Vaibhav Srivastav（VB）

- **One-liner**: Hugging Face Head of Developer Experience —— Open ASR Leaderboard 主要推动者 + "Insanely Fast Whisper"，开源/端侧 audio 的头号布道者，把"选哪个 ASR"变成可复现 benchmark (evidence: [T01-S013, T01-S015])
- **核心身份**: Hugging Face Head of DevX & Community（聚焦 open source / audio / on-device ML）
- **代表作品**: Open ASR Leaderboard (论文 arxiv 2510.06961 + repo)、Insanely Fast Whisper、ASR+diarization+speculative decoding 教程
- **值得读 / 听 / 看的 3 件事**:
  - 📖 Open ASR Leaderboard 论文 (2025-10): https://arxiv.org/abs/2510.06961 (T01-S013)
  - 📖 Leaderboard repo: https://github.com/huggingface/open_asr_leaderboard (T01-S014)
  - 🎬 HF 主页 + posts (audio/on-device 更新): https://huggingface.co/reach-vb (T01-S015)
- **核心思想关键词**: 可复现评测 (WER + RTFx)、开源优先、端侧/本地、量化加速 (insanely fast)、accuracy-efficiency 权衡、GPU-poor 友好
- **voice_samples**:
  - 工程/布道样本: Open ASR Leaderboard 标准化文本归一化，同时报 WER 和 RTFx (inverse real-time factor)，让 accuracy-efficiency 可公平对比 (source: T01-S013, 转述)
  - 推断样本: 持续推 "insanely fast whisper" CLI、本地/Inference Endpoints 上跑 ASR+diarization，立场是把强 ASR 普及给无大算力的开发者 (source: T01-S015, 转述)
  - ⚠️ 稳定 ≥30 字直接原话片段多在 X/LinkedIn（黑名单正文，不引）
- **sub_skill_candidate**: `false` —— DevRel/布道角色，非独立思想体系；但其**评测方法论 (WER×RTFx)** 对 Phase 2 选型决策树极有价值。
- **最近 12 个月动态**: Open ASR Leaderboard 升级**多语 + 长音频赛道**（论文 v4，2025-10），覆盖 86 系统 / 12 数据集 (evidence: [T01-S013])
- **争议 / 批评**: leaderboard 偏 HF 生态数据集，某些闭源商业 API 的真实生产表现未必被公平覆盖；DevRel 立场天然偏开源。
- **来源**:
  - [Primary] 论文: T01-S013
  - [Primary] repo: T01-S014
  - [Primary] HF 主页: T01-S015
- **可信度自评**: high —— 论文+repo+官方主页三重一手。

### 6. Zhifu Gao（高志付）+ Shiliang Zhang（张仕良）— 阿里 DAMO Speech Lab

- **One-liner**: FunASR / Paraformer / SenseVoice 核心作者 —— 中文 ASR 开源工业标杆，把"非自回归并行 transformer (Paraformer)"和端侧多语 SenseVoice 推成中文场景默认选项 (evidence: [T01-S016, T01-S017, T01-S018])
- **核心身份**: 阿里巴巴达摩院 Speech Lab（团队署名，Zhifu Gao 为 FunASR/Paraformer 一作，Shiliang Zhang 为通讯/资深作者）
- **代表作品**: FunASR 工具箱 (T01-S016)、Paraformer (非自回归 e2e，60k 小时中文)、SenseVoice (ASR+LID+SER+AED 多任务，中粤英日韩)、FunAudioLLM
- **值得读 / 听 / 看的 3 件事**:
  - 📖 FunASR 论文: https://arxiv.org/abs/2305.11013 (T01-S017)
  - 📖 FunASR repo (170x realtime, 50+ 语言, 含流式): https://github.com/modelscope/FunASR (T01-S016)
  - 📖 SenseVoice repo (端侧多语+情感): https://github.com/FunAudioLLM/SenseVoice (T01-S018)
- **核心思想关键词**: 非自回归 (NAR/Paraformer)、中文/方言优先、工业级 (170x realtime)、端侧 (SenseVoice 小模型)、多任务 (ASR+情感+事件)、开源 (ModelScope)
- **voice_samples**: ⚠️ 暂未找到团队成员 ≥30 字公开口语原话片段（发声以论文 + repo README + ModelScope 文档为主，本 track 不引知乎/公众号）。论文核心主张（转述）：Paraformer 用 NAR 并行解码在保持准确率的同时大幅提速，针对工业部署 (source: T01-S017, 转述)
- **sub_skill_candidate**: `false` —— 团队署名而非单一思想领袖，属 canon/tools 取向；但"中文专用 + 开源 + 端侧"立场是 Phase 2 中文派核心。
- **最近 12 个月动态**: SenseVoice 持续作为中文端侧首选；FunASR 维持 OpenAI 兼容 API + 流式/说话人分离；FunAudioLLM 线扩展（含 Fun-ASR 大模型，arxiv 2509.12508） (evidence: [T01-S016, T01-S018])
- **争议 / 批评**: 英文/多语广度不及 Whisper-large 与 NeMo Canary；模型与 ModelScope/阿里生态耦合，海外社区集成文档较少；团队个人公开发声少（偏匿名工业输出）。
- **来源**:
  - [Primary] FunASR repo: T01-S016
  - [Primary] FunASR 论文: T01-S017
  - [Primary] SenseVoice repo: T01-S018
  - [Primary] Paraformer 模型卡: T01-S019
- **可信度自评**: high（作品/repo）/ medium（个人 voice）—— 综合 medium-high。

### 7. Alireza Kenarsari（Picovoice CEO）

- **One-liner**: Picovoice 创始人 —— 端侧 STT (Cheetah 流式 / Leopard 批量)，主张"20MB 足够做 STT"，隐私+零延迟+10x 降本的**端侧商业派**，对标并声称在部分 benchmark 超过云 (evidence: [T01-S029, T01-S030])
- **核心身份**: Picovoice (Vancouver) 创始人/CEO；前 Amazon 资深工程师 (有 DL/语音专利)
- **代表作品**: Cheetah (流式端侧 STT)、Leopard (端侧批量 STT)、Porcupine (唤醒词)；客户含 NASA / LG / Analog Devices
- **值得读 / 听 / 看的 3 件事**:
  - 📖 "20 MB is all you need for speech-to-text" (本人 Medium): T01-S030
  - 📖 Leopard 平台页 (端侧 STT，vendor docs): https://picovoice.ai/platform/leopard/ (T01-S029)
  - 🎙️ ⚠️ 长 podcast 较少；多为厂商博客 + 媒体访谈
- **核心思想关键词**: 端侧/离线、隐私优先、零延迟、小模型 (20MB)、降本 10x、"准确且高效" (accurate AND efficient)、去 FAANG 化（让无大厂资源的企业也能用）
- **voice_samples**:
  - 立场/反主流样本: 「If you tell Alexa to turn off the lights, does it really need to go through half of the planet, go to a data center, and come back? Probably not.」—— 质疑云端处理简单指令的必要性 (source: 媒体访谈 via T01-S029 上下文, 原话)
  - 商业立场样本: 「everybody is focused on building accurate speech models, Picovoice is focused on building accurate and efficient speech models」—— 最小模型却号称击败云准确率 (source: T01-S030 上下文, 转述)
  - 科普样本: Cheetah 14.34% WER（实时）vs Leopard 11% WER；Cheetah 号称是唯一在未定制前就达到云 WER 的端侧实时引擎 (source: T01-S029, vendor 数据/转述，**需 ≥2 源校验**)
- **sub_skill_candidate**: `false` —— 厂商立场清晰但属商业 PR 取向，思想体系深度有限；"端侧商业派"坐标进 Phase 2。
- **最近 12 个月动态**: 持续扩 edge voice AI + LLM 端侧组合；2025 强调 voice AI/LLM 与边缘计算结合 (evidence: [T01-S029])
- **争议 / 批评**: "端侧超过云准确率"的 benchmark 多为厂商自测（vendor docs，须二次校验）；闭源商业 SDK，与 whisper.cpp/FunASR 的开源免费路线对立；自由额度受限。
- **来源**:
  - [Primary/本人] Medium 立场文: T01-S030
  - [Surrogate/vendor] Leopard 平台页: T01-S029
  - [Reference] 创始访谈 (GeekWire/Made in CA)
- **可信度自评**: medium —— 立场鲜明但来源偏 vendor，准确率宣称需对照 Open ASR Leaderboard 校验。

### 8. Scott Stephenson（Deepgram CEO）

- **One-liner**: Deepgram 联合创始人/CEO（暗物质物理学家转行）—— **自建 ASR 模型**而非套通用 LLM，主打实时<500ms + 规模经济（10x 更便宜难在 scale），云 API 派代表 (evidence: [T01-S024, T01-S025])
- **核心身份**: Deepgram 联合创始人/CEO；前粒子物理 PhD (UMich，地下两英里暗物质实验室)
- **代表作品**: Deepgram STT API、Nova 系列模型、Flux (2025-10 "对话式语音识别"模型)、Aura TTS
- **值得读 / 听 / 看的 3 件事**:
  - 🎙️ Krisp Voice AI 访谈 "100K parallel conversations": T01-S024
  - 📖 SiliconANGLE 2026-01 (融资$130M + 500ms 立场): T01-S025
  - 🎬 Deepgram/Project Voice talks (官方 blog)
- **核心思想关键词**: 实时/流式 (<500ms)、自建模型 (build own ASR)、规模经济 (10x cheaper at scale)、accuracy×speed×price 三角、对话式 (conversational, Flux)、"skeptical → inevitable"
- **voice_samples**:
  - 立场样本: 「The response has to be generated in 500 milliseconds or less」—— 实时语音的硬门槛与一般 AI 体验不同 (source: T01-S025, 原话)
  - 商业洞察样本: 「It's easy to get an AI model to work but way, way harder to scale it with a 10x cheaper price」—— 竞争优势来自基础设施效率而非单纯模型质量 (source: T01-S024, 原话)
  - 行业判断样本: 2025 语音 AI 市场从"因 Siri/IVR 笨拙而被轻视"转向"skeptical to inevitable"；Flux「listens, understands, and guides conversations with human-like timing」(source: T01-S025, 原话+转述)
- **sub_skill_candidate**: `false` —— 有多篇访谈但属厂商 CEO 立场输出；"云 API 实时派"坐标进 Phase 2。
- **最近 12 个月动态**: 2025-10 发布 Flux（号称首个"对话式语音识别"模型）；**2026-01 融资 $130M**，估值 unicorn (evidence: [T01-S025])
- **争议 / 批评**: 云 API 路线在隐私/离线/成本敏感（端侧免费）场景与 Gerganov/Warden/Kenarsari 直接对立；"对话式 ASR"边界与语音 agent 有重叠（intake 明确不含语音 agent）；自建模型的准确率领先随开源追赶而收窄。
- **来源**:
  - [Secondary/访谈] Krisp: T01-S024
  - [Secondary] SiliconANGLE: T01-S025
  - [Reference] Deepgram 官方 blog/podcast
- **可信度自评**: high —— 多篇近期访谈，立场与时间线清晰。

### 9. Dylan Fox（AssemblyAI CEO）

- **One-liner**: AssemblyAI 创始人/CEO —— 把 ASR 重新定位为"**语音语言模型 (Speech LM)**"基础设施（可提示、带语义理解），云 API 派中的"语音 LM"分支 (evidence: [T01-S026, T01-S027])
- **核心身份**: AssemblyAI 创始人/CEO (2017 起，YC 出身，Series C >$115M)；前 Cisco 研究工程师
- **代表作品**: Universal(-2) STT、Streaming STT、Speech Understanding / LeMUR（LLM over 音频）、可提示语音模型
- **值得读 / 听 / 看的 3 件事**:
  - 🎙️ Krisp 访谈 "Promptable Speech Language Models" (2026-02): T01-S026
  - 📖 Unite.AI 访谈系列 (起源/愿景): T01-S027
  - 🎬 FirstMark "Generative AI for Speech Recognition": https://youtube.com/watch?v=DTghLFSUZ0A (T01-S028)
- **核心思想关键词**: 语音语言模型 (Speech LM)、可提示 (promptable)、语义理解 (speech understanding 不止转写)、基础设施 (foundational voice infra)、企业级、generative ASR
- **voice_samples**:
  - 立场样本: 把 ASR 当"speech language model"基础设施——不只是转文字，而是可提示、能做语义理解的下一代语音 AI 底座 (source: T01-S026, 转述)
  - 起源样本: 2017 受 Alexa 等语音产品启发创立，源于在 Cisco 做 AI 产品的经历 (source: T01-S027, 转述)
  - ⚠️ 稳定 ≥30 字直接原话片段需从 podcast 音频转写补全
- **sub_skill_candidate**: `false` —— 厂商 CEO，多访谈但非独立思想体系；"云 API / 语音 LM 派"坐标进 Phase 2。
- **最近 12 个月动态**: 推"可提示语音 LM"（2026-02 访谈主题）；Universal 模型迭代，强调 speech understanding 而非纯转写 (evidence: [T01-S026])
- **争议 / 批评**: 与 Deepgram 同为云 API 派，但"语音 LM/语义理解"方向与 intake "不含语音 agent/对话式 AI"边界擦边；纯转写场景下相对开源 Whisper 的性价比受质疑。
- **来源**:
  - [Secondary/访谈] Krisp: T01-S026
  - [Secondary] Unite.AI: T01-S027
  - [Reference] FirstMark talk: T01-S028
- **可信度自评**: high —— 多个长访谈 + talk。

### 10. Alec Radford（+ Jong Wook Kim 等，Whisper 论文）

- **One-liner**: Whisper 论文一作（原 OpenAI）—— 用 68 万小时弱监督把 ASR 推进"通用大模型零样本"时代，是当代几乎所有端侧/云 ASR 工程的共同祖先 (evidence: [T01-S012])
- **核心身份**: 原 OpenAI 研究员（GPT/CLIP/Whisper 多个奠基工作一作）
- **代表作品**: Whisper ("Robust Speech Recognition via Large-Scale Weak Supervision", 2022)；合作者 Jong Wook Kim, Tao Xu, Greg Brockman, Christine McLeavey, Ilya Sutskever
- **值得读 / 听 / 看的 3 件事**:
  - 📖 Whisper 论文: https://arxiv.org/abs/2212.04356 (T01-S012)
  - 🎙️ ⚠️ Radford 极少长访谈（偏纯研究输出）
  - 🎬 ⚠️ 无对应工程 talk（纯 paper register）
- **核心思想关键词**: 弱监督 (weak supervision)、大规模 (680k hours)、零样本迁移 (zero-shot)、多任务多语 (multitask/multilingual)、鲁棒性 (robust)、scale
- **voice_samples**: ⚠️ 暂未找到 ≥30 字工程/口语原话片段（输出为论文，无长访谈）。论文核心主张（转述）：仅靠大规模弱监督数据，模型即可在标准 benchmark 上零样本逼近全监督结果，无需 fine-tune (source: T01-S012, 转述)
- **sub_skill_candidate**: `false` —— **纯学术 figure，应主要进 Track 04 (canon)**；无长访谈/工程 talk，不满足本 track dual_role 例外。列于此仅为标注"通用大模型派"的奠基坐标。
- **dual_role**: 否（纯 academic）—— 按 iter4 规则本应仅入 canon，此处保留为立场锚点。
- **最近 12 个月动态**: ⚠️ Radford 本人公开动态稀少；Whisper 谱系由社区 (whisper.cpp/faster-whisper/distil-whisper) 继续推进 (evidence: [T01-S012])
- **争议 / 批评**: Whisper 30 秒定长、幻觉 (hallucination)、长音频/流式不友好、RAM 占用——正是 Moonshine/专用流式阵营批评与改进的靶子。
- **来源**:
  - [Primary] Whisper 论文: T01-S012
- **可信度自评**: low（作为 figure）—— 仅 1 篇论文一手、无个人 voice 材料；**建议作为 canon 作者而非 figure 看待**。

### 11. Boris Ginsburg（+ NeMo 团队）— NVIDIA

- **One-liner**: NVIDIA NeMo 语音负责人方向 —— Parakeet / Canary 系列（RNN-T/TDT/Conformer），GPU 端高吞吐专用流式 ASR，准确率+RTFx 榜单常客 (evidence: [T01-S022, T01-S023])
- **核心身份**: NVIDIA（NeMo 框架团队；Canary 论文署名含 Boris Ginsburg, Jagadeesh Balam, Vitaly Lavrukhin 等）
- **代表作品**: NeMo 框架、Parakeet (RNN-T/TDT, 与 Suno.ai 合作)、Canary (多语 ASR+翻译)、Granary 数据集
- **值得读 / 听 / 看的 3 件事**:
  - 📖 Parakeet ASR 工程博文: https://developer.nvidia.com/blog/pushing-the-boundaries-...-parakeet... (T01-S023)
  - 📖 NeMo repo: https://github.com/NVIDIA-NeMo/NeMo (T01-S022)
  - 🎬 NVIDIA Speech AI talks (GTC，多为团队)
- **核心思想关键词**: 专用流式 (RNN-T/TDT/Conformer)、GPU 高吞吐 (RTFx)、工业级准确率、开源模型+数据集 (Granary)、多语+翻译 (Canary)
- **voice_samples**: ⚠️ 团队署名，个人 ≥30 字口语原话片段未找到（输出为 NVIDIA 技术博客 + 论文 + 模型卡）。立场（转述）：Parakeet/Canary 在 Open ASR Leaderboard 上以高准确率 + 高 RTFx 主打 GPU 部署效率 (source: T01-S023, 转述)
- **sub_skill_candidate**: `false` —— 团队/厂商工程输出，非个人思想体系；"专用流式 + GPU"坐标进 Phase 2。
- **最近 12 个月动态**: Parakeet-tdt-0.6b-v3 等新模型 + Granary 开放数据集/多语模型发布（与 CMU、Fondazione Bruno Kessler 合作） (evidence: [T01-S023])
- **争议 / 批评**: 主打 GPU 部署，端侧/移动场景非其强项（与 whisper.cpp/Moonshine 路线互补而非竞争）；模型与 NVIDIA 生态/CUDA 强绑定。
- **来源**:
  - [Primary] NeMo repo: T01-S022
  - [Primary] Parakeet 博文: T01-S023
- **可信度自评**: medium —— 作品/榜单一手清晰，个人 voice 缺失（团队署名）。

### 12. Guillaume Klein（faster-whisper / CTranslate2）

- **One-liner**: CTranslate2 与 faster-whisper 作者（原 SYSTRAN / OpenNMT）—— 用 INT8 量化把 Whisper 推理提速约 4x 且省内存，开源效率派的关键工程师 (evidence: [T01-S020, T01-S021])
- **核心身份**: 原 SYSTRAN（OpenNMT / CTranslate2 核心）；faster-whisper 维护者
- **代表作品**: CTranslate2 (transformer 快速推理引擎)、faster-whisper (Whisper on CT2)
- **值得读 / 听 / 看的 3 件事**:
  - 📖 faster-whisper repo: https://github.com/SYSTRAN/faster-whisper (T01-S020)
  - 📖 Guillaume Klein GitHub: https://github.com/guillaumekln (T01-S021)
  - 🎙️ ⚠️ 无长访谈（纯工程输出）
- **核心思想关键词**: 量化 (INT8)、推理引擎 (CTranslate2)、4x 加速、低内存、CPU+GPU、Whisper 工程化
- **voice_samples**: ⚠️ 暂未找到 ≥30 字口语原话片段（发声以 repo/README/issue 为主）。项目核心主张（转述）：faster-whisper 用 CTranslate2 后端，相同准确率下比 openai/whisper 快达 4x 且更省内存 (source: T01-S020, 转述)
- **sub_skill_candidate**: `false` —— 纯工程维护者，无个人思想体系；其"量化/推理引擎"实践进 Track 02。
- **最近 12 个月动态**: faster-whisper 持续 release（large-v3 等），是 WhisperX/众多生产管线的默认后端 (evidence: [T01-S020])
- **争议 / 批评**: 依赖 CTranslate2 的算子支持，新架构/新功能跟进慢于上游；个人公开发声极少（纯 repo 维护）。
- **来源**:
  - [Primary] faster-whisper repo: T01-S020
  - [Secondary] 个人 GH: T01-S021
- **可信度自评**: medium-low（作为 figure）—— repo 一手，但个人 voice/思想材料几乎为零；更像 Track 02 工具维护者。

### 13. ByteDance Seed / 火山语音团队（Seed-ASR）

- **One-liner**: 字节 Seed 团队 —— Seed-ASR (LLM-based ASR + 上下文增强)，豆包/火山引擎背后的中文 ASR 大模型，中英 WER/CER 较 e2e 降 10–40% (evidence: [T01-S031, T01-S032])
- **核心身份**: ByteDance Seed Team（团队署名，无公开个人）；火山引擎 (Volcano Engine) 商业化
- **代表作品**: Seed-ASR (论文 arxiv 2407.04675, 2024-07)、Doubao-Seed-ASR-2.0
- **值得读 / 听 / 看的 3 件事**:
  - 📖 Seed-ASR 论文: https://arxiv.org/abs/2407.04675 (T01-S032)
  - 📖 Seed-ASR 技术报告页: https://bytedancespeech.github.io/seedasr_tech_report/ (T01-S031)
  - 🎬 ⚠️ 无公开个人 talk（团队/产品发布为主）
- **核心思想关键词**: LLM-based ASR (audio-conditioned LLM)、上下文增强 (dialogue history/人名/热词)、中文/方言/口音、大规模训练、离线为主 (非流式)
- **voice_samples**: ⚠️ 团队署名，无个人原话；论文核心主张（转述）：Seed-ASR 在 audio-conditioned LLM 框架上，对多领域/方言/语言较 e2e 显著提升，中英公开测试集 WER/CER 降 10–40%，设计偏离线上下文理解而非实时流式 (source: T01-S031/T01-S032, 转述)
- **sub_skill_candidate**: `false` —— 团队/厂商，非个人 figure；"中文 + LLM-based ASR"坐标进 Phase 2。
- **最近 12 个月动态**: 推出 Doubao-Seed-ASR-2.0（多语识别准确率提升）；火山引擎扩 enterprise 客户（会议转写/字幕/审核） (evidence: [T01-S031])
- **争议 / 批评**: LLM-based 偏离线、延迟与成本对实时移动端不友好（与 intake "移动/低成本/快速"focus 部分错位）；闭源商业 API；技术报告为厂商一面之词，独立 benchmark 有限。
- **来源**:
  - [Primary] 论文: T01-S032
  - [Secondary] 技术报告页: T01-S031
- **可信度自评**: medium —— 论文一手，但属团队/厂商，个人 figure 维度为空。

### 14. 讯飞（刘庆峰 / 语音团队）— 科大讯飞

- **One-liner**: 中国老牌语音厂商 —— 中文 ASR 的云+端 SDK 工程化（方言/热词/听写），移动端集成的国内默认选项之一，云 API 派（老牌） (evidence: [T01-S033])
- **核心身份**: 科大讯飞（刘庆峰为董事长；语音研究院团队）；讯飞开放平台 (xfyun.cn)
- **代表作品**: 讯飞听见、语音听写/转写 API、Android/iOS ASR SDK、星火大模型语音线
- **值得读 / 听 / 看的 3 件事**:
  - 📖 讯飞 ASR Android SDK 文档 (vendor docs): https://www.xfyun.cn/doc/asr/voicedictation/Android-SDK.html (T01-S033)
  - 🎙️ ⚠️ 公开技术长访谈多在黑名单平台（不引）
  - 🎬 ⚠️ 个人 talk 难溯一手
- **核心思想关键词**: 中文/方言 (自动方言识别)、云+端、热词定制、移动 SDK (内置 UI)、工业落地、长音频转写
- **voice_samples**: ⚠️ 暂未找到一手 ≥30 字原话（公开发声多在公众号/媒体，本 track 黑名单）。vendor docs 能力（转述）：讯飞 ASR 提供云端多格式转写（mp3/wav/...，≤500MB/5h）、自动方言识别、自动标点、热词配置 (source: T01-S033, vendor docs)
- **sub_skill_candidate**: `false` —— 厂商，非个人思想 figure；"中文云 API 老牌派"坐标进 Phase 2。
- **最近 12 个月动态**: ⚠️ 一手溯源受限（多数动态在黑名单平台）；产品线持续与星火大模型整合。
- **争议 / 批评**: 闭源、价格与离线能力对成本/隐私敏感场景不如开源 FunASR/whisper.cpp；海外可用性与英文表现弱；一手公开技术发声集中在黑名单平台，可调研性差。
- **来源**:
  - [Surrogate/vendor] 讯飞 ASR SDK 文档: T01-S033
- **可信度自评**: low —— 仅 vendor docs 一手，个人 figure 维度几乎为空，**主要价值是标注"中文老牌云 API"坐标**。

---

## Phase 2 提炼提示

**反复出现 ≥ 3 个 figures 都谈到的关键词**（候选行业心智模型）:
- **延迟硬门槛 (latency)**：实时语音的体验阈值 —— Stephenson "<500ms" / Warden "2 秒延迟 = 不可用" / Kenarsari "零延迟" / Deepgram Flux "human-like timing" (figures: Stephenson, Warden, Kenarsari, Fox)
- **端侧 vs 云的根本权衡**：隐私/离线/成本/无网 —— Gerganov / Warden / Kenarsari / Hannun vs Stephenson / Fox / Seed / 讯飞 (几乎全员)
- **模型大小/内存即成本**：Warden "30MB RAM 是 MCU 死线" / Kenarsari "20MB 足够" / Gerganov 量化 / Klein INT8 (figures: Warden, Kenarsari, Gerganov, Klein)
- **准确率×速度×成本 三角**：Stephenson 明确三要素 / VB 的 WER×RTFx 评测 / Picovoice WER 对比 (figures: Stephenson, Srivastav, Kenarsari)
- **量化/工程化加速**：whisper.cpp ggml / faster-whisper CT2 INT8 / MLX / distil (figures: Gerganov, Klein, Hannun)
- **可复现 benchmark 选型**：WER + RTFx，跨语言/长音频 (figures: Srivastav；Kenarsari/NVIDIA 引用榜单)

**显著分歧 / 流派分裂**（本 track 最大价值 = 立场坐标系）:
- **端侧免费/自托管派**（Gerganov, Warden, Hannun, Kenarsari*, FunASR/SenseVoice, Klein）vs **云 API 派**（Stephenson/Deepgram, Fox/AssemblyAI, Seed/火山, 讯飞）
  - *Kenarsari 是"端侧但商业闭源"，独占一格：端侧 ≠ 免费
- **通用大模型 ASR 派**（Whisper/Radford 谱系，whisper.cpp 继承）vs **专用流式派**（Povey k2/RNN-T/CTC, NVIDIA NeMo Parakeet RNN-T/TDT, Deepgram 自建流式）
- **开源派**（Gerganov, Povey, FunASR, NeMo*, faster-whisper, HF/VB）vs **闭源商业 API 派**（Deepgram, AssemblyAI, Picovoice, 讯飞, 火山）
  - *NeMo 开源模型但绑 NVIDIA 生态
- **英文/多语优先**（Whisper, Moonshine, NeMo Canary, Open ASR Leaderboard）vs **中文/方言专用**（FunASR/Paraformer/SenseVoice, Seed-ASR, 讯飞）
- **LLM-based ASR**（Seed-ASR, AssemblyAI speech-LM）vs **传统 e2e**（Paraformer NAR, RNN-T, Conformer）—— 离线上下文增强 vs 实时流式

**冷僻领域信号**:
- 总 figure 数 = 14（其中真正"个人 figure"约 7-8：Gerganov / Warden / Povey / Hannun / Srivastav / Kenarsari / Stephenson / Fox；其余 4-6 为团队/厂商署名：FunASR 团队、NeMo 团队、Seed 团队、讯飞、Klein 偏工具维护者、Radford 偏纯学术）→ **个人 figure 略高于 10 阈值但偏薄**
- 多数 figure 长访谈材料 **< 30 min** 或根本没有（Povey / Radford / Klein / 三个中国团队 / NeMo 几乎无个人长访谈）→ **是**，约 50-60% figures voice 材料薄
- 标 "可信度 low" 的 figure：Radford(作为 figure)、讯飞 ≈ 2/14 ≈ 14%（未超 30%，但 medium 偏多）
- **结论 → Phase 2.8 诚实边界应明说**：figures 维度**中等偏薄**，"思想领袖"少，多数为开源维护者/厂商技术负责人；本 track 的可靠贡献是**立场光谱坐标**（端侧免费 vs 云 API vs 中文专用 vs 通用大模型 vs 专用流式），而非个人思想体系。**Phase 2 权重应压向 tools(02) / canon(04) / workflows(03)**，figures 仅作立场锚点。voice DNA 主要来自 Warden / Gerganov / Stephenson / Kenarsari 四人（有可引原话），其余以转述为主。

---

## 自检

- [x] 候选 ~20 个 → 保留 14（个人 figure 约 7-8，团队/厂商 6）—— 略高于 10，标"中等偏薄"
- [x] 每位 figure ≥ 3 条来源？—— 多数达标；Radford(1)、讯飞(1)、Klein/NeMo/Seed(2) 已诚实标注稀薄
- [x] 一手 (verified_primary) 占比 ≥ 50%？—— 34 源中 verified_primary 约 20 个 ≈ 59%（repo/arxiv/HF/scholar/官方 eng blog）
- [x] 无黑名单来源？—— 是（知乎/公众号/百度百科/CSDN/简书/掘金 全部排除；中国厂商仅用 vendor docs 一手）
- [x] "最近 12 个月动态" 填了 ≥ 80%？—— 是（仅讯飞标注溯源受限）
- [x] Phase 2 接口（关键词 + 分歧 + 冷僻信号）？—— 是
- [x] 可信度自评每位都给 + low 有理由？—— 是
