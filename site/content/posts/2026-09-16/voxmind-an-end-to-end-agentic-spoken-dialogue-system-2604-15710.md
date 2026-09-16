---
title: "VoxMind: An End-to-End Agentic Spoken Dialogue System"
date: 2026-09-16T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#语音对话系统"]
summary: "VoxMind 为端到端语音对话模型引入工具调用能力，通过 Think-before-Speak 与多智能体动态工具管理，任务完成率从 34.88% 提升至 74.57%。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#语音对话系统</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#端到端语音对话</span> <span class="tag-pill tag-pill-soft">#工具调用</span> <span class="tag-pill tag-pill-soft">#多智能体</span> <span class="tag-pill tag-pill-soft">#语音大模型</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2604.15710</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-09-16</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner"><div class="oc-headline"><span class="oc-pulse"></span><span class="oc-title">本论文已开源</span><span class="oc-hint">点击下方卡片直达对应资源</span></div><div class="oc-grid"><a class="oc-chip oc-chip-code" href="https://github.com/MM-Speech/VoxMind" target="_blank" rel="noopener"><span class="oc-icon">💻</span><span class="oc-text"><span class="oc-label">代码仓库</span><span class="oc-sub">MM-Speech/VoxMind</span></span></a></div></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2604.15710" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2604.15710" target="_blank" rel="noopener">📑 PDF</a><a class="rsrc rsrc-code" href="https://github.com/MM-Speech/VoxMind" target="_blank" rel="noopener">💻 代码</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>VoxMind 为端到端语音对话模型引入工具调用能力，通过 Think-before-Speak 与多智能体动态工具管理，任务完成率从 34.88% 提升至 74.57%。
</div>

## 👥 作者与机构

**Tianle Liang** ¹ · **Yifu Chen** ¹ · Shengpeng Ji · Yijun Chen · Zhiyang Jia · Jingyu Lu · Fan Zhuo · Xueyi Pu · … 等 2 人

**机构**：浙江大学

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合做语音对话系统、语音大模型与 agent 工具调用的研究者阅读。建议通读，重点看 §3 的 Think-before-Speak 机制与多智能体动态工具管理架构，以及表 2 的任务完成率对比。若关注低延迟部署，优先看延迟解耦实验部分。

## 🌍 研究背景

端到端语音对话模型已能实现自然交互，但面对复杂用户需求时，仅靠对话能力难以扩展知识边界与完成实际任务。现有研究多聚焦于语音感知与生成，对工具增强的 agentic 扩展探索有限。本文要解决的核心问题是：如何让端到端语音对话模型具备完整的工具调用与规划能力，同时避免大规模工具集成带来的推理延迟瓶颈。

## 💡 核心创新

1. 提出 Think-before-Speak 机制，将结构化推理内化为规划与回复生成的前置步骤
2. 构建 470 小时 AgentChat 数据集，覆盖工具调用与推理对话场景
3. 设计多智能体动态工具管理架构，异步委派检索任务解耦延迟与工具集规模

## 🏗️ 模型架构

VoxMind 以端到端语音对话模型为基座，输入为用户语音，经语音编码器与主干对话模型处理。核心模块包括：Think-before-Speak 推理模块，在生成回复前先输出结构化思考；多智能体动态工具管理架构，主模型推理轨迹对齐一个辅助 agent，由辅助 agent 异步执行检索与工具调用，从而将推理延迟与工具集大小解耦。输出为语音回复与工具调用结果。摘要未给出具体参数量。

## 📚 数据集

- AgentChat（训练，470 小时）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| 任务完成率 | spoken agent tasks | 强基线 34.88% | **74.57%** | +39.69% |

摘要仅给出任务完成率从 34.88% 提升至 74.57%，并称在 spoken agent 任务上超过 Gemini-2.5-Pro，同时保持通用对话质量。未提供 SI-SDR、PESQ、WER 等语音指标，也未给出消融实验、延迟具体数值或跨数据集泛化结果。

## 🎯 结论与影响

VoxMind 证明端到端语音对话模型可通过 Think-before-Speak 与多智能体工具管理获得显著 agent 能力提升，任务完成率翻倍以上并超越 Gemini-2.5-Pro。该工作为语音对话系统的工具增强方向提供了可复现框架与数据集，对工业界构建可执行任务的语音助手有直接参考价值。

## ⚠️ 局限与未解决问题

摘要未报告推理延迟的具体数值，仅声称解耦延迟与工具集规模；缺少消融实验验证 Think-before-Speak 与多智能体架构各自的贡献；未给出通用对话质量的具体指标；AgentChat 数据集为自建，可能存在领域偏差；与 Gemini-2.5-Pro 的对比细节不足。

## 🔗 开源资源

- **代码**：<https://github.com/MM-Speech/VoxMind>

---

<div class="paper-footer"><span>评分：7.8</span><span>原始：7.8</span><a href="/audio-paper-daily/posts/2026-09-16/">← 返回 2026-09-16 速递</a></div>
