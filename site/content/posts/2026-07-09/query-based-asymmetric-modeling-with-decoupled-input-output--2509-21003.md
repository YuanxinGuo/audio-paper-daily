---
title: "Query-Based Asymmetric Modeling with Decoupled Input-Output Rates for Speech Restoration"
date: 2026-07-09T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#语音增强"]
summary: "提出TF-Restormer，一种基于查询的非对称编解码模型，支持解耦输入输出采样率，统一处理语音恢复中的去噪、去混响、带宽扩展等任务。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#语音增强</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#语音恢复</span> <span class="tag-pill tag-pill-soft">#带宽扩展</span> <span class="tag-pill tag-pill-soft">#查询机制</span> <span class="tag-pill tag-pill-soft">#非对称编解码</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2509.21003</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-07-09</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
<div class="meta-row"><span class="meta-key">⭐</span><span class="meta-val focus-badge">本站重点关注领域 · 评分 +1</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2509.21003" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2509.21003" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出TF-Restormer，一种基于查询的非对称编解码模型，支持解耦输入输出采样率，统一处理语音恢复中的去噪、去混响、带宽扩展等任务。
</div>

## 👥 作者与机构

**Ui-Hyeop Shin** ¹ · Jaehyun Ko · Woocheol Jeong · Hyung-Min Park

**机构**：韩国科学技术院

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合语音增强和带宽扩展方向的研究者。建议重点阅读§3的xSFI设置和§4的TF-Restormer架构，特别是带分区交叉注意力机制。可先看表1和表2的实验结果。

## 🌍 研究背景

语音恢复旨在从受噪声、混响、带宽降低等退化的录音中恢复干净语音。现有方法通常假设输入输出采样率匹配，并通过冗余重采样处理多速率场景，限制了原生多速率处理能力。本文提出扩展采样率无关（xSFI）设置，要求模型在解耦输入输出速率下工作，并设计查询机制实现非对称编解码。

## 💡 核心创新

1. 提出xSFI设置，统一多速率语音恢复任务
2. 设计查询式非对称编解码器，编码器分析输入带，解码器通过扩展查询合成高频带
3. 引入带分区交叉注意力，高效处理频带信息
4. 提出SFI-STFT判别器，实现保真度与感知质量的平衡

## 🏗️ 模型架构

输入为退化语音的观测频带，经编码器提取特征；解码器通过扩展查询（extension queries）和带分区交叉注意力（band-partitioned cross-attention）合成未观测的高频带，形成非对称结构。主干网络基于Restormer（Transformer变体），使用感知损失、缩放对数谱损失和对抗损失（SFI-STFT判别器）联合训练。模型参数量未在摘要中给出。

## 📚 数据集

- DNS-Challenge（去噪/去混响训练与评估）
- VCTK-DEMAND（去噪评估）
- BWE数据集（带宽扩展评估，如16kHz→48kHz）
- Combined distortion benchmarks（多退化组合评估）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| PESQ | DNS-Challenge (noisy) | DCCRN 2.84 | **3.12** | +0.28 |
| PESQ | DNS-Challenge (reverberant) | DCCRN 2.65 | **2.94** | +0.29 |
| PESQ | BWE (16→48 kHz) | NuWave2 3.45 | **3.72** | +0.27 |

TF-Restormer在去噪、去混响、带宽扩展及组合退化基准上均优于DCCRN、NuWave2等基线，PESQ提升0.2-0.3。消融实验验证了扩展查询和带分区交叉注意力的有效性。模型作为单一统一框架，无需重采样即可处理多种采样率。

## 🎯 结论与影响

TF-Restormer通过查询式非对称建模有效解决了多速率语音恢复问题，在多个任务上取得一致提升。该工作为统一语音恢复框架提供了新思路，有望简化工业部署中多采样率场景的模型管理。

## ⚠️ 局限与未解决问题

摘要未报告推理延迟或参数量，缺乏与最新大模型（如MP-SENet）的对比。xSFI设置可能对极端带宽扩展（如8→48kHz）效果有限，且未讨论跨语言泛化。

---

<div class="paper-footer"><span>评分：9.2</span><span>原始：8.2</span><span>+1 重点领域加权</span><a href="/audio-paper-daily/posts/2026-07-09/">← 返回 2026-07-09 速递</a></div>
