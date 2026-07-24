---
title: "DynFOA: Generating First-Order Ambisonics with Conditional Diffusion for Dynamic and Acoustically Complex 360-Degree Videos"
date: 2026-07-24T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#空间音频生成"]
summary: "提出DynFOA，利用条件扩散模型和3D场景重建从360度视频生成一阶环绕声，在动态和声学复杂场景中优于现有方法。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero hero-focus">
<div class="hero-score">
<div class="score-num">9.5</div>
<div class="score-stars">★★★★★</div>
<div class="score-tier">前25%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#空间音频生成</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#双耳音频</span> <span class="tag-pill tag-pill-soft">#扩散模型</span> <span class="tag-pill tag-pill-soft">#3D高斯溅射</span> <span class="tag-pill tag-pill-soft">#360度视频</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2602.06846</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-07-24</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
<div class="meta-row"><span class="meta-key">⭐</span><span class="meta-val focus-badge">本站重点关注领域 · 评分 +1</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2602.06846" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2602.06846" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出DynFOA，利用条件扩散模型和3D场景重建从360度视频生成一阶环绕声，在动态和声学复杂场景中优于现有方法。
</div>

## 👥 作者与机构

**Ziyu Luo** ¹ · Lin Chen · Qiang Qu · Xiaoming Chen · Yiran Shen

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合空间音频、沉浸式媒体、扩散模型生成音频方向的研究者。建议重点阅读§3方法部分（场景重建与条件扩散）和§4实验（M2G-360数据集与对比结果）。可先看§3.2与表2。

## 🌍 研究背景

360度视频缺乏空间音频是沉浸式体验的瓶颈。现有方法仅依赖视觉线索，无法建模动态声源和声学效应（遮挡、反射、混响）。本文旨在从视频生成一阶环绕声（FOA），需解决动态场景和复杂声学交互的建模问题。

## 💡 核心创新

1. 融合3D高斯溅射重建场景几何与材质
2. 条件扩散模型利用物理特征生成空间音频
3. 构建M2G-360数据集含动态/多源/几何子集

## 🏗️ 模型架构

输入360度视频帧→通过检测和定位动态声源、估计深度与语义，利用3D高斯溅射（3DGS）重建场景几何与材质→提取物理特征（声源-环境-听者交互）→条件扩散模型（基于U-Net）生成FOA信号（4通道B格式）。

## 📚 数据集

- M2G-360（600个真实世界片段，含MoveSources/Multi-Source/Geometry子集，用于训练和评估）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| Spatial Accuracy (SA) | M2G-360 | AV-Diff (0.72) | **0.85** | +0.13 |
| Acoustic Fidelity (AF) | M2G-360 | AV-Diff (0.68) | **0.79** | +0.11 |
| Distribution Matching (DM) | M2G-360 | AV-Diff (0.65) | **0.74** | +0.09 |
| Perceived Immersive Experience (PIE) | M2G-360 | AV-Diff (3.2) | **4.1** | +0.9 |

DynFOA在M2G-360所有子集上均优于AV-Diff等基线，尤其在动态声源和复杂几何场景中提升显著。消融实验验证了3DGS重建和条件扩散模块的有效性。模型参数量未提及，但推理速度可能受3DGS重建影响。

## 🎯 结论与影响

DynFOA通过3D场景重建与条件扩散模型，首次实现了对动态和声学复杂360度视频的高质量FOA生成，显著提升了空间准确性和沉浸感。该方法为空间音频生成提供了新范式，有望推动VR/AR内容制作。

## ⚠️ 局限与未解决问题

依赖3DGS重建的计算开销，未报告推理时间；M2G-360数据集规模有限（600段），且未在真实录制FOA数据上验证；未与基于物理声学的方法对比；未讨论多说话人场景下的分离性能。

---

<div class="paper-footer"><span>评分：9.5</span><span>原始：8.5</span><span>+1 重点领域加权</span><a href="/audio-paper-daily/posts/2026-07-24/">← 返回 2026-07-24 速递</a></div>
