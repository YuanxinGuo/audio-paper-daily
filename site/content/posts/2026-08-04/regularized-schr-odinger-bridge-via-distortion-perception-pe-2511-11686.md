---
title: "Regularized Schr\\\"odinger Bridge via Distortion-Perception Perturbation for High-Fidelity Speech Enhancement"
date: 2026-08-04T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#语音增强"]
summary: "提出正则化Schrödinger桥（RSB），通过失真-感知扰动缓解暴露偏差，在语音增强中兼顾保真度与感知质量。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero hero-focus">
<div class="hero-score">
<div class="score-num">9.2</div>
<div class="score-stars">★★★★★</div>
<div class="score-tier">前25%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#语音增强</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#扩散模型</span> <span class="tag-pill tag-pill-soft">#Schrödinger Bridge</span> <span class="tag-pill tag-pill-soft">#失真-感知权衡</span> <span class="tag-pill tag-pill-soft">#暴露偏差</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2511.11686</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-08-04</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
<div class="meta-row"><span class="meta-key">⭐</span><span class="meta-val focus-badge">本站重点关注领域 · 评分 +1</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2511.11686" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2511.11686" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出正则化Schrödinger桥（RSB），通过失真-感知扰动缓解暴露偏差，在语音增强中兼顾保真度与感知质量。
</div>

## 👥 作者与机构

**Qing Yao** ¹ · Lijian Gao · Qirong Mao · Ming Dong

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合从事语音增强和扩散模型研究的读者。建议重点阅读第3节（方法）和第4节（实验），特别是RSB的训练策略和与标准SB的对比。可先看摘要和结论，再深入方法细节。

## 🌍 研究背景

语音增强需在保真度和感知质量间权衡。扩散模型如Schrödinger桥（SB）通过桥接退化与干净语音分布，实现高质量重建，但存在保真度-感知权衡和暴露偏差问题。标准SB训练导致预测漂移，放大误差累积。本文旨在通过正则化训练缓解这些问题，提高增强语音的保真度。

## 💡 核心创新

1. 提出失真-感知扰动，构造时间变化目标
2. 在扰动中间状态上训练，模拟推理误差
3. 注入后验均值估计作为保真度引导
4. 缓解训练-推理不匹配，减轻暴露偏差
5. 统一保真度与感知质量，提升重建精度

## 🏗️ 模型架构

RSB基于Schrödinger桥框架，输入含噪语音，通过扩散过程逐步去噪。训练时，构造失真-感知扰动：在干净语音和后验均值估计之间插值生成目标，并在扰动状态上训练网络，使其逐步向真实值校正。推理时，采用多步采样，利用学习到的校正能力减少误差累积。

## 📊 实验结果

摘要未提供具体实验数值，但声称RSB在保真度和感知质量上优于标准SB，并有效缓解暴露偏差。具体指标和数据集未提及，需查阅全文获取。

## 🎯 结论与影响

RSB通过正则化训练解决了扩散模型在语音增强中的保真度-感知权衡和暴露偏差问题，显著提升重建质量。该方法为生成式语音增强提供了新思路，有望推动高保真语音增强的实用化。

## ⚠️ 局限与未解决问题

摘要未提及局限，但可能包括：计算开销增加、对后验均值估计的依赖、以及未在多种噪声场景下验证。此外，缺乏与最新非扩散方法的对比。

---

<div class="paper-footer"><span>评分：9.2</span><span>原始：8.2</span><span>+1 重点领域加权</span><a href="/audio-paper-daily/posts/2026-08-04/">← 返回 2026-08-04 速递</a></div>
