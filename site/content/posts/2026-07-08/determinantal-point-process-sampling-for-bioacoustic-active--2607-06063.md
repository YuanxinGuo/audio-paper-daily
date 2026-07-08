---
title: "Determinantal point process sampling for bioacoustic active learning"
date: 2026-07-08T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#生物声学"]
summary: "提出CARE-DPP方法，结合不确定性、新颖性和DPP采样进行批量主动学习，在BioDCASE挑战中提升生物声学分类性能。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero">
<div class="hero-score">
<div class="score-num">7.2</div>
<div class="score-stars">★★★★☆</div>
<div class="score-tier">前50%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#生物声学</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#主动学习</span> <span class="tag-pill tag-pill-soft">#确定性点过程</span> <span class="tag-pill tag-pill-soft">#音频分类</span> <span class="tag-pill tag-pill-soft">#数据选择</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2607.06063</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-07-08</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2607.06063" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2607.06063" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出CARE-DPP方法，结合不确定性、新颖性和DPP采样进行批量主动学习，在BioDCASE挑战中提升生物声学分类性能。
</div>

## 👥 作者与机构

**Hugo Magaldi** ¹ · Gabriel Dubus

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合从事主动学习、生物声学或音频分类的研究者阅读。建议重点看§3方法部分和表1的消融实验，了解DPP和自适应调度策略的设计。

## 🌍 研究背景

生态声学监测产生大量音频数据，人工标注成本高。主动学习通过选择最有价值的样本标注来降低标注量。现有方法如CoreSet仅考虑多样性，未充分利用不确定性。本文针对BioDCASE挑战，提出结合类平衡不确定性、嵌入空间新颖性和DPP多样性的批量主动学习方法。

## 💡 核心创新

1. 不确定性-新颖性平衡退火策略
2. DPP批量多样化选择
3. 自适应采集调度（小批量→大批量）
4. 混合候选池（高质量+随机探索）

## 🏗️ 模型架构

CARE-DPP方法：首先用预训练音频嵌入提取特征，计算每个样本的类平衡预测不确定性和嵌入空间新颖性，两者加权组合作为质量分数。然后构建DPP核矩阵，结合质量与相似度，通过DPP采样选择多样化批次。不确定性-新颖性权重随标注预算退火，早期侧重新颖性，后期侧重不确定性。候选池混合高质量样本和随机样本，随机比例递减。采集批次大小自适应，早期小批量，后期大批量。

## 📚 数据集

- BirdSet HSN（训练/评估）
- BirdSet POW（训练/评估）
- BirdSet UHH（训练/评估）
- ATBFL（训练/评估）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| macro mAP AULC | BirdSet HSN, POW, UHH + ATBFL | CoreSet 0.46 | **0.50** | +0.04 |

在BirdSet三个子集和ATBFL上，CARE-DPP平均AULC为0.50，优于CoreSet的0.46。消融实验表明DPP批量多样化和自适应采集调度贡献最大。

## 🎯 结论与影响

CARE-DPP通过结合不确定性、新颖性和DPP多样性，在生物声学主动学习任务上取得改进。该方法可推广至其他音频分类场景，降低标注成本。对工业生态监测系统有实用价值。

## ⚠️ 局限与未解决问题

仅在四个数据集上评估，泛化性待验证；未报告计算开销；未与更多主动学习方法对比；退火策略参数需手动调整。

---

<div class="paper-footer"><span>评分：7.2</span><span>原始：7.2</span><a href="/audio-paper-daily/posts/2026-07-08/">← 返回 2026-07-08 速递</a></div>
