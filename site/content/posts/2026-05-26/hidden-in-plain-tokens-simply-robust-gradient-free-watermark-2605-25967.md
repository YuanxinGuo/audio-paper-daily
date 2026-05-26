---
title: "Hidden in Plain Tokens: Simply Robust, Gradient-Free Watermark for Synthetic Audio"
date: 2026-05-26T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#音频水印"]
summary: "提出一种无需微调tokenizer的梯度自由音频水印方法，通过社区检测缩减词汇表提升检测鲁棒性。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#音频水印</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#音频水印</span> <span class="tag-pill tag-pill-soft">#离散表示</span> <span class="tag-pill tag-pill-soft">#生成音频</span> <span class="tag-pill tag-pill-soft">#鲁棒性</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2605.25967</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-05-26</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2605.25967" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2605.25967" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出一种无需微调tokenizer的梯度自由音频水印方法，通过社区检测缩减词汇表提升检测鲁棒性。
</div>

## 👥 作者与机构

**Georgios Milis** ¹ · Yubin Qin · Yihan Wu · Heng Huang

**机构**：马里兰大学

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合音频水印、生成式AI安全方向研究者。建议重点阅读§3（方法）和§4（实验），特别是表1-3的检测性能对比。可先看Fig.2理解词汇缩减流程。

## 🌍 研究背景

生成式AI的快速发展使得音频内容溯源成为关键需求。现有推理时水印方法因离散化不一致不适用于连续模态，而微调tokenizer的方法丧失了训练自由优势。本文针对离散化过程中的词汇冗余问题，提出一种无需训练的水印方案，利用社区检测缩减词汇表，在保持零训练开销的同时大幅提升检测性能。

## 💡 核心创新

1. 提出基于社区检测的词汇缩减策略
2. 理论分析token错误对检测的影响
3. 实现梯度自由且鲁棒的音频水印
4. 检测性能提升数个数量级

## 🏗️ 模型架构

输入音频经预训练tokenizer（如EnCodec）离散化为token序列。水印嵌入：在token序列中按规则修改部分token为缩减词汇表中的对应token。检测时：统计水印token比例并与阈值比较。核心创新在于通过社区检测将原始词汇表聚类为若干社区，每个社区保留一个代表token，形成缩减词汇表，从而减少嵌入错误并增强鲁棒性。

## 📚 数据集

- LibriTTS（训练/评估，用于生成合成音频）
- VCTK（评估，用于生成合成音频）
- DNS-Challenge（评估，用于噪声鲁棒性测试）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| AUROC | LibriTTS | KGW (0.50) | **0.99** | +0.49 |
| AUROC | VCTK | KGW (0.50) | **0.99** | +0.49 |
| AUROC (after MP3 compression) | LibriTTS | KGW (0.50) | **0.95** | +0.45 |

在LibriTTS和VCTK上，所提方法AUROC达0.99，远超KGW的0.50。在MP3压缩、重采样等音频修改下仍保持0.95以上AUROC。消融实验验证了词汇缩减比例对检测性能的影响，且方法无需任何训练，计算开销极低。

## 🎯 结论与影响

本文提出一种简单而强大的梯度自由音频水印方法，通过词汇缩减实现鲁棒检测，性能达SOTA。该方法无需修改tokenizer，可直接应用于现有离散音频模型，对生成式AI内容溯源具有重要价值。工业上可低成本集成到音频生成管线中。

## ⚠️ 局限与未解决问题

方法依赖于预训练tokenizer的词汇表质量，社区检测的聚类数需手动设定。未在音乐或非语音音频上验证。未与基于训练的水印方法（如DeepSigns）对比计算开销。缺乏对更复杂攻击（如时间伸缩、语音合成）的鲁棒性测试。

---

<div class="paper-footer"><span>评分：7.8</span><span>原始：7.8</span><a href="/audio-paper-daily/posts/2026-05-26/">← 返回 2026-05-26 速递</a></div>
