# Synthesis Candidates (raw scratchpad)

> Phase 2 Step 0 output. Cross-track candidate harvest before three-fold validation.
> Date: 2026-06-02. Source counts: T01=15 figures / T02=22 tools / T03=8 workflows / T04=48 canon entries / T05=23 sources / T06=60 glossary.

---

## 候选心智模型 (target 15-30; have 19)

| # | Candidate | 出现于 tracks | figures / canon evidence (count) | 类型 | 备注 |
|---|-----------|---------------|------------------------------|------|------|
| MM1 | Capacity-first design (容量优先 vs 覆盖优先) | T01, T02, T03, T04 | vonNagy, Akin, Parsons, Mackenzie, Coleman (5+) | cross-track, multi-figure | DIRECTLY addresses 80-person scenario; 跨人物 + 跨子场景 + 跨多 tracks |
| MM2 | Retry rate > RSSI (诊断: 重试率 > 信号强度) | T01, T02, T03, T06 | vonNagy, Mackenzie, Akin, Sherwood (4+) | cross-track | 诊断信号优先级颠倒 — 这一行的特殊看法 |
| MM3 | Vendor-neutral RF physics is the foundation (RF 物理跨 vendor) | T01, T04, T06 | Akin, Parsons, Coleman, Westcott, Henry, Badman (6) | cross-track | 15 位 figure 共识最强的一条 |
| MM4 | Client decides roaming (客户端决定漫游而非 AP) | T01, T03, T04, T06 | vonNagy, Coleman, Mackenzie, Henry (4) | cross-track | 11k/v/r mental model + outsider-tell |
| MM5 | Protocol-layer security ≠ patching (KRACK / Dragonblood) | T01, T03, T04, T06 | Vanhoef, Coleman, Henry, Akin (4) | cross-track | Wi-Fi 安全研究核心论点 |
| MM6 | Predictive design ≠ delivered design (设计要验证) | T01, T03, T04 | vonNagy, Mackenzie, Coleman, Akin (4) | cross-track | 设计 → 验证闭环 |
| MM7 | Specs / GUI 不替代 measurement (抓包永远是 ground truth) | T01, T03, T04 | Gast, Mackenzie, Coleman, Akin (4+) | cross-track | CWAP 派核心论点 |
| MM8 | Half-duplex CSMA/CA 决定 throughput 上限 (mesh per-hop) | T04, T06 | CWNA / Gast 多处 | single-track core | 物理事实 — 不进行业 mental model 因排他性弱 |
| MM9 | Layered diagnosis (PHY → MAC → assoc → auth → IP) | T03, T04 | CWAP / CWNA / multiple workflows | cross-track | 故障排查 SOP 根原则 |
| MM10 | Tx power asymmetry (AP 高功率 ≠ 客户端能回包) | T04, T06 | vonNagy, Aruba design guides | medium evidence | 客户端是 weakest link 的特化 |
| MM11 | Client is the weakest link (按最差客户端规划) | T01, T04 | Coleman, vonNagy, Apple Wi-Fi roaming doc | cross-track | CWDP 核心论点 |
| MM12 | Vendor-neutral foundation + vendor-specific overlay (UEWA 在 CWNA 之上) | T01, T04, T06 | Akin, Coleman, Parsons, CWNP 整个体系 | cross-track | UBNT 工程师成长路径 |
| MM13 | AIOps 是 augmentation 而非 replacement (LLM 是 propose, 人 approve) | T01, T02, T03 | Friday vs Akin/Parsons/Badman | controversial split | 流派分歧轴 (Mist vs CWNE 阵营) |
| MM14 | On-prem controller vs cloud-managed (UBNT vs Mist 哲学) | T01, T02 | Sherwood (UniFi), Friday (Mist), Howe | architectural divide | 流派分裂, 双方都对 — 不作 mental model |
| MM15 | UBNT-native pedagogy: GUI-first + 实战 > 理论 | T01, T03 | Sherwood, Lawrence, Howe (3) | new lineage | 6th 流派, 区别于 CWNE 学术派 |
| MM16 | "工具 ≠ 方法论" (装了 Ekahau 不等于会设计) | T02 | tools 提示反复强调 | weaker | 候选 playbook 而非 mental model |
| MM17 | CVE timing > feature timing (升级先看安全公告) | T01, T03 | Lawrence, Sherwood, community.ui.com | playbook-grade | 决策启发式, not mental model |
| MM18 | Monitoring from day 1, not phase 2 (unpoller 提前装) | T03 | senior workflow pattern | playbook-grade | 决策启发式 |
| MM19 | Wi-Fi 7 等待 client 跟上 (≠ "今天必上") | T01, T04, T06 | Akin (CTS Wi-Fi 7 主题), CWNA-110 滞后 | medium signal | 时效性观察, 非 mental model |

### 三重验证矩阵 (Step 1 输入)

| # | Candidate | V1 跨场景复现 | V2 生成力 | V3 排他性 | 判定 |
|---|-----------|--------------|----------|----------|------|
| MM1 | Capacity-first design | ✅ (T01+T02+T03+T04, 5 figures) | ✅ (新 floor plan 自动问 client × airtime) | ✅ (cellular 不用, 仅 Wi-Fi unlicensed) | **行业心智模型 #1** |
| MM2 | Retry rate > RSSI | ✅ (4 figures, multi-track) | ✅ (新故障会先要 retry %) | ✅ (cellular / Ethernet 不存在 retry % 优先) | **行业心智模型 #2** |
| MM3 | Vendor-neutral RF physics | ✅ (6 figures) | ✅ (任何 vendor 选型先问 PHY) | ⚠️ (PARTIAL — 任何 RF 行业都讲物理, 但 Wi-Fi 多 vendor 让 neutrality 成为强排他) | **#3 (放大版) — 强制描述 "在多 vendor 生态下的特化"** |
| MM4 | Client decides roaming | ✅ (4 figures) | ✅ (设计 voice over Wi-Fi 时先问 client cap) | ✅ (cellular handoff 是 network-decided, 反向) | **行业心智模型 #4** |
| MM5 | Protocol-layer security | ✅ (Vanhoef + 3) | ✅ (新 CVE 先问 spec or impl) | ✅ (Wi-Fi 协议史就是 patch-then-redesign) | **行业心智模型 #5** |
| MM6 | Predictive ≠ delivered | ✅ (4 figures) | ✅ | ⚠️ (放大版 — 工程通用 "model ≠ reality", 在 Wi-Fi 因 RF 不可见性而强) | **playbook 通则 (合并到 MM1)** |
| MM7 | Specs 不替代 measurement | ✅ (4+) | ✅ | ⚠️ (PARTIAL — empiricism 通用, 但 Wi-Fi 因 vendor cert 数字虚高而强) | **playbook 通则 (合并到 MM2 sibling)** |
| MM9 | Layered diagnosis PHY→...→IP | ✅ (4+ canon refs) | ✅ (任何故障先问哪一层) | ✅ (网络通用但 Wi-Fi PHY 层是协议而非物理) | **playbook 通则** |
| MM11 | Client is weakest link | ✅ | ✅ | ⚠️ (放大版) | **合并到 MM1** |
| MM12 | Foundation + overlay (CWNA → UEWA) | ✅ (T01+T04+T06 多处) | ✅ (新人成长建议) | ✅ (CWNP 体系是 Wi-Fi 独有 vendor-neutral cert 路径) | **行业心智模型 #6** |
| MM13 | AIOps augmentation 而非 replacement | ⚠️ (controversial: Friday 反对, Akin 支持) | ✅ | ✅ | **playbook + 流派分歧** (不作 mental model, 进 §7 智识谱系) |
| MM15 | UBNT-native pedagogy (GUI-first 实战) | ✅ (3 figures) | ✅ (面对 UBNT 客户先问 GUI workflow) | ⚠️ (放大版 — vendor-specific 实战教学每行都有, UBNT 强在 community-driven) | **#7 (放大版) — 用作行业第 6 流派定位** |
| 其他 (MM8/10/14/16/17/18/19) | — | — | — | — | playbook 或 vendor 信息 |

**最终 7 个 mental model 决定**: MM1, MM2, MM3 (放大), MM4, MM5, MM12, + 合并 MM15 进 §7 智识谱系
**最终选 6 个**: 验证后 MM15 进 §7 流派但不作 mental model. **取 6 个 (在 3-7 范围内)**.

---

## 候选 playbook 规则 (target 10-20; have 13)

| # | Pattern | 来源 (track + figures) |
|---|---------|----------------------|
| P1 | 如果 80-150 人密集办公 + 现有 Wi-Fi 差, 则先做 retry-rate / channel-utilization 诊断 而非加 AP | T01-vonNagy, T03-W3, T02 避坑#1 |
| P2 | 如果 设计 80+ 人办公新建, 则先算 airtime budget × 客户端密度, 后选 AP 数 | T01-vonNagy, T03-W1+W3, T04-CWDP |
| P3 | 如果 客户端 "连不上" / 频繁掉线, 则按 PHY→MAC→assoc→auth→IP 分层诊断, 不跳层 | T03-W2, T04-CWAP, T04-CWNA |
| P4 | 如果 voice / video 漫游粘连, 则同时启用 11k+11v+11r, 而非单开 11r | T03-W4, T04-Coleman/Henry, T06-S030 |
| P5 | 如果 升级 controller / 部署新版本, 则先看 CVE diff 再看 feature notes | T03-W6, T01-Lawrence, T05-S002 |
| P6 | 如果 即将 production change, 则 snapshot backup OR config-as-code 必先做 | T03-W1+W6+W7, T02-Art-of-WiFi |
| P7 | 如果 启用 WPA3, 则 hostapd-mana + nmap 真测 fallback, 而非 GUI 写就算 | T03-W7, T01-Vanhoef, T02-S043 |
| P8 | 如果 Min RSSI 调整, 则典型 -75 dBm (data) / -72 dBm (voice), 而非 -65 dBm 激进设置 | T02 避坑#5, T03-W4, T06-S011 |
| P9 | 如果 SMB ≤ 80 人单层办公预算紧, 则跳过 predictive survey, 用 WiFiman + ad-hoc 调整 | T03-W1+W5 资深路径, T05-iFeelTech |
| P10 | 如果 监控需求, 则 day 1 装 unpoller + Grafana, 不延迟到 phase 2 | T03-W1+W3+W6 资深 add, T05-S006 CTS 385 |
| P11 | 如果 选 AP, 主 AP 一律有线回程 + PoE, mesh 仅补盲 | T02 避坑#4, T04-CWNA, T03-W1 |
| P12 | 如果 2.4 GHz 启用, 则只用 20 MHz + ch 1/6/11, 或干脆关掉留 5/6 GHz | T02 避坑#3, T04-CWNA, T06-S013 |
| P13 | 如果 LLM agent / unifi-mcp 操作, 则 read-only gate + propose-then-approve, 而非直接 write | T03-W8, T02-S020 |

→ Phase 2 §2 取 8-10 条核心规则 (合并 P11+P12 进容量主题; P6+P13 进变更管控主题).

---

## 候选工具流派分裂 (智识谱系)

| Split | A 派代表 | B 派代表 | 核心分歧 |
|-------|---------|---------|---------|
| **Predictive-heavy vs Pragmatic-survey** | vonNagy + Mackenzie + CWDP (Ekahau) | Sherwood + Howe + Lawrence (WiFiman + ad-hoc) | 商业交付 vs SMB 实战 |
| **AIOps 派 vs Human-root-cause 派** | Friday (Mist Marvis) | Akin / Parsons / Badman (CWNE 阵营) | "让 AI 找问题" vs "工程师必须懂底层" |
| **On-prem controller vs Cloud-managed** | UBNT / Cisco WLC | Mist / Meraki / Aruba Central | 控制权 vs telemetry 集中化 |
| **Standards-first vs Vendor-specific** | Gast / Henry / Vanhoef (IEEE WG) | Sherwood / Howe (UBNT-native) | "懂 802.11 spec" vs "懂 UniFi GUI" |
| **Open-source tool vs Commercial tool** | WLAN Pi / Wireshark / unpoller | Ekahau Pro / NetAlly EtherScope | 工程师 DIY vs vendor-grade 交付 |

→ 6 流派定型 (Phase 2 §7):
1. Standards lineage (Gast, Henry, Vanhoef)
2. CWNP/CWNE lineage (Akin founder; Coleman, Westcott, Parsons, Mackenzie, Clements, Badman)
3. Capacity-first lineage (vonNagy)
4. AI-driven WLAN ops (Friday/Mist)
5. Security research (Vanhoef)
6. UBNT-native practitioner (Sherwood, Lawrence, Howe) — new lineage Wave 2

---

## 候选反模式 (target 5-10; have 12)

| # | Anti-pattern | 来源 |
|---|--------------|------|
| AP1 | 默认 AP TX Power 设到 Max ("信号更强 = 更爽") | T02-避坑#1, T04-vonNagy, T06-Tx asymmetry |
| AP2 | 用 WiFiman 替代正经 site survey | T02-避坑#2, T04-CWDP |
| AP3 | 2.4 GHz 启用 + 40 MHz 信道宽度 | T02-避坑#3, T04-CWNA, T06 |
| AP4 | U6/U7 Mesh 当主力 AP (wireless backhaul) | T02-避坑#4, T04 心智模型 |
| AP5 | Min RSSI 设激进 (-65 dBm) | T02-避坑#5, T06-S031 |
| AP6 | Cloud Key Gen1 跑 80 人办公 controller | T02-避坑#6 |
| AP7 | 忽视 UniFi 安全更新 (CVE) | T02-避坑#7, T05-Lawrence |
| AP8 | 假设 GUI "WPA3" 就配置正确, 不做 fallback test | T02-避坑#8, T04-Vanhoef |
| AP9 | 用 AirMagnet Survey PRO (NetAlly 已 EOL) | T02-避坑#9 |
| AP10 | 看 RSSI 而非 retry % / SNR 判断网络健康 | T01-vonNagy, T06-outsider-tell |
| AP11 | 把 PHY rate (1.2 Gbps) 当 throughput | T06-outsider-tell, T04-CWNA |
| AP12 | 加 AP 解决慢 Wi-Fi (causes CCI) | T06-outsider-tell #3, T03-W3 |

→ Phase 2 §6.2 取 8-10 条主要反模式.

---

## 候选时效信号 (诚实边界用)

| Signal | 来源 | Decay 强度 |
|--------|------|------------|
| Wi-Fi 7 textbook lag (CWNA-110 未出) | T01, T04 | high |
| zh-CN locale enterprise UBNT canon 缺位 | T01, T04, T05, T06 | structural (不会衰减) |
| UBNT AIOps 弱于 Mist (结构性 gap) | T01, T02, T03 | medium (~2 年可能改变) |
| China 6 GHz 未开放 (verify quarterly) | T06-S022 | high (政策可变) |
| W7 / W8 high-decay workflows (≤ 12 月) | T03 | high — 季度复查 |
| unifi-mcp / unifly < 1 年历史 single-maintainer | T02 | high |
| Gast 第 2 版未更新 (2005) | T04 | medium-high (canon 缺口) |
| AirMagnet EOL'd 2023-12 | T02-S034 | structural |
| Wi-Fi 7 MLO Wave 2 features still in flux | T06, T04 | high |
| Microsoft NPS PEAP-MSCHAPv2 deprecation | T06-S028 | medium |
| FragAttacks 仍在 vendor patch 进程中 | T01-Vanhoef, T03-W7 | medium |

---

## 候选 Agentic Protocol 维度 (target 5-7; have 6 from prompt)

| 维度 | 推导自 mental model |
|------|---------------------|
| AP1. 场景容量诊断 (client × throughput × airtime) | MM1 capacity-first |
| AP2. 症状指标定位 (retry %, MCS, channel utilization — NOT RSSI) | MM2 retry > RSSI |
| AP3. 客户端兼容性 audit (OS / chipset / 11k/v/r 支持) | MM4 client-decides-roaming |
| AP4. CCI/ACI 频谱审视 (spectrum + channel plan + neighbor) | MM1 + MM2 |
| AP5. CVE / 协议安全 advisory check (current version + WPA3 / FragAttacks) | MM5 protocol-layer security |
| AP6. vendor 对比锚 (Mist/Meraki/Aruba 对比 transparency) | MM12 foundation+overlay + 流派分歧 |

### 互斥性检查 (§B 硬规矩)
- AP1 (容量) vs AP4 (CCI): AP1 输入 = 客户端密度 + SLA; AP4 输入 = 频谱占用 + AP 邻居数. **不重叠** ✓
- AP2 (症状) vs AP4 (CCI): AP2 = 客户端侧 retry %; AP4 = AP 侧 channel utilization. **互补但不重叠** ✓
- AP3 (兼容性) vs AP5 (CVE): AP3 = client OS/chipset; AP5 = vendor firmware/spec. **不重叠** ✓
- AP6 (vendor 对比) 独立于 AP1-5: 仅在客户提及 Mist/Meraki/Aruba 时触发. **不重叠** ✓

→ 6 维度全部独立产出不同结论 — 保留. 

---

## 跨 track 未解决矛盾

无 — Phase 1.5 review checkpoint 已通过, 无未解决 contradiction.

**最强共识**: "vendor-neutral RF physics 是基础" — 15/15 figures 全部认同.
**最强分歧**: AIOps 派 (Friday) vs vendor-neutral CWNE 阵营 (Akin/Parsons/Badman) — 留在 §7 智识谱系明确列出, **不抹平**.

---

## Source counts (cumulative)
- T01 figures: 15 retained, 44 source_ids
- T02 tools: 21 retained, 49 source_ids
- T03 workflows: 8 retained, 30 source_ids
- T04 canon: 48 entries (textbook 9 + paper 7 + course 8 + concept 24), 47 source_ids
- T05 sources: 23 retained, 31 source_ids
- T06 glossary: 60 entries, 31 source_ids

**总 source_id pool**: ~232 (跨 track 重复后 unique 约 180)

**自检 — Step 0 候选门槛**:
- 行业类型 = Technical (Wi-Fi 工程是 standards-driven 技术行业, 介于 Technical 与 Vertical 实操之间)
- 候选 mental model: 19 (target ≥ 12, achieved ✓)
- 候选 playbook: 13 (target ≥ 10, achieved ✓)
- 候选反模式: 12 (target ≥ 5, achieved ✓)
- 候选 Agentic Protocol 维度: 6 (target ≥ 5, achieved ✓)
- Step 0 PASS — 进入 Step 1.
