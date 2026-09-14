---
title: "CMA-OT: Hierarchical Expert Supervision for Dance-to-Music Generation"
date: 2026-09-14T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#音乐生成"]
summary: "用外部音乐专家对生成器隐特征做分层监督，结合课程式多尺度学习与尺度感知最优传输对齐，实现舞蹈到音乐的节奏与风格同步生成。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#音乐生成</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#音乐生成</span> <span class="tag-pill tag-pill-soft">#跨模态生成</span> <span class="tag-pill tag-pill-soft">#最优传输</span> <span class="tag-pill tag-pill-soft">#知识蒸馏</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2609.13118</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-09-14</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2609.13118" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2609.13118" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>用外部音乐专家对生成器隐特征做分层监督，结合课程式多尺度学习与尺度感知最优传输对齐，实现舞蹈到音乐的节奏与风格同步生成。
</div>

## 👥 作者与机构

**Jinting Wang** ¹ · Chenxing Li · Dong Yu · Li Liu

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合做跨模态音乐生成、多模态对齐与知识蒸馏的研究者阅读。建议重点看 §3 的课程式多尺度学习策略与尺度感知 OT 对齐模块，以及实验部分的节奏同步与感知质量指标。若关注 D2M 任务，可先看表 1 与消融实验，判断分层监督是否真正带来增益。

## 🌍 研究背景

舞蹈到音乐生成需从稀疏的舞蹈节奏与风格线索合成结构完整、配器丰富的音乐，存在语义密度不匹配问题。此前方法多依赖稀疏线索并仅监督最终音频输出，导致音乐表征学习不足、生成音乐结构连贯性与音乐性有限。本文引入外部音乐专家提供分层监督，试图弥合语义鸿沟并提升表征学习质量。

## 💡 核心创新

1. 引入外部音乐专家对生成器隐特征做分层监督
2. 课程式多尺度学习策略渐进迁移音乐知识
3. 尺度感知最优传输对齐处理时序错配下的软对应

## 🏗️ 模型架构

输入为舞蹈视频提取的节奏与风格线索，经生成器主干得到多尺度隐特征；外部音乐专家提供分层表征作为监督信号。关键模块包括课程式多尺度学习策略，按尺度逐步对齐专家与生成器表征；以及尺度感知最优传输对齐机制，在不同专家尺度间建模软对应以应对时序错配。输出为与舞蹈节奏和风格对齐的音乐音频。摘要未给出具体参数量。

## 📚 数据集

- 两个数据集（训练与评估，摘要未具名）

## 📊 实验结果

摘要在两个数据集上报告 CMA-OT 在节奏同步、感知质量和整体音乐生成上达到 state-of-the-art，但未给出具体指标数值、基线名称或消融结果，无法量化提升幅度。

## 🎯 结论与影响

本文最强结论是分层专家监督加尺度感知 OT 对齐可显著改善 D2M 的节奏同步与音乐性。该思路对跨模态生成中的稀疏-稠密语义对齐有参考价值，工业上可用于短视频配乐、舞蹈教学伴奏等场景，但需验证推理成本与实时性。

## ⚠️ 局限与未解决问题

摘要未给出具体指标、基线对比与消融实验，无法判断各模块贡献；外部音乐专家的选择与依赖未说明；未报告推理延迟与参数量；两个数据集未具名，泛化性存疑。

---

<div class="paper-footer"><span>评分：6.8</span><span>原始：6.8</span><a href="/audio-paper-daily/posts/2026-09-14/">← 返回 2026-09-14 速递</a></div>
