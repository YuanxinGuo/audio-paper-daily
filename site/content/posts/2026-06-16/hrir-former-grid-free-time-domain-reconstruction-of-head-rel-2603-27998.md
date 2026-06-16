---
title: "HRIR-Former: Grid-Free Time-Domain Reconstruction of Head-Related Impulse Responses with a Spatially Encoded Transformer"
date: 2026-06-16T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#双耳音频"]
summary: "提出HRIR-Former，一种基于Transformer的时域无网格方法，从稀疏测量重建任意方向HRIR，提升时间保真度和空间连续性。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero hero-focus">
<div class="hero-score">
<div class="score-num">9.2</div>
<div class="score-stars">★★★★★</div>
<div class="score-tier">前25%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#双耳音频</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#HRIR重建</span> <span class="tag-pill tag-pill-soft">#空间上采样</span> <span class="tag-pill tag-pill-soft">#Transformer</span> <span class="tag-pill tag-pill-soft">#时域方法</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2603.27998</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-06-16</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
<div class="meta-row"><span class="meta-key">⭐</span><span class="meta-val focus-badge">本站重点关注领域 · 评分 +1</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2603.27998" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2603.27998" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出HRIR-Former，一种基于Transformer的时域无网格方法，从稀疏测量重建任意方向HRIR，提升时间保真度和空间连续性。
</div>

## 👥 作者与机构

**Shaoheng Xu** ¹ · Chunyi Sun · Jihui Zhang · Amy Bastine · Prasanga N. Samarasinghe · Thushara D. Abhayapala · Hongdong Li

**机构**：澳大利亚国立大学

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合双耳音频、空间音频处理方向的研究者。建议重点阅读第3节方法部分（空间编码和Conv1D细化模块）以及第4节实验部分（表1和消融实验）。可先看§3.2与表1。

## 🌍 研究背景

个性化头相关冲激响应（HRIR）是实现双耳渲染的关键，但密集测量成本高。现有方法多在频域处理，依赖最小相位假设或分离时序模型，且使用固定方向网格，导致时间保真度和空间连续性下降。本文旨在从稀疏测量中预测任意方向的HRIR，提出一种时域无网格方法。

## 💡 核心创新

1. 正弦空间特征编码任意方向
2. Conv1D细化模块提升时域精度
3. 辅助ITD/ILD预测头
4. 无需最小相位预处理
5. 无网格时域Transformer架构

## 🏗️ 模型架构

输入为稀疏测量的HRIR序列及对应方向，通过正弦空间特征编码将方向嵌入，与HRIR特征拼接后送入Transformer编码器。编码器输出经Conv1D细化模块处理，最终预测目标方向的HRIR。同时，模型包含辅助ITD和ILD预测头。整体为时域端到端架构，无频域变换或最小相位假设。

## 📚 数据集

- SONICOM（训练/评估，包含多个受试者的HRIR测量）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| NMSE | SONICOM | 未明确给出具体值 | **优于基线** | 未明确 |
| 余弦距离 | SONICOM | 未明确 | **优于基线** | 未明确 |
| ITD误差 | SONICOM | 未明确 | **优于基线** | 未明确 |
| ILD误差 | SONICOM | 未明确 | **优于基线** | 未明确 |

在SONICOM数据集上，HRIR-Former在NMSE、余弦距离、ITD和ILD误差上均优于先前方法。消融实验验证了各模块的有效性，并表明最小相位预处理并非必要。具体数值未在摘要中给出。

## 🎯 结论与影响

HRIR-Former通过时域无网格Transformer实现了从稀疏测量到任意方向HRIR的高质量重建，避免了频域和最小相位假设的局限。该方法为个性化双耳渲染提供了更灵活高效的方案，有望推动空间音频在VR/AR等领域的应用。

## ⚠️ 局限与未解决问题

摘要未提及推理速度或模型参数量，可能影响实时应用。仅在一个数据集（SONICOM）上评估，泛化性待验证。未与更多基线方法（如基于GAN或扩散模型）对比。

---

<div class="paper-footer"><span>评分：9.2</span><span>原始：8.2</span><span>+1 重点领域加权</span><a href="/audio-paper-daily/posts/2026-06-16/">← 返回 2026-06-16 速递</a></div>
