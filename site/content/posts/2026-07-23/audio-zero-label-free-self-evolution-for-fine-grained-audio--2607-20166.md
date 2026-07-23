---
title: "Audio-Zero: Label-Free Self-Evolution for Fine-Grained Audio Reasoning"
date: 2026-07-23T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#音频推理"]
summary: "提出无标签自进化框架Audio-Zero，通过听觉自博弈游戏提升大音频语言模型的细粒度推理能力。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#音频推理</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#大音频语言模型</span> <span class="tag-pill tag-pill-soft">#自进化</span> <span class="tag-pill tag-pill-soft">#细粒度推理</span> <span class="tag-pill tag-pill-soft">#自监督学习</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2607.20166</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-07-23</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2607.20166" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2607.20166" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出无标签自进化框架Audio-Zero，通过听觉自博弈游戏提升大音频语言模型的细粒度推理能力。
</div>

## 👥 作者与机构

**Siqian Tong** ¹ · Xuan Li · Chaozhuo Li · Baolong Bi · Yiwei Wang · Yujun Cai · Shenghua Liu · Chengpeng Hao

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合从事音频语言模型、多模态推理的研究者。建议重点阅读§3方法部分和§4实验分析，尤其是自博弈游戏设计和进化分析。可先看图1和表1了解整体效果。

## 🌍 研究背景

大音频语言模型在声学理解上取得进展，但在细粒度音频推理（如事件顺序、重复、时长）上仍不足。现有后训练方法依赖昂贵的外部标签或仅提供粗粒度语义信号。本文旨在无需标注数据的情况下，通过自进化框架提升模型的细粒度听觉感知与推理能力。

## 💡 核心创新

1. 首次提出无标签自进化框架Audio-Zero
2. 设计听觉自博弈游戏，利用对比音频对生成可验证奖励
3. 通过游戏压力自然涌现细粒度听觉描述
4. 在多个基准上提升细粒度推理且保持泛化能力

## 🏗️ 模型架构

Audio-Zero基于现有LALM（如Qwen2-Audio-7B-Instruct），构建听觉自博弈游戏：多个玩家听参考音频，一个奇数听众听细微变体。模型先生成描述线索，再通过推理线索不一致性识别奇数听众。游戏提供可验证奖励，无需标注。框架迭代优化模型参数。

## 📚 数据集

- TREA（评估细粒度推理）
- MMAU Test-mini（评估细粒度推理）
- MMAR（评估细粒度推理）

## 📊 实验结果

实验在TREA、MMAU Test-mini和MMAR上评估，使用Qwen2-Audio-7B-Instruct和Qwen2.5-Omni-7B。Audio-Zero在细粒度音频推理任务上取得提升，同时保持广泛音频理解能力。进化分析显示游戏压力促使模型生成更细粒度的听觉描述。

## 🎯 结论与影响

Audio-Zero通过无标签自进化框架显著提升LALM的细粒度音频推理能力，为摆脱昂贵标注提供了新范式。该方法有望推动音频理解向更精细方向发展，并可能应用于需要精确时序分析的场景。

## ⚠️ 局限与未解决问题

未报告推理延迟和计算开销；仅在两个模型上验证，泛化性待考；游戏设计依赖对比音频对，其生成方式可能影响效果；缺乏与有监督方法的直接对比。

---

<div class="paper-footer"><span>评分：7.8</span><span>原始：7.8</span><a href="/audio-paper-daily/posts/2026-07-23/">← 返回 2026-07-23 速递</a></div>
