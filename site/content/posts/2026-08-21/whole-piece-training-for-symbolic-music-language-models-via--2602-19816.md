---
title: "Whole-Piece Training for Symbolic Music Language Models via Full-Horizon Compressed Recurrence"
date: 2026-08-21T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#音乐生成"]
summary: "提出全曲训练框架FHCR，通过压缩KV表示保留完整时间跨度，实现符号音乐语言模型的高效全曲训练，并引入KRCU诊断长程上下文利用。"
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
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#符号音乐建模</span> <span class="tag-pill tag-pill-soft">#长程依赖</span> <span class="tag-pill tag-pill-soft">#循环压缩</span> <span class="tag-pill tag-pill-soft">#KV缓存压缩</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2602.19816</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-08-21</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner"><div class="oc-headline"><span class="oc-pulse"></span><span class="oc-title">本论文已开源</span><span class="oc-hint">点击下方卡片直达对应资源</span></div><div class="oc-grid"><a class="oc-chip oc-chip-proj" href="https://wholemusic.github.io" target="_blank" rel="noopener"><span class="oc-icon">🌐</span><span class="oc-text"><span class="oc-label">项目主页</span><span class="oc-sub">wholemusic.github.io</span></span></a><a class="oc-chip oc-chip-demo" href="https://wholemusic.github.io" target="_blank" rel="noopener"><span class="oc-icon">🔊</span><span class="oc-text"><span class="oc-label">在线 Demo</span><span class="oc-sub">wholemusic.github.io</span></span></a></div></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2602.19816" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2602.19816" target="_blank" rel="noopener">📑 PDF</a><a class="rsrc rsrc-proj" href="https://wholemusic.github.io" target="_blank" rel="noopener">🌐 项目主页</a><a class="rsrc rsrc-demo" href="https://wholemusic.github.io" target="_blank" rel="noopener">🔊 Demo</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出全曲训练框架FHCR，通过压缩KV表示保留完整时间跨度，实现符号音乐语言模型的高效全曲训练，并引入KRCU诊断长程上下文利用。
</div>

## 👥 作者与机构

**Yungang Yi** ¹ · Weihua Li · Matthew Kuo · Catherine Shi · Quan Bai

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合音乐生成、序列建模和高效Transformer研究者。建议重点阅读第3节方法（FHCR机制）和第4节实验（KRCU分析）。可先看摘要和图表，再深入方法细节。

## 🌍 研究背景

符号音乐语言模型通常沿用固定长度序列训练，但音乐结构跨越完整作品，片段化训练阻碍了全曲的连续条件建模。现有方法受限于GPU内存，难以处理长序列。本文旨在解决全曲训练的效率问题，同时保持长程依赖建模能力。

## 💡 核心创新

1. 提出FHCR，压缩KV表示降低内存，保留完整时间跨度
2. 引入KRCU诊断，评估模型对长程上下文的利用程度
3. 在MAESTRO上验证FHCR保持长程利用且降低内存成本

## 🏗️ 模型架构

输入为符号音乐序列（如MIDI），采用Transformer解码器作为主干，通过循环机制维护跨片段的隐藏状态。FHCR对KV缓存进行压缩（如低秩近似或投影），减少内存占用，同时保留完整时间跨度。输出为下一个token的概率分布。

## 📚 数据集

- MAESTRO（训练/评估，包含钢琴演奏MIDI）

## 📊 实验结果

摘要未提供具体数值指标，但通过KRCU诊断显示，全曲模型能利用远超局部窗口的上下文，而缩短循环记忆的时间范围会显著削弱长程依赖。FHCR在保持长程利用的同时大幅降低循环记忆成本。

## 🎯 结论与影响

本文证明保留循环历史的时间范围对高效全曲建模至关重要，且可通过KV压缩降低内存成本。该工作为符号音乐语言模型的长序列训练提供了新思路，可能推动音乐生成和长程依赖建模的发展。

## ⚠️ 局限与未解决问题

摘要未提及局限，但可能包括：仅在MAESTRO单一数据集上验证，缺乏与其他长序列方法的对比，未报告生成质量指标（如音乐性），且KRCU诊断的有效性需进一步验证。

## 🔗 开源资源

- **项目主页**：<https://wholemusic.github.io>
- **Demo / 试听**：<https://wholemusic.github.io>

---

<div class="paper-footer"><span>评分：7.2</span><span>原始：7.2</span><a href="/audio-paper-daily/posts/2026-08-21/">← 返回 2026-08-21 速递</a></div>
