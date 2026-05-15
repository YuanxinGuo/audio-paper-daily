---
title: "BioSEN: A Bio-acoustic Signal Enhancement Network for Animal Vocalizations"
date: 2026-05-15T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#生物声学"]
summary: "BioSEN将语音增强方法适配到动物叫声增强，提出多尺度双轴注意力与谐波增强模块，在三个生物声学数据集上以更低计算量达到或超越SOTA语音增强模型。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#生物声学</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#语音增强方法</span> <span class="tag-pill tag-pill-soft">#生物声学</span> <span class="tag-pill tag-pill-soft">#注意力机制</span> <span class="tag-pill tag-pill-soft">#多尺度特征</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2605.12534</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-05-15</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2605.12534" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2605.12534" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>BioSEN将语音增强方法适配到动物叫声增强，提出多尺度双轴注意力与谐波增强模块，在三个生物声学数据集上以更低计算量达到或超越SOTA语音增强模型。
</div>

## 👥 作者与机构

**Tianyu Song** ¹ · Ton Viet Ta · Ngamta Thamwattana · Hisako Nomura · Linh Thi Hoai Nguyen

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合生物声学、语音增强领域研究者。建议重点阅读§3模型架构（多尺度双轴注意力与谐波增强单元）及§4实验对比（表1-3）。可关注其能量自适应门控连接如何避免误删动物叫声。

## 🌍 研究背景

音频增强主要面向人类语音，而生物声学信号因噪声多样、动物叫声谐波结构特殊而研究不足。现有语音增强模型直接应用于生物声学效果不佳，且计算开销大。本文旨在设计专用于动物叫声增强的轻量模型，提升生物多样性监测中的音频质量。

## 💡 核心创新

1. 多尺度双轴注意力单元提取时频特征
2. 生物谐波多尺度增强单元捕获谐波结构
3. 能量自适应门控连接防止误删目标叫声
4. 在三个生物声学数据集上验证有效性

## 🏗️ 模型架构

输入为对数梅尔谱，经多尺度双轴注意力单元（沿时间和频率轴分别应用注意力）提取时频特征；然后通过生物谐波多尺度增强单元（利用谐波模板增强周期性成分）处理；最后经能量自适应门控连接（基于频率权重调整门控）输出增强后的谱图。模型参数量未提及，但计算量显著低于基线。

## 📚 数据集

- Bioacoustic dataset A（训练/评估，未具体命名）
- Bioacoustic dataset B（训练/评估）
- Bioacoustic dataset C（训练/评估）

## 📊 实验结果

摘要未给出具体数值指标，仅说明BioSEN在三个生物声学数据集上匹配或超越SOTA语音增强模型，且计算量大幅降低。具体指标（如PESQ、SI-SDR）及对比基线未提供。

## 🎯 结论与影响

BioSEN成功将语音增强方法适配到生物声学领域，以更低计算量达到可比或更优的增强效果。该工作为生物多样性监测中的音频处理提供了高效方案，有望推动动物叫声自动分析在生态学中的应用。

## ⚠️ 局限与未解决问题

摘要未报告具体指标和对比基线，实验细节不足；未提及模型参数量、推理速度等效率指标；仅在三个数据集上测试，泛化性待验证；未与专门生物声学增强方法对比（可能缺乏此类基线）。

---

<div class="paper-footer"><span>评分：7.8</span><span>原始：7.8</span><a href="/audio-paper-daily/posts/2026-05-15/">← 返回 2026-05-15 速递</a></div>
