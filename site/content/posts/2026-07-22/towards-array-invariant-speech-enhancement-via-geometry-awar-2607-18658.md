---
title: "Towards Array-Invariant Speech Enhancement via Geometry-Aware Dynamic Convolution"
date: 2026-07-22T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#语音增强"]
summary: "提出几何感知动态卷积框架，将固定阵列语音增强模型扩展为阵列不变系统，在RealMAN数据集上验证有效性。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#语音增强</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#多通道语音增强</span> <span class="tag-pill tag-pill-soft">#阵列不变性</span> <span class="tag-pill tag-pill-soft">#动态卷积</span> <span class="tag-pill tag-pill-soft">#几何感知</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2607.18658</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-07-22</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
<div class="meta-row"><span class="meta-key">⭐</span><span class="meta-val focus-badge">本站重点关注领域 · 评分 +1</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2607.18658" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2607.18658" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出几何感知动态卷积框架，将固定阵列语音增强模型扩展为阵列不变系统，在RealMAN数据集上验证有效性。
</div>

## 👥 作者与机构

**Zhenglong Liu** ¹ · Wangyou Zhang · Chenda Li · Yanmin Qian

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合研究多通道语音增强和阵列泛化的读者。建议重点阅读§3的Geo-DConv模块设计和§4的实验结果，特别是表2对不同阵列拓扑的对比。可先看§3.2与图2理解动态卷积如何融合几何信息。

## 🌍 研究背景

多通道语音增强利用空间信息优于单通道，但传统方法依赖固定阵列几何，难以部署于不同设备。现有阵列无关方法虽能处理可变通道数，但未充分利用已知的阵列几何先验，限制了空间滤波性能。本文旨在解决如何将固定阵列模型泛化到任意阵列，同时利用几何信息提升性能。

## 💡 核心创新

1. 提出Geo-DConv模块，将麦克风坐标编码为动态卷积核
2. 设计坐标编码网络，将几何信息映射为卷积核权重
3. 实现固定阵列模型到阵列不变系统的无缝转换

## 🏗️ 模型架构

输入多通道时频特征，首先通过坐标编码网络将麦克风坐标映射为动态卷积核参数。主干网络采用标准固定阵列SE模型（如Conv-TasNet或DPT-FSNet），将其中的静态卷积替换为Geo-DConv。Geo-DConv根据输入坐标生成位置自适应卷积核，实现空间滤波。输出为增强后的单通道语音。

## 📚 数据集

- RealMAN（训练/评估，真实记录多通道语音，含多种阵列拓扑）

## 📊 实验结果

摘要未提供具体数值，但声称在RealMAN数据集上，Geo-DConv使两种固定阵列模型（Conv-TasNet和DPT-FSNet）在阵列不变设置下均取得一致性能提升，且适用于多种阵列拓扑。

## 🎯 结论与影响

本文提出的Geo-DConv框架有效解决了多通道语音增强的阵列不变性问题，通过显式利用麦克风坐标，将固定阵列模型泛化到任意几何。该工作为实际部署中跨设备阵列适配提供了可行方案，有望推动多通道SE在消费电子和通信系统中的应用。

## ⚠️ 局限与未解决问题

仅在一个数据集（RealMAN）上验证，缺乏跨数据集泛化实验；未报告计算开销或推理延迟；未与最新的阵列无关方法（如FaSNet）进行对比；未分析坐标编码的鲁棒性（如噪声对坐标的影响）。

---

<div class="paper-footer"><span>评分：8.8</span><span>原始：7.8</span><span>+1 重点领域加权</span><a href="/audio-paper-daily/posts/2026-07-22/">← 返回 2026-07-22 速递</a></div>
