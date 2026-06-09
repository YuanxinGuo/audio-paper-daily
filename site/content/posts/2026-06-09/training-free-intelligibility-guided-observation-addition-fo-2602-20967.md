---
title: "Training-Free Intelligibility-Guided Observation Addition for Noisy ASR"
date: 2026-06-09T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#语音增强"]
summary: "提出一种无需训练的智能引导观测融合方法，利用后端ASR的清晰度估计动态融合带噪与增强语音，提升噪声环境下的ASR性能。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero hero-focus">
<div class="hero-score">
<div class="score-num">8.2</div>
<div class="score-stars">★★★★☆</div>
<div class="score-tier">前50%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#语音增强</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#语音识别</span> <span class="tag-pill tag-pill-soft">#训练无关</span> <span class="tag-pill tag-pill-soft">#智能融合</span> <span class="tag-pill tag-pill-soft">#鲁棒性</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2602.20967</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-06-09</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
<div class="meta-row"><span class="meta-key">⭐</span><span class="meta-val focus-badge">本站重点关注领域 · 评分 +1</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2602.20967" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2602.20967" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出一种无需训练的智能引导观测融合方法，利用后端ASR的清晰度估计动态融合带噪与增强语音，提升噪声环境下的ASR性能。
</div>

## 👥 作者与机构

**Haoyang Li** ¹ · Changsong Liu · Wei Rao · Hao Shi · Sakriani Sakti · Eng Siong Chng

**机构**：南洋理工大学 · 阿里巴巴达摩院

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合从事语音前端增强与ASR联合优化的研究者阅读。建议重点读§3的方法部分和§4的实验结果，特别是表1-3的对比。可先看§3.2的融合权重推导。

## 🌍 研究背景

噪声环境下ASR性能严重下降。语音增强前端虽能抑制噪声，但常引入损伤识别的伪影。观测融合（OA）通过融合带噪与增强语音来缓解此问题。现有OA方法依赖训练好的神经网络预测融合权重，复杂度高且泛化性有限。本文提出利用后端ASR的清晰度估计直接指导融合权重，无需额外训练。

## 💡 核心创新

1. 利用后端ASR的清晰度估计作为融合权重
2. 完全无需训练的OA方法
3. 支持帧级与话语级融合策略
4. 在多种SE-ASR组合上验证鲁棒性

## 🏗️ 模型架构

输入为带噪语音和经SE增强的语音。首先通过后端ASR模型（如预训练模型）对两者分别计算清晰度估计（如置信度或似然）。然后根据清晰度估计动态计算融合权重，对带噪和增强语音进行加权融合。融合后的语音送入ASR解码。权重计算无需额外训练，可基于帧级或话语级清晰度。

## 📚 数据集

- LibriSpeech（训练ASR模型）
- CHiME-3（评估噪声环境）
- DNS-Challenge（评估噪声环境）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| WER | CHiME-3 | Noisy 15.2% | **12.8%** | -2.4% |
| WER | DNS-Challenge | Noisy 18.7% | **15.1%** | -3.6% |

在CHiME-3和DNS-Challenge上，所提方法相比直接使用带噪或增强语音均显著降低WER，且优于现有基于神经网络的OA方法。帧级融合优于话语级融合。在不同SE模型（如DCCRN、Conv-TasNet）和ASR后端（如Conformer）组合下均表现一致。

## 🎯 结论与影响

本文提出的无需训练的清晰度引导OA方法，通过动态融合带噪与增强语音，有效提升噪声ASR鲁棒性，且不依赖特定SE或ASR模型。该方法为前端增强与后端ASR的联合优化提供了轻量级方案，有望在工业场景中快速部署。

## ⚠️ 局限与未解决问题

方法依赖后端ASR输出的清晰度估计质量，若ASR本身在噪声下不可靠，融合权重可能不准确。实验仅在特定噪声数据集上评估，未见跨域泛化分析。未报告计算开销对比。

---

<div class="paper-footer"><span>评分：8.2</span><span>原始：7.2</span><span>+1 重点领域加权</span><a href="/audio-paper-daily/posts/2026-06-09/">← 返回 2026-06-09 速递</a></div>
