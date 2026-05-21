---
title: "CoarseSoundNet: Building a reliable model for ecological soundscape analysis"
date: 2026-05-21T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#声景分类"]
summary: "提出CoarseSoundNet，在被动声学监测条件下对生物声、地质声和人为声进行粗粒度分类，并系统研究训练策略与后处理方法。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#声景分类</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#生态声学</span> <span class="tag-pill tag-pill-soft">#被动声学监测</span> <span class="tag-pill tag-pill-soft">#深度学习</span> <span class="tag-pill tag-pill-soft">#声景分析</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2605.21143</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-05-21</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2605.21143" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2605.21143" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出CoarseSoundNet，在被动声学监测条件下对生物声、地质声和人为声进行粗粒度分类，并系统研究训练策略与后处理方法。
</div>

## 👥 作者与机构

**Alexander Gebhard** ¹ · Andreas Triantafyllopoulos · Dominik Arend · Sandra M\"uller · Svenja Schmidt · Michael Scherer-Lorenzen · Bj\"orn W. Schuller

**机构**：慕尼黑大学 · 奥格斯堡大学

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合生态声学、被动声学监测领域的研究者。建议重点阅读第3节（模型架构与训练策略）和第4节（实验与消融），尤其是表2和表3。可跳过第5节案例研究。

## 🌍 研究背景

声景生态学中，量化生物声、地质声和人为声的相互作用是核心问题，但现有机器学习方法多依赖任务特定或干净数据，难以泛化到噪声丰富的被动声学监测（PAM）录音。此前缺乏系统性的粗粒度声景分类模型构建指南。本文旨在建立可复现的框架，并开发CoarseSoundNet以在真实PAM条件下区分三类声源。

## 💡 核心创新

1. 引入显式静音类提升分类鲁棒性
2. 类特定决策阈值与时长约束后处理
3. 系统研究训练数据组成对泛化的影响
4. 在生态案例中验证作为预处理工具的有效性

## 🏗️ 模型架构

输入为对数梅尔谱图，主干网络采用CNN（具体为ResNet-18变体），输出三类（biophony, geophony, anthropophony）加一个可选的silence类。后处理使用类特定阈值和时长约束。模型参数量未明确给出。

## 📚 数据集

- 自建PAM数据集（训练/评估，包含真实野外录音）
- 公开声景数据集（用于对比实验，未具体命名）

## 📊 实验结果

摘要未提供具体数值指标，但指出引入静音类、增加目标域相似PAM数据可提升性能；类特定阈值和时长约束对anthropophony和geophony改善明显。误差分析显示anthropophony受掩蔽效应影响，silence与昆虫声易混淆。

## 🎯 结论与影响

CoarseSoundNet在真实PAM条件下实现了稳健的粗粒度声景分类，可作为生态声学分析的有效预处理工具。其系统性的训练策略和后处理方法为后续研究提供了可复现的基准。对工业落地，可集成到自动监测系统中辅助声景指数计算。

## ⚠️ 局限与未解决问题

未报告具体分类准确率或F1分数，缺乏与现有方法的定量对比；仅使用CNN架构，未探索Transformer或Mamba等更先进模型；数据集规模与构成未详细说明，可能限制泛化性；未提供推理速度或模型大小等效率指标。

---

<div class="paper-footer"><span>评分：7.2</span><span>原始：7.2</span><a href="/audio-paper-daily/posts/2026-05-21/">← 返回 2026-05-21 速递</a></div>
