# 中医诊疗 — 中医临床医师的认知操作系统 (经典理论 阴阳五行脏腑气血经络六经卫气营血三焦 + 四诊八纲 + 治法 + 方剂学 经方时方 + 中药学 四气五味归经炮制 + 针灸学 经络穴位手法灸法 + 推拿按摩 + 中医各科 内外妇儿骨伤皮肤眼耳鼻喉肛肠老年急症 + 中西医结合 + 循证中医 + NATCM 监管 + 中医诊所备案 + 国家级名老中医 学术继承人 — 不含 道家修炼 / 风水算命 / 中医养生科普 / 中医美容 / 民族医学藏蒙维傣) CLI

把 中医诊疗 — 中医临床医师的认知操作系统 (经典理论 阴阳五行脏腑气血经络六经卫气营血三焦 + 四诊八纲 + 治法 + 方剂学 经方时方 + 中药学 四气五味归经炮制 + 针灸学 经络穴位手法灸法 + 推拿按摩 + 中医各科 内外妇儿骨伤皮肤眼耳鼻喉肛肠老年急症 + 中西医结合 + 循证中医 + NATCM 监管 + 中医诊所备案 + 国家级名老中医 学术继承人 — 不含 道家修炼 / 风水算命 / 中医养生科普 / 中医美容 / 民族医学藏蒙维傣) master skill 的认知 OS 物化成 bash 工具。
不替代 SKILL.md（思维顾问），是它的「执行端」：交互问询 → 应用 playbook / protocol → 输出结构化报告。

## 用法

所有脚本支持 `--help` / `--explain` / `--dry-run` / `--json` 四个标准 flag。

```bash
# 拿到新问题时, 按 N 个研究维度做功课
./protocol/agentic.sh

# 决策树评估 (基于 playbook)
./decision/topic-1.sh


# 看背后的心智模型 / playbook (不交互)
./protocol/agentic.sh --explain
```

## 脚本清单

| 脚本 | 作用 |
|------|------|
| `protocol/agentic.sh` | Agentic Protocol (7 维度) — 拿到新问题时按这一行的研究维度做功课 |
| `decision/topic-1.sh` | 中医 决策树 (4 条规则) |
| `decision/topic-2.sh` | 长期 决策树 (4 条规则) |
| `decision/topic-3.sh` | 经方 决策树 (1 条规则) |
| `decision/general-playbook.sh` | 通用 Playbook 决策树 (1 条规则) |

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
  --industry-cn "中医诊疗 — 中医临床医师的认知操作系统 (经典理论 阴阳五行脏腑气血经络六经卫气营血三焦 + 四诊八纲 + 治法 + 方剂学 经方时方 + 中药学 四气五味归经炮制 + 针灸学 经络穴位手法灸法 + 推拿按摩 + 中医各科 内外妇儿骨伤皮肤眼耳鼻喉肛肠老年急症 + 中西医结合 + 循证中医 + NATCM 监管 + 中医诊所备案 + 国家级名老中医 学术继承人 — 不含 道家修炼 / 风水算命 / 中医养生科普 / 中医美容 / 民族医学藏蒙维傣)"
```
