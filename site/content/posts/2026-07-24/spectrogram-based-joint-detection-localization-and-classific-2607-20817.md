---
title: "Spectrogram-Based Joint Detection, Localization, and Classification of Events in Continuously Recorded IBR Waveforms"
date: 2026-07-24T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#事件检测"]
summary: "提出基于谱图的框架，在逆变器资源终端连续波形中联合检测、定位和分类事件。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#事件检测</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#电力系统</span> <span class="tag-pill tag-pill-soft">#谱图分析</span> <span class="tag-pill tag-pill-soft">#时频分析</span> <span class="tag-pill tag-pill-soft">#逆变器资源</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2607.20817</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-07-24</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2607.20817" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2607.20817" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出基于谱图的框架，在逆变器资源终端连续波形中联合检测、定位和分类事件。
</div>

## 👥 作者与机构

**Shivanshu Tripathi** ¹ · Maziar Raissi · Hamed Mohsenian-Rad

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合电力系统与信号处理交叉领域的研究者。可重点阅读第3节方法部分和第4节实验对比。建议关注谱图表示相对于原始波形的优势分析。

## 🌍 研究背景

连续高分辨率波形测量能捕捉快速电力系统动态，但需要自动化方法识别事件。现有方法多直接处理原始时域波形，难以有效提取瞬态和谐波特征。本文提出将事件检测转化为谱图图像上的时序目标检测问题，利用短时傅里叶变换将波形转为谱图张量，以提升检测性能。

## 💡 核心创新

1. 将事件检测重定义为谱图图像上的时序目标检测
2. 利用多通道谱图张量作为输入表示
3. 在真实IBR波形数据上验证单相和三相事件
4. 与原始波形基线方法进行系统对比

## 🏗️ 模型架构

输入为连续波形，经短时傅里叶变换得到每通道谱图，堆叠为张量。主干网络采用目标检测框架（如YOLO或Faster R-CNN，摘要未明确），输出事件类别、时间定位和位置信息。未提及参数量。

## 📚 数据集

- 真实IBR终端连续波形数据集（训练/评估，包含单相扰动和三相故障）

## 📊 实验结果

摘要未提供具体数值结果，仅定性说明谱图方法在事件检测、定位和分类上一致优于原始波形基线。

## 🎯 结论与影响

本文提出的谱图框架有效提升了逆变器资源波形中事件的联合检测、定位和分类性能。该工作为电力系统事件监测提供了新思路，谱图表示可推广至其他瞬态信号分析任务。工业上可用于实时电网监控。

## ⚠️ 局限与未解决问题

未报告具体指标（如精度、召回率、F1），缺乏与更多基线方法的对比。未讨论计算开销和实时性。数据集规模及事件类型有限，泛化性待验证。

---

<div class="paper-footer"><span>评分：6.5</span><span>原始：6.5</span><a href="/audio-paper-daily/posts/2026-07-24/">← 返回 2026-07-24 速递</a></div>
