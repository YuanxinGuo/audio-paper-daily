---
title: "SlimDiffuSE: Towards Efficient Diffusion-Based Speech Enhancement using Slimmable Networks"
date: 2026-08-25T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#语音增强"]
summary: "提出SlimDiffuSE，利用可伸缩网络在扩散生成过程中动态调整网络宽度，在保持语音增强性能的同时大幅降低计算复杂度。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero hero-focus">
<div class="hero-score">
<div class="score-num">8.8</div>
<div class="score-stars">★★★★☆</div>
<div class="score-tier">前25%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#语音增强</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#扩散模型</span> <span class="tag-pill tag-pill-soft">#可伸缩网络</span> <span class="tag-pill tag-pill-soft">#计算效率</span> <span class="tag-pill tag-pill-soft">#语音增强</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2608.21188</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-08-25</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
<div class="meta-row"><span class="meta-key">⭐</span><span class="meta-val focus-badge">本站重点关注领域 · 评分 +1</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2608.21188" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2608.21188" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出SlimDiffuSE，利用可伸缩网络在扩散生成过程中动态调整网络宽度，在保持语音增强性能的同时大幅降低计算复杂度。
</div>

## 👥 作者与机构

**Nagashree K. S. Rao** ¹ · Shrishti Saha Shetu · Mohamed Elminshawi · Emanu\"el A. P. Habets · Andreas Brendel

**机构**：弗劳恩霍夫集成电路研究所 · 埃尔朗根-纽伦堡大学

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合研究扩散模型加速和语音增强的学者。建议重点阅读第3节（方法）和第4节（实验），特别是网络宽度调度优化部分。可先看摘要和结论，再深入方法细节。

## 🌍 研究背景

扩散模型在语音增强中取得SOTA性能，但需要多次迭代评估大型网络，计算复杂度高。现有加速方法如蒸馏或减少采样步数，但可能牺牲性能。本文提出在生成过程中动态调整网络宽度，以降低计算成本，同时保持性能。

## 💡 核心创新

1. 提出可伸缩扩散模型，在生成过程中动态调整网络宽度
2. 使用贪心搜索算法优化网络宽度调度
3. 实现高达87.5%的计算复杂度降低，性能几乎无损

## 🏗️ 模型架构

基于扩散模型的语音增强框架，采用U-Net作为主干网络，支持可伸缩宽度。在生成过程中，通过贪心搜索确定每个时间步的网络宽度，从而减少计算量。输入为带噪语音，输出为增强语音。

## 📚 数据集

- VoiceBank-DEMAND（训练和评估）
- DNS-Challenge（可能用于评估）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| PESQ | VoiceBank-DEMAND | 基线扩散模型（如DiffWave） | **相近** | 无显著下降 |
| SI-SDR | VoiceBank-DEMAND | 基线扩散模型 | **相近** | 无显著下降 |

实验表明，所提方法在PESQ和SI-SDR上与基线扩散模型相当，但计算复杂度降低高达87.5%。未提供具体数值，但强调性能无显著下降。

## 🎯 结论与影响

SlimDiffuSE通过可伸缩网络有效降低扩散模型的计算成本，同时保持语音增强性能，为扩散模型在资源受限场景下的应用提供了新思路。对后续研究有启发，可能推动扩散模型在实时语音增强中的落地。

## ⚠️ 局限与未解决问题

摘要未提供具体性能数值，缺乏与更多基线（如非扩散方法）的对比。未讨论推理延迟和实际加速效果。网络宽度调度的搜索可能增加训练成本。

---

<div class="paper-footer"><span>评分：8.8</span><span>原始：7.8</span><span>+1 重点领域加权</span><a href="/audio-paper-daily/posts/2026-08-25/">← 返回 2026-08-25 速递</a></div>
