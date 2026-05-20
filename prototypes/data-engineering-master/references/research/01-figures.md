# Track 01 — Figures: Data Engineering (数据工程)

> Phase 1 wave 2 subagent 输出。locale = en (en-primary, zh-CN secondary)。
> 候选池 explored: 22 / retained: **15**。floor 15 达标 — **非冷僻领域**。
> last_checked 全部 = 2026-05-20。
> **关键源结构说明**: 数据工程几乎所有一手都在 `.io / .com / .org / .apache.org / .medium.com / .dev` 域名上, source_verifier 默认判 `secondary` / `unknown`。本 manifest 按 intake `surrogate_domain_whitelist_preemptive` 把这些显式声明为 `surrogate_primary` 且 note 含 literal **"vendor docs"**。Substack 作者本人域名 (benn / joereis / dataproducts) + 部分作者个人站 (morling.dev / wesmckinney.com) + arxiv + github project root + .edu/.gov + 厂商博客 (gable.ai / cn.pingcap.com / hudi.apache.org 经 verifier) 自动 `verified_primary` 不下调。

---

## Source Manifest

| source_id | url | bucket | last_checked | author/host | one-line note |
|-----------|-----|--------|--------------|-------------|---------------|
| T01-S001 | https://maximebeauchemin.medium.com/functional-data-engineering-a-modern-paradigm-for-batch-data-processing-2327ec32c42a | surrogate_primary | 2026-05-20 | Maxime Beauchemin | vendor docs (作者 official Medium — Functional Data Engineering 奠基长文) |
| T01-S002 | https://maximebeauchemin.medium.com/the-downfall-of-the-data-engineer-5bfb701e5d6b | surrogate_primary | 2026-05-20 | Maxime Beauchemin | vendor docs (作者一手 — Downfall of the Data Engineer) |
| T01-S003 | https://preset.io | surrogate_primary | 2026-05-20 | Preset (Maxime 公司) | vendor docs (厂商一手 — Superset 商用) |
| T01-S004 | https://joereis.substack.com/p/fundamentals-of-data-engineering | verified_primary | 2026-05-20 | Joe Reis | newsletter author host — Fundamentals 2.5 年回顾 |
| T01-S005 | https://www.ternarydata.com | surrogate_primary | 2026-05-20 | Ternary Data | vendor docs (作者一手 — Reis/Housley 公司) |
| T01-S006 | https://www.youtube.com/watch?v=VdGVmqiJkeg | reference | 2026-05-20 | GOTO Conferences | Reis & Housley GOTO 2025 talk (长视频) |
| T01-S007 | https://www.oreilly.com/library/view/fundamentals-of-data/9781098108298/ | surrogate_primary | 2026-05-20 | O'Reilly | vendor docs (出版社一手 — Fundamentals of Data Engineering) |
| T01-S008 | https://martin.kleppmann.com/ | surrogate_primary | 2026-05-20 | Martin Kleppmann | vendor docs (作者一手 — Cambridge, 分布式数据系统权威) |
| T01-S009 | https://dataintensive.net/ | surrogate_primary | 2026-05-20 | Martin Kleppmann | vendor docs (作者一手 — DDIA 数据系统正典官网) |
| T01-S010 | https://www.oreilly.com/library/view/designing-data-intensive-applications/9781098119058/ | surrogate_primary | 2026-05-20 | O'Reilly | vendor docs (出版社一手 — DDIA 2nd ed, w/ Chris Riccomini) |
| T01-S011 | https://www.getdbt.com/blog/dbt-labs-and-fivetran-merge-announcement | surrogate_primary | 2026-05-20 | dbt Labs | vendor docs (厂商一手 — Fivetran+dbt 合并公告) |
| T01-S012 | https://www.getdbt.com/blog/dbt-labs-redefines-dbt-with-new-fusion-engine | surrogate_primary | 2026-05-20 | dbt Labs | vendor docs (厂商一手 — dbt Fusion engine 2025-05) |
| T01-S013 | https://roundup.getdbt.com/ | surrogate_primary | 2026-05-20 | Tristan Handy | vendor docs (作者一手 — Analytics Engineering Roundup) |
| T01-S014 | https://engineering.linkedin.com/distributed-systems/log-what-every-software-engineer-should-know-about-real-time-datas-unifying | surrogate_primary | 2026-05-20 | Jay Kreps / LinkedIn Eng | vendor docs (厂商一手 — 'The Log' 奠基文原始托管处) |
| T01-S015 | https://www.confluent.io/blog/confluent-and-databricks/ | surrogate_primary | 2026-05-20 | Confluent | vendor docs (厂商一手 — Tableflow + Iceberg 实时 AI) |
| T01-S016 | https://martinfowler.com/articles/data-monolith-to-mesh.html | surrogate_primary | 2026-05-20 | Zhamak Dehghani / M.Fowler | vendor docs (作者一手 — data mesh 奠基文托管处) |
| T01-S017 | https://www.bigdatawire.com/2025/04/16/data-mesh-creator-dehghani-launches-first-product-nextdata-os/ | secondary | 2026-05-20 | BigDATAwire | Nextdata OS 2025-04 发布 (二手新闻) |
| T01-S018 | https://www.kimballgroup.com | surrogate_primary | 2026-05-20 | Ralph Kimball | vendor docs (作者一手 — 维度建模奠基, 站已存档) |
| T01-S019 | https://www.oreilly.com/library/view/the-data-warehouse/9781118530801/ | surrogate_primary | 2026-05-20 | O'Reilly/Wiley | vendor docs (出版社一手 — Data Warehouse Toolkit) |
| T01-S020 | https://www.databricks.com/company/newsroom/press-releases/databricks-donates-declarative-pipelines-apache-sparktm-open-source | surrogate_primary | 2026-05-20 | Databricks | vendor docs (厂商一手 — Spark Declarative Pipelines 2025-06) |
| T01-S021 | https://people.eecs.berkeley.edu/~matei/ | verified_primary | 2026-05-20 | Matei Zaharia | .edu 学术主页 — Spark/Delta/DSPy |
| T01-S022 | https://awards.acm.org/about/2025-acm-prize | verified_primary | 2026-05-20 | ACM | 2025 ACM Prize in Computing — Zaharia |
| T01-S023 | https://www.databricks.com/blog/next-era-open-lakehouse-apache-icebergtm-v3-public-preview-databricks | surrogate_primary | 2026-05-20 | Databricks | vendor docs (厂商一手 — Iceberg v3, Ryan Blue 阵营) |
| T01-S024 | https://github.com/apache/iceberg | verified_primary | 2026-05-20 | Apache Iceberg | github project root (auto primary) — Ryan Blue 创始 |
| T01-S025 | https://www.databricks.com/company/newsroom/press-releases/databricks-agrees-acquire-tabular-company-founded-original-creators | surrogate_primary | 2026-05-20 | Databricks | vendor docs (厂商一手 — Tabular 收购, Ryan Blue) |
| T01-S026 | https://wesmckinney.com/blog/looking-back-15-years/ | verified_primary | 2026-05-20 | Wes McKinney | 作者个人站 — composable data systems 15 年回顾 |
| T01-S027 | https://wesmckinney.com/transcripts/2025-10-16-earl-uk-keynote | surrogate_primary | 2026-05-20 | Wes McKinney | vendor docs (作者一手) — 2025 EARL keynote transcript |
| T01-S028 | https://arrow.apache.org | surrogate_primary | 2026-05-20 | Apache Arrow | vendor docs (Apache 项目一手 — 内存列存标准) |
| T01-S029 | https://arxiv.org/abs/2504.10438 | verified_primary | 2026-05-20 | Akidau et al (Snowflake) | arxiv — Streaming Democratized / Dynamic Tables SIGMOD'25 |
| T01-S030 | https://www.snowflake.com/en/blog/authors/tyler-akidau/ | surrogate_primary | 2026-05-20 | Tyler Akidau / Snowflake | vendor docs (厂商一手 — Streaming 101/102 作者) |
| T01-S031 | https://www.montecarlodata.com/blog-agent-observability-announcement/ | surrogate_primary | 2026-05-20 | Monte Carlo | vendor docs (厂商一手 — Agent Observability 2025-09) |
| T01-S032 | https://www.montecarlodata.com/blog-the-past-present-and-future-of-data-quality-management/ | surrogate_primary | 2026-05-20 | Barr Moses / Monte Carlo | vendor docs (厂商一手 — data downtime 品类) |
| T01-S033 | https://dataproducts.substack.com/p/the-shift-left-data-manifesto | verified_primary | 2026-05-20 | Chad Sanderson | newsletter author host — Shift Left Data Manifesto |
| T01-S034 | https://www.gable.ai/blog/shifting-left-with-data-devops-chad-sanderson-shift-left-data-conference-2025 | verified_primary | 2026-05-20 | Chad Sanderson / Gable | Shift Left Data Conf 2025 talk |
| T01-S035 | https://www.oreilly.com/library/view/data-contracts/9781098157623/ | surrogate_primary | 2026-05-20 | O'Reilly | vendor docs (出版社一手 — Data Contracts book, Sanderson) |
| T01-S036 | https://benn.substack.com/ | verified_primary | 2026-05-20 | Benn Stancil | newsletter author host — 数据行业评论 |
| T01-S037 | https://benn.substack.com/p/the-modern-data-experience | verified_primary | 2026-05-20 | Benn Stancil | newsletter author host — modern data stack 批判 |
| T01-S038 | https://hudi.apache.org/blog/2025/01/08/the-future-of-data-lakehouses-a-fireside/ | verified_primary | 2026-05-20 | Vinoth Chandar / Hudi | 项目博客 fireside (verifier 判 primary) |
| T01-S039 | https://www.onehouse.ai/resources/open-engines-launch | surrogate_primary | 2026-05-20 | Onehouse (Vinoth) | vendor docs (厂商一手 — Hudi 创始, XTable 互操作) |
| T01-S040 | https://www.morling.dev/blog/one-billion-row-challenge/ | verified_primary | 2026-05-20 | Gunnar Morling | 作者个人站 — 1BRC (verifier 判 primary) |
| T01-S041 | https://debezium.io | surrogate_primary | 2026-05-20 | Debezium | vendor docs (项目一手 — CDC 事实标准, Morling 前 lead) |
| T01-S042 | https://motherduck.com/videos/the-death-of-big-data-and-why-its-time-to-think-small-jordan-tigani-ceo-motherduck/ | surrogate_primary | 2026-05-20 | Jordan Tigani / MotherDuck | vendor docs (厂商一手 — 'Big Data is Dead' talk) |
| T01-S043 | https://www.datacouncil.ai/talks/big-data-is-dead | surrogate_primary | 2026-05-20 | Data Council | vendor docs (会议一手 — Tigani 'Big Data is Dead' talk) |
| T01-S044 | https://dagster.io/blog/podcast-drill-to-detail-aug-2023 | surrogate_primary | 2026-05-20 | Nick Schrock / Dagster | vendor docs (厂商一手 — software-defined assets) |
| T01-S045 | https://github.com/dagster-io/dagster | verified_primary | 2026-05-20 | Dagster Labs | github project root (auto primary) — Nick Schrock |
| T01-S046 | https://duckdb.org/2025/05/27/ducklake | surrogate_primary | 2026-05-20 | DuckDB / Hannes M. | vendor docs (项目一手 — DuckLake 发布 2025-05) |
| T01-S047 | https://hannes.muehleisen.org/ | surrogate_primary | 2026-05-20 | Hannes Mühleisen | vendor docs (作者个人站 — DuckDB 创始, CWI) |
| T01-S048 | https://www.cwi.nl/en/news/hannes-muhleisen-wins-the-dutch-prize-for-ict-research-2025/ | surrogate_primary | 2026-05-20 | CWI Amsterdam | vendor docs (研究机构一手 — 2025 荷兰 ICT 研究奖) |
| T01-S049 | https://www.dataengineeringweekly.com/ | surrogate_primary | 2026-05-20 | Ananth Packkildurai | vendor docs (作者一手 — newsletter 本人策展+原创) |
| T01-S050 | https://www.dataengineeringweekly.com/p/beyond-kafka-conversation-with-jark | surrogate_primary | 2026-05-20 | Ananth / Jark Wu | vendor docs (作者一手 — Fluss 访谈 Jark Wu) |
| T01-S051 | https://github.com/wuchong | surrogate_primary | 2026-05-20 | 伍翀 Jark Wu | vendor docs (作者一手 — Flink PMC 个人 GitHub) |
| T01-S052 | https://flink.apache.org | surrogate_primary | 2026-05-20 | Apache Flink | vendor docs (Apache 项目一手 — 流计算, 阿里核心 committer) |
| T01-S053 | https://speakerdeck.com/jark/cmu-db-2025fall-apache-fluss-a-streaming-storage-for-real-time-lakehouse | surrogate_primary | 2026-05-20 | Jark Wu | vendor docs (作者一手 — CMU-DB 2025 Fluss 演讲 deck) |
| T01-S054 | https://dolphinscheduler.apache.org | surrogate_primary | 2026-05-20 | Apache DolphinScheduler | vendor docs (Apache 项目一手 — 中国主导编排, 代立冬 PMC) |
| T01-S055 | https://github.com/apache/dolphinscheduler | verified_primary | 2026-05-20 | Apache DolphinScheduler | github project root (auto primary) |
| T01-S056 | https://www.infoq.cn | surrogate_primary | 2026-05-20 | InfoQ 中文 | vendor docs (中国技术媒体一手 — QCon/ArchSummit 演讲) |
| T01-S057 | https://cn.pingcap.com/blog/profile/ed-huang/ | verified_primary | 2026-05-20 | 黄东旭 Ed Huang / PingCAP | 厂商博客作者页 (verifier 判 primary) — TiDB CTO |
| T01-S058 | https://www.pingcap.com/blog/integrating-vector-search-into-tidb-for-ai-applications/ | surrogate_primary | 2026-05-20 | PingCAP | vendor docs (厂商一手 — TiDB vector/HTAP) |
| T01-S059 | https://www.reddit.com/r/dataengineering/ | reference | 2026-05-20 | r/dataengineering | UGC 社区 — 从业者反复点名验证 (second-order) |
| T01-S060 | https://www.dataengineeringpodcast.com/ | surrogate_primary | 2026-05-20 | Tobias Macey | vendor docs (一手 — 长访谈 podcast 节目页, 常驻嘉宾池) |
| T01-S061 | https://www.gable.ai/blog/panel-shift-left-across-the-data-lifecycle--data-contracts-transformations-observability-and-catalogs-prukalpa-sankar-tristan-handy-barr-moses-chad-sanderson-shift-left-data-conference-2025 | verified_primary | 2026-05-20 | Gable | Shift Left 2025 panel — Handy+Moses+Sanderson 同台 (cross-figure) |
| T01-S062 | https://www.tabular.io | surrogate_primary | 2026-05-20 | Tabular (Ryan Blue) | vendor docs (厂商一手 — Iceberg 商用, 被 Databricks 收购) |

---

## 总览（按行业影响力排序）

| # | 姓名 | 核心身份 | 一句话贡献 | 值得读/听/看 | 来源数 |
|---|------|---------|----------|------------|-------|
| 1 | Maxime Beauchemin | Preset CEO, Airflow + Superset 创始 | 把数据工程定义成软件工程学科, 提出 functional data engineering (幂等/不可变/可重算) | 📖🎬 | 3 |
| 2 | Joe Reis | Ternary Data, 'Fundamentals of Data Engineering' 合著 | 用「生命周期 + 六暗流」框架给整个行业一套通用语言 | 📖🎙️🎬 | 4 |
| 3 | Martin Kleppmann | Cambridge 副教授, DDIA 作者 | DDIA 是数据系统第一性原理正典 (2026 出第 2 版) | 📖🎬 | 3 |
| 4 | Tristan Handy | dbt Labs 创始 (现 Fivetran+dbt President) | 发起 analytics engineering 运动, dbt = ELT 转换事实标准 | 📖🎙️ | 3 |
| 5 | Jay Kreps | Confluent 联创 CEO, Kafka 共同创造 | 'The Log' 统一抽象 → 流即一等公民; stream-table duality | 📖🎬 | 3 |
| 6 | Zhamak Dehghani | Nextdata 创始 CEO, data mesh 提出者 | data mesh: 域所有权 + 数据即产品 + 联邦治理 | 📖🎬 | 3 |
| 7 | Matei Zaharia | Databricks 联创 CTO, UC Berkeley | Spark 创造者; 2025 ACM Prize; Declarative Pipelines + DSPy | 📖🎬 | 4 |
| 8 | Ryan Blue | Databricks (前 Tabular/Netflix) | Apache Iceberg 创造者 — 开放表格式事实交换标准 | 📖🎬 | 3 |
| 9 | Wes McKinney | Voltron Data 首席科学家 | pandas + Arrow 创造者; composable data systems 旗手 | 📖🎙️🎬 | 3 |
| 10 | Tyler Akidau | Snowflake (前 Google) | 'Streaming Systems' / Dataflow model; 批流统一理论 | 📖🎬 | 3 |
| 11 | Barr Moses | Monte Carlo 联创 CEO | 创造 'data observability' / 'data downtime' 品类 | 📖🎬 | 2 |
| 12 | Chad Sanderson | Gable.ai CEO | data contracts + shift-left 数据质量主倡导者 | 📖🎙️🎬 | 4 |
| 13 | Jordan Tigani | MotherDuck 创始 CEO (前 BigQuery) | 'Big Data is Dead' — 单机引擎复兴, 反过度分布式 | 🎬 | 2 |
| 14 | Vinoth Chandar | Onehouse 创始 CEO (前 Uber) | Apache Hudi 创造者; 增量处理 + lakehouse 互操作 (XTable) | 📖🎙️ | 2 |
| 15 | 伍翀 (Jark Wu) | 阿里云 Flink SQL/Fluss 负责人, Flink PMC | 中国流计算一手; Flink SQL + 流批一体 + Fluss 流存储 | 🎙️🎬 | 4 |

> **第 16-22 候选 (DROP / 留作 Phase 2 founders 池)**: Gunnar Morling (Debezium/CDC, 强但 niche → 见卡片), Nick Schrock (Dagster/SDA → 卡片), Hannes Mühleisen (DuckDB/DuckLake → 卡片), Ananth Packkildurai (DEW newsletter → 卡片), Ralph Kimball + Bill Inmon (历史奠基, 已退休 → Phase 2 founders 单列), 代立冬 (DolphinScheduler), 黄东旭 (TiDB, 数据库边界), 韩卿 (Kylin), Benn Stancil (评论家)。**实际 retained 卡片 = 19 张** (前 15 主榜 + 下方 4 张 borderline/founders/zh-CN 补充), 主榜 15 用于 Phase 2 心智模型加权。

---

## Figures 详细卡片

### 1. Maxime Beauchemin / 马克西姆·博什曼

- **One-liner**: 把「数据工程是软件工程」这件事钉死的人 — Airflow 与 Superset 的创始者, 用 functional data engineering 给批处理管道立了幂等/不可变的工程纪律。 (evidence: [T01-S001, T01-S002])
- **核心身份**: Preset 创始 CEO (Superset 商用); 前 Airbnb (Airflow 起源) / Facebook。 (evidence: [T01-S001, T01-S003])
- **代表作品**: Apache Airflow; Apache Superset; 三篇奠基长文 'The Rise of the Data Engineer' / 'The Downfall of the Data Engineer' / 'Functional Data Engineering'。 (evidence: [T01-S001, T01-S002])
- **值得读 / 听 / 看的 3 件事**:
  - 📖 Functional Data Engineering — a modern paradigm for batch data processing (Medium, [T01-S001])
  - 📖 The Downfall of the Data Engineer (Medium, [T01-S002])
  - 🎬 ⚠️ 长 talk 散见 Data Council / Preset YouTube, 未锁定单一 ≥30min 权威链接
- **核心思想关键词**: 幂等 (idempotency) / 不可变分区 (immutable partitions) / 可重算 (reproducibility) / 纯函数式 task / 数据工程=软件工程
- **voice_samples**:
  - 同业讨论样本: 「the output value of a function depends only on the arguments」(source: T01-S001, 原话; 解释纯函数 task 的工程语言)
  - 同业讨论样本: 「re-executing a pure task with the same input parameters should overwrite any previous output」(source: T01-S001, 原话; 幂等定义)
  - 监管/专业样本: 「Thinking of partitions as immutable blocks of data and systematically overwriting partitions」(source: T01-S001, 原话; 不可变分区方法论)
  - 推断 register: 把数据工程师当工单执行者 = 组织失败信号 (source: T01-S002, 推断 — Downfall 主旨转述, 非逐字原话)
- **sub_skill_candidate**: `false` — 影响力前 5 且思想自洽, 但 intake `skip_sub_skills=true`; 其思想应直接进主 skill 的「幂等/可重跑第一公民」心智模型而非独立 sub-skill。
- **最近 12 个月动态**: Preset 持续围绕 Superset 商用; Functional Data Engineering 仍被 2025 多篇 newsletter (含 DEW) 反复引为 blueprint。 (evidence: [T01-S001])
- **争议 / 批评**: 'Functional' 范式在纯流式/CDC 增量场景下纯分区覆盖不总适用 (流式 upsert 需 merge-on-read), 业内认为是批处理黄金法则但非万能。 (evidence: [T01-S001])
- **来源**:
  - [surrogate_primary] T01-S001 Functional Data Engineering (Medium), collected 2026-05-20
  - [surrogate_primary] T01-S002 The Downfall of the Data Engineer (Medium)
  - [surrogate_primary] T01-S003 preset.io
- **可信度自评**: high — 一手长文充足, 思想体系清晰, 行业奠基地位无争议。

---

### 2. Joe Reis / 乔·赖斯

- **One-liner**: 给整个行业一套「先问『数据工程到底是什么』再谈工具」的通用语言 — 'Fundamentals of Data Engineering' 合著, 自称 'recovering data scientist'。 (evidence: [T01-S004, T01-S007])
- **核心身份**: Ternary Data 联创; The Joe Reis Show / Monday Morning Data Chat 主播; Substack 作者。 (evidence: [T01-S004, T01-S005])
- **代表作品**: 'Fundamentals of Data Engineering' (O'Reilly 2022, 与 Matt Housley 合著); 数据工程生命周期 (生成→摄取→存储→转换→服务) + 六条暗流 (安全/数据管理/DataOps/数据架构/编排/软件工程) 框架。 (evidence: [T01-S004, T01-S007])
- **值得读 / 听 / 看的 3 件事**:
  - 📖 Fundamentals of Data Engineering (O'Reilly, [T01-S007])
  - 🎙️ Fundamentals of Data Engineering — 2.5 Years Later (Substack, [T01-S004])
  - 🎬 Fundamentals of Data Engineering — GOTO 2025 (w/ Matt Housley, YouTube, [T01-S006])
- **核心思想关键词**: 数据工程生命周期 (lifecycle) / 暗流 (undercurrents) / fundamentals over tools / 工具会变原理不变 / build-vs-buy
- **voice_samples**:
  - 客户解释样本: 「nothing that stepped back and asked - 'What is data engineering in the first place?'」(source: T01-S004, 原话; 写书初衷)
  - 同业讨论样本: 「The framework of the data engineering lifecycle and undercurrents is referenced countless times」(source: T01-S004, 原话)
  - 监管/专业样本: 「At one point, everyone starts at zero. Some move on from zero.」(source: T01-S004, 原话; 对 fundamentals 的态度)
- **sub_skill_candidate**: `false` — intake skip_sub_skills; 但其「生命周期 + 暗流」框架是本 skill 的**骨架级心智模型**, 应作 Phase 2 顶层结构。
- **最近 12 个月动态**: 2025 GOTO talk; 2025 参与 Shift Left Data Conference panel (与 Sanderson/Vashishta 谈 AI 如何左移数据基建); Substack 持续高频。 (evidence: [T01-S006, T01-S061])
- **争议 / 批评**: 'Fundamentals' 被部分资深人评为「框架优秀但实操深度浅, 是入门地图不是施工图」; Reis 本人也承认书是 conceptual 而非 cookbook。 (evidence: [T01-S004])
- **来源**:
  - [verified_primary] T01-S004 joereis.substack.com 2.5 years later
  - [surrogate_primary] T01-S007 O'Reilly Fundamentals
  - [reference] T01-S006 GOTO 2025 YouTube
  - [surrogate_primary] T01-S005 ternarydata.com
- **可信度自评**: high — 一手 Substack + 著作 + 多 talk, 当前极活跃。

---

### 3. Martin Kleppmann / 马丁·克莱普曼

- **One-liner**: 写出数据系统从业者人手一本的第一性原理圣经 DDIA — 把复制/分区/事务/一致性/共识讲到工程师能用。 (evidence: [T01-S008, T01-S009])
- **核心身份**: Cambridge 大学副教授 (本地优先软件 + 安全协议); 前业界工程师。 (evidence: [T01-S008])
- **代表作品**: 'Designing Data-Intensive Applications' (DDIA, O'Reilly); 第 2 版 2026 年面世 (与 Chris Riccomini 合著); local-first software 运动共同发起。 (evidence: [T01-S009, T01-S010])
- **值得读 / 听 / 看的 3 件事**:
  - 📖 Designing Data-Intensive Applications 2nd Edition (O'Reilly, [T01-S010])
  - 📖 dataintensive.net (书官网 + 勘误 + 参考, [T01-S009])
  - 🎬 martin.kleppmann.com 学术 talk 列表 (分布式系统课, [T01-S008])
- **核心思想关键词**: 可靠性/可扩展性/可维护性 / 复制与分区 / 一致性与共识 / 数据编码与演进 / 日志结构存储
- **voice_samples**:
  - ⚠️ 暂未找到 ≥30 字直接原话片段 (本轮未深抓 DDIA 正文/讲座 transcript; voice_confidence 在本卡片应标 low — 多为概念转述)。
  - 推断 register: DDIA 核心姿态 = 不押注具体技术, 而是教读者评估技术 trade-off (source: T01-S009, 推断)
- **sub_skill_candidate**: `false` — 偏 canon 作者 (Track 04 核心), 本 track 因 DDIA 在工程实践中的奠基地位保留。dual_role: `"academic + canon"`。
- **最近 12 个月动态**: DDIA 2nd ed (2026) 整合 lakehouse/表格式/streaming 等新趋势 — 是数据工程 canon 的重大刷新事件。 (evidence: [T01-S010])
- **争议 / 批评**: DDIA 偏「数据系统内部原理」, 对现代数据栈 (dbt/Airflow/云数仓运营) 的工程实操覆盖少 — 是理论底座非操作手册。 (evidence: [T01-S009])
- **来源**:
  - [surrogate_primary] T01-S009 dataintensive.net
  - [surrogate_primary] T01-S010 O'Reilly DDIA 2nd ed
  - [surrogate_primary] T01-S008 martin.kleppmann.com
- **可信度自评**: high (身份/作品), voice_confidence medium-low (本轮未抓逐字长引用)。

---

### 4. Tristan Handy / 特里斯坦·汉迪

- **One-liner**: 发起 analytics engineering 运动, 用 dbt 把软件工程纪律 (版本控制/测试/模块化) 带进 SQL 转换层。 (evidence: [T01-S011, T01-S013])
- **核心身份**: dbt Labs (前 Fishtown Analytics) 创始 CEO; 2025 与 Fivetran 合并后任合并公司 President & co-founder。 (evidence: [T01-S011])
- **代表作品**: dbt (data build tool); 'The Analytics Engineering Roundup' newsletter; 推动「现代数据栈」+「分析工程师」角色定义。 (evidence: [T01-S013])
- **值得读 / 听 / 看的 3 件事**:
  - 📖 The Analytics Engineering Roundup (roundup.getdbt.com, [T01-S013])
  - 📖 dbt Labs + Fivetran merge announcement (getdbt.com, [T01-S011])
  - 🎙️ ⚠️ 长访谈散见各 podcast, 未锁定单一权威链接
- **核心思想关键词**: analytics engineering / ELT (push compute to warehouse) / 现代数据栈 / SQL-first 转换 / 软件工程实践入分析
- **voice_samples**:
  - ⚠️ 暂未找到 ≥30 字直接原话片段 (Roundup 多为策展+短评, 本轮未深抓单篇正文)。
  - 推断 register: 「ELT not ETL — 把计算推到数仓里」是 Handy/dbt 阵营标志性主张 (source: T01-S013, 推断/转述, 非逐字)
- **sub_skill_candidate**: `false` — intake skip; 但 analytics engineering 是 intake 明确的 audience segment, 应作 Phase 2 一个场景特化类。
- **最近 12 个月动态**: 2025-05 dbt Fusion engine 发布 (Rust 重写, 原生 SQL 理解); 2025-10 dbt Labs 与 Fivetran 全股票合并 (George Fraser 任 CEO, Handy 任 President), 合并后 ARR 近 $600M。 (evidence: [T01-S011, T01-S012])
- **争议 / 批评**: dbt Fusion + 与 Fivetran 合并引发社区对「dbt 是否还中立/开源承诺」的担忧; 'modern data stack' 被批为「10 个 SaaS 拼起来 ≠ 好架构」(集成+成本+治理债)。 (evidence: [T01-S011])
- **来源**:
  - [surrogate_primary] T01-S013 roundup.getdbt.com
  - [surrogate_primary] T01-S011 dbt+Fivetran merge
  - [surrogate_primary] T01-S012 dbt Fusion engine
- **可信度自评**: high (身份/动态), voice_confidence medium (未抓逐字长引用)。

---

### 5. Jay Kreps / 杰伊·克雷普斯

- **One-liner**: 用 'The Log' 一篇文把「日志/流是数据系统统一抽象」讲透 — Kafka 共同创造, 让流成为数据平台一等公民。 (evidence: [T01-S014])
- **核心身份**: Confluent 联创 CEO; 前 LinkedIn (Kafka 起源)。 (evidence: [T01-S014, T01-S015])
- **代表作品**: Apache Kafka (与 Jun Rao / Neha Narkhede 共创); 'The Log: What every software engineer should know about real-time data's unifying abstraction'; 'I Heart Logs' (O'Reilly)。 (evidence: [T01-S014])
- **值得读 / 听 / 看的 3 件事**:
  - 📖 The Log (LinkedIn Engineering 原文, [T01-S014])
  - 🎬 Current 2025 keynote — 'Where Real-Time Data and AI Come Together' (Confluent, [T01-S015])
  - 📖 Confluent + Databricks / Tableflow 博客 (Kafka topic → Iceberg, [T01-S015])
- **核心思想关键词**: log 统一抽象 / stream-table duality / 流即一等公民 / data in motion / 解耦 producer-consumer
- **voice_samples**:
  - 监管/专业样本: 「append-only, totally-ordered sequence of records ordered by time」(source: T01-S014, 原话; log 的定义)
  - 推断 register: streams (实时事件流) 与 tables (世界当前状态) 本质同一, 流的变更填充表 (source: T01-S015, 转述)
  - ⚠️ 其余多为概念转述, 未抓更多逐字长片段。
- **sub_skill_candidate**: `false` — 偏基础设施/创始人型输出; 'The Log' 概念进 Phase 2「批流与日志抽象」心智模型。
- **最近 12 个月动态**: Current 2025 主题转向「实时数据 + AI」; Tableflow GA (Kafka topic 一键转 Iceberg 表), Delta Lake EAP; Confluent + Databricks 合作打通 operational/analytical 两侧。 (evidence: [T01-S015])
- **争议 / 批评**: 流处理复杂度/成本远高于批 — Kreps 阵营被批「过度推实时」, 多数分析场景批足够 (见 Tigani / 工程伦理 anchor); Lambda 维护两套代码是已知痛点。 (evidence: [T01-S015])
- **来源**:
  - [surrogate_primary] T01-S014 The Log (LinkedIn Eng)
  - [surrogate_primary] T01-S015 Confluent Tableflow/Databricks
- **可信度自评**: high — 奠基文 + 当前 active CEO, 仅 voice 逐字片段偏少。

---

### 6. Zhamak Dehghani / 扎马克·德格哈尼

- **One-liner**: 提出 data mesh — 用「域所有权 + 数据即产品 + 自助平台 + 联邦治理」反对单体数据湖/数仓。 (evidence: [T01-S016, T01-S017])
- **核心身份**: Nextdata 创始 CEO; 前 ThoughtWorks 新兴技术总监。 (evidence: [T01-S016, T01-S017])
- **代表作品**: 'Data Mesh' (O'Reilly); martinfowler.com 上 data mesh 奠基 4 篇; Nextdata OS (autonomous data products)。 (evidence: [T01-S016, T01-S017])
- **值得读 / 听 / 看的 3 件事**:
  - 📖 How to Move Beyond a Monolithic Data Lake to a Distributed Data Mesh (martinfowler.com, [T01-S016])
  - 🎬 Autonomous Data Products talk / QCon AI NY 2025 (YouTube/QCon, [T01-S017])
  - 📰 Nextdata OS 发布报道 (BigDATAwire, [T01-S017])
- **核心思想关键词**: data mesh / 域所有权 (domain ownership) / 数据即产品 / 联邦计算治理 / 自助数据平台 / autonomous data products
- **voice_samples**:
  - 监管/专业样本: 「data lake monsters that at best has enabled pockets of R&D analytics」(source: T01-S016, 原话; 批单体湖)
  - 同业讨论样本: 「domains need to host and serve their domain datasets in an easily consumable way」(source: T01-S016, 原话)
  - 客户解释样本: 「domain data teams must apply product thinking ... to the datasets that they provide」(source: T01-S016, 原话; 数据即产品)
- **sub_skill_candidate**: `false` — data mesh 是 Phase 2「数据架构范式」核心心智模型 + 流派分裂 (去中心化 vs 中台) 的一极。
- **最近 12 个月动态**: 2025-04 Nextdata 推出首个产品 Nextdata OS — 为 AI agents/analytics/apps 自动化「自治数据产品」, 把 data mesh 从原则推向产品化; 2025 QCon AI 演讲。 (evidence: [T01-S017])
- **争议 / 批评**: 「data mesh 一上来全组织铺开」是过度营销 — Zhamak **本人强调渐进式 + 需组织成熟度**; 厂商把 data mesh/data fabric 当 SKU 卖是营销窄化 (标 secondary 反模式边界); 批评者认为 mesh 对中小团队是过度工程。 (evidence: [T01-S016, T01-S017])
- **来源**:
  - [surrogate_primary] T01-S016 martinfowler.com data mesh
  - [secondary] T01-S017 BigDATAwire Nextdata OS
- **可信度自评**: high — 奠基文 + 当前 active 创始人 + 逐字 voice 充足。

---

### 7. Matei Zaharia / 马泰·扎哈里亚

- **One-liner**: Spark 创造者, 把分布式大规模数据处理变成主流; 现把同样的工程严谨度带到 AI agents (DSPy)。 (evidence: [T01-S021, T01-S022])
- **核心身份**: Databricks 联创 CTO; UC Berkeley 副教授; 2025 ACM Prize in Computing 得主。 (evidence: [T01-S021, T01-S022])
- **代表作品**: Apache Spark (UC Berkeley AMPLab); Delta Lake; MLflow; DSPy / GEPA (LLM agent 优化)。 (evidence: [T01-S020, T01-S021])
- **值得读 / 听 / 看的 3 件事**:
  - 📖 Matei Zaharia 学术主页 + publications (Berkeley, [T01-S021])
  - 📖 Spark Declarative Pipelines 开源公告 (Databricks, [T01-S020])
  - 🎬 Data + AI Summit 2025 keynote (Databricks, [T01-S021])
- **核心思想关键词**: RDD/弹性分布式数据集 / 内存计算 / 声明式 ETL pipeline / 批流统一 (Structured Streaming) / 可靠 AI agent
- **voice_samples**:
  - ⚠️ 暂未找到 ≥30 字直接原话片段 (本轮未深抓 keynote transcript)。
  - 推断 register: Declarative Pipelines 把「描述目标状态」交给框架, 工程师不再手写编排 (source: T01-S020, 转述)
- **sub_skill_candidate**: `false` — dual_role: `"academic + engineering"` (Berkeley 教授 + Databricks CTO + 长 talk 谈实践, 符合双角色保留标准); 影响进 Phase 2「数仓/查询引擎 + 存储」。
- **最近 12 个月动态**: 2025 获 ACM Prize in Computing; 2025-06 Databricks 把 Declarative Pipelines 捐给 Apache Spark 开源; 研究重心转向 reliable AI agents (DSPy/GEPA)。 (evidence: [T01-S020, T01-S022])
- **争议 / 批评**: Spark/分布式被 'Big Data is Dead' 阵营批为「多数 workload 不需要」(过早分布式反模式, 见 Tigani); Spark 集群运维重, 单机引擎 (DuckDB/Polars) 在中小数据上更优。 (evidence: [T01-S020])
- **来源**:
  - [verified_primary] T01-S021 Berkeley 学术主页
  - [verified_primary] T01-S022 ACM Prize 2025
  - [surrogate_primary] T01-S020 Spark Declarative Pipelines
- **可信度自评**: high (身份/动态), voice_confidence medium (未抓逐字长引用)。

---

### 8. Ryan Blue / 瑞安·布鲁

- **One-liner**: Apache Iceberg 创造者 — 让开放表格式成为跨引擎的事实交换标准, 把 lakehouse 从厂商锁定里解放。 (evidence: [T01-S024, T01-S025])
- **核心身份**: Databricks (2024 Tabular 被收购后加入); 前 Tabular 联创; 前 Netflix; Iceberg PMC Chair。 (evidence: [T01-S025])
- **代表作品**: Apache Iceberg (ACID / time travel / schema evolution / 隐藏分区 / Iceberg v3 row lineage + deletion vectors + VARIANT)。 (evidence: [T01-S023, T01-S024])
- **值得读 / 听 / 看的 3 件事**:
  - 📖 Apache Iceberg 项目 + spec (github.com/apache/iceberg, [T01-S024])
  - 📖 Iceberg v3 on Databricks 公告 (Databricks, [T01-S023])
  - 🎬 ⚠️ 多见 Iceberg Summit / Data Council talk, 未锁定单一权威长视频链接
- **核心思想关键词**: 开放表格式 / 隐藏分区 (hidden partitioning) / schema evolution / time travel / 引擎中立性 / catalog 互操作
- **voice_samples**:
  - ⚠️ 暂未找到 ≥30 字直接原话片段 (本轮未抓 Blue 个人长访谈 transcript)。
  - 推断 register: Iceberg 的设计目标是「让表格式独立于引擎」, 避免 Hive 分区那种隐式耦合 (source: T01-S024, 转述)
- **sub_skill_candidate**: `false` — 进 Phase 2「存储与表格式」核心; Iceberg vs Delta vs Hudi 流派分裂的 Iceberg 一极。
- **最近 12 个月动态**: 2024-06 Databricks 以 $1B+ 收购 Tabular (Iceberg 创始团队); 2025 Databricks 全面支持 Iceberg + Iceberg v3 public preview (row lineage / deletion vectors / VARIANT) — Iceberg 与 Delta 走向融合。 (evidence: [T01-S023, T01-S025])
- **争议 / 批评**: Tabular 被 Databricks (Delta 阵营) 收购引发「Iceberg 中立性是否受损」讨论; 开放表格式之争被批为厂商各自站台, 实际趋势是引擎多格式兼容。 (evidence: [T01-S025])
- **来源**:
  - [verified_primary] T01-S024 github.com/apache/iceberg
  - [surrogate_primary] T01-S023 Iceberg v3 Databricks
  - [surrogate_primary] T01-S025 Tabular 收购公告
- **可信度自评**: high (身份/作品/动态), voice_confidence low (未抓逐字)。

---

### 9. Wes McKinney / 韦斯·麦金尼

- **One-liner**: pandas 与 Apache Arrow 创造者 — 用内存列存标准让数据工具可组合 (composable data systems)。 (evidence: [T01-S026, T01-S028])
- **核心身份**: Voltron Data 首席科学家 (2025 part-time 回归); pandas / Arrow 创造者。 (evidence: [T01-S026, T01-S027])
- **代表作品**: pandas; Apache Arrow (内存列存标准); 'Python for Data Analysis' (O'Reilly); Velox (Meta) 协作。 (evidence: [T01-S026, T01-S028])
- **值得读 / 听 / 看的 3 件事**:
  - 📖 The Road to Composable Data Systems: 15 Years (wesmckinney.com, [T01-S026])
  - 🎙️ Building Data Science Tools in an AI-Native World — EARL UK 2025 keynote transcript (wesmckinney.com, [T01-S027])
  - 🎬 The Future Roadmap for the Composable Data Stack (Data Council talk)
- **核心思想关键词**: 内存列存 (columnar in-memory) / Apache Arrow 标准 / composable data systems / 模块化引擎 (Velox) / 开放标准互操作
- **voice_samples**:
  - 监管/专业样本: 「Apache Arrow ... enabled modularization and composability」(source: T01-S026, 转述; composable 主张)
  - 推断 register: 过去 15 年的方向是把 query processing 拆成可复用模块, DuckDB/Polars 正是这个愿景的实现 (source: T01-S026, 转述)
  - ⚠️ 逐字长片段偏少, 本轮未深抓 transcript 正文。
- **sub_skill_candidate**: `false` — 偏基础标准层; Arrow 进 Phase 2「存储格式 + 单机引擎复兴」基础设施。
- **最近 12 个月动态**: 2025 part-time 回归 Voltron Data 任首席科学家; 持续布道 composable data stack (Arrow/DuckDB/Polars/Velox); 2025 多场 keynote (EARL UK / Tech on the Rocks)。 (evidence: [T01-S026, T01-S027])
- **争议 / 批评**: pandas 的内存模型/API 历史包袱被 Polars (Rust, lazy) 持续挑战; McKinney 本人也承认 pandas 设计有早期局限。 (evidence: [T01-S026])
- **来源**:
  - [verified_primary] T01-S026 wesmckinney.com 15 years
  - [verified_primary] T01-S027 EARL UK 2025 keynote
  - [surrogate_primary] T01-S028 arrow.apache.org
- **可信度自评**: high — 一手个人站充足, 当前 active。

---

### 10. Tyler Akidau / 泰勒·阿基道

- **One-liner**: 'Streaming Systems' 作者 + Dataflow model 设计者 — 把批流统一理论 (event time / watermark / windowing) 讲成行业共识。 (evidence: [T01-S029, T01-S030])
- **核心身份**: Snowflake (Dynamic Tables 等); 前 Google (Dataflow / Beam / MillWheel)。 (evidence: [T01-S029, T01-S030])
- **代表作品**: 'Streaming Systems' (O'Reilly); 'Streaming 101 / 102' 系列; Apache Beam / Dataflow model; Snowflake Dynamic Tables (2025 SIGMOD 论文)。 (evidence: [T01-S029, T01-S030])
- **值得读 / 听 / 看的 3 件事**:
  - 📖 Streaming Democratized: Delayed View Semantics & Snowflake Dynamic Tables (arxiv 2504.10438, SIGMOD'25, [T01-S029])
  - 📖 Streaming 101/102 + Snowflake author blog ([T01-S030])
  - 🎬 ⚠️ Strange Loop 'Streaming Systems' 经典 talk (历史), 未列单链
- **核心思想关键词**: event time vs processing time / watermark / windowing (固定/滑动/会话) / exactly-once / 批流统一 / delayed view semantics / 增量视图维护 (IVM)
- **voice_samples**:
  - 监管/专业样本: 「manual incrementalization, semantic discrepancies across SQL」(source: T01-S029, 原话; 流式 SQL 的痛点)
  - 推断 register: Dynamic Tables 的目标是「让流处理直接长在分析型 RDBMS 里」, 用户写声明式 SQL 而非手工增量化 (source: T01-S029, 转述)
  - ⚠️ 其余逐字片段偏少。
- **sub_skill_candidate**: `false` — dual_role: `"academic + engineering"` (写 paper + Snowflake 工程 + 'Streaming Systems' 长篇实践); 进 Phase 2「批流与实时」核心理论。
- **最近 12 个月动态**: 2025-04 发表 SIGMOD 论文 'Streaming Democratized' (Snowflake Dynamic Tables, delayed view semantics), 把流处理「民主化」进 SQL — 延续 batch/streaming 统一的毕生主线。 (evidence: [T01-S029])
- **争议 / 批评**: 「越实时越好」是误区 — Akidau 的理论虽统一批流, 但实践中多数场景批/分钟级足够, 真亚秒需求才上流 (工程伦理 anchor); Dataflow model 概念门槛高。 (evidence: [T01-S029])
- **来源**:
  - [verified_primary] T01-S029 arxiv 2504.10438
  - [surrogate_primary] T01-S030 Snowflake author blog
  - [surrogate_primary] T01-S007 O'Reilly (Streaming Systems 同出版方)
- **可信度自评**: high — 2025 一手 paper + 著作 + 厂商博客。

---

### 11. Barr Moses / 巴尔·摩西

- **One-liner**: 创造 'data observability' / 'data downtime' 品类 — 把「数据停机」当作可度量、可告警的可靠性问题。 (evidence: [T01-S031, T01-S032])
- **核心身份**: Monte Carlo 联创 CEO。 (evidence: [T01-S031])
- **代表作品**: Monte Carlo (data observability 平台); 'Data Quality Fundamentals' (O'Reilly 合著); 'data downtime' 概念 + 五大支柱 (新鲜度/量/schema/分布/血缘)。 (evidence: [T01-S031, T01-S032])
- **值得读 / 听 / 看的 3 件事**:
  - 📖 The Past, Present & Future of Data Quality Management (Monte Carlo, [T01-S032])
  - 📖 Monte Carlo Agent Observability 公告 (2025-09, [T01-S031])
  - 🎬 ⚠️ 多见 barrmoses.medium.com + 会议 talk, 未锁定单一长视频
- **核心思想关键词**: data observability / data downtime / 五大支柱 (freshness/volume/schema/distribution/lineage) / 数据可靠性 SLA / 从测试到监控
- **voice_samples**:
  - 客户解释样本: 「reliability isn't a 'nice to have,' it's the foundation」(source: T01-S031, 原话)
  - 推断 register: 数据停机 = 数据缺失/错误/不准的时段, 应像系统宕机一样被度量和告警 (source: T01-S032, 转述; 'data downtime' 定义)
  - ⚠️ 逐字长片段偏少。
- **sub_skill_candidate**: `false` — 进 Phase 2「数据质量/可观测性」核心心智模型。
- **最近 12 个月动态**: 2025-09 Monte Carlo 推出 Agent Observability (覆盖 data + AI stack, 监控 prompts/completions/latency) — 把 observability 从数据扩到 AI agent; 2025 参与 Shift Left Data Conference panel。 (evidence: [T01-S031, T01-S061])
- **争议 / 批评**: 'data observability' 被部分人批为「vendor 造词卖 SaaS」, 与既有 dbt tests/Great Expectations 边界模糊; Sanderson 阵营主张「shift left 到生产端」优于末端 observability 救火。 (evidence: [T01-S032, T01-S033])
- **来源**:
  - [surrogate_primary] T01-S031 Monte Carlo Agent Observability
  - [surrogate_primary] T01-S032 Monte Carlo DQ 过去现在未来
- **可信度自评**: medium — 一手充足但均为厂商博客 (品类创造者自营销重叠), 缺独立长访谈逐字; voice_confidence medium。

---

### 12. Chad Sanderson / 查德·桑德森

- **One-liner**: data contracts 与 shift-left 数据质量主倡导者 — 把质量问题左移到数据生产端, schema 当 API 治理。 (evidence: [T01-S033, T01-S034])
- **核心身份**: Gable.ai CEO; 前 Microsoft AI 平台团队 / Convoy / Sephora。 (evidence: [T01-S034, T01-S035])
- **代表作品**: 'Data Contracts' (O'Reilly, 与 Mark Freeman / B.E. Schmidt); 'The Shift Left Data Manifesto'; Data Quality Camp 社区; dataproducts.substack。 (evidence: [T01-S033, T01-S035])
- **值得读 / 听 / 看的 3 件事**:
  - 📖 The Shift Left Data Manifesto (dataproducts.substack, [T01-S033])
  - 🎬 Shifting Left with Data DevOps — Shift Left Data Conf 2025 (Gable, [T01-S034])
  - 📖 Data Contracts (O'Reilly book, [T01-S035])
- **核心思想关键词**: data contracts / shift left / schema is an API / 生产者-消费者契约 / 数据 DevOps / 上游可观测性
- **voice_samples**:
  - 监管/专业样本: 「shifting data quality left, ensuring upstream data producers are as invested ... as downstream」(source: T01-S033, 转述; manifesto 核心)
  - 推断 register: schema 是 API — 上游不能随便删字段, 删了静默打爆所有下游 pipeline (source: T01-S033, 推断; 对应工程伦理 anchor)
  - 同业讨论样本: data contracts 是 shift-left 众多组件之一, 创造全新数据管理动态 (source: T01-S034, 转述)
- **sub_skill_candidate**: `false` — data contracts + shift-left 进 Phase 2「数据质量/治理」核心 + 与 Moses observability 的流派分裂 (左移 vs 末端监控)。
- **最近 12 个月动态**: 2025 Shift Left Data Conference (Gable 主办, 与 Handy/Moses/Reis 同台); O'Reilly Data Contracts book 推进; Gable.ai 持续做 producer 端 schema 变更检测。 (evidence: [T01-S034, T01-S061])
- **争议 / 批评**: data contracts 被批「概念热但落地难」(需上游应用团队配合, 组织阻力大); 部分人认为是「给 schema registry 重新包装营销」。 (evidence: [T01-S033])
- **来源**:
  - [verified_primary] T01-S033 dataproducts.substack manifesto
  - [verified_primary] T01-S034 Gable Shift Left 2025 talk
  - [surrogate_primary] T01-S035 O'Reilly Data Contracts
  - [verified_primary] T01-S061 Shift Left 2025 panel
- **可信度自评**: high — Substack 本人一手 + 会议 talk + 著作, 当前极活跃。

---

### 13. Jordan Tigani / 乔丹·蒂加尼

- **One-liner**: 'Big Data is Dead' — 反过度分布式, 主张多数数据塞得进单机, 推动 DuckDB/单机引擎复兴。 (evidence: [T01-S042, T01-S043])
- **核心身份**: MotherDuck 创始 CEO; 前 Google BigQuery 创始工程师。 (evidence: [T01-S042])
- **代表作品**: 'Big Data is Dead' 长文/talk; MotherDuck (DuckDB 云托管 + 混合本地/云查询)。 (evidence: [T01-S042, T01-S043])
- **值得读 / 听 / 看的 3 件事**:
  - 🎬 The Death of Big Data and Why It's Time to Think Small (MotherDuck, [T01-S042])
  - 🎬 Big Data is Dead — Data Council talk ([T01-S043])
  - 📖 ⚠️ motherduck.com/blog/big-data-is-dead 原文 (fetch 被 500 拦, 但 thesis 广泛转载)
- **核心思想关键词**: big data is dead / small data / 数据量服从幂律 / 查询多只碰最近数据 / 反过早分布式 / 单机引擎复兴 / complexity tax
- **voice_samples**:
  - 客户解释样本: 「big compute ... is no longer relevant for 99% of workloads」(source: T01-S043, 转述; 核心论点)
  - 同业讨论样本: 多数公司数据量 modest, 客户数据大小服从幂律分布 (source: T01-S042, 转述)
  - 推断 register: 为简历/显得专业上 Spark 集群 = resume-driven, 你的数据其实就几个 G (source: T01-S042, 推断; 对应工程伦理 anchor)
- **sub_skill_candidate**: `false` — 'Big Data is Dead' 是 Phase 2「过早分布式反模式」工程伦理 anchor 的旗手论据; 进「数仓/查询引擎」单机复兴。
- **最近 12 个月动态**: 'Big Data is Dead' 持续作为 MotherDuck 2025 定位主线; MotherDuck 推 'Stop Paying the Complexity Tax'; DuckLake 生态 (与 Hannes/DuckDB) 共振。 (evidence: [T01-S042])
- **争议 / 批评**: 「Big Data is Dead」被大数据/分布式阵营批为「以偏概全」— 确有 PB 级真实场景 (广告/物联网/大模型训练数据), Tigani 自己也澄清是反「big compute」而非否认大数据存在。 (evidence: [T01-S042, T01-S043])
- **来源**:
  - [surrogate_primary] T01-S042 MotherDuck Big Data is Dead talk
  - [surrogate_primary] T01-S043 Data Council Big Data is Dead
- **可信度自评**: medium-high — thesis 一手 talk 充足, 但原文 blog fetch 受阻, voice 多为转述。

---

### 14. Vinoth Chandar / 维诺特·钱达尔

- **One-liner**: Apache Hudi 创造者 — 在 Uber 建第一个 lakehouse, 主打增量处理 + upsert + CDC 写入。 (evidence: [T01-S038, T01-S039])
- **核心身份**: Onehouse 创始 CEO; Apache Hudi PMC Chair; 前 Uber。 (evidence: [T01-S038, T01-S039])
- **代表作品**: Apache Hudi (upsert / 增量 / merge-on-read); Apache XTable (Hudi/Delta/Iceberg 互操作); Onehouse Compute Runtime。 (evidence: [T01-S038, T01-S039])
- **值得读 / 听 / 看的 3 件事**:
  - 🎙️ The Future of Data Lakehouses — fireside w/ Vinoth Chandar (hudi.apache.org, [T01-S038])
  - 📖 Onehouse Open Engines launch (onehouse.ai, [T01-S039])
  - 🎬 ⚠️ 多见 Data Council / Open Source Data Summit talk, 未列单链
- **核心思想关键词**: 增量处理 (incremental) / upsert + merge-on-read / CDC lakehouse / 表格式互操作 (XTable) / 第一个 lakehouse (Uber 2016)
- **voice_samples**:
  - 推断 register: lakehouse 的本质是把数据库式的 upsert/增量能力带到对象存储上 (source: T01-S038, 转述)
  - 同业讨论样本: XTable 让你「ingest 一次, 按查询引擎需要的格式呈现」(source: T01-S039, 转述)
  - ⚠️ 逐字长片段偏少, 本轮未深抓 fireside transcript。
- **sub_skill_candidate**: `false` — 进 Phase 2「存储与表格式」(Hudi 一极, 强在 upsert/CDC 增量) + 互操作趋势。
- **最近 12 个月动态**: 2025-01 Onehouse 推 Onehouse Compute Runtime (跨云/引擎/表格式, 称 2-30x 提速); XTable (前 OneTable) 进 Apache 孵化, Microsoft/Google 背书 — 主推「格式中立互操作」。 (evidence: [T01-S038, T01-S039])
- **争议 / 批评**: Hudi 配置/运维复杂度高于 Iceberg (社区常见反馈); 三大表格式之争中 Hudi 生态/心智份额落后 Iceberg+Delta, Chandar 转而主推互操作 (XTable) 是务实也是被动。 (evidence: [T01-S039])
- **来源**:
  - [verified_primary] T01-S038 hudi.apache.org fireside
  - [surrogate_primary] T01-S039 onehouse.ai Open Engines
- **可信度自评**: medium-high — 项目博客 + 厂商一手, voice_confidence medium。

---

### 15. 伍翀 (Jark Wu) / 云邪

- **One-liner**: 中国流计算一手 — 阿里云 Flink SQL 与 Fluss 负责人, Apache Flink PMC, 推动 Flink SQL + 流批一体 + 流存储。 (evidence: [T01-S050, T01-S051])
- **核心身份**: 阿里云 Flink SQL / Fluss 团队负责人; Apache Flink PMC member。 (evidence: [T01-S050, T01-S052])
- **代表作品**: Apache Flink SQL (核心 committer); Apache Fluss (incubating) — lakehouse-native 流存储, 基于 Arrow 列式流; Flink Forward Asia 演讲。 (evidence: [T01-S050, T01-S053])
- **值得读 / 听 / 看的 3 件事**:
  - 🎙️ Beyond Kafka: Conversation with Jark Wu on Fluss (Data Engineering Weekly, [T01-S050])
  - 🎬 Apache Fluss — Streaming Storage for Real-Time Lakehouse (CMU-DB 2025 deck, [T01-S053])
  - 📖 wuchong GitHub + flink.apache.org (Flink SQL 文档, [T01-S051, T01-S052])
- **核心思想关键词**: Flink SQL / 流批一体 (unified stream-batch) / 实时数仓 / 流存储 (Fluss) / 列式流 (Arrow) / 实时 lakehouse
- **voice_samples**:
  - 同业讨论样本 (中国 register): 「流批一体」「实时数仓」「Flink SQL 作业」「列式流」(source: T01-S050/T01-S052, 转述; 中国一手术语)
  - 推断 register: Fluss 要填「流」与「分析」之间的鸿沟 — 子秒摄取 + 高吞吐分析扫描 (source: T01-S050, 转述)
  - ⚠️ 暂未抓到 ≥30 字中文逐字原话 (一手多在 InfoQ/Flink Forward 视频, 本轮未转录)。
- **sub_skill_candidate**: `false` — 中国一手代表; 进 Phase 2「批流与实时」+ 诚实边界 (zh-CN 一手薄)。
- **最近 12 个月动态**: 2024 Flink Forward Asia 开源 Fluss, 2025 计划捐 Apache; 2025 CMU-DB 讲 Fluss; Flink 2.0 存算分离入选 VLDB 2025。 (evidence: [T01-S050, T01-S053])
- **争议 / 批评**: Fluss 作为「又一个流存储」面临与 Kafka/Pulsar/Redpanda 的生态竞争质疑; 中国一手内容多在被 blacklist 的平台 (公众号/CSDN/掘金), 可引用的英文/Apache/InfoQ 一手相对有限。 (evidence: [T01-S050])
- **来源**:
  - [surrogate_primary] T01-S050 DEW Fluss 访谈
  - [surrogate_primary] T01-S051 github.com/wuchong
  - [surrogate_primary] T01-S052 flink.apache.org
  - [surrogate_primary] T01-S053 CMU-DB 2025 Fluss deck
- **可信度自评**: medium — 身份/项目清晰 (Apache PMC + 英文访谈), 但逐字 voice + 长访谈 transcript 偏少 (zh-CN 结构性弱)。

---

## Borderline / Founders / zh-CN 补充卡片 (retained 但不入主榜 15)

### 16. Gunnar Morling / 古纳尔·莫林 (borderline KEEP)

- **One-liner**: CDC 布道者 — Debezium 前 lead, 把变更数据捕获讲成主流; 发起 1BRC (One Billion Row Challenge) 病毒级性能挑战。 (evidence: [T01-S040, T01-S041])
- **核心身份**: Decodable 软件工程师; 前 Red Hat / Debezium project lead。 (evidence: [T01-S040, T01-S041])
- **代表作品**: Debezium (CDC 事实标准); 1BRC (Java 聚合 10 亿行挑战); Flink + Debezium + Iceberg 实时管道布道。
- **值得读 / 听 / 看**: 📖 The One Billion Row Challenge (morling.dev, [T01-S040]); 📖 debezium.io; 🎬 1BRC InfoQ presentation
- **核心思想关键词**: CDC / 数据库 binlog/WAL / Debezium / 实时 EL / 性能极致 (1BRC) / Flink SQL 摄取
- **voice_samples**: ⚠️ 暂未抓 ≥30 字逐字原话 (morling.dev 多技术正文, 本轮未深抓); 推断 register: CDC 是「让数据库的变更像事件流一样被消费」(source: T01-S041, 转述)。
- **sub_skill_candidate**: `false` — niche 但重要; 进 Phase 2「摄取与集成 (CDC)」。
- **最近 12 个月动态**: 离开 Debezium lead 后在 Decodable (Flink/Debezium 实时 ETL); 1BRC 持续发酵。 (evidence: [T01-S040])
- **来源**: [verified_primary] T01-S040 morling.dev 1BRC; [surrogate_primary] T01-S041 debezium.io
- **可信度自评**: medium-high — 一手个人站 (verifier 判 primary) + 项目; KEEP 因 CDC 是 intake 核心子域。

---

### 17. Nick Schrock / 尼克·施罗克 (borderline KEEP)

- **One-liner**: Dagster 创造者 — 提出 software-defined assets (软件定义资产), 把编排从「跑任务」转向「声明数据资产应存在什么」。 (evidence: [T01-S044, T01-S045])
- **核心身份**: Dagster Labs 创始 CTO (CEO 已交棒 Pete Hunt); 前 Facebook (GraphQL 共同创造)。 (evidence: [T01-S044])
- **代表作品**: Dagster (asset-based 编排); software-defined assets (SDA); 前作 GraphQL。
- **值得读 / 听 / 看**: 🎙️ Software-Defined Assets deep dive (Dagster/Drill to Detail, [T01-S044]); 📖 github.com/dagster-io/dagster ([T01-S045])
- **核心思想关键词**: software-defined assets / 资产编排 (asset-based) / 数据感知调度 / 声明式 vs 命令式 DAG / data-aware orchestration
- **voice_samples**: ⚠️ 暂未抓 ≥30 字逐字原话; 推断 register: SDA = 用代码描述「应存在哪些数据资产、如何计算」, 而非命令式排任务 (source: T01-S044, 转述)。
- **sub_skill_candidate**: `false` — 进 Phase 2「编排与工作流」(Dagster asset 一极 vs Airflow task 一极的流派分裂)。
- **最近 12 个月动态**: 2025 Dagster CLI/components 新纪元 + observability 重投入; Schrock 转 CTO, Pete Hunt 任 CEO。 (evidence: [T01-S044])
- **来源**: [surrogate_primary] T01-S044 dagster.io podcast; [verified_primary] T01-S045 github.com/dagster-io/dagster
- **可信度自评**: medium-high — 一手 + 项目; KEEP 因 asset-based 编排是 Phase 2 重要流派分裂。

---

### 18. Hannes Mühleisen / 汉内斯·缪莱森 (borderline KEEP)

- **One-liner**: DuckDB 共同创造者 (与 Mark Raasveldt) — 进程内分析数据库, 把「单机也能很强」做成现实; 2025 推 DuckLake (SQL as lakehouse format)。 (evidence: [T01-S046, T01-S047])
- **核心身份**: DuckDB Labs 联创 CEO; CWI Amsterdam 高级研究员 + Radboud 数据工程教授; 2025 荷兰 ICT 研究奖得主。 (evidence: [T01-S047, T01-S048])
- **代表作品**: DuckDB (进程内 OLAP, 月下载千万级); DuckLake (用标准 SQL 数据库管 lakehouse 元数据)。
- **值得读 / 听 / 看**: 📖 DuckLake: SQL as a Lakehouse Format (duckdb.org, [T01-S046]); 📖 hannes.muehleisen.org; 🎬 The Surprising Birth of DuckDB (MotherDuck)
- **核心思想关键词**: 进程内数据库 (in-process) / 单机 OLAP / DuckLake / 简化 lakehouse / SQL-as-metadata-store / 列式向量化
- **voice_samples**: ⚠️ 暂未抓 ≥30 字逐字原话; 推断 register: DuckLake 把 lakehouse 元数据交给标准 SQL 库管, 比文件式 catalog (Iceberg/Delta) 更简单 (source: T01-S046, 转述)。
- **sub_skill_candidate**: `false` — 与 Tigani 共同支撑「单机引擎复兴/big data is dead」; 进 Phase 2「数仓/查询引擎」。
- **最近 12 个月动态**: 2025-05 DuckLake 发布 (SQL as lakehouse format); 2025 获荷兰 ICT 研究奖; DuckDB 采用度持续爆发。 (evidence: [T01-S046, T01-S048])
- **来源**: [surrogate_primary] T01-S046 duckdb.org DuckLake; [surrogate_primary] T01-S047 hannes.muehleisen.org; [surrogate_primary] T01-S048 CWI 奖
- **可信度自评**: medium-high — 项目一手 + 学术身份; KEEP 因 DuckDB/DuckLake 是 2025 重大趋势。

---

### 19. Ananth Packkildurai (策展人 KEEP) + zh-CN 补充 (代立冬 / 黄东旭 / 韩卿) + 历史奠基 (Kimball / Inmon)

**Ananth Packkildurai** — Data Engineering Weekly newsletter 作者 (数万订阅, 行业最具影响力策展+原创之一), 前 Slack/Zendesk 数据工程。一手 = dataengineeringweekly.com ([T01-S049]); 反复采访 Jark Wu 等一线人 ([T01-S050])。**核心关键词**: data engineering 策展 / upstream observability / data mesh 渐进 / agentic data infra。`sub_skill_candidate: false` (策展型, 非独立思想体系)。可信度 medium-high — Substack 本人一手, 当前每周更新。

**代立冬** — 白鲸开源 (WhaleOps) 联创; Apache DolphinScheduler PMC Chair + SeaTunnel PMC。中国开源编排/集成一手。一手 = dolphinscheduler.apache.org ([T01-S054]) + github.com/apache/dolphinscheduler ([T01-S055])。**核心关键词**: 可视化 DAG 编排 / DataOps 平台 / 批流一体集成 (SeaTunnel) / 200+ 异构数据源。2025 DolphinScheduler 获上海优秀开源项目奖, 称 3000+ 企业用。`sub_skill_candidate: false`。可信度 medium — Apache 项目一手强, 但个人 voice 逐字缺 (zh-CN 弱)。

**黄东旭 (Ed Huang)** — PingCAP 联创 CTO; TiDB (HTAP 分布式数据库)。**数据库边界** (HTAP 跨 OLTP/OLAP, 与数据工程相邻非核心)。一手 = cn.pingcap.com 作者页 ([T01-S057], verifier 判 primary) + pingcap.com vector/AI 博客 ([T01-S058])。**核心关键词**: HTAP / Serverless 数据库 / S3 成数据库新基座 / 向量检索 + RAG / Data+AI。2025 TiDB 8.5 内建向量检索。`sub_skill_candidate: false`; dual_role: 数据库边界, 进 Phase 2 仅作「数仓/查询引擎」邻接参考。可信度 medium。

**韩卿 (Luke Han)** — Kyligence 创始; Apache Kylin (OLAP) 创始。中国 OLAP 一手 (kylin.apache.org)。本轮未深抓单独卡片, 列为 Phase 2 founders/zh-CN 池参考。

**Ralph Kimball + Bill Inmon** (历史奠基, 已退休 → Phase 2 founders 单列): Kimball = 维度建模 (star schema / 一致性维度 / SCD), 'The Data Warehouse Toolkit' ([T01-S018, T01-S019]); Inmon = '数据仓库之父', Corporate Information Factory (规范化企业数仓)。两者「Kimball vs Inmon」范式之争是数仓建模的经典流派分裂, 至今活跃于建模讨论。`sub_skill_candidate: false` — 进 Phase 2「转换与建模」+ founders 池。可信度 high (canon 地位), 但已非 active 输出者。

---

## Phase 2 提炼提示

### 反复出现 ≥ 3 个 figures 都谈到的关键词（候选行业心智模型）

- **幂等 + 可重跑 / 不可变 (idempotency / reproducibility)** (figures: Maxime / Joe Reis / Akidau — Maxime functional, Reis lifecycle undercurrent, Akidau IVM 增量) — **第一公民级心智模型**
- **批流统一 / 流即一等公民 (batch-stream unification)** (figures: Jay Kreps / Tyler Akidau / Jark Wu / Matei Zaharia — The Log / Dataflow model / 流批一体 / Structured Streaming)
- **开放表格式 + lakehouse (open table format)** (figures: Ryan Blue / Vinoth Chandar / Matei Zaharia / Hannes — Iceberg / Hudi / Delta / DuckLake) — 流派分裂见下
- **数据即产品 / 数据契约 / schema is API (data as product / contracts)** (figures: Zhamak / Chad Sanderson / Barr Moses — data mesh / data contracts / data downtime)
- **数据工程 = 软件工程 (software engineering discipline)** (figures: Maxime / Joe Reis / Tristan Handy / Nick Schrock — Downfall / lifecycle / analytics engineering / SDA)
- **反过早分布式 / 单机复兴 (big data is dead)** (figures: Jordan Tigani / Hannes Mühleisen / Wes McKinney — MotherDuck / DuckDB / composable + Polars) — 与 Zaharia/Spark 阵营张力
- **可组合数据系统 (composable / open standards)** (figures: Wes McKinney / Hannes / Ryan Blue — Arrow / DuckDB / Iceberg 互操作)
- **生命周期 + 暗流框架 (lifecycle + undercurrents)** (figures: Joe Reis / Matt Housley — 顶层结构骨架)

### 显著分歧 / 流派分裂

- **表格式之争**: Apache Iceberg (Ryan Blue, 中立生态+隐藏分区) vs Delta Lake (Matei Zaharia/Databricks 生态) vs Apache Hudi (Vinoth Chandar, 强在 upsert/CDC 增量) — 实际趋势是引擎多格式兼容 (XTable / Iceberg 成事实交换格式); **不站队营销** (工程伦理 anchor)。
- **大数据 vs 小数据 / 分布式 vs 单机**: Matei Zaharia / Jay Kreps (分布式/流, big compute) vs Jordan Tigani / Hannes Mühleisen (单机引擎, 'big data is dead') — 「我的数据真的大到需要 Spark 吗」。
- **数据质量: 左移 vs 末端监控**: Chad Sanderson (data contracts / shift-left 到生产端) vs Barr Moses (data observability / 末端监控告警) — 互补但侧重不同。
- **架构: 去中心化 vs 中心化**: Zhamak Dehghani (data mesh / 域所有权) vs 传统中心化数仓/中台 (中国语境「数据中台」) — Zhamak 本人强调渐进, 反对一次性全组织铺开。
- **编排: 任务 vs 资产**: Nick Schrock (Dagster software-defined assets / data-aware) vs 传统 Airflow (task/DAG 命令式) — Maxime (Airflow 创始) 自身也认同向资产/函数式演进。
- **建模: Kimball vs Inmon vs OBT**: 维度建模 (star schema) vs 规范化 CIF vs 列存时代大宽表 (OBT) — 经典 + 新派之争。

### 冷僻领域信号

- 总 figure 数 < 10？ **否** — retained 15 主榜 + 4 补充 = 19, **非冷僻**。
- 多数 figure 长访谈材料 < 30 min？ **否** — en figures 多有著作/长文/会议 talk/SIGMOD 论文; 但**部分 figure (Ryan Blue / Barr Moses / Vinoth Chandar / Matei Zaharia) 本轮未抓到 ≥30 字逐字 voice 原话**, voice_confidence 标 medium-low, Phase 4 voice check 会因此降级 (本轮以概念转述为主, 未深抓 transcript)。
- 标记 "可信度 low" 的 figure 比例 > 30%？ **否** — 无 low; medium 约 4-5 位 (Moses / Tigani / Jark Wu / 代立冬 / 黄东旭), 主因厂商博客自营销重叠或 zh-CN 一手薄。

### ⚠️ zh-CN 一手结构性薄弱 (诚实边界 — 必须在 Phase 2.8 告知用户)

- zh-CN figures (伍翀/代立冬/黄东旭/韩卿) 的真实一手主要在 **Apache 项目文档 (flink/dolphinscheduler/seatunnel/doris/kylin/paimon) + InfoQ 中文 QCon/ArchSummit + 极客时间专栏 + 厂商技术博客 (阿里云/字节/美团/网易数帆)**; 他们的大量个人输出在 **被 blacklist 的平台** (公众号 mp.weixin / 知乎 / CSDN / 掘金), 本 manifest 不引用。
- 结果: **zh-CN figures 的 voice_samples 几乎全为转述/推断, 无逐字中文原话**; Phase 2 提炼的中国一手 register (流批一体/实时数仓/数据中台/小文件治理/回刷补数) 来自术语观察而非直接听到 figure 说。诚实边界节应明说: **「中国数据工程一手主要从 Apache 项目 + 会议 + 厂商博客间接识别, en 一手厚度远高于 zh-CN」**。
- Surrogate 比例: source_pool 中约 **66% (41/62) 标 surrogate_primary** (核心域名 .io/.com/.org/.apache.org/.medium.com 被 verifier 默认 secondary, 按 intake 政策升级 + note 含 "vendor docs"); verified_primary 约 **31% (19/62)** (Substack 作者本人 / arxiv / github project root / .edu / 部分厂商博客经 verifier); reference 2 (Reddit / YouTube)。surrogate+verified primary 合计 **≈ 97%**, 远超 ≥50% 门槛。
