---
title: "Academic Text-to-Music Grand Challenge: Datasets, Baselines, and Evaluation Methods"
date: 2026-05-22T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#音乐生成"]
summary: "提出ICME 2026学术文本到音乐生成挑战赛，提供标准化数据集、基线和评估方法，旨在降低学术研究门槛。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero">
<div class="hero-score">
<div class="score-num">7.5</div>
<div class="score-stars">★★★★☆</div>
<div class="score-tier">前25%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#音乐生成</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#文本到音乐生成</span> <span class="tag-pill tag-pill-soft">#基准测试</span> <span class="tag-pill tag-pill-soft">#数据集</span> <span class="tag-pill tag-pill-soft">#评估方法</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2605.21538</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-05-22</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2605.21538" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2605.21538" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出ICME 2026学术文本到音乐生成挑战赛，提供标准化数据集、基线和评估方法，旨在降低学术研究门槛。
</div>

## 👥 作者与机构

**Fang-Chih Hsieh** ¹ · Wei-Jaw Lee · Chun-Ping Wang · Hung-yi Lee · Hao-Wen Dong · Yi-Hsuan Yang

**机构**：台湾大学 · 阳明交通大学

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合从事音乐生成、文本到音频生成的研究者阅读。建议重点读§3挑战设置、§4评估方法（特别是CCS指标）和§5基线。可先看表1数据集统计和表2基线结果。

## 🌍 研究背景

文本到音乐生成（TTM）近年发展迅速，但现有模型多依赖大规模专有数据集和工业级计算资源，学术机构难以复现和参与。这导致研究门槛高、可重复性差。本文提出ATTM挑战赛，通过提供标准化CC许可数据集、开源基线和评估代码，建立公平比较平台，推动学术TTM研究。

## 💡 核心创新

1. 提出Concept Coverage Score (CCS)评估指标
2. 建立标准化CC-licensed音乐生成基准
3. 设置效率与性能双赛道降低门槛
4. 提供完整预处理流水线和参考描述
5. 开源评估代码（FAD/CLAP/CCS）

## 🏗️ 模型架构

挑战赛框架：输入为文本描述，输出为音乐音频。基线模型采用基于扩散的架构，使用预训练CLAP文本编码器，通过U-Net或Transformer解码器生成mel谱图，再经声码器合成波形。效率赛道限制参数量≤500M，性能赛道无限制。评估流程包括客观指标（FAD、CLAP、CCS）和主观听测。

## 📚 数据集

- MTG-Jamendo（训练/评估，CC-licensed子集，仅器乐，约55k曲目）
- MusicCaps（参考描述，用于CLAP训练）

## 📊 实验结果

摘要未提供具体实验结果数值，但描述了评估流程：客观指标包括FAD、CLAP和CCS，主观听测采用MUSHRA协议。基线模型将开源，供参赛者参考。

## 🎯 结论与影响

ATTM挑战赛通过标准化数据集、开源基线和多维度评估，为学术TTM研究提供了公平竞争平台。CCS指标创新性地衡量概念覆盖度，有望成为新标准。该挑战有望降低研究门槛，促进可重复性，并推动音乐生成在学术界的普及。

## ⚠️ 局限与未解决问题

数据集仅含器乐音乐，缺乏人声和复杂编曲；CCS指标依赖预训练概念检测器，可能引入偏差；未报告基线模型的计算成本和推理速度；挑战赛尚未进行，实际效果待验证。

---

<div class="paper-footer"><span>评分：7.5</span><span>原始：7.5</span><a href="/audio-paper-daily/posts/2026-05-22/">← 返回 2026-05-22 速递</a></div>
