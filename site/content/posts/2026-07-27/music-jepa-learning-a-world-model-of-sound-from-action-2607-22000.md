---
title: "Music-JEPA: Learning a World Model of Sound from Action"
date: 2026-07-27T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#音乐表示学习"]
summary: "提出Music-JEPA，将钢琴音频视为状态、钢琴卷帘视为动作，通过预测未来音频状态学习音乐世界模型，支持多项下游任务。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#音乐表示学习</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#自监督学习</span> <span class="tag-pill tag-pill-soft">#世界模型</span> <span class="tag-pill tag-pill-soft">#钢琴转录</span> <span class="tag-pill tag-pill-soft">#联合嵌入预测架构</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2607.22000</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-07-27</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2607.22000" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2607.22000" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出Music-JEPA，将钢琴音频视为状态、钢琴卷帘视为动作，通过预测未来音频状态学习音乐世界模型，支持多项下游任务。
</div>

## 👥 作者与机构

**Ziyu Wang** ¹ · Kun Fang · Yann LeCun

**机构**：纽约大学 · Meta

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合对自监督学习、音乐表示学习感兴趣的读者。建议重点阅读§3方法部分和§4实验部分，特别是下游任务评估和规划式转录。可先看摘要和结论了解整体贡献。

## 🌍 研究背景

联合嵌入预测架构（JEPA）在视觉和视频领域已展现出学习世界模型的能力，但在音乐领域的应用尚不明确。现有音乐表示学习方法多依赖对比学习或重构，缺乏对音乐动作与声音因果关系的建模。本文旨在将JEPA扩展到音乐领域，通过将音频视为状态、钢琴卷帘视为动作，学习一个能够预测动作结果的世界模型，从而捕获音乐动作与声音之间的映射关系。

## 💡 核心创新

1. 将音乐建模为动作条件系统，音频为状态、钢琴卷帘为动作
2. 采用JEPA预测未来音频状态的潜在表示，而非原始波形
3. 通过规划实现钢琴转录，搜索最优动作序列解释目标声音

## 🏗️ 模型架构

输入为当前音频片段（状态）和钢琴卷帘（动作），通过编码器提取音频和动作的潜在表示。主干网络采用Transformer架构，预测器根据当前状态和动作的联合表示预测未来状态的潜在表示。训练目标为对比损失，使预测表示与真实未来状态表示接近。模型参数量未在摘要中提及。

## 📚 数据集

- MAESTRO（训练/评估，包含钢琴音频与MIDI对齐数据）

## 📊 实验结果

摘要未提供具体数值结果，但声称模型在下游任务（节拍跟踪、作曲家识别、调性估计）上表现良好，并展示了通过规划进行钢琴转录的能力。

## 🎯 结论与影响

本文提出Music-JEPA，成功将JEPA应用于音乐领域，通过学习动作与声音的因果关系构建世界模型。该方法无需环境交互即可离线训练，为音乐表示学习提供了新范式。未来可扩展到多乐器场景和实时交互应用，对音乐信息检索和智能音乐教育有潜在影响。

## ⚠️ 局限与未解决问题

目前仅针对钢琴单乐器，未验证多乐器或复杂音乐场景；规划式转录的计算效率未讨论；缺乏与现有自监督方法（如CLIP、HuBERT）的定量对比；未报告模型参数量和推理速度。

---

<div class="paper-footer"><span>评分：7.8</span><span>原始：7.8</span><a href="/audio-paper-daily/posts/2026-07-27/">← 返回 2026-07-27 速递</a></div>
