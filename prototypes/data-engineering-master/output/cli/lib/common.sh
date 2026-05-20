#!/usr/bin/env bash
# common.sh — shared helpers for 数据工程 — 数据平台从业者的认知操作系统, 覆盖把数据从源系统搬运成可靠 / 可查询 / 可信赖形态供分析 / ML / 数据产品消费的全生命周期 (生成 → 摄取 → 存储 → 转换 → 服务 + 安全/数据管理/DataOps/数据架构/编排/软件工程 六条暗流, Reis & Housley 框架): 摄取与集成 (批 + CDC 变更数据捕获 Debezium + EL 工具 Fivetran/Airbyte/Meltano/dlt + Kafka Connect + schema drift) / 存储与文件表格式 (对象存储数据湖 + 列存 Parquet/ORC/Arrow/Avro + 开放表格式 Apache Iceberg/Delta Lake/Apache Hudi + lakehouse + 分区/compaction) / 转换与建模 (ELT dbt/SQLMesh + Spark + 维度建模 Kimball + Inmon + Data Vault + 大宽表 OBT + 渐变维 SCD + 增量模型 + 语义/指标层) / 编排与工作流 (Apache Airflow/Dagster/Prefect/Mage/Kestra/Apache DolphinScheduler + DAG + 幂等 + 回填 backfill + 数据资产调度) / 批流与实时 (Apache Kafka/Apache Flink/Spark Structured Streaming/Kinesis/Pulsar/Redpanda + Lambda vs Kappa + watermark/窗口/exactly-once + 流式 SQL Materialize/RisingWave + 实时 OLAP ClickHouse/Apache Druid/Apache Pinot/StarRocks/Apache Doris) / 数仓与查询引擎 (Snowflake/BigQuery/Redshift/Databricks SQL/Trino/Presto/DuckDB/Polars + 存算分离 + MPP) / 数据质量测试与可观测性 (dbt tests/Great Expectations/Soda + 数据契约 + Monte Carlo data downtime + 新鲜度/量/schema 异常检测) / 数据治理编目与血缘 (DataHub/Amundsen/OpenMetadata/Unity Catalog + 列级血缘 + PII 分类 + 访问控制 + GDPR) / DataOps 与可靠性 (数据 CI/CD + 转换版本控制 + 环境隔离 + 幂等重处理 + 数据 SLA/SLO + 计算存储 FinOps) / 数据架构范式 (现代数据栈 + lakehouse + data mesh + data fabric + 去中心化 vs 中心化所有权) / 分析工程角色 (dbt 时代连接数据工程与分析的桥) — 不含 数据科学/ML 建模本身 (是下游消费者) / BI 仪表盘制作 (serving 下游) / 数据分析报表为终点 / 'data engineer = 跑 Hadoop 的' 过时窄化 / 通用后端应用开发 (平行学科) master CLI scripts.
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
