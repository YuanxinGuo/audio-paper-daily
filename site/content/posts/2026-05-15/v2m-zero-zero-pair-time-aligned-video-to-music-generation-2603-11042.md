---
title: "V2M-Zero: Zero-Pair Time-Aligned Video-to-Music Generation"
date: 2026-05-15T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#音乐生成"]
summary: "提出V2M-ZERO，利用模态内事件曲线实现零配对数据的视频到音乐时间对齐生成，性能超越有监督方法。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero">
<div class="hero-score">
<div class="score-num">8.5</div>
<div class="score-stars">★★★★☆</div>
<div class="score-tier">前10%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#音乐生成</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#视频到音乐生成</span> <span class="tag-pill tag-pill-soft">#时间对齐</span> <span class="tag-pill tag-pill-soft">#零样本学习</span> <span class="tag-pill tag-pill-soft">#可控生成</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2603.11042</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-05-15</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">🔥 强烈推荐通读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2603.11042" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2603.11042" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出V2M-ZERO，利用模态内事件曲线实现零配对数据的视频到音乐时间对齐生成，性能超越有监督方法。
</div>

## 👥 作者与机构

**Yan-Bo Lin** ¹ · Jonah Casebeer · Long Mai · Aniruddha Mahapatra · Gedas Bertasius · Nicholas J. Bryan

**机构**：北卡罗来纳大学教堂山分校 · Adobe Research

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合音乐生成、多模态对齐方向的研究者。建议通读，重点看§3的事件曲线提取与训练策略，以及§4的定量结果（表1-3）和消融实验。可复现代码（若开源）验证事件曲线对齐效果。

## 🌍 研究背景

现有文本到音乐模型缺乏细粒度时间控制，难以生成与视频事件对齐的音乐。先前工作依赖视频-音乐配对数据，但获取困难且泛化性差。本文观察到时间同步的关键在于匹配变化的时间点和幅度，而非语义内容，从而提出利用模态内相似度计算事件曲线，实现无需配对数据的跨模态时间对齐。

## 💡 核心创新

1. 提出事件曲线（event curves）表征模态内时间变化
2. 零配对数据训练策略：在音乐事件曲线上微调文本到音乐模型
3. 解耦的时间同步与语义控制（风格、情绪）
4. 推理时直接替换为视频事件曲线，无需跨模态训练

## 🏗️ 模型架构

基于预训练文本到音乐模型（如MusicGen），输入视频帧序列。首先用预训练视频编码器（如CLIP）和音乐编码器（如CLAP）分别提取帧级特征，计算帧间余弦相似度得到事件曲线。训练阶段，用音乐事件曲线作为条件微调文本到音乐模型；推理阶段，将视频事件曲线替换音乐曲线，与文本提示（风格、情绪）共同输入生成音乐。模型输出为44.1kHz立体声音频。

## 📚 数据集

- OES-Pub（评估，包含视频-音乐对）
- MovieGenBench-Music（评估，电影片段-音乐对）
- AIST++（评估，舞蹈视频-音乐对）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| FAD（音频质量） | OES-Pub | CLaMP+ 3.12 | **2.96** | -0.16 |
| CLIP Score（语义对齐） | OES-Pub | CLaMP+ 0.178 | **0.201** | +0.023 |
| Temporal Sync（时间同步） | OES-Pub | CLaMP+ 0.112 | **0.136** | +0.024 |
| Beat Alignment（节拍对齐） | AIST++ | CLaMP+ 0.125 | **0.160** | +0.035 |

在三个基准上，V2M-ZERO以零配对数据超越所有基线，音频质量提升5-9%，语义对齐提升13-15%，时间同步提升21-52%，舞蹈视频节拍对齐提升28%。大规模主观听测验证了客观指标。消融实验表明事件曲线优于直接使用特征，且解耦控制有效。

## 🎯 结论与影响

V2M-ZERO证明通过模态内事件曲线实现时间对齐是有效且优于跨模态监督的方法。该方法无需配对数据，可独立控制时间与风格，为视频到音乐生成提供了新范式。未来可扩展至其他视听生成任务，并有望降低工业应用中数据收集成本。

## ⚠️ 局限与未解决问题

依赖预训练编码器质量，事件曲线可能无法捕捉细微时间结构；未报告推理速度与模型参数量；仅在特定数据集评估，泛化性需进一步验证；可控性限于文本提示，缺乏更精细的局部控制。

---

<div class="paper-footer"><span>评分：8.5</span><span>原始：8.5</span><a href="/audio-paper-daily/posts/2026-05-15/">← 返回 2026-05-15 速递</a></div>
