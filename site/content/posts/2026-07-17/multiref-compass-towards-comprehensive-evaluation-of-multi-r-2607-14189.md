---
title: "MultiRef-Compass: Towards Comprehensive Evaluation of Multi-Reference-to-Audio-Video Generation"
date: 2026-07-17T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#音频-视频生成评估"]
summary: "提出MultiRef-Compass基准，用于评估多参考到音频-视频生成任务，包含350个样本和14个子指标的评估协议。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero">
<div class="hero-score">
<div class="score-num">7.2</div>
<div class="score-stars">★★★★☆</div>
<div class="score-tier">前25%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#音频-视频生成评估</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#多参考生成</span> <span class="tag-pill tag-pill-soft">#基准测试</span> <span class="tag-pill tag-pill-soft">#多模态评估</span> <span class="tag-pill tag-pill-soft">#音频-视频对齐</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2607.14189</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-07-17</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2607.14189" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2607.14189" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出MultiRef-Compass基准，用于评估多参考到音频-视频生成任务，包含350个样本和14个子指标的评估协议。
</div>

## 👥 作者与机构

**Xiaohan Zhang** ¹ · Yuqing Wen · Junlin Chen · Yuqi Tang · Yiting He · Lizhuo Shao · Weiming Zhu · Tengfei Liu · … 等 4 人

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合从事多模态生成、音频-视频对齐评估的研究者阅读。建议重点看§3（基准构建）和§4（评估协议），以及表1（样本统计）和表2（评估指标）。可跳过§2相关工作。

## 🌍 研究背景

多参考到音频-视频生成（MR2AV）要求模型基于多个参考和文本指令生成同步的音频-视频内容。现有基准主要关注文本驱动生成、单参考主体保持或孤立的音视频对齐，缺乏对MR2AV的全面评估。本文旨在填补这一空白，构建统一基准以评估模型在多参考保持、多实体绑定和组合方面的能力。

## 💡 核心创新

1. 提出MultiRef-Compass基准，含350个可控资产组合样本
2. 定义四维度14子指标的评估协议
3. 引入重判增强的MLLM-as-a-Judge框架
4. 覆盖多视角主体保持、多实体绑定、人-物-场景组合
5. 对8个代表性MR2AV系统进行系统评估

## 🏗️ 模型架构

MultiRef-Compass是一个评估基准而非生成模型。其构建采用可扩展的资产组合流水线，从现有数据集（如AudioSet、VGGSound）中提取参考图像、音频片段和文本指令，通过组合生成多参考样本。评估框架包含自动指标和基于MLLM的评判器，后者通过重判机制提升可靠性。

## 📚 数据集

- MultiRef-Compass（350个样本，用于评估）
- AudioSet（用于提取音频参考）
- VGGSound（用于提取视频参考）

## 📊 实验结果

摘要未提供具体数值结果，但指出对8个代表性MR2AV系统的实验显示多个评估维度存在显著改进空间，表明当前模型在参考保持、音视频一致性和指令遵循方面仍有不足。

## 🎯 结论与影响

MultiRef-Compass是首个针对MR2AV任务的综合基准，填补了评估空白。其可扩展的构建流水线和多维度评估协议为未来研究提供了基础。实验表明现有系统在多个维度上表现不足，亟需改进。该基准有望推动多参考音视频生成领域的标准化评估。

## ⚠️ 局限与未解决问题

基准规模较小（350样本），可能无法覆盖所有复杂场景；依赖MLLM评判器的可靠性需进一步验证；未提供人类评估对比；未讨论计算成本或推理效率。

---

<div class="paper-footer"><span>评分：7.2</span><span>原始：7.2</span><a href="/audio-paper-daily/posts/2026-07-17/">← 返回 2026-07-17 速递</a></div>
