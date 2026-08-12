---
title: "The Watermark Shortcut: How Provenance Marking Sabotages Audio Deepfake Detection"
date: 2026-08-12T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#音频伪造检测"]
summary: "发现语音水印作为虚假线索导致深度伪造检测器性能下降，提出去相关训练可修复。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero hero-focus">
<div class="hero-score">
<div class="score-num">8.8</div>
<div class="score-stars">★★★★☆</div>
<div class="score-tier">前25%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#音频伪造检测</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#水印</span> <span class="tag-pill tag-pill-soft">#深度伪造检测</span> <span class="tag-pill tag-pill-soft">#语音增强</span> <span class="tag-pill tag-pill-soft">#鲁棒性</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2606.23335</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-08-12</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
<div class="meta-row"><span class="meta-key">⭐</span><span class="meta-val focus-badge">本站重点关注领域 · 评分 +1</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2606.23335" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2606.23335" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>发现语音水印作为虚假线索导致深度伪造检测器性能下降，提出去相关训练可修复。
</div>

## 👥 作者与机构

Nicolas M. M\"uller · Pascal Debus

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合音频安全、深度伪造检测研究者阅读。建议重点看第3节实验设计和第4节修复方法，可复现实验验证水印捷径的影响。

## 🌍 研究背景

深度伪造检测是语音安全的关键，现有方法依赖水印作为溯源手段。但水印可能被检测器当作虚假特征，导致泛化下降、逃避检测和误报。本文首次系统分析水印对检测器的负面影响，并提出解决方案。

## 💡 核心创新

1. 识别水印捷径现象，揭示水印与伪造标签的虚假关联
2. 提出去相关训练策略，在水印两侧同时训练以消除捷径
3. 构建WASP数据集，提供配对的水印与无水印语音用于研究
4. 在商业API上验证水印捷径的实际危害

## 🏗️ 模型架构

本文不涉及具体模型架构，而是分析检测器训练过程中的水印捷径。实验使用白盒检测器（如基于ResNet的音频分类器）和黑盒商业API，通过对比有水印和无水印训练数据的检测性能，验证水印捷径的存在及修复效果。

## 📚 数据集

- WASP（训练/评估，配对水印与无水印语音）
- LibriTTS（训练/评估，用于生成合成语音）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| EER | WASP | 无水印训练 16% | **有水印训练 75%** | +59% |

实验表明，水印训练导致检测器在未见数据上性能下降，且水印真实语音被误判为伪造。去相关训练后，EER恢复至接近基线水平。黑盒测试中，商业API对加水印的真实语音误判为伪造。

## 🎯 结论与影响

水印捷径是深度伪造检测的严重隐患，但可通过去相关训练修复。研究为水印与检测的协同设计提供新视角，对工业部署有重要警示意义。

## ⚠️ 局限与未解决问题

实验主要基于合成语音，对真实场景的泛化性需进一步验证。未探讨不同水印强度的影响，且未与其他检测方法对比。

---

<div class="paper-footer"><span>评分：8.8</span><span>原始：7.8</span><span>+1 重点领域加权</span><a href="/audio-paper-daily/posts/2026-08-12/">← 返回 2026-08-12 速递</a></div>
