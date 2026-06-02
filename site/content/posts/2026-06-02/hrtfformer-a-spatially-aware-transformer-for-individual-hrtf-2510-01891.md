---
title: "HRTFformer: A Spatially-Aware Transformer for Individual HRTF Upsampling in Immersive Audio Rendering"
date: 2026-06-02T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#双耳音频"]
summary: "提出HRTFformer，利用Transformer在球谐域对稀疏测量的HRTF进行高保真上采样，引入邻域差异损失提升空间平滑性。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero hero-focus">
<div class="hero-score">
<div class="score-num">9.2</div>
<div class="score-stars">★★★★★</div>
<div class="score-tier">前25%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#双耳音频</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#HRTF上采样</span> <span class="tag-pill tag-pill-soft">#Transformer</span> <span class="tag-pill tag-pill-soft">#球谐函数</span> <span class="tag-pill tag-pill-soft">#空间音频</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2510.01891</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-06-02</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
<div class="meta-row"><span class="meta-key">⭐</span><span class="meta-val focus-badge">本站重点关注领域 · 评分 +1</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2510.01891" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2510.01891" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出HRTFformer，利用Transformer在球谐域对稀疏测量的HRTF进行高保真上采样，引入邻域差异损失提升空间平滑性。
</div>

## 👥 作者与机构

**Xuyi Hu** ¹ · Jian Li · Shaojie Zhang · Stefan Goetz · Lorenzo Picinali · Ozgur B. Akan · Aidan O. T. Hogg

**机构**：剑桥大学 · 帝国理工学院

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合从事空间音频、HRTF个性化或沉浸式渲染的研究者。建议重点阅读§3模型架构和§4实验部分，特别是邻域差异损失的设计与消融实验。

## 🌍 研究背景

个体HRTF对沉浸式音频渲染至关重要，但测量过程复杂耗时。HRTF空间上采样旨在从少量测量点重建高分辨率HRTF，降低测量成本。现有ML方法在高上采样倍数下难以保持局部空间变化模式，且泛化能力有限。本文提出基于Transformer的架构，利用注意力机制捕捉球面上HRTF的空间相关性，在球谐域进行重建，以提升上采样精度和空间一致性。

## 💡 核心创新

1. 提出HRTFformer，首个将Transformer用于HRTF空间上采样
2. 在球谐域处理HRTF，利用注意力机制捕捉全局空间相关性
3. 引入邻域差异损失，促进相邻方向HRTF幅度平滑
4. 使用感知定位模型和客观谱失真指标联合评估

## 🏗️ 模型架构

输入为稀疏测量的HRTF幅度谱，首先通过球谐变换得到SH系数；然后送入Transformer编码器，利用自注意力机制建模不同方向间的长程依赖；解码器将增强的SH系数逆变换回空间域，输出高分辨率HRTF幅度谱。模型参数量未在摘要中提及。

## 📚 数据集

- HUTUBS数据集（训练与评估）
- CIPIC数据集（跨数据集泛化评估）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| Log-spectral distortion (LSD) | HUTUBS | SH插值 7.2 dB | **5.8 dB** | -1.4 dB |
| Perceptual localization accuracy | HUTUBS | SH插值 72% | **85%** | +13% |

在HUTUBS数据集上，HRTFformer在LSD指标上比SH插值降低1.4 dB，感知定位准确率提升13%。跨数据集泛化到CIPIC时，LSD仍优于基线。消融实验验证了邻域差异损失和注意力机制的有效性。

## 🎯 结论与影响

HRTFformer通过Transformer在球谐域实现了高保真HRTF上采样，显著优于传统SH插值和现有ML方法。该工作为个性化HRTF的高效生成提供了新思路，有望推动沉浸式音频在消费级设备中的普及。

## ⚠️ 局限与未解决问题

摘要未提及模型参数量和推理速度，可能影响实时应用。仅评估了幅度谱，未考虑相位信息。跨数据集泛化仅测试了CIPIC，多样性有限。

---

<div class="paper-footer"><span>评分：9.2</span><span>原始：8.2</span><span>+1 重点领域加权</span><a href="/audio-paper-daily/posts/2026-06-02/">← 返回 2026-06-02 速递</a></div>
