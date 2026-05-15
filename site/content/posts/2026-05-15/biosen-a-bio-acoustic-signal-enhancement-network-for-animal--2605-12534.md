---
title: "BioSEN: A Bio-acoustic Signal Enhancement Network for Animal Vocalizations"
date: 2026-05-15T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#注意力机制", "#生物声学", "#语音增强", "#谐波增强"]
summary: "提出BioSEN，一种针对动物发声的语音增强网络，通过多尺度双轴注意力、谐波增强和能量自适应门控，在三个生物声学数据集上以更低计算量达到或超越SOTA。"
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
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#生物声学</span> <span class="tag-pill tag-pill-soft">#语音增强</span> <span class="tag-pill tag-pill-soft">#注意力机制</span> <span class="tag-pill tag-pill-soft">#谐波增强</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2605.12534</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-05-15</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
<div class="meta-row"><span class="meta-key">⭐</span><span class="meta-val focus-badge">本站重点关注领域 · 评分 +1</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2605.12534" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2605.12534" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出BioSEN，一种针对动物发声的语音增强网络，通过多尺度双轴注意力、谐波增强和能量自适应门控，在三个生物声学数据集上以更低计算量达到或超越SOTA。
</div>

## 👥 作者与机构

**Tianyu Song** ¹ · Ton Viet Ta · Ngamta Thamwattana · Hisako Nomura · Linh Thi Hoai Nguyen

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合从事生物声学、语音增强或跨领域应用的研究者。建议通读，重点看§3模型架构和§4实验对比。可复现其开源代码并测试于自身数据集。

## 🌍 研究背景

现有语音增强方法主要针对人类语音，而生物声学信号因噪声复杂、动物声音特性独特（如谐波结构）而研究不足。之前SOTA多为通用语音增强模型（如SEGAN、Conv-TasNet），但直接迁移效果有限。本文旨在设计专门针对动物发声的增强网络，解决噪声环境下动物声音保留与噪声抑制的平衡问题。

## 💡 核心创新

1. 多尺度双轴注意力单元（MS-DAA）提取时频特征
2. 生物谐波多尺度增强单元（BH-MSE）捕获谐波结构
3. 能量自适应门控连接单元（EAG）防止误删发声

## 🏗️ 模型架构

输入为对数梅尔谱或STFT幅度谱。主干网络包含三个模块：1) 多尺度双轴注意力单元（MS-DAA），沿时间和频率轴分别应用注意力，融合多尺度特征；2) 生物谐波多尺度增强单元（BH-MSE），利用谐波模板增强周期性成分；3) 能量自适应门控连接单元（EAG），根据频率能量权重调整门控，保留弱发声。输出为增强后的时频谱或波形。参数量未提及。

## 📚 数据集

- Bioacoustic Dataset A（训练/评估，具体名称未给出）
- Bioacoustic Dataset B（训练/评估）
- Bioacoustic Dataset C（训练/评估）

## 📊 实验结果

摘要未提供具体数值指标，仅说明BioSEN在三个生物声学数据集上匹配或超越SOTA语音增强模型，且计算量显著更低。建议查看全文获取SI-SDR、PESQ等定量结果。

## 🎯 结论与影响

BioSEN在生物声学增强任务上以更低计算量达到SOTA性能，证明针对动物声音特性的设计有效。该工作有望推动生物多样性监测和生态保护中的音频分析应用，为后续生物声学专用模型研究提供基线。

## ⚠️ 局限与未解决问题

摘要未提及模型在极端噪声或多种动物混合场景下的表现，也未报告推理延迟或参数量。缺乏与最新生物声学专用方法的对比（如BirdNET增强模块）。数据集细节和消融实验需在正文中验证。

---

<div class="paper-footer"><span>评分：8.8</span><span>原始：7.8</span><span>+1 重点领域加权</span><a href="/audio-paper-daily/posts/2026-05-15/">← 返回 2026-05-15 速递</a></div>
