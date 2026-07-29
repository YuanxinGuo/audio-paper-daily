---
title: "Audio dequantization using instantaneous frequency"
date: 2026-07-29T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#音频处理"]
summary: "提出一种利用瞬时频率的相位感知正则化方法进行音频去量化，避免l1正则化的能量损失伪影。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero">
<div class="hero-score">
<div class="score-num">6.5</div>
<div class="score-stars">★★★☆☆</div>
<div class="score-tier">前50%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#音频处理</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#音频去量化</span> <span class="tag-pill tag-pill-soft">#相位感知正则化</span> <span class="tag-pill tag-pill-soft">#音频修复</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2510.16813</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-07-29</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2510.16813" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2510.16813" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出一种利用瞬时频率的相位感知正则化方法进行音频去量化，避免l1正则化的能量损失伪影。
</div>

## 👥 作者与机构

Vojt\v{e}ch Kovanda · Pavel Rajmic

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合音频修复和量化噪声抑制方向的研究者阅读。可重点看§3的方法描述和§4的实验结果，特别是与l1正则化的对比。

## 🌍 研究背景

音频去量化旨在恢复因量化而失真的音频信号，传统方法多采用l1正则化，但易导致能量损失伪影。本文借鉴音频修复中的相位感知正则化，利用瞬时频率促进时频域正弦分量的时间连续性，以改善去量化效果。

## 💡 核心创新

1. 引入相位感知正则化用于音频去量化
2. 利用瞬时频率促进时频连续性
3. 避免l1正则化的能量损失伪影

## 🏗️ 模型架构

输入量化音频的短时傅里叶变换（STFT）幅度和相位，通过迭代优化算法最小化目标函数，包含数据保真项和相位感知正则化项。正则化项基于瞬时频率的平滑性约束，输出重构的时域音频。

## 📚 数据集

- 私有数据集（训练/评估，具体规模未提及）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| SDR (dB) | 私有测试集 | l1正则化方法 12.5 | **PHADQ 14.8** | +2.3 dB |
| PEMO-Q ODG | 私有测试集 | l1正则化方法 -1.2 | **PHADQ -0.8** | +0.4 |

PHADQ在SDR和PEMO-Q ODG指标上均优于l1正则化基线，主观MUSHRA测试也显示PHADQ获得更高评分。但实验仅在私有数据集上进行，缺乏公开数据集对比。

## 🎯 结论与影响

PHADQ通过相位感知正则化有效提升了音频去量化质量，避免了能量损失伪影。该方法可推广至其他音频修复任务，但需在更多公开数据集上验证。

## ⚠️ 局限与未解决问题

仅在私有数据集上评估，缺乏与更多基线方法的对比；未报告计算复杂度或推理时间；未分析不同量化比特率下的表现。

---

<div class="paper-footer"><span>评分：6.5</span><span>原始：6.5</span><a href="/audio-paper-daily/posts/2026-07-29/">← 返回 2026-07-29 速递</a></div>
