---
title: "Mitigating Over-Suppression in Speech Enhancement via Inference-Time Rethink-and-Refine Correction Module"
date: 2026-08-12T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#语音增强"]
summary: "提出一种推理时重思与修正模块，通过ASR对齐识别过抑制区间并选择性重混，无需训练即可提升多种语音增强模型的感知质量和可懂度。"
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
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#语音增强</span> <span class="tag-pill tag-pill-soft">#推理时修正</span> <span class="tag-pill tag-pill-soft">#ASR引导</span> <span class="tag-pill tag-pill-soft">#过抑制</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2608.07781</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-08-12</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
<div class="meta-row"><span class="meta-key">⭐</span><span class="meta-val focus-badge">本站重点关注领域 · 评分 +1</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2608.07781" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2608.07781" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出一种推理时重思与修正模块，通过ASR对齐识别过抑制区间并选择性重混，无需训练即可提升多种语音增强模型的感知质量和可懂度。
</div>

## 👥 作者与机构

**Mike Qu** ¹ · Yu-Wen Chen · Julia Hirschberg

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合语音增强和鲁棒语音处理研究者阅读。值得通读，重点看方法部分（§2）和实验部分（§3），尤其是表1和表2。可先看§2.3的权重优化策略。

## 🌍 研究背景

语音增强模型常因过度抑制而损伤语音成分，导致感知质量下降。现有方法多通过改进训练目标或网络结构缓解，但难以泛化到不同模型。本文提出一种推理时后处理模块，利用ASR对齐检测不可靠区间并选择性重混，无需重新训练即可集成到现有SE系统，旨在提升感知质量和语音可懂度。

## 💡 核心创新

1. 推理时无需训练的修正模块，即插即用
2. 利用ASR对齐识别过抑制区间
3. 凸插值重混，分段权重优化
4. 复合目标平衡感知质量和语音保留

## 🏗️ 模型架构

输入为带噪信号和SE增强信号，通过ASR模型获得词/音素级对齐，计算可靠性分数识别过抑制区间。对每个区间，通过凸插值将带噪和增强信号混合，权重通过优化复合目标（如PESQ和STOI）确定。输出为修正后的增强信号。模块不改变原SE模型，仅在后端进行修正。

## 📚 数据集

- URGENT 2024（评估）
- URGENT 2025（评估）
- VCTK-DEMAND（评估）
- MSP-PODCAST（评估）

## 📊 实验结果

摘要未给出具体数值，但声称在URGENT 2024/2025、VCTK-DEMAND和MSP-PODCAST上，相比传统SE，感知质量、可懂度和下游任务性能均有一致提升。

## 🎯 结论与影响

本文提出的推理时修正模块有效缓解了语音增强中的过抑制问题，无需训练即可提升多种SE模型的性能，为鲁棒语音处理提供了新思路。该方法有望作为通用后处理模块集成到现有系统中，推动实际应用。

## ⚠️ 局限与未解决问题

摘要未提及局限。可能的问题：依赖ASR对齐的准确性，在低信噪比或重噪环境下ASR可能失效；未报告计算开销和延迟；未与专门针对过抑制的端到端方法对比；实验仅评估了感知质量，未涉及主观听感测试。

---

<div class="paper-footer"><span>评分：8.8</span><span>原始：7.8</span><span>+1 重点领域加权</span><a href="/audio-paper-daily/posts/2026-08-12/">← 返回 2026-08-12 速递</a></div>
