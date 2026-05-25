---
title: "Data Augmentation for Pathological Speech Enhancement"
date: 2026-05-25T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#语音增强"]
summary: "系统研究数据增强策略对帕金森病病理语音增强的效果，发现噪声增强最有效，生成式增强可能有害。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero hero-focus">
<div class="hero-score">
<div class="score-num">8.2</div>
<div class="score-stars">★★★★☆</div>
<div class="score-tier">前50%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#语音增强</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#数据增强</span> <span class="tag-pill tag-pill-soft">#病理语音</span> <span class="tag-pill tag-pill-soft">#帕金森病</span> <span class="tag-pill tag-pill-soft">#语音增强</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2602.14671</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-05-25</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
<div class="meta-row"><span class="meta-key">⭐</span><span class="meta-val focus-badge">本站重点关注领域 · 评分 +1</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2602.14671" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2602.14671" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>系统研究数据增强策略对帕金森病病理语音增强的效果，发现噪声增强最有效，生成式增强可能有害。
</div>

## 👥 作者与机构

**Mingchi Hou** ¹ · Enno Hermann · Ina Kodrasi

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合从事语音增强、病理语音处理的研究者阅读。建议重点看第3节（数据增强分类）和第4节（实验结果），尤其是表1和表2。可跳过第2节背景。

## 🌍 研究背景

现有语音增强模型在病理语音上性能显著下降，主要因为病理语音声学特征异常且数据稀缺。此前缺乏对数据增强策略在病理语音增强中的系统研究。本文针对帕金森病患者的病理语音，系统评估三类数据增强（变换式、生成式、噪声增强）对预测型和生成型语音增强模型的影响。

## 💡 核心创新

1. 首次系统比较三类数据增强在病理语音增强中的效果
2. 发现噪声增强对病理语音增强最有效且鲁棒
3. 揭示生成式增强随合成数据量增加可能损害性能
4. 指出数据增强对预测型模型更有利
5. 量化了病理与正常语音之间的性能差距

## 🏗️ 模型架构

本文不提出新模型，而是评估现有语音增强模型。预测型模型采用基于卷积循环网络（CRN）的架构，生成型模型采用基于扩散的生成模型。输入为带噪病理语音，输出为增强后的语音。

## 📚 数据集

- 帕金森病语音数据集（训练/评估，具体规模未提及）
- 神经典型语音数据集（训练/评估，具体规模未提及）

## 📊 实验结果

摘要未提供具体数值指标，但指出噪声增强在所有情况下提升最大且最稳定，变换式增强中等，生成式增强效果有限且随合成数据增加可能变差。数据增强对预测型模型更有利。尽管有提升，病理语音与正常语音之间仍存在性能差距。

## 🎯 结论与影响

本文系统评估了数据增强策略对病理语音增强的影响，发现噪声增强是最有效的方法。研究为病理语音增强的数据增强选择提供了指导，但病理与正常语音之间的性能差距表明需要更有针对性的策略。对工业落地，噪声增强易于实现且有效，但需注意生成式增强的潜在风险。

## ⚠️ 局限与未解决问题

仅针对帕金森病语音，未涉及其他病理类型；未报告具体指标数值，难以量化提升幅度；未进行跨数据集泛化测试；未讨论数据增强对模型推理效率的影响。

---

<div class="paper-footer"><span>评分：8.2</span><span>原始：7.2</span><span>+1 重点领域加权</span><a href="/audio-paper-daily/posts/2026-05-25/">← 返回 2026-05-25 速递</a></div>
