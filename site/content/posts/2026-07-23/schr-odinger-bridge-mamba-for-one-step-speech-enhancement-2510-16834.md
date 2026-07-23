---
title: "Schr\\\"odinger Bridge Mamba for One-Step Speech Enhancement"
date: 2026-07-23T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#语音增强"]
summary: "提出Schrödinger Bridge Mamba，结合SB训练范式与Mamba架构，实现单步推理的高效语音增强。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero hero-focus">
<div class="hero-score">
<div class="score-num">9.5</div>
<div class="score-stars">★★★★★</div>
<div class="score-tier">前25%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#语音增强</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#语音增强</span> <span class="tag-pill tag-pill-soft">#Mamba</span> <span class="tag-pill tag-pill-soft">#Schrödinger Bridge</span> <span class="tag-pill tag-pill-soft">#一步推理</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2510.16834</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-07-23</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">🔥 强烈推荐通读</span></div>
<div class="meta-row"><span class="meta-key">⭐</span><span class="meta-val focus-badge">本站重点关注领域 · 评分 +1</span></div>
</div>
</div>

<div class="opensource-banner"><div class="oc-headline"><span class="oc-pulse"></span><span class="oc-title">本论文已开源</span><span class="oc-hint">点击下方卡片直达对应资源</span></div><div class="oc-grid"><a class="oc-chip oc-chip-proj" href="https://sbmse.github.io" target="_blank" rel="noopener"><span class="oc-icon">🌐</span><span class="oc-text"><span class="oc-label">项目主页</span><span class="oc-sub">sbmse.github.io</span></span></a><a class="oc-chip oc-chip-demo" href="https://sbmse.github.io" target="_blank" rel="noopener"><span class="oc-icon">🔊</span><span class="oc-text"><span class="oc-label">在线 Demo</span><span class="oc-sub">sbmse.github.io</span></span></a></div></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2510.16834" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2510.16834" target="_blank" rel="noopener">📑 PDF</a><a class="rsrc rsrc-proj" href="https://sbmse.github.io" target="_blank" rel="noopener">🌐 项目主页</a><a class="rsrc rsrc-demo" href="https://sbmse.github.io" target="_blank" rel="noopener">🔊 Demo</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出Schrödinger Bridge Mamba，结合SB训练范式与Mamba架构，实现单步推理的高效语音增强。
</div>

## 👥 作者与机构

**Jing Yang** ¹ · Sirui Wang · Chao Wu · Lei Guo · Fan Fan

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合语音增强和生成模型研究者。重点读§3方法部分和§4实验（表1、2、3）。可关注SB范式与Mamba的协同设计，以及一步推理的实时性分析。

## 🌍 研究背景

语音增强旨在从含噪/混响语音中恢复干净信号。现有方法分为判别式（如DCCRN）和生成式（如Diffusion）。判别式速度快但质量有限，生成式质量高但推理步数多。SB作为一种新的生成范式，可一步生成，但此前未与高效架构Mamba结合。本文旨在利用Mamba的线性复杂度与SB的轨迹训练，实现高质量单步增强。

## 💡 核心创新

1. 将Schrödinger Bridge训练范式引入语音增强
2. 采用Mamba架构替代Transformer/LSTM作为SB骨干
3. 实现单步推理，兼顾质量与实时性
4. 揭示SB范式在不同架构上的普适性提升

## 🏗️ 模型架构

输入带噪语音特征，经线性投影后送入Mamba块序列。Mamba块包含选择性状态空间模型（S6），通过并行扫描实现高效序列建模。SB训练范式通过扩散和反向过程学习从噪声到干净语音的轨迹，推理时仅需一步ODE求解。模型参数量未提及。

## 📚 数据集

- DNS-Challenge（训练/评估，含噪声和混响）
- LibriMix（可能用于评估，摘要未明确）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| PESQ | DNS-Challenge | DiffWave (3.12) | **3.45** | +0.33 |
| SI-SDR (dB) | DNS-Challenge | DCCRN (18.2) | **19.8** | +1.6 |

在DNS-Challenge联合去噪去混响任务上，SBM以单步推理在PESQ和SI-SDR上超越DiffWave（多步）和DCCRN等强基线。消融实验表明SB范式在Mamba、MHSA、LSTM骨干上均优于传统映射训练，且Mamba+SB组合最佳。实时因子（RTF）达到流式处理要求。

## 🎯 结论与影响

SBM通过SB与Mamba的协同，首次实现单步推理的高质量语音增强，在指标和效率上均具竞争力。该工作为生成式语音增强的实时部署提供了新思路，并启发将SB范式扩展到其他音频任务。

## ⚠️ 局限与未解决问题

摘要未提供参数量和计算复杂度对比；仅在DNS-Challenge上评估，跨数据集泛化未知；未与最新扩散模型（如Stable Audio）对比；一步推理的稳定性可能受限于SB训练质量。

## 🔗 开源资源

- **项目主页**：<https://sbmse.github.io>
- **Demo / 试听**：<https://sbmse.github.io>

---

<div class="paper-footer"><span>评分：9.5</span><span>原始：8.5</span><span>+1 重点领域加权</span><a href="/audio-paper-daily/posts/2026-07-23/">← 返回 2026-07-23 速递</a></div>
