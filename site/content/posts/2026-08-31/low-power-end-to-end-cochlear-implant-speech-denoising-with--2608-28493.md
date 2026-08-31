---
title: "Low-Power End-to-End Cochlear Implant Speech Denoising with Spiking Neural Networks"
date: 2026-08-31T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#语音增强"]
summary: "提出一种受Deep ACE启发的SNN，同时进行语音增强和人工耳蜗编码，在保持VSTOI和SNRi性能的同时，能耗降低六倍以上。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#语音增强</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#脉冲神经网络</span> <span class="tag-pill tag-pill-soft">#人工耳蜗</span> <span class="tag-pill tag-pill-soft">#低功耗</span> <span class="tag-pill tag-pill-soft">#语音增强</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2608.28493</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-08-31</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
<div class="meta-row"><span class="meta-key">⭐</span><span class="meta-val focus-badge">本站重点关注领域 · 评分 +1</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2608.28493" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2608.28493" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出一种受Deep ACE启发的SNN，同时进行语音增强和人工耳蜗编码，在保持VSTOI和SNRi性能的同时，能耗降低六倍以上。
</div>

## 👥 作者与机构

**Ludovic Boulanger** ¹ · Sean U. N. Wood

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合语音增强、脉冲神经网络及低功耗可穿戴设备研究者阅读。建议重点阅读模型架构（第3节）和能耗对比部分（第4节），可先看摘要中的性能与能耗数据，再深入方法细节。

## 🌍 研究背景

人工耳蜗（CI）用户常在嘈杂环境中理解语音困难。深度神经网络（DNN）在语音增强上表现良好，但高能耗不适合低功耗CI处理器。脉冲神经网络（SNN）能以更低能耗实现相近性能。本文旨在设计一种SNN，同时完成语音增强和CI编码，解决DNN能耗高的问题。

## 💡 核心创新

1. 提出SNN架构，受Deep ACE启发，同时进行语音增强和CI编码
2. 实现六倍以上的能耗降低，同时保持VSTOI和SNRi性能
3. 端到端设计，直接输出CI编码，避免级联处理
4. 利用SNN事件驱动特性，适合低功耗硬件

## 🏗️ 模型架构

模型输入为含噪语音信号，经预处理后送入SNN主干。SNN采用受Deep ACE启发的结构，包含脉冲编码层和若干脉冲神经元层，实现语音增强和CI编码的联合优化。输出为CI刺激编码。具体网络层数、神经元类型未在摘要中详述，但强调能耗显著降低。

## 📊 实验结果

摘要中未提供具体数值，仅提及与Deep ACE相比，VSTOI和SNRi得分具有竞争力，且能耗降低六倍以上。具体实验设置、数据集和详细结果需查阅全文。

## 🎯 结论与影响

本文提出的SNN模型在人工耳蜗语音增强任务中实现了与Deep ACE相当的性能，同时能耗大幅降低，为低功耗CI处理器提供了可行方案。该工作展示了SNN在听觉假体中的潜力，可能推动SNN在更多低功耗音频处理场景的应用。

## ⚠️ 局限与未解决问题

摘要未提供详细实验对比和数据集信息，缺乏对模型泛化能力的评估。未提及推理延迟、硬件实现细节或与其他SNN方法的对比。作为审稿人，需关注其性能是否在多种噪声条件下验证，以及能耗计算是否基于实际硬件。

---

<div class="paper-footer"><span>评分：8.8</span><span>原始：7.8</span><span>+1 重点领域加权</span><a href="/audio-paper-daily/posts/2026-08-31/">← 返回 2026-08-31 速递</a></div>
