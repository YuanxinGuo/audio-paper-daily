---
title: "SpikCTU: A Compact Spiking Network with Adaptive Recurrent Computation for Speech Command Recognition"
date: 2026-10-21T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#语音识别"]
summary: "提出紧凑脉冲网络SpikCTU，用共享连续思考单元做自适应循环计算，仅0.16-0.17M参数在语音命令识别上取得有竞争力精度。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#语音识别</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#脉冲神经网络</span> <span class="tag-pill tag-pill-soft">#语音命令识别</span> <span class="tag-pill tag-pill-soft">#自适应计算</span> <span class="tag-pill tag-pill-soft">#轻量化模型</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2610.14594</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-10-21</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner"><div class="oc-headline"><span class="oc-pulse"></span><span class="oc-title">本论文已开源</span><span class="oc-hint">点击下方卡片直达对应资源</span></div><div class="oc-grid"><a class="oc-chip oc-chip-code" href="https://github.com/Rivflyyy/spikctu" target="_blank" rel="noopener"><span class="oc-icon">💻</span><span class="oc-text"><span class="oc-label">代码仓库</span><span class="oc-sub">Rivflyyy/spikctu</span></span></a></div></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2610.14594" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2610.14594" target="_blank" rel="noopener">📑 PDF</a><a class="rsrc rsrc-code" href="https://github.com/Rivflyyy/spikctu" target="_blank" rel="noopener">💻 代码</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出紧凑脉冲网络SpikCTU，用共享连续思考单元做自适应循环计算，仅0.16-0.17M参数在语音命令识别上取得有竞争力精度。
</div>

## 👥 作者与机构

**Li Jin** ¹ · Jiang Wenbin · Chen Tao · Wen Fei

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合做轻量化KWS、SNN事件驱动计算的研究者阅读。值得通读，重点看§3的CTU循环更新机制与stage adapter设计，以及§4的early exit实验和轨迹分析。若只关心精度提升可只看表2与图3。

## 🌍 研究背景

语音命令识别（KWS）在边缘设备上要求极低功耗，SNN因事件驱动稀疏计算被视为候选方案。此前SNN-KWS工作（如基于LIF的卷积/循环SNN）多采用固定计算路径，对所有样本分配相同时间步与计算量，简单样本存在冗余计算，且推理过程中证据如何逐步累积缺乏可解释性。本文要解决的是：在极小参数量下引入自适应循环计算，让模型按样本难度动态决定计算步数，同时保持精度。

## 💡 核心创新

1. 混合脉冲嵌入模块，保留连续输入信息与脉冲特征共同构建固定时序记忆
2. 共享Continuous Thinking Unit (CTU)用脉冲与连续值派生的key反复读取记忆
3. 轻量stage adapter更新二值循环状态，实现逐步纠错
4. 固定基础预测加累积修正，支持学习式聚合与置信度早退

## 🏗️ 模型架构

输入语音特征先经混合脉冲嵌入模块，将连续特征与脉冲特征并行编码，构造一个固定的时序记忆张量。主干为共享参数的Continuous Thinking Unit（CTU），每一步用由脉冲和连续值共同生成的key对记忆做注意力式读取，并通过轻量stage adapter更新二值循环状态，形成多步循环推理。每步输出在固定base prediction上叠加累积修正，最终可学习聚合所有步或按置信度提前退出。整体参数量仅0.16–0.17M。

## 📚 数据集

- Google Speech Commands（训练/评估，摘要称三个语音命令识别基准之一）
- 另外两个语音命令识别基准（摘要未具名，评估）

## 📊 实验结果

摘要仅给出参数量0.16–0.17M与“competitive accuracy”的定性表述，未披露具体准确率数值与基线名称，故无法列表。作者报告early exit策略可在不损精度的前提下显著降低计算成本，并通过轨迹与注意力分析显示循环步能实现错误纠正、逐步细化预测。

## 🎯 结论与影响

最强结论是：极小参数（<0.2M）的SNN配合共享CTU自适应循环，可在语音命令识别上达到有竞争力精度，且早退可进一步省算力。这为SNN-KWS的自适应计算与可解释推理提供了一条轻量路线，对边缘端低功耗唤醒词部署有参考价值。

## ⚠️ 局限与未解决问题

摘要未给出具体准确率数字与对比基线，难以判断“competitive”的强度；三个基准中两个未具名；缺少与主流SNN-KWS及轻量CNN的完整对比表、推理延迟/能耗实测，早退阈值敏感性分析也未在摘要体现。

## 🔗 开源资源

- **代码**：<https://github.com/Rivflyyy/spikctu>

---

<div class="paper-footer"><span>评分：6.8</span><span>原始：6.8</span><a href="/audio-paper-daily/posts/2026-10-21/">← 返回 2026-10-21 速递</a></div>
