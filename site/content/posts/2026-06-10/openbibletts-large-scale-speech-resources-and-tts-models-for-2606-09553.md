---
title: "OpenBibleTTS: Large-Scale Speech Resources and TTS Models for Low-Resource Languages"
date: 2026-06-10T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#语音合成"]
summary: "OpenBibleTTS 是一个覆盖37种低资源语言的语音合成基准，系统比较了多种TTS架构，发现无单一模型在所有语言和指标上占优。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#语音合成</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#低资源TTS</span> <span class="tag-pill tag-pill-soft">#多语言语音合成</span> <span class="tag-pill tag-pill-soft">#开源数据集</span> <span class="tag-pill tag-pill-soft">#语音生成</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2606.09553</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-06-10</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2606.09553" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2606.09553" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>OpenBibleTTS 是一个覆盖37种低资源语言的语音合成基准，系统比较了多种TTS架构，发现无单一模型在所有语言和指标上占优。
</div>

## 👥 作者与机构

David Guzm\'an · Luel Hagos Beyene · Jesujoba Oluwadara Alabi · Yejin Jeon · Dietrich Klakow · David Ifeoluwa Adelani

**机构**：萨里大学 · 亚的斯亚贝巴大学 · 萨尔大学 · 蒙特利尔大学

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合低资源TTS研究者阅读。建议重点看§3数据集构建和§4实验对比，尤其是表2和表3的跨语言/跨领域结果。可先读§4.2主观评测部分。

## 🌍 研究背景

神经TTS在高质量语言上表现优异，但低资源语言研究常使用人工降采样数据，无法反映真实拼写变异和音系覆盖不足。现有模型仍以高资源语言为主，缺乏大规模、多语言低资源TTS基准。本文旨在构建覆盖37种低资源语言的语音资源库，并系统评估多种TTS架构在域内和域外文本上的表现。

## 💡 核心创新

1. 构建37种低资源语言的语音数据集OpenBibleTTS
2. 系统比较多种TTS架构（如EveryVoice、Gemini-TTS）
3. 引入域外文本评估，揭示泛化差距
4. 开源全部数据集、对齐和训练模型

## 🏗️ 模型架构

本文比较多种TTS架构：EveryVoice（基于FastPitch的端到端模型）、Gemini-TTS（大规模多语言生成模型）、以及从零训练的Transformer TTS。输入为文本，经音素编码后送入声学模型生成梅尔谱，再通过声码器合成波形。EveryVoice使用单语言训练，Gemini-TTS为多语言预训练。参数量因模型而异。

## 📚 数据集

- OpenBibleTTS（37种低资源语言，训练/评估，包含圣经文本和语音对齐）
- 域外文本（来自新闻、维基百科等，评估泛化）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| MOS（主观听感评分） | OpenBibleTTS域内测试集 | EveryVoice（单语）: 3.8 | **Gemini-TTS: 4.2** | +0.4 |
| WER（词错误率） | OpenBibleTTS域内测试集 | Gemini-TTS: 15.2% | **EveryVoice: 8.7%** | -6.5% |
| MOS | 域外文本 | EveryVoice: 2.5 | **Gemini-TTS: 3.1** | +0.6 |

在域内测试中，Gemini-TTS在多数语言上获得更高MOS，但EveryVoice在可懂度（WER）上更优，尤其在非洲语言上。域外文本上，所有模型性能下降，从零训练的模型退化严重，表明多语言覆盖与可靠合成质量之间存在差距。

## 🎯 结论与影响

OpenBibleTTS为低资源TTS提供了大规模基准，揭示无单一模型在所有语言和指标上占优。未来研究需平衡多语言覆盖与域外泛化能力。开源资源将推动低资源TTS发展，尤其对非洲语言社区有实际意义。

## ⚠️ 局限与未解决问题

数据集仅基于圣经文本，域外泛化有限；未报告推理延迟和模型参数量；对比模型未包含最新扩散TTS或VITS；主观评测样本量可能不足。

---

<div class="paper-footer"><span>评分：7.8</span><span>原始：7.8</span><a href="/audio-paper-daily/posts/2026-06-10/">← 返回 2026-06-10 速递</a></div>
