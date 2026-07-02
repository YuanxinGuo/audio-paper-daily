---
title: "AV-SyncBench: Decoupled Benchmarking of Temporal and Semantic Audio-Visual Synchronization"
date: 2026-07-02T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#音视频同步评估"]
summary: "提出首个解耦时序与语义的音视频同步基准AV-SyncBench，覆盖语音、音乐、声音10场景，含3269视频38390样本，评估5个代表性模型。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero">
<div class="hero-score">
<div class="score-num">7.5</div>
<div class="score-stars">★★★★☆</div>
<div class="score-tier">前25%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#音视频同步评估</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#音视频同步</span> <span class="tag-pill tag-pill-soft">#多模态特征提取</span> <span class="tag-pill tag-pill-soft">#基准测试</span> <span class="tag-pill tag-pill-soft">#音视频对齐</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2607.00726</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-07-02</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner"><div class="oc-headline"><span class="oc-pulse"></span><span class="oc-title">本论文已开源</span><span class="oc-hint">点击下方卡片直达对应资源</span></div><div class="oc-grid"><a class="oc-chip oc-chip-proj" href="https://fgt7t6g.github.io/AV-SyncBench" target="_blank" rel="noopener"><span class="oc-icon">🌐</span><span class="oc-text"><span class="oc-label">项目主页</span><span class="oc-sub">fgt7t6g.github.io/AV-SyncBench</span></span></a></div></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2607.00726" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2607.00726" target="_blank" rel="noopener">📑 PDF</a><a class="rsrc rsrc-proj" href="https://fgt7t6g.github.io/AV-SyncBench" target="_blank" rel="noopener">🌐 项目主页</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出首个解耦时序与语义的音视频同步基准AV-SyncBench，覆盖语音、音乐、声音10场景，含3269视频38390样本，评估5个代表性模型。
</div>

## 👥 作者与机构

**Tianhong Zhou** ¹ · Mingyang Han · Boyu Li · Yuxuan Jiang · Jiaxin Ye · Dongxiao Wang · Haoxiang Shi · Kunpeng Wang · … 等 3 人

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合多模态学习、音视频同步领域研究者。建议通读，重点看§3基准构建与§4评估任务设计，以及表1数据统计。可复现其评估流程。

## 🌍 研究背景

音视频特征提取是多模态理解与生成的基础，但现有评估协议存在维度偏差：要么只测语义匹配，要么只测时间偏移检测。且数据构建耦合，无法独立评估时序与语义一致性。本文旨在构建首个完全解耦时序与语义评估的音视频同步基准，填补空白。

## 💡 核心创新

1. 首次完全解耦时序与语义同步评估
2. 自动过滤+人工验证确保屏幕内声源
3. 覆盖语音、音乐、声音10场景5挑战任务
4. 提供标准化评估流程与公开数据集

## 🏗️ 模型架构

基准构建流程：从野外视频采集，经自动过滤（如人脸检测、声源定位）和人工验证，确保声源在画面内。数据分为Voice、Music、Sound三类，覆盖10个场景。评估任务包括5个挑战：时序偏移检测、语义匹配、跨模态检索等。评估5个代表性模型（如AV-HuBERT、CAV-MAE等），量化特征质量。

## 📚 数据集

- AV-SyncBench（训练/评估，3269视频，38390样本，含Voice/Music/Sound三类10场景）

## 📊 实验结果

摘要未给出具体数值结果，但提到评估了5个代表性模型，量化特征质量用于对齐和下游任务。具体性能需参考论文正文。

## 🎯 结论与影响

AV-SyncBench是首个解耦时序与语义的音视频同步基准，覆盖多场景多任务，为特征提取模型提供标准化评估。有望推动多模态同步研究，并为工业应用（如视频配音、口型同步）提供可靠评测工具。

## ⚠️ 局限与未解决问题

基准仅覆盖10个场景，可能未涵盖所有现实情况；人工验证虽保证质量但规模有限；未提供模型在基准上的详细性能对比；未讨论跨域泛化能力。

## 🔗 开源资源

- **项目主页**：<https://fgt7t6g.github.io/AV-SyncBench>

---

<div class="paper-footer"><span>评分：7.5</span><span>原始：7.5</span><a href="/audio-paper-daily/posts/2026-07-02/">← 返回 2026-07-02 速递</a></div>
