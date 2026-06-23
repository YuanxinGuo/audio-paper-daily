---
title: "Explainable AI in Speaker Recognition -- Attention Map Visualisation and Evaluation"
date: 2026-06-23T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#说话人识别"]
summary: "提出改进的注意力图评估算法Modified RISE-eval，用于评估说话人识别网络中CAM方法的注意力图质量。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#说话人识别</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#可解释AI</span> <span class="tag-pill tag-pill-soft">#注意力机制</span> <span class="tag-pill tag-pill-soft">#类激活图</span> <span class="tag-pill tag-pill-soft">#评估算法</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2606.22901</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-06-22</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2606.22901" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2606.22901" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出改进的注意力图评估算法Modified RISE-eval，用于评估说话人识别网络中CAM方法的注意力图质量。
</div>

## 👥 作者与机构

**Yanze Xu** ¹ · Mark D. Plumbley · Wenwu Wang

**机构**：萨里大学

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合对XAI在说话人识别中应用感兴趣的读者。建议重点阅读§3（现有评估算法分析）和§4（Modified RISE-eval提出部分），以及§5的实验结果。可先看表1对比改进前后的评估差异。

## 🌍 研究背景

说话人识别神经网络常利用注意力机制进行决策，但如何解释和评估这些注意力图仍是一个挑战。现有CAM方法（如GradCAM、LayerCAM）被广泛用于生成注意力图，但缺乏系统的评估标准。本文指出现有评估算法RISE-eval的缺陷，并提出改进版本，以更可靠地评估注意力图的质量。

## 💡 核心创新

1. 提出Modified RISE-eval评估算法，修正原RISE-eval的缺陷
2. 系统分析现有注意力图评估算法的不足
3. 在说话人识别任务上对比GradCAM和LayerCAM的注意力图质量

## 🏗️ 模型架构

本文不提出新的网络架构，而是聚焦于评估方法。使用一个预训练的说话人识别网络（具体架构未在摘要中说明），输入为语音片段，网络输出说话人身份。注意力图由GradCAM和LayerCAM生成，然后通过Modified RISE-eval算法进行评估。

## 📚 数据集

- 说话人识别数据集（用于训练和评估，具体名称未在摘要中给出）

## 📊 实验结果

摘要未提供具体数值结果，仅说明GradCAM和LayerCAM在不同实验条件下各有优势。实验部分可能包含注意力图的可视化对比和评估分数，但未给出定量指标。

## 🎯 结论与影响

本文提出的Modified RISE-eval算法能够更可靠地评估注意力图质量，为XAI在说话人识别中的应用提供了更有效的工具。该工作有助于推动注意力机制的可解释性研究，但尚未在更多任务或网络上验证。

## ⚠️ 局限与未解决问题

仅在一个说话人识别网络上测试，泛化性未知；未与更多CAM方法对比；未提供开源代码或数据集；评估指标可能仍存在主观性。

---

<div class="paper-footer"><span>评分：6.5</span><span>原始：6.5</span><a href="/audio-paper-daily/posts/2026-06-23/">← 返回 2026-06-23 速递</a></div>
