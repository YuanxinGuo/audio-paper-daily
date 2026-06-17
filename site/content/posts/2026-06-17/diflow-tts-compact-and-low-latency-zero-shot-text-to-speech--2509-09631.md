---
title: "DiFlow-TTS: Compact and Low-Latency Zero-Shot Text-to-Speech with Discrete Flow Matching"
date: 2026-06-17T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#语音合成"]
summary: "提出基于离散流匹配的零样本语音合成框架DiFlow-TTS，兼顾生成质量与推理效率。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#语音合成</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#零样本语音合成</span> <span class="tag-pill tag-pill-soft">#离散流匹配</span> <span class="tag-pill tag-pill-soft">#声学模型</span> <span class="tag-pill tag-pill-soft">#非自回归</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2509.09631</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-06-17</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2509.09631" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2509.09631" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出基于离散流匹配的零样本语音合成框架DiFlow-TTS，兼顾生成质量与推理效率。
</div>

## 👥 作者与机构

**Ngoc-Son Nguyen** ¹ · Thanh V. T. Tran · Hieu-Nghia Huynh-Nguyen · Truong-Son Hy · Van Nguyen

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合语音合成研究者，重点看§3的离散流匹配设计及§4的消融实验，可对比VALL-E等基线。

## 🌍 研究背景

零样本TTS旨在模仿未见说话人声音，现有方法中自回归模型延迟高，扩散模型受限于训练配置，连续流匹配面临优化困难。本文提出离散流匹配框架，通过确定性音素-内容映射器和分解式离散流去噪器，同时生成韵律和声学token，解决连续空间优化问题。

## 💡 核心创新

1. 提出离散流匹配用于零样本TTS
2. 分解式离散流去噪器联合生成韵律和声学token
3. 确定性音素-内容映射器简化语言建模

## 🏗️ 模型架构

输入文本经音素编码器得到音素序列，通过确定性Phoneme-Content Mapper映射为内容表示；Factorized Discrete Flow Denoiser包含两个并行流：一个生成韵律token（如F0），一个生成声学token（如HuBERT离散单元），两者通过离散流匹配训练，最终由声码器合成波形。

## 📚 数据集

- LibriTTS（训练/评估）
- VCTK（评估，未见说话人）

## 📊 实验结果

摘要未提供具体数值，但声称在多个指标上有效。需关注与VALL-E、YourTTS等基线的对比结果。

## 🎯 结论与影响

DiFlow-TTS通过离散流匹配实现了紧凑、低延迟的零样本TTS，在生成质量和效率间取得平衡。该方法为离散空间生成建模提供了新思路，有望推动实时语音克隆应用。

## ⚠️ 局限与未解决问题

未报告推理延迟和模型参数量；缺乏与最新扩散/流匹配方法的直接对比；未见说话人泛化能力可能受限于训练数据多样性。

---

<div class="paper-footer"><span>评分：7.8</span><span>原始：7.8</span><a href="/audio-paper-daily/posts/2026-06-17/">← 返回 2026-06-17 速递</a></div>
