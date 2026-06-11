---
title: "ViP-VL: Vietnamese Self-supervised Speech Pretraining Model with Vector-Quantization Learning"
date: 2026-06-11T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#语音识别"]
summary: "提出ViP-VL，一种基于向量量化的越南语自监督语音预训练模型，在17000小时数据上预训练，刷新四项下游任务SOTA。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero">
<div class="hero-score">
<div class="score-num">8.2</div>
<div class="score-stars">★★★★☆</div>
<div class="score-tier">前25%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#语音识别</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#自监督学习</span> <span class="tag-pill tag-pill-soft">#向量量化</span> <span class="tag-pill tag-pill-soft">#越南语</span> <span class="tag-pill tag-pill-soft">#语音处理</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2606.10360</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-06-11</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner"><div class="oc-headline"><span class="oc-pulse"></span><span class="oc-title">本论文已开源</span><span class="oc-hint">点击下方卡片直达对应资源</span></div><div class="oc-grid"><a class="oc-chip oc-chip-code" href="https://github.com/khanld/chunkformer" target="_blank" rel="noopener"><span class="oc-icon">💻</span><span class="oc-text"><span class="oc-label">代码仓库</span><span class="oc-sub">khanld/chunkformer</span></span></a></div></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2606.10360" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2606.10360" target="_blank" rel="noopener">📑 PDF</a><a class="rsrc rsrc-code" href="https://github.com/khanld/chunkformer" target="_blank" rel="noopener">💻 代码</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出ViP-VL，一种基于向量量化的越南语自监督语音预训练模型，在17000小时数据上预训练，刷新四项下游任务SOTA。
</div>

## 👥 作者与机构

**Khanh Le** ¹ · Kiet Anh Hoang · Bao Nguyen · Duy Vo · Dung Vo · Thai Tran · Linh Pham · Khoa D Doan

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合从事语音自监督学习、多任务预训练或越南语语音技术的研究者。建议重点阅读§3的ChunkFormer架构和Mask Selection策略，以及§4的表1-4对比结果。可复现其开源代码。

## 🌍 研究背景

自监督语音预训练在英语等资源丰富语言上取得显著成功，但针对越南语等低资源语言的工作较少。现有模型如Wav2Vec2.0、HuBERT等通常采用高分辨率输入，计算开销大。此外，越南语特有的声调、方言多样性对表示学习提出挑战。本文旨在设计一个高效、鲁棒的越南语自监督预训练模型，同时提升多项下游任务性能。

## 💡 核心创新

1. Acoustic Stacking实现8倍下采样，降低计算量
2. Receptive Field Alignment同步下采样与ChunkFormer感受野
3. Mask Selection Strategy在BEST-RQ框架中增强表示鲁棒性

## 🏗️ 模型架构

输入16kHz波形经Acoustic Stacking（堆叠帧）实现8倍下采样，送入ChunkFormer主干网络（基于Conformer的块状Transformer），通过Receptive Field Alignment确保下采样后感受野对齐。预训练采用BEST-RQ框架，结合向量量化（VQ）和Mask Selection Strategy（动态选择掩码区域）。输出为离散化表示，用于下游任务微调。模型参数量未提及。

## 📚 数据集

- 17000小时未标注越南语语音（预训练）
- VIVOS（ASR评估）
- VNEMO（SER评估）
- VSDC（方言分类评估）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| WER | VIVOS | Wav2Vec2.0 15.2 | **12.8** | -2.4% |
| Accuracy | VNEMO (SER) | HuBERT 72.3% | **76.1%** | +3.8% |
| Accuracy | VSDC (Dialect) | XLSR-53 85.6% | **88.2%** | +2.6% |
| EER | VoxCeleb1 (SV) | WavLM 3.2% | **2.8%** | -0.4% |

ViP-VL在ASR、SER、方言分类和说话人验证四项任务上均超越现有SOTA，包括Wav2Vec2.0、HuBERT、XLSR-53和WavLM。消融实验验证了Acoustic Stacking和Mask Selection的有效性。模型在低资源场景下表现优异，且推理速度因8倍下采样而提升。

## 🎯 结论与影响

ViP-VL通过向量量化和高效架构设计，在越南语自监督预训练上达到新SOTA，证明了针对特定语言设计预训练策略的价值。该工作为低资源语言语音技术提供了可复现的基线，有望推动越南语语音应用落地。

## ⚠️ 局限与未解决问题

未报告模型参数量和推理延迟的具体数值；预训练数据仅涵盖越南语，跨语言泛化能力未知；Mask Selection策略的消融实验不够深入；未与近期大模型如Whisper对比。

## 🔗 开源资源

- **代码**：<https://github.com/khanld/chunkformer>

---

<div class="paper-footer"><span>评分：8.2</span><span>原始：8.2</span><a href="/audio-paper-daily/posts/2026-06-11/">← 返回 2026-06-11 速递</a></div>
