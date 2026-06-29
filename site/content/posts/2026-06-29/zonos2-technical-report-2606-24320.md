---
title: "ZONOS2 Technical Report"
date: 2026-06-29T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#语音合成"]
summary: "ZONOS2 8B 是一款基于 MoE 架构的大规模 TTS 模型，在自然度、韵律和语音克隆保真度上达到 SOTA，并开源模型权重。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero">
<div class="hero-score">
<div class="score-num">8.5</div>
<div class="score-stars">★★★★☆</div>
<div class="score-tier">前25%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#语音合成</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#文本转语音</span> <span class="tag-pill tag-pill-soft">#语音克隆</span> <span class="tag-pill tag-pill-soft">#混合专家模型</span> <span class="tag-pill tag-pill-soft">#语音合成</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2606.24320</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-06-29</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">🔥 强烈推荐通读</span></div>
</div>
</div>

<div class="opensource-banner"><div class="oc-headline"><span class="oc-pulse"></span><span class="oc-title">本论文已开源</span><span class="oc-hint">点击下方卡片直达对应资源</span></div><div class="oc-grid"><a class="oc-chip oc-chip-code" href="https://github.com/Zonos-org/zonos2" target="_blank" rel="noopener"><span class="oc-icon">💻</span><span class="oc-text"><span class="oc-label">代码仓库</span><span class="oc-sub">Zonos-org/zonos2</span></span></a><a class="oc-chip oc-chip-hf" href="https://huggingface.co/Zonos-org/zonos2-8b" target="_blank" rel="noopener"><span class="oc-icon">🤗</span><span class="oc-text"><span class="oc-label">HuggingFace</span><span class="oc-sub">🤗 Zonos-org/zonos2-8b</span></span></a></div></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2606.24320" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2606.24320" target="_blank" rel="noopener">📑 PDF</a><a class="rsrc rsrc-code" href="https://github.com/Zonos-org/zonos2" target="_blank" rel="noopener">💻 代码</a><a class="rsrc rsrc-hf" href="https://huggingface.co/Zonos-org/zonos2-8b" target="_blank" rel="noopener">🤗 HuggingFace</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>ZONOS2 8B 是一款基于 MoE 架构的大规模 TTS 模型，在自然度、韵律和语音克隆保真度上达到 SOTA，并开源模型权重。
</div>

## 👥 作者与机构

**Gabriel Clark** ¹ · Sofian Mejjoute · Mohamed Osman · George Close · Beren Millidge

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合 TTS 研究人员和工程师阅读。建议重点看 §3 模型架构（MoE 设计）和 §4 数据处理流程，以及表 1-3 的客观/主观评测结果。可先通读摘要和结论，再深入实验部分。

## 🌍 研究背景

文本转语音（TTS）领域近年来发展迅速，但现有模型在自然度、韵律和语音克隆保真度上仍有提升空间。之前的 SOTA 模型如 VALL-E、NaturalSpeech 3 等参数量大、推理延迟高。ZONOS2 8B 旨在通过扩大模型规模、优化数据质量和训练策略，在保持低延迟的同时提升合成质量。

## 💡 核心创新

1. 混合专家（MoE）骨干网络，8B 总参数量仅 900M 激活参数
2. 训练语料从 200K 小时扩展至 6M+ 小时的新数据处理流水线
3. 简化后训练和条件配方以提升自然度和语音克隆保真度
4. 提出 ZTTS1-Eval 基准用于 TTS 评估

## 🏗️ 模型架构

输入文本经 tokenizer 编码后送入 MoE 骨干网络，该网络包含多个专家模块，通过门控网络动态选择激活专家（900M 激活参数）。模型采用自回归解码器生成 mel 频谱，再经声码器合成波形。后训练阶段使用简化的条件配方（如说话人嵌入、韵律控制）。总参数量 8B，支持流式推理。

## 📚 数据集

- 内部数据集（训练，6M+ 小时多语言语音）
- ZTTS1-Eval（评估，新提出的 TTS 基准）
- LibriTTS（评估，用于 WER 和相似度测试）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| MOS（自然度） | ZTTS1-Eval | Zonos-v0.1 4.2 | **4.5** | +0.3 |
| 说话人相似度（SPK-SIM） | ZTTS1-Eval | Zonos-v0.1 0.85 | **0.91** | +0.06 |
| WER（%） | LibriTTS test-clean | Zonos-v0.1 3.2 | **2.8** | -0.4 |

ZONOS2 8B 在 ZTTS1-Eval 上 MOS 达 4.5，说话人相似度 0.91，均优于 Zonos-v0.1。在 LibriTTS test-clean 上 WER 为 2.8%，低于基线。模型支持流式推理，延迟满足实时需求。消融实验验证了 MoE 架构和数据规模扩展的有效性。

## 🎯 结论与影响

ZONOS2 8B 通过 MoE 架构和大规模数据训练，在 TTS 自然度、韵律和语音克隆上达到 SOTA，且推理高效。该工作表明扩大模型规模和优化数据质量仍是提升 TTS 性能的关键路径。开源模型权重将推动社区研究和应用落地。

## ⚠️ 局限与未解决问题

论文未报告跨语言泛化能力；仅与自家基线对比，缺乏与 VALL-E、NaturalSpeech 3 等外部 SOTA 的公平比较；未提供详细推理延迟数据；ZTTS1-Eval 基准的构建细节和公开性未说明。

## 🔗 开源资源

- **代码**：<https://github.com/Zonos-org/zonos2>
- **HuggingFace**：<https://huggingface.co/Zonos-org/zonos2-8b>

---

<div class="paper-footer"><span>评分：8.5</span><span>原始：8.5</span><a href="/audio-paper-daily/posts/2026-06-29/">← 返回 2026-06-29 速递</a></div>
