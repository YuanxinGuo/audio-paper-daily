---
title: "LL-SDR: Low-Latency Speech enhancement through Discrete Representations"
date: 2026-07-29T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#语音增强"]
summary: "提出LL-SDR，一种基于离散表示的语音增强框架，通过VO-RVQ解耦语音和噪声，并引入潜在空间判别器提升增强质量，实现低延迟高性能。"
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
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#语音增强</span> <span class="tag-pill tag-pill-soft">#离散表示</span> <span class="tag-pill tag-pill-soft">#矢量量化</span> <span class="tag-pill tag-pill-soft">#低延迟</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2603.20242</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-07-29</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
<div class="meta-row"><span class="meta-key">⭐</span><span class="meta-val focus-badge">本站重点关注领域 · 评分 +1</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2603.20242" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2603.20242" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出LL-SDR，一种基于离散表示的语音增强框架，通过VO-RVQ解耦语音和噪声，并引入潜在空间判别器提升增强质量，实现低延迟高性能。
</div>

## 👥 作者与机构

**Jingyi Li** ¹ · Luca Della Libera · Mirco Ravanelli · Mingkun Xu · Cem Subakan

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合语音增强和离散表示方向的研究者。建议重点阅读§3的VO-RVQ设计和§4的潜在空间判别器，以及表2和表3的实验结果。可先看摘要和结论了解整体贡献。

## 🌍 研究背景

现有语音增强方法多基于连续表示，近期离散音频令牌被用于自回归生成，但离散化本身是否持续提升性能尚不明确。本文旨在探索离散表示在语音增强中的优势，解决语音和噪声分布难以分离的问题。

## 💡 核心创新

1. 提出VO-RVQ，按方差排序残差量化以解耦语音和噪声
2. 设计潜在空间判别器，对齐增强与语义嵌入
3. 实现低延迟推理（GPU上RTF=0.01）

## 🏗️ 模型架构

输入16kHz语音波形，经编码器提取特征，通过VO-RVQ模块进行离散化，其中VO-RVQ按方差排序量化残差以分离语音和噪声。离散令牌经解码器生成增强语音，同时潜在空间判别器将增强嵌入与预训练语义嵌入对齐。整体为前馈结构，无需自回归生成。

## 📚 数据集

- DNS-Challenge（训练/评估，含噪声和干净语音）
- VCTK-DEMAND（评估，含噪声和干净语音）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| PESQ | DNS-Challenge | DEMUCS 3.07 | **3.15** | +0.08 |
| SI-SDR (dB) | VCTK-DEMAND | DEMUCS 18.5 | **19.2** | +0.7 |

LL-SDR在DNS-Challenge和VCTK-DEMAND上均优于连续基线DEMUCS，且匹配自回归令牌方法的性能。模型轻量高效，10秒16kHz语音仅需40G MACs，GPU RTF=0.01，CPU RTF=0.24。消融实验验证了VO-RVQ和潜在判别器的有效性。

## 🎯 结论与影响

LL-SDR证明离散表示能有效提升语音增强性能，VO-RVQ和潜在判别器是关键创新。该工作为低延迟、轻量级语音增强提供了新思路，有望推动实时通信和助听设备等工业应用。

## ⚠️ 局限与未解决问题

仅在合成噪声条件下评估，未见真实场景泛化实验；未与最新基于扩散或GAN的方法对比；VO-RVQ的方差排序策略可能对噪声类型敏感，缺乏鲁棒性分析。

---

<div class="paper-footer"><span>评分：9.2</span><span>原始：8.2</span><span>+1 重点领域加权</span><a href="/audio-paper-daily/posts/2026-07-29/">← 返回 2026-07-29 速递</a></div>
