---
title: "Phoenix TTS: High-Fidelity Synthesis and Voice Conversion via Flow-Matching-Driven Speech Tokenization"
date: 2026-08-14T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#语音合成"]
summary: "Phoenix TTS通过联合优化语音分词器与流匹配生成模型，弥合离散令牌与连续声学空间差距，实现高保真零样本语音合成与转换。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#语音合成</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#语音合成</span> <span class="tag-pill tag-pill-soft">#语音转换</span> <span class="tag-pill tag-pill-soft">#流匹配</span> <span class="tag-pill tag-pill-soft">#语音分词器</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2608.11737</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-08-14</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">🔥 强烈推荐通读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2608.11737" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2608.11737" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>Phoenix TTS通过联合优化语音分词器与流匹配生成模型，弥合离散令牌与连续声学空间差距，实现高保真零样本语音合成与转换。
</div>

## 👥 作者与机构

**Peijie Chen** ¹ · Zhuanling Zha · Zhipeng Nie · Weijie Wu · Yiming Liu · Daiyu Huang · Junbo Li · Jun Fang · … 等 3 人

**机构**：厦门大学 · 字节跳动

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合语音合成、语音转换及生成式音频建模研究者阅读。建议重点阅读第3节（方法）和第4节（实验），特别是分词器联合训练与流匹配损失的设计。可先看摘要与图表，再深入方法细节。

## 🌍 研究背景

当前零样本TTS系统常采用语义分词器（如ASR或自监督训练），但语音中语义与声学信息难以完全解耦，ASR分词器丢弃声学细节导致说话人相似度不足。此外，这些分词器独立优化，缺乏下游声学生成任务的直接监督，造成离散令牌与连续声学空间的特征鸿沟，限制合成质量上限。Phoenix TTS旨在通过联合优化分词器与流匹配模型，弥合这一鸿沟，提升合成质量与说话人相似度。

## 💡 核心创新

1. 联合优化分词器与流匹配损失，对齐特征空间
2. 分词器重建自监督特征以保持语义丰富性
3. 统一框架支持零样本语音转换，无需微调
4. 110K小时数据训练，WER低于真实录音
5. 高效训练，兼顾可懂度与说话人相似度

## 🏗️ 模型架构

Phoenix TTS采用联合训练框架，包含语音分词器和流匹配生成模型。分词器编码语音为离散令牌，优化目标包括重建自监督特征（如WavLM）以保留语义，同时接收流匹配损失监督，使令牌空间与流匹配模型的特征空间对齐。流匹配模型基于令牌条件生成声学特征，最终通过声码器合成波形。整体框架端到端训练，实现高保真合成。

## 📚 数据集

- 110K小时语音数据（训练）
- LibriSpeech（评估，用于WER）
- VCTK（评估，用于说话人相似度）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| WER | LibriSpeech test-clean | Ground truth 2.5% | **2.1%** | -0.4% |
| SIM | VCTK | YourTTS 0.82 | **0.85** | +0.03 |

实验表明，Phoenix TTS在110K小时数据上训练后，合成语音的WER低于真实录音，表明可懂度极高。在零样本说话人相似度上，与多个大规模基线相比，达到或超越其性能。此外，统一训练的分词器可直接用于零样本语音转换，无需任务特定微调，展示了良好的泛化能力。

## 🎯 结论与影响

Phoenix TTS通过联合优化分词器与流匹配模型，有效弥合了离散令牌与连续声学空间的鸿沟，显著提升了零样本语音合成的可懂度与说话人相似度，并自然支持语音转换。该框架为语音生成提供了一种新范式，有望推动高保真TTS和VC的工业应用，并启发后续研究在表示学习与生成建模的深度融合。

## ⚠️ 局限与未解决问题

论文未提及推理延迟和模型参数量，可能影响实际部署评估。实验仅报告了WER和相似度，缺乏主观MOS评测。此外，训练数据规模大，但未说明数据来源和多样性，可能存在领域偏差。联合训练策略的消融实验未详细展示，难以评估各组件贡献。

---

<div class="paper-footer"><span>评分：8.2</span><span>原始：8.2</span><a href="/audio-paper-daily/posts/2026-08-14/">← 返回 2026-08-14 速递</a></div>
