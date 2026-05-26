---
title: "Diffusion-based Frameworks for Unsupervised Speech Enhancement"
date: 2026-05-26T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#语音增强"]
summary: "提出无监督扩散语音增强框架，显式联合建模语音和噪声，在WSJ0-QUT和VoiceBank-DEMAND上优于现有无监督方法。"
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
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#扩散模型</span> <span class="tag-pill tag-pill-soft">#无监督学习</span> <span class="tag-pill tag-pill-soft">#噪声建模</span> <span class="tag-pill tag-pill-soft">#语音增强</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2601.09931</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-05-26</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">🔥 强烈推荐通读</span></div>
<div class="meta-row"><span class="meta-key">⭐</span><span class="meta-val focus-badge">本站重点关注领域 · 评分 +1</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2601.09931" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2601.09931" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出无监督扩散语音增强框架，显式联合建模语音和噪声，在WSJ0-QUT和VoiceBank-DEMAND上优于现有无监督方法。
</div>

## 👥 作者与机构

**Jean-Eudes Ayilo** ¹ · Mostafa Sadeghi · Romain Serizel · Xavier Alameda-Pineda

**机构**：法国国家信息与自动化研究所 · 欧洲电信学院

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合语音增强、扩散模型研究者。建议重点阅读§3的联合采样框架和§4的扩散噪声先验。先看表1和表2对比结果，再读§3.2的E-step推导。

## 🌍 研究背景

无监督语音增强旨在无需配对数据训练，现有方法结合基于干净语音的分数扩散模型与NMF噪声先验，通过EM迭代估计干净语音。但NMF噪声模型表达能力有限，且E-step仅采样语音，忽略噪声不确定性。本文提出显式联合建模语音和噪声，并引入扩散噪声先验替代NMF，提升增强性能。

## 💡 核心创新

1. 显式联合采样语音和噪声的E-step
2. 扩散噪声先验替代NMF噪声模型
3. 半监督框架联合训练语音和噪声扩散模型
4. 隐式和显式噪声建模两种变体

## 🏗️ 模型架构

输入含噪语音→基于分数匹配的扩散模型（语音和噪声联合建模）。E-step：给定观测，通过反向扩散联合采样语音和噪声潜变量；M-step：更新噪声协方差（NMF）或扩散参数。两种变体：隐式噪声建模（条件分数模型同时预测语音和噪声）和显式噪声建模（噪声作为独立潜变量）。

## 📚 数据集

- WSJ0-QUT（训练/评估，含噪语音）
- VoiceBank-DEMAND（训练/评估，含噪语音）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| PESQ | VoiceBank-DEMAND | SGMSE+ (2.08) | **2.32** | +0.24 |
| STOI | VoiceBank-DEMAND | SGMSE+ (0.91) | **0.93** | +0.02 |
| SI-SDR (dB) | WSJ0-QUT | SGMSE+ (9.8) | **11.2** | +1.4 |

在WSJ0-QUT和VoiceBank-DEMAND上，显式噪声建模的扩散框架在PESQ、STOI和SI-SDR上均优于SGMSE+等无监督方法。在失配条件下，基于NMF的显式噪声框架比监督基线更鲁棒。消融实验验证了联合采样和扩散噪声先验的有效性。

## 🎯 结论与影响

显式联合建模语音和噪声显著提升无监督扩散语音增强性能，扩散噪声先验在匹配条件下达到最佳质量。该框架为无监督SE提供了新范式，有望减少对配对数据的依赖，推动实际应用。

## ⚠️ 局限与未解决问题

扩散模型推理速度慢，未报告实时因子；仅在两个数据集上评估，泛化性待验证；未与最新监督方法（如DPCRN）对比；噪声先验训练需干净噪声数据，实际中可能不易获取。

---

<div class="paper-footer"><span>评分：9.2</span><span>原始：8.2</span><span>+1 重点领域加权</span><a href="/audio-paper-daily/posts/2026-05-26/">← 返回 2026-05-26 速递</a></div>
