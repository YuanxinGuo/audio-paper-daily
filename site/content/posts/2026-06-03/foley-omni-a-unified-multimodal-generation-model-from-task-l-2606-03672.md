---
title: "Foley-Omni: A Unified Multimodal Generation Model from Task-Level Audio Synthesis to Complete Video Soundtrack Generation"
date: 2026-06-03T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#音频生成"]
summary: "提出Foley-Omni统一多模态音频生成模型，将语音、音效和音乐联合建模，实现完整视频配乐生成。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero">
<div class="hero-score">
<div class="score-num">8.2</div>
<div class="score-stars">★★★★☆</div>
<div class="score-tier">前25%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#音频生成</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#多模态生成</span> <span class="tag-pill tag-pill-soft">#视频配乐</span> <span class="tag-pill tag-pill-soft">#统一生成模型</span> <span class="tag-pill tag-pill-soft">#语音合成</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2606.03672</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-06-03</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2606.03672" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2606.03672" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出Foley-Omni统一多模态音频生成模型，将语音、音效和音乐联合建模，实现完整视频配乐生成。
</div>

## 👥 作者与机构

**Ye Tao** ¹ · Lupeng Liu · Xuenan Xu · Jiasun Feng · Jiarui Wang · Ying Qin · Shuiyang Mao · Wei Liu · … 等 1 人

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合音频生成、多模态学习研究者。建议重点阅读§3联合生成框架和§4数据构建流程。可先看表1对比现有统一模型，再深入§3.2共享潜空间设计。

## 🌍 研究背景

现有统一音频生成模型（如AudioLDM2、Make-An-Audio）支持语音、音效、音乐等独立任务级合成，但真实视频制作需要多个音频组件（语音、音效、音乐）联合且一致地生成。缺乏同时建模多组件并保持视听一致性的方法，且缺少用于评估完整视频配乐生成的基准。本文旨在解决这一空白。

## 💡 核心创新

1. 提出Foley-Omni统一多模态生成模型，联合建模语音、音效、音乐
2. 设计共享潜空间生成过程，实现多组件联合生成
3. 开发音视频数据整理流水线，支持训练与复现
4. 构建V2ST-Bench基准，用于评估完整视频配乐生成

## 🏗️ 模型架构

输入为视频帧和文本提示，通过CLAP和图像编码器提取多模态特征，映射到共享潜空间。主干网络采用扩散Transformer（DiT），在潜空间内联合生成语音、音效和音乐的潜表示。最后通过各自的解码器（如HiFi-GAN、AudioMAE解码器）输出波形。模型参数量未在摘要中给出。

## 📚 数据集

- V2ST-Bench（评估基准，包含视频-完整配乐对）
- 内部收集的音视频数据（训练，规模未提及）

## 📊 实验结果

摘要未提供具体数值结果，仅说明Foley-Omni在独立合成任务上达到与专家系统竞争的性能，并在混合配乐生成中提升了语音可懂度、视听一致性和感知质量。

## 🎯 结论与影响

Foley-Omni首次将任务级音频合成扩展到完整视频配乐生成，通过共享潜空间联合建模语音、音效和音乐，在保持各组件质量的同时提升整体一致性。该工作为视频配乐自动化提供了新范式，有望推动影视制作和内容创作领域的应用。

## ⚠️ 局限与未解决问题

摘要未提及模型参数量、推理速度等效率指标；缺乏与现有统一模型在完整配乐任务上的定量对比；数据构建流水线的细节和规模未充分说明；未讨论多组件联合生成时的冲突或权衡问题。

---

<div class="paper-footer"><span>评分：8.2</span><span>原始：8.2</span><a href="/audio-paper-daily/posts/2026-06-03/">← 返回 2026-06-03 速递</a></div>
