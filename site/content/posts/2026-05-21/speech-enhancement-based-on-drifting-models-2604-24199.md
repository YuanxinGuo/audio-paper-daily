---
title: "Speech Enhancement Based on Drifting Models"
date: 2026-05-21T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#语音增强"]
summary: "提出DriftSE，一种基于漂移模型的单步语音增强框架，将去噪建模为均衡问题，无需迭代采样即可实现高质量增强。"
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
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#生成模型</span> <span class="tag-pill tag-pill-soft">#单步推理</span> <span class="tag-pill tag-pill-soft">#漂移模型</span> <span class="tag-pill tag-pill-soft">#非配对训练</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2604.24199</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-05-21</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">🔥 强烈推荐通读</span></div>
<div class="meta-row"><span class="meta-key">⭐</span><span class="meta-val focus-badge">本站重点关注领域 · 评分 +1</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2604.24199" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2604.24199" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出DriftSE，一种基于漂移模型的单步语音增强框架，将去噪建模为均衡问题，无需迭代采样即可实现高质量增强。
</div>

## 👥 作者与机构

**Liang Xu** ¹ · Diego Caviedes-Nozal · W. Bastiaan Kleijn · Longfei Felix Yan · Rasmus Kongsgaard Olsson

**机构**：维多利亚大学 · 谷歌 · 南洋理工大学

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合语音增强和生成模型研究者。建议重点阅读§3的漂移场定义和§4的两种公式化方法，以及表1的实验结果。可先看§3.2与表1。

## 🌍 研究背景

语音增强旨在从含噪语音中恢复干净语音。现有方法包括基于映射的判别模型和基于扩散的生成模型。判别模型通常需要配对数据且泛化性有限；扩散模型虽质量高但需多步迭代，推理慢。本文提出一种新的生成框架DriftSE，通过漂移场将噪声分布直接推向干净分布，实现单步高质量增强，并支持非配对训练。

## 💡 核心创新

1. 提出漂移场概念，将去噪建模为均衡问题
2. 实现原生单步推理，无需迭代采样
3. 支持非配对数据训练，通过分布匹配而非样本匹配
4. 提出两种公式化：直接映射和条件生成模型

## 🏗️ 模型架构

DriftSE包含一个映射函数（如U-Net）和一个漂移场。输入含噪语音，映射函数生成初始估计；漂移场是一个学习到的校正向量，将估计推向干净语音的高密度区域。训练时通过最小化推前分布与干净分布之间的差异来优化。推理时仅需单步前向传播。模型参数量未在摘要中给出。

## 📚 数据集

- VoiceBank-DEMAND（训练和评估，标准基准）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| PESQ | VoiceBank-DEMAND | 多步扩散基线（如SGMSE+） | **DriftSE** | 优于多步扩散基线（具体数值未给出） |

在VoiceBank-DEMAND上，DriftSE以单步推理实现了优于多步扩散基线的增强质量，证明了其高效性和高保真度。具体指标数值未在摘要中提供，但声称建立了新范式。

## 🎯 结论与影响

DriftSE通过漂移模型实现了单步高质量语音增强，无需迭代采样，且支持非配对训练。该方法为语音增强提供了新范式，有望推动生成模型在实时应用中的落地。

## ⚠️ 局限与未解决问题

摘要未提供具体指标数值和与最新判别方法的对比；未讨论模型参数量和计算复杂度；仅在一个数据集上验证，泛化性待考；未提及对噪声类型和混响的鲁棒性。

---

<div class="paper-footer"><span>评分：9.5</span><span>原始：8.5</span><span>+1 重点领域加权</span><a href="/audio-paper-daily/posts/2026-05-21/">← 返回 2026-05-21 速递</a></div>
