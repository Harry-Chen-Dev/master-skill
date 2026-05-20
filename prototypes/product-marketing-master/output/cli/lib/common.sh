#!/usr/bin/env bash
# common.sh — shared helpers for 产品营销 (PMM, Product Marketing) — 拥有「产品如何被定位 / 表达 / 发布 / 卖进市场」的从业者认知操作系统: 是产品 / 销售 / 市场 / 客户之间的连接组织, 负责把产品能力翻译成市场价值, 并把市场声音带回产品。覆盖 (a) 定位与差异化 (April Dunford 「刻意选择语境」框架 + 竞争性替代方案 + 卖价值不卖功能 + 选择「让你优势成立的市场参照系」, 对照 Ries & Trout 经典「定位是占领心智」), (b) 信息传递与叙事 (messaging 层级 / 信息屋 + 价值主张 + 收益导向 vs 战略叙事「换框架」Andy Raskin + 表达清晰度 Emma Stratton / Punchy + 初创 homepage 定位 FletchPMM), (c) 进入市场 (GTM) 策略与产品发布 (发布分级 T1/T2/T3 + 发布流程与跨职能编排 + GTM 打法 PLG vs SLG vs 混合 + 滩头细分选择), (d) 市场与竞争情报 (竞品分析 + battlecard 战卡 + 输赢分析 win/loss + 竞争赋能 Klue/Crayon/Clozd), (e) 买家与客户研究 (ICP 理想客户画像 + 买家 / 用户 persona + Jobs-to-be-Done 任务理论 Christensen/Moesta/Ulwick ODI + 客户之声 VoC + 用真实买家测信息 Wynter/Peep Laja), (f) 销售赋能 (战卡 + pitch / 销售 deck + 一页纸 + demo 叙事 + 异议处理 + 销售培训 + 内容采用率 — 你的产出只值销售实际用到的那部分), (g) 定价与打包 (价值定价 + 打包分层 + 《Monetizing Innovation》Ramanujam/Simon-Kucher + PLG 定价 — 常与产品 / 财务共担), (h) 细分与品类 (市场细分 + TAM/SAM/SOM + 技术采用生命周期与跨越鸿沟 Geoffrey Moore + 品类设计与叙事 Play Bigger / Christopher Lochhead — 稀有且昂贵, 不是默认选项), (i) 需求生成与内容协同 (campaign 信息 + 思想领导力 + 漏斗内容 TOFU/MOFU/BOFU + ABM 基于客户营销), (j) 分析师与影响者关系 (Gartner 魔力象限 + Forrester Wave + 分析师 briefing — To B 场景, 对 pay-to-play 影响诚实标注), (k) 客户营销与倡导 (参考客户 + case study + 评测站 G2/TrustRadius/Capterra 运营 + 社区), (l) PMM 运营与度量 (影响管道 + 赢率 + 发布采用率 + 信息穿透率 + 角色汇报线「向产品还是向市场」之争 + PMM 作为战略职能 vs 接单工具人陷阱); 跨 B2B SaaS (该学科重心) / B2C 消费 / 开发者 PLG / 平台产品。不含 产品管理 (PM 造产品 / 拥有 roadmap, PMM 拥有市场 — 相邻且极易混淆) / 增长 / 效果营销 / 付费投放 (平行学科) / 品牌 / 企业传播 / 公关为终点 / 需求生成为终点 (PMM 与之协同但不等同) / 平面设计 /「做 slide 和周边的团队」(PMM 抗争的接单工具人窄化) / 泛泛「市场营销」。 master CLI scripts.
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
