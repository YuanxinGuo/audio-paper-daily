---
title: "Omni-Embed-Audio: Leveraging Multimodal LLMs for Robust Audio-Text Retrieval"
date: 2026-07-09T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#音频-文本检索"]
summary: "提出Omni-Embed-Audio，利用多模态大语言模型提升音频-文本检索的鲁棒性，并设计用户意图查询和硬负样本挖掘方法进行系统评估。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#音频-文本检索</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#多模态大语言模型</span> <span class="tag-pill tag-pill-soft">#对比学习</span> <span class="tag-pill tag-pill-soft">#鲁棒性评估</span> <span class="tag-pill tag-pill-soft">#负样本挖掘</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2604.18360</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-07-09</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2604.18360" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2604.18360" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出Omni-Embed-Audio，利用多模态大语言模型提升音频-文本检索的鲁棒性，并设计用户意图查询和硬负样本挖掘方法进行系统评估。
</div>

## 👥 作者与机构

**HaeJun Yoo** ¹ · Yongseop Shin · Insung Lee · Myoung-Wan Koo · Du-Seong Chang

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合音频检索、多模态学习领域的研究者。建议重点阅读§3（UIQ设计）和§4.2（硬负样本挖掘与评估指标），实验部分关注表2和表3的对比结果。

## 🌍 研究背景

现有音频-文本检索系统（如CLAP）在标准基准上表现良好，但查询形式多为描述性字幕，与真实用户搜索行为（如问题、命令、关键词）差异大，导致鲁棒性评估不足。本文旨在利用多模态大语言模型的语义理解能力，提升检索系统对多样化查询的鲁棒性，并引入更贴近实际场景的评估方法。

## 💡 核心创新

1. 提出Omni-Embed-Audio，基于多模态LLM的检索编码器
2. 设计五类用户意图查询（UIQ）模拟真实搜索行为
3. 开发硬负样本挖掘管道及判别指标（HNSR, TFR）
4. 在文本-文本检索上相对提升22%
5. 硬负样本判别HNSR@10提升4.3个百分点

## 🏗️ 模型架构

输入音频和文本分别编码：音频通过预训练音频编码器（如HTSAT）提取特征，文本通过多模态LLM（如LLaVA）的文本编码器处理；两者映射到共享嵌入空间，采用对比学习训练。主干网络为多模态LLM，关键模块包括音频编码器、LLM文本编码器及投影层。输出为音频和文本的联合嵌入向量。

## 📚 数据集

- AudioCaps（训练/评估，约50k音频-文本对）
- Clotho（训练/评估，约5k音频-文本对）
- MECAT（评估，约1k音频-文本对）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| T2A Recall@1 | AudioCaps | M2D-CLAP 52.3 | **51.8** | -0.5 |
| T2T Recall@1 | AudioCaps | M2D-CLAP 68.1 | **83.1** | +22.0% relative |
| HNSR@10 | AudioCaps | M2D-CLAP 63.2 | **67.5** | +4.3%p |
| TFR@10 | AudioCaps | M2D-CLAP 0.95 | **1.28** | +34.7% relative |

OEA在标准文本到音频检索上与SOTA M2D-CLAP持平（AudioCaps T2A R@1 51.8 vs 52.3），但在文本到文本检索上显著领先（+22%相对提升），并在硬负样本判别上表现突出（HNSR@10提升4.3个百分点，TFR@10提升34.7%），表明LLM骨干增强了复杂查询的语义理解。

## 🎯 结论与影响

Omni-Embed-Audio通过多模态LLM实现了对多样化查询的鲁棒检索，尤其在文本-文本检索和硬负样本判别上优势明显。该工作为音频检索系统提供了更贴近实际应用的评估范式，并展示了LLM在音频理解中的潜力，对工业级检索系统的鲁棒性提升有参考价值。

## ⚠️ 局限与未解决问题

未报告模型参数量和推理延迟；仅评估了三个数据集，泛化性待验证；UIQ设计依赖人工定义，可能未覆盖所有真实查询类型；与纯音频模型相比，LLM引入的计算开销未讨论。

---

<div class="paper-footer"><span>评分：7.8</span><span>原始：7.8</span><a href="/audio-paper-daily/posts/2026-07-09/">← 返回 2026-07-09 速递</a></div>
