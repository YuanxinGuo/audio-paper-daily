---
title: "Pitch Contour Tokenization using VQ-VAE and Its Application on Korean Traditional Music Analysis"
date: 2026-08-13T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#音乐分析"]
summary: "本文提出用VQ-VAE从无标注音频中学习音高轮廓的离散词汇，并应用于韩国传统音乐分析，无需监督即可恢复专家定义的sigimsae类别和pansori调式信息。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#音乐分析</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#VQ-VAE</span> <span class="tag-pill tag-pill-soft">#音高轮廓</span> <span class="tag-pill tag-pill-soft">#韩国传统音乐</span> <span class="tag-pill tag-pill-soft">#无监督学习</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2608.10979</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-08-13</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2608.10979" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2608.10979" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>本文提出用VQ-VAE从无标注音频中学习音高轮廓的离散词汇，并应用于韩国传统音乐分析，无需监督即可恢复专家定义的sigimsae类别和pansori调式信息。
</div>

## 👥 作者与机构

**Seonguk Ju** ¹ · Seola Cho · Sooin Chung · Danbinaerin Han · Dasaem Jeong

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合音乐信息检索、计算音乐学及自监督语音/音频表示学习研究者阅读。建议重点阅读第3节方法部分（对齐不变训练）和第4节实验（sigimsae与pansori分析）。可先看摘要和结论，再深入方法细节。

## 🌍 研究背景

计算音乐分析常依赖离散表示，但许多音乐传统以连续音高运动为组织方式，难以分割成音符单元。现有方法通常需要预先定义音符或使用监督数据，不适用于此类传统。本文旨在从无标注音频中学习局部音高轮廓的离散词汇，为轮廓中心音乐传统的语料库级分析提供基础单元。

## 💡 核心创新

1. 提出VQ-VAE量化固定长度音高轮廓段，学习离散码本
2. 训练时在候选时域和音高域变换中寻找最佳对齐，增强稳定性
3. 无监督学习到的token能恢复专家定义的sigimsae类别
4. 在pansori中token与两种主要调式（界面调、羽调）对齐
5. 为轮廓中心音乐传统提供语料库级分析单元

## 🏗️ 模型架构

输入为固定长度的音高轮廓段（可能从音频提取的F0序列），通过VQ-VAE编码器映射到连续潜在表示，再经向量量化层映射到最近码本向量，解码器重建原始轮廓。训练时，重建损失在候选时域平移和音高平移变换中取最佳对齐，以增强对分割位置和时序/音高变化的鲁棒性。

## 📚 数据集

- 韩国传统音乐音频数据集（训练/评估，具体规模未提及）

## 📊 实验结果

摘要未提供具体数值指标，但定性结果表明：学习到的token能无监督地恢复专家定义的sigimsae类别，且在pansori中与两种主要调式对齐，支持其作为语料库级分析单元。

## 🎯 结论与影响

本文提出了一种从无标注音频学习音高轮廓离散词汇的方法，在韩国传统音乐中验证了其有效性，无需监督即可恢复专家知识。该方法为轮廓中心音乐传统的计算分析提供了新工具，有望推动相关领域的语料库研究，并对音乐信息检索和计算音乐学有潜在影响。

## ⚠️ 局限与未解决问题

摘要未提及局限，但可能包括：未与其他离散表示方法对比；未评估token在分类任务中的量化性能；未讨论码本大小和轮廓长度的影响；未在更多音乐传统上验证泛化性。

---

<div class="paper-footer"><span>评分：7.2</span><span>原始：7.2</span><a href="/audio-paper-daily/posts/2026-08-13/">← 返回 2026-08-13 速递</a></div>
