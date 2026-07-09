---
title: "DASH: Dynamic Audio-Driven Semantic Chunking for Efficient Omnimodal Token Compression"
date: 2026-07-09T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#多模态压缩"]
summary: "提出DASH，一种无需训练的音频驱动语义分块框架，通过音频语义锚点动态划分多模态序列，实现高效令牌压缩。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#多模态压缩</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#音频驱动</span> <span class="tag-pill tag-pill-soft">#语义分块</span> <span class="tag-pill tag-pill-soft">#令牌压缩</span> <span class="tag-pill tag-pill-soft">#多模态大模型</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2603.15685</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-07-09</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner"><div class="oc-headline"><span class="oc-pulse"></span><span class="oc-title">本论文已开源</span><span class="oc-hint">点击下方卡片直达对应资源</span></div><div class="oc-grid"><a class="oc-chip oc-chip-code" href="https://github.com/laychou666/DASH" target="_blank" rel="noopener"><span class="oc-icon">💻</span><span class="oc-text"><span class="oc-label">代码仓库</span><span class="oc-sub">laychou666/DASH</span></span></a></div></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2603.15685" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2603.15685" target="_blank" rel="noopener">📑 PDF</a><a class="rsrc rsrc-code" href="https://github.com/laychou666/DASH" target="_blank" rel="noopener">💻 代码</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出DASH，一种无需训练的音频驱动语义分块框架，通过音频语义锚点动态划分多模态序列，实现高效令牌压缩。
</div>

## 👥 作者与机构

**Bingzhou Li** ¹ · Tao Huang

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合研究多模态大模型推理效率、令牌压缩的读者。建议重点阅读§3方法部分，尤其是语义分块和重要性估计模块。可先看图1和表2了解整体效果。

## 🌍 研究背景

多模态大模型（OmniLLMs）同时处理音频和视觉流，导致长令牌序列推理成本高昂。现有压缩方法依赖固定窗口划分和注意力剪枝，忽略了音视频信号的片段语义结构，在激进压缩下性能脆弱。本文旨在利用音频的语义结构指导令牌压缩，实现高效且保质的推理。

## 💡 核心创新

1. 音频驱动的动态语义分块（DASH）
2. 基于余弦相似度不连续性的边界检测
3. 三信号重要性估计器融合结构、区分性和显著性
4. 软时间对齐的视频令牌分割先验

## 🏗️ 模型架构

输入为多模态令牌序列（音频+视频）。首先，音频嵌入作为语义锚点，通过余弦相似度不连续性检测边界候选，生成动态可变长度片段。这些边界作为软时间对齐先验投影到视频令牌。在每个片段内，三信号重要性估计器（结构边界线索、表征独特性、注意力显著性）决定令牌保留，保留过渡关键令牌并减少冗余区域。输出为压缩后的令牌序列。

## 📚 数据集

- AVUT（评估）
- VideoMME（评估）
- WorldSense（评估）

## 📊 实验结果

摘要未提供具体数值，但声称在AVUT、VideoMME和WorldSense上，DASH在保持竞争性或更优准确率的同时，实现了比先前方法更高的压缩比。

## 🎯 结论与影响

DASH通过音频驱动的语义分块实现了高效的多模态令牌压缩，无需训练即可提升推理效率。该方法为多模态大模型的实用化提供了新思路，有望降低部署成本。

## ⚠️ 局限与未解决问题

摘要未提及局限性。可能的问题：未报告推理延迟或吞吐量；仅在三个数据集上评估，泛化性待验证；未与更多基线（如VQ-based方法）对比；三信号重要性估计器的计算开销未分析。

## 🔗 开源资源

- **代码**：<https://github.com/laychou666/DASH>

---

<div class="paper-footer"><span>评分：7.8</span><span>原始：7.8</span><a href="/audio-paper-daily/posts/2026-07-09/">← 返回 2026-07-09 速递</a></div>
