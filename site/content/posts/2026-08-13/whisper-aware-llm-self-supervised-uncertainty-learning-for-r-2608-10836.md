---
title: "Whisper-Aware LLM: Self-Supervised Uncertainty Learning for Robust Whispered Speech Recognition"
date: 2026-08-13T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#语音识别"]
summary: "提出Whisper-Aware LLM框架，通过自监督不确定性学习让音频大模型感知耳语信号的不确定性，并用置信度融合解码降低幻觉，在AISHELL6-Whisper上CER相对降低17%。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#语音识别</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#耳语语音识别</span> <span class="tag-pill tag-pill-soft">#不确定性学习</span> <span class="tag-pill tag-pill-soft">#自监督学习</span> <span class="tag-pill tag-pill-soft">#音频大语言模型</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2608.10836</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-08-13</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2608.10836" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2608.10836" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出Whisper-Aware LLM框架，通过自监督不确定性学习让音频大模型感知耳语信号的不确定性，并用置信度融合解码降低幻觉，在AISHELL6-Whisper上CER相对降低17%。
</div>

## 👥 作者与机构

**Gaopeng Xu** ¹ · Zhenyu Wang · Zheng Xue · Yinfeng Xia · Haitao Yao

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合语音识别、鲁棒ASR和音频大模型研究者阅读。建议重点阅读第3节（方法）和第4节（实验），特别是Confidence-Fused Decoding机制和表2的结果。可先看摘要和结论，再深入方法细节。

## 🌍 研究背景

耳语语音识别面临信号模糊性，导致ASR系统要么漏识别耳语，要么将噪声幻觉转录为文本。现有方法多针对正常语音优化，对耳语适应性差。本文提出让音频大模型学习量化声学信号物理缺陷的不确定性，并通过自监督任务获得内在自感知，从而缓解上述问题。

## 💡 核心创新

1. 自监督不确定性学习任务，量化声学信号物理缺陷
2. Confidence-Fused Decoding机制，融合高层指令和帧级注意力调制
3. 在AISHELL6-Whisper上实现17%相对CER降低，幻觉率从25%降至4.5%

## 🏗️ 模型架构

输入为耳语语音特征，送入音频编码器提取特征，然后由Audio-LLM解码。模型通过自监督任务学习不确定性估计，该不确定性被用于Confidence-Fused Decoding机制，该机制向LLM解码器提供高层指令和帧级注意力调制，以引导解码过程。

## 📚 数据集

- AISHELL6-Whisper（评估，耳语语音识别）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| CER | AISHELL6-Whisper | 未明确给出具体值，但相对降低17% | **相对降低17%** | -17% relative |
| Hallucination Rate | AISHELL6-Whisper | >25% | **4.5%** | -20.5% absolute |

实验表明，所提方法在AISHELL6-Whisper上取得SOTA，CER相对降低17%，同时幻觉率从超过25%降至4.5%，显著提升了可靠性。但摘要未提供更多消融或跨数据集泛化结果。

## 🎯 结论与影响

本文通过自监督不确定性学习使音频大模型能够感知耳语信号的不确定性，并利用置信度融合解码有效降低幻觉，显著提升耳语识别性能。该工作为鲁棒ASR提供了新思路，有望推动音频大模型在低资源或噪声环境下的应用。

## ⚠️ 局限与未解决问题

摘要未提及模型参数量、推理效率或跨数据集泛化实验。此外，不确定性学习任务的设计细节和消融实验缺失，可能影响说服力。

---

<div class="paper-footer"><span>评分：8.2</span><span>原始：8.2</span><a href="/audio-paper-daily/posts/2026-08-13/">← 返回 2026-08-13 速递</a></div>
