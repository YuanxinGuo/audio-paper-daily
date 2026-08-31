---
title: "An Attention-Assisted AI Model for Real-Time Underwater Sound Speed Estimation Leveraging Remote Sensing Sea Surface Temperature Data"
date: 2026-08-31T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#声速剖面估计"]
summary: "提出自注意力嵌入的多模态融合CNN，利用遥感海表温度和历史声速剖面估计实时水下声速分布，精度和稳定性优于现有方法。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero">
<div class="hero-score">
<div class="score-num">6.8</div>
<div class="score-stars">★★★☆☆</div>
<div class="score-tier">前50%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#声速剖面估计</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#多模态融合</span> <span class="tag-pill tag-pill-soft">#注意力机制</span> <span class="tag-pill tag-pill-soft">#遥感数据</span> <span class="tag-pill tag-pill-soft">#实时估计</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2502.12817</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-08-31</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2502.12817" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2502.12817" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出自注意力嵌入的多模态融合CNN，利用遥感海表温度和历史声速剖面估计实时水下声速分布，精度和稳定性优于现有方法。
</div>

## 👥 作者与机构

**Pengfei Wu** ¹ · Wei Huang · Yujie Shi · Feng Yin · Hao Zhang

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合水声工程、海洋遥感及音频信号处理交叉领域的研究者。建议重点阅读方法部分（SA-MDF-CNN结构）和实验对比（表2、图5）。若关注实时性，可查看推理时间分析。

## 🌍 研究背景

水下声速分布对通信和定位至关重要，但传统直接测量和声学反演方法需要现场部署，难以实时。现有方法依赖现场数据，无法快速构建声速场。本文利用遥感海表温度（SST）与历史声速剖面（SSP）的关系，通过深度学习方法实现无需现场测量的实时估计，解决实时性和部署难题。

## 💡 核心创新

1. 自注意力嵌入多模态融合CNN（SA-MDF-CNN）
2. 融合SST、历史SSP主成分和空间坐标
3. CNN提取局部特征，注意力机制提取全局相关性
4. 实现实时声速剖面估计，无需现场测量

## 🏗️ 模型架构

输入为遥感海表温度（SST）数据、历史SSP主成分和空间坐标，经预处理后分别提取特征。主干网络为CNN，嵌入自注意力模块以捕获全局依赖。多模态特征融合后，输出预测的声速剖面。模型参数量未提及。

## 📚 数据集

- 历史声速剖面数据（训练/评估，具体规模未提及）
- 遥感海表温度数据（训练/评估，具体来源未提及）

## 📊 实验结果

摘要指出所提方法在精度和稳定性上优于现有先进技术，误差率更低，抗干扰能力更强，但未提供具体数值。

## 🎯 结论与影响

本文提出的SA-MDF-CNN实现了基于遥感SST的实时声速剖面估计，避免了现场测量，精度和稳定性优于现有方法。该研究为水下声速场实时构建提供了新思路，有望推动水下通信和定位系统的实时应用。

## ⚠️ 局限与未解决问题

摘要未提供具体实验数据，缺乏与现有方法的定量对比。未讨论模型在不同海域的泛化能力，以及SST数据分辨率对估计精度的影响。未提及推理延迟和计算资源需求。

---

<div class="paper-footer"><span>评分：6.8</span><span>原始：6.8</span><a href="/audio-paper-daily/posts/2026-08-31/">← 返回 2026-08-31 速递</a></div>
