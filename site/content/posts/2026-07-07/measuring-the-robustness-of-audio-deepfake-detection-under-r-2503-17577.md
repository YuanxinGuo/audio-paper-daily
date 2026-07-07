---
title: "Measuring the Robustness of Audio Deepfake Detection under Real-World Corruption"
date: 2026-07-07T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#音频深度伪造检测"]
summary: "系统评估10种音频深度伪造检测模型在18种真实世界失真下的鲁棒性，发现模型对噪声鲁棒但对音频修改和压缩脆弱，语音基础模型表现更优。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#音频深度伪造检测</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#鲁棒性评估</span> <span class="tag-pill tag-pill-soft">#语音基础模型</span> <span class="tag-pill tag-pill-soft">#数据增强</span> <span class="tag-pill tag-pill-soft">#语音增强</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2503.17577</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-07-07</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
<div class="meta-row"><span class="meta-key">⭐</span><span class="meta-val focus-badge">本站重点关注领域 · 评分 +1</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2503.17577" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2503.17577" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>系统评估10种音频深度伪造检测模型在18种真实世界失真下的鲁棒性，发现模型对噪声鲁棒但对音频修改和压缩脆弱，语音基础模型表现更优。
</div>

## 👥 作者与机构

**Xiang Li** ¹ · Pin-Yu Chen · Wenqi Wei

**机构**：IBM Research · IBM Research · IBM Research

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合音频安全、深度伪造检测领域的研究者。建议重点阅读第3节（实验设置）和第4节（关键发现），尤其是表1和表2。可参考其评估框架设计自己的鲁棒性测试。

## 🌍 研究背景

音频深度伪造检测是应对AI合成语音滥用的关键。现有检测模型多在干净数据上训练，但真实场景中音频常受噪声、修改和压缩等失真影响，导致性能下降。此前缺乏对这些失真类型系统性的鲁棒性评估。本文旨在填补这一空白，通过大规模实验揭示不同模型对各类失真的脆弱性。

## 💡 核心创新

1. 系统评估10种模型对18种失真的鲁棒性
2. 对比传统模型与语音基础模型的表现差异
3. 揭示模型规模与鲁棒性的关系
4. 提出通过数据增强和语音增强提升鲁棒性

## 🏗️ 模型架构

评估框架包括10种检测模型：传统深度学习模型（如LCNN、ResNet）和语音基础模型（如Wav2Vec2、HuBERT、Whisper）。输入为音频波形或频谱特征，经模型处理后输出二分类结果（真实/伪造）。失真类型分三类：噪声扰动（加性噪声、混响）、音频修改（重采样、时间伸缩、音高偏移）、压缩（MP3、AAC、Opus、神经编解码器）。

## 📚 数据集

- ASVspoof2019（训练/评估，包含真实和伪造语音）
- In-the-Wild（评估，真实场景伪造语音）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| EER (%) | ASVspoof2019 | LCNN (1.06) | **Wav2Vec2 (0.82)** | -0.24 |
| EER (%) | In-the-Wild | LCNN (12.34) | **Wav2Vec2 (8.91)** | -3.43 |

实验表明，大多数模型对噪声扰动鲁棒，但对音频修改和压缩（尤其是神经编解码器）脆弱。语音基础模型（如Wav2Vec2、HuBERT）在多数失真下优于传统模型。增大模型规模可提升鲁棒性，但收益递减。通过数据增强（如添加噪声）或推理时语音增强可改善对未见失真的鲁棒性。

## 🎯 结论与影响

本文系统揭示了音频深度伪造检测模型在真实世界失真下的鲁棒性短板，强调评估需覆盖多种失真类型。语音基础模型因大规模预训练更具优势，但仍有改进空间。未来研究应关注开发更鲁棒的检测框架，并考虑实际部署中的不可预测失真。

## ⚠️ 局限与未解决问题

仅评估了10种模型和18种失真，可能未覆盖所有场景。未深入分析模型内部机制对鲁棒性的影响。未提供开源代码或模型权重，可复现性受限。未考虑对抗性攻击等更复杂的失真。

---

<div class="paper-footer"><span>评分：8.8</span><span>原始：7.8</span><span>+1 重点领域加权</span><a href="/audio-paper-daily/posts/2026-07-07/">← 返回 2026-07-07 速递</a></div>
