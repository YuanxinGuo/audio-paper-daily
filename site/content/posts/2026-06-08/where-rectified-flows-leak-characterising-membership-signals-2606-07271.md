---
title: "Where Rectified Flows Leak: Characterising Membership Signals Along the Interpolation Path"
date: 2026-06-08T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#生成模型安全"]
summary: "研究Rectified Flow在插值路径上泄露训练数据成员信息的现象，发现训练与测试数据重构误差呈钟形曲线差异，并利用此进行成员推断攻击。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero">
<div class="hero-score">
<div class="score-num">6.5</div>
<div class="score-stars">★★★☆☆</div>
<div class="score-tier">前50%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#生成模型安全</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#Rectified Flows</span> <span class="tag-pill tag-pill-soft">#成员推断攻击</span> <span class="tag-pill tag-pill-soft">#隐私</span> <span class="tag-pill tag-pill-soft">#音频生成</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2606.07271</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-06-08</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2606.07271" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2606.07271" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>研究Rectified Flow在插值路径上泄露训练数据成员信息的现象，发现训练与测试数据重构误差呈钟形曲线差异，并利用此进行成员推断攻击。
</div>

## 👥 作者与机构

**Thomas Sesmat** ¹ · Gabriel Meseguer-Brocal · Geoffroy Peeters

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合对生成模型隐私安全感兴趣的读者。建议重点阅读第3节（理论分析）和第4节（实验验证），特别是图2和表1。可跳过第2节背景。

## 🌍 研究背景

生成模型可能从训练数据中记忆信息，引发版权和隐私问题。现有研究多关注逐字复制，但模型可能编码更隐蔽的痕迹。Rectified Flow作为一种新兴生成模型，其训练过程涉及从噪声到数据的插值路径。本文旨在探究该路径上是否存在可被利用的成员信息信号，并量化其特性。

## 💡 核心创新

1. 发现训练与测试数据重构误差沿插值路径呈钟形曲线差异
2. 推导高斯假设下峰值位置的闭式解
3. 利用λ分辨结构实现成员推断攻击

## 🏗️ 模型架构

基于Rectified Flow模型，定义插值路径X_λ = (1-λ)X_0 + λX_1，其中X_0为噪声，X_1为数据。训练过程中模型学习从X_0到X_1的映射。本文分析沿λ的重构误差，并利用其差异进行成员推断。

## 📚 数据集

- 音频数据集（训练/评估，未具体命名）
- 图像数据集（训练/评估，未具体命名）

## 📊 实验结果

摘要未提供具体数值结果，但声称在音频和图像上验证了钟形曲线结构的普适性，并在满足高斯假设时峰值预测准确。成员推断攻击作为概念验证，展示了该信号的可利用性。

## 🎯 结论与影响

本文揭示了Rectified Flow在插值路径上泄露训练数据成员信息的机制，为生成模型隐私研究提供了新视角。该发现可能促使未来设计更安全的训练流程，并提醒部署时注意成员推断风险。

## ⚠️ 局限与未解决问题

理论分析基于高斯假设，实际数据分布可能偏离；未报告成员推断攻击的具体成功率；仅在有限数据集上验证，泛化性待考；未与现有成员推断方法对比。

---

<div class="paper-footer"><span>评分：6.5</span><span>原始：6.5</span><a href="/audio-paper-daily/posts/2026-06-08/">← 返回 2026-06-08 速递</a></div>
