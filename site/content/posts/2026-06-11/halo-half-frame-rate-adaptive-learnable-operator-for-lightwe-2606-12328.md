---
title: "HALO: Half-Frame-Rate Adaptive Learnable Operator for Lightweight STFT-Based Speech Enhancement"
date: 2026-06-11T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#语音增强"]
summary: "提出HALO模块，通过减半内部帧率降低STFT语音增强模型的计算冗余，在轻量级模型上实现性能提升。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero hero-focus">
<div class="hero-score">
<div class="score-num">8.5</div>
<div class="score-stars">★★★★☆</div>
<div class="score-tier">前25%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#语音增强</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#轻量化模型</span> <span class="tag-pill tag-pill-soft">#STFT</span> <span class="tag-pill tag-pill-soft">#帧率降低</span> <span class="tag-pill tag-pill-soft">#动态卷积</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2606.12328</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-06-11</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
<div class="meta-row"><span class="meta-key">⭐</span><span class="meta-val focus-badge">本站重点关注领域 · 评分 +1</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2606.12328" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2606.12328" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出HALO模块，通过减半内部帧率降低STFT语音增强模型的计算冗余，在轻量级模型上实现性能提升。
</div>

## 👥 作者与机构

**Jiadong Zhao** ¹ · Dahan Wang · Yu Sun · Leyan Yang · Xiaobin Rong · Shiruo Sun · Yuxiang Hu · Jing Lu

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合从事轻量化语音增强研究的读者。建议重点阅读§3的HALO模块设计和§4的实验结果，特别是表1中不同模型在DNS3上的对比。可先看§3.2的帧率减半与恢复机制。

## 🌍 研究背景

STFT语音增强通常使用重叠分析帧，重叠虽保证处理稳定性，但导致相邻帧高度相关，在轻量级模型中造成计算冗余。现有方法多关注网络结构改进，鲜有从帧率角度减少冗余。本文提出HALO模块，在不改变STFT流程的前提下，通过自适应帧率减半降低骨干网络计算量，释放预算用于通道扩展，从而提升性能。

## 💡 核心创新

1. 提出半帧率自适应可学习算子（HALO），作为即插即用模块
2. 采用轻量动态卷积实现帧率减半与恢复
3. 在不增加算法延迟的前提下减少骨干网络计算量
4. 将节省的计算预算用于通道扩展，提升模型容量

## 🏗️ 模型架构

输入STFT幅度谱，HALO模块先通过自适应帧率减半（轻量动态卷积）将帧率降低一半，送入轻量级骨干网络（如CRN、DCCRN等），再通过帧率恢复模块（轻量动态卷积）重建全帧率频谱，最终输出增强后的STFT幅度谱。整个模块保持因果性，不改变STFT处理流程。

## 📚 数据集

- DNS3（训练与评估，包含合成和真实噪声）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| PESQ | DNS3 | CRN baseline 3.12 | **CRN+HALO 3.21** | +0.09 |
| PESQ | DNS3 | DCCRN baseline 3.18 | **DCCRN+HALO 3.27** | +0.09 |
| PESQ | DNS3 | CRN-8 baseline 3.04 | **CRN-8+HALO 3.14** | +0.10 |

在DNS3数据集上，HALO模块在多种轻量级模型（CRN、DCCRN、CRN-8）上均取得一致的PESQ提升（约0.09-0.10），且计算复杂度与基线相当。消融实验验证了帧率减半和通道扩展各自贡献，并展示了HALO在不同帧移设置下的鲁棒性。

## 🎯 结论与影响

HALO模块通过减半内部帧率有效降低STFT语音增强模型的计算冗余，在轻量级模型上实现性能提升且不增加延迟。该思路为轻量化语音增强提供了新方向，可推广至其他基于STFT的音频处理任务，对工业部署具有实际价值。

## ⚠️ 局限与未解决问题

仅在DNS3数据集上评估，缺乏跨数据集泛化验证；未报告推理延迟或参数量具体数值；未与更先进的轻量化方法（如Mamba、Transformer）对比；帧率减半可能对非平稳噪声场景的细节恢复有影响。

---

<div class="paper-footer"><span>评分：8.5</span><span>原始：7.5</span><span>+1 重点领域加权</span><a href="/audio-paper-daily/posts/2026-06-11/">← 返回 2026-06-11 速递</a></div>
