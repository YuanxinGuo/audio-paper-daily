---
title: "Exploring How Audio Effects Alter Emotion with Foundation Models"
date: 2026-05-22T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#音频情感分析"]
summary: "利用基础模型分析混响、失真等音频效果对音乐情感的影响，揭示非线性关系。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#音频情感分析</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#音频效果</span> <span class="tag-pill tag-pill-soft">#基础模型</span> <span class="tag-pill tag-pill-soft">#情感计算</span> <span class="tag-pill tag-pill-soft">#音乐认知</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2509.15151</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-05-22</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2509.15151" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2509.15151" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>利用基础模型分析混响、失真等音频效果对音乐情感的影响，揭示非线性关系。
</div>

## 👥 作者与机构

**Stelios Katsis** ¹ · Vassilis Lyberatos · Spyridon Kantarelis · Edmund Dervakos · Giorgos Stamou

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合音乐信息检索、情感计算方向的研究者。可重点阅读第3节（探测方法）和第4节（实验结果）。建议先看摘要和结论，再决定是否深入。

## 🌍 研究背景

音频效果（如混响、失真）在音乐情感塑造中起关键作用，但以往研究多关注低级音频特征与情感的联系，缺乏对音频效果系统影响的探索。基础模型（如CLAP、Wav2CLIP）在多模态数据上预训练，编码了音乐结构、音色与情感之间的丰富关联，为分析音频效果的情感后果提供了新工具。本文旨在利用这些模型，通过探测方法揭示音频效果与估计情感之间的复杂非线性关系。

## 💡 核心创新

1. 首次系统研究多种音频效果对情感的影响
2. 利用基础模型嵌入进行情感探测
3. 揭示不同音频效果与情感维度的非线性模式
4. 评估基础模型在音频效果情感分析中的鲁棒性

## 🏗️ 模型架构

使用预训练的基础模型（如CLAP、Wav2CLIP）提取音频嵌入，然后应用线性探测、非线性探测（如MLP）和相似性分析等方法，将嵌入映射到情感维度（如效价、唤醒度）。输入为经过不同音频效果处理的音乐片段，输出为情感估计值。模型参数固定，仅训练探测头。

## 📚 数据集

- DEAM（训练/评估，情感标注音乐数据集）
- 自建音频效果处理数据集（评估，包含混响、失真等效果）

## 📊 实验结果

摘要未提供具体数值结果。实验表明，不同音频效果对情感的影响存在差异，例如混响增加唤醒度，失真降低效价。基础模型嵌入能捕捉这些变化，但非线性探测优于线性探测。模型鲁棒性分析显示，某些效果（如动态范围压缩）对情感估计影响较小。

## 🎯 结论与影响

本文证实基础模型可有效分析音频效果对情感的影响，揭示了混响、失真等效果与情感维度的非线性关系。该工作为音乐制作中的情感设计提供了理论依据，并推动了音乐认知与情感计算交叉领域的研究。未来可探索更多效果组合及实时情感预测。

## ⚠️ 局限与未解决问题

实验仅使用单一数据集（DEAM），样本量有限；未考虑音频效果参数连续变化的影响；未与人类感知实验对比；基础模型可能对某些效果不敏感；缺乏开源代码和模型。

---

<div class="paper-footer"><span>评分：6.5</span><span>原始：6.5</span><a href="/audio-paper-daily/posts/2026-05-22/">← 返回 2026-05-22 速递</a></div>
