---
title: "Qwen-Audio-Jev: A Unified Interface for Audio Decisions"
date: 2026-10-23T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#音频理解"]
summary: "在 Qwen-Audio 上增加 Jev 决策头，用 CHOICE/NOUL/SCORE 三种原语直接输出概率或分数，替代自回归文本生成。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero">
<div class="hero-score">
<div class="score-num">7.2</div>
<div class="score-stars">★★★★☆</div>
<div class="score-tier">前25%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#音频理解</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#大音频语言模型</span> <span class="tag-pill tag-pill-soft">#判别式决策</span> <span class="tag-pill tag-pill-soft">#说话人确认</span> <span class="tag-pill tag-pill-soft">#语音质量评估</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2610.21614</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-10-23</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2610.21614" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2610.21614" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>在 Qwen-Audio 上增加 Jev 决策头，用 CHOICE/NOUL/SCORE 三种原语直接输出概率或分数，替代自回归文本生成。
</div>

## 👥 作者与机构

**Peixin Chen** ¹ · Zhigao Chen · Zhiyun Fan · Ying Fang · Zhifu Gao · Qing Gu · Jiajun He · Kangqi Jing · … 等 14 人

**机构**：阿里巴巴

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合做大音频语言模型（LALM）推理加速与判别式下游任务的研究者与工程团队阅读。值得通读，重点看 §3 中 Jev 决策头的接口设计与三类原语的输出形式，以及 §4 的 18 个基准评测表；若关注落地，优先看延迟/吞吐对比与 VoxCeleb1-O、NISQA 两行结果。

## 🌍 研究背景

当前 LALM（如 Qwen-Audio 系列）在音频理解上进展显著，但下游的选择、判断、打分任务仍依赖自回归文本生成，需逐 token 解码再解析答案，在高吞吐场景（大规模音频筛查、说话人核验、质量评估）中带来明显计算开销与延迟。已有工作多聚焦理解能力提升，较少系统处理“判别式读出”这一接口问题。本文要把这类任务统一为可直接输出概率分布或数值分数的决策接口。

## 💡 核心创新

1. 在 Qwen-Audio-3.1-ASR-Flash-Next 上增加专用 Jev 决策头
2. 提出 CHOICE/NOUL/SCORE 三种决策原语统一选择、二判、打分
3. 按答案规格输出任务条件概率分布或数值分数，免自回归解码

## 🏗️ 模型架构

输入为音频 + 自然语言问题 + 显式答案规格（候选选项、是/否、评分区间）。音频经 Qwen-Audio-3.1-ASR-Flash-Next 编码器与主干得到表示，再由新增的 Jev 决策头做类型化读出：CHOICE 在候选集合上输出归一化概率分布，NOUL 输出二分类概率，SCORE 回归出数值分数。摘要未给出参数量与决策头的具体结构细节。

## 📚 数据集

- MMAU（评估，CHOICE 准确率）
- MMSU（评估，CHOICE 准确率）
- VoxCeleb1-O（评估，说话人确认）
- NISQA（评估，整体质量打分）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| Accuracy | MMAU | 未在摘要给出 | **78.40%** | — |
| Accuracy | MMSU | 未在摘要给出 | **83.14%** | — |
| Accuracy | VoxCeleb1-O | 未在摘要给出 | **93.76%** | — |
| NMAE | NISQA | 未在摘要给出 | **0.1235** | — |

摘要报告在 18 个基准上的评测：CHOICE 在 MMAU 达 78.40%、MMSU 达 83.14%；NOUL 在 VoxCeleb1-O 说话人确认达 93.76%；SCORE 在 NISQA 整体质量评估上归一化平均绝对误差 0.1235。摘要未给出与自回归基线或其他 LALM 的逐项对比数值，也未报告延迟、吞吐与消融结果。

## 🎯 结论与影响

最强结论是：用类型化决策头替代自回归文本生成，可在多个判别式音频任务上取得可用精度。这为 LALM 的高吞吐部署提供了一条接口层面的改造思路，对大规模音频筛查、说话人核验与自动质检的工程落地有直接参考价值。

## ⚠️ 局限与未解决问题

摘要未给出与自回归解码的精度/延迟对照，难以判断效率收益是否以精度为代价；缺少决策头结构、训练数据与消融细节；18 个基准仅列 4 项结果，覆盖不全；未报推理延迟与显存占用。

---

<div class="paper-footer"><span>评分：7.2</span><span>原始：7.2</span><a href="/audio-paper-daily/posts/2026-10-23/">← 返回 2026-10-23 速递</a></div>
