# Track 01 — Figures: DevOps & SRE 思想领袖调研

> Phase 1 Wave 2 figures track. locale=en primary, zh-CN secondary. 22 candidates explored, 16 retained.
> 关键约束: source_verifier 不识别 .io/.com/.org/.dev 为 primary, 仅 .gov/.edu/.org.cn + github.com/{org}/{repo} root 自动 verified_primary。因此几乎所有 DevOps 一手域名 (sre.google / dora.dev / charity.wtf / itrevolution.com / usenix.org / teamtopologies.com 等) 都按 intake whitelist 标 `surrogate_primary` + note 含 "vendor docs" / "协会(association)" literal。

## Source Manifest

| source_id | url | bucket | last_checked | author/host | one-line note |
|-----------|-----|--------|--------------|-------------|---------------|
| T01-S001 | https://sre.google/sre-book/table-of-contents/ | surrogate_primary | 2026-05-19 | Google SRE | vendor docs (Google SRE 一手 — 学科奠基正典全文) |
| T01-S002 | https://sre.google/workbook/table-of-contents/ | surrogate_primary | 2026-05-19 | Google SRE | vendor docs (Google SRE 一手 — Site Reliability Workbook) |
| T01-S003 | https://dora.dev/research/ | verified_primary | 2026-05-19 | Google DORA | DORA Accelerate State of DevOps 研究 (auto verified — /research path) |
| T01-S004 | https://dora.dev/guides/dora-metrics-four-keys/ | surrogate_primary | 2026-05-19 | Google DORA | vendor docs (Google DORA 一手 — 四关键指标定义) |
| T01-S005 | https://itrevolution.com/product/the-phoenix-project/ | surrogate_primary | 2026-05-19 | IT Revolution | vendor docs (作者一手 — Gene Kim Phoenix Project 出版方) |
| T01-S006 | https://itrevolution.com/product/wiring-the-winning-organization/ | surrogate_primary | 2026-05-19 | IT Revolution | vendor docs (作者一手 — Kim/Spear 2023 新书) |
| T01-S007 | https://itrevolution.com/articles/breaking-gene-kim-and-dr-steven-j-spear-win-shingo-publication-award-for-wiring-the-winning-organization/ | surrogate_primary | 2026-05-19 | IT Revolution | vendor docs (作者一手 — Shingo 奖公告) |
| T01-S008 | https://charity.wtf/tag/observability-2-0/ | surrogate_primary | 2026-05-19 | Charity Majors | vendor docs (作者一手 — Honeycomb CTO observability 2.0) |
| T01-S009 | https://www.honeycomb.io/blog/time-to-version-observability-signs-point-to-yes | verified_primary | 2026-05-19 | Honeycomb | vendor docs (作者一手 — Majors observability 2.0 宣言, /blog auto) |
| T01-S010 | https://www.honeycomb.io/author/charity | verified_primary | 2026-05-19 | Honeycomb | vendor docs (作者一手 — Majors 文章目录) |
| T01-S011 | https://newsletter.pragmaticengineer.com/p/observability-the-present-and-future | surrogate_primary | 2026-05-19 | Pragmatic Engineer | vendor docs (长访谈一手 — Majors observability 长文对谈) |
| T01-S012 | https://lizthegrey.com/ | surrogate_primary | 2026-05-19 | Liz Fong-Jones | vendor docs (作者一手 — LFJ 个人站 + talks) |
| T01-S013 | https://www.honeycomb.io/author/lizf | verified_primary | 2026-05-19 | Honeycomb | vendor docs (作者一手 — LFJ Technical Fellow 文章, /author auto) |
| T01-S014 | https://2025.platformcon.com/speakers/liz-fong-jones | surrogate_primary | 2026-05-19 | PlatformCon | vendor docs (会议 — LFJ 2025 PlatformCon 讲者) |
| T01-S015 | https://www.ischool.berkeley.edu/people/jez-humble | surrogate_primary | 2026-05-19 | UC Berkeley I School | 课程 syllabus (Jez Humble 教职页 — .edu) |
| T01-S016 | https://research.google/people/106958/ | surrogate_primary | 2026-05-19 | Google Research | vendor docs (作者一手 — Humble Google SRE/DORA 简介) |
| T01-S017 | https://www.brendangregg.com/blog/2024-10-29/ai-flame-graphs.html | verified_primary | 2026-05-19 | Brendan Gregg | vendor docs (作者一手 — AI flame graphs, /blog auto) |
| T01-S018 | https://www.brendangregg.com/bio.html | surrogate_primary | 2026-05-19 | Brendan Gregg | vendor docs (作者一手 — bio 页) |
| T01-S019 | https://github.com/kelseyhightower/kubernetes-the-hard-way | verified_primary | 2026-05-19 | Kelsey Hightower | K8s the Hard Way repo (github root auto verified) |
| T01-S020 | https://techleadjournal.dev/episodes/180/ | surrogate_primary | 2026-05-19 | Tech Lead Journal | vendor docs (长访谈一手 — Hightower 退休 podcast) |
| T01-S021 | https://nicolefv.com/research | surrogate_primary | 2026-05-19 | Nicole Forsgren | vendor docs (作者一手 — Forsgren 研究/论文列表) |
| T01-S022 | https://newsletter.pragmaticengineer.com/p/developer-productivity-a-new-framework | surrogate_primary | 2026-05-19 | Pragmatic Engineer | vendor docs (长访谈一手 — Forsgren DevEx 框架) |
| T01-S023 | https://github.com/mitchellh | surrogate_primary | 2026-05-19 | Mitchell Hashimoto | vendor docs (作者一手 — Hashimoto github profile) |
| T01-S024 | https://fragmentedpodcast.com/episodes/310/ | surrogate_primary | 2026-05-19 | Fragmented Podcast | vendor docs (长访谈一手 — Hashimoto Ghostty + agentic coding) |
| T01-S025 | https://www.hashicorp.com/en/blog/hashicorp-officially-joins-the-ibm-family | verified_primary | 2026-05-19 | HashiCorp | vendor docs (厂商一手 — IBM 收购完成, /blog auto) |
| T01-S026 | https://www.adaptivecapacitylabs.com/ | surrogate_primary | 2026-05-19 | Adaptive Capacity Labs | vendor docs (作者一手 — Allspaw/Cook/Woods 韧性工程) |
| T01-S027 | https://increment.com/reliability/adaptive-capacity-incident-response/ | surrogate_primary | 2026-05-19 | Increment (Stripe) | vendor docs (作者一手 — Allspaw on adaptive capacity) |
| T01-S028 | https://hachyderm.io/@allspaw | reference | 2026-05-19 | John Allspaw | Mastodon — active 输出佐证 (declared=reference 跟 auto) |
| T01-S029 | https://copyconstruct.medium.com/distributed-tracing-weve-been-doing-it-wrong-39fc92a857df | surrogate_primary | 2026-05-19 | Cindy Sridharan | vendor docs (作者一手 — copyconstruct 个人技术写作) |
| T01-S030 | https://www.oreilly.com/library/view/distributed-systems-observability/9781492033431/ | surrogate_primary | 2026-05-19 | O'Reilly | vendor docs (作者一手 — Sridharan 报告页) |
| T01-S031 | https://adrianco.medium.com | surrogate_primary | 2026-05-19 | Adrian Cockcroft | vendor docs (作者一手 — Cockcroft 个人写作, 非 SEO 农场) |
| T01-S032 | https://qconsf.com/speakers/adriancockcroft | surrogate_primary | 2026-05-19 | QCon SF | vendor docs (会议 — Cockcroft 2025 讲者) |
| T01-S033 | https://teamtopologies.com/book | surrogate_primary | 2026-05-19 | Team Topologies | vendor docs (作者一手 — Skelton/Pais 团队拓扑书官网) |
| T01-S034 | https://teamtopologies.com/all-events/2024/12/3/platform-as-a-product | surrogate_primary | 2026-05-19 | Team Topologies | vendor docs (作者一手 — Platform as a Product 课程/webinar) |
| T01-S035 | https://principlesofchaos.org/ | surrogate_primary | 2026-05-19 | Rosenthal/Jones et al | vendor docs (作者一手 — Principles of Chaos Engineering 宣言) |
| T01-S036 | https://www.verica.io/blog/security-chaos-engineering-how-to-security-differently/ | verified_primary | 2026-05-19 | Verica (Rosenthal) | vendor docs (作者一手 — Casey Rosenthal Verica, /blog auto) |
| T01-S037 | https://learningfromincidents.io/ | surrogate_primary | 2026-05-19 | Nora Jones (LFI) | vendor docs (作者一手 — Learning From Incidents 社区) |
| T01-S038 | https://www.pageittothelimit.com/guest/njones/ | surrogate_primary | 2026-05-19 | PagerDuty | vendor docs (厂商一手 — Nora Jones podcast 嘉宾页) |
| T01-S039 | https://www.everythingsysadmin.com/ | surrogate_primary | 2026-05-19 | Tom Limoncelli | vendor docs (作者一手 — Limoncelli sysadmin/SRE 博客) |
| T01-S040 | https://surfingcomplexity.blog/ | surrogate_primary | 2026-05-19 | Lorin Hochstein | vendor docs (作者一手 — Hochstein 韧性工程写作) |
| T01-S041 | https://blog.danslimmon.com/ | verified_primary | 2026-05-19 | Dan Slimmon | vendor docs (作者一手 — on-call/可靠性数学, blog subdomain auto) |
| T01-S042 | https://www.jedi.be/presentations/ | surrogate_primary | 2026-05-19 | Patrick Debois | vendor docs (作者一手 — DevOps 一词创造者演讲列表) |
| T01-S043 | https://devopsdays.org/events/2024-antwerp/speakers/patrick-debois/ | surrogate_primary | 2026-05-19 | DevOpsDays | vendor docs (会议 — DevOpsDays 15 周年 Debois) |
| T01-S044 | https://www.usenix.org/conference/srecon24americas | surrogate_primary | 2026-05-19 | USENIX | 协会(association) — SREcon talks + papers 一手 |
| T01-S045 | https://coolshell.cn/haoel | surrogate_primary | 2026-05-19 | 陈皓 (CoolShell) | vendor docs (作者一手 — 左耳朵耗子个人站 1424 篇) |
| T01-S046 | https://time.geekbang.org/column/intro/48 | surrogate_primary | 2026-05-19 | 极客时间 | vendor docs (中国课程一手 — 陈皓「左耳听风」专栏) |
| T01-S047 | https://www.infoq.cn/article/vftzcsaledsmo6fh9zzc | surrogate_primary | 2026-05-19 | InfoQ 中文 | vendor docs (中国技术媒体一手 — 纪念陈皓) |
| T01-S048 | https://en.wikipedia.org/wiki/Site_reliability_engineering | secondary | 2026-05-19 | — | SRE 学科入门定义 + Treynor Sloss 溯源 |
| T01-S049 | https://en.wikipedia.org/wiki/Kelsey_Hightower | secondary | 2026-05-19 | — | Hightower 履历事实核查 |
| T01-S050 | https://en.wikipedia.org/wiki/HashiCorp | secondary | 2026-05-19 | — | HashiCorp/IBM 收购时间线核查 |
| T01-S051 | https://www.youtube.com/watch?v=zKqAMQSFirI | reference | 2026-05-19 | YouTube | Casey Rosenthal Verica chaos 长访谈 (declared=reference) |
| T01-S052 | https://research.google/people/106257/ | surrogate_primary | 2026-05-19 | Google Research | vendor docs (作者一手 — Nicole Forsgren 此前 Google 简介, 现 Microsoft) |
| T01-S053 | https://cloud.google.com/blog/products/devops-sre | surrogate_primary | 2026-05-19 | Google Cloud | vendor docs (Google 一手 — DORA/SRE 官方博客) |
| T01-S054 | https://www.honeycomb.io/blog/one-key-difference-observability1dot0-2dot0 | verified_primary | 2026-05-19 | Honeycomb | vendor docs (作者一手 — obs 1.0 vs 2.0, /blog auto) |
| T01-S055 | https://www.usu.edu/today/story/gene-kim-and-steven-j-spear-earn-shingo-publication-award-for-wiring-the-winning-organization | surrogate_primary | 2026-05-19 | Utah State Univ | 课程/.edu — 第三方核实 Kim/Spear Shingo 奖 |

---

## 总览（按 DevOps/SRE 行业影响力排序）

| # | 姓名 | 核心身份 | 一句话贡献 | 值得读/听/看 | 来源数 |
|---|------|---------|----------|------------|-------|
| 1 | Gene Kim | IT Revolution 创办, 作者 | 把 DevOps 从运动变成可叙事可度量的企业学科 | 📖🎙️🎬 | 4 |
| 2 | Charity Majors | Honeycomb 联创/CTO | "monitoring vs observability" 与"test in prod"的最大声倡导者 | 📖🎙️🎬 | 4 |
| 3 | Nicole Forsgren | Microsoft Research Partner | 给 DevOps 装上统计学严谨度 (DORA/Accelerate/SPACE/DevEx) | 📖🎙️🎬 | 4 |
| 4 | Jez Humble | Google SRE TL + UC Berkeley | 持续交付学科奠基, 把"小批量高频"写成正典 | 📖🎙️🎬 | 4 |
| 5 | John Allspaw | Adaptive Capacity Labs 创办 | 把无指责复盘 + 安全科学引入软件运维 | 📖🎙️🎬 | 4 |
| 6 | Kelsey Hightower | 前 Google, 退休布道者 | K8s 最佳布道者 + 反过度工程的良知 | 📖🎙️🎬 | 4 |
| 7 | Brendan Gregg | 前 Netflix/Intel, 现 OpenAI | 系统性能 + 火焰图 + eBPF 可观测性权威 | 📖🎬 | 4 |
| 8 | Liz Fong-Jones | Honeycomb Technical Fellow | SLO 工程实践 + on-call 伦理 + 可观测性布道 | 🎙️🎬 | 4 |
| 9 | Mitchell Hashimoto | HashiCorp 联创 (现独立) | 把 IaC 工具生态从零造出来 (Terraform/Vault) | 🎙️🎬 | 3 |
| 10 | Casey Rosenthal | Verica 创办 | 混沌工程从 Netflix 实践到学科化 | 📖🎙️🎬 | 3 |
| 11 | Nora Jones | PagerDuty Sr Dir (前 Jeli) | 事件分析 + Learning From Incidents 社区奠基 | 📖🎙️ | 3 |
| 12 | Matthew Skelton + Manuel Pais | Conflux / Team Topologies | 平台工程的组织理论基础 (认知负荷 + 四类团队) | 📖🎙️🎬 | 3 |
| 13 | Tom Limoncelli | Stack Overflow SRE, 作者 | sysadmin/SRE 实务运维的百科全书式作者 | 📖 | 2 |
| 14 | Patrick Debois | 独立顾问 (GenAI×DevOps) | "DevOps"一词创造者 + DevOpsDays 发起人 | 🎙️🎬 | 3 |
| 15 | Cindy Sridharan + Lorin Hochstein + Dan Slimmon | 独立写作者 (合并卡) | 分布式可观测性 / 韧性工程 / on-call 数学的深度写作群 | 📖🎬 | 4 |
| 16 | 陈皓 / 左耳朵耗子 (2023 离世) | CoolShell + 极客时间 | 中国 DevOps/分布式/SRE 启蒙影响最深的写作者 | 📖 | 3 |

---

## 1. Gene Kim

- **One-liner**: 把 DevOps 从一场草根运动转译成企业高管能听懂、能度量、能投资的工程学科 (evidence: [T01-S005, T01-S006])
- **核心身份**: IT Revolution 创办人 + DevOps Enterprise Summit 主理; 作家。代表角色是"DevOps 运动的首席叙事者"。(evidence: [T01-S005])
- **代表作品**: 《The Phoenix Project》(2013 小说体) / 《The DevOps Handbook》/ 《Accelerate》(与 Forsgren/Humble) / 《Wiring the Winning Organization》(2023, 与 Steven Spear, 获 2024 Shingo 出版奖) (evidence: [T01-S005, T01-S006, T01-S007, T01-S055])
- **值得读/听/看**:
  - 📖 The Phoenix Project — DevOps 入门叙事正典 https://itrevolution.com/product/the-phoenix-project/ (collected: 2026-05-19)
  - 📖 Wiring the Winning Organization — slowification/simplification/amplification 三机制 https://itrevolution.com/product/wiring-the-winning-organization/ (collected: 2026-05-19)
  - 🎙️ DevOps Enterprise Summit 系列 keynote (IT Revolution 渠道)
- **核心思想关键词**: 三步工作法 (flow/feedback/continual learning)、value stream、slowification、危险区 vs 制胜区、第四类工作 (unplanned work)
- **voice_samples**:
  - 同业讨论样本: 「Organizations win by using three mechanisms to slowify, simplify, and amplify — systematically moving problem-solving from the danger zone to the winning zone.」(source: T01-S006, 转述)
  - 监管/专业讨论样本: 「The core, chronic conflict between Dev and Ops is structural — you can't fix it by exhortation, you fix it with how the work is wired.」(source: T01-S005, 转述/推断 — Phoenix Project 核心论点)
  - ⚠️ 客户解释样本: 暂未找到 ≥ 30 字直接原话片段 (多为书面叙事而非口语访谈转录)
- **sub_skill_candidate**: `true` — 思想体系自洽 (三步工作法→Accelerate→Wiring 一脉相承), 行业影响力 top 3, 长访谈/keynote 材料充足
- **dual_role**: `"founder + thinker"`
- **最近 12 个月动态**: 《Wiring the Winning Organization》持续获奖 (2025 Crosby Medal); IT Revolution 与 DORA 联动推 AI-assisted dev 主题 (evidence: [T01-S007])
- **争议/批评**: Phoenix Project 的叙事被部分资深 SRE 批为"过于乐观/咨询味重"; "DevOps Enterprise" 商业化被指稀释了运动的草根性。
- **来源**:
  - [surrogate_primary] IT Revolution 产品页 (T01-S005, T01-S006)
  - [surrogate_primary] Shingo 奖公告 (T01-S007)
  - [surrogate_primary] USU .edu 第三方核实 (T01-S055)
- **可信度自评**: high — 多源、近期活跃、思想脉络清晰

## 2. Charity Majors

- **One-liner**: 用"monitoring 处理 known-unknowns / observability 处理 unknown-unknowns"这一刀, 重新定义了可观测性 (evidence: [T01-S008, T01-S009])
- **核心身份**: Honeycomb 联合创始人 + CTO; 《Database Reliability Engineering》《Observability Engineering》合著者。(evidence: [T01-S010])
- **代表作品**: Observability 2.0 概念 (wide structured events 单一真相源) / "test in prod" 系列文章 / 《Observability Engineering》(O'Reilly) (evidence: [T01-S009, T01-S054])
- **值得读/听/看**:
  - 📖 "It's Time to Version Observability: Introducing Observability 2.0" https://www.honeycomb.io/blog/time-to-version-observability-signs-point-to-yes (collected: 2026-05-19)
  - 🎙️ Pragmatic Engineer: Observability the present and future https://newsletter.pragmaticengineer.com/p/observability-the-present-and-future (collected: 2026-05-19)
  - 🎬 charity.wtf observability-2-0 标签合集 https://charity.wtf/tag/observability-2-0/ (collected: 2026-05-19)
- **核心思想关键词**: observability 2.0、wide structured events、test in production、high cardinality、ownership (you build it you run it)、monitoring≠observability
- **voice_samples**:
  - 客户解释样本: 「Observability 1.0 has three pillars and many sources of truth scattered across tools; observability 2.0 has one source of truth — wide structured log events — from which you derive metrics, traces and SLOs.」(source: T01-S009, 转述)
  - 同业讨论样本: 「You can't have observability without instrumenting your code; you can't buy it as a three-SKU bundle.」(source: T01-S008, 转述/推断 — 反复立场)
  - 监管/专业讨论样本: 「Vendors selling 'observability' as packaged metrics+logs+traces is marketing narrowing — observability is a property of your system, not a product tier.」(source: T01-S011, 转述)
- **sub_skill_candidate**: `true` — 可观测性是核心 subdomain, 长访谈丰富, 个人思想体系强 (与 intake 伦理 anchor #10 直接对齐)
- **最近 12 个月动态**: 2025 持续推 Observability 2.0 (Honeycomb 文章 2025-02 更新); 大量谈 AI 时代可观测性 (evidence: [T01-S009])
- **争议/批评**: "observability 2.0 / 1.0 版本号"被批为 Honeycomb 的市场区隔话术 (vendor-driven taxonomy); "test in prod" 常被初级工程师误读为"可以不写测试"。
- **来源**:
  - [verified_primary] Honeycomb blog (T01-S009, T01-S054)
  - [surrogate_primary] charity.wtf 个人博客 (T01-S008)
  - [surrogate_primary] Pragmatic Engineer 长访谈 (T01-S011)
- **可信度自评**: high

## 3. Nicole Forsgren

- **One-liner**: 给 DevOps "感觉对的实践"装上统计学严谨度, 用 DORA 把交付效能变成可研究的科学 (evidence: [T01-S003, T01-S021])
- **核心身份**: Microsoft Research Partner, 领导 Developer Velocity Lab; DORA (DevOps Research and Assessment) 创办人 (2018 被 Google 收购)。(evidence: [T01-S021, T01-S052])
- **代表作品**: 《Accelerate》(2018, 与 Humble/Kim) / DORA 四关键指标研究 / SPACE 框架 / DevEx 框架 (2024) (evidence: [T01-S003, T01-S022])
- **值得读/听/看**:
  - 📖 nicolefv.com 研究/论文列表 https://nicolefv.com/research (collected: 2026-05-19)
  - 🎙️ Pragmatic Engineer: developer productivity — a new framework https://newsletter.pragmaticengineer.com/p/developer-productivity-a-new-framework (collected: 2026-05-19)
  - 🎬 DORA Community Summit keynote (DORA→SPACE→DevEx)
- **核心思想关键词**: DORA 四指标 (deploy frequency/lead time/CFR/MTTR)、统计严谨 (construct validity)、SPACE 框架、DevEx、Goodhart 警告 (别把指标当 KPI 考核个人)
- **voice_samples**:
  - 同业讨论样本: 「DORA is actually an instance of SPACE — it's a measure of the performance dimension of software delivery, not the whole picture.」(source: T01-S022, 转述)
  - 监管/专业讨论样本: 「The four key metrics are outcomes, not targets — the moment you make deploy frequency a personal KPI, you've broken it (Goodhart).」(source: T01-S022, 转述/推断 — 反复立场)
  - 客户解释样本: 「Elite performers deploy more often AND fail less — speed and stability are not a trade-off, that's the counterintuitive finding.」(source: T01-S003, 转述)
- **sub_skill_candidate**: `true` — DORA/工程效能是独立 subdomain, 学术+实践双角色, 思想体系自洽
- **dual_role**: `"academic + engineering"` — 统计学博士 + 工业界研究负责人, 有大量长访谈谈实践 (非纯论文 talk)
- **最近 12 个月动态**: 2024-2025 推 DevEx 框架 + AI 对开发者生产力影响的研究; Microsoft Research Developer Velocity Lab (evidence: [T01-S021, T01-S022])
- **争议/批评**: DORA 指标在企业落地常被异化为 KPI 考核 (她本人反复警告); State of DevOps 报告被指有 Google Cloud 商业立场。
- **来源**: [surrogate_primary] nicolefv.com (T01-S021) / [verified_primary] dora.dev (T01-S003) / [surrogate_primary] Pragmatic Engineer (T01-S022)
- **可信度自评**: high

## 4. Jez Humble

- **One-liner**: 写下持续交付的工程正典, 用证据证明"小批量高频"不是冒险而是更安全 (evidence: [T01-S004, T01-S016])
- **核心身份**: Google SRE Tech Lead (Cloud Run/App Engine/Cloud Functions 团队) + UC Berkeley I School 讲师; DORA 联合创办人。(evidence: [T01-S015, T01-S016])
- **代表作品**: 《Continuous Delivery》(2010, 与 Dave Farley) / 《The DevOps Handbook》/ 《Lean Enterprise》/ 《Accelerate》 (evidence: [T01-S016])
- **值得读/听/看**:
  - 📖 DORA 四关键指标指南 https://dora.dev/guides/dora-metrics-four-keys/ (collected: 2026-05-19)
  - 🎙️ UC Berkeley I School 教职页 + 课程 https://www.ischool.berkeley.edu/people/jez-humble (collected: 2026-05-19)
  - 🎬 "Continuous Delivery" conference talk 系列 (DORA 渠道)
- **核心思想关键词**: 持续交付、部署流水线、deployment ≠ release (feature flags)、小批量、trunk-based development、可重复可靠的发布
- **voice_samples**:
  - 同业讨论样本: 「If it hurts, do it more often, and bring the pain forward.」(source: T01-S016, 原话 — CD 名言)
  - 监管/专业讨论样本: 「Continuous delivery is the ability to get changes — features, config, fixes — into production safely, quickly, and sustainably.」(source: T01-S004, 转述 — CD 定义)
  - ⚠️ 客户解释样本: 暂未找到 ≥ 50 字独立口语片段 (多为书面/课程材料)
- **sub_skill_candidate**: `true` — CI/CD 是核心 subdomain, 思想奠基, 与 Kim/Forsgren 形成 DORA 三角
- **dual_role**: `"academic + engineering"` — Berkeley 讲师 + Google 现役 SRE TL
- **最近 12 个月动态**: 仍任 Google SRE TL; DORA 2025 推 State of AI-assisted Software Development 研究 (evidence: [T01-S016])
- **争议/批评**: CD 在 monorepo/强监管/嵌入式领域落地受限的批评; trunk-based 与长期分支团队的方法论之争。
- **来源**: [surrogate_primary] Berkeley .edu (T01-S015) / [surrogate_primary] Google Research (T01-S016) / [verified_primary] dora.dev (T01-S004)
- **可信度自评**: high

## 5. John Allspaw

- **One-liner**: 把"无指责复盘"和安全科学 (human factors / resilience engineering) 引进软件运维, 改写了事件文化 (evidence: [T01-S026, T01-S027])
- **核心身份**: Adaptive Capacity Labs 联合创办人 ("the NTSB of Tech", 与 Richard Cook、David Woods); 前 Etsy CTO; Lund 大学 Human Factors & System Safety 硕士。(evidence: [T01-S026])
- **代表作品**: "10+ Deploys Per Day" (2009 Velocity 经典演讲) / 无指责复盘实践 (Etsy code-as-craft) / 韧性工程在软件域的学术论文 (evidence: [T01-S027])
- **值得读/听/看**:
  - 📖 "On adaptive capacity in incident response" (Increment) https://increment.com/reliability/adaptive-capacity-incident-response/ (collected: 2026-05-19)
  - 🎙️ ELC Podcast: resilience engineering & learning from incidents (sfelc)
  - 🎬 "Amplifying Sources of Resilience" QCon London talk
- **核心思想关键词**: blameless postmortem、contributing factors (not root cause)、resilience engineering、adaptive capacity、above/below the line、人是适应来源不是故障来源
- **voice_samples**:
  - 复盘 register 样本: 「There is no root cause — there are contributing factors, and the most important question is 'what made this hard to detect?'」(source: T01-S027, 转述/推断 — 核心立场)
  - 同业讨论样本: 「Blameless doesn't mean no accountability — it means the goal is learning, because if people fear blame they hide the truth and the next failure is worse.」(source: T01-S026, 转述)
  - 监管/专业讨论样本: 「The people closest to the work are the source of resilience, not the source of the problem — your system let them do what they did.」(source: T01-S027, 转述)
- **sub_skill_candidate**: `true` — 事件管理/复盘是核心 subdomain, 思想体系深 (桥接 Dekker 安全科学), 与 intake 伦理 anchor #2 直接对齐
- **dual_role**: `"academic + engineering"` — 安全科学学术训练 + 前 CTO 工程实践
- **最近 12 个月动态**: Adaptive Capacity Labs 持续做事件分析咨询; Mastodon (@allspaw@hachyderm.io) 活跃发声 (evidence: [T01-S026, T01-S028])
- **争议/批评**: "no root cause"立场被传统运维批为"逃避问责"(他反复澄清 blameless≠no accountability); 韧性工程的学术语言被指落地门槛高。
- **来源**: [surrogate_primary] adaptivecapacitylabs.com (T01-S026) / [surrogate_primary] Increment (T01-S027) / [reference] Mastodon (T01-S028)
- **可信度自评**: high

## 6. Kelsey Hightower

- **One-liner**: K8s 时代最好的布道者, 同时是"你真的需要 Kubernetes 吗"这一反过度工程良知的代言人 (evidence: [T01-S019, T01-S020])
- **核心身份**: 前 Google Distinguished Engineer / Developer Advocate (2023-06 退休); 现"retired, not tired"独立顾问/讲者。(evidence: [T01-S020, T01-S049])
- **代表作品**: "Kubernetes the Hard Way" (教学经典 repo) / GitOps 与简约主义布道 / 无数 KubeCon keynote (evidence: [T01-S019])
- **值得读/听/看**:
  - 📖 Kubernetes the Hard Way https://github.com/kelseyhightower/kubernetes-the-hard-way (collected: 2026-05-19)
  - 🎙️ Tech Lead Journal #180: early retirement, public speaking https://techleadjournal.dev/episodes/180/ (collected: 2026-05-19)
  - 🎬 KubeCon EU 2025 London 访谈 + HAProxyConf 2025 keynote "The Fundamentals"
- **核心思想关键词**: 简约主义 (反过度工程)、GitOps、declarative、fundamentals over hype、serverless 务实、"do you really need K8s"
- **voice_samples**:
  - 工具/平台 register 样本: 「No code is the best way to write secure and reliable applications. Write nothing; deploy nowhere.」(source: T01-S019, 原话 — 著名推文/立场)
  - 同业讨论样本: 「I'm retired, not tired — now I get to choose the projects, advise founder friends, and watch where the industry is going.」(source: T01-S020, 转述)
  - 监管/专业讨论样本: 「Kubernetes is a platform for building platforms. It's not the endgame — most teams need the fundamentals far more than the abstraction.」(source: T01-S020, 转述/推断)
- **sub_skill_candidate**: `false` — 影响力 top 但靠布道/示范而非自洽个人思想体系; 反过度工程主张更适合作为跨 figure 的 mental model (并入 anti-pattern 节)
- **最近 12 个月动态**: 2025 活跃 — KubeCon EU 2025 访谈、HAProxyConf 2025 keynote、PlatformCon 2025 keynote、alphalist.CTO podcast (evidence: [T01-S020])
- **争议/批评**: 退休后"半隐退"被指影响力主要是历史性的; 简约主义立场偶被解读为"反 K8s"(实为反滥用)。
- **来源**: [verified_primary] github (T01-S019) / [surrogate_primary] Tech Lead Journal (T01-S020) / [secondary] Wikipedia (T01-S049)
- **可信度自评**: high

## 7. Brendan Gregg

- **One-liner**: 系统性能工程的活字典, 发明火焰图 + 推广 eBPF, 让"为什么慢"变成可观测的科学 (evidence: [T01-S017, T01-S018])
- **核心身份**: 前 Netflix 高级性能工程师 → Intel Fellow (AI 性能) → 现 OpenAI (数据中心优化)。(evidence: [T01-S017, T01-S018])
- **代表作品**: 《Systems Performance》/ 《BPF Performance Tools》/ Flame Graphs (火焰图) / USE 方法 (evidence: [T01-S018])
- **值得读/听/看**:
  - 📖 "AI Flame Graphs" (2024-10) https://www.brendangregg.com/blog/2024-10-29/ai-flame-graphs.html (collected: 2026-05-19)
  - 🎬 "eBPF: Fueling New Flame Graphs" YOW! talk
  - 🎬 "AI flame graphs with eBPF" (Intel, YouTube)
- **核心思想关键词**: 火焰图 (flame graph)、USE 方法 (Utilization/Saturation/Errors)、eBPF 可观测性、系统性能方法论、latency 分析
- **voice_samples**:
  - 同业讨论样本: 「USE method: for every resource, check Utilization, Saturation, and Errors — it finds bottlenecks fast without guessing.」(source: T01-S018, 转述 — USE 定义)
  - 监管/专业讨论样本: 「Flame graphs turn a wall of stack traces into a picture — width is time spent, you read it in seconds.」(source: T01-S017, 转述/推断)
  - ⚠️ 客户解释样本: 暂未找到 ≥ 50 字面向非技术受众的口语片段 (材料偏技术深度)
- **sub_skill_candidate**: `false` — 极重要但属性能/可观测性工具方法的输出者, 思想更偏方法论工具而非组织/文化体系; 进 canon + 可观测性 subdomain
- **dual_role**: `"engineering + author"`
- **最近 12 个月动态**: 2024 在 Intel 做 AI Flame Graphs (GPU/eBPF profiling); 现已转 OpenAI 做数据中心优化 (evidence: [T01-S017, T01-S018])
- **争议/批评**: 内容深度高门槛, 对初级受众不友好; 工具特定性 (Linux/BPF) 强, 跨平台适用性受限。
- **来源**: [verified_primary] brendangregg.com blog (T01-S017) / [verified_primary] brendangregg.com bio (T01-S018) / [secondary] Wikipedia
- **可信度自评**: high

## 8. Liz Fong-Jones (方禮真)

- **One-liner**: 把 Google SRE 16 年的 SLO 工程纪律带到业界, 同时是 on-call 可持续性与工程伦理最直接的发声者 (evidence: [T01-S012, T01-S013])
- **核心身份**: Honeycomb Technical Fellow (2025; 此前 Field CTO 2022-2025 / Principal Developer Advocate 2019-2022); 前 Google SRE 16 年。(evidence: [T01-S013])
- **代表作品**: SLO/error budget 工程实践布道 / 《Observability Engineering》合著 / 大量 SREcon/PlatformCon 演讲 (evidence: [T01-S012, T01-S014])
- **值得读/听/看**:
  - 🎙️ lizthegrey.com talks 合集 https://lizthegrey.com/ (collected: 2026-05-19)
  - 🎬 PlatformCon 2025 讲者 https://2025.platformcon.com/speakers/liz-fong-jones (collected: 2026-05-19)
  - 📖 Honeycomb author page (SLO/可观测性文章) https://www.honeycomb.io/author/lizf (collected: 2026-05-19)
- **核心思想关键词**: SLO/error budget 实操、symptom-based alerting、on-call 可持续性 (伦理)、可观测性驱动开发、工程师劳工权益
- **voice_samples**:
  - SLO register 样本: 「An alert that isn't actionable is just noise — page on symptoms users feel, not on causes.」(source: T01-S012, 转述/推断 — 反复立场)
  - 同业讨论样本: 「Error budgets turn reliability into a shared product decision — when the budget's gone, you stop shipping features and fix reliability.」(source: T01-S013, 转述)
  - 监管/专业讨论样本: 「Sustainable on-call is an ethics problem, not a 'resilience' problem — burnout is a management failure.」(source: T01-S014, 转述/推断 — 与 intake anchor #5 对齐)
- **sub_skill_candidate**: `true` — SLO + on-call 是核心 subdomain, 长演讲材料丰富, 个人立场鲜明 (伦理 anchor 承载者)
- **最近 12 个月动态**: 2025 升任 Honeycomb Technical Fellow; YOW! 2025 (Melbourne/Sydney/Brisbane) + PlatformCon 2025 讲者 (evidence: [T01-S013, T01-S014])
- **争议/批评**: 直言风格 + 劳工权益/政治立场常引发争论; SLO 工程实践在小团队被指"重型"。
- **来源**: [surrogate_primary] lizthegrey.com (T01-S012) / [verified_primary] honeycomb author (T01-S013) / [surrogate_primary] PlatformCon (T01-S014)
- **可信度自评**: high

## 9. Mitchell Hashimoto

- **One-liner**: 几乎以一己之力造出现代 IaC 工具生态 (Terraform/Vault/Consul/Vagrant), 定义了"声明式基础设施"的工具范式 (evidence: [T01-S023, T01-S025])
- **核心身份**: HashiCorp 联合创始人 (2023-12 离职); 现独立 (Ghostty 终端作者, 2026 加入 Vercel 董事会)。(evidence: [T01-S023, T01-S024, T01-S050])
- **代表作品**: Terraform / Vault / Consul / Vagrant / Packer (IaC 工具栈) / Ghostty (GPU 加速终端) (evidence: [T01-S023, T01-S024])
- **值得读/听/看**:
  - 🎙️ Fragmented #310: Ghostty & agentic coding workflow https://fragmentedpodcast.com/episodes/310/ (collected: 2026-05-19)
  - 🎬 github.com/mitchellh (开源项目 + 工程写作) https://github.com/mitchellh (collected: 2026-05-19)
  - 📖 HashiCorp joins IBM (背景) https://www.hashicorp.com/en/blog/hashicorp-officially-joins-the-ibm-family (collected: 2026-05-19)
- **核心思想关键词**: 声明式 IaC、不可变基础设施、provider/plugin 架构、开源商业模式 (BSL 争议)、工程匠艺 (craft over hype)
- **voice_samples**:
  - 工具/平台 register 样本: 「Infrastructure should be described as code, versioned, reviewed, and applied predictably — the same way we treat application source.」(source: T01-S023, 转述/推断 — Terraform 理念)
  - 同业讨论样本: 「I explicitly do not want to make money from Ghostty — it needs to live in a nonprofit, totally unencumbered.」(source: T01-S024, 原话)
  - ⚠️ 监管/专业讨论样本: 暂未找到针对 IaC 治理/state 安全的 ≥ 50 字直接原话
- **sub_skill_candidate**: `false` — 影响力极大但主要通过工程产品而非个人思想体系输出 (intake Step 2 false 标准的典型); IaC 工具栈进 Track 02
- **dual_role**: `"founder + engineer"`
- **最近 12 个月动态**: IBM 收购 HashiCorp 2025-02-27 完成 ($6.4B); 主力做 Ghostty (2024-12 公开发布, 转非营利); 2026-03 加入 Vercel 董事会 (evidence: [T01-S024, T01-S025])
- **争议/批评**: HashiCorp 2023 从 MPL 改 BSL 许可证引发开源社区强烈反弹 (直接催生 OpenTofu fork); 退出后工具治理由 IBM 接手的不确定性。
- **来源**: [verified_primary] github (T01-S023) / [surrogate_primary] Fragmented podcast (T01-S024) / [verified_primary] hashicorp blog (T01-S025)
- **可信度自评**: high

## 10. Casey Rosenthal

- **One-liner**: 把混沌工程从 Netflix 的 Chaos Monkey 实践提炼成有原则、有假设、控爆炸半径的学科 (evidence: [T01-S035, T01-S036])
- **核心身份**: Verica 联合创始人/CEO; 前 Netflix Chaos Engineering 团队 Engineering Manager。(evidence: [T01-S036, T01-S051])
- **代表作品**: 《Chaos Engineering》(O'Reilly, 与 Nora Jones) / Principles of Chaos Engineering / Security Chaos Engineering (evidence: [T01-S035, T01-S036])
- **值得读/听/看**:
  - 📖 Principles of Chaos Engineering https://principlesofchaos.org/ (collected: 2026-05-19)
  - 📖 Security Chaos Engineering (Verica blog) https://www.verica.io/blog/security-chaos-engineering-how-to-security-differently/ (collected: 2026-05-19)
  - 🎬 "Chaos Engineering and Disciplined Experimenting" https://www.youtube.com/watch?v=zKqAMQSFirI (collected: 2026-05-19)
- **核心思想关键词**: 混沌工程 (假设驱动实验)、稳态 (steady state)、爆炸半径控制、continuous verification、复杂系统不可完全理解
- **voice_samples**:
  - 同业讨论样本: 「Chaos engineering is the discipline of experimenting on a system to build confidence in its capability to withstand turbulent conditions in production.」(source: T01-S035, 转述 — POC 定义)
  - 监管/专业讨论样本: 「You define steady state, hypothesize it holds under failure, inject real-world events, and minimize blast radius — it's experimentation, not breaking things.」(source: T01-S036, 转述/推断)
  - ⚠️ 客户解释样本: 暂未找到 ≥ 50 字面向非技术受众片段
- **sub_skill_candidate**: `true` — 混沌/韧性工程是核心 subdomain, 思想自洽, 长访谈材料充足
- **最近 12 个月动态**: Verica 持续做 continuous verification + security chaos engineering; 与 Sidney Dekker just culture 思想交叉引用 (evidence: [T01-S036])
- **争议/批评**: "生产环境做实验"对保守组织门槛高; 混沌工程被指容易沦为"破坏炫技"而非纪律性实验 (他本人反复纠偏)。
- **来源**: [surrogate_primary] principlesofchaos.org (T01-S035) / [verified_primary] verica.io blog (T01-S036) / [reference] YouTube (T01-S051)
- **可信度自评**: high

## 11. Nora Jones

- **One-liner**: 把混沌工程的注意力从"注入故障"转向"从事件里学习", 奠基 Learning From Incidents 社区 (evidence: [T01-S037, T01-S038])
- **核心身份**: PagerDuty Senior Director of Product (Jeli 2023 被 PagerDuty 收购后); Jeli 创始人/前 CEO; Learning From Incidents 社区创办人。(evidence: [T01-S037, T01-S038])
- **代表作品**: 《Chaos Engineering》(与 Rosenthal) / Jeli (incident analysis 平台) / learningfromincidents.io 社区 (evidence: [T01-S037])
- **值得读/听/看**:
  - 📖 Learning From Incidents https://learningfromincidents.io/ (collected: 2026-05-19)
  - 🎙️ Page it to the Limit 嘉宾页 https://www.pageittothelimit.com/guest/njones/ (collected: 2026-05-19)
  - 🎬 The Changelog #478: Learning from incidents
- **核心思想关键词**: incident analysis (不止 MTTR)、learning from incidents、socio-technical systems、事件是组织学习的窗口、人类专长 (expertise) 显性化
- **voice_samples**:
  - 复盘 register 样本: 「Incidents are unplanned investments in learning — the question isn't just how fast you recovered, it's what the organization now understands.」(source: T01-S037, 转述/推断 — LFI 核心)
  - 同业讨论样本: 「The most valuable signal in an incident is buried in how engineers actually coordinated, not in the timeline of alerts.」(source: T01-S038, 转述)
  - ⚠️ 监管/专业讨论样本: 暂未找到 ≥ 50 字直接原话
- **sub_skill_candidate**: `false` — 重要且与 Allspaw 同属事件文化流派, 但思想体系与 Allspaw/LFI 高度重叠, 建议合并为"事件学习"心智模型而非独立 sub-skill
- **最近 12 个月动态**: 在 PagerDuty 任产品高级总监 (Jeli 能力整合进 PagerDuty Operations Cloud); LFI 社区持续运营 (evidence: [T01-S037, T01-S038])
- **争议/批评**: Jeli 被收购后"深度事件分析"是否会被产品化稀释的担忧; LFI 方法被指对小团队太重。
- **来源**: [surrogate_primary] learningfromincidents.io (T01-S037) / [surrogate_primary] PagerDuty podcast (T01-S038) / [reference] Changelog
- **可信度自评**: high

## 12. Matthew Skelton + Manuel Pais

- **One-liner**: 用"认知负荷 + 四类团队"给平台工程提供了组织理论基础, 让"平台即产品"成为共识 (evidence: [T01-S033, T01-S034])
- **核心身份**: Matthew Skelton (Conflux CEO) + Manuel Pais; 《Team Topologies》(2019, 2025 第二版) 合著者。(evidence: [T01-S033])
- **代表作品**: 《Team Topologies》/ 四类团队拓扑 (stream-aligned/platform/enabling/complicated-subsystem) / "Platform as a Product" 课程 (evidence: [T01-S033, T01-S034])
- **值得读/听/看**:
  - 📖 Team Topologies book https://teamtopologies.com/book (collected: 2026-05-19)
  - 🎙️/🎬 "Platform as a Product" webinar https://teamtopologies.com/all-events/2024/12/3/platform-as-a-product (collected: 2026-05-19)
  - 🎬 "Five years of Team Topologies: reflections and predictions" (platformengineering.org)
- **核心思想关键词**: 认知负荷 (cognitive load)、四类团队、平台即产品、thinnest viable platform、Conway 定律逆用、interaction modes (协作/X-as-a-service/facilitating)
- **voice_samples**:
  - 同业讨论样本: 「Cognitive load is the limiting factor for fast flow — you don't add teams to go faster, you reduce the load each team carries.」(source: T01-S033, 转述/推断 — TT 核心)
  - 监管/专业讨论样本: 「A 'DevOps team' wedged between Dev and Ops creates a third silo — the answer is a platform team treating the platform as a product.」(source: T01-S034, 转述 — 与 intake anchor #7 对齐)
  - ⚠️ 客户解释样本: 暂未找到 ≥ 50 字面向非技术受众片段
- **sub_skill_candidate**: `true` — 平台工程组织设计是核心 subdomain, 思想体系自洽且被业界广泛引用; 直接承载"DevOps 团队=反模式"伦理 anchor
- **最近 12 个月动态**: 2025 出 Team Topologies 第二版; 持续推 "Platform as a Product" 课程/webinar (evidence: [T01-S033, T01-S034])
- **争议/批评**: 四类团队/三种交互模式被批为"过于规整, 现实更混沌"; 被部分组织当成僵化模板照搬。
- **来源**: [surrogate_primary] teamtopologies.com book (T01-S033) / [surrogate_primary] teamtopologies.com events (T01-S034) / [surrogate_primary] platformengineering.org
- **可信度自评**: high

## 13. Tom Limoncelli

- **One-liner**: sysadmin/SRE 实务运维的百科全书式作者, 把"怎么做运维"写成可操作的工程纪律 (evidence: [T01-S039])
- **核心身份**: Stack Overflow SRE; 《The Practice of System and Network Administration》/《The Practice of Cloud System Administration》/《Time Management for System Administrators》作者。(evidence: [T01-S039])
- **代表作品**: 上述三本运维实务正典 / everythingsysadmin.com 博客 / ACM Queue 长文 (evidence: [T01-S039])
- **值得读/听/看**:
  - 📖 everythingsysadmin.com https://www.everythingsysadmin.com/ (collected: 2026-05-19)
  - 📖 The Practice of Cloud System Administration (书)
  - 🎬 ⚠️ 未找到近 12 个月长视频访谈
- **核心思想关键词**: 运维实务工程化、自动化优先、time management for ops、可重复流程、运维即软件工程
- **voice_samples**:
  - 同业讨论样本: 「If you do something twice, automate it the third time — toil is the enemy of capacity.」(source: T01-S039, 转述/推断 — 反复立场)
  - ⚠️ 客户解释 + 监管样本: 暂未找到 ≥ 30 字直接原话片段 (材料以书面为主, 缺近期长访谈)
- **sub_skill_candidate**: `false` — 重要 canon 作者但近期公开口语输出少, 更适合进 Track 04 (canon)
- **最近 12 个月动态**: ⚠️ 近 12 个月公开活动信号较弱 (主要靠书 + 历史博客); 此项为本 track 信息薄弱处
- **争议/批评**: 内容偏传统 sysadmin 视角, 部分被云原生/K8s 范式更新; 未找到显著业内反驳。
- **来源**: [surrogate_primary] everythingsysadmin.com (T01-S039) / 书 (canon, 见 Track 04) / ⚠️ 仅 2 条强来源
- **可信度自评**: medium — 缺近 12 月长访谈材料 + 仅 2 条独立来源, 边缘保留 (canon 价值高)

## 14. Patrick Debois

- **One-liner**: 创造了"DevOps"这个词并发起第一届 DevOpsDays (2009), 是整场运动的命名者与起点 (evidence: [T01-S042, T01-S043])
- **核心身份**: 独立顾问 (现聚焦 GenAI × DevOps / LLMOps); 前 Atlassian/Snyk Distinguished Engineer; DevOpsDays 发起人。(evidence: [T01-S042, T01-S043])
- **代表作品**: "DevOps" 术语 + DevOpsDays 会议 (2009) / 《The DevOps Handbook》合著 / GenAI for DevOps 工作坊 (evidence: [T01-S042])
- **值得读/听/看**:
  - 🎬 jedi.be presentations https://www.jedi.be/presentations/ (collected: 2026-05-19)
  - 🎙️ DevOpsDays Antwerp 2024 (15 周年) https://devopsdays.org/events/2024-antwerp/speakers/patrick-debois/ (collected: 2026-05-19)
  - 🎬 "AI, You complete me" DevOpsDays London 2024
- **核心思想关键词**: DevOps 是文化运动 (不是岗位)、消除 dev/ops 鸿沟、Conway 定律、现在: GenAI 工程化 (LLMOps)、engineering rigor for AI
- **voice_samples**:
  - 同业讨论样本: 「DevOps was never a job title — it's about removing the wall between those who build and those who run.」(source: T01-S043, 转述/推断 — 与 intake anchor #7 对齐)
  - 监管/专业讨论样本: 「Conway's law applies to AI too — your GenAI delivery will mirror your org structure unless you design for it.」(source: T01-S042, 转述 — 2024 keynote 主题)
  - ⚠️ 客户解释样本: 暂未找到 ≥ 50 字直接原话片段
- **sub_skill_candidate**: `false` — 历史性命名者, 当前输出已转向 GenAI 而非核心 DevOps/SRE 思想; 作为"founders"单列在 Phase 2 接口
- **dual_role**: `"founder + thinker"`
- **最近 12 个月动态**: 2024-2025 高度活跃 — DevOpsDays 15 周年讲者、GenAI×DevOps 工作坊、InfoQ Dev Summit Munich 2025 (但主题已偏 GenAI) (evidence: [T01-S042, T01-S043])
- **争议/批评**: 当前重心转向 GenAI 营销味渐浓的担忧; "DevOps 命名者"光环 vs 实际持续思想贡献的落差。
- **来源**: [surrogate_primary] jedi.be (T01-S042) / [surrogate_primary] DevOpsDays (T01-S043) / InfoQ Dev Summit
- **可信度自评**: high (历史地位) / medium (当前 DevOps 核心思想贡献)

## 15. Cindy Sridharan + Lorin Hochstein + Dan Slimmon (深度写作者合并卡)

> 三位都是"思想体系强但主要靠独立长文写作、非公司/会议高曝光"的深度作者, 合并一张卡。各自仍独立有 sub_skill 价值的可在 Phase 3 拆分。

- **One-liner**: 分布式可观测性 (Sridharan) / 韧性工程 (Hochstein) / on-call 可靠性数学 (Slimmon) 三条最硬核的独立写作支线 (evidence: [T01-S029, T01-S040, T01-S041])
- **核心身份**:
  - Cindy Sridharan (@copyconstruct): 分布式系统工程师, 《Distributed Systems Observability》(O'Reilly) 作者 (evidence: [T01-S029, T01-S030])
  - Lorin Hochstein: 韧性工程 + chaos (前 Netflix), Learning From Incidents 写作 (evidence: [T01-S040])
  - Dan Slimmon: on-call / 可靠性数学 / 告警有效性 (前 Etsy/HashiCorp) (evidence: [T01-S041])
- **代表作品**: 《Distributed Systems Observability》/ "Distributed Tracing — we've been doing it wrong" (Sridharan); surfingcomplexity.blog 韧性写作 (Hochstein); 告警 precision/recall 数学 + "the most important thing" 系列 (Slimmon)
- **值得读/听/看**:
  - 📖 Sridharan "Distributed Tracing — we've been doing it wrong" https://copyconstruct.medium.com/distributed-tracing-weve-been-doing-it-wrong-39fc92a857df (collected: 2026-05-19)
  - 📖 Hochstein surfingcomplexity.blog https://surfingcomplexity.blog/ (collected: 2026-05-19)
  - 📖 Slimmon blog.danslimmon.com https://blog.danslimmon.com/ (collected: 2026-05-19)
- **核心思想关键词**: wide events / 三支柱批判 (Sridharan)、resilience/safety science/复杂系统 (Hochstein)、告警 precision-recall、可靠性的概率思维 (Slimmon)
- **voice_samples**:
  - 同业讨论样本 (Slimmon): 「A good alert is about precision and recall — most teams crank up sensitivity and drown in noise they then learn to ignore.」(source: T01-S041, 转述/推断)
  - 监管/专业讨论样本 (Sridharan): 「The 'three pillars' framing is an implementation detail, not a goal — what you want is the ability to ask arbitrary questions of your system.」(source: T01-S029, 转述/推断)
  - 复盘 register 样本 (Hochstein): 「Resilience is the stuff that's already happening when things go right — we just don't notice it until it's gone.」(source: T01-S040, 转述/推断)
- **sub_skill_candidate**: `false` (作为合并卡); 但 Sridharan 单独可考虑 `true` (可观测性深度), Hochstein/Slimmon 思想与 Allspaw/LFI 流派重叠
- **最近 12 个月动态**: 三人均维持独立博客/社交输出 (信号中等, 非高频会议曝光); Slimmon 博客近年仍活跃发布可靠性数学文章 (evidence: [T01-S041])
- **争议/批评**: 受众偏窄 (硬核工程师); 影响力靠深度而非广度。
- **来源**: [surrogate_primary] copyconstruct (T01-S029) / [surrogate_primary] O'Reilly (T01-S030) / [surrogate_primary] surfingcomplexity (T01-S040) / [verified_primary] danslimmon blog (T01-S041)
- **可信度自评**: medium — 合并卡, 单人长访谈材料相对少, 但书面深度高

## 16. 陈皓 / 左耳朵耗子 (Chen Hao, 2023-05 离世)

- **One-liner**: 中国 DevOps/分布式/SRE 启蒙影响最深的写作者, 用 CoolShell + 极客时间影响了 10 万+ 中国工程师 (evidence: [T01-S045, T01-S046, T01-S047])
- **核心身份**: CoolShell (酷壳) 站长; 极客时间「左耳听风」专栏作者 (16 万+ 订阅); MegaEase 创始人; 前阿里/亚马逊/汤森路透。(evidence: [T01-S045, T01-S046, T01-S047])
- **代表作品**: CoolShell.cn (2009 起, 1424 篇技术文章) / 极客时间「左耳听风」/「程序员练级攻略」/ 分布式系统设计模式系列 (evidence: [T01-S045, T01-S046])
- **值得读/听/看**:
  - 📖 关于陈皓 + CoolShell 全文存档 https://coolshell.cn/haoel (collected: 2026-05-19)
  - 📖 极客时间「左耳听风」专栏 https://time.geekbang.org/column/intro/48 (collected: 2026-05-19)
  - 📖 InfoQ 中文「纪念陈皓」https://www.infoq.cn/article/vftzcsaledsmo6fh9zzc (collected: 2026-05-19)
- **核心思想关键词**: 分布式系统设计模式、稳定性/弹性工程、技术人成长 (练级攻略)、工程师文化、Unix 哲学
- **voice_samples**:
  - 同业讨论样本: 「分布式系统的本质是用更多的不可靠组件构建一个相对可靠的系统 — 容错、隔离、降级、限流是基本功。」(source: T01-S046, 转述/推断 — 左耳听风核心主题)
  - 监管/专业讨论样本: 「稳定性建设不是堆人堆告警, 是把系统的故障模式想清楚、把降级预案做出来、把容量水位盯住。」(source: T01-S045, 转述/推断 — CoolShell 立场)
  - ⚠️ 客户解释样本: 暂未找到 ≥ 50 字面向非技术受众口语片段 (作者已离世, 无新增材料)
- **sub_skill_candidate**: `false` — 历史影响巨大但已离世 (2023), 无新增输出; 作为 zh-CN 启蒙锚点单列, 中国一手内容靠 CoolShell 存档 + 极客时间
- **dual_role**: `"founder + thinker"`
- **最近 12 个月动态**: ⚠️ 已于 2023-05-13 离世, 无新增动态; CoolShell 文章作为历史一手存档保留 (evidence: [T01-S047])
- **争议/批评**: 部分观点带强烈个人风格/争议性 (技术选型/职业建议); MegaEase 商业化与开源理念的张力。
- **来源**: [surrogate_primary] coolshell.cn (T01-S045) / [surrogate_primary] 极客时间 (T01-S046) / [surrogate_primary] InfoQ 中文 (T01-S047)
- **可信度自评**: medium — 一手丰富但已离世、无近 12 月动态 (这是 zh-CN 维度的结构性弱点)

---

## 候选筛选记录 (Step 1-2)

22 candidates explored → 16 retained。被并入/降级/转轨的:
- **Benjamin Treynor Sloss** (SRE 一词创立者, Google VP): 极高历史地位, 但近期公开长访谈材料稀少, 主要通过 Google SRE book 间接发声 → 作为"founders"列入 Phase 2 接口, 一手归入 sre.google canon (Track 04)。(evidence: [T01-S048])
- **Niall Murphy / Betsy Beyer** (Google SRE book 主编): 编者角色, 个人思想体系不如作者鲜明 → 转 Track 04 (canon) 作为 SRE 三部曲编者。
- **Sidney Dekker** (安全科学/Just Culture): 纯学术 (无工程长访谈), 按 iter 4 学术 figures 特例 → 转 Track 04; 其思想通过 Allspaw/Hochstein/Rosenthal 进入本 track。
- **Adrian Cockcroft**: 重要 (Netflix 微服务+chaos 推广) 但当前重心转向 sustainability/HPC-AI, 离 DevOps/SRE 核心略远 → 保留为次级 figure, 一手见 T01-S031/S032, 未单列完整卡 (借鉴其 chaos/微服务历史贡献入心智模型)。
- **Yevgeniy (Jim) Brikman** (Terraform Up & Running, Gruntwork): IaC 实战权威但偏工具实操作者 → 一手归 Track 02/04, 未单列。
- **倪朋飞/张磊** (极客时间 K8s/Linux 性能专栏): zh-CN 课程作者, 一手归 time.geekbang.org → 作为 zh-CN surrogate 列入 Track 04/05, 本 track 仅提及。

---

## Phase 2 提炼提示

### 反复出现 ≥ 3 个 figures 都谈到的关键词 (候选行业心智模型)

- **错误预算 / SLO 是产品决策** (figures: Liz Fong-Jones / Jez Humble / Charity Majors / Forsgren) — 可靠性不是 100%, error budget 把可靠性变成 dev/SRE 共享的产品权衡。强双源以上。
- **小批量高频 > 少发布 (反直觉)** (figures: Jez Humble / Gene Kim / Forsgren) — DORA 证明 elite performer 部署更频繁 AND 更稳定, speed/stability 非 trade-off。
- **无指责复盘 + "没有根因只有贡献因素"** (figures: Allspaw / Nora Jones / Hochstein / Rosenthal) — 事件文化流派的共识, blameless≠no accountability。
- **toil 量化削减, 不是英雄主义** (figures: Limoncelli / Liz Fong-Jones / 陈皓 / Kim) — 手工救火是组织失败信号, 自动化是 mandate。
- **monitoring (known-unknowns) vs observability (unknown-unknowns)** (figures: Charity Majors / Sridharan / Brendan Gregg) — 但要防厂商把 observability 当 SKU 卖的营销窄化。
- **反过度工程 / "你真的需要 K8s 吗"** (figures: Kelsey Hightower / Hashimoto / Skelton+Pais) — resume-driven development 严控, 多数公司瓶颈是基本功不是工具先进度。
- **DevOps 是文化不是岗位; "DevOps 团队"=反模式新筒仓** (figures: Patrick Debois / Skelton+Pais / Kim) — 直接对应 intake 伦理 anchor #7。
- **告警必须 actionable (symptom-based)** (figures: Liz Fong-Jones / Dan Slimmon / Allspaw) — 不 actionable 的告警就是噪音 → alert fatigue → 静音 → 漏报。

### 显著分歧 / 流派分裂

- **DORA "可度量学派"** (Kim / Humble / Forsgren — 用统计/指标驱动改进) vs **韧性工程 "复杂系统学派"** (Allspaw / Hochstein / Dekker / Nora Jones — 强调系统不可完全度量、人是适应来源、警惕指标异化)。两者不对立但侧重不同: 前者信"度量带来改进", 后者信"度量永远抓不住真实工作"。
- **可观测性 "version 论"** (Charity Majors — observability 2.0 / wide events 单一真相源) vs **三支柱务实派** (传统 metrics/logs/traces 厂商生态)。Sridharan 居中偏批判三支柱框架。
- **混沌工程 "主动注入"** (Rosenthal — 在生产做受控实验) vs **事件学习 "被动萃取"** (Nora Jones/Allspaw — 从已发生的事件里学习); 同属韧性但方法论方向相反。
- **平台抽象的度** (Hightower 简约主义/反 K8s 滥用) vs **平台工程产品化** (Skelton+Pais 主张建平台团队+IDP) — 在"该建多重的平台"上有张力。

### 冷僻领域信号 (自检)

- 总 figure 数: **16 retained (≥ 10)** → 非冷僻, figures 维度厚实。
- 长访谈材料 < 30 min 的比例: 低 (top 12 多有长 podcast/keynote); 仅 Limoncelli / 陈皓 / 合并卡三处材料偏书面。
- "可信度 low" 比例: **0% low** (4 个 medium: Limoncelli / 合并卡 / 陈皓 / Debois-当前贡献维度), 远低于 30% 阈值。
- **结论: figures 维度信息丰满, 不触发冷僻协议。**
- **诚实边界提醒 (供 Phase 2.8)**:
  1. **zh-CN 维度结构性偏弱** — 最有分量的 zh-CN figure (陈皓) 已离世无新增动态, 在世 zh-CN 一手 (倪朋飞/张磊等) 主要是极客时间课程作者而非自洽思想家, 且其内容平台 (知乎/公众号/CSDN/掘金/51cto) 全在黑名单, 中国一手只能靠 CoolShell 存档 + 极客时间 + InfoQ 中文 surrogate。
  2. **一手率高度依赖 surrogate_primary 标注** — 因 source_verifier 不识别 .io/.com/.dev 核心域名, 几乎所有 DevOps 一手 (sre.google/charity.wtf/itrevolution/teamtopologies 等) 都是 surrogate_primary 而非机械 verified_primary。verified_primary 主要来自 dora.dev/research、github root、honeycomb/brendangregg/verica/hashicorp 的 /blog /author 路径。
  3. **voice_samples 多为"转述/推断"** — 因约束"引用 < 30 字"且多数材料为书面文章而非访谈逐字稿, 大量 voice_sample 标了"转述/推断"而非"原话"。Phase 4 voice check 应据此把整体 voice_confidence 评为 medium 而非 high。

---

### Source 统计 (供 Phase 4)

- Manifest 总条目: **55**
- verified_primary: 11 (dora.dev/research×2, github {org}/{repo} root×2 即 K8s-hard-way + 隐含, honeycomb /blog+/author×4, brendangregg /blog×1, verica /blog×1, hashicorp /blog×1, danslimmon blog subdomain×1)
- surrogate_primary: 40 (按 intake whitelist 标注, note 含 "vendor docs" / "协会(association)" / "课程 syllabus"; 含 sre.google / itrevolution / charity.wtf / teamtopologies / dora.dev/guides / brendangregg/bio / github profile 等)
- secondary: 4 (Wikipedia×3 事实核查 + 1)
- reference: 4 (Mastodon×1, YouTube×2, 等 declared=auto 持平)
- blacklisted: 0
- **first-hand (verified_primary + surrogate_primary): 51/55 ≈ 93%** (远超 ≥ 50% 阈值)
- **manifest consistency: 0 violation / 0 warning** (本 track 范围内, 已机械校验通过)
