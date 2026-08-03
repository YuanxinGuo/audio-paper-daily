---
title: "DoubleHelix: Structured Cross-Modal Fusion for Audio-Visual Speech Recognition with LLMs"
date: 2026-08-03T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#语音识别"]
summary: "提出DoubleHelix框架，通过迭代跨模态交互与退化感知增强，在LRS3上实现0.68% WER，相对提升5.6%。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#语音识别</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#多模态融合</span> <span class="tag-pill tag-pill-soft">#视听语音识别</span> <span class="tag-pill tag-pill-soft">#鲁棒性</span> <span class="tag-pill tag-pill-soft">#大语言模型</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2607.29112</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-08-03</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2607.29112" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2607.29112" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出DoubleHelix框架，通过迭代跨模态交互与退化感知增强，在LRS3上实现0.68% WER，相对提升5.6%。
</div>

## 👥 作者与机构

**Ziwei Cheng** ¹ · Zhenhua Tan · Zhuomin Zhu

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合AVSR和多模态融合研究者。建议重点阅读第3节（方法）和第4节（实验），特别是ReverseParallelHelix和QualitySensor的设计。可先看表1和表2了解性能提升。

## 🌍 研究背景

AVSR旨在融合音频和视觉信息提升识别鲁棒性，尤其在噪声环境下。现有方法通常将跨模态交互视为单步操作，缺乏结构化迭代细化，且未显式处理退化条件。本文提出DoubleHelix框架，将融合重构为迭代过程，并引入退化感知增强，以提升性能。

## 💡 核心创新

1. ReverseParallelHelix：多轮结构化交互，学习对齐约束
2. QualitySensor：学习退化感知门控信号
3. HelixReplication：一致性引导的条件特征增强
4. 不对称路径加权设计分析

## 🏗️ 模型架构

输入为音频和视觉特征，分别编码后送入ReverseParallelHelix模块，该模块通过多轮交互和约束学习融合特征。QualitySensor根据输入质量生成门控信号，控制融合权重。HelixReplication利用一致性约束增强特征。最后融合特征送入LLM解码器输出文本。

## 📚 数据集

- LRS3（训练和评估）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| WER | LRS3 clean | 最佳基线（匹配主干） | **0.68%** | -5.6%相对 |
| WER | LRS3 babble noise SNR -5dB | 未给出 | **11.6%** | 未给出 |

在LRS3干净音频上，DoubleHelix达到0.68% WER，相对提升5.6%。在babble噪声SNR -5dB条件下，WER为11.6%，显示鲁棒性提升。消融实验验证了各组件贡献，并分析了不对称路径加权等设计选择。

## 🎯 结论与影响

DoubleHelix通过迭代跨模态融合和退化感知增强，显著提升AVSR性能，尤其在噪声条件下。该框架为多模态融合提供了新思路，可能推动AVSR在真实场景中的应用。

## ⚠️ 局限与未解决问题

摘要未提及推理效率或参数量，可能影响实际部署。实验仅在LRS3上评估，缺乏跨数据集泛化验证。未与最新AVSR方法（如AV-HuBERT）直接对比。

---

<div class="paper-footer"><span>评分：7.8</span><span>原始：7.8</span><a href="/audio-paper-daily/posts/2026-08-03/">← 返回 2026-08-03 速递</a></div>
