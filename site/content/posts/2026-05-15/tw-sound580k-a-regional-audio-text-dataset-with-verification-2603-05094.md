---
title: "TW-Sound580K: A Regional Audio-Text Dataset with Verification-Guided Curation for Localized Audio-Language Modeling"
date: 2026-05-15T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#数据筛选", "#方言数据集", "#语音理解", "#语音识别", "#音频-语言模型"]
summary: "提出TW-Sound580K，一个台湾地区音频-文本指令数据集，通过验证-生成-批评协议和双ASR验证构建，并基于此微调Tai-LALM模型，在TAU基准上提升6.5%准确率。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#语音理解</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#音频-语言模型</span> <span class="tag-pill tag-pill-soft">#方言数据集</span> <span class="tag-pill tag-pill-soft">#数据筛选</span> <span class="tag-pill tag-pill-soft">#语音识别</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2603.05094</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-05-15</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2603.05094" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2603.05094" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出TW-Sound580K，一个台湾地区音频-文本指令数据集，通过验证-生成-批评协议和双ASR验证构建，并基于此微调Tai-LALM模型，在TAU基准上提升6.5%准确率。
</div>

## 👥 作者与机构

**Hao-Hui Xie** ¹ · Ho-Lam Chung · Yi-Cheng Lin · Ke-Han Lu · Wenze Ren · Xie Chen · Hung-yi Lee

**机构**：National Taiwan University

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合从事音频-语言模型、方言语音处理的研究者。建议重点阅读§3数据构建流程和§4.2动态仲裁策略。可先看表1数据集统计和表2实验结果。

## 🧩 模型一栏概览

| 项 | 内容 |
| --- | --- |
| **应用场景** | 提升大型音频-语言模型对地方方言韵律的理解能力。 |
| **核心创新** | 提出验证-生成-批评协议用于高质量数据集构建 · 双ASR验证过滤低质量音频片段 · 动态双ASR仲裁策略优化推理时转录选择 |
| **模型架构** | Tai-LALM基于DeSTA 2.5-Audio初始化，输入音频经编码器提取特征，与文本指令拼接后送入语言模型。关键模块包括双ASR验证和动态仲裁。参数量未明确给出。 |
| **数据集** | TW-Sound580K（训练，台湾地区音频-文本指令数据集） · TAU Benchmark（评估） |
| **关键结果** | 在TAU Benchmark上，Tai-LALM达到49.1%准确率，相比零样本基线（42.6%）绝对提升6.5%。 |

## 🎯 与本站重点领域的关联

与本站重点领域无直接关联。但数据构建方法（验证-生成-批评协议）可迁移至语音增强或分离任务中的配对数据筛选，动态仲裁策略也可用于多系统融合。

## ⚠️ 局限与未解决问题

数据集仅覆盖台湾地区，泛化性未知；未报告模型参数量和推理延迟；缺乏与更大规模方言数据集的对比；动态仲裁策略的计算开销未分析。

## 📋 引用

```bibtex
@article{xie20262603,
  title  = {TW-Sound580K: A Regional Audio-Text Dataset with Verification-Guided Curation for Localized Audio-Language Modeling},
  author = {Hao-Hui Xie and  Ho-Lam Chung and  Yi-Cheng Lin and  Ke-Han Lu and  Wenze Ren and  Xie Chen and  Hung-yi Lee},
  journal = {arXiv preprint arXiv:2603.05094},
  year   = {2026}
}
```

---

<div class="paper-footer"><span>评分：7.8</span><span>原始：7.8</span><a href="/audio-paper-daily/posts/2026-05-15/">← 返回 2026-05-15 速递</a></div>
