---
title: "BEAT: Tokenizing and Generating Symbolic Music by Uniform Temporal Steps"
date: 2026-05-29T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#音乐生成"]
summary: "提出BEAT分词法，以均匀节拍步长编码符号音乐，提升生成质量与结构连贯性。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#音乐生成</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#符号音乐生成</span> <span class="tag-pill tag-pill-soft">#音乐分词</span> <span class="tag-pill tag-pill-soft">#音乐续写</span> <span class="tag-pill tag-pill-soft">#伴奏生成</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2604.19532</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-05-29</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2604.19532" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2604.19532" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出BEAT分词法，以均匀节拍步长编码符号音乐，提升生成质量与结构连贯性。
</div>

## 👥 作者与机构

**Lekai Qian** ¹ · Haoyu Gu · Jingwei Zhao · Ziyu Wang

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合音乐信息检索与符号音乐生成研究者。重点读§3分词方案与§4实验对比，可先看表1与图2理解分词差异。

## 🌍 研究背景

符号音乐生成中，主流方法将音乐分词为事件序列（如音高、时移），但各token时长不等，导致时间推进不均匀。现有方法隐式处理音乐节奏规律，难以捕捉长程结构。本文提出以均匀节拍步长为基本单元的分词方案，将同一时间步内相同音高的所有事件编码为一个token，显式按时间步分组，类似钢琴卷帘的稀疏编码。

## 💡 核心创新

1. 提出BEAT分词法，以均匀节拍步长为基本单元
2. 将同一时间步内相同音高的所有事件编码为单一token
3. 显式按时间步分组，形成稀疏钢琴卷帘表示
4. 在音乐续写与伴奏生成任务上验证有效性

## 🏗️ 模型架构

输入为符号音乐（MIDI），首先将音乐按均匀节拍步长（如四分音符）切分，每个时间步内，将相同音高的所有事件（如音符开/关、力度）合并为一个token，形成稀疏的钢琴卷帘序列。然后使用Transformer解码器进行自回归生成，输出为相同格式的token序列。模型参数量未在摘要中给出。

## 📚 数据集

- 未在摘要中明确指定数据集，仅提及音乐续写与伴奏生成任务

## 📊 实验结果

摘要未提供具体数值指标，仅定性说明BEAT分词法在音乐续写与伴奏生成任务上相比主流事件基方法提升了音乐质量和结构连贯性，且效率更高、更有效捕捉长程模式。

## 🎯 结论与影响

BEAT分词法通过均匀节拍步长显式编码音乐时间结构，在符号音乐生成中优于传统事件基方法。该工作为音乐分词提供了新视角，可能推动更结构化的音乐生成模型发展，对音乐创作辅助工具具有潜在应用价值。

## ⚠️ 局限与未解决问题

摘要未报告具体数据集与量化指标，缺乏与SOTA方法的严格对比；未讨论不同节拍粒度的影响；未涉及多轨或复杂和声场景的泛化能力。

---

<div class="paper-footer"><span>评分：7.2</span><span>原始：7.2</span><a href="/audio-paper-daily/posts/2026-05-29/">← 返回 2026-05-29 速递</a></div>
