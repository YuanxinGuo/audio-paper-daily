---
title: "Towards Event-Robust Acoustic Scene Classification"
date: 2026-06-11T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#声学场景分类"]
summary: "提出事件迁移声学场景（ESAS）数据集，用于评估声学场景分类系统对未知声音事件的鲁棒性。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#声学场景分类</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#鲁棒性</span> <span class="tag-pill tag-pill-soft">#数据集</span> <span class="tag-pill tag-pill-soft">#事件迁移</span> <span class="tag-pill tag-pill-soft">#声学场景分类</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2606.06921</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-06-11</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2606.06921" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2606.06921" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出事件迁移声学场景（ESAS）数据集，用于评估声学场景分类系统对未知声音事件的鲁棒性。
</div>

## 👥 作者与机构

**Yiqiang Cai** ¹ · Bohan Hu · Yu Yang · Pengwei Lu · Shengchen Li · Xi Shao

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合声学场景分类、鲁棒音频分析方向的研究者。建议重点阅读第3节数据集构建方法和第4节评估协议，以及表2的实验结果。可先看§3.2事件注入策略与§4.2性能退化分析。

## 🌍 研究背景

声学场景分类（ASC）旨在识别音频片段的环境场景（如公园、地铁）。现有数据集（如DCASE）通常包含干净一致的录音，但真实世界常混入意外声音事件（如狗叫、汽车鸣笛），导致模型性能严重下降。目前缺乏专门评估ASC系统对未知事件鲁棒性的基准。本文通过构建ESAS数据集填补这一空白，模拟真实声学变异性。

## 💡 核心创新

1. 提出ESAS数据集，注入前景事件到背景场景
2. 利用大语言模型辅助事件-场景组合生成
3. 系统评估多个SOTA ASC模型的事件鲁棒性
4. 揭示现有模型在事件迁移下性能显著退化

## 🏗️ 模型架构

本文不提出新模型架构，而是构建数据集和评估框架。数据集构建流程：选择背景场景音频（来自现有ASC数据集）→ 利用大语言模型生成合理的事件-场景组合 → 从事件库中选取对应音频 → 按信噪比混合注入。评估使用多个SOTA ASC模型（如CNN、Transformer等），在原始场景和事件迁移场景下对比性能。

## 📚 数据集

- ESAS（事件迁移声学场景数据集，包含多种背景场景与注入事件，用于评估鲁棒性）
- DCASE 2020 Task 1A（原始背景场景数据，用于构建ESAS）
- AudioSet（事件音频来源，用于注入事件）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| 准确率（Accuracy） | ESAS（事件迁移场景） | 原始场景SOTA模型（如CP-ResNet）约85% | **事件迁移下SOTA模型约60%** | -25% |

实验表明，现有SOTA ASC模型在ESAS数据集上准确率平均下降25%以上，其中CNN模型下降尤为明显。不同事件类型对场景分类的影响不同，如动物叫声比车辆声音干扰更大。模型在事件迁移场景下的混淆模式与原始场景显著不同。

## 🎯 结论与影响

本文提出的ESAS数据集有效揭示了现有ASC系统对未知声音事件的脆弱性，为鲁棒ASC研究提供了标准化基准。未来工作可探索事件感知的ASC模型或数据增强策略。该数据集有望推动ASC系统在真实复杂声学环境中的部署。

## ⚠️ 局限与未解决问题

ESAS数据集的事件注入基于预设信噪比，未考虑事件与场景的自然声学交互（如混响）。评估仅覆盖有限的事件类型和场景类别。未提供模型在事件迁移下的泛化性分析（如跨数据集测试）。缺少对模型鲁棒性提升方法的探索。

---

<div class="paper-footer"><span>评分：7.2</span><span>原始：7.2</span><a href="/audio-paper-daily/posts/2026-06-11/">← 返回 2026-06-11 速递</a></div>
