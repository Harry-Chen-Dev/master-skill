# 数据工程 — 数据平台从业者的认知操作系统, 覆盖把数据从源系统搬运成可靠 / 可查询 / 可信赖形态供分析 / ML / 数据产品消费的全生命周期 (生成 → 摄取 → 存储 → 转换 → 服务 + 安全/数据管理/DataOps/数据架构/编排/软件工程 六条暗流, Reis & Housley 框架): 摄取与集成 (批 + CDC 变更数据捕获 Debezium + EL 工具 Fivetran/Airbyte/Meltano/dlt + Kafka Connect + schema drift) / 存储与文件表格式 (对象存储数据湖 + 列存 Parquet/ORC/Arrow/Avro + 开放表格式 Apache Iceberg/Delta Lake/Apache Hudi + lakehouse + 分区/compaction) / 转换与建模 (ELT dbt/SQLMesh + Spark + 维度建模 Kimball + Inmon + Data Vault + 大宽表 OBT + 渐变维 SCD + 增量模型 + 语义/指标层) / 编排与工作流 (Apache Airflow/Dagster/Prefect/Mage/Kestra/Apache DolphinScheduler + DAG + 幂等 + 回填 backfill + 数据资产调度) / 批流与实时 (Apache Kafka/Apache Flink/Spark Structured Streaming/Kinesis/Pulsar/Redpanda + Lambda vs Kappa + watermark/窗口/exactly-once + 流式 SQL Materialize/RisingWave + 实时 OLAP ClickHouse/Apache Druid/Apache Pinot/StarRocks/Apache Doris) / 数仓与查询引擎 (Snowflake/BigQuery/Redshift/Databricks SQL/Trino/Presto/DuckDB/Polars + 存算分离 + MPP) / 数据质量测试与可观测性 (dbt tests/Great Expectations/Soda + 数据契约 + Monte Carlo data downtime + 新鲜度/量/schema 异常检测) / 数据治理编目与血缘 (DataHub/Amundsen/OpenMetadata/Unity Catalog + 列级血缘 + PII 分类 + 访问控制 + GDPR) / DataOps 与可靠性 (数据 CI/CD + 转换版本控制 + 环境隔离 + 幂等重处理 + 数据 SLA/SLO + 计算存储 FinOps) / 数据架构范式 (现代数据栈 + lakehouse + data mesh + data fabric + 去中心化 vs 中心化所有权) / 分析工程角色 (dbt 时代连接数据工程与分析的桥) — 不含 数据科学/ML 建模本身 (是下游消费者) / BI 仪表盘制作 (serving 下游) / 数据分析报表为终点 / 'data engineer = 跑 Hadoop 的' 过时窄化 / 通用后端应用开发 (平行学科) CLI

把 数据工程 — 数据平台从业者的认知操作系统, 覆盖把数据从源系统搬运成可靠 / 可查询 / 可信赖形态供分析 / ML / 数据产品消费的全生命周期 (生成 → 摄取 → 存储 → 转换 → 服务 + 安全/数据管理/DataOps/数据架构/编排/软件工程 六条暗流, Reis & Housley 框架): 摄取与集成 (批 + CDC 变更数据捕获 Debezium + EL 工具 Fivetran/Airbyte/Meltano/dlt + Kafka Connect + schema drift) / 存储与文件表格式 (对象存储数据湖 + 列存 Parquet/ORC/Arrow/Avro + 开放表格式 Apache Iceberg/Delta Lake/Apache Hudi + lakehouse + 分区/compaction) / 转换与建模 (ELT dbt/SQLMesh + Spark + 维度建模 Kimball + Inmon + Data Vault + 大宽表 OBT + 渐变维 SCD + 增量模型 + 语义/指标层) / 编排与工作流 (Apache Airflow/Dagster/Prefect/Mage/Kestra/Apache DolphinScheduler + DAG + 幂等 + 回填 backfill + 数据资产调度) / 批流与实时 (Apache Kafka/Apache Flink/Spark Structured Streaming/Kinesis/Pulsar/Redpanda + Lambda vs Kappa + watermark/窗口/exactly-once + 流式 SQL Materialize/RisingWave + 实时 OLAP ClickHouse/Apache Druid/Apache Pinot/StarRocks/Apache Doris) / 数仓与查询引擎 (Snowflake/BigQuery/Redshift/Databricks SQL/Trino/Presto/DuckDB/Polars + 存算分离 + MPP) / 数据质量测试与可观测性 (dbt tests/Great Expectations/Soda + 数据契约 + Monte Carlo data downtime + 新鲜度/量/schema 异常检测) / 数据治理编目与血缘 (DataHub/Amundsen/OpenMetadata/Unity Catalog + 列级血缘 + PII 分类 + 访问控制 + GDPR) / DataOps 与可靠性 (数据 CI/CD + 转换版本控制 + 环境隔离 + 幂等重处理 + 数据 SLA/SLO + 计算存储 FinOps) / 数据架构范式 (现代数据栈 + lakehouse + data mesh + data fabric + 去中心化 vs 中心化所有权) / 分析工程角色 (dbt 时代连接数据工程与分析的桥) — 不含 数据科学/ML 建模本身 (是下游消费者) / BI 仪表盘制作 (serving 下游) / 数据分析报表为终点 / 'data engineer = 跑 Hadoop 的' 过时窄化 / 通用后端应用开发 (平行学科) master skill 的认知 OS 物化成 bash 工具。
不替代 SKILL.md（思维顾问），是它的「执行端」：交互问询 → 应用 playbook / protocol → 输出结构化报告。

## 用法

所有脚本支持 `--help` / `--explain` / `--dry-run` / `--json` 四个标准 flag。

```bash
# 拿到新问题时, 按 N 个研究维度做功课
./protocol/agentic.sh

# 决策树评估 (基于 playbook)
./decision/topic-1.sh
# SOP 走查 (workflow)
./workflow/elt.sh

# 看背后的心智模型 / playbook (不交互)
./protocol/agentic.sh --explain
```

## 脚本清单

| 脚本 | 作用 |
|------|------|
| `protocol/agentic.sh` | Agentic Protocol (7 维度) — 拿到新问题时按这一行的研究维度做功课 |
| `decision/topic-1.sh` | 数据 决策树 (5 条规则) |
| `decision/topic-2.sh` | 分区 决策树 (2 条规则) |
| `decision/topic-3.sh` | 引擎 决策树 (2 条规则) |
| `decision/general-playbook.sh` | 通用 Playbook 决策树 (1 条规则) |
| `workflow/elt.sh` | 构建一条 ELT 管道 SOP 走查 |
| `workflow/cdc.sh` | CDC / 增量摄取 SOP 走查 |
| `workflow/dbt.sh` | 维度建模 + dbt 项目结构 SOP 走查 |
| `workflow/dag.sh` | 编排 DAG 设计 SOP 走查 |
| `workflow/lakehouse.sh` | lakehouse 表格式落地 SOP 走查 |
| `workflow/workflow-1.sh` | 流处理管道 SOP 走查 |
| `workflow/workflow-2.sh` | 数据质量门禁 + 数据契约 SOP 走查 |
| `workflow/dataops-ci-cd.sh` | 数据 DataOps / CI-CD + 成本治理 SOP 走查 |

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
  --industry-cn "数据工程 — 数据平台从业者的认知操作系统, 覆盖把数据从源系统搬运成可靠 / 可查询 / 可信赖形态供分析 / ML / 数据产品消费的全生命周期 (生成 → 摄取 → 存储 → 转换 → 服务 + 安全/数据管理/DataOps/数据架构/编排/软件工程 六条暗流, Reis & Housley 框架): 摄取与集成 (批 + CDC 变更数据捕获 Debezium + EL 工具 Fivetran/Airbyte/Meltano/dlt + Kafka Connect + schema drift) / 存储与文件表格式 (对象存储数据湖 + 列存 Parquet/ORC/Arrow/Avro + 开放表格式 Apache Iceberg/Delta Lake/Apache Hudi + lakehouse + 分区/compaction) / 转换与建模 (ELT dbt/SQLMesh + Spark + 维度建模 Kimball + Inmon + Data Vault + 大宽表 OBT + 渐变维 SCD + 增量模型 + 语义/指标层) / 编排与工作流 (Apache Airflow/Dagster/Prefect/Mage/Kestra/Apache DolphinScheduler + DAG + 幂等 + 回填 backfill + 数据资产调度) / 批流与实时 (Apache Kafka/Apache Flink/Spark Structured Streaming/Kinesis/Pulsar/Redpanda + Lambda vs Kappa + watermark/窗口/exactly-once + 流式 SQL Materialize/RisingWave + 实时 OLAP ClickHouse/Apache Druid/Apache Pinot/StarRocks/Apache Doris) / 数仓与查询引擎 (Snowflake/BigQuery/Redshift/Databricks SQL/Trino/Presto/DuckDB/Polars + 存算分离 + MPP) / 数据质量测试与可观测性 (dbt tests/Great Expectations/Soda + 数据契约 + Monte Carlo data downtime + 新鲜度/量/schema 异常检测) / 数据治理编目与血缘 (DataHub/Amundsen/OpenMetadata/Unity Catalog + 列级血缘 + PII 分类 + 访问控制 + GDPR) / DataOps 与可靠性 (数据 CI/CD + 转换版本控制 + 环境隔离 + 幂等重处理 + 数据 SLA/SLO + 计算存储 FinOps) / 数据架构范式 (现代数据栈 + lakehouse + data mesh + data fabric + 去中心化 vs 中心化所有权) / 分析工程角色 (dbt 时代连接数据工程与分析的桥) — 不含 数据科学/ML 建模本身 (是下游消费者) / BI 仪表盘制作 (serving 下游) / 数据分析报表为终点 / 'data engineer = 跑 Hadoop 的' 过时窄化 / 通用后端应用开发 (平行学科)"
```
