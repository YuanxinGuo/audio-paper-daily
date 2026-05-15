---
title: "TiCo: Time-Controllable Spoken Dialogue Model"
date: 2026-05-15T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#基准测试", "#强化学习", "#时间可控", "#语音对话模型", "#语音生成"]
summary: "TiCo通过引入口语时间标记和强化学习，使语音对话模型能根据时间指令生成指定时长的语音回复，在TiCo-Bench上显著降低时长误差。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero">
<div class="hero-score">
<div class="score-num">8.5</div>
<div class="score-stars">★★★★☆</div>
<div class="score-tier">前25%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#语音对话模型</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#时间可控</span> <span class="tag-pill tag-pill-soft">#语音生成</span> <span class="tag-pill tag-pill-soft">#强化学习</span> <span class="tag-pill tag-pill-soft">#基准测试</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2603.22267</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-05-15</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">🔥 强烈推荐通读</span></div>
</div>
</div>

<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2603.22267" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2603.22267" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>TiCo通过引入口语时间标记和强化学习，使语音对话模型能根据时间指令生成指定时长的语音回复，在TiCo-Bench上显著降低时长误差。
</div>

## 👥 作者与机构

**Kai-Wei Chang** ¹ · Wei-Chih Chen · En-Pei Hu · Hung-yi Lee · James Glass

**机构**：MIT · National Taiwan University

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合语音交互、对话系统研究者。建议通读，重点看§3.2（Spoken Time Markers）和§4（实验）。可先看表1对比基线。

## 🌍 研究背景

现有语音对话模型（如GPT-4o、Voicebox）能生成自然语音，但缺乏时间感知能力，无法遵循时长约束指令（如“回复约15秒”）。这在语音助手、交互代理等场景中影响交互质量。此前无专门评估时间可控性的基准。本文提出TiCo-Bench基准，并开发TiCo模型解决该问题。

## 💡 核心创新

1. 提出Spoken Time Markers（STM）嵌入生成过程，实时估计已用时间
2. 构建TiCo-Bench，首个时间可控指令跟随基准
3. 采用自生成+强化学习（可验证奖励）进行后训练，无需问答配对数据

## 🏗️ 模型架构

输入为文本指令（含时间约束）和可选上下文，主干为预训练语音对话模型（如基于Transformer的编解码器）。关键模块：在解码过程中，每隔固定帧数插入STM token（如<10.6 seconds>），由时间估计器根据已生成语音时长动态插入。输出为带STM的语音token序列，最终合成语音。参数量未提及。

## 📚 数据集

- TiCo-Bench（评估，包含多种时间约束指令）
- 自生成训练数据（后训练，由模型自身生成带STM的语音回复）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| Duration Error (秒) | TiCo-Bench | Backbone (无STM) 2.7x | **TiCo 1.0x (归一化)** | -1.7x (相对) |
| Duration Error (秒) | TiCo-Bench | 最强基线 1.6x | **1.0x (归一化)** | -0.6x (相对) |

TiCo在TiCo-Bench上将时长误差降低至基线的1/2.7，比最强基线低1.6倍，同时保持回复质量（如自然度、语义准确性）。消融实验验证了STM和强化学习的有效性。

## 🎯 结论与影响

TiCo首次实现语音对话模型的时间可控性，通过STM和强化学习有效遵循时长指令。该工作为交互式语音系统（如语音助手）提供了实用能力，未来可扩展至更细粒度的时间控制或多轮对话。

## ⚠️ 局限与未解决问题

仅评估了英文和单一说话风格；STM插入策略可能增加推理延迟；未报告参数量和计算开销；时间控制精度受限于语音合成质量。

---

<div class="paper-footer"><span>评分：8.5</span><span>原始：8.5</span><a href="/audio-paper-daily/posts/2026-05-15/">← 返回 2026-05-15 速递</a></div>
