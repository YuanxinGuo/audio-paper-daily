---
title: "Auditory and Visual Virtualization in 6DoF XR: Effects on Plausibility and Dynamic Auditory Distance Perception"
date: 2026-11-06T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#双耳音频"]
summary: "首个在6DoF XR中联合评估实时房间声学模拟与双耳渲染对可信度及动态听觉距离感知影响的感知研究。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero hero-focus">
<div class="hero-score">
<div class="score-num">7.8</div>
<div class="score-stars">★★★★☆</div>
<div class="score-tier">中等</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#双耳音频</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#双耳音频</span> <span class="tag-pill tag-pill-soft">#房间声学模拟</span> <span class="tag-pill tag-pill-soft">#听觉感知</span> <span class="tag-pill tag-pill-soft">#XR</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2611.07612</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-11-06</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
<div class="meta-row"><span class="meta-key">⭐</span><span class="meta-val focus-badge">本站重点关注领域 · 评分 +1</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2611.07612" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2611.07612" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>首个在6DoF XR中联合评估实时房间声学模拟与双耳渲染对可信度及动态听觉距离感知影响的感知研究。
</div>

## 👥 作者与机构

**Johannes M. Arend** ¹ · Christian Scheer · Melissa Ram\'irez · Stefan Weinzierl · Fabian Brinkmann

**机构**：柏林工业大学

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合从事双耳渲染、房间声学模拟与XR听觉感知的研究者阅读。若关注系统实现，重点看§3的系统搭建与声学模拟管线；若关注感知结论，先看可信度实验与ADP实验的结果表及四种虚拟化条件的对比。不建议通读全部统计细节。

## 🌍 研究背景

6DoF XR系统已能实时进行房间声学模拟与双耳渲染，但其感知有效性——虚拟声源是否可信、行为是否与真实世界一致——缺乏系统验证。此前双耳渲染评估多在静态或简单场景进行，缺少与视听匹配的大房间虚拟复刻对照，也少有研究同时考察可信度与动态听觉距离感知（ADP）。本文要回答：听觉与视觉虚拟化分别及联合如何影响可信度与ADP。

## 💡 核心创新

1. 构建视听匹配的大实验室6DoF XR复刻系统，集成实时房间声学模拟与双耳渲染
2. 在AAR与VR两种条件下对比真实与虚拟声源的可信度
3. 基于移动的ADP实验，分解听觉虚拟化与视觉虚拟化对距离判断的独立与叠加效应

## 🏗️ 模型架构

系统为6DoF XR感知实验平台：真实房间经几何与声学建模得到虚拟复刻，实时房间声学模拟（含早期反射与晚期混响）驱动双耳渲染，输出头戴式双耳信号；视觉端提供与声学场景匹配的VR/AAR渲染。实验一为可信度评分任务，比较真实与虚拟声源在AAR与VR下的主观可信度；实验二为移动式ADP任务，被试在四种虚拟化条件下走向声源并判断距离，记录准确率、带符号误差与任务努力度。摘要未给出网络结构与参数量。

## 📚 数据集

- 45名被试的行为与主观评分数据（自建实验，评估）

## 📊 实验结果

摘要未给出具体数值指标。主要发现：AAR与VR中双耳渲染均被认为可信，VR可信度更高；ADP任务中任何虚拟化都降低准确率并增加努力度，但整体表现仍较高；纯听觉虚拟化导致距离被感知偏近，纯视觉虚拟化降低准确率但无显著方向偏差；全VR下两种效应未叠加。

## 🎯 结论与影响

最强结论是当前6DoF XR系统已能提供可信的双耳渲染并支撑交互式感知研究，但虚拟化会系统性影响动态距离判断。这提示XR音频评估需按任务做行为验证，对VR/AR音频系统设计与感知实验方法学有直接参考价值。

## ⚠️ 局限与未解决问题

仅单一房间与有限被试，缺乏跨房间、跨声源类型泛化验证；未报告渲染延迟与计算开销；ADP任务仅测距离维度，未涉及方位；统计细节与效应量需正文确认，摘要信息不足以判断对比基线是否充分。

---

<div class="paper-footer"><span>评分：7.8</span><span>原始：6.8</span><span>+1 重点领域加权</span><a href="/audio-paper-daily/posts/2026-11-06/">← 返回 2026-11-06 速递</a></div>
