---
title: "SketchSong: Hierarchical Song Generation with Sketch Planning and Fine-Grained Multi-Track Modeling"
date: 2026-06-03T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#音乐生成"]
summary: "提出SketchSong分层歌曲生成框架，通过高层草图规划与细粒度多轨建模提升歌曲编排连贯性与丰富性。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#音乐生成</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#歌曲生成</span> <span class="tag-pill tag-pill-soft">#分层生成</span> <span class="tag-pill tag-pill-soft">#多轨建模</span> <span class="tag-pill tag-pill-soft">#草图规划</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2606.03169</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-06-03</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2606.03169" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2606.03169" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出SketchSong分层歌曲生成框架，通过高层草图规划与细粒度多轨建模提升歌曲编排连贯性与丰富性。
</div>

## 👥 作者与机构

**Xiaoyue Duan** ¹ · Nanxing Hu · Yutang Feng · Xudong Yan · Jiatao Chen · Jinchao Zhang · Jie Zhou

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合音乐生成、多模态生成方向的研究者。建议重点阅读§3的草图规划与多轨建模部分，以及§4的实验结果。可先看表1与消融实验。

## 🌍 研究背景

现有歌曲生成系统虽能合成逼真音频，但生成完整歌曲仍面临两大挑战：一是缺乏显式的歌曲级编排规划，导致编排不连贯（如段落过渡弱、动态变化有限）；二是对音乐不同声部的粗粒度建模掩盖了其独特角色与交互，限制了编排丰富性。本文旨在解决这些问题。

## 💡 核心创新

1. 提出分层生成框架，先预测高层草图token再生成音频token
2. 沿时间维度采用粗到细的草图规划策略
3. 沿轨道维度显式建模人声、贝斯、鼓、其他乐器四轨
4. 无需后训练偏好优化即可与强基线竞争

## 🏗️ 模型架构

输入：压缩音频表示。主干：分层生成框架，包含草图规划器（预测高层草图token序列）和音频生成器（以草图token为条件生成音频token）。关键模块：草图token由压缩音频表示提取，音频生成器采用类似AudioLM的架构。输出：多轨音频（人声、贝斯、鼓、其他乐器）。参数量未提及。

## 📚 数据集

- 歌曲生成基准数据集（训练/评估，具体名称未给出）

## 📊 实验结果

实验在歌曲生成基准上进行，SketchSong在客观指标和主观听感上均优于基线。尽管未使用歌词或文本提示对齐的后训练偏好优化，SketchSong仍与经过后训练的强开源系统取得竞争性结果，验证了整体设计的有效性。具体数值未在摘要中给出。

## 🎯 结论与影响

SketchSong通过分层草图规划与细粒度多轨建模，有效提升了歌曲生成的编排连贯性与丰富性。该方法为歌曲生成提供了新的设计思路，未来可结合歌词或文本提示进一步优化。对工业应用而言，该框架有望简化歌曲制作流程。

## ⚠️ 局限与未解决问题

摘要未提及模型参数量、推理速度等效率指标；未报告消融实验细节；未明确数据集名称及规模；未与最新方法（如MusicGen、Stable Audio）进行对比；缺乏对草图token可解释性的分析。

---

<div class="paper-footer"><span>评分：7.8</span><span>原始：7.8</span><a href="/audio-paper-daily/posts/2026-06-03/">← 返回 2026-06-03 速递</a></div>
