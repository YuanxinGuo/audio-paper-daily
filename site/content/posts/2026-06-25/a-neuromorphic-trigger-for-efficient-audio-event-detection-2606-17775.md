---
title: "A Neuromorphic Trigger for Efficient Audio Event Detection"
date: 2026-06-25T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#异常声音检测"]
summary: "提出基于脉冲神经网络的神经形态触发器，作为低功耗前端选择性激活下游模型，在ASD和SED任务上实现高F1分数和42.6倍FLOPs降低。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero">
<div class="hero-score">
<div class="score-num">7.8</div>
<div class="score-stars">★★★★☆</div>
<div class="score-tier">前25%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#异常声音检测</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#脉冲神经网络</span> <span class="tag-pill tag-pill-soft">#声音事件检测</span> <span class="tag-pill tag-pill-soft">#低功耗音频处理</span> <span class="tag-pill tag-pill-soft">#神经形态计算</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2606.17775</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-06-25</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2606.17775" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2606.17775" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出基于脉冲神经网络的神经形态触发器，作为低功耗前端选择性激活下游模型，在ASD和SED任务上实现高F1分数和42.6倍FLOPs降低。
</div>

## 👥 作者与机构

**Benjamin Hatton** ¹ · Oliver Rhodes · Luca Peres

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合对低功耗音频事件检测、脉冲神经网络应用感兴趣的读者。建议重点阅读§3触发器架构和§4实验结果，特别是表1的F1分数和FLOPs对比。可先看§4.2的SED实验以了解触发器对下游模型的影响。

## 🌍 研究背景

连续音频流的实时处理对资源受限系统是挑战。传统方法持续运行高计算量模型，能耗高。神经形态计算和脉冲神经网络（SNN）因事件驱动特性有低功耗潜力，但直接用于复杂音频检测任务精度不足。本文提出将SNN作为低功耗前端触发器，选择性激活下游模型，平衡精度与效率。

## 💡 核心创新

1. 提出SNN触发器作为低功耗前端，选择性激活下游模型
2. 采用close-open滤波后处理提升触发稳定性
3. 在ASD任务上实现类无关的0.97 F1分数
4. 在SED任务上实现42.6倍FLOPs降低并改善错误率

## 🏗️ 模型架构

输入为音频特征（如MFCC或原始波形）→ 轻量全连接SNN触发器（使用LIF神经元）→ close-open滤波后处理 → 二值触发信号。触发信号控制下游模型（如Dang分类器）是否处理当前音频段。触发器参数量小，计算成本极低。

## 📚 数据集

- URBAN-SED（ASD评估，类无关版本）
- DCASE 2017 Challenge Task 2（SED评估）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| F1分数（segment-based） | URBAN-SED（ASD） | 无触发器基线（持续处理） | **0.97** | N/A |
| FLOPs降低倍数 | DCASE 2017 Task 2（SED） | 无触发器基线 | **42.6×** | N/A |
| 事件错误率（下限） | DCASE 2017 Task 2（SED） | 0.41 | **0.25** | -0.16 |

在ASD任务上，触发器在URBAN-SED数据集上达到0.97的segment-based F1分数，表明高可靠性。在SED任务上，结合Dang分类器，触发器实现42.6倍FLOPs降低，并将事件错误率下限从0.41降至0.25。实验未提供完整系统（触发器+分类器）的最终错误率，仅给出下限。

## 🎯 结论与影响

本文提出的神经形态触发器能有效降低音频事件检测的计算成本，同时保持高检测精度。SNN前端可作为通用低功耗滤波器，适用于多种音频检测任务。对工业落地有重要意义，尤其适合电池供电的IoT设备。

## ⚠️ 局限与未解决问题

实验仅评估触发器单独性能，未报告完整系统（触发器+下游模型）的最终错误率；仅使用两个数据集，泛化性待验证；未与其它低功耗前端（如轻量CNN）对比；未报告实际功耗或延迟，仅用FLOPs衡量效率。

---

<div class="paper-footer"><span>评分：7.8</span><span>原始：7.8</span><a href="/audio-paper-daily/posts/2026-06-25/">← 返回 2026-06-25 速递</a></div>
