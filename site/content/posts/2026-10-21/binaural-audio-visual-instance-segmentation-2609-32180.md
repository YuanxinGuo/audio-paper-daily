---
title: "Binaural Audio-Visual Instance Segmentation"
date: 2026-10-21T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#双耳音频"]
summary: "提出双耳视听实例分割新任务BiAVIS，用双耳空间线索把发声实例从同类物体中区分开，并构建两个基准。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero hero-focus">
<div class="hero-score">
<div class="score-num">8.8</div>
<div class="score-stars">★★★★☆</div>
<div class="score-tier">前25%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#双耳音频</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#双耳音频</span> <span class="tag-pill tag-pill-soft">#视听分割</span> <span class="tag-pill tag-pill-soft">#声源定位</span> <span class="tag-pill tag-pill-soft">#多模态融合</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2609.32180</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-10-21</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
<div class="meta-row"><span class="meta-key">⭐</span><span class="meta-val focus-badge">本站重点关注领域 · 评分 +1</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2609.32180" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2609.32180" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出双耳视听实例分割新任务BiAVIS，用双耳空间线索把发声实例从同类物体中区分开，并构建两个基准。
</div>

## 👥 作者与机构

**Saijun Wang** ¹ · Guanfeng Tang · Hongbo Zhao · Zhicheng Lei · Yutong Zhang · Wei Ye · Rui Fan

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合做视听分割、双耳空间音频、声源定位的研究者阅读。值得通读：重点看 §3 的 BiAVISM 架构（audio-only SSL 网络如何把双耳线索投影到图像平面）与 §4 的 query-level 融合策略；实验部分先看 BiAVIS-Bench 上的表与消融，确认空间先验的增益来源。

## 🌍 研究背景

视听分割（AVS）此前主要在单声道设定下发展，代表方法如 AVSBench 上的 TPAVI、AVSS 等依赖跨模态语义对应来定位发声物体。这类方法的痛点是：当同一语义类别存在多个视觉相似实例时，仅靠语义匹配无法区分具体是哪一个在发声。人类依靠双耳听觉的耳间时间差/声级差以及头相关滤波带来的方向性声学线索进行空间定位，而现有 AVS 方法基本没有利用这一物理基础的空间信息。本文因此提出双耳视听实例分割任务，要求模型在像素级分割出发声实例，并借助双耳空间线索解决类内实例歧义。

## 💡 核心创新

1. 提出 BiAVIS 新任务：用同步双耳音频+视频做发声实例分割
2. 构建两个基准：重标注现有双耳视听数据集 + 新采集 BiAVIS-Bench
3. audio-only 声源定位网络，将双耳空间线索直接投影到图像平面
4. query-level 视听融合策略，把空间/语义先验注入实例分割解码器

## 🏗️ 模型架构

输入为同步的双耳音频波形与视频帧。音频分支是一个仅音频的声源定位网络（audio-only SSL），利用双耳耳间差异与方向性滤波线索估计声源方位，并将其直接投影到图像平面，形成空间与语义先验图；视觉分支提取帧级特征并送入实例分割解码器（query-based 结构，输出实例 mask 与类别）。关键模块是 query-level 视听融合：把音频分支产生的空间先验以 query 级别注入分割解码器的实例 query，使每个实例 query 携带方向性空间信息，从而在同类多实例场景下区分发声目标。输出为像素级发声实例分割结果。摘要未给出参数量。

## 📚 数据集

- 现有双耳视听数据集（人工重标注，用于训练/评估）
- BiAVIS-Bench（新采集真实场景，用于评估，更具挑战性）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| mAP | BiAVIS-Bench | AVISM | **26.65** | 相对提升约 35.35% |
| FSLA | BiAVIS-Bench | ACVIS | **45.90** | 相对提升约 11.62% |

在两个自建基准上，BiAVISM 均优于此前的单声道 AVS 方法，尤其在类内实例歧义场景下提升明显。在更难的 BiAVIS-Bench 上达到 26.65 mAP 与 45.90 FSLA，相对 AVISM 的 mAP 提升约 35.35%，相对 ACVIS 的 FSLA 提升约 11.62%。摘要未给出消融细节、推理延迟与跨数据集泛化结果。

## 🎯 结论与影响

最强结论是：双耳空间线索能有效解决单声道 AVS 难以处理的类内实例歧义，在实例级分割指标上带来显著提升。该工作开辟了双耳视听实例分割方向并给出两个基准，后续研究可在此基础上探索更精细的空间线索建模与跨场景泛化。对工业落地而言，双耳麦克风在耳机、AR/VR 与机器人听觉中普遍存在，该任务具备实际应用潜力。

## ⚠️ 局限与未解决问题

摘要未提供消融实验来单独验证 audio-only SSL 分支与 query-level 融合各自的贡献；两个基准均为作者自建，标注规模与标注一致性未说明，存在数据 bias 风险；未报告推理延迟与模型参数量，难以评估实用性；对比基线以单声道 AVS 方法为主，缺少与其他双耳/空间音频方法的比较。

---

<div class="paper-footer"><span>评分：8.8</span><span>原始：7.8</span><span>+1 重点领域加权</span><a href="/audio-paper-daily/posts/2026-10-21/">← 返回 2026-10-21 速递</a></div>
