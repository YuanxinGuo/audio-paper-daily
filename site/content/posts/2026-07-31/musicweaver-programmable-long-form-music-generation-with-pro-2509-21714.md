---
title: "MusicWeaver: Programmable Long-Form Music Generation with Provably Local Editing"
date: 2026-07-31T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#音乐生成"]
summary: "MusicWeaver 将音乐生成重构为程序引导的生成，通过显式计划层实现可编辑的长格式音乐生成，并保证局部编辑的精确性。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero">
<div class="hero-score">
<div class="score-num">8.5</div>
<div class="score-stars">★★★★☆</div>
<div class="score-tier">前10%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#音乐生成</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#程序化生成</span> <span class="tag-pill tag-pill-soft">#扩散模型</span> <span class="tag-pill tag-pill-soft">#局部编辑</span> <span class="tag-pill tag-pill-soft">#音乐结构</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2509.21714</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-07-31</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">🔥 强烈推荐通读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2509.21714" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2509.21714" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>MusicWeaver 将音乐生成重构为程序引导的生成，通过显式计划层实现可编辑的长格式音乐生成，并保证局部编辑的精确性。
</div>

## 👥 作者与机构

**Xuanchen Wang** ¹ · Heng Wang · Weidong Cai

**机构**：悉尼大学

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合音乐生成、可控生成和扩散模型研究者阅读。建议重点阅读第3节（计划表示与编辑代数）和第4节（Projected Diffusion Inpainting 与 Global-Local Diffusion Transformer）。可先看图1和表2以快速了解框架和效果。

## 🌍 研究背景

现有音乐生成系统（如 MusicLM、AudioLDM）能生成逼真音频，但缺乏结构控制，用户只能通过文本提示间接控制形式，局部修改需重新生成整段。这限制了创作中的迭代编辑。本文提出程序引导生成，将音乐创作视为程序执行，通过显式计划层连接意图与音频，实现可编辑的长格式音乐生成。

## 💡 核心创新

1. 提出程序引导生成范式，用多级歌曲程序编码音乐结构
2. 形式化编辑为类型化计划操作代数，证明保持计划有效性
3. 提出 Projected Diffusion Inpainting 保证编辑区间外音频精确保留
4. 设计 Global-Local Diffusion Transformer 与 Motif Memory Retrieval 实现分钟级计划执行
5. 支持计划归纳和自然语言编辑，编译指令为操作序列

## 🏗️ 模型架构

MusicWeaver 分为规划与渲染两阶段。规划阶段预测多级歌曲程序，编码音乐形式、主题重复和节拍属性。渲染阶段基于计划合成音频，采用 Global-Local Diffusion Transformer，结合 Motif Memory Retrieval 处理长计划并生成一致且变化的段落回归。编辑通过 Projected Diffusion Inpainting 实现，保证编辑区间外音频精确不变。

## 📊 实验结果

摘要未提供具体数值指标，但声称在文本、视频及其组合条件下生成的结构连贯性和可编辑性达到 SOTA，且编辑质量在连续修订中保持稳定，而先前方法会退化。

## 🎯 结论与影响

MusicWeaver 通过程序引导生成实现了可编辑的长格式音乐生成，显著提升了结构连贯性和编辑保真度。该工作为音乐生成提供了新的可控性范式，有望推动交互式创作工具的发展，并可能影响其他生成领域（如语音、音效）的结构化编辑。

## ⚠️ 局限与未解决问题

摘要未提及局限，但可推测：计划归纳可能受限于录音质量；编辑操作代数可能无法覆盖所有音乐编辑需求；Projected Diffusion Inpainting 可能对长跨度编辑效率不高；实验未报告计算开销或推理延迟。

---

<div class="paper-footer"><span>评分：8.5</span><span>原始：8.5</span><a href="/audio-paper-daily/posts/2026-07-31/">← 返回 2026-07-31 速递</a></div>
