---
title: "Textraction: Unified Text-Guided Speaker Extraction and Enhancement for Single- and Multi-Channel Audio"
date: 2026-11-10T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#目标说话人提取"]
summary: "提出Textraction，用自然语言描述引导统一模型从单/多通道混合中提取目标说话人或噪声源，并兼顾语音增强。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero hero-focus">
<div class="hero-score">
<div class="score-num">8.8</div>
<div class="score-stars">★★★★☆</div>
<div class="score-tier">前25%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#目标说话人提取</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#目标说话人提取</span> <span class="tag-pill tag-pill-soft">#语音增强</span> <span class="tag-pill tag-pill-soft">#多通道语音处理</span> <span class="tag-pill tag-pill-soft">#文本引导</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2611.12493</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-11-09</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
<div class="meta-row"><span class="meta-key">⭐</span><span class="meta-val focus-badge">本站重点关注领域 · 评分 +1</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2611.12493" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2611.12493" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出Textraction，用自然语言描述引导统一模型从单/多通道混合中提取目标说话人或噪声源，并兼顾语音增强。
</div>

## 👥 作者与机构

**Aviad Eisenberg** ¹ · Sharon Gannot · Shlomo E. Chazan

**机构**：巴伊兰大学

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合做目标说话人提取、文本引导语音处理与多通道波束成形的研究者阅读。建议通读，重点看 §3 的统一单/多通道编码器与 TF-transformer 交叉注意力条件机制，以及轻量文本编码器的对比微调细节；实验部分先看属性提取与空间引导提取的对比表，再看语音增强结果与消融。

## 🌍 研究背景

目标说话人提取此前多依赖说话人 embedding、视频或方位线索，近期工作引入大语言模型做文本引导，但计算开销大且多为单通道、单一任务。空间引导提取与语音增强通常各自独立建模，缺乏统一框架；同时现有方法常需分离+源选择两阶段，推理链长。本文要解决的是：用轻量文本编码器实现指令级（保留/去除）文本引导，并在一个统一模型中同时支持单/多通道、说话人与噪声源提取及语音增强。

## 💡 核心创新

1. 统一单/多通道框架，共享TF-transformer块逐块交叉注意力条件化
2. 轻量对比微调文本编码器，敏感于keep/remove指令极性且抗复述
3. 单次前向直接估计目标，无需分离+源选择两阶段
4. 支持任意实体子集提取与保留/去除组合提示

## 🏗️ 模型架构

输入为单通道或多通道混合音频，分别经专用单通道与多通道编码器映射到时间-频率表示，随后送入共享的 TF-transformer 块堆栈。每个块通过交叉注意力对文本提示嵌入与录音配置（通道/空间信息）进行条件化，文本嵌入来自经对比微调的紧凑文本检索模型。模型直接回归目标源波形/谱，一次前向完成，无显式分离与源选择阶段。摘要未给出参数量。

## 📊 实验结果

摘要仅定性说明在属性引导提取、空间引导提取与语音增强三类实验中有效隔离目标实体，并在多种声学与空间条件下匹配或超过专用空间提取与增强基线，同时灵活性更高；未给出具体指标数值、数据集名称或消融数据，无法量化比较。

## 🎯 结论与影响

最强结论是单一统一模型可用自然语言同时完成说话人/噪声提取与语音增强，且覆盖单/多通道。这为文本引导前端处理提供了轻量化、多任务统一的范式，对需要灵活指令控制的会议系统、助听与车载语音前端有落地潜力。

## ⚠️ 局限与未解决问题

摘要未报告具体指标、数据集规模与推理延迟，缺少与文本引导基线（如基于LLM的方法）的量化对比；假设最多两说话人两噪声源，扩展性未知；轻量文本编码器对复杂/歧义指令的鲁棒性缺乏分析；无公开代码与数据链接。

---

<div class="paper-footer"><span>评分：8.8</span><span>原始：7.8</span><span>+1 重点领域加权</span><a href="/audio-paper-daily/posts/2026-11-10/">← 返回 2026-11-10 速递</a></div>
