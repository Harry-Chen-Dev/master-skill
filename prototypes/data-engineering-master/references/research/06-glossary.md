# Track 06 — Data Engineering Glossary / 术语 + 标准

> Phase 1 wave 1, Track 06. Industry = Data Engineering (数据工程). locale = en (en-primary, zh-CN secondary).
> 输出: 高频黑话 / 缩写 / 合规框架 / 认证 / outsider-tells / 厂商话术拒绝。
> FORMAT 约束: 表格单元格内 **绝不**用转义管道 (backslash + pipe)，分隔符一律用 `/` 或 `;`。

## Source Manifest

| source_id | url | bucket | last_checked | author/host | one-line note |
|-----------|-----|--------|--------------|-------------|---------------|
| T06-S001 | https://iceberg.apache.org/spec/ | surrogate_primary | 2026-05-20 | Apache Iceberg | vendor docs — open table format 官方 spec (snapshot/manifest/time travel) |
| T06-S002 | https://github.com/apache/iceberg | verified_primary | 2026-05-20 | Apache | github root — Iceberg 源码/规范权威 |
| T06-S003 | https://docs.delta.io/latest/delta-intro.html | surrogate_primary | 2026-05-20 | Delta Lake | vendor docs — Delta transaction log / ACID / time travel |
| T06-S004 | https://github.com/delta-io/delta | verified_primary | 2026-05-20 | Delta Lake / Linux Fdn | github root — Delta Lake protocol 源码 |
| T06-S005 | https://parquet.apache.org/docs/ | surrogate_primary | 2026-05-20 | Apache Parquet | vendor docs — columnar 文件格式 spec |
| T06-S006 | https://arrow.apache.org/docs/format/Columnar.html | surrogate_primary | 2026-05-20 | Apache Arrow | vendor docs — 内存列式格式 spec |
| T06-S007 | https://docs.getdbt.com/docs/build/incremental-models | verified_primary | 2026-05-20 | dbt Labs | engineering docs — incremental model / materialization |
| T06-S008 | https://docs.getdbt.com/docs/build/data-contracts | verified_primary | 2026-05-20 | dbt Labs | engineering docs — data contract / model contract |
| T06-S009 | https://www.databricks.com/glossary/medallion-architecture | surrogate_primary | 2026-05-20 | Databricks | vendor docs — medallion bronze/silver/gold 来源 |
| T06-S010 | https://openlineage.io/docs/ | surrogate_primary | 2026-05-20 | OpenLineage | vendor docs — 开放 lineage 元数据标准 spec |
| T06-S011 | https://github.com/OpenLineage/OpenLineage | verified_primary | 2026-05-20 | OpenLineage / LF AI | github root — lineage event spec 源码 |
| T06-S012 | https://www.getdbt.com/blog/what-is-analytics-engineering | verified_primary | 2026-05-20 | dbt Labs | blog — analytics engineer (AE) 角色定义 |
| T06-S013 | https://www.startdataengineering.com/post/idempotent-data-pipelines/ | surrogate_primary | 2026-05-20 | Start Data Engineering | vendor docs (author essay) — idempotency/backfill 工程定义 |
| T06-S014 | https://airflow.apache.org/docs/apache-airflow/stable/core-concepts/dags.html | surrogate_primary | 2026-05-20 | Apache Airflow | vendor docs — DAG / scheduler 概念 |
| T06-S015 | https://github.com/apache/airflow | verified_primary | 2026-05-20 | Apache | github root — Airflow orchestrator |
| T06-S016 | https://nightlies.apache.org/flink/flink-docs-stable/docs/concepts/time/ | surrogate_primary | 2026-05-20 | Apache Flink | vendor docs — watermark / event time / windowing |
| T06-S017 | https://spark.apache.org/docs/latest/sql-performance-tuning.html | surrogate_primary | 2026-05-20 | Apache Spark | vendor docs — shuffle / skew / predicate pushdown |
| T06-S018 | https://en.wikipedia.org/wiki/Slowly_changing_dimension | secondary | 2026-05-20 | — | term def — SCD type 1/2/3 |
| T06-S019 | https://en.wikipedia.org/wiki/Star_schema | secondary | 2026-05-20 | — | term def — star/snowflake/fact/dimension |
| T06-S020 | https://en.wikipedia.org/wiki/Online_analytical_processing | secondary | 2026-05-20 | — | term def — OLAP vs OLTP |
| T06-S021 | https://martinfowler.com/articles/data-mesh-principles.html | surrogate_primary | 2026-05-20 | Zhamak Dehghani / M. Fowler | vendor docs (作者一手 — Zhamak data mesh 4 principles 原文) |
| T06-S022 | https://martinfowler.com/bliki/DataLake.html | surrogate_primary | 2026-05-20 | Martin Fowler | vendor docs (作者一手 — data lake / data swamp 警告原文) |
| T06-S023 | https://gdpr.eu/what-is-gdpr/ | surrogate_primary | 2026-05-20 | GDPR.eu | vendor docs (监管) — GDPR 概览 |
| T06-S024 | https://eur-lex.europa.eu/eli/reg/2016/679/oj | surrogate_primary | 2026-05-20 | EUR-Lex | vendor docs (监管) — GDPR Regulation 2016/679 原文 |
| T06-S025 | https://www.npc.gov.cn/npc/c2/c30834/202106/t20210610_311888.html | verified_primary | 2026-05-20 | 全国人大 | 数据安全法 (DSL) 立法原文 |
| T06-S026 | https://www.npc.gov.cn/npc/c2/c30834/202108/t20210820_313088.html | verified_primary | 2026-05-20 | 全国人大 | 个人信息保护法 (PIPL) 立法原文 |
| T06-S027 | https://oag.ca.gov/privacy/ccpa | verified_primary | 2026-05-20 | California AG | CCPA — California 消费者隐私法 ground truth |
| T06-S028 | https://www.aicpa-cima.com/topic/audit-assurance/audit-and-assurance-greater-than-soc-2 | surrogate_primary | 2026-05-20 | AICPA | vendor docs (标准机构) — SOC 2 Trust Services |
| T06-S029 | https://www.singer.io/ | surrogate_primary | 2026-05-20 | Singer | vendor docs — taps/targets open spec |
| T06-S030 | https://github.com/singer-io/getting-started | verified_primary | 2026-05-20 | Singer.io | github root — Singer spec 文档 |
| T06-S031 | https://opentelemetry.io/docs/ | surrogate_primary | 2026-05-20 | OpenTelemetry | vendor docs — telemetry 标准 (data observability 借用) |
| T06-S032 | https://docs.openmetadata.org/ | surrogate_primary | 2026-05-20 | OpenMetadata | vendor docs — 开放元数据/lineage 标准 |
| T06-S033 | https://datahubproject.io/docs/ | surrogate_primary | 2026-05-20 | DataHub | vendor docs — metadata/lineage 平台 spec |
| T06-S034 | https://www.montecarlodata.com/blog-what-is-data-observability/ | surrogate_primary | 2026-05-20 | Monte Carlo | vendor docs — data observability / data downtime 提出者 |
| T06-S035 | https://www.databricks.com/glossary/lambda-architecture | surrogate_primary | 2026-05-20 | Databricks | vendor docs — Lambda 架构 |
| T06-S036 | https://www.oreilly.com/radar/questioning-the-lambda-architecture/ | secondary | 2026-05-20 | Jay Kreps / O'Reilly | author essay — Kappa 架构原文 |
| T06-S037 | https://learn.microsoft.com/en-us/azure/architecture/data-guide/relational-data/etl | surrogate_primary | 2026-05-20 | Microsoft | vendor docs — ETL vs ELT |
| T06-S038 | https://www.confluent.io/learn/change-data-capture/ | surrogate_primary | 2026-05-20 | Confluent | vendor docs — CDC / log-based replication |
| T06-S039 | https://debezium.io/documentation/reference/stable/ | surrogate_primary | 2026-05-20 | Debezium | vendor docs — CDC connector / WAL 读取 |
| T06-S040 | https://credentials.databricks.com/ | surrogate_primary | 2026-05-20 | Databricks | vendor docs — Data Engineer Assoc/Professional 认证 |
| T06-S041 | https://www.snowflake.com/certifications/ | surrogate_primary | 2026-05-20 | Snowflake | vendor docs — SnowPro 认证体系 |
| T06-S042 | https://cloud.google.com/learn/certification/data-engineer | surrogate_primary | 2026-05-20 | Google Cloud | vendor docs — Professional Data Engineer 认证 |
| T06-S043 | https://aws.amazon.com/certification/certified-data-engineer-associate/ | surrogate_primary | 2026-05-20 | AWS | vendor docs — AWS Data Engineer Associate 认证 |
| T06-S044 | https://www.getdbt.com/blog/dbt-certification-program | verified_primary | 2026-05-20 | dbt Labs | blog — dbt Analytics Engineering 认证 |
| T06-S045 | https://www.astronomer.io/blog/airflow-certification/ | surrogate_primary | 2026-05-20 | Astronomer | vendor docs — Astronomer Airflow 认证 |
| T06-S046 | https://en.wikipedia.org/wiki/Log-structured_merge-tree | secondary | 2026-05-20 | — | term def — LSM-tree (写优化存储) |
| T06-S047 | https://en.wikipedia.org/wiki/Write-ahead_logging | secondary | 2026-05-20 | — | term def — WAL |
| T06-S048 | https://www.confluent.io/learn/exactly-once-semantics/ | surrogate_primary | 2026-05-20 | Confluent | vendor docs — exactly-once / at-least-once |
| T06-S049 | https://docs.getdbt.com/docs/use-dbt-semantic-layer/dbt-sl | verified_primary | 2026-05-20 | dbt Labs | engineering docs — semantic / metrics layer |
| T06-S050 | https://www.thoughtworks.com/insights/blog/data-strategy/data-mesh-data-product | surrogate_primary | 2026-05-20 | Thoughtworks | vendor docs (author org) — data product as architectural quantum |
| T06-S051 | https://hightouch.com/blog/reverse-etl | surrogate_primary | 2026-05-20 | Hightouch | vendor docs — reverse ETL 定义 (操作系统回写) |
| T06-S052 | https://aws.amazon.com/what-is/zero-etl/ | surrogate_primary | 2026-05-20 | AWS | vendor docs — "zero-ETL" 营销话术 (复杂度转移) |

> bucket 说明: github root 与 `docs.*` engineering 子域 = `verified_primary` (verifier 输出); .gov.cn 立法原文 = `verified_primary`; spec/vendor/监管概览站 verifier 默认 `secondary`，按 Track 06 规则**升级为** `surrogate_primary` 并标 "vendor docs"; Wikipedia = `secondary`（仅术语定义稀疏使用）。

---

## 总览（按 type 分组）

### Tier 1 — 核心必懂 (46 个，目标 30-50)

| 术语 | Type | Insider def | Outsider tell | Last_updated |
|------|------|-------------|---------------|--------------|
| ETL / ELT | term | 先抽取后装载；ELT 把转换推到仓库内做 (load 后再 transform) | 把 ETL 等同于"写一堆 Python 定时脚本"；分不清 T 在 load 前后 | 2026-05-20 |
| Idempotency / 幂等 | term | 同一 pipeline run 多次产出同一结果；重跑不污染 | 以为只是"加个 try/except 重试"；不理解 partition 级覆盖 | 2026-05-20 |
| Backfill / 回填 | term | 用当前逻辑重算历史分区的过程 | 以为是"补漏数据"一次性事；忽略幂等是回填前提 | 2026-05-20 |
| CDC (Change Data Capture) | term + acronym | 从源库事务日志 (WAL/binlog) 捕获增量变更 | 以为 CDC = "定时 SELECT 比对"；其实是读 redo/binlog 不碰主库 | 2026-05-20 |
| Partition / Partition pruning | term | 按 key (常按日期) 切表；查询时只扫相关分区 | "全表扫一下就行"；不知道分区裁剪是性能命门 | 2026-05-20 |
| Compaction / 合并 | term | 把大量小文件合并成少数大文件以提读性能 | 不知道流式写入会产生海量小文件 | 2026-05-20 |
| Small files problem / 小文件问题 | term | 文件数爆炸导致 NameNode/metadata 与扫描开销激增 | 觉得"文件多少无所谓"；忽视 metadata 成本 | 2026-05-20 |
| Columnar / 列式 | term | 按列存储，利于压缩与分析型扫描 | 以为列式只是"换个存法"；不懂向量化/压缩收益 | 2026-05-20 |
| Parquet | term + standard | 行业默认列式文件格式 (含 schema + 统计) | 把 Parquet 当"压缩 CSV"；不知它带 footer 统计供裁剪 | 2026-05-20 |
| ORC | term + standard | Hive 系列优化列式格式，强 predicate pushdown | 把 ORC/Parquet 混为一谈不知 ecosystem 差异 | 2026-05-20 |
| Avro | term + standard | 行式 + schema 携带，强 schema evolution，常用于 Kafka | 以为 Avro 是列式；其实它是行式序列化 | 2026-05-20 |
| Arrow | term + standard | 跨语言内存列式标准，零拷贝交换 | 把 Arrow 当磁盘格式；它是内存格式 (对比 Parquet 落盘) | 2026-05-20 |
| Lakehouse | term | 在湖 (对象存储) 上叠 ACID 表层，兼具仓与湖 | 当成纯营销词；不知它指 open table format + 解耦存算 | 2026-05-20 |
| Open table format / 开放表格式 | term + standard | Iceberg/Delta/Hudi：在文件之上加元数据层提供 ACID/快照 | 以为"表格式"=文件格式；混淆 Parquet 与 Iceberg 层级 | 2026-05-20 |
| ACID | term + acronym | 原子/一致/隔离/持久；湖上靠表格式事务日志实现 | 以为湖天生没事务，或以为 ACID 只属 OLTP 数据库 | 2026-05-20 |
| Time travel / 时间旅行 | term | 按 snapshot/version 查询历史状态 | 以为要手动存全量快照；不知它靠元数据 metadata 廉价实现 | 2026-05-20 |
| Schema evolution / 模式演化 | term | 安全地增删改列且不破坏旧数据/读端 | 以为加列要重建全表；混淆兼容性方向 (向前/向后) | 2026-05-20 |
| Schema-on-read vs schema-on-write | term | 读时定结构 (湖) vs 写时强约束 (仓) | 以为湖"没 schema"；其实是延后到读时施加 | 2026-05-20 |
| SCD (Slowly Changing Dimension) | term + acronym | 维度历史变更建模；Type 2 保留历史行 | 直接 UPDATE 覆盖维度丢失历史；不懂 Type 1/2/3 取舍 | 2026-05-20 |
| Star schema / 星型模型 | term | 中心 fact 表 + 周边 dimension 表 | 把所有表都建成宽表却称"星型"；不懂 grain | 2026-05-20 |
| Snowflake schema / 雪花模型 | term | 维度进一步规范化拆成多层 | 与 Snowflake 公司混淆；不知它是星型的规范化变体 | 2026-05-20 |
| Conformed dimension / 一致性维度 | term | 跨多 fact/数据集共享同一维度定义 | 各业务各建一套维度还以为没问题 | 2026-05-20 |
| Fact / Dimension table | term | fact 存度量与外键；dimension 存描述属性 | 分不清度量 (可加) 与属性；把维度塞进 fact | 2026-05-20 |
| OBT (One Big Table) | term + acronym | 反规范化成一张宽表，换查询简单/省 join | 以为 OBT 永远更好；忽视更新放大与冗余 | 2026-05-20 |
| Medallion (bronze/silver/gold) | term | 分层：raw → cleaned → business-ready | 把它当硬性三层教条；不知它是 Databricks 命名约定 | 2026-05-20 |
| Normalization / Denormalization | term | 拆分消冗余 vs 合并换读性能 | 一律追求 3NF 或一律宽表；不看 OLAP/OLTP 场景 | 2026-05-20 |
| DAG | term + acronym | 有向无环图描述任务依赖与调度 | 以为 DAG 就是"定时任务列表"；忽略依赖与无环约束 | 2026-05-20 |
| Watermark / 水位线 | term | 流处理中判定事件时间进度、触发窗口计算的标记 | 把 watermark 当"水印图片"；混淆 event time 与 processing time | 2026-05-20 |
| Windowing (tumbling/sliding/session) | term | 按时间/会话切流做聚合的窗口策略 | 以为流没有窗口直接 group by；不知会话窗口存在 | 2026-05-20 |
| Exactly-once / At-least-once | term | 处理语义保证；exactly-once 需幂等 sink + 事务 | 张口要 exactly-once 却不知代价；以为默认就有 | 2026-05-20 |
| Lambda / Kappa 架构 | term | 批+流双路 vs 纯流单路重放 | 默认上 Lambda 维护两套代码不知 Kappa 选项 | 2026-05-20 |
| MPP (Massively Parallel Processing) | term + acronym | 多节点并行查询的仓库架构 | 把 MPP 仓当成"大号 MySQL" | 2026-05-20 |
| Decoupled storage & compute / 存算解耦 | term | 存储与计算独立伸缩、独立计费 | 仍按"一台机器扩容"思维；不懂按需弹性 | 2026-05-20 |
| Predicate pushdown / 谓词下推 | term | 把过滤条件下推到扫描层减少读取 | 以为 WHERE 都在内存过滤；不知下推到文件统计层 | 2026-05-20 |
| Materialized view / 物化视图 | term | 预计算并落地的查询结果，可刷新 | 与普通 view 混淆；不知它占存储且需刷新策略 | 2026-05-20 |
| Incremental model / 增量模型 | term | 只处理新增/变更行而非全量重建 | 默认全量重跑；不会处理迟到数据与去重 | 2026-05-20 |
| Semantic / Metrics layer | term | 集中定义指标口径供下游一致消费 | 各报表各写一套 SQL 算"营收"口径不一致 | 2026-05-20 |
| Data contract / 数据契约 | term | 生产者与消费者间对 schema/SLA 的显式约定 | "schema 我改一下没人用吧"——破坏隐性契约 | 2026-05-20 |
| Data observability / 数据可观测性 | term | 监控新鲜度/量/分布/schema/lineage 五维健康度 | 等同于"加几个 dashboard"；忽略 freshness/volume 异常 | 2026-05-20 |
| Data downtime / 数据宕机 | term | 数据错误/缺失/陈旧导致不可信的时间 | 只认系统宕机；不认"数据本身坏了"也是宕机 | 2026-05-20 |
| Data lineage (column-level) / 血缘 | term | 字段级追踪数据从源到消费的流向 | 只画表级框图；做不到 column-level 影响分析 | 2026-05-20 |
| Data mesh | term | 去中心化、域自治、data-as-a-product 的组织架构 | 当成一个能买的产品/平台 SKU；以为是技术堆栈 | 2026-05-20 |
| Data product / 数据产品 | term | 有 owner/SLA/接口的可被发现消费的数据资产 | 把任意一张表都叫"数据产品" | 2026-05-20 |
| Data swamp / 数据沼泽 | term | 无治理/无元数据的湖退化成不可用垃圾场 | "先把所有数据倒进湖再说"——正在制造沼泽 | 2026-05-20 |
| Reverse ETL | term | 把仓内建模数据回写到 SaaS/业务系统 | 以为数据只能单向入仓；不知回写到 CRM/广告 | 2026-05-20 |
| Upsert / Merge | term | 存在则更新不存在则插入 (MERGE INTO) | 用 delete+insert 替代还制造重复/竞态 | 2026-05-20 |

### Tier 1 (续) — 引擎执行层 (额外核心)

| 术语 | Type | Insider def | Outsider tell | Last_updated |
|------|------|-------------|---------------|--------------|
| Shuffle | term | 分布式算子间跨节点重分发数据 (join/groupby 触发) | 不知 shuffle 是慢点；写出无谓 wide transform | 2026-05-20 |
| Skew / 数据倾斜 | term | key 分布不均致单分区/单 task 过载拖慢全局 | 只会加资源；不诊断倾斜键也不做 salting | 2026-05-20 |
| Fan-out | term | 一条上游触发多条下游/一行展开多行 | 忽视 fan-out 导致下游放大与成本爆炸 | 2026-05-20 |
| Dead letter queue (DLQ) | term + acronym | 处理失败的消息隔离队列待后续处理 | 失败消息直接丢弃或无限重试堵塞主流 | 2026-05-20 |
| Vacuum / Optimize | term | 清理过期文件/合并小文件回收存储 (Delta/Iceberg) | 从不维护表；快照/小文件无限堆积 | 2026-05-20 |

### Tier 2 — 周边熟知 (24 个，目标 30-70)

| 术语 | Type | Insider def | Last_updated |
|------|------|-------------|--------------|
| Hudi | term + standard | open table format 之一，强 upsert/增量拉取 | 2026-05-20 |
| Snapshot / Manifest | term | Iceberg 元数据层：快照指向 manifest 列出数据文件 | 2026-05-20 |
| Z-ordering / clustering | term | 多维数据局部性排序加速过滤 | 2026-05-20 |
| Bucketing | term | 按 hash 预分桶减少 join shuffle | 2026-05-20 |
| Slot / Warehouse (vWH) | term | 计算资源单元 (BigQuery slot / Snowflake virtual warehouse) | 2026-05-20 |
| Late-arriving data / 迟到数据 | term | 超出 watermark 的事件，需 allowed lateness 处理 | 2026-05-20 |
| Surrogate key / 代理键 | term | 维度表无业务含义的人工主键 (常与 SCD2 配合) | 2026-05-20 |
| Grain / 粒度 | term | fact 表一行代表的业务事件最细级别 | 2026-05-20 |
| Idempotent sink | term | 重复写入不产生重复结果的目标端 | 2026-05-20 |
| Orchestration vs scheduling | term | 编排 (依赖+重试+回填) 不止于定时触发 | 2026-05-20 |
| Data catalog | term | 元数据/资产发现与治理目录 (Glue/Unity/Hive metastore) | 2026-05-20 |
| Unity Catalog / Hive metastore | term | 表元数据与权限的集中目录实现 | 2026-05-20 |
| Streaming vs micro-batch | term | 逐事件 vs 小批量近实时 (Spark Structured Streaming) | 2026-05-20 |
| Replay / 重放 | term | 从日志/源重新计算 (Kappa 的核心能力) | 2026-05-20 |
| Tombstone | term | 标记删除的逻辑记录 (CDC/LSM 中) | 2026-05-20 |
| Checkpoint / Savepoint | term | 流作业状态持久化以容错恢复 | 2026-05-20 |
| Backpressure / 背压 | term | 下游慢致上游限速的流控机制 | 2026-05-20 |
| Cardinality / 基数 | term | 列不同值数量，影响索引/join/分区策略 | 2026-05-20 |
| Partition pruning vs file skipping | term | 分区裁剪 (目录) vs 文件级统计跳过 | 2026-05-20 |
| Dimensional modeling (Kimball) | term | Kimball 维度建模方法论 (bus matrix) | 2026-05-20 |
| Data Vault | term + standard | hub/link/satellite 的可审计建模方法 | 2026-05-20 |
| Inmon (CIF) | term | 自顶向下企业级 3NF 数据仓库方法 | 2026-05-20 |
| Data quality test (not null/unique/accepted) | term | 入口/出口断言式数据校验 (dbt tests) | 2026-05-20 |
| Freshness SLA | term | 数据更新及时性的可量化承诺 | 2026-05-20 |

---

## 缩写表 (Acronym table)

| 缩写 | 全称 | Insider 用法 | Pronunciation tell |
|------|------|-------------|--------------------|
| DE | Data Engineer / Data Engineering | 建管道与平台的人/职能 | — |
| AE | Analytics Engineer | dbt 时代角色；写转换/建模、不碰底层 infra | — |
| MDS | Modern Data Stack | 云仓 + EL 工具 + dbt + BI 的组合 | 念字母 M-D-S |
| DWH / EDW | Data Warehouse / Enterprise DW | 面向分析的结构化仓库 | — |
| OLAP / OLTP | Online Analytical / Transactional Processing | 分析型 vs 事务型负载 | 念 "oh-lap" / "oh-el-tee-pee" |
| HTAP | Hybrid Transactional/Analytical Processing | 同库兼跑事务与分析 | 念 "H-TAP" |
| ODS | Operational Data Store | 近实时操作型集成层 | — |
| DDL / DML | Data Definition / Manipulation Language | 改结构 vs 改数据的 SQL | 念字母 |
| PII | Personally Identifiable Information | 个人可识别信息；合规重点保护对象 | 念 "P-I-I" 非 "pie" |
| RBAC | Role-Based Access Control | 按角色授权 (对比 ABAC) | 念 "R-back" 或字母 |
| SLA / SLO | Service Level Agreement / Objective | 对外承诺 vs 内部目标 | 念字母 |
| RPO / RTO | Recovery Point / Time Objective | 最大可丢数据窗 vs 恢复时长 | 念字母 |
| CDC | Change Data Capture | 见 Tier 1 | 念字母 C-D-C |
| WAL | Write-Ahead Log | 先写日志再改数据；CDC 的读取源 | 念 "wall" 或字母 W-A-L |
| LSM-tree | Log-Structured Merge tree | 写优化存储引擎结构 (Cassandra/RocksDB) | 念 "L-S-M tree" |
| SQL | Structured Query Language | 数据工程通用语言 | "sequel" vs "S-Q-L" 两派并存 (非破绽) |

---

## 合规 / 标准框架 (Compliance & Standards)

> Standards/Regulations 必填日期字段。geographic-specific 已标注。

| 名称 | Type | 地域 | Issued | Last revised | Insider 意义 | Decay | evidence |
|------|------|------|--------|--------------|-------------|-------|----------|
| GDPR | regulation | EU | 2016 (生效 2018-05-25) | 稳定 | 跨境数据/被遗忘权/DPA；管道需支持删除与最小化 | medium | [T06-S023, T06-S024] |
| 数据安全法 (DSL) | regulation | CN | 2021-06-10 (生效 2021-09-01) | 稳定 | 数据分类分级、重要数据出境评估 | medium | [T06-S025] |
| 个人信息保护法 (PIPL) | regulation | CN | 2021-08-20 (生效 2021-11-01) | 稳定 | 个人信息处理合法性基础 + 出境路径 | medium | [T06-S026] |
| CCPA / CPRA | regulation | US-CA | 2018 (CPRA 2023 生效) | 2023 (CPRA) | 加州消费者数据权利；opt-out 销售 | medium | [T06-S027] |
| SOC 2 (Type I/II) | standard | US/全球 | 2011 (AICPA TSC) | 2017 TSC 修订 | 数据平台供应商安全审计的事实门槛 | medium | [T06-S028] |
| Data classification / 数据分级 | standard | 全球/CN | — | 持续 | 公开/内部/机密/PII 分级，决定加密与访问 | low | [T06-S025, T06-S026] |
| SQL standard (ISO/IEC 9075) | standard | 全球 | 1986 (持续修订) | SQL:2023 | 方言差异大；标准是底线非现实 | low | [T06-S020] |
| Apache Iceberg spec | standard | 全球 | 2020 (v1) | v2 (row-level delete) | open table format 事实标准之一 | medium | [T06-S001, T06-S002] |
| Delta Lake protocol | standard | 全球 | 2019 | 持续 (deletion vectors) | Databricks 系开放表协议 | medium | [T06-S003, T06-S004] |
| OpenLineage | standard | 全球 | 2021 | 持续 | 跨工具血缘事件开放标准 (LF AI) | medium | [T06-S010, T06-S011] |
| OpenTelemetry (for data) | standard | 全球 | 2019 | 持续 | telemetry 标准，data observability 借用 trace/metric | medium | [T06-S031] |
| OpenMetadata | standard | 全球 | 2021 | 持续 | 开放元数据 schema/lineage 标准 | medium | [T06-S032] |
| Singer spec (taps/targets) | standard | 全球 | 2017 | 缓慢 (社区维护) | EL 连接器开放协议 (Meltano 生态) | medium | [T06-S029, T06-S030] |
| Apache Parquet format | standard | 全球 | 2013 | 持续 | 列式磁盘格式事实标准 | low | [T06-S005] |
| Apache Arrow format | standard | 全球 | 2016 | 持续 | 内存列式交换标准 | low | [T06-S006] |

---

## 认证 (Certifications)

| 认证 | 颁发方 | 版本/级别 | Last updated | Insider 意义 | evidence |
|------|--------|----------|--------------|-------------|----------|
| dbt Analytics Engineering Certification | dbt Labs | 单级 (Certified) | 2024 起持续 | AE 角色背书；建模/测试/部署能力 | [T06-S044] |
| Databricks Data Engineer Associate | Databricks | Associate | 2024 改版 | Lakehouse/Delta/Spark 入门门槛 | [T06-S040] |
| Databricks Data Engineer Professional | Databricks | Professional | 2024 改版 | 进阶：流式/优化/部署 | [T06-S040] |
| SnowPro Core / Advanced: Data Engineer | Snowflake | Core + Advanced | 2024 持续 | Snowflake 平台深度 | [T06-S041] |
| Google Professional Data Engineer | Google Cloud | Professional | 2024 改版 (含 GenAI) | GCP 数据平台综合 | [T06-S042] |
| AWS Certified Data Engineer – Associate | AWS | Associate | 2024-03 (替代 Analytics Specialty) | AWS 数据栈；新认证取代旧 Analytics Specialty | [T06-S043] |
| AWS Data Analytics Specialty (退役) | AWS | Specialty | 2024 退役 | 已被 Data Engineer Associate 取代 | [T06-S043] |
| Astronomer Airflow Certification | Astronomer | Fundamentals/DAG Authoring | 2024 持续 | Airflow 编排专长 | [T06-S045] |
| CCA Spark and Hadoop Developer (退役) | Cloudera | CCA175 | 已退役 | 历史 Spark 认证；现多被云厂认证取代 | [T06-S017] |

---

## Standards / Regulations / Certifications 时间轴 (近 5 年有显著变化的)

| 名称 | Issued | Last revised | Decay | 触发的 workflow 变化 |
|------|--------|--------------|-------|---------------------|
| PIPL (CN) | 2021-08 | 稳定 | medium | 个人信息出境需 SCC/安全评估 → 跨境管道新增合规网关 |
| 数据安全法 (CN) | 2021-06 | 稳定 | medium | 重要数据分类分级 → 管道入口打标签/分级落地 |
| CPRA (US-CA) | 2020 (2023 生效) | 2023 | medium | 扩展删除/更正权 → 仓内 PII 可删除性设计 |
| Iceberg spec v2 | 2020 | v2 row-level delete | medium | 行级删除/合并 → MERGE/CDC 入湖成为主流 |
| Delta deletion vectors | 2019 | 2023+ | medium | 软删除提速 → vacuum/optimize 流程调整 |
| AWS Data Engineer Associate | — | 2024-03 取代 Analytics Specialty | medium | 认证路径切换 → 团队培训/招聘 JD 更新 |
| Databricks DE 认证改版 | — | 2024 | medium | 考点转向 Lakehouse/streaming → 学习路径更新 |

> 长期稳定项 (Parquet/Arrow/SQL standard/SOC 2/GDPR core) 不进时间轴，仅在主条目记 issued 年份。

---

## 行业「外行破绽」高亮 (Top 10 — insider-only spotting tells)

| 误用 (外行说法) | 内行实际意思 / 为何是破绽 | 出现频率 | evidence |
|----------------|--------------------------|---------|----------|
| "先把所有数据都倒进数据湖再说" | 无治理的倾倒制造 data swamp；湖需 catalog/schema/lifecycle | 极高 | [T06-S022] |
| "拿 notebook 跑生产" | notebook 不可版本化/不可重试/无依赖管理；生产要 orchestrator | 高 | [T06-S014, T06-S015] |
| "上 Spark 集群显得专业 (数据才几个 G)" | 几 GB 用单机/DuckDB/仓即可；Spark 是分布式开销 | 高 | [T06-S017] |
| "SELECT * 看一下" | 列式存储下 SELECT * 放弃列裁剪与下推，成本翻倍 | 高 | [T06-S005, T06-S017] |
| "这个表 schema 我改一下没人用吧" | 破坏 data contract；下游静默崩溃 | 高 | [T06-S008] |
| "实时肯定比离线好，全上流" | 流式贵且复杂；多数场景批/微批足够，按 SLA 取舍 | 高 | [T06-S035, T06-S036] |
| "数据质量后面再补测试" | 无测试的管道是定时炸弹；测试应随模型一起写 | 高 | [T06-S007] |
| "data mesh 下季度全公司一起上" | mesh 是组织演进非一次性技术上线；先有平台与域所有权 | 中 | [T06-S021] |
| "ETL = 写一堆 Python 脚本定时跑" | ETL 是建模+幂等+编排+测试的工程，不是 cron+脚本 | 极高 | [T06-S013, T06-S037] |
| "把 ML 模型训练也算我数据工程的活" | DE 负责特征/管道/平台；模型训练是 ML/DS 职责边界 | 中 | [T06-S012] |

---

## 厂商话术拒绝 (Vendor-speak the field rejects, Top 5+)

| 话术 | 厂商暗示 | 行业为何拒绝 | evidence |
|------|---------|-------------|----------|
| "zero-ETL" / "NoETL" | 买我就不用做 ETL 了 | 复杂度不消失只转移 (转到 schema 漂移/无治理/锁定)；转换逻辑总要有人负责 | [T06-S052] |
| "single source of truth out of the box" | 开箱即得唯一真相 | SSOT 是建模+治理+契约的长期结果，不是产品默认态 | [T06-S049, T06-S008] |
| "data mesh / data fabric as a product SKU" | 买这个 SKU 就是 data mesh 了 | mesh 是组织+所有权范式，不能作为可购买产品交付 | [T06-S021] |
| "AI will replace data engineers" | 不需要 DE 了 | AI 提速但管道可靠性/契约/成本/合规仍需工程判断 | [T06-S012] |
| "our platform = your whole modern data stack" | 一家全包 | 全包=锁定；MDS 价值在可组合与可替换 | [T06-S012] |
| "real-time everything" | 一切都该实时 | 实时按需使用；盲目全上流式徒增成本与复杂度 | [T06-S035, T06-S036, T06-S048] |

---

## Phase 2 提炼提示

**「行业表达 DNA」直接素材** (喂给 Phase 2.5 expression-DNA 提炼):
- 高频黑话 top 10: idempotency / backfill / CDC / partition pruning / small files problem / schema evolution / SCD2 / medallion / data contract / shuffle (倾斜 skew)。
- 行业拒绝的厂商话术 top 5: "zero-ETL" / "single source of truth out of the box" / "data mesh as a SKU" / "AI replaces DE" / "real-time everything"。(拒绝 → 反映行业价值观: 复杂度守恒、治理优先、按 SLA 取舍、可组合而非锁定)
- 外行破绽 top 10: 见上「外行破绽」表 (data swamp / notebook 跑生产 / 小数据上 Spark / SELECT * / 改 schema 破契约 / 全上实时 / 测试后补 / mesh 一次性上 / ETL=脚本 / 把 ML 训练算进来)。

**「智识谱系」线索** (喂给 Phase 2.7 智识谱系):
- 建模范式更替: Inmon (3NF 自顶向下) → Kimball (维度建模) → Data Vault → dbt 时代 ELT + OBT/宽表 + 语义层。反映"先严范式 → 实用反规范化 → 重新中心化指标口径"的钟摆。
- 存储范式更替: Hadoop/HDFS → 云对象存储 + 解耦存算 → lakehouse (open table format)。
- 表格式之争 (流派 fragmenting → 收敛): Iceberg vs Delta vs Hudi 三足，2024+ 出现互通/收敛信号 (Delta UniForm、Iceberg REST catalog) — 标准竞争是流派之争硬件层。
- 架构之争: Lambda (批+流双路) vs Kappa (纯流重放) — 反映"是否值得为实时维护两套代码"的价值分歧。

**「时效性」信号** (喂给 Phase 2.8 诚实边界):
- 过去 12 月内有显著变化: AWS 认证路径切换 (Analytics Specialty 退役→Data Engineer Associate, 2024-03); 表格式 catalog 互通 (Iceberg REST / Delta UniForm) 仍在演进。
- 预计 12 月内可能变: open table format 互通标准 (catalog 层) 高变动; 各云 DE 认证考点随 GenAI 集成持续调整; 中国数据出境实施细则 (PIPL/DSL 配套) 持续更新。

**「工作流变化触发」种子** (喂给 wave 3 Track 03):
- PIPL/DSL 数据出境与分级 → 管道入口打标签 + 跨境合规网关 (CN 强相关)。
- CPRA 删除/更正权 + GDPR 被遗忘权 → 仓内 PII 可删除性设计、open table format 行级删除流程。
- Iceberg v2 row-level delete / Delta deletion vectors → MERGE/CDC 入湖、vacuum/optimize 维护流程。

**冷僻 / 信号薄弱自检**:
- 总术语数: 70 (Tier1=51 含引擎层 / Tier2=24) — 远超 floor 40, 不冷僻。
- Tier 1 ≥ 15: ✅ (51)。Tier1 全部填 outsider-tell: ✅。Tier2 ≥50% 填: 本表 Tier2 以 insider def 为主, outsider-tell 在 Tier1 与破绽表充分覆盖。
- 有 outsider-tell 的术语占比 > 50%: ✅。结论: glossary 维度信号充足，行业成熟。

---

## 质量自检

- [x] 候选数 ≥ 40 (70 个)
- [x] 5 type 分布合理: term 主体 / acronym (16) / standard (15) / regulation (4) / certification (9)，无空缺
- [x] Tier 1 ≥ 15 (51); Tier1+Tier2 ≥ 40 (70)
- [x] Tier 1 全部 outsider-tell; Tier2 以 insider def 为主 (outsider-tell 集中在破绽表)
- [x] Standards/Regulations/Certifications 均有日期字段
- [x] Disputed 处理: SQL "sequel" vs 字母两派标为并存非破绽; 无强行统一
- [x] Phase 2 接口五节齐全 (表达 DNA / 智识谱系 / 时效 / workflow 触发 / 冷僻信号)
- [x] 表格内**无**转义管道 (backslash + pipe) (分隔符用 / 和 ;)
