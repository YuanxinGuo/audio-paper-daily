---
title: "DuSpaR: Dual-State Sparsifying Recurrent Unit with Feedback Modulation for Compute-Efficient Speech Processing"
date: 2026-10-01T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#语音增强"]
summary: "提出双状态稀疏循环单元 DuSpaR，通过 ReLU 稀疏化与动态跳零，在 KWS/SLU/SE 三任务上以更少算力达到或超过 GRU。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero hero-focus">
<div class="hero-score">
<div class="score-num">8.2</div>
<div class="score-stars">★★★★☆</div>
<div class="score-tier">前25%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#语音增强</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#语音增强</span> <span class="tag-pill tag-pill-soft">#关键词识别</span> <span class="tag-pill tag-pill-soft">#口语理解</span> <span class="tag-pill tag-pill-soft">#高效推理</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2609.39237</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-10-01</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
<div class="meta-row"><span class="meta-key">⭐</span><span class="meta-val focus-badge">本站重点关注领域 · 评分 +1</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2609.39237" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2609.39237" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出双状态稀疏循环单元 DuSpaR，通过 ReLU 稀疏化与动态跳零，在 KWS/SLU/SE 三任务上以更少算力达到或超过 GRU。
</div>

## 👥 作者与机构

**Zixiao Li** ¹ · Sheng Zhou · Longbiao Cheng · Shih-Chii Liu

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合做边缘端语音模型压缩、稀疏循环网络与高效推理的研究者与工程同学。建议通读，重点看 §3 双状态反馈调制与稀疏跳零机制、以及 KWS/SLU/SE 三任务的算力-精度对比表；若只关心语音增强，可先看 VBD 实验与消融中 dual-state 带来的 3.1~11.3 倍有效算力下降。

## 🌍 研究背景

边缘设备上的语音模型长期受限于算力与权重访存，GRU/LSTM 类循环结构虽参数少但矩阵-向量乘法密集。已有稀疏感知循环模型（如 skip-RNN、结构化稀疏单元）尝试用门控或阈值跳过零激活，但多为单状态循环，状态调制能力弱，稀疏率与精度难以兼顾。本文要解决的是：在参数量相当的前提下，如何用更少的 MAC 与权重读取，同时不牺牲 KWS/SLU 精度与 SE 质量。

## 💡 核心创新

1. 双状态循环反馈调制输入向量，增强状态表达能力
2. 用 ReLU 稀疏化矩阵-向量乘的输入操作数
3. 动态跳过零项，节省 MAC 与权重访存
4. 在 KWS/SLU/SE 三任务统一验证稀疏循环单元

## 🏗️ 模型架构

输入语音特征先经前端（KWS/SLU 用帧级声学特征，SE 用幅度谱）送入 DuSpaR 堆叠层。每个 DuSpaR cell 维护两个循环状态，通过状态反馈回路对输入向量做逐元素调制；调制后的输入经 ReLU 产生稀疏激活，矩阵-向量乘法时动态跳过零项，从而减少 MAC 与权重读取。主干为若干 DuSpaR 层加任务头：KWS/SLU 接分类头，SE 接掩蔽/重建头输出增强谱。摘要未给出具体参数量，仅强调与 GRU 在相似参数量下对比。

## 📚 数据集

- Google Speech Commands（KWS 训练/评估）
- Fluent Speech Commands（SLU 训练/评估）
- Voice Bank + Demand（SE 训练/评估）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| 计算量（相对 GRU） | Google Speech Commands | GRU 100% | **49.0%** | -51.0% |
| 计算量（相对 GRU） | Fluent Speech Commands | GRU 100% | **31.6%** | -68.4% |
| 计算量（相对 GRU） | Voice Bank + Demand | GRU 100% | **49.9%** | -50.1% |
| 有效算力（相对单状态循环） | 消融（三任务） | 单状态循环 1x | **1/3.1~1/11.3** | 降低 3.1~11.3 倍 |

摘要报告：在相似参数量下，DuSpaR 在 KWS 与 SLU 上分别比 GRU 少 51.0% 与 68.4% 计算量且精度更高；在 SE 上少 50.1% 计算量而质量相当。在可比算力与多种模型尺寸下，其 KWS/SLU 精度与 SE 质量优于其他稀疏感知循环模型。消融显示双状态循环相比单状态基线在任务性能相近时把有效算力降低 3.1~11.3 倍。摘要未给出 SI-SDR/PESQ 等具体数值。

## 🎯 结论与影响

最强结论是：双状态稀疏循环单元能在参数量相当的情况下，以约一半甚至更少的计算量匹配或超过 GRU 的多任务表现。这为边缘端语音前端与轻量识别/增强模型提供了可替换的循环模块，后续可探索与 Conformer、BSRNN 等主干的混合设计；工业上有利于在 MCU/手机端降低推理功耗与内存带宽。

## ⚠️ 局限与未解决问题

摘要只给相对计算量，未报绝对 MAC、推理延迟、内存占用与能耗；SE 仅用 VBD 一个数据集，未在 DNS-Challenge 或含混响数据上验证；缺少与 SEPFormer、BSRNN 等强增强基线的直接对比；稀疏跳零的实际硬件加速收益依赖运行时支持，摘要未说明。

---

<div class="paper-footer"><span>评分：8.2</span><span>原始：7.2</span><span>+1 重点领域加权</span><a href="/audio-paper-daily/posts/2026-10-01/">← 返回 2026-10-01 速递</a></div>
