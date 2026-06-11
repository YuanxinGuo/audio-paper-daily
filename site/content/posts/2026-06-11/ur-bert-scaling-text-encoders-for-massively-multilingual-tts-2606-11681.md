---
title: "UR-BERT: Scaling Text Encoders for Massively Multilingual TTS Through Universal Romanization and Speech Token Prediction"
date: 2026-06-11T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#文本到语音合成"]
summary: "提出UR-BERT，通过通用罗马化表示和语音token预测目标，将TTS文本编码器扩展到495种语言。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#文本到语音合成</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#多语言TTS</span> <span class="tag-pill tag-pill-soft">#罗马化</span> <span class="tag-pill tag-pill-soft">#语音token预测</span> <span class="tag-pill tag-pill-soft">#文本编码器</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2606.11681</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-06-11</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2606.11681" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2606.11681" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出UR-BERT，通过通用罗马化表示和语音token预测目标，将TTS文本编码器扩展到495种语言。
</div>

## 👥 作者与机构

**Sangmin Lee** ¹ · Eekgyun Ahn · Woongjib Choi · Hong-Goo Kang

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合多语言TTS研究者。建议重点阅读第3节方法（罗马化策略和语音token预测）及第4节实验（跨语言和低资源性能）。可先看表1、2对比基线。

## 🌍 研究背景

多语言TTS系统通常依赖G2P转换，但可靠G2P资源仅覆盖约100种语言，限制了扩展性。现有方法如多语言BERT或音素编码器在低资源语言上表现不佳。本文旨在通过统一罗马化表示和语音感知预训练，实现大规模多语言TTS文本编码器。

## 💡 核心创新

1. 通用罗马化表示统一495种书写系统
2. 语音token预测目标增强文本-语音对齐
3. 数据高效的预训练策略，无需G2P资源

## 🏗️ 模型架构

UR-BERT基于BERT架构，输入为罗马化后的字符序列。主干网络为Transformer编码器，关键模块包括：1) 罗马化映射层将不同书写系统转为共享子词单元；2) 语音token预测头，在预训练阶段预测对应语音的离散token（来自HuBERT或类似模型）。输出为文本编码表示，供下游TTS解码器使用。模型参数量未明确给出。

## 📚 数据集

- 多语言TTS数据集（训练，涵盖495种语言，具体规模未提及）
- 未见语言测试集（评估泛化能力）

## 📊 实验结果

摘要未提供具体数值，但声称UR-BERT在多种语言和资源条件下持续优于近期文本编码器基线，并在未见语言上展现强泛化能力。具体指标（如MOS、WER）未给出。

## 🎯 结论与影响

UR-BERT通过罗马化和语音token预测，实现了495种语言的TTS文本编码，显著扩展了多语言TTS的覆盖范围。该方法对低资源语言和未见语言的泛化能力表明其在实际多语言TTS系统中的潜力，可能推动全球语言包容性语音合成的发展。

## ⚠️ 局限与未解决问题

摘要未提及局限。可能的问题：1) 罗马化可能丢失原始书写系统的语音细节；2) 语音token预测依赖预训练语音tokenizer，其质量影响性能；3) 未报告推理速度或模型大小；4) 缺乏与端到端多语言TTS系统的直接对比。

---

<div class="paper-footer"><span>评分：8.2</span><span>原始：8.2</span><a href="/audio-paper-daily/posts/2026-06-11/">← 返回 2026-06-11 速递</a></div>
