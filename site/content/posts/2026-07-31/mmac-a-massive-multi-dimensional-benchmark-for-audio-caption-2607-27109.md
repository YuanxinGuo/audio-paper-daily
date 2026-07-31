---
title: "MMAC: A Massive Multi-dimensional Benchmark for Audio Captioning"
date: 2026-07-31T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#音频字幕生成"]
summary: "提出大规模多维音频字幕生成基准MMAC，含5638个音频片段，覆盖6大能力类别和15个评估维度，用于诊断模型生成字幕的信息覆盖与描述可靠性。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#音频字幕生成</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#音频字幕生成</span> <span class="tag-pill tag-pill-soft">#评测基准</span> <span class="tag-pill tag-pill-soft">#音频大语言模型</span> <span class="tag-pill tag-pill-soft">#信息覆盖</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2607.27109</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-07-31</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2607.27109" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2607.27109" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出大规模多维音频字幕生成基准MMAC，含5638个音频片段，覆盖6大能力类别和15个评估维度，用于诊断模型生成字幕的信息覆盖与描述可靠性。
</div>

## 👥 作者与机构

**Weijie Wu** ¹ · Junbo Li · Lin Li · Jun Fang · Qingyang Hong

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合音频字幕生成、音频大语言模型评测方向的研究者阅读。建议重点阅读第3节（基准构建）和第4节（评估结果），可先看表1和表2了解维度划分。若关注评测方法，可精读第3.2节。

## 🌍 研究背景

随着音频大语言模型（AudioLLMs）的发展，音频字幕生成需要从简短描述转向开放、细粒度的自由文本。现有评测多关注生成质量或任务性能，难以诊断信息覆盖和描述可靠性。本文提出MMAC基准，旨在系统评估模型生成字幕的信息覆盖和一致性，填补该领域评测空白。

## 💡 核心创新

1. 构建大规模多维基准，含5638个音频片段，覆盖20+数据源
2. 定义6大能力类别和15个评估维度，细粒度评测
3. 提出信息覆盖与描述可靠性双重评估机制
4. 系统评估开源与专有AudioLLMs，揭示维度差异
5. 将公开基准与评估代码，促进社区发展

## 🏗️ 模型架构

MMAC为评测基准，非模型架构。包含音频片段集、参考标签、评估协议。评估时，给定模型生成字幕，检查是否提及目标维度相关信息，并验证与参考标签的一致性。

## 📚 数据集

- MMAC基准（包含5638个音频片段，来自20+数据源，用于评估）

## 📊 实验结果

摘要未提供具体数值结果，仅提及评估了代表性开源和专有AudioLLMs，结果显示不同评估维度、信息覆盖和描述可靠性存在明显差异。具体指标和对比数据待论文正文。

## 🎯 结论与影响

MMAC为音频字幕生成提供了大规模多维评测基准，能有效诊断模型在信息覆盖和描述可靠性方面的不足。该基准有望推动音频字幕生成向更开放、细粒度的方向发展，并为AudioLLMs的评估提供新标准。对工业界而言，可用于模型选型和改进。

## ⚠️ 局限与未解决问题

摘要未提及局限。可能存在的问题：基准构建的音频来源多样性是否均衡，评估维度是否覆盖所有关键方面，以及人工评估与自动评估的一致性未说明。此外，未提供与现有基准的对比分析。

---

<div class="paper-footer"><span>评分：7.8</span><span>原始：7.8</span><a href="/audio-paper-daily/posts/2026-07-31/">← 返回 2026-07-31 速递</a></div>
