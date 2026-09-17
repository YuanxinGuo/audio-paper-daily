---
title: "Instrument Classification of Solo Sheet Music Images"
date: 2026-09-17T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#音乐信息检索"]
summary: "将独奏乐谱图像转为 bootleg score 词序列，用 AWD-LSTM/GPT-2/RoBERTa 做乐器分类，预训练加数据增强提升准确率。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero">
<div class="hero-score">
<div class="score-num">4.5</div>
<div class="score-stars">★★☆☆☆</div>
<div class="score-tier">后50%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#音乐信息检索</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#乐谱图像分析</span> <span class="tag-pill tag-pill-soft">#音乐信息检索</span> <span class="tag-pill tag-pill-soft">#语言模型预训练</span> <span class="tag-pill tag-pill-soft">#数据增强</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2609.18980</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-09-17</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2609.18980" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2609.18980" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>将独奏乐谱图像转为 bootleg score 词序列，用 AWD-LSTM/GPT-2/RoBERTa 做乐器分类，预训练加数据增强提升准确率。
</div>

## 👥 作者与机构

**Kevin Ji** ¹ · Daniel Yang · TJ Tsai

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合做乐谱图像分析或音乐信息检索（MIR）跨模态研究的读者。若关注音频乐器识别，本文参考价值有限。建议重点看 §3 的 bootleg score 序列化方法与 §4 的数据增强设计，表 2 的预训练消融值得一看。无需通读全文。

## 🌍 研究背景

乐器识别此前主要基于音频数据，依赖频谱特征与 CNN/CRNN 等模型。乐谱图像领域的乐器分类研究较少，且标注数据稀缺，直接训练分类器性能受限。本文把乐谱图像转为符号序列后当作文本分类问题，试图借助 NLP 中成熟的预训练语言模型范式，缓解标注数据不足的问题，并探索数据增强对分类精度的作用。

## 💡 核心创新

1. 将乐谱图像经 bootleg score 转为词序列，复用文本分类范式
2. 用无标注 IMSLP 乐谱预训练语言模型再微调分类器
3. 提出两种针对乐谱序列的数据增强方法

## 🏗️ 模型架构

输入为独奏乐谱图像，先经 bootleg score 表示转换为离散音乐词序列，再送入语言模型主干。作者分别训练 AWD-LSTM、GPT-2 和 RoBERTa 三种模型：先在 IMSLP 无标注乐谱上做语言建模预训练，再用预训练权重初始化分类器，最后在八类乐器的标注数据上微调。输出为八类乐器的分类概率。摘要未给出参数量。

## 📚 数据集

- IMSLP 独奏乐谱图像（预训练，无标注）
- IMSLP 独奏乐谱图像（微调与评估，八类乐器，有标注）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| 分类准确率 | IMSLP 八类乐器 | RoBERTa 无预训练 34.5% | **RoBERTa 预训练 42.9%** | +8.4% |
| 分类准确率 | IMSLP 八类乐器 | RoBERTa 预训练 42.9% | **RoBERTa 预训练+数据增强** | +15% |

摘要报告 GPT-2 与 RoBERTa 略优于 AWD-LSTM；RoBERTa 经预训练后准确率从 34.5% 提升到 42.9%，两种数据增强再带来约 15% 的额外提升。摘要未给出 AWD-LSTM 与 GPT-2 的具体数值，也未报告消融细节、推理效率或跨数据集泛化结果。

## 🎯 结论与影响

本文证明乐谱图像乐器分类可借助语言模型预训练与数据增强显著提升，最强结论是预训练加增强使 RoBERTa 准确率大幅提高。该思路为乐谱图像理解与 MIR 跨模态研究提供了可复用范式，对乐谱数字化、自动编目等工业场景有潜在价值。

## ⚠️ 局限与未解决问题

仅八类乐器、单一 IMSLP 数据源，存在数据集偏差；未报告推理延迟与模型规模；缺少与音频乐器识别方法的对比；数据增强的两种方法细节与消融在摘要中未展开，泛化性存疑。

---

<div class="paper-footer"><span>评分：4.5</span><span>原始：4.5</span><a href="/audio-paper-daily/posts/2026-09-17/">← 返回 2026-09-17 速递</a></div>
