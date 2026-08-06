---
title: "Towards Robust Version Identification in the Wild: A Dataset, Benchmark, and Fine-Tuning Study"
date: 2026-08-06T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#音乐版本识别"]
summary: "提出大规模音乐版本识别数据集DiVers，含110万版本，提升模型对真实世界噪声和多样性的鲁棒性。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#音乐版本识别</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#数据集构建</span> <span class="tag-pill tag-pill-soft">#鲁棒性</span> <span class="tag-pill tag-pill-soft">#微调</span> <span class="tag-pill tag-pill-soft">#音乐信息检索</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2608.04543</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-08-06</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2608.04543" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2608.04543" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出大规模音乐版本识别数据集DiVers，含110万版本，提升模型对真实世界噪声和多样性的鲁棒性。
</div>

## 👥 作者与机构

**Simon Hachmeier** ¹ · R. Oguz Araz · Dmitry Bogdanov · Robert J\"aschke · Xavier Serra

**机构**：柏林洪堡大学 · 庞培法布拉大学 · 哈索·普拉特纳研究院

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合音乐信息检索、版本识别研究者阅读。建议重点阅读第3节（数据集构建）和第4节（实验），以了解数据划分和鲁棒性评估方法。可先看摘要和结论，再深入数据构建细节。

## 🌍 研究背景

音乐版本识别（VI）旨在识别同一首歌曲的不同演绎版本。现有数据集如SecondHandSongs和Discogs主要基于专业录音，导致模型在真实场景（如业余翻唱、现场录音）中性能下降。本文旨在解决这一领域空白，通过构建大规模、多样化的数据集DiVers，并评估现有VI系统在其上的表现，以提升模型的鲁棒性。

## 💡 核心创新

1. 构建DiVers数据集，含110万音乐版本，规模远超现有数据集
2. 提供自动标签（如器乐、现场）和片段级音乐存在性预测
3. 与现有数据集兼容的划分，便于跨数据集评估
4. 实验证明DiVers训练模型对声学多样性和噪声鲁棒性显著提升
5. 开源数据集元数据、构建代码和实验流程，促进可复现性

## 🏗️ 模型架构

本文主要贡献是数据集，而非模型架构。实验中使用现有SOTA VI系统（如基于深度学习的嵌入模型）进行训练和评估。输入为音频片段，通过预训练模型提取特征，训练版本级分类器。具体网络结构未在摘要中详述，但可能包括CNN或Transformer架构。

## 📚 数据集

- DiVers（训练/验证/测试，110万版本）
- Discogs-VI-YT（评估，兼容划分）
- SHS100K（评估，兼容划分）
- Da-TACOS（评估，兼容划分）

## 📊 实验结果

摘要未提供具体指标数值，但指出在DiVers上训练的模型在声学多样性和噪声输入上鲁棒性显著提升，同时在干净、工作室质量基准上保持稳定性能。具体数据需查阅论文。

## 🎯 结论与影响

DiVers数据集填补了真实世界版本识别数据缺失的空白，其大规模和多样性显著提升了VI系统的鲁棒性。该工作为VI研究提供了新基准，有望推动该领域向实际应用发展，并促进可复现研究。

## ⚠️ 局限与未解决问题

摘要未提及局限，但可能包括：自动标签可能存在噪声；数据集构建依赖自动方法，可能引入偏差；未报告模型推理效率；对比实验可能不全面。

---

<div class="paper-footer"><span>评分：7.8</span><span>原始：7.8</span><a href="/audio-paper-daily/posts/2026-08-06/">← 返回 2026-08-06 速递</a></div>
