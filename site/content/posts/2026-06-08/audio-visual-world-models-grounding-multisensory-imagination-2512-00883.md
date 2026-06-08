---
title: "Audio-Visual World Models: Grounding Multisensory Imagination for Embodied Agents"
date: 2026-06-08T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#多模态世界模型"]
summary: "提出音频-视觉世界模型AVWM，通过条件扩散Transformer联合预测双耳音频与视觉未来帧，并验证其在具身导航中的实用性。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero hero-focus">
<div class="hero-score">
<div class="score-num">9.2</div>
<div class="score-stars">★★★★★</div>
<div class="score-tier">前25%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#多模态世界模型</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#双耳音频</span> <span class="tag-pill tag-pill-soft">#视觉-音频联合建模</span> <span class="tag-pill tag-pill-soft">#具身智能</span> <span class="tag-pill tag-pill-soft">#扩散Transformer</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2512.00883</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-06-08</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
<div class="meta-row"><span class="meta-key">⭐</span><span class="meta-val focus-badge">本站重点关注领域 · 评分 +1</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2512.00883" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2512.00883" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出音频-视觉世界模型AVWM，通过条件扩散Transformer联合预测双耳音频与视觉未来帧，并验证其在具身导航中的实用性。
</div>

## 👥 作者与机构

**Jiahua Wang** ¹ · Leqi Zheng · Jialong Wu · Yaoxin Mao · Shijie Cheng

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合多模态学习、具身智能、音频-视觉联合建模方向的研究者。建议重点阅读§3（问题形式化）、§4.2（AV-CDiT架构）及§5.3（导航实验）。可先看表1与图3了解性能。

## 🌍 研究背景

世界模型通过模拟环境动态使智能体能够规划和推理未来状态。现有工作主要关注视觉模态，但真实感知涉及多感官，音频提供空间和时间线索（如声源定位、声学场景）。然而，音频-视觉世界模型在低级动作控制下的统一形式化及联合建模双耳音频与视觉动态尚未被充分探索。本文旨在填补这一空白。

## 💡 核心创新

1. 提出AVWM统一形式化，将多模态环境模拟建模为POMDP
2. 构建AVW-4k基准，含30小时双耳音频-视觉轨迹及动作标注
3. 提出AV-CDiT，采用模态专家架构平衡视觉与听觉学习
4. 设计三阶段训练策略实现有效多模态融合

## 🏗️ 模型架构

输入为历史音频-视觉观测与动作序列。主干为条件扩散Transformer（CDiT），其中引入模态专家架构：视觉和音频各有一个独立的专家模块，通过交叉注意力交互。扩散过程以噪声预测方式生成未来多模态帧。输出为预测的双耳音频和视觉帧。模型参数量未在摘要中给出。

## 📚 数据集

- AVW-4k（训练/评估，30小时双耳音频-视觉轨迹，76个室内环境）

## 📊 实验结果

摘要未提供具体数值指标，但声称AV-CDiT在AVW-4k基准上实现了高保真多模态预测，并在连续音频-视觉导航任务中提升了VLM引导智能体的性能。具体定量结果需查阅全文。

## 🎯 结论与影响

本文首次系统性地提出音频-视觉世界模型，通过AV-CDiT实现了双耳音频与视觉的联合预测，并在具身导航中验证了其有效性。该工作为多模态世界模型研究开辟了新方向，有望推动更真实的具身智能体在复杂环境中的感知与规划。

## ⚠️ 局限与未解决问题

摘要未提及局限。可能的问题包括：基准AVW-4k规模有限（30小时），且仅覆盖室内场景；未与现有世界模型方法（如DreamerV3）进行直接对比；导航实验可能依赖特定VLM，泛化性未知；未报告推理延迟或计算开销。

---

<div class="paper-footer"><span>评分：9.2</span><span>原始：8.2</span><span>+1 重点领域加权</span><a href="/audio-paper-daily/posts/2026-06-08/">← 返回 2026-06-08 速递</a></div>
