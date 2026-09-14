---
title: "PhaseGAN: High-Fidelity Vocoder via Decoupled Amplitude and GAN-Driven Phase Reconstruction"
date: 2026-09-14T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#音频生成"]
summary: "PhaseGAN 提出 mel→幅度→相位的解耦重建流程，用 GAN 驱动相位估计，以约 500K 参数实现高保真声码器。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero">
<div class="hero-score">
<div class="score-num">7.0</div>
<div class="score-stars">★★★★☆</div>
<div class="score-tier">前50%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#音频生成</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#声码器</span> <span class="tag-pill tag-pill-soft">#相位重建</span> <span class="tag-pill tag-pill-soft">#GAN</span> <span class="tag-pill tag-pill-soft">#语音合成</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2609.12918</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-09-14</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner"><div class="oc-headline"><span class="oc-pulse"></span><span class="oc-title">本论文已开源</span><span class="oc-hint">点击下方卡片直达对应资源</span></div><div class="oc-grid"><a class="oc-chip oc-chip-demo" href="https://github.com/phasegan/phasegan-audio-demo" target="_blank" rel="noopener"><span class="oc-icon">🔊</span><span class="oc-text"><span class="oc-label">在线 Demo</span><span class="oc-sub">phasegan/phasegan-audio-demo</span></span></a></div></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2609.12918" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2609.12918" target="_blank" rel="noopener">📑 PDF</a><a class="rsrc rsrc-demo" href="https://github.com/phasegan/phasegan-audio-demo" target="_blank" rel="noopener">🔊 Demo</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>PhaseGAN 提出 mel→幅度→相位的解耦重建流程，用 GAN 驱动相位估计，以约 500K 参数实现高保真声码器。
</div>

## 👥 作者与机构

**Wenzheng Zhang** ¹ · Xueliang Zhang · Shulin He · Fei Zhao · Xin Liu · Pengjie Shen · Zhenlong Guo · Zixuan Xue · … 等 2 人

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合做 TTS 声码器、相位重建与轻量化音频生成的研究者与工程同学阅读。建议重点看 §3 的幅度/相位解耦设计与 GAN 判别器结构，以及参数量/计算量对比表；若关注边缘部署，先看紧凑版配置与推理开销。

## 🌍 研究背景

声码器是 TTS 系统的关键模块，HiFi-GAN、BigVGAN 等基于 GAN 的声码器已在幅度谱建模上取得较好效果，但相位重建仍不准确，直接限制音质与建模效率。多数方法隐式建模相位，或依赖额外相位损失，导致高保真与低算力难以兼得。本文针对相位重建这一瓶颈，提出解耦幅度与相位的重建流程，目标是在更少参数与计算量下超过现有 SOTA。

## 💡 核心创新

1. mel→幅度→相位解耦重建流程
2. GAN 驱动显式相位谱重建
3. 约 500K 参数、1 GMAC 的紧凑声码器
4. 未训练音乐数据却具跨域合成能力

## 🏗️ 模型架构

输入为 mel 频谱，主干先经幅度重建分支估计幅度谱，再由独立的相位重建分支在 GAN 框架下生成相位谱，二者组合后经 iSTFT 还原波形。幅度与相位采用不同方法论建模，避免单一网络同时拟合两种谱带来的耦合困难。紧凑版约 500K 参数、1 GMAC 计算量，面向边缘设备实时推理。摘要未给出具体网络层名与判别器细节。

## 📊 实验结果

摘要仅给出定性结论：PhaseGAN 在更少参数与更低计算量下超过 SOTA 基线，紧凑版约 500K 参数、1 GMAC；并称在未训练音乐数据的情况下展现音乐音频合成能力。摘要未提供 SI-SDR、PESQ、MOS 等具体数值，也未列出训练/评估数据集名称，无法量化对比。

## 🎯 结论与影响

最强结论是解耦幅度与相位、并用 GAN 显式重建相位，可在约 500K 参数下取得优于 SOTA 的保真度。若结果可复现，将推动轻量声码器向显式相位建模方向演进，并利好边缘 TTS 部署；跨域音乐合成能力也提示相位建模的通用性。

## ⚠️ 局限与未解决问题

摘要未给出任何量化指标、数据集与基线数值，难以判断提升幅度；缺少消融验证解耦设计与 GAN 相位分支各自贡献；未报告推理延迟与实时率；跨域音乐合成仅定性描述，缺乏客观评测。

## 🔗 开源资源

- **Demo / 试听**：<https://github.com/phasegan/phasegan-audio-demo>

---

<div class="paper-footer"><span>评分：7.0</span><span>原始：7.0</span><a href="/audio-paper-daily/posts/2026-09-14/">← 返回 2026-09-14 速递</a></div>
