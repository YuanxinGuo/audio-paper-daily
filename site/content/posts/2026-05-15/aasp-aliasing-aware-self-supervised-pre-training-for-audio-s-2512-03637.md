---
title: "AaSP: Aliasing-aware Self-Supervised Pre-Training for Audio Spectrogram Transformers"
date: 2026-05-15T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#自监督学习"]
summary: "提出抗混叠自监督预训练框架AaSP，通过混叠感知补丁嵌入和教师-学生掩码建模提升音频频谱图变换器的表示质量。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#自监督学习</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#音频频谱图变换器</span> <span class="tag-pill tag-pill-soft">#抗混叠</span> <span class="tag-pill tag-pill-soft">#掩码建模</span> <span class="tag-pill tag-pill-soft">#对比学习</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2512.03637</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-05-15</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2512.03637" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2512.03637" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出抗混叠自监督预训练框架AaSP，通过混叠感知补丁嵌入和教师-学生掩码建模提升音频频谱图变换器的表示质量。
</div>

## 👥 作者与机构

**Kohei Yamamoto** ¹ · Kosuke Okusa

**机构**：东京大学

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合从事音频自监督学习或频谱图变换器研究的读者。建议重点阅读§3.2的AaPE模块设计和§4的实验结果，特别是表2的消融研究。可先看§3.1整体框架再深入细节。

## 🌍 研究背景

基于Transformer的音频自监督学习模型通常使用频谱图、视觉风格Transformer和掩码建模目标。然而，卷积分块与时间下采样会降低有效奈奎斯特频率并引入混叠，而简单的低通滤波可能去除任务相关的高频信息。现有方法未专门处理混叠问题，限制了表示质量。本文旨在设计一种混叠感知的预训练框架，以学习对混叠更鲁棒的音频表示。

## 💡 核心创新

1. 提出混叠感知补丁嵌入模块AaPE，融合标准补丁令牌与混叠频带特征
2. 采用带限复正弦核与双边指数窗实现自适应子带分析
3. 结合教师-学生掩码建模与多掩码对比正则化
4. 从输入估计核的频率和衰减参数，实现自适应
5. 在多个声学/环境、语音和音乐基准上取得SOTA

## 🏗️ 模型架构

输入为对数梅尔频谱图，经AaPE模块处理：首先通过标准卷积分块得到补丁令牌，同时使用带限复正弦核（参数由输入估计）提取混叠频带特征，两者融合后输入Transformer编码器。预训练采用教师-学生框架，学生网络对掩码补丁进行预测，教师网络提供目标，并引入交叉注意力预测器与多掩码对比正则化。模型参数量未提及。

## 📚 数据集

- AudioSet（预训练，约2M样本）
- AS-20K（微调/线性评估）
- ESC-50（微调/线性评估）
- NSynth（微调/线性评估）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| Accuracy | AS-20K | AST 0.5M (48.1) | **AaSP (50.2)** | +2.1% |
| Accuracy | ESC-50 | AST 0.5M (97.2) | **AaSP (97.8)** | +0.6% |
| Accuracy | NSynth | AST 0.5M (79.8) | **AaSP (81.2)** | +1.4% |

在微调设置下，AaSP在AS-20K、ESC-50和NSynth上超越所有自监督基线，包括AST 0.5M和MAE-AST等。线性评估中，AaSP在US8K和NSynth上表现最佳，且整体趋势与微调一致。消融实验验证了AaPE、交叉注意力预测器和多掩码对比正则化的贡献。模型在混叠敏感的时间扰动下表现出更稳定的表示。

## 🎯 结论与影响

AaSP通过显式建模混叠频带，显著提升了音频频谱图变换器的自监督预训练质量，在多个基准上达到SOTA。该工作为音频SSL中的混叠问题提供了有效解决方案，有望推动下游任务性能提升。工业上可应用于更鲁棒的音频分类系统。

## ⚠️ 局限与未解决问题

论文未报告模型参数量和推理速度，计算开销不明确。预训练仅使用AudioSet，未验证在其他大规模数据集上的泛化性。混叠感知核的设计可能增加训练复杂度，且对非平稳噪声的鲁棒性未探讨。

---

<div class="paper-footer"><span>评分：8.2</span><span>原始：8.2</span><a href="/audio-paper-daily/posts/2026-05-15/">← 返回 2026-05-15 速递</a></div>
