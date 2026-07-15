---
title: "CoFi-Lite: Pushing the Limits of Ultra-Lightweight Speech Enhancement"
date: 2026-07-15T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#语音增强"]
summary: "提出CoFi-Lite超轻量语音增强模型，通过粗-细双流编码器-解码器及跨路径融合模块，以极低计算量超越现有轻量基线。"
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
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#超轻量模型</span> <span class="tag-pill tag-pill-soft">#双流架构</span> <span class="tag-pill tag-pill-soft">#跨路径融合</span> <span class="tag-pill tag-pill-soft">#低复杂度</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2607.10142</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-07-15</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
<div class="meta-row"><span class="meta-key">⭐</span><span class="meta-val focus-badge">本站重点关注领域 · 评分 +1</span></div>
</div>
</div>

<div class="opensource-banner"><div class="oc-headline"><span class="oc-pulse"></span><span class="oc-title">本论文已开源</span><span class="oc-hint">点击下方卡片直达对应资源</span></div><div class="oc-grid"><a class="oc-chip oc-chip-demo" href="https://acceleration123.github.io/CoFiLite-demo/" target="_blank" rel="noopener"><span class="oc-icon">🔊</span><span class="oc-text"><span class="oc-label">在线 Demo</span><span class="oc-sub">acceleration123.github.io/CoFiLite-demo/</span></span></a></div></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2607.10142" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2607.10142" target="_blank" rel="noopener">📑 PDF</a><a class="rsrc rsrc-demo" href="https://acceleration123.github.io/CoFiLite-demo/" target="_blank" rel="noopener">🔊 Demo</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出CoFi-Lite超轻量语音增强模型，通过粗-细双流编码器-解码器及跨路径融合模块，以极低计算量超越现有轻量基线。
</div>

## 👥 作者与机构

**Leyan Yang** ¹ · Dahan Wang · Xiaobin Rong · Jiadong Zhao · Jing Lu

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合关注边缘设备部署和低复杂度语音增强的研究者。建议重点阅读§II架构设计和§III实验对比，特别是表1的复杂度与性能对比。可先看图1的模型结构。

## 🌍 研究背景

深度学习语音增强在边缘设备部署受限于计算资源。现有超轻量模型如GTCRN、AdaptCRN在MACs和参数量上已有优化，但进一步降低复杂度需要更精细的设计。本文旨在提出一种极低计算量的模型，在保持性能的同时将复杂度推向极限。

## 💡 核心创新

1. 粗-细双流编码器-解码器结构，分别提取全带包络和低频细节
2. Cross-Path Fusion (CPF) 模块实现双流特征交互
3. 仅12.87M MACs/s和83.12k参数，极低复杂度

## 🏗️ 模型架构

输入为带噪语音频谱，经两个并行的对称编码器-解码器路径：粗流处理全频带包络，细流处理低频细节。每个路径包含多个卷积块，中间通过Cross-Path Fusion (CPF)模块进行特征融合。CPF模块采用注意力机制或可学习权重交互两路特征。输出为增强后的频谱，经ISTFT得到时域波形。总参数量83.12k，MACs 12.87M。

## 📚 数据集

- DNS-Challenge (训练与评估，具体规模未提及)

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| MACs (M) | DNS-Challenge | GTCRN (31.97) | **12.87** | -59.7% |
| Params (k) | DNS-Challenge | GTCRN (未给出) | **83.12** | 未给出 |

CoFi-Lite在DNS-Challenge上以12.87M MACs超越GTCRN（31.97M MACs），计算量仅为GTCRN的40.26%。其放大版本性能与AdaptCRN相当，同时计算成本降低19.34%。具体性能指标（如PESQ、SI-SDR）摘要未给出，但声称优于GTCRN。

## 🎯 结论与影响

CoFi-Lite以极低计算量实现了优于GTCRN的性能，证明了粗-细双流设计在超轻量语音增强中的有效性。该工作为边缘设备上的实时语音增强提供了新思路，未来可探索更高效的融合机制或扩展到其他音频任务。

## ⚠️ 局限与未解决问题

摘要未提供具体性能指标（如PESQ、SI-SDR）的数值，仅声称优于基线，缺乏量化对比。未提及跨数据集泛化实验或实时因子（RTF）等效率指标。消融研究未详细说明CPF模块的贡献。

## 🔗 开源资源

- **Demo / 试听**：<https://acceleration123.github.io/CoFiLite-demo/>

---

<div class="paper-footer"><span>评分：9.2</span><span>原始：8.2</span><span>+1 重点领域加权</span><a href="/audio-paper-daily/posts/2026-07-15/">← 返回 2026-07-15 速递</a></div>
