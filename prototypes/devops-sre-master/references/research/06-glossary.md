# Track 06 — DevOps & SRE Glossary / Terminology + Standards (locale=en primary)

> Phase 1 wave 1 第 3 路。术语 + 标准 + 认证 + outsider-tells + 厂商话术。一手率结构性高但 source_verifier 不识 .io/.com/.dev 核心域名 → 大量 surrogate_primary（note 含 literal "vendor docs" / "协会"）。

## Source Manifest

| source_id | url | bucket | last_checked | author/host | one-line note |
|-----------|-----|--------|--------------|-------------|---------------|
| T06-S001 | https://sre.google/sre-book/service-level-objectives/ | surrogate_primary | 2026-05-19 | Google SRE | vendor docs (Google SRE 一手) — SLI/SLO/SLA 定义章 |
| T06-S002 | https://sre.google/sre-book/embracing-risk/ | surrogate_primary | 2026-05-19 | Google SRE | vendor docs (Google SRE 一手) — error budget / 100% 非目标 |
| T06-S003 | https://sre.google/workbook/eliminating-toil/ | surrogate_primary | 2026-05-19 | Google SRE | vendor docs (Google SRE 一手) — toil 定义 + <50% 阈值 |
| T06-S004 | https://sre.google/sre-book/postmortem-culture/ | surrogate_primary | 2026-05-19 | Google SRE | vendor docs (Google SRE 一手) — blameless postmortem |
| T06-S005 | https://sre.google/sre-book/monitoring-distributed-systems/ | surrogate_primary | 2026-05-19 | Google SRE | vendor docs (Google SRE 一手) — four golden signals |
| T06-S006 | https://dora.dev/guides/dora-metrics-four-keys/ | surrogate_primary | 2026-05-19 | Google DORA | vendor docs (Google DORA 一手) — 四个关键指标定义 |
| T06-S007 | https://dora.dev/research/2024/dora-report/ | surrogate_primary | 2026-05-19 | Google DORA | vendor docs (Google DORA 一手) — 2024 报告 + rework rate |
| T06-S008 | https://12factor.net/ | surrogate_primary | 2026-05-19 | Adam Wiggins/Heroku | vendor docs (作者一手) — Twelve-Factor App 方法论 |
| T06-S009 | https://kubernetes.io/docs/reference/glossary/ | verified_primary | 2026-05-19 | Kubernetes/CNCF | CNCF 项目一手 — 官方术语表 (auto primary) |
| T06-S010 | https://opentelemetry.io/docs/concepts/semantic-conventions/ | surrogate_primary | 2026-05-19 | OpenTelemetry | vendor docs (CNCF 项目一手 — 协会) — semconv |
| T06-S011 | https://opentelemetry.io/blog/2023/http-conventions-declared-stable/ | surrogate_primary | 2026-05-19 | OpenTelemetry | vendor docs (CNCF 一手) — HTTP semconv v1.23 stable |
| T06-S012 | https://slsa.dev/spec/v1.0/levels | surrogate_primary | 2026-05-19 | OpenSSF/SLSA | vendor docs (协会 — OpenSSF 供应链 standards) — Build L0-L3 |
| T06-S013 | https://slsa.dev/spec/v1.1/faq | surrogate_primary | 2026-05-19 | OpenSSF/SLSA | vendor docs (协会 — OpenSSF) — v1.1 (2025-04) build track |
| T06-S014 | https://www.cncf.io/projects/ | surrogate_primary | 2026-05-19 | CNCF | vendor docs (协会 — 云原生 standards 基金会) — graduated/incubating |
| T06-S015 | https://github.com/cncf/toc/blob/main/process/graduation_criteria.md | verified_primary | 2026-05-19 | CNCF TOC | 协会 — graduation/incubation criteria (github repo) |
| T06-S016 | https://semver.org/ | surrogate_primary | 2026-05-19 | Tom Preston-Werner | vendor docs (作者一手 — standards) — SemVer 2.0.0 |
| T06-S017 | https://www.conventionalcommits.org/en/v1.0.0/ | surrogate_primary | 2026-05-19 | Conventional Commits | vendor docs (作者一手 — standards) — commit 规范 v1.0.0 |
| T06-S018 | https://opencontainers.org/about/overview/ | verified_primary | 2026-05-19 | OCI / Linux Foundation | 协会 — OCI image/runtime/distribution spec |
| T06-S019 | https://martinfowler.com/bliki/BlueGreenDeployment.html | surrogate_primary | 2026-05-19 | Martin Fowler | vendor docs (作者一手) — blue-green / CD 术语奠基 |
| T06-S020 | https://aws.amazon.com/architecture/well-architected/ | surrogate_primary | 2026-05-19 | AWS | vendor docs (AWS 一手) — Well-Architected 6 支柱 |
| T06-S021 | https://learn.microsoft.com/en-us/azure/well-architected/ | surrogate_primary | 2026-05-19 | Microsoft | vendor docs (Microsoft 一手) — Azure WAF 5 支柱 |
| T06-S022 | https://openmetrics.io/ | surrogate_primary | 2026-05-19 | OpenMetrics/CNCF | vendor docs (协会 — CNCF) — metrics exposition standard |
| T06-S023 | https://prometheus.io/docs/concepts/metric_types/ | surrogate_primary | 2026-05-19 | Prometheus/CNCF | vendor docs (CNCF 项目一手) — 指标类型/percentile |
| T06-S024 | https://www.openpolicyagent.org/docs/latest/ | surrogate_primary | 2026-05-19 | OPA/CNCF | vendor docs (CNCF 项目一手) — policy-as-code/Rego |
| T06-S025 | https://www.cisecurity.org/cis-benchmarks | surrogate_primary | 2026-05-19 | CIS | vendor docs (协会 — standards) — CIS Benchmarks 安全基线 |
| T06-S026 | https://www.iso.org/standard/27001 | verified_primary | 2026-05-19 | ISO | ISO/IEC 27001:2022 信息安全管理 standards |
| T06-S027 | https://en.wikipedia.org/wiki/Idempotence | secondary | 2026-05-19 | — | 术语 cross-check (idempotency) |
| T06-S028 | https://en.wikipedia.org/wiki/Circuit_breaker_design_pattern | secondary | 2026-05-19 | — | 术语 cross-check (circuit breaker) |
| T06-S029 | https://en.wikipedia.org/wiki/ITIL | secondary | 2026-05-19 | — | ITIL 边界 cross-check (legacy 范式) |
| T06-S030 | https://www.honeycomb.io/blog/observability-a-manifesto | surrogate_primary | 2026-05-19 | Charity Majors/Honeycomb | vendor docs (作者一手) — observability vs monitoring |
| T06-S031 | https://teamtopologies.com/key-concepts | surrogate_primary | 2026-05-19 | Skelton/Pais | vendor docs (作者一手) — cognitive load / platform team / golden path |
| T06-S032 | https://response.pagerduty.com/ | surrogate_primary | 2026-05-19 | PagerDuty | vendor docs (厂商一手) — incident commander / SEV / IC 角色 |
| T06-S033 | https://www.brendangregg.com/usemethod.html | surrogate_primary | 2026-05-19 | Brendan Gregg | vendor docs (作者一手) — USE method 发明者原文 |
| T06-S034 | https://www.cncf.io/blog/2022/05/03/the-difference-between-blue-green-and-canary-deployments/ | surrogate_primary | 2026-05-19 | CNCF | vendor docs (协会) — canary/blue-green 对比 |
| T06-S035 | https://principlesofchaos.org/ | surrogate_primary | 2026-05-19 | Rosenthal/Jones | vendor docs (作者一手) — chaos eng / steady state / blast radius |
| T06-S036 | https://www.terraform.io/docs/language/state/index.html | surrogate_primary | 2026-05-19 | HashiCorp | vendor docs (厂商一手) — state / drift / reconciliation |
| T06-S037 | https://docs.aws.amazon.com/whitepapers/latest/availability-and-beyond-improving-resilience/availability-and-beyond-improving-resilience.html | surrogate_primary | 2026-05-19 | AWS | vendor docs (AWS 一手) — availability nines |
| T06-S038 | https://martinfowler.com/articles/feature-toggles.html | surrogate_primary | 2026-05-19 | P. Hodgson/Fowler | vendor docs (作者一手) — feature flag/toggle |

> 一手率说明：38 个 source 中 33 个 surrogate_primary/verified_primary（核心 .io/.dev/.com 一手厂商/协会文档），2 个 secondary（Wikipedia term cross-check），ITIL Wikipedia 仅作边界。一手占比 ≈ 87%。

---

## Tier 1 术语表（核心必懂）

> Type/Tier/insider-def/outsider-friendly/etymology/outsider-tell/关联/decay。表中分隔符用 `/` 或 `;`，不用 escaped pipe。

### 1. SLI — Service Level Indicator
- **Type**: term + acronym; **Tier**: tier-1
- **Insider def**: 对服务行为的一个**量化测量**（如 good requests / total requests），是 SLO 的数据基础 (evidence: [T06-S001])
- **Outsider-friendly**: 衡量服务好不好的一个具体数字
- **Etymology**: Google SRE book 形式化 (2016)
- **outsider-tell** (`usage_tell`): 外行把 SLI 当成"监控指标"随便堆；内行强调 SLI 必须是 **user-facing 的、能直接反映用户体验** 的比率（不是 CPU 利用率这种 cause-level 指标）(evidence: [T06-S001])
- **关联**: SLO / SLA / four golden signals; **decay**: low

### 2. SLO — Service Level Objective
- **Type**: term + acronym; **Tier**: tier-1
- **Insider def**: 对 SLI 设定的**目标阈值**（如 99.9% 请求 < 300ms over 28d），内部工程目标，是错误预算的来源 (evidence: [T06-S001])
- **Outsider-friendly**: 团队给自己定的可靠性及格线
- **outsider-tell** (`semantic_tell`): 外行把 SLO 等同于 SLA（合同），或一上来定 "99.99%"。内行：SLO 是**内部**目标且要比对外 SLA 更严；目标不是越高越好，要留出错误预算 (evidence: [T06-S001, T06-S002])
- **关联**: SLI / SLA / error budget; **decay**: low

### 3. SLA — Service Level Agreement
- **Type**: term + acronym; **Tier**: tier-1
- **Insider def**: 对**外部客户**的合同承诺，违约有商业/赔偿后果；通常松于内部 SLO (evidence: [T06-S001])
- **Outsider-friendly**: 写进合同、违约要赔钱的可靠性承诺
- **outsider-tell** (`semantic_tell`): 外行 SLA/SLO 混用。内行：SLA 是合同（有罚则），SLO 是内部目标（无罚则但触发错误预算政策）；"我们 SLA 99.9%" 但没说 SLI 怎么算 = 外行 (evidence: [T06-S001])
- **关联**: SLO / error budget; **decay**: low

### 4. Error budget — 错误预算
- **Type**: term; **Tier**: tier-1
- **Insider def**: `1 - SLO`，即允许的不可靠额度；是平衡可靠性投入与功能速度的**产品决策货币**，烧光则冻结发布 (evidence: [T06-S002])
- **Outsider-friendly**: 允许出错的配额，没用完就可以继续快速上线
- **etymology**: Google SRE 学科核心概念
- **outsider-tell** (`usage_tell`): 外行视错误预算为"技术债"或失败指标。内行：错误预算**是用来花的**——没烧完说明发布太保守；100% 可用不是目标 (evidence: [T06-S002])
- **关联**: SLO / error budget policy / 可靠性非100%; **decay**: low

### 5. Toil — 苦工
- **Type**: term; **Tier**: tier-1
- **Insider def**: 手工的、重复的、可自动化的、无长期价值的、随服务规模线性增长的运维劳动；SRE 建议 < 50% 时间 (evidence: [T06-S003])
- **Outsider-friendly**: 重复又能被脚本替代的杂活
- **outsider-tell** (`semantic_tell`): 外行把 toil 当"杂事/加班"。内行有严格定义（手工+重复+可自动化+无价值+随规模线性增长），且把削减 toil 当作 mandate 不是 "有空再做"；把救火加班当美德 = 外行 (evidence: [T06-S003])
- **关联**: 自动化 / SRE 50% 工程时间; **decay**: low

### 6. MTTR / MTTD / MTTA / MTBF — 平均恢复/检测/确认/无故障时间
- **Type**: acronym; **Tier**: tier-1
- **Insider def**: MTTR=Mean Time To Recover/Repair（恢复）, MTTD=To Detect（检测）, MTTA=To Acknowledge（确认/响应）, MTBF=Between Failures（无故障间隔）(evidence: [T06-S006])
- **Outsider-friendly**: 一组衡量"出事后多快恢复 / 多久才出一次事"的时间指标
- **outsider-tell** (`pronunciation_tell` + `usage_tell`): 字母逐个念 "M-T-T-R"。外行追 MTBF（少出事）；内行重 MTTR（快恢复）——分布式系统注定会坏，重点是恢复速度而非杜绝故障；MTTR 是 DORA 第四指标 (evidence: [T06-S006])
- **关联**: DORA / 韧性 / incident; **decay**: low

### 7. SEV / Severity — 严重等级
- **Type**: term; **Tier**: tier-1
- **Insider def**: 事件严重度分级（如 SEV1 全站宕机 / SEV2 重大降级 / SEV3 局部影响），决定响应规格与上报链 (evidence: [T06-S032])
- **Outsider-friendly**: 给故障定的紧急程度等级
- **outsider-tell** (`pronunciation_tell`): 念 "sev-one" 不是 "S-E-V-1"；外行不知道 declaring a SEV 意味着拉起正式 incident 流程。内行："declaring a SEV2" 是一个动作 (evidence: [T06-S032])
- **关联**: incident commander / SLO; **decay**: low

### 8. IC — Incident Commander（事件指挥官）
- **Type**: term + acronym; **Tier**: tier-1
- **Insider def**: 事件期间的**单一决策协调者**，借自 ICS（应急指挥系统）；负责协调不亲自修，分派 ops/comms 等角色 (evidence: [T06-S032])
- **Outsider-friendly**: 故障期间负总指挥、做决定的那个人
- **outsider-tell** (`usage_tell`): 外行以为 IC = 最资深工程师亲自下场修。内行：IC 协调而非动手；"who's IC?" 是事件开场第一句 (evidence: [T06-S032])
- **关联**: SEV / on-call / postmortem; **decay**: low

### 9. RCA — Root Cause Analysis（根因分析）
- **Type**: acronym; **Tier**: tier-1
- **Insider def**: 找出事件成因；现代 SRE/韧性社区更倾向说 **contributing factors（贡献因素）** 而非单一 root cause（复杂系统无单一根因）(evidence: [T06-S004])
- **Outsider-friendly**: 查清楚为什么出事
- **outsider-tell** (`semantic_tell`): 外行执着于"找到那个根本原因"并归咎一个人/一行代码。内行：复杂系统失败是多因素叠加，说 "the root cause was human error" 是危险信号 (evidence: [T06-S004])
- **关联**: blameless postmortem / 安全科学; **decay**: low

### 10. Blameless postmortem — 无指责复盘
- **Type**: term; **Tier**: tier-1
- **Insider def**: 复盘聚焦系统/流程为何允许错误发生，而非惩罚个人；前提是"工程师做了当时认为合理的事" (evidence: [T06-S004])
- **Outsider-friendly**: 出事后开总结会，不批斗人，只改系统
- **outsider-tell** (`semantic_tell`): 外行把 blameless 误读为"出事没人负责"。内行：blameless ≠ no accountability——是**系统/流程**问责而非个人惩罚；"the system let them do it" 是核心句 (evidence: [T06-S004])
- **关联**: RCA / Just Culture / accountability; **decay**: low

### 11. Postmortem — 事后复盘 / 复盘文档
- **Type**: term; **Tier**: tier-1
- **Insider def**: 事件后产出的书面分析（时间线 + 影响 + 贡献因素 + 带 owner 的行动项），用于组织学习 (evidence: [T06-S004])
- **Outsider-friendly**: 故障的复盘报告
- **outsider-tell** (`usage_tell`): 外行把它当甩锅文档或合规走过场。内行：好的 postmortem 有 actionable items with owners + 不重复同类故障；"action items with owners" (evidence: [T06-S004])
- **关联**: blameless / incident; **decay**: low

### 12. GitOps
- **Type**: term; **Tier**: tier-1
- **Insider def**: 以 git 为单一真相源、声明式描述期望状态、控制器（Argo CD/Flux）持续 reconcile 实际状态向期望收敛 (evidence: [T06-S009])
- **Outsider-friendly**: 把基础设施配置全放 git，自动同步到环境
- **outsider-tell** (`semantic_tell`): 外行把"用 git 存 YAML + CI 跑 kubectl apply"叫 GitOps（其实是 CIOps/push 模式）。内行：GitOps 强调 **pull-based reconcile + drift 自动纠正**；"is this GitOps or ClickOps" (evidence: [T06-S009])
- **关联**: reconciliation loop / declarative / drift; **decay**: medium

### 13. IaC — Infrastructure as Code（基础设施即代码）
- **Type**: term + acronym; **Tier**: tier-1
- **Insider def**: 用代码（声明式 HCL / 命令式）定义并版本化基础设施，可重复、可审查、可回滚 (evidence: [T06-S036])
- **Outsider-friendly**: 用代码而不是点鼠标来创建服务器/网络
- **outsider-tell** (`usage_tell`): 外行写了 Terraform 却仍手工改控制台（造成 drift），或把 state 文件提交 git。内行：state 含明文密钥是危险面，必须远程加密加锁后端 (evidence: [T06-S036])
- **关联**: Terraform / drift / state / declarative; **decay**: low

### 14. CI/CD — 持续集成 / 持续交付·部署
- **Type**: term + acronym; **Tier**: tier-1
- **Insider def**: CI=频繁合并 + 自动化构建测试；CD=持续交付（随时可发，需手动批准）或持续部署（自动到生产）(evidence: [T06-S019])
- **Outsider-friendly**: 自动构建、测试、上线代码的流水线
- **outsider-tell** (`semantic_tell`): 外行把 CD 一律当"持续部署"，且以为 CI/CD = "有个 Jenkins"。内行区分 continuous delivery vs deployment；CI 的核心是 **trunk-based + 小批量频繁合并**，不是工具 (evidence: [T06-S019])
- **关联**: trunk-based / DORA 部署频率; **decay**: medium

### 15. Canary deployment — 金丝雀发布
- **Type**: term; **Tier**: tier-1
- **Insider def**: 先把新版本放给一小部分流量/用户，观察指标无异常再逐步放量 (evidence: [T06-S034])
- **Outsider-friendly**: 先让一小撮用户试新版本，没问题再全量
- **etymology**: 矿工带金丝雀下井探毒气
- **outsider-tell** (`usage_tell`): 外行 canary 后不看指标就全量，或把 canary 当 "灰度发布的代名词"不设自动回滚门槛。内行：canary 必须绑 SLO/指标 + 自动 rollback (evidence: [T06-S034])
- **关联**: blue-green / progressive delivery / feature flag; **decay**: low

### 16. Blue-green deployment — 蓝绿部署
- **Type**: term; **Tier**: tier-1
- **Insider def**: 维护两套完全相同的环境（蓝/绿），新版本部到空闲那套，验证后切流量；回滚=切回 (evidence: [T06-S019])
- **Outsider-friendly**: 准备两套环境，一套上线一套备用，出问题秒切回
- **outsider-tell** (`usage_tell`): 外行把 blue-green 和 canary 混用。内行：blue-green 是**整体瞬时切换**（无渐进），canary 是**逐步放量**；blue-green 成本翻倍但回滚最快 (evidence: [T06-S019, T06-S034])
- **关联**: canary / rollback; **decay**: low

### 17. Feature flag / toggle — 特性开关
- **Type**: term; **Tier**: tier-1
- **Insider def**: 在代码中用配置开关控制功能是否启用，使**部署与发布解耦**（dark launch / 灰度 / kill switch）(evidence: [T06-S038])
- **Outsider-friendly**: 一个开关，不重新部署就能开关功能
- **outsider-tell** (`usage_tell`): 外行长期堆积 flag 不清理（flag debt），或复用废弃 flag（Knight Capital 2012 即复用旧 flag 触发灾难）。内行：flag 要有生命周期 + 及时清理 (evidence: [T06-S038])
- **关联**: canary / dark launch / kill switch; **decay**: low

### 18. RED method — RED 方法
- **Type**: term + acronym; **Tier**: tier-1
- **Insider def**: 面向**请求驱动服务**的监控三指标：Rate（请求率）/ Errors（错误率）/ Duration（延迟）(evidence: [T06-S005])
- **Outsider-friendly**: 监控一个服务看三件事：多少请求、多少出错、多慢
- **outsider-tell** (`usage_tell`): 外行只看一个平均延迟。内行：RED 针对 service-level（请求维度），与 USE（资源维度）互补；Duration 看分布不看均值 (evidence: [T06-S005, T06-S033])
- **关联**: USE method / four golden signals; **decay**: low

### 19. USE method — USE 方法
- **Type**: term + acronym; **Tier**: tier-1
- **Insider def**: Brendan Gregg 提出，面向**资源**的排查法：Utilization（利用率）/ Saturation（饱和度）/ Errors（错误）(evidence: [T06-S033])
- **Outsider-friendly**: 排查每个硬件/资源看：用了多少、堵了没、有没有报错
- **outsider-tell** (`usage_tell`): 外行只看 Utilization（CPU%）忽略 Saturation（队列/等待）。内行：饱和度（run queue 等）才是瓶颈早期信号 (evidence: [T06-S033])
- **关联**: RED method; **decay**: low

### 20. Four golden signals — 四个黄金信号
- **Type**: term; **Tier**: tier-1
- **Insider def**: Google SRE：Latency（延迟）/ Traffic（流量）/ Errors（错误）/ Saturation（饱和度）(evidence: [T06-S005])
- **Outsider-friendly**: Google 推荐每个服务必看的四个核心监控信号
- **outsider-tell** (`usage_tell`): 外行报一堆 dashboard 没有重点。内行：先看这四个；告警应基于 symptom（这四个）不是 cause (evidence: [T06-S005])
- **关联**: RED / USE / symptom-based alerting; **decay**: low

### 21. Cardinality — 基数
- **Type**: term; **Tier**: tier-1
- **Insider def**: 指标/标签的唯一值组合数；高基数（如按 user_id 打标签）会拖垮 metrics 系统，但是可观测性下钻的关键 (evidence: [T06-S030])
- **Outsider-friendly**: 一个监控维度有多少种不同取值
- **outsider-tell** (`semantic_tell`): 外行随手给 Prometheus 指标加 high-cardinality 标签导致爆炸。内行：metrics 系统怕高基数；observability（宽事件）才适合任意高基数下钻 (evidence: [T06-S030])
- **关联**: observability / Prometheus / wide events; **decay**: medium

### 22. Observability vs Monitoring — 可观测性 vs 监控
- **Type**: term; **Tier**: tier-1
- **Insider def**: monitoring 处理 known-unknowns（预设 dashboard/alert）；observability 处理 unknown-unknowns（高基数任意维度事后下钻）(evidence: [T06-S030])
- **Outsider-friendly**: 监控=盯着你预想到的问题；可观测性=出了没预想到的问题也能查
- **outsider-tell** (`semantic_tell`): 外行把 "observability" 当 "监控的新叫法" 或 "买三件套 SKU"。内行（Charity Majors）：核心是能否回答没预设过的问题；但也不否定 metrics 监控价值 (evidence: [T06-S030])
- **关联**: cardinality / three pillars; **decay**: medium

### 23. p50 / p95 / p99 — 百分位延迟
- **Type**: term; **Tier**: tier-1
- **Insider def**: 延迟分布的百分位数（p99 = 99% 请求快于此值）；尾延迟反映最差用户体验 (evidence: [T06-S023])
- **Outsider-friendly**: 不看平均，看"最慢的那部分用户有多慢"
- **outsider-tell** (`pronunciation_tell` + `usage_tell`): 念 "p-ninety-nine"；外行只报平均延迟。内行：均值掩盖尾延迟，p99/p99.9 才暴露真实体验；百分位**不能相加平均** (evidence: [T06-S023])
- **关联**: SLI / latency / 黄金信号; **decay**: low

### 24. Nines / Availability — 几个 9 / 可用性
- **Type**: term; **Tier**: tier-1
- **Insider def**: 可用性用 9 的个数表达（99.9% = three nines ≈ 8.76h/年停机；99.99% = four nines ≈ 52.6min/年）(evidence: [T06-S037])
- **Outsider-friendly**: 用"几个9"表示一年能宕机多久
- **outsider-tell** (`semantic_tell`): 外行说"我们要 100% 可用"或"五个9"却不知道对应停机时间和成本。内行：每多一个 9 成本指数上升；100% 是错误目标 (evidence: [T06-S037, T06-S002])
- **关联**: SLO / error budget; **decay**: low

### 25. Cattle not pets — 牲畜而非宠物
- **Type**: term; **Tier**: tier-1
- **Insider def**: 服务器应像牲畜——可编号、可替换、坏了重建不抢救；而非宠物（独一无二、手工照料）(evidence: [T06-S008])
- **Outsider-friendly**: 服务器坏了就重建一个，别费劲修
- **outsider-tell** (`usage_tell`): 外行有"那台关键服务器"不敢重启、SSH 进去手工调。内行：基础设施应不可变可重建；"don't SSH in to fix it" (evidence: [T06-S008])
- **关联**: immutable infra / IaC; **decay**: low

### 26. Immutable infrastructure — 不可变基础设施
- **Type**: term; **Tier**: tier-1
- **Insider def**: 部署后不再就地修改；变更=构建新镜像/实例替换旧的 (evidence: [T06-S008])
- **Outsider-friendly**: 不在跑着的机器上改，要变就换新的
- **outsider-tell** (`usage_tell`): 外行登上生产机 apt install / 改配置（造成 config drift + 雪花服务器）。内行：改了就重建 (evidence: [T06-S008, T06-S036])
- **关联**: cattle not pets / drift; **decay**: low

### 27. Declarative vs Imperative — 声明式 vs 命令式
- **Type**: term; **Tier**: tier-1
- **Insider def**: 声明式描述"期望的最终状态"（K8s/Terraform），系统负责达成；命令式描述"逐步怎么做" (evidence: [T06-S009])
- **Outsider-friendly**: 说"我要什么样" vs "一步步教怎么做"
- **outsider-tell** (`semantic_tell`): 外行写一堆命令式脚本拼凑环境。内行："declarative not imperative" 是云原生口头禅 (evidence: [T06-S009])
- **关联**: GitOps / reconciliation; **decay**: low

### 28. Idempotency — 幂等性
- **Type**: term; **Tier**: tier-1
- **Insider def**: 同一操作执行多次与执行一次效果相同；IaC/配置管理/重试机制的根基 (evidence: [T06-S027])
- **Outsider-friendly**: 同一个操作做几遍结果都一样
- **outsider-tell** (`pronunciation_tell` + `usage_tell`): 念错 "eye-dem-PO-tent"（正确 "eye-DEM-po-tent"）；外行写的脚本重跑会重复创建资源。内行：Ansible/Terraform/重试都依赖幂等 (evidence: [T06-S027])
- **关联**: IaC / 重试退避 / reconciliation; **decay**: low

### 29. Drift — 漂移
- **Type**: term; **Tier**: tier-1
- **Insider def**: 实际基础设施状态偏离 IaC/git 中声明的期望状态（通常因手工改动）(evidence: [T06-S036])
- **Outsider-friendly**: 实际环境跟代码里写的不一致了
- **outsider-tell** (`usage_tell`): 外行手工改了控制台又跑 terraform apply 把改动冲掉/或不知 drift 存在。内行：drift detection + GitOps 自动 reconcile (evidence: [T06-S036])
- **关联**: GitOps / reconciliation / IaC; **decay**: low

### 30. Reconciliation loop — 调谐循环
- **Type**: term; **Tier**: tier-1
- **Insider def**: 控制器持续比较期望状态与实际状态并采取行动收敛（K8s 控制器 / Argo CD 核心机制）(evidence: [T06-S009])
- **Outsider-friendly**: 系统不断检查"现状对不对"，不对就自动修正
- **outsider-tell** (`usage_tell`): 外行以为 K8s apply 是一次性命令。内行：是持续 reconcile，删了 Pod 会自动重建 (evidence: [T06-S009])
- **关联**: GitOps / control plane / declarative; **decay**: low

### 31. Sidecar — 边车
- **Type**: term; **Tier**: tier-1
- **Insider def**: 与主容器同 Pod 部署、共享网络/存储、提供横切能力（代理/日志/mesh proxy）的辅助容器 (evidence: [T06-S009])
- **Outsider-friendly**: 跟主程序贴身部署、帮它干杂活的小容器
- **outsider-tell** (`usage_tell`): 外行不知 sidecar 与主容器共享生命周期/网络命名空间。内行：service mesh 的 data plane 就是注入的 sidecar proxy（Envoy）(evidence: [T06-S009])
- **关联**: service mesh / data plane / Pod; **decay**: medium

### 32. Control plane / Data plane — 控制面 / 数据面
- **Type**: term; **Tier**: tier-1
- **Insider def**: 控制面做决策/配置分发（K8s API server、mesh 控制器）；数据面执行实际流量处理（kubelet、Envoy proxy）(evidence: [T06-S009])
- **Outsider-friendly**: 一个负责"指挥决策"，一个负责"干活搬数据"
- **outsider-tell** (`semantic_tell`): 外行把两者混为一谈。内行：控制面挂了数据面通常仍能转发（设计目标）；service mesh 性能开销主要在 data plane (evidence: [T06-S009])
- **关联**: service mesh / sidecar; **decay**: low

### 33. HPA / VPA — 水平/垂直 Pod 自动伸缩
- **Type**: acronym; **Tier**: tier-1
- **Insider def**: HPA=Horizontal Pod Autoscaler（增减副本数）；VPA=Vertical（调单 Pod 的 request/limit）(evidence: [T06-S009])
- **Outsider-friendly**: HPA 多开几个副本，VPA 把单个副本调大
- **outsider-tell** (`usage_tell`): 外行同时给同一负载开 HPA+VPA（冲突）或不设 resource request 导致 HPA 失效。内行：两者一般不混用同一指标 (evidence: [T06-S009])
- **关联**: autoscaling / OOMKilled / KEDA; **decay**: medium

### 34. OOMKilled / CrashLoopBackOff — K8s Pod 状态
- **Type**: term; **Tier**: tier-1
- **Insider def**: OOMKilled=容器超内存 limit 被内核杀；CrashLoopBackOff=容器反复崩溃，kubelet 退避式重启 (evidence: [T06-S009])
- **Outsider-friendly**: 一个是内存爆了被杀，一个是反复崩溃在不停重启
- **outsider-tell** (`semantic_tell`): 外行看到 CrashLoopBackOff 以为是 K8s 的 bug。内行：这是症状，是应用启动失败/配置错/依赖未就绪；OOMKilled = 调 limit 或修内存泄漏 (evidence: [T06-S009])
- **关联**: HPA / resource limit / Pod; **decay**: low

### 35. Cordon / Drain — 隔离 / 排空节点
- **Type**: term; **Tier**: tier-1
- **Insider def**: cordon=标记节点不可调度（不再接新 Pod）；drain=cordon + 优雅驱逐现有 Pod，用于节点维护 (evidence: [T06-S009])
- **Outsider-friendly**: 给节点维护前先"封口 + 把上面的活儿挪走"
- **outsider-tell** (`usage_tell`): 外行直接重启/关节点不 drain（导致 Pod 硬中断）。内行：维护必先 cordon+drain + 检查 PodDisruptionBudget (evidence: [T06-S009])
- **关联**: taint/toleration / PDB; **decay**: low

### 36. Taint / Toleration — 污点 / 容忍
- **Type**: term; **Tier**: tier-1
- **Insider def**: taint 打在节点上排斥 Pod；toleration 打在 Pod 上允许它被调度到带相应 taint 的节点 (evidence: [T06-S009])
- **Outsider-friendly**: 节点贴"别来"标签，Pod 贴"我能去"通行证才进得去
- **outsider-tell** (`usage_tell`): 外行用 taint 当亲和性（affinity）。内行：taint/toleration 是**排斥**机制（专用节点池/GPU 节点），nodeAffinity 才是吸引 (evidence: [T06-S009])
- **关联**: cordon/drain / nodeAffinity; **decay**: low

### 37. Ingress — 入站流量 / 入口
- **Type**: term; **Tier**: tier-1
- **Insider def**: K8s 中管理外部 HTTP(S) 流量进集群的资源（路由/TLS 终止），由 ingress controller 实现 (evidence: [T06-S009])
- **Outsider-friendly**: 集群对外的总入口/网关
- **outsider-tell** (`usage_tell`): 外行把 Ingress 资源本身当成会工作的东西（没装 controller 它什么都不做）。内行：Ingress 正逐步被 Gateway API 取代 (evidence: [T06-S009])
- **关联**: control plane / Gateway API / mTLS; **decay**: medium

### 38. mTLS — 双向 TLS
- **Type**: acronym; **Tier**: tier-1
- **Insider def**: 通信双方互相验证证书的 TLS；service mesh 用它做服务间零信任加密与身份认证 (evidence: [T06-S009])
- **Outsider-friendly**: 通信双方都要亮证书互验，不只是客户端验服务端
- **outsider-tell** (`pronunciation_tell`): 念 "mutual T-L-S"；外行以为普通 HTTPS = mTLS。内行：普通 TLS 只验服务端，mTLS 双向 (evidence: [T06-S009])
- **关联**: service mesh / 零信任 / sidecar; **decay**: low

### 39. Blast radius — 爆炸半径
- **Type**: term; **Tier**: tier-1
- **Insider def**: 一次故障/变更/实验可能波及的影响范围；混沌工程与变更管理都要主动**限制**它 (evidence: [T06-S035])
- **Outsider-friendly**: 一旦出事，能炸到多大范围
- **outsider-tell** (`usage_tell`): 外行做变更/实验不评估影响面（"先在生产试试"）。内行：canary、cell 架构、混沌实验都为缩小爆炸半径 (evidence: [T06-S035])
- **关联**: chaos engineering / canary / cell; **decay**: low

### 40. Steady state — 稳态
- **Type**: term; **Tier**: tier-1
- **Insider def**: 混沌工程中对系统"正常运转"的可测量定义（如吞吐/错误率），实验前后比对它判断假设 (evidence: [T06-S035])
- **Outsider-friendly**: 系统"健康正常"长什么样的可量化标准
- **outsider-tell** (`usage_tell`): 外行做故障演练不先定义稳态（无法判断有没有出问题）。内行：先定 steady state hypothesis 再注入故障 (evidence: [T06-S035])
- **关联**: chaos engineering / blast radius / game day; **decay**: low

### 41. Circuit breaker — 熔断器
- **Type**: term; **Tier**: tier-1
- **Insider def**: 当下游错误率超阈值时快速失败（断开），避免级联故障与资源耗尽，定时半开试探恢复 (evidence: [T06-S028])
- **Outsider-friendly**: 下游坏了就先别打它，免得把自己也拖垮
- **outsider-tell** (`usage_tell`): 外行无限重试已挂的下游（加剧雪崩）。内行：circuit breaker + 退避 + jitter 防止 retry storm (evidence: [T06-S028])
- **关联**: backpressure / rate limiting / graceful degradation; **decay**: low

### 42. Backpressure — 背压
- **Type**: term; **Tier**: tier-1
- **Insider def**: 下游处理不过来时向上游施加"减速/拒绝"信号，防止队列无限堆积压垮系统 (evidence: [T06-S005])
- **Outsider-friendly**: 处理不过来就让上游慢点发，别硬扛到崩
- **outsider-tell** (`usage_tell`): 外行无界队列缓冲一切（最终 OOM）。内行：有界队列 + backpressure + load shedding (evidence: [T06-S005])
- **关联**: load shedding / rate limiting / circuit breaker; **decay**: low

### 43. Rate limiting — 限流
- **Type**: term; **Tier**: tier-1
- **Insider def**: 限制单位时间请求数（令牌桶/漏桶/滑窗），保护服务不被打爆，也用于公平性 (evidence: [T06-S005])
- **Outsider-friendly**: 给请求设速度上限，超了就拒
- **outsider-tell** (`usage_tell`): 外行限流后对超限请求静默丢弃不返回 429/Retry-After。内行：限流要可观测 + 优雅降级 (evidence: [T06-S005])
- **关联**: load shedding / backpressure; **decay**: low

### 44. Graceful degradation — 优雅降级
- **Type**: term; **Tier**: tier-1
- **Insider def**: 部分依赖故障时主动降级非核心功能、保住核心链路可用，而非整体崩溃 (evidence: [T06-S002])
- **Outsider-friendly**: 出问题时砍掉次要功能，保住主功能能用
- **outsider-tell** (`usage_tell`): 外行任一依赖挂了整个页面 500。内行：预设降级预案（fallback / 静态兜底 / 关闭推荐模块）(evidence: [T06-S002])
- **关联**: load shedding / circuit breaker / 降级预案; **decay**: low

### 45. DORA four keys — DORA 四个关键指标
- **Type**: term; **Tier**: tier-1
- **Insider def**: 部署频率（Deployment Frequency）、变更前置时间（Lead Time for Changes）、变更失败率（Change Failure Rate）、恢复时间（Time to Restore / MTTR）(evidence: [T06-S006])
- **Outsider-friendly**: 衡量软件交付又快又稳的四个指标
- **etymology**: DevOps Research and Assessment（现 Google Cloud），Accelerate (Forsgren/Humble/Kim 2018)
- **outsider-tell** (`usage_tell`): 外行把四指标当 KPI 考核个人（触发 Goodhart 定律）或以为快慢是 trade-off。内行：吞吐与稳定**正相关**，elite 团队又快又稳；2024 报告新增第五指标 rework rate (evidence: [T06-S006, T06-S007])
- **关联**: deployment frequency / Accelerate / value stream; **decay**: medium

### 46. Paved road / Golden path — 铺好的路 / 黄金路径
- **Type**: term; **Tier**: tier-1
- **Insider def**: 平台团队提供的、推荐的、自助式的"默认正确做法"路径，降低开发者认知负荷 (evidence: [T06-S031])
- **Outsider-friendly**: 平台给的"照着走就对了"的标准模板/工具链
- **outsider-tell** (`semantic_tell`): 外行把它理解为"强制规范/管控"。内行：golden path 是**好走到大家自愿走**而非强制；偏离要允许但需自担成本 (evidence: [T06-S031])
- **关联**: platform engineering / IDP / cognitive load; **decay**: medium

### 47. Cognitive load — 认知负荷
- **Type**: term; **Tier**: tier-1
- **Insider def**: 团队为完成工作需要持有的心智负担总量；Team Topologies 主张平台团队的目的是**降低** stream-aligned 团队的认知负荷 (evidence: [T06-S031])
- **Outsider-friendly**: 团队要操心的东西太多就转不动
- **outsider-tell** (`usage_tell`): 外行无限扩团队职责范围。内行：团队边界应按认知负荷上限切分；平台/golden path 为减负而生 (evidence: [T06-S031])
- **关联**: Team Topologies / platform engineering / paved road; **decay**: low

### 48. You build it, you run it — 谁开发谁运维
- **Type**: term; **Tier**: tier-1
- **Insider def**: 开发团队对自己服务的生产运行负责（含 on-call），打破开发-运维交接墙（Werner Vogels/Amazon）(evidence: [T06-S031])
- **Outsider-friendly**: 写代码的人也要负责它在生产上跑得好
- **outsider-tell** (`semantic_tell`): 外行据此说"那要运维/SRE 干嘛"。内行：YBYR ≠ 没有平台支持；平台团队提供自助能力让产品团队能运维 (evidence: [T06-S031])
- **关联**: DevOps 文化 / platform engineering; **decay**: low

### 49. Shift-left — 左移
- **Type**: term; **Tier**: tier-1
- **Insider def**: 把测试/安全/可靠性考量提前到开发早期（流水线左侧），越早发现越便宜（DevSecOps 核心）(evidence: [T06-S012])
- **Outsider-friendly**: 把测试和安全检查提前，别等上线才发现问题
- **outsider-tell** (`usage_tell`): 外行把 shift-left 当"把活全甩给开发"。内行：shift-left 要配自助工具 + 不增加认知负荷，否则只是转移 toil (evidence: [T06-S012, T06-S031])
- **关联**: DevSecOps / SAST/DAST / SBOM; **decay**: medium

### 50. SBOM — Software Bill of Materials（软件物料清单）
- **Type**: term + acronym; **Tier**: tier-1
- **Insider def**: 软件所有组件/依赖及其版本的清单（SPDX/CycloneDX 格式），用于漏洞追溯与供应链透明 (evidence: [T06-S012])
- **Outsider-friendly**: 软件的"成分表"，列出它用了哪些第三方库
- **outsider-tell** (`pronunciation_tell` + `usage_tell`): 念 "S-bomb"；外行生成 SBOM 就当合规完成。内行：SBOM 要持续更新 + 接漏洞库 + 配 provenance 才有意义 (evidence: [T06-S012])
- **关联**: SLSA / provenance / supply chain; **decay**: medium

### 51. SLSA — Supply-chain Levels for Software Artifacts
- **Type**: standard + acronym; **Tier**: tier-1
- **Insider def**: OpenSSF 的软件供应链完整性框架，Build track L0–L3 递进（L1 自动 provenance / L3 不可伪造、隔离构建）(evidence: [T06-S012, T06-S013])
- **Outsider-friendly**: 给软件构建过程定的安全等级阶梯
- **etymology**: OpenSSF；v1.0 (2023)，v1.1 (2025-04)，v1.2 草案；念 "salsa"
- **outsider-tell** (`pronunciation_tell` + `semantic_tell`): 念 "S-L-S-A" 而非 "salsa"；外行把 SLSA 当"工具"。内行：是分级框架，目前只有 Build track 稳定，Source/Dependencies track 仍草案 (evidence: [T06-S013])
- **关联**: SBOM / provenance / sigstore; **decay**: high（track 仍演进）

### 52. Provenance — 来源证明
- **Type**: term; **Tier**: tier-1
- **Insider def**: 可验证的元数据，记录工件**由谁、用什么、如何构建**（in-toto attestation），SLSA L1+ 的核心要求 (evidence: [T06-S012])
- **Outsider-friendly**: 软件的"出生证明"，证明它确实是按预期流程造出来的
- **outsider-tell** (`usage_tell`): 外行有了签名就以为有 provenance。内行：签名证明"是谁发的"，provenance 证明"怎么造的"，两者不同 (evidence: [T06-S012])
- **关联**: SLSA / SBOM / sigstore/cosign; **decay**: high

---

## Tier 2 术语（周边熟知，简表）

| 术语 | Type | Insider def | Outsider tell | decay |
|------|------|-------------|---------------|-------|
| Trunk-based development | term | 所有人频繁合并到主干、短命分支 | 外行长命 feature branch + 大合并 | low |
| Progressive delivery | term | canary/blue-green/flag 的统称，渐进暴露变更 | 外行当"灰度"一个词 | medium |
| Rolling update | term | 逐批替换旧实例的滚动更新 | 外行以为=blue-green | low |
| Error budget policy | term | 烧光预算后的跨团队行动协议（冻结发布等） | 外行只有数字没有政策 | low |
| Load shedding | term | 过载时主动丢弃低优先级请求保核心 | 外行硬扛到全崩 | low |
| Capacity planning | term | 按增长预测 + headroom 规划容量 | 外行等 OOM 才扩容 | low |
| Alert fatigue | term | 告警过多致麻木/漏真告警 | 外行"静音那个一直响的告警" | low |
| Runbook / Playbook | term | 处置故障的可执行步骤手册 | 外行无 runbook 全靠记忆 | low |
| Follow-the-sun | term | 跨时区轮班让 on-call 不熬夜 | 外行让一个区扛全天 | low |
| Burn rate | term | 错误预算消耗速度，multi-window 告警 | 外行只看绝对剩余 | medium |
| Wide events / structured logging | term | 高维度结构化事件（observability 基础） | 外行打非结构化文本日志 | medium |
| Three pillars | term | metrics/logs/traces 三支柱 | 外行以为=买三个产品 | medium |
| eBPF | acronym | 内核可编程，零侵入采集网络/性能数据 | 外行不知道无需改应用 | medium |
| Operator / CRD | term | 用 CRD 把运维知识编码进 K8s 控制器 | 外行手工运维有状态服务 | medium |
| Helm / Kustomize | tool | K8s 打包/模板（Helm chart）vs 覆盖式定制 | 外行 Helm/Kustomize 混用不清 | medium |
| CNI / CSI | acronym | 容器网络/存储接口标准 | 外行不知是可插拔标准 | low |
| KEDA | tool | 基于事件源的 K8s 自动伸缩 | 外行只知 HPA | medium |
| PodDisruptionBudget | term | 限制自愿中断时最少可用 Pod 数 | 外行 drain 把服务搞挂 | low |
| Distroless / multi-stage build | term | 最小化镜像、减攻击面 | 外行打 1GB 全功能镜像 | low |
| Policy-as-code (OPA/Rego) | standard | 用代码（Rego）声明并强制策略 | 外行靠人工 review 卡门 | medium |
| Sealed/External Secrets | term | 加密后可入 git / 从外部密钥管理拉取 | 外行把 secret 明文进 git | medium |
| RTO / RPO | acronym | 容灾目标：恢复时间/可接受数据丢失量 | 外行有备份不知 RTO/RPO | low |
| Expand-contract migration | term | schema 迁移分扩展-迁移-收缩三步保兼容 | 外行一次性改 schema 致停机 | low |
| Online DDL (gh-ost/pt-osc) | tool | 不锁表的在线 schema 变更 | 外行高峰期直接 ALTER 锁库 | medium |
| PITR | acronym | 时间点恢复（point-in-time recovery） | 外行只有全量备份 | low |
| FinOps | term | 云成本可见性 + 单位经济学 + 协作治理 | 外行只在账单暴涨后才看 | medium |
| Rightsizing | term | 按实际用量调整资源规格降本 | 外行长期超配 | medium |
| Spot / Preemptible | term | 可被回收的低价实例，适合容错负载 | 外行把有状态关键服务放 spot | low |
| Cell-based architecture | term | 把系统切成独立故障域限制爆炸半径 | 外行单一大故障域 | medium |
| Bulkhead | term | 资源隔离舱壁防一处故障耗尽全局 | 外行共享线程池 | low |
| Jitter (retry) | term | 重试加随机抖动防 thundering herd | 外行固定间隔重试致同步风暴 | low |
| Game day / DiRT | term | 计划内灾难演练验证韧性与流程 | 外行从不演练直接真出事 | low |
| SPACE framework | term | 开发者生产力多维度量框架 | 外行只看代码行/提交数 | medium |
| Stream-aligned team | term | Team Topologies 四类团队之一（对齐价值流） | 外行按技术分层组队 | medium |
| Sigstore / cosign | tool | 无密钥签名 + 透明日志（工件签名） | 外行不签名直接发布 | medium |
| Falco | tool | 运行时安全检测（基于 eBPF/syscall） | 外行只做构建期扫描 | medium |
| Conftest | tool | 用 OPA 测试配置/IaC 策略 | 外行无策略门禁 | medium |

---

## Outsider tells（外行破绽高亮，14 条）

> 直接喂 Phase 2.5 表达 DNA。来源 = intake.voice_register_indicators「反例版」+ 工程伦理 anchor。

| 外行说法 / 假设 | 内行实际意思 / 反应 | tell 类型 | evidence |
|----------------|--------------------|----------|----------|
| "我们要 100% 可用性" | 100% 是错误目标；可靠性是错误预算驱动的产品决策，每多一个 9 成本指数上升 | 价值观破绽 | [T06-S002, T06-S037] |
| "加个 DevOps 团队负责发布" | DevOps 是消除 dev/ops 鸿沟的文化；设孤立 DevOps 团队=造第三个筒仓（Team Topologies 明确批判） | 心智模型破绽 | [T06-S031] |
| "上生产手动改一下就行" / "SSH 进去修" | cattle not pets + 不可变基础设施；手工改造成 drift、不可复现、下次复现不了 | 操作纪律破绽 | [T06-S008, T06-S036] |
| "这个告警先静音吧反正一直响" | 告警必须 actionable；噪音告警要修/删而非静音，静音=alert fatigue 的温床、漏真告警 | 可靠性纪律破绽 | [T06-S005] |
| "备份肯定没问题不用测" | 未验证恢复的备份等于没有（GitLab 2017 五层备份全失效）；备份必须定期演练恢复 | 韧性破绽 | [T06-S004] |
| "先上 K8s + service mesh + multi-cloud 显得专业" | resume-driven development；多数公司不需要这些复杂度，瓶颈是基本功不是工具先进度 | 过度工程破绽 | [T06-S031] |
| "DevOps 就是跑 Jenkins 的岗位" | DevOps 是文化+实践运动；窄化为工具/岗位是根本误解 | 定义破绽 | [T06-S019] |
| "我们 SLA 99.9%"（但说不出 SLI 怎么算 / 不区分 SLO） | SLA=对外合同有罚则，SLO=内部目标，SLI=测量；混用暴露不懂 | 术语破绽 | [T06-S001] |
| "少发布就少出事" | 反直觉：低部署频率=大批量=更高变更失败率+更难定位；DORA 证明 elite 又快又稳 | 心智模型破绽 | [T06-S006, T06-S007] |
| "找到根因了，是某某的人为失误" | 复杂系统无单一根因；归咎个人=隐藏真相；说 "human error is the root cause" 是危险信号 | 复盘文化破绽 | [T06-S004] |
| "observability？就是上一套监控三件套" | observability 是能否回答没预设过的问题（unknown-unknowns），不是 SKU 打包 | 概念破绽 | [T06-S030] |
| "把 terraform.tfstate 提交到 git 方便共享" | state 含明文密钥+是危险操作面；必须远程加密加锁后端 | 安全破绽 | [T06-S036] |
| "用 git 存 YAML + CI 跑 kubectl apply 就是 GitOps" | 那是 CIOps/push；GitOps 强调 pull-based reconcile + drift 自动纠正 | 术语破绽 | [T06-S009] |
| "on-call 被叫醒是工程师韧性问题，扛一扛" | on-call 可持续性是伦理+管理问题；长期 burnout/alert fatigue 是管理失败 | 伦理破绽 | [T06-S004] |

---

## 行业拒绝的厂商话术（vendor-speak the field rejects，7 条）

| 厂商话术 | 行业为何拒绝 | evidence |
|---------|-------------|----------|
| "Single pane of glass"（单一观测大屏） | 营销老梗；现实是工具异构、上下文切换才是问题，一块屏解决不了根因分析 | [T06-S030] |
| "AIOps 会自动修复一切" | 抽象不消除运维责任；自动修复需要极强的可观测性+护栏，盲目 auto-remediate 会放大故障 | [T06-S035] |
| "NoOps"（无运维） | 运维责任不会消失只会换形态；serverless/托管服务仍需 SLO/可观测性/成本/容量管理 | [T06-S008] |
| "Serverless 消灭运维" | 仍需管 SLO、冷启动、成本、供应商风险、可观测性；只是 ops 形态变了 | [T06-S008] |
| "observability = 我们的 metrics+logs+traces 三个 SKU 打包" | Charity Majors 反复反对：observability 是能力（任意高基数下钻）不是产品组合 | [T06-S030] |
| "AI 自动运维取代 SRE" | 抽象层上移不消除可靠性工程判断；过度营销，标 secondary 仅作边界 | [T06-S030] |
| "买我们就 Well-Architected 了" | WAF 是评审框架/思考方式不是可购买状态；合规快照≠持续可靠性 | [T06-S020, T06-S021] |

---

## 标准·框架·认证（Standards / Frameworks / Certs）

### 标准 / 框架（带日期）

| 名称 | 类型 | Issued | Last revised | 一句话 | Decay | evidence |
|------|------|--------|--------------|--------|-------|----------|
| Google SRE discipline | 学科/方法论 | 2003（创立）/ 2016（SRE Book） | Workbook 2018; Building Secure & Reliable Systems 2020 | 可靠性的工程化学科，SLO/error budget/toil/blameless 的源头 | low | [T06-S001, T06-S002, T06-S003] |
| DORA / Accelerate | 研究框架 | 2014（首份报告）/ Accelerate 书 2018 | 2024 报告（新增 rework rate 第五指标，high 集群从 31%→22%） | 四个关键指标 + 24 项能力的实证研究 | medium | [T06-S006, T06-S007] |
| Twelve-Factor App | 方法论 | 2011（Heroku, Adam Wiggins） | 仍 v1（社区有 beyond-12-factor 讨论） | 云原生 SaaS app 的 12 条构建原则 | low | [T06-S008] |
| OpenTelemetry semantic conventions | 标准 | 2019（OTel 成立）；HTTP semconv v1.23 stable 2024 | semconv 持续滚动（v1.4x 系列 2025） | 遥测数据命名统一规范（CNCF 项目，与 Prometheus 合并 OpenMetrics 工作） | medium | [T06-S010, T06-S011] |
| CNCF 成熟度（Sandbox/Incubating/Graduated/Archived） | 治理框架 | 持续；criteria 由 TOC 维护 | criteria 滚动修订 | 项目成熟度阶梯：Graduated 需≥3 独立生产采用者+多组织 committer+第三方安全审计 | low | [T06-S014, T06-S015] |
| AWS Well-Architected Framework | 框架 | 2015；2021 加第六支柱 Sustainability | 持续更新 | 6 支柱：运营卓越/安全/可靠性/性能/成本/可持续 | low | [T06-S020] |
| Azure / GCP Well-Architected | 框架 | Azure WAF 5 支柱；GCP Architecture Framework | 持续更新 | 各云的架构评审框架，与 AWS 五/六支柱呼应 | low | [T06-S021] |
| SLSA | 标准 | v1.0 2023-04 | v1.1 2025-04（build track）；v1.2 草案 | 软件供应链完整性等级（Build L0-L3） | high | [T06-S012, T06-S013] |
| OpenMetrics | 标准 | 2017（基于 Prometheus exposition）；归档并入 OTel/Prometheus 路线 | 与 Prometheus exposition 融合 | metrics 暴露格式标准 | medium | [T06-S022, T06-S023] |
| OCI（image/runtime/distribution spec） | 标准 | 2015（Linux Foundation）；image-spec v1.0 2017 | image-spec v1.1（2024） | 容器镜像/运行时/分发的开放标准 | low | [T06-S018] |
| SemVer | 标准 | 2.0.0（2013, Tom Preston-Werner） | 稳定 | MAJOR.MINOR.PATCH 语义化版本 | low | [T06-S016] |
| Conventional Commits | 标准 | v1.0.0（2019） | 稳定 | 结构化 commit 消息规范（feat:/fix:/BREAKING CHANGE） | low | [T06-S017] |
| CIS Benchmarks | 安全基线 | 持续（各 K8s/云/OS 版本对应） | 跟随软件版本滚动 | 可审计的安全配置基线（Kubernetes/Docker/云）| medium | [T06-S025] |
| ISO/IEC 27001 | 标准（邻接） | 2005；现行 2022 版 | 2022（27001:2022） | 信息安全管理体系（与 DevSecOps/合规即代码邻接） | low | [T06-S026] |

### 认证 landscape（cert）

| 认证 | 颁发 | 面向 | 版本/更新 | evidence |
|------|------|------|-----------|----------|
| CKA (Certified Kubernetes Administrator) | CNCF/Linux Foundation | K8s 集群运维 | 跟随 K8s 版本（performance-based 实操考） | [T06-S014] |
| CKAD (Certified Kubernetes Application Developer) | CNCF/LF | 在 K8s 上部署应用 | 跟随 K8s 版本 | [T06-S014] |
| CKS (Certified Kubernetes Security Specialist) | CNCF/LF | K8s 安全（需先持 CKA） | 跟随 K8s 版本 | [T06-S014] |
| HashiCorp Terraform Associate | HashiCorp | IaC/Terraform 基础 | 003 版（2023+，覆盖 OpenTofu 分叉前知识） | [T06-S036] |
| 各云架构/运维认证 | AWS/GCP/Azure | 云平台（如 AWS SA/DevOps Pro, GCP PCA） | 各云滚动 | [T06-S020, T06-S021] |

> 认证注记（资深视角）：认证是入门/招聘信号，不等于运营深度；intake 明确"NOT 纯云认证速成"。CKA/CKS 因实操考含金量较高，纯选择题云认证次之。

### ITIL — 边界注记（legacy 范式）

- **是什么**: IT 服务管理框架（ITIL v3 2007 / ITIL 4 2019），强调流程化、变更审批委员会（CAB）、工单文化 (evidence: [T06-S029])
- **为何是边界**: intake 定位 ITIL 为"被 DevOps 取代的旧范式"。DevOps/SRE 用自动化变更管理 + 错误预算 + 小批量替代重型 CAB 审批；ITIL 4 已吸收部分敏捷/DevOps 理念但工单+变更委员会文化仍被视为高摩擦 (evidence: [T06-S029])
- **outsider-tell**: 用"提个变更工单走 CAB 审批"做常态部署流程 = 旧范式信号；内行用自动化流水线 + 渐进式发布替代 (evidence: [T06-S029])

---

## Phase 2 提炼提示

**「行业表达 DNA」直接素材**（喂 Phase 2.5）:
- **高频黑话 top 10**: error budget（是用来花的）/ toil（量化削减非美德）/ blameless / "who's IC?" / "declaring a SEV2" / "is this actionable" / GitOps vs ClickOps / cattle not pets / declarative not imperative / "do you really need K8s for this"
- **行业拒绝的厂商话术 top 5**: single pane of glass / NoOps / "serverless 消灭运维" / "observability = 三件套 SKU" / "AIOps 自动修复一切" —— 拒绝点共同反映价值观：**抽象不消除责任、可靠性是工程纪律不是采购**
- **外行破绽 top 10**: "100% 可用" / "加个 DevOps 团队" / "SSH 进去手工改" / "静音那个老响的告警" / "备份不用测" / "上 K8s+mesh+multi-cloud 显专业" / "少发布少出事" / "根因是某人失误" / "tfstate 提交 git" / "on-call 扛一扛就行"

**「智识谱系」线索**（喂 Phase 2.7）:
- 范式更替：ITIL/CAB 工单运维 → DevOps 文化（Patrick Debois 2009）→ SRE 工程化（Google 2003 起）→ 平台工程/IDP（Team Topologies）。每一跳都把"可靠性责任"往"工程化+自助化"推
- 流派张力：monitoring（known-unknowns，Prometheus 阵营）vs observability（unknown-unknowns，Honeycomb/Charity Majors 阵营）—— 不是对立而是层次，但厂商营销制造了对立
- 标准融合信号：OpenMetrics 并入 OpenTelemetry/Prometheus 路线、Ingress → Gateway API、Terraform → OpenTofu 分叉 —— 反映工具标准化与治理权之争

**「时效性」信号**（喂 Phase 2.8 诚实边界）:
- 过去 12 月内有显著变化：DORA 2024 报告（新增 rework rate 第五指标，吞吐/稳定关系重新表述）；SLSA v1.1（2025-04）+ v1.2 草案；OTel semconv 持续滚动至 v1.4x
- 预计 12 月内会变：SLSA Source/Dependencies/Verification track（仍草案，high decay）；OTel semconv（持续）；CNCF 项目成熟度名单（季度变动）；各 K8s 版本驱动的 CKA/CIS Benchmark 更新

**「工作流变化触发」种子**（喂 wave 3 Track 03）:
- SLSA/SBOM 供应链合规要求收紧 → CI/CD 流水线必须加 provenance 生成 + 签名（cosign）步骤
- DORA 2024 rework rate → 工程效能度量工作流可能新增此维度
- Gateway API 取代 Ingress → K8s 流量管理工作流迁移
- ISO 27001:2022 / 合规即代码 → 审计工作流从人工 review 转 policy-as-code（OPA/Conftest）门禁

**冷僻 / 信号薄弱自检**:
- 总术语数 = 52 (Tier 1) + 38 (Tier 2) = 90，远 > 25 floor ✅
- Tier 1 = 52 > 15 ✅；有 outsider-tell 的 Tier 1 术语 = 52/52 = 100% > 50% ✅
- 5 类 type 分布：term/acronym 极丰富，standard 充足（OCI/SLSA/SemVer/OTel/OpenMetrics/ISO），certification 中等（CKA/CKAD/CKS/Terraform Associate），regulation **N/A**（DevOps/SRE 是工程实践非强监管行业；ISO 27001/CIS 作为邻接安全标准而非法规，供应链安全 EO 14028 等政府令属边缘，未深入）
- **信号充沛，非冷僻行业**。surrogate 比例高（≈87% 一手为 surrogate_primary，因 .io/.dev/.com 核心域名不被 source_verifier 识别为 primary），但均为权威厂商/协会一手文档，诚实边界节应说明：mental model claim 多源自 Google SRE / DORA / CNCF 等机构一手，非独立第三方，建议二次校验时交叉对照 textbook（Accelerate / SRE Book）
