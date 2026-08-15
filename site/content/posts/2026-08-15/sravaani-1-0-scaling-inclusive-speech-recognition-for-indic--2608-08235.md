---
title: "SraVaani 1.0: Scaling Inclusive Speech Recognition for Indic Languages"
date: 2026-08-15T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#语音识别"]
summary: "SraVaani-1.0 是一个覆盖 65 种印度语言和方言的多语言 ASR 模型，通过三阶段训练（自监督预训练、音频-图像对齐、TDT-CTC 微调）在多个基准上取得领先 WER，尤其为低资源语言提供开源识别能力。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#语音识别</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#多语言ASR</span> <span class="tag-pill tag-pill-soft">#自监督预训练</span> <span class="tag-pill tag-pill-soft">#多模态对齐</span> <span class="tag-pill tag-pill-soft">#低资源语言</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2608.08235</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-08-15</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">🔥 强烈推荐通读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2608.08235" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2608.08235" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>SraVaani-1.0 是一个覆盖 65 种印度语言和方言的多语言 ASR 模型，通过三阶段训练（自监督预训练、音频-图像对齐、TDT-CTC 微调）在多个基准上取得领先 WER，尤其为低资源语言提供开源识别能力。
</div>

## 👥 作者与机构

**Sujith Pulikodan** ¹ · Agneedh Basu · Pavan Kumar J · Pranav D Bhat · Suryansh Shukla · Nihar Desai · Prasanta Kumar Ghosh

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合语音识别研究者、多语言 ASR 系统开发者以及关注低资源语言技术的人员。建议重点阅读第 3 节（方法）和第 4 节（实验），特别是三阶段训练策略和 VAANI 基准上的结果。可先看摘要和结论，再深入方法细节。

## 🌍 研究背景

印度拥有超过 700 种语言和数千种方言，但现有 ASR 系统仅支持少数几种，大量低资源语言缺乏可用的识别系统。之前的多语言 ASR 模型如 Whisper、IndicWav2Vec 等主要覆盖高资源语言，对低资源语言性能有限。本文旨在构建一个覆盖 65 种印度语言的多语言 ASR 模型，通过利用 VAANI 语料库中的未标注语音和配对图像，结合自监督预训练和多模态对齐，提升低资源语言的识别性能。

## 💡 核心创新

1. 三阶段训练策略：自监督预训练、音频-图像对齐、TDT-CTC 微调
2. 利用 VAANI 语料库的配对图像进行多模态对齐，增强语义表示
3. 覆盖 65 种语言，包括多种低资源部落语言，开源模型
4. 采用 FastConformer 架构，从零训练

## 🏗️ 模型架构

SraVaani-1.0 基于 FastConformer 架构，输入为 80 维 log-mel 特征。第一阶段使用对比学习目标在 31,255 小时未标注语音上进行自监督预训练。第二阶段引入音频-图像表示对齐，利用 VAANI 语料库中的配对图像和语音，通过多模态对齐增强语音编码器的语义表示。第三阶段使用混合 Token-and-Duration Transducer (TDT) 和 CTC 解码器，在 31,263 小时标注多语言语音上进行端到端微调。模型输出为文本 token 序列。

## 📚 数据集

- VAANI 语料库（未标注语音，31,255 小时，用于自监督预训练）
- VAANI 语料库（配对图像和语音，用于多模态对齐）
- 24 个公开数据集（标注语音，31,263 小时，覆盖 65 种语言，用于微调）
- VAANI 基准（评估低资源语言）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| WER | VAANI 基准 | Whisper large-v3（未给出具体值） | **最低 WER（具体值未给出）** | 未给出 |

摘要中未给出具体 WER 数值，但声称在多个语言-数据集对上取得最低 WER，并在高资源语言上与最佳系统竞争。特别强调是唯一开源且能在 VAANI 基准上评估的低资源部落语言提供转录能力的模型。

## 🎯 结论与影响

SraVaani-1.0 是首个覆盖 65 种印度语言的开源多语言 ASR 模型，显著扩展了 ASR 的语言覆盖范围，尤其为低资源语言提供了可用方案。其多模态对齐策略展示了利用视觉信息提升语音识别的潜力，对后续多语言 ASR 研究具有启发意义。工业上可应用于印度多语言语音交互场景，促进技术普惠。

## ⚠️ 局限与未解决问题

摘要未提及模型参数量、推理延迟等效率指标；对比的基线系统未给出具体数值，削弱了说服力；低资源语言性能可能受限于标注数据质量；多模态对齐仅利用静态图像，未涉及视频等动态信息。

---

<div class="paper-footer"><span>评分：8.2</span><span>原始：8.2</span><a href="/audio-paper-daily/posts/2026-08-15/">← 返回 2026-08-15 速递</a></div>
