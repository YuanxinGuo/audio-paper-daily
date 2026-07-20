---
title: "Data-driven Video Codec with Implicit Neural Representations"
date: 2026-07-20T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#视频编解码"]
summary: "提出用单个SIREN网络同时编码视频和音频，通过知识蒸馏和量化压缩，但性能远低于传统编解码器。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero">
<div class="hero-score">
<div class="score-num">5.5</div>
<div class="score-stars">★★★☆☆</div>
<div class="score-tier">后50%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#视频编解码</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#隐式神经表示</span> <span class="tag-pill tag-pill-soft">#SIREN</span> <span class="tag-pill tag-pill-soft">#知识蒸馏</span> <span class="tag-pill tag-pill-soft">#视频压缩</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2607.15298</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-07-20</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">✋ 可以跳过</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2607.15298" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2607.15298" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出用单个SIREN网络同时编码视频和音频，通过知识蒸馏和量化压缩，但性能远低于传统编解码器。
</div>

## 👥 作者与机构

**Nishan Khanal** ¹ · Saugat Neupane · Abhinav Chalise · Nimesh Gopal Pradhan · Dinesh Baniya Kshatri

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合对隐式神经表示在视频压缩中应用感兴趣的读者。可重点看§3的架构设计和§4的量化分析，但整体方法实用性有限，不建议通读。

## 🌍 研究背景

传统视频编解码器如H.264/HEVC依赖手工设计的变换和熵编码，而基于学习的隐式神经表示（INR）方法将视频编码为网络权重，但通常只处理视频或音频单一模态。现有INR方法在压缩效率和重建质量上仍远落后于传统标准。本文尝试用单个SIREN网络联合编码视频和音频，并通过知识蒸馏和量化减小模型大小。

## 💡 核心创新

1. 联合视频音频的SIREN网络架构
2. 双路Siamese音频分支用于残差噪声估计
3. 基于知识蒸馏的教师-学生压缩策略
4. 16-bit对称量化与LZMA2无损编码
5. 浏览器端WebRTC原型系统

## 🏗️ 模型架构

输入为空间-时间坐标(x,y,t)，通过独立的视频和音频初始化层后，进入共享的全连接隐藏层（SIREN激活）。输出分为三个分支：视频分支输出RGB值，两个Siamese音频分支输出音频振幅，其差异用于估计并减去残差噪声。教师网络过拟合训练后，通过响应式知识蒸馏压缩为更小的学生网络，再经16-bit对称量化和LZMA2编码。

## 📚 数据集

- 测试视频（6.08 MiB，含音频轨道，用于训练和评估）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| 视频PSNR (dB) | 测试视频 | H.264 (未给出具体值) | **28.72** | 未与H.264直接比较 |
| 视频SSIM | 测试视频 | 未给出 | **0.75** | — |
| 音频PSNR (dB) | 测试视频 | MP3 (未给出具体值) | **24.18** | — |
| 音频对数谱距离 (dB) | 测试视频 | 未给出 | **10.69** | — |
| 压缩比 | 测试视频 | 原始大小9.05 MiB | **2.33 MiB (2.61x)** | — |

在单个6.08 MiB测试视频上，量化学生网络达到视频PSNR 28.72 dB、SSIM 0.75，音频PSNR 24.18 dB、对数谱距离10.69 dB。从9.05 MiB压缩至2.33 MiB，压缩比2.61。位宽扫描显示16-bit量化后质量饱和。与H.264、HEVC、MP3相比，方法性能不足，但提供了浏览器端原型。

## 🎯 结论与影响

本文证明用单个SIREN网络联合编码视频和音频在技术上是可行的，但压缩效率和重建质量远低于传统编解码器。该方向后续研究需解决网络容量与压缩比的平衡，工业落地前景有限。

## ⚠️ 局限与未解决问题

仅在单个小视频上测试，缺乏标准数据集评估；未与H.264/HEVC/MP3进行公平的率失真比较；未报告推理时间或计算复杂度；知识蒸馏和量化策略简单，压缩比低；音频质量指标（PSNR、LSD）不足以全面评估感知质量。

---

<div class="paper-footer"><span>评分：5.5</span><span>原始：5.5</span><a href="/audio-paper-daily/posts/2026-07-20/">← 返回 2026-07-20 速递</a></div>
