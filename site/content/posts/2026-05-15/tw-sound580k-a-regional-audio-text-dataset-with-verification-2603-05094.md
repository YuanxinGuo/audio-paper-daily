---
title: "TW-Sound580K: A Regional Audio-Text Dataset with Verification-Guided Curation for Localized Audio-Language Modeling"
date: 2026-05-15T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#语音识别"]
summary: "提出TW-Sound580K台湾语音-文本指令数据集，通过验证-生成-批评协议和双ASR验证构建，微调DeSTA 2.5模型在TAU基准上提升6.5%准确率。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#语音识别</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#音频语言模型</span> <span class="tag-pill tag-pill-soft">#方言语音</span> <span class="tag-pill tag-pill-soft">#数据构建</span> <span class="tag-pill tag-pill-soft">#语音识别</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2603.05094</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-05-15</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2603.05094" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2603.05094" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出TW-Sound580K台湾语音-文本指令数据集，通过验证-生成-批评协议和双ASR验证构建，微调DeSTA 2.5模型在TAU基准上提升6.5%准确率。
</div>

## 👥 作者与机构

**Hao-Hui Xie** ¹ · Ho-Lam Chung · Yi-Cheng Lin · Ke-Han Lu · Wenze Ren · Xie Chen · Hung-yi Lee

**机构**：台湾大学

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合从事音频语言模型、方言语音处理的研究者。建议通读，重点看§3数据构建流程和§4.2动态双ASR仲裁策略。可复现其数据筛选方法。

## 🌍 研究背景

大型音频语言模型在处理方言韵律时表现不佳，主要缺乏专用语料库。现有数据集多为通用英语，台湾语音资源稀缺。本文旨在构建高质量台湾语音-文本指令数据集，并验证其对LALM性能的提升。

## 💡 核心创新

1. 提出Verify-Generate-Critique数据构建协议
2. 采用Dual-ASR验证过滤低质量音频
3. 引入动态Dual-ASR仲裁策略优化推理
4. 构建TW-Sound580K台湾语音指令数据集

## 🏗️ 模型架构

输入音频经Whisper和Wav2Vec2.0双ASR系统验证后，由教师模型生成指令对。微调阶段使用DeSTA 2.5-Audio初始化主干，推理时采用动态Dual-ASR仲裁选择最佳转录。

## 📚 数据集

- TW-Sound580K（训练，580K指令对）
- TAU Benchmark（评估，台湾语音理解任务）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| 准确率 | TAU Benchmark | 零样本基线42.6% | **49.1%** | +6.5% |

在TAU基准上，Tai-LALM达到49.1%准确率，相比零样本基线提升6.5%。消融实验验证了VGC协议和动态仲裁的有效性，但摘要未提供更多细节。

## 🎯 结论与影响

TW-Sound580K数据集和Tai-LALM模型证明，结合区域语料库、严格筛选和动态仲裁可显著提升LALM在本地化语音上的性能。该工作为方言音频语言建模提供了数据构建范式和基线。

## ⚠️ 局限与未解决问题

仅针对台湾语音，泛化性未知；未报告模型参数量和推理延迟；缺乏与其他方言数据集的对比；未开源代码和模型。

---

<div class="paper-footer"><span>评分：7.8</span><span>原始：7.8</span><a href="/audio-paper-daily/posts/2026-05-15/">← 返回 2026-05-15 速递</a></div>
