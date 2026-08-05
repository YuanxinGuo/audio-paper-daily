---
title: "Hear to See: Discerning Stateful Listening for Audio-Visual Instance Segmentation"
date: 2026-08-05T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#音视频实例分割"]
summary: "提出H2S模型，通过声学语义投影器和异步动态调制器解决音视频实例分割中的重叠声源匹配与异步动态问题，在AVISeg上达到SOTA。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#音视频实例分割</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#音视频分割</span> <span class="tag-pill tag-pill-soft">#Mamba</span> <span class="tag-pill tag-pill-soft">#音频语义投影</span> <span class="tag-pill tag-pill-soft">#异步动态调制</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2608.03264</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-08-05</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner"><div class="oc-headline"><span class="oc-pulse"></span><span class="oc-title">本论文已开源</span><span class="oc-hint">点击下方卡片直达对应资源</span></div><div class="oc-grid"><a class="oc-chip oc-chip-code" href="https://github.com/leiyeliu/H2S" target="_blank" rel="noopener"><span class="oc-icon">💻</span><span class="oc-text"><span class="oc-label">代码仓库</span><span class="oc-sub">leiyeliu/H2S</span></span></a></div></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2608.03264" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2608.03264" target="_blank" rel="noopener">📑 PDF</a><a class="rsrc rsrc-code" href="https://github.com/leiyeliu/H2S" target="_blank" rel="noopener">💻 代码</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出H2S模型，通过声学语义投影器和异步动态调制器解决音视频实例分割中的重叠声源匹配与异步动态问题，在AVISeg上达到SOTA。
</div>

## 👥 作者与机构

**Leiye Liu** ¹ · Miao Zhang · Jiahong Jiang · Jingjing Li · Jialong Zhong · Kai Peng · Tingwei Liu · Wei Ji · … 等 2 人

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合从事音视频分割、多模态感知的研究人员阅读。建议重点阅读第3节的方法部分，特别是ASP和ADM模块的设计，以及第4节的实验对比。可先看表1和表2了解性能提升，再深入理解Mamba在异步建模中的应用。

## 🌍 研究背景

音视频实例分割（AVIS）要求精确识别并跟踪每个发声物体的像素级掩码。现有方法难以匹配重叠声学事件与视觉实例，且无法处理音视频异步动态。此前方法多采用简单的特征融合或注意力机制，但缺乏对音频语义的显式解耦和时序状态建模。本文旨在解决这两个关键问题，提出H2S模型。

## 💡 核心创新

1. 提出声学语义投影器（ASP），解耦混合音频并建立从语义到空间的层次对应
2. 提出异步动态调制器（ADM），利用音频调制Mamba的状态转换，自适应调整时序信息
3. 在AVISeg上实现48.54 mAP，超越先前最佳7.8%
4. 代码将开源，便于复现和后续研究

## 🏗️ 模型架构

H2S模型输入为视频帧和混合音频。音频经声学语义投影器（ASP）解耦，生成每个声源的语义嵌入和空间位置线索；视觉特征由ResNet50提取。主干网络采用Mamba架构，通过异步动态调制器（ADM）根据音频状态调整Mamba的时序状态转换，优先处理动态变化时的当前信息，保持稳定期的连续性。最终输出每个实例的像素级掩码。

## 📚 数据集

- AVISeg（训练和评估）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| mAP | AVISeg | 先前最佳（未给出具体值） | **48.54** | +7.8% |

在AVISeg上，H2S达到48.54 mAP，相比先前最佳方法提升7.8%。实验表明，ASP和ADM模块均对性能有显著贡献，消融研究验证了其有效性。此外，模型在异步场景下表现稳健，但未报告推理速度或参数量。

## 🎯 结论与影响

H2S通过解耦音频语义和异步动态调制，有效解决了音视频实例分割中的重叠匹配和时序异步问题，达到SOTA性能。该方法为多模态时序建模提供了新思路，有望推动音视频分割在视频理解、自动驾驶等领域的应用。

## ⚠️ 局限与未解决问题

摘要未提及消融实验细节、推理效率、模型复杂度，也未与其他异步建模方法对比。此外，仅在一个数据集上评估，泛化性未知。代码尚未公开，复现性待验证。

## 🔗 开源资源

- **代码**：<https://github.com/leiyeliu/H2S>

---

<div class="paper-footer"><span>评分：7.8</span><span>原始：7.8</span><a href="/audio-paper-daily/posts/2026-08-05/">← 返回 2026-08-05 速递</a></div>
