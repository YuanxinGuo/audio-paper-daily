---
title: "Refining Pseudo-Audio Prompts with Speech-Text Alignment for Text-Only Domain Adaptation in LLM-Based ASR"
date: 2026-05-15T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#语音识别"]
summary: "提出一种利用语音-文本对齐增强伪音频提示的方法，用于基于LLM的ASR的文本领域自适应。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero">
<div class="hero-score">
<div class="score-num">7.5</div>
<div class="score-stars">★★★★☆</div>
<div class="score-tier">前25%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#语音识别</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#领域自适应</span> <span class="tag-pill tag-pill-soft">#文本到音频提示</span> <span class="tag-pill tag-pill-soft">#大语言模型</span> <span class="tag-pill tag-pill-soft">#语音文本对齐</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2605.14340</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-05-15</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2605.14340" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2605.14340" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出一种利用语音-文本对齐增强伪音频提示的方法，用于基于LLM的ASR的文本领域自适应。
</div>

## 👥 作者与机构

**Ryo Magoshi** ¹ · Takashi Maekaku · Yusuke Shinohara

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合从事ASR领域自适应、LLM-based ASR的研究者阅读。建议重点读§3方法部分和§4实验部分，特别是伪音频提示生成和对齐模块的设计。

## 🌍 研究背景

基于LLM的ASR模型通过连接音频编码器和LLM表现出色，但配对语音-文本数据稀缺限制了其领域自适应。现有方法要么仅微调LLM忽略声学上下文，要么使用伪音频提示但存在数据稀缺下可扩展性差或提示表达力不足的问题。本文旨在通过显式建模语音-文本对齐来生成高表达力的伪音频提示，弥合模态差距。

## 💡 核心创新

1. 提出语音-文本对齐模块增强伪音频提示生成
2. 利用文本数据高效生成高表达力伪音频提示
3. 在数据稀缺条件下提升领域自适应性能

## 🏗️ 模型架构

输入为文本转录，通过文本编码器提取特征，再经语音-文本对齐模块（可能基于对比学习或跨注意力）生成伪音频嵌入，该嵌入与音频编码器输出对齐后输入LLM进行ASR解码。整体框架包括预训练的音频编码器、LLM和可训练的对齐模块。

## 📚 数据集

- 目标领域文本数据（用于训练对齐模块）
- 源领域配对语音-文本数据（用于预训练）

## 📊 实验结果

摘要未提供具体数值，但声称方法在整体错误率和词汇外覆盖率上优于现有文本领域自适应方法。

## 🎯 结论与影响

本文提出的语音-文本对齐增强伪音频提示方法有效提升了LLM-based ASR在目标领域的自适应性能，为数据稀缺场景下的领域自适应提供了新思路。未来可探索更高效的对齐机制和跨语言应用。

## ⚠️ 局限与未解决问题

摘要未提及具体局限，可能包括：对齐模块的额外计算开销、对文本数据质量的依赖、未在多种语言或噪声环境下验证。

---

<div class="paper-footer"><span>评分：7.5</span><span>原始：7.5</span><a href="/audio-paper-daily/posts/2026-05-15/">← 返回 2026-05-15 速递</a></div>
