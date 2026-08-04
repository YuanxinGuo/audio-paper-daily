---
title: "AST: Adaptive, Seamless, and Training-Free Precise Speech Editing"
date: 2026-08-04T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#语音编辑"]
summary: "提出AST框架，基于预训练TTS实现无需训练的精准语音编辑，通过潜在重组和自适应弱引导提升保真度与自然度。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero">
<div class="hero-score">
<div class="score-num">8.2</div>
<div class="score-stars">★★★★☆</div>
<div class="score-tier">前25%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#语音编辑</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#语音编辑</span> <span class="tag-pill tag-pill-soft">#零样本</span> <span class="tag-pill tag-pill-soft">#无需训练</span> <span class="tag-pill tag-pill-soft">#语音合成</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2604.16056</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-08-04</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2604.16056" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2604.16056" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出AST框架，基于预训练TTS实现无需训练的精准语音编辑，通过潜在重组和自适应弱引导提升保真度与自然度。
</div>

## 👥 作者与机构

**Sihan Lv** ¹ · Yechen Jin · Zhen Li · Jintao Chen · Jinshan Zhang · Ying Li · Jianwei Yin · Meng Xi

**机构**：浙江大学 · 阿里巴巴达摩院

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合语音编辑、TTS和语音处理研究者阅读。建议重点阅读第3节方法部分（潜在重组与AWFG）以及第4节实验中的表2和表3，对比不同方法在保真度和自然度上的表现。可先看摘要和结论快速了解贡献。

## 🌍 研究背景

文本语音编辑旨在修改特定片段同时保持说话人身份和声学上下文。现有方法分为任务特定训练和TTS适配两类，前者易降低未编辑区域保真度，后者在自然度和时间保真度间存在权衡。本文旨在解决这些挑战，提出无需训练的AST框架，利用潜在重组和自适应弱引导实现高质量编辑。

## 💡 核心创新

1. 提出潜在重组（Latent Recomposition）拼接保留源片段与合成目标，保证未编辑区域保真度
2. 引入自适应弱引导（AWFG）调节mel空间信号，实现无缝边界过渡且不破坏生成流形
3. 构建LibriSpeech-Edit数据集和WDTW指标，填补时间保真度评估空白
4. 实现零样本语音编辑，无需任务特定训练或配对数据

## 🏗️ 模型架构

AST基于预训练TTS构建。输入为源语音和编辑文本，通过TTS编码器生成潜在表示。潜在重组模块将源语音中未编辑部分的潜在表示与合成目标的潜在表示拼接，确保保真度。AWFG模块在mel空间对拼接处进行自适应弱引导，平滑边界。最后通过TTS解码器输出编辑后的语音。

## 📚 数据集

- LibriSpeech-Edit（评估，新构建，用于时间保真度评估）
- LibriSpeech（训练/评估，用于TTS预训练和编辑评估）

## 📊 实验结果

摘要未提供具体数值，但声称AST在内容准确性、感知质量、说话人保持和时间保真度上一致优于现有任务特定和微调方法，并达到SOTA零样本性能。具体指标和数据集细节需查阅论文。

## 🎯 结论与影响

AST通过潜在重组和AWFG有效解决了语音编辑中保真度与自然度的权衡，无需任务特定训练即可实现SOTA零样本编辑。该工作为语音编辑提供了新范式，有望推动TTS在内容编辑中的应用，降低定制化编辑成本。

## ⚠️ 局限与未解决问题

作者未明确提及局限，但作为审稿人可见：实验对比可能缺乏最新基线；未报告推理延迟和计算开销；LibriSpeech-Edit数据集和WDTW指标需进一步验证其普适性；对复杂声学场景（如噪声、多说话人）的鲁棒性未知。

---

<div class="paper-footer"><span>评分：8.2</span><span>原始：8.2</span><a href="/audio-paper-daily/posts/2026-08-04/">← 返回 2026-08-04 速递</a></div>
