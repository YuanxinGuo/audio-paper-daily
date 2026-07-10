---
title: "MulTTiPop: A Multitrack Transcription Dataset for Pop Music"
date: 2026-07-10T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#音乐转录"]
summary: "MulTTiPop是一个包含572段流行音乐的多轨MIDI转录数据集，用于评估自动音乐转录模型。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero">
<div class="hero-score">
<div class="score-num">7.5</div>
<div class="score-stars">★★★★☆</div>
<div class="score-tier">前25%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#音乐转录</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#多轨转录</span> <span class="tag-pill tag-pill-soft">#数据集</span> <span class="tag-pill tag-pill-soft">#流行音乐</span> <span class="tag-pill tag-pill-soft">#MIDI</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2607.08756</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-07-10</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner"><div class="oc-headline"><span class="oc-pulse"></span><span class="oc-title">本论文已开源</span><span class="oc-hint">点击下方卡片直达对应资源</span></div><div class="oc-grid"><a class="oc-chip oc-chip-proj" href="https://gclef-cmu.edu/multtipop" target="_blank" rel="noopener"><span class="oc-icon">🌐</span><span class="oc-text"><span class="oc-label">项目主页</span><span class="oc-sub">gclef-cmu.edu/multtipop</span></span></a></div></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2607.08756" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2607.08756" target="_blank" rel="noopener">📑 PDF</a><a class="rsrc rsrc-proj" href="https://gclef-cmu.edu/multtipop" target="_blank" rel="noopener">🌐 项目主页</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>MulTTiPop是一个包含572段流行音乐的多轨MIDI转录数据集，用于评估自动音乐转录模型。
</div>

## 👥 作者与机构

**Nathan Pruyne** ¹ · Benjamin Stoler · William Chen · Chien-yu Huang · Shinji Watanabe · Chris Donahue

**机构**：卡内基梅隆大学

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合音乐信息检索和自动音乐转录领域的研究者。值得通读，重点关注数据集构建方法（§3）和评估结果（§4）。建议先看表1和表2了解数据集统计和基线性能。

## 🌍 研究背景

自动音乐转录（AMT）旨在将音频转换为符号表示（如MIDI）。现有数据集如MAESTRO和MusicNet主要涵盖古典钢琴音乐，缺乏流行音乐的多轨转录数据。这限制了AMT模型在流行音乐上的泛化能力。本文通过匹配Lakh MIDI和TheoryTab数据集，构建了首个大规模流行音乐多轨转录数据集MulTTiPop，填补了这一空白。

## 💡 核心创新

1. 基于元数据匹配的音频-MIDI对齐方法
2. 手动锚定节拍结合节拍跟踪的时序对齐
3. 首个大规模流行音乐多轨转录数据集
4. 覆盖1930s-2000s的多样化流行音乐

## 🏗️ 模型架构

数据集构建流程：从Lakh MIDI和TheoryTab中筛选流行音乐片段，通过元数据匹配（歌曲名、艺术家）获得候选对；手动标注音频与MIDI之间的锚定节拍；使用librosa的节拍跟踪算法提取音频节拍，并基于锚定节拍对MIDI进行时间扭曲，使其与音频节拍对齐。最终得到572段对齐的多轨MIDI和音频。

## 📚 数据集

- Lakh MIDI（匹配源，包含流行音乐MIDI）
- TheoryTab（匹配源，包含流行音乐MIDI）
- MulTTiPop（评估，572段，3.5小时）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| Onset F1 | MulTTiPop | 未明确给出单一基线，但最佳模型为38% | **38%** | N/A |

在MulTTiPop上评估了多个SOTA AMT模型，最佳模型（未具名）达到38%的Onset F1，表明现有模型在流行音乐多轨转录上仍有很大提升空间。数据集提供了多轨评估基准，但摘要未给出详细消融或跨数据集泛化结果。

## 🎯 结论与影响

MulTTiPop是首个面向流行音乐的多轨转录数据集，覆盖广泛年代和风格，为AMT研究提供了新基准。当前最佳模型仅38% Onset F1，表明该任务挑战性大，未来工作可探索多轨交互建模和领域自适应。数据集有望推动流行音乐转录的工业应用。

## ⚠️ 局限与未解决问题

数据集规模较小（3.5小时），且依赖现有MIDI数据集，可能引入偏差；对齐过程依赖手动标注，可扩展性有限；未提供模型在古典音乐上的对比，无法评估领域迁移效果；未报告推理效率或模型复杂度。

## 🔗 开源资源

- **项目主页**：<https://gclef-cmu.edu/multtipop>

---

<div class="paper-footer"><span>评分：7.5</span><span>原始：7.5</span><a href="/audio-paper-daily/posts/2026-07-10/">← 返回 2026-07-10 速递</a></div>
