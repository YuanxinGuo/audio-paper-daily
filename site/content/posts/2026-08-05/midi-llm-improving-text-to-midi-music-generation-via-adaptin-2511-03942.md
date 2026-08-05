---
title: "MIDI-LLM: Improving Text-to-MIDI Music Generation via Adapting Large Language Models"
date: 2026-08-05T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#音乐生成"]
summary: "MIDI-LLM通过扩展LLM词汇表并采用两阶段训练，显著提升文本到MIDI生成的质量与可控性，并在真实创作场景中验证了其有效性。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#音乐生成</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#文本到MIDI生成</span> <span class="tag-pill tag-pill-soft">#大语言模型</span> <span class="tag-pill tag-pill-soft">#多任务学习</span> <span class="tag-pill tag-pill-soft">#人机共创</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2511.03942</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-08-05</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2511.03942" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2511.03942" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>MIDI-LLM通过扩展LLM词汇表并采用两阶段训练，显著提升文本到MIDI生成的质量与可控性，并在真实创作场景中验证了其有效性。
</div>

## 👥 作者与机构

**Shih-Lun Wu** ¹ · Dave Carlton · Ryan Miyakawa · Yoon Kim · Chris Donahue · Cheng-Zhi Anna Huang

**机构**：麻省理工学院 · 卡内基梅隆大学 · 谷歌

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合音乐生成、多模态LLM研究者及音乐科技从业者阅读。建议重点阅读第3节方法（两阶段训练）与第5节实验（消融与用户研究），可先看§3.2与表2。

## 🌍 研究背景

文本到MIDI生成旨在根据自然语言描述生成多轨音乐，但现有模型如Text2midi在文本控制与音乐质量上仍有不足。大语言模型（LLM）在文本理解上优势明显，但直接用于MIDI生成面临词汇表不匹配和训练数据不足的问题。本文提出MIDI-LLM，通过扩展LLM词汇表并采用两阶段训练，将LLM的文本能力与MIDI生成结合，以提升生成质量与可控性。

## 💡 核心创新

1. 扩展LLM词汇表以包含MIDI token，实现文本与MIDI的统一建模
2. 两阶段训练：单模态继续预训练+多模态监督微调
3. 基于Llama 3.2 (1B)的实例化，优于Text2midi
4. 针对lead sheet生成与填充的微调，适配真实创作流程
5. 大规模真实用户研究验证有效性

## 🏗️ 模型架构

MIDI-LLM基于Llama 3.2 (1B)架构，输入为文本与MIDI token序列。首先扩展词汇表，将MIDI事件（如音符、和弦）映射为token。训练分两阶段：第一阶段在音乐相关文本和独立MIDI数据上进行单模态继续预训练，第二阶段在文本-MIDI对上进行多模态监督微调。推理时支持文本条件生成，并可集成vLLM等优化推理框架。

## 📚 数据集

- 音乐相关文本（单模态预训练）
- 独立MIDI（单模态预训练）
- 文本-MIDI对（多模态微调）
- TheoryTab（lead sheet微调）

## 📊 实验结果

摘要未提供具体数值指标，但提到MIDI-LLM在文本控制和音乐质量上优于Text2midi，并通过消融实验验证了各训练阶段的有效性。此外，在58名Hookpad Aria用户和4002个生成输出的真实用户研究中，MIDI-LLM在零到一lead sheet生成中取得了最高接受率。

## 🎯 结论与影响

MIDI-LLM通过扩展LLM词汇表并采用两阶段训练，显著提升了文本到MIDI生成的质量与可控性，并在真实创作场景中验证了其有效性。该方法为音乐生成领域提供了新思路，即利用LLM的文本理解能力增强音乐生成，有望推动人机共创工具的发展。

## ⚠️ 局限与未解决问题

摘要未提及明显局限，但作为审稿人可看出：未报告具体指标（如BLEU、音乐质量评分），缺乏与更多基线（如MusicGen）的对比，且用户研究仅针对lead sheet生成，未覆盖多轨生成场景。此外，模型规模较小（1B），可能限制复杂音乐结构的学习。

---

<div class="paper-footer"><span>评分：8.2</span><span>原始：8.2</span><a href="/audio-paper-daily/posts/2026-08-05/">← 返回 2026-08-05 速递</a></div>
