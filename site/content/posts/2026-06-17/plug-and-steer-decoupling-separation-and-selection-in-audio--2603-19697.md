---
title: "Plug-and-Steer: Decoupling Separation and Selection in Audio-Visual Target Speaker Extraction"
date: 2026-06-17T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#目标说话人提取"]
summary: "提出Plug-and-Steer方法，通过解耦分离与选择，利用冻结的纯音频骨干和Latent Steering Matrix实现高保真视听目标说话人提取。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#目标说话人提取</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#音频视觉融合</span> <span class="tag-pill tag-pill-soft">#语音分离</span> <span class="tag-pill tag-pill-soft">#解耦方法</span> <span class="tag-pill tag-pill-soft">#Latent Steering Matrix</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2603.19697</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-06-17</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
<div class="meta-row"><span class="meta-key">⭐</span><span class="meta-val focus-badge">本站重点关注领域 · 评分 +1</span></div>
</div>
</div>

<div class="opensource-banner"><div class="oc-headline"><span class="oc-pulse"></span><span class="oc-title">本论文已开源</span><span class="oc-hint">点击下方卡片直达对应资源</span></div><div class="oc-grid"><a class="oc-chip oc-chip-proj" href="https://plugandsteer.github.io" target="_blank" rel="noopener"><span class="oc-icon">🌐</span><span class="oc-text"><span class="oc-label">项目主页</span><span class="oc-sub">plugandsteer.github.io</span></span></a><a class="oc-chip oc-chip-demo" href="https://plugandsteer.github.io" target="_blank" rel="noopener"><span class="oc-icon">🔊</span><span class="oc-text"><span class="oc-label">在线 Demo</span><span class="oc-sub">plugandsteer.github.io</span></span></a></div></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2603.19697" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2603.19697" target="_blank" rel="noopener">📑 PDF</a><a class="rsrc rsrc-proj" href="https://plugandsteer.github.io" target="_blank" rel="noopener">🌐 项目主页</a><a class="rsrc rsrc-demo" href="https://plugandsteer.github.io" target="_blank" rel="noopener">🔊 Demo</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出Plug-and-Steer方法，通过解耦分离与选择，利用冻结的纯音频骨干和Latent Steering Matrix实现高保真视听目标说话人提取。
</div>

## 👥 作者与机构

**Doyeop Kwak** ¹ · Suyeon Lee · Joon Son Chung ✉

**机构**：韩国科学技术院

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合从事视听语音分离/提取的研究者阅读。建议重点看§3的Latent Steering Matrix设计和§4的实验结果，特别是表1-3中不同骨干的保真度对比。可先浏览图1了解整体框架。

## 🌍 研究背景

视听目标说话人提取（AV-TSE）旨在利用视觉线索从混合语音中提取目标说话人。现有方法通常深度融合音视频特征，重新学习整个分离过程，但野外数据集的噪声特性导致保真度受限。之前SOTA如AVSep、AV-Conformer等均采用端到端融合方式。本文旨在解耦分离与选择，利用预训练纯音频分离模型的声学先验，仅通过视觉进行目标选择，避免重新学习分离。

## 💡 核心创新

1. 提出Latent Steering Matrix (LSM)实现线性目标选择
2. 解耦分离与选择，冻结纯音频骨干
3. 跨四种骨干架构验证通用性
4. 保持与原始骨干相当的感知质量

## 🏗️ 模型架构

输入为混合音频和对应目标说话人的视频帧。音频经预训练纯音频分离骨干（如SepFormer、Conv-TasNet等）编码为潜在特征；视频帧通过视觉编码器（如ResNet）提取视觉嵌入。关键模块Latent Steering Matrix (LSM)是一个线性变换，将视觉嵌入映射为潜在特征的通道重排权重，从而将目标说话人锚定到指定输出通道。输出为分离后的目标说话人音频。骨干参数冻结，仅LSM可训练。

## 📚 数据集

- VoxCeleb2（训练/评估，多说话人视频）
- LRS3（评估，野外场景）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| SI-SDRi (dB) | VoxCeleb2 test | AV-Conformer 12.5 | **Plug-and-Steer (SepFormer) 13.8** | +1.3 dB |
| PESQ | VoxCeleb2 test | AV-Conformer 3.12 | **Plug-and-Steer (SepFormer) 3.45** | +0.33 |

在VoxCeleb2上，Plug-and-Steer在SepFormer骨干下SI-SDRi达13.8 dB，PESQ 3.45，优于AV-Conformer。跨四种骨干（SepFormer、Conv-TasNet、DPRNN、DCCRN）均保持与原始骨干相近的感知质量，且参数量仅增加约0.1M。在LRS3上同样表现稳健。

## 🎯 结论与影响

本文证明解耦分离与选择在AV-TSE中有效，通过冻结纯音频骨干和轻量LSM，可保留高保真声学先验，避免重新学习分离。该方法为未来视听融合提供新范式，有望降低对大规模视听配对数据的依赖，并促进在真实场景中的部署。

## ⚠️ 局限与未解决问题

仅验证了四种骨干，未探索更先进的Mamba或Diffusion模型；LSM为线性变换，可能无法处理复杂视觉线索（如多人遮挡）；未报告推理延迟或计算开销；实验仅在VoxCeleb2和LRS3上，缺乏对噪声/混响环境的泛化测试。

## 🔗 开源资源

- **项目主页**：<https://plugandsteer.github.io>
- **Demo / 试听**：<https://plugandsteer.github.io>

---

<div class="paper-footer"><span>评分：9.2</span><span>原始：8.2</span><span>+1 重点领域加权</span><a href="/audio-paper-daily/posts/2026-06-17/">← 返回 2026-06-17 速递</a></div>
