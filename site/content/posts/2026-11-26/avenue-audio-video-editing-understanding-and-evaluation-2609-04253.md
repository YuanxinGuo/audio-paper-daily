---
title: "AVENUE: Audio-Video EditiNg Understanding and Evaluation"
date: 2026-11-26T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#音频生成"]
summary: "提出 AVENUE 音视频编辑基准与模态感知评测框架，覆盖 1291 段视频、7957 条指令，揭示跨模态意外改动问题。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero">
<div class="hero-score">
<div class="score-num">6.8</div>
<div class="score-stars">★★★☆☆</div>
<div class="score-tier">前50%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#音频生成</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#音视频编辑</span> <span class="tag-pill tag-pill-soft">#基准评测</span> <span class="tag-pill tag-pill-soft">#多模态</span> <span class="tag-pill tag-pill-soft">#可控生成</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2609.04253</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-11-26</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner"><div class="oc-headline"><span class="oc-pulse"></span><span class="oc-title">本论文已开源</span><span class="oc-hint">点击下方卡片直达对应资源</span></div><div class="oc-grid"><a class="oc-chip oc-chip-hf" href="https://huggingface.co/datasets/AVENUE-dataset/AVENUE" target="_blank" rel="noopener"><span class="oc-icon">🤗</span><span class="oc-text"><span class="oc-label">HuggingFace</span><span class="oc-sub">🤗 datasets/AVENUE-dataset/AVENUE</span></span></a></div></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2609.04253" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2609.04253" target="_blank" rel="noopener">📑 PDF</a><a class="rsrc rsrc-hf" href="https://huggingface.co/datasets/AVENUE-dataset/AVENUE" target="_blank" rel="noopener">🤗 HuggingFace</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出 AVENUE 音视频编辑基准与模态感知评测框架，覆盖 1291 段视频、7957 条指令，揭示跨模态意外改动问题。
</div>

## 👥 作者与机构

**Hayeon Kim** ¹ · Yoojin Jang · Jaejun Yoo

**机构**：蔚山科学技术院

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合做音视频联合生成、可控编辑与多模态评测的研究者阅读。若关注评测方法论，重点看评测框架定义与模态选择性指标部分；若关注模型，看三种编辑范式（joint/sequential/separate）的对比实验与失败案例分析。建议先看基准构建流程与表格式结果，再决定是否精读。

## 🌍 研究背景

音视频编辑要求模型依据文本提示同时改动音频与视频，且需从提示中推断“改哪个模态、保哪个模态”。此前工作多为单模态编辑（如音频编辑、视频编辑）或联合生成，评测基准覆盖的编辑类型与模态组合有限，评测指标往往模态盲、样本无关，无法判断模型是否忠实保留了不应改动的模态。本文要解决的是：构建覆盖多编辑类型的基准，并给出样本级、模态感知的评测框架。

## 💡 核心创新

1. 构建 AVENUE 基准：1291 段源视频、7957 条编辑指令，人工校验
2. 提出样本级模态感知评测框架，显式区分应改内容与应保内容
3. 首次系统对比 joint / sequential / separate 三种编辑范式的模态选择性

## 🏗️ 模型架构

本文为基准与评测工作，非单一模型架构。数据源自 VGGSound，经筛选与人工校验构建源片段与编辑指令对，覆盖音频目标、视频目标与音视频耦合三类编辑。评测框架对每个样本定义 intended change 与 must-remain-intact 内容，分别度量目标模态改动质量与非目标模态保持度。实验侧选取 joint、sequential、separate 三类代表性音视频编辑模型进行统一评测与跨范式分析。

## 📚 数据集

- VGGSound（源视频来源，用于构建基准）
- AVENUE（评估基准，1291 段源片段 / 7957 条指令）

## 📊 实验结果

摘要未给出具体指标数值，仅给出定性结论：无论 joint、sequential 还是 separate 范式，现有模型在编辑一个模态时都会频繁对另一模态产生非预期改动，说明模态选择性仍是开放难题。基准与评测代码/数据已公开于 Hugging Face。

## 🎯 结论与影响

最强结论是：现有音视频编辑模型普遍缺乏模态选择性，编辑一个模态会污染另一模态。该基准与模态感知评测为后续可控音视频编辑提供了统一比较平台，对工业界音视频内容编辑工具的可控性评估有直接参考价值。

## ⚠️ 局限与未解决问题

摘要未报告具体量化结果与人工主观评分细节；基准仅源自 VGGSound，域覆盖偏自然声事件，缺少音乐、语音等场景；未讨论评测指标与人类判断的一致性验证；也未给出推理效率对比。

## 🔗 开源资源

- **HuggingFace**：<https://huggingface.co/datasets/AVENUE-dataset/AVENUE>
- **数据集**：<https://huggingface.co/datasets/AVENUE-dataset/AVENUE>

---

<div class="paper-footer"><span>评分：6.8</span><span>原始：6.8</span><a href="/audio-paper-daily/posts/2026-11-26/">← 返回 2026-11-26 速递</a></div>
