---
title: "HRTF Upsampling Across Varying Measurement Configurations with Geometry-Aware Query-Conditioned Aggregation"
date: 2026-09-23T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#双耳音频"]
summary: "提出GeoAtt，用单一模型对多种稀疏测量配置做HRTF上采样，几何感知查询条件聚合加Conformer频域建模，在SONICOM上取得最低LSD。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#双耳音频</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#HRTF上采样</span> <span class="tag-pill tag-pill-soft">#空间音频</span> <span class="tag-pill tag-pill-soft">#Conformer</span> <span class="tag-pill tag-pill-soft">#个性化头相关传递函数</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2609.25995</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-09-23</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
<div class="meta-row"><span class="meta-key">⭐</span><span class="meta-val focus-badge">本站重点关注领域 · 评分 +1</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2609.25995" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2609.25995" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出GeoAtt，用单一模型对多种稀疏测量配置做HRTF上采样，几何感知查询条件聚合加Conformer频域建模，在SONICOM上取得最低LSD。
</div>

## 👥 作者与机构

**Xingyu Chen** ¹ · Hanwen Bi · Sipei Zhao · Fei Ma · Eva Cheng · Ian S. Burnett

**机构**：皇家墨尔本理工大学

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合做空间音频、个性化HRTF、双耳渲染的研究者与工程团队阅读。建议通读，重点看 §3 的几何感知查询条件聚合与 cross-attention 加性 bias 设计，以及表 2 中四种 LAP 配置的跨配置泛化结果。若关注落地，可先看泛化到未见配置的实验与推理开销。

## 🌍 研究背景

个性化 HRTF 对空间音频渲染至关重要，但逐人密集测量成本高。HRTF 上采样从稀疏测量估计密集 HRTF 以降低负担。近期学习方法（如基于 CNN/MLP 的稀疏到密集映射）性能可观，但多数绑定于预定义的测量配置，换配置需重训，泛化差。本文要解决的是：用单一模型适配不同测量配置，并泛化到训练中未见的配置。

## 💡 核心创新

1. 几何感知、查询条件的空间聚合，逐频点独立处理可用测量
2. 目标与测量方向的相对几何作为 cross-attention 加性 bias
3. Conformer 块做频域建模，单模型跨多种测量配置

## 🏗️ 模型架构

输入为稀疏测量的 HRTF 幅度谱及其对应方向。GeoAtt 在每个频点上独立进行几何感知、查询条件的空间聚合：以目标方向为 query，对可用测量方向做 cross-attention，相对几何（角度差）作为加性 bias 注入注意力。聚合后的频点表示再送入 Conformer 块做频域建模，捕捉频间依赖，最终输出密集 HRTF 幅度谱。摘要未给出参数量。

## 📚 数据集

- SONICOM 数据集（训练与评估，含多种 LAP 测量配置）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| log-spectral distortion (LSD) | SONICOM（四种 LAP 配置） | 现有学习式 HRTF 上采样方法（摘要未给具体数值） | **最低 LSD（摘要未给具体数值）** | 取得最低 LSD |

摘要称在 SONICOM 上，单一训练模型在全部四种标准 LAP 挑战测量配置下取得最低 log-spectral distortion，并能泛化到训练中未显式包含的配置。摘要未给出具体数值、消融或效率指标，无法量化提升幅度。

## 🎯 结论与影响

最强结论是单一模型可跨多种测量配置完成 HRTF 上采样并泛化到未见配置，降低个性化测量负担。对后续研究的潜在影响是推动配置无关、几何条件化的 HRTF 建模范式。工业上可减少个性化空间音频的测量与重训成本，利于规模化部署。

## ⚠️ 局限与未解决问题

摘要未给具体 LSD 数值、消融与推理延迟，难以判断几何 bias 与 Conformer 各自的贡献。仅在 SONICOM 上验证，跨数据集泛化未知。未讨论相位/时域重建与实时性，对实际渲染的适用性待验证。

---

<div class="paper-footer"><span>评分：8.8</span><span>原始：7.8</span><span>+1 重点领域加权</span><a href="/audio-paper-daily/posts/2026-09-23/">← 返回 2026-09-23 速递</a></div>
