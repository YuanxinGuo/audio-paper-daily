---
title: "CIS-BWE: Chaos-Informed Speech Bandwidth Extension"
date: 2026-05-18T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#语音带宽扩展"]
summary: "提出NDSI-BWE框架，利用七个基于非线性动力学的判别器引导复数ConformerNeXt生成器，实现语音带宽扩展，参数减少8倍，在多个指标上达到新SOTA。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#语音带宽扩展</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#语音增强</span> <span class="tag-pill tag-pill-soft">#生成对抗网络</span> <span class="tag-pill tag-pill-soft">#混沌理论</span> <span class="tag-pill tag-pill-soft">#Conformer</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2507.15970</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-05-18</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
<div class="meta-row"><span class="meta-key">⭐</span><span class="meta-val focus-badge">本站重点关注领域 · 评分 +1</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2507.15970" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2507.15970" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出NDSI-BWE框架，利用七个基于非线性动力学的判别器引导复数ConformerNeXt生成器，实现语音带宽扩展，参数减少8倍，在多个指标上达到新SOTA。
</div>

## 👥 作者与机构

**Tarikul Islam Tamiti** ¹ · Tonmoy Das · Nursadul Mamun · Anomadarshi Barua

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合语音带宽扩展、生成对抗网络、非线性信号处理方向的研究者。建议重点阅读§3（判别器设计）和§4（生成器架构），以及表1-3的实验结果。可先看§3.2的MRLD和§3.3的MS-RD。

## 🌍 研究背景

语音带宽扩展旨在恢复因带宽限制丢失的高频成分，对通信和高保真音频应用至关重要。现有方法多基于生成对抗网络，但判别器设计通常仅关注频谱或时域特征，缺乏对语音混沌动力学特性的建模。本文提出利用非线性动力系统（如Lyapunov指数、递归图、去趋势波动分析）设计多个判别器，以捕捉语音信号中的确定性混沌、自相似递归、长程相关等复杂动态行为，从而提升高频恢复质量。

## 💡 核心创新

1. 提出七个基于非线性动力学的判别器，分别捕捉混沌、递归、分形、相空间等特性
2. 采用复数ConformerNeXt生成器，结合Conformer全局建模和ConvNeXt局部建模
3. 引入双流Lattice-Net同时优化幅度和相位
4. 深度可分离卷积实现八倍参数缩减
5. 在六个客观指标和主观听感上达到新SOTA

## 🏗️ 模型架构

输入为低带宽语音的幅度谱和相位谱。生成器采用复数ConformerNeXt架构，包含Conformer模块（全局依赖建模）和ConvNeXt块（局部时序建模），并通过双流Lattice-Net分别处理幅度和相位，最后输出全带宽语音。判别器组包含七个判别器：MRLD（Lyapunov指数）、MS-RD（递归图）、MSDFA（去趋势波动分析）、MR-PPD（Poincaré图）、MPD（周期）、MRAD（幅度）、MRPD（相位），每个判别器内部使用深度可分离卷积减少参数量。

## 📚 数据集

- VCTK（训练/评估，包含109位说话人）
- TIMIT（评估，包含630位说话人）
- LibriTTS（评估，包含2456位说话人）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| PESQ | VCTK (16 kHz→8 kHz) | NuWave 2.0 (3.85) | **4.12** | +0.27 |
| STOI | VCTK (16 kHz→8 kHz) | NuWave 2.0 (0.95) | **0.97** | +0.02 |
| MCD | VCTK (16 kHz→8 kHz) | NuWave 2.0 (4.21) | **3.85** | -0.36 |
| LSR | VCTK (16 kHz→8 kHz) | NuWave 2.0 (0.82) | **0.89** | +0.07 |

在VCTK、TIMIT、LibriTTS数据集上，NDSI-BWE在PESQ、STOI、MCD、LSR等六个客观指标上均优于NuWave 2.0、HiFi-GAN等基线。主观听感测试（5位评审员）也表明NDSI-BWE生成的高频成分更自然。消融实验验证了每个判别器的贡献，其中MRLD和MS-RD最为关键。参数减少8倍的同时性能提升。

## 🎯 结论与影响

NDSI-BWE通过引入非线性动力学判别器，显著提升了语音带宽扩展的质量，在多个指标上达到新SOTA。该工作为语音增强中的判别器设计提供了新思路，即利用混沌理论等非线性分析工具。对工业应用而言，八倍参数缩减使其更适合资源受限设备。

## ⚠️ 局限与未解决问题

作者未讨论模型推理延迟和计算复杂度（除参数量外）。判别器设计依赖多个非线性特征提取，可能增加训练不稳定性。仅在16kHz→8kHz场景测试，未评估其他带宽条件。主观测试仅5人，样本量较小。

---

<div class="paper-footer"><span>评分：8.8</span><span>原始：7.8</span><span>+1 重点领域加权</span><a href="/audio-paper-daily/posts/2026-05-18/">← 返回 2026-05-18 速递</a></div>
