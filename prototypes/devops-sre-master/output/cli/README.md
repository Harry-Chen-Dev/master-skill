# DevOps 与 SRE CLI

把 DevOps 与 SRE master skill 的认知 OS 物化成 bash 工具。
不替代 SKILL.md（思维顾问），是它的「执行端」：交互问询 → 应用 playbook / protocol → 输出结构化报告。

## 用法

所有脚本支持 `--help` / `--explain` / `--dry-run` / `--json` 四个标准 flag。

```bash
# 拿到新问题时, 按 N 个研究维度做功课
./protocol/agentic.sh

# 决策树评估 (基于 playbook)
./decision/topic-1.sh
# SOP 走查 (workflow)
./workflow/ci-cd-sop-commit-build-test-cana.sh

# 看背后的心智模型 / playbook (不交互)
./protocol/agentic.sh --explain
```

## 脚本清单

| 脚本 | 作用 |
|------|------|
| `protocol/agentic.sh` | Agentic Protocol (7 维度) — 拿到新问题时按这一行的研究维度做功课 |
| `decision/topic-1.sh` | 案例 决策树 (10 条规则) |
| `workflow/ci-cd-sop-commit-build-test-cana.sh` | CI/CD 渐进式发布流水线 SOP（commit → build → test → canary → 自动回滚） SOP 走查 |
| `workflow/on-call-sop-alert-triage-declare.sh` | 事件响应 + on-call SOP（alert → triage → declare SEV → IC → mitigate → comms → resolve） SOP 走查 |
| `workflow/sop-timeline-contributing-factor.sh` | 无指责复盘 SOP（timeline → contributing factors → action items with owners → 不指责个人） SOP 走查 |
| `workflow/slo-error-budget-sop-pick-sli-se.sh` | SLO 定义 + error budget SOP（pick SLI → set SLO → error budget policy → burn-rate alerting） SOP 走查 |
| `workflow/infrastructure-as-code-sop-modul.sh` | Infrastructure as Code 变更 SOP（写 module → plan → review → apply → state 管理 → drift 处理） SOP 走查 |
| `workflow/kubernetes-sop-manifest-helm-res.sh` | Kubernetes 部署与运维 SOP（manifest/Helm → resource limits → rollout → HPA → 排 CrashLoop/OOM） SOP 走查 |
| `workflow/instrumentation-sop-red-use-metr.sh` | 可观测性 instrumentation SOP（RED/USE → metrics+logs+traces → dashboards → actionable 告警） SOP 走查 |
| `workflow/game-day-sop-hypothesis-steady-s.sh` | 混沌工程 / Game Day SOP（hypothesis → steady state → blast radius → experiment → learn） SOP 走查 |

## 设计与生成

CLI 子树由 `tools/cli_writer.py` 自动从 `references/synthesis.md` (Section 2 Playbook + Section 9 Agentic Protocol) 和 `references/research/03-workflows.md` 生成。

完整 spec 在 master-skill 仓库 `references/cli-spec.md`。

## 重新生成

如果 synthesis.md 或 03-workflows.md 更新了, 重跑:

```bash
python3 <master-skill>/tools/cli_writer.py emit \
  --skill-dir <this-skill-dir> \
  --synthesis references/synthesis.md \
  --workflows references/research/03-workflows.md \
  --industry-cn "DevOps 与 SRE"
```
