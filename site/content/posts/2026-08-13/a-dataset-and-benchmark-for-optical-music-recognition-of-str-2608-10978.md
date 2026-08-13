---
title: "A Dataset and Benchmark for Optical Music Recognition of String Quartet Scores"
date: 2026-08-13T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#光学音乐识别"]
summary: "首个面向弦乐四重奏多声部乐谱的光学音乐识别数据集OSSQ-OMR，含系统级和谱表级图像及三种编码，并提供基准测试。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#光学音乐识别</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#数据集</span> <span class="tag-pill tag-pill-soft">#基准测试</span> <span class="tag-pill tag-pill-soft">#弦乐四重奏</span> <span class="tag-pill tag-pill-soft">#多声部</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2608.10978</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-08-13</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2608.10978" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2608.10978" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>首个面向弦乐四重奏多声部乐谱的光学音乐识别数据集OSSQ-OMR，含系统级和谱表级图像及三种编码，并提供基准测试。
</div>

## 👥 作者与机构

**Dongmin Kim** ¹ · Brian Liu · Jose J. Valero-Mas · Dasaem Jeong

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合OMR研究者、音乐信息检索领域学者。建议重点阅读数据集构建部分（§3）和基准实验（§5），以了解数据格式和基线性能。可先看表1和表2。

## 🌍 研究背景

光学音乐识别（OMR）旨在将乐谱图像转录为数字格式。现有研究多集中于单声部或钢琴谱，多声部乐谱识别因缺乏合适数据集而进展缓慢。本文针对弦乐四重奏这一典型多声部体裁，构建了首个专用数据集，填补了该空白。

## 💡 核心创新

1. 首个多声部OMR数据集，基于OpenScore弦乐四重奏语料库
2. 图像与转录文本像素级对齐，提供系统级和谱表级图像
3. 提供三种编码格式（LMXE、**kern、ABC）
4. 提出基准协议，含四种随机划分和互斥测试集
5. 评估两种代表性OMR模型，揭示编码和分割选择的影响

## 🏗️ 模型架构

数据集包含从IMSLP扫描的乐谱图像，与OpenScore数字编码对齐。图像按系统和谱表切分，转录文本提供LMXE、**kern、ABC三种格式。基准测试使用两种OMR模型：基于LSTM和基于Transformer的序列模型，输入为谱表图像，输出为符号序列。

## 📚 数据集

- OSSQ-OMR（训练/评估，116首弦乐四重奏，24,544系统图像，98,172谱表图像）
- OpenScore String Quartet（源语料库，用于生成数字编码）
- IMSLP（原始扫描图像来源）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| OMR-NED | OSSQ-OMR（合成图像） | Transformer基线（具体值未给出） | **LSTM基线（具体值未给出）** | 未给出具体差值 |
| OMR-NED | OSSQ-OMR（扫描图像） | Transformer基线（具体值未给出） | **LSTM基线（具体值未给出）** | LSTM退化程度约为Transformer的1/2.6 |

摘要报告基线在合成图像上OMR-NED最低达3.6%，扫描图像上为5.9%。LSTM基线在扫描图像上的性能退化程度显著小于Transformer基线（约2.6倍），表明模型对扫描噪声的鲁棒性差异。具体各模型数值未在摘要中给出。

## 🎯 结论与影响

本文首次为多声部OMR提供了专用数据集和基准，填补了领域空白。该数据集将促进多声部乐谱识别研究，并可能推动OMR在音乐图书馆数字化中的应用。

## ⚠️ 局限与未解决问题

摘要未提及局限。作为审稿人，可能的问题包括：数据集规模有限（116首），仅覆盖弦乐四重奏一种体裁；基准模型仅两种，缺乏更现代的架构；未报告模型参数量或推理时间；扫描图像与合成图像差异可能影响泛化。

---

<div class="paper-footer"><span>评分：7.2</span><span>原始：7.2</span><a href="/audio-paper-daily/posts/2026-08-13/">← 返回 2026-08-13 速递</a></div>
