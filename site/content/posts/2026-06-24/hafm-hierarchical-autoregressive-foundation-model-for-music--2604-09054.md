---
title: "HAFM: Hierarchical Autoregressive Foundation Model for Music Accompaniment Generation"
date: 2026-06-24T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#音乐生成"]
summary: "提出分层自回归基础模型HAFM，通过双速率标记化和三阶段级联生成，实现人声引导的音乐伴奏生成。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero">
<div class="hero-score">
<div class="score-num">8.2</div>
<div class="score-stars">★★★★☆</div>
<div class="score-tier">前25%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#音乐生成</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#音乐伴奏生成</span> <span class="tag-pill tag-pill-soft">#自回归生成</span> <span class="tag-pill tag-pill-soft">#分层编码</span> <span class="tag-pill tag-pill-soft">#音频生成</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2604.09054</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-06-24</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner"><div class="oc-headline"><span class="oc-pulse"></span><span class="oc-title">本论文已开源</span><span class="oc-hint">点击下方卡片直达对应资源</span></div><div class="oc-grid"><a class="oc-chip oc-chip-code" href="https://github.com/HackerHyper/HAFM.git" target="_blank" rel="noopener"><span class="oc-icon">💻</span><span class="oc-text"><span class="oc-label">代码仓库</span><span class="oc-sub">HackerHyper/HAFM.git</span></span></a></div></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2604.09054" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2604.09054" target="_blank" rel="noopener">📑 PDF</a><a class="rsrc rsrc-code" href="https://github.com/HackerHyper/HAFM.git" target="_blank" rel="noopener">💻 代码</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出分层自回归基础模型HAFM，通过双速率标记化和三阶段级联生成，实现人声引导的音乐伴奏生成。
</div>

## 👥 作者与机构

**Jian Zhu** ¹ · Jianwei Cui · Yunlong Xue · Shihao Chen · Yubang Zhang · Cheng Luo · Jun Sun

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合音乐生成、音频生成方向的研究者。建议重点阅读§3.2双速率标记化策略和§3.3三阶段级联框架，以及表1的客观指标对比。可先看§4实验部分了解性能提升。

## 🌍 研究背景

音乐伴奏生成旨在根据人声输入自动生成节奏、和声、音色协调的乐器伴奏，在个性化音乐创作、编曲辅助和音乐教育中有广泛应用。现有方法主要基于符号域或单阶段音频生成框架，普遍存在高层语义结构建模不足、声学细节重建有限、条件可控性弱等问题。本文提出HAFM模型，通过分层自回归框架解决上述局限。

## 💡 核心创新

1. 双速率标记化：50Hz HuBERT语义标记+75Hz EnCodec声学标记
2. 三阶段级联生成：语义→粗声学→细声学逐步细化
3. 语义与声学表征显式解耦
4. 自回归基础模型架构

## 🏗️ 模型架构

输入为歌声音频，首先通过双速率标记化提取50Hz HuBERT语义标记和75Hz EnCodec声学标记。然后采用三阶段级联自回归生成：第一阶段生成语义标记，第二阶段以语义标记为条件生成粗声学标记，第三阶段以语义和粗声学标记为条件生成细声学标记。整体为自回归Transformer架构，逐步从全局结构到局部细节生成伴奏。

## 📚 数据集

- MUSDB18（训练和评估，包含150首多轨歌曲）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| FAD | MUSDB18 | 两阶段基线 2.10 | **1.71** | -0.39 (18.6%相对提升) |

在MUSDB18数据集上，三阶段模型FAD为1.71，相比两阶段基线（2.10）提升18.6%。主观听测中，生成伴奏与真实伴奏对比获得51.5%偏好率，在节奏对齐、和声兼容性和整体音乐连贯性上显著优于随机基线。

## 🎯 结论与影响

HAFM通过分层自回归框架有效提升了音乐伴奏生成的质量，双速率标记化和三阶段级联策略为语义-声学解耦提供了新思路。该方法有望推动个性化音乐创作和编曲辅助工具的发展，并为音频生成中的分层建模提供参考。

## ⚠️ 局限与未解决问题

仅使用MUSDB18数据集，规模有限；未报告模型参数量和推理速度；缺乏与更多基线（如MusicGen、Jukebox）的对比；主观测试样本量未明确。

## 🔗 开源资源

- **代码**：<https://github.com/HackerHyper/HAFM.git>

---

<div class="paper-footer"><span>评分：8.2</span><span>原始：8.2</span><a href="/audio-paper-daily/posts/2026-06-24/">← 返回 2026-06-24 速递</a></div>
