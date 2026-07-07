<div align="right">

**English** · [中文](README.zh-CN.md)

</div>

<div align="center">

# Awesome Academic Skills [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

<br/>

**The research lifecycle, as agent skills.**
<br/>
A bilingual index of Claude and agent skills for academic work, from literature search to peer review.<br/>
Organized by where skills fit in the research lifecycle; each entry notes its license and what it runs (network, hooks).
<br/>

![Skills](https://img.shields.io/badge/skills-223-000?style=flat-square)
![Categories](https://img.shields.io/badge/categories-14-000?style=flat-square)
![Updated](https://img.shields.io/badge/updated-2026.07.07-000?style=flat-square)
![License](https://img.shields.io/badge/license-CC0--1.0-000?style=flat-square)

</div>

<br/>

## Contents

- [Discover & Collect](#discover--collect)
  - [Literature Search & Discovery](#literature-search--discovery)
  - [Reference & Citation Management](#reference--citation-management)
- [Read & Understand](#read--understand)
  - [Reading, Summarization & Q&A](#reading-summarization--qa)
  - [PDF / OCR / Document Parsing](#pdf--ocr--document-parsing)
- [Analyze & Visualize](#analyze--visualize)
  - [Data Analysis & Statistics](#data-analysis--statistics)
  - [Figures & Visualization](#figures--visualization)
- [Write & Refine](#write--refine)
  - [Academic Writing & Drafting](#academic-writing--drafting)
  - [Writing Quality & De-AI](#writing-quality--de-ai)
- [Review & Publish](#review--publish)
  - [Peer Review & Response](#peer-review--response)
  - [Submission, Formatting & Conversion](#submission-formatting--conversion)
- [Suites, Systems & Meta](#suites-systems--meta)
  - [Skill Suites](#skill-suites)
  - [Autonomous Research Systems](#autonomous-research-systems)
  - [Discipline-Specific Packs](#discipline-specific-packs)
  - [Awesome Lists & Ecosystem Maps](#awesome-lists--ecosystem-maps)
- [At a glance](#at-a-glance)
- [Recently updated](#recently-updated)
- [How to use this list](#how-to-use-this-list)
- [What gets listed](#what-gets-listed)
- [Curation, neutrality & security](#curation-neutrality--security)

## Discover & Collect

> Turn a research question into an organized, reference-clean reading set.

### Literature Search & Discovery

> Find, scope, and gather the literature — multi-source search, citation graphs, and discovery agents that turn a topic into a reading list.

#### Multi-source discovery search

- `Suite` [arxiv-skills](https://github.com/ultimatile/arxiv-skills) - by [ultimatile](https://github.com/ultimatile) · `MIT` · `net`.<br>Pair of arXiv skills: convert a paper (LaTeX-source-first, PDF fallback) into implementation-ready Markdown with preserved math, plus a lightweight arXiv API DOI/title-search lookup. Conversion quality hinges on pandoc.
- `Suite` [cnki-skills](https://github.com/cookjohn/cnki-skills) - by [cookjohn](https://github.com/cookjohn) · `No License` · `net`.<br>Drives CNKI (China's main academic database) from Claude Code via Chrome DevTools MCP: search, journal browse, citation analysis, PDF download, BibTeX/Zotero export. Go-to for Chinese-language lit work; needs browser-MCP setup and ships no license.
- `Suite` [gs-skills](https://github.com/cookjohn/gs-skills) - by [cookjohn](https://github.com/cookjohn) · `MIT` · `net`.<br>A genuinely useful Google Scholar toolkit for the CLI: keyword/advanced search, citation-chain tracking, full-text link resolution and one-step Zotero export. Relies on Chrome DevTools MCP and scrapes the DOM, so it can break when Scholar changes.
- `Suite` [scientific-skills](https://github.com/yorkeccak/scientific-skills) - by [yorkeccak](https://github.com/yorkeccak) · `MIT` · `net`.<br>Natural-language literature search over 13 sources (PubMed, arXiv, bioRxiv/medRxiv, ChEMBL, DrugBank, Open Targets, trials, patents) via Valyu semantic search. Strong biomedical/drug-discovery coverage; depends on the Valyu API, not self-contained.
- [ai-skill-scholar](https://github.com/dsebastien/ai-skill-scholar) - by [Sébastien Dubois (dsebastien)](https://github.com/dsebastien) · `MIT` · `net`.<br>Three composable OpenAlex skills (venue search, citation-graph walk, review orchestrator) — stdlib-only, no pip, no key.
- [asta-skill](https://github.com/agents365-ai/asta-skill) - by [agents365-ai](https://github.com/agents365-ai) · `MIT`.<br>Instruction-pack skill that drives Ai2's Asta MCP (Semantic Scholar): keyword/ID/author search, citation traversal, batch lookup and ~500-word snippet retrieval, with safe defaults. Clean routing; needs the Asta MCP + free API key.
- [paper-search-pro](https://github.com/O0000-code/paper-search-pro) - by [O0000-code](https://github.com/O0000-code) · `Apache-2.0` · `net`.<br>OpenAlex-led five-source search (PubMed, arXiv, Semantic Scholar, CrossRef) across four depth tiers; goes past a hit list to a saturation curve, a stop decision, and an interactive HTML report. No LLM key; one free OpenAlex key to start.
- [scholar-kit](https://github.com/lottshin/scholar-kit) - by [lottshin](https://github.com/lottshin) · `MIT` · `net`.<br>Chinese-first literature toolkit: search CNKI/OpenAlex/Semantic Scholar/arXiv/NSSD, enrich via Crossref, resolve OA via Unpaywall, batch-download (incl. CNKI PDFs), export GB/T 7714/BibTeX/RIS/APA. Strong CNKI; scraping is fragile + ToS-sensitive.
- [semanticscholar-skill](https://github.com/agents365-ai/semanticscholar-skill) - by [agents365-ai](https://github.com/agents365-ai) · `MIT` · `net`.<br>Wraps the Semantic Scholar Graph API for paper search, citation-graph traversal, and author lookup across 200M+ papers, rate-limited for multi-agent use. A reliable discovery building block; intentionally narrow (S2 only), so pair it with others.

#### Systematic review & deep-research pipelines

- `Suite` [literature-review-skill](https://github.com/yanzhanlin/literature-review-skill) - by [yanzhanlin](https://github.com/yanzhanlin) · `MIT`.<br>End-to-end lit-review suite (search, acquire, deep-read, write, dissertation chapter) built on PRISMA-S, PICO/SPIDER and named review-methodology frameworks. Strong grounding and reproducible search logs; Chinese-first, modest in stars.
- [litreviewskill](https://github.com/zsun79/litreviewskill) - by [zsun79](https://github.com/zsun79) · `No License` · `net`.<br>End-to-end literature-review workflow: drafts keywords, builds an OpenAlex seed set, expands by backward/forward citations, screens by title/abstract until saturation, then ranks and reads up to 30 full texts into a concept matrix.
- [oneshot-academic-research-skill](https://github.com/orhoncan/oneshot-academic-research-skill) - by [orhoncan](https://github.com/orhoncan) · `MIT`.<br>Iterative deep-literature-research skill: 5-15 search cycles gathering 12-50+ sources with gap identification, source-diversity tracking and APA7 footnotes, to Obsidian or PDF. Turkish/English auto-detect; depth depends on the underlying web tools.
- [scholar-deep-research](https://github.com/agents365-ai/scholar-deep-research) - by [agents365-ai](https://github.com/agents365-ai) · `MIT` · `net`.<br>Script-driven 8-phase literature-review pipeline over 7 federated sources with enforced citation anchoring, dedup, transparent ranking, citation-chasing and a mandatory self-critique gate.

#### Full-text acquisition

- [literature-harvest](https://github.com/zhongzhx/literature-harvest) - by [zhongzhx](https://github.com/zhongzhx) · `MIT` · `net`.<br>Bulk keyword-driven literature harvesting across PubMed, Europe PMC, Crossref and OpenAlex: builds a candidate table, downloads legally-accessible full-text PDFs with an HTML-to-PDF second pass, and dedups.
- [paper-fetch](https://github.com/agents365-ai/paper-fetch) - by [agents365-ai](https://github.com/agents365-ai) · `MIT` · `net`.<br>Resolves a DOI (or batch) to a downloadable PDF via a 7-source fallback chain (Unpaywall, Semantic Scholar, arXiv, PMC, bioRxiv, publisher, then Sci-Hub) with per-source reporting. Clean and zero-deps; the Sci-Hub fallback is a caveat.

### Reference & Citation Management

> Manage, format, and verify references — library integrations, citation styles, and the DOI/metadata checks that keep a bibliography honest.

#### Reference formatting & style

- [apa-referencing-skill](https://github.com/keemanxp/apa-referencing-skill) - by [Chuah Kee Man (keemanxp)](https://github.com/keemanxp) · `No License` · `net`.<br>The most complete APA-7th formatter: 28 source types, down to tweets and datasets. Ships no open-source license.
- [chinese-reference-formatter-skill](https://github.com/zechang-xiong/chinese-reference-formatter-skill) - by [zechang-xiong](https://github.com/zechang-xiong) · `MIT`.<br>Formats Chinese academic references to GB/T 7714 and completes BibTeX from Chinese/English titles. Fills a real gap for CN scholars that Western citation tools ignore. Narrow by design; bundles helper scripts and an agent.

#### BibTeX / metadata generation

- [citation-assistant](https://github.com/zhangny301/citation-assistant) - by [zhangny301](https://github.com/zhangny301) · `No License` · `net`.<br>Automated academic-citation skill over the Semantic Scholar API: resolve, verify, and format citations into a manuscript. Useful, focused citation helper; single-skill and tied to S2 coverage, and its license needs confirming.
- [make-bib](https://github.com/milkclouds/make-bib) - by [milkclouds](https://github.com/milkclouds) · `No License` · `net`.<br>Human-in-the-loop BibTeX fetcher pulling every field from the authoritative publisher (ACL/PMLR/arXiv/NeurIPS, DBLP fallback) not the LLM, with provenance per entry and a stop-to-ask on ambiguous venues. Great for de-hallucinating .bib; no license.
- [wenxian](https://github.com/njzjz/wenxian) - by [njzjz](https://github.com/njzjz) · `LGPL-3.0` · `net`.<br>Generates BibTeX from a DOI, PMID, arXiv ID, or paper title by querying CrossRef, PubMed, arXiv, Semantic Scholar and ChemRxiv. Mature, tested, PyPI-published; the agent skill is a thin wrapper over a solid CLI. LGPL-3.0.

## Read & Understand

> Turn a pile of PDFs into something you have actually read and can question.

### Reading, Summarization & Q&A

> Read deeply and ask questions of papers — summarization, multi-document synthesis, and grounded question-answering over a corpus.

#### Deep reading & comprehension

- `Suite` [dailypaper-skills](https://github.com/huangkiki/dailypaper-skills) - by [huangkiki](https://github.com/huangkiki) · `Apache-2.0` · `net`.<br>A daily paper-reading pipeline built from Agent Skills: arXiv search, PDF parsing, key-point extraction, Zotero sync, and structured notes plus a daily digest. Cohesive and popular; Chinese-first docs, so non-CJK users lean on the code.
- `Suite` [scholar-skill](https://github.com/eesjgong/scholar-skill) - by [eesjgong](https://github.com/eesjgong) · `MIT` · `net`.<br>Obsidian-centric academic-reading suite: deep-reads papers and links them into an evolving personal knowledge base with reflection prompts. A strong pick for Obsidian users; it reads and organizes rather than discovering papers.
- [benchmark-research-skill](https://github.com/eternalwavee/benchmark-research-skill) - by [eternalwavee](https://github.com/eternalwavee) · `MIT` · `net`.<br>Extracts benchmarks, datasets, metrics and baselines from a paper, or surveys what benchmarks fit a research direction; arXiv-source-first with Obsidian notes. Uses an unscoped Bash(*) allowlist — broad shell access.
- `Plugin` [claude-paper](https://github.com/alaliqing/claude-paper) - by [alaliqing](https://github.com/alaliqing) · `MIT` · `net` `hooks`.<br>Paper-study plugin that turns a PDF or arXiv link into a learning environment: parsed text, adaptive summaries/Q&A, runnable code demos and a KaTeX web viewer. Rich but heavy (Node/Nuxt/poppler deps); uses an unscoped Bash allowlist.
- [deeppapernote](https://github.com/917dhj/deeppapernote) - by [917dhj](https://github.com/917dhj) · `MIT` · `net`.<br>Deep-reads a single paper and produces high-quality, structured Obsidian-style research notes (claims, methods, takeaways) usable across Claude Code/Codex/Cursor. Great for building a notes vault; one-paper-at-a-time, not corpus-scale.
- [paper-analyst](https://github.com/flyer-li/paper-analyst) - by [flyer-li](https://github.com/flyer-li) · `MIT`.<br>Analyzes a paper in five depth modes (quick to presentation-with-figures) with anti-hallucination source tagging and method extraction tuned to paper type. Good for structured reading/summaries; single-skill, no external data sources of its own.
- [paper-reader-heilmeier](https://github.com/realzyzhang/paper-reader-heilmeier) - by [realzyzhang](https://github.com/realzyzhang) · `MIT`.<br>Reads STEM papers through Heilmeier's Catechism, surfacing the core problem, approach, cost and impact for a fast big-picture take. A focused, opinionated comprehension aid; great for triaging papers, less so for deep line-by-line reading.
- [paper-reading-skill](https://github.com/kingslayer-bot/paper-reading-skill) - by [kingslayer-bot](https://github.com/kingslayer-bot) · `MIT`.<br>Deep paper-reading skill with two modes: paragraph-level close reading with agentic Q&A, and a 20+-dimension analysis run by parallel agents, emitting Obsidian-ready notes. Strong for deconstructing single papers; not a search or citation tool.

#### Grounded Q&A & knowledge bases

- [Claude Deep Research Skill](https://github.com/199-biotechnologies/claude-deep-research-skill) - by [199 Longevity (199-biotechnologies)](https://github.com/199-biotechnologies) · `No License` · `net`.<br>The most engineering-heavy deep-research skill — verifies each claim against its source via CrossRef and persists citations across compaction. No license file.
- [Deep Research Skill](https://github.com/Weizhena/Deep-Research-skills) - by [Lan Zheng](https://github.com/Weizhena) · `MIT` · `net`.<br>Two-phase deep research that gates on your approval of the outline before any search runs — the human-in-the-loop answer to fire-and-forget agents.
- `Plugin` [llm-wiki](https://github.com/nvk/llm-wiki) - by [nvk](https://github.com/nvk) · `MIT` · `net`.<br>LLM-compiled knowledge bases for agents: parallel multi-agent research, thesis-driven investigation, source ingestion, then a queryable wiki. Good for building a durable, cited knowledge base from many sources.
- [NotebookLM Research Skill](https://github.com/claude-world/notebooklm-skill) - by [Claude-World](https://github.com/claude-world) · `MIT` · `net`.<br>Drives Google NotebookLM from Claude for cited answers and free artifacts (podcast, mind map, study guide) — an unofficial cookie-based client that can break.
- [notebooklm-skill](https://github.com/pleaseprompto/notebooklm-skill) - by [pleaseprompto](https://github.com/pleaseprompto) · `MIT`.<br>Bridges Claude Code to Google NotebookLM so you get source-grounded, citation-backed answers drawn only from your uploaded documents. Excellent for grounded Q&A over a personal corpus; depends on a Google NotebookLM account and the notebooklm-mcp.

#### Paper translation

- [arxiv-paper-zh](https://github.com/zeya-labs/arxiv-paper-zh) - by [zeya-labs](https://github.com/zeya-labs) · `MIT` · `net`.<br>Translates arXiv LaTeX papers into Chinese while preserving formatting (formulas, figures, citations), from an arXiv ID or local source. The format-preserving approach beats plain-text translation; scope is narrow (arXiv LaTeX, EN to zh).

#### Study & derivative artifacts

- [cheatsheet-generator-skill](https://github.com/evan715823/cheatsheet-generator-skill) - by [evan715823](https://github.com/evan715823) · `MIT` · `net`.<br>Turns course slides and PDFs into dense, exam-ready LaTeX cheatsheets. Narrow and student-focused (study/teaching rather than original research), but well-targeted and popular; good for condensing course material, not for literature work.
- [lecture-to-notes](https://github.com/ysyecust/lecture-to-notes) - by [ysyecust](https://github.com/ysyecust) · `NOASSERTION`.<br>Turns YouTube/Bilibili lecture videos into structured LaTeX/PDF notes via transcript extraction, key-frame detection, and smart-cropped screenshots. Novel and useful for students; quality depends on transcript availability, and the license is murky.
- [paper2code](https://github.com/prathamlearnstocode/paper2code) - by [prathamlearnstocode](https://github.com/prathamlearnstocode) · `MIT` · `net`.<br>arXiv ID in, citation-anchored Python implementation out — each module tagged to the paper section it implements, ambiguities flagged rather than guessed. Great for paper reproduction; not a general code generator.

### PDF / OCR / Document Parsing

> Turn PDFs, scans, and office docs into clean, LLM-ready structure — layout-aware parsing, tables, formulas, and figures preserved.

- [auto-paper-harvester](https://github.com/jxtse/auto-paper-harvester) - by [jxtse](https://github.com/jxtse) · `No License` · `net`.<br>Batch-downloads paper PDFs by DOI, cascading publisher TDM APIs (Wiley/Elsevier/Springer) to OA sources (Crossref/OpenAlex/Unpaywall) to an optional browser fallback on an institutional session. Good for bulk retrieval; ships a hardcoded credential.
- [DOCX (Anthropic document skill)](https://github.com/anthropics/skills/tree/main/skills/docx) - by [Anthropic](https://github.com/anthropics) · `Proprietary`.<br>Anthropic's Word skill whose academic edge is first-class tracked changes and comments — the best off-the-shelf option for revising a marked-up manuscript.
- [mineru-skill](https://github.com/nebutra/mineru-skill) - by [nebutra](https://github.com/nebutra) · `MIT` · `net`.<br>Parses PDFs, Office docs and images into clean Markdown with LaTeX formulas, tables and OCR via MinerU. A solid OCR/extraction entry point for getting papers into editable text.
- [PDF (Anthropic document skill)](https://github.com/anthropics/skills/tree/main/skills/pdf) - by [Anthropic](https://github.com/anthropics) · `Proprietary`.<br>Anthropic's own PDF skill — a task router over pypdf/pdfplumber/reportlab/qpdf for routine merge/split/extract/forms. The reliable default, not a high-accuracy OCR engine.
- [PPTX (Anthropic document skill)](https://github.com/anthropics/skills/tree/main/skills/pptx) - by [Anthropic](https://github.com/anthropics) · `Proprietary`.<br>Anthropic's PowerPoint skill that builds decks and pulls text from any .pptx — an authoring tool for paper-to-talk, not layout-faithful slide OCR.
- [XLSX (Anthropic document skill)](https://github.com/anthropics/skills/tree/main/skills/xlsx) - by [Anthropic](https://github.com/anthropics) · `Proprietary`.<br>Anthropic's spreadsheet skill that, unusually, recalculates formulas rather than reading cached values — good for cleaning messy supplementary-data tables.

## Analyze & Visualize

> Do the analysis, then build the journal-grade figures.

### Data Analysis & Statistics

> Run and reason about analyses — statistics, reproducible pipelines, and tools that keep the numbers and the narrative in step.

#### Statistical modeling & test selection

- `Suite` [ai4ss-skills](https://github.com/siyaozheng/ai4ss-skills) - by [siyaozheng](https://github.com/siyaozheng) · `GPL-3.0` · `net`.<br>Agent skills for social-science research in R and Python that persist dataset/codebook context across sessions, with a benchmarks section. Good for reproducible quant social-science analysis; GPL-3.0 and stats-workflow-focused, not writing.
- `Suite` [social-data-analysis](https://github.com/nealcaren/social-data-analysis) - by [nealcaren](https://github.com/nealcaren) · `MIT` · `net`.<br>An 18-skill sociology methods pack covering quantitative and qualitative social-data analysis, authored by a computational sociologist. Scope and provenance are strong; component depth unverified (content not inspected).
- [claude-statistical-analysis-skill](https://github.com/terryfyl/claude-statistical-analysis-skill) - by [terryfyl](https://github.com/terryfyl) · `MIT` · `net`.<br>Statistical-consultant skill that diagnoses assumptions first, auto-selects methods (t-test to SEM/HLM/IRT/meta-analysis) and emits an APA-7 table, 300dpi figure and results paragraph. Assumption-first is its edge; advanced methods need the R Docker.
- [stata-ai-fusion](https://github.com/haoyu-haoyu/stata-ai-fusion) - by [haoyu-haoyu](https://github.com/haoyu-haoyu) · `MIT`.<br>Lets an agent drive a real Stata session (run commands, inspect data, extract estimation results, capture graphs) via an MCP server plus a Stata skill knowledge base. Fills the AI-Stata gap for econ/epi/biostat; requires a licensed Stata install.
- `Plugin` [stata-skill](https://github.com/dylantmoore/stata-skill) - by [Dylan Moore](https://github.com/dylantmoore) · `No License`.<br>The eval-backed reference that stops Claude writing subtly-wrong Stata — the silent traps that run clean but mislead.

#### Causal inference & econometrics

- [econometrics-skill](https://github.com/xiaomihu1992/econometrics-skill) - by [xiaomihu1992](https://github.com/xiaomihu1992) · `MIT`.<br>Applied causal-inference skill: 17 estimators (OLS, PSM/IPW/AIPW, IV/2SLS, DiD/event-study, sharp/fuzzy RDD) with a method-selection decision tree, diagnostics and reporting templates. Solid for tabular econometrics; assumes clean panel data.

#### Domain computational & simulation pipelines

- `Suite` [claude-scientific-skills](https://github.com/k-dense-ai/claude-scientific-skills) - by [k-dense-ai](https://github.com/k-dense-ai) · `MIT`.<br>Sprawling computational-science suite (143 skills): bioinformatics pipelines (alignment, RNA-seq, variant calling, phylogenetics, protein structure, MD) plus a full stats stack (differential expression, pathway/GO, survival, meta-analysis, more).
- `Suite` [fiftyone-skills](https://github.com/voxel51/fiftyone-skills) - by [voxel51](https://github.com/voxel51) · `Apache-2.0` · `net`.<br>Official FiftyOne skill suite: expert workflows for computer-vision dataset curation, evaluation and model analysis via AI assistants, with a companion MCP server. Strong for CV/ML dataset research; tied to the FiftyOne tool and CV-specific.
- `Suite` [materials-simulation-skills](https://github.com/heshamfs/materials-simulation-skills) - by [heshamfs](https://github.com/heshamfs) · `Apache-2.0` · `net`.<br>23-skill computational-materials-science suite: numerical-stability analysis, finite-element meshing, DFT/MD setup, Monte-Carlo/phase-field modeling, spectral methods, time-integration, and uncertainty quantification. Strong methodological breadth.
- `Suite` [matlab-agentic-toolkit](https://github.com/matlab/matlab-agentic-toolkit) - by [matlab](https://github.com/matlab) · `No License` · `net`.<br>Official MathWorks toolkit of 61 agent skills for MATLAB/Simulink engineering and scientific work: curve fitting, system identification, timeseries forecasting, signal detrending/filtering, parameter optimization, unit conversion, and data cleaning.
- `Suite` [scienceclaw](https://github.com/lamm-mit/scienceclaw) - by [lamm-mit](https://github.com/lamm-mit) · `Apache-2.0` · `net`.<br>Computational science-and-engineering skill suite (340+ skills) from MIT's LAMM lab: materials science, molecular dynamics, finite-element analysis, symbolic math and multiscale modeling.

#### Reproducible-analysis frameworks

- `Suite` [daaf](https://github.com/daaf-contribution-community/daaf) - by [daaf-contribution-community](https://github.com/daaf-contribution-community) · `LGPL-3.0` · `net` `hooks`.<br>Instruction framework making Claude Code behave like a rigorous, reproducible quantitative researcher in any domain, with auditable steps, guardrails, and human-in-the-loop verification. Heavyweight and opinionated; core decisions stay with the user.

### Figures & Visualization

> Make publication-quality figures — charts, plots, and visual encodings built for journals, not dashboards.

#### Method & concept diagrams

- `Suite` [paper-craft-skills](https://github.com/zsyggg/paper-craft-skills) - by [zsyggg](https://github.com/zsyggg) · `No License`.<br>From an arXiv link to publication-style method figures, AIGC slide decks, and deep-dive explainer articles in one command, no API keys. Strongest at turning paper internals into visuals; output style is opinionated.
- [engineering-figure-agent](https://github.com/heyu-233/engineering-figure-agent) - by [heyu-233](https://github.com/heyu-233) · `MIT` · `net`.<br>Generates publication-style engineering and computer-science figures (diagram and plot modes) with bilingual EN/ZH labeling and editable output, tuned for Chinese academic papers. Narrow but does the figure job well; not a general plotting library.
- [gen-pseudocode-skill](https://github.com/huiyuli-2000/gen-pseudocode-skill) - by [huiyuli-2000](https://github.com/huiyuli-2000) · `MIT`.<br>Reconstructs submit-ready algorithm2e LaTeX pseudocode from a paper's methodology, code, and notes, with a code-to-math map, per-venue style, complexity analysis, and a compile check. Strong for ML/SCI algorithm exhibits; works at the method level.
- [paperbanana-skill](https://github.com/plutolei/paperbanana-skill) - by [plutolei](https://github.com/plutolei) · `MIT` · `net`.<br>Multi-agent pipeline (Retriever→Planner→Stylist) for academic diagrams, methodology figures, statistical plots and slide decks from text/data, plus a figure-vs-reference evaluator. Eight providers; mature (v4.x). Heavyweight for one-off diagrams.
- [research-paper-figure-skill-factory](https://github.com/c-narcissus/research-paper-figure-skill-factory) - by [c-narcissus](https://github.com/c-narcissus) · `MIT-0`.<br>A figure-skill factory: distills one class of paper figure (framework, mechanism, taxonomy, results) into a reusable diagram-generation skill with multi-candidate rounds. Process-heavy and meta; overkill for a single one-off figure.
- [skill-research-figure](https://github.com/chingswy/skill-research-figure) - by [chingswy](https://github.com/chingswy) · `No License`.<br>Draws professional academic figures for papers — LaTeX/TikZ diagrams and hand-drawn-style SVG. Tightly scoped to scholarly figure generation; needs a LICENSE added. Clean static scan; a solid pick for paper figures, especially TikZ.
- [thesis-figure-skill](https://github.com/0xe1337/thesis-figure-skill) - by [0xe1337](https://github.com/0xe1337) · `MIT`.<br>Turns paper text into publication-grade figures: LaTeX/TikZ (pixel-precise, embeddable) or draw.io XML (route maps, slides). Targets high density + one-pass compile; bilingual. Best for structured CS/ML schematics, not data-driven statistical plots.

#### Data-driven statistical plots

- `Plugin` [nice-figures](https://github.com/mapika/nice-figures) - by [mapika](https://github.com/mapika) · `MIT`.<br>Matplotlib figures in a soft-pastel research-blog register: smoothed trends with confidence bands, rounded bars, log-log scaling-law scatter, white background, plus 16 recipes. Great for ML/alignment write-ups; one opinionated aesthetic.
- [stata-graphics-skill](https://github.com/youngfujun/stata-graphics-skill) - by [youngfujun](https://github.com/youngfujun) · `No License`.<br>Knowledge base for AI-assisted Stata graphing aimed at economics empirical research. Narrow but well-targeted for econ publication figures; the main gap is a missing LICENSE. A good companion for Stata-based analysis workflows.

#### Figure aesthetics & style systems

- [AgentFigureGallery](https://github.com/Dsadd4/AgentFigureGallery) - by [Dsadd4](https://github.com/Dsadd4) · `MIT` · `net`.<br>A taste layer, not a plotting library — curated references so the agent stops guessing what a Nature figure looks like.
- [paper-style](https://github.com/freemty/paper-style) - by [freemty](https://github.com/freemty) · `MIT`.<br>Five low-saturation color themes giving a paper one coherent identity across LaTeX text and matplotlib figures (documentclass to savefig), with a preview PDF. Great for consistent palettes; purely a styling layer, not a plotting or layout tool.
- [tufte-data-viz](https://github.com/caylent/tufte-data-viz) - by [caylent](https://github.com/caylent) · `MIT`.<br>Applies Tufte's data-viz principles (high data-ink ratio, no chartjunk, no pie charts) across six charting libraries plus accessibility rules. Excellent for clean, honest charts; deliberately opinionated, so it overrides styling choices.

## Write & Refine

> Draft the scholarly prose, win the funding, and strip the machine tells.

### Academic Writing & Drafting

> Draft scholarly prose — sections, structure, and argument scaffolding for papers, theses, and reviews.

#### Manuscript drafting pipelines

- `Suite` [academic-skills](https://github.com/chtc66/academic-skills) - by [chtc66](https://github.com/chtc66) · `MIT` · `net`.<br>Everyday-researcher workflow suite (AI/NLP-leaning, Chinese-first): paper deep-notes, survey writing, arXiv monitoring, review/rebuttal drafting, experiment-log summaries, benchmark extraction, research-gap finding and weekly lab updates.
- `Suite` [academic-writing](https://github.com/alessandrocaforio/academic-writing) - by [alessandrocaforio](https://github.com/alessandrocaforio) · `MIT`.<br>Multi-agent writing system that decomposes an empirical thesis into per-section skills (intro, methods, results, discussion, abstract) plus literature review, analysis, and submission. The section-level structure is its strength; nominally econ.
- `Suite` [academic-writing-skills](https://github.com/wenyuchiou/academic-writing-skills) - by [wenyuchiou](https://github.com/wenyuchiou) · `MIT`.<br>Field-agnostic paper-writing workflow: findings-first drafting, de-AI/overclaim detection, claim-to-evidence checks, reviewer-response tables, and pre-submission checklists, with per-paper journal overrides. Ships evals — rare and welcome.
- `Suite` [enhanced-mathmodel-codex-skills](https://github.com/xzwwwwww/enhanced-mathmodel-codex-skills) - by [xzwwwwww](https://github.com/xzwwwwww) · `No License` · `net`.<br>Full-pipeline skills for mathematical-modeling competitions, automating the workflow through to a complete modeling paper (Codex-oriented). Niche but genuinely scholarly and specific; ships no license.
- `Suite` [nature-paper-skills](https://github.com/boom5426/nature-paper-skills) - by [boom5426](https://github.com/boom5426) · `MIT` · `net`.<br>A journal-first manuscript pipeline for Nature-style submissions — citation-integrity, claim/evidence discipline, submission preflight and rebuttal. Opinionated and narrow by design; strong for high-end bio/medical writing.
- `Suite` [nature-writing-skill](https://github.com/syntaxsmith/nature-writing-skill) - by [syntaxsmith](https://github.com/syntaxsmith) · `No License`.<br>Nature-family (NMI/NC/NCS/Nature) paper-writing craft for Chinese AI/ML researchers, built from sentence-level extraction of 44 open-access papers with a grep-traceable corpus and a sister figure skill. Niche to Nature-style AI methods papers.
- `Suite` [paperorchestra](https://github.com/ar9av/paperorchestra) - by [ar9av](https://github.com/ar9av) · `NOASSERTION` · `net`.<br>Portable skill pack implementing Google's PaperOrchestra: turns agent experiment logs into idea+log inputs, then outline→writing→refinement→plotting with autoraters to a LaTeX paper. Best when experiments already exist, not literature-first.
- `Suite` [paperspine](https://github.com/wubing2023/paperspine) - by [wubing2023](https://github.com/wubing2023) · `MIT` · `net`.<br>Ten-skill academic-writing suite covering discovery, literature synthesis, argument-building, manuscript revision, citations, figures, reviewer responses, and submission. Strong end-to-end coverage, bilingual EN/zh; orchestration-heavy.
- [paper-orchestra-for-claude-code](https://github.com/sunjongos/paper-orchestra-for-claude-code) - by [sunjongos](https://github.com/sunjongos) · `MIT` · `net`.<br>An ambitious 12-agent Korean+English SCI-paper pipeline, but its SKILL.md leans on grand "surpasses everything" marketing — read warily.
- [paper-writing-skill](https://github.com/snl-ucsb/paper-writing-skill) - by [snl-ucsb](https://github.com/snl-ucsb) · `MIT`.<br>Encodes one systems lab's battle-tested paper-writing methodology (brainstorm to compress) with rhetorical-move templates and a figure-synthesis guide. Strongest for CS/systems venues; opinionated voice may not transfer to every field.
- [trivium](https://github.com/MetaQiu/Trivium) - by [MetaQiu](https://github.com/MetaQiu) · `MIT` · `net`.<br>Drafts each paragraph by Claude/Codex/Gemini consensus, betting three-model-approved text also satisfies LLM reviewers — needs all three CLIs.

#### LaTeX & typesetting-integrated writing

- `Suite` [ageaf](https://github.com/onireimu/ageaf) - by [onireimu](https://github.com/onireimu) · `MIT` · `net`.<br>Brings AI agents (Claude, OpenAI and others) directly into Overleaf for LaTeX paper writing and editing. A focused, genuinely academic integration for the dominant collaborative LaTeX editor.
- `Suite` [awesome-latex-skills](https://github.com/calix-l/awesome-latex-skills) - by [calix-l](https://github.com/calix-l) · `MIT` · `net`.<br>LaTeX paper-writing suite: fix compile errors, polish academic prose, format for venue templates, read papers, and recover lost source. Tight and practical for manuscript work; prompt-pack style, so depth depends on the agent.
- `Suite` [latex-paper-skills](https://github.com/yunshenwuchuxun/latex-paper-skills) - by [yunshenwuchuxun](https://github.com/yunshenwuchuxun) · `MIT` · `net`.<br>Modular LaTeX paper-writing bundle for ML/AI: topic-to-compiled-PDF with verified BibTeX citations, gated workflows, a results-backfill step and a prose 'rhythm refiner', plus multi-agent (Claude+Gemini) collaboration.
- `Plugin` [academic-writing-agents](https://github.com/andrehuang/academic-writing-agents) - by [andrehuang](https://github.com/andrehuang) · `MIT`.<br>Claude Code plugin running 12 specialist agents (logic, technical, prose, bibliography, LaTeX reviewers) in parallel over a draft, diagnosing then fixing with human approval. Strong for structured manuscript review; not a from-scratch writer.
- [stats-paper-writing-agent-skills](https://github.com/fuhaoda/stats-paper-writing-agent-skills) - by [fuhaoda](https://github.com/fuhaoda) · `No License`.<br>A statistics-writing LaTeX workbench: drafts abstracts/keywords, audits a manuscript for structure, references, notation and reproducibility cues, writes referee reports and point-by-point response letters, and ships check_tex.py/check_bib.py.

#### Thesis & degree-work authoring

- [chinese-thesis-workbench-skill](https://github.com/zyhsechub/chinese-thesis-workbench-skill) - by [zyhsechub](https://github.com/zyhsechub) · `MIT`.<br>Turns a student project (source code, database, screenshots, references) into a traceable, resumable, reviewable undergraduate thesis following a university template and sample-paper style. Great for CN capstones; not a general academic-writing tool.
- [humanities-thesis-skill](https://github.com/ganzhi-black/humanities-thesis-skill) - by [ganzhi-black](https://github.com/ganzhi-black) · `MIT` · `net`.<br>A Chinese-first humanities/social-science thesis copilot that stresses thinking the argument through and auditing every paragraph over generating text. Strong anti-fabrication discipline.
- [physics-lab-report-skill](https://github.com/ydh0411/physics-lab-report-skill) - by [ydh0411](https://github.com/ydh0411) · `MIT`.<br>Generates pre-lab and formal university-physics lab reports in spec-compliant LaTeX, with real data-processing built in: uncertainty propagation, the method of successive differences, least-squares fitting and uncertainty analysis.
- [skill-thesis-writer](https://github.com/yanlin-cheng/skill-thesis-writer) - by [yanlin-cheng](https://github.com/yanlin-cheng) · `MulanPSL-2.0`.<br>A Chinese-academic thesis-writing skill for undergraduate and graduate work across engineering, psychology, education and management, enforcing GB/T 7714-2015 reference formatting with built-in data-analysis and citation management.

#### Literature-review writing

- [academic-paper-skills](https://github.com/lishix520/academic-paper-skills) - by [Li Shixiong (lishix520)](https://github.com/lishix520) · `MIT`.<br>A rare humanities-focused drafting pipeline for philosophy and preprint venues, with citation-backed gap analysis — now unmaintained.
- [lit-review](https://github.com/bethww/lit-review) - by [bethww](https://github.com/bethww) · `MIT`.<br>Guides a literature review as an argument across seven phases (question, method, synthesis) instead of summarizing sources. Bilingual EN/zh; explicitly will not write the paper for you.
- [litllm](https://github.com/litllm/litllm) - by [litllm](https://github.com/litllm) · `Apache-2.0` · `net`.<br>RAG-based literature-review assistant (TMLR 2025) that drafts structured related-work sections from a paper set, as a web app or Claude Code skill. Strong for related-work synthesis; narrow (related-work, not full-paper) and demo-hosted.

#### Prose refinement & discipline-specific style

- `Suite` [claude-code-my-workflow](https://github.com/pedrohcgs/claude-code-my-workflow) - by [Pedro H. C. Sant'Anna (pedrohcgs)](https://github.com/pedrohcgs) · `MIT` · `net` `hooks` `bypass`.<br>An econometrician's fork-ready, 36-command Claude Code setup from a PhD course — but ships with bypass-permissions on by default.
- `Suite` [paper-discipline-skills](https://github.com/lambenthan/paper-discipline-skills) - by [lambenthan](https://github.com/lambenthan) · `MIT`.<br>12 zh research-writing 'discipline' skills from a real book of mistakes: backup-before-Word, terminology protection, pilot-before-batch, logical-consistency, parallel-audit. Each has a rationalization table to stop skipping. Guardrails, not content.
- [econ-writing-skill](https://github.com/hanlulong/econ-writing-skill) - by [Lu Han (hanlulong)](https://github.com/hanlulong) · `MIT`.<br>The best-sourced discipline writing skill here, distilling 50+ named economics guides into enforceable rules.
- [english-writing](https://github.com/yzy1996/english-writing) - by [yzy1996](https://github.com/yzy1996) · `No License`.<br>Academic-English polishing skill backed by a curated per-section phrasebook (abstract, intro, related work, method, experiment, rebuttal) of good usages mined from real papers. Great phrasing help for non-native CS/ML writers; no LICENSE file.
- [journal-adapt-writing-skill](https://github.com/wantongc/journal-adapt-writing-skill) - by [wantongc](https://github.com/wantongc) · `MIT`.<br>Goes beyond generic style rules by building a corpus-grounded 'dynamic skill' from a target journal's own papers, then revising section by section. The differentiator is journal adaptation; needs you to supply the reference corpus.
- [research-paper-writing](https://github.com/Master-cai/Research-Paper-Writing-Skills) - by [Xudong Cai (Master-cai)](https://github.com/Master-cai) · `MIT`.<br>Packages Peng Sida's well-known research-writing notes into paragraph-level rewriting discipline for ML/CV/NLP papers.
- [research-writing-skill](https://github.com/alfonso0512/research-writing-skill) - by [alfonso0512](https://github.com/alfonso0512) · `MIT`.<br>Bilingual (zh/en) academic-writing prompt pack: 30 templates spanning lit review, outlining, drafting, polishing, de-AI, reviewer rebuttal and grant text. Broad and popular, but template-based rather than tool-backed; light on verification.
- [writing-in-the-sciences-skill](https://github.com/jingkarqi/writing-in-the-sciences-skill) - by [jingkarqi](https://github.com/jingkarqi) · `MIT`.<br>Scientific-writing skill built on Stanford's Writing in the Sciences (Sainani): a structured draft/revise workflow for clear, evidence-backed prose. Strong principled grounding; a Codex-native single skill, English-pedagogy-centric.

### Writing Quality & De-AI

> Tighten and de-slop the draft — clarity, voice, and removing the tells that mark text as machine-generated.

#### De-AI & humanizing

- `Suite` [science_narrative_skills](https://github.com/kangning-huang/science_narrative_skills) - by [kangning-huang](https://github.com/kangning-huang) · `No License` · `net`.<br>Evaluates scientific writing through the And-But-Therefore (ABT) narrative framework (Schimel's 'Writing Science'), diagnosing whether a paper's argument forms a coherent story rather than a list of facts.
- [avoid-ai-writing](https://github.com/conorbronsdon/avoid-ai-writing) - by [Conor Bronsdon (conorbronsdon)](https://github.com/conorbronsdon) · `MIT`.<br>The most intellectually honest de-AI skill — it cites false-positive research and insists its flags are "signals, not proof".
- [humanize-academic-writing](https://github.com/momo2young/humanize-academic-writing) - by [momo2young](https://github.com/momo2young) · `MIT`.<br>De-AI skill for social-science prose: flags AI markers (repetitive structure, abstract language, mechanical flow) and rewrites in an authentic academic voice, with detector/analyzer scripts. Aimed at non-native English researchers.
- [humanizer](https://github.com/blader/humanizer) - by [blader](https://github.com/blader) · `MIT` · `net`.<br>The de-facto standard for stripping AI tells from prose (em-dash overuse, rule-of-three, filler, negative parallelism). Single-purpose and scoped to read/write tools; great as a finishing pass, not a full writing assistant.
- [humanizer-academic](https://github.com/matsuikentaro1/humanizer_academic) - by [Kentaro Matsui (matsuikentaro1)](https://github.com/matsuikentaro1) · `MIT`.<br>De-slop for medical manuscripts that makes the inverse move — it restores formal terms LLMs avoid rather than flattening everything.
- [humanmade-antislop](https://github.com/machinemade-mm/humanmade-antislop) - by [machinemade-mm](https://github.com/machinemade-mm) · `MIT`.<br>De-AI scientific-writing skill fusing human-voice rules, IMRAD/citation-style scaffolding and GRADE-style critique. Strong on banned-phrase removal and reporting-guideline awareness; derivative of K-Dense and the Wikipedia AI-writing guide.
- [paper-humanizer-skill](https://github.com/crabin/paper-humanizer-skill) - by [crabin](https://github.com/crabin) · `No License`.<br>Academic text humanizer for Chinese and English: strips AI-writing tells while strictly preserving facts, numbers and conclusions, and reports which patterns it found. Ships no open-source license.
- [skill-deslop](https://github.com/stephenturner/skill-deslop) - by [Stephen Turner (stephenturner)](https://github.com/stephenturner) · `MIT`.<br>A science-aware de-slop skill that spares conventions like passive-voice Methods — the pick when stop-slop feels too blog-flavored.
- [stop-slop](https://github.com/hardikpandya/stop-slop) - by [Hardik Pandya (hardikpandya)](https://github.com/hardikpandya) · `MIT`.<br>The most-starred de-slop skill — a dogmatic 8-rule rulebook, but general-purpose, not academic-specific, and ignores false positives.
- `Plugin` [unslop](https://github.com/mohamedabdallah-14/unslop) - by [mohamedabdallah-14](https://github.com/mohamedabdallah-14) · `MIT` · `net` `hooks`.<br>De-AI plugin that strips AI-isms (sycophancy, stock phrases, hedging, em-dash pileups) while preserving code, URLs and headings, with a benchmarked detector. Strong general-prose humanizer; not academic-specific, needs tuning to keep technical voice.

#### AIGC detector evasion (thesis)

- [aigc-down-skill](https://github.com/yezery/aigc-down-skill) - by [yezery](https://github.com/yezery) · `MIT`.<br>Chinese-thesis de-AIGC skill: parses CNKI/Wanfang detection reports, targets flagged passages, and rewrites to cut AI-detection rate while keeping argument and register. Effective for zh theses; not for English and no guarantee against detectors.
- [anti-aigc-zh](https://github.com/beizi6/anti-aigc-zh) - by [beizi6](https://github.com/beizi6) · `MIT`.<br>A Chinese counter-AIGC rewriter that reasons from how detectors work (probability curvature, perplexity uniformity, watermark tokens) plus image-metadata stripping. Niche and evasion-focused; bundled chunked-file-writer is incidental.
- [deai-academic-zh](https://github.com/houlaisan/deai-academic-zh) - by [houlaisan](https://github.com/houlaisan) · `MIT`.<br>Chinese-thesis AIGC detection + de-AI rewriting with a documented 3-pass method (wording→burstiness→restructuring) and a zero-fabrication rule; reports real Weipu/CNKI score drops. For zh undergrad/master theses, not English.
- [dissertation-polisher-zh](https://github.com/chipsahoym/dissertation-polisher-zh) - by [chipsahoym](https://github.com/chipsahoym) · `MIT`.<br>Chinese CS-PhD-dissertation polisher: batch-reads 120+ page theses, strips AI-writing markers, enforces academic-norm checks (first-person residue, figure/ref formatting) and chapter consistency. For formal academic prose, not casual humanizing.
- [humanizer-academic-zh](https://github.com/cangtianhuang/humanizer-academic-zh) - by [cangtianhuang](https://github.com/cangtianhuang) · `MIT` · `net`.<br>Chinese-academic "humanizer": rewrites paper text to lower AIGC-detection rates and AI phrasing while keeping the core argument, deliberately lightweight and token-thrifty. A niche pick; results depend on the model and are hard to verify.
- [humanizer-zh-academic](https://github.com/redbaronyyyyy-eng/humanizer-zh-academic) - by [redbaronyyyyy-eng](https://github.com/redbaronyyyyy-eng) · `MIT`.<br>Rewrites Chinese academic prose to read as human-written and lower AIGC-detector scores. Single-purpose and popular among zh writers; quality of output depends heavily on the source draft, and 'beating detectors' is inherently a moving target.

#### Manuscript proofreading & quality audit

- [proofreading](https://github.com/jakobthumm/proofreading) - by [jakobthumm](https://github.com/jakobthumm) · `MIT`.<br>Proofreads academic papers against 100+ checks (structure, math notation, statistics, figures, grammar, abbreviations) in report or interactive mode, and extracts reviewer marks from annotated PDFs. Deep checklist; English-style checks need tuning.
- [slopbuster](https://github.com/gabelul/slopbuster) - by [gabelul](https://github.com/gabelul) · `MIT` · `net`.<br>A local AI-text humanizer for prose, code and academic writing: a two-pass audit flags 100+ tell-tale AI patterns, scores them in three tiers, and rewrites with optional voice injection -- all offline, no API calls.
- [thesis-writer](https://github.com/ibrahim-kukash/thesis-writer) - by [ibrahim-kukash](https://github.com/ibrahim-kukash) · `MIT`.<br>Writes thesis chapters while scanning for 14 common AI-writing tells against a 23-point rubric, aimed at making academic prose read as human. A focused writing + de-AI tool for theses; useful as a quality gate, though only lightly proven (8 stars).

#### Anti-hallucination & over-revision guards

- [grounded-research-skill](https://github.com/arturseo-geo/grounded-research-skill) - by [arturseo-geo](https://github.com/arturseo-geo) · `MIT`.<br>Anti-hallucination mode applying Anthropic's three guardrails: admit uncertainty, quote-before-analyze, cite-every-claim with a self-audit and public retraction. Trades creativity for trust; a fact-grounding overlay, not a general research mode.
- [sciwrite](https://github.com/labarba/sciwrite) - by [Lorena A. Barba (labarba)](https://github.com/labarba) · `CC-BY-4.0`.<br>Encodes Sainani's Stanford "Writing in the Sciences" method into five sequential audit passes. A pedigree de-clutter pick for manuscripts.

## Review & Publish

> Get reviewer-quality critique, then make the manuscript submission-ready.

### Peer Review & Response

> Review and respond — reviewer-quality critique, rebuttal letters, and the response-to-reviewers that gets a paper accepted.

#### Pre-submission review & rebuttal

- `Suite` [AI-research-feedback](https://github.com/claesbackman/AI-research-feedback) - by [Claes Bäckman](https://github.com/claesbackman) · `MIT`.<br>Pre-submission referee simulator tuned only for AER/QJE/JF-tier economics — six parallel agents, not general review.
- `Suite` [archora-skills](https://github.com/richard-kim-79/archora-skills) - by [Richard Kim (Archora)](https://github.com/richard-kim-79) · `MIT`.<br>Simulates an editor-in-chief plus three reviewers; vendor-affiliated (Archora) but runs standalone as plain markdown.
- `Suite` [polisci-review](https://github.com/cmertdalli/polisci-review) - by [cmertdalli](https://github.com/cmertdalli) · `MIT`.<br>Pre-submission audit for political-science manuscripts: 9 modules (contribution, theory, measurement, identification, transparency, journal fit) with journal-aware personas and 8 verified journal-policy profiles. Rigorous and discipline-specific.
- [academic-review-skill](https://github.com/pengkangzhen/academic-review-skill) - by [pengkangzhen](https://github.com/pengkangzhen) · `MIT`.<br>Reviews OR/management-science manuscripts for academic merit rather than implementation, detecting domain-specific red flags (infeasible quantities, trivial VSS%) and deliberately phrasing critiques as queries to avoid killing genuine findings.
- [ai-peer-review-skill](https://github.com/alexwortega/ai-peer-review-skill) - by [alexwortega](https://github.com/alexwortega) · `MIT`.<br>Drop in a paper PDF, get N independent structured reviews plus a synthesized meta-review and a concern matrix CSV. Adapts poldrack/ai-peer-review to free Claude subagents; defaults to a hard alignment-style critic.
- [manuscript-review-skill](https://github.com/shaowen-ye/manuscript-review-skill) - by [shaowen-ye](https://github.com/shaowen-ye) · `MIT`.<br>Pre-submission manuscript review by six role-specialized AI reviewers (architecture, theory, methods, etc.) that emits a bilingual EN-ZH color-annotated .docx with a 1-10 scoring matrix and prioritized fixes, calibrated to a target journal.
- [mean-reviewer-skill](https://github.com/xz-liu/mean-reviewer-skill) - by [xz-liu](https://github.com/xz-liu) · `No License`.<br>Roleplays the worst-case adversarial peer reviewer: an inflated wall of weaknesses, framework attacks, a score fixed at reject, and a rebuttal phase conceding nothing. Half polemic on LLM reviews, half a pre-submission stress test; not a gentle tool.

#### Systematic review & evidence appraisal

- [diogenes](https://github.com/diogenes-project/diogenes) - by [diogenes-project](https://github.com/diogenes-project) · `GPL-3.0` · `net` `hooks`.<br>Applies a unified, anti-sycophantic evidence methodology - ICD 203, GRADE, PRISMA, Cochrane RoB and others - as a 14-step appraisal for systematic reviews, evidence grading and claim verification. Rigorous; ships hooks.
- [slr-prisma](https://github.com/keemanxp/slr-prisma) - by [keemanxp](https://github.com/keemanxp) · `NOASSERTION`.<br>A systematic-literature-review scaffold following the PRISMA 2020 framework (protocol, search, screening, flow diagram, synthesis). Solid methodology for rigorous reviews; process-guidance rather than automated search, and its license is unclear.

### Submission, Formatting & Conversion

> Get it submission-ready — journal templates, format conversion, and the camera-ready details editors check first.

#### LaTeX authoring & submission prep

- `Suite` [mcp-overleaf](https://github.com/bettyguo/mcp-overleaf) - by [bettyguo](https://github.com/bettyguo) · `MIT` · `net`.<br>An Overleaf/LaTeX submission-prep bundle (MCP server plus 6 skills): cleans the .bib, applies venue rule packs, runs latexdiff, and drafts related-work sections.
- `Suite` [paperfit](https://github.com/openraiser/paperfit) - by [openraiser](https://github.com/openraiser) · `MIT` · `net`.<br>LaTeX typesetting suite that compiles, renders pages to images, then visually diagnoses and fixes layout problems (overfull boxes, float placement, spacing, tables). The vision-in-the-loop loop is its real edge; needs a working local LaTeX toolchain.
- [claude-skill-overleaf](https://github.com/junhahyung/claude-skill-overleaf) - by [junhahyung](https://github.com/junhahyung) · `MIT`.<br>Reads and writes Overleaf projects from Claude Code via the Overleaf git bridge: edit, commit, and push LaTeX to the web editor with secure token handling and no force-push. Includes a rebuttal scaffold. A clean way to bring an agent into Overleaf.
- [latex-arxiv-skill](https://github.com/renocrypt/latex-arxiv-skill) - by [renocrypt](https://github.com/renocrypt) · `No License` · `net`.<br>Issue-driven Codex skill for ML/AI arXiv review papers: scaffolds the LaTeX project and verifies every BibTeX entry end-to-end. The BibTeX verification lifts it above generic templates; aimed narrowly at arXiv-style ML reviews; ships no license.
- [latex-document-skill](https://github.com/ndpvt-web/latex-document-skill) - by [ndpvt-web](https://github.com/ndpvt-web) · `MIT`.<br>The most template-heavy LaTeX skill here — 27 templates spanning papers, forms and tables; breadth over a single niche.

#### Slides & presentation decks

- [beamer-academic](https://github.com/faust-donf/beamer-academic) - by [faust-donf](https://github.com/faust-donf) · `MIT`.<br>Turns a thesis or paper into ready-to-present academic Beamer slides with a real layout library and an interactive editing loop. Bilingual, no LaTeX expertise required; scope is defense/conference decks, not general slide design.
- [beamer-skill](https://github.com/Noi1r/beamer-skill) - by [Noi1r](https://github.com/Noi1r) · `MIT`.<br>The strongest pick for academic LaTeX slides, with opinionated pedagogy: no overlays, density caps, visual overflow detection.
- [beamer-skill](https://github.com/jaxonjp/beamer-skill) - by [jaxonjp](https://github.com/jaxonjp) · `MIT`.<br>Create/compile/review/polish academic Beamer decks with TikZ and pedagogical audits and quality gates; explicitly defers PPTX to other skills. A derivative work, extended; LaTeX-only by design.
- [powerpoint-skill](https://github.com/noi1r/powerpoint-skill) - by [noi1r](https://github.com/noi1r) · `MIT`.<br>Creates visually rich PowerPoint decks with native OMML math and LaTeX support, well suited to research talks and lectures that need real equations in slides. Not academic-only, but the math support sets it apart.
- [thesis-defense-pptx-skill](https://github.com/zouchenzhen/thesis-defense-pptx-skill) - by [zouchenzhen](https://github.com/zouchenzhen) · `Apache-2.0`.<br>Builds an editable defense deck from your thesis PDF/LaTeX while strictly reusing a university PPTX template; inventories cited figures and runs overflow/layout checks. Windows+PowerPoint COM for the full quality gates.

#### Journal & Word-template formatting

- `Suite` [docx-skill-4-cn-paper](https://github.com/gostyan/docx-skill-4-cn-paper) - by [gostyan](https://github.com/gostyan) · `MIT`.<br>Applies standard Chinese-paper Word formatting - fonts, sizes, spacing, margins, heading levels, figure/table numbering, references - for course papers, math-modeling competitions and theses, incl. md-to-docx. Narrow but does its job well.
- `Suite` [Manuscript Submission Formatting Agent](https://github.com/maxwell2732/my-submission-formatting-agent) - by [Chen Zhu (朱晨)](https://github.com/maxwell2732) · `No License` · `hooks`.<br>Reformats a finished manuscript to a new journal's author guidelines for post-rejection resubmission, never touching the results.
- `Plugin` [word-format-skill](https://github.com/yeap531/word-format-skill) - by [yeap531](https://github.com/yeap531) · `No License`.<br>Replicates a reference Word document's typography onto new content via an HTML bridge — useful for matching a journal or institutional .docx template. Strong for submission/formatting chores.

#### Format conversion & document transformation

- `Suite` [paper2patent](https://github.com/7tocr/paper2patent) - by [7tocr](https://github.com/7tocr) · `MIT`.<br>Turns a finished paper into a China invention-patent application draft (claims layout, specification norms, technical-effect argumentation) via structured prompts, patent-figure generation, and skills. A unique paper-to-IP bridge for China patents.
- [any2pdf](https://github.com/lovstudio/any2pdf) - by [lovstudio](https://github.com/lovstudio) · `MIT`.<br>Markdown to PDF with no LaTeX; its real edge is CJK rendering where Pandoc and wkhtmltopdf break.
- [Markdown Exporter](https://github.com/bowenliang123/markdown-exporter) - by [bowenliang123](https://github.com/bowenliang123) · `Apache-2.0`.<br>The broadest, most battle-tested format coverage here (DOCX/PDF/PPTX/XLSX/EPUB), running locally with no outbound calls.

## Suites, Systems & Meta

> Multi-stage suites, end-to-end research agents, field-specific packs, and maps of the wider ecosystem.

### Skill Suites

> Multi-skill repositories that cover several lifecycle stages at once. Compared side by side in the table below.

| Suite                                                                                         |     ★ | Skills | Best for                                                                                                                                                                                                                                                 | Runs          |
| --------------------------------------------------------------------------------------------- | ----: | -----: | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------- |
| [academic-research-skills](https://github.com/Imbad0202/academic-research-skills)             | 36.6k |      — | A human-in-the-loop pipeline built to fight AI fabrication that deliberately refuses to ghost-write; non-commercial license                                                                                                                              | `net` `hooks` |
| [academic-research-skills-codex](https://github.com/imbad0202/academic-research-skills-codex) |  5.6k |      — | Codex-native Academic Research Skills: deep research, paper drafting, manuscript review, research-to-paper pipelines, citation/integrity checks. Broad end-to-end; vendored as one giant skill (audit accordingly); non-commercial license               | `net` `hooks` |
| [AcademicForge](https://github.com/HughYau/AcademicForge)                                     |  2.2k |      7 | A convenient web installer that bundles seven existing academic skills — but it repackages others' work rather than adding its own                                                                                                                       | `net`         |
| [AI Research Skills (Orchestra)](https://github.com/Orchestra-Research/AI-Research-SKILLs)    | 10.5k |     98 | A 98-skill curriculum for the engineering half of ML research, taking an agent from idea to trained model — not wet-lab                                                                                                                                  | `net`         |
| [ai-research-skills](https://github.com/zechenzhangagi/ai-research-skills)                    | 10.5k |      — | 98-skill AI/ML research suite: ideation, literature review, baseline/ablation design, experiment tracking, significance testing, figure generation, paper writing, peer review and rebuttals. The reference 'turn your agent into a researcher' suite    | `net`         |
| [anthropics/life-sciences](https://github.com/anthropics/life-sciences)                       |   512 |      — | Anthropic's official life-sciences marketplace — a vetted directory of ~20 partner data integrations, not a skill collection                                                                                                                             | `net`         |
| [aut_sci_write](https://github.com/shzhao27208/aut_sci_write)                                 |   156 |      — | Modular research-lifecycle suite: literature search across arXiv/PubMed/Web of Science, PDF and figure extraction, review/meta-analysis writing, Zotero sync and slides. Broad and well-adopted; a do-everything suite, not a best-in-one-stage tool     | `net`         |
| [claude-academic-research](https://github.com/mronkko/claude-academic-research)               |    17 |      — | Professor-built suite spanning the research lifecycle: PRISMA review, peer review, manuscript revision, empirical-integrity stat checks, and Zotero/MCP-grounded citations that refuse hallucinated references. Strong on rigor; needs Zotero+MCP setup  | `net`         |
| [claude-research](https://github.com/flonat/claude-research)                                  |   109 |      — | PhD-researcher infrastructure: 50 skills plus agents, hooks and rules for bibliography validation, LaTeX health-checks, experiment and causal design, and reproducible project setup. Strong end-to-end; ships hooks and an unscoped Bash                | `net` `hooks` |
| [claude-scholar](https://github.com/Galaxy-Dawn/claude-scholar)                               |  4.5k |     47 | A CS/AI research workspace with an evidence-gated Claim Promotion Gate; uniquely ships its own PreToolUse security-guard hook                                                                                                                            | `net` `hooks` |
| [claude-scholar](https://github.com/yy/claude-scholar)                                        |    29 |      — | A 12-skill academic toolkit: OpenAlex/arXiv search, DOI-to-BibTeX, citation verification, LaTeX cleanup, arXiv packaging, pre-submission checks, math verification, manuscript/figure critique. Honest that it is early-stage; lists its data egress     | `net`         |
| [claude-scientific-writer](https://github.com/k-dense-ai/claude-scientific-writer)            |  2.1k |      — | A 27-skill scientific-writing suite: literature review, citation management, peer review, figures, posters, slides and manuscript drafting. The most popular here and broad, but jack-of-all-trades; ships an unscoped Bash                              | `net`         |
| [codex-paper-skills](https://github.com/moonlarry/codex-paper-skills)                         |   104 |      — | Codex/Claude paper suite (27 skills) covering the writing chain, figures, experiment-to-claim consistency, citation auditing, proof checking and rebuttal, with an evidence-first agent protocol. Strong breadth; the missing LICENSE is its main gap    | `net`         |
| [google-deepmind/science-skills](https://github.com/google-deepmind/science-skills)           |  2.3k |     37 | Google DeepMind's official pack grounding agents in real biological data — narrow to structural bio and genomics, but authoritative                                                                                                                      | `net`         |
| [mgmt-paper-skills](https://github.com/haonanalex/mgmt-paper-skills)                          |   118 |      — | Management-research workbench: idea-to-review pipeline with SPSS/Stata/Python analysis, causal methods (DiD/RDD/IV/SC/PSM), qualitative coding and journal-figure profiles (UTD24). Deep for econ/management; Chinese-data oriented, needs a stats MCP   | `net`         |
| [nature-skills](https://github.com/Yuan1z0825/nature-skills)                                  | 26.7k |      9 | A tight 9-skill bundle strongest on Nature-style prose and figures, weakest as a data toolkit                                                                                                                                                            | `net`         |
| [open-scholar-skill](https://github.com/joshzyj/open-scholar-skill)                           |    96 |      — | Social-science paper suite for top journals: analytics with publication-ready regression tables/figures (NHANES/IPUMS/GSS), literature synthesis, causal design, citation. Broad end-to-end; non-commercial license + a self-citation nudge              | `net`         |
| [papercash](https://github.com/jesseovo/papercash)                                            |    85 |      — | End-to-end Chinese-student paper workflow over 8 free sources (S2, arXiv, Crossref, PubMed, CNKI, Wanfang, Baidu/Google Scholar): search, review, polish, plagiarism precheck, AI-rate reduction, GB/T-7714 refs. Broad but shallow per stage            | `net` `hooks` |
| [posit-dev/skills](https://github.com/posit-dev/skills)                                       |   421 |      — | Posit's official R / Quarto / tidyverse skills from the makers of RStudio — the pick when analysis lives in R, not Python                                                                                                                                | —             |
| [q-skills](https://github.com/tyrealq/q-skills)                                               |    23 |      — | Twelve-skill academic toolkit for empirical research: literature review, R and Stata analysis, reproducible-research scaffolding, survey design, grant writing, peer review, and citations. Strong for quantitative social science; breadth over depth   | —             |
| [research-agora](https://github.com/rpatrik96/research-agora)                                 |    13 |      — | Suite for ML researchers spanning literature search, paper writing, citation verification, experiment tracking, LaTeX automation, benchmarking, and peer review. The experiment-tracking and benchmark angle is its edge; breadth means moderate depth   | `net` `hooks` |
| [researchclaw](https://github.com/alphalab-ustc/researchclaw)                                 |   130 |      — | End-to-end OpenClaw research companion (six capabilities incl. arXiv search, reading, writing) with no API keys and a live demo, from a USTC lab. Broad workflow coverage; a stray SKILL.md.bak suggests light repo hygiene                              | —             |
| [scholaraio](https://github.com/zimoliao/scholaraio)                                          |   541 |      — | Modular all-in-one research suite (47 skills): literature search, reference management, PDF parsing and writing support, built to compose. A reasonable general backbone of moderate depth; note it ships an SSH-backup feature and a hook to review     | `net` `hooks` |
| [sciclaw](https://github.com/drpedapati/sciclaw)                                              |    84 |      — | A 'pair-scientist' research suite (23 skills) wrapped in a lightweight Go runtime that injects lifecycle hooks, a manuscript spine and run-logging so every session is reproducible, logged and citeable                                                 | `net` `hooks` |
| [scienceclaw](https://github.com/zaoqu-liu/scienceclaw)                                       |    55 |      — | End-to-end research suite (275 skills, 9 agents, 77 databases) spanning literature search to publication. Ambitious breadth in one repo, but quality is uneven and it ships a chat-bot channel, hooks and a tools wildcard worth reviewing               | `net` `hooks` |
| [scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills)              | 30.4k |    142 | The biggest computational-science pack — deep for life-science labs, near-useless for humanities                                                                                                                                                         | `net`         |
| [scientific-research-skills](https://github.com/jxtse/scientific-research-skills)             |    54 |      — | Methodology-first research skills for agents: literature search, three-depth paper reading, full-text harvest, related-work survey, Zotero management and publication-figure generation                                                                  | `net`         |
| [voidful/academic-skills](https://github.com/voidful/academic-skills)                         |   101 |      8 | A compact, opinionated grad-school pipeline (CS/ML flavor) across Claude Code, Codex and Gemini                                                                                                                                                          | —             |
| [xueshuzhi-skills](https://github.com/yipng05-max/-skills)                                    |   237 |      — | Wide-coverage Chinese academic suite: topic selection, research design, CNKI/foreign literature search and verification, thematic coding, review and dissertation drafting, plus a 12-checkpoint TA pipeline assembling a Word draft. Breadth over depth | `net`         |

### Autonomous Research Systems

> End-to-end research agents — give them a question, get back a searched, read, and drafted result with citations.

#### Fully autonomous auto-scientists

- `Suite` [ARIS (Auto-Research-In-Sleep)](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep) - by [Yang Ruofeng](https://github.com/wanshuiyin) · `MIT` · `net` `hooks`.<br>An autonomous research loop whose signature is a cross-model jury — Claude, GPT and Gemini critique each other so no model rubber-stamps itself.
- `Suite` [autodidact-skill](https://github.com/damonchen-anan/autodidact-skill) - by [damonchen-anan](https://github.com/damonchen-anan) · `MIT`.<br>Autonomous topic-to-wiki research agent extending Karpathy's LLM-Wiki: auto-fetches web sources, compiles an interlinked wiki, and self-audits coverage gaps each round. Good for unattended literature scaffolding; not a verified-citation tool.
- `Suite` [autoresearch-skill](https://github.com/wjgoarxiv/autoresearch-skill) - by [wjgoarxiv](https://github.com/wjgoarxiv) · `MIT` · `net`.<br>Turns a natural-language research.md goal into a Karpathy-style experiment-evaluate-iterate loop, generalized beyond ML to any task with a mechanical evaluator, with auto rollback, audit trail, safety budgets. Domain-general; thin on literature work.
- `Suite` [de-anthropocentric-research-engine](https://github.com/yogsoth-ai/de-anthropocentric-research-engine) - by [yogsoth-ai](https://github.com/yogsoth-ai) · `Apache-2.0`.<br>Huge pure-markdown library of autonomous-research SOPs (~770 skills) arranged in a Campaign/Strategy/Tactic/SOP hierarchy covering direction-setting, literature acquisition, gap discovery, hypothesis formation and adversarial stress-testing.
- `Suite` [nano-scientist](https://github.com/ai4scientist/nano-scientist) - by [ai4scientist](https://github.com/ai4scientist) · `No License` · `net` `hooks`.<br>Autonomous research agent: turns a topic into a full draft paper via four budget-capped loops (deep-search, experiment, improvement, review) with CrossRef citation recovery and a multi-model review gate.
- `Suite` [rstack](https://github.com/sunnnybala/rstack) - by [sunnnybala](https://github.com/sunnnybala) · `MIT` · `net`.<br>Research-automation chain: /research runs lit-review→novelty-check→experiment→analyze-results→write-paper toward a submittable draft in one session; each skill also works standalone. Ambitious end-to-end; quality hinges on the experiment step.

#### Human-in-the-loop / gate-driven pipelines

- `Suite` [academic-research-agent-skill](https://github.com/ngtiendong/academic-research-agent-skill) - by [ngtiendong](https://github.com/ngtiendong) · `MIT`.<br>Human-in-the-loop research workflow for MS/PhD in CS/AI/math/eng: scopes questions, grounds a lit review in sources, runs a novelty gate, plans experiments, simulates reviewers, verifies claims. Disciplined collaboration, not a hand-off.
- `Suite` [anaxa](https://github.com/citrus-bit/anaxa) - by [citrus-bit](https://github.com/citrus-bit) · `MIT` · `net`.<br>Auditable, pausable research-agent workbench: drives a topic through lit search, evidence binding, sandboxed experiments, draft and citation audit to a LaTeX/PDF bundle with human gates. Heavy full-stack app, not a drop-in skill.
- `Suite` [phd-skills](https://github.com/fcakyon/phd-skills) - by [fcakyon](https://github.com/fcakyon) · `MIT` · `net` `hooks`.<br>PhD/ML research guardrails: reproduce arXiv papers, debug runs evidence-first, compare experiments at the same epoch, audit dataset bias, run pre-flight launch checks. Catches costly AI research mistakes; uses a Bash wildcard plus opt-in alerts.
- `Suite` [research-units-pipeline-skills](https://github.com/willoscar/research-units-pipeline-skills) - by [willoscar](https://github.com/willoscar) · `No License` · `net`.<br>File-first research harness turning open-ended goals into protocolized, resumable pipelines (lit survey, paper review, evidence synthesis) with per-stage acceptance gates and durable artifacts. Heavy machinery; steep to learn; no LICENSE file yet.
- `Plugin` [vibe-science](https://github.com/th3vib3coder/vibe-science) - by [th3vib3coder](https://github.com/th3vib3coder) · `Apache-2.0` · `net` `hooks`.<br>Integrity-first research runtime for Claude Code: a plugin that enforces checks and persists state, plus a methodology skill built on falsification, adversarial review, and confounder discipline. Aims to make AI science hard to fake; heavy exec.

#### Domain-bound autonomous systems

- `Suite` [ai-research-army](https://github.com/terryfyl/ai-research-army) - by [terryfyl](https://github.com/terryfyl) · `Apache-2.0` · `net`.<br>Nine-agent pipeline taking clinical data to a submission-ready medical manuscript — requirement scoping, data profiling, stats, figures, literature, drafting, submission packaging. Ambitious end-to-end; some modules are a partial public release.
- `Suite` [claude-workflow-for-econ-phd](https://github.com/saptarsibhowmick/claude-workflow-for-econ-phd) - by [saptarsibhowmick](https://github.com/saptarsibhowmick) · `MIT` · `net` `hooks`.<br>Fork-ready scaffold for multi-paper empirical-economics PhD work (lit review to submission): 9 skills (missing-lit, referee2, blindspot), a Zotero PDF-chunking literature pipeline, file-safety and IRB handling. A scaffold to adopt, not a drop-in.
- `Suite` [neurico](https://github.com/chicagohai/neurico) - by [chicagohai](https://github.com/chicagohai) · `Apache-2.0` · `net`.<br>Give it a structured hypothesis; it runs the experiment loop and emits code, figures, and a LaTeX paper. Lab-built and genuinely scholarly, though heavy (git+docker) and only as good as the domain harness behind it.
- `Suite` [scienceclaw](https://github.com/beita6969/scienceclaw) - by [beita6969](https://github.com/beita6969) · `MIT` · `net`.<br>Large self-evolving research-agent platform (OpenClaw-based): 285 skills across 28+ disciplines, persistent memory, API-grounded citations. Popular for end-to-end research agents; bundles a full messaging/browser/sandbox OS, so read before trusting.

### Discipline-Specific Packs

> Skills tuned to one field's conventions — bench biology, clinical, social-science, or humanities workflows.

#### Biomedical & life sciences

- `Suite` [alterlab-academic-skills](https://github.com/alterlab-ieu/alterlab-academic-skills) - by [alterlab-ieu](https://github.com/alterlab-ieu) · `MIT` · `net`.<br>186+ domain-organized academic skills for faculty/researchers, wrapping real scientific databases and libraries (ENA, biopython, cellxgene, cobrapy, ESM, etc.).
- `Suite` [beril-research-observatory](https://github.com/kbaseincubator/beril-research-observatory) - by [kbaseincubator](https://github.com/kbaseincubator) · `AGPL-3.0` · `net`.<br>KBase AI co-scientist over the BER microbial-ecology data lakehouse: 16 skills plus reusable patterns for pangenomics, fitness, metagenomics and biochemistry. Strong for KBase research; large executable surface and AGPL, so read before trusting.
- `Suite` [bioSkills](https://github.com/GPTomics/bioSkills) - by [GPTomics](https://github.com/GPTomics) · `MIT`.<br>The most benchmark-honest bioinformatics pack — idiomatic samtools/DESeq2/Seurat code, with published Bio-Task Bench scores.
- `Suite` [clawbio](https://github.com/clawbio/clawbio) - by [clawbio](https://github.com/clawbio) · `MIT` · `net`.<br>Bioinformatics-native agent skill library: local-first, reproducible genomics/QC/GWAS workflows built on OpenClaw, with CI and a cited release. Strong domain coverage; large executable surface typical of a real bioinformatics stack.
- `Suite` [dr-cook](https://github.com/wen-chen/dr-cook) - by [wen-chen](https://github.com/wen-chen) · `MIT`.<br>Modular research-lifecycle suite (literature, gap analysis, writing, peer review, bioinformatics, grants) with a routing layer and depth in Traditional Chinese Medicine. Strong for TCM/biomed; modest adoption, do-everything breadth.
- `Suite` [encode-toolkit](https://github.com/ammawla/encode-toolkit) - by [ammawla](https://github.com/ammawla) · `AGPL-3.0` · `net`.<br>Genomics suite: searches ENCODE, cross-references 14 databases (GWAS, ClinVar, GTEx, JASPAR), runs 7 pipelines, and writes provenance-tracked methods. Heavily tested; AGPL and genomics-specific, so niche elsewhere.
- `Suite` [labclaw](https://github.com/wu-yc/labclaw) - by [wu-yc](https://github.com/wu-yc) · `No License` · `net`.<br>Large lab-science skill library (240 SKILL.md across biology, pharma, medicine, literature, vision) wrapping real tools — ESM, AlphaFold DB, biopython, single-cell stacks — for dry-lab reasoning and protocol composition.
- `Suite` [medical-research-skills](https://github.com/aipoch/medical-research-skills) - by [aipoch](https://github.com/aipoch) · `MIT`.<br>A 500+ skill medical-research suite: RNA-seq/scRNA/spatial analysis, ADMET, evidence mapping, and a full manuscript-writing track. Broad and uneven by nature, but the depth in biomedical data analysis is unmatched here.
- `Suite` [medsci-agent](https://github.com/omar-a-hassan/medsci-agent) - by [omar-a-hassan](https://github.com/omar-a-hassan) · `MIT` · `net`.<br>Biomedical-research suite of 17 skills: multi-source literature search, ClinicalTrials.gov, drug interactions, and a genomics stack (gene lookup, variant annotation via ClinVar/dbSNP/gnomAD, pathway analysis). Deep domain coverage.
- `Suite` [medsci-skills](https://github.com/aperivue/medsci-skills) - by [aperivue](https://github.com/aperivue) · `NOASSERTION` · `net`.<br>A 34-skill medical-research suite from a physician-researcher: PubMed search, study design, IRB protocols, biostatistics, PRISMA/STROBE/TRIPOD reporting checks, figures and manuscript drafting. Broad and clinical; license is NOASSERTION.
- `Suite` [neuroclaw](https://github.com/cuhk-aim-group/neuroclaw) - by [cuhk-aim-group](https://github.com/cuhk-aim-group) · `MIT` · `net`.<br>Neuroscience and medical-imaging skill pack (87 skills) from CUHK's AIM group: connectome analysis, fMRI/EEG pipelines, neuroimaging statistics and clinical-data workflows.
- `Suite` [OpenClaw-Medical-Skills](https://github.com/FreedomIntelligence/OpenClaw-Medical-Skills) - by [FreedomIntelligence](https://github.com/FreedomIntelligence) · `No License` · `net`.<br>The largest open medical-research library (hundreds of skills) — broad coverage, but giant, unauditable and unlicensed.
- `Suite` [protein-design-skills](https://github.com/adaptyvbio/protein-design-skills) - by [Adaptyv Bio](https://github.com/adaptyvbio) · `MIT`.<br>Narrow, deep protein design that auto-chains BoltzGen, Chai and QC into one pipeline; expects real compute backends.
- `Suite` [SciAgent-Skills](https://github.com/jaechang-hits/SciAgent-Skills) - by [jaechang-hits](https://github.com/jaechang-hits) · `CC-BY-4.0`.<br>The largest open life-sciences library (199 skills), reporting a 65%-to-92% BixBench jump; low-risk but too large to fully audit.
- `Suite` [skillfoundry](https://github.com/ma-compbio-lab/skillfoundry) - by [ma-compbio-lab](https://github.com/ma-compbio-lab) · `Apache-2.0` · `net`.<br>Computational-biology discipline pack: 260+ skills wrapping standard bioinformatics workflows (RNA-seq with DESeq2/Salmon, GATK variant calling, ChIP/ATAC-seq, single-cell QC and integration, spatial transcriptomics, MaxQuant proteomics).

#### Physical, computational & mathematical sciences

- `Suite` [automcm-pro](https://github.com/realseaberry/automcm-pro) - by [realseaberry](https://github.com/realseaberry) · `MIT` · `net`.<br>End-to-end math-modeling-competition assistant (CUMCM/MCM): drives literature search, derivation, code, LaTeX and paper writing with forced code self-verification. Strong for modeling contests; competition-specific and Chinese-first.
- `Suite` [mathmodel-skill](https://github.com/yushui2022/mathmodel-skill) - by [yushui2022](https://github.com/yushui2022) · `No License` · `net`.<br>Agent-native math-modeling-contest workflow (10 skills): parse the problem, pick a model route, generate and run code, gate on real evidence, then write and Word-format a full paper with format checks. Built for CUMCM-style contests; uses eval/exec.
- `Suite` [scp](https://github.com/internscience/scp) - by [internscience](https://github.com/internscience) · `MIT` · `net`.<br>200+ computational-science skills (physics, chemistry, materials, numerical methods, HPC) wrapping real simulation tools like ASE. A discipline pack for bench/sim science rather than literature work; broad and cleanly built.

#### Computer science, AI / ML & graphics

- `Suite` [agent-research-skills](https://github.com/lingzhi227/agent-research-skills) - by [lingzhi227](https://github.com/lingzhi227) · `No License` · `net`.<br>31 full-lifecycle skills distilled from 17 LLM-agent repos — useful breadth, but unlicensed and rough-edged.
- `Suite` [awesome-gaussian-skills](https://github.com/jaccen/awesome-gaussian-skills) - by [jaccen](https://github.com/jaccen) · `Apache-2.0` · `net`.<br>Discipline pack for 3D Gaussian Splatting / NeRF research: a 600+ method catalog with an interactive explorer plus skills for paper tracking, CUDA-kernel review, and spatial-intelligence Q&A. Strong for graphics researchers; uses a Bash wildcard.
- [remote-sensing-research-radar](https://github.com/limi124/remote-sensing-research-radar) - by [limi124](https://github.com/limi124) · `No License`.<br>Remote-sensing research-frontier radar: scans arXiv/Papers-with-Code/GitHub/HF and venue pages for geospatial-AI and transferable-CV work, ranks by novelty/reproducibility/fit, drafts related-work tables. Niche but well-scoped; no LICENSE.

#### Social sciences

- `Suite` [academic-research-skills (economics)](https://github.com/franklee16/academic-research-skills) - by [franklee16](https://github.com/franklee16) · `No License`.<br>An economics/social-science pack useful for empirical economists, but lightly curated (near-duplicate skills) and unlicensed.
- `Suite` [ai-agent-research-starter-kit](https://github.com/drchronx/ai-agent-research-starter-kit) - by [drchronx](https://github.com/drchronx) · `NOASSERTION` · `net` `hooks`.<br>Chinese social-science research teaching pack with unusually deep methodology skills: causal inference (DID/RDD/IV/PSM), scale development, theory building, and EEG/ERP work, plus lit search and stats. Methods depth is its value; very large.
- `Suite` [education-agent-skills](https://github.com/GarethManning/education-agent-skills) - by [Gareth Manning](https://github.com/GarethManning) · `CC-BY-SA-4.0`.<br>The largest education pack — 165 evidence-based pedagogical skills across 20 domains; local install free, hosted MCP gated.
- `Suite` [open-science-skills](https://github.com/scdenney/open-science-skills) - by [scdenney](https://github.com/scdenney) · `NOASSERTION`.<br>Social-science methods suite from real methodological texts: conjoint design/cleaning/diagnostics, list-experiments, cross-national design, methods-reporting, FAIR/figure-table audits. Source-grounded; broad, so audit individual skills.

#### Humanities, law & qualitative-research disciplines

- `Suite` [ai-anthropology-toolkit](https://github.com/mattartzanthro/ai-anthropology-toolkit) - by [mattartzanthro](https://github.com/mattartzanthro) · `NOASSERTION`.<br>Qualitative-research skills for anthropology — peer review, manuscript evaluation, revision strategy — that treat epistemic stance as a design parameter rather than an afterthought. Scholarly and self-aware; confirm the license terms.
- `Suite` [claude-skills-journalism](https://github.com/jamditis/claude-skills-journalism) - by [Joe Amditis](https://github.com/jamditis) · `MIT` · `net` `hooks`.<br>A journalism pack whose academic core is its research-toolkit: legal paywall-bypass via Unpaywall, web archiving, change-monitoring.
- `Suite` [tw-research-skills](https://github.com/fw1201/tw-research-skills) - by [fw1201](https://github.com/fw1201) · `No License`.<br>A full Taiwanese-academic lifecycle pack (proposals to submission), strong on qualitative methods (grounded theory, content analysis with Kappa) and TSSCI/NSC norms. Localized but broadly useful; confirm the license.
- [genealogy-research](https://github.com/sliday/genealogy-research) - by [sliday](https://github.com/sliday) · `MIT`.<br>Applies the Genealogical Proof Standard to family-history research — multilingual handwritten-record reading, evidence-level tracking, negative-result logging, GEDCOM and an Obsidian knowledge base. Specialist, but methodologically serious.
- [oh-my-hermes-for-legal-researcher](https://github.com/charliehotel/oh-my-hermes-for-legal-researcher) - by [charliehotel](https://github.com/charliehotel) · `Apache-2.0` · `net`.<br>US legal-research methodology ported from Anthropic's claude-for-legal: structured Federal Register digests, web-searched opinions tagged (verify), optional free CourtListener API for verified citations. No paid databases; US-only, candid on limits.

#### Cross-discipline / multi-field packs

- `Suite` [awesome-rosetta-skills](https://github.com/xjtulyc/awesome-rosetta-skills) - by [xjtulyc](https://github.com/xjtulyc) · `NOASSERTION` · `net` `hooks`.<br>Multi-discipline research-skills library: 169 skills across 24 fields (physics to linguistics to public health), each wiring domain data sources and methods. Unmatched breadth for non-CS disciplines; depth varies, license is NOASSERTION.

### Awesome Lists & Ecosystem Maps

> Other curated lists and maps of the agent-skill ecosystem — where to look next, beyond this index.

- `List` [Awesome AI for Economists](https://github.com/hanlulong/awesome-ai-for-economists) - by [Lu Han](https://github.com/hanlulong) · `CC0-1.0`.<br>A discipline-focused map of AI tools for economics research and teaching, from the OpenEcon team.
- `List` [Awesome AI for Science](https://github.com/ai-boost/awesome-ai-for-science) - by [AwesomeGPTS (ai-boost)](https://github.com/ai-boost) · `MIT`.<br>A broad AI4Science map of tools, papers and datasets — wider and more model-oriented than a skills list.
- `List` [Awesome Scientific Skills](https://github.com/InternScience/Awesome-Scientific-Skills) - by [Intern Science](https://github.com/InternScience) · `MIT`.<br>The closest active peer — a curated awesome-list of agent skills for science. Cross-reference, don't race.
- `List` [Awesome-AI-Scientists](https://github.com/tsinghua-fib-lab/Awesome-AI-Scientists) - by [FIB Lab, Tsinghua University](https://github.com/tsinghua-fib-lab) · `MIT`.<br>The reading list behind Tsinghua FIB Lab's AI-Scientists survey — a paper-centric map of the literature.

## At a glance

**Type** Every entry is a Claude/agent skill; only the distinguishing kinds are tagged — `Suite` · `Plugin` · `List`. An untagged entry is a single skill.
<br/>
**What it runs** Capability tags are the skill's own disclosed behaviour, not a safety rating: `net` = makes network calls; `hooks` = runs lifecycle hooks; `bypass` = needs permission-bypass; `⚠ disclosure` = the declaration disagrees with the code. Untagged = none of these. Always review third-party code before running it.

| Lifecycle stage        | Categories | Skills |
| ---------------------- | ---------: | -----: |
| Discover & Collect     |          2 |     20 |
| Read & Understand      |          2 |     23 |
| Analyze & Visualize    |          2 |     24 |
| Write & Refine         |          2 |     52 |
| Review & Publish       |          2 |     25 |
| Suites, Systems & Meta |          4 |     79 |
| Total                  |         14 |    223 |

## Recently updated

**avoid-ai-writing**, **daaf**, **humanizer-academic**, **Awesome AI for Science**, **academic-research-skills**. (Links and descriptions are in the lifecycle sections above.)

## How to use this list

Organised by what researchers actually do, not alphabetically. Start from your current stage and move down the lifecycle: `Discover → Read → Analyze → Write → Review → Publish`

## What gets listed

*Included.* Open or source-available, with an identifiable license; Actively maintained, with a real README and a working repo; Genuinely useful to researchers — solves a real lifecycle task, not a generic wrapper; Inspectable: behaviour you can read and reason about.

*Excluded.* Closed SaaS with no inspectable skill / agent layer; Generic LLM wrappers with no academic-specific value; Abandoned or non-working repos; AI-generated slop, or submissions that merely restate a repo's own tagline.

## Curation, neutrality & security

This list is maintained by an author of some listed skills; those skills are held to the identical disclosure check, get no preferential placement, and sit in alphabetical order like every other entry.

<details>
<summary>How the disclosure check works (what the capability tags do and don't mean)</summary>

<br/>

Each entry declares its executable surface (network, hooks, bypass, tool scope). An open, deterministic script (`framework/`) reads the repo and reports the capabilities it can infer, then flags any place the declaration disagrees with the code. That is the whole claim: **disclosed facts, cross-checked — not a security audit, not a quality score, no pass/fail label.** We deliberately removed the earlier "analyzed/listed" severity verdict because static severity-guessing produced too many false positives to be trustworthy. Inclusion is a human curator's editorial call about scholarly usefulness, stated openly.

**Security.** Skills run code — Python, shell, hooks that can fire on lifecycle events. This list does **not** security-audit or rate them. What it does is surface each skill's own **disclosed behaviour** — does it make network calls, run hooks, need permission bypass — as plain capability tags, and check that disclosure against the code with an open, re-runnable script (`framework/`). **Tags are facts, not a safety rating; an untagged skill is not "verified safe."** Review the source yourself before running any skill in an institutional or sensitive environment, and see [SECURITY.md](SECURITY.md) to report one behaving badly.

</details>

## Contributing

Contributions are welcome, and most listed skills are self-submitted by their authors. See **CONTRIBUTING.md** for the two ways to contribute (a low-friction Issue Form or a YAML pull request), the eligibility bar, and the security disclosure every entry must make. Submissions are made by humans. See also our [Code of Conduct](CODE_OF_CONDUCT.md).
