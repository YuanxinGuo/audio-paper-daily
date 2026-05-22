---
title: "Quantizing Whisper-small: How design choices affect ASR performance"
date: 2026-05-22T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#语音识别"]
summary: "系统评估了Whisper-small后训练量化的设计选择，发现动态int8量化在57%压缩下提升WER。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero">
<div class="hero-score">
<div class="score-num">7.2</div>
<div class="score-stars">★★★★☆</div>
<div class="score-tier">前25%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#语音识别</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#模型压缩</span> <span class="tag-pill tag-pill-soft">#量化</span> <span class="tag-pill tag-pill-soft">#Whisper</span> <span class="tag-pill tag-pill-soft">#边缘部署</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2511.08093</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-05-22</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2511.08093" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2511.08093" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>系统评估了Whisper-small后训练量化的设计选择，发现动态int8量化在57%压缩下提升WER。
</div>

## 👥 作者与机构

Arthur S\"ohler · Julian Irigoyen · Andreas S{\o}eborg Kirkedal

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合从事ASR模型压缩和边缘部署的研究者。建议重点阅读§3实验设置和§4结果分析，特别是表1和表2。可跳过§2背景。

## 🌍 研究背景

Whisper-small等大型语音识别模型在边缘设备上部署困难，后训练量化（PTQ）是一种无需重新训练的压缩方法。然而，现有研究缺乏对量化方案、方法、粒度和位宽等设计选择的统一比较。本文旨在通过跨库评估，厘清这些因素对ASR性能的影响。

## 💡 核心创新

1. 跨库统一评估框架
2. 解耦量化方案、方法、粒度和位宽的影响
3. 发现动态int8量化优于静态量化
4. 揭示Transformer架构对静态量化的不利影响

## 🏗️ 模型架构

以Whisper-small为基线模型，应用后训练量化。输入为80通道log-Mel特征，经2层CNN和12层Transformer编码器，再经2层Transformer解码器输出文本。量化作用于模型权重和激活，支持动态/静态、逐层/逐通道、int8/int4/nf4/int3等配置。

## 📚 数据集

- LibriSpeech test-clean（评估）
- LibriSpeech test-other（评估）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| WER | LibriSpeech test-clean | Whisper-small (FP16) 3.4 | **Quanto动态int8 3.3** | -0.1 |
| WER | LibriSpeech test-other | Whisper-small (FP16) 7.5 | **Quanto动态int8 7.4** | -0.1 |
| 模型大小 | - | Whisper-small (FP16) 242 MB | **Quanto动态int8 104 MB** | -57% |

动态int8量化（Quanto）在test-clean和test-other上均略优于FP16基线，同时模型大小减少57%。静态量化性能下降，归因于Transformer架构。更激进的nf4和int3格式在噪声条件下精度损失明显，但压缩率达71%。

## 🎯 结论与影响

精心选择的后训练量化方法可以在不重新训练的情况下显著减小模型大小和推理成本，动态int8量化是Whisper-small的最佳折衷。该研究为边缘设备上部署大型ASR模型提供了实用指导，并强调了量化设计选择的重要性。

## ⚠️ 局限与未解决问题

仅评估了Whisper-small，未扩展到更大模型；未报告推理延迟或吞吐量；仅使用LibriSpeech，未考虑其他噪声或领域；未进行硬件部署测试。

---

<div class="paper-footer"><span>评分：7.2</span><span>原始：7.2</span><a href="/audio-paper-daily/posts/2026-05-22/">← 返回 2026-05-22 速递</a></div>
