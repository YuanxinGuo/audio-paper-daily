---
title: "Synaspot: A Lightweight, Streaming Multi-modal Framework for Keyword Spotting with Audio-Text Synergy"
date: 2026-08-14T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#关键词唤醒"]
summary: "提出轻量流式多模态关键词唤醒框架，通过去声纹的语音注册和数学解码，在LibriPhase和WenetPrase上以更少参数超越现有流式方法。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#关键词唤醒</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#多模态融合</span> <span class="tag-pill tag-pill-soft">#流式解码</span> <span class="tag-pill tag-pill-soft">#轻量化</span> <span class="tag-pill tag-pill-soft">#语音-文本协同</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2512.15124</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-08-14</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2512.15124" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2512.15124" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出轻量流式多模态关键词唤醒框架，通过去声纹的语音注册和数学解码，在LibriPhase和WenetPrase上以更少参数超越现有流式方法。
</div>

## 👥 作者与机构

**Kewei Li** ¹ · Yinan Zhong · Xiaotao Liang · Tianchi Dai · Shaofei Xue

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合语音唤醒和轻量级多模态模型研究者阅读。建议重点看第3节（方法）和第4节（实验），特别是去声纹注册和流式解码部分。可先看摘要和结论，再深入方法细节。

## 🌍 研究背景

开放词汇关键词唤醒（KWS）在连续语音流中具有重要应用价值。现有方法虽引入多模态提升性能，但参数开销大且难以端到端部署。本文针对多模态集成带来的参数增加和流式部署限制，提出轻量级流式多模态框架，旨在降低参数同时保持性能。

## 💡 核心创新

1. 去声纹注册：减少语音注册中的说话人特定信息，提取与说话人无关的特征
2. 语音-文本融合：有效融合语音和文本特征，提升唤醒准确性
3. 流式解码框架：仅需编码器提取特征，通过数学解码与三种模态表示匹配，实现流式处理

## 🏗️ 模型架构

输入为语音和文本注册特征。语音注册经过去声纹模块提取说话人无关特征，文本注册通过文本编码器得到文本嵌入。主干网络为轻量级编码器（具体结构未详述），提取语音特征后，与三种模态表示（语音注册、文本注册、可能还有联合表示）进行数学解码（如点积或余弦相似度），输出唤醒决策。整体设计支持流式处理，参数高效。

## 📚 数据集

- LibriPhase（评估）
- WenetPrase（评估）

## 📊 实验结果

摘要未提供具体数值，但声称在LibriPhase和WenetPrase上，与现有流式方法相比，本方法以显著更少的参数取得了更好的性能。具体指标未给出，需查阅原文。

## 🎯 结论与影响

本文提出了一种轻量级流式多模态KWS框架，通过去声纹注册和数学解码，在减少参数的同时提升了性能，展示了多模态协同在KWS中的潜力。对后续研究而言，该框架为轻量化多模态KWS提供了新思路，可能推动端侧部署。工业上，低参数和流式特性有利于实时唤醒应用。

## ⚠️ 局限与未解决问题

摘要未提及具体参数减少量和性能提升幅度，缺乏量化对比。未说明模型在噪声或远场条件下的鲁棒性。未提供推理延迟或计算量等效率指标。未与最新非流式方法对比。

---

<div class="paper-footer"><span>评分：7.8</span><span>原始：7.8</span><a href="/audio-paper-daily/posts/2026-08-14/">← 返回 2026-08-14 速递</a></div>
