---
title: "Vividh-ASR: A Complexity-Tiered Benchmark and Optimization Dynamics for Robust Indic Speech Recognition"
date: 2026-05-15T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#低资源语音识别", "#多语言ASR", "#微调策略", "#语音识别", "#课程学习"]
summary: "提出Vividh-ASR基准，揭示多语言ASR微调中的studio-bias问题，并设计反向多阶段微调（R-MFT）策略，使小模型匹配大模型性能。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero">
<div class="hero-score">
<div class="score-num">8.2</div>
<div class="score-stars">★★★★☆</div>
<div class="score-tier">前25%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#语音识别</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#多语言ASR</span> <span class="tag-pill tag-pill-soft">#低资源语音识别</span> <span class="tag-pill tag-pill-soft">#课程学习</span> <span class="tag-pill tag-pill-soft">#微调策略</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2605.13087</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-05-13</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2605.13087" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2605.13087" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出Vividh-ASR基准，揭示多语言ASR微调中的studio-bias问题，并设计反向多阶段微调（R-MFT）策略，使小模型匹配大模型性能。
</div>

## 👥 作者与机构

**Kush Juvekar** ¹ · Kavya Manohar · Aditya Srinivas Menon · Arghya Bhattacharya · Kumarmanas Nethil

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合从事多语言/低资源ASR的研究者。建议重点阅读§3（基准构建）和§4.2（R-MFT策略），以及§5.2（CKA/SVD分析）。可先看表2和表3对比结果。

## 🧩 模型一栏概览

| 项 | 内容 |
| --- | --- |
| **应用场景** | 针对印度语言（印地语和马拉雅拉姆语）的鲁棒语音识别，覆盖录音室、广播、自发语音和合成噪声场景。 |
| **核心创新** | 提出复杂度分层的Vividh-ASR基准，包含四个难度层级 · 发现并命名studio-bias现象，即微调改善朗读语音但损害自发语音 · 提出反向多阶段微调（R-MFT）策略，优化学习率时序和课程顺序 |
| **模型架构** | 基于Whisper模型，输入为80维log-Mel特征，主干为编码器-解码器Transformer。关键模块包括：编码器（卷积层+Transformer块）和解码器（因果自注意力+交叉注意力）。参数量为244M（小模型）和769M（大模型）。R-MFT策略通过早期大学习率更新和硬到易课程顺序，使244M模型匹配769M性能。 |
| **数据集** | Vividh-ASR（自建基准，包含studio、broadcast、spontaneous、synthetic noise四层） · Common Voice（可能用于预训练或对比） |
| **关键结果** | R-MFT策略在Vividh-ASR上使244M Whisper模型在全局WER上比标准微调提升12个绝对百分点（从约30%降至18%），并匹配或超越769M模型。在自发语音层，硬到易课程顺序带来额外增益。CKA和SVD分析表明有效调度集中在解码器适应，保持编码器声学几何。 |

## 🎯 与本站重点领域的关联

与本站重点领域无直接关联。但语音增强领域可借鉴其课程学习策略和复杂度分层基准设计思路，用于构建不同噪声/混响级别的评估集。

## ⚠️ 局限与未解决问题

仅涵盖两种印度语言（印地语和马拉雅拉姆语），泛化性待验证；未报告推理延迟或模型大小对部署的影响；未与最新端到端ASR模型（如Conformer）对比；课程顺序的消融实验不够充分。

## 📋 引用

```bibtex
@article{juvekar20262605,
  title  = {Vividh-ASR: A Complexity-Tiered Benchmark and Optimization Dynamics for Robust Indic Speech Recognition},
  author = {Kush Juvekar and  Kavya Manohar and  Aditya Srinivas Menon and  Arghya Bhattacharya and  Kumarmanas Nethil},
  journal = {arXiv preprint arXiv:2605.13087},
  year   = {2026}
}
```

---

<div class="paper-footer"><span>评分：8.2</span><span>原始：8.2</span><a href="/audio-paper-daily/posts/2026-05-15/">← 返回 2026-05-15 速递</a></div>
