---
title: "Beyond Content: A Comprehensive Speech Toxicity Dataset and Detection Framework Incorporating Paralinguistic Cues"
date: 2026-05-18T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#有害语音检测"]
summary: "提出大规模有害语音数据集ToxiAlert-Bench及双头神经网络框架，利用副语言线索提升检测性能。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#有害语音检测</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#副语言线索</span> <span class="tag-pill tag-pill-soft">#多模态</span> <span class="tag-pill tag-pill-soft">#数据集构建</span> <span class="tag-pill tag-pill-soft">#分类</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2605.15984</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-05-18</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2605.15984" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2605.15984" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出大规模有害语音数据集ToxiAlert-Bench及双头神经网络框架，利用副语言线索提升检测性能。
</div>

## 👥 作者与机构

**Zhongjie Ba** ¹ · Liang Yi · Peng Cheng · Qingcao Li · Qinglong Wang · Li Lu

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合从事有害内容检测、语音情感分析的研究者。建议通读，重点看§3数据集标注方案和§4双头网络架构及多阶段训练策略。

## 🌍 研究背景

现有有害语音检测主要基于文本，忽略了副语言线索（如情绪、语调、语速）对毒性判断的作用。同时缺乏大规模、细粒度标注的有害语音数据集。本文旨在构建包含30k+音频片段、标注7大毒性类别和20细粒度标签的数据集，并设计能同时利用文本和副语言线索的检测框架。

## 💡 核心创新

1. 构建ToxiAlert-Bench数据集，标注毒性来源（文本/副语言）
2. 提出双头神经网络，分别识别毒性来源和具体类型
3. 多阶段训练策略：独立头训练+联合微调减少任务干扰
4. 类别平衡采样和加权损失函数缓解数据不平衡

## 🏗️ 模型架构

输入音频特征（如MFCC、韵律特征）→ 共享编码器（如CNN+Transformer）→ 双任务分类头：头1预测毒性来源（文本/副语言），头2预测细粒度毒性类别。训练分两阶段：先独立训练各头，再联合微调整个网络。

## 📚 数据集

- ToxiAlert-Bench（30k+音频片段，训练/评估，7大毒性类别+20细粒度标签）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| Macro-F1 | ToxiAlert-Bench | 最强基线（未指名） | **相对提升21.1%** | +21.1% |
| Accuracy | ToxiAlert-Bench | 最强基线（未指名） | **相对提升13.0%** | +13.0% |

实验表明，利用副语言特征显著提升检测性能，所提方法在Macro-F1和准确率上分别相对最强基线提升21.1%和13.0%。消融实验验证了双头结构和多阶段训练的有效性。

## 🎯 结论与影响

本文证实副语言线索对有害语音检测至关重要，ToxiAlert-Bench数据集和双头框架为后续研究提供了基准。该工作有望推动在线平台部署更鲁棒的有害语音检测系统。

## ⚠️ 局限与未解决问题

未报告推理延迟和模型参数量；数据集仅涵盖英语，跨语言泛化未知；未与基于文本的SOTA方法对比；未分析副语言特征的具体贡献（如哪种线索最有效）。

---

<div class="paper-footer"><span>评分：7.8</span><span>原始：7.8</span><a href="/audio-paper-daily/posts/2026-05-18/">← 返回 2026-05-18 速递</a></div>
