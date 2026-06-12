---
title: "Generative Modeling of Bach-Style Symbolic Music: A Comparative Study of Autoregressive, Latent-Variable, and Adversarial Approaches"
date: 2026-06-12T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#音乐生成"]
summary: "比较自回归LSTM、潜变量模型和GAN在巴赫风格钢琴音乐生成上的表现，发现自回归模型生成质量最佳。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero">
<div class="hero-score">
<div class="score-num">6.8</div>
<div class="score-stars">★★★☆☆</div>
<div class="score-tier">前50%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#音乐生成</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#符号音乐</span> <span class="tag-pill tag-pill-soft">#自回归模型</span> <span class="tag-pill tag-pill-soft">#变分自编码器</span> <span class="tag-pill tag-pill-soft">#生成对抗网络</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2606.13626</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-06-12</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2606.13626" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2606.13626" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>比较自回归LSTM、潜变量模型和GAN在巴赫风格钢琴音乐生成上的表现，发现自回归模型生成质量最佳。
</div>

## 👥 作者与机构

**Kyuil Lee** ¹ · Dezhi Yu · Yongkang Huang

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合对符号音乐生成感兴趣的研究者。可重点阅读§3实验设置和§4结果对比，了解不同模型在音乐连贯性和结构上的差异。

## 🌍 研究背景

符号音乐生成是计算创造力领域的重要问题，巴赫风格复调音乐因结构严谨成为经典基准。现有方法包括自回归模型、VAE和GAN，但缺乏系统比较。本文使用统一MIDI语料库，公平对比三类模型在复调序列建模、潜表示学习和风格连贯性上的能力。

## 💡 核心创新

1. 统一语料库和评估协议比较三类生成模型
2. 揭示VQ-VAE缓解后验坍塌优于传统VAE
3. 指出GAN在巴赫风格生成中的训练不稳定问题

## 🏗️ 模型架构

输入为MIDI音符序列（音高、时长、偏移量）。自回归模型使用LSTM+注意力；潜变量模型包括循环VAE和VQ-VAE；GAN使用生成器和判别器。输出为符号音乐序列。

## 📚 数据集

- Bach MIDI语料库（训练/评估，规模未提及）

## 📊 实验结果

摘要未提供具体数值指标，仅定性描述：自回归LSTM+注意力生成样本最连贯；VQ-VAE输出比传统VAE更结构化；GAN捕捉局部音高模式但训练困难，泛化到巴赫风格不可靠。

## 🎯 结论与影响

自回归模型在巴赫风格音乐生成中表现最优，VQ-VAE有效改善潜变量模型的结构化输出，GAN因训练不稳定不适用于此任务。该比较为符号音乐生成的方法选择提供了参考。

## ⚠️ 局限与未解决问题

缺乏定量评估指标（如音乐理论评分或听众测试）；语料库规模未说明；未报告模型参数量或计算成本；未与最新Transformer或扩散模型对比。

---

<div class="paper-footer"><span>评分：6.8</span><span>原始：6.8</span><a href="/audio-paper-daily/posts/2026-06-12/">← 返回 2026-06-12 速递</a></div>
