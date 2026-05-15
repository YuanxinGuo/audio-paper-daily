---
title: "TiCo: Time-Controllable Spoken Dialogue Model"
date: 2026-05-15T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#基准测试", "#强化学习", "#时间可控", "#语音对话模型", "#语音生成"]
summary: "提出TiCo，通过语音时间标记和强化学习实现对话语音时长可控，在TiCo-Bench上时长误差降低2.7倍。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#语音对话模型</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#时间可控</span> <span class="tag-pill tag-pill-soft">#语音生成</span> <span class="tag-pill tag-pill-soft">#强化学习</span> <span class="tag-pill tag-pill-soft">#基准测试</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2603.22267</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-05-15</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">🔥 强烈推荐通读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2603.22267" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2603.22267" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出TiCo，通过语音时间标记和强化学习实现对话语音时长可控，在TiCo-Bench上时长误差降低2.7倍。
</div>

## 👥 作者与机构

**Kai-Wei Chang** ¹ · Wei-Chih Chen · En-Pei Hu · Hung-yi Lee · James Glass

**机构**：麻省理工 · 台湾大学

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合语音对话系统、交互式AI研究者。建议通读，重点看§3（Spoken Time Markers）和§4（强化学习训练）。可复现其方法用于自己的对话系统。

## 🌍 研究背景

现有语音对话模型能生成自然语音，但缺乏时间感知能力，无法遵循时长指令（如“生成约15秒的回复”）。这在语音助手等实际应用中很重要，但开源和商业模型均难以满足显式时间约束。本文提出TiCo，通过语音时间标记（STM）让模型在生成过程中感知已用时间并调整剩余内容，以达成目标时长。

## 💡 核心创新

1. 提出Spoken Time Markers (STM) 嵌入生成过程
2. 无需问答配对数据，基于自生成和强化学习后训练
3. 构建首个时间可控指令跟随基准TiCo-Bench

## 🏗️ 模型架构

输入为文本指令和对话历史，主干为预训练语音对话模型（如VALL-E或类似）。在生成过程中，每隔固定帧数插入STM标记（如<10.6 seconds>），这些标记由时间编码器产生，帮助模型感知已用时间。模型通过自回归方式生成语音token和STM标记。后训练阶段使用强化学习（PPO）优化，奖励函数基于时长误差和语音质量。输出为可控时长的语音波形。

## 📚 数据集

- TiCo-Bench（评估，包含多种时长指令的对话场景）
- 未明确指定训练数据集，但基于公开语音对话数据

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| Duration Error (秒) | TiCo-Bench | Backbone (未说明具体值) | **比Backbone降低2.7倍** | -2.7x |
| Duration Error (秒) | TiCo-Bench | 最强基线 (未说明具体值) | **比最强基线降低1.6倍** | -1.6x |

TiCo在TiCo-Bench上时长误差比其骨干模型降低2.7倍，比最强基线降低1.6倍，同时保持响应质量。消融实验验证了STM和强化学习的有效性。

## 🎯 结论与影响

TiCo首次实现了语音对话模型的时长可控，通过语音时间标记和强化学习后训练，显著提升时间指令跟随能力。该工作为交互式语音系统提供了实用方案，有望推动语音助手等应用更自然的交互。

## ⚠️ 局限与未解决问题

未报告推理延迟和参数量；STM标记可能影响语音自然度；仅评估了时长控制，未考虑其他时间属性（如语速）；基线对比不够详细（未给出具体数值）。

---

<div class="paper-footer"><span>评分：8.2</span><span>原始：8.2</span><a href="/audio-paper-daily/posts/2026-05-15/">← 返回 2026-05-15 速递</a></div>
