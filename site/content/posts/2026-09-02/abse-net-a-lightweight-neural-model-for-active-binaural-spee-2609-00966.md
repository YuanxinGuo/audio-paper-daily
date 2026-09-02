---
title: "ABSE-NET: A Lightweight Neural Model for Active Binaural Speech Enhancement in Open-Fit Hearing Aids"
date: 2026-09-02T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#语音增强"]
summary: "提出ABSE-NET，将双耳MVDR与轻量级神经网络级联，在开放式助听器中联合增强语音并抑制声泄漏，无需耳内麦克风。"
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
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#双耳音频</span> <span class="tag-pill tag-pill-soft">#主动噪声控制</span> <span class="tag-pill tag-pill-soft">#轻量级网络</span> <span class="tag-pill tag-pill-soft">#助听器</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2609.00966</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-09-02</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
<div class="meta-row"><span class="meta-key">⭐</span><span class="meta-val focus-badge">本站重点关注领域 · 评分 +1</span></div>
</div>
</div>

<div class="opensource-banner"><div class="oc-headline"><span class="oc-pulse"></span><span class="oc-title">本论文已开源</span><span class="oc-hint">点击下方卡片直达对应资源</span></div><div class="oc-grid"><a class="oc-chip oc-chip-code" href="https://github.com/Bream101/ABSE-NET" target="_blank" rel="noopener"><span class="oc-icon">💻</span><span class="oc-text"><span class="oc-label">代码仓库</span><span class="oc-sub">Bream101/ABSE-NET</span></span></a></div></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2609.00966" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2609.00966" target="_blank" rel="noopener">📑 PDF</a><a class="rsrc rsrc-code" href="https://github.com/Bream101/ABSE-NET" target="_blank" rel="noopener">💻 代码</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出ABSE-NET，将双耳MVDR与轻量级神经网络级联，在开放式助听器中联合增强语音并抑制声泄漏，无需耳内麦克风。
</div>

## 👥 作者与机构

**De Hu** ¹ · Xue Du · Qingying Zhao · Qintuya Si

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合从事助听器算法、双耳语音增强或主动噪声控制的研究者。建议重点阅读第3节（方法）和第4节（实验），特别是LNN中的特征融合模块设计。可先看摘要和结论，再深入方法细节。

## 🌍 研究背景

开放式助听器佩戴舒适但存在声泄漏，影响双耳语音增强(BSE)性能。传统BSE+ANC方案依赖自适应滤波，需要耳内麦克风，实际部署受限。现有BSE方法未考虑声泄漏问题，导致增强效果下降。本文旨在设计一种无需耳内麦克风的轻量级主动BSE框架，同时处理目标语音增强和声泄漏抑制。

## 💡 核心创新

1. 级联BMVDR与轻量级神经网络，实现粗增强与精补偿
2. LNN同时抑制声泄漏并补偿BMVDR失真，无需耳内麦克风
3. 特征融合模块结合频时依赖学习与卷积注意力
4. 在开放助听器场景下验证优于现有方法
5. 开源代码，便于复现

## 🏗️ 模型架构

输入为双耳含噪语音，首先经过双耳MVDR(BMVDR)进行粗增强，得到初步增强信号。随后送入轻量级神经网络(LNN)，该网络采用编码器-解码器结构，中间包含特征融合模块，该模块由频时依赖学习（如Transformer或LSTM）和卷积注意力块组成，用于同时估计声泄漏并补偿BMVDR引入的失真。输出为增强后的双耳信号。整体级联设计实现主动BSE，无需额外耳内麦克风。

## 📊 实验结果

摘要中未提供具体实验数据，仅声称优于现有最先进方法。需查阅全文获取详细指标（如PESQ、SI-SDR等）和数据集信息。

## 🎯 结论与影响

ABSE-NET通过级联BMVDR与轻量级神经网络，在开放式助听器中实现了无需耳内麦克风的主动双耳语音增强，有效抑制声泄漏并提升语音质量。该工作为助听器算法提供了新思路，有望推动开放式助听器的实用化。后续研究可探索更高效的网络结构或与其他ANC方法结合。

## ⚠️ 局限与未解决问题

摘要未提供实验细节，缺乏与现有方法的定量对比，也未提及模型参数量、计算复杂度或实时性。作为审稿人，需关注其泛化能力（不同噪声、说话人）和实际硬件部署的可行性。

## 🔗 开源资源

- **代码**：<https://github.com/Bream101/ABSE-NET>

---

<div class="paper-footer"><span>评分：8.8</span><span>原始：7.8</span><span>+1 重点领域加权</span><a href="/audio-paper-daily/posts/2026-09-02/">← 返回 2026-09-02 速递</a></div>
