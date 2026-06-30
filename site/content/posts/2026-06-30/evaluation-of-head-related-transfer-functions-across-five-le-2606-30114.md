---
title: "Evaluation of Head-Related Transfer Functions Across Five Levels of Individualisation in Virtual Reality"
date: 2026-06-30T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#双耳音频"]
summary: "在VR中比较五种不同个性化程度的HRTF对声源定位的影响，发现高分辨率合成HRTF可媲美实测，而摄影测量合成HRTF和KEMAR性能最差。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero hero-focus">
<div class="hero-score">
<div class="score-num">8.5</div>
<div class="score-stars">★★★★☆</div>
<div class="score-tier">前25%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#双耳音频</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#双耳音频</span> <span class="tag-pill tag-pill-soft">#虚拟现实</span> <span class="tag-pill tag-pill-soft">#声源定位</span> <span class="tag-pill tag-pill-soft">#个性化</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2606.30114</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-06-30</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
<div class="meta-row"><span class="meta-key">⭐</span><span class="meta-val focus-badge">本站重点关注领域 · 评分 +1</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2606.30114" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2606.30114" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>在VR中比较五种不同个性化程度的HRTF对声源定位的影响，发现高分辨率合成HRTF可媲美实测，而摄影测量合成HRTF和KEMAR性能最差。
</div>

## 👥 作者与机构

**Ludovic Pirard** ¹ · Katarina C. Poole

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合双耳音频、VR音频研究者。重点看§3实验设计和§4结果（图/表）。建议先读§4.2极坐标指标和混淆率部分，再结合§5讨论选择非个性化HRTF的实用建议。

## 🌍 研究背景

HRTF是实现VR/AR空间听觉的关键，但个性化HRTF获取成本高，因此通用HRTF（如KEMAR）和合成HRTF被广泛使用。然而，不同个性化程度HRTF的感知差异缺乏系统性比较。本文通过19名听者在VR中完成定位实验，在受试者内比较五种HRTF条件（实测、KEMAR、随机非实测、高分辨率扫描合成、摄影测量合成），旨在量化各条件的相对性能。

## 💡 核心创新

1. 首次在单一研究中系统比较五种个性化程度的HRTF
2. 采用受试者内设计，结合互补子集条件实现直接对比
3. 发现高分辨率合成HRTF在极坐标指标上匹配实测性能
4. 揭示摄影测量合成HRTF和KEMAR在仰角定位上的显著退化
5. 验证了实测基线跨会话的测试-重测稳定性

## 🏗️ 模型架构

本研究为感知实验，无模型架构。实验使用19名听者，在VR环境中进行声源定位任务。HRTF条件包括：个体实测（B&K 4128C人工耳）、KEMAR、随机非个体实测、高分辨率扫描合成（3D扫描+边界元法）、摄影测量合成（摄影测量+边界元法）。实验采用互补子集条件，每个听者完成两个实验，条件交错，实现受试者内比较。

## 📚 数据集

- 19名听者（实验数据，训练/评估均使用同一批听者）

## 📊 实验结果

摘要未提供具体数值指标，但报告了关键发现：横向定位指标对HRTF类型不敏感，而极坐标指标和混淆率强烈依赖HRTF。随机非个体HRTF在多个极坐标指标上优于KEMAR。高分辨率合成HRTF与实测性能相当，而摄影测量合成HRTF和KEMAR退化最严重。测试-重测稳定性支持跨实验合并。

## 🎯 结论与影响

本文通过系统比较五种HRTF条件，明确了非个性化HRTF的实用选择：高分辨率合成HRTF可替代实测，而KEMAR和摄影测量合成HRTF在仰角定位上表现较差。结果强调了网格分辨率在数值合成中的重要性，为VR音频系统的HRTF选择提供了实验依据。

## ⚠️ 局限与未解决问题

样本量较小（19人），且未评估个体差异对结果的影响。实验仅使用VR环境，可能无法完全推广到真实声场。未报告HRTF合成方法的计算成本或实时性。未比较其他合成方法（如基于PCA的个性化）。

---

<div class="paper-footer"><span>评分：8.5</span><span>原始：7.5</span><span>+1 重点领域加权</span><a href="/audio-paper-daily/posts/2026-06-30/">← 返回 2026-06-30 速递</a></div>
