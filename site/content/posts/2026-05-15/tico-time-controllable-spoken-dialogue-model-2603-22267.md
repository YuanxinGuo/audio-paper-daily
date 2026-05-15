---
title: "TiCo: Time-Controllable Spoken Dialogue Model"
date: 2026-05-15T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#强化学习", "#时间可控", "#语音对话模型", "#语音对话系统", "#语音生成"]
summary: "TiCo通过引入口语时间标记和强化学习后训练，使语音对话模型能按时间约束生成指定时长的语音回复，在TiCo-Bench上时长误差降低2.7倍。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#语音对话系统</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#时间可控</span> <span class="tag-pill tag-pill-soft">#语音对话模型</span> <span class="tag-pill tag-pill-soft">#强化学习</span> <span class="tag-pill tag-pill-soft">#语音生成</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2603.22267</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-05-15</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2603.22267" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2603.22267" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>TiCo通过引入口语时间标记和强化学习后训练，使语音对话模型能按时间约束生成指定时长的语音回复，在TiCo-Bench上时长误差降低2.7倍。
</div>

## 👥 作者与机构

**Kai-Wei Chang** ¹ · Wei-Chih Chen · En-Pei Hu · Hung-yi Lee · James Glass

**机构**：MIT · National Taiwan University

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合语音对话系统、人机交互研究者阅读。建议重点看§3方法（STM与RL训练）和§4实验（表1、表2）。可先读摘要和§1引言了解动机。

## 🧩 模型一栏概览

| 项 | 内容 |
| --- | --- |
| **应用场景** | 语音助手或交互代理需要生成指定时长语音回复的场景。 |
| **核心创新** | 提出Spoken Time Markers (STM)让模型在生成时感知已用时间 · 构建首个时间可控指令跟随基准TiCo-Bench · 无需问答配对数据，通过自生成和可验证奖励的RL高效后训练 |
| **模型架构** | 基于预训练语音对话模型（如Mini-Omni）作为backbone，输入文本指令+语音历史，输出语音token序列。在解码过程中插入STM标记（如<10.6 seconds>）以感知时间，通过RL优化时长控制。参数量未明确给出。 |
| **数据集** | TiCo-Bench（时间可控指令跟随评估） · 自生成训练数据（模型自身生成带STM的语音） |
| **关键结果** | TiCo在TiCo-Bench上将时长误差降低至backbone的2.7倍、最强基线的1.6倍，同时保持响应质量（MOS等指标未降）。具体数值见论文表1、表2。 |

## 🎯 与本站重点领域的关联

与本站重点领域无直接关联。但语音增强/分离中的时长控制思路可迁移至对话系统；双耳音频中时间同步问题也可借鉴其时间标记方法。

## ⚠️ 局限与未解决问题

仅验证了短时长（~15秒）控制，长时长泛化性未知；STM插入可能影响自然度；依赖预训练SDM质量；未报告推理延迟。

## 📋 引用

```bibtex
@article{chang20262603,
  title  = {TiCo: Time-Controllable Spoken Dialogue Model},
  author = {Kai-Wei Chang and  Wei-Chih Chen and  En-Pei Hu and  Hung-yi Lee and  James Glass},
  journal = {arXiv preprint arXiv:2603.22267},
  year   = {2026}
}
```

---

<div class="paper-footer"><span>评分：8.2</span><span>原始：8.2</span><a href="/posts/2026-05-15/">← 返回 2026-05-15 速递</a></div>
