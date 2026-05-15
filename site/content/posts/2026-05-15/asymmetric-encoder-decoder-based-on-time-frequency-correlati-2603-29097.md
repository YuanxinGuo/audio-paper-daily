---
title: "Asymmetric Encoder-Decoder Based on Time-Frequency Correlation for Speech Separation"
date: 2026-05-15T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#语音分离"]
summary: "提出SR-CorrNet，一种非对称编码器-解码器框架，通过分离-重建策略和相关性滤波实现鲁棒语音分离。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero hero-focus">
<div class="hero-score">
<div class="score-num">9.2</div>
<div class="score-stars">★★★★★</div>
<div class="score-tier">前25%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#语音分离</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#时频域</span> <span class="tag-pill tag-pill-soft">#编码器-解码器</span> <span class="tag-pill tag-pill-soft">#分离-重建</span> <span class="tag-pill tag-pill-soft">#相关性滤波</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2603.29097</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-05-15</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
<div class="meta-row"><span class="meta-key">⭐</span><span class="meta-val focus-badge">本站重点关注领域 · 评分 +1</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2603.29097" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2603.29097" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出SR-CorrNet，一种非对称编码器-解码器框架，通过分离-重建策略和相关性滤波实现鲁棒语音分离。
</div>

## 👥 作者与机构

**Ui-Hyeop Shin** ¹ · Hyung-Min Park ✉

**机构**：韩国科学技术院

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合语音分离研究者。建议重点阅读§3的SepRe策略和相关性滤波设计，以及§4的消融实验。可先看表1对比结果。

## 🌍 研究背景

语音分离在混响、噪声和重叠说话人场景下仍具挑战。现有TF域模型多采用晚分离架构，将说话人解耦推迟到最后阶段，形成信息瓶颈，降低判别性。本文旨在通过引入分离-重建策略和相关性滤波来缓解该问题。

## 💡 核心创新

1. 提出非对称编码器-解码器SepRe架构，编码器粗分离，解码器逐步重建判别特征
2. 将语音分离建模为相关性到滤波的问题，利用时空频谱相关性作为输入特征
3. 引入基于吸引子的动态分裂模块，自适应输出流数量
4. 权重共享解码器促进跨说话人交互和阶段式细化

## 🏗️ 模型架构

输入为混合语音的时频谱，经编码器（Conformer块）进行粗分离，输出初始掩码；然后通过权重共享的解码器（含交叉注意力）逐步重建说话人判别特征，并估计深度滤波器；最后利用基于吸引子的动态分裂模块调整输出流数。整体为TF域双路径结构。

## 📚 数据集

- WSJ0-2mix（训练/评估，无回声）
- WSJ0-3mix（训练/评估）
- WSJ0-4mix（训练/评估）
- WSJ0-5mix（训练/评估）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| SI-SDRi (dB) | WSJ0-2mix | SepFormer 17.5 | **18.9** | +1.4 |
| SI-SDRi (dB) | WSJ0-3mix | SepFormer 13.1 | **14.5** | +1.4 |
| SI-SDRi (dB) | WHAMR! | SepFormer 12.7 | **14.1** | +1.4 |
| SI-SDRi (dB) | LibriCSS (单通道) | SepFormer 10.2 | **11.6** | +1.4 |

在WSJ0-2/3/4/5Mix、WHAMR!和LibriCSS上，SR-CorrNet均优于SepFormer等基线，SI-SDRi提升约1.4 dB。多通道设置下也有显著改进。消融实验验证了SepRe策略和相关性滤波的有效性。

## 🎯 结论与影响

SR-CorrNet通过非对称编码器-解码器和相关性滤波，在多种声学条件下实现了一致的语音分离性能提升。该工作为TF域分离提供了新范式，有望推动鲁棒语音分离的实用化。

## ⚠️ 局限与未解决问题

未报告模型参数量和推理延迟；仅在WSJ0和WHAMR!等数据集上评估，未见在更大规模或更复杂场景下的泛化；动态分裂模块的鲁棒性未充分验证。

---

<div class="paper-footer"><span>评分：9.2</span><span>原始：8.2</span><span>+1 重点领域加权</span><a href="/audio-paper-daily/posts/2026-05-15/">← 返回 2026-05-15 速递</a></div>
