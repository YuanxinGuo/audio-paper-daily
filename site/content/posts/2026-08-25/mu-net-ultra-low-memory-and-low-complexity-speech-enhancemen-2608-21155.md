---
title: "{\\mu}Net: Ultra-Low-Memory and Low-Complexity Speech Enhancement for Embedded Digital Signal Processors"
date: 2026-08-25T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#语音增强"]
summary: "提出μNet，一种仅需90KB内存和28MMACs的超低资源语音增强模型，支持4ms低延迟和全整数运算，性能与同复杂度SOTA相当。"
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
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#语音增强</span> <span class="tag-pill tag-pill-soft">#嵌入式DSP</span> <span class="tag-pill tag-pill-soft">#低复杂度</span> <span class="tag-pill tag-pill-soft">#整数运算</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2608.21155</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-08-25</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
<div class="meta-row"><span class="meta-key">⭐</span><span class="meta-val focus-badge">本站重点关注领域 · 评分 +1</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2608.21155" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2608.21155" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出μNet，一种仅需90KB内存和28MMACs的超低资源语音增强模型，支持4ms低延迟和全整数运算，性能与同复杂度SOTA相当。
</div>

## 👥 作者与机构

**Shrishti Saha Shetu** ¹ · Jose Miguel Martinez Aponte · Nagashree K. S. Rao · Sharvin Vittappan · Oliver Thiergart · Emanu\"el A. P. Habets

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合从事嵌入式语音增强、边缘AI部署的研究者或工程师。建议重点阅读第3节模型设计和第4节实验部分，特别是与HiFi 4/5 DSP平台的兼容性验证。可先看摘要和结论，再深入模型架构。

## 🌍 研究背景

语音增强在嵌入式DSP上部署面临内存、计算量、延迟和整数运算支持等多重约束。现有DNN方法虽各有侧重，但缺乏同时满足所有要求的统一框架。本文旨在设计一个端到端模型，在极低资源下达到实用性能，填补这一空白。

## 💡 核心创新

1. 提出μNet，实现90KB静态内存和28MMACs的超低资源占用
2. 支持4ms算法延迟，满足实时处理需求
3. 全整数运算，兼容Cadence Tensilica HiFi 4/5等消费级DSP
4. 性能与同复杂度SOTA方法相当，验证了高效设计

## 🏗️ 模型架构

μNet采用端到端DNN结构，输入为含噪语音波形，通过编码器提取特征，主干网络可能包含卷积和循环或注意力模块，但具体结构未在摘要中详述。输出为增强后的语音波形。模型设计强调低内存和低计算量，支持整数运算，适合嵌入式部署。

## 📊 实验结果

摘要未提供具体实验数据，仅说明μNet在性能上与同复杂度SOTA方法相当，并验证了在Cadence Tensilica HiFi 4/5平台上的兼容性。具体指标和数据集未提及。

## 🎯 结论与影响

μNet为嵌入式语音增强提供了超低资源解决方案，同时满足内存、计算、延迟和整数运算要求，性能不逊于同复杂度方法。该工作有望推动DNN语音增强在消费级DSP上的实际部署，为资源受限场景提供新选择。

## ⚠️ 局限与未解决问题

摘要未提供详细实验对比和消融研究，缺乏具体性能指标（如PESQ、SI-SDR）和数据集信息。未提及模型在更复杂噪声场景下的泛化能力，也未报告实际推理延迟和功耗。

---

<div class="paper-footer"><span>评分：8.8</span><span>原始：7.8</span><span>+1 重点领域加权</span><a href="/audio-paper-daily/posts/2026-08-25/">← 返回 2026-08-25 速递</a></div>
