---
title: "Text2Score: Generating Sheet Music From Textual Prompts"
date: 2026-05-15T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#符号音乐生成"]
summary: "提出Text2Score两阶段框架，通过LLM规划+生成模型执行，从文本提示生成乐谱，无需文本-音乐配对数据。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero">
<div class="hero-score">
<div class="score-num">7.8</div>
<div class="score-stars">★★★★☆</div>
<div class="score-tier">前25%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#符号音乐生成</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#文本驱动音乐生成</span> <span class="tag-pill tag-pill-soft">#乐谱生成</span> <span class="tag-pill tag-pill-soft">#两阶段框架</span> <span class="tag-pill tag-pill-soft">#ABC记谱法</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2605.13431</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-05-15</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner"><div class="oc-headline"><span class="oc-pulse"></span><span class="oc-title">本论文已开源</span><span class="oc-hint">点击下方卡片直达对应资源</span></div><div class="oc-grid"><a class="oc-chip oc-chip-proj" href="https://keshavbhandari.github.io/portfolio/text2score" target="_blank" rel="noopener"><span class="oc-icon">🌐</span><span class="oc-text"><span class="oc-label">项目主页</span><span class="oc-sub">keshavbhandari.github.io/portfolio/text2score</span></span></a><a class="oc-chip oc-chip-demo" href="https://keshavbhandari.github.io/portfolio/text2score" target="_blank" rel="noopener"><span class="oc-icon">🔊</span><span class="oc-text"><span class="oc-label">在线 Demo</span><span class="oc-sub">keshavbhandari.github.io/portfolio/text2score</span></span></a></div></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2605.13431" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2605.13431" target="_blank" rel="noopener">📑 PDF</a><a class="rsrc rsrc-proj" href="https://keshavbhandari.github.io/portfolio/text2score" target="_blank" rel="noopener">🌐 项目主页</a><a class="rsrc rsrc-demo" href="https://keshavbhandari.github.io/portfolio/text2score" target="_blank" rel="noopener">🔊 Demo</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出Text2Score两阶段框架，通过LLM规划+生成模型执行，从文本提示生成乐谱，无需文本-音乐配对数据。
</div>

## 👥 作者与机构

**Keshav Bhandari** ¹ · Sungkyun Chang · Abhinaba Roy · Francesca Ronchini · Emmanouil Benetos · Dorien Herremans · Simon Colton

**机构**：新加坡科技设计大学 · 索尼AI · 伦敦玛丽女王大学

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合符号音乐生成、文本到音乐生成方向的研究者。建议重点阅读§3两阶段框架设计及§4评估框架。可先看图2架构概览，再读§3.2执行阶段的条件生成细节。

## 🌍 研究背景

文本驱动的符号音乐生成面临文本-音乐配对数据稀缺和自动标注不可靠的挑战。现有工作多聚焦MIDI，乐谱表示在文本生成中未被充分探索。之前方法依赖端到端模型或纯LLM，但缺乏结构化规划。本文提出两阶段框架，通过从XML符号数据直接获取监督信号，绕过文本-音乐配对需求。

## 💡 核心创新

1. 两阶段规划-执行框架分离语义规划与乐谱生成
2. LLM orchestrator生成结构化小节级音乐属性计划
3. 基于ABC记谱法的条件生成模型执行阶段
4. 包含可演奏性、可读性等维度的综合评估框架

## 🏗️ 模型架构

输入为自然语言文本提示。第一阶段：LLM orchestrator将提示转换为结构化的小节级计划，包含乐器、调性、拍号、和声等属性。第二阶段：生成模型以计划为条件，生成交织的ABC记谱法符号序列。生成模型采用Transformer架构，编码计划信息并自回归解码ABC token。输出为ABC格式乐谱。

## 📚 数据集

- 自建数据集（训练，来自开源XML乐谱库）
- 自建评估集（评估，包含多样文本提示）

## 📊 实验结果

摘要未提供具体数值指标，但声称Text2Score在客观和主观维度上均优于纯LLM框架和三个端到端基线。评估涵盖可演奏性、可读性、乐器利用、结构复杂度和提示遵循度，并由专业音乐家验证。

## 🎯 结论与影响

Text2Score通过两阶段框架有效解决了文本-音乐配对数据稀缺问题，在乐谱生成任务上优于现有方法。其结构化规划策略为符号音乐生成提供了新范式，有望推动文本驱动的乐谱创作工具发展。开源资源有利于社区复现和扩展。

## ⚠️ 局限与未解决问题

摘要未提及推理效率或生成速度；评估集规模未知；未与基于MIDI的文本生成方法直接对比；ABC记谱法可能限制输出表现力（如力度、表情记号）；LLM规划阶段可能引入错误传播。

## 🔗 开源资源

- **项目主页**：<https://keshavbhandari.github.io/portfolio/text2score>
- **Demo / 试听**：<https://keshavbhandari.github.io/portfolio/text2score>

---

<div class="paper-footer"><span>评分：7.8</span><span>原始：7.8</span><a href="/audio-paper-daily/posts/2026-05-15/">← 返回 2026-05-15 速递</a></div>
