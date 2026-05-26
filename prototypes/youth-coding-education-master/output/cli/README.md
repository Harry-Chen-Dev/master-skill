# 青少年编程教育 CLI

把 青少年编程教育 master skill 的认知 OS 物化成 bash 工具。
不替代 SKILL.md（思维顾问），是它的「执行端」：交互问询 → 应用 playbook / protocol → 输出结构化报告。

## 用法

所有脚本支持 `--help` / `--explain` / `--dry-run` / `--json` 四个标准 flag。

```bash
# 拿到新问题时, 按 N 个研究维度做功课
./protocol/agentic.sh

# 决策树评估 (基于 playbook)
./decision/topic-1.sh
# SOP 走查 (workflow)
./workflow/scratch.sh

# 看背后的心智模型 / playbook (不交互)
./protocol/agentic.sh --explain
```

## 脚本清单

| 脚本 | 作用 |
|------|------|
| `protocol/agentic.sh` | Agentic Protocol (7 维度) — 拿到新问题时按这一行的研究维度做功课 |
| `decision/topic-1.sh` | 编程 决策树 (6 条规则) |
| `decision/topic-2.sh` | 竞赛 决策树 (3 条规则) |
| `decision/general-playbook.sh` | 通用 Playbook 决策树 (1 条规则) |
| `workflow/scratch.sh` | 设计一堂 Scratch 启蒙课 SOP 走查 |
| `workflow/python.sh` | 规划 Python 进阶课程体系 SOP 走查 |
| `workflow/workflow-1.sh` | 设计信奥赛训练计划 SOP 走查 |
| `workflow/workflow-2.sh` | 设计机器人/创客课程 SOP 走查 |
| `workflow/0-1.sh` | 新建少儿编程培训机构 (从0到1) SOP 走查 |
| `workflow/workflow-3.sh` | 招生与转化流程 SOP 走查 |
| `workflow/workflow-4.sh` | 教师培训与认证 SOP 走查 |
| `workflow/workflow-5.sh` | 一堂编程课的交付流程 SOP 走查 |
| `workflow/workflow-6.sh` | 编程作品评价与展示 SOP 走查 |
| `workflow/noip-noi.sh` | 备战 NOIP/NOI 冲刺 SOP 走查 |

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
  --industry-cn "青少年编程教育"
```
