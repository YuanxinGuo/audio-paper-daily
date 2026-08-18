---
title: "SALSA-V: Shortcut-Augmented Long-form Synchronized Audio from Videos"
date: 2026-08-18T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#视频到音频生成"]
summary: "提出SALSA-V，一种基于掩码扩散目标与捷径损失的视频到音频生成模型，能以少步采样生成高同步、高保真长时音频。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero">
<div class="hero-score">
<div class="score-num">8.2</div>
<div class="score-stars">★★★★☆</div>
<div class="score-tier">前25%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#视频到音频生成</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#扩散模型</span> <span class="tag-pill tag-pill-soft">#多模态</span> <span class="tag-pill tag-pill-soft">#长时音频生成</span> <span class="tag-pill tag-pill-soft">#同步</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2510.02916</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-08-18</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2510.02916" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2510.02916" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出SALSA-V，一种基于掩码扩散目标与捷径损失的视频到音频生成模型，能以少步采样生成高同步、高保真长时音频。
</div>

## 👥 作者与机构

**Amir Dellali** ¹ · Luca A. Lanzend\"orfer · Florian Gr\"otschla · Roger Wattenhofer

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合音频生成、多模态学习研究者阅读。建议重点看第3节方法（掩码扩散与捷径损失）和第4节实验（同步性评估）。可先看摘要与图1了解整体框架，再深入方法细节。

## 🌍 研究背景

视频到音频生成旨在为无声视频合成匹配的音频，是多媒体与音频生成交叉领域的热点。现有方法如SpecVQGAN、Diff-Foley等虽能生成音频，但在长序列生成、同步精度和采样效率上存在局限。SALSA-V通过引入掩码扩散目标实现任意长度音频生成，并利用捷径损失加速采样，解决上述痛点。

## 💡 核心创新

1. 掩码扩散目标支持音频条件生成与任意长度序列
2. 捷径损失实现8步快速采样，无需微调
3. 随机掩码训练使模型匹配参考音频频谱特性
4. 在同步性和音频质量上超越现有SOTA

## 🏗️ 模型架构

SALSA-V采用基于扩散的生成框架，输入为视频帧序列（可能包含光流或特征），通过编码器提取视觉特征，然后以这些特征为条件，在潜空间进行扩散过程。主干网络可能采用U-Net或Transformer结构，关键模块包括掩码扩散目标（训练时随机掩码部分音频条件）和捷径损失（加速采样）。输出为梅尔频谱图，经声码器合成波形。

## 📊 实验结果

摘要中未提供具体数值指标，但提到在定量评估和人类试听研究中，SALSA-V在视听对齐和同步性上显著优于现有方法。同时，随机掩码训练使模型能匹配参考音频频谱特性，适用于Foley生成和声音设计。

## 🎯 结论与影响

SALSA-V通过掩码扩散和捷径损失实现了高效、高质量的长时视频到音频生成，显著提升了同步性，为实时应用铺路。其随机掩码训练扩展了模型在专业音频合成中的适用性，对多媒体内容创作和辅助听觉场景有重要影响。

## ⚠️ 局限与未解决问题

摘要未提及局限，但作为审稿人，可能存在的问题包括：未报告具体数据集和指标，缺乏与更多基线方法的对比，未讨论模型参数量和推理延迟，以及长时生成中的累积误差。

---

<div class="paper-footer"><span>评分：8.2</span><span>原始：8.2</span><a href="/audio-paper-daily/posts/2026-08-18/">← 返回 2026-08-18 速递</a></div>
