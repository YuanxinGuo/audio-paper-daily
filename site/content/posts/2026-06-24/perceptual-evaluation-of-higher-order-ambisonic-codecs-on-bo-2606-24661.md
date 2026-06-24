---
title: "Perceptual Evaluation of Higher-Order Ambisonic Codecs on Both Synthetic Mixing and Native Recordings"
date: 2026-06-24T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#空间音频编码"]
summary: "评估IVAS编解码器对高阶Ambisonics内容的压缩性能，相比多单声道方法在相同码率下更优，尤其适用于高通道相关信号。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero">
<div class="hero-score">
<div class="score-num">7.2</div>
<div class="score-stars">★★★★☆</div>
<div class="score-tier">前50%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#空间音频编码</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#高阶Ambisonics</span> <span class="tag-pill tag-pill-soft">#音频编解码</span> <span class="tag-pill tag-pill-soft">#IVAS</span> <span class="tag-pill tag-pill-soft">#感知评估</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2606.24661</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-06-24</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2606.24661" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2606.24661" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>评估IVAS编解码器对高阶Ambisonics内容的压缩性能，相比多单声道方法在相同码率下更优，尤其适用于高通道相关信号。
</div>

## 👥 作者与机构

**Adrien Llave** ¹ · Gr\'egory Pallone · J\'er\^ome Daniel

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合空间音频编码、沉浸式音频领域的研究者。重点看§3实验设置和§4结果分析，对比IVAS与多单声道方法的性能差异。

## 🌍 研究背景

高阶Ambisonics (HOA) 在VR/AR等应用中广泛使用，但多通道传输需要高效压缩。IVAS是新兴的标准化编解码器，本文旨在系统评估其对HOA内容的编码性能，并与基础的多单声道方法对比，揭示IVAS利用通道间相关性的优势。

## 💡 核心创新

1. 首次系统评估IVAS对HOA内容的编码性能
2. 对比合成混合与原生录音两种内容类型
3. 揭示IVAS在高通道相关信号上的鲁棒性

## 🏗️ 模型架构

评估两种编解码器：IVAS（标准化沉浸式语音音频编解码器）和多单声道方法（各通道独立编码）。IVAS利用通道间相关性进行压缩，多单声道方法则独立处理各通道。测试信号包括合成混合（有限平面波）和原生录音（如Ambisonic录音）。

## 📚 数据集

- 合成混合信号（平面波组合，用于评估高通道相关场景）
- 原生录音（实际Ambisonic录音，用于评估真实场景）

## 📊 实验结果

摘要未提供具体数值，但指出IVAS在相同码率下优于多单声道方法，尤其对于高通道相关信号（如有限平面波合成信号），多单声道方法无法利用相关性，性能较差。

## 🎯 结论与影响

IVAS编解码器对HOA内容压缩有效，优于多单声道方法，尤其适用于高通道相关信号。该工作为空间音频编码提供了参考，有助于推动IVAS在沉浸式通信中的应用。

## ⚠️ 局限与未解决问题

未提供客观指标（如PEAQ、PESQ）或主观测试结果，仅依赖定性描述；未比较其他HOA专用编解码器；未分析不同阶数Ambisonics的影响。

---

<div class="paper-footer"><span>评分：7.2</span><span>原始：7.2</span><a href="/audio-paper-daily/posts/2026-06-24/">← 返回 2026-06-24 速递</a></div>
