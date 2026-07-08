---
title: "Flow Matching-Based Speech Source Separation with Best-of-N Biometric Sampling"
date: 2026-07-08T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#语音分离"]
summary: "提出基于条件流匹配的语音分离方法，利用说话人编码器排序源并实现最佳N采样和块级对齐，在Libri2Mix上达到有竞争力的分离质量和最低的下游ASR/SV错误率。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#语音分离</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#流匹配</span> <span class="tag-pill tag-pill-soft">#说话人编码</span> <span class="tag-pill tag-pill-soft">#最佳N采样</span> <span class="tag-pill tag-pill-soft">#语音分离</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2607.06088</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-07-08</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
<div class="meta-row"><span class="meta-key">⭐</span><span class="meta-val focus-badge">本站重点关注领域 · 评分 +1</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2607.06088" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2607.06088" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出基于条件流匹配的语音分离方法，利用说话人编码器排序源并实现最佳N采样和块级对齐，在Libri2Mix上达到有竞争力的分离质量和最低的下游ASR/SV错误率。
</div>

## 👥 作者与机构

**Anastasia Zorkina** ¹ · Alexandr Anikin · Nikita Khmelev · Anastasiya Korenevskaya · Sergey Novoselov · Vladimir Volokhov · Maxim Korenevsky · Yuriy Matveev

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合语音分离和生成模型研究者。建议重点阅读§3的流匹配框架和§4的最佳N采样策略，以及表2的cpWER和EER结果。可先看§3.2与表2。

## 🌍 研究背景

单通道语音分离面临源排列模糊、生成模型采样变异性和长录音分块推理困难。现有方法如SepFormer、DPRNN在分离指标上表现良好，但下游ASR和说话人验证错误率仍有提升空间。本文旨在通过条件流匹配生成有序输出，结合说话人编码器解决排列问题，并通过最佳N采样减少采样噪声。

## 💡 核心创新

1. 条件流匹配生成有序双源输出
2. 冻结说话人编码器定义源顺序并用于推理
3. 最佳N采样候选选择与块级通道对齐
4. Transformer U-Net变体作为骨干网络

## 🏗️ 模型架构

输入混合语音频谱→Transformer U-Net变体作为条件流匹配模型，输出两个有序源的频谱。训练时，冻结的说话人编码器根据源与参考嵌入的相似度定义顺序。推理时，对每个源生成N个候选，选择与说话人嵌入最匹配的候选，并对长录音分块进行通道对齐。

## 📚 数据集

- Libri2Mix（训练/评估，包含train-360和test集）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| SI-SDR (dB) | Libri2Mix test | SepFormer 17.5 | **17.8** | +0.3 dB |
| PESQ | Libri2Mix test | SepFormer 3.42 | **3.45** | +0.03 |
| cpWER (%) | Libri2Mix test (ASR) | SepFormer 12.1 | **10.5** | -1.6% |
| EER (%) | Libri2Mix test (SV) | SepFormer 3.8 | **3.2** | -0.6% |

在Libri2Mix上，所提方法在SI-SDR和PESQ上与SepFormer相当，但在下游ASR的cpWER和说话人验证的EER上显著优于所有基线，包括SepFormer和DPRNN。最佳N采样（N=5）有效降低了生成模型的采样变异。消融实验验证了说话人编码器排序和最佳N采样的贡献。

## 🎯 结论与影响

本文提出的条件流匹配语音分离方法通过说话人编码器排序和最佳N采样，在保持分离质量的同时显著提升了下游ASR和SV性能。该方法为生成模型在语音分离中的应用提供了新思路，有望推动实际部署中分离与下游任务的联合优化。

## ⚠️ 局限与未解决问题

未报告模型参数量和推理延迟；仅在Libri2Mix上评估，未见跨数据集泛化；最佳N采样增加了推理计算量；未与最新扩散模型方法（如DiffSep）对比。

---

<div class="paper-footer"><span>评分：8.8</span><span>原始：7.8</span><span>+1 重点领域加权</span><a href="/audio-paper-daily/posts/2026-07-08/">← 返回 2026-07-08 速递</a></div>
