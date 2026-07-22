---
title: "Auto-AEG: Scalable Data Construction for Open-Vocabulary Audio Event Grounding"
date: 2026-07-22T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#音频事件定位"]
summary: "提出Auto-AEG流水线，通过自动数据构建和强化学习微调，解决开放词汇音频事件定位的数据稀缺问题。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#音频事件定位</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#开放词汇</span> <span class="tag-pill tag-pill-soft">#数据构建</span> <span class="tag-pill tag-pill-soft">#大音频语言模型</span> <span class="tag-pill tag-pill-soft">#强化学习</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2607.04383</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-07-22</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner"><div class="oc-headline"><span class="oc-pulse"></span><span class="oc-title">本论文已开源</span><span class="oc-hint">点击下方卡片直达对应资源</span></div><div class="oc-grid"><a class="oc-chip oc-chip-hf" href="https://huggingface.co/datasets/zihan-audio/AEGBench" target="_blank" rel="noopener"><span class="oc-icon">🤗</span><span class="oc-text"><span class="oc-label">HuggingFace</span><span class="oc-sub">🤗 datasets/zihan-audio/AEGBench</span></span></a></div></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2607.04383" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2607.04383" target="_blank" rel="noopener">📑 PDF</a><a class="rsrc rsrc-hf" href="https://huggingface.co/datasets/zihan-audio/AEGBench" target="_blank" rel="noopener">🤗 HuggingFace</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出Auto-AEG流水线，通过自动数据构建和强化学习微调，解决开放词汇音频事件定位的数据稀缺问题。
</div>

## 👥 作者与机构

**Zihan Zhang** ¹ · Xize Cheng · Wenhao Yan · Tong Zhang · Dongjie Fu · Boyun Zhang · Yongbo He · Tao Jin

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合音频事件检测和LALM研究者阅读。重点看§3数据构建流水线和§4.2奖励函数设计。建议先读摘要和结论，再深入方法部分。

## 🌍 研究背景

开放词汇音频事件定位旨在根据任意自然语言查询预测目标声音事件的所有时间区间，对真实场景音频理解和LALM适配至关重要。然而，大规模提供开放词汇起止时间监督的数据集稀缺，手动标注成本过高。现有方法要么是封闭集的声音事件检测，要么是LALM的粗粒度推理，缺乏精确时间定位能力。本文旨在通过自动数据构建和模型微调解决这一数据瓶颈。

## 💡 核心创新

1. 提出Auto-AEG自动数据构建流水线
2. 程序化合成带精确时间标签的冷启动数据
3. 多模型伪标签结合强化学习微调
4. 发布难度分层的AEGBench基准
5. 设计区间感知奖励函数

## 🏗️ 模型架构

输入为音频和自然语言查询。主干网络采用LALM（如AudioFlama），通过自动数据构建流水线生成训练数据：1）程序化合成音频片段，带有精确的起止时间标签用于监督冷启动；2）对真实音频使用多模型（如SED模型和LALM）生成伪标签作为强化学习奖励信号。模型输出为预测的时间区间。

## 📚 数据集

- DESED（评估，声音事件检测基准）
- AEGBench（评估，本文发布的难度分层基准）
- 合成数据集（训练，程序化生成）
- 真实音频数据集（训练，用于伪标签）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| F1-score | DESED SED | 未明确给出 | **未明确给出** | 有提升（具体数值未在摘要中提供） |
| AEGBench指标 | AEGBench | 未明确给出 | **未明确给出** | 有提升（具体数值未在摘要中提供） |

摘要中未提供具体数值，仅说明在DESED SED基准和AEGBench上取得有前景的性能提升。实验表明自动构建数据结合区间感知奖励函数是扩展LALM时间定位能力的有效数据侧途径。

## 🎯 结论与影响

本文最强结论：自动数据构建结合强化学习可有效解决开放词汇音频事件定位的数据稀缺问题。该工作为LALM的时间定位能力提升提供了数据侧新思路，有望推动音频理解向更精细的时空推理发展。工业上可用于智能监控、音频检索等场景。

## ⚠️ 局限与未解决问题

摘要未明确承认局限。可能的问题：1）伪标签质量依赖多模型，可能引入噪声；2）合成数据与真实数据分布差异；3）未报告推理延迟和计算开销；4）AEGBench的难度分层标准需进一步验证。

## 🔗 开源资源

- **HuggingFace**：<https://huggingface.co/datasets/zihan-audio/AEGBench>
- **数据集**：<https://huggingface.co/datasets/zihan-audio/AEGBench>

---

<div class="paper-footer"><span>评分：7.8</span><span>原始：7.8</span><a href="/audio-paper-daily/posts/2026-07-22/">← 返回 2026-07-22 速递</a></div>
