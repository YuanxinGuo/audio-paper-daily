---
title: "MTAVG-Bench 2.0: Diagnosing Failure Modes of Cinematic Expressiveness in Multi-Talker Audio-Video Generation"
date: 2026-05-28T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#多说话人音视频生成评估"]
summary: "提出MTAVG-Bench 2.0基准，系统诊断多说话人音视频生成中的电影级表现力失败模式。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#多说话人音视频生成评估</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#基准测试</span> <span class="tag-pill tag-pill-soft">#多模态</span> <span class="tag-pill tag-pill-soft">#视频生成</span> <span class="tag-pill tag-pill-soft">#音频生成</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2605.28035</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-05-28</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2605.28035" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2605.28035" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出MTAVG-Bench 2.0基准，系统诊断多说话人音视频生成中的电影级表现力失败模式。
</div>

## 👥 作者与机构

**Haitian Li** ¹ · Yanghao Zhou · Heyan Huang · Liangji Chen · YiMing Cheng · Xu Liu · Dian Jin · Jiajun Xu · … 等 10 人

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合从事音视频生成、多模态评估的研究者阅读。建议重点看§3的失败分类法和§4的评估构建，以及表2的模型对比结果。可先读摘要和结论。

## 🌍 研究背景

现有MTAVG模型在唇形同步、音视频对齐等基础指标上表现良好，但缺乏对场景级电影表现力（如表演连贯性、叙事、氛围）的评估。先前基准主要关注多轮对话质量，无法诊断高级别失败模式。本文旨在构建系统化基准，评估大模型诊断电影级音视频失败的能力。

## 💡 核心创新

1. 提出电影表现力失败分类法（表演、叙事、氛围、视听语言）
2. 构建超1万问答评估实例及短剧级子集
3. 引入时间定位失败模式子任务
4. 系统评估多个全模态大模型诊断能力

## 🏗️ 模型架构

MTAVG-Bench 2.0是一个评估基准而非模型。其核心是构建包含失败分类法、问答实例和子集的评估框架。失败分类法涵盖表演、叙事、氛围、视听语言四个维度。评估实例基于短剧场景生成，包含多轮对话和电影级表现力失败。使用全模态大模型（如Gemini）作为评估器，输出诊断结果。

## 📚 数据集

- MTAVG-Bench 2.0（评估基准，包含超1万问答实例及短剧级子集）

## 📊 实验结果

摘要未提供具体数值结果，仅提及商业模型Gemini显著优于其他评估器，但最强模型仍难以处理复杂失败。

## 🎯 结论与影响

MTAVG-Bench 2.0为诊断多说话人音视频生成中的电影表现力失败提供了系统化基准。实验表明现有全模态大模型在高级别失败诊断上仍有不足，为未来研究指明了方向。该基准有望推动生成模型向更高质量的电影级场景发展。

## ⚠️ 局限与未解决问题

摘要未明确承认局限。作为审稿人，可看出：基准仅评估诊断能力而非生成质量；未提供模型生成的具体失败案例分析；未与人类评估者对比；未讨论基准的泛化性到其他类型视频。

---

<div class="paper-footer"><span>评分：7.2</span><span>原始：7.2</span><a href="/audio-paper-daily/posts/2026-05-28/">← 返回 2026-05-28 速递</a></div>
