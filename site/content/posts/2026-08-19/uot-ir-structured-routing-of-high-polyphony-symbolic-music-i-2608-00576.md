---
title: "UOT-IR: Structured Routing of High-Polyphony Symbolic Music into Fixed-Budget Representations"
date: 2026-08-19T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#符号音乐压缩"]
summary: "提出基于约束非平衡最优传输的UOT-IR框架，将高复调符号音乐压缩为固定预算表示，在SymphonyNet上取得最优性能。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#符号音乐压缩</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#最优传输</span> <span class="tag-pill tag-pill-soft">#符号音乐</span> <span class="tag-pill tag-pill-soft">#结构化路由</span> <span class="tag-pill tag-pill-soft">#无训练</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2608.00576</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-08-19</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2608.00576" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2608.00576" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出基于约束非平衡最优传输的UOT-IR框架，将高复调符号音乐压缩为固定预算表示，在SymphonyNet上取得最优性能。
</div>

## 👥 作者与机构

**Ziyue Kang** ¹ · Nan Nan · Chenhao Lin · Xiaohong Guan

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合从事符号音乐处理、音乐信息检索或最优传输应用的研究者阅读。建议重点阅读第3节方法部分和第4节实验对比，可先看§3.2的边际松弛和§4.2的模板标准化结果。

## 🌍 研究背景

高复调符号音乐在生成、分析和编曲中应用广泛，但许多下游任务需要固定轨道或槽位的紧凑表示。现有方法依赖启发式简化或通用表示空间降维，难以在严格预算下保持结构角色、配器兼容性和可演奏性。本文将该压缩问题形式化为固定预算的结构化路由问题，并引入非平衡最优传输理论，旨在生成紧凑且音乐连贯的表示。

## 💡 核心创新

1. 提出UOT-IR框架，将压缩问题建模为固定预算结构化路由
2. 结合配器先验、自适应边际松弛、时间解码和可演奏性投影
3. 支持模板标准化和自适应保留两种设置，无需训练
4. 在SymphonyNet上取得最优Note-F1和最低结构代价

## 🏗️ 模型架构

UOT-IR基于约束非平衡最优传输，输入为高复调符号音乐序列，通过配器先验构建代价矩阵，利用自适应边际松弛处理预算约束，时间解码模块将传输计划映射为紧凑表示，最后通过可演奏性投影确保输出符合音乐规则。整体为无训练框架，直接优化传输计划。

## 📚 数据集

- SymphonyNet（评估，包含交响乐符号音乐）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| Note-F1 | SymphonyNet | 未明确 | **0.9120** | 最佳 |
| 结构代价 | SymphonyNet | 未明确 | **14.7165** | 最低 |
| 坏结构混淆率 | SymphonyNet | 未明确 | **0.3406** | 最低 |

实验在SymphonyNet语料上进行，UOT-IR在自适应保留设置下取得最佳Note-F1（0.9120），在模板标准化设置下取得最低结构代价（14.7165）和最低坏结构混淆率（0.3406）。结果表明UOT-IR在两种设置下均优于现有方法，验证了其有效性和通用性。

## 🎯 结论与影响

UOT-IR为固定预算符号音乐压缩提供了原则性范式，通过非平衡最优传输实现了紧凑、结构化且音乐连贯的表示。该方法无需训练，可直接应用于现有工作流，有望推动符号音乐压缩和生成领域的发展，并为工业界提供实用工具。

## ⚠️ 局限与未解决问题

摘要未提及计算复杂度或推理时间，作为无训练方法可能在大规模数据上存在效率问题。实验仅在SymphonyNet单一语料上评估，缺乏跨数据集泛化验证。未与基于学习的压缩方法进行对比，基线信息不完整。

---

<div class="paper-footer"><span>评分：7.2</span><span>原始：7.2</span><a href="/audio-paper-daily/posts/2026-08-19/">← 返回 2026-08-19 速递</a></div>
