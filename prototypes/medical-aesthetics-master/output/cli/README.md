# 医疗美容 CLI

把 医疗美容 master skill 的认知 OS 物化成 bash 工具。
不替代 SKILL.md（思维顾问），是它的「执行端」：交互问询 → 应用 playbook / protocol → 输出结构化报告。

## 用法

所有脚本支持 `--help` / `--explain` / `--dry-run` / `--json` 四个标准 flag。

```bash
# 拿到新问题时, 按 N 个研究维度做功课
./protocol/agentic.sh

# 决策树评估 (基于 playbook)
./decision/topic-1.sh
# SOP 走查 (workflow)
./workflow/bdd.sh

# 看背后的心智模型 / playbook (不交互)
./protocol/agentic.sh --explain
```

## 脚本清单

| 脚本 | 作用 |
|------|------|
| `protocol/agentic.sh` | Agentic Protocol (6 维度) — 拿到新问题时按这一行的研究维度做功课 |
| `decision/topic-1.sh` | 医疗 决策树 (3 条规则) |
| `decision/topic-2.sh` | 劝退 决策树 (1 条规则) |
| `decision/topic-3.sh` | 安全 决策树 (1 条规则) |
| `decision/topic-4.sh` | 可逆 决策树 (1 条规则) |
| `decision/evidence.sh` | Evidence 决策树 (2 条规则) |
| `workflow/bdd.sh` | 求美者面诊与需求挖掘（含 BDD / 容貌焦虑筛查） SOP 走查 |
| `workflow/workflow-1.sh` | 审美设计与方案规划（全脸结构化设计） SOP 走查 |
| `workflow/workflow-2.sh` | 产品/术式选型与知情同意 SOP 走查 |
| `workflow/workflow-3.sh` | 注射操作执行（安全核心） SOP 走查 |
| `workflow/workflow-4.sh` | 并发症识别与急救（不可软化） SOP 走查 |
| `workflow/workflow-5.sh` | 术后医嘱与随访 SOP 走查 |
| `workflow/workflow-6.sh` | 机构合规获客 → 面诊转化 → 复购（机构经营链） SOP 走查 |
| `workflow/workflow-7.sh` | 机构合规风控与投诉处理（资质 / 广告 / 价格 / 票据 / 病历） SOP 走查 |

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
  --industry-cn "医疗美容"
```
