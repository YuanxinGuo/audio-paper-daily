---
title: "Removing Speech, Keeping Activities: A Privacy Firewall for Acoustic Sensing in Assisted Living"
date: 2026-09-03T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#语音增强"]
summary: "提出基于U-Net的隐私防火墙，从环境音频中去除语音而保留活动声音，在合成数据上训练，实现0%可检测语音且保持活动识别性能。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero hero-focus">
<div class="hero-score">
<div class="score-num">8.2</div>
<div class="score-stars">★★★★☆</div>
<div class="score-tier">前25%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#语音增强</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#语音增强</span> <span class="tag-pill tag-pill-soft">#活动识别</span> <span class="tag-pill tag-pill-soft">#隐私保护</span> <span class="tag-pill tag-pill-soft">#U-Net</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2609.02376</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-09-03</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
<div class="meta-row"><span class="meta-key">⭐</span><span class="meta-val focus-badge">本站重点关注领域 · 评分 +1</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2609.02376" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2609.02376" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出基于U-Net的隐私防火墙，从环境音频中去除语音而保留活动声音，在合成数据上训练，实现0%可检测语音且保持活动识别性能。
</div>

## 👥 作者与机构

**Pavlos Nicolaou** ¹ · Christos Efstratiou

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合从事语音增强、隐私保护、环境声音识别的研究者阅读。建议重点阅读第3节的模型架构和第4节的实验部分，特别是表2和表3的结果。可先看摘要和结论，再深入方法细节。

## 🌍 研究背景

在辅助生活场景中，声学传感用于监测老年人日常活动，但语音隐私问题阻碍实际部署。现有语音增强方法如Facebook Denoiser、SepFormer等主要面向语音质量提升，不适用于去除语音而保留环境声音。本文提出一种基于U-Net的隐私防火墙，在合成数据上训练，旨在去除语音同时保留活动相关声音，以支持隐私保护的活动识别。

## 💡 核心创新

1. 提出隐私防火墙概念，将语音去除视为语音增强的逆任务
2. 使用U-Net编码器-解码器，在合成数据上训练，无需真实隐私数据
3. 结合VGGish迁移学习和SVM进行活动识别，验证隐私保护后的可用性
4. 在多个语音水平下实现0% VAD可检测语音，优于现有降噪方法
5. 在真实家庭录音上验证，保持76%的精度和召回率

## 🏗️ 模型架构

输入为环境音频的log-mel频谱图，通过U-Net编码器-解码器进行语音去除，输出为处理后的频谱图，再转换为音频。U-Net包含下采样和上采样路径，具有跳跃连接。活动识别使用VGGish提取特征，然后输入SVM分类器。模型在合成数据上训练，合成数据由环境声音和语音混合而成。

## 📚 数据集

- ESC-50（评估，包含环境声音分类，用于活动识别评估）
- SINS（评估，用于活动识别评估）
- AudioHive（真实家庭录音，评估）
- 合成数据（训练，由环境声音和语音混合生成）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| VAD可检测语音比例 | ESC-50 (100%语音水平) | Facebook Denoiser 6.55% | **0%** | -6.55% |
| VAD可检测语音比例 | ESC-50 (100%语音水平) | SepFormer 36.34% | **0%** | -36.34% |
| VAD可检测语音比例 | ESC-50 (100%语音水平) | ConvTasNet 47.21% | **0%** | -47.21% |
| 分类精度/召回率 | ESC-50 (40%语音水平) | 去除前 81%/75% | **85%/85%** | +4%/+10% |

在ESC-50上，不同语音水平下，所提方法均实现0% VAD可检测语音，优于Facebook Denoiser、SepFormer和ConvTasNet。在40%语音水平下，去除语音后分类精度和召回率分别恢复至85%和85%，接近无语音基线的84%/83%。在真实家庭录音中，处理后0% VAD可检测语音，同时保持76%的精度和召回率。

## 🎯 结论与影响

本文提出的隐私防火墙能有效去除语音而保留活动声音，实现隐私保护的活动识别，解决了辅助生活声学传感的主要障碍。该方法在合成数据上训练，可泛化到真实场景，为隐私保护声学传感提供了新思路，有望推动环境监测在老年护理中的应用。

## ⚠️ 局限与未解决问题

实验仅在ESC-50和SINS数据集上评估，缺乏更多样化的真实环境验证。未报告模型参数量和推理延迟，可能影响实时部署。未与更多最新的语音去除方法比较。此外，合成数据训练可能引入域偏移，影响泛化。

---

<div class="paper-footer"><span>评分：8.2</span><span>原始：7.2</span><span>+1 重点领域加权</span><a href="/audio-paper-daily/posts/2026-09-03/">← 返回 2026-09-03 速递</a></div>
