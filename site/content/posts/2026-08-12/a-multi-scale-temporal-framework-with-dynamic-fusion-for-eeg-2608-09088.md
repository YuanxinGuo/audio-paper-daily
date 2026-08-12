---
title: "A Multi-Scale Temporal Framework with Dynamic Fusion for EEG-Based Emotion Recognition"
date: 2026-08-12T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#情感识别"]
summary: "提出多尺度时间框架，用共享注意力编码器和动态融合模块处理EEG信号，在二分类和三分类情感识别中优于全信号基线。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero">
<div class="hero-score">
<div class="score-num">6.5</div>
<div class="score-stars">★★★☆☆</div>
<div class="score-tier">前50%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#情感识别</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#EEG</span> <span class="tag-pill tag-pill-soft">#多尺度时间建模</span> <span class="tag-pill tag-pill-soft">#动态融合</span> <span class="tag-pill tag-pill-soft">#情感识别</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2608.09088</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-08-12</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2608.09088" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2608.09088" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出多尺度时间框架，用共享注意力编码器和动态融合模块处理EEG信号，在二分类和三分类情感识别中优于全信号基线。
</div>

## 👥 作者与机构

**Stefanos Gkikas** ¹ · Yang Guo · Guangliang Li · Raul Fernandez Rojas · Giorgos Giannakakis · Randy Gomez

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合EEG情感识别研究者阅读，重点关注动态融合模块和多尺度设计。可先看方法部分和表2，对比不同尺度配置的效果。

## 🌍 研究背景

EEG情感识别通常使用单一时间窗口，限制了模型对时间结构的利用。混合情绪（如喜忧参半）在临床上重要但研究不足。现有方法多采用固定窗口，无法捕捉不同时间尺度的特征。本文旨在通过多尺度时间分解和动态融合，提升EEG情感识别性能，特别是混合情绪分类。

## 💡 核心创新

1. 多尺度时间分解：将EEG信号分解为多种时长的窗口
2. 共享注意力编码器：处理不同尺度的窗口
3. 动态融合模块：为每个样本分配不同时间尺度的权重
4. 引入混合情绪类别：三分类任务包含混合情感
5. subject-independent评估：跨被试泛化

## 🏗️ 模型架构

输入为EEG波形，分解为多个时间尺度的窗口（如1秒、2秒、4秒），每个窗口通过共享的基于注意力的编码器提取特征，然后通过动态融合模块（可能基于注意力或门控机制）为每个样本学习各尺度权重，加权求和得到最终表示，用于分类。输出为情感类别概率。

## 📚 数据集

- 未明确指定数据集（摘要未提及）

## 📊 实验结果

摘要未提供具体数据集和基线数值，仅报告了最佳准确率：二分类65.22%，三分类45.43%，均高于全信号基线。动态融合在二分类中优于拼接，在三分类中略优，但计算量显著增加。

## 🎯 结论与影响

多尺度时间框架能有效提升EEG情感识别性能，特别是对混合情绪的分类。动态融合优于简单拼接，但计算开销大。未来可探索更高效的融合策略和更优的尺度选择。

## ⚠️ 局限与未解决问题

未提供数据集细节和与现有SOTA的对比，缺乏消融实验和统计显著性检验。计算开销大，未提及推理效率。混合情绪定义可能主观。

---

<div class="paper-footer"><span>评分：6.5</span><span>原始：6.5</span><a href="/audio-paper-daily/posts/2026-08-12/">← 返回 2026-08-12 速递</a></div>
