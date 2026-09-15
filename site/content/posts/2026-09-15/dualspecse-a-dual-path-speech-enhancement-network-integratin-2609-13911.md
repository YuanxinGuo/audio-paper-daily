---
title: "DualSpecSE: A Dual-Path Speech Enhancement Network Integrating Mel and Complex Spectrograms"
date: 2026-09-15T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#语音增强"]
summary: "提出双分支语音增强网络，Mel 分支供 ASR、复数谱分支做高保真重建，通过交互与融合模块交换信息。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#语音增强</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#语音增强</span> <span class="tag-pill tag-pill-soft">#ASR前端</span> <span class="tag-pill tag-pill-soft">#复数谱映射</span> <span class="tag-pill tag-pill-soft">#双分支架构</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2609.13911</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-09-15</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
<div class="meta-row"><span class="meta-key">⭐</span><span class="meta-val focus-badge">本站重点关注领域 · 评分 +1</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2609.13911" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2609.13911" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出双分支语音增强网络，Mel 分支供 ASR、复数谱分支做高保真重建，通过交互与融合模块交换信息。
</div>

## 👥 作者与机构

**Xingchen Li** ¹ · Ziqian Wang · Zikai Liu · Yike Zhu · Zihan Zhang · Longshuai Xiao · Lei Xie

**机构**：浙江大学

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合做 ASR 前端增强与复数谱映射的研究者阅读。建议重点看 §3 的交互模块与融合模块设计，以及表 2 中 Mel 域与复数域联合建模的消融；若关注 ASR 增益，先看 WER 对比表。整体值得通读，但需自行核对基线是否公平。

## 🌍 研究背景

语音增强长期以复数谱映射（如 BSRNN、DeepFilterNet）或 Mel 域映射（如 CleanMel）为主。复数域方法重建保真度高但 ASR 前端收益有限，Mel 域方法利于 ASR 却丢失相位与细粒度细节，且常依赖预训练声码器。本文试图在同一框架内同时优化 ASR 友好表示与波形重建质量，避免两阶段级联带来的误差累积。

## 💡 核心创新

1. 双分支并行建模 Mel 与复数谱，兼顾 ASR 与重建
2. 基于 CleanMel 的 cross-band / narrow-band 块构建主干
3. 引入交互模块实现两分支跨域信息交换
4. 融合模块联合输出增强 Mel 与复数谱，无需预训练声码器

## 🏗️ 模型架构

输入为含噪语音的 Mel 谱与复数谱两路特征。Mel 分支沿用 CleanMel 的 cross-band 与 narrow-band 块学习粗粒度声学表示，复数分支以同类块细化细粒度谱细节。两分支间插入交互模块做跨域特征对齐与信息传递，末端融合模块聚合双路表示，同时输出增强 Mel 谱（直接供 ASR）与增强复数谱（用于波形重建）。摘要未给出参数量与具体层数。

## 📊 实验结果

摘要仅称在语音保真度、感知质量与 ASR 性能上取得一致提升，未给出任何具体指标数值、测试集名称或基线对比结果，因此无法量化评估其增益幅度。需查阅正文确认 SI-SDR、PESQ、WER 等指标及消融实验是否充分。

## 🎯 结论与影响

最强结论是 Mel 与复数谱双分支联合建模可在不依赖预训练声码器的前提下同时改善 ASR 与重建质量。若结果可复现，该双域交互思路可被后续 ASR 前端与联合训练工作借鉴，对工业级远场识别与通话增强管线有潜在价值。

## ⚠️ 局限与未解决问题

摘要未报告任何定量结果、参数量与推理延迟，无法判断相对 CleanMel、BSRNN 等基线的实际优势；双分支结构可能带来计算开销翻倍；交互与融合模块缺少消融说明；未提及训练数据规模与跨域泛化。

---

<div class="paper-footer"><span>评分：7.8</span><span>原始：6.8</span><span>+1 重点领域加权</span><a href="/audio-paper-daily/posts/2026-09-15/">← 返回 2026-09-15 速递</a></div>
