---
title: "Vividh-ASR: A Complexity-Tiered Benchmark and Optimization Dynamics for Robust Indic Speech Recognition"
date: 2026-05-14T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#低资源语音识别", "#参数高效微调", "#多语言ASR", "#语音识别", "#课程学习"]
summary: "提出Vividh-ASR基准，揭示多语言ASR微调中的studio-bias现象，并设计反向多阶段微调（R-MFT）策略，使244M参数Whisper模型匹配769M模型性能。"
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
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#多语言ASR</span> <span class="tag-pill tag-pill-soft">#低资源语音识别</span> <span class="tag-pill tag-pill-soft">#课程学习</span> <span class="tag-pill tag-pill-soft">#参数高效微调</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2605.13087</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-05-13</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2605.13087" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2605.13087" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出Vividh-ASR基准，揭示多语言ASR微调中的studio-bias现象，并设计反向多阶段微调（R-MFT）策略，使244M参数Whisper模型匹配769M模型性能。
</div>

## 👥 作者与机构

**Kush Juvekar** ¹ · Kavya Manohar · Aditya Srinivas Menon · Arghya Bhattacharya · Kumarmanas Nethil

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合从事多语言ASR、低资源语音识别及微调策略的研究者。建议重点阅读§3（基准构建）和§4（R-MFT方法），以及表2和表3的结果对比。可先看§4.2的课程学习实验设计。

## 🧩 模型一栏概览

| 项 | 内容 |
| --- | --- |
| **应用场景** | 针对印度语言（印地语和马拉雅拉姆语）的鲁棒语音识别，覆盖录音室、广播、自发语音和合成噪声场景。 |
| **核心创新** | 提出复杂度分层的Vividh-ASR基准，包含四个难度层级 · 发现并命名studio-bias现象，即微调改善朗读语音但损害自发语音 · 提出反向多阶段微调（R-MFT）策略，结合学习率时序和课程学习 |
| **模型架构** | 基于Whisper模型，输入音频特征→编码器（预训练，冻结或微调）→解码器（主要适应层）→输出文本。采用参数高效微调（仅更新解码器部分参数），总参数量244M。关键模块包括学习率调度和课程排序。 |
| **数据集** | Vividh-ASR（自建，包含印地语和马拉雅拉姆语四个层级） · Common Voice（可能用于预训练或对比） |
| **关键结果** | 在Vividh-ASR上，R-MFT使244M Whisper模型在全局WER上比标准微调提升12个绝对百分点，并在自发语音上进一步改善。与769M模型相比，R-MFT在多数层级上匹配或超越其性能。CKA和SVD分析表明有效调度集中在解码器适应。 |

## 🎯 与本站重点领域的关联

与本站重点领域无直接关联。但语音增强领域可借鉴其课程学习策略和studio-bias诊断思路，用于设计更鲁棒的增强模型。

## ⚠️ 局限与未解决问题

仅涵盖两种印度语言，泛化性未知；未报告推理延迟或模型大小对实际部署的影响；缺乏与其他参数高效微调方法（如LoRA）的对比；合成噪声层级的真实性可能有限。

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

<div class="paper-footer"><span>评分：8.2</span><span>原始：8.2</span><a href="/posts/2026-05-14/">← 返回 2026-05-14 速递</a></div>
