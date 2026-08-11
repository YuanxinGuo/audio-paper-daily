---
title: "Omni-modal decomposition autoencoders learn full-stack wearable disentangled representations"
date: 2026-08-11T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#可穿戴计算"]
summary: "提出OmniDecVAEs，一种可扩展的多模态变分分解自编码器，在多达30模态的HAR任务中实现全栈解耦表示，提升识别精度与生成质量。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero">
<div class="hero-score">
<div class="score-num">7.2</div>
<div class="score-stars">★★★★☆</div>
<div class="score-tier">前25%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#可穿戴计算</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#多模态学习</span> <span class="tag-pill tag-pill-soft">#解耦表示</span> <span class="tag-pill tag-pill-soft">#自编码器</span> <span class="tag-pill tag-pill-soft">#人类活动识别</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2608.07385</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-08-11</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2608.07385" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2608.07385" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出OmniDecVAEs，一种可扩展的多模态变分分解自编码器，在多达30模态的HAR任务中实现全栈解耦表示，提升识别精度与生成质量。
</div>

## 👥 作者与机构

**Ioannis Ziogas** ¹ · Ensieh Khazaei · Bilal Taha · Aamna Al Shehhi · Ahsan H. Khandoker · Leontios J. Hadjileontiadis · Dimitrios Hatzinakos

**机构**：多伦多大学 · 哈利法大学 · 亚里士多德大学

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合可穿戴计算、多模态学习、自监督表示学习研究者阅读。建议重点阅读方法部分（第3节）和实验部分（第4节），尤其是表2和表3，以了解模型在多模态融合和生成方面的优势。可先浏览图1了解整体架构。

## 🌍 研究背景

多模态可穿戴计算需要模型同时具备分类、解耦表示学习、融合和生成能力，但现有方法往往只关注单一任务，难以处理高度异构的多模态时间序列。之前的SOTA如Transformer和VAE方法在解耦性和生成质量上存在局限。本文旨在提出一个统一框架，同时解决这些需求，实现全栈可穿戴处理。

## 💡 核心创新

1. 提出OmniDecVAEs框架，统一处理任意数量模态
2. 引入模态条件的时间-频率潜在子空间
3. 设计多视图自监督分解损失
4. 采用共享非对称自编码器架构
5. 在30模态HAR任务上验证全栈能力

## 🏗️ 模型架构

OmniDecVAEs基于DecVAEs扩展，输入为多模态时间序列，通过模态编码器提取特征，映射到模态条件的时间-频率潜在子空间。采用共享非对称自编码器（AE）结构，编码器将各模态映射到潜在空间，解码器重建原始信号。训练时使用多视图自监督分解损失，促进解耦表示学习。模型参数4.1M，支持实时推理。

## 📚 数据集

- 多模态HAR数据集（30模态，训练/评估）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| 准确率 | 多模态HAR | Transformer-based 方法（未给出具体值） | **提升1.01%** | +1.01% |
| 身份识别准确率 | 多模态HAR | VAE-based 方法（未给出具体值） | **提升6.75%** | +6.75% |
| 平均绝对误差（MAE） | 多模态HAR | 未给出 | **改善76.84%** | -76.84% |
| 最大均值差异（MMD） | 多模态HAR | 未给出 | **改善13.85%** | -13.85% |

实验在包含30个模态的挑战性HAR设置下进行，OmniDecVAEs在活动识别和身份识别上分别比Transformer和VAE方法提升1.01%和6.75%。在生成方面，重建误差（MAE）改善76.84%，分布相似性（MMD）改善13.85%。模型参数仅4.1M，具备实时推理能力，展示了轻量级和高效性。

## 🎯 结论与影响

OmniDecVAEs通过统一框架实现了多模态可穿戴计算的全栈处理，显著提升了解耦表示的质量和生成性能。其轻量级设计适合边缘设备部署，为智能可穿戴和临床医疗提供了新方案。未来可扩展到更多模态和任务，推动多模态学习的发展。

## ⚠️ 局限与未解决问题

摘要未提及具体数据集名称和规模，缺乏与更多SOTA方法的对比，未报告推理延迟的具体数值，也未进行消融研究。此外，模型在真实场景中的泛化能力有待验证。

---

<div class="paper-footer"><span>评分：7.2</span><span>原始：7.2</span><a href="/audio-paper-daily/posts/2026-08-11/">← 返回 2026-08-11 速递</a></div>
