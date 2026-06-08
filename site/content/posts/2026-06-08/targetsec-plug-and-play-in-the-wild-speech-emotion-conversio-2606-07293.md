---
title: "TargetSEC: Plug-and-Play In-the-Wild Speech Emotion Conversion via Arousal-Conditioned Latent Style Diffusion"
date: 2026-06-08T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#语音情感转换"]
summary: "提出TargetSEC，一种基于嵌入驱动的潜在扩散框架，通过唤醒度条件实现非平行野外语音情感转换，兼顾转换准确性和语音质量。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#语音情感转换</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#语音情感转换</span> <span class="tag-pill tag-pill-soft">#扩散模型</span> <span class="tag-pill tag-pill-soft">#潜在空间</span> <span class="tag-pill tag-pill-soft">#非平行数据</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2606.07293</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-06-08</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2606.07293" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2606.07293" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出TargetSEC，一种基于嵌入驱动的潜在扩散框架，通过唤醒度条件实现非平行野外语音情感转换，兼顾转换准确性和语音质量。
</div>

## 👥 作者与机构

**Constantin Alexander Auga** ¹

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合语音情感转换、扩散模型应用方向的研究者。建议重点阅读§3方法部分和§4实验对比，特别是与固定时长方法的比较。可先看表1和表2了解性能提升。

## 🌍 研究背景

语音情感转换旨在保留内容和说话人身份的同时转换情感。野外数据非平行且声学复杂，现有固定时长方法要么转换效果差（高质量低转换），要么牺牲自然度（低质量高转换）。需要一种能同时保证转换准确性和语音质量的方法。

## 💡 核心创新

1. 嵌入驱动的潜在扩散框架
2. 唤醒度条件控制情感强度
3. 说话人身份与连续情感联合条件
4. 在紧凑潜在空间而非频谱上扩散

## 🏗️ 模型架构

输入源语音和目标情感标签（唤醒度值），通过预训练情感编码器提取风格嵌入，说话人编码器提取身份嵌入。将风格嵌入注入潜在扩散模型，该模型以说话人嵌入和连续唤醒度值为条件，在紧凑潜在空间中生成目标风格嵌入。最后用声码器合成语音。

## 📚 数据集

- MSP-Podcast（训练和评估，大规模野外情感语音数据集）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| 转换准确率 | MSP-Podcast | VoiceMask (0.72) | **0.79** | +0.07 |
| 自然度MOS | MSP-Podcast | VoiceMask (3.2) | **3.5** | +0.3 |

TargetSEC在MSP-Podcast上转换准确率达0.79，优于VoiceMask等非时长基线，自然度MOS 3.5，与时长预测系统性能相当。消融实验验证了唤醒度条件和潜在扩散设计的有效性。

## 🎯 结论与影响

TargetSEC通过潜在扩散和唤醒度条件，在非平行野外数据上实现了高转换准确性和高语音质量的平衡。该方法无需显式时长建模，为情感转换提供了新范式，有望推动情感语音交互应用。

## ⚠️ 局限与未解决问题

仅在MSP-Podcast单一数据集上评估，泛化性待验证；未报告推理延迟和模型参数量；缺乏与其他潜在扩散方法的对比；情感类别仅使用唤醒度维度，未探索效价等其他维度。

---

<div class="paper-footer"><span>评分：7.8</span><span>原始：7.8</span><a href="/audio-paper-daily/posts/2026-06-08/">← 返回 2026-06-08 速递</a></div>
