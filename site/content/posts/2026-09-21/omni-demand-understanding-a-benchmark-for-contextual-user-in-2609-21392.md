---
title: "Omni Demand Understanding: A Benchmark for Contextual User-Intent Inference in Multimodal Interaction"
date: 2026-09-21T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#多模态交互理解"]
summary: "提出 ODU-Bench 基准，评测多模态大模型能否从音视频与对话上下文中推断用户潜在需求，14 个模型均表现不佳。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#多模态交互理解</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#多模态大模型评测</span> <span class="tag-pill tag-pill-soft">#用户意图推断</span> <span class="tag-pill tag-pill-soft">#音视频交互</span> <span class="tag-pill tag-pill-soft">#基准数据集</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2609.21392</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-09-21</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2609.21392" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2609.21392" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出 ODU-Bench 基准，评测多模态大模型能否从音视频与对话上下文中推断用户潜在需求，14 个模型均表现不佳。
</div>

## 👥 作者与机构

**Qi Chen** ¹ · Yunfei Chu · Haolin He · Yifan Yang · Zihan Liu · Yuxuan Wang · Ziyang Ma · Ruiyang Xu · … 等 10 人

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合做多模态对话系统、语音助手意图理解与评测的研究者阅读。建议重点看 §3 的 ODU 五维任务定义与 ODU-Bench 构建流程（taxonomy 驱动的 agentic 视频生成 + 人工录制 + 人工校验），以及 §5 的 14 个 MLLM 结果表与 false-trigger 分析。若只关心语音增强/分离方法本身，可略读。

## 🌍 研究背景

音视频自然交互正成为 AI 助手的重要入口，但现有交互能力基准多聚焦回答质量，忽略了更根本的问题：模型能否从复杂多模态交互中正确推断用户潜在需求。真实需求常在语音中欠指定，需结合视觉线索与对话历史推断，并受含糊表达、不流畅语音和噪声环境影响；同时请求式语音未必构成对助手的真实需求，易造成误触发。本文把该问题形式化为 ODU 任务并构建基准。

## 💡 核心创新

1. 形式化 ODU 任务：检测需求是否存在并推断意图
2. 五维评测体系覆盖单轮与多轮交互
3. taxonomy 驱动的 agentic 视频生成 + 人工录制构建数据
4. 媒体锚定标注与人工验证流程
5. 揭示 MLLM 误触发率高的系统性缺陷

## 🏗️ 模型架构

本文为基准与评测工作，非新网络架构。输入为多模态交互流（用户语音、视觉画面、对话历史），要求模型先判断是否存在用户需求（demand detection），再结合视觉、声学与对话上下文推断意图。ODU-Bench 通过挑战驱动分类体系、taxonomy 引导的 agentic 视频生成与人工录制交互构建，并做媒体锚定标注与人工验证。评测对象为 14 个原生 MLLM，按五个维度打分，覆盖单轮与多轮设置。

## 📚 数据集

- ODU-Bench（评测基准，含 agentic 生成视频与人工录制交互，规模摘要未给出）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| 关键信息恢复率 | ODU-Bench | 14 个 MLLM 中多数低于该值 | **Gemini 3.1 Pro 44.7%** | 最强模型仍仅恢复 44.7% |
| 误触发率 (false-trigger rate) | ODU-Bench 非需求场景 | — | **14 个模型中 11 个 >50%** | 11/14 模型超过 50% |

摘要仅报告两项总体结果：最强模型 Gemini 3.1 Pro 在 ODU-Bench 上仅恢复 44.7% 需从视觉、声学或对话上下文推断的关键信息；14 个模型中 11 个在非需求场景的误触发率超过 50%。摘要未给出各维度细分分数、消融实验、推理延迟或跨数据集泛化结果，具体数值需查阅正文。

## 🎯 结论与影响

本文最强结论是：当前 MLLM 在生成合适回答之前，尚不能可靠理解用户真实需求，存在系统性能力缺口。该基准可能推动多模态交互研究从回答质量转向需求推断与误触发抑制，对语音助手、智能座舱等工业落地意味着需在需求检测环节单独设计与评测。

## ⚠️ 局限与未解决问题

作为基准论文，摘要未披露数据规模、标注一致性指标与各维度细分结果；agentic 生成视频与人工录制混合可能引入分布偏差；未报告模型推理延迟与成本；误触发率阈值设定依据不明。缺少与专门意图分类/需求检测基线的对比。

---

<div class="paper-footer"><span>评分：6.8</span><span>原始：6.8</span><a href="/audio-paper-daily/posts/2026-09-21/">← 返回 2026-09-21 速递</a></div>
