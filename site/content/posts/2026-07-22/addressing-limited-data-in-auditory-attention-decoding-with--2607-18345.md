---
title: "Addressing Limited Data in Auditory Attention Decoding with Diffusion Generative Models"
date: 2026-07-22T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#听觉注意解码"]
summary: "利用扩散概率模型生成合成EEG数据，增强听觉注意解码在短时间窗下的性能。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero">
<div class="hero-score">
<div class="score-num">7.2</div>
<div class="score-stars">★★★★☆</div>
<div class="score-tier">前50%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#听觉注意解码</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#扩散模型</span> <span class="tag-pill tag-pill-soft">#数据增强</span> <span class="tag-pill tag-pill-soft">#脑电图</span> <span class="tag-pill tag-pill-soft">#助听器</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2607.18345</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-07-22</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2607.18345" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2607.18345" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>利用扩散概率模型生成合成EEG数据，增强听觉注意解码在短时间窗下的性能。
</div>

## 👥 作者与机构

**David Rannaleet** ¹ · Victor Gunnarsson · Bo Bernhardsson · Martin A. Skoglund · Emina Alickovic

**机构**：隆德大学 · Oticon

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合从事AAD、EEG数据增强或助听器研究的读者。建议重点阅读§3（扩散模型生成方法）和§4（实验设置与结果），特别是表1和表2中的分类准确率对比。

## 🌍 研究背景

听觉注意解码（AAD）旨在从EEG信号中解码听者的注意力方向，用于助听器实时跟踪声源。然而，真实语音诱发的EEG数据稀缺，限制了深度学习模型在短时间窗（≤1s）下的性能。现有方法多依赖实测数据，泛化能力不足。本文提出使用扩散概率模型（DPM）生成合成EEG数据，以缓解数据匮乏问题。

## 💡 核心创新

1. 首次将扩散模型用于AAD的EEG数据生成
2. 提出条件扩散模型生成特定刺激下的EEG信号
3. 验证合成数据增强对短时间窗AAD分类的提升

## 🏗️ 模型架构

采用扩散概率模型（DPM）生成合成EEG数据。模型基于去噪扩散概率框架，前向过程逐步添加高斯噪声，反向过程通过神经网络（U-Net架构）学习去噪。输入为随机噪声和条件信息（如刺激类型），输出为生成的EEG信号。生成数据与真实EEG混合用于训练AAD分类器（基于CNN或LSTM）。

## 📚 数据集

- 公开AAD数据集（训练/评估，包含多说话人场景下的EEG和刺激信号）
- 合成EEG数据集（由DPM生成，用于数据增强）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| 分类准确率（%） | 公开AAD测试集 | 仅实测数据训练 72.3 | **实测+合成数据训练 78.1** | +5.8% |

实验表明，扩散模型生成的EEG信号在时域和频域特征上与真实数据相似。在LoA分类任务中，使用合成数据增强后，模型在1秒时间窗下的准确率从72.3%提升至78.1%（p<0.05），且在不同信噪比条件下均表现鲁棒。消融实验显示，条件扩散模型优于无条件生成。

## 🎯 结论与影响

本文证明扩散模型可生成逼真的EEG数据，有效缓解AAD训练数据不足问题，显著提升短时间窗下的解码性能。该工作为数据驱动的AAD模型在助听器中的实际部署提供了可行方案，并启发了其他神经信号处理领域的数据增强研究。

## ⚠️ 局限与未解决问题

合成数据与真实数据仍存在分布差异，未在多种EEG采集设备上验证；生成模型计算开销较大，实时性未评估；仅针对单一AAD数据集，泛化性需进一步验证。

---

<div class="paper-footer"><span>评分：7.2</span><span>原始：7.2</span><a href="/audio-paper-daily/posts/2026-07-22/">← 返回 2026-07-22 速递</a></div>
