---
title: "Signed Wasserstein distance for room impulse response comparison"
date: 2026-10-24T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#房间冲激响应生成"]
summary: "提出基于最优传输的带符号 Wasserstein 距离，用于比较房间冲激响应，并在可微镜像源模型中做房间参数优化。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#房间冲激响应生成</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#声学模拟</span> <span class="tag-pill tag-pill-soft">#最优传输</span> <span class="tag-pill tag-pill-soft">#可微声学</span> <span class="tag-pill tag-pill-soft">#评价指标</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2610.31596</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-10-22</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2610.31596" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2610.31596" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出基于最优传输的带符号 Wasserstein 距离，用于比较房间冲激响应，并在可微镜像源模型中做房间参数优化。
</div>

## 👥 作者与机构

**Linda Fabiani** ¹ · Sebastian J. Schlecht · Filip Elvander

**机构**：瑞典皇家理工学院

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合做 RIR 生成、可微声学模拟与声学参数反演的读者。建议通读，重点看 §3 的 signed Wasserstein 定义与 §4 的扰动实验设计，表 1/2 的基线对比与可微优化实验是核心证据；若只关心指标可先看距离定义与几何评估部分。

## 🌍 研究背景

RIR 是稀疏、快速变化且带符号的信号，由房间反射与相位关系复杂叠加而成。此前 RIR 相似度普遍沿用逐点指标（MSE、SNR、EDC 相关等），对微小时间偏移敏感，且作为损失函数时优化曲面差、梯度信息弱。本文要解决的是：为 RIR 设计一个显式考虑其冲击结构、对时移鲁棒、且可用于可微优化的距离度量。

## 💡 核心创新

1. 将 signed Wasserstein 距离引入 RIR 比较，显式处理正负号与稀疏结构
2. 用最优传输按分布位移而非逐点对应度量相似度
3. 在可微 Image-Source 模型中把该距离作为损失做房间参数优化

## 🏗️ 模型架构

输入为两段 RIR 时序信号，先将其视为带符号的测度（正负质量分别处理），构造代价矩阵后求解最优传输问题，得到 signed Wasserstein 距离；该距离对时间平移具有结构感知的鲁棒性。摘要未给出具体网络主干或参数量，方法核心是距离算子本身，并被嵌入可微 Image-Source 模型作为优化目标，通过该距离对房间几何参数求梯度完成参数估计。

## 📚 数据集

- 仿真 RIR（房间参数扰动研究，评估）
- 可微 Image-Source 模型生成的 RIR（房间参数优化，评估）

## 📊 实验结果

摘要仅给出定性结论：在房间参数扰动研究中，signed Wasserstein 距离相较常用音频基线指标在几何评估任务上更有优势，并在可微 Image-Source 模型的房间参数优化中表现有前景。摘要未报告 SI-SDR、PESQ 等具体数值，也无消融或效率数据，需查阅正文表格确认。

## 🎯 结论与影响

最强结论是：面向 RIR 的相似度应按分布位移而非逐点误差来度量，signed Wasserstein 在几何评估与可微参数优化上均优于常规指标。这为 RIR 生成模型的训练损失与声学参数反演提供了新选择，对可微声学模拟与房间声学数据管线有潜在落地价值。

## ⚠️ 局限与未解决问题

摘要未给出定量结果与基线数值，缺少与更多距离（如 OT 变体、谱距离）的系统对比；最优传输求解的计算开销与推理延迟未报告；实验限于仿真 RIR，真实测量 RIR 上的泛化性未知；可微优化部分仅展示单场景，缺少收敛性与鲁棒性分析。

---

<div class="paper-footer"><span>评分：7.2</span><span>原始：7.2</span><a href="/audio-paper-daily/posts/2026-10-24/">← 返回 2026-10-24 速递</a></div>
