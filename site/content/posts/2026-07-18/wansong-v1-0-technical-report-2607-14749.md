---
title: "WanSong v1.0 Technical Report"
date: 2026-07-18T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#音乐生成"]
summary: "WanSong是一个纯扩散模型，可直接生成长达5分钟的高保真多语言歌曲，并同时输出人声和背景音乐双轨。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#音乐生成</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#扩散模型</span> <span class="tag-pill tag-pill-soft">#歌声合成</span> <span class="tag-pill tag-pill-soft">#双轨输出</span> <span class="tag-pill tag-pill-soft">#长音频生成</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2607.14749</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-07-18</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2607.14749" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2607.14749" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>WanSong是一个纯扩散模型，可直接生成长达5分钟的高保真多语言歌曲，并同时输出人声和背景音乐双轨。
</div>

## 👥 作者与机构

**Binghui Chen** ¹ · Pandeng Li · Yu Liu · Jingren Zhou

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合音乐生成、扩散模型研究者阅读。建议重点看§3模型架构和§4实验部分，特别是双轨输出和步长蒸馏的细节。可对比现有级联流水线方法。

## 🌍 研究背景

音乐生成基础模型近期受到广泛关注，但现有方法多采用自回归或级联流水线（如AR+扩散），存在生成效率低、长音频保真度不足、可控性差等问题。WanSong旨在通过纯扩散模型直接生成高质量长歌曲，并支持双轨输出和下游编辑。

## 💡 核心创新

1. 纯扩散模型直接生成5分钟长音频
2. 单次推理输出人声和背景音乐双轨
3. 步长蒸馏实现快速推理
4. 支持微调定制和下游编辑任务

## 🏗️ 模型架构

WanSong采用纯扩散模型架构，输入为文本或音频条件，通过扩散过程直接生成双轨音频（人声和背景音乐）。模型可能基于U-Net或Transformer主干，支持长达5分钟的音频生成。通过步长蒸馏加速推理，并支持微调以适应下游编辑任务。

## 📊 实验结果

摘要未提供具体实验指标，仅声称WanSong能生成高保真多语言歌曲，支持双轨输出和快速推理。需参考完整论文获取定量结果。

## 🎯 结论与影响

WanSong提出了一种纯扩散模型用于长格式歌曲生成，避免了级联流水线的复杂性，同时支持双轨输出和高效推理。该方法有望推动音乐生成模型向更简单、更可控的方向发展，对工业级歌曲创作和编辑具有潜在应用价值。

## ⚠️ 局限与未解决问题

摘要未提及模型参数量、训练数据规模、与现有方法的定量对比，也未讨论生成音频的客观指标（如MOS、FAD）。缺乏消融实验和泛化性分析。

---

<div class="paper-footer"><span>评分：8.2</span><span>原始：8.2</span><a href="/audio-paper-daily/posts/2026-07-18/">← 返回 2026-07-18 速递</a></div>
