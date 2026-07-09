---
title: "Rag Classification of Tagore Songs using Symbolic Music Notation and Novel Weighted Distance Measures"
date: 2026-07-09T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#音乐分类"]
summary: "利用符号音乐符号和加权距离度量对泰戈尔歌曲进行拉格分类，提出加权欧氏距离提升分类性能。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero">
<div class="hero-score">
<div class="score-num">6.5</div>
<div class="score-stars">★★★☆☆</div>
<div class="score-tier">前50%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#音乐分类</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#拉格分类</span> <span class="tag-pill tag-pill-soft">#符号音乐</span> <span class="tag-pill tag-pill-soft">#加权距离度量</span> <span class="tag-pill tag-pill-soft">#泰戈尔歌曲</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2607.07241</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-07-09</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2607.07241" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2607.07241" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>利用符号音乐符号和加权距离度量对泰戈尔歌曲进行拉格分类，提出加权欧氏距离提升分类性能。
</div>

## 👥 作者与机构

**Chandan Misra** ¹ · Swarup Chattopadhyay

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合音乐信息检索和计算音乐学领域的研究者阅读。可重点看第3节加权距离度量的定义和第4节实验对比。建议先看表1的分类结果。

## 🌍 研究背景

拉格是印度古典音乐的核心旋律框架，泰戈尔歌曲融合多种音乐传统，但拉格标注常不严格遵循古典规则，导致自动分类困难。现有方法多依赖音频特征，但缺乏大规模标注音频数据集。本文利用符号音乐符号（Swarabitan）构建标注数据集，将拉格分类视为监督分类问题，探索距离度量方法。

## 💡 核心创新

1. 构建了泰戈尔歌曲的拉格标注符号数据集
2. 提出加权欧氏距离，强调arohana和avarohana特征序列
3. 在k近邻框架下验证加权距离的有效性

## 🏗️ 模型架构

输入为符号音乐表示（音符序列），提取特征向量（可能包含音高、时长等）。采用k近邻分类器，距离度量包括欧氏距离、余弦相似度和提出的加权欧氏距离。加权欧氏距离对属于arohana和avarohana特征序列的音符赋予更高权重。输出为拉格类别标签。

## 📚 数据集

- Swarabitan符号数据集（训练/评估，包含泰戈尔歌曲的拉格标注符号）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| 分类准确率 | Swarabitan符号数据集 | 欧氏距离（值未明确给出） | **加权欧氏距离（值未明确给出）** | 提升（具体数值未给出） |

摘要未给出具体数值，仅说明加权欧氏距离在k近邻框架下提升了拉格分类性能，能更好捕捉拉格特有的旋律特征。

## 🎯 结论与影响

本文证明符号音乐表示和加权距离度量可有效用于泰戈尔歌曲的拉格分类，为缺乏音频数据的音乐分类任务提供了新思路。后续可探索更复杂的分类器或融合音频特征。

## ⚠️ 局限与未解决问题

数据集规模未明确，可能较小；仅使用k近邻分类器，未与深度学习等方法对比；未报告分类准确率具体数值；未讨论跨数据集泛化能力。

---

<div class="paper-footer"><span>评分：6.5</span><span>原始：6.5</span><a href="/audio-paper-daily/posts/2026-07-09/">← 返回 2026-07-09 速递</a></div>
