---
title: "Sound-based Multi-Person 3D Pose Estimation"
date: 2026-09-07T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#人体姿态估计"]
summary: "首次尝试仅用声音估计多人3D姿态，提出SoundMHPE编码器-解码器框架，并构建AMP数据集验证其有效性。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#人体姿态估计</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#声学感知</span> <span class="tag-pill tag-pill-soft">#多模态</span> <span class="tag-pill tag-pill-soft">#注意力机制</span> <span class="tag-pill tag-pill-soft">#多尺度编码</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2609.04902</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-09-07</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner"><div class="oc-headline"><span class="oc-pulse"></span><span class="oc-title">本论文已开源</span><span class="oc-hint">点击下方卡片直达对应资源</span></div><div class="oc-grid"><a class="oc-chip oc-chip-proj" href="https://oumi03.github.io/sound-mhpe/" target="_blank" rel="noopener"><span class="oc-icon">🌐</span><span class="oc-text"><span class="oc-label">项目主页</span><span class="oc-sub">oumi03.github.io/sound-mhpe/</span></span></a></div></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2609.04902" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2609.04902" target="_blank" rel="noopener">📑 PDF</a><a class="rsrc rsrc-proj" href="https://oumi03.github.io/sound-mhpe/" target="_blank" rel="noopener">🌐 项目主页</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>首次尝试仅用声音估计多人3D姿态，提出SoundMHPE编码器-解码器框架，并构建AMP数据集验证其有效性。
</div>

## 👥 作者与机构

**Yusuke Oumi** ¹ · Yuto Shibata · Go Irie · Akisato Kimura · Yoshimitsu Aoki · Mariko Isogawa

**机构**：东京理科大学 · 东京大学 · NTT

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合对非视觉感知、多模态人体姿态估计感兴趣的研究者。建议重点阅读第3节方法部分和第4节实验设置，可先看模型架构图与表1对比结果。若关注声学信号处理，可略读数据采集细节。

## 🌍 研究背景

人体姿态估计通常依赖视觉传感器，但在遮挡、隐私或低光场景下受限。声学信号具有非视距感知潜力，但现有工作仅处理单人场景。多人场景下，声学信号叠加和人际反射导致难以分离个体姿态特征。本文首次探索纯声学多人3D姿态估计，需解决信号叠加和反射干扰问题。

## 💡 核心创新

1. 提出SoundMHPE，首个纯声学多人3D姿态估计框架
2. 设计Acoustic Multi-scale Encoder提取多尺度时频特征
3. 采用Temporal Pose Decoder注意力机制解耦多人时序信息
4. 构建6小时AMP数据集，含432K同步帧
5. 在多人场景下验证优于基线模型

## 🏗️ 模型架构

输入为多通道声学信号（如麦克风阵列），经预处理后送入Acoustic Multi-scale Encoder，该编码器包含多个并行卷积分支，分别捕获不同时间尺度和频率分辨率的特征，并融合输出。随后Temporal Pose Decoder采用Transformer-like注意力机制，对帧序列进行建模，通过自注意力捕捉帧间依赖，交叉注意力解耦不同人的特征，最后输出每帧每个人的3D关键点坐标。整体为端到端训练，未提及参数量。

## 📚 数据集

- AMP数据集（训练/评估，6小时，432K帧，多人姿态与声学同步数据）

## 📊 实验结果

摘要未提供具体数值指标，仅说明SoundMHPE在AMP数据集上优于基线模型。实验部分可能包含定量对比和消融研究，但具体数据需查阅全文。

## 🎯 结论与影响

本文首次证明仅用声学信号估计多人3D姿态的可行性，提出的SoundMHPE框架有效处理信号叠加和反射问题。该工作为声学感知开辟新方向，可能推动非视觉人体感知在隐私敏感场景的应用，但距离实际部署仍有距离。

## ⚠️ 局限与未解决问题

摘要未提及局限，但作为首创工作，可能面临数据集规模有限、场景单一（室内？）、多人数量限制、声学干扰鲁棒性等问题。缺乏与视觉方法的对比，且未报告推理延迟等效率指标。

## 🔗 开源资源

- **项目主页**：<https://oumi03.github.io/sound-mhpe/>

---

<div class="paper-footer"><span>评分：7.2</span><span>原始：7.2</span><a href="/audio-paper-daily/posts/2026-09-07/">← 返回 2026-09-07 速递</a></div>
