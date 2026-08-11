---
title: "MI-MIDI: Mechanistic Interpretability of Text-to-MIDI Generation Models via Probing, Lenses and Steering"
date: 2026-08-11T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#音乐生成"]
summary: "本文对两种文本到MIDI生成模型进行机制可解释性分析，揭示音乐概念在模型内部的线性表示与操控方法。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#音乐生成</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#可解释性</span> <span class="tag-pill tag-pill-soft">#符号音乐</span> <span class="tag-pill tag-pill-soft">#文本到MIDI</span> <span class="tag-pill tag-pill-soft">#探针</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2608.06638</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-08-11</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2608.06638" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2608.06638" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>本文对两种文本到MIDI生成模型进行机制可解释性分析，揭示音乐概念在模型内部的线性表示与操控方法。
</div>

## 👥 作者与机构

Jakub Po\'cwiardowski · Mateusz Modrzejewski

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合对音乐生成模型可解释性、模型内部机制感兴趣的读者。建议重点阅读第3节（方法）和第4节（实验结果），可先看摘要中的图1和表1。若时间有限，可略读第2节背景。

## 🌍 研究背景

音乐生成的可解释性研究多集中于音频模型，符号音乐模型（如MIDI生成）的机制分析尚属空白。现有文本到MIDI模型（如text2midi和MIDI-LLM）虽能生成音乐，但其内部如何表示和操控音乐概念（如音高、配器）仍不明确。本文旨在通过多种可解释性工具，揭示这些模型内部结构，并探索如何通过干预控制生成音乐的特征。

## 💡 核心创新

1. 首次对文本到MIDI模型进行系统性机制可解释性分析
2. 提出双方向干预协议，隔离方向性控制
3. 对比两种架构（编码器-解码器与LLM扩展）的内部表示差异
4. 利用线性探针、透镜、激活修补和差分均值引导等多种技术
5. 发现音乐概念在两种模型中均可线性解码，且干预效果因架构而异

## 🏗️ 模型架构

分析对象为两种模型：text2midi（编码器-解码器结构）和MIDI-LLM（基于Llama 3.2 1B扩展MIDI token）。方法包括线性探针（从中间层提取特征预测音乐属性）、logit透镜和调谐透镜（将内部表示映射到输出词汇）、激活修补（替换特定层激活以观察影响）以及差分均值引导（通过调整激活方向控制生成）。

## 📊 实验结果

摘要未提供具体量化指标，但定性结果表明：两种模型均能线性解码音高、配器、和声和纹理；text2midi逐层细化预测，而MIDI-LLM在后期才转向音乐词汇；激活修补显示MIDI-LLM中提示驱动的乐器转移在后期衰减；引导可双向改变音域和复音，MIDI-LLM还可控制速度和能量。

## 🎯 结论与影响

本文揭示了文本到MIDI模型内部音乐概念的可解释性，表明架构差异导致表示形成和控制方式不同。该研究为符号音乐生成模型的可解释性分析提供了实用工具包，有助于未来设计更可控的音乐生成系统，并可能促进音乐生成模型的调试和个性化控制。

## ⚠️ 局限与未解决问题

摘要未提及局限，但可推测：分析仅针对两个特定模型，泛化性未知；未提供量化评估指标；干预可能对生成质量有副作用；未讨论计算开销。

---

<div class="paper-footer"><span>评分：7.2</span><span>原始：7.2</span><a href="/audio-paper-daily/posts/2026-08-11/">← 返回 2026-08-11 速递</a></div>
