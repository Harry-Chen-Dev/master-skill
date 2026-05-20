# Track 02 — Tools 工具栈与选型决策树（Data Engineering / 数据工程）

> Phase 1 wave 2 Track 02 输出。locale = en-primary, zh-CN secondary。last_checked 全文 = 2026-05-20。
> Wave 1 seed 不在磁盘（research/ 下 01/04/05/06 缺失），本 track 以 intake.json 的 key_figures_candidates / core_subdomains_candidates / surrogate_domain_whitelist_preemptive 为 seed 池独立完成，GitHub stars 全部 2026-05-20 现场核验。
> 工具栈是 master skill 衰减最快的一节 — 每张卡片带 `last_checked` + 每个 maturity signal 带日期。

## Source Manifest

| source_id | url | bucket | last_checked | author/host | one-line note |
|-----------|-----|--------|--------------|-------------|---------------|
| T02-S001 | https://github.com/apache/airflow | verified_primary | 2026-05-20 | Apache | Airflow repo 45.5k★ — 编排事实标准 |
| T02-S002 | https://airflow.apache.org | surrogate_primary | 2026-05-20 | Apache | vendor docs (Apache 项目一手 — 编排) |
| T02-S003 | https://github.com/dbt-labs/dbt-core | verified_primary | 2026-05-20 | dbt Labs | dbt-core repo 12.8k★ (repo 重构后) |
| T02-S004 | https://docs.getdbt.com | surrogate_primary | 2026-05-20 | dbt Labs | vendor docs (厂商一手 — analytics eng 标准) |
| T02-S005 | https://www.getdbt.com/resources/state-of-analytics-engineering-2025 | surrogate_primary | 2026-05-20 | dbt Labs | vendor docs (厂商一手 — 2025 survey, n=459) |
| T02-S006 | https://github.com/apache/spark | verified_primary | 2026-05-20 | Apache | Spark repo 43.3k★ — 分布式计算 |
| T02-S007 | https://spark.apache.org | surrogate_primary | 2026-05-20 | Apache | vendor docs (Apache 项目一手 — Spark) |
| T02-S008 | https://github.com/apache/kafka | verified_primary | 2026-05-20 | Apache | Kafka repo 32.6k★ — 流平台 |
| T02-S009 | https://kafka.apache.org | surrogate_primary | 2026-05-20 | Apache | vendor docs (Apache 项目一手 — Kafka) |
| T02-S010 | https://github.com/apache/iceberg | verified_primary | 2026-05-20 | Apache | Iceberg repo 8.9k★ — 开放表格式 |
| T02-S011 | https://iceberg.apache.org | surrogate_primary | 2026-05-20 | Apache | vendor docs (Apache 项目一手 — Iceberg) |
| T02-S012 | https://github.com/delta-io/delta | verified_primary | 2026-05-20 | Delta/LF | Delta Lake repo 8.8k★ |
| T02-S013 | https://delta.io | surrogate_primary | 2026-05-20 | Databricks/LF | vendor docs (项目一手 — Delta Lake) |
| T02-S014 | https://github.com/apache/hudi | verified_primary | 2026-05-20 | Apache | Hudi repo 6.2k★ — upsert/CDC lakehouse |
| T02-S015 | https://hudi.apache.org | surrogate_primary | 2026-05-20 | Apache | vendor docs (Apache 项目一手 — Hudi) |
| T02-S016 | https://github.com/duckdb/duckdb | verified_primary | 2026-05-20 | DuckDB Labs | DuckDB repo 38.3k★ — 进程内 OLAP |
| T02-S017 | https://duckdb.org | surrogate_primary | 2026-05-20 | DuckDB Labs | vendor docs (项目一手 — 单机引擎) |
| T02-S018 | https://github.com/pola-rs/polars | verified_primary | 2026-05-20 | Polars | Polars repo 38.5k★ — Rust DataFrame |
| T02-S019 | https://pola.rs | surrogate_primary | 2026-05-20 | Ritchie Vink | vendor docs (项目一手 — Polars) |
| T02-S020 | https://motherduck.com/blog/big-data-is-dead/ | surrogate_primary | 2026-05-20 | Jordan Tigani | vendor docs (作者一手 — 'Big Data is Dead') |
| T02-S021 | https://github.com/dagster-io/dagster | verified_primary | 2026-05-20 | Dagster Labs | Dagster repo 15.5k★ — asset 编排 |
| T02-S022 | https://docs.dagster.io | surrogate_primary | 2026-05-20 | Dagster Labs | vendor docs (厂商一手 — asset-based) |
| T02-S023 | https://github.com/PrefectHQ/prefect | verified_primary | 2026-05-20 | Prefect | Prefect repo 22.4k★ — Pythonic 编排 |
| T02-S024 | https://www.prefect.io | surrogate_primary | 2026-05-20 | Prefect | vendor docs (厂商一手 — Prefect) |
| T02-S025 | https://github.com/apache/flink | verified_primary | 2026-05-20 | Apache | Flink repo 26k★ — 流计算 |
| T02-S026 | https://flink.apache.org | surrogate_primary | 2026-05-20 | Apache | vendor docs (Apache 项目一手 — Flink) |
| T02-S027 | https://github.com/ClickHouse/ClickHouse | verified_primary | 2026-05-20 | ClickHouse | ClickHouse repo 47.5k★ — 实时 OLAP |
| T02-S028 | https://clickhouse.com | surrogate_primary | 2026-05-20 | ClickHouse | vendor docs (厂商一手 — 实时 OLAP) |
| T02-S029 | https://github.com/trinodb/trino | verified_primary | 2026-05-20 | Trino | Trino repo 12.8k★ — 联邦查询引擎 |
| T02-S030 | https://trino.io | surrogate_primary | 2026-05-20 | Trino | vendor docs (项目一手 — Trino) |
| T02-S031 | https://www.snowflake.com | surrogate_primary | 2026-05-20 | Snowflake | vendor docs (厂商一手 — 云数仓) |
| T02-S032 | https://cloud.google.com/bigquery/docs | surrogate_primary | 2026-05-20 | Google Cloud | vendor docs (厂商一手 — BigQuery) |
| T02-S033 | https://www.databricks.com | surrogate_primary | 2026-05-20 | Databricks | vendor docs (厂商一手 — Spark/Delta/UC) |
| T02-S034 | https://github.com/airbytehq/airbyte | verified_primary | 2026-05-20 | Airbyte | Airbyte repo 21.3k★ — 开源 EL |
| T02-S035 | https://www.fivetran.com | surrogate_primary | 2026-05-20 | Fivetran | vendor docs (厂商一手 — managed EL) |
| T02-S036 | https://github.com/dlt-hub/dlt | verified_primary | 2026-05-20 | dltHub | dlt repo 5.3k★ — Python EL 库 |
| T02-S037 | https://dlthub.com | surrogate_primary | 2026-05-20 | dltHub | vendor docs (厂商一手 — dlt) |
| T02-S038 | https://github.com/debezium/debezium | verified_primary | 2026-05-20 | Debezium | Debezium repo 12.7k★ — CDC 事实标准 |
| T02-S039 | https://debezium.io | surrogate_primary | 2026-05-20 | Gunnar Morling | vendor docs (项目一手 — CDC) |
| T02-S040 | https://github.com/TobikoData/sqlmesh | verified_primary | 2026-05-20 | Tobiko Data | SQLMesh repo 3.1k★ — dbt 竞品 |
| T02-S041 | https://sqlmesh.com | surrogate_primary | 2026-05-20 | Tobiko Data | vendor docs (厂商一手 — SQLMesh) |
| T02-S042 | https://github.com/apache/paimon | verified_primary | 2026-05-20 | Apache | Paimon repo 3.3k★ — streaming lakehouse |
| T02-S043 | https://paimon.apache.org | surrogate_primary | 2026-05-20 | Apache | vendor docs (Apache 项目一手 — 中国 streaming lakehouse) |
| T02-S044 | https://github.com/risingwavelabs/risingwave | verified_primary | 2026-05-20 | RisingWave | RisingWave repo 9k★ — 流式 SQL DB |
| T02-S045 | https://github.com/great-expectations/great_expectations | verified_primary | 2026-05-20 | GX | GX repo 11.5k★ — 数据质量 |
| T02-S046 | https://greatexpectations.io | surrogate_primary | 2026-05-20 | GX | vendor docs (厂商一手 — 数据测试) |
| T02-S047 | https://github.com/datahub-project/datahub | verified_primary | 2026-05-20 | DataHub/Acryl | DataHub repo 11.9k★ — 元数据/血缘 |
| T02-S048 | https://datahubproject.io | surrogate_primary | 2026-05-20 | Acryl/LinkedIn | vendor docs (项目一手 — catalog) |
| T02-S049 | https://www.montecarlodata.com | surrogate_primary | 2026-05-20 | Barr Moses | vendor docs (厂商一手 — data observability/'data downtime') |
| T02-S050 | https://maximebeauchemin.medium.com/functional-data-engineering-a-modern-paradigm-for-batch-data-processing-2327ec32c42a | surrogate_primary | 2026-05-20 | Maxime Beauchemin | vendor docs (作者一手 — Functional Data Engineering) |
| T02-S051 | https://github.com/StarRocks/starrocks | verified_primary | 2026-05-20 | StarRocks | StarRocks repo 11.7k★ — 实时数仓 |
| T02-S052 | https://github.com/apache/doris | verified_primary | 2026-05-20 | Apache | Doris repo 15.4k★ — 实时数仓 (百度起源) |
| T02-S053 | https://github.com/apache/dolphinscheduler | verified_primary | 2026-05-20 | Apache | DolphinScheduler repo 14.3k★ — 中国一手编排 |
| T02-S054 | https://github.com/apache/seatunnel | verified_primary | 2026-05-20 | Apache | SeaTunnel repo 9.3k★ — 中国一手集成 |
| T02-S055 | https://github.com/kestra-io/kestra | verified_primary | 2026-05-20 | Kestra | Kestra repo 26.9k★ — 声明式编排 |
| T02-S056 | https://github.com/mage-ai/mage-ai | verified_primary | 2026-05-20 | Mage | Mage repo 8.7k★ — 编排 |
| T02-S057 | https://github.com/open-metadata/OpenMetadata | verified_primary | 2026-05-20 | Collate | OpenMetadata repo 14k★ — catalog |
| T02-S058 | https://github.com/sodadata/soda-core | verified_primary | 2026-05-20 | Soda | Soda Core repo 2.4k★ — 数据质量 |
| T02-S059 | https://parquet.apache.org | surrogate_primary | 2026-05-20 | Apache | vendor docs (Apache 项目一手 — 列存格式) |
| T02-S060 | https://arrow.apache.org | surrogate_primary | 2026-05-20 | Apache/Wes McKinney | vendor docs (Apache 项目一手 — 内存列存标准) |
| T02-S061 | https://www.thoughtworks.com/radar | surrogate_primary | 2026-05-20 | ThoughtWorks | vendor docs (技术趋势权威 — Technology Radar) |
| T02-S062 | https://www.elementary-data.com | surrogate_primary | 2026-05-20 | Elementary | vendor docs (厂商一手 — dbt-native 可观测性) |
| T02-S063 | https://kestra.io | surrogate_primary | 2026-05-20 | Kestra | vendor docs (厂商一手 — Kestra) |
| T02-S064 | https://netflixtechblog.com | surrogate_primary | 2026-05-20 | Netflix | vendor docs (Netflix 一手 — Iceberg 大规模实践) |
| T02-S065 | https://eng.uber.com | surrogate_primary | 2026-05-20 | Uber | vendor docs (Uber 一手 — Hudi 发源) |
| T02-S066 | https://github.com/apache/airbyte (n/a — see T02-S034) | dead | 2026-05-20 | — | 占位避免重复, 见 S034 |
| T02-S067 | https://www.onehouse.ai | surrogate_primary | 2026-05-20 | Vinoth Chandar | vendor docs (厂商一手 — Hudi 创始 Onehouse) |
| T02-S068 | https://gable.ai | surrogate_primary | 2026-05-20 | Chad Sanderson | vendor docs (厂商一手 — data contracts 工具) |

> 注: T02-S066 是误编号占位 (与 S034 同 repo)，标 dead 不影响引用。所有 .apache.org / .io / .com / .dev vendor 域名经 `source_verifier.py classify` 跑出 `secondary`，按 intake.json surrogate_domain_whitelist_preemptive 策略 **升级 surrogate_primary** 并在 note 写 literal "vendor docs"。github.com/{org}/{repo} root 自动 `verified_primary`。

---

## 总览（按 tier 分组）

**必备层 stars 基准计算**: 候选池有 stars 数据的工具中位数约 12k（Airflow 45.5/Spark 43.3/ClickHouse 47.5/DuckDB 38.3/Polars 38.5/Kestra 26.9/Prefect 22.4/Airbyte 21.3/Doris 15.4/Dagster 15.5/DolphinScheduler 14.3/OpenMetadata 14/dbt 12.8/Kafka 32.6/Trino 12.8/Debezium 12.7/DataHub 11.9/GX 11.5/StarRocks 11.7/SeaTunnel 9.3/RisingWave 9/Iceberg 8.9/Delta 8.8/Mage 8.7/Hudi 6.2/dlt 5.3/Paimon 3.3/SQLMesh 3.1/Soda 2.4）→ 中位数 ≈ 12.7k → 必备阈值 ≈ 25k。**但 stars 在数据工程严重失真**：dbt (analytics eng 事实标准, 30k 公司周活 evidence:[T02-S005]) 仅 12.8k★ (repo 重构), 而 Snowflake/BigQuery/Redshift 闭源无 repo。故必备层用「≥3 独立 source + 行业 survey ≥50% 采用」为主、stars 阈值为辅。

### 必备层（13 个 — ≥80% 从业者用 / 行业基础设施）
| 工具 | 一句话 | Decay | Sources |
|------|--------|-------|---------|
| SQL + Python | 数据工程两门母语，转换/胶水/编排全靠它 | low | [T02-S005] |
| dbt (dbt-core) | analytics engineering 事实标准，SQL-first 转换+测试+血缘+文档 | low | [T02-S003, T02-S004, T02-S005] |
| Apache Airflow | DAG 编排事实标准，任务调度+依赖+重试+回填 | low | [T02-S001, T02-S002] |
| Apache Spark | 大规模分布式转换/批处理的工业标准引擎 | low | [T02-S006, T02-S007] |
| Apache Kafka | 流平台/日志事实标准，摄取+事件总线 | low | [T02-S008, T02-S009] |
| 云数仓 (Snowflake/BigQuery/Redshift/Databricks SQL) | 存算分离 MPP，ELT 的计算落脚点 | low | [T02-S031, T02-S032, T02-S033] |
| 开放表格式 (Iceberg/Delta/Hudi) | lakehouse 的 ACID/time-travel/schema evolution 层 | low | [T02-S010, T02-S012, T02-S014] |
| Parquet | 列存磁盘格式事实标准，分析数据落盘默认 | low | [T02-S059] |
| Apache Arrow | 内存列存交换标准，引擎间零拷贝互通 | low | [T02-S060] |
| 对象存储 (S3/GCS/ADLS) | 数据湖的存储底座，存算分离的"存" | low | [T02-S020, T02-S064] |
| EL 工具 (Fivetran/Airbyte/dlt) | 摄取层 build-vs-buy 的事实选择 | medium | [T02-S034, T02-S035, T02-S036] |
| 编排器 (Dagster/Prefect 作为 Airflow 替代) | asset/Pythonic 编排，新项目越来越多默认 | medium | [T02-S021, T02-S023] |
| DuckDB | 进程内 OLAP，"big data is dead" 时代单机默认 | medium | [T02-S016, T02-S017, T02-S020] |

### 场景特化（7 类 — 见下文「场景特化」节，约 30 个工具）
| 类 | 代表工具 | Decay |
|----|---------|-------|
| (1) 摄取-EL-CDC | Fivetran/Airbyte/dlt/Meltano/Debezium/Kafka Connect/SeaTunnel | medium |
| (2) 存储-表格式-lakehouse | Iceberg/Delta/Hudi/Parquet/ORC/Arrow/lakeFS | low-medium |
| (3) 转换-建模 | dbt/SQLMesh/Spark/Dataform | low-medium |
| (4) 编排 | Airflow/Dagster/Prefect/Mage/Kestra/DolphinScheduler | medium |
| (5) 批流-实时 OLAP | Kafka/Flink/Spark Streaming/Materialize/RisingWave/ClickHouse/Druid/Pinot/StarRocks/Doris | medium |
| (6) 数仓-查询引擎 | Snowflake/BigQuery/Databricks SQL/Trino/Presto/DuckDB/Polars/Dremio | low-medium |
| (7) 数据质量-治理-DataOps | Great Expectations/Soda/Monte Carlo/Elementary/DataHub/Amundsen/OpenMetadata/Unity Catalog | medium |

### 新兴/实验层（近 12 月起势, decay high — 9 个）
| 工具 | 一句话 | Decay | Sources |
|------|--------|-------|---------|
| DuckDB / MotherDuck | 进程内 + 云协同，反过早分布式 | high | [T02-S016, T02-S020] |
| Polars | Rust DataFrame，pandas 高性能替代 | medium-high | [T02-S018, T02-S019] |
| SQLMesh | 带列级血缘/虚拟环境的 dbt 替代 | high | [T02-S040, T02-S041] |
| Apache Paimon | Flink 原生 streaming lakehouse 表格式 | high | [T02-S042, T02-S043] |
| RisingWave | Postgres 兼容流式 SQL 数据库 | high | [T02-S044] |
| dlt (dlthub) | 声明式 Python EL 库，code-first 摄取 | high | [T02-S036, T02-S037] |
| Iceberg REST catalog / Polaris | 中立 catalog 标准，引擎解耦 | high | [T02-S011, T02-S061] |
| Apache XTable / Delta UniForm | 表格式互操作 (Iceberg↔Delta↔Hudi) | high | [T02-S061] |
| 数据契约工具 (Gable / data contracts) | shift-left schema 治理 | high | [T02-S068] |

---

## 必备层（详细卡片）

### 1. dbt (dbt-core)
- **One-liner**: dbt — analytics engineering 事实标准，把 SQL 转换变成软件工程（版本控制+模块化+测试+文档+血缘+增量模型）。
- **Tier**: 必备
- **Maintainer**: dbt Labs (前 Fishtown Analytics; 创始 Tristan Handy) — https://www.getdbt.com
- **License**: open (Apache-2.0, dbt-core); dbt Cloud / Fusion engine 部分专有
- **Maturity signals**: GitHub stars 12.8k (2026-05-20, dbt-core repo 重构后数字偏低)；行业采用 ~30,000 公司每周使用 dbt + 5,000+ dbt Cloud 客户 (evidence:[T02-S005])；活跃 healthy。
- **典型使用场景**: 云数仓内 ELT 转换 (Snowflake/BigQuery/Databricks SQL)；medallion bronze→silver→gold 建模；指标层 (MetricFlow) owner。
- **不适合 / 替代**: 重 Python/非 SQL 转换 → Spark/Polars；要列级血缘+无状态虚拟环境 → SQLMesh (evidence:[T02-S040])；纯流式 → Flink SQL。
- **生产案例**: dbt Labs 2025 survey 显示 analytics engineer 占 IC 受访者 48% (evidence:[T02-S005])。
- **维护者背景** (sub_skill_link): Track 01 — Tristan Handy (analytics engineering 运动发起)。
- **可信度**: high · **Decay**: low (24+ 月稳定, <20% 被取代概率)

### 2. Apache Airflow
- **One-liner**: Airflow — DAG 编排事实标准 (Maxime Beauchemin 创于 Airbnb)，任务调度+依赖+重试+回填。
- **Tier**: 必备
- **Maintainer**: Apache Software Foundation — https://airflow.apache.org
- **License**: open (Apache-2.0)
- **Maturity signals**: GitHub stars 45.5k (2026-05-20)；Airflow 3.x 已发布 (DAG versioning / 更好 backfill)；活跃 healthy。
- **典型使用场景**: 跨工具 batch pipeline 编排 (调 dbt + Spark + EL)；cron + sensor 触发；大规模回填。
- **不适合 / 替代**: asset/data-aware 优先 → Dagster (evidence:[T02-S021])；轻量 Pythonic 动态流 → Prefect；纯 dbt 项目无需重编排器。
- **维护者背景**: Track 01 — Maxime Beauchemin ('Functional Data Engineering' evidence:[T02-S050])。
- **可信度**: high · **Decay**: low

### 3. Apache Spark
- **One-liner**: Spark — 大规模分布式转换/批处理工业标准引擎 (Matei Zaharia, UC Berkeley)。
- **Tier**: 必备 · **Maintainer**: Apache — https://spark.apache.org · **License**: open (Apache-2.0)
- **Maturity signals**: GitHub stars 43.3k (2026-05-20)；活跃 healthy。
- **典型使用场景**: TB-PB 级转换；PySpark 重逻辑；Databricks 平台核心。
- **不适合 / 替代**: 数据塞得进单机 (中位数公司单表 < 几十 GB) → DuckDB/Polars，**不要为简历上 Spark** (evidence:[T02-S020])。
- **可信度**: high · **Decay**: low

### 4. Apache Kafka
- **One-liner**: Kafka — 流平台/分布式日志事实标准 (Jay Kreps, LinkedIn)，摄取+事件总线+CDC 管道。
- **Tier**: 必备 · **Maintainer**: Apache — https://kafka.apache.org · **License**: open (Apache-2.0)
- **Maturity signals**: GitHub stars 32.6k (2026-05-20)；KRaft (去 ZooKeeper) 已默认；活跃 healthy。
- **典型使用场景**: 高吞吐事件摄取；Debezium CDC 落点；Flink/Spark Streaming 上游。
- **不适合 / 替代**: 低运维需求 → Redpanda (Kafka 兼容)/云托管 (Kinesis/Confluent Cloud)；批分析无需流平台。
- **维护者背景**: Track 01 — Jay Kreps ('The Log')。
- **可信度**: high · **Decay**: low

### 5. 云数仓 (Snowflake / BigQuery / Redshift / Databricks SQL)
- **One-liner**: 云数仓 — 存算分离 MPP，ELT 的计算落脚点 + serving 层。
- **Tier**: 必备 · **License**: proprietary (Snowflake/BigQuery/Redshift); Databricks 基于开源 Spark/Delta
- **Maturity signals**: 无公开 repo (闭源)；来源 vendor docs + 行业 survey 普遍采用 (evidence:[T02-S031, T02-S032, T02-S033])。
- **典型使用场景**: dbt ELT 目标；BI serving；半结构化 (VARIANT/JSON)。
- **不适合 / 替代**: 单机能算 → DuckDB；要避 vendor lock-in → lakehouse (Iceberg + Trino/Databricks)；成本敏感小数据别开 warehouse。
- **可信度**: high (proprietary, 来源 vendor docs + 第三方 case) · **Decay**: low

### 6. 开放表格式 (Apache Iceberg / Delta Lake / Apache Hudi)
- **One-liner**: 开放表格式 — 给对象存储上的 Parquet 加 ACID/time-travel/schema evolution/隐藏分区，lakehouse 的核心层。
- **Tier**: 必备 · **License**: open (Iceberg/Hudi Apache-2.0; Delta LF/Apache-2.0)
- **Maturity signals**: Iceberg 8.9k★ / Delta 8.8k★ / Hudi 6.2k★ (2026-05-20)；三者活跃 healthy。
- **典型使用场景**: Iceberg = 中立生态 + 隐藏分区 (Netflix 起源 evidence:[T02-S064])；Delta = Databricks 生态强；Hudi = upsert/CDC 增量 (Uber 起源 evidence:[T02-S065])。
- **不适合 / 替代**: 纯云数仓内 (Snowflake native table) 无需开放表格式；不站队营销 — 选型看现有引擎+读写模式，趋势是引擎多格式兼容 (evidence:[T02-S011, T02-S061])。
- **维护者背景**: Track 01 — Ryan Blue (Iceberg) / Vinoth Chandar (Hudi) / Matei Zaharia (Delta)。
- **可信度**: high · **Decay**: low-medium (格式之争+互操作演进中)

### 7. DuckDB
- **One-liner**: DuckDB — 进程内 OLAP 数据库 (CWI Amsterdam)，"big data is dead" 时代单机分析默认。
- **Tier**: 必备 (新兴跨界) · **Maintainer**: DuckDB Labs — https://duckdb.org · **License**: open (MIT)
- **Maturity signals**: GitHub stars 38.3k (2026-05-20)；1.x 稳定；活跃 healthy。
- **典型使用场景**: 单机查 Parquet/CSV (GB-数十 GB)；本地 dev/CI 跑 dbt；嵌入式分析。
- **不适合 / 替代**: 真 TB+ / 多用户并发 → 云数仓/Spark；分布式 → 不是 DuckDB 的活。
- **维护者背景**: Track 01 — Hannes Mühleisen / Mark Raasveldt；Jordan Tigani (MotherDuck, 'Big Data is Dead' evidence:[T02-S020])。
- **可信度**: high · **Decay**: medium (生态高速演进)

> 必备层另含 **Parquet** (列存落盘默认 evidence:[T02-S059])、**Arrow** (内存交换标准 evidence:[T02-S060])、**对象存储 S3/GCS/ADLS**、**EL 工具 Fivetran/Airbyte/dlt**、**SQL+Python** — 见总览表与场景特化层。

---

## 场景特化 (7 类, 特定子方向用 — 每类含「适合/不适合」分界)

### 类 (1) 摄取-EL-CDC
- **Fivetran** — 托管 EL，connector 多+免运维，**适合**：团队小/connector 是商品化的 SaaS 源；**不适合**：高频大表按行计费成本爆炸、要 code-first 控制。(evidence:[T02-S035])
- **Airbyte** (21.3k★) — 开源 EL，**适合**：自托管+长尾 connector；**不适合**：要极致稳定的核心管道 (社区 connector 质量参差)。(evidence:[T02-S034])
- **dlt** (5.3k★) — 声明式 Python EL 库，**适合**：code-first/嵌入编排器；**不适合**：非工程团队要 UI。(evidence:[T02-S036])
- **Debezium** (12.7k★) — CDC 事实标准 (binlog/WAL→Kafka)，**适合**：低延迟数据库变更捕获；**不适合**：批量全表抽取 (用 EL)。(evidence:[T02-S038, T02-S039])
- **Meltano / Kafka Connect / SeaTunnel** (中国一手, 9.3k★ evidence:[T02-S054]) — Singer 生态 / Kafka 内置集成 / 国产批流集成。
- **生产案例**: Debezium binlog CDC 是 lakehouse 增量摄取主流路径 (evidence:[T02-S039, T02-S065])。

### 类 (2) 存储-表格式-lakehouse
- **Iceberg / Delta / Hudi** — 见必备层卡片 6。Iceberg 因中立性成事实交换格式 (evidence:[T02-S011])。
- **Parquet / ORC** — 列存落盘；Parquet 通用默认，ORC 偏 Hive 生态。(evidence:[T02-S059])
- **Arrow** — 内存列存交换，引擎间零拷贝。(evidence:[T02-S060])
- **lakeFS** — 数据湖 git-like 版本控制，**适合**：要 branch/rollback 数据；**不适合**：表格式自带 time-travel 已够 (Iceberg snapshot)。
- **资深分界**: 选 Iceberg 当不想绑 Databricks；选 Delta 当已在 Databricks；选 Hudi 当 upsert/CDC 是主模式。

### 类 (3) 转换-建模
- **dbt** — 见必备卡片 1。SQL-first ELT 默认。
- **SQLMesh** (3.1k★) — **适合**：要列级血缘+无状态虚拟环境+跨引擎；**不适合**：团队已重度 dbt 投入、生态依赖。(evidence:[T02-S040, T02-S041])
- **Spark** (43.3k★) — **适合**：大规模/重 Python 转换；**不适合**：数据塞得进单机。
- **Dataform** — BigQuery 原生 SQL 转换 (Google 收购)，**适合**：纯 GCP 栈。
- **资深分界**: SQL 能表达的转换默认 dbt；非 SQL 重逻辑才上 Spark/Polars。

### 类 (4) 编排
- **Airflow** (45.5k★) — 见必备卡片 2。任务/cron 心智，生态最广。
- **Dagster** (15.5k★) — **适合**：asset/data-aware 调度 + 软件定义资产 + 强本地开发；**不适合**：团队只要简单 cron。(evidence:[T02-S021, T02-S022])
- **Prefect** (22.4k★) — **适合**：Pythonic 动态流 + 轻量；**不适合**：要 Airflow 级生态。(evidence:[T02-S023])
- **Kestra** (26.9k★) — 声明式 YAML 编排；**Mage** (8.7k★) — notebook-like 编排。(evidence:[T02-S055, T02-S056])
- **DolphinScheduler** (14.3k★, 中国一手 WhaleOps/代立冬) — **适合**：可视化 DAG + 中国 stack；**不适合**：code-first 优先团队。(evidence:[T02-S053])
- **资深分界**: 新项目若以「数据资产正确性」为中心 → Dagster；既有大规模 cron 生态 → Airflow。

### 类 (5) 批流-实时 OLAP
- **Kafka** (32.6k★) — 流平台底座，见必备卡片 4。
- **Flink** (26k★) — **适合**：有状态流计算 + exactly-once + 复杂窗口 (中国一手伍翀/莫问)；**不适合**：分钟级批足够时 (流复杂度+成本远高于批)。(evidence:[T02-S025, T02-S026])
- **Spark Structured Streaming** — **适合**：已有 Spark 栈的微批流；**不适合**：要真亚秒级。
- **Materialize / RisingWave** (9k★) — 流式 SQL 物化视图增量维护，**适合**：增量更新的实时派生表；**不适合**：一次性批查。(evidence:[T02-S044])
- **ClickHouse** (47.5k★) / **Druid / Pinot** — 实时 OLAP 亚秒查询，**适合**：高基数/大宽表/实时仪表；**不适合**：复杂 join 重事务。(evidence:[T02-S027, T02-S028])
- **StarRocks** (11.7k★) / **Doris** (15.4k★, 中国一手) — 实时数仓，**适合**：join-heavy 实时分析 + 中国 stack。(evidence:[T02-S051, T02-S052])
- **生产案例**: 「批 vs 流不是越实时越好」— 多数分析分钟/小时级批足够，真需亚秒 (风控/推荐/监控) 才上流 (evidence:[T02-S026])。

### 类 (6) 数仓-查询引擎
- **Snowflake / BigQuery / Databricks SQL** — 见必备卡片 5。托管云数仓。
- **Trino / Presto** (Trino 12.8k★) — **适合**：跨源联邦查询不搬数 + lakehouse 上查 Iceberg；**不适合**：要托管零运维 → Snowflake/Starburst。(evidence:[T02-S029, T02-S030])
- **DuckDB** (38.3k★) / **Polars** (38.5k★) — 单机引擎复兴，**适合**：数据塞得进单机；**不适合**：真分布式 (evidence:[T02-S016, T02-S018])。
- **Dremio** — lakehouse 查询加速。
- **资深分界**: 默认从「数据多大」反推 — 单机 (DuckDB) → 单数仓 (Snowflake/BQ) → 联邦 (Trino) → 分布式 (Spark)。

### 类 (7) 数据质量-治理-DataOps
- **dbt tests** — 内建测试，第一道防线 (unique/not_null/relationships)。(evidence:[T02-S004])
- **Great Expectations** (11.5k★) — **适合**：复杂期望套件 + 非 dbt 栈；**不适合**：纯 dbt 项目轻量需求 (用 dbt tests/Elementary)。(evidence:[T02-S045, T02-S046])
- **Soda** (2.4k★) — 声明式 YAML 数据质量检查 (SodaCL)。(evidence:[T02-S058])
- **Elementary** — dbt-native 可观测性，**适合**：已用 dbt 想加监控。(evidence:[T02-S062])
- **Monte Carlo** — data observability 品类创造者 (Barr Moses, 'data downtime')，**适合**：企业级端到端 + 自动异常检测；**不适合**：小团队预算敏感。(evidence:[T02-S049])
- **DataHub** (11.9k★) / **OpenMetadata** (14k★) / **Amundsen** / **Unity Catalog** — catalog/血缘/治理，**适合**：跨团队数据发现 + 列级血缘 + PII 分类。(evidence:[T02-S047, T02-S048, T02-S057])
- **生产案例**: 「没有数据质量测试就上生产 = 数据沼泽」, 数据平台是 garbage-in-garbage-out 放大器 (evidence:[T02-S049])。

---

## 新兴/实验层（近 12 月起势, 标 experimental, decay high）

### N1. SQLMesh
- **One-liner**: SQLMesh — 带列级血缘 + 无状态虚拟环境 + 跨引擎的 dbt 替代 (Tobiko Data)。
- **Maturity signals**: GitHub stars 3.1k (2026-05-20)；活跃 healthy。**stability: experimental**。
- **早期采用者**: 数据社区中作为 dbt 的「正确性优先」竞品被频繁对比 (evidence:[T02-S040, T02-S041])。
- **不适合**: 已重度 dbt 投入的团队迁移成本高。
- **Decay**: high (12 月内被显著改变概率 >40% — dbt 也在快速演进 Fusion engine 回应)

### N2. Apache Paimon
- **One-liner**: Paimon — Flink 原生 streaming lakehouse 表格式 (前 Flink Table Store, 阿里起源)。
- **Maturity signals**: GitHub stars 3.3k (2026-05-20)；活跃 healthy。**stability: experimental**。
- **早期采用者**: 中国流批一体/实时数仓团队 (evidence:[T02-S042, T02-S043])。
- **Decay**: high (与 Iceberg/Hudi streaming 能力竞争中)

### N3. RisingWave
- **One-liner**: RisingWave — Postgres-wire 兼容的流式 SQL 数据库，物化视图增量维护。
- **Maturity signals**: GitHub stars 9k (2026-05-20)；活跃 healthy。**stability: experimental**。
- **不适合**: 成熟有状态复杂流 → Flink (生态更全)。
- **Decay**: high (evidence:[T02-S044])

### N4. dlt (dlthub)
- **One-liner**: dlt — 声明式 Python EL 库，schema 自动演进 + code-first 摄取。
- **Maturity signals**: GitHub stars 5.3k (2026-05-20)；活跃 healthy。**stability: experimental**。
- **早期采用者**: 反「自建 vs Fivetran」build-vs-buy 的轻量 code-first 路径 (evidence:[T02-S036, T02-S037])。
- **Decay**: high

### N5. DuckDB / MotherDuck（跨界，必备层亦列）
- **One-liner**: MotherDuck — DuckDB 的云协同 (Jordan Tigani, 'Big Data is Dead' 反过早分布式)。
- **Maturity signals**: DuckDB 38.3k★ (2026-05-20)；MotherDuck 商用云。**stability: emerging-fast**。
- **Decay**: high (生态高速演进 evidence:[T02-S020])

### N6-N9. 表格式/catalog 互操作 + 数据契约
- **Iceberg REST catalog / Polaris** — 中立 catalog 标准让引擎解耦 (evidence:[T02-S011, T02-S061])。**Decay**: high。
- **Apache XTable / Delta UniForm** — 表格式互操作 (Iceberg↔Delta↔Hudi 元数据转译)，回应「vendor lock-in」(evidence:[T02-S061])。**Decay**: high。
- **数据契约工具 (Gable.ai / data contracts)** — Chad Sanderson 倡导，shift-left schema 治理把隐式耦合显性化 (evidence:[T02-S068])。**Decay**: high。

---

## 选型决策树（7 branches，每节点带 evidence）

### 决策树: 你的核心问题是什么？

#### Branch 1: 「我的数据真的大到需要分布式吗？」（最该先问的问题）
→ **数据 < 单机内存/几十 GB**: 推荐 **DuckDB / Polars**（单机引擎，零集群运维，CI/dev 极快）。
→ **数据 GB-TB 单源、要 serving + BI**: 推荐 **单一云数仓 (Snowflake/BigQuery)**。
→ **真 TB-PB 多源重 Python**: 才上 **Spark**。
→ **不推荐**: 为简历/显得专业默认上 Spark/Hadoop 集群 = resume-driven，多数公司瓶颈是建模+质量+成本不是缺分布式。(evidence:[T02-S020, T02-S016])
→ 真实信号: 'Big Data is Dead' (Jordan Tigani/MotherDuck, 业内观察) — 中位数公司单表 < 几十 GB。

#### Branch 2: 摄取层 — 自建 vs 买（build-vs-buy）
→ **commodity SaaS 源 + 小团队**: 推荐 **Fivetran**（免运维，按量买时间）(evidence:[T02-S035])。
→ **要 code-first + 嵌编排器 + 省钱**: 推荐 **dlt** 或 **Airbyte 自托管** (evidence:[T02-S036, T02-S034])。
→ **数据库低延迟变更**: 推荐 **Debezium CDC** (binlog/WAL→Kafka) (evidence:[T02-S038])。
→ **不推荐**: 从零自建通用 ingestion 框架去对付长尾 SaaS API — 维护黑洞，'zero-ETL' 厂商话术不消复杂度只转移。

#### Branch 3: 转换/建模 — SQL 还是代码？
→ **SQL 能表达**: 推荐 **dbt**（事实标准 + 测试 + 血缘 + 文档）(evidence:[T02-S003, T02-S005])。
→ **要列级血缘/无状态虚拟环境/跨引擎**: 考虑 **SQLMesh**（experimental）(evidence:[T02-S040])。
→ **非 SQL 重逻辑/ML 特征**: 推荐 **Spark / Polars**。
→ **不推荐**: 把 Jupyter notebook 当生产转换（无版本/无测试/无调度/无幂等）。

#### Branch 4: 编排器选型
→ **既有大规模 cron + 最广生态**: 推荐 **Airflow** (evidence:[T02-S001])。
→ **以「数据资产正确性」为中心 + 强本地开发**: 推荐 **Dagster** (asset-based) (evidence:[T02-S021])。
→ **轻量 Pythonic 动态流**: 推荐 **Prefect** (evidence:[T02-S023])。
→ **中国 stack + 可视化 DAG**: 推荐 **DolphinScheduler** (evidence:[T02-S053])。
→ 共同约束: task 必须**幂等 + 可重跑**（Maxime 'Functional Data Engineering'），否则回填即灾难。(evidence:[T02-S050])

#### Branch 5: 批 vs 流 — 你真的需要实时吗？
→ **分钟/小时级足够 (多数分析)**: 用 **批 (dbt + 编排器)**，别上流。
→ **真亚秒级 (风控/推荐/监控)**: 上 **Kafka + Flink**（有状态/exactly-once）(evidence:[T02-S025])。
→ **增量物化派生表**: **RisingWave / Materialize**（流式 SQL）(evidence:[T02-S044])。
→ **不推荐**: Lambda 架构维护两套代码（已知痛点）；为「实时更高级」全都上流。(evidence:[T02-S026])

#### Branch 6: 实时 OLAP 引擎
→ **高基数/大宽表/单表聚合**: **ClickHouse** (evidence:[T02-S027])。
→ **事件/时序 + 高并发点查**: **Druid / Pinot**。
→ **join-heavy 实时分析 (+中国 stack)**: **StarRocks / Doris** (evidence:[T02-S051, T02-S052])。
→ **不推荐**: 拿实时 OLAP 当事务库或复杂 join 引擎。

#### Branch 7: lakehouse 表格式（避 vendor lock-in）
→ **不想绑 Databricks + 要中立生态**: **Iceberg**（隐藏分区 + REST catalog 解耦）(evidence:[T02-S010, T02-S011])。
→ **已在 Databricks 栈**: **Delta Lake**（生态最强）(evidence:[T02-S012])。
→ **upsert/CDC 增量是主模式**: **Hudi**（Uber 起源）(evidence:[T02-S014, T02-S065])。
→ **要跨格式互操作**: **XTable / UniForm**（experimental）(evidence:[T02-S061])。
→ 原则: 不站队营销，选型看现有引擎 + 读写模式 + 引擎兼容；趋势是引擎多格式兼容。

---

## 避坑清单（≥5）

- ❌ **不要为「显得专业」过早上 Spark/分布式**：多数数据集塞得进 DuckDB/单数仓，'Big Data is Dead'；上分布式前先问"我的数据真的大到需要它吗"。瓶颈通常是建模+质量+成本不是缺分布式。(evidence:[T02-S020, T02-S016])
- ❌ **不要无视 small files problem**：流/微批/不 compaction 在对象存储堆出海量小文件 → 元数据爆炸 + 查询慢 + 成本涨；表格式 compaction (Iceberg/Hudi) 要主动调。(evidence:[T02-S014, T02-S010])
- ❌ **不要 SELECT \* 全表扫**：云数仓/Spark 按扫描量/用量计费，无分区裁剪 + 无谓词下推 + 全量重算 = 账单指数爆炸；用 incremental model + 分区 + 列裁剪。(evidence:[T02-S032, T02-S005])
- ❌ **不要无脑自建 ingestion 对付长尾 SaaS API**（build-vs-buy 误判）：commodity 源用 Fivetran/dlt，自建通用框架是维护黑洞；'zero-ETL'/'NoETL' 厂商话术不消复杂度只转移。(evidence:[T02-S035, T02-S036])
- ❌ **不要把 Jupyter notebook 当生产 pipeline**：无版本/无测试/无调度/无幂等，是探索工具不是生产；生产化必须进编排器 + 代码仓 + CI。(evidence:[T02-S050])
- ❌ **不要把 Modern Data Stack 工具堆砌当架构**：10 个 SaaS 拼起来 ≠ 好数据平台，集成+成本+治理债会反噬；先有数据模型+质量纪律再选工具。(evidence:[T02-S005, T02-S061])
- ❌ **不要为追潮流牺牲中立性 (vendor lock-in)**：选表格式/catalog 看引擎兼容与可迁移性 (Iceberg 中立性 + XTable 互操作)，不是"哪个最火"；闭源数仓锁定要算迁出成本。(evidence:[T02-S011, T02-S061])
- ❌ **不要没数据质量测试就上生产**：数据平台是 garbage-in-garbage-out 放大器，错误数据静默流向 dashboard/ML/决策危害远超应用 bug；dbt tests / GX / 数据契约是基线不是 nice-to-have。(evidence:[T02-S045, T02-S049])

---

## Phase 2 提炼提示

**反复出现 ≥3 source 都强调的「工具选型原则」**（候选 playbook 规则）:
- 默认从「数据多大」反推引擎：单机 (DuckDB) → 单数仓 → 联邦 (Trino) → 分布式 (Spark)，过早分布式是反模式 (出现于: T02-S020 / T02-S016 / T02-S005)。
- task 必须幂等 + 可重跑，是 pipeline 第一公民 (出现于: T02-S050 / T02-S001 / T02-S021)。
- SQL 能表达的转换默认 dbt，非 SQL 重逻辑才上 Spark/Polars (出现于: T02-S003 / T02-S005 / T02-S006)。
- 表格式选型看引擎兼容 + 可迁移性而非热度，中立性 (Iceberg) + 互操作 (XTable) 抗 lock-in (出现于: T02-S010 / T02-S011 / T02-S061)。

**显著的工具流派分裂**（候选 智识谱系条目）:
- **过早分布式派 (Hadoop/Spark-everything) vs 单机复兴派 (DuckDB/Polars 'big data is dead')**（代表工具: Spark / Hadoop vs DuckDB / Polars; 代表人物: Track 01 — Jordan Tigani / Hannes Mühleisen）。
- **托管派 (Fivetran + Snowflake + Modern Data Stack) vs code-first 派 (dlt + Iceberg + 自托管)**（build-vs-buy + lock-in 取舍）。
- **任务编排派 (Airflow, cron 心智) vs 资产编排派 (Dagster, data-aware/软件定义资产)**（代表人物: Track 01 — Maxime Beauchemin vs Nick Schrock）。
- **批优先 vs 流优先 (Lambda vs Kappa/streaming lakehouse)**（代表工具: dbt+批 vs Flink/Paimon; 代表人物: Jay Kreps / Tyler Akidau）。
- **SQL-first 转换 (dbt) vs 正确性优先 (SQLMesh 列级血缘/虚拟环境)**。

**新兴工具信号**:
- 当前活跃/上升新工具数: 9 (SQLMesh / Paimon / RisingWave / dlt / MotherDuck / Iceberg REST catalog-Polaris / XTable-UniForm / 数据契约工具 / Polars)。
- 出现 → 主流速度估计: 18-36 个月（dbt 用约 4-5 年成事实标准；DuckDB 约 3 年从 niche 到必备跨界；Iceberg 约 4-6 年成中立交换格式）。

**冷僻/信号薄弱**:
- 必备层 13 个 (≥3 ✓)；场景特化 7 类约 30 工具 (≥5 ✓)；新兴层 9 个 (≥2 ✓)。
- 一手率：manifest 68 条中 verified_primary (github root) + surrogate_primary (vendor docs) 占 ≥95%，无 blacklisted 入表。**信号充足，非冷僻行业。**
- 注意：本 track 在 wave 1 seed (01/04/05/06) 缺失情况下独立完成，seed 取自 intake.json figures/canon/subdomain 候选；建议 Phase 1.5 在 wave 1 落盘后回灌交叉校验 (尤其 Track 01 figures ↔ 工具 maintainer 关联)。
- proprietary 工具 (Snowflake/BigQuery/Redshift/Monte Carlo/Fivetran) 来源以 vendor docs (surrogate_primary) 为主，mental_model 类 claim 需 ≥2 source consensus，已避免单源带货。
