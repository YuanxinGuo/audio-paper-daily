---
title: "A Fast Solver for Interpolating Stochastic Differential Equation Diffusion Models for Speech Restoration"
date: 2026-06-24T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#语音增强"]
summary: "提出一种针对插值随机微分方程扩散模型的快速求解器，在语音修复任务中仅需10步网络评估即可达到高质量。"
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
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#扩散模型</span> <span class="tag-pill tag-pill-soft">#快速采样</span> <span class="tag-pill tag-pill-soft">#随机微分方程</span> <span class="tag-pill tag-pill-soft">#语音修复</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2603.09508</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-06-24</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
<div class="meta-row"><span class="meta-key">⭐</span><span class="meta-val focus-badge">本站重点关注领域 · 评分 +1</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2603.09508" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2603.09508" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出一种针对插值随机微分方程扩散模型的快速求解器，在语音修复任务中仅需10步网络评估即可达到高质量。
</div>

## 👥 作者与机构

**Bunlong Lay** ¹ · Timo Gerkmann ✉

**机构**：汉堡大学

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合对扩散模型加速采样感兴趣的语音增强研究者。建议重点阅读第3节iSDE形式化定义和第4节求解器推导，以及表1中的实验结果。可复现其代码以验证加速效果。

## 🌍 研究背景

扩散概率模型（DPMs）在无条件图像生成中表现优异，SGMSE+作为条件扩散模型在语音增强中取得SOTA。然而，DPMs的反向过程需要大量神经网络评估，现有快速采样器（如DDIM）因扩散过程差异无法直接应用于SGMSE+。本文旨在统一SGMSE+的扩散过程为插值SDE（iSDE），并设计专用快速求解器。

## 💡 核心创新

1. 提出iSDE形式化框架统一SGMSE+类模型
2. 设计iSDE专用快速求解器，仅需10步评估
3. 在多个语音修复任务上验证加速效果

## 🏗️ 模型架构

输入为带噪语音观测，通过iSDE前向过程将目标语音插值到观测噪声上。反向过程使用提出的iSDE求解器，基于解析解和数值近似，以少量步数（如10步）迭代去噪。主干网络沿用SGMSE+的U-Net架构，参数量未提及。输出为增强后的干净语音。

## 📚 数据集

- DNS-Challenge（训练/评估，含噪声和干净语音）
- VoiceBank+DEMAND（训练/评估，用于语音增强）
- WSJ0-2mix（评估，用于语音分离）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| PESQ | VoiceBank+DEMAND | SGMSE+ (100步) 3.12 | **SGMSE+ (10步) 3.08** | -0.04 |
| SI-SDR (dB) | WSJ0-2mix | SGMSE+ (100步) 12.5 | **SGMSE+ (10步) 12.3** | -0.2 dB |

在语音增强任务（VoiceBank+DEMAND）上，10步求解器PESQ仅比100步基线低0.04，几乎无损。在语音分离（WSJ0-2mix）上，10步SI-SDR下降0.2 dB。消融实验表明求解器对步数鲁棒，且计算量减少90%。

## 🎯 结论与影响

本文提出的iSDE求解器成功将快速采样技术扩展到插值扩散模型，在语音修复任务中以10步评估达到接近100步的性能。该工作为扩散模型在实时语音增强中的部署提供了可能，并启发了其他插值扩散模型的加速研究。

## ⚠️ 局限与未解决问题

实验仅在SGMSE+上验证，未测试其他iSDE模型；未报告推理延迟具体数值；语音分离任务性能下降略大；未在更复杂噪声场景（如混响）下评估。

---

<div class="paper-footer"><span>评分：8.8</span><span>原始：7.8</span><span>+1 重点领域加权</span><a href="/audio-paper-daily/posts/2026-06-24/">← 返回 2026-06-24 速递</a></div>
