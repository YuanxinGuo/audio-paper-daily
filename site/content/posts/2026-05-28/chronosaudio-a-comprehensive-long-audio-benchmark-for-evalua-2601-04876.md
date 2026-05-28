---
title: "ChronosAudio: A Comprehensive Long-Audio Benchmark for Evaluating Audio-Large Language Models"
date: 2026-05-28T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#音频理解"]
summary: "提出首个面向音频大语言模型的长音频多任务基准ChronosAudio，包含6大任务类别、3.6万测试实例、超200小时音频，揭示模型在长上下文中性能严重下降（特定任务超90%退化）及注意力稀释问题。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#音频理解</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#长音频理解</span> <span class="tag-pill tag-pill-soft">#音频大语言模型</span> <span class="tag-pill tag-pill-soft">#基准测试</span> <span class="tag-pill tag-pill-soft">#注意力稀释</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2601.04876</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-05-28</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">🔥 强烈推荐通读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2601.04876" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2601.04876" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出首个面向音频大语言模型的长音频多任务基准ChronosAudio，包含6大任务类别、3.6万测试实例、超200小时音频，揭示模型在长上下文中性能严重下降（特定任务超90%退化）及注意力稀释问题。
</div>

## 👥 作者与机构

**Kaiwen Luo** ¹ · Liang Lin · Yibo Zhang · Moayad Aloqaily · Jialiang Tao · Dexian Wang · Zhenhong Zhou · Junwei Zhang · … 等 3 人

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合ALLM研究者及音频理解领域从业者。建议通读全文，重点看§3（基准设计）、§4（实验结果与发现）及§5（结论与启示）。可先浏览表1-3了解任务分布与模型表现。

## 🌍 研究背景

音频大语言模型（ALLM）在短音频任务上取得显著进展，但长音频理解能力尚未被系统评估。现有基准多聚焦短片段（<30秒），缺乏对长音频（分钟级）的标准化评测。本文旨在填补这一空白，通过构建多任务、多时长分层的基准，系统评估ALLM的长音频理解能力，并揭示其性能退化机制。

## 💡 核心创新

1. 首个专为ALLM设计的长音频多任务基准
2. 36,000实例、超200小时音频，覆盖短/中/长三类时长
3. 发现长上下文性能崩溃（特定任务退化>90%）
4. 揭示注意力稀释是性能退化的根本原因
5. 评估现有缓解策略仅恢复50%性能

## 🏗️ 模型架构

ChronosAudio是一个基准测试框架，而非模型。它包含6大任务类别（如音频问答、事件检测、说话人识别等），测试实例按时长分为短（<30s）、中（30-120s）、长（>120s）三类。评估16个SOTA ALLM（如Qwen2-Audio、SALMONN等），通过标准化指标（准确率、F1等）衡量性能。

## 📚 数据集

- ChronosAudio（训练/评估，36,000实例，超200小时音频，自建）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| 平均性能退化率 | ChronosAudio | 短上下文性能（100%） | **长上下文性能（<10%）** | -90%+ |

实验表明，所有16个ALLM在长音频任务上均出现严重性能退化，特定任务（如细粒度事件检测）退化超90%。注意力分析显示，模型在长序列中注意力分布趋于扩散，丧失时间局部性。现有缓解策略（如位置编码改进、上下文压缩）仅能恢复约50%的性能，远未解决根本问题。

## 🎯 结论与影响

ChronosAudio揭示了ALLM在长音频理解上的严重缺陷：长上下文性能崩溃和注意力稀释。该基准为领域提供了标准化评测工具，并指出当前模型在文档级音频推理上的巨大差距。未来需发展新的架构或训练策略以突破这一瓶颈，对工业级长音频应用（如会议转录、语音日志）具有重要指导意义。

## ⚠️ 局限与未解决问题

基准仅覆盖6类任务，可能未涵盖所有长音频理解场景；未提供模型参数量与性能的详细关联分析；未评估模型在噪声环境下的鲁棒性；未报告推理时间等效率指标。

---

<div class="paper-footer"><span>评分：8.5</span><span>原始：8.5</span><a href="/audio-paper-daily/posts/2026-05-28/">← 返回 2026-05-28 速递</a></div>
