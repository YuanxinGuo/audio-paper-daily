---
title: "MusTBENCH: Benchmarking and Advancing Temporal Grounding in Music LLMs"
date: 2026-05-29T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#音乐理解"]
summary: "提出MusTBENCH基准测试音乐大模型的时间定位能力，并设计MusT四阶段优化方案显著提升性能。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#音乐理解</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#大语言模型</span> <span class="tag-pill tag-pill-soft">#时间定位</span> <span class="tag-pill tag-pill-soft">#基准测试</span> <span class="tag-pill tag-pill-soft">#音乐理解</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2605.29300</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-05-29</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2605.29300" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2605.29300" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出MusTBENCH基准测试音乐大模型的时间定位能力，并设计MusT四阶段优化方案显著提升性能。
</div>

## 👥 作者与机构

**Daeyong Kwon** ¹ · Qiyu Wu · Shinobu Kuriya · Junghyun Koo · Shuyang Cui · Zhi Zhong · Wei-Hsiang Liao · Hiromi Wakaki · … 等 1 人

**机构**：索尼

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合音乐AI、多模态LLM研究者。重点读§3（MusTBENCH任务设计）和§4（MusT优化方案）。若关注时间定位，建议复现MusT方法。

## 🌍 研究背景

现有大型音频语言模型（LALMs）在音乐理解中展现出潜力，但其回答是否基于正确的音频时间区域尚未被充分探索。音乐中关键信息常为时间局部事件（如乐器进入、节奏变化），而当前模型缺乏精确时间定位能力。本文旨在填补这一空白，通过构建专家验证的基准测试并设计优化方案。

## 💡 核心创新

1. 提出MusTBENCH基准，含5个时间定位问答任务
2. 设计MusT四阶段时间优化方案
3. 结合音乐编码器适配、LLM适配、监督微调和RL优化
4. 揭示现有LALMs时间定位能力缺失

## 🏗️ 模型架构

MusT优化方案包含四阶段：1) 音乐编码器适配（如CLAP）；2) LLM适配（如LLaMA）；3) LLM监督微调；4) 基于强化学习的优化。整体流程将音频编码器输出与LLM对齐，通过时间定位任务进行端到端训练。

## 📚 数据集

- MusTBENCH（评估，含5个时间定位任务，专家验证）

## 📊 实验结果

摘要未提供具体数值，但指出现有LALMs在MusTBENCH上表现不佳，而MusT带来显著提升。实验表明时间定位是当前LALMs缺失的关键能力。

## 🎯 结论与影响

本文证实时间定位是当前LALMs的关键缺失能力，MusTBENCH可作为未来研究的挑战性基准。MusT优化方案为提升时间定位提供了有效路径，有望推动音乐理解LLM的落地应用。

## ⚠️ 局限与未解决问题

摘要未报告具体指标和消融实验，缺乏与现有方法的定量对比。未提及推理效率或模型规模影响。基准测试仅覆盖5个任务，可能未涵盖所有时间定位场景。

---

<div class="paper-footer"><span>评分：7.5</span><span>原始：7.5</span><a href="/audio-paper-daily/posts/2026-05-29/">← 返回 2026-05-29 速递</a></div>
