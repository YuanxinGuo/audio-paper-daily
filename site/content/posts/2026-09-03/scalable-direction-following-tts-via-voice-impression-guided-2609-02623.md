---
title: "Scalable Direction-Following TTS via Voice Impression-Guided Pseudo Triplet Construction"
date: 2026-09-03T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#语音合成"]
summary: "提出一种可扩展的伪三元组构建流程，利用印象可控TTS和LLM生成方向跟随TTS训练数据，实现说话人保持的风格修改。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#语音合成</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#语音合成</span> <span class="tag-pill tag-pill-soft">#风格控制</span> <span class="tag-pill tag-pill-soft">#数据增强</span> <span class="tag-pill tag-pill-soft">#LLM</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2609.02623</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-09-03</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner"><div class="oc-headline"><span class="oc-pulse"></span><span class="oc-title">本论文已开源</span><span class="oc-hint">点击下方卡片直达对应资源</span></div><div class="oc-grid"><a class="oc-chip oc-chip-proj" href="https://ntt-hilab-gensp.github.io/IS2026pseudo/" target="_blank" rel="noopener"><span class="oc-icon">🌐</span><span class="oc-text"><span class="oc-label">项目主页</span><span class="oc-sub">ntt-hilab-gensp.github.io/IS2026pseudo/</span></span></a><a class="oc-chip oc-chip-demo" href="https://ntt-hilab-gensp.github.io/IS2026pseudo/" target="_blank" rel="noopener"><span class="oc-icon">🔊</span><span class="oc-text"><span class="oc-label">在线 Demo</span><span class="oc-sub">ntt-hilab-gensp.github.io/IS2026pseudo/</span></span></a></div></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2609.02623" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2609.02623" target="_blank" rel="noopener">📑 PDF</a><a class="rsrc rsrc-proj" href="https://ntt-hilab-gensp.github.io/IS2026pseudo/" target="_blank" rel="noopener">🌐 项目主页</a><a class="rsrc rsrc-demo" href="https://ntt-hilab-gensp.github.io/IS2026pseudo/" target="_blank" rel="noopener">🔊 Demo</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出一种可扩展的伪三元组构建流程，利用印象可控TTS和LLM生成方向跟随TTS训练数据，实现说话人保持的风格修改。
</div>

## 👥 作者与机构

**Kenichi Fujita** ¹ · Yusuke Ijima

**机构**：日本电报电话公司

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合语音合成、风格控制方向的研究者阅读。建议重点看第3节的伪三元组构建流程和第4节的实验对比。可先看摘要和结论，再深入方法部分。

## 🌍 研究背景

方向跟随TTS要求系统根据自然语言指令调整参考话语的说话风格，同时保持说话人身份和内容。该任务面临训练数据稀缺的挑战，因为需要成对的参考和修改后话语。现有方法依赖人工录制，成本高且难以扩展。本文旨在通过自动构建伪三元组来解决数据瓶颈，利用可控TTS和LLM生成自然语言方向描述。

## 💡 核心创新

1. 提出可扩展的伪三元组构建流程，无需人工标注
2. 利用印象可控TTS生成风格变体，LLM生成方向文本
3. 结合伪数据和真实数据训练，提升方向对齐和说话人相似度

## 🏗️ 模型架构

输入为参考话语和方向文本，通过编码器提取说话人嵌入和内容特征，方向文本经文本编码器处理，融合后送入基于Transformer的解码器生成语音。训练数据由伪三元组构建流程生成：使用印象可控TTS（如基于风格控制的条件生成模型）生成风格变体，并用LLM根据估计的印象差异生成方向文本。

## 📚 数据集

- 内部数据集（用于训练和评估，具体规模未提及）

## 📊 实验结果

摘要未提供具体数值指标，但实验表明仅用伪三元组即可实现稳定的说话人保持修改，结合真实数据可进一步提升方向对齐和说话人相似度。

## 🎯 结论与影响

本文提出了一种可扩展的伪三元组构建方法，有效解决了方向跟随TTS数据稀缺问题。该方法有望推动个性化语音合成和配音应用的发展，降低数据采集成本。

## ⚠️ 局限与未解决问题

摘要未提及局限，但可能包括：伪数据与真实数据分布差异、LLM生成方向文本的准确性、以及缺乏客观指标评估。

## 🔗 开源资源

- **项目主页**：<https://ntt-hilab-gensp.github.io/IS2026pseudo/>
- **Demo / 试听**：<https://ntt-hilab-gensp.github.io/IS2026pseudo/>

---

<div class="paper-footer"><span>评分：7.2</span><span>原始：7.2</span><a href="/audio-paper-daily/posts/2026-09-03/">← 返回 2026-09-03 速递</a></div>
