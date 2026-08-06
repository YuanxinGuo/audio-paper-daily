---
title: "HyPASE: Hyperbolic Geometry for Parameter-Efficient Speech Emotion Fine-Tuning Framework for Large Audio-Language Models"
date: 2026-08-06T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#语音情感识别"]
summary: "提出HyPASE，利用双曲几何进行参数高效微调，提升大音频语言模型在语音情感识别上的性能。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#语音情感识别</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#参数高效微调</span> <span class="tag-pill tag-pill-soft">#双曲几何</span> <span class="tag-pill tag-pill-soft">#大音频语言模型</span> <span class="tag-pill tag-pill-soft">#语音情感识别</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2608.04351</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-08-06</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2608.04351" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2608.04351" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出HyPASE，利用双曲几何进行参数高效微调，提升大音频语言模型在语音情感识别上的性能。
</div>

## 👥 作者与机构

**Tian Jin** ¹ · Ruikang Zhang · Zefeng Zhao · Ding Luo · Jin Zeng

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合研究语音情感识别、参数高效微调及多模态大模型的读者。建议重点阅读第3节（方法）和第4节（实验），特别是HGA和EMCA模块的设计及消融实验。可先看摘要和结论，再深入方法部分。

## 🌍 研究背景

大音频语言模型（LALMs）在通用语音理解上表现优异，但针对细粒度任务如语音情感识别（SER）的适配仍是瓶颈。现有参数高效微调（PEFT）方法多在欧几里得空间操作，无法捕捉情感线索的多粒度特性（从低级韵律到高级语义）。本文提出HyPASE，利用双曲几何的Poincare球模型，以双曲半径作为表征粒度的显式代理，旨在更高效地适配LALM进行SER。

## 💡 核心创新

1. 提出双曲几何PEFT框架HyPASE，用于LALM的SER
2. 设计Hyperbolic Geometric Adapter (HGA)实现层自适应权重调制
3. 提出Emotion-aware Multi-capacity Cross-modal Aggregator (EMCA)压缩多尺度特征为音频前缀
4. 在MELD和IEMOCAP上超越欧氏PEFT基线，尤其在类别不平衡场景
5. 在受限参数预算下实现稳健的零样本跨数据集泛化

## 🏗️ 模型架构

HyPASE基于大音频语言模型（LALM），输入音频特征经预训练编码器提取后，送入双曲PEFT框架。框架包含两个核心模块：Hyperbolic Geometric Adapter (HGA) 在双曲空间进行层自适应权重调制，利用Poincare球模型的双曲半径控制表征粒度；Emotion-aware Multi-capacity Cross-modal Aggregator (EMCA) 将多尺度特征压缩为紧凑的音频前缀，注入LALM的Transformer层。输出为情感类别概率。

## 📚 数据集

- MELD（评估，多模态情感数据集）
- IEMOCAP（评估，交互式情感二元对话数据集）
- 其他标准基准（评估，用于零样本跨数据集泛化）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| Unweighted Accuracy (UA) | IEMOCAP | 欧氏PEFT基线（具体值未给出） | **显著提升（具体值未给出）** | 显著提升 |
| Weighted Accuracy (WA) | IEMOCAP | 欧氏PEFT基线（具体值未给出） | **略有下降（具体值未给出）** | 轻微下降 |

在MELD上，HyPASE在所有指标上均优于欧氏PEFT基线；在IEMOCAP上，取得了显著的UA提升，尤其在类别不平衡的情感识别中，但伴随轻微的WA下降，反映了双曲空间对少数类表征的几何优先。此外，HyPASE在受限参数预算下实现了稳健的零样本跨数据集泛化。

## 🎯 结论与影响

HyPASE通过将适应过程置于双曲几何中，为LALM微调提供了一条高效路径，显著提升了语音情感识别性能，尤其在处理类别不平衡时。该工作为利用几何先验改进PEFT方法提供了新思路，有望推动情感计算和语音交互系统的落地。

## ⚠️ 局限与未解决问题

摘要未提供具体数值，缺乏与更多基线的对比；未讨论推理延迟和计算开销；双曲空间带来的WA轻微下降可能在某些应用场景中不可接受；未提及消融实验细节。

---

<div class="paper-footer"><span>评分：7.8</span><span>原始：7.8</span><a href="/audio-paper-daily/posts/2026-08-06/">← 返回 2026-08-06 速递</a></div>
