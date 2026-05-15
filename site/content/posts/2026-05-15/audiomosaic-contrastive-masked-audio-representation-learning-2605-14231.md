---
title: "AudioMosaic: Contrastive Masked Audio Representation Learning"
date: 2026-05-15T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#音频表示学习"]
summary: "提出AudioMosaic，一种基于对比学习的音频自监督方法，通过结构化时频掩码构造正样本对，学习判别性音频表示，在多个基准上达到SOTA。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#音频表示学习</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#自监督学习</span> <span class="tag-pill tag-pill-soft">#对比学习</span> <span class="tag-pill tag-pill-soft">#掩码建模</span> <span class="tag-pill tag-pill-soft">#音频理解</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2605.14231</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-05-15</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner"><div class="oc-headline"><span class="oc-pulse"></span><span class="oc-title">本论文已开源</span><span class="oc-hint">点击下方卡片直达对应资源</span></div><div class="oc-grid"><a class="oc-chip oc-chip-code" href="https://github.com/HanxunH/AudioMosaic" target="_blank" rel="noopener"><span class="oc-icon">💻</span><span class="oc-text"><span class="oc-label">代码仓库</span><span class="oc-sub">HanxunH/AudioMosaic</span></span></a></div></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2605.14231" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2605.14231" target="_blank" rel="noopener">📑 PDF</a><a class="rsrc rsrc-code" href="https://github.com/HanxunH/AudioMosaic" target="_blank" rel="noopener">💻 代码</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出AudioMosaic，一种基于对比学习的音频自监督方法，通过结构化时频掩码构造正样本对，学习判别性音频表示，在多个基准上达到SOTA。
</div>

## 👥 作者与机构

**Hanxun Huang** ¹ · Qizhou Wang · Xingjun Ma · Cihang Xie · Christopher Leckie · Sarah Erfani

**机构**：墨尔本大学 · 复旦大学 · 加州大学圣克鲁兹分校

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合音频自监督学习研究者阅读。建议重点读§3方法部分和§4实验部分，特别是对比学习框架和掩码策略的设计。可先看表1和表2了解性能提升。

## 🌍 研究背景

音频自监督学习旨在从无标签数据中学习通用表示。现有方法以生成式重建目标为主（如MAE-style），对比学习方法因数据增强设计困难和需要大批量训练而探索不足。本文针对这些问题，提出一种高效的对比学习框架AudioMosaic，通过结构化时频掩码构造正样本对，降低内存需求并支持大批量训练，从而学习更具判别性的音频表示。

## 💡 核心创新

1. 结构化时频掩码构造正样本对
2. 高效大批量对比学习训练
3. 判别性 utterance-level 表示学习
4. 跨数据集和域的良好迁移性

## 🏗️ 模型架构

输入为log-mel spectrogram，经patch嵌入后送入Transformer编码器。预训练时，对每个样本的spectrogram patches应用结构化时频掩码（随机掩码连续时间或频率块），生成两个不同的视图作为正样本对，通过对比损失（InfoNCE）训练。编码器输出全局表示用于下游任务。

## 📚 数据集

- AudioSet (预训练)
- ESC-50 (评估)
- Speech Commands V2 (评估)
- VGGSound (评估)

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| Accuracy | ESC-50 | MAE-AST 95.6% | **97.1%** | +1.5% |
| Accuracy | Speech Commands V2 | MAE-AST 98.3% | **98.7%** | +0.4% |

在ESC-50和Speech Commands V2上，AudioMosaic在linear probing和fine-tuning下均达到SOTA，分别比MAE-AST高1.5%和0.4%。在VGGSound上也取得competitive结果。此外，将AudioMosaic集成到音频语言模型中，提升了音频语言任务的性能。消融实验验证了结构化掩码和对比学习框架的有效性。

## 🎯 结论与影响

AudioMosaic证明了对比学习在音频自监督学习中的潜力，通过结构化时频掩码实现了高效大批量训练，学习到判别性强的表示。该方法为音频SSL提供了新范式，有望推动音频理解任务的发展，并易于集成到多模态模型中。

## ⚠️ 局限与未解决问题

论文未报告模型参数量和推理速度，对比基线不够全面（仅与MAE-AST等少数方法比较），且未在更多样化的音频任务（如语音增强、分离）上验证。结构化掩码的设计可能对某些音频类型不敏感。

## 🔗 开源资源

- **代码**：<https://github.com/HanxunH/AudioMosaic>

---

<div class="paper-footer"><span>评分：8.2</span><span>原始：8.2</span><a href="/audio-paper-daily/posts/2026-05-15/">← 返回 2026-05-15 速递</a></div>
