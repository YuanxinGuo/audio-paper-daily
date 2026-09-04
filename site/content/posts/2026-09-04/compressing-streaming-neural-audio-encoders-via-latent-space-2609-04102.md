---
title: "Compressing Streaming Neural Audio Encoders via Latent-Space Distillation"
date: 2026-09-04T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#语音识别"]
summary: "通过蒸馏预量化器潜在表示，将流式语音编码器压缩2.8倍，在保持WER接近的同时减少内存占用。"
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
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#知识蒸馏</span> <span class="tag-pill tag-pill-soft">#模型压缩</span> <span class="tag-pill tag-pill-soft">#流式编码器</span> <span class="tag-pill tag-pill-soft">#端侧部署</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2609.04102</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-09-04</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2609.04102" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2609.04102" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>通过蒸馏预量化器潜在表示，将流式语音编码器压缩2.8倍，在保持WER接近的同时减少内存占用。
</div>

## 👥 作者与机构

**Prasanth Yadla** ¹ · Mohammad Samragh · Dongseong Hwang · Mingbin Xu · Yuanyuan Zhang · Chung-Cheng Chiu · Yongqiang Wang · Yuan Liu · … 等 2 人

**机构**：Apple

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合语音识别和模型压缩方向的研究者。建议重点阅读方法部分（第3节）和实验部分（第4节），特别是表1和表2，了解蒸馏目标的选择和压缩效果。可先看摘要和结论快速了解贡献。

## 🌍 研究背景

Apple设备上的系统级听写完全在端侧运行，语音通过tokenizer（编码器）转换为语言模型可读的表示。由于语言模型采用稀疏激活，只有部分专家驻留DRAM，常驻的tokenizer与语言模型竞争内存，其参数量直接影响功耗和延迟。因此压缩tokenizer至关重要。现有压缩方法通常蒸馏离散token或输出分布，但本文发现蒸馏预量化器潜在表示更有效，因为该表示是两种token接口共享的最后表示。

## 💡 核心创新

1. 以预量化器潜在表示作为蒸馏目标，而非离散token或输出分布
2. 单一仿射层吸收师生宽度不匹配，简化蒸馏过程
3. 统一适用于两种token接口，无需针对每种接口单独设计
4. 适用于预训练和联合训练的tokenizer，无需微调
5. 在2.8倍压缩下，相对WER仅增加1.9%

## 🏗️ 模型架构

输入为短时波形窗口，教师和学生编码器均为流式编码器（具体结构未在摘要中说明）。学生编码器通过回归教师每帧潜在表示进行训练，使用平方误差损失。在教师和学生潜在表示之间插入一个仿射层以匹配维度。蒸馏目标位于量化器之前，因此不涉及离散token或语言模型桥接。学生编码器输出预量化器潜在表示，供后续量化器和语言模型使用。

## 📊 实验结果

摘要中未提供具体数据集和指标数值，仅提及在六对师生组合中的五对上，2.8倍压缩的学生模型相对WER与教师差距在1.9%以内，且比同容量独立训练的tokenizer相对WER低3.9%。未提及消融实验或效率指标。

## 🎯 结论与影响

本文提出的潜在空间蒸馏方法能有效压缩流式语音编码器，在2.8倍压缩下保持接近教师的性能，且无需微调。该方法统一适用于不同token接口，为端侧语音识别系统的模型压缩提供了新思路。对工业界而言，可降低内存占用和功耗，提升设备端体验。

## ⚠️ 局限与未解决问题

摘要未提及具体数据集和实验细节，缺乏与现有压缩方法的对比。未报告推理延迟和功耗的实际测量。未讨论压缩极限或更大压缩比下的性能下降。未提及学生编码器的具体架构和参数量。

---

<div class="paper-footer"><span>评分：7.8</span><span>原始：7.8</span><a href="/audio-paper-daily/posts/2026-09-04/">← 返回 2026-09-04 速递</a></div>
