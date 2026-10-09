---
title: "SAVU-BENCH: A Real-World Benchmark for Spatial Audio-Visual Understanding"
date: 2026-10-09T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#双耳音频"]
summary: "提出真实场景音视频空间理解基准 SAVU-Bench，含七项任务与诊断集，发现音频空间感知是主要瓶颈。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero hero-focus">
<div class="hero-score">
<div class="score-num">7.8</div>
<div class="score-stars">★★★★☆</div>
<div class="score-tier">前50%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#双耳音频</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#双耳音频</span> <span class="tag-pill tag-pill-soft">#音视频空间理解</span> <span class="tag-pill tag-pill-soft">#基准评测</span> <span class="tag-pill tag-pill-soft">#空间音频感知</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2610.10624</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-10-09</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
<div class="meta-row"><span class="meta-key">⭐</span><span class="meta-val focus-badge">本站重点关注领域 · 评分 +1</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2610.10624" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2610.10624" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出真实场景音视频空间理解基准 SAVU-Bench，含七项任务与诊断集，发现音频空间感知是主要瓶颈。
</div>

## 👥 作者与机构

**Yu Chen** ¹ · Ruihang Liu · Yangguang Xu · Xinyue Jiang · Mohammed Bennamoun · Farid Boussaid · Xinyuan Qian · Qiuhong Ke

**机构**：西澳大学 · 香港城市大学

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合做音视频多模态、空间音频感知与评测的研究者阅读。建议重点看 §3 的三级能力划分与七任务定义、SAVU-Diag 的分解设计，以及 12 个模型的失败模式分析表；若只关心方法可略读 SAVU-EA 部分，因其为 training-free 基线。

## 🌍 研究背景

空间音视频理解要求模型同时判断事件内容、方位及跨模态关系。现有基准多基于模拟场景（如合成 RIR 渲染），只评测孤立空间技能，且缺乏对失败模式的诊断。视觉空间定位已相对成熟，但涉及音频的空间感知仍是瓶颈，缺少真实场景下系统化、可诊断的评测手段。本文要构建真实世界基准并定位失败根源。

## 💡 核心创新

1. 构建真实场景 SAVU-Bench，三级能力、七项评测任务
2. 提出 SAVU-Diag 诊断集，将推理题分解为 grounding 与 alignment 子任务
3. 提出 training-free 的 SAVU-EA 证据增强基线，显式化空间线索

## 🏗️ 模型架构

本文为基准与诊断工作，非单一网络。SAVU-Bench 以真实录制音视频为输入，按三级能力（感知、grounding、推理）组织七项任务，模型需输出事件类别、空间方位及跨模态匹配结果。SAVU-Diag 将每道推理题拆解为前置 grounding 与 alignment 子任务，形成场景关联的诊断链路。SAVU-EA 作为免训练基线，在推理阶段对音频与视觉空间线索做显式增强与拼接，再交由现有多模态大模型作答。摘要未给出参数量。

## 📚 数据集

- SAVU-Bench（真实场景音视频基准，训练/评估，含七项任务）
- SAVU-Diag（场景关联诊断集，评估，分解为 grounding 与 alignment 子任务）

## 📊 实验结果

摘要未给出具体数值指标，仅报告定性结论：在 SAVU-Bench 上评测 12 个代表性模型，视觉空间 grounding 相对成熟，而涉及音频的空间感知是主要瓶颈；SAVU-Diag 显示多数推理错误与前置子任务失败共现，但即使前置任务正确，高层推理仍存在缺口；SAVU-EA 显著提升空间 grounding 与联合匹配，但高层空间推理仍困难。

## 🎯 结论与影响

最强结论是：真实场景下音视频空间理解的核心瓶颈在音频空间感知而非视觉。该基准与诊断集为后续研究提供了可复用的评测与失败归因框架，推动从模拟场景转向真实数据。工业上意味着多模态空间交互产品需优先补强音频空间感知与跨模态空间关系融合。

## ⚠️ 局限与未解决问题

作为基准论文，未提出强方法，SAVU-EA 仅为免训练基线且高层推理提升有限；摘要未报告数据规模、标注一致性、推理延迟与算力开销；12 个模型的选取标准与是否覆盖最新大模型不明；诊断集与主基准的统计相关性缺乏量化。

---

<div class="paper-footer"><span>评分：7.8</span><span>原始：6.8</span><span>+1 重点领域加权</span><a href="/audio-paper-daily/posts/2026-10-09/">← 返回 2026-10-09 速递</a></div>
