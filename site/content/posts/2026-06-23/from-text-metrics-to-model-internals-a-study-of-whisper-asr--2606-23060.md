---
title: "From Text Metrics to Model Internals: A Study of Whisper ASR Hallucination Detection"
date: 2026-06-23T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#语音识别"]
summary: "系统比较了基于文本、LLM和内部解码器状态三种范式检测Whisper ASR幻觉的方法，发现无参考的解码器探测性能最强，融合方法最优。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#语音识别</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#幻觉检测</span> <span class="tag-pill tag-pill-soft">#Whisper</span> <span class="tag-pill tag-pill-soft">#解码器探测</span> <span class="tag-pill tag-pill-soft">#文本指标</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2606.23060</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-06-22</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2606.23060" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2606.23060" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>系统比较了基于文本、LLM和内部解码器状态三种范式检测Whisper ASR幻觉的方法，发现无参考的解码器探测性能最强，融合方法最优。
</div>

## 👥 作者与机构

**Jan Jasiński** ¹ · Mateusz Barański · Julitta Bartolewska · Marcin Witkowski · Konrad Kowalczyk

**机构**：亚当·密茨凯维奇大学

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合ASR鲁棒性、幻觉检测方向的研究者。建议重点阅读§3（方法）和§4（实验结果），特别是表2和表3的对比。可先看§4.3解码器探测部分。

## 🌍 研究背景

ASR模型的幻觉（流畅但无音频依据的转录）会降低系统性能并带来下游风险。现有检测方法多依赖文本指标或外部语言模型，但缺乏对模型内部状态的利用。本文系统研究了Whisper large v3的幻觉检测，探索文本分类、LLM提示和解码器状态探测三种范式，旨在找到无需参考转录的高效检测方法。

## 💡 核心创新

1. 系统比较三种检测范式：文本、LLM、解码器探测
2. 发现无参考的解码器探测优于有参考的文本方法
3. 揭示幻觉特征编码在解码器中间层
4. 提出晚期融合元分类器融合文本与内部状态
5. 在真实语音人工标注数据上评估

## 🏗️ 模型架构

输入为音频特征，主干为Whisper large v3编码器-解码器。文本方法使用文本评估指标（如WER）训练分类器；LLM方法通过领域特定提示调整GPT模型；解码器探测方法从Whisper解码器各层提取隐藏状态，训练线性分类器。最终融合方法将文本指标与解码器状态拼接后训练元分类器。

## 📚 数据集

- 真实语音人工标注数据集（训练/评估，未具名规模）

## 📊 实验结果

摘要未提供具体数值，但指出文本方法在无参考时召回率下降，LLM方法精度更高但不如轻量文本方法，解码器探测无参考时性能最强，融合方法最佳。

## 🎯 结论与影响

本文系统比较了Whisper幻觉检测的三种范式，证明无参考的解码器内部状态探测比依赖参考文本的方法更有效，且融合文本与内部状态可进一步提升性能。该发现为ASR幻觉检测提供了新方向，有望推动更鲁棒的语音识别系统开发，对工业部署中的错误监控有实际意义。

## ⚠️ 局限与未解决问题

仅针对Whisper large v3，未验证其他ASR模型；数据集未公开且规模未知；未报告推理延迟和计算开销；解码器探测需要访问模型内部，对黑盒模型不适用。

---

<div class="paper-footer"><span>评分：7.8</span><span>原始：7.8</span><a href="/audio-paper-daily/posts/2026-06-23/">← 返回 2026-06-23 速递</a></div>
