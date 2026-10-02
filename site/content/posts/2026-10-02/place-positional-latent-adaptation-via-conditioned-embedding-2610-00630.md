---
title: "PLACE: Positional Latent Adaptation via Conditioned Embeddings for Binaural Audio Generation"
date: 2026-10-02T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#双耳音频"]
summary: "PLACE 在预训练 AudioX 上加入感知编码器特征与条件低秩适配，用 ILD/ITD 监督生成双耳音频。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero hero-focus">
<div class="hero-score">
<div class="score-num">8.0</div>
<div class="score-stars">★★★★☆</div>
<div class="score-tier">前25%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#双耳音频</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#双耳音频</span> <span class="tag-pill tag-pill-soft">#音频生成</span> <span class="tag-pill tag-pill-soft">#多模态</span> <span class="tag-pill tag-pill-soft">#空间音频</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2610.00630</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-10-02</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
<div class="meta-row"><span class="meta-key">⭐</span><span class="meta-val focus-badge">本站重点关注领域 · 评分 +1</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2610.00630" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2610.00630" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>PLACE 在预训练 AudioX 上加入感知编码器特征与条件低秩适配，用 ILD/ITD 监督生成双耳音频。
</div>

## 👥 作者与机构

**Tiernon Riesenmy** ¹ · You Zhang · Gautam Bhattacharya · Andrea Fanelli

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合做双耳/空间音频生成与多模态音频生成的研究者阅读。建议通读，重点看条件低秩变换的设计与 ILD/ITD 监督部分，以及 FAIR-Play 与 BEWO-1M 上的对比表；若只关心空间一致性，可先看消融与听感评测小节。

## 🌍 研究背景

双耳音频生成此前多依赖单模态视频条件，ViSAGe 等方法在空间线索建模上有限，SpatialSonic 在 SpatialCLAP 上表现较强但泛化受限。现有方法普遍缺少对文本与视频空间语义的对齐，也少有直接以双耳空间线索（ILD/ITD）监督生成潜变量的做法。本文要解决的是：在任意文本/视频/音频提示组合下，如何让预训练 any-to-audio 模型输出空间一致的双耳音频。

## 💡 核心创新

1. 用 Perception Encoder Core 特征增强视频条件
2. 对齐文本与视频表示以导出空间线索
3. 条件依赖的低秩潜变量变换适配器
4. 以解码音频 ILD/ITD 目标监督适配器

## 🏗️ 模型架构

输入为文本、视频及可选音频提示，视频侧用 Perception Encoder Core 提取特征，文本与视频表示经对齐模块导出空间线索。主干沿用预训练 any-to-audio 模型 AudioX，在其生成潜变量上施加条件依赖的低秩变换适配器，输出双耳音频。适配器由解码后音频的耳间电平差（ILD）与耳间时间差（ITD）目标监督，实现空间一致性约束。摘要未给出参数量。

## 📚 数据集

- MRSAudio（训练）
- FAIR-Play（评估）
- BEWO-1M Single Static test split（评估）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| SpatialCLAP | BEWO-1M Single Static test split | SpatialSonic（具体值未给出） | **更高（具体值未给出）** | 提升（幅度未给出） |

在 MRSAudio 上训练后，PLACE 在 FAIR-Play 上多数指标优于 ViSAGe，并在 BEWO-1M Single Static 测试划分上取得高于 SpatialSonic 的 SpatialCLAP 分数。听感评测在视频到音频及分布外文本到音频生成上更偏好 PLACE，说明多模态控制更灵活、空间一致性更好。摘要未给出具体数值与消融细节。

## 🎯 结论与影响

最强结论是：在预训练 any-to-audio 模型上以条件低秩适配加 ILD/ITD 监督，可有效提升双耳生成的空间一致性并支持多模态控制。这为空间音频生成提供了轻量适配范式，后续可探索更强空间监督与跨数据集泛化。工业上可用于 VR/AR 与影视内容的双耳音频自动生成。

## ⚠️ 局限与未解决问题

摘要未报告推理延迟与参数量，缺少与更多双耳生成基线的定量对比，SpatialCLAP 提升幅度未给出，ILD/ITD 监督的消融与失败案例分析缺失，MRSAudio 训练集偏置可能影响泛化。

---

<div class="paper-footer"><span>评分：8.0</span><span>原始：7.0</span><span>+1 重点领域加权</span><a href="/audio-paper-daily/posts/2026-10-02/">← 返回 2026-10-02 速递</a></div>
