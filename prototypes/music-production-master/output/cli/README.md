# 音乐制作 / 混音 CLI

把 音乐制作 / 混音 master skill 的认知 OS 物化成 bash 工具。
不替代 SKILL.md（思维顾问），是它的「执行端」：交互问询 → 应用 playbook / protocol → 输出结构化报告。

## 用法

所有脚本支持 `--help` / `--explain` / `--dry-run` / `--json` 四个标准 flag。

```bash
# 拿到新问题时, 按 N 个研究维度做功课
./protocol/agentic.sh

# 决策树评估 (基于 playbook)
./decision/topic-1.sh
# SOP 走查 (workflow)
./workflow/arrangement-production-idea.sh

# 看背后的心智模型 / playbook (不交互)
./protocol/agentic.sh --explain
```

## 脚本清单

| 脚本 | 作用 |
|------|------|
| `protocol/agentic.sh` | Agentic Protocol (6 维度) — 拿到新问题时按这一行的研究维度做功课 |
| `decision/topic-1.sh` | 响度 决策树 (3 条规则) |
| `decision/topic-2.sh` | 处理 决策树 (2 条规则) |
| `decision/topic-3.sh` | 房间 决策树 (1 条规则) |
| `decision/topic-4.sh` | 案例 决策树 (3 条规则) |
| `workflow/arrangement-production-idea.sh` | Arrangement / Production（把 idea 做到编曲定型） SOP 走查 |
| `workflow/tracking-programming.sh` | Tracking / Programming（录音 + 编程把表演固化成轨） SOP 走查 |
| `workflow/editing-comping-quantize-pitch-c.sh` | Editing（comping / quantize / pitch-correct / time-align —— 整理成"可混"素材） SOP 走查 |
| `workflow/mixing-gain-staging-balance-eq-c.sh` | Mixing（gain staging → balance → EQ → compression → space → automation → bus/mix-bus） SOP 走查 |
| `workflow/mastering-loudness-eq-limiting-d.sh` | Mastering（loudness / EQ / limiting / dither / sequencing —— 做成可发行母带） SOP 走查 |
| `workflow/delivery-ddp-streaming-spec-stem.sh` | Delivery（DDP / streaming spec / stems / Atmos —— 交付到分发/压盘） SOP 走查 |
| `workflow/ai-stem-driven-cross-cutting-12-.sh` | AI / stem-driven 重混 + 起点生成（cross-cutting，近 12 月的真正新 workflow） SOP 走查 |

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
  --industry-cn "音乐制作 / 混音"
```
