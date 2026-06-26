---
title: "Listening Like a Judge: A Music-Aware Framework for Automatic Singing Performance Evaluation"
date: 2026-06-26T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#歌唱质量评估"]
summary: "提出MusicJudge框架，通过模态引导的多模态分析，结合歌词正确性与音高-节奏保真度，实现自动歌唱质量评估。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#歌唱质量评估</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#多模态</span> <span class="tag-pill tag-pill-soft">#语音识别</span> <span class="tag-pill tag-pill-soft">#音高-节奏</span> <span class="tag-pill tag-pill-soft">#音乐分析</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2606.26451</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-06-26</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2606.26451" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2606.26451" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出MusicJudge框架，通过模态引导的多模态分析，结合歌词正确性与音高-节奏保真度，实现自动歌唱质量评估。
</div>

## 👥 作者与机构

**Neelam Saini** ¹ · Sourav Ghosh

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合从事歌唱评估、多模态语音处理的研究者。建议重点阅读§3的模态引导LoRA微调方法和§4的块对齐多模态分析。可先看表1与图2了解整体框架。

## 🌍 研究背景

自动歌唱质量评估（SQA）需要同时评估歌词正确性和音乐保真度，但现有系统要么仅依赖声学线索，要么仅依赖歌词转录，缺乏整体评估。此外，由于歌唱中存在花腔、颤音和节奏弹性，鲁棒的歌唱转录面临挑战。本文旨在解决这些集成难题，提出一个统一的框架。

## 💡 核心创新

1. 提出MusicJudge框架，实现块对齐的多模态分析
2. 引入多信号匹配检测语义有意义的歌词块
3. 提出Modality-Guided LoRA用于ASR微调，提升歌唱转录鲁棒性

## 🏗️ 模型架构

输入：歌唱音频和歌词文本。主干：多模态分析框架，包含三个模块：1) 块检测模块，通过多信号匹配（语义嵌入、词汇相似性、音素对齐）将音频与歌词对齐并分割成语义块；2) 歌词正确性评估模块，使用Modality-Guided LoRA微调的ASR模型进行转录并计算正确率；3) 音高-节奏保真度评估模块，提取音高和节奏特征与参考对比。输出：每个块的歌词得分和音高-节奏得分，融合得到整体质量评分。

## 📚 数据集

- 公开歌唱数据集（训练与评估）
- 自建专家标注数据集（评估）

## 📊 实验结果

摘要未提供具体数值，但声称在多个数据集上与人类专家判断高度一致，验证了MusicJudge的泛化能力。

## 🎯 结论与影响

MusicJudge通过模态引导的多模态分析，有效整合歌词正确性与音高-节奏保真度，实现了与人类专家高度一致的自动歌唱质量评估。该框架为SQA领域提供了新的范式，有望推动歌唱教学和音乐娱乐等应用。

## ⚠️ 局限与未解决问题

摘要未提及局限。可能的问题：未报告与现有SQA系统的定量对比；未讨论对多种语言或不同歌唱风格的泛化性；未提供推理延迟等效率指标。

---

<div class="paper-footer"><span>评分：7.2</span><span>原始：7.2</span><a href="/audio-paper-daily/posts/2026-06-26/">← 返回 2026-06-26 速递</a></div>
