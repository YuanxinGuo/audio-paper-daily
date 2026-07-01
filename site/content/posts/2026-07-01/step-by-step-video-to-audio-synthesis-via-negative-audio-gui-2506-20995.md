---
title: "Step-by-Step Video-to-Audio Synthesis via Negative Audio Guidance"
date: 2026-07-01T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#视频到音频生成"]
summary: "提出逐步视频到音频生成方法，通过负音频引导避免声音重复，实现多事件音频合成。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#视频到音频生成</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#音频生成</span> <span class="tag-pill tag-pill-soft">#负引导</span> <span class="tag-pill tag-pill-soft">#Foley</span> <span class="tag-pill tag-pill-soft">#逐步生成</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2506.20995</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-07-01</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner"><div class="oc-headline"><span class="oc-pulse"></span><span class="oc-title">本论文已开源</span><span class="oc-hint">点击下方卡片直达对应资源</span></div><div class="oc-grid"><a class="oc-chip oc-chip-proj" href="https://ahykw.github.io/sbsv2a/" target="_blank" rel="noopener"><span class="oc-icon">🌐</span><span class="oc-text"><span class="oc-label">项目主页</span><span class="oc-sub">ahykw.github.io/sbsv2a/</span></span></a><a class="oc-chip oc-chip-demo" href="https://ahykw.github.io/sbsv2a/" target="_blank" rel="noopener"><span class="oc-icon">🔊</span><span class="oc-text"><span class="oc-label">在线 Demo</span><span class="oc-sub">ahykw.github.io/sbsv2a/</span></span></a></div></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2506.20995" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2506.20995" target="_blank" rel="noopener">📑 PDF</a><a class="rsrc rsrc-proj" href="https://ahykw.github.io/sbsv2a/" target="_blank" rel="noopener">🌐 项目主页</a><a class="rsrc rsrc-demo" href="https://ahykw.github.io/sbsv2a/" target="_blank" rel="noopener">🔊 Demo</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出逐步视频到音频生成方法，通过负音频引导避免声音重复，实现多事件音频合成。
</div>

## 👥 作者与机构

**Akio Hayakawa** ¹ · Masato Ishii · Takashi Shibuya · Yuki Mitsufuji ✉

**机构**：索尼

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合音频生成、视频配音领域研究者。建议重点阅读第3节方法（负引导训练与推理）和第4节实验（客观/主观评估）。可先看Fig.2理解整体流程。

## 🌍 研究背景

视频到音频生成旨在为无声视频合成同步音效。现有方法通常一次性生成完整音频，难以精细控制多事件叠加。传统Foley工作流中，音效师逐步叠加声音，但缺乏自动化方法。本文受此启发，提出逐步生成框架，利用负引导避免已生成声音的重复，无需多参考视频-音频数据集。

## 💡 核心创新

1. 负音频引导机制抑制已生成声音
2. 基于非重叠片段音频对的微调训练策略
3. 逐步生成框架支持多事件音频合成

## 🏗️ 模型架构

输入视频帧序列，使用预训练V2A模型（如Diffusion-based）作为基础。每个生成步骤中，模型以视频和之前生成的音频轨迹为条件，通过负引导模块（finetuned guidance model）调整去噪过程，使当前生成的声音与已有声音互补。最终输出多轨音频叠加。

## 📚 数据集

- VGG-Sound（训练/评估，视频-音频对）
- AudioSet（训练/评估，视频-音频对）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| FAD | VGG-Sound | Im2Wav 2.0 (1.82) | **1.53** | -0.29 |
| CLAP score | VGG-Sound | Im2Wav 2.0 (0.31) | **0.33** | +0.02 |
| MOS (overall quality) | VGG-Sound | Im2Wav 2.0 (3.21) | **3.54** | +0.33 |

客观指标上，FAD降低0.29，CLAP分数提升0.02；主观MOS提升0.33。消融实验验证了负引导的有效性，逐步生成相比一次性生成在声音分离度和整体质量上更优。

## 🎯 结论与影响

本文提出的逐步V2A生成方法通过负音频引导实现了多事件音频合成，显著提升生成质量和可控性。该方法为视频配音自动化提供了新思路，有望降低Foley制作成本。

## ⚠️ 局限与未解决问题

依赖预训练V2A模型质量；负引导可能引入伪影；未评估计算效率；仅验证在两类数据集，泛化性待考。

## 🔗 开源资源

- **项目主页**：<https://ahykw.github.io/sbsv2a/>
- **Demo / 试听**：<https://ahykw.github.io/sbsv2a/>

---

<div class="paper-footer"><span>评分：7.8</span><span>原始：7.8</span><a href="/audio-paper-daily/posts/2026-07-01/">← 返回 2026-07-01 速递</a></div>
