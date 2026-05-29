---
title: "AV-EMO-Reasoning: Benchmarking Emotional Reasoning Capabilities in Omni-modal LLMS with Audio-visual Cues"
date: 2026-05-29T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#情感推理"]
summary: "提出AV-EMO-Reasoning基准，系统评估全模态大语言模型在音频-视觉线索下的情感推理能力。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#情感推理</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#多模态大语言模型</span> <span class="tag-pill tag-pill-soft">#情感识别</span> <span class="tag-pill tag-pill-soft">#音频-视觉</span> <span class="tag-pill tag-pill-soft">#对话系统</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2510.07355</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-05-29</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2510.07355" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2510.07355" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出AV-EMO-Reasoning基准，系统评估全模态大语言模型在音频-视觉线索下的情感推理能力。
</div>

## 👥 作者与机构

**Dingkun Zhou** ¹ · Krish Patel · Ajay Kankipati · Akshaj Gupta · Zeyi Austin Li · Mohul Shukla · Vibhor Narang · Sara Kofman · … 等 9 人

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合多模态LLM和情感计算研究者。建议重点阅读§3基准设计和§4评估指标，了解任务构建和度量方法。若关注模型能力，可看实验结果部分。

## 🌍 研究背景

情感理解是人机交互的关键，但现有全模态大语言模型（Omni-modal LLMs）在情感推理方面的评估不足。尽管模型能处理音频和视觉输入，但缺乏系统基准测试其是否真正理解用户情感并产生恰当回应。本文旨在填补这一空白，通过构建包含合成和真实对话的音频-视觉语料库，结合情感感知和交互推理指标，提供可复现的评估标准。

## 💡 核心创新

1. 提出AV-EMO-Reasoning基准，包含合成单轮/多轮对话和真实世界子集
2. 设计情感感知和交互推理两类评估指标
3. 系统评估全模态LLM在音频-视觉情感推理中的表现

## 🏗️ 模型架构

本文不提出新模型，而是构建评估基准。基准包含音频-视觉语料库（合成对话和真实子集），以及评估框架：情感感知指标（如情感分类准确率）和交互推理指标（如回应恰当性）。评估对象为现有全模态LLM，输入为音频-视觉对话片段，输出为情感理解和回应。

## 📚 数据集

- 合成对话语料（训练/评估，包含单轮和多轮对话）
- 真实世界子集（评估，来自公开资源）

## 📊 实验结果

摘要未提供具体实验结果，仅说明基准设计。实际评估结果需参考论文全文。

## 🎯 结论与影响

AV-EMO-Reasoning为全模态LLM的情感推理能力提供了系统评估框架，有助于推动更自然、自适应的人机交互。该基准可复现，有望成为情感感知对话评估的标准工具，对工业界开发情感智能助手具有指导意义。

## ⚠️ 局限与未解决问题

基准依赖合成数据，真实场景泛化性待验证；评估指标可能未覆盖所有情感维度；未报告模型计算开销；缺乏与人类表现的对比。

---

<div class="paper-footer"><span>评分：6.5</span><span>原始：6.5</span><a href="/audio-paper-daily/posts/2026-05-29/">← 返回 2026-05-29 速递</a></div>
