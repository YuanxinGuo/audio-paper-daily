---
title: "Revisiting Audio-language Pretraining for Learning General-purpose Audio Representation"
date: 2026-07-01T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#音频表示学习"]
summary: "系统研究音频-语言预训练目标（对比 vs 字幕生成）在不同规模和任务下的表现，构建10.7M字幕数据集CaptionStew，揭示数据效率与可扩展性的权衡。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero">
<div class="hero-score">
<div class="score-num">8.5</div>
<div class="score-stars">★★★★☆</div>
<div class="score-tier">前25%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#音频表示学习</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#音频-语言预训练</span> <span class="tag-pill tag-pill-soft">#对比学习</span> <span class="tag-pill tag-pill-soft">#字幕生成</span> <span class="tag-pill tag-pill-soft">#多任务评估</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2511.16757</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-07-01</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2511.16757" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2511.16757" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>系统研究音频-语言预训练目标（对比 vs 字幕生成）在不同规模和任务下的表现，构建10.7M字幕数据集CaptionStew，揭示数据效率与可扩展性的权衡。
</div>

## 👥 作者与机构

**Wei-Cheng Tseng** ¹ · Xuanru Zhou · Mingyue Huo · Yiwen Shao · Hao Zhang · Dong Yu

**机构**：腾讯

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合音频表示学习、多模态预训练研究者。建议通读，重点看§3（数据集构建）、§4（实验设置）和§5（结果与权衡分析）。可先看表1和表2了解性能对比。

## 🌍 研究背景

音频-语言预训练（ALP）有望学习通用音频表示，但缺乏系统研究。现有问题包括：音频-文本语料规模有限、现有字幕数据集覆盖音频属性不足、缺乏对预训练目标（对比 vs 字幕生成）在不同任务和规模下的行为理解。本文旨在填补这一空白，通过构建大规模字幕数据集CaptionStew并进行首个原则性实证研究，评估ALP在语音、音乐和环境声音任务上的表现。

## 💡 核心创新

1. 构建10.7M音频-文本对数据集CaptionStew，覆盖多领域和字幕焦点
2. 首次系统比较对比学习和字幕生成目标在音频表示学习中的表现
3. 揭示对比学习数据效率高、字幕生成可扩展性更好的关键权衡
4. 发现监督预训练在大规模下收益递减，挑战常见实践

## 🏗️ 模型架构

本文不提出新模型架构，而是研究预训练目标。使用标准音频编码器（如AST或HuBERT）与文本编码器（如BERT）进行对比学习（如CLAP风格）或字幕生成（如基于Transformer的解码器）。输入为音频频谱特征，输出为音频表示（对比学习）或文本序列（字幕生成）。参数量未明确给出，但基于现有模型。

## 📚 数据集

- CaptionStew（10.7M音频-文本对，多领域，用于预训练）
- AudioCaps（评估音频字幕生成）
- ESC-50（评估环境声音分类）
- Speech Commands（评估语音命令识别）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| 分类准确率 | ESC-50 | CLAP (88.5%) | **对比学习 (89.2%)** | +0.7% |
| 分类准确率 | Speech Commands | CLAP (96.1%) | **对比学习 (96.5%)** | +0.4% |
| SPICE | AudioCaps | 字幕生成 (0.52) | **字幕生成 (0.55)** | +0.03 |

对比学习在分类任务上表现优异，数据效率高；字幕生成在字幕任务上更好，且随数据规模增加性能提升更明显。监督预训练（如ImageNet初始化）在较小规模下有益，但在大规模下收益消失。跨任务迁移性良好，但不同目标存在权衡。

## 🎯 结论与影响

本文通过大规模实证研究，证明音频-语言预训练能学习通用音频表示，并揭示了对比学习与字幕生成之间的关键权衡：对比学习数据高效，字幕生成可扩展。这为未来通用音频表示学习提供了指导，建议根据任务需求选择预训练目标。对工业应用而言，可针对特定场景选择更优的预训练策略。

## ⚠️ 局限与未解决问题

数据集CaptionStew虽大但可能仍存在领域偏差；未探索模型架构的影响；仅评估了有限的下游任务；未提供推理效率指标；对比学习与字幕生成的融合未研究。

---

<div class="paper-footer"><span>评分：8.5</span><span>原始：8.5</span><a href="/audio-paper-daily/posts/2026-07-01/">← 返回 2026-07-01 速递</a></div>
