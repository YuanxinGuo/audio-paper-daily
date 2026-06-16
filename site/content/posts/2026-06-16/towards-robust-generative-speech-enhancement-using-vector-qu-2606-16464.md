---
title: "Towards Robust Generative Speech Enhancement Using Vector Quantisation-Based Neural Audio Codec"
date: 2026-06-16T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#语音增强"]
summary: "探究VQ神经音频编解码在语音增强中连续与离散潜空间建模策略，发现VQ正则化可提升鲁棒性。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero hero-focus">
<div class="hero-score">
<div class="score-num">8.8</div>
<div class="score-stars">★★★★☆</div>
<div class="score-tier">前25%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#语音增强</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#语音增强</span> <span class="tag-pill tag-pill-soft">#向量量化</span> <span class="tag-pill tag-pill-soft">#神经音频编解码</span> <span class="tag-pill tag-pill-soft">#生成式方法</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2606.16464</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-06-16</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
<div class="meta-row"><span class="meta-key">⭐</span><span class="meta-val focus-badge">本站重点关注领域 · 评分 +1</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2606.16464" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2606.16464" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>探究VQ神经音频编解码在语音增强中连续与离散潜空间建模策略，发现VQ正则化可提升鲁棒性。
</div>

## 👥 作者与机构

**Haixin Zhao** ¹ · Nilesh Madhu ✉

**机构**：根特大学

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合语音增强和生成式模型研究者。重点看§3框架设计、§4理论分析与可视化、表1结果。可先读§4理解VQ正则化作用。

## 🌍 研究背景

生成式语音增强方法近年兴起，但基于VQ神经音频编解码的SE框架中，连续与离散潜空间建模策略尚未系统比较。现有方法多直接使用离散token，而连续表示潜力未被充分挖掘。本文旨在探究两种策略的优劣及VQ正则化的本质作用。

## 💡 核心创新

1. 提出cNAC-SE和dNAC-SE两种框架分别预测连续表示和离散token
2. 理论分析并可视化潜空间揭示建模机制
3. 发现VQ正则化通过干净先验约束提升鲁棒性，独立于离散token处理

## 🏗️ 模型架构

输入含噪语音经编码器提取潜表示。cNAC-SE直接预测连续潜表示，dNAC-SE通过VQ层量化后预测离散token。解码器将潜表示重构为增强语音。编码器/解码器基于卷积网络，VQ码本大小8192。参数量未提及。

## 📚 数据集

- DNS-Challenge（训练/评估，包含噪声和干净语音）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| DNS-MOS | DNS-Challenge测试集 | SGMSE+ 3.12 | **cNAC-SE 3.28** | +0.16 |

cNAC-SE在所有测试条件下优于dNAC-SE变体，并在DNS-MOS指标上领先SGMSE+等生成式方法。与判别式方法对比显示，VQ正则化通过干净先验约束提升鲁棒性，且该效果独立于离散token处理。

## 🎯 结论与影响

本文证明基于VQ的连续潜空间建模在语音增强中优于离散token预测，且VQ正则化本身具有鲁棒性提升作用。该发现为生成式SE设计提供新思路，VQ正则化可迁移至其他连续建模方法，具有工业应用潜力。

## ⚠️ 局限与未解决问题

仅在DNS-Challenge单一数据集上评估，缺乏跨数据集泛化验证；未报告推理速度或参数量；与判别式方法对比不够全面（如未与DCCRN等比较）；消融实验未充分分离VQ正则化与其他组件影响。

---

<div class="paper-footer"><span>评分：8.8</span><span>原始：7.8</span><span>+1 重点领域加权</span><a href="/audio-paper-daily/posts/2026-06-16/">← 返回 2026-06-16 速递</a></div>
