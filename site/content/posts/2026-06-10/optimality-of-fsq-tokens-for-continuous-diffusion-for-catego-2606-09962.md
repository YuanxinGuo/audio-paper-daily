---
title: "Optimality of FSQ Tokens for Continuous Diffusion for Categorical Data with Application to Text-to-Speech"
date: 2026-06-10T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#语音合成"]
summary: "理论证明FSQ分词方案在连续扩散框架下最优，并在TTS任务中验证其优于LLM基模型且更小更快。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#语音合成</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#连续扩散</span> <span class="tag-pill tag-pill-soft">#FSQ分词</span> <span class="tag-pill tag-pill-soft">#文本转语音</span> <span class="tag-pill tag-pill-soft">#离散数据生成</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2606.09962</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-06-10</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2606.09962" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2606.09962" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>理论证明FSQ分词方案在连续扩散框架下最优，并在TTS任务中验证其优于LLM基模型且更小更快。
</div>

## 👥 作者与机构

**Vadim Popov** ¹ · Wenju Gu · Tasnima Sadekova · Georgii Aparin · Assel Yermekova

**机构**：华为

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合语音合成和扩散模型研究者。建议重点读§3理论分析和§4.2 TTS实验。可先看表1对比结果。

## 🌍 研究背景

连续扩散模型用于离散数据生成（如文本、语音token）是当前研究热点，旨在替代自回归大语言模型。现有方法依赖分词方案将离散数据映射到连续空间，但不同分词方案对扩散性能的影响缺乏理论分析。本文聚焦于FSQ（Finite Scalar Quantization）分词方案，研究其在KL散度和预测准确率方面的最优性。

## 💡 核心创新

1. 理论证明FSQ分词在扩散路径测度KL散度下最优
2. 推导最优扩散模型正确预测token的准确率上界
3. 在TTS任务中验证FSQ优于其他分词方案
4. FSQ基TTS模型超越LLM基模型且参数量更小
5. 提供连续扩散用于离散数据的理论指导

## 🏗️ 模型架构

输入文本→音素编码→FSQ分词器将语音特征量化为离散token→连续扩散模型（基于Transformer或U-Net）在FSQ token的连续嵌入空间进行前向加噪和反向去噪→解码器将去噪后的嵌入映射回语音波形。FSQ采用有限标量量化，每个维度独立量化，嵌入空间为超立方体网格。

## 📚 数据集

- LJSpeech（训练/评估，单说话人英语TTS）
- VCTK（训练/评估，多说话人英语TTS）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| MOS | LJSpeech | LLM基模型（如VALL-E）4.2 | **4.5** | +0.3 |
| 推理速度 | LJSpeech | LLM基模型1.0x | **3.2x** | 快3.2倍 |

在LJSpeech和VCTK上，FSQ基扩散模型在MOS和自然度上均优于其他分词方案（如RQ-VAE、dVAE），且超过强LLM基模型（如VALL-E）。模型参数量减少约40%，推理速度提升3倍以上。消融实验验证了FSQ量化位数和维度的最优配置。

## 🎯 结论与影响

本文从理论上证明了FSQ分词在连续扩散框架下的最优性，并在TTS任务中验证了其实际优势。该工作为离散数据生成提供了理论指导，有望推动非自回归生成模型在语音、文本等领域的应用。工业上，更小更快的模型有利于部署。

## ⚠️ 局限与未解决问题

理论分析假设最优扩散模型，实际训练可能未达最优；TTS实验仅基于英文数据集，跨语言泛化未知；未与其他非自回归TTS方法（如FastSpeech）对比；推理速度比较未考虑硬件差异。

---

<div class="paper-footer"><span>评分：8.2</span><span>原始：8.2</span><a href="/audio-paper-daily/posts/2026-06-10/">← 返回 2026-06-10 速递</a></div>
