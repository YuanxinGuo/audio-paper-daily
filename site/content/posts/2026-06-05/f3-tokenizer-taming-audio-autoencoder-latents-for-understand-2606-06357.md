---
title: "F3-Tokenizer: Taming Audio Autoencoder Latents for Understanding and Generation"
date: 2026-06-05T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#音频表征学习"]
summary: "提出F3-Tokenizer，通过噪声正则化瓶颈和潜在表示编码器，统一音频理解与生成的连续潜在表示。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#音频表征学习</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#音频编解码</span> <span class="tag-pill tag-pill-soft">#自监督学习</span> <span class="tag-pill tag-pill-soft">#音频生成</span> <span class="tag-pill tag-pill-soft">#音频理解</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2606.06357</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-06-05</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2606.06357" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2606.06357" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出F3-Tokenizer，通过噪声正则化瓶颈和潜在表示编码器，统一音频理解与生成的连续潜在表示。
</div>

## 👥 作者与机构

**Dinghao Zhou** ¹ · Xingchen Song · Di Wu · Pengyu Cheng · Shengfan Shen · Sixiang Lv

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合音频表征学习、自监督学习和生成模型研究者。建议重点阅读§3.1瓶颈设计和§3.2表示编码器，以及表2的对比实验。可先看§1引言了解动机。

## 🌍 研究背景

连续音频自编码器能高质量重建波形，但潜在表示缺乏语义结构，不利于理解任务；自监督音频编码器捕获语义但不可解码。现有方法难以用一个统一的音频分词器同时支持理解和生成。本文旨在设计一种既能提供高维语义表示用于理解，又能保持连续潜在作为生成目标的音频分词器。

## 💡 核心创新

1. 噪声正则化瓶颈：通道归一化+随机扰动替代KL变分训练
2. 潜在侧表示编码器：基于RQ-MTP和冻结LLM监督训练
3. 统一连续潜在表示：同时支持重建和自回归生成

## 🏗️ 模型架构

输入波形经连续音频自编码器编码器得到潜在表示，通过噪声正则化瓶颈（通道归一化+随机扰动）输出尺度可控的连续潜在，用于重建和自回归生成。同时，潜在侧表示编码器（基于RQ-MTP）在冻结的自编码器潜在上训练，受冻结LLM监督，输出高维离散表示用于理解任务。

## 📊 实验结果

摘要未提供具体实验数值，但声称该方法在理解任务上优于连续潜在基线，在生成任务上保持重建质量。

## 🎯 结论与影响

F3-Tokenizer通过噪声正则化瓶颈和表示编码器，有效统一了音频理解与生成的潜在表示，为构建单一音频分词器提供了新思路。未来可探索更高效的表示编码器设计，并应用于更大规模的多任务学习。

## ⚠️ 局限与未解决问题

摘要未报告具体指标和对比基线，缺乏定量验证；未讨论推理效率；表示编码器依赖冻结LLM，可能引入额外计算开销。

---

<div class="paper-footer"><span>评分：7.8</span><span>原始：7.8</span><a href="/audio-paper-daily/posts/2026-06-05/">← 返回 2026-06-05 速递</a></div>
