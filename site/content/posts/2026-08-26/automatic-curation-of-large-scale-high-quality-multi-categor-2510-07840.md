---
title: "Automatic Curation of Large-Scale, High-Quality, Multi-Category Music Source Separation Dataset"
date: 2026-08-26T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#乐器分离"]
summary: "提出ACMID大规模多类别音乐源分离数据集，通过自动清洗提升数据质量，扩展至7-stem分离，显著提升SOTA模型性能。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#乐器分离</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#数据集构建</span> <span class="tag-pill tag-pill-soft">#数据清洗</span> <span class="tag-pill tag-pill-soft">#预训练音频编码器</span> <span class="tag-pill tag-pill-soft">#多类别分离</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2510.07840</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-08-26</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
<div class="meta-row"><span class="meta-key">⭐</span><span class="meta-val focus-badge">本站重点关注领域 · 评分 +1</span></div>
</div>
</div>

<div class="opensource-banner"><div class="oc-headline"><span class="oc-pulse"></span><span class="oc-title">本论文已开源</span><span class="oc-hint">点击下方卡片直达对应资源</span></div><div class="oc-grid"><a class="oc-chip oc-chip-code" href="https://github.com/scottishfold0621/ACMID" target="_blank" rel="noopener"><span class="oc-icon">💻</span><span class="oc-text"><span class="oc-label">代码仓库</span><span class="oc-sub">scottishfold0621/ACMID</span></span></a></div></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2510.07840" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2510.07840" target="_blank" rel="noopener">📑 PDF</a><a class="rsrc rsrc-code" href="https://github.com/scottishfold0621/ACMID" target="_blank" rel="noopener">💻 代码</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出ACMID大规模多类别音乐源分离数据集，通过自动清洗提升数据质量，扩展至7-stem分离，显著提升SOTA模型性能。
</div>

## 👥 作者与机构

**Ji Yu** ¹ · Yang shuo · Xu Yuetonghui · Liu Mengmei · Ji Qiang · Han Zerui

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合音乐源分离、数据挖掘与自动标注方向的研究者。建议重点阅读第3节（数据清洗流程）与第4节（实验对比），可先看表2与图3了解性能提升。若关注数据工程，可细读清洗模型设计。

## 🌍 研究背景

当前音乐源分离（MSS）依赖监督学习，受限于训练数据的数量与质量。网络爬取可获取大量数据，但平台级标签常与音频内容不匹配，导致难以获得准确的音频-标签对。现有数据集如MUSDB18规模有限，且多为4-stem分类。本文旨在通过自动清洗构建大规模、高质量、多类别（7-stem）的MSS数据集，以提升分离性能。

## 💡 核心创新

1. 提出ACMID数据集，基于网络爬取与自动清洗构建大规模多类别MSS数据
2. 利用预训练音频编码器构建乐器分类器，自动过滤并聚合干净片段
3. 将MSS从4-stem扩展至7-stem（钢琴、鼓、贝斯、原声吉他、电吉他、弦乐、管乐）
4. 公开数据爬取与清洗代码及模型权重，促进可复现研究

## 🏗️ 模型架构

数据清洗流程：输入爬取的原始音频轨道，通过预训练音频编码器（如CLAP）提取特征，送入乐器分类器（如线性分类头）判断音频片段是否包含目标乐器且干净，过滤后聚合为ACMID-Cleaned。MSS模型采用SOTA架构（如HTDemucs或BSRNN），输入混合音频，输出7个stem的估计。

## 📚 数据集

- ACMID-Uncleaned（网络爬取原始数据，用于对比清洗效果）
- ACMID-Cleaned（自动清洗后的数据集，用于训练MSS模型）
- MUSDB18（评估，用于与现有方法对比）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| SDR (dB) | MUSDB18 | 使用ACMID-Uncleaned训练的模型（具体值未给出） | **使用ACMID-Cleaned训练的模型（具体值未给出）** | +2.39 dB |
| 平均SDR (dB) | MUSDB18 | 仅使用MUSDB18训练的模型（具体值未给出） | **加入ACMID-Cleaned训练的模型（具体值未给出）** | +1.16 dB |

实验表明，使用ACMID-Cleaned训练的MSS模型相比使用未清洗数据训练的模型，SDR提升2.39dB，验证了清洗流程的有效性。将ACMID-Cleaned加入训练后，模型平均性能提升1.16dB，证明数据集的价值。但摘要未提供具体基线值，也未提及消融实验或跨数据集泛化结果。

## 🎯 结论与影响

本文构建了大规模多类别音乐源分离数据集ACMID，通过自动清洗显著提升数据质量，并扩展至7-stem分离，为MSS研究提供了更丰富的数据资源。该数据集有望推动高粒度分离技术的发展，对音乐制作、混音等工业应用具有潜在价值。

## ⚠️ 局限与未解决问题

摘要未提及清洗流程的局限性，如分类器误差可能引入噪声；未报告清洗后数据规模与原始数据比例；未与其他清洗方法对比；未提供推理效率或训练成本；实验仅基于单一SOTA模型，泛化性待验证。

## 🔗 开源资源

- **代码**：<https://github.com/scottishfold0621/ACMID>

---

<div class="paper-footer"><span>评分：8.8</span><span>原始：7.8</span><span>+1 重点领域加权</span><a href="/audio-paper-daily/posts/2026-08-26/">← 返回 2026-08-26 速递</a></div>
