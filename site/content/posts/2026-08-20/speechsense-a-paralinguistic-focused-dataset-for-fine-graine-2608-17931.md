---
title: "SpeechSense: A Paralinguistic-Focused Dataset for Fine-Grained Speech Sentiment Analysis"
date: 2026-08-20T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#语音情感分析"]
summary: "提出SpeechSense数据集，聚焦通过韵律线索检测八类人际立场，验证声学信息在细粒度语音情感分析中的关键作用。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero">
<div class="hero-score">
<div class="score-num">7.2</div>
<div class="score-stars">★★★★☆</div>
<div class="score-tier">前25%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#语音情感分析</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#语音情感分析</span> <span class="tag-pill tag-pill-soft">#数据集</span> <span class="tag-pill tag-pill-soft">#副语言</span> <span class="tag-pill tag-pill-soft">#多模态</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2608.17931</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-08-20</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner"><div class="oc-headline"><span class="oc-pulse"></span><span class="oc-title">本论文已开源</span><span class="oc-hint">点击下方卡片直达对应资源</span></div><div class="oc-grid"><a class="oc-chip oc-chip-code" href="https://github.com/Sher13cked/SpeechSense" target="_blank" rel="noopener"><span class="oc-icon">💻</span><span class="oc-text"><span class="oc-label">代码仓库</span><span class="oc-sub">Sher13cked/SpeechSense</span></span></a></div></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2608.17931" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2608.17931" target="_blank" rel="noopener">📑 PDF</a><a class="rsrc rsrc-code" href="https://github.com/Sher13cked/SpeechSense" target="_blank" rel="noopener">💻 代码</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出SpeechSense数据集，聚焦通过韵律线索检测八类人际立场，验证声学信息在细粒度语音情感分析中的关键作用。
</div>

## 👥 作者与机构

**Shicheng Ma** ¹ · Wenqian Cui · Irwin King

**机构**：香港中文大学

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合语音情感分析、副语言信息建模及多模态学习研究者阅读。建议重点阅读第3节（数据集构建）和第4节（实验对比），可先看表2和表3了解性能差异。若关注数据构建方法，可细读第3.2节的高保真语音合成与人工验证流程。

## 🌍 研究背景

语音情感分析旨在从语音中解码说话人的态度和情感，对招聘、客服等应用至关重要。现有方法多采用级联ASR与文本分析的文本中心管线，丢失韵律、语调等声学特征，难以捕捉声学模糊话语中的态度含义。同时，现有基准标签粒度粗，侧重基本情绪（如快乐、悲伤），缺乏人际立场（如自信、不耐烦）等细微维度。本文针对这两个局限，提出SpeechSense数据集，专门用于细粒度语音情感分析。

## 💡 核心创新

1. 定义8类人际立场分类法，基于韵律线索而非词汇内容
2. 构建高保真语音合成与人工验证的数据集构建流程
3. 系统对比多模态LLM、文本LLM和语音编码器，验证声学信息优势

## 🏗️ 模型架构

论文提出数据集而非模型，但实验涉及多种模型架构：多模态LLM（如Qwen-Audio）、文本LLM（如GPT-4）、语音编码器（如Wav2Vec2）。输入为语音或文本，多模态模型融合声学特征与文本，文本模型仅处理转录文本。输出为8类人际立场的分类结果。数据集构建采用语音合成生成候选样本，经人工验证确保标签质量。

## 📚 数据集

- SpeechSense（训练/评估，包含8类人际立场，规模未明确）
- MELD（评估，用于对比基本情绪）
- IEMOCAP（评估，用于对比基本情绪）

## 📊 实验结果

摘要未提供具体数值指标，但指出实验表明具有声学访问的模型（多模态LLM、语音编码器）在检测细微说话人态度上一致优于纯文本基线，验证了声学线索的首要性。具体性能数据需查阅论文正文。

## 🎯 结论与影响

SpeechSense数据集填补了细粒度语音情感分析中人际立场标注的空白，实证表明声学信息对捕捉微妙态度至关重要。该数据集有望推动语音情感分析从基本情绪向更细腻的社会信号建模发展，对招聘、客服等需要人际感知的工业应用具有潜在价值。

## ⚠️ 局限与未解决问题

数据集基于语音合成构建，可能缺乏真实语音的自然变异性；8类分类法可能未覆盖所有相关立场；实验对比未提供具体数值，难以量化改进幅度；未讨论跨语言泛化性。

## 🔗 开源资源

- **代码**：<https://github.com/Sher13cked/SpeechSense>

---

<div class="paper-footer"><span>评分：7.2</span><span>原始：7.2</span><a href="/audio-paper-daily/posts/2026-08-20/">← 返回 2026-08-20 速递</a></div>
