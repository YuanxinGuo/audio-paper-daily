---
title: "Can Large Audio Language Models Ignore Multilingual Distractors? An Evaluation of Their Selective Auditory Attention Capabilities"
date: 2026-05-19T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#音频理解"]
summary: "提出MUSA基准，评估大音频语言模型在多语言干扰下的选择性听觉注意能力，发现强单源性能不保证鲁棒性。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#音频理解</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#选择性听觉注意</span> <span class="tag-pill tag-pill-soft">#多语言干扰</span> <span class="tag-pill tag-pill-soft">#鸡尾酒会问题</span> <span class="tag-pill tag-pill-soft">#大音频语言模型</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2605.17225</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-05-19</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2605.17225" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2605.17225" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出MUSA基准，评估大音频语言模型在多语言干扰下的选择性听觉注意能力，发现强单源性能不保证鲁棒性。
</div>

## 👥 作者与机构

**Heejoon Koo** ¹

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合音频理解、多语言语音处理及LALM评估研究者阅读。重点看§3实验设置与§4结果分析，特别是表1和表2。可先读摘要和结论。

## 🌍 研究背景

大音频语言模型（LALM）在语音理解任务中表现优异，但在多语言干扰环境下的选择性听觉注意能力尚未系统评估。现有基准多关注单语言或干净语音，缺乏对多语言干扰和鸡尾酒会场景的测试。本文旨在填补这一空白，通过构建多语言干扰的鸡尾酒会基准MUSA，评估LALM在复杂声学场景中的鲁棒性。

## 💡 核心创新

1. 提出MUSA多语言干扰基准，包含英语、西班牙语、韩语、中文干扰
2. 设计三种评估设置：单源、分离两阶段、端到端鸡尾酒会
3. 发现分离后仍存在源归属错误，揭示LALM的注意力缺陷

## 🏗️ 模型架构

本文不提出新模型，而是构建评估基准MUSA。MUSA包含英语目标对话与语义合理的干扰对话（英语/西班牙语/韩语/中文），在三种设置下评估：单源（无干扰）、基于源分离的两阶段（先分离后理解）、端到端鸡尾酒会（直接处理混合）。控制信噪比（SNR）变化。评估模型包括2个闭源和4个开源LALM。

## 📚 数据集

- MUSA（评估基准，包含多语言干扰对话，规模未提及）

## 📊 实验结果

摘要未提供具体数值结果，但指出强单源性能不保证鲁棒选择性注意：鸡尾酒会准确率在低SNR下下降，错误主要由干扰源混淆导致；分离虽减少声学重叠但未解决源归属，常产生自信的错误答案。

## 🎯 结论与影响

本文揭示了当前LALM在多语言干扰下选择性听觉注意的显著缺陷，强调单源性能不能代表鲁棒性。MUSA基准为未来研究提供了标准化评估工具，推动LALM在真实嘈杂环境中的部署。工业应用中需注意多语言干扰导致的错误。

## ⚠️ 局限与未解决问题

未报告具体模型参数量、推理延迟等效率指标；仅评估英语目标，未涵盖其他目标语言；干扰语言有限（4种）；未分析模型内部注意力机制；未提供开源代码和数据的当前状态。

---

<div class="paper-footer"><span>评分：7.2</span><span>原始：7.2</span><a href="/audio-paper-daily/posts/2026-05-19/">← 返回 2026-05-19 速递</a></div>
