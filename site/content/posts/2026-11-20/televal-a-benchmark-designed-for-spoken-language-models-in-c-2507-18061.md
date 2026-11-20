---
title: "TELEVAL: A Benchmark Designed for Spoken Language Models in Chinese Interactive Scenarios"
date: 2026-11-20T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#语音交互评测"]
summary: "提出TELEVAL，一个面向中文口语交互的SLM评测基准，从内容可靠性与交互适当性两方面诊断模型缺陷。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#语音交互评测</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#语音语言模型</span> <span class="tag-pill tag-pill-soft">#基准测试</span> <span class="tag-pill tag-pill-soft">#中文口语交互</span> <span class="tag-pill tag-pill-soft">#对话系统</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2507.18061</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-11-20</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2507.18061" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2507.18061" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出TELEVAL，一个面向中文口语交互的SLM评测基准，从内容可靠性与交互适当性两方面诊断模型缺陷。
</div>

## 👥 作者与机构

**Zehan Li** ¹ · Hongjie Chen · Qing Wang · Yuxin Zhang · Jing Zhou · Hang Lv · Mengjie Du · Yaodong Song · … 等 4 人

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合做口语对话系统、SLM评测的研究者与产品团队阅读。建议通读，重点看基准构建方法（数据来源与任务设计）与'Caption Trap'失败模式分析部分；若关注中文场景，可先看方言与文化类问题的实验表格。

## 🌍 研究背景

现有SLM评测多聚焦语义任务完成度（如ASR、QA准确率），但高分不代表交互可靠自然。此前基准多依赖任务提示与预设选项，难以反映真实口语交互中的声学与语用挑战。本文要解决的是：如何在没有任务提示和选项的条件下，系统评估中文口语交互的内容可靠性与交互适当性。

## 💡 核心创新

1. 构建无任务提示、无预设选项的中文口语交互评测基准
2. 提出内容可靠性与交互适当性双维度评测框架
3. 揭示并命名'Caption Trap'失败模式
4. 覆盖方言、文化等本地化挑战场景

## 🏗️ 模型架构

TELEVAL为评测基准而非模型架构。其设计为：输入真实口语音频（含不同声学与语言条件），直接要求SLM生成自由文本回复，不提供任务提示或候选答案；随后从两个维度评分——可靠内容满足度（语义准确性，覆盖标准普通话、方言、文化类问题等条件）与交互适当性（对话自然度、对听觉线索的适应）。评测对象为现有SLM，通过人工或自动评分对比不同模型表现。

## 📚 数据集

- TELEVAL中文口语交互基准（评估，含多声学与语言条件）

## 📊 实验结果

摘要未给出具体数值指标，仅以定性方式报告：模型在事实问答数据集上的强表现不能稳定迁移到本地文化知识与方言语音等挑战条件；模型即使识别出听觉线索也难以据此调整回复；并观察到'Caption Trap'现象，即模型描述感知到的声音而非回应用户需求。

## 🎯 结论与影响

最强结论是：现有SLM在中文口语交互中难以同时保证内容准确与交互适当，事实问答高分具有误导性。该基准为SLM诊断提供双维度框架，可能推动后续研究关注声学线索适应与语用适当性；对工业落地意味着口语助手需专门优化交互自然度而非仅追求任务准确率。

## ⚠️ 局限与未解决问题

作为基准论文，摘要未报告评分者间一致性、自动评分与人工评分相关性，也未给出模型规模与推理成本对比；基准覆盖范围与题目数量未说明，存在构建偏差风险；'Caption Trap'的量化比例缺失。

---

<div class="paper-footer"><span>评分：6.8</span><span>原始：6.8</span><a href="/audio-paper-daily/posts/2026-11-20/">← 返回 2026-11-20 速递</a></div>
