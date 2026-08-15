---
title: "CASA: Content-Acoustic Speaking Assessment with Speech Encoder and Large Language Model"
date: 2026-08-15T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#语音评估"]
summary: "提出CASA，结合Whisper-medium和Qwen3.5-2B，在口语评估中取得SOTA，并分离内容与声学贡献。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero">
<div class="hero-score">
<div class="score-num">7.8</div>
<div class="score-stars">★★★★☆</div>
<div class="score-tier">前25%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#语音评估</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#自动口语评估</span> <span class="tag-pill tag-pill-soft">#大语言模型</span> <span class="tag-pill tag-pill-soft">#语音编码器</span> <span class="tag-pill tag-pill-soft">#可解释性</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2608.13101</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-08-15</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2608.13101" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2608.13101" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出CASA，结合Whisper-medium和Qwen3.5-2B，在口语评估中取得SOTA，并分离内容与声学贡献。
</div>

## 👥 作者与机构

**Nhan Phan** ¹ · Ilona L\"ahteenm\"aki · Anna von Zansen · Olli-Pekka Pauna · Yaroslav Getman · Tam\'as Gr\'osz · Mikko Kurimo

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合口语评估、语音+LLM多模态研究者。建议重点阅读第3节架构和第4节消融分析，可先看表2和表3了解性能与稳定性。

## 🌍 研究背景

自动口语评估（ASA）常采用多模态语音大语言模型，但现有研究对声学与内容信息如何贡献预测、性能稳定性分析不足。之前SOTA方法可能依赖复杂结构或大量参数。本文旨在提出更简单架构，实现SOTA性能，同时提供可解释的声学与内容分离，并分析稳定性。

## 💡 核心创新

1. 结合Whisper-medium和Qwen3.5-2B的轻量架构
2. 利用三个手工设计的流利度特征增强声学信息
3. 通过消融和重复运行分析声学与内容贡献
4. 利用LLM推理实现无需训练的内容验证

## 🏗️ 模型架构

输入语音经Whisper-medium提取声学特征和文本转录，结合三个手工流利度特征，送入Qwen3.5-2B语言模型进行评分。输出为预测分数。整体参数约为先前最佳的一半。

## 📚 数据集

- Speak & Improve Corpus 2025（评估）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| RMSE | Speak & Improve Corpus 2025 | 先前最佳（未给出具体值） | **0.358** | 优于先前最佳 |

CASA在Speak & Improve Corpus 2025上取得RMSE 0.358，优于先前最佳，且推理参数减半。消融实验显示声学和内容信息互补，重复运行分析性能稳定性，并展示LLM推理用于内容验证的潜力。

## 🎯 结论与影响

CASA以更简单架构实现SOTA，并增强可解释性，分离声学与内容贡献。对后续研究，其通用架构可适配其他ASA语料库，LLM推理内容验证为无训练评估提供新思路。工业上可降低部署成本。

## ⚠️ 局限与未解决问题

摘要未提及推理延迟、跨语料库泛化实验，且仅在一个数据集上评估。手工流利度特征可能引入主观性，需进一步验证。

---

<div class="paper-footer"><span>评分：7.8</span><span>原始：7.8</span><a href="/audio-paper-daily/posts/2026-08-15/">← 返回 2026-08-15 速递</a></div>
