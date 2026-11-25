---
title: "VividAudio: Multi-Event Reference-Conditioned Video-to-Audio Generation"
date: 2026-11-25T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#音频生成"]
summary: "提出多事件参考条件视频到音频生成任务，用时间对齐复合参考与路由机制控制各事件音色。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero">
<div class="hero-score">
<div class="score-num">7.2</div>
<div class="score-stars">★★★★☆</div>
<div class="score-tier">前25%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#音频生成</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#视频到音频生成</span> <span class="tag-pill tag-pill-soft">#参考条件控制</span> <span class="tag-pill tag-pill-soft">#多事件音频</span> <span class="tag-pill tag-pill-soft">#Foley生成</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2611.32458</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-11-24</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2611.32458" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2611.32458" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出多事件参考条件视频到音频生成任务，用时间对齐复合参考与路由机制控制各事件音色。
</div>

## 👥 作者与机构

**You Li** ¹ · Dewei Zhou · Fan Ma · Dongliang He · Yi Yang

**机构**：浙江大学

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合做 V2A / 可控音频生成的研究者阅读。建议通读：重点看 §3 的 IntraEvtVar 数据构造与 TACO-Ref 双路径注入，以及 §4 中 TRR 路由与 localized reference attention 的消融；表 2 的参考可控性指标是核心证据。

## 🌍 研究背景

V2A 生成已能合成高质量 Foley 音效，主流方法基于扩散或自回归主干在 VGGSound 上做条件生成。但现有方法只能整体控制音频风格，无法为视频中多个事件分别指定声学身份（音色/材质）。用户导向创作需要事件级参考控制，而事件级参考-目标配对数据稀缺，且多参考联合条件易导致声学属性跨事件泄漏，本文即针对这两点。

## 💡 核心创新

1. 提出 Mr-V2A 任务：每事件绑定音频参考与时间跨度
2. IntraEvtVar 用视频内事件四种变化模式构造非 oracle 配对
3. TACO-Ref 时间对齐复合参考 + 局部/全局双路径注入
4. Audio Q-Former 提供 clip 级声学上下文条件
5. TRR 路由与 localized reference attention 抑制属性泄漏

## 🏗️ 模型架构

输入为视频帧序列与若干事件级音频参考及其目标时间跨度。参考按时间对齐组织为 TACO-Ref 复合表示，分两路注入：局部路径保留时间分辨的事件线索，经 localized reference attention 约束事件-参考对应；全局路径由 Audio Q-Former 将参考压缩为 clip 级声学上下文 token。主干为条件生成网络（摘要未明示具体骨干），融合视频特征与双路参考条件后输出目标音频。TACO-Ref Router 显式路由各事件参考以降低跨事件干扰。摘要未给出参数量。

## 📚 数据集

- VGGSound-Ref（评估，参考条件 V2A）
- VividBench（评估，自建基准）
- 视频内事件挖掘数据（训练，IntraEvtVar 构造非 oracle 配对）

## 📊 实验结果

摘要仅给出定性结论：在 VGGSound-Ref 与 VividBench 上参考可控性强于现有 V2A 与 exemplar-based 方法，同时 Foley 生成质量保持竞争力。未披露 FAD、IS、CLAP 分数或主观 MOS 等具体数值，也无效率指标，需查阅正文表格确认提升幅度。

## 🎯 结论与影响

最强结论是事件级参考条件可在不牺牲 Foley 质量的前提下显著提升可控性。该任务定义与 IntraEvtVar 数据构造可能成为后续可控 V2A 研究的参照设定；对影视/游戏音效制作的用户导向生成有直接落地价值。

## ⚠️ 局限与未解决问题

摘要未给定量结果与消融细节，难以判断 TRR 与局部注意各自的贡献；IntraEvtVar 由视频内事件挖掘构造，可能引入与真实用户参考分布不匹配的 bias；未报推理延迟与多参考数量扩展性；对比基线范围未说明。

---

<div class="paper-footer"><span>评分：7.2</span><span>原始：7.2</span><a href="/audio-paper-daily/posts/2026-11-25/">← 返回 2026-11-25 速递</a></div>
