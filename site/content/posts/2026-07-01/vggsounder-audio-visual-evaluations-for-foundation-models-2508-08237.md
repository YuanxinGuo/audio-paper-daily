---
title: "VGGSounder: Audio-Visual Evaluations for Foundation Models"
date: 2026-07-01T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#多模态评估"]
summary: "重新标注VGGSound数据集，构建多标签测试集VGGSounder，用于更可靠地评估音频-视觉基础模型。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#多模态评估</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#音频-视觉</span> <span class="tag-pill tag-pill-soft">#数据集</span> <span class="tag-pill tag-pill-soft">#基础模型评估</span> <span class="tag-pill tag-pill-soft">#多模态理解</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2508.08237</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-07-01</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2508.08237" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2508.08237" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>重新标注VGGSound数据集，构建多标签测试集VGGSounder，用于更可靠地评估音频-视觉基础模型。
</div>

## 👥 作者与机构

**Daniil Zverev** ¹ · Thadd\"aus Wiedemer · Ameya Prabhu · Matthias Bethge · Wieland Brendel · A. Sophia Koepke

**机构**：图宾根大学 · 马克斯·普朗克智能系统研究所

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合从事多模态基础模型评估的研究者阅读。建议重点看§3（数据集构建）和§4（实验分析），了解标注问题和模态混淆度量。

## 🌍 研究背景

音频-视觉基础模型需要可靠的多模态理解评估。VGGSound数据集广泛用于此任务，但存在标注不完整、类别重叠、模态不对齐等问题，导致评估失真。本文旨在通过重新标注和扩展VGGSound来解决这些局限。

## 💡 核心创新

1. 提出VGGSounder多标签测试集
2. 详细模态标注支持模态特定性能分析
3. 引入模态混淆度量评估性能退化

## 🏗️ 模型架构

无模型架构，主要贡献为数据集构建：基于VGGSound原始视频，进行人工重新标注，生成多标签（音频、视觉、音频-视觉）标注，并设计模态混淆度量。

## 📚 数据集

- VGGSound（原始数据集，用于分析局限）
- VGGSounder（新构建的多标签测试集，用于评估）

## 📊 实验结果

摘要未提供具体实验数值，但通过分析VGGSound的局限和VGGSounder的构建，展示了新测试集在评估音频-视觉模型时的有效性，并利用模态混淆度量揭示了模型在添加另一模态时的性能退化。

## 🎯 结论与影响

VGGSounder提供了更可靠的音频-视觉基础模型评估基准，通过详细模态标注和混淆度量，有助于深入理解模型的多模态能力。对后续多模态评估研究具有参考价值，可能推动更严谨的基准构建。

## ⚠️ 局限与未解决问题

仅构建测试集，未提供训练集或验证集；未在多种模型上展示广泛结果；模态混淆度量的有效性需更多验证。

---

<div class="paper-footer"><span>评分：6.5</span><span>原始：6.5</span><a href="/audio-paper-daily/posts/2026-07-01/">← 返回 2026-07-01 速递</a></div>
