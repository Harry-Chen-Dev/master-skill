# AIGC 创作工作流 CLI

把 AIGC 创作工作流 master skill 的认知 OS 物化成 bash 工具。
不替代 SKILL.md（思维顾问），是它的「执行端」：交互问询 → 应用 playbook / protocol → 输出结构化报告。

## 用法

所有脚本支持 `--help` / `--explain` / `--dry-run` / `--json` 四个标准 flag。

```bash
# 拿到新问题时, 按 N 个研究维度做功课
./protocol/agentic.sh

# 决策树评估 (基于 playbook)
./decision/topic-1.sh
# SOP 走查 (workflow)
./workflow/t2i-decay-risk-low-last-updated-.sh

# 看背后的心智模型 / playbook (不交互)
./protocol/agentic.sh --explain
```

## 脚本清单

| 脚本 | 作用 |
|------|------|
| `protocol/agentic.sh` | Agentic Protocol (6 维度) — 拿到新问题时按这一行的研究维度做功课 |
| `decision/topic-1.sh` | 模型 决策树 (2 条规则) |
| `decision/topic-2.sh` | 方向 决策树 (1 条规则) |
| `decision/evidence.sh` | Evidence 决策树 (5 条规则) |
| `workflow/t2i-decay-risk-low-last-updated-.sh` | 单张精控出图（文生图 T2I 全链）(Decay risk: low) last_updated: 2026-06-22 SOP 走查 |
| `workflow/controlnet-decay-risk-low-last-u.sh` | 可控生成（ControlNet 控构图/姿态/线稿）(Decay risk: low) last_updated: 2026-06-22 SOP 走查 |
| `workflow/lora-ipadapter-decay-risk-medium.sh` | 角色/风格一致性（LoRA 训练 + IPAdapter/参考图）(Decay risk: medium) last_updated: 2026-06-22 SOP 走查 |
| `workflow/i2i-inpaint-outpaint-decay-risk-.sh` | 图生图 + 局部重绘修图（I2I + inpaint/outpaint + 修脸换脸）(Decay risk: medium) last_updated: 2026-06-22 SOP 走查 |
| `workflow/comfyui-decay-risk-medium-last-u.sh` | ComfyUI 节点工作流搭建与复用（工程链）(Decay risk: medium) last_updated: 2026-06-22 SOP 走查 |
| `workflow/runway-decay-risk-high-last-upda.sh` | 图生视频 / 文生视频（可灵 / 即梦 / Runway）(Decay risk: high) last_updated: 2026-06-22 SOP 走查 |
| `workflow/ai-curious-refuge-ai-decay-risk-.sh` | AI 短片 / 分镜全流程（Curious Refuge 式 AI 影视）(Decay risk: high) last_updated: 2026-06-22 SOP 走查 |
| `workflow/midjourney-sref-cref-oref-decay-.sh` | Midjourney 闭源易用出图流（sref/cref/oref 一致性）(Decay risk: high) last_updated: 2026-06-22 SOP 走查 |

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
  --industry-cn "AIGC 创作工作流"
```
