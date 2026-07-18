---
title: "Dialogs: a studio-quality expressive conversational Russian speech corpus for dialog assistants"
date: 2026-07-18T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#语音语料库"]
summary: "介绍一个20.6小时、3说话人、带情感标签的俄语对话语音语料库，用于训练表达性对话助手。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#语音语料库</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#俄语对话语料库</span> <span class="tag-pill tag-pill-soft">#表现力语音</span> <span class="tag-pill tag-pill-soft">#语音合成</span> <span class="tag-pill tag-pill-soft">#VITS2</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2607.14310</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-07-18</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2607.14310" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2607.14310" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>介绍一个20.6小时、3说话人、带情感标签的俄语对话语音语料库，用于训练表达性对话助手。
</div>

## 👥 作者与机构

**Ilya Shigabeev** ¹ · Ilya Latyshev

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合语音语料库构建、情感语音合成研究者。可重点阅读§3语料库设计、§4质量评估及§5 VITS2概念验证实验。

## 🌍 研究背景

现有俄语语音资源多为朗读语音，缺乏捕捉对话节奏和表现力的高质量对话语料。对话助手需要自然、富有表现力的语音，但缺乏标注精细的对话数据集。本文构建了Dialogs语料库，填补这一空白。

## 💡 核心创新

1. 首个工作室级俄语对话语料库
2. 每句标注12类风格/情感标签
3. 通过众包MOS验证表现力优势
4. 基于VITS2的概念验证TTS实验

## 🏗️ 模型架构

语料库包含20.6小时44.1kHz立体声对话，由3位演员面对面表演录制，分割为11,796个话语。每个话语带有风格/情感标签。概念验证TTS模型采用VITS2架构，输入文本和风格标签，输出语音波形。

## 📚 数据集

- Dialogs（训练/评估，20.6小时，3说话人）
- Russian studio baselines（对比评估，未指定规模）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| MOS（音频质量） | Dialogs测试集 | Russian studio baselines（未给出具体值） | **与baseline相当** | 无显著差异 |
| MOS（表现力） | Dialogs测试集 | Russian studio baselines（未给出具体值） | **更高** | 未量化 |
| MOS（自然度） | Dialogs测试集 | Russian studio baselines（未给出具体值） | **更高** | 未量化 |

众包MOS测试表明，Dialogs在音频质量和可懂度上与俄语工作室基线相当，但在表现力和对话自然度上获得更高评分。VITS2概念验证模型能生成表达性对话语音，尽管每说话人数据有限。

## 🎯 结论与影响

Dialogs语料库为俄语对话助手提供了高质量、富有表现力的语音资源，填补了现有朗读语料库的不足。其精细标注和工作室质量有望推动表达性TTS和对话系统研究。

## ⚠️ 局限与未解决问题

语料库规模较小（20.6小时，3说话人），且为表演性对话而非自发对话。概念验证TTS实验未与最新TTS系统对比，缺乏客观指标（如WER、自然度MOS）。

---

<div class="paper-footer"><span>评分：6.5</span><span>原始：6.5</span><a href="/audio-paper-daily/posts/2026-07-18/">← 返回 2026-07-18 速递</a></div>
