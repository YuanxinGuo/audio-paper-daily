---
title: "Think2Listen: Evidence-Centric Learning For Agentic Audio Understanding With LALMS"
date: 2026-11-17T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#音频理解"]
summary: "提出以证据为中心的智能体音频理解框架，让LALM主动调用音频工具获取区分性线索并据此修正候选判断。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#音频理解</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#大音频语言模型</span> <span class="tag-pill tag-pill-soft">#工具调用智能体</span> <span class="tag-pill tag-pill-soft">#多步推理</span> <span class="tag-pill tag-pill-soft">#证据驱动学习</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2611.21083</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-11-16</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner"><div class="oc-headline"><span class="oc-pulse"></span><span class="oc-title">本论文已开源</span><span class="oc-hint">点击下方卡片直达对应资源</span></div><div class="oc-grid"><a class="oc-chip oc-chip-code" href="https://github.com/JinWang79/Think2Listen" target="_blank" rel="noopener"><span class="oc-icon">💻</span><span class="oc-text"><span class="oc-label">代码仓库</span><span class="oc-sub">JinWang79/Think2Listen</span></span></a></div></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2611.21083" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2611.21083" target="_blank" rel="noopener">📑 PDF</a><a class="rsrc rsrc-code" href="https://github.com/JinWang79/Think2Listen" target="_blank" rel="noopener">💻 代码</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出以证据为中心的智能体音频理解框架，让LALM主动调用音频工具获取区分性线索并据此修正候选判断。
</div>

## 👥 作者与机构

**Jin Wang** ¹ · Liang Lin · Kaiwen Luo · Weiliu Wang · Yuxuan Li · Zengxin Han · Gan Zhang · Jingtong Wu · … 等 2 人

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合做大音频语言模型、工具增强推理与多模态智能体的研究者阅读。建议重点看方法部分中候选状态更新与训练信用分配的机制，以及实验部分的七类音频基准对比表；若关注语音/音乐具体任务可只看对应子表。

## 🌍 研究背景

大音频语言模型已能覆盖语音、声音与音乐的理解，工具型智能体通过调用预定义音频工具进一步扩展能力。但现有方法存在感知与推理之间的鸿沟：模型能识别听到什么，却难以判断哪些声学线索能消解不确定决策。已有工具调用智能体多为一次性调用或固定流程，缺乏基于观测反馈迭代修正候选判断的机制，本文即针对该问题提出证据驱动的迭代推理框架。

## 💡 核心创新

1. 以候选假设竞争驱动工具调用，主动寻求区分性声学证据
2. 利用观测引起的候选状态变化分配训练信用
3. 学习问什么、如何用证据、何时停止的迭代推理策略

## 🏗️ 模型架构

输入为音频与任务查询，主干为大型音频语言模型（LALM）智能体。框架维护一组候选判断及其状态，在每轮迭代中由LALM决定调用哪个预定义音频工具、以何种参数查询，工具返回观测后更新候选状态分布，并据此决定继续询问或终止输出。训练阶段以观测前后候选状态的变化量作为信用信号，指导工具选择与证据使用策略的学习，形成'先证据后承诺'的闭环推理。

## 📚 数据集

- 两个基准、覆盖七类音频任务（评估，具体名称摘要未给出）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| 总体准确率 | 两个音频基准（七类音频） | 对比音频智能体 | **Think2Listen** | +5.08%~+17.67% |
| 总体准确率 | 两个音频基准（七类音频） | 对应基线模型 | **Think2Listen** | +2.29%~+13.10% |

摘要报告在覆盖七类音频的两个基准上，多步音频推理总体准确率较对比音频智能体提升5.08%至17.67%，音频理解与推理总体准确率较对应基线提升2.29%至13.10%。摘要未给出具体数据集名称、逐类任务细分结果、消融实验与推理开销数据。

## 🎯 结论与影响

最强结论是：以候选状态变化为信用信号、让LALM主动寻求区分性证据，可显著提升智能体音频推理准确率。该思路为工具增强音频理解提供了可训练的迭代推理范式，对需要多步声学证据核验的落地场景（如音频问答、内容审核）有参考价值。

## ⚠️ 局限与未解决问题

摘要未披露具体基准名称与逐任务结果，缺少工具调用次数、推理延迟与训练成本等效率指标；信用分配依赖候选状态设计，候选构造方式的影响未见消融；与端到端LALM及更强工具智能体的对比完整性存疑。

## 🔗 开源资源

- **代码**：<https://github.com/JinWang79/Think2Listen>

---

<div class="paper-footer"><span>评分：6.8</span><span>原始：6.8</span><a href="/audio-paper-daily/posts/2026-11-17/">← 返回 2026-11-17 速递</a></div>
