---
title: "FiPA-SR -- FiLM-Conditioned Perceptually Informed Audio Super-Resolution"
date: 2026-08-11T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#音频超分辨率"]
summary: "提出FiPA-SR，一种基于GAN的音频超分辨率模型，通过FiLM层适配不同输入带宽，在MUSDB上超越AudioSR且更高效。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero">
<div class="hero-score">
<div class="score-num">7.8</div>
<div class="score-stars">★★★★☆</div>
<div class="score-tier">前25%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#音频超分辨率</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#音频带宽扩展</span> <span class="tag-pill tag-pill-soft">#GAN</span> <span class="tag-pill tag-pill-soft">#FiLM</span> <span class="tag-pill tag-pill-soft">#Mamba</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2605.30594</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-08-11</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2605.30594" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2605.30594" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出FiPA-SR，一种基于GAN的音频超分辨率模型，通过FiLM层适配不同输入带宽，在MUSDB上超越AudioSR且更高效。
</div>

## 👥 作者与机构

**Wallace Abreu** ¹ · Luiz W. P. Biscainho

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合音频超分辨率、生成模型研究者阅读。值得通读，重点看第3节模型架构和第4节实验对比。可先看表1和表2了解性能提升。

## 🌍 研究背景

音频带宽扩展旨在从带限信号重建缺失的高频内容。现有方法如AudioSR基于扩散模型，虽性能好但计算开销大。本文基于AEROMamba_P框架，引入FiLM层实现单一模型处理多种输入带宽，旨在提升性能同时降低计算成本。

## 💡 核心创新

1. 引入FiLM层适配不同输入带宽
2. 基于GAN的感知架构，提升重建质量
3. 相比AudioSR，GPU内存减少3倍，推理快60倍以上

## 🏗️ 模型架构

输入带限音频经特征提取后，送入基于Mamba的主干网络，通过FiLM层根据输入带宽调整特征，再经上采样和GAN判别器训练，输出全频带音频。

## 📚 数据集

- MUSDB（训练/评估）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| 客观指标（如SI-SDR） | MUSDB | AudioSR | **FiPA-SR** | 优于AudioSR |

实验表明FiPA-SR在8、20、32 kHz输入采样率下均优于AudioSR，且GPU内存减少约3倍，推理速度提升60倍以上。具体指标数值未在摘要中给出。

## 🎯 结论与影响

FiPA-SR通过FiLM条件化实现了高效的多带宽音频超分辨率，显著优于扩散基线，为实时应用提供了可能。后续研究可探索更轻量级架构和更多带宽适配。

## ⚠️ 局限与未解决问题

摘要未提供具体指标数值，缺乏与更多基线的对比；未讨论不同音乐类型的泛化性；未提及推理延迟的具体硬件环境。

---

<div class="paper-footer"><span>评分：7.8</span><span>原始：7.8</span><a href="/audio-paper-daily/posts/2026-08-11/">← 返回 2026-08-11 速递</a></div>
