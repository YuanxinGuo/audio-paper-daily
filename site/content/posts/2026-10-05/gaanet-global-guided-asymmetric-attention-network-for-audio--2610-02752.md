---
title: "GAANet: Global-guided Asymmetric Attention Network for Audio-Visual Speech Separation"
date: 2026-10-05T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#语音分离"]
summary: "提出非对称多尺度融合与全局引导注意力，用于音视频语音分离，LRS2 上达 16.5 dB SI-SNRi，仅 3.3M 参数。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#语音分离</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#语音分离</span> <span class="tag-pill tag-pill-soft">#多模态</span> <span class="tag-pill tag-pill-soft">#注意力机制</span> <span class="tag-pill tag-pill-soft">#轻量化</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2610.02752</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-10-05</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
<div class="meta-row"><span class="meta-key">⭐</span><span class="meta-val focus-badge">本站重点关注领域 · 评分 +1</span></div>
</div>
</div>

<div class="opensource-banner"><div class="oc-headline"><span class="oc-pulse"></span><span class="oc-title">本论文已开源</span><span class="oc-hint">点击下方卡片直达对应资源</span></div><div class="oc-grid"><a class="oc-chip oc-chip-code" href="https://github.com/redizzy/GAANet" target="_blank" rel="noopener"><span class="oc-icon">💻</span><span class="oc-text"><span class="oc-label">代码仓库</span><span class="oc-sub">redizzy/GAANet</span></span></a></div></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2610.02752" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2610.02752" target="_blank" rel="noopener">📑 PDF</a><a class="rsrc rsrc-code" href="https://github.com/redizzy/GAANet" target="_blank" rel="noopener">💻 代码</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出非对称多尺度融合与全局引导注意力，用于音视频语音分离，LRS2 上达 16.5 dB SI-SNRi，仅 3.3M 参数。
</div>

## 👥 作者与机构

**Zhiyuan Zhang** ¹ · Jingyuan Xu · Yiming Tang · Liu Liu · Dan Guo

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合做音视频多模态分离、轻量化模型的研究者阅读。建议重点看 §3 的非对称多尺度融合框架与全局 token 注意力设计，以及表 1/表 2 与 SOTA 的对比和参数量/MACs 效率分析。若关注工程落地，可先看效率对比表再决定是否通读。

## 🌍 研究背景

音视频语音分离近年以 AV-ConvTasNet、AV-DPRNN、AV-SEPFormer 等为代表，多依赖对称的多尺度或双路结构做跨模态融合。这些方法通常对音频与视觉流采用相同的时序下采样与融合方式，忽略了两种模态最优时间分辨率不同，也未充分利用全局语义信息，导致融合效率与分离性能受限。本文针对这两点，提出非对称多尺度融合与全局引导注意力，在保持轻量的同时提升分离质量。

## 💡 核心创新

1. 非对称多尺度融合框架，音视频各在最优时间分辨率交互，免对称下采样
2. 全局引导注意力，将各模态压缩为时序长度为 1 的全局 token
3. 全局 token 同时引导模态内与跨模态的多尺度融合
4. 轻量设计，仅 3.3M 参数、19.8G MACs 达 SOTA

## 🏗️ 模型架构

输入为混合语音波形与对应说话人视频帧。音频流与视觉流分别经各自编码器提取特征后，进入非对称多尺度融合框架：两路在不同时间分辨率上独立下采样并交互，避免对称时序下采样带来的信息损失。全局引导注意力模块将每个模态特征沿时间维压缩为长度为 1 的全局 token，作为高层语义线索，指导各尺度上的模态内与跨模态融合。融合特征最终经解码器重建目标说话人语音。整体仅 3.3M 参数、19.8G MACs。

## 📚 数据集

- LRS2（训练与评估，音视频语音分离基准）
- VoxCeleb2（训练与评估，大规模说话人视频）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| SI-SNRi | LRS2 | 现有 SOTA（摘要未给具体值） | **16.5 dB** | SOTA |
| SI-SNRi | VoxCeleb2 | 现有 SOTA（摘要未给具体值） | **14.0 dB** | SOTA |

摘要报告 GAANet 在 LRS2 上达 16.5 dB SI-SNRi、VoxCeleb2 上达 14.0 dB，均称达到 SOTA，同时仅 3.3M 参数与 19.8G MACs，体现轻量高效。摘要未给出具体 baseline 数值、消融实验、推理延迟或跨数据集泛化结果，需查阅正文确认非对称设计与全局引导各自的贡献。

## 🎯 结论与影响

最强结论是：非对称时序建模加全局引导可在极轻量参数下取得音视频语音分离 SOTA。这提示后续多模态融合研究不必强求对称结构，按模态最优分辨率交互更高效。对工业落地而言，3.3M 参数与 19.8G MACs 使其适合端侧或实时音视频分离场景。

## ⚠️ 局限与未解决问题

摘要仅给两个数据集的 SI-SNRi，未列 baseline 具体值、消融、推理延迟与内存占用；非对称融合与全局 token 的各自增益不明确。LRS2/VoxCeleb2 以近景人脸为主，遮挡、远场与噪声场景泛化未知。视觉流依赖高质量人脸检测，实际部署鲁棒性待验证。

## 🔗 开源资源

- **代码**：<https://github.com/redizzy/GAANet>

---

<div class="paper-footer"><span>评分：8.8</span><span>原始：7.8</span><span>+1 重点领域加权</span><a href="/audio-paper-daily/posts/2026-10-05/">← 返回 2026-10-05 速递</a></div>
