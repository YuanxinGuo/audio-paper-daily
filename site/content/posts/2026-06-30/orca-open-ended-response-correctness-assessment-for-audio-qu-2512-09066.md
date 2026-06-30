---
title: "ORCA: Open-ended Response Correctness Assessment for Audio Question Answering"
date: 2026-06-30T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#音频问答评估"]
summary: "提出ORCA，一种轻量级模型，用于评估大音频语言模型在开放音频问答中的回答正确性，并建模人类分歧。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero">
<div class="hero-score">
<div class="score-num">7.8</div>
<div class="score-stars">★★★★☆</div>
<div class="score-tier">前25%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#音频问答评估</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#大音频语言模型</span> <span class="tag-pill tag-pill-soft">#自动评估</span> <span class="tag-pill tag-pill-soft">#开放问答</span> <span class="tag-pill tag-pill-soft">#人类对齐</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2512.09066</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-06-30</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2512.09066" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2512.09066" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出ORCA，一种轻量级模型，用于评估大音频语言模型在开放音频问答中的回答正确性，并建模人类分歧。
</div>

## 👥 作者与机构

\v{S}imon Sedl\'a\v{c}ek · Sara Barahona · Bolaji Yusuf · Laura Herrera-Alarc\'on · Santosh Kesiraju · Cecilia Bola\~nos · Alicia Lozano-Diez · Sathvik Udupa · … 等 4 人

**机构**：布尔诺理工大学 · 马里兰大学 · 亚马逊

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合从事音频问答评估、LALM基准测试的研究者。建议重点阅读第3节（三阶段标注流程）和第4节（课程学习与实验结果），特别是表1和表2。可跳过第2节相关工作。

## 🌍 研究背景

大音频语言模型（LALM）在复杂推理和主观任务上能力评估需求迫切，但现有基准多依赖封闭式问题或简单指标。开放问答评估面临人类标注成本高、模型间分歧大等挑战。本文旨在开发一种可靠、轻量的自动评估方法，以替代昂贵的LLM评判器，并有效建模人类分歧。

## 💡 核心创新

1. 三阶段人机协同标注流程（人类判断+结构化反馈+AI修正）
2. 课程学习策略训练评估模型
3. 预测方差与人类分歧强相关，可识别问题项

## 🏗️ 模型架构

ORCA基于预训练语言模型（如RoBERTa）构建，输入为音频问答对的文本转录（问题+音频描述+回答），输出正确性评分（0-1）和方差。采用课程学习：先易后难，从简单二分类到复杂评分。模型轻量（<1B参数），无需音频编码器。

## 📚 数据集

- Clotho-AQA（训练/评估，含音频描述和问答对）
- AVQA（训练/评估，视听问答）
- Music-AQA（训练/评估，音乐问答）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| Spearman相关系数 | 已见基准（Clotho-AQA, AVQA, Music-AQA） | Gemini 2.5 Flash (0.82) | **0.91** | +0.09 |
| Spearman相关系数 | 未见基准（综合） | Gemini 2.5 Flash (0.78) | **0.85** | +0.07 |

ORCA在已见基准上Spearman相关系数达0.91，优于Gemini 2.5 Flash（0.82）；在未见基准上泛化至0.85。预测方差与人类分歧的Pearson相关系数为0.68，能有效识别有问题的基准项。消融实验验证了三阶段标注和课程学习的贡献。

## 🎯 结论与影响

ORCA提供了一种可靠、轻量的LALM开放问答评估方法，与人类判断高度一致，并能建模分歧。该方法有望替代昂贵的LLM评判器，推动音频问答基准的自动评估。对工业界，可降低模型评估成本，加速迭代。

## ⚠️ 局限与未解决问题

ORCA依赖文本转录，可能丢失音频细节；仅在三个基准上验证，泛化性需更多测试；未评估对错误类型（如幻觉）的区分能力；未报告推理延迟。

---

<div class="paper-footer"><span>评分：7.8</span><span>原始：7.8</span><a href="/audio-paper-daily/posts/2026-06-30/">← 返回 2026-06-30 速递</a></div>
