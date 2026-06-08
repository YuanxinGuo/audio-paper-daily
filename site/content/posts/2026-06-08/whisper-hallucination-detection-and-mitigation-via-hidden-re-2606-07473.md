---
title: "Whisper Hallucination Detection and Mitigation via Hidden Representation Steering and Sparse AutoEncoders"
date: 2026-06-08T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#语音识别"]
summary: "利用Whisper内部表示和稀疏自编码器检测并缓解ASR幻觉，将幻觉率从72.63%降至14.11%。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero">
<div class="hero-score">
<div class="score-num">8.2</div>
<div class="score-stars">★★★★☆</div>
<div class="score-tier">前25%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#语音识别</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#幻觉检测</span> <span class="tag-pill tag-pill-soft">#幻觉缓解</span> <span class="tag-pill tag-pill-soft">#稀疏自编码器</span> <span class="tag-pill tag-pill-soft">#表示引导</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2606.07473</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-06-08</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2606.07473" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2606.07473" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>利用Whisper内部表示和稀疏自编码器检测并缓解ASR幻觉，将幻觉率从72.63%降至14.11%。
</div>

## 👥 作者与机构

**Georgii Aparin** ¹ · Vadim Popov · Tasnima Sadekova · Assel Yermekova

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合ASR鲁棒性研究者。重点读§3（表示分析）和§4（引导策略）。可先看表2和表3的量化结果。

## 🌍 研究背景

Whisper等ASR模型在非语音输入上易产生连贯但错误的转录（幻觉），影响实际部署。现有缓解方法依赖微调或外部检测器，计算成本高。本文探索利用Whisper内部表示（编码器激活和SAE潜变量）进行幻觉检测与引导缓解，无需额外模型或数据。

## 💡 核心创新

1. 首次利用SAE潜变量检测ASR幻觉
2. 提出激活空间和SAE潜变量空间两种引导策略
3. 发现幻觉相关信息集中在深层编码器稀疏特征子集
4. 无需微调即可大幅降低幻觉率，接近微调方法性能

## 🏗️ 模型架构

基于Whisper模型（small和large-v3）。输入音频经编码器提取激活，分别使用原始激活和SAE（稀疏自编码器）提取的潜变量作为表示空间。训练线性分类器检测幻觉，并设计两种引导策略：激活空间引导（沿分类器法向调整激活）和SAE潜变量空间引导（调整SAE潜变量后解码回激活）。引导后的激活替换原始编码器输出，再送入解码器生成转录。

## 📚 数据集

- 非语音测试集（包含静音、噪声、音乐等，评估幻觉率）
- LibriSpeech clean（评估语音数据WER退化）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| 幻觉率 | 全非语音测试集 | Whisper small 72.63% | **14.11%** | -58.52% |
| 幻觉率 | 全非语音测试集 | Whisper large-v3 86.88% | **27.33%** | -59.55% |
| WER | LibriSpeech clean | Whisper small 7.2% | **7.5%** | +0.3% |
| WER | LibriSpeech clean | Whisper large-v3 3.6% | **3.9%** | +0.3% |

SAE潜变量空间引导在非语音测试集上将Whisper small幻觉率从72.63%降至14.11%，large-v3从86.88%降至27.33%，接近微调方法（11.45%和20.42%）。语音数据上WER仅增加0.3%。消融实验表明，引导强度需平衡幻觉抑制与转录质量。

## 🎯 结论与影响

本文证明Whisper内部表示包含可分离的幻觉相关信息，通过SAE潜变量引导可无需微调大幅降低幻觉率，为ASR幻觉缓解提供轻量级新思路。该方法有望推广至其他Transformer ASR模型，并促进对模型内部机制的理解。

## ⚠️ 局限与未解决问题

仅在非语音测试集上评估，未覆盖语音中夹杂噪声的幻觉场景；引导强度需手动调节，缺乏自适应机制；SAE训练需额外计算；未与其他轻量级检测方法（如置信度阈值）对比。

---

<div class="paper-footer"><span>评分：8.2</span><span>原始：8.2</span><a href="/audio-paper-daily/posts/2026-06-08/">← 返回 2026-06-08 速递</a></div>
