---
title: "A Lightweight Dual-Branch Visual Front-End for Efficient Audio-Visual Target Speaker Extraction"
date: 2026-10-28T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#目标说话人提取"]
summary: "提出双分支视觉前端，用唇部ROI卷积与面部关键点时序卷积替代ResNet18，视觉编码计算降90%以上。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero hero-focus">
<div class="hero-score">
<div class="score-num">7.8</div>
<div class="score-stars">★★★★☆</div>
<div class="score-tier">中等</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#目标说话人提取</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#目标说话人提取</span> <span class="tag-pill tag-pill-soft">#视觉语音处理</span> <span class="tag-pill tag-pill-soft">#轻量化模型</span> <span class="tag-pill tag-pill-soft">#语音分离</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2610.36834</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-10-28</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
<div class="meta-row"><span class="meta-key">⭐</span><span class="meta-val focus-badge">本站重点关注领域 · 评分 +1</span></div>
</div>
</div>

<div class="opensource-banner"><div class="oc-headline"><span class="oc-pulse"></span><span class="oc-title">本论文已开源</span><span class="oc-hint">点击下方卡片直达对应资源</span></div><div class="oc-grid"><a class="oc-chip oc-chip-demo" href="https://anonymous.4open.science/r/Lightweight-Visual-Frontend-E46E" target="_blank" rel="noopener"><span class="oc-icon">🔊</span><span class="oc-text"><span class="oc-label">在线 Demo</span><span class="oc-sub">anonymous.4open.science/r/Lightweight-Visual-…</span></span></a></div></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2610.36834" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2610.36834" target="_blank" rel="noopener">📑 PDF</a><a class="rsrc rsrc-demo" href="https://anonymous.4open.science/r/Lightweight-Visual-Frontend-E46E" target="_blank" rel="noopener">🔊 Demo</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出双分支视觉前端，用唇部ROI卷积与面部关键点时序卷积替代ResNet18，视觉编码计算降90%以上。
</div>

## 👥 作者与机构

**Zhan Jin** ¹ · Peijun Yang · Juan Liu · Ming Li

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合做AVTSE与轻量化多模态前端的读者。值得通读，重点看§3双分支设计与表2/表3的计算量-性能权衡；若关注落地，先看融合模块与IIANet/SpatialNet接入细节，再核对LRS3-2mix统一训练协议是否公平。

## 🌍 研究背景

AVTSE通常用卷积图像编码器（如ResNet18）从人脸帧提取视觉特征，再与音频分支融合做目标说话人提取。当分离主干走向轻量化（IIANet、SpatialNet等）时，视觉编码的计算占比反而不可忽略，成为系统瓶颈。已有工作多聚焦分离主干或融合策略，较少系统重构视觉前端本身。本文要解决的是：在保持可用提取性能的前提下，大幅压缩视觉编码计算。

## 💡 核心创新

1. 双分支视觉前端：唇部ROI卷积分支建模局部发音线索
2. 面部关键点坐标经轻量时序卷积网络建模全局几何运动
3. 以有限融合开销将两路表示接入IIANet与SpatialNet
4. 在统一缩减训练协议下与ResNet18视觉编码做模块级计算对比

## 🏗️ 模型架构

输入为视频帧与音频混合信号。视觉侧分两路：一路裁剪紧凑唇部ROI，经卷积网络提取局部发音特征；另一路取面部关键点坐标序列，经轻量时序卷积网络（TCN）建模全局几何运动。两路表示以有限融合开销整合后，与音频特征一同送入分离主干IIANet或SpatialNet，输出目标说话人估计。摘要未给出参数量与具体层配置。

## 📚 数据集

- LRS3-2mix（训练与评估，统一缩减训练协议）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| 模块级视觉编码计算量 | LRS3-2mix | ResNet18 视觉编码器 | **双分支视觉前端** | 降低 90% 以上 |

在LRS3-2mix统一缩减训练协议下，所提前端在IIANet与SpatialNet两种主干上均取得接近轻量图像基线（ResNet18）的性能-计算折中，视觉编码计算降幅超过90%，性能差距为中等。摘要未给出SI-SDR等具体数值，也未报告端到端延迟与消融细节。

## 🎯 结论与影响

最强结论是：用唇部ROI加关键点坐标的双分支前端可在视觉编码计算降90%以上的同时保持接近ResNet18的提取性能。这提示AVTSE的视觉前端本身是可优化的计算瓶颈，对轻量化多模态分离与端侧部署有参考价值。

## ⚠️ 局限与未解决问题

对比不含人脸检测与关键点估计，实际端到端节省会被削弱；仅在LRS3-2mix单一数据集、缩减训练协议下验证，缺SI-SDR等绝对指标与消融；未报推理延迟与参数量；关键点质量对噪声与遮挡的鲁棒性未讨论。

## 🔗 开源资源

- **Demo / 试听**：<https://anonymous.4open.science/r/Lightweight-Visual-Frontend-E46E>

---

<div class="paper-footer"><span>评分：7.8</span><span>原始：6.8</span><span>+1 重点领域加权</span><a href="/audio-paper-daily/posts/2026-10-28/">← 返回 2026-10-28 速递</a></div>
