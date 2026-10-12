---
title: "A Systematic Study of Cross-Modal Typographic Attacks on Audio-Visual Reasoning"
date: 2026-10-12T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#多模态推理"]
summary: "系统研究音视频多模态大模型在语音与屏幕文字扰动下的排版攻击脆弱性，并提出微调缓解方案。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#多模态推理</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#对抗攻击</span> <span class="tag-pill tag-pill-soft">#音视频多模态</span> <span class="tag-pill tag-pill-soft">#多模态大模型</span> <span class="tag-pill tag-pill-soft">#安全鲁棒性</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2604.03995</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-10-12</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2604.03995" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2604.03995" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>系统研究音视频多模态大模型在语音与屏幕文字扰动下的排版攻击脆弱性，并提出微调缓解方案。
</div>

## 👥 作者与机构

**Tianle Chen** ¹ · Deepti Ghadiyaram

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合做多模态大模型安全、对抗鲁棒性的研究者阅读。建议重点看攻击构造方法一节与跨模态效应分析，以及微调缓解实验。若只关心语音增强/分离，可略读。可先看 WorldSense 上的 ASR 结果表与消融。

## 🌍 研究背景

音视频多模态大模型（MLLM）正被部署到安全关键场景，但其跨模态脆弱性研究不足。此前对抗攻击多聚焦单模态（图像或文本），针对语音与屏幕文字联合扰动的排版攻击（typographic attack）在音视频推理中几乎空白。本文要系统刻画这类跨模态攻击如何影响闭源与开源模型的推理，并探索缓解手段。

## 💡 核心创新

1. 提出 Multi-Modal Typography 跨模态排版攻击框架
2. 系统分析单模态与多模态攻击的跨模态效应
3. 在内容审核与机器人任务选择等基准上验证攻击泛化性
4. 用微调作为缓解手段降低攻击成功率

## 🏗️ 模型架构

论文为攻击与评测研究，非新网络架构。流程为：对输入语音加扰动、对屏幕文字加排版扰动，构造单模态与多模态攻击样本，送入闭源（Gemini 3.7 Flash）与开源（Qwen2.5-Omni-7B）音视频 MLLM 进行推理，统计攻击成功率（ASR）。缓解侧对 Qwen2.5-Omni-7B 做微调以降低 ASR。摘要未给出参数量或具体主干细节。

## 📚 数据集

- WorldSense（评估，音视频推理基准）
- 内容审核基准（评估）
- 离线机器人任务选择基准（评估）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| ASR | WorldSense | Gemini 3.7 Flash 9.53% | **43.41%** | +33.88% |
| ASR | WorldSense | Qwen2.5-Omni-7B 60.6% | **52.0%（微调缓解后）** | -8.6% |

在 WorldSense 上，攻击使 Gemini 3.7 Flash 的 ASR 从 9.53% 升至 43.41%，Qwen2.5-Omni-7B 原始 ASR 达 60.6%。微调缓解后 Qwen2.5-Omni-7B 的 ASR 降至 52.0%，仅部分缓解。摘要未报告内容审核与机器人任务选择基准的具体数值，也未给出推理延迟或效率指标。

## 🎯 结论与影响

最强结论是音视频 MLLM 对语音与屏幕文字的跨模态排版攻击高度脆弱，闭源模型 ASR 可提升逾 30 个百分点。该工作提示多模态推理安全评测需纳入跨模态攻击维度，对工业界部署安全关键音视频系统具有警示意义，微调仅能部分缓解。

## ⚠️ 局限与未解决问题

微调缓解后 ASR 仍达 52.0%，缓解效果有限；摘要未报告内容审核与机器人基准的具体数值，缺少完整消融；未讨论推理开销与防御的泛化性；攻击对真实部署场景的可行性未充分论证。

---

<div class="paper-footer"><span>评分：6.8</span><span>原始：6.8</span><a href="/audio-paper-daily/posts/2026-10-12/">← 返回 2026-10-12 速递</a></div>
