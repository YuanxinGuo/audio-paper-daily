---
title: "Synchronization and Turn-Taking in Full-Duplex Speech Dialogue Models"
date: 2026-05-21T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#语音对话系统"]
summary: "通过模拟Moshi模型全双工对话，研究说话人间的表征同步与话轮转换预测。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero">
<div class="hero-score">
<div class="score-num">6.5</div>
<div class="score-stars">★★★☆☆</div>
<div class="score-tier">前50%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#语音对话系统</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#全双工对话</span> <span class="tag-pill tag-pill-soft">#神经同步</span> <span class="tag-pill tag-pill-soft">#话轮转换</span> <span class="tag-pill tag-pill-soft">#表征分析</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2605.20356</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-05-21</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2605.20356" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2605.20356" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>通过模拟Moshi模型全双工对话，研究说话人间的表征同步与话轮转换预测。
</div>

## 👥 作者与机构

**Pablo Riera** ¹ · Pablo Brusco · Cristina Kuo · Marcelo Sancinetti · S. R. K. Branavan

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合对话系统研究者。重点看§3同步测量方法与§4话轮预测实验。可先读图2的CKA结果。

## 🌍 研究背景

全双工口语对话模型能同时听和说，但内部表征如何协调尚不清楚。受人类神经耦合启发，本文研究Moshi模型在受控条件下的表征同步与话轮转换预测。

## 💡 核心创新

1. 用CKA测量全双工对话中的表征同步
2. 从延迟内部激活中预测话轮转换
3. 模拟噪声和偏置对同步的影响

## 🏗️ 模型架构

使用两个预训练Moshi模型实例进行全双工对话模拟。Moshi基于Transformer，包含音频编码器、文本编码器和自回归解码器。输入为音频流，输出为文本和音频。通过控制信道噪声和解码偏置操纵条件。同步分析用CKA，话轮预测用因果LSTM。

## 📚 数据集

- 模拟对话数据（由两个Moshi模型生成，无公开数据集）

## 📊 实验结果

摘要未提供具体数值结果，仅描述定性发现：无噪声时同步最强，近零延迟；噪声降低同步；内部状态编码可提前预测话轮转换。

## 🎯 结论与影响

全双工对话模型在无噪声时表现出强表征同步，且内部状态包含话轮转换的预测信息。该分析为理解对话模型交互机制提供了新视角，可能指导更自然的对话系统设计。

## ⚠️ 局限与未解决问题

仅使用单一模型Moshi，未对比其他架构；模拟对话而非真实人机交互；未报告同步或预测的量化指标；缺乏消融实验。

---

<div class="paper-footer"><span>评分：6.5</span><span>原始：6.5</span><a href="/audio-paper-daily/posts/2026-05-21/">← 返回 2026-05-21 速递</a></div>
