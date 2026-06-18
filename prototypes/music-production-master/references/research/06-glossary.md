# Track 06 — Glossary + Standards: Music Production & Mixing (音乐制作 / 混音)

> locale = global (en-primary, material-rich). Industry type = creative audio-engineering craft.
> NOT cold: public material is extremely rich (books, vendor learn-pages, mixer interviews, standards bodies).
> last_updated: 2026-06-18 · last_checked: 2026-06-18

This industry skews **jargon-heavy + standards-medium + regulation-light + certification-near-N/A**.
- **Term / 黑话**: dominant — the craft runs on a dense slang vocabulary (mud, glue, pocket, mojo, pumping).
- **Acronym**: many (LUFS, dBTP, DI, MS, ITB, DAW, DDP, ISRC).
- **Standard**: a tight, high-stakes cluster around **loudness** (ITU-R BS.1770, EBU R128, K-System) + **delivery** (DDP, ISRC, dither/Red Book). These carry hard dates.
- **Regulation**: essentially **N/A** — music production is craft-governed, not law-governed (copyright/royalty law is explicitly out of scope per intake). Streaming "loudness normalization targets" are **de-facto platform specs**, not regulations.
- **Certification**: near-**N/A** — no licensing body. The closest is **Apple Digital Masters** (a vendor delivery program/badge, not a personal cert). No equivalent of "CPA" or "ISO auditor" exists; competence is signaled by credits/discography, not certificates.

---

## Source Manifest

| source_id | url | bucket | last_checked | author/host | one-line note |
|-----------|-----|--------|--------------|-------------|---------------|
| T06-S001 | https://www.itu.int/dms_pubrec/itu-r/rec/bs/R-REC-BS.1770-5-202311-I!!PDF-E.pdf | verified_primary | 2026-06-18 | ITU-R | BS.1770-5 (11/2023) — LUFS/K-weighting algorithm ground truth |
| T06-S002 | https://tech.ebu.ch/publications/r128 | verified_primary | 2026-06-18 | EBU Tech | R128 broadcast loudness recommendation, official |
| T06-S003 | https://support.spotify.com/us/artists/article/loudness-normalization/ | secondary | 2026-06-18 | Spotify for Artists | platform loudness spec (de-facto first-party); -14 LUFS, modes |
| T06-S004 | https://www.aes.org/ | verified_primary | 2026-06-18 | AES | Audio Engineering Society — standards body / Katz K-System paper venue |
| T06-S005 | https://www.ifpi.org/wp-content/uploads/2021/02/ISRC_Handbook.pdf | secondary | 2026-06-18 | IFPI | ISRC Handbook — issuing-body doc (de-facto standards authority) |
| T06-S006 | https://en.wikipedia.org/wiki/LUFS | secondary | 2026-06-18 | Wikipedia | LUFS term + BS.1770 lineage |
| T06-S007 | https://en.wikipedia.org/wiki/EBU_R_128 | secondary | 2026-06-18 | Wikipedia | R128 v5.0 (Nov 2023) revision history, gating |
| T06-S008 | https://en.wikipedia.org/wiki/De-essing | secondary | 2026-06-18 | Wikipedia | de-ess / sibilance term |
| T06-S009 | https://www.izotope.com/en/learn/a-glossary-of-common-and-confusing-mixing-terms | surrogate_primary | 2026-06-18 | iZotope (vendor docs) | vendor learn-page glossary; mixing term defs |
| T06-S010 | https://www.soundonsound.com/techniques/vocal-comping-editing | verified_primary | 2026-06-18 | Sound on Sound | trade magazine — comping/editing canon |
| T06-S011 | https://www.digido.com/portfolio-item/level-practices-part-2/ | verified_primary | 2026-06-18 | Bob Katz (Digido) | K-System originator's own level-practices essay |
| T06-S012 | https://help.uaudio.com/hc/en-us/articles/360049993352-Music-Production-Glossary | surrogate_primary | 2026-06-18 | Universal Audio | vendor docs — UA's own glossary; jargon defs |
| T06-S013 | https://bobbyowsinskiblog.com/the-new-glossary-of-mixing-terms-part-2/ | secondary | 2026-06-18 | Bobby Owsinski | canon author's slang glossary |
| T06-S014 | https://www.meterplugs.com/blog/2016/10/14/k-system-metering-101.html | secondary | 2026-06-18 | MeterPlugs | K-12/14/20 explainer |
| T06-S015 | https://www.audiomaster.co.uk/ddp-mastering-format-explained/ | secondary | 2026-06-18 | Steve Kitch Mastering | DDP format explainer (practitioner) |
| T06-S016 | https://www.izotope.com/en/learn/what-is-dithering-in-audio | surrogate_primary | 2026-06-18 | iZotope (vendor docs) | dither def + apply-once rule |
| T06-S017 | https://www.izotope.com/en/learn/mastering-for-streaming-platforms | surrogate_primary | 2026-06-18 | iZotope (vendor docs) | multi-platform LUFS target table |
| T06-S018 | https://www.criticallisteninglab.com/en/learn/loudness/apple-music | secondary | 2026-06-18 | Critical Listening Lab | Apple Sound Check -16 LUFS, down-only |
| T06-S019 | https://www.blog.landr.com/what-is-mid-side/ | surrogate_primary | 2026-06-18 | LANDR | vendor docs — LANDR's own publication; mid/side processing def |
| T06-S020 | https://www.production-expert.com/production-expert-1/apple-choose-16lufs-loudness-level-for-apple-music-heres-why | secondary | 2026-06-18 | Production Expert | Apple -16 LUFS rationale |

> Vendor SaaS learn-pages (iZotope/LANDR/UA) are marked `surrogate_primary` with `vendor docs` per task rule even where the verifier auto-returns `verified_primary`. Mental-model claims drawn from them require ≥2-source consensus before Phase 2 promotes them.
> No `blacklisted` URLs included. ISRC Handbook (IFPI) and Spotify artist docs are issuing-body/de-facto-first-party and used as `secondary` (verifier default for those hosts) rather than over-claimed.

---

## 总览（按 type 分组）

### Tier 1 — 核心必懂 (32 个)

| 术语 | Type | Insider def | Outsider tell | Last_updated |
|------|------|-------------|---------------|--------------|
| Gain staging | term | 全链路把每级信号设到最优电平,留余量、避噪/失真 | 以为="调音量大点" | 2026-06-18 |
| Headroom (余量) | term | 峰值到 0 dBFS 之间的安全空间 | 把 headroom 和 dynamic range 混为一谈 | 2026-06-18 |
| LUFS | acronym | 感知响度计量单位(ITU K-weighted, 整段积分) | 当成峰值/dB 读数 | 2026-06-18 |
| True Peak / dBTP | term+acronym | 过采样重建后的真实峰值,防 inter-sample 削波 | 以为=sample peak,设到 0 就好 | 2026-06-18 |
| Comping | term | 多 take 拼成一条最佳表演 | 以为=压缩(compression) | 2026-06-18 |
| Parallel compression | term | 干声并入重压副本,要冲击力又留动态(NY compression) | 以为只是"压得更狠" | 2026-06-18 |
| Sidechain | term | 用 A 轨触发 B 轨处理(kick 让 bass "让路") | 以为只用于 EDM "pumping" 效果 | 2026-06-18 |
| Mid-Side (MS) | term+acronym | 把立体声拆成中(和)+边(差)分别处理 | 以为=左右声道 | 2026-06-18 |
| De-ess | term | 动态压制齿音(s/sh/z)频段 | 以为=普通高频 EQ | 2026-06-18 |
| Sibilance (齿音) | term | 4–10 kHz 的刺耳 "嘶" 声 | 笼统说"高频太亮" | 2026-06-18 |
| Glue (胶水) | term | 总线轻压使各轨听起来像一起录的、抱团 | 以为是某个具体插件 | 2026-06-18 |
| The pocket / in the pocket | term/slang | 节奏卡在 groove 甜点上、稳而带律动 | 以为=完全对齐网格 | 2026-06-18 |
| Pumping | term | 压缩/sidechain 引起的可闻"呼吸"起伏 | 总当成缺陷,不知是风格 | 2026-06-18 |
| Mud / muddy (浑浊) | slang | 200–500 Hz 堆积、低中频糊 | 笼统说"低音太多" | 2026-06-18 |
| Harsh (刺耳) | slang | 2–5 kHz 过冲、听感扎耳 | 说"声音太尖"但定位不到频段 | 2026-06-18 |
| Boxy | slang | 300–600 Hz 像在盒子里、空洞中频 | 不知"boxy"指哪 | 2026-06-18 |
| Reference track (参考曲) | term | 用成品商业曲对照混音/响度/音色 | 以为=想抄的歌 | 2026-06-18 |
| A/B | term | 即时切换两版本盲对比(常需电平匹配) | 不知要 level-match 才公平 | 2026-06-18 |
| Bus / aux / send-return | term | 汇总/辅助/发送-返回的信号路由 | bus 与 group/aux 乱用 | 2026-06-18 |
| Dry / Wet | term | 未处理 vs 加效果的比例 | 以为只跟混响有关 | 2026-06-18 |
| Transient | term | 声音起始瞬态(attack),决定冲击力 | 当成"音量峰值" | 2026-06-18 |
| DI (direct input) | acronym | 直接录的干净电平号(吉他/贝斯) | 以为是某种话筒 | 2026-06-18 |
| Reamp | term | 把 DI 重新送回放大器/箱体再录 | 以为=重新录一遍 | 2026-06-18 |
| Print / bounce / render | term | 把处理/MIDI/总线"固化"成音频 | print 与 export 混用 | 2026-06-18 |
| Stems | term | 分组导出的子混(鼓/人声/乐器等) | 以为=单独每轨(那是 tracks/multitracks) | 2026-06-18 |
| Recall | term | 完整还原一个会话/硬件设置 | 不懂为何模拟硬件 recall 是噩梦 | 2026-06-18 |
| DAW | acronym | 数字音频工作站(Pro Tools/Ableton/Logic…) | 念 "dee-ay-double-u" 还是 "daw" 暴露生熟 | 2026-06-18 |
| ITB / OTB | acronym | In-the-box(全数字) / out-of-the-box(模拟硬件) | 不知缩写 | 2026-06-18 |
| Quantize | term | 把演奏对齐到节奏网格 | 以为=自动修一切 | 2026-06-18 |
| Mojo | slang | 难以言说的"灵性/染色感"(常归功硬件) | 当成玄学一笑了之/或盲信 | 2026-06-18 |
| Vibe / feel | slang | 整体情绪与人味,凌驾技术指标 | 以为是含糊托词 | 2026-06-18 |
| Dither | term | 降位深前注入随机噪声以掩盖量化误差 | 以为=普通降噪/可多次用 | 2026-06-18 |

### Tier 2 — 周边熟知 (28 个)

| 术语 | Type | Insider def | Last_updated |
|------|------|-------------|--------------|
| LRA (Loudness Range) | acronym | 整段响度的统计跨度(EBU 量) | 2026-06-18 |
| Integrated / Momentary / Short-term loudness | term | LUFS 的三种时间窗(全段/400ms/3s) | 2026-06-18 |
| K-weighting | term | BS.1770 的频率加权曲线(近 2 kHz 强调) | 2026-06-18 |
| Gating (loudness) | term | 绝对-70 LUFS + 相对-10 LU 门限,排除静音 | 2026-06-18 |
| Loudness penalty | term | 母带超过平台目标时被回拉的"惩罚" | 2026-06-18 |
| Inter-sample peak (ISP) | term | 样本间重建峰值,sample peak 测不到 | 2026-06-18 |
| Crest factor | term | 峰值与 RMS 之比,衡量动态/被压程度 | 2026-06-18 |
| RMS | acronym | 均方根平均电平,近似感知响度(K-System 用) | 2026-06-18 |
| dBFS | acronym | 相对满刻度的分贝,0=数字顶 | 2026-06-18 |
| dBSPL | acronym | 声压级分贝(83/85 为校准参考) | 2026-06-18 |
| Pre-fader / post-fader | term | 发送取自推子前/后 | 2026-06-18 |
| Multing | term | 同源信号分成多份各自处理(Brauer 著名手法) | 2026-06-18 |
| 3-bus / Scheps 3-bus | term | 把混音汇到 hi/mid/低三总线分别处理 | 2026-06-18 |
| Glue compression | term | 专指总线胶水压缩(SSL bus comp 经典) | 2026-06-18 |
| Punch | slang | 瞬态冲击+紧实低频带来的"打击感" | 2026-06-18 |
| Air | slang | 10 kHz+ 的开阔通透感 | 2026-06-18 |
| Presence | term | 2–5 kHz 让元素"靠前/清晰" | 2026-06-18 |
| Warmth | slang | 低中频饱满+谐波(常归功模拟) | 2026-06-18 |
| Width / mono compatibility | term | 立体声宽度 / 折叠成单声道是否劣化 | 2026-06-18 |
| Phase / polarity | term | 相位关系;反相会抵消(尤其多话筒) | 2026-06-18 |
| Null test | term | 两信号反相相加,差异为非零=有变化(揭穿玄学) | 2026-06-18 |
| Automation | term | 参数随时间的自动变化曲线 | 2026-06-18 |
| Swing / groove | term | 网格微偏移制造律动 | 2026-06-18 |
| Humanize | term | 给量化加随机微差找回人味 | 2026-06-18 |
| DDP | acronym | Disc Description Protocol,CD 复制母带交付格式 | 2026-06-18 |
| ISRC | acronym | 国际标准录音码,12 位曲目唯一指纹(IFPI) | 2026-06-18 |
| Red Book | term | 16-bit/44.1 kHz 音频 CD 规范(Philips/Sony) | 2026-06-18 |
| Apple Digital Masters | standard/cert-ish | Apple 的高保真母带交付程序/徽章(原 Mastered for iTunes) | 2026-06-18 |

### Standards / Specs 时间轴 (近 5 年内有显著变化的才进表)

| 名称 | Issued | Last revised | Decay risk |
|------|--------|-------------|------------|
| ITU-R BS.1770 (LUFS/K-weighting 算法) | 2006 | **BS.1770-5, 2023-11** (evidence: [T06-S001]) | Decay risk: medium |
| EBU R128 (广播响度规范) | 2010 | **v5.0, 2023-11** (前次 2020-08) (evidence: [T06-S007, T06-S002]) | Decay risk: medium |
| Spotify normalization target | ~2014 | -14 LUFS 整段, 现行 (Loud -11 / Normal -14 / Quiet -19) (evidence: [T06-S003]) | Decay risk: medium |
| Apple Music Sound Check target | — | ~-16 LUFS, 仅向下归一 (evidence: [T06-S018, T06-S020]) | Decay risk: medium |
| YouTube / Amazon / Tidal / Deezer targets | — | YT/Amazon/Tidal ≈ -14 LUFS, Deezer ≈ -15 LUFS (evidence: [T06-S017]) | Decay risk: medium |

> 长期稳定项不进时间轴: ISRC (IFPI, 设于 1986)、Red Book (1980), DDP 2.00(CD 主力版本)、K-System(AES, 2000) 只在主条目记 issued 年。

### 行业「外行破绽」高亮 (10 条最易暴露)

| 误用 | 内行实际意思 | 频率 |
|------|------------|------|
| 把 "comping" 当成压缩 | comping=拼 take, compression 才是压缩 | 高 |
| "把母带做到 0 dB / 越响越好" | 留 true peak ≤ -1 dBTP,响度战争已被流媒体归一终结 | 高 |
| 把 stems 说成 "每一轨" | stems=分组子混,multitracks 才是逐轨 | 高 |
| true peak 设到 0 就安全 | inter-sample peak 会越过 0,需 dBTP 余量 | 高 |
| "warmth/mojo" 当成必然的客观提升 | 常是谐波染色/安慰剂,内行会做 null test | 中 |
| LUFS 当成一个峰值数字读 | 它是整段 K-weighted 积分感知响度 | 中 |
| "in the pocket" = 完美对齐网格 | 恰相反,是带微偏移的人味 groove | 中 |
| 笼统说"声音太尖/太闷" | 内行定位到具体频段(harsh 2–5k / mud 200–500) | 中 |
| sidechain 只懂 EDM pumping | 它是通用触发式处理(de-ess、ducking 皆是) | 中 |
| 多次/在 24-bit 工程里乱加 dither | dither 只在最后一次降位深时用一次 | 中 |

---

## 详细条目 (Tier 1 全填 outsider-tell;含 standards 变化历史)

### 1. LUFS — Loudness Units relative to Full Scale
- **Type**: acronym + standard-bound
- **Tier**: tier-1
- **Definition (insider)**: 按 ITU-R BS.1770 K-weighting 对整段音频积分得到的感知响度,流媒体归一化就靠它。
- **Definition (outsider)**: 衡量"人耳觉得多响"的标准单位,不是瞬时峰值。
- **Etymology**: 出自 ITU-R BS.1770(2006 起),与 EBU 的 LU/LUFS 命名统一;BS.1770-5 于 2023-11 发布 (evidence: [T06-S001, T06-S006])。
- **outsider-tell**: `usage_tell` 外行把 LUFS 当 dB 峰值读;`pronunciation_tell` 读作 "loofs" 一词,内行也这么念,但把它和 "dB" 混用即露馅。
- **关联术语**: True Peak / Integrated loudness / K-weighting
- **变化历史**: BS.1770 系列 -1(2006)→…→-4(2015,gating 稳定)→**-5(2023-11)** (evidence: [T06-S001])。
- **可信度**: high · **Decay risk: medium** (算法 stable,但平台 target 仍在调)

### 2. True Peak / dBTP — 真实峰值
- **Type**: term + acronym
- **Tier**: tier-1
- **Definition (insider)**: 过采样重建后的真实最高电平,捕捉 sample-peak 测不到的 inter-sample 越界,母带交付一般留 -1 dBTP。
- **Definition (outsider)**: 数字波形采样点之间可能藏着更高的峰,会在播放/转码时削波。
- **outsider-tell**: `usage_tell` 以为限到 0 dBFS sample peak 就不削波。
- **关联术语**: Inter-sample peak / Headroom / dBFS
- **可信度**: high · **Decay risk: low** (evidence: [T06-S001, T06-S003])

### 3. EBU R128 (广播响度规范)
- **Type**: standard
- **Tier**: tier-2(从业必知但日常更多用流媒体 target)
- **Definition (insider)**: 欧洲广播联盟的响度规范,目标 **-23 LUFS**,True Peak ≤ **-1 dBTP**,用 LU/LUFS 计量,含绝对(-70 LUFS)+相对(-10 LU)双门限 gating。
- **Etymology / 变化历史**: 首发 2010;**v5.0 于 2023-11** 发布(新增电影内容补编 s4),前一次修订 2020-08 (evidence: [T06-S007, T06-S002])。
- **outsider-tell**: 把 R128 的 -23 LUFS 误当音乐流媒体目标(那是广播,音乐≈-14)。
- **可信度**: high · **Decay risk: medium** (12–24 月内可能再补编)

### 4. K-System (Bob Katz)
- **Type**: standard (metering/monitoring 协议)
- **Tier**: tier-2
- **Definition (insider)**: Katz 2000 年在 AES 109 提出的"计量+监听+电平"一体协议,以 RMS 为主、对抗响度战争;K-12/K-14/K-20 分别留 12/14/20 dB headroom,0 dB 对应 ~83 dBSPL(单声道)校准。
- **Etymology**: AES 论文《An Integrated Approach to Metering, Monitoring, and Level Practices》,2000 (evidence: [T06-S011, T06-S014, T06-S004])。
- **outsider-tell**: 把 K-14 的 "14" 和 Spotify 的 "-14 LUFS" 当同一回事(只是数字巧合,前者是 headroom 刻度,后者是绝对响度目标)。
- **可信度**: high · **Decay risk: low** (已稳定 20+ 年的概念)

### 5. DDP — Disc Description Protocol
- **Type**: acronym + standard (delivery)
- **Tier**: tier-2
- **Definition (insider)**: CD 复制用的母带交付格式,含音频流 + DDPMS 主描述符 + subcode(track index/ISRC/CD-Text)+ 校验,DDP 2.00 是 Red Book CD 主力版本。
- **outsider-tell**: 以为交付 = 发一堆 WAV;不知道压盘要 DDP image + 校验和。
- **可信度**: medium · **Decay risk: low** (CD 衰退但格式 stable) (evidence: [T06-S015])

### 6. ISRC — International Standard Recording Code
- **Type**: acronym + standard
- **Tier**: tier-2
- **Definition (insider)**: IFPI 制定的录音唯一码(国家码+注册码+年份+5 位序号,共 12 位),母带阶段嵌入 DDP 用于版税追踪;surround/不同版本需新 ISRC。
- **Etymology**: IFPI 体系,ISRC Handbook (evidence: [T06-S005])。
- **outsider-tell**: 把 ISRC 与 UPC(专辑码)/ISWC(作品码)混为一谈。
- **可信度**: high · **Decay risk: low**

### 7. Dither
- **Type**: term
- **Tier**: tier-1
- **Definition (insider)**: 在降低位深(如 24→16 bit)前注入极低电平随机噪声,把量化误差随机化为噪声而非可闻失真,**只在最后一次降位深时用一次**。
- **outsider-tell**: `usage_tell` 以为 dither=降噪,或在中间链路多次叠加;在 32-bit 浮点工程里到处加 dither。
- **可信度**: high · **Decay risk: low** (evidence: [T06-S016])

### 8. Glue / Glue compression
- **Type**: slang → term
- **Tier**: tier-1
- **Definition (insider)**: 混音"抱团、像一起录的"那种凝聚感;常由总线轻压(经典 SSL bus comp)实现。
- **outsider-tell**: `semantic_tell` 以为是某个特定插件名;不知它描述的是结果听感。
- **可信度**: high · **Decay risk: low** (evidence: [T06-S009, T06-S012])

### 9. The pocket / in the pocket
- **Type**: slang
- **Tier**: tier-1
- **Definition (insider)**: 节奏稳稳卡在 groove 甜点上、人味十足;人声"pocket"指人声在 beat 里的落位。
- **outsider-tell**: `usage_tell` 以为=完全量化到网格(恰恰相反,过度量化会丢 pocket)。
- **可信度**: high · **Decay risk: low** (evidence: [T06-S013])

### 10. Mojo / Warmth / Vibe (玄学簇)
- **Type**: slang(disputed)
- **Tier**: tier-1
- **Definition (insider)**: 难量化的"灵性/染色/人味",常归功模拟硬件谐波。
- **disputed**: 一派(模拟拥趸)认为 mojo/warmth 是真实可闻的谐波染色;一派(ITB/科学派)主张多为安慰剂,主张用 **null test** 盲测验证。两派并存,不强行统一。
- **outsider-tell**: 当成纯玄学一笑了之,或反过来盲信硬件必然"更暖"。
- **可信度**: medium · **Decay risk: low** (evidence: [T06-S011 null-test 立场])

> 其余 Tier 1/2 term(gain staging, headroom, comping, parallel compression, sidechain, mid-side, de-ess, transient, DI, reamp, print/bounce, stems, recall, quantize, multing, 3-bus, mud/harsh/boxy/punch/air/presence, phase/null test, automation, swing/humanize 等)定义见上方总览表的 insider def 列;其 outsider-tell 已在总览/破绽表给出。来源主要为 vendor 学习页(surrogate)+ 行业杂志/canon 作者(verified/secondary):evidence: [T06-S009, T06-S010, T06-S012, T06-S013, T06-S019, T06-S008]。

### 判定标准说明
- 全部进表的 Tier 1 词均满足:≥3 处行业 source 解释、定义稳定(除明确标 `disputed` 的 mojo 簇)、非单一厂商造词、可填 outsider-tell。
- 被 DROP 的候选: 通用音频词(如 "EQ"、"reverb"、"compressor" 本体)——外行也大致能正确理解,无强 outsider-tell,留作 Track 02(tools)处理,不占 glossary 配额。

---

## Phase 2 提炼提示

**「行业表达 DNA」直接素材**:
- 高频黑话 top 10: mud / glue / the pocket / mojo / vibe / pumping / punch / boxy / harsh / air —— 全是**听感隐喻**,印证"用耳不用眼、serve the song"的第一性。
- 行业拒绝/警惕的厂商话术 top 5:
  1. "warmth/mojo 是硬件必然优势"(ITB 派要 null test 反驳)→ 价值观:实证 > 玄学。
  2. "AI 一键母带 = 专业母带"(LANDR/iZotope 营销)→ 反模式:craft 不可全自动。
  3. "越响越有冲击力"(响度战争遗毒)→ 已被流媒体归一证伪。
  4. "preset 即风格"→ 内行视 preset 为起点非终点。
  5. 把 LUFS/true peak 包装成"一个数字达标即可"→ 内行强调整链路 gain staging。
- 外行破绽 top 10: 见上方"外行破绽高亮"表(comping=压缩、0 dB 母带、stems=每轨、true peak 设 0、in-the-pocket=网格 等)。

**「智识谱系」线索**:
- 范式更替: **响度战争(峰值最大化)→ 流媒体响度归一(LUFS 目标)** 是本行业近 15 年最大范式翻转;K-System(2000)是其先声,BS.1770/EBU R128 + 平台 -14 LUFS 是制度化落地。
- 竞争/分裂: 平台 target 不统一(Spotify/YT/Amazon/Tidal -14 vs Apple -16 vs Deezer -15)→ "为哪个平台母带"成流派之争的硬件层;ITB vs OTB 是工具哲学的长期分裂线。

**「时效性」信号(诚实边界)**:
- 近期有修订: **BS.1770-5(2023-11)** 与 **EBU R128 v5.0(2023-11)** 同月更新 → 标准层有活跃迭代。
- 预计 12–24 月内可能变: 流媒体响度 target(平台政策驱动,无公告即可调)、Apple Digital Masters 规范、可能的"lossless/空间音频"响度补充。这些是 master skill 衰减热点。

**「工作流变化触发」种子(喂 wave 3 Track 03)**:
- 流媒体归一(LUFS target)直接重写了**母带阶段假设**:从"推到 0 dB 最响"→"留 dBTP 余量、按平台 -14/-16 定 target"。
- 任何平台 target 调整 / 新增空间音频(Dolby Atmos)交付要求,都会触发 mastering + delivery workflow 变更。

**冷僻 / 信号薄弱自检**:
- 总术语数 60(Tier1 32 + Tier2 28)≫ 25 floor → **信号充足,非冷僻**。
- Tier 1 = 32 ≥ 15 ✅;Tier1+2 = 60 ≥ 40 ✅;Tier 1 outsider-tell 覆盖率 100% ✅。
- Regulation 维度 **N/A**(craft-governed,非法律驱动);Certification 维度近 **N/A**(仅 Apple Digital Masters 类 vendor 程序)——已显式标注,非缺漏。
- Surrogate 比例提示: 部分 term 定义来自 vendor 学习页(iZotope/LANDR/UA,标 `surrogate_primary` + `vendor docs`);Phase 2 心智模型 claim 需 ≥2 源 consensus 再提升,标准/响度数值已用 verified_primary(ITU/EBU/AES)或 de-facto 平台一手锚定。
