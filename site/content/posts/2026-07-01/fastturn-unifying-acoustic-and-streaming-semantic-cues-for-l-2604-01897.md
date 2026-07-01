---
title: "FastTurn: Unifying Acoustic and Streaming Semantic Cues for Low-Latency and Robust Turn Detection"
date: 2026-07-01T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#语音交互"]
summary: "FastTurn提出统一声学与流式语义线索的框架，实现低延迟且鲁棒的话轮检测。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#语音交互</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#语音交互</span> <span class="tag-pill tag-pill-soft">#全双工对话</span> <span class="tag-pill tag-pill-soft">#话轮检测</span> <span class="tag-pill tag-pill-soft">#流式CTC</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2604.01897</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-07-01</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2604.01897" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2604.01897" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>FastTurn提出统一声学与流式语义线索的框架，实现低延迟且鲁棒的话轮检测。
</div>

## 👥 作者与机构

**Chengyou Wang** ¹ · Hongfei Xue · Chunjiang He · Jingbin Hu · Shuiyuan Wang · Bo Wu · Yuyu Ji · Jimeng Zheng · … 等 3 人

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合语音交互、全双工对话系统研究者。建议重点阅读§3方法部分和§4实验，特别是流式CTC与声学特征融合的设计。可先看表1和表2了解性能对比。

## 🌍 研究背景

现有全双工对话系统依赖语音活动检测（VAD）或ASR模块进行话轮检测，但VAD缺乏语义理解，ASR引入延迟且在重叠语音和噪声下性能下降。此外，缺乏真实交互场景的数据集限制了评估。本文旨在解决低延迟和鲁棒性兼顾的话轮检测问题。

## 💡 核心创新

1. 流式CTC与声学特征融合实现早期决策
2. 统一框架同时利用声学和语义线索
3. 发布基于真实对话的测试集
4. 低延迟中断决策机制

## 🏗️ 模型架构

FastTurn采用编码器-解码器架构。输入为声学特征（如Mel谱），通过流式CTC解码器输出部分语义token，同时保留声学特征。主干网络可能包含Conformer或类似结构，融合声学和语义线索进行话轮决策。输出为是否继续说话、让出或中断的决策。

## 📚 数据集

- 真实对话测试集（评估，包含话轮转换、重叠语音等）
- 可能使用模拟对话数据（训练）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| 决策准确率 | 真实对话测试集 | VAD基线（未给出具体值） | **更高（具体值未给出）** | 提升 |
| 中断延迟 | 真实对话测试集 | ASR基线（未给出具体值） | **更低（具体值未给出）** | 降低 |

实验表明FastTurn在决策准确率和中断延迟上均优于VAD和ASR基线，且在重叠语音和噪声条件下保持鲁棒。具体数值未在摘要中给出，但声称更高/更低。

## 🎯 结论与影响

FastTurn通过统一声学和流式语义线索，实现了低延迟且鲁棒的话轮检测，为全双工对话系统提供了有效方案。后续研究可探索更丰富的语义融合策略，工业落地可降低对话系统延迟。

## ⚠️ 局限与未解决问题

摘要未提供具体性能数值和消融实验，缺乏与更多基线（如基于Transformer的端到端方法）的对比。测试集规模未说明，可能影响泛化性。未报告模型参数量和推理延迟。

---

<div class="paper-footer"><span>评分：7.8</span><span>原始：7.8</span><a href="/audio-paper-daily/posts/2026-07-01/">← 返回 2026-07-01 速递</a></div>
