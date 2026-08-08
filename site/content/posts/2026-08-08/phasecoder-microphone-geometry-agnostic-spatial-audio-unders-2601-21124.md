---
title: "PhaseCoder: Microphone Geometry-Agnostic Spatial Audio Understanding for Multimodal LLMs"
date: 2026-08-08T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#空间音频理解"]
summary: "PhaseCoder 提出一种与麦克风几何无关的 Transformer 空间音频编码器，生成空间音频令牌，使多模态 LLM 能进行空间推理和定向转录。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero">
<div class="hero-score">
<div class="score-num">8.2</div>
<div class="score-stars">★★★★☆</div>
<div class="score-tier">前25%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#空间音频理解</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#多模态大模型</span> <span class="tag-pill tag-pill-soft">#声源定位</span> <span class="tag-pill tag-pill-soft">#麦克风阵列</span> <span class="tag-pill tag-pill-soft">#空间音频</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2601.21124</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-08-08</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2601.21124" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2601.21124" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>PhaseCoder 提出一种与麦克风几何无关的 Transformer 空间音频编码器，生成空间音频令牌，使多模态 LLM 能进行空间推理和定向转录。
</div>

## 👥 作者与机构

**Artem Dementyev** ¹ · Wazeer Zulfikar · Sinan Hersek · Pascal Getreuer · Anurag Kumar · Vivek Kumar

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合从事多模态 LLM、空间音频、声源定位的研究者。建议重点阅读方法部分（PhaseCoder 架构）和实验部分（定位基准与 LLM 推理结果）。可先看摘要和结论，再深入方法细节。

## 🌍 研究背景

当前多模态 LLM 通常将音频处理为单声道流，忽略空间信息，限制了具身 AI 的应用。现有空间音频模型受限于固定麦克风几何，难以部署到不同设备。本文旨在解决这一问题，提出一种与麦克风几何无关的空间音频编码器，使 LLM 能够理解空间音频并执行复杂空间推理任务。

## 💡 核心创新

1. 提出 PhaseCoder，一种纯 Transformer 空间音频编码器，输入原始多通道音频和麦克风坐标，输出空间嵌入。
2. 实现麦克风几何无关性，可适应任意麦克风阵列。
3. 首次将空间音频令牌集成到多模态 LLM（Gemma 3n）中，实现空间推理和定向转录。
4. 在麦克风不变定位基准上达到 SOTA 结果。

## 🏗️ 模型架构

PhaseCoder 采用纯 Transformer 架构。输入为原始多通道音频和麦克风坐标，通过位置编码融合几何信息，经多层 Transformer 编码器处理，输出空间音频令牌（spatial embeddings）。这些令牌可输入多模态 LLM（如 Gemma 3n）进行微调，以执行空间推理和定向转录。

## 📊 实验结果

摘要未提供具体数值指标，但声称在麦克风不变定位基准上达到 SOTA，并首次使 LLM 能进行复杂空间推理和定向转录。具体性能需查阅论文。

## 🎯 结论与影响

PhaseCoder 提出了一种与麦克风几何无关的空间音频编码器，使多模态 LLM 能够理解空间音频，实现空间推理和定向转录。这一方法有望推动具身 AI 和空间音频理解的发展，为多模态 LLM 提供更丰富的音频信息。

## ⚠️ 局限与未解决问题

摘要未提及局限。可能存在的问题包括：未提供具体性能数值，缺乏与现有方法的详细对比；未讨论计算复杂度和推理延迟；未说明对麦克风数量或类型的限制；未展示在真实场景中的泛化能力。

---

<div class="paper-footer"><span>评分：8.2</span><span>原始：8.2</span><a href="/audio-paper-daily/posts/2026-08-08/">← 返回 2026-08-08 速递</a></div>
