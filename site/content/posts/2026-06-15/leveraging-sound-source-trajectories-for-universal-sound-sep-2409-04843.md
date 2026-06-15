---
title: "Leveraging Sound Source Trajectories for Universal Sound Separation"
date: 2026-06-15T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#语音分离"]
summary: "提出利用声源定位与分离相互促进的迭代框架，通过轨迹细化提升移动声源分离性能。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero hero-focus">
<div class="hero-score">
<div class="score-num">8.8</div>
<div class="score-stars">★★★★☆</div>
<div class="score-tier">前25%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#语音分离</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#声源跟踪</span> <span class="tag-pill tag-pill-soft">#波束成形</span> <span class="tag-pill tag-pill-soft">#多通道</span> <span class="tag-pill tag-pill-soft">#移动声源</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2409.04843</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-06-15</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
<div class="meta-row"><span class="meta-key">⭐</span><span class="meta-val focus-badge">本站重点关注领域 · 评分 +1</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2409.04843" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2409.04843" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出利用声源定位与分离相互促进的迭代框架，通过轨迹细化提升移动声源分离性能。
</div>

## 👥 作者与机构

**Donghang Wu** ¹ · Xihong Wu · Tianshu Qu

**机构**：北京大学

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合研究多通道语音分离和声源跟踪的读者。建议重点阅读§2方法部分和§3实验设置，特别是相互促进机制的迭代细节。可先看表1对比结果。

## 🌍 研究背景

现有利用空间信息的声源分离方法需要先验的DOA或依赖不精确的定位结果，尤其在声源移动时性能下降。定位与分离是相互关联的问题，但以往方法未充分利用其互促机制。本文旨在通过迭代优化轨迹和分离结果，提升移动声源下的分离精度。

## 💡 核心创新

1. 提出定位与分离相互促进的迭代框架
2. 基于信号包络估计的初始跟踪方法
3. 利用分离信号细化轨迹，再提升分离性能
4. 第三阶段神经波束成形结合轨迹与多通道输出

## 🏗️ 模型架构

输入多通道混合音频 → 第一阶段：基于信号包络估计的初始跟踪，得到初步轨迹 → 第二阶段：利用轨迹进行声源分离（具体网络未明确），再对分离信号进行跟踪细化，迭代多次 → 第三阶段：神经波束成形（Neural Beamformer）基于细化轨迹和多通道分离输出，估计最终单通道分离结果。

## 📚 数据集

- 模拟混响移动声源数据集（训练/评估，具体名称未给出）

## 📊 实验结果

摘要未提供具体数值指标，仅说明在混响和移动声源条件下，所提方法基于细化跟踪结果实现了更准确的分离。需查阅全文获取SI-SDR等定量结果。

## 🎯 结论与影响

本文提出的定位与分离互促框架有效提升了移动声源分离性能，为多通道分离提供了新思路。后续研究可探索更高效的迭代策略或结合深度学习端到端优化。对工业应用如智能音箱、会议系统有潜在价值。

## ⚠️ 局限与未解决问题

摘要未提及具体数据集和基线对比，缺乏定量结果；迭代机制的计算开销未讨论；仅模拟混响条件，真实场景泛化性未知。

---

<div class="paper-footer"><span>评分：8.8</span><span>原始：7.8</span><span>+1 重点领域加权</span><a href="/audio-paper-daily/posts/2026-06-15/">← 返回 2026-06-15 速递</a></div>
