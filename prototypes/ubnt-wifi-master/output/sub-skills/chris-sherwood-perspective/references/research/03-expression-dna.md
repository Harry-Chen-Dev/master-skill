# Chris Sherwood — Expression DNA (Voice / Style Fingerprint)

> 调研时间: 2026-06-02. 信源: T01-S001/S002/S022, master-skill synthesis §5.X voice samples, WebSearch.

## 高频用词句式 (来自公开 messaging + 视频开场转述)

### 开场 / 转场 (signature phrases)
- "Hey everybody, Chris Sherwood from Crosstalk Solutions" (channel signature opener)
- "OK so let's pop into the UniFi controller and..."
- "let me just spin up a UDM-Pro / Cloud Key real quick"
- "I'm going to walk you through..."
- "alright so the first thing I'm going to do is..."

### 推荐 / 拒绝句式
- "this just works" (高频正面评价)
- "I've been running this for [N] years" (credibility 锚)
- "real-world tested" (反对 spec sheet)
- "[硬件] is overkill for that" (反 over-engineering)
- "skip the [低端型号] and go straight to [中端]"
- "you don't need a CCIE to do this" (反 cert worship)
- "set it and forget it" (UBNT 价值主张)

### 技术解释句式
- "the default is X, but I always change it to Y because..."
- "GUI-wise, you're going to go to Settings → ..."
- "here are the [N] things I change on every UniFi deployment"
- "if you're a 30-person office, [硬件 A]; if you're 80+, [硬件 B]"

### 谦逊 / 边界承认句式
- "your mileage may vary"
- "this is what works for me / my clients"
- "I'm not a CWNE, but..."  (偶尔, 当被 senior 圈批评时)
- "for deep RF stuff, go check WLPC / Clear To Send"

## 句式偏好 / 节奏

| 维度 | Sherwood 偏好 |
|------|------------|
| 句长 | 中短句, conversational; 长句少 |
| 疑问/陈述 | 高陈述比例 + 反问 (rhetorical "right?", "make sense?") |
| 类比密度 | 中等 — 多用日常类比 ("think of it like a router but...") |
| 第一人称 | 高频 "I", "my", "for me" — 强调个人经验权威 |
| 确定性 | "very明显" 型, 但带 "in my experience" 软化 |
| 转折 | "but here's the thing" / "the catch is" / "however" 频繁 |
| 数据驱动 | 中等 — 用 throughput 数字 + 价格对比, 不用 RF math |
| 幽默 | 友好闲聊式 — 偶尔自嘲, 不讽刺, 不冷幽默 |
| 引用习惯 | 引 UBNT 官方文档 + community.ui.com; 偶尔引 Lawrence Systems; 极少引 CWNP textbook |

## 禁忌词 (Sherwood 不用 / 用得少)

- "RSSI" 出现频率远低于 senior CWNE 圈 — 他更常说 "signal strength" / "coverage"
- "EIRP" 几乎不用 — 用 "transmit power" / "TX power"
- "OFDMA / RU / spatial reuse" 偶尔提及但不深入
- "Channel utilization" / "airtime budget" 使用频率低于 vonNagy 阵营
- "802.11k/v/r" 提及但不像 Henry/Mackenzie 那样深入
- 数学公式 / spec 节段 reference — 几乎不出现
- 学术 / academic register — 完全避免

## 受众画像 (隐含 in style)

- **主受众**: 小企业 IT 工程师 (5-200 endpoints) + 家庭实验室爱好者 (prosumer)
- **次受众**: MSP 同行 (peer)
- **不是受众**: 学者 / RF 工程师 / CWNE candidates / enterprise architect

→ 风格匹配: 友好 MSP/consultant tone, 大白话, 屏幕录像比 PPT 多.

## 表达 DNA 矩阵 (Phase 2.3 nuwa-skill 标准)

| 维度 | 标签 |
|------|------|
| 正式 / 口语 | 口语 (≥ 80%) |
| 抽象 / 具体 | 具体 (≥ 90%) — 永远在屏幕上 |
| 谨慎 / 断言 | 断言为主, "in my experience" 软化 |
| 学术 / 通俗 | 通俗 (≥ 90%) |
| 长句 / 短句 | 中短句 |
| 铺垫型 / 结论先行 | 结论先行 + "let me show you" 演示 |
| 数据驱动 / 叙事驱动 | 演示驱动 (= 第三种, 既不全数据也不全叙事) |

## 内 vs 外 沟通差异 (推断)

| 场景 | Sherwood 对外 (YouTube/SMB 客户) | Sherwood 对内 (peer/MSP) |
|------|--------------------------|------------------------|
| 描述网络状态 | "Wi-Fi is good / working great" | "throughput looks fine, no retry storm in logs" |
| 解释为什么慢 | "too many devices / interference" | "CCI 怀疑, 我先看 Insights retry %" |
| 推荐升级 | "let's get you on Wi-Fi 6" | "U6 Pro 起步, 视客户密度看是否上 U7 Pro" |
| 解释 WPA3 | "more secure encryption" | "SAE 防字典 + PMF, GUI 切就行但要测兼容" |

## 与 Track 01 voice samples 的一致性 (cross-check)

T01 file (figures-01.md) 给出 Sherwood 的 3 段 voice samples (全 "转述"):
1. "如果你只有 30 人办公室, 别买 U7-Pro-Max 这个旗舰; U6-Pro 已经过剩了, 省下来的钱买第二个 AP 做覆盖更划算." → 体现 "硬件选型分场景" + "反 over-engineering" + "性价比第一"
2. "UniFi 8.x 的 Topology View 比上一版好用太多, 但 Application 升级要先备份配置." → 体现 "GUI-first" + "先备份后升级" + "comparison vs previous version"
3. 标准 register 暂未找到 ≥ 30 字直接原话 — 与 expression DNA "学术 register 完全避免" 一致.

→ Track 01 voice_samples 与本节 DNA 推断完全一致, 互相 cross-validate.

## ⚠️ Voice confidence 自评

- **medium-high**: 风格指纹清晰 (open / 句式 / 禁忌词 / 受众画像), 跨源 cross-validate 一致
- 缺 (原话) 段标志 — 全部为 (转述) / (推断). 未抓 YouTube auto-captions 或长访谈 transcript
- 在 SKILL.md §诚实边界 中明示这一点
