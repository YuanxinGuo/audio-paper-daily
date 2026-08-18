---
title: "Omni-LiveAvatar: Minute-Level Real-Time Streaming Joint Audio-Visual Avatar Generation"
date: 2026-08-18T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#音频-视觉生成"]
summary: "提出首个分钟级实时流式音视频联合生成框架，通过渐进式自回归蒸馏和长短期记忆实现33倍加速与高质量输出。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero">
<div class="hero-score">
<div class="score-num">8.2</div>
<div class="score-stars">★★★★☆</div>
<div class="score-tier">前25%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#音频-视觉生成</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#流式生成</span> <span class="tag-pill tag-pill-soft">#自回归蒸馏</span> <span class="tag-pill tag-pill-soft">#数字人</span> <span class="tag-pill tag-pill-soft">#长时记忆</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2608.13602</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-08-18</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner"><div class="oc-headline"><span class="oc-pulse"></span><span class="oc-title">本论文已开源</span><span class="oc-hint">点击下方卡片直达对应资源</span></div><div class="oc-grid"><a class="oc-chip oc-chip-code" href="https://github.com/Aoko955/Omni-LiveAvatar" target="_blank" rel="noopener"><span class="oc-icon">💻</span><span class="oc-text"><span class="oc-label">代码仓库</span><span class="oc-sub">Aoko955/Omni-LiveAvatar</span></span></a></div></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2608.13602" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2608.13602" target="_blank" rel="noopener">📑 PDF</a><a class="rsrc rsrc-code" href="https://github.com/Aoko955/Omni-LiveAvatar" target="_blank" rel="noopener">💻 代码</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出首个分钟级实时流式音视频联合生成框架，通过渐进式自回归蒸馏和长短期记忆实现33倍加速与高质量输出。
</div>

## 👥 作者与机构

**Lunjie Zhu** ¹ · Xingtong Ge · Fangyu Lin · Yi Zhang · Zhening Liu · Mengfei Li · Yumeng Zhang · Guanglu Song · … 等 2 人

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合从事数字人、音视频生成、模型压缩的研究者。建议重点阅读第3节的蒸馏方法和第4节的记忆机制，可先看图1和表2。若关注实时交互应用，值得通读。

## 🌍 研究背景

现有音视频联合生成模型多采用双向注意力与多步去噪，生成片段短且无法实时交互。LTX-2等扩散模型虽质量高但推理慢。本文旨在解决长时、实时生成的需求，通过蒸馏和记忆机制实现分钟级流式生成。

## 💡 核心创新

1. 渐进式自回归蒸馏，无需辅助稳定机制
2. 同步音视频长短期记忆，保持全局一致性
3. 层次化滚动提示规划，实现语义连贯过渡

## 🏗️ 模型架构

输入为文本提示和音频特征，主干为自回归生成器，由教师扩散模型LTX-2蒸馏而来。关键模块包括渐进式蒸馏管道、同步音视频长短期记忆模块（LSTM）和层次化滚动提示规划器。输出为同步的音视频流。

## 📊 实验结果

摘要中未提供具体数值指标，仅提及在单块NVIDIA H200上比教师模型LTX-2加速33倍，并在视觉质量、音频质量、跨模态同步和人类保真度上优于加速基线。

## 🎯 结论与影响

本文首次实现分钟级实时流式音视频联合生成，通过蒸馏和记忆机制大幅提升速度与质量，为数字人交互提供新方案。后续可推动实时生成模型在虚拟助手、直播等场景落地。

## ⚠️ 局限与未解决问题

摘要未提及具体数据集和消融实验，缺乏与更多SOTA的对比，未报告推理延迟细节。作为审稿人，需关注蒸馏过程对多样性的影响及长时记忆的容量限制。

## 🔗 开源资源

- **代码**：<https://github.com/Aoko955/Omni-LiveAvatar>

---

<div class="paper-footer"><span>评分：8.2</span><span>原始：8.2</span><a href="/audio-paper-daily/posts/2026-08-18/">← 返回 2026-08-18 速递</a></div>
