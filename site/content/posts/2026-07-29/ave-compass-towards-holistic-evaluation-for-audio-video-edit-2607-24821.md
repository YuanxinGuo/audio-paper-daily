---
title: "AVE-Compass: Towards Holistic Evaluation for Audio-Video Editing Abilities"
date: 2026-07-29T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#音视频编辑评估"]
summary: "提出AVE-Compass基准，系统评估音视频联合编辑能力，并设计AVE-Agent智能体框架提升跨模态编辑一致性。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#音视频编辑评估</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#音视频编辑</span> <span class="tag-pill tag-pill-soft">#基准测试</span> <span class="tag-pill tag-pill-soft">#多模态评估</span> <span class="tag-pill tag-pill-soft">#智能体</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2607.24821</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-07-29</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2607.24821" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2607.24821" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出AVE-Compass基准，系统评估音视频联合编辑能力，并设计AVE-Agent智能体框架提升跨模态编辑一致性。
</div>

## 👥 作者与机构

**Yuqing Wen** ¹ · Yukai Huang · Qianqian Xie · Jiangtao Wu · Yibin Lin · Yikai Gu · Jialu Chen · Yuanxing Zhang · … 等 1 人

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合从事视频编辑、多模态生成评估的研究者阅读。建议重点看第3节基准设计（数据集构建与评估指标）和第4节实验分析（模型表现与失败案例）。可先浏览表1和表2了解评估维度。

## 🌍 研究背景

现有视频编辑基准主要关注视觉变换（如Text2Video-Zero），音频编辑基准（如AudioLDM）则独立评估。真实世界视频中音视频紧密耦合，编辑一个模态常需协调另一个模态，但缺乏同时评估音视频编辑及跨模态一致性的基准。本文旨在填补这一空白，系统评估指令遵循、保真度、真实感和编辑意图。

## 💡 核心创新

1. 构建145个源视频、196条音视频耦合指令的基准数据集
2. 设计2688项细粒度检查清单，覆盖四个评估维度
3. 提出基于MLLM的清单评判和真实感评估方法
4. 提出AVE-Agent模块化智能体框架，分解复杂指令并迭代优化
5. 引入自动跨模态、视频和音频指标

## 🏗️ 模型架构

AVE-Compass基准包含145个源视频（涵盖多种场景），196条音视频耦合编辑指令，以及2688项检查清单。评估采用MLLM评判（基于GPT-4V）和真实感评估。AVE-Agent框架由指令分解模块、执行模块、自反思模块和评估器组成：指令分解将复杂指令拆分为依赖子任务；执行模块调用现有编辑模型（如VideoCrafter2、AudioLDM2）；自反思模块根据评估器反馈迭代改进。

## 📚 数据集

- AVE-Compass数据集（145个源视频，196条指令，2688项检查清单，用于评估）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| 指令执行成功率 | AVE-Compass | VideoCrafter2+AudioLDM2 0.45 | **AVE-Agent 0.62** | +0.17 |
| 保真度评分 | AVE-Compass | VideoCrafter2+AudioLDM2 0.38 | **AVE-Agent 0.55** | +0.17 |
| 音视频对齐评分 | AVE-Compass | VideoCrafter2+AudioLDM2 0.41 | **AVE-Agent 0.59** | +0.18 |

实验表明，现有模型（如VideoCrafter2+AudioLDM2）在跨模态指令执行上表现不佳，AVE-Agent通过指令分解和自反思显著提升指令执行、保真度和音视频对齐，同时保持感知质量。消融实验验证了各模块的有效性。

## 🎯 结论与影响

AVE-Compass是首个系统评估音视频联合编辑能力的基准，揭示了现有模型在跨模态一致性上的不足。AVE-Agent通过模块化分解和迭代优化有效提升了编辑质量。该工作为音视频编辑评估提供了标准化框架，有望推动多模态生成模型的协同发展。

## ⚠️ 局限与未解决问题

基准规模有限（145个视频），可能未覆盖所有编辑场景；MLLM评判可能引入偏差；AVE-Agent依赖现有编辑模型，其性能受限于底层模型；未评估推理效率。

---

<div class="paper-footer"><span>评分：7.8</span><span>原始：7.8</span><a href="/audio-paper-daily/posts/2026-07-29/">← 返回 2026-07-29 速递</a></div>
