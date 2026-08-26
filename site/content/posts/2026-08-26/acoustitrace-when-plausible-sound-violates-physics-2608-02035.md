---
title: "AcoustiTrace: When Plausible Sound Violates Physics"
date: 2026-08-26T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#音频生成评估"]
summary: "提出AcoustiTrace基准，从声学过程维度评估音视频生成中的物理合理性，发现现有模型在基础声学过程上仍存在不足。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#音频生成评估</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#音视频生成</span> <span class="tag-pill tag-pill-soft">#物理合理性</span> <span class="tag-pill tag-pill-soft">#基准测试</span> <span class="tag-pill tag-pill-soft">#声学建模</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2608.02035</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-08-26</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2608.02035" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2608.02035" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出AcoustiTrace基准，从声学过程维度评估音视频生成中的物理合理性，发现现有模型在基础声学过程上仍存在不足。
</div>

## 👥 作者与机构

**Shiyang Li** ¹ · Yuewen Cao · Yihao Liu · Yuandong Pu · Baochang Zhang · Xiaofei Li · Changqing Zou

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合音视频生成、多模态学习及声学建模研究者阅读。建议重点阅读第3节（评估维度）和第4节（数据集构建），可先看表1和表2了解维度与数据集概览。

## 🌍 研究背景

近期音视频生成模型能产生语义合理且同步的声音，但常违反可见事件和环境隐含的声学过程。现有基准缺乏对特定声学过程违规的归因和严重性量化。本文旨在填补这一空白，通过形式化声学物理真实性，构建诊断基准，以推动生成模型向物理一致方向发展。

## 💡 核心创新

1. 提出声学过程为中心的评估维度框架
2. 构建大规模真实音视频与RGB-D注释数据集
3. 开发针对性提示套件与验证评估器
4. 展示诊断结果可指导模型优化
5. 覆盖T2AV与I2AV两种生成任务

## 🏗️ 模型架构

AcoustiTrace作为诊断基准，不涉及生成模型架构。其核心包括：评估维度定义（声音生成、传播环境、声学接收，共8个维度）、数据集构建（真实音视频记录与声学注释RGB-D观测）、提示套件生成（针对各维度设计提示）、评估器开发（基于声学量验证）。

## 📚 数据集

- AcoustiTrace数据集（构建，包含真实音视频与RGB-D观测）
- 现有音视频生成模型输出（评估）

## 📊 实验结果

实验表明，即使领先的生成器在产生合理声音事件的同时，仍难以处理基础声学过程。诊断结果可指导模型优化，但摘要未提供具体指标数值。

## 🎯 结论与影响

AcoustiTrace为音视频生成提供声学物理真实性的诊断基准，揭示现有模型在声学过程上的不足，为将声学原理融入训练目标、奖励建模和候选选择开辟新方向，有望推动生成模型向物理一致发展。

## ⚠️ 局限与未解决问题

摘要未提及局限。可能的问题包括：数据集规模与多样性有限，评估器可能未覆盖所有声学场景，诊断结果对模型优化的指导作用需进一步验证。

---

<div class="paper-footer"><span>评分：7.8</span><span>原始：7.8</span><a href="/audio-paper-daily/posts/2026-08-26/">← 返回 2026-08-26 速递</a></div>
