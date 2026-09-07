---
title: "Who Wins the Conflict? Mechanistic Interpretability of Text Bias in Audio LLMs"
date: 2026-09-07T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#音频理解"]
summary: "首次从机制层面分析音频大语言模型中的文本主导偏差，发现文本路径抑制而非擦除音频信息，并提出无需训练的反向修补干预以缓解该偏差。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#音频理解</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#可解释性</span> <span class="tag-pill tag-pill-soft">#文本偏差</span> <span class="tag-pill tag-pill-soft">#音频大语言模型</span> <span class="tag-pill tag-pill-soft">#机制分析</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2606.18924</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-09-07</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2606.18924" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2606.18924" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>首次从机制层面分析音频大语言模型中的文本主导偏差，发现文本路径抑制而非擦除音频信息，并提出无需训练的反向修补干预以缓解该偏差。
</div>

## 👥 作者与机构

**Hyebin Cho** ¹ · Suho Yoo · Jaehyuk Jang · Changick Kim · Joon Son Chung

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合音频大语言模型研究者、可解释性方向学者。建议重点阅读第3节（机制分析）与第4节（back-patching方法），可先看图2与表1了解核心发现。若关注模型内部表征，值得通读。

## 🌍 研究背景

音频大语言模型在多模态理解中表现出色，但存在文本主导偏差，即模型更依赖文本而非声学证据，导致幻觉响应。此前研究多关注性能提升，缺乏对内部机制的深入分析。本文首次通过追踪内部表征的跨层传播，揭示文本与音频路径的功能差异及交互机制，为缓解偏差提供新视角。

## 💡 核心创新

1. 首次对音频大语言模型文本主导偏差进行机制级分析
2. 发现文本路径主动抑制完整音频表征而非擦除
3. 提出无需训练的back-patching干预方法，路由后期音频激活至早期层
4. 在多个模型上验证back-patching能一致降低文本主导偏差

## 🏗️ 模型架构

本文分析对象为音频大语言模型，具体架构未在摘要中详述，但涉及多模态编码器与语言模型主干。方法上，通过追踪内部表征跨层传播，识别文本与音频路径的分离与汇聚。干预方法back-patching将后期层音频激活回传至早期层，以增强音频表征。

## 📊 实验结果

摘要未提供具体数值指标，但指出back-patching在多个模型上一致降低文本主导偏差，表明其有效性。实验设计涵盖不同模型，但缺乏定量细节。

## 🎯 结论与影响

本文首次揭示音频大语言模型中文本主导偏差的机制：文本路径主动抑制完整音频表征。提出的back-patching干预无需训练即可缓解该偏差，为提升多模态鲁棒性提供新思路。对后续研究，可探索更精细的干预策略及在更多任务上的应用。

## ⚠️ 局限与未解决问题

摘要未提及局限，但作为机制分析，可能缺乏对模型规模、任务多样性的覆盖；back-patching的通用性及对下游任务的影响未充分讨论；未提供计算开销或推理效率分析。

---

<div class="paper-footer"><span>评分：7.8</span><span>原始：7.8</span><a href="/audio-paper-daily/posts/2026-09-07/">← 返回 2026-09-07 速递</a></div>
