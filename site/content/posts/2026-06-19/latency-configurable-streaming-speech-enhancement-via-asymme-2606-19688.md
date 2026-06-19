---
title: "Latency-Configurable Streaming Speech Enhancement via Asymmetric Temporal Padding"
date: 2026-06-19T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#语音增强"]
summary: "提出一种通过非对称时间填充和双缓冲流式机制实现可配置延迟的语音增强方法，在极低延迟下达到或超越先前因果SOTA。"
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
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#流式处理</span> <span class="tag-pill tag-pill-soft">#低延迟</span> <span class="tag-pill tag-pill-soft">#卷积网络</span> <span class="tag-pill tag-pill-soft">#语音增强</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2606.19688</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-06-19</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
<div class="meta-row"><span class="meta-key">⭐</span><span class="meta-val focus-badge">本站重点关注领域 · 评分 +1</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2606.19688" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2606.19688" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出一种通过非对称时间填充和双缓冲流式机制实现可配置延迟的语音增强方法，在极低延迟下达到或超越先前因果SOTA。
</div>

## 👥 作者与机构

**Yunsik Kim** ¹ · Yoonyoung Chung

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合从事流式语音增强或低延迟音频处理的研究者。建议重点阅读§3.2（非对称时间填充）和§3.3（双缓冲流式），以及表1的延迟-质量权衡结果。可复现其延迟配置机制。

## 🌍 研究背景

流式语音增强需要在算法延迟与增强质量之间权衡。现有方法大多将延迟视为二元选择（因果或非因果），缺乏细粒度配置能力。先前因果SOTA（如46.5ms延迟下PESQ 3.27）难以适应不同应用场景的延迟需求。本文旨在提出一种可配置延迟的流式增强框架，允许用户通过单一超参数在训练时设定延迟，并在推理时获得对应模型。

## 💡 核心创新

1. 非对称时间填充：在卷积层中独立分配过去和未来上下文，实现延迟可配置
2. 双缓冲流式机制：结合状态缓冲和前瞻缓冲，在输入和特征层面提供未来上下文
3. 选择性状态更新：防止未来帧泄漏到流式状态，保证训练-推理一致性

## 🏗️ 模型架构

输入为含噪语音波形，经短时傅里叶变换得到幅度谱。主干网络为1.37M参数的卷积网络（具体结构未详述，但基于卷积层）。关键模块：1）非对称时间填充层，通过训练时设定的超参数控制卷积前后填充的帧数，从而配置延迟；2）双缓冲流式模块，包含状态缓冲（存储过去帧的中间状态）和前瞻缓冲（存储未来帧的输入和特征），在推理时按帧处理。输出为增强后的幅度谱，经逆STFT得到时域波形。

## 📚 数据集

- VoiceBank+DEMAND（训练和评估，包含干净语音和多种噪声）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| PESQ | VoiceBank+DEMAND | 先前因果SOTA（46.5ms延迟）3.27 | **12.5ms延迟下3.35** | +0.08 |
| PESQ | VoiceBank+DEMAND | 本文12.5ms延迟3.35 | **75.0ms延迟下3.43** | +0.08 |

在VoiceBank+DEMAND上，固定1.37M参数量的骨干网络，通过配置延迟从12.5ms到75.0ms，PESQ从3.35提升至3.43。在12.5ms全因果延迟下，PESQ 3.35超过了先前因果SOTA（46.5ms延迟下3.27），表明该方法在极低延迟下仍能保持高质量。未提供其他指标（如SI-SDR）或跨数据集泛化实验。

## 🎯 结论与影响

本文提出的LaCo-SENet通过非对称时间填充和双缓冲流式机制，首次实现了流式语音增强中延迟的细粒度可配置，且不牺牲质量。在12.5ms延迟下达到PESQ 3.35，优于先前因果SOTA。该方法为延迟敏感的应用（如助听器、实时通信）提供了灵活的选择，有望推动流式增强的实用化。

## ⚠️ 局限与未解决问题

仅在VoiceBank+DEMAND单一数据集上评估，缺乏跨噪声类型和混响场景的泛化验证。未报告SI-SDR、STOI等常用指标，对比基线仅一个因果SOTA，对比不充分。未提供推理速度或计算复杂度分析。未开源代码，可复现性存疑。

---

<div class="paper-footer"><span>评分：8.8</span><span>原始：7.8</span><span>+1 重点领域加权</span><a href="/audio-paper-daily/posts/2026-06-19/">← 返回 2026-06-19 速递</a></div>
