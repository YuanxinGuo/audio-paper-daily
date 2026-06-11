---
title: "NaijaS2ST: A Multi-Accent Benchmark for Speech-to-Speech Translation in Low-Resource Nigerian Languages"
date: 2026-06-11T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#语音翻译"]
summary: "NaijaS2ST是一个面向尼日利亚四种低资源语言的语音翻译基准数据集，包含约50小时/语言的平行语音数据，并评估了级联、端到端和AudioLLM方法。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#语音翻译</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#低资源语言</span> <span class="tag-pill tag-pill-soft">#多口音</span> <span class="tag-pill tag-pill-soft">#语音到语音翻译</span> <span class="tag-pill tag-pill-soft">#数据集</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2604.16287</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-06-11</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2604.16287" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2604.16287" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>NaijaS2ST是一个面向尼日利亚四种低资源语言的语音翻译基准数据集，包含约50小时/语言的平行语音数据，并评估了级联、端到端和AudioLLM方法。
</div>

## 👥 作者与机构

**Marie Maltais** ¹ · Yejin Jeon · Min Ma · Shamsuddeen Hassan Muhammad · Idris Abdulmumin · Maryam Ibrahim Mukhtar · Daud Abolade · Joel Okepefi · … 等 2 人

**机构**：Meta · 卡内基梅隆大学 · 谷歌

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合语音翻译、低资源NLP研究者阅读。建议重点看§3数据集构建和§4实验设置，以及表2-4的基准结果。可先读摘要和结论，再深入方法对比。

## 🌍 研究背景

低资源语言的语音翻译因缺乏高质量平行语音数据而受限，尤其在非洲语言中。现有数据集多关注高资源语言或单一口音，缺乏多口音、多语言的基准。本文构建了NaijaS2ST数据集，覆盖伊博语、豪萨语、约鲁巴语和尼日利亚皮钦语，每种语言约50小时，包含丰富的说话人和口音变化，旨在推动低资源多语言语音翻译研究。

## 💡 核心创新

1. 构建了首个多口音尼日利亚语言语音翻译数据集NaijaS2ST
2. 系统比较了级联、端到端和AudioLLM三种范式
3. 发现AudioLLM在语音到文本翻译中优于级联和端到端方法
4. 揭示了语音到语音翻译中级联和AudioLLM性能相当

## 🏗️ 模型架构

本文未提出新模型架构，而是构建数据集并评估多种现有方法。级联方法使用Whisper进行ASR，NLLB-200进行文本翻译，以及Tacotron2或VITS进行TTS。端到端方法基于Transformer编码器-解码器。AudioLLM方法使用Qwen2-Audio，通过few-shot示例进行翻译。

## 📚 数据集

- NaijaS2ST（训练/评估，约50小时/语言，包含伊博语、豪萨语、约鲁巴语、尼日利亚皮钦语与英语平行语音）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| BLEU | NaijaS2ST (语音到文本) | 级联 (Whisper+NLLB) 约20.0 | **AudioLLM (Qwen2-Audio) 约25.0** | +5.0 |
| ASR-BLEU | NaijaS2ST (语音到语音) | 级联 约15.0 | **AudioLLM 约15.0** | 0.0 |

实验表明，在语音到文本翻译中，AudioLLM（Qwen2-Audio）在BLEU上显著优于级联和端到端方法，提升约5个点。但在语音到语音翻译中，级联和AudioLLM性能相当，ASR-BLEU均约15.0，说明该任务仍有较大改进空间。数据集包含多口音，但未报告口音层面的细分结果。

## 🎯 结论与影响

NaijaS2ST为低资源尼日利亚语言语音翻译提供了高质量数据集和系统基准。AudioLLM在语音到文本任务中表现最佳，但语音到语音翻译仍需更专门的模型。该工作有望推动低资源多语言语音翻译研究，并为工业界开发面向非洲语言的翻译系统提供基础。

## ⚠️ 局限与未解决问题

数据集仅覆盖四种尼日利亚语言，未包含其他非洲语言。语音到语音翻译的评估仅使用ASR-BLEU，缺乏主观听感测试。未报告模型推理延迟或参数量。未进行跨数据集泛化实验。

---

<div class="paper-footer"><span>评分：7.2</span><span>原始：7.2</span><a href="/audio-paper-daily/posts/2026-06-11/">← 返回 2026-06-11 速递</a></div>
