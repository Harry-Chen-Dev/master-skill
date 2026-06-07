# 个人投资理财 CLI

把 个人投资理财 master skill 的认知 OS 物化成 bash 工具。
不替代 SKILL.md（思维顾问），是它的「执行端」：交互问询 → 应用 playbook / protocol → 输出结构化报告。

## 用法

所有脚本支持 `--help` / `--explain` / `--dry-run` / `--json` 四个标准 flag。

```bash
# 拿到新问题时, 按 N 个研究维度做功课
./protocol/agentic.sh

# 决策树评估 (基于 playbook)
./decision/evidence.sh
# SOP 走查 (workflow)
./workflow/workflow-1.sh

# 看背后的心智模型 / playbook (不交互)
./protocol/agentic.sh --explain
```

## 脚本清单

| 脚本 | 作用 |
|------|------|
| `protocol/agentic.sh` | Agentic Protocol (6 维度) — 拿到新问题时按这一行的研究维度做功课 |
| `decision/evidence.sh` | Evidence 决策树 (5 条规则) |
| `decision/topic-2.sh` | 账户 决策树 (2 条规则) |
| `decision/topic-3.sh` | 主动 决策树 (1 条规则) |
| `decision/topic-4.sh` | 价值 决策树 (2 条规则) |
| `workflow/workflow-1.sh` | 组合搭建与管理主工作流（端到端，最重要） SOP 走查 |
| `workflow/workflow-2.sh` | 价值投资工作流（选股 → 估值 → 安全边际 → 持有/卖出） SOP 走查 |
| `workflow/workflow-3.sh` | 被动指数工作流（定配置 → 最低费率宽基 → 自动定投 → 阈值再平衡 → 什么都不做） SOP 走查 |
| `workflow/setup-stop-loss.sh` | 技术分析工作流（扫 setup → 入场 → stop-loss → 风险定仓 → 出场 → 复盘） SOP 走查 |
| `workflow/workflow-4.sh` | 趋势 / 动量工作流（定信号 → 分散篮子 → 系统化进出 → 风险定仓 → 跟系统） SOP 走查 |
| `workflow/workflow-5.sh` | 再平衡 + 税损收割子工作流（横切，被多个主工作流复用） SOP 走查 |

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
  --industry-cn "个人投资理财"
```
