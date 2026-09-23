---
title: "LLM-Anchored Paralinguistic Enrichment for Alzheimer's Disease Detection"
date: 2026-09-23T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#语音识别"]
summary: "提出LAPE框架，将韵律事件文本化后与LLM语言表征融合，用于阿尔茨海默病自动检测，在ADReSS/ADReSSo上取得SOTA。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero">
<div class="hero-score">
<div class="score-num">7.0</div>
<div class="score-stars">★★★★☆</div>
<div class="score-tier">前25%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#语音识别</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#副语言特征</span> <span class="tag-pill tag-pill-soft">#阿尔茨海默病检测</span> <span class="tag-pill tag-pill-soft">#多模态融合</span> <span class="tag-pill tag-pill-soft">#LLM</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2609.10896</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-09-23</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2609.10896" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2609.10896" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出LAPE框架，将韵律事件文本化后与LLM语言表征融合，用于阿尔茨海默病自动检测，在ADReSS/ADReSSo上取得SOTA。
</div>

## 👥 作者与机构

**Xiao Wei** ¹ · Yuqin Lin · Yaru Cao · Jinyu Li · Bin Wen · Kai Li · Yueying Chen · Longbiao Wang · … 等 1 人

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合做病理语音、副语言特征建模与多模态融合的研究者阅读。建议重点看§3的三大模块（韵律事件文本化、词汇-韵律单元化、NormGate融合）与ADReSS/ADReSSo上的四组主实验表。若只关心结论，读摘要与结果表即可；若要做复现，需等代码开源后核对文本化标记的具体实现细节。

## 🌍 研究背景

基于语音的阿尔茨海默病（AD）自动检测是非侵入式早期筛查手段。AD同时影响词汇-语义组织与语音产出（异常停顿、词拉长）。此前方法多依赖手工声学特征（如eGeMAPS）或纯文本ASR转写加语言模型，二者割裂：声学模型忽略语义，语言模型丢弃韵律。如何在LLM语言表征中有效注入停顿、拉长等副语言线索，是本文要解决的核心问题。

## 💡 核心创新

1. 韵律事件文本化：把停顿/拉长编码为带时长感知重复的显式标记，与词汇联合建模
2. 词汇-韵律单元化与分块：仅对连续词单元池化，保留两模态的事件身份与幅度
3. 文本锚定副语言融合：用NormGate对语音特征归一化并按文本动态缩放，融合局部与整句特征

## 🏗️ 模型架构

输入为语音及其ASR转写。先做韵律事件检测，将停顿与词拉长转成带时长感知重复的文本标记，与词汇拼接送入LLM得到语言表征；同时对语音提取局部与整句级副语言特征，经词汇-韵律单元化与分块对齐到词单元；最后用NormGate对语音特征做归一化并以文本表征为锚动态缩放，完成文本锚定的副语言融合，输出用于AD分类的表示。摘要未给出参数量。

## 📚 数据集

- ADReSS（训练/评估，参与者级交叉验证）
- ADReSSo（训练/评估，留一受试者评估）

## 📊 实验结果

摘要仅称LAPE在ADReSS与ADReSSo的全部四个主要设置上取得SOTA，采用参与者级交叉验证与留一受试者（LOSO）评估，但未给出具体指标数值、基线名称或提升幅度，故无法列表对比。需查阅正文确认准确率/F1等指标及消融结果。

## 🎯 结论与影响

最强结论是：将韵律事件显式文本化并与LLM语言表征做文本锚定融合，可在ADReSS/ADReSSo四个主设置上达到SOTA。这提示副语言线索与语言内容应在同一表征空间联合建模，对病理语音检测与更广的副语言感知LLM研究有参考价值；工业上利于低成本、可扩展的认知筛查。

## ⚠️ 局限与未解决问题

摘要未报告具体指标、参数量与推理延迟，也未说明与哪些强基线对比；韵律事件文本化的时长量化粒度、NormGate的消融贡献均未在摘要体现。ADReSS/ADReSSo规模小、以英语为主，跨语言与跨语料泛化性存疑，代码尚未发布。

---

<div class="paper-footer"><span>评分：7.0</span><span>原始：7.0</span><a href="/audio-paper-daily/posts/2026-09-23/">← 返回 2026-09-23 速递</a></div>
