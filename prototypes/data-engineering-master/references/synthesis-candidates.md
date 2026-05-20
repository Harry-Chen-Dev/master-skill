# Synthesis Candidates (raw) — Data Engineering

> Phase 2 Step 0 artifact。从 6 轨「Phase 2 接口」段汇集的候选信号池。target ≥ 15 (technical 行业)。

## 候选心智模型 (target 15-30)

| Candidate | 出现于 tracks | 出现 figures / 证据 | 类型 | 评级 (三重验证) | 备注 |
|-----------|-------------|----------------------|------|----------------|------|
| 幂等 + 可重跑 + 不可变分区是第一公民 | 01,02,03,04,06 | Maxime / Joe Reis / Akidau (4+) | cross-track | ✅✅✅ KEEP | 工程伦理 anchor; 出现于 5 track 全部 |
| 反过早分布式 / 单机复兴 (big data is dead) | 01,02,03,04,06 | Tigani / Hannes / Wes McKinney (3) | cross-track | ✅✅✅ KEEP | 工程伦理 anchor; 与 Spark 阵营张力 |
| 数据工程 = 软件工程 (不是 report monkey) | 01,03,04,06 | Maxime / Reis / Handy / Schrock (4) | cross-track | ✅✅✅ KEEP | 角色伦理 anchor (Rise/Downfall) |
| 批与流是同一计算模型两端 (统一抽象) | 01,03,04,06 | Kreps / Akidau / Jark Wu / Zaharia (4) | cross-track | ✅✅✅ KEEP | The Log + Dataflow + 流批一体 |
| schema 是 API + 数据契约 + shift-left | 01,03,04,06 | Sanderson / Moses / DDIA (3) | cross-track | ✅✅✅ KEEP | 工程伦理 anchor; vs 末端 observability |
| lakehouse + 存算分离 + 开放表格式 | 01,02,03,04 | Blue / Chandar / Zaharia / Hannes (4) | cross-track | ✅✅✅ KEEP | 架构范式; Iceberg/Delta/Hudi |
| 生命周期 + 6 暗流框架 | 01,04 | Reis / Housley (2) | structural | ✅✅⚠️ KEEP (放大版) | 顶层骨架; 排他性 PARTIAL → 作组织框架 |
| 数据建模面向消费 (维度/OBT) 非面向事务 | 01,03,04,06 | Kimball / Inmon / Handy (3) | cross-track | ✅✅⚠️ | 可降级 playbook (建模选择是规则) |
| 数据平台是 garbage-in-garbage-out 放大器 | 02,03,06 | Moses / GX (2-3) | cross-track | ✅✅⚠️ | 并入「质量/契约」心智模型 |
| 可组合数据系统 (Arrow / 开放标准) | 01,02 | Wes / Hannes / Blue (3) | partial | ✅⚠️❌ | 并入 lakehouse/单机模型, 不单列 |
| ELT (转换推到仓内) | 03,04,06 | Handy / dbt (2) | heuristic | ✅✅❌ | → playbook (是决策规则非心智模型) |
| 成本是一等可观测指标 (FinOps) | 02,03 | BigQuery / Tigani (2) | heuristic | ✅✅❌ | → playbook + 反模式 |
| data mesh / 去中心化域所有权 | 01,04,06 | Zhamak (1-2) | school | ✅⚠️⚠️ | → 智识谱系一极 (单 figure, 渐进 anchor) |
| 编排: 资产 vs 任务 (software-defined assets) | 01,02,03 | Schrock / Maxime (2) | school | ✅✅❌ | → 智识谱系 + workflow 资深路径 |
| 越实时越好是误区 (批 vs 流按 SLA) | 01,02,03,04 | Akidau / Kreps / Tigani (3) | heuristic | ✅✅⚠️ | 并入「批流统一」心智模型局限 + playbook |

## 候选 playbook 规则 (target 10-20)

| Pattern | 来源 |
|---------|------|
| 上分布式前先量化数据规模 (单机→单仓→联邦→分布式) | T02-S020 / T02-S016 / T03-S032 |
| 任务/写入必须对分区幂等 (merge/upsert 覆盖非追加) | T03-S006 / T03-S007 / T04-S007 |
| 数据流向 BI/ML/决策必须有 test 门禁 + 源端契约 | T03-S003 / T03-S021 / T02-S045 |
| 摄取 build-vs-buy: commodity 源买 Fivetran/dlt, 不自建通用框架 | T02-S035 / T02-S036 / T03-S012 |
| SQL 能表达的转换默认 dbt, 非 SQL 重逻辑才 Spark/Polars | T02-S003 / T02-S005 / T03-S005 |
| 账单异常查四元凶 (SELECT */全量重算/小文件/缺分区裁剪) | T03-S026 / T02-S032 / T02-S005 |
| 不是亚秒需求 (风控/推荐/监控) 则批足够, 不上流 | T03-S019 / T02-S026 / T01-S029 |
| 流/微批写必须配 compaction 治小文件 | T03-S014 / T02-S014 / T03-S016 |
| 表格式选型看引擎兼容+可迁移, 不站队营销 | T02-S010 / T02-S011 / T03-S034 |
| 数据管道当软件: dev/staging/prod + PR CI 门禁 | T03-S024 / T03-S025 / T03-S035 |
| 维度建模面向消费, 不照搬源库规范化给 BI | T03-S001 / T04-S003 / T03-S029 |
| schema 只增不删 (向后兼容演进) | T03-S015 / T04-S001 / T06-S008 |

## 候选工具流派分裂 (智识谱系)

| Split | A 派代表 | B 派代表 |
|-------|---------|---------|
| 建模范式 | Kimball 维度 | Inmon 规范化 CIF / Data Vault / OBT 大宽表 |
| 大数据 vs 小数据 | Zaharia/Kreps 分布式 | Tigani/Hannes 单机复兴 |
| 数据质量 | Sanderson shift-left 契约 | Moses 末端 observability |
| 数据架构 | Zhamak data mesh 去中心化 | 中心化数仓/中国数据中台 |
| 编排 | Schrock Dagster 资产 | Airflow 任务/DAG |
| 批流架构 | Marz Lambda 双链路 | Kreps Kappa 单流 / Akidau 统一 |
| 表格式 | Blue Iceberg | Zaharia Delta / Chandar Hudi |

## 候选反模式

| Anti-pattern | 来源 |
|--------------|------|
| 过早分布式 / 为简历上 Spark | T06-S017 / T04-S018 |
| 无质量测试就上生产 = data swamp | T02-S045 / T02-S049 / T06-S022 |
| 改 schema 不通知 = 破坏数据契约 | T06-S008 / T03-S021 |
| 非幂等任务 + 回填 = 数据翻倍 | T03-S006 / T04-S007 |
| data engineer 当 report monkey | T04-S008 / T06-S012 |
| 把所有数据倒进湖不治理 | T06-S022 / T02-S049 |
| 成本失控 (SELECT */全量重算/集群常开) | T03-S026 / T02-S058? T02-S032 |
| PII / 隐私事后补 | T06-S023 / T06-S026 |
| 越实时越好全上流 | T06-S035 / T01-S029 |
| 表格式站队营销 / vendor lock-in | T02-S011 / T02-S061 |
| notebook 当生产管道 | T06-S014 / T02-S050 |
| Modern Data Stack 工具堆砌当架构 | T02-S005 / T01-S037 |

## 候选时效信号 (诚实边界用)

| Signal | 来源 | Decay 强度 |
|--------|------|-----------|
| 开放表格式 catalog 互通 (Iceberg REST/Polaris/XTable/UniForm) | T02-S061 / T03-S014 | high |
| DataOps CI + cost 工具 (dbt Fusion/slim CI) | T03-S024 / T03-S309 | high |
| streaming lakehouse (Paimon/Fluss/Dynamic Tables) | T01-S029 / T02-S042 | high |
| dbt + Fivetran 合并后生态 | T01-S011 / T01-S012 | high |
| Iceberg v3 (row lineage/deletion vectors) merge-on-read | T01-S023 / T03-S030 | medium |
| 单机引擎 (DuckDB/Polars/DuckLake) 生态 | T01-S046 / T02-S016 | high |

## 候选 Agentic Protocol 维度

| 维度 | 推导自哪个 mental model |
|------|------------------------|
| 数据规模与引擎匹配 | 反过早分布式 |
| 摄取与 build-vs-buy | 数据工程=软件工程 + 成本 |
| 建模范式与消费模式 | 面向消费建模 + 软件工程 |
| 批流边界判定 | 批流统一 (按 SLA) |
| 表格式与 lakehouse 选型 | lakehouse + 开放表格式 |
| 数据质量与契约 | schema 是 API + shift-left |
| 成本与治理 | FinOps + 反模式 |

## 候选数自检
- 候选心智模型 15 (≥15 technical floor) ✅
- candidate > 30? 否 (15) — 已合并同类项 (可组合并入 lakehouse/单机; ELT/成本/建模降 playbook; mesh/资产/编排降谱系)。
- 三重通过 (✅✅✅) = 6 个 → Section 1 心智模型主体; +1 放大版 (生命周期框架) = 7。
