---
title: "X-AVDD: Cross-Attentive Audio-Visual Dataset Distillation"
date: 2026-10-12T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#音频处理"]
summary: "提出跨注意力音视频数据集蒸馏方法X-AVDD，解耦跨模态对齐与联合优化，显存更省、合成数据对齐更好。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero">
<div class="hero-score">
<div class="score-num">6.8</div>
<div class="score-stars">★★★☆☆</div>
<div class="score-tier">前50%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#音频处理</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#数据集蒸馏</span> <span class="tag-pill tag-pill-soft">#音视频学习</span> <span class="tag-pill tag-pill-soft">#跨模态对齐</span> <span class="tag-pill tag-pill-soft">#数据增强</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2610.13687</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-10-12</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2610.13687" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2610.13687" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出跨注意力音视频数据集蒸馏方法X-AVDD，解耦跨模态对齐与联合优化，显存更省、合成数据对齐更好。
</div>

## 👥 作者与机构

**Saumyaranjan Mohanty** ¹ · Aravind Reddy · Konda Reddy Mopuri

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合做数据集蒸馏、音视频多模态学习、数据高效训练的研究者阅读。建议重点看 §3 的跨注意力解耦设计与 §4 的 VGGSound/AVE 实验，表 2 的跨架构泛化结果值得细看。若只关心语音/音频分离主线，可略读。

## 🌍 研究背景

音视频数据集蒸馏旨在从大规模配对音视频数据中合成小数据集，同时近似保留训练效用。此前 DM、AVDD 等方法存在两大痛点：一是显存开销大，难以扩展到复杂架构与高 SPC 设置；二是合成数据常丢失强跨模态语义对应。本文针对这两点，提出显存更省且跨模态对齐更好的蒸馏框架。

## 💡 核心创新

1. 用跨注意力显式建模模态间关系
2. 解耦跨模态对齐与联合优化，降显存
3. 端到端合成成本降低约 8 倍 GPU 小时
4. 在 VGGSound/AVE 上大幅超越 AVDD

## 🏗️ 模型架构

输入为配对的音频-视觉样本，主干采用跨注意力模块在合成过程中显式捕捉音视频模态间关系。关键设计是将跨模态对齐从联合优化中解耦，避免同时优化带来的高显存占用。输出为高度对齐的合成音视频数据集，可直接用于训练下游分类器。摘要未给出具体参数量，但强调可扩展到 AudioCLIP 等复杂架构。

## 📚 数据集

- VGGSound（训练与评估，短 YouTube 音视频片段）
- AVE（评估，音视频事件数据集）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| top-1 准确率 | VGGSound (SPC=10) | AVDD 8.2% | **24.0%** | +15.8% |
| top-1 准确率 | VGGSound (SPC=20) | AVDD 9.8% | **26.5%** | +16.7% |
| top-1 准确率（ViT 目标） | AVE (SPC=50) | AVDD 25.5% | **35.3%** | +9.8% |
| top-1 准确率（AudioCLIP） | VGGSound（5.65% 数据） | 全量数据 72.4% | **62.3%** | 接近全量，训练时间低 9 倍 |

在 VGGSound 上 SPC=10/20 时 top-1 从 8.2%/9.8% 提升到 24.0%/26.5%；AVE 上 SPC=50 跨架构泛化从 25.5% 提升到 35.3%。扩展到 AudioCLIP 时仅用 5.65% 数据达 62.3%，接近全量 72.4%，训练时间低 9 倍。摘要未给消融细节。

## 🎯 结论与影响

最强结论是解耦跨模态对齐可同时提升蒸馏效率与合成数据质量。该思路可能推动音视频数据集蒸馏向更复杂架构扩展，对数据受限场景的工业训练有降本意义。

## ⚠️ 局限与未解决问题

摘要未提供消融实验、推理延迟与显存具体数值，也未说明跨模态对齐解耦是否引入额外超参。评估集中在分类任务，未验证下游检索或生成任务。

---

<div class="paper-footer"><span>评分：6.8</span><span>原始：6.8</span><a href="/audio-paper-daily/posts/2026-10-12/">← 返回 2026-10-12 速递</a></div>
