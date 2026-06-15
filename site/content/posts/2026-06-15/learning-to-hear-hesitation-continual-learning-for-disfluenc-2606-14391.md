---
title: "Learning to Hear Hesitation: Continual Learning for Disfluency-Aware ASR"
date: 2026-06-15T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#语音识别"]
summary: "在预训练ASR模型中引入口吃标记，并通过持续学习在有限数据集上适应口吃语音，避免灾难性遗忘。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero">
<div class="hero-score">
<div class="score-num">7.2</div>
<div class="score-stars">★★★★☆</div>
<div class="score-tier">前50%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#语音识别</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#口吃语音识别</span> <span class="tag-pill tag-pill-soft">#持续学习</span> <span class="tag-pill tag-pill-soft">#语音识别</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2606.14391</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-06-15</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2606.14391" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2606.14391" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>在预训练ASR模型中引入口吃标记，并通过持续学习在有限数据集上适应口吃语音，避免灾难性遗忘。
</div>

## 👥 作者与机构

**Henri-Leon Kordt** ¹ · Theresa Pekarek Rosin · Jae Hee Lee · Stefan Wermter

**机构**：汉堡大学

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合研究口吃语音识别或持续学习在ASR中应用的读者。建议重点阅读第3节方法部分和第4节实验分析，特别是跨注意力头机制的发现。

## 🌍 研究背景

大规模ASR系统在处理口吃语音时表现不佳，常被优化以省略口吃，导致信息丢失和幻觉。先前工作集中于逐字转录和集成口吃标记，但适应有限数据集会导致通用领域知识的灾难性遗忘。本文旨在通过持续学习（CL）结合显式口吃标记来解决这一权衡问题。

## 💡 核心创新

1. 在预训练ASR中引入显式口吃标记
2. 利用持续学习避免灾难性遗忘
3. 发现标记学习与ASR性能之间的权衡
4. 揭示跨注意力头机制在CL方法中的一致性

## 🏗️ 模型架构

基于预训练ASR模型（如Whisper或Wav2Vec2），在输出词汇表中添加口吃标记（如[UH]、[UM]）。首先在包含口吃标记的数据集上微调以稳定标记机制，然后通过持续学习方法（如EWC、SI或LwF）在额外口吃数据集上继续训练，同时保留通用ASR能力。模型输入为语音特征，输出为包含口吃标记的转录文本。

## 📚 数据集

- Switchboard（口吃语音数据集，训练与评估）
- LibriSpeech（通用语音数据集，评估泛化能力）

## 📊 实验结果

摘要未提供具体数值结果，但提到通过详细分析模型动态，发现了标记学习与ASR性能之间的权衡，以及跨持续学习方法共享的跨注意力头机制。实验可能包括口吃标记F1分数和ASR词错误率（WER）的对比。

## 🎯 结论与影响

本文证明了通过持续学习在预训练ASR中引入口吃标记是可行的，能够在不严重遗忘通用知识的情况下适应口吃语音。该工作为口吃语音识别提供了新思路，并揭示了模型内部机制，对开发更鲁棒的ASR系统有潜在影响。

## ⚠️ 局限与未解决问题

摘要未提及模型参数量、推理速度或具体数据集规模；未报告与全微调或从头训练方法的对比；缺乏在多种口吃类型上的细粒度分析；持续学习方法的选择可能影响结果，但未充分讨论。

---

<div class="paper-footer"><span>评分：7.2</span><span>原始：7.2</span><a href="/audio-paper-daily/posts/2026-06-15/">← 返回 2026-06-15 速递</a></div>
