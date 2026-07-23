---
title: "Scalable Keyword Spotting via Modular Network Expansion"
date: 2026-07-23T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#关键词唤醒"]
summary: "提出一种参数受限的模块化扩展方法，在冻结基网络的同时训练轻量扩展分支，实现新关键词的增量添加，降低误拒率并减少计算开销。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero">
<div class="hero-score">
<div class="score-num">7.2</div>
<div class="score-stars">★★★★☆</div>
<div class="score-tier">前50%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#关键词唤醒</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#模块化扩展</span> <span class="tag-pill tag-pill-soft">#参数高效微调</span> <span class="tag-pill tag-pill-soft">#嵌入式设备</span> <span class="tag-pill tag-pill-soft">#持续学习</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2607.19918</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-07-23</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2607.19918" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2607.19918" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出一种参数受限的模块化扩展方法，在冻结基网络的同时训练轻量扩展分支，实现新关键词的增量添加，降低误拒率并减少计算开销。
</div>

## 👥 作者与机构

**Viktor Khaymonenko** ¹ · Dzmitry Saladukha · Aliaksei Rak · Alexander Rostov

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合从事关键词唤醒或嵌入式语音系统的研究人员。建议重点阅读第3节方法描述和第4节实验对比，尤其是表1和表2中的FRR与MACs结果。可复现其模块化扩展思路。

## 🌍 研究背景

嵌入式设备上的关键词唤醒模型在部署后常需添加新关键词，但原始训练数据不可用且需避免对已有关键词的回归。现有方法如单独训练新模型或使用适配器/LoRA等参数高效微调，但存在参数开销大或性能下降的问题。本文旨在解决在固定参数预算下，如何高效添加新关键词同时保持原有性能。

## 💡 核心创新

1. 参数受限的模块化扩展策略
2. 冻结基网络（含BN统计和分类器）
3. 轻量扩展分支+独立新关键词头
4. 保持核心logits和阈值不变

## 🏗️ 模型架构

输入特征（如MFCC）→ 基网络（冻结，含BN统计和核心分类器）→ 轻量扩展分支（新增参数≤10k）→ 新关键词头（独立训练）。扩展分支与基网络并行，输出与基网络logits合并后用于决策。总MACs为16.34M，低于对比方法。

## 📚 数据集

- Google Speech Commands V2（训练/评估，含35个关键词）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| 新关键词平均误拒率 (FRR) | Google Speech Commands V2 | 参数匹配的单独模型基线 6.46 | **4.37** | -2.09 |
| MACs (百万次乘加) | Google Speech Commands V2 | 适配器基线 18.45 / LoRA基线 20.52 | **16.34** | -2.11 / -4.18 |

在固定操作点下，本文方法将新关键词平均误拒率从6.46降至4.37，优于参数匹配的单独模型基线；在相同新增参数预算（≤10k）下，MACs为16.34M，低于适配器（18.45M）和LoRA（20.52M）基线。未报告已有关键词的误拒率变化，但声称保持原有性能。

## 🎯 结论与影响

本文提出的参数受限模块化扩展方法能有效在嵌入式设备上增量添加新关键词，同时降低误拒率和计算开销。该方法对持续学习场景下的关键词唤醒系统具有实用价值，可推广至其他需要增量学习的语音任务。

## ⚠️ 局限与未解决问题

实验仅在单一数据集（Google Speech Commands V2）上进行，未验证跨数据集泛化性；未报告已有关键词的误拒率具体数值，仅声称无回归；未讨论扩展分支的容量上限及多个新关键词的累积影响。

---

<div class="paper-footer"><span>评分：7.2</span><span>原始：7.2</span><a href="/audio-paper-daily/posts/2026-07-23/">← 返回 2026-07-23 速递</a></div>
