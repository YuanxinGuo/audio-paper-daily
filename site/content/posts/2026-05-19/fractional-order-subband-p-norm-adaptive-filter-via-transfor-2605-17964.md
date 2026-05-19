---
title: "Fractional-Order Subband p-Norm Adaptive Filter via Transformation Nearest Kronecker Product Decomposition for Active Noise Control"
date: 2026-05-19T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#主动噪声控制"]
summary: "提出基于最近Kronecker积分解的分数阶子带p范数自适应滤波算法，提升α稳定噪声下主动噪声控制的鲁棒性与计算效率。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#主动噪声控制</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#自适应滤波</span> <span class="tag-pill tag-pill-soft">#分数阶</span> <span class="tag-pill tag-pill-soft">#Kronecker分解</span> <span class="tag-pill tag-pill-soft">#鲁棒性</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2605.17964</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-05-19</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2605.17964" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2605.17964" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出基于最近Kronecker积分解的分数阶子带p范数自适应滤波算法，提升α稳定噪声下主动噪声控制的鲁棒性与计算效率。
</div>

## 👥 作者与机构

**Jianhong Ye** ¹ · Haiquan Zhao · Shaohui Lv · Yang Zhou

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合主动噪声控制、自适应滤波领域的研究者。建议重点阅读§III算法推导与§IV计算复杂度分析，以及§V中不同噪声场景的仿真结果。可跳过§II基础部分。

## 🌍 研究背景

主动噪声控制(ANC)中，传统归一化子带p范数(NSPN)算法在α稳定噪声(1<α≤2)下具有鲁棒性，但在非高斯输入、α≤1的强脉冲噪声及稀疏系统辨识场景下性能显著下降。现有方法如分数阶LMS虽能处理脉冲噪声，但计算复杂度高且未充分利用子带结构。本文旨在通过分数阶随机梯度与Kronecker分解技术，提出一种低复杂度、高鲁棒性的自适应滤波算法。

## 💡 核心创新

1. 提出分数阶子带p范数(FoNSPN)算法
2. 设计基于最近Kronecker积(NKP)的分解方法
3. 提出变换NKP(TNKP)分解降低计算复杂度
4. 推导分数阶参数β的理论界
5. 开发滤波-x变体用于ANC系统

## 🏗️ 模型架构

输入信号经分析滤波器组分解为子带信号，对每个子带采用分数阶p范数误差进行自适应滤波。权重更新基于分数阶随机梯度下降，并利用NKP或TNKP分解将全带滤波器分解为多个小矩阵的Kronecker积，降低参数数量。TNKP通过变换矩阵进一步减少乘法次数。输出经综合滤波器组重构。对于ANC，引入滤波-x结构，即FxFoNSPN和TNKP-FxFoNSPN。

## 📚 数据集

- 粉红噪声（仿真输入）
- 直升机噪声（仿真输入）
- 枪声（仿真输入）
- 打桩机噪声（仿真输入）

## 📊 实验结果

摘要未提供具体数值指标，但声称在粉红、直升机、枪声、打桩机及牵引变电站噪声下，所提算法在稳态失调和乘法成本上优于传统NSPN和NKP-NSPN。在真实单通道管道ANC和仿真多通道ANC系统中验证了降噪性能。

## 🎯 结论与影响

本文提出的TNKP-FoNSPN算法在强脉冲噪声和非高斯输入下具有更低的稳态失调和计算复杂度，为ANC系统提供了一种鲁棒且高效的解决方案。该工作推动了分数阶自适应滤波在ANC中的应用，未来可扩展到非线性或时变噪声场景。

## ⚠️ 局限与未解决问题

缺乏与最新ANC算法（如FxLMS变体）的定量对比；未报告实际降噪量（如dB值）；仅验证了特定噪声类型，泛化性待考；未讨论算法收敛速度与稳定性条件。

---

<div class="paper-footer"><span>评分：6.8</span><span>原始：6.8</span><a href="/audio-paper-daily/posts/2026-05-19/">← 返回 2026-05-19 速递</a></div>
