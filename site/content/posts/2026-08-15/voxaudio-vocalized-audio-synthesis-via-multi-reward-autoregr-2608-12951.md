---
title: "VoxAudio: Vocalized Audio Synthesis via Multi-Reward Autoregressive Flow Matching"
date: 2026-08-15T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#音频生成"]
summary: "VoxAudio 提出因果自回归流匹配模型，通过分块因果分解、多奖励微调和带转写标注的语料库，实现语音与环境声融合的可控生成。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#音频生成</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#语音增强</span> <span class="tag-pill tag-pill-soft">#文本到音频</span> <span class="tag-pill tag-pill-soft">#流匹配</span> <span class="tag-pill tag-pill-soft">#多奖励微调</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2608.12951</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-08-15</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
<div class="meta-row"><span class="meta-key">⭐</span><span class="meta-val focus-badge">本站重点关注领域 · 评分 +1</span></div>
</div>
</div>

<div class="opensource-banner"><div class="oc-headline"><span class="oc-pulse"></span><span class="oc-title">本论文已开源</span><span class="oc-hint">点击下方卡片直达对应资源</span></div><div class="oc-grid"><a class="oc-chip oc-chip-proj" href="https://voxaudio.github.io" target="_blank" rel="noopener"><span class="oc-icon">🌐</span><span class="oc-text"><span class="oc-label">项目主页</span><span class="oc-sub">voxaudio.github.io</span></span></a><a class="oc-chip oc-chip-demo" href="https://voxaudio.github.io" target="_blank" rel="noopener"><span class="oc-icon">🔊</span><span class="oc-text"><span class="oc-label">在线 Demo</span><span class="oc-sub">voxaudio.github.io</span></span></a></div></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2608.12951" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2608.12951" target="_blank" rel="noopener">📑 PDF</a><a class="rsrc rsrc-proj" href="https://voxaudio.github.io" target="_blank" rel="noopener">🌐 项目主页</a><a class="rsrc rsrc-demo" href="https://voxaudio.github.io" target="_blank" rel="noopener">🔊 Demo</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>VoxAudio 提出因果自回归流匹配模型，通过分块因果分解、多奖励微调和带转写标注的语料库，实现语音与环境声融合的可控生成。
</div>

## 👥 作者与机构

**Wenxiang Guo** ¹ · Changhao Pan · Ziyue Jiang · Fei Wu · Zhou Zhao

**机构**：浙江大学

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合音频生成、语音增强和TTS领域的研究者。建议重点阅读第3节（方法）和第4节（实验），尤其是分块因果分解和多奖励微调部分。可先看摘要和结论，再深入方法细节。

## 🌍 研究背景

语音音频合成旨在生成嵌入环境声的可理解语音，应用于播客和视频配音。现有T2A系统要么将语音降为模糊的嘟囔，要么用TTS后处理混合，无法控制语音出现时机和与场景的交互。本文提出VoxAudio，从架构、偏好和数据三个层面解决该问题。

## 💡 核心创新

1. 分块因果分解与独立噪声水平，支持流式推理和KV缓存
2. 随机分块边界预训练，实现任意分块粒度推理
3. 多奖励负感知微调（NFT），联合优化语义、语言、美学和时间对齐
4. 构建VoxCorpus语料库和VoxBench基准，提供转写和时间间隔标注

## 🏗️ 模型架构

VoxAudio采用因果自回归流匹配模型。输入为文本和音频特征，通过分块因果分解，每个块独立噪声水平，支持滑动窗口流式推理和KV缓存。预训练时使用随机分块边界。推理时通过多奖励NFT微调，优化语义保真度、语言准确性、美学质量和时间对齐。输出为生成的音频特征。

## 📚 数据集

- VoxCorpus（训练，大规模，含转写和时间间隔标注）
- VoxBench（评估，间隔标注基准）
- 四个基准（评估，涵盖通用音频、语音和统一语音音频）

## 📊 实验结果

摘要未提供具体数值，但声称在四个基准上验证了有效性和效率。实验涵盖通用音频、语音和统一语音音频，表明模型在多个任务上表现良好。

## 🎯 结论与影响

VoxAudio通过因果流匹配和多奖励微调，实现了可控的语音音频合成，解决了现有T2A系统语音不可理解和控制性差的问题。其分块因果分解和随机边界预训练为流式生成提供了新思路，对音频生成和配音应用有潜在影响。

## ⚠️ 局限与未解决问题

摘要未提及局限。可能存在的问题包括：多奖励微调的权重平衡未详细说明，VoxCorpus的构建成本高，且未与其他T2A系统进行直接对比，缺乏消融实验。

## 🔗 开源资源

- **项目主页**：<https://voxaudio.github.io>
- **Demo / 试听**：<https://voxaudio.github.io>

---

<div class="paper-footer"><span>评分：9.2</span><span>原始：8.2</span><span>+1 重点领域加权</span><a href="/audio-paper-daily/posts/2026-08-15/">← 返回 2026-08-15 速递</a></div>
