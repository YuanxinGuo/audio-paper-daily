---
title: "STAM-ASR: Speaker-Temporal Anchoring with Memory for Multi-Speaker ASR"
date: 2026-09-25T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#语音识别"]
summary: "STAM-ASR 用 AudioLLM 中间特征学习说话人活动与说话人感知表示，无需外部日志系统即可为多说话人 ASR 提供 who/when 线索。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#语音识别</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#多说话人ASR</span> <span class="tag-pill tag-pill-soft">#说话人日志</span> <span class="tag-pill tag-pill-soft">#AudioLLM</span> <span class="tag-pill tag-pill-soft">#记忆机制</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2609.29805</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-09-25</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2609.29805" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2609.29805" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>STAM-ASR 用 AudioLLM 中间特征学习说话人活动与说话人感知表示，无需外部日志系统即可为多说话人 ASR 提供 who/when 线索。
</div>

## 👥 作者与机构

**Victor Tolulope Olufemi** ¹ · Syeda Faiza Ahmed Sara · Shammur Absar Chowdhury

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合做多说话人 ASR、AudioLLM 适配、说话人感知建模的研究者阅读。建议重点看 §3 中说话人-时间锚定模块与固定大小记忆的设计，以及表 2 在 AMI/ICSI/LibriCSS/NOTSOFAR-1 上的跨域对比。若关注端到端日志替代方案，可通读；若只关心分离前端，可略读。

## 🌍 研究背景

多说话人 ASR 长期依赖外部说话人日志系统提供 who/when 线索，或先做语音分离再识别，流程复杂且误差累积。近期 AudioLLM 在单说话人 ASR 上表现强劲，但直接用于自然对话时，轮换、重叠与说话人重现仍导致识别与说话人归属困难。已有方法多需额外日志模块或分离前端，推理开销大且跨域鲁棒性不足。本文要解决的是：能否在不依赖外部日志与显式分离的前提下，让 AudioLLM 自身学会说话人-时间感知。

## 💡 核心创新

1. 从 AudioLLM 中间特征直接学习说话人活动与说话人感知表示
2. 用 who/when 线索调制语义表示，无需显式语音分离
3. 维护固定大小说话人记忆与对话记忆跨轮传递上下文

## 🏗️ 模型架构

输入为多说话人对话音频，经预训练 AudioLLM 提取中间层特征。STAM-ASR 在中间特征上并行接说话人活动预测头与说话人感知表示学习模块，得到 who/when 线索；这些线索以调制方式注入 AudioLLM 的语义表示，而非做波形分离。同时维护固定大小的说话人记忆与对话记忆，跨轮聚合互补上下文。最终由 AudioLLM 解码输出带说话人归属的文本。摘要未给出参数量与具体主干网络名。

## 📚 数据集

- AMI（评估，会议多说话人对话）
- ICSI（评估，会议多说话人对话）
- LibriCSS（评估，重叠与远场条件）
- NOTSOFAR-1（评估，跨域远场条件）

## 📊 实验结果

摘要仅给出定性结论：说话人-时间条件与记忆带来互补收益，且参考说话人活动与预测说话人活动之间的差距表明稳健说话人跟踪仍是关键挑战。未报告 SI-SDR、WER、cpWER 等具体数值，也未给出与 SEPFormer、Whisper、Qwen-Audio 等基线的定量对比，因此无法列表。

## 🎯 结论与影响

最强结论是：无需外部日志与显式分离，仅靠 AudioLLM 中间特征即可为多说话人 ASR 提供有效的说话人-时间锚定与记忆上下文。这为 AudioLLM 在自然对话场景的端到端适配提供了新思路，可能推动日志与识别进一步融合。工业落地方面，若推理开销可控，可简化会议转录与远场对话系统流水线。

## ⚠️ 局限与未解决问题

摘要未给出任何定量指标、参数量或推理延迟，难以判断相对强基线的实际增益。四个数据集均为评估集，未见训练数据与消融细节。作者也承认预测说话人活动与参考之间的差距，说明说话人跟踪仍不稳健。缺少与外部日志+ASR 级联方案的公平对比。

---

<div class="paper-footer"><span>评分：6.8</span><span>原始：6.8</span><a href="/audio-paper-daily/posts/2026-09-25/">← 返回 2026-09-25 速递</a></div>
