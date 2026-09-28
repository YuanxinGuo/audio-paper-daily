---
title: "Coupled Meta-Adaptive Filtering for Active Noise Control Under Time-Varying Acoustic Paths"
date: 2026-09-28T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#语音增强"]
summary: "提出耦合元自适应滤波ANC方法，联合学习控制滤波器与声路径跟踪，在时变声路径下提升降噪与稳定性。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero hero-focus">
<div class="hero-score">
<div class="score-num">8.3</div>
<div class="score-stars">★★★★☆</div>
<div class="score-tier">前25%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#语音增强</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#主动噪声控制</span> <span class="tag-pill tag-pill-soft">#元学习</span> <span class="tag-pill tag-pill-soft">#自适应滤波</span> <span class="tag-pill tag-pill-soft">#声路径跟踪</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2609.30945</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-09-28</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
<div class="meta-row"><span class="meta-key">⭐</span><span class="meta-val focus-badge">本站重点关注领域 · 评分 +1</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2609.30945" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2609.30945" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出耦合元自适应滤波ANC方法，联合学习控制滤波器与声路径跟踪，在时变声路径下提升降噪与稳定性。
</div>

## 👥 作者与机构

**Boxiang Wang** ¹ · Zhengding Luo · Ziyi Yang · Dongyuan Shi · Xuexian Liu · Woon-Seng Gan

**机构**：南洋理工大学

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合做主动噪声控制、自适应滤波与元学习优化的研究者阅读。建议通读，重点看 §3 的 MG-JPI 结构与闭环耦合机制，以及时变路径跟踪实验表；若只关心方法，可先看 MG-JPI 与双速率实现两节，再对照 headrest 实测结果。

## 🌍 研究背景

主动噪声控制中，FxLMS 等传统自适应滤波依赖手工更新规则，收敛与跟踪能力受限。Meta-AF 用学习到的优化器替代手工更新，在 ANC 上取得进展，但其物理信息特征由次级路径估计构造，当物理路径随时间变化时特征失配，导致滤波器更新不准、降噪退化。本文要解决的核心问题是：在时变声路径下，如何让元自适应滤波器与路径跟踪协同更新，保持降噪性能与稳定性。

## 💡 核心创新

1. 提出 CoMeta-AF-ANC，闭环联合学习控制滤波与声路径跟踪
2. Meta-Gated Joint Path Identifier 无辅助噪声同时跟踪主/次级路径
3. 将更新后的次级路径估计反馈重建 Meta-AF 控制器特征
4. 无延迟双速率实现：帧率学习、采样率生成控制信号

## 🏗️ 模型架构

输入为 ANC 系统可获取的参考、误差与控制信号，主干为元学习驱动的自适应滤波框架。核心模块 MG-JPI 以门控机制从这些信号中联合估计主路径与次级路径，无需注入辅助噪声；更新后的次级路径估计回馈至 Meta-AF 控制器，用于重建物理信息优化器特征，形成闭环耦合。控制滤波器在帧率上执行学习式自适应，控制信号在采样率上于时域生成，构成无延迟双速率实现。摘要未给出参数量。

## 📚 数据集

- 实测头枕声路径（评估时变路径跟踪与降噪）
- 真实世界噪声（评估训练外泛化）

## 📊 实验结果

摘要仅给出定性结论：在实测头枕声路径上，CoMeta-AF-ANC 在跟踪时变声路径方面优于代表性 ANC 算法，并在未见头部移动场景下保持更高稳定性，同时对训练中未出现的真实噪声具有良好泛化。摘要未提供 SI-SDR、降噪量 dB、收敛速度等具体数值，也未给出消融与推理开销数据。

## 🎯 结论与影响

最强结论是：将声路径跟踪与控制滤波自适应在闭环中联合元学习，可显著缓解时变路径导致的 Meta-AF 特征失配。这为 ANC 中元学习优化器的鲁棒性研究提供了新思路，后续工作可沿闭环联合估计方向扩展。工业上对头戴/头枕等佩戴位置易变的主动降噪产品有直接参考价值。

## ⚠️ 局限与未解决问题

摘要未给出降噪量、收敛速度等定量指标，也未报告推理延迟与计算开销，难以判断双速率实现的实际成本。缺少与更多 ANC 基线（如 FxLMS、FxNLMS、Meta-AF 变体）的完整对比表与消融实验。评估仅限头枕实测路径，跨设备与强非线性场景的泛化性未知。

---

<div class="paper-footer"><span>评分：8.3</span><span>原始：7.3</span><span>+1 重点领域加权</span><a href="/audio-paper-daily/posts/2026-09-28/">← 返回 2026-09-28 速递</a></div>
