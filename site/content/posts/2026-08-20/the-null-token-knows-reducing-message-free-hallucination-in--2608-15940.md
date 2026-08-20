---
title: "The Null Token Knows: Reducing Message-Free Hallucination in ASR and NMT"
date: 2026-08-20T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#语音识别"]
summary: "通过分析ASR和NMT模型中空标记的分数，提出利用空标记分数作为弃权信号来抑制无消息幻觉，并强调评估时应同时考虑抑制和删除成本。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#语音识别</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#语音识别</span> <span class="tag-pill tag-pill-soft">#机器翻译</span> <span class="tag-pill tag-pill-soft">#幻觉抑制</span> <span class="tag-pill tag-pill-soft">#空标记</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2608.15940</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-08-20</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2608.15940" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2608.15940" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>通过分析ASR和NMT模型中空标记的分数，提出利用空标记分数作为弃权信号来抑制无消息幻觉，并强调评估时应同时考虑抑制和删除成本。
</div>

## 👥 作者与机构

**Kirill Borodin** ¹ · Vasiliy Kudryavtsev · Ivan Viakhirev · Grach Mkrtchian

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合语音识别和机器翻译领域的研究者，尤其是关注模型鲁棒性和幻觉问题的读者。建议重点阅读第3节（空标记分数审计）和第4节（干预实验），可先看摘要和结论以快速了解核心发现。

## 🌍 研究背景

现代编码器-解码器系统在输入无可恢复消息时仍能生成流畅文本，导致幻觉问题。现有方法多依赖外部门控或监督信号，但未充分利用模型自身的空标记。本文旨在探究空标记分数是否可作为弃权信号，并分析干预的副作用。

## 💡 核心创新

1. 提出利用空标记分数作为弃权信号
2. 系统审计ASR和NMT模型中的空标记分数
3. 比较监督行编辑与外部门控方法
4. 强调评估需同时考虑抑制和删除成本
5. 将空标记作为幻觉诊断工具

## 🏗️ 模型架构

本文不提出新模型，而是分析现有编码器-解码器架构（如Whisper和翻译模型）中的空标记。输入为语音或文本，通过解码器生成序列，空标记分数由解码器输出层计算。在Whisper中，额外探测解码器状态并比较监督行编辑与外部门控。

## 📊 实验结果

摘要未提供具体实验数据，但指出空标记分数在多数模型中能提供有用的弃权信号，但标准解码未可靠利用。提高空标记分数可抑制幻觉，但过度干预会删除有效语音或缩短合法翻译。

## 🎯 结论与影响

空标记分数可作为幻觉诊断和弃权信号，但需平衡抑制与删除成本。该研究为评估弃权方法提供了新视角，建议未来工作关注成本权衡。对工业应用，可指导开发更可靠的幻觉抑制策略。

## ⚠️ 局限与未解决问题

摘要未提及具体实验细节，如数据集和基线，可能缺乏全面对比。未讨论不同模型架构的泛化性，以及空标记分数在不同噪声条件下的稳定性。

---

<div class="paper-footer"><span>评分：7.2</span><span>原始：7.2</span><a href="/audio-paper-daily/posts/2026-08-20/">← 返回 2026-08-20 速递</a></div>
