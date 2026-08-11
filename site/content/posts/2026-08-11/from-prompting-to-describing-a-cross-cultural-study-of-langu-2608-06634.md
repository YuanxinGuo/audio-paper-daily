---
title: "From Prompting to Describing: A Cross-Cultural Study of Language for AI-Generated Music"
date: 2026-08-11T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#音乐生成"]
summary: "通过配对真实Udio提示与听众描述，构建音乐提示词汇分类法，发现提示以体裁和叙事为主，叙事提示导致语义错位，且跨文化描述存在差异。"
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
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#文本到音乐</span> <span class="tag-pill tag-pill-soft">#跨文化</span> <span class="tag-pill tag-pill-soft">#用户研究</span> <span class="tag-pill tag-pill-soft">#语义对齐</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2608.06634</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-08-11</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2608.06634" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2608.06634" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>通过配对真实Udio提示与听众描述，构建音乐提示词汇分类法，发现提示以体裁和叙事为主，叙事提示导致语义错位，且跨文化描述存在差异。
</div>

## 👥 作者与机构

**Sangheon Park** ¹ · Claire Arthur

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合音乐信息检索、文本到音乐生成及人机交互研究者阅读。建议重点阅读第3节（分类法构建）和第4节（语义对齐分析），可先看摘要中的图1和表2。

## 🌍 研究背景

文本到音乐（TTM）生成系统允许用户通过自然语言提示创作音乐，但提示语言与描述听到音乐的语言是否一致尚不清楚。现有研究多关注生成模型本身，缺乏对用户提示语言的分析。本文通过配对真实提示与听众描述，构建基于真实用户数据的音乐提示词汇分类法，并分析提示与感知之间的语义对齐，以及跨文化差异。

## 💡 核心创新

1. 构建基于真实用户数据的音乐提示词汇分类法
2. 发现提示中体裁和叙事语言占主导，叙事提示导致语义错位
3. 初步跨文化比较揭示描述维度差异
4. 结合词级和向量级分析揭示结构不对称性
5. 使用真实Udio提示和生成音频，而非人工合成数据

## 🏗️ 模型架构

本文不涉及模型架构，而是采用数据分析方法：收集200个真实Udio提示及其生成音频，由英语和韩语听众提供自由描述，通过人工标注构建分类法，并利用词嵌入和向量分析进行语义对齐和跨文化比较。

## 📚 数据集

- Udio提示与生成音频（200对，用于分析）
- 英语听众描述（n=70，用于评估）
- 韩语听众描述（n=78，用于评估）

## 📊 实验结果

摘要未提供具体数值指标，但报告了主要发现：提示中体裁和叙事语言占主导，体裁术语从提示到感知的传播最可靠，而叙事提示是语义错位的最强预测因子。跨文化比较显示描述特征在叙事、功能和情感维度上存在差异。

## 🎯 结论与影响

本文揭示了TTM系统中提示语言与感知描述之间的结构不对称性，强调叙事提示可能导致语义错位，并指出当前TTM系统可能无法适应多样化的音乐表达方式。研究为改进TTM系统的提示理解和生成评估提供了新视角，对跨文化音乐生成系统设计具有启示。

## ⚠️ 局限与未解决问题

样本量有限（200个提示，148名听众），且仅涉及英语和韩语，可能无法代表全球多样性。分析基于Udio平台，可能引入平台偏差。未提供定量指标，缺乏统计显著性检验。

---

<div class="paper-footer"><span>评分：7.2</span><span>原始：7.2</span><a href="/audio-paper-daily/posts/2026-08-11/">← 返回 2026-08-11 速递</a></div>
