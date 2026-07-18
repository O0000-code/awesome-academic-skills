<div align="right">

[English](README.md) · **中文**

</div>

<div align="center">

# Awesome Academic Skills [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

<br/>

**把科研全流程，做成 agent 技能。**
<br/>
一个双语的 Claude 与 agent 技能索引，覆盖从文献检索到同行评审的学术工作。<br/>
按技能在研究流程中的位置来组织；每个条目都标注许可证，以及它会做什么（联网、hook）。
<br/>

![Skills](https://img.shields.io/badge/skills-223-000?style=flat-square)
![Categories](https://img.shields.io/badge/categories-14-000?style=flat-square)
![Updated](https://img.shields.io/badge/updated-2026.07.18-000?style=flat-square)
![License](https://img.shields.io/badge/license-CC0--1.0-000?style=flat-square)

</div>

<br/>

## 目录

- [检索与采集](#检索与采集)
  - [文献检索与发现](#文献检索与发现)
  - [参考文献与引用管理](#参考文献与引用管理)
- [阅读与理解](#阅读与理解)
  - [阅读、摘要与问答](#阅读摘要与问答)
  - [PDF / OCR / 文档解析](#pdf--ocr--文档解析)
- [分析与可视化](#分析与可视化)
  - [数据分析与统计](#数据分析与统计)
  - [图表与可视化](#图表与可视化)
- [写作与润色](#写作与润色)
  - [学术写作与起草](#学术写作与起草)
  - [写作质量与去 AI 味](#写作质量与去-ai-味)
- [评审与发表](#评审与发表)
  - [同行评审与回应](#同行评审与回应)
  - [投稿、格式与转换](#投稿格式与转换)
- [套件、系统与生态](#套件系统与生态)
  - [技能套件](#技能套件)
  - [自主研究系统](#自主研究系统)
  - [学科专用包](#学科专用包)
  - [精选列表与生态导览](#精选列表与生态导览)
- [速览](#速览)
- [最近更新](#最近更新)
- [如何使用本列表](#如何使用本列表)
- [收录标准](#收录标准)
- [策展、中立性与安全](#策展中立性与安全)

## 检索与采集

> 检索、界定并汇集文献——再把参考文献理清楚。

### 文献检索与发现

> 检索、界定并汇集文献——多源检索、引文网络，以及把一个题目变成一份阅读清单的发现型 agent。

#### 多源检索发现

- `Suite` [arxiv-skills](https://github.com/ultimatile/arxiv-skills) - 作者 [ultimatile](https://github.com/ultimatile) · `MIT` · `net`.<br>一对 arXiv skill：把论文（优先 LaTeX 源、PDF 兜底）转换为可直接用于实现的 Markdown 并保留数学公式，外加一个轻量的 arXiv API DOI/标题检索查询。转换质量取决于 pandoc。
- `Suite` [cnki-skills](https://github.com/cookjohn/cnki-skills) - 作者 [cookjohn](https://github.com/cookjohn) · `No License` · `net`.<br>在 Claude Code 中经由 Chrome DevTools MCP 驱动 CNKI（中国主要学术数据库）：检索、期刊浏览、引文分析、PDF 下载，以及 BibTeX/Zotero 导出。中文文献工作的首选；需要配置 browser MCP，且未附 LICENSE。
- `Suite` [gs-skills](https://github.com/cookjohn/gs-skills) - 作者 [cookjohn](https://github.com/cookjohn) · `MIT` · `net`.<br>一套真正实用的命令行 Google Scholar 工具箱：关键词/高级检索、引用链追踪、全文链接解析与一键 Zotero 导出。依赖 Chrome DevTools MCP 并抓取 DOM，因此 Scholar 一改版就可能失效。
- `Suite` [scientific-skills](https://github.com/yorkeccak/scientific-skills) - 作者 [yorkeccak](https://github.com/yorkeccak) · `MIT` · `net`.<br>借助 Valyu 语义检索，在 13 个数据源（PubMed、arXiv、bioRxiv/medRxiv、ChEMBL、DrugBank、Open Targets、临床试验、专利）上进行自然语言文献检索。生物医学/药物发现的覆盖很强；依赖 Valyu API，并非自包含。
- [ai-skill-scholar](https://github.com/dsebastien/ai-skill-scholar) - 作者 [Sébastien Dubois (dsebastien)](https://github.com/dsebastien) · `MIT` · `net`.<br>三个可组合的 OpenAlex 技能（会议检索、引用图游走、综述编排）——纯标准库，免 pip、免 key。
- [asta-skill](https://github.com/agents365-ai/asta-skill) - 作者 [agents365-ai](https://github.com/agents365-ai) · `MIT`.<br>驱动 Ai2 旗下 Asta MCP（Semantic Scholar）的指令包式 skill：支持关键词/ID/作者检索、引文追溯、批量查询与约 500 词的片段抓取，并配有稳妥的默认设置。路由清晰；需要 Asta MCP 与一个免费 API key。
- [paper-search-pro](https://github.com/O0000-code/paper-search-pro) - 作者 [O0000-code](https://github.com/O0000-code) · `Apache-2.0` · `net`.<br>以 OpenAlex 为主轴的五源检索（PubMed、arXiv、Semantic Scholar、CrossRef），分四档深度；不止给命中清单，还产出饱和度曲线、停检判定与可交互 HTML 报告。免 LLM key，一个免费 OpenAlex key 即可起步。
- [scholar-kit](https://github.com/lottshin/scholar-kit) - 作者 [lottshin](https://github.com/lottshin) · `MIT` · `net`.<br>以中文为先的文献工具包：检索知网/OpenAlex/Semantic Scholar/arXiv/国家哲学社会科学文献中心，用 Crossref 补全元数据，经 Unpaywall 解析 OA 版本，批量下载（含知网 PDF），导出 GB/T 7714/BibTeX/RIS/APA。知网支持出色；但抓取较脆弱且涉及 ToS 风险。
- [semanticscholar-skill](https://github.com/agents365-ai/semanticscholar-skill) - 作者 [agents365-ai](https://github.com/agents365-ai) · `MIT` · `net`.<br>封装 Semantic Scholar Graph API，可在 2 亿多篇论文中做论文检索、引用图遍历与作者查询，并为多 agent 使用做了限速。是可靠的检索基础组件；刻意做得很窄（仅 S2），宜与其他工具搭配使用。

#### 系统综述与深度检索流程

- `Suite` [literature-review-skill](https://github.com/yanzhanlin/literature-review-skill) - 作者 [yanzhanlin](https://github.com/yanzhanlin) · `MIT`.<br>一套端到端的文献综述套件（检索、获取、精读、写作、学位论文章节），构建于 PRISMA-S、PICO/SPIDER 及具名的综述方法学框架之上。方法依据扎实，检索日志可复现；以中文为先，star 数一般。
- [litreviewskill](https://github.com/zsun79/litreviewskill) - 作者 [zsun79](https://github.com/zsun79) · `No License` · `net`.<br>端到端的文献综述工作流：拟定关键词，构建 OpenAlex 种子集，通过前向/后向引用扩展，按标题/摘要筛选直至饱和，再排序并通读至多 30 篇全文，整理成概念矩阵。流程严谨。
- [oneshot-academic-research-skill](https://github.com/orhoncan/oneshot-academic-research-skill) - 作者 [orhoncan](https://github.com/orhoncan) · `MIT`.<br>迭代式深度文献研究 skill：用 5-15 轮检索汇集 12-50+ 篇文献，附带空白识别、来源多样性追踪与 APA7 脚注，可导出到 Obsidian 或 PDF。自动识别土耳其语/英语；深度取决于底层的 web 检索工具。
- [scholar-deep-research](https://github.com/agents365-ai/scholar-deep-research) - 作者 [agents365-ai](https://github.com/agents365-ai) · `MIT` · `net`.<br>脚本驱动的 8 阶段文献综述 pipeline，覆盖 7 个联合来源，强制引用锚定、去重、透明排序、引文追溯，并设有一道必经的自我批判关卡。

#### 全文获取

- [literature-harvest](https://github.com/zhongzhx/literature-harvest) - 作者 [zhongzhx](https://github.com/zhongzhx) · `MIT` · `net`.<br>跨 PubMed、Europe PMC、Crossref 和 OpenAlex 的关键词批量文献采集：构建候选清单，下载合法可获取的全文 PDF（并以 HTML 转 PDF 作为兜底补充），并做去重。适合可复现的语料库构建。
- [paper-fetch](https://github.com/agents365-ai/paper-fetch) - 作者 [agents365-ai](https://github.com/agents365-ai) · `MIT` · `net`.<br>通过一条 7 源兜底链（Unpaywall、Semantic Scholar、arXiv、PMC、bioRxiv、出版商，最后才是 Sci-Hub）把一个（或一批）DOI 解析为可下载的 PDF，并逐源报告结果。干净、零依赖；Sci-Hub 兜底是一处需注意的隐患。

### 参考文献与引用管理

> 管理、规范并核验参考文献——文献库集成、引用样式，以及让参考文献表站得住脚的 DOI 与元数据核查。

#### 参考文献格式与样式

- [apa-referencing-skill](https://github.com/keemanxp/apa-referencing-skill) - 作者 [Chuah Kee Man (keemanxp)](https://github.com/keemanxp) · `No License` · `net`.<br>最完整的 APA 第 7 版格式化工具：28 种文献类型，细到推文和数据集。要注意：没有开源协议。
- [chinese-reference-formatter-skill](https://github.com/zechang-xiong/chinese-reference-formatter-skill) - 作者 [zechang-xiong](https://github.com/zechang-xiong) · `MIT`.<br>将中文学术参考文献格式化为 GB/T 7714 标准，并依据中英文标题补全 BibTeX 条目。填补了西方引用工具忽视的中文学者真实需求空白。定位本就专一；附带辅助脚本和一个 agent。

#### BibTeX / 元数据生成

- [citation-assistant](https://github.com/zhangny301/citation-assistant) - 作者 [zhangny301](https://github.com/zhangny301) · `No License` · `net`.<br>基于 Semantic Scholar API 的自动化学术引用 skill：解析、核验并将引用格式化嵌入稿件。实用、聚焦的引用助手；为单一 skill，受限于 S2 的覆盖范围，且其 license 仍待确认。
- [make-bib](https://github.com/milkclouds/make-bib) - 作者 [milkclouds](https://github.com/milkclouds) · `No License` · `net`.<br>带人工确认环节的 BibTeX 抓取器，每个字段都从权威出版方（ACL/PMLR/arXiv/NeurIPS，DBLP 兜底）取得，而非来自 LLM，逐条记录来源出处，遇到含混的 venue 会停下来询问。非常适合给 .bib 去幻觉；未附许可协议。
- [wenxian](https://github.com/njzjz/wenxian) - 作者 [njzjz](https://github.com/njzjz) · `LGPL-3.0` · `net`.<br>通过查询 CrossRef、PubMed、arXiv、Semantic Scholar 和 ChemRxiv，从 DOI、PMID、arXiv ID 或论文标题生成 BibTeX。成熟、经过测试、已发布到 PyPI；该 agent skill 是对一个扎实 CLI 的轻量封装。LGPL-3.0。

## 阅读与理解

> 把一堆 PDF 变成你真正读过、还能向其提问的东西。

### 阅读、摘要与问答

> 深读论文并向其提问——摘要、跨文献综合，以及在语料之上有据可循的问答。

#### 深读与理解

- `Suite` [dailypaper-skills](https://github.com/huangkiki/dailypaper-skills) - 作者 [huangkiki](https://github.com/huangkiki) · `Apache-2.0` · `net`.<br>由 Agent Skills 搭建的每日读论文流水线：arXiv 检索、PDF 解析、要点抽取、Zotero 同步，外加结构化笔记与每日摘要。整体连贯且受欢迎；文档以中文为主，非中日韩用户更多需依赖代码本身。
- `Suite` [scholar-skill](https://github.com/eesjgong/scholar-skill) - 作者 [eesjgong](https://github.com/eesjgong) · `MIT` · `net`.<br>以 Obsidian 为中心的学术阅读套件：深读论文，并借助反思式提示将其链接进一个不断演进的个人知识库。如果你常驻 Obsidian，这是个不错的选择；它做的是阅读与整理，而非发现论文。
- [benchmark-research-skill](https://github.com/eternalwavee/benchmark-research-skill) - 作者 [eternalwavee](https://github.com/eternalwavee) · `MIT` · `net`.<br>从论文中提取 benchmark、数据集、指标与 baseline，或调研哪些 benchmark 契合某个研究方向；优先用 arXiv 源、配 Obsidian 笔记。使用未加限定的 Bash(*) 白名单——shell 权限范围很宽。
- `Plugin` [claude-paper](https://github.com/alaliqing/claude-paper) - 作者 [alaliqing](https://github.com/alaliqing) · `MIT` · `net` `hooks`.<br>一个论文研读 plugin，把 PDF 或 arXiv 链接变成学习环境：解析文本、自适应摘要/问答、可运行的代码示例，以及一个 KaTeX 网页阅读器。功能丰富但偏重（依赖 Node/Nuxt/poppler）；使用了未加限定的 Bash 白名单。
- [deeppapernote](https://github.com/917dhj/deeppapernote) - 作者 [917dhj](https://github.com/917dhj) · `MIT` · `net`.<br>深读单篇论文，产出高质量、结构化的 Obsidian 风格研究笔记（论断、方法、要点），可在 Claude Code/Codex/Cursor 间通用。很适合搭建笔记库；一次只读一篇，不面向语料级规模。
- [paper-analyst](https://github.com/flyer-li/paper-analyst) - 作者 [flyer-li](https://github.com/flyer-li) · `MIT`.<br>以五种深度模式分析论文（从快速浏览到带图表的汇报），配有防幻觉的来源标注，并针对论文类型做相应的方法提取。擅长结构化阅读/摘要；为单个 skill，自身不接入外部数据源。
- [paper-reader-heilmeier](https://github.com/realzyzhang/paper-reader-heilmeier) - 作者 [realzyzhang](https://github.com/realzyzhang) · `MIT`.<br>以 Heilmeier 问题清单（Heilmeier's Catechism）的视角阅读 STEM 论文，提炼核心问题、方法、成本与影响，快速形成全局把握。一个聚焦而有主见的理解辅助工具；很适合对论文做初筛分流，但不擅长逐行深读。
- [paper-reading-skill](https://github.com/kingslayer-bot/paper-reading-skill) - 作者 [kingslayer-bot](https://github.com/kingslayer-bot) · `MIT`.<br>一个深度论文研读 skill，提供两种模式：段落级的细读配 agentic 问答，以及由并行 agent 执行的 20+ 维度分析，并输出可直接导入 Obsidian 的笔记。擅长拆解单篇论文；不是检索或引用工具。

#### 有据问答与知识库

- [Claude Deep Research Skill](https://github.com/199-biotechnologies/claude-deep-research-skill) - 作者 [199 Longevity (199-biotechnologies)](https://github.com/199-biotechnologies) · `No License` · `net`.<br>工程味最重的深度研究技能——逐条对 CrossRef 核验论断出处，让引用在上下文压缩后仍留存。没有协议文件。
- [Deep Research Skill](https://github.com/Weizhena/Deep-Research-skills) - 作者 [Lan Zheng](https://github.com/Weizhena) · `MIT` · `net`.<br>两段式深度研究，任何检索动手前先让你确认提纲——是对"一键放飞"型代理的人在环路制衡。
- `Plugin` [llm-wiki](https://github.com/nvk/llm-wiki) - 作者 [nvk](https://github.com/nvk) · `MIT` · `net`.<br>为 agent 构建 LLM 编译的知识库：并行多 agent 调研、论点驱动的探查、来源摄入，最终形成可查询的 wiki。适合从大量来源搭建持久、带引用的知识库，属于研究综合工具，而非文献检索工具。
- [NotebookLM Research Skill](https://github.com/claude-world/notebooklm-skill) - 作者 [Claude-World](https://github.com/claude-world) · `MIT` · `net`.<br>从 Claude 里驱动 Google NotebookLM，产出带引用的答案和免费产物（播客、思维导图、学习指南）。要注意：靠 cookie 的非官方客户端，随时可能失效。
- [notebooklm-skill](https://github.com/pleaseprompto/notebooklm-skill) - 作者 [pleaseprompto](https://github.com/pleaseprompto) · `MIT`.<br>把 Claude Code 接入 Google NotebookLM，让回答仅取自你上传的文档、有出处、附引用。在个人语料库上做有据 Q&A 表现出色；依赖一个 Google NotebookLM 账号和 notebooklm-mcp。

#### 论文翻译

- [arxiv-paper-zh](https://github.com/zeya-labs/arxiv-paper-zh) - 作者 [zeya-labs](https://github.com/zeya-labs) · `MIT` · `net`.<br>将 arXiv 的 LaTeX 论文翻译成中文，并保留格式——公式、图表与引用——可从 arXiv ID 或本地源文件读取。这种保留格式的方式优于纯文本翻译；适用范围较窄（仅限 arXiv LaTeX、英译中）。

#### 学习与衍生材料

- [cheatsheet-generator-skill](https://github.com/evan715823/cheatsheet-generator-skill) - 作者 [evan715823](https://github.com/evan715823) · `MIT` · `net`.<br>把课程幻灯片与 PDF 转成信息密集、可直接应考的 LaTeX 速查表。定位窄、面向学生（偏学习/教学而非原创研究），但切中需求且受欢迎；适合浓缩课程材料，不适合文献工作。
- [lecture-to-notes](https://github.com/ysyecust/lecture-to-notes) - 作者 [ysyecust](https://github.com/ysyecust) · `NOASSERTION`.<br>通过字幕提取、关键帧检测与智能裁剪截图，把 YouTube/Bilibili 的讲座视频转成结构化的 LaTeX/PDF 笔记。对学生既新颖又实用；质量取决于字幕是否可得，许可证情况也存疑。
- [paper2code](https://github.com/prathamlearnstocode/paper2code) - 作者 [prathamlearnstocode](https://github.com/prathamlearnstocode) · `MIT` · `net`.<br>输入一个 arXiv ID，输出有引用锚定的 Python 实现——每个模块都标注它对应论文的哪一节，遇到含糊之处会明确标记而非擅自猜测。非常适合论文复现；并非通用代码生成器。

### PDF / OCR / 文档解析

> 把 PDF、扫描件与 Office 文档转成干净、可直接喂给大模型的结构——版面感知解析，保留表格、公式与图片。

- [auto-paper-harvester](https://github.com/jxtse/auto-paper-harvester) - 作者 [jxtse](https://github.com/jxtse) · `No License` · `net`.<br>按 DOI 批量下载论文 PDF，逐级回退：先走出版商 TDM API（Wiley/Elsevier/Springer），再到 OA 渠道（Crossref/OpenAlex/Unpaywall），最后可选复用机构 session 的浏览器回退。适合批量获取；内置一处硬编码凭证。
- [DOCX (Anthropic document skill)](https://github.com/anthropics/skills/tree/main/skills/docx) - 作者 [Anthropic](https://github.com/anthropics) · `Proprietary`.<br>Anthropic 的 Word 技能，学术上的长处是对修订痕迹和批注的一流支持——处理已批注稿件，开箱即用里的最佳选择。
- [mineru-skill](https://github.com/nebutra/mineru-skill) - 作者 [nebutra](https://github.com/nebutra) · `MIT` · `net`.<br>借助 MinerU 将 PDF、Office 文档和图片解析为干净的 Markdown，保留 LaTeX 公式、表格并支持 OCR。是把论文转为可编辑文本的扎实 OCR/提取入口；但依赖 MinerU，且只是若干 PDF 转 MD skill 之一，宜对比后再选。
- [PDF (Anthropic document skill)](https://github.com/anthropics/skills/tree/main/skills/pdf) - 作者 [Anthropic](https://github.com/anthropics) · `Proprietary`.<br>Anthropic 自家的 PDF 技能——在 pypdf/pdfplumber/reportlab/qpdf 之上做合并/拆分/抽取/填表。日常活儿的可靠默认，但不是高精度 OCR 引擎。
- [PPTX (Anthropic document skill)](https://github.com/anthropics/skills/tree/main/skills/pptx) - 作者 [Anthropic](https://github.com/anthropics) · `Proprietary`.<br>Anthropic 的 PowerPoint 技能，能做幻灯片、也能从任意 .pptx 抽文字——把论文改成报告很顺手。是创作工具，不是忠于版式的幻灯 OCR。
- [XLSX (Anthropic document skill)](https://github.com/anthropics/skills/tree/main/skills/xlsx) - 作者 [Anthropic](https://github.com/anthropics) · `Proprietary`.<br>Anthropic 的表格技能，难得地真去重算公式、而非只读缓存值——适合把杂乱的补充数据表整理干净。

## 分析与可视化

> 做分析、出图——让数字与论述保持一致。

### 数据分析与统计

> 做分析、也讲清分析——统计、可复现流程，以及让数字与论述保持一致的工具。

#### 统计建模与检验选择

- `Suite` [ai4ss-skills](https://github.com/siyaozheng/ai4ss-skills) - 作者 [siyaozheng](https://github.com/siyaozheng) · `GPL-3.0` · `net`.<br>面向社会科学研究的 agent 技能，用 R 和 Python，能跨 session 保持数据集/codebook 上下文，并附 benchmarks 板块。适合可复现的定量社科分析；GPL-3.0，聚焦统计工作流而非写作。
- `Suite` [social-data-analysis](https://github.com/nealcaren/social-data-analysis) - 作者 [nealcaren](https://github.com/nealcaren) · `MIT` · `net`.<br>18 个技能的社会学方法包，覆盖定量与定性社会数据分析，作者为一位计算社会学家。范围与来源可靠；各组件深度未经核实（内容未作检视）。
- [claude-statistical-analysis-skill](https://github.com/terryfyl/claude-statistical-analysis-skill) - 作者 [terryfyl](https://github.com/terryfyl) · `MIT` · `net`.<br>统计顾问式 skill：先诊断前提假设，再自动选择方法（从 t 检验到 SEM/HLM/IRT/meta-analysis），并产出 APA-7 表格、300dpi 图表与结果段落。先验前提优先是它的特色；高级方法需要 R Docker 支持。
- [stata-ai-fusion](https://github.com/haoyu-haoyu/stata-ai-fusion) - 作者 [haoyu-haoyu](https://github.com/haoyu-haoyu) · `MIT`.<br>让 agent 通过一个 MCP server 加一份 Stata skill 知识库，驱动一个真实的 Stata 会话：运行命令、查看数据、提取估计结果、抓取图形。为经济学/流行病学/生物统计填补了 AI 与 Stata 之间的空缺；需要已授权的 Stata 安装。
- `Plugin` [stata-skill](https://github.com/dylantmoore/stata-skill) - 作者 [Dylan Moore](https://github.com/dylantmoore) · `No License`.<br>一份有评测背书的参考，专治 Claude 写出"看似没错、实则有坑"的 Stata 代码——那些不报错却误导结果的陷阱。

#### 因果推断与计量经济

- [econometrics-skill](https://github.com/xiaomihu1992/econometrics-skill) - 作者 [xiaomihu1992](https://github.com/xiaomihu1992) · `MIT`.<br>一个应用因果推断 skill：涵盖 17 种估计量（OLS、PSM/IPW/AIPW、IV/2SLS、DiD/事件研究、精确/模糊 RDD），并配有方法选择决策树、诊断检验与报告模板。对表格型计量经济学很扎实；但前提是面板数据已清洗干净。

#### 领域计算与仿真流程

- `Suite` [claude-scientific-skills](https://github.com/k-dense-ai/claude-scientific-skills) - 作者 [k-dense-ai](https://github.com/k-dense-ai) · `MIT`.<br>庞杂的计算科学 skill 套件（143 个 skill）：生物信息学流水线（比对、RNA-seq、变异检测、系统发育、蛋白结构、MD）外加完整的统计栈（差异表达、通路/GO、生存分析、meta 分析等）。
- `Suite` [fiftyone-skills](https://github.com/voxel51/fiftyone-skills) - 作者 [voxel51](https://github.com/voxel51) · `Apache-2.0` · `net`.<br>FiftyOne 官方 skill 集：借助 AI 助手完成计算机视觉数据集整理、评估与模型分析的专家级工作流，并配有一个配套的 MCP server。对 CV/ML 数据集研究很强；但与 FiftyOne 工具绑定，且专限于计算机视觉。
- `Suite` [materials-simulation-skills](https://github.com/heshamfs/materials-simulation-skills) - 作者 [heshamfs](https://github.com/heshamfs) · `Apache-2.0` · `net`.<br>含 23 个 skill 的计算材料科学套件：数值稳定性分析、有限元网格剖分、DFT/MD 设置、蒙特卡洛与相场建模、谱方法、时间积分以及不确定性量化。方法学覆盖面很广。
- `Suite` [matlab-agentic-toolkit](https://github.com/matlab/matlab-agentic-toolkit) - 作者 [matlab](https://github.com/matlab) · `No License` · `net`.<br>MathWorks 官方出品、面向 MATLAB/Simulink 工程与科学工作的 61 个 agent skill 工具包：曲线拟合、系统辨识、时间序列预测、信号去趋势/滤波、参数优化、单位换算、数据清洗等。
- `Suite` [scienceclaw](https://github.com/lamm-mit/scienceclaw) - 作者 [lamm-mit](https://github.com/lamm-mit) · `Apache-2.0` · `net`.<br>来自 MIT LAMM 实验室、含 340+ 个 skill 的计算科学与工程套件：材料科学、分子动力学、有限元分析、符号数学与多尺度建模。

#### 可复现分析框架

- `Suite` [daaf](https://github.com/daaf-contribution-community/daaf) - 作者 [daaf-contribution-community](https://github.com/daaf-contribution-community) · `LGPL-3.0` · `net` `hooks`.<br>一套指令框架，让 Claude Code 在任何领域都表现得像一名严谨、可复现的定量研究者：可审计的步骤、护栏，以及人在回路（human-in-the-loop）的核验。重量级且观点鲜明；每个核心决策都由用户把舵。

### 图表与可视化

> 绘制达到发表水准的图——为期刊而非仪表盘打造的图表、绘图与视觉编码。

#### 方法与概念图

- `Suite` [paper-craft-skills](https://github.com/zsyggg/paper-craft-skills) - 作者 [zsyggg](https://github.com/zsyggg) · `No License`.<br>一条命令即可从 arXiv 链接生成发表级的方法图、AIGC 幻灯片，以及深入浅出的讲解文章，无需 API key。最擅长把论文内部机制转化为可视化呈现；输出风格主张鲜明。
- [engineering-figure-agent](https://github.com/heyu-233/engineering-figure-agent) - 作者 [heyu-233](https://github.com/heyu-233) · `MIT` · `net`.<br>生成发表级的工程与计算机科学图表（示意图与绘图两种模式），支持中英双语标注、输出可编辑，并针对中文学术论文做了调校。功能聚焦，但把作图这件事做得很好；不是通用绘图库。
- [gen-pseudocode-skill](https://github.com/huiyuli-2000/gen-pseudocode-skill) - 作者 [huiyuli-2000](https://github.com/huiyuli-2000) · `MIT`.<br>依据论文的方法、代码与笔记，重建可直接投稿的 algorithm2e LaTeX 伪代码，配有 code-to-math 记号映射、分会议期刊的样式、复杂度分析和编译检查。适合 ML/SCI 的算法展示；以方法层级切入。
- [paperbanana-skill](https://github.com/plutolei/paperbanana-skill) - 作者 [plutolei](https://github.com/plutolei) · `MIT` · `net`.<br>多 agent 流水线（Retriever→Planner→Stylist），从文本/数据生成学术示意图、方法图、统计图与幻灯片，并配有「图 vs 参考图」评估器。支持八家 provider；较为成熟（v4.x）。用于一次性出图则偏重。
- [research-paper-figure-skill-factory](https://github.com/c-narcissus/research-paper-figure-skill-factory) - 作者 [c-narcissus](https://github.com/c-narcissus) · `MIT-0`.<br>一个“制图 skill 的工厂”：把某一类论文配图（框架图、机制图、分类图、结果图）提炼成可复用的图表生成 skill，并以多候选轮次产出。流程偏重、偏元层面；用于单张一次性配图属于杀鸡用牛刀。
- [skill-research-figure](https://github.com/chingswy/skill-research-figure) - 作者 [chingswy](https://github.com/chingswy) · `No License`.<br>为论文绘制专业的学术配图——LaTeX/TikZ 图示与手绘风格 SVG。定位严格收敛于学术配图生成；需补上 LICENSE。静态扫描干净；做论文配图（尤其 TikZ）是一个靠谱之选。
- [thesis-figure-skill](https://github.com/0xe1337/thesis-figure-skill) - 作者 [0xe1337](https://github.com/0xe1337) · `MIT`.<br>把论文文字转成可发表质量的图：LaTeX/TikZ（像素级精确、可嵌入）或 draw.io XML（路线图、幻灯片）。追求高信息密度 + 一次编译通过；支持双语。最适合结构化的 CS/ML 示意图，而非数据驱动的统计图。

#### 数据驱动的统计绘图

- `Plugin` [nice-figures](https://github.com/mapika/nice-figures) - 作者 [mapika](https://github.com/mapika) · `MIT`.<br>走柔和粉彩、研究博客风格的 Matplotlib 图表：带置信带的平滑趋势线、圆角柱状图、双对数 scaling-law 散点图、白色背景，外加 16 套配方。很适合 ML/alignment 类的文章；但只有一种鲜明的审美风格。
- [stata-graphics-skill](https://github.com/youngfujun/stata-graphics-skill) - 作者 [youngfujun](https://github.com/youngfujun) · `No License`.<br>面向经济学实证研究的 AI 辅助 Stata 绘图知识库。定位窄但精准切中经济学发表用图；主要短板是缺少 LICENSE。是基于 Stata 的分析工作流的好搭档。

#### 图表美学与样式系统

- [AgentFigureGallery](https://github.com/Dsadd4/AgentFigureGallery) - 作者 [Dsadd4](https://github.com/Dsadd4) · `MIT` · `net`.<br>一层"审美"而非绘图库——agent 从 1.6 万+ 图库中遴选，从此不再凭空想象 Nature 配图该长什么样。
- [paper-style](https://github.com/freemty/paper-style) - 作者 [freemty](https://github.com/freemty) · `MIT`.<br>五套低饱和度配色主题，让一篇论文在 LaTeX 正文与 matplotlib 图表（从 documentclass 到 savefig）之间拥有统一的视觉身份，并附预览 PDF。很适合保持配色一致；纯粹是样式层，不是绘图或排版工具。
- [tufte-data-viz](https://github.com/caylent/tufte-data-viz) - 作者 [caylent](https://github.com/caylent) · `MIT`.<br>在六种绘图库上贯彻 Tufte 的数据可视化原则（高 data-ink 比、不要 chartjunk、不用饼图），并附带可访问性规则。做干净、诚实的图表极佳；刻意地立场鲜明，因而会覆盖你的样式选择。

## 写作与润色

> 起草学术文字、拿下经费，并抹去机器写作的痕迹。

### 学术写作与起草

> 起草学术文字——为论文、学位论文与综述搭好章节、结构与论证骨架。

#### 稿件起草流程

- `Suite` [academic-skills](https://github.com/chtc66/academic-skills) - 作者 [chtc66](https://github.com/chtc66) · `MIT` · `net`.<br>面向日常科研的工作流套件（偏 AI/NLP、中文优先）：论文精读笔记、综述写作、arXiv 追踪、审稿/rebuttal 草拟、实验日志小结、benchmark 提取、研究空白挖掘与每周组会汇报。覆盖面广，单项偏轻量。
- `Suite` [academic-writing](https://github.com/alessandrocaforio/academic-writing) - 作者 [alessandrocaforio](https://github.com/alessandrocaforio) · `MIT`.<br>多 agent 写作系统，将一篇实证论文拆解为各章节专属的 skill（引言、方法、结果、讨论、摘要），外加文献综述、分析与投稿环节。章节级的结构划分是其强项；名义上面向经济学。
- `Suite` [academic-writing-skills](https://github.com/wenyuchiou/academic-writing-skills) - 作者 [wenyuchiou](https://github.com/wenyuchiou) · `MIT`.<br>一套不限学科的论文写作工作流：以发现为先的起草、去 AI 痕迹/过度宣称检测、论点到证据的核查、审稿回应表，以及投稿前清单，并支持逐篇论文的期刊规范覆盖。附带 evals——这很少见，值得肯定。
- `Suite` [enhanced-mathmodel-codex-skills](https://github.com/xzwwwwww/enhanced-mathmodel-codex-skills) - 作者 [xzwwwwww](https://github.com/xzwwwwww) · `No License` · `net`.<br>面向数学建模竞赛的全流程 skill，把工作流一路自动化到一篇完整的建模论文（偏 Codex）。小众但确实有学术性、针对性强；无许可证是主要短板。
- `Suite` [nature-paper-skills](https://github.com/boom5426/nature-paper-skills) - 作者 [boom5426](https://github.com/boom5426) · `MIT` · `net`.<br>一条以期刊为先、面向 Nature 风格投稿的稿件流水线——引用完整性、论点/证据的严格把控、投稿前预检与反驳回应。主张鲜明、定位有意收窄；对高端生物/医学写作很有优势。
- `Suite` [nature-writing-skill](https://github.com/syntaxsmith/nature-writing-skill) - 作者 [syntaxsmith](https://github.com/syntaxsmith) · `No License`.<br>面向中国 AI/ML 研究者的 Nature 系（NMI/NC/NCS/Nature）论文写作技艺，基于对 44 篇开放获取论文的句子级抽取构建，配有可 grep 溯源的语料库和一个配套的图表 skill。聚焦于 Nature 风格的 AI 方法类论文这一细分场景。
- `Suite` [paperorchestra](https://github.com/ar9av/paperorchestra) - 作者 [ar9av](https://github.com/ar9av) · `NOASSERTION` · `net`.<br>一个可移植的 skill 包，实现 Google 的 PaperOrchestra：把 agent 的实验日志转化为“想法+日志”输入，再经由提纲→写作→精修→绘图、配合 autorater 产出一篇 LaTeX 论文。最适合你已有实验数据的情形，而非以文献为起点。
- `Suite` [paperspine](https://github.com/wubing2023/paperspine) - 作者 [wubing2023](https://github.com/wubing2023) · `MIT` · `net`.<br>十个技能的学术写作套件，覆盖文献发现、文献综合、论点构建、稿件修订、引用、配图、审稿回复与投稿。端到端覆盖扎实，中英双语；偏重编排。
- [paper-orchestra-for-claude-code](https://github.com/sunjongos/paper-orchestra-for-claude-code) - 作者 [sunjongos](https://github.com/sunjongos) · `MIT` · `net`.<br>一条野心十足的 12-agent 韩英双语 SCI 论文流水线，但其 SKILL.md 充斥"超越一切"式夸大宣传——阅读时需多留个心眼。
- [paper-writing-skill](https://github.com/snl-ucsb/paper-writing-skill) - 作者 [snl-ucsb](https://github.com/snl-ucsb) · `MIT`.<br>将某 systems 实验室久经实战的论文写作方法论（从头脑风暴到精炼压缩）编码成形，配有修辞策略模板与配图综合指南。在 CS/systems 类会议上最为见长；其鲜明的风格未必适用于所有领域。
- [trivium](https://github.com/MetaQiu/Trivium) - 作者 [MetaQiu](https://github.com/MetaQiu) · `MIT` · `net`.<br>让 Claude、Codex、Gemini 三方共识起草每个段落，赌三模型认可的文字也能让 LLM 审稿人满意——需同时装好三个 CLI。

#### LaTeX 与排版一体化写作

- `Suite` [ageaf](https://github.com/onireimu/ageaf) - 作者 [onireimu](https://github.com/onireimu) · `MIT` · `net`.<br>把 AI agent（Claude、OpenAI 等）直接接入 Overleaf 进行 LaTeX 论文写作与编辑。面向主流协作式 LaTeX 编辑器的一个聚焦、真正学术向的集成；验证度尚浅（22 stars），但切中了一个真实的工作流。
- `Suite` [awesome-latex-skills](https://github.com/calix-l/awesome-latex-skills) - 作者 [calix-l](https://github.com/calix-l) · `MIT` · `net`.<br>一个 LaTeX 论文写作 skill 集：修复编译报错、润色学术文笔、按会议/期刊模板排版、阅读论文，以及找回丢失的源码。对稿件工作精炼而实用；本质是 prompt 合集，因此深度取决于背后的 agent。
- `Suite` [latex-paper-skills](https://github.com/yunshenwuchuxun/latex-paper-skills) - 作者 [yunshenwuchuxun](https://github.com/yunshenwuchuxun) · `MIT` · `net`.<br>面向 ML/AI 的模块化 LaTeX 论文写作套件：从选题到编译出 PDF，配有经核验的 BibTeX 引用、带关卡的工作流、结果回填步骤和文句「节奏精修器」，并支持多 agent（Claude+Gemini）协作。
- `Plugin` [academic-writing-agents](https://github.com/andrehuang/academic-writing-agents) - 作者 [andrehuang](https://github.com/andrehuang) · `MIT`.<br>一个 Claude Code 插件，让 12 个专项 agent（逻辑、技术、文笔、参考文献、LaTeX 等评审角色）并行审阅同一份草稿，先诊断问题、再在人工确认后修改。擅长结构化的稿件评审；并非从零起草的写作工具。
- [stats-paper-writing-agent-skills](https://github.com/fuhaoda/stats-paper-writing-agent-skills) - 作者 [fuhaoda](https://github.com/fuhaoda) · `No License`.<br>一个面向统计学写作的 LaTeX 工作台：起草摘要/关键词，从结构、参考文献、记号和可复现性线索等方面审查稿件，撰写审稿意见与逐条回复信，并附带 check_tex.py/check_bib.py。

#### 学位论文写作

- [chinese-thesis-workbench-skill](https://github.com/zyhsechub/chinese-thesis-workbench-skill) - 作者 [zyhsechub](https://github.com/zyhsechub) · `MIT`.<br>把学生的项目（源代码、数据库、截图、参考文献）转成可追溯、可续写、可评审的本科毕业论文，遵循学校模板与范文风格。非常适合中文毕设；并非通用学术写作工具。
- [humanities-thesis-skill](https://github.com/ganzhi-black/humanities-thesis-skill) - 作者 [ganzhi-black](https://github.com/ganzhi-black) · `MIT` · `net`.<br>中文优先的人文/社科学位论文副驾，强调把论证想透、逐段审查，而非直接生成文字。反编造的纪律很强。
- [physics-lab-report-skill](https://github.com/ydh0411/physics-lab-report-skill) - 作者 [ydh0411](https://github.com/ydh0411) · `MIT`.<br>生成符合规范的大学物理预习与正式实验报告（LaTeX），并内置真实的数据处理：不确定度传递、逐差法、最小二乘拟合与不确定度分析。
- [skill-thesis-writer](https://github.com/yanlin-cheng/skill-thesis-writer) - 作者 [yanlin-cheng](https://github.com/yanlin-cheng) · `MulanPSL-2.0`.<br>一个中文学术学位论文写作技能，覆盖工科、心理、教育与管理的本科及研究生工作，强制 GB/T 7714-2015 参考文献格式，内置数据分析与引用管理。

#### 文献综述写作

- [academic-paper-skills](https://github.com/lishix520/academic-paper-skills) - 作者 [Li Shixiong (lishix520)](https://github.com/lishix520) · `MIT`.<br>难得以人文学科为重心的撰写流水线，面向哲学与预印本平台，配引文支撑的研究空白分析——现已停止维护。
- [lit-review](https://github.com/bethww/lit-review) - 作者 [bethww](https://github.com/bethww) · `MIT`.<br>把文献综述当作一项论证、分七个阶段（提问、方法、综合）来引导，而非堆砌文献摘要。中英双语；明确声明不会替你把论文写出来。
- [litllm](https://github.com/litllm/litllm) - 作者 [litllm](https://github.com/litllm) · `Apache-2.0` · `net`.<br>基于 RAG 的文献综述助手（TMLR 2025），从给定论文集起草结构化的 related-work 章节，可作为 web app 或 Claude Code skill 使用。在 related-work 综合上很强；但定位窄（只做 related-work，非整篇论文）且以 demo 形式托管。

#### 行文润色与学科风格

- `Suite` [claude-code-my-workflow](https://github.com/pedrohcgs/claude-code-my-workflow) - 作者 [Pedro H. C. Sant'Anna (pedrohcgs)](https://github.com/pedrohcgs) · `MIT` · `net` `hooks` `bypass`.<br>一位计量经济学家从博士课程打磨出的、可直接 fork 的 36 命令 Claude Code 配置——但默认开启 bypass-permissions。
- `Suite` [paper-discipline-skills](https://github.com/lambenthan/paper-discipline-skills) - 作者 [lambenthan](https://github.com/lambenthan) · `MIT`.<br>源自一本真实「错误记录册」的 12 个中文科研写作「纪律」skill：改 Word 前先备份、术语保护、批量前先试点、逻辑一致性、并行审查。每个都配有一张「借口对照表」来杜绝偷工。提供的是护栏，而非内容。
- [econ-writing-skill](https://github.com/hanlulong/econ-writing-skill) - 作者 [Lu Han (hanlulong)](https://github.com/hanlulong) · `MIT`.<br>本列表中出处最扎实的学科写作技能，把 50+ 篇名家经济学写作指南提炼成可执行的规则。
- [english-writing](https://github.com/yzy1996/english-writing) - 作者 [yzy1996](https://github.com/yzy1996) · `No License`.<br>学术英语润色 skill，背后是一本精选的分章节短语手册（摘要、引言、相关工作、方法、实验、rebuttal），收录了从真实论文中挖掘的地道用法。对非母语的 CS/ML 作者在措辞上帮助很大；无 LICENSE 文件。
- [journal-adapt-writing-skill](https://github.com/wantongc/journal-adapt-writing-skill) - 作者 [wantongc](https://github.com/wantongc) · `MIT`.<br>不止于套用通用文体规则，而是从目标期刊自身的论文出发、构建一个以语料为依据的“动态 skill”，再逐节修改。其独到之处在于针对具体期刊做适配；但需要你自行提供参考语料库。
- [research-paper-writing](https://github.com/Master-cai/Research-Paper-Writing-Skills) - 作者 [Xudong Cai (Master-cai)](https://github.com/Master-cai) · `MIT`.<br>把彭思达广为流传的科研写作笔记，封装成面向 ML/CV/NLP 论文的段落级改写纪律。
- [research-writing-skill](https://github.com/alfonso0512/research-writing-skill) - 作者 [alfonso0512](https://github.com/alfonso0512) · `MIT`.<br>中英双语的学术写作 prompt 合集：30 个模板，涵盖文献综述、列提纲、起草、润色、de-AI、审稿 rebuttal 与基金文本。覆盖广、受欢迎，但基于模板而非工具支撑；核验能力较弱。
- [writing-in-the-sciences-skill](https://github.com/jingkarqi/writing-in-the-sciences-skill) - 作者 [jingkarqi](https://github.com/jingkarqi) · `MIT`.<br>一个基于斯坦福《Writing in the Sciences》（Sainani）课程的科学写作 skill：用结构化的起草/修改工作流，产出清晰、有证据支撑的文字。原则根基扎实；为 Codex 原生的单个 skill，以英语写作教学为核心。

### 写作质量与去 AI 味

> 把初稿改紧、去 AI 味——讲清楚、有自己的语气，并抹去那些一眼看出是机器写的痕迹。

#### 去 AI 味与拟人化

- `Suite` [science_narrative_skills](https://github.com/kangning-huang/science_narrative_skills) - 作者 [kangning-huang](https://github.com/kangning-huang) · `No License` · `net`.<br>借助 And-But-Therefore（ABT）叙事框架（出自 Schimel 的《Writing Science》）评估科技写作，诊断一篇论文的论证是否构成连贯的故事，而非一堆事实的罗列。
- [avoid-ai-writing](https://github.com/conorbronsdon/avoid-ai-writing) - 作者 [Conor Bronsdon (conorbronsdon)](https://github.com/conorbronsdon) · `MIT`.<br>最诚实的去 AI 化技能——它引用误报研究，坚持自己的标记"只是信号，不是证据"。
- [humanize-academic-writing](https://github.com/momo2young/humanize-academic-writing) - 作者 [momo2young](https://github.com/momo2young) · `MIT`.<br>面向社会科学文本的“去 AI 味”skill：标记 AI 痕迹（结构重复、语言空泛、行文机械），并以真实可信的学术口吻重写，配有检测/分析脚本。面向英语非母语的研究者。
- [humanizer](https://github.com/blader/humanizer) - 作者 [blader](https://github.com/blader) · `MIT` · `net`.<br>去除文本 AI 痕迹（破折号滥用、三段式法则、填充语、否定式排比）的事实标准。单一用途，权限仅限读/写工具；作为收尾润色一遍极佳，但不是完整的写作助手。
- [humanizer-academic](https://github.com/matsuikentaro1/humanizer_academic) - 作者 [Kentaro Matsui (matsuikentaro1)](https://github.com/matsuikentaro1) · `MIT`.<br>面向医学论文的去 AI 味工具，反其道而行——找回 LLM 刻意回避的正式术语，而非把一切抹平。
- [humanmade-antislop](https://github.com/machinemade-mm/humanmade-antislop) - 作者 [machinemade-mm](https://github.com/machinemade-mm) · `MIT`.<br>去 AI 味的科学写作 skill，融合人声化规则、IMRAD/引用格式脚手架与 GRADE 式点评。在禁用词清除和报告规范意识上很强；衍生自 K-Dense 与维基百科的 AI 写作指南。
- [paper-humanizer-skill](https://github.com/crabin/paper-humanizer-skill) - 作者 [crabin](https://github.com/crabin) · `No License`.<br>中英文学术文本去 AI 味工具：清除 AI 写作痕迹，同时严格保留事实、数字与结论，并报告检测到的模式。缺少明确的 LICENSE。
- [skill-deslop](https://github.com/stephenturner/skill-deslop) - 作者 [Stephen Turner (stephenturner)](https://github.com/stephenturner) · `MIT`.<br>一款懂科研的去 AI 味技能，对 Methods 被动语态等学科惯例网开一面——嫌 stop-slop 太"博客腔"时就选它。
- [stop-slop](https://github.com/hardikpandya/stop-slop) - 作者 [Hardik Pandya (hardikpandya)](https://github.com/hardikpandya) · `MIT`.<br>star 数最高的去 AI 味技能——一本独断的八条规则手册，但面向通用散文、非专为学术，也不处理误报。
- `Plugin` [unslop](https://github.com/mohamedabdallah-14/unslop) - 作者 [mohamedabdallah-14](https://github.com/mohamedabdallah-14) · `MIT` · `net` `hooks`.<br>一个去 AI 痕迹的 plugin，剔除各类 AI 腔（谄媚口吻、套话、模棱两可的措辞、em-dash 堆砌），同时保留代码、URL 与标题，并配有经过基准测试的检测器。通用文字的"去 AI 化"很强；但不针对学术场景，需调校才能保住技术性语气。

#### AIGC 检测规避（学位论文）

- [aigc-down-skill](https://github.com/yezery/aigc-down-skill) - 作者 [yezery](https://github.com/yezery) · `MIT`.<br>面向中文学位论文的去 AIGC skill：解析知网/万方的检测报告，定位被标记的段落，在保留论证与语体的前提下改写以降低 AI 检测率。对中文论文有效；不适用于英文，且不保证能通过各类检测器。
- [anti-aigc-zh](https://github.com/beizi6/anti-aigc-zh) - 作者 [beizi6](https://github.com/beizi6) · `MIT`.<br>一个中文反 AIGC 改写工具，从检测器的工作原理出发进行推理（概率曲率、perplexity 均匀性、水印 token），并附带图片元数据清除功能。定位小众、偏重规避检测；附带的分块写文件工具只是顺带提供。
- [deai-academic-zh](https://github.com/houlaisan/deai-academic-zh) - 作者 [houlaisan](https://github.com/houlaisan) · `MIT`.<br>面向中文学位论文的 AIGC 检测 + 去 AI 改写，采用有据可查的三轮方法（措辞→突发性→重构）并恪守零捏造原则；报告了维普/知网检测分数的实际下降。适用于中文本科/硕士学位论文，不适用于英文。
- [dissertation-polisher-zh](https://github.com/chipsahoym/dissertation-polisher-zh) - 作者 [chipsahoym](https://github.com/chipsahoym) · `MIT`.<br>面向中文计算机博士学位论文的润色工具：批量通读 120 页以上的论文，清除 AI 写作痕迹，执行学术规范检查（残留的第一人称、图表/参考文献格式）并核对章节一致性。面向正式的学术文本，而非随意的口语化“去 AI 味”。
- [humanizer-academic-zh](https://github.com/cangtianhuang/humanizer-academic-zh) - 作者 [cangtianhuang](https://github.com/cangtianhuang) · `MIT` · `net`.<br>中文学术"去 AI 味"工具：在保留核心论点的前提下改写论文文本，以降低 AIGC 检测率与 AI 腔调，刻意做得轻量、省 token。中文语境下实用的小众工具；效果取决于模型，且难以验证。
- [humanizer-zh-academic](https://github.com/redbaronyyyyy-eng/humanizer-zh-academic) - 作者 [redbaronyyyyy-eng](https://github.com/redbaronyyyyy-eng) · `MIT`.<br>改写中文学术文字，使其读起来像人写的，并降低 AIGC 检测器的评分。单一用途，在中文写作者中颇受欢迎；产出质量高度依赖原始草稿，而且"击败检测器"本身就是个不断变化的移动靶。

#### 稿件校对与质量审查

- [proofreading](https://github.com/jakobthumm/proofreading) - 作者 [jakobthumm](https://github.com/jakobthumm) · `MIT`.<br>对照 100+ 项检查（结构、数学记号、统计、配图、语法、缩写）校对学术论文，支持报告模式或交互模式，并能从批注 PDF 中提取审稿标记。检查清单详尽；英文风格的检查项需要调校。
- [slopbuster](https://github.com/gabelul/slopbuster) - 作者 [gabelul](https://github.com/gabelul) · `MIT` · `net`.<br>面向散文、代码与学术写作的本地去 AI 味工具：两遍式审查标记出 100+ 种典型 AI 模式，按三档评分，并可选注入个人语气进行改写——全程离线，无 API 调用。
- [thesis-writer](https://github.com/ibrahim-kukash/thesis-writer) - 作者 [ibrahim-kukash](https://github.com/ibrahim-kukash) · `MIT`.<br>撰写学位论文章节，同时对照一份 23 点量表扫查 14 种常见的 AI 写作痕迹，力求让学术文字读起来像人写的。一个聚焦于写作 + 去 AI 味的学位论文工具；作为质量闸门很有用，但验证尚浅（8 star）。

#### 反幻觉与过度修订防护

- [grounded-research-skill](https://github.com/arturseo-geo/grounded-research-skill) - 作者 [arturseo-geo](https://github.com/arturseo-geo) · `MIT`.<br>反幻觉研究模式，落实 Anthropic 的三条护栏：承认不确定、先引用后分析、每条论断都给出引用，并配以自我审计与公开更正。以创造力换取可信度；它是一层事实校准的叠加层，而非通用的 research 模式。
- [sciwrite](https://github.com/labarba/sciwrite) - 作者 [Lorena A. Barba (labarba)](https://github.com/labarba) · `CC-BY-4.0`.<br>把 Sainani 在斯坦福的"Writing in the Sciences"方法编码成五道顺序审查。一款有学术渊源的论文"去冗赘"之选。

## 评审与发表

> 拿到审稿水准的评判，再把稿件做到可投状态。

### 同行评审与回应

> 评审与回应——审稿水准的评判、申辩信，以及让论文获接收的「致审稿人回复」。

#### 投稿前评审与申辩

- `Suite` [AI-research-feedback](https://github.com/claesbackman/AI-research-feedback) - 作者 [Claes Bäckman](https://github.com/claesbackman) · `MIT`.<br>专为 AER/QJE/JF 量级经济学调校的投稿前审稿人模拟器——六个并行 agent，不适合泛用型审稿。
- `Suite` [archora-skills](https://github.com/richard-kim-79/archora-skills) - 作者 [Richard Kim (Archora)](https://github.com/richard-kim-79) · `MIT`.<br>能模拟主编加三位审稿人；背靠厂商（Archora），但以纯 markdown 形式独立运行。
- `Suite` [polisci-review](https://github.com/cmertdalli/polisci-review) - 作者 [cmertdalli](https://github.com/cmertdalli) · `MIT`.<br>面向政治学论文的投稿前审查：9 个模块（贡献、理论、测量、识别、透明度、期刊匹配），配有按期刊定制的审稿人 persona 与 8 份经核实的期刊政策档案。严谨且高度学科专属。
- [academic-review-skill](https://github.com/pengkangzhen/academic-review-skill) - 作者 [pengkangzhen](https://github.com/pengkangzhen) · `MIT`.<br>审阅运筹学/管理科学稿件，着眼学术价值而非实现细节，识别领域特有的疑点（不可行的取值、无意义的 VSS%），并刻意把批评措辞为提问，以免误伤真正反直觉的发现。
- [ai-peer-review-skill](https://github.com/alexwortega/ai-peer-review-skill) - 作者 [alexwortega](https://github.com/alexwortega) · `MIT`.<br>丢进一份论文 PDF，得到 N 份独立的结构化评审意见，外加一份综合的 meta-review 和一张问题清单 CSV。将 poldrack/ai-peer-review 改造为免费的 Claude subagent；默认采用 alignment 式的严苛批评者口径。
- [manuscript-review-skill](https://github.com/shaowen-ye/manuscript-review-skill) - 作者 [shaowen-ye](https://github.com/shaowen-ye) · `MIT`.<br>由六位角色专精的 AI 审稿人（架构、理论、方法等）做投稿前稿件评审，输出一份中英双语、彩色批注的 .docx，含 1-10 评分矩阵与按优先级排列的修改建议，并按目标期刊校准。专业性强。
- [mean-reviewer-skill](https://github.com/xz-liu/mean-reviewer-skill) - 作者 [xz-liu](https://github.com/xz-liu) · `No License`.<br>扮演最坏情况下的对抗式审稿人：堆砌夸大的“缺点墙”、攻击研究框架、把分数钉死在 reject，并在 rebuttal 阶段寸步不让。一半是对 LLM 审稿的讽喻，一半是真正的投稿前压力测试；并非一个温和的工具。

#### 系统综述与证据评估

- [diogenes](https://github.com/diogenes-project/diogenes) - 作者 [diogenes-project](https://github.com/diogenes-project) · `GPL-3.0` · `net` `hooks`.<br>将一套统一的、反“随声附和”的证据方法论（ICD 203、GRADE、PRISMA、Cochrane RoB 等）落实为 14 步评估流程，用于系统综述、证据分级与论断核验。严谨；附带 hook。
- [slr-prisma](https://github.com/keemanxp/slr-prisma) - 作者 [keemanxp](https://github.com/keemanxp) · `NOASSERTION`.<br>按 PRISMA 2020 框架（方案、检索、筛选、流程图、综合）引导你完成一次系统文献综述。是严谨综述的扎实方法学脚手架；提供的是流程指引而非自动检索，且其 license 尚不明确。

### 投稿、格式与转换

> 让稿件达到可投状态——期刊模板、格式转换，以及编辑最先检查的清样细节。

#### LaTeX 写作与投稿准备

- `Suite` [mcp-overleaf](https://github.com/bettyguo/mcp-overleaf) - 作者 [bettyguo](https://github.com/bettyguo) · `MIT` · `net`.<br>一套 Overleaf/LaTeX 投稿准备工具包（一个 MCP server 加 6 个 skill）：清理 .bib、套用会议/期刊规则包、运行 latexdiff，并起草 related-work 章节。
- `Suite` [paperfit](https://github.com/openraiser/paperfit) - 作者 [openraiser](https://github.com/openraiser) · `MIT` · `net`.<br>LaTeX 排版套件，先编译、把页面渲染为图像，再以视觉方式诊断并修复版式问题（overfull box、浮动体摆放、间距、表格）。其真正的优势在于“视觉闭环”；需要一套可用的本地 LaTeX 工具链。
- [claude-skill-overleaf](https://github.com/junhahyung/claude-skill-overleaf) - 作者 [junhahyung](https://github.com/junhahyung) · `MIT`.<br>在 Claude Code 中经由 Overleaf 的 git bridge 读写 Overleaf 项目：编辑、提交并把 LaTeX 推回网页编辑器，token 处理安全、不做 force-push。附带 rebuttal 脚手架。把 agent 接入 Overleaf 的干净做法。
- [latex-arxiv-skill](https://github.com/renocrypt/latex-arxiv-skill) - 作者 [renocrypt](https://github.com/renocrypt) · `No License` · `net`.<br>一个以 issue 驱动、面向 ML/AI 领域 arXiv 综述论文的 Codex skill：搭建 LaTeX 项目脚手架，并对每条 BibTeX 条目做端到端核验。BibTeX 核验让它高出一般的 LaTeX 模板一筹；定位狭窄，仅针对 arXiv 风格的 ML 综述，且无许可证。
- [latex-document-skill](https://github.com/ndpvt-web/latex-document-skill) - 作者 [ndpvt-web](https://github.com/ndpvt-web) · `MIT`.<br>本列表中模板最丰富的 LaTeX skill——27 套模板覆盖论文、表单与表格；走广度而非深耕一隅。

#### 幻灯片与演示

- [beamer-academic](https://github.com/faust-donf/beamer-academic) - 作者 [faust-donf](https://github.com/faust-donf) · `MIT`.<br>将学位论文或期刊论文转化为可直接演示的学术 Beamer 幻灯片，配有实用的版式库与交互式编辑循环。支持双语，无需 LaTeX 专业知识；适用范围是答辩/会议演示，而非通用幻灯片设计。
- [beamer-skill](https://github.com/Noi1r/beamer-skill) - 作者 [Noi1r](https://github.com/Noi1r) · `MIT`.<br>学术 LaTeX 幻灯片的首选，带着鲜明的排版主张：不用逐步显现动画、设密度上限、靠视觉审查检测溢出。
- [beamer-skill](https://github.com/jaxonjp/beamer-skill) - 作者 [jaxonjp](https://github.com/jaxonjp) · `MIT`.<br>创建/编译/评审/打磨学术 Beamer 幻灯片，支持 TikZ、教学法审查与质量关卡；明确把 PPTX 交由其他 skill 处理。一个经过扩展的衍生作品；设计上仅支持 LaTeX。
- [powerpoint-skill](https://github.com/noi1r/powerpoint-skill) - 作者 [noi1r](https://github.com/noi1r) · `MIT`.<br>制作视觉丰富的 PowerPoint 幻灯片，原生支持 OMML 公式与 LaTeX，很适合需要在幻灯片中呈现真实公式的学术报告与讲座。不限于学术场景，但公式处理能力是它有别于一般 ppt 工具的关键。
- [thesis-defense-pptx-skill](https://github.com/zouchenzhen/thesis-defense-pptx-skill) - 作者 [zouchenzhen](https://github.com/zouchenzhen) · `Apache-2.0`.<br>从你的学位论文 PDF/LaTeX 构建可编辑的答辩幻灯片，并严格沿用学校的 PPTX 模板；清点所引图表，执行溢出/版式检查。完整的质量 gate 需要 Windows + PowerPoint COM 才能运行。

#### 期刊与 Word 模板排版

- `Suite` [docx-skill-4-cn-paper](https://github.com/gostyan/docx-skill-4-cn-paper) - 作者 [gostyan](https://github.com/gostyan) · `MIT`.<br>套用标准中文论文 Word 排版——字体、字号、行距、页边距、标题层级、图表编号、参考文献——适用于课程论文、数学建模竞赛和学位论文，含 md 转 docx。功能窄，但本职做得很好。
- `Suite` [Manuscript Submission Formatting Agent](https://github.com/maxwell2732/my-submission-formatting-agent) - 作者 [Chen Zhu (朱晨)](https://github.com/maxwell2732) · `No License` · `hooks`.<br>为被拒后改投，把已完稿论文按新期刊作者须知重新排版，全程不动结果。
- `Plugin` [word-format-skill](https://github.com/yeap531/word-format-skill) - 作者 [yeap531](https://github.com/yeap531) · `No License`.<br>借助 HTML 桥接，把参照 Word 文档的排版样式复刻到新内容上——适合套用期刊或机构的 .docx 模板。在投稿/格式化这类杂活上很强；适用面广（不限学术），其 license 待核实。

#### 格式转换与文档转化

- `Suite` [paper2patent](https://github.com/7tocr/paper2patent) - 作者 [7tocr](https://github.com/7tocr) · `MIT`.<br>把一篇完成的论文转成中国发明专利申请草稿（权利要求布局、说明书规范、技术效果论证），借助结构化提示、专利附图生成与多个技能完成。一座独特的论文到知识产权的桥梁；面向中国专利。
- [any2pdf](https://github.com/lovstudio/any2pdf) - 作者 [lovstudio](https://github.com/lovstudio) · `MIT`.<br>无需 LaTeX 的 Markdown 转 PDF；真正的过人之处在中日韩文渲染，能正常处理 Pandoc 与 wkhtmltopdf 翻车之处。
- [Markdown Exporter](https://github.com/bowenliang123/markdown-exporter) - 作者 [bowenliang123](https://github.com/bowenliang123) · `Apache-2.0`.<br>本列表中格式覆盖最广、最久经考验的转换器（DOCX/PDF/PPTX/XLSX/EPUB），纯本地运行、无外联。

## 套件、系统与生态

> 多阶段套件、端到端研究 agent、学科专用包，以及更广生态的导览图。

### 技能套件

> 一次覆盖多个生命周期阶段的多技能仓库。在下表中横向比较。

| 套件                                                                                            |     ★ | 技能数 | 最适合                                                                                                                                                | 运行            |
| --------------------------------------------------------------------------------------------- | ----: | --: | -------------------------------------------------------------------------------------------------------------------------------------------------- | ------------- |
| [academic-research-skills](https://github.com/Imbad0202/academic-research-skills)             | 38.3k |   — | 一条专为对抗 AI 编造而设计、刻意拒绝代笔的人在环路流水线；非商业许可证                                                                                                              | `net` `hooks` |
| [academic-research-skills-codex](https://github.com/imbad0202/academic-research-skills-codex) |  6.5k |   — | Codex 原生的学术研究 Skill 集：深度调研、论文起草、稿件评审、从研究到成文的流水线、引用与学术诚信核查。端到端覆盖面广；但以一整个巨型 skill 的形式打包内置（审查时需相应留意）；采用非商用 license                                    | `net` `hooks` |
| [AcademicForge](https://github.com/HughYau/AcademicForge)                                     |  2.3k |   7 | 一个方便的网页安装器，把七套现成的学术 skill 打包装入——但本质是转手打包他人的成果，而非自有产出                                                                                               | `net`         |
| [AI Research Skills (Orchestra)](https://github.com/Orchestra-Research/AI-Research-SKILLs)    | 10.8k |  98 | 一套 98 个 skill 的课程体系，专攻机器学习研究偏工程的那一半，带 agent 从想法走到训练好的模型——不涉及湿实验                                                                                    | `net`         |
| [ai-research-skills](https://github.com/zechenzhangagi/ai-research-skills)                    | 10.8k |   — | 包含 98 个 skill 的 AI/ML 研究套件：研究构思、文献综述、baseline/消融设计、实验追踪、统计显著性检验、图表生成、论文写作、同行评审与 rebuttal。堪称“把你的 agent 变成研究者”的参照级套件                                 | `net`         |
| [anthropics/life-sciences](https://github.com/anthropics/life-sciences)                       |   537 |   — | Anthropic 官方的生命科学 marketplace——一份经甄选的约 20 项合作方数据集成目录，而非 skill 合集                                                                                   | `net`         |
| [aut_sci_write](https://github.com/shzhao27208/aut_sci_write)                                 |   164 |   — | 一个覆盖研究全生命周期的模块化 skill 集：跨 arXiv/PubMed/Web of Science 文献检索、PDF 与图表提取、综述/meta 分析写作、Zotero 同步以及幻灯片制作。覆盖面广、采用率高；属于“样样都能做”的大而全 skill 集，而非某一环节做到最好的专精工具 | `net`         |
| [claude-academic-research](https://github.com/mronkko/claude-academic-research)               |    18 |   — | 由教授打造、覆盖研究全生命周期的套件：PRISMA 综述、同行评议、稿件修订、实证完整性的统计核查，以及由 Zotero/MCP 锚定、拒绝幻觉引用的参考文献。严谨性强；需要配置 Zotero+MCP                                               | `net`         |
| [claude-research](https://github.com/flonat/claude-research)                                  |   120 |   — | 面向博士研究者的基础设施：50 个 skill，外加 agent、hook 与规则，用于参考文献校验、LaTeX 健康检查、实验与因果设计，以及可复现的项目搭建。端到端能力很强；附带 hook 和一个未限定范围的 Bash                                    | `net` `hooks` |
| [claude-scholar](https://github.com/Galaxy-Dawn/claude-scholar)                               |  4.7k |  47 | 面向 CS/AI 研究者的工作台，带一道以证据为门槛的 Claim Promotion Gate；独有自带的 PreToolUse 安全防护 hook                                                                        | `net` `hooks` |
| [claude-scholar](https://github.com/yy/claude-scholar)                                        |    30 |   — | 一套 12 个 skill 的学术工具箱：OpenAlex/arXiv 检索、DOI 转 BibTeX、引用核验、LaTeX 清理、arXiv 打包、投稿前检查、数学核验、稿件/图表点评。坦诚自己尚处早期阶段；并列出其数据外发情况                                | `net`         |
| [claude-scientific-writer](https://github.com/k-dense-ai/claude-scientific-writer)            |  2.1k |   — | 一个包含 27 个 skill 的科学写作 skill 集：文献综述、引用管理、同行评审、图表、海报、幻灯片以及稿件起草。是此处最受欢迎、覆盖面最广的一个，但样样通而无一精；且附带了一个未限定权限范围的 Bash                                         | `net`         |
| [codex-paper-skills](https://github.com/moonlarry/codex-paper-skills)                         |   115 |   — | 面向 Codex/Claude 的论文套件（27 个 skill），覆盖写作链路、图表、实验与论点的一致性、引用审计、证明核查与反驳，并采用证据优先的 agent 协议。覆盖面很广；缺少 LICENSE 是它的主要短板                                      | `net`         |
| [google-deepmind/science-skills](https://github.com/google-deepmind/science-skills)           |  2.4k |  37 | Google DeepMind 官方套件，把 agent 接入真实的生物数据——范围窄于结构生物学与基因组学，但权威                                                                                         | `net`         |
| [mgmt-paper-skills](https://github.com/haonanalex/mgmt-paper-skills)                          |   118 |   — | 管理学研究工作台：从选题到评审的全流程，含 SPSS/Stata/Python 分析、因果方法（DiD/RDD/IV/SC/PSM）、质性编码与期刊图表规范（UTD24）。在经济/管理领域很深；偏向中文数据，需要一个统计 MCP                                 | `net`         |
| [nature-skills](https://github.com/Yuan1z0825/nature-skills)                                  | 29.4k |   9 | 一个精炼的九 skill 套件，最强在 Nature 风格的行文与配图，最弱在作为数据工具集                                                                                                     | `net`         |
| [open-scholar-skill](https://github.com/joshzyj/open-scholar-skill)                           |   102 |   — | 面向顶刊的社会科学论文套件：分析能力可产出可直接发表的回归表格/图（NHANES/IPUMS/GSS）、文献综合、因果设计、引用。端到端覆盖面广；非商业许可，且带一处自引导向                                                            | `net`         |
| [papercash](https://github.com/jesseovo/papercash)                                            |    87 |   — | 面向中国学生、覆盖 8 个免费来源（S2、arXiv、Crossref、PubMed、CNKI、万方、百度/Google Scholar）的端到端论文工作流：检索、综述、润色、查重预检、降 AI 率、GB/T 7714 参考文献。覆盖广，但每个环节都偏浅                    | `net` `hooks` |
| [posit-dev/skills](https://github.com/posit-dev/skills)                                       |   438 |   — | 出自 RStudio 团队的 Posit 官方 R / Quarto / tidyverse skill——当分析建立在 R 而非 Python 上时的首选                                                                     | —             |
| [q-skills](https://github.com/tyrealq/q-skills)                                               |    24 |   — | 面向实证研究、含 12 个 skill 的学术工具箱：文献综述、R 与 Stata 分析、可复现研究脚手架、问卷设计、基金申请书写作、同行评议与参考文献。对定量社会科学很强；重广度而非深度                                                     | —             |
| [research-agora](https://github.com/rpatrik96/research-agora)                                 |    14 |   — | 面向 ML 研究者的套件，覆盖文献检索、论文写作、引用核验、实验追踪、LaTeX 自动化、基准测试与同行评审。实验追踪与基准测试这一切入点是它的长处；覆盖面广也意味着各项深度只属中等                                                        | `net` `hooks` |
| [researchclaw](https://github.com/alphalab-ustc/researchclaw)                                 |   130 |   — | 端到端的 OpenClaw 研究伴侣（六项能力，含 arXiv 检索、阅读、写作），无需 API key 并附带在线 demo，来自 USTC 的一个实验室。工作流覆盖面广；仓库里残留的 SKILL.md.bak 暗示其清理略显粗放                               | —             |
| [scholaraio](https://github.com/zimoliao/scholaraio)                                          |   550 |   — | 模块化的一体式研究套件（47 个技能）：文献检索、引用管理、PDF 解析与写作支持，设计上可自由组合。是一套深度中等、尚算合理的通用骨架；注意它附带一个 SSH 备份功能和一个需要审查的 hook                                                 | `net` `hooks` |
| [sciclaw](https://github.com/drpedapati/sciclaw)                                              |    85 |   — | 一套"结对科学家"式的研究套件（23 个 skill），封装在轻量的 Go runtime 中，注入生命周期 hook、稿件主干结构与运行日志，使每次会话都可复现、有记录、可引用                                                          | `net` `hooks` |
| [scienceclaw](https://github.com/zaoqu-liu/scienceclaw)                                       |    57 |   — | 端到端研究套件（275 个 skill、9 个 agent、77 个数据库），覆盖文献检索到发表。单一仓库内野心勃勃、覆盖面极广，但质量参差，且附带一个聊天机器人通道、hook 与一个 tools 通配符，值得先行审查                                      | `net` `hooks` |
| [scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills)              | 31.1k | 142 | 体量最大的计算科学套件——对生命科学实验室极深入，对人文学科几乎无用                                                                                                                 | `net`         |
| [scientific-research-skills](https://github.com/jxtse/scientific-research-skills)             |    58 |   — | 方法学优先的 agent 研究技能：文献检索、三种深度的论文阅读、全文获取、related-work 综述、Zotero 管理与可发表配图生成。沉淀的是工作流经验，而非单薄的工具封装                                                        | `net`         |
| [voidful/academic-skills](https://github.com/voidful/academic-skills)                         |   105 |   8 | 精简而主张鲜明、带 CS/ML 气质的研究生流水线，可在 Claude Code、Codex 与 Gemini 上运行                                                                                        | —             |
| [xueshuzhi-skills](https://github.com/yipng05-max/-skills)                                    |   245 |   — | 覆盖面很广的中文学术套件：选题、研究设计、CNKI/外文文献检索与核验、主题编码、综述与学位论文撰写，外加一条 12 检查点的 TA 流水线来拼装 Word 初稿。重广度而非深度                                                          | `net`         |

### 自主研究系统

> 端到端的研究 agent——给它一个问题，拿回一份检索过、读过、并附引用的成稿。

#### 全自主 AI 科学家

- `Suite` [ARIS (Auto-Research-In-Sleep)](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep) - 作者 [Yang Ruofeng](https://github.com/wanshuiyin) · `MIT` · `net` `hooks`.<br>一个自主科研循环，标志性设计是跨模型陪审团——Claude、GPT 与 Gemini 互相批判，使任何模型都无法为自己盖橡皮图章。
- `Suite` [autodidact-skill](https://github.com/damonchen-anan/autodidact-skill) - 作者 [damonchen-anan](https://github.com/damonchen-anan) · `MIT`.<br>在 Karpathy 的 LLM-Wiki 基础上扩展的自主"主题转 wiki"研究 agent：自动抓取网络来源，编纂出相互链接的 wiki，并在每一轮自查覆盖盲区。适合无人值守地搭建文献框架；但不是用于核验引用的工具。
- `Suite` [autoresearch-skill](https://github.com/wjgoarxiv/autoresearch-skill) - 作者 [wjgoarxiv](https://github.com/wjgoarxiv) · `MIT` · `net`.<br>把自然语言写的 research.md 目标转化为 Karpathy 式的「实验—评估—迭代」循环，并从 ML 推广到任何有机械化评估器的任务，配有自动回滚、审计轨迹与安全预算。领域通用；文献能力有限。
- `Suite` [de-anthropocentric-research-engine](https://github.com/yogsoth-ai/de-anthropocentric-research-engine) - 作者 [yogsoth-ai](https://github.com/yogsoth-ai) · `Apache-2.0`.<br>庞大的纯 markdown 自主研究 SOP 库（约 770 个技能），按 Campaign/Strategy/Tactic/SOP 层级组织，覆盖方向设定、文献获取、空白发现、假设形成与对抗式压力测试。
- `Suite` [nano-scientist](https://github.com/ai4scientist/nano-scientist) - 作者 [ai4scientist](https://github.com/ai4scientist) · `No License` · `net` `hooks`.<br>自主研究 agent：通过四个有预算上限的循环（深度检索、实验、改进、评审）把一个选题变成完整的论文初稿，配 CrossRef 引用补全和多模型评审关卡。强大且模块化（含 87+ 研究技能）。
- `Suite` [rstack](https://github.com/sunnnybala/rstack) - 作者 [sunnnybala](https://github.com/sunnnybala) · `MIT` · `net`.<br>一条研究自动化链：/research 在一次会话内依次执行文献综述→新颖性核查→实验→结果分析→论文撰写，直至产出可投稿的草稿；其中每个 skill 也能独立使用。端到端的雄心之作；但成品质量取决于实验这一环。

#### 人在回路 / 门控流程

- `Suite` [academic-research-agent-skill](https://github.com/ngtiendong/academic-research-agent-skill) - 作者 [ngtiendong](https://github.com/ngtiendong) · `MIT`.<br>面向 CS/AI/数学/工科硕博的人在回路（human-in-the-loop）研究工作流：界定问题、把文献综述锚定到真实来源、先过一道新颖性闸门，再规划实验、模拟审稿人、核验论断。是讲纪律的协作，不是一键代劳。
- `Suite` [anaxa](https://github.com/citrus-bit/anaxa) - 作者 [citrus-bit](https://github.com/citrus-bit) · `MIT` · `net`.<br>可审计、可暂停的研究 agent 工作台：把一个选题依次推过文献检索、证据绑定、沙箱实验、初稿与引用审计，最终产出带人工闸门的 LaTeX/PDF 成品包。是重型全栈应用，而非即插即用的 skill。
- `Suite` [phd-skills](https://github.com/fcakyon/phd-skills) - 作者 [fcakyon](https://github.com/fcakyon) · `MIT` · `net` `hooks`.<br>面向博士/ML 研究的护栏：复现 arXiv 论文、以证据为先地调试实验、在同一 epoch 下对比实验、审查数据集偏差、运行启动前的预检。能拦下代价高昂的 AI 研究错误；使用了一个 Bash 通配符外加可选的告警。
- `Suite` [research-units-pipeline-skills](https://github.com/willoscar/research-units-pipeline-skills) - 作者 [willoscar](https://github.com/willoscar) · `No License` · `net`.<br>以文件为先的研究 harness，把开放式目标转化为流程化、可续跑的 pipeline（文献调查、论文评审、证据综合），各阶段设有验收 gate 并产出持久化 artifact。机制厚重；学习曲线陡峭；目前尚无 LICENSE 文件。
- `Plugin` [vibe-science](https://github.com/th3vib3coder/vibe-science) - 作者 [th3vib3coder](https://github.com/th3vib3coder) · `Apache-2.0` · `net` `hooks`.<br>以诚信为先的 Claude Code 研究运行时：一个强制执行检查并持久化状态的 plugin，外加一个建立在可证伪性、对抗式评审与混杂因素纪律之上的方法学 skill。目标是让 AI 做科学难以造假；执行开销较重。

#### 领域专用自主系统

- `Suite` [ai-research-army](https://github.com/terryfyl/ai-research-army) - 作者 [terryfyl](https://github.com/terryfyl) · `Apache-2.0` · `net`.<br>九个 agent 组成的流水线，把临床数据一路推到可投稿的医学稿件——需求界定、数据画像、统计、绘图、文献、撰写、投稿打包。端到端的野心十足；部分模块只是部分公开发布。
- `Suite` [claude-workflow-for-econ-phd](https://github.com/saptarsibhowmick/claude-workflow-for-econ-phd) - 作者 [saptarsibhowmick](https://github.com/saptarsibhowmick) · `MIT` · `net` `hooks`.<br>面向多篇论文的实证经济学博士工作、可直接 fork 的脚手架（从文献综述到投稿）：9 个 skill（missing-lit、referee2、blindspot）、一条基于 Zotero 的 PDF 分块文献流水线，以及文件安全与 IRB 处理。是供人采纳的脚手架，而非即插即用。
- `Suite` [neurico](https://github.com/chicagohai/neurico) - 作者 [chicagohai](https://github.com/chicagohai) · `Apache-2.0` · `net`.<br>给它一个结构化假设，它就跑完实验循环，并产出代码、图表和一篇 LaTeX 论文。由实验室打造、确有学术性，但偏重（需 git+docker），其上限取决于背后的领域测评框架。
- `Suite` [scienceclaw](https://github.com/beita6969/scienceclaw) - 作者 [beita6969](https://github.com/beita6969) · `MIT` · `net`.<br>一个大型自演化研究 agent 平台（基于 OpenClaw）：横跨 28+ 个学科的 285 个 skill，配有持久化记忆和以 API 为依据的引用。在端到端研究 agent 领域颇受欢迎；但内置了一整套消息/浏览器/沙箱式的“操作系统”，使用前务必先读懂再信任。

### 学科专用包

> 为某一学科的惯例量身打造的技能——实验生物学、临床、社会科学或人文领域的工作流。

#### 生物医学与生命科学

- `Suite` [alterlab-academic-skills](https://github.com/alterlab-ieu/alterlab-academic-skills) - 作者 [alterlab-ieu](https://github.com/alterlab-ieu) · `MIT` · `net`.<br>面向教师/研究人员的 186+ 个按领域组织的学术 skill，封装了真实的科研数据库与库（ENA、biopython、cellxgene、cobrapy、ESM 等）。在生物信息学/计算科学的覆盖广度上很强。
- `Suite` [beril-research-observatory](https://github.com/kbaseincubator/beril-research-observatory) - 作者 [kbaseincubator](https://github.com/kbaseincubator) · `AGPL-3.0` · `net`.<br>架设在 BER 微生物生态数据湖仓之上的 KBase AI 协作科学家：16 个 skill 外加用于泛基因组学、适应度、宏基因组学与生物化学的可复用范式。对 KBase 研究很强；可执行面较大且采用 AGPL，信任前请先通读。
- `Suite` [bioSkills](https://github.com/GPTomics/bioSkills) - 作者 [GPTomics](https://github.com/GPTomics) · `MIT`.<br>基准测试最坦诚的生物信息学套件——地道的 samtools/DESeq2/Seurat 代码，并公布了 Bio-Task Bench 成绩。
- `Suite` [clawbio](https://github.com/clawbio/clawbio) - 作者 [clawbio](https://github.com/clawbio) · `MIT` · `net`.<br>生物信息学原生的 agent skill 库：基于 OpenClaw 构建的本地优先、可复现的基因组学/QC/GWAS 工作流，配有 CI 与可被引用的发布版本。领域覆盖扎实；可执行面较大，这是真实生物信息学技术栈的常态。
- `Suite` [dr-cook](https://github.com/wen-chen/dr-cook) - 作者 [wen-chen](https://github.com/wen-chen) · `MIT`.<br>模块化的研究全生命周期套件（文献、空白分析、写作、同行评审、生物信息学、基金申请），带路由层，并在中医药领域有深度积累。在中医/生物医学场景下很强；采用度一般，主打面面俱到的广度。
- `Suite` [encode-toolkit](https://github.com/ammawla/encode-toolkit) - 作者 [ammawla](https://github.com/ammawla) · `AGPL-3.0` · `net`.<br>基因组学套件：检索 ENCODE，交叉比对 14 个数据库（GWAS、ClinVar、GTEx、JASPAR），运行 7 条 pipeline，并撰写带 provenance 追踪的 methods。测试充分；AGPL 且专攻基因组学，在其他领域较为小众。
- `Suite` [labclaw](https://github.com/wu-yc/labclaw) - 作者 [wu-yc](https://github.com/wu-yc) · `No License` · `net`.<br>大型实验科学技能库（240 个 SKILL.md，覆盖生物、制药、医学、文献、影像），封装了真实工具：ESM、AlphaFold DB、biopython、单细胞工具栈，用于干实验推理与实验方案编排。
- `Suite` [medical-research-skills](https://github.com/aipoch/medical-research-skills) - 作者 [aipoch](https://github.com/aipoch) · `MIT`.<br>500+ 技能的医学研究套件：RNA-seq/scRNA/空间组学分析、ADMET、证据图谱，以及完整的稿件写作线。天然地广而不均，但在生物医学数据分析上的深度在此无出其右。
- `Suite` [medsci-agent](https://github.com/omar-a-hassan/medsci-agent) - 作者 [omar-a-hassan](https://github.com/omar-a-hassan) · `MIT` · `net`.<br>面向生物医学研究的 17 个 skill 套件：多源文献检索、ClinicalTrials.gov、药物相互作用，以及一套基因组学工具栈（基因查询、经 ClinVar/dbSNP/gnomAD 的变异注释、通路分析）。领域覆盖很深。
- `Suite` [medsci-skills](https://github.com/aperivue/medsci-skills) - 作者 [aperivue](https://github.com/aperivue) · `NOASSERTION` · `net`.<br>由一位临床研究型医师打造、含 34 个 skill 的医学研究套件：PubMed 检索、研究设计、IRB 方案、生物统计、PRISMA/STROBE/TRIPOD 报告核查、绘图与稿件撰写。覆盖广、偏临床；许可证为 NOASSERTION。
- `Suite` [neuroclaw](https://github.com/cuhk-aim-group/neuroclaw) - 作者 [cuhk-aim-group](https://github.com/cuhk-aim-group) · `MIT` · `net`.<br>来自 CUHK AIM 团队的神经科学与医学影像 skill 包（87 个 skill）：连接组分析、fMRI/EEG 流水线、神经影像统计以及临床数据工作流。
- `Suite` [OpenClaw-Medical-Skills](https://github.com/FreedomIntelligence/OpenClaw-Medical-Skills) - 作者 [FreedomIntelligence](https://github.com/FreedomIntelligence) · `No License` · `net`.<br>最大的开放医学研究 skill 库（数百个 skill）——覆盖很广，但体量巨大、无法逐一审查、且无许可证。
- `Suite` [protein-design-skills](https://github.com/adaptyvbio/protein-design-skills) - 作者 [Adaptyv Bio](https://github.com/adaptyvbio) · `MIT`.<br>专精而深入的蛋白质设计，把 BoltzGen、Chai 与质控自动串成一条流水线；需要真实的算力后端。
- `Suite` [SciAgent-Skills](https://github.com/jaechang-hits/SciAgent-Skills) - 作者 [jaechang-hits](https://github.com/jaechang-hits) · `CC-BY-4.0`.<br>最大的开放生命科学 skill 库（199 个 skill），据称将 BixBench 成绩从 65% 提到 92%；风险低，但体量过大、无法完整审查。
- `Suite` [skillfoundry](https://github.com/ma-compbio-lab/skillfoundry) - 作者 [ma-compbio-lab](https://github.com/ma-compbio-lab) · `Apache-2.0` · `net`.<br>面向计算生物学的学科包：260+ 个 skill 封装了标准的生物信息学工作流（用 DESeq2/Salmon 做 RNA-seq、GATK 变异检测、ChIP/ATAC-seq、单细胞 QC 与整合、空间转录组、MaxQuant 蛋白质组、IQ-TREE 系统发育……）。

#### 物理、计算与数学科学

- `Suite` [automcm-pro](https://github.com/realseaberry/automcm-pro) - 作者 [realseaberry](https://github.com/realseaberry) · `MIT` · `net`.<br>端到端的数学建模竞赛助手（CUMCM/MCM）：贯通文献检索、推导、代码、LaTeX 与论文写作，并强制进行代码自我验证。在建模竞赛场景下很强；专为竞赛设计、以中文为先。
- `Suite` [mathmodel-skill](https://github.com/yushui2022/mathmodel-skill) - 作者 [yushui2022](https://github.com/yushui2022) · `No License` · `net`.<br>面向数学建模竞赛的 agent 原生工作流（10 个技能）：解析题目、选定模型路线、生成并运行代码、以真实证据设卡，再撰写并 Word 排版整篇论文且做格式检查。为 CUMCM 类竞赛打造；使用 eval/exec。
- `Suite` [scp](https://github.com/internscience/scp) - 作者 [internscience](https://github.com/internscience) · `MIT` · `net`.<br>200+ 个计算科学 skill（物理、化学、材料、数值方法、HPC），封装了 ASE 等真实仿真工具。这是一个面向实验/仿真科学而非文献工作的学科包；覆盖广、构建干净。

#### 计算机、AI / ML 与图形学

- `Suite` [agent-research-skills](https://github.com/lingzhi227/agent-research-skills) - 作者 [lingzhi227](https://github.com/lingzhi227) · `No License` · `net`.<br>提炼自 17 个 LLM agent 仓库的 31 个全生命周期 skill——广度实用，但未附许可证、略显粗糙。
- `Suite` [awesome-gaussian-skills](https://github.com/jaccen/awesome-gaussian-skills) - 作者 [jaccen](https://github.com/jaccen) · `Apache-2.0` · `net`.<br>面向 3D Gaussian Splatting / NeRF 研究的学科包：含 600+ 方法目录与交互式浏览器，外加论文追踪、CUDA kernel 审查与空间智能问答等 skill。对图形学研究者很强；使用了 Bash 通配符。
- [remote-sensing-research-radar](https://github.com/limi124/remote-sensing-research-radar) - 作者 [limi124](https://github.com/limi124) · `No License`.<br>遥感研究前沿雷达：扫描 arXiv/Papers-with-Code/GitHub/HF 及会议/期刊页面，搜罗地理空间 AI 与可迁移 CV 方向的工作，按新颖性/可复现性/契合度排序，并起草相关工作（related work）表格。题材小众但定位清晰；无 LICENSE。

#### 社会科学

- `Suite` [academic-research-skills (economics)](https://github.com/franklee16/academic-research-skills) - 作者 [franklee16](https://github.com/franklee16) · `No License`.<br>对实证经济学者有用的经济学/社会科学套件，但筛选较粗（存在近似重复的 skill）、且无许可证。
- `Suite` [ai-agent-research-starter-kit](https://github.com/drchronx/ai-agent-research-starter-kit) - 作者 [drchronx](https://github.com/drchronx) · `NOASSERTION` · `net` `hooks`.<br>中文社会科学研究教学包，方法学技能罕见地深入：因果推断（DID/RDD/IV/PSM）、量表开发、理论建构、EEG/ERP 工作，外加文献检索与统计。价值在方法深度；体量很大。
- `Suite` [education-agent-skills](https://github.com/GarethManning/education-agent-skills) - 作者 [Gareth Manning](https://github.com/GarethManning) · `CC-BY-SA-4.0`.<br>最大的教育类套件——165 个循证教学 skill、横跨 20 个领域；本地安装免费，托管版 MCP 设有门槛。
- `Suite` [open-science-skills](https://github.com/scdenney/open-science-skills) - 作者 [scdenney](https://github.com/scdenney) · `NOASSERTION`.<br>一套源自真实方法学文献的社会科学方法套件：联合分析（conjoint）的设计/清洗/诊断、列举实验（list-experiments）、跨国研究设计、方法报告、FAIR 与图表审计。有文献依据；覆盖面广，建议逐个 skill 自行核查。

#### 人文、法律与质性研究

- `Suite` [ai-anthropology-toolkit](https://github.com/mattartzanthro/ai-anthropology-toolkit) - 作者 [mattartzanthro](https://github.com/mattartzanthro) · `NOASSERTION`.<br>面向人类学的质性研究 skill——同行评审、稿件评估、修改策略——将认识论立场当作一项设计参数来对待，而非事后补充。学术性强且具自省意识；使用前请确认其 license 条款。
- `Suite` [claude-skills-journalism](https://github.com/jamditis/claude-skills-journalism) - 作者 [Joe Amditis](https://github.com/jamditis) · `MIT` · `net` `hooks`.<br>面向新闻业的套件，学术内核是 research-toolkit：经 Unpaywall 合法绕过付费墙、网页存档、变更监控。
- `Suite` [tw-research-skills](https://github.com/fw1201/tw-research-skills) - 作者 [fw1201](https://github.com/fw1201) · `No License`.<br>覆盖台湾学术全生命周期的工具包（从研究计划到投稿），长于质性方法（扎根理论、带 Kappa 的内容分析）与 TSSCI/NSC 规范。本地化但普遍适用；请确认 license。
- [genealogy-research](https://github.com/sliday/genealogy-research) - 作者 [sliday](https://github.com/sliday) · `MIT`.<br>将"族谱证明标准"（Genealogical Proof Standard）应用于家族史研究——多语种手写记录识读、证据等级追踪、阴性结果记录、GEDCOM 与 Obsidian 知识库。高度专门化，但方法论上相当严谨。
- [oh-my-hermes-for-legal-researcher](https://github.com/charliehotel/oh-my-hermes-for-legal-researcher) - 作者 [charliehotel](https://github.com/charliehotel) · `Apache-2.0` · `net`.<br>从 Anthropic 的 claude-for-legal 移植而来的美国法律研究方法论：结构化的《联邦公报》摘要、带（verify）标记的网络检索判例，以及可选的免费 CourtListener API 用于核验引用。不依赖付费数据库；仅限美国，并坦诚自身局限。

#### 跨学科 / 多领域包

- `Suite` [awesome-rosetta-skills](https://github.com/xjtulyc/awesome-rosetta-skills) - 作者 [xjtulyc](https://github.com/xjtulyc) · `NOASSERTION` · `net` `hooks`.<br>多学科研究技能库：横跨 24 个领域（从物理到语言学到公共卫生）共 169 个技能，每个都接入了该领域的数据源与方法。在非 CS 学科上覆盖面无出其右；但深度参差，license 为 NOASSERTION。

### 精选列表与生态导览

> agent 技能生态中的其他精选列表与导览图——本索引之外，下一步该往哪儿看。

- `List` [Awesome AI for Economists](https://github.com/hanlulong/awesome-ai-for-economists) - 作者 [Lu Han](https://github.com/hanlulong) · `CC0-1.0`.<br>面向经济学研究与教学的 AI 工具图谱，由 OpenEcon 团队维护。
- `List` [Awesome AI for Science](https://github.com/ai-boost/awesome-ai-for-science) - 作者 [AwesomeGPTS (ai-boost)](https://github.com/ai-boost) · `MIT`.<br>覆盖面更广的 AI4Science 资源图谱（工具、论文、数据集），比技能列表更偏模型与文献。
- `List` [Awesome Scientific Skills](https://github.com/InternScience/Awesome-Scientific-Skills) - 作者 [Intern Science](https://github.com/InternScience) · `MIT`.<br>最接近的活跃同类——一份科研 agent 技能的 awesome 列表；可交叉参考，而非竞争。
- `List` [Awesome-AI-Scientists](https://github.com/tsinghua-fib-lab/Awesome-AI-Scientists) - 作者 [FIB Lab, Tsinghua University](https://github.com/tsinghua-fib-lab) · `MIT`.<br>清华 FIB 实验室《AI 科学家综述》的配套阅读清单——以论文为主的文献图谱。

## 速览

**类型** 每个条目都是 Claude/agent 技能；只有需要区分的类型才加标记—— `Suite` · `Plugin` · `List`。无标记的条目即单个技能。
<br/>
**运行行为** 能力标记是该技能自我披露的行为，不是安全评级：`net` = 会联网；`hooks` = 有生命周期 hook；`bypass` = 需要权限绕过；`⚠ disclosure` = 声明与代码不符。无标记 = 以上皆无。运行任何第三方代码前请自行审查。

| 生命周期阶段   | 分类 | 技能数 |
| -------- | -: | --: |
| 检索与采集    |  2 |  20 |
| 阅读与理解    |  2 |  23 |
| 分析与可视化   |  2 |  24 |
| 写作与润色    |  2 |  52 |
| 评审与发表    |  2 |  25 |
| 套件、系统与生态 |  4 |  79 |
| 合计       | 14 | 223 |

## 最近更新

**academic-research-skills**, **ai-anthropology-toolkit**, **latex-document-skill**, **nature-skills**, **sciclaw**。（链接与描述见上方各生命周期分区。）

## 如何使用本列表

按研究者实际做的事来组织，而非按字母排序。从你当前所处的阶段开始，沿研究生命周期往下走： `检索 → 精读 → 分析 → 写作 → 评审 → 发表`

## 收录标准

*收录。* 开源或源码可得，且有可辨识的许可证；活跃维护，有像样的 README 和一个能跑起来的仓库；对研究者确有用处——解决生命周期里的某个真实任务，而非一个通用套壳；可检视：其行为读得懂、推得明白。

*不收录。* 闭源 SaaS，没有可检视的技能 / agent 层；通用大模型套壳，缺乏面向学术的特定价值；已弃坑或跑不起来的仓库；AI 生成的注水内容，或只是把仓库自己的标语复述一遍的提交。

## 策展、中立性与安全

本列表由部分被收录技能的作者维护；这些技能接受完全相同的披露核验、不享受任何排序优待，并和其他所有条目一样按字母序排列。

<details>
<summary>披露核验如何运作（能力标记意味着什么、不意味着什么）</summary>

<br/>

每个条目都会声明自己的可执行面（联网、hook、权限绕过、工具范围）。一套开放、确定性的脚本（`framework/`）读取仓库、报告它能推断出的能力，并标出任何声明与代码不符之处。全部主张仅此而已：**披露的事实 + 交叉核验——不是安全审计、不是质量评分、没有通过/不通过标签。** 我们刻意移除了早先的「analyzed/listed」严重度判定，因为静态severity猜测误报太多、不可信。是否收录是维护者关于学术价值的人工编辑判断，并公开说明。

**安全说明。** 技能会执行代码——Python、Shell、以及可在生命周期事件上触发的 hook。本列表**不**对它们做安全审计或评级，而是把每个技能**自我披露的行为**——是否联网、是否有 hook、是否需要权限绕过——以能力标记呈现，并用一套开放、可复跑的脚本（`framework/`）拿这些声明去对照代码核验。 **标记是事实，不是安全评级；无标记也不代表「已验证安全」。** 在机构或敏感环境中运行任何技能前请自行审查源码；发现行为不当请见 [SECURITY.md](SECURITY.md) 举报。

</details>

## 参与贡献

欢迎贡献，且大多数收录技能都由其作者自行提交。两种贡献方式（低门槛的 Issue 表单，或一个 YAML pull request）、收录门槛、以及每个条目必须做的安全披露，详见 **CONTRIBUTING.md**。所有提交均由真人完成。另见我们的[行为准则](CODE_OF_CONDUCT.md)。
