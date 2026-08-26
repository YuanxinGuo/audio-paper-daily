---
title: "Few-Shot Open-Set Audio Classification via Transductive Prototype Refinement and Class Logit Enhancement"
date: 2026-08-26T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#音频分类"]
summary: "提出两阶段直推式方法，通过潜在内点加权和先验自适应自由能评分，提升少样本开集音频分类性能。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#音频分类</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#少样本学习</span> <span class="tag-pill tag-pill-soft">#开集识别</span> <span class="tag-pill tag-pill-soft">#直推式学习</span> <span class="tag-pill tag-pill-soft">#音频事件分类</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2607.26607</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-08-26</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2607.26607" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2607.26607" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出两阶段直推式方法，通过潜在内点加权和先验自适应自由能评分，提升少样本开集音频分类性能。
</div>

## 👥 作者与机构

**Tianyan Deng** ¹ · Yanxiong Li · Rui Gao · Jiahao Du

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合少样本学习、开集识别和音频分类研究者。建议重点阅读方法部分（§3）和实验对比（§4），可先看表1和表2。

## 🌍 研究背景

少样本开集音频分类要求利用少量标注样本识别已知类，同时拒绝未知类。现有直推式方法在优化原型时未区分已知和未知查询样本，导致原型受开集污染。本文旨在通过潜在内点加权和先验自适应评分，提高原型估计的鲁棒性和开集检测的准确性。

## 💡 核心创新

1. 潜在内点加权：降低未知类样本对原型更新的影响
2. 两阶段直推式优化：结合交叉熵、条件熵最小化和边缘熵最大化
3. 先验自适应自由能评分：根据未知类先验比例调整阈值
4. 解耦检测与分类：提升开集拒绝性能

## 🏗️ 模型架构

使用冻结的音频编码器提取特征，第一阶段计算每个查询样本的潜在内点分数，加权后用于原型细化；第二阶段在细化原型上优化直推式损失，包括支持集交叉熵、内点加权条件熵最小化和边缘熵最大化。开集拒绝采用先验自适应自由能评分。

## 📚 数据集

- AudioSet（评估）
- ESC-50（评估）
- UrbanSound8K（评估）

## 📊 实验结果

摘要未提供具体数值，但声称在三个音频数据集上、多种实验条件下达到最先进水平。具体指标和对比需查阅全文。

## 🎯 结论与影响

本文通过潜在内点加权和先验自适应自由能评分，有效缓解了直推式原型更新中的开集污染问题，在少样本开集音频分类上取得SOTA。该方法为后续研究提供了新思路，有望提升实际场景中音频分类系统的鲁棒性。

## ⚠️ 局限与未解决问题

摘要未提及局限，但可能包括：依赖先验未知类比例、冻结编码器可能限制特征表达、未报告计算开销和推理延迟。

---

<div class="paper-footer"><span>评分：7.8</span><span>原始：7.8</span><a href="/audio-paper-daily/posts/2026-08-26/">← 返回 2026-08-26 速递</a></div>
