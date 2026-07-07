---
title: "AViS-Mamba: Adaptive Visual Steering of Audio State-Space Dynamics for Violence Detection"
date: 2026-07-07T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#暴力检测"]
summary: "提出AViS-Mamba，用视觉流自适应调控音频编码器的状态空间动态，在暴力检测任务上达到SOTA。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#暴力检测</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#音视频融合</span> <span class="tag-pill tag-pill-soft">#Mamba</span> <span class="tag-pill tag-pill-soft">#自适应调制</span> <span class="tag-pill tag-pill-soft">#对比学习</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2604.03329</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-07-07</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2604.03329" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2604.03329" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出AViS-Mamba，用视觉流自适应调控音频编码器的状态空间动态，在暴力检测任务上达到SOTA。
</div>

## 👥 作者与机构

**Damith Chamalke Senadeera** ¹ · Dimitrios Kollias · Gregory Slabaugh

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合音视频融合、暴力检测方向的研究者。建议重点阅读§3模型架构和§4.3消融实验，了解视觉调制向量和路由门的设计。可对比现有融合方法（如后期融合、注意力融合）的差异。

## 🌍 研究背景

暴力检测中，视觉信息可能因遮挡、距离等受限，音频可提供补充证据。但音频可能缺失、被配音或受环境噪声干扰，因此关键不是是否融合音频，而是如何根据视觉场景自适应调整对音频的依赖。现有方法多采用固定融合策略，缺乏对音频可靠性的动态评估。本文提出视觉引导音频编码器状态空间动态的架构，以自适应调节音频利用程度。

## 💡 核心创新

1. 视觉调制向量条件化音频编码器内部时序算子
2. 路由门控机制动态调节视觉干预强度
3. 自适应AV-InfoNCE对比损失平衡音视频对齐方向
4. 层间分析揭示网络深度选择性调控音频流

## 🏗️ 模型架构

输入为视频帧和对应音频。视觉流使用预训练模型提取紧凑视觉表示；音频流采用Mamba编码器，每层接收视觉调制向量和路由门控信号。调制向量通过线性变换生成，条件化音频编码器的状态空间模型参数；路由门控输出0-1标量，控制视觉调制强度。最终音视频特征经对比学习对齐后用于分类。

## 📚 数据集

- NTU-CCTV（训练/评估，音频有效子集）
- DVD（训练/评估）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| Accuracy | NTU-CCTV (audio-valid) | AViS (88.59%) | **88.59%** | 持平（SOTA） |
| Accuracy | DVD | AViS (75.74%) | **75.74%** | 持平（SOTA） |

在NTU-CCTV和DVD基准上达到SOTA准确率88.59%和75.74%。消融实验表明自适应视觉调制优于固定路由，且在音频退化或缺失条件下性能提升显著。层间分析显示模型在网络深层对音频调控更强。

## 🎯 结论与影响

AViS-Mamba通过视觉自适应调控音频编码器动态，有效解决了暴力检测中音频可靠性变化的问题。该方法为音视频融合提供了新范式，即视觉主导音频处理流程，而非后期融合。对工业监控场景中多模态融合系统的设计具有参考价值。

## ⚠️ 局限与未解决问题

仅在两个数据集上评估，泛化性待验证；未报告推理延迟和参数量；缺少与近期大模型（如VideoMAE）的对比；音频缺失条件下的性能提升幅度未给出具体数值。

---

<div class="paper-footer"><span>评分：7.8</span><span>原始：7.8</span><a href="/audio-paper-daily/posts/2026-07-07/">← 返回 2026-07-07 速递</a></div>
