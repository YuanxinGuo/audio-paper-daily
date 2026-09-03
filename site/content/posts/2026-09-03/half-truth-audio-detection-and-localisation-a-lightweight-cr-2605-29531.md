---
title: "Half-Truth Audio Detection and Localisation: A Lightweight Cross-Attentive Architecture and a Cross-Corpus Diagnostic Study"
date: 2026-09-03T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#音频取证"]
summary: "提出轻量级CAFNet模型，融合多特征联合分类半真语音并回归篡改边界，跨语料泛化呈能力依赖而非均匀。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero">
<div class="hero-score">
<div class="score-num">7.2</div>
<div class="score-stars">★★★★☆</div>
<div class="score-tier">前25%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#音频取证</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#半真语音检测</span> <span class="tag-pill tag-pill-soft">#篡改定位</span> <span class="tag-pill tag-pill-soft">#交叉注意力</span> <span class="tag-pill tag-pill-soft">#轻量级模型</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2605.29531</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-09-03</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2605.29531" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2605.29531" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出轻量级CAFNet模型，融合多特征联合分类半真语音并回归篡改边界，跨语料泛化呈能力依赖而非均匀。
</div>

## 👥 作者与机构

**S. Sutharya** ¹ · Remya K. Sasi

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合音频取证、伪造检测研究者。建议重点阅读第3节架构和第4节跨语料实验，特别是表2和表3。可先看摘要中的跨语料不对称性分析，再深入方法细节。

## 🌍 研究背景

现有深度伪造检测多针对全合成语音，但现实中更常见的是部分篡改（半真语音），即短合成片段拼接进真实语音。此类检测更具挑战性，且现有方法缺乏对篡改边界的定位能力。本文旨在解决半真语音的检测与定位问题，提出轻量级模型CAFNet，并首次在MLADDC基准上报告连续拼接边界定位结果。

## 💡 核心创新

1. 提出CAFNet，576K参数轻量级交叉注意力架构，融合MFCC、LFCC、Chroma-STFT特征。
2. 联合分类（真实/全假/半真）与回归篡改边界，实现14ms CPU延迟。
3. 通过消融发现交叉注意力融合是关键，而深层监督辅助头反而有害，移除后性能提升且方差降低。
4. 首次在MLADDC T2+T3上报告连续拼接边界定位结果（MAE 0.037s）。
5. 揭示跨语料迁移能力依赖而非均匀，强调跨语料评估应伴随架构决策。

## 🏗️ 模型架构

输入为MFCC、LFCC、Chroma-STFT三种特征，经特征融合后送入交叉注意力模块（CAFNet核心），主干为轻量级卷积网络，输出两个分支：分类头（三分类）和回归头（边界定位）。模型参数量576K，大小2.24MB，CPU延迟约14ms。

## 📚 数据集

- MLADDC T2+T3（训练与评估，含半真语音样本）
- HAD（零样本评估）
- PartialSpoof（零样本评估）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| 三元准确率 | MLADDC T2+T3 | 未提供 | **97.55%±0.69%** | — |
| 边界MAE | MLADDC T2+T3 | 未提供 | **0.037s** | — |
| 检测召回率 | HAD | 未提供 | **84.9%** | — |
| 三元分类正确率（半真） | HAD | 未提供 | **50.4%** | — |
| AUC | PartialSpoof | 未提供 | **0.5544** | — |

在MLADDC上取得97.55%三元准确率和0.037s边界MAE，首次报告连续定位结果。零样本测试显示HAD上检测召回84.9%，但半真分类仅50.4%；PartialSpoof上接近随机（AUC 0.5544）。消融表明移除深层监督头提升所有域内指标并降低方差，交叉注意力融合是关键。

## 🎯 结论与影响

CAFNet以轻量级架构实现半真语音检测与定位，域内性能优异，但跨语料泛化能力依赖具体任务和语料，并非均匀。研究强调跨语料评估应伴随架构决策，为音频取证领域提供了新基准和思考方向。

## ⚠️ 局限与未解决问题

跨语料泛化有限，尤其在PartialSpoof上接近随机，表明模型可能过拟合域内特征。未与现有深度伪造检测方法对比，缺乏基线。未报告推理延迟的详细硬件环境。未提供错误分析，如边界定位失败案例。

---

<div class="paper-footer"><span>评分：7.2</span><span>原始：7.2</span><a href="/audio-paper-daily/posts/2026-09-03/">← 返回 2026-09-03 速递</a></div>
