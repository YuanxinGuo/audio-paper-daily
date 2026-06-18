---
title: "Adaptive Speech-to-Spike Encoding for Spiking Neural Networks"
date: 2026-06-18T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#语音识别"]
summary: "提出一种可学习的残差语音到脉冲编码器，与R-LIF骨干网络联合训练，在GSC-v2上以35k参数达到89.8%准确率，并对比了DFA与BPTT的性能权衡。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero">
<div class="hero-score">
<div class="score-num">7.2</div>
<div class="score-stars">★★★★☆</div>
<div class="score-tier">前25%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#语音识别</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#脉冲神经网络</span> <span class="tag-pill tag-pill-soft">#语音编码</span> <span class="tag-pill tag-pill-soft">#神经形态计算</span> <span class="tag-pill tag-pill-soft">#语音指令识别</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2606.19039</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-06-18</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2606.19039" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2606.19039" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出一种可学习的残差语音到脉冲编码器，与R-LIF骨干网络联合训练，在GSC-v2上以35k参数达到89.8%准确率，并对比了DFA与BPTT的性能权衡。
</div>

## 👥 作者与机构

**Taharim Rahman Anon** ¹ · Jakaria Islam Emon

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合从事神经形态计算、低功耗语音处理的读者。建议重点阅读§3的编码器设计和§4.2的线性探针分析，可跳过§4.3的DFA对比。

## 🌍 研究背景

传统语音处理依赖连续信号，而脉冲神经网络（SNN）需要离散脉冲输入。现有系统多采用固定编码器（如LIF编码），导致输入表示无法适应任务，限制了SNN性能。本文旨在设计一种可学习的语音到脉冲编码器，与SNN骨干联合优化，以提升分类精度和参数效率。

## 💡 核心创新

1. 提出可学习的残差语音到脉冲编码器
2. 编码器与R-LIF骨干端到端联合训练
3. 线性探针分析揭示编码器学习任务对齐表示
4. 对比DFA与BPTT在神经形态音频中的性能权衡

## 🏗️ 模型架构

输入为语音波形，首先通过可学习的残差编码器（包含卷积层和残差连接）将连续信号转换为脉冲序列，然后送入Recurrent Leaky Integrate-and-Fire (R-LIF) 骨干网络进行时序处理，最后通过全连接层输出分类结果。编码器参数量仅35k，整体模型轻量。

## 📚 数据集

- Google Speech Commands v2 (GSC-v2)（训练与评估，35类语音指令）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| Accuracy | GSC-v2 | Prior SNN baselines (e.g., 94.0% with larger models) | **94.97%** | +0.97% |
| Accuracy (35k params) | GSC-v2 | Prior baselines with ~350k params | **89.8%** | 匹配或超越 |
| Accuracy (DFA) | GSC-v2 | BPTT (94.97%) | **91.5%** | -3.47% |

在GSC-v2上，完整模型（参数量未明确）达到94.97%准确率，超越先前SNN基线。紧凑型35k参数版本达到89.8%，与需十倍参数量的基线相当。DFA训练达到91.5%，展示了生物启发学习规则在精度上的权衡。线性探针实验表明编码器学习任务对齐表示而非信号重建。

## 🎯 结论与影响

本文证明可学习的语音到脉冲编码器能显著提升SNN在语音指令识别上的性能，且参数高效。该工作为神经形态音频处理提供了新范式，有望推动低功耗语音唤醒和边缘设备应用。

## ⚠️ 局限与未解决问题

仅在单一数据集GSC-v2上验证，未在噪声环境或更大词汇量任务上测试。未报告推理延迟或能耗。DFA对比仅针对准确率，未分析收敛速度或稳定性。编码器设计未与多种SNN骨干（如Spiking ResNet）结合。

---

<div class="paper-footer"><span>评分：7.2</span><span>原始：7.2</span><a href="/audio-paper-daily/posts/2026-06-18/">← 返回 2026-06-18 速递</a></div>
