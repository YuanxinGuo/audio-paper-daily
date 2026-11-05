---
title: "The Hearpiece Database of Binaural Room Impulse Responses and Driver Responses on KEMAR"
date: 2026-11-05T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#双耳音频"]
summary: "发布 KEMAR 人工头配 Hearpiece 入耳阵列的 BRIR 与驱动器响应数据库，覆盖多房间、多朝向、多次佩戴。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero hero-focus">
<div class="hero-score">
<div class="score-num">7.8</div>
<div class="score-stars">★★★★☆</div>
<div class="score-tier">前50%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#双耳音频</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#双耳音频</span> <span class="tag-pill tag-pill-soft">#房间冲激响应</span> <span class="tag-pill tag-pill-soft">#助听器信号处理</span> <span class="tag-pill tag-pill-soft">#数据集</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2611.06345</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-11-05</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
<div class="meta-row"><span class="meta-key">⭐</span><span class="meta-val focus-badge">本站重点关注领域 · 评分 +1</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2611.06345" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2611.06345" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>发布 KEMAR 人工头配 Hearpiece 入耳阵列的 BRIR 与驱动器响应数据库，覆盖多房间、多朝向、多次佩戴。
</div>

## 👥 作者与机构

**Tong Xiao** ¹ · Reinhild Roden · Matthias Blau · Simon Doclo

**机构**：Carl von Ossietzky Universität Oldenburg

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合做双耳/助听器阵列处理、空间滤波与去混响的研究者。值得通读，但重点看 §2 测量设置与 §4 数据组织，确认房间条件、插入次数与朝向网格是否匹配自己的实验协议；再对照 MATLAB 加载脚本核对通道定义与 loopback 校准方式。

## 🌍 研究背景

双耳与助听器信号处理（空间滤波、去混响、主动降噪、反馈消除）长期依赖少量公开 BRIR 库，如 MIT KEMAR、CIPIC HRTF 及部分助听器阵列数据集。这些资源多缺少入耳多麦克风/多受话器配置、缺少同一配置下多次独立佩戴的重复测量，也少有同时提供中心麦克风 RIR 与系统 loopback 的完整链路标定，导致跨研究复现与阵列算法评估受限。本文针对该缺口，系统采集并公开一套可复现的测量数据库。

## 💡 核心创新

1. 在 KEMAR 上以 Hearpiece 入耳多麦多受话器设备采集 BRIR 与驱动器响应
2. 两种 Hearpiece 配置 × 三次独立佩戴，支持佩戴差异统计
3. 三种房间条件 × 24 个水平声源方向的空间覆盖
4. 附带中心麦克风 RIR 与录放链路 loopback 冲激响应用于标定

## 🏗️ 模型架构

数据库构建流程：在 KEMAR 人工头上佩戴 Hearpiece（多麦克风、多受话器入耳研究设备），于三种房间条件下按 24 个水平方位角播放激励信号，同步采集双耳 BRIR、Hearpiece 各驱动器响应、中心麦克风 RIR 以及播放-录制系统的 loopback 冲激响应；每种 Hearpiece 配置重复三次独立插入以捕捉佩戴位置差异。数据以 MATLAB 文件格式组织，配套加载脚本与文档，摘要未给出参数量等模型信息。

## 📚 数据集

- Hearpiece Database（自建，KEMAR 测量，含 BRIR 与驱动器响应，用于评估/研究）
- 三种房间条件（测量环境，非公开第三方数据集）

## 📊 实验结果

本文为数据库描述性论文，摘要未给出 SI-SDR、PESQ、WER 等定量指标，也未与基线系统对比，因此无法列出结果表。可确认的量化信息为数据规模：2 种 Hearpiece 配置、3 种房间条件、每配置 3 次独立插入、24 个水平声源方向，另含中心麦克风 RIR 与 loopback 响应。

## 🎯 结论与影响

最强结论是提供了一套带重复佩戴与完整链路标定的 KEMAR+Hearpiece 双耳响应数据库，可直接支撑双耳与助听器阵列算法的可复现评测。对后续研究，它可作为空间滤波、去混响、反馈消除与降噪方法的统一测试床；对工业落地，有助于助听器与入耳设备厂商在真实佩戴差异下评估算法鲁棒性。

## ⚠️ 局限与未解决问题

仅水平面 24 方向，未覆盖仰角与近场；仅 KEMAR 单个人工头，个体差异有限；三种房间条件规模偏小。作为数据库论文缺少下游任务基线实验（如波束成形或去混响的 benchmark 结果），也未报告测量信噪比与重复性统计指标，使用者需自行验证数据质量。

## 🔗 开源资源

- **数据集**：<https://doi.org/10.5281/zenodo.23667308>

---

<div class="paper-footer"><span>评分：7.8</span><span>原始：6.8</span><span>+1 重点领域加权</span><a href="/audio-paper-daily/posts/2026-11-05/">← 返回 2026-11-05 速递</a></div>
