---
title: "Exploration of Perceptual Speech Features for Clinical Decision-Support in Mental Health Care"
date: 2026-05-26T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#语音特征分析"]
summary: "提出基于感知语音特征的分析框架，结合声学与语言特征，用可解释机器学习分析抑郁、焦虑、ADHD与语音关联。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero">
<div class="hero-score">
<div class="score-num">6.8</div>
<div class="score-stars">★★★☆☆</div>
<div class="score-tier">前50%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#语音特征分析</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#心理健康</span> <span class="tag-pill tag-pill-soft">#可解释机器学习</span> <span class="tag-pill tag-pill-soft">#声学特征</span> <span class="tag-pill tag-pill-soft">#临床决策支持</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2605.24678</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-05-26</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2605.24678" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2605.24678" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出基于感知语音特征的分析框架，结合声学与语言特征，用可解释机器学习分析抑郁、焦虑、ADHD与语音关联。
</div>

## 👥 作者与机构

**Vassilis Lyberatos** ¹ · Edmund G. Dervakos · Eleni Adamidi · Athanasios Voulodimos · Giorgos Stamou

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合心理健康与语音分析交叉领域研究者。重点看§3特征工程与§4实验结果，特别是表2的消融研究。可跳过§2相关工作。

## 🌍 研究背景

语音技术为心理健康评估提供客观线索，但现有方法多依赖黑盒深度学习，缺乏临床可解释性。此前工作多聚焦单一特征或数据集，未系统比较多种感知特征。本文旨在构建透明、可解释的框架，关联语音特征与抑郁、焦虑、ADHD症状。

## 💡 核心创新

1. 融合声学（jitter/shimmer）与语言（语义连贯性、讽刺）特征
2. 使用XGBoost+SHAP/LIME实现可解释性
3. 在5个数据集（含真实临床数据）上验证
4. 跨数据集消融研究识别最有效特征组

## 🏗️ 模型架构

输入为语音转录文本与声学特征（基频、能量、jitter、shimmer等）。语言特征通过NLP提取（语义连贯性、句法复杂度、讽刺检测）。所有特征拼接后输入XGBoost分类器，输出症状严重程度预测。可解释性通过SHAP和LIME实现。

## 📚 数据集

- StressID（训练/评估，受控环境）
- DAIC-WOZ（训练/评估，临床访谈）
- Androids（训练/评估，模拟对话）
- EATD（训练/评估，真实临床数据）

## 📊 实验结果

摘要未提供具体数值指标，但指出框架在多个数据集上揭示了症状严重度与声学不规则性（如shimmer、jitter）、词汇句法模式及情感语调之间的稳定一致关系。消融研究识别出最有效的特征组。

## 🎯 结论与影响

本文证明基于感知语音特征的可解释框架能有效关联心理健康症状，为临床决策支持提供透明工具。后续可扩展至更多症状维度，并探索实时监测应用。对工业落地而言，低计算开销的XGBoost模型便于部署。

## ⚠️ 局限与未解决问题

未报告具体分类性能指标（如F1/AUC），难以量化改进。数据集规模可能有限，且真实临床数据标注可靠性未知。未与深度学习基线对比。特征工程依赖手工设计，可能遗漏深层模式。

---

<div class="paper-footer"><span>评分：6.8</span><span>原始：6.8</span><a href="/audio-paper-daily/posts/2026-05-26/">← 返回 2026-05-26 速递</a></div>
