---
title: "Investigating Codec-Internal Latent Audio Watermarking for Neural Codec Robustness"
date: 2026-07-24T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#音频水印"]
summary: "研究在神经音频编解码器的连续潜在空间中嵌入水印，以提升对编解码变换的鲁棒性，并分析了水印嵌入位置与质量/鲁棒性的权衡。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero hero-focus">
<div class="hero-score">
<div class="score-num">8.2</div>
<div class="score-stars">★★★★☆</div>
<div class="score-tier">前25%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#音频水印</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#神经音频编解码</span> <span class="tag-pill tag-pill-soft">#潜在空间水印</span> <span class="tag-pill tag-pill-soft">#鲁棒性</span> <span class="tag-pill tag-pill-soft">#语音增强</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2607.21132</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-07-24</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
<div class="meta-row"><span class="meta-key">⭐</span><span class="meta-val focus-badge">本站重点关注领域 · 评分 +1</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2607.21132" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2607.21132" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>研究在神经音频编解码器的连续潜在空间中嵌入水印，以提升对编解码变换的鲁棒性，并分析了水印嵌入位置与质量/鲁棒性的权衡。
</div>

## 👥 作者与机构

**Zi Hu** ¹ · Houmin Sun · Linxi Li · Yechen Wang · Liwei Jin · Carsten Maple · Ming Li

**机构**：杜伦大学 · 华威大学

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合音频水印、神经编解码领域的研究者。建议重点阅读第3节方法部分和第4节实验，特别是表1和图2的权衡分析。可先看§3.2的Conformer嵌入器和§3.3的RVQ分解。

## 🌍 研究背景

神经音频编解码器（如EnCodec）因其重编码、量化和重合成过程，对音频水印构成严峻挑战。传统水印方法在波形或频谱上嵌入，易被编解码破坏。本文旨在探索在编解码器内部的连续潜在空间中嵌入水印，以提升对编解码变换的鲁棒性，并系统研究嵌入位置（波形、频谱、潜在空间）带来的质量与鲁棒性权衡。

## 💡 核心创新

1. 提出在类编解码器自编码器的连续潜在空间中嵌入水印
2. 使用Conformer作为消息嵌入器，结合RVQ引导的潜在分解
3. 在潜在域训练检测器，同时考虑信号处理和神经编解码变换
4. 系统评估了水印嵌入位置对质量和鲁棒性的影响

## 🏗️ 模型架构

输入48 kHz语音，经SEANet风格编码器得到连续潜在表示。Conformer-based消息嵌入器将32-bit消息嵌入潜在表示中，然后通过RVQ（残差向量量化）引导的潜在分解进行量化。解码器重建带水印语音。检测器在潜在域训练，使用信号处理和神经编解码变换增强鲁棒性。整体流程为：语音→编码器→潜在嵌入（Conformer）→RVQ→解码器→带水印语音。

## 📚 数据集

- 48 kHz语音数据（训练/评估，未指定具体名称）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| 比特准确率 | EnCodec-24k | 波形域水印 78.8% | **潜在域水印 95.6%** | +16.8% |
| 比特准确率 | EnCodec-24k | 频谱域水印 78.8% | **潜在域水印 97.1%** | +18.3% |
| PESQ | 48 kHz语音 | 无水印 4.5（估计） | **潜在域水印 3.514** | -0.213 |
| PESQ | 48 kHz语音 | 无 | **潜在域水印 3.427** | （相对于另一配置） |

实验表明，在EnCodec-24k编解码下，潜在域水印的比特准确率从波形域的78.8%提升至95.6%和97.1%，但PESQ从3.727下降至3.514和3.427，揭示了鲁棒性与质量之间的权衡。未提供其他数据集或消融实验细节。

## 🎯 结论与影响

本文证明在神经编解码器的连续潜在空间中嵌入水印能显著提升对编解码变换的鲁棒性，但会牺牲一定语音质量。该工作为设计鲁棒音频水印提供了新思路，未来可探索更优的嵌入策略以平衡质量与鲁棒性，对数字版权保护和内容认证有潜在应用价值。

## ⚠️ 局限与未解决问题

仅使用单一编解码器EnCodec评估，未测试其他编解码器（如SoundStream、Lyra）；未报告推理延迟或计算开销；缺乏对不同消息长度、攻击类型（如加噪、裁剪）的鲁棒性测试；PESQ下降明显，实际应用需权衡。

---

<div class="paper-footer"><span>评分：8.2</span><span>原始：7.2</span><span>+1 重点领域加权</span><a href="/audio-paper-daily/posts/2026-07-24/">← 返回 2026-07-24 速递</a></div>
