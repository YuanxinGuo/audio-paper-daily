---
title: "CODA: Cascaded Online Discontinuity-Aware Alignment for Real-Time Image-Based Score Following"
date: 2026-07-27T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#乐谱跟踪"]
summary: "提出CODA，首个利用级联结构（系统→小节→音符）实现实时乐谱跟踪的系统，并支持重复、跳转等不连续性恢复。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#乐谱跟踪</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#实时系统</span> <span class="tag-pill tag-pill-soft">#级联预测</span> <span class="tag-pill tag-pill-soft">#不连续性恢复</span> <span class="tag-pill tag-pill-soft">#图像到音频对齐</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2607.21899</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-07-27</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner"><div class="oc-headline"><span class="oc-pulse"></span><span class="oc-title">本论文已开源</span><span class="oc-hint">点击下方卡片直达对应资源</span></div><div class="oc-grid"><a class="oc-chip oc-chip-code" href="https://github.com/ValleyC/CODA" target="_blank" rel="noopener"><span class="oc-icon">💻</span><span class="oc-text"><span class="oc-label">代码仓库</span><span class="oc-sub">ValleyC/CODA</span></span></a></div></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2607.21899" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2607.21899" target="_blank" rel="noopener">📑 PDF</a><a class="rsrc rsrc-code" href="https://github.com/ValleyC/CODA" target="_blank" rel="noopener">💻 代码</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出CODA，首个利用级联结构（系统→小节→音符）实现实时乐谱跟踪的系统，并支持重复、跳转等不连续性恢复。
</div>

## 👥 作者与机构

**Yining Yang** ¹ · Ruogu Chen · Jie Han

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合音乐信息检索、实时音频对齐方向的研究者。建议重点阅读§3的级联对齐机制和§4的静音驱动中断模式。可先看表1的对比结果。

## 🌍 研究背景

实时乐谱跟踪（score following）旨在将流式音频与乐谱图像对齐，是音乐表演辅助、自动伴奏等应用的核心。现有图像方法通过多分辨率预测（同时预测系统、小节、音符位置）但各层级独立，导致预测不稳定且搜索空间大。此外，多数方法无法处理重复、D.C.、coda等乐谱不连续性。本文针对这两个问题提出CODA。

## 💡 核心创新

1. 级联预测架构：先选系统，再选小节，最后选音符，强制跨分辨率一致性
2. 静音驱动中断模式：利用静音检测触发不连续性恢复，无需先验重复结构知识
3. 首个同时解决实时跟踪与不连续性恢复的系统

## 🏗️ 模型架构

输入为流式音频特征和乐谱图像。主干采用卷积循环网络提取音频和图像特征。级联对齐模块：首先通过系统选择网络预测当前活跃系统，然后在小节选择网络内定位活跃小节，最后音符选择网络确定具体音符。每个子网络均使用注意力机制融合音频和图像特征。输出为实时对齐位置。参数量未提及。

## 📚 数据集

- Multimodal Sheet Music Dataset (MSMD) piano benchmarks（评估）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| 跟踪准确率 | MSMD piano | 多分辨率方法（未指名） | **SOTA** | 未提供具体数值 |
| 不连续性恢复性能 | MSMD piano | 现有方法（未指名） | **SOTA** | 未提供具体数值 |

在MSMD钢琴基准上，CODA在跟踪准确率和中断恢复性能上均达到SOTA，且满足实时吞吐量。摘要未提供具体数值，但声称优于现有方法。

## 🎯 结论与影响

CODA首次将级联预测用于实时乐谱跟踪，有效解决了多分辨率预测不一致和不连续性恢复两大难题。该工作为音乐表演中的实时对齐系统提供了新范式，有望推动自动伴奏、音乐教育等应用的发展。

## ⚠️ 局限与未解决问题

仅评估了钢琴数据集，未验证其他乐器或合奏场景；未报告推理延迟的具体数值；未与基于MIDI的方法对比；级联架构可能累积误差，但未进行误差传播分析。

## 🔗 开源资源

- **代码**：<https://github.com/ValleyC/CODA>

---

<div class="paper-footer"><span>评分：7.8</span><span>原始：7.8</span><a href="/audio-paper-daily/posts/2026-07-27/">← 返回 2026-07-27 速递</a></div>
