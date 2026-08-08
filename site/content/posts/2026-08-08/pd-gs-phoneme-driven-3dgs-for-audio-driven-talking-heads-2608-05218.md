---
title: "PD-GS: Phoneme-Driven 3DGS for Audio-Driven Talking Heads"
date: 2026-08-08T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#语音驱动说话头生成"]
summary: "PD-GS通过音素驱动3DGS，利用ASR强制对齐的音素令牌增强口型准确性，减少唇部闭合错误。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#语音驱动说话头生成</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#3D高斯泼溅</span> <span class="tag-pill tag-pill-soft">#语音驱动</span> <span class="tag-pill tag-pill-soft">#口型同步</span> <span class="tag-pill tag-pill-soft">#音素对齐</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2608.05218</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-08-08</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2608.05218" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2608.05218" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>PD-GS通过音素驱动3DGS，利用ASR强制对齐的音素令牌增强口型准确性，减少唇部闭合错误。
</div>

## 👥 作者与机构

**Ao Fu** ¹ · Yi Zhou

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合从事语音驱动动画、3DGS渲染或口型同步的研究者。建议重点阅读第3节（方法）和第4节（实验），特别是LFM模块的设计和表2的LMD对比。可先看摘要和结论，再深入方法细节。

## 🌍 研究背景

3DGS在说话头生成中实现快速逼真渲染，但口型精度不足，存在过度平滑和唇部闭合违规（如双唇闭合）导致的“漏嘴”伪影。现有方法从连续声学嵌入回归口型，偏向平均嘴型，难以捕捉短暂离散的发音事件。自监督语音编码器虽提供丰富线索，但缺乏帧级语言目标。本文提出音素驱动3DGS，利用ASR强制对齐的音素令牌提供显式语言约束，解决闭合级事件歧义。

## 💡 核心创新

1. 引入时间对齐音素令牌作为显式语言目标
2. 设计Linguistic Fusion Module（LFM）自适应融合音频和音素嵌入
3. 通过门控机制保留音频动态同时强化音素指导
4. 仅用单目视频和图像重建及唇部关键点监督训练

## 🏗️ 模型架构

输入为单目视频帧和对应音频。音频经自监督编码器提取连续特征，同时ASR强制对齐生成音素令牌序列。LFM模块通过可学习门控融合音频特征和音素嵌入，输出融合特征。该特征驱动3DGS渲染说话头。训练使用图像重建损失和唇部关键点损失。

## 📚 数据集

- HDTF（训练和评估，包含多说话人视频）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| LMD | HDTF | 未提供具体基线值 | **2.66** | 未提供 |

在HDTF上，PD-GS实现了最佳唇部几何（LMD 2.66），相比基线减少了挑战性音素序列中的闭合违规，产生更语言上忠实的神经化身。摘要未提供其他指标如PSNR或SSIM，也未提供消融实验细节。

## 🎯 结论与影响

PD-GS通过音素驱动3DGS显著提升口型准确性，减少唇部闭合错误，为语音驱动说话头提供新思路。该方法有望推动更逼真的虚拟化身应用，并可能启发结合显式语言约束的其他生成任务。

## ⚠️ 局限与未解决问题

摘要未提及推理速度、参数量或跨数据集泛化。可能依赖ASR对齐质量，且仅在HDTF上评估，缺乏多样性。未与最新SOTA如DiffTalk或Audio2Face对比。

---

<div class="paper-footer"><span>评分：7.8</span><span>原始：7.8</span><a href="/audio-paper-daily/posts/2026-08-08/">← 返回 2026-08-08 速递</a></div>
