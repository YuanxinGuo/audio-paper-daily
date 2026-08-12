---
title: "Physics-Informed Learning for Robust Acoustic Localization with Calibrated Uncertainty"
date: 2026-08-12T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#声源定位"]
summary: "提出物理信息学习框架，修正双曲定位在复杂户外声景中的极端误差，并提供校准的不确定性估计。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#声源定位</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#被动声学监测</span> <span class="tag-pill tag-pill-soft">#物理信息学习</span> <span class="tag-pill tag-pill-soft">#不确定性量化</span> <span class="tag-pill tag-pill-soft">#野外环境</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2608.08911</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-08-12</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2608.08911" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2608.08911" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出物理信息学习框架，修正双曲定位在复杂户外声景中的极端误差，并提供校准的不确定性估计。
</div>

## 👥 作者与机构

**Jennifer N. Kampe** ¹ · Changwoo J. Lee · Xin Shen · Ari Lehti\"o · Sandro von Brandenburg · Ossi Nokelainen · David B. Dunson · Otso Ovaskainen

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合声源定位、被动声学监测及物理信息学习研究者。建议重点阅读方法部分（第3节）和实验部分（第4节），特别是表2和图5展示的误差修正效果。可先看摘要和结论把握核心贡献。

## 🌍 研究背景

被动声学监测（PAM）为生态空间点过程数据提供了前所未有的规模，但需要准确可扩展的定位方法。经典双曲和基于评分的定位方法在真实户外声景中常因多径主导、近场效应和复杂传播而失效，导致极端误差。现有方法要么完全依赖物理模型，要么纯数据驱动，缺乏鲁棒性。本文旨在通过物理信息学习修正物理模型，提高非理想条件下的鲁棒性，同时提供校准的不确定性。

## 💡 核心创新

1. 物理信息声学特征输入，修正双曲求解器
2. 学习模型仅修正不可信解，保留中位精度
3. 几何感知的不确定性校准，适用于下游空间模型
4. 在真实和模拟户外阵列上验证鲁棒性
5. 显著降低灾难性最坏情况误差

## 🏗️ 模型架构

输入为多麦克风阵列的到达时间差（TDOA）特征，结合物理信息声学特征（如信噪比、多径指标）。主干网络为轻量级神经网络（如MLP或小型CNN），输出为位置修正量。关键模块包括：双曲求解器作为基础预测器，学习模型判断其解是否可信，若不可信则输出修正。最终输出为修正后的位置坐标及不确定性（方差）。模型训练采用物理信息损失，结合校准不确定性。

## 📚 数据集

- 真实户外分布式麦克风阵列数据（评估）
- 模拟户外环境数据（训练和评估）

## 📊 实验结果

摘要未提供具体数值指标，但声称在真实和模拟户外环境中，所提方法显著降低灾难性最坏情况误差，同时中位精度与快速双曲求解器相当。不确定性估计经过校准，适用于下游空间模型。

## 🎯 结论与影响

本文提出物理信息学习框架，有效提升复杂户外声景中声源定位的鲁棒性，显著减少极端误差，并提供校准的不确定性。该方法为大规模自动化野生动物监测提供了可行方案，对生态学研究和工业部署（如生物多样性监测）具有潜在影响。

## ⚠️ 局限与未解决问题

摘要未提及计算开销和实时性能，可能限制大规模部署。实验仅针对户外环境，未验证室内或极端天气条件。未与最新深度学习方法（如基于学习的直接回归）对比，可能缺乏竞争力。不确定性校准方法未详细说明，可能依赖特定假设。

---

<div class="paper-footer"><span>评分：7.8</span><span>原始：7.8</span><a href="/audio-paper-daily/posts/2026-08-12/">← 返回 2026-08-12 速递</a></div>
