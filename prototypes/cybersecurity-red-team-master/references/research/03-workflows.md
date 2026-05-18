# Track 03 — Workflows / SOP / Pipeline: Cybersecurity Red Team (Offensive Security Operations)

Cybersecurity red team 的 engagement lifecycle 在业内已经被 PTES (Penetration Testing Execution Standard) + OSSTMM 3 + NIST SP 800-115 + MITRE ATT&CK + Cyber Kill Chain + Unified Kill Chain 六大方法论框架反复打磨, 现代 mature 红队的 SOP 大致沿 **KO (kick-off) meeting → scoping + ROE 签字 → 法律 + 律师 review → safe word + emergency contact → recon (passive OSINT + active enum) → initial access (phishing / 外网 web exploit / 物理 / supply chain) → C2 established + beacon → post-ex (priv esc + lateral + AD owns / cloud takeover) → exfil simulation (without 真实泄漏) → persistence (有时不要) → reporting (executive + technical + ATT&CK + 整改 + retest plan) → retest (verify fixes)** 这条 17-22 步主轴展开. 每一阶段都有对应的 ATT&CK tactic 映射 (TA0043 Recon → TA0001 Initial Access → TA0011 C2 → TA0010 Exfil), 资深红队人员通常用 ATT&CK ID 作为 engagement note 与 report 的标签系统, 让 detection engineer + blue team 在 retest / purple team 复盘时可以 1:1 map.

不同 engagement 类型 SOP 差异很大. **外网渗透 (External Network)** 起点是 在网域名 + IP CIDR + SaaS 资产清单, 重点 OSINT + Shodan + Censys + nuclei + 边界服务 (VPN + Citrix + Exchange + RDWeb) exploit; **内网 AD 渗透 (Internal AD)** 假设 assume breach 起点是 plant box 拿到 Domain User 账号, 主轴是 BloodHound attack path + Kerberoasting + ADCS ESC1-15 + NTLM 中继到 DA; **Web 应用渗透** 走 OWASP WSTG v4.2 的 12 大测试域 checklist + Burp Suite Pro 工作流; **移动 (iOS/Android)** 走 OWASP MASTG 的静态 + 动态 + 网络三层 + Frida instrumentation; **云渗透 (AWS/Azure/GCP)** 起点是 leaked credentials / S3 公开桶 / GitHub secrets, 主轴是 IAM enum (Pacu + ScoutSuite + AzureHound) + 攻击路径分析 + STS chain + serverless escape; **物理 + 社工** 是 badge clone (Proxmark3 + Flipper Zero) + tailgating + pretexting + USB drop; **紫队 / adversary emulation** 是 选定 APT actor (FIN7 / APT29 / Scattered Spider) 提取 TTPs, 用 Atomic Red Team + CALDERA + Scythe + Vectr 与 SOC + detection engineer 共同 run 评估检测覆盖率; **bug bounty** 是 程序 (HackerOne / Bugcrowd / Intigriti / YesWeHack) 长尾资产 monitoring + change detection + impact-driven report; **TIBER-EU + CBEST 监管型** 是 欧洲金融监管 + 英国央行驱动的 Threat Intelligence-based Ethical Red-Teaming, 流程更长 (6-12 个月) + 必须 threat intel provider + red team provider 分离 + 监管观察员全程在场.

入门 (junior, 1-3 年 / OSCP / CRTP / GPEN 持证) 与 资深 (senior, 5+ 年 / OSEP + CRTL + GXPN 持证 + 多 engagement lead) 在 SOP 走法上有 系统性 分歧. 入门倾向于 严守 checklist (PTES 7 阶段 / WSTG 12 域 / MASTG / ATT&CK 全 14 tactic), 工具默认 (Nessus + Burp Active Scan + nuclei full template + ScoutSuite full audit), payload 默认 (msfvenom / SET default templates), C2 默认 profile (Cobalt Strike 默认 malleable profile 不改), 报告 finding-by-finding 列. 资深则系统性 优化 + 跳过 + 添加 — **跳过** 那些低 ROI / 高 risk / 客户已知的步骤 (例如跳过 default scope 全量扫描, 跳过 KO 重复 scope 确认, 跳过 default C2 profile 暴露指纹), **优化** 工具链 (parallelization + 自定义 fork + in-memory 替代 disk write + per-engagement bespoke C2 profile), **额外** 做 入门 SOP 不涵盖的高级动作 (supply chain check / ADCS ESC9-13 / device code phishing / BOF inline / detection engineering 反馈 / chain low-medium findings 成 critical).

法律 + 道德 + OPSEC 三条 anchor 贯穿全程, 不可妥协. **法律 anchor** = engagement letter + signed SOW + ROE 三件套 + 律师 review (US CFAA 18 USC 1030 / UK CMA 1990 / 中国 刑法 285+286 + 网络安全法 27 + 数据安全法; 越界 = 重罪即使无意); **道德 anchor** = stay in scope + reporting 优先 weaponization (找到 critical 不立即 exploit, 先评估业务影响 + 沟通客户是否继续) + 不收集 PII 超出必要 + 测试后清理 (artifacts + persistence + 测试账号); **OPSEC anchor** = 攻击 infrastructure 隔离 (不复用 IP / 域名 / cert) + traffic encryption (TLS + DNS over HTTPS + 域 fronting) + payload 一次性 (不复用 stager) + C2 profile per-engagement 自定义 + log 加密保管 + retest 之后 archive. 这三条 anchor 在每个 SOP subsection 的 **OPSEC 注意** 列项中以工程级动作落地, 不是抽象口号.

最后, 红队 SOP 永远是 lifecycle 闭环 — engagement 结束不是 report 交付而是 **retest + remediation verification + 复盘 workshop**, 资深红队人员会主动把 detection guidance (Sigma rule + KQL hunting query + Splunk SPL + Suricata signature) 写在 report 附录, 与 detection engineering team 一起把 finding 转化为 detection content, 这是 红队从 'one-shot pentest 服务' 升级为 'continuous security validation partner' 的核心动作.

## Source Manifest

| source_id | url | bucket | last_checked | author/host | one-line note |
|---|---|---|---|---|---|
| T03-S001 | http://www.pentest-standard.org/index.php/PTES_Technical_Guidelines | surrogate_primary | 2026-05-18 | PTES Team pentest-standard.org | PTES Technical Guidelines — 完整 7-phase 渗透方法论 + 工具映射, engagement lifecycle 业内事实标准 [declared=surrogate_primary, auto=secondary; reason=vendor docs (协会)] |
| T03-S002 | http://www.pentest-standard.org/index.php/Pre-engagement | surrogate_primary | 2026-05-18 | PTES Team pentest-standard.org | PTES Pre-engagement Interactions — Scoping / Goals / Authorization / Engagement Letter / Specify Start End Dates / IP ranges / Out of Scope / 三件套模板 [declared=surrogate_primary, auto=secondary; reason=vendor docs (协会)] |
| T03-S003 | https://www.isecom.org/OSSTMM.3.pdf | surrogate_primary | 2026-05-18 | ISECOM isecom.org | OSSTMM 3 — Pete Herzog 主编, Rules of Engagement + RAV scoring + 10 channel 测试 (Human / Physical / Wireless / Telecomm / Data Network) [declared=surrogate_primary, auto=secondary; reason=vendor docs (协会)] |
| T03-S004 | https://csrc.nist.gov/pubs/sp/800/115/final | verified_primary | 2026-05-18 | NIST csrc.nist.gov | NIST SP 800-115 Technical Guide to Information Security Testing and Assessment — 4 phase (Planning / Discovery / Attack / Reporting) + Rules of Engagement 模板 |
| T03-S005 | https://attack.mitre.org/ | surrogate_primary | 2026-05-18 | MITRE Corporation attack.mitre.org | MITRE ATT&CK Enterprise v14+ — 14 战术 600+ 技术 engagement note + report 标签事实标准 [declared=surrogate_primary, auto=secondary; reason=vendor docs (协会 + 教材)] |
| T03-S006 | https://attack.mitre.org/resources/engage-with-attack/get-started/ | surrogate_primary | 2026-05-18 | MITRE Corporation attack.mitre.org | ATT&CK Getting Started — 如何在 engagement 中以 ATT&CK 标签结构化记录 TTPs + 与 detection engineer 1:1 map [declared=surrogate_primary, auto=secondary; reason=vendor docs (协会)] |
| T03-S007 | https://owasp.org/www-project-web-security-testing-guide/v42/ | surrogate_primary | 2026-05-18 | OWASP WSTG Project owasp.org | OWASP WSTG v4.2 — 12 测试域 (Info Gather / Config / Identity / Authn / Authz / Session / Input / Error / Crypto / Business Logic / Client / API) Web 渗透事实 SOP [declared=surrogate_primary, auto=secondary; reason=vendor docs (协会 教材)] |
| T03-S008 | https://mastg.owasp.org/ | surrogate_primary | 2026-05-18 | OWASP MASTG Project mastg.owasp.org | OWASP MASTG (Mobile App Security Testing Guide) v1.7+ — iOS + Android 静态 + 动态 + 网络 + 反制 三层方法学 [declared=surrogate_primary, auto=secondary; reason=vendor docs (协会 教材)] |
| T03-S009 | https://posts.specterops.io/red-team-engagement-process-92e833ce1abb | surrogate_primary | 2026-05-18 | SpecterOps Team posts.specterops.io | SpecterOps — Red Team Engagement Process, 从 scoping → reporting 完整 SOP + lessons learned [declared=surrogate_primary, auto=secondary; reason=vendor docs (作者一手 公司)] |
| T03-S010 | https://specterops.io/wp-content/uploads/sites/3/2022/03/Certified_Pre-Owned.pdf | surrogate_primary | 2026-05-18 | Will Schroeder / Lee Christensen / SpecterOps | Certified Pre-Owned: Abusing Active Directory Certificate Services (2021) — ADCS ESC1-8 一手 whitepaper, 后续 ESC9-15 在 blog post 增补 [declared=surrogate_primary, auto=secondary; reason=vendor docs (作者一手 公司)] |
| T03-S011 | https://posts.specterops.io/adcs-esc13-abuse-technique-fda4272fbd53 | surrogate_primary | 2026-05-18 | Jonas Bülow Knudsen / SpecterOps | ADCS ESC13 — OID Group Link 滥用, 2024 新 chain (Issuance Policy 链接 AD Group) [declared=surrogate_primary, auto=secondary; reason=vendor docs (作者一手 公司)] |
| T03-S012 | https://adsecurity.org/?page_id=1821 | surrogate_primary | 2026-05-18 | Sean Metcalf / Trimarc adsecurity.org | Active Directory Security Resources (Sean Metcalf) — Kerberoasting / Golden Ticket / DCSync / Mimikatz / Trust Attack 全 AD 攻击合集 [declared=surrogate_primary, auto=secondary; reason=vendor docs (作者一手)] |
| T03-S013 | https://www.harmj0y.net/blog/redteaming/targeted-kerberoasting/ | surrogate_primary | 2026-05-18 | Will Schroeder (harmj0y) harmj0y.net | Targeted Kerberoasting — 不全 domain dump, 只针对 high-value SPN 账户的 OPSEC-safe Kerberoasting 路径 [declared=surrogate_primary, auto=secondary; reason=vendor docs (作者一手)] |
| T03-S014 | https://www.ired.team/offensive-security-experiments/active-directory-kerberos-abuse | surrogate_primary | 2026-05-18 | Mantvydas Baranauskas ired.team | ired.team AD + Kerberos Abuse — SharpHound / BloodHound / Rubeus / Mimikatz / Impacket 工具链 + 步骤化笔记 [declared=surrogate_primary, auto=secondary; reason=vendor docs (作者一手)] |
| T03-S015 | https://book.hacktricks.wiki/en/generic-methodologies-and-resources/pentesting-methodology.html | surrogate_primary | 2026-05-18 | Carlos Polop / HackTricks book.hacktricks.xyz | HackTricks Pentesting Methodology — 单页 12-step 渗透通用 SOP + 各步骤 link 子方法 [declared=surrogate_primary, auto=secondary; reason=vendor docs (作者一手)] |
| T03-S016 | https://book.hacktricks.wiki/en/network-services-pentesting/pentesting-web/web-vulnerabilities-methodology.html | surrogate_primary | 2026-05-18 | Carlos Polop / HackTricks book.hacktricks.xyz | HackTricks Web Vulnerabilities Methodology — 完整 Web 测试 checklist + payload 库 [declared=surrogate_primary, auto=secondary; reason=vendor docs (作者一手)] |
| T03-S017 | https://www.hackingarticles.in/comprehensive-guide-on-pentesters-tools/ | surrogate_primary | 2026-05-18 | Raj Chandel hackingarticles.in | Comprehensive Pentester Tools Guide — 完整工具链 + use case + 实操 step-by-step [declared=surrogate_primary, auto=secondary; reason=vendor docs (作者一手)] |
| T03-S018 | https://www.trustedsec.com/blog/the-tactical-application-security-program-getting-stuff-done | surrogate_primary | 2026-05-18 | TrustedSec trustedsec.com | TrustedSec — Tactical AppSec Program: getting stuff done, AppSec engagement SOP + 整改 pipeline [declared=surrogate_primary, auto=secondary; reason=vendor docs (作者一手 公司)] |
| T03-S019 | https://www.nccgroup.com/us/research-blog/ | surrogate_primary | 2026-05-18 | NCC Group nccgroup.com | NCC Group Research Blog — 渗透 / 红队 / cryptography / hardware 多领域一手研究博客 [declared=surrogate_primary, auto=secondary; reason=vendor docs (作者一手 公司)] |
| T03-S020 | https://www.offsec.com/courses/pen-200/ | surrogate_primary | 2026-05-18 | OffSec offsec.com | OffSec PEN-200 / OSCP — Penetration Testing with Kali Linux syllabus + 24h hands-on, 入门红队事实认证 [declared=surrogate_primary, auto=secondary; reason=vendor docs (cert org syllabus + 教材)] |
| T03-S021 | https://www.offsec.com/courses/pen-300/ | surrogate_primary | 2026-05-18 | OffSec offsec.com | OffSec PEN-300 / OSEP — Evasion Techniques and Breaching Defenses, AV/EDR 绕过 + AD + Linux post-ex 进阶 syllabus [declared=surrogate_primary, auto=secondary; reason=vendor docs (cert org syllabus + 教材)] |
| T03-S022 | https://www.sans.org/cyber-security-courses/network-penetration-testing-ethical-hacking/ | surrogate_primary | 2026-05-18 | SANS Institute sans.org | SANS SEC560 / GPEN — Enterprise Penetration Testing 6 天 syllabus, Ed Skoudis 主创 [declared=surrogate_primary, auto=secondary; reason=vendor docs (cert org syllabus + 教材)] |
| T03-S023 | https://www.zeropointsecurity.co.uk/red-team-ops | surrogate_primary | 2026-05-18 | Zero-Point Security zeropointsecurity.co.uk | CRTO (Certified Red Team Operator) — Cobalt Strike 路径 syllabus + 实验室 + lab exam 完整红队 engagement [declared=surrogate_primary, auto=secondary; reason=vendor docs (cert org syllabus)] |
| T03-S024 | https://www.zeropointsecurity.co.uk/red-team-ops-ii | surrogate_primary | 2026-05-18 | Zero-Point Security zeropointsecurity.co.uk | CRTL (Certified Red Team Lead) — Cobalt Strike 高级 + lead engagement + OPSEC 自定义 profile [declared=surrogate_primary, auto=secondary; reason=vendor docs (cert org syllabus)] |
| T03-S025 | https://hstechdocs.helpsystems.com/manuals/cobaltstrike/current/userguide/content/cobalt-4-9-user-guide.pdf | surrogate_primary | 2026-05-18 | Fortra / Cobalt Strike cobaltstrike.com | Cobalt Strike User Guide v4.9 — 完整 C2 framework 文档 + listener + payload + malleable profile + BOF + Aggressor Script [declared=surrogate_primary, auto=secondary; reason=vendor docs (工具厂商 一手)] |
| T03-S026 | https://sliver.sh/docs?name=Getting+Started | surrogate_primary | 2026-05-18 | Bishop Fox sliver.sh | Sliver Docs — 开源 C2 framework Getting Started + 实战 implant + listener + armoury [declared=surrogate_primary, auto=secondary; reason=vendor docs (开源工具 一手)] |
| T03-S027 | https://docs.mythic-c2.net/ | surrogate_primary | 2026-05-18 | MythicC2 docs.mythic-c2.net | Mythic C2 Docs — modular C2 framework, payload type + C2 profile 分离, OPSEC 灵活 [declared=surrogate_primary, auto=secondary; reason=vendor docs (开源工具 一手)] |
| T03-S028 | https://getgophish.com/documentation/ | surrogate_primary | 2026-05-18 | Gophish getgophish.com | Gophish Docs — 开源 phishing framework 安装 + campaign 配置 + landing page + tracking [declared=surrogate_primary, auto=secondary; reason=vendor docs (开源工具 一手)] |
| T03-S029 | https://github.com/kgretzky/evilginx2 | surrogate_primary | 2026-05-18 | Kuba Gretzky / GitHub | Evilginx2 — AiTM (Adversary-in-the-Middle) phishing framework, 绕过 MFA via session cookie 中继 [declared=surrogate_primary, auto=secondary; reason=vendor docs (作者一手)] |
| T03-S030 | https://github.com/RhinoSecurityLabs/pacu | surrogate_primary | 2026-05-18 | Rhino Security Labs / GitHub | Pacu — AWS exploitation framework, 80+ 攻击模块 + 渗透 AWS 事实工具 [declared=surrogate_primary, auto=secondary; reason=vendor docs (作者一手 公司)] |
| T03-S031 | https://github.com/nccgroup/ScoutSuite | surrogate_primary | 2026-05-18 | NCC Group / GitHub | ScoutSuite — multi-cloud (AWS/Azure/GCP/Aliyun/Oracle) security audit tool, 红队 misconfig recon [declared=surrogate_primary, auto=secondary; reason=vendor docs (作者一手 公司)] |
| T03-S032 | https://github.com/BloodHoundAD/BloodHound | surrogate_primary | 2026-05-18 | SpecterOps / GitHub | BloodHound / BloodHound CE — AD attack path 图分析, 与 SharpHound / AzureHound 配套 [declared=surrogate_primary, auto=secondary; reason=vendor docs (作者一手 公司)] |
| T03-S033 | https://github.com/redcanaryco/atomic-red-team | surrogate_primary | 2026-05-18 | Red Canary / GitHub | Atomic Red Team — ATT&CK 技术原子化测试库, 紫队 + adversary emulation 事实工具 [declared=surrogate_primary, auto=secondary; reason=vendor docs (作者一手 公司)] |
| T03-S034 | https://github.com/mitre/caldera | surrogate_primary | 2026-05-18 | MITRE / GitHub | CALDERA — MITRE 出品 adversary emulation framework, 与 ATT&CK 集成 + 自动化 emulation chain [declared=surrogate_primary, auto=secondary; reason=vendor docs (协会)] |
| T03-S035 | https://portswigger.net/burp/documentation/desktop | surrogate_primary | 2026-05-18 | PortSwigger portswigger.net | Burp Suite Pro Docs — Web 渗透事实工具完整 user guide + extension API [declared=surrogate_primary, auto=secondary; reason=vendor docs (协会 + syllabus)] |
| T03-S036 | https://portswigger.net/web-security/all-materials | surrogate_primary | 2026-05-18 | PortSwigger Academy portswigger.net | PortSwigger Web Security Academy — 240+ lab Web 渗透 syllabus + walkthrough [declared=surrogate_primary, auto=secondary; reason=vendor docs (协会 syllabus)] |
| T03-S037 | https://www.bankingsupervision.europa.eu/ecb/pub/pdf/tibereu/ecb.tiber_eu_framework.en.pdf | surrogate_primary | 2026-05-18 | ECB / europa.eu | TIBER-EU Framework (European Central Bank) — 欧盟金融机构 Threat Intelligence-based Ethical Red-Teaming 监管型 SOP, 6-12 月 lifecycle [declared=surrogate_primary, auto=secondary; reason=vendor docs (监管 + 协会 — ECB europa.eu 公共监管文件, .europa.eu 不在 auto-verify 后缀)] |
| T03-S038 | https://www.bankofengland.co.uk/financial-stability/operational-resilience-of-the-financial-sector/cbest-intelligence-led-testing | surrogate_primary | 2026-05-18 | Bank of England bankofengland.co.uk | CBEST Intelligence-Led Testing — 英国央行驱动金融机构红队监管型框架, 与 TIBER-EU 对应 [declared=surrogate_primary, auto=secondary; reason=vendor docs (监管 — Bank of England 公共监管文件, .co.uk 不在 auto-verify 后缀)] |
| T03-S039 | https://docs.hackerone.com/en/articles/8410434-disclosure-guidelines | surrogate_primary | 2026-05-18 | HackerOne hackerone.com | HackerOne Disclosure Guidelines + Code of Conduct — Bug bounty hunter ROE + 边界 [declared=surrogate_primary, auto=secondary; reason=vendor docs (平台 一手)] |
| T03-S040 | https://www.cisa.gov/news-events/news/cisa-releases-cybersecurity-advisory-update-tactics-techniques-and-procedures-fin7 | verified_primary | 2026-05-18 | CISA cisa.gov | CISA Advisory — FIN7 TTPs, adversary emulation 选 target actor 参考 |
| T03-S041 | https://www.frida.re/docs/home/ | surrogate_primary | 2026-05-18 | NowSecure / Frida frida.re | Frida Docs — 动态 instrumentation framework iOS/Android/Linux/Windows 一手文档 [declared=surrogate_primary, auto=secondary; reason=vendor docs (开源工具 一手)] |
| T03-S042 | https://github.com/sensepost/objection | surrogate_primary | 2026-05-18 | SensePost / GitHub | Objection — Frida 高层封装, mobile 渗透 SSL pinning bypass + Java/Obj-C 方法 hook [declared=surrogate_primary, auto=secondary; reason=vendor docs (作者一手 公司)] |
| T03-S043 | https://www.thedfirreport.com/ | surrogate_primary | 2026-05-18 | The DFIR Report thedfirreport.com | The DFIR Report — 详细 attack chain 复盘报告, 红队 emulation 真实 TTPs 参考 [declared=surrogate_primary, auto=secondary; reason=vendor docs (作者一手)] |
| T03-S044 | https://anquanke.com/ | surrogate_primary | 2026-05-18 | 安全客 / 奇虎 360 anquanke.com | 安全客 — 中国一线红队 / 漏洞研究 一手社区, KEEN Lab / Vulcan / Chaitin 等 PoC + writeup [declared=surrogate_primary, auto=secondary; reason=vendor docs (中国 安全 社区)] |
| T03-S045 | https://xz.aliyun.com/ | surrogate_primary | 2026-05-18 | 阿里云先知 xz.aliyun.com | 阿里先知 — 中国 Web / 内网 / 云 红队中文一手社区 [declared=surrogate_primary, auto=secondary; reason=vendor docs (中国 安全 社区)] |

## SOPs

### 1. External Network Pentest 外网渗透 SOP

**目标 + 适用场景**: 评估客户在公网暴露的资产 (域名 + IP CIDR + SaaS + 子域名) 的攻击面与可被外部攻击者直接利用的漏洞, 输出 攻击链 (从无凭据 外部攻击者 → DMZ → 内部) + 整改优先级. 适用于 年度合规 (PCI-DSS / SOC 2 / ISO 27001) / 上线前 / 收购尽调 / 重大产品发布前.

**入门 SOP**:
1. **Phase 0 — Pre-engagement**: 接收 SOW + ROE + scope 文档, 确认 IP / 域名白名单, 签 engagement letter + 律师 review, 设 safe word + emergency contact, 与客户 NOC 协调 maintenance window.
2. **Phase 1 — Passive Recon**: 用 amass / subfinder / assetfinder / chaos / crt.sh / DNSdumpster 收集子域名, securitytrails + virustotal 查 历史 DNS, theHarvester 收集 邮箱 + 员工.
3. **Phase 1 — Active Recon**: 对 in-scope IP/domain 跑 nmap -sV -sC -p- (全端口 service+script), naabu 快速 port discovery, httpx 探测 web 服务, eyewitness / aquatone 截图 web 资产.
4. **Phase 2 — Vulnerability Identification**: 跑 nuclei (含 cves / vulnerabilities / exposures / misconfigurations templates), 手动 review web app (Burp Proxy + Repeater), 检查 CVE 在 NVD / CISA KEV.
5. **Phase 3 — Exploitation**: 优先验证 CISA KEV catalog 中已被在野利用的 CVE, 用 Metasploit / 公开 PoC / 自定义 exploit, 拿到 RCE / shell 之后立刻 sleep + 与 PM / 客户 确认是否 weaponize.
6. **Phase 4 — Web Pivot**: 拿到 web shell 之后, 检查 内网 reachability + AWS metadata IMDS + 凭据文件 + SSRF chain.
7. **Phase 5 — Reporting**: finding 列表 (CVSS + ATT&CK ID + repro + impact + remediation), executive summary, 整改 retest plan.

- **资深路径**: **跳过** standard KO meeting 中不必要的 scope 重申 (老客户 SOW 已签 + 历史 engagement 已有 baseline, 直接进入 delta 资产差异即可), **优化** OSINT 用 SecurityTrails + Shodan + Censys + Chaos + GitHub dorking 多源并行 (Python asyncio + httpx + dnsx pipeline 批量, 而不是 一个一个 工具串行), **额外** 做 supply chain 检测 (3rd party SaaS dependency 如 Salesforce / Workday / HubSpot 配置错误 + GitHub repo 泄漏 secrets via TruffleHog / gitleaks + S3/GCS 公开桶 via cloud_enum + npm/pip typosquat).

**失败模式 + remediation**:
1. **失败: scope creep — 测着测着发现 in-scope 资产 host on shared infra 与 out-of-scope 资产同 IP**. Remediation: 立即 STOP + 通知 PM + 与客户法务 重新签 scope addendum, 不要 'just a quick check' 假设授权.
2. **失败: active scan 触发 WAF / IPS 客户 SOC 报警**. Remediation: 提前与 SOC 协调 source IP 白名单, 用 stealth 模式 (nmap -T2 / nuclei -rate-limit 10), 必要时 暂停 + 调整速率.
3. **失败: nuclei false positive 太多, 报告充水**. Remediation: 资深应人工验证 high/critical, low/info 用 -severity 过滤 + 二次验证.
4. **失败: 找到 RCE 立即 exploit 触发服务中断**. Remediation: 严守 'exploit before weaponize 必须 PM 确认' 原则, prod 系统 default 仅 PoC level 验证, 不 deploy persistence.
5. **失败: 客户事后否认授权, 法律风险**. Remediation: 永远 engagement letter + SOW + ROE 三件套书面 + 律师 review, 口头授权无效, 邮件备份 + 时间戳.

**OPSEC 注意**:
1. 攻击 infrastructure 隔离: VPS / 域名 / cert 不复用历史 engagement, payload 一次性.
2. 流量加密: TLS 1.3 + DNS over HTTPS, 不走未加密 HTTP/DNS.
3. Source IP 白名单提交客户 SOC, 但 自己 OPSEC 也用 Cloudflare / Fastly 等 CDN 中继.
4. 不在公网留任何 artifact (uploaded shell / cron / scheduled task) 超出 engagement 周期, 离场 cleanup checklist.
5. Burp / Caido 项目文件加密保管, 包含 credentials + session token 必须 7-zip AES-256 加密 + air-gapped 存储.

### 2. Internal AD Pentest SOP (Assume Breach)

**目标 + 适用场景**: 假设 attacker 已经通过 phishing / 物理 plant box / 供应链 拿到一台普通 Domain User 主机, 评估 从 Domain User 到 Domain Admin (DA) / Enterprise Admin (EA) / Forest Admin 的攻击路径, 输出 AD 攻击面 + 优先整改路径. 适用于 大型企业 internal red team / assume breach assessment / TIBER-EU + CBEST 监管.

**入门 SOP**:
1. **Phase 0 — Recon (低噪音)**: nltest / setspn / dsquery / net user /domain 基础 AD 信息收集 (built-in 不触发 EDR), 确认 Domain Controller IP + functional level.
2. **Phase 1 — BloodHound 收集**: 跑 SharpHound (-c All) 或 bloodhound-python / ldeep / SOAPHound 收集对象 + ACL + session.
3. **Phase 1 — BloodHound 分析**: 在 BloodHound CE GUI 查 'Shortest Paths to Domain Admins from Owned Principals', 标记 attack path.
4. **Phase 2 — Kerberos abuse**: 查找 Kerberoastable (SPN 注册 user account) via Rubeus / GetUserSPNs.py kerberoast → hashcat -m 13100; AS-REP-roastable (DONT_REQ_PREAUTH) via Rubeus / GetNPUsers.py → hashcat -m 18200.
5. **Phase 3 — ADCS 检查**: 跑 Certify / certipy find -enabled -vulnerable 查 ESC1-15 vulnerable template, 优先 ESC1 (ENROLLEE_SUPPLIES_SUBJECT) + ESC8 (Web Enrollment NTLM relay).
6. **Phase 4 — NTLM 中继 / coercion**: PetitPotam / Coercer 强制 DC NTLM auth, ntlmrelayx.py 中继到 LDAPS / ADCS Web Enroll / SMB.
7. **Phase 5 — DCSync / DA**: 拿到 高权限后 secretsdump.py / mimikatz dcsync 同步 krbtgt + 域用户 hash, golden ticket persistence.
8. **Phase 6 — Reporting**: 攻击链图 (BloodHound 截图 + Mermaid) + ATT&CK 映射 + Tier 0 整改建议.

- **资深路径**: **跳过** 全 domain 自动 SharpHound (`-c All` 在大 enterprise = 数百万条 LDAP query + 反 EDR 高风险触发 ML detection), 改用 ldapsearch + targeted SOAPHound + 仅 collect 必要 collection method (SessionLoop + LocalAdmin 单跑 而不是 All); **优化** 用 in-memory PowerView (Invoke-Expression 不落盘) + impacket targeted 操作 (单 SPN Kerberoast 而不是 全 dump) + Rubeus /opsec 模式 (避开 4769 高熵 ticket request), 与 PowerSploit 历史完整 dump 路径对比 OPSEC stealth 大幅提升; **额外** 做 ADCS 全 cert template ESC chain 检查 (Certipy find -vulnerable -dc-ip) + ESC8 NTLM 中继到 ADCS Web Enrollment 拿 DC cert + ESC9-11 (2023+) noPreAuth + weak EKU + cert remapping 新 chain + ESC13 (2024 SpecterOps) OID Group Link + ESC14-15 (2024 后续) 新型 + SCCM / MECM 滥用 (SharpSCCM) + Microsoft Configuration Manager NAA / network access account.

**失败模式 + remediation**:
1. **失败: SharpHound -c All 在 50k+ user enterprise 跑 12+ 小时 + EDR alert**. Remediation: 分批 (Collection 拆 + DCOnly + targeted), 或换 SOAPHound (SOAP-based 低噪音).
2. **失败: Rubeus kerberoast 在 ETW + ML EDR (CrowdStrike / Defender for Identity) 触发**. Remediation: 用 /opsec 模式 + 一次只 request 一个 SPN, 间隔 sleep.
3. **失败: 跑 mimikatz 触发 AV (Defender + Sophos + S1)**. Remediation: 用 in-memory invoke + sRDI shellcode + Donut + reflective DLL load, 或换 nanodump (handle dump LSASS) + impacket secretsdump 离线 解析.
4. **失败: Coercer / PetitPotam 触发 4624 + 4625 SOC noise**. Remediation: 与 SOC 提前协调或 严守 monitoring window, 必要时 暂停.
5. **失败: 拿到 DA 立即 dcsync 导出全 hash 报告显得过度**. Remediation: PoC 级别仅证明 path, 不导出完整 NTDS.dit, OPSEC + 法务 + 客户接受度三角平衡.

**OPSEC 注意**:
1. 不复用历史 implant / payload hash, EDR ML detection 会跨 engagement learn.
2. C2 流量 long sleep (300+ jitter 30%) + low rate, 不要 default 60s beacon.
3. LDAP query 限制 size limit + page size, 不要 default 1000 一次.
4. 离场 cleanup: 删除 添加的账号 / persistence / 测试 SPN / lab cert / kerberos ticket cache.
5. 报告 redact: NTDS.dit hash / cleartext credential 必须 partial mask (前 8 后 4) + 加密 PDF + 仅 客户 CISO 直接 + 律师 收到.

### 3. Web Application Pentest SOP (OWASP WSTG)

**目标 + 适用场景**: 系统性测试 Web 应用 (传统 MVC + SPA + GraphQL + REST API + WebSocket) 的认证 / 授权 / 输入 / 业务逻辑 / 客户端 / API 等 12 域, 输出 OWASP Top 10 + WSTG 覆盖率报告. 适用于 上线前安全审计 / 年度合规 / SaaS 续约 / DevSecOps pipeline gate.

**入门 SOP**:
1. **Phase 1 — Information Gathering**: WSTG-INFO-01-10, 收集 fingerprint (Wappalyzer / WhatWeb / httpx -tech-detect), spider Burp / Caido + 手动 click-through, 列 endpoints + parameters.
2. **Phase 2 — Configuration & Deployment**: WSTG-CONF, 检查 .git / .svn / backup / .env / robots.txt / sitemap.xml / Header (HSTS / CSP / X-Frame-Options).
3. **Phase 3 — Identity & Authentication**: WSTG-IDNT + WSTG-ATHN, username enumeration + password policy + MFA bypass + session fixation + remember me.
4. **Phase 4 — Authorization**: WSTG-ATHZ, IDOR (替换 ID) / privilege escalation / path traversal / forced browsing.
5. **Phase 5 — Session Management**: WSTG-SESS, cookie attr (Secure/HttpOnly/SameSite) / token entropy / logout invalidation.
6. **Phase 6 — Input Validation**: WSTG-INPV, SQLi / XSS / SSRF / XXE / SSTI / 反序列化 / 命令注入 / LDAP / NoSQL / 模板注入.
7. **Phase 7 — Error / Crypto**: error message 信息泄漏 / weak TLS / 自签证书 / random number 弱.
8. **Phase 8 — Business Logic**: race condition / 替换 价格 / 重复使用 一次性 token / workflow 跳步.
9. **Phase 9 — Client-side**: DOM XSS / postMessage / CORS / CSP bypass / clickjacking.
10. **Phase 10 — API**: REST / GraphQL / WebSocket / gRPC mass assignment + BOLA + BFLA.

- **资深路径**: **跳过** default 一刀切 12 域全 categories 测试 (中小应用 + tight timeline 浪费 ROI), 优先 high-value endpoints (login / payment / admin panel / file upload / SSO callback / OAuth + JWT issuer) + 复用 历史 engagement baseline; **优化** Burp Pro Active Scan + Param Miner (隐藏参数发现) + Autorize (二账户授权对比) + Logger++ (请求历史搜索) + Turbo Intruder (race condition + 高并发) + Backslash Powered Scanner (深 input fuzz) 并行扩展, performance 上换 Caido (Rust 性能更好 + 现代 UI) 对超大 scope; **额外** 做 GraphQL introspection (InQL / GraphQL Voyager) + JWT key confusion (HS256 vs RS256 / jwt_tool / jwt-cracker) + race condition (Turbo Intruder single-packet attack via HTTP/2) + SSRF chain to Cloud metadata IMDS (AWS 169.254.169.254 IMDSv1 v2 token / Azure / GCP) + HTTP request smuggling (CL.TE / TE.CL / TE.TE) + Server-Side Prototype Pollution + Web cache deception + OAuth 2.0 / OIDC bypass.

**失败模式 + remediation**:
1. **失败: Active scan 触发 WAF block source IP 整个 engagement 暂停**. Remediation: 提前与客户 WAF 团队 协调白名单 source IP, 或 Burp 设 Throttle + 用户代理伪装.
2. **失败: SQLi 验证用 ' OR 1=1 -- 触发整表 update / delete 数据损坏**. Remediation: 用 sqlmap --safe / 只 boolean-based / time-based blind, prod 系统 default 不 dump 完整表.
3. **失败: SSRF 验证打 内部 metadata 触发 AWS account compromise**. Remediation: PoC 仅 hostname leak / DNS callback (Burp Collaborator), 不直接 fetch credential.
4. **失败: 业务逻辑漏洞 描述客户不接受 ('this is by design')**. Remediation: 资深应在 finding 加 'attack scenario + business impact + 监管/合规映射' 论证, 不是只描述技术 mechanism.
5. **失败: Burp scope 配错导致测了 out-of-scope subdomain**. Remediation: scope 用 regex 显式 + Include/Exclude 二次确认, 每天结束 check log 有无 out-of-scope 请求.

**OPSEC 注意**:
1. Burp / Caido session 加密保管 + 离场后 加密 archive + 90 天 后销毁.
2. 不在公网测试服务器留 webshell / file upload artifact 超过 engagement window.
3. Credentials 不写在 issue tracker / Jira / Slack, 用 KeePassXC + age-encrypted file.
4. 测试用户账号 (test_redteam_xx) 离场 disable + 通知客户.
5. Browser cookie + localStorage 离场 clear, 不复用 historic profile.

### 4. Mobile App Pentest SOP (OWASP MASTG)

**目标 + 适用场景**: 测试 Android (APK) + iOS (IPA) 应用的 storage / crypto / authentication / network / platform interaction / code quality / resilience 7 类 (MASVS), 输出 MAS Verification Standard L1/L2 覆盖度报告. 适用于 金融 / 政务 / 医疗 mobile app 上线前 / 应用商店审核前 / 合规 (PCI 4.0 SAQ-A-EP / HIPAA / 等保 2.0).

**入门 SOP**:
1. **Phase 1 — 收集 + 准备**: 客户提供 APK / IPA + 测试账号 + 测试环境 + 业务文档, 准备 测试设备 (Android: Pixel + Magisk / KernelSU root; iOS: 越狱 iPhone X with checkra1n / palera1n).
2. **Phase 2 — Static Analysis (Android)**: apktool d / jadx-gui 反编译 APK, 看 AndroidManifest.xml 权限 + exported component + intent filter, 看 res/values/strings.xml 硬编码 secret, 用 MobSF 自动扫描.
3. **Phase 2 — Static Analysis (iOS)**: class-dump / Hopper / Ghidra / IDA Pro 反编译 Mach-O, 看 plist 权限, 看 .ipa 内 embedded provisioning + 证书.
4. **Phase 3 — Dynamic Instrumentation**: Frida + Objection 设置 hook, 监听 关键 API (NSURLSession / okhttp / Cipher / KeyStore / Keychain).
5. **Phase 4 — SSL Pinning Bypass**: 用 frida-script (codeshare frida.re 上 universal pinning bypass) 或 objection android sslpinning disable / ios sslpinning disable.
6. **Phase 5 — Traffic 拦截**: Burp / Caido 配置 proxy + 安装 CA 到 system store (Android 7+ 需 root 装 system trust) + iptables / WiFi proxy 设备级 redirect.
7. **Phase 6 — Local Storage**: 检查 SharedPreferences (Android) / NSUserDefaults / Keychain (iOS) / SQLite / Realm / Core Data 内是否硬编码 token / 明文 PII.
8. **Phase 7 — Reporting MASVS 1-3**: 按 MASVS-Storage / Crypto / Auth / Network / Platform / Code / Resilience 输出 finding + MASTG test ID.

- **资深路径**: **跳过** 普通 root/jailbreak detection 一个一个绕 (大部分 app 用 RootBeer + 几个常规 magic file path 检测), 直接 Magisk Hide / KernelSU + Shamiko / Zygisk-DenyList 系统级 hide + iOS 用 Liberty Lite / Shadow 全局 hide, 省 reverse 数小时; **优化** Frida script reuse from codeshare.frida.re collection (universal-android-ssl-pinning-bypass-with-frida / fridantiroot / objection patcher 模板), 复用 比 从头 hook 快 10x; **额外** 做 native lib reverse engineering (libxxx.so / Mach-O 二进制 via Ghidra / IDA Pro / Binary Ninja, JNI 接口 + obfuscation 解密) + WebView 漏洞 (JavaScript bridge addJavascriptInterface RCE + file:// scheme access + WebContents loadUrl JS injection) + deep link / universal link hijacking + intent abuse (exported activity / broadcast receiver) + Android 13+ TileService / Permissions Controller misconfiguration + iOS URL scheme hijack + Mach IPC interception.

**失败模式 + remediation**:
1. **失败: SSL pinning bypass 失败 — 应用用 native pinning + obfuscated**. Remediation: 用 native level Frida hook SSL_CTX_set_verify (boringssl) 或 BoringSSL OpenSSL 函数 替换, 不要 Java/Swift level.
2. **失败: 客户 app 检测 Frida 启动失败**. Remediation: frida-server rename + non-default port (默认 27042), 或用 spawn gating + early instrument, 或 patch APK 直接 inject frida-gadget.
3. **失败: 拿到 token 测后端 API 触发后端 rate limit / 锁账号**. Remediation: 测试账号专用 + 与后端 SRE 协调 throttle 白名单.
4. **失败: 反编译 obfuscated DEX (ProGuard / R8 / DexGuard) 函数名全 a/b/c**. Remediation: 用 jadx-gui 高级 deobfuscation + 字符串解密 + cross-reference, 或 dynamic 跑 + Frida log 推断.
5. **失败: 测试设备意外 brick (root 失败 / 越狱失败)**. Remediation: 测试前 全镜像 backup (Magisk Manager / iTunes IPSW), 多备机 + iOS 用 旧 iPhone (易越狱).

**OPSEC 注意**:
1. 测试用户账号专用 (test_mas_redteam_NN), 不混 个人 Apple ID / Google account.
2. APK / IPA 反编译 artifact 加密保管 + 离场后 销毁 (客户知识产权).
3. Burp CA 证书离场 device 内 uninstall, 不留在 system trust.
4. 不上传 客户 app 到 VirusTotal / koodous / 其他 公开扫描 (信息泄漏 + IP 风险).
5. 测试设备每 engagement 重置 + factory reset, 不跨 engagement 复用.

### 5. Cloud Pentest SOP (AWS focus + Azure + GCP)

**目标 + 适用场景**: 评估云环境 (AWS / Azure / GCP) 的 IAM 配置 + 资源 misconfiguration + 攻击路径, 输出 从初始 凭据 → cross-service privesc → cross-account → 数据 exfil 完整链. 适用于 cloud migration 后 / 多云架构 / 大型 SaaS 厂商 / 容器化 (K8s) workload.

**入门 SOP**:
1. **Phase 0 — Credential acquisition**: 起点凭据由 客户提供 (assume-role / IAM user) 或 phishing 模拟 (在 ROE 内) / S3 公开桶 leak / GitHub repo secret / .env 文件.
2. **Phase 1 — IAM Enumeration (AWS)**: Pacu (whoami → IAM__enum_users_roles_policies_groups) + aws iam list-* + enumerate-iam.py + cloudfox aws inventory.
3. **Phase 1 — IAM Enumeration (Azure)**: AzureHound + ROADtools (roadrecon) + AADInternals.
4. **Phase 1 — IAM Enumeration (GCP)**: gcp_enum + IAM Recon + gcloud auth + cloudfox gcp.
5. **Phase 2 — Privilege Escalation 路径**: ScoutSuite full audit + Pacu iam__privesc_scan (21 IAM privesc paths) + Cloudsplaining + IAMSpy.
6. **Phase 3 — 资产 enumeration**: S3 (s3scanner + AWSBucketDump), Lambda (function code + env var), EC2 (metadata IMDSv1/v2), SSM Parameter Store + Secrets Manager, RDS, EFS, ECR.
7. **Phase 4 — Lateral via STS chain**: assume-role chain + cross-account trust + EC2 instance role + Lambda invoke + RDS IAM auth.
8. **Phase 5 — Exfil simulation**: 不真实 download 数据, 用 S3 ls + DynamoDB scan dry-run + Snowflake list table 证明 access, 离场清理.
9. **Phase 6 — Reporting**: IAM 路径图 (AWSPX 可视化) + ATT&CK Cloud 映射 + 整改 priority.

- **资深路径**: **跳过** 全自动 ScoutSuite 完整 audit 在大型 multi-account org (慢 + noisy + CloudTrail 大量 log entry), 按 IAM role attack path 优先级 (BloodHound-like 思路 — 从已有 principal 反推可达 high-value target via assume-role + service trust + condition); **优化** 同时跑 AzureHound + Pacu + ScoutSuite + cloudfox + Prowler 多云多工具并行 (asyncio + Docker 隔离) + 自己写 SHARP-cloud / AWS API direct boto3 script 针对 specific IAM permission (例如 lambda:UpdateFunctionCode 单 permission privesc 不需跑全 audit); **额外** 做 K8s RBAC 链 (kubectl who-can + peirates + kubehound + KubiScan) + container 逃逸 (CVE-2022-0492 cgroup / CVE-2024-21626 runc / 挂载 /var/run/docker.sock + privileged pod + hostPath / hostNetwork) + Cloud SIEM evasion (CloudTrail event source 仿冒 + EventBridge rule + GuardDuty 已知 detector 规避 + AWS Config / Azure Sentinel rule bypass) + serverless cold start abuse + Service Control Policy (SCP) bypass at org level.

**失败模式 + remediation**:
1. **失败: 误删 / 误改 客户 cloud 资源**. Remediation: ROE 必须显式 'read-only' 或 'simulated write' 模式, prod account 禁用 destructive API call (IAM policy explicit Deny).
2. **失败: 跑 ScoutSuite / Prowler 触发 CloudTrail 大量 ReadOnly log 占满 storage**. Remediation: 与客户 SOC 协调 throttle + temporary CloudTrail filter.
3. **失败: assume-role chain 触发 cross-account alert (GuardDuty UnauthorizedAccess:IAMUser/InstanceCredentialExfiltrationOutsideAWS)**. Remediation: 走 客户 designated source IP (VPN 进 客户 jump box), 不要从随机 VPS.
4. **失败: 拿到 S3 bucket 列出 PII 报告写入 finding**. Remediation: PoC 仅 list head + 1-2 sample object key, 不下载完整数据 + 不在报告 列 真实 PII.
5. **失败: K8s pod 逃逸到 node 之后 影响 其他 tenant**. Remediation: 多租户 K8s 必须 与 client 提前确认 in-scope tenant, 不要 cross-namespace.

**OPSEC 注意**:
1. 攻击 source 用 客户 designated IP (VPN / WireGuard) 不要随机 VPS (GuardDuty geo + ASN 异常 detection).
2. Boto3 / az-cli / gcloud user-agent 自定义统一标记 (例如 'redteam-engagement-001'), 便于 客户 SOC 在 log 中 滤掉测试流量.
3. STS session token 短期 (15 min - 1 hr) + 用完即弃, 不存盘.
4. CloudTrail / Azure Activity / GCP Audit Log 离场 与客户 一起 export + archive (而不是 删除证据).
5. 测试 IAM role 离场 disable / detach policy / delete, 不留 backdoor.

### 6. C2 Setup + Operate SOP

**目标 + 适用场景**: 搭建 + 运行 红队 C2 framework (Cobalt Strike / Sliver / Mythic / Havoc) 用于 长期 engagement 的 implant management + post-ex tasking + OPSEC 隐蔽 + 多 operator 协作. 适用于 long-term assumed breach engagement / TIBER-EU + CBEST monthsslong / adversary emulation.

**入门 SOP**:
1. **Phase 0 — Infrastructure plan**: 设计 redirector (Nginx / Apache mod_rewrite / HAProxy) → C2 server 二层架构, CDN front (Cloudflare / Fastly / Azure Front Door), categorization aged domain (购 30+ days 老域名 + Google SafeBrowsing / OpenDNS / Cisco Talos / VirusTotal 分类查), Let's Encrypt cert.
2. **Phase 1 — C2 server 部署**: Cobalt Strike teamserver (Java) 或 Sliver (Go) 或 Mythic (Docker compose) 部署在 隔离 VPS, 配置 listener (HTTP / HTTPS / DNS / SMB pipe / TCP).
3. **Phase 2 — Malleable C2 profile (CS) / extensible config**: 写 .profile 文件指定 HTTP header + URI + 数据 transform + sleep + jitter + DNS profile, 与 redirector + CDN 配合做 traffic camouflage.
4. **Phase 3 — Payload generation**: 生成 stager / stageless beacon (CS) / implant (Sliver: sliver generate --mtls / Mythic: payload type Apollo/Poseidon/Athena), 配合 obfuscation (ConfuserEx / Donut / sRDI / Garble for Go).
5. **Phase 4 — Initial delivery**: phishing / 物理 USB / supply chain (在 ROE 内) deliver payload.
6. **Phase 5 — Beacon callback + tasking**: callback 后立即 sleep 调高 + situation awareness (whoami / hostname / domain / AV/EDR 检测).
7. **Phase 6 — Post-ex**: 按 ATT&CK tactics 走 (Discovery → Cred Access → Lateral → Collection → Exfil), 每步 OPSEC 评估.
8. **Phase 7 — 离场 cleanup**: kill all beacons + 通知客户 + infrastructure 解构 (域名 + cert 不复用) + log archive.

- **资深路径**: **跳过** default malleable profile (CS default = signature trip — Defender / CrowdStrike / Sentinel / Elastic 已有 default profile detection, 直接用 default = 立即 burned), 必须 自定义 profile + Domain Fronting + 长 sleep (300+ s) + jitter (30-50%) + Sleep Mask (CS BeaconGate / Ekko + Sleep Mask Kit); **优化** redirector + Cloudflare Workers / Fastly Compute@Edge + DNS over HTTPS + 域名 categorization aged (购 30+ days old domain via ExpiredDomains.net + Domcop + 检查 Wayback historical content), HTTPS cert 用 Let's Encrypt + SAN match + DNS validation; **额外** 做 BOF (Beacon Object File) for inline execution (避免 fork & run process create 噪音 — situational_awareness_bof + adcs_bof + sccm_bof 全 in-process), IPC for cross-beacon communication (SMB pipe + named pipe + cross-session lateral), Aggressor Script (CS) / Sliver extension / Mythic command 自动化 engagement repetitive task, BOF.NET / InlineExecute-Assembly inline .NET assembly 执行替代 execute-assembly fork.

**失败模式 + remediation**:
1. **失败: Cobalt Strike default profile 被 Defender / CrowdStrike 立即 detect**. Remediation: 严禁 default profile, 必须 per-engagement customized + 测试在 lab 先验证 detection.
2. **失败: C2 域名被 categorize 为 malicious 后 burn**. Remediation: 提前 categorization test (URLCat + Cisco Talos check), aged domain + 提前 warm-up.
3. **失败: 多 operator 同时 task beacon 冲突**. Remediation: 用 CS team server + Slack / Mattermost engagement channel + clear ownership note.
4. **失败: payload 触发 ML EDR (CrowdStrike / S1) heuristic detection**. Remediation: BOF inline 替代 execute-assembly + indirect syscall (HellsGate / HalosGate / TartarusGate) + ETW patch + AMSI patch.
5. **失败: beacon log 含 大量 sensitive credential 客户 不接受存盘**. Remediation: log encryption + 离场 archive 加密 + 7-zip AES + 仅客户 CISO + 律师 持有.

**OPSEC 注意**:
1. C2 infrastructure 完全隔离 — VPS / 域名 / cert / SSH key 不复用历史 engagement.
2. Operator 自身 OPSEC: 用 separate browser profile / VM (Whonix + Tails / Qubes) 连 teamserver, 不混 个人 setup.
3. 日 metrics 监控: 哪些 beacon checking in / 网络 异常 / 是否 客户 SOC 已 IOC published.
4. Sleep mask + thread stack spoofing (CS 4.7+ / Ekko / FOLIAGE) 应对 in-memory scan.
5. 离场 24h 内 完全 解构 infrastructure (域名 release + VPS destroy + cert revoke) + log archive 加密.

### 7. Phishing Campaign (Authorized Only) SOP

**目标 + 适用场景**: 在 engagement letter + ROE 显式 phishing 授权下, 执行 social engineering 钓鱼 campaign, 评估 用户安全意识 + email gateway + MFA + EDR 检测覆盖, 输出 click rate + credential capture rate + 培训建议. 适用于 季度 awareness program / TIBER-EU initial access 模拟 / assumed breach 起点.

**入门 SOP**:
1. **Phase 0 — Engagement letter**: 必须 显式 phishing 授权 + safe word + emergency contact (24/7) + 客户 SOC + IT helpdesk + 法务 通知列表.
2. **Phase 1 — Infrastructure**: Gophish (open source) 或 Evilginx2 (AiTM) 或 Tycoon 2FA (商业) + 邮件 SES / Mailgun / 自建 SMTP + warm-up (新域 不能立刻发 万封) + SPF + DKIM + DMARC + ARC 配置.
3. **Phase 2 — Pretext + landing**: 设计 客户业务相关 pretext (HR 政策更新 / IT 安全公告 / 业务伙伴邀请) + landing page (clone target 真实 SSO / Office 365 / Okta login).
4. **Phase 3 — Target list**: 客户 HR 提供 employee 邮箱 (与法务确认 GDPR + 客户内部 合规) 或 OSINT (LinkedIn + hunter.io + theHarvester).
5. **Phase 4 — Send + track**: 小批量先发 (10-50) 测试 deliverability + IP reputation 不被 spam filter block, 然后逐步 scale.
6. **Phase 5 — Capture + interaction**: 抓取 click / open / submit credential / MFA token, 实时监控.
7. **Phase 6 — Reporting**: click rate + credential rate + MFA bypass rate + ATT&CK ID (T1566.001-004) + 部门 trend + 培训建议.

- **资深路径**: **跳过** generic templates (Microsoft Office 365 phishing 现 普通 user 警觉 — 多年安全培训后 click rate 个位数), 用 client-specific spoof (合伙人邮件 / HR 福利通知 / 内部 IT ticket / 第三方 SaaS 通知 — 例如 真实 ServiceNow / Workday 域名 typosquat); **优化** 用 Tycoon 2FA / Evilginx2 AiTM (Adversary-in-the-Middle reverse proxy) 对抗 MFA, 一次 capture session cookie 直接 import 浏览器 (而不是 credential 简单 capture 后 还要 prompt MFA); **额外** 做 device code phishing (Microsoft authentication device code flow abuse — t1528 OAuth token theft via 微软 / Google 合法 device code grant flow + 用户输入 attacker provided device code) + OAuth consent phishing (恶意 Azure AD app 请求 user 同意 Graph API offline_access + Mail.Read + Files.ReadWrite.All 持久 token) + smishing (SMS 钓鱼 Twilio + 短信网关) + vishing (Vapi / ElevenLabs + AI voice clone, 在 ROE 内) 多通道 + Browser-in-Browser (BitB) attack + ClickFix social engineering.

**失败模式 + remediation**:
1. **失败: 邮件全被 spam filter block, deliverability 0%**. Remediation: 严守 SPF + DKIM + DMARC + ARC + warm-up + 老域 + 合规 reply-to + 与客户 IT 协调 allow-list source IP.
2. **失败: phishing 钓到 客户高管 触发 法律 / 公关风险**. Remediation: 严守 target list 与 客户 HR + 法务签确认 + 高管可豁免 + safe word 触发立即 stop.
3. **失败: 真实员工 用 钓鱼 credential 攻击 真实生产系统**. Remediation: capture 后 立即 mark + 不 actually use credential 入 prod, OPSEC 严守.
4. **失败: 客户 SOC 不知道 在 跑 phishing 上报 真实 IR 流程**. Remediation: 提前 通知 SOC 该日期 + source IP + 域名 in allow-list (但 random sample 不通知 measure 真实 detection).
5. **失败: 钓鱼 触发 GDPR / 网安法 / 数据安全法 个人信息合规**. Remediation: 提前法务 review + 限制 collect 信息 (仅 credential 而非 PII) + 一定 retention 后销毁.

**OPSEC 注意**:
1. 域名 + 邮件 infrastructure 隔离 + 一次性 + 不复用历史 engagement.
2. landing page TLS + Let's Encrypt + cert 单独 + 离场 revoke.
3. Captured credentials 加密保管 (age + KeePassXC) + 与客户 24h 内 移交 + 自己端 销毁.
4. 不在公网 留任何 phishing landing 超过 engagement window.
5. 报告 redact: 个人 click record 必须 anonymize (group level statistics 不 named-and-shamed).

### 8. Purple Team / Adversary Emulation SOP

**目标 + 适用场景**: 选定 threat actor (基于 客户 threat model 选 e.g. FIN7 / APT29 Cozy Bear / APT41 / Scattered Spider / Volt Typhoon), 提取 TTPs (ATT&CK ID), 用 Atomic Red Team / CALDERA / Scythe / Vectr build emulation chain, 与 blue team SOC + Detection Engineering 团队 协同执行 + 实时收集 telemetry + 评估 detection 覆盖率 + 改进 detection content. 适用于 detection engineering maturity 提升 / SOC 演练 / CTEM (Continuous Threat Exposure Management) 实施.

**入门 SOP**:
1. **Phase 1 — Threat actor 选定**: 与 客户 CISO + threat intel 团队 协作, 选 1-3 个 relevant actor (基于 行业 / 历史 incident / threat report — Mandiant + CrowdStrike + Recorded Future + Microsoft Threat Intel).
2. **Phase 2 — TTP 提取**: 从 ATT&CK actor page + Mandiant report + CISA advisory + The DFIR Report 提取 TTP list (ATT&CK Tactic + Technique + Sub-technique ID).
3. **Phase 3 — Emulation plan**: 用 Atomic Red Team (atomic 单技术 PowerShell / Bash test) + CALDERA (整 chain) + Scythe (商业 lifecycle) 或 自定义 chain 编排.
4. **Phase 4 — 协调 blue team**: 提前与 SOC + Detection Engineering 协调 时间窗口 + scope + ATT&CK ID checklist + telemetry 收集 (Sigma / KQL / SPL).
5. **Phase 5 — Execute emulation**: 按 chain 顺序执行 每步 ATT&CK technique, 实时 record 时间戳 + telemetry data + alert generated.
6. **Phase 6 — Detection gap analysis**: 对每 technique 列 'detected? yes/no + alert source + MTTD (mean time to detect) + MTTR (mean time to respond)', identify gap.
7. **Phase 7 — Reporting + improvement**: report detection gap + Sigma rule 推荐 + KQL hunting query + D3FEND 映射 + roadmap.

- **资深路径**: **跳过** 'just throw red attack at blue and surprise them' 模式 (老 红队 一相情愿炫技 但 blue 没 telemetry baseline 也没 alert tuning 时间 = 浪费 engagement), 提前 协调 detection engineering team 知 哪些 controls / log source 在 (SIEM 是 Splunk / Sentinel / Elastic / Chronicle? EDR 是 CrowdStrike / S1 / Defender / Carbon Black? 哪些 log 已 onboard?); **优化** 用 Vectr (开源 purple team 平台) + Scythe (商业 multi-cycle) + AttackIQ / SafeBreach (BAS) 自动化 multi-cycle emulation (而不是 一次性 manual run), 让 detection 改进 → re-emulate → metric 提升 闭环; **额外** 做 D3FEND 反向 mapping (每 attack technique 对应 D3FEND defense → 哪些 defense 应 deploy / harden / detect / isolate / deceive / evict) + GTI (Google Threat Intelligence / Mandiant Advantage) 集成 + 红蓝复盘 workshop + 培训 detection engineer 写 Sigma + KQL + SPL + 与 CISA / MITRE Center for Threat-Informed Defense (CTID) 项目 (TRAM / Decider / Attack Flow) 集成.

**失败模式 + remediation**:
1. **失败: blue team 提前知道一切 时间窗 + ATT&CK list 导致 'cheating' 高 detection rate**. Remediation: 区分 'announced purple' (透明全 disclose) vs 'unannounced purple' (仅 SOC manager 知), 取决于 engagement objective.
2. **失败: emulation 误真实触发 production incident response**. Remediation: 严格 scope + lab environment 优先 + production 必须 显式 ROE + safe word.
3. **失败: detection 改进 仅停留 在 'we'll fix it' 不落地**. Remediation: 资深 SOP 必须 包括 follow-up retest (2-4 weeks 后 re-emulate verify fix).
4. **失败: 选 不 relevant 的 threat actor (例如 给 制造业 用 APT29 路径)**. Remediation: 用 客户业 horizontal threat model (Mandiant M-Trends / Verizon DBIR + 客户 sector intel) 选 actor.
5. **失败: telemetry log 太多 没人看 noise**. Remediation: 协助 detection engineer prioritize alert + tune fidelity + 不是 增加 100 个 low-fidelity rule.

**OPSEC 注意**:
1. Emulation 工具 (Atomic Red Team / CALDERA agent) 显式标记 (不假装真实 malware), Sigma rule 可识别 emulation source.
2. Emulation lab environment 隔离 production, 必须 production emulation 需 客户 CIO + CISO 双重审批.
3. Captured telemetry / log 加密保管 + 与客户 共享 (而不是 独占) — purple 本质 知识转移.
4. 不 emulate 真实 destructive technique (T1485 Data Destruction / T1486 Encryption) on prod, lab 限定.
5. 报告 redact: 真实 IP / 真实 user / 真实 host 名 必须 mask, 培训用 anonymize.

### 9. Bug Bounty Workflow SOP

**目标 + 适用场景**: 在 公开 bug bounty 平台 (HackerOne / Bugcrowd / Intigriti / YesWeHack / Synack Red Team) 注册 program, 严守 program scope + ROE, 长期持续 monitor + 提交 vulnerability + 收益. 适用于 独立 researcher / red team 个人 side project / 公司 dedicated bug bounty hunter 团队.

**入门 SOP**:
1. **Phase 0 — Program 选定 + 读 ROE**: HackerOne / Bugcrowd / Intigriti 选 program, 严守 scope (in-scope / out-of-scope / rules / 禁止 testing 时段 / payout range / 禁止 自动化扫描 / 禁止 social engineering).
2. **Phase 1 — Asset mapping**: subfinder + amass + chaos (Project Discovery) + cert.sh + Wayback Machine + JSluice (JS 解析) 收集 子域名 + endpoint + parameter, scope 内 资产清单.
3. **Phase 2 — Automated recon**: nuclei (自定义 template) + httpx + naabu + dnsx 自动化 monitoring, 一次扫描后 周期性 monitor 新增 asset.
4. **Phase 3 — Manual 业务逻辑测试**: Burp + Caido 手动 click-through + 业务流程, 找 IDOR / authn bypass / business logic flaw (自动化 工具不擅长).
5. **Phase 4 — Reproduce + impact**: 严格 reproduce step + screenshot / video, write 清晰 impact 描述 (CVSS + 业务 scenario).
6. **Phase 5 — Submit + 沟通**: 用 platform 模板 + 清晰 PoC + remediation 建议, 与 triager 友好沟通 + 不抢 P0.
7. **Phase 6 — Disclosure + 收益**: 等待 triage → accepted → fix → bounty, 公开 disclosure 须 program 同意.

- **资深路径**: **跳过** 大 platform 已 saturated low-hanging fruit (Yahoo / Verizon / Microsoft / Apple / Google / Meta program 都 千 hunter 在 卷, 简单 XSS / IDOR 早被 抢), 选 private invitation-only program (Synack / Bugcrowd private) 或 中小 program 或新 launched program (前 90 天 hunter 少); **优化** monitor change detection (subfinder + cron + diff alert 新增 subdomain → Slack/Telegram notify + cert transparency monitor crt.sh + JS analysis ParamSpider + LinkFinder + GoLinkFinder 自动 fetch JS 找新 endpoint + 自定义 nuclei template) 持续 监控 新 attack surface, 比 一次性 recon ROI 高 10x; **额外** 做 chain (low → medium → critical via combine — 例如 self-XSS + CSRF + IDOR + Account Takeover 单看每个 low/medium combined critical RCE / takeover) + responsible disclosure to ZDI (Zero Day Initiative) / SSD Secure Disclosure 转 broker upgrade payout (broker 通常 payout 5-50x HackerOne) + CVE assignment 申请 + 学术 paper 发表 (USENIX Security / Black Hat) 提升个人 reputation.

**失败模式 + remediation**:
1. **失败: 越界测试 out-of-scope asset 被 program 关闭 + 法律风险**. Remediation: 严守 scope (每次提交前 三次 check), 任何模糊地带 提前 platform support 询问.
2. **失败: 重复 提交 (duplicate) — 别人 已先报**. Remediation: 不可避免, 资深应 转向 unique / 业务逻辑 / 新 asset.
3. **失败: triager 不接受 finding (informative / N/A)**. Remediation: 资深应在 impact 描述强化业务 scenario + 与 triager 礼貌讨论 + escalate if needed.
4. **失败: payment 延迟 / 不公**. Remediation: platform 申诉 + community pressure (Twitter / Discord) 但 不撕逼.
5. **失败: 自动化 scan 过度发请求 触发 platform abuse rule**. Remediation: 严格 rate limit + 在 ROE rule 允许 范围内, 不 burst.

**OPSEC 注意**:
1. 攻击 source 用 隔离 VPS / Cloudflare WARP + 不暴露 个人 home IP.
2. 测试账号专用 (test_bb_hunter_NN), 不混 个人.
3. PoC video / screenshot 不含 自身 个人信息 (browser history / personal account).
4. 不公开 disclose 任何 client-side credential / PII / 商业敏感数据, redact 后再提交.
5. 不向第三方泄漏 program ROE / private invitation 内容 (常 NDA 约束).

### 10. Reporting + Remediation SOP

**目标 + 适用场景**: 把 engagement 期间发现的所有 finding 整理成 客户可执行的 report — Executive Summary (业务风险 + 战略建议) + Technical Findings (详细 CVSS + ATT&CK + repro + remediation + retest) + Appendix (原始 artifact + Sigma + KQL + 整改 roadmap). 适用于 每个 engagement 收尾 / 监管 (PCI / SOC 2 / ISO) 报告 / 内部 audit 报告.

**入门 SOP**:
1. **Phase 1 — Finding 收集**: 从 engagement note (Obsidian / OneNote / Notion / Dradis) 汇总所有 finding, 去重 + 合并.
2. **Phase 2 — CVSS scoring**: 每 finding 用 CVSS v3.1 (现 v4.0 渐推) calculator 算 Base + Temporal + Environmental, 分 Critical / High / Medium / Low / Info.
3. **Phase 3 — ATT&CK mapping**: 每 finding 标 ATT&CK Tactic + Technique + Sub-technique ID.
4. **Phase 4 — Repro steps + screenshot**: 每 finding 写 detailed step-by-step + screenshot + curl command + payload.
5. **Phase 5 — Remediation**: 每 finding 列 短期 mitigation + 长期 fix + reference (NIST / OWASP / vendor).
6. **Phase 6 — Executive Summary**: 1-2 页 business-language summary, 不写技术细节, 写 风险 + 影响 + 战略建议 + roadmap.
7. **Phase 7 — Retest plan**: 标 哪些 finding 需 retest + 时间表 + verification 标准.
8. **Phase 8 — 交付**: PDF + 加密 + 通过 client portal (HackerOne / SafeBase) 或 PGP email + 不通过公共 网盘.

- **资深路径**: **跳过** finding-by-finding laundry list 100 个 Low / Info 灌水 (客户读不下去 + 关键 critical 被掩盖), 按 attack chain 组织 (将 single 'foothold + privesc + lateral + DA' chain 整合为一个故事 + 列附属 finding) + 业务 impact narrative 优先; **优化** 用 PlexTrac / Dradis / AttackForge / Cobalt.io / Hexway Hive 报告模板 自动化 finding tracking + CVSS 计算 + 多 engagement portfolio view (不是 每次 Word 手写 — 重复 50+ engagement 后 ROI 巨大); **额外** 做 detection guidance (每 finding 附 Sigma rule + KQL hunting query + Splunk SPL + Suricata signature 让 detection engineer 立即 deploy) + remediation prioritization (DREAD + business impact 矩阵 + roadmap timeline 90/180/365 day) + 复盘 workshop (与 客户 IT + SOC + AppSec + 高管 各级 现场 walkthrough + Q&A + 培训 detection engineer) + post-engagement metrics tracking (重测 fix rate + recurrence rate + 培训效果).

**失败模式 + remediation**:
1. **失败: 报告交付后 客户读不下去 / 不整改**. Remediation: 资深应 executive summary 优先 + 复盘 workshop 现场 walkthrough + remediation prioritization matrix.
2. **失败: 报告 找回 出现 wrong CVSS score 或 重复 finding**. Remediation: 内部 peer review (二人复核) + CVSS calculator 二次验证.
3. **失败: 报告 含 真实 credential / PII / NTDS dump 数据泄漏风险**. Remediation: redact + partial mask + 仅 客户 CISO 持 完整版 + 加密 PDF + 短期 retention 后销毁.
4. **失败: retest 时 fix 不完整 / 客户已修改 architecture**. Remediation: 提前定义 retest scope + acceptance criteria + 与 客户 contracted retest 单独 SOW.
5. **失败: 客户 不接受 finding 与 工程团队推诿**. Remediation: 资深应 attack scenario + 业务 impact 强化 + 引 CISA KEV / vendor advisory / 监管要求 论证 + escalate to CISO / board if needed.

**OPSEC 注意**:
1. 报告 默认 加密 (PDF AES-256 + 7-zip / age 加密), 不通过 公共 网盘 / 邮件附件 明文.
2. 报告 distribution 严限 (客户 CISO + 直接 stakeholder + 律师 only), 不广发.
3. 报告 retention 政策与 客户合同明确 (通常 90-365 day 后 销毁 + log).
4. Engagement note / artifact / Burp project 加密 archive + retention 后 secure delete (shred / cryptsetup zero).
5. 不在 个人 portfolio / LinkedIn / Twitter 公开 真实客户 finding (即使 anonymize 也可能反推), 仅 CTF / lab finding 可公开.
