---
title: "Assessing speech quality metrics for evaluation of neural audio codecs under clean speech conditions"
date: 2026-08-05T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#语音质量评估"]
summary: "本文评估了45种客观语音质量指标在干净语音条件下对神经音频编解码器的可靠性，发现scoreq和utmos与主观评分相关性最高。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#语音质量评估</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#神经音频编解码器</span> <span class="tag-pill tag-pill-soft">#客观语音质量指标</span> <span class="tag-pill tag-pill-soft">#主观评分相关性</span> <span class="tag-pill tag-pill-soft">#非侵入式指标</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2509.24457</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-08-05</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2509.24457" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2509.24457" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>本文评估了45种客观语音质量指标在干净语音条件下对神经音频编解码器的可靠性，发现scoreq和utmos与主观评分相关性最高。
</div>

## 👥 作者与机构

**Wolfgang Mack** ¹ · Nezih Topaloglu · Laura Lechler · Ivana Bali\'c · Alexandra Craciun · Mansur Yesilbursa · Kamil Wojcicki

**机构**：华为技术有限公司

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合语音编解码器研究者、质量评估领域学者。建议重点阅读第3节（实验设置）和第4节（结果分析），特别是表2和表3。可先看摘要和结论，再深入方法部分。

## 🌍 研究背景

神经音频编解码器（如EnCodec、SoundStream）的快速发展使得客观质量评估变得重要。传统指标如PESQ、STOI等可能不适用于神经编解码器产生的伪影。本文针对干净语音条件下，系统评估45种客观指标与主观听感评分的相关性，以确定哪些指标最可靠。此前缺乏对神经编解码器专用指标的全面比较。

## 💡 核心创新

1. 首次大规模评估45种客观指标在神经编解码器上的表现
2. 发现scoreq和utmos等神经指标与主观评分相关性最高
3. 揭示非侵入式指标在高主观质量区间存在饱和现象
4. 提供跨17种编解码器条件的系统性比较

## 🏗️ 模型架构

本文不涉及模型架构，而是评估方法。使用17种编解码器条件处理干净语音，生成测试样本，然后计算45种客观指标（包括PESQ、STOI、ViSQOL、scoreq、utmos等），并与主观听感评分（如MOS）进行相关性分析。

## 📚 数据集

- 内部测试集（评估，包含17种编解码器条件）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| Pearson correlation | 内部测试集 | PESQ 0.85 | **scoreq 0.92** | +0.07 |
| Pearson correlation | 内部测试集 | STOI 0.78 | **utmos 0.91** | +0.13 |

实验结果显示，神经指标scoreq和utmos与主观评分的Pearson相关系数最高（约0.92和0.91），显著优于传统指标如PESQ（0.85）和STOI（0.78）。进一步分析表明，非侵入式指标在高主观质量区间（如MOS>4）出现饱和，导致区分度下降。

## 🎯 结论与影响

本文系统评估了45种客观指标，证明scoreq和utmos在干净语音条件下对神经编解码器质量评估最可靠。该发现为神经编解码器的质量评估提供了指导，建议采用神经指标替代传统指标。对工业界，可提升编解码器开发中的质量监控效率。

## ⚠️ 局限与未解决问题

仅评估了干净语音条件，未考虑噪声和混响等复杂场景；主观评分可能受测试人员影响；未提供指标的计算复杂度对比；未涵盖所有最新神经编解码器。

---

<div class="paper-footer"><span>评分：7.2</span><span>原始：7.2</span><a href="/audio-paper-daily/posts/2026-08-05/">← 返回 2026-08-05 速递</a></div>
