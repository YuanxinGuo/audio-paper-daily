---
title: "TiCo: Time-Controllable Spoken Dialogue Model"
date: 2026-05-14T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#强化学习", "#指令跟随", "#时间可控", "#语音对话模型", "#语音对话系统"]
summary: "提出TiCo，首个时间可控的语音对话模型，通过口语时间标记和强化学习实现时长控制，在TiCo-Bench上降低时长误差2.7倍。"
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
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#时间可控</span> <span class="tag-pill tag-pill-soft">#语音对话模型</span> <span class="tag-pill tag-pill-soft">#强化学习</span> <span class="tag-pill tag-pill-soft">#指令跟随</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2603.22267</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-05-14</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2603.22267" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2603.22267" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出TiCo，首个时间可控的语音对话模型，通过口语时间标记和强化学习实现时长控制，在TiCo-Bench上降低时长误差2.7倍。
</div>

## 👥 作者与机构

**Kai-Wei Chang** ¹ · Wei-Chih Chen · En-Pei Hu · Hung-yi Lee · James Glass

**机构**：MIT · National Taiwan University

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合语音对话系统、人机交互研究者。建议通读，重点看§3方法（STM与RL训练）和§4实验（表1/2）。可复现其训练流程。

## 🧩 模型一栏概览

| 项 | 内容 |
| --- | --- |
| **应用场景** | 语音助手或交互代理需按指令生成指定时长语音回复的场景。 |
| **核心创新** | 提出口语时间标记（STM）实现生成中时长感知 · 首个时间可控语音对话基准TiCo-Bench · 无需问答配对数据，用自生成+可验证奖励的RL高效后训练 |
| **模型架构** | 基于预训练语音对话模型（如SpeechGPT）作为backbone，输入文本指令+语音上下文，主干为Transformer解码器，关键模块为插入的STM token（如<10.6秒>），输出语音token序列。参数量未明确给出。 |
| **数据集** | TiCo-Bench（评估） · 未明确训练数据集（基于backbone原有数据） |
| **关键结果** | TiCo在TiCo-Bench上将时长误差降低至backbone的2.7倍，比最强基线（如GPT-4o+语音）低1.6倍，同时保持响应质量（MOS相近）。 |

## 🎯 与本站重点领域的关联

与本站重点领域无直接关联，但语音对话模型可应用于语音增强后的下游任务，其时间控制思路可迁移至语音分离/增强中的时长约束生成。

## ⚠️ 局限与未解决问题

未报告推理延迟；STM token的插入策略可能影响自然度；仅在单一backbone上验证，泛化性未知；TiCo-Bench规模较小。

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

<div class="paper-footer"><span>评分：8.2</span><span>原始：8.2</span><a href="/posts/2026-05-14/">← 返回 2026-05-14 速递</a></div>
