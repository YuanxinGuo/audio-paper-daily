---
title: "Audio Sentiment Analysis via Distillation and Cross-Modal Integration of Generated Multilingual Transcripts"
date: 2026-07-09T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#情感识别"]
summary: "提出通过ASR生成多语言文本，结合跨模态Transformer融合音频与文本特征，并蒸馏至纯音频模型以提升情感分类性能。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero">
<div class="hero-score">
<div class="score-num">7.2</div>
<div class="score-stars">★★★★☆</div>
<div class="score-tier">前25%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#情感识别</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#多模态</span> <span class="tag-pill tag-pill-soft">#知识蒸馏</span> <span class="tag-pill tag-pill-soft">#跨模态</span> <span class="tag-pill tag-pill-soft">#语音情感分析</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2607.06611</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-07-09</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner"><div class="oc-headline"><span class="oc-pulse"></span><span class="oc-title">本论文已开源</span><span class="oc-hint">点击下方卡片直达对应资源</span></div><div class="oc-grid"><a class="oc-chip oc-chip-code" href="https://github.com/andreidurdun/cross-modal-audio-sentiment" target="_blank" rel="noopener"><span class="oc-icon">💻</span><span class="oc-text"><span class="oc-label">代码仓库</span><span class="oc-sub">andreidurdun/cross-modal-audio-sentiment</span></span></a></div></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2607.06611" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2607.06611" target="_blank" rel="noopener">📑 PDF</a><a class="rsrc rsrc-code" href="https://github.com/andreidurdun/cross-modal-audio-sentiment" target="_blank" rel="noopener">💻 代码</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出通过ASR生成多语言文本，结合跨模态Transformer融合音频与文本特征，并蒸馏至纯音频模型以提升情感分类性能。
</div>

## 👥 作者与机构

**Andrei-George Durdun** ¹ · Victor Constantinescu · Radu Tudor Ionescu

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合语音情感分析、多模态学习研究者。建议重点阅读§3跨模态架构与§4蒸馏方法，以及表1的消融实验。可复现代码已开源。

## 🌍 研究背景

语音情感识别需同时分析声学特征和语义内容。现有方法多依赖音频基础模型，但难以充分捕捉语义信息。本文提出利用ASR生成文本转录，并通过机器翻译创建多语言文本模态，与音频特征通过跨模态Transformer融合，再蒸馏至纯音频模型，以提升情感分类准确率。

## 💡 核心创新

1. 利用ASR和机器翻译生成多语言文本模态
2. 级联跨模态Transformer逐步融合音频与多语言文本
3. 从多模态教师蒸馏知识至纯音频学生模型
4. 在大型数据集上验证多语言文本的有效性

## 🏗️ 模型架构

输入音频经预训练音频编码器提取特征，同时通过ASR生成文本转录并翻译为多种语言，经文本编码器提取特征。音频与多语言文本特征通过级联的跨模态Transformer模块逐步融合，最终分类。训练后，将多模态教师模型的知识蒸馏至纯音频学生模型（仅音频编码器+分类头）。

## 📚 数据集

- 大规模情感分类数据集（训练与评估，具体名称未提及）

## 📊 实验结果

摘要未提供具体数值，但声称多模态融合显著提升情感极性分类性能，消融实验证实自动转录和翻译均有帮助，蒸馏可提升纯音频模型性能且无推理开销。

## 🎯 结论与影响

本文证明通过ASR生成多语言文本并融合音频特征可有效提升语音情感识别，蒸馏至纯音频模型实现无额外开销的性能提升。该思路可推广至其他语音理解任务，工业落地中可结合现有ASR服务实现低成本增强。

## ⚠️ 局限与未解决问题

未报告具体指标和数据集规模，缺乏与SOTA方法的定量对比；多语言翻译质量依赖机器翻译工具，可能引入噪声；未分析不同语言组合的影响；蒸馏学生模型与教师差距未量化。

## 🔗 开源资源

- **代码**：<https://github.com/andreidurdun/cross-modal-audio-sentiment>

---

<div class="paper-footer"><span>评分：7.2</span><span>原始：7.2</span><a href="/audio-paper-daily/posts/2026-07-09/">← 返回 2026-07-09 速递</a></div>
