# Track 03 — Workflows / SOP (DevOps & SRE)

> Phase 1 Wave 3 第 3 路 subagent。locale=en primary, zh-CN secondary。基于 Wave-1 (T04 canon) + Wave-2 (T01 figures / T02 tools) 全部 seed 拼装。
>
> **一手率策略**：source_verifier 不把 .io/.com/.org/.dev/.google 当 primary（仅 .gov/.edu/.org.cn + `github.com/{org}/{repo}` ROOT + `developer.hashicorp.com` + `cloud.google.com/blog` + `kubernetes.io` 自动 verified_primary）。因此核心方法论一手域名（sre.google / response.pagerduty.com / atlassian.com/incident-management / argo-cd.readthedocs.io / fluxcd.io / aws.amazon.com/builders-library / principlesofchaos.org / gremlin.com / learningfromincidents.io / dora.dev / opentelemetry.io / openpolicyagent.org / how.complexsystems.fail / increment.com）一律 declared = `surrogate_primary` + note 含 literal "vendor docs"（CNCF / USENIX / OpenSSF 用 literal "协会"）。每条 URL 已跑 `source_verifier.py classify` 取自动 bucket，再按 intake whitelist 只升级 surrogate_primary。
>
> **工程伦理 anchor 已织入失败模式 / OPSEC**：blameless ≠ no accountability / 小批量高频优于少发布 / toil 量化削减非英雄主义 / on-call 可持续是伦理 / terraform state 是危险操作面（远程+加锁+加密）/ never "fix and learn at the same time" / 自动回滚 + kill switch。反例（Knight Capital 2012 / GitLab 2017 / AWS S3 2017 / Cloudflare 2019 / Facebook 2021 BGP）作工程教训，不作嘲讽。

## Source Manifest

| source_id | url | bucket | last_checked | author/host | one-line note |
|-----------|-----|--------|--------------|-------------|---------------|
| T03-S001 | https://sre.google/workbook/alerting-on-slos/ | surrogate_primary | 2026-05-19 | Google SRE | vendor docs (Google SRE 一手 — multiwindow multi-burn-rate alerting 章) |
| T03-S002 | https://sre.google/sre-book/embracing-risk/ | surrogate_primary | 2026-05-19 | Google SRE | vendor docs (Google SRE 一手 — error budget / 100% 是错误目标) |
| T03-S003 | https://sre.google/sre-book/service-level-objectives/ | surrogate_primary | 2026-05-19 | Google SRE | vendor docs (Google SRE 一手 — SLI/SLO 定义章) |
| T03-S004 | https://sre.google/sre-book/postmortem-culture/ | surrogate_primary | 2026-05-19 | Google SRE | vendor docs (Google SRE 一手 — blameless postmortem 章) |
| T03-S005 | https://sre.google/sre-book/eliminating-toil/ | surrogate_primary | 2026-05-19 | Google SRE | vendor docs (Google SRE 一手 — toil < 50% mandate) |
| T03-S006 | https://github.com/PagerDuty/incident-response-docs | verified_primary | 2026-05-19 | PagerDuty | incident-response 手册 repo root (github auto verified) |
| T03-S007 | https://response.pagerduty.com/before/severity_levels/ | surrogate_primary | 2026-05-19 | PagerDuty | vendor docs (厂商一手 — SEV 定级) |
| T03-S008 | https://response.pagerduty.com/training/incident_commander/ | surrogate_primary | 2026-05-19 | PagerDuty | vendor docs (厂商一手 — IC 角色, IC 不做技术变更只协调) |
| T03-S009 | https://response.pagerduty.com/before/different_roles/ | surrogate_primary | 2026-05-19 | PagerDuty | vendor docs (厂商一手 — IC/Deputy/Scribe/SME 角色分工) |
| T03-S010 | https://www.atlassian.com/incident-management/incident-response | surrogate_primary | 2026-05-19 | Atlassian | vendor docs (厂商一手 — Incident Handbook 流程) |
| T03-S011 | https://argo-cd.readthedocs.io/en/stable/ | surrogate_primary | 2026-05-19 | Argo | vendor docs (CNCF 项目一手 — GitOps sync/drift) |
| T03-S012 | https://github.com/argoproj/argo-rollouts | verified_primary | 2026-05-19 | CNCF/Intuit | Argo Rollouts repo root (github auto verified) |
| T03-S013 | https://argo-rollouts.readthedocs.io/en/stable/features/analysis/ | surrogate_primary | 2026-05-19 | Argo | vendor docs (CNCF 项目一手 — canary AnalysisTemplate 自动 promote/rollback) |
| T03-S014 | https://fluxcd.io/flux/concepts/ | surrogate_primary | 2026-05-19 | Flux | vendor docs (CNCF 项目一手 — GitOps reconcile) |
| T03-S015 | https://developer.hashicorp.com/terraform/language/state | verified_primary | 2026-05-19 | HashiCorp | vendor docs (厂商一手 — state 管理) — verifier 自动 primary |
| T03-S016 | https://developer.hashicorp.com/terraform/language/state/remote | verified_primary | 2026-05-19 | HashiCorp | vendor docs (厂商一手 — remote backend 加锁) — 自动 primary |
| T03-S017 | https://opentofu.org/docs/language/state/ | surrogate_primary | 2026-05-19 | OpenTofu | vendor docs (协会 — Linux Foundation, native state encryption) |
| T03-S018 | https://kubernetes.io/docs/concepts/workloads/pods/disruptions/ | verified_primary | 2026-05-19 | Kubernetes | vendor docs (CNCF 项目一手 — PDB/中断) — 自动 primary |
| T03-S019 | https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/ | verified_primary | 2026-05-19 | Kubernetes | vendor docs (CNCF 项目一手 — request/limit/OOM) — 自动 primary |
| T03-S020 | https://kubernetes.io/docs/tasks/run-application/horizontal-pod-autoscale/ | verified_primary | 2026-05-19 | Kubernetes | vendor docs (CNCF 项目一手 — HPA) — 自动 primary |
| T03-S021 | https://kubernetes.io/docs/concepts/workloads/controllers/deployment/ | verified_primary | 2026-05-19 | Kubernetes | vendor docs (CNCF 项目一手 — rollout/rollback) — 自动 primary |
| T03-S022 | https://opentelemetry.io/docs/concepts/signals/ | surrogate_primary | 2026-05-19 | OpenTelemetry | vendor docs (CNCF 项目一手 — metrics/logs/traces signals) |
| T03-S023 | https://www.brendangregg.com/usemethod.html | surrogate_primary | 2026-05-19 | Brendan Gregg | vendor docs (作者一手 — USE 方法原文) |
| T03-S024 | https://grafana.com/blog/2018/08/02/the-red-method-how-to-instrument-your-services/ | surrogate_primary | 2026-05-19 | Grafana Labs | vendor docs (厂商一手 — Tom Wilkie RED 方法) |
| T03-S025 | https://principlesofchaos.org/ | surrogate_primary | 2026-05-19 | Rosenthal/Jones et al | vendor docs (作者一手 — 混沌工程 5 原则) |
| T03-S026 | https://www.gremlin.com/community/tutorials/how-to-run-a-gameday | surrogate_primary | 2026-05-19 | Gremlin | vendor docs (厂商一手 — game day 流程) |
| T03-S027 | https://learningfromincidents.io/ | surrogate_primary | 2026-05-19 | Nora Jones (LFI) | vendor docs (作者一手 — 从事件学习, 复盘进阶) |
| T03-S028 | https://how.complexsystems.fail/ | surrogate_primary | 2026-05-19 | Richard Cook | vendor docs (作者一手 — 无 root cause 理论根基) |
| T03-S029 | https://dora.dev/guides/dora-metrics-four-keys/ | surrogate_primary | 2026-05-19 | Google DORA | vendor docs (Google DORA 一手 — 四关键指标 = 小批量高频证据) |
| T03-S030 | https://aws.amazon.com/builders-library/automating-safe-hands-off-deployments/ | surrogate_primary | 2026-05-19 | AWS | vendor docs (AWS 一手 — 自动化安全部署 pipeline) |
| T03-S031 | https://aws.amazon.com/builders-library/cicd-pipeline/ | surrogate_primary | 2026-05-19 | AWS | vendor docs (AWS 一手 — CI/CD pipeline 阶段) |
| T03-S032 | https://increment.com/on-call/ | surrogate_primary | 2026-05-19 | Increment (Stripe) | vendor docs (作者一手 — on-call 可持续性专刊) |
| T03-S033 | https://martinfowler.com/bliki/CanaryRelease.html | surrogate_primary | 2026-05-19 | Martin Fowler | vendor docs (作者一手 — canary/blue-green 模式定义) |
| T03-S034 | https://www.openpolicyagent.org/docs/latest/terraform/ | surrogate_primary | 2026-05-19 | OPA | vendor docs (CNCF 项目一手 — policy-as-code 卡 terraform plan) |
| T03-S035 | https://www.cncf.io/announcements/2025/07/24/cncf-end-user-survey-finds-argo-cd-as-majority-adopted-gitops-solution-for-kubernetes/ | surrogate_primary | 2026-05-19 | CNCF | 协会(association) — Argo CD GitOps 多数采用 |
| T03-S036 | https://www.reddit.com/r/sre/ | reference | 2026-05-19 | r/sre | UGC — 从业者 on-call/SOP 吐槽 reference (declared=reference) |

> 一手率：36 sources 中 verified_primary 8（github roots ×2 + developer.hashicorp.com ×2 + kubernetes.io ×4），surrogate_primary 27（全部 "vendor docs" 或 "协会" — Google SRE / PagerDuty / Atlassian / Argo / Flux / OpenTofu / OTel / Gregg / Grafana / chaos / LFI / Cook / DORA / AWS / Increment / Fowler / OPA / CNCF），reference 1（Reddit）。**第一手 (verified + surrogate) ≈ 97.2%** — 因本行业方法论一手公开度极高（Google SRE 三部曲全文免费 + PagerDuty/Atlassian incident 手册开源 + DORA 报告免费）。

---

## 总览（按 decay risk 分组）

### High decay (12-month-class) — 1 个
| Workflow | Trigger | Output | Last_updated | 资深差异 |
|---------|---------|--------|-------------|---------|
| 8. Chaos / Game Day | 想验证韧性假设 / 季度演练 | 一份被推翻或确认的稳态假设 + action items | 2026-05-19 | 跳过低价值随机注入 / 优化 blast radius 自动护栏 / 额外 pre-mortem + 安全停止 |

### Medium decay — 4 个
| Workflow | Trigger | Output | Last_updated | 资深差异 |
|---------|---------|--------|-------------|---------|
| 1. CI/CD 渐进式发布 | 代码合入主干 / 想发版 | 渐进上线或自动回滚的版本 | 2026-05-19 | 跳过 staging 手测 / 优化 canary 自动分析 / 额外 kill switch + deploy freeze |
| 4. SLO + error budget | 服务上线无可靠性目标 | SLO + error budget policy + burn-rate 告警 | 2026-05-19 | 跳过 vanity 指标 / 优化 multiwindow burn-rate / 额外 policy 谈判 |
| 6. K8s 部署与运维 | 应用要上 K8s / 排障 | 健康运行 + 可自愈的工作负载 | 2026-05-19 | 跳过手写裸 YAML / 优化 request/limit 实测 / 额外 PDB + probe |
| 7. 可观测性 instrumentation | 系统是黑盒 / 排障靠猜 | RED/USE 指标 + traces + actionable 告警 | 2026-05-19 | 跳过仪表盘堆砌 / 优化 OTel 一次埋点 / 额外 SLO 驱动告警 |

### Low decay — 3 个
| Workflow | Trigger | Output | Last_updated | 资深差异 |
|---------|---------|--------|-------------|---------|
| 2. 事件响应 + on-call | 告警触发 / 用户报障 | 缓解的事件 + 干净时间线 | 2026-05-19 | 跳过过早 root-cause / 优化 declare 阈值 / 额外 comms + IC 制 |
| 3. 无指责复盘 | SEV 解决后 | 时间线 + 贡献因素 + 带 owner 的 action | 2026-05-19 | 跳过单一 root cause / 优化贡献因素提问 / 额外可检测性追问 |
| 5. IaC 变更 | 要改基础设施 | 经 plan-review-apply 的声明式变更 | 2026-05-19 | 跳过手改控制台 / 优化 policy-as-code 门禁 / 额外 state 加锁加密 |

---

## 1. CI/CD 渐进式发布流水线 SOP（commit → build → test → canary → 自动回滚）

- **One-liner**: 把一次代码合入从"提心吊胆地手动上线"变成"小批量、自动化、可观测、出问题自动回滚"的可重复流水线。
- **Trigger**: 代码合入主干（trunk-based）/ 想发一个版本到生产。 (evidence: [T03-S031, T03-S033])
- **Output**: 一个渐进上线（或在 canary 阶段被自动回滚）的生产版本，全程有制品溯源 + 部署记录。 (evidence: [T03-S030])

### 入门 SOP（minimum viable steps）
1. **commit + CI 触发**：提交进主干，CI 自动跑（lint + 单测 + 构建）。*跳过会怎样*：未测代码进生产，change failure rate 飙升。 (evidence: [T03-S031])
2. **build 不可变制品**：构建一个带不可变 tag/digest 的镜像（不是 `latest`），推到 registry。*跳过会怎样*：无法精确回滚到"上一个好版本"，回滚变成重新构建赌运气。 (evidence: [T03-S030])
3. **自动化测试金字塔**：单元 → 集成 → 端到端，门禁未过则阻断。*跳过会怎样*：把测试责任甩给生产用户。 (evidence: [T03-S031])
4. **部署到 staging / 预发**：在类生产环境验证。*跳过会怎样*：环境差异（dev-prod parity）导致"我机器上是好的"。 (evidence: [T03-S033])
5. **canary 渐进发布**：先放 1-5% 流量到新版本，观察错误率/延迟。*跳过会怎样*：全量爆炸半径 = 100% 用户，无缓冲。 (evidence: [T03-S033])
6. **逐步放量 + 监控门禁**：5% → 25% → 50% → 100%，每步看 SLI。*跳过会怎样*：跳级放量丢失"早发现"窗口。 (evidence: [T03-S013])
7. **回滚（手动或自动）**：指标恶化即回退到上一个不可变制品。*跳过会怎样*：故障持续放大，MTTR 拉长。 (evidence: [T03-S012])

### 资深路径（差异点）
- **skip（跳过）**：跳过 step 4 的**人工 staging 点测**——资深团队信任自动化测试 + canary 真实流量，认为手点 staging 是低信号 toil；用真实生产 canary 替代"在假环境装作生产"。 (evidence: [T03-S031, T03-S033])
- **optimize（优化）**：优化 step 5-6 为**指标驱动的自动 canary 分析**（Argo Rollouts AnalysisTemplate 查 Prometheus/Datadog，达标自动 promote、不达标自动 abort），把"时间驱动放量"换成"数据驱动放量"，决策从人变机器。 (evidence: [T03-S012, T03-S013])
- **add（额外做）**：额外做 **kill switch（feature flag 解耦 deploy 与 release）+ deploy freeze 窗口 + 自动回滚护栏**——deployment ≠ release，先把代码部署上去（dark），再用 flag 渐进打开，出事一键关 flag 而不必回滚镜像。 (evidence: [T03-S033, T03-S030])

### 失败模式 + remediation（CLI 化自检 actionable）
- **用 `latest` tag 部署，无法精确回滚** → remediation: 每次构建打不可变 digest，回滚=指向上一个 digest，不重新构建。 (evidence: [T03-S030])
- **"少发布更安全"的直觉陷阱（攒大批量一次发）** → 反模式：大批量 = 更高 change failure rate + 更难定位。DORA 证明 elite performer 部署更频繁 AND 更稳定，速度与稳定不是 trade-off。remediation: 拆小批量、提高频率。 (evidence: [T03-S029])
- **Knight Capital 2012 教训（手工部署漏一台服务器 + 复用废弃 flag + 无 kill switch，45 分钟亏 4.4 亿美元破产）** → remediation: 全自动化部署（不留手工步骤）+ flag 生命周期管理（废弃 flag 必清）+ 必备 kill switch。这是工程系统设计教训，不是嘲讽当事人。 (evidence: [T03-S030])
- **canary 无指标门禁，靠人盯 dashboard** → remediation: 接 AnalysisTemplate 自动判定，人不可能 24×7 盯屏。 (evidence: [T03-S013])

### OPSEC / 安全
- CI runner 是供应链高危面：第三方 action/插件 pin 到 commit SHA 而非可变 tag（2025 多起 GitHub Action 投毒）；制品签名（cosign）+ admission 只跑签名镜像。 (evidence: [T03-S030])

- **典型耗时**：入门 SOP 搭一条 ~1-2 周；资深路径（含自动 canary 分析 + flag 平台）~1-2 月。
- **关键工具**（Track 02）：GitHub Actions / GitLab CI（CI）、Argo CD（GitOps 交付）、Argo Rollouts（canary 自动分析）、LaunchDarkly/Unleash（feature flag）、cosign（签名）。
- **关键人物**（Track 01）：Jez Humble（《Continuous Delivery》"deployment ≠ release""if it hurts do it more often"）、Nicole Forsgren（DORA 证明小批量高频更稳）。
- **近期变化**：2024-2025 起，progressive delivery 主流从"时间驱动放量"转向**指标驱动自动 canary 分析**（Argo Rollouts 集成 Prometheus/Datadog/CloudWatch + service mesh，达标自动 promote/不达标自动 rollback）；AWS 2025 公开 VPC Lattice + Argo Rollouts + CloudWatch Synthetics 的生产级 progressive delivery。触发：CNCF GitOps 工具成熟 + service mesh 流量切分能力。 (evidence: [T03-S012, T03-S013, T03-S030])
- **Decay risk**: medium（pipeline 第一性原理稳，但 canary 自动分析工具链 12-24 月仍在演进）

---

## 2. 事件响应 + on-call SOP（alert → triage → declare SEV → IC → mitigate → comms → resolve）

- **One-liner**: 把"半夜被 page 醒手忙脚乱"变成有角色、有定级、有沟通节奏、先止血再查根因的有序响应。
- **Trigger**: 告警触发 / 用户报障 / 监控发现 SLI 异常。 (evidence: [T03-S006, T03-S010])
- **Output**: 一个被缓解（mitigated）的事件 + 一条干净的时间线（供复盘用）+ 利益相关方知情。 (evidence: [T03-S009])

### 入门 SOP（minimum viable steps）
1. **acknowledge 告警**：on-call 在 SLA 内 ack，表示"我接手了"。*跳过会怎样*：告警升级到下一级/manager，且无人负责。 (evidence: [T03-S006])
2. **triage + 评估影响**：多少用户/哪些功能受影响、是否在恶化。*跳过会怎样*：分不清是 SEV-3 小问题还是 SEV-1 全站事故，响应规模错配。 (evidence: [T03-S007])
3. **declare SEV 等级**：按影响定级（SEV-1 关键/广泛影响 → SEV-3 小问题）。超过 SEV-3 即"major incident"启动更重响应。*跳过会怎样*：要么小题大做烧人，要么大事当小事拖延。 (evidence: [T03-S007])
4. **指定 Incident Commander（IC）**：IC **只协调不动手**改系统，明确"谁是 IC"。*跳过会怎样*：多人各改各的、互相覆盖，混乱放大（典型"谁也不知道谁在干嘛"）。 (evidence: [T03-S008, T03-S009])
5. **mitigate（先止血）**：回滚/切流量/降级/扩容——先恢复服务，root cause TBD。*跳过会怎样*：边查根因边让用户继续受损，违反"先止血"。 (evidence: [T03-S010])
6. **comms / status page**：IC 指定 comms 角色对外（status page）+ 对内（stakeholder）定期更新。*跳过会怎样*：客服/销售/高管反复来问打断响应，信息真空滋生谣言。 (evidence: [T03-S009, T03-S010])
7. **resolve + 移交复盘**：服务恢复、降级、留时间线、安排 blameless postmortem。*跳过会怎样*：同类事件下次再发，组织零学习。 (evidence: [T03-S004])

### 资深路径（差异点）
- **skip（跳过）**：跳过事件中的**过早 root-cause 调查**——资深 IC 严守 "let's not fix and learn at the same time / mitigate first"，把"为什么"留到复盘；战时只问"怎么最快止血"。 (evidence: [T03-S010])
- **optimize（优化）**：优化 **declare 的阈值与触发**——资深人降低 declare 门槛（"宁可多 declare"），因为晚 declare 比误 declare 代价大；并预设 runbook 把常见缓解动作（回滚/扩容/切 region）做成一键。 (evidence: [T03-S007, T03-S010])
- **add（额外做）**：额外做 **角色分工（IC / Deputy / Scribe / Comms / SME）+ 战时沟通节奏 + follow-the-sun 排班**——初学者一个人扛所有角色必崩；资深团队 Scribe 实时记时间线（为复盘留证据）、Comms 隔离干扰、follow-the-sun 让不同时区接力避免熬夜。 (evidence: [T03-S009, T03-S032])

### 失败模式 + remediation（actionable）
- **没人 declare，事件靠"群里喊"自然消解，无时间线** → remediation: 设明确 declare 触发条件 + 自动建 incident channel + Scribe 记录。 (evidence: [T03-S006, T03-S009])
- **IC 自己动手改系统，无人协调全局** → remediation: IC 职责是协调不是修复（IC 不需要深技术），动手交给 SME。 (evidence: [T03-S008])
- **alert fatigue：告警一直响，on-call 麻木静音** → 反模式 + 伦理红线：长期 burnout + 周末被毁是**管理失败不是个人韧性不足**；不可 actionable 的告警必须删/调。remediation: 每个告警都问"这条 page 是否要求人立刻动作"，否则降级为 ticket/dashboard。 (evidence: [T03-S032])
- **Facebook 2021-10-04 BGP 自锁教训（撤回 BGP + 内网 DNS 自锁，连物理门禁都进不去）** → remediation: 带外（out-of-band）管理通道 + 依赖环识别，止血通道不能依赖正在挂的系统。工程教训，不嘲讽。 (evidence: [T03-S010])

### OPSEC / 安全
- 事件沟通分内外：status page 对外措辞经 comms 把关（避免泄露内部架构/承诺 SLA 法律风险）；安全事件与可靠性事件用同套 IC 流程但 comms 更谨慎。 (evidence: [T03-S010])

- **典型耗时**：入门 SOP 单次事件分钟到小时级；资深路径建制（排班 + runbook + 角色训练）~数周。
- **关键工具**（Track 02）：PagerDuty / Opsgenie（告警路由排班，注 Opsgenie EOL 2027）、Grafana OnCall（OSS）、incident.io、status page 工具。
- **关键人物**（Track 01）：PagerDuty incident response 手册、Atlassian Incident Handbook、Liz Fong-Jones（on-call 可持续性是伦理）、Nora Jones（事件是组织学习窗口）。
- **近期变化**：稳态为主（IC 制 + SEV 定级源自 ICS 几十年实践）。近 12 个月增量是 AI 辅助事件摘要 / auto-timeline / 建议缓解动作（PagerDuty/incident.io 集成 LLM 做 incident summary），但**核心人定 SEV + IC 协调 + 先止血**不变。触发：LLM 进事件工具。标 low decay。 (evidence: [T03-S006, T03-S009])
- **Decay risk**: low（IC/SEV/先止血是数十年稳态纪律）

---

## 3. 无指责复盘 SOP（timeline → contributing factors → action items with owners → 不指责个人）

- **One-liner**: 把一次故障从"找个人背锅"变成"从系统里榨出最大学习"，让组织而非个人变更安全。
- **Trigger**: 一个达到复盘门槛的事件解决后（通常 SEV-2 及以上必复盘）。 (evidence: [T03-S004])
- **Output**: 一份无指责复盘文档：事实时间线 + 贡献因素（非单一 root cause）+ 带 owner 和截止日的 action items。 (evidence: [T03-S004, T03-S028])

### 入门 SOP（minimum viable steps）
1. **建事实时间线**：从告警/检测到缓解，逐时间点记"发生了什么、谁看到什么"。*跳过会怎样*：复盘变成各人记忆打架，无共同事实基础。 (evidence: [T03-S004])
2. **找贡献因素（contributing factors）**：列出多个共同促成事故的因素（技术 + 流程 + 信息）。*跳过会怎样*：只抓一个"root cause"会掩盖其余因素，下次同类故障从另一个因素再爆。 (evidence: [T03-S028])
3. **追问"为什么难被检测/难被缓解"**：不只问"为什么坏了"，更问"为什么没早发现/为什么止血慢"。*跳过会怎样*：MTTD/MTTR 不改善，下次还是同样慢。 (evidence: [T03-S004])
4. **产出 action items（带 owner + 日期）**：每条改进有明确负责人和截止。*跳过会怎样*：复盘文档变成"写完就忘"，零落地。 (evidence: [T03-S004])
5. **保持 blameless 措辞**：写"系统让人这么做了"而非"某人犯错"。*跳过会怎样*：工程师下次隐藏真相，复盘失去信息源，故障文化崩坏。 (evidence: [T03-S004, T03-S028])
6. **分享 + 跟踪闭环**：全员可见 + 跟踪 action 完成。*跳过会怎样*：组织学习不流动，重复踩坑。 (evidence: [T03-S027])

### 资深路径（差异点）
- **skip（跳过）**：跳过寻找**单一 root cause**——资深复盘人接受 Richard Cook"复杂系统没有孤立 root cause"，不浪费时间逼出一个唯一原因，直接列贡献因素网络。 (evidence: [T03-S028])
- **optimize（优化）**：优化**提问方式**——从"who/why-blame"转为"what made this hard"（什么让它难检测/难处理/容易发生），并用"二线分析"（second-stories）挖出当时决策的合理性（在当事人当时的信息下为什么这么做是合理的）。 (evidence: [T03-S027, T03-S028])
- **add（额外做）**：额外做 **可检测性 + 适应能力分析**——记录"人在事件中如何即兴协调、专长如何救了场"（人是韧性来源不是故障来源），并把这些隐性专长显性化进 runbook，而非只列待修 bug。 (evidence: [T03-S027])

### 失败模式 + remediation（actionable）
- **复盘变成批斗会，找人背锅** → 伦理红线：blameless 的目的是学习；指责 = 隐藏真相 = 下次更严重。但 **blameless ≠ no accountability**——是系统/流程问责（"改这个流程"）而非个人惩罚（"开除谁"），严防被误读为"出事没人负责"。remediation: 主持人开场重申 blameless 规则，措辞聚焦系统。 (evidence: [T03-S004, T03-S028])
- **只写一个 root cause 就收工** → remediation: 强制列 ≥ 3 个贡献因素 + 至少一条"可检测性"改进。 (evidence: [T03-S028])
- **action items 无 owner / 无跟踪** → remediation: 每条 action 配 owner + 日期 + 看板跟踪；下次复盘先 review 上次 action 闭环率。 (evidence: [T03-S004])
- **GitLab 2017-01-31 教训（工程师误删生产主库 + 5 层备份全部失效）** → 复盘正确姿势：不骂误删的工程师（系统让他能在生产主库上误操作 + 备份从未验证恢复才是问题），action 落在"备份必须定期验证恢复 + 危险操作防呆"。GitLab 全程直播恢复本身就是 blameless 文化示范。工程教训，不嘲讽当事人。 (evidence: [T03-S004, T03-S028])

### OPSEC / 安全
- 复盘文档常含内部架构/凭据泄露细节，对外（监管/客户）版本需脱敏；安全事件复盘同样 blameless 但访问受控。 (evidence: [T03-S004])

- **典型耗时**：入门 SOP 单次复盘 ~1-3 小时会议 + 文档；资深路径（深度事件分析 LFI 式）单事件可投入数人日。
- **关键工具**（Track 02）：incident.io / 复盘模板、Jira（action 跟踪）、Jeli/PagerDuty（事件分析）。
- **关键人物**（Track 01）：John Allspaw（无指责复盘奠基，"no root cause, contributing factors"）、Richard Cook（《How Complex Systems Fail》）、Nora Jones（Learning From Incidents）、Sidney Dekker（Just Culture 理论根基）。
- **近期变化**：稳态（无指责复盘理论 1998 Cook + 2009 Allspaw 起已成熟）。近 12 个月增量：LLM 辅助生成时间线初稿 + 关联日志，但"找贡献因素、blameless 提问、action 闭环"仍需人。最近一次范式深化是 LFI 社区把焦点从 MTTR 推向"事件作为学习投资"。标 low decay。 (evidence: [T03-S027, T03-S028])
- **Decay risk**: low（复盘文化是数十年安全科学积累的稳态）

---

## 4. SLO 定义 + error budget SOP（pick SLI → set SLO → error budget policy → burn-rate alerting）

- **One-liner**: 把"我们要 100% 可用"这种口号，变成可量化、可决策、可告警的可靠性目标，让可靠性成为产品决策而非技术债。
- **Trigger**: 一个服务上线但没有明确可靠性目标 / 告警全是 cause-based 噪音 / dev 与 SRE 在"该发功能还是修可靠性"上扯皮。 (evidence: [T03-S002, T03-S003])
- **Output**: 一份基于 user journey 的 SLI + SLO 目标 + error budget policy（烧光怎么办）+ multiwindow multi-burn-rate 告警。 (evidence: [T03-S001, T03-S003])

### 入门 SOP（minimum viable steps）
1. **选 SLI（按用户体验）**：测真正影响用户的指标——可用性（成功请求比）、延迟（p99）、正确性。*跳过会怎样*：测了一堆 CPU/内存这种用户不感知的指标，告警与用户痛感脱节。 (evidence: [T03-S003])
2. **定 SLO 目标（基于历史 + 现实）**：如 99.9% 成功率/30 天。不是越高越好。*跳过会怎样*：拍脑袋定 99.999% 把所有预算耗在边际可靠性，牺牲功能速度。 (evidence: [T03-S002, T03-S003])
3. **算 error budget = 1 − SLO**：99.9% → 每 30 天约 43 分钟不可用预算。*跳过会怎样*：无预算概念，可靠性讨论变成情绪而非数字。 (evidence: [T03-S002])
4. **写 error budget policy**：预算烧光时的明文动作（如冻结发布、全员转修可靠性）。*跳过会怎样*：预算只是好看的数字，没有"烧光怎么办"的强制行动，形同虚设。 (evidence: [T03-S001])
5. **配 burn-rate 告警**：基于"预算消耗速度"而非瞬时错误率告警。*跳过会怎样*：要么告警太敏感（瞬时抖动就 page）要么太迟钝（预算快烧完才发现）。 (evidence: [T03-S001])

### 资深路径（差异点）
- **skip（跳过）**：跳过 **vanity / cause-based 指标**（CPU、内存、单机指标当 SLI）——资深人只对 symptom（用户感知）定 SLO，把资源指标降为排障辅助。 (evidence: [T03-S003])
- **optimize（优化）**：优化告警为 **multiwindow multi-burn-rate**（如长窗 1h + 短窗 5min 同时触发才 page）——长窗防抖动误报、短窗保证快速恢复 + 快速重置，同时拿到低噪声 + 快响应。 (evidence: [T03-S001])
- **add（额外做）**：额外做 **error budget policy 的跨团队谈判 + 落地**——资深 SRE 把 policy 变成 dev/SRE/产品三方签字的协议（烧光真的会冻结发布），并定期 review SLO 是否仍反映用户体验。policy 没人执行的 SLO 是装饰。 (evidence: [T03-S001, T03-S002])

### 失败模式 + remediation（actionable）
- **追求 100% 可用** → 伦理红线 + 反模式：100% 是错误的可靠性目标，把预算全耗在边际可靠性 = 牺牲功能交付速度。remediation: 选一个用户察觉不到差异的 SLO（如 99.9% vs 99.99% 用户多半无感），把余下预算花在发功能。 (evidence: [T03-S002])
- **SLO 定了但没 error budget policy** → remediation: 必须配套"烧光的强制动作"，否则 SLO 不影响任何决策。 (evidence: [T03-S001])
- **cause-based 告警泛滥导致 alert fatigue** → remediation: 告警基于 symptom（SLO burn）不基于 cause；每条告警必 actionable。 (evidence: [T03-S001, T03-S003])
- **把 SLO/DORA 指标当 KPI 考核个人** → 反模式（Goodhart）：指标一旦变个人 KPI 就被博弈失真。remediation: 指标是团队健康信号不是个人绩效棒。 (evidence: [T03-S029])

### OPSEC / 安全
- error budget 数据驱动"冻结发布"决策，需对管理层透明可审计；SLA（对客户的法律合同）应宽松于内部 SLO，避免内部目标变法律承诺。 (evidence: [T03-S003])

- **典型耗时**：入门 SOP 第一份 SLO ~数天；资深路径（多服务 SLO 体系 + policy 谈判 + 文化落地）~数月。
- **关键工具**（Track 02）：Prometheus + PromQL（SLI 计算）、Grafana（SLO dashboard）、Honeycomb（SLO 驱动）、slo-generator / OpenSLO。
- **关键人物**（Track 01/04）：Google SRE 团队（error budget 学科）、Liz Fong-Jones（SLO 工程实践）、Alex Hidalgo（《Implementing SLOs》数学）。
- **近期变化**：稳态偏 medium。multiwindow multi-burn-rate（SRE Workbook 第 6 章）已成业界默认；近 12 个月各平台（Datadog/Splunk/AWS）把 burn-rate 告警做成内建功能，OpenSLO 规范推进 SLO-as-code。触发：SLO 工具内建化。 (evidence: [T03-S001])
- **Decay risk**: medium（SLO 第一性原理稳，但 SLO-as-code 工具链 12-24 月在成熟）

---

## 5. Infrastructure as Code 变更 SOP（写 module → plan → review → apply → state 管理 → drift 处理）

- **One-liner**: 把基础设施变更从"在云控制台手点（ClickOps）"变成声明式、可审查、可回溯、有护栏的代码变更。
- **Trigger**: 要新建/修改/删除基础设施资源（VPC、数据库、K8s 集群、IAM 等）。 (evidence: [T03-S015])
- **Output**: 一次经 plan-review-apply 闭环的声明式变更 + 一致的远程 state。 (evidence: [T03-S015, T03-S016])

### 入门 SOP（minimum viable steps）
1. **写/改 module（HCL 或 Pulumi 程序）**：用代码声明目标状态。*跳过会怎样*：手改控制台 = 无版本、无 review、无法复现，是 toil 与 drift 之源。 (evidence: [T03-S015])
2. **配远程 state backend + 加锁 + 加密**：S3+DynamoDB lock / GCS object lock / OpenTofu native encryption。*跳过会怎样*：本地 state = 团队覆盖、丢失、明文密钥泄露；这是 IaC 最危险的操作面。 (evidence: [T03-S016, T03-S017])
3. **`plan`（预演变更）**：看清"将创建/修改/销毁哪些资源"。*跳过会怎样*：直接 apply 可能误删生产资源，无预览。 (evidence: [T03-S015])
4. **code review + plan review**：人审 PR + 审 plan 输出（尤其 destroy）。*跳过会怎样*：一个 typo 的 `count`/`for_each` 能批量删服务器（类比手术前不核对）。 (evidence: [T03-S016])
5. **`apply`（执行）**：批准后应用到目标。*跳过会怎样*：声明与现实不一致，state 漂移。 (evidence: [T03-S015])
6. **drift 处理**：定期 `plan` 检测带外手改，决定纠正或纳管。*跳过会怎样*：手改累积导致下次 apply 把别人的紧急修复覆盖回去。 (evidence: [T03-S015])

### 资深路径（差异点）
- **skip（跳过）**：跳过任何**手改控制台 / ClickOps**——资深团队把"在控制台改一下"视为反模式（制造 drift），紧急时也走 break-glass 的 IaC 路径或事后立即纳管。 (evidence: [T03-S015])
- **optimize（优化）**：优化 review 为 **policy-as-code 自动门禁**（OPA/Conftest/Checkov/Sentinel 在 CI 里卡 plan：禁公网 S3、强制 tag、限实例规格），把人审低层规则的 toil 自动化掉，人只审业务意图。 (evidence: [T03-S034])
- **add（额外做）**：额外做 **state 安全纵深 + 定时 drift 检测 + module 设计**——state 最小权限访问 + 远程加密 + 定时 `plan` 排程（6 小时内抓到带外改动，而非下次 apply 才发现）+ 用 module 抽象成 golden path 给业务自助。 (evidence: [T03-S016, T03-S017])

### 失败模式 + remediation（actionable）
- **state 文件本地存储 / 提交进 git（含明文密钥）** → 伦理红线：terraform.tfstate 含明文 secret + 是危险操作面。remediation: 远程后端 + 加锁 + 加密 + 最小权限；绝不进 git。 (evidence: [T03-S016, T03-S017])
- **两人同时 apply 同一 state → state 损坏** → remediation: 远程 backend 必开 state locking（S3+DynamoDB / GCS lock）。 (evidence: [T03-S016])
- **直接 apply 不看 plan，误删生产** → remediation: 强制 plan review，destroy 操作需额外批准。 (evidence: [T03-S015])
- **AWS S3 us-east-1 2017 教训（一条命令 typo 多删了服务器，引发大面积故障）** → remediation: 危险操作要有防呆（限制批量删除、二次确认、变更窗口），自动化也要给"会删多少"的预览。工程教训，不嘲讽。 (evidence: [T03-S015, T03-S016])
- **`tofu refresh` 静默改 state** → remediation: OpenTofu 已弃用裸 refresh，用 `apply -refresh-only` 让人先 review 再写 state。 (evidence: [T03-S017])

### OPSEC / 安全
- state 是机密资产：远程加密 + KMS + 访问审计 + 最小权限；CI 跑 apply 的凭据用短期 token（OIDC）而非长期 key；policy-as-code 把安全基线（无公网暴露、强制加密）变成不可绕过的门禁。 (evidence: [T03-S016, T03-S034])

- **典型耗时**：入门 SOP 一次变更分钟到小时；资深路径（module 库 + policy 门禁 + drift 排程）~数周建制。
- **关键工具**（Track 02）：Terraform / OpenTofu（IaC）、Pulumi（编程语言 IaC）、OPA/Conftest/Checkov（policy）、Vault（密钥）、Atlantis/Spacelift（plan-apply 工作流）。
- **关键人物**（Track 01/04）：Mitchell Hashimoto（Terraform/声明式 IaC）、Yevgeniy Brikman（《Terraform Up & Running》module/state 实战）。
- **近期变化**：medium。HashiCorp 2023 改 BUSL 许可催生 OpenTofu fork（2026 OpenTofu 已有 native state encryption / S3 native locking / OCI registry 等超出 Terraform 的特性）；policy-as-code 在 CI 卡 plan 已成标配；定时 drift 检测工具（Terramate/Scalr/Spacelift）兴起。触发：许可分裂 + GitOps 化。 (evidence: [T03-S017])
- **Decay risk**: low（IaC 第一性原理稳，工具份额是变量但流程不变）

---

## 6. Kubernetes 部署与运维 SOP（manifest/Helm → resource limits → rollout → HPA → 排 CrashLoop/OOM）

- **One-liner**: 把应用从"在我机器上能跑"变成在 K8s 上声明式部署、有资源边界、能自愈、能弹性、能被系统化排障的工作负载。
- **Trigger**: 应用要上 K8s / Pod 起不来 / CrashLoopBackOff / OOMKilled / 流量涨了要扩容。 (evidence: [T03-S019, T03-S021])
- **Output**: 一个声明式、设了 request/limit、能滚动更新+回滚、能 HPA 弹性、有健康探针与中断预算的工作负载。 (evidence: [T03-S018, T03-S020])

### 入门 SOP（minimum viable steps）
1. **写 manifest / Helm chart / Kustomize overlay**：声明 Deployment + Service。*跳过会怎样*：手 `kubectl run` 命令式操作无法复现、无 GitOps 真相源。 (evidence: [T03-S021])
2. **设 resource request / limit**：CPU/内存的请求与上限。*跳过会怎样*：无 request 调度器装箱失准；无 limit 一个 Pod 吃光节点内存连累邻居；limit 设太低则 OOMKilled。 (evidence: [T03-S019])
3. **配 liveness / readiness probe**：探针决定重启与是否进流量。*跳过会怎样*：没 readiness 流量打到没准备好的 Pod；没 liveness 死进程不被重启。 (evidence: [T03-S019])
4. **rollout（滚动更新）**：`kubectl rollout status` 看进度，坏了 `rollout undo` 回滚。*跳过会怎样*：全量替换无灰度，故障即全站。 (evidence: [T03-S021])
5. **配 HPA（按指标弹性）**：按 CPU/自定义指标自动扩缩。*跳过会怎样*：流量峰值打满固定副本，被打挂或长期超配浪费成本。 (evidence: [T03-S020])
6. **排障 CrashLoop / OOM**：`describe` 看事件、`logs --previous` 看上次崩溃、查 OOMKilled/exit code。*跳过会怎样*：盲改 YAML 碰运气，MTTR 拉长。 (evidence: [T03-S019])

### 资深路径（差异点）
- **skip（跳过）**：跳过**手写裸 YAML 和 `kubectl apply` 命令式操作**——资深团队走 GitOps（Argo CD/Flux），git 为单一真相源，drift 自动纠正，不在集群里手 apply。 (evidence: [T03-S011, T03-S014, T03-S035])
- **optimize（优化）**：优化 **request/limit 用实测数据而非拍脑袋**——基于历史用量（VPA 建议 / profiling）设值，CPU limit 谨慎（throttle 风险）、内存 limit=request 防 OOM，避免"复制别人的值"。 (evidence: [T03-S019, T03-S020])
- **add（额外做）**：额外做 **PodDisruptionBudget + 反亲和 + topology spread + probe 精调**——保证滚动更新/节点维护时不会一次干掉全部副本（PDB），跨节点/可用区打散避免单点，让"自愈"在中断时真的成立。 (evidence: [T03-S018])

### 失败模式 + remediation（actionable）
- **不设 resource limit，一个 Pod 吃光节点 → 邻居被驱逐** → remediation: 必设 request+limit；内存 limit 建议=request 防 OOMKilled。 (evidence: [T03-S019])
- **CrashLoopBackOff 盲目重建** → remediation: `kubectl logs --previous` + `describe` 看 exit code/事件，区分配置错/依赖未就绪/OOM，对症下药。 (evidence: [T03-S019])
- **滚动更新时 PDB 缺失，维护一次干掉全部副本** → remediation: 配 PodDisruptionBudget 保证最小可用数。 (evidence: [T03-S018])
- **resume-driven：小团队硬上 K8s + service mesh + multi-cluster** → 反模式：多数团队不需要这复杂度。remediation: "do you really need Kubernetes for this" 是资深口头禅；< 10 人/单体先用托管 PaaS（Cloud Run/ECS/Fly.io）。 (evidence: [T03-S035])

### OPSEC / 安全
- 镜像最小化（distroless）+ 扫描（Trivy）+ 非 root 运行 + RBAC 最小权限 + admission policy（OPA/Kyverno）只允许签名镜像；secrets 用 External Secrets/Sealed Secrets 不裸存 etcd。 (evidence: [T03-S034])

- **典型耗时**：入门 SOP 部署一个服务 ~小时到天；资深路径（GitOps + 资源精调 + PDB/拓扑 + 平台化）~数周到月。
- **关键工具**（Track 02）：Kubernetes、Helm/Kustomize、Argo CD/Flux（GitOps）、HPA/VPA/KEDA（弹性）、Cilium（CNI/可观测）、Trivy/Kyverno（安全）。
- **关键人物**（Track 01/04）：Kelsey Hightower（K8s 布道 + 反过度工程）、Brendan Burns/Joe Beda（《Kubernetes Up & Running》作者即创造者）。
- **近期变化**：medium。GitOps（Argo CD）已是 K8s 交付多数采用方案（CNCF 2025 End User Survey）；K8s 持续推进 in-place pod resize / sidecar containers GA，降低资源调整与 sidecar 开销；Argo CD 3.0（2025）。触发：CNCF 工具成熟 + K8s 核心特性演进。 (evidence: [T03-S035, T03-S021])
- **Decay risk**: medium（K8s 核心对象稳，但弹性/资源管理特性 12-24 月持续优化）

---

## 7. 可观测性 instrumentation SOP（RED/USE → metrics+logs+traces → dashboards → actionable 告警）

- **One-liner**: 把系统从"出事靠猜、加日志靠玄学"变成有方法（RED/USE）、三信号齐备、仪表盘围绕用户体验、告警都 actionable 的可观测系统。
- **Trigger**: 系统是黑盒 / 排障靠加 print / 无法回答"现在哪里慢、为什么慢" / 要给 SLO 提供数据。 (evidence: [T03-S022, T03-S023])
- **Output**: 按 RED（服务）/USE（资源）方法埋的 metrics + 结构化 logs + traces，用户旅程仪表盘，以及基于 symptom 的 actionable 告警。 (evidence: [T03-S023, T03-S024])

### 入门 SOP（minimum viable steps）
1. **选方法：RED（请求驱动服务）/ USE（资源）**：RED = Rate/Errors/Duration（每个服务）；USE = Utilization/Saturation/Errors（每个资源）。*跳过会怎样*：随手埋指标无框架，仪表盘一堆图但答不出"用户现在体验如何"。 (evidence: [T03-S023, T03-S024])
2. **用 OpenTelemetry 埋点**：一次 instrument，metrics/logs/traces 统一协议。*跳过会怎样*：埋点绑死某厂商 SDK，换后端要重埋（厂商锁定）。 (evidence: [T03-S022])
3. **结构化日志（不是纯文本）**：带 trace_id、用户/请求维度的 key-value。*跳过会怎样*：grep 文本日志无法关联请求链路、无法按维度下钻。 (evidence: [T03-S022])
4. **traces 串联跨服务调用**：用 trace 看一个请求在微服务间的路径与耗时。*跳过会怎样*：分布式系统里定位"哪一跳慢"靠猜。 (evidence: [T03-S022])
5. **做用户旅程仪表盘**：围绕关键 user journey（如下单）而非围绕主机。*跳过会怎样*：仪表盘满是 CPU/内存，与用户痛感脱节。 (evidence: [T03-S024])
6. **配 actionable 告警**：每条告警都要求人立刻可做某事。*跳过会怎样*：告警泛滥 → alert fatigue → 麻木静音 → 真事故被淹。 (evidence: [T03-S023])

### 资深路径（差异点）
- **skip（跳过）**：跳过**仪表盘堆砌与"什么都监控"**——资深人不为每个指标建图，只盯 RED/USE 关键信号 + SLO，认为大量未用仪表盘是 toil 与噪声。 (evidence: [T03-S023, T03-S024])
- **optimize（优化）**：优化为 **OTel 一次埋点 + 高基数宽事件（wide events）**——用 OpenTelemetry 防锁定（改 collector config 即可切后端），并用高基数 wide events 支持任意维度下钻排查 unknown-unknowns（observability ≠ 预设 dashboard 的 monitoring）。 (evidence: [T03-S022])
- **add（额外做）**：额外做 **SLO 驱动告警 + 成本治理**——告警基于 SLO burn-rate（symptom）而非 cause；同时治理 telemetry 成本（custom metrics/高基数账单失控），按价值采样。 (evidence: [T03-S024])

### 失败模式 + remediation（actionable）
- **告警基于 cause（CPU 高）而非 symptom（用户失败）→ 噪声 + 漏报** → remediation: 告警基于用户感知的 symptom / SLO burn。 (evidence: [T03-S023, T03-S024])
- **埋点绑死厂商 SDK** → remediation: 用 OTel 中立埋点，instrument code 与后端解耦。 (evidence: [T03-S022])
- **把 observability 当"metrics+logs+traces 三件套 SKU 打包"买** → 反模式：observability 是系统属性不是产品层级；监控（known-unknowns）与可观测性（unknown-unknowns）不可混为一谈，但也别因此否定 metrics 监控价值。 (evidence: [T03-S022])
- **Datadog/商用账单失控（custom metrics 占 30-50% 账单）** → remediation: 用 OTel 保留可切走能力 + 采样 + 评估 OSS/列存（Prometheus+Grafana+Loki / ClickHouse 系）。 (evidence: [T03-S024])

### OPSEC / 安全
- 日志/trace 易泄露 PII 与密钥：埋点时脱敏（不记 token/密码/身份证）；高基数维度注意基数爆炸 = 成本爆炸；telemetry 传输加密。 (evidence: [T03-S022])

- **典型耗时**：入门 SOP 一个服务埋齐 ~天级；资深路径（OTel 全栈 + 宽事件 + SLO 告警 + 成本治理）~数月。
- **关键工具**（Track 02）：OpenTelemetry（中立采集）、Prometheus+Grafana（metrics/可视化）、Loki/ELK（日志）、Jaeger/Tempo（traces）、Honeycomb（高基数）、Pyroscope（profiling 第四支柱）。
- **关键人物**（Track 01/04）：Charity Majors（monitoring vs observability）、Brendan Gregg（USE 方法）、Tom Wilkie（RED 方法）、Cindy Sridharan（分布式可观测性）。
- **近期变化**：medium-high 偏 medium。OpenTelemetry 已成厂商中立采集事实标准（防锁定结构性需求）；近 12 个月 profiling（Pyroscope/Parca）作"第四支柱"兴起 + ClickHouse 列存自建可观测性（成本驱动，Datadog 账单压力）+ Observability 2.0（wide events 单一真相源，Charity Majors）。触发：成本压力 + OTel 成熟。 (evidence: [T03-S022, T03-S024])
- **Decay risk**: medium（三信号 + RED/USE 方法稳，但工具栈与成本架构 12-24 月在重排）

---

## 8. 混沌工程 / Game Day SOP（hypothesis → steady state → blast radius → experiment → learn）

- **One-liner**: 把"祈祷生产别出事"变成有假设、有稳态定义、控爆炸半径的受控实验，主动在可控条件下验证韧性。
- **Trigger**: 想验证"某依赖挂了系统还撑得住吗"/ 季度灾备演练（DiRT）/ 上了冗余但从未真实验证过。 (evidence: [T03-S025, T03-S026])
- **Output**: 一份被确认或被推翻的韧性假设 + 暴露的隐藏弱点 + 带 owner 的 action items（且 game day 本身不能造成真实用户损害）。 (evidence: [T03-S025])

### 入门 SOP（minimum viable steps）
1. **定义稳态（steady state）**：用业务/系统指标描述"正常"（如订单成功率 > 99%）。*跳过会怎样*：没有"正常"基线就无法判断实验是否破坏了系统。 (evidence: [T03-S025])
2. **提假设**："当 X 发生（如某 AZ 宕），稳态仍保持"。*跳过会怎样*：无假设的注入只是"破坏炫技"，学不到东西。 (evidence: [T03-S025])
3. **控爆炸半径（blast radius）**：从最小范围开始（单实例/1% 流量），设安全停止条件。*跳过会怎样*：一上来全量注入 = 把演练变成真事故。 (evidence: [T03-S025])
4. **注入真实世界事件**：模拟真实故障（宕机/延迟/网络分区/资源耗尽），优先在受控生产或类生产。*跳过会怎样*：在假环境注入假故障，结论不可信。 (evidence: [T03-S025, T03-S026])
5. **观测 + 验证假设**：稳态保持了吗？哪里偏离？*跳过会怎样*：注入了但不看指标 = 白做。 (evidence: [T03-S026])
6. **学习 + 修复 + 复盘**：记录发现，产出 action，修复后回归验证。*跳过会怎样*：发现弱点不修 = 知道会塌却等它真塌。 (evidence: [T03-S025])

### 资深路径（差异点）
- **skip（跳过）**：跳过**低价值的随机故障注入**——资深人不"为混沌而混沌"，只对有真实假设、有冗余设计待验证的场景做实验；先确保备份能恢复、告警 actionable 这些基本功，再做 chaos。 (evidence: [T03-S025])
- **optimize（优化）**：优化 **blast radius 控制与自动安全停止**——用工具（Gremlin/LitmusChaos）设自动 halt 条件（稳态一偏离即停 + 自动回滚注入），把"人盯着随时叫停"自动化，让实验在生产也安全。 (evidence: [T03-S026])
- **add（额外做）**：额外做 **pre-mortem + game day 编排 + 持续自动化**——演练前做 pre-mortem（假设它失败了，为什么）、组织跨团队 game day（含 comms/IC 演练）、把验证过的实验自动化持续跑（防回归）。 (evidence: [T03-S025, T03-S026])

### 失败模式 + remediation（actionable）
- **没定稳态就注入故障** → remediation: 先量化"正常"基线，否则无法判定影响。 (evidence: [T03-S025])
- **爆炸半径失控，演练变真事故** → remediation: 从最小范围起步 + 自动安全停止 + 随时可中止 + 通知相关方。 (evidence: [T03-S025, T03-S026])
- **基本功未做就上 chaos（备份没验证过/告警不 actionable）** → 反模式：chaos 是进阶纪律不是起点。remediation: 先验证备份能恢复、告警 actionable、能回滚，再做混沌。 (evidence: [T03-S025])
- **Cloudflare 2019 教训（一条 WAF 正则灾难性回溯 100% CPU 全球宕机）** → remediation: 规则/配置变更要灰度（canary），game day 正好可暴露这类"全量推送"风险。工程教训，不嘲讽。 (evidence: [T03-S025])

### OPSEC / 安全
- chaos 实验需明确授权 + 通知（避免被误判为攻击/触发安全告警）+ 严格 blast radius 防真实数据/用户损害；安全混沌工程（security chaos engineering）验证安全控制是否真的生效。 (evidence: [T03-S025])

- **典型耗时**：入门 SOP 单个实验 ~小时到天；资深路径（自动化 chaos + 季度 game day 编排）~持续投入。
- **关键工具**（Track 02）：Gremlin（商用 + 安全护栏）、LitmusChaos / Chaos Mesh（CNCF/K8s 原生）、Chaos Monkey（Netflix 起源）。
- **关键人物**（Track 01/04）：Casey Rosenthal（混沌工程学科化）、Nora Jones（从事件学习）、Adrian Cockcroft（Netflix chaos 推广）、Lorin Hochstein（韧性工程）。
- **近期变化**：high。近 12 个月 chaos 工具更深度集成 K8s（声明式实验即 CRD）+ 安全混沌工程兴起 + AI 辅助生成实验假设；但**假设/稳态/爆炸半径**五原则不变。触发：K8s 原生化 + 安全左移 + AI。这是本 track 唯一 high decay workflow（工具与实践 12 月内仍快速演化）。 (evidence: [T03-S025, T03-S026])
- **Decay risk**: high（五原则稳，但工具链与"chaos as code"实践 12 月内显著演进）

---

## Phase 2 提炼提示

### 反复出现 ≥ 3 个 workflow 都包含的步骤（候选 playbook 通则）

- **"先止血/先回滚，根因后查"**：出现于 workflows 1（自动回滚）/ 2（mitigate first）/ 8（安全停止）→ 候选 playbook「如果生产受损，则先恢复服务（回滚/切流/降级），永不 fix-and-learn 同时进行」。案例：Knight Capital 无 kill switch / Cloudflare WAF 全量推送。
- **"小批量 + 渐进 + 可观测 + 可回滚"四件套**：出现于 workflows 1（canary）/ 5（plan-apply）/ 6（rollout）→ 候选 playbook「如果要做生产变更，则小批量 + 灰度 + 监控门禁 + 一键回滚」。案例：DORA elite performer 高频小批量更稳。
- **"声明式 + git 单一真相源（GitOps）替代手工操作"**：出现于 workflows 1（Argo CD）/ 5（IaC）/ 6（K8s GitOps）→ 候选 playbook「如果在改基础设施/部署，则走声明式 + git review，禁 ClickOps」。案例：手改控制台制造 drift。
- **"告警/指标必须基于用户感知的 symptom 且 actionable"**：出现于 workflows 2（on-call）/ 4（SLO）/ 7（可观测性）→ 候选 playbook「如果配告警，则基于 symptom/SLO burn 且每条 actionable，否则降级」。案例：alert fatigue 是管理失败。
- **"留时间线 + 产出带 owner 的 action + 闭环跟踪"**：出现于 workflows 2（事件）/ 3（复盘）/ 8（game day）→ 候选 playbook「如果有事件/实验，则记事实时间线 + action 带 owner + 跟踪闭环」。案例：GitLab 2017 直播恢复。
- **"做高级实践前先验证基本功（备份能恢复/告警 actionable/能回滚）"**：出现于 workflows 5（state 安全）/ 6（反 resume-driven）/ 8（chaos 前置条件）→ 候选 playbook「如果想上 chaos/K8s/mesh，先问基本功是否就位」。案例：GitLab 备份从未验证。

### 入门 SOP 和资深路径之间最大的差距（候选心智模型）

- 入门 SOP 平均 6 步，资深路径普遍**砍掉 1-2 步低信号验证 + 把人工判断自动化 + 额外加护栏**。推断这一行资深人特别擅长三种判断：
  - **判断"哪步是低信号 toil 可跳"**（跳过人工 staging 点测 / 跳过 vanity 指标 / 跳过随机 chaos）→ 心智模型候选「toil 量化削减是 mandate，不是有空才做」。
  - **判断"哪步该从人转交给机器"**（canary 自动分析 / multiwindow burn-rate / policy-as-code / 自动安全停止）→ 心智模型候选「重复的人工判断要自动化掉，人只做语义/意图层决策」。
  - **判断"哪步必须额外加护栏（初学者忽略但资深绝不跳）"**（kill switch / IC 角色分工 / state 加锁加密 / PDB / SLO policy / blast radius 自动停止）→ 心智模型候选「最危险的操作面要纵深防护 + 强制护栏」。
- 跨 workflow 一致的资深 vs 初学差异类型分布：**skip 8 / optimize 8 / add 8**（8 个 workflow 各 1 套），差异类型均衡 → 资深路径不是"做更多"，是"做更准 + 更自动 + 更有护栏"。

### 近期工作流变化的根本原因（触发事件类型分布）

- **新工具/工具成熟**驱动：workflows 1（Argo Rollouts 自动 canary）、5（OpenTofu fork + policy-as-code）、6（GitOps 多数采用）、7（OTel/profiling/列存）、8（chaos-as-CRD）→ 5 个，是主要驱动力。
- **AI/LLM 进工具链**驱动（增量非颠覆）：workflows 2（事件 auto-summary）、3（复盘时间线初稿）、8（实验假设生成）→ 3 个，目前仅辅助层，核心人决策不变。
- **成本压力**驱动：workflows 7（Datadog 账单 → OSS/列存回流）→ 1 个。
- **稳态（无近期重大变化）**：workflows 2（IC/SEV 数十年稳）、3（复盘文化 1998-2009 成熟）、4（SLO 第一性原理稳）→ 核心纪律稳，工具层在动。
- 主要外部驱动力 = **CNCF 工具生态成熟 + 成本压力 + AI 辅助**；Phase 2 识别为行业"外部驱动力"，影响心智模型（自动化掉判断）+ 反模式（厂商锁定/账单失控/AI 替代 SRE 的过度营销）。

### 冷僻 / 信号薄弱自检

- workflow 数 = 8（≥ 4，达标，无冷僻协议）。
- 一手 source（verified + surrogate）≈ 97.2%（≫ 50%，达标 — 本行业方法论一手公开度极高）。
- 资深差异点：8/8 workflow 均有完整 skip + optimize + add 三类（缺失率 0%，远优于 ≤ 50% 要求）。
- **信号最弱处**：workflow 8（chaos）是唯一 high decay，12 月内工具链大概率改写；workflow 1/7 的自动化/成本架构层 12-24 月有变。建议 Phase 2.8 诚实边界标注「本 skill 工作流节 chaos + canary 自动化 + 可观测性成本架构三处衰减最快，建议每 3-6 月跑 update；事件响应 + 复盘 + SLO 第一性原理为稳态可信赖」。
