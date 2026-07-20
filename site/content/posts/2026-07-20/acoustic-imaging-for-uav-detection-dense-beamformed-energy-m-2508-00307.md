---
title: "Acoustic Imaging for UAV Detection: Dense Beamformed Energy Maps and U-Net SELD"
date: 2026-07-20T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#声源定位"]
summary: "提出U-Net模型将360°声源定位转化为球面语义分割任务，通过分割波束成形能量图实现无人机检测，并泛化至DCASE SELD任务。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero">
<div class="hero-score">
<div class="score-num">7.2</div>
<div class="score-stars">★★★★☆</div>
<div class="score-tier">前25%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#声源定位</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#无人机检测</span> <span class="tag-pill tag-pill-soft">#声学成像</span> <span class="tag-pill tag-pill-soft">#U-Net</span> <span class="tag-pill tag-pill-soft">#波束成形</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2508.00307</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-07-20</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2508.00307" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2508.00307" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出U-Net模型将360°声源定位转化为球面语义分割任务，通过分割波束成形能量图实现无人机检测，并泛化至DCASE SELD任务。
</div>

## 👥 作者与机构

**Belman Jahir Rodriguez** ¹ · Sergio F. Chevtchenko · Marcelo Herrera Martinez · Yeshwanth Bethi · Saeed Afshar

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合声源定位、无人机声学检测及SELD领域研究者。建议重点阅读§3方法部分（波束成形能量图生成与U-Net分割）及§4实验（无人机数据集与DCASE泛化结果）。可先看表1、图3了解性能。

## 🌍 研究背景

传统声源定位（SSL）通常将问题视为离散方向到达角（DoA）回归，难以处理空间分布声源。波束成形虽能生成空间能量图，但后续处理依赖阈值或峰值拾取，鲁棒性不足。本文提出将SSL重新定义为球面语义分割任务，利用U-Net分割波束成形能量图，实现密集空间声学理解，并首次应用于无人机检测。

## 💡 核心创新

1. 将SSL重新定义为球面语义分割任务
2. 使用U-Net分割波束成形能量图而非回归DoA
3. 引入Tversky损失处理类别不平衡
4. 方法具有阵列无关性，可迁移至不同麦克风配置
5. 在无人机检测和DCASE SELD两个任务上验证泛化性

## 🏗️ 模型架构

输入：24麦克风阵列接收信号，经延迟求和（DAS）波束成形生成方位-俯仰能量图（频率域表示）。主干网络：修改的U-Net，编码器-解码器结构，用于分割能量图。输出：二值分割图（声源存在区域），后处理计算质心得到DoA估计。模型参数量未提及。

## 📚 数据集

- 自建无人机数据集（真实开阔场地录制，DJI Air 3，同步360°视频和飞行日志，多日期多地点）
- DCASE 2019 TAU Spatial Sound Events（评估泛化性，多类SELD场景）

## 📊 实验结果

摘要未提供具体数值指标，仅定性说明U-Net在不同环境下泛化良好，角精度提升。在DCASE 2019上验证了波束成形加分割公式对多类SELD的泛化能力。

## 🎯 结论与影响

本文提出将声源定位转化为语义分割的新范式，通过U-Net分割波束成形能量图，在无人机检测和DCASE SELD任务上展示了有效性和泛化性。该方法阵列无关，可适应不同麦克风配置，为密集空间声学理解提供了新思路，有望推动无人机声学监测和通用SELD的发展。

## ⚠️ 局限与未解决问题

摘要未报告定量结果（如角度误差、检测率），缺乏与现有SSL方法的直接对比。仅使用单一无人机型号，泛化性需更多机型验证。未讨论计算复杂度或实时性。DCASE实验细节不足。

---

<div class="paper-footer"><span>评分：7.2</span><span>原始：7.2</span><a href="/audio-paper-daily/posts/2026-07-20/">← 返回 2026-07-20 速递</a></div>
