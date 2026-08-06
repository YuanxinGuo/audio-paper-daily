---
title: "A Dual Evaluation for Music Transcription"
date: 2026-08-06T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#音乐转录"]
summary: "本文提出对音乐转录系统进行记谱相似度和播放相似度的双重评估，发现CLEWS指标与人类判断最相关且成本最低，且两种评估维度偏好不同系统。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero">
<div class="hero-score">
<div class="score-num">7.5</div>
<div class="score-stars">★★★★☆</div>
<div class="score-tier">前25%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#音乐转录</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#音乐转录</span> <span class="tag-pill tag-pill-soft">#评估指标</span> <span class="tag-pill tag-pill-soft">#播放相似度</span> <span class="tag-pill tag-pill-soft">#记谱相似度</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2608.04511</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-08-06</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2608.04511" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2608.04511" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>本文提出对音乐转录系统进行记谱相似度和播放相似度的双重评估，发现CLEWS指标与人类判断最相关且成本最低，且两种评估维度偏好不同系统。
</div>

## 👥 作者与机构

**Ping Wang** ¹ · Guang Yang · Nazif Can Tamer · Victoria Ebert · Noah A. Smith

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合音乐信息检索和自动音乐转录领域的研究者阅读。建议重点阅读第3节（评估方法）和第4节（实验结果），特别是关于CLEWS指标与人类判断的相关性分析。可先看摘要和结论，再深入方法部分。

## 🌍 研究背景

自动音乐转录系统生成可读可播放的乐谱，但现有评估通常只关注单一指标，未能全面反映转录质量。本文提出应分别评估记谱相似度（与参考乐谱比较）和播放相似度（与原始演奏比较），并探索不同指标的有效性。

## 💡 核心创新

1. 提出双重评估框架，区分记谱相似度和播放相似度
2. 通过大规模听感实验验证多种播放相似度指标
3. 发现CLEWS指标与人类判断最相关且计算成本最低
4. 构建24种转录流水线并分析组件对评估结果的影响
5. 提出新端到端系统Rubato，在记谱相似度上显著提升

## 🏗️ 模型架构

本文主要提出评估框架，而非具体模型。评估框架包括：输入为音频和参考乐谱，使用光学音乐识别中的记谱相似度指标和多种播放相似度方法。播放相似度方法包括基于对齐的、基于嵌入的等，其中CLEWS为最优。同时构建了由8种音频转MIDI模型和3种MIDI转乐谱转换器组成的24种流水线，以及新系统Rubato。

## 📚 数据集

- 230首钢琴录音（评估，覆盖23部作品、30位演奏者、6位作曲家）
- 100多名参与者（听感实验，评估播放相似度指标）

## 📊 实验结果

摘要未提供具体数值，但指出CLEWS指标与人类判断相关性最好且成本最低。两种评估维度偏好不同系统，其中MIDI转乐谱转换器对评估结果影响显著。Rubato在记谱相似度上大幅提升，但在播放相似度上虽具竞争力但非最优。

## 🎯 结论与影响

本文强调音乐转录评估应兼顾记谱和播放两个维度，并发现CLEWS是高效且有效的播放相似度指标。该工作为转录系统评估提供了新视角，可能推动更全面的评估标准，对音乐转录系统的开发和优化具有指导意义。

## ⚠️ 局限与未解决问题

摘要未提及局限，但可能包括：评估仅针对钢琴录音，泛化性未知；听感实验参与者背景可能影响主观判断；未提供具体指标数值，难以量化改进幅度；未讨论计算成本细节。

---

<div class="paper-footer"><span>评分：7.5</span><span>原始：7.5</span><a href="/audio-paper-daily/posts/2026-08-06/">← 返回 2026-08-06 速递</a></div>
