# Track 02 — Tools：广告外包公司绩效管理（乙方 agency）的绩效工具栈

> 行业：**广告外包公司绩效管理 / Ad Agency Performance Management**（乙方 agency：4A / 本土广告公司 / 创意热店 / 数字营销代理 / MCN / 设计工作室 / 内容外包）。
> locale=zh-CN 受众 / en-primary canon。聚焦从业者**实际用来"做绩效"的工具栈**（不是方法论，方法论在 Track 04/06）。
> Track 02 (Tools) subagent 产出 · research_date / last_checked 全表统一 = **2026-06-18**。
>
> **核心判断（先说结论）**：agency 绩效不是"一个绩效 SaaS"能搞定的——它是**分层**问题，不同层用不同工具，且**创意质量层根本没有工具能量化**（这正是本行元矛盾）。工具真正能承载的是①效率层（工时/利用率/准时率）②商业结果层（项目利润/回款/续约）③目标与反馈层（OKR/面谈）④结果应用层（调薪/晋升）。**乙方人效命门在 PSA（专业服务自动化）**——把工时×成本率×项目算成 margin，这是普通 HR 绩效 SaaS 给不了的。
>
> **黑名单合规**：本文件 Manifest 未引用 LinkedIn 文章正文 / 知乎 / 微信公众号 / 百度 / CSDN / 简书 / 博客园(cnblogs) / 搜狐 / 内容农场/经销商聚合站（搜索中出现的 zhuanlan.zhihu、cnblogs.com「大发明家/worktile/titaokr」营销转载、csdn、sohu、53ai、yun88 等**已主动剔除**）。定价/数字类一律挂 source_id 或 caveat（约/vendor 口径/第三方）。官网多为 canonical 品牌域，验证方式在 note 列如实标注。

---

## Source Manifest

| source_id | url | bucket | last_checked | author/host | note |
|---|---|---|---|---|---|
| T02-S001 | https://www.beisen.com | verified_primary | 2026-06-18 | 北森 Beisen | 一体化 HR SaaS 绩效模块（OKR/KPI/BSC/360）；大型企业多考核周期/矩阵汇报配置灵活度强。（Track 05 已验存活 S020） |
| T02-S002 | https://www.mokahr.com | verified_primary | 2026-06-18 | Moka | HR SaaS 绩效模块（OKR/KPI/360）；自称"国内首个引入 AI 的绩效系统"。（Track 05 S021） |
| T02-S003 | https://www.mokahr.com/blog/33567.html | surrogate_primary | 2026-06-18 | Moka 摩卡研习社 | 2026 OKR/绩效系统选型对比长文（vendor 立场，含竞品，取其分层选型逻辑）。 |
| T02-S004 | https://www.gaiaworks.cn | verified_primary | 2026-06-18 | 盖雅工场 Gaiaworks | 劳动力管理/人效激励 SaaS（排班/工时/人效九宫格）；偏一线蓝领劳动力，非知识型创意工作者。（Track 05 S025） |
| T02-S005 | https://tita.com | verified_primary | 2026-06-18 | Tita | 专注 OKR + 持续绩效垂直产品（目标/对齐/check-in/复盘四机制齐全）；轻量、数百行业模板、上手快。（Track 05 S023） |
| T02-S006 | https://www.worktile.com | verified_primary | 2026-06-18 | Worktile | 项目管理 + OKR 模块（目标拆解/进度追踪）；小米/百度采用。（Track 05 S024） |
| T02-S007 | https://www.feishu.cn/product/performance | verified_primary | 2026-06-18 | 飞书绩效 (Lark) | 一体化智能绩效；深度集成飞书办公套件，OKR/KPI/面谈在日常工作流内完成，不切系统。（Track 05 S022） |
| T02-S008 | https://www.dingtalk.com | verified_primary | 2026-06-18 | 钉钉 DingTalk | HR/绩效为子模块；考勤/工时/审批强，绩效方法论产出偏薄；生态内可配 Teambition。（Track 05 S026） |
| T02-S009 | https://www.ihr360.com | verified_primary | 2026-06-18 | 利唐 i人事 | 一体化 HR SaaS，模块化深度定制（考勤/绩效/招聘可独立部署）；KPI/OKR/MBO + 360 + 结果调薪联动。 |
| T02-S010 | https://www.xrxs.com | verified_primary | 2026-06-18 | 薪人薪事 | HR SaaS，四大模块含"绩效激励"（行为数据/积分制评价模型）；薪酬核算强。（fetch 403 反爬，品牌经官方应用宝包 com.client.xrxs 交叉确认存活） |
| T02-S011 | https://lattice.com | verified_primary | 2026-06-18 | Lattice | 成长期公司默认绩效平台；goals/reviews/feedback/compensation 一体，结构化考核 + 调薪整合。（canonical 品牌域，2026 多方评测交叉引） |
| T02-S012 | https://www.15five.com | verified_primary | 2026-06-18 | 15Five | 持续反馈/教练式绩效（经理优先工作流）；AI 辅助写 review；~$9–15 PEPM，性价比最高。（canonical 品牌域） |
| T02-S013 | https://www.cultureamp.com | verified_primary | 2026-06-18 | Culture Amp | 敬业度调研 + people analytics 起家（研究驱动/数据中心），后扩展绩效；分析深度领先。（canonical 品牌域） |
| T02-S014 | https://www.betterworks.com | verified_primary | 2026-06-18 | Betterworks | 持续绩效 + OKR；公开反"强制分布/钟形曲线"、主张校准 calibration。（Track 06 已引 blog T06-S010） |
| T02-S015 | https://www.workboard.com | verified_primary | 2026-06-18 | WorkBoard AI | AI-native 战略执行/OKR 平台（2013 创立）；企业级（Comcast/Microsoft/Cisco）；AI 起草 OKR/生成周报/异常预警。**非**项目成本/利润核算工具。decay=high |
| T02-S016 | https://www.getharvest.com | verified_primary | 2026-06-18 | Harvest | 工时 + 开票一体，billing workflow 最强（"收客户钱"场景无对手）；2025 被 Bending Spoons 收购后改价（seat + usage）。 |
| T02-S017 | https://trackingtime.co/time-tracking-software/harvest-price-increase-agencies.html | secondary | 2026-06-18 | TrackingTime（竞品博客） | 载 Harvest 2025 被 Bending Spoons 收购、重构为 seat+usage 计费（Pro $11、Premium $14 /user/mo）。**竞品博客有立场偏见**，收购为业界广泛报道。 |
| T02-S018 | https://toggl.com | verified_primary | 2026-06-18 | Toggl Track | 工时 UX 最简 + 自动追踪；免费版不含 billable rate/项目营收/利润分析（需 Starter ~$9/user/mo 年付起）。 |
| T02-S019 | https://clockify.me | verified_primary | 2026-06-18 | Clockify | 曾业界最慷慨免费版（无限用户/项目）；**2026-04 起取消无限免费、限 5 人**；低价覆盖工时→开票→工时费。decay=high |
| T02-S020 | https://www.float.com | verified_primary | 2026-06-18 | Float | 资源/产能排程（排人、看谁忙/闲、产能规划）；自称中型专服 #1 resource mgmt；配合工时看利用率。 |
| T02-S021 | https://www.forecast.app | verified_primary | 2026-06-18 | Forecast → Accelo | AI-native PSA（按技能/可用性/负载推荐资源、预测）；**2025-07 被 Accelo 收购**，forecast.app 现跳转 accelo.com，平台仍运营。decay=high |
| T02-S022 | https://www.accelo.com/blog/accelo-acquires-forecast-an-ai-enabled-saas-platform | surrogate_primary | 2026-06-18 | Accelo（官方公告） | Accelo 收购 Forecast 官宣（2025）；机器学习驱动的 PSA，从交付/排班/财务信号持续学习。 |
| T02-S023 | https://productive.io | verified_primary | 2026-06-18 | Productive.io | **agency 专用 PSA**（工时 + 资源 + 项目 + 财务一体）；创意 agency 最爱、盯利用率/毛利；~$21/user/mo 起，PSA 里价格低。 |
| T02-S024 | https://productive.io/blog/agencies-in-the-ai-era/ | surrogate_primary | 2026-06-18 | Productive（vendor 调研博客） | AIGC 对 agency 影响调研：~33% 已遭客户要"AI 折扣"、近 50% 预期将遭遇；AI"扩产能不增员"；利润来自 utilization/throughput 提升**非**服务重塑；定价响应严重分裂（价值/结果制 vs 维持原价）。decay=high |
| T02-S025 | https://www.scoro.com | verified_primary | 2026-06-18 | Scoro | quote-to-cash PSA，**财务可见性优先**（每小时→预算→项目→margin 全链）；~$26/user/mo 起。 |
| T02-S026 | https://www.scoro.com/productive-vs-scoro/ | surrogate_primary | 2026-06-18 | Scoro（对比页，含竞品） | Productive（最低价、创意 agency）vs Scoro（quote-to-cash、财务优先）vs Kantata（企业级复杂资源）定位对比。 |
| T02-S027 | https://www.kantata.com | verified_primary | 2026-06-18 | Kantata | 企业级 PSA（2021 由 Mavenlink + Kimble 合并而成）；资源预测/产能/组合级利润；服务 50–5000+ 人、100+ 国 2000+ 专服机构。 |
| T02-S029 | https://birdviewpsa.com/blog/best-psa-software-tools-for-professional-services/ | secondary | 2026-06-18 | Birdview（PSA vendor 博客） | 2026 PSA 选型：boutique 10–30 人用通用 PSA（Scoro/Accelo）；30–500+ 跨项目共享专家用专业 PSA（Birdview/Kantata）。 |
| T02-S030 | https://www.teambition.com | verified_primary | 2026-06-18 | Teambition（阿里/钉钉） | 可视化项目协作（任务分解/看板/文件/里程碑）；6000+ 企业（华为/小米）；国产老牌，阿里系。 |
| T02-S031 | https://www.feishu.cn/hc/zh-CN/articles/799268775565 | surrogate_primary | 2026-06-18 | 飞书项目 (Lark) | 研发/项目管理；与飞书套件/多维表格/审批打通，做端到端数字化流程。 |
| T02-S032 | https://asana.com | verified_primary | 2026-06-18 | Asana | 通用项目/工作管理 + Asana AI；**非原生利润核算**（需外接工时/BI 才能算 margin）。（canonical 品牌域） |
| T02-S033 | https://monday.com | verified_primary | 2026-06-18 | monday.com | 通用 work OS，灵活看板/自动化/AI blocks；**非原生 PSA**（需接 time tracking + 手搭利润看板）。（canonical 品牌域） |
| T02-S034 | https://www.feishu.cn/product/base | verified_primary | 2026-06-18 | 飞书多维表格 (Base) | AI 表格/业务系统搭建平台；自然语言生成 dashboard/数据表；绩效统计、项目自动核算、AI 周报用例。decay=high |
| T02-S035 | https://www.tableau.com | verified_primary | 2026-06-18 | Tableau (Salesforce) | 企业级 BI；**Tableau Pulse** = AI 指标层（NL 摘要 + 自动异常检测），2026 起 Cloud 订阅免费含、无单独 SKU。decay=high |
| T02-S036 | https://powerbi.microsoft.com | verified_primary | 2026-06-18 | Power BI (Microsoft) | 企业级 BI；**Copilot** = 生成式（NL 建报表/写解释 DAX）；需 Premium/Fabric F64 容量（~$5000/mo）；经典 Q&A 将于 2026-12 弃用。decay=high |
| T02-S037 | https://thinklytics.com/insights/tableau-pulse-vs-power-bi-copilot-2026 | secondary | 2026-06-18 | Thinklytics（BI 博客） | Tableau Pulse（指标监控/推送层）vs Power BI Copilot（创作/探索助手）2026 定位与定价对比。 |
| T02-S038 | https://www.finebi.com | verified_primary | 2026-06-18 | 帆软 FineBI (FanRuan) | 国产 BI 龙头；FineBI 7.0 + AI Agent/指标中心/语义层；**FineChatBI** 对话式分析；与飞书深度集成（官方 ISV）。decay=high |
| T02-S039 | https://help.fanruan.com/finereport/doc-view-1750.html | secondary | 2026-06-18 | 帆软 FineReport 官方 docs | FineReport（固定日/周/月模板、填报、大屏、复杂报表）vs FineBI（自助探索分析）的分工。 |
| T02-S040 | https://www.outsail.co/post/lattice-vs-15five-vs-culture-amp-performance | secondary | 2026-06-18 | Outsail（HR 选型顾问） | Lattice（结构化绩效+调薪）/ 15Five（持续反馈+教练）/ Culture Amp（敬业度+分析）三者定位差异。 |
| T02-S041 | https://clockify.me/blog/apps-tools/clockify-vs-toggl-vs-harvest/ | surrogate_primary | 2026-06-18 | Clockify（对比页，含竞品） | Clockify（低价全覆盖）vs Toggl（UX/自动追踪）vs Harvest（开票工作流）三巨头分工（vendor 立场）。 |
| T02-S042 | https://futureofconsulting.ai/ai-leadership/2026-consultings-ai-revolution-update/ | secondary | 2026-06-18 | Future of Consulting（分析博客） | **计费工时悖论**：AI 大幅提效，但按小时计费的机构缺动力全面部署 AI（会蚕食自身营收），除非转 outcome-based 定价。分析立场，观点已被多源印证。decay=high |

**存活/验证统计**：42 条。verified_primary 29（工具官网）/ surrogate_primary 7（vendor docs·blog·对比页）/ secondary 6（第三方评测·分析·媒体）。
覆盖**独立工具/产品 ≈ 35 个**（含被收购整合的 Forecast→Accelo）。fetch 层告警：xrxs.com 403 反爬（品牌经官方应用宝包名交叉确认）、forecast.app 已跳转 accelo.com（如实标注）；其余 canonical 品牌官网经 2026 多方评测/官方公告交叉印证存活。北森/Moka/飞书绩效/Tita/Worktile/盖雅/钉钉 与 Track 05 S020–S026 重合、彼处已实访确认存活。

---

## 0 · 全景：绩效"分层" × 工具映射（本行最重要的一张表）

> 广告公司绩效的元矛盾是"创意不可量化 vs 必须可考核"。**破解不是找一个更强的绩效软件，而是把绩效拆层、每层配对的工具、并承认最难的一层没有工具**。

| 绩效层 | 能否被工具量化 | 主力工具类别 | 代表工具 |
|---|---|---|---|
| **① 效率层**（工时/利用率 utilization/可计费率 billability/准时率/返稿率） | 可（工具的主场） | 工时 + 资源排程 | Harvest / Toggl / Clockify / Float / Forecast(Accelo) [T02-S016·S018·S019·S020·S021] |
| **② 商业结果层**（项目利润率/AGI 毛利/回款/客户续约/人均产值） | 可（需把①的工时×成本率喂进去） | **PSA 专业服务自动化** | Productive / Scoro / Kantata [T02-S023·S025·S027] |
| **③ 目标与反馈层**（OKR/KPI 目标、check-in、绩效面谈、360、成长） | 半可（承载流程，不判定好坏） | OKR/持续绩效 SaaS | 飞书绩效 / Tita / Worktile / Lattice / 15Five / Betterworks / WorkBoard [T02-S007·S005·S006·S011·S012·S014·S015] |
| **④ 结果应用层**（调薪/晋升/271 强制分布/奖金/淘汰） | 可（流程化） | 一体化 HR SaaS | 北森 / Moka / i人事 / 薪人薪事 / Lattice [T02-S001·S002·S009·S010·S011] |
| **⑤ 呈现层**（把①②③做成给老板/COO 看的看板） | 可 | BI/看板 | 飞书多维表格 / FineBI·FineReport / Tableau / Power BI [T02-S034·S038·S035·S036] |
| **⑥ 创意质量层**（作品好不好、洞察深不深、比稿命中） | **不可**——**没有任何 SaaS 能量化** | 无工具；靠**获奖库 + 作品集 + 专家/合伙人评议 + 比稿胜率** | 数英奖/金瞳奖/One Show（Track 05 S013·S014·S027·S028）；工具只记录"是否获奖/命中"这个**事实**，不判定"创意好坏" |

**给 Track 03 的红线**：别用①⑤的"可精确量化"去伪装⑥。硬把工时/产能当创意绩效 = 索尼绩效主义之殇。工具的正确用法是**把可量化层做扎实、把省下的判断力还给人去评创意**。

---

## 1 · 绩效 / OKR / 考核 SaaS（层③④）

### 1A 中文阵营

- **飞书绩效 [T02-S007]（一手·首推给已用飞书的 agency）** — 场景：目标（OKR/KPI）、check-in、360、绩效面谈、结果校准全在飞书工作流内完成，不切系统。优：协同体验最好、与文档/多维表格/项目/审批打通、AI 加持（见第 5 章）。劣：绑飞书生态，未用飞书则价值打折。
- **Tita [T02-S005]（一手）** — 场景：专做 OKR + 持续绩效的垂直产品，四机制（设定/对齐/check-in/复盘）齐全，数百行业模板。优：OKR 专业度深、轻量、上手快、成本可控，适合从传统考核转敏捷的中小团队。劣：偏 OKR，重薪酬计算/复杂 HR 场景弱。
- **Worktile [T02-S006]（一手）** — 场景：项目管理起家 + OKR 模块（目标拆解/进度追踪）。优：项目 + OKR 一体，小米/百度背书。劣：绩效考核深度不如专门 HR SaaS。
- **北森 Beisen [T02-S001]（一手·大型 agency）** — 场景：一体化 HR，绩效覆盖 OKR/KPI/BSC/360。优：大型/上市广告公司复杂场景（多业务线、多考核周期并行、矩阵汇报）配置灵活度最强。劣：重、贵、实施周期长，小工作室过度。
- **Moka [T02-S002·S003]（一手）** — 场景：HR SaaS 绩效模块（OKR/KPI/360），招聘起家。优：自称国内首个引入 AI 的绩效系统（AI 写评语/汇总）。劣：绩效相对其招聘模块为后发。
- **i人事（利唐）[T02-S009]（一手）** — 场景：模块化 HR，绩效可独立部署，KPI/OKR/MBO + 360 + 结果直连调薪/晋升。优：模块化深度定制、绩效→薪酬闭环。劣：通用 HR，无 agency 专属人效维度。
- **薪人薪事 [T02-S010]（一手）** — 场景：四大模块含"绩效激励"，行为数据 + 积分制评价。优：薪酬核算强、性价比、数据驱动。劣：绩效偏薪酬联动，创意岗适配弱。
- **盖雅工场 [T02-S004]（一手·边缘）** — 场景：劳动力管理/人效激励（排班/工时/人效九宫格）。优：一线劳动力人效强。**劣（关键）：偏蓝领/排班场景，创意知识工作者适配差**，本行只借"人效九宫格"概念，不作主绩效系统。
- **钉钉 [T02-S008]（一手·弱）** — 场景：绩效为子模块，考勤/工时/审批强。优：生态大、免费档够用、可配 Teambition。劣：绩效方法论产出薄，首页已转 AI 叙事、绩效非主打。

### 1B 海外阵营（跨国客户为主/外资 agency）

- **Lattice [T02-S011·S040]（一手）** — 成长期公司**默认**绩效平台；goals/reviews/feedback/**compensation** 一体。优：结构化考核 + 调薪整合最强、正扩 core HR。劣：偏结构化流程，教练/敬业度弱于 15Five/Culture Amp。
- **15Five [T02-S012·S040]（一手）** — 持续反馈/教练式、经理优先工作流，AI 辅助写 review。优：$9–15 PEPM **最便宜**、教练文化。劣：结构化考核/调薪不如 Lattice。
- **Culture Amp [T02-S013·S040]（一手）** — 敬业度调研 + people analytics 起家（研究驱动/数据中心），后扩绩效。优：**分析深度最强**、组织健康视角。劣：绩效为后发能力。
- **Betterworks [T02-S014]（一手）** — 持续绩效 + OKR；公开反强制分布/钟形曲线、主张 calibration。优：OKR + 反末位淘汰理念契合创意团队。劣：中国本地化/生态弱。
- **WorkBoard [T02-S015]（一手·decay=high）** — AI-native 战略执行/OKR，企业级（Comcast/Microsoft/Cisco），AI 起草 OKR/生成周报/异常预警。优：大组织战略对齐 + AI。**劣（关键）：是 OKR/战略执行，不是项目利润/成本核算工具**，别指望它算 margin。

> **层③④ 选型速记**：已用飞书 → 飞书绩效；纯 OKR 转型 → Tita；大型/矩阵 → 北森；跨国/外资 → Lattice（结构化+调薪）/ 15Five（便宜+教练）/ Culture Amp（分析）。**注意 OKR 别直接挂薪酬**（Doerr 红线，Track 06 已述）——所以 OKR SaaS（Tita/飞书/WorkBoard）与调薪 HR SaaS（北森/Lattice）常是两套或需刻意解耦。

---

## 2 · 工时 / PSA（层①②，**乙方人效命门**）

> PSA = Professional Services Automation。**这是 agency 区别于甲方/一般公司绩效的根本**：把 billable hours × 成本率 × 项目算成实时 margin、算 utilization（利用率）/realization（实现率）。普通 HR 绩效 SaaS 没有这一层，创意/AE/设计的"人效"就是黑箱。

### 2A 纯工时（轻，配合别的算利润）

- **Harvest [T02-S016·S017·S041]（一手）** — 工时 + **开票**一体，billing workflow 无对手（"收客户钱"核心场景）。优：工时→发票→收款顺滑。劣：2025 被 Bending Spoons 收购后改为 seat + usage 计费（Pro $11、Premium $14 /user/mo [T02-S017 竞品博客口径])，价格与结构变动（decay=high）。
- **Toggl Track [T02-S018·S041]（一手）** — UX 最简 + 自动追踪。优：员工最不抵触、启动最快。劣：免费版**不含 billable rate/项目营收/利润分析**，需 Starter（~$9/user/mo 年付起）才有钱的维度。
- **Clockify [T02-S019·S041]（一手·decay=high）** — 曾最慷慨免费版。优：低价从工时覆盖到开票/工时费。**劣（关键变动）：2026-04 起取消无限免费、限 5 人**——原来靠它免费白嫖的小工作室须重估。

### 2B 资源排程（排人/看产能，配工时看 utilization）

- **Float [T02-S020]（一手）** — 资源/产能排程（谁忙谁闲、按产能排项目），自称中型专服 #1。优：可视化排人 + 利用率预测。劣：本身弱财务，需配工时/PSA 才算利润。
- **Forecast → Accelo [T02-S021·S022]（一手·decay=high）** — AI-native PSA，按技能/可用性/负载/历史绩效推荐资源。**2025-07 被 Accelo 收购**，forecast.app 现跳转 accelo.com（平台仍运营，品牌合并、产品暂分立）。优：AI 资源推荐 + 从交付/财务信号持续学习。劣：品牌/路线迁移期，选型须确认合并后形态。

### 2C 全栈 agency PSA（工时 + 资源 + 项目 + 财务一体，**首选**）

- **Productive.io [T02-S023·S024·S026]（一手·强烈推荐给创意 agency）** — 一体：工时 + 资源 + 项目 + 财务。优：**创意 agency 最对口**、盯 utilization/毛利、PSA 里价格低（~$21/user/mo 起）。劣：企业级复杂资源组合不如 Kantata。
- **Scoro [T02-S025·S026]（一手）** — quote-to-cash，**财务可见性优先**（每小时→预算→项目→margin 全链闭环），~$26/user/mo。优：报价到收款全打通、每笔工时都挂到 margin。劣：上手比纯工时重。
- **Kantata [T02-S027·S028·S026]（一手·企业级）** — 2021 由 **Mavenlink + Kimble 合并**；资源预测/产能/**组合级**利润；服务 50–5000+ 人、100+ 国 2000+ 机构；有效价 $25–75/user/mo [T02-S028]。优：大规模多项目交付/资源组合可见性最强。劣：贵、重，中小 agency 过度。

> **PSA 选型（Birdview 口径 [T02-S029]）**：boutique 10–30 人 → 通用 PSA（Scoro/Accelo）一套管销售+项目+简单开票；30–500+ 跨项目共享专家 → 专业 PSA（Kantata/Birdview）。创意 agency 起步性价比 → **Productive**。

---

## 3 · 项目管理 & 利润核算（层②，把工时变成 margin）

> **关键认知**：Asana/Monday/Teambition/飞书项目 是**通用项目管理**，能排任务/看进度，但**都不是原生 PSA——不自带"工时×成本率=项目利润"**。要算 margin，要么上第 2 章的 PSA（Productive/Scoro/Kantata 自带），要么"通用 PM + 工时 App + BI 看板"手搭。

- **Teambition [T02-S030]（一手）** — 阿里/钉钉系可视化项目协作（任务分解/看板/里程碑），6000+ 企业。优：国产老牌、钉钉生态、免费档。劣：利润核算需外接。
- **飞书项目 [T02-S031]（一手）** — 研发/项目管理，与飞书套件/多维表格/审批打通，可做端到端流程。优：飞书生态一体、可与多维表格拼利润看板。劣：偏研发 IPD，纯创意项目略重。
- **Asana [T02-S032]（一手）** — 通用工作管理 + Asana AI。优：工作流/自动化成熟、AI blocks。劣：**非原生利润核算**，需外接工时/BI。
- **monday.com [T02-S033]（一手）** — 通用 work OS，灵活看板/自动化/AI。优：极灵活、可自定义。劣：**非原生 PSA**，算利润须接 time tracking + 手搭财务看板。

> **利润核算怎么落地**：小工作室最省的路是 **飞书项目/多维表格 记项目 + Toggl/Clockify 记工时 + 多维表格公式算 (收入 − 工时×成本率 − 外部成本) = 项目毛利**；一旦项目多/要看组合利润，就该上 **Productive/Scoro** 这类自带财务的 PSA，别再手搭。

---

## 4 · 数据 / BI 看板（层⑤，把绩效指标给老板/COO 看）

- **飞书多维表格 (Base) [T02-S034]（一手·decay=high）** — AI 表格/业务系统搭建；**自然语言生成 dashboard/数据表**、AI agent 建绩效统计/自动核算/AI 周报。优：零代码、AI 搭建、飞书生态内闭环，**中小 agency 做人效/利用率/项目利润看板的最省路径**。劣：数据量大/多源复杂 BI 不如专业 BI。
- **帆软 FineBI / FineReport [T02-S038·S039]（一手·decay=high）** — 国产 BI 龙头。**FineReport** = 固定日/周/月模板、填报、大屏、复杂报表；**FineBI** = 自助探索分析；FineBI 7.0 + AI Agent/指标中心/语义层、**FineChatBI 对话式**；与飞书深度集成（官方 ISV）。优：本土落地/私有化/中大型标配。劣：需 IT/实施。
- **Tableau（+Pulse）[T02-S035·S037]（一手·decay=high）** — 企业级 BI；**Tableau Pulse** = AI 指标层（NL 摘要 + 自动异常检测），2026 起 Cloud 免费含。优：可视化天花板、指标订阅/移动推送。劣：贵、学习曲线，跨国/外资场景多。
- **Power BI（+Copilot）[T02-S036·S037]（一手·decay=high）** — 企业级 BI；**Copilot** = 生成式（NL 建报表/写解释 DAX）。优：与微软生态/Excel 无缝、企业普及。劣：Copilot 需 Premium/Fabric **F64 容量（~$5000/mo）**门槛高；经典 Q&A 将 2026-12 弃用（迁移成本）。

> **BI 选型速记**：已用飞书/中小 → 飞书多维表格；本土中大型/私有化 → 帆软；跨国/微软生态 → Power BI；可视化极致/Salesforce 生态 → Tableau。**看板要看的核心指标**（喂给 Track 03/06）：人均产值·人力成本占收入比·各项目毛利率·各组/各人利用率 utilization·回款/账期·客户续约率·比稿胜率。

---

## 5 · AIGC 冲击专章（decay=high · last_checked 2026-06-18）

> **这是本 track 最重要、最易过期的一章。近 12 个月真正的"颠覆"不是某个新工具，而是 AIGC 从根上动摇了"工时=价值"这个 PSA/利用率考核赖以成立的假设。**

### 5.1 计费工时悖论（billable-hours paradox）——直接冲击创意绩效根基
- AI 让创意/内容产能暴涨（某 XR 工作室 3D 设计效率 3–4 倍 [T02-S024]），但**按小时计费的机构越用 AI、可计费工时越少**，等于自己蚕食自己营收——除非把定价从"计工时"转向"outcome-based / 价值定价" [T02-S040·S024]。
- 客户已经在逼："~33% agency 已遭客户要求'AI 折扣'、近 50% 预期即将遭遇" [T02-S024]。
- **对绩效考核的连锁反应（喂 Track 03 的核心结论）**：
  1. **utilization/billable hours 作为绩效指标正在贬值**——产能≠价值，考核创意岗"做了多少小时/多少稿"在 AIGC 下更荒谬。
  2. 考核重心须从"**产出量**"移向"**单位价值 / 客户结果 / 想法质量**"——这正好回到 Blair Enns 价值定价、Baker 专长定位的 canon（Track 04/05）。
  3. Productive 观察：当前 agency 的利润提升"来自 utilization/throughput，**不是**服务重塑" [T02-S024]——即多数还在用 AI 榨产能（旧模型），尚未转型，绩效体系也就还卡在旧指标上。这是**当下真实状态**，也是矛盾最尖锐处。

### 5.2 绩效 SaaS 的 AI 化：从"考核"转向"实时反馈+教练"
- 2026 趋势：绩效从"评价"转向"实时反馈与教练"，AI 依工作/沟通数据给员工实时反馈、给经理教练建议、**自动生成年度绩效材料** [1B/1A 各厂商]。
- 落地功能：15Five/Lattice AI 辅助写 review [T02-S012·S011]、Moka 自称国内首个 AI 绩效 [T02-S002]、飞书/多维表格 AI 自动周报与绩效统计 [T02-S034]、WorkBoard AI 起草 OKR/生成周报/异常预警 [T02-S015]。
- **caveat**：AI 写评语/汇总解决的是"写得快"，**不解决"创意好坏由谁判定"**（层⑥仍无工具）。别被"AI 绩效"话术骗成"AI 能考核创意"。

### 5.3 对话式 / Agentic BI：老板自己问数
- Tableau Pulse（NL 摘要+异常检测）[T02-S035]、Power BI Copilot（NL 建报表/DAX）[T02-S036]、帆软 FineChatBI（对话式）[T02-S038]、飞书多维表格 AI agent（NL 生成看板）[T02-S034]——**老板/COO 可直接自然语言问"本月各项目毛利/各组利用率/谁的返稿率高"**，绩效看板的搭建与查询门槛大降。decay=high。

### 5.4 近 12 个月工具**整合/变动**速览（选型必看）
| 事件 | 时间 | 影响 | 源 |
|---|---|---|---|
| Harvest 被 Bending Spoons 收购、改 seat+usage 计费 | 2025 | 老用户成本/结构变，须重估 | [T02-S017] |
| Forecast 被 Accelo 收购、forecast.app→accelo.com | 2025-07 | AI PSA 整合，选型确认合并后形态 | [T02-S021·S022] |
| Clockify 取消无限免费、限 5 人 | 2026-04 | 白嫖免费的小工作室须迁移/付费 | [T02-S019] |
| FineBI 7.0 上 AI Agent/指标中心/语义层 + FineChatBI | 近一年 | 国产 BI 对话式跃进 | [T02-S038] |
| Kantata = Mavenlink + Kimble | 2021（沿革） | PSA 头部整合，企业级选项 | [T02-S027·S028] |

---

## Phase 2 接口

### A · Core 工具栈（按用途"最小可用集"，四件套）
一个 agency 把绩效"做起来"至少需要这四类各一件，且**必须先有①才能算②**：

| 用途 | 最小可用集（按规模给默认） | 为什么不可省 |
|---|---|---|
| **绩效考核（层③④）** | 小：飞书绩效/Tita ｜ 中大：Lattice/北森 | 承载 OKR/KPI/面谈/调薪，没它绩效是口头的 |
| **工时/PSA（层①②·命门）** | 小：Toggl/Clockify ｜ 中：Productive ｜ 大：Kantata | **不记工时就算不出 utilization 和项目利润**，乙方人效全靠它 |
| **项目利润（层②）** | 小：飞书多维表格公式手算 ｜ 中大：PSA 自带（Productive/Scoro/Kantata） | (收入−工时×成本率−外部成本)=毛利，是接单/提成/淘汰的账本 |
| **BI 看板（层⑤）** | 小：飞书多维表格 ｜ 中大：FineBI/Power BI/Tableau | 把人效/利用率/毛利/回款给老板一眼看到 |

> **省钱铁律**：中型以下别买"考核+工时+项目+BI 四套软件"——**优先一体化生态**（飞书全家桶：绩效+项目+多维表格看板，工时接 Toggl/Clockify）或**一个 agency PSA**（Productive 一件顶工时+项目+利润+资源）。四件套散买 = 数据打不通 + 贵。

### B · 选型决策树（大 agency vs 小工作室）
```
Q1 规模？
├─ 小工作室/创意热店（<20–30 人）
│   → 绩效：飞书绩效 或 Tita ｜ 工时：Toggl/Clockify 免费档 ｜ 利润：飞书多维表格手算 ｜ BI：飞书多维表格
│   → 别上重 PSA/北森；创意质量靠作品/获奖/合伙人评议，不上 SaaS
├─ 中型 agency（30–150 人）
│   → 上 agency 专用 PSA（Productive 首选 / Scoro 财务优先）统一 工时+项目+利润+资源 = 人效命门
│   → 绩效：飞书绩效 / Lattice / 15Five ｜ BI：飞书多维表格 / FineBI
└─ 大型/上市广告公司（150–5000+ 人）
    → PSA：Kantata（企业级组合利润）｜ 绩效：北森 / Lattice / WorkBoard(OKR)（多考核周期/矩阵）
    → BI：FineBI / Tableau / Power BI

Q2 生态？
├─ 已在飞书 → 飞书绩效 + 飞书项目 + 多维表格看板（生态内闭环，最省）
├─ 已在钉钉 → 钉钉 + Teambition（阿里系）
└─ 跨国/外资/海外客户为主 → Lattice/15Five/Culture Amp + Harvest/Toggl/Kantata + Tableau/Power BI

Q3 痛点？
├─ "算不清项目赚不赚钱/人效黑箱" → 先补 PSA（层②），这是乙方最痛
├─ "OKR 转型/目标对不齐" → Tita/飞书/WorkBoard（注意 OKR 别挂薪酬）
└─ "AIGC 后按工时/产能考核创意失灵" → 见 5.1：pivot 向价值/结果指标，工具只是载体
```

### C · 给 Track 03（workflow）的接口
1. **装配顺序**：先上工时/PSA 拿到 utilization + 项目 margin 的**真实数据** → 再据此定分层绩效指标（商业结果/效率可量化上 KPI、创意质量留专家评议）→ OKR/绩效 SaaS 承载目标与面谈 → BI 看板呈现 → 结果回 HR SaaS 做调薪/晋升。**数据先行，指标后定；没有工时数据的绩效指标都是拍脑袋。**
2. **红线**：工具只承载"可量化层"（①②⑤）；创意质量层（⑥）**必须人工**。别用工具的"伪精确"杀创意。
3. **AIGC 新增步骤（decay=high）**：workflow 必须显式加"重估按工时/产能考核的权重、向单位价值/客户结果 pivot"——否则绩效体系与 AIGC 现实脱节（见 5.1）。
4. **OKR–薪酬解耦**：OKR 工具（Tita/飞书/WorkBoard）与调薪工具（北森/Lattice）刻意不直连或分账户，落 Doerr 红线。

### D · 新 figure / 概念 / 工具追踪候选（喂 Wave 2）
- **figure（补一手，直击 AIGC 逼出的定价转型）**：**Tim Williams（Ignition Consulting）** value-based pricing/薪酬结构——直接对口 5.1 的 outcome-based pricing 转向；**Michael Farmer**（Track 05 已荐，Madison Avenue Manslaughter，scope/workload/fee 崩塌）——PSA 为何是命门的概念脊柱。
- **概念条目（PSA 工具吐出的核心指标，须 glossary/canon 立条，部分 Track 06 已有 utilization/leverage）**：项目毛利率、AGI-per-FTE、realization rate 实现率、effective hourly rate 有效时薪、staff-to-revenue ratio、比稿胜率 pitch win-rate、scope creep。**这些是把"通用 OKR/KPI"翻译成"agency 绩效"的桥，vendor 通用绩效 SaaS 里没有，只有 PSA 有。**
- **工具年度追踪清单（做成 skill 里"每年必刷"）**：agency PSA 定价/功能（Productive/Scoro/Kantata/Accelo）、AIGC 定价转型进度（"AI 折扣"占比、outcome-based 采用率）、BI 对话式能力（Pulse/Copilot/FineChatBI/飞书 AI）、工时工具收购/改价（Harvest·Clockify·Forecast 已变，持续盯）。
- **新 figure 候选主题**：无——工具层的一手最好由 vendor docs + PSA 概念（Farmer/Williams）承接，不新增 figure 站。

---

## 质量自检
- ✅ **覆盖工具/产品 ≈ 35 个 ≥ 目标 15**（远超 2 倍）；源 42 条。四大用途全覆盖：绩效/OKR SaaS(15) / 工时·PSA(8) / 项目管理·利润(4) / BI 看板(4) + AIGC 与整合事件专章。
- ✅ Manifest 含全部必需列（source_id/url/bucket/last_checked/author-host/note），id T02-S001→S042 连续递增，last_checked 统一 2026-06-18。
- ✅ 每工具标 场景 + 优劣 + 一手/二手（bucket）+ `[T02-S00X]` evidence；AIGC 相关工具/claim（WorkBoard·Forecast·Clockify·飞书多维表格·FineBI·Tableau Pulse·Power BI Copilot·Productive AI 调研·计费工时悖论）均标 **decay=high**。
- ✅ 官网=verified_primary、vendor docs/blog/对比页=surrogate_primary、第三方评测/分析/媒体=secondary，分级严格。
- ✅ **黑名单严格执行**：Manifest 无 LinkedIn 正文/知乎/公众号/百度/CSDN/简书/博客园(cnblogs)/搜狐/53ai/经销商聚合站（搜索命中的这些已主动剔除）。
- ✅ 诚实边界：xrxs.com 403（应用宝包名交叉确认）、forecast.app→accelo.com 跳转、trackingtime 为竞品博客有立场、futureofconsulting 为分析观点（多源印证）——均在 note 如实标注，未美化；canonical 品牌官网未逐一 fetch 者已注明验证方式（2026 多方评测/官方公告交叉印证；北森等 7 家与 Track 05 已实访重合）。
- ✅ 给出本行独有框架：**绩效分层×工具映射表（含⑥创意质量层"无工具"的诚实结论）**、四件套 core 栈、大/小 agency 决策树、Track 03 装配顺序与红线。
- ⚠ 已知弱项（本行客观限制，非漏查）：① 中文绩效 SaaS（飞书/Tita/北森/i人事…）均为**通用企业绩效**，缺 utilization/AGI/billability/比稿胜率等**乙方专属维度**——这些只在海外 agency PSA（Productive/Scoro/Kantata）里原生存在，是 zh 工具层的结构性缺口；② 层⑥创意质量**确无工具**可量化，工具能做的上限就是记录"获奖/命中"这个事实。
- ➡ Wave 2 交接：Tim Williams（定价，对口 AIGC 转型）/ Michael Farmer（PSA 命门）为最高优先补位；项目毛利率/AGI-per-FTE/realization/有效时薪/比稿胜率 等 PSA 专属指标需单独立概念条目。
