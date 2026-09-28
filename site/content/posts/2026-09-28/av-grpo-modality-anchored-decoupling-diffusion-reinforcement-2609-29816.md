---
title: "AV-GRPO: Modality-Anchored Decoupling Diffusion Reinforcement Learning for Joint Audio-Video Generation"
date: 2026-09-28T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#音频生成"]
summary: "提出AV-GRPO，用模态锚定的解耦扩散强化学习框架与5DAV数据集，提升音视频联合生成的质量、语义对齐与跨模态同步。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#音频生成</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#音频生成</span> <span class="tag-pill tag-pill-soft">#视频生成</span> <span class="tag-pill tag-pill-soft">#强化学习</span> <span class="tag-pill tag-pill-soft">#多模态</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2609.29816</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-09-28</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner"><div class="oc-headline"><span class="oc-pulse"></span><span class="oc-title">本论文已开源</span><span class="oc-hint">点击下方卡片直达对应资源</span></div><div class="oc-grid"><a class="oc-chip oc-chip-code" href="https://github.com/zhiyuxu03/AV-GRPO" target="_blank" rel="noopener"><span class="oc-icon">💻</span><span class="oc-text"><span class="oc-label">代码仓库</span><span class="oc-sub">zhiyuxu03/AV-GRPO</span></span></a></div></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2609.29816" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2609.29816" target="_blank" rel="noopener">📑 PDF</a><a class="rsrc rsrc-code" href="https://github.com/zhiyuxu03/AV-GRPO" target="_blank" rel="noopener">💻 代码</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出AV-GRPO，用模态锚定的解耦扩散强化学习框架与5DAV数据集，提升音视频联合生成的质量、语义对齐与跨模态同步。
</div>

## 👥 作者与机构

**Zhiyu Xu** ¹ · Weilong Yan · Yufei Shi · Shiyang Li · Yihao Liu · Kin-Man Lam · Yuewen Cao

**机构**：香港城市大学

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合做音视频联合生成、扩散模型 RL 后训练的研究者阅读。建议重点看 §3 的三大模块（模态锚定 rollout、冻结塔优化、自适应目标）与 5DAV 数据集的五维解耦设计，再看 JavisBench/VABench 上的对比表与消融。若只关心语音/音频分离方向，可略读。

## 🌍 研究背景

音视频联合生成近年进展明显，但现有模型在单模态保真度、文本-模态对齐和跨模态同步上仍不足。RL 后训练是潜在补救手段，但直接迁移到联合生成面临三重困难：异构多模态奖励纠缠导致信用分配困难；两个模态塔联合优化计算代价高且动态差异大；同步评估依赖配对样本，难以公平比较奖励。本文针对这些问题提出解耦式在线扩散 RL 框架。

## 💡 核心创新

1. 模态锚定 rollout，解耦学习信号并稳定难度
2. 轨迹锁定冻结塔优化，降低计算成本并重分配信用
3. 面向模态动态的自适应目标与扰动强度
4. 5DAV 五维解耦、难度可控训练数据集

## 🏗️ 模型架构

输入为文本条件与音视频对，主干为扩散生成模型（含音频塔与视频塔）。AV-GRPO 在在线 RL 后训练中引入三个模块：模态锚定 rollout 将联合采样拆为单模态子问题以解耦奖励；轨迹锁定冻结塔优化在更新一塔时冻结另一塔，降低联合优化开销并重新分配信用；自适应目标与扰动强度按各模态动态调整。最终将耦合多模态偏好学习转化为单模态子问题，输出音视频生成结果。摘要未给出参数量。

## 📚 数据集

- 5DAV（训练，五维解耦、难度可控）
- JavisBench（评估）
- VABench（评估）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| 生成质量 / 语义对齐 / 跨模态同步（综合） | JavisBench 与 VABench | LTX-2.3 | **AV-GRPO** | 在 LoRA 与全量微调下均优于基线 |

摘要称在 JavisBench 和 VABench 上，AV-GRPO 在生成质量、语义对齐和跨模态同步三方面均优于 LTX-2.3，且在 LoRA 与全量微调两种设置下成立；消融实验确认了各设计模块的有效性。但摘要未给出具体指标数值、推理延迟或参数量，无法量化提升幅度。

## 🎯 结论与影响

最强结论是：将耦合多模态偏好学习解耦为单模态子问题，可在不牺牲单模态质量的前提下改善跨模态同步。这为音视频联合生成的 RL 后训练提供了可复用的解耦范式，并提示工业界可用冻结塔策略降低联合优化成本。

## ⚠️ 局限与未解决问题

摘要未报告具体指标数值、推理延迟与参数量，难以判断实际增益与效率；同步评估依赖配对样本的问题是否被彻底解决仍不明确；5DAV 数据集的构建细节与偏差未在摘要中说明；与更多音视频联合生成基线的对比缺失。

## 🔗 开源资源

- **代码**：<https://github.com/zhiyuxu03/AV-GRPO>

---

<div class="paper-footer"><span>评分：6.5</span><span>原始：6.5</span><a href="/audio-paper-daily/posts/2026-09-28/">← 返回 2026-09-28 速递</a></div>
