---
title: "Frame-Level Pansori Mode Classification with Complementary Audio Representations"
date: 2026-08-11T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#音乐分类"]
summary: "本文提出46小时帧级盘索里调式标注，评估四种互补音频表示，发现模型学习调式相关特征而非记忆曲目，并揭示源分离对特定调式的影响。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#音乐分类</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#音乐信息检索</span> <span class="tag-pill tag-pill-soft">#韩国传统音乐</span> <span class="tag-pill tag-pill-soft">#多模态表示</span> <span class="tag-pill tag-pill-soft">#源分离</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2608.06633</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-08-11</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2608.06633" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2608.06633" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>本文提出46小时帧级盘索里调式标注，评估四种互补音频表示，发现模型学习调式相关特征而非记忆曲目，并揭示源分离对特定调式的影响。
</div>

## 👥 作者与机构

**Sangheon Park** ¹ · Seonguk Ju · Suin Chung · Danbinaerin Han · Dasaem Jeong

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合音乐信息检索、计算音乐学及音频表示学习研究者。建议重点阅读第3节（数据集构建）和第4节（实验设置与结果），尤其是跨模态不一致性分析部分。可先看摘要和结论，再深入方法细节。

## 🌍 研究背景

盘索里是韩国传统声乐体裁，其调式（jo）由音高集合、微音修饰（sigimsae）和音色共同定义，而非仅由音阶决定。现有研究多基于乐谱或人工分析，缺乏大规模帧级标注和自动分类方法。本文旨在构建帧级调式标注数据集，并评估不同音频表示在调式分类中的有效性，同时检测模型是否依赖曲目记忆等捷径。

## 💡 核心创新

1. 构建46小时帧级盘索里调式标注，覆盖五种传统调式
2. 评估四种互补音频表示（mel谱、F0轮廓、MIDI钢琴卷帘、多文化SSL）
3. 设计两种数据划分策略检测捷径学习
4. 通过跨模态不一致性分析揭示音乐学现象
5. 发现源分离对特定调式（changjo）的负面影响

## 🏗️ 模型架构

输入特征包括mel频谱图、F0轮廓、MIDI钢琴卷帘和多文化SSL嵌入。模型采用分类器（具体架构未详述，可能为CNN或Transformer）对每个帧进行分类，输出五种调式标签。训练时采用两种数据划分策略：随机划分和整曲留出，以评估泛化能力。

## 📚 数据集

- 自建盘索里数据集（46小时帧级标注，训练/评估）
- 可能使用源分离后的音频（评估）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| F1 | 自建盘索里数据集（三种主要调式） | 随机划分性能（未给出具体值） | **整曲留出时性能下降2.1-3.6点** | -2.1~-3.6 |

实验表明，在整曲留出策略下，三种主要调式的F1仅下降2.1-3.6点，说明模型学习到调式相关特征而非记忆曲目。源分离去除打击乐线索后，changjo调式性能下降，而通用多文化预训练在Ujo与Gyemyeonjo区分上表现不佳。跨模态不一致性分析恢复了音乐学文献记载的现象，并与现代changjak盘索里的乐谱分析一致。

## 🎯 结论与影响

本文首次提供大规模帧级盘索里调式标注，并系统评估多种音频表示，证明模型能学习调式本质特征。研究为传统音乐自动分析提供新资源和方法，对音乐信息检索和计算音乐学有重要价值，也为源分离在音乐分类中的应用提供警示。

## ⚠️ 局限与未解决问题

未提供具体模型架构和参数量，缺乏与现有方法的对比。数据集仅覆盖盘索里，泛化性未知。未报告推理效率。源分离对调式分类的影响仅初步分析，未深入探讨。

---

<div class="paper-footer"><span>评分：7.2</span><span>原始：7.2</span><a href="/audio-paper-daily/posts/2026-08-11/">← 返回 2026-08-11 速递</a></div>
