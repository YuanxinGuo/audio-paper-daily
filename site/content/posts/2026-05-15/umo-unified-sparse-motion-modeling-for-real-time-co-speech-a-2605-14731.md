---
title: "UMo: Unified Sparse Motion Modeling for Real-Time Co-Speech Avatars"
date: 2026-05-15T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#语音驱动动画生成"]
summary: "提出统一稀疏运动建模架构UMo，实现实时、高保真的语音驱动手势与面部动画生成。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#语音驱动动画生成</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#语音驱动手势</span> <span class="tag-pill tag-pill-soft">#语音驱动面部动画</span> <span class="tag-pill tag-pill-soft">#稀疏建模</span> <span class="tag-pill tag-pill-soft">#实时</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2605.14731</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-05-15</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2605.14731" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2605.14731" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出统一稀疏运动建模架构UMo，实现实时、高保真的语音驱动手势与面部动画生成。
</div>

## 👥 作者与机构

**Xiaoyu Zhan** ¹ · Xinyu Fu · Chenghao Yang · Xiaohong Zhang · Dongjie Fu · Pengcheng Fang · Tengjiao Sun · Xiaohao Cai · … 等 4 人

**机构**：南京大学 · 香港大学 · 北京航空航天大学

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合从事数字人、语音驱动动画、多模态生成的研究者。建议重点阅读§3架构设计与§4多阶段训练策略，以及表2的延迟对比。

## 🌍 研究背景

语音驱动手势与面部动画是数字人表达的关键。现有方法要么局限于单模态（仅音频-运动对齐），未能充分利用大规模人体运动数据；要么受限于多模态模型的表示能力和吞吐量，难以同时实现高质量运动生成与实时性能。本文旨在解决高保真实时协同语音动画的难题。

## 💡 核心创新

1. 统一文本/音频/运动token的稀疏建模架构
2. 空间稀疏MoE框架提升模型容量与效率
3. 时间稀疏关键帧设计实现实时密集重建
4. 多阶段训练策略结合音频增强提升语义一致性

## 🏗️ 模型架构

输入：文本、音频、运动token。主干：统一稀疏运动建模架构，包含空间稀疏MoE（Mixture-of-Experts）框架和时间稀疏关键帧设计。关键模块：MoE层处理多模态token，关键帧预测器输出稀疏关键帧，再通过密集重建模块生成连续动画。输出：面部表情与手势的3D运动序列。

## 📚 数据集

- BEAT（训练/评估，包含语音、文本、手势和面部动画）
- TED Gesture（训练/评估，语音驱动手势数据集）
- VOCA（训练/评估，语音驱动面部动画数据集）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| FGD (Fréchet Gesture Distance) | BEAT | TalkSHOW 12.5 | **8.3** | -4.2 |
| L1 (面部顶点误差) | VOCA | FaceFormer 0.82 | **0.71** | -0.11 |
| 延迟 (ms) | BEAT | TalkSHOW 120 | **30** | -90 ms |

UMo在BEAT数据集上FGD为8.3，优于TalkSHOW的12.5；在VOCA上L1误差0.71，优于FaceFormer的0.82。延迟仅30ms，达到实时要求。消融实验验证了稀疏MoE和关键帧设计的有效性。

## 🎯 结论与影响

UMo通过统一稀疏建模实现了实时高保真语音驱动动画，在质量和延迟上均优于现有方法。该工作为数字人实时交互提供了实用方案，有望推动游戏、虚拟制作等领域的应用。

## ⚠️ 局限与未解决问题

未报告推理时的参数量和计算成本；仅评估了英文语音，多语言泛化性未知；手势多样性指标（如多样性得分）未提供；未与最新的大模型方法（如基于扩散的方法）对比。

---

<div class="paper-footer"><span>评分：8.2</span><span>原始：8.2</span><a href="/audio-paper-daily/posts/2026-05-15/">← 返回 2026-05-15 速递</a></div>
