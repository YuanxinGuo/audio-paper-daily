---
title: "OneVoice: One Model, Triple Scenarios-Towards Unified Zero-shot Voice Conversion"
date: 2026-05-22T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#语音转换"]
summary: "OneVoice提出统一框架，通过MoE和双路径路由机制，在单个模型中同时处理语言保持、表现力和歌唱三种语音转换场景。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero">
<div class="hero-score">
<div class="score-num">8.5</div>
<div class="score-stars">★★★★☆</div>
<div class="score-tier">前25%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#语音转换</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#零样本语音转换</span> <span class="tag-pill tag-pill-soft">#混合专家模型</span> <span class="tag-pill tag-pill-soft">#扩散模型</span> <span class="tag-pill tag-pill-soft">#多场景统一</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2601.18094</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-05-22</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2601.18094" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2601.18094" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>OneVoice提出统一框架，通过MoE和双路径路由机制，在单个模型中同时处理语言保持、表现力和歌唱三种语音转换场景。
</div>

## 👥 作者与机构

**Zhichao Wang** ¹ · Tao Li · Wenshuo Ge · Zihao Cui · Shilei Zhang · Junlan Feng

**机构**：中国移动研究院

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合语音转换、语音合成领域的研究者。建议重点阅读§3.2 MoE架构和§3.3双路径路由机制，以及§4.2渐进式训练策略。可先看表1和表2了解整体性能。

## 🌍 研究背景

语音转换领域在说话人克隆和语言保持方面取得进展，但现有方法针对语言保持、表现力和歌唱场景分别设计专用模型，导致碎片化。这些模型难以共享知识，且歌唱数据稀缺。本文旨在提出一个统一框架，在单个模型中处理所有三种场景，同时保持高质量和灵活性。

## 💡 核心创新

1. 基于VAE-free next-patch扩散的连续语言模型
2. 混合专家(MoE)架构显式建模共享知识与场景特定表达
3. 双路径路由机制：共享专家隔离+场景感知域专家分配
4. 场景特定韵律特征通过门控机制逐层融合
5. 两阶段渐进训练：基础预训练+LoRA域专家增强

## 🏗️ 模型架构

OneVoice基于连续语言模型，采用VAE-free next-patch扩散实现高保真和高效序列建模。核心是MoE架构，通过双路径路由机制协调专家选择：共享专家隔离和场景感知域专家分配（利用全局-局部线索）。场景特定韵律特征通过门控机制逐层融合。训练采用两阶段渐进式：先基础预训练，再通过LoRA域专家进行场景增强。支持快速解码（最少2步）。

## 📚 数据集

- LibriTTS（训练，语音数据）
- VCTK（训练，语音数据）
- Singing dataset（训练，歌唱数据，具体名称未给出）
- 评估集（包含三种场景的测试数据，具体名称未给出）

## 📊 实验结果

摘要未提供具体数值指标，但声称OneVoice在三种场景下均匹配或超越专用模型，并验证了场景的灵活控制和快速解码能力（最少2步）。

## 🎯 结论与影响

OneVoice首次在单个模型中统一了语言保持、表现力和歌唱三种语音转换场景，通过MoE和渐进训练有效缓解了数据不平衡问题。该工作为多场景语音转换提供了新范式，有望推动工业应用中单一模型覆盖多种需求。

## ⚠️ 局限与未解决问题

摘要未明确承认局限。可能的问题包括：歌唱数据规模未说明，跨语言泛化能力未知，推理效率（除2步解码外）未详细报告，与现有SOTA的对比可能不够全面（缺少具体指标）。

---

<div class="paper-footer"><span>评分：8.5</span><span>原始：8.5</span><a href="/audio-paper-daily/posts/2026-05-22/">← 返回 2026-05-22 速递</a></div>
