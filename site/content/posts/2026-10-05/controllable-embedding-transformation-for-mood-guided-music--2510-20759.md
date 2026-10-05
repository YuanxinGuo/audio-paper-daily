---
title: "Controllable Embedding Transformation for Mood-Guided Music Retrieval"
date: 2026-10-05T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#音乐信息检索"]
summary: "提出情绪引导的音乐嵌入变换框架，通过学习轻量翻译模型将种子音频嵌入映射到目标情绪嵌入，同时保留流派与配器属性。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero">
<div class="hero-score">
<div class="score-num">6.8</div>
<div class="score-stars">★★★☆☆</div>
<div class="score-tier">前50%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#音乐信息检索</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#音乐检索</span> <span class="tag-pill tag-pill-soft">#嵌入变换</span> <span class="tag-pill tag-pill-soft">#可控生成</span> <span class="tag-pill tag-pill-soft">#音乐表示学习</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2510.20759</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-10-05</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2510.20759" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2510.20759" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出情绪引导的音乐嵌入变换框架，通过学习轻量翻译模型将种子音频嵌入映射到目标情绪嵌入，同时保留流派与配器属性。
</div>

## 👥 作者与机构

**Julia Wilkins** ¹ · Jaehun Kim · Matthew E. P. Davies · Juan Pablo Bello · Matthew C. McCallum

**机构**：纽约大学

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合做音乐推荐、可控检索与音乐表示学习的研究者阅读。建议重点看 §3 的代理目标采样机制与联合目标函数设计，以及实验部分的情绪变换成功率与属性保留指标。若只关心语音/音频分离主线，可略读。

## 🌍 研究背景

音乐嵌入是现代推荐系统、歌单生成与相似检索的核心，但现有嵌入（如 CLAP、MERT 等自监督表示）通常只提供整体相似度，难以沿单一属性（如情绪）做可控调整而保持流派、配器不变。已有可控生成多依赖文本提示或训练-free 的嵌入算术，缺乏对属性解耦的显式约束，且情绪无法直接在种子音频上修改，导致监督信号缺失。本文要解决的是：在无配对数据条件下，学习情绪引导的嵌入变换并保留其他音乐属性。

## 💡 核心创新

1. 提出情绪引导的嵌入翻译框架，学习种子嵌入到目标情绪嵌入的映射
2. 设计代理目标采样机制，在多样性与种子相似度间平衡
3. 提出联合目标函数，同时约束变换效果与信息保留
4. 在无配对情绪数据下实现可控音乐检索

## 🏗️ 模型架构

输入为种子音频的预训练音乐嵌入（如 CLAP/MERT 类表示），主干为轻量翻译网络（MLP/Transformer 编码-解码结构），将种子嵌入映射到目标情绪嵌入空间。关键模块包括：代理目标采样器，从数据集中检索与种子相似但情绪标签不同的曲目嵌入作为监督目标；联合损失由变换损失（拉近目标情绪嵌入）与信息保留损失（保持流派、配器属性）组成。输出为变换后的嵌入，用于最近邻检索返回歌曲。摘要未给出具体参数量。

## 📚 数据集

- 两个音乐数据集（训练与评估，具体名称摘要未给出）

## 📊 实验结果

摘要仅说明在两个数据集上取得强情绪变换性能，并在流派与配器保留上显著优于 training-free 基线，但未给出具体指标数值、数据集名称或消融细节，无法量化对比。

## 🎯 结论与影响

本文最强结论是：可控嵌入变换可作为个性化音乐检索的有效范式，在改变情绪的同时较好保留流派与配器。该思路可能推动音乐表示学习从单一相似度走向属性解耦与可控检索，对工业推荐系统的可解释、可调控歌单生成有潜在价值。

## ⚠️ 局限与未解决问题

摘要未给出具体数据集、指标数值与消融实验，代理目标采样对数据分布的依赖未分析；情绪标签噪声与跨数据集泛化性存疑；未报告推理延迟与模型规模，与文本提示类可控方法的对比缺失。

---

<div class="paper-footer"><span>评分：6.8</span><span>原始：6.8</span><a href="/audio-paper-daily/posts/2026-10-05/">← 返回 2026-10-05 速递</a></div>
