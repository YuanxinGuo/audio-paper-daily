---
title: "Objects as Audio-Visual Modal Sound Fields"
date: 2026-08-11T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#音频生成"]
summary: "提出AV-MSF，用3D高斯泼溅和视觉特征先验，从多视图图像和少量撞击声重建物体级模态声音场，实现高质量撞击声渲染。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#音频生成</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#3D高斯泼溅</span> <span class="tag-pill tag-pill-soft">#模态声音场</span> <span class="tag-pill tag-pill-soft">#少样本重建</span> <span class="tag-pill tag-pill-soft">#视听学习</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2608.05145</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-08-11</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2608.05145" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2608.05145" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出AV-MSF，用3D高斯泼溅和视觉特征先验，从多视图图像和少量撞击声重建物体级模态声音场，实现高质量撞击声渲染。
</div>

## 👥 作者与机构

**Zisen Shao** ¹ · Zihao Wei · Derong Jin · Ruohan Gao

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合音频生成、3D重建和视听学习研究者。建议重点阅读方法部分（§3）和实验对比（§4），可先看§3.2的模态参数表示和§4.2的定量结果。

## 🌍 研究背景

现代3D重建能建模物体几何和外观，但忽略物理交互产生的丰富声学线索。物体撞击声反映材质、刚度和结构，但现有方法要么依赖昂贵的物理模拟，要么需要大数据集进行纯数据驱动学习。本文旨在从多视图图像和少量撞击声重建物体级声场，实现高效少样本重建。

## 💡 核心创新

1. 提出AV-MSF，结合3DGS和密集视觉特征作为几何先验
2. 用紧凑的物理模态参数表示撞击声场，实现少样本重建
3. 在真实数据集上超越物理模拟和数据驱动基线
4. 展示接触定位和声音编辑等下游应用

## 🏗️ 模型架构

输入多视图图像和少量撞击声录音。使用3D高斯泼溅（3DGS）重建物体几何，并集成密集3D视觉特征提供几何感知先验。撞击声场用模态参数表示，通过神经网络预测每个高斯的模态参数，最终渲染撞击声。

## 📚 数据集

- 真实世界数据集1（训练和评估）
- 真实世界数据集2（训练和评估）

## 📊 实验结果

摘要未提供具体数值，但声称在两个真实数据集上达到SOTA，优于物理模拟和数据驱动基线。还展示了接触定位和声音编辑等下游应用。

## 🎯 结论与影响

AV-MSF通过结合3DGS和模态参数，实现了从少量样本重建物体级撞击声场，显著优于现有方法。该表示有望推动视听学习、虚拟现实和机器人交互等应用，为物体级声学建模提供新思路。

## ⚠️ 局限与未解决问题

摘要未提及局限。可能的问题包括：模态参数表示对复杂声音的泛化能力、对多视图图像质量的依赖、以及未报告推理延迟和计算开销。

---

<div class="paper-footer"><span>评分：8.2</span><span>原始：8.2</span><a href="/audio-paper-daily/posts/2026-08-11/">← 返回 2026-08-11 速递</a></div>
