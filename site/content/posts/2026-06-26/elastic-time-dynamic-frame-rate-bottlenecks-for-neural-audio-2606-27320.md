---
title: "Elastic Time: Dynamic Frame Rate Bottlenecks for Neural Audio Coding"
date: 2026-06-26T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#音频编码"]
summary: "提出Elastic Time动态帧率瓶颈，将固定帧率音频自编码器转为动态帧率，在推理时实现率控并提升效率-质量权衡。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#音频编码</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#神经音频编解码</span> <span class="tag-pill tag-pill-soft">#变帧率</span> <span class="tag-pill tag-pill-soft">#自编码器</span> <span class="tag-pill tag-pill-soft">#效率优化</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2606.27320</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-06-26</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2606.27320" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2606.27320" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出Elastic Time动态帧率瓶颈，将固定帧率音频自编码器转为动态帧率，在推理时实现率控并提升效率-质量权衡。
</div>

## 👥 作者与机构

**Dimitrios Bralios** ¹ · Paris Smaragdis · Minje Kim

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合音频编码、生成模型研究者。建议重点阅读§3方法部分及§4实验中的率控与效率对比。可先看Fig.2理解动态帧率机制。

## 🌍 研究背景

神经音频自编码器是压缩、特征提取和生成的核心组件。现有系统虽支持可变比特率，但大多仍采用固定潜在帧率，为信息密度差异大的区域分配相同时间预算，导致序列冗余。本文旨在解决固定帧率带来的效率低下问题，提出动态帧率瓶颈以自适应调整时间分辨率。

## 💡 核心创新

1. 轻量级潜在预测器用于决定帧跳过
2. 高效贪心边界选择策略
3. 将固定帧率自编码器转换为动态帧率
4. 部署时可调节率控

## 🏗️ 模型架构

输入音频经编码器生成固定帧率潜在表示；轻量级潜在预测器评估每帧重要性，通过贪心边界选择决定哪些帧可跳过；解码器从保留帧重建音频。整体框架可适配任意自编码器，无需重新训练。

## 📊 实验结果

摘要未提供具体数值结果，仅提及方法在效率-质量权衡上优于基线，支持部署时率控。

## 🎯 结论与影响

Elastic Time提供了一种灵活机制，将固定帧率音频自编码器转为动态帧率，有望提升生成和长上下文任务的效率。该方法无需重新训练即可适配现有模型，对工业部署具有实用价值。

## ⚠️ 局限与未解决问题

摘要未提及局限。可能的问题：贪心边界选择非最优；预测器引入额外计算；未在多种自编码器架构上验证；缺乏与变比特率方法的直接对比。

---

<div class="paper-footer"><span>评分：7.2</span><span>原始：7.2</span><a href="/audio-paper-daily/posts/2026-06-26/">← 返回 2026-06-26 速递</a></div>
