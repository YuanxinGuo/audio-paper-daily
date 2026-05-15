---
title: "Streaming Speech-to-Text Translation with a SpeechLLM"
date: 2026-05-15T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#语音翻译"]
summary: "提出一种基于LLM的流式语音到文本翻译系统，模型自主决定何时输出翻译，延迟仅1-2秒，翻译质量接近非流式基线。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#语音翻译</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#流式处理</span> <span class="tag-pill tag-pill-soft">#大语言模型</span> <span class="tag-pill tag-pill-soft">#端到端</span> <span class="tag-pill tag-pill-soft">#语音翻译</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2605.14766</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-05-15</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2605.14766" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2605.14766" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出一种基于LLM的流式语音到文本翻译系统，模型自主决定何时输出翻译，延迟仅1-2秒，翻译质量接近非流式基线。
</div>

## 👥 作者与机构

**Titouan Parcollet** ¹ · Shucong Zhang · Xianrui Zheng · Rogier C. van Dalen

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合语音翻译、流式处理、SpeechLLM方向的研究者。建议重点阅读§3（模型架构与训练策略）和§4（实验结果与延迟分析），可对比现有流式方案。

## 🌍 研究背景

传统语音翻译系统通常级联ASR和文本翻译模块，存在级联误差且无法利用副语言信息。SpeechLLM将两者合并，但现有系统要么等待完整语句，要么固定间隔输出，不适用于实时场景。本文旨在实现真正的流式语音翻译，让LLM自主决定何时输出，同时保持翻译质量。

## 💡 核心创新

1. LLM自主决策输出时机，无需固定间隔
2. 利用语音-文本对齐进行训练
3. 流式架构实现1-2秒低延迟

## 🏗️ 模型架构

输入语音特征序列，通过编码器映射为连续表示，送入LLM。LLM不仅生成输出文本token，还通过一个额外的决策头判断是否已收集足够音频来输出当前token。训练时使用强制对齐将输入语音帧与输出文本token对应，使模型学习何时输出。推理时流式处理，逐帧输入，模型自主决定输出。

## 📚 数据集

- CoVoST 2（多语言语音翻译数据集，训练与评估）
- MuST-C（多语言语音翻译数据集，训练与评估）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| BLEU | CoVoST 2 En→De | 非流式基线（如S2T-Transformer） | **接近非流式基线** | 未明确数值 |
| 延迟（秒） | CoVoST 2 En→De | 非流式基线（完整语句后输出） | **1-2** | 显著降低 |

在多个语言对上，所提流式系统翻译质量（BLEU）接近非流式基线，但延迟从数秒降至1-2秒。实验未提供具体BLEU数值，但声称接近。未报告消融实验或效率指标。

## 🎯 结论与影响

本文证明LLM可以学习自主决策输出时机，实现低延迟流式语音翻译，同时保持翻译质量。该工作为实时语音翻译系统提供了新范式，有望推动SpeechLLM在工业场景中的落地。

## ⚠️ 局限与未解决问题

未提供具体BLEU数值，仅称“接近”，缺乏量化对比；未报告模型参数量、推理速度等效率指标；仅验证了部分语言对，泛化性待考；未与现有流式方法（如Wait-k策略）直接对比。

---

<div class="paper-footer"><span>评分：7.8</span><span>原始：7.8</span><a href="/audio-paper-daily/posts/2026-05-15/">← 返回 2026-05-15 速递</a></div>
