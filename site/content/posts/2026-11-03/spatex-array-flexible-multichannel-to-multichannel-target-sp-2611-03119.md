---
title: "SPATEX: Array-Flexible Multichannel-to-Multichannel Target Speech Extraction using Direction Clue"
date: 2026-11-03T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#目标说话人提取"]
summary: "提出首个阵列灵活的多通道到多通道目标说话人提取框架，利用麦克风坐标与目标DOA重建各通道目标语音并保留空间信息。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#目标说话人提取</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#目标说话人提取</span> <span class="tag-pill tag-pill-soft">#多通道语音处理</span> <span class="tag-pill tag-pill-soft">#空间音频</span> <span class="tag-pill tag-pill-soft">#阵列灵活</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2611.03119</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-11-02</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
<div class="meta-row"><span class="meta-key">⭐</span><span class="meta-val focus-badge">本站重点关注领域 · 评分 +1</span></div>
</div>
</div>

<div class="opensource-banner"><div class="oc-headline"><span class="oc-pulse"></span><span class="oc-title">本论文已开源</span><span class="oc-hint">点击下方卡片直达对应资源</span></div><div class="oc-grid"><a class="oc-chip oc-chip-code" href="https://github.com/Wenanzhi/SPATEX" target="_blank" rel="noopener"><span class="oc-icon">💻</span><span class="oc-text"><span class="oc-label">代码仓库</span><span class="oc-sub">Wenanzhi/SPATEX</span></span></a></div></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2611.03119" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2611.03119" target="_blank" rel="noopener">📑 PDF</a><a class="rsrc rsrc-code" href="https://github.com/Wenanzhi/SPATEX" target="_blank" rel="noopener">💻 代码</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出首个阵列灵活的多通道到多通道目标说话人提取框架，利用麦克风坐标与目标DOA重建各通道目标语音并保留空间信息。
</div>

## 👥 作者与机构

**Wen Wen** ¹ · Changda Chen · Yu Xi · Haoyu Li · Qiang Zhou · Guanyu Chen · Xiaoyu Gu · Bohan Li · … 等 2 人

**机构**：上海交通大学

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合做多通道语音增强/分离与空间音频的研究者阅读。建议通读，重点看 §3 的几何感知通道交换与共享时间注意力设计，以及表 2/表 3 中与固定阵列 MIMO 基线的对比和消融；工程落地者可关注 DOA 误差鲁棒性实验。

## 🌍 研究背景

多通道到多通道（MIMO）目标说话人提取需在每支麦克风处恢复目标语音并保留通道间空间信息，是双耳/空间音频渲染与下游波束成形的前端关键。此前 MIMO TSE 系统（如基于固定阵列的通道级重建方法）普遍假设麦克风数量与几何固定，换设备即失效；而阵列灵活的通用分离方法多为单输出，丢失空间线索。本文要解决的是在麦克风数量与阵列几何均可变的条件下，同时保证提取质量与空间保真度。

## 💡 核心创新

1. 首个阵列灵活的 MIMO TSE 框架，支持变麦克风数与任意几何
2. 几何感知通道交换模块，以麦克风坐标编码空间关系
3. 共享时间注意力实现通道间协调并保持置换等变
4. 空间监督与时间协调的消融验证

## 🏗️ 模型架构

输入为多通道混合语音特征，辅以麦克风坐标与目标 DOA 作为几何条件。主干采用通道维共享的时间注意力结构，先由几何感知通道交换模块依据麦克风坐标对通道特征做重排与交互，再经共享时间注意力在时间轴上建模并跨通道协调，输出每支麦克风的 target 语音波形，保持对通道排列的置换等变。摘要未给出参数量。

## 📚 数据集

- 自建多通道数据集（训练与评估，随代码开源）

## 📊 实验结果

摘要仅给出定性结论：在多数测试条件下优于阵列灵活的单输出基线，并在提取质量与空间保真度上稳定优于固定阵列 MIMO 基线；消融验证了时间协调与空间监督的有效性，额外实验显示对目标 DOA 误差具有鲁棒性。摘要未披露 SI-SDR、PESQ 等具体数值，需查阅原文表格。

## 🎯 结论与影响

最强结论是阵列几何与麦克风数可变条件下仍能完成 MIMO 目标提取并保留空间信息，打破固定阵列假设。这为跨设备的空间音频前端与真实录音场景部署提供可行路径，后续研究可在此基础上扩展至混响与移动阵列。

## ⚠️ 局限与未解决问题

摘要未给出具体指标与推理延迟，难以判断实时性；依赖目标 DOA 输入，虽报告鲁棒性但误差较大时的退化程度不明；数据集为自建，跨域泛化与与更多强基线（如固定阵列 SOTA）的全面对比仍待补充。

## 🔗 开源资源

- **代码**：<https://github.com/Wenanzhi/SPATEX>

---

<div class="paper-footer"><span>评分：8.8</span><span>原始：7.8</span><span>+1 重点领域加权</span><a href="/audio-paper-daily/posts/2026-11-03/">← 返回 2026-11-03 速递</a></div>
