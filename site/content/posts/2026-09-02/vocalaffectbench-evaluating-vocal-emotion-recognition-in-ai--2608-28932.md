---
title: "VocalAffectBench: Evaluating Vocal Emotion Recognition in AI Audio Models"
date: 2026-09-02T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#语音情感识别"]
summary: "VocalAffectBench是一个公开的语音情感识别测试基准，包含273个音频片段，评估六个基线模型，平均准确率仅35.5%，表明离散情感识别仍不稳健。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero">
<div class="hero-score">
<div class="score-num">6.8</div>
<div class="score-stars">★★★☆☆</div>
<div class="score-tier">前50%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#语音情感识别</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#情感识别</span> <span class="tag-pill tag-pill-soft">#基准测试</span> <span class="tag-pill tag-pill-soft">#语音音频</span> <span class="tag-pill tag-pill-soft">#多模态</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2608.28932</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-09-02</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2608.28932" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2608.28932" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>VocalAffectBench是一个公开的语音情感识别测试基准，包含273个音频片段，评估六个基线模型，平均准确率仅35.5%，表明离散情感识别仍不稳健。
</div>

## 👥 作者与机构

**Luc Debaupte** ¹ · Tyler Baumgartner · Brandon Tai · Candice Fan · Bill Wang · Yi Zhong

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合语音情感识别、人机交互和音频基础模型研究者阅读。建议重点阅读基准构建部分（§2）和结果分析（§4），以了解任务难度和模型差距。可先看表1和表2，快速把握数据分布和性能概览。

## 🌍 研究背景

语音产品需要从语音中识别情感，但现有模型多依赖文本或上下文。此前缺乏公开的、仅基于音频的语音情感识别基准，导致模型评估不一致。VocalAffectBench旨在提供一个标准化的测试集，评估AI音频模型从原始音频中识别七类离散情感的能力，填补了该领域基准缺失的空白。

## 💡 核心创新

1. 构建了包含273个真实录音的测试基准，覆盖七类情感
2. 严格限定仅使用音频输入，排除文本和元数据干扰
3. 提供六种基线模型的系统评估，揭示性能差距
4. 引入效价分桶分析，提供更粗粒度的情感识别视角

## 🏗️ 模型架构

基准测试本身不涉及模型架构，而是评估现有模型。测试集包含273个WAV片段，时长1.95小时，来自51个说话人。评估的基线模型包括gemini_3_5_flash等，输入为原始音频，输出为七类情感标签。

## 📚 数据集

- VocalAffectBench（测试集，273个WAV片段，1.95小时，七类情感）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| 准确率 | VocalAffectBench | 平均基线 35.5% | **最强基线 gemini_3_5_flash 46.5%** | +11.0% |
| 召回率 | VocalAffectBench | 中性 75.6% | **惊讶 10.7%** | -64.9% |

在七分类任务中，平均准确率35.5%，最强基线gemini_3_5_flash达46.5%，远高于随机水平14.3%。效价分桶分析（正/中性/负）聚合准确率提升至50.9%。类别间性能差异显著：中性召回率最高（75.6%），而惊讶（10.7%）和恐惧（15.4%）召回率极低，表明模型对非中性情感识别脆弱。

## 🎯 结论与影响

VocalAffectBench揭示了当前AI音频模型在离散语音情感识别上的不足，平均准确率仅35.5%，远未达到稳健水平。该基准为领域提供了标准评估工具，有望推动更鲁棒的情感识别模型发展，对语音助手等工业应用具有重要参考价值。

## ⚠️ 局限与未解决问题

基准仅包含英语语音，且样本量较小（每类39个），可能引入语言和类别不平衡偏差。未提供模型推理延迟或计算成本，也未分析说话人差异对结果的影响。此外，未与基于文本或多模态方法对比，限制了结论的普适性。

---

<div class="paper-footer"><span>评分：6.8</span><span>原始：6.8</span><a href="/audio-paper-daily/posts/2026-09-02/">← 返回 2026-09-02 速递</a></div>
