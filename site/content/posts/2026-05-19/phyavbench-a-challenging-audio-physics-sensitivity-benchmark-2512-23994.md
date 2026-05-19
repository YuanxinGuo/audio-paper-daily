---
title: "PhyAVBench: A Challenging Audio Physics-Sensitivity Benchmark for Physically Grounded Text-to-Audio-Video Generation"
date: 2026-05-19T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#音频生成评估"]
summary: "提出首个系统评估音视频生成模型音频物理合理性基准PhyAVBench，含新数据集和对比物理响应分数指标。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero">
<div class="hero-score">
<div class="score-num">8.5</div>
<div class="score-stars">★★★★☆</div>
<div class="score-tier">前25%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#音频生成评估</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#文本到音视频生成</span> <span class="tag-pill tag-pill-soft">#物理合理性</span> <span class="tag-pill tag-pill-soft">#基准测试</span> <span class="tag-pill tag-pill-soft">#对比度量</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2512.23994</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-05-19</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">🔥 强烈推荐通读</span></div>
</div>
</div>

<div class="opensource-banner"><div class="oc-headline"><span class="oc-pulse"></span><span class="oc-title">本论文已开源</span><span class="oc-hint">点击下方卡片直达对应资源</span></div><div class="oc-grid"><a class="oc-chip oc-chip-code" href="https://github.com/imxtx/PhyAVBench" target="_blank" rel="noopener"><span class="oc-icon">💻</span><span class="oc-text"><span class="oc-label">代码仓库</span><span class="oc-sub">imxtx/PhyAVBench</span></span></a></div></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2512.23994" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2512.23994" target="_blank" rel="noopener">📑 PDF</a><a class="rsrc rsrc-code" href="https://github.com/imxtx/PhyAVBench" target="_blank" rel="noopener">💻 代码</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出首个系统评估音视频生成模型音频物理合理性基准PhyAVBench，含新数据集和对比物理响应分数指标。
</div>

## 👥 作者与机构

**Tianxin Xie** ¹ · Wentao Lei · Kai Jiang · Guanjie Huang · Pengfei Zhang · Chunhui Zhang · Fengji Ma · Haoyu He · … 等 22 人

**机构**：腾讯 · 北京大学 · 香港中文大学

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合T2AV/V2A生成研究者及评估方法开发者。建议通读，重点看§3数据集构建、§4评估指标CPRS及§6实验结果。可先复现其评估流程。

## 🌍 研究背景

文本到音视频生成在电影制作、世界建模中至关重要，但现有模型常生成物理不合理的音频。先前基准主要关注音视频时间同步，忽略音频物理合理性评估。本文旨在填补这一空白，系统评估模型对音频物理现象的敏感性。

## 💡 核心创新

1. 提出PhyAVBench基准，首个系统评估音频物理合理性
2. 构建PhyAV-Sound-11K数据集，含337组配对提示和6个物理维度
3. 提出对比物理响应分数CPRS，量化生成音频与真实音频的物理一致性
4. 采用配对提示范式评估音频物理敏感性
5. 全面评估17个SOTA模型，揭示物理合理性差距

## 🏗️ 模型架构

本文为基准评估框架，非生成模型。核心组件：PhyAV-Sound-11K数据集（25.5小时，11605个视频，184参与者，337组配对提示，6个物理维度41个测试点）；评估指标CPRS（对比物理响应分数，基于配对提示的生成音频与真实音频的声学一致性）。评估对象包括17个T2AV/I2AV/V2A模型。

## 📚 数据集

- PhyAV-Sound-11K（训练/评估，25.5小时，11605个视频，184参与者）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| CPRS | PhyAV-Sound-11K | 无（基准评估） | **CPRS指标** | 揭示模型物理合理性差距 |

评估17个SOTA模型，包括商业模型，发现即使领先模型在基本音频物理现象（如材质、速度、距离等）上表现不佳，暴露了超越音视频同步的关键差距。具体数值未在摘要中给出。

## 🎯 结论与影响

本文最强结论：现有音视频生成模型在音频物理合理性上存在显著缺陷，CPRS指标有效量化了该差距。该基准将推动物理合理的音视频生成研究，为未来模型改进提供方向。工业上可用于筛选更逼真的生成模型。

## ⚠️ 局限与未解决问题

数据集仅涵盖6个物理维度，可能不全面；CPRS依赖配对提示设计，泛化性待验证；未评估模型效率或推理延迟；对比模型数量有限，未包含所有最新方法。

## 🔗 开源资源

- **代码**：<https://github.com/imxtx/PhyAVBench>

---

<div class="paper-footer"><span>评分：8.5</span><span>原始：8.5</span><a href="/audio-paper-daily/posts/2026-05-19/">← 返回 2026-05-19 速递</a></div>
