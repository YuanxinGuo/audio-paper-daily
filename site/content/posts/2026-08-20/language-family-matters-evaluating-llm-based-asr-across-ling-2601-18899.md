---
title: "Language Family Matters: Evaluating LLM-Based ASR Across Linguistic Boundaries"
date: 2026-08-20T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#语音识别"]
summary: "提出基于语言家族共享连接器的多语言ASR策略，减少参数并提升跨域泛化。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#语音识别</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#多语言ASR</span> <span class="tag-pill tag-pill-soft">#连接器共享</span> <span class="tag-pill tag-pill-soft">#语言家族</span> <span class="tag-pill tag-pill-soft">#LLM-ASR</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2601.18899</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-08-20</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2601.18899" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2601.18899" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出基于语言家族共享连接器的多语言ASR策略，减少参数并提升跨域泛化。
</div>

## 👥 作者与机构

**Yuchen Zhang** ¹ · Ravi Shekhar · Haralambos Mouratidis

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合从事多语言ASR和LLM语音结合的研究者。建议重点阅读方法部分（第3节）和实验对比（第4节），可先看表1和表2了解效果。

## 🌍 研究背景

LLM驱动的ASR系统通过轻量连接器将冻结语音编码器与预训练LLM结合，实现低资源强性能。先前工作为每种语言训练独立连接器，忽略语言间相关性，导致参数冗余且泛化受限。本文旨在利用语言家族关系共享连接器，以提升效率与泛化。

## 💡 核心创新

1. 提出基于语言家族共享连接器的策略
2. 每个语系仅需一个连接器，大幅减少参数
3. 在两种多语言LLM和两个真实语料上验证有效性
4. 跨域泛化能力提升，适用于众包语音
5. 提供可扩展的多语言ASR部署方案

## 🏗️ 模型架构

输入语音特征经冻结语音编码器提取，通过轻量连接器映射到预训练LLM的嵌入空间。连接器按语言家族共享，即同一语系的语言共用同一连接器，而非每语言独立。LLM解码输出文本。该方法适用于多种LLM架构，具体连接器类型未详述。

## 📚 数据集

- Curated speech corpus（训练/评估）
- Crowd-sourced speech corpus（训练/评估）

## 📊 实验结果

摘要未提供具体数值，但表明基于家族共享连接器在减少参数的同时，跨域泛化优于每语言独立连接器，且适用于两种多语言LLM和两个真实语料。

## 🎯 结论与影响

本文证明基于语言家族共享连接器是多语言ASR的有效策略，在降低参数开销的同时提升跨域泛化，为大规模多语言部署提供实用方案，并启发后续利用语言关系优化LLM-ASR。

## ⚠️ 局限与未解决问题

摘要未提及具体局限，但可能包括：未报告各语言细粒度性能、未与更多基线对比、未讨论语系内差异大的情况、未提供推理效率指标。

---

<div class="paper-footer"><span>评分：7.2</span><span>原始：7.2</span><a href="/audio-paper-daily/posts/2026-08-20/">← 返回 2026-08-20 速递</a></div>
