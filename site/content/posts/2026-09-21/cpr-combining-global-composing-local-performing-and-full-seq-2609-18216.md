---
title: "CPR: Combining global composing, local performing and full-sequence refining in piano rendering with continuous autoregressive modelling"
date: 2026-09-21T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#音乐生成"]
summary: "提出 Composer-Performer-Refiner 连续自回归框架，用局部流匹配生成 24kHz 声学隐变量并上采样至 48kHz，实现钢琴 MIDI 到音频渲染。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero">
<div class="hero-score">
<div class="score-num">7.0</div>
<div class="score-stars">★★★★☆</div>
<div class="score-tier">前25%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#音乐生成</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#音乐生成</span> <span class="tag-pill tag-pill-soft">#自回归建模</span> <span class="tag-pill tag-pill-soft">#流匹配</span> <span class="tag-pill tag-pill-soft">#音频生成</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2609.18216</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-09-21</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner"><div class="oc-headline"><span class="oc-pulse"></span><span class="oc-title">本论文已开源</span><span class="oc-hint">点击下方卡片直达对应资源</span></div><div class="oc-grid"><a class="oc-chip oc-chip-code" href="https://github.com/FEAfeatherTHER/CPR_official" target="_blank" rel="noopener"><span class="oc-icon">💻</span><span class="oc-text"><span class="oc-label">代码仓库</span><span class="oc-sub">FEAfeatherTHER/CPR_official</span></span></a></div></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2609.18216" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2609.18216" target="_blank" rel="noopener">📑 PDF</a><a class="rsrc rsrc-code" href="https://github.com/FEAfeatherTHER/CPR_official" target="_blank" rel="noopener">💻 代码</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出 Composer-Performer-Refiner 连续自回归框架，用局部流匹配生成 24kHz 声学隐变量并上采样至 48kHz，实现钢琴 MIDI 到音频渲染。
</div>

## 👥 作者与机构

**Chong Jing** ¹ · Junan Zhang · Zhizheng Wu

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合做音乐生成、连续自回归建模与流匹配的读者。建议通读，重点看 §3 的 CPR 三段式结构与 BREPA、MT-RoPE 两个模块设计，以及表 2 的消融与主观评测；若只关心效率，可先看 Performer 局部流匹配的复杂度分析。

## 🌍 研究背景

钢琴 MIDI-to-Music 渲染要求在忠实还原目标音符的同时复刻参考录音音色。此前主流分两支：离散 codec 自回归模型具备因果时序建模能力，但量化会丢失声学细节；flow matching / diffusion 保留声学结构更好，却需全序列注意力、代价高且语义结构较弱。本文要解决的核心问题是：如何在保留 AR 条件跟随能力的同时避免量化瓶颈，并降低全序列注意力的计算开销。

## 💡 核心创新

1. Composer-Performer-Refiner 三段式连续 AR 渲染框架
2. Bottlenecked Representation Alignment (BREPA) 强化音乐语义
3. Modality-Time RoPE (MT-RoPE) 跨模态时间对齐
4. Performer 用局部 flow matching 生成 24kHz 声学隐变量

## 🏗️ 模型架构

输入为 MIDI 音符与参考音色提示，Composer 以连续自回归方式逐帧预测隐藏状态，避免离散量化；Performer 在局部窗口内用 flow matching 将隐藏状态解码为 24kHz 声学隐变量，规避全序列注意力开销；Refiner 再将波形上采样至 48kHz。BREPA 通过瓶颈表示对齐增强 Composer 隐藏状态的音乐语义结构，MT-RoPE 在模态与时间维度上做旋转位置编码以对齐跨模态时序。摘要未给出参数量。

## 📊 实验结果

摘要未提供任何具体指标数值、数据集名称或与基线的定量对比，仅以定性方式声称连续 AR 兼顾 AR 的条件跟随能力与 flow matching 的分布建模能力，并绕过量化瓶颈、降低计算成本。因此无法核验其相对离散 codec AR 与 flow matching 方法的实际增益，需查阅正文实验部分确认。

## 🎯 结论与影响

本文最强结论是：连续自回归 + 局部流匹配可在不量化声学表示的前提下完成高采样率钢琴渲染，兼顾条件跟随与声学保真。若实验成立，该范式可迁移到其他高保真符号到音频任务，并为工业级音乐渲染管线提供比全序列 diffusion 更省算力的替代路径。

## ⚠️ 局限与未解决问题

摘要未给出任何定量结果、数据集与基线对比，无法判断相对 SOTA 的实际提升；BREPA 与 MT-RoPE 缺少消融证据；未报告推理延迟与显存占用，而效率正是其核心卖点之一；48kHz 上采样 Refiner 的增益也未量化。

## 🔗 开源资源

- **代码**：<https://github.com/FEAfeatherTHER/CPR_official>

---

<div class="paper-footer"><span>评分：7.0</span><span>原始：7.0</span><a href="/audio-paper-daily/posts/2026-09-21/">← 返回 2026-09-21 速递</a></div>
