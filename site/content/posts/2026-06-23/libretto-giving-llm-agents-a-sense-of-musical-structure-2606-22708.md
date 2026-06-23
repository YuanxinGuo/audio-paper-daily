---
title: "Libretto: Giving LLM Agents a Sense of Musical Structure"
date: 2026-06-23T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#音乐生成"]
summary: "提出Libretto框架，通过LLM原生语法和统计评估空间，使符号音乐生成可编辑、可诊断、可迭代。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#音乐生成</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#符号音乐生成</span> <span class="tag-pill tag-pill-soft">#LLM代理</span> <span class="tag-pill tag-pill-soft">#音乐结构</span> <span class="tag-pill tag-pill-soft">#可控生成</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2606.22708</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-06-21</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2606.22708" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2606.22708" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出Libretto框架，通过LLM原生语法和统计评估空间，使符号音乐生成可编辑、可诊断、可迭代。
</div>

## 👥 作者与机构

**Yichen Xu** ¹

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合音乐生成、可控生成方向的研究者。建议重点阅读§3的语法设计和§4的评估空间，以及§5的四个任务实验。可先看表1和算法1了解整体流程。

## 🌍 研究背景

现有生成式音乐系统能从文本提示生成音频，但音频输出难以检查、编辑和诊断音乐结构。符号音乐生成虽可操作，但缺乏统一的结构化表示和评估方法。本文旨在为LLM代理提供一种可测量、可编辑的符号音乐表示框架。

## 💡 核心创新

1. LLM原生语法：显式onset槽、声部、小节级组织
2. 语料校准统计空间：评估节奏、和声、旋律、织体、形式、变奏
3. 同一结构轴支持检索、诊断、复制风险控制和迭代自修正

## 🏗️ 模型架构

输入为符号音乐序列（如MIDI），通过LLM原生语法解析为结构化表示（onset槽、声部、小节）。主干为LLM代理，利用语法约束生成或修改音乐。关键模块包括统计评估空间（基于语料库校准的六维特征）和迭代自修正循环。输出为符号音乐序列。

## 📚 数据集

- 自定义语料库（用于校准统计空间，未说明规模）
- 四个任务数据集（gap filling, reference-guided generation, morphing, educational generation，未公开）

## 📊 实验结果

摘要未提供具体数值结果，仅描述框架在四个任务上的定性表现：gap filling、参考引导的全曲生成、渐变变形和教育音乐生成。无定量指标对比。

## 🎯 结论与影响

Libretto将符号音乐从原始token序列转化为LLM代理可测量、可编辑的对象，通过结构化语法和统计评估空间实现了可控生成和迭代修正。对音乐生成子方向提供了新的表示范式，有望推动符号音乐与LLM的深度结合，但工业落地需更多定量验证。

## ⚠️ 局限与未解决问题

缺乏定量实验和与现有方法的指标对比；未报告推理延迟或计算开销；语料库规模未说明，可能影响统计空间泛化性；仅支持符号音乐，不直接处理音频。

---

<div class="paper-footer"><span>评分：6.5</span><span>原始：6.5</span><a href="/audio-paper-daily/posts/2026-06-23/">← 返回 2026-06-23 速递</a></div>
