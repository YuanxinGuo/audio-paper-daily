---
title: "Mind the Divergence: Divergence-Guided Reliability-Aware Fusion and Adaptive LLM Prompting for Conversational Emotion Recognition"
date: 2026-11-09T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#情感识别"]
summary: "用单模态预测分布间的归一化散度量化模态分歧，指导门控、可靠性加权与自适应LLM提示，提升对话情感识别。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero">
<div class="hero-score">
<div class="score-num">6.8</div>
<div class="score-stars">★★★☆☆</div>
<div class="score-tier">中等</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#情感识别</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#多模态融合</span> <span class="tag-pill tag-pill-soft">#对话情感识别</span> <span class="tag-pill tag-pill-soft">#大语言模型提示</span> <span class="tag-pill tag-pill-soft">#可靠性建模</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2611.08860</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-11-09</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2611.08860" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2611.08860" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>用单模态预测分布间的归一化散度量化模态分歧，指导门控、可靠性加权与自适应LLM提示，提升对话情感识别。
</div>

## 👥 作者与机构

**Jingwen Wang** ¹ · Jiao Li · Yuhang Qian · Yuyin Wang · Min Zhang

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合做多模态情感识别与多模态融合的研究者阅读。若关注融合可靠性建模，值得通读；重点看散度分数定义、门控与可靠性加权模块，以及高分歧样本上的实验分析。可先看方法总览图与IEMOCAP/MELD主表，再核对消融。

## 🌍 研究背景

对话情感识别（MERC）融合文本、声学、视觉三模态，主流做法是Conformer/Transformer编码后直接拼接或注意力融合，代表工作多在IEMOCAP、MELD上报SOTA。但真实对话中存在语义不一致、情绪掩饰、噪声观测与歧义，各模态可靠性随样本变化， indiscriminate fusion 会传播不可靠证据。现有方法多分别处理各类不一致来源，缺少对“模态预测分歧”这一共同后果的统一建模。本文要解决的是如何按样本自适应地依据模态分歧调节融合与提示。

## 💡 核心创新

1. 用归一化散度分数统一量化单模态情感分布间的预测分歧
2. 散度引导的跨模态门控（divergence-guided cross-modal gating）
3. 散度调制的模态可靠性加权融合
4. 散度条件化的自适应LLM提示，无需冲突标签或外部检索

## 🏗️ 模型架构

输入为对话中每句的文本、声学、视觉特征，分别经单模态编码器得到各模态在统一情感标签集上的预测分布；计算归一化散度分数作为样本级分歧度量，并据此估计各模态可靠性。主干包含三部分：散度引导的跨模态门控对模态表示做选择性交互；散度调制的可靠性加权对单模态预测做加权融合；散度条件化的自适应LLM提示将分歧信号转为提示词，引导大语言模型输出。整体端到端训练，仅用标准情感标注，摘要未给出参数量。

## 📚 数据集

- IEMOCAP（训练与评估，对话级情感识别基准）
- MELD（训练与评估，多说话人对话情感识别基准）

## 📊 实验结果

摘要仅声称在IEMOCAP与MELD上达到state-of-the-art，并强调在高分歧样本上提升尤为明显，但未给出具体指标数值、对比基线名称或消融结果。因此无法量化其相对现有MERC方法的增益，也无法判断门控、可靠性加权与LLM提示各自的贡献比例。

## 🎯 结论与影响

最强结论是：以单模态预测分歧作为统一信号来协调融合与LLM提示，可在不引入额外冲突标注的情况下提升对话情感识别，且在高分歧样本上收益更大。这为多模态融合的可靠性建模提供了可复用的分歧视角，对工业对话情感分析中的噪声与不一致场景有潜在价值。

## ⚠️ 局限与未解决问题

摘要未报告具体指标与基线，难以核验SOTA声明；缺少对散度阈值、门控与提示模块的消融与敏感性分析；LLM提示带来额外推理开销但未报延迟；仅在IEMOCAP与MELD两个英文数据集验证，跨语言与跨域泛化未知；散度作为分歧代理的因果有效性仍需验证。

---

<div class="paper-footer"><span>评分：6.8</span><span>原始：6.8</span><a href="/audio-paper-daily/posts/2026-11-09/">← 返回 2026-11-09 速递</a></div>
