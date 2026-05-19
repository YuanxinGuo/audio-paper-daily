---
title: "TED-TTS: Training-Free Intra-Utterance Emotion and Duration Control for Text-to-Speech Synthesis"
date: 2026-05-19T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#语音合成"]
summary: "提出TED-TTS，一种无需训练的框架，实现预训练零样本TTS的语句内情感和时长精细控制。"
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
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#文本到语音</span> <span class="tag-pill tag-pill-soft">#情感控制</span> <span class="tag-pill tag-pill-soft">#时长控制</span> <span class="tag-pill tag-pill-soft">#零样本TTS</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2601.03170</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-05-19</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2601.03170" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2601.03170" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出TED-TTS，一种无需训练的框架，实现预训练零样本TTS的语句内情感和时长精细控制。
</div>

## 👥 作者与机构

**Qifan Liang** ¹ · Yuansen Liu · Ruixin Wei · Nan Lu · Junchuan Zhao · Ye Wang

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合TTS和可控语音合成研究者。建议重点阅读§3.1情感调节和§3.2时长引导策略，以及§4实验部分。可先看表1和表2了解性能提升。

## 🌍 研究背景

可控文本到语音合成（TTS）虽取得进展，但现有方法多限于语句间控制，难以实现语句内细粒度情感和时长表达，且依赖非公开数据集或复杂多阶段训练。本文旨在提出一种无需训练的框架，在预训练零样本TTS基础上实现语句内情感和时长控制。

## 💡 核心创新

1. 段感知情感调节策略：因果掩码+单调流对齐过滤
2. 段感知时长引导策略：局部时长嵌入+全局EOS logit调制
3. 基于LLM的自动提示构建，无需手动段级提示工程

## 🏗️ 模型架构

输入文本和情感/时长段标签 → 预训练零样本TTS模型（如YourTTS）→ 段感知情感调节模块（因果掩码+单调流对齐过滤）→ 段感知时长引导模块（局部时长嵌入+全局EOS logit调制）→ 输出语音。无需额外训练，仅推理时干预。

## 📚 数据集

- LibriTTS（训练零样本TTS）
- 自定义30k样本多情感时长标注文本数据集（用于LLM提示构建）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| MOS（情感一致性） | 自建测试集 | YourTTS 3.2 | **4.1** | +0.9 |
| MOS（语音质量） | 自建测试集 | YourTTS 4.3 | **4.2** | -0.1 |
| 时长控制准确率 | 自建测试集 | FastSpeech2 85% | **92%** | +7% |

实验表明，TED-TTS在情感一致性和时长控制上达到SOTA，同时保持基线语音质量。消融实验验证了各模块有效性。跨说话人泛化良好，但未报告推理速度。

## 🎯 结论与影响

TED-TTS无需训练即可实现语句内情感和时长控制，为可控TTS提供新范式。后续可探索更细粒度控制（如音素级）和更多情感维度。工业上可快速集成到现有TTS系统。

## ⚠️ 局限与未解决问题

依赖预训练TTS模型质量；情感类别有限；未评估长句或多段情感切换的稳定性；未报告推理延迟；数据集非公开。

---

<div class="paper-footer"><span>评分：7.8</span><span>原始：7.8</span><a href="/audio-paper-daily/posts/2026-05-19/">← 返回 2026-05-19 速递</a></div>
