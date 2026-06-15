---
title: "Spatio-Temporal Audio Language Modeling for Dynamic Sound Sources"
date: 2026-06-15T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#音频问答"]
summary: "提出ST-AudioQA数据集和ST-AudioLM模型，实现动态声源的时空音频问答推理。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero hero-focus">
<div class="hero-score">
<div class="score-num">8.8</div>
<div class="score-stars">★★★★☆</div>
<div class="score-tier">前25%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#音频问答</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#空间音频</span> <span class="tag-pill tag-pill-soft">#声源定位</span> <span class="tag-pill tag-pill-soft">#音频语言模型</span> <span class="tag-pill tag-pill-soft">#双耳音频</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2606.14141</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-06-15</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
<div class="meta-row"><span class="meta-key">⭐</span><span class="meta-val focus-badge">本站重点关注领域 · 评分 +1</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2606.14141" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2606.14141" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出ST-AudioQA数据集和ST-AudioLM模型，实现动态声源的时空音频问答推理。
</div>

## 👥 作者与机构

**Oh Hyun-Bin** ¹ · Kazuki Shimada · Yuhta Takida · Kim Sung-Bin · Toshimitsu Uesaka · Takashi Shibuya · Kyeongyoon Lee · Tae-Hyun Oh · … 等 1 人

**机构**：韩国科学技术院 · 索尼

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合音频语言模型、声源定位和空间音频研究者。建议重点阅读§3数据集构建和§4模型架构，先看表1和表2的对比结果。

## 🌍 研究背景

现有音频语言模型通常将整段音频作为全局事件进行推理，缺乏对声源位置和轨迹的细粒度理解；而声源定位模型虽能跟踪方向，但语义覆盖有限。本文旨在弥合这一鸿沟，通过构建包含静态和移动声源的一阶环绕声渲染数据集，并设计联合学习语义与轨迹的音频编码器，实现时空音频问答。

## 💡 核心创新

1. 构建ST-AudioQA数据集，含密集轨迹标注和时空问题
2. 提出ST-Audio Encoder，联合学习事件语义与源轨迹
3. 设计ST-AudioLM，连接音频token与LLM进行时空推理
4. 在语义-定位权衡上优于静态和定位基线

## 🏗️ 模型架构

输入为FOA音频，经ST-Audio Encoder（基于Conformer的时间分辨率编码器）提取音频token，同时输出事件语义和轨迹信息；这些token通过连接层送入预训练LLM（如LLaMA），进行时空音频问答。模型参数量未在摘要中给出。

## 📚 数据集

- ST-AudioQA（训练/评估，基于SpatialSounD和AudioSet的FOA渲染，含静态和移动声源）

## 📊 实验结果

摘要未提供具体数值结果，但声称ST-AudioLM在语义-定位权衡上优于静态空间基线和纯定位基线，推理性能更强。

## 🎯 结论与影响

本文通过ST-AudioQA数据集和ST-AudioLM模型，首次将动态声源的时空信息融入音频语言推理，为音频问答和空间理解提供了新范式。后续可推动具身智能和虚拟现实中的音频场景理解。

## ⚠️ 局限与未解决问题

摘要未报告推理延迟、模型参数量或跨数据集泛化实验；数据集基于模拟渲染，真实场景泛化性未知；未与最新音频语言模型（如LTU、Qwen-Audio）对比。

---

<div class="paper-footer"><span>评分：8.8</span><span>原始：7.8</span><span>+1 重点领域加权</span><a href="/audio-paper-daily/posts/2026-06-15/">← 返回 2026-06-15 速递</a></div>
