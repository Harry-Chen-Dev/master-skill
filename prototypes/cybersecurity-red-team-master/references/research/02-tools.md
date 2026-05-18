# Track 02 — Tools (Cybersecurity Red Team / Offensive Security Operations)

> Wave 1 Track 02 — 必备工具栈 (≥80% engagement 使用) + 场景特化 (Web / 移动 / 云 / AD / C2 / 物理 / 无线 / 物理-社工) + 新兴 (近 12 月) + 选型决策树 + 避坑清单. Industry: Cybersecurity Red Team — Offensive Security Operations, locale=en (global English primary, zh-CN secondary), profile=practitioner. 全部工具默认 authorized engagement 使用 — 任何 unauthorized 使用 = CFAA / CMA / 中国 刑法 285 / 286 重罪.

红队工具栈的整体结构与软件架构 / 牙科 / 法律完全不同 — 它没有 "1 个事实标准 SOT 平台 + N 个 niche 替代品" 的清晰分层, 反而是 **9 大功能层 (C2 + payload dev + AD recon/abuse + Web fuzzer/scanner + 移动 instrumentation + 云 enum/exploit + binary RE + 物理/社工 hardware + reporting/collab)** 在不同 engagement 类型里相互交错, 同一个 engagement 里 operator 平均要打开 12-18 个工具窗口 (业内估 — 基于 SANS SEC560 + CRTO 课件实验 + ired.team 案例). 工具间没有官方 integration — operator 自己用 tmux / Windows Terminal / Sliver client + Burp + Ghidra + BloodHound GUI + Excel 报告模板 + Notion / Obsidian / Joplin 笔记 + Signal / Slack 客户沟通 拼装出 daily workflow. 这种碎片化是行业客观结构, 不是工具厂商缺位 — 红队 engagement 本身就是 "ATT&CK 14 战术 × 600+ 技术" 的 combinatorial 空间, 不可能由单一工具覆盖.

按商业 / OSS / SaaS / 学习 lab 四象限分: **canonical commercial** = Cobalt Strike (Fortra, 红队 C2 事实首选, $5k+/year per operator, 严格 license screening 不卖个人 + 不卖制裁国) + Burp Suite Pro (PortSwigger, Web 测试事实标准, $475/year per user) + IDA Pro (Hex-Rays, 二进制 RE 商业霸主, $2.5k+ Home / $10k+ Pro per year) + Brute Ratel (Chetan Nayak Dark Vortex, modern 进阶 C2 商业, 严格 vetting); **canonical OSS** = Metasploit Framework (Rapid7 维护, 历史最长 + 最大 exploit 库 5000+ modules) + Nmap (Gordon "Fyodor" Lyon, 端口扫描事实标准 26 年+) + BloodHound (SpecterOps, AD 攻击路径事实标准) + Sliver (Bishop Fox, 开源 modern C2) + Impacket (Fortra 维护 SecureAuthCorp 起源, Python AD/SMB 协议工具集) + Mimikatz (Benjamin Delpy / gentilkiwi, AD 凭据滥用事实标准); **SaaS** = Cobalt Strike teamserver hosting (各 vendor) + Burp Suite Enterprise (PortSwigger SaaS) + 各 EDR vendor (CrowdStrike Falcon / SentinelOne / Microsoft Defender for Endpoint) + BloodHound Enterprise (SpecterOps 商用 SaaS, 持续 attack path management); **学习 lab** = HackTheBox (HTB Labs + HTB Academy CPTS/CBBH/CWEE 认证) + TryHackMe (rooms + paths 入门标杆) + OffSec Proving Grounds (OSCP 备考 lab) + PentesterLab (Web 漏洞专项) + PortSwigger Web Security Academy (免费, 240+ Web lab 事实 syllabus).

C2 framework 这一层是红队工具栈的灵魂 — 因为它是 post-exploitation 全流程的 host, 所有 implant / persistence / lateral / data exfil 都通过 C2 channel 协调. **Cobalt Strike 自 2012 (Raphael Mudge Strategic Cyber LLC) 起 25 年是行业事实首选**, Beacon + Aggressor Script + Malleable C2 Profile 的组合让 operator 能高度定制 OPSEC 行为 (sleep / jitter / DNS over HTTPS / HTTPS / SMB pipe / TCP / external C2). 2020 年被 Fortra (前 HelpSystems) 收购后 license 收紧 — 不卖给个人 / 不卖制裁国 / 强制 background check, 这反而催生 OSS 替代品爆发. **Sliver (Bishop Fox, 2019+, Go 写 BSD-3) + Mythic (SpecterOps Cody Thomas, 2018+, Python + Docker 模块化 multi-agent) + Havoc (C5pider, 2022+, 现代 C++ 风格 community OSS) + Brute Ratel (Chetan Nayak Dark Vortex 商业, 2020+, OPSEC 顶级但 license 严控)** 形成 4 大现代 C2 替代品矩阵. 历史 C2 框架 — Empire (PowerShell, 现 BC Security OSS 维护) / PoshC2 (Nettitude OSS Python) / Covenant (.NET C# OSS) — 仍在学习场景使用, 但生产 engagement 已基本被现代框架取代. Metasploit Meterpreter 是 OSS C2 的鼻祖, 现在主要用于 OSCP 备考 (考场限 1 次 Metasploit) + 培训 demo, 真实 engagement 因签名问题 (所有 EDR 都有 default Meterpreter signature) 基本不上.

AD 红队工具的 canon 高度集中在 **SpecterOps 生态 (BloodHound + SharpHound + AzureHound + GhostPack 系列 Rubeus/Seatbelt/SafetyKatz)** + **Impacket suite (Fortra, Python NTLM/Kerberos/SMB/MSRPC 完整实现 — secretsdump / psexec / wmiexec / smbexec / ntlmrelayx / GetUserSPNs / GetNPUsers / dcomexec / addcomputer / 共 60+ utility)** + **NetExec (前 CrackMapExec, @Pennyw0rth 维护, SMB / WinRM / MSSQL / SSH / RDP / FTP / LDAP / WMI / VNC swiss-army 多协议批量) + Responder (LLMNR/NBT-NS/MDNS poison + NTLM relay capture) + Mimikatz (Benjamin Delpy, 凭据 dump + Pass-the-Hash + Golden Ticket + Silver Ticket + DCSync + DCShadow 鼻祖) + Certipy (ADCS ESC1-15 abuse, Oliver Lyak)** 这一套组合. 现代 AD engagement 90%+ 时间在这套工具内. Web pentest 的 canon = Burp Suite Pro (Java, 商业标准) + sqlmap (Python, SQLi OSS 事实标准) + ffuf (Go, 现代 fuzzer 取代旧 wfuzz/gobuster/dirb) + nuclei (ProjectDiscovery YAML template scanner) + subfinder/amass/httpx/naabu (ProjectDiscovery 侦察套件). 移动 = Frida (动态 instrumentation 事实标准, Ole André V. Ravnås) + Objection (Frida 上层 Sensepost) + apktool/jadx (Android 静态) + Hopper/Ghidra/IDA (iOS Mach-O). 云 = Pacu (AWS, Rhino Security Labs) + Prowler (multi-cloud audit) + ScoutSuite (NCC Group multi-cloud) + AzureHound + ROADtools (Azure AD) + kube-hunter/peirates (K8s). Binary RE = IDA Pro (商业) + Ghidra (NSA OSS, .gov 一手) + Binary Ninja (Vector 35 商业 mid-tier) + radare2/Cutter (OSS).

选型决策树有 6 个常见交叉维度: **(1) 商用 license 预算 + 客户接受度** — 大型金融 / 政府 客户 要求 Cobalt Strike 或同等 OPSEC 级别 + 商业 EULA 法律保障, 小客户 / startup engagement 可用 Sliver/Mythic OSS; **(2) OPSEC 对抗 EDR 水平** — 客户 EDR 已 deploy CrowdStrike Falcon / SentinelOne / Microsoft Defender for Endpoint 等 Tier 1, 必须 Cobalt Strike Malleable C2 Profile 调优 或 Brute Ratel 商业, OSS 默认 profile (Sliver / Havoc / Mythic out-of-box) 基本秒被 detect; **(3) 团队 trust 阈值** — Brute Ratel + Cobalt Strike 都需要 Fortra / Dark Vortex 严格 vetting (公司 background + 公司 use case + 政府名单 cross-check), individual researcher 难拿到 license, 选 OSS; **(4) 客户 ROE 限制** — 客户禁 cracked Cobalt Strike (合理担忧 OPSEC 已 burn + 法律风险) → 强制 OSS; 客户禁 公网 redirector (内网 only) → C2 选 SMB pipe / named pipe / TCP beacon 而不是 HTTPS; **(5) 法律地域** — 中国境内 engagement 必须 等保备案 + 公安部 / 网信办 报备 + 资质渗透公司协作, 工具选型同时要考虑 数据安全法 (任何客户数据离境 严管); 欧盟 engagement GDPR 约束 客户 PII 处理 严限; **(6) 工具签名状态 + EDR 反应** — Mimikatz GitHub release binary = 99% trip on Defender, 必须自编译 + 加壳 + AMSI bypass + 内存 only loading (SafetyKatz + Donut + sRDI 反射式加载技术).

---

## Source Manifest

| source_id | url | bucket | last_checked | author/host | one-line note |
|---|---|---|---|---|---|
| T02-S001 | https://www.cobaltstrike.com/product/features | surrogate_primary | 2026-05-18 | Fortra (originally Raphael Mudge) | vendor docs (工具厂商) — Cobalt Strike 官方 features + Beacon + Malleable C2 Profile + Aggressor Script + BOF [declared=surrogate_primary, auto=secondary; reason=vendor docs (工具厂商)] |
| T02-S002 | https://hstechdocs.helpsystems.com/manuals/cobaltstrike/current/userguide/content/topics/welcome_main.htm | surrogate_primary | 2026-05-18 | Fortra HelpSystems | vendor docs (工具厂商) — Cobalt Strike User Guide v4.10+ 官方手册 [declared=surrogate_primary, auto=secondary; reason=vendor docs (工具厂商)] |
| T02-S003 | https://github.com/BishopFox/sliver | surrogate_primary | 2026-05-18 | Bishop Fox / GitHub | vendor docs (开源工具 一手) — Sliver C2 BSD-3 Go 写, mTLS / HTTP(S) / DNS / WireGuard 通道 [declared=surrogate_primary, auto=secondary; reason=vendor docs (开源工具 一手)] |
| T02-S004 | https://sliver.sh/ | surrogate_primary | 2026-05-18 | Bishop Fox | vendor docs (开源工具 一手 文档) — Sliver 官方 wiki + docs [declared=surrogate_primary, auto=secondary; reason=vendor docs (开源工具 一手 文档)] |
| T02-S005 | https://docs.mythic-c2.net/ | surrogate_primary | 2026-05-18 | Cody Thomas / SpecterOps | vendor docs (开源工具 一手) — Mythic C2 framework docs, multi-agent (Apollo / Athena / Apfell / Poseidon / Merlin) + Docker 部署 [declared=surrogate_primary, auto=secondary; reason=vendor docs (开源工具 一手)] |
| T02-S006 | https://github.com/HavocFramework/Havoc | surrogate_primary | 2026-05-18 | C5pider / GitHub | vendor docs (开源工具 一手) — Havoc C2 modern community OSS, C++ 写 + Demon agent [declared=surrogate_primary, auto=secondary; reason=vendor docs (开源工具 一手)] |
| T02-S007 | https://bruteratel.com/ | surrogate_primary | 2026-05-18 | Chetan Nayak / Dark Vortex | vendor docs (工具厂商) — Brute Ratel C4 商业 modern C2, OPSEC 顶级 + 严格 vetting [declared=surrogate_primary, auto=secondary; reason=vendor docs (工具厂商)] |
| T02-S008 | https://github.com/BC-SECURITY/Empire | surrogate_primary | 2026-05-18 | BC Security / GitHub | vendor docs (开源工具 一手) — Empire 5.x PowerShell + Python C2, 原 SpecterOps 现 BC Security 维护 [declared=surrogate_primary, auto=secondary; reason=vendor docs (开源工具 一手)] |
| T02-S009 | https://github.com/nettitude/PoshC2 | surrogate_primary | 2026-05-18 | Nettitude / GitHub | vendor docs (开源工具 一手) — PoshC2 Python C2 + PowerShell payload [declared=surrogate_primary, auto=secondary; reason=vendor docs (开源工具 一手)] |
| T02-S010 | https://docs.metasploit.com/ | surrogate_primary | 2026-05-18 | Rapid7 | vendor docs (工具厂商 + 开源工具 一手) — Metasploit Framework 官方文档, 5000+ exploit modules, Meterpreter post-ex shell [declared=surrogate_primary, auto=secondary; reason=vendor docs (工具厂商 + 开源工具)] |
| T02-S011 | https://github.com/rapid7/metasploit-framework | surrogate_primary | 2026-05-18 | Rapid7 / GitHub | vendor docs (开源工具 一手) — Metasploit Framework BSD-3 OSS, HD Moore 创立 (2003) 现 Rapid7 维护 [declared=surrogate_primary, auto=secondary; reason=vendor docs (开源工具 一手)] |
| T02-S012 | https://nmap.org/book/man.html | surrogate_primary | 2026-05-18 | Gordon Lyon (Fyodor) / nmap.org | vendor docs (作者一手 + 协会 + 教材) — Nmap 官方 reference manual + Network Scanning book [declared=surrogate_primary, auto=secondary; reason=vendor docs (作者一手 + 协会 + 教材)] |
| T02-S013 | https://github.com/SpecterOps/BloodHound | surrogate_primary | 2026-05-18 | SpecterOps / GitHub | vendor docs (开源工具 一手) — BloodHound Community Edition (BHCE) v6+, 2023 split + Neo4j + 现代 AD attack path [declared=surrogate_primary, auto=secondary; reason=vendor docs (开源工具 一手)] |
| T02-S014 | https://bloodhound.specterops.io/ | surrogate_primary | 2026-05-18 | SpecterOps | vendor docs (作者一手 + 公司) — BloodHound CE + Enterprise 官方 docs, attack path + Cypher queries [declared=surrogate_primary, auto=secondary; reason=vendor docs (作者一手 + 公司)] |
| T02-S015 | https://bloodhoundenterprise.io/ | surrogate_primary | 2026-05-18 | SpecterOps | vendor docs (公司一手) — BloodHound Enterprise 商用 SaaS, attack path management 持续监控 [declared=surrogate_primary, auto=secondary; reason=vendor docs (公司一手)] |
| T02-S016 | https://github.com/fortra/impacket | surrogate_primary | 2026-05-18 | Fortra (originally SecureAuth) / GitHub | vendor docs (开源工具 一手) — Impacket Python AD/SMB/MSRPC/NTLM/Kerberos suite, 60+ utility scripts [declared=surrogate_primary, auto=secondary; reason=vendor docs (开源工具 一手)] |
| T02-S017 | https://github.com/Pennyw0rth/NetExec | surrogate_primary | 2026-05-18 | @Pennyw0rth / GitHub | vendor docs (开源工具 一手) — NetExec (CrackMapExec successor), SMB/WinRM/MSSQL/SSH/RDP/FTP/LDAP/WMI/VNC swiss-army [declared=surrogate_primary, auto=secondary; reason=vendor docs (开源工具 一手)] |
| T02-S018 | https://github.com/lgandx/Responder | surrogate_primary | 2026-05-18 | Laurent Gaffié / GitHub | vendor docs (开源工具 一手) — Responder LLMNR/NBT-NS/MDNS poisoner + NTLM relay capture, Python [declared=surrogate_primary, auto=secondary; reason=vendor docs (开源工具 一手)] |
| T02-S019 | https://github.com/Kevin-Robertson/Inveigh | surrogate_primary | 2026-05-18 | Kevin Robertson / GitHub | vendor docs (开源工具 一手) — Inveigh PowerShell + C# Responder 等价物, Windows host 端 [declared=surrogate_primary, auto=secondary; reason=vendor docs (开源工具 一手)] |
| T02-S020 | https://github.com/gentilkiwi/mimikatz | surrogate_primary | 2026-05-18 | Benjamin Delpy (gentilkiwi) / GitHub | vendor docs (开源工具 一手) — Mimikatz AD 凭据 dump + Pass-the-Hash + Golden/Silver Ticket + DCSync + DCShadow 鼻祖 [declared=surrogate_primary, auto=secondary; reason=vendor docs (开源工具 一手)] |
| T02-S021 | https://github.com/GhostPack/Rubeus | surrogate_primary | 2026-05-18 | GhostPack (Will Schroeder 等 SpecterOps) / GitHub | vendor docs (开源工具 一手) — Rubeus C# Kerberos abuse (Kerberoasting / AS-REP-roasting / S4U / Pass-the-Ticket) [declared=surrogate_primary, auto=secondary; reason=vendor docs (开源工具 一手)] |
| T02-S022 | https://github.com/GhostPack/Seatbelt | surrogate_primary | 2026-05-18 | GhostPack / SpecterOps / GitHub | vendor docs (开源工具 一手) — Seatbelt C# Windows 安全 enum (host triage + privilege escalation 路径侦察) [declared=surrogate_primary, auto=secondary; reason=vendor docs (开源工具 一手)] |
| T02-S023 | https://github.com/GhostPack/SafetyKatz | surrogate_primary | 2026-05-18 | GhostPack / SpecterOps / GitHub | vendor docs (开源工具 一手) — SafetyKatz Mimikatz 内存版 + AMSI bypass + 反射式加载 [declared=surrogate_primary, auto=secondary; reason=vendor docs (开源工具 一手)] |
| T02-S024 | https://github.com/PowerShellMafia/PowerSploit | surrogate_primary | 2026-05-18 | PowerShellMafia / GitHub | vendor docs (开源工具 一手) — PowerSploit (PowerView + PowerUp + Invoke-Mimikatz + 反射式 PE 加载), 历史 AD 红队工具集, 现代 EDR 已签名 [declared=surrogate_primary, auto=secondary; reason=vendor docs (开源工具 一手)] |
| T02-S025 | https://github.com/ly4k/Certipy | surrogate_primary | 2026-05-18 | Oliver Lyak (ly4k) / GitHub | vendor docs (开源工具 一手) — Certipy ADCS ESC1-15 abuse Python 工具, AD CS 模板攻击事实标准 [declared=surrogate_primary, auto=secondary; reason=vendor docs (开源工具 一手)] |
| T02-S026 | https://github.com/p0dalirius/Coercer | surrogate_primary | 2026-05-18 | Remi Gascou (Podalirius) / GitHub | vendor docs (开源工具 一手) — Coercer Windows auth coercion (PetitPotam / DFSCoerce / PrinterBug 等 10+ 方法) [declared=surrogate_primary, auto=secondary; reason=vendor docs (开源工具 一手)] |
| T02-S027 | https://github.com/dirkjanm/ROADtools | surrogate_primary | 2026-05-18 | Dirk-jan Mollema (dirkjanm) / GitHub | vendor docs (开源工具 一手) — ROADtools Azure AD / Entra ID 红队 enum + abuse, ROADrecon + roadtx [declared=surrogate_primary, auto=secondary; reason=vendor docs (开源工具 一手)] |
| T02-S028 | https://github.com/NetSPI/MicroBurst | surrogate_primary | 2026-05-18 | NetSPI (Karl Fosaaen) / GitHub | vendor docs (开源工具 一手) — MicroBurst Azure 红队 PowerShell 工具集 (subdomain / storage / VM / Function) [declared=surrogate_primary, auto=secondary; reason=vendor docs (开源工具 一手)] |
| T02-S029 | https://portswigger.net/burp | surrogate_primary | 2026-05-18 | PortSwigger | vendor docs (协会 + 工具) — Burp Suite Pro / Community / Enterprise, Web 渗透事实标准 + extension ecosystem [declared=surrogate_primary, auto=secondary; reason=vendor docs (协会 + 工具)] |
| T02-S030 | https://portswigger.net/burp/documentation/desktop | surrogate_primary | 2026-05-18 | PortSwigger | vendor docs (工具) — Burp Suite Desktop docs, Proxy / Repeater / Intruder / Scanner / Collaborator [declared=surrogate_primary, auto=secondary; reason=vendor docs (工具)] |
| T02-S031 | https://caido.io/ | surrogate_primary | 2026-05-18 | Caido Labs | vendor docs (工具厂商) — Caido modern Rust-based Burp alternative, 2023+ 快速崛起 [declared=surrogate_primary, auto=secondary; reason=vendor docs (工具厂商)] |
| T02-S032 | https://www.zaproxy.org/docs/ | surrogate_primary | 2026-05-18 | OWASP ZAP / Software Security Project | vendor docs (协会 + 工具) — OWASP ZAP 开源 Web proxy + scanner, 现 Software Security Project 维护 [declared=surrogate_primary, auto=secondary; reason=vendor docs (协会 + 工具)] |
| T02-S033 | https://github.com/sqlmapproject/sqlmap | surrogate_primary | 2026-05-18 | Bernardo Damele + Miroslav Stampar / GitHub | vendor docs (开源工具 一手) — sqlmap Python SQL injection 事实标准, 1.8+ MySQL/PostgreSQL/MSSQL/Oracle/SQLite [declared=surrogate_primary, auto=secondary; reason=vendor docs (开源工具 一手)] |
| T02-S034 | https://github.com/ffuf/ffuf | surrogate_primary | 2026-05-18 | Joohoi (Joona Hoikkala) / GitHub | vendor docs (开源工具 一手) — ffuf Go-based 现代 Web fuzzer (取代 wfuzz / gobuster / dirb), v2+ [declared=surrogate_primary, auto=secondary; reason=vendor docs (开源工具 一手)] |
| T02-S035 | https://github.com/projectdiscovery/nuclei | surrogate_primary | 2026-05-18 | ProjectDiscovery / GitHub | vendor docs (开源工具 一手) — Nuclei YAML template-based scanner + nuclei-templates community lib 5000+ [declared=surrogate_primary, auto=secondary; reason=vendor docs (开源工具 一手)] |
| T02-S036 | https://github.com/projectdiscovery/subfinder | surrogate_primary | 2026-05-18 | ProjectDiscovery / GitHub | vendor docs (开源工具 一手) — subfinder Go-based subdomain enum (cert transparency + 多源 API) [declared=surrogate_primary, auto=secondary; reason=vendor docs (开源工具 一手)] |
| T02-S037 | https://github.com/projectdiscovery/httpx | surrogate_primary | 2026-05-18 | ProjectDiscovery / GitHub | vendor docs (开源工具 一手) — httpx fast HTTP probe (status + title + tech + cert + screenshot) [declared=surrogate_primary, auto=secondary; reason=vendor docs (开源工具 一手)] |
| T02-S038 | https://github.com/projectdiscovery/naabu | surrogate_primary | 2026-05-18 | ProjectDiscovery / GitHub | vendor docs (开源工具 一手) — naabu fast Go port scanner, SYN + CONNECT 模式 [declared=surrogate_primary, auto=secondary; reason=vendor docs (开源工具 一手)] |
| T02-S039 | https://github.com/owasp-amass/amass | surrogate_primary | 2026-05-18 | OWASP Amass Project / GitHub | vendor docs (协会 + 开源工具) — OWASP Amass subdomain + asset discovery + graph, Jeff Foley 主创 [declared=surrogate_primary, auto=secondary; reason=vendor docs (协会 + 开源工具)] |
| T02-S040 | https://frida.re/docs/home/ | surrogate_primary | 2026-05-18 | Ole André V. Ravnås / frida.re | vendor docs (开源工具 一手 文档) — Frida 动态 instrumentation 框架 (iOS / Android / Windows / Linux / macOS), 移动渗透事实标准 [declared=surrogate_primary, auto=secondary; reason=vendor docs (开源工具 一手 文档)] |
| T02-S041 | https://github.com/sensepost/objection | surrogate_primary | 2026-05-18 | Sensepost / GitHub | vendor docs (开源工具 一手) — Objection runtime mobile exploration on top of Frida (无 编程 instrumentation 命令行界面) [declared=surrogate_primary, auto=secondary; reason=vendor docs (开源工具 一手)] |
| T02-S042 | https://github.com/MobSF/Mobile-Security-Framework-MobSF | surrogate_primary | 2026-05-18 | OpenSecurity (MobSF) / GitHub | vendor docs (开源工具 一手) — MobSF Mobile Security Framework, 自动化 Android + iOS 静动态分析 [declared=surrogate_primary, auto=secondary; reason=vendor docs (开源工具 一手)] |
| T02-S043 | https://ibotpeaches.github.io/Apktool/ | surrogate_primary | 2026-05-18 | Connor Tumbleson (iBotPeaches) | vendor docs (开源工具 一手 文档) — Apktool Android APK 反编译 + 重打包 [declared=surrogate_primary, auto=secondary; reason=vendor docs (开源工具 一手 文档)] |
| T02-S044 | https://github.com/skylot/jadx | surrogate_primary | 2026-05-18 | skylot / GitHub | vendor docs (开源工具 一手) — JADX Android DEX → Java decompiler + GUI [declared=surrogate_primary, auto=secondary; reason=vendor docs (开源工具 一手)] |
| T02-S045 | https://www.hex-rays.com/products/ida/ | surrogate_primary | 2026-05-18 | Hex-Rays | vendor docs (工具厂商) — IDA Pro 商业二进制 RE 事实霸主, Hex-Rays decompiler $2.5k+ Home / $10k+ Pro [declared=surrogate_primary, auto=secondary; reason=vendor docs (工具厂商)] |
| T02-S046 | https://ghidra-sre.org/ | surrogate_primary | 2026-05-18 | NSA / ghidra-sre.org | NSA Ghidra 开源 RE 框架, .gov 一手 (注: ghidra-sre.org 由 NSA 维护, 实际 domain 为 .org 但作者为 .gov 机构 NSA, 走 surrogate 模式) [declared=surrogate_primary, auto=secondary; reason=vendor docs (政府 .gov NSA 开源)] |
| T02-S047 | https://binary.ninja/ | surrogate_primary | 2026-05-18 | Vector 35 | vendor docs (工具厂商) — Binary Ninja 商业二进制分析 + decompiler, mid-tier 价位 [declared=surrogate_primary, auto=secondary; reason=vendor docs (工具厂商)] |
| T02-S048 | https://rada.re/n/ | surrogate_primary | 2026-05-18 | radare2 Project / pancake | vendor docs (开源工具 一手) — radare2 OSS 多平台 RE 框架 + r2 cli [declared=surrogate_primary, auto=secondary; reason=vendor docs (开源工具 一手)] |
| T02-S049 | https://rizin.re/ | surrogate_primary | 2026-05-18 | Rizin Project | vendor docs (开源工具 一手) — Rizin (radare2 friendly fork) + Cutter GUI [declared=surrogate_primary, auto=secondary; reason=vendor docs (开源工具 一手)] |
| T02-S050 | https://github.com/RhinoSecurityLabs/pacu | surrogate_primary | 2026-05-18 | Rhino Security Labs / GitHub | vendor docs (开源工具 一手) — Pacu AWS exploitation framework + 80+ 攻击模块, Spencer Gietzen 主创 [declared=surrogate_primary, auto=secondary; reason=vendor docs (开源工具 一手)] |
| T02-S051 | https://docs.prowler.com/ | surrogate_primary | 2026-05-18 | Prowler Project / Toni de la Fuente | vendor docs (开源工具 一手) — Prowler AWS/GCP/Azure/K8s CSPM + 500+ 检查 (CIS/NIST/PCI/HIPAA/ISO27001) [declared=surrogate_primary, auto=secondary; reason=vendor docs (开源工具 一手)] |
| T02-S052 | https://github.com/nccgroup/ScoutSuite | surrogate_primary | 2026-05-18 | NCC Group / GitHub | vendor docs (开源工具 一手) — ScoutSuite multi-cloud 安全 audit (AWS / Azure / GCP / Alibaba / Oracle) [declared=surrogate_primary, auto=secondary; reason=vendor docs (开源工具 一手)] |
| T02-S053 | https://github.com/RhinoSecurityLabs/cloudgoat | surrogate_primary | 2026-05-18 | Rhino Security Labs / GitHub | vendor docs (开源工具 一手) — CloudGoat AWS 渗透 CTF 训练 lab [declared=surrogate_primary, auto=secondary; reason=vendor docs (开源工具 一手)] |
| T02-S054 | https://github.com/aquasecurity/kube-hunter | surrogate_primary | 2026-05-18 | Aqua Security / GitHub | vendor docs (开源工具 一手) — kube-hunter K8s 渗透 + attack 模拟 [declared=surrogate_primary, auto=secondary; reason=vendor docs (开源工具 一手)] |
| T02-S055 | https://github.com/inguardians/peirates | surrogate_primary | 2026-05-18 | InGuardians / GitHub | vendor docs (开源工具 一手) — Peirates K8s pentest tool (Pod 内运行, escape + lateral) [declared=surrogate_primary, auto=secondary; reason=vendor docs (开源工具 一手)] |
| T02-S056 | https://aquasecurity.github.io/trivy/ | surrogate_primary | 2026-05-18 | Aqua Security | vendor docs (开源工具 一手 文档) — Trivy OSS 容器 + IaC + 仓库 + license 扫描, multi-target [declared=surrogate_primary, auto=secondary; reason=vendor docs (开源工具 一手 文档)] |
| T02-S057 | https://nmap.org/ | surrogate_primary | 2026-05-18 | Gordon Lyon (Fyodor) | vendor docs (作者一手 + 协会) — Nmap 26 年+ 端口扫描事实标准 + NSE 脚本 + zenmap GUI [declared=surrogate_primary, auto=secondary; reason=vendor docs (作者一手 + 协会)] |
| T02-S058 | https://github.com/robertdavidgraham/masscan | surrogate_primary | 2026-05-18 | Robert Graham (Errata Security) / GitHub | vendor docs (开源工具 一手) — masscan 高速端口扫描 (整 IPv4 5 分钟) [declared=surrogate_primary, auto=secondary; reason=vendor docs (开源工具 一手)] |
| T02-S059 | https://www.wireshark.org/docs/ | surrogate_primary | 2026-05-18 | Wireshark Foundation | vendor docs (协会 + 工具) — Wireshark 协议分析事实标准 + tshark CLI [declared=surrogate_primary, auto=secondary; reason=vendor docs (协会 + 工具)] |
| T02-S060 | https://mitmproxy.org/ | surrogate_primary | 2026-05-18 | Aldo Cortesi / mitmproxy.org | vendor docs (开源工具 一手 文档) — mitmproxy Python interactive HTTPS proxy + scripting [declared=surrogate_primary, auto=secondary; reason=vendor docs (开源工具 一手 文档)] |
| T02-S061 | https://www.aircrack-ng.org/doku.php | surrogate_primary | 2026-05-18 | Aircrack-ng team / aircrack-ng.org | vendor docs (开源工具 一手 文档) — Aircrack-ng WPA/WPA2/WEP 破解 + airodump + airmon + aireplay [declared=surrogate_primary, auto=secondary; reason=vendor docs (开源工具 一手 文档)] |
| T02-S062 | https://hashcat.net/wiki/ | surrogate_primary | 2026-05-18 | Jens Steube (Atom) / hashcat.net | vendor docs (工具厂商 + 协会) — hashcat GPU 密码破解事实标准, 300+ hash 算法支持 [declared=surrogate_primary, auto=secondary; reason=vendor docs (工具厂商 + 协会)] |
| T02-S063 | https://www.openwall.com/john/doc/ | surrogate_primary | 2026-05-18 | Openwall Project | vendor docs (工具厂商 + 协会) — John the Ripper 密码破解经典 OSS + Jumbo edition [declared=surrogate_primary, auto=secondary; reason=vendor docs (工具厂商 + 协会)] |
| T02-S064 | https://getgophish.com/ | surrogate_primary | 2026-05-18 | Jordan Wright (Duo) / Gophish | vendor docs (开源工具 一手) — Gophish OSS phishing campaign framework, Go 写 [declared=surrogate_primary, auto=secondary; reason=vendor docs (开源工具 一手)] |
| T02-S065 | https://github.com/kgretzky/evilginx2 | surrogate_primary | 2026-05-18 | Kuba Gretzky / GitHub | vendor docs (开源工具 一手) — Evilginx2 AiTM phishing proxy (绕过 2FA + session cookie 捕获) [declared=surrogate_primary, auto=secondary; reason=vendor docs (开源工具 一手)] |
| T02-S066 | https://github.com/drk1wi/Modlishka | surrogate_primary | 2026-05-18 | Piotr Duszyński / GitHub | vendor docs (开源工具 一手) — Modlishka AiTM reverse proxy, Evilginx2 替代品 [declared=surrogate_primary, auto=secondary; reason=vendor docs (开源工具 一手)] |
| T02-S067 | https://github.com/fin3ss3g0d/evilgophish | surrogate_primary | 2026-05-18 | fin3ss3g0d / GitHub | vendor docs (开源工具 一手) — EvilGoPhish Gophish + Evilginx 整合, SMS + email phishing [declared=surrogate_primary, auto=secondary; reason=vendor docs (开源工具 一手)] |
| T02-S068 | https://shop.hak5.org/products/usb-rubber-ducky | surrogate_primary | 2026-05-18 | Hak5 LLC | vendor docs (工具厂商) — USB Rubber Ducky HID keystroke injection 物理工具 [declared=surrogate_primary, auto=secondary; reason=vendor docs (工具厂商)] |
| T02-S069 | https://shop.hak5.org/products/bash-bunny | surrogate_primary | 2026-05-18 | Hak5 LLC | vendor docs (工具厂商) — Bash Bunny multi-vector USB attack platform + payload library [declared=surrogate_primary, auto=secondary; reason=vendor docs (工具厂商)] |
| T02-S070 | https://shop.hak5.org/products/wifi-pineapple | surrogate_primary | 2026-05-18 | Hak5 LLC | vendor docs (工具厂商) — Wi-Fi Pineapple rogue AP + Wi-Fi MITM 平台 [declared=surrogate_primary, auto=secondary; reason=vendor docs (工具厂商)] |
| T02-S071 | https://proxmark.com/ | surrogate_primary | 2026-05-18 | RfidResearchGroup / Proxmark.com | vendor docs (工具厂商 + 开源) — Proxmark3 RFID/NFC 读取 + clone + sniff + emulate [declared=surrogate_primary, auto=secondary; reason=vendor docs (工具厂商 + 开源)] |
| T02-S072 | https://flipperzero.one/ | surrogate_primary | 2026-05-18 | Flipper Devices / flipperzero.one | vendor docs (工具厂商) — Flipper Zero multi-RF 玩具 (Sub-GHz + RFID + NFC + IR + BLE + iButton) [declared=surrogate_primary, auto=secondary; reason=vendor docs (工具厂商)] |
| T02-S073 | https://github.com/carlospolop/PEASS-ng | surrogate_primary | 2026-05-18 | Carlos Polop / GitHub | vendor docs (开源工具 一手) — PEASS-ng (LinPEAS + WinPEAS + macPEAS) 提权枚举事实标准 [declared=surrogate_primary, auto=secondary; reason=vendor docs (开源工具 一手)] |
| T02-S074 | https://github.com/AlessandroZ/LaZagne | surrogate_primary | 2026-05-18 | Alessandro Z / GitHub | vendor docs (开源工具 一手) — LaZagne cross-platform 凭据 dump (浏览器 / WiFi / 邮件 / 数据库 / SSH) [declared=surrogate_primary, auto=secondary; reason=vendor docs (开源工具 一手)] |
| T02-S075 | https://github.com/skelsec/pypykatz | surrogate_primary | 2026-05-18 | Tamas Jos (skelsec) / GitHub | vendor docs (开源工具 一手) — pypykatz Python pure-Python Mimikatz 等价物 (LSASS parse) [declared=surrogate_primary, auto=secondary; reason=vendor docs (开源工具 一手)] |
| T02-S076 | https://github.com/jpillora/chisel | surrogate_primary | 2026-05-18 | Jaime Pillora (jpillora) / GitHub | vendor docs (开源工具 一手) — chisel Go-based fast TCP/UDP tunnel over HTTP/WebSocket [declared=surrogate_primary, auto=secondary; reason=vendor docs (开源工具 一手)] |
| T02-S077 | https://github.com/nicocha30/ligolo-ng | surrogate_primary | 2026-05-18 | Nicolas Chatelain (nicocha30) / GitHub | vendor docs (开源工具 一手) — Ligolo-ng modern Go reverse tunneling (TUN interface, 比 chisel 高效) [declared=surrogate_primary, auto=secondary; reason=vendor docs (开源工具 一手)] |
| T02-S078 | https://github.com/redcanaryco/atomic-red-team | surrogate_primary | 2026-05-18 | Red Canary / GitHub | vendor docs (开源工具 一手) — Atomic Red Team ATT&CK 测试库 (TTP 复现 + detection 验证) [declared=surrogate_primary, auto=secondary; reason=vendor docs (开源工具 一手)] |
| T02-S079 | https://caldera.mitre.org/ | surrogate_primary | 2026-05-18 | MITRE Corporation | vendor docs (协会 + 教材) — MITRE CALDERA 自动化对手模拟 + plugin (Stockpile + Sandcat agent) [declared=surrogate_primary, auto=secondary; reason=vendor docs (协会 + 教材)] |
| T02-S080 | https://www.kali.org/docs/ | surrogate_primary | 2026-05-18 | OffSec / Kali Linux | vendor docs (cert org + 工具) — Kali Linux 红队事实主流 OS, OffSec 维护 + 600+ 预装工具 [declared=surrogate_primary, auto=secondary; reason=vendor docs (cert org + 工具)] |
| T02-S081 | https://parrotsec.org/docs/ | surrogate_primary | 2026-05-18 | Parrot Security | vendor docs (工具厂商) — Parrot OS Kali 替代 Linux distro, 隐私 + 渗透 + 加密 [declared=surrogate_primary, auto=secondary; reason=vendor docs (工具厂商)] |
| T02-S082 | https://blackarch.org/ | surrogate_primary | 2026-05-18 | BlackArch Linux | vendor docs (工具厂商) — BlackArch Arch-based rolling 红队 distro, 2700+ 工具 [declared=surrogate_primary, auto=secondary; reason=vendor docs (工具厂商)] |
| T02-S083 | https://github.com/mandiant/commando-vm | surrogate_primary | 2026-05-18 | Mandiant / GitHub | vendor docs (厂商研究 一手) — Commando VM Mandiant Windows-based 红队 VM (Windows + 140+ 工具) [declared=surrogate_primary, auto=secondary; reason=vendor docs (厂商研究 一手)] |
| T02-S084 | https://www.maltego.com/ | surrogate_primary | 2026-05-18 | Maltego | vendor docs (工具厂商) — Maltego OSINT graph + transforms + Community Edition 免费 [declared=surrogate_primary, auto=secondary; reason=vendor docs (工具厂商)] |
| T02-S085 | https://github.com/smicallef/spiderfoot | surrogate_primary | 2026-05-18 | Steve Micallef / GitHub | vendor docs (开源工具 一手) — SpiderFoot OSINT 自动化 + 200+ 模块 + SpiderFoot HX SaaS [declared=surrogate_primary, auto=secondary; reason=vendor docs (开源工具 一手)] |
| T02-S086 | https://github.com/laramies/theHarvester | surrogate_primary | 2026-05-18 | Christian Martorella (laramies) / GitHub | vendor docs (开源工具 一手) — theHarvester email + domain + IP + employee 多源 OSINT [declared=surrogate_primary, auto=secondary; reason=vendor docs (开源工具 一手)] |
| T02-S087 | https://www.shodan.io/explore | surrogate_primary | 2026-05-18 | Shodan / John Matherly | vendor docs (工具厂商) — Shodan 互联网设备搜索引擎事实标准 [declared=surrogate_primary, auto=secondary; reason=vendor docs (工具厂商)] |
| T02-S088 | https://search.censys.io/ | surrogate_primary | 2026-05-18 | Censys | vendor docs (工具厂商) — Censys Shodan 替代 + cert transparency + 学术起源 (Michigan U) [declared=surrogate_primary, auto=secondary; reason=vendor docs (工具厂商)] |
| T02-S089 | https://github.com/trufflesecurity/trufflehog | surrogate_primary | 2026-05-18 | Truffle Security / GitHub | vendor docs (开源工具 一手) — TruffleHog secrets scanning (GitHub / GitLab / S3 / Docker / 多源), 800+ detector [declared=surrogate_primary, auto=secondary; reason=vendor docs (开源工具 一手)] |
| T02-S090 | https://github.com/gitleaks/gitleaks | surrogate_primary | 2026-05-18 | Zachary Rice (zricethezav) / GitHub | vendor docs (开源工具 一手) — Gitleaks Git history secrets scan, Go 写 [declared=surrogate_primary, auto=secondary; reason=vendor docs (开源工具 一手)] |
| T02-S091 | https://semgrep.dev/docs/ | surrogate_primary | 2026-05-18 | Semgrep / r2c | vendor docs (工具厂商) — Semgrep OSS + Cloud SAST + 1500+ rule registry, 多语言 [declared=surrogate_primary, auto=secondary; reason=vendor docs (工具厂商)] |
| T02-S092 | https://codeql.github.com/docs/ | surrogate_primary | 2026-05-18 | GitHub Advanced Security | vendor docs (工具厂商) — CodeQL semantic code analysis (GitHub Advanced Security 内置 + free for OSS) [declared=surrogate_primary, auto=secondary; reason=vendor docs (工具厂商)] |
| T02-S093 | https://labs.watchtowr.com/ | surrogate_primary | 2026-05-18 | watchTowr Labs | vendor docs (公司一手) — watchTowr Labs n-day automation + ASM 研究 一手, 2023+ 顶级 nday output [declared=surrogate_primary, auto=secondary; reason=vendor docs (公司一手)] |
| T02-S094 | https://www.assetnote.io/resources | surrogate_primary | 2026-05-18 | Assetnote (Searchlight Cyber 子) | vendor docs (公司一手) — Assetnote n-day + ASM 研究, 现 Searchlight Cyber 旗下 [declared=surrogate_primary, auto=secondary; reason=vendor docs (公司一手)] |
| T02-S095 | https://github.com/AdaptixFramework/AdaptixC2 | surrogate_primary | 2026-05-18 | AdaptixFramework / GitHub | vendor docs (开源工具 一手) — Adaptix C2 modern lightweight OSS, 2024+ Cobalt Strike-like UI [declared=surrogate_primary, auto=secondary; reason=vendor docs (开源工具 一手)] |
| T02-S096 | https://outflank.nl/ | surrogate_primary | 2026-05-18 | Outflank | vendor docs (公司一手) — Outflank C2 (Stage1) 商业 + Outflank Security Tooling OST, 欧洲红队上游 [declared=surrogate_primary, auto=secondary; reason=vendor docs (公司一手)] |
| T02-S097 | https://github.com/netero1010/EDRSilencer | surrogate_primary | 2026-05-18 | netero1010 / GitHub | vendor docs (开源工具 一手) — EDRSilencer Windows Filtering Platform 阻断 EDR 上报 (BYOVD 等), 严授权用 [declared=surrogate_primary, auto=secondary; reason=vendor docs (开源工具 一手)] |
| T02-S098 | https://github.com/wavestone-cdt/EDRSandblast | surrogate_primary | 2026-05-18 | Wavestone CDT / GitHub | vendor docs (开源工具 一手) — EDRSandblast EDR kernel callback / hooks 反向 unhook, 严授权用 [declared=surrogate_primary, auto=secondary; reason=vendor docs (开源工具 一手)] |
| T02-S099 | https://lolbas-project.github.io/ | surrogate_primary | 2026-05-18 | LOLBAS Project / GitHub | vendor docs (开源工具 一手) — LOLBAS Living-Off-The-Land Binaries Scripts Libraries 200+ Windows binaries [declared=surrogate_primary, auto=secondary; reason=vendor docs (开源工具 一手)] |
| T02-S100 | https://gtfobins.github.io/ | surrogate_primary | 2026-05-18 | GTFOBins Project / GitHub | vendor docs (开源工具 一手) — GTFOBins Unix/Linux 380+ 可滥用 binary (find / vi / awk / sudo misconfig) 提权 [declared=surrogate_primary, auto=secondary; reason=vendor docs (开源工具 一手)] |
| T02-S101 | https://github.com/danielmiessler/SecLists | surrogate_primary | 2026-05-18 | Daniel Miessler / GitHub | vendor docs (开源工具 一手) — SecLists wordlist 集合 (username / password / fuzzing / payload) 事实标准 [declared=surrogate_primary, auto=secondary; reason=vendor docs (开源工具 一手)] |
| T02-S102 | https://github.com/swisskyrepo/PayloadsAllTheThings | surrogate_primary | 2026-05-18 | swisskyrepo / GitHub | vendor docs (开源工具 一手) — PayloadsAllTheThings Web 攻击 payload + cheat sheet 知识库 [declared=surrogate_primary, auto=secondary; reason=vendor docs (开源工具 一手)] |
| T02-S103 | https://book.hacktricks.wiki/en/index.html | surrogate_primary | 2026-05-18 | Carlos Polop / HackTricks | vendor docs (作者一手) — HackTricks pentest 知识库 GitBook, 全球 #1 引用 cheat sheet [declared=surrogate_primary, auto=secondary; reason=vendor docs (作者一手)] |
| T02-S104 | https://plextrac.com/platform/ | surrogate_primary | 2026-05-18 | PlexTrac | vendor docs (工具厂商) — PlexTrac commercial pentest reporting + collab + retest 平台 [declared=surrogate_primary, auto=secondary; reason=vendor docs (工具厂商)] |
| T02-S105 | https://dradisframework.com/ | surrogate_primary | 2026-05-18 | Security Roots / Dradis | vendor docs (工具厂商) — Dradis OSS Community + Pro pentest reporting + collaboration [declared=surrogate_primary, auto=secondary; reason=vendor docs (工具厂商)] |
| T02-S106 | https://github.com/SECFORCE/faraday | surrogate_primary | 2026-05-18 | Faraday Security / GitHub | vendor docs (开源工具 一手) — Faraday OSS collaborative pentest IDE + vulnerability manager [declared=surrogate_primary, auto=secondary; reason=vendor docs (开源工具 一手)] |
| T02-S107 | https://vectr.io/ | surrogate_primary | 2026-05-18 | Security Risk Advisors | vendor docs (工具厂商) — VECTR purple team simulation + ATT&CK + detection metrics [declared=surrogate_primary, auto=secondary; reason=vendor docs (工具厂商)] |
| T02-S108 | https://www.exploit-db.com/ | surrogate_primary | 2026-05-18 | OffSec | vendor docs (协会 + 教材) — Exploit Database 50,000+ public PoC + shellcode + Google Hacking Database [declared=surrogate_primary, auto=secondary; reason=vendor docs (协会 + 教材)] |
| T02-S109 | https://www.tenable.com/products/nessus | surrogate_primary | 2026-05-18 | Tenable | vendor docs (工具厂商) — Nessus 商业漏洞扫描事实标准 (Pro + Expert), 70k+ plugin [declared=surrogate_primary, auto=secondary; reason=vendor docs (工具厂商)] |
| T02-S110 | https://greenbone.github.io/docs/latest/ | surrogate_primary | 2026-05-18 | Greenbone | vendor docs (工具厂商) — OpenVAS / Greenbone OSS 漏洞扫描 (Nessus OSS fork 谱系) [declared=surrogate_primary, auto=secondary; reason=vendor docs (工具厂商)] |
| T02-S111 | https://www.hackthebox.com/ | surrogate_primary | 2026-05-18 | Hack The Box | vendor docs (lab syllabus) — HackTheBox labs + Academy CPTS/CBBH/CWEE 认证, 红队 lab 平台 #1 [declared=surrogate_primary, auto=secondary; reason=vendor docs (lab syllabus)] |
| T02-S112 | https://tryhackme.com/ | surrogate_primary | 2026-05-18 | TryHackMe | vendor docs (lab syllabus) — TryHackMe 入门 lab + Path (Pentest+ / Red Team / SOC L1) [declared=surrogate_primary, auto=secondary; reason=vendor docs (lab syllabus)] |
| T02-S113 | https://www.offsec.com/labs/individual/ | surrogate_primary | 2026-05-18 | OffSec | vendor docs (cert org + lab) — OffSec Proving Grounds (PG Practice + PG Play) OSCP 备考 lab [declared=surrogate_primary, auto=secondary; reason=vendor docs (cert org + lab)] |
| T02-S114 | https://github.com/internetwache/CT_subdomains | surrogate_primary | 2026-05-18 | Internet Wache / GitHub | vendor docs (开源工具 一手) — CT subdomains scraping + Certificate Transparency log mining [declared=surrogate_primary, auto=secondary; reason=vendor docs (开源工具 一手)] |
| T02-S115 | https://crt.sh/ | surrogate_primary | 2026-05-18 | Sectigo | vendor docs (协会 + 工具) — crt.sh Certificate Transparency log search 事实标准 [declared=surrogate_primary, auto=secondary; reason=vendor docs (协会 + 工具)] |
| T02-S116 | https://github.com/EnableSecurity/wafw00f | surrogate_primary | 2026-05-18 | Enable Security / GitHub | vendor docs (开源工具 一手) — wafw00f WAF fingerprint + detection [declared=surrogate_primary, auto=secondary; reason=vendor docs (开源工具 一手)] |
| T02-S117 | https://github.com/FortyNorthSecurity/EyeWitness | surrogate_primary | 2026-05-18 | FortyNorth Security (Chris Truncer) / GitHub | vendor docs (开源工具 一手) — EyeWitness 自动 screenshot + report + RDP/VNC/HTTP 多协议 [declared=surrogate_primary, auto=secondary; reason=vendor docs (开源工具 一手)] |
| T02-S118 | https://github.com/x0rz/aquatone | surrogate_primary | 2026-05-18 | Michael Henriksen (x0rz) / GitHub | vendor docs (开源工具 一手) — Aquatone subdomain screenshot + categorization [declared=surrogate_primary, auto=secondary; reason=vendor docs (开源工具 一手)] |
| T02-S119 | https://www.metasploit.com/ | surrogate_primary | 2026-05-18 | Rapid7 | vendor docs (工具厂商) — Metasploit 官方 + Pro 商业版 + Community Edition [declared=surrogate_primary, auto=secondary; reason=vendor docs (工具厂商)] |
| T02-S120 | https://docs.bishopfox.com/ | surrogate_primary | 2026-05-18 | Bishop Fox | vendor docs (公司一手) — Bishop Fox tools docs (Sliver / RustHound / 红队工具集) [declared=surrogate_primary, auto=secondary; reason=vendor docs (公司一手)] |

---

## Tools Inventory

### C2 frameworks (Command & Control)

| tool | category | role | maturity | pricing | os | author/maintainer | reference_source_id |
|---|---|---|---|---|---|---|---|
| Cobalt Strike | C2 | post-ex Beacon + Aggressor Script + Malleable C2 Profile / 商业 SOT 25 年 事实首选 | mature | commercial ($5k+/year per operator; strict Fortra screening) | Windows/Linux beacon | Fortra (originally Raphael Mudge Strategic Cyber LLC) | T02-S001, T02-S002 |
| Sliver | C2 | OSS multi-protocol beacon (mTLS / HTTP(S) / DNS / WireGuard) / Cobalt Strike 现代 OSS 替代 | mature | OSS BSD-3 | Windows/Linux/macOS | Bishop Fox | T02-S003, T02-S004, T02-S120 |
| Mythic | C2 | OSS modular multi-agent (Apollo / Athena / Apfell / Poseidon / Merlin) Docker-based | mature | OSS BSD-3 | Cross-platform | Cody Thomas / SpecterOps | T02-S005 |
| Havoc | C2 | OSS modern community C++ + Demon agent | growing | OSS GPL-2 | Windows beacon / Linux team server | C5pider | T02-S006 |
| Brute Ratel C4 | C2 | commercial advanced OPSEC C2; OEM screening 严格 | mature | commercial (per-operator; strict vetting) | Windows beacon | Chetan Nayak / Dark Vortex | T02-S007 |
| Empire 5.x | C2 | OSS PowerShell + Python C2 (历史 SpecterOps; 现 BC Security 维护) | maintained | OSS BSD-3 | Windows beacon / Linux server | BC Security | T02-S008 |
| PoshC2 | C2 | OSS Python C2 + PowerShell payload | maintained | OSS BSD-3 | Windows beacon / Linux server | Nettitude | T02-S009 |
| Metasploit Framework | C2 / exploitation | OSS 5000+ exploit modules + Meterpreter post-ex shell; 历史 OSS 最大 | mature | OSS BSD-3 + Pro 商业 | Cross-platform | Rapid7 (originally HD Moore) | T02-S010, T02-S011, T02-S119 |
| Covenant | C2 | OSS C# .NET C2 (history, semi-maintained) | legacy | OSS GPL-3 | Windows / Linux | cobbr et al. | n/a (GitHub) |
| Adaptix C2 | C2 | 新兴 OSS modern lightweight C2 (Cobalt Strike-like UI, 2024+) | new | OSS BSD-3 | Cross-platform | AdaptixFramework | T02-S095 |
| Outflank Stage1 | C2 | commercial European 红队 上游 (与 OST 同套) | mature | commercial | Windows beacon | Outflank | T02-S096 |

### AD recon + enum + abuse

| tool | category | role | maturity | pricing | os | author/maintainer | reference_source_id |
|---|---|---|---|---|---|---|---|
| BloodHound CE | AD recon | AD attack path graph (Neo4j-based) / v6+ Community Edition | mature | OSS Apache-2 | Cross-platform | SpecterOps | T02-S013, T02-S014 |
| BloodHound Enterprise | AD recon | SaaS attack path management; 商用持续监控 | mature | commercial SaaS | Cross-platform | SpecterOps | T02-S015 |
| SharpHound | AD recon | C# AD collector for BloodHound | mature | OSS Apache-2 | Windows | SpecterOps | T02-S013 |
| AzureHound | Azure recon | Azure AD / Entra ID collector for BloodHound | mature | OSS Apache-2 | Cross-platform | SpecterOps | T02-S014 |
| PowerView | AD recon | PowerShell AD enumeration (historical PowerSploit 子集) | legacy (signed by EDR) | OSS BSD-3 | Windows | Will Schroeder / SpecterOps | T02-S024 |
| PowerSploit | AD post-ex | PowerShell post-ex toolkit (Invoke-Mimikatz / PowerView / PowerUp) | legacy (signed) | OSS BSD-3 | Windows | PowerShellMafia | T02-S024 |
| Impacket | AD / SMB / NTLM / Kerberos | Python suite (secretsdump / psexec / wmiexec / smbexec / ntlmrelayx / GetUserSPNs / GetNPUsers / dcomexec / addcomputer) 60+ utility | mature | OSS Apache-2 | Cross-platform | Fortra (originally SecureAuth) | T02-S016 |
| NetExec (nxc) | AD lateral | CrackMapExec successor; SMB/WinRM/MSSQL/SSH/RDP/FTP/LDAP/WMI/VNC swiss-army | mature | OSS BSD-3 | Cross-platform | @Pennyw0rth | T02-S017 |
| Responder | network poison | LLMNR/NBT-NS/MDNS poison + NTLM relay capture | mature | OSS GPL-3 | Linux | Laurent Gaffié | T02-S018 |
| Inveigh | network poison | PowerShell/C# Responder 等价物 Windows-side | mature | OSS BSD-3 | Windows | Kevin Robertson | T02-S019 |
| Mimikatz | credential dump | AD 凭据 dump + Pass-the-Hash + Golden/Silver Ticket + DCSync + DCShadow 鼻祖 | mature (signed by all EDR; must self-compile + AMSI bypass) | OSS CC | Windows | Benjamin Delpy (gentilkiwi) | T02-S020 |
| Rubeus | Kerberos abuse | C# Kerberoasting + AS-REP-roasting + S4U + Pass-the-Ticket | mature | OSS BSD-3 | Windows | Will Schroeder / GhostPack | T02-S021 |
| Seatbelt | host enum | C# Windows 安全 enum (host triage + privesc 路径侦察) | mature | OSS BSD-3 | Windows | GhostPack | T02-S022 |
| SafetyKatz | credential dump | Mimikatz 内存版 + AMSI bypass + 反射式加载 | mature | OSS BSD-3 | Windows | GhostPack | T02-S023 |
| pypykatz | credential dump | Python pure-Python Mimikatz 等价物 (LSASS parse) | mature | OSS MIT | Cross-platform | Tamas Jos (skelsec) | T02-S075 |
| Certipy | ADCS abuse | ADCS ESC1-15 abuse 事实标准 Python | mature | OSS MIT | Cross-platform | Oliver Lyak (ly4k) | T02-S025 |
| Coercer | auth coercion | PetitPotam / DFSCoerce / PrinterBug 等 10+ NTLM coerce 方法 | mature | OSS GPL-2 | Cross-platform | Remi Gascou (Podalirius) | T02-S026 |
| ROADtools | Azure recon | Azure AD / Entra ID 红队 enum + abuse (ROADrecon + roadtx) | mature | OSS MIT | Cross-platform | Dirk-jan Mollema | T02-S027 |
| MicroBurst | Azure enum | PowerShell Azure 红队工具集 (subdomain / storage / VM / Function) | mature | OSS BSD-3 | Windows / Cross | NetSPI (Karl Fosaaen) | T02-S028 |
| Stormspotter | Azure graph | Azure attack graph (Microsoft 自家 OSS) | maintained | OSS MIT | Cross-platform | Microsoft | n/a (GitHub) |
| AADInternals | Azure abuse | PowerShell Azure AD / O365 admin abuse | mature | OSS MIT | Windows | Nestori Syynimaa | n/a (GitHub) |
| LdapRelayScan | NTLM relay | LDAP signing + channel binding 检测 + relay 链 | mature | OSS MIT | Cross-platform | zyn3rgy | n/a (GitHub) |

### Web pentest

| tool | category | role | maturity | pricing | os | author/maintainer | reference_source_id |
|---|---|---|---|---|---|---|---|
| Burp Suite Pro | Web proxy | Web 渗透事实标准 + Proxy + Repeater + Intruder + Scanner + Collaborator + extension ecosystem | mature | commercial ($475/year per user; Community Edition 免费阉割) | Cross-platform Java | PortSwigger | T02-S029, T02-S030 |
| Burp Suite Enterprise | Web scanner | Burp SaaS 自动化扫描 + CI/CD | mature | commercial | SaaS | PortSwigger | T02-S029 |
| Caido | Web proxy | Modern Rust-based Burp alternative, 2023+ 快速崛起 | growing | freemium + Pro paid | Cross-platform | Caido Labs | T02-S031 |
| OWASP ZAP | Web proxy | OSS Web proxy + scanner (Burp Community 替代) | mature | OSS Apache-2 | Cross-platform Java | OWASP / SSP | T02-S032 |
| sqlmap | SQLi | SQL injection 事实标准 / 1.8+ MySQL/PostgreSQL/MSSQL/Oracle/SQLite | mature | OSS GPL-2 | Cross-platform Python | Bernardo Damele + Miroslav Stampar | T02-S033 |
| ffuf | Web fuzzer | 现代 Go-based fuzzer (取代 wfuzz / gobuster / dirb) | mature | OSS MIT | Cross-platform | Joohoi | T02-S034 |
| wfuzz | Web fuzzer | Legacy Python fuzzer (history) | legacy | OSS GPL-2 | Cross-platform | xmendez | n/a (GitHub) |
| gobuster | Web fuzzer | Go directory / DNS / vhost brute | mature | OSS Apache-2 | Cross-platform | OJ Reeves | n/a (GitHub) |
| feroxbuster | Web fuzzer | Rust recursive content discovery | mature | OSS MIT | Cross-platform | epi052 | n/a (GitHub) |
| Nuclei | scanner | YAML template-based scanner + 5000+ community templates | mature | OSS MIT | Cross-platform | ProjectDiscovery | T02-S035 |
| subfinder | OSINT | Go-based subdomain enum (cert transparency + 多源 API) | mature | OSS MIT | Cross-platform | ProjectDiscovery | T02-S036 |
| amass | OSINT | OWASP subdomain + asset discovery + graph | mature | OSS Apache-2 | Cross-platform | OWASP / Jeff Foley | T02-S039 |
| chaos | OSINT | ProjectDiscovery subdomain dataset | mature | freemium API | Cross-platform | ProjectDiscovery | n/a (chaos.projectdiscovery.io) |
| Findomain | OSINT | Rust subdomain enum (高速 multi-source) | mature | OSS Apache-2 | Cross-platform | Edu4rdSHL | n/a (GitHub) |
| assetfinder | OSINT | Go subdomain enum simple | mature | OSS MIT | Cross-platform | Tomnomnom | n/a (GitHub) |
| massdns | OSINT | High-perf DNS resolver | mature | OSS GPL-3 | Cross-platform | blechschmidt | n/a (GitHub) |
| httpx | Web probe | Fast HTTP probe (status + title + tech + cert + screenshot) | mature | OSS MIT | Cross-platform | ProjectDiscovery | T02-S037 |
| naabu | port scan | Fast Go port scanner (SYN + CONNECT) | mature | OSS MIT | Cross-platform | ProjectDiscovery | T02-S038 |
| katana | Web crawl | Next-gen Go crawler (headless / JS-aware) | mature | OSS MIT | Cross-platform | ProjectDiscovery | n/a (GitHub) |
| Aquatone | Web screenshot | Subdomain screenshot + categorization | maintained | OSS MIT | Cross-platform | x0rz (Michael Henriksen) | T02-S118 |
| EyeWitness | Web screenshot | Auto screenshot + report + RDP/VNC/HTTP 多协议 | mature | OSS GPL-3 | Cross-platform | FortyNorth Security (Chris Truncer) | T02-S117 |
| wafw00f | recon | WAF fingerprint + detection | mature | OSS BSD-3 | Cross-platform | Enable Security | T02-S116 |
| crt.sh | OSINT | Certificate Transparency log search 事实标准 | mature | free web | SaaS | Sectigo | T02-S115 |

### Burp extensions (high-impact)

| tool | category | role | maturity | pricing | os | author/maintainer | reference_source_id |
|---|---|---|---|---|---|---|---|
| Logger++ | Burp ext | Advanced HTTP request/response logger + filter + colorize | mature | OSS Apache-2 | Burp Java | NCC Group / Soroush Dalili | n/a (BApp Store) |
| Param Miner | Burp ext | Hidden parameter + header discovery (cache poisoning research) | mature | OSS Apache-2 | Burp Java | James Kettle / PortSwigger | n/a (BApp Store) |
| Turbo Intruder | Burp ext | High-perf Intruder alternative (race condition + 100k+ rps) | mature | OSS Apache-2 | Burp Java | James Kettle / PortSwigger | n/a (BApp Store) |
| Autorize | Burp ext | Automated AuthZ test (IDOR / privilege escalation) | mature | OSS MIT | Burp Java | Barak Tawily | n/a (BApp Store) |
| Active Scan++ | Burp ext | Active Scan extension (additional payloads) | mature | OSS MIT | Burp Java | James Kettle / PortSwigger | n/a (BApp Store) |
| Hackvertor | Burp ext | Inline encoding / hashing tag DSL | mature | OSS MIT | Burp Java | Gareth Heyes / PortSwigger | n/a (BApp Store) |
| J2EEScan | Burp ext | Java EE specific vuln scanner | mature | OSS MIT | Burp Java | Federico Dotta | n/a (BApp Store) |

### Mobile

| tool | category | role | maturity | pricing | os | author/maintainer | reference_source_id |
|---|---|---|---|---|---|---|---|
| Frida | mobile instrumentation | iOS / Android / Windows / Linux / macOS 动态 instrumentation 事实标准 | mature | OSS Apache-2 | Cross-platform | Ole André V. Ravnås | T02-S040 |
| Objection | mobile instrumentation | Frida 上层 runtime mobile exploration (无 编程 instrumentation 命令行) | mature | OSS GPL-3 | Cross-platform | Sensepost | T02-S041 |
| Drozer | Android pentest | Android attack surface / IPC / content provider audit | maintained | OSS BSD-3 | Cross-platform | WithSecure (originally MWR) | n/a (GitHub) |
| apktool | Android RE | APK 反编译 + 重打包 | mature | OSS Apache-2 | Cross-platform | Connor Tumbleson (iBotPeaches) | T02-S043 |
| JADX | Android RE | DEX → Java decompiler + GUI | mature | OSS Apache-2 | Cross-platform | skylot | T02-S044 |
| MobSF | mobile audit | Mobile Security Framework, 自动化 Android + iOS 静动态分析 | mature | OSS GPL-3 | Cross-platform | OpenSecurity | T02-S042 |
| Hopper Disassembler | iOS RE | macOS / Linux Mach-O / ELF / PE disassembler + decompiler | mature | commercial ($100+ Personal) | macOS / Linux | Cryptic Apps | n/a (hopperapp.com) |
| adb | Android device | Android Debug Bridge (设备控制 + 文件传输) | mature | OSS Apache-2 (Android SDK) | Cross-platform | Google | n/a (developer.android.com) |
| Magisk | Android root | systemless root + Magisk Hide (Zygisk) | mature | OSS GPL-3 | Android | topjohnwu | n/a (GitHub) |
| KernelSU | Android root | Kernel-based root alternative | growing | OSS GPL-3 | Android | tiann | n/a (GitHub) |
| checkra1n | iOS jailbreak | iOS jailbreak (A11 及更早, checkm8 bootrom exploit) — lab only | mature | OSS / freeware | macOS / Linux | checkra1n team | n/a (checkra.in) |
| palera1n | iOS jailbreak | iOS jailbreak (A11 之前, modern alternative) — lab only | growing | OSS / freeware | macOS / Linux | palera1n team | n/a (palera.in) |

### Cloud

| tool | category | role | maturity | pricing | os | author/maintainer | reference_source_id |
|---|---|---|---|---|---|---|---|
| Pacu | AWS exploitation | AWS exploitation framework + 80+ 攻击模块 | mature | OSS BSD-3 | Cross-platform | Rhino Security Labs (Spencer Gietzen) | T02-S050 |
| Prowler | multi-cloud audit | AWS / GCP / Azure / K8s CSPM + 500+ check (CIS/NIST/PCI/HIPAA/ISO27001) | mature | OSS Apache-2 + ProwlerPro SaaS | Cross-platform | Toni de la Fuente | T02-S051 |
| ScoutSuite | multi-cloud audit | AWS / Azure / GCP / Alibaba / Oracle 安全 audit | mature | OSS GPL-2 | Cross-platform | NCC Group | T02-S052 |
| CloudGoat | AWS lab | AWS 渗透 CTF 训练 lab (Vulnerable-by-Design) | mature | OSS MIT | Cross-platform | Rhino Security Labs | T02-S053 |
| kube-hunter | K8s pentest | K8s 渗透 + attack 模拟 | mature | OSS Apache-2 | Cross-platform | Aqua Security | T02-S054 |
| kube-bench | K8s audit | K8s CIS Benchmark check | mature | OSS Apache-2 | Cross-platform | Aqua Security | n/a (GitHub aquasecurity/kube-bench) |
| Peirates | K8s pentest | K8s pentest (Pod 内运行, escape + lateral) | mature | OSS Apache-2 | Linux | InGuardians | T02-S055 |
| Trivy | container scan | OSS 容器 + IaC + 仓库 + license 扫描, multi-target | mature | OSS Apache-2 | Cross-platform | Aqua Security | T02-S056 |
| Snyk | SAST + SCA | commercial 多语言 SAST + container + IaC + dependency | mature | commercial freemium | Cross-platform | Snyk | n/a (snyk.io) |
| Grype | container scan | OSS Anchore container vuln scan | mature | OSS Apache-2 | Cross-platform | Anchore | n/a (GitHub) |
| G-Scout | GCP audit | GCP security audit (legacy) | maintained | OSS Apache-2 | Cross-platform | Spotify | n/a (GitHub) |
| GCPBucketBrute | GCP enum | GCS bucket enumeration | mature | OSS BSD-3 | Cross-platform | Rhino Security Labs | n/a (GitHub) |

### Binary RE + exploit dev

| tool | category | role | maturity | pricing | os | author/maintainer | reference_source_id |
|---|---|---|---|---|---|---|---|
| IDA Pro | RE | 商业二进制 RE 事实霸主, Hex-Rays decompiler | mature | commercial ($2.5k+ Home / $10k+ Pro per year) | Windows / Linux / macOS | Hex-Rays | T02-S045 |
| Ghidra | RE | NSA OSS RE 框架 + decompiler (IDA Pro 免费替代) | mature | OSS Apache-2 (NSA) | Cross-platform Java | NSA | T02-S046 |
| Binary Ninja | RE | 商业二进制 RE mid-tier 价位 + decompiler + Python API | mature | commercial ($299 Personal / $1500+ Commercial) | Windows / Linux / macOS | Vector 35 | T02-S047 |
| radare2 (r2) | RE | OSS 多平台 RE 框架 + r2 CLI | mature | OSS LGPL-3 | Cross-platform | pancake | T02-S048 |
| Rizin | RE | radare2 friendly fork | mature | OSS LGPL-3 | Cross-platform | Rizin Project | T02-S049 |
| Cutter | RE | Rizin GUI | mature | OSS GPL-3 | Cross-platform | Rizin Project | T02-S049 |
| x64dbg | debugger | OSS Windows x32/x64 debugger | mature | OSS GPL-3 | Windows | mrexodia | n/a (x64dbg.com) |
| WinDbg | debugger | Microsoft Windows kernel + user debugger | mature | free (Microsoft) | Windows | Microsoft | n/a (microsoft.com) |
| gdb | debugger | GNU debugger + pwndbg / GEF / peda 扩展 (Linux exploit dev) | mature | OSS GPL-3 | Linux / Cross | FSF / pwndbg / GEF / peda | n/a |
| frida-trace | RE tracing | Frida runtime trace tool | mature | OSS Apache-2 | Cross-platform | Ole André V. Ravnås | T02-S040 |
| BinDiff | binary diff | binary diffing (now Google free) | mature | free (Google) | Cross-platform | Google (originally zynamics) | n/a (zynamics.com/bindiff) |
| Diaphora | binary diff | OSS IDA Pro binary diffing plugin | mature | OSS AGPL-3 | IDA Pro | Joxean Koret | n/a (GitHub) |
| angr | symbolic exec | Python symbolic execution + binary analysis | mature | OSS BSD-2 | Cross-platform | UCSB / angr team | n/a (angr.io) |
| pwntools | exploit dev | Python CTF + exploit dev 事实库 | mature | OSS MIT | Cross-platform | Gallopsled | n/a (pwntools.com) |
| AFL++ | fuzzing | 现代 AFL fork (state-of-the-art coverage-guided fuzzer) | mature | OSS Apache-2 | Cross-platform | AFLplusplus team | n/a (aflplus.plus) |
| honggfuzz | fuzzing | Google security-focused fuzzer | mature | OSS Apache-2 | Cross-platform | Google (Robert Swiecki) | n/a (GitHub) |
| libFuzzer | fuzzing | LLVM in-process coverage-guided fuzzer | mature | OSS Apache-2 | Cross-platform | LLVM | n/a (llvm.org) |

### Network + scan + capture

| tool | category | role | maturity | pricing | os | author/maintainer | reference_source_id |
|---|---|---|---|---|---|---|---|
| Nmap | port scan | 端口扫描事实标准 26 年+ + NSE 脚本 + zenmap GUI | mature | OSS BSD-style (Nmap Public Source License) | Cross-platform | Gordon Lyon (Fyodor) | T02-S012, T02-S057 |
| masscan | port scan | 高速端口扫描 (整 IPv4 5 分钟) | mature | OSS AGPL-3 | Cross-platform | Robert Graham (Errata Security) | T02-S058 |
| zmap | port scan | 学术高速 Internet-wide scanner | mature | OSS Apache-2 | Linux | ZMap Project / Michigan U | n/a (zmap.io) |
| Wireshark | packet | 协议分析事实标准 + tshark CLI | mature | OSS GPL-2 | Cross-platform | Wireshark Foundation | T02-S059 |
| tcpdump | packet | classic CLI packet capture | mature | OSS BSD | Linux / macOS / BSD | The Tcpdump Group | n/a (tcpdump.org) |
| mitmproxy | proxy | Python interactive HTTPS proxy + scripting | mature | OSS MIT | Cross-platform | Aldo Cortesi | T02-S060 |
| Nessus | vuln scanner | 商业漏洞扫描事实标准 (Pro + Expert), 70k+ plugin | mature | commercial | Cross-platform | Tenable | T02-S109 |
| OpenVAS / GVM | vuln scanner | OSS 漏洞扫描 (Nessus OSS fork 谱系) | mature | OSS GPL-2 | Linux | Greenbone | T02-S110 |

### Wireless / RF

| tool | category | role | maturity | pricing | os | author/maintainer | reference_source_id |
|---|---|---|---|---|---|---|---|
| Aircrack-ng | Wi-Fi | WPA/WPA2/WEP 破解 + airodump + airmon + aireplay | mature | OSS GPL-2 | Linux / Cross | Aircrack-ng team | T02-S061 |
| Wifite | Wi-Fi | 自动化 Wi-Fi 攻击 (Aircrack-ng wrapper) | mature | OSS GPL-2 | Linux | derv82 / kimocoder | n/a (GitHub) |
| airgeddon | Wi-Fi | 全功能 Wi-Fi 审计 + Evil twin + PMKID + WPS | mature | OSS GPL-3 | Linux | v1s1t0r1sh3r3 | n/a (GitHub) |
| bettercap | network MITM | Swiss-army MITM (Wi-Fi + BLE + HID + IPv4/6) | mature | OSS GPL-3 | Cross-platform | evilsocket | n/a (bettercap.org) |
| HackRF One | SDR | wideband software-defined radio (1 MHz - 6 GHz) | mature | commercial (~$340 hardware) | Linux / GNURadio | Great Scott Gadgets | n/a (greatscottgadgets.com) |
| GNURadio | SDR framework | OSS SDR signal processing | mature | OSS GPL-3 | Cross-platform | GNU Radio Project | n/a (gnuradio.org) |

### Password cracking

| tool | category | role | maturity | pricing | os | author/maintainer | reference_source_id |
|---|---|---|---|---|---|---|---|
| hashcat | crack | GPU 密码破解事实标准, 300+ hash 算法 | mature | OSS MIT | Cross-platform | Jens Steube (Atom) | T02-S062 |
| John the Ripper | crack | 经典 OSS 密码破解 + Jumbo edition | mature | OSS GPL-2 + Jumbo BSD | Cross-platform | Openwall | T02-S063 |

### Phishing

| tool | category | role | maturity | pricing | os | author/maintainer | reference_source_id |
|---|---|---|---|---|---|---|---|
| Gophish | phishing campaign | OSS phishing campaign framework, Go 写 | mature | OSS MIT | Cross-platform | Jordan Wright | T02-S064 |
| Evilginx2 | AiTM phishing | AiTM phishing proxy (绕过 2FA + session cookie 捕获) | mature | OSS BSD-3 | Cross-platform | Kuba Gretzky | T02-S065 |
| Modlishka | AiTM phishing | AiTM reverse proxy, Evilginx2 替代品 | mature | OSS BSD-2 | Cross-platform | Piotr Duszyński | T02-S066 |
| EvilGoPhish | phishing combo | Gophish + Evilginx 整合, SMS + email phishing | growing | OSS BSD-3 | Cross-platform | fin3ss3g0d | T02-S067 |
| SET (Social Engineer Toolkit) | phishing | 历史 SET, Dave Kennedy 原作 | legacy | OSS GPL-3 | Linux | TrustedSec | n/a (GitHub) |
| King Phisher | phishing | history phishing campaign (Rapid7, abandoned 2022) | legacy | OSS BSD-3 | Linux | SecureState (history) | n/a (GitHub archived) |

### Physical / RFID / NFC / USB

| tool | category | role | maturity | pricing | os | author/maintainer | reference_source_id |
|---|---|---|---|---|---|---|---|
| Proxmark3 | RFID/NFC | RFID/NFC 读取 + clone + sniff + emulate (LF/HF/UHF) | mature | commercial (~$300 hardware) + OSS firmware | Cross-platform host | RfidResearchGroup | T02-S071 |
| Flipper Zero | multi-RF | Sub-GHz + RFID + NFC + IR + BLE + iButton 多模 toy | mature | commercial (~$170 hardware) + OSS firmware | embedded | Flipper Devices | T02-S072 |
| USB Rubber Ducky | HID injection | USB HID keystroke injection 物理工具 | mature | commercial ($80+ hardware) | Windows / macOS / Linux targets | Hak5 | T02-S068 |
| Bash Bunny | USB attack | multi-vector USB attack platform + payload library | mature | commercial ($120+ hardware) | Cross-target | Hak5 | T02-S069 |
| Wi-Fi Pineapple | rogue AP | rogue AP + Wi-Fi MITM 平台 | mature | commercial ($120+ hardware) | embedded | Hak5 | T02-S070 |
| iCopy-X | badge clone | RFID badge cloner (Proxmark3 alternative) | mature | commercial | embedded | KSEC / iCopy team | n/a |
| ESPKey | badge sniff | Wiegand badge sniffer (HID prox readers) | mature | OSS + DIY hardware | embedded | Eric Evenchick | n/a (GitHub octosavvi/ESPKey) |

### Post-ex utility

| tool | category | role | maturity | pricing | os | author/maintainer | reference_source_id |
|---|---|---|---|---|---|---|---|
| LinPEAS | linux privesc | Linux Privilege Escalation Awesome Script (PEASS-ng) | mature | OSS MIT | Linux | Carlos Polop | T02-S073 |
| WinPEAS | windows privesc | Windows Privilege Escalation Awesome Script (PEASS-ng) | mature | OSS MIT | Windows | Carlos Polop | T02-S073 |
| macPEAS | macOS privesc | macOS Privilege Escalation (PEASS-ng) | mature | OSS MIT | macOS | Carlos Polop | T02-S073 |
| PowerUp | windows privesc | PowerShell Windows privesc enum (PowerSploit 子集) | legacy (signed) | OSS BSD-3 | Windows | Will Schroeder | T02-S024 |
| Mimipenguin | linux cred dump | Linux memory cred dump (Mimikatz-style) | mature | OSS Apache-2 | Linux | huntergregal | n/a (GitHub) |
| LaZagne | cred dump | Cross-platform 凭据 dump (浏览器 / WiFi / 邮件 / 数据库 / SSH) | mature | OSS LGPL-3 | Cross-platform | Alessandro Z | T02-S074 |
| chisel | tunneling | Go fast TCP/UDP tunnel over HTTP/WebSocket | mature | OSS MIT | Cross-platform | Jaime Pillora | T02-S076 |
| Ligolo-ng | tunneling | Modern Go reverse tunneling (TUN interface, 比 chisel 高效) | mature | OSS GPL-3 | Cross-platform | Nicolas Chatelain | T02-S077 |
| gost | tunneling | Go multi-protocol tunnel (HTTP/HTTPS/SOCKS5/Shadowsocks) | mature | OSS MIT | Cross-platform | ginuerzh | n/a (GitHub) |
| ngrok | tunneling | Commercial managed tunnel (lab use; prod 必授权) | mature | freemium SaaS | Cross-platform | ngrok | n/a (ngrok.com) |
| Donut | shellcode loader | PE → shellcode + reflective loader | mature | OSS BSD-3 | Cross-platform | TheWover | n/a (GitHub) |
| sRDI | shellcode loader | shellcode Reflective DLL injection | mature | OSS BSD-3 | Windows | monoxgas | n/a (GitHub) |

### SAST / SCA / secrets

| tool | category | role | maturity | pricing | os | author/maintainer | reference_source_id |
|---|---|---|---|---|---|---|---|
| Semgrep | SAST | OSS + Cloud SAST + 1500+ rule registry, 多语言 | mature | OSS LGPL-2 + Cloud freemium | Cross-platform | Semgrep / r2c | T02-S091 |
| CodeQL | SAST | Semantic code analysis (GitHub Advanced Security 内置 + free for OSS) | mature | free for OSS / commercial via GHAS | Cross-platform | GitHub | T02-S092 |
| SonarQube | SAST | Java/JS/Python/C# SAST + Community/Developer/Enterprise | mature | OSS Community + commercial | Cross-platform | SonarSource | n/a (sonarsource.com) |
| TruffleHog | secrets | Secrets scanning (GitHub / GitLab / S3 / Docker / 多源), 800+ detector | mature | OSS AGPL-3 + Enterprise | Cross-platform | Truffle Security | T02-S089 |
| Gitleaks | secrets | Git history secrets scan, Go 写 | mature | OSS MIT | Cross-platform | Zachary Rice | T02-S090 |
| Gitrob | secrets | history GitHub secrets scan (less maintained) | legacy | OSS MIT | Cross-platform | michenriksen | n/a (GitHub) |

### OSINT

| tool | category | role | maturity | pricing | os | author/maintainer | reference_source_id |
|---|---|---|---|---|---|---|---|
| Maltego | OSINT graph | OSINT graph + transforms + Community Edition 免费 | mature | freemium + commercial | Cross-platform | Maltego Technologies | T02-S084 |
| SpiderFoot | OSINT auto | OSINT 自动化 + 200+ 模块 + SpiderFoot HX SaaS | mature | OSS MIT + HX SaaS | Cross-platform | Steve Micallef | T02-S085 |
| theHarvester | OSINT | email + domain + IP + employee 多源 OSINT | mature | OSS GPL-2 | Cross-platform | Christian Martorella | T02-S086 |
| Recon-ng | OSINT | Modular Python recon framework | mature | OSS GPL-3 | Cross-platform | Tim Tomes (LaNMaSteR53) | n/a (GitHub) |
| Shodan | search engine | 互联网设备搜索引擎事实标准 | mature | freemium ($69+ Membership lifetime sale) | SaaS / API | John Matherly | T02-S087 |
| Censys | search engine | Shodan 替代 + cert transparency + 学术起源 Michigan U | mature | freemium API + Enterprise | SaaS / API | Censys | T02-S088 |
| FOFA | search engine | 中国 互联网资产搜索引擎 (白帽汇) | mature | freemium API | SaaS / API | BAIMAOHUI | n/a (fofa.info) |
| Hunter | OSINT | Email finder / verifier | mature | freemium SaaS | SaaS / API | Hunter | n/a (hunter.io) |
| ZoomEye | search engine | 知道创宇 中国 互联网资产搜索 | mature | freemium API | SaaS / API | Knownsec | n/a (zoomeye.org) |
| Quake | search engine | 360 Quake 互联网资产搜索 (中国) | mature | freemium API | SaaS / API | Qihoo 360 | n/a (quake.360.cn) |
| waybackurls | OSINT | Wayback Machine URL scraper | mature | OSS MIT | Cross-platform | Tomnomnom | n/a (GitHub) |
| GauPlus | OSINT | URL collection from multiple sources (Gau fork) | mature | OSS MIT | Cross-platform | bp0lr | n/a (GitHub) |
| holehe | username enum | Email used on services check | mature | OSS GPL-3 | Cross-platform | megadose | n/a (GitHub) |
| sherlock | username enum | Username enumeration across 300+ social platforms | mature | OSS MIT | Cross-platform | Sherlock Project | n/a (GitHub) |
| Trace Labs OSINT VM | OSINT distro | Specialized OSINT Linux distro (Trace Labs CTF) | mature | free | Linux | Trace Labs | n/a (tracelabs.org) |

### Reporting + collab

| tool | category | role | maturity | pricing | os | author/maintainer | reference_source_id |
|---|---|---|---|---|---|---|---|
| PlexTrac | reporting | commercial pentest reporting + collab + retest 平台 | mature | commercial | SaaS | PlexTrac | T02-S104 |
| Dradis | reporting | OSS Community + Pro pentest reporting + collaboration | mature | OSS GPL-2 + Pro | Cross-platform | Security Roots | T02-S105 |
| Faraday | reporting | OSS collaborative pentest IDE + vulnerability manager | mature | OSS GPL-3 + Pro | Cross-platform | Faraday Security | T02-S106 |
| VECTR | purple team | Purple team simulation + ATT&CK + detection metrics | mature | OSS Community + commercial | Cross-platform | Security Risk Advisors | T02-S107 |
| Atomic Red Team | purple team | ATT&CK 测试库 (TTP 复现 + detection 验证) | mature | OSS MIT | Cross-platform | Red Canary | T02-S078 |
| CALDERA | purple team | MITRE 自动化对手模拟 + plugin (Stockpile + Sandcat agent) | mature | OSS Apache-2 | Cross-platform | MITRE Corporation | T02-S079 |

### OS for red team

| tool | category | role | maturity | pricing | os | author/maintainer | reference_source_id |
|---|---|---|---|---|---|---|---|
| Kali Linux | distro | 红队事实主流 OS, OffSec 维护 + 600+ 预装工具 | mature | free Debian-based | Linux | OffSec | T02-S080 |
| Parrot OS | distro | Kali 替代 Linux distro, 隐私 + 渗透 + 加密 | mature | free Debian-based | Linux | Parrot Security | T02-S081 |
| BlackArch | distro | Arch-based rolling 红队 distro, 2700+ 工具 | mature | free Arch-based | Linux | BlackArch Linux | T02-S082 |
| Athena OS | distro | Arch-based newer 红队 distro (gaming-grade UX) | growing | free Arch-based | Linux | Athena OS | n/a (athenaos.org) |
| Commando VM | distro | Mandiant Windows-based 红队 VM (Windows + 140+ 工具) | mature | free Windows | Windows | Mandiant | T02-S083 |

### Knowledge / cheat sheet / wordlists

| tool | category | role | maturity | pricing | os | author/maintainer | reference_source_id |
|---|---|---|---|---|---|---|---|
| SecLists | wordlists | wordlist 集合 (username / password / fuzzing / payload) 事实标准 | mature | OSS MIT | Cross-platform | Daniel Miessler | T02-S101 |
| PayloadsAllTheThings | payload library | Web 攻击 payload + cheat sheet 知识库 | mature | OSS MIT | Cross-platform | swisskyrepo | T02-S102 |
| HackTricks | knowledge | pentest 知识库 GitBook, 全球 #1 引用 cheat sheet | mature | OSS free | Cross-platform | Carlos Polop | T02-S103 |
| LOLBAS | knowledge | Living-Off-The-Land Binaries Scripts Libraries 200+ Windows binaries | mature | OSS MIT | Cross-platform | LOLBAS Project | T02-S099 |
| GTFOBins | knowledge | Unix/Linux 380+ 可滥用 binary (find / vi / awk / sudo misconfig) 提权 | mature | OSS GPL-3 | Cross-platform | GTFOBins Project | T02-S100 |
| Exploit-DB | exploit DB | 50,000+ public PoC + shellcode + Google Hacking Database | mature | OSS / free | Web + Searchsploit CLI | OffSec | T02-S108 |

### Learning labs

| tool | category | role | maturity | pricing | os | author/maintainer | reference_source_id |
|---|---|---|---|---|---|---|---|
| HackTheBox | lab | HTB labs + Academy CPTS/CBBH/CWEE 认证, 红队 lab 平台 #1 | mature | freemium + VIP $14/month + Academy | SaaS / VPN | HackTheBox | T02-S111 |
| TryHackMe | lab | 入门 lab + Path (Pentest+ / Red Team / SOC L1) | mature | freemium $10/month | SaaS / browser | TryHackMe | T02-S112 |
| OffSec Proving Grounds | lab | OffSec PG Practice + PG Play OSCP 备考 lab | mature | $19/month subscription | SaaS / VPN | OffSec | T02-S113 |
| PentesterLab | lab | Web 漏洞专项 lab 集合 (反序列化 / JWT / Code Review / API / Auth) | mature | $30/month subscription | SaaS / browser | Louis Nyffenegger | n/a (pentesterlab.com) |
| PortSwigger Web Academy | lab | 免费 240+ Web lab 事实 syllabus | mature | free | SaaS / browser | PortSwigger | n/a (portswigger.net/web-security) |
| VulnHub | lab | Free downloadable VM challenges (legacy 主) | mature | free | VM download | VulnHub | n/a (vulnhub.com) |
| HackerOne | bug bounty | Bug bounty 平台 + Hacktivity public reports | mature | freemium platform | SaaS | HackerOne | n/a (hackerone.com) |
| Bugcrowd | bug bounty | Bug bounty 平台 + CrowdStream feed | mature | freemium platform | SaaS | Bugcrowd | n/a (bugcrowd.com) |
| Intigriti | bug bounty | EU-based bug bounty platform | mature | freemium platform | SaaS | Intigriti | n/a (intigriti.com) |

### 新兴 (近 12 个月) + EDR bypass research (严授权用)

| tool | category | role | maturity | pricing | os | author/maintainer | reference_source_id |
|---|---|---|---|---|---|---|---|
| watchTowr Labs research | n-day | n-day automation + ASM 研究 一手 (2023+ 顶级 nday output) | growing | research blog / commercial | SaaS / research | watchTowr | T02-S093 |
| Assetnote / Searchlight | n-day | n-day + ASM 研究 (Searchlight Cyber 子) | mature | research blog / commercial | SaaS / research | Assetnote / Searchlight | T02-S094 |
| Adaptix C2 | C2 | 新兴 OSS modern lightweight C2 (Cobalt Strike-like UI, 2024+) | new | OSS BSD-3 | Cross-platform | AdaptixFramework | T02-S095 |
| EDRSilencer | EDR research | Windows Filtering Platform 阻断 EDR 上报 (BYOVD 等), 严授权用 | growing | OSS MIT | Windows | netero1010 | T02-S097 |
| EDRSandblast | EDR research | EDR kernel callback / hooks 反向 unhook, 严授权用 | mature | OSS Apache-2 | Windows | Wavestone CDT | T02-S098 |
| Hells Gate / Halos Gate / Tartarus Gate | EDR research | Direct syscall evolution (绕 EDR userland hook) | research / OSS | OSS | Windows | am0nsec / RtlDDoS / trickster0 | n/a (multiple GitHub PoC) |
| Outflank OST | red team SaaS | Outflank Security Tooling (Stage1 + tooling), 欧洲红队上游 | mature | commercial subscription | Windows beacon | Outflank | T02-S096 |
| ContiOps / RansomwareTracker | OPSEC research | Leaked ransomware ops manual (反向 hunt 学习 OPSEC) | research / public archive | free archive | research | various researchers | n/a (Twitter / GitHub mirrors) |
| BloodHound CE v6+ | AD recon | 2023 split + 持续 community release, 现 BHCE | mature | OSS Apache-2 | Cross-platform | SpecterOps | T02-S013, T02-S014 |
| MAESTRO | Azure recon | Microsoft Entra 红队 attack path (新兴 2024+) | new | OSS | Cross-platform | Roberto Rodriguez (Cyb3rWard0g) | n/a (GitHub) |
| Sliver-Implant Mod | C2 | community-developed Sliver modules / OPSEC profile | growing | OSS | Cross-platform | community | T02-S004 |

---

## 工具选型决策树

红队工具选型的 6-7 个常见决策场景 — 每个决策点都涉及 license / OPSEC / 客户 ROE / 法律 / 团队 trust 5 个维度的交叉, 没有 "single best" 答案, 只有 "for this engagement, given these constraints" 的最优解.

### 决策 1: C2 框架选型 (engagement 启动第一天最大决策)

```
客户预算 + 严肃 engagement?
├── YES (大型企业 / 金融 / 政府 / 50k+ engagement budget)
│   └── 客户接受 Fortra license + Fortra background check 通过?
│       ├── YES → Cobalt Strike (CS) + Malleable C2 Profile 调优 + 商业 EULA 法律保障
│       └── NO (Fortra 拒绝 / 个人 researcher / 制裁国地理 / vetting 拒)
│           └── 客户接受 Brute Ratel + Dark Vortex vetting?
│               ├── YES → Brute Ratel C4 (OPSEC 最顶级商业替代)
│               └── NO → Sliver (OSS) + 自调 sleep/jitter/profile + 自接 redirector
└── NO (内部 / lab / 教学 / 小型 engagement)
    ├── 现代 modular 多 agent 需求? → Mythic (Apollo + Athena agent)
    ├── 简单跨平台 OSS? → Sliver
    ├── 新颖 community OSS (尝鲜)? → Havoc / Adaptix C2 (2024+)
    └── PowerShell + AD 教学 demo? → Empire 5.x (BC Security 维护)

避坑: 不要用 cracked Cobalt Strike — OPSEC burn 100% + 法律风险 (Fortra 主动追查) + 客户检测能力高 (CS 默认 binary 已 fingerprint to death)
```

### 决策 2: Web pentest proxy 选型

```
预算 + 团队习惯?
├── 商业 ($475/year per user OK) → Burp Suite Pro + 高价值 extension (Logger++ / Param Miner / Turbo Intruder / Autorize)
├── 免费 必须 + Burp 习惯 → Burp Suite Community (Repeater + Proxy + 基础 Intruder, 无 Active Scan + 无 Collaborator + 无 extension API limited)
├── 想尝鲜 modern Rust performance → Caido (2023+ 兴起, 已可日常使用)
└── 大规模 SaaS 自动化扫描 CI/CD → Burp Suite Enterprise (DAST automation) 或 OWASP ZAP (OSS DAST CI)

避坑: Burp Pro 拿到就开 Active Scan 而不调 scope = 测产品域名 越界 ROE → 客户投诉
```

### 决策 3: AD enumeration 工具 (内网 engagement 首日)

```
有 valid domain user 凭据?
├── YES → SharpHound (C# native, 隐蔽) + AzureHound (如混合 Azure AD) → BloodHound CE GUI 分析 attack path → Rubeus (Kerberoasting / AS-REP-roasting) + Certipy (ADCS 检查)
├── NO (假设 zero-cred, 物理 / 网络 access only) → Responder (LLMNR/NBT-NS poison capture NTLMv1/v2 hash) → hashcat crack OR impacket-ntlmrelayx (relay 直接 lateral) → Coercer (PetitPotam / DFSCoerce trigger)
└── EDR 严控不能跑 SharpHound? → ldapsearch + adidnsdump + 手动 BloodHound JSON (ingest 后台分析)

避坑: SharpHound default profile = noisy (查所有 collection method), 必须 -CollectionMethod minimal 或 stealth 减 noise
```

### 决策 4: Mobile 平台选型

```
平台?
├── Android
│   ├── 静态 RE → JADX (DEX → Java decompiler) + apktool (resource + smali)
│   ├── 动态 instrumentation → Frida (root or no-root) + Objection (无编程 CLI)
│   ├── 自动化全套 → MobSF (Static + Dynamic + API)
│   └── IPC / content provider 审计 → Drozer
└── iOS
    ├── 越狱设备 (lab only) → checkra1n (A11-) / palera1n (modern) → Frida + Objection + cycript
    ├── 不越狱 → Frida-iOS-Dump + IPA 静态 RE
    └── 二进制 → Hopper Disassembler (Mach-O 商业 mid-tier) / Ghidra (免费) / IDA Pro (商业 high-tier)

避坑: SSL pinning 不绕 = 抓不到 HTTPS, 必须 Frida script (objection ios sslpinning disable / android sslpinning disable) 或 frida-ios-dump
```

### 决策 5: Cloud 平台选型

```
云?
├── AWS → Pacu (exploitation modules) + Prowler (CSPM audit) + ScoutSuite (multi-cloud audit) + CloudGoat (lab 训练)
├── Azure → AzureHound + ROADtools (Entra ID) + MicroBurst (PowerShell modules) + Stormspotter (graph) + AADInternals
├── GCP → ScoutSuite + GCPBucketBrute (Bucket enum) + custom IAM scripts
├── K8s → kube-hunter (attack 模拟) + kube-bench (CIS check) + Peirates (Pod 内 escape + lateral) + Trivy (container scan)
└── Multi-cloud audit → Prowler (覆盖 AWS+Azure+GCP+K8s 500+ check)

避坑: 云 enum 必须 限速 + 用客户提供 IAM credential (不要 stuff 公开 leaked creds) + 严守 stay-in-scope (账号 ID 白名单)
```

### 决策 6: Binary RE 工具

```
预算 + 平台?
├── 商业 high-tier 预算 ($2.5k+ Home / $10k+ Pro per year) → IDA Pro + Hex-Rays decompiler (事实霸主)
├── 商业 mid-tier ($299 Personal) → Binary Ninja (Vector 35, Python API + 现代 UI)
├── 免费高质量 → Ghidra (NSA OSS, IDA Pro 最强免费替代 + 内置 decompiler)
├── 命令行 + 脚本 → radare2 / Rizin + Cutter GUI
└── 调试器 → Windows: x64dbg + WinDbg / Linux: gdb + pwndbg / GEF / peda

避坑: Ghidra 默认 Java 内存 1.5G, 分析大 binary 必须改启动脚本 MAXMEM, 否则 OOM
```

### 决策 7: 法律地域 + 客户合规约束

```
engagement 地域?
├── US → CFAA 18 USC 1030 严守 + engagement letter + ROE + SOW 三件套必须
├── UK → CMA 1990 严守 + CHECK / CREST 认证体系 + NCSC guidance
├── EU → GDPR (客户 PII 处理 严限) + TIBER-EU (金融 红队 框架)
├── 中国 → 网络安全法 27 + 数据安全法 + 刑法 285/286 (比 US 更宽) + 等保备案 + 公安部 / 网信办 报备 + 资质渗透公司协作 (中国信安测评中心 / 公安部第三研究所 / 启明星辰 / 绿盟 / 奇安信 / 360 / 深信服 / 安恒) + 客户数据严禁离境
└── 其他 → 当地律师 review + 教训 engagement: 不熟悉地区 不接 engagement

避坑: 自带 Wi-Fi / SDR / RFID hardware 出差 没 OFAC export check (国家受限设备出境) = 法律风险, 高敏感 hardware 当地租赁 / 邮寄
```

---

## 避坑清单

红队新人 / 中级 operator 工具选型常犯的 10 个错, 每条都源于业内反复出现的 engagement 翻车 / 法律纠纷 / OPSEC burn / 报告被拒案例.

1. **OSCP 备考时只用 Metasploit 简化版** — OSCP 考场限 1 次 Metasploit 使用 (auxiliary + multi-handler 不算), 必须熟悉手动 exploit + 手动 shellcode + 手动 priv esc. 备考阶段只刷 HTB easy box 走 Metasploit autopwn 路径 = 真考砸. 正解: HTB Academy CPTS path + OffSec PG Practice + 手动 sql injection + 手动 buffer overflow (虽然 PEN-200 2023 改版去掉 BOF, 仍建议练).

2. **把 Cobalt Strike 当默认 C2 但 license 拿不到** — Fortra 自 2020 收购后 license 严格 (不卖个人 + 不卖制裁国地理 + 强制 background check), 单 operator $5k+/year. 公开 cracked CS 用 = OPSEC 100% burn (cracked binary 已 fingerprint 到所有 EDR) + 法律双重风险 (Fortra 主动追查 + 客户检测后投诉). 正解: 单人 / 小团队 选 Sliver / Mythic OSS, 大团队 + 严肃 engagement 走正规 Fortra 流程.

3. **Sliver 想替代 Cobalt Strike 但 OPSEC 默认设置 = 不够隐蔽** — Sliver default beacon profile (固定 user-agent + 固定 sleep + 固定 jitter + 默认 HTTPS routes) 已被各 EDR signature, 不调直接上 production = 立即 detect. 必须 tune: custom HTTPS profile + sleep mask (Ekko / Foliage encryption) + jitter % 调高 + redirector + Domain fronting (如客户接受) + 自编译加 obfuscation flags.

4. **PowerView / PowerSploit 在现代 EDR 几乎都被签名** — 2014-2018 的 PowerShell 红队工具 (PowerView / Invoke-Mimikatz / Get-NetUser) 现在 Defender + CrowdStrike + SentinelOne 默认 signature 拦截 + AMSI 上报. 直接 IEX (New-Object Net.WebClient).DownloadString("...PowerView.ps1") = 秒被杀. 正解: AMSI bypass (patching amsi.dll 或 String.Replace) + Invoke-Obfuscation + 内存 only loading + 改 Cmdlet 名 + 反射式加载.

5. **直接用 GitHub release 的 Mimikatz 二进制 = 99% trip on Defender / EDR** — gentilkiwi 仓库 release binary 已被全 EDR signature 到死. 正解: 自编译 (MinGW + 改 build string + 改 export name) + 加壳 (UPX 注意签名也被识) + 用 SafetyKatz (反射式 Mimikatz, Donut 加载 to memory) + pypykatz (Python 重写 LSASS parser, 不调 Mimikatz binary).

6. **NetExec / CrackMapExec 默认 SMB scan = noisy, Tier 1 EDR 都报警** — `nxc smb 10.0.0.0/24` default 触发大量 SMB Null Session enum, EDR 立即报警 "Suspicious SMB enumeration from host X". 正解: 限速 (--threads 1 --jitter 5) + 限范围 (针对性 host list 而非 /24 sweep) + 用 valid credential (不要 null session) + 与客户 SOC 沟通预报告 (purple team 模式).

7. **不熟悉 ATT&CK 就开始 engagement = 报告没法 mapping, 客户 detection team 无法 verify** — 客户 (尤其大型企业) 现在要求 red team 报告必须每个 finding 映射 MITRE ATT&CK T 编号 (T1059.001 PowerShell / T1003.001 LSASS Memory / T1078 Valid Accounts 等). 没 mapping 的报告会被 detection engineering team 退回. 正解: 熟读 ATT&CK Enterprise v15+ + 在 engagement timeline 实时记录 (Joplin / Obsidian / Notion 模板) + 报告生成时 Atomic Red Team / VECTR 辅助 mapping.

8. **Burp Pro 拿到就开始 Active Scan 而不调 scope = 风险测产品域名 ROE 越界** — Burp Suite Pro Active Scan 默认 in-scope 是 当前 URL host, 如果 SSO 跨域 redirect (login.example.com → app.example.com → api.example.com), Active Scan 会爬到 ROE 外的 host. 正解: engagement 启动后 第一件事 = Settings → Scope → 严格白名单 IP + 域名, 任何 Scope 外 host 自动 drop, 不发包.

9. **自带 Wi-Fi / SDR / RFID hardware 出差 没 OFAC export check = 国家受限设备出境法律风险** — HackRF One + Wi-Fi Pineapple + Proxmark3 + Flipper Zero + Bash Bunny 在某些国家入境 = "dual-use technology" 海关扣留 + 罚款 + 个人记录. 美国 OFAC EAR (Export Administration Regulations) ECCN 5A002 / 5D002 涉及 cryptographic / surveillance gear. 正解: 高敏感 hardware 当地租赁 / 邮寄 (UPS / FedEx ARRC 服务) + engagement 前 公司法务 + customs broker review.

10. **物理 engagement 没 emergency contact + safe word + get-out-of-jail-free letter = 触警报后无法证明授权, 警察当场 detain** — 物理 / 社工 engagement (badge cloning / tailgating / lockpicking / drop attack) 触发客户安保系统报警, 第一线响应是 物业 / 警察 / 安保 force, 他们不知道 engagement 存在. 正解: engagement letter 必须 含 (a) 客户高管 24/7 emergency contact 电话, (b) safe word / phrase (operator 当场说出, 物业/警察 verify with 客户), (c) get-out-of-jail-free letter (printed PDF + sealed, operator 随身, 含 客户 CEO/CISO 签名 + 律师 contact + 警察 hotline), (d) 物理 engagement 前 24h 客户安保团队预告 (允许 watch but not respond 模式).
