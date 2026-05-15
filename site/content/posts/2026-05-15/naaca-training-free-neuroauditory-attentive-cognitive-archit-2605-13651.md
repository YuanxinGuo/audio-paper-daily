---
title: "NAACA: Training-Free NeuroAuditory Attentive Cognitive Architecture with Oscillatory Working Memory for Salience-Driven Attention Gating"
date: 2026-05-15T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#听觉注意力", "#工作记忆", "#无训练", "#语音事件检测", "#音频语言模型"]
summary: "提出一种无需训练的神经听觉注意力认知架构NAACA，通过振荡工作记忆模型实现基于显著性的注意力门控，显著提升音频语言模型在长时录音中的事件检测精度。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#语音事件检测</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#听觉注意力</span> <span class="tag-pill tag-pill-soft">#工作记忆</span> <span class="tag-pill tag-pill-soft">#音频语言模型</span> <span class="tag-pill tag-pill-soft">#无训练</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2605.13651</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-05-15</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2605.13651" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2605.13651" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出一种无需训练的神经听觉注意力认知架构NAACA，通过振荡工作记忆模型实现基于显著性的注意力门控，显著提升音频语言模型在长时录音中的事件检测精度。
</div>

## 👥 作者与机构

**Zhongju Yuan** ¹ · Geraint Wiggins · Dick Botteldooren

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合从事音频事件检测、听觉注意力建模的研究者阅读。建议重点阅读§3的OWM模型设计和§4.1的XD-Violence实验结果，可先看图2的架构概览。

## 🌍 研究背景

当前音频语言模型在处理长时录音时存在注意力瓶颈，背景噪声会稀释罕见但重要的事件。现有方法多依赖端到端训练或复杂注意力机制，计算开销大且泛化性有限。本文受神经科学启发，将注意力分配重构为听觉显著性过滤问题，旨在无需额外训练的情况下提升ALM对显著事件的响应能力。

## 💡 核心创新

1. 提出训练免费的NAACA架构，无需微调ALM
2. 设计振荡工作记忆模型OWM，模拟吸引子状态
3. 利用能量波动触发高层认知处理，实现门控机制

## 🏗️ 模型架构

输入音频特征 → OWM模块（振荡工作记忆，维持稳定吸引子状态并检测能量波动）→ 当能量超过阈值时触发ALM（如AudioQwen）进行高层推理 → 输出事件标签。OWM核心是耦合振荡器网络，通过自适应能量阈值判断显著性，无需训练参数。

## 📚 数据集

- XD-Violence（评估，长时暴力事件检测）
- Urban Soundscapes of the World (USoW)（定性案例研究）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| 平均精度 (AP) | XD-Violence | AudioQwen 53.50% | **NAACA+AudioQwen 70.60%** | +17.10% |

在XD-Violence上，NAACA将AudioQwen的平均精度从53.50%提升至70.60%，同时减少了不必要的ALM调用。在USoW数据集上的定性案例显示，OWM能捕获新事件和子类别转换，对短暂停顿和环境噪声具有鲁棒性。

## 🎯 结论与影响

NAACA通过神经启发的振荡工作记忆模型，无需训练即可显著提升ALM在长时音频中的显著性事件检测能力，为听觉注意力建模提供了新范式。未来可探索将OWM集成到更多ALM架构中，并应用于实时音频监控系统。

## ⚠️ 局限与未解决问题

仅在两个数据集上验证，缺乏大规模基准测试；未报告计算效率指标（如推理延迟、内存占用）；OWM的阈值设定可能依赖经验，缺乏自适应机制；未与其它无训练方法（如基于能量的检测器）对比。

---

<div class="paper-footer"><span>评分：8.5</span><span>原始：8.5</span><a href="/audio-paper-daily/posts/2026-05-15/">← 返回 2026-05-15 速递</a></div>
