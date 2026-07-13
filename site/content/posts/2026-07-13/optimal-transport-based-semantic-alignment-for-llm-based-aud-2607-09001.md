---
title: "Optimal Transport-based Semantic Alignment for LLM-based Audio-Visual Speech Recognition"
date: 2026-07-13T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#语音识别"]
summary: "提出基于最优传输的语义对齐框架，通过将音视频表示对齐到LLM语言空间，提升LLM-AVSR在噪声下的鲁棒性。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero">
<div class="hero-score">
<div class="score-num">8.2</div>
<div class="score-stars">★★★★☆</div>
<div class="score-tier">前25%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#语音识别</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#多模态融合</span> <span class="tag-pill tag-pill-soft">#最优传输</span> <span class="tag-pill tag-pill-soft">#对比学习</span> <span class="tag-pill tag-pill-soft">#大语言模型</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2607.09001</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-07-13</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2607.09001" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2607.09001" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出基于最优传输的语义对齐框架，通过将音视频表示对齐到LLM语言空间，提升LLM-AVSR在噪声下的鲁棒性。
</div>

## 👥 作者与机构

**Xugang Lu** ¹ · Peng Shen · Yu Tsao · Hisashi Kawai

**机构**：日本国立信息学研究所 · 中央研究院

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合从事多模态语音识别、鲁棒ASR的研究者。建议重点阅读§3.2最优传输对齐与§3.3对比学习部分，以及表1的消融实验。可复现其OT耦合矩阵可视化方法。

## 🌍 研究背景

LLM-AVSR通过融合音频和视觉信息在噪声环境下表现鲁棒。现有方法通常独立预训练音视频编码器，投影后作为软提示输入LLM，但未显式对齐不同模态的表示，导致跨模态融合效果受限。本文旨在通过最优传输将音视频特征对齐到LLM的语言嵌入空间，减少模态差异。

## 💡 核心创新

1. 用最优传输估计模态特征与语言嵌入的耦合矩阵
2. 将OT耦合作为软伪标签监督对比学习
3. 显式将音视频表示锚定到LLM语言空间
4. 在Whisper+AV-HuBERT+LLaMA3.2上实现SOTA

## 🏗️ 模型架构

输入：音频波形经Whisper编码器提取声学特征，视频帧经AV-HuBERT编码器提取视觉特征。主干：分别通过线性投影层映射到LLM嵌入维度。关键模块：最优传输模块计算声学/视觉特征与LLM文本嵌入之间的耦合矩阵，并作为软标签进行对比学习，对齐后的特征拼接作为软提示输入LLaMA3.2-3B解码器。输出：文本转录。

## 📚 数据集

- LRS3-TED（训练/评估，约433小时）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| WER (%) | LRS3-TED (clean) | AV-HuBERT+LLaMA 2.1 | **1.8** | -0.3 |
| WER (%) | LRS3-TED (noisy, SNR 0dB) | AV-HuBERT+LLaMA 12.5 | **9.2** | -3.3 |

在LRS3-TED上，本文方法在干净条件下WER 1.8%，噪声0dB下9.2%，均优于AV-HuBERT+LLaMA基线。消融实验表明OT对齐和对比学习均贡献显著，且在不同SNR下均有一致提升。

## 🎯 结论与影响

本文通过最优传输对齐音视频表示到LLM语言空间，显著提升了LLM-AVSR在噪声下的性能。该方法为多模态融合提供了新范式，有望推广到其他音视频理解任务。工业上可应用于嘈杂环境下的语音交互系统。

## ⚠️ 局限与未解决问题

仅使用LRS3-TED单一数据集，未在更大规模或多语种上验证；未报告推理延迟或模型参数量；对比学习依赖OT耦合作为伪标签，可能引入噪声；未与近期其他LLM-AVSR方法（如基于适配器的）对比。

---

<div class="paper-footer"><span>评分：8.2</span><span>原始：8.2</span><a href="/audio-paper-daily/posts/2026-07-13/">← 返回 2026-07-13 速递</a></div>
