---
title: "Rethinking Training Targets, Architectures and Data Quality for Universal Speech Enhancement"
date: 2026-10-07T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#语音增强"]
summary: "系统重审通用语音增强的训练目标、架构与数据质量，提出时移无回声目标与两阶段框架，在 URGENT 2025 非盲测集达 SOTA。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero hero-focus">
<div class="hero-score">
<div class="score-num">9.5</div>
<div class="score-stars">★★★★★</div>
<div class="score-tier">前10%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#语音增强</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#语音增强</span> <span class="tag-pill tag-pill-soft">#去混响</span> <span class="tag-pill tag-pill-soft">#数据筛选</span> <span class="tag-pill tag-pill-soft">#语音识别</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2603.02641</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-10-07</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">🔥 强烈推荐通读</span></div>
<div class="meta-row"><span class="meta-key">⭐</span><span class="meta-val focus-badge">本站重点关注领域 · 评分 +1</span></div>
</div>
</div>

<div class="opensource-banner"><div class="oc-headline"><span class="oc-pulse"></span><span class="oc-title">本论文已开源</span><span class="oc-hint">点击下方卡片直达对应资源</span></div><div class="oc-grid"><a class="oc-chip oc-chip-hf" href="https://huggingface.co/nvidia/RE-USE" target="_blank" rel="noopener"><span class="oc-icon">🤗</span><span class="oc-text"><span class="oc-label">HuggingFace</span><span class="oc-sub">🤗 nvidia/RE-USE</span></span></a></div></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2603.02641" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2603.02641" target="_blank" rel="noopener">📑 PDF</a><a class="rsrc rsrc-hf" href="https://huggingface.co/nvidia/RE-USE" target="_blank" rel="noopener">🤗 HuggingFace</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>系统重审通用语音增强的训练目标、架构与数据质量，提出时移无回声目标与两阶段框架，在 URGENT 2025 非盲测集达 SOTA。
</div>

## 👥 作者与机构

**Szu-Wei Fu** ¹ · **Rong Chao** ¹ · Xuesong Yang · Sung-Feng Huang · Ryandhimas E. Zezario · Rauf Nasretdinov · Ante Juki\'c · Yu Tsao · … 等 1 人

**机构**：英伟达 · 中央研究院 · 台湾大学

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合做通用语音增强、去混响与 TTS 数据清洗的研究者与工程团队。建议通读：先看 §3 关于训练目标（时移无回声 vs 早期反射）的分析与表 2，再看两阶段框架与数据规模-质量权衡实验，最后对照 URGENT 2025 结果。

## 🌍 研究背景

通用语音增强（USE）目标是在多种退化条件下恢复语音质量并保持信号保真度。此前 SOTA 多依赖早期反射语音作为去混响目标，并堆叠大规模未筛选语料训练。但早期反射目标会引入感知伪影、损害下游 ASR；同时失真-感知权衡与数据规模-质量关系缺乏系统研究，导致性能存在天花板。本文针对训练目标选择、失真-感知权衡、数据筛选三个被忽视的问题展开系统研究。

## 💡 核心创新

1. 用时间对齐的无回声干净语音替代早期反射语音作为去混响训练目标
2. 基于失真-感知权衡理论提出两阶段框架，在给定感知质量下最小化失真
3. 系统分析训练数据规模与质量权衡，揭示未筛选大语料的性能天花板
4. 方法具备强语言无关泛化能力，可有效提升 TTS 训练数据质量

## 🏗️ 模型架构

摘要未给出具体网络结构细节。整体为两阶段框架：第一阶段在给定感知质量约束下优化失真，第二阶段进一步精修以逼近最小失真点。训练目标由早期反射语音改为时间对齐的无回声干净语音，输入为退化语音，输出为增强后语音。模型权重以 RE-USE 名称发布，具体主干网络（如 Conformer / BSRNN 等）摘要未说明。

## 📚 数据集

- URGENT 2025 非盲测试集（评估）
- 大规模未筛选语料（训练，具体名称未给出）
- TTS 训练数据（应用验证）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| SOTA 性能 | URGENT 2025 非盲测试集 | 摘要未给出具体基线数值 | **达到 SOTA** | 摘要未给出具体数值 |

摘要称方法在 URGENT 2025 非盲测试集上达到 SOTA，并展现强语言无关泛化能力，可有效改善 TTS 训练数据。但摘要未提供 SI-SDR、PESQ、WER 等具体指标数值，也未给出消融实验与效率指标，需查阅正文表格确认提升幅度。

## 🎯 结论与影响

最强结论是：训练目标、架构与数据质量三者需协同重审，时移无回声目标加两阶段框架可在 USE 上取得 SOTA。该工作可能推动社区重新审视去混响目标定义与数据筛选策略，并对 TTS 数据清洗、跨语言语音前端等工业落地有直接价值。

## ⚠️ 局限与未解决问题

摘要未给出具体指标数值、消融实验与推理延迟，难以判断各组件贡献；数据规模-质量权衡结论依赖特定语料，泛化性待验证；两阶段框架增加训练与推理复杂度，未报告效率开销；与最新强基线（如基于扩散或语言模型的方法）对比不明确。

## 🔗 开源资源

- **HuggingFace**：<https://huggingface.co/nvidia/RE-USE>

---

<div class="paper-footer"><span>评分：9.5</span><span>原始：8.5</span><span>+1 重点领域加权</span><a href="/audio-paper-daily/posts/2026-10-07/">← 返回 2026-10-07 速递</a></div>
