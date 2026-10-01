---
title: "Rate-Agnostic Bioacoustics: Heterogeneous Multi-Taxa Classification with Continuous Filterbanks and Fourier Neural Operators"
date: 2026-10-01T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#生物声学"]
summary: "提出采样率无关前端SFI配合Fourier神经算子主干，直接在原生采样率处理生物声学录音，在84类60种采样率语料上达0.906准确率。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero">
<div class="hero-score">
<div class="score-num">7.0</div>
<div class="score-stars">★★★★☆</div>
<div class="score-tier">前25%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#生物声学</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#生物声学</span> <span class="tag-pill tag-pill-soft">#采样率无关</span> <span class="tag-pill tag-pill-soft">#Fourier神经算子</span> <span class="tag-pill tag-pill-soft">#音频分类</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2609.37540</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-10-01</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2609.37540" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2609.37540" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出采样率无关前端SFI配合Fourier神经算子主干，直接在原生采样率处理生物声学录音，在84类60种采样率语料上达0.906准确率。
</div>

## 👥 作者与机构

**Stefano Ciapponi** ¹ · Francesco Ardan Dal R{\i} · Nicola Conci · Elisabetta Farella

**机构**：特伦托大学

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合做生物声学分类、多采样率音频建模的研究者与工程团队阅读。建议通读，重点看 §3 的 SFI 前端设计与 FNO 渐进时间尺度融合模块，以及表 2 中与固定采样率、语料最大采样率基线的对比；若关注部署，可先看采样率增强的消融实验。

## 🌍 研究背景

生物声学分类长期依赖固定采样率的频谱表示（如 mel 谱），遇到野外录音采样率异构时需先重采样，导致高频信息丢失或计算冗余。此前 SOTA 多为固定输入率的 CNN/Transformer 分类器，在跨采样率场景下泛化差。本文要解决的核心问题是：如何让单一模型直接在任意原生采样率上工作，并输出固定尺寸表示以支持多类群分类。

## 💡 核心创新

1. SFI 前端直接处理原生采样率，免重采样
2. FNO 主干实现跨采样率固定尺寸表示
3. 渐进时间尺度融合模块聚合多尺度特征
4. 训练期采样率增强提升未见率鲁棒性

## 🏗️ 模型架构

输入为各录音的原生采样率波形，经 Sampling-Frequency-Independent (SFI) 前端映射为与采样率无关的连续滤波器组表示；主干采用 Fourier Neural Operator (FNO)，在频域进行全局卷积以捕捉长程依赖，并叠加渐进时间尺度融合模块逐级整合不同时间分辨率特征；最终输出固定尺寸嵌入接分类头，完成 84 类多类群分类。摘要未给出参数量。

## 📚 数据集

- 多类群生物声学语料（84 类、60 种采样率，训练与评估）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| Accuracy | 多类群语料（84 类/60 采样率） | 固定采样率与语料最大采样率基线（具体值未给出） | **0.906** | 优于基线 |
| Balanced Accuracy | 多类群语料 | 固定采样率与语料最大采样率基线 | **0.921** | 优于基线 |
| Macro-F1 | 多类群语料 | 固定采样率与语料最大采样率基线 | **0.899** | 优于基线 |

摘要报告 SFI-FNO 在 84 类、60 种采样率语料上取得 0.906 准确率、0.921 平衡准确率与 0.899 Macro-F1，均优于固定采样率与语料最大采样率基线。训练期采样率增强被证实可提升对未见采样率变化的鲁棒性，但摘要未给出各基线的具体数值、消融细节与推理效率指标。

## 🎯 结论与影响

最强结论是：采样率无关前端加 FNO 主干可在异构采样率生物声学数据上稳定超越固定率基线。该思路对野外声学监测、多设备录音融合有直接价值，可能推动后续研究放弃统一重采样范式，转向原生率建模。工业落地可降低边缘设备预处理成本。

## ⚠️ 局限与未解决问题

摘要未给出基线具体数值、参数量与推理延迟，缺少与主流生物声学模型（如 BirdNET、Perch）的直接对比；84 类语料是否覆盖足够类群多样性、采样率增强的增益幅度均未量化，消融实验信息不足。

---

<div class="paper-footer"><span>评分：7.0</span><span>原始：7.0</span><a href="/audio-paper-daily/posts/2026-10-01/">← 返回 2026-10-01 速递</a></div>
