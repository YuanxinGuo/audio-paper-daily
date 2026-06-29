---
title: "Taming Text-to-Sounding Video Generation via Advanced Modality Condition and Interaction"
date: 2026-06-29T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#音视频生成"]
summary: "提出HVGC框架解耦视频和音频文本条件，并设计BridgeDiT双塔扩散Transformer实现对称双向跨模态交互，在T2SV任务上达到SOTA。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#音视频生成</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#文本到音视频生成</span> <span class="tag-pill tag-pill-soft">#扩散Transformer</span> <span class="tag-pill tag-pill-soft">#跨模态交互</span> <span class="tag-pill tag-pill-soft">#解耦字幕</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2510.03117</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-06-29</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2510.03117" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2510.03117" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出HVGC框架解耦视频和音频文本条件，并设计BridgeDiT双塔扩散Transformer实现对称双向跨模态交互，在T2SV任务上达到SOTA。
</div>

## 👥 作者与机构

**Kaisi Guan** ¹ · Xihua Wang · Zhengfeng Lai · Xin Cheng · Peng Zhang · XiaoJiang Liu · Ruihua Song · Meng Cao

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合音视频生成、多模态学习方向的研究者。建议重点阅读§3.1 HVGC框架和§3.2 BridgeDiT架构，以及§4.3消融实验。可先看表1和表2了解整体性能。

## 🌍 研究背景

文本到音视频生成（T2SV）旨在从文本生成同步音视频，但现有方法存在两个问题：1）共享文本条件导致模态干扰，混淆预训练骨干；2）跨模态特征交互机制不明确。本文针对这两个挑战提出解耦字幕和对称交互机制。

## 💡 核心创新

1. 提出HVGC框架生成解耦的视频和音频字幕
2. 设计BridgeDiT双塔扩散Transformer架构
3. 提出Dual CrossAttention实现对称双向信息交换
4. 在三个基准数据集上达到SOTA

## 🏗️ 模型架构

输入文本经HVGC生成视频字幕和音频字幕，分别作为条件。主干为双塔扩散Transformer（BridgeDiT），每塔包含多个DiT块，块间通过Dual CrossAttention（DCA）模块连接，实现对称双向跨模态交互。输出为同步的视频帧和音频波形。

## 📚 数据集

- Landscape（训练/评估，含自然风景视频）
- AudioCaps（训练/评估，含音频描述）
- VAS（训练/评估，含音视频对）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| FVD | Landscape | T2AV 89.2 | **72.1** | -17.1 |
| FAD | Landscape | T2AV 2.34 | **1.87** | -0.47 |
| CLIPSIM | Landscape | T2AV 0.312 | **0.335** | +0.023 |

在Landscape、AudioCaps、VAS三个数据集上，本文方法在FVD、FAD、CLIPSIM等指标上均优于T2AV等基线。消融实验验证了HVGC和DCA各自的有效性，且DCA优于单向交叉注意力。人类评估也表明生成音视频同步性更好。

## 🎯 结论与影响

本文通过解耦字幕和对称跨模态交互有效解决了T2SV中的模态干扰和交互问题，为音视频联合生成提供了新范式。开源代码将促进该方向研究，对多媒体内容创作有潜在应用价值。

## ⚠️ 局限与未解决问题

未报告模型参数量和推理速度；仅在自然风景和通用视频上评估，未见复杂场景（如对话、音乐）；解耦字幕依赖预训练模型，可能引入误差；未与最新视频生成模型（如VideoLDM）对比。

---

<div class="paper-footer"><span>评分：7.8</span><span>原始：7.8</span><a href="/audio-paper-daily/posts/2026-06-29/">← 返回 2026-06-29 速递</a></div>
