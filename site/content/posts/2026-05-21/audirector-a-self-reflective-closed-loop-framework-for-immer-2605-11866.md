---
title: "AuDirector: A Self-Reflective Closed-Loop Framework for Immersive Audio Storytelling"
date: 2026-05-21T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#音频叙事生成"]
summary: "提出AuDirector，一个自反思闭环多智能体框架，通过身份感知预制作、协作合成与校正、人机交互精炼模块，实现连贯且情感丰富的长音频叙事生成。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#音频叙事生成</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#语音合成</span> <span class="tag-pill tag-pill-soft">#多智能体框架</span> <span class="tag-pill tag-pill-soft">#自校正</span> <span class="tag-pill tag-pill-soft">#交互式生成</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2605.11866</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-05-21</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner"><div class="oc-headline"><span class="oc-pulse"></span><span class="oc-title">本论文已开源</span><span class="oc-hint">点击下方卡片直达对应资源</span></div><div class="oc-grid"><a class="oc-chip oc-chip-demo" href="https://anonymous-itsh.github.io/" target="_blank" rel="noopener"><span class="oc-icon">🔊</span><span class="oc-text"><span class="oc-label">在线 Demo</span><span class="oc-sub">anonymous-itsh.github.io/</span></span></a></div></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2605.11866" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2605.11866" target="_blank" rel="noopener">📑 PDF</a><a class="rsrc rsrc-demo" href="https://anonymous-itsh.github.io/" target="_blank" rel="noopener">🔊 Demo</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出AuDirector，一个自反思闭环多智能体框架，通过身份感知预制作、协作合成与校正、人机交互精炼模块，实现连贯且情感丰富的长音频叙事生成。
</div>

## 👥 作者与机构

**Yiming Ren** ¹ · Xuenan Xu · Ziyang Zhang · Wen Wu · Baoxiang Li · Chao Zhang

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合语音合成、音频叙事生成方向的研究者。建议重点阅读§3.2协作合成与校正模块和§3.3人机交互精炼模块，以及表2的消融实验。可先看demo页面了解效果。

## 🌍 研究背景

尽管文本和视觉生成取得进展，创建连贯的长音频叙事仍具挑战。现有框架存在角色设定与语音表现不匹配、缺乏自校正机制、人机交互有限等问题。本文旨在通过多智能体闭环框架解决这些痛点，实现上下文对齐的语音适配和高质量音频生成。

## 💡 核心创新

1. 身份感知预制作机制，从叙事文本提取角色档案和情感指令
2. 协作合成与校正模块，实现闭环自校正
3. 人机交互精炼模块，支持自然语言反馈交互式优化
4. 多智能体协作框架整合语音检索、合成与校正
5. 情感指令引导的语音合成，提升情感表现力

## 🏗️ 模型架构

输入叙事文本 → 身份感知预制作模块提取角色档案和情感指令 → 语音检索模块从候选库中匹配合适语音 → 协作合成与校正模块（包含多个智能体）进行语音合成并闭环审计缺陷，重新生成 → 人机交互精炼模块接收用户自然语言反馈，迭代优化脚本和语音。整体为多智能体协作架构。

## 📚 数据集

- 内部数据集（训练与评估，包含长叙事文本和语音样本）

## 📊 实验结果

摘要未提供具体数值指标，但声称在结构连贯性、情感表现力和声学保真度上优于现有基线。消融实验验证了各模块的有效性。

## 🎯 结论与影响

AuDirector通过自反思闭环多智能体框架显著提升了长音频叙事的连贯性和情感表现力。其身份感知预制作和交互式精炼机制为个性化音频生成提供了新思路，有望推动有声书、播客等工业应用的发展。

## ⚠️ 局限与未解决问题

摘要未提及推理延迟和计算开销；依赖内部数据集，泛化性未知；缺乏与开源方法的定量对比（如MOS分）；自校正机制可能增加生成时间。

## 🔗 开源资源

- **Demo / 试听**：<https://anonymous-itsh.github.io/>

---

<div class="paper-footer"><span>评分：7.8</span><span>原始：7.8</span><a href="/audio-paper-daily/posts/2026-05-21/">← 返回 2026-05-21 速递</a></div>
