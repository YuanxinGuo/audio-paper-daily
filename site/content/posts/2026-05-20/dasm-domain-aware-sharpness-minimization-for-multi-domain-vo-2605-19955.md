---
title: "DASM: Domain-Aware Sharpness Minimization for Multi-Domain Voice Stream Steganalysis"
date: 2026-05-20T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#语音隐写分析"]
summary: "提出域感知锐度最小化（DASM）优化器，通过域监督对比学习与锐度感知优化结合，提升多域语音流隐写分析的泛化能力。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero">
<div class="hero-score">
<div class="score-num">7.5</div>
<div class="score-stars">★★★★☆</div>
<div class="score-tier">前25%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#语音隐写分析</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#域泛化</span> <span class="tag-pill tag-pill-soft">#锐度感知优化</span> <span class="tag-pill tag-pill-soft">#对比学习</span> <span class="tag-pill tag-pill-soft">#语音流</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2605.19955</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-05-20</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2605.19955" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2605.19955" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出域感知锐度最小化（DASM）优化器，通过域监督对比学习与锐度感知优化结合，提升多域语音流隐写分析的泛化能力。
</div>

## 👥 作者与机构

**Pengcheng Zhou** ¹ · Pianran Guo · Shuhua Chen · Mengqin Zhao · Zhongliang Yang · Linna Zhou

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合从事语音安全、隐写分析的研究者阅读。建议重点读§3方法部分和§4实验，尤其是Hessian分析与损失景观可视化。可先看算法伪代码与域自适应调制策略。

## 🌍 研究背景

网络流媒体中隐写术用于隐蔽通信，对安全构成威胁。现有语音流隐写分析方法多依赖特定场景数据分布，难以适应非同源数据分布。通过Hessian分析发现主流模型损失景观存在大量鞍点和尖锐局部极小值，导致对数据分布偏移敏感，泛化能力受限。本文旨在解决跨域泛化问题。

## 💡 核心创新

1. 域监督对比学习与锐度感知优化结合
2. 自适应域间隙调制策略动态调整损失权重
3. 通过Hessian分析揭示模型泛化瓶颈

## 🏗️ 模型架构

输入为网络语音流特征，主干网络未明确指定（可能基于CNN或Transformer）。关键模块：域监督对比学习模块（保留域间特征分离）、锐度感知优化（寻找平坦极小值）、自适应域间隙调制（根据实时特征可分性调整损失权重）。输出为隐写/非隐写分类结果。

## 📚 数据集

- 网络语音流数据集（训练与评估，具体名称未给出）

## 📊 实验结果

摘要未给出具体数值，但声称在多个域上大幅超越现有方法，泛化性和鲁棒性优异。需查看全文获取详细指标。

## 🎯 结论与影响

本文提出的DASM优化器有效提升了多域语音流隐写分析的泛化能力，通过域感知锐度最小化解决了数据分布偏移问题。对语音安全领域的跨域检测有重要推动作用，有望应用于实际网络监控。

## ⚠️ 局限与未解决问题

未报告具体数据集名称和规模，缺乏与现有方法的定量对比表格；未说明主干网络结构及参数量；未讨论计算开销和推理延迟；跨域场景的域定义可能不够清晰。

---

<div class="paper-footer"><span>评分：7.5</span><span>原始：7.5</span><a href="/audio-paper-daily/posts/2026-05-20/">← 返回 2026-05-20 速递</a></div>
