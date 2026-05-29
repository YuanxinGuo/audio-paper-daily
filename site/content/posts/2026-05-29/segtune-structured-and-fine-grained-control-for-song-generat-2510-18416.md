---
title: "SegTune: Structured and Fine-Grained Control for Song Generation"
date: 2026-05-29T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#音乐生成"]
summary: "提出SegTune，一种非自回归框架，通过段级文本提示实现歌曲的结构化细粒度控制，并引入LLM时长预测器实现歌词与音乐精确对齐。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#音乐生成</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#可控音乐生成</span> <span class="tag-pill tag-pill-soft">#非自回归模型</span> <span class="tag-pill tag-pill-soft">#歌词对齐</span> <span class="tag-pill tag-pill-soft">#段级控制</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2510.18416</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-05-29</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner"><div class="oc-headline"><span class="oc-pulse"></span><span class="oc-title">本论文已开源</span><span class="oc-hint">点击下方卡片直达对应资源</span></div><div class="oc-grid"><a class="oc-chip oc-chip-proj" href="https://cai525.github.io/SegTune_demo" target="_blank" rel="noopener"><span class="oc-icon">🌐</span><span class="oc-text"><span class="oc-label">项目主页</span><span class="oc-sub">cai525.github.io/SegTune_demo</span></span></a><a class="oc-chip oc-chip-demo" href="https://cai525.github.io/SegTune_demo" target="_blank" rel="noopener"><span class="oc-icon">🔊</span><span class="oc-text"><span class="oc-label">在线 Demo</span><span class="oc-sub">cai525.github.io/SegTune_demo</span></span></a></div></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2510.18416" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2510.18416" target="_blank" rel="noopener">📑 PDF</a><a class="rsrc rsrc-proj" href="https://cai525.github.io/SegTune_demo" target="_blank" rel="noopener">🌐 项目主页</a><a class="rsrc rsrc-demo" href="https://cai525.github.io/SegTune_demo" target="_blank" rel="noopener">🔊 Demo</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出SegTune，一种非自回归框架，通过段级文本提示实现歌曲的结构化细粒度控制，并引入LLM时长预测器实现歌词与音乐精确对齐。
</div>

## 👥 作者与机构

**Pengfei Cai** ¹ · Joanna Wang · Haorui Zheng · Xu Li · Zihao Ji · Teng Ma · Zhongliang Liu · Chen Zhang · … 等 1 人

**机构**：字节跳动

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合音乐生成、可控生成方向的研究者。建议重点阅读§3.2段级控制注入方法和§3.3 LLM时长预测器，以及实验部分表2的定量对比。可先看demo页面了解效果。

## 🌍 研究背景

现有歌曲生成系统通常从歌词或全局文本提示生成歌曲，但缺乏对音乐随时间变化属性的建模，无法实现细粒度控制，如段落结构、动态变化等。之前的方法如MusicGen、Jukebox等主要依赖全局条件，难以指定局部音乐描述。本文旨在解决段级控制问题，允许用户或LLM为歌曲的不同段落指定局部描述，同时保持整体风格一致性。

## 💡 核心创新

1. 段级文本提示注入：将局部描述广播到对应时间窗口
2. LLM-based时长预测器：自回归生成带时间戳的LRC格式歌词
3. 大规模数据流水线：收集高质量对齐的歌曲-提示数据
4. 新评估指标：段级对齐和声乐属性一致性度量

## 🏗️ 模型架构

SegTune采用非自回归框架。输入为歌词和段级文本提示，首先通过LLM时长预测器（基于预训练语言模型）生成句子级时间戳LRC歌词。然后，将段级提示通过时间广播机制注入到对应时间窗口，全局提示则影响整首歌以保持风格一致。主干网络基于扩散模型或类似架构（摘要未明确具体网络名），输出为音频波形。模型参数量未提及。

## 📚 数据集

- 自建数据集（训练/评估）：大规模高质量歌曲与对齐歌词和提示，具体规模未提及

## 📊 实验结果

摘要未提供具体数值结果，仅声称SegTune在可控性和音乐连贯性上优于现有基线。实验部分可能包含主观MOS测试和客观指标（如段级对齐准确率），但摘要未给出。

## 🎯 结论与影响

SegTune通过段级控制实现了对歌曲结构的细粒度操控，结合LLM时长预测器提升了歌词与音乐的对齐精度。该工作为可控音乐生成提供了新范式，有望推动个性化音乐创作和交互式音乐生成应用。

## ⚠️ 局限与未解决问题

摘要未明确讨论局限。可能的问题包括：依赖LLM时长预测器的准确性，段级控制可能限制创作自由度，大规模数据流水线的质量依赖标注，以及缺乏与主流方法（如MusicGen）的定量对比。

## 🔗 开源资源

- **项目主页**：<https://cai525.github.io/SegTune_demo>
- **Demo / 试听**：<https://cai525.github.io/SegTune_demo>

---

<div class="paper-footer"><span>评分：7.8</span><span>原始：7.8</span><a href="/audio-paper-daily/posts/2026-05-29/">← 返回 2026-05-29 速递</a></div>
