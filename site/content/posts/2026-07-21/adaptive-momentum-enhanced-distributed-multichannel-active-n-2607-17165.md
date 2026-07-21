---
title: "Adaptive Momentum Enhanced Distributed Multichannel Active Noise Control for Faster Convergence under Communication Delays"
date: 2026-07-21T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#主动噪声控制"]
summary: "针对分布式多通道主动噪声控制在通信延迟下收敛慢的问题，提出自适应动量加速的AMAS-MGDFxLMS算法。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero">
<div class="hero-score">
<div class="score-num">6.5</div>
<div class="score-stars">★★★☆☆</div>
<div class="score-tier">前50%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#主动噪声控制</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#分布式多通道</span> <span class="tag-pill tag-pill-soft">#自适应动量</span> <span class="tag-pill tag-pill-soft">#通信延迟</span> <span class="tag-pill tag-pill-soft">#滤波参考LMS</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2607.17165</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-07-21</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2607.17165" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2607.17165" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>针对分布式多通道主动噪声控制在通信延迟下收敛慢的问题，提出自适应动量加速的AMAS-MGDFxLMS算法。
</div>

## 👥 作者与机构

**Junwei Ji** ¹ · Woon-Seng Gan · Boxiang Wang · Ziyi Yang · Haowen Li

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合主动噪声控制领域的研究者阅读。重点看§3的自适应动量设计及§4的仿真结果。若关注分布式ANC的延迟鲁棒性，建议通读。

## 🌍 研究背景

分布式多通道主动噪声控制（DMCANC）通过节点间信息交换实现全局降噪，但通信延迟会降低性能。现有ASSS-MGDFxLMS算法通过自适应步长提升鲁棒性，但步长减小导致收敛变慢。本文旨在加速收敛同时保持延迟下的稳定性。

## 💡 核心创新

1. 引入自适应动量项加速收敛
2. 利用余弦相似度动态调整动量参数
3. 在通信延迟下保持稳定性
4. 提出AMAS-MGDFxLMS算法

## 🏗️ 模型架构

基于分布式多通道ANC架构，每个节点采用滤波参考LMS（FxLMS）算法。核心改进是在ASSS-MGDFxLMS基础上增加自适应动量项：计算当前梯度与动量分量的余弦相似度，动态调整动量系数，当方向一致时增大动量加速，方向不一致时减小动量保持稳定。

## 📚 数据集

- 仿真数据（模拟声学路径和通信延迟，用于训练和评估）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| 收敛速度（迭代次数） | 仿真环境 | ASSS-MGDFxLMS（基准） | **AMAS-MGDFxLMS（更快收敛）** | 收敛速度提升（具体数值未给出） |

仿真结果表明，所提AMAS-MGDFxLMS算法在通信延迟下比ASSS-MGDFxLMS收敛更快，且保持稳定的降噪性能。但摘要未提供具体数值指标（如降噪量、收敛步数等）。

## 🎯 结论与影响

本文通过自适应动量机制有效加速了分布式ANC在通信延迟下的收敛，为实际部署提供了更高效的算法。后续可探索更复杂的动量调整策略或结合其他自适应方法。

## ⚠️ 局限与未解决问题

仅通过仿真验证，缺乏实际硬件实验；未报告具体降噪量或收敛步数等量化指标；未与更多基线（如其他动量方法）对比；未分析计算复杂度增加。

---

<div class="paper-footer"><span>评分：6.5</span><span>原始：6.5</span><a href="/audio-paper-daily/posts/2026-07-21/">← 返回 2026-07-21 速递</a></div>
