---
title: "MedMosaic: A Challenging Large Scale Benchmark of Diverse Medical Audio"
date: 2026-05-29T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#医学音频问答"]
summary: "MedMosaic是一个大规模医学音频问答基准，包含多种音频类型和46,701个问答对，评估13个模型发现推理仍具挑战。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#医学音频问答</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#医学音频</span> <span class="tag-pill tag-pill-soft">#多模态推理</span> <span class="tag-pill tag-pill-soft">#基准数据集</span> <span class="tag-pill tag-pill-soft">#音频问答</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2605.00969</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-05-29</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner"><div class="oc-headline"><span class="oc-pulse"></span><span class="oc-title">本论文已开源</span><span class="oc-hint">点击下方卡片直达对应资源</span></div><div class="oc-grid"><a class="oc-chip oc-chip-demo" href="https://shorturl.at/Lyp33" target="_blank" rel="noopener"><span class="oc-icon">🔊</span><span class="oc-text"><span class="oc-label">在线 Demo</span><span class="oc-sub">shorturl.at/Lyp33</span></span></a></div></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2605.00969" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2605.00969" target="_blank" rel="noopener">📑 PDF</a><a class="rsrc rsrc-demo" href="https://shorturl.at/Lyp33" target="_blank" rel="noopener">🔊 Demo</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>MedMosaic是一个大规模医学音频问答基准，包含多种音频类型和46,701个问答对，评估13个模型发现推理仍具挑战。
</div>

## 👥 作者与机构

**Harshit Rajgarhia** ¹ · Shuubham Ojha · Asif Shaik · Akhil Pothanapalli · Rachuri Lokesh · Abhishek Mukherji · Prasanna Desikan

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合医学AI、多模态推理研究者阅读。重点看§3数据集构建和§4实验结果（表1-3）。可先浏览数据样本链接了解音频多样性。

## 🌍 研究背景

医学音频数据因隐私和标注成本难以收集，现有基准多覆盖简单场景。本文提出MedMosaic，包含生理声、合成伪影语音、长短临床对话等多样音频，并设计多类型问答对，系统评估模型的多跳推理和答案生成能力。

## 💡 核心创新

1. 包含4种医学音频类型（生理声、合成伪影、短/长对话）
2. 46,701个问答对，覆盖多选、多轮、开放问答
3. 系统评估13个音频/多模态模型，揭示推理短板

## 🏗️ 模型架构

数据集而非模型。MedMosaic包含46,701个问答对，音频来源包括公开生理声数据集、合成语音（添加伪影）、真实临床对话。问答类型分多选、顺序多轮、开放问答。评估使用13个基线模型，包括音频编码器+LLM、多模态模型等。

## 📚 数据集

- MedMosaic（训练/评估，46,701问答对，含多种医学音频）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| 准确率 | MedMosaic | Gemini-2.5-pro 68.1% | **N/A（基准数据集，无新方法）** | N/A |

13个模型中，Gemini-2.5-pro最佳（68.1%），但远未饱和；不同问答类型性能差异大，多轮推理最困难。模型在生理声和合成伪影音频上表现较差，表明医学音频推理仍需改进。

## 🎯 结论与影响

MedMosaic揭示了当前多模态模型在医学音频推理上的显著不足，即使最强模型也仅68.1%准确率。该基准将推动领域专用多模态推理模型的发展，对临床辅助诊断有潜在价值。

## ⚠️ 局限与未解决问题

数据集未公开完整音频（仅样本链接），无法复现；未提供人类基线；未分析模型失败原因；音频来源多样性可能受限（如缺乏手术室音频）。

## 🔗 开源资源

- **Demo / 试听**：<https://shorturl.at/Lyp33>

---

<div class="paper-footer"><span>评分：7.2</span><span>原始：7.2</span><a href="/audio-paper-daily/posts/2026-05-29/">← 返回 2026-05-29 速递</a></div>
