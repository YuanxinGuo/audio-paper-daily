---
title: "I Understand How You Feel: Enhancing Deeper Emotional Support Through Multilingual Emotional Validation in Dialogue System"
date: 2026-06-11T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#情感验证"]
summary: "提出多语言情感验证对话系统，包含语料库、时序检测模型MEGUMI和基准测试。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero">
<div class="hero-score">
<div class="score-num">6.5</div>
<div class="score-stars">★★★☆☆</div>
<div class="score-tier">前50%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#情感验证</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#对话系统</span> <span class="tag-pill tag-pill-soft">#多语言</span> <span class="tag-pill tag-pill-soft">#情感识别</span> <span class="tag-pill tag-pill-soft">#语料库</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2606.11875</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-06-11</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner"><div class="oc-headline"><span class="oc-pulse"></span><span class="oc-title">本论文已开源</span><span class="oc-hint">点击下方卡片直达对应资源</span></div><div class="oc-grid"><a class="oc-chip oc-chip-code" href="https://github.com/zihaurpang/Multilingual-Emotional-Validation" target="_blank" rel="noopener"><span class="oc-icon">💻</span><span class="oc-text"><span class="oc-label">代码仓库</span><span class="oc-sub">zihaurpang/Multilingual-Emotional-Validation</span></span></a></div></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2606.11875" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2606.11875" target="_blank" rel="noopener">📑 PDF</a><a class="rsrc rsrc-code" href="https://github.com/zihaurpang/Multilingual-Emotional-Validation" target="_blank" rel="noopener">💻 代码</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出多语言情感验证对话系统，包含语料库、时序检测模型MEGUMI和基准测试。
</div>

## 👥 作者与机构

**Zi Haur Pang** ¹ · Yahui Fu · Koji Inoue · Tatsuya Kawahara

**机构**：京都大学

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合对话系统、情感计算研究者。可重点读§3语料库构建和§4 MEGUMI模型。建议先看表2和表3的性能对比。

## 🌍 研究背景

情感验证在心理治疗中有效，但在对话系统中研究不足。现有工作缺乏多语言语料库和时序检测模型。本文旨在构建大规模多语言情感验证语料库，并提出时序检测模型MEGUMI，同时评估LLM在情感验证上的能力。

## 💡 核心创新

1. 构建120k英日双语情感验证语料库M-EDESConv
2. 提出MEGUMI模型融合语义与情感特征
3. 设计多语言口语测试集M-TESC
4. 基准测试GPT-4.1 Nano和Llama-3.1 8B

## 🏗️ 模型架构

MEGUMI模型：输入文本经XLM-RoBERTa提取语义特征，同时通过语言特定情感编码器提取情感特征；两者经交叉注意力对齐后，通过门控融合机制整合，最终用于时序检测（二分类判断是否应进行情感验证）。

## 📚 数据集

- M-EDESConv（120k英日双语，训练/评估）
- M-TESC（多语言口语测试集，评估）

## 📊 实验结果

摘要未提供具体数值，仅提及MEGUMI在M-EDESConv和M-TESC上主客观性能优越，且LLM生成验证响应在上下文相似性和多样性上表现良好，但情感理解仍需改进。

## 🎯 结论与影响

本文首次系统研究多语言情感验证，构建大规模语料库和时序检测模型，为对话系统情感支持提供新方向。未来可推动情感验证在心理咨询等场景的应用。

## ⚠️ 局限与未解决问题

未报告模型参数量、推理速度；语料库仅含英日两种语言，泛化性待验证；时序检测任务定义较简单（二分类），实际对话中验证时机更复杂。

## 🔗 开源资源

- **代码**：<https://github.com/zihaurpang/Multilingual-Emotional-Validation>

---

<div class="paper-footer"><span>评分：6.5</span><span>原始：6.5</span><a href="/audio-paper-daily/posts/2026-06-11/">← 返回 2026-06-11 速递</a></div>
