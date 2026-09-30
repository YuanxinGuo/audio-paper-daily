---
title: "MultiTalk: Scaling Full-Duplex Speech Models to Long, Multi-Party, Bilingual Conversation"
date: 2026-09-30T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#语音对话系统"]
summary: "构建57.6k小时中英多方全双工对话数据与MultiTalkBench基准，训练Moshi式模型实现长时多方双语对话。"
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
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#全双工语音对话</span> <span class="tag-pill tag-pill-soft">#多方对话</span> <span class="tag-pill tag-pill-soft">#长上下文建模</span> <span class="tag-pill tag-pill-soft">#双语语音</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2609.36903</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-09-30</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner"><div class="oc-headline"><span class="oc-pulse"></span><span class="oc-title">本论文已开源</span><span class="oc-hint">点击下方卡片直达对应资源</span></div><div class="oc-grid"><a class="oc-chip oc-chip-hf" href="https://huggingface.co/datasets/MultiTalk/MultiTalkPT" target="_blank" rel="noopener"><span class="oc-icon">🤗</span><span class="oc-text"><span class="oc-label">HuggingFace</span><span class="oc-sub">🤗 datasets/MultiTalk/MultiTalkPT</span></span></a></div></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2609.36903" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2609.36903" target="_blank" rel="noopener">📑 PDF</a><a class="rsrc rsrc-hf" href="https://huggingface.co/datasets/MultiTalk/MultiTalkPT" target="_blank" rel="noopener">🤗 HuggingFace</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>构建57.6k小时中英多方全双工对话数据与MultiTalkBench基准，训练Moshi式模型实现长时多方双语对话。
</div>

## 👥 作者与机构

**Ke Wang** ¹ · Houxing Ren · Zimu Lu · Yunqiao Yang · Zhuofan Zong · Mingjie Zhan · Hongsheng Li

**机构**：香港中文大学

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合做全双工语音对话、多方交互建模的研究者与工程团队阅读。建议重点看数据合成流水线（如何控制轮次、重叠、插话、指称转移）与MultiTalkBench的探针设计，§3数据构造与§4实验表格值得通读；若只关心建模，可先看模型扩展部分与长上下文鲁棒性消融。

## 🌍 研究背景

全双工语音模型（以Moshi为代表）已让开源机器对话接近自然人机交互，但现有系统在长上下文鲁棒性与多方交互两个维度上受限。会议、小组课、接待机器人等场景要求单模型在长时间内跟踪、上下文化并回应多个说话人。进展受数据与评测双重制约：开源多方语音语料规模小且非为codec帧级全双工建模设计，长音频基准偏被动聆听，语音到语音基准多为短时双人对话。

## 💡 核心创新

1. 发布57.6k小时中英长时多方全双工合成对话数据，可控长度/人数/轮次/重叠/插话
2. 提出MultiTalkBench，基于真实录音，平均32.6分钟，含长程实体跟踪与话题连贯探针
3. 在Moshi范式上联合扩展长时程与多方轴，训练双语全双工模型
4. 支持addressee shifts与long-range coreference等细粒度交互现象

## 🏗️ 模型架构

沿用Moshi式全双工架构：输入为双通道codec帧级语音流（用户与系统并行），主干为流式自回归Transformer，配合语义-声学双码本token预测，实现边听边说。模型在中英双语数据上训练，需同时处理多说话人轮次、重叠与插话，输出为连续的语音token序列。摘要未给出具体参数量与层数配置，仅说明为Moshi-style双语模型，并在MultiTalkBench上对比Moshi、MiniCPM-o-4.5、Qwen3-Omni-30B-A3B-Instruct。

## 📚 数据集

- MultiTalkPT（预训练，57.6k小时合成中英多方全双工对话）
- MultiTalkFT（微调，合成多方全双工对话）
- MultiTalkBench（评估，真实人类录音，平均32.6分钟，含长程实体跟踪/话题连贯/指称选择探针）

## 📊 实验结果

摘要仅声明模型在MultiTalkBench上显著优于Moshi、MiniCPM-o-4.5与Qwen3-Omni-30B-A3B-Instruct，但未给出任何具体指标数值（如WER、MOS、响应延迟或探针准确率），也未报告消融实验、推理效率或跨语言泛化数据，因此无法量化对比。

## 🎯 结论与影响

本文最强结论是：通过大规模可控合成数据与真实录音基准，Moshi式全双工模型可扩展到长时、多方、中英双语对话并超越现有开源基线。这为全双工对话研究提供了数据与评测基础设施，可能推动会议助手、社交机器人等长时多方交互的工业落地。

## ⚠️ 局限与未解决问题

训练数据以合成为主，与真实多方对话的声学与语用分布可能存在偏差；MultiTalkBench虽基于真实录音但规模与语言覆盖有限。摘要未报告推理延迟、显存占用与实时因子，也未给出与基线的逐项指标对比和消融，难以判断各设计（数据规模、探针、双语）的独立贡献。

## 🔗 开源资源

- **HuggingFace**：<https://huggingface.co/datasets/MultiTalk/MultiTalkPT>
- **数据集**：<https://huggingface.co/datasets/MultiTalk/MultiTalkPT>
- **数据集**：<https://huggingface.co/datasets/MultiTalk/MultiTalkFT>
- **数据集**：<https://huggingface.co/datasets/MultiTalk/MultiTalkBench>

---

<div class="paper-footer"><span>评分：7.8</span><span>原始：7.8</span><a href="/audio-paper-daily/posts/2026-09-30/">← 返回 2026-09-30 速递</a></div>
