---
title: "TW-Sound580K: A Regional Audio-Text Dataset with Verification-Guided Curation for Localized Audio-Language Modeling"
date: 2026-05-15T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#区域方言", "#数据筛选", "#语音语言模型", "#音频文本数据集"]
summary: "提出TW-Sound580K台湾音频文本指令数据集，通过验证-生成-批评协议和双ASR验证筛选，微调DeSTA 2.5得到Tai-LALM，在TAU基准上提升6.5%准确率。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#语音语言模型</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#音频文本数据集</span> <span class="tag-pill tag-pill-soft">#区域方言</span> <span class="tag-pill tag-pill-soft">#语音语言模型</span> <span class="tag-pill tag-pill-soft">#数据筛选</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2603.05094</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-05-15</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2603.05094" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2603.05094" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出TW-Sound580K台湾音频文本指令数据集，通过验证-生成-批评协议和双ASR验证筛选，微调DeSTA 2.5得到Tai-LALM，在TAU基准上提升6.5%准确率。
</div>

## 👥 作者与机构

**Hao-Hui Xie** ¹ · Ho-Lam Chung · Yi-Cheng Lin · Ke-Han Lu · Wenze Ren · Xie Chen · Hung-yi Lee

**机构**：National Taiwan University

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合从事音频语言模型、方言语音处理的研究人员。建议通读，重点看§3数据构建流程（VGC协议）和§4.2双ASR仲裁策略。可复现其数据筛选方法。

## 🌍 研究背景

大型音频语言模型（LALM）在处理区域方言韵律时表现不佳，主要缺乏专门语料库。现有数据集多为通用英语，方言数据稀缺且质量参差不齐。本文针对台湾华语，构建高质量音频文本指令数据集，并设计验证-生成-批评（VGC）协议确保数据质量，同时提出动态双ASR仲裁策略优化推理。

## 💡 核心创新

1. VGC协议：验证-生成-批评三阶段数据筛选
2. 双ASR验证过滤522K原始片段
3. 动态双ASR仲裁策略优化转录选择
4. Tai-LALM模型基于DeSTA 2.5微调

## 🏗️ 模型架构

输入为音频特征，主干网络采用DeSTA 2.5（音频初始化）作为编码器-解码器架构。关键模块包括：VGC协议中双ASR验证（使用两个ASR系统一致性过滤），教师模型生成指令对；推理时动态双ASR仲裁策略选择最佳ASR转录。输出为文本指令响应。参数量未提及。

## 📚 数据集

- TW-Sound580K（训练/评估，580K指令对，源自522K原始片段）
- TAU Benchmark（评估，区域语音理解基准）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| 准确率 | TAU Benchmark | 零样本基线（ASR文本条件）42.6% | **Tai-LALM 49.1%** | +6.5% |

在TAU基准上，Tai-LALM达到49.1%准确率，相比零样本基线（42.6%）提升6.5%。消融实验可能验证了VGC协议和双ASR仲裁的有效性，但摘要未提供更多细节。未报告其他数据集或效率指标。

## 🎯 结论与影响

本文证明通过严格筛选的区域语料库和动态推理策略能显著提升LALM在方言语音上的表现。TW-Sound580K数据集和Tai-LALM为后续区域音频语言建模提供了基础。工业上可用于方言语音助手等场景。

## ⚠️ 局限与未解决问题

摘要未提供消融实验细节，未报告模型参数量、推理延迟等效率指标。数据集仅覆盖台湾华语，泛化性未知。对比基线仅为零样本，缺少与其他微调方法的比较。

---

<div class="paper-footer"><span>评分：7.8</span><span>原始：7.8</span><a href="/audio-paper-daily/posts/2026-05-15/">← 返回 2026-05-15 速递</a></div>
