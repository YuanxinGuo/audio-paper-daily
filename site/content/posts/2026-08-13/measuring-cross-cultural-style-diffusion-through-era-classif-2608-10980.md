---
title: "Measuring Cross-Cultural Style Diffusion Through Era Classification: US and Korean Popular Music"
date: 2026-08-13T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#音乐信息检索"]
summary: "通过时代分类框架量化美国与韩国流行音乐之间的风格扩散，发现韩国歌曲在1960-1980年代落后美国约4-5年，1990年代后差距缩小至2-3年。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#音乐信息检索</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#音乐风格扩散</span> <span class="tag-pill tag-pill-soft">#时代分类</span> <span class="tag-pill tag-pill-soft">#跨文化分析</span> <span class="tag-pill tag-pill-soft">#CNN</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2608.10980</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-08-13</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2608.10980" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2608.10980" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>通过时代分类框架量化美国与韩国流行音乐之间的风格扩散，发现韩国歌曲在1960-1980年代落后美国约4-5年，1990年代后差距缩小至2-3年。
</div>

## 👥 作者与机构

**Dasol Lee** ¹ · Minhee Lee · Seonguk Ju · Daewoong Kim · Harin Lee · Dasaem Jeong

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合音乐信息检索、计算音乐学及跨文化传播研究者阅读。建议重点阅读方法部分（§3）和结果分析（§4），可先看图2和表1了解核心发现。

## 🌍 研究背景

流行音乐在全球传播并被本地重新诠释，但跨文化风格扩散的过程很少被量化。以往研究多依赖人工标注或小规模分析，缺乏大规模、可复现的度量方法。本文提出基于时代分类的框架，利用CNN分类器从Billboard音频中学习时代特征，并应用于韩国Melon榜单歌曲，以量化两国音乐风格的时序对齐程度。

## 💡 核心创新

1. 提出基于时代分类的跨文化风格扩散量化框架
2. 利用从零训练的CNN分类器，避免预训练偏差
3. 发现韩国音乐风格滞后美国约4-5年，1990年代后缩小至2-3年
4. 通过反向推断验证结果，并跨架构和随机种子验证稳健性
5. 框架可推广至其他文化对

## 🏗️ 模型架构

使用从零训练的CNN分类器，输入为音频的mel-spectrogram特征，主干为简单的卷积神经网络，包含多个卷积层和池化层，最后通过全连接层输出时代类别。模型在Billboard Hot 100音频上训练，用于预测歌曲所属的时代（如1960s、1970s等）。训练时使用交叉熵损失，并采用数据增强（如时间平移、音高变化）提升泛化。

## 📚 数据集

- Billboard Hot 100音频（训练时代分类器）
- Melon榜单歌曲（评估跨文化风格扩散）

## 📊 实验结果

摘要未提供具体数值，但报告了关键发现：韩国歌曲在1960-1980年代被推断为更早的Billboard时代，中位数差距约4-5年；1990年代差距减半至2-3年，并持续至2000年代。反向推断显示互补的缩小趋势，且结果在不同架构和随机种子下保持一致。

## 🎯 结论与影响

本文提出的时代分类框架有效量化了美韩流行音乐的风格扩散，揭示了韩国音乐从滞后到逐渐同步的演变过程。该框架可推广至其他文化对，为计算音乐学提供新工具。对工业界，可用于音乐推荐和趋势预测，理解全球音乐风格流动。

## ⚠️ 局限与未解决问题

摘要未提及局限，但可推测：依赖音频特征，可能忽略歌词、视觉等维度；分类器可能受录音质量、制作风格影响；样本量未说明，可能影响统计效力；未提供具体数值，难以评估效应大小。

---

<div class="paper-footer"><span>评分：7.2</span><span>原始：7.2</span><a href="/audio-paper-daily/posts/2026-08-13/">← 返回 2026-08-13 速递</a></div>
