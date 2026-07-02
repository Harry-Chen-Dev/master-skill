# Track 03 — Workflows：广告外包公司绩效管理（乙方 agency）的完整工作流 / SOP

> 行业：**广告外包公司绩效管理 / Ad Agency Performance Management**（乙方 agency：4A / 本土广告公司 / 创意热店 / 数字营销代理 / MCN / 设计工作室 / 内容外包）。
> locale=zh-CN 受众 / en-primary canon。视角：**从业者（老板 / COO / HR / 项目总监 / team lead）在乙方内部"做绩效"的动作序列**——不是方法论清单（在 Track 04/06），也不是工具清单（在 Track 02），而是**按阶段的 SOP：先做什么、再做什么、哪步能跳、哪步是坑**。
> Track 03 (Workflows) subagent 产出。**本次为重跑**（上次未落盘）。
>
> **核心判断（先说结论）**：agency 绩效不是"套一个模板"，而是**一条有先后依赖的装配线**——① 先有定位/定价（决定有没有利润可分）→ ② 再上工时/PSA 拿到 utilization+项目 margin 的**真实数据**（没数据的指标都是拍脑袋）→ ③ 据数据分层设岗位指标（结果/效率可量化上 KPI，创意质量留专家评议）→ ④ 目标共识+过程辅导+自评+校准+面谈 → ⑤ 结果应用（调薪/晋升/PIP）→ ⑥ 复盘迭代 + 反 Goodhart。**装反顺序（先定 KPI 再补数据、先考核再定价）是本行最常见的失败模式。**
>
> **黑名单合规**：本文件 Manifest **未**引用 LinkedIn 文章正文 / 知乎 / 微信公众号 / 百度 / CSDN / 简书 / 脉脉 / g2 / capterra 评论站 / HR 内容农场。研究 华为奖金包 时搜索命中的 zhuanlan.zhihu / 360doc / keycourse / 腾讯新闻 转载**已主动剔除**，改用 对标考察网 + MBA智库 + 《以奋斗者为本》书页（与 Track 01/04/06 同一批 clean 源）。数字类（utilization 目标 / 人力成本占比 / 提成 / 流失率 / 账期 / 奖金池占比）一律挂 source_id 或 caveat（约/vendor 口径/行业经验/倡导方口径）。
> **last_checked 约定**：`2026-06-18` = 从 Track 01/02/04/06 已验证 manifest **继承**（本次未重新 fetch）；`2026-07-02` = 本次 Track 03 **亲自 WebSearch/WebFetch 验证/取用**。

---

## Source Manifest

| source_id | url | bucket | last_checked | author/host | note |
|---|---|---|---|---|---|
| T03-S001 | https://davidmaister.com/books.mtpsf/ | verified_primary | 2026-06-18 | David Maister | 《Managing the PSF》PSF 圣经：利润/合伙人 = Leverage×Utilization×Billing×Realization×Margin（LUBRM）；欠授权吃 40-50% 产能；utilization=短期 hygiene 别当目标榨。继承 T01/T04/T06。 |
| T03-S002 | https://davidmaister.com/articles/results-and-rewards-in-the-multi-group-firm/ | verified_primary | 2026-07-02 | David Maister | 多组织/多利润中心奖酬：多数好公司**避免短期公式化分配**，用 3-5 年"判断式"让组回报≈组利润——直击"项目分成 vs 协作"矛盾。本次 WebSearch 确认存活（站点反爬 fetch，取 snippet）。 |
| T03-S003 | https://punctuation.com/benchmark-unburdened-compensation-load/ | verified_primary | 2026-06-18 | David C. Baker / Punctuation | agency 财务基准：未负担薪酬 ≤45% AGI、AGI/FTE≈$90K、整体 utilization 目标 ~60%、营业利润 ≥15%（美国口径 caveat）。继承 T06。 |
| T03-S004 | https://www.winwithoutpitching.com/books/the-win-without-pitching-manifesto | verified_primary | 2026-06-18 | Blair Enns | 拒绝免费比稿 + 靠定位换定价权（定价决定内部有没有 margin 可考核）。继承 T04/T06。 |
| T03-S005 | https://www.winwithoutpitching.com/business-development-compensation-plans/ | verified_primary | 2026-07-02 | Blair Enns | 「BD 薪酬 5 步」：BD 目标**质量优先于数量**→定目标薪酬→与绩效对齐→浮动激励上限**约 +20-25%**（多数人要收入安全、雇主要绩效稳定）。姊妹页 /how-much-to-pay/ 同源。本次 WebSearch 确认。 |
| T03-S006 | https://www.whatmatters.com/faqs/okr-meaning-definition-example | verified_primary | 2026-06-18 | John Doerr / What Matters | OKR「I will (O) as measured by (KR)」+ CFR（对话/反馈/认可）+ 铁律 OKR 与薪酬脱钩。继承 T04/T06。 |
| T03-S007 | https://hbr.org/2005/07/the-balanced-scorecard-measures-that-drive-performance | verified_primary | 2026-06-18 | Kaplan & Norton / HBR | 平衡计分卡四视角（财务/客户/内部流程/学习成长）+ 战略地图（战略→指标的拆解母体）。继承 T04/T06。 |
| T03-S008 | https://global.kyocera.com/inamori/management/amoeba/ | verified_primary | 2026-06-18 | 稻盛和夫 / 京瓷官方 | 阿米巴：5-50 人独立核算单元；单位时间核算=(销售−费用)÷总工时——工作室/项目组独立核算母体。继承 T04/T06。 |
| T03-S009 | https://deming.org/deming-on-management-performance-appraisal/ | verified_primary | 2026-06-18 | W. Edwards Deming Institute | 废除年度考评（"七大恶疾"之一）；94% 变异=系统非个人；考评"滋养短期、扼杀长期、制造恐惧、摧毁协作"。反强制分布最强论据。继承 T04。 |
| T03-S010 | https://www.danpink.com/books/drive/ | verified_primary | 2026-06-18 | Daniel Pink | 创意/认知任务上 if-then 奖励**降**绩效；动力=自主/精进/意义（Motivation 3.0）。直击提成制杀创意。继承 T04。 |
| T03-S011 | https://deming.org/tyranny-of-metrics/ | secondary | 2026-06-18 | Deming Institute（评 Muller 书） | Goodhart 定律「度量一旦成为目标就不再是好度量」；metric fixation 招致 gaming。继承 T04。 |
| T03-S012 | https://www.jiemian.com/article/938548.html | secondary | 2026-06-18 | 界面新闻 | 「索尼真被绩效考核毁了吗」——天外伺郎论点 + 反驳（考核主义≠绩效主义、单因论被证伪）。矛盾两面保留。继承 T04。 |
| T03-S013 | https://www.parakeeto.com/blog/agency-metrics/ | surrogate_primary | 2026-07-02 | Parakeeto（agency 财务 vendor） | **本次 WebFetch**：utilization（个人年 65-80%、agency 整体 50-60%+、producer 周 75-90%）、ABR=AGI÷交付工时、交付毛利/项目 60-70% AGI、营业利润 25-35%；建议**先立核心财务再逐步加非财务指标**。数字=vendor 口径。 |
| T03-S014 | https://productive.io/blog/billable-utilization/ | surrogate_primary | 2026-06-18 | Productive（agency PSA） | billable utilization=可计费工时÷总工时；PSF 最优 70-75%。继承 T04/T06。 |
| T03-S015 | https://productive.io/blog/agency-kpis-profitability-metrics/ | surrogate_primary | 2026-07-02 | Productive（agency PSA） | 「7 个保利润 KPI」：利用率/交付毛利/项目利润/AGI-per-FTE/回款/在手订单 等。本次 WebSearch 取用。 |
| T03-S016 | https://corehelpcenter.bqe.com/hc/en-us/articles/360058716473 | secondary | 2026-06-18 | BQE CORE（PSA） | utilization vs realization 区分：高 util+低 realization=拼命干客户不付钱的活。继承 T06。 |
| T03-S017 | https://www.metric.ai/blog/leverage-models-in-professional-services | surrogate_primary | 2026-06-18 | Metric.ai（PSA） | leverage 杠杆模型：初级÷资深；欠授权=利润杀手。继承 T06。 |
| T03-S018 | https://business.adobe.com/blog/basics/kpis-for-creative-teams | surrogate_primary | 2026-06-18 | Adobe | 创意团队 KPI 四支柱：运营效率/创意质量/干系人满意/商业影响——"创意三层"的一个版本。继承 T04。 |
| T03-S019 | https://blog.betterworks.com/never-grade-on-a-curve/ | surrogate_primary | 2026-06-18 | Betterworks（绩效 SaaS） | 批判强制分布/钟形曲线；主张 calibration + 面谈改革。继承 T06。 |
| T03-S020 | https://www.betterworks.com/magazine/performance-review-cycle | surrogate_primary | 2026-07-02 | Betterworks | 现代绩效周期：从年度评价转向持续 check-in + 校准 + 面谈；本次 WebSearch 取用。 |
| T03-S021 | https://www.shrm.org/topics-tools/tools/express-requests/performance-improvement-plans-pip | surrogate_primary | 2026-06-18 | SHRM | PIP 绩效改进计划定义（限期+目标+支持）。继承 T06。 |
| T03-S022 | https://www.shrm.org/topics-tools/flagships/all-things-work/360-degree-evaluations-insights-into-action | surrogate_primary | 2026-06-18 | SHRM | 360 环评定义；建议只作发展用、不直接挂奖惩。继承 T06。 |
| T03-S023 | https://www.perdoo.com/resources/blog/okrs-kpis-for-marketing | surrogate_primary | 2026-07-02 | Perdoo（OKR vendor） | KPI=诊断/OKR=处方；先立战略再选 KPI；KPI 上限 10-12 个；**分阶段试点（1-2 个高绩效团队）再全铺**。本次 WebSearch 取用。 |
| T03-S024 | https://www.cultureamp.com/blog/performance-review-calibrations | surrogate_primary | 2026-07-02 | Culture Amp（绩效 SaaS） | 校准=多主管拉齐评分口径；定尺度→释义→定分布→证据讨论→调分。本次 WebSearch 取用。 |
| T03-S025 | https://lattice.com/articles/the-how-and-why-of-performance-review-calibration | surrogate_primary | 2026-07-02 | Lattice（绩效 SaaS） | 校准的 why/how：HR 主持、证据驱动、消除宽严不一。本次 WebSearch 取用。 |
| T03-S026 | https://www.lifelabslearning.com/blog/creating-a-performance-review-process | surrogate_primary | 2026-07-02 | LifeLabs Learning（管理培训） | 绩效周期落地：自评→经理评→1:1 对齐→发展对话；6 个月一大评 + 每周/双周 1:1。本次 WebSearch 取用。 |
| T03-S027 | https://www.sidekickaccounting.co.uk/post/creative-agency-staff-bonus-plan | secondary | 2026-07-02 | Sidekick（创意 agency 会计所） | 创意 agency 奖金池经验值 **5-15% 毛利**；先做现金流建模再上分享制。本次 WebSearch 取用（vendor 经验，caveat）。 |
| T03-S028 | https://matchstick.legal/blog/employee-incentive-program-ideas-creative-agency | secondary | 2026-07-02 | Matchstick（服务创意公司的律所） | 创意 agency 激励菜单：利润分享 / phantom equity（含并购触发）/ real equity；个人 vs 团队建议 **70/30 或 60/40 偏团队**（纯个人奖金毁协作）。本次 WebSearch 取用。 |
| T03-S029 | https://www.workamajig.com/blog/agency-roles | secondary | 2026-06-18 | Workamajig（agency PSA） | agency 岗位职责：AE/account director/CD/copywriter/art director。继承 T06。 |
| T03-S030 | https://agencyanalytics.com/blog/agency-metrics-kpis-profitability-growth | secondary | 2026-07-02 | AgencyAnalytics | agency 盈利/留存/增长 KPI（利润率/留存/LTV/回款）+ retainer vs 项目制。本次 WebSearch 取用。 |
| T03-S031 | https://www.digitalapplied.com/blog/agency-scope-creep-prevention-2026-sow-framework | secondary | 2026-06-18 | DigitalApplied | SOW 四段框架；scope creep 侵蚀 retainer 有效时薪 15-30%（vendor 口径）。继承 T06。 |
| T03-S032 | https://www.trinityp3.com/agency-performance/measure-and-manage-agencys-ai-transformation/ | secondary | 2026-07-02 | TrinityP3（agency 管理咨询） | **本次 WebFetch**：AI 转型记分卡（CPDA 每可交付资产成本 -30%、HRI 人力再配置 15%、ADIS AI 增量分 5-10% lift/60% 用例、TTP -50% 等）+ **"分母挑战"**：AI 让工时分母失真、util 指标误导，须转"每美元质量校正产出"。目标值=咨询方倡导口径 caveat。 |
| T03-S033 | https://digiday.com/marketing/as-industry-layoffs-become-the-new-normal-so-does-fear-of-ais-impact-on-adlands-job-market/ | secondary | 2026-07-02 | Digiday（行业媒体） | 裁员成"新常态"+ AI 就业恐惧；Forrester 上修 AI 致美国广告从业净 **-15%**（~2027）。本次 WebSearch 取用。 |
| T03-S034 | https://adage.com/agencies/aa-agency-layoffs-everything-to-know/ | secondary | 2026-07-02 | Ad Age（行业媒体） | 2025 大厂裁员盘点：Omnicom 约 4000（并购 IPG 后）、Dentsu 3400、Ogilvy 700（5%）；四大 holdco Q3 有机增长 0.3%（5 年最低）；Dentsu 营业利润率降至 16-17%（2027E，原 20-25%）。本次 WebSearch 取用。 |
| T03-S035 | https://advertisingweek.com/ai-is-changing-the-way-we-work-agency-pricing-needs-to-change-too/ | secondary | 2026-07-02 | Advertising Week | WPP 等 holdco 明确从"按工时"转"按产出/结果"定价（AI 驱动）。本次 WebSearch 取用。 |
| T03-S036 | http://www.duibiao.org/2020/news_0730/2325.html | secondary | 2026-06-18 | 对标考察网（咨询对标） | 华为 价值创造→评价→分配 + 获取分享制：前台按结果获取、后台按服务分享、向增量倾斜。继承 T06。 |
| T03-S037 | https://book.douban.com/subject/26183356/ | surrogate_primary | 2026-06-18 | 《以奋斗者为本》黄卫伟主编·中信 2014 书页 | 华为人力资源纲要：PBC 三段、奖金包=去年×(1+经营效益改善率)、超预算 2 倍熔断、活力曲线（主要针对干部层）。继承 T01。 |
| T03-S038 | https://news.mbalib.com/story/247054 | reference | 2026-06-18 | MBA智库资讯 | 华为/IBM PBC 流程（PDCA 闭环）、业务目标权重约 80%。培训口径 caveat。继承 T04/T06。 |
| T03-S039 | https://en.wikipedia.org/wiki/Vitality_curve | reference | 2026-06-18 | Wikipedia | 活力曲线 20-70-10、rank-and-yank、GE ~2015 弃用、微软 2013 废 stack ranking。继承 T04/T06。 |
| T03-S040 | https://en.wikipedia.org/wiki/After-action_review | reference | 2026-06-18 | Wikipedia | AAR 事后回顾（美军起源）=中文"复盘"对应物。继承 T06。 |
| T03-S041 | https://michaelfarmer.substack.com | verified_primary | 2026-06-18 | Michael Farmer | SOW→SMU 计量工作量；2025 建模：继续按工时计费，AI 将削 agency fee ~24%（WPP 预测 5 倍）。继承 T01。 |
| T03-S042 | https://www.ignitiongroup.com/propulsion-blog | verified_primary | 2026-06-18 | Tim Williams（Ignition） | value-based pricing：对外按工时卖→对内必按工时考核 utilization→死亡螺旋；对外按价值→对内才能转向价值创造。继承 T01。 |
| T03-S043 | https://agencymanagementinstitute.com | verified_primary | 2026-06-18 | Drew McLellan（AMI） | 中小 agency：以 AGI 为分母（loaded salary≈55% AGI、AGI/FTE、12-40 人最优）；2026 趋势团队更小/更多合同工/AI 重塑岗位。继承 T01。 |
| T03-S044 | https://www.jiemian.com/article/3767945.html | secondary | 2026-06-18 | 界面新闻 | 末位淘汰/强制分布法律风险：中国最高法「末位≠不胜任」，硬末位淘汰有违法风险。继承 T01。 |
| T03-S045 | https://2bobs.com/podcast/the-complexities-of-commission-culture | verified_primary | 2026-07-02 | David C. Baker + Blair Enns（2Bobs） | 「提成文化的复杂性」专集：提成制在创意服务业的副作用（抢单/短视/伤协作）。本次 WebSearch 确认。 |

**统计**：45 源。bucket：verified_primary **13**（Maister×2/Baker/Enns×2/Doerr/Kaplan-Norton/稻盛/Deming/Pink/Farmer/Williams/McLellan/2Bobs）· surrogate_primary **13**（Parakeeto/Productive×2/BQE/Metric.ai/Adobe/Betterworks×2/SHRM×2/Perdoo/CultureAmp/Lattice/LifeLabs/以奋斗者为本书页/TrinityP3）· secondary **13**（界面×2/Sidekick/Matchstick/Workamajig/AgencyAnalytics/DigitalApplied/Digiday/AdAge/AdWeek/对标）· reference **3**（mbalib/Wikipedia×2）。**一手 verified_primary ≈ 29%**——诚实边界：workflow track 的高价值内容多是"落地手法/基准数字"，天然落在 PSA/HR SaaS/咨询 vendor docs（surrogate）与行业媒体（secondary）；绩效**方法论正典**的一手（Maister/Enns/Doerr/Kaplan-Norton/稻盛/Deming/Pink/2Bobs）已全部取到作者官网/官方，共 13 条。**本次亲验 18 条（2026-07-02），继承 27 条（2026-06-18）。**

---

## Phase 1 · 绩效体系搭建（从 0）

> 序列：**定战略/定位 → 拆组织目标 → 选框架与工具 → 分岗位设指标 → 定周期与治理**。本行的第一性铁律（跨 Farmer/Williams/Baker/Enns 五人共识）：**对外定价方式决定对内考核方式**——你按工时卖，内部就会按工时/utilization 榨人（掉进死亡螺旋）；你按价值/产出卖，内部才谈得上按价值创造考核 [T03-S042/S004]。所以"搭绩效"真正的第 0 步不是选 SaaS，是**确认定位与定价权**。

### 1.1 小工作室 / 创意热店（<20-30 人）怎么做
- **动作**：老板+合伙人先用一页纸写清"我们只做什么、凭什么收更高价"（定位）→ 全公司 3-5 条季度 OKR（定性目标+可量 KR）→ 工时用 Toggl/Clockify 免费档、项目毛利用飞书多维表格手算 → 岗位指标只分"结果层/效率层可量化 + 创意质量层靠合伙人评议"三档 → 周期用**季度轻 check-in + 半年一次正式面谈**，不上年度大考。
- **▸ 跳过哪步**：**跳过 BSC 四视角 + 多考核周期 + 强制分布**——小团队上这些=指标暴政、逼走人才。KPI 清单**上限 10-12 条**，超了就砍 [T03-S023]。
- **案例**：Perdoo 的 marketing 绩效落地建议——"若不知道要达成什么，就还没到定 KPI 的时候"，先用 OKR/SMART/BSC 之一把战略讲清，KPI 只留核心几条，**先在 1-2 个高绩效小组试点 OKR 再全铺**（phased rollout 降低组织排异）[T03-S023]。创意热店直接用这套轻装上阵即可。

### 1.2 成熟大 agency / 4A / 上市集团（150-5000+ 人）怎么做
- **动作**：集团战略→事业部/客户组目标层层拆解（BSC 战略地图：财务→客户→流程→学习成长四视角对应 回款利润/客户续约/交付返稿/人才培养）[T03-S007] → 上北森/Lattice 承载多业务线×多考核周期×矩阵汇报 → 岗位指标按职级+职能精细化 → 周期用**季度 OKR check-in + 年度正式考核 + 校准会**，结果直连调薪/晋升/职级。
- **▸ 优化点**：把"创意质量"从硬 KPI 里拆出来单独走专家评议/获奖/比稿命中通道——**别让 BSC 的"可量化诱惑"把创意也塞进仪表盘**（Track 02 红线：别用①效率层⑤呈现层的伪精确伪装⑥创意质量层）。
- **案例**：Kaplan-Norton BSC 四视角本就是为"别只看财务一个数"设计——大 agency 用它把签单额之外的客户续约、交付效率、团队能力一起纳入，但正典也警告 BSC 易膨胀成"20 个指标没人看的仪表盘"[T03-S007]，所以大厂的优化点恰恰是"减指标"。

### 1.3 近期变化（AIGC / 经济下行）
- **▸ 额外动作（经济下行）**：2025 起把绩效体系的"北极星"从"冲流水/产量"改成"**保毛利 + 保现金（回款）+ 人效**"——四大 holdco 2025 Q3 有机增长仅 0.3%（5 年最低），Omnicom（并 IPG 后）约裁 4000、Dentsu 3400、Ogilvy 700（5%），Dentsu 营业利润率被压到 16-17%（2027E，原 20-25%）[T03-S034]。体系搭建必须内嵌"更小团队、更多合同工/兼职、按项目弹性配置"的假设 [T03-S043]。
- **▸ 额外动作（AIGC）**：建体系时就要预留"工时/产量类指标权重会下降"的接口——WPP 等已公开从"按工时"转"按产出/结果"定价 [T03-S035]；对外定价一变，对内考核口径必须同步改（回到 1.1 的第一性铁律）。
- **案例**：McLellan/AMI 2026 系列判断——agency 团队更小、更多全球/合同人才、AI 重塑岗位；同时"AI Impact 2026"调研 79% 说 AI 正向影响绩效但仅 3% 自认专家、且 2025 各渠道 ROI 反而下降 [T03-S043]。启示：体系要能容纳"产能涨、单价跌、岗位重构"的新常态，别把去年的指标冻结。

> **矛盾保留**：量化派（先定 KPI/OKR 把目标落地）⇄ 反绩效主义（Deming：先别急着考评，多数问题是系统 [T03-S009]）。本阶段的调和是"**先定位定价（修上游）、再上可量化数据、最后才配指标**"，而非一上来就发考核表。

---

## Phase 2 · 分岗位指标设计（本行最难点）

> 招牌心智模型 **创意可量化三层**（化解"创意不可量化 vs 必须可考核"元矛盾）：任何岗位的产出都拆成 **① 创意质量（难量化→专家评议/获奖/作品集/客户反馈，主观，不上硬 KPI）+ ② 交付效率（可量化→工时/准时率/返稿次数/利用率）+ ③ 商业结果（可量化→项目利润/ROAS/续约/增购）**。Adobe/Workamajig 的"创意四支柱"（运营效率/创意质量/干系人满意/商业影响）本质就是这个分层的一个版本 [T03-S018]。**各岗位的差别，只是三层的配比不同。**

### 2.1 小工作室怎么做（粗粒度分层）
- **各岗位三层配比（起步版）**：
  - **创意（文案/美术/CD）**：质量 60%（合伙人/CD 评议 + 获奖 + 代表作，**不货币化到条数**）+ 效率 20%（准时/返稿）+ 结果 20%（项目利润/客户口碑）。
  - **AE / 客户执行**：结果 60%（客户满意/续约/回款/客单毛利）+ 效率 30%（准时/响应）+ 质量 10%。**回款必须进指标**——签单不回款是虚假业绩 [T03-S030]。
  - **媒介 / 投放**：结果 70%（ROI/ROAS/CPM/转化，本行**最易量化**岗）+ 效率 30%。注意考核**服务费/返点**而非过手媒介流水。
  - **设计 / 产能岗**：效率 50%（产能/准时/返稿率）+ 质量 30% + 结果 20%。
  - **项目管理 PM**：效率+结果各半（准时交付率 + 项目利润率 + 预算达成）[T03-S029]。
  - **BD / 新业务**：结果为主（新签/回款/客户质量），但**质量优先于数量**——Enns：BD 目标应是"塑造未来客户结构"的质量目标，浮动激励上限约 +20-25% [T03-S005]。
- **▸ 跳过哪步**：跳过"给创意岗设产量 KPI（几条文案/几张图）"——这是索尼绩效主义之殇的入口 [T03-S012]。
- **案例**：Adobe 创意四支柱把"创意质量"与"运营效率/商业影响"并列而非混为一谈 [T03-S018]——小工作室照此把创意人的"作品质量"单独走评议、把"准时/返稿/项目利润"走数字，就已经比"一张 KPI 表打天下"高明。

### 2.2 成熟大 agency 怎么做（细粒度×职级）
- **动作**：同一职能按职级拆指标（junior copywriter 重效率/成长、CD 重质量把关+团队产出+客户结果）；用 360 环评补"协作/带教"这类单一上级看不全的软性贡献 [T03-S022]；媒介岗直接挂 ROAS/CPA dashboard；PM 岗由其判定工时 billable/non-billable，喂给人效核算 [T03-S029]。
- **▸ 优化点**：AE 岗要**防"甲方压力传导"**——若 AE 指标全是"客户满意度"，会逼 AE 无底线满足甲方、牺牲创意与利润；须把"客单毛利/回款/scope 管控"一起纳入，让 AE 替公司挡回无限改稿 [T03-S031]。
- **案例**：Productive「7 个保利润 KPI」（利用率/交付毛利/项目利润/AGI-per-FTE/回款/在手订单）给大 agency 一套"结果+效率层"的标准件 [T03-S015]；再叠加创意质量的评议通道，就是完整的分层指标体系。

### 2.3 近期变化（AIGC / 经济下行）
- **▸ 额外动作（AIGC）**：创意/设计岗的"**产量、工时**"类指标正在失效——AI 让产能暴涨，考核"做了多少稿/多少小时"更荒谬。TrinityP3 建议改用**面向产出质量与增量**的新指标：ADIS（AI 生成素材必须做 A/B、对人工基线有 5-10% CTR/CPA/CVR 统计显著提升，至少 60% 用例达标）、HRI（把 15% 的媒介/创意工时从重复劳动移到策略）、CPDA（每"可交付、已上线"资产成本降 30%）[T03-S032]。媒介岗 ROAS 类硬指标反而更稳固。
- **案例**：TrinityP3 的 AI 转型记分卡明确"**别再考核原始产出量，考核'质量校正的每美元产出'**"[T03-S032]——这正是把"创意三层"在 AIGC 时代重新配比：质量层权重上升、纯产量/工时层权重下降。

> **矛盾保留**：媒介岗（一切可量化）⇄ 创意岗（核心不可量化）是同一张组织架构里的两极；用同一套 KPI 模板套两者是本行最常见的设计错误。**分层，不分对错。**

---

## Phase 3 · 项目与人效核算（乙方区别于甲方的命门）

> 序列：**工时表 → utilization/billability → realization → 项目利润率 → 人均产值/毛利 → AGI per head**，用 LUBRM 做诊断总图。第一性铁律（Track 02 装配顺序）：**没有工时数据，一切人效指标都是拍脑袋**——必须先上工时/PSA 拿真实数据，再定指标。

### 3.1 小工作室怎么做（最省路径）
- **动作**：Toggl/Clockify 记工时（区分 billable=客户项目 vs non-billable=比稿/内训/行政）→ 飞书多维表格公式算 **项目毛利 =（收入 − 工时×成本率 − 外部成本）** → 汇总看 人均毛利 与 整体 utilization。
- **▸ 优化点**：utilization 目标**别照搬律所的 80%+**——agency 因比稿/创意打磨/内部会等非计费时间天然多，**整体合理区间 ~50-60%（Baker/Parakeeto 口径）**，个人年 65-80%，producer 周可 75-90% [T03-S013/S003/S014]。把 agency 硬压到 85% = 逼员工造假工时 + 过劳。
- **案例**：Parakeeto 给的落地顺序——"**先立核心财务（毛利/利润），再逐步加非财务指标，频率与精度慢慢提**"，别一上来追求工时颗粒度到分钟 [T03-S013]。小工作室按这个"由粗到细"上，不会被数据工程压垮。

### 3.2 成熟大 agency 怎么做（PSA 全栈）
- **动作**：上 agency 专用 PSA（Productive/Scoro/Kantata）把 工时×成本率×项目 实时算成 margin、utilization、realization；按 **AGI（毛收入=收入−外部媒介/制作转付）为分母**算一切比率（loaded salary≈55% AGI、AGI/FTE≈$90K、营业利润≥15%，均**美国口径 caveat**）[T03-S003/S043]；用 LUBRM 逐杠杆诊断"利润漏在哪"[T03-S001]。
- **▸ 额外动作**：盯 **realization（实现率=实收÷标准价）**——它是 agency **最隐蔽的利润漏斗**：高 utilization + 低 realization = 团队拼命干了客户永远不会付钱的活（免费改稿/超范围/打折）[T03-S016]。无限改稿的伤害就量化在这里，必须有人管。
- **案例**：Maister LUBRM 拆解——利润/合伙人=杠杆×利用率×费率×实现率×利润率；且他点名"**欠授权（资深人干初级活）吃掉 40-50% 产能**"是利润杀手，改善顺序应是**先提 rate（涨价）、最后才逼 utilization**（后者是短期 hygiene，靠拉更重的车，最弱）[T03-S001/S017]。大 agency 的人效核算不是"催工时"，是"修杠杆+提价+堵 realization 漏"。

### 3.3 近期变化（AIGC / 经济下行）
- **▸ 额外动作（AIGC）**：正视"**分母挑战**"——AI 让人力工时（分母）缩小、产出（分子）放大，**历史 utilization 基准正在失真、甚至误导**。TrinityP3 建议从"消耗了多少小时"转向"每美元投入的质量校正产出"、并引入可变成本占比（handle +25% 客户量而可变成本升 <5%）等 scalability 指标 [T03-S032]。
- **案例**：Farmer 建模——若继续按工时计费，AI 把 adaptation 产能从 5→25 SMU/人年（5×），一个 $61.7M fee 的 agency 掉约 $15M=24% fee，生产率红利全归甲方 [T03-S041]。即：**AIGC 下"人效"若还用工时口径算，会算出越用 AI 越"没产值"的荒谬结论**——必须改用产出/价值口径。数字为其私有 benchmark 口径，caveat。

> **矛盾保留**：工时制（utilization/realization/项目利润全靠工时表，是从咨询/律所引入的绩效基础设施）⇄ 员工健康（工时制"绑架健康"、为凑 billable 造假/过劳，与 996 同一批判母题）⇄ 价值定价派（Enns/Ron Baker「没有客户买你的时间」，主张埋葬工时表）。**工时数据要采，但别把工时当绩效目标去榨。**

---

## Phase 4 · 激励与分配落地

> 激励光谱（协作 ↔ 强激励 ↔ 留人）：**固定+奖金 → 项目分成 → 提成 → 事业合伙人/工作室制 → 股权**。核心难题：**广告是集体产物，怎么把奖金拆到个人而不摧毁协作。**

### 4.1 小工作室怎么做（团队奖金池优先）
- **动作**：底薪具竞争力（把"钱"这件事拿下桌面，Pink [T03-S010]）+ **年度/季度奖金池 = 毛利的 5-15%**（先做现金流建模确认养得起再上）[T03-S027] + 池子按 **70/30 或 60/40 偏团队** 切分（纯个人奖金会毁掉创意所需的协作）[T03-S028]。
- **▸ 跳过哪步**：**跳过给创意岗上纯提成/计件**——Pink：创意/认知任务上 if-then 奖励反而**降**绩效 [T03-S010]；2Bobs「提成文化的复杂性」也点名提成制在创意服务业的抢单/短视/伤协作副作用 [T03-S045]。提成留给 BD 岗，且**按毛利/回款计基而非流水**（否则鼓励低价冲规模、亏本接单）。
- **案例**：Matchstick 给创意 agency 的激励菜单明确建议"**个人 vs 团队 70/30 偏团队**，因为创意工作是协作的，纯个人计划会摧毁团队产出"[T03-S028]；小工作室照此以团队奖金池为主、个人浮动为辅，最稳。

### 4.2 成熟大 agency 怎么做（获取分享 + 合伙人/阿米巴）
- **动作**：华为式"**获取分享制**"——前台（直接创收组）按经营结果"获取"、后台（设计/AE 支撑）按服务"分享"，贯穿 价值创造→评价→分配 [T03-S036]；**奖金包公式** = 去年奖金包 ×(1+经营效益改善率)、**超预算 2 倍熔断**（防爆款投机）[T03-S037]；核心人才走**事业合伙人/超额分成**（不必稀释股权）或 studio/阿米巴独立核算多劳多得 [T03-S008]。
- **▸ 优化点**：项目分成**别用短期公式硬拆**——Maister（多组织奖酬）：多数成熟公司**避免短期公式化**，用 3-5 年"判断式"让组回报≈组利润，正是为了不制造组间恶性竞争 [T03-S002]。把"当期项目利润"当唯一分配公式，会逼各组抢客户/不协作。
- **案例**：华为"奖金包=去年×(1+效益改善率)+2 倍熔断"[T03-S037] 映射 agency = 项目组/客户组按**毛利增量**分奖金 + 熔断防投机；PBC 里强制的"团队合作承诺"（约占 10%）对冲个人英雄主义 [T03-S038]。**caveat（矛盾保留）**：具体公式存在培训口径分歧——一说"存量×系数×80% + 增量×系数×160%"（向增量倾斜），另一说"存量增量线性、不额外加码"，且华为内部文档不公开；**取"先获取利润才有奖金包 + 向增量/战略贡献倾斜"的机理，不背书任何具体系数**。

### 4.3 近期变化（AIGC / 经济下行）
- **▸ 额外动作（创意非物质激励）**：预算收缩期现金激励空间被压，更要靠 Pink 的 **自主/精进/意义**——给创意人作品署名、成长路径、自主权，而非纯金钱 KPI [T03-S010]。
- **▸ 额外动作（AIGC）**：**重估计件/产量挂钩的分配**——AI 让设计/文案产能暴增，按"条数/张数"计酬会奖励灌水；分配口径应随定价从"按工时/产量"转"按产出价值/客户结果"（WPP 转向印证）[T03-S035]。
- **案例**：Enns「BD 薪酬 5 步」——BD 激励要**质量优先于数量**、浮动上限约 +20-25%、且承认"多数人要收入安全、雇主要绩效稳定"，所以别做无上限纯提成 [T03-S005]。经济下行下这条尤其重要：无上限提成在下行期既烧现金又诱导短视抢单。

> **矛盾保留**：提成制（多劳多得、强激励，但抢单/短视/伤协作 [T03-S045]）⇄ 固定+奖金（公平但大锅饭）⇄ 项目分成/阿米巴（划小核算、责任到组，但组间抢资源/本位主义 [T03-S002/S008]）。**没有普适最优，只有与"你按什么定价、你要协作还是单兵"匹配的选择。**

---

## Phase 5 · 考核执行与面谈

> 序列：**目标共识（军令状/PBC）→ 过程辅导（1:1/CFR）→ 自评述职 → 校准 calibration → 面谈（GROW）→ 结果应用（调薪/晋升/PIP/淘汰）→ 申诉**。

### 5.1 小工作室怎么做（轻校准、重面谈）
- **动作**：期初 老板/组长与员工**共同**定目标（避免单方面拍指标，Drucker「目标+自我控制」）→ 期中每周/双周 1:1 辅导 → 期末员工先自评 → 组长与老板**碰一次简单校准**（拉齐宽严）→ 一对一面谈用 **GROW（Goal/Reality/Options/Will）提问式**、让创意人自己说出差距与下一步，别下判决 [T03-S026]。
- **▸ 跳过哪步**：**跳过强制分布/末位淘汰**——团队 <10 人时强制淘汰 10% 反而逼走人才、制造内斗 [T03-S039]。
- **案例**：LifeLabs 的绩效周期——自评→经理评→1:1 对齐（比对各自答案、谈成就与下一步）、6 个月一大评 + 每周/双周 1:1 持续辅导 [T03-S026]；小工作室把"面谈质量"做扎实，比任何评分表都管用（创意岗量不出的作品好坏靠专家式对话给反馈）。

### 5.2 成熟大 agency 怎么做（PBC + 正式校准 + 分档应用）
- **动作**：**目标共识**用 PBC/目标承诺书（业务目标~80% + 执行 + 团队合作，主管一对一沟通后立下，相当于"军令状"）[T03-S038] → **过程**季度 check-in + CFR [T03-S006] → **自评述职** → **校准会**：多主管开会横向比对评分、证据驱动、HR 主持消除宽严不一 [T03-S024/S025] → **面谈** → **结果应用**：调薪/晋升/PIP（限期+目标+支持，SHRM）[T03-S021] → **申诉**通道。
- **▸ 优化点**：**校准会防"谁嗓门大/职位高谁说了算"**——Betterworks/CultureAmp 都指出 calibration 实操易引入政治与偏见，须有主持纪律、以证据（作品/项目数据/360）说话 [T03-S019/S024]。
- **案例**：完整校准 6 步（定目标与准备→定尺度与释义→证据讨论→调分→定稿存档→沟通结果）[T03-S024]；大 agency 跨组公平全靠它（创意组长手松、媒介组长手紧会毁掉全公司绩效可信度）。

### 5.3 强制分布 / 活力曲线：用不用？（矛盾核心，双面呈现）
- **用的一方**：华为活力曲线 20/70/10（A 拿 B 的 2-3 倍），但**落地偏柔性、主要针对干部层**（任正非"不能让人人自危"）[T03-S037]；GE 拥趸称 1981-2001 盈利涨 28 倍（**倡导方口径、非因果证据** caveat）[T03-S039]。
- **不用的一方**：Deming——94% 变异是系统非个人，排名个人既不公也毁士气、摧毁协作 [T03-S009]；GE 本尊 ~2015 弃用、微软 2013 废 stack ranking [T03-S039]；**中国最高法「末位≠不胜任」，硬末位淘汰有违法风险** [T03-S044]。
- **▸ 额外动作（折中）**：若要用，**只对总监/组长层柔性用**、给足申诉与 PIP 缓冲、绝不对 <10 人小组硬淘汰。

### 5.4 近期变化（AIGC）
- **案例**：绩效 SaaS 正从"评价"转向"实时反馈+教练"，AI 辅助写 review/自动生成绩效材料 [T03-S020]。**caveat**：AI 解决的是"写得快"，**不解决"创意好坏由谁判定"**——别被"AI 绩效"话术骗成"AI 能考核创意"。

> **矛盾保留**：结果导向（PBC/KPI 打分排名）⇄ 发展导向（GROW/CFR 教练对话，不评分）；强制分布拥趸 ⇄ Deming/最高法反排名。**面谈的正确姿势是"发展而非审判"，评分只是副产品。**

---

## Phase 6 · 复盘迭代 + 反绩效主义防坑

> 序列：**项目复盘（AAR）→ 指标体系年度复盘 → Goodhart 反身检查 → 随定价/AIGC 迭代**。这一阶段是"防止绩效体系自我腐化"的免疫系统。

### 6.1 小工作室怎么做（项目复盘沉淀能力）
- **动作**：每个大项目/比稿结束做 **AAR 复盘**（目标 vs 结果、哪里对/错、下次怎么改），把"个人经验"转"组织资产"[T03-S040]；这是过程导向绩效抓不到的"学习成长"维度的软性抓手。
- **▸ 优化点**：上任何硬 KPI 前先做 **Goodhart 反身检查**——问"这个数被挂高利害后会被怎么钻空子？"（改稿刷工时、抢易做的客户、注水续约、灌水作品冲产量）[T03-S011]。
- **案例**：Muller「度量一旦成为目标就不再是好度量」[T03-S011]——小工作室每次想给创意加一个硬指标时，先假想员工会怎么 game 它；能被轻易 game 的，就留给专家评议而非上 KPI。

### 6.2 成熟大 agency 怎么做（体系年度复盘、防指标暴政）
- **动作**：年度回看"哪些指标真的驱动了想要的行为、哪些只是被 game 了"，砍掉膨胀的仪表盘（BSC 易变 20 指标暴政）[T03-S007]；核对"绩效体系是否在系统性制造 996/无限改稿"（工时论英雄→系统性 996，合规红线）。
- **▸ 额外动作**：把"甲乙方权力不对等（压价/无限改稿/比稿白嫖/账期）"如何经绩效制度传导到员工过劳，作为年度复盘的显性议题——**乙方绩效本质是"用内部考核对冲甲方不确定性的转嫁"**，若不修上游（定位/定价/SOW 变更单），内部再怎么拧人都是治标 [T03-S031/S042]。
- **案例**：《绩效主义毁了索尼》——绩效主义使激情集团消亡、上司只看指标不把下属当人、精力耗在统计业绩而非做事 [T03-S012]；**但反驳同样重要**：界面新闻指出索尼衰落是多因（错失数字化/组织僵化），把锅全甩给"绩效主义"是单因论、已被证伪，且索尼跑的其实是"考核主义（评级挂钱）"非真"绩效主义"[T03-S012]。**引用必须两面给，别当护身符也别当稻草人。**

### 6.3 近期变化（AIGC 冲击工时制后怎么改考核）——本阶段最重要
- **▸ 额外动作**：AIGC 从根上动摇了"工时=价值"这个 utilization 考核赖以成立的假设，考核体系必须**显式重估工时/产量指标的权重、向单位价值/客户结果 pivot**——否则绩效体系与现实脱节。
- **落地新指标框架（TrinityP3 AI 转型记分卡）[T03-S032]**（目标值=咨询方倡导口径，caveat 偏理想）：
  - **CPDA 每可交付资产成本**（含人力+许可费÷已上线资产数）目标 12 个月降 30%；
  - **HRI 人力再配置指数**（重复劳动工时→策略/创新）目标首年 15%；
  - **ADIS AI 增量分**（AI 素材须 A/B、对人工基线 5-10% lift、≥60% 用例达标）——取代 vanity metric；
  - **TTP 上线速度**降 50%、**可变成本占比**（+25% 客户量、可变成本升 <5%）等。
  - 治理层：从"按工时问责"转"按产出问责"。
- **案例**：Forrester 已上修 AI 致美国广告从业净 **-15%**（~2027）[T03-S033]；叠加经济下行裁员（见 Phase 1.3），**"越用 AI 越省工时→按工时算越没产值→越裁人"** 是死亡螺旋。破法即 Farmer/Williams 早说的：对外转产出/结果定价 [T03-S041/S042/S035]，对内同步把考核从工时/产量改成价值/结果——这是 AIGC 时代 agency 绩效改革的唯一出路。

> **矛盾保留**：量化派（不考核养懒人、老板算不清账）⇄ 反绩效主义（Deming/Pink/Muller/索尼：硬考核杀创意、被博弈、毁协作）。**这条元矛盾无法靠选边解决，只能靠"三层拆分（质量/效率/结果）+ Goodhart 反身检查 + 随定价/AIGC 持续迭代"动态调和。**

---

## Phase 2 接口

### 完整绩效 SOP 一图流（装配顺序，箭头=依赖，不可倒装）

```
【0 上游·前置】定位/专长 → 定价方式（价值/产出 vs 工时）        ← Baker/Enns/Williams：定价决定考核 [S004/S042]
        │  (对外按什么收费，对内就得按什么考核；不修这层，下游全是拧人)
        ▼
【1 搭体系】战略 → 拆组织目标(BSC四视角/OKR) → 选框架&工具 → 定周期治理   [S007/S006/S023]
        │  小:季度OKR轻check-in ｜ 大:季度OKR+年度考核+校准会
        ▼
【2 分岗位指标】按"创意三层"配比：质量(评议/获奖,不上硬KPI)｜效率(工时/准时/返稿)｜结果(利润/ROAS/续约/回款)  [S018/S015]
        │  创意重质量 · AE/BD重结果(含回款) · 媒介重ROAS · 设计/PM重效率
        ▼
【3 人效核算】工时表 → utilization(agency~50-60%,别照搬律所80%) → realization(堵免费改稿漏) → 项目利润 → 人均毛利 → AGI/FTE ； LUBRM诊断  [S013/S016/S001/S003]
        │  小:Toggl+飞书多维表格手算 ｜ 大:PSA(Productive/Kantata)全栈  ← 没数据的指标都是拍脑袋
        ▼
【4 激励分配】固定+奖金(池=毛利5-15%,70/30偏团队) → 项目分成/阿米巴 → 提成(仅BD,按毛利计) → 事业合伙人 → 股权 ； 获取分享制+奖金包×(1+效益改善率)+熔断  [S027/S028/S036/S037]
        │  创意慎提成(Pink);非物质激励(自主/精进/意义)
        ▼
【5 考核执行】目标共识(PBC/军令状) → 过程辅导(1:1/CFR) → 自评述职 → 校准(证据驱动,防嗓门大) → 面谈(GROW发展式) → 结果应用(调薪/晋升/PIP/申诉)  [S038/S006/S024/S026/S021]
        │  强制分布:只干部层柔性用,小团队/基层禁(最高法末位≠不胜任) [S044]
        ▼
【6 复盘迭代】项目AAR复盘 → 指标年度体检 → Goodhart反身检查 → 随AIGC/定价pivot(工时权重↓、价值/结果权重↑)  [S040/S011/S032]
        │  防坑:三层别混、创意别硬KPI、OKR别挂薪酬、签单必计回款、防系统性996
        └──────────────► 回流【0/1】：迭代定价与体系
```

### 大 agency vs 小工作室：关键差异（同一 SOP，不同颗粒度）

| 维度 | 小工作室/创意热店（<30 人） | 成熟大 agency/4A/上市集团（150+ 人） |
|---|---|---|
| **体系框架** | 一页纸定位 + 3-5 条全公司 OKR，**跳过 BSC/多周期** [S023] | BSC 四视角 + 战略地图 + 多业务线×多周期×矩阵 [S007] |
| **工具** | Toggl/Clockify + 飞书多维表格手算 margin | agency PSA（Productive/Kantata）全栈 + 北森/Lattice + BI [S015] |
| **人效口径** | 整体 utilization + 人均毛利，由粗到细 [S013] | AGI/FTE、realization、LUBRM 逐杠杆诊断、组合级利润 [S001/S003] |
| **激励** | 团队奖金池(毛利 5-15%)为主、个人浮动为辅 [S027/S028] | 获取分享制 + 奖金包公式 + 事业合伙人/阿米巴/股权 [S036/S037/S008] |
| **考核** | 目标共识 + 轻校准 + GROW 面谈；**无强制分布** [S026] | PBC/军令状 + 正式校准会 + 分档应用 + 申诉；活力曲线仅干部层柔性 [S038/S024/S037] |
| **周期** | 季度 check-in + 半年面谈 | 季度 OKR + 年度考核 + 校准 [S020] |
| **最痛点** | 老板凭感觉、算不清项目赚不赚钱 → **先补工时/毛利数据** | 指标膨胀/校准政治/矩阵双线打架 → **减指标、立校准纪律** |
| **AIGC/下行** | 产能涨单价跌、现金紧 → 保毛利+非物质激励 | 大规模裁员(0.3%有机增长)、工时口径失真 → 转产出/结果考核 [S034/S032] |

### 最值得进 skill 的 playbook 清单（按"本行独有 + 高决策杠杆"排序）

1. **"对外定价决定对内考核"第一性检查**：搭绩效前先问"我们按工时卖还是按价值/产出卖？"——按工时卖就注定内部按工时榨（死亡螺旋）。修上游(定位→定价)优先于拧下游(考核) [S042/S004]。
2. **创意可量化三层拆分卡**：质量(专家评议/获奖,不上硬KPI) / 效率(工时/准时/返稿) / 结果(利润/ROAS/续约)——化解元矛盾的操作解，各岗位只是三层配比不同 [S018]。**master skill 招牌 figure。**
3. **人效核算装配顺序**：工时→utilization(agency~50-60%,别照搬律所)→realization(堵免费改稿漏)→项目利润→AGI/FTE；LUBRM 诊断"利润漏在哪个杠杆"，先提 rate 最后才逼 utilization [S013/S001/S016]。
4. **奖金分配三原则**：池=毛利 5-15%、70/30 偏团队、创意慎提成(提成仅 BD 且按毛利计基)；华为"获取分享制+奖金包×(1+效益改善率)+熔断"取机理不背书系数 [S027/S028/S037/S045]。
5. **校准会纪律**：证据驱动、HR 主持、防"嗓门大/职位高说了算"——跨组公平的命门 [S024/S019]。
6. **强制分布决策树**：只对干部层柔性用、给足 PIP/申诉缓冲、<10 人小组禁硬淘汰（最高法末位≠不胜任）[S044/S039]。
7. **Goodhart 反身检查（上KPI前必做）**：假想"这个数被挂高利害会怎么被 game"，能被轻易 game 的留给评议 [S011]。
8. **AIGC 考核 pivot**：显式下调工时/产量权重、上调价值/结果权重；可选 TrinityP3 记分卡(CPDA/HRI/ADIS)做过渡 [S032/S035]。
9. **回款入指标**：签单不计回款=虚假业绩+现金危机；AE/BD 必挂回款 [S030]。
10. **SOP 一图流**：0上游→1体系→2指标→3人效→4激励→5考核→6复盘 的装配线（含"不可倒装"警告）。

---

## 质量自检

- [x] **6 阶段全覆盖**：① 体系搭建 ② 分岗位指标 ③ 人效核算 ④ 激励分配 ⑤ 考核面谈 ⑥ 复盘迭代+反绩效——每阶段均含「小工作室/大 agency/近期变化(AIGC/经济下行)」三节。✓
- [x] **源数 ≥15**：**45 源**（T03-S001→S045），远超目标。bucket：verified_primary 13 / surrogate_primary 13 / secondary 13 / reference 3。**本次亲验 18 条(2026-07-02) + 继承 27 条(2026-06-18)**，last_checked 列已区分标注。✓
- [x] **每阶段「跳过哪步/优化点/额外动作」三类提示均出现**：Phase1(跳过BSC/优化拆创意/额外动作×3) · Phase2(跳过产量KPI/优化AE压力/额外动作AIGC) · Phase3(优化util口径/额外动作realization+分母) · Phase4(跳过创意提成/优化项目分成/额外动作非物质+计件) · Phase5(跳过强制分布/优化校准/额外动作折中+AI) · Phase6(优化Goodhart/额外动作上游+AIGC)。✓
- [x] **每节 1 案例带 [T03-S00X] evidence**：18 个子节各附案例(Perdoo试点/BSC/AMI/Adobe/Productive/TrinityP3/Parakeeto/Maister LUBRM/Farmer/Matchstick/华为奖金包/Enns 5步/LifeLabs/校准6步/索尼两面/Muller/Forrester 等)。✓
- [x] **矛盾保留**：量化 vs 反绩效主义(每阶段结尾)、提成 vs 协作(P4)、工时制 vs 员工健康(P3)、强制分布用不用(P5.3 双面)、项目分成公式化 vs 判断式(P4.2)、AI绩效话术 caveat(P5.4)。✓
- [x] **数字挂来源/caveat**：utilization 50-60%/65-80%/70-75%[S013/S003/S014]、奖金池 5-15%毛利[S027]、70/30[S028]、AGI/FTE≈$90K/营业利润≥15%(美国口径)[S003]、交付毛利60-70%AGI/营业利润25-35%[S013]、华为奖金包公式(培训口径分歧,不背书系数)[S037]、scope creep 15-30%[S031]、Forrester -15%[S033]、holdco 0.3%增长/Dentsu 16-17%利润率[S034]、GE 28×(倡导方口径)[S039]、TrinityP3 目标值(咨询倡导口径)[S032]、Farmer 24% fee(私有benchmark)[S041]——均标口径/caveat。✓
- [x] **黑名单合规**：0 条 LinkedIn 正文/知乎/公众号/百度/CSDN/简书/脉脉/g2/capterra/HR 内容农场。华为奖金包研究命中的 zhihu/360doc/keycourse/腾讯新闻转载已主动剔除，改用 对标考察网+MBA智库+《以奋斗者为本》书页(与 T01/04/06 同批 clean 源)。✓
- [x] **一手/二手标注**：每行 manifest 标 bucket；华为/索尼/中式工具均标"培训口径/二手/倡导方口径"caveat，取机理不背书。✓
- [⚠] **诚实边界**：① verified_primary 占比 29%（低于 50% 期望）——结构性：workflow 的落地手法/基准数字天然在 vendor docs(surrogate)与行业媒体(secondary)，方法论正典一手已全取到(13 条)；② TrinityP3 AI 记分卡目标值偏理想(咨询倡导)，作过渡框架用、非验证常量；③ 华为奖金包具体系数培训口径互相矛盾(80/160 向增量 vs 线性)，已标"取机理不背书系数"；④ 时效层(AIGC 冲击工时/产量考核、2025-2026 holdco 裁员)decay=high，须随 last_checked 更新。
