---
title: "MOSS-Audio Technical Report"
date: 2026-06-03T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#音频理解"]
summary: "MOSS-Audio是一个统一的音频-语言模型，支持语音、环境声和音乐理解，通过DeepStack跨层特征注入和时间标记实现强性能。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#音频理解</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#语音理解</span> <span class="tag-pill tag-pill-soft">#环境声音理解</span> <span class="tag-pill tag-pill-soft">#音乐理解</span> <span class="tag-pill tag-pill-soft">#多模态大语言模型</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2606.01802</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-06-03</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2606.01802" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2606.01802" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>MOSS-Audio是一个统一的音频-语言模型，支持语音、环境声和音乐理解，通过DeepStack跨层特征注入和时间标记实现强性能。
</div>

## 👥 作者与机构

**Chen Yang** ¹ · Chufan Yu · Hanfu Chen · Jie Zhu · Jingqi Chen · Ke Chen · Wenxuan Wang · Yang Wang · … 等 18 人

**机构**：复旦大学

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合从事音频理解、多模态大模型研究的读者。建议重点阅读第3节模型架构和第4节数据标注流程，了解DeepStack和时间标记的设计细节。可先看表1和表2的性能对比。

## 🌍 研究背景

现有音频-语言模型通常针对单一领域（如语音或音乐）设计，缺乏统一的音频理解能力。同时，时间感知的问答和时间戳转录等任务需要模型具备细粒度的时间定位能力，但现有方法在时间标记和跨层特征融合方面存在不足。本文旨在构建一个统一的音频-语言模型，支持多种音频理解任务，并引入DeepStack和时间标记来提升性能。

## 💡 核心创新

1. DeepStack跨层特征注入：将多编码器层特征注入解码器
2. 时间标记：在音频token流中插入显式时间戳
3. 事件保持音频标注流水线：按事件边界分割并统一标注
4. 多阶段后训练：增强指令跟随和音频推理能力

## 🏗️ 模型架构

输入音频首先经过专用音频编码器（产生12.5 Hz时间表示），然后通过模态适配器投影到语言解码器空间。解码器采用自回归文本生成。核心创新包括DeepStack跨层特征注入（从编码器多个深度提取特征并注入解码器）和时间标记（在音频token流中插入时间戳标记）。模型有4B和8B两种变体，分为Instruct和Thinking配置。

## 📚 数据集

- 大规模音频-语言数据（预训练，未具体说明规模）
- 任务导向SFT数据（基于分支特定标注构建）

## 📊 实验结果

摘要未提供具体数值结果，但声称在通用音频理解、语音字幕、ASR和时间戳ASR上取得强性能，定位为未来语音代理的理解基础。

## 🎯 结论与影响

MOSS-Audio通过统一架构和创新的DeepStack、时间标记设计，在多种音频理解任务上表现优异。其事件保持标注流水线和多阶段后训练为后续研究提供了可复用的范式。该模型有望成为语音代理的音频理解基础，推动工业级多模态交互系统的发展。

## ⚠️ 局限与未解决问题

摘要未报告具体指标和对比基线，缺乏定量评估。未提及推理延迟和模型效率。数据标注流水线的泛化性未验证。时间标记的粒度（12.5 Hz）可能限制高精度时间定位。

---

<div class="paper-footer"><span>评分：8.2</span><span>原始：8.2</span><a href="/audio-paper-daily/posts/2026-06-03/">← 返回 2026-06-03 速递</a></div>
