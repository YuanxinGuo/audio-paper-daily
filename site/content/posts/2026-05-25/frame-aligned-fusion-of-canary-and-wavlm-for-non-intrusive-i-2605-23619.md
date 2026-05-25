---
title: "Frame-Aligned Fusion of Canary and WavLM for Non-Intrusive Intelligibility Prediction of Hearing-Aid-Processed Speech"
date: 2026-05-25T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#语音可懂度预测"]
summary: "提出帧对齐融合策略，结合Canary和WavLM编码器，在无参考条件下预测助听器处理语音的可懂度，在Clarity挑战中取得最优结果。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero">
<div class="hero-score">
<div class="score-num">7.5</div>
<div class="score-stars">★★★★☆</div>
<div class="score-tier">前25%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#语音可懂度预测</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#非侵入式预测</span> <span class="tag-pill tag-pill-soft">#助听器处理语音</span> <span class="tag-pill tag-pill-soft">#特征融合</span> <span class="tag-pill tag-pill-soft">#自监督模型</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2605.23619</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-05-25</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2605.23619" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2605.23619" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出帧对齐融合策略，结合Canary和WavLM编码器，在无参考条件下预测助听器处理语音的可懂度，在Clarity挑战中取得最优结果。
</div>

## 👥 作者与机构

**Kazushi Nakazawa** ¹

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合语音可懂度评估、助听器算法研究者。重点读§3融合策略对比和§4.2消融实验。可复现其帧对齐融合思路用于其他双编码器任务。

## 🌍 研究背景

非侵入式语音可懂度预测旨在无需干净参考的情况下，估计听障患者对助听器处理语音的理解程度。现有方法多使用单一预训练模型（如WavLM）提取特征，但不同编码器（如Canary）可能提供互补信息。如何有效融合多编码器特征是一个开放问题。本文系统研究了不同融合策略（均匀平均、池后融合、交叉注意力、帧对齐融合等）的效果，并探索了融合发生的时序位置对性能的影响。

## 💡 核心创新

1. 提出帧对齐融合（Frame-Aligned Fusion），在粗时间尺度上对齐WavLM与Canary特征
2. 使用可学习步长卷积对WavLM进行时间准备，匹配Canary时间线
3. 系统比较了6种融合策略，揭示粗粒度局部时序对齐作为有效归纳偏置
4. 在统一双耳框架下保持左右声道信息，提升预测准确性

## 🏗️ 模型架构

输入为双耳助听器处理语音，分别送入两个冻结的预训练编码器：Canary（输出帧率50Hz）和WavLM（输出帧率50Hz但特征维度更高）。WavLM特征先通过可学习步长卷积进行时间下采样，使其帧率与Canary对齐。然后在对齐后的时间点上进行逐帧融合（拼接或相加），再经过池化层得到全局表示，最后通过回归头预测可懂度分数。模型参数量未明确给出。

## 📚 数据集

- Clarity Prediction Challenge 3rd (CPC3) 训练集（用于训练）
- CPC3 开发集（用于验证）
- CPC3 评估集（用于测试）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| RMSE | CPC3 Eval | 单编码器Canary基线 26.10 | **帧对齐融合 24.96** | -1.14 |
| Corr | CPC3 Eval | 单编码器Canary基线 0.780 | **帧对齐融合 0.796** | +0.016 |

帧对齐融合在CPC3评估集上取得RMSE 24.96±0.06、Corr 0.796±0.001，优于单编码器基线（Canary: 26.10/0.780, WavLM: 26.30/0.775）和均匀平均融合（25.50/0.788）。消融实验表明，帧对齐融合优于池后融合和交叉注意力。严重程度、增强系统、层窗口和时间偏移分析进一步验证了粗粒度局部时序对齐的有效性。

## 🎯 结论与影响

本文证明，在非侵入式可懂度预测中，将互补的预训练编码器在粗时间尺度上进行帧对齐融合，比后期融合或均匀平均更有效。这一发现为多编码器融合提供了新的设计原则，有望推广到其他语音评估任务。对助听器算法开发而言，该方法可提供更准确的客观评估，减少主观测试成本。

## ⚠️ 局限与未解决问题

仅使用两个特定编码器（Canary和WavLM），未探索其他组合；融合策略仅在CPC3数据集上验证，泛化性未知；未报告推理延迟或计算开销；未与侵入式方法（如STOI）对比；未分析听障患者听力图的影响。

---

<div class="paper-footer"><span>评分：7.5</span><span>原始：7.5</span><a href="/audio-paper-daily/posts/2026-05-25/">← 返回 2026-05-25 速递</a></div>
