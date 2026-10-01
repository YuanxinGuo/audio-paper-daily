---
title: "WASIL: In-the-Wild Arabic Spoken Interactions with LLMs"
date: 2026-10-01T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#语音识别"]
summary: "发布WASIL阿拉伯语真实场景语音交互数据集，含8529轮对话与点赞/点踩反馈，并提供2000轮方言测试集与多ASR后编辑金标转录。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero">
<div class="hero-score">
<div class="score-num">6.0</div>
<div class="score-stars">★★★☆☆</div>
<div class="score-tier">中等</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#语音识别</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#语音识别</span> <span class="tag-pill tag-pill-soft">#数据集</span> <span class="tag-pill tag-pill-soft">#阿拉伯语</span> <span class="tag-pill tag-pill-soft">#LLM评估</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2605.16364</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-10-01</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2605.16364" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2605.16364" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>发布WASIL阿拉伯语真实场景语音交互数据集，含8529轮对话与点赞/点踩反馈，并提供2000轮方言测试集与多ASR后编辑金标转录。
</div>

## 👥 作者与机构

**Zien Sheikh Ali** ¹ · Hamdy Mubarak · Soon-Gyo Jung · Hunzalah Hassan Bhatti · Firoj Alam · Shammur Absar Chowdhury

**机构**：卡塔尔计算研究所

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合做阿拉伯语ASR、语音助手评测、LLM-as-judge的研究者阅读。建议重点看数据集构建流程（多ASR一致性后编辑）与可回答性标注体系，以及§测试集方言分布与多评委打分协议。若只关心建模方法可略读。

## 🌍 研究背景

级联ASR-LLM语音助手中，识别错误会扭曲用户意图，但用户点踩也可能源于问题本身歧义、超域或非请求轮次，导致ASR影响难以隔离。此前阿拉伯语缺乏真实场景、带显式反馈且区分方言的交互数据，评测多依赖合成或单一方言，无法分离内在不可回答与ASR退化。本文构建WASIL以填补该空白。

## 💡 核心创新

1. 发布8529轮真实阿拉伯语语音交互数据，含显式点赞/点踩反馈
2. 多ASR一致性引导后编辑，低成本获取金标转录
3. 四类可回答性标注，分离内在不可回答与ASR退化
4. 多评委LLM无参考打分，对比ASR与金标转录响应

## 🏗️ 模型架构

数据来自真实语音助手交互，每条含音频、ASR假设、助手响应与用户反馈。构建流程：先由多个ASR系统识别，利用一致性信号引导人工后编辑得到金标转录；再对每轮标注可回答性（answerable / ambiguous / unsupported / not-a-request）。评测侧采用多评委LLM对ASR转录与金标转录生成的响应做无参考打分，比较级联系统在不同转录质量下的表现。摘要未给出具体声学模型或参数量。

## 📚 数据集

- WASIL训练/开发集（8529轮真实阿拉伯语交互，含音频、ASR假设、响应与反馈）
- WASIL测试集（2000轮，覆盖MSA与四种主要方言，带方言标签）

## 📊 实验结果

摘要未给出具体指标数值，仅说明数据集规模（8529轮，14.2%点踩）、测试集规模（2000轮）与方言覆盖，以及采用多评委LLM无参考评分对比ASR与金标转录响应。无SI-SDR、WER、PESQ等具体结果可报告。

## 🎯 结论与影响

本文最强结论是提供了首个带显式反馈、方言标签与可回答性标注的阿拉伯语真实语音交互数据集，并给出可扩展的无参考响应评测流程。后续研究可基于该数据分离ASR与内在不可回答对用户体验的影响，工业上可用于阿拉伯语语音助手的错误归因与方言鲁棒性诊断。

## ⚠️ 局限与未解决问题

摘要未报告任何ASR或响应质量的具体指标，缺少与现有阿拉伯语数据集的定量对比；多ASR后编辑金标的质量与一致性未量化；14.2%点踩的类别分布与方言偏差未说明；无参考LLM评委的可靠性缺乏人工校验；未涉及推理延迟或成本。

---

<div class="paper-footer"><span>评分：6.0</span><span>原始：6.0</span><a href="/audio-paper-daily/posts/2026-10-01/">← 返回 2026-10-01 速递</a></div>
