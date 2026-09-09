---
title: "Stabilizing Instruction Supervision for Instruct-TTS via Controllable Diversification and Drift Filtering"
date: 2026-09-09T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#语音合成"]
summary: "针对Instruct-TTS中指令重写导致的语义漂移问题，提出可控多样化与漂移过滤的数据稳定化方案，提升指令跟随率。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#语音合成</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#Instruct-TTS</span> <span class="tag-pill tag-pill-soft">#指令跟随</span> <span class="tag-pill tag-pill-soft">#数据增强</span> <span class="tag-pill tag-pill-soft">#漂移过滤</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2609.08204</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-09-08</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2609.08204" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2609.08204" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>针对Instruct-TTS中指令重写导致的语义漂移问题，提出可控多样化与漂移过滤的数据稳定化方案，提升指令跟随率。
</div>

## 👥 作者与机构

**Yizhong Geng** ¹ · Kecan Mao · Qifei Li · Cong Wang · Yingming Gao · Ruimin Wang · Chunfeng Wang · Hao Li · … 等 1 人

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合从事TTS、语音合成及指令驱动生成的研究者阅读。建议重点阅读第3节的方法部分和第4节的实验对比，可先看表1和表2了解主要结果。

## 🌍 研究背景

Instruct-TTS系统通过LLM将结构化风格标签重写为自然语言指令，但无约束重写导致超过40%的语义漂移，破坏监督信号并削弱泛化。现有方法未系统处理指令监督的不稳定性。本文旨在通过数据中心的稳定化方案，提升指令覆盖率和保真度，从而改善指令跟随性能。

## 💡 核心创新

1. 提出可控指令多样化策略，系统扩展指令覆盖
2. 引入LLM漂移过滤机制，降低语义漂移
3. 设计属性对齐监督，将韵律控制与声学扰动结合
4. 构建漂移分类法，可推广至其他指令驱动生成
5. 在InstructTTSEval中文集上验证有效性

## 🏗️ 模型架构

本文方法不涉及特定模型架构，而是数据中心的处理流程：输入为原始风格标签，通过LLM重写生成指令，经可控多样化扩展，再经漂移过滤筛选，最后与声学扰动对齐形成训练数据。该流程可应用于任意Instruct-TTS模型，如基于Transformer或扩散的TTS系统。

## 📚 数据集

- InstructTTSEval中文集（评估）
- 内部中文TTS训练数据（训练）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| 指令跟随率 | InstructTTSEval中文集 | 无微调 34.5% | **56.4%** | +21.9% |
| 指令跟随率 | InstructTTSEval中文集 | 朴素微调 51.0% | **56.4%** | +5.4% |
| 漂移率 | 重写指令 | 无约束重写 40.4% | **约束重写 15.4%** | -25.0% |

实验表明，所提方法在InstructTTSEval中文集上将指令跟随率从无微调的34.5%和朴素微调的51.0%提升至56.4%，同时约束重写将漂移率从40.4%降至15.4%。消融实验证实三个机制互补，且漂移分类法可能泛化至TTS之外的指令驱动生成。

## 🎯 结论与影响

本文通过数据中心的稳定化方案有效缓解Instruct-TTS中的指令监督不稳定问题，显著提升指令跟随性能。该工作为指令驱动生成的数据质量提供了新视角，其漂移分类法可能影响后续研究。工业上，该方法可低成本提升TTS系统的可控性，无需修改模型架构。

## ⚠️ 局限与未解决问题

实验仅在中文数据集上验证，泛化性未知；未报告主观MOS或自然度指标；漂移过滤依赖LLM，可能引入额外计算开销；未与更多基线方法对比；未分析指令多样性对性能的具体影响。

---

<div class="paper-footer"><span>评分：7.2</span><span>原始：7.2</span><a href="/audio-paper-daily/posts/2026-09-09/">← 返回 2026-09-09 速递</a></div>
