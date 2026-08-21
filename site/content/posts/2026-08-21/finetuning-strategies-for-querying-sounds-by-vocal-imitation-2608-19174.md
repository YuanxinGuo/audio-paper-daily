---
title: "Finetuning Strategies for Querying Sounds by Vocal Imitation"
date: 2026-08-21T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#声音检索"]
summary: "本文提出两种微调策略用于通过声音模仿查询音效，在AES AIMLA 2025挑战赛中获胜。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#声音检索</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#声音事件检索</span> <span class="tag-pill tag-pill-soft">#对比学习</span> <span class="tag-pill tag-pill-soft">#三元组损失</span> <span class="tag-pill tag-pill-soft">#微调</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2608.19174</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-08-21</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2608.19174" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2608.19174" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>本文提出两种微调策略用于通过声音模仿查询音效，在AES AIMLA 2025挑战赛中获胜。
</div>

## 👥 作者与机构

**Aditya Bhattacharjee** ¹ · Christos Plachouras · Sungkyun Chang · Emmanouil Benetos

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合从事声音检索、多模态学习的研究者阅读。可重点看第3节（方法）和第4节（实验），了解对比学习和三元组损失的结合方式。若对挑战赛细节感兴趣，可通读全文。

## 🌍 研究背景

声音检索是音频信息检索的重要方向，通过声音模仿查询音效具有自然交互的优势。现有方法多采用预训练编码器加微调，但微调策略对性能影响显著。本文针对AES AIMLA 2025挑战赛，探索两种微调策略：冻结CED编码器的对比学习和MobileNetV3的联合对比-三元组学习，以提升检索准确率。

## 💡 核心创新

1. 冻结CED编码器进行对比学习微调
2. 联合对比-三元组损失与半硬负样本挖掘
3. 在挑战赛中取得第一名
4. 系统分析两种微调策略的互补性

## 🏗️ 模型架构

输入为声音模仿音频和音效音频，分别通过编码器提取特征。策略一：使用冻结的预训练CED编码器，仅训练对比学习头。策略二：使用MobileNetV3编码器，联合优化对比损失和三元组损失，并采用半硬负样本挖掘。输出为嵌入向量，通过相似度匹配实现检索。

## 📚 数据集

- AES AIMLA 2025 Challenge数据集（训练/评估）

## 📊 实验结果

摘要未提供具体数值，但提及在挑战赛中获胜，表明所提策略优于其他参赛方法。未报告消融实验或跨数据集泛化结果。

## 🎯 结论与影响

本文提出的两种微调策略在声音模仿检索任务上表现优异，赢得挑战赛。工作展示了冻结预训练编码器与联合损失训练的有效性，为后续研究提供了新思路。对工业界音效检索应用具有潜在价值。

## ⚠️ 局限与未解决问题

摘要未提供详细实验对比，缺乏与现有方法的定量比较。未讨论推理效率或模型复杂度。未提及失败案例或局限性。

---

<div class="paper-footer"><span>评分：7.2</span><span>原始：7.2</span><a href="/audio-paper-daily/posts/2026-08-21/">← 返回 2026-08-21 速递</a></div>
