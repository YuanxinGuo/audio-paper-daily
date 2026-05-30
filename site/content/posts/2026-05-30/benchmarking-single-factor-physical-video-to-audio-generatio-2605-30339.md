---
title: "Benchmarking Single-Factor Physical Video-to-Audio Generation"
date: 2026-05-30T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#视频到音频生成"]
summary: "提出FlatSounds基准，通过反事实对和单视频模式测试评估V2A模型的物理推理能力，发现模型依赖文本而非视觉，且文本提升物理准确性但降低时间对齐。"
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
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#物理推理</span> <span class="tag-pill tag-pill-soft">#基准测试</span> <span class="tag-pill tag-pill-soft">#因果评估</span> <span class="tag-pill tag-pill-soft">#视频到音频</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2605.30339</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-05-28</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner"><div class="oc-headline"><span class="oc-pulse"></span><span class="oc-title">本论文已开源</span><span class="oc-hint">点击下方卡片直达对应资源</span></div><div class="oc-grid"><a class="oc-chip oc-chip-proj" href="https://research.nvidia.com/labs/cosmos-lab/flatsounds/" target="_blank" rel="noopener"><span class="oc-icon">🌐</span><span class="oc-text"><span class="oc-label">项目主页</span><span class="oc-sub">research.nvidia.com/labs/cosmos-lab/flatsounds/</span></span></a></div></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2605.30339" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2605.30339" target="_blank" rel="noopener">📑 PDF</a><a class="rsrc rsrc-proj" href="https://research.nvidia.com/labs/cosmos-lab/flatsounds/" target="_blank" rel="noopener">🌐 项目主页</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出FlatSounds基准，通过反事实对和单视频模式测试评估V2A模型的物理推理能力，发现模型依赖文本而非视觉，且文本提升物理准确性但降低时间对齐。
</div>

## 👥 作者与机构

**Tingle Li** ¹ · Siddharth Gururani · Kevin J. Shih · Gantavya Bhatt · Sang-gil Lee · Zhifeng Kong · Arushi Goel · Gopala Anumanchipalli · … 等 1 人

**机构**：英伟达 · 加州大学伯克利分校

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合视频到音频生成、多模态推理领域的研究者。重点读§3（基准设计）和§4（实验结果），特别是表1和图3。可先看§4.2关于文本-视觉依赖的发现。

## 🌍 研究背景

现有视频到音频（V2A）生成模型能产生逼真的音轨，但缺乏对物理过程正确性的评估。传统评估侧重感知质量，忽略物理因果推理。本文旨在通过控制单一物理因素的反事实对和单视频模式测试，系统审计V2A模型的物理推理能力，揭示模型是否真正从像素学习物理过程。

## 💡 核心创新

1. 提出FlatSounds基准，包含反事实对和单视频模式测试
2. 设计物理指标（如速度-频率一致性、碰撞时间对齐）
3. 发现文本描述提升物理准确性但损害时间对齐的权衡
4. 证明物理指标与人类偏好强相关

## 🏗️ 模型架构

不适用（本文为基准测试，不提出新模型）。评估了多个SOTA V2A模型（如Diffusion-based、Auto-regressive），输入为视频帧和可选文本，输出音频。

## 📚 数据集

- FlatSounds（自建，包含反事实对和单视频模式测试，用于评估）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| 物理准确性（速度-频率一致性） | FlatSounds | 无文本模型 0.52 | **有文本模型 0.68** | +0.16 |
| 时间对齐（碰撞事件偏移） | FlatSounds | 无文本模型 0.12s | **有文本模型 0.21s** | +0.09s（退化） |

实验表明，所有模型在物理推理上存在一致权衡：文本描述显著提升物理准确性（如速度-频率一致性从0.52升至0.68），但导致时间对齐退化（碰撞偏移从0.12s增至0.21s）。模型更依赖文本而非视觉流推断物理属性。物理指标与人类偏好强相关（Spearman ρ>0.8）。

## 🎯 结论与影响

本文揭示了当前V2A模型在物理推理上的根本局限：依赖文本而非像素学习物理过程。FlatSounds基准为未来研究提供了评估工具，推动V2A从感知质量向物理正确性发展。工业应用中，需谨慎使用文本提示以避免时间对齐退化。

## ⚠️ 局限与未解决问题

基准仅覆盖单一物理因素（如速度、材质），未测试多因素交互。评估模型数量有限（4个），未涵盖最新模型。未提供模型参数量或推理时间等效率指标。反事实对可能引入人工痕迹。

## 🔗 开源资源

- **项目主页**：<https://research.nvidia.com/labs/cosmos-lab/flatsounds/>

---

<div class="paper-footer"><span>评分：7.8</span><span>原始：7.8</span><a href="/audio-paper-daily/posts/2026-05-30/">← 返回 2026-05-30 速递</a></div>
