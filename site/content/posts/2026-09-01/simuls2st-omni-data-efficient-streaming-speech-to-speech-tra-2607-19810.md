---
title: "SimulS2ST-Omni: Data-Efficient Streaming Speech-to-Speech Translation via Explicit Trajectory Supervision"
date: 2026-09-01T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#语音翻译"]
summary: "提出一种数据高效的流式语音到语音翻译训练方案，通过联合文本-代码轨迹监督和双流Thinker-Talker架构，在仅约2k小时配对数据下达到与闭源系统相当的翻译质量。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#语音翻译</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#流式语音翻译</span> <span class="tag-pill tag-pill-soft">#多任务学习</span> <span class="tag-pill tag-pill-soft">#轨迹监督</span> <span class="tag-pill tag-pill-soft">#语音语言模型</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2607.19810</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-09-01</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2607.19810" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2607.19810" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出一种数据高效的流式语音到语音翻译训练方案，通过联合文本-代码轨迹监督和双流Thinker-Talker架构，在仅约2k小时配对数据下达到与闭源系统相当的翻译质量。
</div>

## 👥 作者与机构

**Rongshen He** ¹ · Xinyu Liang · Dekun Chen · Jiaqi Li · Mingjie Chen · Zhizheng Wu

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合语音翻译、语音语言模型和流式生成研究者阅读。建议重点阅读第3节的训练方案和第4节的架构设计，以及第5节的实验对比。可先看摘要和结论，再深入方法部分。

## 🌍 研究背景

流式语音到语音翻译（S2ST）需要在严格延迟约束下进行增量、无界翻译。现有方法通常受限于句子级监督或需要大量配对S2ST数据。本文旨在解决数据效率问题，利用辅助多任务训练和联合轨迹监督，在少量配对数据下实现高质量流式翻译。

## 💡 核心创新

1. 联合文本-代码轨迹监督，统一目标文本和声学语义码的预测路径
2. 双流Thinker-Talker分解，解耦语言推理与声学预测，减少模态干扰
3. 数据高效训练方案，仅需约2k小时配对数据，且对配对数据预算减少90%仍鲁棒

## 🏗️ 模型架构

系统基于语音语言模型，采用编码器-解码器架构。输入为源语言语音，通过编码器提取特征，然后由Thinker流进行语言推理生成目标文本，Talker流基于文本和声学语义码进行声学预测。训练时使用联合轨迹监督，将文本和声学码作为统一目标序列。推理时采用流式解码，支持长句和长对话。

## 📚 数据集

- RealSI（评估）
- ACL60/60-dev（评估）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| ASR-BLEU | RealSI | LiveInterpret 2.0（闭源） | **匹配** | 持平 |
| ASR-BLEU | ACL60/60-dev | LiveInterpret 2.0（闭源） | **匹配** | 持平 |

实验表明，所提系统在RealSI和ACL60/60-dev上取得了与闭源SOTA系统LiveInterpret 2.0相当的ASR-BLEU，同时具有竞争力的质量-延迟权衡。消融研究验证了联合轨迹监督和双流分解的有效性，且当配对数据预算减少90%时性能依然稳健。

## 🎯 结论与影响

本文提出的数据高效流式S2ST训练方案，通过联合轨迹监督和双流架构，在少量配对数据下实现了与闭源系统相当的性能，为流式S2ST提供了新思路。该方法有望降低数据需求，推动流式翻译的实用化。

## ⚠️ 局限与未解决问题

摘要未提供具体数值，对比仅提及ASR-BLEU，缺乏其他指标（如翻译质量、延迟）的详细数据。未讨论对低资源语言对的泛化能力，也未报告推理效率（如实时因子）。

---

<div class="paper-footer"><span>评分：8.2</span><span>原始：8.2</span><a href="/audio-paper-daily/posts/2026-09-01/">← 返回 2026-09-01 速递</a></div>
