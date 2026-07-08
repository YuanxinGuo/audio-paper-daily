---
title: "Perceptually Aligning Representations of Music via Noise-Augmented Autoencoders"
date: 2026-07-08T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#音频表征学习"]
summary: "通过噪声增强自编码器结合感知损失，使音频表征按感知层次结构化，在音高惊讶估计和EEG预测上超越先前方法。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#音频表征学习</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#自编码器</span> <span class="tag-pill tag-pill-soft">#感知层次</span> <span class="tag-pill tag-pill-soft">#噪声增强</span> <span class="tag-pill tag-pill-soft">#音乐</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2511.05350</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-07-08</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner"><div class="oc-headline"><span class="oc-pulse"></span><span class="oc-title">本论文已开源</span><span class="oc-hint">点击下方卡片直达对应资源</span></div><div class="oc-grid"><a class="oc-chip oc-chip-code" href="https://github.com/CPJKU/pa-audioic" target="_blank" rel="noopener"><span class="oc-icon">💻</span><span class="oc-text"><span class="oc-label">代码仓库</span><span class="oc-sub">CPJKU/pa-audioic</span></span></a></div></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2511.05350" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2511.05350" target="_blank" rel="noopener">📑 PDF</a><a class="rsrc rsrc-code" href="https://github.com/CPJKU/pa-audioic" target="_blank" rel="noopener">💻 代码</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>通过噪声增强自编码器结合感知损失，使音频表征按感知层次结构化，在音高惊讶估计和EEG预测上超越先前方法。
</div>

## 👥 作者与机构

**Mathias Rose Bjare** ¹ · Giorgia Cantisani · Marco Pasini · Stefan Lattner · Gerhard Widmer

**机构**：约翰内斯·开普勒大学林茨分校

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合音频表征学习、感知建模方向的研究者。建议重点阅读§3方法部分和§4实验，尤其是表1和表2的结果。可先看§3.2噪声增强机制。

## 🌍 研究背景

自编码器常用于学习音频表征，但传统训练方式未显式对齐感知层次。先前方法如VQ-VAE、SoundStream等关注重建质量，但表征结构缺乏感知可解释性。本文旨在通过噪声增强输入编码和感知损失，使表征按感知显著性分层，并验证其在音高惊讶估计和EEG预测中的有效性。

## 💡 核心创新

1. 噪声增强编码重建：对编码加噪后解码，迫使粗粒度结构捕获感知显著信息
2. 感知损失结合：引入音高、响度等感知相关损失引导层次形成
3. 跨模态验证：在音高惊讶估计和EEG预测任务上验证表征的感知对齐性

## 🏗️ 模型架构

输入音频经编码器（如卷积网络）得到潜在编码，对该编码施加噪声（如高斯噪声），再由解码器重建音频。训练时结合重建损失（如L1或STFT损失）和感知损失（如音高损失、响度损失）。编码器输出多尺度特征，噪声强度控制不同尺度，使粗尺度编码捕获更感知显著的信息。

## 📚 数据集

- MAESTRO（训练/评估，钢琴音乐）
- NSynth（评估，乐器音色）
- EEG数据集（评估，音乐聆听脑电）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| 音高惊讶估计准确率 | MAESTRO | 先前方法（如CREPE-based） | **优于基线** | 具体数值未给出 |
| EEG预测相关性 | EEG数据集 | 先前方法 | **优于基线** | 具体数值未给出 |

实验表明，噪声增强自编码器产生的表征在粗尺度上编码了更多感知显著信息（如音高），在音高惊讶估计任务上优于基于CREPE的方法，在EEG响应预测上也超越先前模型。消融研究验证了噪声增强和感知损失的必要性。

## 🎯 结论与影响

本文证明噪声增强自编码器结合感知损失能产生按感知层次结构化的音频表征，在音高惊讶估计和EEG预测中取得更优结果。该工作为感知对齐表征学习提供了新范式，有望推动音乐信息检索和神经音频处理领域发展。

## ⚠️ 局限与未解决问题

实验仅在音乐数据上验证，未涉及语音或通用音频；感知损失的设计依赖特定先验（如音高），泛化性待考；未报告模型参数量和推理速度；与现有自编码器（如VQ-VAE）的直接对比缺失。

## 🔗 开源资源

- **代码**：<https://github.com/CPJKU/pa-audioic>

---

<div class="paper-footer"><span>评分：7.8</span><span>原始：7.8</span><a href="/audio-paper-daily/posts/2026-07-08/">← 返回 2026-07-08 速递</a></div>
