---
title: "BiTSE: Binaural Target Speaker Extraction in Noisy Multi-Talker Environments for AR Glass Arrays"
date: 2026-08-13T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#目标说话人提取"]
summary: "提出BiTSE，利用目标说话人方位和语音活动信息，在双耳信号上实现鲁棒的目标说话人提取，在SPEAR数据集上优于传统方法。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#目标说话人提取</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#双耳音频</span> <span class="tag-pill tag-pill-soft">#语音增强</span> <span class="tag-pill tag-pill-soft">#注意力机制</span> <span class="tag-pill tag-pill-soft">#AR</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2608.10106</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-08-13</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
<div class="meta-row"><span class="meta-key">⭐</span><span class="meta-val focus-badge">本站重点关注领域 · 评分 +1</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2608.10106" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2608.10106" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出BiTSE，利用目标说话人方位和语音活动信息，在双耳信号上实现鲁棒的目标说话人提取，在SPEAR数据集上优于传统方法。
</div>

## 👥 作者与机构

**Selani A. Indrapala** ¹ · Wageesha N. Manamperi

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合研究目标说话人提取、双耳音频处理和AR可穿戴设备语音增强的学者。建议重点阅读第3节（模型架构）和第4节（实验），特别是DoA注意力机制和两阶段损失设计。可先看摘要和结论，再深入方法部分。

## 🌍 研究背景

在嘈杂多说话人场景中，AR眼镜等可穿戴设备需要从双耳麦克风阵列中提取目标说话人。现有TSE方法多依赖单耳或阵列信号，未充分利用双耳空间信息。传统波束形成和语音增强方法在动态场景下性能受限。本文旨在结合目标方位（DoA）和语音活动信息，提升双耳TSE的性能和感知质量。

## 💡 核心创新

1. DoA感知注意力机制，使用循环位置编码
2. 基于时间戳的掩蔽策略，利用说话人活动抑制非目标段
3. 两阶段损失优化：先训练去噪，再微调感知质量

## 🏗️ 模型架构

输入为双耳麦克风信号，提取目标说话人DoA和语音活动信息。主干为双耳信号去噪网络，集成三个关键模块：DoA感知注意力（循环位置编码）引导空间特征，时间戳掩蔽利用VAD抑制非目标段，两阶段训练（先MSE后感知损失）优化。输出为估计的目标语音双耳信号。

## 📚 数据集

- SPEAR challenge dataset（评估）

## 📊 实验结果

摘要未提供具体数值，仅说明BiTSE在SPEAR数据集上一致优于传统方法，提升了信号保真度和感知质量。具体指标和消融实验需查阅全文。

## 🎯 结论与影响

BiTSE通过融合空间和时间线索，显著提升了双耳目标说话人提取性能，为AR可穿戴设备提供了有效方案。其DoA感知注意力和两阶段训练策略有望启发后续研究，推动双耳TSE在真实场景中的应用。

## ⚠️ 局限与未解决问题

摘要未提及模型参数量、推理延迟等效率指标，也未给出具体性能数值，缺乏与最新方法的定量对比。可能未考虑移动端部署的实时性要求。

---

<div class="paper-footer"><span>评分：8.8</span><span>原始：7.8</span><span>+1 重点领域加权</span><a href="/audio-paper-daily/posts/2026-08-13/">← 返回 2026-08-13 速递</a></div>
