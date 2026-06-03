# 研学营地教育 CLI

把 研学营地教育 master skill 的认知 OS 物化成 bash 工具。
不替代 SKILL.md（思维顾问），是它的「执行端」：交互问询 → 应用 playbook / protocol → 输出结构化报告。

## 用法

所有脚本支持 `--help` / `--explain` / `--dry-run` / `--json` 四个标准 flag。

```bash
# 拿到新问题时, 按 N 个研究维度做功课
./protocol/agentic.sh

# 决策树评估 (基于 playbook)
./decision/topic-1.sh
# SOP 走查 (workflow)
./workflow/b-end-to-end.sh

# 看背后的心智模型 / playbook (不交互)
./protocol/agentic.sh --explain
```

## 脚本清单

| 脚本 | 作用 |
|------|------|
| `protocol/agentic.sh` | Agentic Protocol (7 维度) — 拿到新问题时按这一行的研究维度做功课 |
| `decision/topic-1.sh` | —— 决策树 (4 条规则) |
| `decision/topic-2.sh` | 安全 决策树 (4 条规则) |
| `decision/topic-3.sh` | 课程 决策树 (1 条规则) |
| `decision/topic-4.sh` | 营地 决策树 (1 条规则) |
| `workflow/b-end-to-end.sh` | 一次完整研学旅行项目全流程（B 端校采 end-to-end） SOP 走查 |
| `workflow/c.sh` | C 端夏令营 / 营地营期全流程（产品→获客→执行→复购） SOP 走查 |
| `workflow/sop-kolb-pbl-5e-lb-t-092.sh` | 课程设计 SOP（Kolb 体验学习圈 + PBL/5E + LB/T 092 官方七步） SOP 走查 |
| `workflow/sop.sh` | 安全风控 SOP（行业生命线·最高优先级，贯穿全程） SOP 走查 |
| `workflow/sop-lb-t-054-2025-t-cats-002.sh` | 选研学基地 / 营地 SOP（对标 LB/T 054-2025 + T/CATS 002） SOP 走查 |
| `workflow/b.sh` | B 端政府采购 / 招投标 / 履约全流程（含合规与廉政红线） SOP 走查 |

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
  --industry-cn "研学营地教育"
```
