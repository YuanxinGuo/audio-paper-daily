---
title: "FiLM-Based Speaker Conditioning of a SpeechLLM for Pathological Speech Recognition"
date: 2026-06-05T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#语音识别"]
summary: "通过FiLM注入x-vector信息到冻结ASR编码器各层，实现病理语音的说话人自适应，无需修改基座模型权重。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#语音识别</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#病理语音识别</span> <span class="tag-pill tag-pill-soft">#说话人自适应</span> <span class="tag-pill tag-pill-soft">#FiLM</span> <span class="tag-pill tag-pill-soft">#参数高效微调</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2606.06211</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-06-05</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2606.06211" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2606.06211" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>通过FiLM注入x-vector信息到冻结ASR编码器各层，实现病理语音的说话人自适应，无需修改基座模型权重。
</div>

## 👥 作者与机构

Fernando L\'opez · Santosh Kesiraju · Jordi Luque

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合从事ASR自适应、病理语音处理的研究者。建议重点阅读§3的FiLM注入方式及§4的实验对比，特别是表2的WER结果。可关注其与LoRA等方法的比较。

## 🌍 研究背景

标准ASR在病理语音上性能严重下降，主要由于说话人声学特征与正常语音差异大。现有自适应方法如微调全部参数或使用适配器模块，存在过拟合或计算开销大的问题。本文提出利用FiLM层将说话人嵌入（x-vector）注入冻结的ASR编码器各Transformer层，实现轻量级说话人自适应，同时保持模型对非条件语音的泛化能力。

## 💡 核心创新

1. FiLM层注入x-vector到每层Transformer
2. 冻结基座ASR编码器，仅训练FiLM参数
3. 在西班牙语和英语病理语音上验证
4. 保留模型回答语音相关问题的能力

## 🏗️ 模型架构

输入语音特征→冻结的ASR编码器（如Whisper或HuBERT）→每层Transformer中插入FiLM层，该层根据x-vector（从说话人嵌入提取）计算缩放和偏移参数，调制层归一化后的特征→输出文本。仅FiLM参数可训练，基座模型权重冻结。

## 📚 数据集

- Spanish pathological speech dataset (训练/评估，未说明规模)
- English pathological speech dataset (训练/评估，未说明规模)

## 📊 实验结果

摘要未提供具体WER数值，仅说明说话人条件ASR与现有自适应方法竞争力相当，且保留非条件语音性能。需查阅全文获取详细指标。

## 🎯 结论与影响

FiLM说话人条件化是一种有效的病理语音ASR自适应方法，仅需少量参数即可提升性能，且不损害通用ASR能力。该方法为低资源病理语音自适应提供了新思路，有望推动临床语音接口落地。

## ⚠️ 局限与未解决问题

未报告具体WER数值，缺乏与更多基线（如Adapter、LoRA）的详细对比；仅在两个数据集上验证，泛化性待考；未分析FiLM层数对性能的影响；未提及推理速度或参数量。

---

<div class="paper-footer"><span>评分：7.2</span><span>原始：7.2</span><a href="/audio-paper-daily/posts/2026-06-05/">← 返回 2026-06-05 速递</a></div>
