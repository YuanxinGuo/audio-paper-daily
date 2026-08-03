---
title: "Learning to Predict Performance-induced Emotion Differences in Classical Piano Music"
date: 2026-08-03T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#音乐情感识别"]
summary: "本文提出Delta-VA框架，用表演特定特征预测古典钢琴演奏中情感（效价-唤醒）相对平均表演的偏差，并引入几何评估指标。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#音乐情感识别</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#音乐表演分析</span> <span class="tag-pill tag-pill-soft">#情感计算</span> <span class="tag-pill tag-pill-soft">#回归</span> <span class="tag-pill tag-pill-soft">#钢琴音乐</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2607.28876</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-08-03</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2607.28876" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2607.28876" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>本文提出Delta-VA框架，用表演特定特征预测古典钢琴演奏中情感（效价-唤醒）相对平均表演的偏差，并引入几何评估指标。
</div>

## 👥 作者与机构

**Joann Ching** ¹ · Gerhard Widmer

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合音乐信息检索、情感计算方向研究者阅读。可重点看第3节方法（特征编码与Delta-VA框架）和第4节实验（几何评估指标）。若关注表演分析，值得通读；若仅关注情感识别，可略读。

## 🌍 研究背景

音乐情感感知受作曲和表演双重影响，现有研究多关注作曲层面，忽略表演差异。本文针对古典钢琴独奏，使用巴赫平均律的6个商业录音，通过仅编码表演特定特征来隔离表演信息，旨在预测由表演引起的细微情感变化。

## 💡 核心创新

1. 提出Delta-VA相对回归框架，预测相对平均表演的效价-唤醒偏差
2. 引入几何评估指标，衡量表演间成对差异的保持
3. 使用表演特定特征编码，隔离作曲信息
4. 在真实商业录音上验证特征有效性

## 🏗️ 模型架构

输入为音频的表演特定特征（如速度、力度等），通过编码器提取特征，然后使用回归模型（如线性回归或神经网络）预测效价和唤醒的偏差值（Delta-VA）。模型输出为相对平均表演的偏差，而非绝对情感值。

## 📚 数据集

- Bach Well-Tempered Clavier Book I（6个商业录音，用于训练和评估）

## 📊 实验结果

摘要未提供具体数值结果，仅提及高方向一致性和预测幅度压缩，表明模型低估表演效果。

## 🎯 结论与影响

本文提出Delta-VA框架，成功预测表演引起的情感偏差，但存在预测压缩问题。该工作为表演分析提供新视角，可能促进个性化音乐推荐和表演教学。

## ⚠️ 局限与未解决问题

摘要未提及局限，但可推测：数据集规模小（仅6个录音），可能缺乏泛化性；未报告具体指标数值；未与其他方法对比；预测压缩问题未解决。

---

<div class="paper-footer"><span>评分：6.8</span><span>原始：6.8</span><a href="/audio-paper-daily/posts/2026-08-03/">← 返回 2026-08-03 速递</a></div>
