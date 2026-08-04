---
title: "DRONEAUDIONET: Noise Suppression for Drone Audition-based Search and Rescue"
date: 2026-08-04T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#语音增强"]
summary: "提出DRONEAUDIONET，将源分离模型重构为无人机噪声估计器，通过可学习掩码缩放和残差校正，在极低SNR下提升语音增强与下游分类性能。"
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
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#无人机听觉</span> <span class="tag-pill tag-pill-soft">#噪声抑制</span> <span class="tag-pill tag-pill-soft">#语音增强</span> <span class="tag-pill tag-pill-soft">#声学场景分析</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2608.00875</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-08-04</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
<div class="meta-row"><span class="meta-key">⭐</span><span class="meta-val focus-badge">本站重点关注领域 · 评分 +1</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2608.00875" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2608.00875" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出DRONEAUDIONET，将源分离模型重构为无人机噪声估计器，通过可学习掩码缩放和残差校正，在极低SNR下提升语音增强与下游分类性能。
</div>

## 👥 作者与机构

**Chitralekha Gupta** ¹ · Soundarya Ramesh · Yifei Luo · Suranga Nanayakkara

**机构**：新加坡国立大学 · 南洋理工大学

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合从事无人机听觉、极端噪声下语音增强的研究者。建议重点阅读方法部分（掩码缩放与残差校正）和实验部分（跨域泛化）。可先看§3模型架构与表2结果，再决定是否通读。

## 🌍 研究背景

无人机搭载麦克风可实现空中声学场景分析，如搜救、野生动物监测。然而，无人机旋翼噪声在混合信号中常占主导，SNR低于-10 dB，使源恢复极具挑战。现有增强和分离方法多针对近平衡混合设计，在无人机听觉场景下性能大幅下降。本文旨在解决无人机主导噪声下的语音增强问题，提出专用模型以提升源恢复和下游分类性能。

## 💡 核心创新

1. 将源分离模型重构为无人机噪声估计器，利用噪声先验
2. 引入可学习掩码缩放机制，允许掩码幅度超过1
3. 增加加性残差校正项，提升噪声估计与源恢复精度
4. 在公开无人机听觉数据集上训练，并验证跨域泛化性

## 🏗️ 模型架构

DRONEAUDIONET采用源分离模型架构，输入为混合音频的时频特征。主干网络可能基于U-Net或类似编码器-解码器结构，用于估计无人机噪声。关键模块包括可学习的掩码缩放层，允许掩码值大于1，以及残差校正分支，用于细化噪声估计。输出为估计的无人机噪声和增强后的源信号。具体参数量未提及。

## 📚 数据集

- 公开无人机听觉数据集（训练与评估）
- 跨域数据集（评估，包含未见过的无人机硬件和飞行模式）

## 📊 实验结果

摘要未提供具体数值指标，但指出DRONEAUDIONET持续提升下游声音分类性能，尤其对人类语音改善最大。实验验证了跨域泛化能力，表明模型对未见过的无人机硬件和飞行模式具有鲁棒性。

## 🎯 结论与影响

DRONEAUDIONET通过针对无人机噪声的专门建模，显著提升了极低SNR下的源恢复和下游分类性能，证明了源分离方法在无人机辅助搜救等实际应用中的潜力。该工作强调了领域特定建模的重要性，为后续无人机听觉研究提供了新思路，并可能推动相关工业应用。

## ⚠️ 局限与未解决问题

摘要未提及模型参数量、推理延迟等效率指标，也未与最新增强方法进行对比。跨域测试仅涉及未见过的硬件和飞行模式，但未涵盖更多样化的环境噪声。此外，对语音增强的客观指标（如PESQ、SI-SDR）未报告，仅以下游分类性能间接评估。

---

<div class="paper-footer"><span>评分：8.8</span><span>原始：7.8</span><span>+1 重点领域加权</span><a href="/audio-paper-daily/posts/2026-08-04/">← 返回 2026-08-04 速递</a></div>
