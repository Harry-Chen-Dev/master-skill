# Track 05 — Sources (Cybersecurity Red Team)

> Wave 1 Track 05 — newsletter / podcast / conference / community / vendor research / 作者一手 blog / 政府 advisory / 学术 paper venue / 中文 community. Industry: Cybersecurity Red Team — Offensive Security Operations, locale=en (global English primary, zh-CN secondary, English:Chinese ≈ 4:1), profile=practitioner.
>
> 结构约束 notes (诚实): (1) 英文一手信源密度远高于中文 (8-10x), 中文优质内容大量集中在 zh-CN 黑名单平台 (公众号 / 知乎 / CSDN) 或散落 Twitter/X — 必须用 surrogate_primary 兜底标 'vendor docs (中国 安全 社区)'; (2) 红队 community 信源生态结构性碎片化 — 没有 single SOT 类似软件架构的 martinfowler.com / dentistry 的 AAID — 而是 ~10 个 顶级 vendor research blog (SpecterOps / TrustedSec / Mandiant / Google Project Zero / Securelist / Talos / Check Point / NCC / Synacktiv / watchTowr) + ~15 个 作者一手 blog (harmj0y / adsecurity / ired.team / hacktricks / bohops / hexacorn / Krebs / Schneier / Tavis Ormandy cmpxchg8b / Daniel Miessler) 共同构成 daily reading; (3) Newsletter 中 tl;dr sec (Clint Gibler, 月 50k+ subs 业内 deep dive 周刊) + Risky Business News (Catalin Cimpanu, ex-ZDNet/Recorded Future 调查记者 周刊) + This Week in 4n6 (Phil Moore, DFIR 周刊 全球 forensicators 必读) 三家是 community gold standard; (4) Podcast 中 Darknet Diaries (Jack Rhysider, 2017 起, 月下载 600k+) 是行业入门标杆, Risky Business (Patrick Gray + Adam Boileau, 2007 起, 澳大利亚, 每周一 + Risky Business News 短播) 是业内分析最高密度, SANS Internet Storm Center StormCast (Johannes Ullrich) 5 分钟 daily 是 IOC/CVE 速报最快入口; (5) 顶级 conference 集中在 8 月 Las Vegas Hacker Summer Camp (DEF CON + Black Hat USA + BSides Las Vegas 同周, 行业一年最大一手输入窗口), 红队特化 OffensiveCon (Berlin 4 月 漏洞研究 + exploit dev 顶会) + x33fcon (Gdynia 6 月 红队 vs 蓝队 mixed) + TROOPERS (Heidelberg 6 月 AD / AppSec 强项) + Chaos Communication Congress (CCC 12 月 Hamburg/Leipzig, 政治 + exploitation + 反监控 视角); (6) 红队 community 实时讨论已大幅从 Twitter/X 迁移至 Mastodon infosec.exchange (2022-11 起 Elon 收购后 ≈ 50% sec 圈大牛迁移, Tavis Ormandy / Marcus Hutchins / Daniel Miessler / Troy Hunt / Mikko Hyppönen 等仍 cross-post) + BloodHound Slack (SpecterOps managed, 20k+ members) + Cobalt Strike user community (Fortra managed) + Mythic Discord (其他 C2 community), Discord 取代旧 IRC #defcon 等成为 daily watercooler.

---

## Source Manifest

| source_id | url | bucket | last_checked | author/host | one-line note |
|-----------|-----|--------|--------------|-------------|---------------|
| T05-S001 | https://tldrsec.com | surrogate_primary | 2026-05-17 | Clint Gibler (NCC Group / r2c) | vendor docs (业内 newsletter 作者一手) — tl;dr sec 周刊 50k+ subs, AppSec + red team 深度 curated |
| T05-S002 | https://risky.biz/subscribe | surrogate_primary | 2026-05-17 | Catalin Cimpanu | vendor docs (业内 newsletter) — Risky Business News 周刊, ex-ZDNet 调查记者, threat intel 一手 |
| T05-S003 | https://thisweekin4n6.com | surrogate_primary | 2026-05-17 | Phil Moore | vendor docs (业内 newsletter) — This Week in 4n6 周刊, DFIR 全球链接聚合标准 |
| T05-S004 | https://www.bleepingcomputer.com | secondary | 2026-05-17 | Bleeping Computer editorial | 行业媒体 — 漏洞 + ransomware + 行动 daily 报道, Lawrence Abrams 主编 |
| T05-S005 | https://thecyberwire.com | surrogate_primary | 2026-05-17 | N2K Networks | vendor docs (业内 podcast + newsletter) — Cyberwire Daily 5 分钟 daily IOC + 政策 |
| T05-S006 | https://www.sans.org/newsletters/newsbites/ | surrogate_primary | 2026-05-17 | SANS Institute | vendor docs (协会 + syllabus) — SANS NewsBites 周二/周五, 行业 editor panel commentary |
| T05-S007 | https://www.opensecuritysummit.org | surrogate_primary | 2026-05-17 | Open Security Summit org | vendor docs (协会 + 会议) — OWASP-aligned 年度 unconference, 录播免费 |
| T05-S008 | https://darknetdiaries.com | surrogate_primary | 2026-05-17 | Jack Rhysider | vendor docs (业内 podcast 作者一手) — Darknet Diaries 月下载 600k+, 2017+ 红队 + 网络犯罪 故事 |
| T05-S009 | https://risky.biz/podcasts | surrogate_primary | 2026-05-17 | Patrick Gray + Adam Boileau | vendor docs (业内 podcast) — Risky Business 周更 + Risky Business News short, 2007+ |
| T05-S010 | https://www.smashingsecurity.com | surrogate_primary | 2026-05-17 | Graham Cluley + Carole Theriault | vendor docs (业内 podcast) — Smashing Security 周更, 业内八卦 + 教育 |
| T05-S011 | https://www.blackhillsinfosec.com/podcasts/ | surrogate_primary | 2026-05-17 | Black Hills Information Security | vendor docs (业内 podcast 厂商研究) — BHIS Active Countermeasures + Talkin' Bout [In]fosec News |
| T05-S012 | https://isc.sans.edu/podcast.html | surrogate_primary | 2026-05-17 | Johannes Ullrich (SANS ISC) | vendor docs (协会 + 业内 podcast) — StormCast 5 分钟 daily IOC + CVE 速报 |
| T05-S013 | https://defensiveSecurity.org | secondary | 2026-05-17 | Jerry Bell + Andrew Kalat | Defensive Security Podcast 周更, 蓝队向但红队反推必听 |
| T05-S014 | https://www.hackedpodcast.com | surrogate_primary | 2026-05-17 | Jordan Bloemen + Scott Francis Winder | vendor docs (业内 podcast) — Hacked 双周, 网络犯罪 + 红队 案例 |
| T05-S015 | https://www.defcon.org | surrogate_primary | 2026-05-17 | DEF CON | vendor docs (会议) — DEF CON 34 2026-08-06 ~ 09 Las Vegas, talks + 录像 一手 |
| T05-S016 | https://media.defcon.org | surrogate_primary | 2026-05-17 | DEF CON | vendor docs (会议) — DEF CON 历年 talks media 永久存档 |
| T05-S017 | https://www.blackhat.com/us-26/ | surrogate_primary | 2026-05-17 | Black Hat | vendor docs (会议) — Black Hat USA 2026-08-01 ~ 06 Mandalay Bay Las Vegas |
| T05-S018 | https://www.blackhat.com/eu-26/ | surrogate_primary | 2026-05-17 | Black Hat | vendor docs (会议) — Black Hat Europe 2026-12 伦敦 ExCeL |
| T05-S019 | https://www.blackhat.com/asia-26/ | surrogate_primary | 2026-05-17 | Black Hat | vendor docs (会议) — Black Hat Asia 2026-04 Marina Bay Sands Singapore |
| T05-S020 | https://i.blackhat.com | surrogate_primary | 2026-05-17 | Black Hat | vendor docs (会议) — Black Hat USA 历年 whitepaper + slides 永久存档 (按年份 path) |
| T05-S021 | https://www.offensivecon.org | surrogate_primary | 2026-05-17 | OffensiveCon Berlin | vendor docs (会议) — OffensiveCon 2026-04-30 ~ 05-01 Berlin, 漏洞研究 + exploit dev 顶会 |
| T05-S022 | https://troopers.de | surrogate_primary | 2026-05-17 | ERNW (Heidelberg) | vendor docs (会议) — TROOPERS26 2026-06 Heidelberg, AD/AppSec/红队 强项 |
| T05-S023 | https://www.x33fcon.com | surrogate_primary | 2026-05-17 | x33fcon | vendor docs (会议) — x33fcon 2026-06 Gdynia 波兰, 红队 + 蓝队 + purple team 顶会 |
| T05-S024 | https://media.ccc.de | surrogate_primary | 2026-05-17 | Chaos Computer Club | vendor docs (会议) — CCC media archive, 38C3 (2024-12 Hamburg) + 历年 talks 永久免费 |
| T05-S025 | https://events.ccc.de | surrogate_primary | 2026-05-17 | Chaos Computer Club | vendor docs (会议) — CCC events page, Congress + Camp + Easterhegg |
| T05-S026 | https://nsec.io | surrogate_primary | 2026-05-17 | NorthSec | vendor docs (会议) — NorthSec 2026-05 Montreal, 北美红队 + CTF 顶会 |
| T05-S027 | https://conference.hitb.org | surrogate_primary | 2026-05-17 | Hack In The Box | vendor docs (会议) — HITB Amsterdam (5 月) + HITB Phuket (8 月) + HITB GSEC Singapore |
| T05-S028 | https://www.ekoparty.org | surrogate_primary | 2026-05-17 | Ekoparty | vendor docs (会议) — Ekoparty 2026-10 Buenos Aires 阿根廷, 拉美最大 hacking 会 |
| T05-S029 | https://nullcon.net | surrogate_primary | 2026-05-17 | Nullcon | vendor docs (会议) — Nullcon Goa (印度, 2-3 月) + Berlin (9 月) |
| T05-S030 | https://www.zerodayinitiative.com/Pwn2Own | surrogate_primary | 2026-05-17 | Trend Micro ZDI | vendor docs (会议 + 协会) — Pwn2Own 每年 3-4 场 (Vancouver / Tokyo / Ireland / Berlin), $7M+ 奖金 |
| T05-S031 | https://bsides.org | surrogate_primary | 2026-05-17 | Security BSides | vendor docs (会议 + 协会) — BSides 全球 200+ chapters, BSidesLV (8 月 与 DEF CON 同周) 最大 |
| T05-S032 | https://shmoocon.org | surrogate_primary | 2026-05-17 | The Shmoo Group | vendor docs (会议) — ShmooCon 2026-01 Washington DC, 老牌东海岸黑客会 |
| T05-S033 | https://saintcon.org | surrogate_primary | 2026-05-17 | SaintCon | vendor docs (会议) — SaintCon 2026-10 Utah, 中西部红队 + hands-on workshops |
| T05-S034 | https://posts.specterops.io | surrogate_primary | 2026-05-17 | SpecterOps team | vendor docs (厂商研究 作者一手) — BloodHound 作者团队博客, AD attack path #1 一手 |
| T05-S035 | https://specterops.io/blog/ | surrogate_primary | 2026-05-17 | SpecterOps | vendor docs (厂商研究) — SpecterOps 官博, 含 BloodHound CE + Enterprise release notes |
| T05-S036 | https://www.trustedsec.com/blog/ | surrogate_primary | 2026-05-17 | TrustedSec (Dave Kennedy) | vendor docs (厂商研究) — TrustedSec 博客, COFF/BOF + Cobalt Strike 实战 高密度 |
| T05-S037 | https://research.nccgroup.com | surrogate_primary | 2026-05-17 | NCC Group | vendor docs (厂商研究) — NCC Group Research, exploit dev + 红队咨询 案例 一手 |
| T05-S038 | https://www.mandiant.com/resources/blog | surrogate_primary | 2026-05-17 | Mandiant (Google Cloud) | vendor docs (厂商研究) — Mandiant 博客 (现 cloud.google.com/blog/topics/threat-intelligence), APT 调查 一手 |
| T05-S039 | https://googleprojectzero.blogspot.com | surrogate_primary | 2026-05-17 | Google Project Zero | vendor docs (厂商研究 作者一手) — Project Zero, 顶级漏洞研究 + 0-day 揭露 90 天政策 |
| T05-S040 | https://msrc.microsoft.com/blog | surrogate_primary | 2026-05-17 | Microsoft Security Response Center | vendor docs (厂商研究) — MSRC 博客, Patch Tuesday + advisories 一手 |
| T05-S041 | https://securelist.com | surrogate_primary | 2026-05-17 | Kaspersky GReAT | vendor docs (厂商研究) — Securelist Kaspersky Global Research & Analysis Team, APT 报告 顶级 一手 |
| T05-S042 | https://research.checkpoint.com | surrogate_primary | 2026-05-17 | Check Point Research | vendor docs (厂商研究) — CPR 博客, 漏洞 + APT 调查 一手 |
| T05-S043 | https://blog.talosintelligence.com | surrogate_primary | 2026-05-17 | Cisco Talos | vendor docs (厂商研究) — Talos 博客, threat intel + 红队对抗 一手 |
| T05-S044 | https://www.crowdstrike.com/en-us/blog/ | surrogate_primary | 2026-05-17 | CrowdStrike | vendor docs (厂商研究) — CrowdStrike 博客 + Global Threat Report 年度 (APT 命名 BEAR/PANDA/SPIDER) |
| T05-S045 | https://redcanary.com/blog/ | surrogate_primary | 2026-05-17 | Red Canary | vendor docs (厂商研究) — Red Canary 博客 + 年度 Threat Detection Report, ATT&CK detection 一手 |
| T05-S046 | https://thedfirreport.com | surrogate_primary | 2026-05-17 | The DFIR Report | vendor docs (厂商研究) — TheDFIRReport 独立 incident 复盘, 详细 attack chain + IOC 一手 |
| T05-S047 | https://harmj0y.net | surrogate_primary | 2026-05-17 | Will Schroeder | vendor docs (作者一手) — Empire / Rubeus / Kerberoasting / Certify 原创, SpecterOps co-founder |
| T05-S048 | https://adsecurity.org | surrogate_primary | 2026-05-17 | Sean Metcalf | vendor docs (作者一手) — AD 安全权威博客, Golden Ticket / Mimikatz 深度 + Trimarc 创始人 |
| T05-S049 | https://ired.team | surrogate_primary | 2026-05-17 | Mantvydas Baranauskas | vendor docs (作者一手) — 系统化红队 tradecraft 知识库, AD + Windows + macOS + C2 全覆盖 |
| T05-S050 | https://book.hacktricks.xyz | surrogate_primary | 2026-05-17 | Carlos Polop | vendor docs (作者一手) — HackTricks GitBook, pentest checklist + cheatsheet 知识库 全球 #1 引用 |
| T05-S051 | https://bohops.com | surrogate_primary | 2026-05-17 | Jonathan Boucher (bohops) | vendor docs (作者一手) — LOLBin / Living-off-the-Land 研究权威博客 |
| T05-S052 | https://www.hexacorn.com/blog/ | surrogate_primary | 2026-05-17 | Adam (Hexacorn) | vendor docs (作者一手) — Windows internals + persistence techniques 深度博客 2009+ |
| T05-S053 | https://krebsonsecurity.com | surrogate_primary | 2026-05-17 | Brian Krebs | vendor docs (作者一手) — 调查记者 / 网络犯罪经济链 报道 顶级 一手 |
| T05-S054 | https://www.schneier.com | surrogate_primary | 2026-05-17 | Bruce Schneier | vendor docs (作者一手) — Schneier on Security, 1998+ 密码学 + 安全经济学 evergreen |
| T05-S055 | https://danielmiessler.com | surrogate_primary | 2026-05-17 | Daniel Miessler | vendor docs (作者一手) — SecLists 维护者 + Unsupervised Learning podcast/newsletter |
| T05-S056 | https://blog.cmpxchg8b.com | surrogate_primary | 2026-05-17 | Tavis Ormandy | vendor docs (作者一手) — Project Zero researcher 个人博客, Linux + 反 AV / EDR 经典批评 |
| T05-S057 | https://ippsec.rocks | surrogate_primary | 2026-05-17 | Ippsec | vendor docs (作者一手) — HTB 视频教程 顶级, OSCP 备考 community 公认 #1 free video |
| T05-S058 | https://0xdf.gitlab.io | surrogate_primary | 2026-05-17 | 0xdf | vendor docs (作者一手) — HackTheBox writeups 全 retired box, IppSec 文字版补充 |
| T05-S059 | https://www.youtube.com/@LiveOverflow | surrogate_primary | 2026-05-17 | LiveOverflow | vendor docs (作者一手) — CTF + exploit dev YouTube, 教育向最深入 series |
| T05-S060 | https://www.youtube.com/@JohnHammond | surrogate_primary | 2026-05-17 | John Hammond | vendor docs (作者一手) — Huntress senior researcher, malware analysis + CTF + 红队 教学 |
| T05-S061 | https://www.youtube.com/@NahamSec | surrogate_primary | 2026-05-17 | Ben Sadeghipour (NahamSec) | vendor docs (作者一手) — bug bounty + recon 教学 + NahamCon 主办 |
| T05-S062 | https://infosec.exchange | surrogate_primary | 2026-05-17 | Jerry Bell (admin) | vendor docs (业内 社区) — Mastodon infosec.exchange, 2022-11 Elon 收购 X 后 大量 sec 圈迁入 |
| T05-S063 | https://www.reddit.com/r/netsec | reference | 2026-05-17 | r/netsec community | UGC default reference (community 入口, 不作 一手) |
| T05-S064 | https://www.reddit.com/r/AskNetsec | reference | 2026-05-17 | r/AskNetsec community | UGC default reference (community 入口, 不作 一手) |
| T05-S065 | https://hackerone.com/hacktivity | surrogate_primary | 2026-05-17 | HackerOne | vendor docs (协会 + user-provided 一手 reports) — Hacktivity public reports feed, real-world exploit 学习 |
| T05-S066 | https://bugcrowd.com/crowdstream | surrogate_primary | 2026-05-17 | Bugcrowd | vendor docs (协会) — Bugcrowd CrowdStream public disclosures feed |
| T05-S067 | https://www.intigriti.com/researchers/bug-bytes | surrogate_primary | 2026-05-17 | Intigriti | vendor docs (协会 + 业内 newsletter) — Intigriti Bug Bytes 周刊, bug bounty curated |
| T05-S068 | https://yeswehack.com/learn-bug-bounty | surrogate_primary | 2026-05-17 | YesWeHack | vendor docs (协会 + syllabus) — YesWeHack Dojo + Learn 教材, EU based bug bounty platform |
| T05-S069 | https://ctftime.org | surrogate_primary | 2026-05-17 | CTFtime | vendor docs (协会) — CTFtime, 全球 CTF 联合排名 + event calendar 标准 |
| T05-S070 | https://www.cisa.gov/news-events/cybersecurity-advisories | verified_primary | 2026-05-17 | CISA (US) | auto-verified (.gov) — CISA Cybersecurity Advisories, KEV + AA-series alerts |
| T05-S071 | https://www.cisa.gov/known-exploited-vulnerabilities-catalog | verified_primary | 2026-05-17 | CISA (US) | auto-verified (.gov) — CISA KEV Known Exploited Vulnerabilities Catalog, federal due date 强制 |
| T05-S072 | https://nvd.nist.gov | verified_primary | 2026-05-17 | NIST (US) | auto-verified (.gov) — NVD National Vulnerability Database, CVE + CVSS 一手 |
| T05-S073 | https://www.ncsc.gov.uk/section/advice-guidance/all-topics | verified_primary | 2026-05-17 | NCSC UK | auto-verified (.gov.uk) — NCSC UK advisories + guidance |
| T05-S074 | https://www.enisa.europa.eu/publications | surrogate_primary | 2026-05-17 | ENISA | ENISA Threat Landscape 年报 + topical reports [declared=surrogate_primary, auto=secondary; reason=vendor docs (协会 + 监管 — ENISA 欧盟网络安全局, .europa.eu 不在 auto-verify 后缀)] |
| T05-S075 | https://www.kb.cert.org/vuls/ | surrogate_primary | 2026-05-17 | CERT/CC (SEI/CMU) | CERT/CC Vulnerability Notes database (Carnegie Mellon SEI 维护) [declared=surrogate_primary, auto=secondary; reason=vendor docs (协会 + 监管 — CERT/CC 卡内基梅隆 SEI 协调 disclosure, .org 不在 auto-verify 后缀)] |
| T05-S076 | https://www.ic3.gov/AnnualReport | verified_primary | 2026-05-17 | IC3 FBI | auto-verified (.gov) — IC3 Internet Crime Report 年报 |
| T05-S077 | https://www.cncert.org.cn | surrogate_primary | 2026-05-17 | CNCERT/CC | vendor docs (监管) — 国家计算机网络应急技术处理协调中心, 网信办下属 |
| T05-S078 | https://www.usenix.org/conferences/byname/108 | surrogate_primary | 2026-05-17 | USENIX | vendor docs (协会 + 会议) — USENIX Security Symposium, 开放 proceedings, 系统安全顶会 |
| T05-S079 | https://www.ieee-security.org/TC/SP2026/ | surrogate_primary | 2026-05-17 | IEEE Computer Society | vendor docs (协会 + 会议) — IEEE S&P (Oakland) 2026-05 San Francisco, 学术安全顶会 |
| T05-S080 | https://www.sigsac.org/ccs.html | surrogate_primary | 2026-05-17 | ACM SIGSAC | vendor docs (协会 + 会议) — ACM CCS Computer & Communications Security, 学术顶会 |
| T05-S081 | https://www.ndss-symposium.org | surrogate_primary | 2026-05-17 | Internet Society | vendor docs (协会 + 会议) — NDSS Network & Distributed System Security, 学术顶会 |
| T05-S082 | https://arxiv.org/list/cs.CR/recent | verified_primary | 2026-05-17 | arXiv (Cornell) | auto-verified (arxiv) — preprint cs.CR Cryptography & Security, 配 cs.CY + cs.SE |
| T05-S083 | https://seclists.org/fulldisclosure/ | surrogate_primary | 2026-05-17 | seclists.org / Gordon Lyon | vendor docs (协会 + 监管) — Full Disclosure mailing list archive, 1990s+ 漏洞披露 历史 |
| T05-S084 | https://www.openwall.com/lists/oss-security/ | surrogate_primary | 2026-05-17 | Openwall | vendor docs (协会 + 监管) — oss-security mailing list, Linux/OSS 漏洞 coordinated disclosure |
| T05-S085 | https://www.anquanke.com | surrogate_primary | 2026-05-17 | 安全客 (奇安信) | vendor docs (中国 安全 社区) — 安全客, 奇安信维护 一手 中国安全研究 平台 |
| T05-S086 | https://www.freebuf.com | surrogate_primary | 2026-05-17 | FreeBuf | vendor docs (中国 安全 社区) — FreeBuf, 中国安全媒体 + 社区 一手 |
| T05-S087 | https://www.kanxue.com | surrogate_primary | 2026-05-17 | 看雪学院 (Pediy) | vendor docs (中国 安全 社区) — 看雪, 中国逆向 + 漏洞研究 社区 1999+ |
| T05-S088 | https://paper.seebug.org | surrogate_primary | 2026-05-17 | Seebug Paper (知道创宇) | vendor docs (中国 安全 社区) — Seebug Paper, 知道创宇 安全研究 paper 平台 |
| T05-S089 | https://xz.aliyun.com | surrogate_primary | 2026-05-17 | 先知社区 (阿里云) | vendor docs (中国 安全 社区) — 先知, 阿里云安全社区 一手 |
| T05-S090 | https://tttang.com | surrogate_primary | 2026-05-17 | 跳跳糖 (腾讯安全) | vendor docs (中国 安全 社区) — 跳跳糖 TTTANG, 腾讯安全社区 一手 |
| T05-S091 | https://keenlab.tencent.com | surrogate_primary | 2026-05-17 | Tencent KEEN Lab | vendor docs (中国 安全 社区) — KEEN Security Lab, 腾讯 Pwn2Own 顶级团队 一手 |
| T05-S092 | https://www.chaitin.cn/zh/blog | surrogate_primary | 2026-05-17 | 长亭科技 Chaitin Tech | vendor docs (中国 安全 社区) — 长亭科技 博客, XCTF + RealWorldCTF 主办 |
| T05-S093 | https://vul.360.net | surrogate_primary | 2026-05-17 | 360 Vulcan / DigitalSec | vendor docs (中国 安全 社区) — 360 漏洞云, 360 Vulcan Team Pwn2Own + 0-day 一手 |
| T05-S094 | https://www.defenseindepth.io | secondary | 2026-05-17 | David Spark + Allan Alford / CISO Series | Defense in Depth podcast 周更, CISO + 红队 视角 mixed |
| T05-S095 | https://microsoftsecurityinsights.com | secondary | 2026-05-17 | Microsoft Security Insights | Microsoft Security Insights podcast, Sentinel / Defender 视角, 红队对抗反推 |

---

## 5.1 Newsletter (英文 — community standard)

- **tl;dr sec** [T05-S001] / tldrsec.com / Clint Gibler (NCC Group → r2c → Semgrep CSO) / 周刊 (周一) / 2018+ / 50k+ subs / 免费 / Why: AppSec + 红队 deep dive curated, 业内 #1 周读, Clint 本人 也是 BSides SF + DEF CON AppSec Village 组织者.
- **Risky Business News** [T05-S002] / risky.biz/subscribe / Catalin Cimpanu (ex-ZDNet / Recorded Future) / 周三 + 周五 短播 / 2021+ / 免费 + paid tier / Why: threat intel + 政策 一手, Catalin 是业内最资深网络犯罪调查记者之一.
- **This Week in 4n6** [T05-S003] / thisweekin4n6.com / Phil Moore / 周日 / 2017+ / 免费 / Why: DFIR 全球链接聚合, 红队 也读 (反推 detection + 攻击 chain).
- **SANS NewsBites** [T05-S006] / sans.org/newsletters/newsbites / SANS Institute editor panel / 周二 + 周五 / 2001+ / 免费 / Why: editor (Alan Paller / John Pescatore / Bill Murray 等) commentary 是其特色, 行业事件视角.
- **Cyberwire Daily** [T05-S005] / thecyberwire.com / N2K Networks / 周一 ~ 五 daily / 免费 + paid Pro / Why: 5 分钟 daily IOC + 政策, 通勤听 / 早晨读 双形态.
- **Bleeping Computer** [T05-S004] / bleepingcomputer.com / Lawrence Abrams 主编 / 滚动 daily / 免费 (with ads) / Why: 漏洞 + ransomware + actor 行动 daily 报道, 偏新闻向但红队需追 emerging.
- **Intigriti Bug Bytes** [T05-S067] / intigriti.com/researchers/bug-bytes / 周刊 / 免费 / Why: bug bounty hunter 视角 curated, EU 视角 Intigriti researcher community 一手.
- **Open Security Summit** [T05-S007] / opensecuritysummit.org / 年度 unconference (OWASP-aligned) / 录播免费 / Why: 行业实践分享 集中地, 不是周刊 newsletter 但 reference 一年.

## 5.2 Podcast (英文 — 业内必听)

- **Darknet Diaries** [T05-S008] / darknetdiaries.com / Jack Rhysider / 2017-09+ / 月下载 600k+ / 每月 1-2 集 / 免费 / Why: 入门标杆, 红队 + 网络犯罪 + 国家行为 故事化叙事, 业内最有声望 podcast 公认 (但 不是 technical deep dive).
- **Risky Business** [T05-S009] / risky.biz/podcasts / Patrick Gray (主持) + Adam Boileau (合作 panel) / 2007+ / 周更 / 免费 / Why: 业内分析最高密度, 澳大利亚视角但全球受众, 每集附 RB News short.
- **Smashing Security** [T05-S010] / smashingsecurity.com / Graham Cluley + Carole Theriault / 2017+ / 周更 / 免费 / Why: 业内八卦 + 教育向, 给 non-tech 同事推荐入门.
- **The Cyberwire Daily** [T05-S005] / thecyberwire.com / N2K / 周一 ~ 五 daily / Why: 5 分钟 daily 适合通勤, IOC + 政策快速更新.
- **BHIS Talkin' Bout [In]fosec News + Active Countermeasures** [T05-S011] / blackhillsinfosec.com/podcasts / Black Hills Information Security / 双周 / 免费 / Why: John Strand 主持的 lab 实战风格, BHIS 是顶级红队 consulting + 培训厂商.
- **SANS Internet Storm Center StormCast** [T05-S012] / isc.sans.edu/podcast.html / Johannes Ullrich / daily 5 分钟 / 1995+ / 免费 / Why: IOC / CVE / honeypot 趋势 速报最快入口, 工程师早晨第一耳听.
- **Hacked** [T05-S014] / hackedpodcast.com / Jordan Bloemen + Scott Francis Winder / 双周 / 2018+ / Why: 网络犯罪 + 红队 案例 故事化, 与 Darknet Diaries 同类型互补.
- **Defense in Depth** [T05-S094] / defenseindepth.io / David Spark + Allan Alford / 周更 / Why: CISO Series 出品, 红队反推 detection / governance.
- **Microsoft Security Insights** [T05-S095] / microsoftsecurityinsights.com / Why: Microsoft Sentinel + Defender 视角, 红队对抗反推 (Microsoft 自己 ATT&CK 模拟 案例 一手).
- **Defensive Security Podcast** [T05-S013] / defensiveSecurity.org / Jerry Bell + Andrew Kalat / 周更 / Why: 蓝队向但红队反推必听, infosec.exchange admin Jerry Bell 主持.

## 5.3 顶级 conferences

英文 / 国际:
- **DEF CON 34** [T05-S015][T05-S016] / defcon.org / 2026-08-06 ~ 09 Las Vegas (Convention Center) / 历年 talks media.defcon.org 永久免费 / Why: 全球最大 hacker 会议, Villages (Aerospace / AI / BioHacking / Car Hacking / ICS / IoT / Lockpicking / Red Team / Recon / Social Engineering / Voting) 是红队 sub-niche 圣地.
- **Black Hat USA 2026** [T05-S017][T05-S020] / blackhat.com/us-26 / 2026-08-01 ~ 06 Mandalay Bay Las Vegas / talks + whitepaper i.blackhat.com 历年永久存档 / Why: 商业向, training (4 天) + briefings (2 天) + Arsenal (tool demo) + Business Hall, 业内 announcement 集中地.
- **Black Hat Europe** [T05-S018] / blackhat.com/eu-26 / 2026-12 London ExCeL / Why: 欧洲红队大会 标杆.
- **Black Hat Asia** [T05-S019] / blackhat.com/asia-26 / 2026-04 Singapore Marina Bay Sands / Why: 亚洲红队入口, Pwn2Own Asia 通常 同期.
- **OffensiveCon 2026** [T05-S021] / offensivecon.org / 2026-04-30 ~ 05-01 Berlin / 漏洞研究 + exploit dev 顶会 / 200 人小会高浓度 / Why: 内核 / 浏览器 / hypervisor exploit 顶级研究员 (Tavis / Saelo / Maddie Stone / niklasb) 一手分享.
- **TROOPERS26** [T05-S022] / troopers.de / 2026-06 Heidelberg / ERNW 主办 / Why: AD / AppSec / Telecom (5G) 红队强项, NGI track AD-specific 深度.
- **x33fcon** [T05-S023] / x33fcon.com / 2026-06 Gdynia 波兰 / Why: 红队 vs 蓝队 vs purple team mixed 顶会, 实操 hands-on 较多.
- **CCC 38C3 / 39C3** [T05-S024][T05-S025] / media.ccc.de + events.ccc.de / 12 月 (Hamburg / Leipzig 轮换) / Why: 欧洲最大 hacker 政治 + exploitation + 反监控 会, talks 永久免费 高质量翻译.
- **NorthSec 2026** [T05-S026] / nsec.io / 2026-05 Montreal / 含 全球最大 CTF 之一 / Why: 北美红队 + CTF 顶会.
- **HITB** [T05-S027] / conference.hitb.org / Amsterdam (5 月) + Phuket (8 月) + GSEC Singapore / Why: 国际化, exploit dev + 红队 + CTF mixed.
- **Ekoparty 2026** [T05-S028] / ekoparty.org / 2026-10 Buenos Aires / Why: 拉美最大 hacking 会, 西语圈核心.
- **Nullcon** [T05-S029] / nullcon.net / Goa (2-3 月) + Berlin (9 月) / Why: 印度最大安全会, 漏洞研究 + 红队.
- **Pwn2Own** [T05-S030] / zerodayinitiative.com/Pwn2Own / 每年 3-4 场 (Vancouver CanSecWest 3 月 + Tokyo Pacific 11 月 + Ireland + Berlin + Automotive) / $7M+ 累计奖金 / Why: 顶级 exploit dev 竞赛, KEEN Lab / 360 Vulcan / Synacktiv / STAR Labs / DEVCORE 长期参赛.
- **BSides 全球 200+ chapters** [T05-S031] / bsides.org / BSidesLV (8 月 与 DEF CON 同周, Las Vegas Tuscany) 最大 / Why: 草根, 任何城市可办, 跟踪本地 chapter 是 networking 一手.
- **ShmooCon** [T05-S032] / shmoocon.org / 2026-01 Washington DC / 售罄速度世界纪录 (开票后秒杀) / Why: 老牌东海岸黑客会, talks 质量 + 社群密度高.
- **SaintCon** [T05-S033] / saintcon.org / 2026-10 Utah / Why: 中西部红队 + 大量 hands-on workshops + 价格亲民.

中文 / 大中华区:
- **看雪安全峰会 / KCon** / 看雪学院主办 / 北京 / Why: 中国逆向 + 漏洞研究 #1 大会.
- **XCon** / 北京 / Why: 老牌中国黑客会议 2002+.
- **RealWorldCTF** / 长亭科技主办 / Why: 中国最大国际化 CTF, finals 海外参赛队 普遍前 10.
- **OPPO 安全峰会 / 滴滴 DDCTF / 字节跳动 BCTF** / 厂商主办 / Why: 大厂红队 / 漏洞研究 一手分享 + 招聘窗口.
- **HITB GSEC Singapore** [T05-S027] / Why: 亚洲红队入口 之一.

## 5.4 Vendor research blog (顶级 — daily / weekly 追)

- **SpecterOps** [T05-S034][T05-S035] / posts.specterops.io + specterops.io/blog / SpecterOps team (Will Schroeder / Andy Robbins / Lee Christensen 等) / Why: BloodHound 作者团队, AD attack path + Cobalt Strike + 红队 tradecraft #1 公司博客.
- **TrustedSec** [T05-S036] / trustedsec.com/blog / Dave Kennedy 创始 (SET / Unicorn 作者) / Why: COFF/BOF + Cobalt Strike + payload 实战, 偶尔大放送 (e.g. SysWhispers 系列).
- **NCC Group Research** [T05-S037] / research.nccgroup.com / Why: exploit dev + 红队咨询 案例 + 内核 / 浏览器 研究 一手, Matt Lewis / Aaron Adams 等长期出 paper.
- **Mandiant (Google Cloud)** [T05-S038] / cloud.google.com/blog/topics/threat-intelligence / Why: APT 调查 一手 (APT1 / APT28 / FIN7 命名标杆), 现 cloud.google.com 路径下.
- **Google Project Zero** [T05-S039] / googleprojectzero.blogspot.com / Why: 顶级漏洞研究 + 0-day 揭露 90 天政策, Maddie Stone / Tavis Ormandy / Ben Hawkes 等历年文章 evergreen.
- **MSRC Blog** [T05-S040] / msrc.microsoft.com/blog / Microsoft Security Response Center / Why: Patch Tuesday + Microsoft 自己 advisories 一手 + 偶尔 case study.
- **Securelist (Kaspersky GReAT)** [T05-S041] / securelist.com / Kaspersky Global Research & Analysis Team / Why: APT 报告顶级 (Equation Group / Carbanak 揭露), 俄语视角.
- **Check Point Research** [T05-S042] / research.checkpoint.com / Why: 漏洞 + APT 调查 一手, 偶有重大研究 (e.g. iOS Triangulation 2023).
- **Cisco Talos** [T05-S043] / blog.talosintelligence.com / Why: threat intel + 红队对抗 一手, IOC 高密度 + ClamAV 维护.
- **CrowdStrike Blog** [T05-S044] / crowdstrike.com/en-us/blog + 年度 Global Threat Report / Why: APT 命名 (BEAR/PANDA/SPIDER/CHOLLIMA) 业内引用标准 之一.
- **Red Canary** [T05-S045] / redcanary.com/blog + 年度 Threat Detection Report / Why: ATT&CK detection 一手, Atomic Red Team 维护方.
- **The DFIR Report** [T05-S046] / thedfirreport.com / 独立 team / Why: 详细 incident attack chain 复盘 + IOC + sigma rule, 红队 反推学习 detection.

## 5.5 作者一手 blog (个人 — community 引用密度高)

- **harmj0y.net** [T05-S047] / Will Schroeder / SpecterOps co-founder / Why: Empire / Rubeus / Kerberoasting / Certify 原创, AD attack 顶级.
- **adsecurity.org** [T05-S048] / Sean Metcalf / Trimarc 创始人 / Why: AD 安全权威博客 2015+, Golden Ticket / DCSync / DCShadow 深度解析.
- **ired.team** [T05-S049] / Mantvydas Baranauskas / Why: 系统化红队 tradecraft 知识库 (cheatsheet style 但 hands-on lab 详细), 涵盖 AD + Windows + macOS + C2.
- **HackTricks** [T05-S050] / book.hacktricks.xyz / Carlos Polop / GitBook 形式 / Why: pentest checklist + cheatsheet 知识库 全球 #1 引用 (CTF / OSCP / 红队 工作 daily 翻).
- **Bohops** [T05-S051] / bohops.com / Jonathan Boucher / Why: LOLBin / Living-off-the-Land 研究权威, MSBuild / regsvr32 / mshta 绕过技巧原创.
- **Hexacorn** [T05-S052] / hexacorn.com/blog / Adam / 2009+ / Why: Windows internals + persistence techniques 深度, "Beyond good ol' Run key" 系列权威.
- **Krebs on Security** [T05-S053] / krebsonsecurity.com / Brian Krebs / 2009+ / Why: 调查记者, 网络犯罪经济链 / IAB / ransomware affiliate 深度调查.
- **Schneier on Security** [T05-S054] / schneier.com / Bruce Schneier / 1998+ / Why: 密码学 + 安全经济学 evergreen, 每周 squid blog Friday.
- **Daniel Miessler** [T05-S055] / danielmiessler.com / Daniel Miessler / Why: SecLists 维护者 + Unsupervised Learning podcast/newsletter, AI + 安全交叉视角.
- **cmpxchg8b** [T05-S056] / blog.cmpxchg8b.com / Tavis Ormandy / Project Zero researcher / Why: 个人博客 Linux + 反 AV / EDR 经典批评 (Kaspersky / Sophos / Symantec 多次 takedown).
- **0xdf hacks stuff** [T05-S058] / 0xdf.gitlab.io / Why: HackTheBox writeups 全 retired box, IppSec 文字版补充, OSCP 备考必读.

## 5.6 视频 教学 (HTB / CTF / bug bounty)

- **IppSec** [T05-S057] / ippsec.rocks (索引 + YouTube) / Why: HTB 视频教程 顶级, OSCP 备考 community 公认 #1 free video, ippsec.rocks 提供 全 transcript 搜索.
- **LiveOverflow** [T05-S059] / youtube.com/@LiveOverflow / Why: CTF + exploit dev YouTube, 教育向最深入 series (pwn intro / browser exploit / 等).
- **John Hammond** [T05-S060] / youtube.com/@JohnHammond / Huntress senior researcher / Why: malware analysis + CTF + 红队 教学, daily upload 高频.
- **NahamSec** [T05-S061] / youtube.com/@NahamSec / Ben Sadeghipour / Why: bug bounty + recon 教学, NahamCon 主办 (年度免费 bug bounty 大会).
- **HackerSploit / The Cyber Mentor (Heath Adams TCM Security)** / YouTube / Why: 入门 + OSCP 备考 视频, TCM Security 现也 提供 PNPT certification.

## 5.7 Community (Discord / Slack / Mastodon / Reddit)

- **BloodHound Slack** / 由 SpecterOps managed (含 BHCE channel) / 20k+ members / Why: BloodHound + AD attack path 现场答疑, 维护者 直接互动 (Andy Robbins / Stephen Hinck 等).
- **Cobalt Strike user community** / Fortra (Help Systems) managed (用户须有 license) / Why: 商用 Cobalt Strike 操作员社区, malleable C2 profile 分享 + BOF 讨论.
- **Mythic Discord** / Cody Thomas (SpecterOps) / Why: Mythic C2 + Apollo / Athena 等 agent 讨论, 开源 C2 community 核心.
- **OWASP Slack** / owasp.org → invite link / 50k+ members / Why: AppSec 全球社区, 各 chapter + project channel.
- **TryHackMe Discord** / tryhackme.com → invite / Why: TryHackMe 学员社区, beginner 提问 + writeup 分享.
- **HackTheBox Discord** / hackthebox.com → invite / Why: HTB 学员社区, retired box writeup + 实战讨论.
- **NahamSec Discord** / Ben Sadeghipour / Why: bug bounty community, NahamCon + 周更 Twitch 流 配套.
- **Hacker101 Discord** / HackerOne 维护 / Why: bug bounty 入门 community + CTF.
- **infosec.exchange (Mastodon)** [T05-S062] / Jerry Bell admin / Why: 2022-11 Elon 收购 X 后 ≈ 50% sec 圈大牛迁移, Tavis Ormandy / Marcus Hutchins / Daniel Miessler / Troy Hunt / Mikko Hyppönen 等 active.
- **Twitter / X 红队圈** / 仍是 主流 实时讨论 (尽管迁移 Mastodon) / Why: 跟随 list 推荐 (SwiftOnSecurity / hacks4pancakes Lesley Carhart / Marcus Hutchins MalwareTechBlog / Tavis Ormandy taviso / Daniel Miessler / Troy Hunt / Jake Williams MalwareJake / Florian Roth cyb3rops Sigma 作者).
- **r/netsec** [T05-S063] / reddit.com/r/netsec / 600k+ subs / Why: 漏洞 / disclosure / paper 转载入口, UGC 但 高质 (mod 严格).
- **r/AskNetsec** [T05-S064] / reddit.com/r/AskNetsec / Why: 职业 + 入门问答.
- **r/HowToHack / r/redteamsec / r/blueteamsec** / Why: 细分 sub, redteamsec 偏 商业咨询视角, blueteamsec 反推必读.

## 5.8 Bug bounty platforms (作为 信息源)

- **HackerOne Hacktivity** [T05-S065] / hackerone.com/hacktivity / Why: public disclosed reports feed, real-world exploit 学习 + writeup 一手 (e.g. Frans Rosén / Sam Curry / Sean Yeoh 等顶级 hunter 公开 reports).
- **Bugcrowd CrowdStream** [T05-S066] / bugcrowd.com/crowdstream / Why: Bugcrowd 公开 disclosures feed.
- **Intigriti Bug Bytes** [T05-S067] / intigriti.com/researchers/bug-bytes / Why: EU 视角 bug bounty 周刊 + Hall of Fame.
- **YesWeHack Dojo + Learn** [T05-S068] / yeswehack.com/learn-bug-bounty / Why: EU based 教材 + lab + program.
- **Synack Red Team (SRT)** / synack.com / Why: 受邀私有 platform, ROE 严格 + 报告深度高 (但 program / writeup 不公开, 仅 SRT member 可见).

## 5.9 CTF (学习 + 招聘窗口)

- **CTFtime** [T05-S069] / ctftime.org / Why: 全球 CTF 联合排名 + event calendar 标准, team 战绩 + writeup 索引.
- **picoCTF** / picoCTF.org / Carnegie Mellon / Why: 入门 CTF, 学生友好, 全年开放 + 春季比赛.
- **PlaidCTF** / pwning.net / CMU PPP team / Why: 顶级 CTF 之一.
- **DEFCON CTF** / defcon.org/html/links/dc-ctf.html / Nautilus Institute 主办 (2022 起接替 OOO) / Why: 决赛在 DEF CON 现场, 业内最高荣誉.
- **Google CTF + Beginners Quest** / Why: 大厂 CTF 入门 + 招聘窗口.
- **RealWorldCTF** / 长亭科技 / Why: 中国最大国际化 CTF, finals 海外参赛队 普遍前 10.

## 5.10 政府 advisory feeds (verified_primary)

- **CISA Cybersecurity Advisories** [T05-S070] / cisa.gov/news-events/cybersecurity-advisories / Why: KEV + AA-series alerts (e.g. AA24-XXXX) 一手, 美国联邦 + critical infra 视角.
- **CISA KEV** [T05-S071] / cisa.gov/known-exploited-vulnerabilities-catalog / Why: Known Exploited Vulnerabilities Catalog, federal due date 强制 (BOD 22-01), 红队 也参考 (active exploitation 优先).
- **NIST NVD** [T05-S072] / nvd.nist.gov / Why: CVE + CVSS 一手 (近期 backlog 严重 2024-02 起 enrichment 延迟, 红队 需 备 ⼀贝 VulnCheck NVD++ 等 mirror).
- **NCSC UK advisories** [T05-S073] / ncsc.gov.uk/section/advice-guidance/all-topics / Why: UK 政府视角 + GCHQ 关联.
- **ENISA Threat Landscape** [T05-S074] / enisa.europa.eu/publications / Why: EU 视角 年度 Threat Landscape 报告 (2024 年报 已发) + sectoral reports.
- **CERT/CC Vulnerability Notes** [T05-S075] / kb.cert.org/vuls / SEI/CMU / Why: coordinated disclosure 历史标杆 (Heartbleed CVE-2014-0160 coordination 等).
- **IC3 FBI** [T05-S076] / ic3.gov/AnnualReport / Why: Internet Crime Report 年报, BEC + ransomware 经济损失数据.
- **CNCERT/CC** [T05-S077] / cncert.org.cn / Why: 中国 国家计算机网络应急技术处理协调中心, 网信办下属, 国内 advisory + 漏洞 协调 一手 (但 仅 中文 + 部分内容仅 国家机关可见).

## 5.11 学术 paper venue (顶会 / preprint)

- **USENIX Security Symposium** [T05-S078] / usenix.org/conferences/byname/108 / 每年 8 月 / 开放 proceedings / Why: 系统安全顶会, exploit research + applied crypto + 红队 学术化基础.
- **IEEE S&P (Oakland)** [T05-S079] / ieee-security.org/TC/SP2026 / 2026-05 San Francisco / Why: 学术安全顶会 (IEEE Symposium on Security and Privacy).
- **ACM CCS** [T05-S080] / sigsac.org/ccs.html / 每年 10-11 月 / Why: ACM Computer & Communications Security, applied crypto + AppSec.
- **NDSS** [T05-S081] / ndss-symposium.org / 每年 2 月 San Diego / Internet Society / Why: Network & Distributed System Security.
- **arXiv cs.CR** [T05-S082] / arxiv.org/list/cs.CR/recent / Cornell / Why: 滚动 preprint, 顶会 paper 提前 6-12 月可见.
- **Black Hat USA whitepapers archive** [T05-S020] / i.blackhat.com / Why: 历年 (1997+) talks whitepaper + slides 按年份 path 永久存档.
- **Full Disclosure mailing list** [T05-S083] / seclists.org/fulldisclosure / Gordon Lyon / Why: 1990s+ 漏洞披露 mailing list archive, 历史 reference.
- **oss-security mailing list** [T05-S084] / openwall.com/lists/oss-security / Openwall / Why: Linux/OSS 漏洞 coordinated disclosure mailing list, distro security 必跟.

## 5.12 中文 一手 信源 (中国 安全 社区)

- **安全客** [T05-S085] / anquanke.com / 奇安信维护 / Why: 中国安全研究 平台 #1, 含 KCon / Codebreaker 等大会 转发 + 国内厂商研究员 一手投稿.
- **FreeBuf** [T05-S086] / freebuf.com / Why: 中国安全媒体 + 社区, 新闻 + 教程 + 厂商 PR mixed (注意识别).
- **看雪学院 (Pediy)** [T05-S087] / kanxue.com / 1999+ / Why: 中国逆向 + 漏洞研究 社区 #1, KCon 主办, 老牌 forum 仍 active.
- **Seebug Paper** [T05-S088] / paper.seebug.org / 知道创宇 / Why: Seebug 漏洞库配套 paper 平台, 漏洞分析深度高.
- **先知社区** [T05-S089] / xz.aliyun.com / 阿里云 / Why: 阿里云安全社区, AppSec + 漏洞 案例.
- **跳跳糖 TTTANG** [T05-S090] / tttang.com / 腾讯安全 / Why: 腾讯安全社区, KEEN Lab 配套 一手.
- **腾讯 KEEN Security Lab** [T05-S091] / keenlab.tencent.com / Why: 腾讯 Pwn2Own 顶级团队 一手研究, 浏览器 + 移动 + 车联网 0-day.
- **长亭科技 Chaitin Tech** [T05-S092] / chaitin.cn/zh/blog / Why: XCTF + RealWorldCTF 主办方博客, Web 安全 + 红队 工具 (XRAY / Rad).
- **360 漏洞云 / 360 Vulcan Team** [T05-S093] / vul.360.net / Why: 360 Vulcan Pwn2Own 顶级团队 + 0-day 研究 一手.
- **CNCERT/CC** [T05-S077] / cncert.org.cn / Why: 国家级 advisory (前文 5.10 重复列入, 但 中文 信源 中是 唯一 政府 一手).
- **中文 podcast + YouTube**: 中文红队 podcast 极少 (业内 sec 圈微博 + Twitter 仍为主), 腾讯 / 阿里 / 字节 安全团队 偶 通过 B 站 / 优酷 发 大会回放 — 单独条目不进 manifest, 主入口仍是 KCon / RealWorldCTF / XCon 大会现场 + B 站官方频道.

## 5.13 频率字段 (refresh window 速查)

| 类型 | source 例 | frequency | 何时刷新 |
|------|-----------|-----------|----------|
| Daily IOC podcast | StormCast / Cyberwire Daily | daily | 每早 通勤 |
| Daily news | Bleeping Computer | daily 滚动 | 工作中刷 |
| Weekly newsletter | tl;dr sec / Risky Biz News / This Week in 4n6 / Bug Bytes | weekly | 周一上午 batch |
| Weekly podcast | Risky Business / Smashing Security / Darknet Diaries / BHIS | weekly | 通勤 / 周末 |
| Monthly research | SpecterOps / TrustedSec / Mandiant / Google P0 | event-driven (新 research 触发) | RSS / Mastodon follow |
| Quarterly / Annual | CrowdStrike GTR / Red Canary TDR / ENISA TL / IC3 | quarterly + annual | 发布日新闻 |
| Event-driven | DEF CON / Black Hat / OffensiveCon / Pwn2Own | event-driven (会议日历) | 提前 3-6 月 plan |
| Advisory feed | CISA KEV / NVD / NCSC | event-driven (新 CVE / advisory) | RSS + Slack bot |
| Daily community | Mastodon infosec.exchange / Discord BloodHound Slack | daily 滚动 | 工作中刷 |
| CTF | CTFtime calendar | event-driven (CTF 日历) | 提前 1-2 周 register |

---

> 黑名单提醒 (踩坑预防): 不论作者多有名, 以下平台一律 blacklisted 必须改引底层一手:
> - mp.weixin.qq.com (微信公众号) — 即使腾讯安全 / 阿里安全 / 360 / 奇安信 / 长亭 公众号文章, 改引底层公司 vendor docs (keenlab.tencent.com / xz.aliyun.com / vul.360.net / anquanke.com / chaitin.cn).
> - zhihu.com / weibo.com / csdn.net / cnblogs.com / jianshu.com / baike.baidu.com — 全部 secondary 转载, 找原始作者 GitHub repo / 安全客 / 看雪 / FreeBuf 等 一手.
> - medium.com 个人 'How I hacked X' 帖 — 除非 BishopFox / SpecterOps / TrustedSec 公司 official Medium, 否则 default secondary.
> - reddit.com — default secondary (除 r/netsec 高质 disclosure 转载 仍 secondary, 找原 reference).
> - 'darkweb' / 'leaked database' / 'breach hub' 类站点引用 — STRICT BLACKLIST (违反 ROE + 法律 CFAA / 网络安全法 + 学术 ethics).
> - 已被 CVE 撤回 / 厂商认定为 false positive 的 PoC reference — 必须 cross-verify NVD + 厂商 advisory.
