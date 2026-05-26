# 教育SaaS CLI

把 教育SaaS master skill 的认知 OS 物化成 bash 工具。
不替代 SKILL.md（思维顾问），是它的「执行端」：交互问询 → 应用 playbook / protocol → 输出结构化报告。

## 用法

所有脚本支持 `--help` / `--explain` / `--dry-run` / `--json` 四个标准 flag。

```bash
# 拿到新问题时, 按 N 个研究维度做功课
./protocol/agentic.sh

# 决策树评估 (基于 playbook)
./decision/topic-1.sh
# SOP 走查 (workflow)
./workflow/lms.sh

# 看背后的心智模型 / playbook (不交互)
./protocol/agentic.sh --explain
```

## 脚本清单

| 脚本 | 作用 |
|------|------|
| `protocol/agentic.sh` | Agentic Protocol (7 维度) — 拿到新问题时按这一行的研究维度做功课 |
| `decision/topic-1.sh` | 案例 决策树 (4 条规则) |
| `decision/topic-2.sh` | 数据 决策树 (2 条规则) |
| `decision/topic-3.sh` | 教师 决策树 (1 条规则) |
| `decision/saas.sh` | Saas 决策树 (1 条规则) |
| `decision/topic-5.sh` | 教育 决策树 (1 条规则) |
| `decision/canvas.sh` | Canvas 决策树 (1 条规则) |
| `workflow/lms.sh` | LMS 选型与部署 SOP 走查 |
| `workflow/sis.sh` | SIS 数据迁移与上线 SOP 走查 |
| `workflow/workflow-1.sh` | 招生漏斗管理 SOP 走查 |
| `workflow/workflow-2.sh` | 课程设计与上线 SOP 走查 |
| `workflow/workflow-3.sh` | 在线/混合授课 SOP 走查 |
| `workflow/workflow-4.sh` | 学习分析与教学干预 SOP 走查 |
| `workflow/lti.sh` | LTI/集成工具接入 SOP 走查 |
| `workflow/workflow-5.sh` | 学术诚信审查 SOP 走查 |
| `workflow/workflow-6.sh` | 培训机构教务全流程（中国） SOP 走查 |
| `workflow/edtech-saas-gtm-go-to-market.sh` | EdTech SaaS GTM（Go-to-Market） SOP 走查 |

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
  --industry-cn "教育SaaS"
```
