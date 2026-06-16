---
title: "WavSLM: Single-Stream Speech Language Modeling via WavLM Distillation"
date: 2026-06-16T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#语音生成"]
summary: "提出WavSLM，通过量化蒸馏WavLM表示到单码本，实现无文本监督的单流自回归语音语言模型。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#语音生成</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#语音语言模型</span> <span class="tag-pill tag-pill-soft">#自监督蒸馏</span> <span class="tag-pill tag-pill-soft">#单流建模</span> <span class="tag-pill tag-pill-soft">#自回归生成</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2603.05299</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-06-16</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2603.05299" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2603.05299" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出WavSLM，通过量化蒸馏WavLM表示到单码本，实现无文本监督的单流自回归语音语言模型。
</div>

## 👥 作者与机构

**Luca Della Libera** ¹ · Cem Subakan · Mirco Ravanelli

**机构**：蒙特利尔大学 · 康考迪亚大学

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合语音生成与自监督学习研究者。重点读§3方法设计与§4实验对比。可先看表1与图2理解单流架构优势。

## 🌍 研究背景

现有语音语言模型多依赖文本监督、分层token流或复杂混合架构，偏离了文本领域成功的单流自回归预训练范式。语音中语义与声学信息的纠缠使得简单扩展困难。本文旨在设计一个无需文本监督、单token流、自回归的语音语言模型，同时建模语义与声学信息。

## 💡 核心创新

1. 单码本量化蒸馏WavLM表示
2. 无文本监督的下一块预测目标
3. 支持流式推理的自回归架构
4. 参数与数据量更少仍达竞争性能

## 🏗️ 模型架构

输入语音经WavLM编码器提取特征，通过量化器映射到单码本离散token序列。采用自回归Transformer以下一块预测目标训练，每个token对应固定时长语音块。输出离散token经解码器合成语音。模型参数量较少，支持流式推理。

## 📚 数据集

- LibriTTS（训练与评估）
- VCTK（评估）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| 一致性（人工评分） | LibriTTS | VALL-E 3.8 | **4.1** | +0.3 |
| 语音质量（MOS） | LibriTTS | VALL-E 3.2 | **3.5** | +0.3 |

WavSLM在LibriTTS和VCTK上的一致性及语音质量MOS均优于VALL-E等基线，且参数量更少、训练数据更少。消融实验验证了单码本蒸馏与下一块预测目标的有效性。

## 🎯 结论与影响

WavSLM证明无需文本监督，单流自回归语音语言模型可达到竞争性能，简化了语音生成范式。对后续研究，该工作可能推动更简洁的语音预训练模型发展。工业上，流式推理特性利于低延迟应用。

## ⚠️ 局限与未解决问题

未报告推理延迟与参数量具体数值；仅评估英文数据集，泛化性未知；与最新模型（如Voicebox）对比缺失；量化码本大小影响未充分探索。

---

<div class="paper-footer"><span>评分：7.8</span><span>原始：7.8</span><a href="/audio-paper-daily/posts/2026-06-16/">← 返回 2026-06-16 速递</a></div>
