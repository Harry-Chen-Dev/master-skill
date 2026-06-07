# UBNT/UniFi 企业 Wi-Fi 工程 CLI

把 UBNT/UniFi 企业 Wi-Fi 工程 master skill 的认知 OS 物化成 bash 工具。
不替代 SKILL.md（思维顾问），是它的「执行端」：交互问询 → 应用 playbook / protocol → 输出结构化报告。

## 用法

所有脚本支持 `--help` / `--explain` / `--dry-run` / `--json` 四个标准 flag。

```bash
# 拿到新问题时, 按 N 个研究维度做功课
./protocol/agentic.sh

# 决策树评估 (基于 playbook)
./decision/topic-1.sh
# SOP 走查 (workflow)
./workflow/greenfield-ubnt-deployment-for-a.sh

# 看背后的心智模型 / playbook (不交互)
./protocol/agentic.sh --explain
```

## 脚本清单

| 脚本 | 作用 |
|------|------|
| `protocol/agentic.sh` | Agentic Protocol (6 维度) — 拿到新问题时按这一行的研究维度做功课 |
| `decision/topic-1.sh` | 客户 决策树 (2 条规则) |
| `decision/general-playbook.sh` | 通用 Playbook 决策树 (6 条规则) |
| `workflow/greenfield-ubnt-deployment-for-a.sh` | Greenfield UBNT deployment for an 80-person office SOP 走查 |
| `workflow/unifi-performance-troubleshoot-l.sh` | UniFi performance troubleshoot (low throughput / drop / jitter) SOP 走查 |
| `workflow/high-density-capacity-planning-8.sh` | High-density capacity planning (80+ user dense office) ★ USER SCENARIO ★ SOP 走查 |
| `workflow/roaming-optimization-sticky-clie.sh` | Roaming optimization (sticky clients / slow roam) SOP 走查 |
| `workflow/site-survey-post-install-validat.sh` | Site survey + post-install validation SOP 走查 |
| `workflow/unifi-controller-upgrade-migrati.sh` | UniFi controller upgrade / migration SOP 走查 |
| `workflow/wpa3-security-hardening-dragonbl.sh` | WPA3 security hardening + Dragonblood-aware audit SOP 走查 |
| `workflow/ai-augmented-operation-unifi-unp.sh` | AI-augmented operation (UniFi + unpoller + LLM agent stack) SOP 走查 |

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
  --industry-cn "UBNT/UniFi 企业 Wi-Fi 工程"
```
