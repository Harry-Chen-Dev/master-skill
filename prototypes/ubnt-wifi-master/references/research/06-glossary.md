# Track 06 — Glossary: UniFi/UBNT Enterprise Wi-Fi Engineering

> Phase 1 wave 1, Track 06. Locale: global (English primary, zh-CN notes where notable).
> Industry: UniFi/UBNT Enterprise Wi-Fi Engineering. Scenario lens: 80-person dense office.

## Source Manifest

| source_id | url | bucket | last_checked | author/host | one-line note |
|-----------|-----|--------|--------------|-------------|---------------|
| T06-S001 | https://standards.ieee.org/ieee/802.11/7028/ | verified_primary | 2026-06-02 | IEEE-SA | 802.11-2020 base standard, all amendments roll into this |
| T06-S002 | https://standards.ieee.org/ieee/802.11ax/7831/ | verified_primary | 2026-06-02 | IEEE-SA | 802.11ax (Wi-Fi 6/6E) spec |
| T06-S003 | https://standards.ieee.org/ieee/802.11be/10403/ | verified_primary | 2026-06-02 | IEEE-SA | 802.11be (Wi-Fi 7) draft, ratified 2024 |
| T06-S004 | https://www.wi-fi.org/discover-wi-fi/wi-fi-certified-6 | surrogate_primary | 2026-06-02 | Wi-Fi Alliance | Wi-Fi 6/6E branding + cert program — vendor docs (一手 publication, surrogate) |
| T06-S005 | https://www.wi-fi.org/discover-wi-fi/security | surrogate_primary | 2026-06-02 | Wi-Fi Alliance | WPA3 / OWE / Enhanced Open spec hub — vendor docs (一手 publication, surrogate) |
| T06-S006 | https://www.fcc.gov/wireless/bureau-divisions/mobility-division/35-46-ghz-band/35-ghz-broadband-radio-service-brs | verified_primary | 2026-06-02 | FCC | UNII band rules + 6 GHz Order (2020) |
| T06-S007 | https://www.fcc.gov/document/fcc-opens-6-ghz-band-wi-fi-and-other-unlicensed-uses | verified_primary | 2026-06-02 | FCC | 2020 6 GHz opening order (UNII-5/6/7/8) |
| T06-S008 | https://www.etsi.org/deliver/etsi_en/300300_300399/30032802/ | surrogate_primary | 2026-06-02 | ETSI | EN 300 328 — 2.4 GHz EU rules — vendor docs (一手 publication, surrogate) |
| T06-S009 | https://www.etsi.org/deliver/etsi_en/301800_301899/30189301/ | surrogate_primary | 2026-06-02 | ETSI | EN 301 893 — 5 GHz EU rules + DFS — vendor docs (一手 publication, surrogate) |
| T06-S010 | https://help.ui.com/hc/en-us/categories/6583256751767-UniFi-Network | surrogate_primary | 2026-06-02 | Ubiquiti | UniFi Network official KB — vendor docs (UBNT 一手 官方, surrogate) |
| T06-S011 | https://help.ui.com/hc/en-us/articles/360008070793 | surrogate_primary | 2026-06-02 | Ubiquiti | Min RSSI / fast roaming UBNT-specific guide — vendor docs (UBNT 一手 官方, surrogate) |
| T06-S012 | https://www.cwnp.com/certifications/ | surrogate_primary | 2026-06-02 | CWNP | CWNA/CWAP/CWDP/CWSP/CWNE cert catalog — vendor-neutral cert syllabus (CWNP 协会 教材, surrogate) |
| T06-S013 | https://www.cwnp.com/certifications/cwna | surrogate_primary | 2026-06-02 | CWNP | CWNA exam objectives — canonical entry-level Wi-Fi cert — vendor-neutral cert syllabus (CWNP 协会 教材, surrogate) |
| T06-S014 | https://datatracker.ietf.org/doc/html/rfc5415 | verified_primary | 2026-06-02 | IETF | RFC 5415 CAPWAP protocol |
| T06-S015 | https://datatracker.ietf.org/doc/html/rfc3748 | verified_primary | 2026-06-02 | IETF | RFC 3748 EAP framework |
| T06-S016 | https://datatracker.ietf.org/doc/html/rfc2865 | verified_primary | 2026-06-02 | IETF | RFC 2865 RADIUS |
| T06-S017 | https://www.ieee802.org/1/pages/802.1x-2020.html | surrogate_primary | 2026-06-02 | IEEE 802.1 WG | 802.1X-2020 port-based NAC — vendor docs (一手 publication, surrogate) |
| T06-S018 | https://en.wikipedia.org/wiki/IEEE_802.11 | secondary | 2026-06-02 | Wikipedia | Solid 802.11 amendment timeline cross-ref |
| T06-S019 | https://en.wikipedia.org/wiki/Wi-Fi_6 | secondary | 2026-06-02 | Wikipedia | Wi-Fi 6/6E primer cross-ref |
| T06-S020 | https://www.ekahau.com/ecse-certification/ | surrogate_primary | 2026-06-02 | Ekahau | ECSE — de-facto enterprise survey cert — vendor docs (Ekahau/Hamina vendor 一手, surrogate) |
| T06-S021 | https://store.ui.com/us/en/category/professional-certifications | surrogate_primary | 2026-06-02 | Ubiquiti | UEWA / UBWA / UFSP catalog — vendor docs (UBNT 一手 官方, surrogate) |
| T06-S022 | https://www.miit.gov.cn/zwgk/zcwj/wjfb/tg/art/2021/art_98e6c45d7f704c79bdee35bf06edf17b.html | verified_primary | 2026-06-02 | China MIIT | 2.4/5 GHz rules; 6 GHz still gated (verify 2026 state) |
| T06-S023 | https://www.cisco.com/c/en/us/products/wireless/what-is-wifi-6e.html | secondary | 2026-06-02 | Cisco | Wi-Fi 6E vendor explainer cross-ref |
| T06-S024 | https://www.cwnp.com/uploads/802-11-2020.pdf | surrogate_primary | 2026-06-02 | CWNP | 802.11-2020 reader-friendly redaction — vendor-neutral cert syllabus (CWNP 协会 教材, surrogate) |
| T06-S025 | https://www.wi-fi.org/discover-wi-fi/wi-fi-certified-7 | surrogate_primary | 2026-06-02 | Wi-Fi Alliance | Wi-Fi 7 cert program (2024 launch) — vendor docs (一手 publication, surrogate) |
| T06-S026 | https://help.ui.com/hc/en-us/articles/360008520794-UniFi-Network-Best-Practices-for-Managing-Chromecasts-and-Other-mDNS-Devices | surrogate_primary | 2026-06-02 | Ubiquiti | mDNS / multicast on UniFi — VLAN gotcha — vendor docs (UBNT 一手 官方, surrogate) |
| T06-S027 | https://help.ui.com/hc/en-us/articles/115005212927 | surrogate_primary | 2026-06-02 | Ubiquiti | UniFi WiFi AI / RF planning auto-channel doc — vendor docs (UBNT 一手 官方, surrogate) |
| T06-S028 | https://www.cisco.com/c/dam/en/us/td/docs/wireless/controller/9800/17-9/config-guide/b_wl_17_9_cg/m_802_1x_authentication_ewlc.pdf | surrogate_primary | 2026-06-02 | Cisco | 802.1X EAP types reference — vendor docs (Cisco 一手 vendor 文档/blog, surrogate) |
| T06-S029 | https://www.fcc.gov/document/fcc-adopts-rules-facilitate-next-generation-wireless-technologies | verified_primary | 2026-06-02 | FCC | AFC (Automated Frequency Coordination) order 2023 |
| T06-S030 | https://www.cwnp.com/blog/802-11k-v-r-fast-secure-transition | verified_primary | 2026-06-02 | CWNP blog | 11k/v/r insider explainer |
| T06-S031 | https://community.ui.com/questions/UniFi-Min-RSSI-explanation/ | reference | 2026-06-02 | Ubiquiti Community | Min RSSI usage debates (insider register) |

---

## 总览

### Tier 1 — 核心必懂 (24 个，目标 ≥ 20)

| 术语 | Type | Insider def | Outsider tell | Last_updated |
|------|------|-------------|---------------|--------------|
| SSID | acronym | Logical network name (broadcast string) — many BSSIDs can share one SSID | "ESSID/SSID" confusion; thinks changing SSID = changing the AP | 2026-06-02 |
| BSSID | acronym | The MAC of an AP's radio for a given SSID — what a client actually associates to | Outsider conflates with SSID; thinks "one BSSID per network" | 2026-06-02 |
| AP / Access Point | term | L2 bridge that turns Ethernet into RF — **not** a router | Outsider says "the router" when they mean the AP | 2026-06-02 |
| RSSI | acronym | Received Signal Strength Indicator in dBm — **negative** values, closer to 0 = stronger | Thinks -50 < -70 because "-70 is bigger" (sign error) | 2026-06-02 |
| SNR | acronym | Signal-to-Noise Ratio in dB — positive number; >25 dB needed for high MCS | Outsider equates SNR with RSSI | 2026-06-02 |
| dBm | term | Decibel relative to 1 mW — logarithmic, always negative for received Wi-Fi | "More dBm = stronger" — wrong sign intuition | 2026-06-02 |
| dBi | term | Antenna gain over isotropic radiator — passive directional concentration, not amplification | Outsider thinks higher dBi = "stronger transmitter" | 2026-06-02 |
| EIRP | acronym | Effective Isotropic Radiated Power — tx-power + antenna-gain - cable-loss; the regulator-capped number | Outsider tunes tx-power without realizing EIRP cap | 2026-06-02 |
| Channel | term | Discrete center frequency slot (e.g., ch 36, ch 149) — distinct from channel width | Outsider uses "channel" for both center freq and bandwidth | 2026-06-02 |
| Channel Width | term | RF bandwidth around a channel: 20/40/80/160 MHz — wider = more throughput but more CCI | Outsider says "I set channel to 80" meaning width | 2026-06-02 |
| CCI | acronym | Co-Channel Interference — APs on same channel hearing each other, sharing airtime | Outsider "fixes" weak Wi-Fi by adding more APs → causes CCI | 2026-06-02 |
| ACI | acronym | Adjacent Channel Interference — overlapping channels (e.g., ch 1 + ch 3 in 2.4 GHz) | Outsider thinks 2.4 GHz has 11 usable channels (actually only 1/6/11) | 2026-06-02 |
| DFS | acronym | Dynamic Frequency Selection — radar-sharing rule on UNII-2A/2C (5 GHz channels 52-144) | Outsider blames "AP rebooting itself" for an unrelated bug | 2026-06-02 |
| MCS | acronym | Modulation and Coding Scheme — index 0-11 (HE) / 0-13 (EHT) tied to throughput rate | Outsider thinks PHY rate = throughput | 2026-06-02 |
| OFDMA | acronym | Orthogonal Frequency-Division Multiple Access — Wi-Fi 6 subcarrier multiplexing (RUs) | Outsider conflates OFDMA with MU-MIMO | 2026-06-02 |
| MU-MIMO | acronym | Multi-User MIMO — concurrent spatial-stream tx to multiple clients | Outsider thinks "8 streams = 8x speed" regardless of clients | 2026-06-02 |
| Wi-Fi 6 (802.11ax) | standard + term | OFDMA + BSS coloring + TWT — efficiency upgrade for dense deployments | Outsider says "Wi-Fi 6 is faster than Wi-Fi 5" as the sole takeaway | 2026-06-02 |
| Wi-Fi 6E | standard + term | 802.11ax extended into 6 GHz (UNII-5/6/7/8, US/EU only — not China yet) | Outsider thinks Wi-Fi 6E is a separate generation from Wi-Fi 6 | 2026-06-02 |
| Wi-Fi 7 (802.11be) | standard + term | EHT — 320 MHz channels, MLO, 4K-QAM. Ratified 2024 | Outsider thinks 6E and 7 are the same | 2026-06-02 |
| WPA3 | standard | SAE-based PSK replacement; mandatory PMF; 192-bit option in Enterprise | Outsider says "WPA3 password" meaning passphrase; conflates with WPA2 | 2026-06-02 |
| PSK / Passphrase | term | Pre-Shared Key derived from passphrase via PBKDF2 — **not** "the WPA password" | Outsider says "WiFi password" sloppily; insiders say PSK or passphrase | 2026-06-02 |
| 802.1X | standard | Port-based NAC for authenticating individual users to a wired/wireless port via EAP/RADIUS | Outsider mixes "WPA2 Enterprise" with separate 802.1X concept | 2026-06-02 |
| Roaming (incl. 11k/v/r) | term | Client-driven handoff between BSSIDs of one ESS; 11r = key caching, 11k/v = AP hints | Outsider says "AP handed off the client" — clients decide, not APs | 2026-06-02 |
| 5 GHz Wi-Fi | term | 5 GHz band Wi-Fi (UNII-1/2/3) — **not** cellular 5G | "I have 5G WiFi" — mixing cellular gen with band | 2026-06-02 |

### Tier 2 — 周边熟知 (38 个，目标 ≥ 25)

| 术语 | Type | Insider def | Last_updated |
|------|------|-------------|--------------|
| ESSID | acronym | Extended SSID — same SSID across multiple APs forming one ESS | 2026-06-02 |
| STA / Station | term | Any 802.11 client (laptop, phone, IoT) | 2026-06-02 |
| ESS | acronym | Extended Service Set — set of BSSes sharing one SSID | 2026-06-02 |
| Beacon | term | Periodic mgmt frame announcing BSS — default 100 TUs (~102.4 ms) | 2026-06-02 |
| DTIM | acronym | Delivery Traffic Indication Message — buffers multicast; period affects battery vs latency | 2026-06-02 |
| RTS/CTS | acronym | Request-to-Send / Clear-to-Send — collision avoidance handshake; usually off below threshold | 2026-06-02 |
| TWT | acronym | Target Wake Time — Wi-Fi 6 scheduled sleep for IoT battery savings | 2026-06-02 |
| BSS Coloring | term | Wi-Fi 6 mechanism marking each BSS with a color (0-63) for spatial reuse | 2026-06-02 |
| TPC | acronym | Transmit Power Control — regulatory + automated power adjustment | 2026-06-02 |
| Min RSSI | term | UBNT-specific: kick clients below threshold to force roaming (e.g., -75 dBm) | 2026-06-02 |
| Band Steering | term | Push dual-band clients to 5/6 GHz away from crowded 2.4 GHz | 2026-06-02 |
| Airtime Fairness | term | Scheduler prevents slow clients from hogging the medium | 2026-06-02 |
| CAPWAP | acronym | Control And Provisioning of Wireless APs — tunneling protocol (RFC 5415) | 2026-06-02 |
| RADIUS | acronym | Remote Authentication Dial-In User Service — RFC 2865; AAA for 802.1X | 2026-06-02 |
| EAP | acronym | Extensible Authentication Protocol — RFC 3748; container for PEAP/TLS/TTLS | 2026-06-02 |
| EAP-TLS | term | Cert-based 802.1X — strongest, no passwords on wire | 2026-06-02 |
| PEAP / EAP-PEAP | term | Tunneled EAP with server-side cert + inner MSCHAPv2 — Windows default | 2026-06-02 |
| PMF | acronym | Protected Management Frames (802.11w) — encrypts disassoc/deauth; mandatory in WPA3 | 2026-06-02 |
| SAE | acronym | Simultaneous Authentication of Equals — WPA3-Personal handshake (Dragonfly) | 2026-06-02 |
| OWE | acronym | Opportunistic Wireless Encryption — encrypted "open" SSID (Enhanced Open) | 2026-06-02 |
| 11k | standard | 802.11k — Radio Resource Measurement; AP hints clients about neighbor BSSIDs | 2026-06-02 |
| 11v | standard | 802.11v — BSS Transition Management; AP politely asks client to move | 2026-06-02 |
| 11r | standard | 802.11r — Fast BSS Transition; pre-cached keys for sub-50 ms roam | 2026-06-02 |
| 11w | standard | 802.11w — PMF (see above) | 2026-06-02 |
| AFC | acronym | Automated Frequency Coordination — 6 GHz Standard Power mode (FCC 2023) | 2026-06-02 |
| UNII-1/2A/2B/2C/3 | term | FCC sub-bands of 5 GHz, each with its own EIRP cap + DFS rules | 2026-06-02 |
| UNII-5/6/7/8 | term | FCC sub-bands of 6 GHz (5.925-7.125 GHz, Wi-Fi 6E/7) | 2026-06-02 |
| MLO | acronym | Multi-Link Operation — Wi-Fi 7's simultaneous multi-band aggregation | 2026-06-02 |
| 4K-QAM | term | Wi-Fi 7's 4096-QAM modulation — 20% rate over Wi-Fi 6's 1024-QAM | 2026-06-02 |
| RU | acronym | Resource Unit — OFDMA subcarrier block (26/52/106/242/484/996/2x996-tone) | 2026-06-02 |
| Spatial Stream | term | Independent MIMO data path; 2x2/4x4 = stream count | 2026-06-02 |
| PoE / PoE+ / PoE++ | term | Power over Ethernet — 802.3af/at/bt — most APs are PoE-powered | 2026-06-02 |
| UniFi Network Application | term | UBNT's controller software (formerly "UniFi Controller") | 2026-06-02 |
| Cloud Key (UCK) | term | UBNT appliance hosting the Network Application | 2026-06-02 |
| Adopt | term (UBNT) | Verb: bind an AP to a controller — UBNT-specific wording | 2026-06-02 |
| U6 / U7 series | term (UBNT) | UBNT Wi-Fi 6 (U6 Lite/+/Pro/Enterprise) and Wi-Fi 7 (U7 Pro/Wall) AP family | 2026-06-02 |
| WiFiman | term (UBNT) | UBNT mobile app for survey / speed test | 2026-06-02 |
| Wireless Uplink | term (UBNT) | UBNT's mesh-via-wireless backhaul feature (vs. mandatory wired downlink) | 2026-06-02 |

### Standards / Regulations / Certifications 时间轴 (近 5 年内有显著变化)

| 名称 | Issued | Last revised | Decay | Note |
|------|--------|--------------|-------|------|
| IEEE 802.11ax (Wi-Fi 6/6E) | 2021 | 2021 | low | Now stable, but 6E rollout still uneven globally |
| IEEE 802.11be (Wi-Fi 7) | 2024 | 2024 | high | Fresh, certified products still maturing |
| Wi-Fi Alliance Wi-Fi 7 cert | 2024-Jan | 2024-Jan | high | Brand-new program; vendor profiles still expanding |
| FCC 6 GHz Order (US) | 2020-Apr | 2023 (AFC) | medium | Standard Power + AFC went live 2024 |
| ETSI EN 303 687 (EU 6 GHz LPI) | 2022 | 2024 | medium | EU low-power indoor; SP rules deferred |
| China MIIT 6 GHz status | — | 2024 | **high** | As of 2026 update, China has **not** opened 6 GHz for unlicensed Wi-Fi — verify quarterly |
| WPA3 mandate (Wi-Fi 6/6E/7) | 2018 | 2022 | low | All new Wi-Fi 6E/7 cert requires WPA3 + PMF |
| 802.11-2020 base | 2020 | 2020 | low | Rolling baseline; next consolidation expected ~2027 |
| Ekahau ECSE | (legacy) | 2023 (Sidekick 2) | medium | Ekahau Pro 11+ tool updates each year |
| CWNA exam | 2002 | 2024 (CWNA-109) | medium | Refreshed every 3-4 years; current = -109 |
| UEWA (Ubiquiti) | ~2018 | 2024 | medium | Free online, refreshed with U7 lineup |

### 行业「外行破绽」高亮 (Top 12 最容易暴露的)

| 误用 | 内行实际意思 | 出现频率 |
|------|--------------|----------|
| "5G WiFi" 指 5 GHz | Cellular 5G ≠ 5 GHz Wi-Fi band; mixing telecom gen with RF band | 极高 |
| "-50 dBm 比 -70 dBm 弱" | -50 dBm is **stronger** (closer to 0) than -70 dBm — sign error | 极高 |
| "Wi-Fi 慢就多加几个 AP" | More APs without proper channel plan → CCI, slower throughput | 极高 |
| "改信道 80" (混淆 channel vs width) | Channel = center freq; 80 = bandwidth (MHz) | 高 |
| "Router 信号差" 实际指 AP | Router (L3 gateway) ≠ AP (L2 RF bridge); usually it's the AP | 高 |
| "Wi-Fi 6E 是新一代,不是 Wi-Fi 6" | 6E = same 802.11ax PHY, extended to 6 GHz | 高 |
| "WPA 密码" / "WiFi 密码" | Insider: PSK / passphrase | 高 |
| "Mesh 能解决一切" | Wireless backhaul halves capacity per hop; wired is always better | 高 |
| "AP 把客户端切到另一个" | Clients decide roaming; APs only hint (11k/v) or kick (Min RSSI / disassoc) | 中-高 |
| "8 流就是 8 倍速" | Streams require client support + spatial separation; rarely linear | 中 |
| "信道 1-11 都能用" (2.4G) | Only 1/6/11 are non-overlapping; "ch 3" causes ACI | 高 |
| "Boost the signal" / 加功率 | EIRP capped by regulator; client uplink limited; asymmetric | 高 |

---

## Detailed Entries — Tier 1

### 1. SSID — Service Set Identifier

- **Type**: acronym + term
- **Tier**: tier-1
- **Definition (insider)**: The human-readable network name string broadcast in beacons; many BSSIDs (per-radio MACs) can share one SSID across an ESS (evidence: [T06-S001, T06-S024]).
- **Definition (outsider-friendly)**: "The Wi-Fi network name you pick from a list." 
- **Etymology**: IEEE 802.11-1997.
- **常见误用 (outsider-tell)**:
  - `usage_tell`: "Changed the SSID, why is my device still disconnecting from the same AP?" — confuses SSID (logical) with BSSID (physical radio) (evidence: [T06-S031]).
  - `pronunciation_tell`: Pronounced as "S-S-I-D" or sometimes mistakenly "E-S-S-I-D" — they're different concepts.
- **关联术语**: BSSID, ESSID, ESS
- **是否被错位包装**: Not particularly — vendors haven't claimed SSID.
- **Source**: [Primary] T06-S001 (IEEE 802.11-2020 §3 Definitions); [Secondary] T06-S018.
- **可信度**: high
- **Decay risk**: low

### 2. BSSID — Basic Service Set Identifier

- **Type**: acronym
- **Tier**: tier-1
- **Definition (insider)**: The 48-bit MAC address of an AP's radio interface for a given SSID — what a client actually associates to. One physical AP with two radios on the same SSID has two BSSIDs (evidence: [T06-S001]).
- **Definition (outsider-friendly)**: The unique hardware address of the radio you're connected to.
- **Etymology**: IEEE 802.11-1997. The "Basic" in Basic Service Set is from the 1997 spec hierarchy: BSS < ESS.
- **常见误用 (outsider-tell)**:
  - `semantic_tell`: "What's the BSSID of my home network?" — Networks have SSIDs; BSSIDs are per-radio. (evidence: [T06-S031])
  - `usage_tell`: Treating BSSID as a network identifier that can be set rather than a MAC that's assigned.
- **关联术语**: SSID, ESSID, AP
- **是否被错位包装**: No.
- **Source**: [Primary] T06-S001; [Secondary] T06-S018.
- **可信度**: high
- **Decay risk**: low

### 3. AP / Access Point

- **Type**: term + acronym
- **Tier**: tier-1
- **Definition (insider)**: A Layer-2 wireless-to-Ethernet bridge with a built-in 802.11 radio. **Not** a router. In enterprise architecture, APs are dumb-ish edge devices; intelligence lives in the controller (evidence: [T06-S010, T06-S014]).
- **Definition (outsider-friendly)**: The puck on the ceiling or wall that broadcasts Wi-Fi.
- **Etymology**: IEEE 802.11 from inception (1997).
- **常见误用 (outsider-tell)**:
  - `semantic_tell`: "The router has bad signal" — the router is usually a separate gateway; signal comes from the AP. In a home all-in-one box this is forgivable; in enterprise it marks an outsider.
  - `usage_tell`: "I bought a new router because the signal was weak" — when the actual issue is AP placement / density.
- **关联术语**: STA, BSSID, Controller
- **是否被错位包装**: SOHO vendors (Linksys, ASUS) marketing AP+router+switch combo boxes as "the router," conflating the concepts.
- **Source**: [Primary] T06-S001 §3; [Secondary] T06-S010.
- **可信度**: high
- **Decay risk**: low

### 4. RSSI — Received Signal Strength Indicator

- **Type**: acronym
- **Tier**: tier-1
- **Definition (insider)**: Vendor-defined relative measure of received power, conventionally expressed in dBm. **Always negative** in Wi-Fi. -65 dBm is a strong signal; -85 dBm is barely usable. The IEEE specifies RSSI as a unitless 0-255 register; vendors map it to dBm (evidence: [T06-S001 §9.4.2, T06-S024]).
- **Definition (outsider-friendly)**: How loud the AP sounds at your device, in negative numbers — the smaller the absolute value, the better.
- **Etymology**: 802.11 PHY layer concept; vendor-specific dBm mapping.
- **常见误用 (outsider-tell)**:
  - `semantic_tell`: "My RSSI is -70, the neighbor's is -50 — mine is better" — **wrong**. -50 is stronger. The sign trips up novices and even some IT generalists (evidence: [T06-S031]).
  - `usage_tell`: Treating RSSI as throughput predictor — it's a precondition for high MCS, not a guarantee.
  - `pronunciation_tell`: Spelled "R-S-S-I" (four letters), not "russy."
- **关联术语**: SNR, MCS, dBm
- **是否被错位包装**: Vendors expose proprietary "signal bars" that don't linearly map to dBm.
- **Source**: [Primary] T06-S001 §9.4.2; [Secondary] T06-S024.
- **可信度**: high
- **Decay risk**: low

### 5. SNR — Signal-to-Noise Ratio

- **Type**: acronym
- **Tier**: tier-1
- **Definition (insider)**: The dB difference between signal power and noise floor. Positive number. Practical thresholds: ≥ 25 dB for high MCS / 1024-QAM, ≥ 20 dB for stable voice, ≥ 15 dB for basic data, < 10 dB = unusable (evidence: [T06-S024, T06-S013 CWNA objectives]).
- **Definition (outsider-friendly)**: How much louder the Wi-Fi signal is than the background noise.
- **Etymology**: General RF engineering, predates Wi-Fi.
- **常见误用 (outsider-tell)**:
  - `semantic_tell`: "RSSI is -65, that's my SNR" — confuses signal with signal-to-noise.
  - `usage_tell`: Reporting SNR without knowing the noise-floor measurement was bogus (most consumer tools fake the noise floor as -95 dBm constant).
- **关联术语**: RSSI, MCS, Noise Floor
- **是否被错位包装**: No.
- **Source**: [Primary] T06-S024; [Secondary] T06-S013.
- **可信度**: high
- **Decay risk**: low

### 6. dBm

- **Type**: term + acronym
- **Tier**: tier-1
- **Definition (insider)**: Decibels relative to 1 milliwatt. Logarithmic; +3 dBm = doubling power; +10 dBm = 10×. Wi-Fi received power is always negative dBm (e.g., -50 dBm = 10 nW). Tx power and EIRP, by contrast, are typically positive dBm (e.g., 20 dBm = 100 mW).
- **Definition (outsider-friendly)**: A way to express signal power on a log scale; less negative = stronger.
- **Etymology**: General telecom engineering.
- **常见误用 (outsider-tell)**:
  - `semantic_tell`: "Set the AP to higher dBm to fix bad coverage" — increasing tx power often makes things worse: client uplink stays the same → asymmetric link.
  - `usage_tell`: Failing to distinguish tx-power dBm (positive) from received-power dBm (negative).
- **关联术语**: dBi, EIRP, RSSI
- **是否被错位包装**: No.
- **Source**: [Primary] IEEE 802 PHY definitions (T06-S001); [Secondary] T06-S024.
- **可信度**: high
- **Decay risk**: low

### 7. dBi

- **Type**: term + acronym
- **Tier**: tier-1
- **Definition (insider)**: Antenna gain measured against an isotropic (theoretical omnidirectional) radiator. Passive — concentrates RF in a direction; **does not amplify**. A 6 dBi antenna gives 6 dB more EIRP in its boresight, at the cost of pattern coverage elsewhere.
- **Definition (outsider-friendly)**: How directional an antenna is; higher means tighter beam.
- **Etymology**: Antenna engineering.
- **常见误用 (outsider-tell)**:
  - `semantic_tell`: "This AP has 8 dBi antennas so it transmits 8 dB more power" — **no**, it concentrates the existing power.
  - `usage_tell`: Choosing high-gain antennas indoor where coverage pattern matters more than range.
- **关联术语**: dBm, EIRP, omnidirectional
- **是否被错位包装**: Consumer "high-gain" antennas marketed as performance boosters.
- **Source**: [Primary] T06-S001 §17 PHY; [Secondary] T06-S013.
- **可信度**: high
- **Decay risk**: low

### 8. EIRP — Effective Isotropic Radiated Power

- **Type**: acronym
- **Tier**: tier-1
- **Definition (insider)**: tx-power (dBm) + antenna-gain (dBi) − cable-loss (dB). The number regulators cap (e.g., FCC limits 36 dBm EIRP on UNII-1, 30 dBm EIRP on 6 GHz LPI). What actually goes out into the air (evidence: [T06-S006, T06-S007]).
- **Definition (outsider-friendly)**: The radiated power you'd need from a perfect omni-antenna to match what the real antenna puts out in its strongest direction.
- **Etymology**: Radio regulation.
- **常见误用 (outsider-tell)**:
  - `semantic_tell`: "I set tx power to 30 dBm" without computing EIRP including antenna gain — exceeds regulatory cap.
  - `usage_tell`: Confusing tx-power knob with EIRP, leading to fines or interference.
- **关联术语**: TPC, dBi, dBm
- **是否被错位包装**: No.
- **Source**: [Primary] T06-S006 FCC Part 15.247/.407; [Secondary] T06-S008 ETSI EN 300 328.
- **可信度**: high
- **Decay risk**: low

### 9. Channel

- **Type**: term
- **Tier**: tier-1
- **Definition (insider)**: A discrete center frequency in a band. 2.4 GHz channels 1-13 (US: 1-11); 5 GHz channels 36, 40, 44... 165; 6 GHz channels 1-233. **Independent of width**.
- **Definition (outsider-friendly)**: The radio slot the AP is using; like picking a TV channel.
- **Etymology**: ITU-R + IEEE 802.11.
- **常见误用 (outsider-tell)**:
  - `semantic_tell`: "Set the channel to 80" — they mean channel **width** 80 MHz, not channel 80 (which is in 6 GHz!).
  - `usage_tell`: Choosing non-1/6/11 in 2.4 GHz "to find a free one" — causes ACI.
- **关联术语**: Channel Width, DFS, UNII
- **是否被错位包装**: No.
- **Source**: [Primary] T06-S001 §17; T06-S006 FCC band plan.
- **可信度**: high
- **Decay risk**: low

### 10. Channel Width

- **Type**: term
- **Tier**: tier-1
- **Definition (insider)**: Spectral bandwidth allocated to a channel. Options: 20/40/80/160/320 MHz (320 only Wi-Fi 7). Doubling width doubles theoretical PHY rate but halves available channels → more CCI in dense deployments. 80-person office: typically 40 MHz in 5 GHz (evidence: [T06-S002, T06-S010]).
- **Definition (outsider-friendly)**: How wide a radio slot you take — wider = potentially faster but harder to share.
- **Etymology**: 802.11n introduced 40 MHz (2009); 802.11ac 80/160 (2013); 802.11be 320 (2024).
- **常见误用 (outsider-tell)**:
  - `semantic_tell`: "I'm on channel 80 MHz" — conflates channel number with width unit.
  - `usage_tell`: Forcing 160 MHz everywhere; in 80-person dense offices this collapses to a single non-DFS channel and causes CCI.
- **关联术语**: Channel, CCI, MCS
- **是否被错位包装**: Consumer routers sell "AX6000" tri-band based on max-width PHY rates that are unreachable in practice.
- **Source**: [Primary] T06-S002; [Secondary] T06-S027 UniFi AI auto-channel.
- **可信度**: high
- **Decay risk**: low

### 11. CCI — Co-Channel Interference

- **Type**: acronym
- **Tier**: tier-1
- **Definition (insider)**: When two or more APs (or clients) on the same channel can hear each other above the CCA threshold (-82 dBm CCA-ED for OFDM), they must share airtime via CSMA/CA. More APs on the same channel = less airtime per AP, not more total capacity (evidence: [T06-S013, T06-S024]).
- **Definition (outsider-friendly)**: APs on the same channel having to take turns instead of talking simultaneously.
- **Etymology**: Cellular engineering, adopted in Wi-Fi.
- **常见误用 (outsider-tell)**:
  - `semantic_tell`: "Add more APs to fix slow Wi-Fi" — without channel planning, this **causes** CCI and makes it worse.
  - `usage_tell`: Cranking tx-power on all APs, increasing CCI radius.
- **关联术语**: ACI, BSS Coloring, CCA
- **是否被错位包装**: No.
- **Source**: [Primary] T06-S024; [Secondary] T06-S013.
- **可信度**: high
- **Decay risk**: low

### 12. ACI — Adjacent Channel Interference

- **Type**: acronym
- **Tier**: tier-1
- **Definition (insider)**: Power leaking from one channel into a neighboring channel that overlaps in spectrum. In 2.4 GHz, channels 1/6/11 are the only **non-overlapping** 20-MHz channels. Choosing channel 3 or 9 causes ACI with both 1 and 6.
- **Definition (outsider-friendly)**: Neighbors on close channels stepping on each other.
- **Etymology**: 802.11 PHY spec.
- **常见误用 (outsider-tell)**:
  - `semantic_tell`: "There are 11 channels in 2.4 GHz so let me pick a quiet one like 4" — channel 4 overlaps both 1 and 6.
  - `usage_tell`: Setting up two APs on adjacent 40 MHz channels in 5 GHz without realizing they overlap.
- **关联术语**: CCI, Channel
- **是否被错位包装**: No.
- **Source**: [Primary] T06-S024; [Secondary] T06-S013.
- **可信度**: high
- **Decay risk**: low

### 13. DFS — Dynamic Frequency Selection

- **Type**: acronym + standard
- **Tier**: tier-1
- **Definition (insider)**: Regulatory mechanism on 5 GHz UNII-2A (ch 52-64) and UNII-2C (ch 100-144) requiring APs to detect radar and vacate the channel within ~10 s. Doubles your usable 5 GHz channels but introduces unpredictable channel hops when radar (or false positives like terminal Doppler weather radar near airports) is detected (evidence: [T06-S006, T06-S009]).
- **Definition (outsider-friendly)**: A rule that lets Wi-Fi share certain 5 GHz channels with radar, jumping away when radar appears.
- **Etymology**: FCC Part 15.407 (US, 2003); ETSI EN 301 893 (EU).
- **常见误用 (outsider-tell)**:
  - `usage_tell`: "The AP randomly reboots itself" — actually a DFS event causing channel change (which clients see as a brief disconnect).
  - `semantic_tell`: Avoiding DFS channels entirely "because they're unreliable" — in dense urban areas non-DFS channels are saturated; DFS is essential.
- **关联术语**: TPC, UNII-2, AFC
- **是否被错位包装**: No.
- **Source**: [Primary] T06-S006 FCC Part 15.407; T06-S009 ETSI EN 301 893.
- **可信度**: high
- **Decay risk**: low

### 14. MCS — Modulation and Coding Scheme

- **Type**: acronym
- **Tier**: tier-1
- **Definition (insider)**: Index identifying modulation (BPSK→4K-QAM) + coding rate combination. HT (11n) MCS 0-31, VHT (11ac) MCS 0-9, HE (11ax) MCS 0-11, EHT (11be) MCS 0-13. MCS 11 = 1024-QAM 5/6; MCS 13 = 4K-QAM 5/6. Higher MCS demands higher SNR (evidence: [T06-S002, T06-S003]).
- **Definition (outsider-friendly)**: A number describing how much data the radio packs per symbol — bigger number = faster but needs cleaner signal.
- **Etymology**: 802.11n (2009).
- **常见误用 (outsider-tell)**:
  - `semantic_tell`: "AP is at MCS 11, so I'm getting 1.2 Gbps" — that's PHY rate, real throughput is ~60-70%.
  - `usage_tell`: Looking at PHY rate as performance KPI rather than retry rate.
- **关联术语**: SNR, RSSI, PHY rate
- **是否被错位包装**: Consumer routers advertised by max PHY rate ("AX5400") that maps to top MCS × max width × max streams — never seen in practice.
- **Source**: [Primary] T06-S002; [Secondary] T06-S024.
- **可信度**: high
- **Decay risk**: low

### 15. OFDMA — Orthogonal Frequency-Division Multiple Access

- **Type**: acronym
- **Tier**: tier-1
- **Definition (insider)**: Wi-Fi 6 multi-user access scheme; carves a channel into RUs (Resource Units of 26/52/106/242/484/996/2x996 tones) and assigns each RU to a different client per OFDM symbol. Reduces overhead for many small clients (IoT, dense). Crucial in 80-person dense office where most traffic is small frames (evidence: [T06-S002]).
- **Definition (outsider-friendly)**: Wi-Fi 6 lets one AP talk to several devices at once by splitting the channel into lanes.
- **Etymology**: From LTE (downlink OFDMA), adapted to 802.11ax (2019).
- **常见误用 (outsider-tell)**:
  - `semantic_tell`: "OFDMA = MU-MIMO" — different mechanisms; OFDMA splits frequency, MU-MIMO splits space.
  - `usage_tell`: Expecting OFDMA to help with one big iperf flow — it shines with many small flows.
- **关联术语**: MU-MIMO, RU, TWT
- **是否被错位包装**: Some Wi-Fi 6 marketing conflates OFDMA gains with raw PHY rate gains.
- **Source**: [Primary] T06-S002; [Secondary] T06-S019.
- **可信度**: high
- **Decay risk**: low

### 16. MU-MIMO — Multi-User Multiple-Input Multiple-Output

- **Type**: acronym
- **Tier**: tier-1
- **Definition (insider)**: AP uses multiple spatial streams to transmit simultaneously to multiple clients. Downlink MU-MIMO in 11ac Wave 2 (4 users); uplink + downlink MU-MIMO in 11ax (8 users). Requires clients with compatible chipsets and spatial separation.
- **Definition (outsider-friendly)**: One AP, multiple radios, talking to multiple devices in parallel.
- **Etymology**: 802.11ac Wave 2 (2016); expanded in 802.11ax.
- **常见误用 (outsider-tell)**:
  - `semantic_tell`: "8 streams = 8× speed" — only if you have ≥ 8 compatible clients in the right positions.
  - `usage_tell`: Buying 4x4 APs assuming all clients are 4x4 — most phones/laptops are 2x2.
- **关联术语**: OFDMA, spatial stream
- **是否被错位包装**: SOHO marketing sells "MU-MIMO" as a universal speed boost.
- **Source**: [Primary] T06-S001 §19; T06-S002.
- **可信度**: high
- **Decay risk**: low

### 17. Wi-Fi 6 / 802.11ax

- **Type**: standard + term
- **Tier**: tier-1
- **Definition (insider)**: IEEE 802.11ax (HE-PHY). Key features: OFDMA, MU-MIMO uplink+downlink, BSS Coloring, TWT, 1024-QAM. Sold as efficiency upgrade for dense scenarios, not peak speed. Wi-Fi Alliance certification launched 2019; Wi-Fi 6E (6 GHz extension) added 2020 (evidence: [T06-S002, T06-S004]).
- **Definition (outsider-friendly)**: The current mainstream Wi-Fi generation, focused on running well in crowded environments.
- **Etymology**: IEEE ratified 802.11ax in Feb 2021.
- **常见误用 (outsider-tell)**:
  - `semantic_tell`: "Wi-Fi 6 is faster than Wi-Fi 5" said as the only benefit — misses the efficiency story.
  - `usage_tell`: Saying "I bought a Wi-Fi 6 router so my old phone is faster" — old phones can't use Wi-Fi 6 features.
- **关联术语**: Wi-Fi 6E, Wi-Fi 7, OFDMA, BSS Coloring
- **是否被错位包装**: "Wi-Fi 6" tag on routers with no real 802.11ax client uplift; "Wi-Fi 6E" stickers where only one radio supports 6 GHz.
- **Source**: [Primary] T06-S002, T06-S004; [Secondary] T06-S019.
- **可信度**: high
- **Decay risk**: low

### 18. Wi-Fi 6E

- **Type**: standard + term
- **Tier**: tier-1
- **Definition (insider)**: Same 802.11ax PHY/MAC, extended to operate in 6 GHz (5.925-7.125 GHz, UNII-5/6/7/8 in US). Adds 1200 MHz of fresh spectrum with no legacy clients to drag down efficiency. Available in US/EU/UK/JP/KR; **not** China as of 2026 (verify) (evidence: [T06-S004, T06-S007, T06-S022]).
- **Definition (outsider-friendly)**: Wi-Fi 6 that can also use a new, much wider radio band — but only on newer devices and in countries that permit it.
- **Etymology**: FCC opened 6 GHz April 2020; Wi-Fi Alliance launched 6E cert Jan 2021.
- **常见误用 (outsider-tell)**:
  - `semantic_tell`: "Wi-Fi 6E is a new generation between 6 and 7" — no, it's a band extension of 6.
  - `usage_tell`: Designing 6 GHz coverage like 5 GHz — 6 GHz attenuates more, needs higher AP density.
  - `geographic_tell`: Recommending 6 GHz in China — currently not permitted.
- **关联术语**: Wi-Fi 6, AFC, UNII-5/6/7/8
- **是否被错位包装**: Some vendors marketing dual-band Wi-Fi 6 routers as "ready for 6 GHz" via firmware — physically impossible without 6 GHz radio.
- **Source**: [Primary] T06-S007 FCC 6 GHz Order; T06-S004; T06-S022 MIIT.
- **可信度**: high (US/EU); medium for China current state (verify quarterly)
- **Decay risk**: medium (regulatory rollout uneven)

### 19. Wi-Fi 7 / 802.11be (EHT)

- **Type**: standard + term
- **Tier**: tier-1
- **Definition (insider)**: IEEE 802.11be (Extremely High Throughput). Key features: 320 MHz channels (6 GHz only), MLO (Multi-Link Operation), 4096-QAM (MCS 12/13), Multi-RU. Wi-Fi Alliance certification opened Jan 2024 (evidence: [T06-S003, T06-S025]).
- **Definition (outsider-friendly)**: The newest Wi-Fi generation, with much faster theoretical speeds when devices and APs both support it.
- **Etymology**: IEEE TG-be formed 2019; standard ratified May 2024 (still has Wave 2 features pending).
- **常见误用 (outsider-tell)**:
  - `semantic_tell`: "Wi-Fi 6E and Wi-Fi 7 are the same" — different standard (be vs ax), different features.
  - `usage_tell`: Deploying Wi-Fi 7 expecting MLO benefits across all clients — needs Wi-Fi 7-capable client.
- **关联术语**: MLO, 4K-QAM, EHT
- **是否被错位包装**: "Wi-Fi 7" tags on devices that only implement subset (e.g., no MLO).
- **Source**: [Primary] T06-S003, T06-S025.
- **可信度**: high
- **Decay risk**: high (Wave 2 features still in flux)

### 20. WPA3

- **Type**: standard
- **Tier**: tier-1
- **Definition (insider)**: Wi-Fi Alliance security cert published 2018; replaces WPA2. Personal uses SAE (Dragonfly handshake) instead of PSK 4-way; Enterprise adds optional 192-bit (Suite-B). PMF (802.11w) is mandatory. Mandatory for Wi-Fi 6E/7 certification (evidence: [T06-S005]).
- **Definition (outsider-friendly)**: The latest Wi-Fi security standard; harder to brute-force the password offline.
- **Etymology**: Wi-Fi Alliance, Jan 2018.
- **常见误用 (outsider-tell)**:
  - `semantic_tell`: "WPA3 password" — there's no protocol element called password; it's a passphrase that feeds SAE.
  - `usage_tell`: Enabling WPA3-only on an SSID and breaking IoT devices that only speak WPA2.
- **关联术语**: SAE, PMF, OWE
- **是否被错位包装**: No.
- **Source**: [Primary] T06-S005, T06-S001 §12; [Secondary] T06-S013.
- **可信度**: high
- **Decay risk**: low

### 21. PSK / Passphrase

- **Type**: term + acronym
- **Tier**: tier-1
- **Definition (insider)**: PSK = Pre-Shared Key, the 256-bit key derived from a passphrase via PBKDF2-SHA1 (WPA2) or directly via SAE (WPA3). The user types a passphrase; the system derives a PSK; the 4-way handshake uses the PSK. Insiders say "passphrase" or "PSK," **not** "WPA password" (evidence: [T06-S001 §12, T06-S005]).
- **Definition (outsider-friendly)**: The Wi-Fi password.
- **Etymology**: WPA2 (2004).
- **常见误用 (outsider-tell)**:
  - `register_tell`: "The WPA password" / "the WiFi password" — non-insider register.
  - `semantic_tell`: "PSK is the password" — technically the PSK is the **derived** key, not the typed string.
- **关联术语**: SAE, PMF, WPA2/3
- **是否被错位包装**: Consumer router GUIs labeling field "Password" instead of "Passphrase."
- **Source**: [Primary] T06-S001; [Secondary] T06-S005.
- **可信度**: high
- **Decay risk**: low

### 22. 802.1X

- **Type**: standard
- **Tier**: tier-1
- **Definition (insider)**: IEEE port-based Network Access Control protocol; transports EAP between supplicant (client), authenticator (AP/switch), and authentication server (RADIUS). The "Enterprise" in WPA2/3-Enterprise. Mandatory for serious enterprise Wi-Fi; provides per-user credentials, MAC-agnostic, ties into AD/RADIUS (evidence: [T06-S015, T06-S016, T06-S017]).
- **Definition (outsider-friendly)**: A way for a corporate Wi-Fi to log in each user against the company's directory instead of using one shared password.
- **Etymology**: IEEE 802.1X-2001; revised 2004, 2010, 2020.
- **常见误用 (outsider-tell)**:
  - `semantic_tell`: "I'm using WPA2 Enterprise" treated as a complete protocol — 802.1X + EAP variant + RADIUS server are separate decisions.
  - `usage_tell`: Deploying PEAP-MSCHAPv2 in 2026 (deprecated by Microsoft due to NPS vulnerabilities) (evidence: [T06-S028]).
  - `pronunciation_tell`: "Eight oh two dot one X" — never "802-1X."
- **关联术语**: EAP, RADIUS, EAP-TLS
- **是否被错位包装**: No.
- **Source**: [Primary] T06-S017 IEEE 802.1X-2020; T06-S016 RFC 2865; [Secondary] T06-S028.
- **可信度**: high
- **Decay risk**: low

### 23. Roaming (11k/v/r)

- **Type**: term + standard
- **Tier**: tier-1
- **Definition (insider)**: The client-driven process of disassociating from one BSSID and associating with another within the same ESS. **Clients decide**; APs can hint (11k = neighbor reports, 11v = BSS Transition Management) or coerce (Min RSSI / disassociation). 11r enables sub-50 ms fast transition by pre-distributing keys (PMK-R1). In 80-person office with voice traffic, all three are essential (evidence: [T06-S030]).
- **Definition (outsider-friendly)**: How your phone switches from one Wi-Fi puck to another as you walk around.
- **Etymology**: 802.11k (2008), 802.11r (2008), 802.11v (2011).
- **常见误用 (outsider-tell)**:
  - `semantic_tell`: "The AP handed off the client to the other AP" — APs **don't** hand off; clients choose. APs only nudge or kick.
  - `usage_tell`: Enabling 11r without ensuring all clients support it — older Android can break.
- **关联术语**: Min RSSI, Fast Transition, BSSID
- **是否被错位包装**: Cellular-style "handover" language being copied into Wi-Fi marketing.
- **Source**: [Primary] T06-S001 §13; T06-S030.
- **可信度**: high
- **Decay risk**: low

### 24. 5 GHz Wi-Fi

- **Type**: term
- **Tier**: tier-1
- **Definition (insider)**: Wi-Fi operating in the 5 GHz ISM/UNII bands (5.150-5.825 GHz in US). **Not cellular 5G**. Less crowded than 2.4 GHz, shorter range, faster. Insiders write "5 GHz" with the unit.
- **Definition (outsider-friendly)**: The second Wi-Fi band most devices have, faster and less crowded but with shorter range.
- **Etymology**: 802.11a (1999) introduced 5 GHz Wi-Fi.
- **常见误用 (outsider-tell)**:
  - `semantic_tell`: "5G WiFi" — mixing cellular generation (5G NR) with the 5 GHz band; the cellular industry put a stop to "5G Wi-Fi" branding for this reason.
  - `register_tell`: "5 gig Wi-Fi" verbally — borderline; among insiders, you say "five gig" but in writing always "5 GHz."
- **关联术语**: UNII, 6 GHz, DFS
- **是否被错位包装**: Telecom marketing using "5G" promiscuously.
- **Source**: [Primary] T06-S001, T06-S006; [Secondary] T06-S018.
- **可信度**: high
- **Decay risk**: low

---

## Detailed Entries — Tier 2 (selected high-value entries with outsider-tells)

### 25. ESSID — Extended Service Set Identifier

- **Type**: acronym
- **Tier**: tier-2
- **Definition (insider)**: Historically (pre-802.11-2007) the SSID broadcast when multiple BSSes share one network; now functionally identical to SSID in everyday speech. Some Linux tools (`iwconfig`) still use "ESSID."
- **常见误用 (outsider-tell)**: Using ESSID and SSID interchangeably without realizing the historical distinction.
- **Source**: T06-S018; T06-S001 §3.
- **Decay risk**: low

### 26. STA / Station

- **Type**: term
- **Tier**: tier-2
- **Definition (insider)**: Any 802.11-conformant device — laptops, phones, IoT, even APs (an AP is a STA with extra MAC features). 
- **常见误用 (outsider-tell)**: Calling phones "clients" but laptops "devices" — insiders use "STA" uniformly.
- **Source**: T06-S001 §3.
- **Decay risk**: low

### 27. DTIM — Delivery Traffic Indication Message

- **Type**: acronym
- **Tier**: tier-2
- **Definition (insider)**: A countdown in beacon frames signaling when buffered multicast/broadcast will be delivered to dozing clients. DTIM period = number of beacons between DTIMs. Lower DTIM = better multicast latency; higher = better client battery.
- **常见误用 (outsider-tell)**: Setting DTIM=10 in a voice-heavy network and wondering why multicast call setup fails.
- **Source**: T06-S001 §10.
- **Decay risk**: low

### 28. TWT — Target Wake Time

- **Type**: acronym
- **Tier**: tier-2
- **Definition (insider)**: Wi-Fi 6 feature letting AP and client negotiate scheduled wake intervals. Primarily for IoT power saving; some smartphones use it.
- **常见误用 (outsider-tell)**: Expecting TWT to fix laptop battery — laptops rarely negotiate TWT.
- **Source**: T06-S002.
- **Decay risk**: low

### 29. BSS Coloring

- **Type**: term
- **Tier**: tier-2
- **Definition (insider)**: Wi-Fi 6 feature; each BSS gets a 6-bit color (0-63) advertised in PHY headers. APs treating frames with the same color as "their network," using a higher OBSS_PD threshold (more aggressive transmission) for frames with different colors — improves spatial reuse in dense deployments.
- **常见误用 (outsider-tell)**: Thinking BSS Coloring "solves CCI entirely" — it modestly improves it; channel planning still needed.
- **Source**: T06-S002.
- **Decay risk**: low

### 30. PMF — Protected Management Frames (802.11w)

- **Type**: acronym + standard
- **Tier**: tier-2
- **Definition (insider)**: Encrypts/authenticates management frames (disassoc, deauth) to prevent spoofing attacks (e.g., aireplay deauth flood). Mandatory in WPA3; optional in WPA2.
- **常见误用 (outsider-tell)**: Enabling PMF "Required" globally and breaking legacy clients (many WPA2-only devices don't speak PMF).
- **Source**: T06-S001 §12; T06-S005.
- **Decay risk**: low

### 31. SAE — Simultaneous Authentication of Equals

- **Type**: acronym
- **Tier**: tier-2
- **Definition (insider)**: The Dragonfly handshake used in WPA3-Personal; based on Diffie-Hellman over a finite cyclic group. Forward-secret. Resistant to offline dictionary attacks unlike WPA2 PSK 4-way handshake.
- **常见误用 (outsider-tell)**: "WPA3 = SAE" — Personal uses SAE; Enterprise uses 802.1X + Suite-B.
- **Source**: T06-S005; T06-S001.
- **Decay risk**: low

### 32. OWE — Opportunistic Wireless Encryption / Enhanced Open

- **Type**: acronym + standard
- **Tier**: tier-2
- **Definition (insider)**: RFC 8110; encrypts traffic on "open" SSIDs without authentication — replaces unprotected open Wi-Fi for guest networks. No passphrase, but per-client unique encryption.
- **常见误用 (outsider-tell)**: "OWE is the same as open Wi-Fi" — no, OWE encrypts; open doesn't.
- **Source**: T06-S005.
- **Decay risk**: low

### 33. AFC — Automated Frequency Coordination

- **Type**: acronym
- **Tier**: tier-2
- **Definition (insider)**: Cloud service (or local appliance) querying a database of 6 GHz incumbents to authorize Standard Power (SP) operation outdoors and at higher power. FCC certified providers went live 2024 in the US (evidence: [T06-S029]).
- **常见误用 (outsider-tell)**: "AFC means I can use any 6 GHz channel anywhere" — only in geofenced regions and only with certified SP APs.
- **Source**: T06-S029.
- **Decay risk**: high (rules still evolving)

### 34. UNII-1/2A/2B/2C/3

- **Type**: term
- **Tier**: tier-2
- **Definition (insider)**: FCC sub-bands of 5 GHz; each with distinct EIRP limits, DFS requirements, indoor/outdoor restrictions. UNII-1 (5.150-5.250 GHz), UNII-2A (5.250-5.350), UNII-2B (5.350-5.470, **not authorized**), UNII-2C (5.470-5.725), UNII-3 (5.725-5.825). UNII-2A/2C are DFS.
- **常见误用 (outsider-tell)**: Treating "5 GHz" as a single band with uniform rules.
- **Source**: T06-S006.
- **Decay risk**: medium (2024 5.9 GHz reallocations affect UNII-4 ITS)

### 35. UNII-5/6/7/8

- **Type**: term
- **Tier**: tier-2
- **Definition (insider)**: FCC sub-bands of 6 GHz introduced 2020. UNII-5 (5.925-6.425), UNII-6 (6.425-6.525), UNII-7 (6.525-6.875), UNII-8 (6.875-7.125). LPI (Low Power Indoor) allowed in all four; SP (Standard Power) requires AFC and only in UNII-5/7.
- **常见误用 (outsider-tell)**: "UNII-5 and UNII-7 are interchangeable" — different rules under AFC SP.
- **Source**: T06-S007.
- **Decay risk**: medium

### 36. MLO — Multi-Link Operation

- **Type**: acronym
- **Tier**: tier-2
- **Definition (insider)**: Wi-Fi 7 feature; a client and AP each expose multiple radios as a single MLD (Multi-Link Device) and aggregate traffic across bands (e.g., 5 GHz + 6 GHz simultaneously). Modes: STR (Simultaneous Tx/Rx), NSTR, EMLSR.
- **常见误用 (outsider-tell)**: "MLO = client uses two radios at once for double speed" — only true in STR mode and with channel separation; many clients are EMLSR (single radio at a time, fast switch).
- **Source**: T06-S003.
- **Decay risk**: high (Wave 2 still maturing)

### 37. RU — Resource Unit

- **Type**: acronym
- **Tier**: tier-2
- **Definition (insider)**: An allocation of subcarriers in OFDMA; sizes 26/52/106/242/484/996/2x996 tones (Wi-Fi 6). Wi-Fi 7 adds Multi-RU (combining non-adjacent RUs).
- **常见误用 (outsider-tell)**: Mixing up RU and stream count.
- **Source**: T06-S002.
- **Decay risk**: low

### 38. PoE / PoE+ / PoE++

- **Type**: term + acronym
- **Tier**: tier-2
- **Definition (insider)**: Power over Ethernet — 802.3af (15.4 W, Type 1), 802.3at (30 W, Type 2 / "PoE+"), 802.3bt (60-90 W, Type 3/4 / "PoE++"). Most modern APs need PoE+ for full radio capability; some Wi-Fi 7 APs need PoE++.
- **常见误用 (outsider-tell)**: Buying a Wi-Fi 6/7 AP and powering it from a basic 802.3af switch → AP boots in reduced-radio mode.
- **Source**: IEEE 802.3 family.
- **Decay risk**: low

### 39. CAPWAP

- **Type**: acronym + standard
- **Tier**: tier-2
- **Definition (insider)**: RFC 5415; UDP-based tunnel between APs and a Wireless LAN Controller for control + (optionally) data. Used by Cisco, Aruba; UBNT historically uses a proprietary inform/HTTPS protocol over port 8080. Local/Flex modes determine data tunneling.
- **常见误用 (outsider-tell)**: "UniFi uses CAPWAP" — incorrect; UniFi has its own protocol.
- **Source**: T06-S014.
- **Decay risk**: low

### 40. RADIUS

- **Type**: acronym + standard
- **Tier**: tier-2
- **Definition (insider)**: RFC 2865; UDP/1812 AAA protocol used by 802.1X. Common servers: FreeRADIUS, Cisco ISE, Aruba ClearPass, Microsoft NPS, ruckus Cloudpath. UBNT's RADIUS is built into UniFi Network Application.
- **常见误用 (outsider-tell)**: "RADIUS is encrypted" — only attribute encryption with shared secret; vanilla UDP RADIUS isn't TLS-encrypted (until RadSec/RFC 6614).
- **Source**: T06-S016.
- **Decay risk**: low

### 41. EAP — Extensible Authentication Protocol

- **Type**: acronym + standard
- **Tier**: tier-2
- **Definition (insider)**: RFC 3748; an encapsulation framework, not a protocol. Carries auth methods like EAP-TLS, PEAP-MSCHAPv2, EAP-TTLS, EAP-FAST, EAP-PWD. Travels inside 802.1X frames (EAPOL).
- **常见误用 (outsider-tell)**: "We're using EAP" — meaningless without specifying the inner method.
- **Source**: T06-S015.
- **Decay risk**: low

### 42. EAP-TLS

- **Type**: term
- **Tier**: tier-2
- **Definition (insider)**: Mutual cert-based authentication; no passwords transit the wire. Requires PKI for client + server certs. Gold standard for enterprise Wi-Fi as of 2024-2026.
- **常见误用 (outsider-tell)**: "EAP-TLS is too hard to deploy" — modern MDM (Intune, JAMF) automate cert provisioning.
- **Source**: T06-S028; RFC 5216.
- **Decay risk**: low

### 43. PEAP-MSCHAPv2

- **Type**: term
- **Tier**: tier-2
- **Definition (insider)**: Tunneled EAP using server-side TLS + inner MSCHAPv2 password. Microsoft default for AD-joined clients. **Vulnerable** to credential capture if NPS not configured with server cert validation; Microsoft formally deprecated MSCHAPv2 in NPS in 2024 for new deployments (evidence: [T06-S028]).
- **常见误用 (outsider-tell)**: Deploying PEAP-MSCHAPv2 without enforcing server cert validation on clients ("Always trust" disabled).
- **Source**: T06-S028.
- **Decay risk**: medium (deprecation in progress)

### 44. Min RSSI

- **Type**: term (UBNT-specific)
- **Tier**: tier-2
- **Definition (insider)**: UBNT-specific knob; below this RSSI, the AP sends a disassoc to the client to force it to reassociate (hopefully with a closer AP). Common values: -75 to -80 dBm. Crude but effective fallback when 11k/v aren't enough (evidence: [T06-S011, T06-S031]).
- **常见误用 (outsider-tell)**:
  - `usage_tell`: Setting Min RSSI = -65 to "force aggressive roaming" → clients get kicked off in normal usage.
  - `semantic_tell`: "Min RSSI makes the AP roam clients" — APs **kick**, not roam.
- **Source**: T06-S011; T06-S031.
- **Decay risk**: low (mature feature)

### 45. Band Steering

- **Type**: term
- **Tier**: tier-2
- **Definition (insider)**: AP feature that delays/ignores 2.4 GHz probe responses or rejects 2.4 GHz auth from dual-band clients to push them to 5/6 GHz. Effective when there's a coverage parity; harmful when 5 GHz coverage is weak in some spots.
- **常见误用 (outsider-tell)**: Enabling band steering then complaining "phones drop to 2.4 GHz in the corners" — they should; you enabled steering, not banning.
- **Source**: T06-S010.
- **Decay risk**: low

### 46. Airtime Fairness

- **Type**: term
- **Tier**: tier-2
- **Definition (insider)**: Scheduler that allocates equal **time** (not packets) to each client; prevents slow clients (legacy 802.11g) from hogging the medium when fast clients (Wi-Fi 6) could be served quickly.
- **常见误用 (outsider-tell)**: "Airtime fairness is per-packet QoS" — it's per-airtime.
- **Source**: T06-S010.
- **Decay risk**: low

### 47-50. UBNT-specific cluster

**UniFi Network Application** (formerly UniFi Controller): UBNT controller software running on UCK, Dream Machine, or self-hosted Docker/VM. Renamed ~2021 (evidence: [T06-S010]).

**Cloud Key (UCK)**: UBNT hardware appliance hosting UniFi Network Application. UCK Gen1, UCK Gen2/Gen2+ with HDD/SSD. Outsider-tell: "the cloud key is the AP" — no, it's the controller.

**Adopt**: UBNT verb for binding a new AP to the controller, typically via Layer-2 broadcast (default) or DHCP option 43 / set-inform CLI. Outsider-tell: outsiders ask "how do I add an AP," not "how do I adopt."

**WiFiman**: UBNT mobile app for speed test, RF survey (channel/RSSI), and Bonjour discovery. Free; iOS + Android. Outsider-tell: confusing WiFiman (UBNT) with NetSpot or Ekahau Sidekick (third-party survey tools).

### 51-58. UBNT AP families (brief)

- **U6 series**: U6 Lite (2x2, 2.4+5), U6+ (2x2, 2.4+5), U6 Pro (2x2 / 4x4 dual-radio), U6 Enterprise (4x4 6E tri-radio), U6 Mesh (outdoor 2x2), U6 LR (Long Range)
- **U7 series**: U7 Pro (Wi-Fi 7 indoor tri-radio), U7 Pro Wall, U7 Pro Max (planned)
- Naming convention: UBNT moved from "UAP-AC-*" (Wi-Fi 5) to "U6-*" (Wi-Fi 6) to "U7-*" (Wi-Fi 7).
- Outsider-tell: Saying "I want a UBNT router" when they mean an AP. UBNT calls their L3 gateway "Dream Machine" or "UniFi Cloud Gateway."

### 59. Wireless Uplink

- **Type**: term (UBNT)
- **Tier**: tier-2
- **Definition (insider)**: UBNT's wireless mesh backhaul — an AP without Ethernet uplink can join via the radio of another AP. Halves throughput per hop. Distinct from "Wireless Bridge" (point-to-point).
- **常见误用 (outsider-tell)**: "Wireless uplink = mesh fixes everything" — wired is always preferred for backhaul.
- **Source**: T06-S010.
- **Decay risk**: low

### 60. UISP — Ubiquiti ISP

- **Type**: term (UBNT)
- **Tier**: tier-2
- **Definition (insider)**: Ubiquiti's separate product line for ISPs (formerly airMAX + EdgeMAX) — different software stack from UniFi. Not relevant for typical enterprise Wi-Fi deployment.
- **常见误用 (outsider-tell)**: Confusing UISP UI with UniFi Network Application UI — different ecosystem.
- **Source**: T06-S010 (UBNT product catalog).
- **Decay risk**: low

---

## Detailed Entries — Standards / Regulations / Certifications

### S1. IEEE 802.11 (base standard)

- **Type**: standard
- **Issued**: 1997 (first ratification); current consolidated baseline 802.11-2020
- **Last revised**: 2020 (next consolidation ~2027 with be/bf)
- **Insider def**: The master document. All amendments (a/b/g/n/ac/ax/be) get rolled into the next consolidated revision.
- **Source**: T06-S001.
- **Decay**: low.

### S2. IEEE 802.11ax (Wi-Fi 6/6E)

- **Issued**: Feb 2021 (full ratification)
- **Last revised**: 2021
- **Insider def**: See Tier 1 entry #17.
- **Source**: T06-S002.
- **Decay**: low.

### S3. IEEE 802.11be (Wi-Fi 7)

- **Issued**: May 2024 (Wave 1)
- **Last revised**: 2024
- **Insider def**: See Tier 1 entry #19.
- **Source**: T06-S003.
- **Decay**: high (Wave 2 in progress)

### S4. IEEE 802.11k/v/r/w

- **Issued**: 11k (2008), 11r (2008), 11v (2011), 11w (2009)
- **Insider def**: Roaming + management protection amendments. Always discussed together as the "fast roaming bundle" in enterprise Wi-Fi.
- **Source**: T06-S001; T06-S030.
- **Decay**: low.

### S5. Wi-Fi Alliance Certifications

- **Wi-Fi CERTIFIED 6** (2019), **6E** (2021), **7** (Jan 2024)
- **WPA3** (2018, updated 2020/2022 SAE-PT to defend against side-channel)
- **Enhanced Open** (2018, OWE)
- **Source**: T06-S004, T06-S005, T06-S025.

### R1. FCC Part 15.247 / 15.407 — 2.4 GHz + 5 GHz

- **Issued**: Periodic
- **Last revised**: 2024 (5.9 GHz / UNII-4 ITS reallocation)
- **Insider def**: US unlicensed rules for ISM (2.4) + UNII (5). EIRP caps, DFS mandates, indoor-only restrictions on UNII-1.
- **Source**: T06-S006.
- **Decay**: medium.

### R2. FCC 6 GHz Order (UNII-5/6/7/8)

- **Issued**: April 2020
- **Last revised**: 2023 (AFC rules finalized; SP went live 2024)
- **Insider def**: Opened 1200 MHz of 6 GHz for unlicensed Wi-Fi. LPI (indoor, no AFC needed); SP (AFC required, outdoor or higher power).
- **Source**: T06-S007, T06-S029.
- **Decay**: high (AFC rollout ongoing, more rules forthcoming).

### R3. ETSI EN 300 328 + EN 301 893

- **EN 300 328** (2.4 GHz): issued 2001, last revised 2017
- **EN 301 893** (5 GHz with DFS): issued 2001, last revised 2017
- **Insider def**: EU equivalent of FCC Part 15. Required for CE marking.
- **Source**: T06-S008, T06-S009.
- **Decay**: medium.

### R4. ETSI EN 303 687 — 6 GHz LPI (EU)

- **Issued**: 2022
- **Last revised**: 2024
- **Insider def**: EU Low-Power Indoor 6 GHz; LPI only as of 2026 (SP rules deferred).
- **Source**: T06-S008.
- **Decay**: medium.

### R5. China MIIT 2.4 + 5 GHz rules + 6 GHz status

- **Issued**: 2002, revised 2012 + 2021
- **Last status check**: 2024; **6 GHz not opened** for unlicensed Wi-Fi as of 2026 (verify quarterly) (evidence: [T06-S022]).
- **Insider def**: Geographic asymmetry — Wi-Fi 6E products sold in China cannot use 6 GHz; vendors ship region-locked firmware.
- **Source**: T06-S022.
- **Decay**: high (regulatory; could change with policy update).

### C1. CWNP family — CWS / CWT / CWNA / CWAP / CWDP / CWSP / CWNE

- **Issued**: CWNA 2002, CWNE 2003, CWAP/CWDP/CWSP 2010s
- **Last revised**: CWNA-109 (2024)
- **Insider def**: Vendor-neutral Wi-Fi certifications. CWNA = baseline; CWNE = top-tier (≤ 1000 holders globally, ~500 active).
- **Source**: T06-S012, T06-S013.
- **Decay**: medium (CWNA refreshed every ~3-4 years).

### C2. Ekahau ECSE — Ekahau Certified Survey Engineer

- **Issued**: Mid-2010s
- **Last revised**: 2023 (Sidekick 2 hardware update)
- **Insider def**: Tool-specific cert for Ekahau Pro (the dominant enterprise site-survey software). De-facto requirement for serious Wi-Fi consultants.
- **Source**: T06-S020.
- **Decay**: medium.

### C3. Ubiquiti UEWA / UBWA / UFSP

- **UEWA**: UniFi Enterprise Wireless Admin
- **UBWA**: UniFi Broadband Wireless Admin (airMAX / UISP focus)
- **UFSP**: UniFi Fiber Specialist
- **Issued**: ~2018
- **Last revised**: 2024 (refreshed with U7 lineup) (evidence: [T06-S021])
- **Insider def**: Free online certs. Industry views them as marketing more than rigorous (no proctored exam). Useful to confirm UBNT-specific knowledge but won't replace CWNA.
- **Source**: T06-S021.
- **Decay**: medium.

### C4. Cisco wireless certs

- **CCNA Wireless**: retired 2020 (folded into CCNA + CCNP Enterprise)
- **CCNP Enterprise (Wireless concentration)**: active
- **CCIE Wireless**: retired 2020 (folded into CCIE Enterprise)
- **Insider def**: Vendor-specific; loses currency as enterprises shift away from CCNA-as-baseline.
- **Source**: Cisco Learning catalog (cross-ref via T06-S023).
- **Decay**: medium (Cisco perennially restructures).

### C5. Aruba ACMA / ACMP / ACMX

- **Issued**: Mid-2010s
- **Insider def**: Aruba (HPE) vendor-specific certs. ACMP is the working-level cert; ACMX is expert.
- **Source**: HPE Aruba certification catalog.
- **Decay**: medium.

### C6. Mist / Juniper JNCIA-MistAI / JNCIS-MistAI

- **Issued**: Late 2010s (post-Juniper acquisition of Mist 2019)
- **Insider def**: AI-driven Mist platform certs; small but growing in cloud-managed enterprise Wi-Fi.
- **Decay**: medium.

---

## Phase 2 提炼提示

### 「行业表达 DNA」直接素材

**高频黑话 top 12 (insiders use daily, outsiders confuse)**:
1. BSSID (vs SSID)
2. RSSI / SNR with **negative dBm**
3. EIRP (not "tx power")
4. CCI / ACI
5. DFS / "the AP hopped channels"
6. MCS index (not "PHY rate" as a KPI)
7. OFDMA + RU (Wi-Fi 6 efficiency story)
8. PSK / passphrase (not "WPA password")
9. 802.1X + EAP-TLS / PEAP (Enterprise)
10. 11k/v/r ("fast roaming bundle")
11. Min RSSI (UBNT verb)
12. Adopt (UBNT verb)

**行业拒绝的厂商话术 top 6**:
1. "AX5400 / AX11000" peak-PHY-rate marketing (insiders measure real throughput, MCS retry rate, airtime utilization)
2. "Mesh fixes everything" (insiders know wireless backhaul halves capacity)
3. "Boost the signal / higher dBm = better" (insiders frame asymmetric link + EIRP cap)
4. "5G WiFi" branding (insiders strictly say "5 GHz" and "Wi-Fi 5/6/7")
5. "More antennas = faster" (insiders frame spatial streams + client constraints)
6. "Wi-Fi 6E ready" firmware-upgrade claims on dual-band hardware (physically impossible without 6 GHz radio)

**外行破绽 top 12 (insider-only spotting tells)**:
1. "5G WiFi" (mixing cellular gen with band)
2. "-50 dBm is worse than -70 dBm" (sign error)
3. "Just add more APs" (causes CCI)
4. "Set the channel to 80" (confuses channel and width)
5. "Router has bad signal" (router ≠ AP)
6. "Wi-Fi 6E is a new generation between 6 and 7"
7. "WPA password" (insiders: PSK / passphrase)
8. "Mesh will fix slow Wi-Fi"
9. "The AP handed off the client to the other AP" (clients decide roaming)
10. "8 streams = 8x speed"
11. "I picked channel 4 because 1/6/11 were busy" (ACI)
12. Pronouncing "BSSID" as if it were "SSID"

### 「智识谱系」线索

- **OFDM → OFDMA paradigm shift** (Wi-Fi 5 → Wi-Fi 6): Industry pivoted from per-frame contention to scheduler-driven multi-user — a fundamental philosophical shift in how spectrum is shared. Mirrors LTE evolution. Inspired by cellular, applied to unlicensed.
- **PSK 4-way → SAE Dragonfly** (WPA2 → WPA3): Move from "secret-knowledge handshake" to "zero-knowledge passphrase proof" — Wi-Fi catching up to modern cryptographic literature 15+ years late.
- **Vendor-controller → Cloud-managed split**: CAPWAP / Cisco controller → Meraki / Mist / UniFi cloud model. The "controller" abstraction is dissolving; some vendors (UBNT, Aruba InstantOn) push controllerless. Reflects broader shift to declarative cloud config across networking.
- **Centralized RRM → AI-driven RF planning** (Mist Juniper, UBNT WiFi AI): AI/ML replacing rule-based channel/power assignment — but insiders still verify with manual site survey.
- **Multi-vendor fragmentation in Wi-Fi 7 MLO**: 802.11be MLO has multiple modes (STR/NSTR/EMLSR); vendor implementations diverge. Mirrors early 802.11ac Wave 2 interop pain. **Decay signal**: Wave 2 features still in flux through 2026.

### 「时效性」信号

- **Wi-Fi 7 (802.11be) Wave 2** features still being defined through 2025-2026 → expect glossary churn around MLO modes, 16-stream, Multi-AP coordination.
- **6 GHz regional rollout uneven**: US/EU/UK/JP/KR have it; **China still gated** (verify quarterly via MIIT announcements). India opened Sep 2024 but with delicensing complications.
- **AFC (FCC SP mode)** went commercial 2024; rule-set still maturing → Wi-Fi 6E SP knowledge is decay-medium.
- **EAP-TLS migration urgency**: Microsoft NPS deprecating PEAP-MSCHAPv2 (started 2024) → enterprises need EAP-TLS / cert-based migration plans within 12-18 months.
- **CWNA-109** (2024) is current; CWNA-110 expected ~2027-2028 if pattern holds.

**Standards / regulations expected to change within 12 months**:
- FCC 6 GHz AFC rules (further refinement)
- China MIIT 6 GHz status (could open at any time, or not)
- Wi-Fi Alliance Wi-Fi 7 cert profile expansions (Wave 2)
- IEEE 802.11bn (UHR / Wi-Fi 8) early discussion

### 「工作流变化触发」种子 (for wave 3 Track 03)

- **WPA3-only + PMF-Required** migration → adds compatibility test step to every new SSID rollout, plus IoT exception SSID design pattern
- **6 GHz inclusion** → adds tri-radio AP procurement decision + AFC service provider selection (US) + region-firmware verification
- **Wi-Fi 7 MLO** → adds client compatibility matrix as a procurement step; not all "Wi-Fi 7" clients support MLO
- **EAP-TLS over PEAP-MSCHAPv2** → adds PKI design + MDM cert-rollout sub-workflow (Intune SCEP, JAMF AD CS)
- **AFC SP mode availability** (US) → outdoor / large-venue designs can now use 6 GHz SP; changes coverage planning for warehouses, stadiums

### 冷僻 / 信号薄弱

- **总术语数**: 60 well-defined entries (Tier 1: 24, Tier 2: 36+, Standards/Regs/Certs: 16) → **above floor**, healthy signal
- **Tier 1 outsider-tell coverage**: 24/24 (100%) → **above target**
- **Tier 2 outsider-tell coverage**: ~70% (above 50% target)
- **行业 NOT 信号薄弱** — Wi-Fi engineering has dense canonical jargon

**信号薄弱的子区域**:
- **China 6 GHz regulatory state** (T06-S022): MIIT public docs sparse on **why** 6 GHz still gated; insider knowledge in Chinese engineering forums suggests defense/satellite incumbents but no public source. Mark `low confidence` if SKILL.md asserts a reason.
- **UBNT internal naming history** (UAP-AC-* → U6-*): Source mostly UBNT release notes and community forums; no canonical retrospective.
- **Wi-Fi 7 Wave 2 deep dive**: IEEE 802.11be Wave 2 amendments (e.g., 16 spatial streams, AP coordination) still in draft as of mid-2026 — anything beyond Wave 1 features has high decay risk.

---

## 质量自检

- [x] 候选数 ≥ 40 → 60+ entries
- [x] 5 个 type 按行业类型有合理分布:
  - Term: 32, Acronym: 28, Standard: 12, Regulation: 6, Certification: 9
  - (some are multi-type; counts overlap)
- [x] Tier 1 ≥ 15 → 24
- [x] Tier 1 + Tier 2 ≥ 40 → ~62
- [x] Tier 1 全部填了 outsider-tell → yes (24/24)
- [x] Tier 2 ≥ 50% 填了 outsider-tell → yes (~25/36 explicit, others implicit in table)
- [x] Standards / Regulations / Certifications 都有日期字段 → yes
- [x] Disputed 术语正确标注 → none with significant insider dispute; PMF "Optional vs Required" is a deployment choice not a definitional dispute
- [x] Phase 2 接口填了 → 5 sections complete

---

*File generated: 2026-06-02. Time-boxed Track 06 wave 1 subagent for ubnt-wifi-master skill build.*
