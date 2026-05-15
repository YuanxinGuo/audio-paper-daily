---
title: "Persian MusicGen: A Large-Scale Dataset and Culturally-Aware Generative Model for Persian Music"
date: 2026-05-15T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#音乐生成"]
summary: "构建首个大规模波斯音乐数据集（900+小时），微调MusicGen模型以生成符合波斯音乐风格的作品。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero">
<div class="hero-score">
<div class="score-num">7.2</div>
<div class="score-stars">★★★★☆</div>
<div class="score-tier">前25%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#音乐生成</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#音乐生成</span> <span class="tag-pill tag-pill-soft">#文化适应</span> <span class="tag-pill tag-pill-soft">#数据集构建</span> <span class="tag-pill tag-pill-soft">#微调</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2605.14765</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-05-15</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2605.14765" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2605.14765" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>构建首个大规模波斯音乐数据集（900+小时），微调MusicGen模型以生成符合波斯音乐风格的作品。
</div>

## 👥 作者与机构

**Mohammad Hossein Sameti** ¹ · Diba Hadi Esfangereh · Sepehr Harfi Moridani · Leili Javidpour · Mahdieh Soleymani Baghshah

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合音乐生成、文化适应领域的研究者。建议重点阅读第3节（数据集构建）和第4节（微调方法），可先看表1了解数据集规模。

## 🌍 研究背景

现有音乐生成模型（如MusicGen）主要基于西方音乐训练，难以捕捉波斯音乐独特的调式（Dastgah）和节奏结构。缺乏大规模波斯音乐数据集是主要瓶颈。本文旨在填补这一空白，通过构建900+小时的高质量波斯音乐数据集，并微调MusicGen使其生成符合波斯风格的音乐。

## 💡 核心创新

1. 首个大规模波斯音乐数据集（900+小时）
2. 文化感知的MusicGen微调方法
3. 引入语义对齐评估指标（标签准确率）

## 🏗️ 模型架构

基于MusicGen架构：输入为文本/风格标签，经文本编码器映射到嵌入空间，然后由自回归Transformer解码器生成音频token，最后通过音频解码器输出波形。微调时冻结部分层，仅更新特定参数以适应波斯音乐风格。

## 📚 数据集

- 波斯音乐数据集（900+小时，训练/评估，包含流行、传统、当代等子类型）

## 📊 实验结果

摘要未提供具体数值结果，仅提及微调模型生成的音乐更符合波斯风格，并通过主观评估和标签准确率衡量语义对齐。

## 🎯 结论与影响

本文构建了首个大规模波斯音乐数据集，并展示了MusicGen在文化适应上的潜力。未来可推动非西方音乐生成研究，并为工业界提供多文化音乐生成工具。

## ⚠️ 局限与未解决问题

未报告客观指标（如FAD、CLAP score），缺乏与基线模型的定量对比；数据集仅覆盖波斯音乐，泛化性未知；未讨论模型参数量及推理效率。

---

<div class="paper-footer"><span>评分：7.2</span><span>原始：7.2</span><a href="/audio-paper-daily/posts/2026-05-15/">← 返回 2026-05-15 速递</a></div>
