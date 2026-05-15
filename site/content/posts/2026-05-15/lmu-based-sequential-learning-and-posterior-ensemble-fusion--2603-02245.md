---
title: "LMU-Based Sequential Learning and Posterior Ensemble Fusion for Cross-Domain Infant Cry Classification"
date: 2026-05-15T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#LMU", "#后验融合", "#婴儿哭声分类", "#跨域泛化", "#音频分类"]
summary: "提出基于LMU的轻量时序模型与后验融合方法，提升跨数据集婴儿哭声分类的宏F1分数。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero">
<div class="hero-score">
<div class="score-num">6.8</div>
<div class="score-stars">★★★☆☆</div>
<div class="score-tier">前50%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#音频分类</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#婴儿哭声分类</span> <span class="tag-pill tag-pill-soft">#LMU</span> <span class="tag-pill tag-pill-soft">#后验融合</span> <span class="tag-pill tag-pill-soft">#跨域泛化</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2603.02245</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-05-15</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2603.02245" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2603.02245" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出基于LMU的轻量时序模型与后验融合方法，提升跨数据集婴儿哭声分类的宏F1分数。
</div>

## 👥 作者与机构

**Niloofar Jazaeri** ¹ · Hilmi R. Dajani · Marco Janeczek · Martin Bouchard

**机构**：University of Ottawa

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合从事非语音音频分类或婴儿监护研究的读者。可重点阅读§3.2 LMU模块和§3.3后验融合部分，以及表2的跨域结果。若对实时部署感兴趣，可关注§4.4效率分析。

## 🌍 研究背景

婴儿哭声分类在健康监护中面临信号非平稳、标注少、跨域漂移等挑战。现有方法多采用LSTM或CNN，但参数量大、跨数据集泛化差。本文旨在设计轻量模型并引入后验融合策略，提升跨域分类性能。

## 💡 核心创新

1. 采用增强型Legendre Memory Unit (LMU)替代LSTM，减少参数量
2. 多分支CNN编码器融合MFCC、STFT、F0特征
3. 校准后验融合与熵门控加权，缓解数据集偏差

## 🏗️ 模型架构

输入为MFCC、STFT和F0三种特征，分别送入三个CNN分支提取局部模式，拼接后送入增强型LMU模块建模时序依赖，最后通过全连接层输出分类。LMU使用勒让德多项式基函数实现长程记忆，参数量远少于LSTM。

## 📚 数据集

- Baby2020（训练/评估，含多个婴儿哭声）
- Baby Crying（跨域评估，未见婴儿）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| 宏F1 | Baby2020→Baby Crying | LSTM基线（未给出具体值） | **本文方法（未给出具体值）** | 提升（未给出具体值） |

摘要未提供具体数值，仅提及在跨域评估中宏F1有提升，并验证了泄漏感知划分和实时可行性。

## 🎯 结论与影响

本文提出的LMU+后验融合框架在婴儿哭声分类上实现了轻量高效的跨域泛化，为资源受限设备上的实时监护提供了可行方案。后续可探索更丰富的声学特征或自监督预训练。

## ⚠️ 局限与未解决问题

摘要未报告具体指标数值，缺乏与更多基线（如Transformer）的对比；仅使用两个数据集，泛化性验证有限；未分析LMU在不同序列长度下的记忆衰减。

---

<div class="paper-footer"><span>评分：6.8</span><span>原始：6.8</span><a href="/audio-paper-daily/posts/2026-05-15/">← 返回 2026-05-15 速递</a></div>
