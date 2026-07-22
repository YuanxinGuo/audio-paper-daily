---
title: "End-to-End Markov State Sequence Learning for Auditory Attention Decoding"
date: 2026-07-22T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#听觉注意力解码"]
summary: "提出端到端马尔可夫状态序列学习框架，将听觉注意力解码建模为两状态序列，用CRF联合优化窗口级发射和状态转移，在动态AVGC数据集上达到86.5%因果准确率。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#听觉注意力解码</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#EEG</span> <span class="tag-pill tag-pill-soft">#条件随机场</span> <span class="tag-pill tag-pill-soft">#端到端学习</span> <span class="tag-pill tag-pill-soft">#语音-脑电相关性</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2607.18614</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-07-22</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2607.18614" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2607.18614" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出端到端马尔可夫状态序列学习框架，将听觉注意力解码建模为两状态序列，用CRF联合优化窗口级发射和状态转移，在动态AVGC数据集上达到86.5%因果准确率。
</div>

## 👥 作者与机构

**Yushan Yashengjiang** ¹ · Jie Zhang · Miao Sun · Huadong Liang · Xin Li · Zhen-hua Ling

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合从事听觉注意力解码、脑机接口或神经引导助听器的研究者阅读。建议重点读§3框架设计和§4实验部分，尤其是表1-3的对比结果。可先看§3.2的CRF训练目标与§4.2的ESCNet骨干。

## 🌍 研究背景

听觉注意力解码（AAD）旨在从EEG信号中识别听者关注的说话人，是神经引导助听器的关键算法。现有方法大多将AAD视为独立短窗分类器，忽略了注意力作为时间持续认知状态的特性，且短窗EEG-语音证据常含噪声和歧义。本文提出端到端马尔可夫AAD框架，利用条件随机场（CRF）建模两状态注意力先验，使时间连续性引导表示学习，而非仅在训练后平滑预测。

## 💡 核心创新

1. 提出端到端CRF框架联合优化窗口级发射与状态转移
2. 将任意AAD骨干的logits视为马尔可夫发射，从标准HMM初始化转移率
3. 设计ESCNet骨干，保留时间对齐特征并转换Pearson相关差为状态logits
4. 在动态AVGC数据集上实现86.5%因果和92.4%非因果准确率（1秒窗）

## 🏗️ 模型架构

输入为EEG和语音特征（如mel谱）。ESCNet骨干：EEG和语音分别通过时间卷积保持对齐，计算两路平均Pearson相关，取差值作为状态logits。框架将任意AAD骨干（如ESCNet、卷积、循环、注意力网络）的logits视为马尔可夫发射，通过标准HMM初始化转移率，联合优化交叉熵和CRF目标，输出两状态（关注说话人A或B）的序列预测。

## 📚 数据集

- AVGC（动态，训练/评估，含多说话人切换）
- KUL（静态，评估）
- USTC（静态，评估）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| 因果准确率 | AVGC | ESCNet无CRF（基线值未明确给出，但CRF优于后处理HMM） | **86.5%** | 优于后处理HMM平滑 |
| 非因果准确率 | AVGC | ESCNet无CRF | **92.4%** | 优于后处理HMM平滑 |
| 因果准确率提升 | KUL | 固定率后处理HMM基线 | **提升5.6%** | +5.6% |
| 因果准确率提升 | USTC | 固定率后处理HMM基线 | **提升2.0%** | +2.0% |

在动态AVGC数据集上，CRF训练普遍优于后处理HMM平滑；ESCNet骨干结合CRF达到86.5%因果和92.4%非因果准确率（1秒窗）。在静态KUL和USTC数据集上，因果解码准确率分别比固定率后处理HMM基线提升5.6%和2.0%，验证了端到端序列学习的优势。

## 🎯 结论与影响

本文证明将AAD建模为注意力状态序列并端到端学习优于独立窗分类。CRF框架可即插即用于多种骨干，为神经引导助听器提供了更鲁棒的实时解码方案。未来可探索更复杂的注意力状态模型或结合多模态线索。

## ⚠️ 局限与未解决问题

仅在三个数据集上评估，且AVGC为动态但KUL/USTC为静态，泛化性需更多验证。未报告推理延迟或参数量，对实时助听器部署的可行性分析不足。CRF框架对长序列的依赖可能增加计算开销。

---

<div class="paper-footer"><span>评分：8.2</span><span>原始：8.2</span><a href="/audio-paper-daily/posts/2026-07-22/">← 返回 2026-07-22 速递</a></div>
