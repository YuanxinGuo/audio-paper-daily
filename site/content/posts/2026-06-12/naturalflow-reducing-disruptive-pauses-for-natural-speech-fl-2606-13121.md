---
title: "NaturalFlow: Reducing Disruptive Pauses for Natural Speech Flow in Simultaneous Speech-to-Speech Translation"
date: 2026-06-12T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#语音翻译"]
summary: "提出流利度感知优化框架，在同步语音翻译中减少块间停顿，平衡低延迟与自然语音流。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#语音翻译</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#同声传译</span> <span class="tag-pill tag-pill-soft">#语音生成</span> <span class="tag-pill tag-pill-soft">#流利度优化</span> <span class="tag-pill tag-pill-soft">#低延迟</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2606.13121</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-06-12</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2606.13121" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2606.13121" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出流利度感知优化框架，在同步语音翻译中减少块间停顿，平衡低延迟与自然语音流。
</div>

## 👥 作者与机构

**Dongwook Lee** ¹ · Youngho Cho · Sangkwon Park · Heeseung Kim · Sungroh Yoon

**机构**：首尔大学

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合语音翻译、实时通信领域研究者。建议重点阅读§3优化框架和§4实验，关注其利用模型内部信号（语言多样性、时长变异性）减少停顿的方法。

## 🌍 研究背景

同步语音翻译追求低延迟，但过度优化导致输出语音碎片化、频繁停顿，增加听者认知负荷。现有方法多关注延迟和翻译质量，忽略语音流自然度。本文旨在找到同步翻译低延迟与连续翻译自然流之间的平衡点。

## 💡 核心创新

1. 提出流利度感知优化框架，减少块间停顿
2. 利用模型内部信号（语言多样性、时长变异性）指导停顿减少
3. 在长短格式基准上验证自然语音流与竞争性延迟/翻译质量
4. 无需外部停顿检测模块，端到端优化

## 🏗️ 模型架构

输入源语音→编码器→解码器→语音生成。框架在解码过程中利用模型内部信号（如语言多样性、预测时长变异性）动态调整输出块大小，最小化块间静音。未提及具体网络结构如Conformer等。

## 📚 数据集

- 短格式基准（训练/评估，未具体说明）
- 长格式基准（训练/评估，未具体说明）

## 📊 实验结果

摘要未提供具体数值指标，仅称在短格式和长格式基准上产生自然语音流，同时保持竞争性延迟和翻译质量。需阅读全文获取定量结果。

## 🎯 结论与影响

本文提出流利度感知优化框架，有效减少同步语音翻译中的块间停顿，提升语音自然度。对实时语音翻译系统的人机交互体验有积极影响，可能推动低延迟与自然流利度兼顾的实用系统发展。

## ⚠️ 局限与未解决问题

摘要未提及具体数据集、基线方法和量化结果，缺乏可复现性细节。未讨论框架在不同语言对、噪声环境下的鲁棒性，也未报告推理延迟或计算开销。

---

<div class="paper-footer"><span>评分：7.2</span><span>原始：7.2</span><a href="/audio-paper-daily/posts/2026-06-12/">← 返回 2026-06-12 速递</a></div>
