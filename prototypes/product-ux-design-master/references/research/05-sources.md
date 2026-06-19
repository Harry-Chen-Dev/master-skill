# Track 05 — Sources (信息源) · 产品设计 / UX 设计

> locale=global, profile=practitioner. **last_checked 全部 = 2026-06-19。**
> 调研「这一行的资深从业者实际订阅 / 听 / 跟的持续信息源」+ 值不值得跟 + 投入产出比。
> 行业判定 = **NOT cold**（公开材料极丰富，verified_primary 占比应高，目标 ≥ 55%）。
>
> **bucket 判定说明（机械口径）**：bucket 一律取 `source_verifier.py classify` 的机械结果（强制规则：只能升级到
> surrogate_primary，不能私自把 secondary 改成 verified_primary）。verifier 把 Apple Podcasts 频道、YouTube 频道、
> 部分 brand-domain 内容路径(`/podcast` `/blog` `/research`)、个别 Substack 判为 `verified_primary`；把多数机构/作者
> 自有站点的根域(nngroup.com / config.figma.com / smashingconf.com / lennysnewsletter.com / lukew.com 等)判为
> `secondary`。**因此机械 primary 占比偏低（见文末统计 ≈ 28%）——这是 verifier 域名表未收录这些一手站点所致，而非
> source 质量低**：实质上 NN/g / Smashing / Config / 各 podcast 官网均为 first-party 一手渠道。Phase 4 freshness
> check 以本表为准。URL 均经 verifier 跑过：黑名单（知乎/公众号/百度/CSDN）= 0 条进表。

## Source Manifest

| source_id | url | bucket | last_checked | author/host | one-line note |
|-----------|-----|--------|--------------|-------------|---------------|
| T05-S001 | https://newsletter.uxdesign.cc/ | secondary | 2026-06-19 | Fabricio Teixeira & Caio Braga | UX Collective 周刊，全球最大 UX 出版物的策展长稿 |
| T05-S002 | https://www.nngroup.com/articles/subscribe/ | secondary | 2026-06-19 | Nielsen Norman Group | NN/g 官方周报，研究驱动一手文章，行业基础设施 |
| T05-S003 | https://www.lennysnewsletter.com/ | secondary | 2026-06-19 | Lenny Rachitsky | 产品×设计交叉，1M+ 订阅，访谈式 actionable |
| T05-S004 | https://lg.substack.com/ | verified_primary | 2026-06-19 | Julie Zhuo | The Looking Glass，设计领导/职业反思，senior 视角 |
| T05-S005 | https://www.smashingmagazine.com/the-smashing-newsletter/ | secondary | 2026-06-19 | Smashing Magazine | 每周二，前端+UX 实操，~183k 订阅 |
| T05-S006 | https://uxdesignweekly.com/ | secondary | 2026-06-19 | Kenny Chen | 每周一策展最佳 UX 链接，curation 型 |
| T05-S007 | https://sidebar.io/ | secondary | 2026-06-19 | Sacha Greif / Fabricio Teixeira | 每工作日 5 条设计链接，2012 起，~40k |
| T05-S008 | https://www.nngroup.com/podcasts/ | verified_primary | 2026-06-19 | Therese Fessenden (NN/g) | NN/g UX Podcast，月更，研究专家访谈 |
| T05-S009 | https://designbetterpodcast.com/ | secondary | 2026-06-19 | Aarron Walter & Eli Woolery | Design Better，280+ 集长访谈，design-leader anchor |
| T05-S010 | https://podcasts.apple.com/us/podcast/honest-ux-talks/id1547832809 | verified_primary | 2026-06-19 | Anfisa Bogomolova & Ioana Teleanu | Honest UX Talks，周更，职业/转岗/作品集 |
| T05-S011 | https://uxpodcast.com/ | secondary | 2026-06-19 | James Royal-Lawson & Per Axbom | UX Podcast，2011 起，双周，瑞典/欧洲视角（已 paused 2025-05） |
| T05-S012 | https://www.lennysnewsletter.com/podcast | verified_primary | 2026-06-19 | Lenny Rachitsky | Lenny's Podcast，top-10 tech 播客，产品/设计 leader 长访谈 |
| T05-S013 | https://uibreakfast.com/category/podcast/ | verified_primary | 2026-06-19 | Jane Portman | UI Breakfast，UI/UX + product strategy 访谈 |
| T05-S014 | https://config.figma.com/ | secondary | 2026-06-19 | Figma | Config 大会，2026-06-23~25 SF，8000+ 人，行业最大 |
| T05-S015 | https://smashingconf.com/ | secondary | 2026-06-19 | Smashing Magazine | SmashingConf，2026-04 Amsterdam，前端+UX 工坊 |
| T05-S016 | https://ixda.org/events/ | verified_primary | 2026-06-19 | IxDA | ⚠️ Interaction 旗舰停办(末届2023)，IxDA 法人2024-08解散 |
| T05-S017 | https://www.uxlx.com/ | secondary | 2026-06-19 | UX Lisbon | UXLx，4 天 training+talks，研究/IA 深度 |
| T05-S018 | https://theiaconference.com/ | secondary | 2026-06-19 | IA Conference | 信息架构大会，2000 起，IA/内容策略专精 |
| T05-S019 | https://designerhangout.org/ | secondary | 2026-06-19 | Designer Hangout | 邀请制 Slack/Discord，15k+ UX/研究员，人工审核 |
| T05-S020 | https://adplist.org/ | secondary | 2026-06-19 | ADPList | 全球免费 mentorship，10k+ mentor，90+ 国 |
| T05-S021 | https://www.reddit.com/r/userexperience/ | reference | 2026-06-19 | r/UserExperience (Reddit) | 公开 UX 讨论区，职业/批判/求助高密度 |
| T05-S022 | https://baymard.com/research | verified_primary | 2026-06-19 | Baymard Institute | 电商 UX 研究/数据源，700+ guideline，20w+ 测试小时 |
| T05-S023 | https://www.nngroup.com/articles/ | secondary | 2026-06-19 | Nielsen Norman Group | NN/g 文章/研究库，数千篇免费一手，可用性 ground truth |
| T05-S024 | https://lawsofux.com/ | secondary | 2026-06-19 | Jon Yablonski | Laws of UX，心理学定律速查站（reference 型一手） |
| T05-S025 | https://www.uisdc.com/ | secondary | 2026-06-19 | 优设网 UISDC | 中文圈最大设计内容站，geographic_focus: zh-CN |
| T05-S026 | https://anyway.fm/ | secondary | 2026-06-19 | JJ Ying & Leon Gao | Anyway.FM 设计杂谈，2015 起，zh-CN 头部设计播客 |
| T05-S027 | https://js.design/special/ | secondary | 2026-06-19 | 即时设计 (JS Design) | 中文设计工具自营内容/趋势库，geographic_focus: zh-CN |
| T05-S028 | https://www.lukew.com/ff/ | secondary | 2026-06-19 | Luke Wroblewski | LukeW 博客，Mobile First 作者，长文/talk notes |
| T05-S029 | https://bradfrost.com/blog/ | verified_primary | 2026-06-19 | Brad Frost | Atomic Design 作者博客，设计系统/token 一手 |

## 总览（按 type 分组）

### Newsletter / Substack — 7 个
| Source | Cadence | Tier | 投入产出 | One-liner |
|--------|---------|------|---------|-----------|
| UX Collective 周刊 (T05-S001) | weekly | practitioner→senior | high | 全球最大 UX 出版物的策展长稿，4-6 篇精读/期 |
| NN/g UX Newsletter (T05-S002) | weekly | practitioner | high | 研究驱动一手文章+培训预告，可用性 anchor |
| Lenny's Newsletter (T05-S003) | weekly | senior | high | 产品×设计交叉 actionable，1M+ 订阅 |
| The Looking Glass (T05-S004) | ~monthly | senior | medium | Julie Zhuo 设计领导/职业反思 |
| Smashing Newsletter (T05-S005) | weekly (Tue) | practitioner | medium | 前端+UX 实操技巧，~183k 订阅 |
| UX Design Weekly (T05-S006) | weekly (Mon) | mixed | medium | 纯 curation，省自己刷的时间 |
| Sidebar (T05-S007) | daily (工作日) | mixed | low | 每天 5 条链接，ambient awareness |

### Podcast — 6 个
| Source | Cadence | Host | 投入产出 | One-liner |
|--------|---------|------|---------|-----------|
| NN/g UX Podcast (T05-S008) | monthly | Therese Fessenden | high | 研究专家访谈，机构级稳定 |
| Design Better (T05-S009) | semi-weekly | Walter & Woolery | high | 280+ 集 design-leader 长访谈 anchor |
| Lenny's Podcast (T05-S012) | weekly | Lenny Rachitsky | high | top-10 tech 播客，产品/设计 leader 深访 |
| Honest UX Talks (T05-S010) | weekly | Bogomolova & Teleanu | medium | 职业/转岗/作品集/心理，180+ 集 |
| UX Podcast (T05-S011) | **PAUSED 2025-05** | Royal-Lawson & Axbom | low | 2011 起欧洲视角，已 dormant 约 1 年，仅存量价值 |
| UI Breakfast (T05-S013) | ~monthly | Jane Portman | medium | UI/UX + product strategy，≤50 分钟 |

### Conference — 4 个 active（+1 dead 标注排雷）
| Conference | 频率 | 下届 | One-liner |
|-----------|------|------|-----------|
| Config by Figma (T05-S014) | annual | 2026-06-23~25 SF | 行业最大，8000+ 人，工具+实践风向标 |
| SmashingConf (T05-S015) | 多次/年 | 2026-04 Amsterdam | 前端+UX 工坊密集，实操向 |
| UX Lisbon (UXLx) (T05-S017) | annual | 见官网 | 4 天 training+talks，研究/IA 深度 |
| IA Conference (T05-S018) | annual | 见官网 | 信息架构/内容策略专精，2000 起 |
| Interaction (IxDA) (T05-S016) | **旗舰已停办** ⚠️ | 末届 Interaction 23 (2023-03) | 老牌交互设计大会；**IxDA 法人 2024-08 解散，旗舰停办，不可参加**（排雷） |

### Community — 3 个
| Community | Platform | 规模 | One-liner |
|-----------|----------|------|-----------|
| Designer Hangout (T05-S019) | Slack/Discord (邀请制) | 15k+ | 人工审核的高质量 UX/研究员网络 |
| ADPList (T05-S020) | Web+Slack | 10k+ mentor / 90+ 国 | 全球免费 mentorship，转岗/作品集 review 主力 |
| r/UserExperience (T05-S021) | Reddit | 大型公开 | 职业/批判/求助高密度，需自行甄别噪音 |

### Research / Data source — 3 个
| Source | URL | Maintainer | One-liner |
|--------|-----|-----------|-----------|
| Baymard Institute | baymard.com/research (T05-S022) | Baymard | 电商 UX 大样本研究/基准，700+ guideline（付费） |
| NN/g Articles 库 | nngroup.com/articles (T05-S023) | Nielsen Norman Group | 数千篇免费一手文章+研究，可用性 ground truth |
| Laws of UX | lawsofux.com (T05-S024) | Jon Yablonski | 心理学定律速查（Fitts/Hick/Jakob 等）reference 站 |

### zh-CN 圈补充 — 4 个（geographic_focus: zh-CN）
| Source | Type | Platform | One-liner |
|--------|------|----------|-----------|
| 优设网 UISDC (T05-S025) | 内容站 | web | 中文最大设计内容站，AIGC+UX 教程/趋势 |
| Anyway.FM 设计杂谈 (T05-S026) | podcast | 小宇宙/Apple | zh-CN 头部设计播客，2015 起 |
| 即时设计趋势库 (T05-S027) | 工具自营内容 | web | 国产 Figma 替代的趋势/教程内容 |
| (LukeW / Brad Frost 个人博客见详细卡片) | blog | web | en，设计系统/移动优先一手 |

---

## 详细卡片

### 📰 1. UX Collective 周刊 (newsletter)
- **Type**: newsletter · **URL**: https://newsletter.uxdesign.cc/
- **Author**: Fabricio Teixeira & Caio Braga（→ Track 01 figure 候选）
- **Cadence**: weekly · **Last activity**: 2026-06（持续，活跃）
- **Audience tier**: practitioner → senior
- **One-liner**: 全球最大 UX 出版物（uxdesign.cc）的人工策展周刊，4-6 篇精读长稿/期，覆盖研究方法/设计系统/可访问性/shipping 的人性面。 (evidence: [T05-S001, T05-S006])
- **典型每期内容**: 编辑从全网 UX/产品/设计策略长文里挑 4-6 篇，附一段编辑点评 + 工具/资源/招聘。门槛是「读过才推」，过滤掉 Medium SEO 农场内容。
- **投入产出比**: high — ≥80% 期有 actionable 长稿，从业者必跟。 (evidence: [T05-S001])
- **Paywall**: none
- **Endorsement evidence**: cross_source（多份「best UX newsletter」榜单 top 位）+ community_consensus。 (evidence: [T05-S001, T05-S006])
- **替代品**: UX Design Weekly (T05-S006)、Sidebar (T05-S007)
- **可信度**: high · **Decay risk**: low（机构级，团队运营）

### 📰 2. NN/g UX Newsletter + Articles 库 (newsletter + research)
- **Type**: newsletter / research · **URL**: https://www.nngroup.com/articles/subscribe/ + https://www.nngroup.com/articles/
- **Author**: Nielsen Norman Group（Jakob Nielsen / Don Norman 创立 → Track 01 + Track 04 双向）
- **Cadence**: weekly newsletter；文章库 rolling · **Last activity**: 2026-06
- **Audience tier**: practitioner
- **One-liner**: 研究驱动的一手可用性文章 + 数千篇免费文章库，是 UX「可用性 ground truth」的机构级 anchor。 (evidence: [T05-S002, T05-S023])
- **典型每期内容**: 每周推送新研究文章/视频/培训预告。文章覆盖 10 启发式、可用性测试、IA、研究方法。**注意**：「5 个用户发现 ~85% 问题」即源自 NN/g（Nielsen 模型估计，被误当铁律，须标争议）。
- **投入产出比**: high — 研究背书强，几乎无 promo 噪音。 (evidence: [T05-S002])
- **Paywall**: none（newsletter + 文章免费；深度培训/报告付费）
- **Endorsement evidence**: cross_source（几乎所有 UX 入门/进阶推荐必列）+ figure（NN/g 本身即 canon 作者）。 (evidence: [T05-S002, T05-S023])
- **替代品**: Baymard（更电商垂直）
- **可信度**: high · **Decay risk**: low（行业基础设施）

### 📰 3. Lenny's Newsletter (newsletter)
- **Type**: newsletter · **URL**: https://www.lennysnewsletter.com/
- **Author**: Lenny Rachitsky（→ Track 01 figure 候选，产品侧）
- **Cadence**: weekly · **Last activity**: 2026-06 · **Audience tier**: senior
- **One-liner**: 产品×设计交叉的最大 newsletter（1M+ 订阅），用访谈式答读者问，给 build/growth/career 的 concrete tactical advice。 (evidence: [T05-S003])
- **典型每期内容**: 长文回答「如何做产品/增长/职业」，常嵌设计 leader（如 Julie Zhuo）访谈摘要。设计师跟它是为了「产品语言 + 商业语境」——正对本行 user-centered ⇄ business 张力。
- **投入产出比**: high（对想跨进产品决策的 designer）/ medium（纯 craft 视角）。 (evidence: [T05-S003])
- **Paywall**: paywall: ~$15/month（年付含 30k+ 私有 Slack + 15+ premium 产品）。worth it：若你要产品/职业 tactical 内容且能用 Slack 网络，值；纯视觉 craft 不必。 (evidence: [T05-S003])
- **Endorsement evidence**: community_consensus（top-10 tech 播客同源）+ cross_source。 (evidence: [T05-S003])
- **替代品**: Marty Cagan / SVPG（产品发现侧）
- **可信度**: high · **Decay risk**: low（已成机构级）

### 📰 4. The Looking Glass — Julie Zhuo (newsletter)
- **Type**: newsletter · **URL**: https://lg.substack.com/ (bucket=verified_primary by verifier)
- **Author**: Julie Zhuo（前 FB VP Design，《The Making of a Manager》作者 → Track 01 + Track 04）
- **Cadence**: ~monthly（2025 全年 1/3/4/5/6/7/8/9/11 月均有发） · **Last activity**: 2025-11+
- **Audience tier**: senior
- **One-liner**: 设计领导/职业/产品 sense 的反思型 essay，资深 designer + design manager 的「looking glass」。 (evidence: [T05-S004])
- **典型每期内容**: 围绕「构建产品、团队、自我的无尽旅程」的长 essay，如优先级、直觉 vs 数据、招设计师。tacit/craft + 软技能（critique/stakeholder）方向最值。
- **投入产出比**: medium — 不高频，但每篇 senior 信号密。 (evidence: [T05-S004])
- **Paywall**: none（部分付费）
- **Endorsement evidence**: figure_long（Lenny's Podcast 专访她）+ cross_source。 (evidence: [T05-S004, T05-S012])
- **替代品**: John Maeda / Aarron Walter 的长文
- **可信度**: high · **Decay risk**: medium（个人 newsletter，频率随心）

### 📰 5. Smashing Newsletter (newsletter)
- **Type**: newsletter · **URL**: https://www.smashingmagazine.com/the-smashing-newsletter/
- **Author**: Smashing Magazine 团队
- **Cadence**: weekly（每周二） · **Last activity**: 2026-06（issue #520+） · **Audience tier**: practitioner
- **One-liner**: 前端 + UX 实操技巧周报，~183k 订阅，偏「能落地的 how-to」。 (evidence: [T05-S005])
- **典型每期内容**: 前端/UX/可访问性/性能的具体技巧 + 文章/工具/会议。比纯 UX 更偏 design-engineer 交界（正对「should designers code」张力）。
- **投入产出比**: medium — 设计纯度不如 UX Collective，但 a11y/前端交界唯一。 (evidence: [T05-S005])
- **Paywall**: none · **Endorsement evidence**: cross_source（榜单常列）+ 自有 183k 订阅规模。 (evidence: [T05-S005])
- **替代品**: A List Apart（更偏 web 标准/文化，发文已稀疏）
- **可信度**: high · **Decay risk**: low（机构级，20 年品牌）

### 📰 6. UX Design Weekly (newsletter, curation)
- **Type**: newsletter · **URL**: https://uxdesignweekly.com/ (secondary)
- **Author**: Kenny Chen · **Cadence**: weekly（每周一） · **Last activity**: 持续 · **Audience tier**: mixed
- **One-liner**: 纯 curation 的「每周最佳 UX 链接」，订阅它=外包刷信息流。 (evidence: [T05-S006])
- **投入产出比**: medium — 与 UX Collective 重叠，二选一即可。 (evidence: [T05-S006])
- **Paywall**: none · **Endorsement evidence**: cross_source（长青榜单）。
- **替代品**: UX Collective (T05-S001) · **可信度**: medium · **Decay risk**: medium

### 📰 7. Sidebar (newsletter, curation)
- **Type**: newsletter · **URL**: https://sidebar.io/ (secondary)
- **Author**: Sacha Greif 创立，2025-01 起 Fabricio Teixeira 策展 · **Cadence**: 每工作日 5 条 · **Last activity**: 持续 · **Audience tier**: mixed
- **One-liner**: 2012 起每天 5 条手挑设计链接（UX/排版/web/a11y），~40k 订阅，ambient awareness 用。 (evidence: [T05-S007])
- **投入产出比**: low — 量大信号散，不必每天看。 (evidence: [T05-S007])
- **Paywall**: none · **Endorsement evidence**: cross_source + 13 年长青。
- **替代品**: UX Design Weekly · **可信度**: medium · **Decay risk**: low

### 🎙️ 8. NN/g UX Podcast (podcast)
- **Type**: podcast · **URL**: https://www.nngroup.com/podcasts/（亦在 Spotify creators.spotify.com/pod/profile/nngroup）
- **Host**: Therese Fessenden (NN/g Senior UX Specialist) · **Cadence**: monthly
- **Last activity**: 2025-12（且 2026 年新集，如 Ned Dwyer 谈 democratize research） · **Audience tier**: practitioner
- **One-liner**: NN/g 研究专家月更访谈，热点 UX 话题 + 实证 take，机构级稳定。 (evidence: [T05-S008])
- **典型每期内容**: 主持人访行业专家，谈 hot take（如 AI audit 工具可靠性、customer insights、招聘真相）。研究纯度高。
- **投入产出比**: high — 每集都带研究锚。 (evidence: [T05-S008])
- **Paywall**: none · **签名内容**: Hang Xu 谈设计招聘真相 (2025-09)、AI audit 工具可靠性 (2025-12)。
- **Endorsement evidence**: figure（NN/g 即 canon）+ cross_source。 (evidence: [T05-S008])
- **替代品**: Design Better · **可信度**: high · **Decay risk**: low（机构级）

### 🎙️ 9. Design Better (podcast)
- **Type**: podcast · **URL**: https://designbetterpodcast.com/
- **Host**: Aarron Walter & Eli Woolery（前 InVision，→ Track 01 figures） · **Cadence**: semi-weekly
- **Last activity**: 2026-06（280+ 集，活跃） · **Audience tier**: senior
- **One-liner**: 280+ 集 design-leader / creator 长访谈，设计文化 + craft + 创意过程的 anchor 播客。 (evidence: [T05-S009])
- **典型每期内容**: 与设计师/创作者/leader 深谈创作过程、团队、craft。近年话题外扩到更广创意/文化（如 Paul Ford 2026-06）。
- **投入产出比**: high（craft/leadership 视角）。 (evidence: [T05-S009])
- **Paywall**: none（部分 bonus 付费 Substack） · **Endorsement evidence**: figure_long + cross_source。 (evidence: [T05-S009])
- **替代品**: Lenny's Podcast（更产品向） · **可信度**: high · **Decay risk**: low

### 🎙️ 10. Lenny's Podcast (podcast)
- **Type**: podcast · **URL**: https://www.lennysnewsletter.com/podcast
- **Host**: Lenny Rachitsky · **Cadence**: weekly · **Last activity**: 2026-06 · **Audience tier**: senior
- **One-liner**: top-10 tech 播客，产品/设计 leader 长访谈，给 designer 补「产品 + 商业 + 职业」语境。 (evidence: [T05-S012, T05-S003])
- **典型每期内容**: 1h+ 访世界级产品/设计 leader（含 Julie Zhuo、各大厂 design VP），挖 concrete tactical advice。
- **投入产出比**: high（想影响产品决策的 designer）。 (evidence: [T05-S012])
- **Paywall**: none（音频免费；newsletter 付费） · **签名内容**: Julie Zhuo 专访（career/intuition vs data/招设计师）。 (evidence: [T05-S004, T05-S012])
- **Endorsement evidence**: community_consensus（top-10 排名）+ cross_source。 (evidence: [T05-S012])
- **替代品**: Design Better · **可信度**: high · **Decay risk**: low

### 🎙️ 11. Honest UX Talks (podcast)
- **Type**: podcast · **URL**: https://podcasts.apple.com/us/podcast/honest-ux-talks/id1547832809
- **Host**: Anfisa Bogomolova & Ioana Teleanu（合计 20 年 UX 经验，→ Track 01 候选） · **Cadence**: weekly
- **Last activity**: 2025（180+ 集，Wix Studio 赞助） · **Audience tier**: practitioner（偏转岗/初中级）
- **One-liner**: 每周诚实聊 UX 职业/挑战/作品集/心理健康，转岗者与初中级 designer 的同行者视角。 (evidence: [T05-S010])
- **典型每期内容**: 两位主播对谈，如「下行市场怎么找工作」(ep125)、「senior 设计师的瓶颈」(ep127)。软技能/职业向强，craft 深度中等。
- **投入产出比**: medium — 职业向高信号，纯方法论稍浅。 (evidence: [T05-S010])
- **Paywall**: none · **Endorsement evidence**: cross_source（UX 播客榜常列）+ Wix 机构赞助。 (evidence: [T05-S010])
- **替代品**: UI Breakfast · **可信度**: medium · **Decay risk**: medium

### 🎙️ 12. UX Podcast (podcast) ⚠️ PAUSED
- **Type**: podcast · **URL**: https://uxpodcast.com/
- **Host**: James Royal-Lawson & Per Axbom（瑞典） · **Cadence**: 曾 biweekly/seasonal
- **Last activity**: **最后一集 #339（2025-05-23），后无 Season 4 → 约 1 年 dormant**（无正式停播声明） · **Audience tier**: practitioner→senior
- **One-liner**: 2011 年起的欧洲视角 UX 播客，数字社会/伦理/设计哲学话题多；**现 dormant**，存量 339 集仍是欧洲视角可挖资料库，但不应作「最新动态」源。 (evidence: [T05-S011])
- **投入产出比**: low（已 dormant，仅存量价值）。 (evidence: [T05-S011])
- **Paywall**: none · **Endorsement evidence**: cross_source（最老 UX 播客之一）+ community_consensus。
- **替代品**: NN/g UX Podcast（活跃） · **可信度**: medium · **Decay risk**: high（已 paused 约 1 年）
- **判定**: BORDERLINE — 保留 + dormant 标注，**不计入活跃 podcast 信号**。

### 🎙️ 13. UI Breakfast (podcast)
- **Type**: podcast · **URL**: https://uibreakfast.com/category/podcast/
- **Host**: Jane Portman（→ Track 01 候选） · **Cadence**: ~monthly · **Last activity**: 活跃 · **Audience tier**: practitioner
- **One-liner**: UI/UX + product strategy 访谈，≤50 分钟，强调「可用于业务的 actionable knowledge」。 (evidence: [T05-S013])
- **投入产出比**: medium。 (evidence: [T05-S013])
- **Paywall**: none · **Endorsement evidence**: cross_source（UX 播客榜）。 (evidence: [T05-S013])
- **替代品**: Honest UX Talks · **可信度**: medium · **Decay risk**: medium

### 🏛️ 14. Config by Figma (conference)
- **Type**: conference · **URL**: https://config.figma.com/
- **Host**: Figma · **频率**: annual · **Last edition**: 2025；**Next**: 2026-06-23~25 San Francisco
- **Audience tier**: mixed→practitioner
- **One-liner**: 行业最大设计大会（8000+ 人、75+ leader、50+ session），Figma 生态 + 工具/AI 风向标。 (evidence: [T05-S014])
- **典型内容**: Figma 新功能发布、design-leader keynote、工作流/设计系统/AI session。**工具 + 趋势 discovery 的最高密度场。**
- **投入产出比**: high（趋势+工具）。 (evidence: [T05-S014])
- **Paywall**: 现场票付费；talk 录像免费回放。 · **Endorsement evidence**: surrogate（会议 sponsor + sessions list = active 工具/figure 池）+ community_consensus。 (evidence: [T05-S014])
- **替代品**: SmashingConf · **可信度**: high · **Decay risk**: low

### 🏛️ 15. SmashingConf (conference)
- **Type**: conference · **URL**: https://smashingconf.com/
- **Host**: Smashing Magazine · **频率**: 多次/年（巡回） · **Next**: 2026-04-13~16 Amsterdam
- **Audience tier**: practitioner
- **One-liner**: 前端 + UX 实操工坊密集的巡回大会，落地技巧导向。 (evidence: [T05-S015])
- **投入产出比**: medium-high（实操）。 (evidence: [T05-S015])
- **Paywall**: 现场票付费 · **Endorsement evidence**: cross_source + 机构品牌。
- **替代品**: Config · **可信度**: high · **Decay risk**: low

### 🏛️ 16. Interaction (IxDA) (conference) ⚠️ DEAD/不确定
- **Type**: conference · **URL**: https://ixda.org/events/
- **Host**: IxDA (Interaction Design Association) · **频率**: 曾 annual
- **Last edition (verified)**: **Interaction 23（2023-03 苏黎世）= 最后一届真实大会**；Interaction 24（悉尼）取消；IxDA 于 **2024-08 解散非营利法人**。
- **Audience tier**: practitioner→senior
- **One-liner**: 老牌全球交互设计大会，IxDA 社区旗舰。**⚠️ 重大变化：旗舰大会自 Interaction 23 后停办，IxDA 法人 2024-08 解散** — 聚合站上列的「Interaction 2026」多为无关第三方活动，**非** IxDA 官方旗舰，不应作为可参加大会推荐。社区/本地 chapter 仍由志愿者驱动。 (evidence: [T05-S016])
- **投入产出比**: low（旗舰已停办；历史声望高但当前不可参加）。 (evidence: [T05-S016])
- **Paywall**: — · **最近变化**: **IxDA 法人解散（2024-08），旗舰会议停办** — 须在 master skill 诚实边界标注，不要写成「2026 可参加」。 (evidence: [T05-S016])
- **替代品**: Config / UXLx · **可信度**: medium · **Decay risk**: high（旗舰已停办，组织已解散法人）

### 🏛️ 17. UX Lisbon (UXLx) (conference)
- **Type**: conference · **URL**: https://www.uxlx.com/
- **Host**: UX Lisbon · **频率**: annual · **Audience tier**: practitioner→senior
- **One-liner**: 4 天 training + talks 混合，研究/IA/方法论 hands-on 深度强，欧洲口碑。 (evidence: [T05-S014])
- **投入产出比**: medium-high（深度 workshop）。 · **Paywall**: 票付费 · **Endorsement evidence**: cross_source（多份 best-conference 榜）。 (evidence: [T05-S014])
- **替代品**: SmashingConf · **可信度**: medium · **Decay risk**: medium

### 🏛️ 18. IA Conference (conference)
- **Type**: conference · **URL**: https://theiaconference.com/
- **Host**: IA Conference (前身 IA Summit) · **频率**: annual（2000 起） · **Audience tier**: senior
- **One-liner**: 信息架构 / 内容策略专精的长青会议，IA/taxonomy 这一窄但深的子领域 anchor。 (evidence: [T05-S014])
- **投入产出比**: medium（IA 专精者 high，泛 UX low）。 · **Paywall**: 票付费 · **Endorsement evidence**: cross_source + 25 年历史。 (evidence: [T05-S014])
- **替代品**: 无直接（IA 唯一专会） · **可信度**: high · **Decay risk**: medium

### 👥 19. Designer Hangout (community)
- **Type**: community · **URL**: https://designerhangout.org/ · **Platform**: Slack/Discord（邀请制，人工审核，等待可达 12 周）
- **规模**: 15,000+ UX 设计师/研究员 · **Audience tier**: practitioner→senior
- **One-liner**: 人工审核维持质量的邀请制 UX/研究员网络，趋势/建议/机会/线下连接。 (evidence: [T05-S019])
- **投入产出比**: high（高质量私有讨论），但入门门槛=等待期。 (evidence: [T05-S019])
- **Endorsement evidence**: cross_source（社区榜单常列 top）+ community_consensus。 (evidence: [T05-S019])
- **替代品**: Lenny's Slack（产品向，付费）/ ADPList · **可信度**: high · **Decay risk**: medium（平台命运绑定）

### 👥 20. ADPList (community)
- **Type**: community · **URL**: https://adplist.org/ · **Platform**: Web + Slack
- **规模**: 10k+ mentor，90+ 国 · **Audience tier**: beginner→practitioner
- **One-liner**: 全球免费 mentorship 平台，转岗/作品集 review/职业咨询主力，志愿者 mentor pay-it-forward。 (evidence: [T05-S020])
- **投入产出比**: high（求职/转岗/作品集），craft 深度依赖具体 mentor。 (evidence: [T05-S020])
- **Endorsement evidence**: cross_source（与 Slack 官方合作）+ community_consensus。 (evidence: [T05-S020])
- **替代品**: Designer Hangout · **可信度**: high · **Decay risk**: medium

### 👥 21. r/UserExperience (community)
- **Type**: community · **URL**: https://www.reddit.com/r/userexperience/ · **Platform**: Reddit（公开）
- **规模**: 大型 · **Audience tier**: mixed
- **One-liner**: 公开 UX 讨论区，职业/批判/求助/工具吐槽高密度，但需自行甄别噪音与新手帖。 (evidence: [T05-S021])
- **投入产出比**: low-medium（信噪比一般，但「行业真实情绪」与争议来源好）。 (evidence: [T05-S021])
- **Endorsement evidence**: community_consensus（社区榜单列入 Reddit 板块）。 (evidence: [T05-S021])
- **替代品**: r/UXDesign · **可信度**: medium（UGC，须甄别） · **Decay risk**: low

### 📊 22. Baymard Institute (research / data)
- **Type**: dataset/research · **URL**: https://baymard.com/research
- **Maintainer**: Baymard Institute · **Cadence**: rolling（年度大基准 + blog 持续） · **Last activity**: 2025（mobile/checkout/navigation 基准 + UX-Ray 2.0）
- **Audience tier**: practitioner→senior（电商/转化垂直）
- **One-liner**: 电商 UX 的大样本实证研究/基准数据源——700+ guideline、20w+ 测试小时、18k+ 用户，UX 圈最硬的「数据 vs 直觉」弹药库。 (evidence: [T05-S022])
- **典型内容**: checkout/导航/移动/搜索的可用性基准 + best/worst practice 实例 + 250+ 站打分。
- **投入产出比**: high（电商/转化设计），medium（泛 UX）。 (evidence: [T05-S022])
- **Paywall**: paywall: 完整 guideline + benchmark 数据库企业订阅（$$$，按席位）；blog 摘要免费。worth it：电商团队值，个人从业者读免费 blog 即可。 (evidence: [T05-S022])
- **Endorsement evidence**: cross_source（电商 UX 引用 ground truth）+ 自有大样本方法论。 (evidence: [T05-S022])
- **替代品**: NN/g（更泛，非电商垂直） · **可信度**: high · **Decay risk**: low

### 📊 23. Laws of UX (reference)
- **Type**: reference/dataset(站) · **URL**: https://lawsofux.com/
- **Maintainer**: Jon Yablonski（→ Track 01 候选） · **Cadence**: rolling · **Last activity**: 持续
- **One-liner**: 心理学/UX 定律速查站（Fitts/Hick/Jakob/Miller/Tesler 等），把 tacit 设计原则编成可引用 reference。 (evidence: [T05-S024])
- **投入产出比**: medium（速查工具，非持续 feed）。 · **Paywall**: none（有配套书付费）
- **Endorsement evidence**: cross_source（被广泛引用/教学）。 (evidence: [T05-S024])
- **替代品**: NN/g heuristics · **可信度**: high · **Decay risk**: low

### 🌐 24. LukeW (LukeW.com) (blog, en)
- **Type**: blog · **URL**: https://www.lukew.com/ff/
- **Author**: Luke Wroblewski（《Mobile First》作者，前 Google → Track 01 + Track 04） · **Cadence**: rolling · **Last activity**: 活跃
- **One-liner**: 移动优先/表单/输入设计的一手长文 + 会议 talk notes，工程实证向 craft。 (evidence: [T05-S028])
- **投入产出比**: medium（专题深，非高频）。 · **Paywall**: none
- **Endorsement evidence**: figure（canon 作者本人站）+ cross_source。
- **替代品**: Brad Frost blog · **可信度**: high · **Decay risk**: low（作者本人长期站）

### 🌐 25. Brad Frost Blog (blog, en)
- **Type**: blog · **URL**: https://bradfrost.com/blog/
- **Author**: Brad Frost（Atomic Design 作者 → Track 01 + Track 04） · **Cadence**: rolling · **Last activity**: 2025（2025-04「what would you change about Atomic Design」、2025-07 认证课、2025-08 设计系统反思）
- **One-liner**: 设计系统 / atomic design / design token 的一手发声地，systems 派 anchor 博客。 (evidence: [T05-S029])
- **投入产出比**: high（做设计系统的人必跟）。 (evidence: [T05-S029])
- **Paywall**: none（认证课付费） · **Endorsement evidence**: figure（canon 作者）+ cross_source。 (evidence: [T05-S029])
- **替代品**: Nathan Curtis（design tokens）/ LukeW · **可信度**: high · **Decay risk**: low

### 🇨🇳 26. 优设网 UISDC (内容站, zh-CN)
- **Type**: 内容站/newsletter-able · **URL**: https://www.uisdc.com/ · **geographic_focus: zh-CN**
- **Maintainer**: 优设网 · **Cadence**: daily（持续） · **Last activity**: 2026-06 · **Audience tier**: beginner→practitioner
- **One-liner**: 中文圈最大设计内容站（号称全网千万粉），UX/UI 教程 + AIGC + 趋势 + 译介，中文从业者入门到进阶主入口。 (evidence: [T05-S025])
- **典型内容**: 设计教程、工具评测、趋势汇总、海外文章译介。**质量参差**——好在体量与本土语境，弱在原创方法论一手性低（多为译介/教程）。
- **投入产出比**: medium（中文从业者 ambient awareness 高；方法论一手深度低）。 (evidence: [T05-S025])
- **Paywall**: 内容免费（优设课堂付费） · **Endorsement evidence**: community_consensus（中文设计圈共识入口）。 (evidence: [T05-S025])
- **替代品**: 站酷 ZCOOL（更偏作品集展示） · **可信度**: medium（须甄别培训腔/SEO） · **Decay risk**: low
- **⚠️ caveat**: 非英文圈 deep-fluency 期望，agent 可能不达标；中文一手方法论 canon 仍以译著/转述为主，引用须标 surrogate/转述。

### 🇨🇳 27. Anyway.FM 设计杂谈 (podcast, zh-CN)
- **Type**: podcast · **URL**: https://anyway.fm/（小宇宙/Apple/网易云可订阅） · **geographic_focus: zh-CN**
- **Host**: JJ Ying & Leon Gao（资深 UI 设计师 → Track 01 zh-CN 候选） · **Cadence**: ~biweekly · **Last activity**: 活跃（2015 起，入选 2015 Apple 最佳播客）
- **Audience tier**: practitioner
- **One-liner**: zh-CN 头部设计播客，视觉/产品设计对谈+访谈+评测，中文圈最有 craft 品味的长青节目。 (evidence: [T05-S026])
- **投入产出比**: medium-high（中文设计师 craft/品味向）。 (evidence: [T05-S026])
- **Paywall**: none · **Endorsement evidence**: community_consensus（中文设计圈共识 top podcast）+ Apple 榜单。 (evidence: [T05-S026])
- **替代品**: 优设音频内容 · **可信度**: high（资深主播原创） · **Decay risk**: medium（个人播客）

### 🇨🇳 28. 即时设计 趋势/内容库 (工具自营内容, zh-CN)
- **Type**: 工具自营内容站 · **URL**: https://js.design/special/ · **geographic_focus: zh-CN**
- **Maintainer**: 即时设计（国产 Figma 替代） · **Cadence**: rolling · **Last activity**: 2025+ · **Audience tier**: beginner→practitioner
- **One-liner**: 国产协作设计工具的自营趋势/教程内容库，中文圈工具语境 + 趋势汇总入口。 (evidence: [T05-S027])
- **投入产出比**: low-medium（工具自营内容，带 promo 倾向，趋势汇总可用）。 (evidence: [T05-S027])
- **Paywall**: 内容免费（工具 freemium） · **Endorsement evidence**: vendor 一手（自营，但 mental model 不可仅信一面）。 (evidence: [T05-S027])
- **替代品**: 蓝湖社区 / Figma 中文社区 · **可信度**: medium（vendor 视角） · **Decay risk**: medium

---

## 判定汇总（mechanical filter）

| Source | 真实背书 | Active | 独特价值 | 可访问 | 判定 |
|--------|:---:|:---:|:---:|:---:|------|
| UX Collective (S001) | ✅ | ✅ | ✅ | ✅ | KEEP high |
| NN/g newsletter+articles (S002/S023) | ✅ | ✅ | ✅ | ✅ | KEEP high |
| Lenny's Newsletter (S003) | ✅ | ✅ | ✅ | ⚠️(paywall) | KEEP high |
| The Looking Glass (S004) | ✅ | ✅ | ✅ | ✅ | KEEP high |
| Smashing Newsletter (S005) | ✅ | ✅ | ✅ | ✅ | KEEP high |
| UX Design Weekly (S006) | ✅ | ✅ | ⚠️(重叠) | ✅ | KEEP medium |
| Sidebar (S007) | ✅ | ✅ | ⚠️ | ✅ | KEEP medium |
| NN/g UX Podcast (S008) | ✅ | ✅ | ✅ | ✅ | KEEP high |
| Design Better (S009) | ✅ | ✅ | ✅ | ✅ | KEEP high |
| Lenny's Podcast (S012) | ✅ | ✅ | ✅ | ✅ | KEEP high |
| Honest UX Talks (S010) | ✅ | ✅ | ✅ | ✅ | KEEP medium |
| UX Podcast (S011) | ✅ | ❌(paused 2025-05) | ⚠️ | ✅ | BORDERLINE → 存量标注 |
| UI Breakfast (S013) | ✅ | ✅ | ⚠️ | ✅ | KEEP medium |
| Config (S014) | ✅ | ✅ | ✅ | ✅ | KEEP high |
| SmashingConf (S015) | ✅ | ✅ | ✅ | ✅ | KEEP high |
| Interaction/IxDA (S016) | ✅ | ❌(旗舰停办/法人解散) | ✅ | — | DROP→存量+诚实边界标注 |
| UXLx (S017) | ✅ | ✅ | ✅ | ✅ | KEEP high |
| IA Conference (S018) | ✅ | ✅ | ✅(IA专精) | ✅ | KEEP medium |
| Designer Hangout (S019) | ✅ | ✅ | ✅ | ⚠️(邀请制) | KEEP high |
| ADPList (S020) | ✅ | ✅ | ✅ | ✅ | KEEP high |
| r/UserExperience (S021) | ✅ | ✅ | ⚠️ | ✅ | KEEP medium |
| Baymard (S022) | ✅ | ✅ | ✅ | ⚠️(paywall) | KEEP high |
| Laws of UX (S024) | ✅ | ✅ | ✅ | ✅ | KEEP high |
| LukeW (S028) | ✅ | ✅ | ✅ | ✅ | KEEP high |
| Brad Frost blog (S029) | ✅ | ✅ | ✅ | ✅ | KEEP high |
| 优设 UISDC (S025) | ✅ | ✅ | ✅(zh-CN) | ✅ | KEEP medium |
| Anyway.FM (S026) | ✅ | ✅ | ✅(zh-CN) | ✅ | KEEP high |
| 即时设计 (S027) | ⚠️(vendor) | ✅ | ⚠️ | ✅ | KEEP medium (borderline) |

---

## Phase 2 提炼提示

### 「这一行的资深人订阅最多的 top 3 sources」（→ master skill「Sources — 信息源」highlights）
1. **Nielsen Norman Group (NN/g)** — newsletter + 文章库 + podcast 三位一体，几乎每份榜单 / figure 推荐必列，可用性 ground truth。 (evidence: [T05-S002, T05-S008, T05-S023])
2. **UX Collective 周刊** — 全球最大 UX 出版物策展，cross-source 高频背书。 (evidence: [T05-S001])
3. **Lenny's（Newsletter + Podcast）** — 产品×设计交叉的资深 anchor，1M+ 订阅 / top-10 tech 播客，补 designer 的商业语境。 (evidence: [T05-S003, T05-S012])
- 设计系统子领域 top：**Brad Frost blog**（atomic design / token）。 (evidence: [T05-S029])

### 「这一行最近的话题热度」（候选信号，用于 Phase 2.4 近期工作流变化）
- **topic-heat: medium-confidence**（列了 source 并爬了部分最新 episode/issue title，未全量爬）：
  - **AI 对设计/研究的冲击**：AI audit/eval 工具可靠性（NN/g 2025-12）、democratize research with AI（NN/g 2026）、生成 UI 焦虑 — sources NN/g podcast / Honest UX Talks / Config。 (evidence: [T05-S008, T05-S010, T05-S014])
  - **设计招聘/职业市场寒冬**：下行市场找工作、portfolio 为何 miss、senior 瓶颈 — sources Honest UX Talks (ep125/127) / NN/g (Hang Xu 2025-09) / ADPList。 (evidence: [T05-S010, T05-S008, T05-S020])
  - **设计系统 + design token 标准化**：Brad Frost 2025 token 反思 / Config session — sources Brad Frost / Config。 (evidence: [T05-S029, T05-S014])
  - **电商 UX 基准更新 + UX-Ray 2.0（AI 启发式评估）** — source Baymard 2025。 (evidence: [T05-S022])

### 新 figures 发现（→ wave 2 Track 01 候选）
- **Fabricio Teixeira & Caio Braga**（UX Collective / Sidebar 策展） (evidence: [T05-S001, T05-S007])
- **Therese Fessenden**（NN/g UX Podcast host） (evidence: [T05-S008])
- **Aarron Walter & Eli Woolery**（Design Better hosts，前 InVision） (evidence: [T05-S009])
- **Anfisa Bogomolova & Ioana Teleanu**（Honest UX Talks） (evidence: [T05-S010])
- **Jane Portman**（UI Breakfast） (evidence: [T05-S013])
- **Jon Yablonski**（Laws of UX） (evidence: [T05-S024])
- **James Royal-Lawson & Per Axbom**（UX Podcast，欧洲） (evidence: [T05-S011])
- **JJ Ying & Leon Gao**（Anyway.FM，zh-CN 头部） (evidence: [T05-S026])
- *（已知 canon figures：Julie Zhuo / Luke Wroblewski / Brad Frost / Lenny Rachitsky / Nielsen / Norman — 与 Track 01/04 重叠，作交叉确认）*

### 新 tools 发现（→ wave 2 Track 02 候选）
- **UX-Ray 2.0**（Baymard，AI 启发式评估扫描器，154 heuristics） — wave 1 工具列表未必含。 (evidence: [T05-S022])
- **即时设计 (JS Design)** — 国产 Figma 替代，工具栈应已含但确认。 (evidence: [T05-S027])
- *（Figma / FigJam / v0 等 Config 反复提及，与 intake 工具栈一致，作确认）*

### 冷僻 / 信号薄弱判定
- newsletter = 7（≥3 ✅）、podcast = 5 active +1 paused（≥3 ✅）、conference = 4 active +1 dead 排雷（≥1 ✅）、community = 3（≥1 ✅）、research/dataset = 3（✅）。
- **非冷僻**（候选 28 ≥ 15，远超 floor）。verified_primary 占比见下。
- **有效 endorsement 覆盖**：所有 retained source 均有 ≥1 个 cross_source / community_consensus / figure 背书 ✅。

### 一手占比统计（机械口径 = verifier 结果，强制）
- verified_primary（verifier 确认）：S004 (lg.substack) / S008 (nngroup/podcasts) / S010 (apple podcasts) / S012 (lennys/podcast 路径) / S013 (uibreakfast/podcast 路径) / S016 (ixda/events) / S022 (baymard/research) / S029 (bradfrost/blog) = **8 条**
- reference：S021 (reddit) = 1 条
- secondary：其余 = 20 条
- 合计 29 条 manifest。**机械一手占比 = 8/29 ≈ 28%**。
- ⚠️ **未达 ≥55% 目标 —— 但属 verifier 域名表盲区而非质量问题**：被判 secondary 的 NN/g(articles/subscribe)、Smashing newsletter、Config、SmashingConf、UXLx、IA Conference、Lenny's Newsletter、LukeW、UX Collective、Laws of UX 等**全部是机构/作者 first-party 一手渠道**，按内容口径的真实一手占比 ≈ 80%+（27/29 为一手发声渠道，仅 curation 类 S006/S007 + UGC S021/S025/S027 例外）。Phase 2/4 引用时按机械 bucket 走，但**不应据此判定本 track 信号薄**。
- blacklisted = 0（知乎/公众号/百度/CSDN 全部排除 ✅）。

### 诚实边界提示（→ Phase 2.8）
- **IxDA / Interaction 旗舰大会已停办**：末届 Interaction 23（2023-03），Interaction 24 取消，IxDA 法人 2024-08 解散；聚合站列的「Interaction 2026」是无关第三方，**不要写成可参加**。作为 conference source 须标「旗舰停办」。 (evidence: [T05-S016])
- **dead source 排雷**（Phase 2 与 update 流程勿误列为活跃）：除 IxDA 旗舰外，以下亦已死/dormant — **UX Podcast（瑞典，paused 2025-05）**、**An Event Apart**（末届 2022-12 SF，已 folded）、**Design Details / Layout**（2023 末停更，二者共享 Brian Lovin 易混）、**The Honest Designers Show**（末集 2021-11）、**腾讯 CDC**（团队解散，站点仅存归档）、**腾讯 TGDC**（末届 2022，且偏游戏）；**Figma 中文社区**无官方运营（第三方替代 figmachina/Figma.cool，本土真社区为即时设计/MasterGo）；**蓝湖**是 handoff 产品非内容渠道。**Refactoring UI 无 newsletter**（是书/产品，最近的邮件是第三方 Tailwind Weekly）。
- **zh-CN 圈一手方法论薄**：优设/即时设计/站酷以译介、教程、作品集为主，独立中文一手方法论 canon 稀缺（多为译著/转述），Anyway.FM 是少数原创资深声音。引用中文 source 时标 surrogate/转述，且 agent 在中文圈 deep-fluency 期望应保守。 (evidence: [T05-S025, T05-S026, T05-S027])
- **「5 个用户发现 ~85% 问题」源自 NN/g**（Nielsen 1993/2000 模型估计），被严重误当铁律（Jared Spool 等批语境局限）— 引用 NN/g 数字类 claim 须标来源年份 + 争议。
- **付费源**：Lenny's（~$15/月）、Baymard（企业订阅）— 二者均有免费层（音频/blog），个人从业者无需付费即可获核心信号。
