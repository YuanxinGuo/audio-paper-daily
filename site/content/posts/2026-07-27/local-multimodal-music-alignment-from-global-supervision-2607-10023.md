---
title: "Local Multimodal Music Alignment from Global Supervision"
date: 2026-07-27T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#多模态音乐对齐"]
summary: "提出FuSiLi相似度，通过Sinkhorn软对齐实现仅需全局监督即可学习局部多模态音乐对应关系。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#多模态音乐对齐</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#对比学习</span> <span class="tag-pill tag-pill-soft">#Sinkhorn对齐</span> <span class="tag-pill tag-pill-soft">#乐谱-音频对齐</span> <span class="tag-pill tag-pill-soft">#跨模态检索</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2607.10023</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-07-27</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2607.10023" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2607.10023" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出FuSiLi相似度，通过Sinkhorn软对齐实现仅需全局监督即可学习局部多模态音乐对应关系。
</div>

## 👥 作者与机构

**Irmak Bukey** ¹ · Zachary Novack · Jongmin Jung · Dasaem Jeong · Chris Donahue ✉

**机构**：卡内基梅隆大学 · 韩国艺术综合大学

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合多模态学习、音乐信息检索领域研究者。重点读§3的FuSiLi公式和§4的对比实验，可复现代码。

## 🌍 研究背景

音乐理解需要跨模态局部对应（如音频时间点对应乐谱位置），但局部标注昂贵。现有对比学习方法通常使用全局相似度，无法捕捉细粒度对齐。本文旨在仅利用全局配对监督（音频-乐谱片段对）学习局部对齐，填补这一空白。

## 💡 核心创新

1. 提出FuSiLi相似度，基于Sinkhorn算法实现局部特征软对齐
2. 混合对比学习目标，联合全局与局部相似度
3. 在CLIP/CLAP编码器上微调，无需从头训练
4. 在跨模态检索和帧级对齐任务上超越全局与局部基线

## 🏗️ 模型架构

输入：乐谱图像和对应音频。编码器：使用预训练CLIP（图像）和CLAP（音频）提取局部特征（图像块和音频帧）。关键模块：FuSiLi计算局部相似度矩阵，通过Sinkhorn迭代得到软对齐，再聚合为局部对比损失。同时保留全局对比损失（传统相似度）。输出：对齐后的特征用于检索和帧级对齐。

## 📚 数据集

- Scores2Performance（训练/评估，包含乐谱-音频对）
- CLEF（评估，跨模态检索）
- MusicNet（评估，帧级对齐）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| Recall@1 (检索) | Scores2Performance | CLAP+CLIP 全局对比 0.72 | **FuSiLi 0.75** | +0.03 |
| 帧级对齐准确率 | MusicNet | 全局对比 0.31 | **FuSiLi 0.45** | +0.14 |

在Scores2Performance上，FuSiLi在跨模态检索中Recall@1达0.75，优于全局对比基线0.72。在MusicNet帧级对齐任务上，准确率0.45，显著高于全局对比0.31，表明局部对齐能力提升。消融实验验证了Sinkhorn迭代和混合损失的有效性。

## 🎯 结论与影响

FuSiLi仅需全局监督即可学习局部多模态对齐，在检索和帧级对齐任务上均取得改进。该方法可推广至其他多模态场景（如视频-文本），为弱监督细粒度对齐提供了新思路。

## ⚠️ 局限与未解决问题

依赖预训练编码器（CLIP/CLAP），可能限制领域外泛化；Sinkhorn迭代增加计算开销；仅在音乐领域验证，未测试其他模态组合。

---

<div class="paper-footer"><span>评分：7.8</span><span>原始：7.8</span><a href="/audio-paper-daily/posts/2026-07-27/">← 返回 2026-07-27 速递</a></div>
