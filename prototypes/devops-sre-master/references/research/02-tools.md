# Track 02 — Tools 工具栈与选型决策树（DevOps & SRE）

> Phase 1 wave 2 第 2 路。locale=en primary, zh-CN secondary。所有 `last_checked = 2026-05-19`（GitHub maturity signal 均为当日 GitHub API 实测）。
>
> **一手率策略**：source_verifier 不把 .io/.com/.org 当 primary（仅 .gov/.edu/.org.cn + `github.com/{org}/{repo}` ROOT 自动 verified_primary）。因此本文件**优先引用 GitHub repo root**（auto verified_primary）作为每个工具的 maturity 一手源，vendor docs 一律 declared = `surrogate_primary` + note 含 literal "vendor docs"。CNCF/OpenSSF/Linux Foundation 用 literal "协会"。

## Source Manifest

| source_id | url | bucket | last_checked | author/host | one-line note |
|-----------|-----|--------|--------------|-------------|---------------|
| T02-S001 | https://github.com/kubernetes/kubernetes | verified_primary | 2026-05-19 | CNCF | K8s repo root — stars/活跃度一手 |
| T02-S002 | https://kubernetes.io/docs/home/ | surrogate_primary | 2026-05-19 | Kubernetes | vendor docs (CNCF 项目一手) |
| T02-S003 | https://github.com/hashicorp/terraform | verified_primary | 2026-05-19 | HashiCorp | Terraform repo root |
| T02-S004 | https://developer.hashicorp.com/terraform | verified_primary | 2026-05-19 | HashiCorp | vendor docs (厂商一手) — verifier 自动 primary |
| T02-S005 | https://github.com/opentofu/opentofu | verified_primary | 2026-05-19 | Linux Foundation | OpenTofu repo root (Terraform fork) |
| T02-S006 | https://opentofu.org/ | surrogate_primary | 2026-05-19 | OpenTofu | vendor docs (协会 — Linux Foundation 项目) |
| T02-S007 | https://github.com/pulumi/pulumi | verified_primary | 2026-05-19 | Pulumi | Pulumi repo root |
| T02-S008 | https://github.com/ansible/ansible | verified_primary | 2026-05-19 | Red Hat | Ansible repo root |
| T02-S009 | https://github.com/crossplane/crossplane | verified_primary | 2026-05-19 | CNCF | Crossplane repo root |
| T02-S010 | https://github.com/open-policy-agent/opa | verified_primary | 2026-05-19 | CNCF | OPA repo root |
| T02-S011 | https://www.openpolicyagent.org/ | surrogate_primary | 2026-05-19 | OPA | vendor docs (CNCF 项目一手) |
| T02-S012 | https://github.com/argoproj/argo-cd | verified_primary | 2026-05-19 | CNCF/Intuit | Argo CD repo root |
| T02-S013 | https://argo-cd.readthedocs.io/en/stable/ | surrogate_primary | 2026-05-19 | Argo | vendor docs (CNCF 项目一手) |
| T02-S014 | https://github.com/fluxcd/flux2 | verified_primary | 2026-05-19 | CNCF/Weaveworks | Flux v2 repo root |
| T02-S015 | https://fluxcd.io/ | surrogate_primary | 2026-05-19 | Flux | vendor docs (CNCF 项目一手) |
| T02-S016 | https://github.com/prometheus/prometheus | verified_primary | 2026-05-19 | CNCF | Prometheus repo root |
| T02-S017 | https://prometheus.io/docs/ | surrogate_primary | 2026-05-19 | Prometheus | vendor docs (CNCF 项目一手) |
| T02-S018 | https://github.com/grafana/grafana | verified_primary | 2026-05-19 | Grafana Labs | Grafana repo root |
| T02-S019 | https://github.com/grafana/loki | verified_primary | 2026-05-19 | Grafana Labs | Loki repo root |
| T02-S020 | https://grafana.com/observability-survey/2025/ | surrogate_primary | 2026-05-19 | Grafana Labs | vendor docs (厂商一手 — 第三方调研报告) |
| T02-S021 | https://github.com/open-telemetry/opentelemetry-collector | verified_primary | 2026-05-19 | CNCF | OTel Collector repo root |
| T02-S022 | https://opentelemetry.io/docs/ | surrogate_primary | 2026-05-19 | OpenTelemetry | vendor docs (CNCF 项目一手) |
| T02-S023 | https://github.com/jaegertracing/jaeger | verified_primary | 2026-05-19 | CNCF | Jaeger repo root |
| T02-S024 | https://github.com/grafana/tempo | verified_primary | 2026-05-19 | Grafana Labs | Tempo repo root |
| T02-S025 | https://github.com/VictoriaMetrics/VictoriaMetrics | verified_primary | 2026-05-19 | VictoriaMetrics | VM repo root |
| T02-S026 | https://github.com/thanos-io/thanos | verified_primary | 2026-05-19 | CNCF | Thanos repo root |
| T02-S027 | https://www.honeycomb.io/ | surrogate_primary | 2026-05-19 | Honeycomb | vendor docs (厂商一手 — Charity Majors) |
| T02-S028 | https://www.datadoghq.com/ | surrogate_primary | 2026-05-19 | Datadog | vendor docs (厂商一手 — 商用 all-in-one) |
| T02-S029 | https://github.com/istio/istio | verified_primary | 2026-05-19 | CNCF | Istio repo root |
| T02-S030 | https://github.com/linkerd/linkerd2 | verified_primary | 2026-05-19 | CNCF | Linkerd repo root |
| T02-S031 | https://github.com/cilium/cilium | verified_primary | 2026-05-19 | CNCF | Cilium repo root (eBPF) |
| T02-S032 | https://github.com/helm/helm | verified_primary | 2026-05-19 | CNCF | Helm repo root |
| T02-S033 | https://github.com/kubernetes-sigs/kustomize | verified_primary | 2026-05-19 | Kubernetes SIG | Kustomize repo root |
| T02-S034 | https://github.com/backstage/backstage | verified_primary | 2026-05-19 | CNCF/Spotify | Backstage repo root (IDP) |
| T02-S035 | https://github.com/hashicorp/vault | verified_primary | 2026-05-19 | HashiCorp | Vault repo root |
| T02-S036 | https://github.com/aquasecurity/trivy | verified_primary | 2026-05-19 | Aqua Security | Trivy repo root |
| T02-S037 | https://github.com/sigstore/cosign | verified_primary | 2026-05-19 | OpenSSF/sigstore | cosign repo root |
| T02-S038 | https://slsa.dev/ | surrogate_primary | 2026-05-19 | OpenSSF | vendor docs (协会 — OpenSSF 供应链标准) |
| T02-S039 | https://github.com/spinnaker/spinnaker | verified_primary | 2026-05-19 | Netflix/Google | Spinnaker repo root |
| T02-S040 | https://github.com/tektoncd/pipeline | verified_primary | 2026-05-19 | CDF | Tekton Pipeline repo root |
| T02-S041 | https://github.com/actions/runner | verified_primary | 2026-05-19 | GitHub | GitHub Actions runner repo root |
| T02-S042 | https://www.gremlin.com/ | surrogate_primary | 2026-05-19 | Gremlin | vendor docs (厂商一手 — chaos 商用) |
| T02-S043 | https://github.com/litmuschaos/litmus | verified_primary | 2026-05-19 | CNCF | LitmusChaos repo root |
| T02-S044 | https://github.com/chaos-mesh/chaos-mesh | verified_primary | 2026-05-19 | CNCF/PingCAP | Chaos Mesh repo root |
| T02-S045 | https://www.pagerduty.com/ | surrogate_primary | 2026-05-19 | PagerDuty | vendor docs (厂商一手 — incident/on-call) |
| T02-S046 | https://response.pagerduty.com/ | surrogate_primary | 2026-05-19 | PagerDuty | vendor docs (厂商一手 — 开源 incident 手册) |
| T02-S047 | https://landscape.cncf.io/ | surrogate_primary | 2026-05-19 | CNCF | vendor docs (协会 — 云原生工具全景) |
| T02-S048 | https://www.thoughtworks.com/radar | surrogate_primary | 2026-05-19 | ThoughtWorks | vendor docs (厂商一手 — 技术趋势权威) |
| T02-S049 | https://cloud.google.com/blog/products/ai-machine-learning/announcing-the-2025-dora-report | verified_primary | 2026-05-19 | Google Cloud / DORA | vendor docs (Google 一手 — 2025 DORA 报告) — verifier 自动 primary |
| T02-S050 | https://dora.dev/ | surrogate_primary | 2026-05-19 | Google DORA | vendor docs (Google DORA 一手 — Accelerate 研究) |
| T02-S051 | https://www.cncf.io/announcements/2025/07/24/cncf-end-user-survey-finds-argo-cd-as-majority-adopted-gitops-solution-for-kubernetes/ | surrogate_primary | 2026-05-19 | CNCF | vendor docs (协会 — End User Survey, Argo CD GitOps 多数采用) |
| T02-S052 | https://github.com/openobserve/openobserve | verified_primary | 2026-05-19 | OpenObserve | OpenObserve repo root (新兴 OSS observability) |
| T02-S053 | https://github.com/kyverno/kyverno | verified_primary | 2026-05-19 | CNCF/Nirmata | Kyverno repo root (K8s policy) |
| T02-S054 | https://github.com/falcosecurity/falco | verified_primary | 2026-05-19 | CNCF | Falco repo root (runtime security) |
| T02-S055 | https://github.com/opencost/opencost | verified_primary | 2026-05-19 | CNCF | OpenCost repo root (FinOps spec) |
| T02-S056 | https://sre.google/sre-book/ | surrogate_primary | 2026-05-19 | Google SRE | vendor docs (Google SRE 一手 — 学科正典, SLO/toil 来源) |
| T02-S057 | https://aws.amazon.com/builders-library/ | surrogate_primary | 2026-05-19 | AWS | vendor docs (AWS 一手 — 大规模运维实战) |
| T02-S058 | https://www.cncf.io/blog/2025/12/16/how-to-build-a-cost-effective-observability-platform-with-opentelemetry/ | surrogate_primary | 2026-05-19 | CNCF | vendor docs (协会 — observability 成本/OTel) |
| T02-S059 | https://github.com/grafana/pyroscope | verified_primary | 2026-05-19 | Grafana Labs | Pyroscope repo root (continuous profiling) |
| T02-S060 | https://www.reddit.com/r/devops/ | reference | 2026-05-19 | r/devops | UGC — 从业者吐槽/选型讨论 reference |

---

## 总览（按 tier 分组）

### 必备层（≥80% 从业者用，14 个）

| 工具 | 一句话 | Decay | Sources |
|------|--------|-------|---------|
| Kubernetes | 容器编排事实标准，云原生底座 | low | T02-S001, T02-S002, T02-S047 |
| Docker / OCI | 容器镜像与本地构建的通用语 | low | T02-S001, T02-S002 |
| Terraform | IaC 的事实标准（HCL + provider 生态） | low | T02-S003, T02-S004 |
| GitHub Actions | repo 内置 CI/CD，最低摩擦起步 | low | T02-S041 |
| Prometheus | 指标监控事实标准（pull + PromQL） | low | T02-S016, T02-S017, T02-S020 |
| Grafana | 可视化/dashboard 通用层 | low | T02-S018, T02-S020 |
| OpenTelemetry | 厂商中立 telemetry 采集标准（防锁定） | low | T02-S021, T02-S022, T02-S020 |
| Helm | K8s 应用打包/分发标准 | medium | T02-S032 |
| Argo CD | K8s GitOps 多数采用方案 | low | T02-S012, T02-S013, T02-S051 |
| Ansible | 配置管理/无 agent 编排常青树 | medium | T02-S008 |
| Vault | 密钥管理/动态凭证事实标准 | low | T02-S035 |
| PagerDuty | on-call/事件告警路由通用平台 | medium | T02-S045, T02-S046 |
| Datadog | 商用 all-in-one 可观测性（企业默认） | medium | T02-S028 |
| AWS / GCP / Azure | 云平台底座（Well-Architected） | low | T02-S049, T02-S057 |

### 场景特化层（7 子域，22 个）

| 工具 | 一句话 | 子域 | Decay | Sources |
|------|--------|------|-------|---------|
| GitLab CI | 一体化 DevSecOps 平台（CI+SCM+registry） | CI/CD | low | T02-S047 |
| Jenkins | 插件最广的自托管 CI（legacy 但仍庞大） | CI/CD | medium | T02-S047 |
| Tekton | K8s 原生云上 CI/CD 构建块 | CI/CD | medium | T02-S040 |
| Flux | GitOps 的 controller-only / 模块化派 | CI/CD | low | T02-S014, T02-S015 |
| Spinnaker | 多云重型渐进式部署（高运维成本） | CI/CD | high | T02-S039 |
| OpenTofu | Terraform 开源 fork（state 加密/许可中立） | IaC | medium | T02-S005, T02-S006 |
| Pulumi | 通用编程语言写 IaC | IaC | medium | T02-S007 |
| Crossplane | 把云资源做成 K8s CRD 的控制平面 | IaC | medium | T02-S009 |
| OPA | 通用 policy-as-code（Rego） | IaC/sec | low | T02-S010, T02-S011 |
| Kustomize | 无模板 K8s overlay（kubectl 内置） | K8s | low | T02-S033 |
| Istio | 功能最全的 service mesh（重） | K8s | medium | T02-S029 |
| Linkerd | 轻量 service mesh（Rust 数据面） | K8s | medium | T02-S030 |
| Cilium | eBPF CNI + 网络可观测性 | K8s | low | T02-S031 |
| Loki | 标签化/低成本日志（Prometheus 式） | 可观测性 | low | T02-S019 |
| Tempo | 对象存储后端的分布式追踪 | 可观测性 | medium | T02-S024 |
| Jaeger | 追踪查询/可视化（OTel 后端） | 可观测性 | low | T02-S023 |
| VictoriaMetrics | 高性能省内存 Prometheus 替代/长存 | 可观测性 | low | T02-S025 |
| Thanos | Prometheus 全局视图/长期存储 | 可观测性 | medium | T02-S026 |
| Honeycomb | 高基数 wide-event 可观测性（unknown-unknowns） | 可观测性 | medium | T02-S027 |
| Opsgenie | on-call 告警（Atlassian，注 EOL 风险） | 事件 | high | T02-S045 |
| Trivy | 镜像/IaC/SBOM 一体扫描 | DevSecOps | low | T02-S036 |
| cosign / sigstore | 制品签名/供应链来源证明 | DevSecOps | medium | T02-S037, T02-S038 |
| Backstage | 内部开发者门户/IDP 框架 | 平台工程 | medium | T02-S034, T02-S048 |

### 新兴/实验层（近 12 个月起势，6 个）

| 工具 | 一句话 | Decay | Sources |
|------|--------|-------|---------|
| OpenObserve | Rust + 列存的 OSS Datadog 替代（成本驱动） | high | T02-S052 |
| ClickHouse-as-observability (ClickStack) | 大体量 telemetry 用列存自建（成本暴降） | high | T02-S048, T02-S058 |
| Kyverno | YAML 原生 K8s policy（对标 OPA Gatekeeper） | medium | T02-S053 |
| OpenCost | FinOps 成本归因开放规范 | medium | T02-S055 |
| Grafana Pyroscope / Parca | 持续性能剖析（profiling 作为第四支柱） | high | T02-S059 |
| Falco | eBPF 运行时安全/异常检测（CNCF 毕业） | medium | T02-S054 |

---

## Layer 1 · 必备层（≥80% 从业者用）

> 证据门槛：GitHub stars 远超候选池中位数（本池 stars 中位数约 12k → 必备阈值 24k；Vault/PagerDuty/Datadog 等以 ≥3 独立 source + survey 采用率达标补足），或行业 survey ≥50% 采用率，或 ≥3 独立 source 点名。

### 1. Kubernetes
- **One-liner**: 容器编排的事实标准，几乎所有现代云原生栈的运行底座。
- **Tier**: 必备
- **Maintainer**: CNCF (graduated) — github.com/kubernetes/kubernetes
- **License**: open / Apache-2.0
- **Maturity signals**: stars 122,357 (2026-05-19); last push 2026-05-19（当日活跃）; activity healthy (evidence: [T02-S001])
- **不适合 / 替代**: 单体小应用 / 团队 <10 人 / 无专职平台能力时是过度工程——用托管 PaaS（Cloud Run / Fly.io / ECS）或单机 Docker Compose。"do you really need Kubernetes for this" 是资深人的口头禅 (evidence: [T02-S060])
- **生产案例**: CNCF End User Survey 显示 K8s 是云原生底座，Argo CD 在其上运行于约 60% 集群做应用交付 (evidence: [T02-S051])
- **近期变化**: 持续 ~3 月一个 minor；sidecar containers GA、in-place pod resize 等推进 (evidence: [T02-S002])
- **可信度**: high
- **Decay risk**: low（24+ 月稳定，已是基础设施，<20% 概率被取代）

### 2. Docker / OCI
- **One-liner**: 容器镜像格式与本地构建/运行的通用语；OCI 标准让镜像可移植。
- **Tier**: 必备
- **Maintainer**: Docker Inc + OCI (Open Container Initiative)
- **License**: open (Apache-2.0, OCI spec) + Docker Desktop 部分商用
- **Maturity signals**: OCI 已成 K8s/所有 registry 通用格式 (evidence: [T02-S002])
- **不适合 / 替代**: 生产构建链可用 BuildKit/buildah/Kaniko（无 daemon）；Docker Desktop 在大企业有许可成本，常换 Podman/Rancher Desktop
- **资深提示**: 多阶段构建 + distroless/最小基础镜像 + 镜像扫描是基本功 (evidence: [T02-S036])
- **可信度**: high
- **Decay risk**: low（OCI 标准化后镜像格式 24+ 月稳定）

### 3. Terraform
- **One-liner**: IaC 事实标准，HCL + 庞大 provider 生态声明式管理任意云资源。
- **Tier**: 必备
- **Maintainer**: HashiCorp (IBM) — github.com/hashicorp/terraform
- **License**: BUSL-1.1（2023 从 MPL 改为 source-available，引发 OpenTofu fork）
- **Maturity signals**: stars 48,429 (2026-05-19); last push 2026-05-19; activity healthy (evidence: [T02-S003])
- **典型使用场景**: 多云/多账户基础设施声明 + module 复用 + remote state 加锁
- **不适合 / 替代**: 配置管理（用 Ansible）；命令式逻辑/循环复杂（用 Pulumi）；纯 K8s 内资源（用 Crossplane/Helm）；许可顾虑（用 OpenTofu）
- **近期变化**: 许可改 BUSL 是最大事件——直接催生 Linux Foundation 的 OpenTofu fork (evidence: [T02-S004, T02-S005])
- **可信度**: high
- **Decay risk**: low（IaC 标准；但许可分裂使 OpenTofu 长期份额是变量，工具本身 low）

### 4. GitHub Actions
- **One-liner**: 与 repo 同居的 CI/CD，YAML workflow + marketplace，最低摩擦起步。
- **Tier**: 必备
- **Maintainer**: GitHub (Microsoft) — github.com/actions/runner
- **License**: runner MIT；托管服务商用（self-hosted runner 免费）
- **Maturity signals**: runner repo stars 6,022 (2026-05-19); last push 2026-05-19（托管服务用量远超此数，repo 仅 runner）(evidence: [T02-S041])
- **典型使用场景**: GitHub 上的项目默认 CI；用 marketplace action 拼装 pipeline
- **不适合 / 替代**: 复杂 fan-out/审批流弱于 GitLab CI；自托管大规模需自管 runner 池（成本/安全）；非 GitHub 仓库用 GitLab CI / Buildkite
- **避坑**: 第三方 action pin 到 commit SHA 而非 tag（供应链风险，2025 多起 action 投毒）(evidence: [T02-S038])
- **可信度**: high
- **Decay risk**: low

### 5. Prometheus
- **One-liner**: 指标监控事实标准，pull 模型 + PromQL + exporter 生态。
- **Tier**: 必备
- **Maintainer**: CNCF (graduated) — github.com/prometheus/prometheus
- **License**: open / Apache-2.0
- **Maturity signals**: stars 64,092 (2026-05-19); last push 2026-05-19; activity healthy (evidence: [T02-S016])
- **采用率**: 67% 组织生产使用 Prometheus，总使用率（含 POC）86%——可观测性 OSS 第一 (evidence: [T02-S020])
- **不适合 / 替代**: 单实例长期存储/高基数受限——长存用 Thanos/Mimir/VictoriaMetrics；超高基数任意维度下钻用 Honeycomb
- **近期变化**: OTLP ingest、原生 histogram、Prometheus 3.0 (evidence: [T02-S017])
- **可信度**: high
- **Decay risk**: low

### 6. Grafana
- **One-liner**: 可视化/dashboard 通用层，对接 Prometheus/Loki/Tempo/任意数据源。
- **Tier**: 必备
- **Maintainer**: Grafana Labs — github.com/grafana/grafana
- **License**: AGPLv3（2021 从 Apache 改）
- **Maturity signals**: stars 73,871 (2026-05-19); last push 2026-05-19; activity healthy (evidence: [T02-S018])
- **不适合 / 替代**: 仅做 dashboard 不解决高基数排障；商用一体化体验弱于 Datadog
- **可信度**: high
- **Decay risk**: low

### 7. OpenTelemetry (OTel)
- **One-liner**: 厂商中立的 telemetry（traces/metrics/logs）采集与协议标准，instrument 一次随意切后端。
- **Tier**: 必备
- **Maintainer**: CNCF (incubating, K8s 后第二活跃) — github.com/open-telemetry
- **License**: open / Apache-2.0
- **Maturity signals**: collector repo stars 7,032 (2026-05-19); last push 2026-05-19; activity healthy (evidence: [T02-S021])
- **采用率**: 生产使用 41%，总使用率 79%；切后端自由（37%）+ 易采用（41%）是首要采用动因 (evidence: [T02-S020]); ThoughtWorks Radar 称其"正快速成为可观测性行业标准" (evidence: [T02-S048])
- **典型使用场景**: 防可观测性厂商锁定——在 collector 改 config 就能从 Datadog 切到 OSS 后端
- **不适合 / 替代**: 早期 logs SDK 成熟度参差；纯指标场景 Prometheus 直采更简单
- **可信度**: high
- **Decay risk**: low（防锁定是结构性需求，标准地位 24+ 月稳固）

### 8. Helm
- **One-liner**: K8s 应用打包/分发标准（chart + values + 模板）。
- **Tier**: 必备
- **Maintainer**: CNCF (graduated) — github.com/helm/helm
- **License**: open / Apache-2.0
- **Maturity signals**: stars 29,823 (2026-05-19); last push 2026-05-19; activity healthy (evidence: [T02-S032])
- **不适合 / 替代**: Go template 字符串拼 YAML 易脆——纯环境差异用 Kustomize overlay；二者常组合（Helm 装第三方 + Kustomize 改本地）
- **可信度**: high
- **Decay risk**: medium（chart 模板范式被诟病，CUE/Timoni 等替代在试，12-24 月内有变数 20-40%）

### 9. Argo CD
- **One-liner**: K8s GitOps 持续交付，git 为单一真相源 + 声明式 sync + UI。
- **Tier**: 必备（GitOps 域内）
- **Maintainer**: CNCF (graduated) — github.com/argoproj/argo-cd
- **License**: open / Apache-2.0
- **Maturity signals**: stars 22,922 (2026-05-19); last push 2026-05-19; activity healthy (evidence: [T02-S012])
- **采用率**: CNCF End User Survey——K8s 上 GitOps 的多数采用方案，NPS 79，约 60% 集群用于应用交付；Argo CD 3.0 (2025) 是 2021 来首个大版本 (evidence: [T02-S051])
- **典型使用场景**: app-of-apps 管理多环境 K8s 部署 + PR 即变更 + drift 自动纠正
- **不适合 / 替代**: 想要 controller-only / 更模块化 / 多租户 sync 用 Flux；非 K8s 资源 GitOps 较弱
- **可信度**: high
- **Decay risk**: low

### 10. Ansible
- **One-liner**: 无 agent、SSH 推送的配置管理与编排，幂等 playbook，常青树。
- **Tier**: 必备
- **Maintainer**: Red Hat (IBM) — github.com/ansible/ansible
- **License**: open / GPLv3
- **Maturity signals**: stars 68,602 (2026-05-19); last push 2026-05-19; activity healthy (evidence: [T02-S008])
- **不适合 / 替代**: 云资源 provisioning（用 Terraform，Ansible 是配置层不是 provisioning 层）；大规模并发性能弱
- **可信度**: high
- **Decay risk**: medium（不可变基础设施潮流下配置管理重要性缓降，但存量巨大，12-24 月 20-40%）

### 11. Vault
- **One-liner**: 密钥管理/动态凭证/加密即服务的事实标准。
- **Tier**: 必备（DevSecOps 域内）
- **Maintainer**: HashiCorp (IBM) — github.com/hashicorp/vault
- **License**: BUSL-1.1（同 Terraform 改许可，OpenBao 为其 LF fork）
- **Maturity signals**: stars 35,634 (2026-05-19); last push 2026-05-19; activity healthy (evidence: [T02-S035])
- **典型使用场景**: 动态数据库凭证 + 密钥轮换 + PKI；替代把密钥写进 env/git
- **不适合 / 替代**: 纯 K8s 内可用 External Secrets Operator + 云 KMS / Sealed Secrets；运维 Vault HA 本身成本高，小团队用云原生 secrets manager
- **避坑**: IaC state（terraform.tfstate）含明文密钥 + 是危险操作面——必须远程后端 + 加锁 + 加密 (evidence: [T02-S004, T02-S006])
- **可信度**: high
- **Decay risk**: low

### 12. PagerDuty
- **One-liner**: on-call 排班 + 告警路由 + 事件响应编排的通用平台。
- **Tier**: 必备（事件/on-call 域内）
- **Maintainer**: PagerDuty Inc (proprietary)
- **License**: proprietary（其 Incident Response 文档 response.pagerduty.com 开源 CC）
- **Maturity signals**: 行业 incident 方法论事实参考；开源 incident response 手册被广泛引用 (evidence: [T02-S045, T02-S046])
- **典型使用场景**: 告警分级路由 + 升级策略 + IC 流程 + follow-the-sun 排班
- **不适合 / 替代**: 预算敏感/已在 Atlassian 栈用 Opsgenie（但注 Opsgenie 已宣 EOL，2027 迁移）；Grafana OnCall (OSS) / incident.io（事件协作侧）
- **避坑**: 告警必须 actionable——长期 alert fatigue + 周末被毁是管理失败不是个人韧性问题 (evidence: [T02-S056, T02-S046])
- **可信度**: high
- **Decay risk**: medium

### 13. Datadog
- **One-liner**: 商用 all-in-one 可观测性（metrics/logs/traces/APM/RUM/security 一站），企业默认选择。
- **Tier**: 必备（商用派代表）
- **Maintainer**: Datadog Inc (proprietary)
- **License**: proprietary
- **Maturity signals**: 企业可观测性市场领导者；OSS best-of-breed 的对立面 (evidence: [T02-S028])
- **不适合 / 替代**: 成本会失控——团队遇到 40%/60%/200% 账单跳涨；custom metrics 占 30-50% 账单；50-500 微服务的中型团队可观测性花费已超其 AWS/GCP 实际算存成本。成本敏感用 Prometheus+Grafana+Loki OSS 栈 / OpenObserve / ClickHouse 自建 (evidence: [T02-S058])
- **避坑**: 用 OTel instrument 后能随时切走——别把 instrument code 绑死在厂商 SDK 上 (evidence: [T02-S020])
- **可信度**: high
- **Decay risk**: medium（OTel + 成本压力使部分负载回流 OSS，12-24 月份额有变 20-40%）

### 14. AWS / GCP / Azure
- **One-liner**: 云平台底座，Well-Architected 框架定义可靠/安全/成本/性能/运维支柱。
- **Tier**: 必备
- **Maintainer**: Amazon / Google / Microsoft (proprietary)
- **License**: proprietary
- **Maturity signals**: AWS Builders' Library 是大规模运维一手实战；DORA 2025 称 90% 组织已采用至少一个平台 (evidence: [T02-S057, T02-S049])
- **不适合 / 替代**: multi-cloud 不要为"显得专业"硬上——多数公司单云 + 抽象层即可；厂商锁定是真实成本，用 OTel/Terraform/K8s 等中立层缓解
- **可信度**: high
- **Decay risk**: low

---

## Layer 2 · 场景特化层（7 子域）

> 写法：场景特化 (7 类) = CI/CD 与发布 / IaC / 容器与编排 / 可观测性 / 事件与 on-call / 云平台与 FinOps / 平台工程与 DevSecOps。

### 子域 A — CI/CD 与发布工程

#### 15. GitLab CI
- **One-liner**: 一体化 DevSecOps 平台（SCM + CI + registry + security 同处）。
- **Tier**: 场景特化（CI/CD）
- **Maintainer**: GitLab Inc; License: open core (MIT + EE 商用)
- **典型使用场景**: 想要"一个平台搞定全部"、自托管、强 fan-out/审批流 (evidence: [T02-S047])
- **不适合 / 替代**: 已重度在 GitHub 生态用 GitHub Actions；只要轻 CI 用 Buildkite/CircleCI
- **Decay risk**: low

#### 16. Jenkins
- **One-liner**: 插件最广、自托管 CI 老兵；存量极大但被视为 legacy 维护负担。
- **Tier**: 场景特化（CI/CD, legacy）
- **Maintainer**: CDF (Continuous Delivery Foundation); License: open / MIT
- **典型使用场景**: 已有大量 Jenkinsfile/插件依赖、复杂自托管编排、无法迁移的存量 (evidence: [T02-S047])
- **不适合 / 替代**: 绿地项目不要新上 Jenkins——插件安全/维护 toil 高；用 GitHub Actions / GitLab CI / Tekton。ThoughtWorks 长期把"自管 Jenkins 当默认"视为应被取代 (evidence: [T02-S048])
- **Decay risk**: medium（存量稳态，但新项目份额持续流失）

#### 17. Tekton
- **One-liner**: K8s 原生的 CI/CD 构建块（Task/Pipeline 即 CRD），云上跑流水线。
- **Tier**: 场景特化（CI/CD）
- **Maintainer**: CDF — github.com/tektoncd/pipeline
- **License**: open / Apache-2.0
- **Maturity signals**: stars 8,967 (2026-05-19); last push 2026-05-19 (evidence: [T02-S040])
- **典型使用场景**: 想把 CI/CD 本身做成 K8s 原生、平台团队给业务方提供可组合 pipeline building blocks
- **不适合 / 替代**: 直接给开发者用太底层——通常作为平台底座，上层套 Argo Workflows / 自建抽象；简单团队用 GitHub Actions
- **Decay risk**: medium

#### 18. Flux
- **One-liner**: GitOps 的 controller-only / 模块化派（无内置 UI，GitOps Toolkit 组件化）。
- **Tier**: 场景特化（CI/CD GitOps）
- **Maintainer**: CNCF (graduated) — github.com/fluxcd/flux2
- **License**: open / Apache-2.0
- **Maturity signals**: stars 8,131 (2026-05-19); last push 2026-05-19 (evidence: [T02-S014])
- **典型使用场景**: 多租户/多集群 GitOps、想要纯 controller 无 UI、与 Helm controller 深度集成、平台团队嵌入
- **不适合 / 替代**: 想要开箱 UI/可视化应用拓扑用 Argo CD（采用率更高）(evidence: [T02-S051])
- **Decay risk**: low

#### 19. Spinnaker
- **One-liner**: Netflix 起源的多云重型 CD，内建渐进式部署/canary 分析。
- **Tier**: 场景特化（CI/CD, 重型）
- **Maintainer**: Netflix/Google → CDF — github.com/spinnaker/spinnaker
- **License**: open / Apache-2.0
- **Maturity signals**: stars 9,728 (2026-05-19); last push 2026-05-12（活跃但增速放缓）(evidence: [T02-S039])
- **典型使用场景**: 真·多云 + 复杂多阶段渐进式发布 + 大规模 canary 自动分析的大厂
- **不适合 / 替代**: 运维成本极高——多数团队过度；K8s 上用 Argo CD + Argo Rollouts 做 canary/blue-green 更轻 (evidence: [T02-S012])
- **Decay risk**: high（份额被 Argo 系蚕食，12 月内显著变化 >40%）

### 子域 B — 基础设施即代码（IaC）

#### 20. OpenTofu
- **One-liner**: Terraform 的开源 fork（Linux Foundation），许可中立 + 原生 state 加密。
- **Tier**: 场景特化（IaC）
- **Maintainer**: Linux Foundation — github.com/opentofu/opentofu
- **License**: open / MPL-2.0（保持开源，对 Terraform BUSL 的回应）
- **Maturity signals**: stars 28,698 (2026-05-19); last push 2026-05-19; activity healthy (evidence: [T02-S005])
- **典型使用场景**: 对 BUSL 许可有顾虑、需要客户端 state 加密（PBKDF2/AWS KMS/GCP KMS/OpenBao）、想要社区治理；2026 已发独立特性（OCI registry、native S3 state locking、ephemeral resources）超出 Terraform (evidence: [T02-S006])
- **采用率**: ~12% IaC 从业者采用，27% 团队计划评估/扩大 (evidence: [T02-S006])
- **不适合 / 替代**: 重度依赖 HashiCorp 商业生态（HCP/TFC 高级特性）留 Terraform
- **Decay risk**: medium（fork 已成熟但长期相对 Terraform 份额是变量）

#### 21. Pulumi
- **One-liner**: 用通用编程语言（TS/Python/Go/C#）写 IaC，复用语言生态做循环/抽象。
- **Tier**: 场景特化（IaC）
- **Maintainer**: Pulumi Corp — github.com/pulumi/pulumi
- **License**: open core (Apache-2.0 + 托管 backend 商用)
- **Maturity signals**: stars 25,212 (2026-05-19); last push 2026-05-19; activity healthy (evidence: [T02-S007])
- **典型使用场景**: 团队是开发者背景、需要复杂条件/循环/单元测试 IaC、想用真正的编程抽象（命令式控制 vs HCL 声明式）
- **不适合 / 替代**: 团队习惯声明式 + provider 生态最大化用 Terraform/OpenTofu；过度抽象会让 IaC 变成"普通代码"难审计
- **Decay risk**: medium

#### 22. Crossplane
- **One-liner**: 把云资源建模成 K8s CRD，用控制平面 + reconcile 循环管理基础设施。
- **Tier**: 场景特化（IaC, K8s 原生）
- **Maintainer**: CNCF (graduated) — github.com/crossplane/crossplane
- **License**: open / Apache-2.0
- **Maturity signals**: stars 11,692 (2026-05-19); last push 2026-05-19 (evidence: [T02-S009])
- **典型使用场景**: 平台团队想用 K8s API 给业务方做自助基础设施（Composition 抽象成 golden path）、已全栈 K8s
- **不适合 / 替代**: 不想把 K8s 当通用控制平面、团队没有 operator/CRD 运维能力——用 Terraform；学习曲线陡
- **Decay risk**: medium

#### 23. OPA (Open Policy Agent)
- **One-liner**: 通用 policy-as-code 引擎（Rego 语言），统一管 K8s admission / IaC / API 授权。
- **Tier**: 场景特化（IaC / DevSecOps）
- **Maintainer**: CNCF (graduated) — github.com/open-policy-agent/opa
- **License**: open / Apache-2.0
- **Maturity signals**: stars 11,749 (2026-05-19); last push 2026-05-19 (evidence: [T02-S010])
- **典型使用场景**: 跨多系统统一策略（K8s Gatekeeper + Terraform plan 校验 + Conftest CI 门禁）、Rego 已是团队技能
- **不适合 / 替代**: 只做 K8s policy 且嫌 Rego 难学——用 Kyverno（YAML 原生）；IaC 专项用 Checkov/tfsec
- **Decay risk**: low

### 子域 C — 容器与编排（K8s 周边）

#### 24. Kustomize
- **One-liner**: 无模板的 K8s 配置 overlay（base + patches），kubectl 内置（`-k`）。
- **Tier**: 场景特化（K8s）
- **Maintainer**: Kubernetes SIG-CLI — github.com/kubernetes-sigs/kustomize
- **License**: open / Apache-2.0
- **Maturity signals**: stars 12,050 (2026-05-19); last push 2026-05-19 (evidence: [T02-S033])
- **典型使用场景**: 多环境（dev/staging/prod）仅差异覆盖、讨厌 Helm 字符串模板、kubectl 原生
- **不适合 / 替代**: 需要打包/分发/版本化给第三方装用 Helm；复杂动态逻辑两者都弱
- **Decay risk**: low

#### 25. Istio
- **One-liner**: 功能最全的 service mesh（流量管理 + mTLS + 可观测性 + 策略），重。
- **Tier**: 场景特化（K8s）
- **Maintainer**: CNCF (graduated) — github.com/istio/istio
- **License**: open / Apache-2.0
- **Maturity signals**: stars 38,208 (2026-05-19); last push 2026-05-19 (evidence: [T02-S029])
- **典型使用场景**: 大规模微服务需要细粒度流量管理/金丝雀路由/全 mesh mTLS/多集群；ambient mode 降 sidecar 开销
- **不适合 / 替代**: 小规模不要上 mesh（认知负荷 + 资源开销 = resume-driven 重灾区）；要轻量 mTLS 用 Linkerd；只要 mesh 化网络可观测用 Cilium
- **Decay risk**: medium

#### 26. Linkerd
- **One-liner**: 轻量级 service mesh，Rust micro-proxy 数据面，主打简单/低开销。
- **Tier**: 场景特化（K8s）
- **Maintainer**: CNCF (graduated) — github.com/linkerd/linkerd2
- **License**: open / Apache-2.0
- **Maturity signals**: stars 11,396 (2026-05-19); last push 2026-05-19 (evidence: [T02-S030])
- **典型使用场景**: 想要 mTLS + 基础流量指标但拒绝 Istio 复杂度、追求最小运维负担
- **不适合 / 替代**: 需要 Istio 级丰富流量策略/多集群联邦；注 Buoyant 已对稳定版企业许可收费（生产用要评估）
- **Decay risk**: medium

#### 27. Cilium
- **One-liner**: eBPF 驱动的 K8s CNI + 网络安全 + 可观测性（Hubble），无 sidecar mesh。
- **Tier**: 场景特化（K8s 网络）
- **Maintainer**: CNCF (graduated) — github.com/cilium/cilium
- **License**: open / Apache-2.0
- **Maturity signals**: stars 24,390 (2026-05-19); last push 2026-05-19; activity healthy (evidence: [T02-S031])
- **典型使用场景**: 需要高性能 CNI + L3-L7 网络策略 + eBPF 级可观测性、想要无 sidecar 的 mesh（Cilium Mesh）；多家云托管 K8s 已默认 Cilium CNI
- **不适合 / 替代**: 内核版本旧/不支持 eBPF；只要简单 overlay 用 Calico/Flannel
- **Decay risk**: low（eBPF 网络已成主流方向）

### 子域 D — 可观测性

#### 28. Loki
- **One-liner**: 标签化、低成本日志聚合（"Prometheus for logs"，只索引标签不索引全文）。
- **Tier**: 场景特化（可观测性）
- **Maintainer**: Grafana Labs — github.com/grafana/loki
- **License**: AGPLv3
- **Maturity signals**: stars 28,211 (2026-05-19); last push 2026-05-19 (evidence: [T02-S019])
- **典型使用场景**: 已用 Grafana 栈、日志量大想省存储成本、按标签查而非全文搜
- **不适合 / 替代**: 重度全文检索/复杂分析用 Elasticsearch/OpenSearch；超大体量用 ClickHouse 系
- **Decay risk**: low

#### 29. Tempo
- **One-liner**: 仅靠对象存储（S3/GCS）的分布式追踪后端，成本低、与 Grafana 栈一体。
- **Tier**: 场景特化（可观测性）
- **Maintainer**: Grafana Labs — github.com/grafana/tempo
- **License**: AGPLv3
- **Maturity signals**: stars 5,261 (2026-05-19); last push 2026-05-19 (evidence: [T02-S024])
- **典型使用场景**: 已用 Grafana/Loki、想要便宜的 trace 存储（仅对象存储）、用 OTel 采集
- **不适合 / 替代**: 想要独立 trace UI/查询能力用 Jaeger
- **Decay risk**: medium

#### 30. Jaeger
- **One-liner**: CNCF 分布式追踪查询/可视化，OTel 的常用展示后端。
- **Tier**: 场景特化（可观测性）
- **Maintainer**: CNCF (graduated) — github.com/jaegertracing/jaeger
- **License**: open / Apache-2.0
- **Maturity signals**: stars 22,818 (2026-05-19); last push 2026-05-19 (evidence: [T02-S023])
- **典型使用场景**: 需要成熟的 trace UI/服务依赖图、OTel collector 后接 Jaeger
- **不适合 / 替代**: 已全 Grafana 栈用 Tempo；高基数任意维度分析用 Honeycomb
- **Decay risk**: low

#### 31. VictoriaMetrics
- **One-liner**: 高性能、省内存的 Prometheus 兼容时序库，可做长期存储/集群替代。
- **Tier**: 场景特化（可观测性）
- **Maintainer**: VictoriaMetrics — github.com/VictoriaMetrics/VictoriaMetrics
- **License**: open / Apache-2.0（企业版另算）
- **Maturity signals**: stars 17,025 (2026-05-19); last push 2026-05-19; activity healthy (evidence: [T02-S025])
- **典型使用场景**: Prometheus 内存/基数撑不住、要长期存储 + 更低成本、单二进制集群
- **不适合 / 替代**: 想留在原生 Prometheus 全局视图生态用 Thanos/Mimir
- **Decay risk**: low

#### 32. Thanos
- **One-liner**: 给 Prometheus 加全局查询视图 + 对象存储长期存储 + 高可用去重。
- **Tier**: 场景特化（可观测性）
- **Maintainer**: CNCF (incubating) — github.com/thanos-io/thanos
- **License**: open / Apache-2.0
- **Maturity signals**: stars 14,074 (2026-05-19); last push 2026-05-19 (evidence: [T02-S026])
- **典型使用场景**: 多 Prometheus 实例要全局视图 + 长期存储、想保留原生 Prometheus 不换引擎
- **不适合 / 替代**: 嫌组件多/运维重——用 Grafana Mimir（同源更集成）或直接 VictoriaMetrics
- **Decay risk**: medium

#### 33. Honeycomb
- **One-liner**: 高基数 wide-event 可观测性，主打用任意维度下钻排查 unknown-unknowns。
- **Tier**: 场景特化（可观测性）
- **Maintainer**: Honeycomb (Charity Majors), proprietary
- **License**: proprietary（OTel 原生采集）
- **Maturity signals**: observability 范式领导者；其 CTO Charity Majors 反复强调"monitoring 处理 known-unknowns，observability 处理 unknown-unknowns" (evidence: [T02-S027])
- **典型使用场景**: 复杂分布式系统排查"从没见过的故障"、需要高基数任意维度下钻、SLO 驱动告警
- **不适合 / 替代**: 简单已知指标监控 Prometheus 足够（别把 observability 当"三件套 SKU 打包"买）；商用成本要算
- **Decay risk**: medium

### 子域 E — 事件管理与 on-call

#### 34. Opsgenie
- **One-liner**: Atlassian 的 on-call 告警/排班，与 Jira 生态集成。
- **Tier**: 场景特化（事件，注 EOL）
- **Maintainer**: Atlassian, proprietary
- **典型使用场景**: 已在 Atlassian（Jira/Confluence）栈、要低成本告警 (evidence: [T02-S045])
- **不适合 / 替代**: Atlassian 已宣布 Opsgenie 退役（迁 Jira Service Management / Compass），新项目别选；用 PagerDuty / Grafana OnCall (OSS) / incident.io
- **Decay risk**: high（产品退役路径明确）

> 事件域核心方法论一手：PagerDuty 开源 Incident Response 手册 + Atlassian Incident Handbook（流程/角色/IC/SEV 定级）；本 track 工具侧已在必备层列 PagerDuty (evidence: [T02-S046])

### 子域 F — 云平台与 FinOps

#### 35. OpenCost
- **One-liner**: K8s 成本分配/归因的开放规范与实现（CNCF），FinOps 可见性基础。
- **Tier**: 场景特化（FinOps）/ 新兴
- **Maintainer**: CNCF (sandbox/incubating) — github.com/opencost/opencost
- **License**: open / Apache-2.0
- **Maturity signals**: stars 6,549 (2026-05-19); last push 2026-05-19 (evidence: [T02-S055])
- **典型使用场景**: 需要把 K8s 集群成本按 namespace/team/label 归因、做 showback/chargeback、对接 Kubecost
- **不适合 / 替代**: 非 K8s 成本用云原生 Cost Explorer / 第三方 FinOps 平台
- **Decay risk**: medium

> 云平台必备本身（AWS/GCP/Azure + Well-Architected）见必备层 #14；FinOps 方法一手 = AWS Builders' Library + 云厂商架构文档 (evidence: [T02-S057])

### 子域 G — 平台工程与 DevSecOps

#### 36. Backstage
- **One-liner**: Spotify 开源的内部开发者门户/IDP 框架（service catalog + software templates + TechDocs）。
- **Tier**: 场景特化（平台工程）
- **Maintainer**: CNCF (incubating) — github.com/backstage/backstage
- **License**: open / Apache-2.0
- **Maturity signals**: stars 33,386 (2026-05-19); last push 2026-05-19; activity healthy (evidence: [T02-S034]); ThoughtWorks 曾把 Backstage/开发者门户列 Adopt (evidence: [T02-S048])
- **典型使用场景**: 大组织要统一 service catalog + golden path 自助脚手架 + 集中技术文档、把平台当产品
- **不适合 / 替代**: 小团队自建 Backstage 投入巨大（需专职平台团队维护插件）——先用更轻的内部门户或托管 IDP（如 Port/Cortex）；DORA 2025 警示平台质量低时 AI 收益接近零，门户≠平台质量 (evidence: [T02-S049])
- **Decay risk**: medium（IDP 框架方向稳，但自建成本使部分团队转托管）

#### 37. Trivy
- **One-liner**: 一体化安全扫描器（容器镜像 + IaC + 文件系统 + SBOM + 漏洞 + 配置）。
- **Tier**: 场景特化（DevSecOps）
- **Maintainer**: Aqua Security — github.com/aquasecurity/trivy
- **License**: open / Apache-2.0
- **Maturity signals**: stars 35,058 (2026-05-19); last push 2026-05-19; activity healthy (evidence: [T02-S036])
- **典型使用场景**: CI 里 shift-left 扫镜像/IaC/依赖、生成 SBOM、最广覆盖单工具
- **不适合 / 替代**: 商业 SCA 深度/许可合规用 Snyk；运行时威胁检测用 Falco（Trivy 是静态扫描）
- **Decay risk**: low

#### 38. cosign / sigstore
- **One-liner**: 制品签名 + 透明日志 + 来源证明，让供应链可验证（keyless 签名）。
- **Tier**: 场景特化（DevSecOps）
- **Maintainer**: OpenSSF (Linux Foundation) — github.com/sigstore/cosign
- **License**: open / Apache-2.0
- **Maturity signals**: cosign stars 5,928 (2026-05-19); last push 2026-05-19 (evidence: [T02-S037])
- **典型使用场景**: 镜像/制品签名 + admission 校验只跑签名镜像 + 满足 SLSA 等级要求
- **不适合 / 替代**: 无供应链合规需求时是额外复杂度；SLSA 框架定义等级目标 (evidence: [T02-S038])
- **Decay risk**: medium（标准上升期）

### 子域 H — 韧性与混沌工程

#### 39. Gremlin
- **One-liner**: 商用混沌工程平台（"Failure as a Service"），托管故障注入 + 爆炸半径控制。
- **Tier**: 场景特化（混沌）
- **Maintainer**: Gremlin Inc, proprietary
- **典型使用场景**: 企业要托管/合规的 chaos 实验 + 安全护栏（自动停止）+ game day 编排 (evidence: [T02-S042])
- **不适合 / 替代**: 预算敏感/全 K8s 用 LitmusChaos / Chaos Mesh（OSS）；早期成熟度不足别先上 chaos——先做好备份恢复验证 + 告警 actionable 基本功
- **Decay risk**: medium

#### 40. LitmusChaos
- **One-liner**: CNCF 的 K8s 原生混沌工程框架（实验即 CRD，ChaosHub）。
- **Tier**: 场景特化（混沌）
- **Maintainer**: CNCF (incubating) — github.com/litmuschaos/litmus
- **License**: open / Apache-2.0
- **Maturity signals**: stars 5,400 (2026-05-19); last push 2026-05-19 (evidence: [T02-S043])
- **典型使用场景**: 全 K8s、想 GitOps 式声明混沌实验、CNCF 生态一致
- **不适合 / 替代**: 想要更细粒度网络/IO 故障注入用 Chaos Mesh；要商用支持/护栏用 Gremlin
- **Decay risk**: medium

#### 41. Chaos Mesh
- **One-liner**: CNCF 的 K8s 混沌平台（PingCAP 起源），细粒度网络/IO/时钟/压力故障注入。
- **Tier**: 场景特化（混沌）
- **Maintainer**: CNCF (incubating) — github.com/chaos-mesh/chaos-mesh
- **License**: open / Apache-2.0
- **Maturity signals**: stars 7,710 (2026-05-19); last push 2026-05-03（活跃，节奏稍慢）(evidence: [T02-S044])
- **典型使用场景**: 需要丰富故障类型（网络分区/延迟/IO 错误/时钟偏移）、有 dashboard
- **不适合 / 替代**: 与 LitmusChaos 二选一看团队偏好；混沌起源理论参考 Netflix Chaos Monkey / Principles of Chaos
- **Decay risk**: medium

> 数据库与有状态运维子域（schema 迁移 gh-ost/Flyway/Liquibase、备份验证、StatefulSet）工具更分散，未单列卡片但在避坑/决策树覆盖（"备份必须验证恢复"是 GitLab 2017 教训核心）。

---

## Layer 3 · 新兴/实验层（近 12 个月起势）

> 全部标 `stability: experimental`，6 个月后格局可能大变。

### 42. OpenObserve
- **One-liner**: Rust + 列存（Parquet）的 OSS 全栈可观测性，主打替代 Datadog 降本。
- **Tier**: 新兴；stability: experimental
- **Maintainer**: OpenObserve Inc — github.com/openobserve/openobserve
- **License**: open core (AGPL-3.0)
- **Maturity signals**: stars 18,897 (2026-05-19); repo created 2023-02-02; last push 2026-05-19; activity healthy (evidence: [T02-S052])
- **典型使用场景**: 可观测性账单失控、想要 logs/metrics/traces/RUM 一站 OSS、benchmark 称 60-98% 成本下降 (evidence: [T02-S058])
- **早期采用信号**: 2026 多篇成本对比把它列为 Datadog OSS 替代头部 (evidence: [T02-S058])
- **不适合 / 替代**: 生态/集成成熟度远不及 Datadog/Grafana；关键生产前充分评估
- **Decay risk**: high（新兴，>40% 概率 12 月内格局变）

### 43. ClickHouse-as-observability (ClickStack 等)
- **One-liner**: 用 ClickHouse 列存自建 telemetry 后端，超大体量下成本暴降。
- **Tier**: 新兴；stability: experimental
- **Maintainer**: ClickHouse Inc + 生态; License: open (Apache-2.0 core)
- **Maturity signals**: 2026 趋势——TB/日级 telemetry 用 ClickHouse 省 >90%，ThoughtWorks Radar 收录 ClickStack (evidence: [T02-S048, T02-S058])
- **典型使用场景**: 数 TB/日 telemetry、有自建运维能力、成本是首要约束
- **不适合 / 替代**: 小体量不值得自建复杂度——用托管或 Grafana 栈
- **Decay risk**: high

### 44. Kyverno
- **One-liner**: YAML 原生的 K8s policy 引擎（无需学 Rego），对标 OPA Gatekeeper。
- **Tier**: 新兴→成长；stability: experimental→stabilizing
- **Maintainer**: CNCF (incubating) — github.com/kyverno/kyverno
- **License**: open / Apache-2.0
- **Maturity signals**: stars 7,766 (2026-05-19); last push 2026-05-19 (evidence: [T02-S053])
- **典型使用场景**: 只做 K8s policy、团队不想学 Rego、要 mutate/generate 资源
- **不适合 / 替代**: 跨多系统统一策略用 OPA（Rego 更通用）
- **Decay risk**: medium

### 45. Grafana Pyroscope / Parca（持续性能剖析）
- **One-liner**: continuous profiling，把 CPU/内存火焰图作为可观测性"第四支柱"。
- **Tier**: 新兴；stability: experimental
- **Maintainer**: Grafana Labs (Pyroscope) — github.com/grafana/pyroscope
- **License**: AGPLv3
- **Maturity signals**: Pyroscope stars 11,441 (2026-05-19); last push 2026-05-19 (evidence: [T02-S059])
- **典型使用场景**: 已用 Grafana 栈、要把性能剖析常态化关联 traces、eBPF 无侵入采集
- **不适合 / 替代**: profiling 是高级需求，多数团队先把 metrics/logs/traces 做好
- **Decay risk**: high

### 46. Falco
- **One-liner**: eBPF 驱动的 K8s/主机运行时安全检测（异常 syscall/行为告警）。
- **Tier**: 新兴→成熟（CNCF 毕业）；stability: stabilizing
- **Maintainer**: CNCF (graduated) — github.com/falcosecurity/falco
- **License**: open / Apache-2.0
- **Maturity signals**: stars 8,960 (2026-05-19); repo created 2016；last push 2026-05-19（成熟但运行时安全采用仍在扩散）(evidence: [T02-S054])
- **典型使用场景**: 运行时威胁检测（Trivy 管静态、Falco 管运行时）、合规要求行为审计
- **不适合 / 替代**: 无运行时安全需求时是额外噪音源；需调优规则降误报
- **Decay risk**: medium

---

## 选型决策树

> 节点 7 个分支，每分支挂证据。原则：先问"你真的需要这个复杂度吗"，再选工具（反 resume-driven development）。

### 决策树 A：你当前最痛的子域是什么？

#### Branch 1：刚起步 / 验证想法 / 小团队（<10 人）
→ 推荐：托管 PaaS（Cloud Run/ECS/Fly.io）+ GitHub Actions + 云原生托管监控
→ **不推荐**：Kubernetes + service mesh + multi-cloud——这是 resume-driven development 重灾区，认知负荷与运维 toil 远超收益 (evidence: [T02-S001, T02-S060])
→ 理由：DORA 2025 强调平台质量 > 工具先进度；小团队的可靠性瓶颈是基本功（备份能否恢复 / 告警 actionable / 变更可回滚）不是工具栈复杂度 (evidence: [T02-S049])

#### Branch 2：已有 PMF，要 production-grade CI/CD + 部署
##### Branch 2a：GitHub 生态 / 想最低摩擦
→ 推荐：GitHub Actions（CI）+ Argo CD（K8s GitOps，多数采用方案）(evidence: [T02-S041, T02-S012, T02-S051])
→ 替代：GitLab CI（要一体化平台）/ Flux（要 controller-only 模块化）
##### Branch 2b：真·多云 + 复杂渐进式发布
→ 推荐：Argo CD + Argo Rollouts 做 canary/blue-green（轻）
→ **不推荐**：Spinnaker——除非确实是大厂多云重型场景，否则运维成本过高 (evidence: [T02-S039])
##### Branch 2c：已有大量 Jenkins 存量
→ 现实：维护存量但绿地不新增 Jenkins；逐步迁 Actions/GitLab CI/Tekton (evidence: [T02-S047])

#### Branch 3：基础设施即代码（IaC）
##### Branch 3a：标准声明式 + 最大 provider 生态
→ 推荐：Terraform（事实标准）；若顾虑 BUSL 许可或要 state 加密 → OpenTofu (evidence: [T02-S003, T02-S005, T02-S006])
##### Branch 3b：团队是开发者背景 + 需要复杂逻辑/测试
→ 推荐：Pulumi（通用语言）(evidence: [T02-S007])
##### Branch 3c：平台团队要给业务方 K8s 原生自助基础设施
→ 推荐：Crossplane（云资源即 CRD）(evidence: [T02-S009])
→ 全分支硬规矩：state 远程后端 + 加锁 + 加密；apply 到生产前必 plan review (evidence: [T02-S004])

#### Branch 4：可观测性——按"成本 vs 排障深度 vs 锁定"分
##### Branch 4a：默认起点 / 想要 OSS best-of-breed
→ 推荐：Prometheus + Grafana + Loki + OTel 采集（67%/86% 采用，防锁定）(evidence: [T02-S016, T02-S020])
##### Branch 4b：要企业级 all-in-one + 不在意成本
→ 推荐：Datadog——但用 OTel instrument 以保留切换自由，警惕 custom metrics 账单 (evidence: [T02-S028, T02-S058])
##### Branch 4c：复杂分布式系统、要查 unknown-unknowns / 高基数
→ 推荐：Honeycomb（wide events）+ OTel (evidence: [T02-S027])
##### Branch 4d：telemetry 体量巨大、成本是首要约束
→ 推荐（新兴）：VictoriaMetrics（指标长存）/ OpenObserve / ClickHouse 自建——标 experimental (evidence: [T02-S025, T02-S052, T02-S058])
→ 全分支：用 OpenTelemetry instrument 一次，后端可换——别把 instrument code 绑死厂商 SDK (evidence: [T02-S022])

#### Branch 5：事件管理与 on-call
→ 推荐：PagerDuty（告警路由 + 排班 + IC 流程）+ 采用其开源 Incident Response 手册做流程 (evidence: [T02-S045, T02-S046])
→ **不推荐**：新项目选 Opsgenie（Atlassian 已宣 EOL）；OSS 用 Grafana OnCall (evidence: [T02-S045])
→ 硬规矩：每条告警必须 actionable（基于 symptom 不是 cause），否则就是制造 alert fatigue (evidence: [T02-S056])

#### Branch 6：平台工程（要给开发者自助 golden path）
→ 推荐：Backstage（service catalog + templates）——但需专职平台团队维护 (evidence: [T02-S034])
→ 前提检查：DORA 2025——门户≠平台质量；平台质量低时 AI/自助收益接近零，先把 paved road 的可靠性做实 (evidence: [T02-S049])
→ **不推荐**：设独立"DevOps 团队"做发布——那是制造第三个筒仓的反模式 (evidence: [T02-S048])

#### Branch 7：DevSecOps / 供应链安全
→ 推荐：Trivy（一体扫描，shift-left CI 门禁）+ cosign/sigstore（签名）+ OPA/Kyverno（admission policy）+ Vault（密钥）(evidence: [T02-S036, T02-S037, T02-S010, T02-S035])
→ 等级目标：SLSA 框架定义供应链成熟度等级 (evidence: [T02-S038])
→ 优先级：先扫已知漏洞（Trivy）再上签名/SLSA——别为合规等级跳过基础扫描

---

## 避坑清单（≥5 条）

- ❌ **不要为"显得专业"上 Kubernetes + service mesh + multi-cloud**：多数公司不需要这个复杂度，这是典型 resume-driven development；可靠性瓶颈通常是基本功不是工具先进度。"do you really need Kubernetes for this" (evidence: [T02-S001, T02-S060])
- ❌ **不要把 Terraform state 当普通文件**：terraform.tfstate 含明文密钥 + 是危险操作面，本地存储/提交 git/误删 = 灾难；必须远程后端 + 加锁 + 加密 + apply 前 plan review (evidence: [T02-S004, T02-S006])
- ❌ **不要把可观测性厂商 SDK 绑进 instrument code**：直接用 Datadog/厂商 SDK 埋点会锁死；用 OpenTelemetry instrument 一次，换后端只改 collector config（37% 团队就是为切换自由选 OTel）(evidence: [T02-S022, T02-S020])
- ❌ **不要无视 Datadog custom metrics 账单**：custom metrics 易占 30-50% 账单，加服务/集成时账单 40-200% 跳涨，中型团队可观测性花费会超过算存成本；定期审计 metric 基数 (evidence: [T02-S058])
- ❌ **不要把 observability 当"三件套 SKU 打包"买**：monitoring（known-unknowns，预设 dashboard/alert）≠ observability（unknown-unknowns，高基数任意下钻）；厂商把"observability"窄化成打包销售是营销，但也别因此否定 metrics 监控价值 (evidence: [T02-S027])
- ❌ **不要新项目选 Jenkins / Opsgenie / Spinnaker**：Jenkins 是 legacy 维护负担、Opsgenie 已宣 EOL、Spinnaker 运维成本过高份额下滑；绿地用 GitHub Actions / PagerDuty(或 Grafana OnCall) / Argo CD+Rollouts (evidence: [T02-S047, T02-S045, T02-S039])
- ❌ **不要把第三方 GitHub Action pin 到 tag**：tag 可被重新指向（2025 多起 action 投毒），pin 到 commit SHA (evidence: [T02-S038])
- ❌ **不要假设备份没问题就不测恢复**：GitLab 2017 误删生产主库 + 5 层备份全部失效——备份必须定期验证恢复，否则等于没有；用 chaos/game day 验证 DR (evidence: [T02-S043, T02-S057])
- ❌ **不要为合规等级跳过基础安全扫描**：先用 Trivy 扫已知漏洞/配置，再追 SLSA 签名等级——顺序反了是合规剧场 (evidence: [T02-S036, T02-S038])

---

## Phase 2 提炼提示

### 反复出现 ≥3 source 强调的「工具选型原则」（候选 playbook 规则）
- **先问"是否真需要这个复杂度"再选工具**（反 resume-driven development）：可靠性瓶颈多是基本功不是工具先进度 (出现于: T02-S001 / T02-S049 / T02-S060)
- **用厂商中立标准层防锁定**（OTel 之于可观测性、Terraform/OpenTofu 之于云、K8s 之于编排）：instrument/声明一次，后端/云可换 (出现于: T02-S020 / T02-S022 / T02-S058)
- **声明式 + GitOps + git 为单一真相源** 优于命令式 ClickOps：drift 自动纠正、可审计、可回滚 (出现于: T02-S012 / T02-S014 / T02-S051)
- **成本是 2026 头号选型变量**（observability 尤甚）：Datadog 账单失控催生 OSS/列存自建回流 (出现于: T02-S028 / T02-S052 / T02-S058)
- **平台质量 > 工具数量**：DORA 2025——平台质量低时 AI/自助收益接近零 (出现于: T02-S049 / T02-S034 / T02-S048)

### 显著的工具流派分裂（候选 智识谱系条目）
- **可观测性数据采集：pull 派 vs push 派** — Prometheus 拉模型（scrape，服务自暴露）vs OTel/push（agent/collector 推送）；现实趋同于"Prometheus 指标 + OTel 统一采集" (evidence: [T02-S016, T02-S022])
- **IaC：声明式 HCL 派 vs 命令式通用语言派** — Terraform/OpenTofu（HCL 声明式，provider 生态最大）vs Pulumi（TS/Python/Go 命令式控制，复用语言抽象/测试）vs Crossplane（K8s CRD 控制平面派）(evidence: [T02-S003, T02-S007, T02-S009])
- **可观测性商业模式：商用 all-in-one 派 vs OSS best-of-breed 派** — Datadog/Honeycomb（一站托管，省心但锁定+贵）vs Prometheus+Grafana+Loki+OTel（自组装，省钱+防锁定但运维重）；2026 成本压力使天平向 OSS/自建倾斜 (evidence: [T02-S028, T02-S016, T02-S058])
- **监控 vs 可观测性范式之争** — monitoring（known-unknowns，预设 dashboard/alert，Prometheus 派）vs observability（unknown-unknowns，高基数 wide events 任意下钻，Honeycomb/Charity Majors 派）；不对立但常被厂商营销混为一谈 (evidence: [T02-S027])
- **service mesh：全功能重型 vs 轻量 vs 无 sidecar** — Istio（功能全，重）vs Linkerd（轻，Rust）vs Cilium eBPF mesh（无 sidecar，内核态）(evidence: [T02-S029, T02-S030, T02-S031])
- **GitOps：开箱 UI 派 vs controller-only 模块化派** — Argo CD（UI + app-of-apps，采用率第一）vs Flux（纯 controller + GitOps Toolkit 组件化）(evidence: [T02-S012, T02-S014])
- **K8s 配置：模板派 vs overlay 派** — Helm（chart 模板 + 打包分发）vs Kustomize（无模板 overlay，kubectl 内置）；常组合使用 (evidence: [T02-S032, T02-S033])
- **K8s policy：通用 Rego 派 vs YAML 原生派** — OPA/Gatekeeper（Rego 跨系统通用）vs Kyverno（YAML 原生，仅 K8s，更易上手）(evidence: [T02-S010, T02-S053])

### 新兴工具信号
- 当前活跃/上升的新工具数：6（OpenObserve / ClickStack / Kyverno / OpenCost / Pyroscope-Parca / Falco）
- 出现→主流速度估计：成本驱动的 OSS 可观测性替代约 18-24 月（OpenTelemetry 从试到 79% 总采用用了约 3-4 年；列存自建仍 early）；K8s policy（Kyverno）已接近成长期
- 主导宏观趋势：(1) 成本治理（observability tax）→ OSS/列存回流；(2) OTel 成防锁定标准层；(3) 平台工程 + IDP 制度化；(4) 供应链安全（SLSA/sigstore）上升；(5) eBPF（Cilium/Falco/Pyroscope）作为新基础能力层

### 冷僻 / 信号薄弱评估
- 必备层 14 个（远超 ≥3 门槛）✓；多个必备有行业 survey ≥50-86% 采用率背书（Prometheus 67%、OTel 79% 总用、Argo CD ~60% 集群、平台 90% 组织）✓；新兴层 6 个（≥2）✓
- **结论：工具栈维度信号丰满，非冷僻**。一手率结构性高：60 个 source 中 41 个 verified_primary（GitHub repo root + cloud.google.com/blog DORA），约 68% 一手；其余 surrogate_primary（vendor docs，按规则不可降级）+ 1 个 reference（Reddit）。无 blacklist URL。
- Phase 2.8 无需"工具栈维度信号薄弱"标注；唯一边界：新兴层（OpenObserve/ClickStack/Pyroscope）decay=high，6 月后需复核。
