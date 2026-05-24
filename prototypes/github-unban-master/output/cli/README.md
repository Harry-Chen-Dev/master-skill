# GitHub 解封 — 账号封禁/限制/恢复的领域操作系统。覆盖：(a) GitHub 官方政策体系 (TOS / 可接受使用政策 / Trust & Safety 执行模式 / 公开申诉路径 / 受制裁地区解读)；(b) 封号原因诊断学 (spam / abuse / 制裁误标 / 2FA 丢失 / ToS 违规 / 账号劫持误判 / ban evasion 等子类型 + 症状→原因映射 + 自我分诊压测)；(c) 申诉实操 craft (写一封能让 T&S 快速判误伤的英文申诉信 + 升级阶梯 + 法务介入边界 + Don'ts)；(d) 制裁与合规硬边界 (OFAC SDN 名单 / 哪些国家或地区真不可达 / VPN 误判路径 / 中国大陆不是美国制裁地区的反复重申)；(e) 中国大陆开发者特别处境 (sanctioned region 误标 + SMS 验证不支持 +86/+852 + Gitee/GitLab/Codeberg/JihuLab 备用迁移 + 私有自托管 Gitea/Forgejo)；(f) 真实案例库 (~30+ 公开案例分类拆解：误伤 / 真违规 / 制裁误标三类各自赔率与申诉成功路径)。伦理锚绝不软化：不教 ban evasion / 不教撒谎式申诉 / 真违规承认改进 / 丢 2FA 无恢复因子则诚实告知 / 中国制裁误标靠申诉不靠换 VPN / 申诉 6 个月窗口必算清 / ~3% 真违规恢复 vs ~79% 误伤申诉成功率分层标。 CLI

把 GitHub 解封 — 账号封禁/限制/恢复的领域操作系统。覆盖：(a) GitHub 官方政策体系 (TOS / 可接受使用政策 / Trust & Safety 执行模式 / 公开申诉路径 / 受制裁地区解读)；(b) 封号原因诊断学 (spam / abuse / 制裁误标 / 2FA 丢失 / ToS 违规 / 账号劫持误判 / ban evasion 等子类型 + 症状→原因映射 + 自我分诊压测)；(c) 申诉实操 craft (写一封能让 T&S 快速判误伤的英文申诉信 + 升级阶梯 + 法务介入边界 + Don'ts)；(d) 制裁与合规硬边界 (OFAC SDN 名单 / 哪些国家或地区真不可达 / VPN 误判路径 / 中国大陆不是美国制裁地区的反复重申)；(e) 中国大陆开发者特别处境 (sanctioned region 误标 + SMS 验证不支持 +86/+852 + Gitee/GitLab/Codeberg/JihuLab 备用迁移 + 私有自托管 Gitea/Forgejo)；(f) 真实案例库 (~30+ 公开案例分类拆解：误伤 / 真违规 / 制裁误标三类各自赔率与申诉成功路径)。伦理锚绝不软化：不教 ban evasion / 不教撒谎式申诉 / 真违规承认改进 / 丢 2FA 无恢复因子则诚实告知 / 中国制裁误标靠申诉不靠换 VPN / 申诉 6 个月窗口必算清 / ~3% 真违规恢复 vs ~79% 误伤申诉成功率分层标。 master skill 的认知 OS 物化成 bash 工具。
不替代 SKILL.md（思维顾问），是它的「执行端」：交互问询 → 应用 playbook / protocol → 输出结构化报告。

## 用法

所有脚本支持 `--help` / `--explain` / `--dry-run` / `--json` 四个标准 flag。

```bash
# 拿到新问题时, 按 N 个研究维度做功课
./protocol/agentic.sh

# 决策树评估 (基于 playbook)
./decision/evidence.sh
# SOP 走查 (workflow)
./workflow/suspension-discovery-triage.sh

# 看背后的心智模型 / playbook (不交互)
./protocol/agentic.sh --explain
```

## 脚本清单

| 脚本 | 作用 |
|------|------|
| `protocol/agentic.sh` | Agentic Protocol (7 维度) — 拿到新问题时按这一行的研究维度做功课 |
| `decision/evidence.sh` | Evidence 决策树 (6 条规则) |
| `decision/topic-2.sh` | 恢复 决策树 (1 条规则) |
| `decision/github.sh` | Github 决策树 (1 条规则) |
| `decision/topic-4.sh` | 迁移 决策树 (1 条规则) |
| `decision/general-playbook.sh` | 通用 Playbook 决策树 (1 条规则) |
| `workflow/suspension-discovery-triage.sh` | 封禁发现与快速分诊 (Suspension Discovery & Triage) SOP 走查 |
| `workflow/emergency-data-rescue.sh` | 紧急数据抢救 (Emergency Data Rescue) SOP 走查 |
| `workflow/root-cause-diagnosis.sh` | 封号原因深度诊断 (Root Cause Diagnosis) SOP 走查 |
| `workflow/appeal-letter-crafting.sh` | 申诉信撰写 (Appeal Letter Crafting) SOP 走查 |
| `workflow/appeal-submission-follow-up.sh` | 申诉提交与跟进 (Appeal Submission & Follow-up) SOP 走查 |
| `workflow/sanctions-mis-flag-resolution.sh` | 制裁误标专项处理 (Sanctions Mis-flag Resolution) SOP 走查 |
| `workflow/2fa-2fa-loss-recovery.sh` | 2FA 丢失恢复 (2FA Loss Recovery) SOP 走查 |
| `workflow/post-reinstatement-recovery.sh` | 申诉成功后的恢复操作 (Post-Reinstatement Recovery) SOP 走查 |
| `workflow/post-failure-migration.sh` | 申诉失败后的迁移 (Post-Failure Migration) SOP 走查 |
| `workflow/preventive-security-hardening.sh` | 预防性安全加固 (Preventive Security Hardening) SOP 走查 |

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
  --industry-cn "GitHub 解封 — 账号封禁/限制/恢复的领域操作系统。覆盖：(a) GitHub 官方政策体系 (TOS / 可接受使用政策 / Trust & Safety 执行模式 / 公开申诉路径 / 受制裁地区解读)；(b) 封号原因诊断学 (spam / abuse / 制裁误标 / 2FA 丢失 / ToS 违规 / 账号劫持误判 / ban evasion 等子类型 + 症状→原因映射 + 自我分诊压测)；(c) 申诉实操 craft (写一封能让 T&S 快速判误伤的英文申诉信 + 升级阶梯 + 法务介入边界 + Don'ts)；(d) 制裁与合规硬边界 (OFAC SDN 名单 / 哪些国家或地区真不可达 / VPN 误判路径 / 中国大陆不是美国制裁地区的反复重申)；(e) 中国大陆开发者特别处境 (sanctioned region 误标 + SMS 验证不支持 +86/+852 + Gitee/GitLab/Codeberg/JihuLab 备用迁移 + 私有自托管 Gitea/Forgejo)；(f) 真实案例库 (~30+ 公开案例分类拆解：误伤 / 真违规 / 制裁误标三类各自赔率与申诉成功路径)。伦理锚绝不软化：不教 ban evasion / 不教撒谎式申诉 / 真违规承认改进 / 丢 2FA 无恢复因子则诚实告知 / 中国制裁误标靠申诉不靠换 VPN / 申诉 6 个月窗口必算清 / ~3% 真违规恢复 vs ~79% 误伤申诉成功率分层标。"
```
