---
title: "Towards Interpretable Framework for Neural Audio Codecs via Sparse Autoencoders: A Case Study on Accent Information"
date: 2026-07-08T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#音频编码器可解释性"]
summary: "使用稀疏自编码器分解神经音频编解码器的隐表示，以口音信息为案例量化可解释性。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero">
<div class="hero-score">
<div class="score-num">7.2</div>
<div class="score-stars">★★★★☆</div>
<div class="score-tier">前25%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#音频编码器可解释性</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#稀疏自编码器</span> <span class="tag-pill tag-pill-soft">#口音信息</span> <span class="tag-pill tag-pill-soft">#神经音频编解码器</span> <span class="tag-pill tag-pill-soft">#可解释性</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2603.18359</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-07-08</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2603.18359" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2603.18359" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>使用稀疏自编码器分解神经音频编解码器的隐表示，以口音信息为案例量化可解释性。
</div>

## 👥 作者与机构

**Shih-Heng Wang** ¹ · Tiantian Feng · Aditya Kommineni · Thanathai Lertpetchpun · Bowen Yi · Xuan Shi · Shrikanth Narayanan

**机构**：南加州大学

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合对音频编解码器可解释性、口音分析感兴趣的读者。建议重点阅读第3节（SAE配置与评估方法）和第4节（实验结果与发现），尤其是不同NAC编码口音方式的对比。

## 🌍 研究背景

神经音频编解码器（NAC）如EnCodec、DAC等被广泛用于语音压缩与生成，但其隐表示如何编码语言和副语言信息尚不明确。现有可解释性研究多针对语音识别模型，对NAC的探索有限。口音作为重要的副语言属性，其编码方式的理解有助于公平性和鲁棒性分析。本文提出用稀疏自编码器（SAE）分解NAC表示，并构建量化框架评估可解释性。

## 💡 核心创新

1. 提出用SAE分解NAC密集表示为稀疏可解释激活
2. 构建相对性能指数（RPI）量化可解释性
3. 发现DAC和SpeechTokenizer可解释性最高
4. 揭示声学/音素导向NAC编码口音的不同机制
5. 发现低比特率EnCodec变体可解释性更高

## 🏗️ 模型架构

输入为NAC编码器的隐层表示（如EnCodec、DAC、SpeechTokenizer、HiFi-Codec的编码器输出），通过稀疏自编码器（SAE）将其分解为稀疏激活向量。SAE包含编码器（线性层+ReLU）和解码器（线性层），通过L1稀疏正则化训练。评估时，从稀疏激活中训练线性分类器预测口音类别，以分类准确率作为可解释性指标。

## 📚 数据集

- Common Voice（口音分类训练与评估）
- LibriTTS（辅助评估）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| 口音分类准确率（RPI） | Common Voice | 原始NAC表示（如EnCodec 1.5kbps 0.72） | **SAE稀疏表示（如EnCodec 1.5kbps 0.78）** | +0.06 |

在16种SAE配置下评估4种NAC模型，DAC和SpeechTokenizer的稀疏表示口音分类准确率最高。声学导向NAC（如DAC）的口音信息主要编码在激活幅度中，而音素导向NAC（如SpeechTokenizer）更依赖激活位置。低比特率EnCodec变体（1.5kbps）比高比特率（6kbps）可解释性更高。

## 🎯 结论与影响

本文证明SAE能有效提升NAC表示的可解释性，并揭示不同NAC编码口音信息的机制差异。该框架可推广至其他副语言属性（如情感、说话人身份），为NAC在敏感应用中的可信部署提供分析工具。工业上，可指导选择更可解释的编解码器用于语音分析。

## ⚠️ 局限与未解决问题

仅针对口音单一属性，未验证其他副语言属性；SAE配置（如稀疏度）未充分优化；评估仅用线性分类器，可能低估表示能力；未在真实下游任务（如语音增强）中验证可解释性的影响。

---

<div class="paper-footer"><span>评分：7.2</span><span>原始：7.2</span><a href="/audio-paper-daily/posts/2026-07-08/">← 返回 2026-07-08 速递</a></div>
