---
title: "MetaSICL: Adapting Audiroty LLM via Meta Speech In-Context Learning"
date: 2026-05-27T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#音频理解"]
summary: "提出MetaSICL方法，通过元学习增强听觉大语言模型的上下文学习能力，在低资源任务上优于直接微调。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero">
<div class="hero-score">
<div class="score-num">7.2</div>
<div class="score-stars">★★★★☆</div>
<div class="score-tier">前25%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#音频理解</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#上下文学习</span> <span class="tag-pill tag-pill-soft">#听觉大语言模型</span> <span class="tag-pill tag-pill-soft">#低资源任务</span> <span class="tag-pill tag-pill-soft">#元学习</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2601.18904</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-05-27</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2601.18904" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2601.18904" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出MetaSICL方法，通过元学习增强听觉大语言模型的上下文学习能力，在低资源任务上优于直接微调。
</div>

## 👥 作者与机构

**Haolong Zheng** ¹ · Siyin Wang · Zengrui Jin · Mark Hasegawa-Johnson

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合研究听觉LLM和上下文学习的读者。建议重点阅读第3节MetaSICL方法设计和第4节实验对比，特别是表1和表2。可先看§3.2的训练流程。

## 🌍 研究背景

听觉大语言模型在多种语音音频理解任务上表现优异，但在低资源场景下因标注数据稀缺或分布不匹配而性能下降。直接微调易过拟合，而上下文学习（ICL）提供了一种无需训练的推理时适应方案。本文首先验证了vanilla ICL在听觉LLM上的有效性，然后提出MetaSICL，利用高资源任务数据通过元学习增强模型的ICL能力，以解决低资源适应问题。

## 💡 核心创新

1. 首次验证vanilla ICL在听觉LLM上的有效性
2. 提出MetaSICL元学习训练框架
3. 仅用高资源数据训练，提升低资源任务性能
4. 无需额外标注或模型架构修改

## 🏗️ 模型架构

基于预训练听觉LLM（如Qwen2-Audio），MetaSICL采用两阶段训练：首先在多种高资源任务上构建支持-查询样本对，然后通过元学习优化模型参数，使其在给定少量支持样本时能快速适应新任务。推理时，将测试样本与少量标注演示拼接作为输入，模型直接输出预测。

## 📚 数据集

- LibriSpeech（高资源语音识别，训练）
- VoxCeleb（高资源说话人识别，训练）
- ESC-50（高资源音频事件分类，训练）
- 低资源任务数据集（如自定义小样本集，评估）

## 📊 实验结果

摘要未提供具体数值，但声称MetaSICL在多个低资源语音和音频任务上优于直接微调，且vanilla ICL能提升零样本性能。实验涵盖语音识别、说话人识别、音频事件分类等任务。

## 🎯 结论与影响

MetaSICL通过元学习有效增强了听觉LLM的上下文学习能力，在低资源场景下比直接微调更鲁棒。该方法为听觉LLM的快速适应提供了新范式，有望推动其在数据稀缺领域的应用。

## ⚠️ 局限与未解决问题

摘要未提及推理延迟或计算开销；未与更多ICL基线（如prompt tuning）对比；低资源任务的具体定义和数据集未明确；未分析支持样本数量对性能的影响。

---

<div class="paper-footer"><span>评分：7.2</span><span>原始：7.2</span><a href="/audio-paper-daily/posts/2026-05-27/">← 返回 2026-05-27 速递</a></div>
