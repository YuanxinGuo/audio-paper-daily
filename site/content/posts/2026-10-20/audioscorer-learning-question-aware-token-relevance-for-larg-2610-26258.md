---
title: "AudioScorer: Learning Question-Aware Token Relevance for Large Audio Language Models"
date: 2026-10-20T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#音频处理"]
summary: "提出轻量AudioScorer，按用户问题给音频token打分，蒸馏冻结LALM的答案梯度显著性排序，实现问题感知的音频token剪枝。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#音频处理</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#音频语言模型</span> <span class="tag-pill tag-pill-soft">#Token剪枝</span> <span class="tag-pill tag-pill-soft">#知识蒸馏</span> <span class="tag-pill tag-pill-soft">#语音识别</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2610.26258</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-10-19</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2610.26258" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2610.26258" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出轻量AudioScorer，按用户问题给音频token打分，蒸馏冻结LALM的答案梯度显著性排序，实现问题感知的音频token剪枝。
</div>

## 👥 作者与机构

**Marwan Farag** ¹ · Bin Yang

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合做大模型音频编码效率、token压缩与LALM推理加速的研究者阅读。值得通读，重点看§3的蒸馏目标设计与§4的10%保留率实验表；可先看表2与消融部分，确认问题感知打分相对纯注意力/相似度启发式的增益来源。

## 🌍 研究背景

LALM（如Qwen-Audio、SALMONN类）在语音、环境声、音乐上做推理，但音频编码器输出稠密token序列，长音频推理成本高。已有剪枝方法依赖注意力权重、表示相似度或时间采样等启发式，未显式建模“当前问题需要哪些token”。本文要解决的是：在给定用户问题条件下学习token相关性打分，从而在低保留率下保住下游任务性能。

## 💡 核心创新

1. 轻量AudioScorer按问题对音频token打分
2. 蒸馏冻结LALM的答案梯度显著性排序
3. 联合下游答案监督训练打分器
4. 问题感知剪枝替代注意力/相似度启发式

## 🏗️ 模型架构

输入为用户问题文本与LALM音频编码器输出的稠密音频token序列；AudioScorer作为轻量打分网络，对每个音频token输出与问题相关的重要性分数，据此保留Top-K token送入冻结的LALM解码。训练采用双监督：一是蒸馏冻结LALM上答案梯度显著性所诱导的token排序，二是下游答案的生成监督。摘要未给出参数量与具体主干网络名。

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| 10% token保留率下的任务表现（最佳或并列最佳任务数） | 10个语义与声学任务（含语音识别、情感识别、音频场景分类） | 注意力/表示相似度/时间采样等剪枝方法 | **10个任务中7个最佳或并列最佳** | 7/10 任务领先 |

摘要仅报告在10% token保留率下，AudioScorer在10个语义与声学任务中的7个取得最佳或并列最佳，覆盖语音识别、情感识别与音频场景分类；未给出具体指标数值、消融细节、效率（延迟/显存）数据，也未说明剩余3个任务的具体差距。

## 🎯 结论与影响

最强结论是：问题感知的token打分在极低保留率（10%）下优于现有启发式剪枝，说明“按问题选token”是有效方向。对LALM长音频推理加速与token压缩研究有直接参考价值，工业上可降低长音频推理成本。

## ⚠️ 局限与未解决问题

摘要未给具体指标数值与逐任务对比，缺少打分器开销、端到端延迟与显存测量；蒸馏依赖答案梯度显著性，其计算成本与稳定性未讨论；仅报10%单点保留率，缺少多保留率曲线与跨LALM泛化验证。

---

<div class="paper-footer"><span>评分：6.8</span><span>原始：6.8</span><a href="/audio-paper-daily/posts/2026-10-20/">← 返回 2026-10-20 速递</a></div>
