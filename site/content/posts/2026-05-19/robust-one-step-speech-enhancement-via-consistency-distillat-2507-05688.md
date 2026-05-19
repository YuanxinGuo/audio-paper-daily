---
title: "Robust One-step Speech Enhancement via Consistency Distillation"
date: 2026-05-19T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#语音增强"]
summary: "提出ROSE-CD，通过一致性蒸馏实现单步扩散语音增强，引入随机学习轨迹和时域辅助损失，在VoiceBank-DEMAND上达到SOTA，推理速度提升54倍。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero hero-focus">
<div class="hero-score">
<div class="score-num">9.5</div>
<div class="score-stars">★★★★★</div>
<div class="score-tier">前10%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#语音增强</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#一致性蒸馏</span> <span class="tag-pill tag-pill-soft">#扩散模型</span> <span class="tag-pill tag-pill-soft">#单步推理</span> <span class="tag-pill tag-pill-soft">#语音增强</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2507.05688</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-05-19</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">🔥 强烈推荐通读</span></div>
<div class="meta-row"><span class="meta-key">⭐</span><span class="meta-val focus-badge">本站重点关注领域 · 评分 +1</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2507.05688" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2507.05688" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出ROSE-CD，通过一致性蒸馏实现单步扩散语音增强，引入随机学习轨迹和时域辅助损失，在VoiceBank-DEMAND上达到SOTA，推理速度提升54倍。
</div>

## 👥 作者与机构

**Liang Xu** ¹ · Longfei Felix Yan · W. Bastiaan Kleijn

**机构**：维多利亚大学惠灵顿

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合语音增强和扩散模型研究者。建议通读，重点看§3的随机学习轨迹设计和§4的时域辅助损失。可对比现有蒸馏方法（如CTM）的差异。

## 🌍 研究背景

扩散模型在语音增强中表现优异，但多步迭代采样限制了实时应用。一致性蒸馏通过将多步教师模型蒸馏为单步学生模型，有望解决推理速度问题。然而，蒸馏模型存在对教师采样轨迹的固有偏差，导致对噪声鲁棒性差且易继承教师误差。本文旨在提出一种鲁棒的单步一致性蒸馏方法，克服上述局限。

## 💡 核心创新

1. 提出随机学习轨迹，增强模型对噪声的鲁棒性
2. 联合优化两个时域辅助损失，使学生模型超越教师
3. 首个纯单步一致性蒸馏模型用于扩散语音增强
4. 推理速度比30步教师模型快54倍

## 🏗️ 模型架构

输入带噪语音→预训练扩散教师模型（多步）→一致性蒸馏学生模型（单步）。学生模型采用与教师相同的U-Net架构，但通过随机学习轨迹训练：在训练时随机选择时间步和噪声水平，而非固定教师采样路径。同时，联合优化两个时域辅助损失（L1损失和SI-SDR损失），使学生模型能从教师误差中恢复。输出为增强后的干净语音。

## 📚 数据集

- VoiceBank-DEMAND（训练和评估，包含28个说话人）
- DNS-Challenge（域外泛化评估）
- 真实噪声录音（泛化评估）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| PESQ | VoiceBank-DEMAND测试集 | SGMSE+ (3.12) | **3.22** | +0.10 |
| CSIG | VoiceBank-DEMAND测试集 | SGMSE+ (4.21) | **4.33** | +0.12 |
| CBAK | VoiceBank-DEMAND测试集 | SGMSE+ (3.65) | **3.72** | +0.07 |
| COVL | VoiceBank-DEMAND测试集 | SGMSE+ (3.49) | **3.62** | +0.13 |

在VoiceBank-DEMAND上，ROSE-CD在PESQ、CSIG、CBAK、COVL指标上均超越SGMSE+等基线，达到SOTA。推理速度比30步教师模型快54倍。在DNS-Challenge域外数据集和真实噪声录音上，模型表现出良好的泛化能力，验证了随机学习轨迹和辅助损失的有效性。

## 🎯 结论与影响

ROSE-CD通过一致性蒸馏实现了单步扩散语音增强，在保持SOTA质量的同时大幅提升推理速度。随机学习轨迹和时域辅助损失有效克服了蒸馏偏差，使学生模型超越教师。该工作为实时语音增强提供了高效方案，有望推动扩散模型在低延迟场景的落地。

## ⚠️ 局限与未解决问题

仅在VoiceBank-DEMAND单一数据集上报告主要结果，缺乏更多数据集（如WSJ0-2mix）的对比。未提供模型参数量和计算复杂度（除推理速度外）。未讨论蒸馏过程对教师模型选择敏感性的影响。域外泛化仅定性展示，缺乏定量指标。

---

<div class="paper-footer"><span>评分：9.5</span><span>原始：8.5</span><span>+1 重点领域加权</span><a href="/audio-paper-daily/posts/2026-05-19/">← 返回 2026-05-19 速递</a></div>
