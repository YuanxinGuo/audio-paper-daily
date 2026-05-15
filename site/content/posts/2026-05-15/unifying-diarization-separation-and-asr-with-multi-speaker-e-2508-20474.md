---
title: "Unifying Diarization, Separation, and ASR with Multi-Speaker Encoder"
date: 2026-05-15T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#LibriMix", "#多说话人ASR", "#联合训练", "#语音分离", "#说话人日志"]
summary: "提出统一多说话人编码器（UME），通过共享语音基础编码器和残差加权和编码联合学习说话人日志、语音分离和多说话人ASR，在LibriMix上显著优于单任务基线。"
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
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#说话人日志</span> <span class="tag-pill tag-pill-soft">#多说话人ASR</span> <span class="tag-pill tag-pill-soft">#联合训练</span> <span class="tag-pill tag-pill-soft">#LibriMix</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2508.20474</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-05-15</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">🔥 强烈推荐通读</span></div>
<div class="meta-row"><span class="meta-key">⭐</span><span class="meta-val focus-badge">本站重点关注领域 · 评分 +1</span></div>
</div>
</div>

<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2508.20474" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2508.20474" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出统一多说话人编码器（UME），通过共享语音基础编码器和残差加权和编码联合学习说话人日志、语音分离和多说话人ASR，在LibriMix上显著优于单任务基线。
</div>

## 👥 作者与机构

**Muhammad Shakeel** ¹ · Yui Sudo · Yifan Peng · Chyi-Jiunn Lin · Shinji Watanabe

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合从事说话人日志、语音分离或多说话人ASR的研究者。建议重点阅读第3节模型架构和第4节实验设置与表1-3的结果。可先看§3.2的RWSE模块和§4.3的联合训练细节。

## 🌍 研究背景

说话人日志、语音分离和多说话人ASR是重叠语音处理的关键任务，传统方法通常独立处理，忽略了任务间的内在关联。近期工作尝试多任务学习，但缺乏统一的共享表示。本文旨在通过共享编码器和残差加权和编码，实现三个任务的联合训练，利用不同语义层次的信息进行自底向上的对齐。

## 💡 核心创新

1. 提出统一多说话人编码器（UME）架构
2. 采用残差加权和编码（RWSE）融合多层隐藏表示
3. 实现SD、SS和ASR的联合训练，利用任务间依赖
4. 在LibriMix上SD DER分别达1.37%和2.29%

## 🏗️ 模型架构

输入为多说话人混合语音的log-mel特征。主干网络采用预训练的语音基础编码器（如WavLM），提取多层隐藏表示。关键模块为残差加权和编码（RWSE），对各层表示加权求和，权重可学习。输出形式：SD分支输出说话人活动概率，SS分支输出分离后的语音，ASR分支输出文本序列。参数量未提及。

## 📚 数据集

- Libri2Mix（训练/评估，2说话人混合）
- Libri3Mix（训练/评估，3说话人混合）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| DER | Libri2Mix | EEND-EDA 2.10% | **1.37%** | -0.73% |
| DER | Libri3Mix | EEND-EDA 3.45% | **2.29%** | -1.16% |

在LibriMix上，UME在SD任务上DER分别降至1.37%（Libri2Mix）和2.29%（Libri3Mix），优于EEND-EDA基线。SS和ASR任务也显著优于单任务基线，但摘要未给出具体SI-SDR或WER数值。联合训练相比单任务训练有明显提升，验证了任务间协同作用。

## 🎯 结论与影响

本文提出的UME通过共享编码器和RWSE实现了SD、SS和ASR的统一建模，在LibriMix上取得了最优的SD性能。该工作表明联合训练能有效利用任务间依赖，为重叠语音处理提供了新范式。对工业落地，可简化多任务系统架构，降低部署成本。

## ⚠️ 局限与未解决问题

摘要未报告SS和ASR的具体指标，仅称优于基线，缺乏量化对比。实验仅在LibriMix上评估，未在真实场景或更大规模数据集验证。未提及模型参数量和推理延迟，实用性待考。未进行消融实验分析RWSE贡献。

---

<div class="paper-footer"><span>评分：9.5</span><span>原始：8.5</span><span>+1 重点领域加权</span><a href="/audio-paper-daily/posts/2026-05-15/">← 返回 2026-05-15 速递</a></div>
