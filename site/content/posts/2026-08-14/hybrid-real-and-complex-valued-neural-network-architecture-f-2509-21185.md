---
title: "Hybrid Real- and Complex-Valued Neural Network Architecture for Speech Enhancement"
date: 2026-08-14T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#语音增强"]
summary: "提出混合实值-复值神经网络用于单声道语音增强，在匹配参数下以更低计算量提升语音可懂度和质量。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#语音增强</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#语音增强</span> <span class="tag-pill tag-pill-soft">#复数神经网络</span> <span class="tag-pill tag-pill-soft">#混合架构</span> <span class="tag-pill tag-pill-soft">#单声道</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2509.21185</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-08-14</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
<div class="meta-row"><span class="meta-key">⭐</span><span class="meta-val focus-badge">本站重点关注领域 · 评分 +1</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2509.21185" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2509.21185" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出混合实值-复值神经网络用于单声道语音增强，在匹配参数下以更低计算量提升语音可懂度和质量。
</div>

## 👥 作者与机构

Luan Vin\'icius Fiorio · Alex Young · Ronald M. Aarts

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合语音增强研究者阅读，重点关注混合架构设计（§3）和实验结果（§4）。可先看摘要和结论，再细读方法部分，对比不同主干网络下的性能与效率。

## 🌍 研究背景

语音增强旨在从带噪语音中恢复干净语音。传统方法多采用实值网络估计幅度掩码，而复数网络能原生处理时频表示，但计算开销大，在小模型下效率低。现有混合方法缺乏系统研究。本文针对此问题，提出一种匹配参数的混合实值-复值架构，在保持性能的同时降低计算成本。

## 💡 核心创新

1. 提出实值幅度掩码分支与复值加性校正分支的混合架构
2. 在瓶颈处引入域转换函数耦合两分支
3. 应用于卷积去噪自编码器和卷积循环网络两种主干
4. 在匹配参数下显著减少操作次数，提升可懂度和质量

## 🏗️ 模型架构

输入为带噪语音的短时傅里叶变换（STFT）幅度和复数谱。主干网络采用卷积去噪自编码器（CDAE）或卷积循环网络（CRN）。混合架构包含两个分支：实值分支估计幅度掩码，复值分支估计复数加性校正。两分支在瓶颈处通过域转换函数（如从实值到复数）耦合。输出为增强后的复数谱，经逆STFT得到时域波形。

## 📚 数据集

- 未知（训练和评估数据集未在摘要中说明）

## 📊 实验结果

摘要中未提供具体数值结果，仅提及在四个信噪比（SNR）下平均，混合模型相比对照模型在可懂度和质量上有所提升，同时大幅减少操作次数。具体指标和数据集未给出。

## 🎯 结论与影响

本文提出的混合实值-复值架构在单声道语音增强中有效平衡了性能与计算效率，为小模型场景提供了新思路。未来可探索更复杂的域转换函数和不同主干网络，有望推动低资源设备上的实时语音增强应用。

## ⚠️ 局限与未解决问题

摘要未提供具体数据集和指标，缺乏与SOTA方法的定量对比。未讨论模型参数量、推理延迟等效率细节。未进行消融实验验证各组件贡献。

---

<div class="paper-footer"><span>评分：8.2</span><span>原始：7.2</span><span>+1 重点领域加权</span><a href="/audio-paper-daily/posts/2026-08-14/">← 返回 2026-08-14 速递</a></div>
