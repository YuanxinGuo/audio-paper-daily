---
title: "PhASE-Flow: Phonetic-Conditioned Acoustic Flow Matching in SSL Representation Domain for Speech Enhancement"
date: 2026-06-17T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#语音增强"]
summary: "提出PhASE-Flow，在SSL表示空间进行语音增强的流匹配框架，利用音素条件建模干净语音分布，仅需4步采样即可达到SOTA性能。"
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
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#流匹配</span> <span class="tag-pill tag-pill-soft">#自监督学习</span> <span class="tag-pill tag-pill-soft">#语音增强</span> <span class="tag-pill tag-pill-soft">#高效推理</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2606.17806</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-06-17</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
<div class="meta-row"><span class="meta-key">⭐</span><span class="meta-val focus-badge">本站重点关注领域 · 评分 +1</span></div>
</div>
</div>

<div class="opensource-banner"><div class="oc-headline"><span class="oc-pulse"></span><span class="oc-title">本论文已开源</span><span class="oc-hint">点击下方卡片直达对应资源</span></div><div class="oc-grid"><a class="oc-chip oc-chip-demo" href="https://anonymous.4open.science/w/phase-flow_demo-E6E1/" target="_blank" rel="noopener"><span class="oc-icon">🔊</span><span class="oc-text"><span class="oc-label">在线 Demo</span><span class="oc-sub">anonymous.4open.science/w/phase-flow_demo-E6E1/</span></span></a></div></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2606.17806" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2606.17806" target="_blank" rel="noopener">📑 PDF</a><a class="rsrc rsrc-demo" href="https://anonymous.4open.science/w/phase-flow_demo-E6E1/" target="_blank" rel="noopener">🔊 Demo</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出PhASE-Flow，在SSL表示空间进行语音增强的流匹配框架，利用音素条件建模干净语音分布，仅需4步采样即可达到SOTA性能。
</div>

## 👥 作者与机构

**Jun Gao** ¹ · Xiaobin Rong · Yu Sun · Dahan Wang · Jing Lu

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合语音增强和生成式模型研究者。建议重点阅读§3方法部分和§4实验中的采样步数对比。可先看表1和表2了解性能提升，再深入§3.2的SSL空间流匹配设计。

## 🌍 研究背景

流匹配（FM）在语音增强中展现出高保真生成能力，但现有方法主要在频谱域操作，仅将自监督学习（SSL）特征作为外部条件，未充分利用SSL表示的结构化信息。SSL模型（如wav2vec 2.0）能提供层次化的声学和音素表示，但如何直接在SSL潜在空间建模干净语音分布仍未被探索。本文旨在解决这一问题，提出在SSL空间内进行条件流匹配，以提升增强语音的质量和效率。

## 💡 核心创新

1. 在SSL潜在空间而非频谱域进行流匹配建模
2. 音素条件声学流匹配，利用SSL层次化表示
3. 仅需4步采样即可达到SOTA性能，推理高效

## 🏗️ 模型架构

输入含噪语音经SSL模型（如wav2vec 2.0）提取声学表示和音素表示。声学表示作为流匹配的目标分布，音素表示作为条件。流匹配网络采用Transformer架构，通过条件流匹配学习从先验分布到干净声学表示的映射。最后使用神经声码器（如HiFi-GAN）将生成的干净声学表示重建为波形。模型参数量未在摘要中给出。

## 📚 数据集

- DNS-Challenge（训练/评估，规模未提及）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| PESQ | DNS-Challenge | SOTA基线（未指名具体值） | **优于基线** | 未给出具体数值 |
| STOI | DNS-Challenge | SOTA基线 | **优于基线** | 未给出具体数值 |

实验表明，PhASE-Flow在感知质量和可懂度指标上优于现有SOTA基线。特别地，仅用4个采样步骤即可达到竞争性能，显著提升推理效率。但摘要未提供具体数值，仅定性描述。

## 🎯 结论与影响

PhASE-Flow通过在SSL潜在空间进行流匹配，有效利用了SSL表示的层次化结构，实现了高质量且高效的语音增强。该方法为生成式语音增强提供了新范式，有望推动实时应用。对工业落地而言，其少步采样特性降低了计算成本。

## ⚠️ 局限与未解决问题

摘要未提及局限。可能的问题包括：依赖SSL模型的质量；未报告参数量和实际推理延迟；仅在DNS-Challenge上评估，泛化性未知；缺少与频谱域流匹配方法的直接对比。

## 🔗 开源资源

- **Demo / 试听**：<https://anonymous.4open.science/w/phase-flow_demo-E6E1/>

---

<div class="paper-footer"><span>评分：9.2</span><span>原始：8.2</span><span>+1 重点领域加权</span><a href="/audio-paper-daily/posts/2026-06-17/">← 返回 2026-06-17 速递</a></div>
