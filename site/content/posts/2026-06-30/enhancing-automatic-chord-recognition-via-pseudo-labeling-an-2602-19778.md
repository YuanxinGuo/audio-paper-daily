---
title: "Enhancing Automatic Chord Recognition via Pseudo-Labeling and Knowledge Distillation"
date: 2026-06-30T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#和弦识别"]
summary: "提出两阶段训练流程，利用预训练模型生成伪标签并配合知识蒸馏，在无标签数据上训练学生模型，最终超越教师模型和监督基线。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#和弦识别</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#伪标签</span> <span class="tag-pill tag-pill-soft">#知识蒸馏</span> <span class="tag-pill tag-pill-soft">#半监督学习</span> <span class="tag-pill tag-pill-soft">#音乐信息检索</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2602.19778</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-06-30</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2602.19778" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2602.19778" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出两阶段训练流程，利用预训练模型生成伪标签并配合知识蒸馏，在无标签数据上训练学生模型，最终超越教师模型和监督基线。
</div>

## 👥 作者与机构

**Nghia Phan** ¹ · Rong Jin · Gang Liu · Xiao Dong

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合音乐信息检索和半监督学习研究者。建议通读，重点看§3两阶段训练和§4实验。可关注伪标签生成策略和知识蒸馏的消融实验。

## 🌍 研究背景

自动和弦识别（ACR）受限于对齐标签稀缺且标注成本高。现有预训练模型虽易获取，但训练数据不公开。本文旨在利用大量无标签音频和预训练模型，通过伪标签和知识蒸馏提升ACR性能，解决标签不足问题。

## 💡 核心创新

1. 两阶段训练：先伪标签预训练，后真实标签微调
2. 选择性知识蒸馏防止灾难性遗忘
3. 使用BTC模型作为教师生成1000+小时伪标签
4. 学生模型在多个指标上超越教师和监督基线

## 🏗️ 模型架构

输入音频特征 → 预训练BTC模型作为教师生成伪标签 → 学生模型（BTC或2E1D）在伪标签上训练（Stage 1）→ 在真实标签上微调，同时从教师进行选择性知识蒸馏作为正则化（Stage 2）→ 输出和弦标签序列。

## 📚 数据集

- 未标注音频（1000+小时，用于伪标签生成）
- 标注数据集（用于Stage 2训练和评估，具体名称未提及）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| mir_eval指标（7个标准指标） | 未指定测试集 | 传统监督基线（未给出具体值） | **BTC学生模型超越教师和监督基线** | 未给出具体数值 |

Stage 1中，BTC学生模型达到教师约99%性能，2E1D模型约97%。Stage 2后，BTC学生模型在所有指标上超越监督基线和教师模型；2E1D学生模型超越监督基线，接近教师水平。稀有和弦类别上提升显著。

## 🎯 结论与影响

本文证明利用预训练模型和大量无标签数据可显著提升ACR性能，两阶段训练结合知识蒸馏有效避免灾难性遗忘。该方法为半监督音乐标注提供了新范式，有望降低标注成本，推动ACR实际应用。

## ⚠️ 局限与未解决问题

未报告具体数据集名称和规模，缺乏与最新ACR方法的对比；未分析伪标签质量对结果的影响；未讨论模型参数量和推理效率；稀有和弦提升的具体指标未量化。

---

<div class="paper-footer"><span>评分：7.8</span><span>原始：7.8</span><a href="/audio-paper-daily/posts/2026-06-30/">← 返回 2026-06-30 速递</a></div>
