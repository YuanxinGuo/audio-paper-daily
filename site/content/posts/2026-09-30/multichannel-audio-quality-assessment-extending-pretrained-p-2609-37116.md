---
title: "Multichannel Audio Quality Assessment: Extending Pretrained Perceptual Models to Spatial Audio"
date: 2026-09-30T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#音频质量评估"]
summary: "将预训练感知质量模型扩展到5.1声道空间音频，提出特征级Feature-Band Group Attention融合空间组，在五个测试集上取得最佳整体性能。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero hero-focus">
<div class="hero-score">
<div class="score-num">7.8</div>
<div class="score-stars">★★★★☆</div>
<div class="score-tier">前50%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#音频质量评估</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#双耳音频</span> <span class="tag-pill tag-pill-soft">#空间音频</span> <span class="tag-pill tag-pill-soft">#预训练模型迁移</span> <span class="tag-pill tag-pill-soft">#注意力机制</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2609.37116</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-09-30</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
<div class="meta-row"><span class="meta-key">⭐</span><span class="meta-val focus-badge">本站重点关注领域 · 评分 +1</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2609.37116" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2609.37116" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>将预训练感知质量模型扩展到5.1声道空间音频，提出特征级Feature-Band Group Attention融合空间组，在五个测试集上取得最佳整体性能。
</div>

## 👥 作者与机构

**Gouthaman KV** ¹ · Shiv Gehlot · Vishnu Raj · Lars Villemoes · Arijit Biswas

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合做音频质量评估、空间音频感知建模的研究者与工程团队阅读。建议重点看 §3 中四种多通道集成层级（signal/prediction/latent/feature）的定义与对比，以及 FGAtt 模块的结构图与消融实验。若只关心结论，可先看表 2 与五个 5.1 测试集的整体对比。

## 🌍 研究背景

空间音频的感知质量同时取决于信号保真度与通道间空间关系，主观评测成本高。现有感知质量模型（如基于 PESQ/PEAQ 或预训练嵌入的 MOS 预测器）多针对单声道或固定少量通道训练，无法直接迁移到 5.1 等高通道数配置。本文要回答的核心问题是：如何有效复用预训练感知知识来做多通道空间音频质量评估。

## 💡 核心创新

1. 系统比较 signal/prediction/latent/feature 四种多通道集成层级
2. 提出 latent 级空间组表示聚合方法
3. 提出 Feature-Band Group Attention (FGAtt) 在特征级自适应融合空间组

## 🏗️ 模型架构

输入为 5.1 声道音频，先按空间分组（如前后/左右）组织通道。主干复用预训练感知模型提取特征，在四种层级之一进行多通道集成：信号级直接拼接、预测级对各通道预测做聚合、latent 级对空间组表示做聚合、特征级用 FGAtt 在感知处理前自适应融合空间组。FGAtt 在特征-频带维度上做组注意力，输出最终质量分数。摘要未给出参数量。

## 📚 数据集

- 五个 5.1 声道测试集（评估，具体名称摘要未给出）

## 📊 实验结果

摘要仅说明在五个 5.1 声道测试集上 FGAtt 取得最强整体性能，未给出具体指标数值、基线名称或提升幅度，因此无法列出定量对比。作者结论是特征级自适应比信号级、预测级、latent 级集成更有效。

## 🎯 结论与影响

最强结论是特征级自适应融合（FGAtt）是复用预训练感知知识做多通道空间音频质量评估的最有效方式。这为空间音频质量评估提供了可复用的迁移范式，后续可探索更高通道数（如 7.1.4、Ambisonics）与更细粒度空间分组。工业上可用于空间音频编解码与渲染链路的自动化质量监控。

## ⚠️ 局限与未解决问题

摘要未给出具体指标数值与基线对比，难以判断提升幅度；仅验证 5.1 配置，未覆盖 Ambisonics 或对象音频；未报告推理延迟与参数量；四种集成层级的消融细节与统计显著性未知；测试集来源与主观 MOS 标注可靠性未说明。

---

<div class="paper-footer"><span>评分：7.8</span><span>原始：6.8</span><span>+1 重点领域加权</span><a href="/audio-paper-daily/posts/2026-09-30/">← 返回 2026-09-30 速递</a></div>
