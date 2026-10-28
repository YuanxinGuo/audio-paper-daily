---
title: "EEG-Based Decoding of Musical Mode and Melodic Direction Using Empirical Mode Decomposition"
date: 2026-10-28T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#脑电信号解码"]
summary: "用EMD分解钢琴演奏时EEG信号，取前四个IMF的能量特征训练宽神经网络，解码调式与旋律走向。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero">
<div class="hero-score">
<div class="score-num">5.8</div>
<div class="score-stars">★★★☆☆</div>
<div class="score-tier">中等</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#脑电信号解码</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#EEG解码</span> <span class="tag-pill tag-pill-soft">#音乐信息检索</span> <span class="tag-pill tag-pill-soft">#经验模态分解</span> <span class="tag-pill tag-pill-soft">#脑机接口</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2610.37148</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-10-28</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2610.37148" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2610.37148" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>用EMD分解钢琴演奏时EEG信号，取前四个IMF的能量特征训练宽神经网络，解码调式与旋律走向。
</div>

## 👥 作者与机构

Sergio Guill\'en · Lorenzo J. Tard\'on · Ana M. Barbancho · Isabel Barbancho

**机构**：马拉加大学

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合做EEG音乐认知解码、MIR神经机制的研究者。若关注语音/音频信号处理本身，本文参考价值有限。建议重点看§方法中的EMD-IMF能量特征构造与跨被试实验设置，表对比标准分类器结果即可，无需通读频域分析细节。

## 🌍 研究背景

音乐诱发的EEG解码是MIR与情感神经科学交叉方向，此前多用频带功率（如theta/alpha/beta）或事件相关电位作为特征，配合SVM、LDA、CNN等分类器。痛点在于EEG非平稳、信噪比低，固定频带划分难以适配个体差异，跨被试泛化差。本文试图用数据驱动的经验模态分解替代固定频带，提取自适应IMF能量特征来检测音乐调式与旋律走向。

## 💡 核心创新

1. 用EMD将EEG自适应分解为IMF，替代固定频带特征
2. 取前四个IMF的能量描述子作为分类特征
3. 采用Wide Neural Network分类器并与多种标准分类器对比
4. 验证方法对左右利手的鲁棒性

## 🏗️ 模型架构

输入为钢琴主动演奏时采集的多通道EEG时序信号；先做预处理，再用经验模态分解（EMD）逐通道分解为若干本征模态函数（IMF），取前四个IMF计算能量型描述子构成特征向量；随后送入Wide Neural Network（宽神经网络，单隐层宽结构）进行二分类，分别判定音乐调式与旋律走向。同时与SVM、LDA、随机森林等标准EEG分类器做基准对比，并做IMF与常规EEG子频带的频域对应分析。摘要未给出参数量。

## 📚 数据集

- 自采集钢琴演奏EEG数据集（训练与评估，被试内与被试间两种设置）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| Accuracy | 自采集EEG（被试内） | 标准分类器基准（摘要未给具体值） | **84%** | 摘要未给具体差值 |
| Accuracy | 自采集EEG（被试间，首个IMF） | 标准分类器基准（摘要未给具体值） | **81%** | 摘要未给具体差值 |
| AUC-ROC | 自采集EEG（两种设置） | 摘要未给 | **0.9** | 摘要未给具体差值 |

被试内平均准确率84%，被试间用首个IMF达81%，两种设置AUC-ROC均约0.9。频域分析显示IMF与常规EEG子频带高度对应，但部分频率成分未被完整表征。激活主要分布于额区、颞区与顶枕区，与音乐加工脑区一致。方法对左右利手均稳健。摘要未给出与各基线分类器的逐项数值对比及消融结果。

## 🎯 结论与影响

最强结论是EMD-IMF能量特征可在被试内与被试间稳定解码音乐调式与旋律走向，且不受利手影响。这为MIR与情感神经科学提供了一种自适应特征提取思路，可能推动基于EEG的音乐结构神经编码研究；工业落地层面更偏向脑机接口与音乐推荐中的生理反馈建模，短期实用价值有限。

## ⚠️ 局限与未解决问题

摘要未给出与各标准分类器的具体数值对比，难以判断增益幅度；数据集为自采集、被试规模未说明，存在小样本偏差；仅做二分类任务，未报推理延迟与跨数据集泛化；EMD存在模态混叠与端点效应，摘要未讨论其稳定性。

---

<div class="paper-footer"><span>评分：5.8</span><span>原始：5.8</span><a href="/audio-paper-daily/posts/2026-10-28/">← 返回 2026-10-28 速递</a></div>
