#!/usr/bin/env bash
# common.sh — shared helpers for GitHub 解封 — 账号封禁/限制/恢复的领域操作系统。覆盖：(a) GitHub 官方政策体系 (TOS / 可接受使用政策 / Trust & Safety 执行模式 / 公开申诉路径 / 受制裁地区解读)；(b) 封号原因诊断学 (spam / abuse / 制裁误标 / 2FA 丢失 / ToS 违规 / 账号劫持误判 / ban evasion 等子类型 + 症状→原因映射 + 自我分诊压测)；(c) 申诉实操 craft (写一封能让 T&S 快速判误伤的英文申诉信 + 升级阶梯 + 法务介入边界 + Don'ts)；(d) 制裁与合规硬边界 (OFAC SDN 名单 / 哪些国家或地区真不可达 / VPN 误判路径 / 中国大陆不是美国制裁地区的反复重申)；(e) 中国大陆开发者特别处境 (sanctioned region 误标 + SMS 验证不支持 +86/+852 + Gitee/GitLab/Codeberg/JihuLab 备用迁移 + 私有自托管 Gitea/Forgejo)；(f) 真实案例库 (~30+ 公开案例分类拆解：误伤 / 真违规 / 制裁误标三类各自赔率与申诉成功路径)。伦理锚绝不软化：不教 ban evasion / 不教撒谎式申诉 / 真违规承认改进 / 丢 2FA 无恢复因子则诚实告知 / 中国制裁误标靠申诉不靠换 VPN / 申诉 6 个月窗口必算清 / ~3% 真违规恢复 vs ~79% 误伤申诉成功率分层标。 master CLI scripts.
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
