---
title: "DEMON: Diffusion Engine for Musical Orchestrated Noise"
date: 2026-05-28T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#音乐生成"]
summary: "提出DEMON，一个基于扩散模型的实时音乐生成引擎，通过四种机制实现可演奏的降噪控制，在消费级GPU上达到每秒12.3次解码。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#音乐生成</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#扩散模型</span> <span class="tag-pill tag-pill-soft">#实时音频生成</span> <span class="tag-pill tag-pill-soft">#音乐交互</span> <span class="tag-pill tag-pill-soft">#流式推理</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2605.28657</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-05-28</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2605.28657" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2605.28657" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出DEMON，一个基于扩散模型的实时音乐生成引擎，通过四种机制实现可演奏的降噪控制，在消费级GPU上达到每秒12.3次解码。
</div>

## 👥 作者与机构

**Ryan Fosdick** ¹

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合对实时扩散模型、交互式音乐生成感兴趣的读者。建议重点阅读第3节（四种机制）和第4节（性能评估），特别是3.2节关于异构调度和3.4节窗口化VAE解码。

## 🌍 研究背景

扩散模型在音乐生成中取得显著进展，但实时交互控制仍是挑战。现有方法如StreamDiffusion采用环形缓冲区实现流式生成，但参数更新受限于缓冲区排空速率，无法实现即时响应。本文旨在将扩散模型的降噪过程转化为可演奏的乐器，要求控制既广泛（多参数逐帧调整）又响应迅速（控制效果尽快生效）。

## 💡 核心创新

1. 每槽异构降噪调度：每个环形缓冲区槽独立拥有时间步调度
2. 共享可变每步状态：参数在每一步立即生效，绕过缓冲区延迟
3. 逐帧源混合：在采样时控制SDE重噪步骤的变换强度
4. 窗口化VAE解码：利用感受野分析实现8倍解码加速

## 🏗️ 模型架构

基于ACE-Step 1.5和StreamDiffusion的环形缓冲区架构，结合TensorRT加速。输入为噪声和条件信号，通过环形缓冲区维护多个去噪步骤的中间状态。关键模块包括：每槽异构调度器（每个槽独立时间步）、共享可变状态层（参数即时生效）、逐帧源混合模块（控制变换强度）、窗口化VAE解码器（利用感受野分析加速）。输出为60秒音乐片段。

## 📚 数据集

- 未明确指定数据集（训练/评估）

## 📊 实验结果

摘要未提供具体客观指标对比，仅报告了在RTX 5090上每秒12.3次解码完成（60秒音乐）和11.3次生成（环深4）。缺乏与基线方法的定量比较，如FAD、IS等音乐生成指标。

## 🎯 结论与影响

DEMON通过四种机制将扩散模型转化为实时可演奏乐器，实现了参数控制的广泛性和响应性。该工作为交互式音乐生成提供了新范式，有望推动扩散模型在实时创意工具中的应用。工业上可用于现场表演和音乐制作软件。

## ⚠️ 局限与未解决问题

缺乏与现有音乐生成方法的定量对比（如FAD、CLAP分数）；未报告模型参数量和训练细节；仅测试了RTX 5090，泛化性未知；未讨论音频质量的主观评估；窗口化VAE解码可能引入边界伪影。

---

<div class="paper-footer"><span>评分：7.8</span><span>原始：7.8</span><a href="/audio-paper-daily/posts/2026-05-28/">← 返回 2026-05-28 速递</a></div>
