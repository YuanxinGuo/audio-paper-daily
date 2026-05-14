---
title: "Do not copy and paste! Rewriting strategies for code retrieval"
date: 2026-05-14T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#LLM", "#代码检索", "#嵌入模型", "#重写策略"]
summary: "系统研究三种重写策略（风格改写、伪代码、自然语言）在代码检索中的效果，发现联合查询-语料库重写显著提升性能，而仅语料库重写常导致退化，并提出Delta H指标预测重写收益。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero">
<div class="hero-score">
<div class="score-num">7.5</div>
<div class="score-stars">★★★★☆</div>
<div class="score-tier">前25%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#代码检索</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#代码检索</span> <span class="tag-pill tag-pill-soft">#重写策略</span> <span class="tag-pill tag-pill-soft">#LLM</span> <span class="tag-pill tag-pill-soft">#嵌入模型</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2605.08299</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-05-08</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2605.08299" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2605.08299" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>系统研究三种重写策略（风格改写、伪代码、自然语言）在代码检索中的效果，发现联合查询-语料库重写显著提升性能，而仅语料库重写常导致退化，并提出Delta H指标预测重写收益。
</div>

## 👥 作者与机构

**Andrea Gurioli** ¹ · Federico Pennino · Maurizio Gabbrielli

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合从事代码检索、嵌入模型或LLM应用的读者。建议重点阅读§3（重写策略层次）和§5（实验结果与Delta H诊断），可跳过§2相关工作。先看表1和表2了解整体效果。

## 🧩 模型一栏概览

| 项 | 内容 |
| --- | --- |
| **应用场景** | 提升基于嵌入的代码检索系统性能。 |
| **核心创新** | 首次评估NL-enriched PseudoCode和片段级NL作为直接检索表示 · 提出Delta H指标预测重写收益 · 系统比较三种重写策略和两种增强模式 |
| **模型架构** | 输入代码查询和语料库 → 使用LLM（Qwen/DeepSeek/Mistral）进行重写（风格改写/伪代码/自然语言）→ 联合或仅语料库增强 → 使用五个编码器（如MoSE-18）生成嵌入 → 检索。无具体参数量。 |
| **数据集** | CoIR基准（包含6个数据集，如CT-Contest） |
| **关键结果** | 全NL重写+QC在CT-Contest上对MoSE-18取得+0.51绝对NDCG@10提升；仅语料库重写在90个配置中56个退化（约62%）；Delta H与QC增益的Spearman rho达0.593（Codestral）。 |

## 🎯 与本站重点领域的关联

与本站5个重点领域无直接关联。但代码检索中的重写策略和诊断指标思路可迁移至语音领域，例如对语音查询进行风格归一化或使用熵指标预测增强收益。

## ⚠️ 局限与未解决问题

未报告推理延迟或计算成本；仅评估CoIR基准，泛化性未知；未消融不同重写策略的单独贡献；Delta H预测仅基于QC模式，未验证C模式。

## 📋 引用

```bibtex
@article{gurioli20262605,
  title  = {Do not copy and paste! Rewriting strategies for code retrieval},
  author = {Andrea Gurioli and  Federico Pennino and  Maurizio Gabbrielli},
  journal = {arXiv preprint arXiv:2605.08299},
  year   = {2026}
}
```

---

<div class="paper-footer"><span>评分：7.5</span><span>原始：7.5</span><a href="/posts/2026-05-14/">← 返回 2026-05-14 速递</a></div>
