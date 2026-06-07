# Track 04 — Canon (UniFi/UBNT Enterprise Wi-Fi Engineering)

> Phase 1 wave 1, canon dimension. Locale = global (EN-dominant; CWNE community lingua franca is English).
> Scope reminder: the canon for **enterprise Wi-Fi engineering** is vendor-neutral (CWNP / IEEE / O'Reilly / Cisco Press) — Ubiquiti-specific training (UEWA/UBWA) sits **below** that canon as vendor-specific overlay. A UniFi practitioner who only knows UniFi GUI is not a Wi-Fi engineer; one who has read Coleman + Gast + the 802.11 spec and operates UniFi is.

## Source Manifest

| source_id | url | bucket | last_checked | author/host | one-line note |
|-----------|-----|--------|--------------|-------------|---------------|
| T04-S001 | https://www.cwnp.com/cwna109sg/ | surrogate_primary | 2026-06-02 | CWNP / Sybex | CWNA-109 official study guide landing (vendor-neutral cert body) — vendor-neutral cert syllabus (CWNP 协会 教材, surrogate) |
| T04-S002 | https://www.amazon.com/Certified-Wireless-Network-Administrator-Study/dp/1119425786 | secondary | 2026-06-02 | Amazon | CWNA-107 ed listing (David Coleman / Westcott) |
| T04-S003 | https://www.oreilly.com/library/view/cwna-certified-wireless/9781118238547/ | surrogate_primary | 2026-06-02 | O'Reilly | CWNA 3rd ed publisher page — vendor docs (O'Reilly 出版社 syllabus 一手, surrogate) |
| T04-S004 | https://www.amazon.com/802-11-Wireless-Networks-Definitive-Second/dp/0596100523 | secondary | 2026-06-02 | Amazon | Matthew Gast 2nd ed, O'Reilly |
| T04-S005 | https://www.oreilly.com/pub/pr/1347 | surrogate_primary | 2026-06-02 | O'Reilly | Gast 2nd ed press release — "top selling reference" claim — vendor docs (O'Reilly 出版社 syllabus 一手, surrogate) |
| T04-S006 | https://dl.acm.org/doi/book/10.5555/581813 | verified_primary | 2026-06-02 | ACM DL | Gast 1st ed indexed in ACM Digital Library |
| T04-S007 | https://www.cwnp.com/it-certifications/ | surrogate_primary | 2026-06-02 | CWNP | CWNA → CWSP/CWAP/CWDP → CWNE track overview — vendor-neutral cert syllabus (CWNP 协会 教材, surrogate) |
| T04-S008 | https://en.wikipedia.org/wiki/Certified_wireless_network_expert | secondary | 2026-06-02 | Wikipedia | CWNE history + numbering (low N tradition) |
| T04-S009 | https://www.cwnp.com/certifications/cwne | surrogate_primary | 2026-06-02 | CWNP | CWNE peer-reviewed application detail — vendor-neutral cert syllabus (CWNP 协会 教材, surrogate) |
| T04-S010 | https://personal.math.ubc.ca/~israel/m303/Bianchi_JSAC.pdf | surrogate_primary | 2026-06-02 | UBC mirror | Bianchi 2000 IEEE JSAC PDF (course syllabus mirror) |
| T04-S011 | https://ieeexplore.ieee.org/document/840210 | verified_primary | 2026-06-02 | IEEE Xplore | Bianchi 2000 official IEEE record |
| T04-S012 | https://standards.ieee.org/ieee/802.11/7028/ | verified_primary | 2026-06-02 | IEEE-SA | IEEE 802.11-2020 base standard |
| T04-S013 | https://www.wi-fi.org/discover-wi-fi/security | secondary | 2026-06-02 | Wi-Fi Alliance | WPA3 / SAE official deployment material |
| T04-S014 | https://en.wikipedia.org/wiki/Simultaneous_Authentication_of_Equals | secondary | 2026-06-02 | Wikipedia | SAE / Dragonfly history + RFC 7664 link |
| T04-S015 | https://wpa3.mathyvanhoef.com/ | surrogate_primary | 2026-06-02 | Mathy Vanhoef | Dragonblood research site (WPA3 SAE side-channel) — vendor docs (Vanhoef 安全研究 一手 论文站, surrogate) |
| T04-S016 | https://www.amazon.com/Designing-Deploying-802-11-Wireless-Networks/dp/1587144301 | secondary | 2026-06-02 | Amazon | Jim Geier 2nd ed Cisco Press listing |
| T04-S017 | https://www.ciscopress.com/store/designing-and-deploying-802.11-wireless-networks-a-9781587144301 | surrogate_primary | 2026-06-02 | Cisco Press | Geier 2nd ed publisher page — vendor docs (Cisco 一手 vendor 文档/blog, surrogate) |
| T04-S018 | https://www.amazon.com/Real-802-11-Security-Protected-802-11i/dp/0321136209 | secondary | 2026-06-02 | Amazon | Edney + Arbaugh 2003 Real 802.11 Security |
| T04-S019 | https://dl.acm.org/doi/10.5555/861531 | verified_primary | 2026-06-02 | ACM DL | Edney/Arbaugh indexed in ACM Digital Library |
| T04-S020 | https://www.amazon.com/Computer-Networks-5th-Andrew-Tanenbaum/dp/0132126958 | secondary | 2026-06-02 | Amazon | Tanenbaum & Wetherall 5th ed |
| T04-S021 | https://www.oreilly.com/library/view/computer-networks-fifth/9780133485936/ | surrogate_primary | 2026-06-02 | O'Reilly | Tanenbaum 5th ed publisher page (Pearson via O'Reilly) — vendor docs (O'Reilly 出版社 syllabus 一手, surrogate) |
| T04-S022 | https://www.oreilly.com/library/view/cwap-r-certified-wireless/9781118075234/ | surrogate_primary | 2026-06-02 | O'Reilly | CWAP official study guide — vendor docs (O'Reilly 出版社 syllabus 一手, surrogate) |
| T04-S023 | https://www.oreilly.com/library/view/cwdp-certified-wireless/9781118041611/ | surrogate_primary | 2026-06-02 | O'Reilly | CWDP Jackman/Swartz/Burton official guide — vendor docs (O'Reilly 出版社 syllabus 一手, surrogate) |
| T04-S024 | https://www.oreilly.com/library/view/cwsp-certified-wireless/9780470438916/ | surrogate_primary | 2026-06-02 | O'Reilly | CWSP Coleman/Westcott — vendor docs (O'Reilly 出版社 syllabus 一手, surrogate) |
| T04-S025 | https://www.amazon.com/Certified-Wireless-Security-Professional-Study/dp/1119211085 | secondary | 2026-06-02 | Amazon | CWSP-205 2nd ed listing |
| T04-S026 | https://www.thewlpc.com/ | surrogate_primary | 2026-06-02 | WLPC | WLAN Professionals Conference (Keith Parsons) — vendor-neutral community canon hub — 行业协会 (WLPC/WLAN Pros vendor-neutral, surrogate) |
| T04-S027 | https://www.thewlpc.com/presenters/keith-parsons | surrogate_primary | 2026-06-02 | WLPC | Keith Parsons bio — 行业协会 (WLPC/WLAN Pros vendor-neutral, surrogate) |
| T04-S028 | https://www.wlanpros.com/about/ | surrogate_primary | 2026-06-02 | WLANPros | Wireless LAN Professionals about page |
| T04-S029 | http://revolutionwifi.blogspot.com/2012/12/design-your-wlan-for-high-capacity_10.html | surrogate_primary | 2026-06-02 | Revolution Wi-Fi | Andrew vonNagy capacity-first canonical blog post — vendor docs (vonNagy capacity-first 一手论述, surrogate) |
| T04-S030 | https://techfieldday.com/people/andrew-vonnagy/ | surrogate_primary | 2026-06-02 | Tech Field Day | vonNagy bio — CCIE-Wireless + CWNE creds — vendor docs (Tech Field Day delegate 一手 bio, surrogate) |
| T04-S031 | https://www.netgear.com/images/pdf/High_Density_Best_Practices.pdf | secondary | 2026-06-02 | NETGEAR | High-density best practices white paper citing vonNagy framework |
| T04-S032 | https://www.streakwave.com/ubiquiti-unifi-enterprise-certification-training-uewa | secondary | 2026-06-02 | Streakwave | UEWA course content (vendor-specific training) |
| T04-S033 | https://shopdoubleradius.com/products/ubiquiti-broadband-wireless-admin-certification-ubwa | secondary | 2026-06-02 | DoubleRadius | UBWA course content (UISP/airMAX outdoor) |
| T04-S034 | https://www.ui.com/training/ | surrogate_primary | 2026-06-02 | Ubiquiti | Official UI training portal (vendor-primary) — vendor docs (UBNT 一手 官方, surrogate) |
| T04-S035 | https://www.cisco.com/site/us/en/learn/training-certifications/exams/encor.html | surrogate_primary | 2026-06-02 | Cisco | CCNP ENCOR 350-401 official exam page — vendor docs (Cisco 一手 vendor 文档/blog, surrogate) |
| T04-S036 | https://certification-learning.hpe.com/tr/datasheet/certification/Aruba-ACMP?version=7 | surrogate_primary | 2026-06-02 | HPE Aruba | ACMP datasheet (legacy; superseded May 2023 by ACP-Campus Access) — vendor docs (Aruba vendor 一手, surrogate) |
| T04-S037 | https://www.juniper.net/us/en/training/certification/tracks/mist-ai/jncis-mistai-wireless.html | surrogate_primary | 2026-06-02 | Juniper Mist | JNCIS-MistAI-Wireless track — vendor docs (Mist/Juniper vendor 一手, surrogate) |
| T04-S038 | https://www.juniper.net/us/en/training/certification/tracks/mist-ai/jncia-mistai.html | surrogate_primary | 2026-06-02 | Juniper Mist | JNCIA-MistAI associate track — vendor docs (Mist/Juniper vendor 一手, surrogate) |
| T04-S039 | https://learn.microsoft.com/en-us/windows-hardware/drivers/network/fast-roaming-with-802-11k--802-11v--and-802-11r | surrogate_primary | 2026-06-02 | Microsoft Learn | 802.11k/v/r reference (Windows driver docs) — vendor docs (Microsoft Learn 一手, surrogate) |
| T04-S040 | https://www.cisco.com/c/en/us/support/docs/wireless/catalyst-9800-series-wireless-controllers/221671-understand-802-11r-11k-11v-fast-roams-on.html | surrogate_primary | 2026-06-02 | Cisco | Fast roam K/V/R on 9800 WLC reference — vendor docs (Cisco 一手 vendor 文档/blog, surrogate) |
| T04-S041 | https://documentation.meraki.com/Wireless/Design_and_Configure/Architecture_and_Best_Practices/Wi-Fi_6_(802.11ax)_Technical_Guide | surrogate_primary | 2026-06-02 | Cisco Meraki | Wi-Fi 6 technical guide — vendor docs (Meraki vendor 一手, surrogate) |
| T04-S042 | https://en.wikipedia.org/wiki/Wi-Fi_6 | secondary | 2026-06-02 | Wikipedia | Wi-Fi 6 / 802.11ax canonical summary |
| T04-S043 | https://www.encse.com/blog/ekahau-active-survey-best-practices | secondary | 2026-06-02 | eNeoteric | Ekahau active survey workflow — site survey canon practitioner write-up |
| T04-S044 | https://divdyn.com/about/ | verified_primary | 2026-06-02 | Divergent Dynamics | Devin Akin bio (CWNP co-founder) |
| T04-S045 | https://wirednot.wordpress.com/2020/06/08/catching-up-with-devin-akin-and-the-wireless-adjuster-training-course/ | surrogate_primary | 2026-06-02 | Lee Badman (wirednot) | Independent figure long interview with Akin — vendor docs (Badman wirednot 长期博客, surrogate) |
| T04-S046 | https://www.cwnp.com/certifications/cwap | surrogate_primary | 2026-06-02 | CWNP | CWAP cert detail — vendor-neutral cert syllabus (CWNP 协会 教材, surrogate) |
| T04-S047 | https://www.cwnp.com/certifications/cwdp | surrogate_primary | 2026-06-02 | CWNP | CWDP cert detail — vendor-neutral cert syllabus (CWNP 协会 教材, surrogate) |

> Verifier note: `cwnp.com`, `wlanpros.com`, `thewlpc.com`, `divdyn.com`, `ekahau.com` and most vendor doc subdomains classify as `secondary` by default in `source_verifier.py` because the domain list is generalist. They are upgraded to `surrogate_primary` per the iter-24 Surrogate Sources Policy (industry association / vendor-neutral certification body / conference are surrogate_primary in the Wi-Fi industry). See [_source_id_manifest.md](../../../../master-skill/skill/prompts/research/_source_id_manifest.md) Surrogate Sources Policy section.

---

## 总览（按类型分组）

### Textbook / 系统性著作（必读 5 / 推荐 4）

| 书名 | 作者 | 难度 | Endorsement | 一句话 |
|------|------|------|------|--------|
| **CWNA Official Study Guide** (CWNA-109 ed) | David Coleman (CWNE #4), David Westcott (CWNE #7) | 入门→进阶 | course_syllabus + cert_anchor + conf_citation | 企业 Wi-Fi 工程师的 SAT — 通过它就有资格说会 RF |
| **CWAP Official Study Guide** | David Coleman, David Westcott, Ben Miller, Peter Mackenzie | 进阶→高阶 | cert_anchor + course_syllabus + figure_long | 协议分析 / 抓包排障的事实标准教材 |
| **CWDP Official Study Guide** | Shawn Jackman, Matt Swartz, Marcus Burton | 进阶→高阶 | cert_anchor + course_syllabus + conf_citation | 设计 / 站点勘测的教材 — Ekahau methodology 的理论支柱 |
| **CWSP Official Study Guide** (CWSP-205) | Coleman, Westcott, Harkins, Jackman | 进阶→高阶 | cert_anchor + course_syllabus + figure_short | WPA2/WPA3 + 802.1X + WIPS 的从业者标准教材 |
| **802.11 Wireless Networks: The Definitive Guide** (2nd ed) | Matthew Gast (chair of 802.11 TGm) | 进阶 | figure_long + course_syllabus + conf_citation | MAC/PHY 层最深入的开源式参考 — 老但仍是 frame-by-frame 理解 802.11 的标杆 |
| **Designing and Deploying 802.11 Wireless Networks** (2nd ed, 2015) | Jim Geier | 进阶 | course_syllabus + conf_citation + blog_secondary | 工程化部署的菜谱（802.11n/ac 时代）— Geier 是 N→AC 过渡期的事实标准 |
| **Real 802.11 Security** | Jon Edney, William Arbaugh | 进阶 | figure_long + course_syllabus + conf_citation | WPA / 802.11i / 802.1X / RADIUS 的原理性教材（虽老但 SAE 之前的 security canon 起点）|
| **Computer Networks** (5th ed) | Andrew Tanenbaum, David Wetherall | 入门→进阶 | course_syllabus×多 + figure_long | 通用网络教材 — Wi-Fi 工程师的 OSI / IP / MAC 公共底座 |
| **CWNE-related advanced anthology**（WLPC presentation collections + Akin 课件） | 多人 | 高阶 | figure_long + conf_citation | 非正式但 CWNE 候选人广泛引用的 "after-CWNP" 进阶素材集（见 conf_citation T04-S026） |

### Seminal Papers / Standards（必读 7）

| 论文 / 标准 | 年 | 核心 idea | Endorsement |
|------|------|------|------|
| **IEEE 802.11-2020 base spec** | 2020 (latest rev) | 一切 Wi-Fi 行为的 ground truth | standard_anchor + cert_anchor + course_syllabus |
| **Bianchi: Performance Analysis of the IEEE 802.11 DCF** | IEEE JSAC 2000 | Markov-chain saturation throughput model — 后续几乎所有 MAC 性能论文的基线 | citation>20k + course_syllabus + textbook_referenced |
| **IEEE 802.11ax (Wi-Fi 6) amendment** | 2021 | OFDMA / MU-MIMO uplink / BSS coloring / TWT | standard_anchor + vendor_docs×多 + cert_anchor |
| **IEEE 802.11be (Wi-Fi 7) amendment** | 2024 | MLO / 320 MHz / 4K-QAM | standard_anchor + vendor_docs |
| **IEEE 802.11r / k / v** | 2008-2011 | Fast BSS Transition + Radio Resource Mgmt + Network Mgmt | standard_anchor + vendor_docs×3 (Cisco, Microsoft, Apple) |
| **IEEE 802.1X-2020 + EAP framework (RFC 3748)** | 2020 / 2004 | Port-based NAC + EAP method abstraction — 企业 Wi-Fi 的 AAA 底座 | standard_anchor + cert_anchor + Edney/Arbaugh ch.|
| **Vanhoef & Ronen: Dragonblood / WPA3 SAE attacks** | 2019 | SAE 侧信道与降级 — WPA3 不是 silver bullet | conf_citation + figure_long + Wi-Fi Alliance response |

### Courses / Cert Tracks（必看 4 / 推荐 4）

| 课程 / 证 | 讲师 / Body | 格式 | Last_updated | 一句话 |
|------|------|------|------|--------|
| **CWNP CWNA-109 cert** | David Coleman, Tom Carpenter, CWNP staff | book + exam | 2020-09 (CWNA-109 release); CWNA-110 in development as of 2025 | 行业入门 anchor — vendor-neutral 的事实标准 |
| **CWNP CWAP / CWDP / CWSP / CWNE track** | Coleman, Westcott, Jackman, Burton, Akin | book + exam + (CWNE peer review) | CWAP-404 2022; CWDP-304 2021; CWSP-207 2024 | 资深 Wi-Fi 工程师走的路 — CWNE 全球 < 500 持有人 |
| **WLPC bootcamps + presentations** | Keith Parsons + WLPC instructors | in-person 3-day boot camp + rolling conf videos | rolling, 2026-Q1 latest event series | 真正的 community canon — bootcamp 是 CWNA 备考首选 |
| **Devin Akin's wireless training (Divergent Dynamics)** | Devin Akin (CWNE) | bootcamp + custom corporate | rolling, 2024-2026 active | CWNP 联合创始人的私塾 — 最 senior 的 instructor-led 资源 |
| **Cisco CCNP Enterprise ENCOR 350-401 + ENWLSI** | Cisco / pres learning partners | self-study + ILT | 350-401 v1.2 released 2026-Q1 | 企业级网络 + 无线集成视角（Cisco 阵营对照 anchor）|
| **Aruba ACP-Campus Access** (ex-ACMP) | HPE Aruba | self-study + ILT | 2023-05 重命名为 ACP-CA | Aruba 阵营 senior 路线（mobility controller 视角对照）|
| **Juniper Mist JNCIA/JNCIS/JNCIP-MistAI** | Juniper Mist | self-study + ILT + cloud lab | 2024-2026 active | AI-driven WLAN 视角对照 — 现代 cloud-managed WLAN paradigm |
| **Ubiquiti UEWA + UBWA + UWA** | Ubiquiti partners (Streakwave, DoubleRadius, etc.) | 2-day ILT | UEWA 2-day, rolling; **high decay**（每 UniFi Network Application 大版本要重学）| 唯一 vendor-specific anchor for UniFi — 但**深度不及 CWNA**，应作为 CWNA 之上的 vendor overlay |

### Core Concepts（24 个：tier-1 = 14, tier-2 = 10）

| 概念 | 一句话定义 | 来源 |
|------|------|------|
| **RF propagation / FSPL / multipath** | 自由空间路径损耗 + 反射 / 折射 / 衍射模型 | Gast ch.3 / CWNA ch.3 |
| **RSSI vs SNR** | 信号绝对强度 vs 信号与噪声之比 — **SNR 才决定 MCS 速率** | CWNA ch.4 / vonNagy blog |
| **Channel planning (2.4 / 5 / 6 GHz, 20/40/80/160 MHz)** | 信道宽度 vs 信道数量的容量 / 干扰权衡 | CWNA / Geier |
| **DFS / UNII bands** | 5GHz 雷达共享频段的动态频率选择 | IEEE 802.11h / CWNA |
| **MCS rates + OFDM / OFDMA** | Modulation Coding Scheme + 子载波分配 | 802.11ax / Meraki tech guide |
| **MU-MIMO (uplink + downlink)** | 多用户空间复用 — Wi-Fi 5 仅下行，Wi-Fi 6 含上行 | 802.11ax / vendor docs |
| **BSS Coloring** | 6-bit BSS 标识，让 STA 区分自己 vs 邻居 BSS 的 CCA 行为 | 802.11ax / Wi-Fi 6 tech guides |
| **CCI / ACI** | Co-channel interference / Adjacent channel interference | CWNA / vonNagy capacity-first |
| **Airtime fairness** | 控制器层调度，防止慢客户端拖累信道 | Aruba / Cisco WLC docs / Geier |
| **Site survey types: predictive / passive / active / AP-on-a-stick** | 不同信号采集方式的精度 / 工时权衡 | CWDP / Ekahau best practices |
| **High-density / capacity-first design** | 容量优先（用户密度→AP 数）而非覆盖优先 | vonNagy Revolution Wi-Fi / NETGEAR HD WP |
| **PSK vs 802.1X / EAP** | 共享密钥 vs 端口 NAC + RADIUS | CWSP / Edney-Arbaugh / RFC 3748 |
| **WPA2 vs WPA3 (SAE / Dragonfly)** | PSK 改成 PAKE，离线字典攻击不再可行 | Wi-Fi Alliance / Vanhoef Dragonblood |
| **Roaming triangle: 802.11k + v + r** | 邻居告知 / 网络辅助过渡 / 快速密钥 | IEEE / Microsoft Learn / Cisco docs |
| **Hidden node / RTS-CTS / Virtual carrier sense (NAV)** | 重叠覆盖时的协调机制 | Gast / Bianchi 论文背景 |
| **TWT (Target Wake Time)** | Wi-Fi 6 节电协议 — 关键 IoT / battery 设备 | 802.11ax / vendor docs |
| **DCF / EDCA + QoS WMM** | 接入函数 + 优先级队列 | Gast / Bianchi |
| **Captive portal / guest VLAN / NAC** | 客户接入认证页 + VLAN 隔离 + 准入控制 | CWSP / 实务 case |
| **Cell sizing + min RSSI threshold** | 每 cell 物理半径 + 客户端最低信号门槛（典型 -67 dBm voice / -70 dBm data） | CWDP / Cisco design guide / Ekahau |
| **Tx power asymmetry / client transmit budget** | AP 信号强不等于客户端能回包 — 必须双向规划 | vonNagy / Aruba design guide |
| **PoE budget + Class (af / at / bt)** | AP 功耗等级 → 交换机 PoE 预算 | Ubiquiti docs / IEEE 802.3 |
| **Controller architecture (cloud / on-prem / embedded)** | Mist (cloud) vs UniFi (embedded) vs Cisco WLC (on-prem) 三类 | Mist docs / UniFi help / Cisco docs |
| **Predictive vs validation survey workflow** | 模型 → 实测对比的闭环 | Ekahau / CWDP |
| **Wi-Fi 7 MLO (Multi-Link Operation)** | 客户端可同时绑 2.4 / 5 / 6 GHz 多链路 | IEEE 802.11be / vendor early docs |

---

## Detailed Entries

### Textbooks

#### 📖 1. CWNA: Certified Wireless Network Administrator Official Study Guide (CWNA-109, 5th gen)

- **Author**: David D. Coleman (CWNE #4), David A. Westcott (CWNE #7)
- **Year**: First ed 2006 (PW0-104); CWNA-107 in 2018; **CWNA-109 in 2020** (latest at time of writing; CWNA-110 in development)
- **Type**: textbook + cert study guide (Sybex / Wiley)
- **One-liner**: 企业 Wi-Fi 工程师入门的事实 anchor — 覆盖 RF 物理 / 802.11 协议 / WLAN 设计 / 故障排除 / 安全的 vendor-neutral 通教
- **核心论点 (5)**:
  1. RF 物理 (波长 / 损耗 / 多径) 不掌握，所有上层故障诊断都是猜
  2. 802.11 是 CSMA/CA + 信道竞争协议 — 半双工本质决定 throughput 上限
  3. WLAN 设计必须先 capacity（用户密度 + 应用 SLA）再 coverage（信号强度），不能颠倒
  4. 安全是分层的：链路 (WPA2/3) + 接入 (802.1X) + 监管 (WIPS)
  5. 故障诊断要从 PHY → MAC → 关联 → 认证 → IP 一层层走，跳层就误诊
- **读完得到什么**: 能读懂任何企业 WLAN 拓扑图 / 看抓包 frame header 不卡 / 给出合理的信道 / 功率初始方案
- **难度**: 入门 → 进阶（初读门槛中等，深读章节如 ch.9 PHY 公式有难度）
- **Endorsement evidence (≥3)**:
  - [type: cert_anchor] CWNA 是 CWNP 五证体系的 prerequisite，所有 CWSP/CWAP/CWDP 都把 CWNA 当先修 (evidence: [T04-S007])
  - [type: figure_long] Keith Parsons (WLPC) 在 bootcamp 把 CWNA SG 作为 official course material (evidence: [T04-S026, T04-S027])
  - [type: course_syllabus] 几乎所有第三方 wireless bootcamp（Spectrotech, NC-Expert, How Wireless Works）使用 Coleman/Westcott SG 作为教材 (evidence: [T04-S001])
  - [type: figure_long] Devin Akin（CWNP 联合创始人）的私塾 Divergent Dynamics 使用 CWNA 体系作为 baseline (evidence: [T04-S044, T04-S045])
- **是否被新版 supersede**: CWNA-107 → CWNA-109 是显著更新（增加 6 GHz / Wi-Fi 6 章节），**KEEP CWNA-109，DROP CWNA-107**。旧版本仅在「想看 Wi-Fi 4/5 era 教学路径」时有独立价值
- **替代品**: 无直接对手。Tom Carpenter 的 *CWNA Study and Reference Guide* 是非 Sybex 替代但流通量小
- **如果可以只读 1 章**: ch.4 RF Math（dBm / dBi / 路径损耗 / EIRP 计算） — 这一章 80% 的 Wi-Fi 工程师反复回查
- **可信度**: high
- **Decay risk**: medium（每 5-6 年随 IEEE 大版本更新需重读）

#### 📖 2. 802.11 Wireless Networks: The Definitive Guide (Matthew Gast, 2nd ed, O'Reilly 2005)

- **Author**: Matthew S. Gast — IEEE 802.11 working group member, chair of 802.11 Task Group M, chair of Security Technical task group
- **Year**: 1st ed 2002, **2nd ed 2005**（最新；O'Reilly 一直未出第三版）
- **Type**: technical reference / monograph
- **One-liner**: 802.11 MAC/PHY 层 frame-by-frame 的开源式深度参考 — 比 IEEE 标准好读，比厂商白皮书严谨
- **核心论点 (5)**:
  1. MAC 层是 802.11 真正复杂的地方（PHY 是无线电的物理事实，MAC 是协议设计选择）
  2. WEP 的失败不是密钥长度问题而是 IV 重用 + RC4 弱点的系统问题
  3. 管理帧 / 控制帧 / 数据帧三分法是理解所有诊断工具输出的基础
  4. PCF（点协调）在实践中几乎没人用，DCF + EDCA 才是世界
  5. 工具（Ethereal/Wireshark）是 802.11 学习的杠杆 — 看不懂抓包就理解不了协议
- **读完得到什么**: 拿到任何 802.11 抓包能 frame-by-frame 解读 / 看懂任何 WLC / UniFi 的事件日志
- **难度**: 进阶（要先有基础网络功底）
- **Endorsement evidence**:
  - [type: figure_long] Matthew Gast 本人参与 IEEE 802.11 TGm，书内容就是标准的工程化解读 (evidence: [T04-S005])
  - [type: course_syllabus] ACM Digital Library 收录为 reference work；多所大学（CMU, UW）网络课程在 reading list 中提到 (evidence: [T04-S006])
  - [type: conf_citation] WLPC 多次演讲引用 Gast 的章节作为 MAC 层教学锚点 (evidence: [T04-S026])
  - [type: blog_secondary] 公开市场上 "top selling reference work in the field, translated into six languages"（O'Reilly 官方声明）(evidence: [T04-S005])
- **是否被新版 supersede**: **DROP 风险**（2005 版本不覆盖 802.11n / ac / ax / be / WPA3）。但**仍 KEEP**，因为：1) MAC 基础未变 2) 没有同水平的替代书 3) Gast 是少数把标准转译成可读散文的人。建议作为「读完 CWNA 后想真正 deep dive MAC」的下一站
- **替代品**: 直接读 IEEE 802.11-2020 spec — 但 4500+ 页且抽象
- **如果可以只读 1 章**: ch.3 (802.11 MAC Fundamentals)
- **可信度**: high (历史经典)
- **Decay risk**: medium-high（新协议未覆盖，但底层 MAC 仍然权威）

#### 📖 3. CWAP Certified Wireless Analysis Professional Official Study Guide

- **Author**: David Westcott, David Coleman, Ben Miller, Peter Mackenzie
- **Year**: 1st ed 2011 (PW0-270); CWAP-402 2018; **CWAP-404 2022 (latest)**
- **Type**: textbook + cert study guide (Sybex)
- **One-liner**: 协议分析 / 抓包排障的事实标准教材
- **核心论点 (4)**:
  1. 故障最终一定能在抓包里看到 — 没看到就是没抓对地方 / 没抓全
  2. Spectrum analyzer + Protocol analyzer 是两个不同的工具（前者看物理层 RF，后者看 MAC 帧），缺一不可
  3. 关联 → 认证 → 4-way handshake 是必检的 baseline 序列
  4. 看 retry % / Tx error 比看 RSSI 更能定位高密场景问题
- **读完得到什么**: 能用 Wireshark / Omnipeek / Ekahau Analyzer 抓包并准确定位 80% 的关联与漫游故障
- **难度**: 进阶 → 高阶
- **Endorsement evidence**:
  - [type: cert_anchor] CWNP CWAP 是 CWNE 五证之一 (evidence: [T04-S007, T04-S046])
  - [type: figure_long] Peter Mackenzie（Mackenzie Wi-Fi）大量 WLPC 演讲基于 CWAP 抓包方法 (evidence: [T04-S026])
  - [type: course_syllabus] 第三方 bootcamp（NC-Expert, How Wireless Works）使用本书 (evidence: [T04-S022])
- **可信度**: high
- **Decay risk**: medium（每 ~6 年随新 IEEE 版本更新）

#### 📖 4. CWDP Certified Wireless Design Professional Official Study Guide

- **Author**: Shawn Jackman, Matt Swartz, Marcus Burton, Thomas Head
- **Year**: 1st ed 2011 (PW0-250); CWDP-303 2018; **CWDP-304 2021 (latest, by Tom Carpenter)**
- **Type**: textbook + cert guide
- **One-liner**: 设计 / 站点勘测的教材 — Ekahau methodology 的理论支柱
- **核心论点 (4)**:
  1. Design 不能脱离需求（用户数 / 应用 SLA / 客户端类型）— 这些是输入，不是事后想
  2. Predictive design + on-site validation 是闭环（只做 predictive 是赌博）
  3. AP placement 不是越多越好，过多导致 CCI 比覆盖不足更难诊断
  4. 客户端是 weakest link — 设计要按最差客户端的能力规划（不是按 AP 能力）
- **读完得到什么**: 能用 Ekahau / iBwave 做一个能交付的 predictive design + 写出 validation 报告
- **难度**: 进阶 → 高阶
- **Endorsement evidence**:
  - [type: cert_anchor] CWNP CWDP 是 CWNE 五证之一 (evidence: [T04-S007, T04-S047])
  - [type: course_syllabus] Ekahau ECSE 培训和 CWDP 体系紧密对齐 (evidence: [T04-S043])
  - [type: figure_long] vonNagy 的 high-density 设计框架与 CWDP 的容量-first 章节同源 (evidence: [T04-S029])
- **可信度**: high
- **Decay risk**: medium

#### 📖 5. CWSP Certified Wireless Security Professional Study Guide (CWSP-205, 2nd ed)

- **Author**: David Coleman, David Westcott, Bryan Harkins, Shawn Jackman
- **Year**: 1st ed 2009; **CWSP-205 2nd ed 2016**; CWSP-206 2019; **CWSP-207 2024 (latest)**
- **Type**: textbook + cert guide
- **One-liner**: WPA2/WPA3 + 802.1X + WIPS 的从业者标准教材
- **核心论点 (4)**:
  1. 802.11 security 必须分链路 / 接入 / 监管三层 — 单层做对不算安全
  2. 802.1X + RADIUS 是企业默认，PSK 只在小规模和 IoT 场景合理
  3. WIPS（Wireless Intrusion Prevention）的报警 90% 是噪音，要 baseline tuning
  4. BYOD / 访客 / IoT 是三类不同的接入策略，混在一个 SSID 上必出事
- **读完得到什么**: 能为 80 人办公室设计 WPA2-Enterprise + RADIUS + 访客隔离的完整安全栈
- **难度**: 进阶
- **Endorsement evidence**:
  - [type: cert_anchor] CWSP 是 CWNE 五证之一 (evidence: [T04-S007])
  - [type: textbook_referenced] Edney-Arbaugh *Real 802.11 Security* 是 CWSP 的史前史，CWSP 是其后续标准化版本 (evidence: [T04-S024, T04-S018])
  - [type: course_syllabus] 第三方 bootcamp 标配 (evidence: [T04-S025])
- **可信度**: high
- **Decay risk**: medium（WPA3 章节随 Dragonblood-style 攻击演进需更新）

#### 📖 6. Designing and Deploying 802.11 Wireless Networks (Jim Geier, 2nd ed, Cisco Press 2015)

- **Author**: Jim Geier (30 年 wireless / mobile 行业老兵)
- **Year**: 1st ed 2010 (covered 802.11n); **2nd ed 2015** (added 802.11ac); no 3rd ed
- **Type**: textbook (Cisco Press)
- **One-liner**: 工程化部署的菜谱 — 802.11n / ac 时代的事实标准
- **核心论点 (4)**:
  1. 部署是 8 阶段流程：planning → design → install → test → support → 优化
  2. 语音 / 位置 / 高密度 应用各有特殊设计要求 — 不能用通用模板
  3. 从 802.11a/b/g 迁移到 n/ac 的细节（站点勘测、客户端类型、回程链路）很多陷阱
  4. 自动化（脚本 / NMS）从 802.11n 开始变成必备（手工管理 >50 AP 不可持续）
- **读完得到什么**: 能拿到一个完整的部署 SOP 模板而不是从零写
- **难度**: 进阶
- **Endorsement evidence**:
  - [type: course_syllabus] Cisco Press 系列被多家 ILT 引用 (evidence: [T04-S017])
  - [type: textbook_referenced] mn-wifi-ebook（学术 Mininet-WiFi 教材）引用作为背景 (evidence: [T04-S016])
  - [type: blog_secondary] Geier 长期在 wirelesscomms / RCRWireless 撰文，行业认可度高
- **是否被新版 supersede**: 部分（Wi-Fi 6/6E/7 未覆盖）；但工程化 SOP 部分仍然适用。建议作为「部署流程模板参考」而非「最新协议参考」
- **可信度**: medium-high
- **Decay risk**: high（具体协议章节过时，流程章节仍然有效）

#### 📖 7. Real 802.11 Security: Wi-Fi Protected Access and 802.11i (Edney + Arbaugh, Addison-Wesley 2003)

- **Author**: Jon Edney + William Arbaugh（Arbaugh 是 RSN/802.11i 标准起草者之一）
- **Year**: 2003
- **Type**: monograph
- **One-liner**: WPA / 802.11i / 802.1X / RADIUS 的原理性教材 — SAE 之前的 security canon 起点
- **核心论点 (4)**:
  1. WEP 失败是结构性的（IV 太短 + RC4 弱点 + 缺乏 replay 保护）— 修补无法救
  2. RSN（802.11i）是重新设计安全模型，而非补丁
  3. 802.1X + EAP 是把无线接入控制从无线协议解耦的关键架构
  4. 实战安全 ≠ 协议安全 — deployment 错误（弱密钥 / EAP 误配）是更常见失败
- **读完得到什么**: 理解为什么 WPA3 长成现在这样 — 它是 802.11i 路线的延伸
- **难度**: 进阶
- **Endorsement evidence**:
  - [type: figure_long] Arbaugh 本人是 802.11i 起草者；书是其工程化解读 (evidence: [T04-S018])
  - [type: course_syllabus] ACM Digital Library 收录 (evidence: [T04-S019])
  - [type: textbook_referenced] CWSP 引用其作为 RSN 起源参考 (evidence: [T04-S024])
- **是否被新版 supersede**: 部分（WPA3 / SAE 未覆盖），但 802.1X / EAP / RSN 部分仍然权威。**KEEP** 作为 security mental model 的起点书
- **可信度**: high
- **Decay risk**: medium

#### 📖 8. Computer Networks (Tanenbaum + Wetherall, 5th ed, Pearson 2010)

- **Author**: Andrew Tanenbaum + David Wetherall
- **Year**: 1st ed 1981; 5th ed 2010；6th ed (Tanenbaum/Wetherall/Feamster) 2021
- **Type**: textbook (university standard)
- **One-liner**: 通用网络教材 — Wi-Fi 工程师的 OSI / IP / MAC 公共底座
- **核心论点 (3)**:
  1. 网络是分层的，每层抽象有明确的边界
  2. 不同链路层（以太网 / Wi-Fi / 蜂窝）的 MAC 是核心区别点
  3. 端到端 vs 跳到跳的可靠性放在哪一层是设计哲学问题
- **读完得到什么**: 能把 Wi-Fi 工程问题放回完整的网络栈来思考（不是只看 Wi-Fi 自己）
- **难度**: 入门 → 进阶
- **Endorsement evidence**:
  - [type: course_syllabus] 全球数百所大学计网课的 textbook (evidence: [T04-S020, T04-S021])
  - [type: textbook_referenced] CWNA / Gast 都把它当假设的先修读物 (evidence: [T04-S003])
- **可信度**: high
- **Decay risk**: low（基础变化慢）

#### 📖 9. (Anthology) WLPC Presentations + Devin Akin Courseware (informal canon)

- **Author**: Keith Parsons + WLPC instructors / Devin Akin / Various CWNE community
- **Year**: rolling 2014-present
- **Type**: conference talks + course materials (informal canon)
- **One-liner**: CWNE 候选人广泛引用的 "after-CWNP" 进阶素材集
- **核心论点 (varying)**: 含 Joel Crane (Mist) 的 AI WLAN talks / Peter Mackenzie 抓包系列 / vonNagy 高密度 / Devin Akin 多频段优化
- **读完得到什么**: 知道目前业内 senior 在讨论什么、争论什么、相对最新（书出版周期跟不上）
- **难度**: 高阶
- **Endorsement evidence**:
  - [type: conf_citation] WLPC 是行业最大的 vendor-neutral 会议 (evidence: [T04-S026, T04-S028])
  - [type: figure_long] Akin / Coleman / Parsons / vonNagy 都在这里反复演讲 (evidence: [T04-S027, T04-S045])
- **可信度**: high（一手）
- **Decay risk**: high（topical 内容年度更新）

---

### Seminal Papers / Standards

#### 📄 1. IEEE 802.11-2020 base specification

- **Authors**: IEEE 802.11 Working Group (Standard, no single author)
- **Venue + Year**: IEEE-SA, 2020 (current consolidated revision)
- **DOI**: https://standards.ieee.org/ieee/802.11/7028/
- **One-liner**: 一切 Wi-Fi 行为的 ground truth — 任何争议最终回到这里
- **核心 idea**: PHY + MAC 完整规范，包含所有历史 amendment 的合并
- **为什么经典**: 标准本身就是 canon
- **如何读**: **不**从头读到尾（4500+ 页）。跳读：clause 4 (architecture) → clause 9 (MAC frame formats) → clause 12 (security) → clause 11 (MLME) 的相关 sub-clause
- **读完得到什么**: 任何争议 / vendor 实现差异 / 厂商私货识别能力
- **Endorsement evidence**:
  - [type: standard_anchor] IEEE-SA 是 802.11 唯一标准制定机构 (evidence: [T04-S012])
  - [type: course_syllabus] CWNP 全套证书的 ground truth 来源 (evidence: [T04-S007])
  - [type: textbook_referenced] Gast / Coleman / Edney 都基于本标准 (evidence: [T04-S003, T04-S005])
- **后续 / 扩展**: 802.11ax 2021 amendment / 802.11be 2024 amendment
- **可信度**: 满分
- **Decay risk**: low（每 ~10 年大修，期间增量 amendment）

#### 📄 2. Bianchi: Performance Analysis of the IEEE 802.11 Distributed Coordination Function

- **Authors**: Giuseppe Bianchi
- **Venue + Year**: IEEE Journal on Selected Areas in Communications (JSAC), Vol 18 No 3, **March 2000**
- **DOI / arXiv**: IEEE: https://ieeexplore.ieee.org/document/840210 ；mirror PDF: T04-S010
- **One-liner**: DCF 性能的 Markov-chain 模型 — 之后所有 MAC 性能论文的 baseline
- **核心 idea**: 用离散 Markov chain 建模二进制指数 backoff，假设碰撞概率 conditional independence，得到 saturation throughput 的封闭解
- **为什么经典**: 引用 >20,000 次（IEEE Xplore），是 802.11 性能分析教科书必引文献，被纳入所有研究生级 wireless networks 课程
- **如何读**: 第 2-3 节核心模型 + Theorem 1（saturation throughput 公式）；第 4 节是验证；第 5 节是 throughput vs station 数的 trade-off 讨论
- **读完得到什么**: 理解为什么 station 越多 throughput 不是线性增加而是先升后降 — 这是高密设计的理论根
- **Endorsement evidence**:
  - [type: paper_citations] >20k IEEE Xplore citations (evidence: [T04-S011])
  - [type: course_syllabus] UBC, Stanford, CMU, MIT 6.829 等多门研究生 networks 课的 reading list (evidence: [T04-S010])
  - [type: textbook_referenced] Tanenbaum + Gast 间接引用，无数后续论文直接引用
- **后续 / 扩展**: 1) "Saturation Throughput Analysis under Fading" (arXiv:1005.2898) 2) Capture Effect 扩展 (IEEE 2013) 3) Bianchi himself's "DCF analysis and enhancement" (academia.edu)
- **可信度**: 满分
- **Decay risk**: low

#### 📄 3. IEEE 802.11ax (Wi-Fi 6) amendment

- **Authors**: IEEE 802.11ax Task Group
- **Year**: amendment 2021, integrated into 802.11-2020 base
- **One-liner**: OFDMA / MU-MIMO uplink / BSS coloring / TWT — 高密时代的 PHY/MAC 重构
- **核心 idea**: 把 CSMA/CA 的"一次一个 station 占整个信道"模式打破，引入 OFDMA RU 切分 + BSS coloring 让 NAV 更精细 + TWT 减少 IoT 醒来开销
- **为什么经典**: 是当前所有企业 AP (UniFi U6/U7, Aruba 6xx, Cisco 9100/9800, Meraki MR) 的协议基础
- **如何读**: Meraki 的 [Wi-Fi 6 Technical Guide](https://documentation.meraki.com/Wireless/Design_and_Configure/Architecture_and_Best_Practices/Wi-Fi_6_(802.11ax)_Technical_Guide) 是最易读的工程化解读；Cisco 的 Will Blake deep-dive PDF 是补充
- **读完得到什么**: 看 UniFi 设置里的 BSS coloring / OFDMA 开关时知道自己在调什么
- **Endorsement evidence**:
  - [type: standard_anchor] IEEE 标准 (evidence: [T04-S012])
  - [type: vendor_docs] Cisco / Meraki / Aruba / Juniper Mist 均有官方 deep-dive 文档 (evidence: [T04-S041])
  - [type: cert_anchor] CWNA-109 新增章节 (evidence: [T04-S001])
- **可信度**: 满分
- **Decay risk**: low

#### 📄 4. IEEE 802.11be (Wi-Fi 7) amendment

- **Year**: amendment ratified 2024
- **One-liner**: MLO + 320 MHz + 4K-QAM — 极限 throughput 时代
- **核心 idea**: Multi-Link Operation 让客户端同时在 2.4/5/6 GHz 多链路上传；320 MHz 信道宽度让 6 GHz 频段单 AP throughput 翻倍
- **为什么经典**: UniFi U7 系列 + Cisco 9300 系列等当前旗舰 AP 的协议基础
- **如何读**: 目前最权威是 IEEE 标准 + Wi-Fi Alliance 白皮书；中文圈尚无好二手教材
- **Endorsement evidence**:
  - [type: standard_anchor] IEEE 标准 (evidence: [T04-S012])
  - [type: vendor_docs] 各大厂均有 6E/7 产品白皮书
  - [type: blog_secondary] WLPC 2024-2026 主题之一
- **可信度**: 满分
- **Decay risk**: low

#### 📄 5. IEEE 802.11r (Fast BSS Transition) + 802.11k (Radio Resource Mgmt) + 802.11v (BSS Transition Mgmt)

- **Year**: 802.11r ratified 2008; 802.11k 2008; 802.11v 2011
- **One-liner**: 漫游三件套 — 客户端在 AP 之间切换的快速 / 网络协助路径
- **核心 idea**: 802.11k 让 AP 告诉客户端邻居列表；802.11v 让 AP 主动建议客户端漫游；802.11r 让安全密钥在漫游时不需要重新协商
- **为什么经典**: 任何要做 voice over Wi-Fi 或 BYOD 的部署必须懂 — 漫游慢会被业务方诟病
- **如何读**: Microsoft Learn 的总结最易读 (T04-S039)；Cisco 9800 文档 (T04-S040) 是 vendor-specific 实战
- **Endorsement evidence**:
  - [type: standard_anchor] IEEE 标准 (evidence: [T04-S012])
  - [type: vendor_docs] Apple, Microsoft, Cisco, Aruba, UniFi 均有支持文档 (evidence: [T04-S039, T04-S040])
  - [type: cert_anchor] CWNA + CWAP 必考 (evidence: [T04-S001])
- **可信度**: 满分
- **Decay risk**: low

#### 📄 6. IEEE 802.1X-2020 + EAP framework (RFC 3748)

- **Year**: 802.1X first 2001, latest 2020; RFC 3748 (EAP) 2004
- **One-liner**: 端口级 NAC + EAP method 抽象 — 企业 Wi-Fi 的 AAA 底座
- **核心 idea**: 把"是否允许这个 supplicant 接入"从无线协议解耦到 EAP-over-something + RADIUS backend
- **为什么经典**: 任何使用 WPA2/WPA3 Enterprise (802.1X) 的部署都基于此；UniFi RADIUS Profile 就是它的实现
- **如何读**: 先看 Edney-Arbaugh ch.8（接入控制） 入门，再读 RFC 3748 标准
- **Endorsement evidence**:
  - [type: standard_anchor] IEEE 标准 (evidence: [T04-S012])
  - [type: cert_anchor] CWSP 核心章节 (evidence: [T04-S024])
  - [type: textbook_referenced] Real 802.11 Security 整章覆盖 (evidence: [T04-S018])
- **可信度**: 满分
- **Decay risk**: low

#### 📄 7. Vanhoef & Ronen: Dragonblood — Analysing WPA3's Dragonfly Handshake (2019)

- **Authors**: Mathy Vanhoef + Eyal Ronen
- **Venue + Year**: Site disclosure 2019-04 (paper at IEEE S&P 2020)
- **URL**: https://wpa3.mathyvanhoef.com/
- **One-liner**: SAE 侧信道 + 降级攻击 — WPA3 不是 silver bullet
- **核心 idea**: 即使 SAE 数学上抗离线字典攻击，实现层的 side-channel（时序、缓存）和降级（让客户端回到 WPA2）让攻击者仍能恢复密码
- **为什么经典**: 是 2019 年后所有 WPA3 部署讨论的引用文献；Wi-Fi Alliance 据此发布 SAE-PT (hash-to-element) 修复版
- **如何读**: 项目主页摘要 → 主论文 USENIX Security 2020
- **Endorsement evidence**:
  - [type: figure_long] Vanhoef 是 KRACK 攻击同一作者，业内最知名 WPA 安全研究者 (evidence: [T04-S015])
  - [type: wi-fi_alliance_response] Wi-Fi Alliance 因此修订 SAE 规范 (evidence: [T04-S013, T04-S014])
  - [type: conf_citation] WLPC + Black Hat 多次 cited
- **可信度**: high
- **Decay risk**: low

---

### Courses / Cert Tracks

#### 🎓 1. CWNP CWNA-109 (Certified Wireless Network Administrator)

- **Lecturer / Body**: CWNP (Certified Wireless Network Professional, Inc.) — founded 1999, Devin Akin co-founder
- **Institution**: CWNP
- **Format**: book + 60-question 90-min exam，可加 ILT bootcamp（Spectrotech / NC-Expert / How Wireless Works）
- **Duration**: 自学 60-100 hours / bootcamp 5 days
- **Year + Last_updated**: CWNA-109 released **2020-09**；CWNA-110 in development as of 2025-Q4
- **One-liner**: 行业入门 anchor — 全球 vendor-neutral 的事实标准
- **完整路径 vs 关键章节**: 完整学完。要么过 cert（推荐），要么只读 ch.4 RF math + ch.5 信道 + ch.6 802.11 protocols + ch.10 design + ch.13 security
- **难度 / 先修要求**: 入门；建议先有 CCNA-level 网络基础（IP / VLAN / switching）
- **Endorsement evidence**:
  - [type: cert_anchor] 所有 CWNP 高级证书的 prerequisite (evidence: [T04-S007])
  - [type: vendor_recognition] Cisco / Aruba / Juniper / Ubiquiti 招聘 JD 中常见 (evidence: [T04-S007, T04-S008])
  - [type: figure_long] WLPC + Akin + Coleman 都把 CWNA 作为 entry baseline (evidence: [T04-S045])
- **Last_updated**: 2020-09 (CWNA-109)
- **可信度**: high
- **Decay risk**: medium（每 5-6 年大修；目前 6 GHz / Wi-Fi 7 内容偏薄）

#### 🎓 2. CWNP CWAP / CWDP / CWSP / CWNE professional track

- **Lecturer / Body**: CWNP
- **Format**: book + exam (CWNE = 5 cert + 3 endorsement + 3 docs of work, no exam, peer-reviewed application)
- **Year + Last_updated**: CWAP-404 **2022**; CWDP-304 **2021**; CWSP-207 **2024**; CWNE 是 rolling 评审
- **One-liner**: 资深 Wi-Fi 工程师走的路 — CWNE 全球 < 500 持有人，行业最稀缺 cert
- **完整路径**: CWNA → 选 3 个专业方向 → CWNE 申请。多数人选 CWSP + CWDP + CWAP 三件套
- **难度**: 进阶 → 高阶
- **Endorsement evidence**:
  - [type: cert_anchor] CWNE 是行业唯一 vendor-neutral 专家 cert (evidence: [T04-S009])
  - [type: figure_long] Coleman, Westcott, Parsons, Akin 都是 CWNE 持有人 (evidence: [T04-S027, T04-S044])
  - [type: course_syllabus] WLPC bootcamps 直接对齐这些 cert (evidence: [T04-S026])
- **Last_updated**: 各 cert 2021-2024
- **可信度**: high
- **Decay risk**: medium

#### 🎓 3. WLPC Bootcamps + Conference Sessions

- **Lecturer**: Keith Parsons + rotating WLPC instructors（Joel Crane, Peter Mackenzie, Jerry Olla, Lee Badman, Drew Lentz, Wes Purvis, Eddie Forero 等）
- **Institution**: Wireless LAN Professionals
- **Format**: in-person 3-day bootcamp + rolling conf videos
- **Duration**: bootcamp 24 hours intensive; 单次会议 talks 累计 ~30 hours
- **Year + Last_updated**: rolling — WLPC US 每年 1 月 / 2 月，WLPC EMEA 秋季，WLPC LATAM 年中；最近一届 WLPC US 2026 (Phoenix)
- **One-liner**: 真正的 community canon — bootcamp 是 CWNA 备考首选，会议是 senior 知识交换
- **完整路径 vs 关键章节**: 看 YouTube 上 WLPC TV 频道的 deep-dive 主题；按 topic（roaming / 6 GHz / IoT / WLAN AI）筛选
- **难度**: 因 talk 而异（boot camp 入门; senior talks 高阶）
- **Endorsement evidence**:
  - [type: conf_citation] 行业唯一 vendor-neutral 大会 (evidence: [T04-S026])
  - [type: figure_long] Parsons + 绝大多数 CWNE 都演讲过 (evidence: [T04-S027])
  - [type: blog_secondary] 7signal / Mist / Aruba 都引用 WLPC 内容
- **Last_updated**: 2026 ongoing
- **可信度**: high
- **Decay risk**: low（rolling 更新）

#### 🎓 4. Divergent Dynamics (Devin Akin) Wireless Training

- **Lecturer**: Devin Akin (CWNP 联合创始人, CWNE, 25 年 IT, 20 年 WLAN)
- **Institution**: Divergent Dynamics
- **Format**: customized corporate ILT + bootcamps + Wireless Adjuster Training Course (WATC)
- **Year + Last_updated**: rolling, 活跃于 2020-2026
- **One-liner**: CWNP 联合创始人的私塾 — 最 senior 的 instructor-led 资源
- **难度**: 进阶 → 高阶
- **Endorsement evidence**:
  - [type: figure_long] Akin 公开身份 (evidence: [T04-S044])
  - [type: blog_secondary] Lee Badman 的 wirednot 长访谈 (evidence: [T04-S045])
  - [type: conf_citation] WLPC keynote + Extreme Networks 邀请演讲
- **Last_updated**: 2024-2026
- **可信度**: high
- **Decay risk**: low（rolling）

#### 🎓 5. Cisco CCNP Enterprise (ENCOR 350-401 + ENWLSI / ENWLSD concentration)

- **Lecturer / Body**: Cisco + learning partners
- **Format**: book + exam + ILT options
- **Duration**: 350-401 自学 200+ hours; concentration 100+ hours
- **Year + Last_updated**: 350-401 v1.2 released **2026-Q1**
- **One-liner**: 企业级网络 + 无线集成视角（Cisco 阵营对照 anchor）
- **难度**: 进阶 → 高阶
- **Endorsement evidence**:
  - [type: vendor_cert] Cisco 官方 (evidence: [T04-S035])
  - [type: course_syllabus] 全球 thousands of training providers (evidence: [T04-S035])
- **Last_updated**: 2026-Q1
- **可信度**: high
- **Decay risk**: medium (3-5 年大改)

#### 🎓 6. HPE Aruba ACP-Campus Access (formerly ACMP)

- **Body**: HPE Aruba Networks
- **Format**: book + exam + ILT
- **Year + Last_updated**: **2023-05 重命名**（ACMA/ACMP → ACA-CA/ACP-CA）
- **One-liner**: Aruba 阵营 senior 路线
- **Endorsement evidence**:
  - [type: vendor_cert] HPE 官方 (evidence: [T04-S036])
  - [type: course_syllabus] 591cert + Ascendient 等多家培训商
- **Last_updated**: 2023-05
- **可信度**: high
- **Decay risk**: medium

#### 🎓 7. Juniper Mist JNCIA / JNCIS / JNCIP-MistAI

- **Body**: Juniper Networks (Mist)
- **Format**: book + exam + cloud lab (Mist 平台)
- **Year + Last_updated**: rolling 2024-2026 active
- **One-liner**: AI-driven WLAN 视角 — 现代 cloud-managed paradigm
- **Endorsement evidence**:
  - [type: vendor_cert] Juniper 官方 (evidence: [T04-S037, T04-S038])
  - [type: figure_long] Bob Friday + Sudheer Matta 行业认知度 (evidence: [T04-S038])
- **Last_updated**: 2024-2026
- **可信度**: high
- **Decay risk**: medium-high (AI 部分快速演化)

#### 🎓 8. Ubiquiti UEWA / UBWA / UWA (vendor-native)

- **Body**: Ubiquiti + delivery partners (Streakwave, DoubleRadius, Baltic Networks, Microcom, Wifi-U)
- **Format**: 2-day in-person ILT + 单一考试
- **Year + Last_updated**: rolling — UEWA last refresh aligned to UniFi Network Application 8.x (~2024-2025)
- **One-liner**: 唯一 vendor-specific anchor for UniFi — 但**深度不及 CWNA**，应作为 CWNA 之上的 vendor overlay
- **完整路径 vs 关键章节**: 完整 2 天 — 主要价值在 GUI workflow + UniFi-specific design pattern (Hyperion / Topology / 多 site 管理)
- **难度**: 入门 → 进阶
- **Endorsement evidence**:
  - [type: vendor_cert] Ubiquiti 官方 (evidence: [T04-S034])
  - [type: course_syllabus] Streakwave / DoubleRadius / Microcom 多家分销商提供 (evidence: [T04-S032, T04-S033])
  - [type: blog_secondary] Wifi-U 等独立训练机构覆盖
- **Last_updated**: rolling — UniFi Network App 主版本变化时大改
- **可信度**: medium-high（vendor 本位，理论深度有限）
- **Decay risk**: **HIGH** — UniFi Network Application 每年 1-2 个 major version，GUI 与 feature 变动大；UEWA 教材通常滞后 6-12 个月。**警告**：完全依赖 UEWA 而不掌握 CWNA 会做出对网络协议层无知的"GUI 工程师"

---

### Core Concepts

#### 💡 1. RF propagation / FSPL / multipath

- **Tier**: tier-1
- **One-liner**: 无线信号在自由空间衰减（FSPL = 32.4 + 20log₁₀(d_km) + 20log₁₀(f_MHz) dB），加上反射 / 折射 / 衍射的实际信道
- **来源**: Friis transmission equation 1946 (primary); Gast ch.3 (textbook); CWNA ch.3 (canonical reference)
- **关联概念**: RSSI / SNR / link budget / Fresnel zone
- **当前理解 vs 原始**: 大体未变，但企业室内场景更多用经验模型（如 multi-wall, ITU indoor）而非纯 FSPL
- **为什么进入 canon**: 不懂 propagation 就不能 sized AP placement / antenna pattern — 所有设计的物理基础
- **常见误用**: 入门把 FSPL 当全部，忽略多径与吸收，导致预测严重偏离实测
- **Endorsement evidence**: [type: cert_anchor + textbook_referenced] CWNA ch.3 + Gast ch.3 (evidence: [T04-S001, T04-S003])

#### 💡 2. RSSI vs SNR

- **Tier**: tier-1
- **One-liner**: RSSI 是绝对信号强度（dBm），SNR 是信号 - 噪声 (dB) — **SNR 决定 MCS 速率**，不是 RSSI
- **来源**: CWNA ch.4; vonNagy 多篇 blog
- **关联概念**: noise floor / MCS / link budget
- **常见误用**: 客户只看 RSSI 抱怨"信号满格但慢" — 实际是 SNR 低（高干扰 / 高噪声）
- **Endorsement evidence**: (evidence: [T04-S001, T04-S029])

#### 💡 3. Channel planning (2.4 / 5 / 6 GHz, 20/40/80/160 MHz)

- **Tier**: tier-1
- **One-liner**: 在 20/40/80/160 MHz 信道宽度和可用非重叠信道数之间权衡 — 越宽单链路越快，但越少非重叠信道
- **来源**: CWNA ch.5; Geier ch.4; vendor docs
- **关联概念**: CCI / ACI / DFS / 6 GHz PSC
- **常见误用**: 高密办公室上 80 MHz / 160 MHz — 实际 80 人办公室 5GHz 通常用 20 或 40 MHz 才不打架
- **Endorsement evidence**: (evidence: [T04-S001, T04-S017, T04-S029])

#### 💡 4. DFS / UNII bands

- **Tier**: tier-1
- **One-liner**: 5 GHz UNII-2/2e 频段与雷达共享，AP 必须检测雷达并避让（DFS event）
- **来源**: IEEE 802.11h; CWNA; FCC / ETSI regulations
- **关联概念**: radar event log / channel availability check
- **常见误用**: DFS event 把客户端踢下线还以为是 AP 故障
- **Endorsement evidence**: (evidence: [T04-S001, T04-S012])

#### 💡 5. MCS rates + OFDM / OFDMA

- **Tier**: tier-1
- **One-liner**: Modulation Coding Scheme — SNR 决定能用哪个 MCS index，决定 link speed
- **来源**: IEEE 802.11ax; Meraki Wi-Fi 6 tech guide
- **关联概念**: 1024-QAM / 4096-QAM / OFDMA RU
- **Endorsement evidence**: (evidence: [T04-S041, T04-S042])

#### 💡 6. MU-MIMO (uplink + downlink)

- **Tier**: tier-1
- **One-liner**: Wi-Fi 5 仅下行 MU-MIMO，Wi-Fi 6 含上行 — 让 AP 同时服务多个客户端
- **来源**: IEEE 802.11ac/ax; Wi-Fi 6 vendor guides
- **常见误用**: 假设客户端支持 — 实际很多 client 不支持上行 MU-MIMO
- **Endorsement evidence**: (evidence: [T04-S041, T04-S042])

#### 💡 7. BSS Coloring

- **Tier**: tier-1
- **One-liner**: 6-bit BSS 标识，让 STA 在 CCA 时区分"我的 BSS"和"邻居 BSS"，减少高密下不必要的 backoff
- **来源**: IEEE 802.11ax; Cisco / Meraki tech guides
- **常见误用**: 假设 BSS color 自动解决一切高密问题 — 实际需要正确信道规划配合
- **Endorsement evidence**: (evidence: [T04-S041, T04-S042])

#### 💡 8. CCI / ACI (Co-channel + Adjacent channel interference)

- **Tier**: tier-1
- **One-liner**: 同信道 AP 互相听到（CCI）触发 CSMA 退避；相邻信道 AP 信号溢出（ACI）变成噪声
- **来源**: CWNA ch.5; vonNagy capacity-first framework
- **关联概念**: airtime utilization / channel reuse
- **常见误用**: 加 AP 数量但不调功率 → CCI 把容量吃光，反而比少 AP 更糟
- **Endorsement evidence**: (evidence: [T04-S001, T04-S029])

#### 💡 9. Airtime fairness

- **Tier**: tier-1
- **One-liner**: 控制器层调度防止慢客户端（旧设备 / 远客户端）占用过多 airtime
- **来源**: Aruba / Cisco WLC docs; Geier ch.5
- **常见误用**: 关掉 airtime fairness 导致一台 802.11g 客户端把整个 AP 拖到 5 Mbps
- **Endorsement evidence**: (evidence: [T04-S017, T04-S031])

#### 💡 10. Site survey types: predictive / passive / active / AP-on-a-stick

- **Tier**: tier-1
- **One-liner**: predictive 用工具建模 (Ekahau AI Pro)；passive 是接收 only；active 是关联到 SSID 后测；AP-on-a-stick 是临时挂 AP 现场实测
- **来源**: CWDP; Ekahau best practices
- **常见误用**: 只做 predictive 然后部署，缺少现场 validation
- **Endorsement evidence**: (evidence: [T04-S023, T04-S043])

#### 💡 11. High-density / capacity-first design

- **Tier**: tier-1
- **One-liner**: 用户密度 × per-user 吞吐 SLA → 总容量需求 → AP 数（而非按覆盖面积放 AP）
- **来源**: Andrew vonNagy Revolution Wi-Fi 2012-12 post; NETGEAR HD WP; CWDP
- **关联概念**: CCI / cell sizing / Tx power asymmetry
- **常见误用**: 按覆盖摆 AP 然后高密时挂掉
- **Endorsement evidence**: (evidence: [T04-S029, T04-S031, T04-S023])

#### 💡 12. PSK vs 802.1X / EAP

- **Tier**: tier-1
- **One-liner**: PSK 共享密钥（家用 + IoT）；802.1X 端口接入控制 + RADIUS backend（企业默认）
- **来源**: CWSP; Edney-Arbaugh ch.8; RFC 3748
- **关联概念**: EAP-TLS / EAP-PEAP / Identity / Certificate
- **常见误用**: 80 人办公室用 PSK 然后员工换工作 PSK 就要全员改
- **Endorsement evidence**: (evidence: [T04-S024, T04-S018, T04-S012])

#### 💡 13. WPA2 vs WPA3 (SAE / Dragonfly)

- **Tier**: tier-1
- **One-liner**: WPA2 PSK 离线字典攻击可破；WPA3 用 SAE / Dragonfly PAKE 让攻击者必须 live 在线尝试
- **来源**: Wi-Fi Alliance; Vanhoef Dragonblood
- **常见误用**: 假设 WPA3 是 silver bullet — 实际有 SAE-PT 修复前的 side-channel
- **Endorsement evidence**: (evidence: [T04-S013, T04-S014, T04-S015])

#### 💡 14. Roaming triangle: 802.11k + v + r

- **Tier**: tier-1
- **One-liner**: k 邻居告知 / v 网络辅助过渡 / r 快速密钥 — 三者结合让漫游 <50 ms
- **来源**: IEEE 802.11k/v/r; Microsoft Learn; Cisco docs
- **关联概念**: PMK caching / Opportunistic Key Caching (OKC) / 802.11w PMF
- **常见误用**: 只开 802.11r 不开 k/v — 漫游决策仍由客户端独立做，效果有限
- **Endorsement evidence**: (evidence: [T04-S039, T04-S040, T04-S012])

#### 💡 15. Hidden node / RTS-CTS / Virtual carrier sense (NAV)

- **Tier**: tier-2
- **One-liner**: 两个 STA 互相听不见但都听得见 AP，RTS-CTS 让 AP 协调
- **来源**: Gast ch.3; Bianchi 论文背景
- **常见误用**: 高密场景盲目开 RTS-CTS 反而增加 overhead
- **Endorsement evidence**: (evidence: [T04-S004, T04-S010])

#### 💡 16. TWT (Target Wake Time)

- **Tier**: tier-2
- **One-liner**: Wi-Fi 6 节电协议 — IoT 设备可以协商唤醒间隔
- **来源**: IEEE 802.11ax
- **常见误用**: 旧客户端不支持
- **Endorsement evidence**: (evidence: [T04-S041, T04-S042])

#### 💡 17. DCF / EDCA + QoS WMM

- **Tier**: tier-2
- **One-liner**: 基本接入函数（DCF）+ QoS 增强（EDCA, 4 access categories）+ WMM 标记
- **来源**: Gast ch.4; Bianchi
- **常见误用**: 不打 WMM 标签做 voice over Wi-Fi
- **Endorsement evidence**: (evidence: [T04-S004, T04-S010, T04-S012])

#### 💡 18. Captive portal / guest VLAN / NAC

- **Tier**: tier-2
- **One-liner**: 访客接入认证页 + VLAN 隔离 + 准入控制
- **来源**: CWSP; UniFi / Cisco / Aruba docs
- **常见误用**: 访客与员工 VLAN 不隔离
- **Endorsement evidence**: (evidence: [T04-S024])

#### 💡 19. Cell sizing + min RSSI threshold

- **Tier**: tier-2
- **One-liner**: 每 cell 物理半径 + 客户端最低信号门槛 — 典型 -67 dBm voice / -70 dBm data
- **来源**: CWDP; Cisco design guides; Ekahau
- **常见误用**: 数据网用 -85 dBm 阈值导致客户端粘住远 AP
- **Endorsement evidence**: (evidence: [T04-S023, T04-S043])

#### 💡 20. Tx power asymmetry / client transmit budget

- **Tier**: tier-2
- **One-liner**: AP 信号强不等于客户端能回包 — 客户端通常 Tx power 仅 14-18 dBm
- **来源**: vonNagy; Aruba design guides
- **常见误用**: AP 开到最大功率反而导致单向覆盖
- **Endorsement evidence**: (evidence: [T04-S029, T04-S001])

#### 💡 21. PoE budget + Class (af / at / bt)

- **Tier**: tier-2
- **One-liner**: AP 功耗等级（802.3af 15.4W / at 30W / bt 60-90W）决定交换机预算
- **来源**: IEEE 802.3; Ubiquiti docs
- **常见误用**: U7 Pro Max（802.3bt）插 af 交换机带不动
- **Endorsement evidence**: (evidence: [T04-S034])

#### 💡 22. Controller architecture: cloud / on-prem / embedded

- **Tier**: tier-2
- **One-liner**: Mist (pure cloud) vs UniFi (controller as software, can be embedded) vs Cisco WLC (on-prem appliance)
- **来源**: Mist docs; UniFi help; Cisco docs
- **常见误用**: 选 Ubiquiti 当 enterprise 因为便宜但不评估 telemetry 与 AI ops 缺口
- **Endorsement evidence**: (evidence: [T04-S037, T04-S034, T04-S041])

#### 💡 23. Predictive vs validation survey workflow

- **Tier**: tier-2
- **One-liner**: 模型 → 实测对比的闭环（design → install → validate → tune）
- **来源**: Ekahau; CWDP
- **常见误用**: 只做 predictive 然后跳过 validation
- **Endorsement evidence**: (evidence: [T04-S043, T04-S023])

#### 💡 24. Wi-Fi 7 MLO (Multi-Link Operation)

- **Tier**: tier-2
- **One-liner**: 客户端可同时使用 2.4/5/6 GHz 多链路传输
- **来源**: IEEE 802.11be; vendor early docs
- **常见误用**: 假设客户端支持 MLO — 当前 (2026-Q2) 支持的 client SoC 还少
- **Endorsement evidence**: (evidence: [T04-S012, T04-S042])

---

## Phase 2 提炼提示

### 反复出现 ≥ 3 个 canon 都讨论的核心 idea（候选行业心智模型）

- **「Capacity first, coverage second」**: vonNagy blog / CWDP / Geier ch.4 / NETGEAR HD WP / 多个 WLPC talks 都强调。 → 候选心智模型 #1（适用于本任务的 80 人办公室场景）
- **「Layered diagnosis: PHY → MAC → assoc → auth → IP」**: CWNA ch.13 / CWAP / Gast / UniFi support docs 反复用。 → 候选心智模型 #2（故障排除 SOP 的根原则）
- **「Client is the weakest link」**: CWDP / vonNagy / Aruba design guides / Apple Wi-Fi roaming doc 都强调。客户端能力 < AP 能力 → 设计要按 client 规划而非 AP 规划。 → 候选心智模型 #3
- **「Specs不替代measurement」**: Gast (帧分析) / CWAP / Ekahau workflows / WLPC 都强调。Vendor 文档说支持不等于实际能工作 — 必须抓包 + survey 验证。 → 候选心智模型 #4
- **「Vendor-neutral foundation, vendor-specific overlay」**: CWNP 体系本身就是这个论点；Ubiquiti / Cisco / Aruba / Mist 的 cert 都建议先 CWNA。 → 候选心智模型 #5（直接对应 Ubiquiti 工程师的成长路径建议）

### 智识谱系种子

- **流派 A — Standards-first (IEEE 中心)**: 奠基 IEEE 802.11 WG (1997)；当前代表 Matthew Gast (TGm chair), Eldad Perahia, Mark Hamilton, Stephen McCann。Track 01 应包含。
- **流派 B — Vendor-neutral certification (CWNP)**: 奠基 Devin Akin + Kevin Sandlin (CWNP 1999)；当前代表 David Coleman, David Westcott, Tom Carpenter, Bryan Harkins。Track 01 应包含 Coleman / Westcott / Akin / Parsons。
- **流派 C — Capacity-first design**: 奠基 Andrew vonNagy (~2010 Revolution Wi-Fi blog)；当前代表 vonNagy, Peter Mackenzie, Devin Akin, Joel Crane (Mist)。Track 01 应包含 vonNagy。
- **流派 D — AI-driven WLAN ops**: 奠基 Bob Friday + Sudheer Matta (Mist Systems 2014, acquired by Juniper 2019)；当前代表 Friday, Matta, Cloud-Wi-Fi 阵营。Track 01 应包含 Friday。
- **流派 E — Wireless security research**: 奠基 Arbaugh (802.11i)；当前代表 Mathy Vanhoef (KRACK + Dragonblood), Eyal Ronen, Wi-Fi Alliance Security WG。Track 01 应包含 Vanhoef。
- **主要分歧 (still-debated within the canon)**:
  - **AI-driven ops vs first-principles**: Mist 阵营 / Akin 私塾 分别强调"让 ML 找问题" vs "工程师必须懂底层" 
  - **Cloud-managed vs self-hosted**: Mist / Meraki vs UniFi / Cisco WLC — telemetry vs 控制权的权衡
  - **6 GHz adoption pace**: 监管 / 客户端支持速度仍在演进，2026 仍有保守派建议先稳 5 GHz
  - **WPA3 deployment readiness**: 客户端兼容性 vs 安全升级压力

### 核心概念 → 候选 playbook

- **「Client RSSI 满但慢」→ 检查 SNR + airtime utilization + retry%，不只看 RSSI**
- **「漫游慢导致 voice 掉话」→ 检查是否启用 802.11k + v + r 全套，不只 r**
- **「高密下吞吐崩」→ 检查 CCI（同信道 AP 数）+ channel width（80 → 40 → 20 MHz）+ min RSSI threshold**
- **「IoT 设备频繁掉线」→ 检查 PSK SSID 是否分离 + TWT 配置 + 频段（2.4 vs 5 GHz）**
- **「访客网络泄漏到内网」→ 检查 captive portal + guest VLAN 隔离 + DNS 隔离**
- **「设备说支持 Wi-Fi 6 但行为像 Wi-Fi 5」→ 抓包验证 PHY rate + MCS index，不信 vendor spec sheet**
- **「UniFi GUI 看起来正常但用户抱怨慢」→ 别只看 controller dashboard，做被动 survey + 抓包**

### 冷僻 / 信号薄弱

- 必读书 5 个（≥3） ✅ 
- paper / standard 7 个（≥5） ✅
- 课程 8 个（≥2） ✅
- 概念 24 个（≥15） ✅
- Endorsement evidence ≥ 3 处的项: 100% （所有 textbook / paper / course / concept 都有 ≥ 3 处独立 endorsement）✅
- 一手 endorsement（figures 直推 / 课程 syllabus）≥ 50%: 估算 ~70% （CWNP cert track + WLPC + 标准是 primary 一手）✅

**信号薄弱点**:
1. **中文圈 canon**: 中文环境下没有原生的 Wi-Fi engineering canon — 几乎所有 senior 都是消费英文一手材料。CWNA 有中文译本但版本通常滞后 1-2 代。**locale=global 是事实**，但 zh-CN 用户接触门槛是英文阅读能力。
2. **Ubiquiti-native canon 薄弱**: Ubiquiti 没有像 Cisco Press / Sybex 那样的体系化教材，仅有 vendor-native 短训（UEWA 2-day）。**这暗示 Ubiquiti 工程师如果想成长，必须借用 vendor-neutral 教材（CWNA + Gast + WLPC）**，纯靠 UniFi 文档无法成 engineer。
3. **Wi-Fi 7 教材尚未成熟**: 当前（2026-Q2）尚无 Wi-Fi 7 的 Sybex / O'Reilly 系统教材，CWNA-110 在开发中。Wi-Fi 7 章节目前依赖 IEEE 标准 + 厂商白皮书 + WLPC 演讲，textbook 维度待补。
4. **Gast 第三版缺位**: O'Reilly *802.11 Wireless Networks* 自 2005 年第 2 版后无更新。Matthew Gast 仍活跃于 802.11 WG，但没出新版书。这是 canon 的一个**结构性缺口** — 介于 CWNA（入门）和 IEEE 标准（无法直接读）之间的"工程化解读"层缺失。

### Wave 2 / 3 接力提示

- **Track 01 figures (Wave 2)**: 候选名单：Devin Akin / David Coleman / David Westcott / Keith Parsons / Andrew vonNagy / Matthew Gast / Peter Mackenzie / Bob Friday / Mathy Vanhoef / Sudheer Matta / Joel Crane / Lee Badman (wirednot) / Drew Lentz / Jerry Olla / Eddie Forero / Stephen McCann
- **Track 02 tools (Wave 2)**: 候选名单：Ekahau AI Pro + Sidekick 2 / iBwave / NetAlly EtherScope / Wireshark + airpcap / Metageek inSSIDer / Acrylic Wi-Fi / Wi-Fi Explorer / Ubiquiti UniFi Controller / Cisco DNA Center / Aruba Central / Mist cloud / Hamina / 7signal Sapphire / Cape Networks / Cisco Spectrum Expert
- **Track 03 workflows (Wave 3)**: capacity-first design workflow / predictive→validation survey loop / PHY→MAC→assoc→auth→IP layered diagnosis / WPA2/WPA3 migration workflow / 802.1X RADIUS rollout / high-density 80-人 office baseline / 6 GHz rollout decision tree

调研未超时；输出落地完整。
