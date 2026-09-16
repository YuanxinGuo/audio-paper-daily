---
title: "PARSA-Bench: A Comprehensive Persian Audio-Language Model Benchmark"
date: 2026-09-16T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#音频理解基准"]
summary: "首个波斯语音频-语言模型基准，含16项任务（10项新），覆盖语音理解、副语言与文化音频推理。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero">
<div class="hero-score">
<div class="score-num">6.5</div>
<div class="score-stars">★★★☆☆</div>
<div class="score-tier">前50%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#音频理解基准</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#语音理解</span> <span class="tag-pill tag-pill-soft">#副语言分析</span> <span class="tag-pill tag-pill-soft">#多模态大模型</span> <span class="tag-pill tag-pill-soft">#波斯语</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2603.14456</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-09-16</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner"><div class="oc-headline"><span class="oc-pulse"></span><span class="oc-title">本论文已开源</span><span class="oc-hint">点击下方卡片直达对应资源</span></div><div class="oc-grid"><a class="oc-chip oc-chip-hf" href="https://huggingface.co/datasets/MohammadJRanjbar/PARSA-Bench" target="_blank" rel="noopener"><span class="oc-icon">🤗</span><span class="oc-text"><span class="oc-label">HuggingFace</span><span class="oc-sub">🤗 datasets/MohammadJRanjbar/PARSA-Bench</span></span></a></div></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2603.14456" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2603.14456" target="_blank" rel="noopener">📑 PDF</a><a class="rsrc rsrc-hf" href="https://huggingface.co/datasets/MohammadJRanjbar/PARSA-Bench" target="_blank" rel="noopener">🤗 HuggingFace</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>首个波斯语音频-语言模型基准，含16项任务（10项新），覆盖语音理解、副语言与文化音频推理。
</div>

## 👥 作者与机构

**Mohammad Javad Ranjbar Kalahroodi** ¹ · Mohammad Amini · Parmis Bathayan · Heshaam Faili · Azadeh Shakery

**机构**：德黑兰大学

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合做多语言/低资源音频-语言模型评测与数据构建的研究者。建议重点看任务分类表与音频vs文本对比实验，以及诗歌韵律任务的分析小节；若只关心建模方法可略读。

## 🌍 研究背景

现有音频-语言模型（LALM）基准以英语为主，波斯语的古典诗歌、传统音乐与普遍语码转换带来的音频理解挑战未被覆盖。此前评测多依赖翻译的英语任务或纯文本基准，无法衡量文化相关的韵律与音乐理解，也缺乏对音频输入相对文本增益的系统诊断。本文构建首个波斯语专用基准以填补该空白。

## 💡 核心创新

1. 首个波斯语音频-语言模型基准，含16项任务、10项全新任务
2. 覆盖语音理解、副语言分析与文化音频推理三类维度
3. 系统对比音频vs文本输入，揭示音频理解为主要瓶颈
4. 发现诗歌韵律任务中音频优于文本，格律检测仅大模型可学

## 🏗️ 模型架构

本文为基准与评测工作，非新模型架构。评测对象为现有LALM（音频-语言模型），输入为波斯语音频或音频+转写文本，输出为各任务答案。任务涵盖语音理解、副语言分析与文化音频推理共16项，通过统一评测流程比较音频输入与纯文本基线，并分析加入转写后对弱模型的提升。

## 📚 数据集

- PARSA-Bench（评测基准，16项任务，公开于HuggingFace）

## 📊 实验结果

摘要未给出具体数值指标。核心发现：多数任务上纯文本基线优于音频基线，说明音频理解而非语言知识是主要瓶颈；同时提供转写可将弱模型提升至接近纯文本水平。例外是波斯诗歌任务，音频在两个诗歌任务上均优于文本，格律检测仅在最大模型规模下显现可学习迹象。

## 🎯 结论与影响

最强结论是：对波斯语LALM而言，音频理解能力而非语言知识是当前主要短板，而诗歌韵律是文本无法替代的音频信息。该基准为低资源语言与文化音频理解评测提供参照，提示后续研究应聚焦音频编码与文化韵律建模；工业上可用于多语言语音助手的文化场景能力评估。

## ⚠️ 局限与未解决问题

作为基准论文，未提出新方法；任务与数据规模、标注一致性、评测协议细节在摘要中未说明；未报告推理延迟或计算成本；音频vs文本对比可能受提示设计影响，缺乏充分消融；波斯语单一语言限制泛化结论。

## 🔗 开源资源

- **HuggingFace**：<https://huggingface.co/datasets/MohammadJRanjbar/PARSA-Bench>
- **数据集**：<https://huggingface.co/datasets/MohammadJRanjbar/PARSA-Bench>

---

<div class="paper-footer"><span>评分：6.5</span><span>原始：6.5</span><a href="/audio-paper-daily/posts/2026-09-16/">← 返回 2026-09-16 速递</a></div>
