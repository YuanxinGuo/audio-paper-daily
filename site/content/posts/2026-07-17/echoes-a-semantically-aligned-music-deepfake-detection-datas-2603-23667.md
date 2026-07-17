---
title: "Echoes: A semantically-aligned music deepfake detection dataset"
date: 2026-07-17T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#音频深度伪造检测"]
summary: "提出Echoes数据集，通过语义对齐和生成器多样性提升音乐深度伪造检测的泛化性。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#音频深度伪造检测</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#音乐深度伪造检测</span> <span class="tag-pill tag-pill-soft">#数据集构建</span> <span class="tag-pill tag-pill-soft">#语义对齐</span> <span class="tag-pill tag-pill-soft">#泛化性</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2603.23667</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-07-17</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2603.23667" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2603.23667" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出Echoes数据集，通过语义对齐和生成器多样性提升音乐深度伪造检测的泛化性。
</div>

## 👥 作者与机构

**Octavian Pascu** ¹ · Dan Oneata · Horia Cucu · Nicolas M. Muller

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合音频伪造检测、音乐信息检索领域的研究者阅读。建议重点看§3数据集构建方法和§4.2跨数据集评估结果，以理解语义对齐和生成器多样性的实际效果。

## 🌍 研究背景

音乐深度伪造检测面临两大挑战：现有数据集生成器单一、缺乏语义对齐，导致模型学习到捷径（如音频质量差异）而非真正的伪造特征。此前SOTA方法使用Wav2Vec2等预训练模型，但在跨数据集场景下泛化性差。本文旨在构建一个更具挑战性、能促进鲁棒泛化的数据集。

## 💡 核心创新

1. 语义对齐：通过条件生成确保伪造音频与真实音频在内容上匹配
2. 生成器多样性：包含10种流行AI音乐生成系统
3. 跨数据集评估：系统对比三个现有数据集上的迁移性能

## 🏗️ 模型架构

本文不提出新模型架构，而是构建数据集。数据集包含4,468首曲目（131小时），涵盖流行、摇滚、电子等流派，由10种AI音乐生成系统生成。语义对齐通过两种方式实现：基于真实波形条件生成和基于歌曲描述条件生成。评估使用Wav2Vec2 XLS-R 2B作为特征提取器，训练线性分类器进行检测。

## 📚 数据集

- Echoes（训练/评估，4,468首，131小时）
- 现有AI生成音乐数据集（跨数据集评估，三个数据集）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| 等错误率 (EER) | Echoes (in-domain) | 现有数据集训练模型 (EER未明确给出) | **Echoes训练模型 (EER最低)** | 显著降低 |
| 泛化性能 (跨数据集EER) | 跨数据集 | 现有数据集训练模型 (泛化差) | **Echoes训练模型 (泛化最强)** | 提升显著 |

实验表明：Echoes是域内最难的数据集；现有数据集训练的模型迁移到Echoes上表现差；而在Echoes上训练的模型展现出最强的跨数据集泛化性能，说明生成器多样性和语义对齐有助于学习可迁移的检测线索。

## 🎯 结论与影响

Echoes数据集通过语义对齐和生成器多样性，有效提升了音乐深度伪造检测的泛化性，为未来研究提供了更具挑战性的基准。该工作对工业界部署鲁棒检测系统具有重要参考价值。

## ⚠️ 局限与未解决问题

数据集仅包含三种主要音乐流派，可能无法覆盖所有音乐类型；未评估对未见生成器的泛化能力；未提供模型推理效率等实际部署指标。

---

<div class="paper-footer"><span>评分：7.8</span><span>原始：7.8</span><a href="/audio-paper-daily/posts/2026-07-17/">← 返回 2026-07-17 速递</a></div>
