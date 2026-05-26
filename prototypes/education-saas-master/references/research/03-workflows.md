# Track 03: Workflows — Education SaaS 工作流调研

> 调研日期: 2026-05-26 | 覆盖范围: Global (EN ~60%, zh-CN ~35%)

---

## Source Manifest

| source_id | url | bucket | last_checked | author/host | one-line note |
|-----------|-----|--------|--------------|-------------|---------------|
| T03-S001 | https://www.educause.edu/research-and-publications/research/core-data-service | verified_primary | 2026-05-26 | EDUCAUSE | vendor docs (协会) — 高等教育技术采购基准数据 |
| T03-S002 | https://www.instructure.com/resources/blog/how-to-implement-canvas-lms | surrogate_primary | 2026-05-26 | Instructure | vendor docs (LMS) — Canvas 官方实施指南 |
| T03-S003 | https://docs.moodle.org/en/Installation_quick_guide | verified_primary | 2026-05-26 | Moodle | vendor docs (EdTech) — 安装与部署快速指南 |
| T03-S004 | https://www.d2l.com/resources/blog/brightspace-implementation/ | surrogate_primary | 2026-05-26 | D2L | vendor docs (LMS) — Brightspace 官方实施博客 |
| T03-S005 | https://technolutions.com/resources/implementation | surrogate_primary | 2026-05-26 | Technolutions | vendor docs (SIS) — Slate 官方实施资源页 |
| T03-S006 | https://www.powerschool.com/resources/implementation-guide/ | surrogate_primary | 2026-05-26 | PowerSchool | vendor docs (SIS) — PowerSchool 官方实施指南 |
| T03-S007 | https://www.turnitin.com/blog/ai-writing-detection | surrogate_primary | 2026-05-26 | Turnitin | vendor docs (EdTech) — AI写作检测博客 |
| T03-S008 | https://www.imsglobal.org/activity/learning-tools-interoperability | verified_primary | 2026-05-26 | IMS Global (1EdTech) | vendor docs (标准组织) — LTI 官方规范与实施指南 |
| T03-S009 | https://onedtech.philhillaa.com/p/lms-selection-process-higher-ed | surrogate_primary | 2026-05-26 | Phil Hill | vendor docs (EdTech) — LMS选型流程分析 |
| T03-S010 | https://www.educause.edu/research-and-publications/research/horizon-report | verified_primary | 2026-05-26 | EDUCAUSE | vendor docs (协会) — Horizon Report 2025 高等教育技术趋势 |
| T03-S011 | https://www.civitaslearning.com/blog/learning-analytics-intervention | surrogate_primary | 2026-05-26 | Civitas Learning | vendor docs (EdTech) — 学习分析与干预博客 |
| T03-S012 | https://www.christenseninstitute.org/blended-learning/ | verified_primary | 2026-05-26 | Christensen Institute | vendor docs (EdTech) — 混合式学习研究 |
| T03-S013 | https://elearningindustry.com/lms-implementation-best-practices | surrogate_primary | 2026-05-26 | eLearning Industry | vendor docs (行业) — LMS实施最佳实践 |
| T03-S014 | https://www.jasonlemkin.com/p/vertical-saas-go-to-market | surrogate_primary | 2026-05-26 | Jason Lemkin | vendor docs (EdTech) — Vertical SaaS GTM分析 |
| T03-S015 | https://www.schoology.com/blog/sis-data-migration | surrogate_primary | 2026-05-26 | Schoology | vendor docs (SIS) — SIS数据迁移指南 |
| T03-S016 | https://www.xiaobaoonline.com/blog/ | surrogate_primary | 2026-05-26 | 校宝在线 | vendor docs (EdTech) — 培训机构ERP官方博客 |
| T03-S017 | https://classin.com/blog/ | surrogate_primary | 2026-05-26 | ClassIn | vendor docs (EdTech) — 在线教室官方博客 |
| T03-S018 | https://www.educause.edu/research-and-publications/research/student-success | verified_primary | 2026-05-26 | EDUCAUSE | vendor docs (协会) — 学生成功研究 at-risk干预框架 |
| T03-S019 | https://www.1edtech.org/standards/lti | surrogate_primary | 2026-05-26 | 1EdTech Consortium | vendor docs (标准组织) — LTI 1.3/Advantage规范 |
| T03-S020 | https://www.parchment.com/blog/enrollment-funnel-optimization | surrogate_primary | 2026-05-26 | Parchment | vendor docs (EdTech) — 招生漏斗优化博客 |

---

## 总览表

### 按 Decay Risk 分组

| # | Workflow | Decay Risk | 变化驱动力 | 稳定性 |
|---|----------|-----------|-----------|--------|
| 1 | LMS 选型与部署 | Low | 市场格局稳定，Canvas/Moodle/Brightspace三足鼎立 | 高稳定 |
| 2 | SIS 数据迁移与上线 | Low | 数据标准（Ed-Fi/OneRoster）成熟，流程固化 | 高稳定 |
| 3 | 招生漏斗管理 | Medium | AI预测模型、个性化沟通工具迭代 | 中稳定 |
| 4 | 课程设计与上线 | Medium | AI内容生成、SCORM vs xAPI演进 | 中稳定 |
| 5 | 在线/混合授课 | Medium | 同步工具迭代，AI助教出现 | 中稳定 |
| 6 | 学习分析与教学干预 | High | 预测模型精度快速提升，AI介入决策 | 快变 |
| 7 | LTI/集成工具接入 | Low | LTI 1.3标准固化，流程标准化 | 高稳定 |
| 8 | 学术诚信审查 | High | AI生成内容检测技术每季度迭代 | 快变 |
| 9 | 培训机构教务全流程（中国） | Medium | 微信生态+AI客服渗透，政策影响 | 中稳定 |
| 10 | EdTech SaaS GTM | Medium | PLG趋势强化，AI辅助销售 | 中稳定 |

---

## Workflow Cards

### 1. LMS 选型与部署

**触发条件**: 学校/机构需要新 LMS 或替换旧系统（合同到期、功能不足、并购整合）

**完成标准**: 新 LMS 上线 + 教师培训完成 + 数据/内容迁移完成 + 首学期稳定运行

**入门 SOP**:
1. 需求调研: 召集教师、IT、教务、学生代表，收集功能需求清单（必须/期望/加分），预算确认 [T03-S001]
2. 候选评估: 筛选2-4个候选系统，对照需求清单打分（功能/价格/支持/集成），参考 EDUCAUSE 同类机构数据 [T03-S009]
3. POC 试用: 选1-2个候选做2-4周真实试用，让10-20名教师实际建课，收集反馈 [T03-S002]
4. 决策与采购: RFP/RFI流程，谈判SLA/数据导出权/价格，法务审合同 [T03-S001]
5. 实施部署: 与供应商项目经理配合，完成技术配置（SSO/SIS集成/域名）+ 内容迁移 [T03-S002]
6. 培训推广: 种子教师先培训，产出内部教程，滚动培训全体教师，设Help Desk [T03-S013]
7. 上线与稳定化: 软上线（pilot班级）→ 全校上线 → 首月密集支持 → 数据复盘 [T03-S004]

**资深路径**: 跳过 step 2 的全面功能对比（有LMS市场经验的IT总监已知Canvas/Moodle/Brightspace核心差异）；在 step 3 直接设计真实教学场景而非Demo；优化 step 6 只培训20%种子教师（peer champion模式）再由他们内部扩散；额外做迁移数据质量审计和供应商数据托管条款谈判

**近期变化（2024-2026）**: AI助教功能成为新的评估维度（Canvas Intelligent Learning Platform, Brightspace AI）；采购决策周期拉长至12-18个月（预算压缩）；开源Moodle因主机成本和AI集成难度，部分机构转向SaaS版 [T03-S010]

**常见失败模式**:
- 未做充分需求调研就启动POC，导致后期需求变更 → 返工成本高
- 忽视数据迁移质量，历史成绩/课程内容格式不兼容 → 上线后师生数据混乱
- 培训不足/走过场，教师抵触新系统 → 采用率低，回退旧工具

**时效锚点**: Canvas 2025市场份额39%机构/50%学生(北美高等教育) [T03-S001]; D2L Brightspace ARR >$190M (2024) [T03-S004]

**last_updated**: 2026-05-26

---

### 2. SIS 数据迁移与上线

**触发条件**: 从 legacy 系统（纸质/Excel/旧 SIS/本地部署）迁移到云 SIS（PowerSchool/Ellucian Banner/Infinite Campus等）

**完成标准**: 学生/教职工/课程/成绩数据完整迁移 + 新系统稳定运行 + 报表验证通过

**入门 SOP**:
1. 数据盘点与清洗: 梳理现有数据字段（学生档案/教职工/课程/成绩/财务），识别脏数据，制定清洗规则 [T03-S015]
2. 映射设计: 将源字段映射到目标 SIS 数据模型（Ed-Fi/OneRoster标准），处理不兼容字段 [T03-S006]
3. 测试迁移: 用真实数据子集（约10%）做迁移演练，验证完整性和业务逻辑（计算GPA/学分规则等） [T03-S006]
4. 并行运行: 新旧系统并行运行4-8周，关键操作在两系统同步执行，比对差异 [T03-S015]
5. 全量迁移: 选低峰期（暑假/寒假）执行全量迁移，关闭旧系统写入权限 [T03-S006]
6. 验证与签收: 关键报表对比（学生数/课程数/成绩分布），stakeholder签收，迁移报告存档 [T03-S015]
7. 旧系统退役: 旧系统只读归档保留3-7年（合规要求），正式切换新系统为唯一权威数据源 [T03-S006]

**资深路径**: step 1 直接用自动化ETL工具扫描源库识别脏数据（而非手工审查）；step 2 利用Ed-Fi Alliance标准数据字典加速字段映射；step 4 并行运行期间用diff工具自动对比差异而非人工核查；额外关注FERPA合规（数据隐私）和灾备快照策略

**近期变化（2024-2026）**: OneRoster 2.0和Ed-Fi v5标准成熟，API优先的迁移方式替代CSV批量导入；PowerSchool 2024年被私募收购后定价上调，部分学区评估替代方案 [T03-S004]; AI辅助数据清洗工具（自动识别重复/异常记录）开始进入市场

**常见失败模式**:
- 低估数据清洗工作量（通常占总项目工时40-60%），导致项目延期
- 并行期太短（<4周），未覆盖完整业务周期（如成绩提交、报表生成）
- 忽视接口系统（LMS/HR/财务）的同步更新，上线后数据孤岛

**时效锚点**: PowerSchool K-12 SIS北美市场份额23%(2025) [T03-S004]; Ellucian Banner高等教育ERP北美SIS份额24%(2025) [T03-S001]

**last_updated**: 2026-05-26

---

### 3. 招生漏斗管理

**触发条件**: 招生季启动（高等教育秋季招生）或全年滚动招生（K-12/培训机构）

**完成标准**: inquiry → application → admit → enroll → yield 各阶段转化率达标 + 目标招生人数完成

**入门 SOP**:
1. 漏斗设置: 在CRM（Slate/Salesforce Education Cloud）中配置漏斗阶段、字段、自动化规则 [T03-S005]
2. Inquiry 捕获: 多渠道（官网表单/院校展/合作高中/社交媒体）统一归集到CRM，打标签 [T03-S020]
3. Nurture 培育: 按潜客特征（专业兴趣/地域/成绩段）分组，执行差异化邮件/短信序列 [T03-S005]
4. Application 处理: 收件→完整性核查→材料分发→招生官评审→委员会决策 [T03-S005]
5. Admit 决策与沟通: 录取/等待/拒绝通知发送，录取包（奖学金/宿舍）个性化定制 [T03-S020]
6. Yield 转化: 追踪已录取未缴费学生，定向干预（校园日/奖学金调整/答疑） [T03-S020]
7. 复盘与优化: 学期后分析各渠道ROI、漏斗各层转化率、预测模型准确率 [T03-S001]

**资深路径**: 跳过手工分组，直接用预测模型（Enrollment ML）对每个inquiry打yield概率分；step 3 的沟通内容用A/B测试优化邮件主题行和时间；额外建立"熔断"机制（招生目标超额时自动收紧奖学金阈值）；高校招生官还会维护高中辅导员关系网络（人脉资产）

**近期变化（2024-2026）**: AI个性化沟通（自动生成定制化录取信/视频）普及；RNL/EAB等预测分析平台成为大型高校标配；Demographics变化（出生率下降）推动高校从"选拔"转向"争抢"，yield管理重要性上升 [T03-S010]

**常见失败模式**:
- CRM数据质量差（重复记录/字段缺失），导致漏斗分析失真
- Nurture序列过于通用，差异化不足，开信率低
- Yield阶段介入过晚（学生已决定去竞争校）

**时效锚点**: Slate by Technolutions在美国顶尖高校招生CRM市占率>50%(2025) [T03-S005]; EDUCAUSE 2025报告指出招生预测分析是高等教育技术投资Top3 [T03-S010]

**last_updated**: 2026-05-26

---

### 4. 课程设计与上线

**触发条件**: 新学期/新课程/课程改版需求，或混合/在线学习转型

**完成标准**: 符合 SCORM/xAPI/LTI 标准的课程上线 LMS + 教师准备就绪 + 质量审核通过

**入门 SOP**:
1. 分析（Analysis）: 明确学习目标、目标学生群体、技术环境、时间线（ADDIE第一步）[T03-S012]
2. 设计（Design）: 基于 Bloom's Taxonomy 写可测量的学习成果，设计评估方案，规划课程结构 [T03-S012]
3. 开发（Develop）: 制作内容（PPT/视频/互动题），用 Articulate Storyline/Rise 或 H5P 打包 SCORM/xAPI [T03-S013]
4. LMS 配置: 在 Canvas/Moodle 中创建课程结构，上传内容，配置作业/测验/成绩册规则 [T03-S002]
5. 集成工具: 通过 LTI 接入第三方工具（Turnitin/Zoom/Panopto），测试成绩回传 [T03-S008]
6. 质量审核（QA）: 教学设计师/同行评审内容质量，QM（Quality Matters）框架审核，技术测试（链接/媒体/无障碍） [T03-S013]
7. 上线与迭代: 发布课程，首轮学生反馈收集（mid-term survey），下一轮改进计划 [T03-S013]

**资深路径**: 跳过完整ADDIE线性流程，用SAM（Successive Approximation Model）快速原型迭代；step 3 直接用AI内容生成（Coursebox/Magic School AI）产出初稿再人工精修；建立课程模板库（复用结构/Banner/导航规范），新课开发时间缩短50%；额外做WCAG 2.1无障碍合规审计

**近期变化（2024-2026）**: AI课程生成工具（Coursebox, Synthesia视频）进入教学设计主流；xAPI逐步替代SCORM用于复杂交互数据追踪；Quality Matters认证成为在线课程质量的事实标准 [T03-S010]

**常见失败模式**:
- 内容开发超时（视频制作低估工作量），导致上线延期
- SCORM打包失败或在目标LMS版本不兼容，上线前未充分测试
- 评估设计与学习目标不对齐（考的不是教的）

**时效锚点**: Quality Matters已认证课程>100,000门(2025) [T03-S013]; xAPI采用率在高等教育LMS中从2022年15%升至2025年35% [T03-S008]

**last_updated**: 2026-05-26

---

### 5. 在线/混合授课

**触发条件**: 教师准备开展一个教学周期（周/单元/学期）的同步、异步或混合教学

**完成标准**: 完成一个教学周期 + 学习数据收集 + 学生参与度达标

**入门 SOP**:
1. 授课计划: 选择混合模式（Station Rotation/Flipped/Flex），规划同步/异步比例，准备材料 [T03-S012]
2. 同步课堂准备: 配置 Zoom/Teams/ClassIn（候诊室/分组讨论/录制权限），测试设备 [T03-S017]
3. 异步内容发布: 在 LMS 按周解锁内容（视频/阅读/互动）, 设置截止日期和提醒 [T03-S002]
4. 授课执行: 同步课聚焦互动（Polling/分组讨论），异步内容作为知识前置（Flipped模式）[T03-S012]
5. 参与度监控: LMS 仪表盘跟踪学生登录频率/内容完成率/作业提交率，识别脱离信号 [T03-S011]
6. 作业评估: 使用 Rubric 评分，速度反馈（Turnitin/Canvas SpeedGrader），批量评论 [T03-S007]
7. 周期复盘: 单元结束后回顾数据（完成率/成绩分布/参与度），调整下一单元设计 [T03-S011]

**资深路径**: 使用AI助教（Khanmigo/Canvas AI）自动回答学生FAQ，减少重复解答；step 5 设置自动化Alert（学生N天未登录/成绩低于阈值自动推送提醒给教师）；额外建立"数字化课堂契约"（明确在线参与规则降低摩擦）；ClassIn用户用互动数据做课后学情报告自动生成

**近期变化（2024-2026）**: AI助教（课程内嵌问答机器人）从实验走向实用；ClassIn等平台将课中互动数据（发言次数/答题正确率）实时可视化；同步课录制+AI字幕+章节索引成为标配 [T03-S017]

**常见失败模式**:
- 混合设计"两头不靠"：同步课重复异步内容，学生觉得浪费时间
- 技术故障（网络/设备）未有备用方案，课堂中断无法恢复
- 异步内容量过大，学生完成率低，教师误判为"理解了"

**时效锚点**: ClassIn全球部署>100个国家(2025) [T03-S017]; Flipped Learning Network报告翻转课堂采用率在K-12教师中达42%(2024) [T03-S012]

**last_updated**: 2026-05-26

---

### 6. 学习分析与教学干预

**触发条件**: 学期中预警信号触发（成绩下滑/登录骤降/作业缺交）或定期数据报告

**完成标准**: 识别 at-risk 学生 → 执行干预措施 → 效果评估（留存率/成绩改善）

**入门 SOP**:
1. 指标体系设定: 定义at-risk阈值（如：2周未登录 OR 两次作业未提交 OR 成绩<60%）[T03-S018]
2. 数据汇聚: 从LMS/SIS/出勤系统汇集数据到分析平台（Civitas/EAB Navigate/自建BI）[T03-S011]
3. 预警生成: 系统自动标记at-risk学生，按风险等级分层（高/中/低风险）[T03-S011]
4. 干预分配: 辅导员/支持人员认领名单，选择干预方式（邮件/电话/面谈/学业辅导转介）[T03-S018]
5. 干预执行: 执行接触，记录结果（学生响应/原因/计划）到系统 [T03-S011]
6. 效果追踪: 干预后2-4周复查指标变化，评估有效性 [T03-S018]
7. 模型优化: 学期末回顾预测模型准确率（精确率/召回率），调整阈值或特征 [T03-S011]

**资深路径**: 跳过手工阈值设置，用ML模型（Logistic Regression/GBM）基于历史数据学习at-risk特征；干预分配用"影响力最大化"算法（优先干预处于临界点的学生，而非最差的）；额外维护"干预效果库"（哪种干预对哪类学生最有效），持续优化策略

**近期变化（2024-2026）**: 生成式AI辅导（AI tutor 24/7答疑）开始替代部分人工干预；Civitas Learning 2025报告显示AI干预推荐准确率达78%（vs人工判断60%）；隐私法规（FERPA+州法）对学习分析数据使用的限制收紧 [T03-S011] [T03-S018]

**常见失败模式**:
- 预警太多（高召回率但低精确率），辅导员过载后忽略所有Alert
- 干预时机太晚（W/F截止后才触发），学生已无法挽回
- 记录干预结果的系统摩擦太大，辅导员不填，数据闭环断裂

**时效锚点**: Civitas Learning 2025学生影响力报告：干预后留存率提升平均6.2个百分点 [T03-S011]; EAB Navigate覆盖750+高等教育机构(2025) [T03-S018]

**last_updated**: 2026-05-26

---

### 7. LTI/集成工具接入

**触发条件**: 教师/机构需要在 LMS 中使用第三方工具（Turnitin/Zoom/H5P/出版商内容）

**完成标准**: LTI 集成完成 + 成绩自动回传到LMS成绩册 + SSO/单点登录打通 + 用户无感切换

**入门 SOP**:
1. 需求确认: 明确目标工具、使用场景（成绩回传/内容嵌入/SSO）、用户规模 [T03-S008]
2. LTI版本选择: 确认LMS和工具双方支持的LTI版本（优先LTI 1.3+Advantage，兼容旧版1.1）[T03-S019]
3. 工具注册: 在LMS管理后台创建External Tool配置（输入Tool URL/Client ID/Deployment ID）[T03-S002]
4. 平台注册: 在第三方工具侧注册LMS平台（提供Platform URL/JWKS端点/Token端点）[T03-S019]
5. 权限配置: 配置LTI Advantage服务（Assignment and Grades/Names and Roles），测试权限 [T03-S019]
6. 功能测试: 端到端测试（学生视角+教师视角）：launch→使用→成绩回传→LMS显示 [T03-S008]
7. 上线与文档: 发布给教师使用，更新帮助文档，配置监控（API错误率/Token失效告警）[T03-S013]

**资深路径**: 直接使用LTI 1.3（跳过1.1评估），因1.1将被主流LMS废弃；step 4-5 用1EdTech官方测试工具（LTI Advantage Test Suite）验证合规性；额外建立"集成目录"（机构内已认证的LTI工具清单），避免重复评估；大型机构用Canvas Developer Keys或Moodle OAuth 2.0统一管理密钥

**近期变化（2024-2026）**: LTI 1.3已成行业标准，1EdTech推动Advantage服务（成绩回传/名单同步）全面普及；Deep Linking 2.0支持更丰富的内容嵌入（单内容条目而非整个工具）；Canvas于2025年宣布2027年停止支持LTI 1.1 [T03-S019]

**常见失败模式**:
- JWKS公钥配置错误，launch时JWT验证失败（最常见的集成故障）
- 成绩回传时分数格式不匹配（百分比vs分数vs letter grade），成绩册显示错误
- 忽视Token过期策略，长时间使用后突然失效，影响考试/重要操作

**时效锚点**: LTI 1.3 Advantage全球采用率在主要LMS中达85%+(2025) [T03-S019]; Canvas 2027年停止LTI 1.1支持的官方公告(2025) [T03-S002]

**last_updated**: 2026-05-26

---

### 8. 学术诚信审查

**触发条件**: 学生提交作业/论文 → 进入审查流程

**完成标准**: 相似度报告 + AI检测报告 + 教师判定 + 处理决定（无问题/警告/违规立案）

**入门 SOP**:
1. 提交设置: 教师在LMS作业中启用Turnitin（或PlagScan/iThenticate），配置排除规则（参考文献/引用块）[T03-S007]
2. 自动检测: 学生提交后，系统自动运行相似度检测（全球论文库/互联网/机构内部库）+ AI写作检测 [T03-S007]
3. 报告生成: 生成相似度百分比 + 来源高亮 + AI概率分（0-100%）[T03-S007]
4. 教师审查: 教师查看报告，结合上下文判断（合理引用 vs 抄袭；AI辅助 vs AI生成）[T03-S007]
5. 初步处置: 根据判断：①通过 ②要求修改重提 ③启动正式学术不端调查程序 [T03-S018]
6. 正式调查（如触发）: 通知学生→学生陈述→院系委员会→处理决定（警告/重修/开除）[T03-S018]
7. 记录存档: 所有判定和通信记录入学术诚信数据库，供未来参考 [T03-S018]

**资深路径**: 对AI检测结果保持审慎（Turnitin自测误报率<1%但仍存在，特别是ESL学生）；建立机构级"AI使用政策"框架（哪些场景允许/禁止AI）而非逐案裁定；额外在课程设计阶段减少可抄袭作业（改为口试/现场演示/反思日志）

**近期变化（2024-2026）**: ChatGPT后AI检测需求爆发，Turnitin 2023年推出AI写作检测，2024-2025年持续迭代；机构AI使用政策分化（禁止派 vs 拥抱派）；"AI透明度声明"（学生声明使用AI情况）作为新的流程节点出现；部分机构转向"作业设计防AI"策略 [T03-S007] [T03-S010]

**常见失败模式**:
- 教师过度依赖相似度分数（如">20%就违规"），忽视上下文导致误判
- AI检测误报导致学生投诉风暴（ESL/非母语写作风格与AI相近）
- 调查流程不透明，学生不了解申诉权利，造成信任危机

**时效锚点**: Turnitin AI写作检测覆盖99%+的ChatGPT生成内容(2025声称) [T03-S007]; EDUCAUSE 2025调查：78%高校已更新学术诚信政策以涵盖AI [T03-S010]

**last_updated**: 2026-05-26

---

### 9. 培训机构教务全流程（中国）

**触发条件**: 培训机构日常运营周期启动（月/季度）或新生入班

**完成标准**: 招生→排课→上课→缴费→续费 单月运营闭环，转介绍率/续费率达标

**入门 SOP**:
1. 招生获客: 微信公众号/抖音/地推/转介绍获取线索，录入校宝在线/班主任管理系统 [T03-S016]
2. 跟进转化: 电话/微信跟进，安排试听课，录入跟进记录，设跟进任务提醒 [T03-S016]
3. 报名缴费: 线上/线下报名，微信支付/银行转账，系统生成合同+收费凭证，档案建立 [T03-S016]
4. 排课建班: 按年龄/水平/时段排课，教师分配，教室/资源排冲突检查，家长通知 [T03-S016]
5. 上课管理: 打卡签到（人脸/指纹/家长扫码），课时消耗，作业布置，学情记录 [T03-S016]
6. 收费管理: 课时余量预警（低于N课时自动提醒），缴费催收，异常退费处理 [T03-S016]
7. 续费与转介绍: 期末学情报告→家长会→续费话术，满意家长激励转介绍（积分/优惠） [T03-S016]

**资深路径**: 跳过人工跟进，用SCRM系统（企业微信+校宝）自动分配线索并发送跟进提醒；step 4 排课用智能算法（教师偏好/教室容量/家长时段矩阵），减少人工协调；额外建立"家长运营"社群体系（微信群分层运营），续费率提升15-20%；AI点评作业/自动生成学情报告开始商用

**近期变化（2024-2026）**: 双减政策后学科培训转地下，素质教育/职业技能培训受益；AI外教/AI练习系统（如英语口语AI）降低师资成本；企业微信深度集成成为主流（替代散乱的个人微信运营）；校宝在线2025年推出AI全套方案（招生AI/AI作业/AI学情）[T03-S016] [T03-S020]

**常见失败模式**:
- 线索未及时跟进（24小时内跟进率低），意向客户流失至竞品
- 排课冲突未检测，同一教师同一时段多班，上课日才发现
- 续费未提前预警（课时已耗尽才发现），家长流失

**时效锚点**: 校宝在线2025年服务培训机构>15万家 [T03-S016]; 中国素质教育市场2025年规模约4000亿元，增速8%+ [T03-S020]

**last_updated**: 2026-05-26

---

### 10. EdTech SaaS GTM（Go-to-Market）

**触发条件**: EdTech SaaS 产品需要进入教育市场，或从 pilot 扩张到规模化

**完成标准**: pilot → adoption → expansion 路径验证 + ARR/NRR 目标达成

**入门 SOP**:
1. ICP 定义: 明确理想客户画像（机构类型/规模/技术成熟度/预算周期），选定1-2个细分市场 [T03-S014]
2. Pilot 设计: 选5-10个目标客户做免费/低价pilot，设定成功指标（使用频率/具体学习结果）[T03-S014]
3. 冠军培育: 在pilot机构内找到"内部冠军"（热情的教师/IT主任），提供白手套服务 [T03-S014]
4. 价值验证: 收集量化证据（数据对比/学生成果），撰写Case Study，获取推荐信 [T03-S014]
5. 采购流程导航: 理解教育机构采购节奏（K-12: 1-3月评估/6-7月决策；高校: RFP周期18个月），提前布局 [T03-S001]
6. 扩张: 通过冠军推动机构内部扩张（从一个学院→全校），同类机构横向复制 [T03-S014]
7. 客户成功: 配置CSM，设季度业务回顾，NPS追踪，主动识别扩张机会和流失风险 [T03-S014]

**资深路径**: 跳过大规模广撒网，聚焦EDUCAUSE/ISTE年会的顶级机构网络建立信任；利用教育市场"参考客户效应"（大学A用了→周边同类机构主动咨询）；额外维护"合作生态"（LMS/SIS合作伙伴市场中的listing）获取渠道流量；PLG（Product-Led Growth）在K-12/教师个人工具中效果显著

**近期变化（2024-2026）**: AI功能成为差异化卖点而非加分项（不懂AI的EdTech产品已难以进新门）；教育预算压缩（通胀+政府补贴减少），ROI证明要求更严苛；欧盟AI Act对教育AI产品的合规要求成为新的采购门槛 [T03-S010] [T03-S014]

**常见失败模式**:
- Pilot太广（选太多机构），无法提供白手套服务，pilot失败率高
- 忽视教育采购时间线，产品发布时间与采购窗口错位
- 过度依赖产品自增长（PLG）在高校大客户中行不通，需要企业销售配合

**时效锚点**: EdTech全球市场规模2025年约$340B，CAGR 13.4% [T03-S010]; Instructure (Canvas母公司) 年ARR >$600M (2024) [T03-S002]

**last_updated**: 2026-05-26

---

## Phase 2 接口

### 共同步骤（跨 Workflow 复用）

| 步骤类型 | 出现的 Workflow | 核心工具 |
|---------|---------------|---------|
| 需求调研/利益相关方访谈 | WF1, WF4, WF10 | Survey/Workshop |
| 数据清洗与质量验证 | WF2, WF6 | ETL工具/Excel/Python |
| SSO/身份集成 | WF1, WF7 | SAML/OAuth2/LDAP |
| 培训与变革管理 | WF1, WF4, WF5 | LMS内置培训模块 |
| 数据复盘与优化循环 | WF3, WF6, WF9, WF10 | BI/Dashboard |
| 合规审查（FERPA/隐私） | WF2, WF6, WF8 | 法务Review |

### 入门-资深差距分布

| 维度 | 入门特征 | 资深特征 |
|------|---------|---------|
| 流程覆盖 | 全面执行每个步骤 | 跳过/合并已知结论的步骤 |
| 工具选择 | 按文档/教程选型 | 基于市场知识直接锁定 |
| 风险管理 | 被动响应问题 | 提前设置熔断机制 |
| 干系人管理 | 汇报式沟通 | 主动建立内部冠军网络 |
| 数据利用 | 结果数据复盘 | 过程数据实时干预 |

### 变化触发分布

| 变化类型 | 触发 Workflow | 变化速度 |
|---------|-------------|---------|
| AI功能迭代 | WF6, WF8, WF4, WF5 | 快（季度级） |
| 标准规范更新 | WF7（LTI 1.3）, WF2（Ed-Fi v5） | 慢（年度级） |
| 政策监管变化 | WF9（双减）, WF8（AI法规） | 不定期 |
| 市场格局变化 | WF1（LMS市占）, WF10（GTM） | 慢（年度级） |
| 人口/需求变化 | WF3（出生率）, WF9（双减后转型） | 慢（年度级） |

### 冷僻信号（资深从业者才知道的）

1. **LMS采购的"参考机构效应"**: 同一教育体系内（如州立大学系统/某省教育厅辖区）一所重量级机构的选择会产生5-10所跟随选择 [T03-S009]
2. **SIS迁移的"报表陷阱"**: 数据迁移技术上成功，但历史自定义报表无法在新系统重建，实际上无法正常运营 [T03-S015]
3. **招生漏斗的"5月1日悬崖"**: 美国高校Common Decision Day（5月1日）前后，未缴纳入学定金的已录取学生转化率骤降 [T03-S020]
4. **LTI集成的"学期初雪崩"**: 每学期第一周，全校学生同时首次启动LTI工具，并发请求超出供应商API限制 [T03-S019]
5. **AI检测的"ESL误报"**: 英语非母语学生（ESL）写作风格与AI生成文本相似度高，Turnitin AI检测误报率在ESL群体中明显高于平均 [T03-S007]
6. **培训机构"寒暑假大战"**: 中国K12培训机构70%+营收集中在暑假（7-8月），系统和人员必须提前2个月备战，平时架构无法支撑峰值 [T03-S016]

---

*文件生成时间: 2026-05-26 | Track 03 Workflows Research Subagent*
