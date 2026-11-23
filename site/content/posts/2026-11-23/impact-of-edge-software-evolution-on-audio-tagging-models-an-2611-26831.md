---
title: "Impact of Edge Software Evolution on Audio Tagging Models: An Empirical Study on NVIDIA Jetson Orin Nano"
date: 2026-11-23T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#音频事件检测"]
summary: "在 Jetson Orin Nano 上对比 JetPack 6.2/7.2 两代软件栈对 PANNs、AST、PaSST 音频标记模型推理延迟与能耗的影响。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero">
<div class="hero-score">
<div class="score-num">6.0</div>
<div class="score-stars">★★★☆☆</div>
<div class="score-tier">中等</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#音频事件检测</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#边缘部署</span> <span class="tag-pill tag-pill-soft">#音频标记</span> <span class="tag-pill tag-pill-soft">#基准评测</span> <span class="tag-pill tag-pill-soft">#模型效率</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2611.26831</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-11-23</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2611.26831" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2611.26831" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>在 Jetson Orin Nano 上对比 JetPack 6.2/7.2 两代软件栈对 PANNs、AST、PaSST 音频标记模型推理延迟与能耗的影响。
</div>

## 👥 作者与机构

**Guillem Fustier-Castillo** ¹ · Ruben Ribes-Serrano · Jordi Grau-Haro · Marta Garcia-Ballesteros · Javier Naranjo-Alcazar

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合做边缘音频部署、模型选型与基准评测的工程师与实验研究者阅读。若关注算法创新可略读；建议重点看实验设置与结果表（不同 backend、power mode 下的延迟/能耗对比），以及关于 TensorRT 与卷积架构协同增益的分析段落，作为自建 benchmark 的参考模板。

## 🌍 研究背景

音频标记是机器听觉的基础任务，广泛用于智能监控、工业检测与环境感知。随着这类应用迁移到边缘平台，延迟、能耗、资源占用等部署指标与预测性能同等重要。然而现有研究几乎都在单一软件环境下评测模型，忽略了软件栈（驱动、CUDA、TensorRT 版本）演进对执行效率的潜在影响，可能导致模型选型结论失真。本文针对这一问题，系统考察软件生态更新如何改变主流音频标记架构在边缘设备上的部署表现。

## 💡 核心创新

1. 以 JetPack 6.2/7.2 两代软件栈做受控对比实验
2. 覆盖 CNN/ResNet/Transformer 三类架构（PANNs、AST、PaSST）
3. 同时测量延迟、能耗、CPU/GPU 利用率与内存占用
4. 跨多种推理 backend 与 power mode 做交叉评测

## 🏗️ 模型架构

本文为实证研究，不提出新网络。评测对象包括 PANNs 的 CNN 与 ResNet 变体、AST 与 PaSST：输入为 log-mel 频谱，PANNs 系列用卷积主干，AST/PaSST 用 Transformer 编码器并配合 patch embedding 与位置编码。所有模型部署在 NVIDIA Jetson Orin Nano 上，分别在 JetPack 6.2 与 7.2 环境下，通过不同推理 backend（含 TensorRT）与多种 power mode 运行，采集推理延迟、能耗、CPU/GPU 利用率与内存占用。

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| 推理延迟 / 能耗 | Jetson Orin Nano 实测 | JetPack 6.2 | **JetPack 7.2 + TensorRT** | 降低超过 50%（多个卷积架构） |

摘要给出的是相对趋势而非逐模型数值：JetPack 7.2 配合 TensorRT 时，多个卷积架构的延迟与能耗下降超过 50%，GPU 利用率显著上升；AST 仅有边际收益，PaSST 表现居中。这说明软件栈演进会改变不同架构之间的相对部署效率排序。摘要未提供具体延迟毫秒数、能耗焦耳值及消融细节。

## 🎯 结论与影响

最强结论是软件栈版本本身即可让卷积类音频标记模型的延迟与能耗减半，并可能颠覆架构间的效率排名。这提示后续边缘音频研究必须显式报告软件环境，否则基准结论不可复现、不可比。对工业落地而言，升级 JetPack 与启用 TensorRT 可能是比换模型更低成本的优化手段。

## ⚠️ 局限与未解决问题

仅覆盖单一硬件平台（Jetson Orin Nano）与 NVIDIA 生态，结论向其他 SoC 或非 CUDA 后端的外推性未知；未报告模型精度是否随软件栈变化，缺少多次运行的方差与统计显著性；数据集与输入配置细节在摘要中缺失，难以判断负载代表性。

---

<div class="paper-footer"><span>评分：6.0</span><span>原始：6.0</span><a href="/audio-paper-daily/posts/2026-11-23/">← 返回 2026-11-23 速递</a></div>
