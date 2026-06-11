# Quality Check Report — enterprise-b2b-sales-master

- **Skill version**: v1.0 (initial distill)
- **Check date**: 2026-06-11
- **Subagent runs**: 4.1 (3 questions) / 4.2 (1 question) / 4.3 (1 sample) — 全部独立 opus subagent,只加载 `output/SKILL.md`,未触 references/research(隔离确认:subagent 自报 + 工具调用清单核对)

## Run 1 (2026-06-11)

## 4.1 Sanity check

### 题 1: 高级经理喜欢我们 + demo 反馈好 + 「今年应该会买」,能进 commit 吗?
- Ground truth (Track 04/03, source: T04-S008/S009/S024 + W7): 不能。happy ears 反模式;commit = 证据归类(EB named & engaged / champion tested / decision & paper process 走查 / 痛点量化),「喜欢我们的高级经理」未经测试只是 coach。
- Skill answer: 「直说,不能进 commit。你现在掌握的全是 happy ears……commit 靠证据不靠心情,标准是这单你能不能说出名字(EB 是谁、champion 测试过没、paper process 走查没)」[full in /tmp/quality-check/sanity-answers.md]
- Verdict: ✅
- Reasoning: 方向、术语、纪律标准与 ground truth 完全一致,还主动补了 multithread 检查。

### 题 2: rep 学 Challenger 后当面反驳客户 VP 战略判断翻车,Challenger 不适合我们?
- Ground truth (Track 04, source: T04-S004/S032 + T06 外行破绽 #7): 不是方法论错,是执行错——constructive tension(基于 commercial insight 的 reframe)≠ argumentative;同时应保留「Challenger 执行难度高 + CEB 数据 contested」的批判,不银弹化。
- Skill answer: 「不是 Challenger 不适合你们,是这位 rep 把它做错了——把 challenge 当成『怼客户』……Teach-Tailor-Take control,用商业洞见 reframe……」并引「B2B 忠诚最大驱动是销售体验本身」,同时标注 CEB 数据 contested。[full in /tmp/...]
- Verdict: ✅
- Reasoning: 命中误用辨析 + 双面批判都保留,无银弹叙事。

### 题 3: 早期客户要求先做 POC 再谈商务,SE 紧张,怎么处理?
- Ground truth (Track 03, source: T03-S012 + W4): success-criteria-first——无共签书面 success criteria + 时间盒不启动;把 criteria 谈判当资格测试;未 qualify(EB/pain)的单不配 POC。
- Skill answer: 「先把这个 POC 请求当成一次资格测试……没有共签的书面 success criteria 与时间盒,就不启动 POC。没锁 criteria 的 POC 会变成无限期免费咨询,平均拖六到八周……」[full in /tmp/...]
- Verdict: ✅
- Reasoning: 与 W4 资深路径逐点一致(含耗时 caveat 的转述)。

### Aggregate: ✅ PASS (3/3)

## 4.2 Edge case

### 题: 工业设备预测性维护 SaaS($80K ACV / 6-9 月周期 / 多部门买方)想 (a) AI agent 完全替代 SDR (b) AI 自动填 MEDDPICC 让 reps 不做 qualify
- Skill answer: 「两个决定共享同一个底层错误:把 AI 当成『创造销售动作』的东西……(a) 『完全替代』这个量词不靠谱……(b) 危险,会直接踩头号败因 box-checking theater……」[full in /tmp/quality-check/edge-answer.md]
- Hedging 检测: ✅ — TCPA circuit split「须复核至今日判例」、合规「按目标地域逐一核」、AI 工具层「decay high,买前先 pilot,别签长约」、给出可辩护中间态而非二元结论。
- 调用 mental models: 4 个 — 1.7(工具放大动作)、1.5(资格纪律/打勾剧场)、1.3(multithread 委员会)、playbook #8(signal-based + 合规闸)。
- Verdict: ✅ PASS — ≥2 模型显式调用 + 显式 hedging,零编造,且把「AI 增强精瘦 SDR 层」的杠杆中间态推理出来(非 SKILL.md 逐字内容,是模型生成力的正向证据)。

## 4.3 Voice check

### 测试 prompt: 「写 100-150 字同行向短评:2026 年年中 AI 在 enterprise sales 的真实处境」
- Skill output: 「2026 年年中,AI 在 enterprise sales 里早过了『全自动外呼』的泡沫期。去年那波 AI SDR 群发把大家的 deliverability 打穿……量是送达率的敌人……工具放大动作不创造动作……AI 帮你填满八个字段不等于真 qualify,那还是打勾剧场,EB 是谁、champion 测过没,机器替不了。signal-based 那套少而准才是正道。」(~145 字)
- Reference samples (3 段真实从业者): T01-S009 McMahon verbatim(流程纪律 register)/ T05-S002 30MPC newsletter 近期 issue(战术直给 register)/ T04 canon 现代正典段(方法论引用 register)。
- Tier 1 术语用量: 8 个(deliverability / AI SDR / auto-MEDDPICC / qualify / 打勾剧场 / EB / champion / signal-based),target ≥ 3 ✓
- 厂商话术拒绝: 1+(「没人再信『一天两千封不用人工』」= AI 全自动 outbound 银弹话术的显式拒绝)✓
- Register 接近度: ✅ — 短句直给、黑话密度高、自带怀疑层(「交了学费」),无 "In summary" 类 ChatGPT 默认句式、无 bullet、无外行 tell。
- Verdict: ✅ PASS

## 4.4 Mechanical rubric (17 项, iter 27)

`tools/research/quality_check.py check --skill-dir prototypes/enterprise-b2b-sales-master/output` → **17 pass / 0 partial / 0 fail**(首轮)。

亮点项: item 7 voice samples 15 entries / 9 原话 (60%) → voice_confidence **high**;item 13 manifest first-hand 194/229 = 84.7%;item 14 零黑名单零违规;item 17 数字 caveat 10/10 = 100%。

不通过项数: 0

## 总评级

- **总评级**: ✅ **PASS**(首轮,无迭代)
- 修复建议: 无。候选改进(非阻塞):Track 05 发现的 Andy Paul(反教条席位)可在未来 update 轮补入 figures。

## 迭代次数: Run 1 即 PASS
