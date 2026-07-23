---
title: "Layer-Wise Decision Fusion for Fake Audio Detection Using XLS-R"
date: 2026-07-23T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#假音频检测"]
summary: "提出层间决策融合方法，利用XLS-R多层表示进行假音频检测，在In-the-Wild数据集上取得6.90% EER。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#假音频检测</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#语音反欺骗</span> <span class="tag-pill tag-pill-soft">#XLS-R</span> <span class="tag-pill tag-pill-soft">#决策融合</span> <span class="tag-pill tag-pill-soft">#泛化性</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2607.20023</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-07-23</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2607.20023" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2607.20023" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出层间决策融合方法，利用XLS-R多层表示进行假音频检测，在In-the-Wild数据集上取得6.90% EER。
</div>

## 👥 作者与机构

**Yixuan Xiao** ¹ · Ngoc Thang Vu

**机构**：斯图加特大学

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合从事音频反欺骗、说话人验证的研究者阅读。建议重点读§3方法部分和§4.2跨数据集实验，可复现其决策融合策略。

## 🌍 研究背景

假音频检测（FAD）旨在区分真实语音与合成/重放语音。现有方法多基于大语音模型（如XLS-R）提取单层或融合特征，但深层模型的多层表示未被充分利用，且特征融合可能导致信息丢失或特征坍塌。本文针对此问题，提出层间决策融合方法，在每层独立决策后再融合，提升检测性能与模型可解释性。

## 💡 核心创新

1. 提出层间决策融合（Layer-wise Decision Fusion）
2. 在XLS-R每层后接轻量分类器，独立决策后融合
3. 跨数据集泛化性优于单层/特征融合基线
4. 提供决策可视化分析，揭示模型内部机制

## 🏗️ 模型架构

输入语音经XLS-R（大规模自监督语音模型）提取多层表示，每层表示通过一个轻量分类器（全连接层+softmax）输出决策分数，最后将所有层的决策分数进行加权融合（权重可学习或固定），得到最终预测。模型参数量取决于XLS-R规模（如XLS-R-0.3B）。

## 📚 数据集

- In-the-Wild（评估，包含真实与多种伪造语音）
- ASVspoof2019 LA（训练/评估，逻辑访问场景）
- ASVspoof2021 DF（评估，深度伪造场景）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| EER (%) | In-the-Wild | XLS-R单层（最后一层） 8.50 | **6.90** | -1.60 |
| EER (%) | ASVspoof2021 DF | XLS-R单层 12.30 | **10.50** | -1.80 |

在In-the-Wild数据集上，所提方法EER为6.90%，优于单层（8.50%）和特征融合（7.80%）基线。在ASVspoof2021 DF上EER 10.50%，同样优于基线。消融实验表明，融合所有层比仅用浅层或深层效果更好，且可学习权重优于平均融合。

## 🎯 结论与影响

本文提出的层间决策融合方法有效利用了XLS-R的多层表示，在假音频检测任务上取得跨数据集最优性能。该方法增强了模型可解释性，为后续研究提供了新思路，有望提升工业级反欺骗系统的鲁棒性。

## ⚠️ 局限与未解决问题

仅在XLS-R上验证，未探索其他大语音模型（如WavLM、HuBERT）。融合权重可学习但未分析其与层语义的关系。未报告推理速度与计算开销。

---

<div class="paper-footer"><span>评分：7.8</span><span>原始：7.8</span><a href="/audio-paper-daily/posts/2026-07-23/">← 返回 2026-07-23 速递</a></div>
