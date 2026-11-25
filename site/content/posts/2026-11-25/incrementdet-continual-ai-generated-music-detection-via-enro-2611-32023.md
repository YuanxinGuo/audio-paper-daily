---
title: "IncrementDET: Continual AI-Generated Music Detection via Enrollment"
date: 2026-11-25T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#音频生成检测"]
summary: "提出IncrementDET，用逐生成器线性探针（needle）加Sidak校正实现持续AI音乐检测，并构建EvoMusicFake-17K基准。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero">
<div class="hero-score">
<div class="score-num">6.8</div>
<div class="score-stars">★★★☆☆</div>
<div class="score-tier">中等</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#音频生成检测</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#AI生成音乐检测</span> <span class="tag-pill tag-pill-soft">#持续学习</span> <span class="tag-pill tag-pill-soft">#音乐信息检索</span> <span class="tag-pill tag-pill-soft">#异常检测</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2611.32023</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-11-24</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2611.32023" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2611.32023" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出IncrementDET，用逐生成器线性探针（needle）加Sidak校正实现持续AI音乐检测，并构建EvoMusicFake-17K基准。
</div>

## 👥 作者与机构

**Runbao Du** ¹ · Wei Li · Qile He

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合做AI生成内容检测、持续学习与音乐信息检索的研究者阅读。建议重点看§3的needle设计与Sidak校正推导，以及§4基准协议和表2的更新成本对比；若关注落地，可先看与SpecTTTra的少样本对比实验。

## 🌍 研究背景

AI生成音乐在流媒体平台泛滥，固定生成器集合上训练的检测器面对新生成器泛化差。现有SOTA如SpecTTTra走通用检测器路线，更新需大量数据与算力，且易遗忘旧生成器。本文要解决的是：新生成器频繁出现时，如何以低更新成本持续扩展检测能力并保持旧类性能。

## 💡 核心创新

1. 逐生成器训练线性分类器needle，与固定人类参考集对比
2. 新生成器仅新增needle，旧needle冻结不变
3. Sidak多重比较校正控制整体假阳性率
4. 定义持续AI音乐检测任务并给出基准协议
5. 构建EvoMusicFake-17K六生成器四平台数据集

## 🏗️ 模型架构

输入为音乐音频特征（摘要未详述前端特征提取器），核心不是端到端深度主干，而是对每个生成器训练一个线性分类器needle，将该生成器样本与固定人类参考曲目集合分离。推理时多个needle并行，用Sidak校正调整各needle阈值以维持整体假阳性率目标。新增生成器只追加一个needle，旧needle参数冻结，更新成本仅为单线性分类器训练。

## 📚 数据集

- EvoMusicFake-17K（训练与评估，含六个近期生成器与四个真人音乐平台的器乐音乐）

## 📊 实验结果

摘要仅给出定性结论：相比SOTA通用检测器SpecTTTra，IncrementDET用少量样本即可更准确学习新生成器，对未见生成器泛化更好，对已学生成器性能保持更佳，且更新成本显著更低。摘要未给出具体指标数值，无法列表量化对比。

## 🎯 结论与影响

最强结论是冻结旧needle、仅追加新线性分类器的enrollment机制可在低更新成本下兼顾新生成器学习与旧类保持。该思路对持续学习式生成内容检测有参考价值，并可迁移到生成图像与视频检测；工业上利于平台低成本增量上线新检测能力。

## ⚠️ 局限与未解决问题

摘要未报告推理延迟与needle数量增长后的开销；线性分类器依赖前端特征质量，特征提取器是否冻结未说明；基准仅六个生成器、单一音乐类型（器乐），跨类型与跨语言泛化未知；缺少与更多持续学习基线（如EWC、replay）的对比。

---

<div class="paper-footer"><span>评分：6.8</span><span>原始：6.8</span><a href="/audio-paper-daily/posts/2026-11-25/">← 返回 2026-11-25 速递</a></div>
