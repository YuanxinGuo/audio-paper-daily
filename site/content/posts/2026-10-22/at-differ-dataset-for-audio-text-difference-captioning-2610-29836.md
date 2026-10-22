---
title: "AT-Differ: Dataset for Audio-Text Difference Captioning"
date: 2026-10-22T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#音频文本对齐"]
summary: "提出音频-文本差异描述任务并构建AT-DIFFER数据集，微调多模态大模型以文本描述音频与文本间的差异。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero">
<div class="hero-score">
<div class="score-num">6.8</div>
<div class="score-stars">★★★☆☆</div>
<div class="score-tier">中等</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#音频文本对齐</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#音频文本对齐</span> <span class="tag-pill tag-pill-soft">#多模态大语言模型</span> <span class="tag-pill tag-pill-soft">#数据集构建</span> <span class="tag-pill tag-pill-soft">#音频描述</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2610.29836</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-10-22</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2610.29836" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2610.29836" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出音频-文本差异描述任务并构建AT-DIFFER数据集，微调多模态大模型以文本描述音频与文本间的差异。
</div>

## 👥 作者与机构

**Akihiro Fujii** ¹ · Yuki Okamoto · Yuki Saito · Hiroshi Saruwatari

**机构**：东京大学

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合做音频-语言对齐评估、音频描述生成的研究者阅读。值得浏览，重点看 §3 数据集构建流程（差异模拟方式与标注协议）与 §4 微调实验及评估指标设计。若关注 MLLM 音频理解能力边界，可精读实验与错误分析部分。

## 🌍 研究背景

音频-文本语义对齐评估是音频-语言任务的基础环节，现有方法（如 CLIP 类对比模型、音频描述指标）多输出单一相似度分数，只能判断'是否匹配'，无法说明音频与文本在哪些属性上不一致。这种黑箱式打分在需要可解释反馈的场景（如生成音频的描述校验、数据清洗）中不够用。本文提出音频-文本差异描述任务，要求模型用自然语言指出音频与给定文本之间的具体差异，并为此构建带系统化模拟差异与对应描述的数据集。

## 💡 核心创新

1. 提出 audio-text difference captioning 新任务
2. 构建 AT-DIFFER 数据集，系统化模拟差异并配描述
3. 微调现有多模态大模型以生成差异描述

## 🏗️ 模型架构

输入为一段音频与其对应的文本描述，二者存在人为注入的差异（如事件、属性、时序层面的改动）。音频经编码器转为声学表征，与文本 token 一同送入现有多模态大语言模型（MLLM）主干，通过指令式提示让模型生成描述差异的自然语言。作者在 AT-DIFFER 上对该模型进行监督微调，输出为差异描述文本。摘要未给出具体参数量与网络细节。

## 📚 数据集

- AT-DIFFER（本文构建，含系统化模拟差异的音频-文本对及差异描述，用于训练与评估）

## 📊 实验结果

摘要仅给出定性结论：原始多模态大模型描述音频-文本差异的能力有限，而在 AT-DIFFER 上微调后该能力显著提升。未报告具体指标数值、基线名称或消融结果，因此无法量化改进幅度。

## 🎯 结论与影响

本文最强结论是：差异描述能力并非现成 MLLM 的固有强项，但可通过针对性数据集微调显著获得。这为音频-文本对齐评估从单一分数走向可解释描述提供了新范式，对音频描述生成、数据质量审核等落地场景有潜在价值。

## ⚠️ 局限与未解决问题

差异由系统化模拟注入，与真实场景中自然产生的音频-文本不一致分布可能存在偏差；摘要未给出量化指标、基线对比与消融，评估协议与人工评价细节不明；未报告推理开销与模型规模。

---

<div class="paper-footer"><span>评分：6.8</span><span>原始：6.8</span><a href="/audio-paper-daily/posts/2026-10-22/">← 返回 2026-10-22 速递</a></div>
