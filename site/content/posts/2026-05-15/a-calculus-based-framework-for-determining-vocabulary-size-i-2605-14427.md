---
title: "A Calculus-Based Framework for Determining Vocabulary Size in End-to-End ASR"
date: 2026-05-15T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#语音识别"]
summary: "提出基于微积分的框架，通过曲线拟合和导数测试自动确定端到端ASR的最佳词汇量。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#语音识别</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#端到端ASR</span> <span class="tag-pill tag-pill-soft">#词汇量选择</span> <span class="tag-pill tag-pill-soft">#BPE</span> <span class="tag-pill tag-pill-soft">#LibriSpeech</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2605.14427</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-05-15</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2605.14427" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2605.14427" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出基于微积分的框架，通过曲线拟合和导数测试自动确定端到端ASR的最佳词汇量。
</div>

## 👥 作者与机构

**Sunil Kumar Kopparapu** ¹

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合ASR研究者，尤其是关注词汇量超参数调优的读者。建议重点阅读§3方法部分和§4实验部分，了解曲线拟合和导数测试的具体应用。可先看表1对比结果。

## 🌍 研究背景

端到端ASR系统的词汇量（token数量）是重要超参数，但现有方法如BPE、WordPiece需手动设定，缺乏理论指导。近期工作[1]提出了代价函数框架，但未给出自动确定方法。本文旨在通过微积分原理自动估计最优词汇量。

## 💡 核心创新

1. 提出基于曲线拟合的词汇量-性能关系建模
2. 利用一阶和二阶导数测试确定最优词汇量
3. 在LibriSpeech上验证方法有效性

## 🏗️ 模型架构

输入为不同词汇量下的ASR性能指标（如WER），通过曲线拟合得到连续函数，然后应用一阶导数（临界点）和二阶导数（凹凸性）测试确定最优词汇量。不涉及具体ASR模型架构。

## 📚 数据集

- LibriSpeech（训练和评估）

## 📊 实验结果

摘要未提供具体数值结果，仅说明在LibriSpeech上应用该方法能提升ASR性能。需阅读全文获取详细指标。

## 🎯 结论与影响

本文提出了一种基于微积分的词汇量确定框架，通过曲线拟合和导数测试自动选择最优词汇量，避免了手动调参。该方法有望为端到端ASR系统提供理论指导，简化超参数选择过程。

## ⚠️ 局限与未解决问题

仅在一个数据集（LibriSpeech）上验证，泛化性未知；未与多种tokenization算法对比；未讨论计算开销；曲线拟合的精度可能影响结果。

---

<div class="paper-footer"><span>评分：6.5</span><span>原始：6.5</span><a href="/audio-paper-daily/posts/2026-05-15/">← 返回 2026-05-15 速递</a></div>
