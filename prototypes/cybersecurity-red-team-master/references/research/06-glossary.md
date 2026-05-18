# Track 06 — Cybersecurity Red Team / Offensive Security Glossary

红队 / 渗透测试 是一个 **缩写 / 术语 / 标准框架密集到几乎构成独立技术方言** 的行业 — 一个简单的 客户 sync 报告里, 一句 "we caught a beacon after Kerberoasting a SPN account, pivoted via PtT to the DC, dumped NTDS with DCSync, mapped to T1558.003 + T1003.006, CVSS 8.8" 就并发了 5 套独立术语体系: (1) **MITRE ATT&CK TTPs 编号体系** (Tactic TA00xx → Technique T1xxx → Sub-technique T1xxx.00x → Procedure 描述), 是 全行业 single source of truth, ATT&CK v15 (2024) 起进入 ICS / Mobile / Cloud / Containers / Enterprise 五矩阵 + Mitigations + Groups (APT29 / FIN7 / Lazarus) + Software (Cobalt Strike / Empire / Mimikatz) cross-reference, 任何 严肃 红队报告 都必须 map ATT&CK; (2) **Active Directory 攻击专门话术** (Kerberoasting / AS-REP Roasting / Pass-the-Hash / Pass-the-Ticket / Pass-the-Certificate / Golden Ticket / Silver Ticket / Diamond Ticket / Sapphire Ticket / DCSync / DCShadow / Shadow Credentials / NTLM Relay / ADCS ESC1-15), 几乎每个术语都对应 一篇 SpecterOps / harmj0y.net / adsecurity.org 原创 blog 论文 + 一个 Impacket / Rubeus / Certipy 工具 + 一个 ATT&CK Technique ID, 缺一不可; (3) **OPSEC + C2 黑话** (beacon / implant / stager / sleep mask / jitter / Malleable Profile / process injection / process hollowing / DLL sideloading / Hell's Gate / AMSI bypass / ETW bypass / BYOVD / LOLBins / LOLBAS), 来自 Cobalt Strike / Sliver / Mythic / Havoc 工具生态 + Black Hat / DEF CON / OffensiveCon 演讲序列.

(4) **法律 framework** 三套并行: 美国 **CFAA 18 USC 1030** (Computer Fraud and Abuse Act, 1986, 未授权访问 5 年 / 加重 10 年 / 第三巡回 2014 weev 案部分推翻 + Aaron Swartz JSTOR 2011 检察官重判后自杀触发 Aaron's Law CFAA 改革讨论), 英国 **CMA 1990** (Computer Misuse Act, sections 1-3A), 中国 **刑法 285** (非法侵入计算机信息系统罪, 三年以下 + 加重七年) + **286** (破坏计算机信息系统罪, 五年以下 + 加重十年) + **287** (利用计算机信息系统实施犯罪) + **网络安全法 2017 第 27 条** (任何 渗透 即使授权 也需 等保备案 + 公安/网信办报备, 比 US "合同即可" 更严) + **数据安全法 2021** + **个人信息保护法 PIPL 2021** + **关基条例 2021 国务院令 745 号**; 欧盟 **GDPR Article 32** (technical and organizational measures) + 美国行业 **HIPAA / SOX / PCI DSS / GLBA / NIS2**; (5) **vulnerability scoring 体系** 三代并行 (CVSS v3.0 → v3.1 → v4.0 由 FIRST.org 维护) + 互补指标 **EPSS** (Exploit Prediction Scoring System, first.org 概率模型) + **CISA KEV Catalog** (Known Exploited Vulnerabilities, 美国联邦机构强制 patch deadline 来源) + **SSVC** (CISA Stakeholder-Specific Vulnerability Categorization) + **Tenable VPR** (vendor 商用替代); (6) **cert syllabus 黑话** OffSec 系 (OSCP / OSEP / OSEE / OSED / OSWA / OSWE → 合称 OSCE3) + SANS GIAC (GPEN / GXPN / GMOB / GAWN / GCIH / GREM) + Zero-Point Security (CRTO / CRTL) + Altered Security (CRTP / CRTE / CRTM) + ISC2 (CISSP / CCSP) + EC-Council (CEH / CPENT / LPT), 每个 cert 都隐含 一套 方法论 + 工具栈 + 报告 template.

**OPSEC framework 术语** 来自 三套互补 模型: **Cyber Kill Chain (Lockheed Martin 2011, Hutchins / Cloppert / Amin)** 7 阶段线性 (Recon → Weaponization → Delivery → Exploitation → Installation → C2 → Actions on Objectives) → 因 跳过 lateral movement + 内部行为 被批评 → 演化为 **Unified Kill Chain (Paul Pols 2017 + 2022)** 18 阶段 cyclical 含 internal + objective + payoff → 与之并行的 **Diamond Model (Caltagirone / Pendergast / Betz 2013)** 四顶点 (Adversary / Capability / Infrastructure / Victim) 用于 threat intel 归因 → **MITRE ATT&CK** 是上述模型的具体化矩阵, ATT&CK 不是替代 Kill Chain 而是给 Kill Chain 每一阶段填具体 TTPs → **D3FEND (NSA + MITRE 2021)** 是 ATT&CK 的 defensive counterpart, 用于 detection engineering 反推 → **Pyramid of Pain (David Bianco 2013)** 解释 为什么 indicators of compromise (IOC) 从 hash → IP → domain → tools → TTPs 越往上 攻击者 越难替换, 帮 detection engineer 决定 投资优先级 → **MITRE ATLAS** (Adversarial Threat Landscape for AI Systems, 2021+) 是 ML/AI 系统的 ATT&CK 类比.

**Web / API / Mobile / Cloud 术语** 各有 行业标准化组织: Web 是 **OWASP** (Open Worldwide Application Security Project, 非营利, 维护 WSTG 4.2 Web Security Testing Guide + Top 10 2021 + API Security Top 10 2023 + Cheat Sheet Series + ASVS Application Security Verification Standard); Mobile 是 **OWASP MASTG / MASVS** (Mobile App Security Testing Guide + Mobile Application Security Verification Standard L1/L2/R 三档); Cloud 在 IAM enumeration / privilege escalation / service account abuse / metadata service SSRF (IMDSv1 → IMDSv2 演化) / container escape / K8s RBAC abuse 是 行业共识 但 没有 单一 SOT 文档 — 主要 一手 在 SpecterOps / Rhino Security Labs (Pacu) / NCC Group / Christophe Tafani-Dereeper / Scott Piper (flaws.cloud / fwd:cloudsec 会议) 博客 + AWS / Azure / GCP 官方 security advisories. **物理 + 社工 + RF** 术语 (Tailgating / Piggyback / Badge cloning Proxmark3 / Flipper Zero / ESPKey / Bash Bunny / Rubber Ducky / TOOOL lockpicking) 几乎完全 vendor + community 维护, 没有 ISO/NIST 类标准化文档 — 一手 在 Hak5 厂商文档 + DEF CON Physical Security Village + TOOOL (The Open Organisation Of Lockpickers) 协会.

**反例 + 历史案例** 在 红队 教学中 严区分 法律事实 / 学术批评 / 业内 lessons 三重边界 不入人身攻击: weev / Andrew Auernheimer AT&T iPad 2010 案 (公开 API endpoint 暴力枚举 ICC-ID, CFAA 起诉 联邦 41 个月监禁, 第三巡回 2014 因 venue 推翻, 学术余波至今 — 教训 = 公开 endpoint + brute-force 仍触 CFAA), Aaron Swartz / JSTOR 2011 (MIT 校园网 批量下载 JSTOR 论文, 联邦检察官 13 项 CFAA + Wire Fraud 起诉 最高 35 年, 2013-01 自杀, 触发 Aaron's Law CFAA 改革立法讨论), Marcus Hutchins / MalwareTech 2017 (WannaCry kill switch 触发英雄, FBI 同年 8 月 因 Kronos malware 历史 plea bargain 拘留, 业内重新接纳, 灰色历史 vs 当前贡献 严区分), NSO Group Pegasus (商业 spyware 卖给 政府 监控 记者 + 异见者 + 律师, 学术 + Amnesty + Citizen Lab 严批评 + 2021 US 商务部 实体清单), Cellebrite UFED (iPhone 解锁工具 卖给 威权政府 + 美国警方, 同 NSO 类灰色), Stuxnet 2010 (Symantec + Kaspersky disclosure, 国家级 cyber-physical 攻击 PLC, 行业边界教训), NotPetya 2017 (Mandiant 归因 GRU, 全球 supply-chain wiper, $10B+ 损失), SolarWinds Orion 2020 (FireEye / Mandiant 自身被 APT29 attack 触发披露, supply-chain 边界教训) — 这些标 secondary, 仅用于 反模式 + 边界教学, 不入 effective tradecraft.

## Source Manifest

| source_id | url | bucket | last_checked | author/host | one-line note |
|-----------|-----|--------|--------------|-------------|---------------|
| T06-S001 | https://attack.mitre.org/ | surrogate_primary | 2026-05-18 | MITRE (attack.mitre.org) | MITRE ATT&CK Enterprise Matrix v15 (2024); 14 Tactics + 200+ Techniques + 600+ Sub-techniques + Mitigations + Groups + Software; 行业 SOT 框架 [declared=surrogate_primary, auto=secondary; reason=vendor docs (协会 + 教材 — MITRE 是非营利联邦研发中心 FFRDC)] |
| T06-S002 | https://d3fend.mitre.org/ | surrogate_primary | 2026-05-18 | MITRE + NSA (d3fend.mitre.org) | MITRE D3FEND v1.0 (2024); ATT&CK 的 defensive 对应, ontology of defensive techniques; detection engineering 反推 [declared=surrogate_primary, auto=secondary; reason=vendor docs (协会)] |
| T06-S003 | https://csrc.nist.gov/pubs/sp/800/115/final | verified_primary | 2026-05-18 | NIST (csrc.nist.gov) | NIST SP 800-115 Technical Guide to Information Security Testing and Assessment (2008); 联邦渗透测试 baseline; 仍是 政府合规 reference |
| T06-S004 | https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final | verified_primary | 2026-05-18 | NIST (csrc.nist.gov) | NIST SP 800-53 r5 (2020 + 2023 update 1); Security and Privacy Controls; 联邦机构强制 + 私营 mapping |
| T06-S005 | https://www.nist.gov/cyberframework | verified_primary | 2026-05-18 | NIST (nist.gov) | NIST CSF 2.0 (2024-02 release); 6 functions Govern + Identify + Protect + Detect + Respond + Recover |
| T06-S006 | https://owasp.org/www-project-web-security-testing-guide/ | surrogate_primary | 2026-05-18 | OWASP (owasp.org) | OWASP WSTG 4.2 Web Security Testing Guide; 12 章 覆盖 Information Gathering / Auth / AuthZ / Session / Input / Crypto / Error / Business Logic / Client-side [declared=surrogate_primary, auto=secondary; reason=vendor docs (协会 教材 — OWASP 非营利标准化)] |
| T06-S007 | https://mas.owasp.org/MASTG/ | surrogate_primary | 2026-05-18 | OWASP (mas.owasp.org) | OWASP MASTG Mobile App Security Testing Guide + MASVS 2.0 verification standard L1/L2/R [declared=surrogate_primary, auto=secondary; reason=vendor docs (协会 教材)] |
| T06-S008 | https://owasp.org/Top10/ | surrogate_primary | 2026-05-18 | OWASP (owasp.org) | OWASP Top 10 2021 (Web) + OWASP API Security Top 10 2023 [declared=surrogate_primary, auto=secondary; reason=vendor docs (协会)] |
| T06-S009 | http://www.pentest-standard.org/index.php/Main_Page | surrogate_primary | 2026-05-18 | PTES (pentest-standard.org) | PTES Penetration Testing Execution Standard (2014 final); 7 phases Pre-engagement → Intel Gathering → Threat Modeling → Vuln Analysis → Exploitation → Post-Ex → Reporting [declared=surrogate_primary, auto=secondary; reason=vendor docs (协会)] |
| T06-S010 | https://www.isecom.org/OSSTMM.3.pdf | surrogate_primary | 2026-05-18 | ISECOM (isecom.org) | OSSTMM 3 Open Source Security Testing Methodology Manual (2010); ISECOM 维护; rav 评分 + 10 security operations [declared=surrogate_primary, auto=secondary; reason=vendor docs (协会)] |
| T06-S011 | https://www.lockheedmartin.com/en-us/capabilities/cyber/cyber-kill-chain.html | surrogate_primary | 2026-05-18 | Lockheed Martin (lockheedmartin.com) | Cyber Kill Chain (Hutchins/Cloppert/Amin 2011 white paper); 7 阶段 Recon → Weaponization → Delivery → Exploitation → Installation → C2 → Actions [declared=surrogate_primary, auto=secondary; reason=vendor docs (vendor 教材)] |
| T06-S012 | https://www.unifiedkillchain.com/ | surrogate_primary | 2026-05-18 | Paul Pols (unifiedkillchain.com) | Unified Kill Chain (Paul Pols 2017 thesis + 2022 update); 18 phases 含 Initial Foothold + Network Propagation + Action on Objectives 三 macro-phases [declared=surrogate_primary, auto=secondary; reason=vendor docs (作者一手 教材)] |
| T06-S013 | https://apps.dtic.mil/sti/pdfs/ADA586960.pdf | verified_primary | 2026-05-18 | DTIC (apps.dtic.mil) | Diamond Model of Intrusion Analysis (Caltagirone/Pendergast/Betz 2013); 4 顶点 Adversary + Capability + Infrastructure + Victim |
| T06-S014 | https://www.first.org/cvss/v4.0/specification-document | surrogate_primary | 2026-05-18 | FIRST (first.org) | FIRST CVSS v4.0 specification (2023-11 release); 替代 v3.1 (2019); Base + Threat + Environmental + Supplemental [declared=surrogate_primary, auto=secondary; reason=vendor docs (协会 standards)] |
| T06-S015 | https://www.cisa.gov/known-exploited-vulnerabilities-catalog | verified_primary | 2026-05-18 | CISA (cisa.gov) | CISA KEV Known Exploited Vulnerabilities Catalog; 联邦机构 BOD 22-01 强制 patch deadline |
| T06-S016 | https://www.first.org/epss/ | surrogate_primary | 2026-05-18 | FIRST (first.org) | EPSS Exploit Prediction Scoring System v3 (2023); 概率模型 0-1 预测 30 天内 exploitation 概率 [declared=surrogate_primary, auto=secondary; reason=vendor docs (协会)] |
| T06-S017 | https://www.congress.gov/bill/99th-congress/house-bill/4718 | verified_primary | 2026-05-18 | US Congress (congress.gov) | CFAA 18 USC 1030 Computer Fraud and Abuse Act (1986 enacted + 1994 + 1996 + 2001 PATRIOT + 2008 amendments); 未授权访问 5 年 / 加重 10 年 |
| T06-S018 | https://www.legislation.gov.uk/ukpga/1990/18 | verified_primary | 2026-05-18 | UK Legislation (legislation.gov.uk) | UK Computer Misuse Act 1990; Sections 1-3A + Police and Justice Act 2006 amendments + Serious Crime Act 2015 |
| T06-S019 | http://www.npc.gov.cn/npc/c30834/202012/0fa377383d8e4356955d6dbdf81de7e7.shtml | verified_primary | 2026-05-18 | 全国人大 (npc.gov.cn) | 中华人民共和国刑法 285 (非法侵入计算机信息系统罪 3 年; 286 破坏 5/10 年; 287 利用计算机犯罪); 2009 + 2015 修正案 |
| T06-S020 | http://www.npc.gov.cn/npc/c30834/201611/270b43e8b35e4f7ea98502b6f0e26f8a.shtml | verified_primary | 2026-05-18 | 全国人大 (npc.gov.cn) | 中华人民共和国网络安全法 (Cybersecurity Law) 2017-06 施行; 第 27 条 禁止 未经授权 渗透 |
| T06-S021 | http://www.npc.gov.cn/npc/c30834/202106/7c9af12f51334a73b56d7938f99a788a.shtml | verified_primary | 2026-05-18 | 全国人大 (npc.gov.cn) | 中华人民共和国数据安全法 (Data Security Law) 2021-09 施行; 第 21 条 数据分类分级 + 重要数据 + 核心数据 |
| T06-S022 | http://www.npc.gov.cn/npc/c30834/202108/a8c4e3672c74491a80b53a172bb753fe.shtml | verified_primary | 2026-05-18 | 全国人大 (npc.gov.cn) | 中华人民共和国个人信息保护法 PIPL 2021-11 施行; 中国版 GDPR; 第 55 条 PIA + 第 28 条 敏感个人信息 |
| T06-S023 | https://eur-lex.europa.eu/eli/reg/2016/679/oj | surrogate_primary | 2026-05-18 | EU (eur-lex.europa.eu) | GDPR EU 2016/679 General Data Protection Regulation; Article 32 technical and organizational measures; Article 33 breach notification 72h [declared=surrogate_primary, auto=secondary; reason=vendor docs (立法 + 监管 — EUR-Lex 欧盟立法门户, .europa.eu 不在 auto-verify 后缀)] |
| T06-S024 | https://posts.specterops.io/ | surrogate_primary | 2026-05-18 | SpecterOps (specterops.io) | SpecterOps research blog; Will Schroeder + Andy Robbins + Lee Christensen + Matt Graeber 等一手 AD attack 论文 + BloodHound + Certify + Rubeus 作者团队 [declared=surrogate_primary, auto=secondary; reason=vendor docs (作者一手)] |
| T06-S025 | https://www.adsecurity.org/ | surrogate_primary | 2026-05-18 | Sean Metcalf (adsecurity.org) | ADSecurity.org Sean Metcalf (Trimarc CEO); AD 安全权威博客 (DCSync / Golden Ticket / Kerberos abuse 系列) [declared=surrogate_primary, auto=secondary; reason=vendor docs (作者一手)] |
| T06-S026 | https://www.offsec.com/courses/pen-200/ | surrogate_primary | 2026-05-18 | OffSec (offsec.com) | OffSec OSCP PEN-200 + OSEP PEN-300 + OSED EXP-301 + OSEE EXP-401 + OSWA WEB-200 + OSWE WEB-300; 合称 OSCE3 [declared=surrogate_primary, auto=secondary; reason=vendor docs (cert org syllabus 教材)] |
| T06-S027 | https://www.sans.org/cyber-security-courses/network-penetration-testing-ethical-hacking/ | surrogate_primary | 2026-05-18 | SANS (sans.org) | SANS GPEN SEC560 + GXPN SEC660 + GMOB SEC575 + GAWN SEC617 + GCIH SEC504 + GREM FOR610 GIAC syllabus [declared=surrogate_primary, auto=secondary; reason=vendor docs (cert org syllabus 教材)] |
| T06-S028 | https://training.zeropointsecurity.co.uk/courses/red-team-ops | surrogate_primary | 2026-05-18 | Zero-Point Security (zeropointsecurity.co.uk) | Zero-Point Security CRTO Certified Red Team Operator + CRTL Lead syllabus (Daniel Duggan / @_RastaMouse); Cobalt Strike + Brute Ratel 教学 [declared=surrogate_primary, auto=secondary; reason=vendor docs (cert org syllabus)] |
| T06-S029 | https://www.alteredsecurity.com/adlab | surrogate_primary | 2026-05-18 | Altered Security (alteredsecurity.com) | Altered Security CRTP Certified Red Team Professional + CRTE + CRTM (Nikhil Mittal / @nikhil_mitt); AD attack 全栈 [declared=surrogate_primary, auto=secondary; reason=vendor docs (cert org syllabus)] |
| T06-S030 | https://www.trimarcsecurity.com/blog | surrogate_primary | 2026-05-18 | Trimarc + SpecterOps (trimarcsecurity.com) | Trimarc Sean Metcalf + SpecterOps Certipy / ADCS ESC1-15 (Will Schroeder + Lee Christensen 2021 Whitepaper "Certified Pre-Owned") [declared=surrogate_primary, auto=secondary; reason=vendor docs (作者一手)] |
| T06-S031 | https://www.cisa.gov/news-events/cybersecurity-advisories | verified_primary | 2026-05-18 | CISA (cisa.gov) | CISA Cybersecurity Advisories; AA21-xxx + AA22-xxx 系列 APT 通报 + #StopRansomware joint advisories |
| T06-S032 | https://www.pcisecuritystandards.org/document_library/ | surrogate_primary | 2026-05-18 | PCI SSC (pcisecuritystandards.org) | PCI DSS v4.0 (2022 + 2025-03 mandatory); 支付卡数据安全标准; Requirement 11.4 渗透测试强制 [declared=surrogate_primary, auto=secondary; reason=vendor docs (协会 standards)] |
| T06-S033 | https://www.iso.org/standard/27001 | surrogate_primary | 2026-05-18 | ISO (iso.org) | ISO/IEC 27001:2022 + 27002:2022 ISMS Information Security Management System; Annex A 93 controls [declared=surrogate_primary, auto=secondary; reason=vendor docs (协会 standards)] |
| T06-S034 | https://nvd.nist.gov/ | verified_primary | 2026-05-18 | NIST (nvd.nist.gov) | NVD National Vulnerability Database; CVE + CPE + CVSS scoring 美国权威 |
| T06-S035 | https://cwe.mitre.org/ | surrogate_primary | 2026-05-18 | MITRE (cwe.mitre.org) | CWE Common Weakness Enumeration; 软件 + 硬件 weakness 分类; CWE Top 25 2023 [declared=surrogate_primary, auto=secondary; reason=vendor docs (协会 standards)] |
| T06-S036 | https://capec.mitre.org/ | surrogate_primary | 2026-05-18 | MITRE (capec.mitre.org) | CAPEC Common Attack Pattern Enumeration and Classification; 500+ attack patterns; ATT&CK 抽象 + WSTG 具体 之间桥梁 [declared=surrogate_primary, auto=secondary; reason=vendor docs (协会 standards)] |
| T06-S037 | https://www.cve.org/ | surrogate_primary | 2026-05-18 | MITRE (cve.org) | CVE Common Vulnerabilities and Exposures program; CNA Numbering Authority 体系 [declared=surrogate_primary, auto=secondary; reason=vendor docs (协会 监管)] |
| T06-S038 | https://atlas.mitre.org/ | surrogate_primary | 2026-05-18 | MITRE (atlas.mitre.org) | MITRE ATLAS Adversarial Threat Landscape for AI Systems (2021+); ML / AI 系统 攻防矩阵 [declared=surrogate_primary, auto=secondary; reason=vendor docs (协会)] |
| T06-S039 | https://www.harmj0y.net/ | surrogate_primary | 2026-05-18 | Will Schroeder (harmj0y.net) | Will Schroeder 个人 + SpecterOps 联创; Kerberoasting (2014) + Empire + Rubeus + PowerView 原创 [declared=surrogate_primary, auto=secondary; reason=vendor docs (作者一手)] |
| T06-S040 | https://www.cobaltstrike.com/blog | surrogate_primary | 2026-05-18 | Fortra (cobaltstrike.com) | Cobalt Strike 官方博客 + Raphael Mudge 历史 archive; Malleable C2 + BOF + Aggressor Script 工具厂商一手 [declared=surrogate_primary, auto=secondary; reason=vendor docs (工具厂商 一手)] |
| T06-S041 | https://www.ic3.gov/ | verified_primary | 2026-05-18 | FBI IC3 (ic3.gov) | FBI Internet Crime Complaint Center; Marcus Hutchins / WannaCry 公开 案件来源 |
| T06-S042 | https://www.ncsc.gov.uk/section/about-this-website/cbest-framework | verified_primary | 2026-05-18 | UK NCSC (ncsc.gov.uk) | CBEST UK financial sector intelligence-led red team framework; Bank of England + NCSC 联合 |
| T06-S043 | https://www.ecb.europa.eu/paym/cyber-resilience/tiber-eu/html/index.en.html | surrogate_primary | 2026-05-18 | ECB (europa.eu) | TIBER-EU Threat Intelligence-Based Ethical Red Teaming framework; ECB 2018; EU 金融基础设施红队标准 [declared=surrogate_primary, auto=secondary; reason=vendor docs (监管 + 协会 — ECB europa.eu 公共监管文件, .europa.eu 不在 auto-verify 后缀)] |
| T06-S044 | https://congress.gov/bill/113th-congress/house-bill/2454 | verified_primary | 2026-05-18 | US Congress (congress.gov) | Aaron's Law Act of 2013 (HR 2454, 未通过 但 重要立法讨论); CFAA 改革提案 Zoe Lofgren + Ron Wyden |
| T06-S045 | https://hackerone.com/disclosure-guidelines | surrogate_primary | 2026-05-18 | HackerOne (hackerone.com) | HackerOne Disclosure Guidelines + Safe Harbor; bug bounty 行业标准 [declared=surrogate_primary, auto=secondary; reason=vendor docs (协会)] |
| T06-S046 | https://capec.mitre.org/data/definitions/1000.html | surrogate_primary | 2026-05-18 | MITRE (capec.mitre.org) | CAPEC Domains of Attack View; physical + supply chain + social engineering 等抽象 [declared=surrogate_primary, auto=secondary; reason=vendor docs (协会 standards)] |
| T06-S047 | https://www.djbh.net/ | surrogate_primary | 2026-05-18 | 公安部 (djbh.net) | 中国 网络安全等级保护网 (等保 2.0 GB/T 22239-2019); 公安部 直管 五级分级 [declared=surrogate_primary, auto=secondary; reason=vendor docs (监管 — 公安部 等保 standards — .net 不在 primary suffix)] |
| T06-S048 | https://www.cncert.org.cn/ | surrogate_primary | 2026-05-18 | CNCERT (cncert.org.cn) | CNCERT/CC 国家计算机网络应急技术处理协调中心; 网信办下属; 漏洞应急 + 通报 [declared=surrogate_primary, auto=secondary; reason=vendor docs (监管 — 网信办下属)] |
| T06-S049 | https://www.enginepedia.org/index.html | surrogate_primary | 2026-05-18 | David Bianco (enginepedia.org) | David Bianco Pyramid of Pain (2013 SANS blog); IoC 难度阶梯 hash → IP → domain → tools → TTPs [declared=surrogate_primary, auto=secondary; reason=vendor docs (作者一手)] |
| T06-S050 | https://github.com/redcanaryco/atomic-red-team | surrogate_primary | 2026-05-18 | Red Canary (github.com) | Atomic Red Team; ATT&CK technique 测试库 [declared=surrogate_primary, auto=secondary; reason=vendor docs (开源工具 一手)] |

## Glossary Table

| term | category | definition_brief | reference_source_id |
|---|---|---|---|
| MITRE ATT&CK | framework | Adversarial Tactics, Techniques, and Common Knowledge; 14 Tactics / 200+ Techniques / 600+ Sub-techniques 矩阵 (Enterprise + Mobile + ICS + Cloud + Containers); v15 (2024); 行业 SOT, 任何严肃红队报告必须 map ATT&CK ID. | T06-S001 |
| MITRE D3FEND | framework | Defensive counterpart to ATT&CK; ontology of defensive techniques; NSA + MITRE 2021; detection engineering 反推. | T06-S002 |
| CWE | framework | Common Weakness Enumeration; 软件/硬件 weakness 分类; CWE Top 25 2023 (CWE-787 OOB Write 居首). | T06-S035 |
| CVE | framework | Common Vulnerabilities and Exposures; MITRE 运营 CNA Numbering Authorities 体系; CVE-YYYY-NNNNN 标识. | T06-S037 |
| CAPEC | framework | Common Attack Pattern Enumeration and Classification; 500+ attack patterns; ATT&CK 抽象 与 WSTG 具体之间桥梁. | T06-S036 |
| PTES | framework | Penetration Testing Execution Standard; 7 phases (Pre-engagement / Intel Gathering / Threat Modeling / Vuln Analysis / Exploitation / Post-Ex / Reporting); 2014 final; 仍是常用 pentest 方法论 SOT. | T06-S009 |
| OSSTMM 3 | framework | Open Source Security Testing Methodology Manual; ISECOM 2010; rav 评分 + 10 security operations; 重 metric 体系. | T06-S010 |
| NIST SP 800-115 | framework | Technical Guide to Information Security Testing and Assessment (2008); 联邦渗透 baseline; 仍是政府合规 reference. | T06-S003 |
| NIST SP 800-53 r5 | framework | Security and Privacy Controls for Information Systems; 2020 + 2023 update; 联邦机构强制 + 私营 mapping 基线. | T06-S004 |
| NIST CSF 2.0 | framework | Cybersecurity Framework 2.0 (2024-02); 6 functions Govern + Identify + Protect + Detect + Respond + Recover. | T06-S005 |
| Cyber Kill Chain | framework | Lockheed Martin (Hutchins/Cloppert/Amin 2011); 7 阶段线性 Recon → Weaponization → Delivery → Exploitation → Installation → C2 → Actions on Objectives. | T06-S011 |
| Unified Kill Chain | framework | Paul Pols 2017 thesis + 2022 update; 18 phases cyclical; 含 Initial Foothold + Network Propagation + Action on Objectives 三 macro-phases; 补 Lockheed 缺 internal movement. | T06-S012 |
| Diamond Model | framework | Caltagirone/Pendergast/Betz 2013 DTIC; 4 顶点 Adversary + Capability + Infrastructure + Victim; threat intel 归因 SOT. | T06-S013 |
| Pyramid of Pain | framework | David Bianco 2013 SANS blog; IoC 难度阶梯 hash (trivial) → IP → domain → network/host artifact → tools → TTPs (tough); detection ROI 分析. | T06-S049 |
| MITRE ATLAS | framework | Adversarial Threat Landscape for AI Systems (2021+); ML/AI 系统 攻防矩阵; ATT&CK 类比. | T06-S038 |
| TA0043 Reconnaissance | tactic | ATT&CK Tactic; 收集可用于规划未来 operations 的信息; passive + active OSINT, asset discovery. | T06-S001 |
| TA0042 Resource Development | tactic | ATT&CK Tactic; 建立 资源 (infrastructure / accounts / capabilities) 用于支持 operations. | T06-S001 |
| TA0001 Initial Access | tactic | ATT&CK Tactic; 进入网络的入口 vectors (phishing / exploit-facing app / valid accounts / supply chain). | T06-S001 |
| TA0002 Execution | tactic | ATT&CK Tactic; 在 local / remote 系统运行 adversary-controlled code. | T06-S001 |
| TA0003 Persistence | tactic | ATT&CK Tactic; 重启 / 凭据变更 后仍保持 foothold. | T06-S001 |
| TA0004 Privilege Escalation | tactic | ATT&CK Tactic; 获得更高 permissions on system or network (UAC bypass / token theft / kernel exploit). | T06-S001 |
| TA0005 Defense Evasion | tactic | ATT&CK Tactic; 规避 detection (obfuscation / signed binary proxy / disable security tools / DLL sideloading). | T06-S001 |
| TA0006 Credential Access | tactic | ATT&CK Tactic; 偷取 凭据 (account name + password / hash / ticket / token / certificate). | T06-S001 |
| TA0007 Discovery | tactic | ATT&CK Tactic; 摸清 环境 (account / process / system / network / domain enumeration). | T06-S001 |
| TA0008 Lateral Movement | tactic | ATT&CK Tactic; 在环境中 横向 (PsExec / WMI / RDP / SMB / WinRM / DCOM). | T06-S001 |
| TA0009 Collection | tactic | ATT&CK Tactic; 收集 数据 (screen capture / keylog / clipboard / email / file). | T06-S001 |
| TA0011 Command and Control | tactic | ATT&CK Tactic; C2 channel (Application Layer Protocol / Web Protocols / DNS / proxy). | T06-S001 |
| TA0010 Exfiltration | tactic | ATT&CK Tactic; 数据带走 (alternative protocol / over web / over C2 / staged). | T06-S001 |
| TA0040 Impact | tactic | ATT&CK Tactic; 破坏 availability / integrity (encryption for impact / wiper / DoS / defacement). | T06-S001 |
| T1059.001 PowerShell | technique | ATT&CK; Execution via PowerShell; encoded command / IEX / AMSI bypass 常配套; ScriptBlock logging 是核心 detection. | T06-S001 |
| T1078 Valid Accounts | technique | ATT&CK; 用 已有的合法账号 (local / domain / cloud / default) 实现 access + persistence + privesc + evasion 四合一. | T06-S001 |
| T1003 OS Credential Dumping | technique | ATT&CK; LSASS memory / SAM / NTDS.dit / DCSync / DCSync / Cached / LSA secrets; Mimikatz / pypykatz / nanodump 是主工具. | T06-S001 |
| T1003.006 DCSync | technique | ATT&CK; abuse MS-DRSR Directory Replication Service Remote Protocol; 拿 KRBTGT / 任意账户 hash; 需 Replicating Directory Changes 权限. | T06-S001 |
| T1218 System Binary Proxy Execution | technique | ATT&CK; LOLBins (rundll32 / regsvr32 / mshta / msbuild / installutil / odbcconf); signed binary 跑 unsigned payload. | T06-S001 |
| T1566 Phishing | technique | ATT&CK; Spearphishing Attachment / Link / Service / Voice; 仍然 Initial Access #1 vector. | T06-S001 |
| T1190 Exploit Public-Facing Application | technique | ATT&CK; n-day / 0-day exploit 对外暴露应用; ProxyLogon / Log4Shell / MOVEit 类. | T06-S001 |
| T1558.003 Kerberoasting | technique | ATT&CK; Request TGS for SPN-enabled accounts; offline crack 弱密码; Will Schroeder 2014 SpecterOps 原创. | T06-S039 |
| T1558.004 AS-REP Roasting | technique | ATT&CK; Request AS-REP for accounts with DONT_REQ_PREAUTH; offline crack; 比 Kerberoasting 不需任何 valid credential. | T06-S001 |
| T1550.002 Pass-the-Hash | technique | ATT&CK; NTLM hash 直接用作 authentication; Mimikatz sekurlsa::pth / Impacket; NTLMv2 不影响 hash 复用. | T06-S001 |
| T1550.003 Pass-the-Ticket | technique | ATT&CK; Kerberos TGT/TGS ticket 注入 当前 session; Rubeus ptt / Mimikatz kerberos::ptt. | T06-S001 |
| T1207 Rogue Domain Controller (DCShadow) | technique | ATT&CK; 注册 fake DC 通过 replication 写任意 AD object; Mimikatz lsadump::dcshadow; Vincent Le Toux + Benjamin Delpy 2018. | T06-S001 |
| T1484.001 GPO Modification | technique | ATT&CK; abuse Group Policy Object 写权限 push 恶意配置 / scheduled task / startup script. | T06-S001 |
| T1611 Escape to Host | technique | ATT&CK; 容器逃逸 to underlying host; privileged container / hostPath / Docker socket mount. | T06-S001 |
| T1098 Account Manipulation | technique | ATT&CK; 修改 account properties / add credentials / register additional device for MFA. | T06-S001 |
| T1071.001 Application Layer Protocol Web | technique | ATT&CK; HTTP/S C2 channel; blend in legit traffic; Malleable C2 profile 核心场景. | T06-S001 |
| T1572 Protocol Tunneling | technique | ATT&CK; tunnel traffic 在其他 protocol 内 (DNS / ICMP / HTTPS); chisel / dnscat2 / iodine 常用. | T06-S001 |
| T1486 Data Encrypted for Impact | technique | ATT&CK; 勒索软件 加密 受害者数据; NOT 红队 default scope, 必须 单独显式授权 + 客户 接受业务中断. | T06-S001 |
| T1027 Obfuscated Files or Information | technique | ATT&CK; payload 编码 / 加密 / packed; Invoke-Obfuscation / ConfuserEx / donut. | T06-S001 |
| T1140 Deobfuscate/Decode Files | technique | ATT&CK; runtime 解密 / decode payload; XOR / RC4 / AES; certutil -decode 历史. | T06-S001 |
| T1620 Reflective Code Loading | technique | ATT&CK; in-memory 加载 PE / .NET assembly without writing disk; Reflective DLL Injection (Stephen Fewer); Donut. | T06-S001 |
| Kerberoasting | AD attack | T1558.003; Request TGS for SPN-enabled service account; ticket RC4/AES 加密 用 service account NT hash; offline crack via Hashcat -m 13100/19700; Will Schroeder 2014 BSidesDFW + Tim Medin 2014 SANS Hackfest. | T06-S039 |
| AS-REP Roasting | AD attack | T1558.004; account with UF_DONT_REQUIRE_PREAUTH set; request AS-REP 无需 preauth; offline crack via Hashcat -m 18200; Rubeus asreproast / Impacket GetNPUsers. | T06-S024 |
| Unconstrained Delegation | AD attack | TrustedForDelegation flag; 凡是 access 该 host 的 user 的 TGT 都被缓存; 拿下后 TGT 拿任意 user 身份; Coercer + Petitpotam + Printerbug 强制 DC 认证. | T06-S025 |
| Constrained Delegation | AD attack | msDS-AllowedToDelegateTo; account 只能 to specific service; S4U2self + S4U2proxy 双调用; Kekeo + Rubeus s4u 利用. | T06-S025 |
| Resource-Based Constrained Delegation (RBCD) | AD attack | msDS-AllowedToActOnBehalfOfOtherIdentity; resource 反向指定 谁可以 delegate to it; Elad Shamir 2019; Rubeus + Impacket; Computer object GenericWrite 即可触发. | T06-S024 |
| S4U2self | AD attack | Service-for-User-to-self; Kerberos extension; service 为任意 user 申请 ticket to itself; PAC contains forwardable ticket for next stage. | T06-S025 |
| S4U2proxy | AD attack | Service-for-User-to-proxy; service 用 forwardable ticket 申请 任意 target service 的 ticket; constrained / RBCD 利用核心. | T06-S025 |
| Golden Ticket | AD attack | Forge TGT using KRBTGT NT hash; 任意 user / 任意 group / 任意 lifetime; Benjamin Delpy 2014 Mimikatz; KRBTGT 必须 double-reset 才能 invalidate. | T06-S025 |
| Silver Ticket | AD attack | Forge TGS using target service account NT hash; 限定 single service; 比 Golden 更隐蔽 (不经 DC). | T06-S025 |
| Diamond Ticket | AD attack | Forge TGT by 修改 legitimate AS-REP PAC; 避免 Golden Ticket 的 anomalous lifetime 特征; Charlie Clark 2022. | T06-S024 |
| Sapphire Ticket | AD attack | Forge TGT 利用 S4U2self + Diamond 组合; 更进一步的 stealthy alternative to Golden; 2022 research. | T06-S024 |
| Pass-the-Hash (PtH) | AD attack | T1550.002; NTLM hash 复用作 authentication; Mimikatz sekurlsa::pth; Impacket psexec.py / wmiexec.py -hashes; 不需 plaintext password. | T06-S025 |
| Pass-the-Ticket (PtT) | AD attack | T1550.003; Kerberos TGT/TGS 注入 sesssion; Rubeus ptt / Mimikatz kerberos::ptt. | T06-S025 |
| Overpass-the-Hash | AD attack | NTLM hash → Kerberos TGT; Rubeus asktgt /user /rc4; 配合 ptt 实现 nthash → Kerberos auth. | T06-S025 |
| Pass-the-Certificate | AD attack | Certificate-based Kerberos PKINIT; 拿到 user 证书 → 申请 TGT; Certipy auth / Rubeus asktgt /certificate. | T06-S030 |
| Shadow Credentials | AD attack | msDS-KeyCredentialLink attribute (Windows Hello for Business); 加 alternate key credential → request TGT via PKINIT; Whisker / Certipy shadow; Elad Shamir 2021. | T06-S024 |
| NTLM Relay | AD attack | 截获 NTLM authentication 转发至 third service; SMB / HTTP / LDAP / LDAPS; ntlmrelayx.py; SMB signing / EPA / Channel Binding 是 mitigation. | T06-S024 |
| SMB Relay | AD attack | NTLM Relay 的 SMB protocol 子类; Responder + ntlmrelayx; SMB signing OFF 是必要条件. | T06-S024 |
| KRBTGT Account | AD attack | Domain controller 上的 Kerberos service account; 其 NT hash 是 Golden Ticket 唯一来源; double-reset (两次连续重置) 才能 invalidate 所有 Golden. | T06-S025 |
| DCSync | AD attack | T1003.006; abuse MS-DRSR Replicating Directory Changes 权限 拿 KRBTGT / 任意 user hash; Mimikatz lsadump::dcsync; Impacket secretsdump. | T06-S025 |
| DCShadow | AD attack | T1207; 注册 rogue DC 通过 replication 写任意 AD attribute (SID History / sidHistory); Mimikatz lsadump::dcshadow; 极隐蔽. | T06-S025 |
| SID History | AD attack | sidHistory attribute (originally for AD migration); 注入 Domain Admins SID 实现 cross-domain privesc; Mimikatz / DCShadow 写入. | T06-S025 |
| ACL Abuse | AD attack | AD object ACE (GenericAll / WriteDACL / WriteOwner / GenericWrite) misconfig 实现 takeover; BloodHound 是 ACL 路径发现 SOT. | T06-S024 |
| ADCS ESC1-15 | AD attack | Active Directory Certificate Services 模板配置错误 15 类 (ESC1 SAN abuse / ESC2 Any Purpose / ESC4 vulnerable template ACL / ESC8 NTLM relay to HTTP / ESC9 / ESC10 / ESC11 / ESC13 / ESC14 / ESC15); SpecterOps "Certified Pre-Owned" Whitepaper 2021. | T06-S030 |
| Petitpotam | AD attack | MS-EFSRPC EfsRpcOpenFileRaw 强制 任意 host 认证至 attacker; Topotam 2021; 常配 ADCS ESC8 NTLM relay to HTTP cert request. | T06-S024 |
| PrintSpoofer | AD attack | SeImpersonatePrivilege abuse 通过 named pipe coercion; Local SYSTEM privesc; Itm4n 2020; JuicyPotato 后继. | T06-S024 |
| SeImpersonatePrivilege | AD attack | Windows privilege 允许 impersonate token; service account (IIS / MSSQL) 常有; "Potato" 系列 (Juicy / Rotten / Print / God) 利用此. | T06-S024 |
| Inveigh | AD attack | LLMNR / NBT-NS / mDNS poisoning + SMB / HTTP relay; PowerShell + .NET 实现; Responder Windows 版. | T06-S024 |
| Responder | AD attack | LLMNR / NBT-NS / mDNS poisoning; SpiderLabs (Laurent Gaffié) 维护; 内网 #1 starting point; 配 ntlmrelayx 是经典组合. | T06-S024 |
| SQLi | Web/API | T1190 子集; OWASP A03:2021 Injection; 用户输入拼接 SQL 致 任意 query 执行; UNION / Boolean / Time-based / Out-of-band 四类; sqlmap 自动化工具. | T06-S006 |
| XSS (Stored/Reflected/DOM) | Web/API | Cross-Site Scripting; OWASP A03 Injection; 浏览器执行注入脚本; CSP / HttpOnly cookie / output encoding 是 mitigation. | T06-S006 |
| SSRF | Web/API | Server-Side Request Forgery; OWASP A10:2021; 服务端按用户输入发起请求; 云环境 IMDS metadata service 是高危目标 (IMDSv1 → IMDSv2 PUT token 演化). | T06-S006 |
| XXE | Web/API | XML External Entity; OWASP A05; XML parser 解析 external entity 致 file read / SSRF; libxml2 / .NET XmlDocument 默认配置历史漏洞. | T06-S006 |
| Deserialization | Web/API | Insecure Deserialization; OWASP A08:2021; Java / .NET / PHP / Python; ysoserial 是 Java payload 生成器; Marshalsec / .NET TypeConfuseDelegate gadget chains. | T06-S006 |
| SSTI | Web/API | Server-Side Template Injection; Jinja2 / Twig / Freemarker / Velocity / Handlebars; James Kettle (PortSwigger) 2015 经典研究; ${7*7} fingerprint. | T06-S008 |
| NoSQL Injection | Web/API | MongoDB / CouchDB / Redis 注入; $ne / $gt operator abuse; JSON body 参数化失效. | T06-S006 |
| LDAP Injection | Web/API | LDAP filter 注入; *)(uid=*) 类 wildcard; Active Directory 查询接口常见. | T06-S006 |
| Prototype Pollution | Web/API | JS Object.prototype 污染 (__proto__ / constructor.prototype); 影响整个 application object 行为; Olivier Arteau 2018 NodeJS 研究. | T06-S008 |
| DOM Clobbering | Web/API | HTML element name/id 污染 window / document property; 绕过 CSP + sanitizer; Gareth Heyes (PortSwigger) 研究. | T06-S008 |
| GraphQL Injection | Web/API | GraphQL introspection abuse + 嵌套 query DoS + alias batching; InQL / Clairvoyance 工具; 默认 introspection 开启是常见 misconfig. | T06-S008 |
| JWT Abuse | Web/API | alg:none / key confusion (HS256 ↔ RS256) / weak secret brute / kid path traversal / jwk header injection; jwt_tool 工具. | T06-S008 |
| IDOR | Web/API | Insecure Direct Object Reference; OWASP API1:2023 Broken Object Level Authorization; /api/user/123 直接换 ID 即 越权; #1 API 漏洞类. | T06-S008 |
| Race Condition | Web/API | TOCTOU Time-of-check-time-of-use; 并发请求绕过 once-only check; James Kettle PortSwigger 2023 single-packet attack. | T06-S008 |
| Mass Assignment | Web/API | OWASP API6:2023; ORM 自动 bind 用户输入到 model 字段; isAdmin=true 注入. | T06-S008 |
| OAuth Flow Attacks | Web/API | redirect_uri 验证缺失 / state CSRF / PKCE 缺失 / device code phishing / token theft; OAuth 2.0 RFC 6749 + Security BCP RFC 8252. | T06-S006 |
| SAML Attacks | Web/API | XML Signature Wrapping (XSW) / Comment injection / Signature exclusion; Onelogin SAML 2018 漏洞经典; SAMLRaider / SAML Burp 工具. | T06-S006 |
| WebAuthn Replay | Web/API | challenge reuse / origin binding bypass; 较新攻击面; FIDO2 ceremony abuse. | T06-S006 |
| CSRF | Web/API | Cross-Site Request Forgery; OWASP A01:2021 (并入 Broken Access Control); SameSite cookie + CSRF token 是双重 mitigation. | T06-S006 |
| CORS Misconfig | Web/API | Access-Control-Allow-Origin reflection + Allow-Credentials: true 致 cross-origin read; James Kettle 研究. | T06-S006 |
| Open Redirect | Web/API | unsanitized redirect parameter; phishing chain + OAuth flow attack 跳板. | T06-S006 |
| Clickjacking | Web/API | UI redress; iframe 覆盖 + X-Frame-Options / frame-ancestors CSP mitigation. | T06-S006 |
| HTTP Request Smuggling | Web/API | CL.TE / TE.CL / TE.TE 前后端 header 解析差异; James Kettle 2019 BlackHat; queue poisoning. | T06-S008 |
| HTTP/2 Desync | Web/API | HTTP/2 → HTTP/1.1 downgrade smuggling; James Kettle 2021 BlackHat; 多 CDN 受影响. | T06-S008 |
| SSL Pinning | Mobile | client 验证 server 证书 public key / hash; bypass via Frida + Objection + universal pinning bypass script; iOS + Android. | T06-S007 |
| Frida | Mobile | Dynamic instrumentation toolkit; JavaScript hooks into native function; Ole André V. Ravnås; iOS / Android / desktop. | T06-S007 |
| Objection | Mobile | Frida-based mobile runtime exploration; SSL pinning bypass + root/jailbreak detection bypass; SensePost. | T06-S007 |
| Drozer | Mobile | Android security assessment framework; IPC + content provider + intent attack surface; WithSecure (F-Secure) 维护. | T06-S007 |
| APK / IPA | Mobile | Android Application Package / iOS App Store Package; reverse via apktool + jadx (APK) / class-dump + Hopper (IPA). | T06-S007 |
| Magisk Hide | Mobile | Android root + module hiding; bypass SafetyNet / Play Integrity API; Zygisk 是新机制. | T06-S007 |
| OWASP MASVS | Mobile | Mobile Application Security Verification Standard 2.0; L1 (basic) + L2 (defense-in-depth) + R (resilience against reverse engineering). | T06-S007 |
| IMDSv1/v2 | Cloud | AWS EC2 Instance Metadata Service; v1 plain HTTP 169.254.169.254 (SSRF 即拿 role credentials); v2 PUT token required; Capital One 2019 100M record breach 由 v1 SSRF 触发. | T06-S001 |
| IAM Enumeration | Cloud | AWS / Azure / GCP IAM policy + role + group 枚举; AWS Pacu + iam_enum + ScoutSuite; AzureHound + ROADtools; G-Scout. | T06-S024 |
| AssumeRole / STS Chain | Cloud | AWS STS sts:AssumeRole 跨账号 / 跨服务 role 链路; cross-account trust policy misconfig; Rhino Security pacu_assume_role 利用. | T06-S001 |
| Lambda Backdoor | Cloud | Lambda function modify 加 reverse shell / cron persistence; serverless persistence 模式; ATT&CK T1525 Implant Internal Image. | T06-S001 |
| S3 Bucket Misconfig | Cloud | Public READ/WRITE + ACL 错配 + bucket policy * principal; S3Scanner + s3-account-search 枚举. | T06-S001 |
| Azure AD Enumeration | Cloud | AAD user / group / role / app / service principal 枚举; AzureHound (BloodHound Edge) + ROADtools (Dirk-jan Mollema). | T06-S024 |
| AzureHound | Cloud | BloodHound Enterprise + Community for Azure / Entra ID; SpecterOps 维护; collect AAD graph 数据. | T06-S024 |
| ROADtools | Cloud | Azure AD enumeration framework; Dirk-jan Mollema; roadrecon + roadlib; Azure Graph API 抓取. | T06-S024 |
| GCP Service Account Abuse | Cloud | actAs / impersonate / generateAccessToken chain; Christophe Tafani-Dereeper 系列研究; gcloud iam service-accounts. | T06-S001 |
| kube-hunter | Cloud | Aqua Security 维护 K8s 集群安全扫描; pod-level + remote (master IP 暴露) 双模; CVE 检测. | T06-S001 |
| kubectl who-can | Cloud | RBAC 反查 谁可以做什么; Aqua Security; permission audit 必备. | T06-S001 |
| Docker Escape | Cloud | T1611; privileged container / Docker socket mount / cap_sys_admin / hostPath / cgroup release_agent (CVE-2022-0492). | T06-S001 |
| Privileged Container | Cloud | --privileged flag disables most isolation; 直接 host 设备访问; container escape 默认入场券. | T06-S001 |
| hostPath Mount | Cloud | K8s Pod 挂 host 文件系统; /var/run/docker.sock 即 Docker socket; /etc/shadow 即 host credentials. | T06-S001 |
| Service Account Token | Cloud | K8s Pod 默认挂载 SA token at /var/run/secrets/kubernetes.io/serviceaccount/token; RBAC 配错即 cluster takeover. | T06-S001 |
| Beacon | C2/OPSEC | Cobalt Strike implant 通用术语; 周期性 callback 至 teamserver; sleep + jitter 控制 OPSEC. | T06-S040 |
| Implant | C2/OPSEC | 通用 后门 程序; Sliver / Mythic / Havoc / Cobalt Strike Beacon 总称. | T06-S040 |
| Stager | C2/OPSEC | 小型 first-stage loader 下载 main payload; HTTP / DNS / Smb staged channel; staged vs stageless 是 OPSEC 取舍. | T06-S040 |
| Sleep Mask | C2/OPSEC | Beacon sleep 期间 加密 / 解密 内存 + heap 隐藏 IoC; Cobalt Strike 4.4+; Ekko / FOLIAGE / DeathSleep 公开技术. | T06-S040 |
| Jitter | C2/OPSEC | Beacon callback interval 随机化 (sleep 60 jitter 30 = 60s ± 30%); 反 beaconing detection 第一步. | T06-S040 |
| Malleable C2 Profile | C2/OPSEC | Cobalt Strike 自定义 C2 traffic + behavioral characteristics; mimic 合法应用 (jQuery / Gmail / Slack); profile 文件 .profile. | T06-S040 |
| Process Injection | C2/OPSEC | T1055; 注入 code 进入 另一 process 内存空间; CreateRemoteThread / QueueUserAPC / Early Bird / NtMapViewOfSection / Process Hollowing / Thread Hijacking 子类. | T06-S001 |
| Process Hollowing | C2/OPSEC | T1055.012; CreateProcess SUSPENDED + ZwUnmapViewOfSection + WriteProcessMemory + SetThreadContext + ResumeThread; svchost.exe mask. | T06-S001 |
| DLL Sideloading | C2/OPSEC | T1574.002; 合法 signed binary 加载 attacker DLL (search order hijack); 大量 vendor binary 受影响. | T06-S001 |
| Direct Syscalls | C2/OPSEC | 直接 invoke ntdll syscall number 避开 userland EDR hook; SysWhispers (Jackson_T) / Hells Gate / Halos Gate 系列. | T06-S001 |
| Indirect Syscalls | C2/OPSEC | call instruction 仍指向 ntdll.dll syscall stub 但 syscall ID 动态解析; 更 stealthy; Tartarus Gate. | T06-S001 |
| Hell's Gate | C2/OPSEC | dynamic syscall ID extraction from ntdll; am0nsec + RtlMourner 2020; bypass EDR userland hook 基础技术. | T06-S001 |
| AMSI Bypass | C2/OPSEC | Anti-Malware Scan Interface (Windows 10+); patch AmsiScanBuffer / hook / unload amsi.dll; Matt Graeber + Cn33liz 系列 patch. | T06-S024 |
| ETW Bypass | C2/OPSEC | Event Tracing for Windows patch / disable; EtwEventWrite null patch; Matt Graeber 研究; 影响 EDR telemetry 大半. | T06-S024 |
| Domain Fronting | C2/OPSEC | TLS SNI ≠ HTTP Host header; 流量 看 CDN 高信誉 domain; AWS CloudFront / Azure 2018 后陆续禁; Fastly 部分仍可. | T06-S001 |
| DNS Tunneling | C2/OPSEC | T1572; DNS query/response 携带 C2 data; iodine / dnscat2 / DNSExfiltrator; TXT record 大 payload. | T06-S001 |
| Token Impersonation | C2/OPSEC | T1134; SeImpersonatePrivilege + DuplicateTokenEx + ImpersonateLoggedOnUser; incognito.exe / Rubeus / Cobalt Strike steal_token. | T06-S001 |
| SeDebugPrivilege | C2/OPSEC | Windows privilege OpenProcess to any process; LSASS read 必要 (除非 PPL); Mimikatz / nanodump dump credentials. | T06-S025 |
| LOLBins / LOLBAS | C2/OPSEC | Living Off The Land Binaries And Scripts; lolbas-project.github.io; signed Microsoft binary 跑 unsigned payload (mshta / installutil / regsvr32 / msbuild / certutil). | T06-S001 |
| BYOVD | C2/OPSEC | Bring Your Own Vulnerable Driver; 加载 已签名 但 有漏洞的 driver (gigabyte / dell / mhyprot2) 实现 kernel-level EDR kill; LazyCat / KDU / EDRSandblast. | T06-S024 |
| CVSS v3.1 | scoring | Common Vulnerability Scoring System 3.1 (2019); Base + Temporal + Environmental; 0.0-10.0; AV/AC/PR/UI + S/C/I/A 八字段. | T06-S014 |
| CVSS v4.0 | scoring | FIRST 2023-11 release; Base + Threat + Environmental + Supplemental; 新增 AT (Attack Requirements) + VC/VI/VA (Vulnerable system) + SC/SI/SA (Subsequent system); 替代 v3.1. | T06-S014 |
| EPSS | scoring | Exploit Prediction Scoring System; FIRST 概率模型; 0-1 30 天内 exploitation 概率; CVSS + EPSS + KEV 三者补充, 不替代. | T06-S016 |
| KEV | scoring | CISA Known Exploited Vulnerabilities Catalog; 联邦机构 BOD 22-01 强制 patch deadline; 不是 评分但 是 binary actionable. | T06-S015 |
| SSVC | scoring | Stakeholder-Specific Vulnerability Categorization; CISA + CMU SEI; decision tree 替代单一 score; act / attend / track / track* 四级. | T06-S015 |
| VPR | scoring | Tenable Vulnerability Priority Rating; vendor 商用替代 CVSS; ML 模型 + threat context; 闭源不开源. | T06-S034 |
| CFAA 18 USC 1030 | legal | US Computer Fraud and Abuse Act 1986 + 多次 amend; 未授权 access (subsection a)(2)) 5 年; 加重 + intent damage 10 年; civil cause of action; weev / Swartz / Hutchins 案核心法源. | T06-S017 |
| CMA 1990 (UK) | legal | UK Computer Misuse Act 1990; Section 1 unauthorised access 2 年; Section 2 with intent 5 年; Section 3 unauthorised modification 10 年; Section 3A making/supplying tools 2 年. | T06-S018 |
| 中国 刑法 285 | legal | 非法侵入计算机信息系统罪; 三年以下有期 + 加重情节 七年以下; 285 条 1/2/3 款 分别 国防/金融/科技 系统 vs 一般 vs 提供 tools. | T06-S019 |
| 中国 刑法 286 | legal | 破坏计算机信息系统罪; 五年以下 + 加重 五年以上; 删除 / 修改 / 增加 / 干扰 致 系统 不能正常运行. | T06-S019 |
| 中国 刑法 287 | legal | 利用计算机信息系统实施犯罪; 不是 独立罪名而是 入罪 catch-all; 配合 诈骗 / 盗窃 / 侵犯公民个人信息 定罪. | T06-S019 |
| 中国 网络安全法 第 27 条 | legal | 任何 个人 / 组织 不得 从事 非法侵入 + 干扰 + 窃取数据 等 危害网络安全的活动; 明确 渗透 必须 授权 + 等保备案. | T06-S020 |
| 中国 数据安全法 2021 | legal | DSL 2021-09 施行; 数据分类分级 (一般 / 重要 / 核心) + 重要数据出境安全评估 + 数据交易市场监管. | T06-S021 |
| 中国 个人信息保护法 PIPL 2021 | legal | 中国版 GDPR; 2021-11 施行; 第 55 条 PIA 个人信息保护影响评估; 第 28 条 敏感个人信息; 第 38-39 条 跨境提供 三路径. | T06-S022 |
| GDPR Article 32 | legal | EU 2016/679; technical and organizational measures to ensure security appropriate to risk; pseudonymisation + encryption + CIA + resilience + testing + assessment. | T06-S023 |
| DMCA Section 1201 | legal | US Digital Millennium Copyright Act Section 1201; anti-circumvention; security research exemption (Library of Congress triennial review 2015-2018-2021-2024) 部分豁免. | T06-S017 |
| HIPAA | legal | US Health Insurance Portability and Accountability Act 1996; PHI Protected Health Information; Security Rule + Privacy Rule + Breach Notification Rule; 医疗 红队 必读. | T06-S004 |
| SOX | legal | US Sarbanes-Oxley Act 2002; Section 404 internal control over financial reporting; SOC 1 audit; 金融 + 上市公司 红队相关. | T06-S004 |
| PCI DSS v4.0 | legal | Payment Card Industry Data Security Standard 4.0 (2022 release + 2025-03 mandatory); Requirement 11.4 渗透测试 年度 + 重大变更后; cardholder data environment. | T06-S032 |
| Engagement Letter | legal | 红队 / 渗透 服务合同正文; 客户 + 测试方 双方签字; 必含 scope + timeline + deliverables + fee. | T06-S009 |
| SOW (Statement of Work) | legal | Statement of Work; engagement letter 子文档; detailed scope + asset list + IP whitelist + test windows + escalation procedures. | T06-S009 |
| ROE (Rules of Engagement) | legal | Rules of Engagement; 操作边界细则 (允许的 TTPs / 禁止的 actions DoS-default-禁 / 测试时间窗 / emergency contacts / safe word for 社工). | T06-S009 |
| Letter of Authorization | legal | "Get out of jail" letter; engagement letter + ROE 的简化授权证明; operator 现场被 challenged 时出示 (尤其物理 engagement). | T06-S009 |
| Safe Harbor (bug bounty) | legal | Bug bounty program 提供的 法律承诺 不起诉 good-faith research; HackerOne / Bugcrowd / Disclose.io 推 standard template; #LegalBugBounty 倡议. | T06-S045 |
| Aaron's Law | legal | 2013 HR 2454 CFAA 改革提案 (Zoe Lofgren + Ron Wyden); 排除 ToS 违反 即 CFAA 违法; 未通过 但 至今 引用 立法讨论. | T06-S044 |
| NIS2 | legal | EU Directive 2022/2555 Network and Information Security Directive 2; 2024-10 transposed; essential + important entities; 24-72h breach notification. | T06-S023 |
| GLBA | legal | US Gramm-Leach-Bliley Act 1999; financial institutions privacy + safeguards rule; FTC + functional regulators 执法. | T06-S004 |
| OSCP | cert | OffSec Certified Professional (PEN-200); 24h proctored hands-on + 24h report; entry-level red team gold standard. | T06-S026 |
| OSEP | cert | OffSec Experienced Penetration Tester (PEN-300); evasion + AD attacks; intermediate-advanced; 48h exam + report. | T06-S026 |
| OSEE | cert | OffSec Exploitation Expert (EXP-401); 高阶 binary exploitation + Windows kernel; 72h exam; smallest cert population. | T06-S026 |
| OSED | cert | OffSec Exploit Developer (EXP-301); Windows user-land exploit dev; entry binary exploitation. | T06-S026 |
| OSWA | cert | OffSec Web Assessor (WEB-200); web pentest entry; 替代 老 OSWP 命名. | T06-S026 |
| OSWE | cert | OffSec Web Expert (WEB-300); advanced web (white box + custom exploit chain); 48h exam. | T06-S026 |
| OSCE3 | cert | OSEP + OSED + OSWE 三合一 designation; OffSec 2021 推出; 替代 老 OSCE 单 cert. | T06-S026 |
| GPEN | cert | GIAC Penetration Tester (SANS SEC560); network pentest; 普及度高 + 美国政府合规常引. | T06-S027 |
| GXPN | cert | GIAC Exploit Researcher and Advanced Pen Tester (SANS SEC660); advanced exploit dev + AD attacks. | T06-S027 |
| GMOB | cert | GIAC Mobile Device Security Analyst (SANS SEC575); mobile pentest. | T06-S027 |
| GCIH | cert | GIAC Certified Incident Handler (SANS SEC504); 蓝队 cross-over 但 红队反推必修. | T06-S027 |
| GREM | cert | GIAC Reverse Engineering Malware (SANS FOR610); malware analysis cross-discipline. | T06-S027 |
| CEH | cert | EC-Council Certified Ethical Hacker; entry-level + 多选题 + 历史争议较多; HR 友好但 业内非偏好. | T06-S027 |
| CPENT / LPT | cert | EC-Council Certified Penetration Testing Professional / Licensed Penetration Tester; CEH 升级路径. | T06-S027 |
| CRTO | cert | Zero-Point Security Certified Red Team Operator; Daniel Duggan (@_RastaMouse); Cobalt Strike 实操 + AD; 性价比高 community 推荐. | T06-S028 |
| CRTL | cert | Zero-Point Security Certified Red Team Lead; CRTO 进阶 + payload dev + engagement lead. | T06-S028 |
| CRTP | cert | Altered Security Certified Red Team Professional; Nikhil Mittal; AD attack 入门 + 24h hands-on; 性价比最高 AD cert. | T06-S029 |
| CRTE | cert | Altered Security Certified Red Team Expert; CRTP 进阶 + multi-forest + Azure AD. | T06-S029 |
| CRTM | cert | Altered Security Certified Red Team Master; engagement lead + 高级 evasion. | T06-S029 |
| CISSP | cert | ISC2 Certified Information Systems Security Professional; 管理向 + 5 年经验要求; 红队 selling cert 高于 hands-on cert. | T06-S033 |
| Red Team | role | 模拟真实 adversary 攻击客户环境的团队; 与传统 pentest 区别 = stealth + assumed-breach + objectives-driven + multi-week-engagement. | T06-S001 |
| Blue Team | role | 防御侧; SOC analyst + detection engineer + incident responder; 平行学科 但 红队反推必修. | T06-S002 |
| Purple Team | role | 红 + 蓝 协作; 共同 build + test detection; Atomic Red Team / CALDERA / Vectr 协作工具; 高水准红队 default 模式. | T06-S050 |
| White Team | role | 演练 监督方; engagement 期间 客户内部协调 + emergency stop authority + scope arbiter. | T06-S042 |
| SOC | role | Security Operations Center; 7×24 监控 + triage + incident response. | T06-S004 |
| CSIRT | role | Computer Security Incident Response Team; 较 SOC 更聚焦 incident response (vs 持续监控). | T06-S031 |
| CISO | role | Chief Information Security Officer; 客户侧 engagement 主要 sponsor + final approval. | T06-S005 |
| Assumed Breach | role | Engagement 假设初始 access 已得 (skip phishing 阶段); 重 内部 lateral + privesc + persistence; 现代 红队默认场景. | T06-S001 |
| Adversary Emulation | role | 模拟特定 APT 组 (APT29 / FIN7 / Lazarus) 的 specific TTPs; CALDERA + Atomic Red Team 配合; ATT&CK Groups 映射. | T06-S050 |
| Adversary Simulation | role | 与 Emulation 区分; 不限定 specific group; 自由组合 TTPs 达成 objectives; 多数 红队 engagement 实操模式. | T06-S001 |
| TIBER-EU | role | Threat Intelligence-Based Ethical Red Teaming; ECB 2018; EU 金融基础设施 红队标准; 含 TI + RT 双阶段. | T06-S043 |
| CBEST | role | UK Bank of England + NCSC 联合; 金融部门 intelligence-led red team framework; TIBER-EU 的英国对应. | T06-S042 |
| Spear Phishing | phishing | T1566.001 / 002 / 003; targeted phishing; 个人化诱饵 + 特定 victim list; 区别于 mass phishing. | T06-S001 |
| Whaling | phishing | Spear phishing 子类; target 高管 / C-suite; 高价值 fraud / BEC Business Email Compromise. | T06-S001 |
| Smishing | phishing | SMS phishing; T1566.004 (新 sub-technique); mobile-first 攻击面. | T06-S001 |
| Vishing | phishing | Voice phishing; 电话 + caller ID spoofing; T1566.004; deepfake voice 2024+ 已实战. | T06-S001 |
| Tycoon 2FA | phishing | Adversary-in-the-Middle phishing kit; 2023+ 主流; reverse proxy 截获 MFA token; Microsoft 365 主要目标. | T06-S001 |
| Evilginx2 | phishing | Reverse proxy phishing framework; Kuba Gretzky; session cookie 截获 绕过 MFA; lure 模板生态丰富. | T06-S001 |
| Modlishka | phishing | Polish researcher Piotr Duszyński; reverse proxy phishing; Evilginx 之前的主流. | T06-S001 |
| AiTM | phishing | Adversary in the Middle; Tycoon 2FA / Evilginx 类技术总称; Microsoft 2022 命名. | T06-S001 |
| Device Code Phishing | phishing | OAuth 2.0 Device Code flow abuse; 用户输入 code 至合法 microsoft.com 自愿授权; 无需 victim password; Bobby Rauch 2021 研究. | T06-S001 |
| Pretexting | phishing | 社工 准备角色 + 背景故事 增加可信; Christopher Hadnagy 框架; vishing 必备. | T06-S046 |
| Tailgating | physical | T1200 类 (Hardware Additions 类比); 跟随 合法员工 通过门禁; 物理 social engineering 第一步. | T06-S046 |
| Piggyback | physical | Tailgating 同义; 与 主动 hold door open 的合作 区分 (后者 victim 知情). | T06-S046 |
| Badge Cloning | physical | RFID 125kHz (HID Prox / EM4100) + 13.56MHz (HID iCLASS / MIFARE) clone; Proxmark3 + Flipper Zero 工具. | T06-S046 |
| Proxmark3 | physical | RFRD / NFC research + clone hardware; Iceman fork 是主流 firmware; 125kHz + 13.56MHz + Mifare crack. | T06-S046 |
| Flipper Zero | physical | Multi-protocol 玩具/工具 (Sub-GHz + RFID + NFC + IR + GPIO); Tamagotchi 外形 + 社区 firmware; 2023+ Canada / Brazil 受限. | T06-S046 |
| ESPKey | physical | Wiegand wire MITM device; 安装在 reader 与 controller 之间; 抓 + replay badge data; Red Team Tools 推出. | T06-S046 |
| Bash Bunny | physical | Hak5 USB attack platform; HID + storage + serial 多 mode; payload 切换. | T06-S046 |
| Rubber Ducky | physical | Hak5 USB HID injection; 写 ducky script 模拟 keyboard input; Mr. Robot 出名. | T06-S046 |
| TOOOL | physical | The Open Organisation Of Lockpickers; 非营利锁具教学组织; DEF CON Physical Security Village 主办方. | T06-S046 |
| weev (Andrew Auernheimer) | case | AT&T iPad ICC-ID enumeration 2010; CFAA 起诉 + 41 月监禁 2012; 第三巡回 2014 venue 推翻 释放; 教训 = 公开 endpoint 暴力枚举仍触 CFAA. | T06-S017 |
| Aaron Swartz | case | JSTOR 论文 批量下载 MIT 2011; 联邦 13 项 CFAA + Wire Fraud 起诉 最高 35 年; 2013-01 自杀; 触发 Aaron's Law CFAA 改革立法讨论; 业内 CFAA 重判 反思源点. | T06-S044 |
| Marcus Hutchins | case | WannaCry kill switch 注册英雄 2017-05; 同年 8 月 FBI 因 Kronos malware 历史 plea bargain 拘留; 业内重新接纳; 灰色历史 vs 当前贡献 严区分. | T06-S041 |
| NSO Group / Pegasus | case | 商业 spyware 卖给 政府监控 记者 + 异见者 + 律师; Citizen Lab + Amnesty 严批评; 2021 US 商务部 实体清单; 行业明边界 反例. | T06-S031 |
| Cellebrite UFED | case | iPhone 解锁工具 卖给 威权政府 + 美国警方; 同 NSO 类 灰色 商业模式; 行业明边界 反例. | T06-S031 |
| Stuxnet 2010 | case | Symantec + Kaspersky disclosure; 国家级 cyber-physical 攻击 Iran Natanz PLC; air-gap 跳跃 + 4 个 0-day; 行业边界教训. | T06-S031 |
| NotPetya 2017 | case | Mandiant 归因 GRU; Ukrainian M.E.Doc supply-chain wiper; 全球 $10B+ 损失 (Maersk + Merck + FedEx); supply-chain 风险标志事件. | T06-S031 |
| SolarWinds Orion 2020 | case | FireEye / Mandiant 自身被 APT29 (SVR) attack 触发披露; Orion 软件更新 supply-chain 投毒; 18000+ 客户受影响; 边界教训 supply chain risk. | T06-S031 |
