---
title: "Acoustic Cue Alignment in Audio Language Models for Speech Emotion Recognition"
date: 2026-06-08T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#语音情感识别"]
summary: "通过在音频语言模型中插入可解释的声学概念token，研究模型是否真正利用这些线索进行语音情感识别。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero">
<div class="hero-score">
<div class="score-num">7.2</div>
<div class="score-stars">★★★★☆</div>
<div class="score-tier">前50%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#语音情感识别</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#音频语言模型</span> <span class="tag-pill tag-pill-soft">#可解释性</span> <span class="tag-pill tag-pill-soft">#声学线索</span> <span class="tag-pill tag-pill-soft">#情感计算</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2606.07309</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-06-08</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2606.07309" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2606.07309" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>通过在音频语言模型中插入可解释的声学概念token，研究模型是否真正利用这些线索进行语音情感识别。
</div>

## 👥 作者与机构

**Iosif Tsangko** ¹ · Andreas Triantafyllopoulos · Bj\"orn W. Schuller

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合对音频语言模型可解释性、语音情感识别感兴趣的研究者。建议重点阅读§3（token设计）和§4（实验结果），特别是表1和表2的扰动分析。

## 🌍 研究背景

语音情感识别（SER）中，音频语言模型（ALM）可结合显式声学线索，但尚不清楚当原始音频已存在时，模型是否真正基于这些线索进行推理。现有工作多关注提示工程，缺乏对模型内部利用声学信息的理解。本文通过设计可解释的声学概念token，研究ALM对声学线索的依赖程度。

## 💡 核心创新

1. 从eGeMAPS特征集提取6个可解释声学概念token
2. 提出token对齐/打乱/冲突/损坏的扰动实验范式
3. 揭示模型对符号线索敏感但仍部分依赖音频信号
4. 提供了一种轻量级可解释性探针方法

## 🏗️ 模型架构

输入：原始音频+文本提示（含声学概念token）。音频编码器（如Whisper）提取特征，与文本token拼接后送入语言模型解码。声学概念token由eGeMAPS特征离散化得到，包括能量、音高、动态、亮度、共振峰和音质。输出为情感类别。

## 📚 数据集

- FAU-Aibo（训练/评估，儿童情感语音）
- IEMOCAP（训练/评估，演员表演情感语音）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| UAR | FAU-Aibo | 无token 62.3% | **对齐token 63.8%** | +1.5% |
| UAR | IEMOCAP | 无token 68.1% | **对齐token 69.4%** | +1.3% |

对齐token在FAU-Aibo和IEMOCAP上分别提升UAR 1.5%和1.3%。打乱、冲突或损坏token导致性能下降，但未完全崩溃，表明模型仍依赖音频信号。消融实验显示各token贡献不同，能量和音高token影响最大。

## 🎯 结论与影响

本文证明在ALM中插入可解释声学token可提升SER性能，且模型对符号线索敏感但非完全依赖。该工作为理解ALM的声学基础提供了新视角，并提示未来可设计更细粒度的token干预方法。对工业应用而言，该方法可增强模型可解释性和鲁棒性。

## ⚠️ 局限与未解决问题

仅使用6个eGeMAPS特征，可能遗漏其他重要声学线索；实验仅在两个数据集上进行，泛化性未知；未与端到端微调方法对比；token离散化方式可能损失信息；未报告推理延迟或计算开销。

---

<div class="paper-footer"><span>评分：7.2</span><span>原始：7.2</span><a href="/audio-paper-daily/posts/2026-06-08/">← 返回 2026-06-08 速递</a></div>
