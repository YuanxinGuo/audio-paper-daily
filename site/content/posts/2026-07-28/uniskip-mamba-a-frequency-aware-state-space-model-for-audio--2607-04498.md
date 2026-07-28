---
title: "UniSkip-Mamba: A Frequency-Aware State Space Model for Audio-Visual Temporal Forgery Localization"
date: 2026-07-28T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#音视频伪造定位"]
summary: "提出UniSkip-Mamba，利用频率感知的状态空间模型实现音视频时序伪造定位，在低频/中频区域聚焦判别性模式，SOTA性能且推理加速6倍。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#音视频伪造定位</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#状态空间模型</span> <span class="tag-pill tag-pill-soft">#频率分析</span> <span class="tag-pill tag-pill-soft">#多模态融合</span> <span class="tag-pill tag-pill-soft">#音视频取证</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2607.04498</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-07-28</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">🔥 强烈推荐通读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2607.04498" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2607.04498" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出UniSkip-Mamba，利用频率感知的状态空间模型实现音视频时序伪造定位，在低频/中频区域聚焦判别性模式，SOTA性能且推理加速6倍。
</div>

## 👥 作者与机构

**Cangjin Yu** ¹ · Quan Zhang · Dan Jiang · Ke Zhang

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合音视频取证、多模态学习、状态空间模型研究者。重点读§3频率分析发现和§4.2 Skip-Scanning Mamba模块。建议复现Group-Scan-Merge机制并对比Transformer基线。

## 🌍 研究背景

音视频时序伪造定位（AV-TFL）旨在检测篡改片段的起止时间。现有方法多基于Transformer时序建模或通道级多模态融合，但平等处理所有频率分量，易过拟合高频噪声，在真实退化场景下鲁棒性不足。本文通过频域分析发现伪造判别模式集中在低频/中频（归一化频率0-0.15），高频成分主要引入噪声，去除后检测性能提升1.4%。基于此提出频率感知的Mamba框架。

## 💡 核心创新

1. 统一多模态序列融合（UMSF）保持跨模态相位关系
2. Skip-Scanning Mamba模块通过Group-Scan-Merge机制实现频率感知正则化
3. 频域分析揭示伪造判别模式集中于低频/中频区域
4. 6倍推理加速于Transformer基线

## 🏗️ 模型架构

输入为音视频特征序列，经统一多模态序列融合（UMSF）对齐并保持相位关系，然后送入Skip-Scanning Mamba Blocks。每个Block包含Group-Scan-Merge机制：将序列分组，每组内沿不同扫描方向（前向/后向/跳跃）应用Mamba，合并后通过频率感知正则化偏置学习低频/中频模式。输出为伪造概率序列。模型参数量未提及。

## 📚 数据集

- LAV-DF（训练/评估，规模未提及）
- AV-Deepfake1M（训练/评估，规模未提及）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| AP@0.95 | LAV-DF | 未明确基线，但提升+9.8% | **63.4%** | +9.8% |
| mAP | AV-Deepfake1M | 未明确基线，但提升+14.32% | **63.58%** | +14.32% |

在LAV-DF上AP@0.95达63.4%，比最佳基线提升9.8%；在AV-Deepfake1M上mAP达63.58%，提升14.32%。推理速度比Transformer基线快6倍。消融实验验证了Skip-Scanning和频率正则化的有效性，去除高频噪声后性能提升1.4%。

## 🎯 结论与影响

本文通过频域分析揭示了音视频伪造定位中频率偏置现象，并提出UniSkip-Mamba框架，在两大基准上取得SOTA，同时推理加速6倍。该工作为状态空间模型在多媒体取证中的应用提供了新范式，并强调了频率感知设计的重要性，有望推动鲁棒伪造检测的工业部署。

## ⚠️ 局限与未解决问题

未报告参数量和FLOPs，难以评估计算效率全貌；仅验证了两个数据集，泛化性需更多测试；未与最新的Mamba变体（如VMamba）对比；频率分析基于特定数据集，可能不适用于其他伪造类型。

---

<div class="paper-footer"><span>评分：8.5</span><span>原始：8.5</span><a href="/audio-paper-daily/posts/2026-07-28/">← 返回 2026-07-28 速递</a></div>
