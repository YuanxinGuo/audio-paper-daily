---
title: "From Continuous Deployment to Queryable Dataset: Terabyte-Scale AIS-Aligned Passive Acoustic Labelling"
date: 2026-07-16T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#声学数据处理"]
summary: "提出一种数据库原生工作流，将水听器录音与AIS位置报告对齐，生成可查询的结构化表格，支持大规模被动声学数据的机器学习分析。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#声学数据处理</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#被动声学监测</span> <span class="tag-pill tag-pill-soft">#AIS数据对齐</span> <span class="tag-pill tag-pill-soft">#数据库工作流</span> <span class="tag-pill tag-pill-soft">#海洋声学</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2607.13840</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-07-16</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2607.13840" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2607.13840" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出一种数据库原生工作流，将水听器录音与AIS位置报告对齐，生成可查询的结构化表格，支持大规模被动声学数据的机器学习分析。
</div>

## 👥 作者与机构

**Wayne Renaud** ¹ · Priyanka Aravindan · Gabriel Spadon

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合海洋声学、被动声学监测及大规模音频数据处理研究者。重点读§3（数据库工作流设计）和§4（结果分析），可跳过§2背景。若关注声学特征提取，可结合附录看频谱分析细节。

## 🌍 研究背景

长期被动声学部署产生大量录音档案，但缺乏与船只轨迹或遭遇结构的关联，导致距离和接触条件不可用，需手动选择分析。现有方法依赖内存嵌套迭代，无法处理连续多年、百万窗口的存档。本文提出数据库原生工作流，通过空间时间索引连接水听器录音与AIS位置报告，生成结构化表格，支持可扩展的机器学习。

## 💡 核心创新

1. 数据库原生工作流替代内存嵌套迭代
2. 索引时空连接实现可扩展处理
3. 确定性频谱排名表征背景条件
4. 生成无接触、单接触、双接触窗口的结构化表格

## 🏗️ 模型架构

输入为固定时长录音窗口和AIS消息，存储为持久化地理空间表。通过索引时空连接关联两者，使用数据库集合操作替代内存迭代。输出结构化表格，包含最近接近点距离、背景频谱排名等字段。处理约95万录音窗口和690万AIS位置报告。

## 📚 数据集

- 被动声学录音（约9.5e5窗口，用于处理和分析）
- AIS位置报告（约6.9e6条，用于对齐）

## 📊 实验结果

摘要未提供具体定量指标（如SI-SDR等），但展示了处理规模：约95万录音窗口和690万AIS位置报告。结果显示噪声主导条件，船只贡献主要在短距离，信号噪声比随距离衰减，弱音调信号嵌入噪声中。

## 🎯 结论与影响

本文提出一种可扩展的数据库原生工作流，将大规模被动声学数据与AIS对齐，生成结构化表格，支持机器学习分析。该方法能处理多年连续部署，揭示噪声主导环境下的信号结构，为海洋声学预测建模和相似性分析提供基础。对工业落地，可提升海洋监测自动化水平。

## ⚠️ 局限与未解决问题

摘要未提及方法在真实海洋环境中的泛化能力，未报告处理延迟或内存消耗对比。缺乏与现有方法（如基于内存的迭代）的定量比较。未讨论不同水域或噪声条件下的鲁棒性。

---

<div class="paper-footer"><span>评分：6.5</span><span>原始：6.5</span><a href="/audio-paper-daily/posts/2026-07-16/">← 返回 2026-07-16 速递</a></div>
