---
title: "Rethinking Language Model-Based Generative Speech Enhancement in the Latent Space of a Neural Audio Codec"
date: 2026-08-14T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#语音增强"]
summary: "本文统一了六种基于语言模型的生成式语音增强范式，首次在统一实验设置下比较，并提出辅助损失微调策略提升主客观指标。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero hero-focus">
<div class="hero-score">
<div class="score-num">9.2</div>
<div class="score-stars">★★★★★</div>
<div class="score-tier">前25%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#语音增强</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#语音增强</span> <span class="tag-pill tag-pill-soft">#语言模型</span> <span class="tag-pill tag-pill-soft">#神经音频编解码器</span> <span class="tag-pill tag-pill-soft">#生成式模型</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2608.12082</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-08-14</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
<div class="meta-row"><span class="meta-key">⭐</span><span class="meta-val focus-badge">本站重点关注领域 · 评分 +1</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2608.12082" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2608.12082" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>本文统一了六种基于语言模型的生成式语音增强范式，首次在统一实验设置下比较，并提出辅助损失微调策略提升主客观指标。
</div>

## 👥 作者与机构

**Yihui Fu** ¹ · Zhengyang Li · Tim Fingscheidt

**机构**：布伦瑞克工业大学

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合语音增强和生成式音频建模研究者阅读。建议重点阅读第3节（统一框架）和第4节（实验对比），尤其是表2和表3。可先看摘要和结论，再深入方法细节。

## 🌍 研究背景

基于语言模型（LM）的语音增强（SE）方法近期利用神经音频编解码器（NAC）的潜在特征快速发展。然而，现有研究分散在不同范式（如自回归、非自回归、扩散、流匹配），缺乏统一框架和公平比较。本文旨在统一这些范式，并在相同实验条件下评估其性能，同时提出改进策略。

## 💡 核心创新

1. 提出统一框架，涵盖六种LM-based生成式SE范式
2. 首次在统一实验设置下比较离散/连续潜在特征范式
3. 提出辅助损失微调策略，提升主客观指标
4. 实验证明连续域范式优于离散域，CNAR最佳
5. 辅助损失策略在六种范式上一致提升DNSMOS等指标

## 🏗️ 模型架构

输入为含噪语音的NAC潜在特征（离散或连续），主干为语言模型（如Transformer）或非自回归模型，关键模块包括自回归/非自回归生成、扩散模型、流匹配。输出为增强语音的潜在表示，经NAC解码器重建语音。辅助损失在重建语音上计算，用于微调。

## 📚 数据集

- URGENT 2025 Speech Enhancement Challenge data splits（训练和评估）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| DNSMOS | URGENT 2025 | 未明确给出具体值 | **提升（具体值未给出）** | 一致提升 |
| NISQA | URGENT 2025 | 未明确给出具体值 | **提升（具体值未给出）** | 一致提升 |
| PESQ | URGENT 2025 | 未明确给出具体值 | **提升（具体值未给出）** | 一致提升 |
| POLQA | URGENT 2025 | 未明确给出具体值 | **提升（具体值未给出）** | 一致提升 |

实验在URGENT 2025数据集上进行，所有连续域范式（CAR, CNAR, CFM）在多个指标上优于离散域范式（DAR, DNAR, DDiff）。其中CNAR（连续非自回归）表现最佳。提出的辅助损失微调策略在六种范式上一致提升了DNSMOS、NISQA、PESQ和POLQA，表明该策略具有通用性。

## 🎯 结论与影响

本文首次统一并比较了六种基于LM的生成式语音增强范式，证明连续域方法优于离散域，且CNAR为最佳。辅助损失微调策略能有效提升主客观指标，为后续研究提供了基准和优化方向。对工业应用而言，连续域方法可能更实用，但需权衡计算复杂度。

## ⚠️ 局限与未解决问题

摘要未提供具体数值，仅定性描述，缺乏定量对比。未提及模型参数量、推理延迟等效率指标。未进行跨数据集泛化测试。辅助损失策略的消融实验未详细说明。

---

<div class="paper-footer"><span>评分：9.2</span><span>原始：8.2</span><span>+1 重点领域加权</span><a href="/audio-paper-daily/posts/2026-08-14/">← 返回 2026-08-14 速递</a></div>
