---
title: "Learning from Annotation Uncertainty: Entropy-Aware Curriculum for Speech Emotion Recognition"
date: 2026-06-29T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#语音情感识别"]
summary: "提出基于标注不确定性的分布监督方法，使用WavLM多任务模型在9类情感识别中优于硬标签训练。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#语音情感识别</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#分布监督</span> <span class="tag-pill tag-pill-soft">#标注不确定性</span> <span class="tag-pill tag-pill-soft">#WavLM</span> <span class="tag-pill tag-pill-soft">#MSP-Podcast</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2606.27536</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-06-29</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2606.27536" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2606.27536" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出基于标注不确定性的分布监督方法，使用WavLM多任务模型在9类情感识别中优于硬标签训练。
</div>

## 👥 作者与机构

**Zahra Omidi** ¹ · John H. L. Hansen

**机构**：德克萨斯大学达拉斯分校

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合SER研究者阅读，重点看§3的分布监督方法和§4.3的熵分层评估。可先看表1对比结果。

## 🌍 研究背景

语音情感识别通常使用硬共识标签，忽略标注者之间的分歧。先前SOTA方法多基于硬标签训练，但无法捕捉情感感知的不确定性。本文旨在利用标注者投票分布作为监督信号，提升模型与人类感知的一致性。

## 💡 核心创新

1. 使用主标注和主-次标注合并的投票分布作为训练目标
2. 引入熵分层评估分析高歧义样本
3. WavLM-Base多任务模型同时预测类别和VAD维度

## 🏗️ 模型架构

输入为语音特征，主干网络采用WavLM-Base，后接两个分支：一个用于9类情感分类（输出分布），另一个用于维度VAD回归。训练时使用KL散度或JS散度作为分布损失。

## 📚 数据集

- MSP-Podcast 2.0（训练/评估，9类情感标注）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| JSD | MSP-Podcast 2.0 | 硬标签训练（未给出具体值） | **分布监督（未给出具体值）** | 降低（具体值未给出） |
| KLD | MSP-Podcast 2.0 | 硬标签训练（未给出具体值） | **分布监督（未给出具体值）** | 降低（具体值未给出） |

分布监督相比硬标签训练降低了JSD和KLD，表明与人类投票分布更一致。熵分层评估显示高歧义样本仍具挑战，但分布监督更好地捕捉了感知不确定性。

## 🎯 结论与影响

分布监督能更好地反映标注者分歧，提升SER模型与人类感知的一致性。未来可探索更复杂的标注不确定性建模，对实际应用中的情感标注收集有指导意义。

## ⚠️ 局限与未解决问题

仅在MSP-Podcast数据集上评估，未验证跨数据集泛化；未报告模型参数量和推理速度；未与最新SER方法（如基于自监督模型）对比。

---

<div class="paper-footer"><span>评分：7.2</span><span>原始：7.2</span><a href="/audio-paper-daily/posts/2026-06-29/">← 返回 2026-06-29 速递</a></div>
