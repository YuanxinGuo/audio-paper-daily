---
title: "Scaling to Multimodal and Multichannel Heart Sound Classification with Synthetic and Augmented Biosignals"
date: 2026-07-03T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#生物声学"]
summary: "利用扩散模型生成合成心音数据增强训练集，微调Wav2Vec2实现多模态多通道心音分类，在CinC2016等数据集上达到SOTA。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#生物声学</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#心音分类</span> <span class="tag-pill tag-pill-soft">#数据增强</span> <span class="tag-pill tag-pill-soft">#扩散模型</span> <span class="tag-pill tag-pill-soft">#Wav2Vec2</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2509.11606</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-07-03</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2509.11606" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2509.11606" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>利用扩散模型生成合成心音数据增强训练集，微调Wav2Vec2实现多模态多通道心音分类，在CinC2016等数据集上达到SOTA。
</div>

## 👥 作者与机构

**Milan Marocchi** ¹ · Matthew Fynn · Kayapanda Mandana · Yue Rong

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合生物医学信号处理或音频分类研究者。可重点读§3数据增强方法和§4实验结果，特别是表1-3。若对扩散模型生成生物信号感兴趣，可通读全文。

## 🌍 研究背景

心血管疾病是全球主要死因，早期筛查需求迫切。深度学习已用于心音分类，但同步多模态（PCG+ECG）和多通道PCG数据集稀缺，限制了Transformer等先进架构的应用。现有方法多依赖单通道PCG，且数据量不足。本文旨在通过数据增强解决数据稀缺问题，提升分类性能。

## 💡 核心创新

1. 使用WaveGrad和DiffWave扩散模型生成合成PCG/ECG信号
2. 结合传统信号处理与扩散模型进行数据增强
3. 微调Wav2Vec2用于多模态和多通道心音分类
4. 在三个不同数据集上验证有效性

## 🏗️ 模型架构

输入为PCG/ECG波形信号，经特征提取后送入预训练的Wav2Vec2模型（基于Transformer），通过微调进行二分类（正常/异常）。数据增强阶段使用WaveGrad或DiffWave扩散模型生成合成信号，并与原始信号混合扩充训练集。模型参数量未明确给出。

## 📚 数据集

- CinC 2016（单通道PCG，训练/评估，约3000样本）
- CinC training-a（同步PCG+ECG，训练/评估）
- 可穿戴背心数据集（多通道PCG，训练/评估）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| Accuracy | CinC 2016 | 未明确给出 | **92.48%** | SOTA |
| UAR | CinC 2016 | 未明确给出 | **93.05%** | SOTA |
| Accuracy | CinC training-a (PCG+ECG) | 未明确给出 | **93.14%** | SOTA |
| Accuracy | 可穿戴背心 (mPCG) | 未明确给出 | **77.13%** | SOTA |

在CinC 2016单通道PCG上，准确率92.48%，UAR 93.05%；在同步PCG+ECG上准确率93.14%；在多通道PCG上准确率77.13%。所有指标均达到SOTA，但未与现有方法进行直接数值对比。消融实验显示扩散模型增强优于传统方法。

## 🎯 结论与影响

本文证明扩散模型生成合成生物信号可有效增强训练数据，使Wav2Vec2在有限数据下达到SOTA。该方法有望推动多模态心音分类的临床应用，并为其他生物声学任务提供数据增强范式。

## ⚠️ 局限与未解决问题

未与现有方法（如CNN、LSTM）进行公平对比，缺乏推理延迟和模型复杂度分析。多通道数据集性能较低（77%），可能因数据量不足或通道间相关性未充分利用。未开源代码和模型。

---

<div class="paper-footer"><span>评分：7.2</span><span>原始：7.2</span><a href="/audio-paper-daily/posts/2026-07-03/">← 返回 2026-07-03 速递</a></div>
