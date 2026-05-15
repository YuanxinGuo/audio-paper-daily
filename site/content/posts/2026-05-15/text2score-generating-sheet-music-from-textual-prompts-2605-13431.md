---
title: "Text2Score: Generating Sheet Music From Textual Prompts"
date: 2026-05-15T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#ABC记谱法", "#LLM规划", "#两阶段生成", "#文本到乐谱", "#符号音乐生成"]
summary: "提出Text2Score两阶段框架，通过LLM规划音乐属性后生成ABC记谱法乐谱，在客观和主观评估上优于纯LLM和端到端基线。"
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
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#文本到乐谱</span> <span class="tag-pill tag-pill-soft">#两阶段生成</span> <span class="tag-pill tag-pill-soft">#ABC记谱法</span> <span class="tag-pill tag-pill-soft">#LLM规划</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2605.13431</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-05-15</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2605.13431" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2605.13431" target="_blank" rel="noopener">📑 PDF</a><a class="rsrc rsrc-proj" href="https://keshavbhandari.github.io/portfolio/text2score" target="_blank" rel="noopener">🌐 项目主页</a><a class="rsrc rsrc-demo" href="https://keshavbhandari.github.io/portfolio/text2score" target="_blank" rel="noopener">🔊 Demo</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出Text2Score两阶段框架，通过LLM规划音乐属性后生成ABC记谱法乐谱，在客观和主观评估上优于纯LLM和端到端基线。
</div>

## 👥 作者与机构

**Keshav Bhandari** ¹ · Sungkyun Chang · Abhinaba Roy · Francesca Ronchini · Emmanouil Benetos · Dorien Herremans · Simon Colton

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合符号音乐生成、文本到音乐生成方向的研究者。建议重点阅读§3两阶段框架设计（规划与执行）和§4评估方法（含专家验证）。可先看表2和表3的客观指标对比。

## 🌍 研究背景

文本驱动的符号音乐生成面临文本-音乐对齐数据稀缺和自动标注不可靠的挑战。现有工作多聚焦MIDI，而乐谱表示（如ABC记谱法）在文本生成中未被充分探索。之前SOTA包括纯LLM代理框架和端到端模型，但存在生成质量不稳定、结构约束弱等问题。本文旨在通过两阶段框架（规划+执行）直接利用符号XML数据监督，避免噪声文本-音乐对，生成结构化的乐谱。

## 💡 核心创新

1. 两阶段框架：LLM规划器生成结构化度量级计划
2. 从符号XML直接导出监督信号，避免文本-音乐对
3. 执行阶段生成ABC记谱法，受计划约束
4. 引入包含可演奏性、可读性等维度的评估框架

## 🏗️ 模型架构

输入为自然语言提示。第一阶段：LLM规划器（如GPT-4）将提示转换为结构化度量级计划，定义乐器、调号、拍号、和声等属性。第二阶段：执行阶段的生成模型（基于Transformer）以计划为条件，生成ABC记谱法表示的乐谱。输出为ABC格式文本，可渲染为五线谱。模型参数量未提及。

## 📚 数据集

- 自建数据集（训练/评估，来源为符号XML数据，规模未提及）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| 客观指标（如可演奏性、可读性等） | 自建测试集 | 纯LLM代理框架（未提供具体值） | **优于基线（未提供具体值）** | 未提供具体数值 |

摘要未提供具体数值，仅称Text2Score在客观和主观维度上一致优于纯LLM代理框架和三个端到端基线。主观评估由专家音乐家验证，涵盖可演奏性、可读性、乐器利用、结构复杂性和提示遵循度。

## 🎯 结论与影响

Text2Score通过两阶段框架有效生成结构化的乐谱，避免了文本-音乐对稀缺问题。其规划-执行范式为符号音乐生成提供了新思路，有望推动文本到乐谱的实用化。开源数据集和代码有助于后续研究。

## ⚠️ 局限与未解决问题

摘要未明确承认局限。可能的问题：数据集规模未提及，可能偏小；未报告推理延迟；对比基线可能不够强（如未与最新符号生成模型比较）；客观指标具体数值缺失，削弱说服力。

## 🔗 开源资源

- **项目主页**：<https://keshavbhandari.github.io/portfolio/text2score>
- **Demo / 试听**：<https://keshavbhandari.github.io/portfolio/text2score>

---

<div class="paper-footer"><span>评分：7.8</span><span>原始：7.8</span><a href="/audio-paper-daily/posts/2026-05-15/">← 返回 2026-05-15 速递</a></div>
