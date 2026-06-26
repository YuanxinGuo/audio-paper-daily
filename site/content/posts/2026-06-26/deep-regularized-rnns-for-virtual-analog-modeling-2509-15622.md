---
title: "Deep Regularized RNNs for Virtual Analog Modeling"
date: 2026-06-26T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#音频处理"]
summary: "提出深度控制条件LSTM和伽马通滤波器组损失，在虚拟模拟建模中消除时变控制噪声伪影，同时保持建模精度。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero">
<div class="hero-score">
<div class="score-num">7.5</div>
<div class="score-stars">★★★★☆</div>
<div class="score-tier">前25%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#音频处理</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#虚拟模拟建模</span> <span class="tag-pill tag-pill-soft">#递归神经网络</span> <span class="tag-pill tag-pill-soft">#正则化</span> <span class="tag-pill tag-pill-soft">#音频处理</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2509.15622</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-06-26</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2509.15622" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2509.15622" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出深度控制条件LSTM和伽马通滤波器组损失，在虚拟模拟建模中消除时变控制噪声伪影，同时保持建模精度。
</div>

## 👥 作者与机构

**V. Valtteri Kallinen** ¹ · Lauri Juvela · Thom Sherson

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合音频建模和VA建模研究者。重点读§3方法部分和§4实验，特别是GFB损失和正则化效果。可先看表1对比结果。

## 🌍 研究背景

虚拟模拟建模旨在用数字信号处理模拟模拟音频硬件。黑盒方法常用RNN，但时变控制输入会产生噪声伪影。现有正则化方法虽减少伪影但牺牲精度。本文旨在消除伪影同时保持建模精度。

## 💡 核心创新

1. 深度控制条件LSTM架构
2. 伽马通滤波器组损失函数
3. 动力学正则化质量提升

## 🏗️ 模型架构

输入为音频样本和控制参数，经深度控制条件LSTM（多层LSTM，控制值作为条件输入）处理，输出模拟音频。训练时使用GFB损失，将输出和参考信号通过伽马通滤波器组后计算损失，正则化RNN动力学。

## 📚 数据集

- 吉他放大器数据集（训练/评估，具体规模未提及）

## 📊 实验结果

摘要未给出具体数值，但声称所提方法在建模性能上与未正则化基线相当，同时避免了时变控制输入引起的噪声伪影。

## 🎯 结论与影响

本文通过深度控制条件LSTM和GFB损失，在VA建模中实现了无伪影的时变控制，同时保持高精度。该方法有望推动黑盒VA建模的实用化，减少对白盒或灰盒方法的依赖。

## ⚠️ 局限与未解决问题

摘要未提及局限。可能的问题：仅在吉他放大器上评估，泛化性未知；未报告计算复杂度或推理速度；缺少与更多基线（如WaveNet）的对比。

---

<div class="paper-footer"><span>评分：7.5</span><span>原始：7.5</span><a href="/audio-paper-daily/posts/2026-06-26/">← 返回 2026-06-26 速递</a></div>
