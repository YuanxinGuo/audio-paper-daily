---
title: "MSU-Bench: Towards Speaker-Centric Understanding in Conversational Multi-Speaker Scenarios"
date: 2026-06-23T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#说话人理解"]
summary: "提出MSU-Bench基准，系统评估大音频语言模型在多说话人对话中的说话人中心理解能力，涵盖16项任务和2300个QA实例。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero">
<div class="hero-score">
<div class="score-num">8.2</div>
<div class="score-stars">★★★★☆</div>
<div class="score-tier">前25%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#说话人理解</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#多说话人</span> <span class="tag-pill tag-pill-soft">#对话理解</span> <span class="tag-pill tag-pill-soft">#基准测试</span> <span class="tag-pill tag-pill-soft">#大音频语言模型</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2606.22868</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-06-22</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">🔥 强烈推荐通读</span></div>
</div>
</div>

<div class="opensource-banner"><div class="oc-headline"><span class="oc-pulse"></span><span class="oc-title">本论文已开源</span><span class="oc-hint">点击下方卡片直达对应资源</span></div><div class="oc-grid"><a class="oc-chip oc-chip-code" href="https://github.com/ASLP-lab/MSU-Bench" target="_blank" rel="noopener"><span class="oc-icon">💻</span><span class="oc-text"><span class="oc-label">代码仓库</span><span class="oc-sub">ASLP-lab/MSU-Bench</span></span></a></div></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2606.22868" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2606.22868" target="_blank" rel="noopener">📑 PDF</a><a class="rsrc rsrc-code" href="https://github.com/ASLP-lab/MSU-Bench" target="_blank" rel="noopener">💻 代码</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出MSU-Bench基准，系统评估大音频语言模型在多说话人对话中的说话人中心理解能力，涵盖16项任务和2300个QA实例。
</div>

## 👥 作者与机构

**Zhaokai Sun** ¹ · Shuai Wang · Zhennan Lin · Chengyou Wang · Dehui Gao · Yuang Cao · Chunjiang He · Pan Zhou · … 等 1 人

**机构**：西北工业大学

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合研究SLU、LALM及多说话人场景的学者。建议通读，重点看§3任务框架和§5实验结果，了解模型在说话人定位与推理上的瓶颈。

## 🌍 研究背景

语音语言理解正从任务特定管道转向大音频语言模型，但现有基准多聚焦单说话人或孤立子任务，缺乏对多说话人对话中说话人中心理解的系统评估。本文旨在填补这一空白，构建覆盖说话人定位到对话推理的多层次诊断基准。

## 💡 核心创新

1. 提出16项说话人中心任务的两层框架
2. Gemini辅助标注与人工验证的QA生成管道
3. 系统分析说话人引用方案与诊断错误类型
4. 揭示闭源与开源模型在说话人理解上的差距

## 🏗️ 模型架构

MSU-Bench是一个基准测试框架，非模型架构。它包含2300个QA实例，覆盖16项任务，分为说话人定位和对话推理两层。数据来自多说话人对话，通过Gemini辅助生成QA对，经人工验证确保质量。评估脚本开源。

## 📚 数据集

- MSU-Bench（基准测试，2300个QA实例，覆盖16项任务）

## 📊 实验结果

摘要未提供具体数值，但指出闭源系统整体领先，所有模型在复杂说话人定位和多说话人推理上仍面临挑战。实验揭示了不同模型家族间的明显差距。

## 🎯 结论与影响

MSU-Bench为多说话人对话中的说话人中心理解提供了系统评估框架，揭示了现有LALM在说话人定位与推理上的不足。该基准将推动模型在真实对话场景中的能力提升，对语音助手等工业应用有重要参考价值。

## ⚠️ 局限与未解决问题

基准规模有限（2300个QA），可能未覆盖所有多说话人场景；依赖Gemini辅助标注，可能存在偏差；未评估模型效率或推理延迟；未提供模型在基准上的详细性能分解。

## 🔗 开源资源

- **代码**：<https://github.com/ASLP-lab/MSU-Bench>

---

<div class="paper-footer"><span>评分：8.2</span><span>原始：8.2</span><a href="/audio-paper-daily/posts/2026-06-23/">← 返回 2026-06-23 速递</a></div>
