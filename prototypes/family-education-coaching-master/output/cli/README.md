# 家庭教育指导 CLI

把 家庭教育指导 master skill 的认知 OS 物化成 bash 工具。
不替代 SKILL.md（思维顾问），是它的「执行端」：交互问询 → 应用 playbook / protocol → 输出结构化报告。

## 用法

所有脚本支持 `--help` / `--explain` / `--dry-run` / `--json` 四个标准 flag。

```bash
# 拿到新问题时, 按 N 个研究维度做功课
./protocol/agentic.sh

# 决策树评估 (基于 playbook)
./decision/topic-1.sh
# SOP 走查 (workflow)
./workflow/workflow-1.sh

# 看背后的心智模型 / playbook (不交互)
./protocol/agentic.sh --explain
```

## 脚本清单

| 脚本 | 作用 |
|------|------|
| `protocol/agentic.sh` | Agentic Protocol (7 维度) — 拿到新问题时按这一行的研究维度做功课 |
| `decision/topic-1.sh` | 家庭 决策树 (2 条规则) |
| `decision/topic-2.sh` | 教育 决策树 (1 条规则) |
| `decision/topic-3.sh` | 家长 决策树 (2 条规则) |
| `decision/topic-4.sh` | 孩子 决策树 (3 条规则) |
| `decision/topic-5.sh` | 行为 决策树 (2 条规则) |
| `workflow/workflow-1.sh` | 首次家庭教育咨询工作流 SOP 走查 |
| `workflow/workflow-2.sh` | 儿童行为问题干预工作流 SOP 走查 |
| `workflow/workflow-3.sh` | 青春期亲子冲突调解工作流 SOP 走查 |
| `workflow/workflow-4.sh` | 学习习惯养成指导工作流 SOP 走查 |
| `workflow/workflow-5.sh` | 手机/网络沉迷干预工作流 SOP 走查 |
| `workflow/workflow-6.sh` | 离异家庭共同养育指导工作流 SOP 走查 |
| `workflow/workflow-7.sh` | 隔代教育矛盾调解工作流 SOP 走查 |
| `workflow/workflow-8.sh` | 家庭教育指导师职业培训工作流 SOP 走查 |
| `workflow/workflow-9.sh` | 家长课堂/讲座交付工作流 SOP 走查 |
| `workflow/workflow-10.sh` | 家校合作工作坊工作流 SOP 走查 |

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
  --industry-cn "家庭教育指导"
```
