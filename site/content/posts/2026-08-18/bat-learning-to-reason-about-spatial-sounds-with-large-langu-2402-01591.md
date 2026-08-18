---
title: "BAT: Learning to Reason about Spatial Sounds with Large Language Models"
date: 2026-08-18T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#双耳音频"]
summary: "BAT结合双耳声学场景分析模型与LLM，实现空间声音推理，并构建了空间声音QA数据集SpatialSoundQA。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero hero-focus">
<div class="hero-score">
<div class="score-num">9.2</div>
<div class="score-stars">★★★★★</div>
<div class="score-tier">前25%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#双耳音频</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#空间音频推理</span> <span class="tag-pill tag-pill-soft">#大语言模型</span> <span class="tag-pill tag-pill-soft">#双耳音频</span> <span class="tag-pill tag-pill-soft">#声音事件检测</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2402.01591</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-08-18</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
<div class="meta-row"><span class="meta-key">⭐</span><span class="meta-val focus-badge">本站重点关注领域 · 评分 +1</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2402.01591" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2402.01591" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>BAT结合双耳声学场景分析模型与LLM，实现空间声音推理，并构建了空间声音QA数据集SpatialSoundQA。
</div>

## 👥 作者与机构

**Zhisheng Zheng** ¹ · Puyuan Peng · Ziyang Ma · Xie Chen · Eunsol Choi · David Harwath

**机构**：德克萨斯大学奥斯汀分校 · 西北工业大学 · 上海交通大学

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合从事双耳音频、声音事件定位与检测（SELD）以及多模态LLM的研究者。建议重点阅读第3节（Spatial-AST架构）和第4节（BAT模型与训练），以及第5节的实验对比。可先看摘要和结论，再深入方法部分。

## 🌍 研究背景

空间声音推理是人类基本技能，但现有模型多限于声音事件检测或定位，缺乏对声音间空间关系的推理能力。此前SELD任务通常使用专用模型，难以进行自然语言交互。本文旨在结合双耳声学分析模型与LLM，实现空间声音的感知与推理，并解决缺乏野外空间声音数据的问题。

## 💡 核心创新

1. 提出Spatial-AST，一种新的空间音频编码器，在SELD任务上表现优异
2. 构建SpatialSoundQA数据集，包含多种空间声音QA任务
3. 将Spatial-AST与LLaMA-2 7B集成，实现空间声音推理
4. 利用AudioSet和SoundSpaces 2.0合成双耳音频数据集
5. 在空间声音感知和推理任务上超越现有方法

## 🏗️ 模型架构

BAT由声学前端编码器Spatial-AST和LLM（LLaMA-2 7B）组成。Spatial-AST基于音频频谱图Transformer，处理双耳音频输入，输出声音事件、空间位置和距离的表示。该编码器通过预训练和微调在SELD任务上达到强性能。随后，Spatial-AST的输出与文本指令一起输入LLM，LLM进行推理并生成文本回答。

## 📚 数据集

- AudioSet（用于合成双耳音频，训练Spatial-AST）
- SoundSpaces 2.0（用于合成双耳音频，训练Spatial-AST）
- SpatialSoundQA（训练和评估BAT的空间声音QA任务）

## 📊 实验结果

摘要未提供具体数值，但声称BAT在空间声音感知和推理任务上表现优越，Spatial-AST在声音事件检测、空间定位和距离估计上均取得强性能。实验展示了BAT在SELD任务上的能力，并强调了LLM在复杂空间音频环境中的潜力。

## 🎯 结论与影响

BAT成功将双耳声学感知与LLM推理结合，实现了空间声音的感知与推理，展示了LLM在空间音频理解中的巨大潜力。该工作为空间音频推理提供了新范式，有望推动智能助听、机器人导航等应用的发展。

## ⚠️ 局限与未解决问题

摘要未提及局限，但可推测：合成数据与真实场景存在域差距；SpatialSoundQA的规模可能有限；未报告推理延迟和计算成本；与真实世界复杂声学环境的泛化性有待验证。

---

<div class="paper-footer"><span>评分：9.2</span><span>原始：8.2</span><span>+1 重点领域加权</span><a href="/audio-paper-daily/posts/2026-08-18/">← 返回 2026-08-18 速递</a></div>
