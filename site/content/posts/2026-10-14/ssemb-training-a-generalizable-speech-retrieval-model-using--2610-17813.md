---
title: "SSEmb: Training a Generalizable Speech Retrieval Model Using Only Automatic Speech Recognition Data"
date: 2026-10-14T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#语音检索"]
summary: "用ASR语料的语音-文本对训练轻量适配器，将冻结语音编码器输出投影到冻结文本嵌入空间，实现可泛化的语音检索。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#语音检索</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#语音检索</span> <span class="tag-pill tag-pill-soft">#跨模态对齐</span> <span class="tag-pill tag-pill-soft">#语音表征</span> <span class="tag-pill tag-pill-soft">#参数高效微调</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2610.17813</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-10-13</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2610.17813" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2610.17813" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>用ASR语料的语音-文本对训练轻量适配器，将冻结语音编码器输出投影到冻结文本嵌入空间，实现可泛化的语音检索。
</div>

## 👥 作者与机构

**Sangkwon Park** ¹ · Dongwook Lee · Youngho Cho · Donghun Kang · Heeseung Kim · Sungroh Yoon

**机构**：首尔大学

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合做语音检索、跨模态对齐、参数高效微调的研究者与工程团队阅读。建议通读，重点看适配器结构设计、损失函数消融（§4）以及跨任务迁移实验（TTS/TTS检索）。若关注落地，可先看推理延迟对比表。

## 🌍 研究背景

端到端语音到文本检索是语音助手的重要能力，但训练通常依赖大规模语音-文档对，采集成本高且跨域跨语言扩展困难。现有方案多为级联ASR再检索，延迟高且受ASR错误传播影响；公开语音嵌入模型在检索任务上表现有限。本文希望仅用标准ASR语料中的语音-转写对，训练一个可泛化的语音检索模型，避免任务特定监督。

## 💡 核心创新

1. 用ASR语音-转写对替代任务特定语音-文档对做监督
2. 轻量适配器将冻结语音编码器投影到冻结文本嵌入空间
3. 无需额外训练即可迁移到TTS与S2S检索
4. 系统消融损失函数与可训练模块给出实践指南

## 🏗️ 模型架构

输入为语音波形，经冻结的语音编码器提取帧级或话语级表征；轻量适配器（具体结构摘要未详述）将该表征投影到冻结预训练文本嵌入模型的检索空间，与对应转写文本的嵌入做对齐训练。输出为与文本嵌入同维的语音嵌入，可直接用于最近邻检索。训练仅更新适配器参数，语音编码器与文本编码器均冻结，参数量与计算开销低。

## 📚 数据集

- 标准ASR语料（训练，具体名称摘要未给出）

## 📊 实验结果

摘要未给出具体数值指标，仅定性说明：SSEmb与级联ASR再检索系统竞争力相当且推理延迟更低，优于现有公开语音嵌入模型；无需额外训练即可迁移到TTS检索与S2S检索；控制实验表明对训练数据减少具有鲁棒性，语料增大带来一致增益；损失函数与可训练模块消融给出实践建议。

## 🎯 结论与影响

最强结论是仅用ASR语音-转写对即可训练出有竞争力的通用语音检索模型，并具备跨任务迁移能力。这为语音检索的数据瓶颈提供了低成本路径，可能推动后续研究转向利用现成ASR语料做跨模态对齐。工业上可降低语音助手检索系统的训练与推理成本。

## ⚠️ 局限与未解决问题

摘要未给出具体数据集名称、指标数值与参数量，实验可复现性信息不足；未说明适配器具体结构；缺少与更多强语音嵌入模型的定量对比；未报告跨语言泛化结果；模型权重与代码仅称'将发布'，当前无法验证。

---

<div class="paper-footer"><span>评分：6.8</span><span>原始：6.8</span><a href="/audio-paper-daily/posts/2026-10-14/">← 返回 2026-10-14 速递</a></div>
