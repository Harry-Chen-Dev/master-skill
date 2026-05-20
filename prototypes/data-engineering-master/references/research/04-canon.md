# Track 04 — Data Engineering 知识正典 (Canon)

> Phase 1 wave 1 输出。Industry = **Data Engineering / 数据工程**。locale = **en** (en-primary, zh-CN secondary)。
> 调研日期 2026-05-20。本文件是「资深人真正读过 / 学过 / 引用过的核心文本 + 概念」，不是 awesome-X 推荐列表。

## ⚠️ Locale 诚实声明 (zh-CN canon 薄)

数据工程的 canon **压倒性是英文一手**：奠基书 (DDIA / Fundamentals / Kimball / Streaming Systems / Data Mesh) 全部英文原版，奠基论文 (MapReduce / GFS / Dataflow / Spark RDD / Lakehouse) 全部英文学术，奠基长文 (Maxime / Jay Kreps / Zhamak) 全部英文。中文读者主要消费 **翻译版** (DDIA《数据密集型应用系统设计》中译广泛流传) + **Apache 项目官方文档** + **极客时间 / DataFun 专栏**。中国一手贡献集中在工具层 (Flink SQL / 流批一体 / DolphinScheduler / Doris / StarRocks / Paimon)，不在 canon 著作层。本 track 的 canon 列表因此 ~90% 英文。Phase 2 接口已 flag。

---

## Source Manifest

> bucket 由 `tools/research/source_verifier.py classify` 跑出。`.io/.com/.org/.dev/.medium.com(作者官方)/.apache.org` 出版社/作者/项目一手 → 人工标 `surrogate_primary` + note 含 literal **"vendor docs"** (任务规则)。arxiv / .edu / research.google / usenix / cidrdb / engineering.linkedin.com 自动 `verified_primary` 保留。github repo root 自动 primary。黑名单 URL 不入表。

| source_id | url | bucket | last_checked | author/host | one-line note |
|-----------|-----|--------|--------------|-------------|---------------|
| T04-S001 | https://dataintensive.com | surrogate_primary | 2026-05-20 | Martin Kleppmann | vendor docs (作者一手 — DDIA 数据系统正典书官网) |
| T04-S002 | https://www.oreilly.com/library/view/fundamentals-of-data/9781098108298/ | surrogate_primary | 2026-05-20 | O'Reilly | vendor docs (出版社一手 — Fundamentals of Data Engineering) |
| T04-S003 | https://www.kimballgroup.com/data-warehouse-business-intelligence-resources/books/data-warehouse-dw-toolkit/ | surrogate_primary | 2026-05-20 | Kimball Group | vendor docs (作者一手 — 维度建模奠基, 站存档) |
| T04-S004 | https://www.oreilly.com/library/view/streaming-systems/9781491983867/ | surrogate_primary | 2026-05-20 | O'Reilly | vendor docs (出版社一手 — Streaming Systems) |
| T04-S005 | https://www.oreilly.com/library/view/data-mesh/9781492092384/ | surrogate_primary | 2026-05-20 | O'Reilly | vendor docs (出版社一手 — Data Mesh, Zhamak) |
| T04-S006 | https://maximebeauchemin.medium.com/the-rise-of-the-data-engineer-91be18f1e603 | surrogate_primary | 2026-05-20 | Maxime Beauchemin | vendor docs (作者官方 Medium — Rise of the Data Engineer) |
| T04-S007 | https://maximebeauchemin.medium.com/functional-data-engineering-a-modern-paradigm-for-batch-data-processing-2327ec32c42a | surrogate_primary | 2026-05-20 | Maxime Beauchemin | vendor docs (作者官方 Medium — Functional Data Engineering) |
| T04-S008 | https://maximebeauchemin.medium.com/the-downfall-of-the-data-engineer-5bfb701e5d6b | surrogate_primary | 2026-05-20 | Maxime Beauchemin | vendor docs (作者官方 Medium — Downfall of the Data Engineer) |
| T04-S009 | https://engineering.linkedin.com/distributed-systems/log-what-every-software-engineer-should-know-about-real-time-datas-unifying | verified_primary | 2026-05-20 | Jay Kreps / LinkedIn Eng | The Log 奠基文原文托管处 |
| T04-S010 | https://martinfowler.com/articles/data-mesh-principles.html | surrogate_primary | 2026-05-20 | Zhamak Dehghani / M.Fowler | vendor docs (作者一手 — data mesh 4 原则文托管处) |
| T04-S011 | https://martinfowler.com/articles/data-monolith-to-mesh.html | surrogate_primary | 2026-05-20 | Zhamak Dehghani / M.Fowler | vendor docs (作者一手 — data mesh 第 1 篇 2019) |
| T04-S012 | https://www.vldb.org/pvldb/vol8/p1792-Akidau.pdf | surrogate_primary | 2026-05-20 | Akidau et al / VLDB | vendor docs (会议/协会 — Dataflow Model VLDB 2015) |
| T04-S013 | https://research.google/pubs/pub62/ | verified_primary | 2026-05-20 | Dean & Ghemawat / Google | MapReduce OSDI 2004 论文页 |
| T04-S014 | https://research.google/pubs/pub51/ | verified_primary | 2026-05-20 | Ghemawat et al / Google | GFS Google File System SOSP 2003 |
| T04-S015 | https://research.google/pubs/pub27898/ | verified_primary | 2026-05-20 | Melnik et al / Google | Dremel VLDB 2010 (BigQuery 引擎奠基) |
| T04-S016 | https://www.usenix.org/system/files/conference/nsdi12/nsdi12-final138.pdf | surrogate_primary | 2026-05-20 | Zaharia et al / NSDI | vendor docs (会议/协会 — Spark RDD NSDI 2012) |
| T04-S017 | https://www.cidrdb.org/cidr2021/papers/cidr2021_paper17.pdf | verified_primary | 2026-05-20 | Armbrust/Zaharia / CIDR | Lakehouse CIDR 2021 论文 |
| T04-S018 | https://motherduck.com/blog/big-data-is-dead/ | verified_primary | 2026-05-20 | Jordan Tigani / MotherDuck | "Big Data is Dead" 长文 |
| T04-S019 | https://docs.getdbt.com | verified_primary | 2026-05-20 | dbt Labs | dbt 官方文档 — analytics engineering 事实标准 |
| T04-S020 | https://github.com/DataTalksClub/data-engineering-zoomcamp | verified_primary | 2026-05-20 | DataTalks.Club | 免费实操课 repo (github root 自动 primary) |
| T04-S021 | https://15445.courses.cs.cmu.edu/fall2024/ | verified_primary | 2026-05-20 | Andy Pavlo / CMU | CMU 15-445 数据库系统课 (.edu) |
| T04-S022 | https://www.oreilly.com/library/view/data-pipelines-pocket/9781492087823/ | surrogate_primary | 2026-05-20 | O'Reilly | vendor docs (出版社一手 — Data Pipelines Pocket Reference) |
| T04-S023 | https://www.oreilly.com/library/view/data-quality-fundamentals/9781098112035/ | surrogate_primary | 2026-05-20 | O'Reilly | vendor docs (出版社一手 — Data Quality Fundamentals) |
| T04-S024 | https://www.oreilly.com/library/view/the-data-warehouse/9781119228431/ | surrogate_primary | 2026-05-20 | O'Reilly/Wiley | vendor docs (出版社一手 — Data Warehouse Lifecycle Toolkit) |
| T04-S025 | https://www.oreilly.com/radar/questioning-the-lambda-architecture/ | surrogate_primary | 2026-05-20 | Jay Kreps / O'Reilly | vendor docs (作者一手 — Kappa 架构提出文) |
| T04-S026 | http://nathanmarz.com/blog/how-to-beat-the-cap-theorem.html | surrogate_primary | 2026-05-20 | Nathan Marz | vendor docs (作者一手 — Lambda 架构原始文) |
| T04-S027 | https://iceberg.apache.org/ | surrogate_primary | 2026-05-20 | Apache Iceberg | vendor docs (Apache 项目一手 — 开放表格式) |
| T04-S028 | https://delta.io/ | surrogate_primary | 2026-05-20 | Delta Lake / Linux Fdn | vendor docs (项目一手 — 开放表格式) |
| T04-S029 | https://www.databricks.com/blog/2020/01/30/what-is-a-data-lakehouse.html | surrogate_primary | 2026-05-20 | Databricks | vendor docs (厂商一手 — lakehouse 术语推广) |
| T04-S030 | https://research.google/pubs/pub27/ | verified_primary | 2026-05-20 | Chang et al / Google | Bigtable OSDI 2006 论文页 |
| T04-S031 | https://www.montecarlodata.com/blog-what-is-data-observability/ | surrogate_primary | 2026-05-20 | Barr Moses / Monte Carlo | vendor docs (厂商一手 — data downtime 品类) |
| T04-S032 | https://dataproducts.substack.com/p/the-rise-of-data-contracts | surrogate_primary | 2026-05-20 | Chad Sanderson | vendor docs (作者一手 Substack — data contracts) |
| T04-S033 | https://www.startdataengineering.com/post/code-patterns/ | surrogate_primary | 2026-05-20 | Joseph Machado | vendor docs (作者一手 — idempotency/pipeline 教程) |
| T04-S034 | https://benn.substack.com/p/the-modern-data-experience | surrogate_primary | 2026-05-20 | Benn Stancil | vendor docs (作者一手 Substack — MDS 评论) |
| T04-S035 | https://www.getdbt.com/blog/what-is-analytics-engineering | surrogate_primary | 2026-05-20 | dbt Labs / Tristan Handy | vendor docs (厂商一手 — analytics engineering 运动) |

---

## 总览（按类型分组）

### Textbook / 系统性著作（必读 5 / 推荐 4）

| 书名 | 作者 | 年 | 难度 | Endorsement | 一句话 |
|------|------|----|----|-------------|--------|
| Designing Data-Intensive Applications (DDIA) | Martin Kleppmann | 2017 | 进阶 | course + figure + conf | THE 数据系统第一性原理书, 全行业「读过没」的暗号 |
| Fundamentals of Data Engineering | Joe Reis & Matt Housley | 2022 | 入门-进阶 | figure + course + conf | 数据工程生命周期框架 (生成→服务 + 6 暗流), 角色定义书 |
| The Data Warehouse Toolkit | Ralph Kimball & Margy Ross | 2013 (3e) | 进阶 | course + conf + book | 维度建模圣经 (star schema / SCD / 一致性维度) |
| Streaming Systems | Akidau / Chernyak / Lax | 2018 | 高阶 | figure + conf + book | 批流统一理论 (Dataflow model 的书本化), watermark/窗口权威 |
| Data Mesh | Zhamak Dehghani | 2022 | 进阶 | figure + conf + book | 去中心化数据架构 (域所有权+数据即产品+联邦治理) |
| The Data Warehouse Lifecycle Toolkit | Kimball Group | 2008 (2e) | 进阶 | book + conf | Kimball 方法论的端到端实施手册 (建模+ETL+BI 全流程) |
| Building the Data Warehouse | Bill Inmon | 2005 (4e) | 进阶 | book + conf | CIF 规范化企业数仓奠基 (与 Kimball 范式之争另一极) |
| Data Pipelines Pocket Reference | James Densmore | 2021 | 入门 | book + blog | 现代 EL/ELT 管道的最小可用动手指南 |
| Data Quality Fundamentals | Barr Moses et al | 2022 | 进阶 | figure + book | data observability / data downtime 的体系化 |

### Seminal Papers / 奠基长文（必读 8 + 推荐 4）

| 标题 | 年 | 核心 idea | Endorsement |
|------|----|----------|-------------|
| The Log (Jay Kreps) | 2013 | 日志是流/批/复制的统一抽象, Kafka 思想根 | figure + conf + book |
| Functional Data Engineering (Maxime) | 2018 | 幂等+不可变分区+纯函数式批处理 | figure + conf |
| The Rise / Downfall of the Data Engineer (Maxime) | 2017/2021 | DE 是软件工程, 不是 report monkey | figure + conf |
| MapReduce (Dean & Ghemawat) | 2004 | 大规模批处理编程模型, 大数据时代起点 | course + book |
| The Dataflow Model (Akidau et al) | 2015 | 批流统一的理论框架 (event-time/watermark/trigger) | book + conf |
| Spark: RDD (Zaharia et al) | 2012 | 内存弹性分布式数据集, 取代 MapReduce | course + book |
| Lakehouse (Armbrust/Zaharia) | 2021 | 湖上加事务表层 = 湖+仓合一 | conf + book |
| Big Data is Dead (Jordan Tigani) | 2023 | 多数数据塞得进单机, 反过度分布式 | figure + conf |
| GFS / Bigtable / Dremel (Google) | 2003/06/10 | 分布式存储 + 列存查询的工程奠基 | course + book |
| Data Mesh 4 原则 (Zhamak, martinfowler) | 2019-20 | 书前身, 域所有权奠基文 | figure + conf |
| Questioning the Lambda Architecture (Kreps) | 2014 | Kappa 架构 — 用单流引擎替双链路 | conf + book |
| Lambda Architecture (Nathan Marz) | 2011 | 批层+速度层+服务层 (历史性, 多被 supersede) | book + conf |

### Courses（必看 3 / 推荐 1）

| 课程 | 讲师/机构 | 格式 | Last_updated | 一句话 |
|------|----------|------|-------------|--------|
| dbt Learn / dbt Fundamentals | dbt Labs | rolling 互动 | 2026-05 (rolling) | analytics engineering 事实标准的官方上手 |
| Data Engineering Zoomcamp | DataTalks.Club | rolling 免费实操 | 2025-01 cohort | 端到端建管道 (Docker→Kafka→Spark→dbt→BigQuery) |
| CMU 15-445/645 Database Systems | Andy Pavlo / CMU | 视频+lab | 2024 fall | 数据库内核 (存储/索引/查询/事务) 一手理解 |
| DDIA (作为自学课程读) | Kleppmann | 读+讨论 | 2017 (2e 在写) | 配合 DDIA 章节的分布式系统自学路径 |

### Core Concepts（27 个）

| 概念 | 一句话定义 | 来源 |
|------|-----------|------|
| Idempotency / 幂等 | 同一任务重跑结果一致, pipeline 第一公民 | Maxime Functional DE |
| Partitioning / 分区 | 按 key 切表减少扫描, 成本+并行的核心 | Kimball; 表格式社区 |
| CDC / 变更数据捕获 | 从源库 binlog/WAL 捕获增量变更 | Debezium; The Log |
| ELT vs ETL | 转换推到数仓内做 (E-L-T) 而非加载前 | dbt; Fundamentals |
| 维度建模 / star schema / SCD | 事实+维度星型 + 渐变维记录历史 | Kimball Toolkit |
| 规范化 / Normalization | 去冗余的关系建模 (Inmon CIF 取向) | Inmon; DDIA |
| Lakehouse / 湖仓一体 | 对象存储 + 事务表层 = 湖+仓合一 | Lakehouse CIDR 2021 |
| Open table format / 开放表格式 | Iceberg/Delta/Hudi 给湖上文件加表语义 | Iceberg; Delta |
| ACID on object store | 在 S3 等最终一致存储上做原子提交 | Iceberg; Lakehouse |
| Time travel / 时间旅行 | 按快照/版本查历史数据 | Iceberg; Delta |
| Schema evolution / schema 演进 | 表结构向后兼容地增改 (新增不删) | DDIA; Iceberg |
| Watermark / Windowing | 流处理处理乱序+界定窗口完整性 | Dataflow; Streaming Systems |
| Exactly-once | 故障重放下精确一次语义 | Streaming Systems; Flink |
| Lambda / Kappa 架构 | 批+速度双层 vs 单流统一 | Marz; Kreps Kappa |
| Medallion 架构 | bronze/silver/gold 分层提纯 | Databricks; dbt 社区 |
| Data contract / 数据契约 | producer-consumer 显式 schema 约定 | Chad Sanderson |
| Data observability / data downtime | 数据五维健康监控 + 错误数据成本 | Barr Moses |
| Columnar storage / 列存 | 按列存压缩+只读所需列 (Parquet/ORC) | Dremel; Arrow |
| Predicate pushdown / 谓词下推 | 把过滤推到存储层减少扫描 | Dremel; 查询引擎社区 |
| MPP / 大规模并行处理 | 多节点分片并行查询 | DDIA; 数仓社区 |
| 存算分离 / Decoupled storage&compute | 计算与存储独立伸缩 | Snowflake; Lakehouse |
| Backfill / 回填 | 用新逻辑重算历史分区 (需幂等) | Maxime; Airflow 社区 |
| Semantic / metrics layer / 语义层 | 指标定义一次, 全栈一致 | dbt MetricFlow; Benn |
| Data mesh / 数据网格 | 域所有权 + 数据即产品 + 联邦治理 | Zhamak |
| OBT / One Big Table / 大宽表 | 列存时代去 join 的宽表建模 | dbt 社区; Kimball 对照 |
| Small files problem / 小文件 | 海量小文件拖垮元数据+扫描 | Hudi; Iceberg compaction |
| DataOps | 数据的 CI/CD + 测试 + 环境隔离纪律 | Maxime; dbt; Fundamentals |

---

## 📖 Books / 系统性著作（详条）

### 📖 1. Designing Data-Intensive Applications (DDIA)

- **Author**: Martin Kleppmann (Cambridge, 前 LinkedIn)
- **Year**: 2017 (1e); 2e 在写 (草稿连载中)
- **Type**: textbook / 系统性著作
- **One-liner**: 数据工程师的「物理学」——存储引擎 / 复制 / 分区 / 事务 / 一致性 / 批流处理的第一性原理，全行业判断一个人是否「真懂」的暗号书。
- **核心论点 (3-5)**:
  - 没有银弹存储——B-tree vs LSM-tree、行存 vs 列存各有取舍，选型看读写模式 (evidence: [T04-S001])
  - 可靠/可扩展/可维护是数据系统的三个基本目标 (evidence: [T04-S001])
  - 复制+分区+事务+共识是分布式数据系统的四大支柱
  - 批处理 (MapReduce 谱系) 与流处理 (日志谱系) 在抽象上正在收敛
  - 编码与 schema 演进——序列化格式 (Avro/Protobuf) 决定系统能否平滑升级
- **读完得到什么**: 能在 Snowflake / Kafka / Iceberg 之上看到底层共性，不被厂商术语绑架；面试与架构选型的共同语言。
- **难度**: 进阶 (需要基本系统/网络/SQL 背景)
- **Endorsement evidence**:
  - `[type: course_syllabus]` 几乎所有数据工程/分布式系统自学路径与大学课程列为必读 (evidence: [T04-S001])
  - `[type: figure_long]` Joe Reis / Maxime 等反复在长访谈与书中引用为先修 (evidence: [T04-S002])
  - `[type: conf_citation]` Data Council / 数据系统 talk 默认引用基线 (evidence: [T04-S001])
- **是否被新版 supersede**: 2e 在写，但 1e 仍是事实标准；不 DROP。
- **如果可以只读 1 章**: Ch.3 (存储与检索, LSM vs B-tree) 或 Ch.11 (流处理)。
- **可信度**: high / **Decay risk**: low (原理性, 工具会变原理不变)

### 📖 2. Fundamentals of Data Engineering

- **Author**: Joe Reis & Matt Housley (Ternary Data)
- **Year**: 2022
- **Type**: textbook / 框架性著作
- **One-liner**: 给「数据工程」这个职业下定义的书——数据工程生命周期 (生成→摄取→存储→转换→服务) + 6 条暗流 (安全/数据管理/DataOps/数据架构/编排/软件工程)。
- **核心论点 (3-5)**:
  - 数据工程 = 生命周期，而非某个工具；工具会换，生命周期阶段不变 (evidence: [T04-S002])
  - 「暗流」(undercurrents) 贯穿全生命周期，安全/治理/DataOps 不是事后补 (evidence: [T04-S002])
  - 工具选型应 build-vs-buy + 总拥有成本驱动，不是追新
  - 拥抱常识与「足够好」架构，警惕过度工程
- **读完得到什么**: 一张能挂在墙上的全局地图；能判断一个数据团队缺哪一环。
- **难度**: 入门-进阶 (新人入行第一本 / 老兵补全局)
- **Endorsement evidence**:
  - `[type: figure_long]` 作者 Joe Reis 在 podcast/Substack 长篇展开框架 (evidence: [T04-S002])
  - `[type: course_syllabus]` 大量 bootcamp / Zoomcamp 列为配套读物 (evidence: [T04-S020])
  - `[type: conf_citation]` Data Council 等会议常引「生命周期」框架
- **替代品**: 无直接替代 (这是唯一系统讲「角色与生命周期」的)
- **如果可以只读 1 章**: 生命周期总览章 + undercurrents 章。
- **可信度**: high / **Decay risk**: low-medium (框架稳定, 工具示例会旧)

### 📖 3. The Data Warehouse Toolkit

- **Author**: Ralph Kimball & Margy Ross
- **Year**: 2013 (3e); 初版 1996
- **Type**: textbook / 方法论奠基
- **One-liner**: 维度建模的圣经——star schema、事实表/维度表、渐变维 (SCD)、一致性维度，至今 dbt 时代的建模仍站在它肩上。
- **核心论点 (3-5)**:
  - 面向查询/分析建模 (维度) 而非面向事务建模 (规范化) (evidence: [T04-S003])
  - 一致性维度 (conformed dimensions) 是企业级一致性的关键
  - SCD type 1/2/3 处理维度的历史变化 (evidence: [T04-S003])
  - 总线矩阵 (bus matrix) 规划企业数仓
- **读完得到什么**: 能设计经得起业务变化的数仓模型；理解为什么「大宽表 vs 星型」之争各有取舍。
- **难度**: 进阶
- **Endorsement evidence**:
  - `[type: course_syllabus]` 数仓/BI 课程标准教材 (evidence: [T04-S003])
  - `[type: conf_citation]` dbt/分析工程社区讨论建模时默认引用
  - `[type: blog_secondary]` Fundamentals / Densmore 书中引用为建模权威 (evidence: [T04-S002])
- **是否被新版 supersede**: 列存+OBT 时代部分主张被挑战, 但维度概念仍是基础语汇, 不 DROP。
- **如果可以只读 1 章**: SCD 章 + 维度建模技巧导论。
- **可信度**: high / **Decay risk**: low (概念) / medium (技术细节面向 MPP 行存时代)

### 📖 4. Streaming Systems

- **Author**: Tyler Akidau, Slava Chernyak, Reuven Lax (Google → Snowflake 等)
- **Year**: 2018
- **Type**: textbook (Dataflow model 的书本化)
- **One-liner**: 把「批是流的特例」讲透——event-time vs processing-time、watermark、window、trigger，流处理的理论权威。
- **核心论点 (3-5)**:
  - 批/流是同一计算模型的两端，统一在 Dataflow 抽象下 (evidence: [T04-S004], [T04-S012])
  - watermark 回答「这个窗口的数据到齐了吗」 (evidence: [T04-S004])
  - 正确性/延迟/成本三角，由 trigger 策略权衡
  - exactly-once 是工程可达的, 但有成本
- **读完得到什么**: 看懂 Flink / Beam / Spark Structured Streaming 的语义差异；不再把「实时」当玄学。
- **难度**: 高阶
- **Endorsement evidence**:
  - `[type: figure_long]` 作者基于 Dataflow VLDB 论文展开, 流社区奠基 (evidence: [T04-S012])
  - `[type: conf_citation]` Flink/Beam 社区与 Data Council talk 引用基线
  - `[type: blog_secondary]` DDIA 流章节互为补充引用 (evidence: [T04-S001])
- **如果可以只读 1 章**: Streaming 101/102 两章 (即原始博客系列)。
- **可信度**: high / **Decay risk**: low

### 📖 5. Data Mesh

- **Author**: Zhamak Dehghani (前 ThoughtWorks)
- **Year**: 2022
- **Type**: monograph / 架构范式
- **One-liner**: 把单体数据平台拆成域自治的「数据产品」——域所有权 + 数据即产品 + 自助平台 + 联邦计算治理 四原则。
- **核心论点 (4)**:
  - 域所有权 (domain ownership)——数据归生产它的域，而非中央团队 (evidence: [T04-S005], [T04-S010])
  - 数据即产品 (data as a product)——有 owner/SLA/可发现性
  - 自助数据平台——降低域自治的门槛
  - 联邦计算治理——全局标准 + 域自主的平衡 (evidence: [T04-S010])
- **读完得到什么**: 判断「我们该中心化还是去中心化」；识别厂商把 data mesh 当 SKU 卖的营销窄化。
- **难度**: 进阶
- **⚠️ 工程伦理边界**: Zhamak 本人强调**渐进式 + 需组织成熟度**，「一上来全公司铺开」是过度营销反模式 (标 secondary 边界教学)。 (evidence: [T04-S010])
- **Endorsement evidence**:
  - `[type: figure_long]` 4 篇 martinfowler.com 原始长文是书的前身 (evidence: [T04-S010], [T04-S011])
  - `[type: conf_citation]` ThoughtWorks Radar + Data Council 广泛讨论
  - `[type: blog_secondary]` Benn Stancil 等行业评论长期辩论 (evidence: [T04-S034])
- **如果可以只读**: 4 篇 martinfowler 原文足够入门 (evidence: [T04-S010], [T04-S011])。
- **可信度**: high / **Decay risk**: medium (范式仍在辩论中)

### 📖 6-9. 推荐补充书（简条）

- **📖 6. The Data Warehouse Lifecycle Toolkit** (Kimball Group, 2008 2e) — Kimball 方法论的端到端实施手册，配合 Toolkit 看「怎么落地」。难度进阶。Endorsement: book + conf。 (evidence: [T04-S024])
- **📖 7. Building the Data Warehouse** (Bill Inmon, 2005 4e) — 「数据仓库之父」的 CIF 规范化路线，是 Kimball 范式之争的另一极；读它理解「自上而下规范化 vs 自下而上维度」的历史辩论。难度进阶。Endorsement: book + conf (Fundamentals 引为两大数仓范式之一, evidence: [T04-S002])。
- **📖 8. Data Pipelines Pocket Reference** (James Densmore, 2021) — 现代 EL/ELT 管道的最小动手指南，新人补「具体怎么搭」的空白。难度入门。Endorsement: book + blog (evidence: [T04-S022])。
- **📖 9. Data Quality Fundamentals** (Barr Moses, Lior Gavish, Molly Vorwerck, 2022) — data observability / data downtime 的体系化，质量与可观测性维度的 canon。难度进阶。Endorsement: figure (Barr Moses 长文) + book (evidence: [T04-S023], [T04-S031])。

---

## 📄 Seminal Papers / 奠基长文（详条）

### 📄 1. The Log: What every software engineer should know about real-time data's unifying abstraction

- **Author**: Jay Kreps (Kafka 共同创造者, Confluent CEO)
- **Venue + Year**: LinkedIn Engineering Blog, 2013
- **URL**: engineering.linkedin.com (evidence: [T04-S009])
- **One-liner**: 「日志」(append-only ordered log) 是数据集成、复制、流处理、状态重建的统一抽象——Kafka 的思想根。
- **核心 idea**: 一切数据系统都可以围绕一个持久有序日志重构；流是日志的消费，表是日志的物化。 (evidence: [T04-S009])
- **为什么经典**: Kafka 生态 + 现代流架构的思想宪法; CDC / event sourcing / Kappa 都从这里长出。
- **如何读**: 从头读到尾，长但值得 (≈ 一本小册子)。
- **读完得到什么**: 理解为什么 Kafka 不只是消息队列, 而是数据平台的中枢。
- **Endorsement**: figure_long (作者本人长文) + conf (流社区引用基线) + book (DDIA/Streaming Systems 引用)。
- **后续/扩展**: Questioning the Lambda Architecture (Kappa, [T04-S025]); Streaming Systems。
- **可信度**: high / **Decay risk**: low

### 📄 2. Functional Data Engineering — a modern paradigm for batch data processing

- **Author**: Maxime Beauchemin (Airflow + Superset 创始)
- **Venue + Year**: 作者官方 Medium, 2018
- **URL**: maximebeauchemin.medium.com (evidence: [T04-S007])
- **One-liner**: 把函数式编程纪律带入批处理——纯函数式、不可变分区、幂等任务，让 pipeline 可重跑可回填。
- **核心 idea**: task 应是纯函数 (不可变输入分区 → 确定输出分区); 同一分区重跑结果一致, 这是回填安全的前提。 (evidence: [T04-S007])
- **为什么经典**: 「幂等 + 可重跑」成为 Airflow/Dagster 时代 pipeline 设计的第一公民; 是工程伦理 anchor。
- **如何读**: 从头读完, 配合 Rise/Downfall 两篇。
- **读完得到什么**: 知道为什么「非幂等 pipeline 一回填就是灾难」。
- **Endorsement**: figure_long (作者本人) + conf (DataOps/编排社区引用)。
- **后续/扩展**: The Rise [T04-S006] / The Downfall [T04-S008] of the Data Engineer。
- **可信度**: high / **Decay risk**: low

### 📄 3. The Rise / The Downfall of the Data Engineer

- **Author**: Maxime Beauchemin
- **Venue + Year**: 作者官方 Medium, 2017 / 2021
- **URL**: [T04-S006] / [T04-S008]
- **One-liner**: 定义并捍卫「数据工程是软件工程」——版本控制/测试/CI/模块化/code review，不是手工拉数发表。
- **核心 idea**: data engineer 不是 report monkey / 工单执行者; 把 DE 当需求响应工具人 = 组织失败信号 + 技术债工厂。 (evidence: [T04-S006], [T04-S008])
- **为什么经典**: 这两篇 + Functional 三件套是 Maxime 给数据工程「立人格」的奠基长文, 全行业引用。
- **如何读**: 短, 一口气读完三篇。
- **Endorsement**: figure_long (作者) + conf (角色讨论默认引用) + book (Fundamentals 呼应, [T04-S002])。
- **可信度**: high / **Decay risk**: low

### 📄 4. MapReduce: Simplified Data Processing on Large Clusters

- **Author**: Jeffrey Dean & Sanjay Ghemawat (Google)
- **Venue + Year**: OSDI 2004
- **URL**: research.google (evidence: [T04-S013])
- **One-liner**: 大规模批处理的编程模型 (map + reduce)，开启「大数据 = 分布式」时代，Hadoop 的蓝本。
- **核心 idea**: 把容错+并行+数据本地性藏在 map/reduce 抽象后, 让普通工程师写大规模批处理。 (evidence: [T04-S013])
- **为什么经典**: 现代数据工程的历史起点; 即便现在多被 lakehouse/单机引擎取代，理解它才理解「为什么后来要去掉它」。
- **⚠️ 工程伦理边界**: MapReduce/Hadoop 时代过度复杂性是**范式变迁教训**, 不嘲讽早期工程 — 现代默认不是 Spark/Hadoop 集群 (evidence: [T04-S018])。
- **如何读**: 读 abstract + 编程模型 + 容错节即可。
- **Endorsement**: course (CMU/分布式课, [T04-S021]) + book (DDIA 引用, [T04-S001])。
- **后续/扩展**: GFS [T04-S014] / Bigtable [T04-S030] / Dremel [T04-S015]; Spark RDD [T04-S016]。
- **可信度**: high / **Decay risk**: low (历史地位)

### 📄 5. The Dataflow Model

- **Author**: Tyler Akidau et al (Google)
- **Venue + Year**: VLDB 2015
- **URL**: vldb.org (evidence: [T04-S012])
- **One-liner**: 用 What/Where/When/How 四问统一批与流，watermark + trigger 处理无界乱序数据的理论框架。
- **核心 idea**: 无界数据上的正确性由「event-time 窗口 + watermark + trigger + accumulation」四要素决定。 (evidence: [T04-S012])
- **为什么经典**: Apache Beam 的理论基础, Streaming Systems 一书的源头; Flink/Spark 流语义的参照系。
- **如何读**: 配合 Streaming Systems Ch.1-3 读, 论文偏密。
- **Endorsement**: book (Streaming Systems, [T04-S004]) + conf (流社区基线)。
- **可信度**: high / **Decay risk**: low

### 📄 6. Spark: Resilient Distributed Datasets (RDD)

- **Author**: Matei Zaharia et al (UC Berkeley AMPLab)
- **Venue + Year**: NSDI 2012
- **URL**: usenix nsdi (evidence: [T04-S016])
- **One-liner**: 内存中的弹性分布式数据集 + lineage 容错，比 MapReduce 快一个数量级，取代 Hadoop MR 成为分布式计算事实标准。
- **核心 idea**: RDD 用 lineage (血缘) 而非 checkpoint 实现容错, 允许内存迭代计算。 (evidence: [T04-S016])
- **为什么经典**: Spark 是过去十年最重要的分布式计算引擎; PySpark/Spark SQL 仍是大规模转换主力。
- **如何读**: 读 RDD 抽象 + lineage 容错节。
- **Endorsement**: course (数据库/分布式课) + book (DDIA/Fundamentals 引用, [T04-S001])。
- **后续/扩展**: Lakehouse [T04-S017] (同一团队); Delta Lake [T04-S028]。
- **可信度**: high / **Decay risk**: low

### 📄 7. Lakehouse: A New Generation of Open Platforms that Unify Data Warehousing and Advanced Analytics

- **Author**: Michael Armbrust, Ali Ghodsi, Reynold Xin, Matei Zaharia (Databricks)
- **Venue + Year**: CIDR 2021
- **URL**: cidrdb.org (evidence: [T04-S017])
- **One-liner**: 在数据湖 (对象存储 + 开放格式) 上加事务表层 + 元数据层 = 既有湖的开放低成本, 又有仓的 ACID/性能。
- **核心 idea**: 用 Delta/Iceberg 这样的表格式给湖加 ACID/版本/schema 治理, 消除「湖 + 仓两套系统」。 (evidence: [T04-S017], [T04-S029])
- **为什么经典**: 定义了过去几年最主流的数据架构范式; Iceberg/Delta/Hudi 都是它的实现。
- **如何读**: 通读, 论文不长且工程导向。
- **Endorsement**: conf (CIDR + Data Council) + book (Fundamentals 架构章, [T04-S002])。
- **后续/扩展**: Iceberg [T04-S027] / Delta [T04-S028] 官方文档。
- **可信度**: high / **Decay risk**: low-medium

### 📄 8. Big Data is Dead

- **Author**: Jordan Tigani (MotherDuck CEO, 前 BigQuery 创始工程师)
- **Venue + Year**: MotherDuck Blog, 2023
- **URL**: motherduck.com (evidence: [T04-S018])
- **One-liner**: 多数公司的数据塞得进单机，「大数据时代」的分布式默认是反模式——DuckDB/Polars/单数仓优先。
- **核心 idea**: 数据量中位数远小于业界宣传; 查询热数据更小; 默认上 Spark 集群多是 resume-driven 而非真需求。 (evidence: [T04-S018])
- **为什么经典**: 标志了从「大数据=越大越分布式越好」到「先问数据真有那么大吗」的范式翻转; 工程伦理 anchor。
- **⚠️ 工程伦理边界**: 「为简历/显得专业上 Spark」是反模式; 多数公司瓶颈是建模+质量+成本, 不是缺分布式 (evidence: [T04-S018])。
- **如何读**: 短文一篇, 必读。
- **Endorsement**: figure_long (作者, BigQuery 创始工程师权威) + conf (Data Council 广泛引用)。
- **可信度**: high / **Decay risk**: low

### 📄 9-12. 推荐补充论文/长文（简条）

- **📄 9. GFS / Bigtable / Dremel** (Google, 2003/2006/2010) — 分布式文件系统 / 宽列存储 / 列存交互式查询 (BigQuery 引擎) 三篇工程奠基；理解云数仓与列存的根 (evidence: [T04-S014], [T04-S030], [T04-S015])。Endorsement: course + book。
- **📄 10. Data Mesh 4 篇原文** (Zhamak, martinfowler.com, 2019-2020) — 书的前身, 「How to move beyond a monolithic data lake」+ 4 原则文; 比书更精炼 (evidence: [T04-S011], [T04-S010])。Endorsement: figure_long + conf。
- **📄 11. Questioning the Lambda Architecture** (Jay Kreps, O'Reilly Radar, 2014) — Kappa 架构提出文, 用单流引擎替双链路, 反对维护两套代码 (evidence: [T04-S025])。Endorsement: figure + conf。
- **📄 12. How to beat the CAP theorem (Lambda Architecture)** (Nathan Marz, 2011) — Lambda 架构 (批层+速度层+服务层) 原始文；历史性，多被 Kappa/统一引擎挑战，但术语仍通用 (evidence: [T04-S026])。Endorsement: book + conf。

---

## 🎓 Courses（详条）

### 🎓 1. dbt Learn / dbt Fundamentals

- **Lecturer/Institution**: dbt Labs (Tristan Handy 团队)
- **Format**: rolling 互动课程 + 官方文档 (evidence: [T04-S019])
- **Year + 最近更新**: rolling, last_updated 2026-05 (随 dbt 版本持续更新; 近期重点 MetricFlow 语义层 + dbt Mesh + Fusion 引擎)
- **One-liner**: analytics engineering 事实标准的官方上手——SQL-first 转换 + 测试 + 文档 + 血缘 + 增量模型。
- **完整路径 vs 关键章节**: 完整 = dbt Fundamentals → Advanced materializations → Analyses/Metrics; 只看 Fundamentals 即可建第一个测试过的 dbt 项目。
- **难度/先修**: 入门-进阶; 先修 = SQL + 基本数仓概念。
- **Endorsement**: figure (Tristan Handy 长期布道, [T04-S035]) + conf (Coalesce 大会) + 行业默认技能。
- **Last_updated**: 2026-05 (rolling)
- **可信度**: high / **Decay risk**: medium (工具课, 跟版本走)

### 🎓 2. Data Engineering Zoomcamp

- **Lecturer/Institution**: DataTalks.Club (Alexey Grigorev 等)
- **Format**: rolling 免费实操 (GitHub repo + 视频 + homework), cohort 制 (evidence: [T04-S020])
- **Year + 最近更新**: rolling, last_updated 2025-01 cohort (covers Docker/Terraform → Kafka → Spark → dbt → BigQuery/Postgres → 编排 Kestra/Airflow)
- **One-liner**: 端到端自己搭一条现代数据管道的最佳免费实操课, 转型者入门首选。
- **完整路径 vs 关键章节**: 完整 9 周端到端; 只想补「批+流」的看 Spark + Kafka 两 module。
- **难度/先修**: 入门-进阶; 先修 = Python + SQL + 基本命令行。
- **Endorsement**: course_syllabus (社区标准入门路径) + 大量从业者背书 + GitHub 高 star (evidence: [T04-S020])。
- **Last_updated**: 2025-01
- **可信度**: high / **Decay risk**: medium (年度刷新, 工具栈跟进)

### 🎓 3. CMU 15-445/645 Intro to Database Systems

- **Lecturer/Institution**: Andy Pavlo / Carnegie Mellon University
- **Format**: 公开讲座视频 + project lab (.edu) (evidence: [T04-S021])
- **Year + 最近更新**: last_updated 2024 fall (每年开, 视频公开)
- **One-liner**: 数据库内核 (存储/索引/查询执行/事务/MVCC) 的一手理解, 让你看懂 DuckDB/Snowflake/列存引擎里在发生什么。
- **完整路径 vs 关键章节**: 完整一学期; 数据工程师重点看 存储模型 (行存 vs 列存) + 查询执行 + 谓词下推 几讲。
- **难度/先修**: 进阶; 先修 = C++/系统基础 (project) 或纯听课。
- **Endorsement**: course_syllabus (.edu 一手) + 广泛被推荐为「想懂引擎就看这门」 + conf。
- **Last_updated**: 2024
- **可信度**: high / **Decay risk**: low (内核原理稳定, 年更内容)

### 🎓 4. (推荐) DDIA 作为自学路径

- DDIA ([T04-S001]) 本身常被当成「读 + 讨论」式自学课程 (有社区读书会路线图)。Last_updated: 2017 (2e 在写)。难度进阶。作为课程补 CMU 15-445 之上的「分布式」维度。

---

## 💡 Core Concepts（详条选关键 8 个，其余见总览表）

### 💡 1. Idempotency / 幂等

- **Tier**: tier-1
- **One-liner**: 同一任务对同一输入分区重跑，结果完全一致 (无重复/无错乱)。
- **来源**: `[primary]` Maxime Beauchemin "Functional Data Engineering" (2018, [T04-S007]); `[significant]` Airflow/Dagster 调度社区。
- **关联概念**: backfill / 不可变分区 / 可重跑 / pure function。
- **当前理解 vs 原始**: 从函数式编程概念被 Maxime 引入批处理纪律, 现已是 pipeline 设计公理。
- **为什么进入 canon**: 非幂等 pipeline 一旦回填或重试就产生脏数据, 是数据平台最隐蔽灾难源。
- **常见误用**: 把「跑成功了」当幂等; 真正幂等要求重跑覆盖而非追加。
- **Endorsement**: [T04-S007], [T04-S033], [T04-S002]

### 💡 2. ELT vs ETL

- **Tier**: tier-1
- **One-liner**: 把转换 (T) 推到数仓内部做 (Extract-Load-Transform), 而非加载前用独立 ETL 引擎。
- **来源**: `[primary]` dbt 运动 / Fundamentals 框架 ([T04-S035], [T04-S002]); `[significant]` 云数仓 (Snowflake/BigQuery) 算力廉价化。
- **关联概念**: dbt / 现代数据栈 / 存算分离 / 数仓内转换。
- **当前理解 vs 原始**: 云数仓让「先 load 再用 SQL transform」比传统 ETL 更经济, 催生 analytics engineering 角色。
- **为什么进入 canon**: 现代数据栈的核心范式转移; dbt 整个生态建立在此。
- **常见误用**: 以为 ELT 就免去建模; T 仍要建模+测试, 只是位置变了。
- **Endorsement**: [T04-S035], [T04-S019], [T04-S002]

### 💡 3. Open Table Format / 开放表格式 (Iceberg / Delta / Hudi)

- **Tier**: tier-1
- **One-liner**: 在对象存储的 Parquet 文件之上加一层表元数据，使湖上数据具备 ACID/time travel/schema evolution/隐藏分区。
- **来源**: `[primary]` Lakehouse CIDR 2021 ([T04-S017]); `[significant]` Iceberg ([T04-S027]) / Delta ([T04-S028]) 官方。
- **关联概念**: lakehouse / ACID on object store / time travel / 小文件 compaction。
- **⚠️ 工程伦理边界**: Iceberg vs Delta vs Hudi 各有取舍 (Iceberg 中立生态+隐藏分区 / Delta Databricks 强 / Hudi 强 upsert+CDC), 选型看现有生态+读写模式, **不站队营销**; 趋势是引擎多格式兼容, Iceberg 中立性使其成事实交换格式。
- **常见误用**: 把「开放格式」当「随便哪个引擎都最优读写」; 兼容性与性能仍有引擎差异。
- **Endorsement**: [T04-S017], [T04-S027], [T04-S028]

### 💡 4. Watermark / Windowing

- **Tier**: tier-1
- **One-liner**: 流处理中 watermark 估计「event-time 进度」以界定窗口何时算「数据到齐」可触发。
- **来源**: `[primary]` Dataflow Model (VLDB 2015, [T04-S012]); `[significant]` Streaming Systems ([T04-S004])。
- **关联概念**: event-time vs processing-time / trigger / 乱序 / exactly-once。
- **常见误用**: 以为窗口靠 processing-time 切; 乱序数据下必须用 event-time + watermark。
- **Endorsement**: [T04-S012], [T04-S004]

### 💡 5. Data Contract / 数据契约

- **Tier**: tier-1
- **One-liner**: producer 与 consumer 之间对 schema/语义/SLA 的显式约定，把隐式耦合显性化。
- **来源**: `[primary]` Chad Sanderson "Rise of Data Contracts" ([T04-S032]); `[significant]` schema registry / Avro 演进实践。
- **关联概念**: schema evolution / shift-left quality / schema is an API。
- **⚠️ 工程伦理 anchor**: schema 是 API, 上游随意删字段静默打爆下游所有 pipeline; 数据契约 + 向后兼容演进是基线 (evidence: [T04-S032])。
- **常见误用**: 把数据契约当文档而非可强制的校验门禁。
- **Endorsement**: [T04-S032], [T04-S001]

### 💡 6. Data Observability / Data Downtime

- **Tier**: tier-1
- **One-liner**: 用新鲜度/量/schema/分布/血缘五维监控数据健康，"data downtime" = 数据错误/缺失/不可信的时间成本。
- **来源**: `[primary]` Barr Moses / Monte Carlo ([T04-S031]); `[significant]` Data Quality Fundamentals ([T04-S023])。
- **关联概念**: 数据质量测试 / dbt tests / Great Expectations / 列级血缘。
- **常见误用**: 把可观测性当「加监控面板」; 核心是异常自动检测 + 影响面血缘。
- **Endorsement**: [T04-S031], [T04-S023]

### 💡 7. Decoupled Storage & Compute / 存算分离

- **Tier**: tier-1
- **One-liner**: 计算与存储独立伸缩 (Snowflake/BigQuery/lakehouse)，按需启停计算而存储常驻廉价对象存储。
- **来源**: `[primary]` Lakehouse ([T04-S017]) / Dremel ([T04-S015]); `[significant]` Snowflake 架构 / DDIA MPP 章。
- **关联概念**: MPP / 弹性 / 成本 FinOps / 对象存储。
- **常见误用**: 以为存算分离自动省钱; 不优化分区/扫描量仍会账单爆炸。
- **Endorsement**: [T04-S017], [T04-S001]

### 💡 8. Medallion 架构 (Bronze / Silver / Gold)

- **Tier**: tier-1
- **One-liner**: 数据分层提纯——bronze 原始落地、silver 清洗规范、gold 业务聚合，逐层增加质量与可用性。
- **来源**: `[primary]` Databricks lakehouse 实践 ([T04-S029]); `[significant]` dbt staging/intermediate/marts 分层社区惯例。
- **关联概念**: ELT / dbt 分层 / OBT / 维度建模。
- **常见误用**: 把分层当 SKU 复制; 实际是「每层有明确质量契约」而非机械三段。
- **Endorsement**: [T04-S029], [T04-S019]

> 其余 19 个概念 (Partitioning / CDC / 维度建模-SCD / 规范化 / Lakehouse / ACID on object store / Time travel / Schema evolution / Exactly-once / Lambda-Kappa / Columnar storage / Predicate pushdown / MPP / Backfill / Semantic layer / Data mesh / OBT / Small files / DataOps) 见上方「Core Concepts 总览表」, 每个均有来源 + evidence 锚点。

---

## Phase 2 提炼提示

### 反复出现 ≥ 3 个 canon 都讨论的核心 idea（候选行业心智模型）

- **「幂等 + 可重跑 + 不可变分区」是 pipeline 第一公民** 出现于: Functional Data Engineering [T04-S007] / Fundamentals [T04-S002] / Airflow-Dagster 实践 → **强候选心智模型** (工程伦理 anchor)。
- **「批与流是同一计算模型的两端」(统一抽象)** 出现于: The Log [T04-S009] / Dataflow [T04-S012] / Streaming Systems [T04-S004] / DDIA [T04-S001] → **强候选心智模型**。
- **「先问数据真的大到需要分布式吗」(反过早分布式)** 出现于: Big Data is Dead [T04-S018] / DuckDB 复兴 / Fundamentals「足够好架构」[T04-S002] → **强候选心智模型** (工程伦理 anchor)。
- **「schema 是 API, 数据质量要 shift-left」** 出现于: Data Contracts [T04-S032] / Data Quality Fundamentals [T04-S023] / DDIA schema 演进 [T04-S001] → **候选心智模型** (工程伦理 anchor)。
- **「数据工程是软件工程, 不是 report monkey」** 出现于: Rise/Downfall [T04-S006][T04-S008] / Fundamentals undercurrents [T04-S002] / dbt analytics engineering [T04-S035] → **候选心智模型** (角色伦理 anchor)。
- **「湖+仓合一 (lakehouse) + 存算分离 + 开放表格式」** 出现于: Lakehouse CIDR [T04-S017] / Iceberg [T04-S027] / Delta [T04-S028] → **候选架构心智模型**。
- **「数据建模面向消费 (维度/OBT) 而非面向事务」** 出现于: Kimball [T04-S003] / Inmon 对照 / dbt 分层 [T04-S019] → **候选心智模型**。

### 智识谱系种子

- **分布式数据系统第一性原理派** 奠基: DDIA (Kleppmann, [T04-S001]) + Google 三论文 (MapReduce/GFS/Bigtable, [T04-S013][T04-S014][T04-S030])。当前代表: 与 Track 01 figure **Martin Kleppmann** 关联。
- **日志/流统一抽象派** 奠基: Jay Kreps "The Log" [T04-S009] + Akidau Dataflow [T04-S012]。当前代表: Track 01 **Jay Kreps** (Kafka/Confluent) + **Tyler Akidau** (Streaming Systems)。
- **维度建模派 vs 规范化 CIF 派** (历史范式之争): Kimball ([T04-S003], 自下而上维度) vs Inmon (自上而下规范化企业数仓)。当前代表: Track 01 **Ralph Kimball** / **Bill Inmon**。
- **analytics engineering / 现代数据栈派** 奠基: dbt (Tristan Handy, [T04-S035][T04-S019]) + ELT 范式。当前代表: Track 01 **Tristan Handy** / **Benn Stancil** (批判性评论)。
- **lakehouse / 开放表格式派** 奠基: Lakehouse CIDR ([T04-S017]) + Spark RDD ([T04-S016])。当前代表: Track 01 **Matei Zaharia** (Spark/Delta) / **Ryan Blue** (Iceberg) / **Vinoth Chandar** (Hudi)。
- **去中心化数据架构派** 奠基: Data Mesh (Zhamak, [T04-S010][T04-S005])。当前代表: Track 01 **Zhamak Dehghani**。
- **反过度分布式 / 单机复兴派** 奠基: Big Data is Dead (Tigani, [T04-S018]) + DuckDB。当前代表: Track 01 **Jordan Tigani** / **Hannes Mühleisen**。
- **数据质量/可观测性派** 奠基: Data Downtime (Barr Moses, [T04-S031]) + Data Contracts (Chad Sanderson, [T04-S032])。当前代表: Track 01 **Barr Moses** / **Chad Sanderson**。
- **数据工程纪律/工程化派** 奠基: Maxime Beauchemin 三件套 ([T04-S006][T04-S007][T04-S008])。当前代表: Track 01 **Maxime Beauchemin**。
- **主要分歧 (still-debated within the canon)**:
  - 维度建模 (Kimball star) vs OBT 大宽表 vs Data Vault — 列存时代谁更优 (悬而未决)
  - Lambda vs Kappa vs 统一引擎 — 双链路 vs 单流 (Kreps Kappa [T04-S025] vs Marz Lambda [T04-S026])
  - 中心化 (数据中台) vs 去中心化 (data mesh) 数据所有权 — 组织成熟度依赖
  - Iceberg vs Delta vs Hudi 表格式之争 — 不站队, 趋势多格式兼容
  - 实时 vs 批 — 「越实时越好」是误区, 多数分析分钟/小时级批足够

### 核心概念 → 候选 playbook

- **幂等** 暗示: 「如果 pipeline 要支持回填/重试, 则任务必须对分区幂等 (覆盖而非追加, 用 merge/upsert with primary key)」。 案例: 非幂等 append 任务回填 → 数据翻倍。
- **反过早分布式** 暗示: 「如果数据 < 单机内存 (中位数公司单表几十 GB 内), 则默认 DuckDB/Polars/单数仓, 上 Spark 前先量化数据规模」。 案例: 几个 G 数据上 Spark 集群 = resume-driven。
- **ELT** 暗示: 「如果有云数仓, 则 Extract-Load 原始数据后用 dbt 在仓内 transform, 而非加载前 ETL」。
- **数据契约** 暗示: 「如果下游依赖上游表 schema, 则在生产端加契约校验 (schema is API), 而非数仓末端救火」。
- **成本** 暗示: 「如果云数仓账单异常, 则查 SELECT * / 全量重算 / 小文件 / 缺分区裁剪四大元凶」。
- **批 vs 流** 暗示: 「如果不是亚秒级 (风控/推荐/监控) 需求, 则批足够, 不为实时上 Flink 双倍复杂度」。

### 冷僻 / 信号薄弱

- 必读书 ≥ 9 (远超 floor 3) ✅
- 论文/长文 ≥ 12 (远超 floor 5) ✅
- 课程 4 门 (超 floor 2) ✅
- 核心概念 27 (超 floor 15) ✅
- Endorsement ≥ 3 处的项 > 50% ✅ (绝大多数 book/paper 有 figure_long + conf + book/course 三类)
- **诚实边界 flag**: ① **zh-CN canon 薄** — DE canon ~90% 英文, 中文读者消费翻译版 + Apache 文档 + 极客时间; 中国一手在工具层 (Flink/DolphinScheduler/Doris/Paimon) 非著作层。② **surrogate 比例较高** — 因 source_verifier 不识 .io/.com/.org/.apache.org/medium.com 作者域名, 大量出版社/作者/项目一手标 surrogate_primary (含 "vendor docs"), 而非内容不可信; 真正自动 verified_primary 的是 arxiv/.edu/research.google/usenix/cidrdb/linkedin-eng/github-repo/docs.getdbt.com。
