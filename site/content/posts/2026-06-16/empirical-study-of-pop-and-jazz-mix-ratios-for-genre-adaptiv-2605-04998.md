---
title: "Empirical Study of Pop and Jazz Mix Ratios for Genre-Adaptive Chord Generation"
date: 2026-06-16T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#和弦生成"]
summary: "研究流行与爵士和弦生成中混合比例对领域自适应的影响，修正了先前版本中的检查点选择错误。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero">
<div class="hero-score">
<div class="score-num">5.5</div>
<div class="score-stars">★★★☆☆</div>
<div class="score-tier">后50%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#和弦生成</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#音乐生成</span> <span class="tag-pill tag-pill-soft">#迁移学习</span> <span class="tag-pill tag-pill-soft">#爵士</span> <span class="tag-pill tag-pill-soft">#流行</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2605.04998</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-06-16</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">✋ 可以跳过</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2605.04998" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2605.04998" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>研究流行与爵士和弦生成中混合比例对领域自适应的影响，修正了先前版本中的检查点选择错误。
</div>

## 👥 作者与机构

**Jinju Lee** ¹

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合音乐信息检索领域研究者。可快速浏览摘要和修正说明，无需通读全文。重点关注实验设置和指标修正部分。

## 🌍 研究背景

和弦生成是音乐生成的重要子任务，不同音乐风格（如流行、爵士）的和弦进行差异显著。现有方法通常针对单一风格训练，缺乏跨风格自适应能力。本文探索在流行数据上预训练后，通过混合爵士数据微调实现领域自适应，并修正了先前版本中的检查点选择错误。

## 💡 核心创新

1. 提出流行到爵士的领域自适应和弦生成框架
2. 系统研究混合比例对双风格性能的影响
3. 修正检查点选择错误，确保结果可复现

## 🏗️ 模型架构

采用基于Transformer的序列生成模型，输入为和弦序列（流行或爵士），通过自回归方式预测下一个和弦。主干网络为多层Transformer解码器，关键模块包括多头自注意力和前馈网络。输出为和弦类别概率分布。

## 📚 数据集

- 流行和弦数据集（训练/评估，规模未提及）
- 爵士和弦数据集（微调/评估，规模未提及）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| F1 | 流行测试集 | Phase 0（未微调）: 未提供 | **ft-pop80-v2: 未提供** | 未提供 |
| F1 | 爵士测试集 | Phase 0（未微调）: 未提供 | **ft-pop80-v2: 未提供** | 未提供 |

摘要仅提及最佳epoch指标显示适度流行预训练可保持流行准确率同时提升爵士预测，但未给出具体数值。v2修正了检查点选择错误，ft-pop80-v2在3个种子下恢复了哈希区分的爵士自适应F1。

## 🎯 结论与影响

本文表明通过适度混合爵士数据进行微调，流行预训练模型可有效适应爵士和弦生成，同时保持流行性能。修正后的实验为领域自适应和弦生成提供了更可靠的结果。对音乐生成领域的风格迁移研究有参考价值，但工业落地尚需更大规模验证。

## ⚠️ 局限与未解决问题

摘要未提供具体指标数值，实验规模较小，仅涉及流行和爵士两种风格，泛化性未知。未报告推理效率或模型复杂度。缺乏与现有和弦生成方法的全面对比。

---

<div class="paper-footer"><span>评分：5.5</span><span>原始：5.5</span><a href="/audio-paper-daily/posts/2026-06-16/">← 返回 2026-06-16 速递</a></div>
