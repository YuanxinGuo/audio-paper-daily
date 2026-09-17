---
title: "Scalable Music Cover Retrieval Using Lyrics-Aligned Audio Embeddings"
date: 2026-09-17T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#音乐信息检索"]
summary: "LIVI 用歌词对齐的音频嵌入做翻唱检索，训练时借助转录与文本嵌入监督，推理时去掉转录步骤，兼顾精度与效率。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#音乐信息检索</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#翻唱识别</span> <span class="tag-pill tag-pill-soft">#歌词对齐</span> <span class="tag-pill tag-pill-soft">#音频嵌入</span> <span class="tag-pill tag-pill-soft">#多模态</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2601.11262</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-09-17</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2601.11262" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2601.11262" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>LIVI 用歌词对齐的音频嵌入做翻唱检索，训练时借助转录与文本嵌入监督，推理时去掉转录步骤，兼顾精度与效率。
</div>

## 👥 作者与机构

**Joanne Affolter** ¹ · Benjamin Martin · Elena V. Epure · Gabriel Meseguer-Brocal · Fr\'ed\'eric Kaplan

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合做音乐检索、版权识别、跨版本匹配的研究者与工程团队阅读。建议重点看 §3 的 LIVI 训练框架与推理简化设计，以及表 2 的精度-效率对比；若关注工业部署，可先看效率指标与消融部分。

## 🌍 研究背景

翻唱检索（Version Identification）此前以和声与旋律特征为主，SOTA 方法如基于 chroma 或深度和声嵌入的管线虽有效，但训练与推理开销大，且对翻唱中变化剧烈的音乐属性需大量不变性设计。歌词是翻唱间强不变量，但多声部音频中歌词提取困难，早期方法框架简单导致性能受限，近期多模态系统又依赖大模型与复杂架构。本文要解决的是：如何在保持检索精度的同时，用歌词信息构建轻量高效的翻唱检索方案。

## 💡 核心创新

1. 训练时用 SOTA 转录与文本嵌入模型提供歌词监督
2. 推理时移除转录步骤，仅用音频嵌入检索
3. 以歌词对齐嵌入替代复杂和声管线，降低计算量
4. 在精度与效率间取得平衡，挑战复杂管线主导地位

## 🏗️ 模型架构

LIVI（Lyrics-Informed Version Identification）输入为音频，训练阶段先由 SOTA 自动转录模型提取歌词，再用文本嵌入模型生成歌词嵌入，与音频编码器输出对齐，形成歌词对齐的音频嵌入；推理阶段去掉转录与文本分支，仅保留音频编码器输出嵌入用于检索。摘要未给出具体主干网络名与参数量，整体设计强调轻量与高效，避免复杂多模态大模型。

## 📊 实验结果

摘要未给出具体数据集名称与数值指标，仅声称 LIVI 的检索精度与和声基系统相当或更优，且推理时无需转录步骤，保持轻量高效。缺少与具体 baseline 的数值对比、消融实验与效率指标（如推理延迟、参数量），无法量化验证其效率优势。

## 🎯 结论与影响

LIVI 表明歌词对齐的音频嵌入可在不牺牲检索精度的前提下替代复杂和声管线，推理时去掉转录步骤进一步降低开销。若结论成立，将推动翻唱检索向轻量多模态方向演进，对版权识别与曲库管理的工业部署有直接价值，尤其适合算力受限场景。

## ⚠️ 局限与未解决问题

摘要未提供具体数据集、指标数值与 baseline 对比，无法判断精度是否真达 SOTA；缺少消融验证歌词监督与推理简化各自的贡献；未报告推理延迟、参数量等效率指标；歌词转录在纯音乐或非英语曲目上的鲁棒性未讨论。

---

<div class="paper-footer"><span>评分：6.8</span><span>原始：6.8</span><a href="/audio-paper-daily/posts/2026-09-17/">← 返回 2026-09-17 速递</a></div>
