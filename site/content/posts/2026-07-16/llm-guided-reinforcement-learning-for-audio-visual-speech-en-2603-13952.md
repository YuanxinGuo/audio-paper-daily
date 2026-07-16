---
title: "LLM-Guided Reinforcement Learning for Audio-Visual Speech Enhancement"
date: 2026-07-16T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#语音增强"]
summary: "提出基于LLM可解释奖励模型的强化学习框架，用于优化视听语音增强的感知质量。"
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
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#语音增强</span> <span class="tag-pill tag-pill-soft">#视听融合</span> <span class="tag-pill tag-pill-soft">#强化学习</span> <span class="tag-pill tag-pill-soft">#大语言模型</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2603.13952</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-07-16</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
<div class="meta-row"><span class="meta-key">⭐</span><span class="meta-val focus-badge">本站重点关注领域 · 评分 +1</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2603.13952" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2603.13952" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出基于LLM可解释奖励模型的强化学习框架，用于优化视听语音增强的感知质量。
</div>

## 👥 作者与机构

**Chih-Ning Chen** ¹ · Jen-Cheng Hou · Hsin-Min Wang · Shao-Yi Chien · Yu Tsao · Fan-Gang Zeng

**机构**：台湾中央研究院 · 台湾大学 · 加州大学尔湾分校

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合语音增强、多模态学习及RL研究者。建议重点阅读§3奖励模型设计与§4实验对比，尤其是表2的PESQ/STOI结果。可复现代码后尝试替换LLM为其他音频描述模型。

## 🌍 研究背景

现有视听语音增强方法多采用SI-SNR、MSE等目标函数，但这些指标与感知质量相关性差且缺乏可解释性。虽然DNSMOS等无参考指标被用于优化，但其反馈仍是标量，无法提供语义信息。本文旨在利用LLM生成自然语言描述作为奖励信号，结合强化学习提升增强语音的感知质量。

## 💡 核心创新

1. 提出LLM生成自然语言描述作为可解释奖励
2. 将情感分析模型将文本描述转为1-5评分用于PPO
3. 首次将LLM奖励用于视听语音增强RL微调
4. 在AVSEC-4上超越DNSMOS-based RL基线

## 🏗️ 模型架构

输入：视频帧与含噪音频经预训练AVSE模型（如AV-ConvTasNet）生成增强语音。增强语音送入音频LLM（如Qwen-Audio）生成自然语言描述，再经情感分析模型（如RoBERTa）输出1-5评分作为奖励。使用PPO算法微调AVSE模型，最大化奖励。

## 📚 数据集

- AVSEC-4（训练/评估，包含4种噪声类型和SNR条件）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| PESQ | AVSEC-4 | Supervised baseline (未明确值) | **未明确值** | 显著提升（原文表述） |
| STOI | AVSEC-4 | Supervised baseline | **未明确值** | 显著提升 |
| 主观听感MOS | AVSEC-4 | DNSMOS-based RL baseline | **未明确值** | 更优 |

实验在AVSEC-4数据集上进行，与监督基线及DNSMOS-based RL基线对比。所提方法在PESQ、STOI、神经质量指标及主观听感测试中均取得更优结果。消融实验验证了LLM奖励的有效性，且自然语言描述提供了可解释的反馈。

## 🎯 结论与影响

本文证明LLM生成的语义反馈可有效指导AVSE模型优化感知质量，优于传统标量奖励。该思路可推广至其他语音处理任务，为可解释性奖励设计提供新范式。工业上可提升助听器、通信等场景的语音质量。

## ⚠️ 局限与未解决问题

依赖音频LLM的生成质量，可能引入偏差；情感分析模型将文本映射为评分存在信息损失；仅在单一数据集AVSEC-4上验证，泛化性未知；未报告推理延迟与计算开销。

---

<div class="paper-footer"><span>评分：8.8</span><span>原始：7.8</span><span>+1 重点领域加权</span><a href="/audio-paper-daily/posts/2026-07-16/">← 返回 2026-07-16 速递</a></div>
