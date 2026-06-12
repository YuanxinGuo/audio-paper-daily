---
title: "Towards Personalized Federated Learning for Dysarthric Speech Recognition"
date: 2026-06-12T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#语音识别"]
summary: "针对构音障碍语音识别，提出两种联邦学习个性化聚合策略，在UASpeech和TORGO上取得WER降低。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#语音识别</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#联邦学习</span> <span class="tag-pill tag-pill-soft">#个性化</span> <span class="tag-pill tag-pill-soft">#构音障碍语音</span> <span class="tag-pill tag-pill-soft">#语音识别</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2606.13253</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-06-12</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2606.13253" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2606.13253" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>针对构音障碍语音识别，提出两种联邦学习个性化聚合策略，在UASpeech和TORGO上取得WER降低。
</div>

## 👥 作者与机构

**Tao Zhong** ¹ · Mengzhe Geng · Jiajun Deng · Shujie Hu · Xunying Liu ✉

**机构**：香港中文大学

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合研究联邦学习或构音障碍语音识别的读者。建议重点阅读§3的两种聚合策略和§4的实验结果，特别是表1和表2。可先看§3.2和§3.3了解方法细节。

## 🌍 研究背景

构音障碍语音识别因说话人变异性大而具有挑战性。联邦学习（FL）虽能保护隐私，但面临异质性难题。现有FL方法如FedAvg强制所有说话人共享模型参数，在异质性下效果不佳。个性化FL是一个有前景的方向，但在构音障碍语音上研究有限。本文旨在探索两种个性化聚合策略以提升识别性能。

## 💡 核心创新

1. 提出基于参数的个性化平均策略（P-Avg）
2. 提出基于嵌入的个性化平均策略（E-Avg）
3. 在构音障碍语音上首次系统比较两种个性化FL方法

## 🏗️ 模型架构

采用基于Conformer的端到端ASR模型作为基础架构。输入为80维FBank特征，经CNN下采样后送入Conformer编码器，再经RNN-T解码器输出词片序列。联邦学习框架中，各客户端本地训练后，服务器通过参数平均或嵌入平均聚合生成个性化模型。

## 📚 数据集

- UASpeech（训练/评估，包含16个构音障碍说话人）
- TORGO（训练/评估，包含8个构音障碍说话人）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| WER (%) | UASpeech | 正则化FedAvg (31.4) | **P-Avg (30.41)** | -0.99%绝对 |
| WER (%) | TORGO | 正则化FedAvg (11.84) | **E-Avg (11.28)** | -0.56%绝对 |

在UASpeech上，P-Avg和E-Avg分别取得30.41%和30.56%的WER，相比基线正则化FedAvg（31.4%）分别降低0.99%和0.84%绝对。在TORGO上，E-Avg取得11.28%的WER，相比基线（11.84%）降低0.56%绝对。两种策略均优于基线，且统计显著。

## 🎯 结论与影响

本文提出的两种个性化联邦学习策略在构音障碍语音识别上显著优于传统FedAvg，验证了个性化FL在异质性场景下的有效性。未来可探索更细粒度的个性化方法，并扩展到更多说话人和数据集。对工业落地，该方案可在保护隐私的同时提升构音障碍用户的ASR体验。

## ⚠️ 局限与未解决问题

实验仅在两个小规模数据集上进行，说话人数量有限；未报告推理延迟或模型大小等效率指标；未与更先进的个性化FL方法（如pFedMe、Per-FedAvg）对比；缺乏对聚合策略的消融分析。

---

<div class="paper-footer"><span>评分：7.2</span><span>原始：7.2</span><a href="/audio-paper-daily/posts/2026-06-12/">← 返回 2026-06-12 速递</a></div>
