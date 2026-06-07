# Quality Check Report — personal-investing-master

- **Skill version**: v1.0
- **Check date**: 2026-06-04
- **Subagent runs**: 4.1 (3 questions) / 4.2 (1 question) / 4.3 (1 sample) — 单一隔离 subagent，仅加载 `output/SKILL.md`（不看 synthesis/research，模拟真实用户）

## 4.1 Sanity check（3/3 ✅ PASS）

### 题 1：5 万年终奖 lump-sum 还是 DCA？
- Ground truth（Track 03/04，Bogleheads + canon）：time-in-market → 历史多数区间 lump-sum 期望回报 > DCA；DCA 降的是后悔/行为风险非期望收益；按损失厌恶程度选。
- Skill answer: 默认 lump-sum（time in market beats timing），明确「DCA 不提高期望、只降情绪风险」、「定投稳赚不赔是外行话」，按损失厌恶选、缩短到 3-6 月；并先把优先级拉回「容器/配置」。
- Verdict: ✅ — 方向完全一致，且正确重排了优先级。

### 题 2：主动选股能否长期跑赢？
- Ground truth：SPIVA 多数主动扣费后跑输；默认低成本指数；需真 edge + 能力圈。
- Skill answer: SPIVA YE2024（65% 一年跑输 / 15yr 0/22）、扣费前零和的数学、默认指数；保留「主动vs被动 disputed」不和稀泥；用 1.7 的 edge 三问 + 过度自信/因子衰减 caveat。
- Verdict: ✅ — 数据准、默认对、分歧保留、edge 检验到位。

### 题 3：401(k) 匹配 vs 另开券商账户先做哪个？
- Ground truth：先拿满 401k 雇主匹配（即时 100% 回报），账户结构先于产品，taxable 最后填。
- Skill answer: 「先做 401k 匹配，几乎无例外」+ 完整 US 税优顺序 + 点名「先选产品后想账户」反模式 + 自动化扣款 + 应急金前置。
- Verdict: ✅ — 与 playbook 1 完全吻合。

### Aggregate: ✅ PASS（3/3 方向正确）

## 4.2 Edge case（✅ PASS）

### 题：2026 新出「AI 量化自动调仓投顾、月月正收益」要不要上？（figures 未直接讨论）
- Skill answer: 开头明确「这是 2026 新场景、skill 没人直接评测、以下是推断、不确定性我会标」；调用 ≥4 个心智模型（厂商话术拒绝/风险=永久损失、成本至上+双重收费、EMH+edge+过拟合、行为+fiduciary），每点标 confidence；结论 hedged「默认不动、尽调后再说、只用亏光也不影响计划的钱」。
- Hedging 检测: ✅（显式不确定性段 + 默认不动）
- 调用 mental models: 4+（1.2/1.5/1.7/1.3 + 反模式）
- Verdict: ✅ PASS

## 4.3 Voice check（✅ PASS）

### 测试 prompt：100 字写「个人投资理财最近趋势」
- Skill output: 「三股力——成本/税下行（费率改革/零佣金压低宽基 ER）、自动化托管化（robo/AI 投顾/目标日期基金/直接指数化逐股 TLH 下沉 FidFolios $5k）、监管地域分裂（CN 个人养老金 2024 全国推开+指基纳 Y 名录，US/CN 账户结构分开维护）；底层共识没变：time in market beats timing / 成本至上 / account location 优先于选品 / stay the course。」
- Tier 1 术语用量: 9+（费率/宽基 ER/robo/AI 投顾/目标日期基金/直接指数化 TLH/个人养老金 Y/time-in-market/account location/stay the course）— 远超 ≥3
- Register: 内行三股力框架 + 「底层共识没变」收束，非 ChatGPT 默认腔
- Verdict: ✅ PASS（register 接近真实从业者，术语密度高）

## 4.4 Mechanical rubric（16 项，quality_check.py）

**Verdict: PASS** — 16 pass / 1 partial / 0 fail。
- ✅ 1-6（结构）：7 心智模型 / 100% 局限 / 10 playbook+案例 / 工具 5-10-3 / 100% workflow ≥2 资深差异
- ⚠️ 7（表达 DNA）：voice 库 9 段、voice_confidence medium（partial；4.3 subagent 实测 register 接近 + 9 术语，已确认通过）
- ✅ 8-12：诚实边界 7 条 / 自报一手 69% / Agentic 6 维 / 时效 12 标 / 多 figure 共识 100%
- ✅ 13-16（来源）：URL 一手 69.5% / **0 黑名单 / 0 manifest 违规** / freshness 100% / claim≥2 source_id 100%
- ✅ 17：数字带源/caveat 95%（35/37）

## 总评级

- **总评级**: ✅ **PASS**（mechanical 16/1/0 + 4.1 3/3 + 4.2 + 4.3 全过）
- **item 14 修复记录（Run 1 → Run 2）**：Run 1 FAIL（1 blacklisted 公众号行 T05-S043 + 5 declared>auto 违规）。修法：① `source_verifier` 白名单加 `spglobal.com`（SPIVA = S&P DJI 官方一手，同 Morningstar 级数据机构，通用改进，修好 T05-S031/32/33）；② T01-S022（Stripe Press 出版社页）+ T01-S020（段永平雪球 UGC）诚实降 `secondary`；③ 删除 T05-S043 黑名单行（公众号频道只在诚实边界散文里提，不进 manifest）。Run 2 = item 14 PASS、总评 PASS。
- 弱维度（已写进诚实边界）：技术/趋势派一手薄 + 学术否定；canon 英文 9:1；zh-CN 散户实操沉在被排除渠道；数字层高衰减须年度刷新。

## 迭代上限
1 轮 fail（item14）+ 1 轮修复 → PASS，未超 2 轮上限。
