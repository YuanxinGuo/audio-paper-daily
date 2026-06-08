---
title: "How Far Can Chord-Symbol Time-Series Adaptation Carry Genre Identity? Capabilities and Boundaries in Multi-Genre Chord-Symbol Modeling"
date: 2026-06-08T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#音乐信息检索"]
summary: "评估多种参数高效微调方法将预训练和弦符号模型适应到11种音乐流派的能力，发现微调可提升流派内和弦预测，但和弦符号本身不足以完全表征流派身份。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#音乐信息检索</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#和弦符号建模</span> <span class="tag-pill tag-pill-soft">#音乐流派适应</span> <span class="tag-pill tag-pill-soft">#参数高效微调</span> <span class="tag-pill tag-pill-soft">#音乐Transformer</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2606.07334</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-06-08</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2606.07334" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2606.07334" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>评估多种参数高效微调方法将预训练和弦符号模型适应到11种音乐流派的能力，发现微调可提升流派内和弦预测，但和弦符号本身不足以完全表征流派身份。
</div>

## 👥 作者与机构

**Jinju Lee** ¹

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合音乐信息检索和迁移学习研究者阅读。重点看§3实验设置、§4.1主结果和§4.4控制实验。可跳过§4.5-4.7的额外诊断。

## 🌍 研究背景

和弦符号序列是音乐中可解释的表示层，但现有模型多针对特定流派。预训练音乐Transformer在跨流派泛化上有限，参数高效微调（PEFT）方法如LoRA、IA3等被提出用于适应新任务。然而，和弦符号序列本身能否承载流派身份信息尚不明确。本文系统评估了五种PEFT方法在11种流派上的适应能力，并探讨了和弦符号作为流派表征的边界。

## 💡 核心创新

1. 系统比较5种PEFT方法在11种流派上的适应效果
2. 引入匹配数据量控制实验揭示数据驱动效应
3. 通过错误流派适配器实验验证和弦符号的流派信息局限性

## 🏗️ 模型架构

基于冻结的pop-jazz Music Transformer检查点，输入为和弦符号序列。采用五种轻量级适应接口：LoRA（低秩适配）、IA3（抑制和放大）、BitFit（偏置微调）、前缀微调（prefix tuning）和全微调。输出为下一个和弦符号的概率分布。模型参数量未明确给出，但PEFT方法仅更新少量参数。

## 📚 数据集

- 11种流派和弦符号数据集（训练/评估，包含blues, bossa nova等，规模未明确）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| 宏观平均和弦预测准确率提升 | 11种流派混合 | 冻结基线（未给出具体值） | **LoRA/IA3最高（+3.61/+3.58）** | +2.89~+3.61 |

所有五种微调方法在11种流派上均优于冻结基线，宏观提升2.89-3.61个百分点。LoRA和IA3得分最高，但统计检验不支持显著差异。匹配数据量控制实验中，IA3保持最优而LoRA降至末位，表明差距部分由数据驱动。错误流派适配器也优于冻结基线，说明效果主要来自轻量级条件化而非特定适配器族。

## 🎯 结论与影响

和弦符号序列的轻量级适应能可靠提升流派内和声预测，但和弦符号本身不足以完整表征流派身份。该结论为音乐信息检索中的流派建模提供了边界认知，提示未来需结合其他音乐维度（如节奏、音色）以实现流派感知。工业上可用于音乐推荐系统的流派标签细化。

## ⚠️ 局限与未解决问题

未评估感知流派真实性或整体音乐质量，缺乏听众或音乐家评估。实验仅基于和弦符号序列，未考虑其他音乐特征。数据规模差异可能影响结论泛化性。未报告推理延迟或计算成本。

---

<div class="paper-footer"><span>评分：6.8</span><span>原始：6.8</span><a href="/audio-paper-daily/posts/2026-06-08/">← 返回 2026-06-08 速递</a></div>
