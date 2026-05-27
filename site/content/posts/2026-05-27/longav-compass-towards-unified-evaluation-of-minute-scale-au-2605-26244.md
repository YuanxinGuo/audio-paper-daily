---
title: "LongAV-Compass: Towards Unified Evaluation of Minute-Scale Audio-Visual Generation Across T2AV, I2AV, and V2AV"
date: 2026-05-27T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#音视频生成评估"]
summary: "提出首个分钟级音视频生成统一评估基准LongAV-Compass，覆盖T2AV、I2AV、V2AV三种条件，含284个测试用例和20+细粒度评估维度。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero">
<div class="hero-score">
<div class="score-num">8.2</div>
<div class="score-stars">★★★★☆</div>
<div class="score-tier">前25%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#音视频生成评估</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#音视频生成</span> <span class="tag-pill tag-pill-soft">#评估基准</span> <span class="tag-pill tag-pill-soft">#长时生成</span> <span class="tag-pill tag-pill-soft">#多模态评估</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2605.26244</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-05-27</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2605.26244" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2605.26244" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出首个分钟级音视频生成统一评估基准LongAV-Compass，覆盖T2AV、I2AV、V2AV三种条件，含284个测试用例和20+细粒度评估维度。
</div>

## 👥 作者与机构

**Tengfei Liu** ¹ · Yang Shi · Xuanyu Zhu · Jiafu Tang · Liu Yang · Qixun Wang · Zhuoran Zhang · Yuqi Tang · … 等 12 人

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合音视频生成、评估基准研究者阅读。建议重点看§3基准构建方法和§4评估框架，尤其是表1的维度定义和表2的模型对比结果。可跳过§2相关工作。

## 🌍 研究背景

当前音视频生成评估主要针对5-10秒短片段，缺乏对分钟级长时内容的统一评估。现有基准多聚焦文本条件生成，不支持图像/视频条件，且无法衡量身份一致性、叙事连贯性和音视频对齐在长时间尺度上的退化。本文旨在填补这一空白。

## 💡 核心创新

1. 构建284个分钟级测试用例，覆盖T2AV/I2AV/V2AV三种条件
2. 提出分类学引导的基准构建方法
3. 集成MLLM辅助评估与感知/多模态指标（DINO-v2, ArcFace, CLIP, ImageBind）
4. 定义20+细粒度评估维度，涵盖段内质量、跨段一致性、全局叙事连贯性等

## 🏗️ 模型架构

LongAV-Compass是一个评估基准而非生成模型。其评估框架包含：输入（文本/图像/视频）→ 生成模型（11个代表性模型）→ 输出分钟级音视频 → 评估模块：MLLM辅助评估（如GPT-4o）结合感知指标（DINO-v2, ArcFace, CLIP, ImageBind）→ 输出20+维度评分。基准构建采用分类学引导，按应用场景和生成复杂度组织测试用例。

## 📚 数据集

- LongAV-Compass（284个测试用例，用于评估，包含T2AV/I2AV/V2AV三种条件）

## 📊 实验结果

摘要未提供具体数值结果，但提到在11个代表性模型上进行了实验，并通过人类对齐验证了基准的有效性。实验分析了当前系统在分钟级生成中保持连贯性、语义对齐和时间一致性的局限性。

## 🎯 结论与影响

LongAV-Compass是首个分钟级音视频生成统一评估基准，覆盖多种输入条件和20+评估维度，为诊断长时生成系统的缺陷提供了系统工具。该基准有望推动音视频生成从短片段向长时、连贯、多模态方向的发展，对工业界评估和优化长视频生成模型具有实用价值。

## ⚠️ 局限与未解决问题

基准测试用例数量有限（284个），可能无法覆盖所有场景；评估依赖MLLM，存在一定主观性和成本；未提供开源代码或模型权重，可复现性待验证；未讨论评估指标的计算效率。

---

<div class="paper-footer"><span>评分：8.2</span><span>原始：8.2</span><a href="/audio-paper-daily/posts/2026-05-27/">← 返回 2026-05-27 速递</a></div>
