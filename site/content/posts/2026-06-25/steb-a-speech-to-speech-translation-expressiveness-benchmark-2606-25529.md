---
title: "STEB: A Speech-to-Speech Translation Expressiveness Benchmark for Evaluating Beyond Translation Fidelity"
date: 2026-06-25T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#语音翻译"]
summary: "提出STEB基准，评估语音到语音翻译中的表现力（情感、场景风格、非语言声音）保留，发现现有系统在语义翻译上表现良好但表现力保留不足。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero">
<div class="hero-score">
<div class="score-num">7.8</div>
<div class="score-stars">★★★★☆</div>
<div class="score-tier">前25%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#语音翻译</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#语音翻译</span> <span class="tag-pill tag-pill-soft">#表现力评估</span> <span class="tag-pill tag-pill-soft">#情感保留</span> <span class="tag-pill tag-pill-soft">#非语言声音</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2606.25529</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-06-25</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner"><div class="oc-headline"><span class="oc-pulse"></span><span class="oc-title">本论文已开源</span><span class="oc-hint">点击下方卡片直达对应资源</span></div><div class="oc-grid"><a class="oc-chip oc-chip-proj" href="https://cmots.github.io/steb.github.io/" target="_blank" rel="noopener"><span class="oc-icon">🌐</span><span class="oc-text"><span class="oc-label">项目主页</span><span class="oc-sub">cmots.github.io/steb.github.io/</span></span></a><a class="oc-chip oc-chip-demo" href="https://cmots.github.io/steb.github.io/" target="_blank" rel="noopener"><span class="oc-icon">🔊</span><span class="oc-text"><span class="oc-label">在线 Demo</span><span class="oc-sub">cmots.github.io/steb.github.io/</span></span></a></div></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2606.25529" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2606.25529" target="_blank" rel="noopener">📑 PDF</a><a class="rsrc rsrc-proj" href="https://cmots.github.io/steb.github.io/" target="_blank" rel="noopener">🌐 项目主页</a><a class="rsrc rsrc-demo" href="https://cmots.github.io/steb.github.io/" target="_blank" rel="noopener">🔊 Demo</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出STEB基准，评估语音到语音翻译中的表现力（情感、场景风格、非语言声音）保留，发现现有系统在语义翻译上表现良好但表现力保留不足。
</div>

## 👥 作者与机构

**Sitong Cheng** ¹ · Weizhen Bian · Songjun Cao · Jin Li · Bei Liu · Chunyang Jiang · Yike Zhang · Weihao Wu · … 等 4 人

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合语音翻译、多模态评估研究者阅读。重点看§3（基准设计）和§5（实验结果），尤其是表2和表3。可先浏览demo页面了解评估框架。

## 🌍 研究背景

语音到语音翻译（S2ST）需同时保留词汇语义和表现力属性（情感、场景风格、非语言声音）。现有评估主要关注翻译保真度、说话人相似度等，缺乏对表现力的系统评估。由于跨语言目标语音难以大规模收集，基于参考的评估不实用。本文旨在构建一个无需参考的表现力评估基准。

## 💡 核心创新

1. 提出STEB基准，覆盖翻译保真度、说话人相似度、时长对齐及表现力维度
2. 设计caption-then-summarize框架，将语音转为结构化表现力属性
3. 使用LLM judge比较源与假设的表现力属性，无需参考语音
4. 人工验证表明与听者判断显著相关
5. 揭示语义翻译与表现力保留之间的差距

## 🏗️ 模型架构

STEB基准包含32.6小时中英双语语音数据，评估框架采用caption-then-summarize方法：首先用语音识别和表现力标注模型将源语音和假设语音转换为结构化表现力属性（情感、场景风格、非语言声音），然后使用LLM judge比较属性一致性。评估维度包括标准维度（翻译保真度、说话人相似度、时长对齐）和表现力维度（情感、场景风格、非语言声音保留）。

## 📚 数据集

- STEB（32.6小时中英双语，评估基准，包含多种情感和场景风格）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| 情感保留评分 | STEB | 级联系统最佳 3.82/5 | **N/A** | N/A |
| 非语言声音保留评分 | STEB | 级联系统最佳 2.31/5 | **N/A** | N/A |

评估了6个S2ST系统（级联、端到端、语音大语言模型）。级联系统在翻译保真度上表现强，但情感保留最高仅3.82/5，非语言声音保留最高2.31/5，表明表现力保留是开放挑战。人工验证显示评估框架与听者判断显著相关。

## 🎯 结论与影响

STEB揭示了现有S2ST系统在语义翻译与表现力保留之间的显著差距，情感和非语言声音保留尤为薄弱。该基准为未来研究提供了标准化评估工具，推动S2ST向更自然的人机交互发展。工业应用中，提升表现力保留可增强语音翻译的沉浸感和情感传达。

## ⚠️ 局限与未解决问题

基准仅覆盖中英语言对，其他语言对的表现力评估未验证。LLM judge可能引入偏见，且评估框架依赖语音识别和表现力标注模型的准确性。未报告推理延迟或计算开销。

## 🔗 开源资源

- **项目主页**：<https://cmots.github.io/steb.github.io/>
- **Demo / 试听**：<https://cmots.github.io/steb.github.io/>

---

<div class="paper-footer"><span>评分：7.8</span><span>原始：7.8</span><a href="/audio-paper-daily/posts/2026-06-25/">← 返回 2026-06-25 速递</a></div>
