---
title: "GrowLoop: Self-Evolving Conversation Evaluation Seeded by Human"
date: 2026-05-29T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#对话评估"]
summary: "提出GrowLoop，一种自进化的对话评估系统，通过少量人工种子标注和启发式学习持续优化评估准则，实现与人类判断高度对齐。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero">
<div class="hero-score">
<div class="score-num">7.8</div>
<div class="score-stars">★★★★☆</div>
<div class="score-tier">前25%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#对话评估</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#大语言模型</span> <span class="tag-pill tag-pill-soft">#自进化基准</span> <span class="tag-pill tag-pill-soft">#人类相似性评估</span> <span class="tag-pill tag-pill-soft">#启发式学习</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2605.28882</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-05-29</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2605.28882" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2605.28882" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出GrowLoop，一种自进化的对话评估系统，通过少量人工种子标注和启发式学习持续优化评估准则，实现与人类判断高度对齐。
</div>

## 👥 作者与机构

**Yihang Lin** ¹ · Yunze Gao · Zeyang Lin · Dongbo Li · Kun Peng · Chenglong Song · Yue Liu

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合从事LLM评估、对话系统研究的读者。建议重点阅读§3方法部分（Heuristic Learning和Rubric-Case共进化机制）以及§4实验结果。可先看图1和表2了解整体框架和性能。

## 🌍 研究背景

开放域对话中的人类相似性评估是隐性知识，人类判断存在一致性和分歧，且评估标准随模型能力动态变化。现有方法如专家编写的基准、奖励模型、自进化基准均无法同时解决这三个挑战。本文旨在构建一个能持续适应模型进步和场景变化的对话评估系统。

## 💡 核心创新

1. Heuristic Learning：LLM代理从种子标注中迭代提取和精炼评估准则
2. Rubric-Case共进化机制：准则与测试案例协同更新
3. 人类-AI一致性约束：收敛处要求一致，分歧处仅需合理性
4. 新种子注入实现评估目标迁移

## 🏗️ 模型架构

输入：少量人工种子标注（对话样本及人类判断）→ LLM代理通过Heuristic Learning提取初始评估准则（rubrics）→ 基于准则生成测试案例（cases）→ 人类与AI共同评估，收敛处要求一致，分歧处仅需合理性 → 准则与案例迭代更新（Rubric-Case共进化）→ 当评估目标变化时注入新种子重新启动进化。输出：持续更新的评估准则和基准测试集。

## 📚 数据集

- 自建对话数据集（用于种子标注和评估，未说明规模）
- 现有对话基准（用于对比实验，未具体列出）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| 与人类判断的一致性（如Spearman相关系数） | 自建对话评估集 | 现有方法（如Reward Model） | **GrowLoop** | 显著优于（具体数值未给出） |

摘要指出生成的准则在人类判断对齐上显著优于现有方法，并能发现标注者忽略的问题。基准有效区分不同能力层级的模型，并揭示其不足。同时能泛化到新场景并随模型进步适应。但未提供具体数值，需查阅全文。

## 🎯 结论与影响

GrowLoop通过自进化机制实现了对话评估的持续适应，在人类对齐和发现问题能力上超越现有方法。该工作将基准构建从手动更新或难度扩展转向全面、持续的自进化，为LLM评估提供了新范式，有望推动更动态、更贴近人类直觉的评估体系。

## ⚠️ 局限与未解决问题

摘要未提及局限。可能的问题：种子标注的质量和数量对初始准则影响大；Heuristic Learning的收敛性未分析；与人类判断的一致性可能受标注者偏差影响；未报告计算开销和推理延迟。

---

<div class="paper-footer"><span>评分：7.8</span><span>原始：7.8</span><a href="/audio-paper-daily/posts/2026-05-29/">← 返回 2026-05-29 速递</a></div>
