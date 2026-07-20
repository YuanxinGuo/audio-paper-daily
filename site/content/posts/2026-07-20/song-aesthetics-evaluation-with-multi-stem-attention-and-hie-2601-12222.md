---
title: "Song Aesthetics Evaluation with Multi-Stem Attention and Hierarchical Uncertainty Modeling"
date: 2026-07-20T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#音乐质量评估"]
summary: "提出多轨注意力融合与分层粒度感知区间聚合的歌曲美学评估框架，在AI生成和人工创作歌曲数据集上优于现有模型。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#音乐质量评估</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#音乐美学评估</span> <span class="tag-pill tag-pill-soft">#多轨注意力融合</span> <span class="tag-pill tag-pill-soft">#分层不确定性建模</span> <span class="tag-pill tag-pill-soft">#音乐生成</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2601.12222</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-07-20</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner"><div class="oc-headline"><span class="oc-pulse"></span><span class="oc-title">本论文已开源</span><span class="oc-hint">点击下方卡片直达对应资源</span></div><div class="oc-grid"><a class="oc-chip oc-chip-code" href="https://github.com/yisan33/song-aesthetics-evaluation" target="_blank" rel="noopener"><span class="oc-icon">💻</span><span class="oc-text"><span class="oc-label">代码仓库</span><span class="oc-sub">yisan33/song-aesthetics-evaluation</span></span></a></div></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2601.12222" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2601.12222" target="_blank" rel="noopener">📑 PDF</a><a class="rsrc rsrc-code" href="https://github.com/yisan33/song-aesthetics-evaluation" target="_blank" rel="noopener">💻 代码</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出多轨注意力融合与分层粒度感知区间聚合的歌曲美学评估框架，在AI生成和人工创作歌曲数据集上优于现有模型。
</div>

## 👥 作者与机构

**Yishan Lv** ¹ · Jing Luo · Boyuan Ju · Yang Zhang · Xinda Wu · Bo Yuan · Xinyu Yang

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合音乐信息检索、音频质量评估方向的研究者。建议重点阅读第3节MSAF和HiGIA模块设计，以及第4节实验对比。可先看表1和表2了解性能提升。

## 🌍 研究背景

音乐生成AI快速发展，大量音乐内容涌现，亟需自动化的歌曲美学评估方法。现有研究多聚焦于语音、音频或演唱质量，对歌曲整体美学评估关注不足。传统方法直接预测精确的MOS值，难以捕捉人类感知的细微差别。本文旨在提出一个面向歌曲的美学评估框架，通过多轨注意力融合和分层不确定性建模来提升评估性能。

## 💡 核心创新

1. 提出Multi-Stem Attention Fusion (MSAF)模块，实现混合-人声与混合-伴奏的双向交叉注意力融合
2. 提出Hierarchical Granularity-Aware Interval Aggregation (HiGIA)模块，学习多粒度分数概率分布并聚合为区间
3. 在区间内进行回归预测最终分数，替代直接MOS预测
4. 在AI生成和人工创作两个歌曲数据集上验证有效性

## 🏗️ 模型架构

输入为歌曲的混合音频、人声和伴奏（通过分离模型获取）。主干网络：混合、人声、伴奏分别通过预训练音频编码器提取特征。关键模块：1) MSAF：混合-人声与混合-伴奏对之间构建双向交叉注意力，融合多轨特征；2) HiGIA：学习多粒度分数概率分布，聚合为分数区间，再通过区间内回归输出最终MOS。输出为多维美学评分。

## 📚 数据集

- SongEval数据集（AI生成歌曲，评估）
- 内部美学数据集（人工创作歌曲，评估）

## 📊 实验结果

摘要未给出具体数值，仅说明在SongEval和内部数据集上，所提方法在多维歌曲美学评估中优于两个SOTA模型。具体指标和提升幅度需查阅全文。

## 🎯 结论与影响

本文提出的多轨注意力融合与分层不确定性建模框架有效提升了歌曲美学评估性能，为音乐质量评估提供了新思路。后续研究可探索更细粒度的多轨交互和不确定性建模方法，对音乐生成内容的质量控制具有潜在应用价值。

## ⚠️ 局限与未解决问题

摘要未提及模型参数量、推理速度等效率指标；仅与两个SOTA对比，baseline数量有限；未进行消融实验验证各模块贡献；数据集规模未说明，可能影响泛化性。

## 🔗 开源资源

- **代码**：<https://github.com/yisan33/song-aesthetics-evaluation>

---

<div class="paper-footer"><span>评分：7.2</span><span>原始：7.2</span><a href="/audio-paper-daily/posts/2026-07-20/">← 返回 2026-07-20 速递</a></div>
