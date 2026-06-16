---
title: "SSNAPS: Audio-Visual Separation of Speech and Background Noise with Diffusion Inverse Sampling"
date: 2026-06-16T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#语音分离"]
summary: "提出SSNAPS，利用扩散先验和逆采样实现无监督视听语音分离与增强，在WER上超越有监督基线。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero hero-focus">
<div class="hero-score">
<div class="score-num">9.5</div>
<div class="score-stars">★★★★★</div>
<div class="score-tier">前25%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#语音分离</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#语音增强</span> <span class="tag-pill tag-pill-soft">#目标说话人提取</span> <span class="tag-pill tag-pill-soft">#扩散模型</span> <span class="tag-pill tag-pill-soft">#视听融合</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2602.01394</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-06-16</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
<div class="meta-row"><span class="meta-key">⭐</span><span class="meta-val focus-badge">本站重点关注领域 · 评分 +1</span></div>
</div>
</div>

<div class="opensource-banner"><div class="oc-headline"><span class="oc-pulse"></span><span class="oc-title">本论文已开源</span><span class="oc-hint">点击下方卡片直达对应资源</span></div><div class="oc-grid"><a class="oc-chip oc-chip-proj" href="https://ssnaps2026.github.io/ssnaps2026/" target="_blank" rel="noopener"><span class="oc-icon">🌐</span><span class="oc-text"><span class="oc-label">项目主页</span><span class="oc-sub">ssnaps2026.github.io/ssnaps2026/</span></span></a><a class="oc-chip oc-chip-demo" href="https://ssnaps2026.github.io/ssnaps2026/" target="_blank" rel="noopener"><span class="oc-icon">🔊</span><span class="oc-text"><span class="oc-label">在线 Demo</span><span class="oc-sub">ssnaps2026.github.io/ssnaps2026/</span></span></a></div></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2602.01394" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2602.01394" target="_blank" rel="noopener">📑 PDF</a><a class="rsrc rsrc-proj" href="https://ssnaps2026.github.io/ssnaps2026/" target="_blank" rel="noopener">🌐 项目主页</a><a class="rsrc rsrc-demo" href="https://ssnaps2026.github.io/ssnaps2026/" target="_blank" rel="noopener">🔊 Demo</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出SSNAPS，利用扩散先验和逆采样实现无监督视听语音分离与增强，在WER上超越有监督基线。
</div>

## 👥 作者与机构

**Yochai Yemini** ¹ · Yoav Ellinson · Rami Ben-Ari · Sharon Gannot · Ethan Fetaya

**机构**：巴伊兰大学 · IBM Research

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合语音分离、扩散模型方向的研究者。建议重点阅读§3的逆采样公式和§4的视听融合策略，以及表1的WER对比。可先看Demo页面了解效果。

## 🌍 研究背景

真实环境中的语音分离与增强面临多说话人、非平稳噪声等挑战。现有监督方法依赖配对数据，泛化性受限；无监督方法性能不足。扩散模型在生成任务中表现优异，但如何将其用于分离多个未知源仍是难题。本文提出利用多个扩散先验联合建模语音和噪声，通过逆采样实现无监督分离。

## 💡 核心创新

1. 提出多源扩散逆采样框架，联合建模语音与噪声先验
2. 改进逆采样算法适配多源分离场景
3. 支持1-3说话人及屏外说话人分离
4. 分离的噪声分量可用于声学场景检测

## 🏗️ 模型架构

输入为混合音频和对应视频帧（可选）。采用多个预训练扩散模型分别作为语音和噪声的先验，每个源对应一个扩散模型。通过逆采样过程从混合信号中迭代去噪，恢复各源。逆采样器基于DPS（Diffusion Posterior Sampling）改进，引入多源约束。输出为分离的语音和噪声分量。

## 📚 数据集

- VoxCeleb2（训练视频编码器）
- LibriSpeech（训练语音扩散模型）
- ESC-50（训练噪声扩散模型）
- 自建混合数据集（1/2/3说话人+噪声，评估）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| WER (%) | 1-speaker + noise | AVHuBERT 18.2 | **12.1** | -6.1 |
| WER (%) | 2-speaker + noise | AVHuBERT 35.4 | **22.3** | -13.1 |
| WER (%) | 3-speaker + noise | AVHuBERT 52.1 | **33.7** | -18.4 |

在1/2/3说话人加噪声混合上，SSNAPS的WER分别比AVHuBERT低6.1%、13.1%、18.4%，且完全无监督。在屏外说话人场景中，SSNAPS也优于基线。噪声分量可用于声学场景检测，准确率与专用分类器相当。

## 🎯 结论与影响

SSNAPS证明了无监督扩散逆采样在语音分离中的潜力，在WER上显著超越有监督方法。该方法无需配对数据，可灵活扩展至任意数量源。对工业落地而言，无监督特性降低了数据采集成本，但推理速度可能成为瓶颈。

## ⚠️ 局限与未解决问题

依赖多个扩散模型，推理计算量大；未报告推理时间或参数量；仅在自建混合数据集上评估，缺乏标准基准（如WSJ0-2mix）对比；未消融视频模态贡献；噪声扩散模型仅用ESC-50，泛化性待验证。

## 🔗 开源资源

- **项目主页**：<https://ssnaps2026.github.io/ssnaps2026/>
- **Demo / 试听**：<https://ssnaps2026.github.io/ssnaps2026/>

---

<div class="paper-footer"><span>评分：9.5</span><span>原始：8.5</span><span>+1 重点领域加权</span><a href="/audio-paper-daily/posts/2026-06-16/">← 返回 2026-06-16 速递</a></div>
