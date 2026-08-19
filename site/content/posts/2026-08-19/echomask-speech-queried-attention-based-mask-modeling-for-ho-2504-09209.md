---
title: "EchoMask: Speech-Queried Attention-based Mask Modeling for Holistic Co-Speech Motion Generation"
date: 2026-08-19T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#共语手势生成"]
summary: "提出基于语音查询注意力的掩码建模框架，通过运动-音频对齐和选择性掩码提升共语手势生成质量。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#共语手势生成</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#掩码建模</span> <span class="tag-pill tag-pill-soft">#跨模态对齐</span> <span class="tag-pill tag-pill-soft">#注意力机制</span> <span class="tag-pill tag-pill-soft">#手势生成</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2504.09209</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-08-19</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2504.09209" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2504.09209" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出基于语音查询注意力的掩码建模框架，通过运动-音频对齐和选择性掩码提升共语手势生成质量。
</div>

## 👥 作者与机构

**Xiangyue Zhang** ¹ · Jianfang Li · Jiaxu Zhang · Jianqiang Ren · Liefeng Bo · Zhigang Tu

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合从事共语手势生成、跨模态生成的研究者。建议重点阅读第3节的MAM和SQA模块，以及第4节的实验对比。可先看§3.2和表2，了解核心创新。

## 🌍 研究背景

共语手势生成旨在根据语音生成自然协调的手势，是虚拟人、人机交互等领域的关键技术。现有方法多采用掩码建模，但难以识别语义重要的运动帧进行有效掩码。此前SOTA方法如DiffGesture、Trimodal等虽能生成手势，但缺乏对语音-运动对齐的精细建模，导致生成的手势节奏和语义表达不足。本文旨在通过语音引导的注意力掩码，实现更精准的运动掩码和生成。

## 💡 核心创新

1. 提出运动-音频对齐模块(MAM)，构建潜在联合空间
2. 设计语音查询注意力机制(SQA)，计算帧级注意力分数
3. 利用高注意力分数引导选择性掩码，聚焦语义帧
4. 将运动对齐语音特征注入生成网络，提升生成质量

## 🏗️ 模型架构

输入为语音特征和运动序列。首先通过MAM模块将语音特征投影到运动-音频联合空间，使用可学习的语音查询获得运动对齐的语音表示。然后SQA模块通过运动键和语音查询的交互计算帧级注意力分数，指导掩码选择高注意力帧。最后，运动对齐的语音特征和掩码后的运动序列输入生成网络（如Transformer或扩散模型）生成完整运动。

## 📊 实验结果

摘要中未提供具体数值指标，仅提及定性定量评估优于现有SOTA。具体指标如FGD、BC等未给出，无法进行数值对比。

## 🎯 结论与影响

本文通过语音查询注意力掩码建模，有效提升了共语手势生成的质量，尤其在节奏和语义表达方面。该方法为跨模态生成提供了新思路，未来可扩展到其他运动生成任务。对虚拟人、游戏动画等工业应用具有潜在价值。

## ⚠️ 局限与未解决问题

摘要未提及局限，但可推测：未提供具体指标和消融实验，缺乏与更多SOTA的对比；可能依赖大规模配对数据，泛化性待验证；未讨论推理效率。

---

<div class="paper-footer"><span>评分：7.8</span><span>原始：7.8</span><a href="/audio-paper-daily/posts/2026-08-19/">← 返回 2026-08-19 速递</a></div>
