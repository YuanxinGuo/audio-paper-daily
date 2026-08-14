---
title: "RT-SEMamba: Real-Time Speech Enhancement Mamba via Progressive Knowledge Distillation"
date: 2026-08-14T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#语音增强"]
summary: "RT-SEMamba提出基于因果时频Mamba的实时语音增强模型，通过渐进式知识蒸馏将8层教师压缩为1层学生，在Voicebank-DEMAND上达到3.18 PESQ，速度提升2.75倍。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#语音增强</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#Mamba</span> <span class="tag-pill tag-pill-soft">#知识蒸馏</span> <span class="tag-pill tag-pill-soft">#实时语音增强</span> <span class="tag-pill tag-pill-soft">#因果模型</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2608.12099</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-08-14</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
<div class="meta-row"><span class="meta-key">⭐</span><span class="meta-val focus-badge">本站重点关注领域 · 评分 +1</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2608.12099" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2608.12099" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>RT-SEMamba提出基于因果时频Mamba的实时语音增强模型，通过渐进式知识蒸馏将8层教师压缩为1层学生，在Voicebank-DEMAND上达到3.18 PESQ，速度提升2.75倍。
</div>

## 👥 作者与机构

**Rong Chao** ¹ · Sung-Feng Huang · Moreno La Quatra · Sabato Marco Siniscalchi · Wen-Huang Cheng · Szu-Wei Fu · Yu Tsao

**机构**：台湾大学 · 纽约大学 · 佐治亚理工学院 · 台湾中央研究院

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合语音增强和高效模型设计的研究者阅读。建议重点看第3节的模型架构和第4节的渐进蒸馏策略，以及表2的PESQ和RTF对比。若关注实时部署，可先看第5节延迟分析。

## 🌍 研究背景

实时语音增强需要在低延迟下保持高质量，Transformer模型因自注意力缓存增长导致长序列推理效率低。Mamba等状态空间模型以固定大小循环状态传播，内存和带宽高效，但直接应用在语音增强上性能不足。本文旨在利用Mamba的因果时频块构建实时SE模型，并通过知识蒸馏提升浅层模型性能，实现质量与延迟的平衡。

## 💡 核心创新

1. 提出因果时频Mamba块，实现全因果实时语音增强
2. 渐进式知识蒸馏，同时蒸馏频谱输出和中间表示
3. 将8层教师压缩为1层学生，PESQ提升0.12且速度提升2.75倍
4. 在25ms延迟约束下达到3.32 PESQ，优于Transformer基线

## 🏗️ 模型架构

RT-SEMamba采用编码器-解码器结构，输入为带噪语音的复数频谱，通过因果时频Mamba块处理。每个块包含沿频率轴和时间轴的Mamba层，保持因果性。教师模型为8层，学生为1层，通过渐进式KD训练，蒸馏目标包括输出频谱和中间层表示。模型全因果，支持流式推理，固定状态大小保证内存效率。

## 📚 数据集

- Voicebank-DEMAND（训练和评估，包含带噪语音和干净语音）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| PESQ | Voicebank-DEMAND | Naive 1-layer 3.06 | **Distilled 1-layer 3.18** | +0.12 |
| PESQ | Voicebank-DEMAND | Teacher 8-layer 3.32 | **Student 1-layer 3.18** | -0.14 |

在Voicebank-DEMAND上，8层教师模型达到3.32 PESQ，满足25ms延迟约束。蒸馏后的1层学生模型PESQ从3.06提升至3.18，同时保持相同的稳态RTF，推理速度比教师快2.75倍。结果表明渐进式KD有效弥补了深度缩减带来的性能损失。

## 🎯 结论与影响

RT-SEMamba证明了状态空间模型结合渐进式知识蒸馏能在实时语音增强中取得质量与延迟的优越权衡。1层学生模型在保持实时性的同时显著提升性能，为低资源设备上的高质量SE提供了新方案。未来可探索更高效的蒸馏策略和跨数据集泛化。

## ⚠️ 局限与未解决问题

仅在单一数据集（Voicebank-DEMAND）上评估，缺乏跨数据集泛化验证。未报告模型参数量和计算量（MACs），也未与更多实时SE基线（如DCCRN、FullSubNet）对比。蒸馏过程可能依赖教师质量，未探讨教师性能上限的影响。

---

<div class="paper-footer"><span>评分：9.2</span><span>原始：8.2</span><span>+1 重点领域加权</span><a href="/audio-paper-daily/posts/2026-08-14/">← 返回 2026-08-14 速递</a></div>
