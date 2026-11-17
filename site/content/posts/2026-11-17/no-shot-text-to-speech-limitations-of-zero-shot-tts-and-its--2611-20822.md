---
title: "No-Shot Text-to-Speech: Limitations of Zero-Shot TTS and its Evaluation Methods in Representing Queer and Transgender Voices"
date: 2026-11-17T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#语音合成"]
summary: "评测六个零样本TTS模型对性别多元声音的合成表现，发现自动指标与人类感知不一致。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#语音合成</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#零样本TTS</span> <span class="tag-pill tag-pill-soft">#公平性评估</span> <span class="tag-pill tag-pill-soft">#说话人相似度</span> <span class="tag-pill tag-pill-soft">#主观评测</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2611.20822</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-11-16</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2611.20822" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2611.20822" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>评测六个零样本TTS模型对性别多元声音的合成表现，发现自动指标与人类感知不一致。
</div>

## 👥 作者与机构

**Juliana Francis** ¹ · Robin Netzorg · Joakim Gustafson · Éva Székely

**机构**：KTH皇家理工学院

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合做TTS评测、数据集公平性与语音感知的研究者阅读。建议重点看实验设计（数据集构建与听测流程）与自动指标对比部分，尤其是speaker similarity与MOS预测器在GE/N-GE两组上的分歧表；若只关心建模方法可略读。

## 🌍 研究背景

零样本TTS（如基于speaker embedding或in-context learning的方案）已在VALL-E、YourTTS等工作中成为主流，其泛化性依赖训练数据的说话人覆盖。现有语音数据集对性别多元（trans/queer）说话人严重欠代表，可能导致模型对这类声音的合成质量下降。此前评测多依赖自动指标（speaker similarity、MOS预测器），但这些指标是否对人类感知的少数群体声音敏感尚不清楚，本文即针对该盲区做系统评测。

## 💡 核心创新

1. 构建自识别GE与N-GE两组对照评测数据集
2. 六模型×双数据集的零样本TTS人类听测对比
3. 揭示自动speaker similarity与MOS预测器同人评不一致
4. 提出评测流程对性别多元声音的盲区问题

## 🏗️ 模型架构

本文为评测研究，无新模型架构。流程为：选取六个零样本TTS系统（摘要未列具体模型名），输入参考语音与文本，合成目标语句；对N-GE与GE两组自识别说话人数据分别合成。评估分两路：人类听测给出相似度与自然度评分；自动侧使用speaker similarity模型与automated MOS predictor打分，再与人类评分做一致性对比分析。

## 📚 数据集

- 自建N-GE说话人数据集（评估）
- 自建GE自识别说话人数据集（评估）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| 人类相似度评分（模型数统计） | GE vs N-GE 自建集 | N-GE 说话人合成表现 | **6模型中2个对GE更差、3个对GE更好** | 模型间方向不一致 |

人类评分显示六个模型中两个对GE声音合成相似度低于N-GE，三个反而更好，说明模型间差异大。自动评测结果相互冲突：speaker similarity与automated MOS predictor在GE与N-GE间的排序既不一致于彼此，也不一致于人类评分。摘要未给出具体SI-SDR/MOS数值与置信区间。

## 🎯 结论与影响

最强结论是现有零样本TTS评测管线对性别多元声音存在系统性盲区，自动指标不能可靠替代人评。这将推动后续工作构建更具代表性的数据集与感知对齐的评测指标，对工业TTS在少数群体上的质量保障与合规评估有直接提示。

## ⚠️ 局限与未解决问题

摘要未披露具体模型清单、听测人数与评分量表，统计显著性不明；仅六个模型、两组自建数据，规模有限；未分析偏差来源（数据覆盖 vs 声学特性）；缺少对推理成本与跨语言泛化的讨论。

---

<div class="paper-footer"><span>评分：6.8</span><span>原始：6.8</span><a href="/audio-paper-daily/posts/2026-11-17/">← 返回 2026-11-17 速递</a></div>
