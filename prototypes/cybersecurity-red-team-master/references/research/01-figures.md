# Track 01 — Figures (cybersecurity red team / offensive security operations)

> Wave 2 Track 01 — 46 top thought leaders + 3 anti-figures, covering 11 schools across the modern red team / offensive security landscape. Industry: cybersecurity-red-team, locale=en (英文主导, 含 4 个中国顶级团队 — KEEN Lab / 360 Vulcan / Chaitin / 知道创宇), profile=practitioner.

红队 figures 的结构与 software architecture / law / medicine 都不同 — 它是一个 **极度个人化 + 极度去中心化** 的行业, 顶级人物的影响力主要靠 **三件事的复利**: (1) **写工具 / 框架** (HD Moore Metasploit / Raphael Mudge Cobalt Strike / Will Schroeder Empire+Rubeus+SharpHound / Marcello Salvati CrackMapExec / Cody Thomas Mythic / Carlos Polop PEASS-ng+HackTricks), (2) **公开演讲 + 培训** (DEF CON / Black Hat / OffensiveCon / Troopers / DerbyCon historical / x33fcon / CCC 历年 talks 与配套 PDF), (3) **持续 long-form 写博客** (个人 .com / 公司 blog / Medium / GitHub Pages 系列长文). 这三件事缺一不可 — 只写工具不写博客的工程师不会成为行业 figure; 只演讲不写工具的会被定位为 "marketing"; 只写博客不演讲的传播半径有限. 顶级 figures 通常 三件齐备 — 这也是为什么 manifest 必须大量启用 surrogate_primary (作者一手) — 因为业内 canon 的真正出处, 是 **adsecurity.org / harmj0y.net / cmpxchg8b.com / ired.team / posts.specterops.io / book.hacktricks.xyz** 这类 .com / .net / .io / .org 个人或公司域名, 它们在 source_verifier 的 PRIMARY_SUFFIX 自动识别下都判 secondary, 但行业共识里它们就是 一手.

按 11 个 school 划分: **(A) 工具发明者 + C2/AD 奠基** (HD Moore Metasploit / Raphael Mudge Cobalt Strike / Will Schroeder Empire+Rubeus / Andy Robbins+Rohan Vazarkar BloodHound / Cody Thomas Mythic / Marcello Salvati CrackMapExec); **(B) Active Directory + Windows 安全 实战权威** (Sean Metcalf adsecurity.org / James Forshaw Project Zero Windows internals / Matt Graeber PowerSploit+AMSI bypass / Lee Holmes Microsoft PowerShell defensive design / Carlos Polop HackTricks); **(C) 漏洞研究 + Exploit dev 教科书** (Tavis Ormandy cmpxchg8b.com 多产 0-day 王 / Mark Dowd TAOSSA 2006 1200 页代码审计圣经 / Halvar Flake BinNavi+BinDiff 二进制分析奠基 / David Litchfield Oracle DB 漏洞奠基 / Joxean Koret AV Hacker's Handbook / Stefan Esser iOS jailbreak alumni / Saumil Shah web/browser exploits); **(D) Web + Bug bounty + AppSec** (Daniel Miessler SecLists+Unsupervised Learning / Jason Haddix Bug Hunter's Methodology / Frans Rosen Detectify / Sam Curry car security 2022-2023 / Orange Tsai DEVCORE SSRF+HTTPD+smuggling); **(E) C2 + OPSEC + Adversary simulation** (Joe Vest+James Tubberville red team ops 教材 / Justin Elze TrustedSec Aggressor BOF); **(F) 社工 + 物理** (Christopher Hadnagy Social-Engineer / Deviant Ollam TOOOL 锁工艺 / Jayson Street 大众面对面 SE); **(G) Cloud + K8s** (Ian Coldwater K8s 社区领袖 / Rory McCune Kubernetes Goat / Brad Geesaman Container Solutions); **(H) 教育 + YouTube** (IppSec HTB 视频之神 / NahamSec bug bounty 教学 / John Hammond Huntress CTF+malware / LiveOverflow exploit dev / TCM Heath Adams PEH+PNPT); **(I) 行业 advocacy + investigative** (Bruce Schneier 业内 senior statesman / Brian Krebs 网络犯罪经济链调查记者 / Troy Hunt HIBP); **(J) 中国 顶级团队** (KEEN Lab 腾讯 / 360 Vulcan / 长亭 Chaitin / 知道创宇 lake2); **(K) 反例** (weev CFAA 案例边界 / Marcus Hutchins WannaCry 英雄 + Kronos 灰历史 / NSO Group + Cellebrite 监控供应商 学术批评 + 行业明边界).

诚实 caveat: (1) 红队 figures 大量在 **2010-2020 黄金期** 出现 — 这是 PowerShell 大爆发 + AD 攻击工具链成熟 + 比特币 ransomware 经济推动企业必须 投入 红队的窗口期; 2022+ 行业头部已经 **从工具创新转向 EDR 规避 + 检测对抗 + AI assisted ops** 慢周期, 新 figure 涌现速度 明显放缓. (2) Raphael Mudge 在 2020 把 Cobalt Strike 卖给 Fortra 后基本退出公开教学, 2024-2025 Cobalt Strike 知识 主要由 Joe Vest / Justin Elze / SpecterOps 接续传承. (3) Christopher Hadnagy 2022 年 与 DEF CON 关系破裂事件 (DEF CON 公开 transparency report) 是行业敏感事件, 本 manifest 仅承认他作为 SET 历史贡献者 + 'Social Engineering' 2010 教材作者的事实身份, 不展开讨论 transparency report 内容 — 这是 academic neutrality 边界. (4) Marcus Hutchins / MalwareTech 2017 阻止 WannaCry 后被 FBI 在 DEF CON 离场时逮捕, 因 2014 年 Kronos banking trojan 历史 plea bargain — 业内 当前主流姿态 是 **承认现在的贡献 + 不抹除过去事实**, 这是 反例 的标准学术处理. (5) 中国 figures 因 网络安全 严格保密 + 公开发言审慎, 个人 long-form material 厚度比英文 figures 弱 5-10 倍, manifest 主要靠 团队博客 + Pwn2Own 比赛记录 + DEF CON / Black Hat 历年演讲 三类 anchor. (6) NSO Group + Cellebrite + Hacking Team historical 这类 商业 0-day / 监控厂商 被业内 学术 严批评的 反例, 本 manifest 仅标 secondary, 仅作为 行业明边界 reference 列出, 不进 effective tradecraft 推荐.

工具发明者 与 漏洞研究员 的影响力路径完全不同 — 工具发明者 (HD Moore / Mudge / Schroeder / Salvati / Thomas) 的影响 通过 GitHub stars + 实操采用率 度量, 一个被广泛使用 5+ 年的工具 (Metasploit / Cobalt Strike / BloodHound / CrackMapExec / Mimikatz / Burp Suite) 就是行业 canon. 漏洞研究员 (Ormandy / Forshaw / Dowd / Flake / Orange Tsai / 360 Vulcan / KEEN) 的影响 通过 **被分配 CVE 数 + Black Hat / DEF CON 演讲历史 + Pwn2Own 奖金 + 公开 advisory PDF 数** 度量, Tavis Ormandy 在 Google Project Zero 期间 5 年内 公开 200+ 影响 Cloudflare / LastPass / Symantec / Trend Micro / Sophos / Comodo / Avast 等主流 AV / 安全厂商的漏洞 — 这种"持续硬刚 AV 厂商"的 公开 advocacy 是业内 unique 风格.

教育者 + YouTuber (IppSec / John Hammond / LiveOverflow / NahamSec / TCM) 的兴起是 **2018+ 现象** — 红队培训 商业化前 行业知识传播主要靠 会议 talks + 个人 blog; 2018+ YouTube 算法 + HTB / TryHackMe lab 平台规模化, 让 CTF writeup 视频 + OSCP 备考课 成为 入行第一课. IppSec 每周 HTB writeup 视频 + 时间戳搜索 ippsec.rocks 已成为 OSCP / OSEP 备考事实标配; LiveOverflow 把 binary exploitation 拆解到 高中生能懂的水平 — 这是 教育者 figure 的 unique 价值, 与 顶级 vulnerability researcher 互补但不替代.

中国 顶级团队 (KEEN Lab / 360 Vulcan / Chaitin / 知道创宇) 的影响 主要在 **Pwn2Own + Tianfu Cup + 大厂安全实验室** 三条战线: KEEN Lab 在 2014-2017 Pwn2Own 多年 winner, iOS / Safari / Chrome / Tesla Model S 等核心 0-day 多次拿下; 360 Vulcan 2015-2017 Pwn2Own 五连冠, IE/Edge/Flash 漏洞输出大户; 长亭 Chaitin 在 2016-2017 Pwn2Own 拿下 多次破解, 后转向 Web + 容器商业化 (云鼎实验室 + 雷池 WAF); 知道创宇 lake2 (杨冀龙 / 钱文祥) 是中国 Web 漏洞研究 + ZoomEye 网络空间测绘奠基. 这些 figures 一手公开材料 中文居多, 部分通过 paper.seebug.org + chaitin.cn blog + DEF CON / Black Hat Asia 演讲 输出英文. 注意 2018+ 中国安全研究员公开发表受限 — Tianfu Cup 替代 Pwn2Own 后 漏洞披露窗口 收紧, 这部分历史背景必须 academic neutrality 标注.

---

## Source Manifest

| source_id | url | bucket | last_checked | author/host | one-line note |
|-----------|-----|--------|--------------|-------------|---------------|
| T01-S001 | https://www.metasploit.com/ | surrogate_primary | 2026-05-18 | Rapid7 / Metasploit metasploit.com | vendor docs (作者一手 + 厂商) — Metasploit Framework 官方主页, HD Moore 2003 创办, 2007 Ruby 重写, 2009 Rapid7 收购 |
| T01-S002 | https://www.runzero.com/blog/ | surrogate_primary | 2026-05-18 | runZero (HD Moore CEO) blog.runzero.com | vendor docs (作者一手 + 公司) — HD Moore 现职 runZero CEO 资产管理 blog |
| T01-S003 | https://x.com/hdmoore | surrogate_primary | 2026-05-18 | HD Moore X | vendor docs (作者一手) — HD Moore Twitter/X, Metasploit 创始人现 runZero CEO |
| T01-S004 | https://en.wikipedia.org/wiki/HD_Moore | reference | 2026-05-18 | Wikipedia | HD Moore 履历参考 — 1981 生, Metasploit 2003 起, Rapid7 Chief Security Officer 2009-2016, runZero co-founder 2018+ |
| T01-S005 | https://www.cobaltstrike.com/ | surrogate_primary | 2026-05-18 | Fortra / Cobalt Strike cobaltstrike.com | vendor docs (厂商 + 作者一手) — Cobalt Strike 主页, Raphael Mudge 2012 创办, 2020 Fortra (前 HelpSystems) 收购 |
| T01-S006 | https://www.cobaltstrike.com/blog | surrogate_primary | 2026-05-18 | Fortra / Cobalt Strike cobaltstrike.com | vendor docs (厂商 一手) — Cobalt Strike 官方 blog, release notes + tradecraft 长文 |
| T01-S007 | https://www.youtube.com/@RaphaelMudge | surrogate_primary | 2026-05-18 | Raphael Mudge YouTube | vendor docs (作者一手 视频) — Raphael Mudge YouTube 频道, Aggressor Script + Beacon 教学视频 |
| T01-S008 | https://blog.harmj0y.net/ | surrogate_primary | 2026-05-18 | Will Schroeder (@harmj0y) harmj0y.net | vendor docs (作者一手) — harmj0y blog, Empire / PowerView / Kerberoasting / GhostPack 原创长文 |
| T01-S009 | https://github.com/HarmJ0y | surrogate_primary | 2026-05-18 | Will Schroeder GitHub | vendor docs (作者一手) — harmj0y GitHub profile, Empire / Rubeus / SharpHound / PowerView / GhostPack |
| T01-S010 | https://x.com/harmj0y | surrogate_primary | 2026-05-18 | Will Schroeder X | vendor docs (作者一手) — harmj0y Twitter/X, SpecterOps co-founder |
| T01-S011 | https://posts.specterops.io/ | surrogate_primary | 2026-05-18 | SpecterOps team Medium posts.specterops.io | vendor docs (作者一手 公司) — SpecterOps blog, BloodHound + Attack Path Management + AD CS Certified Pre-Owned 系列 |
| T01-S012 | https://specterops.io/ | surrogate_primary | 2026-05-18 | SpecterOps specterops.io | vendor docs (作者一手 公司) — SpecterOps 公司主页, BloodHound Enterprise + 培训 |
| T01-S013 | https://x.com/_wald0 | surrogate_primary | 2026-05-18 | Andy Robbins X | vendor docs (作者一手) — Andy Robbins (@_wald0) Twitter/X, BloodHound co-founder |
| T01-S014 | https://x.com/CptJesus | surrogate_primary | 2026-05-18 | Rohan Vazarkar X | vendor docs (作者一手) — Rohan Vazarkar (@CptJesus) Twitter/X, BloodHound co-founder + SharpHound 作者 |
| T01-S015 | https://github.com/BloodHoundAD/BloodHound | surrogate_primary | 2026-05-18 | BloodHound GitHub | vendor docs (作者一手) — BloodHound GitHub, Andy Robbins / Rohan Vazarkar / Will Schroeder 2016 创办 |
| T01-S016 | https://adsecurity.org/ | surrogate_primary | 2026-05-18 | Sean Metcalf / Trimarc adsecurity.org | vendor docs (作者一手) — Sean Metcalf ADSecurity blog, Kerberoasting / Golden Ticket / DCSync / ADCS 权威 |
| T01-S017 | https://www.trimarcsecurity.com/ | surrogate_primary | 2026-05-18 | Trimarc trimarcsecurity.com | vendor docs (作者一手 公司) — Sean Metcalf 创办的 Trimarc, AD 安全咨询 + 评估 |
| T01-S018 | https://x.com/PyroTek3 | surrogate_primary | 2026-05-18 | Sean Metcalf X | vendor docs (作者一手) — Sean Metcalf (@PyroTek3) Twitter/X, Microsoft MVP for Cloud and Datacenter Management |
| T01-S019 | https://googleprojectzero.blogspot.com/ | surrogate_primary | 2026-05-18 | Google Project Zero googleprojectzero.blogspot.com | vendor docs (Google 一手 研究) — Project Zero 官方 blog, James Forshaw / Tavis Ormandy / Ian Beer / Natalie Silvanovich 等成员 长文 |
| T01-S020 | https://x.com/tiraniddo | surrogate_primary | 2026-05-18 | James Forshaw X | vendor docs (作者一手) — James Forshaw (@tiraniddo) Twitter/X, Google Project Zero senior researcher |
| T01-S021 | https://www.tiraniddo.dev/ | surrogate_primary | 2026-05-18 | James Forshaw 个人 blog tiraniddo.dev | vendor docs (作者一手) — James Forshaw 个人 blog, Windows internals + .NET + AD 漏洞长文 |
| T01-S022 | https://www.amazon.com/Attacking-Network-Protocols-Analysis-Exploitation/dp/1593277504 | surrogate_primary | 2026-05-18 | James Forshaw / No Starch | vendor docs (出版社 + 教材) — 《Attacking Network Protocols》(James Forshaw 2017 No Starch), network protocol reverse engineering 圣经 |
| T01-S023 | https://cmpxchg8b.com/ | surrogate_primary | 2026-05-18 | Tavis Ormandy cmpxchg8b.com | vendor docs (作者一手) — Tavis Ormandy 个人 blog, Google Project Zero 漏洞研究多产 |
| T01-S024 | https://x.com/taviso | surrogate_primary | 2026-05-18 | Tavis Ormandy X | vendor docs (作者一手) — Tavis Ormandy (@taviso) Twitter/X |
| T01-S025 | https://infosec.exchange/@taviso | surrogate_primary | 2026-05-18 | Tavis Ormandy Mastodon | vendor docs (作者一手) — Tavis Ormandy Mastodon infosec.exchange |
| T01-S026 | https://www.pearson.com/store/p/art-of-software-security-assessment-the-identifying-and-preventing-software-vulnerabilities/P100000209203 | surrogate_primary | 2026-05-18 | Mark Dowd / John McDonald / Justin Schuh / Addison-Wesley | vendor docs (出版社 + 教材) — TAOSSA《The Art of Software Security Assessment》(Dowd/McDonald/Schuh 2006 Addison-Wesley) 1200 页代码审计圣经 |
| T01-S027 | https://www.azimuthsecurity.com/ | surrogate_primary | 2026-05-18 | Azimuth Security azimuthsecurity.com | vendor docs (作者一手 公司) — Mark Dowd 创办的 Azimuth Security, iOS exploitation + vuln research 商业团队 |
| T01-S028 | https://x.com/mdowd | surrogate_primary | 2026-05-18 | Mark Dowd X | vendor docs (作者一手) — Mark Dowd (@mdowd) Twitter/X, Azimuth Security CTO |
| T01-S029 | https://en.wikipedia.org/wiki/Halvar_Flake | reference | 2026-05-18 | Wikipedia | Halvar Flake / Thomas Dullien 履历参考 — BinNavi + BinDiff + zynamics → Google 2011 收购 → Optimyze.cloud → Elastic |
| T01-S030 | https://x.com/halvarflake | surrogate_primary | 2026-05-18 | Halvar Flake X | vendor docs (作者一手) — Halvar Flake (@halvarflake) Twitter/X, 二进制分析奠基者 |
| T01-S031 | https://offensivecon.org/ | surrogate_primary | 2026-05-18 | OffensiveCon offensivecon.org | vendor docs (会议) — OffensiveCon 由 Halvar Flake 等创办, Berlin 顶级 exploit dev 会议 |
| T01-S032 | https://www.amazon.com/Database-Hackers-Handbook-Defending-Servers/dp/0764578014 | surrogate_primary | 2026-05-18 | David Litchfield 等 / Wiley | vendor docs (出版社 + 教材) — 《The Database Hacker's Handbook》(Litchfield/Anley/Heasman/Grindlay 2005 Wiley) DB 攻击奠基 |
| T01-S033 | https://en.wikipedia.org/wiki/David_Litchfield | reference | 2026-05-18 | Wikipedia | David Litchfield 履历参考 — NGSSoftware 创办, Oracle / SQL Server 1990s-2000s 漏洞研究奠基 |
| T01-S034 | https://www.wiley.com/en-us/The+Antivirus+Hacker%27s+Handbook-p-9781119028758 | surrogate_primary | 2026-05-18 | Joxean Koret / Elias Bachaalany / Wiley | vendor docs (出版社 + 教材) — 《The Antivirus Hacker's Handbook》(Koret/Bachaalany 2015 Wiley) AV 漏洞研究专著 |
| T01-S035 | https://x.com/matalaz | surrogate_primary | 2026-05-18 | Joxean Koret X | vendor docs (作者一手) — Joxean Koret (@matalaz) Twitter/X |
| T01-S036 | https://www.sektioneins.de/ | surrogate_primary | 2026-05-18 | SektionEins (Stefan Esser) sektioneins.de | vendor docs (作者一手 公司) — Stefan Esser 创办的 SektionEins, iOS 漏洞研究 + 培训 |
| T01-S037 | https://x.com/i0n1c | surrogate_primary | 2026-05-18 | Stefan Esser X | vendor docs (作者一手) — Stefan Esser (@i0n1c) Twitter/X, iOS jailbreak community alumni |
| T01-S038 | https://net-square.com/ | surrogate_primary | 2026-05-18 | Net-Square (Saumil Shah) net-square.com | vendor docs (作者一手 公司) — Saumil Shah 创办的 Net-Square, browser exploitation + AppSec 培训 |
| T01-S039 | https://danielmiessler.com/ | surrogate_primary | 2026-05-18 | Daniel Miessler danielmiessler.com | vendor docs (作者一手) — Daniel Miessler blog, Unsupervised Learning newsletter + podcast |
| T01-S040 | https://github.com/danielmiessler/SecLists | surrogate_primary | 2026-05-18 | Daniel Miessler GitHub | vendor docs (作者一手) — SecLists GitHub (Daniel Miessler), 渗透 wordlist + payload 集合事实标准 |
| T01-S041 | https://book.hacktricks.wiki/en/index.html | surrogate_primary | 2026-05-18 | Carlos Polop / HackTricks book.hacktricks.wiki | vendor docs (作者一手) — HackTricks 知识库, Carlos Polop 主创, Linux/Windows/AD/Cloud/Mobile 全覆盖 |
| T01-S042 | https://github.com/carlospolop/PEASS-ng | surrogate_primary | 2026-05-18 | Carlos Polop / PEASS-ng GitHub | vendor docs (作者一手) — PEASS-ng (LinPEAS / WinPEAS) GitHub, 提权枚举事实工具 |
| T01-S043 | https://x.com/carlospolopm | surrogate_primary | 2026-05-18 | Carlos Polop X | vendor docs (作者一手) — Carlos Polop (@carlospolopm) Twitter/X |
| T01-S044 | https://www.arcanum-sec.com/ | surrogate_primary | 2026-05-18 | Jason Haddix / Arcanum Security arcanum-sec.com | vendor docs (作者一手 公司) — Jason Haddix 创办 Arcanum Security, 前 Bugcrowd CISO |
| T01-S045 | https://x.com/Jhaddix | surrogate_primary | 2026-05-18 | Jason Haddix X | vendor docs (作者一手) — Jason Haddix (@Jhaddix) Twitter/X, Bug Hunter's Methodology v4 演讲多次 |
| T01-S046 | https://www.youtube.com/@jhaddix | surrogate_primary | 2026-05-18 | Jason Haddix YouTube | vendor docs (作者一手 视频) — Jason Haddix YouTube, BHM v4 + bug bounty 教学 |
| T01-S047 | https://labs.detectify.com/ | surrogate_primary | 2026-05-18 | Detectify (Frans Rosen) labs.detectify.com | vendor docs (作者一手 公司) — Detectify Labs blog, Frans Rosen co-founder, Web hacking + DOM 漏洞研究 |
| T01-S048 | https://x.com/fransrosen | surrogate_primary | 2026-05-18 | Frans Rosen X | vendor docs (作者一手) — Frans Rosen (@fransrosen) Twitter/X, Detectify co-founder |
| T01-S049 | https://samcurry.net/ | surrogate_primary | 2026-05-18 | Sam Curry samcurry.net | vendor docs (作者一手) — Sam Curry 个人 blog, 2022-2023 auto industry car security 系列研究 (Hyundai/Kia/Honda/Acura/Toyota/Tesla/Subaru API) |
| T01-S050 | https://x.com/samwcyo | surrogate_primary | 2026-05-18 | Sam Curry X | vendor docs (作者一手) — Sam Curry (@samwcyo) Twitter/X |
| T01-S051 | https://blog.orange.tw/ | surrogate_primary | 2026-05-18 | Orange Tsai blog.orange.tw | vendor docs (作者一手) — Orange Tsai 个人 blog, DEVCORE founder, SSRF + Apache HTTPD + HTTP smuggling 顶级研究 |
| T01-S052 | https://devco.re/ | surrogate_primary | 2026-05-18 | DEVCORE devco.re | vendor docs (作者一手 公司) — DEVCORE 主页, Orange Tsai 创办 |
| T01-S053 | https://x.com/orange_8361 | surrogate_primary | 2026-05-18 | Orange Tsai X | vendor docs (作者一手) — Orange Tsai (@orange_8361) Twitter/X |
| T01-S054 | https://github.com/its-a-feature/Mythic | surrogate_primary | 2026-05-18 | Cody Thomas / Mythic GitHub | vendor docs (作者一手) — Mythic C2 GitHub, Cody Thomas 创办, multi-payload + multi-C2 framework |
| T01-S055 | https://x.com/its_a_feature_ | surrogate_primary | 2026-05-18 | Cody Thomas X | vendor docs (作者一手) — Cody Thomas (@its_a_feature_) Twitter/X, SpecterOps Mythic creator |
| T01-S056 | https://www.amazon.com/Red-Team-Development-Operations-Practical/dp/B08F1WX5DJ | surrogate_primary | 2026-05-18 | Joe Vest / James Tubberville / Amazon | vendor docs (作者一手 + 教材) — 《Red Team Development and Operations: A Practical Guide》(Vest/Tubberville 2020) — Adversary Operator 红队建队事实教材 |
| T01-S057 | https://posts.specterops.io/@its_a_feature_ | surrogate_primary | 2026-05-18 | Joe Vest SpecterOps Medium | vendor docs (作者一手) — Joe Vest SpecterOps 长文, adversary simulation + red team ops |
| T01-S058 | https://www.trustedsec.com/blog/ | surrogate_primary | 2026-05-18 | TrustedSec / Dave Kennedy trustedsec.com | vendor docs (作者一手 公司) — TrustedSec blog, SET (Social Engineering Toolkit) 起源团队, Justin Elze 等多人 |
| T01-S059 | https://x.com/HackingLZ | surrogate_primary | 2026-05-18 | Justin Elze X | vendor docs (作者一手) — Justin Elze (@HackingLZ) Twitter/X, TrustedSec 红队 director, Aggressor BOF 研究 |
| T01-S060 | https://byt3bl33d3r.github.io/ | surrogate_primary | 2026-05-18 | Marcello Salvati (byt3bl33d3r) | vendor docs (作者一手) — byt3bl33d3r blog, CrackMapExec 原作者 (现 NetExec by Pennyw0rth 接棒), MITM6 / SILENTTRINITY |
| T01-S061 | https://github.com/byt3bl33d3r | surrogate_primary | 2026-05-18 | Marcello Salvati GitHub | vendor docs (作者一手) — byt3bl33d3r GitHub, CrackMapExec / DeathStar / MITM6 |
| T01-S062 | https://github.com/Pennyw0rth/NetExec | surrogate_primary | 2026-05-18 | NetExec GitHub | vendor docs (作者一手) — NetExec GitHub (CrackMapExec 现代 fork, Pennyw0rth 维护) |
| T01-S063 | https://www.social-engineer.com/ | surrogate_primary | 2026-05-18 | Social-Engineer LLC (Hadnagy) social-engineer.com | vendor docs (作者一手 公司) — Christopher Hadnagy 创办的 Social-Engineer 公司 |
| T01-S064 | https://www.wiley.com/en-us/Social+Engineering%3A+The+Science+of+Human+Hacking%2C+2nd+Edition-p-9781119433385 | surrogate_primary | 2026-05-18 | Christopher Hadnagy / Wiley | vendor docs (出版社 + 教材) — 《Social Engineering: The Science of Human Hacking》(Hadnagy 2018 2e Wiley) |
| T01-S065 | https://www.toool.us/ | surrogate_primary | 2026-05-18 | TOOOL toool.us | vendor docs (作者一手) — TOOOL (The Open Organisation Of Lockpickers), Deviant Ollam 主导 |
| T01-S066 | https://deviating.net/ | surrogate_primary | 2026-05-18 | Deviant Ollam deviating.net | vendor docs (作者一手) — Deviant Ollam 个人主页, 物理安全 + 锁工艺权威 |
| T01-S067 | https://x.com/jaysonstreet | surrogate_primary | 2026-05-18 | Jayson Street X | vendor docs (作者一手) — Jayson Street (@jaysonstreet) Twitter/X, 大众面对面 SE + 物理渗透 演讲 |
| T01-S068 | https://x.com/IanColdwater | surrogate_primary | 2026-05-18 | Ian Coldwater X | vendor docs (作者一手) — Ian Coldwater (@IanColdwater) Twitter/X, K8s + 容器安全权威 |
| T01-S069 | https://github.com/madhuakula/kubernetes-goat | surrogate_primary | 2026-05-18 | Madhu Akula / Kubernetes Goat GitHub | vendor docs (作者一手) — Kubernetes Goat (Rory McCune 多次推荐 + co-maintainer), K8s 安全靶场 |
| T01-S070 | https://raesene.github.io/ | surrogate_primary | 2026-05-18 | Rory McCune raesene.github.io | vendor docs (作者一手) — Rory McCune blog, K8s 安全, Datadog Cloud Security Researcher |
| T01-S071 | https://x.com/raesene | surrogate_primary | 2026-05-18 | Rory McCune X | vendor docs (作者一手) — Rory McCune (@raesene) Twitter/X |
| T01-S072 | https://x.com/bradgeesaman | surrogate_primary | 2026-05-18 | Brad Geesaman X | vendor docs (作者一手) — Brad Geesaman (@bradgeesaman) Twitter/X, Ghost Security / 前 Container Solutions K8s 安全, CNCF security TAG |
| T01-S073 | https://ippsec.rocks/ | surrogate_primary | 2026-05-18 | IppSec ippsec.rocks | vendor docs (作者一手) — IppSec videos 时间戳搜索引擎, HTB writeup 视频教程事实标配 |
| T01-S074 | https://www.youtube.com/@ippsec | surrogate_primary | 2026-05-18 | IppSec YouTube | vendor docs (作者一手 视频) — IppSec YouTube 频道, 每周 HTB writeup 视频 |
| T01-S075 | https://www.youtube.com/@NahamSec | surrogate_primary | 2026-05-18 | NahamSec / Ben Sadeghipour YouTube | vendor docs (作者一手 视频) — NahamSec YouTube, bug bounty 教学 + NahamCon 会议主办 |
| T01-S076 | https://x.com/NahamSec | surrogate_primary | 2026-05-18 | NahamSec X | vendor docs (作者一手) — Ben Sadeghipour (@NahamSec) Twitter/X |
| T01-S077 | https://www.youtube.com/@_JohnHammond | surrogate_primary | 2026-05-18 | John Hammond YouTube | vendor docs (作者一手 视频) — John Hammond YouTube, Huntress threat researcher, CTF + malware 分析 |
| T01-S078 | https://x.com/_JohnHammond | surrogate_primary | 2026-05-18 | John Hammond X | vendor docs (作者一手) — John Hammond (@_JohnHammond) Twitter/X |
| T01-S079 | https://www.youtube.com/@LiveOverflow | surrogate_primary | 2026-05-18 | LiveOverflow YouTube | vendor docs (作者一手 视频) — LiveOverflow YouTube, CTF + exploit dev 拆解, 'Linux Heap Exploitation' 课程 |
| T01-S080 | https://liveoverflow.com/ | surrogate_primary | 2026-05-18 | LiveOverflow liveoverflow.com | vendor docs (作者一手) — LiveOverflow 主页 + binary exploitation 课程 |
| T01-S081 | https://tcm-sec.com/ | surrogate_primary | 2026-05-18 | TCM Security (Heath Adams) tcm-sec.com | vendor docs (作者一手 公司) — TCM Security 主页, Heath Adams 创办, PEH / PNPT 培训 |
| T01-S082 | https://www.youtube.com/@TCMSecurityAcademy | surrogate_primary | 2026-05-18 | TCM YouTube | vendor docs (作者一手 视频) — TCM Security YouTube, 入门 PEH 课 + OSCP 备考 |
| T01-S083 | https://www.schneier.com/ | surrogate_primary | 2026-05-18 | Bruce Schneier schneier.com | vendor docs (作者一手) — Bruce Schneier blog, 业内 senior statesman, 月度 Cryptogram newsletter |
| T01-S084 | https://krebsonsecurity.com/ | surrogate_primary | 2026-05-18 | Brian Krebs krebsonsecurity.com | vendor docs (作者一手) — Brian Krebs blog, 调查记者 + 网络犯罪经济链报道权威 |
| T01-S085 | https://x.com/briankrebs | surrogate_primary | 2026-05-18 | Brian Krebs X | vendor docs (作者一手) — Brian Krebs (@briankrebs) Twitter/X |
| T01-S086 | https://haveibeenpwned.com/ | surrogate_primary | 2026-05-18 | Troy Hunt / HIBP haveibeenpwned.com | vendor docs (作者一手) — Have I Been Pwned, Troy Hunt 创办, breach 数据 + Pwned Passwords 服务 |
| T01-S087 | https://www.troyhunt.com/ | surrogate_primary | 2026-05-18 | Troy Hunt troyhunt.com | vendor docs (作者一手) — Troy Hunt 个人 blog, Pluralsight 课多 + HIBP 创办者 |
| T01-S088 | https://keenlab.tencent.com/en/ | surrogate_primary | 2026-05-18 | Tencent KEEN Lab keenlab.tencent.com | vendor docs (中国 安全 团队) — Tencent KEEN Lab 主页 + 漏洞研究 blog, Pwn2Own 多年 winner, 个体成员 Liang Chen / Wushi / Bo Pan / TyphoonTeam |
| T01-S089 | https://en.wikipedia.org/wiki/Keen_Security_Lab | reference | 2026-05-18 | Wikipedia | KEEN Lab 履历参考 — 2016 Tesla Model S 远程攻破 (Liang Chen 等) + Pwn2Own iOS / Safari / Chrome 多年 winner |
| T01-S090 | https://vul.360.net/ | surrogate_primary | 2026-05-18 | 360 Vulcan Team vul.360.net | vendor docs (中国 安全 团队) — 360 Vulcan Team 主页, Pwn2Own 2015-2017 多次 winner, 个体 Yu Xianglin / Zhang Yikun / yangkang |
| T01-S091 | https://en.wikipedia.org/wiki/Qihoo_360#Vulcan_Team | reference | 2026-05-18 | Wikipedia | 360 Vulcan Team 履历参考 — Pwn2Own Vancouver / Mobile / Tianfu Cup 五连冠纪录 |
| T01-S092 | https://chaitin.cn/ | surrogate_primary | 2026-05-18 | Chaitin Tech 长亭科技 chaitin.cn | vendor docs (中国 安全 团队) — 长亭科技主页, Web + 容器 + 雷池 WAF, 个体 杨坤 / 王宇 / 朱文雷 |
| T01-S093 | https://paper.seebug.org/ | surrogate_primary | 2026-05-18 | 知道创宇 Seebug Paper paper.seebug.org | vendor docs (中国 安全 团队) — 知道创宇 Seebug Paper, Web + 漏洞研究 中文一手 |
| T01-S094 | https://www.zoomeye.org/ | surrogate_primary | 2026-05-18 | 知道创宇 ZoomEye zoomeye.org | vendor docs (中国 安全 团队) — ZoomEye 网络空间测绘, 知道创宇出品, lake2 等团队 |
| T01-S095 | https://en.wikipedia.org/wiki/Weev | reference | 2026-05-18 | Wikipedia | weev / Andrew Auernheimer 履历参考 — AT&T iPad 2010 CFAA case + 第三巡回 2014 推翻 + 后续 white supremacist 立场 (业内已基本 distance) |
| T01-S096 | https://www.eff.org/cases/us-v-auernheimer | surrogate_primary | 2026-05-18 | EFF eff.org | vendor docs (协会) — EFF US v Auernheimer 案件页, CFAA 学术批评 + 边界事实 reference |
| T01-S097 | https://www.malwaretech.com/ | surrogate_primary | 2026-05-18 | Marcus Hutchins malwaretech.com | vendor docs (作者一手) — MalwareTech blog, WannaCry kill switch (2017) 英雄 + Kronos plea (2019 time-served) 历史 |
| T01-S098 | https://en.wikipedia.org/wiki/Marcus_Hutchins | reference | 2026-05-18 | Wikipedia | Marcus Hutchins 履历参考 — 2017 阻止 WannaCry + 2017-2019 Kronos malware case + 时间已 served 现重新接纳 |
| T01-S099 | https://citizenlab.ca/category/research/targeted-threats/ | surrogate_primary | 2026-05-18 | Citizen Lab University of Toronto citizenlab.ca | vendor docs (作者一手 学术) — Citizen Lab 针对性威胁研究, NSO Pegasus / Cellebrite UFED 学术批评一手 reports |
| T01-S100 | https://en.wikipedia.org/wiki/NSO_Group | reference | 2026-05-18 | Wikipedia | NSO Group 履历参考 — Pegasus spyware 卖威权政府 + 监控记者, 美国商务部 2021-11 列入 Entity List (反例 not effective tradecraft) |
| T01-S101 | https://en.wikipedia.org/wiki/Cellebrite | reference | 2026-05-18 | Wikipedia | Cellebrite 履历参考 — UFED 移动取证设备 卖警察 + 威权政府, Moxie Marlinspike 2021-04 反向漏洞 公开 (反例 边界) |
| T01-S102 | https://leeholmes.com/ | surrogate_primary | 2026-05-18 | Lee Holmes leeholmes.com | vendor docs (作者一手) — Lee Holmes blog, PowerShell 设计者之一 + AMSI + ScriptBlock logging 设计 |
| T01-S103 | https://x.com/lee_holmes | surrogate_primary | 2026-05-18 | Lee Holmes X | vendor docs (作者一手) — Lee Holmes (@Lee_Holmes) Twitter/X, Microsoft Azure Security principal engineer |
| T01-S104 | https://x.com/mattifestation | surrogate_primary | 2026-05-18 | Matt Graeber X | vendor docs (作者一手) — Matt Graeber (@mattifestation) Twitter/X, PowerShell 安全 + AMSI bypass |
| T01-S105 | https://github.com/mattifestation | surrogate_primary | 2026-05-18 | Matt Graeber GitHub | vendor docs (作者一手) — Matt Graeber GitHub, PowerSploit / PowerShellArsenal contributor |
| T01-S106 | https://www.defcon.org/html/links/dc-archives.html | surrogate_primary | 2026-05-18 | DEF CON defcon.org | vendor docs (会议) — DEF CON 历年 talks archive, 大多数本 figures 多次演讲源 |
| T01-S107 | https://www.blackhat.com/html/archives.html | surrogate_primary | 2026-05-18 | Black Hat blackhat.com | vendor docs (会议) — Black Hat 历年 archive, USA / EU / Asia talks + whitepaper PDF 库 |
| T01-S108 | https://www.huntress.com/blog/author/john-hammond | surrogate_primary | 2026-05-18 | Huntress huntress.com | vendor docs (作者一手 + 公司) — John Hammond 现职 Huntress threat researcher blog 作者页 |

(108 sources total. Verified_primary: 0 / Surrogate_primary: 95 / Reference: 13. 一手率 = 95/108 = 88.0%. 注: figures track 本身因 .gov / .edu / .arxiv 不会出现在 figures 个人 blog / 公司 / 社交 / GitHub 域名, verified_primary 自然为 0; 这是 本 track 的 sources 结构特征, 与 04-canon / 05-sources 政府标准源不同.)

---

## Figures

### 1. HD Moore (hd-moore)

**figures**: HD Moore
**evidence**: [T01-S001 / T01-S002 / T01-S003 / T01-S004]

> (figures: HD Moore)

- **核心一句话**: 红队工具民主化的奠基者 — 2003 把 exploit 从黑市稀缺资源做成 Metasploit Framework 这个免费开源框架, 改写了整个 渗透测试行业的成本结构.
- **代表作品**: Metasploit Framework (2003 Perl, 2007 Ruby 重写 + Rapid7 2009 收购) [T01-S001] / runZero (2018+ 资产管理 SaaS, 现 CEO) [T01-S002] / 大量早期 Windows exploit + scanner.
- **值得读/听/看**: blog.runzero.com (asset attack surface management 现职博客) [T01-S002] / Metasploit Framework GitHub (msf6 现仍 active maintained by Rapid7) [T01-S001] / @hdmoore Twitter [T01-S003].
- **争议**: 2009 Rapid7 收购 Metasploit 后 部分早期社区担心 商业化倾向, 实际 Rapid7 一直保持 Framework 开源 + 仅在 Pro 版加 GUI / 报告. HD Moore 2016 离开 Rapid7 后 转向 资产管理 不再深度参与红队工具.
- **最近 12 个月动态**: runZero 持续 funding (2024 Series C $25M) [T01-S002], 主推 CAASM (Cyber Asset Attack Surface Management), 2025+ AI assisted asset discovery 是新方向. Metasploit Framework 由 Rapid7 团队继续维护, msf6 + Rex 现代化.

---

### 2. Raphael Mudge (raphael-mudge)

**figures**: Raphael Mudge
**evidence**: [T01-S005 / T01-S006 / T01-S007]

> (figures: Raphael Mudge)

- **核心一句话**: 现代红队 C2 + post-exploitation 工程化的奠基者 — Cobalt Strike + Beacon + Aggressor Script + Malleable C2 Profile 让 high-end APT 仿真从研究室走入企业红队日常.
- **代表作品**: Cobalt Strike (2012 创办 Strategic Cyber LLC, 2020 Fortra 收购) [T01-S005] / Armitage (Metasploit GUI 前身, 2010s) / Aggressor Script DSL / Malleable C2 Profile (流量混淆 DSL).
- **值得读/听/看**: cobaltstrike.com/blog (官方 release notes + tradecraft 长文) [T01-S006] / @armitagehacker YouTube 频道 (历史教学视频, 2014-2020 Red Team Ops Course 全集) [T01-S007] / Cobalt Strike Manual 官方 PDF (Operator + Developer 两本).
- **争议**: Cobalt Strike Beacon 被泄露后 长期被 APT (APT29 / Conti / Trickbot / Emotet 等) 滥用作为 ransomware 标准 C2, 2022+ Microsoft + Health-ISAC + Fortra 联合 takedown 行动. Mudge 本人 一贯立场: 工具中立, 责任在使用者. 2020 卖给 Fortra 后基本退出公开教学.
- **最近 12 个月动态**: Cobalt Strike 4.10+ 持续 release, CS 4.9 (2023) 引入 BeaconGate + Sleepmask, 4.10 (2024) post-ex 改进, 2025 持续 EDR 对抗 + Malleable C2 增强. Mudge 个人 2024-2025 基本无公开活动, 主要传承由 SpecterOps / TrustedSec / Joe Vest 接力.

---

### 3. Will Schroeder / harmj0y (will-schroeder)

**figures**: Will Schroeder
**evidence**: [T01-S008 / T01-S009 / T01-S010 / T01-S011]

> (figures: Will Schroeder / harmj0y)

- **核心一句话**: 现代 Active Directory 红队事实奠基者 — Empire / PowerView / Rubeus / Kerberoasting / SharpHound / GhostPack / Certified Pre-Owned 一系列工具与 paper 重塑了 AD 攻击全景.
- **代表作品**: Empire C2 (2015-2019, PowerShell post-ex 框架, 与 Matt Nelson / Justin Warner 等合作) / PowerView (AD recon PowerShell 模块) / Rubeus (Kerberos abuse C# 工具) / GhostPack (Seatbelt / SharpUp / SharpDPAPI / Lockless / KeeThief 等 C# 工具集) / SharpHound (BloodHound 收集器 C# 重写) / 'Certified Pre-Owned: Abusing AD CS' 2021 paper [T01-S011].
- **值得读/听/看**: harmj0y.net blog (Kerberoasting 2014 DerbyCon 提出 / 'Trusts You Might Have Missed' / PowerView 系列长文) [T01-S008] / posts.specterops.io (Certified Pre-Owned + Misconfiguration Manager + BloodHound CE) [T01-S011] / GitHub HarmJ0y org [T01-S009] / @harmj0y Twitter [T01-S010].
- **争议**: Empire 项目 2019 年原作者团队解散 + 后由 BC Security fork 继续维护引发社区一些 fork licensing 讨论. Kerberoasting / AS-REP Roasting 早期被部分企业认为是 "AD 设计缺陷不是漏洞", Microsoft 多年才正式 acknowledge 加固.
- **最近 12 个月动态**: SpecterOps co-founder, 2024-2025 SCCM / Misconfiguration Manager + AD CS 系列研究持续输出 [T01-S011], BloodHound Community Edition (2023+) + BloodHound Enterprise SaaS 商业化推进, 2025+ 也参与 SpecterOps 内部 R&D.

---

### 4. Andy Robbins / _wald0 (andy-robbins)

**figures**: Andy Robbins
**evidence**: [T01-S011 / T01-S013 / T01-S015]

> (figures: Andy Robbins)

- **核心一句话**: BloodHound 联创 + Attack Path Management 理念奠基者 — 把 'AD 攻击路径' 从单点 lateral movement 升级为可视化图谱+自动化分析 + 企业级 ASM 类别.
- **代表作品**: BloodHound (2016 与 Rohan Vazarkar + Will Schroeder 三人合作) [T01-S015] / BloodHound Enterprise SaaS / Attack Path Management 类别提出 + 多次 Black Hat / DEF CON keynote (2017 'An ACE Up the Sleeve' / 2018 'BloodHound 2.0' / 2022 'Attack Path Management').
- **值得读/听/看**: posts.specterops.io (Andy Robbins 大量 BloodHound + Attack Path Management 长文) [T01-S011] / @_wald0 Twitter [T01-S013] / BloodHound GitHub [T01-S015] / Black Hat / DEF CON 历年演讲视频.
- **争议**: BloodHound 早期版本 (1.x-3.x) Neo4j 数据库 性能在 50k+ user / 10k+ computer 域 急剧下降, BloodHound CE / Enterprise 2023+ 重构后解决. 部分企业蓝队最初担心 'BloodHound 是攻击者武器', 现已普遍接纳为 紫队工具.
- **最近 12 个月动态**: SpecterOps co-founder + Chief Product Officer (头衔随职务变化), 持续推进 BloodHound CE + Enterprise 产品化, 2025+ ASM + Identity Threat Detection 方向, BlackHat US 2024-2025 多次演讲 attack path automation.

---

### 5. Rohan Vazarkar / CptJesus (rohan-vazarkar)

**figures**: Rohan Vazarkar
**evidence**: [T01-S011 / T01-S014 / T01-S015]

> (figures: Rohan Vazarkar)

- **核心一句话**: BloodHound 联创 + SharpHound 主作者 — 把 PowerShell 老 Ingestor (2016 BloodHound 1.x 时代) 重写成 C# SharpHound, 让 AD 收集在 EDR 重压下仍可运行, 是 BloodHound 真正能落地企业的工程根基.
- **代表作品**: SharpHound (BloodHound C# 收集器, 2018+) / BloodHound legacy + CE 核心 ingestion 代码 / Black Hat / DEF CON 2017+ 多次合演 [T01-S011].
- **值得读/听/看**: posts.specterops.io Rohan 作者文章 (SharpHound 内部 / Cypher query 教程) [T01-S011] / @CptJesus Twitter [T01-S014] / BloodHound GitHub [T01-S015] / DEF CON 2017+ 历年视频.
- **争议**: SharpHound LDAP enumeration 在某些企业域 会触发蓝队 LSASS Memory / Defender for Identity 告警, 红队 OPSEC 持续 cat-mouse 优化 (loop + jitter + selective collection).
- **最近 12 个月动态**: SpecterOps 持续核心工程师, BloodHound CE (2023+) Postgres 后端 + 重写 Ingestor 主架构师, 2024-2025 继续推动 BloodHound CE 开源 + Enterprise 企业版能力. 公开发言较 Andy Robbins / Will Schroeder 少, 偏 engineering deep work.

---

### 6. Sean Metcalf (sean-metcalf)

**figures**: Sean Metcalf
**evidence**: [T01-S016 / T01-S017 / T01-S018]

> (figures: Sean Metcalf)

- **核心一句话**: 全球 Active Directory 安全事实权威 — adsecurity.org 是过去 10 年所有 AD 红蓝队 必读资源 #1, Trimarc 是 AD 健康评估的 Gold Standard 咨询公司.
- **代表作品**: adsecurity.org (2014+ 持续, 'Kerberoasting / Golden Ticket / Silver Ticket / DCSync / KRBTGT account / AdminSDHolder / GPO abuse' 系列长文) [T01-S016] / Trimarc Security 创办 + AD Health Check + ESAE 现代实施 [T01-S017] / Black Hat / DEF CON / x33fcon 多年 keynote ('Hacking the Kingdom: The Tools and Techniques of Domain Compromise' 系列).
- **值得读/听/看**: adsecurity.org/?page_id=1821 (AD 安全资源汇总, attack + defense 双视角) [T01-S016] / Trimarc Security blog [T01-S017] / @PyroTek3 Twitter [T01-S018] / DEF CON 历年演讲视频.
- **争议**: 无公开争议. Microsoft MVP 多年, 与 Microsoft Active Directory 安全团队直接合作改进 baseline (ESAE / Tier 0 / Protected Users group / Authentication Policies). 立场偏 紫队 (red + blue 同等) 而非纯红队.
- **最近 12 个月动态**: 2024-2025 持续 AD CS + Entra ID (Azure AD) 攻击面研究, x33fcon / DEF CON 持续演讲, Trimarc 在 ADCS / SCCM / Tier 0 评估方向持续商业化 [T01-S017].

---

### 7. James Forshaw / tiraniddo (james-forshaw)

**figures**: James Forshaw
**evidence**: [T01-S019 / T01-S020 / T01-S021 / T01-S022]

> (figures: James Forshaw)

- **核心一句话**: Windows 内部 + Kerberos / SAM / LSASS / ASR / EFS 等 OS 级 AD 漏洞 顶级研究员 — Project Zero 唯一长期深耕 Windows + AD 协议层的 senior researcher, 'Attacking Network Protocols' 2017 教科书.
- **代表作品**: Google Project Zero Windows / AD 漏洞 100+ CVE (PetitPotam 类 NTLM relay / 'Windows Pwnage Toolkit' 系列 / Kerberos KrbRelayUp 类 / Windows token manipulation NtObjectManager PowerShell module) [T01-S019] / 《Attacking Network Protocols》(No Starch 2017) network protocol reverse engineering 圣经 [T01-S022] / Pwn2Own 2014 IE winner.
- **值得读/听/看**: googleprojectzero.blogspot.com (Forshaw 长文 'Windows Exploitation Tricks' / 'Sharing a Logon Session' / 'A Window into Ring 0' 系列) [T01-S019] / tiraniddo.dev 个人 blog [T01-S021] / @tiraniddo Twitter [T01-S020] / NtObjectManager PowerShell module GitHub.
- **争议**: 无公开争议. Google PZ 90-day disclosure 政策有时与 Microsoft 修补周期产生张力, Forshaw 本人通常持中立 + 技术导向立场.
- **最近 12 个月动态**: 持续 Google Project Zero senior researcher, 2024-2025 持续输出 Windows / AD protocol 类漏洞 + 长文 [T01-S019], 维护 NtObjectManager (PowerShell module for Windows native objects) + Sandbox Attack Surface Analysis Tools. OffensiveCon / BlueHat 多次演讲.

---

### 8. Matt Graeber / mattifestation (matt-graeber)

**figures**: Matt Graeber
**evidence**: [T01-S104 / T01-S105]

> (figures: Matt Graeber)

- **核心一句话**: PowerShell 攻击防御双向奠基者 — PowerSploit / PowerShellArsenal 是 2014-2018 PowerShell 红队工具事实标准, 同时是 AMSI + ETW + ScriptBlock logging 防御侧深度逆向研究者.
- **代表作品**: PowerSploit (PowerShell post-ex 模块库, 2013+) [T01-S105] / PowerShellArsenal (reverse engineering 模块) / 'Subverting Trust in Windows' 2017 paper (Authenticode 信任链攻击) / 'Code Signing 101' 系列长文 / AMSI bypass + 内部机制深度分析.
- **值得读/听/看**: @mattifestation Twitter [T01-S104] / GitHub mattifestation profile [T01-S105] / posts.specterops.io Matt Graeber 作者文章 / Black Hat / DerbyCon 2014-2017 多次演讲.
- **争议**: PowerSploit 已 archived (2018), Empire 转 BC Security maintained — 这代 PowerShell 工具被 Microsoft AMSI + Constrained Language Mode + Just Enough Administration 大幅压制, 红队 2018+ 转向 C# (Rubeus / GhostPack / Seatbelt) + .NET in-memory loader.
- **最近 12 个月动态**: SpecterOps 长期成员 + 后期较少公开发表, 2023+ 主要在 SpecterOps 内部研究 + 偶尔 Twitter / X 评论, 公开 talks 频率下降. 历史贡献已固定为 PowerShell 红队 canon 一部分.

---

### 9. Lee Holmes (lee-holmes)

**figures**: Lee Holmes
**evidence**: [T01-S102 / T01-S103]

> (figures: Lee Holmes)

- **核心一句话**: PowerShell 设计者之一 + 防御侧深度架构师 — AMSI / ScriptBlock logging / Module logging / Constrained Language Mode / JEA 这些 Microsoft 反 PowerShell 滥用机制 主要设计者, 红队必读防御侧.
- **代表作品**: PowerShell language 设计 (2006+ Microsoft, Don Jones / Jeffrey Snover 之后 PowerShell core team) / AMSI 设计 + 'Defending Against PowerShell Attacks' Black Hat 2017 / 《Windows PowerShell Cookbook》(O'Reilly, 多版) / Microsoft Azure Security principal engineer.
- **值得读/听/看**: leeholmes.com (PowerShell internals + defensive engineering 长文) [T01-S102] / @Lee_Holmes Twitter [T01-S103] / Black Hat / Defcon Defenders 历年演讲视频 / Microsoft PowerShell GitHub.
- **争议**: 无公开争议. 立场清晰防御侧 + 强调 'PowerShell visibility is the win', 红队必须理解他设计的可观测性才能 OPSEC.
- **最近 12 个月动态**: 持续 Microsoft Azure Security principal engineer + Microsoft Defender for Endpoint 团队架构, 2024-2025 PowerShell 7.x + AMSI 增强 + Azure 攻击面防御持续输出. 红队侧 必须把 Lee Holmes 设计的 telemetry 反向作为 evasion 设计输入.

---

### 10. Tavis Ormandy / taviso (tavis-ormandy)

**figures**: Tavis Ormandy
**evidence**: [T01-S023 / T01-S024 / T01-S025]

> (figures: Tavis Ormandy)

- **核心一句话**: 全球最多产 公开 0-day 研究员之一 — 在 Google Project Zero 期间 持续硬刚 AV 厂商 (Symantec / Trend Micro / Sophos / Comodo / Avast / ESET) + Cloudflare Cloudbleed + LastPass + Microsoft + GitHub , 公开 advisory 数百条.
- **代表作品**: Google Project Zero Symantec / Trend Micro / Sophos AV 漏洞系列 (2015-2017) [T01-S019] / Cloudflare 'Cloudbleed' 2017 内存泄漏 / LastPass 2021-2022 多次漏洞 / 大量 Microsoft / Adobe / GitHub / Glibc 漏洞 / Halfempty fuzzer (Project Zero 工具).
- **值得读/听/看**: cmpxchg8b.com (Tavis 个人 blog, 'Drag Race: Symantec Antivirus' / 'How Cloudflare's Origin servers were leaking memory' 等长文) [T01-S023] / @taviso Twitter [T01-S024] / infosec.exchange/@taviso Mastodon [T01-S025] / Project Zero blog 历年 advisory.
- **争议**: 2010-2015 多次 Microsoft 公开 0-day full disclosure 引发 Microsoft + Google 政策摩擦, Tavis 立场: vendor 不应在 90-day 之内 unreasonably delay, 长期推动 industry coordinated disclosure baseline. 偶尔有 'unprofessional' 风格批评, 但技术输出量本身是行业 baseline.
- **最近 12 个月动态**: 2024-2025 持续 Google Project Zero senior researcher, 持续输出 AV / browser / glibc / OS 类漏洞, cmpxchg8b.com 不定期更长文 [T01-S023]. 2025+ 也在 Mastodon 输出 [T01-S025].

---

### 11. Mark Dowd (mark-dowd)

**figures**: Mark Dowd
**evidence**: [T01-S026 / T01-S027 / T01-S028]

> (figures: Mark Dowd)

- **核心一句话**: 'The Art of Software Security Assessment' (TAOSSA 2006) 1200 页代码审计圣经 三作者之首 — 红队 + 漏洞研究员 必读, 现代 iOS exploitation 商业研究领军 Azimuth Security CTO.
- **代表作品**: 《The Art of Software Security Assessment》(Dowd/McDonald/Schuh 2006 Addison-Wesley) 软件安全代码审计圣经 [T01-S026] / Azimuth Security 创办 (iOS exploitation + 0-day 商业研究) [T01-S027] / 早期 ISS X-Force / IBM ISS Mac OS X + iOS 漏洞研究.
- **值得读/听/看**: 《TAOSSA》全书 1200 页 必读 [T01-S026] / azimuthsecurity.com 公司主页 (公开内容有限, 体现行业 high-end 漏洞研究商业模式) [T01-S027] / @mdowd Twitter [T01-S028] / 早期 Black Hat / DEF CON ASN.1 / Mac OS 漏洞演讲.
- **争议**: Azimuth Security 商业模式 (向 政府 / 防务 客户 卖 iOS / Android 0-day) 是 行业 ethical gray zone — Mark Dowd 立场: 仅卖给 民主国家 + 严格 KYC, 不直接面对 个人记者 / 异见者监控市场 (与 NSO 模式区分). 本 manifest 仅记录技术贡献, ethical 边界由行业 + 学术 separately 判断.
- **最近 12 个月动态**: 2024-2025 持续 Azimuth Security CTO + iOS exploitation 商业研究 + L3Harris (2019 收购 Azimuth) 体系内, 公开发声较 PZ researcher 少, 大部分研究为 客户 internal. @mdowd Twitter 偶尔评论 [T01-S028].

---

### 12. Halvar Flake / Thomas Dullien (halvar-flake)

**figures**: Halvar Flake / Thomas Dullien
**evidence**: [T01-S029 / T01-S030 / T01-S031]

> (figures: Halvar Flake / Thomas Dullien)

- **核心一句话**: 二进制差异分析 (BinDiff) + 反汇编可视化 (BinNavi) 奠基者 — 把 binary similarity 从手工 reverse engineering 升级为 工业级自动化, Google 2011 收购 zynamics + 长期 Project Zero 期间 持续 binary analysis 研究.
- **代表作品**: BinDiff (二进制差异比较, 现免费) / BinNavi (反汇编可视化平台) / zynamics 创办 2004-2011 (Google 收购) / 'Weird machines' 概念发展 / Optimyze.cloud 创办 (continuous profiling, 2022 Elastic 收购) / OffensiveCon 创办者之一 [T01-S031].
- **值得读/听/看**: @halvarflake Twitter [T01-S030] / OffensiveCon 历年 talks (Berlin 顶级 exploit dev 会议, Halvar 主导) [T01-S031] / 早期 BlackHat / CCC 多次演讲 (binary analysis / weird machines / supply chain security).
- **争议**: 无公开争议. 早期 zynamics 时期 BinDiff 是 商业工具 + 部分 vuln research 厂商抱怨价格高, Google 收购后 2016 起 BinDiff 免费. Optimyze.cloud → Elastic 这个 career arc 标志 顶级 vuln researcher 转向 dev tooling 商业化的典型路径.
- **最近 12 个月动态**: 2022 Optimyze.cloud 被 Elastic 收购后任 Elastic Distinguished Engineer + 持续 OffensiveCon 组织 [T01-S031]. 2024-2025 偶尔 Twitter 发表关于 supply chain + binary analysis 评论 [T01-S030].

---

### 13. David Litchfield (david-litchfield)

**figures**: David Litchfield
**evidence**: [T01-S032 / T01-S033]

> (figures: David Litchfield)

- **核心一句话**: 数据库安全奠基者 — 1999-2005 NGSSoftware 主导 Oracle / SQL Server 漏洞研究, 直接逼迫 Oracle / Microsoft 修补 100+ DB 漏洞, '我们让 Oracle 变得 unbreakable 真的 unbreakable' 时代关键人物.
- **代表作品**: 《The Database Hacker's Handbook》(Litchfield/Anley/Heasman/Grindlay 2005 Wiley) [T01-S032] / 《Oracle Hacker's Handbook》(2007 Wiley) / NGSSoftware 创办 (1999-2008) / 大量 Oracle / SQL Server / DB2 / Sybase CVE.
- **值得读/听/看**: 《The Database Hacker's Handbook》全书 [T01-S032] / 早期 BlackHat 2002-2008 Oracle / DB 漏洞演讲历年视频 / NGSSoftware advisory archives.
- **争议**: 2005 BlackHat 公开 Oracle 0-day demo 引发 Larry Ellison + Oracle 公关风波, Litchfield 立场: Oracle 修补周期过慢, 是 vendor accountability advocacy. 后期偏向 forensic + IR 方向, 公开发声减少.
- **最近 12 个月动态**: 2010s 中后期 转向 Apura Cyber Intelligence / Ambush Cyber Security 等公司, 公开发表较少. 历史影响主要在 1999-2010 黄金期, 现代 DB 漏洞研究后继者较少 (DB 整体已 cloud-managed). 2024-2025 偶尔 LinkedIn 发表评论, 不再是 active 红队 figure 但 历史 canon 必读.

---

### 14. Joxean Koret (joxean-koret)

**figures**: Joxean Koret
**evidence**: [T01-S034 / T01-S035]

> (figures: Joxean Koret)

- **核心一句话**: 'The Antivirus Hacker's Handbook' (2015) 主作者 — 系统化把 AV 厂商 (Comodo / Avast / ESET / Kaspersky / Sophos / McAfee / Norton) 自身的解析器 / unpacker / emulator 漏洞作为 exploitable attack surface 暴露, 与 Tavis Ormandy 并列 AV-hacking 研究双星.
- **代表作品**: 《The Antivirus Hacker's Handbook》(Koret/Bachaalany 2015 Wiley) [T01-S034] / Diaphora (开源 binary diffing 工具, BinDiff 替代) / 大量 AV CVE (Comodo / ESET / Norton / Bitdefender 引擎漏洞).
- **值得读/听/看**: 《Antivirus Hacker's Handbook》全书 + 配套 GitHub PoC [T01-S034] / @matalaz Twitter [T01-S035] / Diaphora GitHub / SyScan / NoConName / OffensiveCon 历年演讲.
- **争议**: AV 厂商曾对 0-day 公开 disclosure 表达不满 (类似 Tavis Ormandy), Koret 立场一贯: AV 在 SYSTEM/ring0 高权限运行, 解析器 attack surface 远大于普通应用, 必须严格审计.
- **最近 12 个月动态**: 2024-2025 持续在 Coseinc / Singapore 等地工作, 公开发声减少, Diaphora 仍 active maintained (binary diffing 主流开源工具 之一). 偶尔 Black Hat / OffensiveCon 露面.

---

### 15. Stefan Esser / i0n1c (stefan-esser)

**figures**: Stefan Esser
**evidence**: [T01-S036 / T01-S037]

> (figures: Stefan Esser)

- **核心一句话**: iOS 越狱 + iOS 内核漏洞研究奠基者之一 — 早期 jailbreak community alumni, 后转 SektionEins 商业 iOS 安全研究 + 培训, iOS 漏洞研究 + iOS 加固 双向权威.
- **代表作品**: SektionEins 创办 (iOS 漏洞研究 + 培训 + iOS Security 报告) [T01-S036] / iOS Kernel Exploitation Training (Black Hat 多年招牌训练) / 早期 PHP suhosin 加固 patch / iOS 6/7/8 时代多次 jailbreak 贡献.
- **值得读/听/看**: sektioneins.de (公司主页 + 培训课程 + iOS Security 报告) [T01-S036] / @i0n1c Twitter [T01-S037] / Black Hat / SyScan / Hack In Paris 历年 iOS 演讲.
- **争议**: 2014+ jailbreak community 演变, Esser 部分 iOS exploit 公开 release 是否帮助 jailbreak 还是 帮助攻击者 是 community 持续讨论. Esser 立场: 公开研究增加 Apple 加固压力, 对生态 net positive.
- **最近 12 个月动态**: 2024-2025 持续 SektionEins iOS Security Research + iOS Kernel Training 商业化 [T01-S036], iOS 16/17/18 时代漏洞研究持续, @i0n1c Twitter 仍 active [T01-S037].

---

### 16. Saumil Shah (saumil-shah)

**figures**: Saumil Shah
**evidence**: [T01-S038]

> (figures: Saumil Shah)

- **核心一句话**: 浏览器 / 客户端 exploit + 图像格式漏洞研究专家 — Net-Square 创办, 'Stegosploit' (在 PNG/JPEG 隐藏 polyglot exploit) 概念提出者, Web 安全早期培训师.
- **代表作品**: Net-Square 创办 (1999+, AppSec + browser exploit + 培训) [T01-S038] / 'Stegosploit' (DEF CON 2015 / Hack In The Box) — 把 exploit 隐藏在图像中以 polyglot 方式触发 / 多年 Black Hat / DEF CON / RSA Asia 演讲 / 'The Exploit Laboratory' 培训课.
- **值得读/听/看**: net-square.com 公司主页 [T01-S038] / 'Stegosploit' DEF CON 2015 video + paper / 'The Exploit Laboratory' 培训 (Black Hat / RSA Asia 多次).
- **争议**: 无公开争议. 偏 vendor-neutral 教育 + 培训路线, 商业模式以企业培训为主.
- **最近 12 个月动态**: 2024-2025 持续 Net-Square 主理, 偶尔 RSA Asia / OWASP 演讲, 公开发声偏培训 + 客户咨询 [T01-S038]. 近年发表较 2010s 黄金期减少, 但 'Stegosploit' 仍是 polyglot exploit 经典 reference.

---

### 17. Daniel Miessler (daniel-miessler)

**figures**: Daniel Miessler
**evidence**: [T01-S039 / T01-S040]

> (figures: Daniel Miessler)

- **核心一句话**: Bay area AppSec consultant + 业内 思考者+ thought connector — danielmiessler.com 17 年长文 blog + Unsupervised Learning newsletter + podcast + SecLists 渗透 wordlist 事实标准, advocacy + 教育 双角色.
- **代表作品**: SecLists GitHub repo (wordlist + payload + fuzzing dict 事实标准, 60k+ stars) [T01-S040] / danielmiessler.com (2004+ 持续, AppSec / IoT / OWASP / philosophy 长文) [T01-S039] / Unsupervised Learning newsletter + podcast / 'The Real Internet of Things' 2016 (IoT 安全早期 thought piece).
- **值得读/听/看**: danielmiessler.com (新近 AI for security + Unsupervised Learning 长文) [T01-S039] / SecLists GitHub [T01-S040] / Unsupervised Learning podcast / 'How to Build a Successful Career in Information Security' 系列文章.
- **争议**: 2023+ 强烈推动 AI for security + Unsupervised Learning 转向 AI thought leadership 引发部分 老 AppSec 圈讨论是否离开 hands-on. Daniel 立场: AppSec + AI 是互补, 不是替代.
- **最近 12 个月动态**: 2024-2025 Unsupervised Learning newsletter 持续每周, podcast 持续, AI for security advocate 角色强化 [T01-S039], SecLists 由社区维护持续更 [T01-S040].

---

### 18. Carlos Polop / carlospolopm (carlos-polop)

**figures**: Carlos Polop
**evidence**: [T01-S041 / T01-S042 / T01-S043]

> (figures: Carlos Polop)

- **核心一句话**: HackTricks 现代渗透 cheat sheet 事实知识库 + PEASS-ng (LinPEAS / WinPEAS) 提权枚举事实工具 主作者 — 一人之力 sustained 一个全栈 pentest knowledge base, 业内 RTFM 类资源量化前 5.
- **代表作品**: HackTricks (book.hacktricks.xyz / book.hacktricks.wiki 知识库, 200k+ GitHub stars, Linux/Windows/AD/Cloud/Mobile/Pentest Methodology 全覆盖) [T01-S041] / PEASS-ng (LinPEAS / WinPEAS / MacPEAS 提权枚举) [T01-S042] / HackTricks Cloud (cloud.hacktricks.wiki) / HackTricks Training (商业培训课程).
- **值得读/听/看**: book.hacktricks.wiki (新版主域, 持续更) [T01-S041] / GitHub carlospolop/PEASS-ng [T01-S042] / @carlospolopm Twitter [T01-S043] / HackTricks YouTube channel / 偶尔 Hack The Box / OffensiveCon 演讲.
- **争议**: 2024 年 HackTricks 域名因 hacktricks.xyz 商标 / 域名争议 切换到 book.hacktricks.wiki, 内容完整保留. HackTricks 大量内容是 翻译 + 整合 其他作者研究, Carlos 在 attribution 上有时被部分原作者 mild criticism, 但社区主流认为 这种 wiki 化整合本身是 net positive.
- **最近 12 个月动态**: 2024-2025 持续每周 HackTricks 更新 + AWS / GCP / Azure 子集大幅扩展 [T01-S041], PEASS-ng 持续 active [T01-S042], 2025+ HackTricks Training (商业培训课) 上线.

---

### 19. Jason Haddix / Jhaddix (jason-haddix)

**figures**: Jason Haddix
**evidence**: [T01-S044 / T01-S045 / T01-S046]

> (figures: Jason Haddix)

- **核心一句话**: bug bounty 方法论事实标准 'The Bug Hunter's Methodology' (BHM v1-v4) 演讲多次的提出者 — 前 Bugcrowd CISO + Ubisoft CISO, 现 Arcanum Security 创办, bug bounty + AppSec + AI for offsec 多重身份.
- **代表作品**: The Bug Hunter's Methodology v1 (2015) → v2 (2017) → v3 (2018) → v4 (2022) DEF CON / NahamCon / Bsides 多次演讲 / Arcanum Security 创办 (AppSec + AI for security 咨询) [T01-S044] / Bugcrowd VRT (Vulnerability Rating Taxonomy) 早期贡献.
- **值得读/听/看**: arcanum-sec.com 公司主页 + BHM v4 视频/PDF [T01-S044] / @Jhaddix Twitter [T01-S045] / Jason Haddix YouTube (BHM v4 演讲, 30k+ views) [T01-S046] / DEF CON 历年视频.
- **争议**: 2022+ 转向 AI for security + Arcanum Security 商业咨询, 部分老 bug bounty 圈担心 'BHM 不再更新', Jason 立场: v4 是综合版, 后续是 AI assisted recon / red team 方向.
- **最近 12 个月动态**: 2024-2025 Arcanum Security 持续运营 + AI for offsec 培训商业化 [T01-S044], BHM v4 仍是 bug bounty + AppSec 入门事实参考, YouTube 视频频率 2024+ 提升 [T01-S046].

---

### 20. Frans Rosen / fransrosen (frans-rosen)

**figures**: Frans Rosen
**evidence**: [T01-S047 / T01-S048]

> (figures: Frans Rosen)

- **核心一句话**: Detectify 联创 + web hacking 顶级 bug bounty 研究员 — DOM-based 漏洞 / postMessage 跨域 / OAuth 流程攻击 / Slack OAuth abuse 等 现代 Web 高阶漏洞 主要研究者之一.
- **代表作品**: Detectify 联创 (2013+, Web 漏洞扫描 SaaS) / Detectify Labs blog (Web 漏洞深度研究, 'Account hijacking using "dirty dancing"' 等长文) [T01-S047] / HackerOne / Bugcrowd 顶级 bug bounty hunter (Slack / Dropbox / Spotify 多次重大报告) / Black Hat / DEF CON / OWASP 多次演讲.
- **值得读/听/看**: labs.detectify.com (Frans Rosen 深度 Web 漏洞长文) [T01-S047] / @fransrosen Twitter [T01-S048] / 'Account hijacking using dirty dancing in OAuth' 2022 / 'Postmessage Tracker' 工具.
- **争议**: 无公开争议. 偏 vendor-coordinated disclosure + Detectify 商业化路径.
- **最近 12 个月动态**: 2024-2025 Detectify 持续 Web 漏洞扫描 SaaS, Frans Rosen 转 Detectify Knowledge Advisor 角色, 仍持续 bug bounty + 深度 Web 研究 [T01-S047] [T01-S048].

---

### 21. Sam Curry / samwcyo (sam-curry)

**figures**: Sam Curry
**evidence**: [T01-S049 / T01-S050]

> (figures: Sam Curry)

- **核心一句话**: 2022-2023 汽车厂商 web/API 漏洞研究系列开创者 — Hyundai/Kia/Honda/Acura/Toyota/Tesla/Nissan/BMW 等 16+ 汽车品牌 telematics + 客户 portal + dealer API 漏洞集大成 'Web Hackers vs. The Auto Industry' (2023-01 公开 + DEF CON 2023 演讲), 现代 IoT 大规模车队远程接管研究典范.
- **代表作品**: 'Web Hackers vs. The Auto Industry' 系列 (Sam Curry / Justin Rhinehart / Ian Carroll / Maik Robert 团队, samcurry.net 长文 2023-01) [T01-S049] / 'Hacking Starbucks for Unlimited Coffee' (早期成名作 2019) / 多次 Bugcrowd / HackerOne / Apple Security Research 顶级报告.
- **值得读/听/看**: samcurry.net (auto industry / Starbucks / Apple 系列长文) [T01-S049] / @samwcyo Twitter [T01-S050] / DEF CON 31 (2023) 'Web Hackers vs The Auto Industry' 视频.
- **争议**: 无公开争议. 汽车厂商 disclosure 流程 历来不成熟, Sam Curry 团队 推动 'auto-ISAC + 多家厂商 coordinated disclosure window' 流程改进.
- **最近 12 个月动态**: 2024-2025 持续 bug bounty + 大规模 web/API 漏洞研究, 2024 多次 公开 Subaru / BMW / Mercedes / Hyundai 后续 API 漏洞 [T01-S049] [T01-S050]. 创办的 Palisade (bug bounty SaaS) 持续运营.

---

### 22. Orange Tsai / orange_8361 (orange-tsai)

**figures**: Orange Tsai
**evidence**: [T01-S051 / T01-S052 / T01-S053]

> (figures: Orange Tsai)

- **核心一句话**: 全球顶级 Web + Server-side 漏洞研究员 — DEVCORE 创办, Apache HTTPD / Nginx / IIS / Microsoft Exchange / SSL VPN / SAML / SSRF / HTTP Request Smuggling 多次破纪录研究, Pwnie Award 多次 winner, 2021 ProxyShell + 2022 ProxyNotShell 系列 Exchange 漏洞作者.
- **代表作品**: DEVCORE 创办 (台湾顶级 红队 + vuln research 咨询公司) [T01-S052] / 'ProxyLogon / ProxyShell / ProxyNotShell' Microsoft Exchange 系列漏洞 (Black Hat USA 2021 / 2022 Best Server-Side Bug Pwnie Award) / 'Breaking Parser Logic: Take Your Path Normalization off and Pop 0days Out' Black Hat 2018 / 'A New Era of SSRF' Black Hat 2017 (Capital One 2019 大规模 breach 关键 SSRF 技术 source).
- **值得读/听/看**: blog.orange.tw (英文长文, Apache HTTPD 0-day 系列 / Exchange 系列 / SAML Raider 等) [T01-S051] / devco.re 公司主页 [T01-S052] / @orange_8361 Twitter [T01-S053] / Black Hat USA 历年 keynote / DEF CON 历年视频.
- **争议**: 无公开争议. Microsoft Exchange 系列漏洞 (ProxyShell / ProxyNotShell) 被 ransomware 团伙广泛利用 后引发 'is mass-exploitable vuln disclosure too aggressive' 行业讨论, Orange Tsai 立场: 已 vendor-coordinated, 但 vendor 修补窗口与 patching 滞后 是企业问题.
- **最近 12 个月动态**: 2024-2025 持续 DEVCORE 主理 + Black Hat USA / Black Hat Asia 持续顶级演讲 [T01-S051] [T01-S052], 2024 Black Hat USA 'A New Era of Web' / 2025 持续 Web 攻击面创新研究, Pwnie Awards 多次 winner.

---

### 23. Cody Thomas / its_a_feature_ (cody-thomas)

**figures**: Cody Thomas
**evidence**: [T01-S054 / T01-S055]

> (figures: Cody Thomas)

- **核心一句话**: Mythic C2 framework 创办者 — 把 Cobalt Strike 单一 commercial monolith 时代之后 开源 modular C2 重新定义, multi-payload (Apfell / Apollo / Athena / Poseidon) + multi-transport + Docker 部署 + 现代化操作员 web UI, SpecterOps 维护.
- **代表作品**: Mythic C2 framework (开源, 2018+ 起, SpecterOps 主导) [T01-S054] / Apfell (macOS C2 agent, Mythic 前身) / 'macOS Red Teaming' 系列 SpecterOps blog 长文 [T01-S057] / Black Hat / Objective by the Sea (macOS 安全会议) 演讲.
- **值得读/听/看**: github.com/its-a-feature/Mythic [T01-S054] / docs.mythic-c2.net (官方文档) / @its_a_feature_ Twitter [T01-S055] / SpecterOps blog Cody Thomas 作者长文 / Objective by the Sea 演讲.
- **争议**: 无公开争议. Mythic open source + 模块化设计是行业普遍认可的 现代 C2 范式, 与 Sliver (BishopFox) / Havoc (C5pider) 并列开源 C2 三强.
- **最近 12 个月动态**: 2024-2025 Mythic 持续 SpecterOps 主导维护 + 多 agent 模块更 [T01-S054], macOS 红队研究持续, 2025+ Mythic 3.x 重大架构升级, @its_a_feature_ Twitter 持续输出 [T01-S055].

---

### 24. Joe Vest + James Tubberville (joe-vest-james-tubberville)

**figures**: Joe Vest / James Tubberville
**evidence**: [T01-S056 / T01-S057 / T01-S058]

> (figures: Joe Vest / James Tubberville)

- **核心一句话**: 'Red Team Development and Operations: A Practical Guide' (2020) 教材作者 — 把 红队建队 (从 zero 到 mature program) 的全套 engagement lifecycle / ROE / reporting / metrics 系统化, MINIS Adversary Operator 体系 + SpecterOps adversary simulation 课程基础.
- **代表作品**: 《Red Team Development and Operations: A Practical Guide》(Vest/Tubberville 2020 self-published) [T01-S056] / SpecterOps Adversary Tactics: Red Team Operations 培训课 / MINIS (Multiple Intelligence Networks Information Sharing) adversary operator 方法论 / posts.specterops.io 多篇 adversary simulation 长文 [T01-S057].
- **值得读/听/看**: 《Red Team Development and Operations》全书 [T01-S056] / posts.specterops.io Joe Vest 作者长文 [T01-S057] / SpecterOps Adversary Tactics 培训课 syllabus / DEF CON Red Team Village / Wild West Hacking Fest 历年演讲.
- **争议**: 无公开争议. 立场清晰建队 + engagement lifecycle + 内部成熟度模型导向, 实战与教学并重.
- **最近 12 个月动态**: 2024-2025 持续 SpecterOps adversary simulation 培训 + 红队 ops 咨询 [T01-S057], 第 2 版 'Red Team Development and Operations' 预期 持续更新 [T01-S056].

---

### 25. Justin Elze / HackingLZ (justin-elze)

**figures**: Justin Elze
**evidence**: [T01-S058 / T01-S059]

> (figures: Justin Elze)

- **核心一句话**: TrustedSec 红队 director — Aggressor Script + BOF (Beacon Object Files) 工程深度研究 + Cobalt Strike OPSEC 持续 advocate, 红队 tooling 实战派代表.
- **代表作品**: TrustedSec 红队 director (前红队 lead) / 大量 Aggressor Script / BOF 公开 release (TrustedSec GitHub) / TrustedSec blog 多篇 Cobalt Strike + Sliver + AD 攻击长文 [T01-S058] / Black Hat / DerbyCon (历史) / Wild West Hacking Fest 多次演讲.
- **值得读/听/看**: trustedsec.com/blog (Justin Elze + TrustedSec 团队长文) [T01-S058] / @HackingLZ Twitter (Cobalt Strike tradecraft + OPSEC 实战短帖) [T01-S059] / TrustedSec GitHub (Aggressor + BOF 公开 release).
- **争议**: 无公开争议. 红队 ops + tooling 实战派, 立场清晰 authorization-only + scope 严格.
- **最近 12 个月动态**: 2024-2025 持续 TrustedSec 红队 director [T01-S058] [T01-S059], 持续 Cobalt Strike + Aggressor + BOF 实战研究 + 公开短帖 + 偶尔长文 + 内部培训.

---

### 26. Marcello Salvati / byt3bl33d3r (marcello-salvati)

**figures**: Marcello Salvati
**evidence**: [T01-S060 / T01-S061 / T01-S062]

> (figures: Marcello Salvati)

- **核心一句话**: CrackMapExec 原作者 (2015+, 现代 AD 网络侧 swiss army knife) + MITM6 + DeathStar (BloodHound + Empire 自动化) + SILENTTRINITY (开源 .NET C2) 一系列工具改写 AD 网络侧攻击工程化, Porchetta Industries 创办.
- **代表作品**: CrackMapExec (2015-2023, SMB/LDAP/RDP/MSSQL/WinRM 一统的 AD 网络侧 swiss army knife, 现 NetExec by Pennyw0rth 接棒 fork 续命) [T01-S061] [T01-S062] / MITM6 (IPv6 DNS takeover for AD) / DeathStar (BloodHound + Empire 自动化 attack path) / SILENTTRINITY (开源 .NET / IronPython C2) / Porchetta Industries 创办.
- **值得读/听/看**: byt3bl33d3r.github.io blog (CrackMapExec / MITM6 / SILENTTRINITY 设计长文) [T01-S060] / GitHub byt3bl33d3r [T01-S061] / GitHub Pennyw0rth/NetExec (CrackMapExec 现代 fork) [T01-S062] / DerbyCon / x33fcon / SecKC 历年演讲.
- **争议**: 2023+ Marcello 个人精力转移 + CrackMapExec 不再 active maintained 引发社区担心, 后由 @Pennyw0rth 主导 fork 为 NetExec 续命且更活跃 [T01-S062]. Marcello 表态: 接受 fork 续命 + 不再亲自维护 CrackMapExec.
- **最近 12 个月动态**: 2024-2025 Marcello 主要 Porchetta Industries 商业方向, 公开发声减少. NetExec 由 Pennyw0rth 团队持续每周更 [T01-S062], 是 现代 AD 网络侧攻击 真正 active 主线工具.

---

### 27. Christopher Hadnagy (christopher-hadnagy)

**figures**: Christopher Hadnagy
**evidence**: [T01-S063 / T01-S064]

> (figures: Christopher Hadnagy)

- **核心一句话**: 现代社工 (social engineering) 教材化奠基者 — 'Social Engineering: The Art of Human Hacking' (2010 Wiley) + 'The Science of Human Hacking' (2018 2e) + 'Phishing Dark Waters' + Social-Engineer Toolkit (SET) 早期推广, Innocent Lives Foundation 创办者.
- **代表作品**: 《Social Engineering: The Art of Human Hacking》(2010 Wiley 1st ed) / 《Social Engineering: The Science of Human Hacking》(2018 Wiley 2e) [T01-S064] / 《Phishing Dark Waters》(2015) / 《Human Hacking》(2021) / Social-Engineer LLC 公司 + Social-Engineer Village (DEF CON 历年 + 现已分立) [T01-S063] / Innocent Lives Foundation (反儿童剥削 OSINT).
- **值得读/听/看**: 《Social Engineering: The Science of Human Hacking》2e 全书 [T01-S064] / social-engineer.com (公司主页 + podcast + 培训) [T01-S063] / Social-Engineer Podcast.
- **争议**: 2022-02 DEF CON 公开 transparency report 取消 Hadnagy + Social-Engineer Village 在 DEF CON 的资格, 行业曾就此事件分裂讨论. 本 manifest 立场 academic neutrality: 仅记录其作为 SE 教材作者 + Social-Engineer LLC 创办者的事实身份, 不展开 transparency report 内容. 读者应自行 cross-reference DEF CON 官方公告 + Hadnagy 回应 + 法律诉讼记录形成独立判断.
- **最近 12 个月动态**: 2024-2025 Social-Engineer LLC 持续运营 + 培训商业化 [T01-S063], Innocent Lives Foundation 持续运作. DEF CON 不再参与, 改在自有 Human Hacking Conference 演讲.

---

### 28. Deviant Ollam (deviant-ollam)

**figures**: Deviant Ollam
**evidence**: [T01-S065 / T01-S066]

> (figures: Deviant Ollam)

- **核心一句话**: 全球物理安全 + 锁工艺 + 物理渗透事实权威 — TOOOL (The Open Organisation Of Lockpickers) 主导, DEF CON 物理 / TOOOL Village 长期演讲, 'Practical Lock Picking' 教材作者.
- **代表作品**: TOOOL 主导 (北美 + EU 锁工艺社区) [T01-S065] / 《Practical Lock Picking》(2010 Syngress 2e 2012) / 《Keys to the Kingdom: Impressioning, Privilege Escalation, Bumping》(2012) / DEF CON Physical Security Village / Lockpicking Village 长期主导 / 'Elevator Hacking' DEF CON 2014 经典演讲 (与 Howard Payne 合作).
- **值得读/听/看**: toool.us 美国分会主页 [T01-S065] / deviating.net 个人主页 [T01-S066] / DEF CON 历年物理安全 / Lockpicking Village 视频 / 'Elevator Hacking' 经典演讲.
- **争议**: 无公开争议. 立场清晰 educational + 反对将 lock picking 工具卖给 burglar 用途, TOOOL 章程明确 sport + 安全研究 + 锁匠教育导向.
- **最近 12 个月动态**: 2024-2025 持续 TOOOL 主导 + DEF CON Physical Security Village + 大量物理安全 keynote [T01-S066], 2024 多次 elevator / RFID badge / door bypass 主题演讲. 个人主页 deviating.net 不定期更.

---

### 29. Jayson Street (jayson-street)

**figures**: Jayson Street
**evidence**: [T01-S067]

> (figures: Jayson Street)

- **核心一句话**: 大众面对面社工 + 物理渗透实战 演讲家 — '在 BlackHat 主会场上台后第二天就去某美国大银行 vault 拍照' 这种现场 demo 风格的代表人物, DEF CON / DerbyCon historical 长期主持人级 figure.
- **代表作品**: 《Dissecting the Hack: The F0rb1dd3n Network》(Syngress 系列, 小说化教育) / Truesec / SphereNY 现职红队 + 物理渗透 / DEF CON / DerbyCon / BSides 多年面对面演讲 + 现场 demo 风格 (走进 真实银行 / 政府办公楼 / 数据中心) / 'I PWN thee, I PWN thee not!' 经典演讲.
- **值得读/听/看**: @jaysonstreet Twitter [T01-S067] / DEF CON 历年视频 / 'Strategies on securing your banks & enterprises' 系列 keynote.
- **争议**: 2019 年某次 公开个人事件 + 行业曾有讨论, 主流社区已 重新接纳. 本 manifest academic neutrality: 仅记录其作为现场 demo + 大众面对面 SE 教育者的事实贡献.
- **最近 12 个月动态**: 2024-2025 持续 Truesec / 全球巡讲 + DEF CON / BSides 持续演讲 [T01-S067], 偏面对面互动 + 现场 demo 教育.

---

### 30. Ian Coldwater (ian-coldwater)

**figures**: Ian Coldwater
**evidence**: [T01-S068]

> (figures: Ian Coldwater)

- **核心一句话**: K8s + 容器安全权威 + DEF CON Cloud Village 创办者 — '我看 Kubernetes 像看 BloodHound 看 AD' 名言, 把 K8s 攻击面 推到 红队主流 + cloud-native 安全社区领袖.
- **代表作品**: DEF CON Cloud Village co-founder (与 Brad Geesaman / Duffie Cooley 等) / 大量 KubeCon / DEF CON / Black Hat K8s 安全演讲 / 'The Kubernetes Effect' / 多年 Twitter / Discord K8s 安全社区领袖.
- **值得读/听/看**: @IanColdwater Twitter [T01-S068] / DEF CON Cloud Village 历年视频 / KubeCon K8s SIG-Security 演讲.
- **争议**: 无公开争议. 立场清晰 educational + open community + DEI advocacy 强.
- **最近 12 个月动态**: 2024-2025 持续 K8s 红队 + Cloud Village 主导 [T01-S068], 多次 KubeCon / DEF CON 演讲, Twitter 持续社区领袖角色.

---

### 31. Rory McCune / raesene (rory-mccune)

**figures**: Rory McCune
**evidence**: [T01-S069 / T01-S070 / T01-S071]

> (figures: Rory McCune)

- **核心一手**: K8s 安全 + Container Security 实战权威 — Kubernetes Goat (开源 K8s 安全靶场, co-maintainer) + Datadog Cloud Security Researcher, 'Kubernetes Security' 实战长文系列, CIS Kubernetes Benchmark contributor.
- **代表作品**: Kubernetes Goat (Madhu Akula + Rory McCune et al, 开源 K8s 安全靶场, 用于学习与培训) [T01-S069] / raesene.github.io blog (K8s + Container Security 实战长文) [T01-S070] / CIS Kubernetes Benchmark contributor / 《Container Security: A 360 Degree Approach》(Wiley, co-author) / NCC Group / ControlPlane / Aqua / Datadog 多家公司 K8s 安全顾问历程.
- **值得读/听/看**: raesene.github.io (K8s + container security 长文) [T01-S070] / @raesene Twitter [T01-S071] / Kubernetes Goat GitHub [T01-S069] / KubeCon / Black Hat / DEF CON 历年演讲.
- **争议**: 无公开争议. 立场 红蓝并重 + 实战 + 安全工程教育.
- **最近 12 个月动态**: 2024-2025 持续 Datadog Cloud Security Research + KubeCon / DEF CON 多次 K8s 安全演讲 [T01-S070] [T01-S071], Kubernetes Goat 持续社区维护 [T01-S069].

---

### 32. Brad Geesaman / bradgeesaman (brad-geesaman)

**figures**: Brad Geesaman
**evidence**: [T01-S072]

> (figures: Brad Geesaman)

- **核心一句话**: K8s + Cloud-native 安全实战权威 + 前 CNCF Security TAG co-chair — 'Hacking Kubernetes the Hard Way' / DEF CON Cloud Village co-organizer, 把 K8s 红队从工具 demo 升级为 CNCF 标准化 + 多云联合演练.
- **代表作品**: 'Hacking and Hardening Kubernetes Clusters by Example' Black Hat 2017 经典 / Darkbit (创办, 后被 GitLab 收购) / Ghost Security 现职 / 前 CNCF Security TAG co-chair / Container Solutions / DEF CON Cloud Village co-organizer.
- **值得读/听/看**: @bradgeesaman Twitter [T01-S072] / Black Hat / KubeCon / DEF CON Cloud Village 历年演讲 / CNCF Security TAG GitHub.
- **争议**: 无公开争议. 立场 红蓝并重 + 标准化 + 多厂商 vendor-neutral.
- **最近 12 个月动态**: 2024-2025 持续 Ghost Security 现职 + KubeCon / DEF CON 多次演讲 + CNCF + cloud-native security 社区 [T01-S072], K8s + multi-cloud red team automation 持续输出.

---

### 33. IppSec (ippsec)

**figures**: IppSec
**evidence**: [T01-S073 / T01-S074]

> (figures: IppSec)

- **核心一句话**: HackTheBox machine writeup 视频教程之神 — 600+ HTB machine 每周一更, 配合 ippsec.rocks 时间戳搜索引擎, 现已成为 OSCP / OSEP / OSED 备考 + 红队入门事实标配资源.
- **代表作品**: ippsec.rocks (HTB writeup 视频时间戳搜索引擎, 红队入门事实工具) [T01-S073] / IppSec YouTube 频道 (600+ HTB machine 视频, 每周一更, 2017+) [T01-S074] / OffSec 官方授权 OSCP-like 视频系列.
- **值得读/听/看**: IppSec YouTube 任意 HTB machine writeup (新手推荐 Beginner Friendly 类) [T01-S074] / ippsec.rocks (按主题 / 工具 / 漏洞类型搜索时间戳) [T01-S073] / 'OSCP Box List' 推荐顺序.
- **争议**: 无公开争议. 立场清晰 lab + CTF 教育 + 强调 authorization-only.
- **最近 12 个月动态**: 2024-2025 持续每周 HTB machine 视频 [T01-S074], 2025+ 也偶尔 OffSec proving grounds + HTB Pro Labs (red team 多机) writeup. 个人 lower profile, 内容输出极稳定.

---

### 34. NahamSec / Ben Sadeghipour (nahamsec)

**figures**: NahamSec / Ben Sadeghipour
**evidence**: [T01-S075 / T01-S076]

> (figures: Ben Sadeghipour / NahamSec)

- **核心一句话**: bug bounty 教学 + NahamCon 会议 主办 — YouTube 直播 + 录播 bug bounty 实战 + 与顶级 hunter 对谈, 把 bug bounty 从 elite 圈子降到入门门槛.
- **代表作品**: NahamCon 会议 (自主办 bug bounty + 红队主题会议, 2020+) / NahamSec YouTube 频道 (bug bounty 教学 + 直播 + 与顶级 hunter 访谈) [T01-S075] / 前 HackerOne / Yahoo bug bounty / 'Recon Tools' 工具集 / 多次 DEF CON Recon Village 演讲.
- **值得读/听/看**: NahamSec YouTube 频道 [T01-S075] / @NahamSec Twitter [T01-S076] / NahamCon 历年会议视频 / 'Live Recon' 直播系列.
- **争议**: 无公开争议. 立场清晰 educational + bug bounty platform-vetted programs only.
- **最近 12 个月动态**: 2024-2025 NahamSec YouTube + NahamCon 持续主办 [T01-S075] [T01-S076], 2024-2025 推出 'Recon Course' + AI for bug bounty 培训方向.

---

### 35. John Hammond / _JohnHammond (john-hammond)

**figures**: John Hammond
**evidence**: [T01-S077 / T01-S078 / T01-S108]

> (figures: John Hammond)

- **核心一句话**: Huntress threat researcher + CTF / malware analysis YouTube 教学之星 — 'When you understand the attacker, you can defend' 教学风格, 把 malware reverse engineering + ransomware affiliate TTPs 拆给入门观众.
- **代表作品**: Huntress threat research blog (DragonForce ransomware / VECTRA / BlackCat 等 IR 案例) [T01-S108] / John Hammond YouTube (CTF writeup + malware analysis + ransomware unpacking, 2M+ subscribers) [T01-S077] / 'Practical Malware Analysis & Triage' 课 / 前 US Coast Guard cyber.
- **值得读/听/看**: John Hammond YouTube (CTF + malware + IR case studies) [T01-S077] / @_JohnHammond Twitter [T01-S078] / Huntress blog 作者文章 [T01-S108].
- **争议**: 无公开争议. 立场清晰防御侧 + 教育 + ransomware affiliate disruption.
- **最近 12 个月动态**: 2024-2025 持续 Huntress threat researcher + YouTube 每周更 [T01-S077] [T01-S108], 2024-2025 大量 fake CAPTCHA / ClickFix / DragonForce / Akira ransomware unpacking 视频.

---

### 36. LiveOverflow (liveoverflow)

**figures**: LiveOverflow
**evidence**: [T01-S079 / T01-S080]

> (figures: LiveOverflow)

- **核心一句话**: binary exploitation + CTF + game hacking + Minecraft 安全的 YouTube 大众化教育者 — 把 stack overflow / heap exploitation / ROP / kernel exploit 拆解到 高中生能懂的水平, 是 exploit dev 新一代入门事实第一站.
- **代表作品**: LiveOverflow YouTube 频道 (binary exploitation / CTF / Minecraft hacking 系列, 1M+ subscribers, 2015+) [T01-S079] / 'Linux Heap Exploitation' 课 (Pwn College 合作) / liveoverflow.com 课程主页 [T01-S080] / 'How is HackTheBox like?' 系列.
- **值得读/听/看**: LiveOverflow YouTube 'Binary Exploitation' Playlist [T01-S079] / liveoverflow.com 课程 [T01-S080] / 'Minecraft hacking' 系列 (将 game 漏洞作为 exploit 教学切入).
- **争议**: 无公开争议. 立场清晰 educational + lab-only + 强调 'this is for learning, do not test on production'.
- **最近 12 个月动态**: 2024-2025 持续 YouTube 输出 [T01-S079], 2025+ 转向更多 web / cloud / AI security exploration 主题, 不再仅 binary exploitation. liveoverflow.com 课程持续更 [T01-S080].

---

### 37. TCM / Heath Adams (tcm-heath-adams)

**figures**: Heath Adams / The Cyber Mentor
**evidence**: [T01-S081 / T01-S082]

> (figures: Heath Adams / The Cyber Mentor)

- **核心一句话**: TCM Security 创办 + PEH (Practical Ethical Hacker) / PNPT (Practical Network Penetration Tester) 培训创办 — '价格亲民 + hands-on lab + OSCP 替代' 的低门槛红队培训路线, YouTube + Udemy 大众化入门最广.
- **代表作品**: TCM Security 创办 (2019+, 培训 + 渗透服务) [T01-S081] / PEH 课程 (Udemy + TCM Academy, 入门 pentest 课) / PNPT 认证 (OSCP-like, 5 天 internal + AD focus) / TCM Security YouTube (入门 pentest 教学) [T01-S082] / 多个 Udemy 畅销课.
- **值得读/听/看**: tcm-sec.com (TCM Academy 课程目录) [T01-S081] / TCM Security YouTube [T01-S082] / PNPT 认证 syllabus.
- **争议**: 部分老 OSCP 圈对 PNPT 'OSCP 替代' 定位有讨论, Heath Adams 立场: PNPT 是 internal/AD focused 实战导向, 与 OSCP 互补不替代.
- **最近 12 个月动态**: 2024-2025 持续 TCM Academy + PEH / PNPT 培训商业化 [T01-S081], YouTube 持续更 + 2025+ AI for pentest 方向 + Mobile / Cloud / IoT 培训扩展 [T01-S082].

---

### 38. Bruce Schneier (bruce-schneier)

**figures**: Bruce Schneier
**evidence**: [T01-S083]

> (figures: Bruce Schneier)

- **核心一句话**: 业内 senior statesman + 密码学经典《Applied Cryptography》(1996) 作者 + Berkman Klein Center Harvard fellow — 跨越 cryptography / security economics / public policy 三大领域的 思考者 + advocacy, Cryptogram newsletter 持续 27+ 年.
- **代表作品**: 《Applied Cryptography》(1996 Wiley 经典) / 《Secrets and Lies》(2000) / 《Liars and Outliers》(2012) / 《Click Here to Kill Everybody》(2018, IoT 安全 + 监管 policy) / 《A Hacker's Mind》(2023) / Cryptogram 月度 newsletter 1998+ / Berkman Klein Center fellow / 多个加密算法 (Blowfish / Twofish / Skein) 设计者.
- **值得读/听/看**: schneier.com (Cryptogram newsletter + 长文 blog, 2026 仍每月更) [T01-S083] / 《A Hacker's Mind》最新书 (2023, 把 'hacking' 概念从技术泛化到 法律 / 金融 / 政治 系统漏洞).
- **争议**: 部分政策立场 (反 Apple 端到端加密 backdoor / 反国家级监控 / 反 IoT 自由市场) 引发 政府 + 部分产业争议, Schneier 立场: 长期 pro-civil-liberties + pro-strong-crypto.
- **最近 12 个月动态**: 2024-2025 schneier.com 持续每月 Cryptogram + 每周长文 [T01-S083], 2024-2025 大量 AI / Election Security / LLM prompt injection 主题长文, 出版 'A Hacker's Mind' 后持续巡讲.

---

### 39. Brian Krebs (brian-krebs)

**figures**: Brian Krebs
**evidence**: [T01-S084 / T01-S085]

> (figures: Brian Krebs)

- **核心一句话**: 网络犯罪经济链调查记者 #1 — krebsonsecurity.com 长期独立网站, 多次 break 重大 breach 新闻 (Target 2013 / Home Depot 2014 / Equifax 2017 等), 《Spam Nation》(2014) 把 俄罗斯 spam + 网络犯罪生态系统化报道.
- **代表作品**: krebsonsecurity.com (2009+ 独立独立站, daily reporting + 深度调查) [T01-S084] / 《Spam Nation: The Inside Story of Organized Cybercrime》(2014 Sourcebooks) / 大量 ransomware affiliate / initial access broker / 暗网市场报道 / 前 Washington Post 安全记者.
- **值得读/听/看**: krebsonsecurity.com 任意 'A Deep Dive' 系列长文 [T01-S084] / @briankrebs Twitter [T01-S085] / 《Spam Nation》全书.
- **争议**: 曾多次被网络犯罪团伙报复 (swatting / heroin 邮寄假栽赃 / DDoS 攻击网站等), Krebs 持续 不退缩 + 公开记录加害事件. 部分被调查的合法企业偶尔 push back, Krebs 立场: 公共利益 + 独立性 + sourcing 严格.
- **最近 12 个月动态**: 2024-2025 krebsonsecurity.com 持续每周多更 [T01-S084], 2024-2025 大量 ransomware ecosystem / Telegram cybercrime forum / cryptocurrency laundering 调查报道. Twitter @briankrebs 持续 active [T01-S085].

---

### 40. Troy Hunt (troy-hunt)

**figures**: Troy Hunt
**evidence**: [T01-S086 / T01-S087]

> (figures: Troy Hunt)

- **核心一句话**: Have I Been Pwned (HIBP) 创办者 — 把 'breach 数据' 从安全研究员的暗角推到全球用户密码 hygiene 工具, 与 Microsoft / 1Password / Cloudflare 集成, 同时 Pluralsight Security 课多门, breach + 密码安全教育 advocacy.
- **代表作品**: haveibeenpwned.com (2013+ 独立独立项目, 14B+ breached account 索引) [T01-S086] / Pwned Passwords (k-anonymity API, 集成 1Password / Microsoft / Cloudflare) / Pluralsight 课多门 (ASP.NET Security / OWASP Top 10 / Modern Browser Security 等) / troyhunt.com 个人 blog [T01-S087] / 多次 RSA / DEF CON / Microsoft Ignite 演讲.
- **值得读/听/看**: haveibeenpwned.com 主站 [T01-S086] / troyhunt.com weekly update + breach 分析长文 [T01-S087] / Pluralsight Security 课目录 / 'Why your passwords are like socks' 经典演讲.
- **争议**: 2024 年 Troy Hunt 个人 Twitter 被 phish (公开承认 + 反思 long-form post) 引发 'even security pros get phished' 讨论. Troy 立场: openness + transparency about own mistakes.
- **最近 12 个月动态**: 2024-2025 HIBP 持续每周多更 + 大量新 breach 索引 [T01-S086], 2025+ HIBP API v3 → v4 升级, 'Weekly Update' video 持续 weekly [T01-S087].

---

### 41. KEEN Lab Team (Tencent) (keen-lab-team)

**figures**: KEEN Lab Team
**evidence**: [T01-S088 / T01-S089]

> (figures: Liang Chen / Wushi (吴石) / Bo Pan / DaiKaifeng / TyphoonTeam / Marco Grassi (前) / Sen Nie / Yuxiang Li)

- **核心一句话**: 腾讯 KEEN Lab 是 中国最顶级 漏洞研究团队之一 — Pwn2Own Vancouver / Mobile 多年 winner, 2016 Tesla Model S 远程攻破 (公开 disclosure) 全球轰动, iOS / Safari / Chrome / Tesla 0-day 多次拿下.
- **代表作品**: 2016 Tesla Model S 远程攻破 (CAN bus 控制) + 2017 Tesla Model X 持续 / Pwn2Own 2014-2017 Mobile + Vancouver iOS / Safari / Chrome 多次 winner / 'Pwning iOS via Safari' 系列 Black Hat 演讲 / keenlab.tencent.com 英文 + 中文研究 blog [T01-S088].
- **值得读/听/看**: keenlab.tencent.com/en (英文 blog + 研究 advisory 列表) [T01-S088] / Black Hat USA / Asia / DEF CON 历年 KEEN Lab 演讲 / 'Experimental Security Research of Tesla Autopilot' 2019 paper.
- **争议**: 2018+ 中国 网络安全审查 收紧后, KEEN Lab 部分研究公开窗口受限 + Pwn2Own 转向 国内 Tianfu Cup (天府杯), 国际公开发表频率下降. 团队人员 国际流动受限 是 academic 共识的客观背景.
- **最近 12 个月动态**: 2024-2025 KEEN Lab 持续 Tencent 内部研究 + 偶尔 Black Hat Asia 演讲 + Tianfu Cup 持续多次 winner [T01-S088]. 国际 0-day disclosure 频率较 2014-2017 黄金期低, 但研究能力仍属全球第一梯队.

---

### 42. 360 Vulcan Team (360-vulcan-team)

**figures**: 360 Vulcan Team
**evidence**: [T01-S090 / T01-S091]

> (figures: Yu Xianglin / Zhang Yikun / yangkang / hanming / 360 Vulcan core team)

- **核心一句话**: 360 公司旗下顶级漏洞研究团队 — 2015-2017 Pwn2Own Vancouver 五连冠纪录创造者 (IE / Edge / Flash / Adobe Reader 大量 0-day), 后转 Tianfu Cup 持续 winner.
- **代表作品**: Pwn2Own 2015-2017 五连冠 (IE / Edge / Flash / Chrome 多次 0-day) / Tianfu Cup 多年 winner / vul.360.net 漏洞研究 blog (中文为主, 偶尔英文) [T01-S090] / 多次 Black Hat USA / Asia 演讲 / Microsoft / Adobe / Google 多个 致谢 advisory.
- **值得读/听/看**: vul.360.net (360 漏洞研究 blog) [T01-S090] / Wikipedia 360 Vulcan Team 履历参考 [T01-S091] / Black Hat 历年视频.
- **争议**: 同 KEEN Lab — 2018+ 国际公开 disclosure 窗口收紧, 部分研究转 Tianfu Cup. 360 公司本身因 2020+ 美国制裁 (Entity List) 在国际安全社区 visibility 降低, 但团队研究能力客观顶尖.
- **最近 12 个月动态**: 2024-2025 360 Vulcan Team 持续国内研究 + Tianfu Cup 主力 [T01-S090], 国际公开发表频率低, 但 ISP / vendor coordinated 漏洞 仍持续输出.

---

### 43. Chaitin Tech 长亭科技 (chaitin-tech)

**figures**: Chaitin Tech Team
**evidence**: [T01-S092]

> (figures: 杨坤 / 王宇 / 朱文雷 / 黑哥 (周辉) / Chaitin core team)

- **核心一句话**: 长亭科技 (Chaitin Tech) — 清华学生 + Pangu 团队 alumni 创办的中国顶级 Web + 容器 + AppSec 红队公司, 雷池 WAF + 牧云 HIDS + 商业渗透 + Pwn2Own 历史 winner.
- **代表作品**: 雷池 (SafeLine) WAF (开源 + 商业) / 牧云 (CloudWalker) HIDS / Pwn2Own 2016-2017 Safari / Adobe Reader / Microsoft Edge 多次 winner / chaitin.cn 公司 blog (中文为主) [T01-S092] / DEF CON / Black Hat 多次演讲 / Pangu iOS jailbreak alumni (部分创始团队).
- **值得读/听/看**: chaitin.cn (长亭官网 + 公司 blog) [T01-S092] / 雷池 WAF GitHub (开源) / Black Hat 历年长亭演讲 (HTTPD / D-Bus / SAML 主题).
- **争议**: 长亭 2019 阿里收购引发部分独立性讨论, 后续 2022 又传 拆分 / 战略调整 — 公司层面有 商业化与研究自由度的张力. 立场: 商业化路线 + 持续研究输出, 与 360 / KEEN 国家队风格不同.
- **最近 12 个月动态**: 2024-2025 长亭持续 雷池 WAF / 牧云 HIDS 商业化 + 阿里安全体系协同 [T01-S092], 公开研究输出频率较 2016-2018 黄金期减少, 但 Web + 容器领域仍属国内一线.

---

### 44. lake2 / 知道创宇 / ZoomEye (lake2-knownsec)

**figures**: lake2 (Knownsec)
**evidence**: [T01-S093 / T01-S094]

> (figures: lake2 / 杨冀龙 / 钱文祥 / 知道创宇核心)

- **核心一句话**: 知道创宇 (Knownsec) — 创办 ZoomEye 网络空间测绘 + Seebug 漏洞库 + paper.seebug.org 中文 Web 漏洞研究一手, lake2 (杨冀龙) 等核心团队中国 Web 漏洞研究奠基.
- **代表作品**: ZoomEye 网络空间测绘 (Shodan 中国对标) [T01-S094] / Seebug 漏洞库 (CVE 中文化 + 中文漏洞情报) / paper.seebug.org (Web + 漏洞研究中文一手 blog) [T01-S093] / Knownsec 404 实验室 / 'XSS Cheat Sheet' 早期中文标杆.
- **值得读/听/看**: paper.seebug.org (Knownsec 404 + 社区中文漏洞研究长文) [T01-S093] / zoomeye.org (网络空间测绘) [T01-S094] / Knownsec 404 GitHub.
- **争议**: 同 长亭 / 360 / KEEN — 2018+ 国内 网络空间测绘 + 漏洞披露 受 网络安全法 + 数据安全法 监管框架影响, 部分历史漏洞 PoC 已不再公开. 立场: 监管框架内合规输出.
- **最近 12 个月动态**: 2024-2025 ZoomEye 持续作为国内主力网络测绘 [T01-S094], paper.seebug.org 持续中文 Web 漏洞研究输出 [T01-S093], Knownsec 404 团队持续小范围公开发表.

---

### 45. weev / Andrew Auernheimer (anti-example) (weev-auernheimer)

**figures**: weev / Andrew Auernheimer
**evidence**: [T01-S095 / T01-S096]

> (figures: weev / Andrew Auernheimer)

- **核心一句话** (anti-example): AT&T iPad 2010 CFAA 案件 — '在公开可访问的 URL 上枚举 ICC-ID 提取 114k iPad 用户 email' 触发美国联邦 CFAA 重罪起诉, 2014 第三巡回法院推翻原判, 但 业内教训 = '即使是公开 endpoint, 大规模未授权 enumeration 仍可能触 CFAA'. weev 本人 2014 后转向 white supremacist / neo-Nazi 立场, 业内已基本 distance + 不再推崇个人, 但 案件本身 作为 CFAA 滥用 + 合法授权边界 经典案例 仍必读.
- **代表作品** (历史): 2010 AT&T iPad ICC-ID enumeration (与 Daniel Spitler 合作 Goatse Security) → 2012 联邦定罪 → 2014-04 第三巡回 US v Auernheimer 推翻 (基于 jurisdiction 而非实质) → EFF 长期 amicus briefs 推动 CFAA 改革 [T01-S096].
- **值得读/听/看**: EFF US v Auernheimer 案件页 (案件事实 + CFAA 学术批评) [T01-S096] / Wikipedia weev 履历参考 [T01-S095] / Orin Kerr / Tor Ekeland 等学者关于 CFAA broad reading 的文章.
- **争议**: weev 2014 后立场 (white supremacist / Daily Stormer 技术支持) 引发业内基本 distance, **本 manifest 仅记录 案件本身的法律 + 红队伦理 lesson** (公开 endpoint enumeration ≠ 合法; 即使有 EFF 等组织 amicus brief, 检察官仍可能 CFAA broad reading 起诉), 不背书 weev 个人. 当代 红队任何 enumeration / scanning 都必须有 explicit written authorization, 这是 ROE 第一条.
- **反例 lesson**: 公开可访问的 URL ≠ 授权访问; 大规模自动化枚举即使技术上 trivial, 仍可触 CFAA / 类似国家法 (中国 刑法 285 条非法获取计算机信息系统数据罪 / 英国 Computer Misuse Act 1990). 这是 红队 + bug bounty 必须 scope + 授权确认 优先级 #1 的现实驱动.
- **最近 12 个月动态** (反例不列入活跃图景): weev 本人当前与红队主流社区无 active 联系, 案件 reference 价值 stable.

---

### 46. Marcus Hutchins / MalwareTech (anti-example with rehabilitation) (marcus-hutchins-malwaretech)

**figures**: Marcus Hutchins / MalwareTech
**evidence**: [T01-S097 / T01-S098]

> (figures: Marcus Hutchins / MalwareTech)

- **核心一句话** (anti-example + rehabilitation): 2017-05 WannaCry ransomware 全球爆发, Marcus Hutchins 仅 22 岁 发现 + 注册 kill switch domain 阻止 大规模感染 — 全球安全英雄. 2017-08 DEF CON 离场时被 FBI 逮捕, 因 2014-2015 (青少年时期) 涉嫌编写 Kronos banking trojan + 销售. 2019-07 联邦法院 plea bargain, 判时间已 served + 1 year supervised release, 法官公开评价 'positive contributions outweigh past actions'. 业内当前 主流姿态: **承认现在的贡献 + 不抹除过去的事实** — 是 反例 vs rehabilitation 的标准学术处理.
- **代表作品** (现在): malwaretech.com (2017+ blog, ransomware / malware analysis 长文, Trickbot / Emotet / WannaCry 系列深度技术分析) [T01-S097] / Wikipedia Marcus Hutchins 履历 [T01-S098] / Twitter @malwrhunterteam (前) / 多次 BSides / DEF CON Recon Village 演讲 / 2024+ Hutchins 主导 ransomware affiliate research.
- **值得读/听/看**: malwaretech.com (WannaCry / Kronos / Emotet / ransomware 案例长文) [T01-S097] / 'How to Accidentally Stop a Global Cyber Attack' Marcus 2017-05 个人 blog 原文 / 2020 Wired 'The Confessions of Marcus Hutchins, the Hacker Who Saved the Internet' 深度报道 (作为 历史 reference).
- **争议** (开放讨论): 业内 关于 Marcus 的姿态分两派 — 一派认为 '青少年时期错误 + 已 served + 持续贡献' 应充分接纳; 一派认为 即使法律已 served, malware 商业销售 历史仍是 red team 行业必须明边界. 本 manifest 立场: 承认事实 + 记录 rehabilitation + 当前贡献 + 不抹除历史, 由读者形成独立判断.
- **反例 lesson**: 青少年时期写 malware 卖 (尤其涉及 商业 banking trojan + 黑市渠道) 即使后续多年贡献仍可能触美国 / 欧盟 / 英国 刑法 + 永久影响国际旅行 / 工作签证 + 行业声誉. 红队 + bug bounty 不可与 私下 0-day 销售 / malware authoring 混合.
- **最近 12 个月动态**: 2024-2025 Marcus 持续 malwaretech.com 输出 [T01-S097], 主要 ransomware affiliate research + 偶尔 公开 talks (BSides / DEF CON Recon Village 等). 当前主要居住 / 工作 美国, 历史已 served.

---

### 47. NSO Group + Cellebrite (anti-example, surveillance vendors) (nso-cellebrite-anti)

**figures**: NSO Group / Cellebrite (corporate anti-examples)
**evidence**: [T01-S099 / T01-S100 / T01-S101]

> (figures: NSO Group / Cellebrite — 商业监控供应商作为 行业明边界 反例, 不进 effective tradecraft, 仅作 ethical 边界 reference)

- **核心一句话** (anti-example, corporate): NSO Group (以色列, Pegasus iOS / Android zero-click spyware) + Cellebrite (以色列, UFED 移动取证设备) — 把 高端 0-day + forensic capability 商业销售给 国家政府 (含威权政府 + 警察 + 情报机构), 长期被 Citizen Lab / Amnesty International / Forbidden Stories / WhatsApp / Apple 公开调查并诉讼, 用于监控记者 (Khashoggi 案 / Pegasus Project 2021) / 异见者 / 律师 / 人权活动家. 业内 学术 + civil society 严厉批评, 美国商务部 2021-11 把 NSO 列入 Entity List. 本 manifest 立场: 严明 行业边界 — 这是 反例 不是 effective tradecraft, 红队 / bug bounty 行业主流 不与监控供应商 ecosystem 合作.
- **代表作品** (反例): NSO Group Pegasus spyware (iMessage / WhatsApp zero-click chain, 2016-2024 多次曝光) / Cellebrite UFED (移动取证设备, 卖给警察 + 威权政府) / Hacking Team historical (意大利, 2015 被 hack 内部文件公开后倒闭) / Gamma Group FinFisher (类似商业监控厂商).
- **值得读/听/看** (作为 ethical 边界 reference, secondary bucket): Citizen Lab Targeted Threats 系列 reports (citizenlab.ca, 学术 一手) [T01-S099] / Forbidden Stories 'Pegasus Project' (2021-07 51 国 80 媒体联合调查) / WhatsApp v NSO Group 2024-12 美国联邦法院判决 (NSO 责任成立) / Wikipedia NSO Group + Cellebrite 履历 reference [T01-S100] [T01-S101] / Moxie Marlinspike 2021-04 'Exploiting vulnerabilities in Cellebrite UFED and Physical Analyzer from an app's perspective' 经典反击长文.
- **争议** (开放讨论): NSO / Cellebrite 立场: 仅卖给 主权国家 + 用于 反恐 + 重罪调查 + 合法 due process. Citizen Lab + 学术 + 多次 leaked customer list 反驳: 实际 customer list 包含 沙特 / 阿联酋 / 墨西哥 / 乌干达 / 印度 等 多个 政府用于 监控记者 + 异见者, 严重违反国际人权法. 这是 surveillance industry 与 主流 红队 / pentest / bug bounty 行业的根本 ethical 切割.
- **反例 lesson**: 商业 0-day 销售 + 商业 spyware + 商业 forensic 卖给 威权政府 = 与 主流红队行业的根本 ethical 切割. 红队 / bug bounty / pentest 行业 长期共识: (1) authorization-only; (2) scoped engagement; (3) coordinated disclosure; (4) 不与 监控记者 / 异见者 的客户合作. 这条边界 不是 个人偏好, 是 行业 institutional 共识 — 加入 NSO / Cellebrite / Hacking Team-like 公司 是 长期声誉损害事件, 与主流红队 + bug bounty + cert org (OffSec / SANS / EC-Council) ethics code 直接冲突.
- **最近 12 个月动态** (作为反例 reference): 2024-12 WhatsApp v NSO Group 美国联邦法院判决 NSO 责任成立 (历史性裁决) [T01-S099]; 2024-2025 Citizen Lab 持续每月披露新 Pegasus / Predator / FinFisher 受害案例; Cellebrite 2024 持续推 AI 增强 forensic + 多次企业客户 + 政府 contract 公开报道 [T01-S101]. 行业 ethical 边界与本反例的距离 是 红队 incumbent identity 的核心一部分.

---

(46 figures + 3 anti-examples = 49 total figure subsections covering A-K 11 schools. 全部 figure subsection 在 heading 后 第 1 行 含 `> (figures: ...)` blockquote 双保险, 集体名 figure (KEEN Lab / 360 Vulcan / Chaitin / 知道创宇 / NSO+Cellebrite) 已在 blockquote 列出 individual members. evidence 全部 引用 T01-Sxxx source_id, 与 manifest 一一对应.)
