---
title: "TF-MossFormer: Integrating Convolution Gated Local-Global Attentions for Enhanced Time-Frequency Domain Monaural Speech Separation"
date: 2026-07-24T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#语音分离"]
summary: "提出TF-MossFormer，在时频域结合卷积门控与局部-全局注意力，在WSJ0-2Mix上以5.9M参数达到22.6 dB SI-SDRi，超越此前方法。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero hero-focus">
<div class="hero-score">
<div class="score-num">9.5</div>
<div class="score-stars">★★★★★</div>
<div class="score-tier">前10%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#语音分离</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#语音分离</span> <span class="tag-pill tag-pill-soft">#Transformer</span> <span class="tag-pill tag-pill-soft">#时频域</span> <span class="tag-pill tag-pill-soft">#注意力机制</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2607.21128</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-07-24</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">🔥 强烈推荐通读</span></div>
<div class="meta-row"><span class="meta-key">⭐</span><span class="meta-val focus-badge">本站重点关注领域 · 评分 +1</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2607.21128" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2607.21128" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出TF-MossFormer，在时频域结合卷积门控与局部-全局注意力，在WSJ0-2Mix上以5.9M参数达到22.6 dB SI-SDRi，超越此前方法。
</div>

## 👥 作者与机构

**Shengkui Zhao** ¹ · Zexu Pan · Haoxu Wang · Biao Tian · Bin Ma · Xiangang Li

**机构**：字节跳动

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合语音分离和Transformer架构研究者。建议通读，重点看§3的滑动窗口注意力机制和§4的实验结果。可复现代码并对比MossFormer。

## 🌍 研究背景

语音分离旨在从混合语音中分离出每个说话人的干净语音。现有方法中，时域模型如SepFormer、MossFormer利用全局注意力捕获长程依赖，但可能忽略局部连续性；频域方法则能同时建模时间和频率结构。本文旨在设计一种时频域Transformer，同时建模局部和全局上下文，提升分离性能。

## 💡 核心创新

1. 提出内容感知滑动窗口注意力，动态调整感受野增强局部交互
2. 在时频域2D谱图上建模时间和频率轴结构
3. 在注意力层间引入卷积门控，改善特征选择和信息流

## 🏗️ 模型架构

输入为混合语音的2D时频谱图，经线性投影后送入多个TF-MossFormer块。每个块包含：内容感知滑动窗口注意力（局部注意力）、全局注意力（如MossFormer中的GAU）、卷积门控前馈网络。输出经线性层和掩蔽估计得到分离谱图，再通过ISTFT恢复波形。模型有5.9M、16.9M、25.4M三种参数量。

## 📚 数据集

- WSJ0-2Mix（训练/评估，包含30小时训练集）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| SI-SDRi (dB) | WSJ0-2Mix | MossFormer (5.9M) 22.1 | **22.6** | +0.5 |
| SI-SDRi (dB) | WSJ0-2Mix | MossFormer (16.9M) 23.5 | **24.0** | +0.5 |
| SI-SDRi (dB) | WSJ0-2Mix | MossFormer (25.4M) 23.9 | **24.4** | +0.5 |

TF-MossFormer在WSJ0-2Mix上以三种参数量均超越MossFormer约0.5 dB SI-SDRi，且优于SepFormer等基线。消融实验验证了滑动窗口注意力和卷积门控的有效性。模型在参数量更小的情况下达到更高性能。

## 🎯 结论与影响

TF-MossFormer通过结合局部-全局注意力和卷积门控，在时频域语音分离中取得了SOTA结果。其设计思路可推广至其他音频处理任务，如语音增强。工业上，小参数量模型利于部署。

## ⚠️ 局限与未解决问题

仅在WSJ0-2Mix上评估，未见跨数据集泛化实验；未报告推理速度或计算复杂度；滑动窗口注意力的超参数（窗口大小）未充分讨论。

---

<div class="paper-footer"><span>评分：9.5</span><span>原始：8.5</span><span>+1 重点领域加权</span><a href="/audio-paper-daily/posts/2026-07-24/">← 返回 2026-07-24 速递</a></div>
