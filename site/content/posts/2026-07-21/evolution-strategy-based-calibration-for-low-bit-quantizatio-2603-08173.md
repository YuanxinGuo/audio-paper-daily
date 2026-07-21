---
title: "Evolution Strategy-Based Calibration for Low-Bit Quantization of Speech Models"
date: 2026-07-21T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#模型量化"]
summary: "提出基于进化策略的校准方法ESC，解决语音模型低比特量化中激活值范围大导致的信息损失问题，首次实现全INT4量化近无损性能。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#模型量化</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#低比特量化</span> <span class="tag-pill tag-pill-soft">#进化策略</span> <span class="tag-pill tag-pill-soft">#语音模型</span> <span class="tag-pill tag-pill-soft">#校准方法</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2603.08173</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-07-21</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2603.08173" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2603.08173" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出基于进化策略的校准方法ESC，解决语音模型低比特量化中激活值范围大导致的信息损失问题，首次实现全INT4量化近无损性能。
</div>

## 👥 作者与机构

**Lucas Rakotoarivony** ¹

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合从事模型压缩、语音模型部署的研究者阅读。建议重点读§3方法部分和§4实验部分，特别是表1-3的量化结果。可先看§3.2的两步局部-全局优化策略。

## 🌍 研究背景

量化是语音处理系统高效部署的关键技术，但现有方法多针对视觉和NLP架构，忽视了音频信号激活值范围大的特性。标准校准技术（如MinMax、Percentile）会导致显著信息损失，尤其在低比特（INT4）量化时。本文旨在设计一种针对语音模型激活值特性的校准方法，实现近无损的低比特量化。

## 💡 核心创新

1. 提出ESC方法，将激活值缩放建模为优化问题
2. 采用两步局部-全局进化策略求解缩放因子
3. 首次实现全INT4量化下多个语音任务的近无损性能
4. 与PTQ方法结合进一步降低性能损失

## 🏗️ 模型架构

ESC是一种校准方法，不改变模型架构。它针对量化过程中的激活值缩放因子，将其建模为优化问题，通过进化策略（ES）进行求解。具体采用两步方案：先局部优化每层缩放因子，再全局联合优化，以平衡各层量化误差。输入为预训练语音模型（如AST）的激活值统计量，输出为最优缩放因子，用于后续量化（如INT8/INT4）。

## 📚 数据集

- Speech Commands V2（评估，关键词分类）
- ESC-50（评估，环境声音分类）
- AudioSet（评估，音频事件分类）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| Accuracy | Speech Commands V2 | MinMax校准 INT4 92.5% | **ESC校准 INT4 96.7%** | +4.2% |
| Accuracy | ESC-50 | MinMax校准 INT4 78.3% | **ESC校准 INT4 85.1%** | +6.8% |
| mAP | AudioSet | MinMax校准 INT4 0.385 | **ESC校准 INT4 0.432** | +0.047 |

实验表明，ESC在INT8量化下实现无损性能，INT4量化下首次达到近无损（AST模型仅1%相对精度下降）。与现有PTQ方法（如LSQ、QAT）结合，ESC进一步减少性能损失，在AST上INT4量化仅损失1%相对精度。消融实验验证了两步优化策略的有效性。

## 🎯 结论与影响

本文提出的ESC校准方法有效解决了语音模型低比特量化中激活值范围大的问题，首次实现全INT4量化近无损性能。该方法可即插即用于现有PTQ流程，对语音模型在资源受限设备上的部署具有重要价值，有望推动语音处理系统的边缘化应用。

## ⚠️ 局限与未解决问题

实验仅在AST模型和分类任务上验证，未在语音增强、分离等生成式任务上测试。未报告推理速度或模型大小等效率指标。进化策略的收敛速度可能较慢，缺乏与其他校准方法（如AdaRound、BRECQ）的对比。

---

<div class="paper-footer"><span>评分：8.5</span><span>原始：8.5</span><a href="/audio-paper-daily/posts/2026-07-21/">← 返回 2026-07-21 速递</a></div>
