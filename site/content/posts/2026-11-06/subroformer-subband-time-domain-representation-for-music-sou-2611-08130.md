---
title: "SubRoformer: Subband Time-Domain Representation for Music Source Separation"
date: 2026-11-06T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#乐器分离"]
summary: "提出子带时域表示加残差 RoFormer 的 Transformer 系统，在 MUSDB18-HQ 上四轨平均 SDR 达 10.63 dB（目标专属模型）与 11.59 dB（单模型多轨）。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#乐器分离</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#乐器分离</span> <span class="tag-pill tag-pill-soft">#Transformer</span> <span class="tag-pill tag-pill-soft">#子带建模</span> <span class="tag-pill tag-pill-soft">#复数域掩码</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2611.08130</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-11-06</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">🔥 强烈推荐通读</span></div>
<div class="meta-row"><span class="meta-key">⭐</span><span class="meta-val focus-badge">本站重点关注领域 · 评分 +1</span></div>
</div>
</div>

<div class="opensource-banner"><div class="oc-headline"><span class="oc-pulse"></span><span class="oc-title">本论文已开源</span><span class="oc-hint">点击下方卡片直达对应资源</span></div><div class="oc-grid"><a class="oc-chip oc-chip-code" href="https://github.com/ArchiMickey/SubRoformer" target="_blank" rel="noopener"><span class="oc-icon">💻</span><span class="oc-text"><span class="oc-label">代码仓库</span><span class="oc-sub">ArchiMickey/SubRoformer</span></span></a></div></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2611.08130" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2611.08130" target="_blank" rel="noopener">📑 PDF</a><a class="rsrc rsrc-code" href="https://github.com/ArchiMickey/SubRoformer" target="_blank" rel="noopener">💻 代码</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出子带时域表示加残差 RoFormer 的 Transformer 系统，在 MUSDB18-HQ 上四轨平均 SDR 达 10.63 dB（目标专属模型）与 11.59 dB（单模型多轨）。
</div>

## 👥 作者与机构

**Chunyat Wu** ¹ · Chuang Ding · Paris Smaragdis · Qiuqiang Kong

**机构**：香港中文大学 · 伊利诺伊大学厄巴纳-香槟分校

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合做音乐分离与 Transformer 音频建模的研究者与工程团队阅读。建议通读：重点看 §3 子带分解/重构模块与残差 RoFormer 的门控融合设计，以及表 2、表 3 中与 BSRNN、HT Demucs、Band-Split RNN 等基线的对比；复现可直接用其开源 checkpoint。

## 🌍 研究背景

音乐源分离此前主流分两派：波形域方法（如 Demucs、HDemucs）样本数多、计算开销大；全带频谱图方法（如 BSRNN、Band-Split RNN）受单一时频分辨率折衷限制，低频与高频难以同时兼顾。混合域方法虽有改进，但跨频带建模与时间分辨率压缩仍不充分。本文要解决的是：如何在降低采样率与计算量的同时，保留频带局部性与跨频带上下文，从而更准确地估计各 stem 的复数掩码。

## 💡 核心创新

1. 子带模块将混合分解为频率局部化、低采样率信号再重构目标波形
2. 残差 RoFormer 在时间压缩特征上建模时间与跨频带关系
3. 门控残差融合将上下文与细粒度特征结合估计复数掩码
4. 目标专属与单模型多轨两种设定均达对比系统 SOTA

## 🏗️ 模型架构

输入为时域混合波形，先经子带模块分解为若干频率局部化、低采样率的子带信号；主干为 Transformer 结构的残差 RoFormer 模块，在时间压缩后的特征上建模时间依赖与跨频带关系，再通过门控残差融合（gated residual fusion）与细时间分辨率特征结合，输出源特定的复数掩码；最后由子带模块从估计子带重构目标波形。摘要未给出参数量。

## 📚 数据集

- MUSDB18-HQ（训练与评估，仅用其训练集训练）
- 额外 500 首歌曲（训练，用于单模型多轨设定）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| SDR（四轨平均） | MUSDB18-HQ test | 对比系统（目标专属模型，无额外数据） | **10.63 dB** | 达对比系统 SOTA |
| SDR（四轨平均） | MUSDB18-HQ test | 对比单模型多轨系统（含额外数据） | **11.59 dB** | 达对比系统 SOTA |

摘要仅报告两项平均 SDR：仅用 MUSDB18-HQ 训练的目标专属模型为 10.63 dB，加入 500 首额外歌曲的单模型多轨系统为 11.59 dB，均称在对比系统中取得 SOTA。摘要未给出各 stem 分项 SDR、SI-SDRi、消融实验、推理延迟或参数量等细节，需查阅正文与开源代码确认。

## 🎯 结论与影响

最强结论是子带时域表示配合残差 RoFormer 可在不依赖额外数据时达到对比系统最优的四轨平均 SDR，加少量额外数据后单模型多轨亦领先。这为音乐分离中“降采样+跨频带建模”的路线提供了可复现基线，对音乐重混、内容生产等落地场景有直接参考价值。

## ⚠️ 局限与未解决问题

摘要未报告各 stem 分项指标、消融（子带模块与门控融合各自贡献）、推理延迟与显存开销；对比系统清单未列出，SOTA 声明需正文核实；额外数据仅 500 首，规模与来源未说明，可能存在数据偏置；缺少与最新混合域方法的系统比较。

## 🔗 开源资源

- **代码**：<https://github.com/ArchiMickey/SubRoformer>

---

<div class="paper-footer"><span>评分：9.2</span><span>原始：8.2</span><span>+1 重点领域加权</span><a href="/audio-paper-daily/posts/2026-11-06/">← 返回 2026-11-06 速递</a></div>
