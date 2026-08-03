---
title: "OmniVAE: An Audio-Video VAE with Cross-Modal Alignment for Joint Generation"
date: 2026-08-03T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#多模态生成"]
summary: "OmniVAE提出联合训练的音频-视频VAE，通过对比学习和语义蒸馏实现跨模态对齐，提升下游音视频联合生成质量。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#多模态生成</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#音视频联合生成</span> <span class="tag-pill tag-pill-soft">#跨模态对齐</span> <span class="tag-pill tag-pill-soft">#VAE</span> <span class="tag-pill tag-pill-soft">#对比学习</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2607.23855</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-08-03</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2607.23855" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2607.23855" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>OmniVAE提出联合训练的音频-视频VAE，通过对比学习和语义蒸馏实现跨模态对齐，提升下游音视频联合生成质量。
</div>

## 👥 作者与机构

**Jun Zhan** ¹ · Chen Yang · Yitian Gong · Donghua Yu · Kuangwei Chen · Wenbo Zhang · Kexin Huang · Qi Luo · … 等 18 人

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合从事多模态生成、音视频联合建模的研究者阅读。建议重点阅读第3节（方法）和第4节（实验），特别是对比学习目标和语义蒸馏的设计细节。可先看摘要和结论，再深入方法部分。

## 🌍 研究背景

当前生成模型趋向于联合生成同步的音频和视频，但音频和视频的结构差异使得细粒度跨模态对应困难。现有方法通常分别训练音频和视频VAE，导致潜在空间缺乏对齐，下游生成模型需从头学习跨模态同步。本文旨在通过联合训练音频-视频VAE，学习音频和视频潜在表示之间的细粒度语义对齐，以提升下游生成质量。

## 💡 核心创新

1. 联合训练音频-视频VAE，实现潜在空间对齐
2. 引入段级音频-视频对比学习目标，捕获时间-语义对应
3. 从预训练模态特定语义编码器蒸馏特征，增强潜在空间可学习性

## 🏗️ 模型架构

OmniVAE采用联合训练的音频-视频VAE架构。输入为成对的音频和视频片段，分别通过各自的编码器提取潜在表示。主干网络采用VAE结构，关键模块包括段级对比学习模块和语义蒸馏模块。对比学习模块对齐音频和视频潜在表示的时间-语义对应，语义蒸馏模块将预训练编码器的特征蒸馏到各模态潜在空间。输出为重构的音频和视频，以及对齐的潜在表示。

## 📊 实验结果

摘要中未提供具体数值指标，但声称对比学习和语义蒸馏目标均能一致提升潜在空间的可学习性，并转化为更高的生成质量和更准确的跨模态同步。实验细节需查阅论文正文。

## 🎯 结论与影响

OmniVAE证明了联合训练音频-视频VAE并引入跨模态对齐目标的重要性，为多模态生成提供了统一表示基础。该方法有望推动音视频联合生成领域的发展，并为工业界的多模态内容创作提供新思路。

## ⚠️ 局限与未解决问题

摘要未提及局限，但可能包括：对比学习对负样本选择敏感，语义蒸馏依赖预训练编码器质量，以及未报告推理效率或模型大小。此外，实验可能仅在特定数据集上验证，泛化性未知。

---

<div class="paper-footer"><span>评分：7.8</span><span>原始：7.8</span><a href="/audio-paper-daily/posts/2026-08-03/">← 返回 2026-08-03 速递</a></div>
