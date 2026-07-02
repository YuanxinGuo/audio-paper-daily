---
title: "Evaluating Pretrained Music Embeddings for Cross-Performance Jazz Standard Recognition"
date: 2026-07-02T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#音乐检索"]
summary: "使用预训练音乐嵌入进行跨演奏爵士标准曲识别，发现预训练嵌入优于从头训练模型，但受演奏者身份影响。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero">
<div class="hero-score">
<div class="score-num">6.5</div>
<div class="score-stars">★★★☆☆</div>
<div class="score-tier">前50%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#音乐检索</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#爵士标准曲识别</span> <span class="tag-pill tag-pill-soft">#预训练音乐表征</span> <span class="tag-pill tag-pill-soft">#对比学习</span> <span class="tag-pill tag-pill-soft">#音乐信息检索</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2607.00777</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-07-02</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner"><div class="oc-headline"><span class="oc-pulse"></span><span class="oc-title">本论文已开源</span><span class="oc-hint">点击下方卡片直达对应资源</span></div><div class="oc-grid"><a class="oc-chip oc-chip-code" href="https://github.com/cagries/tipofmyear" target="_blank" rel="noopener"><span class="oc-icon">💻</span><span class="oc-text"><span class="oc-label">代码仓库</span><span class="oc-sub">cagries/tipofmyear</span></span></a></div></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2607.00777" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2607.00777" target="_blank" rel="noopener">📑 PDF</a><a class="rsrc rsrc-code" href="https://github.com/cagries/tipofmyear" target="_blank" rel="noopener">💻 代码</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>使用预训练音乐嵌入进行跨演奏爵士标准曲识别，发现预训练嵌入优于从头训练模型，但受演奏者身份影响。
</div>

## 👥 作者与机构

\c{C}a\u{g}r{\i} Eser

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合音乐信息检索和预训练音频模型研究者。可重点阅读§3实验设置和§4结果分析，特别是表1和表2。建议关注对比投影层对缓解演奏者偏差的效果。

## 🌍 研究背景

爵士标准曲识别是曲目级音乐检索的挑战性任务：同一标准曲的不同演奏在速度、调性、编曲、即兴内容甚至主旋律是否存在上均有差异。现有方法多从头训练谱图模型，但易过拟合于训练演奏。预训练音乐基础模型（如MERT、CLAP）在多种下游任务中表现优异，但其在跨演奏标准曲识别中的泛化能力尚未被系统评估。本文旨在填补这一空白。

## 💡 核心创新

1. 构建了Jazz Trio Database的跨演奏标准曲识别子集
2. 系统比较了从头训练与预训练嵌入的识别性能
3. 提出轻量对比投影层缓解演奏者身份偏差
4. 将爵士标准曲识别作为音乐表征模型的压力测试

## 🏗️ 模型架构

输入为音频片段（3秒），提取对数梅尔谱图。对比方法包括：1) 从头训练的Harmonic CNN基线（3层卷积+全连接）；2) 冻结的预训练嵌入（MERT、CLAP、MusicFM等）通过线性探针或最近邻检索进行分类；3) 预训练嵌入后接轻量对比投影层（MLP+对比损失）进行微调。输出为标准曲类别或检索排名。

## 📚 数据集

- Jazz Trio Database子集（训练/评估，包含多个演奏版本的标准曲）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| Top-1准确率 | Jazz Trio Database子集 | Harmonic CNN 0.35 | **MERT线性探针 0.52** | +0.17 |
| Top-5准确率 | Jazz Trio Database子集 | Harmonic CNN 0.60 | **MERT线性探针 0.78** | +0.18 |

预训练嵌入在Top-1和Top-5准确率上均显著优于从头训练模型（MERT线性探针Top-1 0.52 vs 0.35）。但预训练嵌入对演奏者身份敏感：同一标准曲不同演奏者间的检索性能下降。轻量对比投影层可部分缓解此问题，提升跨演奏泛化能力。消融实验表明，嵌入维度、训练数据规模对性能有影响。

## 🎯 结论与影响

预训练音乐嵌入在跨演奏爵士标准曲识别中优于从头训练模型，但存在演奏者偏差。本文表明该任务可作为音乐表征模型泛化能力的压力测试。未来可探索更有效的偏差消除方法，并扩展至更大规模数据集。对工业应用而言，预训练嵌入可快速部署于音乐检索系统。

## ⚠️ 局限与未解决问题

数据集规模较小（仅Jazz Trio Database子集），未在更大规模或更多风格上验证。未报告推理时间或计算开销。对比投影层的设计较简单，可能未完全消除演奏者偏差。缺乏与更先进微调方法（如适配器）的比较。

## 🔗 开源资源

- **代码**：<https://github.com/cagries/tipofmyear>

---

<div class="paper-footer"><span>评分：6.5</span><span>原始：6.5</span><a href="/audio-paper-daily/posts/2026-07-02/">← 返回 2026-07-02 速递</a></div>
