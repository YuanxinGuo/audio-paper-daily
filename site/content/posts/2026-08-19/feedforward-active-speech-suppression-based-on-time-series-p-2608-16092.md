---
title: "Feedforward Active Speech Suppression Based on Time Series Prediction of Speech Signals Using Neural Networks"
date: 2026-08-19T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#主动噪声控制"]
summary: "提出一种基于神经网络时间序列预测的前馈主动语音抑制方法，通过预测未来信号改进控制滤波器更新，提升非平稳语音的降噪效果。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero">
<div class="hero-score">
<div class="score-num">6.8</div>
<div class="score-stars">★★★☆☆</div>
<div class="score-tier">前50%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#主动噪声控制</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#语音抑制</span> <span class="tag-pill tag-pill-soft">#时间序列预测</span> <span class="tag-pill tag-pill-soft">#神经网络</span> <span class="tag-pill tag-pill-soft">#自适应滤波</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2608.16092</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-08-19</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2608.16092" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2608.16092" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出一种基于神经网络时间序列预测的前馈主动语音抑制方法，通过预测未来信号改进控制滤波器更新，提升非平稳语音的降噪效果。
</div>

## 👥 作者与机构

**Manami Nishikata** ¹ · Shoichi Koyama

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合主动噪声控制、语音增强和自适应滤波领域的研究者。建议重点阅读方法部分（第3节）和实验部分（第4节），了解预测信号如何融入滤波器更新。可先看摘要和结论，再深入方法细节。

## 🌍 研究背景

主动噪声控制（ANC）在抑制平稳噪声方面已取得显著效果，但面对高度非平稳的语音信号仍具挑战。现有前馈ANC方法通常依赖参考麦克风信号，对语音这类快速变化的信号难以实时跟踪。本文提出利用神经网络进行时间序列预测，提前获取未来信号，从而改进线性控制滤波器的更新，以更好地抑制语音。

## 💡 核心创新

1. 利用神经网络预测未来语音信号，用于前馈ANC
2. 基于预测信号和当前/过去信号计算控制滤波器更新值
3. 在真实预测和神经网络预测两种情况下均验证了降噪改进

## 🏗️ 模型架构

输入为参考麦克风信号（当前及过去样本），通过神经网络预测未来信号。预测信号与当前、过去信号共同用于计算线性控制滤波器的更新值。控制滤波器为自适应线性滤波器，输出用于驱动扬声器产生反相声波。神经网络结构未在摘要中详述，但属于时间序列预测模型。

## 📊 实验结果

摘要中未提供具体数值指标，仅说明数值实验表明在真实预测信号和神经网络预测信号两种情况下，噪声降低均有改进。具体降噪量、数据集和对比方法未提及。

## 🎯 结论与影响

本文提出了一种基于神经网络时间序列预测的前馈主动语音抑制方法，通过预测未来信号改进控制滤波器更新，有效提升了非平稳语音的降噪效果。该方法为ANC处理语音类非平稳噪声提供了新思路，有望推动主动噪声控制在语音场景的应用，如车内通话、耳机降噪等。

## ⚠️ 局限与未解决问题

摘要未提供实验细节，如数据集、基线对比、计算复杂度等。神经网络预测的实时性和准确性对系统性能影响较大，但未讨论推理延迟和模型复杂度。此外，仅验证了预测信号的有效性，未与现有ANC方法进行系统对比。

---

<div class="paper-footer"><span>评分：6.8</span><span>原始：6.8</span><a href="/audio-paper-daily/posts/2026-08-19/">← 返回 2026-08-19 速递</a></div>
