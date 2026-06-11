---
title: "A Sensitivity Analysis of Multi-Event Audio Grounding in Audio LLMs"
date: 2026-06-11T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#音频理解"]
summary: "系统评估音频LLM在多事件场景下的事件定位与幻觉行为，发现事件数增加导致TPR下降、FPR上升，提示存在权衡。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#音频理解</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#音频大语言模型</span> <span class="tag-pill tag-pill-soft">#事件检测</span> <span class="tag-pill tag-pill-soft">#幻觉分析</span> <span class="tag-pill tag-pill-soft">#鲁棒性评估</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2603.03855</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-06-11</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2603.03855" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2603.03855" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>系统评估音频LLM在多事件场景下的事件定位与幻觉行为，发现事件数增加导致TPR下降、FPR上升，提示存在权衡。
</div>

## 👥 作者与机构

**Taehan Lee** ¹ · Jaehan Jung · Hyukjun Lee

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合音频LLM鲁棒性研究者。建议重点读§3（查询构建）和§4.2（事件数影响分析），可跳过§2。

## 🌍 研究背景

音频LLM在复杂声场景中的可靠性尚未充分探索。现有工作规模小或查询构建控制不足。本文通过大规模评估，研究事件定位与假警报随场景复杂度的变化，填补了该空白。

## 💡 核心创新

1. 构建71K AudioCapsV2片段并提取归一化事件
2. 设计相似性过滤负采样生成缺席事件查询
3. 使用12种提示变体评估4种SOTA音频LLM
4. 揭示事件数增加导致TPR下降、FPR上升的权衡

## 🏗️ 模型架构

无模型架构，采用评估框架：输入为AudioCapsV2音频片段，通过音频LLM（如Qwen2-Audio、SALMONN等）处理，输出yes/no回答。查询分为存在事件查询（基于真实事件）和缺席事件查询（通过负采样生成）。

## 📚 数据集

- AudioCapsV2（71K片段，用于构建查询和评估）

## 📊 实验结果

摘要未提供具体数值，但指出随着事件数增加，所有模型的true-positive rate下降，false-positive rate上升，且提示词在两者间引入强权衡。置信度分析显示模型在多事件音频上更不确定。

## 🎯 结论与影响

音频LLM在多事件场景下可靠性不足，事件数增加导致检测率下降和幻觉率上升。提示词设计需权衡TPR和FPR。该工作为音频LLM鲁棒性评估提供了大规模基准，推动未来改进。

## ⚠️ 局限与未解决问题

仅使用AudioCapsV2数据集，可能不覆盖所有声场景；未分析模型内部机制；未提供具体指标数值；未比较不同模型架构差异。

---

<div class="paper-footer"><span>评分：6.5</span><span>原始：6.5</span><a href="/audio-paper-daily/posts/2026-06-11/">← 返回 2026-06-11 速递</a></div>
