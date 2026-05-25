---
title: "AffectCodec: Emotion-Preserving Neural Speech Codec with Block-Diagonal Residual FSQ"
date: 2026-05-25T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#语音编解码"]
summary: "提出AffectCodec，通过块对角残差有限标量量化（BD-RFSQ）在低比特率下保留语音情感信息，同时保持声学质量。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#语音编解码</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#情感保留</span> <span class="tag-pill tag-pill-soft">#残差有限标量量化</span> <span class="tag-pill tag-pill-soft">#语音压缩</span> <span class="tag-pill tag-pill-soft">#语音语言模型</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2605.23373</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-05-25</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2605.23373" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2605.23373" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出AffectCodec，通过块对角残差有限标量量化（BD-RFSQ）在低比特率下保留语音情感信息，同时保持声学质量。
</div>

## 👥 作者与机构

**Zhaoyang Meng** ¹ · Zhengyao Ma · Kecan Mao · Yingming Gao · Ya Li

**机构**：北京理工大学

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合语音编解码、情感计算和语音语言模型研究者。建议重点阅读§3的BD-RFSQ设计和§4的实验结果，特别是表1和表2。可先看§3.2理解块对角投影机制。

## 🌍 研究背景

神经语音编解码器作为语音语言模型的离散接口，主要优化声学重建保真度，导致情感相关线索在量化中被丢弃。现有方法在有限比特率下采用重建驱动的比特分配，且拼接式编解码器中存在跨流泄漏，使情感维度被声学梯度覆盖。本文旨在通过结构化的量化方法显式保留情感信息。

## 💡 核心创新

1. 提出块对角残差有限标量量化（BD-RFSQ），将情感和声学子空间投影分离
2. BD-RFSQ将比特分配从隐式损失驱动变为显式结构保证
3. 结合多粒度情感条件化和多速率训练，实现低比特率下鲁棒情感保留

## 🏗️ 模型架构

输入语音经编码器提取特征，送入BD-RFSQ模块。BD-RFSQ采用块对角输入和输出投影，将情感和声学子空间解耦，每个子空间独立进行残差有限标量量化。量化后得到扁平token序列，供下游语音语言模型使用。解码器结合多粒度情感条件化（全局和局部情感嵌入）重建语音。支持多速率训练，适应不同比特率。

## 📚 数据集

- EmoV-DB（情感语音数据集，训练/评估）
- RAVDESS（情感语音数据集，训练/评估）
- CREMA-D（情感语音数据集，训练/评估）
- LibriTTS（纯净语音，用于声学质量评估）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| 情感识别准确率（%） | RAVDESS | EnCodec (24 kbps) 72.3 | **AffectCodec (24 kbps) 78.1** | +5.8% |
| 情感识别准确率（%） | RAVDESS | EnCodec (6 kbps) 58.2 | **AffectCodec (6 kbps) 70.5** | +12.3% |
| PESQ | LibriTTS | EnCodec (24 kbps) 4.12 | **AffectCodec (24 kbps) 4.08** | -0.04 |
| PESQ | LibriTTS | EnCodec (6 kbps) 3.45 | **AffectCodec (6 kbps) 3.42** | -0.03 |

在多个情感语音基准上，AffectCodec在低比特率（6 kbps）下情感识别准确率比EnCodec提升12.3%，同时PESQ仅下降0.03，表明情感保留显著改善而声学质量几乎无损。消融实验验证了BD-RFSQ和多粒度情感条件化的有效性。

## 🎯 结论与影响

AffectCodec通过结构保护的量化（BD-RFSQ）有效保留情感信息，在低比特率下优势明显。该工作为属性感知的神经语音压缩提供了新思路，有望推动情感语音语言模型的发展。工业上可用于低带宽情感通信和情感语音合成。

## ⚠️ 局限与未解决问题

未在真实低比特率通信场景下测试；情感评估仅依赖识别准确率，缺乏主观MOS测试；未与最新编解码器（如SoundStream、HiFi-Codec）对比；BD-RFSQ的块大小选择未充分消融。

---

<div class="paper-footer"><span>评分：8.2</span><span>原始：8.2</span><a href="/audio-paper-daily/posts/2026-05-25/">← 返回 2026-05-25 速递</a></div>
