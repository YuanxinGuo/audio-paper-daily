---
title: "Spacing Out: On the Reliability of Binaural Music Source Separation Metrics"
date: 2026-07-29T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#双耳音频"]
summary: "通过感知实验评估双耳音乐源分离中客观空间失真指标与人类感知的相关性，发现ITD估计不可靠，需设计专用空间指标。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero hero-focus">
<div class="hero-score">
<div class="score-num">8.2</div>
<div class="score-stars">★★★★☆</div>
<div class="score-tier">前25%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#双耳音频</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#乐器分离</span> <span class="tag-pill tag-pill-soft">#空间音频</span> <span class="tag-pill tag-pill-soft">#感知评估</span> <span class="tag-pill tag-pill-soft">#客观指标</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2607.25919</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-07-29</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
<div class="meta-row"><span class="meta-key">⭐</span><span class="meta-val focus-badge">本站重点关注领域 · 评分 +1</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2607.25919" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2607.25919" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>通过感知实验评估双耳音乐源分离中客观空间失真指标与人类感知的相关性，发现ITD估计不可靠，需设计专用空间指标。
</div>

## 👥 作者与机构

**Richa Namballa** ¹ · Magdalena Fuentes

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合双耳音频、音乐源分离及空间感知评估领域的研究者。建议重点阅读§3感知实验设计和§4结果分析，尤其是ITD估计的鲁棒性-准确性权衡部分。可跳过§2背景中已知的立体声MSS方法。

## 🌍 研究背景

沉浸式音频日益流行，但双耳音乐在MIR中研究不足，尤其是音乐源分离（MSS）任务。现有立体声MSS模型处理双耳音频时会降低分离音轨的空间质量，破坏沉浸感。客观空间失真指标（如ITD、ILD）常用于评估，但其与人类感知的相关性尚未被系统验证。本文通过感知实验，评估这些指标在双耳MSS中的可靠性，发现ITD估计对噪声和分离伪影高度敏感，且不同估计方法存在鲁棒性与准确性的权衡。

## 💡 核心创新

1. 首次系统评估双耳MSS中客观空间指标与感知的相关性
2. 揭示ITD估计在双耳音乐分离中的不可靠性
3. 发现窄带乐器（如贝斯）下ITD估计的鲁棒性-准确性权衡

## 🏗️ 模型架构

本文为感知评估研究，无模型架构。实验使用现有立体声MSS模型（如Demucs）处理双耳音频，生成分离音轨，然后计算客观空间指标（ITD、ILD等），并与人类主观评分对比。

## 📚 数据集

- 自建双耳音乐混合数据集（包含多乐器音轨，用于感知实验）

## 📊 实验结果

摘要未提供具体数值结果，但指出ITD估计与人类感知的一致性较差，且不同ITD估计方法在鲁棒性和准确性间存在权衡，尤其对窄带乐器影响显著。

## 🎯 结论与影响

本文通过感知实验证实现有客观空间指标在双耳MSS中不可靠，强调需开发准确、可解释的双耳音乐专用空间指标。该结论将推动双耳MSS模型设计时考虑空间保真度，对沉浸式音频工业应用（如VR/AR）有重要指导意义。

## ⚠️ 局限与未解决问题

未提供具体指标数值和统计显著性；仅使用单一MSS模型（Demucs），泛化性有限；未评估其他空间线索（如ILD、IC）的感知相关性；未提出新指标或改进方法。

---

<div class="paper-footer"><span>评分：8.2</span><span>原始：7.2</span><span>+1 重点领域加权</span><a href="/audio-paper-daily/posts/2026-07-29/">← 返回 2026-07-29 速递</a></div>
