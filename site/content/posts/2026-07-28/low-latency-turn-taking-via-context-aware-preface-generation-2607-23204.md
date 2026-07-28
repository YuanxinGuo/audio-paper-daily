---
title: "Low-Latency Turn-Taking via Context-Aware Preface Generation in a Real-World Dialogue Robot"
date: 2026-07-28T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#对话系统"]
summary: "提出两阶段增量框架，通过上下文感知的前言生成降低对话机器人响应延迟，并在真实购物中心导览机器人上验证。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#对话系统</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#语音交互</span> <span class="tag-pill tag-pill-soft">#大语言模型</span> <span class="tag-pill tag-pill-soft">#低延迟</span> <span class="tag-pill tag-pill-soft">#机器人</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2607.23204</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-07-28</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2607.23204" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2607.23204" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出两阶段增量框架，通过上下文感知的前言生成降低对话机器人响应延迟，并在真实购物中心导览机器人上验证。
</div>

## 👥 作者与机构

**Yuki Okafuji** ¹ · Koji Inoue · Yoshiki Ohira

**机构**：京都大学

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合对话系统、语音交互领域的研究者。重点看§3两阶段框架设计和§4现场实验设置。可先看表1的延迟指标对比。

## 🌍 研究背景

基于LLM的对话系统通常等待完整ASR结果后才生成回复，导致响应延迟。现有方案如固定填充语虽简单但随时间变得不自然。本文旨在通过预测用户意图提前生成上下文相关的前言，同时利用语音活动投影模型决定发言时机，以平衡自然性和低延迟。

## 💡 核心创新

1. 两阶段增量框架：前言生成与语音输出解耦
2. 意图就绪检测器触发LLM生成上下文前言
3. VAP模型动态决定发言时机
4. 真实购物中心现场实验验证

## 🏗️ 模型架构

输入用户语音流 → 意图就绪检测器（基于ASR部分结果）判断用户意图是否可预测 → 触发LLM生成简短前言（如“好的，我来指路”）→ VAP模型（基于语音活动投影）预测用户停顿时机 → 输出前言语音。主回复仍由完整ASR触发。

## 📚 数据集

- 购物中心导览对话数据（现场收集，用于评估）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| 初始响应延迟 | 购物中心现场实验 | 无填充：约2.1s | **上下文前言：约1.3s** | -0.8s |
| 初始到主回复间隔 | 购物中心现场实验 | 固定填充：约2.5s | **上下文前言：约1.8s** | -0.7s |

现场实验表明，上下文前言相比无填充显著降低初始响应延迟（约0.8s），但比固定填充略长；然而上下文前言显著缩短了初始到主回复的间隔（约0.7s）。用户主观评分无显著差异，表明存在时序权衡。

## 🎯 结论与影响

本文证明通过上下文感知前言生成可有效降低对话机器人响应延迟，同时保持自然性。该框架为低延迟语音交互提供了新思路，但需进一步优化前言与主回复的衔接。对工业落地有参考价值，尤其适用于需要快速响应的服务机器人。

## ⚠️ 局限与未解决问题

现场实验样本量有限（未报告具体人数），主观评分无显著差异可能因统计功效不足。未对比其他预测性生成方法（如流式ASR+部分生成）。VAP模型依赖语音活动投影，在嘈杂环境可能失效。

---

<div class="paper-footer"><span>评分：6.5</span><span>原始：6.5</span><a href="/audio-paper-daily/posts/2026-07-28/">← 返回 2026-07-28 速递</a></div>
