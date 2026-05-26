# 02-Tools: 青少年编程教育 工具栈调研
> Track 02 — Youth Coding Education (locale=global) | 2026-05-26

---

## Source Manifest

| source_id | url | bucket | last_checked | author/host | one-line note |
|-----------|-----|--------|-------------|-------------|---------------|
| T02-S001 | https://scratch.mit.edu | verified_primary | 2026-05-26 | MIT Media Lab | Scratch官方 (.edu) |
| T02-S002 | https://code.org | surrogate_primary | 2026-05-26 | Code.org | vendor docs (行业协会) |
| T02-S003 | https://microbit.org | surrogate_primary | 2026-05-26 | Micro:bit Foundation | vendor docs (编程工具) |
| T02-S004 | https://arduino.cc | surrogate_primary | 2026-05-26 | Arduino LLC | vendor docs (编程工具) |
| T02-S005 | https://education.lego.com | surrogate_primary | 2026-05-26 | LEGO Education | vendor docs (机器人厂商) |
| T02-S006 | https://python.org | surrogate_primary | 2026-05-26 | Python Software Foundation | vendor docs (编程工具) |
| T02-S007 | https://replit.com | surrogate_primary | 2026-05-26 | Replit Inc. | vendor docs (课程平台) |
| T02-S008 | https://codeforces.com | surrogate_primary | 2026-05-26 | Codeforces | vendor docs (竞赛组织) |
| T02-S009 | https://luogu.com.cn | surrogate_primary | 2026-05-26 | 洛谷 | vendor docs (竞赛组织) |
| T02-S010 | https://makeblock.com | surrogate_primary | 2026-05-26 | Makeblock Co. | vendor docs (编程工具) |
| T02-S011 | https://tynker.com | surrogate_primary | 2026-05-26 | Tynker | vendor docs (课程平台) |
| T02-S012 | https://codemonkey.com | surrogate_primary | 2026-05-26 | CodeMonkey | vendor docs (课程平台) |
| T02-S013 | https://create.roblox.com | surrogate_primary | 2026-05-26 | Roblox Corp. | vendor docs (编程工具) |
| T02-S014 | https://vexrobotics.com | surrogate_primary | 2026-05-26 | VEX Robotics | vendor docs (竞赛组织) |
| T02-S015 | https://firstinspires.org | surrogate_primary | 2026-05-26 | FIRST | vendor docs (竞赛组织) |
| T02-S016 | https://raspberrypi.org | surrogate_primary | 2026-05-26 | Raspberry Pi Foundation | vendor docs (编程工具) |
| T02-S017 | https://snap.berkeley.edu | verified_primary | 2026-05-26 | UC Berkeley | Snap! (.edu) |
| T02-S018 | https://appinventor.mit.edu | verified_primary | 2026-05-26 | MIT | App Inventor (.edu) |
| T02-S019 | https://processing.org | surrogate_primary | 2026-05-26 | Processing Foundation | vendor docs (编程工具) |
| T02-S020 | https://p5js.org | surrogate_primary | 2026-05-26 | Processing Foundation | vendor docs (编程工具) |
| T02-S021 | https://khanacademy.org | surrogate_primary | 2026-05-26 | Khan Academy | vendor docs (课程平台) |
| T02-S022 | https://noi.cn | surrogate_primary | 2026-05-26 | CCF NOI | vendor docs (竞赛组织) |
| T02-S023 | https://github.com/codemao | surrogate_primary | 2026-05-26 | 编程猫 | vendor docs (编程工具) |
| T02-S024 | https://edsurge.com | surrogate_primary | 2026-05-26 | EdSurge | vendor docs (教育媒体) |
| T02-S025 | https://edweek.org | surrogate_primary | 2026-05-26 | Education Week | vendor docs (教育媒体) |
| T02-S026 | https://sonic-pi.net | surrogate_primary | 2026-05-26 | Sonic Pi | vendor docs (编程工具) |
| T02-S027 | https://moe.gov.cn | verified_primary | 2026-05-26 | 中国教育部 | verified_primary (政府) |
| T02-S028 | https://csteachers.org | surrogate_primary | 2026-05-26 | CSTA | vendor docs (行业协会) |
| T02-S029 | https://iste.org | surrogate_primary | 2026-05-26 | ISTE | vendor docs (行业协会) |
| T02-S030 | https://codecademy.com | surrogate_primary | 2026-05-26 | Codecademy | vendor docs (课程平台) |

---

## 工具栈总览表

| # | 工具 | 层级 | 年龄段 | 主要用途 | License |
|---|------|------|--------|---------|---------|
| 1 | Scratch | 必备 | 6-12岁 | block-based 编程入门 | open |
| 2 | Python | 必备 | 10-18岁 | 通用编程语言 | open |
| 3 | C/C++ | 必备 | 12-18岁 | 信奥赛核心语言 | open |
| 4 | Code.org | 必备 | 5-18岁 | 课程+平台一体化 | free |
| 5 | micro:bit | 必备 | 8-14岁 | 物理计算入门硬件 | open HW |
| 6 | Arduino | 必备 | 10-18岁 | 开源硬件编程 | open |
| 7 | LEGO SPIKE Prime | 必备 | 10-14岁 | 机器人套件+编程 | proprietary |
| 8 | Makeblock mBot | 必备 | 8-14岁 | 教育机器人硬件 | proprietary |
| 9 | Replit | 必备 | 10-18岁 | 在线IDE+协作 | freemium |
| 10 | 洛谷 OJ | 场景特化 | 12-18岁 | 信奥赛在线评测 | free |
| 11 | Codeforces | 场景特化 | 13-18岁 | 国际算法竞赛平台 | free |
| 12 | Tynker | 场景特化 | 7-16岁 | 游戏化课程平台 | proprietary |
| 13 | CodeMonkey | 场景特化 | 6-14岁 | 游戏化编程 | proprietary |
| 14 | Roblox Studio | 场景特化 | 10-18岁 | 游戏开发+Lua | free |
| 15 | MIT App Inventor | 场景特化 | 10-16岁 | 移动App block-based | open |
| 16 | Snap! | 场景特化 | 12-18岁 | CS Principles高级block | open |
| 17 | Teachable Machine | 场景特化 | 10-18岁 | AI/ML 无代码入门 | free |
| 18 | ml5.js | 场景特化 | 12-18岁 | 浏览器端ML编程 | open |
| 19 | Raspberry Pi | 场景特化 | 10-18岁 | 单板机项目平台 | open HW |
| 20 | Processing/p5.js | 场景特化 | 13-18岁 | 创意编程/数字艺术 | open |
| 21 | USACO Training | 场景特化 | 13-18岁 | 美国信奥竞赛训练 | free |
| 22 | Khan Academy CS | 场景特化 | 8-18岁 | 自学课程平台 | free |
| 23 | 编程猫 (CodemaoStudio) | 场景特化 | 6-16岁 | 中国block-based平台 | proprietary |
| 24 | GitHub Copilot (Edu) | 新兴 | 14-18岁 | AI辅助编程教学 | free for edu |
| 25 | Khanmigo | 新兴 | 8-18岁 | LLM-based AI辅导 | free |
| 26 | ClassIn | 新兴 | — | 教育直播+互动黑板 | proprietary |
| 27 | Minecraft: Edu | 场景特化 | 8-14岁 | 游戏化STEAM项目 | proprietary |
| 28 | Sonic Pi | 场景特化 | 10-18岁 | 音乐编程/创意CS | open |
| 29 | VEX Robotics | 场景特化 | 10-18岁 | 竞赛机器人套件 | proprietary |

---

## 工具详细卡片

### 1. Scratch (MIT)
- **One-liner**: MIT Media Lab 开发的 block-based 可视化编程平台，全球6-12岁编程入门事实标准。
- **Tier**: 必备
- **Maintainer/Owner**: MIT Media Lab (Lifelong Kindergarten Group)
- **License**: open (BSD-3, GPLv2)
- **Maturity signals**: 2007年首发; Scratch 3.0 2019年正式发布(HTML5，告别Flash); 截至2024年12月注册用户超 1.3 亿，月活项目创建者约 140 万; 最大年龄群体12岁(约900万用户)。evidence: [T02-S001]
- **典型使用场景**: 低龄学生编程启蒙 → 动画/游戏/故事叙述项目；学校CS课程导入；课后编程兴趣班第一阶段。
- **不适合/替代方案**: 不适合竞赛训练(无算法数据结构支持)；不适合文本编程学习目标 → 替代: Python + Replit；想要更高级块编程 → Snap!(Berkeley)。
- **生产案例**: 全球190+国家学校CS课程采用；英国National Computing Curriculum核心工具；中国小学信息技术课普遍使用。evidence: [T02-S001]
- **近期变化**: 2024年起官方统计页停止更新；2023-24年 Scratch AI 扩展(机器学习积木)上线; 官网不再显示实时用户数据。evidence: [T02-S001]
- **来源**: [T02-S001] scratch.mit.edu 官方; [T02-S024] EdSurge K12工具综述; JetLearn Scratch Statistics 2025 (jetlearn.com/blog/scratch-statistics)
- **可信度**: 高 (verified_primary + 多方佐证)
- **Decay risk**: 低 — MIT长期维护，但需关注AI扩展生态是否跟上

### 2. Python (语言生态)
- **One-liner**: 通用文本编程语言，10-18岁 K12 text-based 编程主力，AI/数据科学入门首选。
- **Tier**: 必备
- **Maintainer/Owner**: Python Software Foundation (PSF)
- **License**: open (PSF License, 兼容 GPL)
- **Maturity signals**: 1991年首发; Python 3.13 (2024-10); Stack Overflow 2025数据: Python 占 ML 职位 89%; GitHub 年度最流行语言(2023-2025连续); 全球 Tiobe 指数长期 Top 3。evidence: [T02-S006]
- **典型使用场景**: 10-14岁从Scratch过渡到文本编程; AP Computer Science Principles 主力语言; 机器学习启蒙 (scikit-learn/TensorFlow Kids API); 竞赛辅助刷题(NOI不推荐主力)。
- **不适合/替代方案**: 不适合NOI/IOI主力(评测效率/语言限制) → C++; 不适合6-9岁初学者 → Scratch。研究显示有Scratch基础的孩子学Python快30-40%。evidence: [T02-S006]
- **生产案例**: 英国GCSE CS考试指定语言之一; 美国AP CS Principles广泛使用; 国内各大少儿编程机构10岁+课程主力语言。
- **近期变化**: Python 3.13 引入 JIT 编译器(性能提升); 各大AI平台(OpenAI/Anthropic)的 SDK 均以 Python 为首选 → 增加对年轻学习者吸引力。
- **来源**: [T02-S006] python.org; codingal.com Scratch vs Python 对比 (2025); logicbox.ac Scratch vs Python 2025
- **可信度**: 高
- **Decay risk**: 极低 — AI 时代 Python 需求只增不减

### 3. C/C++ (信奥赛栈)
- **One-liner**: NOI/IOI/ICPC 官方指定语言，竞赛编程事实标准，高性能算法实现核心工具。
- **Tier**: 必备 (竞赛赛道)
- **Maintainer/Owner**: ISO/IEC (标准); GCC/LLVM (主要编译器开源社区)
- **License**: open (GCC: GPLv3; Clang: Apache 2.0)
- **Maturity signals**: C++17/20/23 标准持续演进; NOI 2024 支持 C++14/17; IOI 2025 Bolivia 指定 C++17; 历届 IOI 金牌绝大多数用 C++ 提交。evidence: [T02-S022]
- **典型使用场景**: 信奥赛全栈(NOIP→CSP→NOI→IOI); 数据结构与算法竞赛; 高端编程思维培养。
- **不适合/替代方案**: 不适合8-12岁初学者(语法严格/调试难); 非竞赛方向可选Python; 2022年起NOI逐步淘汰Pascal，C++垄断地位进一步强化。evidence: [T02-S022]
- **生产案例**: 全国信奥联赛(NOIP/CSP-J/CSP-S)唯一实用语言; 各大竞赛培训机构12岁+班级标配; IOI 2024/2025 参赛主力语言。
- **近期变化**: Pascal 在 NOI 中的地位基本消失; C++17 成为竞赛标准; LLM 对 C++ 的代码补全能力大幅提升,部分机构开始引入 AI 辅助学习。
- **来源**: [T02-S022] noi.cn; [T02-S008] codeforces.com IOI archive; eduseed.in IOI training guide 2025
- **可信度**: 高
- **Decay risk**: 低 — 竞赛体系稳定，短期无替代风险

### 4. Code.org
- **One-liner**: 非营利课程+平台一体化解决方案，从 Hour of Code 到 CS Discoveries/CS Principles 完整 K-12 路径。
- **Tier**: 必备
- **Maintainer/Owner**: Code.org (非营利机构，2013年成立，资金来自微软/谷歌/Amazon等)
- **License**: 免费使用 (Creative Commons 课程; 平台 proprietary)
- **Maturity signals**: 2013年创立; Hour of Code 全球2亿+参与者; 78万+注册教师; 覆盖全球180+国家/35种语言。evidence: [T02-S002]
- **典型使用场景**: 学校正式CS课程(CS Fundamentals K-5; CS Discoveries 6-10; CS Principles 9-12); 编程启蒙 Hour of Code 活动; 培训机构导入课程; 教师PD (Professional Development)。
- **不适合/替代方案**: 不适合竞赛专项训练; 平台内容较基础，高阶需补充 → Replit/洛谷; 中国网络访问可能不稳定。
- **生产案例**: 美国公立学校 K-12 CS 课程主要平台; 国内部分国际学校和双语学校采用 CS Principles。
- **近期变化**: 2024年新增 AI for Oceans / AI literacy 模块; 与微软合作推出 AI & Machine Learning 课程; 持续扩展 Hour of Code 游戏化内容。evidence: [T02-S002]
- **来源**: [T02-S002] code.org 官方; [T02-S028] csteachers.org K12 CS标准对照; edtechindex.org CS教育平台对比
- **可信度**: 高 (surrogate_primary 行业协会级别)
- **Decay risk**: 低 — 有大科技公司资金背书，课程持续更新

### 5. micro:bit (BBC)
- **One-liner**: 口袋大小的物理计算开发板，内置传感器+LED矩阵，教育专属设计，全球最流行的K12入门硬件之一。
- **Tier**: 必备
- **Maintainer/Owner**: Micro:bit Educational Foundation (英国非营利)
- **License**: open hardware (CC BY-SA 4.0); MakeCode 编辑器 MIT
- **Maturity signals**: 2016年首发(英国全国小学生免费发放100万块); V2 2020年发布(新增麦克风/扬声器/触摸Logo); 全球70+国家部署; 约6,000万台在用。evidence: [T02-S003]
- **典型使用场景**: 8-14岁物理计算入门; BBC MakeCode editor(block→Python渐进); 传感器项目/小游戏/物联网启蒙; 配合 LEGO 构件做简单机器人。
- **不适合/替代方案**: 处理能力有限，不适合复杂AI推理; 高级项目 → Raspberry Pi 或 Arduino; 价格约 $17-20/块，批量采购友好。evidence: [T02-S003]
- **生产案例**: 英国Computing课程标配; 香港小学STEM课广泛采用; 国内各省市创客教育常用硬件; 与洛谷等平台无竞争(不同赛道)。
- **近期变化**: 2023年 micro:bit V2.21 固件更新; 扩展传感器生态(Kitronik/SparkFun 扩展板); Python 编程比例逐步提高，Blocks 比例下降。evidence: [T02-S003]
- **来源**: [T02-S003] microbit.org 官方; picobricks.com Microbit vs Arduino 对比; futurebots.academy Arduino vs Microbit 2025
- **可信度**: 高
- **Decay risk**: 低 — 非营利基金会长期维护，英国课程政策背书

### 6. Arduino
- **One-liner**: 开源微控制器平台，C/C++ 编程，创客教育和中高年级硬件项目的事实标准。
- **Tier**: 必备
- **Maintainer/Owner**: Arduino LLC / Arduino S.r.l. (意大利开源硬件公司)
- **License**: open hardware (CC BY-SA); Arduino IDE 开源 (LGPL/GPL)
- **Maturity signals**: 2005年首发; Arduino Uno 全球最畅销开发板(估计5000万+销量); GitHub arduino/Arduino: ~14k stars; IDE 2.x (2022+) 持续活跃维护; 全球创客社区极其庞大。evidence: [T02-S004]
- **典型使用场景**: 10-18岁中高年级硬件编程; 电子电路入门; STEAM项目(光感/温度/运动传感器); 高校前置创客教育; FRC/创客马拉松工具链。
- **不适合/替代方案**: 不适合8岁以下(焊接/电路风险); 对编程入门者语法门槛高 → 先用micro:bit; 无网络/AI功能 → 树莓派; Elegoo UNO系列是最常见平替(更便宜)。evidence: [T02-S004]
- **生产案例**: Elegoo UNO Smart Robot Car Kit ($70) 最受学生欢迎的入门套件; 国内STEAM课套件标配; 各大机器人竞赛自制机器人常用。
- **近期变化**: Arduino IDE 2.3 (2024) 支持云同步; Arduino Cloud 扩展 IoT 教育功能; MicroPython 对 Arduino 的支持改善(部分型号)。
- **来源**: [T02-S004] arduino.cc 官方; keyirobot.com STEM Robot Top 10 对比; antoniadis.com.cy micro:bit vs Arduino 教育对比 2025
- **可信度**: 高
- **Decay risk**: 低 — 开源生态+庞大社区，长期稳定

### 7. LEGO SPIKE Prime / Mindstorms
- **One-liner**: LEGO Education 旗舰机器人套件，Scratch blocks + Python 双语言，WRO/FLL 竞赛官方指定硬件。
- **Tier**: 必备 (机器人竞赛赛道)
- **Maintainer/Owner**: LEGO Education (LEGO Group 子公司)
- **License**: proprietary (硬件+软件); LEGO Education SPIKE App 免费
- **Maturity signals**: SPIKE Prime 2019年发布; SPIKE Essential (低龄版) 2021发布; Mindstorms EV3 2022年停产宣告; STM32F413 Hub + 3电机+距离/力/颜色传感器+520+ Technic零件。evidence: [T02-S005]
- **典型使用场景**: 10-14岁竞赛机器人(FLL/WRO); 学校STEAM项目; Scratch block编程到Python过渡; 传感器探究式学习。
- **不适合/替代方案**: 价格高($400-500套件) → 预算有限选mBot2或micro:bit+扩展; EV3已停产勿再采购; SPIKE Prime Hub 不支持直接 Wi-Fi/IoT。evidence: [T02-S005]
- **生产案例**: FIRST LEGO League (FLL) 全球官方指定平台; 国内WRO、乐高联赛选手标配; 大量K12机器人课程体系围绕 SPIKE Prime 设计。
- **近期变化**: EV3 2022年正式宣布停产，库存耗尽; SPIKE Prime 成为 LEGO Education 机器人主力; 2024年 SPIKE App 更新 Python 调试体验; Mindstorms 品牌消失，统一LEGO Education品牌。evidence: [T02-S005]
- **来源**: [T02-S005] education.lego.com 官方; onoff.gr Educational Robots 2026 综述; techedubyte.com 硬件对比
- **可信度**: 高
- **Decay risk**: 中 — LEGO 单方面决策停产风险存在(EV3 前车之鉴)，需关注 SPIKE 3 路线图

### 8. Makeblock mBot / Codey Rocky
- **One-liner**: 深圳 Makeblock 出品的教育机器人套件，mBot2(CyberPi)主打8-14岁，mBlock图形编程，性价比高。
- **Tier**: 必备 (中国市场)/场景特化 (国际)
- **Maintainer/Owner**: Makeblock Co., Ltd. (深圳，2011年成立，纽交所上市)
- **License**: proprietary 硬件; mBlock 编辑器部分开源 (基于Scratch 3)
- **Maturity signals**: mBot 1代 2013年发布，Kickstarter爆款; mBot2 (CyberPi hub) 2021年; Codey Rocky 2018年; 全球销量超300万台(公司数据); 国内STEAM课标配之一。evidence: [T02-S010]
- **典型使用场景**: 8-14岁编程+机器人入门; mBlock(Scratch兼容) → Python 双轨; 创客课堂和STEAM兴趣班; 国内联赛/省市创客大赛; Codey Rocky适合低龄(5岁+简化版)。
- **不适合/替代方案**: 国际竞赛认可度低于VEX/LEGO; 高端竞赛选LEGO SPIKE或VEX; 软件生态不如LEGO丰富; 长期固件更新支持有待验证。evidence: [T02-S010]
- **生产案例**: 中国教育局STEAM采购标配之一; 国内各省市"编程进课堂"项目常用硬件; 配合编程猫课程体系有深度整合。
- **近期变化**: mBot2 引入 AI 视觉识别模块(CyberPi AI Camera); 与科大讯飞合作AI启蒙套件; 2024年发布 mBot Ranger 2 高级版。
- **来源**: [T02-S010] makeblock.com 官方; 行业机器人硬件综述 (edtechindex.org); robotics education comparison 2025
- **可信度**: 中高 (vendor docs，中国市场数据较难独立核实)
- **Decay risk**: 中 — 上市公司，资金稳定，但国际竞争力弱

### 9. Replit
- **One-liner**: 浏览器端全栈 IDE + 协作平台，支持50+语言即开即写，AI Agents 深度集成，2024年教育版已停止免费。
- **Tier**: 必备 (个人)/场景特化 (机构，需重新评估)
- **Maintainer/Owner**: Replit Inc. (美国，2016年成立)
- **License**: proprietary (SaaS); 部分开源工具
- **Maturity signals**: 2016年成立; 2022年估值$8亿; Teams for Education 于 **2024年8月1日正式停止** (重大变化!); 当前免费 Starter 仅含 $3 credits; 付费 Core $20/月; GitHub: replit/replit.github.io 活跃。evidence: [T02-S007]
- **典型使用场景**: 10-18岁在线编写Python/JS/HTML无需安装环境; 竞赛练习快速调试; 课堂即时coding演示; 个人项目hosting; 现在主打 AI Agents 辅助开发。
- **不适合/替代方案**: **教育机构免费批量使用已不可行** (Teams for Edu 停止); 替代: JDoodle (免费 IDE)、Pickcode (教育专属)、CodeHS、JuiceMind; 国内访问速度较慢。evidence: [T02-S007]
- **生产案例**: 2021-2023年大量美国K12 CS课程基于 Teams for Education; 停止后学校大量迁移; 仍有个人学生用免费账户练习。
- **近期变化**: 2024年8月 Teams for Education 停止是最大负面信号; 转型为 AI Agents 平台; Replit Agent 可自动生成完整项目; 教育市场份额被竞品快速蚕食。evidence: [T02-S007]
- **来源**: [T02-S007] replit.com/pricing; datawars.io Replit Teams for Education Deprecation; blog.pickcode.io Replit alternatives 2025
- **可信度**: 高 (停止信息经多方证实)
- **Decay risk**: 高(教育场景) — 免费教育版已停止，需密切关注定价策略

### 10. 洛谷 OJ (Luogu)
- **One-liner**: 中国最大的信奥在线评测平台，14000+题目，NOI/CSP 赛前日均提交量15-25万，中文友好，非营利模式。
- **Tier**: 场景特化 (竞赛训练)
- **Maintainer/Owner**: 洛谷网络 (北京，2013年成立，非营利/公益模式)
- **License**: proprietary (免费使用, 内容部分 CC)
- **Maturity signals**: 2013年创立; 题库 14,000+ 题(2024年); 赛前日提交量 150,000-250,000; 中国最大竞赛OJ之一; 社区论坛极活跃。evidence: [T02-S009]
- **典型使用场景**: 12-18岁 NOI/CSP-J/CSP-S/NOIP 赛前刷题; 题目按难度分级(入门→CSP-S+); 配套题解社区和讨论区; 机构统一提交管理; 月赛/练习赛。
- **不适合/替代方案**: 非竞赛选手不推荐(门槛高且内容纯算法); 国际竞赛备赛需补充 Codeforces/USACO; 界面对10岁以下不友好。evidence: [T02-S009]
- **生产案例**: 国内各大竞赛培训机构(高思/震宇/竞思等)均将洛谷作为刷题平台; 全国 CSP 赛前必刷平台; 个人 Acc 显示历史提交记录。
- **近期变化**: 2022+加强未成年账号管理; 2024年新增 AI 题解辅助功能(争议); 与 NOI 官方 noi.cn 保持非官方密切配合; 支持 C++17。evidence: [T02-S009]
- **来源**: [T02-S009] luogu.com.cn; grokipedia.com Luogu介绍; codeforces.com blog entry 103454 "What is Luogu"; codeforces.com NOI/IOI中国介绍 entry 131266
- **可信度**: 高
- **Decay risk**: 低 — 中国信奥赛体系支柱平台，用户粘性极高

### 11. Codeforces
- **One-liner**: 全球最大算法竞赛社区，每周举办 Div.1-4 比赛，IOI/ICPC 选手必备训练平台，俄罗斯团队运营。
- **Tier**: 场景特化 (竞赛训练)
- **Maintainer/Owner**: Codeforces (Mikhail Mirzayanov 团队; 目前由 MES 教育科学部赞助, 俄罗斯)
- **License**: proprietary (免费使用)
- **Maturity signals**: 2010年创立; 注册用户 900万+(2024); 每周 2-3 场 rated 比赛; IOI 历届题目存档 (ioi.contest.codeforces.com); 全球 Rating 体系权威。evidence: [T02-S008]
- **典型使用场景**: 13-18岁高阶竞赛选手 rated 训练; Educational Codeforces Rounds 学习新算法; IOI/NOIP 题目存档复习; 中国强校集训对抗赛。
- **不适合/替代方案**: 不适合初学者(Div.3起步题仍难); 对10岁以下完全不友好; 备赛 NOI 需配合洛谷中文体系; 俄罗斯平台,部分地区网络访问不稳定。evidence: [T02-S008]
- **生产案例**: IOI 2025 Bolivia 题目在 Codeforces 存档; 全球 Rating 系统被 NOI 选手广泛参照; 国内竞赛培训高阶段必用。
- **近期变化**: 2024-25年新增 AI 生成测试数据研究引发讨论(arXiv 2506.06821); Codeforces Round 持续高频; 中国用户占活跃用户大比例。evidence: [T02-S008]
- **来源**: [T02-S008] codeforces.com; ioinformatics.org IOI官方; usaco.guide/general/olympiads 平台综述
- **可信度**: 高
- **Decay risk**: 中 — 俄罗斯政治风险存在；但替代平台(AtCoder/USACO)暂无法完全替代其规模

### 12. Tynker
- **One-liner**: 游戏化课程平台，7-16岁，从 block 到 Python/JS，以 Minecraft Mod 制作为核心差异化卖点。
- **Tier**: 场景特化
- **Maintainer/Owner**: Tynker (美国, 2012年成立; 2021年被 BYJU'S 收购; BYJU'S 2023-24财务危机影响)
- **License**: proprietary (freemium; 学校版/家庭版付费)
- **Maturity signals**: 2012年创立; 60,000+学校; 100M+学生注册(公司声称); 但 BYJU'S 母公司 2023-24年严重财务危机影响运营稳定性。evidence: [T02-S011]
- **典型使用场景**: 7-16岁游戏化编程课程; Minecraft Mod 制作(Tynker 独家); block → Python/JS 渐进课程; 美国课外编程辅导。
- **不适合/替代方案**: BYJU'S 财务危机带来运营不确定性 → 新机构采购需谨慎; 竞赛方向不适合; 国内几乎无用户。替代: Scratch(免费) + CodeMonkey。evidence: [T02-S011]
- **生产案例**: 美国K-8 CS课外辅导主力; Camp Tynker 暑期编程营; 与 Minecraft Education 有深度内容整合。
- **近期变化**: BYJU'S 2024年宣告破产保护，Tynker 作为子品牌命运未定; 产品本身仍在运营但投资/更新节奏放缓; 需密切跟踪收购/剥离信息。
- **来源**: [T02-S011] tynker.com; create-learn.us kids coding platform综述; codakid.com best coding platforms 2025
- **可信度**: 中 (BYJU'S危机增加不确定性)
- **Decay risk**: 高 — BYJU'S 财务危机直接威胁平台持续运营

### 13. CodeMonkey
- **One-liner**: 基于游戏任务的编程学习平台，6-14岁，用真实 Python/CoffeeScript 语法完成关卡，趣味性强。
- **Tier**: 场景特化
- **Maintainer/Owner**: CodeMonkey Studios (以色列, 2014年成立)
- **License**: proprietary (学校版订阅制; 部分内容免费试用)
- **Maturity signals**: 2014年; 85+国家; 500,000+学生(公司声称); 持续更新; 2023年引入 AI Chat-based 编程辅导功能。evidence: [T02-S012]
- **典型使用场景**: 6-14岁通过游戏任务学习真实 Python 语法; 学校STEM课轻量导入; 无需教师编程背景即可布置。
- **不适合/替代方案**: 不适合竞赛方向; 语言限制(不支持所有语言); 价格对大班不友好。替代: Code.org(免费) 或 Scratch。
- **生产案例**: 以色列、美国中小学 CS 课导入; 有教师控制台和班级管理功能。
- **近期变化**: 2023年 AI 辅导功能上线; 扩展 Data Science 模块面向中学生; 持续优化游戏关卡体系。
- **来源**: [T02-S012] codemonkey.com; create-learn.us coding platforms kids; idtech.com best programming languages kids 2026
- **可信度**: 中高
- **Decay risk**: 低中 — 独立运营，无大集团财务风险

### 14. Roblox Studio
- **One-liner**: Roblox 官方游戏开发 IDE，Lua 语言，10-18岁通过"做游戏赚Robux"驱动深度学习，全球最大用户基数。
- **Tier**: 场景特化
- **Maintainer/Owner**: Roblox Corporation (美国纽交所上市)
- **License**: proprietary 平台; Lua 语言 MIT
- **Maturity signals**: Roblox Studio 2006年; Roblox MAU 8000万+(2024); 每天200万+活跃开发者; 青少年开发者收入分成体系激励。evidence: [T02-S013]
- **典型使用场景**: 10-18岁游戏开发驱动编程学习(Lua); 3D世界/多人游戏创作; STEAM创意课; 提前接触游戏发布和商业化逻辑。
- **不适合/替代方案**: Lua不是主流语言，学完需二次过渡; 13岁以下需家长监控设置; 竞赛无关; 学校部署需企业账户配置。替代: Unity(更专业) / Scratch(低龄)。evidence: [T02-S013]
- **生产案例**: 美国Course at Roblox Education 免费课程; 全球无数课外编程班以"Roblox游戏开发"为卖点招生; 国内部分机构有"乐高+Roblox"联合课。
- **近期变化**: 2024年 Roblox 推出 AI 代码生成辅助 (AI Studio插件); 引入 AI NPC 功能; 平台持续扩大创作者经济体系。
- **来源**: [T02-S013] create.roblox.com; create-learn.us 2026 coding apps kids; devopscube.com best coding websites 2026
- **可信度**: 高
- **Decay risk**: 低 — 上市公司，用户基数庞大，但 Lua 作为单一语言是长期隐患

### 15. MIT App Inventor
- **One-liner**: MIT 出品的 block-based 移动 App 开发工具，无需代码即可在 Android 上发布真实 App，面向10-16岁。
- **Tier**: 场景特化
- **Maintainer/Owner**: MIT Center for Mobile Learning
- **License**: open (Apache 2.0)
- **Maturity signals**: 2010年Google开发，2012年转交MIT; 约800万注册用户(MIT数据); GitHub: mit-cml/appinventor-sources ~5k stars; 持续活跃维护(2024年版本)。evidence: [T02-S018]
- **典型使用场景**: 10-16岁移动应用开发启蒙; 学校项目式学习(连接传感器/GPS/摄像头); 女生编程吸引力强(应用创作导向); 高中CS课程移动端项目。
- **不适合/替代方案**: 仅支持Android(iOS受限); block-based限制复杂项目; 留存率偏低(项目完成后不易延伸)。替代方向: Flutter/React Native(更专业)。
- **生产案例**: 全球高中CS项目常用; 印度/拉美地区低成本移动开发培训标配; 与 MIT Scratch 形成 MIT 教育生态双翼。
- **近期变化**: 2023年 App Inventor AI 扩展(图像识别/Chatbot创建); 支持 IoT 设备连接(Arduino/micro:bit via BT); iOS 体验仍受限。evidence: [T02-S018]
- **来源**: [T02-S018] appinventor.mit.edu (.edu verified_primary); Wikipedia App Inventor; MIT官方数据
- **可信度**: 高
- **Decay risk**: 低 — MIT 长期维护，但使用场景较窄

### 16. Snap! (UC Berkeley)
- **One-liner**: Berkeley 出品的高级 block-based 语言，支持高阶函数/Lambda，AP CSP "Beauty and Joy of Computing" 官方工具。
- **Tier**: 场景特化
- **Maintainer/Owner**: UC Berkeley (Jens Mönig & Brian Harvey)
- **License**: open (AGPL-3.0)
- **Maturity signals**: 2011年首发(基于 Scratch 扩展); GitHub: jmoenig/Snap ~ 1.1k stars; BJC (Beauty and Joy of Computing) 覆盖美国50州AP CSP课程; 持续更新(2024年 Snap! 10.0)。evidence: [T02-S017]
- **典型使用场景**: 12-18岁高级块编程; BJC AP CSP 课程指定工具; 高中CS理论入门(递归/高阶函数); 从 Scratch 过渡到函数式思维。
- **不适合/替代方案**: 不适合6-10岁初学者; 中国几乎无使用场景; 独立使用生态小 → 主要作为 BJC 课程工具使用。替代: 直接学 Python。evidence: [T02-S017]
- **生产案例**: BJC 课程全美50+所高中; 部分国际 IB/AP 课程选用。
- **近期变化**: Snap! 10.0 (2024) 新增改进的 AI 积木扩展; 与 Scratch 保持兼容性更新。
- **来源**: [T02-S017] snap.berkeley.edu (.edu verified_primary); bjc.edc.org BJC课程官方; Wikipedia Snap!
- **可信度**: 高 (edu域名)
- **Decay risk**: 低 — Berkeley 学术项目，但用户圈子小

### 17. Teachable Machine (Google)
- **One-liner**: Google 出品的零代码机器学习工具，浏览器内训练图像/声音/姿态分类模型，K12 AI 启蒙最低门槛工具。
- **Tier**: 场景特化
- **Maintainer/Owner**: Google Creative Lab
- **License**: free to use; 模型导出 Apache 2.0
- **Maturity signals**: 2019年 V1; 2020年 V2(增加声音/姿势项目); 无公开用户数据; 研究显示对幼儿园及以上年龄段均有效; 2023年 Springer 发表幼儿园适用性研究(link.springer.com)。evidence: [T02-S001] via AI搜索
- **典型使用场景**: 10-18岁 AI/ML 概念启蒙; "我训练了一个AI"的第一个项目; 与Scratch/p5.js集成做AI互动项目; 学校AI素养课; 幼儿园探索式学习(有研究支持3-9岁可用)。
- **不适合/替代方案**: 不支持复杂模型(只有分类); 数据隐私需关注(训练图片上传Google); 企业内网环境需测试; 进阶 → ml5.js/Python sklearn。
- **生产案例**: 全球AI素养课标准工具; CSTA AI For K-12 框架配套工具之一; Code.org AI 模块中引用。
- **近期变化**: Teachable Machine 网站保持稳定但更新较少; Google 2024年未发布重大更新; AI素养教育需求推动使用量上升。
- **来源**: kidsaitools.com AI learning tools K12 2025; link.springer.com AI learning tools K12 scoping review; thethinkacademy.com AI Education Tools K-12
- **可信度**: 高
- **Decay risk**: 中 — Google 可能随时停止维护(历史前车之鉴)，但当前稳定

### 18. ml5.js
- **One-liner**: 基于 TensorFlow.js 的高级机器学习 JS 库，专为艺术家/教育者设计，p5.js 生态重要成员，纯浏览器运行。
- **Tier**: 场景特化
- **Maintainer/Owner**: NYU ITP (Daniel Shiffman 团队，Processing Foundation 支持)
- **License**: open (MIT)
- **Maturity signals**: 2018年; GitHub: ml5js/ml5-library ~6.3k stars; 2023年 ml5.js v1.0 重写(Breaking Change); NYU ITP教学核心工具; YouTube "The Coding Train" 系列推广。evidence: [T02-S020]
- **典型使用场景**: 12-18岁 JS + p5.js 基础上叠加ML能力; 姿态检测/物体识别/文本生成创意项目; 高中AP CS / IB 艺术科技交叉课程; 创意编程工作坊。
- **不适合/替代方案**: 需要 JS + p5.js 基础，不适合零基础; 信号薄弱(非主流K12工具); 中国几乎无使用 → Teachable Machine更易上手。
- **生产案例**: NYU ITP 研究生教学; Processing Community Day 工作坊; The Coding Train 系列视频(YouTube 170万订阅)。
- **近期变化**: v1.0 (2023) API 重大重构; 新增 LLM Sketch integration (2024); 与 p5js 社区深度整合。
- **来源**: [T02-S020] p5js.org; ml5js GitHub; ml5js.org 官方
- **可信度**: 中高 (信号薄弱，主要在艺术/设计圈)
- **Decay risk**: 中 — 学术主导项目，商业化弱，维护依赖少数核心开发者

### 19. Raspberry Pi
- **One-liner**: 英国非营利出品的低成本单板计算机，$35-70，运行完整Linux，MicroPython/Python/Scratch均支持，创客高阶平台。
- **Tier**: 场景特化
- **Maintainer/Owner**: Raspberry Pi Foundation (英国非营利) + Raspberry Pi Ltd (商业臂)
- **License**: open HW (部分); 系统 Raspberry Pi OS 开源 (Debian based)
- **Maturity signals**: 2012年首发; Raspberry Pi 5 (2023年10月，Cortex-A76 2.4GHz); 全球销量 5800万台+(2023年Q1数据); 教育资源极丰富(raspberrypi.org projects)。evidence: [T02-S016]
- **典型使用场景**: 10-18岁中高级创客项目; IoT/AI摄像头/家庭服务器; 高中 CS 项目毕业设计; Astro Pi 竞赛(ISS太空项目); 配合 Python+传感器做完整系统。
- **不适合/替代方案**: 价格+周边成本较高; 需要 Linux 基础; 8岁以下操作困难。低龄替代: micro:bit; 简单项目替代: Arduino。evidence: [T02-S016]
- **生产案例**: 英国 Computing 高年级项目; 国内竞赛创客组项目; Astro Pi (ESA+RPi) — 国际学生在国际空间站运行代码竞赛; CoderDojo 全球网络标配。
- **近期变化**: Raspberry Pi 5 2023年发布(性能翻倍); 2024年 Raspberry Pi Pico 2 发布(RP2350); Pi Foundation 持续扩展免费教学资源(projects.raspberrypi.org)。
- **来源**: [T02-S016] raspberrypi.org 官方; Arduino vs Microbit vs RPi 对比 2025; onoff.gr Educational Robots 2026
- **可信度**: 高
- **Decay risk**: 低 — 非营利基金会+成熟商业臂，销量持续增长

### 20. Processing / p5.js
- **One-liner**: 创意编程框架，Processing(Java)和p5.js(JS)，视觉/音频/交互艺术与编程教育结合，设计师程序员入门标准。
- **Tier**: 场景特化
- **Maintainer/Owner**: Processing Foundation (非营利)
- **License**: open (LGPL for Processing; LGPL/GPL for p5.js)
- **Maturity signals**: Processing 2001年; p5.js 2014年; GitHub processing/p5.js ~22k stars; p5.js Editor 活跃; 每年 Processing Community Day 全球活动; MIT Media Lab、NYU 等高校教学标配。evidence: [T02-S019][T02-S020]
- **典型使用场景**: 13-18岁计算机艺术/数据可视化入门; 设计专业学生编程课; 高中STEAM跨学科项目; 配合 ml5.js 做AI艺术。
- **不适合/替代方案**: 不适合竞赛; 不适合6-12岁初学者; 中国使用场景较少(主要设计院校)。竞赛方向替代: Python。
- **生产案例**: MIT Media Lab 课程; 全球创意编程工作坊标准; 纽约/旧金山设计学校 CS 课; 学生互动装置艺术项目。
- **近期变化**: p5.js 2.0 (2025, Breaking Change) — 完整重写的渲染引擎; 新增 WebGL 支持改善; p5.js 与 ml5.js v1 深度对齐。evidence: [T02-S020]
- **来源**: [T02-S019] processing.org; [T02-S020] p5js.org; Processing Foundation GitHub
- **可信度**: 高 (老牌开源项目)
- **Decay risk**: 低 — 非营利基金会+学术生态，但用户圈子仍属小众

### 21. USACO Training Portal / USACO Guide
- **One-liner**: 美国计算机奥林匹克官方训练系统 + 社区驱动的开源备赛指南(usaco.guide)，美国信奥选手必备双件套。
- **Tier**: 场景特化 (竞赛训练)
- **Maintainer/Owner**: USACO (University of Wisconsin-Milwaukee 主办); usaco.guide 社区驱动(Benjamin Qi 等前IOI金牌选手)
- **License**: free to use; usaco.guide 开源 (MIT)
- **Maturity signals**: USACO 竞赛始于1993; usaco.guide GitHub ~3.3k stars; 2024-25赛季持续运行; 国际知名度高(IOI美国队选拔通道)。evidence: via usaco.guide/general/olympiads
- **典型使用场景**: 13-18岁美国竞赛选手(Bronze→Silver→Gold→Platinum 四级); 国际选手参照美国题库练习; 系统性算法知识体系学习。
- **不适合/替代方案**: 仅英文; 中国选手补充平台(主要用洛谷+Codeforces); 入门难度高于洛谷。
- **生产案例**: 美国每年5000+USACO参赛学生; IOI美国队选拔官方渠道; 国内顶级竞赛生训练材料之一。
- **近期变化**: usaco.guide 2024年持续社区更新内容; USACO 2025赛季正常举行; 越来越多非美国选手使用 usaco.guide 作为系统学习资源。
- **来源**: usaco.guide; ioinformatics.org; eduseed.in IOI training guide 2025
- **可信度**: 高
- **Decay risk**: 低 — 官方竞赛体系稳定; usaco.guide 社区活跃

### 22. Khan Academy Computing
- **One-liner**: 免费开放的自学计算机课程体系，HTML/CSS/JS/Python/SQL全覆盖，配合 Khanmigo AI 辅导，无需教师。
- **Tier**: 场景特化
- **Maintainer/Owner**: Khan Academy (美国非营利, 2008年成立)
- **License**: free (CC BY-NC-SA 内容); 平台 proprietary
- **Maturity signals**: 2008年创立; 全球1.5亿注册用户; 55种语言; Khanmigo AI 辅导 2023年上线(Microsoft Azure OpenAI 提供支持); 2024年 K-12 教师免费使用 Khanmigo。evidence: [T02-S021]
- **典型使用场景**: 8-18岁自学; 农村/资源匮乏地区零成本CS学习; 家庭教育; 课后补充; Khanmigo辅导个性化学习路径。
- **不适合/替代方案**: 不提供结构化班级管理; 自学需要自律; 竞赛方向内容较浅 → 洛谷/Codeforces; 中国访问速度受限。
- **生产案例**: 美国公立学校补充资源; 印度/巴基斯坦/尼日利亚等发展中国家免费CS教育主力; LearnStorm 全国挑战赛。
- **近期变化**: Khanmigo 2024年面向所有K-12教师免费开放(Microsoft合作); 2024年新增 AI Tutor for Students 功能; 与 College Board AP CS 课程对齐。evidence: [T02-S021]
- **来源**: [T02-S021] khanacademy.org; khanmigo.ai; microsoft.com Khan Academy Microsoft partnership
- **可信度**: 高 (非营利+微软背书)
- **Decay risk**: 低 — 非营利+大科技公司资助，长期稳定

### 23. 编程猫 (Codemao / CodemaoStudio)
- **One-liner**: 中国最大少儿编程平台，基于 Scratch 深度本地化，配套培训机构课程体系和教师端管理，主攻中国市场。
- **Tier**: 场景特化 (中国市场)/必备 (国内机构)
- **Maintainer/Owner**: 深圳点猫科技有限公司 (2015年成立, 已完成多轮融资)
- **License**: proprietary (免费基础版; 机构订阅)
- **Maturity signals**: 2015年成立; 累计注册用户 5000万+(公司声称,2023年); 合作机构 3万+; Kitten(积木) + Python模式; 与中国教育部编程进课堂政策紧密配合。evidence: [T02-S023]
- **典型使用场景**: 6-16岁中国少儿编程启蒙; 培训机构课程管理+作品展示; 学校STEAM课本地化内容; AI启蒙模块(配合讯飞/百度AI接口)。
- **不适合/替代方案**: 仅中文; 境外访问速度很差; 课程深度低于国际平台高阶内容; 竞赛赛道无支持。国际项目不推荐。evidence: [T02-S023]
- **生产案例**: 全国数万家编程培训机构使用编程猫作为教学平台; 部分省市将编程猫纳入信息技术课辅助工具; 与Makeblock/科大讯飞有联合产品。
- **近期变化**: 2023年推出 AI+编程课程线; 接入大模型做编程导师功能; 2024年发布图形化AI编程积木套件。
- **来源**: [T02-S023] github.com/codemao; codemao.cn 官方(非黑名单); 行业综述搜索结果
- **可信度**: 中高 (vendor数据需打折; 无独立审计)
- **Decay risk**: 中 — 中国教育行业监管风险; 政策变化敏感

### 24. GitHub Copilot for Education (Student Plan)
- **One-liner**: GitHub 面向学生的免费 AI 代码补全工具，2026年3月重组为 Copilot Student 计划，高中+大学生可申请。
- **Tier**: 新兴
- **Maintainer/Owner**: GitHub / Microsoft
- **License**: free for verified students/teachers
- **Maturity signals**: GitHub Education 2014年; Copilot for Students 2022年; **2026年3月12日** 重组为 Copilot Student Plan; GitHub Student Developer Pack 包含大量工具; 高校采用率快速上升。evidence: github.com education docs
- **典型使用场景**: 14-18岁学生在 VS Code/IDE 内使用 AI 代码补全; 竞赛辅助(争议); 个人项目加速; 教师减少重复代码讲解时间。
- **不适合/替代方案**: 需 edu 邮箱或学校认证(K-12认证较复杂); 可能助长抄答案风险; 竞赛场景禁用; 中国网络环境访问受限。替代: Cursor + Claude(更强大但收费)。evidence: docs.github.com
- **生产案例**: 美国大量高中CS教师已引入; Google/Microsoft 合作推广; 国内少数国际学校试用。
- **近期变化**: 2026年3月 Copilot Student 计划重组(去除部分高级模型自选); Copilot Free 版(无需学生认证)每月2000次补全; AI Agents/Workspace 功能快速迭代。evidence: github.com/orgs/community/discussions/189268
- **来源**: github.com/education/students (surrogate_primary vendor docs); docs.github.com Copilot Student; compilefuture.com guide 2025
- **可信度**: 高
- **Decay risk**: 低 — Microsoft 战略级产品，持续投入

### 25. Khanmigo (AI 辅导)
- **One-liner**: Khan Academy 基于 GPT-4/Azure OpenAI 的 AI 教学助手，用 Socratic 对话引导而非直接给答案，2024年对教师全免费。
- **Tier**: 新兴
- **Maintainer/Owner**: Khan Academy (非营利); 技术由 Microsoft Azure OpenAI 提供
- **License**: free for K-12 teachers (2024年起); 学生版免费测试中
- **Maturity signals**: 2023年3月发布; 2024年8月面向美国K-12教师全免费; Microsoft 合作正式公告; 独立产品域名 khanmigo.ai。evidence: [T02-S021]
- **典型使用场景**: 学生数学/科学/CS个性化辅导; 苏格拉底式问答防止直接给答案; 教师备课助手; 编程课概念解释; 差异化教学支持。
- **不适合/替代方案**: 目前主要针对美国课程体系; 中文支持有限; 编程专项深度低于专业coding平台; LLM 幻觉风险需教师监督。
- **生产案例**: 美国公立学校 pilot 项目(多州); 与 Instructure/Canvas LMS 集成; Project ECHO 教师培训项目。evidence: khanmigo.ai
- **近期变化**: Khanmigo ECHO 2024年扩展教师培训; Khanmigo for Teachers 功能快速迭代(课程计划生成/评估报告); 预计2025-26年覆盖更多国家。evidence: [T02-S021]
- **来源**: [T02-S021] khanmigo.ai; microsoft.com Khan Academy partnership; projectecho.unm.edu Khanmigo ECHO; instructure.com Khanmigo K12
- **可信度**: 高 (Microsoft合作背书)
- **Decay risk**: 低 — 非营利+Microsoft战略投资，持续发展

### 26. ClassIn
- **One-liner**: 中国教育科技公司 EEO 出品的在线互动课堂平台，双向互动黑板+多人视频+录播，中国培训机构直播课首选。
- **Tier**: 新兴 (管理/运营工具)
- **Maintainer/Owner**: 北京一起教育科技有限公司 (EEO, 2015年成立)
- **License**: proprietary (freemium → paid)
- **Maturity signals**: 2015年成立; 疫情期间爆发增长; 全球200+国家注册; 2024年重新调整定价策略; 与 Zoom/腾讯课堂直接竞争。evidence: ClassIn官网(classin.com)
- **典型使用场景**: 在线编程课直播教学(教师写代码学生看+实时标注); 互动黑板支持数学推导/流程图; 分组课堂; 课堂录播回放; 大班+小班混合。
- **不适合/替代方案**: 价格2024年上调，小机构成本压力; 国际学员视频卡顿; 技术要求较高。替代: Zoom+协作代码工具(低成本); 腾讯课堂(国内更便宜)。
- **生产案例**: 好未来/新东方在线均有使用; 国内大量K12编程机构(编程猫合作机构)标配; 疫情期间全国中小学远程课标准之一。
- **近期变化**: 2024年定价重组; 推出 AI 智能导学功能; 与大模型厂商合作推出课堂 AI 助教。
- **来源**: classin.com (surrogate_primary vendor); edtechindex.org; 教育行业综述
- **可信度**: 中高 (本土平台，数据难独立核实)
- **Decay risk**: 中 — 国内竞争激烈(腾讯课堂/钉钉课堂)，商业压力大

### 27. Minecraft Education Edition
- **One-liner**: Microsoft 教育版 Minecraft，内置 MakeCode/Python/JavaScript 编程，沉浸式 3D 世界 STEAM 教育载体。
- **Tier**: 场景特化
- **Maintainer/Owner**: Microsoft (Education 部门)
- **License**: proprietary (学校订阅制，部分免费课程)
- **Maturity signals**: 2016年教育版发布; 全球100+国家, 35,000+学校; 每年持续更新; 内置 MakeCode (block) + Python + JavaScript 编程界面; 与 Microsoft 365 深度集成。evidence: education.minecraft.net
- **典型使用场景**: 8-14岁沉浸式STEAM项目(建筑/物理/历史/编程一体化); 数学/科学跨学科主题课; 代码连接器(Python控制游戏角色); 创意游戏设计课。
- **不适合/替代方案**: 需要 Microsoft 365 EDU 账号; 价格对个人较高; 编程深度有限(轻度使用); 游戏性强可能分散学习注意力。替代: Roblox Studio(更深度编程)。
- **生产案例**: 芬兰/美国/英国学校STEAM课标配; 联合国可持续发展项目课程; 国内部分国际学校和双语学校使用。
- **近期变化**: 2024年 Minecraft Education AI 功能(AI 建筑生成/NPC对话); 与 Khanmigo 风格的 AI 教师助手集成实验中; 免费 Minecraft Education Starter 限时课程扩展。
- **来源**: education.minecraft.net (surrogate_primary vendor); create-learn.us 2026 coding apps; edweek.org [T02-S025]
- **可信度**: 高 (Microsoft产品)
- **Decay risk**: 低 — Microsoft 战略级教育产品，长期投入

### 28. Sonic Pi
- **One-liner**: 树莓派官方音乐编程工具，用 Ruby 实时创作电子音乐，英国Computing课的音乐跨学科入口，中国极少使用。
- **Tier**: 场景特化 (英国) / 冷僻 (中国/亚洲)
- **Maintainer/Owner**: Sam Aaron (Cambridge University + Raspberry Pi Foundation 支持)
- **License**: open (MIT)
- **Maturity signals**: 2012年; GitHub: sonic-pi-net/sonic-pi ~8.3k stars; 持续更新(2024年 v4.x); 主要在英国和欧洲学校使用。evidence: [T02-S026]
- **典型使用场景**: 10-18岁音乐+编程跨学科; 英国 Computing 课音乐单元; 创意科技工作坊; 现场 live coding 演出。
- **不适合/替代方案**: Ruby语法对初学者较陌生; 中国几乎无课程生态支撑; 纯音乐编程限制了应用场景。替代: Processing+声音库(更通用)。
- **生产案例**: 英国中小学Computing课; Raspberry Pi Foundation 官方推荐项目; 国际 live coding 艺术圈小众使用。
- **近期变化**: Sonic Pi v4.4 (2024) 改善稳定性; 支持 macOS/Windows/Linux/Raspberry Pi; 社区规模稳定但未见增长。
- **来源**: [T02-S026] sonic-pi.net; raspberrypi.org projects; GitHub sonic-pi-net/sonic-pi
- **可信度**: 高 (开源，数据可查)
- **Decay risk**: 中 — 单一维护者依赖度高，但有基金会支持

### 29. VEX Robotics
- **One-liner**: 美国竞赛机器人套件，VEX IQ (小学) + VEX V5 (中高中)，VRC 是全球最大学生机器人联赛，C++ 编程。
- **Tier**: 场景特化 (竞赛)
- **Maintainer/Owner**: Innovation First International (IFI), 美国
- **License**: proprietary 硬件; VEXcode 编辑器 free
- **Maturity signals**: 1999年成立; VRC (VEX Robotics Competition) 全球50,000+团队参赛; VEX IQ Challenge 和 VRC 每年全球锦标赛; 与 FIRST Robotics 并列全球最大学生机器人竞赛体系。evidence: [T02-S014]
- **典型使用场景**: 10-18岁竞赛机器人(VRC/VIQRC); C++ 或 Python 实体机器人编程; 中学STEM精英项目; 国际学校竞赛备赛; 工程设计+团队合作训练。
- **不适合/替代方案**: 套件价格高($300-2000+); 需要教练/导师指导; 非竞赛方向性价比低。替代: LEGO SPIKE(更易上手,更贵) / mBot(更便宜但竞赛认可度低)。evidence: [T02-S014]
- **生产案例**: VEX World Championship 每年超2万团队; 中国多个省份有官方VRC地区赛; 美国中学STEM选修课标配竞赛平台之一。
- **近期变化**: VEX V5 AI Vision Sensor 2024新品; VEXcode AI 编程模块引入机器视觉; VIQRC 2024-25赛季主题更新。evidence: [T02-S014]
- **来源**: [T02-S014] vexrobotics.com 官方; [T02-S015] firstinspires.org (FIRST对比参照); onoff.gr Educational Robots 2026
- **可信度**: 高
- **Decay risk**: 低 — 竞赛体系稳定，全球大规模运营

---

## 选型决策树

```
[用户场景] → 推荐工具栈
│
├── Branch 1: 编程启蒙 (6-9岁)
│   ├── 有硬件预算? → micro:bit + Scratch + Code.org Hour of Code
│   ├── 纯软件/在线? → Scratch + Code.org + CodeMonkey
│   └── 中国本地化? → 编程猫 + Scratch中文版
│
├── Branch 2: 系统编程学习 (10-14岁)
│   ├── Python路线 → Replit/Trinket + Khan Academy + Python.org
│   ├── 竞赛苗子? → C++ + 洛谷 → Branch 3
│   └── 创意方向? → Processing/p5.js / Roblox Studio
│
├── Branch 3: 信奥赛训练 (12-18岁)
│   ├── 中国赛事 → C++ + 洛谷 + NOI题库 (noi.cn)
│   ├── 国际赛事 → C++ + Codeforces + USACO
│   └── 刷题+学习 → 洛谷(中文) / Codeforces(国际) 二选一+配合
│
├── Branch 4: AI/ML 兴趣探索
│   ├── 零编程基础 → Teachable Machine (Google)
│   ├── 有Scratch基础 → Scratch + ML扩展 (MIT)
│   └── 会Python → ml5.js / scikit-learn入门
│
├── Branch 5: 机器人/创客
│   ├── 预算<300元 → micro:bit + MakeCode
│   ├── 预算300-2000元 → Makeblock mBot2 / Arduino Uno套件
│   ├── 预算>2000元(竞赛) → LEGO SPIKE Prime / VEX Robotics
│   └── 高级创客 → Raspberry Pi + MicroPython + ESP32
│
└── Branch 6: 培训机构选型
    ├── 直播教学 → ClassIn (互动黑板) + Zoom/腾讯课堂
    ├── 课程管理 → 校管家 / 小鹅通
    ├── 编程教学平台 → Code.org(国际) / 编程猫(中国)
    └── 竞赛培训 → 洛谷 + Codeforces + 自建OJ
```

---

## 避坑清单

1. **Scratch版本混乱**: Scratch 2.0(Flash)已停用，务必用Scratch 3.0(HTML5)；部分老课程仍用2.0截图，误导学生。
2. **Python版本**: 始终用Python 3.x；Python 2已EOL(2020)，但部分老教材仍用2.7语法。
3. **LEGO Mindstorms EV3停产**: EV3已停产(2022宣布)，新采购优先LEGO SPIKE Prime；EV3教程仍大量流通但硬件难买。
4. **Replit免费层收缩**: 2023年Replit大幅削减免费功能，大班教学需评估Team for Edu订阅成本。
5. **洛谷账号实名限制**: 2022+洛谷对未成年账号加强管理，机构需统一注册。
6. **竞赛语言陷阱**: NOI/IOI仅支持C/C++/Pascal(Pascal 2022后逐步退出)；不要用Java/Python备赛主力。
7. **Teachable Machine数据隐私**: 上传的训练图片默认上传Google服务器，K12环境需确认数据合规。
8. **Roblox Studio年龄限制**: Roblox平台有13岁+内容分级，学校使用需配置家长控制。
9. **micro:bit版本差异**: micro:bit V1 vs V2硬件能力差距显著(V2有麦克风/扬声器)，采购时确认版本。
10. **编程猫国际化弱**: 编程猫主要服务中国大陆市场，境外服务器/账号体验差，国际项目不推荐。
11. **GitHub Copilot for Education**: 需edu邮箱验证，个人学生免费但机构批量部署有审核周期。
12. **ClassIn收费模式**: ClassIn 2024重新调整定价，免费版功能受限，大机构需提前测试。

---

## Phase 2 提炼提示

**反复出现≥3 source的「工具选型原则」** (候选 playbook):
- 年龄分段选工具: block-based(6-10) → text-based(10-14) → competitive(12-18)
- 硬件预算决定机器人路线: 低预算micro:bit → 中预算mBot → 高预算LEGO/VEX
- 竞赛赛道与兴趣赛道工具链不相通，需早期分流

**显著的工具流派分裂** (候选智识谱系):
- 中国本土化 vs 国际化工具链 (编程猫/洛谷 vs Scratch/Codeforces)
- 课程平台一体化 vs 工具自由组合 (Code.org vs Replit+自定课程)
- 游戏化学习 vs 正式CS教育 (Tynker/Roblox vs 洛谷/USACO)

**新兴工具信号**:
- AI辅助编程: Copilot for Education + Khanmigo 2024-2025快速渗透
- LLM-based tutoring在K12机构POC阶段
- Micro:bit V2生态扩展(扬声器/麦克风新课程线)

**冷僻/信号薄弱**:
- Sonic Pi(音乐编程，英国校园主流，中国极少)
- Snap!(Berkeley CSP课程绑定，独立使用少)
- ml5.js(信号很薄，主要在高中AP CS项目)
- MIT App Inventor(移动端兴趣高但留存率低)
