---
title: "Wan-Streamer v0.1: End-to-end Real-time Interactive Foundation Models"
date: 2026-06-25T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#多模态交互"]
summary: "提出Wan-Streamer，一个原生流式、端到端的多模态交互基础模型，统一建模语言、音频和视频，实现约200ms模型响应延迟和550ms总交互延迟。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#多模态交互</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#流式模型</span> <span class="tag-pill tag-pill-soft">#全双工</span> <span class="tag-pill tag-pill-soft">#低延迟</span> <span class="tag-pill tag-pill-soft">#端到端</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2606.25041</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-06-25</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2606.25041" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2606.25041" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出Wan-Streamer，一个原生流式、端到端的多模态交互基础模型，统一建模语言、音频和视频，实现约200ms模型响应延迟和550ms总交互延迟。
</div>

## 👥 作者与机构

**Lianghua Huang** ¹ · Zhifan Wu · Wei Wang · Yupeng Shi · Mengyang Feng · Junjie He · Chenwei Xie · Yu Liu · … 等 16 人

**机构**：阿里巴巴

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合从事多模态交互、语音对话系统、实时通信的研究者。建议重点阅读§3（模型架构）和§4（延迟分析），特别是块因果注意力和流式调度机制。可对比现有级联系统的延迟和性能。

## 🌍 研究背景

现有交互系统通常采用级联架构，依赖独立的VAD、ASR、TTS、视频生成等模块，导致流水线延迟累积和错误传播。尽管端到端模型在单一模态（如语音）上有所进展，但多模态实时交互仍面临流式处理、低延迟和跨模态同步的挑战。本文旨在设计一个统一的基础模型，原生支持流式全双工音频-视觉交互。

## 💡 核心创新

1. 原生流式端到端架构，无需外部模块
2. 块因果注意力机制支持增量流式处理
3. 因果编码器和解码器设计
4. 低延迟多模态令牌调度，160ms流式单元
5. 统一建模语言、音频、视频输入输出

## 🏗️ 模型架构

输入为交错的视觉、音频和文本令牌序列，输出同样为多模态令牌。采用单一Transformer架构，通过块因果注意力实现增量流式处理。编码器和解码器均为因果设计，支持流式。多模态令牌调度器协调不同模态的生成时序，实现低延迟交互。模型侧响应延迟约200ms，总交互延迟约550ms（含350ms网络延迟）。

## 📚 数据集

- 未在摘要中明确提及

## 📊 实验结果

摘要未提供具体指标对比，仅报告了延迟数据：模型侧响应延迟约200ms，总交互延迟约550ms（含350ms网络延迟），支持160ms流式单元。未提供与其他系统的定量比较。

## 🎯 结论与影响

Wan-Streamer作为首个原生流式端到端多模态交互基础模型，实现了亚秒级全双工音频-视觉通信。其统一架构消除了级联系统的延迟和错误累积，为实时多模态交互提供了新范式。未来可能推动语音助手、虚拟人、远程协作等领域的工业落地。

## ⚠️ 局限与未解决问题

摘要未提供与现有系统的定量对比（如延迟、质量指标），缺乏消融实验和跨数据集泛化评估。未报告模型参数量、计算成本及在标准基准（如语音识别、生成质量）上的表现。网络延迟假设为350ms，实际场景可能变化。

---

<div class="paper-footer"><span>评分：8.5</span><span>原始：8.5</span><a href="/audio-paper-daily/posts/2026-06-25/">← 返回 2026-06-25 速递</a></div>
