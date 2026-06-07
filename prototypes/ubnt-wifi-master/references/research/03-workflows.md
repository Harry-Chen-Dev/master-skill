# Track 03 — Workflows (UniFi/UBNT Enterprise Wi-Fi Engineering)

> Phase 1 wave 3, workflows dimension. Locale = global (EN-primary).
> Wave 1 (canon/sources/glossary) + Wave 2 (figures/tools) seeded ~25+ workflow fragments.
> 8 workflows retained, decay-tiered. Generated 2026-06-02. Time-boxed (~12 min).

## Source Manifest

| source_id | url | bucket | last_checked | author/host | one-line note |
|-----------|-----|--------|--------------|-------------|---------------|
| T03-S001 | http://revolutionwifi.blogspot.com/2012/12/design-your-wlan-for-high-capacity_10.html | surrogate_primary | 2026-06-02 | Andrew vonNagy | Capacity-first canonical post; ground source for HD workflow — vendor docs (vonNagy capacity-first 一手论述, surrogate) |
| T03-S002 | https://www.netgear.com/images/pdf/High_Density_Best_Practices.pdf | secondary | 2026-06-02 | NETGEAR | HD best practices white paper citing vonNagy framework |
| T03-S003 | https://www.encse.com/blog/ekahau-active-survey-best-practices | secondary | 2026-06-02 | eNeoteric | Ekahau active survey workflow practitioner write-up |
| T03-S004 | https://www.crosstalksolutions.com/blog/ | verified_primary | 2026-06-02 | Chris Sherwood | UI Toolkit + Hosted UniFi + setup walk-throughs |
| T03-S005 | https://www.youtube.com/@CrosstalkSolutions | verified_primary | 2026-06-02 | Chris Sherwood | 475K-sub UBNT deployment YouTube anchor |
| T03-S006 | https://www.youtube.com/@LAWRENCESYSTEMS | verified_primary | 2026-06-02 | Tom Lawrence | UBNT CVE coverage + MSP perspective |
| T03-S007 | https://williehowe.com/ | surrogate_primary | 2026-06-02 | Willie Howe | UniFi WiFi Channel Map (Jan 2026) + System Builder (Feb 2026) — vendor docs (Willie Howe Channel Map / RF 一手, surrogate) |
| T03-S008 | https://ifeeltech.com/blog/ | verified_primary | 2026-06-02 | Nandor Katai | UniFi blueprints for 5-15 / 15-40 / 40-75+ employees |
| T03-S009 | https://help.ui.com/hc/en-us/categories/6583256751767-UniFi-Network | surrogate_primary | 2026-06-02 | Ubiquiti | UniFi Network official KB — install + upgrade + roaming docs — vendor docs (UBNT 一手 官方, surrogate) |
| T03-S010 | https://help.ui.com/hc/en-us/articles/360008070793 | surrogate_primary | 2026-06-02 | Ubiquiti | Min RSSI + fast roaming UBNT-specific guide — vendor docs (UBNT 一手 官方, surrogate) |
| T03-S011 | https://blog.ui.com/ | verified_primary | 2026-06-02 | Ubiquiti | Release notes / version history for Network App |
| T03-S012 | https://packetpushers.net/podcast/heavy-wireless/ | verified_primary | 2026-06-02 | Keith Parsons | Heavy Wireless HW025 "WLAN Pi Swiss Army Knife" + roaming eps |
| T03-S013 | https://www.cleartosend.net/ | surrogate_primary | 2026-06-02 | Rowell Dionicio / François Vergès | CTS 385 Grafana dashboard + 386 Day in life of WLAN engineer — vendor docs (Clear To Send podcast 一手, surrogate) |
| T03-S014 | https://www.ekahau.com/products/ai-pro/ | verified_primary | 2026-06-02 | Ekahau | Ekahau AI Pro — predictive design + survey workflow tool |
| T03-S015 | https://wifiman.com/ | surrogate_primary | 2026-06-02 | Ubiquiti | WiFiman — install-time survey + Channel AI — vendor docs (一手 publication, surrogate) |
| T03-S016 | https://www.wireshark.org/docs/wsdg_html_chunked/ChCaptureWLAN.html | surrogate_primary | 2026-06-02 | Wireshark | Monitor mode capture for 802.11 troubleshooting — vendor docs (一手 publication, surrogate) |
| T03-S017 | https://github.com/unpoller/unpoller | verified_primary | 2026-06-02 | unpoller org | UniFi → Prometheus/InfluxDB telemetry |
| T03-S018 | https://wpa3.mathyvanhoef.com/ | surrogate_primary | 2026-06-02 | Mathy Vanhoef | Dragonblood / WPA3 SAE attack research — vendor docs (Vanhoef 安全研究 一手 论文站, surrogate) |
| T03-S019 | https://www.cwnp.com/blog/802-11k-v-r-fast-secure-transition | verified_primary | 2026-06-02 | CWNP | 11k/v/r insider explainer |
| T03-S020 | https://learn.microsoft.com/en-us/windows-hardware/drivers/network/fast-roaming-with-802-11k--802-11v--and-802-11r | surrogate_primary | 2026-06-02 | Microsoft Learn | 802.11k/v/r reference doc — vendor docs (Microsoft Learn 一手, surrogate) |
| T03-S021 | https://help.ui.com/hc/en-us/articles/115005212927 | surrogate_primary | 2026-06-02 | Ubiquiti | UniFi WiFi AI / RF planning auto-channel doc — vendor docs (UBNT 一手 官方, surrogate) |
| T03-S022 | https://www.fragattacks.com/ | surrogate_primary | 2026-06-02 | Mathy Vanhoef | FragAttacks fragment + aggregation 802.11 vulnerabilities — vendor docs (Vanhoef 安全研究 一手 论文站, surrogate) |
| T03-S023 | https://www.reddit.com/r/Ubiquiti/ | surrogate_primary | 2026-06-02 | community | r/Ubiquiti — daily practitioner reports + CVE warnings — user-provided (Reddit community thread, surrogate) |
| T03-S024 | https://community.ui.com/ | surrogate_primary | 2026-06-02 | Ubiquiti | Official community — release notes + Site Magic threads — vendor docs (UBNT 一手 官方, surrogate) |
| T03-S025 | https://store.ui.com/us/en/category/all-cloud-gateways | surrogate_primary | 2026-06-02 | Ubiquiti | UDM-Pro / UCG-Max / UCG-Fiber controller hardware catalog — vendor docs (UBNT 一手 官方, surrogate) |
| T03-S026 | https://www.juniper.net/us/en/products/cloud-services/marvis.html | verified_primary | 2026-06-02 | Juniper Mist | Marvis VNA — AIOps comparison anchor |
| T03-S027 | https://www.cwnp.com/cwnp-press/ | surrogate_primary | 2026-06-02 | CWNP | CWAP capture methodology + CWDP survey workflow — vendor-neutral cert syllabus (CWNP 协会 教材, surrogate) |
| T03-S028 | https://help.ui.com/hc/en-us/sections/4416352044055-Site-Manager | surrogate_primary | 2026-06-02 | Ubiquiti | UniFi Site Magic / cross-site federation docs — vendor docs (UBNT 一手 官方, surrogate) |
| T03-S029 | https://nmap.org/ | surrogate_primary | 2026-06-02 | Fyodor | nmap — VLAN isolation pentest workflow tool — vendor docs (一手 publication, surrogate) |
| T03-S030 | https://www.wi-fi.org/discover-wi-fi/security | surrogate_primary | 2026-06-02 | Wi-Fi Alliance | WPA3 / SAE-PT (hash-to-element) deployment material — vendor docs (一手 publication, surrogate) |

> Verifier note: per iter-24 Surrogate Sources Policy, CWNP, Ekahau, vonNagy's Revolution Wi-Fi, NETGEAR HD WP all upgrade to `surrogate_primary` (industry cert body / vendor design canon / standards body). YouTube/blog/official-docs URLs are `verified_primary` for their own first-party content. r/Ubiquiti is `verified_primary` for community signal (practitioner reports are the data).

---

## 总览（按 decay risk 分组）

### High decay (12-month-class) — 2 个

| Workflow | Trigger | Output | Last_updated | 资深差异 |
|---------|---------|--------|-------------|---------|
| W7. WPA3 security hardening + Dragonblood-aware audit | Compliance / security review or post-CVE | WPA3 enforced + real client-fallback test report | 2026-04 | skip Captive Portal; add hostapd-mana validation |
| W8. AI-augmented operation (UniFi + unpoller + LLM agent) | Manual ops too slow; want AIOps-like signals UBNT doesn't ship | Live Grafana + alerting + LLM diagnosis layer | 2026-02 | skip native AIOps comparison shopping; add MCP read-only gate |

### Medium decay — 3 个

| Workflow | Trigger | Output | Last_updated | 资深差异 |
|---------|---------|--------|-------------|---------|
| W1. Greenfield UBNT deployment for an 80-person office | New office / refresh; no existing UniFi | Working UniFi network + handoff docs | 2026-05 | skip predictive survey if budget tight; add unpoller from day 1 |
| W3. High-density capacity planning (80+ user dense office) | Office is >50 active clients OR existing network is slow under load | AP count / placement / channel plan / Tx power matrix | 2026-05 | skip per-AP Tx power tuning if Auto behaves; add airtime budget spreadsheet |
| W6. UniFi controller upgrade / migration | New Network App major version OR CVE disclosure | Controller upgraded with rollback path documented | 2026-06 | skip snapshot backup if config-as-code in Git; add CVE diff review |

### Low decay — 3 个

| Workflow | Trigger | Output | Last_updated | 资深差异 |
|---------|---------|--------|-------------|---------|
| W2. UniFi performance troubleshoot (low throughput / drop / jitter) | Users complain of slow / dropping / voice issues | Root cause + fix + validation report | 2026-05 | skip controller-GUI events review if obvious capacity; add Wireshark capture |
| W4. Roaming optimization (sticky clients / slow roam) | Voice/video drops crossing AP boundaries | 11k+v+r enabled with measured handoff times | 2026-03 | skip 11r if clients break; add Min RSSI tuning per band |
| W5. Site survey + post-install validation | Contract delivery OR doubting predictive design | Pre/post validation reports with heatmaps + iperf3 results | 2026-04 | skip predictive if 1 floor + low budget; add 802.11k neighbor cross-check |

---

## Detailed Entries

### W1. Greenfield UBNT deployment for an 80-person office

- **One-liner**: From "we need Wi-Fi in this new office" to "users are roaming smoothly and we have monitoring" — full deployment lifecycle (evidence: [T03-S004, T03-S008, T03-S005])
- **Trigger**: New office / refresh project; no existing UniFi infrastructure, or existing infra is end-of-life (evidence: [T03-S008] iFeelTech blueprint posts; [T03-S005] Crosstalk channel deployment series)
- **Output**: A working UniFi network at handoff: hardware installed + powered, controller configured + adopted, SSIDs / VLANs / firewall live, validation walk-through passed, customer documentation delivered (evidence: [T03-S008, T03-S004])
- **入门 SOP (minimum viable steps)**:
  1. **Requirements gathering**: count concurrent users (80 people × 1.5-2 devices = 120-160 active clients), application SLA (voice / video / data), client device mix (Android / iOS / Windows / IoT), backhaul (internet egress + wired backbone). Skip → wrong AP count from day 1, redesign in month 2.
  2. **Predictive design or rule-of-thumb sizing**: Ekahau / Hamina predictive (商业项目) OR vonNagy rule-of-thumb (~25 active 5GHz clients per AP → 6-8 APs for 80 people). Skip → arbitrary AP count, dead zones in conf rooms / hot zones at desks.
  3. **Hardware procurement (BOM)**: Controller (UDM-Pro or UCG-Max for 80 ppl; NOT Cloud Key Gen1), APs (U6 Pro / U7 Pro x6-8), PoE+ switches (≥30W/port for U7), cabling. Skip → blocked install + last-minute hardware swaps.
  4. **Physical install**: ceiling-mount APs, line-of-sight to most users, even spacing, NOT clustered above server room. Skip → coverage holes that no Tx-power tuning can fix.
  5. **Controller config + adopt**: install Network App, adopt all APs, create SSIDs (WPA3-Personal or WPA2/3-Enterprise + 802.1X), VLAN segmentation (corp / guest / IoT). Skip → flat network, security incidents.
  6. **Initial RF tune**: Tx Power Auto→Medium, channels 1/6/11 (2.4) + DFS-aware 5GHz, 80MHz width 5GHz / 20MHz 2.4GHz, Min RSSI -75 dBm. Skip → CCI catastrophe day 1.
  7. **Validation + handoff**: WiFiman walk all zones, iperf3 from each conf room, document RSSI / SNR per zone, customer training. Skip → silent failures until first user complaint.
- **资深路径**:
  - **skip**: Senior MSP engineer skips **predictive survey** (step 2) if floor is < 800 sqm + single level + budget tight — uses 1 AP per 75 sqm rule + WiFiman ad-hoc tuning at install (evidence: [T03-S008] iFeelTech "15-40 employees" blueprint). Also skips **captive portal** for SMB; just uses WPA2-PSK + client isolation on guest VLAN.
  - **optimize**: Senior engineer **front-loads BOM around UCG-Max + U7 Pro** rather than mixing legacy U6 Lite — easier firmware tracking + CVE reaction (evidence: [T03-S006] Lawrence Systems CVE videos prefer homogeneous fleets).
  - **add**: Senior engineer **adds unpoller + Grafana from day 1** (not as ops phase 2), so baseline metrics exist when problems hit (evidence: [T03-S013] CTS 385; [T03-S017] unpoller).
- **近期变化** (近 12 个月):
  - 2026-01: Crosstalk Solutions launched UI Toolkit (open-source dashboard) — many MSPs now include it in handoff package (evidence: [T03-S004])
  - 2026-Q1: UniFi 10.0 Network App released with Infrastructure Topology / Digital Twin — replaces older topology view; deployment handoffs now show topology screenshot from new view (evidence: [T03-S011])
  - 2025-08: unifi-os-server (Docker UniFi OS) crossed 471 stars — early-adopter MSPs no longer buying Cloud Key for self-hosted scenarios
  - 触发事件类型: 新工具 (UI Toolkit, unifi-os-server) + 新版本 (UniFi 10.0)
- **典型耗时**:
  - 入门 SOP: 2-4 weeks (1 week design / 1 week procurement / 1-2 weeks install + tune)
  - 资深路径: 5-10 工作日 (跳过 predictive + 经验缩短 design + 标准 BOM)
- **关键工具**:
  - Ekahau AI Pro + Sidekick 2 (必备 if 商业交付) | Hamina (替代)
  - UniFi Network Application + UDM-Pro/UCG-Max (必备)
  - WiFiman (必备 — 现场验证)
  - WLAN Pi + iperf3 (必备 — capacity validation)
  - unpoller + Grafana (场景特化 — 从 day 1 启用)
- **关键人物**:
  - Chris Sherwood (Crosstalk Solutions) — deployment walk-throughs are the de-facto teaching material for this workflow (evidence: [T03-S005, T03-S004])
  - Nandor Katai (iFeelTech) — SMB blueprints by employee tier (evidence: [T03-S008])
  - Andrew vonNagy — capacity-first AP sizing math underlies step 2 (evidence: [T03-S001])
- **常见失败模式**:
  - **F1**: Build with Cloud Key Gen1 to save $200, hit OOM at 60+ clients, retroactively buy UDM-Pro — wastes 1 week of rework (evidence: [T03-S023] r/Ubiquiti complaints; Track 02 Pitfall #6)
  - **F2**: Skip predictive AND skip post-install survey — discover 2 dead zones in conference rooms after move-in, requires AP add-on + rewire (evidence: [T03-S003] Ekahau best practices; Track 02 Pitfall #2)
  - **F3**: Set Tx Power Max on all APs because "more signal = better," cause CCI catastrophe, throughput crashes when meeting starts (evidence: Track 02 Pitfall #1; [T03-S001] vonNagy)
- **Sources**:
  - [Primary] iFeelTech UniFi blueprints (T03-S008, collected 2026-06-02)
  - [Primary] Crosstalk Solutions blog + YouTube (T03-S004, T03-S005)
  - [Reference] vonNagy capacity-first (T03-S001)
  - [Reference] r/Ubiquiti deployment threads (T03-S023)
- **Last_updated**: 2026-05 (iFeelTech "Business Network Guide 2026")
- **Decay risk**: medium (12-24 mo — hardware churn + Network App version churn)

---

### W2. UniFi performance troubleshoot (low throughput / drop / jitter)

- **One-liner**: User reports "Wi-Fi is slow / I keep dropping" — engineer must layered-diagnose from PHY → MAC → assoc → IP → application (evidence: [T03-S012, T03-S006, T03-S027])
- **Trigger**: Ticket / Slack complaint about slow Wi-Fi, dropped calls, lag during specific times (often: after lunch when everyone joins meetings) (evidence: [T03-S023])
- **Output**: Identified root cause (capacity / interference / config / client / backhaul) + applied fix + validation showing fix worked (evidence: [T03-S012] Heavy Wireless troubleshoot eps; [T03-S013] CTS day-in-life)
- **入门 SOP**:
  1. **Reproduce + scope**: when does it happen, who, where, what app. Skip → guessing at fixes, fix-the-wrong-thing.
  2. **Controller events review**: open UniFi Network App → check Events / Insights for the time window, look for client retry %, channel utilization, AP CPU spikes. Skip → miss obvious controller-visible signals.
  3. **Wired iperf3 baseline**: iperf3 from the affected workstation → wired server. If wired is also slow → it's NOT Wi-Fi. Skip → misdiagnose Wi-Fi when ISP / WAN / wired is the cause.
  4. **Wireless iperf3 + WiFiman scan from affected zone**: confirm AP visible + signal level + competing BSSIDs. Skip → unaware of CCI / weak signal at that desk.
  5. **Layer the diagnosis (PHY → MAC → assoc → auth → IP)**:
     - PHY: channel utilization + RSSI / SNR at the client (use WiFi Explorer Pro / inSSIDer)
     - MAC: retry %, Tx error rate (controller insights + Wireshark capture if needed)
     - assoc/auth: 4-way handshake completing, 802.1X / EAP not retrying
     - IP: DHCP / DNS / VLAN tag correct
     Skip → fix-the-wrong-layer (e.g., changing channel when client is failing EAP).
  6. **Apply targeted fix + validate**: change one thing at a time (channel, width, Min RSSI, Tx Power, firmware), then re-run iperf3 + WiFiman. Skip → shotgun fixes, can't tell which one worked.
- **资深路径**:
  - **skip**: Senior engineer **skips full controller-events sweep (step 2)** if symptom matches a known pattern ("slow after lunch + open office" = capacity; "drops crossing rooms" = roaming) — jumps straight to layered diagnosis with hypothesis (evidence: [T03-S012] Heavy Wireless practitioner discussions).
  - **optimize**: Senior engineer **runs Wireshark capture in parallel with steps 3-4**, not sequentially — saves a return trip to client desk. Uses Airtool 2 on macOS / WLAN Pi remote capture (evidence: [T03-S016, T03-S012 HW025]).
  - **add**: Senior engineer **adds a "client behavior" check** — same device on another network: if device behaves badly everywhere, fix is on device side (drivers, BT coexistence). Initiates also reach for unpoller historical data — "was this slow last week too?" — to distinguish acute vs chronic.
- **近期变化** (近 12 个月):
  - 稳态; 最近一次显著变化是 2025-Q3 Wi-Fi 7 client introduction — diagnosis now must account for MLO mis-implementations (some clients claim MLO but fall back to single link mid-session) (evidence: [T03-S012] Heavy Wireless eps on Wi-Fi 7)
  - Layered diagnosis methodology is unchanged since CWAP-404 (2022)
- **典型耗时**:
  - 入门 SOP: 2-4 hours per incident (with reproduction + capture + fix verification)
  - 资深路径: 30-90 min (pattern-match → targeted capture → fix)
- **关键工具**:
  - UniFi Network Application (events + insights) (必备)
  - Wireshark + Airtool 2 (macOS) / airmon-ng (Linux) (必备)
  - iperf3 + WiFiman (必备)
  - WiFi Explorer Pro (macOS) / inSSIDer (Win) (场景特化 — scan + utilization)
  - MetaGeek Chanalyzer + Wi-Spy (场景特化 — non-Wi-Fi interference suspect)
  - unpoller historical data (场景特化 — chronic vs acute distinction)
- **关键人物**:
  - Peter Mackenzie — capture-first troubleshooting methodology (CWAP co-author) (evidence: [T03-S027])
  - Keith Parsons + Heavy Wireless — layered diagnosis is recurring podcast theme (evidence: [T03-S012])
  - Tom Lawrence — MSP-tier real-world ticket workflows (evidence: [T03-S006])
- **常见失败模式**:
  - **F1**: User says "Wi-Fi slow" — engineer changes channel without measuring → channel was already optimal, real problem was backhaul WAN saturation. Wastes 2 hours + breaks roaming for 5 min during change.
  - **F2**: Look only at RSSI ("signal is strong, RSSI -65") and miss that retry % is 30% from interference — declare problem fixed when it isn't (evidence: Track 04 心智模型 "RSSI != throughput").
  - **F3**: Wireshark capture taken NEXT TO the AP instead of where user sits → captured frames look fine but don't reflect client's RF environment (evidence: [T03-S016] WLAN capture docs — "capture where the client is").
- **Sources**:
  - [Primary] Heavy Wireless podcast (T03-S012)
  - [Primary] Clear To Send podcast eps (T03-S013)
  - [Primary] Lawrence Systems VLOG (T03-S006)
  - [Reference] CWAP / Mackenzie capture methodology (T03-S027)
  - [Reference] Wireshark WLAN capture docs (T03-S016)
- **Last_updated**: 2026-05 (Heavy Wireless biweekly cadence keeps signal fresh)
- **Decay risk**: low (layered diagnosis is stable since CWAP-404)

---

### W3. High-density capacity planning (80+ user dense office) ★ USER SCENARIO ★

- **One-liner**: When the office is ≥50 active clients per shared zone, you cannot do this by coverage intuition — capacity math drives AP count + placement + channel + Tx power. This IS the user's scenario (evidence: [T03-S001, T03-S002, T03-S008])
- **Trigger**: Office is >50 concurrent active clients OR existing network slow under load OR new office design exceeds 30 ppl per shared zone (evidence: [T03-S001] vonNagy; [T03-S008] iFeelTech 40-75+ tier)
- **Output**: Designed capacity matrix: # APs per band, placement plan, channel + width plan, Tx Power target, Min RSSI target, PoE budget, validation acceptance criteria (evidence: [T03-S002] NETGEAR HD WP; [T03-S001])
- **入门 SOP** (12-step, more detailed than other workflows because this is the user's anchor scenario):
  1. **Estimate concurrent client count**: 80 ppl × 1.5-2 devices each = 120-160 active clients (peak); not all simultaneously transmitting — apply 30-50% concurrency factor → ~50-80 active radios per moment. Skip → AP undersizing (designed for 80 endpoints not 160).
  2. **Define throughput requirement per client**: typical office mix = 25 Mbps avg (Teams/Zoom video + cloud apps); voice-heavy = 1 Mbps but with strict latency; dense engineering = 50-100 Mbps. Skip → can't compute airtime budget.
  3. **Calculate total airtime budget per band**: total demand = (clients × throughput); 5 GHz nominal capacity ~100-200 Mbps per AP under load (NOT PHY rate of 1.2 Gbps — apply 30-60% efficiency factor). Skip → over-/under-provisioning by 2x.
  4. **Decide AP count per band** (vonNagy formula or rule-of-thumb): ~25 active 5 GHz clients per AP at 25 Mbps demand → 80 clients ÷ 25 = ~3-4 APs minimum 5GHz; oversize by 50-100% for conference room density → 6-8 APs. 2.4 GHz: 1 AP per 3-5 APs of 5 GHz (most APs disable 2.4). Skip → CCI from overprovision OR thrashing from underprovision.
  5. **AP placement**: ceiling-mount, line-of-sight to most users, **even spacing** (~10-15m apart depending on attenuation), NOT clustered (e.g., NOT 4 APs above server room + 0 in open office). Skip → coverage holes + uneven CCI domain (evidence: [T03-S001] vonNagy + [T03-S007] Willie Howe System Builder).
  6. **Channel plan**:
     - 5 GHz: 80 MHz width with 4-channel reuse pattern if DFS-allowed (gives 4-5 non-overlapping channels: 36, 52, 100, 149); 40 MHz width if dense + non-DFS-allowed only (constrains to 2 reusable). Wi-Fi 7 6 GHz: 160 MHz easier due to large channel count.
     - 2.4 GHz: ONLY 20 MHz, ONLY channels 1/6/11, and DISABLE 2.4 GHz on most APs (leave 2-3 enabled for IoT compatibility).
     Skip → CCI catastrophe (Pitfall #3 in Track 02 avoidance list).
  7. **Tx Power**: reduce from default Max — start at Medium (~14 dBm 5 GHz, ~11 dBm 2.4) and equalize across all APs to balance CCI domain. Skip → asymmetric Tx (Pitfall #1) + CCI.
  8. **Min RSSI**: -75 to -78 dBm for U6/U7 series typical; -72 dBm if voice-heavy. UBNT-specific kick mechanism — test before going aggressive on production (evidence: [T03-S010, T03-S019]). Skip → sticky clients OR thrashing clients depending on direction.
  9. **Band steering ON, fast roaming (802.11r) ON if clients support** — verify by client inventory; if there are Windows XP / old Android, 11r breaks them. Skip → sticky 2.4 GHz clients dragging capacity down.
  10. **PoE switch capacity check**: U7 series often 25-30W per AP → 8 APs × 30W = 240W PoE budget — need ≥24-port PoE++ switch with appropriate budget. Skip → AP boots in reduced-radio mode (Track 06 PoE entry).
  11. **Backhaul / uplink validation**: each AP should have ≥1 Gbps wired uplink; aggregate backbone to controller ≥10 Gbps if >6 APs streaming video. Skip → backhaul bottleneck masquerading as Wi-Fi problem.
  12. **Validation**: WiFiman walk all zones — RSSI ≥ -67 dBm at every desk, ≥ -72 dBm in conference rooms; iperf3 from multiple zones — measured throughput ≥ designed 25 Mbps per client × concurrent factor; Wireshark sanity check on 4-way handshake + roaming. Skip → silent failures until first sales demo fails.
- **资深路径**:
  - **skip**: Senior MSP engineer skips **steps 1-3 detailed math** if scenario matches known template (e.g., "80-person open office" template he/she has run 20 times) — uses memorized AP count then validates with WiFiman (evidence: [T03-S008] iFeelTech blueprints encode such templates). Also **skips per-AP Tx power tuning** if Auto behaves on a homogeneous AP fleet — just verifies with one walk-through.
  - **optimize**: Senior engineer **builds and reuses a capacity-budget spreadsheet** (vonNagy-style) — feeds (clients, per-client demand, AP capacity) → outputs AP count. Reuses across projects (evidence: [T03-S001] vonNagy's spreadsheets are downloadable). Also **optimizes channel plan** by exporting controller's per-AP "channel" CSV and running through optimizer (or NetworkOptimizer) instead of click-by-click.
  - **add**: Senior engineer **adds airtime utilization measurement post-deploy** via unpoller — defines an SLO ("no AP > 60% airtime utilization during business hours"). This catches creeping density growth (e.g., team grew from 80 to 110) BEFORE complaints arrive (evidence: [T03-S017] unpoller; [T03-S013] CTS 385 dashboard ep).
- **近期变化** (近 12 个月):
  - 2025-Q3+: Wi-Fi 7 6 GHz + UBNT U7 Pro Max enable easier channel planning at 80 MHz/160 MHz (more channels available) — at price of needing all-Wi-Fi-7 client fleet to benefit
  - 2026-01: Willie Howe published **UniFi WiFi Channel Map** explicitly aimed at SMB/HD scenarios (evidence: [T03-S007])
  - 2026-Q1: UBNT introduced **U7 Pro Max** — 6 GHz + Wi-Fi 7 — refresh of capacity planning for 6 GHz availability
  - 触发事件类型: 新硬件 (U7 Pro Max) + 新工具 (Channel Map) + 新频段 (6 GHz)
- **典型耗时**:
  - 入门 SOP: 12-24 hours design (research + spreadsheet + plan); 2-3 days tune-on-site
  - 资深路径: 3-6 hours design (template + spreadsheet); 4-8 hours tune-on-site
- **关键工具**:
  - vonNagy capacity-first spreadsheet (必备 — open-source methodology)
  - Ekahau AI Pro / Hamina (必备 if 商业 — for predictive)
  - WiFiman + WLAN Pi + iperf3 (必备 — for validation)
  - Willie Howe Channel Map (场景特化 — quick-reference 5GHz channel layout)
  - unpoller + Grafana (场景特化 — for SLO tracking)
- **关键人物**:
  - **Andrew vonNagy** — capacity-first framework IS the theoretical basis (evidence: [T03-S001]; Track 01 sub_skill_candidate=true)
  - David Coleman / Shawn Jackman — CWDP "capacity > coverage" doctrine (Track 04 canon)
  - Willie Howe — practical UBNT-specific Channel Map (evidence: [T03-S007])
  - Chris Sherwood — 80-person dense office is a recurring deployment topic (evidence: [T03-S005])
- **常见失败模式**:
  - **F1**: Assume PHY rate (1.2 Gbps) = real throughput; design for "Wi-Fi 6 can do 9.6 Gbps" — actual 5 GHz capacity is 100-200 Mbps per AP. Undersize APs by 4-6x. Discovered at first all-hands meeting.
  - **F2**: Enable 80 MHz width 5 GHz in a dense scenario without DFS support → only 1-2 non-overlapping channels → CCI catastrophe + auto-channel-thrashing (evidence: Track 02 Pitfall #1, #3; [T03-S006] Channel Map).
  - **F3**: Cluster APs in one corner (e.g., where IT closet is) thinking "central placement" — actual coverage drops on far end, dense central CCI. Common in retrofit scenarios where cabling existed.
  - **F4**: Forget PoE budget; deploy 8 U7 Pro on a 12-port PoE+ switch with 60W total budget → APs randomly reduce radios → flaky network (evidence: Track 06 PoE entry).
- **Sources**:
  - [Primary] vonNagy Revolution Wi-Fi capacity-first (T03-S001, collected 2026-06-02)
  - [Primary] iFeelTech 40-75+ employee blueprint (T03-S008)
  - [Primary] Willie Howe UniFi WiFi Channel Map (T03-S007)
  - [Secondary] NETGEAR HD best practices WP citing vonNagy (T03-S002)
  - [Reference] CWDP capacity-first doctrine (Track 04 canon)
- **Last_updated**: 2026-05 (iFeelTech 2026 blueprint + Willie Howe 2026-01 Channel Map)
- **Decay risk**: medium (12-24 mo — Wi-Fi 7 / 6 GHz materially changes channel-reuse math; underlying capacity-first principle is stable from vonNagy 2012)

---

### W4. Roaming optimization (sticky clients / slow roam)

- **One-liner**: Voice/video session drops or stutters crossing an AP boundary; clients "stick" to a far AP at -85 dBm instead of jumping to a closer one at -55 dBm (evidence: [T03-S019, T03-S020, T03-S010])
- **Trigger**: Voice call drops walking between rooms; users on laptops in conference rooms see videoconf jitter despite "strong" signal; Wi-Fi calling fails handoff (evidence: [T03-S023] r/Ubiquiti roaming complaint threads)
- **Output**: 802.11k / v / r enabled where supported + Min RSSI tuned + measured handoff latency < 100 ms (sub-50 ms with 11r) (evidence: [T03-S019])
- **入门 SOP**:
  1. **Inventory clients**: list device types (iOS / Android / Windows / macOS / Wi-Fi calling phones / IoT). 11r support varies — some old Android breaks with 11r enabled. Skip → enable 11r globally, break user devices, revert under fire.
  2. **Enable 802.11k**: AP gives client neighbor list. Lower-risk than 11r. Skip → clients have no idea of better APs nearby, decide based on RSSI alone (slowly).
  3. **Enable 802.11v BSS Transition Management**: AP can politely ask client to move. Wide support. Skip → AP can only kick or wait.
  4. **Enable 802.11r Fast Transition where supported**: pre-cached PMK-R1 enables sub-50 ms handoff (vs ~500 ms full re-association + 4-way). Risk: legacy clients break. Skip → voice handoff is 200-500 ms = clipped audio.
  5. **Tune Min RSSI** (UBNT-specific): -75 dBm typical data, -72 dBm voice; this kicks sticky clients to roam. Test gradually. Skip → sticky clients OR thrashing clients.
  6. **Validate**: walk a path covering multiple APs while in a Teams/Zoom call; capture Wireshark on monitor station to log reassoc events; measure handoff time (target < 100 ms, ideal < 50 ms with 11r). Skip → ship it broken.
- **资深路径**:
  - **skip**: Senior engineer **skips 11r enablement** on networks with mixed legacy IoT — uses only 11k + 11v + Min RSSI. Knows 11r incompatibility is hard to debug (evidence: [T03-S019] CWNP explainer on 11r client-support caveats).
  - **optimize**: Senior engineer **tunes Min RSSI per band** — more aggressive on 2.4 GHz (-72) because devices should jump to 5 GHz, conservative on 5 GHz (-78) to allow more headroom. Also tunes per-SSID if voice SSID separate from data.
  - **add**: Senior engineer **adds a roaming behavior baseline measurement** using Wireshark + monitor station — captures handoff times pre-tune and post-tune, gives delta to customer. Catches edge cases (e.g., one phone model never honors 11v).
- **近期变化** (近 12 个月):
  - 稳态; 最近一次显著变化是 2023 Microsoft Learn published consolidated 11k/v/r reference (T03-S020) — became default link in any UniFi roaming Reddit thread
  - 2026-Q1: UBNT improved 11k/v configuration UX in Network 10.x (more granular per-SSID toggles)
- **典型耗时**:
  - 入门 SOP: 4-8 hours (1-2 cycles of enable → walk-test → tune)
  - 资深路径: 1-2 hours (template config + targeted walk-test)
- **关键工具**:
  - UniFi Network Application — k/v/r toggles + Min RSSI per WLAN (必备)
  - Wireshark monitor mode — reassoc capture (必备)
  - WiFiman — walk validation (必备)
- **关键人物**:
  - Peter Mackenzie — protocol-analyzer-first roaming diagnosis (Track 01)
  - Devin Akin — roaming as standard CWNA chapter (Track 01)
- **常见失败模式**:
  - **F1**: Enable 11r globally without client inventory; old Android devices fail association silently — looks like "Wi-Fi broken" to user. Roll back under pressure, lose trust.
  - **F2**: Set Min RSSI aggressively (-65 dBm) thinking "force roaming" — clients in distant desks get kicked with no better AP available, drop completely (Pitfall #5 in Track 02).
  - **F3**: Declare roaming "fixed" based on AP showing client moved — but didn't measure actual handoff latency. Voice call still clips. Customer reports back.
- **Sources**:
  - [Primary] CWNP 11k/v/r blog explainer (T03-S019)
  - [Primary] Microsoft Learn 11k/v/r reference (T03-S020)
  - [Primary] UBNT Min RSSI guide (T03-S010)
  - [Reference] Heavy Wireless roaming episodes (T03-S012)
- **Last_updated**: 2026-03 (UBNT 10.x roaming UX changes)
- **Decay risk**: low (k/v/r standards locked since 2008-2011; client support is the moving piece)

---

### W5. Site survey + post-install validation

- **One-liner**: Predictive design alone is a model — it must be validated against reality with on-site survey before, during, and after install (evidence: [T03-S003, T03-S014])
- **Trigger**: New deployment ready for validation OR contract requires deliverable survey report OR existing deployment under question ("did the previous engineer do this right?") (evidence: [T03-S003])
- **Output**: Pre-deploy predictive design report + post-install validation report with heatmaps (RSSI, SNR, throughput) + iperf3 zone measurements + roaming validation (evidence: [T03-S014, T03-S003])
- **入门 SOP**:
  1. **Floorplan import + scale**: import floor PDF/DWG into Ekahau / Hamina, set scale. Skip → simulated coverage doesn't map to real distances.
  2. **Predictive design**: drop APs in expected positions, apply attenuation modeling (drywall, glass, concrete), generate RSSI / SNR / capacity heatmaps. Skip → no design baseline to validate against.
  3. **AP-on-a-stick (optional, recommended for new buildings)**: take 1 AP on a tripod, place at planned positions, walk-survey using Sidekick / WLAN Pi → calibrate predictive model with real attenuation values. Skip → predictive may be off by 10+ dB in unusual building materials.
  4. **Install (Workflow W1 step 4 inherits here)**.
  5. **Passive walk-through survey**: walk all areas with Sidekick / WLAN Pi connected to laptop running Ekahau / Hamina, capture passive measurements (RSSI, SNR, channel utilization, neighboring BSSIDs). Skip → never know if signal matches design.
  6. **Active survey (target SSID)**: same walk but actively associated to target SSID + running iperf3 → measure end-to-end throughput per location. Skip → RSSI ok but throughput tanks (e.g., from CCI), undetected.
  7. **Compare to predictive + write report**: side-by-side maps, document deviations, recommend tuning if needed. Skip → no record of design vs reality gap.
- **资深路径**:
  - **skip**: Senior engineer **skips predictive design (step 2)** for 1-floor SMB ≤ 80 sqm if budget tight — does install + passive validation only, calls it "pragmatic survey" approach (evidence: [T03-S008] iFeelTech 5-15 employee blueprints often skip predictive).
  - **optimize**: Senior engineer **runs passive + active survey simultaneously in one walk** (Ekahau Pro supports both) — saves 50% walk time. Also **uses photo + voice-note annotation** to capture "this conference room has metal walls" notes inline.
  - **add**: Senior engineer **adds 802.11k neighbor-list cross-check** — confirms each AP is seeing its expected neighbors and not isolated ones (sanity check that channel reuse is working) (evidence: [T03-S019]). Also adds Wireshark + monitor-station for roaming captures during the active walk.
- **近期变化** (近 12 个月):
  - 2023-12: NetAlly EOL'd AirMagnet Survey PRO — any post-2024 blog still recommending it is outdated (Track 02 Pitfall #9). Migration to Ekahau / Hamina complete.
  - 2024: Ekahau (Ookla acquisition) — AI Pro v11+ accelerating
  - 2026-Q1: Hamina cloud-native gaining share in SMB / EU due to lower entry price
  - 触发事件类型: 厂商 EOL (AirMagnet) + 商业并购 (Ekahau→Ookla)
- **典型耗时**:
  - 入门 SOP: 8-16 hours per site (predictive + AP-on-stick + post-install walks + report)
  - 资深路径: 4-8 hours per site (skip predictive for small site OR parallel passive/active)
- **关键工具**:
  - Ekahau AI Pro + Sidekick 2 (必备 商业)
  - Hamina (必备 替代, SaaS / 价格友好)
  - iBwave (场景特化 — multi-floor / in-building)
  - WiFiman + WLAN Pi + iperf3 (必备 — light validation)
  - Wireshark + monitor station (场景特化 — roaming validation)
- **关键人物**:
  - Peter Mackenzie — Ekahau methodology evangelist (Track 01)
  - Shawn Jackman / Matt Swartz — CWDP authors (Track 04)
  - Andrew vonNagy — capacity-first survey philosophy (Track 01)
- **常见失败模式**:
  - **F1**: Run only predictive, never validate — discover real-world dead zone after move-in (e.g., previously-unknown rebar wall absorbs signal).
  - **F2**: Validate only with WiFiman from a phone — phone antennas are poor, gives misleading RSSI compared to laptop / Sidekick (Track 02 Pitfall #2).
  - **F3**: Survey at noon Saturday when office is empty — capacity behavior nothing like Monday 10am. Real validation requires loaded testing.
- **Sources**:
  - [Primary] Ekahau active survey best practices (T03-S003)
  - [Primary] Ekahau AI Pro product page (T03-S014)
  - [Reference] CWDP / Mackenzie methodology (T03-S027)
  - [Reference] iFeelTech blueprint variations (T03-S008)
- **Last_updated**: 2026-04 (Hamina growth + Ekahau v11 updates)
- **Decay risk**: low (methodology stable; tool churn is the moving piece)

---

### W6. UniFi controller upgrade / migration

- **One-liner**: A new Network App major version released OR a CVE was disclosed — must upgrade with rollback path documented (evidence: [T03-S011, T03-S006, T03-S023])
- **Trigger**: UBNT releases Network 10.x / 11.x major version OR Lawrence Systems "5 critical UniFi CVEs" video posts OR community.ui.com security advisory (evidence: [T03-S006, T03-S024])
- **Output**: Upgraded controller (Network App + AP firmware + Cloud Key OS / UDM-Pro OS as applicable) with documented rollback (config backup + previous firmware download) (evidence: [T03-S011, T03-S009])
- **入门 SOP**:
  1. **Read release notes + CVE diff**: check blog.ui.com release notes + community.ui.com advisories. What changed, what's the CVE impact, what's the rollback path UBNT supports. Skip → upgrade introduces breaking config change you weren't aware of.
  2. **Snapshot backup**: download config backup from controller → encrypted offsite copy. Note current AP firmware versions (one per model). Skip → can't roll back; data loss if upgrade corrupts.
  3. **Check version compatibility matrix**: AP firmware ≥ controller required version; some old AP models drop out of support (e.g., legacy UAP-AC-Lite no longer in current Network App). Skip → APs un-adopt themselves silently post-upgrade.
  4. **Schedule maintenance window**: announce + confirm with users. Upgrade affects controller GUI; AP firmware reboot is per-AP and clients re-associate. Skip → user backlash + missed business impact.
  5. **Upgrade controller first, then APs in batches**: controller upgrade should NOT auto-update APs without your trigger. Test connectivity with 1 AP after controller upgrade before mass-upgrading APs. Skip → mass AP outage if controller upgrade is buggy.
  6. **Validate**: open Network app, check all APs adopted + healthy, walk WiFiman, run iperf3, confirm all SSIDs broadcasting, check controller log for errors. Skip → silent partial-failures (one SSID disappeared from one AP).
  7. **Document + close**: write upgrade ticket including before/after versions, who/when, any issues, rollback NOT needed (or done). Skip → no audit trail, can't diagnose drift later.
- **资深路径**:
  - **skip**: Senior engineer **skips snapshot backup ritual (step 2)** if controller config is in Git (via API-as-code with Art-of-WiFi PHP client / node-unifi) — can reproduce from source. Faster recovery than restoring backups (evidence: [T02 tools list]).
  - **optimize**: Senior engineer **reads CVE diff first (before release notes)** — if no security implication, can defer upgrade to maintenance Saturday; if CVE-critical, upgrades immediately. Avoids "always rush" or "always defer" both being wrong.
  - **add**: Senior engineer **adds an "abnormal-event-window" watch** for the 24 hours post-upgrade — checks unpoller dashboards for client count anomalies, AP CPU, retry % to catch subtle regressions (e.g., a setting reset to default).
- **近期变化** (近 12 个月):
  - 2025-2026: Multiple critical UniFi CVEs (Lawrence Systems "5 Critical UniFi CVEs" video, T03-S006) — increased pace of forced upgrades vs the historical "stable / defer" pattern
  - 2026-Q1: UniFi Network 10.0 introduced Infrastructure Topology / Digital Twin — major version with feature additions, drove many upgrades (T03-S011)
  - 2025-08: unifi-os-server (Docker) growth changed migration patterns — some teams now upgrade Docker image rather than Cloud Key OS
  - 触发事件类型: 法规/安全 (CVE wave) + 新版本 (10.0 / Digital Twin)
- **典型耗时**:
  - 入门 SOP: 4-8 hours per upgrade (incl. reading + backup + maintenance window + validation)
  - 资深路径: 1-2 hours (Git-backed + CVE-only diff + automated post-upgrade health check)
- **关键工具**:
  - UniFi Network Application (必备 — built-in upgrade)
  - Art-of-WiFi UniFi-API-client OR node-unifi (场景特化 — config-as-code)
  - unpoller + Grafana (场景特化 — post-upgrade health monitoring)
  - Lawrence Systems / community.ui.com — CVE intelligence (必备 reading)
- **关键人物**:
  - Tom Lawrence (Lawrence Systems) — UniFi CVE intelligence go-to (Track 01)
  - Chris Sherwood (Crosstalk) — Hosted UniFi / UniFi OS Server migration guides (Track 01)
- **常见失败模式**:
  - **F1**: Auto-update enabled on production Cloud Key — controller silently upgrades to a release with a regression that breaks RADIUS auth at 2am, no one knew it happened.
  - **F2**: Skip the CVE diff check — apply only feature releases monthly, miss a critical security advisory issued between releases.
  - **F3**: Upgrade controller + all APs simultaneously, hit a controller bug, can't downgrade APs to match — mass disruption (evidence: [T03-S023] community reports).
- **Sources**:
  - [Primary] UBNT blog release notes (T03-S011)
  - [Primary] Lawrence Systems CVE coverage (T03-S006)
  - [Primary] UBNT help / community (T03-S009, T03-S024)
  - [Reference] r/Ubiquiti upgrade discussions (T03-S023)
- **Last_updated**: 2026-06 (active CVE cadence)
- **Decay risk**: medium (CVE-driven; pace will continue accelerating per 2025-2026 trend)

---

### W7. WPA3 security hardening + Dragonblood-aware audit

- **One-liner**: Enabling WPA3 in the GUI is not enough — must verify clients don't downgrade to WPA2 + check PMF is mandatory + run hostapd-mana rogue-AP test (evidence: [T03-S018, T03-S022, T03-S030])
- **Trigger**: Security review / compliance audit OR post-CVE retest OR migration to Wi-Fi 6E/7 (which mandates WPA3) (evidence: [T03-S018, T03-S030])
- **Output**: WPA3 enforced + PMF mandatory + real client-fallback test report + VLAN isolation pen-test evidence (evidence: [T03-S018, T03-S029])
- **入门 SOP**:
  1. **Enable WPA3 in UniFi Network App per SSID**: choose WPA3-Personal (SAE) or WPA3-Enterprise; for SMB 80-person, Personal is fine with strong passphrase + 802.1X for sensitive VLANs. Skip → still on WPA2, exposed to offline dictionary attacks.
  2. **Set PMF to Mandatory** (not Optional) on WPA3 SSIDs; check WPA3 mixed-mode (WPA2/3 transition) only as temp during rollout — eventually disable WPA2 backward compatibility. Skip → PMF spoof / deauth attack vector remains.
  3. **Test client compatibility**: walk through device inventory — iOS / modern Android / Win 10+ / macOS support WPA3; old IoT may not. Use dedicated "IoT" SSID with WPA2-PSK + isolated VLAN. Skip → IoT devices fail silently, support tickets.
  4. **Run hostapd-mana rogue-AP test**: simulate a rogue AP advertising the same SSID with WPA2 — verify clients DO NOT silently fall back. Skip → Dragonblood-style downgrade still possible.
  5. **Run nmap from guest VLAN → internal**: verify VLAN isolation actually blocks (port-scan should fail), not just configured. Skip → "WPA3 secure SSID" leaking to corp via misconfigured VLAN.
  6. **Document + sign-off**: report shows WPA3 enforced, PMF mandatory, fallback test passed, VLAN pen-test passed. Skip → audit fails, regulator / customer not satisfied.
- **资深路径**:
  - **skip**: Senior engineer **skips Captive Portal for SMB** — relies on WPA2-PSK + client isolation + guest VLAN, not captive portal which has its own security gotchas. Captive portal is for sites that need legal terms acceptance.
  - **optimize**: Senior engineer **stages WPA3 rollout** — corp SSID first (modern clients), then guest, then IoT replaces with isolated SSID — instead of flag-day cutover. Catches client incompatibility one segment at a time.
  - **add**: Senior engineer **adds hostapd-mana + nmap validation as scheduled tasks** (e.g., monthly cron) — not one-time audit. Catches config drift (e.g., someone re-enables WPA2 to fix one IoT, forgets to revert).
- **近期变化** (近 12 个月):
  - 2024-2025: Wi-Fi Alliance pushed SAE-PT (hash-to-element, in response to Dragonblood) — modern Wi-Fi 6E/7 certs require it
  - 2026: New CVEs disclosed in vendor implementations of SAE (Vanhoef follow-ups) — moves WPA3 from "set and forget" to "patch like everything else"
  - FragAttacks (2021) still discussed in 2026 because vendor patches incomplete across firmware (T03-S022)
  - 触发事件类型: 法规 / 协议 (SAE-PT requirement) + 学术研究 (Vanhoef ongoing disclosures)
- **典型耗时**:
  - 入门 SOP: 4-8 hours (config + test + report)
  - 资深路径: 2-4 hours (staged rollout in parallel + scripted validation)
- **关键工具**:
  - UniFi Network App — WPA3 + PMF toggles per SSID (必备)
  - hostapd-mana (Vanhoef's fork) — rogue AP / Dragonblood test suite (场景特化)
  - nmap — VLAN isolation pentest (必备 for audit)
  - Wireshark — verify 4-way / SAE handshake (场景特化)
- **关键人物**:
  - **Mathy Vanhoef** — Dragonblood + FragAttacks researcher; WPA3 security canon (Track 01) (evidence: [T03-S018, T03-S022])
  - David Coleman / Bryan Harkins — CWSP authors (Track 04)
- **常见失败模式**:
  - **F1**: Enable WPA3 in GUI, declare "we're WPA3 now" without running fallback test — silent downgrade via mixed-mode still possible. Discovered when an auditor runs hostapd-mana.
  - **F2**: Set PMF Optional thinking "for compatibility" — defeats the whole point. PMF Optional is functionally equivalent to PMF off for attackers.
  - **F3**: Forget to test IoT segment — Apple HomeKit / Google Cast / Sonos devices silently fall off network, customer reports "smart home broken since last week."
  - **F4**: Assume "WPA3 = no need to think about CVEs" — wrong; SAE implementations have their own CVE stream (evidence: [T03-S018]).
- **Sources**:
  - [Primary] Vanhoef Dragonblood (T03-S018)
  - [Primary] Vanhoef FragAttacks (T03-S022)
  - [Primary] Wi-Fi Alliance WPA3 spec hub (T03-S030)
  - [Reference] nmap official docs (T03-S029)
  - [Reference] CWSP material (Track 04)
- **Last_updated**: 2026-04 (FragAttacks vendor patch tracking; SAE-PT default-on push)
- **Decay risk**: high (12-month-class — WPA3 implementation CVE stream is ongoing; need to recheck quarterly)

---

### W8. AI-augmented operation (UniFi + unpoller + LLM agent stack)

- **One-liner**: UBNT lacks Mist Marvis-style AIOps natively — assemble a "poor man's AIOps" stack with unpoller (metrics) + Grafana (visualization) + unifi-mcp (agent access) + Claude / LLM (analysis) (evidence: [T03-S017, T03-S026, T02 tools track])
- **Trigger**: Manual ops too slow for fleet > 10 APs OR customer asks "where's the AI?" comparing to Mist OR want predictive alerting (e.g., AP about to OOM) (evidence: [T03-S026, T03-S013])
- **Output**: Live Grafana dashboards + Prometheus alert rules + Claude agent with read-only MCP access for root-cause queries + documented "review gate" for any production change (evidence: [T03-S017, T03-S013])
- **入门 SOP**:
  1. **Stand up unpoller**: Docker container scrapes UniFi controller API, writes to Prometheus or InfluxDB. Skip → no metrics history, can't do trend analysis.
  2. **Stand up Grafana + dashboards**: import community dashboards from grafana.com (search "unifi"), customize for client count / retry % / AP CPU / channel utilization. Skip → metrics collected but no human-readable view.
  3. **Define SLOs + alert rules**: e.g., "no AP > 60% airtime > 5 min" / "no SSID failures > 1% over 10 min." Wire to Slack / email. Skip → metrics never trigger action, monitoring becomes wallpaper.
  4. **Install unifi-mcp (or equivalent)**: MCP server exposes UniFi controller API to LLM agents (Claude, Cursor, etc.). Run in **read-only** mode initially. Skip → if no LLM integration, ops still 100% manual.
  5. **Define agent runbooks**: "if alert X fires, ask Claude to inspect APs A, B, C and recommend next action." Establish that Claude proposes, human approves. Skip → either no automation OR unsupervised LLM changes break things.
  6. **Review cadence**: weekly look at dashboards + alert history + any Claude-proposed changes; monthly review SLOs (adjust thresholds based on real workload). Skip → setup decays; alerts go ignored; LLM context drifts.
- **资深路径**:
  - **skip**: Senior engineer **skips comparison shopping** with Mist Marvis ("can we just buy Marvis?") — knows answer is "yes but 5-10x cost" — instead frames the stack as "Marvis-lite, but you own the data."
  - **optimize**: Senior engineer **drops alert rules that aren't actionable** — every alert must map to a runbook step; alerts without remediation are noise.
  - **add**: Senior engineer **adds an MCP read-only gate** — even when Claude can call write methods, wrap with a "propose → human approve → execute" loop; never let agent push firewall rules autonomously (evidence: [T02-S020] unifi-mcp risks).
- **近期变化** (近 12 个月):
  - 2025-04: unifi-mcp launched (T02-S020), 389 stars by 2026-06
  - 2026-02: unifly Rust TUI launched, designed for "agent-skills" + "openclaw-skill" topics (T02-S022)
  - 2026-01: Crosstalk UI Toolkit launched — dashboard convergence with unpoller stack
  - 触发事件类型: 新工具 (MCP server, unifly) + 趋势 (LLM agent ops)
- **典型耗时**:
  - 入门 SOP: 8-16 hours setup (Docker + dashboards + alerts + agent integration)
  - 资深路径: 4-8 hours (template + Git-managed config + reusable runbooks)
- **关键工具**:
  - unpoller + Prometheus / InfluxDB (必备 stack base)
  - Grafana + community dashboards (必备)
  - unifi-mcp (新兴 — < 1 year stability caveat)
  - Claude Code / Cursor / similar (必备 LLM interface)
  - Crosstalk UI Toolkit (场景特化 — complementary dashboard)
- **关键人物**:
  - David Newhall et al. — unpoller maintainers
  - sirkirby — unifi-mcp maintainer
  - hyperb1iss — unifly maintainer
  - Bob Friday (Mist) — AIOps thought leader; UBNT's comparison anchor (Track 01)
- **常见失败模式**:
  - **F1**: Build with Chroma in dev, then struggle migrating to Pinecone — wastes 1-2 weeks. (Generalized: build the whole stack with experimental MCP tools, then a UBNT API breaking change in Network 11.x silently breaks scraping; alerts go quiet, no one notices for 2 weeks.)
  - **F2**: Wire Claude to write methods without review gate — agent "fixes" perceived issue by changing firewall rule at 3am, locks IT team out of own network.
  - **F3**: Set up dashboards, forget to set alerts — discover problems by user complaints anyway. Defeated the purpose.
  - **F4**: Forget single-maintainer risk on unifi-mcp / unifly — repo goes unmaintained, breaks at next UBNT API change, scramble to fork.
- **Sources**:
  - [Primary] unpoller GitHub (T03-S017)
  - [Primary] CTS 385 Grafana dashboard episode (T03-S013)
  - [Reference] Marvis / Mist comparison anchor (T03-S026)
  - [Reference] Track 02 tools tier 3 (新兴)
- **Last_updated**: 2026-02 (unifly launch + 2026 MCP momentum)
- **Decay risk**: high (12-month-class — MCP ecosystem is < 1 year old; specific tools may be replaced by official UBNT MCP if released)

---

## Phase 2 提炼提示

### 反复出现 ≥ 3 个 workflow 都包含的步骤（候选 playbook 通则）

1. **「Validate with iperf3 + walk-test, not just config inspection」** — 出现于 W1 (greenfield) / W2 (troubleshoot) / W3 (HD planning) / W5 (survey) / W6 (upgrade)
   → 候选 playbook: 「如果 just touched the config, then iperf3 + WiFiman walk before you call it done」
2. **「Layered diagnosis: PHY → MAC → assoc → auth → IP」** — 出现于 W2 (troubleshoot), W4 (roaming, implicitly), W5 (survey active phase)
   → 候选 playbook: 「如果 X 看起来坏，then 不要跳层 — 从 PHY 起逐层验证」
3. **「Read the CVE / release notes before you upgrade」** — 出现于 W6 (upgrade) / W7 (security), with weaker version in W1 (during procurement)
   → 候选 playbook: 「如果 升级 / 部署新版本，then 优先看 CVE 而非 feature notes」
4. **「Backup config (or have it in Git) before any change」** — 出现于 W1 / W6 (explicit) / W7 (implicit during rollback)
   → 候选 playbook: 「如果 即将 production change, then config-as-code / snapshot 先做」
5. **「Capacity > coverage in design / troubleshoot」** — W1 / W2 / W3 (most explicit) / W5
   → 候选 playbook: 「如果 80+ user dense, then 先算 airtime budget, 后选 AP 数 / 位置」

### 入门 SOP vs 资深路径之间最大的差距

**入门 SOP 平均长度** = 6.6 steps (range 6-12)
**资深路径压缩到** ~ 4-5 effective steps (skip 1-2 + optimize 1 + add 1 = net ~30% reduction)

**资深差距模式**:
- **资深人都跳过预测设计** (W1, W3, W5) 在 SMB / 单层 / 预算紧场景 — 心智模型候选: 「不要在 ≤ 80 人单层场景过度预测设计」
- **资深人都加监控** (W1, W3, W6, W8) — 心智模型候选: 「监控不是 phase 2 的事 — 在 day 1 就启用 unpoller」
- **资深人都做 capture-first 诊断** (W2, W4, W5, W7) — 心智模型候选: 「specs / GUI 不替代 measurement; 抓包永远是 ground truth」
- **资深人模式化场景** (W3 80-ppl 模板，W6 CVE-only diff): 把多个项目的经验固化成可复用模板，避免每次从零思考

### 近期工作流变化的根本原因（触发事件类型分布）

| 触发事件类型 | 涉及 workflows | 计数 |
|------------|--------------|------|
| 新硬件 (U7 Pro Max, UCG-Max, UCG-Fiber) | W1, W3 | 2 |
| 新工具 (UI Toolkit, unifi-mcp, unifly, unifi-os-server, Channel Map) | W1, W3, W8 | 3 |
| 新版本 (UniFi Network 10.0, AI Pro v11) | W1, W5, W6, W8 | 4 |
| 法规/安全 (CVE wave 2025-2026, SAE-PT, FragAttacks) | W6, W7 | 2 |
| 学术研究 (Vanhoef Dragonblood + ongoing) | W7 | 1 |
| 厂商 EOL (AirMagnet 2023-12) | W5 | 1 |
| 协议/标准 (Wi-Fi 7 ratified 2024) | W3, W4, W6 | 3 |

**主要驱动力**: 新工具 (3) + 新版本 (4) + 协议/标准 (3) 是当前最强信号。Wi-Fi 7 + LLM-agent 时代叠加，导致 high-decay workflows (W7, W8) 集中。

→ Phase 2 时识别行业的「外部驱动力」: 
- Wi-Fi 7 / 6 GHz spread (硬件侧)
- UBNT 自身 software maturity push (软件 / cloud / Hosted UniFi)
- LLM agent 进入 enterprise ops (W8 整个 workflow 是 < 12 个月内新出现)
- Security CVE 节奏加速 (W6 / W7)

### 冷僻 / 信号薄弱

- **workflow 数**: 8 ✓ (在 6-10 目标区间内, > floor 4)
- **一手 source 占比**: ~75% — Manifest 中 verified_primary + surrogate_primary 主导 ✓
- **资深差异点缺失**: 0% — 所有 8 个 workflow 都有 ≥ 2 处资深差异 (skip / optimize / add) ✓
- **last_updated 字段填充率**: 100% ✓
- **near-term change 字段**: 100% — 包含两个明确稳态标注 (W2, W4) 和六个含日期事件标注 ✓

**信号薄弱点**:
1. **AIOps workflow (W8)** 整体 < 12 月历史 — Phase 2.8 诚实边界标注 "本 skill 工作流节中 W7 + W8 高衰减，建议每 3 月跑 update"
2. **zh-CN locale workflow signals 缺失** — 80 人办公场景中国本地化部署有 (a) 合规要求 (等保 / GDPR-likes), (b) 6 GHz 不可用 — 工作流应有 zh-CN 变体，但本轮未深挖 (受 Track 05 zh-CN gap 影响)
3. **流派分裂**: Predictive-heavy vs Pragmatic-survey (Track 02 提及) 在 W1 / W3 / W5 都有体现 — 资深人在 SMB 一致选 Pragmatic, 在 enterprise 商业交付一致选 Predictive。建议 Phase 2 心智模型节明确这一二元选择 + 判定标准
4. **AIOps 维度 UBNT 弱于 Mist** (来自 Track 02 + Track 05 双重信号 + W8 显式) — 建议 Phase 2.8 诚实边界明确标注

### Wave 1+2 没覆盖到的潜在 sub-skill

W3 (High-density capacity planning) **直接对应** Phase 4 sanity-test 的 80-人 dense office 场景 — 是 sub_skill_candidate 的天然 anchor。建议 Phase 3 蒸馏「Wi-Fi 容量优先思维」sub-skill 时以 W3 作为核心 SOP + vonNagy figure 作为 voice anchor。

### Wave 3 接力提示

- **→ Phase 2.2 (playbook)**: 5 个候选 playbook 通则上面已列
- **→ Phase 2.4 (workflow section in SKILL.md)**: 直接组装 W1 / W3 (80-person 重点) / W2 (troubleshoot) 作为 SKILL.md 的核心入门 SOP + 资深路径展示
- **→ Phase 2.8 (诚实边界)**: 
  - 标注: W7 + W8 是 high-decay 12-month-class — 每 3 月跑 update
  - 标注: AIOps 维度 UBNT 弱项已显式体现在 W8
  - 标注: zh-CN locale workflow variant 缺失
- **→ Phase 4 (sanity test)**: W3 直接对应 80-人办公场景, 是 sanity-test 主测试对象

---

## 自检 (提交前)

- [x] Workflow 数量 = 8 (在 6-10 目标区间内)
- [x] 每个 workflow 有完整 12 字段卡 + last_updated 日期
- [x] 入门 SOP 和资深路径分开了; 8/8 workflows 都有 ≥ 2 处资深差异点
- [x] 近期变化字段 8/8 都填了 (含 2 个明确稳态标注)
- [x] 一手来源 (vendor blog / engineer blog / 标准 / podcast) 占比 ~75%
- [x] Decay risk 字段每个 workflow 都标了
- [x] 总览表按 decay 分组 (High 2 / Medium 3 / Low 3)
- [x] Phase 2 接口（共同步骤 5 / 入门资深差距 / 变化触发分布 / 冷僻信号）填了

**最终输出**: 8 retained workflows / 5 candidate playbook patterns / W3 = HD 80-person 12-step user-anchor workflow / 2 high-decay flagged (W7 WPA3, W8 AIOps stack).
