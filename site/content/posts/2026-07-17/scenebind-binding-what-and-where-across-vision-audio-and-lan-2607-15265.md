---
title: "SceneBind: Binding What and Where Across Vision, Audio and Language"
date: 2026-07-17T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#多模态场景表示"]
summary: "SceneBind提出一种联合语义与3D空间理解的全模态场景表示方法，通过语义-空间槽实现跨视觉、音频和语言的场景检索与目标定位。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#多模态场景表示</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#跨模态检索</span> <span class="tag-pill tag-pill-soft">#双耳音频</span> <span class="tag-pill tag-pill-soft">#3D空间理解</span> <span class="tag-pill tag-pill-soft">#目标定位</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2607.15265</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-07-17</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
<div class="meta-row"><span class="meta-key">⭐</span><span class="meta-val focus-badge">本站重点关注领域 · 评分 +1</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2607.15265" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2607.15265" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>SceneBind提出一种联合语义与3D空间理解的全模态场景表示方法，通过语义-空间槽实现跨视觉、音频和语言的场景检索与目标定位。
</div>

## 👥 作者与机构

**Mingfei Chen** ¹ · Zijun Cui · Ruoke Zhang · Hyeonggon Ryu · Eli Shlizerman ✉

**机构**：华盛顿大学

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合多模态学习、场景理解、视听定位领域的研究者。建议重点阅读§3的语义-空间表示与匹配方案，以及§4的数据集构建与训练协议。可先看表1、2的检索与定位结果。

## 🌍 研究背景

现有全模态编码器（如ImageBind）擅长实例级语义理解（“有什么”），但缺乏显式空间结构（“在哪里”）。跨模态场景检索与目标定位任务中，需要同时捕捉语义和3D空间信息。此前方法多依赖单模态或弱空间建模，SceneBind旨在通过语义-空间槽表示弥补这一空白，并构建了首个带结构化语义与空间标注的双耳视听数据集。

## 💡 核心创新

1. 提出语义-空间槽表示，联合编码对象语义与3D位置
2. 设计SceneBind Matching，融合全局场景相似度与对象对齐
3. 构建真实世界双耳视听数据集，含结构化语义与空间标注
4. 兼容预训练语义编码器，仅需少量额外token实现空间建模

## 🏗️ 模型架构

输入：视觉图像、双耳音频、文本描述。主干：使用预训练语义编码器（如CLIP、AudioCLIP）提取全局语义嵌入，再通过轻量Transformer模块生成对象级语义-空间槽（每个槽包含语义特征与3D坐标）。输出：场景的全局语义嵌入+对象槽集合。SceneBind Matching模块计算跨模态场景相似度（全局+对象对齐），支持检索与目标定位。

## 📚 数据集

- SceneBind-Binaural（自建，训练/评估，真实场景双耳音频-视觉对，含语义与空间标注）
- SpatialAudio（评估，用于音频-视觉定位）
- AudioSet（预训练，语义编码器初始化）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| 场景检索Recall@1 | SceneBind-Binaural | ImageBind 0.72 | **0.85** | +0.13 |
| 空间检索Recall@1 | SceneBind-Binaural | ImageBind 0.31 | **0.68** | +0.37 |
| 音频-视觉定位准确率 | SpatialAudio | AVLNet 0.52 | **0.61** | +0.09 |

SceneBind在自建数据集上场景检索Recall@1达0.85，空间检索Recall@1达0.68，显著优于ImageBind。在SpatialAudio数据集上零样本音频-视觉定位准确率0.61，超越AVLNet。消融实验表明语义-空间槽对空间检索贡献最大。模型参数量仅增加5%，推理速度接近实时。

## 🎯 结论与影响

SceneBind通过语义-空间槽表示有效融合了场景的“是什么”与“在哪里”，在跨模态检索与定位任务上达到SOTA。其轻量设计兼容现有编码器，有望推动多模态场景理解在机器人、AR/VR等领域的应用。

## ⚠️ 局限与未解决问题

数据集规模有限（约10k场景），且仅含静态场景；未评估动态场景或时序建模。空间槽的3D坐标依赖相机位姿标注，实际部署需额外校准。未与更多基线（如3D-ALIGN）对比。

---

<div class="paper-footer"><span>评分：9.2</span><span>原始：8.2</span><span>+1 重点领域加权</span><a href="/audio-paper-daily/posts/2026-07-17/">← 返回 2026-07-17 速递</a></div>
