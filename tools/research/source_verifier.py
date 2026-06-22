#!/usr/bin/env python3
"""source_verifier.py — mechanical URL classifier for Phase 4 quality gate.

Classifies URLs into 5 buckets based on domain + path heuristics:

  verified_primary  Authoritative one-hand source (arXiv / DOI / official docs /
                    repo root / standard body / author's own blog / govt site).
                    Eligible to anchor a mental model claim.
  secondary         Secondhand reportage / analysis / encyclopedia / general
                    tech news. Allowed but cannot solo-anchor a claim.
  reference         Pointer-only — stack overflow answers, GH issue comments,
                    HN / Reddit threads, single tweets. Allowed as supporting
                    pointer, not as evidence.
  blacklisted       Locale-specific banned sources (zh-CN: 知乎 / 公众号 / 百度百科 /
                    CSDN / 博客园; en: G2 / Capterra / Medium-farm patterns;
                    universal: PR-wire / AI-summary auto-content).
  dead              HTTP HEAD returns 4xx/5xx or domain doesn't resolve. Only
                    checked when --check-liveness is set; otherwise unknown
                    URLs default to "secondary".

Pure stdlib. macOS python3 out-of-the-box.

Usage:
  # Single URL — exit code mirrors classification (0=primary, 1=secondary,
  # 2=reference, 3=blacklisted, 4=dead, 5=error)
  python3 source_verifier.py classify https://arxiv.org/abs/2305.12345

  # Batch a research directory's .md files, output JSON map URL→classification
  python3 source_verifier.py scan --research-dir <skill_dir>/references/research/

  # With liveness check (slower, ~1 HEAD request per URL; respects timeout)
  python3 source_verifier.py scan --research-dir <path> --check-liveness

  # Optional locale narrows the blacklist applied (default: both en + zh-CN)
  python3 source_verifier.py classify <URL> --locale zh-CN
"""
from __future__ import annotations

import argparse
import json
import re
import sys
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path
from typing import Any

# ---------------------------------------------------------------------------
# Classification tables. Order matters — earlier rules take priority.
# Key principle: domains-only when possible, path patterns only when domain
# is mixed-quality (e.g. youtube.com — channel root vs random video).
# ---------------------------------------------------------------------------

VerifiedPrimary = "verified_primary"
Secondary = "secondary"
Reference = "reference"
Blacklisted = "blacklisted"
Dead = "dead"
SurrogatePrimary = "surrogate_primary"  # manifest-only; never returned by classifier
Unknown = "secondary"  # default fallback

# Buckets the URL classifier can return on its own (auto). Manifests may also
# declare `surrogate_primary` per the cold-deep-mode policy in
# prompts/research/_source_id_manifest.md, but it's never auto-assigned.
AUTO_BUCKETS: tuple[str, ...] = (
    VerifiedPrimary, Secondary, Reference, Blacklisted, Dead,
)
ALL_BUCKETS: tuple[str, ...] = AUTO_BUCKETS + (SurrogatePrimary,)

EXIT_CODES = {
    VerifiedPrimary: 0,
    Secondary: 1,
    Reference: 2,
    Blacklisted: 3,
    Dead: 4,
}

# Domains that are blanket verified_primary regardless of path.
# Academic, standard bodies, government, journal publishers, well-known
# canonical channels.
PRIMARY_DOMAINS_EXACT: set[str] = {
    # iter (medical-aesthetics 2026-06-21): genuine first-hand domains for Chinese
    # medical aesthetics / injectables — global device & drug VENDOR official sites
    # (manufacturer = first-hand for their own 械字号/product spec), peer-reviewed
    # JOURNAL publishers (OUP/MDPI/Elsevier — scientific literature, recurs in every
    # medical/scientific field), the CSRC official disclosure platform 巨潮资讯 cninfo
    # (listed-company filings = issuer first-hand), and the 中华医学会 official journal
    # platform yiigle (consensus statements = association/originator first-hand).
    # Industry media (丁香园/39健康/界面/虎嗅/动脉网) is deliberately NOT whitelisted —
    # stays secondary (no washing of marketing/journalism into primary).
    "www.juvederm.com", "juvederm.com",               # AbbVie/艾尔建 乔雅登 vendor 官网
    "www.galderma.com", "galderma.com",               # 高德美 瑞蓝/吉适 vendor 官网
    "www.imeik.com.cn", "imeik.com.cn",               # 爱美客 Imeik 国产械字号 vendor 官网
    "www.merzaesthetics.com", "merzaesthetics.com",   # 默茨 Merz 西马/艾维岚/超声炮 vendor 官网
    "www.solta.com", "solta.com",                     # Solta Medical 热玛吉原厂 vendor 官网
    "www.canfield.com", "canfield.com",               # Canfield VISIA 原厂 vendor 官网
    "academic.oup.com",                               # Oxford University Press journals (ASJ 等同行评审)
    "www.mdpi.com", "mdpi.com",                       # MDPI 同行评审期刊 (Diagnostics 等)
    "www.sciencedirect.com", "sciencedirect.com",     # Elsevier 期刊全文 (同行评审一手)
    "www.cninfo.com.cn", "cninfo.com.cn", "static.cninfo.com.cn",  # 巨潮资讯 CSRC 指定披露站 = 发行人一手
    "rs.yiigle.com", "yiigle.com",                    # 中华医学会杂志社官方期刊平台 (专家共识原文 originator)
    # iter (web-novel-writing): genuine first-hand domains for Chinese web-novel
    # writing — national writers-association official platform (originator of the
    # 「破壁者」author-interview series + 学术综述), platform author-zones / official
    # rule & ranking pages (vendor/first-party), writing-tool vendor sites, and the
    # CASS academic platform. Commercial media reposts (腾讯新闻/澎湃/搜狐/光明网/界面/
    # 36氪/虎嗅) are deliberately NOT whitelisted — they stay secondary (no washing).
    "www.chinawriter.com.cn", "chinawriter.com.cn",   # 中国作家网 (中国作协官方, 破壁者访谈 originator + 学术综述)
    "write.qq.com",                                    # 阅文/起点官方作家专区 (写作问答/portal, vendor 一手)
    "www.fanqienovel.com", "fanqienovel.com",          # 番茄小说官方作家专区 (vendor 一手)
    "acts.qidian.com", "m.qidian.com", "www.qidian.com", "qidian.com",  # 起点官方规则/榜单/活动 (first-party)
    "www.cssn.cn", "cssn.cn",                          # 中国社会科学网 (CASS 学术平台 originator)
    "www.1xiezuo.com", "1xiezuo.com",                  # 壹写作 码字软件 vendor 官网
    "www.mx-xz.com", "mx-xz.com",                      # 墨星写作网 vendor 官网
    "www.mogugu.co", "mogugu.co",                      # 墨咕/墨者写作 vendor 官网
    "www.mubu.com", "mubu.com",                        # 幕布 大纲/思维导图 vendor 官网
    # iter40 (photography): genuine first-party photography vendor / standards-body
    # / optics docs domains — gear & post-processing vendors are first-party for
    # "what this tool is/does", ethics-code publishing bodies are originators.
    "www.aputure.com", "aputure.com",                # LED 持续光 vendor
    "www.topazlabs.com", "topazlabs.com",            # Topaz Photo AI vendor
    "www.dxo.com", "dxo.com",                        # DxO PureRAW/PhotoLab vendor
    "calibrite.com", "www.calibrite.com",            # 校色仪 vendor (ex X-Rite)
    "pixieset.com", "www.pixieset.com",              # 客片交付/选片平台 vendor
    "www.godox.com", "godox.com",                    # 平民灯具 vendor
    "www.sigma-global.com", "sigma-global.com",      # 副厂镜头 vendor
    "nppa.org", "www.nppa.org",                       # 视觉记者伦理守则发布机构
    "www.worldpressphoto.org", "worldpressphoto.org",# 改图/AI 红线发布机构 (originator)
    "lenspire.zeiss.com",                            # 蔡司光学技术白皮书 (optics 一手)
    "snapshot.canon-asia.com",                       # Canon 官方技法内容 (vendor 一手)
    # iter40 (photography): photography institutions / cooperatives / festivals /
    # competition orgs / podcast-official sites — first-party for the org/show.
    "www.magnumphotos.com", "magnumphotos.com",      # Magnum 摄影合作社 (Capa/Salgado/HCB 一手)
    "www.icp.org", "icp.org",                        # International Center of Photography (Capa 创办)
    "aperture.org", "www.aperture.org", "archive.aperture.org",  # Aperture 基金会/出版 (canon 机构)
    "www.iphf.org", "iphf.org",                      # Intl Photography Hall of Fame (机构)
    "www.hauserwirth.com", "hauserwirth.com",        # 画廊官方页 (代理艺术家一手资料)
    "thecandidframe.com", "www.thecandidframe.com",  # The Candid Frame 播客官方
    "thisweekinphoto.com", "www.thisweekinphoto.com",# TWiP 播客官方
    "www.streetphotographymagazine.com", "streetphotographymagazine.com",
    "fstopandlisten.podbean.com",                    # F-Stop Collaborate 播客官方 feed
    "phlearn.com", "www.phlearn.com",                # Aaron Nace 后期教育品牌官方
    "www.rencontres-arles.com", "rencontres-arles.com",  # Arles 摄影节官方
    "visapourlimage.com", "www.visapourlimage.com",  # Visa pour l'Image 纪实节官方
    "gulfphotoplus.com", "www.gulfphotoplus.com",    # GPP 官方
    "www.wppiexpo.com", "wppiexpo.com",              # WPPI 婚礼人像展官方
    "www.worldphoto.org", "worldphoto.org",          # Sony World Photography Awards 主办方
    "www.photoawards.com", "photoawards.com",        # IPA 国际摄影奖官方
    "arxiv.org",
    "doi.org",
    "ieeexplore.ieee.org",
    "dl.acm.org",
    "www.nature.com",
    "www.science.org",
    "www.cell.com",
    "www.thelancet.com",
    "www.nejm.org",
    "openreview.net",
    "papers.nips.cc",
    "papers.neurips.cc",
    "proceedings.mlr.press",
    "www.w3.org",
    "datatracker.ietf.org",
    "www.rfc-editor.org",
    "www.ietf.org",
    "www.iso.org",
    "www.iec.ch",
    "standards.ieee.org",
    "spec.commonmark.org",
    "www.unicode.org",
    "tc39.es",
    "schema.org",
    "developer.mozilla.org",
    "docs.python.org",
    "go.dev",
    "rust-lang.org",
    "kubernetes.io",
    "pytorch.org",
    "www.tensorflow.org",
    "huggingface.co",
    "platform.openai.com",
    "docs.anthropic.com",
    "ai.google.dev",
    "neurips.cc",
    "icml.cc",
    "iclr.cc",
    "aclanthology.org",
    "kubecon.io",
    "aaos.org",
    "aofas.org",
    "www.aofas.org",
    "www.aaos.org",
    "www.npc.gov.cn",  # 全国人大 — 立法源
    "www.court.gov.cn",  # 最高法
    "www.spp.gov.cn",  # 最高检
    "www.gov.cn",  # 中国政府门户
    "scholar.google.com",
    "semanticscholar.org",
    # Iter 26: industry standards bodies (insurance / finance) — referenced as
    # canonical sources by master-skill insurance-broker-cn run.
    "www.mdrt.org",
    "mdrt.org",
    "www.lloyds.com",
    "lloyds.com",
    "www.iso20022.org",  # finance messaging standard
    "www.bis.org",       # Bank for International Settlements
    "www.imf.org",
    "www.worldbank.org",
    # Iter 27: Chinese classics digital archives — canonical text ground truth
    # for any zh-CN classics-heavy industry (bazi-metaphysics, china-law historical
    # canon, traditional Chinese medicine, etc.).
    "ctext.org",                  # Chinese Text Project — 古籍数字化主源
    "www.guoxuedashi.net",        # 国学大师 — 综合古籍数据库
    "zh.wikisource.org",          # 中文维基文库 — 公共领域古籍
    "archive.org",                # Internet Archive — 民国整理本 PDF / 长内容档案
    "www.archive.org",
    # Iter 28: design / dev-tooling first-party — Adobe / Figma / Microsoft Learn /
    # ICC / Photopea / package registries / ImageMagick. Canonical for figma-to-psd
    # + any design-tool / frontend / file-format skill. Generic improvement.
    "www.adobe.com",
    "adobe.com",
    "helpx.adobe.com",
    "news.adobe.com",
    "developer.adobe.com",
    "www.figma.com",
    "figma.com",
    "help.figma.com",
    "learn.microsoft.com",
    "color.org",
    "www.color.org",
    "registry.color.org",
    "www.photopea.com",
    "photopea.com",
    "www.npmjs.com",
    "npmjs.com",
    "registry.npmjs.org",
    "pypi.org",
    "www.pypi.org",
    "imagemagick.org",
    "www.imagemagick.org",
    # Iter 30 (ai-short-drama): AIGC video/model vendor official sites + zh-CN
    # content-industry data platforms + platform/studio/festival official — these
    # ARE the subject/canon of AI 短剧 (parallel to figma-to-psd allowlisting
    # Adobe/Figma). Generic for any AIGC-video / content-ops / 出海 skill.
    "kling.ai", "www.kling.ai",          # 可灵 (快手)
    "jimeng.jianying.com",                # 即梦 (字节)
    "vidu.cn", "www.vidu.cn",            # Vidu (生数)
    "minimaxi.com", "www.minimaxi.com",  # MiniMax
    "hailuoai.com", "hailuoai.video",    # 海螺 AI
    "volcengine.com", "www.volcengine.com",  # 火山引擎 (字节; 即梦/豆包)
    "tongyi.aliyun.com",                  # 通义 (阿里)
    "www.aliyun.com", "aliyun.com",      # 阿里云官方文档 (百炼/通义)
    "chatglm.cn",                         # 智谱清影
    "heygen.com", "www.heygen.com",      # HeyGen 对口型
    "pixverse.ai", "www.pixverse.ai",    # PixVerse
    "lumalabs.ai",                        # Luma
    "fal.ai",                             # fal
    "capcut.cn", "www.capcut.cn",        # 剪映 / CapCut
    "ir.kuaishou.com",                    # 快手投资者关系 (官方披露)
    "m.yangshipin.cn", "yangshipin.cn", "www.yangshipin.cn",  # 央视频 (平台官方)
    "bonafilm.cn", "www.bonafilm.cn",    # 博纳影业 (出品方官方)
    "www.bjiff.com", "bjiff.com",        # 北京国际电影节 (官方)
    "www.dataeye.com", "dataeye.com",    # DataEye 短剧数据
    "www.enlightent.cn", "enlightent.cn",# 艺恩数据
    "www.diandian.com", "diandian.com",  # 点点数据 (出海)
    "www.newrank.cn", "newrank.cn",      # 新榜
    # Iter 31 (personal-investing): finance/investing first-party authorities —
    # fund companies whose investor-education + research IS the canon (Vanguard =
    # Bogle's firm), the Berkshire letters (Buffett/Munger primary source), the
    # de-facto passive-investing canon (Bogleheads wiki), canonical data/ratings
    # providers (Morningstar), SRO + professional standards bodies (FINRA / CFA),
    # factor-research first-party (AQR), the finance working-paper archive (SSRN =
    # arXiv-equivalent for finance), authoritative fund manager memos (Oaktree =
    # Howard Marks), and the Fed economic-data archive. Generic for any future
    # investing / personal-finance / asset-allocation skill.
    "www.berkshirehathaway.com", "berkshirehathaway.com",  # Buffett/Munger 股东信 — 一手
    "www.vanguard.com", "vanguard.com", "investor.vanguard.com", "corporate.vanguard.com",
    "www.fidelity.com", "fidelity.com",
    "www.schwab.com", "schwab.com",
    "www.interactivebrokers.com", "interactivebrokers.com", "ibkr.com",
    "www.morningstar.com", "morningstar.com",      # 基金数据/评级 — canonical
    "www.bogleheads.org", "bogleheads.org",         # Bogleheads wiki — 被动投资正典
    "www.finra.org", "finra.org",                   # SRO 监管 — 投资者保护权威
    "www.cfainstitute.org", "cfainstitute.org",     # CFA Institute — 专业标准机构
    "www.aqr.com", "aqr.com",                       # AQR — 因子研究一手 (Asness)
    "papers.ssrn.com", "ssrn.com", "www.ssrn.com",  # SSRN — 金融工作论文档案
    "www.oaktreecapital.com", "oaktreecapital.com", # Oaktree — Howard Marks memos
    "fred.stlouisfed.org",                          # FRED — 美联储经济数据档案
    "www.spglobal.com", "spglobal.com",             # S&P DJI / SPIVA — 主动vs被动权威记分卡(官方一手), 同 Morningstar 级数据机构
    # Iter 32 (speech-to-text): official cloud + ASR vendor docs. cloud.google /
    # azure / aws docs are first-party canon for ANY cloud/tech skill; Deepgram /
    # AssemblyAI are canonical ASR API docs; k2-fsa = sherpa-onnx/k2 project docs.
    "deepgram.com", "www.deepgram.com",
    "assemblyai.com", "www.assemblyai.com",
    "cloud.google.com",
    "azure.microsoft.com",
    "aws.amazon.com", "docs.aws.amazon.com",
    "k2-fsa.github.io",
    # Iter 34 (web-online-exhibition): 3D-web / WebXR / standards / panorama-lib
    # official docs — Three.js / Khronos / glTF-Transform / model-viewer / R3F /
    # Babylon / IIIF / A-Frame / panorama viewers / web.dev / SIGGRAPH. First-party
    # canon for any web-3D / WebXR / frontend-perf / digital-museum skill. Generic.
    "threejs.org", "www.threejs.org",
    "discoverthreejs.com",
    "www.khronos.org", "khronos.org", "registry.khronos.org",
    "modelviewer.dev",
    "gltf-transform.dev",
    "r3f.docs.pmnd.rs", "docs.pmnd.rs",
    "doc.babylonjs.com", "babylonjs.com", "www.babylonjs.com",
    "iiif.io", "www.iiif.io",
    "aframe.io",
    "pannellum.org", "www.pannellum.org",
    "photo-sphere-viewer.js.org",
    "www.marzipano.net", "marzipano.net",
    "binomialllc.github.io",
    "matterport.github.io",
    "www.agisoftmetashape.com", "agisoftmetashape.com",
    "web.dev",
    "web3d.siggraph.org", "s2026.siggraph.org",
    # Iter 35 (management-consulting): top-3 strategy firms' OWN insight/publication
    # sites + HBR/HBS Publishing + Big-Four strategy arms + major boutique firms.
    # These are first-party thought-leadership canon (BCG growth-share matrix /
    # experience curve, McKinsey 7S/Three Horizons, Bain NPS, Porter Five Forces via
    # HBR) — the firms literally authored the frameworks. Parallel to allowlisting
    # Adobe/Figma for design or Vanguard/Berkshire for investing. Generic for any
    # strategy / business / management / case-interview skill.
    "www.mckinsey.com", "mckinsey.com",
    "www.bcg.com", "bcg.com",
    "www.bain.com", "bain.com",
    "hbr.org", "www.hbr.org",          # Harvard Business Review — strategy canon journal
    "store.hbr.org",                   # HBR Store — official article/book landing
    "www.deloitte.com", "deloitte.com", "www2.deloitte.com",
    "www.strategyand.pwc.com", "strategyand.pwc.com",  # Strategy& (PwC)
    "www.pwc.com", "pwc.com",
    "www.ey.com", "ey.com",
    "kpmg.com", "www.kpmg.com",
    "www.oliverwyman.com", "oliverwyman.com",
    "www.kearney.com", "kearney.com",
    "www.rolandberger.com", "rolandberger.com",
    "www.lek.com", "lek.com",
    "www.adlittle.com", "adlittle.com",  # Arthur D. Little
    "www.netpromotersystem.com", "netpromotersystem.com",  # Bain NPS official
    "bcghendersoninstitute.com", "www.bcghendersoninstitute.com",  # BCG's official R&D institute (Henderson/experience-curve canon archive)
    # Consulting-canon author OWN sites (parallel to lexfridman.com / karpathy.ai above):
    "www.barbaraminto.com", "barbaraminto.com",  # Barbara Minto — Pyramid Principle author official
    "caseinterview.com", "www.caseinterview.com",  # Victor Cheng — Case Interview Secrets / LOMS official
    "mwstewart.com", "www.mwstewart.com",          # Matthew Stewart — The Management Myth author
    "rogerlmartin.com", "www.rogerlmartin.com",  # Roger Martin (Playing to Win) official
    "www.mintzberg.org", "mintzberg.org",          # Henry Mintzberg official
    "blueoceanstrategy.com", "www.blueoceanstrategy.com",  # Kim & Mauborgne Blue Ocean official
    "claytonchristensen.com", "www.claytonchristensen.com",  # Clayton Christensen official
    "www.ritamcgrath.com", "ritamcgrath.com",      # Rita McGrath — transient advantage / inflection points official
    "tompeters.com", "www.tompeters.com",          # Tom Peters — In Search of Excellence / 7S author official
    # Iter 36 (enterprise-b2b-sales): B2B complex-sales methodology ORIGINATORS'
    # own sites (they authored the methodologies — parallel to McKinsey authoring
    # 7S or Adobe authoring PSD) + the canonical first-party data lab (Gong Labs)
    # + the de-facto practitioner podcast. These ARE the canon of enterprise B2B
    # selling. Generic for any future sales / GTM / revenue skill.
    "www.forcemanagement.com", "forcemanagement.com",      # Force Management — Command of the Message / Value Framework originator
    "www.sandler.com", "sandler.com",                      # Sandler — Sandler Selling System originator
    "meddicc.com", "www.meddicc.com",                      # MEDDICC (Andy Whyte) — MEDDIC/MEDDPICC canon org
    "meddic.academy", "www.meddic.academy",                # MEDDIC Academy (Darius Lahoutifard) — MEDDIC training originator
    "www.challengerinc.com", "challengerinc.com",          # Challenger Inc — the org behind The Challenger Sale/Customer
    "winningbydesign.com", "www.winningbydesign.com",      # Winning by Design (Jacco van der Kooij) — SaaS revenue architecture / bowtie canon
    "predictablerevenue.com", "www.predictablerevenue.com",# Predictable Revenue (Aaron Ross) — SDR/AE split canon
    "www.forentrepreneurs.com", "forentrepreneurs.com",    # David Skok — SaaS metrics canon (CAC/LTV/magic number)
    "www.gong.io", "gong.io",                              # Gong — Gong Labs first-party conversation-intelligence sales research (widely-cited benchmark data)
    "30mpc.com", "www.30mpc.com",                          # 30 Minutes to President's Club — de-facto top practitioner podcast (Cegelski & Farrokh)
    "www.rainsalestraining.com", "rainsalestraining.com",  # RAIN Group — insight selling first-party research
    "www.richardson.com", "richardson.com",                # Richardson Sales Performance — Sprint Selling / acquired Huthwaite-SPIN lineage
    "www.huthwaiteinternational.com", "huthwaiteinternational.com",  # Huthwaite International — the org Rackham founded; SPIN methodology originator
    "jolteffect.com", "www.jolteffect.com",                # The JOLT Effect (Dixon & McKenna) — no-decision/FOMU canon book site
    # Iter 35 (clinical-diagnostic-reasoning): medical journals / academic
    # publishers / med orgs + the field's own teaching orgs. First-party canon
    # for any medical / clinical / health / med-ed skill. Generic.
    "jamanetwork.com", "www.jamanetwork.com",
    "www.amjmed.com",                          # American Journal of Medicine
    "www.annemergmed.com",                     # Annals of Emergency Medicine
    "bjgp.org",                                # British Journal of General Practice
    "link.springer.com", "www.springer.com",   # Springer
    "journals.lww.com",                        # Wolters Kluwer / LWW (Academic Medicine)
    "www.tandfonline.com", "tandfonline.com",  # Taylor & Francis
    "www.degruyter.com", "degruyter.com",      # De Gruyter (Diagnosis 期刊)
    "bmcmededuc.biomedcentral.com",            # BMC Medical Education
    "www.nationalacademies.org", "nationalacademies.org", "nap.nationalacademies.org",  # NAM/NASEM 报告
    "www.aamc.org", "aamc.org",                # AAMC
    "www.improvediagnosis.org", "improvediagnosis.org",  # SIDM 诊断安全学会
    "clinicalproblemsolving.com", "www.clinicalproblemsolving.com",  # Clinical Problem Solvers
    "www.massgeneral.org",                     # Mass General (academic hospital)
    "ucsdim.com",                              # UCSD Internal Medicine 教学
    # Iter 36 (xiaohongshu / twitter-cn AI creator): 小红书官方子域(平台规则/创作一手)
    # + 中文 AI 创作者个人站(figure 一手)。通用于 zh-CN 内容创作者 / 自媒体 skill。
    "creator.xiaohongshu.com", "pgy.xiaohongshu.com",
    "school.xiaohongshu.com", "pro.xiaohongshu.com",
    "guizang.ai", "www.guizang.ai",            # 歸藏 个人站
    "qiaomu.ai", "www.qiaomu.ai",              # 向阳乔木 个人站
    "baoyu.io", "www.baoyu.io",                # 宝玉 个人站
    # Iter 37 (twitter-cn AI creator): X 官方 docs + 代码截图工具 + 英文写作 canon
    # 作者站。通用 zh-CN/全球 内容创作者 / 写作 / 独立开发 skill。
    "help.x.com", "legal.x.com",
    "carbon.now.sh",
    "swyx.io", "www.swyx.io",                  # swyx — Learn in Public
    "perell.com", "www.perell.com",            # David Perell — Write of Passage
    "readmake.com", "www.readmake.com",        # Pieter Levels — MAKE (build in public)
    # Iter 38 (zhihu AI creator): AI content-production tool vendor official sites
    # — first-party product homepages (parallel to figma/photopea allowlisting).
    # Generic for any AI-writing / content-ops / LLM-tooling skill.
    "metaso.cn", "www.metaso.cn",               # 秘塔 AI 搜索 (上海秘塔科技)
    "kimi.com", "www.kimi.com",                 # Kimi (月之暗面 Moonshot)
    "deepseek.com", "www.deepseek.com",         # DeepSeek (深度求索)
    "doubao.com", "www.doubao.com",             # 豆包 (字节)
    "claude.ai",                                # Claude (Anthropic)
    "perplexity.ai", "www.perplexity.ai",       # Perplexity
    "midjourney.com", "www.midjourney.com",     # Midjourney
    "mermaid.live",                             # Mermaid Live Editor (official)
    "drawio.com", "www.drawio.com",             # draw.io (JGraph) 官方
    "ray.so",                                   # ray.so 代码美图 (Raycast 出品)
    "editor.mdnice.com", "mdnice.com", "www.mdnice.com",  # Markdown Nice (墨滴) 官方编辑器
    "matrix.tencent.com",                       # 腾讯朱雀 AI 检测 (official)
    # Iter 39 (music-production): audio-engineering first-party — plugin/hardware
    # vendors (FabFilter/iZotope/UAD/Waves/Valhalla authored the de-facto tools,
    # parallel to Adobe/Figma for design), the field's canonical trade press
    # (Sound on Sound / Mix / Tape Op — like HBR for consulting), pro standards
    # bodies (AES / EBU loudness), and originator masterclass/education platforms.
    # Generic for any future audio / recording / mixing / mastering skill.
    "www.soundonsound.com", "soundonsound.com",          # Sound on Sound — canonical recording/mixing trade magazine
    "www.mixonline.com", "mixonline.com",                # Mix magazine
    "tapeop.com", "www.tapeop.com",                       # Tape Op
    "www.aes.org", "aes.org",                             # Audio Engineering Society — pro standards/journal body
    "tech.ebu.ch", "www.ebu.ch", "ebu.ch",               # EBU R128 loudness standard (BS.1770 lineage)
    # plugin / DAW / hardware vendor official sites (vendor docs = first-party tool source)
    "www.fabfilter.com", "fabfilter.com",
    "www.izotope.com", "izotope.com",
    "www.uaudio.com", "uaudio.com",                       # Universal Audio
    "www.waves.com", "waves.com",
    "www.plugin-alliance.com", "plugin-alliance.com",
    "valhalladsp.com", "www.valhalladsp.com",
    "www.native-instruments.com", "native-instruments.com",
    "www.ableton.com", "ableton.com",
    "www.avid.com", "avid.com",                           # Pro Tools
    "www.steinberg.net", "steinberg.net",                 # Cubase
    "www.image-line.com", "image-line.com",               # FL Studio
    "www.reaper.fm", "reaper.fm",                          # Cockos REAPER
    "www.presonus.com", "presonus.com",                  # Studio One
    "www.soundtoys.com", "soundtoys.com",
    "www.slatedigital.com", "slatedigital.com",
    "www.eventideaudio.com", "eventideaudio.com",
    "www.genelec.com", "genelec.com",
    "www.rme-audio.de", "rme-audio.de",
    "www.adam-audio.com", "adam-audio.com",
    "www.focusrite.com", "focusrite.com",
    "splice.com", "www.splice.com",                       # Splice — sample/loop ecosystem
    "www.spitfireaudio.com", "spitfireaudio.com",
    "www.celemony.com", "celemony.com",                   # Melodyne (pitch/time editing)
    "www.antarestech.com", "antarestech.com",             # Auto-Tune
    # originator masterclass / education platforms (parallel to caseinterview.com)
    "mixwiththemasters.com", "www.mixwiththemasters.com",
    "www.producelikeapro.com", "producelikeapro.com",    # Warren Huart
    "www.puremix.com", "puremix.com", "puremix.net",
    # iter (investment-banking-mna): M&A is a practitioner field whose first-party
    # voices are the advisory banks, the market-data originators, the deal-tooling
    # vendors, and the dealmaker podcasts. Same precedent as the design/dev-tooling
    # vendor allowlist (figma/adobe) and the audio-gear vendors above — a firm's /
    # vendor's / data-originator's OWN site is verified_primary for itself.
    # (Education vendors — WSP/CFI/BIWS/TTS — stay surrogate_primary via note; law
    #  firm client alerts stay surrogate_primary "own publication".)
    # — advisory / M&A boutiques (their own thought-leadership + deal pages):
    "www.goldmansachs.com", "goldmansachs.com",
    "www.lazard.com", "lazard.com",
    "www.moelis.com", "moelis.com",
    "www.centerviewpartners.com", "centerviewpartners.com",
    "www.pjtpartners.com", "pjtpartners.com",
    "pwpartners.com", "www.pwpartners.com",            # Perella Weinberg
    "www.hl.com", "hl.com",                            # Houlihan Lokey
    # — market-data / deal-data originators (their own data + press):
    "press.spglobal.com", "www.spglobal.com", "spglobal.com",
    "www.lseg.com", "lseg.com",                        # LSEG / Refinitiv
    "pitchbook.com", "www.pitchbook.com",
    "dealogic.com", "www.dealogic.com",
    "info.mergermarket.com", "www.mergermarket.com", "mergermarket.com",
    "insight.factset.com", "www.factset.com", "factset.com",
    "www.bloomberg.com",                               # data/terminal originator pages
    "www.srsacquiom.com", "srsacquiom.com",            # SRS Acquiom deal-terms study (dataset originator)
    # — deal tooling / VDR / AI-for-finance vendors (own product + docs pages):
    "www.microsoft.com", "microsoft.com",              # Excel/PowerPoint product pages (subdomains already covered)
    "www.think-cell.com", "think-cell.com",
    "upslide.net", "www.upslide.net",
    "macabacus.com", "www.macabacus.com",
    "www.intralinks.com", "intralinks.com",
    "www.idealsvdr.com", "idealsvdr.com",
    "www.datasite.com", "datasite.com",
    "www.ansarada.com", "ansarada.com",
    "www.firmex.com", "firmex.com",
    "intapp.com", "www.intapp.com",
    "www.hebbia.com", "hebbia.com",
    "www.brightwave.io", "brightwave.io",
    "www.blueflame.ai", "blueflame.ai",
    "rogo.ai", "www.rogo.ai",
    "daloopa.com", "www.daloopa.com",
    "grata.com", "www.grata.com",
    "kisonpatel.com", "www.kisonpatel.com",            # DealRoom / Kison Patel own site
    "www.mascience.com", "mascience.com",              # M&A Science (Kison Patel) — podcast + book + blog platform
    "www.alpha-sense.com", "alpha-sense.com",
    # — dealmaker podcast channels (channel own site = primary, like a youtube channel):
    "www.acquired.fm", "acquired.fm",
    "podcasts.thecompoundnews.com",
    # iter (product-ux-design): UX research org + design-tool vendors + standards
    # bodies — genuine first-party. NN/g = Nielsen & Norman's own research org (the
    # definitive UX first-hand authority); vendor official sites = vendor 一手 (per
    # manifest Surrogate Policy "vendor docs = verified_primary"); standards bodies =
    # ground truth. Generic for any future design / UX / product-design skill.
    "www.nngroup.com", "nngroup.com",                   # Nielsen Norman Group — UX 研究一手权威
    "www.designcouncil.org.uk", "designcouncil.org.uk", # UK Design Council — Double Diamond originator
    "designtokens.org", "tr.designtokens.org",          # W3C Design Tokens Community Group — 标准
    "www.designkit.org", "designkit.org",               # IDEO — Design Kit 方法库 (一手)
    "config.figma.com",                                 # Figma Config — vendor 自家大会
    # — design-tool / research-tool vendor official sites (vendor 一手):
    "www.figma.com", "figma.com",
    "www.optimalworkshop.com", "optimalworkshop.com",
    "www.maze.co", "maze.co",
    "v0.dev",
    "zeroheight.com", "www.zeroheight.com", "report.zeroheight.com",
    "www.usertesting.com", "usertesting.com",
    "www.tailwindcss.com", "tailwindcss.com",
    "www.supernova.io", "supernova.io",
    "www.sketch.com", "sketch.com",
    "www.protopie.io", "protopie.io",
    "principleformac.com", "www.principleformac.com",
    "penpot.app", "www.penpot.app",
    "miro.com", "www.miro.com",
    "tokens.studio", "www.tokens.studio",
    "dovetail.com", "www.dovetail.com",
    "clarity.microsoft.com",
    "baymard.com", "www.baymard.com",
    "www.hotjar.com", "hotjar.com",
    "www.framer.com", "framer.com",
    # iter (crypto-onchain-trading): genuine first-party crypto vendor/tool/
    # exchange/protocol/conference/research domains. On-chain trading is a
    # data-rich field whose ground-truth lives in analytics-platform docs,
    # exchange/DEX/wallet official sites, protocol foundations, conference
    # official event pages, and a few original-research firms. These are the
    # entity "speaking about its own product/event/research" = verified_primary
    # (vendor 一手). News/journalism media (The Block / Blockworks / The Defiant /
    # BlockBeats / PANews / Foresight) deliberately NOT added — they stay secondary.
    # --- on-chain analytics / data platforms ---
    "coinglass.com", "www.coinglass.com",
    "nansen.ai", "www.nansen.ai",
    "dune.com", "www.dune.com",
    "defillama.com", "www.defillama.com",
    "tokenterminal.com", "www.tokenterminal.com",
    "debank.com", "www.debank.com",
    "dexscreener.com", "www.dexscreener.com",
    "gmgn.ai", "www.gmgn.ai",
    "photon-sol.tinyastro.io",
    "cryptoquant.com", "www.cryptoquant.com", "userguide.cryptoquant.com",
    "glassnode.com", "www.glassnode.com", "insights.glassnode.com",
    "arkm.com", "www.arkm.com", "codex.arkm.com", "intel.arkm.com",
    "token.unlocks.app",
    "tokenomist.ai", "www.tokenomist.ai",
    "rootdata.com", "www.rootdata.com",
    # --- exchanges / DEX / wallets / security tools ---
    "metamask.io", "www.metamask.io",
    "ledger.com", "www.ledger.com",
    "hyperliquid.xyz", "app.hyperliquid.xyz", "www.hyperliquid.xyz",
    "jup.ag", "www.jup.ag",
    "1inch.io", "www.1inch.io",
    "uniswap.org", "app.uniswap.org", "www.uniswap.org",
    "rabby.io", "www.rabby.io",
    "phantom.com", "www.phantom.com",
    "revoke.cash", "www.revoke.cash",
    "gopluslabs.io", "www.gopluslabs.io",
    "de.fi", "www.de.fi",
    "rugcheck.xyz", "www.rugcheck.xyz",
    "axiom.trade", "www.axiom.trade",
    "gmx.io", "www.gmx.io",
    "dydx.exchange", "www.dydx.exchange",
    "solana.com", "www.solana.com",
    "kraken.com", "www.kraken.com",
    "coinbase.com", "www.coinbase.com",
    "tradingview.com", "www.tradingview.com",
    "coingecko.com", "www.coingecko.com",
    # --- protocol foundations (official) ---
    "bitcoin.org", "www.bitcoin.org",
    "ethereum.org", "www.ethereum.org",
    # --- conferences (official event sites = first-party of the event) ---
    "token2049.com", "www.token2049.com",
    "consensus.coindesk.com",
    "devconnect.org", "www.devconnect.org",
    "ethdenver.com", "www.ethdenver.com",
    # --- podcasts (official channel = first-party show) ---
    "uponly.tv", "www.uponly.tv",
    "unchainedcrypto.com", "www.unchainedcrypto.com",
    # --- original-research firms (first-party on-chain research, not journalism) ---
    "messari.io", "www.messari.io",
    "a16zcrypto.com", "www.a16zcrypto.com",
    "delphidigital.io", "www.delphidigital.io", "members.delphidigital.io",
    # iter (semiconductor-process): genuine first-hand domains for IC fabrication —
    # equipment/EDA vendors (vendor docs), foundry/IDM official tech blogs & investor
    # disclosures, standards/roadmap bodies (IRDS/IEEE), research institutes (imec/VTT),
    # academic publishers + journals (OUP/Wiley/AIP), the IEDM conference handout host,
    # a scientific society (AVS), and a museum archive (CHM oral histories = originator's
    # own words). Industry media (SemiEngineering/EE Times/SemiWiki/SemiAnalysis) stays
    # secondary; this only whitelists "the entity speaking about its own thing".
    # --- equipment / EDA / materials vendors (official vendor docs) ---
    "asml.com", "www.asml.com",
    "synopsys.com", "www.synopsys.com",
    "plasmatherm.com", "www.plasmatherm.com", "corial.plasmatherm.com",
    "oxinst.com", "plasma.oxinst.com",
    # --- foundries / IDMs (official tech blog + investor disclosure = first-party) ---
    "tsmc.com", "www.tsmc.com", "investor.tsmc.com",
    "intel.com", "www.intel.com", "newsroom.intel.com",
    "semiconductor.samsung.com",
    "ibm.com", "www.ibm.com",
    # --- standards / roadmap bodies (IRDS roadmap = ground-truth spec) ---
    "irds.ieee.org", "ieee.org", "www.ieee.org",
    # --- research institutes (own published research) ---
    "imec-int.com", "www.imec-int.com",
    "vtt.fi", "www.vtt.fi", "sarjaweb.vtt.fi",
    # --- academic publishers + journals (peer-reviewed first-hand) ---
    "global.oup.com", "oup.com",
    "onlinelibrary.wiley.com", "wiley.com",
    "pubs.aip.org", "aip.org",
    # --- scientific society (originator talks, e.g. AVS CMP user group) ---
    "avs.org", "www.avs.org", "nccavs-usergroups.avs.org",
    # --- IEDM conference official handout host (first-party of the conference) ---
    "iedm23.mapyourshow.com", "mys.mapyourshow.com", "iedm.mapyourshow.com",
    # --- museum archive (Computer History Museum oral histories = originator's words) ---
    "computerhistory.org", "www.computerhistory.org", "archive.computerhistory.org",
    # --- original-research / reverse-engineering firms (first-party measurement, NOT
    # journalism) — the semiconductor analog of the crypto research-firm whitelist
    # (messari/a16zcrypto/delphi). TechInsights physically delayers & measures shipping
    # silicon (the de-facto ground truth for real node parameters); IC Knowledge builds
    # original cost/process-economics models. Their published findings are first-hand
    # empirical data. Analyst NEWSLETTERS that are commentary/journalism (SemiAnalysis,
    # SemiEngineering, EE Times) stay secondary.
    "techinsights.com", "www.techinsights.com",
    "icknowledge.com", "www.icknowledge.com",
    # iter (aigc-creative-workflow 2026-06-22): genuine first-party AIGC visual-creation
    # MODEL/TOOL VENDOR official sites — first-hand for their own model spec / license /
    # release notes (parallel to allowlisting Adobe/Figma for design, device vendors for
    # medical). Black Forest Labs (Flux) rebranded blackforestlabs.ai → bfl.ai; Stability
    # AI official news/blog; Runway/Luma/Ideogram/Recraft official. arxiv/github/
    # huggingface/civitai already covered by generic rules. AI-tool review/listicle sites
    # (pxz.ai/aimagicx 等 /blog SEO) are deliberately NOT whitelisted — stay secondary.
    "bfl.ai", "www.bfl.ai", "blackforestlabs.ai", "www.blackforestlabs.ai",  # Black Forest Labs / Flux 官方
    "stability.ai", "www.stability.ai",               # Stability AI 官方 news/blog (SD/SDXL/SD3 originator)
    "runwayml.com", "www.runwayml.com",               # Runway 官方 (Gen-3/Gen-4 vendor)
    "lumalabs.ai", "www.lumalabs.ai",                 # Luma Dream Machine 官方
    "ideogram.ai", "www.ideogram.ai",                 # Ideogram 官方
    "www.recraft.ai", "recraft.ai",                   # Recraft 官方
}

# Suffix patterns for primary (TLD or sub-domain end-match).
PRIMARY_DOMAIN_SUFFIXES: tuple[str, ...] = (
    ".gov",
    ".gov.cn",
    ".gov.uk",
    ".gov.hk",
    ".gov.tw",
    ".gov.jp",
    ".gov.kr",
    ".edu",
    ".edu.cn",
    ".ac.uk",
    ".ac.jp",
    ".mil",
    ".int",
    ".org.cn",  # 行业协会
    ".edu.tw",  # iter (semiconductor-process): Taiwan academic (NYCU/NTU 等) — IC 研究重镇
    ".chinalaw.gov.cn",
    ".readthedocs.io",  # iter 28: OSS project docs (read-the-docs hosted) — first-party
    # iter 29 (study-camp-education): experiential-ed / camp / outdoor-ed standard
    # bodies, method originators, nonprofit canonical platforms, national gov edu
    # platform — genuine first-hand authorities (not commercial vendor marketing).
    ".acacamps.org",      # American Camp Association — 营地认证标准机构
    ".lnt.org",           # Leave No Trace — 户外无痕原则标准机构
    ".pblworks.org",      # PBLWorks / Buck Institute — Gold Standard PBL 方法 originator
    ".outwardbound.net",  # Outward Bound — 外展 / 体验教育运动 org
    ".icfconnect.net",    # International Camping Fellowship — 国际营地组织
    ".cceacamps.org",     # 中国营地教育联盟 CCEA — 全国行业联盟（.org，非 .org.cn）
    ".inaturalist.org",   # iNaturalist — 公益公民科学平台（自然教育工具一手）
    ".smartedu.cn",       # 国家智慧教育公共服务平台（教育部国家级平台）
    # iter (perfumery): EU official institutional domain — every *.europa.eu host
    # is an EU body (eur-lex 立法原文 / osha / ec / europarl). Legislation original
    # text = genuine verified_primary; recurs in any EU-regulated profession.
    ".europa.eu",
)

# Known author / podcast / personal blog primaries (heuristic).
# This list is non-exhaustive — agent can extend per industry research.
PRIMARY_PERSONAL_DOMAINS: set[str] = {
    # iter40 (photography): figure/estate own sites — author blogs + artist foundation
    "henricartierbresson.org", "www.henricartierbresson.org",  # Fondation HCB (作者基金会)
    # iter (crypto-onchain-trading): figure/author own blogs & self-hosted pubs
    "www.lynalden.com", "lynalden.com",                         # Lyn Alden 本人宏观站
    "vitalik.eth.limo", "vitalik.ca",                           # Vitalik Buterin 本人博客
    "hasu.blog",                                                # Hasu 本人研究博客
    "uncommoncore.co", "www.uncommoncore.co",                   # Hasu/Uncommon Core 本人研究
    "woobull.com", "charts.woobull.com",                        # Willy Woo 本人(NVT/链上指标 originator)
    "cryptohayes.medium.com",                                   # Arthur Hayes 本人 Medium 长文
    "strobist.blogspot.com",                                    # David Hobby 本人 Strobist 原文
    "joemcnally.com", "www.joemcnally.com",                     # Joe McNally 本人博客
    "seantucker.photography", "www.seantucker.photography",     # Sean Tucker 本人教程站
    "www.anseladams.com", "anseladams.com",                     # Ansel Adams 官方/画廊
    "www.stevemccurry.com", "stevemccurry.com",                 # Steve McCurry 本人官网
    "www.chasejarvis.com", "chasejarvis.com",                   # Chase Jarvis 本人官网
    "www.joelgrimes.com", "joelgrimes.com",                     # Joel Grimes 本人官网
    "karltaylor.com", "www.karltaylor.com",                     # Karl Taylor 本人
    "visualeducation.com", "www.visualeducation.com",           # Karl Taylor 教育平台
    "zackarias.com", "www.zackarias.com",                       # Zack Arias 本人
    "www.aaron-nace.com", "aaron-nace.com",                     # Aaron Nace 本人
    "erickimphotography.com", "www.erickimphotography.com",     # Eric Kim 本人街头博客
    "www.billwadman.com", "billwadman.com",                     # Bill Wadman 摄影师本人博客
    "www.joeedelman.com", "joeedelman.com",                     # Joe Edelman 本人
    "www.solsticeretouch.com", "solsticeretouch.com",           # Pratik Naik 工作室官方
    "www.saulleiterfoundation.org", "saulleiterfoundation.org", # Saul Leiter 基金会
    "learn.lindsayadlerphotography.com",
    "lindsayadlerphotography.com", "www.lindsayadlerphotography.com",  # Lindsay Adler 本人
    "victorliu.tuchong.com", "thomaskksj.tuchong.com",          # 阿刘/储卫民 图虫创作者主页 (一手)
    "asianometry.com", "www.asianometry.com",  # iter (semiconductor): Jon Y 本人 newsletter/深度 essay
    "lexfridman.com",
    "latent.space",
    "www.latent.space",
    "swyx.io",
    "simonwillison.net",
    "karpathy.ai",
    "magazine.sebastianraschka.com",
    "rachelbythebay.com",
    "danluu.com",
    "stratechery.com",
    "mattturck.com",
    "blog.replit.com",
    "anthropic.com",
    "openai.com",
    "deepmind.com",
    "deepmind.google",
    # Iter 28: cross-tool / design-tooling figure blogs
    "bjango.com",          # Marc Edwards — cross-tool rendering fidelity authority
    "www.bjango.com",
    "madebyevan.com",      # Evan Wallace — Figma co-founder, .fig format internals
    # Iter 31 (personal-investing): investing figure first-party blogs / podcasts —
    # the authors' OWN sites where their thinking lives long-form. Generic for any
    # future personal-finance / investing skill.
    "rationalreminder.ca", "www.rationalreminder.ca",   # Ben Felix / PWL — 被动+因子证据派
    "jlcollinsnh.com", "www.jlcollinsnh.com",           # JL Collins — Simple Path to Wealth
    "collaborativefund.com", "www.collaborativefund.com",  # Morgan Housel essays
    "ofdollarsanddata.com", "www.ofdollarsanddata.com",  # Nick Maggiulli
    "awealthofcommonsense.com", "www.awealthofcommonsense.com",  # Ben Carlson
    "ritholtz.com", "www.ritholtz.com",                  # Barry Ritholtz
    "humbledollar.com", "www.humbledollar.com",          # Jonathan Clements
    "abnormalreturns.com", "www.abnormalreturns.com",    # Tadas Viskanta
    "jasonzweig.com", "www.jasonzweig.com",              # Jason Zweig (WSJ Intelligent Investor)
    "earlyretirementnow.com", "www.earlyretirementnow.com",  # ERN — SWR series 权威
    "www.mrmoneymustache.com", "mrmoneymustache.com",    # MMM — FIRE
    # Iter 33 (poker-strategy): poker figures' OWN long-form sites — the
    # author/figure speaking for themselves (parallel to lexfridman.com /
    # karpathy.ai already above). Genuine first-hand, not vendor marketing.
    # Generic for any future poker / competitive-games skill.
    "www.tommyangelo.com", "tommyangelo.com",            # Tommy Angelo — Elements of Poker / tilt
    "jaredtendler.com", "www.jaredtendler.com",          # Jared Tendler — Mental Game of Poker
    "www.thinkingpoker.net", "thinkingpoker.net",        # Andrew Brokos — Thinking Poker / Play Optimal Poker
    "www.philgalfond.com", "philgalfond.com",            # Phil Galfond — Run It Once founder, 个人长文
    "noambrown.github.io",                                # Noam Brown — Libratus/Pluribus 作者学术主页
    "jonathanlittlepoker.com", "www.jonathanlittlepoker.com",  # Jonathan Little — PokerCoaching 创始人
    # Iter 36 (enterprise-b2b-sales): B2B-sales figures' OWN long-form sites —
    # the author/figure speaking for themselves (parallel to lexfridman.com /
    # caseinterview.com already above). Genuine first-hand practitioner canon.
    "salesgravy.com", "www.salesgravy.com",              # Jeb Blount — Fanatical Prospecting / Sales EQ
    "salesgrowth.com", "www.salesgrowth.com",            # Keenan — A Sales Growth Company / Gap Selling
    "thesalesblog.com", "www.thesalesblog.com",          # Anthony Iannarino — The Lost Art of Closing / Eat Their Lunch
    "iannarino.com", "www.iannarino.com",                # Anthony Iannarino — personal
    "joshbraun.com", "www.joshbraun.com",                # Josh Braun — modern prospecting / objection handling
    "blackswanltd.com", "www.blackswanltd.com",          # Chris Voss — The Black Swan Group (Never Split the Difference)
    "jbarrows.com", "www.jbarrows.com",                  # John Barrows — JB Sales training (driving-to-close canon)
    "saleshood.com", "www.saleshood.com",                # Elay Cohen — sales enablement (ex-Salesforce)
    "flipthescript.com", "www.flipthescript.com",        # Becc Holland — Flip the Script founder, modern prospecting
    "podcast.jbarrows.com",                              # John Barrows — Make It Happen Mondays podcast (subdomain of whitelisted jbarrows.com)
    # Iter 38 (zhihu AI creator): zh-CN AI 写作/研究 figure first-party blogs &
    # personal sites. Generic for any zh-CN AI / writing / research skill.
    "kexue.fm",                                          # 苏剑林 科学空间 (RoPE 发明人; /feed 全文)
    "hzwer.com",                                         # hzwer 黄哲威 个人站
    "dingxiaohan.xyz",                                   # 丁霄汉 个人站 (RepVGG/RepLKNet 一作)
    "wwxfromtju.github.io",                              # 王小惟 个人站 (RL4LLM)
    "lijigang.com",                                      # 李继刚 个人博客 (prompt 方法论)
    "yangzhiping.com", "www.yangzhiping.com",            # 阳志平 (认知写作学 / 开智)
    "huasheng.ai", "www.huasheng.ai",                    # 花叔 Alchain (女娲/huashu-design)
    # Iter 39 (music-production): audio-engineering figures'/educators' OWN sites
    # — the author/figure speaking for themselves (parallel to lexfridman.com).
    # Genuine first-hand canon. Generic for any future audio / mixing skill.
    "cambridge-mt.com", "www.cambridge-mt.com",          # Mike Senior — Mixing Secrets / free multitracks
    "www.digido.com", "digido.com",                       # Bob Katz — Digital Domain Mastering / K-system
    "productionadvice.co.uk", "www.productionadvice.co.uk",  # Ian Shepherd — loudness/Dynamic Range Day
    "recordingrevolution.com", "www.recordingrevolution.com",  # Graham Cochrane — bedroom mixing
    "theproaudiofiles.com", "www.theproaudiofiles.com",  # The Pro Audio Files — engineer-authored tutorials
    "pensadosplace.tv", "www.pensadosplace.tv",          # Dave Pensado — Pensado's Place
    "www.gearspace.com", "gearspace.com",                # Gearspace (ex-Gearslutz) — pro-engineer forum (practitioner primary)
    # Iter (investment-banking-mna): Aswath Damodaran's own blog — the valuation
    # originator speaking long-form (NYU stern page already covered by .edu suffix).
    "aswathdamodaran.blogspot.com",
    # Iter (product-ux-design): UX/design figures' & authors' OWN long-form sites /
    # official book sites — the figure/author speaking for themselves (parallel to
    # lexfridman.com / cambridge-mt.com). Genuine first-hand canon. Generic for any
    # future design / UX / product-design skill.
    "jnd.org", "www.jnd.org",                           # Don Norman — 个人站
    "www.jakobnielsenphd.com", "jakobnielsenphd.com",   # Jakob Nielsen — 个人站 (NN/g 已在 EXACT)
    "sensible.com", "www.sensible.com",                 # Steve Krug — Advanced Common Sense / DMMT
    "www.svpg.com", "svpg.com",                         # Marty Cagan — Silicon Valley Product Group
    "www.producttalk.org", "producttalk.org",           # Teresa Torres — Continuous Discovery / Product Talk
    "www.thesprintbook.com", "thesprintbook.com",       # Jake Knapp — Sprint 官方书站
    "atomicdesign.bradfrost.com", "bradfrost.com", "www.bradfrost.com",  # Brad Frost — Atomic Design
    "www.lukew.com", "lukew.com",                       # Luke Wroblewski — LukeW / Mobile First
    "www.deceptive.design", "deceptive.design",         # Harry Brignull — deceptive/dark patterns originator
    "mule.design", "www.mule.design", "www.mulebook.com", "mulebook.com",  # Erika Hall — Mule Design / Just Enough Research
    "leanuxbook.com", "www.leanuxbook.com",             # Jeff Gothelf — Lean UX 官方书站
    "lawsofux.com", "www.lawsofux.com",                 # Jon Yablonski — Laws of UX
    "maeda.pm", "www.maeda.pm",                         # John Maeda — 个人站
    "kimgoodwin.com", "www.kimgoodwin.com",             # Kim Goodwin — Designing for the Digital Age
    "refactoringui.com", "www.refactoringui.com",       # Wathan & Schoger — Refactoring UI 官方书站
    "articles.uie.com", "uie.com", "www.uie.com",       # Jared Spool — User Interface Engineering
    "measuringu.com", "www.measuringu.com",             # Jeff Sauro — MeasuringU (SUS/quant UX research originator)
    "designbetterpodcast.com", "www.designbetterpodcast.com",  # Design Better — 一手 show 自家站
    # iter (aigc-creative-workflow 2026-06-22): figure's OWN academic/personal page —
    # Lvmin Zhang (ControlNet/Fooocus/IC-Light author) self-hosted homepage on github.io.
    "lllyasviel.github.io",                             # 张吕敏 Lvmin Zhang 本人学术主页 (ControlNet 作者)
}

# Substack / Beehiiv-hosted newsletters: primary IF subdomain looks like an
# author/publication name (i.e., not "www" / "help" / "discover").
NEWSLETTER_HOSTS: tuple[str, ...] = (
    "substack.com",
    "beehiiv.com",
    "ghost.io",
    "convertkit.com",
)

# zh-CN newsletter / podcast platforms (channel listings allowed; reference
# for individual posts).
ZH_NEWSLETTER_HOSTS: set[str] = {
    "xiaoyuzhoufm.com",  # 小宇宙
    "www.xiaoyuzhoufm.com",
    "podcasts.apple.com",
    "open.spotify.com",
    "music.apple.com",
}

# Repo / code hosts: github.com/{org}/{repo} root → primary. github.com/{...}/issues/N → reference.
REPO_HOSTS: set[str] = {
    "github.com",
    "gitlab.com",
    "bitbucket.org",
    "codeberg.org",
    "gitee.com",
}

# ---------------------------------------------------------------------------
# Blacklists (locale-specific)
# ---------------------------------------------------------------------------

BLACKLIST_ZH_EXACT: set[str] = {
    "www.zhihu.com",
    "zhihu.com",
    "zhuanlan.zhihu.com",
    "baike.baidu.com",
    "wenku.baidu.com",
    "jingyan.baidu.com",
    "blog.csdn.net",
    "www.csdn.net",
    "blog.51cto.com",
    "www.cnblogs.com",
    "www.jianshu.com",
    "juejin.cn",  # 掘金 — 部分原创但 SEO 农场化
    "developer.aliyun.com",  # 阿里云开发者社区 — 多为厂商 PR
    "tencent.cloud.com",
}

# 公众号 mp.weixin.qq.com: blacklisted as evidence (cannot cite content),
# but the WeChat *channel* itself is allowed in Track 05 source listings.
# We classify URL = blacklisted; agents that maintain Track 05 channel lists
# should override / annotate via meta when the URL is the channel root.
BLACKLIST_ZH_PATTERNS: tuple[str, ...] = (
    "mp.weixin.qq.com",  # 微信公众号文章
)

BLACKLIST_EN_EXACT: set[str] = {
    "www.g2.com",
    "g2.com",
    "www.capterra.com",
    "capterra.com",
    "www.gartner.com",
    "www.forrester.com",
    "www.softwareadvice.com",
    "www.trustradius.com",
    "www.businesswire.com",  # PR newswire
    "www.prnewswire.com",
    "www.globenewswire.com",
    "www.einnews.com",
}

# Medium / dev.to: hard to classify without author check. We mark as
# secondary by default; classify path /@{author}/ as secondary; specific
# known SEO-farm subdomains as blacklisted.
MEDIUM_FARM_SUBDOMAINS: set[str] = {
    "javascript.plainenglish.io",
    "betterprogramming.pub",
    "levelup.gitconnected.com",
}

# Reference-tier: forum / Q&A / aggregator hosts where typical URL is a single
# answer / comment / thread, not authoritative.
REFERENCE_DOMAINS: set[str] = {
    "stackoverflow.com",
    "superuser.com",
    "serverfault.com",
    "askubuntu.com",
    "stackexchange.com",
    "news.ycombinator.com",
    "www.reddit.com",
    "old.reddit.com",
    "twitter.com",
    "x.com",
    "mobile.twitter.com",
    "t.co",
    "v2ex.com",
    "tieba.baidu.com",
    "www.douban.com",
    "movie.douban.com",
}

SECONDARY_DOMAINS_EXACT: set[str] = {
    "en.wikipedia.org",
    "zh.wikipedia.org",
    "www.wikipedia.org",
    "en.wiktionary.org",
    "techcrunch.com",
    "www.theverge.com",
    "www.wired.com",
    "www.economist.com",
    "www.bloomberg.com",
    "www.ft.com",
    "www.nytimes.com",
    "www.wsj.com",
    "www.36kr.com",  # 36 氪 — 二手分析
    "36kr.com",
    "www.geekpark.net",
    "www.huxiu.com",
    "www.latepost.com",
    "www.caixin.com",
    "tech.sina.com.cn",
    "tech.qq.com",
    "tech.163.com",
    "www.ithome.com",
    "www.leiphone.com",
    "www.jiqizhixin.com",  # 机器之心 — 偏二手
    "medium.com",
    "dev.to",
    "hacker-news.firebaseapp.com",
}

# Canonical entity-reference hosts: pages of the form /subject/X, /album/Y,
# /book/Z, /podcast/N — these are the authoritative landing for a real-world
# entity (a book, a podcast, an album). Agents reasonably cite them as the
# primary URL for the entity even if the host itself isn't an "official source"
# in the traditional sense. Treated as verified_primary when path matches.
ENTITY_REFERENCE_HOSTS: dict[str, frozenset[str]] = {
    "book.douban.com": frozenset({"subject"}),
    "movie.douban.com": frozenset({"subject"}),
    "music.douban.com": frozenset({"subject"}),
    "www.douban.com": frozenset({"subject", "book", "movie", "music"}),
    "weread.qq.com": frozenset({"web", "bookDetail"}),  # 微信读书 book pages
    "www.ximalaya.com": frozenset({"album", "sound", "track"}),
    "ximalaya.com": frozenset({"album", "sound"}),
    "www.lizhi.fm": frozenset({"podcast"}),
    "www.acast.com": frozenset({"show"}),
    "podcasts.google.com": frozenset({"feed"}),
    "open.spotify.com": frozenset({"show", "episode"}),
}

# ---------------------------------------------------------------------------
# Core classifier
# ---------------------------------------------------------------------------


def _norm_host(url: str) -> tuple[str, str]:
    """Return (host, path) lowercased; strip default port + leading www only
    when host has no further label. e.g., www.foo.com stays as-is for matching
    in tables that include `www.`. Path is left urlencoded."""
    parsed = urllib.parse.urlsplit(url.strip())
    host = (parsed.hostname or "").lower()
    path = parsed.path or ""
    return host, path


def classify_url(url: str, locale: str = "all") -> tuple[str, str]:
    """Classify a single URL. Return (bucket, reason).

    locale:
      "all"   apply both zh-CN + en blacklists (default; safe over-rejecting)
      "zh-CN" zh-CN blacklist only
      "en"    en blacklist only
      "ja"/"ko"/... fall through to "all" (placeholder for future expansion)
    """
    if not url or not url.strip():
        return Secondary, "empty url"
    if not re.match(r"^https?://", url, re.IGNORECASE):
        return Reference, "non-http url (file? mailto?)"
    host, path = _norm_host(url)
    if not host:
        return Secondary, "no host parsed"

    # 1) Blacklists first — locale-narrow if asked, else apply both.
    apply_zh = locale in ("all", "zh-CN")
    apply_en = locale in ("all", "en")
    if apply_zh:
        if host in BLACKLIST_ZH_EXACT:
            return Blacklisted, f"zh-CN blacklist domain: {host}"
        for pat in BLACKLIST_ZH_PATTERNS:
            if pat in host:
                return Blacklisted, f"zh-CN blacklist pattern: {pat}"
    if apply_en:
        if host in BLACKLIST_EN_EXACT:
            return Blacklisted, f"en blacklist domain: {host}"
        if host in MEDIUM_FARM_SUBDOMAINS:
            return Blacklisted, f"en SEO-farm subdomain: {host}"

    # 2) Verified primary — explicit domain match.
    if host in PRIMARY_DOMAINS_EXACT:
        return VerifiedPrimary, f"primary domain (exact): {host}"
    for suffix in PRIMARY_DOMAIN_SUFFIXES:
        if host == suffix.lstrip(".") or host.endswith(suffix):
            return VerifiedPrimary, f"primary domain (suffix): {suffix}"
    if host in PRIMARY_PERSONAL_DOMAINS:
        return VerifiedPrimary, f"known personal/author primary: {host}"

    # 3) Repo hosts — root path / docs / releases → primary; issues/PRs → reference.
    if host in REPO_HOSTS:
        # github.com/{org}/{repo}     → primary (project root)
        # github.com/{org}/{repo}/...
        # github.com/{org}/{repo}/(issues|pull|discussions)/N → reference
        seg = [s for s in path.strip("/").split("/") if s]
        if len(seg) >= 3 and seg[2] in ("issues", "pull", "discussions"):
            return Reference, f"{host} thread/comment, not project root"
        if len(seg) >= 2:
            return VerifiedPrimary, f"{host} project root"
        return Secondary, f"{host} top-level / org page"

    # 4) Newsletter hosts (Substack/Beehiiv/Ghost/ConvertKit).
    for nh in NEWSLETTER_HOSTS:
        if host.endswith(nh):
            sub = host[: -len(nh)].rstrip(".")
            # Bare host (e.g. substack.com) → secondary marketing
            if not sub or sub.lower() in {"www", "help", "discover", "about"}:
                return Secondary, f"{host} root/marketing page"
            return VerifiedPrimary, f"newsletter author host: {sub}.{nh}"

    # 5) zh-CN podcast / 小宇宙 / Apple / Spotify — channel pages are primary,
    # episode play pages reference (single play vs the channel as a tracked source).
    if host in ZH_NEWSLETTER_HOSTS:
        seg_all = [s.lower() for s in path.strip("/").split("/") if s]
        if "episode" in seg_all:
            return Reference, f"{host} single episode link"
        if any(s in seg_all for s in ("podcast", "podcasts")):
            return VerifiedPrimary, f"{host} podcast channel"
        return Secondary, f"{host} unspecified path"

    # 6) Reference-tier hosts (forums / Q&A / aggregators / single tweets).
    if host in REFERENCE_DOMAINS:
        return Reference, f"forum/Q&A/aggregator: {host}"

    # 7) Wikipedia / general tech news → secondary.
    if host in SECONDARY_DOMAINS_EXACT:
        return Secondary, f"known secondary domain: {host}"

    # 7.5) Canonical entity-reference hosts (douban /subject, ximalaya /album, ...)
    # These hosts have authoritative pages for real-world entities (books, podcasts,
    # albums). Agents reasonably treat the entity-page URL as the primary citation.
    if host in ENTITY_REFERENCE_HOSTS:
        seg = [s for s in path.strip("/").split("/") if s]
        if seg and seg[0].lower() in ENTITY_REFERENCE_HOSTS[host]:
            return VerifiedPrimary, f"canonical entity reference: {host}/{seg[0]}/{seg[1] if len(seg) > 1 else ''}"
        return Secondary, f"{host} non-entity path"

    # Podcast platform fallthrough (xyzfm.space hosts independent podcasts via feeds)
    if host == "feed.xyzfm.space" or host.endswith(".xyzfm.space"):
        return VerifiedPrimary, "xyzfm podcast feed root"

    # 8) Heuristic: subdomain "blog.{company}" / "engineering.{company}" /
    # "research.{company}" / "tech.{company}" — primary when company has its
    # own .com / .io / .ai domain. Captures "blog.replit.com" etc that aren't
    # in the static list.
    if re.match(r"^(blog|engineering|research|labs?|tech|developers?|docs)\.", host):
        return VerifiedPrimary, f"engineering/blog subdomain heuristic: {host}"

    # 9) YouTube channel paths.
    if host in ("www.youtube.com", "youtube.com", "m.youtube.com"):
        seg = [s for s in path.strip("/").split("/") if s]
        if seg and (seg[0] in ("c", "channel", "user") or seg[0].startswith("@")):
            return VerifiedPrimary, f"youtube channel root: /{seg[0]}"
        return Reference, "youtube generic page"

    # 9.5) Bilibili (zh-CN creator video platform). iter30: a creator's space or
    # uploaded video/column is first-party creator content (parallel to a youtube
    # channel) — primary for "what this creator said/made"; other pages reference.
    if host in ("www.bilibili.com", "bilibili.com", "m.bilibili.com", "space.bilibili.com"):
        if host == "space.bilibili.com":
            return VerifiedPrimary, "bilibili creator space"
        seg = [s for s in path.strip("/").split("/") if s]
        if seg and seg[0].lower() in ("video", "read", "opus", "medialist"):
            return VerifiedPrimary, "bilibili creator content"
        return Reference, "bilibili generic page"

    # 10) Content-publishing path on an unknown domain.
    # Conservative rule (iter 25 — codex P0 audit): only paths that are
    # *unambiguous* content publishing (`/podcast`, `/blog`, `/post`, `/author`,
    # `/events`, `/newsletter`) on a not-yet-seen domain are promoted to
    # verified_primary. Bare-host roots (`https://example.com/`) and
    # generic-slug articles (`https://random.com/some-cool-article`) used
    # to also be auto-promoted, which made `verified_primary` rubber-stamp
    # SEO-farm reposts. Default for those is now `secondary` — promote them
    # by adding the host to PRIMARY_DOMAINS_EXACT or PRIMARY_PERSONAL_DOMAINS
    # (allowlist), or by writing the manifest entry by hand with a reason.
    seg = [s for s in path.strip("/").split("/") if s]
    content_segments = {
        "podcast", "podcasts", "episodes", "episode",
        "blog", "blogs", "post", "posts",
        "author", "authors", "writers",
        "events", "event", "newsletter", "newsletters",
        "research", "papers", "case-studies", "casestudies",
        "talks", "writing", "essays", "notes",
        # Iter 26: corporate "about" / "team" / "leadership" pages — authoritative
        # description of the entity itself (vendor / agency / partner).
        "about", "team", "leadership", "officers",
        "products",  # vendor product pages — primary for THAT product (not generic admin)
    }
    admin_segments = {
        # iter 26: removed "products"/"product" — vendor product pages are
        # authoritative descriptions of the vendor's own product (helium10/podcast,
        # dt.com.cn/baoxianjia). Primary, not admin.
        "pricing", "buy", "shop", "cart",
        "login", "signup", "signin", "support", "help",
        "privacy", "terms", "legal",
        "contact", "careers", "jobs",
    }
    if seg:
        if seg[0].lower() in admin_segments:
            return Secondary, f"brand-domain admin path: /{seg[0]}"
        if any(s.lower() in content_segments for s in seg):
            return VerifiedPrimary, f"brand-domain content path: /{seg[0]}"

    # 11) Default: secondary. Primary requires either an allowlisted domain,
    # the engineering/blog subdomain heuristic, the YouTube/Apple-Podcast
    # channel heuristic, or an explicit content path (handled above). Bare
    # hosts and slug-style article URLs are *not* enough by themselves —
    # they need a manual manifest entry with a reason.
    return Secondary, f"unknown host (default secondary): {host}"


# ---------------------------------------------------------------------------
# Liveness check (optional, slow)
# ---------------------------------------------------------------------------


def check_liveness(url: str, timeout: float = 5.0) -> tuple[bool, int | None, str]:
    """HEAD the URL; return (alive, status_code, reason). Treats 4xx/5xx as
    dead, 2xx/3xx as alive. Falls back to GET (range bytes=0-0) if the host
    rejects HEAD with 405."""
    try:
        req = urllib.request.Request(
            url,
            method="HEAD",
            headers={"User-Agent": "master-skill-source-verifier/1.0"},
        )
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            code = resp.status
            return (200 <= code < 400), code, f"HEAD {code}"
    except urllib.error.HTTPError as e:
        if e.code == 405:
            # HEAD not allowed; try GET with byte range so we don't pull body
            try:
                req = urllib.request.Request(
                    url,
                    headers={
                        "User-Agent": "master-skill-source-verifier/1.0",
                        "Range": "bytes=0-0",
                    },
                )
                with urllib.request.urlopen(req, timeout=timeout) as resp:
                    code = resp.status
                    return (200 <= code < 400), code, f"GET-range {code}"
            except Exception as e2:
                return False, getattr(e2, "code", None), f"GET-range failed: {type(e2).__name__}"
        return False, e.code, f"HTTP {e.code}"
    except urllib.error.URLError as e:
        return False, None, f"URLError: {e.reason}"
    except Exception as e:
        return False, None, f"{type(e).__name__}: {e}"


# ---------------------------------------------------------------------------
# Batch scan
# ---------------------------------------------------------------------------

# Pull every http(s) URL out of markdown — covers `[text](url)`, `<url>`, and
# bare `https://...` forms. Trailing punctuation is stripped.
URL_RE = re.compile(r"https?://[^\s<>\)\]'\"`]+", re.IGNORECASE)


def extract_urls(text: str) -> list[str]:
    raw = URL_RE.findall(text)
    out: list[str] = []
    seen: set[str] = set()
    for u in raw:
        u = u.rstrip(".,;:!?'\")")
        if u and u not in seen:
            seen.add(u)
            out.append(u)
    return out


def scan_dir(
    research_dir: Path,
    locale: str = "all",
    check_live: bool = False,
) -> dict[str, Any]:
    """Walk *.md under research_dir, classify every URL, return aggregate dict."""
    if not research_dir.exists():
        raise FileNotFoundError(f"research dir not found: {research_dir}")
    files = sorted(research_dir.rglob("*.md"))
    by_url: dict[str, dict[str, Any]] = {}
    counts: dict[str, int] = {b: 0 for b in EXIT_CODES.keys()}
    counts.setdefault("dead", 0)
    for f in files:
        try:
            text = f.read_text(encoding="utf-8")
        except OSError:
            continue
        for u in extract_urls(text):
            if u in by_url:
                # Already classified; just record file
                by_url[u]["files"].append(str(f.relative_to(research_dir)))
                continue
            bucket, reason = classify_url(u, locale=locale)
            entry: dict[str, Any] = {
                "bucket": bucket,
                "reason": reason,
                "files": [str(f.relative_to(research_dir))],
            }
            if check_live and bucket != Blacklisted:
                alive, code, lreason = check_liveness(u)
                entry["live"] = alive
                entry["http_status"] = code
                entry["live_reason"] = lreason
                if not alive:
                    entry["bucket"] = Dead
                    entry["reason"] = f"liveness: {lreason}"
                    bucket = Dead
            counts[bucket] = counts.get(bucket, 0) + 1
            by_url[u] = entry
    total = sum(counts.values())
    primary_ratio = counts.get(VerifiedPrimary, 0) / total if total else 0.0
    return {
        "research_dir": str(research_dir),
        "locale": locale,
        "total_urls": total,
        "counts": counts,
        "verified_primary_ratio": round(primary_ratio, 4),
        "urls": by_url,
    }


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------


def cmd_classify(args: argparse.Namespace) -> int:
    bucket, reason = classify_url(args.url, locale=args.locale)
    if args.json:
        print(json.dumps({"url": args.url, "bucket": bucket, "reason": reason}))
    else:
        print(f"{bucket}\t{reason}\t{args.url}")
    if args.check_liveness and bucket != Blacklisted:
        alive, code, lreason = check_liveness(args.url)
        print(f"liveness: alive={alive} status={code} reason={lreason}", file=sys.stderr)
        if not alive:
            return EXIT_CODES[Dead]
    return EXIT_CODES.get(bucket, 1)


def cmd_scan(args: argparse.Namespace) -> int:
    report = scan_dir(args.research_dir, locale=args.locale, check_live=args.check_liveness)
    out: str
    if args.json:
        out = json.dumps(report, indent=2, ensure_ascii=False)
    else:
        out_lines: list[str] = [
            f"# source_verifier scan — {report['research_dir']}",
            "",
            f"locale: `{report['locale']}`  total: {report['total_urls']}",
            "",
            "counts:",
        ]
        for k, v in report["counts"].items():
            out_lines.append(f"  - {k}: {v}")
        out_lines.append("")
        out_lines.append(
            f"verified_primary_ratio: {report['verified_primary_ratio'] * 100:.1f}%"
        )
        out_lines.append("")
        out_lines.append("| bucket | url | reason |")
        out_lines.append("|--------|-----|--------|")
        for u, info in sorted(report["urls"].items(), key=lambda kv: kv[1]["bucket"]):
            out_lines.append(f"| {info['bucket']} | {u} | {info['reason']} |")
        out = "\n".join(out_lines)

    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(out, encoding="utf-8")
        print(f"wrote {args.output}", file=sys.stderr)
    else:
        print(out)

    # exit non-zero on hard violations:
    #   3 — at least one blacklisted source detected
    #   4 — at least one dead source detected (only meaningful with --check-liveness)
    #   1 — primary ratio under 0.5
    # Blacklist takes priority over dead because it's a content quality issue,
    # dead is fixable by URL update.
    if report["counts"].get(Blacklisted, 0) > 0:
        return 3
    if report["counts"].get(Dead, 0) > 0:
        return 4
    if report["verified_primary_ratio"] < 0.5:
        return 1
    return 0


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        description="source_verifier — classify URLs into 5 buckets for Phase 4 quality gate"
    )
    sub = p.add_subparsers(dest="action", required=True)

    pc = sub.add_parser("classify", help="classify a single URL")
    pc.add_argument("url")
    pc.add_argument("--locale", default="all", choices=["all", "zh-CN", "en", "ja", "ko"])
    pc.add_argument("--check-liveness", action="store_true",
                    help="HEAD the URL; flag dead links")
    pc.add_argument("--json", action="store_true")

    ps = sub.add_parser("scan", help="scan a research directory of markdown files")
    ps.add_argument("--research-dir", required=True, type=Path)
    ps.add_argument("--locale", default="all", choices=["all", "zh-CN", "en", "ja", "ko"])
    ps.add_argument("--check-liveness", action="store_true")
    ps.add_argument("--output", type=Path,
                    help="write scan report here (markdown or JSON per --json)")
    ps.add_argument("--json", action="store_true")

    return p


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    if args.action == "classify":
        return cmd_classify(args)
    if args.action == "scan":
        return cmd_scan(args)
    return 99


if __name__ == "__main__":
    sys.exit(main())
