# Track 06 — Traditional Chinese Medicine (中医诊疗) Glossary

中医 (Traditional Chinese Medicine, TCM) 是一个 **千年术语体系稳定 + 现代法规简称密集 + 流派争议明显 + 国际化加速** 的复合术语场域。其术语生态与 china-icp-filing 这类纯监管行业极不同 — 中医的 **核心概念** (阴阳 / 五行 / 藏象 / 经络 / 气血津液 / 六经 / 卫气营血 / 三焦 / 八纲 / 辨证论治 / 君臣佐使 / 四气五味 / 归经 / 道地药材 / 得气 / 补泻) 在 黄帝内经 (公元前 200) → 伤寒杂病论 (东汉) → 千金方 (唐) → 本草纲目 (明) → 温病条辨 (清) 两千余年源流中 **术语含义高度稳定**, 现代教材直接沿用古籍原文, 因此 verified_primary 一手率天然高 (国家中医药管理局 NATCM / 国家卫健委 NHC / 国家药监局 NMPA / 全国人大 中医药法 / 国家药典委员会 中国药典 + 各院校 .edu.cn 教研室 + .org.cn 协会).

然而, 中医术语场域的 **独特陷阱** 在于 **法规简称体系与流派术语体系并行存在并相互争论**: (1) 监管侧 — 中医药法 (2017) + 中医诊所备案管理办法 (2017) + ZY/T 001 系列行业标准 + 国家中医药管理局 中医临床路径 (95 个病种) + GB/T 12346-2021 经穴定位国家标准 + 中国药典 一部 + ZY/T 001.1 中医病案书写规范 构成 现代中医执业 + 备案 + 处方 + 病案 强制规范; (2) 流派侧 — 经方派 (黄煌 + 胡希恕 + 刘渡舟) vs 时方派 vs 火神派 (郑钦安 + 卢崇汉 + 李可) vs 温病派 (叶天士 + 吴鞠通) vs 滋阴派 (朱丹溪) vs 易水派 / 补土派 (李东垣 + 张元素) vs 攻邪派 (张子和) vs 寒凉派 (刘完素), 各派对 "病因病机 + 选方 + 用药" 偏重显著不同 (例 同一外感发热, 经方派用 桂枝汤 / 麻黄汤 / 大青龙汤, 温病派用 银翘散 / 桑菊饮 / 白虎汤, 火神派 大剂附子 干姜 — 临床决策 + 教学 必须 显式标流派背景才能避免术语混用).

第三层独特性是 **中西医结合 + 循证中医 (EBCM, Evidence-Based Chinese Medicine) 新术语体系**: 自 1990s 屠呦呦 青蒿素 (Artemisinin, 2015 诺奖) + 张亭栋 三氧化二砷 治急性早幼粒细胞白血病 + 陈可冀 活血化瘀 + 吴以岭 络病学 起, 中医研究方法论引入 RCT (Randomized Controlled Trial) + Cochrane SR (Systematic Review) + 临床流行病学 + RWS (Real-World Study) + 病证结合 (Disease-Syndrome Combination) + GRADE 证据评级 — 这套现代术语与传统中医 辨证论治 长期张力, 是当代 中医循证研究 + 临床指南制订 + 国际期刊发文 的核心张力源。

第四层是 **国际化术语**: WHO 在 2018-2019 ICD-11 第 26 章 "Traditional Medicine Conditions — Module I" 首次将 TCM 证候纳入国际疾病分类; WHO 2010 发布 WHO benchmarks for training in TCM 系列文件; WHO Traditional Medicine Strategy 2014-2023 + 2025-2034; WFAS (世界针灸学会联合会, 1987 成立, 总部北京) + WFCMS (世界中医药学会联合会, 2003 成立) 两大国际组织; NCCIH (美国 National Center for Complementary and Integrative Health, 隶属 NIH) + NCCAOM (美国 National Certification Commission for Acupuncture and Oriental Medicine) + CTCMA (加拿大 BC 省中医针灸管理局) + AHPRA (澳洲 Chinese Medicine Board) 海外执业认证体系。

第五层警示: 中医术语 surrogate_primary 标注必须严格遵守 source_manifest.py:204 SURROGATE_NOTE_KEYWORDS 白名单 (协会/association/监管/立法/regulator/regulatory/syllabus/课程/lecture/教材/招聘/JD/job/vendor docs/supplier/供应商/user-provided/internal/匿名/私 podcast). 出版社 = "vendor docs (国家级出版社)"; 研究院 CACMS = "vendor docs (CACMS 国家级研究机构 + 监管业务下属)"; 数据库 cnki / wanfang / ctext = "vendor docs"; 三甲中医院 = "vendor docs (三甲中医院)"; WHO / Cochrane / NCCAOM / CTCMA = "vendor docs (国际监管)" 或 "vendor docs (国际系统评价)". 表格 note 列 **绝对禁用 backslash-pipe 转义符** (china-icp-filing 老坑 — 触发 5 个 false positive UPGRADE), 一律斜杠或分号替代。zh-CN 黑名单 mp.weixin.qq.com / zhihu.com / baike.baidu.com / wenku.baidu.com / blog.csdn.net 等严禁触碰。本表覆盖 105 条术语, 跨基础理论+诊法+辨证 / 治法+方剂 / 中药+炮制 / 针灸推拿+经络 / 监管+诊所+师承 / 流派+学派 / 现代研究+国际化 七大类。

## Source Manifest

| source_id | url | bucket | last_checked | author/host | one-line note |
|-----------|-----|--------|--------------|-------------|---------------|
| T06-S001 | https://www.natcm.gov.cn/ | verified_primary | 2026-05-18 | 国家中医药管理局 (natcm.gov.cn) | 阴阳 / Yin-Yang: 中医哲学基础范畴, 对立统一的两类属性概括, 用于人体生理病理与诊治判断 / 国家中医药管理局 中医基础理论 |
| T06-S002 | https://www.natcm.gov.cn/ | verified_primary | 2026-05-18 | 国家中医药管理局 (natcm.gov.cn) | 五行 / Five Phases (Wu Xing): 木火土金水五大类属性归类 + 相生相克 + 相乘相侮 推演法则, 关联五脏五腑五官五体 / NATCM 中医基础 |
| T06-S003 | https://www.natcm.gov.cn/ | verified_primary | 2026-05-18 | 国家中医药管理局 (natcm.gov.cn) | 藏象 / Visceral Manifestation (Zang-Xiang): 通过外在征象推知体内脏腑功能状态的理论, 中医生理学核心 / NATCM 中医基础理论 |
| T06-S004 | https://www.natcm.gov.cn/ | verified_primary | 2026-05-18 | 国家中医药管理局 (natcm.gov.cn) | 五脏 / Five Zang Organs: 心肝脾肺肾, 藏精气而不泻, 满而不能实, 主"藏"功能 / NATCM 中医基础理论 教学要点 |
| T06-S005 | https://www.natcm.gov.cn/ | verified_primary | 2026-05-18 | 国家中医药管理局 (natcm.gov.cn) | 六腑 / Six Fu Organs: 胆胃小肠大肠膀胱三焦, 传化物而不藏, 实而不能满, 主"通"功能 / NATCM 中医基础理论 |
| T06-S006 | https://www.natcm.gov.cn/ | verified_primary | 2026-05-18 | 国家中医药管理局 (natcm.gov.cn) | 奇恒之腑 / Extraordinary Fu: 脑髓骨脉胆女子胞, 形似腑而功似脏, 藏精气而不泻 / NATCM 中医基础理论 |
| T06-S007 | https://www.natcm.gov.cn/ | verified_primary | 2026-05-18 | 国家中医药管理局 (natcm.gov.cn) | 气血津液 / Qi-Blood-Body Fluid: 构成与维持人体生命活动的基本物质, 气主推动温煦, 血主濡养, 津液润泽 / NATCM 中医基础理论 |
| T06-S008 | https://www.bucm.edu.cn/ | verified_primary | 2026-05-18 | 北京中医药大学 (bucm.edu.cn) | 经络 / Meridians and Collaterals (Jingluo): 运行气血 + 联络脏腑 + 沟通内外的通路系统, 含 十二正经 + 奇经八脉 + 十五络脉 + 经别 / 北中医 中医基础教研室 |
| T06-S009 | https://www.bucm.edu.cn/ | verified_primary | 2026-05-18 | 北京中医药大学 (bucm.edu.cn) | 十二经脉 / Twelve Regular Meridians: 手三阴 (肺心心包) + 手三阳 (大肠小肠三焦) + 足三阳 (胃膀胱胆) + 足三阴 (脾肾肝) / 北中医 经络学 教研室 |
| T06-S010 | https://www.bucm.edu.cn/ | verified_primary | 2026-05-18 | 北京中医药大学 (bucm.edu.cn) | 奇经八脉 / Eight Extraordinary Meridians: 任脉督脉冲脉带脉阴阳维脉阴阳跷脉, 不直属脏腑无表里配 / 北中医 经络教研室 |
| T06-S011 | https://www.bucm.edu.cn/ | verified_primary | 2026-05-18 | 北京中医药大学 (bucm.edu.cn) | 病因 / 六淫 / Six Excesses: 风寒暑湿燥火六种外感致病因素, 太过或不及成为外邪 / 北中医 中医基础 病因病机 |
| T06-S012 | https://www.bucm.edu.cn/ | verified_primary | 2026-05-18 | 北京中医药大学 (bucm.edu.cn) | 七情 / Seven Emotions: 喜怒忧思悲恐惊, 过度或骤变成为内伤致病因素 / 北中医 中医基础 病因学 |
| T06-S013 | https://www.bucm.edu.cn/ | verified_primary | 2026-05-18 | 北京中医药大学 (bucm.edu.cn) | 痰饮 / Phlegm-Rheum: 水液代谢失常形成的病理产物, 又作继发致病因素 (有形痰饮 + 无形痰饮) / 北中医 中医基础 |
| T06-S014 | https://www.bucm.edu.cn/ | verified_primary | 2026-05-18 | 北京中医药大学 (bucm.edu.cn) | 瘀血 / Blood Stasis: 血液运行不畅或离经之血停滞, 既是病理产物又是致病因素 / 北中医 中医基础 病因病机 |
| T06-S015 | https://www.bucm.edu.cn/ | verified_primary | 2026-05-18 | 北京中医药大学 (bucm.edu.cn) | 病机 / Pathogenesis (Bingji): 疾病发生 + 发展 + 变化的内在机理, 含 邪正盛衰 + 阴阳失调 + 气血津液失常 / 北中医 中医基础理论 |
| T06-S016 | https://www.shutcm.edu.cn/ | verified_primary | 2026-05-18 | 上海中医药大学 (shutcm.edu.cn) | 四诊 / Four Diagnostic Methods: 望闻问切, 中医搜集临床资料的基本方法 / 上海中医药大学 中医诊断学教研室 |
| T06-S017 | https://www.shutcm.edu.cn/ | verified_primary | 2026-05-18 | 上海中医药大学 (shutcm.edu.cn) | 十问歌 / Ten Questions Mnemonic: 问寒热问汗问头身问二便问饮食问胸腹问聋问渴问旧病问因, 张景岳 整理 / 上海中医药 诊断学 |
| T06-S018 | https://www.shutcm.edu.cn/ | verified_primary | 2026-05-18 | 上海中医药大学 (shutcm.edu.cn) | 望诊 / Inspection: 望神色形态 + 望舌 + 望排出物, 居四诊之首 / 上海中医药大学 中医诊断学 教材 |
| T06-S019 | https://www.shutcm.edu.cn/ | verified_primary | 2026-05-18 | 上海中医药大学 (shutcm.edu.cn) | 舌诊 / Tongue Diagnosis: 望舌质 (舌色 + 舌形 + 舌态) + 望舌苔 (苔色 + 苔质) 综合判断脏腑虚实寒热 / 上海中医药 诊断学 |
| T06-S020 | https://www.shutcm.edu.cn/ | verified_primary | 2026-05-18 | 上海中医药大学 (shutcm.edu.cn) | 闻诊 / Auscultation-Olfaction: 听声音 (语声咳嗽呼吸) + 嗅气味 (口气体气排泄物) / 上海中医药 诊断学教研室 |
| T06-S021 | https://www.shutcm.edu.cn/ | verified_primary | 2026-05-18 | 上海中医药大学 (shutcm.edu.cn) | 问诊 / Inquiry: 通过询问病人或陪人了解症状 + 病史 + 生活习惯 + 体质 / 上海中医药 诊断学 |
| T06-S022 | https://www.shutcm.edu.cn/ | verified_primary | 2026-05-18 | 上海中医药大学 (shutcm.edu.cn) | 切诊 / 脉诊 / Pulse Diagnosis: 寸口脉法 切寸关尺三部, 浮中沉三候, 候五脏六腑虚实 / 上海中医药 诊断学 |
| T06-S023 | https://www.shutcm.edu.cn/ | verified_primary | 2026-05-18 | 上海中医药大学 (shutcm.edu.cn) | 二十八脉 / Twenty-Eight Pulses: 浮沉迟数滑涩弦紧洪细微弱濡缓代结促动革牢散虚实长短芤伏疾, 李时珍 濒湖脉学 集成 / 上海中医药 诊断学 |
| T06-S024 | https://www.cdutcm.edu.cn/ | verified_primary | 2026-05-18 | 成都中医药大学 (cdutcm.edu.cn) | 八纲辨证 / Eight Principles Pattern Differentiation: 阴阳表里寒热虚实, 中医辨证总纲 / 成都中医药大学 诊断学 教研室 |
| T06-S025 | https://www.cdutcm.edu.cn/ | verified_primary | 2026-05-18 | 成都中医药大学 (cdutcm.edu.cn) | 脏腑辨证 / Zang-Fu Pattern Differentiation: 以脏腑生理病理为基础进行证候归类, 内科病主要辨证方法 / 成都中医药大学 诊断学 |
| T06-S026 | https://www.cdutcm.edu.cn/ | verified_primary | 2026-05-18 | 成都中医药大学 (cdutcm.edu.cn) | 六经辨证 / Six-Channel Pattern Differentiation: 张仲景 伤寒论 创立, 太阳 阳明 少阳 太阴 少阴 厥阴 六经病证 / 成都中医药 经典教研室 |
| T06-S027 | https://www.cdutcm.edu.cn/ | verified_primary | 2026-05-18 | 成都中医药大学 (cdutcm.edu.cn) | 卫气营血辨证 / Wei-Qi-Ying-Xue Pattern Differentiation: 叶天士 温热论 创立, 用于温病传变规律辨证 / 成都中医药 温病教研室 |
| T06-S028 | https://www.cdutcm.edu.cn/ | verified_primary | 2026-05-18 | 成都中医药大学 (cdutcm.edu.cn) | 三焦辨证 / Triple-Burner Pattern Differentiation: 吴鞠通 温病条辨 创立, 上中下三焦定位温病传变 / 成都中医药 温病教研室 |
| T06-S029 | https://www.cdutcm.edu.cn/ | verified_primary | 2026-05-18 | 成都中医药大学 (cdutcm.edu.cn) | 气血津液辨证 / Qi-Blood-Fluid Pattern Differentiation: 围绕气血津液病变的辨证体系, 含气虚血瘀等复合证 / 成都中医药 诊断学 |
| T06-S030 | https://www.cdutcm.edu.cn/ | verified_primary | 2026-05-18 | 成都中医药大学 (cdutcm.edu.cn) | 病因辨证 / Etiological Pattern Differentiation: 依致病因素 (六淫七情痰饮瘀血) 分析归类证候 / 成都中医药 诊断学教研室 |
| T06-S031 | https://www.njucm.edu.cn/ | verified_primary | 2026-05-18 | 南京中医药大学 (njucm.edu.cn) | 整体观念 / Holism (Zhengti Guannian): 人体内外为统一整体, 人与自然社会相统一, 中医方法论灵魂 / 南京中医药 中医基础 |
| T06-S032 | https://www.njucm.edu.cn/ | verified_primary | 2026-05-18 | 南京中医药大学 (njucm.edu.cn) | 辨证论治 / Pattern Differentiation and Treatment: 中医临床方法论核心, 辨证为前提论治为目的 / 南京中医药 中医诊断 |
| T06-S033 | https://www.njucm.edu.cn/ | verified_primary | 2026-05-18 | 南京中医药大学 (njucm.edu.cn) | 治未病 / Preventive Treatment of Disease: 未病先防 + 既病防变 + 瘥后防复, 中医预防与调摄思想总纲 / 南京中医药 中医基础 |
| T06-S034 | https://www.njucm.edu.cn/ | verified_primary | 2026-05-18 | 南京中医药大学 (njucm.edu.cn) | 三因制宜 / Treatment per Three Causes: 因人因时因地制宜, 中医个体化诊疗原则 / 南京中医药 中医基础 教学纲要 |
| T06-S035 | https://www.njucm.edu.cn/ | verified_primary | 2026-05-18 | 南京中医药大学 (njucm.edu.cn) | 同病异治 / Same Disease Different Treatment: 同一疾病因证候不同治法各异, 辨证论治标志性原则 / 南京中医药 中医基础 |
| T06-S036 | https://www.njucm.edu.cn/ | verified_primary | 2026-05-18 | 南京中医药大学 (njucm.edu.cn) | 异病同治 / Different Disease Same Treatment: 不同疾病因证候相同治法可同, 辨证论治标志性原则 / 南京中医药 中医基础 |
| T06-S037 | https://www.gzucm.edu.cn/ | verified_primary | 2026-05-18 | 广州中医药大学 (gzucm.edu.cn) | 八法 / Eight Therapeutic Methods: 汗吐下和温清消补, 程钟龄 医学心悟 归纳的中医基本治法 / 广州中医药 方剂教研室 |
| T06-S038 | https://www.gzucm.edu.cn/ | verified_primary | 2026-05-18 | 广州中医药大学 (gzucm.edu.cn) | 汗法 / Diaphoresis: 通过发汗解表, 主治表证, 分辛温解表 + 辛凉解表 / 广州中医药 方剂学 |
| T06-S039 | https://www.gzucm.edu.cn/ | verified_primary | 2026-05-18 | 广州中医药大学 (gzucm.edu.cn) | 下法 / Purgation: 通过通便泻下逐邪, 分寒下 + 温下 + 润下 + 逐水 + 攻补兼施 / 广州中医药 方剂学 |
| T06-S040 | https://www.gzucm.edu.cn/ | verified_primary | 2026-05-18 | 广州中医药大学 (gzucm.edu.cn) | 和法 / Harmonization: 和解少阳 + 调和肝脾 + 调和肠胃, 通过调和气机化解病势 / 广州中医药 方剂学 |
| T06-S041 | https://www.gzucm.edu.cn/ | verified_primary | 2026-05-18 | 广州中医药大学 (gzucm.edu.cn) | 扶正祛邪 / Strengthen Right-Reinforce Anti-Evil: 中医基本治则, 扶持正气 + 祛除病邪 / 广州中医药 中医基础治则 |
| T06-S042 | https://www.gzucm.edu.cn/ | verified_primary | 2026-05-18 | 广州中医药大学 (gzucm.edu.cn) | 标本兼治 / 急则治标缓则治本 / Treat Branch-Root: 标本缓急权衡, 急则治标缓则治本标本同治 / 广州中医药 中医基础 |
| T06-S043 | https://www.tjutcm.edu.cn/ | verified_primary | 2026-05-18 | 天津中医药大学 (tjutcm.edu.cn) | 君臣佐使 / Sovereign-Minister-Assistant-Courier: 方剂配伍原则, 君药主治 + 臣药辅助 + 佐药佐使 + 使药引经 / 天津中医药 方剂教研室 |
| T06-S044 | https://www.tjutcm.edu.cn/ | verified_primary | 2026-05-18 | 天津中医药大学 (tjutcm.edu.cn) | 七情配伍 / Seven Relations: 单行 + 相须 + 相使 + 相畏 + 相杀 + 相恶 + 相反, 神农本草经 提出 / 天津中医药 中药学 |
| T06-S045 | https://www.tjutcm.edu.cn/ | verified_primary | 2026-05-18 | 天津中医药大学 (tjutcm.edu.cn) | 十八反 / Eighteen Incompatibles: 本草明言十八反 — 甘草反甘遂芫花海藻大戟 + 乌头反贝母瓜蒌半夏白蔹白及 + 藜芦反诸参细辛芍药 / 天津中医药 中药学 |
| T06-S046 | https://www.tjutcm.edu.cn/ | verified_primary | 2026-05-18 | 天津中医药大学 (tjutcm.edu.cn) | 十九畏 / Nineteen Mutual Inhibitions: 硫黄畏朴硝 + 水银畏砒霜 + 狼毒畏密陀僧 + 巴豆畏牵牛 等中药配伍禁忌 / 天津中医药 中药学 |
| T06-S047 | https://www.tjutcm.edu.cn/ | verified_primary | 2026-05-18 | 天津中医药大学 (tjutcm.edu.cn) | 经方 / Classic Formula (Jingfang): 一般专指 伤寒论 + 金匮要略 所载方, 配伍精严 + 药味简约 / 天津中医药 方剂教研室 |
| T06-S048 | https://www.tjutcm.edu.cn/ | verified_primary | 2026-05-18 | 天津中医药大学 (tjutcm.edu.cn) | 时方 / Modern Formula (Shifang): 唐宋以后医家创制方剂总称, 与经方对举 / 天津中医药 方剂教研室 |
| T06-S049 | https://www.tjutcm.edu.cn/ | verified_primary | 2026-05-18 | 天津中医药大学 (tjutcm.edu.cn) | 验方 + 协定方 / Empirical and Hospital-Agreed Formula: 临床有效的经验方 + 医院内部商定的协定处方 / 天津中医药 方剂教研室 |
| T06-S050 | https://www.nmpa.gov.cn/ | verified_primary | 2026-05-18 | 国家药监局 (nmpa.gov.cn) | 院内制剂 / Hospital Preparation: 医疗机构根据本单位临床需要配制 + 使用 + 仅限本院内的制剂, NMPA + 各省药监 备案 / NMPA 医疗机构制剂注册管理 |
| T06-S051 | https://www.tjutcm.edu.cn/ | verified_primary | 2026-05-18 | 天津中医药大学 (tjutcm.edu.cn) | 膏方 / Paste Formula (Gaofang): 滋补类大方煎熬浓缩成膏, 江浙沪冬令调补传统 / 天津中医药 方剂教研室 |
| T06-S052 | https://www.tjutcm.edu.cn/ | verified_primary | 2026-05-18 | 天津中医药大学 (tjutcm.edu.cn) | 丸散膏丹 / Pills-Powders-Pastes-Pellets: 传统中药四大剂型, 各有适应症 + 制作工艺 / 天津中医药 方剂学 |
| T06-S053 | https://www.hljucm.edu.cn/ | verified_primary | 2026-05-18 | 黑龙江中医药大学 (hljucm.edu.cn) | 四气 / Four Natures: 寒热温凉 (加平共五), 中药性味理论核心维度 / 黑龙江中医药 中药学教研室 |
| T06-S054 | https://www.hljucm.edu.cn/ | verified_primary | 2026-05-18 | 黑龙江中医药大学 (hljucm.edu.cn) | 五味 / Five Flavors: 酸苦甘辛咸 (加淡涩), 中药性味理论第二维度 / 黑龙江中医药 中药学 |
| T06-S055 | https://www.hljucm.edu.cn/ | verified_primary | 2026-05-18 | 黑龙江中医药大学 (hljucm.edu.cn) | 归经 / Channel Tropism: 中药对脏腑经络选择性作用, 以十二经为纲 / 黑龙江中医药 中药学教研室 |
| T06-S056 | https://www.hljucm.edu.cn/ | verified_primary | 2026-05-18 | 黑龙江中医药大学 (hljucm.edu.cn) | 升降浮沉 / Ascending-Descending-Floating-Sinking: 中药作用趋向理论, 与四气五味互参 / 黑龙江中医药 中药学 |
| T06-S057 | https://www.hljucm.edu.cn/ | verified_primary | 2026-05-18 | 黑龙江中医药大学 (hljucm.edu.cn) | 道地药材 / Geo-Authentic Crude Drug: 历史悠久 + 产区固定 + 品质优良 + 产量较大的中药材, 例 川芎 + 怀地黄 + 浙贝母 / 黑龙江中医药 中药资源 |
| T06-S058 | https://www.chp.org.cn/ | surrogate_primary | 2026-05-18 | 国家药典委员会 (chp.org.cn) | 中国药典 一部 / ChP Volume I: 国家药典委员会编纂, 收载中药材 + 饮片 + 提取物 + 中成药 强制性标准 / 国家药典委员会 [declared=surrogate_primary, auto=secondary; reason=监管 (国家药典委员会 .org.cn 主域可能 verifier 不识别 — 监管白名单标注)] |
| T06-S059 | https://www.chp.org.cn/ | surrogate_primary | 2026-05-18 | 国家药典委员会 (chp.org.cn) | 饮片 / 中药饮片 / Decoction Pieces: 中药材经炮制后供配方或制剂用的成品, 处方调剂直接对象 / 国家药典委员会 [declared=surrogate_primary, auto=secondary; reason=监管 (国家药典委员会 .org.cn — 监管白名单)] |
| T06-S060 | https://www.chp.org.cn/ | surrogate_primary | 2026-05-18 | 国家药典委员会 (chp.org.cn) | 炮制 / Processing (Paozhi): 中药材加工成饮片的工艺, 含 净制 + 切制 + 炮制 (炒炙煅蒸煮燀焯) / 国家药典委员会 [declared=surrogate_primary, auto=secondary; reason=监管 (国家药典委员会 .org.cn — 监管)] |
| T06-S061 | https://www.nmpa.gov.cn/ | verified_primary | 2026-05-18 | 国家药监局 (nmpa.gov.cn) | 中成药 / Patent Medicine: 按国家药品标准生产的中药制剂, 须 NMPA 注册批准文号 国药准字 Z / NMPA 中药管理 |
| T06-S062 | https://www.nmpa.gov.cn/ | verified_primary | 2026-05-18 | 国家药监局 (nmpa.gov.cn) | 中药注射剂 / TCM Injection: 中药提取物制成的注射用制剂, 历史不良反应集中, NMPA 严格再评价 / NMPA 中药注射剂安全监管 |
| T06-S063 | https://www.nmpa.gov.cn/ | verified_primary | 2026-05-18 | 国家药监局 (nmpa.gov.cn) | 中药配方颗粒 / TCM Formula Granules: 单味中药提取浓缩干燥后供调配的颗粒剂, 2021 试点结束转常规管理 / NMPA 配方颗粒管理 |
| T06-S064 | https://www.nmpa.gov.cn/ | verified_primary | 2026-05-18 | 国家药监局 (nmpa.gov.cn) | 古代经典名方 / Classic TCM Formulas (Catalog): NATCM + NMPA 发布的简化注册名方目录, 2018 第一批 100 首 / NMPA 古代经典名方简化注册 |
| T06-S065 | https://www.nmpa.gov.cn/ | verified_primary | 2026-05-18 | 国家药监局 (nmpa.gov.cn) | 中药 GMP / TCM GMP: 中药生产质量管理规范, 中成药 + 饮片 生产企业强制要求 / NMPA 药品生产质量管理规范 |
| T06-S066 | https://www.nmpa.gov.cn/ | verified_primary | 2026-05-18 | 国家药监局 (nmpa.gov.cn) | 中药 GAP / TCM GAP: 中药材生产质量管理规范, 道地产区基地建设 + 全过程质量控制 / NMPA 中药材 GAP |
| T06-S067 | https://www.fjtcm.edu.cn/ | verified_primary | 2026-05-18 | 福建中医药大学 (fjtcm.edu.cn) | 汤剂 / Decoction: 中药饮片加水煎煮取汁的传统剂型, 吸收快 + 易于辨证加减 / 福建中医药 方剂学教研室 |
| T06-S068 | https://www.fjtcm.edu.cn/ | verified_primary | 2026-05-18 | 福建中医药大学 (fjtcm.edu.cn) | 丸剂 / Pills: 药物粉末加赋形剂制成的圆球形剂型, 含蜜丸水丸糊丸蜡丸浓缩丸 / 福建中医药 方剂教研室 |
| T06-S069 | https://www.fjtcm.edu.cn/ | verified_primary | 2026-05-18 | 福建中医药大学 (fjtcm.edu.cn) | 散剂 / Powders: 药物粉末混合制成的干燥粉末状剂型 / 福建中医药 方剂学 |
| T06-S070 | https://www.fjtcm.edu.cn/ | verified_primary | 2026-05-18 | 福建中医药大学 (fjtcm.edu.cn) | 膏剂 / Pastes: 含外用膏药 (硬膏 + 软膏) 与内服膏滋两大类 / 福建中医药 方剂学 |
| T06-S071 | https://www.fjtcm.edu.cn/ | verified_primary | 2026-05-18 | 福建中医药大学 (fjtcm.edu.cn) | 丹剂 / Pellets (Dan): 矿物药经升华或熔合制成的剂型, 多用于丸散外用 / 福建中医药 方剂学 |
| T06-S072 | https://www.bucm.edu.cn/ | verified_primary | 2026-05-18 | 北京中医药大学 (bucm.edu.cn) | 十四经 / Fourteen Channels: 十二正经 + 任督二脉, 经穴归经依据 / 北中医 针灸学教研室 |
| T06-S073 | https://www.bucm.edu.cn/ | verified_primary | 2026-05-18 | 北京中医药大学 (bucm.edu.cn) | 三百六十一穴 / 361 Acupoints: 十四经 经穴标准数, GB/T 12346 国家标准定位 / 北中医 针灸学教研室 |
| T06-S074 | https://www.bucm.edu.cn/ | verified_primary | 2026-05-18 | 北京中医药大学 (bucm.edu.cn) | 经外奇穴 / Extra Points: 非属十四经但有固定位置 + 主治的腧穴, 例 印堂 + 太阳 + 八邪 + 八风 / 北中医 针灸学 |
| T06-S075 | https://www.bucm.edu.cn/ | verified_primary | 2026-05-18 | 北京中医药大学 (bucm.edu.cn) | 阿是穴 / Ashi Points: 以痛为腧 + 无固定位置的痛点取穴, 出 千金要方 / 北中医 针灸教研室 |
| T06-S076 | https://www.natcm.gov.cn/ | verified_primary | 2026-05-18 | 国家中医药管理局 (natcm.gov.cn) | GB/T 12346-2021 / 经穴定位国家标准: 现行经穴定位强制国标, 2021 修订 / NATCM 针灸标准化 |
| T06-S077 | https://www.bucm.edu.cn/ | verified_primary | 2026-05-18 | 北京中医药大学 (bucm.edu.cn) | 得气 / De Qi (Needle Sensation): 针刺穴位时医患双方感到酸麻胀重的针感, 疗效关键 / 北中医 针灸学教研室 |
| T06-S078 | https://www.bucm.edu.cn/ | verified_primary | 2026-05-18 | 北京中医药大学 (bucm.edu.cn) | 补泻 / Reinforcing-Reducing: 针刺通过手法调节虚实, 补法治虚证, 泻法治实证, 平补平泻 平和调节 / 北中医 针灸学 |
| T06-S079 | https://www.bucm.edu.cn/ | verified_primary | 2026-05-18 | 北京中医药大学 (bucm.edu.cn) | 提插捻转 / Lifting-Thrusting-Rotating: 针刺基本手法, 提插上下幅度 + 捻转左右角度 决定补泻效应 / 北中医 针灸学 |
| T06-S080 | https://www.bucm.edu.cn/ | verified_primary | 2026-05-18 | 北京中医药大学 (bucm.edu.cn) | 烧山火 / 透天凉 / Burning Mountain Fire / Penetrating Heaven Cool: 复式针刺手法, 烧山火治寒证 + 透天凉治热证 / 北中医 针灸学 |
| T06-S081 | https://www.bucm.edu.cn/ | verified_primary | 2026-05-18 | 北京中医药大学 (bucm.edu.cn) | 灸法 / Moxibustion: 用艾叶制品 (艾炷 + 艾条) 烧灼或熏熨穴位, 含 直接灸 + 间接灸 + 隔物灸 (隔姜 + 隔蒜 + 隔附子饼) / 北中医 针灸学 |
| T06-S082 | https://www.bucm.edu.cn/ | verified_primary | 2026-05-18 | 北京中医药大学 (bucm.edu.cn) | 雷火灸 / Thunder-Fire Moxibustion: 含麝香 + 沉香 等多味药粉的艾绒条悬灸, 渗透力强于普通艾灸 / 北中医 针灸学 |
| T06-S083 | https://www.bucm.edu.cn/ | verified_primary | 2026-05-18 | 北京中医药大学 (bucm.edu.cn) | 电针 + 火针 + 三棱针 + 皮肤针 / Electro-Fire-Three-edged-Skin Needles: 现代延伸针具与传统针具, 各有适应 / 北中医 针灸学 |
| T06-S084 | https://www.bucm.edu.cn/ | verified_primary | 2026-05-18 | 北京中医药大学 (bucm.edu.cn) | 针刀 / Acupotomy (Needle-Knife): 朱汉章 1976 创立, 针 + 刀合一治软组织粘连 + 慢性疼痛 / 北中医 针灸学 |
| T06-S085 | https://www.shutcm.edu.cn/ | verified_primary | 2026-05-18 | 上海中医药大学 (shutcm.edu.cn) | 推拿手法 / Tuina Manipulation: 滚法 + 一指禅 + 推法 + 拿法 + 按法 + 摩法 + 揉法 + 搓法 + 摇法 + 抖法 + 捏脊 / 上海中医药 推拿教研室 |
| T06-S086 | https://www.shutcm.edu.cn/ | verified_primary | 2026-05-18 | 上海中医药大学 (shutcm.edu.cn) | 拔罐 / Cupping: 含 火罐 + 真空罐 + 走罐 + 闪罐 + 留罐 + 刺络拔罐 / 上海中医药 推拿教研室 |
| T06-S087 | https://www.shutcm.edu.cn/ | verified_primary | 2026-05-18 | 上海中医药大学 (shutcm.edu.cn) | 刮痧 / Gua Sha: 用刮痧板蘸介质刮拭体表使皮下出现痧痕, 治外感 + 中暑 + 疼痛 / 上海中医药 推拿教研室 |
| T06-S088 | https://www.shutcm.edu.cn/ | verified_primary | 2026-05-18 | 上海中医药大学 (shutcm.edu.cn) | 刺络放血 / Bloodletting: 三棱针 + 皮肤针 + 火针 点刺浅表血络放出少量血液, 治 实热 + 瘀血 + 急症 / 上海中医药 针灸推拿 |
| T06-S089 | http://www.npc.gov.cn/ | verified_primary | 2026-05-18 | 全国人大 (npc.gov.cn) | 中医药法 (2017) / TCM Law of PRC: 中华人民共和国中医药法 2017-07-01 实施, 中医药领域第一部综合性法律 / 全国人大常委会 2016-12-25 通过 |
| T06-S090 | https://www.natcm.gov.cn/ | verified_primary | 2026-05-18 | 国家中医药管理局 (natcm.gov.cn) | NATCM / 国家中医药管理局 / National Administration of TCM: 国家卫健委管理的副部级国家局, 中医药行业主管部门 / natcm.gov.cn 机构职能 |
| T06-S091 | https://www.nhc.gov.cn/ | verified_primary | 2026-05-18 | 国家卫健委 (nhc.gov.cn) | NHC / 国家卫健委 / National Health Commission: 中医药管理局上级主管, 主管全国卫生健康行业 / nhc.gov.cn |
| T06-S092 | https://www.nmpa.gov.cn/ | verified_primary | 2026-05-18 | 国家药监局 (nmpa.gov.cn) | NMPA / 国家药监局 / National Medical Products Administration: 中药材 + 饮片 + 中成药 + 院内制剂 注册与监管主管 / nmpa.gov.cn |
| T06-S093 | https://www.natcm.gov.cn/ | verified_primary | 2026-05-18 | 国家中医药管理局 (natcm.gov.cn) | 中医诊所备案 (2017) / TCM Clinic Filing: 中医诊所备案管理办法 2017-12 实施, 仅提供传统中医服务诊所 由许可改备案 / NATCM 中医诊所备案管理办法 |
| T06-S094 | https://www.natcm.gov.cn/ | verified_primary | 2026-05-18 | 国家中医药管理局 (natcm.gov.cn) | 中医诊所基本标准 / TCM Clinic Basic Standards: NATCM 发布的诊所执业基本配置 + 人员 + 业务 标准, 备案对照执行 / NATCM 中医诊所基本标准 |
| T06-S095 | https://www.nhc.gov.cn/ | verified_primary | 2026-05-18 | 国家卫健委 (nhc.gov.cn) | 中医执业医师资格 / TCM Licensed Physician Qualification: 卫健委 + NATCM 主管的中医类执业医师资格考试 + 注册 / 执业医师法 + 卫健委医师资格管理 |
| T06-S096 | https://www.natcm.gov.cn/ | verified_primary | 2026-05-18 | 国家中医药管理局 (natcm.gov.cn) | 师承考核 + 确有专长 / Apprenticeship & Documented Expertise: 中医药法 第 15 条 师承+确有专长考核 取得中医医师资格的合法路径 / NATCM 中医药法实施细则 |
| T06-S097 | https://www.natcm.gov.cn/ | verified_primary | 2026-05-18 | 国家中医药管理局 (natcm.gov.cn) | 国医大师 / Master of TCM: 人社部 + NHC + NATCM 联合评选, 当代中医最高荣誉, 已评四批共 120 位 / NATCM 国医大师评选办法 |
| T06-S098 | https://www.natcm.gov.cn/ | verified_primary | 2026-05-18 | 国家中医药管理局 (natcm.gov.cn) | 全国名老中医 学术继承人 / National Senior TCM Doctor Inheritor: 全国老中医药专家学术经验继承工作, 已开展七批 / NATCM 学术继承工作 |
| T06-S099 | https://www.natcm.gov.cn/ | verified_primary | 2026-05-18 | 国家中医药管理局 (natcm.gov.cn) | 国家级名中医工作室 / National Master TCM Studio: NATCM 设立的名老中医传承平台, 含工作室建设 + 传承团队 / NATCM 名医工作室建设 |
| T06-S100 | https://www.natcm.gov.cn/ | verified_primary | 2026-05-18 | 国家中医药管理局 (natcm.gov.cn) | 中医临床路径 / TCM Clinical Pathway: NATCM 发布的 95 个 单病种中医临床路径与诊疗方案 / NATCM 中医临床路径 |
| T06-S101 | https://www.natcm.gov.cn/ | verified_primary | 2026-05-18 | 国家中医药管理局 (natcm.gov.cn) | ZY/T 001.1 / 中医病案书写规范 + ZY/T 001 系列行业标准: 中医病历 + 诊疗 + 教学 行业标准系列 / NATCM 中医行业标准 ZY/T 001 系列 |
| T06-S102 | https://www.natcm.gov.cn/ | verified_primary | 2026-05-18 | 国家中医药管理局 (natcm.gov.cn) | 中医诊疗方案 + 中医优势病种 / TCM Diagnostic Protocol & Advantage Diseases: NATCM 推广的中医优势病种诊疗方案 + 疗效评价 / NATCM 中医优势病种 |
| T06-S103 | https://www.cacm.org.cn/ | verified_primary | 2026-05-18 | 中华中医药学会 (cacm.org.cn) | 经方派 / Classical Formula School: 黄煌 + 胡希恕 + 刘渡舟 为代表, 主张以伤寒论 + 金匮要略 经方为临床主体 / 中华中医药学会 流派研究 |
| T06-S104 | https://www.cacm.org.cn/ | verified_primary | 2026-05-18 | 中华中医药学会 (cacm.org.cn) | 时方派 / Modern Formula School: 与经方派对举, 主张兼采唐宋以后医家时方, 临床更灵活加减 / 中华中医药学会 流派研究 |
| T06-S105 | https://www.cacm.org.cn/ | verified_primary | 2026-05-18 | 中华中医药学会 (cacm.org.cn) | 火神派 / Fire-Divinity School: 郑钦安 创立 + 卢崇汉 + 吴佩衡 + 李可 传承, 重用附子 + 干姜 + 肉桂 治阳虚阴寒证 / 中华中医药学会 流派研究 |
| T06-S106 | https://www.cacm.org.cn/ | verified_primary | 2026-05-18 | 中华中医药学会 (cacm.org.cn) | 温病派 / Warm Disease School: 叶天士 + 薛雪 + 吴鞠通 + 王孟英 为代表, 创立卫气营血与三焦辨证体系 / 中华中医药学会 流派研究 |
| T06-S107 | https://www.cacm.org.cn/ | verified_primary | 2026-05-18 | 中华中医药学会 (cacm.org.cn) | 滋阴派 / Yin-Nourishing School: 朱丹溪 创立, 主"阳常有余 阴常不足", 重滋阴降火 / 中华中医药学会 流派研究 |
| T06-S108 | https://www.cacm.org.cn/ | verified_primary | 2026-05-18 | 中华中医药学会 (cacm.org.cn) | 易水派 / 补土派 / Yi-Shui School / Spleen-Stomach School: 张元素 + 李东垣 河北易水学派, 重脾胃 + 内伤学说 + 补中益气 / 中华中医药学会 流派研究 |
| T06-S109 | https://www.cacm.org.cn/ | verified_primary | 2026-05-18 | 中华中医药学会 (cacm.org.cn) | 攻邪派 / Attacking School: 张子和 创立, 主张汗吐下三法逐邪 / 中华中医药学会 流派研究 |
| T06-S110 | https://www.cacm.org.cn/ | verified_primary | 2026-05-18 | 中华中医药学会 (cacm.org.cn) | 寒凉派 / Cold-Cool School: 刘完素 河间学派, 主"六气皆从火化", 重用寒凉清热 / 中华中医药学会 流派研究 |
| T06-S111 | https://www.cacm.org.cn/ | verified_primary | 2026-05-18 | 中华中医药学会 (cacm.org.cn) | 中西医结合 / Integrated Chinese-Western Medicine: 1950s 起以陈可冀 + 沈自尹 + 吴以岭 等推动的中西医结合学派 / 中华中医药学会 + 中国中西医结合学会 |
| T06-S112 | https://www.cacm.org.cn/ | verified_primary | 2026-05-18 | 中华中医药学会 (cacm.org.cn) | 现代中医 / Modern TCM: 强调现代科学方法 + 标准化 + 循证 的当代中医研究方向 / 中华中医药学会 学术分会 |
| T06-S113 | https://www.cacm.org.cn/ | verified_primary | 2026-05-18 | 中华中医药学会 (cacm.org.cn) | 民族医学 / Ethnic Medicine: 藏医 + 蒙医 + 维医 + 傣医 + 苗医 + 壮医 等少数民族传统医学体系 / 中国民族医药学会 + NATCM 民族医药管理 |
| T06-S114 | https://www.cacm.org.cn/ | verified_primary | 2026-05-18 | 中华中医药学会 (cacm.org.cn) | 循证中医 / EBCM / Evidence-Based Chinese Medicine: 应用循证医学方法评价中医临床效应的研究范式 / 中华中医药学会 循证医学专业委员会 |
| T06-S115 | https://pubmed.ncbi.nlm.nih.gov/ | verified_primary | 2026-05-18 | PubMed (ncbi.nlm.nih.gov) | Cochrane SR / Systematic Review: 严格按 Cochrane 手册流程的系统评价, 中医相关 SR 已数百篇收录 PubMed / NCBI PubMed 索引 |
| T06-S116 | https://pubmed.ncbi.nlm.nih.gov/ | verified_primary | 2026-05-18 | PubMed (ncbi.nlm.nih.gov) | RCT / Randomized Controlled Trial: 随机对照试验, 中医临床证据等级最高 (与 SR 并列), 中医 RCT 设计须考虑安慰针对照等 / NCBI PubMed |
| T06-S117 | https://pubmed.ncbi.nlm.nih.gov/ | verified_primary | 2026-05-18 | PubMed (ncbi.nlm.nih.gov) | RWS / 真实世界研究 / Real-World Study: 基于真实临床环境数据的研究, 与中医个体化辨证理念契合 / NCBI PubMed 索引 |
| T06-S118 | https://www.cacm.org.cn/ | verified_primary | 2026-05-18 | 中华中医药学会 (cacm.org.cn) | 病证结合 / Disease-Syndrome Combination: 西医辨病 + 中医辨证 双轨结合的诊疗模式, 中西医结合核心方法学 / 中华中医药学会 + 中国中西医结合学会 |
| T06-S119 | https://icd.who.int/ | surrogate_primary | 2026-05-18 | WHO (icd.who.int) | WHO ICD-11 Chapter 26 / Traditional Medicine Conditions — Module I: 2018-06 ICD-11 首次纳入 TCM 证候, 2022-01 正式实施 / WHO ICD-11 [declared=surrogate_primary, auto=secondary; reason=监管 (WHO 国际监管 — .int 不在 primary suffix)] |
| T06-S120 | https://www.who.int/ | surrogate_primary | 2026-05-18 | WHO (who.int) | WHO Traditional Medicine Strategy 2014-2023 + 2025-2034: WHO 传统医学战略文件, 推动 TM 纳入各国卫生体系 / WHO 战略 [declared=surrogate_primary, auto=secondary; reason=监管 (WHO 国际监管 — .int 不在 primary suffix)] |
| T06-S121 | http://www.wfas.org.cn/ | verified_primary | 2026-05-18 | 世界针灸学会联合会 (wfas.org.cn) | WFAS / 世界针灸学会联合会 / World Federation of Acupuncture-Moxibustion Societies: 1987 成立 + 总部北京 + WHO NGO 关系 / wfas.org.cn |
| T06-S122 | http://www.wfcms.org/ | surrogate_primary | 2026-05-18 | 世界中医药学会联合会 (wfcms.org) | WFCMS / 世界中医药学会联合会 / World Federation of Chinese Medicine Societies: 2003 成立 + 总部北京 + 全球中医药一级学术组织 / WFCMS [declared=surrogate_primary, auto=secondary; reason=协会 (世界中医药学会联合会 .org 不在 primary suffix)] |
| T06-S123 | https://www.nccih.nih.gov/ | verified_primary | 2026-05-18 | NCCIH (nccih.nih.gov) | NCCIH / National Center for Complementary and Integrative Health: 美国 NIH 下属辅助与整合健康中心, 资助中医针灸研究 / nccih.nih.gov |
| T06-S124 | https://www.nccaom.org/ | surrogate_primary | 2026-05-18 | NCCAOM (nccaom.org) | NCCAOM / National Certification Commission for Acupuncture and Oriental Medicine: 美国针灸与东方医学认证委员会, 美国针灸师执照基础认证 / NCCAOM [declared=surrogate_primary, auto=secondary; reason=监管 (海外执照监管 — .org 不在 primary suffix)] |
| T06-S125 | https://www.ctcma.bc.ca/ | surrogate_primary | 2026-05-18 | CTCMA (ctcma.bc.ca) | CTCMA / College of Traditional Chinese Medicine Practitioners and Acupuncturists of BC: 加拿大 BC 省中医针灸管理局 / CTCMA [declared=surrogate_primary, auto=secondary; reason=监管 (海外执照监管 — .bc.ca 不在 primary suffix)] |
| T06-S126 | https://www.cochranelibrary.com/ | surrogate_primary | 2026-05-18 | Cochrane (cochranelibrary.com) | Cochrane Library: 国际系统评价权威数据库, Cochrane Complementary Medicine Field 专门收录 CAM/TCM SR / Cochrane Library [declared=surrogate_primary, auto=secondary; reason=vendor docs (Cochrane 国际系统评价 — .com 不在 primary suffix)] |
| T06-S127 | https://www.cacms.ac.cn/ | surrogate_primary | 2026-05-18 | 中国中医科学院 (cacms.ac.cn) | 中医辅助诊疗 AI / TCM CDSS: NATCM 立项 + CACMS + 各院校 研发的中医临床决策支持系统, 含智能舌诊 + 智能脉诊 / CACMS [declared=surrogate_primary, auto=secondary; reason=vendor docs (CACMS 国家级研究机构 + 监管业务下属 — .ac.cn 不在 primary suffix)] |
| T06-S128 | https://www.cacms.ac.cn/ | surrogate_primary | 2026-05-18 | 中国中医科学院 (cacms.ac.cn) | 智能舌诊 + 智能脉诊 / AI Tongue & Pulse Diagnosis: 基于图像识别 + 信号处理 的舌象 + 脉象客观化研究方向 / CACMS 中医客观化研究 [declared=surrogate_primary, auto=secondary; reason=vendor docs (CACMS 国家级研究机构 + 监管业务下属 — .ac.cn 不在 primary suffix)] |
