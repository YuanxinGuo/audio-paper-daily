---
title: "SpeechEQ: Benchmarking Emotional Intelligence Quotient in Socially Aware Voice Conversational Models"
date: 2026-06-25T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#情感识别"]
summary: "提出SpeechEQ框架，评估语音语言模型在多轮对话中的社会语言推理能力，包含2265个对话数据集和SEQ评分指标。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#情感识别</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#语音语言模型</span> <span class="tag-pill tag-pill-soft">#情感商数</span> <span class="tag-pill tag-pill-soft">#多模态推理</span> <span class="tag-pill tag-pill-soft">#基准测试</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2606.25990</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-06-25</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner"><div class="oc-headline"><span class="oc-pulse"></span><span class="oc-title">本论文已开源</span><span class="oc-hint">点击下方卡片直达对应资源</span></div><div class="oc-grid"><a class="oc-chip oc-chip-hf" href="https://huggingface.co/datasets/SpeechEQ/SpeechEQ" target="_blank" rel="noopener"><span class="oc-icon">🤗</span><span class="oc-text"><span class="oc-label">HuggingFace</span><span class="oc-sub">🤗 datasets/SpeechEQ/SpeechEQ</span></span></a><a class="oc-chip oc-chip-proj" href="https://binomial14.github.io/speecheq-demo/" target="_blank" rel="noopener"><span class="oc-icon">🌐</span><span class="oc-text"><span class="oc-label">项目主页</span><span class="oc-sub">binomial14.github.io/speecheq-demo/</span></span></a><a class="oc-chip oc-chip-demo" href="https://binomial14.github.io/speecheq-demo/" target="_blank" rel="noopener"><span class="oc-icon">🔊</span><span class="oc-text"><span class="oc-label">在线 Demo</span><span class="oc-sub">binomial14.github.io/speecheq-demo/</span></span></a></div></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2606.25990" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2606.25990" target="_blank" rel="noopener">📑 PDF</a><a class="rsrc rsrc-hf" href="https://huggingface.co/datasets/SpeechEQ/SpeechEQ" target="_blank" rel="noopener">🤗 HuggingFace</a><a class="rsrc rsrc-proj" href="https://binomial14.github.io/speecheq-demo/" target="_blank" rel="noopener">🌐 项目主页</a><a class="rsrc rsrc-demo" href="https://binomial14.github.io/speecheq-demo/" target="_blank" rel="noopener">🔊 Demo</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出SpeechEQ框架，评估语音语言模型在多轮对话中的社会语言推理能力，包含2265个对话数据集和SEQ评分指标。
</div>

## 👥 作者与机构

**Liang-Yuan Wu** ¹ · **Zih-Ching Chen** ¹ · Tongshuang Wu · Chao-Han Huck Yang · Hua Shen

**机构**：卡内基梅隆大学 · 华盛顿大学 · 英伟达

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合语音情感识别、多模态对话系统研究者。值得通读，重点看§3数据集构建和§4评估协议。可先看表1和SEQ指标定义。

## 🌍 研究背景

现有机器情感智能评估局限于孤立文本或被动声学感知，缺乏对主动多轮对话中跨模态推理的评估。语音语言模型（SLM）在理解副语言社交线索方面存在瓶颈，但缺乏系统基准。本文基于EQ-i 2.0理论构建SpeechEQ框架，填补这一空白。

## 💡 核心创新

1. 提出SpeechEQ基准，含2265个对话覆盖15个EQ子量表
2. 设计多轮SEQ评分指标，模拟人类EQ评估
3. 揭示端到端SLM的三种缺陷：模态捷径、安全陷阱、上下文遗忘

## 🏗️ 模型架构

SpeechEQ框架包含数据集和评估协议。数据集由2265个多轮对话组成，覆盖15个EQ子量表。评估协议采用多轮交互，通过SEQ指标量化模型对副语言线索的理解。实验对比了级联系统（ASR+文本模型）和端到端SLM（如SpeechGPT、Qwen-Audio等），分析其情感推理能力。

## 📚 数据集

- SpeechEQ数据集（2265个对话，15个EQ子量表，用于评估）

## 📊 实验结果

摘要未提供具体数值结果，但指出端到端SLM优于级联系统，但仍存在模态捷径、安全陷阱和上下文遗忘等问题。实验揭示了当前模型在副语言理解上的局限性。

## 🎯 结论与影响

SpeechEQ揭示了现有语音语言模型在情感推理中的关键缺陷，为开发真正情感感知的AI提供了基准。未来工作可基于此改进模型架构，避免文本依赖和过度对齐。对工业界，该基准可指导语音助手的情感交互设计。

## ⚠️ 局限与未解决问题

数据集规模有限（2265对话），可能未覆盖所有情感场景；SEQ指标的有效性需进一步验证；未提供模型参数量或推理效率分析；对比模型不够全面。

## 🔗 开源资源

- **HuggingFace**：<https://huggingface.co/datasets/SpeechEQ/SpeechEQ>
- **项目主页**：<https://binomial14.github.io/speecheq-demo/>
- **Demo / 试听**：<https://binomial14.github.io/speecheq-demo/>
- **数据集**：<https://huggingface.co/datasets/SpeechEQ/SpeechEQ>

---

<div class="paper-footer"><span>评分：7.8</span><span>原始：7.8</span><a href="/audio-paper-daily/posts/2026-06-25/">← 返回 2026-06-25 速递</a></div>
