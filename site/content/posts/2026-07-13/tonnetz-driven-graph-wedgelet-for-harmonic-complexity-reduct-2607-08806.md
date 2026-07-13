---
title: "Tonnetz-Driven Graph Wedgelet for Harmonic Complexity Reduction in Music Scores"
date: 2026-07-13T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#音乐分析"]
summary: "提出一种基于Tonnetz嵌入和二分楔形树的图压缩方法，用于简化钢琴子图和声复杂度，生成可读可演奏的简化乐谱。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#音乐分析</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#图神经网络</span> <span class="tag-pill tag-pill-soft">#音乐压缩</span> <span class="tag-pill tag-pill-soft">#和声简化</span> <span class="tag-pill tag-pill-soft">#符号音乐</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2607.08806</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-07-13</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2607.08806" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2607.08806" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出一种基于Tonnetz嵌入和二分楔形树的图压缩方法，用于简化钢琴子图和声复杂度，生成可读可演奏的简化乐谱。
</div>

## 👥 作者与机构

**Emmanuel Caronna** ¹ · Elisa Francomano · Silvia Licciardi

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合音乐信息检索（MIR）和符号音乐处理研究者阅读。重点看§3的楔形树构建算法和§4的Tonnetz嵌入部分。可先浏览图2的压缩流程概览。

## 🌍 研究背景

符号音乐乐谱可建模为异构图，包含音符、歌词音节和伴奏事件，用于和声分析、声部分离等任务。现有方法多直接处理完整乐谱，计算复杂度高且和声信息冗余。本文旨在通过图压缩降低和声复杂度，同时保留任务相关信息与图结构，生成简化乐谱。

## 💡 核心创新

1. 基于Tonnetz六维嵌入的二分楔形树分割
2. 自适应贪婪算法递归最小化L²误差
3. 以和声距离作为分裂准则
4. 分段常数函数重建简化乐谱

## 🏗️ 模型架构

输入为钢琴子图（音符节点及边），每个音符映射到六维Tonnetz嵌入空间。通过全自适应贪婪算法递归构建二分楔形树，在每个节点以和声距离为准则分裂，最小化L²误差。最终每个楔形区域用均值常数表示，生成简化乐谱。

## 📚 数据集

- 三位作曲家（未具体说明）的符号音乐乐谱语料库（实验评估）

## 📊 实验结果

摘要未提供具体数值结果，仅提及在三位作曲家的语料库上进行了实验评估，但未给出量化指标（如压缩率、重构误差等）。

## 🎯 结论与影响

本文提出的Tonnetz驱动图楔形树方法能有效降低音乐乐谱的和声复杂度，生成可读可演奏的简化版本。该方法为音乐分析和计算音乐学提供了新的工具，未来可扩展到其他乐器子图或更复杂的音乐结构。

## ⚠️ 局限与未解决问题

实验仅在三位作曲家的语料库上评估，缺乏大规模基准测试；未与现有乐谱简化方法（如基于规则或深度学习）进行定量对比；未报告计算效率或压缩率等关键指标。

---

<div class="paper-footer"><span>评分：6.5</span><span>原始：6.5</span><a href="/audio-paper-daily/posts/2026-07-13/">← 返回 2026-07-13 速递</a></div>
