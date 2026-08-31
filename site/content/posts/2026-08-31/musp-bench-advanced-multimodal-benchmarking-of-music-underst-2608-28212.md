---
title: "MuSP-Bench: Advanced Multimodal Benchmarking of Music Understanding across Score and Performance"
date: 2026-08-31T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#音乐理解"]
summary: "提出MuSP-Bench，一个包含490个问题的多模态音乐理解基准，评估前沿模型在乐谱与演奏音频上的表现，发现模型在两者上均存在显著困难。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#音乐理解</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#多模态大语言模型</span> <span class="tag-pill tag-pill-soft">#乐谱理解</span> <span class="tag-pill tag-pill-soft">#音乐表演</span> <span class="tag-pill tag-pill-soft">#基准测试</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2608.28212</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-08-31</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner"><div class="oc-headline"><span class="oc-pulse"></span><span class="oc-title">本论文已开源</span><span class="oc-hint">点击下方卡片直达对应资源</span></div><div class="oc-grid"><a class="oc-chip oc-chip-proj" href="https://musp.vaclis.net/" target="_blank" rel="noopener"><span class="oc-icon">🌐</span><span class="oc-text"><span class="oc-label">项目主页</span><span class="oc-sub">musp.vaclis.net/</span></span></a></div></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2608.28212" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2608.28212" target="_blank" rel="noopener">📑 PDF</a><a class="rsrc rsrc-proj" href="https://musp.vaclis.net/" target="_blank" rel="noopener">🌐 项目主页</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出MuSP-Bench，一个包含490个问题的多模态音乐理解基准，评估前沿模型在乐谱与演奏音频上的表现，发现模型在两者上均存在显著困难。
</div>

## 👥 作者与机构

**Milan Liessens Dujardin** ¹ · Song-Ze Yu · Kevin Miao

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合多模态LLM、音乐信息检索研究者阅读。建议重点看基准设计（§3）与实验结果（§4），可先浏览问题示例和评估协议。若关注音乐理解评估，值得通读。

## 🌍 研究背景

音乐交流常通过乐谱和演奏两种模态进行，乐谱编码意图，演奏实现声音。现有基准多聚焦单一模态（如乐谱识别或音频分类），缺乏对跨模态理解与推理的评估。多模态大语言模型（如GPT-4V）在视觉-语言任务上表现优异，但在音乐领域，尤其是乐谱与演奏音频的联合理解上，缺乏系统性评测。本文旨在填补这一空白，通过构建人类撰写的基准，评估前沿模型在乐谱、演奏及跨模态推理上的能力。

## 💡 核心创新

1. 构建490个问题的人类撰写基准，覆盖乐谱、演奏、诠释与长程推理
2. 跨模态评估：同时输入乐谱图像与音频，考察多模态理解
3. 涵盖古典钢琴与管弦乐作品，增加多样性
4. 系统评估多个前沿多模态LLM，揭示其音乐理解短板

## 🏗️ 模型架构

MuSP-Bench本身不是模型，而是一个评估基准。其设计包括：输入形式为乐谱图像（如PDF或PNG）和演奏音频（如WAV），问题类型涵盖乐谱理解（如识别音符、调号）、演奏理解（如速度、力度）、诠释对比（如不同演奏版本差异）以及长程推理（如结构分析）。评估协议要求模型以多模态输入（图像+音频）生成答案，并与人类标注的参考答案比较。

## 📚 数据集

- MuSP-Bench（评估，490个问题，涵盖古典钢琴与管弦乐作品）

## 📊 实验结果

摘要未提供具体数值结果，仅指出模型在乐谱理解上表现挣扎，在演奏音频推理上挑战更大。未报告具体准确率或对比基线，需查阅论文获取详细数据。

## 🎯 结论与影响

MuSP-Bench揭示了当前多模态LLM在音乐理解上的显著不足，尤其在乐谱与演奏音频的跨模态推理上。该基准为音乐AI评估提供了新资源，有望推动多模态模型在音乐领域的改进。对工业界，可能影响音乐教育、自动乐谱识别等应用的发展方向。

## ⚠️ 局限与未解决问题

摘要未提及局限。作为审稿人，可能的问题包括：基准规模较小（490题），覆盖风格有限（仅古典钢琴与管弦乐）；未提供人类基线对比；未分析模型错误类型；未讨论问题难度分布。

## 🔗 开源资源

- **项目主页**：<https://musp.vaclis.net/>

---

<div class="paper-footer"><span>评分：7.2</span><span>原始：7.2</span><a href="/audio-paper-daily/posts/2026-08-31/">← 返回 2026-08-31 速递</a></div>
