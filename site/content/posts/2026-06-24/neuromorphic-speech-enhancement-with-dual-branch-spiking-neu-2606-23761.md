---
title: "Neuromorphic Speech Enhancement with Dual-Branch Spiking Neural Networks"
date: 2026-06-24T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#语音增强"]
summary: "提出双分支脉冲神经网络GSU-DBNet，通过门控脉冲单元联合建模幅度和复数谱，以极低参数量实现优于现有SNN方法的语音增强性能。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#语音增强</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#脉冲神经网络</span> <span class="tag-pill tag-pill-soft">#双分支架构</span> <span class="tag-pill tag-pill-soft">#门控脉冲单元</span> <span class="tag-pill tag-pill-soft">#频谱掩码</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2606.23761</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-06-24</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
<div class="meta-row"><span class="meta-key">⭐</span><span class="meta-val focus-badge">本站重点关注领域 · 评分 +1</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2606.23761" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2606.23761" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出双分支脉冲神经网络GSU-DBNet，通过门控脉冲单元联合建模幅度和复数谱，以极低参数量实现优于现有SNN方法的语音增强性能。
</div>

## 👥 作者与机构

**Taiyu Meng** ¹ · Wenbin Jiang · Haoyi Zhang · Yuhan Zhou · Haibing Yin

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合语音增强和脉冲神经网络研究者阅读。重点看§3的双分支架构和GSU模块设计，以及§4的表1、表2对比结果。可复现其开源代码验证能效优势。

## 🌍 研究背景

基于脉冲神经网络（SNN）的语音增强因能效优势成为新兴方向，但受限于二值激活和缺乏精心设计的网络架构，性能远低于传统人工神经网络（ANN）方法。现有SNN方法多采用简单堆叠或单分支结构，未能充分利用语音的幅度和相位信息。本文旨在设计一种高效的SNN架构，在保持低功耗的同时缩小与ANN方法的性能差距。

## 💡 核心创新

1. 提出双分支架构分别建模幅度谱和复数谱
2. 设计门控脉冲单元（GSU）融合时空特征
3. 双路径GSU模块同时利用时间和频率信息
4. 参数量仅394K，为ANN方法的4.5%-10.6%

## 🏗️ 模型架构

输入为带噪语音的幅度谱和复数谱，分别送入两个分支。每个分支包含多个双路径GSU模块，每个模块由时间路径和频率路径的脉冲神经元组成，通过门控机制融合。GSU模块内部采用脉冲神经元（如LIF）和门控单元，输出预测的幅度掩码和复数掩码。最终通过掩码与带噪谱相乘得到增强语音。总参数量394K。

## 📚 数据集

- DNS-Challenge（训练/评估，公开基准数据集）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| PESQ | DNS-Challenge | SNN方法（最佳）约2.70 | **3.04** | +0.34 |

在DNS-Challenge数据集上，GSU-DBNet以394K参数量取得PESQ 3.04，优于所有现有SNN方法，且参数量仅为代表性ANN模型（如CRN、DPCRN）的4.5%-10.6%。未提供SI-SDR等其他指标，也未报告推理能耗或延迟。

## 🎯 结论与影响

本文提出的GSU-DBNet证明了脉冲神经网络在语音增强任务上的潜力，通过双分支架构和门控脉冲单元有效提升了性能，同时保持极低参数量。该工作为低功耗语音增强设备提供了可行方案，有望推动SNN在音频领域的实际应用。

## ⚠️ 局限与未解决问题

仅在一个数据集上评估，缺乏跨数据集泛化验证；未报告SI-SDR、STOI等常用指标；未提供实际功耗或推理延迟测量；与ANN方法的对比不够全面（仅比较参数量，未对比性能上限）；消融实验未详细分析各组件贡献。

---

<div class="paper-footer"><span>评分：8.8</span><span>原始：7.8</span><span>+1 重点领域加权</span><a href="/audio-paper-daily/posts/2026-06-24/">← 返回 2026-06-24 速递</a></div>
