---
title: "RT-Tango: Real-Time Distributed Binaural Speech Enhancement for Low-Power Hearing Aid Devices"
date: 2026-07-03T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#语音增强"]
summary: "提出RT-Tango，一种面向低功耗助听器的实时分布式双耳语音增强框架，通过ERB特征压缩、分组循环掩码估计和时域稀疏化降低计算量，在8ms延迟下达到竞争性性能。"
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
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#双耳音频</span> <span class="tag-pill tag-pill-soft">#低功耗</span> <span class="tag-pill tag-pill-soft">#实时处理</span> <span class="tag-pill tag-pill-soft">#助听器</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2607.01834</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-07-03</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
<div class="meta-row"><span class="meta-key">⭐</span><span class="meta-val focus-badge">本站重点关注领域 · 评分 +1</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2607.01834" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2607.01834" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出RT-Tango，一种面向低功耗助听器的实时分布式双耳语音增强框架，通过ERB特征压缩、分组循环掩码估计和时域稀疏化降低计算量，在8ms延迟下达到竞争性性能。
</div>

## 👥 作者与机构

**Z. Benslimane** ¹ · P. Chouteau · M. Poreba · F. Auzanneau · M. Szczepanski · F. Chersi · R. Serizel

**机构**：洛林大学 · 法国国家科学研究中心

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合从事助听器、可穿戴设备或低功耗语音增强的研究者阅读。建议重点读§3架构设计和§4实验部分，特别是表1的延迟与MACs对比。若对分布式系统感兴趣，可通读全文。

## 🌍 研究背景

双耳语音增强在助听器中至关重要，但现有方法多针对单通道，且实时性受限于延迟和计算成本。传统方法如波束成形性能有限，而深度学习方法虽效果好但计算量大，难以部署在低功耗设备上。本文旨在设计一个满足严格延迟（<10ms）和低计算量的分布式双耳增强框架。

## 💡 核心创新

1. ERB特征压缩降低输入维度
2. 分组循环掩码估计减少参数量
3. 时域稀疏化进一步降低MACs
4. 非对称STFT解耦频谱分辨率与算法延迟
5. 在线空间统计估计实现分布式处理

## 🏗️ 模型架构

输入双耳信号经非对称STFT（分析窗长与帧移解耦）提取频谱特征，然后通过ERB滤波器组压缩为子带特征。主干网络为分组循环神经网络（GRU），逐组估计时频掩码。为降低计算量，采用时域稀疏化（仅对活跃帧计算）。最后结合在线估计的空间统计（如IPD）进行后处理，输出增强信号。模型为因果且支持流式处理。

## 📚 数据集

- WSJ0-2mix（训练/评估，双耳版本）
- LibriMix（训练/评估，双耳版本）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| SI-SDR (dB) | WSJ0-2mix | DCCRN (14.2) | **15.1** | +0.9 dB |
| PESQ | WSJ0-2mix | DCCRN (2.85) | **2.93** | +0.08 |
| MACs (M) | WSJ0-2mix | DCCRN (120) | **45** | -62.5% |
| 延迟 (ms) | WSJ0-2mix | DCCRN (16) | **8** | -8 ms |

RT-Tango在WSJ0-2mix上以45M MACs和8ms延迟达到15.1 dB SI-SDR，优于DCCRN（120M MACs, 16ms, 14.2 dB）。在LibriMix上也有类似趋势。消融实验验证了ERB压缩和时域稀疏化的有效性，且分布式架构相比集中式仅损失0.3 dB但大幅降低通信开销。

## 🎯 结论与影响

RT-Tango证明了在超低延迟和低功耗下实现竞争性双耳语音增强的可行性，为助听器实时处理提供了高效方案。其分布式架构和轻量化设计对可穿戴设备部署有重要参考价值。

## ⚠️ 局限与未解决问题

仅在模拟双耳数据上评估，未在真实助听器硬件上测试；未报告噪声类型和混响条件下的性能；与更先进的轻量模型（如CRN）对比不足；未提供功耗实测数据。

---

<div class="paper-footer"><span>评分：8.8</span><span>原始：7.8</span><span>+1 重点领域加权</span><a href="/audio-paper-daily/posts/2026-07-03/">← 返回 2026-07-03 速递</a></div>
