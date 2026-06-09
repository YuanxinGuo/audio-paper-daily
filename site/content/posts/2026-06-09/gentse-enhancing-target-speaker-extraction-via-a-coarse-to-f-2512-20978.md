---
title: "GenTSE: Enhancing Target Speaker Extraction via a Coarse-to-Fine Generative Language Model"
date: 2026-06-09T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#目标说话人提取"]
summary: "提出GenTSE，一种两阶段解码器仅生成式语言模型，通过粗到细的语义和声学令牌预测实现高保真目标说话人提取。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#目标说话人提取</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#生成式语言模型</span> <span class="tag-pill tag-pill-soft">#语音增强</span> <span class="tag-pill tag-pill-soft">#语音分离</span> <span class="tag-pill tag-pill-soft">#自监督学习</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2512.20978</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-06-09</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
<div class="meta-row"><span class="meta-key">⭐</span><span class="meta-val focus-badge">本站重点关注领域 · 评分 +1</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2512.20978" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2512.20978" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出GenTSE，一种两阶段解码器仅生成式语言模型，通过粗到细的语义和声学令牌预测实现高保真目标说话人提取。
</div>

## 👥 作者与机构

**Haoyang Li** ¹ · Xuyi Zhuang · Azmat Adnan · Ye Ni · Wei Rao · Shreyas Gopal · Eng Siong Chng · Boon Siew Han · … 等 1 人

**机构**：南洋理工大学 · 新加坡科技设计大学

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合目标说话人提取和生成式语音处理研究者。建议通读，重点看第3节方法（两阶段生成和Frozen-LM Conditioning）及第4节实验（表1-3）。可复现其DPO训练策略。

## 🌍 研究背景

目标说话人提取（TSE）旨在从混合语音中提取特定说话人的语音。现有方法多基于判别式模型，泛化性和语音保真度有限。近期基于语言模型（LM）的生成式方法展现出潜力，但存在离散化提示导致上下文丢失、训练与推理不匹配等问题。本文提出GenTSE，利用连续SSL和编解码器嵌入，通过两阶段生成和Frozen-LM Conditioning训练策略提升性能。

## 💡 核心创新

1. 两阶段粗到细生成：先预测语义令牌，再生成声学令牌
2. 连续嵌入替代离散化提示，保留丰富上下文
3. Frozen-LM Conditioning训练策略减少曝光偏差
4. 应用DPO对齐感知偏好

## 🏗️ 模型架构

GenTSE采用两阶段解码器仅LM架构。输入为混合语音的连续SSL特征（如WavLM）和说话人嵌入。Stage-1使用解码器LM预测粗粒度语义令牌（来自HuBERT），Stage-2以语义令牌为条件，使用另一个解码器LM生成细粒度声学令牌（来自EnCodec）。两阶段均采用因果自注意力。训练时使用Frozen-LM Conditioning：用早期检查点的预测令牌作为条件，而非真实令牌。最后通过DPO微调。输出声学令牌经EnCodec解码器合成波形。

## 📚 数据集

- Libri2Mix（训练/评估，包含混合语音和干净目标语音）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| SI-SDRi (dB) | Libri2Mix test | SepFormer 16.4 | **18.9** | +2.5 dB |
| PESQ | Libri2Mix test | SepFormer 3.52 | **3.78** | +0.26 |
| WER (%) | Libri2Mix test | SepFormer 4.8 | **3.9** | -0.9% |

在Libri2Mix上，GenTSE在SI-SDRi、PESQ和WER上均超越SepFormer等强基线，且优于先前LM-based系统（如Voicebox TSE）。消融实验验证了两阶段生成和Frozen-LM Conditioning的有效性。DPO进一步提升了感知质量。模型参数量约300M，推理速度未报告。

## 🎯 结论与影响

GenTSE通过粗到细的生成式LM在TSE任务上取得了显著性能提升，证明了生成式方法在语音提取中的潜力。其两阶段设计和训练策略可为后续生成式语音处理研究提供参考。工业上可用于高保真语音提取场景，但实时性需进一步优化。

## ⚠️ 局限与未解决问题

仅在Libri2Mix上评估，未见跨数据集泛化实验；未报告推理延迟和参数量对比；DPO训练依赖额外偏好数据；两阶段生成可能增加推理复杂度；未与最新判别式方法（如Mamba-TSE）对比。

---

<div class="paper-footer"><span>评分：9.2</span><span>原始：8.2</span><span>+1 重点领域加权</span><a href="/audio-paper-daily/posts/2026-06-09/">← 返回 2026-06-09 速递</a></div>
