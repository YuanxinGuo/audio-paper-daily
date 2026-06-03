---
title: "Tonal parsimony in chord-sequence analysis: combining modulation cost and tonal vocabulary"
date: 2026-06-03T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#和弦分析"]
summary: "提出调性简约原则，通过联合优化调性转换次数和调性词汇量，实现和弦序列的局部调性分配。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#和弦分析</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#调性分析</span> <span class="tag-pill tag-pill-soft">#动态规划</span> <span class="tag-pill tag-pill-soft">#音乐信息检索</span> <span class="tag-pill tag-pill-soft">#爵士和声</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2606.03459</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-06-03</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2606.03459" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2606.03459" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出调性简约原则，通过联合优化调性转换次数和调性词汇量，实现和弦序列的局部调性分配。
</div>

## 👥 作者与机构

Fran\c{c}ois Pachet

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合音乐信息检索和计算音乐学研究者阅读。重点看§3的算法设计和§4的实验结果，尤其是表1和表2。可先看§3.2的加权爵士替代闭包部分。

## 🌍 研究背景

和弦序列的调性分配是音乐分析、作曲和即兴演奏的基础任务。传统动态规划方法仅最小化调性转换次数，但可能导致不必要的调性中心过多。另一种极端是纯最小词汇量分析，但可能忽略调性转换的合理性。本文旨在平衡两者，提出调性简约原则，在保持转换最优的同时减少调性词汇量。

## 💡 核心创新

1. 提出调性简约原则，联合优化转换次数和调性词汇量
2. 给出精确算法，利用24调性大小调空间降低复杂度
3. 引入加权爵士替代闭包，提升爵士标准曲的分析效果
4. 在31k+序列和1.5k爵士标准曲上验证有效性

## 🏗️ 模型架构

输入为和弦序列（如LMD Chords格式）。采用动态规划框架，定义状态为当前调性（24种大小调）。目标函数为调性简约：先最小化调性转换次数，再最小化不同调性数量。通过两阶段优化实现：第一阶段用标准DP求最小转换次数，第二阶段在保持该次数下用DP求最小词汇量。加权爵士替代闭包通过和弦替换规则扩展和弦集，再应用相同算法。

## 📚 数据集

- LMD Chords（31,032条和弦序列，用于训练/评估）
- 1,555首标注爵士标准曲（用于评估调性分配准确性）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| 平均调性数量 | LMD Chords | 转换最优：3.802 | **调性简约：3.206** | -0.596 |
| 平均转换次数 | LMD Chords | 转换最优：16.728 | **调性简约：12.141** | -4.587 |
| 和弦-音阶兼容性 | 爵士标准曲 | 未明确给出 | **95.6%** | 提升 |

在LMD Chords数据集上，调性简约在55.8%的序列中减少了调性词汇量，同时保持转换最优。加权爵士替代闭包进一步将平均调性数量从3.802降至3.206，转换次数从16.728降至12.141。在爵士标准曲上，和弦-音阶兼容性达到95.6%，表明该方法适用于专业级和声分析。

## 🎯 结论与影响

调性简约原则有效平衡了调性转换和词汇量，在保持转换最优的同时显著减少调性中心数量。该工作为和弦调性分配提供了新视角，算法高效且可扩展，有望应用于自动和声分析、音乐教学和爵士即兴辅助系统。

## ⚠️ 局限与未解决问题

仅考虑24种大小调，未涵盖其他调式（如多利亚、混合利底亚）。加权爵士替代闭包依赖专家规则，可能不适用于其他音乐风格。未与基于深度学习的方法对比。计算复杂度虽可接受，但未报告实际运行时间。

---

<div class="paper-footer"><span>评分：6.5</span><span>原始：6.5</span><a href="/audio-paper-daily/posts/2026-06-03/">← 返回 2026-06-03 速递</a></div>
