---
title: "EEG-Based Prediction of Music Enjoyment Using Deep Learning with Explainable Temporal Analysis"
date: 2026-10-16T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#脑电信号分析"]
summary: "用六种深度学习模型在MUSIN-G脑电数据集上做音乐愉悦度回归，并用梯度与遮挡方法做时间维度可解释性分析。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero">
<div class="hero-score">
<div class="score-num">4.5</div>
<div class="score-stars">★★☆☆☆</div>
<div class="score-tier">后50%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#脑电信号分析</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#EEG</span> <span class="tag-pill tag-pill-soft">#音乐情感</span> <span class="tag-pill tag-pill-soft">#可解释性</span> <span class="tag-pill tag-pill-soft">#回归预测</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2610.20795</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-10-16</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2610.20795" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2610.20795" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>用六种深度学习模型在MUSIN-G脑电数据集上做音乐愉悦度回归，并用梯度与遮挡方法做时间维度可解释性分析。
</div>

## 👥 作者与机构

**Parshav Singla** ¹ · Simranjit Kaur · Maanya Walia · Niharika

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合做EEG情感解码或音乐神经科学的研究者快速浏览。建议重点看§3的participant-wise协议与表2的六模型对比，以及可解释性部分的时间段定位图。若关注音乐愉悦度建模可通读，若只关心音频分离/增强则可跳过。

## 🌍 研究背景

音乐愉悦度是主观且随时间变化的体验，传统研究多把音乐情感当作离散类别标签，或用黑盒模型预测，缺乏对神经时间动态的解释。MUSIN-G等公开EEG数据集提供了128通道听歌脑电与歌曲级愉悦评分，但跨被试泛化与可解释性仍是痛点。本文把愉悦度预测建模为回归任务，在跨被试协议下比较多种深度模型，并引入时间可解释性分析。

## 💡 核心创新

1. 将音乐愉悦度建模为1-5连续回归而非分类
2. 采用participant-wise跨被试评估协议
3. 用梯度与遮挡法定位2秒窗内关键时间段
4. 对比DeepConvNet/CNN-LSTM/GNN-CNN/TCN六种模型

## 🏗️ 模型架构

输入为128通道EEG信号，按2秒窗口切分。比较六种深度模型：DeepConvNet（多层时域卷积）、CNN-LSTM（卷积提特征后接LSTM建模时序）、GNN-CNN（图神经网络建模电极空间关系后接CNN）、TCN（时序卷积网络，膨胀因果卷积堆叠）等。输出为1-5愉悦度回归值。可解释性方面，对TCN使用梯度法与遮挡法，在留出窗口上平均，得到每个2秒窗内影响预测的时间段。摘要未给出参数量。

## 📚 数据集

- MUSIN-G（训练+验证，15名被试，128通道EEG）
- MUSIN-G（测试，5名被试留出）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| MAE（1-5量表） | MUSIN-G | 未给出具体基线值 | **0.97-0.99（DeepConvNet/CNN-LSTM/GNN-CNN）** | — |
| Pearson r | MUSIN-G | 未给出具体基线值 | **0.21（TCN最高）** | — |

摘要报告DeepConvNet、CNN-LSTM与GNN-CNN取得最低MAE（0.97-0.99），TCN取得最高Pearson相关（r=0.21）。相关性偏低说明跨被试愉悦度预测仍困难。可解释性分析在留出窗口上平均，定位了每个2秒窗内对TCN预测影响最大的时间段。摘要未给出消融实验、效率指标或与已有方法的数值对比。

## 🎯 结论与影响

本文提供了EEG音乐愉悦度回归的可复现跨被试基准，并展示可解释性分析可作为标准指标的补充。其最强结论是TCN在时间相关性上最优而卷积类模型在MAE上更稳。对后续EEG情感解码研究，提示应重视跨被试协议与时间可解释性；工业上可用于个性化音乐推荐的原型验证，但r=0.21的精度尚不足以直接落地。

## ⚠️ 局限与未解决问题

Pearson r仅0.21，预测能力有限；仅20名被试、单一数据集，跨被试泛化证据薄弱；未报告推理延迟与模型参数量；缺少与经典EEG基线（如FBCSP、EEGNet）的数值对比；可解释性仅针对TCN，未验证解释稳定性。

---

<div class="paper-footer"><span>评分：4.5</span><span>原始：4.5</span><a href="/audio-paper-daily/posts/2026-10-16/">← 返回 2026-10-16 速递</a></div>
