---
title: "NAACA: Training-Free NeuroAuditory Attentive Cognitive Architecture with Oscillatory Working Memory for Salience-Driven Attention Gating"
date: 2026-05-15T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#听觉注意力", "#工作记忆", "#显著性过滤", "#语音事件检测", "#音频语言模型"]
summary: "提出一种免训练的神经听觉认知架构NAACA，通过振荡工作记忆模型实现基于显著性的注意力门控，显著提升音频语言模型在长时录音中的关键事件检测性能。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#语音事件检测</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#听觉注意力</span> <span class="tag-pill tag-pill-soft">#工作记忆</span> <span class="tag-pill tag-pill-soft">#音频语言模型</span> <span class="tag-pill tag-pill-soft">#显著性过滤</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2605.13651</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-05-15</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2605.13651" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2605.13651" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出一种免训练的神经听觉认知架构NAACA，通过振荡工作记忆模型实现基于显著性的注意力门控，显著提升音频语言模型在长时录音中的关键事件检测性能。
</div>

## 👥 作者与机构

**Zhongju Yuan** ¹ · Geraint Wiggins · Dick Botteldooren

**机构**：根特大学

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合从事音频事件检测、听觉注意力建模或音频语言模型优化的研究者。建议重点阅读§3的OWM模型设计和§4.1的XD-Violence实验结果，可先看表1对比AP提升。

## 🌍 研究背景

当前音频语言模型（ALMs）在处理长时录音时存在注意力瓶颈：主导性背景模式会稀释罕见但重要的事件。传统方法依赖端到端训练或复杂注意力机制，计算开销大且泛化性有限。本文借鉴神经科学中的工作记忆和显著性理论，提出无需训练的认知架构，旨在高效过滤背景噪声、触发高层推理。

## 💡 核心创新

1. 提出OWM振荡工作记忆模型，模拟吸引子状态维持与能量波动检测
2. 将注意力分配重构为听觉显著性过滤问题，免训练集成到现有ALM
3. 在XD-Violence上仅用ALM部分调用即实现AP从53.50%到70.60%的提升

## 🏗️ 模型架构

输入音频特征 → OWM模块（振荡工作记忆）：包含多个振荡器单元，每个单元维持稳定吸引子状态，通过自适应能量阈值检测显著性波动 → 当能量超过阈值时触发ALM（如AudioQwen）进行高层推理，否则保持低功耗状态 → 输出事件检测结果。架构无需训练，直接作为ALM的前端过滤器。

## 📚 数据集

- XD-Violence（评估，包含长时监控音频，用于异常事件检测）
- Urban Soundscapes of the World (USoW)（定性案例研究，评估城市环境声音事件检测）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| Average Precision (AP) | XD-Violence | AudioQwen 53.50% | **70.60%** | +17.10% |

在XD-Violence上，NAACA将AudioQwen的平均精度从53.50%提升至70.60%，同时减少了不必要的ALM调用。在USoW数据集上的定性案例显示，OWM能捕获新事件和子类别转换，并对短暂停顿和环境噪声具有鲁棒性。未提供消融实验或效率指标。

## 🎯 结论与影响

NAACA通过免训练的认知架构有效缓解了ALM在长时录音中的注意力瓶颈，显著提升关键事件检测精度。其神经启发设计为听觉注意力建模提供了新思路，有望降低ALM在实际部署中的计算开销，推动工业级音频监控应用。

## ⚠️ 局限与未解决问题

仅在一个数据集上报告定量结果，缺乏跨数据集泛化验证；未提供消融实验分析OWM各组件贡献；未报告推理延迟或计算效率指标；定性案例研究缺乏量化评估；未与现有显著性检测或注意力门控方法对比。

---

<div class="paper-footer"><span>评分：7.8</span><span>原始：7.8</span><a href="/audio-paper-daily/posts/2026-05-15/">← 返回 2026-05-15 速递</a></div>
