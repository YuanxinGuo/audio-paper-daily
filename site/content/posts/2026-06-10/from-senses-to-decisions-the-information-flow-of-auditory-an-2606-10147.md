---
title: "From Senses to Decisions: The Information Flow of Auditory and Visual Perception in Multimodal LLMs"
date: 2026-06-10T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#多模态大语言模型"]
summary: "系统分析音频-视觉大语言模型中音频和视觉信息流的路径与机制，揭示其顺序与并行路由模式。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#多模态大语言模型</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#信息流分析</span> <span class="tag-pill tag-pill-soft">#可解释性</span> <span class="tag-pill tag-pill-soft">#音频-视觉融合</span> <span class="tag-pill tag-pill-soft">#AVLLM</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2606.10147</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-06-10</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2606.10147" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2606.10147" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>系统分析音频-视觉大语言模型中音频和视觉信息流的路径与机制，揭示其顺序与并行路由模式。
</div>

## 👥 作者与机构

**Wish Suharitdamrong** ¹ · Muhammad Awais · Xiatian Zhu · Sara Atito

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合多模态LLM研究者、可解释性方向学者。建议重点阅读§3（信息流路径）和§4（丢弃策略），可先看Figure 2-4理解核心发现。

## 🌍 研究背景

多模态大语言模型（MLLM）能同时处理音频和视觉输入，但内部信息如何流动并影响决策尚不明确。现有工作多关注单模态或视觉-语言模型，缺乏对音频-视觉联合信息流的系统分析。本文旨在揭示AVLLM中音频和视觉信号的路由、利用与整合机制。

## 💡 核心创新

1. 首次系统分析AVLLM中音频-视觉信息流路径
2. 发现视频任务中遵循顺序信息流，多交错项时转为并行流
3. 提出信息转移后丢弃冗余token可提升效率且不影响性能
4. 跨模型尺度（3B/7B）验证发现泛化性

## 🏗️ 模型架构

分析对象为Qwen2.5-Omni和Video-SALMONN2 Plus两种AVLLM，输入为音频-视觉视频或多交错音频-视觉项。通过注意力权重和因果干预追踪token贡献，识别信息流路径。模型包含音频编码器、视觉编码器、LLM主干及融合模块。

## 📚 数据集

- Video-MME（评估，多模态视频理解）
- AVQA（评估，音频-视觉问答）
- MUSIC-AVQA（评估，音频-视觉问答）

## 📊 实验结果

摘要未提供具体量化指标，但通过注意力分析和token丢弃实验表明：在视频任务中，音频和视觉贡献沿顺序路径流动；在多交错项任务中，信息流转为并行。丢弃已传递信息的token可减少计算量，对预测影响极小甚至略有提升。

## 🎯 结论与影响

本文首次描绘了AVLLM中音频与视觉信息流的完整图景，揭示了顺序与并行路由机制，并证明信息传递后丢弃冗余token可提升效率。为多模态LLM的可解释性、设计和效率优化奠定基础。

## ⚠️ 局限与未解决问题

仅分析两种模型架构，未覆盖更多AVLLM变体；缺乏对信息流路径的定量度量（如信息瓶颈）；未探讨不同任务难度下信息流的变化；丢弃策略的通用性需更多验证。

---

<div class="paper-footer"><span>评分：7.2</span><span>原始：7.2</span><a href="/audio-paper-daily/posts/2026-06-10/">← 返回 2026-06-10 速递</a></div>
