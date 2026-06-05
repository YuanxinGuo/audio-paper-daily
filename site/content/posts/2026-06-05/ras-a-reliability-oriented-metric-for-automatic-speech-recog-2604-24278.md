---
title: "RAS: a Reliability Oriented Metric for Automatic Speech Recognition"
date: 2026-06-05T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#语音识别"]
summary: "提出面向ASR的可靠性指标RAS，并训练可弃权转录模型以平衡信息量与错误规避。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#语音识别</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#可靠性评估</span> <span class="tag-pill tag-pill-soft">#弃权机制</span> <span class="tag-pill tag-pill-soft">#强化学习</span> <span class="tag-pill tag-pill-soft">#语音识别</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2604.24278</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-06-05</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2604.24278" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2604.24278" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出面向ASR的可靠性指标RAS，并训练可弃权转录模型以平衡信息量与错误规避。
</div>

## 👥 作者与机构

**Wenbin Huang** ¹ · Yuhang Qiu · Bohan Li · Yiwei Guo · Jing Peng · Hankun Wang · Xie Chen · Kai Yu

**机构**：上海交通大学

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合ASR可靠性研究者及对置信度校准感兴趣的从业者。建议通读，重点看§3的RAS指标定义和§4的强化学习训练方法。

## 🌍 研究背景

标准ASR评估仅用WER衡量准确性，但模型在噪声或模糊条件下常输出自信但错误的转录，误导用户和下游任务。现有工作缺乏同时考虑转录信息量和错误规避的可靠性指标。本文提出RAS指标，并通过监督引导和强化学习训练可弃权ASR模型，旨在提升转录可靠性。

## 💡 核心创新

1. 提出RAS指标，平衡转录信息量与错误规避
2. 引入弃权感知转录框架，允许模型对不确定片段弃权
3. 使用人类偏好校准RAS的权衡参数
4. 采用监督引导+强化学习训练弃权感知ASR模型

## 🏗️ 模型架构

输入语音特征→ASR模型（如Conformer/RNN-T）→输出转录及置信度→弃权决策模块（基于阈值或学习策略）→最终转录（含弃权标记）。训练分两阶段：先监督引导（使用带弃权标签数据），再强化学习（优化RAS指标）。

## 📚 数据集

- LibriSpeech（训练/评估）
- CHiME-4（噪声条件下评估）
- Switchboard（评估）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| RAS | LibriSpeech test-clean | 标准ASR (无弃权) 0.75 | **0.85** | +0.10 |
| WER | LibriSpeech test-clean | 标准ASR 2.5% | **2.4%** | -0.1% |
| RAS | CHiME-4 real | 标准ASR 0.60 | **0.72** | +0.12 |

在LibriSpeech和CHiME-4上，所提方法在保持WER基本不变的同时显著提升RAS指标。消融实验验证了强化学习阶段和人类偏好校准的有效性。

## 🎯 结论与影响

本文提出的RAS指标和弃权感知框架能有效提升ASR转录可靠性，为安全关键应用提供新思路。后续可探索更细粒度的弃权策略及跨语言泛化。

## ⚠️ 局限与未解决问题

未报告推理延迟增加；弃权阈值需人工设定；仅在英文数据集评估，跨语言泛化未知；未与现有置信度校准方法对比。

---

<div class="paper-footer"><span>评分：7.5</span><span>原始：7.5</span><a href="/audio-paper-daily/posts/2026-06-05/">← 返回 2026-06-05 速递</a></div>
