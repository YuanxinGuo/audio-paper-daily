---
title: "PashtoTTS-Bench: automated screening for low-resource non-Latin-script text-to-speech"
date: 2026-05-27T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#语音合成评估"]
summary: "提出INSV-A自动筛选框架用于低资源非拉丁文字TTS评估，并构建普什图语基准PashtoTTS-Bench。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#语音合成评估</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#低资源TTS</span> <span class="tag-pill tag-pill-soft">#非拉丁文字</span> <span class="tag-pill tag-pill-soft">#自动评估</span> <span class="tag-pill tag-pill-soft">#普什图语</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2605.26978</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-05-27</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2605.26978" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2605.26978" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出INSV-A自动筛选框架用于低资源非拉丁文字TTS评估，并构建普什图语基准PashtoTTS-Bench。
</div>

## 👥 作者与机构

**Hanif Rahman** ¹

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合从事低资源TTS评估的研究者阅读。建议重点看§3的INSV-A框架定义和§4的基准结果，特别是WER与自然语音基线的对比分析。可跳过附录中的详细系统配置。

## 🌍 研究背景

低资源非拉丁文字TTS评估常依赖单一ASR往返WER，但该方法存在缺陷：系统可能无输出、输出邻接语言、仅ASR转录保留目标文字、或听感不自然。现有评估缺乏对这些失败模式的系统区分。本文旨在提出一个分离不同失败模式的评估框架INSV，并实现其自动筛选子集INSV-A。

## 💡 核心创新

1. 提出INSV评估框架，分离可懂度、自然度、文字保真度、验证四个维度
2. 定义INSV-A自动筛选子集，包含合成完成率、ASR WER/CER、文字保真率、音频语种识别
3. 构建普什图语TTS基准PashtoTTS-Bench，包含400条提示和5个系统
4. 揭示WER低于自然语音基线反映音频过于干净，不应视为优于自然语音

## 🏗️ 模型架构

INSV-A框架包含四个自动指标：合成完成率（检测是否生成音频）、ASR WER/CER（使用omniASR_CTC_300M_v2）、转录文字保真率（计算ASR转录中目标文字比例）、音频语种识别（使用MMS-LID-4017和SpeechBrain VoxLingua107）。评估流程：输入TTS系统输出音频，依次通过各模块，输出结构化报告。

## 📚 数据集

- FLEURS（200条提示，评估）
- Common Voice 24（200条过滤提示，评估）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| WER | FLEURS | 自然语音基线（未给出具体值） | **OmniVoice auto 24.1%** | 低于基线 |
| WER | Common Voice 24 | 自然语音基线（未给出具体值） | **OmniVoice auto 27.4%** | 低于基线 |

OmniVoice auto在FLEURS和CV24上取得最低WER（24.1%和27.4%），但低于自然语音基线，表明合成音频过于干净。Whisper Large V3对普什图语TTS音频返回0.0%普什图语标签，而MMS-LID-4017和VoxLingua107能有效区分普什图语和乌尔都语。

## 🎯 结论与影响

INSV-A框架能有效识别低资源非拉丁文字TTS的多种失败模式，WER低于基线不应视为优于自然语音。该框架为低资源TTS评估提供了更全面的自动化工具，可推广至其他非拉丁文字语言。对工业落地而言，可帮助开发者快速筛选TTS系统质量。

## ⚠️ 局限与未解决问题

仅报告了自动筛选子集INSV-A，未包含人工MOS和音素标注；基准仅覆盖普什图语，泛化性未知；仅评估5个系统，样本量有限；未分析不同ASR模型对WER的影响。

---

<div class="paper-footer"><span>评分：6.5</span><span>原始：6.5</span><a href="/audio-paper-daily/posts/2026-05-27/">← 返回 2026-05-27 速递</a></div>
