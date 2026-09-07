---
title: "PRISM-Bench: An Audio-Centric Diagnostic Benchmark for Text-to-Audio-Video Generation"
date: 2026-09-07T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#音视频生成评估"]
summary: "提出首个以音频为中心的文本到音视频生成诊断基准PRISM-Bench，通过双轴分类和35项细粒度标准，系统评估生成系统的音频能力。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#音视频生成评估</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#文本到音视频生成</span> <span class="tag-pill tag-pill-soft">#诊断基准</span> <span class="tag-pill tag-pill-soft">#多模态评估</span> <span class="tag-pill tag-pill-soft">#MLLM-as-a-Judge</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2609.04867</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-09-07</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2609.04867" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2609.04867" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出首个以音频为中心的文本到音视频生成诊断基准PRISM-Bench，通过双轴分类和35项细粒度标准，系统评估生成系统的音频能力。
</div>

## 👥 作者与机构

**Yuchen Sun** ¹ · Qian Yang · Jun Wang · Detai Xin · Guoqiao Yu · Guanglu Wan · Qi Jia

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合从事音视频生成、多模态评估的研究者阅读。建议重点阅读第3节（基准设计）和第4节（评估协议），了解其双轴分类和MLLM评判方法。可先看表1和表2了解基准概览和评估结果。

## 🌍 研究背景

文本到音视频（T2AV）生成发展迅速，但现有评估低估音频模态，要么将音频视为视频质量的附属，要么孤立评估音频而忽略视听关联，难以诊断系统在音频生成上的真实成败。PRISM-Bench旨在填补这一空白，提供首个以音频为中心的诊断基准。

## 💡 核心创新

1. 首个音频中心T2AV诊断基准，双轴分解音频类型与声源可见性
2. 35项细粒度标准覆盖四个感知维度，全面评估生成音频
3. 采用盲测、并排对比的增强MLLM-as-a-Judge协议，与人类评分高度一致
4. 揭示前沿与开源模型在音频生成上的显著差距，及过度拟合感知保真度问题

## 🏗️ 模型架构

PRISM-Bench是一个评估基准，而非生成模型。其核心包括：1) 数据集：900个人工验证样本，按音频类型（语音、音乐、声音）和声源可见性（屏上/屏外）双轴分类；2) 评估维度：视听一致性、音频质量、音频表现力、提示遵循，共35个细粒度标准；3) 评估协议：采用盲测、并排对比的MLLM-as-a-Judge方法，与真实参考对比，确保可靠性。

## 📚 数据集

- PRISM-Bench数据集（900个人工验证样本，用于评估）

## 📊 实验结果

摘要未提供具体数值结果，但提到评估了近期T2AV系统，发现前沿与开源模型间存在显著性能差距，且当前生成范式过度拟合感知保真度，在复杂接地和控制任务（尤其是音乐生成和屏上音频同步）上表现不佳。

## 🎯 结论与影响

PRISM-Bench为T2AV生成提供了首个音频中心诊断基准，通过细粒度评估揭示现有系统在音频生成上的短板，特别是音乐和屏上音频同步。该基准有望推动T2AV评估标准化，引导研究关注音频模态的真实质量，对工业界模型迭代具有参考价值。

## ⚠️ 局限与未解决问题

摘要未提及局限。可能的问题包括：基准规模有限（900样本），可能不足以覆盖所有场景；MLLM评判虽与人类高度一致，但仍可能存在偏差；未提供与其他评估基准的对比，难以衡量其优势；未讨论基准在跨语言或跨文化场景的适用性。

---

<div class="paper-footer"><span>评分：7.8</span><span>原始：7.8</span><a href="/audio-paper-daily/posts/2026-09-07/">← 返回 2026-09-07 速递</a></div>
