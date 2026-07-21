---
title: "Efficient Audio-Visual Event Recognition via Knowledge Distillation and Dynamic INT8 Quantization of a Hybrid Cross-Attention Network"
date: 2026-07-21T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#音视频事件识别"]
summary: "提出结合知识蒸馏和动态INT8量化的压缩框架，在音视频事件识别任务上减少59%参数，模型压缩至2.04MB，精度仅降2.14%。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero">
<div class="hero-score">
<div class="score-num">7.2</div>
<div class="score-stars">★★★★☆</div>
<div class="score-tier">前50%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#音视频事件识别</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#知识蒸馏</span> <span class="tag-pill tag-pill-soft">#模型量化</span> <span class="tag-pill tag-pill-soft">#交叉注意力</span> <span class="tag-pill tag-pill-soft">#边缘部署</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2607.16980</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-07-21</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2607.16980" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2607.16980" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出结合知识蒸馏和动态INT8量化的压缩框架，在音视频事件识别任务上减少59%参数，模型压缩至2.04MB，精度仅降2.14%。
</div>

## 👥 作者与机构

**Parinaz Binandeh Dehaghani** ¹ · Danilo Pena · A. Pedro Aguiar

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合关注模型压缩与边缘部署的研究者。重点看§3知识蒸馏与量化方法及表1、表2的精度-效率对比。可复现其压缩流程。

## 🌍 研究背景

音视频事件识别（AVER）在Transformer架构下取得显著进展，但模型计算复杂度和内存占用高，难以部署在边缘设备。现有压缩方法如剪枝、量化、蒸馏多单独使用，缺乏系统性联合优化。本文旨在通过结合架构压缩、知识蒸馏和动态INT8量化，实现高精度与低资源消耗的平衡。

## 💡 核心创新

1. 结合VideoMAE、AST与混合交叉注意力融合的教师模型
2. 轻量学生模型通过降维、减注意力头、缩FFN构建
3. 知识蒸馏传递教师判别性知识
4. 动态INT8后训练量化进一步压缩模型

## 🏗️ 模型架构

教师模型：VideoMAE提取视觉特征，AST提取音频特征，混合交叉注意力融合网络整合多模态特征。学生模型：保持相同架构但降低隐藏维度、注意力头数和FFN大小。训练时学生通过知识蒸馏学习教师输出。最后应用动态INT8后训练量化。融合模块参数量从原始降至59.06%。

## 📚 数据集

- AVE数据集（训练/评估，音视频事件识别）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| 分类准确率 | AVE | 教师模型（未压缩） | **学生模型+蒸馏+量化** | -2.14% |
| 模型大小 | AVE | 教师模型10.71 MB | **2.04 MB** | -80.9% |
| 融合模块参数量减少 | AVE | 教师模型 | **学生模型** | -59.06% |

在AVE数据集上，所提框架在融合模块减少59.06%参数，分类准确率仅下降2.14%。动态INT8量化将模型从10.71MB压缩至2.04MB，保持竞争性性能。未报告推理速度或延迟。

## 🎯 结论与影响

本文证明结合架构压缩、知识蒸馏和动态INT8量化可有效平衡音视频事件识别的精度与效率，为边缘部署提供可行方案。后续可探索更高效的蒸馏策略和量化感知训练。

## ⚠️ 局限与未解决问题

仅在一个数据集（AVE）上评估，泛化性未知；未报告推理延迟或吞吐量；未与现有压缩方法（如剪枝、量化感知训练）对比；学生模型架构设计缺乏消融。

---

<div class="paper-footer"><span>评分：7.2</span><span>原始：7.2</span><a href="/audio-paper-daily/posts/2026-07-21/">← 返回 2026-07-21 速递</a></div>
