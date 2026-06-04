# Track 06 — Glossary + 成本对照矩阵 + 流派分歧：语音转文字 / ASR 应用工程

> Research date: 2026-06-04 · Locale: zh-CN（canon 全球）· Profile: practitioner（移动端 / 快速 / 低成本）
> 本 track 三大硬交付：(1) **bilingual 术语表 ≥25**（短定义 + 出处 + 外行易错）；(2) **成本对照矩阵**（云 API vs 端侧/自托管，海外 vs 中国，本行业最实用）；(3) **流派分歧矩阵**（端侧 vs 云 / 准确率 vs 成本 vs 延迟 不可能三角 —— 本行业核心分歧）。
> SEED 复用 Wave-1：T02（tools/定价主源）、T04（canon/指标）、T01（figures/立场）。新源主攻术语精确定义 + break-even 经济性 + 流式/批量准确率权衡。

---

## Source Manifest

> 新增 T06 源 18 个（术语精确定义 / break-even / 流式-批量权衡 / 幻觉实证）。跨轨复用 ID（T01/T02/T04）在 evidence 中直接出现，不重复登记。bucket 由 `source_verifier.py classify` 给出；vendor blog/docs 按 Surrogate Policy 标注（note 注明），bucket 取 verifier 自动结果。

| source_id | url | bucket | last_checked | author/host | one-line note |
|-----------|-----|--------|--------------|-------------|---------------|
| T06-S001 | https://huggingface.co/learn/audio-course/en/chapter5/evaluation | verified_primary | 2026-06-04 | Hugging Face Audio Course | WER/CER/RTFx 公式+S/D/I 定义，教学一手 |
| T06-S002 | https://openvoice-tech.net/index.php/Real-time-factor | secondary | 2026-06-04 | Open Voice Tech Wiki | RTF=f(d)/d 定义，RTF vs 延迟区分 |
| T06-S003 | https://www.emergentmind.com/topics/inverse-real-time-factor-rtfx | secondary | 2026-06-04 | Emergent Mind | RTFx 定义 + "RTFx≠延迟/内存" 限制 |
| T06-S004 | https://arxiv.org/abs/2402.08021 | verified_primary | 2026-06-04 | Koenecke et al (FAccT'24) | Careless Whisper — 幻觉实证 1.4%/38% 有害 |
| T06-S005 | https://arxiv.org/abs/2501.11378 | verified_primary | 2026-06-04 | (arXiv) | 非语音音频诱发 Whisper 幻觉调查 |
| T06-S006 | https://arxiv.org/abs/2505.12969 | verified_primary | 2026-06-04 | (arXiv) | Calm-Whisper — 抑制非语音段幻觉 |
| T06-S007 | https://www.science.org/content/article/ai-transcription-tools-hallucinate-too | verified_primary | 2026-06-04 | Science/AAAS | 幻觉新闻：静音触发、医疗场景风险 |
| T06-S008 | https://arxiv.org/html/2505.17070v1 | verified_primary | 2026-06-04 | (arXiv) | 端点检测(endpointing) 改进，定义来源 |
| T06-S009 | https://apxml.com/courses/speech-recognition-synthesis-asr-tts/chapter-6-optimization-deployment-toolkits/streaming-asr-deployment | secondary | 2026-06-04 | APXML course | 流式部署：endpointing/VAD 教学定义 |
| T06-S010 | https://k2-fsa.github.io/sherpa/onnx/hotwords/index.html | secondary | 2026-06-04 | k2-fsa sherpa docs | 热词(contextual biasing) 一手实现文档 |
| T06-S011 | https://arxiv.org/abs/2512.21828 | verified_primary | 2026-06-04 | (arXiv) | LLM-ASR 热词检索+RL 偏置（新方法） |
| T06-S012 | https://github.com/ggml-org/llama.cpp/blob/master/tools/quantize/README.md | verified_primary | 2026-06-04 | ggml-org | ggml/gguf 量化类型 Q4_0/Q8_0/K-quant 一手 |
| T06-S013 | https://www.assemblyai.com/blog/self-hosting-whisper | verified_primary | 2026-06-04 | AssemblyAI (vendor blog) | 自托管 Whisper break-even ≈500hr/月 |
| T06-S014 | https://nikolas.blog/whisper-api-vs-self-hosting/ | secondary | 2026-06-04 | Nikolas blog | T4 $0.35/hr GPU 自托管 vs API 实测 |
| T06-S015 | https://huggingface.co/blog/nvidia/nemotron-speech-asr-scaling-voice-agents | verified_primary | 2026-06-04 | NVIDIA (HF blog) | 流式 lookahead 动态权衡，0.21% WER gap |
| T06-S016 | https://www.assemblyai.com/blog/speaker-diarization-vs-recognition | verified_primary | 2026-06-04 | AssemblyAI (vendor blog) | diarization vs recognition 区分 |
| T06-S017 | https://brasstranscripts.com/blog/deepgram-pricing-per-minute-2025-real-time-vs-batch | secondary | 2026-06-04 | Brass Transcripts | Deepgram Nova-3 批量$0.258/流式$0.462/hr 复核 |
| T06-S018 | https://smallest.ai/blog/how-to-evaluate-asr-in-2026 | secondary | 2026-06-04 | Smallest.ai | ASR 评测三维(准确/延迟/成本) 框架 |

> **黑名单核查**：18 个新源全部跑过 `source_verifier.py classify`，无 `blacklisted`（知乎/公众号/百度百科/CSDN/简书/掘金；G2/Capterra 均未收录，命中即丢）。`openvoice-tech.net` / `emergentmind.com` / `apxml.com` / `k2-fsa.github.io` / `nikolas.blog` / `brasstranscripts.com` / `smallest.ai` 被 verifier 判 `secondary`（unknown host），内容用于术语佐证 / 价格复核，已标二手。AssemblyAI/Dialpad `/blog` 路径 verifier 自动判 `verified_primary`（brand-domain content path），但属 vendor blog，note 已注明，mental-model claim 不单靠其一面之词。

---

## Part 1 — 术语表（Bilingual Glossary，30 条）

> 每条：Type / Tier / 双语定义 / 来源 / **外行易错(outsider-tell)**。本行业是**技术类**：术语+缩写多，正式 standard/regulation/certification **几乎空白**（ASR 无行业准入认证、无强制法规，仅隐私法规如 GDPR/个保法间接相关——见 Part 5 标 N/A）。

### 总览（按 Tier 分组）

#### Tier 1 — 核心必懂（19 个）

| 术语 | Type | Insider def（一句） | 外行易错 |
|------|------|--------------------|----------|
| WER | acronym | 词错率 (S+D+I)/N | 跨数据集比大小；当成"准确率=1-WER"（可>100%）|
| CER | acronym | 字错率，中文/无词界语言用 | 拿中文 CER 和英文 WER 比高低 |
| RTF | acronym | 实时率=处理时长/音频时长，<1 才实时 | 把 RTF 当延迟 |
| RTFx | acronym | 实时倍数=1/RTF，越大越快 | 把 RTFx 当延迟/当实时性 |
| 延迟 latency | term | 最后一块音频到出字的时延 | 与 RTFx 混为一谈 |
| 流式 streaming | term | 边说边出字，低延迟 | 以为流式=批量同准确率 |
| 非流式 offline/batch | term | 整段音频后出，准确率高 | 以为离线就是"端侧" |
| VAD | acronym | 语音活动检测，裁静音 | 与 endpointing 划等号 |
| endpointing | term | 判断"说完了"的收尾时机 | 等同 VAD（VAD 是其手段之一）|
| diarization | term | 说话人分离"谁在何时说" | 与"声纹识别(认人)"混 |
| 端侧 on-device | term | 模型跑在手机/边缘，离线 | 以为端侧一定免费（Picovoice 闭源收费）|
| 量化 quantization | term | 权重降精度(int8/4bit)省内存提速 | 以为量化必掉准确率（Q8 近无损）|
| Whisper | term | OpenAI 开源通用 ASR 事实标准 | 以为 Whisper 能流式/实时 |
| CTC | acronym | 无对齐序列标注+blank，解码极快 | 以为 CTC 是模型（它是损失/解码法）|
| RNN-T | acronym | 流式转导主导架构 | 以为所有端到端都能流式 |
| Conformer | term | CNN+attention 主力编码器 | — |
| 热词/biasing | term | 偏置专名/术语提升识别 | 以为换模型就能修专名错 |
| 幻觉 hallucination | term | 模型编造没说过的话 | 把幻觉当"识别错"（是无中生有）|
| 自托管 break-even | term | 量超阈值则自建比云便宜 | 以为云一定贵/端侧一定省 |

#### Tier 2 — 周边熟知（11 个）

| 术语 | Type | Insider def（一句） | 来源 |
|------|------|--------------------|------|
| TDT | acronym | token+时长转导器，跳帧极快 | T04-S025 |
| NAR 非自回归 | term | 并行出 token，>10x 提速 | T04-S007 |
| beam search | term | 解码保留 top-k 路径，宽则准但慢 | T04-S006 |
| ITN 逆文本规整 | acronym | "一百二"→120、口语→书面 | T04-S020 |
| 标点恢复 | term | 无标点流→带标点 | T04-S020 |
| ggml / gguf | term | Gerganov 张量库 / 单文件量化模型格式 | T06-S012 |
| 蒸馏 distillation | term | 大模型教小模型(distil-whisper) | T04-S010 |
| 弱监督 weak supervision | term | 海量带噪转录做监督(Whisper) | T04-S001 |
| 自监督预训练 | term | 无标注音频学表征(wav2vec2) | T04-S003 |
| 时间戳 timestamps | term | 词/段级 start-end | T04-S025 |
| SDK 包体 footprint | term | 端侧库/模型体积(MB) | T02-S013 |

---

### 术语详卡

#### 1. WER (Word Error Rate) — 词错率
- **Type**: acronym · **Tier**: tier-1
- **Insider def**: `WER = (S + D + I) / N`（替换+删除+插入 ÷ 参考词数），源自 Levenshtein 编辑距离；**lower is better**，0=完美 (evidence: [T06-S001, T04-S017])。
- **Outsider def**: 转写错了多少词的比例。
- **外行易错**（`usage_tell`+`semantic_tell`）:
  - ① **WER 无上限、可 >100%**：预测 10 词、参考 2 词且全错 → WER=500%。把 WER 当"1-准确率"是错的 (evidence: [T06-S001])。
  - ② **拼写敏感**："sit" vs "sat" 整词判错，一个字母也算一个 substitution (evidence: [T06-S001])。
  - ③ **跨数据集比 WER 无意义**：LibriSpeech-clean(~2-3%) 与真实噪声(~15-18%) 差一个数量级 (evidence: [T04-S030, T06-S001])。
- **关联**: CER / RTFx / 厂商自报 WER 陷阱
- **可信度 high / Decay low**

#### 2. CER (Character Error Rate) — 字错率
- **Type**: acronym · **Tier**: tier-1
- **Insider def**: 字符级 (S+D+I)/N，**中文/日文等无词界语言的标准指标**（AISHELL 用 CER）(evidence: [T04-S015, T06-S001])。
- **外行易错**: **拿中文 CER 和英文 WER 直接比高低**——两套口径，FireRedASR 中文 CER 0.55% 不能与英文 WER 5% 比"谁更准" (evidence: [T04-S015, T02-S012])。
- **可信度 high / Decay low**

#### 3. RTF (Real-Time Factor) — 实时率
- **Type**: acronym · **Tier**: tier-1
- **Insider def**: `RTF = 处理时长 / 音频时长`（=f(d)/d）；**RTF<1 才能实时**，云服务通常 0.2–0.6，RTF=4 表示比音频慢 4 倍 (evidence: [T06-S002])。
- **外行易错**（`semantic_tell`）: **把 RTF 当延迟**。RTF 是吞吐比率（与音频长度无关的归一化值），latency 是绝对时延（依赖具体时长）；批量处理 RTF 很好但延迟可能很差 (evidence: [T06-S002, T06-S003])。
- **可信度 high / Decay low**

#### 4. RTFx (Inverse Real-Time Factor) — 实时倍数
- **Type**: acronym · **Tier**: tier-1
- **Insider def**: `RTFx = 音频时长 / 处理时长 = 1/RTF`；榜单用（**higher is better**，易读相对加速）；Parakeet-TDT 达 3386x（1 小时音频约 1 秒转完）(evidence: [T06-S001, T04-S025])。
- **外行易错**（`semantic_tell`）: **把 RTFx 当延迟或实时性**。RTFx **不反映**流式延迟、内存占用、准确率；**批量(batch128)会通过摊薄固定开销人为抬高 RTFx**，对延迟敏感的流式场景不适用 (evidence: [T06-S003, T06-S001])。RTFx 还**强依赖硬件/batch size**，跨设备不可移植 (evidence: [T06-S003])。
- **可信度 high / Decay low**

#### 5. 延迟 (Latency)
- **Type**: term · **Tier**: tier-1
- **Insider def**: 最后一块音频可用到收到推断文本之间的时延；流式 ASR 的核心体验指标（Deepgram 主张 <500ms、Warden 称 2 秒=不可用）(evidence: [T06-S003, T01-S025, T01-S004])。
- **外行易错**: **把延迟和 RTFx/RTF 混用**。一个 RTFx=3000 的批量模型延迟可能是几十秒（要等整段）；流式低延迟模型 RTFx 反而不高 (evidence: [T06-S003, T06-S015])。
- **可信度 high / Decay low**

#### 6. 流式 vs 7. 非流式 (Streaming vs Offline/Batch)
- **Type**: term · **Tier**: tier-1
- **Insider def**: **流式**=边说边增量出字（RNN-T/CTC，亚 200ms 首字延迟）；**非流式/批量**=整段后出（Whisper enc-dec，双向上下文、准确率更高）(evidence: [T06-S015, T04-S005, T04-S001])。
- **外行易错**（`usage_tell`，本行业高频破绽）:
  - ① **以为"流式≠批量"准确率相同**：流式**看不到未来音频帧（无 lookahead）**，是准确率掉点的根因；研究显示 0.56s 延迟 + 5.6s 历史可把差距压到仅 **0.21% WER** 高于批量基线，但不为零 (evidence: [T06-S015])。
  - ② **把"离线(offline/batch)"等同"端侧(on-device)"**：offline 指非实时整段处理（可在云上），on-device 指模型跑在本机——两个维度 (evidence: [T04-S001])。
- **可信度 high / Decay low**

#### 8. VAD (Voice Activity Detection) — 语音活动检测
- **Type**: acronym · **Tier**: tier-1
- **Insider def**: 检测哪段有人声 → **裁掉静音**：省算力、省按时长计费的成本、做分块。Silero VAD <1ms/chunk、2MB 是事实标准 (evidence: [T04-S021])。
- **外行易错**: **VAD = endpointing**。VAD 是帧级"有没有人声"的分类器；endpointing 是据此判"说完了"的决策（含最小/最大停顿守卫）。VAD 是 endpointing 的手段之一，不是同义词 (evidence: [T06-S008, T06-S009])。
- **可信度 high / Decay low**

#### 9. Endpointing — 端点检测/收尾判定
- **Type**: term · **Tier**: tier-1
- **Insider def**: 判断用户"说完了一句"的时机，决定何时结束本次识别。没有它，流式系统会无限等待（长延迟）、空转处理静音（浪费算力）、或过早截断（漏字）(evidence: [T06-S008, T06-S009])。
- **外行易错**: 与 VAD 混用；以为是模型自带——常需独立 VAD/端点模型或多任务架构 (evidence: [T06-S008])。
- **可信度 high / Decay low**

#### 10. Diarization — 说话人分离
- **Type**: term · **Tier**: tier-1
- **Insider def**: 把音频按说话人切分，回答"**谁在何时说(who spoke when)**"，**无需事先知道说话人身份**；pyannote.audio 开源事实标准，常与 Whisper 拼成带说话人转写(whisperX)(evidence: [T06-S016, T04-S022])。
- **外行易错**（`semantic_tell`）: **把 diarization(分离"说话人A/B")和 speaker recognition/identification(认出"这是张三")混为一谈**——前者不认身份只分组，后者要匹配已知声纹 (evidence: [T06-S016])。也常误以为 ASR 自带分离（多数要外挂）。
- **可信度 high / Decay low**

#### 11. 端侧 (On-Device)
- **Type**: term · **Tier**: tier-1
- **Insider def**: 模型跑在手机/边缘（whisper.cpp+CoreML/Metal、Moonshine、sherpa-onnx）：离线、隐私、零云边际成本 (evidence: [T04-S018, T04-S009])。
- **外行易错**（`semantic_tell`）: **以为"端侧"="免费"**。whisper.cpp/Apple/SenseVoice/Vosk 端侧免费，但 **Picovoice 是端侧却闭源收费**（端侧≠免费，是两个维度）(evidence: [T02-S031, T01-S030])。也常误以为端侧=低准确率（whisper.cpp 跑 large 同精度）(evidence: [T02-S005])。
- **可信度 high / Decay low**

#### 12. 量化 (Quantization, int8/4bit)
- **Type**: term · **Tier**: tier-1
- **Insider def**: 把权重从 fp16/32 降到 int8/4bit，省内存提速；faster-whisper int8 显存 2926 vs fp16 4708MB (evidence: [T04-S019, T02-S004])。
- **外行易错**: **以为量化必然明显掉准确率**。**Q8_0（8bit）近乎无损**（每 32 值一块一个 scale），K-quant 在低 bit 下也尽量保质；端侧标配 (evidence: [T06-S012])。
- **关联**: ggml/gguf
- **可信度 high / Decay low**

#### 13. Whisper
- **Type**: term · **Tier**: tier-1
- **Insider def**: OpenAI 680k 小时弱监督 enc-dec Transformer，99 语言、零样本鲁棒，**开源应用层默认基线**，衍生整条端侧生态 (evidence: [T04-S001, T02-S003])。
- **外行易错**（`usage_tell`）: **以为 Whisper 能流式/实时**——它是 30s 窗口非流式 enc-dec，低延迟要 RNN-T/Parakeet/Deepgram；长音频/静音**易幻觉** (evidence: [T04-S001, T06-S004])。
- **可信度 high / Decay low**

#### 14. CTC (Connectionist Temporal Classification)
- **Type**: acronym · **Tier**: tier-1
- **Insider def**: 无需逐帧对齐的序列标注，引入 **blank token** 折叠重复帧；解码无自回归、极快，速度/流式派根基 (evidence: [T04-S004])。
- **外行易错**: **以为 CTC 是一种模型**——它是损失函数/解码范式，可装在不同 encoder（Conformer 等）上 (evidence: [T04-S004])。
- **可信度 high / Decay low**

#### 15. RNN-T (RNN-Transducer)
- **Type**: acronym · **Tier**: tier-1
- **Insider def**: encoder+prediction+joint 三网络，天然流式增量解码，**设备端流式 ASR 主导架构**（Google/Apple 听写）(evidence: [T04-S005])。
- **外行易错**: **以为所有"端到端"模型都能流式**——Whisper(enc-dec) 是端到端但非流式；流式要 RNN-T/CTC 这类 (evidence: [T04-S005, T04-S001])。
- **可信度 high / Decay low**

#### 16. Conformer
- **Type**: term · **Tier**: tier-1
- **Insider def**: CNN(局部)+self-attention(全局) 的 ASR 主力编码器；现代高准确率系统(Parakeet/Canary/zipformer)的 encoder，"Conformer 系"≈准确率天花板 (evidence: [T04-S002, T04-S012])。
- **外行易错**（`pronunciation_tell`）: 读 "con-FOR-mer"，是 Convolution-augmented Transformer 合成词，非 "conformer(顺从者)" 含义。
- **可信度 high / Decay low**

#### 17. 热词 / Biasing (Contextual Biasing / Hotwords)
- **Type**: term · **Tier**: tier-1
- **Insider def**: 给定专名/术语表，**偏置解码**让稀有词（人名/品牌/行话）更易被正确识别（shallow fusion 建 n-gram FST 在 beam search 中加分），缓解长尾词问题 (evidence: [T06-S010, T04-S020])。
- **外行易错**（`usage_tell`）: **以为专名识别错只能靠"换更强模型"**——实际**热词/biasing 是更便宜直接的修法**；通用模型对训练集没见过的专名天生差，再大也救不了，要靠 biasing/热词表 (evidence: [T06-S010, T06-S011, T04-S020])。
- **可信度 high / Decay low**

#### 18. 幻觉 (Hallucination)
- **Type**: term · **Tier**: tier-1
- **Insider def**: ASR（尤其 Whisper 类 enc-dec 在长音频/**静音段/非语音音频**）**编造根本没说过的话** (evidence: [T06-S004, T06-S005, T04-S001])。
- **外行易错**（`semantic_tell`，安全关键）:
  - ① **把幻觉当"识别错"**——它是**无中生有**（凭空多出整句），不是把 A 听成 B。**静音/停顿直接触发**幻觉，而停顿是人类对话常态 (evidence: [T06-S007, T06-S005])。
  - ② **低估其危害**：Careless Whisper 实证约 **1.4% 转写含幻觉**，其中 **38% 含显式有害内容**（暴力/虚构关联/伪造权威）；医疗转写场景已发现编造病人从未说过的话 (evidence: [T06-S004, T06-S007])。缓解：VAD 裁静音/分段、换 distil-whisper（更少幻觉）、或 Calm-Whisper 类方法 (evidence: [T04-S010, T06-S006])。
- **可信度 high / Decay low**

#### 19. 自托管 break-even（量本盈亏平衡）
- **Type**: term · **Tier**: tier-1
- **Insider def**: 转写量超过某阈值时，自托管开源(faster-whisper/whisper.cpp)的边际成本低于云 API 按分钟计费 → 该自建。实测阈值 **≈500 小时/月**（T4 GPU 实例约 $276/月 + DevOps $50–200/月）(evidence: [T06-S013, T06-S014, T04-S019])。
- **外行易错**（`usage_tell`）:
  - ① **以为云一定贵**——量小时云 API（无固定成本）更划算；**80% 场景 OpenAI API 更省事**，尤其请求量波动大时 (evidence: [T06-S013, T06-S014])。
  - ② **忽略"VM 时长 vs 音频时长"**：自托管按**实例运行分钟**计费，不是音频分钟；一段音频跑 12.7 分钟实例≠音频时长，闲置也烧钱 (evidence: [T06-S014])。
- **可信度 high / Decay medium**（GPU 价格随市场变）

#### 20. TDT (Token-and-Duration Transducer)
- **Type**: acronym · **Tier**: tier-2
- **Insider def**: RNN-T 提速变体，同时预测 token 和其时长、跳过冗余帧 → 极高 RTFx（Parakeet-TDT 用它）(evidence: [T04-S025])。
- **外行易错**: 与普通 RNN-T 混；以为只是"更快"而无架构差异。
- **可信度 high / Decay low**

#### 21. 非自回归 NAR (Non-Autoregressive)
- **Type**: term · **Tier**: tier-2
- **Insider def**: 并行一步出所有 token（Paraformer），不逐字生成 → >10x 提速，成本/速度派代表 (evidence: [T04-S007])。
- **外行易错**: **以为 NAR 一定不如 AR 准**——Paraformer 在 AISHELL 达 AR-SOTA 同档准确率 (evidence: [T04-S007])。
- **可信度 high / Decay low**

#### 22. Beam Search — 束搜索
- **Type**: term · **Tier**: tier-2
- **Insider def**: 解码时保留 top-k 候选路径搜最优转写；beam 越宽越准但越慢（速度↔准确率旋钮）(evidence: [T04-S006])。
- **外行易错**: 以为 beam 越大越好——边际收益递减且拖慢。
- **可信度 high / Decay low**

#### 23. ITN (Inverse Text Normalization) — 逆文本规整
- **Type**: acronym · **Tier**: tier-2
- **Insider def**: 把口语规整成书面：「一百二十三」→「123」、「百分之五」→「5%」、日期/货币格式化 (evidence: [T04-S020])。
- **外行易错**: **把 ITN 和"标点恢复"混为一谈**（两件事：ITN 管数字/格式，标点恢复管逗号句号）(evidence: [T04-S020])。
- **可信度 high / Decay low**

#### 24. 标点恢复 (Punctuation Restoration)
- **Type**: term · **Tier**: tier-2
- **Insider def**: ASR 原始输出常无标点 → 后处理模型补逗号句号（FunASR 用 CT-Transformer）(evidence: [T04-S020])。
- **可信度 high / Decay low**

#### 25. ggml / gguf
- **Type**: term · **Tier**: tier-2
- **Insider def**: **ggml** = Gerganov 的 C/C++ 最小张量库（CPU/Apple Silicon 推理基石）；**gguf**(Georgi Gerganov Universal Format) = 把架构+tokenizer+量化参数+权重打包进**单个可移植文件**的二进制格式，支持 memory-mapped 零拷贝加载；whisper.cpp/llama.cpp 共用此生态 (evidence: [T06-S012, T04-S018])。
- **外行易错**（`pronunciation_tell`+`usage_tell`）: 把 ggml 和 gguf 当同一个东西——gguf 是 ggml 的**后继文件格式**（ggml 是库/旧格式，gguf 是新格式）。Q4_0/Q5_0/Q8_0 是量化类型，不是模型名 (evidence: [T06-S012])。
- **可信度 high / Decay low**

#### 26. 蒸馏 (Knowledge Distillation)
- **Type**: term · **Tier**: tier-2
- **Insider def**: 大模型(teacher)教小模型(student)；distil-whisper 5.8x 快、少 51% 参数、OOD <1% WER 差，且**更少幻觉** (evidence: [T04-S010])。
- **外行易错**: 把"蒸馏(distil)"和"量化(quant)"混——前者改模型结构/参数量，后者只降权重精度 (evidence: [T04-S010, T06-S012])。
- **可信度 high / Decay low**

#### 27. 弱监督 (Weak Supervision)
- **Type**: term · **Tier**: tier-2
- **Insider def**: 用海量带噪互联网转录做监督（Whisper 680k 小时），换鲁棒性与零样本 (evidence: [T04-S001])。
- **外行易错**: 与"自监督"混——弱监督有(带噪)标签，自监督无标签 (evidence: [T04-S001, T04-S003])。
- **可信度 high / Decay low**

#### 28. 自监督预训练 (Self-Supervised Pretraining)
- **Type**: term · **Tier**: tier-2
- **Insider def**: 无标注音频上 mask+对比学习学表征（wav2vec 2.0），解锁低资源/小语种（10 分钟标注即可微调）(evidence: [T04-S003])。
- **可信度 high / Decay low**

#### 29. 时间戳 (Timestamps)
- **Type**: term · **Tier**: tier-2
- **Insider def**: 词级/段级 start-end 时间，用于字幕对齐、检索、diarization 拼接 (evidence: [T04-S025, T04-S001])。
- **外行易错**: 以为所有模型时间戳都精确——Whisper 段级时间戳粗、词级需额外对齐(whisperX)。
- **可信度 high / Decay low**

#### 30. SDK 包体 / Footprint
- **Type**: term · **Tier**: tier-2
- **Insider def**: 端侧库+模型在 App 里占的体积(MB)，移动端关键约束；Picovoice <40MB、Vosk 小模型 50MB、Whisper-large 1.5GB (evidence: [T02-S013, T02-S016])。
- **外行易错**（`semantic_tell`）: 只看模型参数量不看**实际包体+运行内存**；Warden 强调"30MB RAM 是 MCU 死线"，Kenarsari "20MB 足够"——端侧成本=包体+内存 (evidence: [T01-S004, T01-S030])。
- **可信度 high / Decay low**

---

## Part 2 — 成本对照矩阵（本行业最实用，"成本尽量低"硬交付）

> **比价口径**：统一到 USD/hr（中国厂商并列￥/hr，按 ~￥7.1/$ 估算）。区分**云 API(按量付费)** vs **端侧/自托管**；**海外 vs 中国**；**批量 vs 流式**。云价为 list price(PAYG)，未含量级折扣。**端侧标"免费/边际≈0"，自托管标 GPU 实例成本**。

### 2.1 一张可比总表（按"每小时音频成本"升序）

| 方案 | 类型 | 成本/hr(音频) | 流式? | 中文 | 隐私/离线 | 适用量级 | evidence |
|---|---|---|---|---|---|---|---|
| **端侧免费**（whisper.cpp/Apple/SenseVoice/Vosk/Moonshine）| on-device 开源 | **$0 边际**（仅设备电费）| 部分(Vosk/Moonshine/Picovoice 流式)| 强(SenseVoice)| **最佳** | 任意（移动端首选）| T02-S005,T02-S019,T02-S009 |
| **自托管开源**（faster-whisper int8 / Parakeet / FunASR）| 自建 GPU | **~$0.10–0.20/hr**（T4 $0.35/hr 摊到数百 RTFx；break-even ≈500hr/月）| 看模型 | 强(FunASR)| 高(数据不出域)| **大量(>500hr/月)** | T06-S013,T06-S014,T02-S004 |
| **腾讯云 录音文件(30万hr包)** | 中国云批量 | **￥0.7≈$0.10** | 否 | 原生 | 否 | 大量中文 | T02-S027 |
| **阿里云 ISI 录音(25万hr包)** | 中国云批量 | **￥0.8≈$0.11** | 否 | 原生 | 否 | 大量中文 | T02-S028 |
| **火山/腾讯/阿里 流式(50万hr包)** | 中国云流式 | **￥1.0≈$0.14** | 是 | 原生 | 否 | 大量中文实时 | T02-S029,T02-S027 |
| **AssemblyAI Universal-2** | 海外云批量+流式 | **$0.15** | 是 | 100+语言 | 否 | 中小量(便宜)| T02-S022 |
| **OpenAI gpt-4o-mini-transcribe** | 海外云 | **$0.18** | 是 | 多语种 | 否 | 验证/省事接入 | T02-S026 |
| **Azure Speech 批量** | 海外云批量 | **$0.18** | — | 支持 | 容器版 | 已在 Azure 生态 | T02-S024 |
| **Deepgram Nova-3 批量** | 海外云批量 | **$0.258**（按秒计无 idle 坑）| — | 45+语言 | **可 self-host** | 流式强/中量 | T02-S020,T06-S017 |
| **Deepgram Nova-3 流式** | 海外云流式 | **$0.29–0.462** | 是 | 45+语言 | 可 self-host | 实时(海外首选)| T02-S020,T06-S017 |
| **OpenAI gpt-4o-transcribe / whisper-1** | 海外云 | **$0.36** | mini 才流式 | 多语/99语 | 否 | 省事高精 | T02-S026 |
| **AssemblyAI U-3 Pro 流式** | 海外云流式 | **$0.45** | 是 | 100+语言 | 否 | 高精流式 | T02-S022 |
| **Google Cloud STT(Chirp)** | 海外云 | **~$0.24（量大）→$0.96** | 是 | 支持 | on-prem 另计 | 已在 GCP 生态 | T02-S023 |
| **Azure Speech 实时** | 海外云流式 | **$1.00** | 是 | 支持 | 容器版 | ⚠️小量勿用 | T02-S024 |
| **AWS Transcribe T1** | 海外云 | **$1.44**（T4 5M+min 降$0.47）| 是 | 支持 | 否 | ⚠️小量最贵 | T02-S025 |
| **Picovoice Leopard/Cheetah** | 端侧商业 | 免费 100hr/月，超出付费起 ~$999 | Cheetah 流式 | 弱 | **最佳(端侧)** | 嵌入式商用 | T02-S031 |

\* Deepgram 流式 PAYG 实测 $0.0077/min=$0.462/hr、批量 $0.0043/min=$0.258/hr（按秒计、$200 免费额度）；早前 T02-S020 记单语流式 $0.29/hr 为不同档/口径，二者并存 (evidence: [T02-S020, T06-S017])。

### 2.2 "按量级选最低成本"的硬结论

| 用量场景 | 最低成本选择 | 理由 | evidence |
|---|---|---|---|
| **移动端 / 离线 / 任意量** | **端侧免费**（whisper.cpp/Apple/SenseVoice）| 边际成本归零、零服务器账单、隐私最佳 | T02-S005,T02-S019 |
| **小量(<~100hr/月)、不想运维** | **AssemblyAI $0.15/hr（批量）** 或 **OpenAI mini $0.18/hr** | 无固定成本，量小云 API 最划算（80% 场景 API 胜）| T02-S022,T06-S013 |
| **中量、要实时(海外)** | **Deepgram Nova-3 流式（按秒计、无 idle 坑）** | AssemblyAI 流式更便宜但**WebSocket idle 计费**是大坑 | T02-S020,T02-S022 |
| **大量(>~500hr/月)、有运维** | **自托管 faster-whisper/Parakeet（~$0.1–0.2/hr）** | 量大边际成本≈电费，低于任何云 API | T06-S013,T02-S004 |
| **大量中文、不想运维** | **腾讯录音 ￥0.7 / 阿里 ￥0.8/hr（大资源包）** | ≈$0.10/hr，比海外云便宜，且**只对 VAD 语音段计费** | T02-S027,T02-S028 |
| **极致省钱通用三件套** | **批量优先 + 大资源包 + VAD 裁静音** | 批量比流式便宜 40–50%；资源包腰斩；静音不付费 | T06-S017,T02-S025,T02-S028 |

**一句话总结**：**小量→端侧(免费) 或 省事档云 API($0.15–0.18/hr)；大量→批量+自托管/中国大资源包(~$0.10–0.20/hr)，break-even 约 500hr/月**。最贵踩雷：AWS T1 $1.44/hr、Azure 实时 $1.00/hr（小量级勿碰，除非已在该云生态）(evidence: [T02-S025, T02-S024])。

---

## Part 3 — 流派分歧矩阵（framework 甜区，保留分歧）

> 本行业**核心分歧 = 端侧 vs 云 / 准确率 vs 成本 vs 延迟（不可能三角）**。每轴列：各派主张 / 代表方案或人物 / 适用场景 / 核心分歧。**保留矛盾，不强行裁决**。

### 轴 1：部署形态 —— 端侧免费 vs 云 API vs 端侧商业

| 派别 | 主张 | 代表方案/人物 | 适用场景 | evidence |
|---|---|---|---|---|
| **端侧免费派** | 边际成本归零+隐私+离线，能端侧就端侧 | whisper.cpp(Gerganov)/Apple SpeechAnalyzer/SenseVoice/Vosk/Moonshine(Warden)| 移动端、隐私敏感、无网、零云成本 | T02-S005,T02-S019,T01-S004 |
| **云 API 派** | 零运维、按量付费、起步快、规模化效率 | Deepgram(Stephenson)/AssemblyAI(Fox)/OpenAI/三大云/讯飞/火山 | 量小波动大、不想运维、要 SLA/流式 | T02-S020,T02-S022,T01-S025 |
| **端侧商业派** | 端侧≠免费：闭源 SDK 换 SLA+极小包体+商用支持 | Picovoice Leopard/Cheetah(Kenarsari)| 嵌入式商用、要 SLA、<40MB | T02-S031,T01-S030 |
| **核心分歧** | **决策轴=用量规模 × 运维能力 × 隐私要求**。Kenarsari "20MB 足够、质疑云端处理简单指令"；Stephenson "实时<500ms、10x 便宜难在 scale"——端侧派与云派直接对立 | — | — | T01-S030,T01-S025 |

### 轴 2：模型范式 —— 通用大模型 vs 专用流式

| 派别 | 主张 | 代表方案/人物 | 适用场景 | evidence |
|---|---|---|---|---|
| **通用大模型派** | 弱监督大规模换鲁棒/零样本/多语，准确率高 | Whisper(Radford)/gpt-4o-transcribe/distil-whisper | 批量转写、多语、高准确（**非流式、慢、可能幻觉**）| T04-S001,T06-S004 |
| **专用流式派** | 流式转导(RNN-T/CTC/Conformer)，低延迟实时 | Parakeet/Canary(NVIDIA)/k2-icefall(Povey)/Deepgram 自建 | 实时字幕、语音输入、对话（低延迟优先）| T04-S005,T04-S025,T01-S025 |
| **中文 NAR 派** | 非自回归并行解码，同精度 >10x 提速 | Paraformer/SenseVoice(阿里 DAMO)| 中文批量/端侧、成本敏感 | T04-S007,T02-S009 |
| **核心分歧** | **速度↔准确率帕累托前沿**：Open ASR 实证 Conformer-enc+Transformer-dec 准确率最佳，但 **CTC/TDT 解码 RTFx 更高**——准确率派 vs 速度派的架构层；Whisper 的 30s 定长/幻觉正是 Moonshine/专用流式批评改进的靶子 | — | — | T04-S012,T01-S004 |

### 轴 3：开闭源 —— 闭源 API vs 开源自托管

| 派别 | 主张 | 代表方案 | 适用场景 | evidence |
|---|---|---|---|---|
| **闭源商业 API 派** | 托管+SLA+持续调优，省心 | Deepgram/AssemblyAI/Picovoice/讯飞/火山 | 量小、要 SLA、不想碰模型 | T02-S020,T02-S031 |
| **开源自托管派** | 可控+隐私+量大单位成本最低 | faster-whisper/whisper.cpp/FunASR/FireRedASR/NeMo* | 量大、数据不出域、有运维 | T02-S004,T02-S008 |
| **核心分歧** | break-even ≈500hr/月：量小闭源 API 省事更划算，量大自托管边际≈电费更省。*NeMo 模型开源但 **CC-BY-4.0 需署名**、绑 NVIDIA 生态；Whisper/faster-whisper/FunASR 才是 MIT/Apache 可放心商用（**license 是隐性分歧**）| — | T06-S013,T02-S007 |

### 轴 4：语言阵营 —— 英文优先 vs 中文 ASR

| 派别 | 主张 | 代表方案 | 适用场景 | evidence |
|---|---|---|---|---|
| **英文/多语优先派** | Open ASR Leaderboard 榜首即最优 | Parakeet/Canary(榜首但**无中文或仅25欧语**)/Whisper/Open ASR Leaderboard | 英文/欧语场景 | T02-S001,T02-S007 |
| **中文 ASR 派** | 中文/方言是另一套榜单另一套最优解 | FunASR/SenseVoice/FireRedASR/讯飞/Seed-ASR | 中文/粤语/方言场景 | T02-S011,T02-S012 |
| **核心分歧（本行业最尖锐之一）** | **两套世界、两套基准**：英文看 WER(LibriSpeech/Open ASR)、中文看 CER(AISHELL/WenetSpeech)；**Open ASR 榜首 Canary/Parakeet 英语 only，无中文**——**绝不能用英文跑分指导中文选型** | — | — | T02-S001,T04-S015,T02-S012 |

### 轴 5：优化优先级 —— 准确率派 vs 成本派 vs 延迟派（不可能三角）

| 派别 | 主张 | 代表方案/人物 | 牺牲什么 | evidence |
|---|---|---|---|---|
| **准确率派** | 错一个字代价高(医疗/金融/法务)，准确率第一 | Canary-Qwen(5.63%榜首)/FireRedASR(中文SOTA)/Deepgram Nova-3 | 牺牲速度/成本（大模型贵慢）| T02-S001,T02-S011 |
| **成本派** | 成本尽量低，达标即止 | 端侧免费/批量+大包+VAD/Paraformer 0.2B/mini-transcribe | 牺牲峰值准确率/实时性 | T02-S027,T06-S013 |
| **延迟派** | 实时体验是硬门槛(<500ms / 2s=不可用) | RNN-T/Parakeet 流式/Deepgram/Moonshine 50ms | 牺牲准确率(无 lookahead)/成本(流式更贵) | T01-S025,T01-S004,T06-S015 |
| **核心分歧（本行业第一性矛盾）** | **没有免费午餐**：准确率/速度/成本三选二。Stephenson 明确 accuracy×speed×price 三角；VB 的 WER×RTFx 评测；流式为低延迟牺牲 0.21%+ WER；NVIDIA Nemotron 主张**推理时动态选 lookahead 点**以缓解(而非训练时定死)——但权衡本身消不掉 | — | — | T01-S025,T06-S015,T06-S018 |

**最尖锐的 3 个分歧**：
1. **准确率 vs 成本 vs 延迟不可能三角**（轴 5）——全行业第一性矛盾，所有选型最终落到这里。
2. **英文优先 vs 中文 ASR 两套榜单**（轴 4）——外行最易踩，"榜首≠对你最优"，Canary/Parakeet 无中文。
3. **端侧免费 vs 云 API vs 端侧商业**（轴 1）——决定整个成本/隐私结构；"端侧≠免费"(Picovoice) 是反直觉点。

---

## Part 4 — 关键差异对照

### 4.1 端侧 vs 云（六维）

| 维度 | 端侧 on-device | 云 API |
|---|---|---|
| **成本** | 边际≈0（免费开源）或一次性 SDK 费(商业)；自托管摊 GPU | 按量付费 $0.15–1.44/hr；量大可降 | 
| **隐私** | 数据不离设备，最佳；合规友好 | 音频上云，受隐私法规约束 |
| **延迟** | 无网络往返，可极低(Moonshine 50ms)，但受设备算力限 | 含网络往返；流式可<500ms 但依赖连接 |
| **包体/内存** | 受 App 包体+RAM 限（tiny 73MB ~ large 1.5GB）；端侧死线 | 零本地占用 |
| **准确率** | 受模型大小限，但 whisper.cpp 可跑 large 同精度 | 可用最大/最新模型，峰值准确率高 |
| **离线** | 完全离线可用 | 必须联网 |
| evidence | T02-S005,T02-S019,T01-S004,T06-S012 | T02-S020,T02-S022,T06-S017 |

**裁决**（推断，跨源一致）：移动端/隐私/零边际成本 → 端侧；量小波动大/要峰值准确率/要 SLA → 云。**端侧≠免费**(Picovoice 闭源)、**端侧≠低准确率**(whisper.cpp large) 是两个常见误区 (evidence: [T02-S031, T02-S005]) `[推断]`。

### 4.2 批量 vs 流式

| 维度 | 批量(offline/pre-recorded) | 流式(streaming/real-time) |
|---|---|---|
| **何时出字** | 整段音频后一次出 | 边说边增量出 |
| **准确率** | 高（双向 lookahead 全上下文）| 略低（无未来帧；可压到 +0.21% WER）|
| **延迟** | 高（等整段）| 低（亚 200ms 首字）|
| **成本** | 便宜（同厂商比流式低 40–50%）| 贵（Azure $0.18 vs $1.00；按会话时长还可能含 idle）|
| **架构** | enc-dec(Whisper)/NAR/CTC-TDT 批 | RNN-T/CTC/Conformer 流式 |
| evidence | T06-S015,T02-S024,T04-S001 | T06-S015,T02-S022,T04-S005 |

**裁决**：不需要实时就走批量（更便宜更准）；要实时字幕/语音输入/对话才上流式，并接受准确率与成本代价 (evidence: [T06-S015, T02-S024]) `[推断]`。

### 4.3 ASR vs TTS（一句话澄清，方向相反）

- **ASR (Speech-to-Text / 语音转文字)** = 音频 → 文本（本 skill 主题）；**TTS (Text-to-Speech / 文字转语音)** = 文本 → 音频，**方向完全相反**。
- **外行易错**：把两者混为"语音 AI"或互换术语。它们是逆操作，指标(WER/CER vs MOS/自然度)、架构、厂商产品线均不同（Deepgram Aura、OpenAI TTS 是 TTS 线，不在本 skill 范围）(evidence: [T01-S025]) `[推断]`。

---

## Part 5 — Type 覆盖说明（standard/regulation/certification）

本行业是**技术类**，5 个 type 分布极不均衡：

| Type | 本行业状态 | 说明 |
|---|---|---|
| **Term / 术语** | ✅ 充足（~22）| 架构/指标/工程概念为主 |
| **Acronym / 缩写** | ✅ 充足（~8）| WER/CER/RTF/RTFx/CTC/RNN-T/TDT/NAR/ITN/VAD |
| **Standard / 标准** | ⚠️ **几乎 N/A** | ASR **无统一行业技术标准/协议**；事实标准是开源 README(whisper.cpp/FunASR) + Open ASR Leaderboard 评测口径，非正式 spec |
| **Regulation / 法规** | ⚠️ **间接 N/A** | ASR 本身**无专门准入法规**；仅**隐私法规间接相关**（GDPR/中国个保法约束音频数据处理、医疗场景 HIPAA）——属应用合规而非 ASR 技术法规 |
| **Certification / 认证** | ❌ **N/A** | **无 ASR 从业/产品认证**；能力靠 Open ASR Leaderboard 排名 + 厂商 SLA 背书，非证书 |

**诚实标注**：本行业的"标准"实质是**评测口径之争**（厂商自报 WER vs Open ASR Leaderboard 统一口径），而非传统标准化机构 spec；这本身就是 Part 3 轴 5 分歧的延伸 (evidence: [T04-S030, T04-S012])。

---

## Phase 2 提炼提示

### 「行业表达 DNA」直接素材（喂 Phase 2.5）

**高频黑话 top 10**：WER / CER / RTFx / 流式 vs 批量 / 端侧(on-device) / 量化(int8/gguf) / 热词(biasing) / 幻觉(hallucination) / VAD 裁静音 / break-even。

**行业拒绝的厂商话术 top 5**（拒绝→价值观/反模式）：
1. **厂商自报 WER**（Deepgram 5.26% / Picovoice 自家友好）—— 内行：测试集不同不可跨家比，要在自己数据上 A/B (evidence: [T04-S030, T02-S021])。
2. **"准确率第一/我们最准"**—— 内行：没有全能王，是准确率×速度×成本三角 (evidence: [T01-S025])。
3. **"端侧=免费"暗示**—— 内行：Picovoice 端侧但闭源收费 (evidence: [T02-S031])。
4. **"流式和批量一样准"**—— 内行：流式无 lookahead 必掉点 (evidence: [T06-S015])。
5. **把 RTFx 当实时性/延迟卖**—— 内行：RTFx≠延迟，批量可灌水 (evidence: [T06-S003])。

**外行破绽 top 10**（insider-only spotting tells）：
1. 把 RTF/RTFx 当延迟；2. 拿中文 CER 比英文 WER 高低；3. 以为 Whisper 能流式；4. 把幻觉当"识别错"；5. VAD=endpointing 划等号；6. 以为端侧=免费/=低准确率；7. 以为量化必掉准确率；8. 拿厂商自报 WER 跨家比；9. 用英文榜单选中文模型；10. 把 ASR 和 TTS 互换；(+ diarization 当声纹认人) (evidence: [T06-S001, T06-S003, T06-S004, T06-S015, T02-S001])。

### 「智识谱系」线索（喂 Phase 2.7）

- **范式更替路径**：CTC(2006)→RNN-T(2012)→LAS(2015)→Conformer(2020)→Whisper 通用大模型(2022)→LLM-based(Seed-ASR/2024)；同时 NAR(Paraformer/2022) 与端侧专用(Moonshine/2024) 分叉——**通用大模型 vs 专用流式**的硬件层。
- **"标准"碎片化即流派之争**：ASR **无统一 spec**，事实标准是**评测口径战争**（厂商 benchmark vs Open ASR Leaderboard），反映"准确率怎么算"本身有分歧 (evidence: [T04-S012, T04-S030])。
- **license 谱系**：MIT/Apache(Whisper/faster-whisper/FunASR) vs CC-BY-4.0 需署名(Parakeet/Canary) vs 闭源(Picovoice/Deepgram)——开源理想 vs 商业护城河之争 (evidence: [T02-S003, T02-S007, T02-S031])。

### 「时效性」信号（喂 Phase 2.8）

- **无正式法规/标准/认证**（见 Part 5），故**无法规修订型时效衰减**；衰减主要来自 **模型/榜单/价格快速迭代**（ASR 模型 6–12 月一换代：turbo/Nova-3/Parakeet-v3/FireRedASR/Moonshine v2 均 12 月内起势）。
- 预计 12 月内会变：云 API 价格（持续下行）、Open ASR Leaderboard 排名（每月滚动）、端侧新模型（Moonshine 等 experimental）。**术语本身 decay low**（核心术语 5+ 年稳定）。

### 「工作流变化触发」种子（喂 wave 3 Track 03）

- 本行业 workflow 变化触发源**不是法规**（无），而是：(1) 新模型发布（换 SOTA/换更便宜档）；(2) 云价格调整（触发 build-vs-buy 重算）；(3) break-even 阈值（量增长到 ~500hr/月触发自托管迁移）；(4) 端侧能力跃迁（iOS26 SpeechAnalyzer/Moonshine v2 触发"从云搬回端")(evidence: [T06-S013, T02-S019])。

### 冷僻 / 信号薄弱自检

- 总术语数 **30**（≥25 ✅，远超 floor 40 的术语侧——本行业术语密集）；Tier 1 **19**（≥15 ✅）；有 outsider-tell 的术语 **Tier 1 全部 + Tier 2 多数 ≈ 80%**（≥50% ✅）。
- 新增源 **18 个 T06**（目标 12–20，达标）+ 跨轨复用 T01/T02/T04 数十源；新源 bucket：verified_primary 11（arxiv/HF/github/science.org/vendor-blog）/ secondary 7（wiki/course/独立 blog/价格复核站）。
- **诚实边界**：(1) standard/regulation/certification 三 type **N/A/间接**（技术类行业特征，非数据缺漏，已在 Part 5 明说）；(2) 部分价格为 vendor pricing/第三方复核站(secondary)，中国厂商￥价 JS 渲染难直取，建议用时二次核对具体档位；(3) **自报 WER vs 第三方口径矛盾未解**（这是行业现状，SKILL.md 选型节须提醒"自有数据 A/B"）；(4) break-even ≈500hr/月 是公开 benchmark 推断值，精确点取决于 GPU 单价/并发/RTFx，标 `[推断]`。
- **结论**：glossary 维度**信号充沛**（术语密集、定义稳定、矛盾清晰），**非冷僻**。本 track 最大价值 = **成本对照矩阵（最实用硬交付）+ 五轴流派分歧（保留三大尖锐矛盾）+ 30 条带 outsider-tell 的术语**。

---

## 自检

- [x] 术语 ≥25？—— **30**（Tier1 19 + Tier2 11）✅
- [x] bilingual？—— 每条中英对照 ✅
- [x] 每条短定义 + 出处 + 外行易错？—— Tier1 全填 outsider-tell，Tier2 多数填 ✅
- [x] 成本对照矩阵（云 vs 端侧、海外 vs 中国、英 vs 中）+ 按量级最低成本结论？—— Part 2 总表 16 行 + 6 条量级结论 ✅
- [x] 流派分歧矩阵 ≥4 轴 + 保留分歧？—— **5 轴**（部署/范式/开闭源/语言/优化三角）+ 每轴标核心分歧 + 最尖锐 3 个 ✅
- [x] 关键差异：端侧vs云 / 批量vs流式 / ASR vs TTS？—— Part 4 全覆盖 ✅
- [x] Source Manifest 在最前 + T06-Sxxx 格式 + 跨轨复用 evidence？—— ✅
- [x] 无黑名单？—— 18 新源全跑 verifier，无 blacklisted ✅
- [x] 保留矛盾 + 标一手/二手/推断？—— 自报 WER 矛盾、Deepgram 价格双口径、break-even 标[推断] ✅
- [x] Phase 2 接口（DNA/谱系/时效/workflow 触发/冷僻）？—— ✅
