---
title: "MiDashengLM-Spatial: Unifying General Audio Understanding and Spatial Awareness"
date: 2026-10-09T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#双耳音频"]
summary: "小米提出首个开源统一音频语言模型 MiDashengLM-Spatial，通过 Spatial-Dasheng 编码器与语义-空间分层条件模块，同时支持通用音频理解与空间感知。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero hero-focus">
<div class="hero-score">
<div class="score-num">8.5</div>
<div class="score-stars">★★★★☆</div>
<div class="score-tier">前25%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#双耳音频</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#音频语言模型</span> <span class="tag-pill tag-pill-soft">#声源定位与检测</span> <span class="tag-pill tag-pill-soft">#空间音频</span> <span class="tag-pill tag-pill-soft">#多模态</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2610.11156</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-10-09</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
<div class="meta-row"><span class="meta-key">⭐</span><span class="meta-val focus-badge">本站重点关注领域 · 评分 +1</span></div>
</div>
</div>

<div class="opensource-banner"><div class="oc-headline"><span class="oc-pulse"></span><span class="oc-title">本论文已开源</span><span class="oc-hint">点击下方卡片直达对应资源</span></div><div class="oc-grid"><a class="oc-chip oc-chip-code" href="https://github.com/xiaomi-research/midashenglm-spatial" target="_blank" rel="noopener"><span class="oc-icon">💻</span><span class="oc-text"><span class="oc-label">代码仓库</span><span class="oc-sub">xiaomi-research/midashenglm-spatial</span></span></a><a class="oc-chip oc-chip-hf" href="https://huggingface.co/mispeech/midashenglm-spatial" target="_blank" rel="noopener"><span class="oc-icon">🤗</span><span class="oc-text"><span class="oc-label">HuggingFace</span><span class="oc-sub">🤗 mispeech/midashenglm-spatial</span></span></a></div></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2610.11156" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2610.11156" target="_blank" rel="noopener">📑 PDF</a><a class="rsrc rsrc-code" href="https://github.com/xiaomi-research/midashenglm-spatial" target="_blank" rel="noopener">💻 代码</a><a class="rsrc rsrc-hf" href="https://huggingface.co/mispeech/midashenglm-spatial" target="_blank" rel="noopener">🤗 HuggingFace</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>小米提出首个开源统一音频语言模型 MiDashengLM-Spatial，通过 Spatial-Dasheng 编码器与语义-空间分层条件模块，同时支持通用音频理解与空间感知。
</div>

## 👥 作者与机构

**Jinbo Hu** ¹ · Hang Su · Lichun Fan · Heinrich Dinkel · Gang Li · Zhanchen Dai · Yiru Zhang · Chang Liu · … 等 5 人

**机构**：小米

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合做 LALM、空间音频、SELD 的研究者与工程团队阅读。建议通读，重点看 §3 的 Spatial-Dasheng 编码器与语义到空间分层条件模块设计，以及 §4 的数据合成管线；实验部分先看空间理解 benchmark 表与单声道通用 benchmark 对比表，确认空间能力是否以牺牲通用理解为代价。

## 🌍 研究背景

大型音频语言模型（LALM）在通用音频理解上已取得不错成绩，但主流模型多为单声道输入，丢弃了通道间线索，无法进行空间感知。已有的空间音频语言模型则专为空间任务定制，无法复用单声道 LALM 的通用理解能力。本文要解决的核心问题是：能否在单一架构内同时保留通用音频理解与空间感知，而不牺牲任一方。

## 💡 核心创新

1. 提出 Spatial-Dasheng 空间音频编码器，扩展 MiDashengLM 支持双耳输入
2. 设计语义到空间的分层条件模块，多深度注入中间语义表征
3. 构建大规模空间声学场景合成管线，生成场景级空间描述与 QA 对
4. 首个开源端到端统一通用理解与空间感知的音频语言模型

## 🏗️ 模型架构

输入为双耳/多通道音频，经 Spatial-Dasheng 空间编码器提取空间特征；同时保留原 MiDashengLM 的语义编码通路。关键模块为分层语义到空间条件模块，在多个深度将中间语义表征注入空间分支，使空间分支获得语义先验而不破坏原语义路径。两路特征融合后送入语言模型解码，输出文本回答，支持通用音频理解与空间问答两类任务。

## 📚 数据集

- 合成空间声学场景（训练，含场景级空间描述与 QA 对）
- 真实场景 SELD 数据集（评估 Spatial-Dasheng）
- 空间理解与推理 benchmark（评估 MiDashengLM-Spatial）
- 单声道通用音频 benchmark（评估通用理解保持情况）

## 📊 实验结果

摘要未给出具体数值指标，仅定性说明：Spatial-Dasheng 在真实场景声事件定位与检测上表现强；MiDashengLM-Spatial 在空间理解与推理 benchmark 上显著优于现有 LALM；在多种单声道 benchmark 上与 8B 级 SOTA LALM 保持竞争力，说明空间感知的引入未损害通用音频理解。

## 🎯 结论与影响

最强结论是空间感知能力可在不牺牲通用音频理解的前提下被统一模型获得。这为后续 LALM 的多模态空间扩展提供了可复用架构与数据合成范式，也意味着工业界可在同一模型上同时部署通用音频问答与空间感知能力，降低多模型维护成本。

## ⚠️ 局限与未解决问题

摘要未给出具体指标与消融，无法判断语义到空间条件模块各深度的贡献；数据合成管线可能引入仿真到真实的域偏差；未报告推理延迟与参数量；与专用 SELD 方法的对比细节缺失。

## 🔗 开源资源

- **代码**：<https://github.com/xiaomi-research/midashenglm-spatial>
- **HuggingFace**：<https://huggingface.co/mispeech/midashenglm-spatial>

---

<div class="paper-footer"><span>评分：8.5</span><span>原始：7.5</span><span>+1 重点领域加权</span><a href="/audio-paper-daily/posts/2026-10-09/">← 返回 2026-10-09 速递</a></div>
