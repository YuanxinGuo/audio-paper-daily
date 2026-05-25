---
title: "XAttnMark: Learning Robust Audio Watermarking with Cross-Attention"
date: 2026-05-25T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#音频水印"]
summary: "提出XAttnMark，利用交叉注意力和部分参数共享实现鲁棒音频水印，在检测和归因上达到SOTA。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero">
<div class="hero-score">
<div class="score-num">8.5</div>
<div class="score-stars">★★★★☆</div>
<div class="score-tier">前25%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#音频水印</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#音频水印</span> <span class="tag-pill tag-pill-soft">#生成式AI</span> <span class="tag-pill tag-pill-soft">#交叉注意力</span> <span class="tag-pill tag-pill-soft">#鲁棒性</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2502.04230</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-05-25</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">🔥 强烈推荐通读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2502.04230" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2502.04230" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出XAttnMark，利用交叉注意力和部分参数共享实现鲁棒音频水印，在检测和归因上达到SOTA。
</div>

## 👥 作者与机构

**Yixin Liu** ¹ · Lie Lu · Jihui Jin · Lichao Sun · Andrea Fanelli

**机构**：Lehigh University · Dolby Laboratories · Penn State University

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合音频水印、生成式AI安全领域研究者。建议通读，重点看§3.2交叉注意力机制和§3.3心理声学TF掩蔽损失。可复现代码。

## 🌍 研究背景

生成式音频合成与编辑技术引发版权侵权、数据溯源和深度伪造音频传播等担忧。水印通过嵌入不可感知但可追踪信号提供主动防护。现有方法如WavMark、AudioSeal在鲁棒性和质量上有所提升，但难以同时优化鲁棒检测和准确归因。本文旨在解决这一权衡问题。

## 💡 核心创新

1. 生成器与检测器部分参数共享
2. 交叉注意力机制用于高效消息检索
3. 时序条件模块改善消息分布
4. 心理声学对齐的时频掩蔽损失

## 🏗️ 模型架构

输入音频经编码器生成水印信号，与原始音频混合。生成器采用卷积网络，检测器通过交叉注意力从混合信号中提取消息。部分参数在生成器和检测器间共享。时序条件模块调节消息嵌入位置。心理声学TF掩蔽损失指导水印不可感知性。

## 📚 数据集

- LibriSpeech（训练/评估）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| 检测准确率 | LibriSpeech | AudioSeal 0.95 | **0.98** | +0.03 |
| 归因准确率 | LibriSpeech | WavMark 0.90 | **0.96** | +0.06 |
| 鲁棒性（平均） | LibriSpeech | AudioSeal 0.85 | **0.93** | +0.08 |

XAttnMark在检测和归因准确率上均超越AudioSeal和WavMark，尤其对生成式编辑（如变声、重合成）鲁棒性提升显著。心理声学损失使水印不可感知性更好（PESQ提升0.2）。

## 🎯 结论与影响

XAttnMark通过交叉注意力与参数共享实现了检测与归因的联合优化，在多种音频变换下保持鲁棒，为生成式AI时代音频版权保护提供了有效方案。后续可探索更轻量级模型和实时应用。

## ⚠️ 局限与未解决问题

仅在LibriSpeech上评估，未见跨数据集泛化测试；未报告推理延迟和模型参数量；心理声学损失的计算复杂度未讨论。

---

<div class="paper-footer"><span>评分：8.5</span><span>原始：8.5</span><a href="/audio-paper-daily/posts/2026-05-25/">← 返回 2026-05-25 速递</a></div>
