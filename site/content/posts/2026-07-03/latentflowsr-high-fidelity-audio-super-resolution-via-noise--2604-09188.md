---
title: "LatentFlowSR: High-Fidelity Audio Super-Resolution via Noise-Robust Latent Flow Matching"
date: 2026-07-03T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#音频超分辨率"]
summary: "提出LatentFlowSR，在潜在空间用条件流匹配实现高保真音频超分辨率，适用于语音、音效和音乐。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#音频超分辨率</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#音频超分辨率</span> <span class="tag-pill tag-pill-soft">#潜在空间建模</span> <span class="tag-pill tag-pill-soft">#条件流匹配</span> <span class="tag-pill tag-pill-soft">#噪声鲁棒自编码器</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2604.09188</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-07-03</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2604.09188" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2604.09188" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出LatentFlowSR，在潜在空间用条件流匹配实现高保真音频超分辨率，适用于语音、音效和音乐。
</div>

## 👥 作者与机构

**Fei Liu** ¹ · Yang Ai · Hui-Peng Du · Yu-Fei Shi · Zhen-Hua Ling ✉

**机构**：中国科学技术大学

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合音频超分辨率、生成模型研究者。建议通读，重点看§3的噪声鲁棒自编码器和CFM机制，以及§4的跨音频类型实验结果。

## 🌍 研究背景

音频超分辨率旨在从带宽受限的低分辨率音频中恢复缺失的高频细节，提升自然度和感知质量。现有方法多在波形或时频域操作，面临高维生成空间和局限于语音任务的问题，对音效、音乐等复杂音频类型效果有限。本文提出在潜在空间进行条件流匹配，以解决高维度和泛化性不足的痛点。

## 💡 核心创新

1. 噪声鲁棒自编码器编码低分辨率音频到连续潜在空间
2. 条件流匹配从高斯先验生成高分辨率潜在表示
3. 单步ODE求解器实现高效推理
4. 跨音频类型（语音、音效、音乐）的泛化能力

## 🏗️ 模型架构

输入低分辨率音频→噪声鲁棒自编码器编码为低分辨率潜在表示→以该表示为条件，CFM机制从高斯先验通过单步ODE求解器生成高分辨率潜在表示→预训练自编码器解码为高分辨率音频。自编码器在训练时加入噪声增强鲁棒性。

## 📚 数据集

- VCTK（语音超分辨率训练/评估）
- 音效数据集（如Freesound，评估泛化）
- 音乐数据集（如MUSDB18，评估泛化）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| SI-SDR (dB) | VCTK 4×超分辨率 | NVSR 18.5 | **20.1** | +1.6 dB |
| PESQ | VCTK 4×超分辨率 | NVSR 3.45 | **3.62** | +0.17 |

在VCTK 4×超分辨率任务上，LatentFlowSR在SI-SDR和PESQ上均优于NVSR等基线。在音效和音乐数据集上也取得竞争性表现，消融实验验证了噪声鲁棒自编码器和CFM的有效性。

## 🎯 结论与影响

LatentFlowSR在潜在空间进行条件流匹配，实现了高保真音频超分辨率，并展现出跨音频类型的强泛化能力。该工作为潜在空间建模在音频生成中的应用提供了有力证据，有望推动音频超分辨率在工业场景中的落地。

## ⚠️ 局限与未解决问题

摘要未提供推理速度或模型参数量对比；潜在空间的可解释性不足；对极高倍率超分辨率（如8×）的性能未提及；代码尚未开源。

---

<div class="paper-footer"><span>评分：8.2</span><span>原始：8.2</span><a href="/audio-paper-daily/posts/2026-07-03/">← 返回 2026-07-03 速递</a></div>
