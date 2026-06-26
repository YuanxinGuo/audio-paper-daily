---
title: "Neural Speaker Diarization via Multilingual Training: Evaluation on Low-Resource Nepali-Hindi Speech"
date: 2026-06-26T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#说话人日志"]
summary: "本文通过多语言训练，比较EEND-EDA和DiaPer两种端到端神经说话人日志架构在低资源尼泊尔-印地语上的表现，DiaPer在多数场景下DER更低。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#说话人日志</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#低资源语音</span> <span class="tag-pill tag-pill-soft">#多语言训练</span> <span class="tag-pill tag-pill-soft">#端到端神经说话人日志</span> <span class="tag-pill tag-pill-soft">#Perceiver</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2606.26144</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-06-26</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2606.26144" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2606.26144" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>本文通过多语言训练，比较EEND-EDA和DiaPer两种端到端神经说话人日志架构在低资源尼泊尔-印地语上的表现，DiaPer在多数场景下DER更低。
</div>

## 👥 作者与机构

**Samip Neupane** ¹ · Sandesh Pokhrel · Sandesh Pyakurel · Basanta Joshi

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合从事说话人日志、低资源语音处理的研究者阅读。建议重点看§3多语言训练设置和§4实验结果（表1-2），对比两种架构在不同说话人数下的DER差异。

## 🌍 研究背景

说话人日志是确定多说话人录音中“谁在何时说话”的任务，在会议转录、多语言信息检索中至关重要。端到端神经说话人日志（EEND）在英语等资源丰富语言上表现优异，但在标注数据稀缺的低资源语言上性能大幅下降。本文针对尼泊尔-印地语这一低资源语言，探索多语言训练策略，并比较EEND-EDA和DiaPer两种架构的跨语言泛化能力。

## 💡 核心创新

1. 多语言训练策略结合英语、VoxCeleb及尼泊尔-印地语数据
2. 首次将DiaPer（Perceiver-based attractors）应用于低资源说话人日志
3. 构建尼泊尔-印地语（NeHi）测试集用于低资源评估
4. 系统比较EEND-EDA与DiaPer在多说话人场景下的性能

## 🏗️ 模型架构

输入为多说话人混合语音的log-mel filterbank特征。EEND-EDA采用Transformer编码器后接LSTM-based encoder-decoder attractors，输出每个时间步的说话人活动向量。DiaPer使用Perceiver架构作为attractor计算模块，通过交叉注意力从输入序列中提取固定数量的说话人嵌入。两种模型均通过多任务学习同时预测说话人活动和数量。

## 📚 数据集

- LibriSpeech（英语，训练/评估）
- VoxCeleb（多说话人英语，训练/评估）
- Nepali-Hindi (NeHi)（自收集，训练/评估，低资源）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| DER (%) | NeHi 2-speaker | EEND-EDA 1.50 | **DiaPer 3.28** | +1.78 |
| DER (%) | NeHi 3-speaker | EEND-EDA 9.68 | **DiaPer 2.02** | -7.66 |
| DER (%) | NeHi 4-speaker | EEND-EDA 16.17 | **DiaPer 4.05** | -12.12 |
| DER (%) | NeHi mixed-speaker | EEND-EDA 11.19 | **DiaPer 4.76** | -6.43 |

在NeHi测试集上，DiaPer在3/4说话人及混合场景下DER显著低于EEND-EDA（如4-speaker场景DER从16.17%降至4.05%），但在2-speaker场景下EEND-EDA更优（1.50% vs 3.28%）。在LibriSpeech和VoxCeleb上，DiaPer同样在多数多说话人设置中表现更好，表明Perceiver架构对复杂场景的鲁棒性。

## 🎯 结论与影响

本文证明基于Perceiver的端到端神经说话人日志（DiaPer）在多语言训练下对低资源尼泊尔-印地语有效，尤其在多说话人场景中大幅优于EEND-EDA。该工作为低资源语言的说话人日志提供了可行方案，未来可扩展至更多低资源语言。工业上可用于多语言会议转录系统。

## ⚠️ 局限与未解决问题

仅比较了两种架构，未与更先进的说话人日志系统（如基于聚类的方法）对比；NeHi数据集规模较小且未公开；未分析模型对未见语言的泛化能力；缺乏推理速度和参数量对比。

---

<div class="paper-footer"><span>评分：7.2</span><span>原始：7.2</span><a href="/audio-paper-daily/posts/2026-06-26/">← 返回 2026-06-26 速递</a></div>
