---
title: "FRAUDSkill: Structured Frozen-Weight Skill Optimization for Audio Anti-Fraud Detection"
date: 2026-09-18T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#音频反欺诈检测"]
summary: "提出FRAUDSkill框架，冻结音频语言模型权重，通过外部技能程序与路由策略优化，实现结构化音频反欺诈检测。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#音频反欺诈检测</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#音频语言模型</span> <span class="tag-pill tag-pill-soft">#冻结权重适配</span> <span class="tag-pill tag-pill-soft">#结构化输出控制</span> <span class="tag-pill tag-pill-soft">#反欺诈检测</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2609.18766</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-09-18</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner"><div class="oc-headline"><span class="oc-pulse"></span><span class="oc-title">本论文已开源</span><span class="oc-hint">点击下方卡片直达对应资源</span></div><div class="oc-grid"><a class="oc-chip oc-chip-code" href="https://anonymous.4open.science/r/FRAUDSKILL-114514" target="_blank" rel="noopener"><span class="oc-icon">💻</span><span class="oc-text"><span class="oc-label">代码仓库</span><span class="oc-sub">anonymous.4open.science/r/FRAUDSKILL-114514</span></span></a></div></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2609.18766" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2609.18766" target="_blank" rel="noopener">📑 PDF</a><a class="rsrc rsrc-code" href="https://anonymous.4open.science/r/FRAUDSKILL-114514" target="_blank" rel="noopener">💻 代码</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出FRAUDSkill框架，冻结音频语言模型权重，通过外部技能程序与路由策略优化，实现结构化音频反欺诈检测。
</div>

## 👥 作者与机构

**Chengxian Hu** ¹ · Zhiming Ma · Mingjun Pan · Yifan Wang · Shun Zhang · Qifan Wang · Zhilei Zhao · Yijin Zhou · … 等 4 人

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合关注音频语言模型落地、结构化预测与反欺诈检测的研究者阅读。建议重点看§3技能程序与路由策略设计、§4结构化输出控制与验证引导多路径推理，以及表2在TeleAntiFraud上的对比结果。若关注冻结权重适配范式，可通读；若仅关注语音增强/分离，可略读。

## 🌍 研究背景

音频反欺诈检测需模型在预定义标签空间内完成服务场景识别、欺诈检测与条件欺诈类型分类的结构化决策。现有微调与提示方法将任务知识、约束与决策规则编码进模型参数或人工维护的提示中，难以随欺诈模式与标注策略演进而快速适配。本文旨在不修改底层音频语言模型的前提下，通过外部技能优化实现可适配的结构化反欺诈检测。

## 💡 核心创新

1. 冻结底层音频语言模型，仅优化外部技能程序层
2. 引入路由特定策略与决策规则实现结构化决策
3. 结合结构化输出控制与验证引导多路径推理
4. 在TeleAntiFraud上显著降低无效输出至1.94%

## 🏗️ 模型架构

输入为语音信号，经冻结的音频语言模型提取表征；外部技能程序层包含路由特定策略与决策规则，负责服务场景识别、欺诈检测与条件欺诈类型分类；结构化输出控制模块约束预测符合预定义标签空间；验证引导多路径推理模块在推理阶段筛选协议合规输出。底层模型权重不变，仅优化外部技能层。

## 📚 数据集

- TeleAntiFraud（评估，基准测试）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| Macro-F1 | TeleAntiFraud | 共享冻结模型基线 41.54% | **73.50%** | +31.96% |
| 无效输出率 | TeleAntiFraud | 未提供 | **1.94%** | 未提供 |

在TeleAntiFraud基准上，FRAUDSkill取得73.50% Macro-F1，较共享冻结模型基线提升31.96%，无效输出降至1.94%。摘要未提供消融实验、跨数据集泛化或推理延迟等具体数据，仅说明大量实验验证了外部技能优化的有效性与可适配性。

## 🎯 结论与影响

本文最强结论是：在不修改底层音频语言模型的前提下，外部技能优化可有效实现结构化音频反欺诈检测。该范式为音频语言模型在合规敏感场景的快速适配提供了新思路，对工业界反欺诈系统迭代与标注策略更新具有落地参考价值。

## ⚠️ 局限与未解决问题

摘要未提供消融实验、推理延迟与参数量等效率指标，也未说明技能程序与路由策略的具体实现细节及跨数据集泛化能力。仅在一个基准上评估，缺乏与更多微调或提示方法的全面对比，外部技能层的可维护性与扩展性未充分讨论。

## 🔗 开源资源

- **代码**：<https://anonymous.4open.science/r/FRAUDSKILL-114514>

---

<div class="paper-footer"><span>评分：6.0</span><span>原始：6.0</span><a href="/audio-paper-daily/posts/2026-09-18/">← 返回 2026-09-18 速递</a></div>
