---
title: "Device Invariance using Domain Adaptation on Acoustic Scene Classification"
date: 2026-07-30T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#声学场景分类"]
summary: "研究域自适应技术（DANN和CDAN）在声学场景分类中对CNN和Transformer特征提取器的效果，发现DANN更稳定而CDAN仅适用于CNN。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#声学场景分类</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#域自适应</span> <span class="tag-pill tag-pill-soft">#CNN</span> <span class="tag-pill tag-pill-soft">#Transformer</span> <span class="tag-pill tag-pill-soft">#DCASE</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2607.25887</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-07-30</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2607.25887" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2607.25887" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>研究域自适应技术（DANN和CDAN）在声学场景分类中对CNN和Transformer特征提取器的效果，发现DANN更稳定而CDAN仅适用于CNN。
</div>

## 👥 作者与机构

**Abhishek dileep** ¹ · Shubham Sharma · Padmanabhan Rajan

**机构**：印度理工学院

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合声学场景分类或域自适应方向的研究者。可重点阅读第3节方法描述和第4节实验结果，特别是表1和表2的对比。建议关注DANN与CDAN在不同特征提取器上的表现差异。

## 🌍 研究背景

声学场景分类（ASC）中，不同录音设备导致的域偏移严重影响模型泛化性能。现有方法多采用域自适应技术缓解，但大多针对CNN特征提取器。随着Transformer在音频领域的兴起，其与域自适应方法的兼容性尚不明确。本文旨在系统评估DANN和CDAN在CNN和Transformer两种特征提取器下的域自适应效果，为实际应用提供指导。

## 💡 核心创新

1. 系统对比DANN和CDAN在CNN与Transformer特征提取器上的域自适应效果
2. 揭示CDAN对CNN有效但对Transformer无效的发现
3. 在DCASE 2020多设备数据集上验证结论

## 🏗️ 模型架构

采用两种特征提取器：CNN（如VGG-like）和Transformer（如AST）。域自适应模块分别使用DANN（梯度反转层）和CDAN（条件对抗网络）。输入为log-mel频谱图，经特征提取后送入域分类器，同时保留场景分类分支。整体为端到端训练。

## 📚 数据集

- DCASE 2020 ASC数据集（训练/评估，包含多个设备录音）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| 分类准确率（%） | DCASE 2020 | 无域自适应CNN 60.0 | **DANN+CNN 65.2** | +5.2% |
| 分类准确率（%） | DCASE 2020 | 无域自适应Transformer 62.5 | **DANN+Transformer 67.8** | +5.3% |

实验表明，DANN在CNN和Transformer特征提取器上均能稳定提升域自适应性能，准确率提升约5%。CDAN仅在CNN上有效（提升约4%），在Transformer上效果不佳甚至下降。消融实验验证了不同域偏移程度下的鲁棒性。

## 🎯 结论与影响

DANN是更通用的域自适应方法，适用于CNN和Transformer；CDAN需谨慎选择特征提取器。该发现为ASC系统设计提供了实用指导，建议优先采用DANN。未来可探索更复杂的自适应策略。

## ⚠️ 局限与未解决问题

仅评估了DCASE 2020单一数据集，泛化性未知。未分析计算开销和推理延迟。CDAN失效原因未深入探究（如特征对齐可视化）。缺少与其他域自适应方法（如CORAL、MMD）的对比。

---

<div class="paper-footer"><span>评分：6.5</span><span>原始：6.5</span><a href="/audio-paper-daily/posts/2026-07-30/">← 返回 2026-07-30 速递</a></div>
