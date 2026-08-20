---
title: "Target Speaker Identification: A Low-Latency Streaming Pipeline"
date: 2026-08-20T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#说话人日志"]
summary: "提出一个低延迟流式目标说话人识别流水线，结合流式说话人日志与验证，在播客数据上验证了实时助听器应用的可行性。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#说话人日志</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#目标说话人识别</span> <span class="tag-pill tag-pill-soft">#流式处理</span> <span class="tag-pill tag-pill-soft">#助听器</span> <span class="tag-pill tag-pill-soft">#说话人验证</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2608.17972</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-08-20</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2608.17972" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2608.17972" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出一个低延迟流式目标说话人识别流水线，结合流式说话人日志与验证，在播客数据上验证了实时助听器应用的可行性。
</div>

## 👥 作者与机构

Patrick S. Burke (Children's National Hospital) · Satyam Raj (Arizona State University) · Sean Kinahan (Arizona State University)

**机构**：儿童国家医院 · 亚利桑那州立大学

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合研究助听器低延迟处理或流式说话人日志的读者。可重点阅读第3节（系统设计）和第4节（实验设置），了解Diart与Pyannote的集成及参数调优。若关注实时性，可先看延迟分析部分。

## 🌍 研究背景

助听器应用中，选择性放大目标说话人可提升嘈杂环境下的语音清晰度，但传统离线处理延迟高，无法满足实时需求。现有流式说话人日志方法（如Diart）和验证模型（如Pyannote、TitaNet）各有优劣，但缺乏系统级集成评估。本文旨在构建一个低延迟、实时的目标说话人识别流水线，并验证其可行性。

## 💡 核心创新

1. 提出流式日志+验证的两步流水线
2. 利用播客数据模拟对话场景，选择主持人作为目标
3. 系统级评估采用100ms二进制掩码，贴近实际应用
4. 调优Diart聚类参数以平衡DER与实时性

## 🏗️ 模型架构

输入音频流先经Diart进行流式说话人日志，得到分段和说话人标签；然后对每个分段提取说话人嵌入，与注册的目标说话人嵌入进行余弦相似度比较，通过阈值判定是否为目标。系统采用Pyannote验证模型，并集成Diart的流式处理，实现低延迟。

## 📚 数据集

- This American Life Podcast Transcripts（评估，17个episodes）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| Accuracy | This American Life Podcast | N/A | **>0.90** | N/A |
| Specificity | This American Life Podcast | N/A | **0.95-0.98** | N/A |

系统在17个评估episode上达到中位准确率>0.90，特异性0.95-0.98（余弦阈值0.7-0.75）。离线日志中Pyannote优于LIUM，流式集成Diart后DER有所降低。验证模型ROC曲线显示Pyannote与TitaNet性能相当，但系统级评估仅采用Pyannote。

## 🎯 结论与影响

本文证明了一个基于开源模型的低延迟流式目标说话人识别流水线在助听器场景下的可行性，为后续选择性放大提供了基础。该工作可能推动流式日志与验证模型在实时音频处理中的集成，但距离实际产品还需更多优化和硬件集成。

## ⚠️ 局限与未解决问题

实验仅基于播客数据，未在真实助听器场景或噪声环境下评估；未报告具体延迟数值，仅提及低延迟；未与端到端方法对比；系统级评估仅用单一验证模型，缺乏泛化性验证。

---

<div class="paper-footer"><span>评分：6.8</span><span>原始：6.8</span><a href="/audio-paper-daily/posts/2026-08-20/">← 返回 2026-08-20 速递</a></div>
