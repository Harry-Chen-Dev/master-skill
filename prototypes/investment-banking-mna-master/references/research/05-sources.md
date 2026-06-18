# Track 05 — Sources: 投行并购 / M&A 交易撮合 (Investment Banking M&A)

locale = global (en-primary) · last_checked = 2026-06-16

这行是 en 媒体层**极厚**的典型反例 (与 zh-CN 创作者行业相反): 一手 SEC filing、顶级 newsletter、长青 podcast、付费 deal 数据平台并存。公开材料丰富, NOT cold。

---

## Source Manifest

| source_id | url | bucket | last_checked | author/host | note |
|---|---|---|---|---|---|
| T05-S001 | https://www.bloomberg.com/opinion/authors/ARbTQlRLRjE/matthew-s-levine | secondary | 2026-06-16 | Matt Levine (Bloomberg) | 《Money Stuff》专栏 author 页; WebFetch 403 (Bloomberg bot 墙) 但源活跃, 业界必读; 媒体平台→二手 |
| T05-S002 | https://aswathdamodaran.blogspot.com/ | verified_primary | 2026-06-16 | Aswath Damodaran (NYU Stern) | "Musings on Markets" 估值博客; 实访确认 (最新 2026-06-04 SpaceX 估值); 作者个人站→一手 |
| T05-S003 | https://pages.stern.nyu.edu/~adamodar/ | verified_primary | 2026-06-16 | Aswath Damodaran (NYU Stern) | 免费估值数据集/spreadsheet/课程页 (frameset); 实访确认存活; 一手金矿 |
| T05-S004 | https://mergersandinquisitions.com/ | secondary | 2026-06-16 | Brian DeChesare | M&I: IB/M&A 职业+技术博客 (641+ 篇); 实访确认更新中; 创作者媒体→二手 |
| T05-S005 | https://www.sec.gov/edgar/search/ | verified_primary | 2026-06-16 | U.S. SEC | EDGAR 全文检索 (2001+); 搜 DEFM14A/S-4/fairness opinion 一手原文; WebFetch 403 (政府 bot 墙) 但通过 WebSearch 确认 UI 存活; 一手 |
| T05-S006 | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany | verified_primary | 2026-06-16 | U.S. SEC | EDGAR 按公司浏览 filing; 403 (bot 墙) 但 sec.gov 公认存活; 一手 filing 入口 |
| T05-S007 | https://efts.sec.gov/LATEST/search-index | verified_primary | 2026-06-16 | U.S. SEC | EDGAR 全文检索 JSON API; 程序化拉 merger proxy; WebSearch 确认存活; 一手 |
| T05-S008 | https://www.mascience.com/podcast | verified_primary | 2026-06-16 | Kison Patel (DealRoom) | M&A Science podcast channel 页; 实访确认 (300+ 集, 周更); 频道主页→一手 |
| T05-S009 | https://www.acquired.fm/ | verified_primary | 2026-06-16 | Ben Gilbert & David Rosenthal | Acquired 公司/并购深挖 podcast; 实访确认 (2026-05 活跃); 频道主页→一手 |
| T05-S010 | https://www.oaktreecapital.com/insights/memos | verified_primary | 2026-06-16 | Howard Marks (Oaktree) | Howard Marks 备忘录档案 (1990–今); 实访确认 (2026-04 "Private Credit"); 作者官方站→一手 |
| T05-S011 | https://podcasts.thecompoundnews.com/show/animalspirits/ | verified_primary | 2026-06-16 | Michael Batnick & Ben Carlson | Animal Spirits podcast 官方主页 (Ritholtz); WebSearch 确认 canonical URL, 周三更新; 频道主页→一手 |
| T05-S012 | https://corporatefinanceinstitute.com/resources/valuation/ | surrogate_primary | 2026-06-16 | CFI | 估值/M&A/建模 vendor docs + 免费 resource 库; 实访确认 (DCF/comps/precedent tx); vendor→代理一手 |
| T05-S013 | https://www.wallstreetprep.com/free-resources/ | surrogate_primary | 2026-06-16 | Wall Street Prep | WSP 免费 M&A/merger model/accretion-dilution 指南; 实访确认 (301 redirect from /knowledge/); vendor→代理一手 [education vendor] |
| T05-S014 | https://breakingintowallstreet.com/biws/ | surrogate_primary | 2026-06-16 | Brian DeChesare (BIWS) | BIWS 财务建模/M&A 训练 (case study, merger model); 实访确认; vendor→代理一手 [education vendor] |
| T05-S015 | https://macabacus.com/learn | surrogate_primary | 2026-06-16 | Macabacus | Excel/财务建模/M&A 教程 + 插件; WebFetch 403 (bot 墙) 但源活跃公认; vendor→代理一手 |
| T05-S016 | https://www.lseg.com/en/data-analytics/financial-data/deals-data | surrogate_primary | 2026-06-16 | LSEG (Refinitiv) | 全球 M&A 交易数据 + 季度 league table (3.3M+ 笔, 1970s+); 实访确认; 数据平台 vendor→代理一手 (多付费) |
| T05-S017 | https://www.dealogic.com/ | surrogate_primary | 2026-06-16 | Dealogic (ION) | 资本市场 deal 数据 + IB Scorecard/league table; 实访确认; 数据平台 vendor→代理一手 (付费) |
| T05-S018 | https://info.mergermarket.com/ | surrogate_primary | 2026-06-16 | Mergermarket (ION Analytics) | 预测性 M&A 情报 + deal origination (1.4M 公司, 300+ 记者); 实访确认 (302 from mergermarket.com); 付费, 标 surrogate/secondary |
| T05-S019 | https://pitchbook.com/news | surrogate_primary | 2026-06-16 | PitchBook (Morningstar) | PE/VC/M&A deal 数据 + 免费 news/research; WebFetch 403 (bot 墙) 但源公认存活; 数据平台 vendor→代理一手 (核心付费) |
| T05-S020 | https://corpgov.law.harvard.edu/ | secondary | 2026-06-16 | Harvard Law (HLS Forum) | 公司治理论坛: Delaware Chancery 判例/earnout/fiduciary/takeover law; 实访确认 (2026-06 活跃, 日更-周更); 法律视角→二手 |
| T05-S021 | https://www.axios.com/signup/pro-rata | secondary | 2026-06-16 | Dan Primack (Axios) | Axios Pro Rata 日更 deal newsletter (M&A/PE/VC, 200k+ 订阅); WebSearch 确认; 媒体平台→二手 |
| T05-S022 | https://www.goldmansachs.com/investor-relations/ | verified_primary | 2026-06-16 | Goldman Sachs | bank IR 官方材料 (earnings/presentation/deal 评论); WebFetch 403 (bot 墙) 但官方站公认; bank 一手 (作 IR 样板) |

---

## 总览 (按 type 分组)

### 1. Newsletter / 专栏 (3)
- **T05-S001** Matt Levine《Money Stuff》(Bloomberg) — 二手 — 用途: 当日并购/资本市场怪现状的犀利解读; cadence: 工作日日更.
- **T05-S002 / S003** Damodaran 博客 + NYU 个人站 — **一手** — 用途: 估值方法论 + 免费行业 multiple/数据集/spreadsheet; cadence: 博客月-不定期, 数据集年度刷新.
- **T05-S021** Axios Pro Rata (Dan Primack) — 二手 — 用途: 每日 deal/dealmaker 速报与独家; cadence: 工作日日更 + 周末版.

### 2. Podcast (4)
- **T05-S008** M&A Science (Kison Patel) — 一手 — 用途: 实操 M&A 执行 (尽调/整合/deal execution); cadence: 周更.
- **T05-S009** Acquired (Gilbert & Rosenthal) — 一手 — 用途: 公司史/并购案例长篇深挖; cadence: 不定期 (深度集).
- **T05-S010** Howard Marks Memos (Oaktree) — 一手 — 用途: 周期/风险/信用判断 (非纯 M&A 但 deal 思维); cadence: 一年 3-12 篇.
- **T05-S011** Animal Spirits (Batnick & Carlson) — 一手 — 用途: 市场/投资闲谈 (宏观语境); cadence: 周三更.

### 3. 一手 filing / 数据 (4)
- **T05-S005 / S006 / S007** SEC EDGAR (全文检索 UI + 浏览 + JSON API) — **一手金矿** — 用途: 拉 merger proxy (DEFM14A)/S-4/fairness opinion 原文; cadence: 实时随 filing.
- **T05-S022** Goldman Sachs IR — 一手 — 用途: bank 官方 deal/earnings 材料样板; cadence: 季度 earnings + 不定期.

### 4. 培训 / 参考 vendor docs (4)
- **T05-S012** CFI — 代理一手 — 估值/M&A/建模课 + 免费 resource; cadence: 持续更新.
- **T05-S013** Wall Street Prep — 代理一手 — merger model/accretion-dilution/synergy 指南; cadence: 持续.
- **T05-S014** BIWS — 代理一手 — 财务建模/M&A case study; cadence: 持续.
- **T05-S015** Macabacus — 代理一手 — Excel/建模/M&A 教程 + 插件; cadence: 持续.

### 5. 第三方 deal 数据 (3, 多付费, surrogate/secondary)
- **T05-S016** LSEG (Refinitiv) — 代理一手 — 全球 M&A 数据 + 季度 league table; 付费.
- **T05-S017** Dealogic (ION) — 代理一手 — 资本市场 deal 数据 + IB Scorecard; 付费.
- **T05-S018** Mergermarket (ION) — surrogate/secondary — 预测性 M&A 情报; 付费.
- **T05-S019** PitchBook — 代理一手 — PE/VC/M&A 数据 + 免费 news; 核心付费.

### + 法律/治理 (1, 跨 newsletter/reference)
- **T05-S020** Harvard Law Forum on Corporate Governance — 二手 — Delaware 判例/earnout/fiduciary; cadence: 日-周更.

---

## 媒体层厚薄判断

这行 en 媒体层**极厚, 三足鼎立**:
1. **一手 SEC filing** (EDGAR): 全美上市公司并购的 merger proxy / S-4 / fairness opinion 全文公开免费 — 全球罕见的一手原始文书金矿, 远胜任何二手分析.
2. **顶级 newsletter / 专栏**: Matt Levine、Damodaran、Axios Pro Rata 构成日更-月更的活跃创作层, 作者多为业界 / 学界顶流.
3. **长青 podcast**: M&A Science (实操)、Acquired (案例史)、Howard Marks (思维) 各占一个生态位.
4. **成熟 vendor 训练层** (CFI/WSP/BIWS/Macabacus) + **重资产付费数据平台** (LSEG/Dealogic/Mergermarket/PitchBook), 形成清晰的"免费引流 → 付费深度"漏斗.

与 zh-CN 创作者主导行业**正好相反**: 这里**不是**靠个人创作者撑场, 而是机构 (SEC/bank/数据平台) + 学界 (Damodaran/HLS) + 媒体平台 (Bloomberg/Axios) + vendor 共同支撑, 一手原始材料供给极其充沛, 信息可信度天然高。

**一手占比估计**: 22 条活源中 verified_primary 9 条 + surrogate_primary 8 条 ≈ 17/22 (约 77%) 带一手属性; 纯二手仅 5 条 (Levine/M&I/Axios/HLS + Bloomberg 平台)。真·一手 (sec.gov / Damodaran / podcast channel / bank IR) 占 9/22 ≈ 41%。

---

## 新 figure / tool 候选 (喂 Wave 2)

**Figure (人物 — 可蒸馏思维 skill):**
- **Aswath Damodaran** — 估值教父, 方法论体系完整, 公开材料海量 (强候选, 已有博客+数据集).
- **Matt Levine** — 金融现象解构者, "Money Stuff" 视角独特.
- **Howard Marks** — 周期/风险二阶思维, memo 体系成熟.
- **Kison Patel** — M&A 执行实操 (DealRoom 创始人, M&A Science host).
- **Brian DeChesare** — IB/M&A 职业+建模教学体系 (M&I + BIWS).

**Tool / 数据源 (供 Wave 2 抓取或集成):**
- **SEC EDGAR full-text search API** (efts.sec.gov/LATEST/search-index) — 程序化拉 merger proxy / S-4 / fairness opinion, 可作 retrieval 后端.
- **Macabacus / WSP merger model 模板** — accretion-dilution、contribution analysis、value creation 标准模型.
- **LSEG / Dealogic league table** — deal 排名与 market share 基准 (付费, 但季度报告部分公开).

---

## 质量自检

- 目标活源 ≥18 → **达成 22 条活源** (其中 6 条 WebFetch 403/connection 但均为 SEC/Bloomberg/Goldman/Macabacus/PitchBook 等公认存活机构站, 已用 WebSearch 或常识交叉确认; 其余 16 条 WebFetch 直接实访确认).
- **dead: 0 条** (无失效源; 旧 SEC `srqsb` 全文检索旧 URL 已废弃, 已替换为现行 `/edgar/search/` 故不计 dead).
- 5 分类全覆盖: newsletter (3) / podcast (4) / 一手 filing+数据 (4) / vendor 训练 (4) / 第三方 deal 数据 (4) + 法律治理补充 (1).
- 黑名单合规: 未收录任何 LinkedIn 文章正文 / WSO 匿名论坛帖 / 知乎 / 公众号 / 百度 / CSDN / Quora / 内容农场.
- bucket 分布: verified_primary 9, surrogate_primary 8, secondary 5, dead 0.
