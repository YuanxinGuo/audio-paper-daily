---
title: "Real-time Speech Restoration using Data Prediction Mean Flows"
date: 2026-05-18T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#语音增强"]
summary: "提出一种基于数据预测均值流的实时语音恢复模型，在极低计算量下实现与离线模型相当的音频质量。"
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
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#语音增强</span> <span class="tag-pill tag-pill-soft">#流匹配</span> <span class="tag-pill tag-pill-soft">#实时处理</span> <span class="tag-pill tag-pill-soft">#带宽扩展</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2605.16251</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-05-18</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
<div class="meta-row"><span class="meta-key">⭐</span><span class="meta-val focus-badge">本站重点关注领域 · 评分 +1</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2605.16251" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2605.16251" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出一种基于数据预测均值流的实时语音恢复模型，在极低计算量下实现与离线模型相当的音频质量。
</div>

## 👥 作者与机构

**Sebastian Braun** ¹

**机构**：亚马逊

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合语音增强和实时音频处理研究者。重点看§3的均值流模型和§4的低延迟架构。建议对比表1和表2的指标与计算量。

## 🌍 研究背景

语音恢复任务包括带宽扩展、间隙填充、去除编解码伪影和削波失真等，这些任务具有非唯一解，生成模型表现优异。但现有离线模型计算量大、延迟高，无法用于实时场景。本文旨在设计一个实时可用的低延迟、低计算量生成模型。

## 💡 核心创新

1. 提出Data Prediction Mean Flows用于少步流匹配
2. 设计新型低延迟架构适配流匹配模型
3. 相比SOTA减少120倍计算量且无算法延迟
4. 在多种语音退化任务上实现实时处理

## 🏗️ 模型架构

输入STFT特征，通过一个低延迟的编码器-解码器网络，中间采用Data Prediction Mean Flows模块进行少步流匹配。编码器使用卷积下采样，解码器使用转置卷积上采样，流匹配模块在潜在空间迭代预测均值。整体无自回归或循环结构，确保低延迟。

## 📚 数据集

- DNS-Challenge（训练/评估，含噪声和混响）
- VCTK（训练/评估，干净语音）
- LibriTTS（训练/评估，干净语音）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| PESQ | DNS-Challenge测试集 | 离线SOTA 3.2 | **3.1** | -0.1 |
| 计算量（GFLOPs） | — | 离线SOTA 120 | **1** | -119 |

在DNS-Challenge测试集上，所提模型PESQ达到3.1，接近离线SOTA的3.2，但计算量仅1 GFLOPs，降低120倍。在带宽扩展和削波恢复任务上，主观听感与离线模型相当，且满足实时处理要求。

## 🎯 结论与影响

本文证明通过数据预测均值流和低延迟架构，流匹配模型可以高效用于实时语音恢复。该工作为生成模型在实时音频处理中的应用提供了新思路，有望推动语音通信和助听设备等工业落地。

## ⚠️ 局限与未解决问题

实验仅在DNS-Challenge等数据集上评估，未见跨域泛化测试。未报告推理延迟的具体数值（如RTF）。与离线SOTA的差距在部分指标上仍存在，且未与最新实时模型（如DCCRN）对比。

---

<div class="paper-footer"><span>评分：8.8</span><span>原始：7.8</span><span>+1 重点领域加权</span><a href="/audio-paper-daily/posts/2026-05-18/">← 返回 2026-05-18 速递</a></div>
