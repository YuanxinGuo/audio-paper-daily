---
title: "PromptTTSD: Controllable Text to Spoken Dialogue Synthesis with Open-Ended Text Descriptions"
date: 2026-11-23T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#语音合成"]
summary: "从多播讲有声书构建带开放式风格描述的对话语音数据集PromptDialog，并提出支持零样本克隆与自然语言风格控制的对话合成模型PromptTTSD。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#语音合成</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#对话语音合成</span> <span class="tag-pill tag-pill-soft">#风格可控TTS</span> <span class="tag-pill tag-pill-soft">#零样本语音克隆</span> <span class="tag-pill tag-pill-soft">#数据集构建</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2611.27601</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-11-23</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2611.27601" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2611.27601" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>从多播讲有声书构建带开放式风格描述的对话语音数据集PromptDialog，并提出支持零样本克隆与自然语言风格控制的对话合成模型PromptTTSD。
</div>

## 👥 作者与机构

**Sulong Yang** ¹ · Zhi Zeng · Xiupeng Wu · Juewen Hu · Pring Wong · Shuwu Zhang · Shuo Chen

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合做可控TTS、对话语音合成与语音数据构建的研究者阅读。建议重点看数据构建流水线（两阶段对齐算法与LLM风格描述抽取）以及§方法中的prompt-aware微调如何把风格prompt嵌入文本-语音交错序列；实验部分关注开放式风格控制的对比与多轮上下文适当性评测。

## 🌍 研究背景

对话语音合成需在多轮脚本上生成保持说话人一致且语境贴切的语音。现有prompt-based TTS已能对单说话人做细粒度风格控制，但相关数据集多依赖预定义标签，难以刻画开放式风格；同时对话场景下的风格随上下文动态漂移，现有模型缺乏细粒度可控性。本文要解决的是开放式风格描述驱动的多说话人对话语音合成，以及配套大规模数据缺失的问题。

## 💡 核心创新

1. 从多播讲有声书构建对话语音的可扩展流水线
2. 改进的两阶段对齐算法保持对话连续性
3. LLM从叙述文本直接抽取开放式风格描述
4. prompt-aware微调将风格prompt融入文本-语音交错序列

## 🏗️ 模型架构

输入为对话脚本与自然语言风格描述，二者与语音token组成文本-语音交错序列；风格prompt经编码后与文本、语音序列拼接送入主干TTS模型，通过prompt-aware微调策略实现风格条件注入，输出多说话人对话语音。模型支持零样本音色克隆与自然语言风格控制，摘要未给出参数量与具体主干网络名。

## 📚 数据集

- PromptDialog（训练/评估，8383小时中文+120小时英文对话语音，79%语句带开放式风格描述）

## 📊 实验结果

摘要未给出SI-SDR、PESQ、MOS或WER等具体数值，仅定性说明PromptTTSD在保持基础合成能力的同时，开放式风格控制与专有模型相比具有竞争力，并显著提升多轮对话的上下文适当性。缺少定量表格与消融细节。

## 🎯 结论与影响

最强结论是开放式风格描述可在多说话人对话合成中实现有竞争力的可控性。其数据构建流水线与PromptDialog数据集有望推动对话TTS的风格控制研究，并为有声书转对话语音、角色化语音助手等落地场景提供数据与模型基础。

## ⚠️ 局限与未解决问题

摘要未报告客观指标、主观MOS细节、推理延迟与模型规模；风格控制与专有模型的对比缺乏量化；数据集以中文为主，英文仅120小时，跨语言泛化待验证；两阶段对齐与LLM抽取的误差传播未做消融。

---

<div class="paper-footer"><span>评分：7.2</span><span>原始：7.2</span><a href="/audio-paper-daily/posts/2026-11-23/">← 返回 2026-11-23 速递</a></div>
