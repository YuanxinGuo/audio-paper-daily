---
title: "Sounding Surgical Instrument Localisation through Audio-Visual Correspondence"
date: 2026-10-26T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#声学事件定位"]
summary: "用单麦克风与相机学习手术器械外观与声音的对应关系，弱监督生成发声器械热力图。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero">
<div class="hero-score">
<div class="score-num">6.5</div>
<div class="score-stars">★★★☆☆</div>
<div class="score-tier">中等</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#声学事件定位</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#音视频对应</span> <span class="tag-pill tag-pill-soft">#弱监督定位</span> <span class="tag-pill tag-pill-soft">#手术场景理解</span> <span class="tag-pill tag-pill-soft">#声源定位</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2610.32816</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-10-26</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2610.32816" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2610.32816" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>用单麦克风与相机学习手术器械外观与声音的对应关系，弱监督生成发声器械热力图。
</div>

## 👥 作者与机构

**Dominic Behling** ¹ · Jonas Hein · Matthias Seibold

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合做音视频弱监督定位、手术室感知的研究者阅读。属于概念验证，方法本身较直接（音视频对应+热力图），建议重点看 §3 的损失设计（silence 项与 composite 项）和跨设备独立语料的泛化实验，无需逐节精读。

## 🌍 研究背景

手术场景理解目前主要依赖视觉数据，声学感知被视为可提供互补信息。此前手术活动定位多依赖麦克风阵列与声学波束成形，需要多通道硬件与空间标注。本文要解决的问题是：能否仅用单个麦克风加一台相机，在没有任何位置标注的情况下，定位正在发声的手术器械，从而降低硬件与标注成本。

## 💡 核心创新

1. 将弱监督音视频对应定位迁移到手术场景
2. 引入 silence 项抑制静音与背景噪声输出
3. 引入 composite 项在双器械时选择发声者
4. 跨相机与麦克风的独立语料验证泛化

## 🏗️ 模型架构

输入为单通道音频与同步视频帧；音频分支提取声学特征，视觉分支提取器械外观特征，通过音视频对应学习将声音与器械外观关联，输出覆盖发声器械的热力图。训练为弱监督，不使用任何空间位置标注。在基础训练目标上增加 silence 项（静音与背景噪声时抑制输出）与 composite 项（两件可见器械中选出正在发声的一件）。摘要未给出参数量与具体主干网络名。

## 📚 数据集

- 自采模拟手术动作录音（锯、钻、凿，训练）
- 独立采集语料（不同相机与麦克风，光学跟踪提供器械位置，评估）

## 📊 实验结果

摘要未给出 SI-SDR、PESQ 等定量指标，仅定性说明：模型能在不同相机与麦克风采集的独立语料上定位发声器械，能将器械活动与静音、背景噪声区分，并在两件器械同时出现时正确归属声音。缺少与波束成形基线的定量对比及消融数值。

## 🎯 结论与影响

最强结论是：仅凭单麦克风与相机、无需位置标注，即可通过音视频对应定位发声手术器械。这为手术室活动感知提供了一条低标注成本的新范式，若后续量化验证充分，对智能手术系统与术中上下文感知有潜在价值。

## ⚠️ 局限与未解决问题

属概念验证，摘要无任何定量指标与基线对比，silence 项与 composite 项的消融效果未量化；仅覆盖锯、钻、凿三类模拟动作，真实手术场景与多器械干扰未验证；未报告推理延迟与实时性。

---

<div class="paper-footer"><span>评分：6.5</span><span>原始：6.5</span><a href="/audio-paper-daily/posts/2026-10-26/">← 返回 2026-10-26 速递</a></div>
