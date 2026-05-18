#!/usr/bin/env bash
# common.sh — shared helpers for 红队渗透 / 攻防 — 受授权的红队作业者 + 渗透测试工程师 + 攻击型安全顾问的认知操作系统 (侦察 OSINT / 外网渗透 / 内网 AD 渗透 BloodHound + Kerberoasting + ADCS 利用 + 横向移动 / Web 应用渗透 OWASP WSTG / 移动 OWASP MASTG / 云渗透 AWS Azure GCP IAM 路径 + 容器逃逸 + K8s / C2 操作 Cobalt Strike Sliver Mythic Havoc + OPSEC / 初始访问 + AV EDR 绕过 (仅授权场景) / 无线 RF / 物理社工 / 报告与整改 / 框架 MITRE ATT&CK + D3FEND + PTES + OSSTMM + NIST 800-115 + Kill Chain / 法律伦理 CFAA + 网络安全法 + 刑法 285 286 + 数据安全法 + GDPR + 授权书 + 范围 + 交战规则 — 不含 黑产 / 未授权攻击 / 大规模 exploitation / 供应链投毒 / 未授权 DoS — 这是 重罪 + 行业封杀 + 律师吊销, 本 skill 严守 authorized-only 边界 — 也不含 蓝队 SOC + 恶意软件 即服务 / 僵尸网络 / 勒索软件作者 — 这是 cybercrime 不是 红队) master CLI scripts.
# Pure bash 4 + POSIX coreutils. No external deps.

if [[ -t 1 ]]; then
  MS_BOLD=$'\033[1m'; MS_DIM=$'\033[2m'
  MS_RED=$'\033[31m'; MS_GREEN=$'\033[32m'
  MS_YELLOW=$'\033[33m'; MS_BLUE=$'\033[34m'
  MS_RESET=$'\033[0m'
else
  MS_BOLD=""; MS_DIM=""; MS_RED=""; MS_GREEN=""; MS_YELLOW=""; MS_BLUE=""; MS_RESET=""
fi

ms_section() { printf "\n%s━━ %s ━━%s\n" "$MS_BOLD$MS_BLUE" "$1" "$MS_RESET"; }
ms_info()    { printf "%s%s%s\n" "$MS_DIM" "$1" "$MS_RESET"; }
ms_warn()    { printf "%s⚠ %s%s\n" "$MS_YELLOW" "$1" "$MS_RESET"; }
ms_error()   { printf "%s✗ %s%s\n" "$MS_RED" "$1" "$MS_RESET" >&2; }
ms_ok()      { printf "%s✓ %s%s\n" "$MS_GREEN" "$1" "$MS_RESET"; }
ms_prompt()  { printf "%s? %s%s " "$MS_BOLD" "$1" "$MS_RESET"; }

ms_read_multiline() {
  local result=""
  local line
  while IFS= read -r line; do
    [[ -z "$line" ]] && break
    result+="$line"$'\n'
  done
  printf "%s" "$result"
}

ms_confirm() {
  ms_prompt "$1 [y/N]"
  local ans
  read -r ans
  [[ "$ans" =~ ^[Yy] ]]
}

# Markdown buffer (global)
MS_REPORT_BUFFER=""
ms_buffer_append() { MS_REPORT_BUFFER+="$1"$'\n'; }

ms_emit_md_file() {
  local slug="$1"
  local fname="${slug}-$(date +%Y%m%d-%H%M%S).md"
  printf "%s" "$MS_REPORT_BUFFER" > "$fname"
  ms_ok "报告已写到 $fname"
}

ms_emit_md_stdout() { printf "%s" "$MS_REPORT_BUFFER"; }

ms_json_escape() {
  local s="$1"
  s="${s//\\/\\\\}"
  s="${s//\"/\\\"}"
  s="${s//$'\n'/\\n}"
  s="${s//$'\t'/\\t}"
  s="${s//$'\r'/}"
  printf "%s" "$s"
}

ms_emit_json() {
  local out="{"
  local first=1
  while [[ $# -ge 2 ]]; do
    [[ $first -eq 1 ]] || out+=","
    first=0
    out+="\"$(ms_json_escape "$1")\":\"$(ms_json_escape "$2")\""
    shift 2
  done
  out+="}"
  printf "%s\n" "$out"
}
