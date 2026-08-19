---
title: "Memory Efficient Audio Synthesis with Decoupled Temporal Depth Diffusion Transformers"
date: 2026-08-19T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#语音合成"]
summary: "提出一种内存高效的音频合成架构，通过解耦时间与深度处理的扩散Transformer，在设备端实现实时、低内存的语音合成。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero">
<div class="hero-score">
<div class="score-num">8.5</div>
<div class="score-stars">★★★★☆</div>
<div class="score-tier">前10%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#语音合成</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#语音合成</span> <span class="tag-pill tag-pill-soft">#扩散Transformer</span> <span class="tag-pill tag-pill-soft">#内存高效</span> <span class="tag-pill tag-pill-soft">#设备端推理</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2607.23811</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-08-19</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">🔥 强烈推荐通读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2607.23811" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2607.23811" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出一种内存高效的音频合成架构，通过解耦时间与深度处理的扩散Transformer，在设备端实现实时、低内存的语音合成。
</div>

## 👥 作者与机构

**Dongseong Hwang** ¹ · Prasanth Yadla · Kaan Elgin · Shifas Padinjaru Veettil · Sivanand Achanta · Dipjyoti Paul · Ramya Rasipuram · Tyler Johnson · … 等 3 人

**机构**：苹果

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合语音合成、设备端推理和扩散模型研究者阅读。建议重点阅读第3节架构设计和第4节实验部分，特别是消融研究。可先看摘要和结论，再深入方法细节。

## 🌍 研究背景

设备端语音合成受限于计算和内存预算，传统Transformer和GAN方法存在线性或二次方内存扩展问题。先前多解码器架构为每个RVQ级别配备专用解码器，导致模型庞大。本文旨在设计一种在Apple Matrix Coprocessor上高效运行的音频合成架构，解决内存和延迟瓶颈。

## 💡 核心创新

1. 解耦时间与深度处理，采用流式编码器、时间解码器和深度解码器三组件设计
2. 单一可复用深度解码器，通过DiT风格阶段条件生成所有RVQ级别，替代多解码器
3. 因果滑动窗口注意力与固定窗口KV缓存，实现常数内存复杂度
4. 在AMX上实现约10ms/步，16倍实时，峰值内存仅21MB
5. 在1B参数激活规模下，MOS提升0.28（整体）和0.42（对话语音）

## 🏗️ 模型架构

输入为语义音频token，经流式编码器转换为RVQ表示。时间解码器处理时间维度，深度解码器（DiT风格）处理深度维度，通过阶段条件生成所有RVQ级别。采用因果滑动窗口注意力，固定窗口KV缓存，内存复杂度常数。部署在AMX上，峰值内存21MB，模型资产329MB。

## 📚 数据集

- 内部语音数据集（训练和评估）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| MOS | 内部测试集（整体） | 先前设备端TTS 3.87 | **4.15** | +0.28 |
| MOS | 内部测试集（对话语音） | 先前设备端TTS 3.82 | **4.24** | +0.42 |

实验表明，所提架构在保持合成质量的同时，实现了显著的内存和延迟改进。消融研究验证了关键组件（如深度解码器复用、滑动窗口注意力）的有效性。在AMX上，生成速度约10ms/步，支持20-320秒连续流式合成。

## 🎯 结论与影响

本文提出了一种内存高效的音频合成架构，通过解耦时间与深度处理，实现了设备端实时、低内存的语音合成。该设计为资源受限环境下的高质量语音合成提供了新思路，有望推动设备端TTS的普及。

## ⚠️ 局限与未解决问题

摘要未提供详细的数据集规模和多样性信息，可能影响泛化性评估。未报告与其他SOTA方法的详细对比，如延迟和内存的具体数值。未讨论模型在复杂声学环境下的鲁棒性。

---

<div class="paper-footer"><span>评分：8.5</span><span>原始：8.5</span><a href="/audio-paper-daily/posts/2026-08-19/">← 返回 2026-08-19 速递</a></div>
