---
title: "Natural Yet Challenging to Detect: Robust In-the-Wild TTS through EMA and Dual-Scoring Prompt Selection -- Submission for WildSpoof 2026 TTS Track"
date: 2026-05-25T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#语音合成"]
summary: "基于F5-TTS架构，结合EMA和双评分提示选择，生成自然且难以被SASV系统检测的语音。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#语音合成</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#语音合成</span> <span class="tag-pill tag-pill-soft">#对抗检测</span> <span class="tag-pill tag-pill-soft">#EMA</span> <span class="tag-pill tag-pill-soft">#提示选择</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2605.23859</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-05-25</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2605.23859" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2605.23859" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>基于F5-TTS架构，结合EMA和双评分提示选择，生成自然且难以被SASV系统检测的语音。
</div>

## 👥 作者与机构

**Renhe Sun** ¹ · Jiayi Zhou · Haolin He · Yueying Feng · Jian Liu

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合语音合成和反欺骗领域的研究者。重点读第3节方法（EMA和双评分提示选择）和第4节实验（a-DCF结果）。可先看表1和表2了解性能。

## 🌍 研究背景

WildSpoof挑战赛TTS Track要求使用野外数据生成自然且能欺骗语音欺骗检测系统的语音。现有TTS模型在噪声环境下对齐困难，且合成语音易被先进SASV系统识别。本文旨在通过稳定训练和高质量提示选择，提升合成语音的自然度和欺骗性。

## 💡 核心创新

1. 引入EMA到监督微调中稳定训练
2. 利用LLM和LALM进行双评分提示选择
3. 在WildSpoof挑战赛中取得最佳a-DCF分数

## 🏗️ 模型架构

基于F5-TTS架构，输入为参考音频和文本提示。主干网络采用F5-TTS的扩散Transformer。关键模块：1) EMA应用于微调阶段；2) 双评分提示选择：LLM评估文本质量，LALM评估音频质量，筛选高质量参考。输出为合成语音波形。

## 📚 数据集

- WildSpoof开发集（评估）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| UTMOS | WildSpoof开发集 | 未明确基线 | **3.20** | N/A |
| 说话人相似度 | WildSpoof开发集 | 未明确基线 | **0.51** | N/A |
| a-DCF | WildSpoof开发集（SASV系统1） | 其他提交最佳 | **0.1582** | 最佳 |
| a-DCF | WildSpoof开发集（SASV系统2） | 其他提交最佳 | **0.5233** | 最佳 |
| a-DCF | WildSpoof开发集（SASV系统3） | 其他提交最佳 | **0.2562** | 最佳 |

在WildSpoof开发集上，F5-TTS-DPS取得UTMOS 3.20和说话人相似度0.51。在三个先进SASV系统上均取得最佳a-DCF分数（0.1582、0.5233、0.2562），表明合成语音最难被检测且自然度高。WER表现也具有竞争力。

## 🎯 结论与影响

本文证明结合EMA和双评分提示选择能有效提升TTS的自然度和欺骗性，在WildSpoof挑战赛中取得最佳反检测性能。该方法为生成高保真且难以检测的语音提供了新思路，对语音反欺骗研究有重要参考价值。

## ⚠️ 局限与未解决问题

仅报告了开发集结果，未提供测试集或跨数据集泛化实验。未与更多基线方法（如VITS、WaveGrad）对比。缺乏消融实验量化EMA和双评分提示选择的各自贡献。未报告模型参数量和推理速度。

---

<div class="paper-footer"><span>评分：7.8</span><span>原始：7.8</span><a href="/audio-paper-daily/posts/2026-05-25/">← 返回 2026-05-25 速递</a></div>
