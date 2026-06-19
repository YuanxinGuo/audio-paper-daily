---
title: "Segment-Level Mandarin Chinese Speech-Based Cognitive Impairment Detection via an Autoencoder with Contrastive Learning"
date: 2026-06-19T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#认知障碍检测"]
summary: "提出基于自编码器和对比学习的段级语音表征学习框架，用于普通话认知障碍检测，在四个数据集上表现稳定。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero">
<div class="hero-score">
<div class="score-num">7.2</div>
<div class="score-stars">★★★★☆</div>
<div class="score-tier">前25%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#认知障碍检测</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#语音生物标志物</span> <span class="tag-pill tag-pill-soft">#自编码器</span> <span class="tag-pill tag-pill-soft">#对比学习</span> <span class="tag-pill tag-pill-soft">#数据增强</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2606.19996</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-06-19</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2606.19996" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2606.19996" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出基于自编码器和对比学习的段级语音表征学习框架，用于普通话认知障碍检测，在四个数据集上表现稳定。
</div>

## 👥 作者与机构

**Yongqi Shao** ¹ · Hong Huo · Flavio Bertini · Danilo Montesi · Tao Fang

**机构**：上海交通大学 · 费拉拉大学 · 博洛尼亚大学

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合从事语音生物标志物和认知障碍检测的研究者阅读。建议重点看§2方法部分的数据增强和对比学习设计，以及§3的消融实验。可先读摘要和结论，再深入方法细节。

## 🌍 研究背景

语音作为低成本、非侵入性的数字生物标志物，在认知障碍检测中具有潜力。然而，标注数据有限和跨数据集差异是主要挑战。现有方法多基于全局语音特征，忽略了局部时间信息，且在小样本场景下泛化能力不足。本文旨在通过段级表征学习结合自编码器和对比学习，提升在有限数据下的鲁棒性和分类性能。

## 💡 核心创新

1. 段级语音分割与频谱图表示
2. 离线+在线数据增强策略
3. 自编码器与对比学习联合训练
4. 在四分类任务中显著提升三分类性能

## 🏗️ 模型架构

输入：语音录音分割为短段，转换为频谱图。主干：自编码器（编码器-解码器结构）提取潜在表征。关键模块：对比学习目标（如NT-Xent损失）增强判别性；离线增强（加噪、变速）和在线增强（SpecAugment）结合。输出：段级表征经聚合后用于二分类/三分类（认知正常、轻度认知障碍、痴呆）。

## 📚 数据集

- 数据集1（训练/评估，四个独立普通话语音数据集，具体名称未给出）

## 📊 实验结果

摘要未提供具体数值指标，但声称在四个独立数据集上二分类和三分类任务表现稳定，三分类提升显著。消融实验验证了框架各模块的有效性。

## 🎯 结论与影响

本文提出的段级语音表征学习框架为认知障碍筛查提供了可扩展且实用的方法，尤其在资源受限的临床环境中。该工作表明结合自编码器和对比学习能有效利用有限标注数据，未来可推动语音生物标志物在认知障碍早期诊断中的应用。

## ⚠️ 局限与未解决问题

摘要未报告具体指标和基线对比，无法评估改进幅度；未提及推理延迟和模型复杂度；数据集名称和规模未给出，可重复性受限；仅针对普通话，跨语言泛化性未知。

---

<div class="paper-footer"><span>评分：7.2</span><span>原始：7.2</span><a href="/audio-paper-daily/posts/2026-06-19/">← 返回 2026-06-19 速递</a></div>
