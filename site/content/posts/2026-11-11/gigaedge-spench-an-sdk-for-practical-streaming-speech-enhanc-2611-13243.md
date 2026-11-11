---
title: "GigaEdge Spench: An SDK for Practical Streaming Speech Enhancement"
date: 2026-11-11T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#语音增强"]
summary: "开源流式语音增强SDK，集成降噪、归一化、重采样与回声消除，支持CPU/移动端/浏览器多平台部署。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#语音增强</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#语音增强</span> <span class="tag-pill tag-pill-soft">#流式推理</span> <span class="tag-pill tag-pill-soft">#跨平台部署</span> <span class="tag-pill tag-pill-soft">#实时系统</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2611.13243</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-11-11</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
<div class="meta-row"><span class="meta-key">⭐</span><span class="meta-val focus-badge">本站重点关注领域 · 评分 +1</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2611.13243" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2611.13243" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>开源流式语音增强SDK，集成降噪、归一化、重采样与回声消除，支持CPU/移动端/浏览器多平台部署。
</div>

## 👥 作者与机构

**Artem Sokolov** ¹ · Artem Khaidarov · Yana Lysova · Alexander Gladkikh · Vitaliy Yulis

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合做语音增强工程落地、端侧部署的工程师与系统方向研究者阅读。若关注算法创新可略读；建议重点看模型与执行环境对比实验部分及多流并发测试，了解chunk size与推理成本权衡。

## 🌍 研究背景

流式语音增强在端侧部署已有RNNoise等轻量方案，但缺乏统一的可配置跨平台SDK。现有工作多聚焦单一模型或单一平台，工程集成、多流共享、chunk策略对实时性的影响缺少系统研究。本文构建开源SDK，整合神经降噪、归一化、重采样与AEC模块，并系统评估模型选择、chunk大小与执行环境对处理成本的影响。

## 💡 核心创新

1. 统一C++核心支持ONNX Runtime与TFLite多后端
2. 多流共享模型资源与连续帧合并单次推理
3. 可组合的降噪/归一化/重采样/AEC处理链
4. 跨原生、Android/iOS与WebAssembly部署

## 🏗️ 模型架构

SDK以共享C++核心为骨架，通过ONNX Runtime与TensorFlow Lite原生接口运行神经网络，向上封装Android/iOS SDK与WebAssembly。处理链由神经降噪、归一化、动态处理、采样率转换与AEC模块可配置组合。发布模型包括8kHz INT8降噪器及48kHz FP32判别式与混合模型。多流上下文共享模型资源，同一流连续帧可合并为单次推理调用。

## 📚 数据集

- EARS-WHAM v2（评估）

## 📊 实验结果

摘要未给出具体SI-SDR/PESQ数值，仅说明在EARS-WHAM v2上与RNNoise、DPDFNet2对比质量与处理成本。所有原生与Web配置均快于实时，但较大chunk需更多时间收集输入；并测量了单CPU上共享模型可并发处理的流数。

## 🎯 结论与影响

本文最强结论是提供了一套可配置、跨平台且快于实时的流式语音增强部署系统。其工程价值在于统一多后端与多流共享机制，对端侧语音增强落地有直接参考意义，但算法层面贡献有限。

## ⚠️ 局限与未解决问题

摘要未报告SI-SDR/PESQ等客观指标具体数值，对比仅限RNNoise与DPDFNet2，缺少消融与延迟细节；AEC仅部分平台支持，模型规模与内存占用未说明。

---

<div class="paper-footer"><span>评分：7.8</span><span>原始：6.8</span><span>+1 重点领域加权</span><a href="/audio-paper-daily/posts/2026-11-11/">← 返回 2026-11-11 速递</a></div>
