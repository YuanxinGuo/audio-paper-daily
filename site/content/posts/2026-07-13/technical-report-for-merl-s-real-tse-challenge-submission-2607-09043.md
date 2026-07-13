---
title: "Technical Report for MERL's Real-TSE Challenge Submission"
date: 2026-07-13T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#目标说话人提取"]
summary: "MERL在Real-TSE挑战赛中通过精心数据准备和四阶段训练，在远场嘈杂混响条件下取得第一名，并揭示了DNSMOS和说话人相似度指标的脆弱性。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero hero-focus">
<div class="hero-score">
<div class="score-num">8.5</div>
<div class="score-stars">★★★★☆</div>
<div class="score-tier">前25%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#目标说话人提取</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#语音增强</span> <span class="tag-pill tag-pill-soft">#数据准备</span> <span class="tag-pill tag-pill-soft">#远场</span> <span class="tag-pill tag-pill-soft">#Real-TSE</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2607.09043</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-07-13</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
<div class="meta-row"><span class="meta-key">⭐</span><span class="meta-val focus-badge">本站重点关注领域 · 评分 +1</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2607.09043" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2607.09043" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>MERL在Real-TSE挑战赛中通过精心数据准备和四阶段训练，在远场嘈杂混响条件下取得第一名，并揭示了DNSMOS和说话人相似度指标的脆弱性。
</div>

## 👥 作者与机构

**Dominik Klement** ¹ · Yoshiki Masuyama · Christoph Boeddeker · Kohei Saijo · Julius Richter · Gordon Wichern · Jonathan Le Roux

**机构**：三菱电机研究实验室

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合从事目标说话人提取和远场语音处理的读者。重点阅读第3节数据准备和第4节训练策略，以及第5节对抗攻击分析。建议先看摘要和结论，再深入实验部分。

## 🌍 研究背景

目标说话人提取（TSE）在合成全重叠数据上表现良好，但在真实远场嘈杂混响场景中性能下降。Real-TSE挑战旨在推动真实场景性能。现有方法多关注模型架构创新，而数据质量的影响被低估。本文基于基线模型，通过系统性的数据准备和训练策略，探索数据对TSE性能的关键作用。

## 💡 核心创新

1. 四阶段训练策略：从合成到真实数据逐步适应
2. 伪目标生成：利用处理后的近讲麦克风信号
3. 对抗攻击分析：揭示DNSMOS和说话人相似度指标的脆弱性

## 🏗️ 模型架构

基于基线TSE模型（未明确命名，可能为Conv-TasNet或类似），输入为远场混合语音和说话人注册语音，提取目标说话人。模型结构未改动，重点在数据预处理和训练流程。参数量未提及。

## 📚 数据集

- Real-TSE Challenge数据集（训练/评估，远场嘈杂混响录音）
- 合成全重叠混合（预训练）
- 模拟多说话人对话（预训练，含噪声和混响）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| DNSMOS | Real-TSE Challenge Track 2 | 未提供 | **第一名** | 未提供具体数值 |
| 说话人相似度 | Real-TSE Challenge Track 2 | 未提供 | **第一名** | 未提供具体数值 |

MERL提交在Real-TSE挑战赛Track 2中获得第一名，但摘要未给出具体指标数值。通过对抗攻击实验发现，DNSMOS和说话人相似度可被优化至极值而不影响词错误率和VAD F1分数，表明这些指标易受攻击。

## 🎯 结论与影响

本文强调高质量数据准备对TSE在真实场景中的关键作用，四阶段训练策略有效提升性能。同时指出常用评估指标（DNSMOS、说话人相似度）的脆弱性，建议未来结合更鲁棒的指标。对工业落地有指导意义：数据清洗和训练策略比模型架构创新更重要。

## ⚠️ 局限与未解决问题

未开源代码和模型；未报告具体指标数值（如SI-SDR、PESQ）；仅基于基线模型，未探索架构改进；对抗攻击分析仅针对两个指标，未全面评估其他指标；数据集规模未明确。

---

<div class="paper-footer"><span>评分：8.5</span><span>原始：7.5</span><span>+1 重点领域加权</span><a href="/audio-paper-daily/posts/2026-07-13/">← 返回 2026-07-13 速递</a></div>
