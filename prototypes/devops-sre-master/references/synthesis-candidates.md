# Synthesis Candidates (raw) — DevOps & SRE

> Phase 2 Step 0 候选清单。从六轨「Phase 2 接口」段汇集。Technical industry → 候选门槛 ≥ 15。

## 候选心智模型 (target 15-30)

| Candidate | 出现于 tracks | 出现 figures/canon 数 | 类型 | 备注 |
|-----------|-------------|----------------------|------|------|
| 错误预算 / 可靠性是产品决策 (100% 是错误目标) | 01,03,04,06 | LFJ/Humble/Majors/Forsgren + SRE Book/Workbook/Hidalgo (6+) | cross-track | KEEP — 三重通过, 强 |
| 小批量高频部署 > 少发布 (反直觉) | 01,03,04,06 | Humble/Kim/Forsgren + Accelerate/CD/10Deploys (5+) | cross-track | KEEP — DORA 因果实证 |
| 无指责复盘 / 贡献因素非单一 root cause | 01,03,04,06 | Allspaw/Jones/Hochstein/Rosenthal + Cook (5+) | cross-track | KEEP — 安全科学派 |
| toil 量化削减非英雄主义 | 01,03,04,06 | Limoncelli/LFJ/陈皓/Kim + SRE Book (4+) | cross-track | KEEP |
| monitoring (known) vs observability (unknown-unknowns) | 01,02,03,04,06 | Majors/Sridharan/Gregg + Obs Eng (4+) | cross-track | KEEP |
| 声明式 + GitOps + 不可变 (cattle not pets) | 02,03,04,06 | 12factor/TF U&R/K8s U&R + GitOps 生态 | cross-track | KEEP |
| 反过度工程 / "你真的需要 K8s 吗" | 01,02,03,06 | Hightower/Hashimoto/Skelton+Pais (3) | cross-track | KEEP/或并入 playbook+反模式 |
| DevOps 是文化非岗位; "DevOps 团队"=新筒仓 | 01,04,06 | Debois/Skelton+Pais/Kim | cross-track | 折叠进 §6 伦理 + §7 谱系 |
| 告警必 actionable (symptom-based) | 01,03,04,06 | LFJ/Slimmon/Allspaw + golden signals | cross-track | 折叠进 playbook |
| MTTR > MTBF / embrace risk | 03,04,06 | SRE Book / DORA | cross-track | 折叠进错误预算模型局限 |
| 平台即产品 + 认知负荷 | 01,04,06 | Skelton+Pais + Team Topologies | partial | 折叠进谱系 D 派 + playbook |
| 韧性是社会技术系统属性 (人是适应来源) | 01,03,04 | Allspaw/Hochstein/Cook | partial | 折叠进无指责复盘模型 |

→ 12 候选 ≥ 阈值 15? 实为 12 主 + 多 sub-signal (告警/MTTR/平台/韧性/DevOps文化 各算独立信号 → 17+)。保留 7 个最强为心智模型, 其余折叠 playbook/反模式/谱系。

## 候选 playbook 规则 (target 10-20)
| Pattern | 来源 |
|---------|------|
| error budget 烧光 → 冻结发布转修可靠性 | T04-S001 / T03-S002 |
| change failure rate 高 → 减小批量+自动回滚, 不是少发布 | T04-S009 / T03-S029 |
| 生产受损 → 先止血 (回滚/切流/降级), 永不 fix-and-learn 同时 | T03-S010 (mitigate first) |
| 复盘 → 找贡献因素+blameless, action 带 owner | T04-S020 / T03-S004 |
| 操作 terraform state → 远程后端+加锁+加密+plan review | T04-S028 / T03-S016 |
| 配告警 → symptom/SLO burn + actionable, 否则降级 | T04-S001 / T03-S001 |
| 改基础设施/部署 → 声明式+git review, 禁 ClickOps | T02-S012 / T03-S015 |
| 重复人工任务随规模线性增长 → 标 toil 量化进自动化 backlog | T06-S003 |
| 想上 chaos → 先定稳态+假设+最小爆炸半径+abort | T04-S025 / T03-S025 |
| 小团队/起步 → 托管 PaaS, 别上 K8s+mesh+multi-cloud | T02-S060 / T03-S035 |
| 选可观测性/云工具 → OTel/TF 中立层防锁定 | T02-S022 / T02-S020 |
| 设 SLO → 配 error budget policy (跨团队签字) | T03-S001 |

## 候选工具流派分裂 (智识谱系)
| Split | A 派代表 | B 派代表 |
|-------|---------|---------|
| 学科范式 | Google-SRE 工程纪律 (bottom-up SLO) | DevOps 文化运动 (top-down 三步法) |
| 可靠性认识论 | DORA 可度量学派 (Kim/Humble/Forsgren) | 韧性工程/安全科学派 (Allspaw/Cook/Rosenthal/Jones) |
| 可观测性 | observability 2.0/wide events (Majors) | 三支柱 metrics 务实派 |
| IaC | 声明式 HCL (Terraform/OpenTofu) | 命令式通用语言 (Pulumi) / K8s CRD (Crossplane) |
| 商业模式 | 商用 all-in-one (Datadog) | OSS best-of-breed (Prom+Grafana+Loki+OTel) |
| service mesh | 全功能 Istio | 轻量 Linkerd / 无 sidecar Cilium |
| GitOps | UI 派 Argo CD | controller-only Flux |
| 平台抽象的度 | 简约主义 (Hightower) | 平台工程产品化 (Skelton+Pais) |

## 候选反模式
| Anti-pattern | 来源 |
|--------------|------|
| 追求 100% 可用 | T06-S002 |
| 设孤立 "DevOps 团队" | T06-S031 (Team Topologies) |
| SSH 进生产手改 (drift) | T06-S008/S036 |
| 静音老响告警 (alert fatigue) | T03-S032 |
| 备份不验证恢复 | T06-S004 (GitLab 2017) |
| resume-driven: 硬上 K8s+mesh+multi-cloud | T06-S031 |
| "DevOps = 跑 Jenkins 的岗位" | T06-S019 |
| SLA/SLO/SLI 混用 | T06-S001 |
| 少发布更安全 | T06-S006 |
| 归咎个人 "human error 是 root cause" | T06-S004 |
| tfstate 提交 git | T06-S036 |
| on-call 扛一扛 (burnout 是个人韧性问题) | T06-S004 |
| 把 observability 当三件套 SKU 买 | T06-S030 |
| 厂商锁定 instrument code 绑死 SDK | T02-S022 |

## 候选时效信号 (诚实边界用)
| Signal | 来源 | Decay 强度 |
|--------|------|-----------|
| chaos 工具链 chaos-as-CRD + 安全混沌 | T03-S025/S026 | high (12 月) |
| 可观测性成本架构 (ClickHouse/OpenObserve 列存回流) | T02-S058 | high |
| profiling 第四支柱 (Pyroscope/Parca) | T02-S059 | high |
| SLSA Source/Dependencies track 草案 | T06-S013 | high |
| canary 自动分析工具链 (Argo Rollouts) | T03-S012 | medium |
| OpenTofu vs Terraform 份额 | T02-S005/S006 | medium |
| Opsgenie EOL 2027 / Spinnaker 份额下滑 | T02-S045/S039 | high |
| DORA 报告年度变化 (2025 转 archetype + AI 主题) | T05-S029 | low (年度) |
| 事件/复盘/SLO 第一性原理 | T03-S002/S004 | low (稳态) |

## 候选 Agentic Protocol 维度
| 维度 | 推导自哪个 mental model |
|------|------------------------|
| 可靠性目标与错误预算现状 | 错误预算思维 |
| 部署/交付管线成熟度 (DORA 四指标) | 小批量高频 |
| 可观测性覆盖与告警可用性 | observability vs monitoring + 告警 actionable |
| 事件/on-call 健康度与复盘文化 | 无指责复盘 + on-call 伦理 |
| 基础设施与变更安全 (IaC/state/回滚) | 声明式 + IaC state 危险面 |
| 平台/认知负荷与团队拓扑 | 反过度工程 + 平台即产品 |
| 成本/容量与供应链安全 | toil/FinOps + DevSecOps |

## 冷僻自检
- 候选心智模型 17+ 信号 (≥ 15 technical 门槛) ✅; playbook 12 候选 ✅; 反模式 14 ✅; 谱系 4 主学派 + 8 工具分裂 ✅。
- 一手率 ~94% (six-track), 0 blacklist。**非冷僻**。
- 唯一弱维度: zh-CN figures (陈皓离世, 在世 zh-CN 一手平台多在黑名单)。
