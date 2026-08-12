---
title: "SpotSound: Enhancing Large Audio-Language Models with Fine-Grained Temporal Grounding"
date: 2026-08-12T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#音频事件定位"]
summary: "SpotSound 提出一种带时间定位能力的音频语言模型，通过新训练目标抑制幻觉时间戳，并构建了目标事件占比极低的 SpotSound-Bench 基准，在时间定位任务上达到 SOTA。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#音频事件定位</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#音频语言模型</span> <span class="tag-pill tag-pill-soft">#时间定位</span> <span class="tag-pill tag-pill-soft">#基准测试</span> <span class="tag-pill tag-pill-soft">#幻觉抑制</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2604.13023</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-08-12</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner"><div class="oc-headline"><span class="oc-pulse"></span><span class="oc-title">本论文已开源</span><span class="oc-hint">点击下方卡片直达对应资源</span></div><div class="oc-grid"><a class="oc-chip oc-chip-proj" href="https://loiesun.github.io/spotsound/" target="_blank" rel="noopener"><span class="oc-icon">🌐</span><span class="oc-text"><span class="oc-label">项目主页</span><span class="oc-sub">loiesun.github.io/spotsound/</span></span></a></div></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2604.13023" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2604.13023" target="_blank" rel="noopener">📑 PDF</a><a class="rsrc rsrc-proj" href="https://loiesun.github.io/spotsound/" target="_blank" rel="noopener">🌐 项目主页</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>SpotSound 提出一种带时间定位能力的音频语言模型，通过新训练目标抑制幻觉时间戳，并构建了目标事件占比极低的 SpotSound-Bench 基准，在时间定位任务上达到 SOTA。
</div>

## 👥 作者与机构

**Luoyi Sun** ¹ · Xiao Zhou · Zeqian Li · Ya Zhang · Yanfeng Wang · Weidi Xie

**机构**：上海交通大学 · 微软研究院

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合音频语言模型、时间定位方向的研究者阅读。建议重点看第 3 节方法（训练目标设计）和第 4 节实验（SpotSound-Bench 构建与结果）。可先看 §3.2 的幻觉抑制机制和 §4.2 的基准对比。

## 🌍 研究背景

大型音频语言模型（ALMs）在整体音频理解上表现出色，但在时间定位（即精确指出事件发生时间）上不可靠。原因在于训练数据多为片段级监督，缺乏精确时间戳，且现有基准未模拟短事件被密集背景声掩盖的真实场景。本文旨在解决 ALMs 在时间定位上的不足，提出 SpotSound 模型和 SpotSound-Bench 基准。

## 💡 核心创新

1. 提出 SpotSound 模型，专为音频事件时间定位设计
2. 设计新训练目标，抑制输入中不存在事件的幻觉时间戳
3. 构建 SpotSound-Bench 基准，目标事件占比<10%，模拟'大海捞针'场景
4. 在时间定位基准上达到 SOTA，同时保持通用音频语言任务性能

## 🏗️ 模型架构

SpotSound 基于大型音频语言模型架构，输入为音频特征序列，通过编码器提取特征，送入主干网络（可能为 Transformer 或类似结构），结合文本指令进行解码。关键模块包括时间定位头，用于输出事件起止时间。训练目标包含时间戳预测和幻觉抑制项。具体参数量未在摘要中提及。

## 📚 数据集

- SpotSound-Bench（评估，目标事件占比<10%的挑战性时间定位基准）
- 通用音频语言任务数据集（训练，具体名称未提及）

## 📊 实验结果

摘要中未给出具体数值指标，但声称在时间定位基准上达到 SOTA，并在通用下游音频语言任务上保持稳健性能。实验部分可能包含与现有 ALMs 的对比以及消融研究，但具体数据未在摘要中提供。

## 🎯 结论与影响

SpotSound 通过专门设计的时间定位训练目标和挑战性基准，显著提升了 ALMs 的时间定位能力，同时不损害通用性能。该工作为音频语言模型在细粒度时间理解方面提供了新思路，有望推动相关应用如音频事件检索、监控等的发展。

## ⚠️ 局限与未解决问题

摘要未提及局限，但可推测：SpotSound-Bench 可能仅覆盖特定类型音频事件，泛化性待验证；幻觉抑制方法可能对长尾事件效果有限；未报告推理效率或模型大小等实际部署因素。

## 🔗 开源资源

- **项目主页**：<https://loiesun.github.io/spotsound/>

---

<div class="paper-footer"><span>评分：8.2</span><span>原始：8.2</span><a href="/audio-paper-daily/posts/2026-08-12/">← 返回 2026-08-12 速递</a></div>
