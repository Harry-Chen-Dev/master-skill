# Track 03 — 工作流 / SOP / Pipeline · 摄影 (Photography) · locale=global

> Phase 1 Wave 3 输出。调研日期 2026-06-19。覆盖：商业 + 人像 + 纪实/街头 + 风光。
> seed = Track 01 (figures 怎么干活) + Track 02 (tools 怎么用) + Track 04 (canon 描述的标准流程)。
> 核心张力（喂 Phase 2）：抓取 vs 构建 · 前期 in-camera vs 后期塑造 · 真实纪录 vs 修饰美化 · 手工修 vs 生成式 AI。
> 7 个核心 workflow，每个含「入门 SOP（最少步骤）+ 资深路径（skip/optimize/add）+ 失败模式自检 + 近期变化」。

## Source Manifest

| source_id | url | bucket | last_checked | author/host | one-line note |
|-----------|-----|--------|--------------|-------------|---------------|
| T03-S001 | https://www.photopills.com/articles/exposure-photography-guide | secondary | 2026-06-19 | PhotoPills | 曝光三角系统教程（光圈/快门/ISO 决策） |
| T03-S002 | https://en.wikipedia.org/wiki/Exposing_to_the_right | secondary | 2026-06-19 | Wikipedia | ETTR 定义 + 信噪比/宽容度论证 |
| T03-S003 | https://fstoppers.com/education/how-use-ansel-adams-zone-system-digital-world-417047 | secondary | 2026-06-19 | Fstoppers | Zone System 数字时代映射 ETTR |
| T03-S004 | https://contrastly.com/basic-studio-lighting-setup-for-portraits/ | secondary | 2026-06-19 | Contrastly | 影棚布光设置顺序 key→meter→fill→test |
| T03-S005 | https://www.slrlounge.com/common-key-light-patterns/ | secondary | 2026-06-19 | SLR Lounge | 5 大 key light 布光模式（蝴蝶/环形/伦勃朗/分割） |
| T03-S006 | https://snapshot.canon-asia.com/article/eng/techniques-for-posing-and-directing-portrait-subjects | verified_primary | 2026-06-19 | Canon Asia (vendor) | 摆姿与引导：先摆身体再转脸 |
| T03-S007 | https://thelenslounge.com/how-to-cull-photos-in-lightroom/ | secondary | 2026-06-19 | The Lens Lounge | LR culling 评星法（first pass star rating） |
| T03-S008 | https://imagen-ai.com/valuable-tips/photo-mechanic-vs-lightroom-culling/ | secondary | 2026-06-19 | Imagen | Photo Mechanic vs LR 选片速度对比 |
| T03-S009 | https://phlearn.com/tutorial/professional-retouching-workflow/ | verified_primary | 2026-06-19 | PHLEARN (Aaron Nace) | 商业精修工作流顺序（cleanup→FS→D&B） |
| T03-S010 | https://retouchingacademy.com/dodge-burn-working-with-micro-transitions/ | secondary | 2026-06-19 | Retouching Academy | dodge & burn 微过渡修饰 |
| T03-S011 | https://aftershoot.com/blog/wedding-photography-workflow-peak-season/ | verified_primary | 2026-06-19 | Aftershoot (brand blog) | 婚礼旺季工作流系统 |
| T03-S012 | https://albertpalmerphotography.com/my-wedding-photography-backup-workflow/ | secondary | 2026-06-19 | Albert Palmer | 从业者本人婚礼备份 SOP（双卡/多盘/异地） |
| T03-S013 | https://aftershoot.com/blog/photo-culling-workflow/ | verified_primary | 2026-06-19 | Aftershoot (brand blog) | AI 选片完整工作流指南 |
| T03-S014 | https://www.slrlounge.com/snapshot-2025-aftershoot/ | secondary | 2026-06-19 | SLR Lounge | Snapshot 2025：AI 省下 12 工作周/人数据 |
| T03-S015 | https://fstoppers.com/software/aftershoot-just-became-entire-ai-photography-workflow-903026 | secondary | 2026-06-19 | Fstoppers | Aftershoot 2026 从选片变全栈 AI 工作流 |
| T03-S016 | https://erickimphotography.com/blog/zone-focusing/ | verified_primary | 2026-06-19 | Eric Kim (本人 blog) | 区域对焦/预对焦街头实操（figure 本人原文） |
| T03-S017 | https://www.picturecorrect.com/how-to-use-zone-focusing-for-street-photography/ | secondary | 2026-06-19 | PictureCorrect | zone focusing 距离/光圈设定 |
| T03-S018 | https://marszalstudio.pl/en/focus-stacking/ | secondary | 2026-06-19 | Marszal Studio | 产品景深合成 focus stacking 完整指南 |
| T03-S019 | https://blog.sigmaphoto.com/2020/tabletop-product-photography-guide-with-video/ | verified_primary | 2026-06-19 | Sigma (vendor blog) | 台面产品布光 + 控反光指南 |
| T03-S020 | https://vflatworld.com/blogs/behind-the-scenes/one-light-product-photography-setups | verified_primary | 2026-06-19 | V-Flat World (brand blog) | 单灯产品布光控高光（反光物体） |
| T03-S021 | https://www.bluebendphotography.com/wildlife-photography-in-2026/ | secondary | 2026-06-19 | Blue Bend | AI 眼控/动物追焦改变了/没改变什么 |
| T03-S022 | https://www.worldpressphoto.org/news/2023/could-an-ai-image-win-our-contest | surrogate_primary | 2026-06-19 | World Press Photo | 行业机构原文：全类别禁生成式 AI（纪实红线） |
| T03-S023 | https://www.digitalcameraworld.com/news/world-press-photo-relents-and-bans-ai-generated-images-from-its-2024-contest | secondary | 2026-06-19 | Digital Camera World | WPP 2024 禁 AI 来龙去脉 + 可接受/禁止编辑界 |
| T03-S024 | https://www.lensculture.com/articles/joel-meyerowitz-ready-for-surprise-joel-meyerowtiz-interview | secondary | 2026-06-19 | LensCulture / Meyerowitz | 街头「为惊喜做准备」预判姿态（figure 长访谈） |
| T03-S025 | https://strobist.blogspot.com/2006/03/lighting-101.html | verified_primary | 2026-06-19 | David Hobby (Strobist) | 离机闪光 Lighting 101 奠基（单灯起步） |

> 黑名单核验：无知乎/公众号/百度百科/CSDN，无 G2/Capterra，无纯导购农场。`source_verifier.py classify` 全跑过：aftershoot.com/blog、erickimphotography.com/blog、blog.sigmaphoto.com、vflatworld.com/blogs 自动判 verified_primary（brand/figure 一手 blog）；worldpressphoto.org 按行业机构原文人工标 surrogate_primary（org 第一方规则文件）。media 评测/教学站默认 secondary。**verified_primary 占比：5/25 = 20%**（含 surrogate 6/25 = 24%）——摄影工作流权威多为 figure 本人 blog + 教学媒体，机械可验证一手 URL 天然稀薄（与 Track 02/04 同结构问题），详见末尾自评。

---

## 总览（按 decay risk 分组）

### High decay (12-month-class) — 1 个
| Workflow | Trigger | Output | Last_updated | 资深差异 |
|---------|---------|--------|-------------|---------|
| 4. 后期 pipeline | RAW 进电脑要交付 | 调色/精修完成的成片 | 2026-06 | skip 手动逐张选片(AI 兜底) / optimize 批量预设+同步 / add 留校色+软打样 |

### Medium decay — 2 个
| Workflow | Trigger | Output | Last_updated | 资深差异 |
|---------|---------|--------|-------------|---------|
| 1. 通用拍摄链 | 举机前的现场 | 曝光/对焦/构图正确的 RAW | 2025-12 | skip 逐项思考(肌肉记忆) / optimize 眼控 AF / add 预判+ETTR |
| 5. 婚礼/活动一天 | 接到一场活动委托 | 全天关键时刻齐全的交付集 | 2026-06 | skip 死守清单 / optimize timeline 缓冲 / add 双机+冗余备份 |

### Low decay — 4 个
| Workflow | Trigger | Output | Last_updated | 资深差异 |
|---------|---------|--------|-------------|---------|
| 2. 影棚商业布光 | 棚拍人像/产品任务 | 光比/光型受控的成片光 | 2025-12 | skip 测光表(读直方图) / optimize 主光先定形 / add 轮廓+背景光分离 |
| 3. 人像引导与摆姿 | 真人坐到镜头前 | 自然不僵的表情与体态 | 2025-12 | skip 死姿势库 / optimize 先身体后脸 / add 持续引导+表情管理 |
| 6. 纪实/街头扫街 | 上街拍 | 决定性瞬间的抓拍 | 2026-06 | skip AF 半按等待(改预对焦) / optimize 区域对焦 / add 预判+接近伦理 |
| 7. 产品/电商台面 | 一批产品要拍图 | 清晰、控反光、全景深成图 | 2026-06 | skip 单帧拍(改堆栈) / optimize 单灯控高光 / add focus stacking |

---

## Workflow 卡片

### 1. 通用拍摄链 (Capture Pipeline)

- **One-liner**: 从「看到一个场景」到「按下快门得到一张曝光/对焦/构图都对的 RAW」的核心闭环——所有流派的地基。
- **Trigger**: 举起相机准备拍任意一张照片。
- **Output**: 一张曝光正确（高光不溢、暗部有信息）、主体合焦、构图成立的 RAW 文件。
- **入门 SOP（minimum viable steps）**:
  1. **看光选光**: 判断光的方向/软硬/色温，决定拍不拍、从哪个角度拍、要不要等光。跳过 → 顺光大白光拍出平淡无立体的废片，后期救不回光质。(evidence: [T04-S007, T03-S024])
  2. **曝光三角决策**: 先定意图——光圈定景深（虚化/全景深）、快门定动静（凝固/拖影）、ISO 兜底补够曝光。跳过 → 该虚化的全清晰、该凝固的糊掉，曝光意图丢失。(evidence: [T03-S001])
  3. **测光与曝光**: 用评价测光起手，对高反差场景切点测光 + 看直方图确认高光不溢出（数字时代向右曝光 ETTR 提信噪比）。跳过 → 高光死白不可逆 / 暗部噪点重，宽容度浪费。(evidence: [T03-S002, T03-S003])
  4. **构图**: 三分法放主体、引导线/框架引视线、留负空间、安排前景层次。跳过 → 主体居中呆板、画面无引导、视觉重心散。(evidence: [T04-S006])
  5. **对焦**: 对主体（人像对眼）合焦，确认焦点不在背景。跳过 → 主体脱焦，整张作废。
  6. **拍摄 + 即时回看**: 按快门，必要时回放直方图/放大检查焦点。跳过即时回看 → 直到回家才发现整组脱焦/欠曝。
- **资深路径（差异点）**:
  - **skip**: 资深人**跳过**逐项「想」曝光三角——光圈/快门/ISO 决策已是肌肉记忆，看一眼场景直接出参数；点测光也常被「看直方图凭经验补偿」取代。(evidence: [T03-S001])
  - **optimize**: 用**无反眼控/主体追焦**把「对焦」这步几乎自动化，注意力从「合不合焦」转移到「人物状态/时机」；构图靠取景框实时所见即所得微调而非事后裁切。(evidence: [T03-S021])
  - **add**: 资深人**额外做**预判（下一秒会发生什么，提前构好图等）+ 刻意 ETTR 给后期留宽容度 + 包围/多拍关键帧保险。(evidence: [T03-S002, T03-S024])
- **近期变化（近 12 个月）**:
  - 2023-2024 起，由无反**AI 主体识别/眼控对焦**（Sony/Canon/Nikon 旗舰）推动，原 step 5「手动选焦点 + 半按等待合焦」对人像/野生大幅自动化；资深注意力从「技术合焦」转向「行为/时机」——技术性锐度被民主化，但预判与定位仍是差异点。(evidence: [T03-S021])
  - 触发事件类型: 新工具（机身 AF 算法）。采用率: 旗舰无反已普遍，APS-C 中端 2024-2025 普及。
- **典型耗时**: 入门 SOP: 每张 10–60 秒思考；资深路径: 每张 1–5 秒（肌肉记忆）。
- **关键工具**: 无反相机系统（眼控 AF，必备）、直方图（必备）、点/评价测光（必备）。
- **关键人物**: Ansel Adams（Zone System/previsualization，Track 01）；Joel Meyerowitz（「为惊喜做准备」预判，[T03-S024]）。
- **常见失败模式**:
  - **顺光平拍**: 不看光从正面大白光拍 → 强制先判断光向，逆/侧光或等黄金时刻。**CLI 自检**: 「你判断过光的方向和软硬了吗？还是举起就拍？」
  - **高光溢出**: 没看直方图把高光拍死白 → 拍后扫一眼直方图右端，溢出就 -EV 重拍（高光死白后期不可逆，暗部还能拉）。**CLI 自检**: 「直方图右端贴墙了吗？高光救不回比暗部噪点严重得多。」
  - **背景对焦**: 焦点落在主体后方 → 人像锁眼控 AF，静物用单点对主体。
- **Last_updated**: 2025-12 · **Decay risk**: medium（AF 算法年年迭代，但「看光→曝光三角→构图→对焦」框架 10+ 年稳定）

---

### 2. 影棚商业布光 (Studio Lighting)

- **One-liner**: 在可控环境里从零搭出主光/辅光/轮廓光，得到光比和光型都受控的成片光——商业人像/产品的硬功底。
- **Trigger**: 棚拍人像或产品任务，需要人工塑光而非靠自然光。
- **Output**: 主体被想要的光型（蝴蝶/环形/伦勃朗/分割）和光比（如 2:1/4:1）照亮，背景与主体分离。
- **入门 SOP（minimum viable steps）**:
  1. **主光定位（key）**: 先只开主光，定方向/高度/距离决定光型与面部塑形，选修饰器（softbox 柔/beauty dish 硬）。跳过先定主光 → 多灯同时开根本看不出谁在塑形，光一团乱。(evidence: [T03-S004])
  2. **测光/确认主光**: 用测光表测主光在主体位的读数（或看试拍直方图）作为曝光基准。跳过 → 曝光全靠猜，多次试拍浪费时间，光比不可控。(evidence: [T03-S004])
  3. **辅光/光比（fill）**: 加补光填暗部，按想要的反差把补光设在主光下 1–2 档（2:1 柔/4:1 戏剧）。跳过 → 暗部死黑或反差失控，立体感全无或太硬。(evidence: [T03-S004])
  4. **轮廓光/背景光（rim/back）**: 加轮廓光把主体从背景剥离 + 背景光控背景影调。跳过 → 主体与背景糊成一片，无空间纵深。(evidence: [T04-S019])
  5. **修饰器选择**: softbox（柔/宽容瑕疵）/octabox（圆 catchlight，通用）/beauty dish（硬、雕纹理，美妆）/grid（控溢光）。选错 → 该柔的太硬（皮肤瑕疵全暴露）或该雕的太平。(evidence: [T02-S012, T02-S013])
  6. **试拍微调**: 拍一张看效果，按暗部太黑/catchlight 位置/溢光逐项调。跳过 → 把瑕疵带进整组拍摄。
  - 人像四光型记忆锚：**蝴蝶光**（正上方，鼻下蝴蝶影）/ **环形光**（鼻侧小环，最通用）/ **伦勃朗光**（颊上三角，45–60° 侧上）/ **分割光**（只照半脸）。(evidence: [T03-S005])
- **资深路径（差异点）**:
  - **skip**: 资深人常**跳过测光表**——看试拍直方图 + 经验直接定功率，尤其熟悉的固定布光；也跳过「四光型查表」，直接凭脸型想要的情绪定主光位。(evidence: [T03-S004, T03-S005])
  - **optimize**: 严格遵守**「一次只调一盏灯」**——先把主光调到完美再开第二盏，把调光从「猜」变成「可控变量」；用 grid/旗板精确切光防溢出而非加更多灯。(evidence: [T03-S004])
  - **add**: 资深人**额外做**主体/背景光分离（轮廓光 + 背景光独立控制制造纵深）、控反光的旗板/黑卡 negative fill 加深阴影侧塑形——初学者只想着「加光」，资深人懂「减光/挡光」同样塑形。(evidence: [T03-S020])
- **近期变化（近 12 个月）**: 近 12 个月**无重大变化**（行业稳态，光学原理不变）。唯一缓慢迁移：持续 LED（Aputure）让「所见即所得」布光降低初学门槛，photo/video hybrid 用同一套灯不换；但凝固动作/压环境光仍靠闪光。最近一次范式事件是 2006 起 Strobist 把离机闪光平民化。(evidence: [T03-S025], [T02-S010])
- **典型耗时**: 入门 SOP: 单一光型 30–60 分钟搭+调；资深路径: 5–15 分钟（熟悉布光直接复现）。
- **关键工具**: 离机闪光/影室灯（Godox/Profoto，必备）、修饰器（softbox/octabox/beauty dish/grid，必备）、测光表（场景特化）。
- **关键人物**: Joe McNally（小灯「用光书写」）/ David Hobby（Strobist 单灯起步）/ Lindsay Adler（时尚色彩布光）/ Karl Taylor（棚拍体系），均 Track 01。
- **常见失败模式**:
  - **一次开全部灯**: 多灯同时开看不出谁在塑形 → 先关全部，只开主光定形，再逐盏加。**CLI 自检**: 「你是先把主光单独调好，还是一上来就全开？」
  - **买灯不买修饰器/裸灯硬光**: 裸灯打人脸瑕疵全暴露、无商业感 → 修饰器才决定光质，预算优先投 softbox/octabox。**CLI 自检**: 「你的光质是修饰器塑的，还是裸灯/反光伞凑合？」
  - **主体粘背景**: 没有轮廓/背景光，主体与背景糊一起 → 加 rim light 或拉开主体与背景距离。
- **Last_updated**: 2025-12 · **Decay risk**: low（光学/光比原理 10+ 年不变）

---

### 3. 人像引导与摆姿 (Portrait Posing & Direction)

- **One-liner**: 把镜头前僵硬紧张的真人，引导成自然、有表情、体态显瘦的状态——决定人像「像不像个人」的软技能闭环。
- **Trigger**: 真人坐/站到镜头前，尤其是非专业模特/紧张的客户。
- **Output**: 主体表情自然、下巴/肩线/手脚位置经过管理、不显僵硬的人像。
- **入门 SOP（minimum viable steps）**:
  1. **建立 rapport**: 开拍前聊几句、解释流程、降低紧张，让对方信任。跳过 → 对方全程僵硬，表情假笑或木讷，再好的光也救不了。(evidence: [T03-S006])
  2. **先摆身体再调脸**: 先定身体角度（三七侧身 30–45° 最显瘦），再转头/脸找角度。跳过顺序 → 正面平拍显胖、姿势别扭。(evidence: [T03-S006])
  3. **下巴/肩线管理**: 「下巴前伸略下压」（Peter Hurley 的「乌龟」/ Sue Bryce「chin forward and down」）定义下颌线、消除双下巴；肩膀主动下沉后拉去紧张。跳过 → 双下巴、耸肩、脖子缩。(evidence: [T03-S006])
  4. **手脚处理**: 给手一个「任务」（扶、插兜、碰头发），脚分重心避免直挺挺。跳过 → 手不知放哪显尴尬，全身重心呆板。
  5. **表情管理 + 引导**: 实拍中持续给指令/逗笑/给情绪，抓自然表情而非「茄子」。跳过 → 一组假笑或呆滞，无可用表情。(evidence: [T03-S006])
- **资深路径（差异点）**:
  - **skip**: 资深人**跳过死记姿势库**——不再「摆 pose #1/#2」，而是从一个基础姿态微调（手肘外扩一点、下巴再低一度）连续流动出几十个变体。(evidence: [T03-S006])
  - **optimize**: 把引导**口令化/连续化**（"chin down… now laugh… look away"），让被摄者一直在动作流里不僵；rapport 与拍摄同步进行而非分两段。(evidence: [T03-S006])
  - **add**: 资深人**额外做**逐人定制——按脸型/身材/紧张程度判断该藏什么（双下巴/手臂压扁）、强调什么，并管理「微表情峰值」按快门，初学者只摆到「不难看」就拍。
- **近期变化（近 12 个月）**: 近 12 个月**无重大变化**（行业稳态，人体工学与心理引导原理不变）。眼控 AF 让摄影师不必盯对焦、可全程盯表情，间接强化了「引导优先」——但摆姿/引导方法论本身稳态。(evidence: [T03-S021])
- **典型耗时**: 入门 SOP: 每个姿势 2–5 分钟摆+调；资深路径: 连续流动，每分钟数个可用姿势。
- **关键工具**: 无（软技能为主），眼控 AF 机身解放注意力。
- **关键人物**: Platon（共情建立连接抹平紧张）/ Annie Leibovitz（与被摄者合作）/ Lindsay Adler（摆姿系统），Track 01。
- **常见失败模式**:
  - **不建立 rapport 直接开拍**: 对方紧张僵硬假笑 → 先聊 2 分钟、解释流程再举机。**CLI 自检**: 「你和被摄者建立信任了吗，还是冷场直接拍？」
  - **先调脸再摆身体**: 顺序反了导致姿势别扭 → 永远先定身体角度再转脸。
  - **忘了下巴/肩线**: 出现双下巴、耸肩 → 每个机位提醒「下巴前伸下压、肩膀沉下去」。**CLI 自检**: 「下巴前伸略下压了吗？肩膀放松下沉了吗？」
- **Last_updated**: 2025-12 · **Decay risk**: low（人体工学/心理引导稳态）

---

### 4. 后期 Pipeline (Cull → RAW → Retouch → Grade → Deliver)

- **One-liner**: 从一堆 RAW 到交付成片的完整流水线——选片、RAW 调整、像素级精修、调色、色彩管理输出。**全行业衰减最快的工作流**。
- **Trigger**: 一次拍摄结束，RAW 进了电脑，要产出可交付/可发布的成片。
- **Output**: 选定、调色、（人像/商业）精修、做了色彩管理、按 sRGB/打印 profile 导出的成片。
- **入门 SOP（minimum viable steps）**:
  1. **选片 culling**: 在 Lightroom/Photo Mechanic 里第一遍打星/旗标，筛掉废片（脱焦/闭眼/重复），只留 keeper。跳过 → 对几百张全图无差别精修，时间爆炸、交付质量参差。(evidence: [T03-S007, T03-S008])
  2. **RAW 调整**: 在 LR/Capture One 调曝光/白平衡/对比/高光阴影/色调曲线/HSL/局部蒙版。跳过 → 直接进 PS 精修一张没调好基底的图，事倍功半。(evidence: [T02-S014, T02-S015])
  3. **精修 retouch（人像/商业）**: 进 Photoshop 先 cleanup（去明显瑕疵/杂物）→ 频率分离（高频修纹理、低频修色块）→ dodge & burn 塑立体 → 液化微调形体。顺序：cleanup → FS → D&B → 调色之前。跳过 cleanup 直接 FS → 在大瑕疵上磨皮，事倍功半且不自然。(evidence: [T03-S009, T03-S010])
  4. **调色 grading**: 统一影调/色调（曲线/分离色调/LUT），定整组风格。跳过 → 一组照片色调跳跃不统一。
  5. **输出交付**: 做色彩管理（校色屏 + 按用途转 sRGB 网络/Adobe RGB 或打印 profile + 软打样），导出 + 上传客片平台/图库。跳过色彩管理 → 「我屏上好看，客户/印刷出来偏色」。(evidence: [T02-S026, T02-S027])
- **资深路径（差异点）**:
  - **skip**: 资深人**跳过逐张手动选片**——用 **AI 选片（Aftershoot/Imagen）** 一键筛重复/脱焦/闭眼，只复核边界；批量同色场景**跳过逐张调白平衡**用一张同步全组。(evidence: [T03-S013, T03-S007])
  - **optimize**: 建**预设/profile 库**一键套基底 + LR 同步把一张调整复制到整组 + Photoshop 动作/模板化频率分离；精修只在 keeper 的 hero 图做深度，其余批量过。(evidence: [T03-S007])
  - **add**: 资深人**额外做**校色仪 + 软打样 + 按交付端（网络 sRGB / 打印 ICC）分别导出，并保留分层 PSD 以便客户改稿；建立可复现的 catalog/命名/备份归档结构，初学者交完即丢。(evidence: [T02-S026])
- **近期变化（近 12 个月，Decay HIGH）**:
  - **2024-05 起**，由 **Lightroom Generative Remove + Photoshop Generative Fill + Topaz/DxO AI 降噪**推动，原 step 1 选片与 step 3 精修被改写：AI 一键移除杂物/扩展画面/救高 ISO，原本手动克隆/磨皮大量缩短。(evidence: [T02-S018, T02-S019])
  - **2025-2026**，**AI 选片+编辑一体化**（Aftershoot 2026 从「选片」扩成 cull→edit→retouch→export→卖图全栈；Imagen 把选片当全自动后期链第一步）正在合并 step 1–5。行业数据：AI 选片普遍减少 75–90% 初选时间（每场婚礼省 4–6 小时）；2025「Snapshot」报告称从业者人均省回约 12 工作周。(evidence: [T03-S013, T03-S014, T03-S015])
  - 触发事件类型: 新工具（生成式 AI + AI 选片/编辑）。采用率: AI 降噪 2024 起已成默认一步；AI 选片在婚礼/活动量产方向快速普及。
  - **红线**: 纪实/新闻方向**禁用生成式 AI**（见 Workflow 6），此变化只适用于商业/人像/婚礼/风光。
- **典型耗时**: 入门 SOP: 一场婚礼选片+调色 8–15 小时；资深路径（AI 选片+预设+批量）: 1–3 小时。(evidence: [T03-S014])
- **关键工具**: Lightroom Classic / Capture One（RAW，必备）、Photoshop（精修，必备）、Photo Mechanic（快选）、Aftershoot/Imagen（AI 选片/编辑，新兴）、Topaz/DxO/LR Denoise（AI 降噪，必备）、校色仪 + Pixieset/Pic-Time（交付）。
- **关键人物**: Aaron Nace/PHLEARN（PS 精修）/ Pratik Naik（高端修图工艺）/ 李涛（PS 后期体系）/ 储卫民（风光后期），Track 01。
- **常见失败模式**:
  - **不选片就全量精修**: 对几百张无差别修，时间爆炸 → 永远先 culling 打星只留 keeper 再精修。**CLI 自检**: 「你是先选片只留 keeper，还是想把每张都修？」
  - **跳过 cleanup 直接频率分离**: 在大瑕疵上磨皮不自然 → 顺序永远 cleanup → FS → D&B。**CLI 自检**: 「频率分离前，明显杂物/大痘清干净了吗？」
  - **不做色彩管理就交付**: 「我屏好看客户偏色」 → 校色屏 + 按用途转 sRGB/打印 profile + 软打样。**CLI 自检**: 「你的屏校过色吗？导出 profile 匹配交付端（网络 sRGB / 打印 ICC）吗？」
  - **AI 选片全盘信任**: AI 误删了情绪好但技术轻瑕疵的 keeper → AI 初筛后人工复核边界帧，别裸信。**CLI 自检**: 「AI 筛掉的里，有没有你其实想要的瞬间？复核过吗？」
- **Last_updated**: 2026-06 · **Decay risk**: **high**（生成式 AI + AI 选片/编辑 12 月内持续改写，强烈建议每 3 月复审）

---

### 5. 婚礼/活动一天流程 (Wedding / Event)

- **One-liner**: 从接单到交付一整场不可重来的活动——靠 timeline、关键时刻清单、冗余备份把「一次性、高压、不可 retake」变成可控流程。
- **Trigger**: 接到一场婚礼/活动委托（单次、不可重拍、客户期望高）。
- **Output**: 覆盖全天关键时刻（无遗漏）、有备份冗余、按风格调色交付的成片集。
- **入门 SOP（minimum viable steps）**:
  1. **行前 timeline + 勘景**: 与客户敲定当天时间线（化妆/仪式/合影/宴会），提前看场地光线与机位，做关键时刻 + 家庭合影清单。跳过 → 当天乱套、错过仪式、漏拍关键家人。(evidence: [T03-S011])
  2. **关键时刻清单**: 列「必拍」（戒指、宣誓、初吻、第一支舞、合影名单）。跳过 → 漏掉不可重来的核心瞬间 = 灾难性投诉。(evidence: [T03-S011])
  3. **双机 + 备份策略**: 带 ≥2 机身、多镜、多卡多电；机身开**双卡同时写入**，关键节点后**立即下卡备份**到多块盘 + 云/异地。跳过双卡冗余 → 一张卡损坏 = 整场丢失、无法挽回的法律/声誉风险。(evidence: [T03-S012])
  4. **当天节奏执行**: 按 timeline 走但留 15–20 分钟缓冲吸收延误，盯光/盯清单/不慌。跳过缓冲 → 一处延误连锁崩盘，赶场漏拍。(evidence: [T03-S011])
  5. **交付**: 选片（量大，AI 选片救场）→ 调色统一风格 → 客片平台在线交付。跳过统一调色 → 一套照片色调跳跃显业余。(evidence: [T02-S027])
- **资深路径（差异点）**:
  - **skip**: 资深人**不死守纸面清单**——核心时刻已内化为本能，清单只用于「合影名单」这类必须核对项；勘景靠经验快速读光不必逐角拍试。(evidence: [T03-S011])
  - **optimize**: 在 timeline 里**主动塞缓冲**并管理客户预期（合影 15 分钟够拍多少人有数）；用**双机不同焦段**（如机身 A 挂 35、机身 B 挂 70-200）减少换镜漏拍。(evidence: [T03-S011])
  - **add**: 资深人**额外做**多层冗余备份（机内双卡 + 当天多盘 + 当晚异地/云 = 3-2-1）+ 第二/助理摄影分担机位 + 后期 AI 选片把量产交付时间压到入门的几分之一。(evidence: [T03-S012, T03-S013])
- **近期变化（近 12 个月）**: 由 **AI 选片/编辑一体化**（Aftershoot/Imagen）推动，原 step 5「选片+调色」从 8–15 小时压到 1–3 小时，使「旺季一周接多场」可行（见 Workflow 4 数据）。拍摄/备份环节稳态。触发: 新工具。(evidence: [T03-S013, T03-S014])
- **典型耗时**: 入门 SOP: 拍摄 8–12 小时 + 后期 10–20 小时；资深路径: 拍摄同，后期压到 2–5 小时。
- **关键工具**: 大三元（24-70 核心）+ Godox 闪光（必备）、双卡机身 + 多块盘/云（备份）、Pixieset/Pic-Time（交付）、Aftershoot/Imagen（AI 选片）。
- **关键人物**: Zack Arias（从业生存论/单灯活动布光），Track 01。
- **常见失败模式**:
  - **单卡无冗余**: 卡损坏整场丢失 → 永远开机内双卡 + 当天立即下卡到多盘（3-2-1 备份）。**CLI 自检**: 「机身开双卡了吗？当天下午备份到了至少两个物理位置吗？」
  - **timeline 无缓冲**: 一处延误连锁崩盘 → 每段间塞 15–20 分钟缓冲。**CLI 自检**: 「你的当天时间线给延误留了缓冲，还是排得满满？」
  - **没勘景/没合影名单**: 漏拍关键家人 → 行前确认合影名单 + 指定一名亲友当天叫人。**CLI 自检**: 「合影名单和叫人的人，行前定好了吗？」
- **Last_updated**: 2026-06 · **Decay risk**: medium（拍摄/备份稳态，后期段被 AI 快速改写）

---

### 6. 纪实/街头扫街 (Street / Documentary)

- **One-liner**: 在不可控的公共空间里，靠预对焦、预判、伦理化接近，等到并抓住「决定性瞬间」——抓取派的核心闭环，也是 AI 伦理红线最硬的领域。
- **Trigger**: 上街/进现场拍真实发生的、不可摆布的瞬间。
- **Output**: 焦点准、几何成立、抓到行为/情绪峰值的纪实/街头帧。
- **入门 SOP（minimum viable steps）**:
  1. **预对焦/区域对焦 zone focusing**: 手动把焦点设到固定距离（如 2–3 米）+ 收小光圈（f/8–f/16）让一段「焦区」恒定清晰，进区即合焦。跳过 → 靠 AF 半按等合焦，错过瞬间或追焦拉风箱。(evidence: [T03-S016, T03-S017])
  2. **设好曝光基底**: 街头光变化大，常用光圈优先或全手动 + Auto ISO，先把曝光定个安全档不临场调。跳过 → 关键瞬间还在拨参数，错过。(evidence: [T03-S016])
  3. **预判 + 观察**: 找有潜力的光/背景/舞台，预判谁会走进画面、下一秒会发生什么，提前构好图等（「为惊喜做准备」）。跳过 → 看到才举机，永远慢半拍。(evidence: [T03-S024])
  4. **接近 + 伦理**: 「不够好是因为不够近」靠近主体；同时处理拍摄伦理（眼神/尊重/必要时交流/当地法规）。跳过接近 → 远摄裁切松散无张力；跳过伦理 → 冲突/侵犯/声誉风险。(evidence: [T04-S004])
  5. **等待决定性瞬间 + 抓拍**: 在构好的框里等元素（人/光/姿态）对齐到峰值再按。跳过 → 乱拍碰运气，几何/时机都不对。(evidence: [T04-S004])
- **资深路径（差异点）**:
  - **skip**: 资深人**跳过 AF 依赖**——直接区域对焦/超焦距把对焦从流程里删掉，相机成「速写本」零延迟；也跳过临场调曝光（已设好安全档）。(evidence: [T03-S016])
  - **optimize**: 把区域对焦距离/光圈**按场景预设成一套肌肉记忆**（街道 2m/f8、广场超焦距）；用安静小机身/旁轴降低存在感更好接近。(evidence: [T03-S016, T03-S017])
  - **add**: 资深人**额外做**主动预判与「布置舞台」式等待（选好光+背景守株待兔）+ 处理接近的社交/伦理（眼神交流、被发现时的应对），初学者只想着「偷拍清楚」。(evidence: [T03-S024], [T04-S004])
- **近期变化（近 12 个月，伦理红线 Decay high）**:
  - **2023-2024 起**，**World Press Photo 全类别禁用生成式 AI**（含 Photoshop Generative Fill 与部分 Topaz 生成式增强；Singles/Stories/Long-Term/Open Format 全禁），仅允许去噪、基础 levels/contrast、对象选择等不引入新信息的编辑；原文由两名独立数字分析师验原始文件。这把纪实/新闻后期的「可做/不可做」边界硬性钉死——与商业/人像可自由用生成式 AI 形成红线对立。(evidence: [T03-S022, T03-S023])
  - 触发事件类型: 行业标准/规则更新 + 行业事件（生成式 AI 冲击真实性）。采用率: 顶级新闻赛事/通讯社已普遍采纳零生成式 AI 政策。
  - 拍摄端（区域对焦/预判/接近）本身稳态——眼控 AF 对刻意「慢摄影」的旁轴/胶片街拍派影响有限。
- **典型耗时**: 入门 SOP: 一次扫街数小时换数张 keeper；资深路径: 命中率更高但仍靠等待，量不可强求。
- **关键工具**: 轻便定焦机身（Fuji X / 全幅 / 徕卡 M，必备）、单 35/50 定焦（必备）、区域对焦/超焦距（技术）。**严禁生成式 AI 改像素**。
- **关键人物**: Cartier-Bresson（决定性瞬间）/ Capa（靠近）/ Meyerowitz（为惊喜做准备）/ Eric Kim（区域对焦/克服恐惧）/ Daido Moriyama，Track 01。
- **常见失败模式**:
  - **靠 AF 等合焦错过瞬间**: 追焦拉风箱 → 改区域对焦/超焦距预设固定焦区，进区即拍。**CLI 自检**: 「你预对焦到固定距离了吗，还是每张都让 AF 重新找？」
  - **远摄裁切代替接近**: 画面松散无张力 → 物理靠近（安全/伦理前提下），不够好是因为不够近。
  - **越线用生成式 AI**: 纪实/新闻用 Generative Fill 移除/添加元素 = 伦理 + 资格双杀 → 纪实只允许去噪/基础调整，绝不引入新信息。**CLI 自检**: 「这是纪实/新闻吗？那你只能去噪/调基础影调，移除/添加任何元素都越线。」
- **Last_updated**: 2026-06 · **Decay risk**: low（拍摄技术稳态；AI 伦理规则段单独 high，但方向是「收紧/钉死」非「重写流程」）

---

### 7. 产品/电商台面 (Product / Tabletop)

- **One-liner**: 在台面上从控反光的布光、稳固支撑/构图、到景深合成、再到后期修瑕，产出清晰、无杂反光、全景深的商业产品图。
- **Trigger**: 一批产品（电商/广告/珠宝/美食）需要拍成可上架/投放的图。
- **Output**: 主体清晰锐利、反光受控、（必要时）前后全景深、背景干净的产品成图。
- **入门 SOP（minimum viable steps）**:
  1. **布光控反光**: 用 softbox/柔光 + 旗板/黑卡控制反光物体（电子/玻璃/金属）的高光与色彩溢出，单灯起步先控住一个主反光面。跳过 → 反光面一片死白或映出环境杂物/摄影师。(evidence: [T03-S019, T03-S020])
  2. **支撑 + 构图**: 三脚架固定机位（台面必须稳）、用支架/粘土/吊线固定产品角度，安排构图与背景。跳过脚架 → 长曝/景深合成糊掉、机位不可复现。(evidence: [T02-S010])
  3. **对焦 + 拍摄**: 用微距镜（90/100/105）对产品关键面合焦拍摄。跳过 → 细节不锐、放大露怯。(evidence: [T02-S032])
  4. **后期修瑕**: 进 PS/C1 清灰尘/划痕、修反光、抠背景、统一影调。跳过 → 灰尘瑕疵在白底上全暴露，不可上架。(evidence: [T02-S015])
- **资深路径（差异点）**:
  - **skip**: 单一平面产品资深人**跳过景深合成**直接单帧拍（小光圈够用）；熟悉的品类**跳过反复试光**直接复现一套标准布光模板。(evidence: [T03-S018])
  - **optimize**: 用**单灯 + 多块黑/白卡**精确雕高光而非堆多灯（反光物体加灯反而更乱）；联机拍摄（Capture One tether）实时大屏看反光即时调。(evidence: [T03-S020], [T02-S015])
  - **add**: 立体/有纵深产品（珠宝/含近远细节）**额外做 focus stacking 景深合成**——固定机位拍一系列逐步移焦的帧，用 Helicon Focus 等堆栈成「全清晰」；初学者用小光圈牺牲锐度，资深人用堆栈兼顾景深与镜头最佳光圈锐度。(evidence: [T03-S018])
- **近期变化（近 12 个月）**: 由 **AI 辅助景深合成**（如 Luminar Neo 自动识别各帧最锐区 + 校正畸变/色差）推动，原本 Helicon Focus 的手动堆栈门槛降低、减少人工判断。商业产品后期也用 Generative Fill 扩背景/补阴影（商业可接受，非纪实）。布光控反光物理原理稳态。触发: 新工具（AI 堆栈/生成式）。(evidence: [T03-S018], [T02-S021])
- **典型耗时**: 入门 SOP: 单品 30–60 分钟；资深路径（模板布光 + 堆栈自动化）: 单品 10–20 分钟。
- **关键工具**: 微距镜（90/100/105，必备）、三脚架 + 旗板/黑白卡（必备）、Capture One tether（场景特化）、移轴镜（tilt 调焦平面，可替代部分堆栈）、Helicon Focus/Luminar（景深合成）。
- **关键人物**: Light Science & Magic 谱系（family of angles 控反光物理），Track 04。
- **常见失败模式**:
  - **反光物体加更多灯**: 反光面映出更多杂物更乱 → 减灯 + 用黑卡 negative fill 控高光，单灯精确雕。**CLI 自检**: 「反光问题你是靠加灯还是靠黑/白卡控？反光物体往往要减光。」
  - **小光圈硬凑景深**: f/22 衍射使整体变软 → 用镜头最佳光圈 + focus stacking 堆栈兼顾景深与锐度。**CLI 自检**: 「需要前后全清晰时，你是 f/22 硬凑，还是堆栈？」
  - **不修瑕直接上架**: 白底灰尘/划痕全暴露 → 后期逐个清灰修反光。
- **Last_updated**: 2026-06 · **Decay risk**: low（控反光/景深物理稳态；AI 堆栈是优化非重写）

---

## Phase 2 接口

### 反复出现 ≥3 个 workflow 都包含的步骤模式（候选 playbook + 心智模型）

- **「先定主变量，再加次要变量，一次只调一个」**：出现于 W1（先看光再曝光三角）/ W2（先主光定形再加 fill/rim）/ W7（先控主反光面再加卡）→ 候选 playbook「塑造任何画面：隔离并锁定首要变量（光/主光/反光面），逐个叠加可控变量，绝不一次全开」。(evidence: [T04-S007, T03-S004, T03-S020])
- **「决策前置：按快门前就决定结果」**：W1（曝光三角意图先行/ETTR）/ W2（光型先想好）/ W3（先摆身体再拍）/ W6（预判+预对焦+构好图等）→ 候选心智模型「拍摄是决策前置不是事后补救」（呼应 Track 04 Adams previsualization + HCB 决定性瞬间）。(evidence: [T03-S001, T03-S016, T03-S024])
- **「冗余/兜底保险」**：W1（包围/多拍 + ETTR 留宽容度）/ W5（双卡 + 3-2-1 备份 + 双机）/ W4（保留分层 PSD/归档）→ 候选 playbook「不可重来的产出必须有冗余：拍摄端包围、存储端 3-2-1、交付端留可改稿母版」。(evidence: [T03-S002, T03-S012])
- **「分级处理：先粗筛只对 keeper 投入深度」**：W4（先 culling 再精修 hero）/ W5（量产选片 AI 初筛人工复核）→ 候选 playbook「永远先 triage 再深耕，别对全量做高成本操作」。(evidence: [T03-S007, T03-S013])
- **「修饰器/控光 > 灯本身；减光/挡光也是塑形」**：W2 + W7 共享 → 与 Track 02/04「光是主语、器材是宾语」直接合流。(evidence: [T03-S020], [T02-S012])

### 入门 SOP 和资深路径之间最大的差距（候选 心智模型）

- **入门平均 5–6 步，资深压缩到「肌肉记忆 + 自动化工具」后 2–3 个真正决策点**。这一行资深人特别擅长：①**把可名词化的技术步骤（曝光三角/对焦/选片）内化成本能或交给工具（眼控 AF / AI 选片）**，把省下的注意力全投到「不可自动化」的判断——光质、时机/预判、人物状态、伦理边界。
- 推断心智模型候选：**「自动化技术地基，把人脑留给判断」**——资深差异几乎不在「会不会做某步」，而在「哪步可以交给肌肉记忆/工具、哪步必须人脑亲自盯」。眼控 AF 和 AI 选片是这条心智模型在 2024-2026 的最新放大器。
- 另一条：**「减法思维」**——资深在布光（减光/黑卡）、选片（先删废片）、街头（删掉对焦这步）、摆姿（从一个姿态微调而非堆姿势库）上都体现「做减法比做加法更高阶」。

### 近期工作流变化清单（触发事件类型分布）

- **新工具（AI 后期/选片）→ 改写后期 + 婚礼交付段**（Decay high）：2024-05 LR Generative Remove / PS Generative Fill / Topaz·DxO·LR AI 降噪改写选片+精修；2025-2026 Aftershoot/Imagen AI 选片+编辑一体化合并整条后期链，省 75–90% 初选时间、人均省回约 12 工作周。(evidence: [T03-S013, T03-S014, T03-S015]) — 影响 W4、W5、W7。
- **新工具（机身 AF）→ 改写拍摄段**（Decay medium）：2023-2024 无反 AI 眼控/主体追焦把对焦自动化，注意力转向时机/状态。(evidence: [T03-S021]) — 影响 W1、W3、W6（街拍弱）。
- **行业标准/规则更新 + 行业事件 → 钉死纪实伦理红线**（Decay：规则段 high，流程稳态）：2023-2024 World Press Photo 全类别禁生成式 AI，只允许去噪/基础调整。(evidence: [T03-S022, T03-S023]) — 影响 W6，并与 W4 商业可用生成式 AI 形成「真实 vs 修饰」张力（呼应 Track 04 主分歧 ③）。
- 触发类型分布：**新工具 ≈ 大头（4 workflow 受影响）**，标准/规则 1 个（纪实），其余 low-decay 物理/人体工学稳态。**主要外部驱动力 = 生成式 AI**（双向：后期民主化 + 纪实伦理收紧）。

### 冷僻 / 信号薄弱自评

- **Workflow 数 7**（≥ floor 4 ✅，覆盖任务剧本指定全部 7 个）。
- **入门/资深/失败模式覆盖**: 7/7 都有完整入门 SOP + ≥2 类资深差异（skip/optimize/add）+ ≥2 处差异点 + 失败模式自检（含 CLI 化 actionable 写法）✅（100%，远超 80% 门槛）。
- **近期变化覆盖**: 7/7 都填了（3 个实质性变化 + 4 个明确标「稳态」并给最近一次范式事件）✅（100% ≥ 60% 门槛）。
- **一手来源占比**: verified_primary 5/25 = 20%，含 surrogate_primary 共 6/25 = 24%，**低于 50% 门槛**。原因与 Track 02/04 同构——摄影工作流的权威多来自 figure 本人 blog（Eric Kim/Strobist）+ 品牌/vendor blog（Aftershoot/Sigma/V-Flat）+ 教学媒体（PHLEARN/SLR Lounge/Fstoppers），classifier 默认把教学媒体归 secondary；机械可验证一手 URL 在本行天然稀薄，非调研失败。关键 claim 已做跨源（≥2 source）交叉。
- **Decay 分布**: high 1（后期）/ medium 2（拍摄、婚礼）/ low 4（布光、摆姿、街拍、产品）——本行工作流主体稳态（物理/人体工学），衰减集中在「后期 + AI」一条线。
- → **Phase 2.8 诚实边界标注**: workflow 维度信号充足（7 个全 retain、资深差异 100% 覆盖），但「一手 URL 机械可验证比例」偏低；Phase 2 提炼时将 figure 本人 blog + vendor blog 视为一手声音，教学媒体作共识交叉源。**后期 pipeline（W4）是全 skill 衰减最快模块，强烈建议每 3 月跑 update。**
