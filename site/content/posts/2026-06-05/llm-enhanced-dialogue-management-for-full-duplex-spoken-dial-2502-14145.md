---
title: "LLM-Enhanced Dialogue Management for Full-Duplex Spoken Dialogue Systems"
date: 2026-06-05T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#对话管理"]
summary: "提出一个轻量级LLM作为语义VAD模块，用于全双工语音对话系统中的话轮管理，实现实时决策并降低计算开销。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#对话管理</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#全双工语音对话系统</span> <span class="tag-pill tag-pill-soft">#语义VAD</span> <span class="tag-pill tag-pill-soft">#大语言模型</span> <span class="tag-pill tag-pill-soft">#话轮管理</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2502.14145</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-06-05</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2502.14145" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2502.14145" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出一个轻量级LLM作为语义VAD模块，用于全双工语音对话系统中的话轮管理，实现实时决策并降低计算开销。
</div>

## 👥 作者与机构

**Hao Zhang** ¹ · Weiwei Li · Rilin Chen · Vinay Kothapally · Meng Yu · Dong Yu

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合语音对话系统、对话管理方向的研究者。建议重点阅读§3语义VAD设计及§4实验部分，关注控制令牌预测和消融实验。

## 🌍 研究背景

全双工语音对话系统需要实时协调听、说、思考，传统VAD无法区分有意/无意打断和查询完成。现有方法通常将对话管理集成在对话引擎中，难以独立优化且计算开销大。本文提出将语义VAD作为独立对话管理器，利用轻量级LLM预测控制令牌，实现高效话轮切换与保持。

## 💡 核心创新

1. 提出语义VAD模块作为独立对话管理器
2. 设计四种控制令牌实现话轮切换与保持
3. 区分有意/无意打断及查询完成检测
4. 独立优化DM无需重训核心对话引擎
5. 短间隔处理实现实时决策

## 🏗️ 模型架构

输入语音经短间隔切分后送入轻量级0.5B LLM（语义VAD），该LLM经全双工对话数据微调，输出四种控制令牌（turn-switch, turn-keep, barge-in, query-complete）。核心对话引擎（CDE）仅在需要生成响应时激活，语义VAD实时决策话轮管理，降低计算开销。

## 📚 数据集

- 全双工对话数据集（训练/评估，未公开具体名称）

## 📊 实验结果

摘要未提供具体实验指标，但声称语义VAD能有效管理话轮切换，区分打断类型，并在实时性和计算效率上优于传统方法。

## 🎯 结论与影响

本文提出的语义VAD模块为全双工语音对话系统提供了一种高效的话轮管理方案，通过轻量级LLM实现实时决策，独立优化DM，有望推动下一代全双工SDS的实用化。

## ⚠️ 局限与未解决问题

摘要未报告具体实验数据，缺乏与现有方法的定量对比；数据集未公开，可复现性存疑；仅评估了0.5B模型，更大LLM的效果未知；未讨论多语言或噪声环境下的鲁棒性。

---

<div class="paper-footer"><span>评分：7.2</span><span>原始：7.2</span><a href="/audio-paper-daily/posts/2026-06-05/">← 返回 2026-06-05 速递</a></div>
