---
title: "Label Authority in Speech Emotion Recognition: Intended and Perceived Ground Truth in Emozionalmente"
date: 2026-10-20T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#语音情感识别"]
summary: "在意大利语表演语料 Emozionalmente 上比较三种标签权威：表演条件、听众多数票、完整投票分布，用冻结 XLS-R/HuBERT/WavLM 探针分析。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero">
<div class="hero-score">
<div class="score-num">6.8</div>
<div class="score-stars">★★★☆☆</div>
<div class="score-tier">中等</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#语音情感识别</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#语音情感识别</span> <span class="tag-pill tag-pill-soft">#标签不确定性</span> <span class="tag-pill tag-pill-soft">#自监督表征</span> <span class="tag-pill tag-pill-soft">#评测方法</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2610.26446</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-10-19</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2610.26446" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2610.26446" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>在意大利语表演语料 Emozionalmente 上比较三种标签权威：表演条件、听众多数票、完整投票分布，用冻结 XLS-R/HuBERT/WavLM 探针分析。
</div>

## 👥 作者与机构

**Marco Giordano** ¹ · Stefano Giacomelli · Claudia Rinaldi · Fabio Graziosi

**机构**：拉奎拉大学

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合做 SER 标注与评测、以及自监督表征 probing 的研究者。值得通读，重点看标签权威定义与探针实验设计（§3 与结果表），以及关于投票分布训练对概率校准影响的讨论；若只关心模型结构可略读。

## 🌍 研究背景

SER 长期把情感标签当作单一类别事实，但表演语料中“被表演的情感”与“听者感知到的情感”是不同问题。此前 SER 多以单标签训练与评测，忽略标注者分歧，导致模型在模糊样本上过拟合硬标签、评测口径不清。本文在同时提供表演标签与五名听者投票的 Emozionalmente 上，系统比较三种标签权威的可学习性与评测含义。

## 💡 核心创新

1. 区分表演条件、听众多数票、投票分布三种标签权威
2. 用冻结 XLS-R/HuBERT/WavLM 加匹配探针做受控比较
3. 分析听者一致性下降时多数票作为硬目标的脆弱性
4. 用完整投票分布训练改善概率分配而非硬决策

## 🏗️ 模型架构

输入为语音波形，分别经冻结的 XLS-R、HuBERT、WavLM 自监督前端提取帧级表征，经池化得到话语级嵌入；后端接匹配的轻量探针分类器（线性/浅层分类头），分别预测表演条件、听众多数票硬标签，以及五名听者投票的完整分布（分布目标用软标签损失）。三种标签权威共用同一表征与探针结构以隔离标签差异，输出为类别后验或投票分布。摘要未给出参数量。

## 📚 数据集

- Emozionalmente（意大利语表演情感语料，含表演标签与每段五名听者投票，用于训练与评估）

## 📊 实验结果

摘要未给出具体数值指标，仅给出定性结论：恢复表演条件比预测去平局后的听众多数票更容易，但二者回答的是不同问题；听者一致性越弱，多数票作为硬目标越脆弱；用完整投票分布训练基本不改变硬决策的获胜类别，但使概率分配更贴近听者所选备选，尤其在模糊片段上。

## 🎯 结论与影响

最强结论是三种标签权威不可互相替代：表演标签描述产生方式，多数票给出可操作的单类决策，投票分布保留感知不确定性。这提示后续 SER 研究应明确所预测的标签权威并保留聚合规则与一致性信息，对面向人机的 Internet of Sounds 应用评测口径有直接影响。

## ⚠️ 局限与未解决问题

仅在一个意大利语表演语料上验证，跨语种与自然语料泛化未知；未报告推理延迟与模型规模；探针容量与池化方式可能影响结论；缺少与端到端 SER 强 baseline 的对比，分布训练的收益仅体现在概率层面。

---

<div class="paper-footer"><span>评分：6.8</span><span>原始：6.8</span><a href="/audio-paper-daily/posts/2026-10-20/">← 返回 2026-10-20 速递</a></div>
