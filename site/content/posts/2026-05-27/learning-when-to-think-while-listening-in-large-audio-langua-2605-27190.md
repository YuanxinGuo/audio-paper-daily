---
title: "Learning When to Think While Listening in Large Audio-Language Models"
date: 2026-05-27T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#语音推理控制"]
summary: "提出可学习的等待-思考-回答控制机制，优化LALM在流式语音交互中的推理时机与响应延迟。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#语音推理控制</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#大音频语言模型</span> <span class="tag-pill tag-pill-soft">#流式推理</span> <span class="tag-pill tag-pill-soft">#强化学习</span> <span class="tag-pill tag-pill-soft">#语音问答</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2605.27190</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-05-27</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2605.27190" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2605.27190" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出可学习的等待-思考-回答控制机制，优化LALM在流式语音交互中的推理时机与响应延迟。
</div>

## 👥 作者与机构

**Zhiyuan Song** ¹ · Weici Zhao · Yang Xiao · Suhao Yu · Cheng Zhu · Jiatao Gu

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合研究LALM流式推理、语音交互延迟优化的读者。建议重点阅读§3控制公式化与§4.2 DAPO奖励设计，以及表1的基准结果。可复现其控制策略思路。

## 🌍 研究背景

大音频语言模型（LALM）在流式语音交互中面临推理质量与响应速度的权衡：过早回答可能基于不完整证据，过晚回答则增加用户感知延迟。现有方法通常固定等待语音结束再推理，或简单提前回答，缺乏动态决策机制。本文受人类对话增量特性启发，提出可学习的等待-思考-回答控制，旨在优化推理时机。

## 💡 核心创新

1. 提出等待-思考-回答控制公式化框架
2. 构建对齐的等待-思考-回答轨迹数据
3. 设计六奖励DAPO优化完整轨迹
4. 在合成和真实语音基准上验证有效性

## 🏗️ 模型架构

基于Qwen2.5-Omni-7B作为基座模型。控制器接收部分音频证据，输出等待、外部化推理更新或回答的动作。训练分两阶段：先SFT对齐轨迹，再使用DAPO强化学习优化完整轨迹。奖励函数包含答案正确性、动作有效性、更新时机、延迟同步、推理质量和链一致性。

## 📚 数据集

- SRQA基准（六任务合成语音推理问答，训练/评估）
- Real Audio Bench（186条人类录音，评估跨域泛化）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| 行加权准确率 | SRQA基准 | 基线（Qwen2.5-Omni-7B）67.6% | **六奖励DAPO 70.3%** | +2.7% |
| 端点后最终思考长度 | SRQA基准 | 基线（Qwen2.5-Omni-7B） | **六奖励DAPO** | -14% |

在SRQA基准上，六奖励DAPO控制器将行加权准确率从67.6%提升至70.3%，同时减少14%的端点后最终思考长度。在真实音频基准上，SFT控制器取得最强准确率，而六奖励DAPO是唯一最终思考长度低于基线的学习变体，表明其跨域泛化能力。

## 🎯 结论与影响

本文证明流式LALM应学习在音频流中何时进行中间推理。所提控制机制在合成和真实数据上均能提升准确率并降低延迟，为实时语音交互系统提供了新范式。未来可探索更复杂的动作空间和端到端训练。

## ⚠️ 局限与未解决问题

实验仅在单一基座模型上验证；真实音频基准规模较小（186条）；未报告推理延迟的具体数值；控制器的泛化性在更复杂场景（如噪声、多说话人）未测试。

---

<div class="paper-footer"><span>评分：7.8</span><span>原始：7.8</span><a href="/audio-paper-daily/posts/2026-05-27/">← 返回 2026-05-27 速递</a></div>
