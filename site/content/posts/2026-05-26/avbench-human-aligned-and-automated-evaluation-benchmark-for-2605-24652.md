---
title: "AVBench: Human-Aligned and Automated Evaluation Benchmark for Audio-Video Generative Models"
date: 2026-05-26T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#音视频生成评估"]
summary: "提出AVBench，一个面向人类中心音视频生成的自动化评估基准，包含细粒度指标和通过偏好学习训练的专业评估器。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#音视频生成评估</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#音视频生成</span> <span class="tag-pill tag-pill-soft">#评估基准</span> <span class="tag-pill tag-pill-soft">#偏好学习</span> <span class="tag-pill tag-pill-soft">#人类对齐</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2605.24652</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-05-26</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2605.24652" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2605.24652" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出AVBench，一个面向人类中心音视频生成的自动化评估基准，包含细粒度指标和通过偏好学习训练的专业评估器。
</div>

## 👥 作者与机构

**Jialiang Yang** ¹ · Bin Xia · Ruihang Chu · Dingdong Wang · Wanke Xia · Zhun Mou · Tianyang Zhong · Yiting Zhao · … 等 1 人

**机构**：清华大学

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合音视频生成、评估方法研究者阅读。建议重点看第3节（评估维度设计）和第4节（偏好学习训练策略），以及表2（与人类判断的对齐结果）。

## 🌍 研究背景

音视频生成领域快速发展，但评估方法滞后。现有基准粗粒度、依赖通用多模态大模型，缺乏针对人类相关场景（如语音、交互）的细粒度评估，且评估结果不准确。本文旨在构建一个自动化、人类对齐的评估基准，解决评估维度不全面和评估器训练数据缺乏的问题。

## 💡 核心创新

1. 提出10个面向人类中心的细粒度评估维度
2. 通过真实视频加扰动构建大规模偏好训练数据
3. 基于二元决策置信度输出连续评分，替代VQA式离散判断
4. 评估器可作为RLHF的奖励信号
5. 全自动化评估流程，无需人工标注

## 🏗️ 模型架构

AVBench包含两个核心组件：1）评估维度体系：10个维度覆盖视觉质量、音频质量、跨模态一致性（如唇同步、语义对齐）。2）专业评估器：基于预训练多模态模型（如CLIP、AV-HuBERT），通过偏好学习微调。训练数据由真实视频经可控扰动（如时间偏移、音频替换）生成正负样本对。评估时，模型对二元决策（是否一致）输出置信度，映射为连续评分。

## 📚 数据集

- VoxCeleb2（用于训练评估器的唇同步维度）
- AVE（用于训练评估器的音视频语义对齐维度）
- 自建扰动数据集（从上述视频生成正负样本对，用于偏好学习）
- Human Evaluation Set（人工标注的测试集，用于验证对齐性）

## 📊 实验结果

摘要未提供具体数值结果，但声称AVBench的评估与人类判断高度对齐，且能有效区分不同生成模型的质量。评估器在检测跨模态不一致（如音画不同步）方面优于现有VQA方法。

## 🎯 结论与影响

AVBench提供了首个面向人类中心音视频生成的自动化、细粒度评估基准，其基于偏好学习的评估器能输出与人类对齐的连续评分。该工作有望推动音视频生成评估标准化，并可作为RLHF的奖励信号用于模型优化，对工业界模型筛选和训练有实际价值。

## ⚠️ 局限与未解决问题

未报告评估器在不同生成模型上的具体对比分数；训练数据仅基于有限扰动类型，可能无法覆盖所有真实失真；评估维度虽细但可能仍不全面（如未考虑音频空间感）；未讨论计算开销。

---

<div class="paper-footer"><span>评分：7.8</span><span>原始：7.8</span><a href="/audio-paper-daily/posts/2026-05-26/">← 返回 2026-05-26 速递</a></div>
