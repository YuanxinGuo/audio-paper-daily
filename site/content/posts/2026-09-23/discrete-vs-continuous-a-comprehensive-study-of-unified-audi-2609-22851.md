---
title: "Discrete vs. Continuous: A Comprehensive Study of Unified Audio Understanding in LALMs"
date: 2026-09-23T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#音频理解"]
summary: "系统对比LALM中连续特征与离散token在语音、声音、音乐理解上的表现，发现语义约束对tokenization至关重要。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero">
<div class="hero-score">
<div class="score-num">6.8</div>
<div class="score-stars">★★★☆☆</div>
<div class="score-tier">前50%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#音频理解</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#音频语言模型</span> <span class="tag-pill tag-pill-soft">#离散token</span> <span class="tag-pill tag-pill-soft">#连续表征</span> <span class="tag-pill tag-pill-soft">#语音理解</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2609.22851</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-09-23</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2609.22851" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2609.22851" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>系统对比LALM中连续特征与离散token在语音、声音、音乐理解上的表现，发现语义约束对tokenization至关重要。
</div>

## 👥 作者与机构

**Jing Peng** ¹ · Zichao Nie · Zhisheng Zhang · Jingran Xie · Zhiyong Wu

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合做LALM表征学习与tokenizer设计的研究者阅读。建议重点看§3的UniARC框架与双评估策略，以及§4中数据量-模型容量-效率的交互分析。若只关心语音增强/分离，可略读；若关注音频理解表征范式，值得通读。

## 🌍 研究背景

LALM通常采用连续音频特征（如Whisper encoder输出）或离散token（如SoundStream/EnCodec量化）作为输入，但哪种范式更适合通用音频理解尚无定论。现有benchmark多聚焦单一领域（仅语音或仅音乐），或在LALM之外单独评估encoder，无法反映端到端LALM中的真实表现。本文旨在统一框架下系统比较两种表征在语音、声音、音乐三类任务上的差异，并分析数据量、模型容量与计算效率的权衡。

## 💡 核心创新

1. 提出UniARC统一评估框架，覆盖语音/声音/音乐三类任务
2. 设计双评估策略，在LALM端到端语境下对比连续与离散表征
3. 系统分析数据量、模型容量与计算效率的动态关系
4. 揭示语义约束tokenization对音频理解的关键作用

## 🏗️ 模型架构

输入为原始音频，分别经连续特征提取器（如Whisper/SSL encoder）或离散tokenizer（如EnCodec/SoundStream量化器）转为表征序列。主干采用SmolLM2-135M至Llama-3-8B等不同规模LLM，通过投影层对齐音频表征与文本空间。输出为文本形式的理解结果。框架UniARC统一了训练与评估流程，支持在相同数据与计算预算下对比两种表征范式，并分析语义密度、保真度与效率的权衡。

## 📚 数据集

- 语音、声音、音乐多领域音频理解数据集（训练/评估，具体名称摘要未给出）

## 📊 实验结果

摘要未给出具体指标数值，仅报告定性结论：语义约束在tokenization中对音频理解起关键作用；扩大LLM主干无法弥补音频表征的信息损失，尤其在数据受限任务中更为明显。实验覆盖SmolLM2-135M到Llama-3-8B多种规模，并分析了数据量、模型容量与计算效率的动态关系。

## 🎯 结论与影响

本文最强结论是：音频表征的语义约束比单纯扩大LLM规模更重要，离散token需引入语义约束才能缩小与连续特征的差距。该发现为未来LALM的tokenizer设计与表征选择提供实证指导，提示工业界在算力受限时应优先优化音频前端而非盲目堆叠LLM参数。

## ⚠️ 局限与未解决问题

摘要未给出具体数据集名称与量化指标，实验可复现性存疑；未报告推理延迟与显存占用等效率细节；连续与离散表征的对比可能受tokenizer训练数据影响，缺乏跨tokenizer的消融；未讨论多模态对齐质量对结论的干扰。

---

<div class="paper-footer"><span>评分：6.8</span><span>原始：6.8</span><a href="/audio-paper-daily/posts/2026-09-23/">← 返回 2026-09-23 速递</a></div>
