---
title: "Few-Shot Contrastive Adaptation for Audio Abuse Detection in Low-Resource Indic Languages"
date: 2026-08-03T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#音频分类"]
summary: "本文研究利用CLAP音频表示直接检测低资源印度语言的辱骂性语音，无需转录，少量标注即可接近全监督性能。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero hero-focus">
<div class="hero-score">
<div class="score-num">8.2</div>
<div class="score-stars">★★★★☆</div>
<div class="score-tier">前25%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#音频分类</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#语音增强</span> <span class="tag-pill tag-pill-soft">#少样本学习</span> <span class="tag-pill tag-pill-soft">#跨语言</span> <span class="tag-pill tag-pill-soft">#CLAP</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2604.09094</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-08-03</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
<div class="meta-row"><span class="meta-key">⭐</span><span class="meta-val focus-badge">本站重点关注领域 · 评分 +1</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2604.09094" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2604.09094" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>本文研究利用CLAP音频表示直接检测低资源印度语言的辱骂性语音，无需转录，少量标注即可接近全监督性能。
</div>

## 👥 作者与机构

**Aditya Narayan Sankaran** ¹ · Reza Farahbakhsh · Noel Crespi

**机构**：巴黎萨克雷大学 · IMT Atlantique

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合音频分类、少样本学习和跨语言研究的读者。建议重点阅读第3节（方法）和第4节（实验），特别是表2和表3，了解CLAP表示在不同语言上的表现。可先看摘要和结论，再深入实验部分。

## 🌍 研究背景

辱骂性语音在语音笔记、电话和短视频中日益增多，但现有检测系统通常先转录再分类，对于缺乏强语音识别器的低资源语言，转录不可靠且丢失语气和情感。本文探索直接基于音频检测辱骂性语音，利用CLAP模型学习的声音-语言共享表示，在ADIMA数据集的十种印度语言上评估，旨在减少对标注数据的依赖。

## 💡 核心创新

1. 利用CLAP预训练表示进行零样本和少样本辱骂检测
2. 系统评估跨十种印度语言的泛化能力
3. 对比轻量分类器与全监督系统的性能差距
4. 分析少量标注样本适配的收益与不稳定性

## 🏗️ 模型架构

输入音频通过CLAP模型提取音频表示，然后训练一个轻量级分类器（如线性层或MLP）进行二分类（辱骂/非辱骂）。CLAP模型本身不进行微调，仅利用其预训练表示。分类器在少量标注样本上训练，评估零样本和少样本场景。

## 📚 数据集

- ADIMA（评估，十种印度语言）

## 📊 实验结果

摘要中未提供具体数值指标，但提到轻量分类器在CLAP表示上接近全监督系统（差距1-3个百分点），且远优于无标注的提示方法。少样本适配带来的额外收益有限且跨语言不稳定。

## 🎯 结论与影响

CLAP音频表示为跨语言辱骂检测提供了强且廉价的基线，降低了实际应用中对标注数据的需求。该工作表明预训练音频-语言模型可直接用于音频分类任务，对低资源语言的音频内容审核有潜在价值，但少样本适配的收益有限，需进一步研究。

## ⚠️ 局限与未解决问题

摘要未提及具体局限，但可推测：仅评估了CLAP一种模型，未与其他音频表示对比；少样本适配效果不稳定，缺乏深入分析；未报告计算成本或推理延迟；数据集ADIMA的规模和标注质量未知。

---

<div class="paper-footer"><span>评分：8.2</span><span>原始：7.2</span><span>+1 重点领域加权</span><a href="/audio-paper-daily/posts/2026-08-03/">← 返回 2026-08-03 速递</a></div>
