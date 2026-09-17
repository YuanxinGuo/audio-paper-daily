---
title: "Arti-JEPA: Adapting Video World Model to Real-Time MRI of the Vocal Tract for Speech-Production Analysis"
date: 2026-09-17T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#语音识别"]
summary: "将视频世界模型 V-JEPA 适配到实时 MRI 声道视频，冻结表征用于音素预测、口吃分类与舌切除术后分析。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero">
<div class="hero-score">
<div class="score-num">6.8</div>
<div class="score-stars">★★★☆☆</div>
<div class="score-tier">前50%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#语音识别</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#自监督学习</span> <span class="tag-pill tag-pill-soft">#发音运动建模</span> <span class="tag-pill tag-pill-soft">#医学语音分析</span> <span class="tag-pill tag-pill-soft">#视频世界模型</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2609.09757</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-09-17</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2609.09757" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2609.09757" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>将视频世界模型 V-JEPA 适配到实时 MRI 声道视频，冻结表征用于音素预测、口吃分类与舌切除术后分析。
</div>

## 👥 作者与机构

**Hong Nguyen** ¹ · Sean Foley · Christina Hagedorn · Yijing Lu · Sudarsana Reddy Kadiri · Dani Byrd · Shrikanth Narayanan

**机构**：南加州大学

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合做发音语音学、rtMRI 语音分析、临床语音评估与自监督表征的研究者。若关注语音增强/分离则相关性低。建议重点看 §3 的域适应目标与 §4 三个下游探针设置，表 2 的 κ 对比与术后解码结果最值得细读，可先跳过视频世界模型背景介绍。

## 🌍 研究背景

rtMRI 能捕捉发音时整个声道的动态，但标注数据稀缺，且单切片、灰度、低分辨率的特点与自然视频差异大，导致在自然视频上预训练的视频基础模型难以直接迁移。此前发音研究多依赖逐帧图像编码器或小规模监督模型，缺少时序先验与跨域泛化能力。本文要解决的是：如何用自监督视频世界模型在无标注 rtMRI 上继续预训练，并检验冻结表征在音素、流畅度与术后临床任务上的可迁移性。

## 💡 核心创新

1. 在 62h 无标注 rtMRI 上继续 V-JEPA 自监督目标，得到域适应声道编码器
2. 系统对比时序视频先验 vs 逐帧图像编码器、潜空间预测 vs 像素重建
3. 用冻结探针量化术前/术后舌切除语音的可解码性，定位迁移差距来源

## 🏗️ 模型架构

输入为单切片灰度 rtMRI 声道视频帧序列，主干沿用 V-JEPA 的联合嵌入预测架构：编码器提取时空表征，预测器在潜空间预测被掩码区域的表征，训练目标为潜空间预测损失而非像素重建。在约 62h 无标注声道视频上继续自监督预训练后冻结编码器，仅训练轻量下游探针，分别用于音素预测、流畅/不流畅二分类以及术前术后对比。摘要未给出参数量与具体层数。

## 📚 数据集

- 无标注声道 rtMRI 视频约 62h（自监督继续预训练）
- 典型说话人音素标注语料（跨域音素预测评估）
- 含口吃语音语料（流畅/不流畅分类评估）
- 舌部分切除患者术前/术后 rtMRI（临床迁移评估）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| Cohen's κ | 跨域音素预测 | 未域适应编码器 | **0.352** | 约翻倍 |

摘要给出三点结论：时序视频先验显著优于逐帧图像编码器，潜空间预测（V-JEPA）至少与像素重建（VideoMAE）相当，且在细粒度音素上更优；域适应效果任务相关，跨域音素预测 κ 约翻倍至 0.352，但对二分类口吃检测无帮助；术后解码不低于术前，域内探针在患者上的表现至少与典型说话人相当。摘要未报告 SI-SDR、PESQ 等信号级指标，也未给出推理延迟与消融细节。

## 🎯 结论与影响

最强结论是：冻结的域适应 rtMRI 编码器可作为可复用的测量工具，术后解码未下降说明迁移差距来自跨说话人/域错配而非手术信号损失。这为发音语音学与临床语音科学提供了低成本表征方案，后续研究可围绕跨说话人对齐与更细粒度发音单元展开，工业上可用于临床语音评估与康复监测。

## ⚠️ 局限与未解决问题

作者承认域适应收益任务相关，对二分类任务无效。作为审稿人可见：仅报告 κ 单一指标，缺少与监督 rtMRI 模型的充分对比；62h 数据来源与说话人多样性未说明，存在域偏置；未报告推理延迟与模型规模；术后结论基于小样本患者，统计效力存疑。

---

<div class="paper-footer"><span>评分：6.8</span><span>原始：6.8</span><a href="/audio-paper-daily/posts/2026-09-17/">← 返回 2026-09-17 速递</a></div>
