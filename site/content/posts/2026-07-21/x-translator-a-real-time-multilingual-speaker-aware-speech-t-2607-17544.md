---
title: "X-Translator: A Real-Time Multilingual Speaker-Aware Speech-to-Speech Translation System"
date: 2026-07-21T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#语音翻译"]
summary: "X-Translator 是一个模块化级联的实时语音到语音翻译系统，通过增量段确认和在线说话人提示管理，在长对话和多说话人场景下平衡翻译质量、延迟和说话人一致性。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#语音翻译</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#流式语音翻译</span> <span class="tag-pill tag-pill-soft">#级联系统</span> <span class="tag-pill tag-pill-soft">#说话人一致性</span> <span class="tag-pill tag-pill-soft">#多说话人</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2607.17544</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-07-21</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner"><div class="oc-headline"><span class="oc-pulse"></span><span class="oc-title">本论文已开源</span><span class="oc-hint">点击下方卡片直达对应资源</span></div><div class="oc-grid"><a class="oc-chip oc-chip-code" href="https://github.com/zhaoyx239/X-Translator" target="_blank" rel="noopener"><span class="oc-icon">💻</span><span class="oc-text"><span class="oc-label">代码仓库</span><span class="oc-sub">zhaoyx239/X-Translator</span></span></a></div></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2607.17544" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2607.17544" target="_blank" rel="noopener">📑 PDF</a><a class="rsrc rsrc-code" href="https://github.com/zhaoyx239/X-Translator" target="_blank" rel="noopener">💻 代码</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>X-Translator 是一个模块化级联的实时语音到语音翻译系统，通过增量段确认和在线说话人提示管理，在长对话和多说话人场景下平衡翻译质量、延迟和说话人一致性。
</div>

## 👥 作者与机构

**Yuxiang Zhao** ¹ · Yichi Zhang · Yanjie An · Yanqiao Zhu · Zhanxun Liu · Yushen Chen · Qixi Zheng · Haina Zhu · … 等 5 人

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合从事语音翻译系统部署的研究者或工程师。建议重点阅读 §3 系统设计（增量段确认和说话人提示管理）以及 §4 实验中的长语音稳定性评估。可先看图 2 系统架构概览。

## 🌍 研究背景

实时语音到语音翻译（S2ST）需兼顾翻译质量、延迟、自然度和说话人一致性。现有开源系统在长对话和多说话人场景下存在部分ASR假设不稳定、话轮边界模糊、目标语音需匹配说话人提示等问题。本文提出X-Translator，一个低成本的模块化级联系统，结合流式ASR、机器翻译和提示条件TTS，通过会话级运行时控制器解决上述挑战。

## 💡 核心创新

1. 增量段确认机制将不稳定ASR流转换为翻译就绪单元
2. 在线说话人提示管理器绑定源语音段到特定说话人提示
3. 会话级运行时控制器协调ASR、MT、TTS模块
4. 开源完整系统，提供部署导向的S2ST平台

## 🏗️ 模型架构

输入流式音频 → 流式ASR（如Whisper）输出部分假设 → 增量段确认模块（Incremental Segment Commitment）将不稳定流转换为稳定段 → 机器翻译模块（如NLLB）翻译文本 → 在线说话人提示管理器（Online Speaker Prompt Manager）根据源语音段选择对应说话人提示 → 提示条件TTS（如VITS）合成目标语音。系统通过会话级运行时控制器管理模块间通信和延迟。

## 📚 数据集

- OpenSTBench（评估翻译质量、语音质量和延迟）
- 内部多说话人对话数据集（评估说话人保持和长语音稳定性）

## 📊 实验结果

摘要未提供具体数值，但声称在OpenSTBench上评估翻译质量、语音质量和延迟，并与商业API对比；在长语音稳定性、多说话人说话人保持和多语言翻译质量上进行了评估。具体结果需查阅全文。

## 🎯 结论与影响

X-Translator 提供了一个开放平台，用于理解部署导向S2ST的实际权衡。其增量段确认和在线说话人提示管理为长对话和多说话人场景下的实时翻译提供了有效方案。对工业落地有参考价值，尤其适合需要说话人一致性的多语种会议翻译。

## ⚠️ 局限与未解决问题

摘要未提及推理延迟的具体数值、与端到端系统的对比、以及在不同噪声环境下的鲁棒性。作为级联系统，错误传播问题未充分讨论。缺少对TTS语音自然度的主观评测。

## 🔗 开源资源

- **代码**：<https://github.com/zhaoyx239/X-Translator>

---

<div class="paper-footer"><span>评分：7.8</span><span>原始：7.8</span><a href="/audio-paper-daily/posts/2026-07-21/">← 返回 2026-07-21 速递</a></div>
