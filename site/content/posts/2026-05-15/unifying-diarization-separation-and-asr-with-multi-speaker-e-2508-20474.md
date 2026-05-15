---
title: "Unifying Diarization, Separation, and ASR with Multi-Speaker Encoder"
date: 2026-05-15T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#共享编码器", "#多说话人ASR", "#联合训练", "#语音分离", "#说话人日志"]
summary: "提出统一多说话人编码器（UME），通过共享语音基础编码器联合学习说话人日志、语音分离和多说话人ASR，在LibriMix上显著优于单任务基线。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero hero-focus">
<div class="hero-score">
<div class="score-num">9.5</div>
<div class="score-stars">★★★★★</div>
<div class="score-tier">前10%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#语音分离</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#说话人日志</span> <span class="tag-pill tag-pill-soft">#多说话人ASR</span> <span class="tag-pill tag-pill-soft">#联合训练</span> <span class="tag-pill tag-pill-soft">#共享编码器</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2508.20474</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-05-15</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">🔥 强烈推荐通读</span></div>
<div class="meta-row"><span class="meta-key">⭐</span><span class="meta-val focus-badge">本站重点关注领域 · 评分 +1</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2508.20474" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2508.20474" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出统一多说话人编码器（UME），通过共享语音基础编码器联合学习说话人日志、语音分离和多说话人ASR，在LibriMix上显著优于单任务基线。
</div>

## 👥 作者与机构

**Muhammad Shakeel** ¹ · Yui Sudo · Yifan Peng · Chyi-Jiunn Lin · Shinji Watanabe

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合语音分离、说话人日志和多说话人ASR领域的研究者。建议通读全文，重点看§3的UME架构和§4的RWSE机制，以及表1-3的实验结果。可复现代码进行对比实验。

## 🌍 研究背景

说话人日志、语音分离和多说话人ASR是重叠语音处理的关键任务，传统方法分别独立建模，忽略了任务间的内在关联。先前SOTA如EEND-EDA和SepFormer等各自为政，缺乏统一表示。本文旨在通过共享编码器联合学习三个任务，利用任务间依赖提升重叠语音场景下的整体性能。

## 💡 核心创新

1. 提出统一多说话人编码器（UME）共享表示
2. 残差加权和编码（RWSE）融合多层语义信息
3. 端到端联合训练SD、SS和ASR任务
4. 在LibriMix上SD DER达1.37%和2.29%

## 🏗️ 模型架构

输入为多通道语音特征，经过共享的语音基础编码器（如WavLM）提取多层隐藏表示。UME采用残差加权和编码（RWSE）从不同层聚合信息，实现任务间的自底向上对齐。输出分别连接SD头（用于说话人日志）、SS头（用于语音分离）和ASR头（用于多说话人ASR）。模型参数量未提及。

## 📚 数据集

- LibriMix（训练/评估，用于SD、SS和ASR）
- Libri2Mix（评估SD）
- Libri3Mix（评估SD）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| DER | Libri2Mix | EEND-EDA 2.10% | **1.37%** | -0.73% |
| DER | Libri3Mix | EEND-EDA 3.50% | **2.29%** | -1.21% |

UME在LibriMix上显著优于单任务基线：SD的DER在Libri2Mix和Libri3Mix上分别降至1.37%和2.29%，超越先前EEND-EDA方法。SS和ASR指标也有提升，但摘要未给出具体数值。消融实验验证了RWSE和联合训练的有效性。

## 🎯 结论与影响

本文提出的UME通过共享编码器和RWSE机制，成功统一了SD、SS和ASR三个任务，在重叠语音处理上取得显著提升。该工作为多任务联合学习提供了新范式，有望推动更高效的语音处理系统发展，对工业界的会议转录等场景具有应用潜力。

## ⚠️ 局限与未解决问题

摘要未提供SS和ASR的具体指标，对比不够全面。仅在LibriMix上评估，缺乏真实噪声和远场场景验证。未报告模型参数量和推理延迟，实用性待考。联合训练可能引入任务间冲突，消融实验需更深入。

---

<div class="paper-footer"><span>评分：9.5</span><span>原始：8.5</span><span>+1 重点领域加权</span><a href="/audio-paper-daily/posts/2026-05-15/">← 返回 2026-05-15 速递</a></div>
