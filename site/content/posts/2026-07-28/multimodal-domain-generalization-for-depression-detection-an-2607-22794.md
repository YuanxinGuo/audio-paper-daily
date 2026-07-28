---
title: "Multimodal Domain Generalization for Depression Detection: An Attention-Based BiLSTM Network with Domain-Adversarial Training"
date: 2026-07-28T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#抑郁症检测"]
summary: "提出首个患者独立的多模态抑郁症检测框架，结合BiLSTM与注意力机制，通过域对抗训练提升跨说话人泛化能力，在Androids-Corpus上达到93.2%准确率。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#抑郁症检测</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#多模态融合</span> <span class="tag-pill tag-pill-soft">#领域泛化</span> <span class="tag-pill tag-pill-soft">#域对抗训练</span> <span class="tag-pill tag-pill-soft">#BiLSTM</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2607.22794</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-07-28</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2607.22794" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2607.22794" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出首个患者独立的多模态抑郁症检测框架，结合BiLSTM与注意力机制，通过域对抗训练提升跨说话人泛化能力，在Androids-Corpus上达到93.2%准确率。
</div>

## 👥 作者与机构

**Ali Tabaraei** ¹ · Federico Simonetta · Stavros Ntalampiras

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合从事语音情感计算、抑郁症检测的研究者阅读。建议重点看§3的模型架构（尤其是域对抗模块）和§4的实验设置与消融研究。可先读摘要和结论，再深入方法部分。

## 🌍 研究背景

抑郁症检测中，深度学习模型常因说话人间差异导致的域偏移而泛化能力差。现有方法多为患者依赖或单模态，缺乏跨说话人泛化的系统研究。本文首次提出患者独立的多模态域泛化框架，利用声学和文本模态，通过域对抗训练减少患者特定偏差，提升泛化性。

## 💡 核心创新

1. 首个患者独立的多模态抑郁症检测域泛化框架
2. BiLSTM结合帧内与跨模态注意力机制
3. 基于梯度反转层的域对抗训练增强泛化
4. 段级融合策略用于决策

## 🏗️ 模型架构

输入为音频Mel频谱和文本ItalianBERT嵌入。主干为双向LSTM，分别处理音频和文本序列。帧内注意力捕捉单模态内部依赖，跨模态注意力对齐声学与文本特征。段级融合将多帧特征聚合为段级表示，最后通过全连接层分类。域对抗分支通过梯度反转层（GRL）使特征提取器无法区分说话人身份，从而学习域不变表示。

## 📚 数据集

- Androids-Corpus（训练与评估，5折交叉验证）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| Accuracy | Androids-Corpus | 无DG基线（90.7%） | **93.2%** | +2.5% |
| F1-score | Androids-Corpus | 无DG基线（90.9%） | **94.2%** | +3.3% |

在Androids-Corpus上，所提方法以MelSpec和ItalianBERT为最优特征组合，30秒段长下达到93.2%准确率和94.2%F1，超越所有现有基准。消融实验验证了多模态融合、深度架构选择和域对抗训练各自对性能的贡献，其中域对抗训练带来2.5%准确率和3.3%F1提升。

## 🎯 结论与影响

本文证明域对抗训练能有效提升抑郁症检测的跨说话人泛化能力，多模态融合进一步增强了鲁棒性。该框架为患者独立的抑郁症检测提供了新范式，有望推动临床实际应用。后续可探索更复杂的域泛化策略及更大规模数据集验证。

## ⚠️ 局限与未解决问题

仅在单一数据集（Androids-Corpus）上验证，缺乏跨数据集泛化实验。未报告模型参数量或推理延迟，实用性评估不足。域对抗训练可能引入训练不稳定，未详细讨论。对比基线未包含最新多模态抑郁症检测方法。

---

<div class="paper-footer"><span>评分：7.8</span><span>原始：7.8</span><a href="/audio-paper-daily/posts/2026-07-28/">← 返回 2026-07-28 速递</a></div>
