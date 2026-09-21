---
title: "Towards the Vision-Sound-Language-Action Paradigm: The HEAR Framework for Sound-Centric Manipulation"
date: 2026-09-21T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#音频处理"]
summary: "提出VSLA连续控制范式与HEAR框架，用流式音频历史器、音频世界模型与流匹配策略实现声音驱动的机器人操作。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero">
<div class="hero-score">
<div class="score-num">6.0</div>
<div class="score-stars">★★★☆☆</div>
<div class="score-tier">中等</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#音频处理</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#多模态</span> <span class="tag-pill tag-pill-soft">#机器人操作</span> <span class="tag-pill tag-pill-soft">#音频世界模型</span> <span class="tag-pill tag-pill-soft">#流式音频</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2603.16086</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-09-21</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner"><div class="oc-headline"><span class="oc-pulse"></span><span class="oc-title">本论文已开源</span><span class="oc-hint">点击下方卡片直达对应资源</span></div><div class="oc-grid"><a class="oc-chip oc-chip-proj" href="https://hear.irmv.top" target="_blank" rel="noopener"><span class="oc-icon">🌐</span><span class="oc-text"><span class="oc-label">项目主页</span><span class="oc-sub">hear.irmv.top</span></span></a><a class="oc-chip oc-chip-demo" href="https://hear.irmv.top" target="_blank" rel="noopener"><span class="oc-icon">🔊</span><span class="oc-text"><span class="oc-label">在线 Demo</span><span class="oc-sub">hear.irmv.top</span></span></a></div></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2603.16086" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2603.16086" target="_blank" rel="noopener">📑 PDF</a><a class="rsrc rsrc-proj" href="https://hear.irmv.top" target="_blank" rel="noopener">🌐 项目主页</a><a class="rsrc rsrc-demo" href="https://hear.irmv.top" target="_blank" rel="noopener">🔊 Demo</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出VSLA连续控制范式与HEAR框架，用流式音频历史器、音频世界模型与流匹配策略实现声音驱动的机器人操作。
</div>

## 👥 作者与机构

**Chang Nie** ¹ · Tianchen Deng · Guangming Wang · Zhe Liu · Hesheng Wang

**机构**：上海交通大学

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合做具身智能、多模态VLA、音频-动作联合建模的研究者。若关注语音/音频信号处理本身，本文相关性有限，可只看§3的Historizer与Advancer设计。建议先看HEAR-Bench的因果时序规则与表2的消融，判断流式音频上下文是否真带来增益。

## 🌍 研究背景

现有VLA模型虽开始引入音频，但多把声音当作执行前的静态提示，或仅处理人类语音，忽略执行过程中瞬态环境声提供的状态校验信息。动作分块与开环执行造成Blind Execution Interval，离散音频观测窗之间的事件易被漏掉。本文要解决实时、以声音为中心的机器人操作中，如何保持连续听觉感知并据此生成动作。

## 💡 核心创新

1. 形式化VSLA连续控制范式，含延迟决策环与流式音频
2. 流式Historizer维持跨执行间隙的因果音频上下文
3. Advancer作为音频世界模型预测近未来音频码
4. 流匹配Realizer生成平滑动作块
5. 构建OpenX-Sound预训练集与HEAR-Bench基准

## 🏗️ 模型架构

输入为视觉、流式音频、语言与本体感受。Historizer以因果方式压缩历史音频为紧凑上下文；Envisioner基于omni基础模型融合多感官输入进行推理；Advancer被建模为音频世界模型，通过预测近未来音频码学习时间动态；Realizer采用flow-matching策略生成平滑动作块。整体在延迟决策环下运行，输出为动作块序列。摘要未给出参数量。

## 📚 数据集

- OpenX-Sound（预训练，本文构建）
- HEAR-Bench（评估，首个声音中心操作基准，含严格因果时序规则）

## 📊 实验结果

摘要仅给出定性结论：稳健的声音中心操作需要因果持续性与显式时间学习，未提供SI-SDR、PESQ、成功率等具体数值，也未列出与基线的定量对比。因此无法从摘要判断相对现有VLA或音频-VLA方法的提升幅度。

## 🎯 结论与影响

最强结论是：声音中心操作必须依赖因果持续与显式时间建模，而非静态音频提示。该工作为多感官具身基础模型提供了一条可实践路径，可能推动后续研究把流式音频世界模型纳入VLA闭环。工业上对需要听觉反馈的机器人操作（如装配、交互）有潜在价值，但尚需真实平台验证。

## ⚠️ 局限与未解决问题

摘要未报告任何定量指标、消融或推理延迟，难以评估Historizer与Advancer各自的贡献。HEAR-Bench为自建基准，规模与多样性未知，存在自评偏差风险。与现有音频-VLA方法的对比缺失，且未说明真实机器人部署的实时性约束是否满足。

## 🔗 开源资源

- **项目主页**：<https://hear.irmv.top>
- **Demo / 试听**：<https://hear.irmv.top>

---

<div class="paper-footer"><span>评分：6.0</span><span>原始：6.0</span><a href="/audio-paper-daily/posts/2026-09-21/">← 返回 2026-09-21 速递</a></div>
