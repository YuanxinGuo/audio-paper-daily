---
title: "Time-Unconditional Generative Speech Enhancement via Autonomous Rectified Flow"
date: 2026-06-19T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#语音增强"]
summary: "提出时间无条件的自主整流流框架，去除显式时间步嵌入，提升语音增强质量与推理效率。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero hero-focus">
<div class="hero-score">
<div class="score-num">9.2</div>
<div class="score-stars">★★★★★</div>
<div class="score-tier">前25%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#语音增强</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#生成式语音增强</span> <span class="tag-pill tag-pill-soft">#整流流</span> <span class="tag-pill tag-pill-soft">#时间无条件</span> <span class="tag-pill tag-pill-soft">#扩散模型</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2606.20001</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-06-19</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
<div class="meta-row"><span class="meta-key">⭐</span><span class="meta-val focus-badge">本站重点关注领域 · 评分 +1</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2606.20001" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2606.20001" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出时间无条件的自主整流流框架，去除显式时间步嵌入，提升语音增强质量与推理效率。
</div>

## 👥 作者与机构

**Wen Zhang** ¹ · Wenbin Jiang · Yang Zhang · Xiaofei Zhou

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合语音增强与生成模型研究者。重点读§3（时间不变性证明）与§4（网络设计）。建议复现其消融实验。

## 🌍 研究背景

生成式语音增强方法通常依赖扩散模型或流模型，需要显式时间步嵌入来调节去噪过程。然而，这种时间条件可能导致模型过拟合时间轨迹，限制泛化能力。本文挑战这一范式，证明在特定插值路径下目标向量场是时间不变的，从而提出无需时间条件的自主整流流框架。

## 💡 核心创新

1. 证明线性插值路径下目标向量场时间不变性
2. 提出时间无条件网络，仅从空间关系推断去噪方向
3. 避免过拟合时间轨迹，提升生成质量与鲁棒性
4. 简化模型结构，提高推理效率

## 🏗️ 模型架构

输入含噪语音特征，通过线性插值路径构建当前状态与带噪观测的空间关系。主干网络采用时间无条件网络（如U-Net或Transformer变体），去除时间步嵌入，直接预测目标向量场（等价于噪声分布）。输出为增强后的干净语音。

## 📚 数据集

- DNS-Challenge（训练与评估，含噪声和干净语音）
- LibriTTS（训练与评估，干净语音）
- WHAM!（评估，含噪混合）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| PESQ | DNS-Challenge test set | SGMSE+ 2.86 | **3.12** | +0.26 |
| SI-SDR (dB) | WHAM! test set | SGMSE+ 13.4 | **14.8** | +1.4 dB |

在DNS-Challenge和WHAM!数据集上，所提方法在PESQ和SI-SDR上均优于SGMSE+等基线。消融实验验证了时间无条件设计的有效性，且推理速度提升约30%。

## 🎯 结论与影响

本文证明在特定插值路径下，语音增强的向量场可时间不变，从而提出时间无条件网络。该方法简化了生成式增强流程，提升了质量与效率，为未来生成式语音处理提供了新范式。

## ⚠️ 局限与未解决问题

仅在合成噪声场景下验证，未见真实噪声泛化实验；未报告模型参数量与计算复杂度；与最新扩散模型（如StoRM）对比缺失。

---

<div class="paper-footer"><span>评分：9.2</span><span>原始：8.2</span><span>+1 重点领域加权</span><a href="/audio-paper-daily/posts/2026-06-19/">← 返回 2026-06-19 速递</a></div>
