---
title: "Efficient Audio Enhancement with a Differentiable Psychoacoustic Loss"
date: 2026-08-05T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#音频增强"]
summary: "提出基于Mamba的高效音频增强模型AEROMamba，结合可微PAQM感知损失，在带宽扩展和压缩音频恢复上超越基线，且大幅降低计算开销。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#音频增强</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#音频超分辨率</span> <span class="tag-pill tag-pill-soft">#Mamba</span> <span class="tag-pill tag-pill-soft">#感知损失</span> <span class="tag-pill tag-pill-soft">#音频增强</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2608.02918</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-08-05</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2608.02918" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2608.02918" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出基于Mamba的高效音频增强模型AEROMamba，结合可微PAQM感知损失，在带宽扩展和压缩音频恢复上超越基线，且大幅降低计算开销。
</div>

## 👥 作者与机构

**Wallace Abreu** ¹ · Bernardo V. Miranda · Luiz W. P. Biscainho

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合音频增强、超分辨率及高效模型设计研究者。建议重点阅读第3节（方法）和第4节（实验），特别是PAQM损失的设计与Mamba架构的替换细节。可先看摘要和结论，再深入实验部分。

## 🌍 研究背景

音频增强旨在提升音频感知质量，包括带宽扩展和压缩音频恢复。现有方法如AERO采用注意力与LSTM，计算开销大。感知损失多基于简单距离或已有指标，与主观质量相关性有限。本文旨在通过轻量级状态空间模型（Mamba）和可微感知损失（PAQM）实现高效且高质量的增强。

## 💡 核心创新

1. 用Mamba替换AERO中的注意力与LSTM层，降低计算复杂度
2. 提出可微PAQM感知损失，直接优化感知质量
3. 针对压缩音频恢复，用PAQM损失替代STFT重建损失
4. 在带宽扩展和压缩恢复两个任务上验证有效性
5. 实现14倍推理加速和2-4倍训练显存节省

## 🏗️ 模型架构

AEROMamba基于AERO超分辨率架构，将注意力与LSTM层替换为Mamba状态空间模型。输入为低分辨率/压缩音频的STFT幅度谱，经Mamba编码器提取特征，再通过解码器重建高分辨率/高质量音频。训练时使用可微PAQM损失（针对带宽扩展）或PAQM损失替代STFT重建损失（针对压缩恢复）。模型参数量未提及，但推理显存仅为基线的1/5。

## 📚 数据集

- 钢琴数据集（训练/评估，用于带宽扩展）
- MUSDB18（训练/评估，用于带宽扩展）
- MP3压缩音频（训练/评估，用于压缩恢复）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| 主观感知质量评分 | 钢琴数据集和MUSDB18（11.025kHz→44.1kHz） | AERO（100%） | **AEROMamba_P（115%）** | +15% |
| 主观感知质量评分 | MP3 32kbps压缩音频 | AEROMamba_P（100%） | **AEROMamba_PS（152%）** | +52% |

主观听感测试显示，在带宽扩展任务中，AEROMamba_P比AERO感知质量高15%；在压缩音频恢复中，AEROMamba_PS比AEROMamba_P高52%。推理速度提升14倍，GPU内存减少至1/5，训练显存节省2-4倍。

## 🎯 结论与影响

本文证明PAQM驱动的训练与轻量级状态空间模型结合，能在带宽扩展和压缩音频恢复中实现高感知质量和计算效率。该工作为音频增强提供了新范式，有望推动实时音频处理应用。

## ⚠️ 局限与未解决问题

摘要未提供客观指标（如PESQ、SI-SDR），仅依赖主观测试，可能受听者偏好影响。未报告模型参数量、推理延迟的具体数值，也未与更多SOTA方法对比。压缩恢复实验仅针对MP3 32kbps，泛化性未知。

---

<div class="paper-footer"><span>评分：7.8</span><span>原始：7.8</span><a href="/audio-paper-daily/posts/2026-08-05/">← 返回 2026-08-05 速递</a></div>
