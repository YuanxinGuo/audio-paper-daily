---
title: "Automatic Lyric Transcription for Greek Songs: Scaling and Task Composition Effects in Whisper Adaptation"
date: 2026-09-11T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#歌词转录"]
summary: "首个希腊语歌词转录基准，系统研究Whisper规模、多任务比例与两阶段语音到歌唱适配的影响。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#歌词转录</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#Whisper微调</span> <span class="tag-pill tag-pill-soft">#低资源语言</span> <span class="tag-pill tag-pill-soft">#多任务学习</span> <span class="tag-pill tag-pill-soft">#歌唱语音处理</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2609.11302</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-09-11</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2609.11302" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2609.11302" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>首个希腊语歌词转录基准，系统研究Whisper规模、多任务比例与两阶段语音到歌唱适配的影响。
</div>

## 👥 作者与机构

**Maria Frangiadaki** ¹ · Dimitrios Damianos · Kosmas Kritsis · Vassilis Katsouros

**机构**：雅典研究创新中心

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合做低资源语音/歌唱转录与Whisper适配的研究者阅读。建议重点看§3的数据构建流程（源分离+CTC强制对齐）与多任务比例实验，表2的规模对比可快速浏览。若关注ALT工程落地，可复现两阶段适配配方。

## 🌍 研究背景

自动歌词转录（ALT）因旋律起伏、节奏不规则与伴奏干扰，远难于常规ASR；希腊语等低资源语言此前无ALT基准。现有工作多依赖通用ASR模型零样本迁移，缺乏对模型规模、任务组合与适配策略的系统分析。本文针对希腊语构建首个ALT基准，并研究Whisper在不同容量与训练配置下的适配效果。

## 💡 核心创新

1. 首个希腊语ALT基准与分段对齐数据集
2. 系统分析Whisper模型规模对ALT的影响
3. 多任务transcribe-translate比例作为正则化
4. 两阶段语音到歌唱适配策略

## 🏗️ 模型架构

输入为歌唱音频的log-Mel特征，主干采用Whisper编码器-解码器（Tiny至Large-v3多规模）。数据侧先用源分离去除伴奏，再用CTC强制对齐生成分段级歌词标注。训练分两阶段：先在语音数据上适配，再迁移到歌唱数据；同时以transcribe/translate多任务比例联合训练，输出为歌词token序列。

## 📚 数据集

- Greek Audio Dataset（GAD，训练/评估，经源分离与CTC对齐构建）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| WER | Greek ALT benchmark | Whisper Large-v3 zero-shot | **27.2%** | 显著下降（摘要未给具体基线值） |

摘要报告两阶段适配的Whisper Large-v3达到27.2% WER，显著优于零样本基线；规模扩大持续提升性能，多任务学习主要对小容量模型起正则化作用。摘要未给出各规模的具体WER、消融细节与推理效率数据。

## 🎯 结论与影响

本文确立首个希腊语ALT基准，证明规模扩展与两阶段语音到歌唱适配对Whisper有效。该基准与配方可推动低资源歌唱转录研究，并为音乐歌词检索、卡拉OK对齐等应用提供可复用流程。

## ⚠️ 局限与未解决问题

仅覆盖希腊语单一语言，数据规模与歌手多样性未知；未报告推理延迟与参数量；多任务比例的最优区间缺乏细粒度消融；与专用ALT模型的对比缺失。

---

<div class="paper-footer"><span>评分：6.8</span><span>原始：6.8</span><a href="/audio-paper-daily/posts/2026-09-11/">← 返回 2026-09-11 速递</a></div>
