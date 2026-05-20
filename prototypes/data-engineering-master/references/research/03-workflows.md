# Track 03 — Workflows / SOPs: Data Engineering (数据工程)

> Phase 1 wave 3 subagent 输出。Industry = **Data Engineering / 数据工程**。locale = **en** (en-primary, zh-CN secondary)。
> 调研日期 last_checked 全文 = 2026-05-20。
> seed: Wave-1 outputs 01-figures.md / 02-tools.md / 04-canon.md (磁盘已存在)。共抽出 ~28 个 workflow 片段, 拼成 **8 个完整 workflow**。
> **格式契约 (cli_writer.py)**: 每个 workflow heading = `### N. Title` (三井号 + 整数 + `. ` + 标题)。`**入门 SOP**:` 后紧跟 `1. 2. 3.` 内联编号列表。`**资深路径**:` 含 跳过/优化/额外。`**近期变化**:` 含 low/medium/high decay。

---

## Source Manifest

> bucket 由 `tools/research/source_verifier.py classify` 跑出。vendor/project docs + 作者 blog (.io/.com/.org/.dev/.apache.org/medium 作者域) → 人工标 `surrogate_primary` + note 含 literal **"vendor docs"** (任务规则)。`github.com/{org}/{repo}` root → 自动 `verified_primary`。arxiv/.edu/.gov/research.google/usenix/cidrdb/linkedin-eng → 自动 `verified_primary`。Reddit/SO → `reference`。黑名单 URL 不入表。

| source_id | url | bucket | last_checked | author/host | one-line note |
|-----------|-----|--------|--------------|-------------|---------------|
| T03-S001 | https://docs.getdbt.com/best-practices/how-we-structure/1-guide-overview | surrogate_primary | 2026-05-20 | dbt Labs | vendor docs (厂商一手 — staging/intermediate/marts 项目结构) |
| T03-S002 | https://docs.getdbt.com/docs/build/incremental-models | surrogate_primary | 2026-05-20 | dbt Labs | vendor docs (厂商一手 — incremental model + merge) |
| T03-S003 | https://docs.getdbt.com/docs/build/data-tests | surrogate_primary | 2026-05-20 | dbt Labs | vendor docs (厂商一手 — dbt tests 质量门禁) |
| T03-S004 | https://docs.getdbt.com/docs/build/sources | surrogate_primary | 2026-05-20 | dbt Labs | vendor docs (厂商一手 — source freshness) |
| T03-S005 | https://www.getdbt.com/blog/what-is-analytics-engineering | surrogate_primary | 2026-05-20 | dbt Labs / Tristan Handy | vendor docs (厂商一手 — ELT/analytics engineering) |
| T03-S006 | https://maximebeauchemin.medium.com/functional-data-engineering-a-modern-paradigm-for-batch-data-processing-2327ec32c42a | surrogate_primary | 2026-05-20 | Maxime Beauchemin | vendor docs (作者一手 — 幂等/不可变分区/可重跑) |
| T03-S007 | https://www.startdataengineering.com/post/code-patterns/ | surrogate_primary | 2026-05-20 | Joseph Machado | vendor docs (作者一手 — pipeline code pattern/幂等教程) |
| T03-S008 | https://airflow.apache.org/docs/apache-airflow/stable/core-concepts/dags.html | surrogate_primary | 2026-05-20 | Apache Airflow | vendor docs (Apache 一手 — DAG 依赖/重试/调度) |
| T03-S009 | https://airflow.apache.org/docs/apache-airflow/stable/authoring-and-scheduling/backfill.html | surrogate_primary | 2026-05-20 | Apache Airflow | vendor docs (Apache 一手 — backfill 回填) |
| T03-S010 | https://docs.dagster.io/guides/build/assets/defining-assets | surrogate_primary | 2026-05-20 | Dagster Labs | vendor docs (厂商一手 — software-defined assets/data-aware) |
| T03-S011 | https://docs.dagster.io/guides/automate/declarative-automation | surrogate_primary | 2026-05-20 | Dagster Labs | vendor docs (厂商一手 — declarative automation/freshness) |
| T03-S012 | https://debezium.io/documentation/reference/stable/tutorial.html | surrogate_primary | 2026-05-20 | Debezium / Gunnar Morling | vendor docs (项目一手 — CDC binlog/WAL→Kafka) |
| T03-S013 | https://kafka.apache.org/documentation/#connect | surrogate_primary | 2026-05-20 | Apache Kafka | vendor docs (Apache 一手 — Kafka Connect 摄取) |
| T03-S014 | https://iceberg.apache.org/docs/latest/maintenance/ | surrogate_primary | 2026-05-20 | Apache Iceberg | vendor docs (Apache 一手 — compaction/expire snapshots/小文件) |
| T03-S015 | https://iceberg.apache.org/docs/latest/evolution/ | surrogate_primary | 2026-05-20 | Apache Iceberg | vendor docs (Apache 一手 — schema/partition evolution/隐藏分区) |
| T03-S016 | https://delta.io/blog/2023-01-25-delta-lake-small-file-compaction-optimize/ | surrogate_primary | 2026-05-20 | Delta Lake | vendor docs (项目一手 — OPTIMIZE/小文件 compaction) |
| T03-S017 | https://flink.apache.org/what-is-flink/flink-applications/ | surrogate_primary | 2026-05-20 | Apache Flink | vendor docs (Apache 一手 — windowing/state/event-time) |
| T03-S018 | https://nightlies.apache.org/flink/flink-docs-stable/docs/concepts/time/ | surrogate_primary | 2026-05-20 | Apache Flink | vendor docs (Apache 一手 — watermark/event-time/exactly-once) |
| T03-S019 | https://www.oreilly.com/radar/questioning-the-lambda-architecture/ | surrogate_primary | 2026-05-20 | Jay Kreps / O'Reilly | vendor docs (作者一手 — Kappa vs Lambda 取舍) |
| T03-S020 | https://greatexpectations.io/expectations/ | surrogate_primary | 2026-05-20 | Great Expectations | vendor docs (厂商一手 — expectation suite/数据校验) |
| T03-S021 | https://dataproducts.substack.com/p/the-shift-left-data-manifesto | verified_primary | 2026-05-20 | Chad Sanderson | newsletter author host — shift-left 数据契约 manifesto |
| T03-S022 | https://www.montecarlodata.com/blog-what-is-data-observability/ | surrogate_primary | 2026-05-20 | Barr Moses / Monte Carlo | vendor docs (厂商一手 — 五维 freshness/volume/schema/distribution/lineage) |
| T03-S023 | https://docs.confluent.io/platform/current/schema-registry/index.html | surrogate_primary | 2026-05-20 | Confluent | vendor docs (厂商一手 — schema registry/兼容性) |
| T03-S024 | https://docs.getdbt.com/docs/deploy/ci-jobs | surrogate_primary | 2026-05-20 | dbt Labs | vendor docs (厂商一手 — CI job/slim CI/state:modified) |
| T03-S025 | https://docs.getdbt.com/docs/build/environments | surrogate_primary | 2026-05-20 | dbt Labs | vendor docs (厂商一手 — dev/staging/prod 环境隔离) |
| T03-S026 | https://cloud.google.com/bigquery/docs/best-practices-costs | surrogate_primary | 2026-05-20 | Google Cloud | vendor docs (厂商一手 — 分区裁剪/扫描量/成本治理) |
| T03-S027 | https://github.com/DataTalksClub/data-engineering-zoomcamp | verified_primary | 2026-05-20 | DataTalks.Club | github root (auto primary) — 端到端管道实操课 |
| T03-S028 | https://www.cidrdb.org/cidr2021/papers/cidr2021_paper17.pdf | verified_primary | 2026-05-20 | Armbrust/Zaharia / CIDR | Lakehouse CIDR 2021 — 湖仓+开放表格式奠基 |
| T03-S029 | https://www.databricks.com/glossary/medallion-architecture | surrogate_primary | 2026-05-20 | Databricks | vendor docs (厂商一手 — bronze/silver/gold medallion) |
| T03-S030 | https://hudi.apache.org/docs/write_operations/ | surrogate_primary | 2026-05-20 | Apache Hudi / Vinoth Chandar | vendor docs (项目一手 — upsert/merge-on-read 增量) |
| T03-S031 | https://docs.getdbt.com/docs/build/snapshots | surrogate_primary | 2026-05-20 | dbt Labs | vendor docs (厂商一手 — SCD type-2 snapshot) |
| T03-S032 | https://motherduck.com/blog/big-data-is-dead/ | surrogate_primary | 2026-05-20 | Jordan Tigani / MotherDuck | vendor docs (作者一手 — 反过早分布式) |
| T03-S033 | https://www.reddit.com/r/dataengineering/ | reference | 2026-05-20 | r/dataengineering | UGC 社区 — 从业者实操痛点二阶验证 |
| T03-S034 | https://www.thoughtworks.com/radar | surrogate_primary | 2026-05-20 | ThoughtWorks | vendor docs (技术趋势权威 — Technology Radar) |
| T03-S035 | https://docs.getdbt.com/best-practices/best-practice-workflows | surrogate_primary | 2026-05-20 | dbt Labs | vendor docs (厂商一手 — PR 测试门禁/部署 best practice) |

---

## 总览（按 decay risk 分组）

### High decay (12-month-class) — 1 个
| Workflow | Trigger | Output | Last_updated | 资深差异 |
|---------|---------|--------|-------------|---------|
| 8. DataOps / CI-CD + 成本治理 | 团队要把 pipeline 当软件部署 + 账单失控 | 多环境 + PR 门禁 + 部署流水 + 成本护栏 | 2026-05 | 跳过手工 promote / 优化 slim CI state:modified / 额外 cost 异常告警 |

### Medium decay — 4 个
| Workflow | Trigger | Output | Last_updated | 资深差异 |
|---------|---------|--------|-------------|---------|
| 2. CDC / 增量摄取 | 源库高频变更要低延迟同步 | Debezium→Kafka→幂等 merge 增量表 | 2026-05 | 跳过自建 connector / 优化幂等 upsert / 额外 schema 漂移处理 |
| 5. lakehouse 表格式落地 | 对象存储上要 ACID + 演进 + 治理 | Iceberg/Delta 表 + compaction 计划 | 2026-05 | 跳过手工分区 / 优化隐藏分区+compaction / 额外 snapshot 过期 |
| 6. 流处理管道 | 真亚秒级实时需求 (风控/推荐/监控) | Kafka→Flink exactly-once 有状态管道 | 2026-05 | 跳过 Lambda 双链路 / 优化 watermark+checkpoint / 额外背压治理 |
| 7. 数据质量门禁 + 数据契约 | 错误数据静默流向 BI/ML | dbt tests + GX + 契约 + 五维监控 | 2026-05 | 跳过末端救火 / 优化 shift-left 契约 / 额外 freshness+anomaly |

### Low decay — 3 个
| Workflow | Trigger | Output | Last_updated | 资深差异 |
|---------|---------|--------|-------------|---------|
| 1. 构建一条 ELT 管道 | 新数据源要进数仓供分析 | source→EL→raw→dbt→serve 全链路 | 2026-05 | 跳过自建 EL / 优化 incremental / 额外幂等+contract |
| 3. 维度建模 + dbt 项目结构 | 杂乱 SQL 要变成可维护建模层 | staging/intermediate/marts + SCD + tests | 2026-05 | 跳过过度规范化 / 优化 OBT 取舍 / 额外一致性维度 |
| 4. 编排 DAG 设计 | 多步骤管道要调度+依赖+回填 | 幂等 DAG + 重试 + backfill 能力 | 2026-05 | 跳过 cron 心智 / 优化 data-aware 调度 / 额外幂等回填 |

---

## Workflows 详细卡片

### 1. 构建一条 ELT 管道

- **One-liner**: 从一个新数据源到「可被 BI/分析直接消费的建模表」的端到端最短闭环 — source → 抽取加载 (EL) → land raw → dbt transform → serve。 (evidence: [T03-S005, T03-S027])
- **Trigger**: 业务方要分析一个尚未进数仓的数据源 (SaaS API / 业务库 / 文件)，或现有报表口径要从手工 SQL 升级为可维护管道。 (evidence: [T03-S005])
- **Output**: 一条可调度、可重跑、有测试的管道 — 原始层 (raw) + 转换层 (staging/marts) + serving 表 (BI/dashboard 直连)。 (evidence: [T03-S001, T03-S027])
- **入门 SOP**:
  1. 选 EL 工具抽数落 raw：commodity SaaS 源用 Fivetran/Airbyte，code-first 用 dlt，原样落 raw schema 不做转换 (跳过 = 转换混进抽取层，源 schema 一变全链路断)。 (evidence: [T03-S005])
  2. 在数仓建 raw landing 层：保留源结构 + 加载时间戳 + 不可变 (append/overwrite by partition)，作为唯一真相源 (跳过 = 直接转换无 raw 备份，回填/排错时无法重放)。 (evidence: [T03-S006])
  3. 写 dbt staging 模型：1:1 清洗 raw (改名/类型/去重)，每源一个 staging，view 物化 (跳过 = 业务逻辑直接堆在源表上，无清洗隔离层，复用即复制粘贴)。 (evidence: [T03-S001])
  4. 写 dbt marts/转换：join + 聚合成业务事实/维度，table/incremental 物化，按消费方建模 (跳过 = BI 直接 query raw，每个 dashboard 各写一份口径，指标不一致)。 (evidence: [T03-S001, T03-S005])
  5. 加 dbt tests + 调度：unique/not_null/relationships + source freshness，进编排器每日跑 (跳过 = 无测试上生产 = 数据沼泽，错误数据静默进 dashboard)。 (evidence: [T03-S003, T03-S004])
- **资深路径**: **跳过** 从零自建通用 ingestion 框架去对付长尾 SaaS API（维护黑洞，commodity 源直接 buy Fivetran/dlt，"zero-ETL" 话术不消复杂度只转移）；**优化** 把全量重算的 mart 改成 incremental model（只算新增分区，扫描量/成本砍一个量级）+ 大表 raw 直接落 lakehouse 表格式而非数仓内表；**额外** 在 source 层挂数据契约 + freshness 监控（schema is API，上游删字段静默打爆下游），并把 medallion bronze/silver/gold 质量契约显式化而非机械三段。 (evidence: [T03-S002, T03-S021, T03-S029, T03-S032])
- **近期变化**: **low** decay — 行业稳态。ELT (vs ETL) 范式 5+ 年稳定，dbt + 云数仓 + EL 工具的四段式是事实标准。近 12 月增量变化：2025-05 dbt Fusion engine (Rust 重写原生 SQL 理解) 推动 staging 层开发体验，但管道骨架不变；dlt 等 code-first EL 在新项目中替代部分 Fivetran (成本驱动)。 (evidence: [T03-S005, T03-S032])
- **典型耗时**: 入门 SOP 1 源约 1-3 天；资深路径熟练后单源 0.5-1 天 (模板化 staging + 复用 macro)。
- **关键工具**: Fivetran/Airbyte/dlt (EL，必备/medium decay)、dbt (转换，必备)、云数仓 Snowflake/BigQuery (serving，必备)、Airflow/Dagster (调度)。
- **关键人物**: Tristan Handy (Track 01 — analytics engineering/ELT 运动)；Maxime Beauchemin (Track 01 — 幂等/raw 不可变)。
- **常见失败模式**:
  - 转换逻辑混进 EL 层：源 schema 一变整条管道断 → 严格分离 EL (只搬不变) 与 T (dbt 内变换)。**CLI 自检**: "Did you load raw 原样落地, with transform ONLY in dbt? Mixing them = source schema change breaks everything."
  - 用 Fivetran 抽高频大表按行计费 → 月底账单爆炸，几个 TB 同步花掉数万刀 → 高频大表改 CDC (workflow 2) 或 incremental。**CLI 自检**: "Is any high-volume table billed per-row by Fivetran? Switch to CDC/incremental before the bill explodes."
  - 全量重算 mart 当默认 → 数据涨了之后每日跑数小时 + 扫描量计费失控 → 早期就用 incremental + 分区。**CLI 自检**: "Are marts full-refresh by default? Convert to incremental once data > a few GB."
  - notebook 当生产管道 → 无版本/测试/调度/幂等 → 必须进 dbt + 代码仓 + 编排器。**CLI 自检**: "Is any step a Jupyter notebook run by hand? Notebooks are exploration, NOT production."
- **来源** (≥3):
  - [surrogate_primary] T03-S005 dbt analytics engineering (ELT 范式), collected 2026-05-20
  - [surrogate_primary] T03-S001 dbt how-we-structure (staging/marts)
  - [verified_primary] T03-S027 Data Engineering Zoomcamp (端到端实操)
  - [surrogate_primary] T03-S006 Functional Data Engineering (raw 不可变/幂等)
- **Last_updated**: 2026-05-20
- **Decay risk**: low (ELT 四段式范式稳态，工具示例会旧但骨架不变)

---

### 2. CDC / 增量摄取

- **One-liner**: 从源数据库捕获行级变更并以幂等方式增量落到数仓/湖 — Debezium/Kafka Connect 读 binlog/WAL → Kafka → 增量 merge (idempotent upsert)，而非每日全表抽取。 (evidence: [T03-S012, T03-S030])
- **Trigger**: 源业务库 (MySQL/Postgres) 高频变更，全表抽取太慢/太贵或延迟不可接受；需要近实时同步到分析侧或下游服务。 (evidence: [T03-S012])
- **Output**: 一条捕获 insert/update/delete 的增量管道 + 目标表 (含软删标记/版本)，重跑/回填不产生重复行。 (evidence: [T03-S012, T03-S030])
- **入门 SOP**:
  1. 配 Debezium connector 读源库 binlog/WAL：建 replication slot/开 binlog，定 server/database/table 白名单 (跳过 = 用 query-based 轮询，漏掉 delete + 给源库加压)。 (evidence: [T03-S012])
  2. 变更事件写入 Kafka topic：每表一 topic，事件含 before/after/op (c/u/d) + 时间戳 (跳过 = 直接 sink 不经 Kafka，无 replay buffer，下游故障即丢数据)。 (evidence: [T03-S012, T03-S013])
  3. 做一次初始快照 (snapshot)：Debezium 先全量快照再切增量，保证目标表有历史基线 (跳过 = 只接增量，目标表缺历史数据，count 永远对不上)。 (evidence: [T03-S012])
  4. 增量 merge/upsert 进目标表：用主键 MERGE (upsert)，delete 事件转软删或物理删，幂等覆盖 (跳过 = append-only 接 CDC 流，update 变成重复行，一回填数据翻倍)。 (evidence: [T03-S030, T03-S006])
  5. 加监控 + 死信处理：lag 监控 + schema 漂移告警 + DLQ，源库 schema 变更不静默断流 (跳过 = 源加字段时 connector 静默挂掉，下游几小时后才发现断流)。 (evidence: [T03-S023, T03-S022])
- **资深路径**: **跳过** 自建 CDC connector / 自己 parse binlog（Debezium 是事实标准，自建是巨坑，长尾源才考虑），也跳过给所有源都上 CDC（多数批量同步用 EL 全量足够，CDC 只给真高频/低延迟表）；**优化** 用主键 MERGE + 去重窗口做幂等 upsert（同一变更重放结果一致），merge-on-read 表格式 (Hudi/Iceberg v3 deletion vector) 降写放大；**额外** 显式处理 schema 漂移 (schema registry + 兼容性策略) + tombstone 软删 + exactly-once 投递语义，避免乱序 update 覆盖新值。 (evidence: [T03-S030, T03-S023, T03-S006])
- **近期变化**: **medium** decay。2025 起 Confluent Tableflow GA — Kafka topic 可一键物化为 Iceberg 表，CDC → lakehouse 路径缩短；Iceberg v3 (2025 public preview) 引入 row lineage + deletion vectors，merge-on-read upsert 写放大显著降低，改变了「CDC 增量怎么落表」的优化点。触发事件类型: 新工具/标准更新。 (evidence: [T03-S023, T03-S030])
- **典型耗时**: 入门 SOP 单库约 2-5 天 (含快照调试)；资深路径模板化后单库 1-2 天。
- **关键工具**: Debezium (CDC 事实标准，必备/medium)、Kafka + Kafka Connect (流缓冲)、Hudi/Iceberg (merge-on-read 落点)、Schema Registry (schema 漂移)。
- **关键人物**: Gunnar Morling (Track 01 — Debezium 前 lead/CDC)；Vinoth Chandar (Track 01 — Hudi upsert/增量处理)；Jay Kreps (Track 01 — The Log/流即一等公民)。
- **常见失败模式**:
  - append-only 接 CDC 流：update 变重复行，回填即数据翻倍 → 必须主键 MERGE/upsert 覆盖。**CLI 自检**: "Is the CDC sink append-only? Updates will duplicate rows — use MERGE/upsert by primary key."
  - 漏配初始快照：目标表只有增量缺历史，count 永远对不上源 → Debezium 先 snapshot 再切增量。**CLI 自检**: "Did you run an initial snapshot before streaming? Without it the target table is missing all history."
  - 源库 schema 变更静默断流：上游加/删字段 connector 挂掉，几小时后才被发现 → schema registry + 兼容性策略 + 告警。**CLI 自检**: "Will a source schema change silently kill the connector? Add schema registry + drift alerts."
  - query-based 轮询冒充 CDC：漏 delete + 给源库加压 → 用 log-based (binlog/WAL) CDC。**CLI 自检**: "Are you polling with SELECT instead of reading the binlog/WAL? Polling misses deletes and stresses the source."
- **来源** (≥3):
  - [surrogate_primary] T03-S012 Debezium tutorial (binlog→Kafka), collected 2026-05-20
  - [surrogate_primary] T03-S030 Hudi write operations (upsert/merge-on-read)
  - [surrogate_primary] T03-S013 Kafka Connect (摄取)
  - [surrogate_primary] T03-S023 Confluent Schema Registry (schema 漂移)
- **Last_updated**: 2026-05-20
- **Decay risk**: medium (CDC 概念稳定，但 Tableflow/Iceberg v3 改写落表优化路径)

---

### 3. 维度建模 + dbt 项目结构

- **One-liner**: 把杂乱 SQL 整理成分层、可测试、面向消费的建模层 — dbt staging → intermediate → marts (对应 medallion bronze/silver/gold)，含 SCD 历史维 + tests。 (evidence: [T03-S001, T03-S029])
- **Trigger**: BI/分析的 SQL 各写各的、口径不一致、改一处崩一片；要把 ad-hoc 查询升级成可维护、有血缘、可复用的建模资产。 (evidence: [T03-S001, T03-S005])
- **Output**: 一个分层 dbt 项目 — staging (清洗) / intermediate (复用逻辑) / marts (事实+维度) + SCD type-2 历史表 + 每层 tests + 文档/血缘。 (evidence: [T03-S001, T03-S031])
- **入门 SOP**:
  1. 建 staging 层：每源 1:1 清洗 (改名/类型/标准化)，view 物化，命名 `stg_<source>__<entity>` (跳过 = 业务逻辑直接堆源表，无清洗隔离，到处复制粘贴脏数据)。 (evidence: [T03-S001])
  2. 设计维度模型：识别业务过程 → 事实表 (度量) + 维度表 (上下文)，star schema，按消费方而非源结构建 (跳过 = 照搬源库规范化表给 BI，分析要 join 十几张表，慢且难懂)。 (evidence: [T03-S001])
  3. 建 intermediate 层 (可选)：抽取被多个 mart 复用的中间逻辑，避免重复 (跳过 = 同一段 join 在多个 mart 复制，改口径要改 N 处)。 (evidence: [T03-S001])
  4. 建 marts 层：业务域分组的事实/维度，table/incremental 物化，作为 serving 契约 (跳过 = BI 直连 staging，无稳定消费接口，重构即破坏所有 dashboard)。 (evidence: [T03-S001, T03-S029])
  5. 处理历史变化 (SCD) + 加 tests：维度用 dbt snapshot 做 SCD type-2 留历史，每层挂 unique/not_null/relationships + accepted_values (跳过 = 维度 type-1 直接覆盖，历史口径丢失无法回溯；无 test 即数据沼泽)。 (evidence: [T03-S031, T03-S003])
- **资深路径**: **跳过** 对所有维度无脑上 SCD type-2（多数维度 type-1 覆盖足够，只对真要审计历史的维度做 type-2），也跳过照搬 Inmon 全规范化（OLAP 场景规范化反而慢）；**优化** 在列存数仓时代用 OBT/大宽表替代部分 star schema（去 join 提速，但权衡刷新成本），incremental 物化大事实表；**额外** 做一致性维度 (conformed dimensions) + 总线矩阵规划企业级一致性 + 在 marts 层定义指标/语义层 (MetricFlow)，保证「指标定义一次全栈一致」。 (evidence: [T03-S001, T03-S031, T03-S005])
- **近期变化**: **low** decay — 维度建模 (Kimball, 1996+) 是稳态基础语汇。近 12 月增量：列存时代「star schema vs OBT 大宽表 vs Data Vault」之争持续 (悬而未决)；dbt 分层 (staging/intermediate/marts) 已成社区惯例并对齐 medallion (bronze/silver/gold)；MetricFlow 语义层把指标定义上移。触发事件类型: 标准更新 (社区惯例固化)。 (evidence: [T03-S001, T03-S005])
- **典型耗时**: 入门 SOP 一个业务域约 1-2 周；资深路径 (有模板+conformed dim 库) 同等域 3-5 天。
- **关键工具**: dbt (建模+测试+血缘，必备)、SQLMesh (列级血缘/虚拟环境替代)、云数仓 (物化落点)、dbt snapshot (SCD)。
- **关键人物**: Ralph Kimball (Track 01 — 维度建模圣经)；Bill Inmon (Track 01 — CIF 规范化对照极)；Tristan Handy (Track 01 — dbt 分层)。
- **常见失败模式**:
  - 照搬源库规范化表给 BI：分析要 join 十几张表，慢且没人看得懂 → 面向消费做维度/OBT 建模。**CLI 自检**: "Are you exposing normalized source tables to BI? Model dimensionally (star/OBT) for consumption instead."
  - 维度 type-1 覆盖丢历史：业务问「上季度的口径」答不出 → 需审计的维度用 SCD type-2 snapshot。**CLI 自检**: "Do dimensions overwrite history (type-1)? Use SCD type-2 snapshots where audit/historical query matters."
  - 无 intermediate 层导致逻辑复制：同一段 join 在多 mart 重复，改口径要改 N 处 → 抽 intermediate 复用。**CLI 自检**: "Is the same join logic copy-pasted across marts? Extract an intermediate model."
  - 无分层无 test 的扁平项目：一个文件夹堆几百个 model 无血缘 → staging/intermediate/marts 分层 + 每层 test。**CLI 自检**: "Is the dbt project a flat pile of models with no tests? Adopt staging/intermediate/marts layering with tests."
- **来源** (≥3):
  - [surrogate_primary] T03-S001 dbt how-we-structure (分层), collected 2026-05-20
  - [surrogate_primary] T03-S031 dbt snapshots (SCD type-2)
  - [surrogate_primary] T03-S029 Databricks medallion (bronze/silver/gold)
  - [surrogate_primary] T03-S003 dbt data tests
- **Last_updated**: 2026-05-20
- **Decay risk**: low (维度建模概念稳态，OBT/Data Vault 之争是 medium 层细节)

---

### 4. 编排 DAG 设计

- **One-liner**: 把多步骤管道组织成可调度、可重试、幂等、可回填的有向无环图 — Airflow/Dagster 设计任务依赖 + 重试 + idempotency + backfill + (新) data-aware scheduling。 (evidence: [T03-S008, T03-S010])
- **Trigger**: 管道从单脚本长成「EL → dbt → 质量检查 → 通知」多步骤，需要依赖管理、失败重试、定时调度、历史重算。 (evidence: [T03-S008])
- **Output**: 一个生产级 DAG — 明确依赖 + 重试策略 + 幂等任务 + 可安全 backfill + 监控告警。 (evidence: [T03-S008, T03-S009])
- **入门 SOP**:
  1. 拆任务定依赖：把管道拆成原子任务 (extract/load/transform/test/notify)，用 upstream→downstream 声明 DAG (跳过 = 一个巨型脚本干所有事，单点失败全挂、无法局部重跑)。 (evidence: [T03-S008])
  2. 设调度 + 重试：定 schedule (cron/interval)，每任务设 retries + retry_delay + timeout (跳过 = 无重试，瞬时网络抖动即整条管道失败需人工救火)。 (evidence: [T03-S008])
  3. 保证任务幂等：每个 task 对同一输入分区重跑结果一致 (覆盖而非追加，merge/upsert by key) (跳过 = 非幂等 task 重试/回填即产生脏数据、数据翻倍 — pipeline 最隐蔽灾难源)。 (evidence: [T03-S006, T03-S007])
  4. 支持 backfill 回填：任务按 execution_date/分区参数化，能用新逻辑安全重算历史区间 (跳过 = 改了转换逻辑无法重算历史，新旧口径数据并存)。 (evidence: [T03-S009, T03-S006])
  5. 加监控 + 告警 + SLA：任务失败/超时/SLA miss 告警，关键产出挂新鲜度检查 (跳过 = 管道半夜静默失败，早上 dashboard 空白才发现)。 (evidence: [T03-S011, T03-S022])
- **资深路径**: **跳过** 纯 cron/time-based 调度心智（资深默认任务幂等所以重跑无害，不靠精确定时），也跳过把编排器当通用计算引擎（重计算下推到 dbt/Spark/数仓，编排器只调度不算数）；**优化** 用 data-aware / asset-based 调度 (Dagster software-defined assets / Airflow datasets)，上游资产更新自动触发下游而非盲目定时跑 + declarative freshness 策略；**额外** 把幂等 + 不可变分区作为设计前提 (Functional Data Engineering) + 参数化分区让 backfill 一键安全 + 任务级 SLA/血缘，避免「回填即灾难」。 (evidence: [T03-S010, T03-S011, T03-S006])
- **近期变化**: **low** decay — 编排核心 (依赖/重试/幂等/回填) 稳态。近 12 月增量：2025 Airflow 3.x (DAG versioning + 改进 backfill)；Dagster software-defined assets + declarative automation 推动从「任务编排」转向「资产/数据感知编排」(data-aware scheduling)；Databricks 2025-06 把 Declarative Pipelines 捐给 Apache Spark (描述目标状态而非手写编排)。触发事件类型: 新工具/新版本。 (evidence: [T03-S008, T03-S010, T03-S011])
- **典型耗时**: 入门 SOP 一条管道约 2-4 天；资深路径 (asset 模板) 1-2 天。
- **关键工具**: Airflow (任务编排事实标准，必备)、Dagster (asset/data-aware，medium)、Prefect (Pythonic 轻量)、DolphinScheduler (中国 stack 可视化)。
- **关键人物**: Maxime Beauchemin (Track 01 — Airflow 创始/幂等)；Nick Schrock (Track 01 — Dagster/software-defined assets)。
- **常见失败模式**:
  - 非幂等任务 + 回填：append 任务一回填数据翻倍 → 任务必须幂等 (覆盖/merge by key)。**CLI 自检**: "Is every task idempotent (overwrite, not append)? A non-idempotent backfill doubles your data."
  - 巨型单任务无原子拆分：单点失败整条挂、无法局部重跑 → 拆成原子可重试任务。**CLI 自检**: "Is the pipeline one giant task? Split into atomic, individually-retryable tasks."
  - 编排器当计算引擎：把重 transform 塞进 Python operator 跑挂内存 → 计算下推 dbt/Spark/数仓。**CLI 自检**: "Are you doing heavy compute inside the orchestrator? Push it down to dbt/Spark/warehouse."
  - 无 backfill 参数化：改逻辑后无法重算历史，新旧口径并存 → 任务按分区/execution_date 参数化。**CLI 自检**: "Can you safely backfill a date range with new logic? Parameterize tasks by partition/execution_date."
- **来源** (≥3):
  - [surrogate_primary] T03-S008 Airflow DAGs (依赖/重试/调度), collected 2026-05-20
  - [surrogate_primary] T03-S009 Airflow backfill (回填)
  - [surrogate_primary] T03-S010 Dagster assets (data-aware/software-defined)
  - [surrogate_primary] T03-S006 Functional Data Engineering (幂等前提)
- **Last_updated**: 2026-05-20
- **Decay risk**: low (核心稳态，asset/data-aware 调度是 medium 层演进)

---

### 5. lakehouse 表格式落地

- **One-liner**: 在对象存储上用开放表格式 (Iceberg/Delta) 落地一张生产表并持续治理 — partition 设计 / compaction 小文件治理 / schema evolution / snapshot 过期 / time travel。 (evidence: [T03-S014, T03-S028])
- **Trigger**: 数据落在 S3/GCS 上要 ACID 提交、schema 安全演进、按快照回查，或要避开闭源数仓 vendor lock-in 用 lakehouse 架构。 (evidence: [T03-S028, T03-S015])
- **Output**: 一张生产 Iceberg/Delta 表 + 分区策略 + compaction/expire 维护作业 + schema evolution 规范 + time-travel 能力。 (evidence: [T03-S014, T03-S015])
- **入门 SOP**:
  1. 选表格式 + catalog：按现有引擎选 Iceberg (中立/Trino/Flink) 或 Delta (Databricks)，配 REST/Glue/Unity catalog (跳过 = 裸 Parquet 无表层，无 ACID、并发写互相覆盖、无 schema 治理)。 (evidence: [T03-S028])
  2. 设计分区：按查询谓词 (常按日期) 分区，用隐藏分区 (Iceberg) 避免暴露物理布局 (跳过 = 不分区全表扫，或过细分区每分区一小文件，两头都炸成本)。 (evidence: [T03-S015, T03-S026])
  3. 写入 + ACID 提交：批/流写经表格式原子 commit，并发写有快照隔离 (跳过 = 直接覆盖文件，读到半写状态/脏读，写冲突丢数据)。 (evidence: [T03-S028])
  4. 配 compaction 治理小文件：定期 compact 小文件 + rewrite manifests，流/微批写尤其需要 (跳过 = 小文件堆积，元数据爆炸 + 查询越来越慢 + 列表 S3 成本涨)。 (evidence: [T03-S014, T03-S016])
  5. 配 snapshot 过期 + schema 演进规范：定期 expire 旧快照控存储，schema 只增不删保向后兼容 (跳过 = 快照无限增长存储爆炸；删/改字段静默打爆下游读)。 (evidence: [T03-S014, T03-S015])
- **资深路径**: **跳过** 手工管理物理分区目录 / Hive 式显式分区列（Iceberg 隐藏分区让查询不暴露布局，重分区不重写查询），也跳过为小数据上 lakehouse（几十 GB 单机 DuckDB/单数仓更省心）；**优化** 用隐藏分区 + 自动 compaction (Iceberg rewrite/Delta OPTIMIZE+Z-ORDER) 调到「文件大小适中」+ partition evolution 不重写历史数据改分区策略；**额外** 显式做 snapshot expiration + orphan file 清理 + schema evolution 兼容性规则 (只增不删/不改类型) + 用 time travel 做审计/回滚，避免存储和元数据无限膨胀。 (evidence: [T03-S014, T03-S015, T03-S016, T03-S032])
- **近期变化**: **medium** decay。2025 Iceberg v3 public preview (row lineage + deletion vectors + VARIANT) 大幅改善 merge-on-read/小更新；Databricks 全面支持 Iceberg + Delta UniForm/Apache XTable 推动表格式互操作 (Iceberg↔Delta↔Hudi 元数据转译)，「选哪个格式」的锁定焦虑下降；Iceberg REST catalog/Polaris 成中立 catalog 标准。触发事件类型: 新标准/行业事件 (Tabular 被 Databricks 收购)。 (evidence: [T03-S014, T03-S015, T03-S034])
- **典型耗时**: 入门 SOP 一张表约 2-4 天 (含 catalog/compaction 配置)；资深路径 (有维护作业模板) 1-2 天。
- **关键工具**: Iceberg/Delta/Hudi (开放表格式，必备/low-medium)、Parquet (落盘)、Trino/Spark/Flink (读写引擎)、对象存储 S3/GCS、catalog (Glue/Unity/Polaris)。
- **关键人物**: Ryan Blue (Track 01 — Iceberg/隐藏分区)；Matei Zaharia (Track 01 — Delta/Lakehouse 论文)；Vinoth Chandar (Track 01 — Hudi/小文件 compaction)。
- **常见失败模式**:
  - 不做 compaction 的流/微批写：海量小文件 → 元数据爆炸 + 查询慢 + S3 列表成本涨 → 定期 compact + rewrite manifests。**CLI 自检**: "Are you streaming writes without compaction? Schedule compaction or small files will tank query speed and cost."
  - 裸 Parquet 当生产表：无 ACID，并发写互相覆盖、读到半写脏数据 → 用 Iceberg/Delta 表层。**CLI 自检**: "Are you writing bare Parquet with no table format? You get no ACID — concurrent writes corrupt each other."
  - 删/改字段破坏 schema 演进：下游读静默失败 → schema 只增不删，遵守兼容性规则。**CLI 自检**: "Are you dropping/retyping columns? Schema is an API — evolve additively (add, don't drop)."
  - 快照永不过期：存储无限增长，账单慢慢爬高 → 配 expire snapshots + orphan 清理。**CLI 自检**: "Do you expire old snapshots? Without it, storage grows unbounded."
- **来源** (≥3):
  - [surrogate_primary] T03-S014 Iceberg maintenance (compaction/expire), collected 2026-05-20
  - [surrogate_primary] T03-S015 Iceberg evolution (schema/partition/隐藏分区)
  - [verified_primary] T03-S028 Lakehouse CIDR 2021 (湖仓奠基)
  - [surrogate_primary] T03-S016 Delta OPTIMIZE (小文件 compaction)
- **Last_updated**: 2026-05-20
- **Decay risk**: medium (格式之争 + 互操作 + Iceberg v3 演进中)

---

### 6. 流处理管道

- **One-liner**: 构建一条真实时的有状态流处理管道 — Kafka → Flink/Spark Streaming，处理 windowing / watermark / exactly-once / state，并先做 Lambda vs Kappa 架构取舍 (要不要这条流)。 (evidence: [T03-S017, T03-S018, T03-S019])
- **Trigger**: 出现真亚秒/秒级实时需求 (风控/实时推荐/监控告警/实时大盘)，批的分钟级延迟不可接受。 (evidence: [T03-S017, T03-S019])
- **Output**: 一条 Kafka 上游 + Flink/Spark Streaming 计算 + exactly-once 写出的有状态流管道，正确处理乱序与窗口。 (evidence: [T03-S017, T03-S018])
- **入门 SOP**:
  1. 先确认「真的需要流吗」：量化延迟需求，分钟/小时级用批 (workflow 1/4)，只有真亚秒才上流 (跳过 = 为「实时更高级」上流，背上双倍复杂度+成本却无业务收益)。 (evidence: [T03-S019, T03-S032])
  2. Kafka 做事件源 + 分区：上游事件入 Kafka topic 按 key 分区保证同 key 有序 (跳过 = 直连源无缓冲，下游故障即丢事件，无法 replay)。 (evidence: [T03-S017])
  3. 选 event-time + 配 watermark：用事件时间而非处理时间，watermark 估计「窗口数据到齐」处理乱序 (跳过 = 用 processing-time 切窗口，乱序/迟到数据算错，结果不可复现)。 (evidence: [T03-S018])
  4. 设计 windowing + state：选窗口类型 (滚动/滑动/会话) + 状态后端 + checkpoint 周期 (跳过 = 无状态管理，聚合算不对；无 checkpoint，故障重启状态全丢)。 (evidence: [T03-S017, T03-S018])
  5. 配 exactly-once + 监控背压：开 checkpoint + 事务性 sink 保 exactly-once，监控 lag/背压/重启 (跳过 = at-least-once 重复计数，或故障后数据丢失/重复，下游金额对不上)。 (evidence: [T03-S018, T03-S022])
- **资深路径**: **跳过** Lambda 架构维护批+流两套代码（资深默认 Kappa/单流引擎，用流回放替双链路，避免「同一逻辑写两遍口径漂移」），也跳过给多数分析上流（先用批，真亚秒才上）；**优化** 用 watermark + allowed lateness 精调正确性/延迟/成本三角，state TTL + 增量 checkpoint 控状态膨胀，事务性 sink 做端到端 exactly-once；**额外** 显式做背压/反压治理 + state schema 演进 + 用流式 SQL (Flink SQL / RisingWave / Snowflake Dynamic Tables) 把流处理「民主化」成声明式 SQL，降低手工增量化心智负担。 (evidence: [T03-S017, T03-S018, T03-S019])
- **近期变化**: **medium** decay。2025-04 Tyler Akidau SIGMOD 论文 'Streaming Democratized' + Snowflake Dynamic Tables 把流处理推进声明式 SQL (delayed view semantics)；Confluent Current 2025 主题转「实时数据 + AI」+ Tableflow (Kafka→Iceberg)；Apache Paimon/Fluss (Jark Wu) 推 streaming lakehouse 流批一体。趋势是「手写 Flink 算子」逐步被「流式 SQL/增量物化视图」替代。触发事件类型: 新工具/标准更新。 (evidence: [T03-S017, T03-S018])
- **典型耗时**: 入门 SOP 一条管道约 1-3 周 (state/exactly-once 调试重)；资深路径 (流式 SQL) 可压到数天。
- **关键工具**: Kafka (流底座，必备)、Flink (有状态流计算，medium)、Spark Structured Streaming (微批)、RisingWave/Materialize (流式 SQL 物化视图)、Paimon (streaming lakehouse)。
- **关键人物**: Jay Kreps (Track 01 — The Log/Kappa)；Tyler Akidau (Track 01 — Streaming Systems/watermark/批流统一)；伍翀 Jark Wu (Track 01 — Flink SQL/流批一体/Fluss)。
- **常见失败模式**:
  - 为「实时更高级」上流：背双倍复杂度+成本无业务收益 → 先量化延迟需求，分钟级用批。**CLI 自检**: "Do you have a true sub-second requirement, or does batch suffice? Don't pay streaming's 2x complexity for no business gain."
  - 用 processing-time 切窗口：乱序/迟到数据算错且不可复现 → event-time + watermark。**CLI 自检**: "Are windows based on processing-time? Use event-time + watermarks or out-of-order data computes wrong."
  - Lambda 双链路：批流两套代码口径漂移、维护翻倍 → 走 Kappa/单流引擎。**CLI 自检**: "Are you maintaining separate batch and streaming code (Lambda)? Consider Kappa/single-engine to avoid logic drift."
  - 无 checkpoint/at-least-once sink：故障后重复计数或丢数据，金额对不上 → checkpoint + 事务性 sink 做 exactly-once。**CLI 自检**: "Is the sink at-least-once with no checkpoint? Failures will duplicate or lose data — use exactly-once."
- **来源** (≥3):
  - [surrogate_primary] T03-S017 Flink applications (windowing/state), collected 2026-05-20
  - [surrogate_primary] T03-S018 Flink time/watermark (event-time/exactly-once)
  - [surrogate_primary] T03-S019 Questioning the Lambda Architecture (Kappa 取舍)
  - [surrogate_primary] T03-S032 Big Data is Dead (反过度复杂)
- **Last_updated**: 2026-05-20
- **Decay risk**: medium (流式 SQL/增量物化视图正在改写「手写 Flink」)

---

### 7. 数据质量门禁 + 数据契约

- **One-liner**: 给管道装上「错误数据上不了生产」的门禁 — dbt tests / Great Expectations + schema registry + freshness/volume/anomaly 监控 + shift-left 数据契约 (schema is API)。 (evidence: [T03-S003, T03-S020, T03-S021])
- **Trigger**: 错误/缺失数据静默流向 dashboard/ML/决策；上游随意改 schema 打爆下游；需要把质量从「末端救火」变成「门禁 + 契约」。 (evidence: [T03-S021, T03-S022])
- **Output**: 一套分层质量门禁 — 转换层 dbt tests + 校验套件 (GX) + 源端数据契约/schema registry + 五维监控 (freshness/volume/schema/distribution/lineage)。 (evidence: [T03-S003, T03-S020, T03-S022])
- **入门 SOP**:
  1. 加 dbt tests 第一道防线：模型挂 unique/not_null/relationships/accepted_values，CI 失败即阻断 (跳过 = 无测试上生产，主键重复/外键悬空静默进 BI = 数据沼泽)。 (evidence: [T03-S003])
  2. 配 source freshness 检查：源表挂 freshness (warn/error 阈值)，过期即告警 (跳过 = 上游断流半天没人知道，dashboard 显示陈旧数据当最新)。 (evidence: [T03-S004])
  3. 加期望套件 (复杂校验)：非 dbt 栈或复杂分布校验用 Great Expectations/Soda 套件 (跳过 = 只测结构不测分布，数值漂移/异常值静默通过)。 (evidence: [T03-S020])
  4. 配五维监控：freshness/volume/schema/distribution/lineage 异常检测 + 影响面血缘 (跳过 = 只在出问题时手查，无主动告警 + 不知道坏数据影响哪些下游)。 (evidence: [T03-S022])
  5. 在源端立数据契约：producer-consumer 显式 schema 约定 + schema registry 兼容性门禁 (跳过 = 上游加/删字段静默打爆所有下游 pipeline，末端 N 个团队救火)。 (evidence: [T03-S021, T03-S023])
- **资深路径**: **跳过** 纯末端 observability 救火心智（资深 shift-left 到生产端，让上游 producer 与下游一样为质量负责），也跳过对每张表都堆几十条 test（聚焦关键产出表 + 主键/口径关键列，避免 test 维护反成负担）；**优化** 把质量检查左移到 CI/PR 门禁 (state:modified 只测改动) + 数据契约做成可强制校验门禁而非文档 + anomaly detection 用统计基线替手设阈值；**额外** 做列级血缘影响分析 (改一列知道炸哪些下游) + PII/敏感字段分类与契约 + schema registry 向后兼容策略，把「schema 是 API」落成机制。 (evidence: [T03-S021, T03-S022, T03-S023, T03-S024])
- **近期变化**: **medium** decay。2025 Shift Left Data Conference (Gable 主办，Handy/Moses/Sanderson/Reis 同台) 把「shift-left + 数据契约」推成行业议题；Monte Carlo 2025-09 推 Agent Observability 把质量监控扩到 AI/LLM stack (prompts/completions)；data observability (末端) vs shift-left contract (源端) 的流派之争仍在演进。触发事件类型: 行业事件/新工具。 (evidence: [T03-S021, T03-S022])
- **典型耗时**: 入门 SOP 一个项目约 3-5 天 (test + freshness)；资深路径 (契约 + 血缘 + CI 门禁) 1-3 周 (需上游团队配合，组织阻力是主要成本)。
- **关键工具**: dbt tests (第一道防线，必备)、Great Expectations/Soda (校验套件)、Monte Carlo/Elementary (data observability)、Schema Registry/Gable (数据契约)、DataHub/OpenMetadata (列级血缘/PII)。
- **关键人物**: Chad Sanderson (Track 01 — data contracts/shift-left/schema is API)；Barr Moses (Track 01 — data observability/data downtime/五维)。
- **常见失败模式**:
  - 无测试上生产：主键重复/外键悬空静默进 BI/ML → dbt tests 做最低门禁。**CLI 自检**: "Are you shipping to prod with zero data tests? Add unique/not_null/relationships — no tests = data swamp."
  - 只测结构不测分布：数值漂移/异常值通过结构检查仍是错的 → 加分布/anomaly 校验。**CLI 自检**: "Do you only test schema, not distributions? Add value/distribution/anomaly checks."
  - 数据契约当文档不强制：写在 wiki 上没人遵守，上游照样删字段 → 契约做成 CI 可强制门禁。**CLI 自检**: "Is the data contract just a doc? Make it an enforceable CI gate, not a wiki page."
  - 末端 observability 救火：等坏数据流到 dashboard 才发现，下游 N 个团队修 → shift-left 到源端契约。**CLI 自检**: "Are you firefighting bad data at the consumer end? Shift quality left to the producer / contract."
- **来源** (≥3):
  - [surrogate_primary] T03-S003 dbt data tests, collected 2026-05-20
  - [surrogate_primary] T03-S020 Great Expectations (期望套件)
  - [verified_primary] T03-S021 Shift Left Data Manifesto (Sanderson/契约)
  - [surrogate_primary] T03-S022 Monte Carlo data observability (五维)
- **Last_updated**: 2026-05-20
- **Decay risk**: medium (observability vs shift-left 流派 + AI observability 扩展中)

---

### 8. 数据 DataOps / CI-CD + 成本治理

- **One-liner**: 把数据管道当软件来交付并控住云账单 — dev/staging/prod 环境隔离 + PR 测试门禁 + 部署流水 + FinOps 成本治理 (分区裁剪/物化/按需暂停/查询审计)。 (evidence: [T03-S024, T03-S025, T03-S026])
- **Trigger**: 团队多人改同一管道互相踩踏、改动直接上生产出事故；或云数仓/计算账单异常飙升要治理。 (evidence: [T03-S025, T03-S026])
- **Output**: 一套 DataOps 流程 — 三环境隔离 + PR 自动化测试门禁 + 受控部署 + 成本护栏 (分区/物化/暂停/审计) + 账单异常告警。 (evidence: [T03-S024, T03-S025, T03-S026])
- **入门 SOP**:
  1. 建 dev/staging/prod 环境隔离：每环境独立 schema/数据库/计算，dev 不碰生产数据 (跳过 = 直接改生产，一个手滑 drop 生产表/跑爆账单)。 (evidence: [T03-S025])
  2. 代码进 git + PR 流程：管道/dbt 项目版本控制，改动走 PR + code review (跳过 = 改动无记录无 review，出事无法回溯/回滚)。 (evidence: [T03-S035])
  3. 配 PR 测试门禁 (CI)：PR 触发 build + dbt tests + lint，绿灯才可合并 (跳过 = 坏改动直接合并上线，生产事故才发现)。 (evidence: [T03-S024, T03-S035])
  4. 配受控部署：合并到 main 自动部署 staging→prod，可回滚 (跳过 = 手工 promote，漏步骤/环境不一致/部署即祈祷)。 (evidence: [T03-S035, T03-S025])
  5. 立成本护栏 (FinOps)：分区裁剪 + 列裁剪 + incremental 物化 + 计算按需暂停 + 查询成本审计/告警 (跳过 = SELECT * 全表扫 + 全量重算 + 集群常开，账单指数爆炸)。 (evidence: [T03-S026, T03-S032])
- **资深路径**: **跳过** 手工 promote/部署到各环境（资深用 CI/CD 自动化 + slim CI 只 build 改动），也跳过「先上线再说」的无门禁交付；**优化** 用 dbt slim CI (state:modified 只测+建改动模型，CI 从小时级降到分钟级) + 临时 PR schema/虚拟环境隔离 + incremental + 物化策略按查询频率分层 (热表物化/冷查 view)；**额外** 主动做 cost FinOps — 查询成本审计 (谁的 query 最贵)、分区裁剪强制、计算 auto-suspend/auto-scale、账单异常告警 + 按团队 chargeback，把成本当一等可观测指标。 (evidence: [T03-S024, T03-S025, T03-S026, T03-S032])
- **近期变化**: **high** decay。dbt slim CI / state:modified + dbt Cloud CI jobs 持续演进；2025-05 dbt Fusion engine (Rust，更快 parse/CI) 改写 CI 体验；云数仓成本治理工具 (查询审计/自动暂停) 快速迭代；SQLMesh 的「虚拟环境/无状态 dev」是 CI-CD 的新竞争范式。CI-CD + cost 这块工具/最佳实践 12 个月内显著刷新概率高。触发事件类型: 新工具/新版本。 (evidence: [T03-S024, T03-S026])
- **典型耗时**: 入门 SOP 一个团队约 1-2 周 (环境 + CI 搭建)；资深路径 (slim CI + FinOps 护栏) 持续优化、初次落地 2-4 周。
- **关键工具**: dbt (CI jobs/环境/slim CI，必备)、git + GitHub Actions/GitLab CI (PR 门禁)、云数仓成本控制台 (BigQuery/Snowflake，分区裁剪/审计)、SQLMesh (虚拟环境替代范式)。
- **关键人物**: Maxime Beauchemin (Track 01 — DataOps/数据工程是软件工程)；Tristan Handy (Track 01 — dbt CI/环境/analytics engineering 纪律)。
- **常见失败模式**:
  - 直接改生产无环境隔离：手滑 drop 生产表 / 跑爆账单 → dev/staging/prod 隔离。**CLI 自检**: "Are you editing prod directly with no dev/staging? One slip drops a prod table — isolate environments."
  - 无 PR 测试门禁：坏改动直接合并上线，生产才发现 → PR 触发 CI build + tests 绿灯才合。**CLI 自检**: "Do PRs merge without CI tests? Add a build+test gate — bad changes must fail before merge."
  - SELECT * 全表扫 + 全量重算 + 集群常开：账单指数爆炸 → 分区裁剪 + 列裁剪 + incremental + auto-suspend。**CLI 自检**: "Any SELECT * / full re-compute / always-on cluster? These are the four bill-killers — prune partitions/columns, go incremental, auto-suspend."
  - 手工 promote 各环境：漏步骤/环境漂移/部署即祈祷 → CI/CD 自动化部署 + 可回滚。**CLI 自检**: "Are you promoting between environments by hand? Automate deploy with rollback."
- **来源** (≥3):
  - [surrogate_primary] T03-S024 dbt CI jobs (slim CI/state:modified), collected 2026-05-20
  - [surrogate_primary] T03-S025 dbt environments (dev/staging/prod)
  - [surrogate_primary] T03-S026 BigQuery cost best practices (分区裁剪/审计)
  - [surrogate_primary] T03-S035 dbt best-practice workflows (PR/部署)
- **Last_updated**: 2026-05-20
- **Decay risk**: high (CI 引擎 Fusion/slim CI + cost 工具 12 月内显著刷新)

---

## Phase 2 提炼提示

**反复出现 ≥ 3 个 workflow 都包含的步骤**（候选 playbook 通则）:
- **「保证任务/写入幂等 (覆盖/merge by key 而非追加)」** 出现于 workflows: 1 (ELT) / 2 (CDC merge) / 4 (DAG 回填) / 5 (lakehouse ACID commit) → 候选 playbook「如果 pipeline 要支持回填/重试，则任务必须对分区幂等 (merge/upsert with primary key，覆盖而非追加)」(工程伦理 anchor)。 (evidence: [T03-S006, T03-S007])
- **「在源/转换层加质量门禁 + 契约 (test/freshness/schema)」** 出现于 workflows: 1 / 2 (schema 漂移) / 3 (dbt tests) / 7 (契约) / 8 (CI 门禁) → 候选 playbook「如果数据流向 BI/ML/决策，则上线前必须有 test 门禁 + 源端 schema 契约 (schema is API)」。 (evidence: [T03-S003, T03-S021])
- **「先问『我真的需要 X 吗』(反过早复杂)」** 出现于 workflows: 1 (反自建 EL) / 5 (反小数据上 lakehouse) / 6 (反过早上流) → 候选 playbook「如果要上分布式/流/自建框架，则先量化数据规模与延迟需求，默认更简单方案」(工程伦理 anchor)。 (evidence: [T03-S019, T03-S032])
- **「成本/扫描量治理 (分区裁剪/incremental/小文件 compaction)」** 出现于 workflows: 1 (incremental) / 5 (compaction) / 8 (FinOps) → 候选 playbook「如果云账单异常，则查 SELECT * / 全量重算 / 小文件 / 缺分区裁剪四大元凶」。 (evidence: [T03-S026])

**入门 SOP 和资深路径之间最大的差距**（候选 心智模型）:
- 入门 SOP 平均 5 步，资深路径普遍「跳过 1-2 步 (自建 framework / Lambda 双链路 / 全 SCD type-2 / 手工 promote) + 优化 1-2 步 (incremental / 隐藏分区 / asset 调度 / slim CI) + 额外 1-2 步 (契约 / 幂等前提 / snapshot 过期 / FinOps)」。
- 资深差异最集中的判断：**「反过早复杂 + 幂等是设计前提 + 质量/契约左移」** — 这一行的资深人特别擅长 (1) 不为简历/显得专业上分布式/流/自建，(2) 默认任务幂等所以重跑/回填无害不靠精确定时，(3) 把质量门禁从末端救火移到源端契约。→ 三大心智模型候选: 「反过早分布式」「幂等/可重跑第一公民」「schema 是 API / shift-left」。

**近期工作流变化的根本原因**（触发事件类型分布）:
- 新工具/新版本驱动: 6 个 workflow (CDC Tableflow / Iceberg v3 / Dagster asset / 流式 SQL Dynamic Tables / dbt Fusion / slim CI) — **主要驱动力**。
- 标准更新/社区惯例固化: 2 个 (dbt 分层↔medallion / data contract 行业议题化)。
- 行业事件: 1 个 (Tabular 被 Databricks 收购 → 表格式互操作)。
- **主要外部驱动力**: ① 表格式/流处理「声明式化 + 互操作化」(Iceberg v3 / Dynamic Tables / XTable)，② CI/成本工具的 Rust 化提速 (Fusion)，③ 质量从末端 observability 向源端 shift-left contract 迁移。→ Phase 2 据此识别行业外部驱动力，影响心智模型 + 反模式。

**冷僻 / 信号薄弱**:
- workflow 数 = 8 (远超 floor 4) ✅
- 每个 workflow 有完整卡 (One-liner/Trigger/Output/入门 SOP/资深路径/近期变化/耗时/工具/人物/失败模式/来源/last_updated/decay) ✅
- 入门 SOP 与资深路径分开 + 100% (8/8) workflow 有 ≥2 处资深差异 (每个都含 跳过+优化+额外 三类) ✅ (远超 80% 门槛)
- 近期变化字段 100% (8/8) 都填了 (含 decay level) ✅ (超 60% 门槛)
- 一手来源 (vendor docs surrogate_primary + github/arxiv/cidr verified_primary + author newsletter) 占比 ≥95%，无 blacklisted 入表 ✅ (一手率远超 50%)
- decay risk 字段 8/8 都标 ✅；总览表按 decay 分组 ✅
- **诚实边界 flag**: ① 来源以 vendor/project docs (surrogate_primary) 为主 — 因 source_verifier 不识 .io/.org/.apache.org 项目域名，按任务规则升级 surrogate_primary 含 "vendor docs"，非内容不可信；mental_model 类 claim 已交叉 ≥2 source。② 本 track workflow 与 Track 01/02/04 高度自洽 (幂等/反过早分布式/ELT/shift-left/lakehouse 反复印证)，**非冷僻行业**。③ workflow 8 (DataOps/CI-CD+成本) decay = high，建议 master skill 每 3-6 月跑 update 优先刷新此节 + workflow 2/5/6 (medium)。
