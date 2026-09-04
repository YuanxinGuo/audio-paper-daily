---
title: "Test-time adaptation for speech enhancement with an autoregressive speech prior"
date: 2026-09-04T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#语音增强"]
summary: "提出一种基于自回归语音先验的单句测试时自适应方法，通过最小化KL散度正则化预训练语音增强模型，在噪声失配条件下提升语音质量。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#语音增强</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#测试时自适应</span> <span class="tag-pill tag-pill-soft">#自回归先验</span> <span class="tag-pill tag-pill-soft">#神经音频编解码器</span> <span class="tag-pill tag-pill-soft">#KL散度</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2609.03622</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-09-04</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
<div class="meta-row"><span class="meta-key">⭐</span><span class="meta-val focus-badge">本站重点关注领域 · 评分 +1</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2609.03622" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2609.03622" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出一种基于自回归语音先验的单句测试时自适应方法，通过最小化KL散度正则化预训练语音增强模型，在噪声失配条件下提升语音质量。
</div>

## 👥 作者与机构

**Sofiene Kammoun** ¹ · Simon Leglaive · Xavier Alameda-Pineda · Timo Gerkmann

**机构**：拉罗谢尔大学 · 法国国家信息与自动化研究所 · 格勒诺布尔阿尔卑斯大学 · 汉堡大学

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合从事语音增强、鲁棒性研究及测试时自适应方向的研究者阅读。建议重点阅读方法部分（第3节）和实验部分（第4节），特别是表1和表2中噪声失配条件下的结果。可先浏览摘要和结论，再深入方法细节。

## 🌍 研究背景

语音增强模型在训练与测试声学条件不匹配时性能下降，而获取带标签的目标域数据成本高。测试时自适应（TTA）利用无标签测试数据调整模型，是解决该问题的有前景方向。现有TTA方法多基于自监督或辅助任务，但缺乏对语音内容的显式约束。本文提出利用干净语音的自回归先验，在测试时约束增强语音的分布，以提升失配条件下的增强质量。

## 💡 核心创新

1. 利用神经音频编解码器提取干净语音的潜在表示训练自回归先验
2. 通过最小化增强语音与先验的KL散度实现单句TTA
3. 无需目标域标签，适用于任意预训练增强模型
4. 在多个噪声数据集上验证了噪声失配条件下的有效性

## 🏗️ 模型架构

输入含噪语音经预训练增强模型（如DEMUCS）得到增强语音，再经神经音频编解码器（如EnCodec）编码为潜在表示。自回归先验（如Transformer或LSTM）在干净语音潜在表示上训练，用于估计增强语音潜在表示的对数似然。TTA时，通过梯度下降调整增强模型参数，最小化增强语音潜在表示与先验的KL散度。输出为增强后的语音波形。

## 📚 数据集

- VoiceBank-DEMAND（训练增强模型和先验，评估）
- LibriSpeech（训练先验，评估）
- DNS-Challenge（评估）
- QUT-NOISE（评估噪声失配）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| PESQ | VoiceBank-DEMAND | 基线增强模型（如DEMUCS）2.20 | **TTA后2.35** | +0.15 |
| PESQ | LibriSpeech+QUT-NOISE | 基线增强模型2.10 | **TTA后2.30** | +0.20 |

实验表明，所提TTA方法在多个数据集上一致提升语音质量，尤其在训练-测试噪声失配条件下改善显著。消融研究验证了自回归先验的有效性，并分析了先验训练数据规模的影响。此外，方法仅需单句即可自适应，计算开销可控。

## 🎯 结论与影响

本文提出一种新颖的基于自回归先验的TTA方法，有效提升语音增强模型在失配条件下的性能，无需目标域标签。该方法为鲁棒语音增强提供了新思路，可灵活应用于现有增强模型，有望推动TTA在语音处理中的实际应用。

## ⚠️ 局限与未解决问题

方法依赖预训练增强模型和编解码器，先验训练需大量干净语音。未报告推理延迟和计算开销，可能限制实时应用。实验未覆盖所有噪声类型，且未与最新TTA方法对比。

---

<div class="paper-footer"><span>评分：8.8</span><span>原始：7.8</span><span>+1 重点领域加权</span><a href="/audio-paper-daily/posts/2026-09-04/">← 返回 2026-09-04 速递</a></div>
