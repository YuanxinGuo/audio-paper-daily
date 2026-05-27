---
title: "ParsVoice: A Large-Scale Multi-Speaker Persian Speech Corpus for Text-to-Speech Synthesis"
date: 2026-05-27T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#语音合成"]
summary: "构建了目前最大的公开波斯语多说话人语音-文本语料库ParsVoice（2200小时），并验证其在零样本TTS中的有效性。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#语音合成</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#多说话人语音合成</span> <span class="tag-pill tag-pill-soft">#波斯语语料库</span> <span class="tag-pill tag-pill-soft">#零样本语音合成</span> <span class="tag-pill tag-pill-soft">#数据构建流程</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2510.10774</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-05-27</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner"><div class="oc-headline"><span class="oc-pulse"></span><span class="oc-title">本论文已开源</span><span class="oc-hint">点击下方卡片直达对应资源</span></div><div class="oc-grid"><a class="oc-chip oc-chip-hf" href="https://huggingface.co/datasets/MohammadJRanjbar/ParsVoice" target="_blank" rel="noopener"><span class="oc-icon">🤗</span><span class="oc-text"><span class="oc-label">HuggingFace</span><span class="oc-sub">🤗 datasets/MohammadJRanjbar/ParsVoice</span></span></a></div></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2510.10774" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2510.10774" target="_blank" rel="noopener">📑 PDF</a><a class="rsrc rsrc-hf" href="https://huggingface.co/datasets/MohammadJRanjbar/ParsVoice" target="_blank" rel="noopener">🤗 HuggingFace</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>构建了目前最大的公开波斯语多说话人语音-文本语料库ParsVoice（2200小时），并验证其在零样本TTS中的有效性。
</div>

## 👥 作者与机构

**Mohammad Javad Ranjbar Kalahroodi** ¹ · Heshaam Faili · Azadeh Shakery

**机构**：德黑兰大学

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合从事低资源语言TTS、语音语料库构建的研究者阅读。建议重点看§3数据构建流程和§4.2质量评估部分，可参考其pipeline设计。

## 🌍 研究背景

波斯语在开源语音-文本资源中严重不足，限制了多说话人TTS、语音语言建模等研究。此前最大的公开波斯语TTS数据集规模有限，且缺乏高质量的多说话人标注。本文旨在构建大规模、高质量、多说话人的波斯语语音-文本语料库，以推动该语言在TTS及相关领域的研究。

## 💡 核心创新

1. 结合ParsBERT句子完成分类器与ASR边界优化的对齐方法
2. 多维质量评估同时覆盖音频和波斯语特定文本属性
3. 构建2200小时、1815说话人的最大公开波斯语TTS语料库
4. 在零样本TTS模型XTTS上验证语料库有效性

## 🏗️ 模型架构

本文主要贡献为数据构建流程，而非模型架构。流程包括：长音频录音→语音活动检测→说话人日志→ASR转录→ParsBERT句子完成分类器分割→ASR边界优化→标点恢复→说话人识别→多维质量评估。最终输出对齐的语音-文本对。验证模型使用XTTS（基于VITS的零样本多语言TTS模型），直接处理原始波斯语文本，无需音素表示。

## 📚 数据集

- ParsVoice（训练/评估，2200小时TTS子集，136万对齐片段，1815说话人）
- 先前最大公开波斯语TTS数据集（对比，规模约88小时）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| 自然度MOS | ParsVoice测试集 | 无（首次大规模评估） | **3.6/5** | N/A |
| 说话人相似度MOS | ParsVoice测试集 | 无 | **4.0/5** | N/A |

在ParsVoice上微调XTTS模型，自然度MOS达3.6/5，说话人相似度MOS达4.0/5，表明语料库可用于训练高质量多说话人TTS系统。未提供与其他波斯语TTS系统的直接对比，但语料库规模是先前最大数据集的25倍以上。

## 🎯 结论与影响

ParsVoice作为最大公开波斯语多说话人语音-文本语料库，填补了该语言在TTS资源上的空白。其构建流程可推广至其他低资源语言。该语料库有望推动波斯语TTS、语音语言建模及低资源语音处理的研究。

## ⚠️ 局限与未解决问题

未提供与现有波斯语TTS系统的直接对比（如MOS基线）；说话人识别基于自动方法，可能存在误差；仅验证了XTTS模型，未测试其他TTS架构；语料库来源为有声书，可能引入特定风格偏差。

## 🔗 开源资源

- **HuggingFace**：<https://huggingface.co/datasets/MohammadJRanjbar/ParsVoice>
- **数据集**：<https://huggingface.co/datasets/MohammadJRanjbar/ParsVoice>

---

<div class="paper-footer"><span>评分：7.5</span><span>原始：7.5</span><a href="/audio-paper-daily/posts/2026-05-27/">← 返回 2026-05-27 速递</a></div>
