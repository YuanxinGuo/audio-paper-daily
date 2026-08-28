---
title: "From Sound to Symptom: Real-Time Respiratory Signal Understanding for Conversational Healthcare Agents"
date: 2026-08-28T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#语音事件检测"]
summary: "HealthCUES利用多模态大模型实现对话场景中的实时咳嗽检测与分类，提供亚秒级延迟和对话感知门控，用于远程医疗。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#语音事件检测</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#咳嗽检测</span> <span class="tag-pill tag-pill-soft">#多模态大模型</span> <span class="tag-pill tag-pill-soft">#对话系统</span> <span class="tag-pill tag-pill-soft">#医疗健康</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2608.26163</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-08-28</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2608.26163" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2608.26163" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>HealthCUES利用多模态大模型实现对话场景中的实时咳嗽检测与分类，提供亚秒级延迟和对话感知门控，用于远程医疗。
</div>

## 👥 作者与机构

**Tanmay Laud** ¹ · Herprit Mahal · Subhabrata Mukherjee

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合语音交互、医疗AI和健康监测研究者阅读。建议重点阅读系统架构（第3节）和实验部分（第4节），特别是对话感知门控机制和延迟优化。可先看摘要和图表，再深入方法细节。

## 🌍 研究背景

在实时对话系统中，咳嗽等副语言事件常被视为噪声而被丢弃，但其中蕴含临床价值。现有对话系统缺乏对这类信号的实时理解能力。HealthCUES旨在填补这一空白，通过流式处理和多模态大模型实现咳嗽检测、分类和时长估计，同时避免干扰对话流程。

## 💡 核心创新

1. 滚动缓冲与对话轮次对齐，实现亚秒级事件检测
2. 细粒度咳嗽分析：区分咳嗽与清嗓，分类干/湿/犬吠/百日咳
3. 对话感知门控机制，根据上下文调节触发，减少警报疲劳
4. 利用Qwen3Omni多模态大模型，分解并行预测任务优化提示
5. 端到端延迟340ms，实时性满足对话场景需求

## 🏗️ 模型架构

HealthCUES采用流式管道，输入音频通过滚动缓冲与对话轮次对齐，送入Qwen3Omni多模态大模型。模型输出约束为结构化格式，分解为并行预测任务：咳嗽检测、咳嗽/清嗓区分、亚型分类（干/湿/犬吠/百日咳）及时间边界估计。对话感知门控根据上下文调节触发，减少误报。

## 📚 数据集

- 847段内部对话音频（训练与评估）
- AMI会议语料库（外部验证）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| F1 | 内部对话音频 | 未提及 | **0.93** | N/A |
| 加权F1 | 内部对话音频（湿/干亚型） | 未提及 | **0.75** | N/A |
| 宏F1 | AMI会议语料库 | 未提及 | **0.91** | N/A |

在内部数据上，咳嗽检测F1达93%，湿/干亚型分类加权F1为0.75，平均端到端延迟340ms。在AMI外部验证中，咳嗽、清嗓和语音分离的宏F1为0.91，表明跨场景泛化能力。用户研究证实亚型信息的临床相关性。

## 🎯 结论与影响

HealthCUES首次在对话系统中实现实时副语言呼吸监测，通过多模态大模型和对话感知门控，提供细粒度咳嗽分析，且不干扰对话。该工作为语音交互在医疗健康领域的应用开辟新方向，有望推动远程医疗和患者监测的智能化。

## ⚠️ 局限与未解决问题

摘要未提及模型参数量、训练细节和消融实验。内部数据集规模有限，可能引入偏差。未报告计算资源需求，可能影响实时部署。外部验证仅用AMI，多样性不足。

---

<div class="paper-footer"><span>评分：7.2</span><span>原始：7.2</span><a href="/audio-paper-daily/posts/2026-08-28/">← 返回 2026-08-28 速递</a></div>
