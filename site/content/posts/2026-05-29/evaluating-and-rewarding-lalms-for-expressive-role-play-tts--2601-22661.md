---
title: "Evaluating and Rewarding LALMs for Expressive Role-Play TTS via Mean Continuation Log-Probability"
date: 2026-05-29T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#语音合成"]
summary: "提出MCLP指标用于评估和优化角色扮演TTS的风格一致性，并作为强化学习奖励提升表现。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#语音合成</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#角色扮演TTS</span> <span class="tag-pill tag-pill-soft">#风格一致性</span> <span class="tag-pill tag-pill-soft">#强化学习</span> <span class="tag-pill tag-pill-soft">#评估指标</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2601.22661</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-05-29</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner"><div class="oc-headline"><span class="oc-pulse"></span><span class="oc-title">本论文已开源</span><span class="oc-hint">点击下方卡片直达对应资源</span></div><div class="oc-grid"><a class="oc-chip oc-chip-code" href="https://github.com/y-ren16/MCLP" target="_blank" rel="noopener"><span class="oc-icon">💻</span><span class="oc-text"><span class="oc-label">代码仓库</span><span class="oc-sub">y-ren16/MCLP</span></span></a></div></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2601.22661" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2601.22661" target="_blank" rel="noopener">📑 PDF</a><a class="rsrc rsrc-code" href="https://github.com/y-ren16/MCLP" target="_blank" rel="noopener">💻 代码</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出MCLP指标用于评估和优化角色扮演TTS的风格一致性，并作为强化学习奖励提升表现。
</div>

## 👥 作者与机构

**Yong Ren** ¹ · Jingbei Li · Haiyang Sun · Yujie Chen · Cheng Yi · Yechang Huang · Hao Gu · Ye Bai · … 等 1 人

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合从事TTS、角色扮演对话系统或语音风格控制的研究者。建议重点阅读§3（MCLP定义）和§4（RL训练方法），实验部分可快速浏览。

## 🌍 研究背景

角色扮演TTS要求语音与角色设定和场景描述高度一致，但现有模型在多轮对话中难以保持风格连贯。缺乏客观的风格量化指标是主要瓶颈。本文提出MCLP，利用预训练LALM的上下文学习能力度量语音token的似然，作为风格连续性的代理，并用作强化学习奖励信号。

## 💡 核心创新

1. 提出MCLP指标量化语音风格连续性
2. 将MCLP作为强化学习奖励优化RP-TTS
3. 构建大规模RP-TTS数据集含场景和角色标注

## 🏗️ 模型架构

基于LALM的RP-TTS系统，输入为文本和角色/场景描述，生成语音token。MCLP计算时，将历史上下文（文本、生成语音、重复文本）输入预训练LALM，输出ground-truth语音token的log-probability均值。强化学习阶段，以MCLP为奖励，使用策略梯度优化生成器。

## 📚 数据集

- 自建RP-TTS数据集（训练/评估，含场景和角色标注，规模未提及）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| MCLP | 自建RP-TTS测试集 | 基线模型（未使用MCLP奖励） | **使用MCLP奖励的模型** | 提升（具体数值未给出） |
| 主观风格一致性评分 | 自建RP-TTS测试集 | 基线模型 | **使用MCLP奖励的模型** | 提升（具体数值未给出） |

实验表明MCLP与人类对风格一致性的判断高度对齐，作为强化学习奖励能有效提升RP-TTS的风格连贯性，在客观指标和主观评估上均取得一致增益。具体数值未在摘要中给出。

## 🎯 结论与影响

MCLP为角色扮演TTS提供了有效的风格量化指标和优化信号，有望推动交互式语音合成的发展。该方法可推广至其他需要风格控制的TTS任务，对工业界提升虚拟角色语音质量有参考价值。

## ⚠️ 局限与未解决问题

MCLP依赖预训练LALM，计算开销较大；数据集未公开；未与现有风格评估指标（如MOS）进行充分对比；缺乏跨数据集泛化实验。

## 🔗 开源资源

- **代码**：<https://github.com/y-ren16/MCLP>

---

<div class="paper-footer"><span>评分：7.8</span><span>原始：7.8</span><a href="/audio-paper-daily/posts/2026-05-29/">← 返回 2026-05-29 速递</a></div>
