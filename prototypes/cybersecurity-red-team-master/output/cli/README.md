# 红队渗透 / 攻防 — 受授权的红队作业者 + 渗透测试工程师 + 攻击型安全顾问的认知操作系统 (侦察 OSINT / 外网渗透 / 内网 AD 渗透 BloodHound + Kerberoasting + ADCS 利用 + 横向移动 / Web 应用渗透 OWASP WSTG / 移动 OWASP MASTG / 云渗透 AWS Azure GCP IAM 路径 + 容器逃逸 + K8s / C2 操作 Cobalt Strike Sliver Mythic Havoc + OPSEC / 初始访问 + AV EDR 绕过 (仅授权场景) / 无线 RF / 物理社工 / 报告与整改 / 框架 MITRE ATT&CK + D3FEND + PTES + OSSTMM + NIST 800-115 + Kill Chain / 法律伦理 CFAA + 网络安全法 + 刑法 285 286 + 数据安全法 + GDPR + 授权书 + 范围 + 交战规则 — 不含 黑产 / 未授权攻击 / 大规模 exploitation / 供应链投毒 / 未授权 DoS — 这是 重罪 + 行业封杀 + 律师吊销, 本 skill 严守 authorized-only 边界 — 也不含 蓝队 SOC + 恶意软件 即服务 / 僵尸网络 / 勒索软件作者 — 这是 cybercrime 不是 红队) CLI

把 红队渗透 / 攻防 — 受授权的红队作业者 + 渗透测试工程师 + 攻击型安全顾问的认知操作系统 (侦察 OSINT / 外网渗透 / 内网 AD 渗透 BloodHound + Kerberoasting + ADCS 利用 + 横向移动 / Web 应用渗透 OWASP WSTG / 移动 OWASP MASTG / 云渗透 AWS Azure GCP IAM 路径 + 容器逃逸 + K8s / C2 操作 Cobalt Strike Sliver Mythic Havoc + OPSEC / 初始访问 + AV EDR 绕过 (仅授权场景) / 无线 RF / 物理社工 / 报告与整改 / 框架 MITRE ATT&CK + D3FEND + PTES + OSSTMM + NIST 800-115 + Kill Chain / 法律伦理 CFAA + 网络安全法 + 刑法 285 286 + 数据安全法 + GDPR + 授权书 + 范围 + 交战规则 — 不含 黑产 / 未授权攻击 / 大规模 exploitation / 供应链投毒 / 未授权 DoS — 这是 重罪 + 行业封杀 + 律师吊销, 本 skill 严守 authorized-only 边界 — 也不含 蓝队 SOC + 恶意软件 即服务 / 僵尸网络 / 勒索软件作者 — 这是 cybercrime 不是 红队) master skill 的认知 OS 物化成 bash 工具。
不替代 SKILL.md（思维顾问），是它的「执行端」：交互问询 → 应用 playbook / protocol → 输出结构化报告。

## 用法

所有脚本支持 `--help` / `--explain` / `--dry-run` / `--json` 四个标准 flag。

```bash
# 拿到新问题时, 按 N 个研究维度做功课
./protocol/agentic.sh

# 决策树评估 (基于 playbook)
./decision/topic-1.sh
# SOP 走查 (workflow)
./workflow/external-network-pentest-sop.sh

# 看背后的心智模型 / playbook (不交互)
./protocol/agentic.sh --explain
```

## 脚本清单

| 脚本 | 作用 |
|------|------|
| `protocol/agentic.sh` | Agentic Protocol (7 维度) — 拿到新问题时按这一行的研究维度做功课 |
| `decision/topic-1.sh` | 客户 决策树 (7 条规则) |
| `decision/engagement.sh` | Engagement 决策树 (1 条规则) |
| `decision/day.sh` | Day 决策树 (2 条规则) |
| `workflow/external-network-pentest-sop.sh` | External Network Pentest 外网渗透 SOP SOP 走查 |
| `workflow/internal-ad-pentest-sop-assume-b.sh` | Internal AD Pentest SOP (Assume Breach) SOP 走查 |
| `workflow/web-application-pentest-sop-owas.sh` | Web Application Pentest SOP (OWASP WSTG) SOP 走查 |
| `workflow/mobile-app-pentest-sop-owasp-mas.sh` | Mobile App Pentest SOP (OWASP MASTG) SOP 走查 |
| `workflow/cloud-pentest-sop-aws-focus-azur.sh` | Cloud Pentest SOP (AWS focus + Azure + GCP) SOP 走查 |
| `workflow/c2-setup-operate-sop.sh` | C2 Setup + Operate SOP SOP 走查 |
| `workflow/phishing-campaign-authorized-onl.sh` | Phishing Campaign (Authorized Only) SOP SOP 走查 |
| `workflow/purple-team-adversary-emulation-.sh` | Purple Team / Adversary Emulation SOP SOP 走查 |
| `workflow/bug-bounty-workflow-sop.sh` | Bug Bounty Workflow SOP SOP 走查 |
| `workflow/reporting-remediation-sop.sh` | Reporting + Remediation SOP SOP 走查 |

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
  --industry-cn "红队渗透 / 攻防 — 受授权的红队作业者 + 渗透测试工程师 + 攻击型安全顾问的认知操作系统 (侦察 OSINT / 外网渗透 / 内网 AD 渗透 BloodHound + Kerberoasting + ADCS 利用 + 横向移动 / Web 应用渗透 OWASP WSTG / 移动 OWASP MASTG / 云渗透 AWS Azure GCP IAM 路径 + 容器逃逸 + K8s / C2 操作 Cobalt Strike Sliver Mythic Havoc + OPSEC / 初始访问 + AV EDR 绕过 (仅授权场景) / 无线 RF / 物理社工 / 报告与整改 / 框架 MITRE ATT&CK + D3FEND + PTES + OSSTMM + NIST 800-115 + Kill Chain / 法律伦理 CFAA + 网络安全法 + 刑法 285 286 + 数据安全法 + GDPR + 授权书 + 范围 + 交战规则 — 不含 黑产 / 未授权攻击 / 大规模 exploitation / 供应链投毒 / 未授权 DoS — 这是 重罪 + 行业封杀 + 律师吊销, 本 skill 严守 authorized-only 边界 — 也不含 蓝队 SOC + 恶意软件 即服务 / 僵尸网络 / 勒索软件作者 — 这是 cybercrime 不是 红队)"
```
