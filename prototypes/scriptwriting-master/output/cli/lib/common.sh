#!/usr/bin/env bash
# common.sh — shared helpers for 影视编剧 (Scriptwriting / Screenwriting) — 为电影 / 电视 / 流媒体剧集写戏剧蓝本的从业者认知操作系统: 决定「讲什么故事、人物是谁为何转变、场景如何被戏剧化、主题为何重要」的学科 —— 区别于导演 (调度 / 视觉实现)、制片 (融资 / 排期)、小说 (无格式 / 场景 / 视觉动作约束)。覆盖 (a) 故事与结构理论 (亚里士多德《诗学》情节 / 人物 / 思想 + 突转 peripeteia / 发现 anagnorisis + 净化 catharsis; Syd Field 范式 / 三幕 / 情节点; Freytag 金字塔; Egri 前提; McKee《故事》掌控性理念 / 鸿沟 / 价值正负转变 / 激励事件 / 渐进式复杂化; Truby《故事剖析》22 步 + 道德论证; Vogler/Campbell 英雄之旅; Blake Snyder《救猫咪》15 拍节拍表; Dan Harmon 故事环; John Yorke 五幕《进入森林》; Frank Daniel 八序列法; 起承转合东亚戏剧结构), (b) 人物 (想要 vs 需要 / 外在目标 vs 内在缺失, 人物弧光 正 / 负 / 平, flaw-wound-ghost 创伤背景, 主动 vs 被动主角的能动性, Egri 三维人物 生理 / 社会 / 心理, 反派是主角的镜子, 群像与关系网, 人物在压力下的选择中显形), (c) 对白 (潜台词 subtext, 对白即动作与冲突而非信息, 避免太直白 on the nose, 人物独特声口, 信息植入 exposition, Mamet/Sorkin 意图-阻碍式对白, 展示而非告知, 中文剧台词工艺), (d) 场景与序列工艺 (场景是有目标 / 冲突 / 转折的微型故事, 场景价值充能与转折点, 晚进早出, 八序列法, set piece, 转场, 场景头 / 动作行 / 括号提示 格式工艺), (e) 主题与前提 (掌控性理念 / 前提, 主题是被戏剧化的论证而非说教, 道德论证 Truby, 主题统一性, 这到底在讲什么), (f) 类型 (类型惯例是对观众的承诺, Snyder 10 类故事, 颠覆 vs 尊重套路, 类型片 vs 文艺片, 中国类型 主旋律 / 古装 / 年代 / 悬疑 / 甜宠 / 都市 / 军旅 / 历史正剧), (g) 格式与工业流程 (好莱坞剧本格式与 Final Draft, logline 一句话故事, treatment 故事大纲, 节拍表, 分场 / 分集大纲, spec 原创剧本 vs 委托, pitch, coverage, 美剧编剧室与 showrunner 制; 中国 大纲→人物小传→分集大纲→剧本, 长剧集 40 集结构, 网络电影 / 网大, 分账剧, 平台定制剧, 微短剧竖屏短剧), (h) 改稿与开发 (写作就是改写, 改稿 / 润色 / 推倒重写, 处理意见 / 改稿意见, 片方与平台 notes, 杀死你的宝贝, 围读, 开发地狱), (i) 改编 (IP改编 小说 / 漫画 / 游戏改编, 忠于精神而非字句, 压缩, 中国网文 IP 热), (j) 中国影视编剧产业现实 (审查 / 广电总局约束, 备案 / 立项, 平台定制剧 爱优腾芒, 分账, 编剧维权 署名权 / 欠薪 / 枪手, 注水剧, 流量 + 大IP 资本逻辑 vs 原创工艺, 导演中心制 vs 编剧话语权), (k) 编剧职业与工艺生涯 (spec vs 委托, 编剧 vs 编审 / 策划, 单兵 vs 编剧室, 在开发链条中的位置, WGA 与署名仲裁规范, 入行, 中国编剧地位与权益)。跨 电影 / 美剧流媒体 / 中国电影与长剧集。不含 导演 / 摄影 / 制片 / 融资 / 表演 / 电影理论批评为终点 / 泛小说写作 / 纪录片 / 新闻 —— 本 skill 是「戏剧化编剧」工艺: 故事 / 人物 / 场景 / 对白 / 主题 / 结构 / 格式 与围绕它们的产业流程。 master CLI scripts.
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
