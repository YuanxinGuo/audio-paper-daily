---
title: "Longest Filled Common Subsequence for Song Identification from Degraded Audio via Construct--Merge--Solve--Adapt Optimization"
date: 2026-08-15T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#音频处理"]
summary: "本文提出自适应CMSA框架求解NP难的LFCS问题，在大规模实例上达到SOTA，并首次将LFCS应用于歌曲识别，但音频实验较初步。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero">
<div class="hero-score">
<div class="score-num">6.5</div>
<div class="score-stars">★★★☆☆</div>
<div class="score-tier">前50%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#音频处理</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#最长填充公共子序列</span> <span class="tag-pill tag-pill-soft">#组合优化</span> <span class="tag-pill tag-pill-soft">#歌曲识别</span> <span class="tag-pill tag-pill-soft">#CMSA</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2509.12261</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-08-15</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2509.12261" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2509.12261" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>本文提出自适应CMSA框架求解NP难的LFCS问题，在大规模实例上达到SOTA，并首次将LFCS应用于歌曲识别，但音频实验较初步。
</div>

## 👥 作者与机构

**Marko Djukanovic** ¹ · Christian Blum · Aleksandar Kartelj · Ana Nikolikj · Guenther Raidl

**机构**：奥地利科学与技术研究所 · 贝尔格莱德大学 · 马德里理工大学 · 维也纳工业大学

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合对组合优化或音频指纹识别感兴趣的读者。可重点阅读第4节（CMSA框架）和第6节（歌曲识别应用）。若关注音频应用，可先看第6节；若关注算法优化，可通读全文。

## 🌍 研究背景

LFCS问题在生物信息学中有重要应用，但现有算法主要在小实例上评估，缺乏大规模基准。本文旨在解决大规模实例的可扩展性问题，并探索LFCS在歌曲识别中的新应用。

## 💡 核心创新

1. 引入大规模LFCS基准数据集，弥补现有数据集区分度不足
2. 提出自适应CMSA框架，通过组件构建和反馈迭代生成子问题
3. 首次将LFCS应用于歌曲识别，基于真实音乐能量谱
4. 进行可解释性分析，揭示影响算法性能的关键特征
5. 在98.4%的已知最优实例上达到最优，显著提升可扩展性

## 🏗️ 模型架构

采用自适应CMSA框架：首先通过组件构建生成候选子问题，然后使用外部黑盒求解器求解子问题，并根据求解结果反馈调整后续构建过程。该框架迭代进行，直至满足终止条件。

## 📚 数据集

- 标准LFCS基准（评估）
- 新引入的大规模LFCS实例（评估）
- 真实音乐能量谱实例（歌曲识别应用）

## 📊 实验结果

摘要未提供具体数值指标，但提及在1,510个已知最优实例中，方法在1,486个上达到最优（98.4%），优于四种现有方法。歌曲识别应用仅作为工程贡献提出，未给出详细实验结果。

## 🎯 结论与影响

本文提出的自适应CMSA框架显著提升了LFCS问题的可扩展性，并在大规模实例上达到SOTA。首次将LFCS应用于歌曲识别，展示了组合优化方法在音频领域的潜力。对后续研究而言，该基准和框架可作为大规模LFCS求解的参考，并可能启发更多音频应用。

## ⚠️ 局限与未解决问题

歌曲识别部分仅为初步应用，缺乏与现有音频指纹方法的对比和详细评估。音频实验未提供识别准确率等指标，且未讨论计算效率。此外，LFCS在音频中的适用性可能受限于能量谱表示，未考虑噪声和失真等实际因素。

---

<div class="paper-footer"><span>评分：6.5</span><span>原始：6.5</span><a href="/audio-paper-daily/posts/2026-08-15/">← 返回 2026-08-15 速递</a></div>
