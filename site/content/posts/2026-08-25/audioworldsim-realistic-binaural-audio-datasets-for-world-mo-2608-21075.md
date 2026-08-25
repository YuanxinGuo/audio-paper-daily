---
title: "AudioWorldSim: Realistic Binaural Audio Datasets For World Models"
date: 2026-08-25T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#双耳音频"]
summary: "AudioWorldSim 是一个基于 SoundSpaces 2.0 的开源平台，用于自动生成真实双耳音频数据集，支持世界模型研究。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero hero-focus">
<div class="hero-score">
<div class="score-num">7.8</div>
<div class="score-stars">★★★★☆</div>
<div class="score-tier">前50%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#双耳音频</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#双耳音频</span> <span class="tag-pill tag-pill-soft">#世界模型</span> <span class="tag-pill tag-pill-soft">#声学模拟</span> <span class="tag-pill tag-pill-soft">#数据生成</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2608.21075</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-08-25</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
<div class="meta-row"><span class="meta-key">⭐</span><span class="meta-val focus-badge">本站重点关注领域 · 评分 +1</span></div>
</div>
</div>

<div class="opensource-banner"><div class="oc-headline"><span class="oc-pulse"></span><span class="oc-title">本论文已开源</span><span class="oc-hint">点击下方卡片直达对应资源</span></div><div class="oc-grid"><a class="oc-chip oc-chip-code" href="https://github.com/Luizerko/AudioWorldSim" target="_blank" rel="noopener"><span class="oc-icon">💻</span><span class="oc-text"><span class="oc-label">代码仓库</span><span class="oc-sub">Luizerko/AudioWorldSim</span></span></a></div></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2608.21075" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2608.21075" target="_blank" rel="noopener">📑 PDF</a><a class="rsrc rsrc-code" href="https://github.com/Luizerko/AudioWorldSim" target="_blank" rel="noopener">💻 代码</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>AudioWorldSim 是一个基于 SoundSpaces 2.0 的开源平台，用于自动生成真实双耳音频数据集，支持世界模型研究。
</div>

## 👥 作者与机构

**Luis Vitor Zerkowski** ¹ · Luiz Velho

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合从事双耳音频、声学模拟或世界模型研究的读者。建议重点阅读平台架构与数据生成流程部分，可快速了解其与 SoundSpaces 2.0 的差异。若需复现，可参考其 GitHub 仓库。

## 🌍 研究背景

双耳音频数据在沉浸式应用和机器学习中至关重要，但真实数据采集成本高、难以大规模获取。现有模拟平台如 SoundSpaces 2.0 提供了声学框架，但缺乏自动化的随机导航生成和连续声音合成修复。AudioWorldSim 旨在填补这一空白，为世界模型等音频任务提供高质量、可复现的双耳音频数据集。

## 💡 核心创新

1. 自动随机代理导航生成
2. 修复连续声音合成问题
3. 基于 SoundSpaces 2.0 扩展
4. 开源平台促进可复现性

## 🏗️ 模型架构

AudioWorldSim 基于 Meta 的 SoundSpaces 2.0 平台，扩展其声学框架。核心模块包括：随机代理导航控制器，自动生成代理在场景中的移动路径；声音合成模块，修复连续声源的合成逻辑；数据输出模块，生成双耳音频及对应元数据。平台支持多种声学场景，输出为双耳音频格式。

## 📊 实验结果

摘要未提供具体实验数据或指标，仅描述平台功能。因此无法进行定量评估，但平台开源，可自行验证生成数据的质量。

## 🎯 结论与影响

AudioWorldSim 提供了一个开源、自动化的双耳音频数据集生成平台，解决了 SoundSpaces 2.0 在连续声音合成和自动导航方面的不足。对世界模型和音频机器学习研究有潜在价值，可促进可复现研究。工业上可用于生成训练数据，降低采集成本。

## ⚠️ 局限与未解决问题

摘要未提及实验验证，缺乏与现有数据集的对比或下游任务评估。平台依赖 SoundSpaces 2.0，可能受限于其场景和声学模型精度。未讨论生成数据的真实性和多样性。

## 🔗 开源资源

- **代码**：<https://github.com/Luizerko/AudioWorldSim>

---

<div class="paper-footer"><span>评分：7.8</span><span>原始：6.8</span><span>+1 重点领域加权</span><a href="/audio-paper-daily/posts/2026-08-25/">← 返回 2026-08-25 速递</a></div>
