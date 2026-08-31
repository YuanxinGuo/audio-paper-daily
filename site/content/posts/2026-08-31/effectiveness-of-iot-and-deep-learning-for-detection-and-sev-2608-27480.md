---
title: "Effectiveness of IoT and Deep Learning for Detection and Severity Assessment of Postelectrotermes militaris in Tea Plantations"
date: 2026-08-31T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#生物声学"]
summary: "提出基于IoT声学监测与CNN的茶树白蚁侵染检测与严重度评估框架，在真实茶园实现81.5%准确率。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#生物声学</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#IoT</span> <span class="tag-pill tag-pill-soft">#深度学习</span> <span class="tag-pill tag-pill-soft">#声学监测</span> <span class="tag-pill tag-pill-soft">#病虫害检测</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2608.27480</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-08-31</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2608.27480" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2608.27480" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出基于IoT声学监测与CNN的茶树白蚁侵染检测与严重度评估框架，在真实茶园实现81.5%准确率。
</div>

## 👥 作者与机构

**D. K. C. Senevirathna** ¹ · A. A. E. Nanayakkara · H. M. C. K. Kulathunga · J. K. D. P. Nadula · R. M. Mapatuna · Malithi Nawarathne · Jaliya L. Wijayaraja · P. D. Senanayake · … 等 2 人

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合从事农业声学监测、IoT与深度学习结合的研究者阅读。可重点看方法部分（§3）的声学特征提取与严重度模型，以及实验部分（§4）的现场验证。建议先看摘要和结论，再细读方法中的CNN架构与严重度加权模型。

## 🌍 研究背景

茶树种植园易受Upcountry Live Wood Termite (ULWT)侵害，若未及时发现可造成重大损失。传统检测依赖人工巡检，效率低且难以早期发现。近年来，声学监测结合机器学习在害虫检测中展现出潜力，但缺乏针对ULWT的专用框架。现有方法多限于实验室环境，未考虑现场噪声和严重度评估。本文旨在开发一种非侵入式、可部署的IoT声学监测系统，实现ULWT的早期检测和严重度量化，以支持精准防控。

## 💡 核心创新

1. IoT声学采集设备：Raspberry Pi+高灵敏度麦克风，非侵入式采集茶树树干音频
2. CNN分类器：基于Fourier频谱图训练，输出侵染概率
3. 加权严重度模型：结合CNN概率、平均声学幅度、5米内邻近侵染植株数
4. 地理空间映射：可视化侵染分布，支持管理决策

## 🏗️ 模型架构

输入为10秒茶树树干音频，经预处理（修剪、重采样、分段）后生成Fourier频谱图。频谱图输入CNN进行二分类（健康/侵染），输出侵染概率。同时计算平均声学幅度。严重度评估模型为加权组合：Severity = w1*CNN概率 + w2*平均幅度 + w3*邻近侵染植株数（5米内）。最后通过地理坐标进行空间映射，生成侵染分布图。

## 📚 数据集

- 自建数据集（训练/验证/测试：1600/200/200，共2000个10秒样本，1000健康/1000侵染）
- Kaggle公开数据集（Senevirathna et al. 2026）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| Accuracy | 自建测试集 | 未提及 | **81.5%** | — |
| Precision | 自建测试集 | 未提及 | **80.6%** | — |
| Recall | 自建测试集 | 未提及 | **83.0%** | — |
| F1-score | 自建测试集 | 未提及 | **81.8%** | — |
| ROC-AUC | 自建测试集 | 未提及 | **0.819** | — |

在真实茶园现场测试中，CNN分类器在测试集上达到81.5%准确率、80.6%精确率、83.0%召回率、81.8% F1和0.819 AUC。严重度评估模型结合概率、幅度和邻近侵染植株，输出定量严重度等级。地理空间映射成功可视化侵染分布，有助于识别高风险区域。但摘要未提供与基线方法的对比或消融实验。

## 🎯 结论与影响

本研究首次提出针对ULWT的IoT声学监测与深度学习框架，实现非侵入式检测和严重度评估，现场验证可行。该框架可支持茶园管理者精准定位高风险区域，优化巡检资源。未来可扩展至其他害虫监测，推动智慧农业中的声学AI应用。

## ⚠️ 局限与未解决问题

摘要未提及与现有方法的对比，缺乏消融实验验证各组件贡献。数据集仅来自单一茶园，可能缺乏泛化性。未报告推理延迟或设备成本，实际部署可行性待评估。严重度模型权重未说明如何确定，可能依赖经验。

---

<div class="paper-footer"><span>评分：6.8</span><span>原始：6.8</span><a href="/audio-paper-daily/posts/2026-08-31/">← 返回 2026-08-31 速递</a></div>
