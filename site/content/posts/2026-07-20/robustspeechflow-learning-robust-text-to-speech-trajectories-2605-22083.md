---
title: "RobustSpeechFlow: Learning Robust Text-to-Speech Trajectories via Augmentation-based Contrastive Flow Matching"
date: 2026-07-20T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#语音合成"]
summary: "通过扩展对比流匹配与长度保持的重复/跳过潜在增强，提升TTS对齐鲁棒性，降低字错误率。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero">
<div class="hero-score">
<div class="score-num">7.6</div>
<div class="score-stars">★★★★☆</div>
<div class="score-tier">前25%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#语音合成</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#文本转语音</span> <span class="tag-pill tag-pill-soft">#流匹配</span> <span class="tag-pill tag-pill-soft">#对比学习</span> <span class="tag-pill tag-pill-soft">#鲁棒性</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2605.22083</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-07-20</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner"><div class="oc-headline"><span class="oc-pulse"></span><span class="oc-title">本论文已开源</span><span class="oc-hint">点击下方卡片直达对应资源</span></div><div class="oc-grid"><a class="oc-chip oc-chip-demo" href="https://robustspeechflow.github.io/" target="_blank" rel="noopener"><span class="oc-icon">🔊</span><span class="oc-text"><span class="oc-label">在线 Demo</span><span class="oc-sub">robustspeechflow.github.io/</span></span></a></div></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2605.22083" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2605.22083" target="_blank" rel="noopener">📑 PDF</a><a class="rsrc rsrc-demo" href="https://robustspeechflow.github.io/" target="_blank" rel="noopener">🔊 Demo</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>通过扩展对比流匹配与长度保持的重复/跳过潜在增强，提升TTS对齐鲁棒性，降低字错误率。
</div>

## 👥 作者与机构

**Jinhyeok Yang** ¹ · Hyeongju Kim · Yechan Yu · Joon Byun · Frederik Bous · Juheon Lee

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合TTS研究者，重点看§3的增强策略和§4的WER/CER结果。可先读§3.2了解对比流匹配扩展，再对比表1的消融。

## 🌍 研究背景

流匹配TTS在零样本语音克隆中表现优异，但对齐不完美导致内容错误（如跳词、重复）。现有方法依赖外部对齐器或偏好数据，成本高。本文旨在通过训练策略直接惩罚这些失败模式，无需额外模块。

## 💡 核心创新

1. 长度保持的重复/跳过潜在增强
2. 扩展对比流匹配到TTS对齐鲁棒性
3. 无需外部对齐器或偏好数据
4. 即插即用于现有流匹配TTS管线

## 🏗️ 模型架构

基于流匹配TTS框架，编码器将文本映射到隐空间，通过对比流匹配训练，其中正样本对为原始与增强后的隐轨迹，负样本对为不同文本的轨迹。增强模块对隐轨迹施加长度保持的重复或跳过操作，模拟对齐错误。解码器从隐轨迹生成波形。参数量0.06B。

## 📚 数据集

- Seed-TTS-eval（评估，WER测试）
- ZERO500（评估，自建基准，含多样说话人和韵律条件）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| WER | Seed-TTS-eval | 基线 1.44 | **1.38** | -0.06 |
| CER | ZERO500 (English, NFE=24) | 0.48% | **0.35%** | -0.13% |
| CER | ZERO500 (Korean, NFE=24) | 0.81% | **0.57%** | -0.24% |

在Seed-TTS-eval上WER从1.44降至1.38；在自建ZERO500基准上，英语CER从0.48%降至0.35%，韩语CER从0.81%降至0.57%。方法在低NFE下仍保持优势，且无需外部对齐器。

## 🎯 结论与影响

本文通过对比流匹配与潜在增强，有效提升了TTS对齐鲁棒性，降低了内容错误。该方法轻量且即插即用，有望成为流匹配TTS的标准训练策略，对工业部署中的稳定性有实际意义。

## ⚠️ 局限与未解决问题

仅验证了0.06B小模型，更大模型效果未知；增强策略仅模拟重复和跳过，未覆盖其他错误类型；ZERO500为自建基准，泛化性需更多公开数据集验证。

## 🔗 开源资源

- **Demo / 试听**：<https://robustspeechflow.github.io/>

---

<div class="paper-footer"><span>评分：7.6</span><span>原始：7.6</span><a href="/audio-paper-daily/posts/2026-07-20/">← 返回 2026-07-20 速递</a></div>
