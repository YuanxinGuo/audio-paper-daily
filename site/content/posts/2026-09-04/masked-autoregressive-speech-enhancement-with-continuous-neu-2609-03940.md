---
title: "Masked Autoregressive Speech Enhancement with Continuous Neural Audio Codec Representations"
date: 2026-09-04T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#语音增强"]
summary: "提出MARSE，利用连续神经音频编解码器表示进行掩码自回归语音增强，通过不同解码策略实现性能与计算开销的灵活权衡。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero hero-focus">
<div class="hero-score">
<div class="score-num">8.5</div>
<div class="score-stars">★★★★☆</div>
<div class="score-tier">前25%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#语音增强</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#掩码生成建模</span> <span class="tag-pill tag-pill-soft">#连续神经音频编解码器</span> <span class="tag-pill tag-pill-soft">#自回归解码</span> <span class="tag-pill tag-pill-soft">#Conformer</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2609.03940</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-09-04</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
<div class="meta-row"><span class="meta-key">⭐</span><span class="meta-val focus-badge">本站重点关注领域 · 评分 +1</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2609.03940" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2609.03940" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出MARSE，利用连续神经音频编解码器表示进行掩码自回归语音增强，通过不同解码策略实现性能与计算开销的灵活权衡。
</div>

## 👥 作者与机构

**Yoto Fujita** ¹ · Simon Leglaive · Laurent Girin

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合语音增强和生成式建模方向的研究者。建议重点阅读第3节（方法）和第4节（实验），特别是不同解码策略的对比分析。可先看摘要和结论，再深入方法细节。

## 🌍 研究背景

基于掩码生成建模的语音增强方法通常使用离散token表示，但近期研究表明连续潜在表示在语音质量和可懂度上更有优势。本文旨在探索使用连续NAC表示进行掩码自回归语音增强，并系统比较不同解码策略，以在性能和计算成本间取得平衡。

## 💡 核心创新

1. 提出MARSE框架，结合掩码建模与连续NAC表示
2. 系统比较多种解码策略（如并行、自回归等）
3. 在相同DNN、NAC和训练设置下进行公平对比
4. 实现性能与计算开销的灵活权衡

## 🏗️ 模型架构

输入含噪语音经DAC编码器得到连续潜在表示，按一定比例掩码后输入Conformer模型，通过迭代解码逐步预测掩码帧。解码策略包括并行解码、自回归解码等，最终由DAC解码器重建增强语音。

## 📊 实验结果

摘要未提供具体实验数值，但表明MARSE能实现性能与计算开销的灵活权衡，且音频示例和代码已公开。

## 🎯 结论与影响

MARSE验证了连续NAC表示在掩码自回归语音增强中的有效性，为生成式SE提供了新思路。其灵活的解码策略有助于适应不同资源约束场景，可能推动实时或低延迟SE应用的发展。

## ⚠️ 局限与未解决问题

摘要未提及具体性能数值，缺乏与强基线的定量对比；未讨论模型参数量、推理延迟等效率指标；解码策略的适用范围和局限性未明确。

---

<div class="paper-footer"><span>评分：8.5</span><span>原始：7.5</span><span>+1 重点领域加权</span><a href="/audio-paper-daily/posts/2026-09-04/">← 返回 2026-09-04 速递</a></div>
