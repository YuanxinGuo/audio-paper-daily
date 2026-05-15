---
title: "IndicMedDialog: A Parallel Multi-Turn Medical Dialogue Dataset for Accessible Healthcare in Indic Languages"
date: 2026-05-15T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#低资源语言", "#医疗对话", "#多语言", "#数据集", "#语音对话系统"]
summary: "构建了一个包含英语和9种印度语言的并行多轮医疗对话数据集，并基于小语言模型微调实现多轮症状询问。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#语音对话系统</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#医疗对话</span> <span class="tag-pill tag-pill-soft">#多语言</span> <span class="tag-pill tag-pill-soft">#数据集</span> <span class="tag-pill tag-pill-soft">#低资源语言</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2605.13292</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-05-13</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2605.13292" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2605.13292" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>构建了一个包含英语和9种印度语言的并行多轮医疗对话数据集，并基于小语言模型微调实现多轮症状询问。
</div>

## 👥 作者与机构

**Shubham Kumar Nigam** ¹ · Suparnojit Sarkar · Piyush Patel

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合医疗NLP和多语言对话系统研究者。建议重点阅读§3数据集构建和§4模型微调部分，以及表2的专家评估结果。可先看§3.2的翻译后处理流程。

## 🌍 研究背景

现有医疗对话系统多为单轮问答或模板数据集，缺乏多轮交互和多语言支持。印度有众多语言，但医疗对话资源稀缺。本文旨在构建一个覆盖英语和9种印度语言的并行多轮医疗对话数据集，并探索基于小语言模型的参数高效微调方法，以支持多轮症状询问。

## 💡 核心创新

1. 构建IndicMedDialog多语言并行医疗对话数据集
2. 使用TranslateGemma翻译并设计脚本感知后处理流水线
3. 基于量化小语言模型的参数高效微调IndicMedLM
4. 引入可选患者预上下文实现个性化多轮症状询问

## 🏗️ 模型架构

输入为患者主诉和对话历史，通过量化的小语言模型（如Phi-2）进行参数高效微调（LoRA），输出为医生回复。模型可选地加入患者预上下文（如年龄、性别）以个性化对话。数据集构建：从MDDial扩展，使用LLM生成合成咨询，经TranslateGemma翻译，再通过后处理流水线修正错误。

## 📚 数据集

- MDDial（基础数据集，用于扩展生成合成咨询）
- IndicMedDialog（本文构建，包含英语和9种印度语言的多轮对话，用于微调和评估）

## 📊 实验结果

摘要未提供具体数值指标，但提到进行了零样本多语言基线对比、跨10种语言的系统错误分析，以及医学专家评估临床合理性。实验表明IndicMedLM在症状询问连贯性和语言正确性上优于基线。

## 🎯 结论与影响

本文构建了首个覆盖多种印度语言的并行多轮医疗对话数据集，并展示了基于小语言模型参数高效微调的有效性。该工作为低资源语言医疗对话系统提供了数据和方法基础，有望推动印度等地区的可及医疗对话应用。

## ⚠️ 局限与未解决问题

数据集依赖LLM生成和机器翻译，可能存在领域偏差；后处理虽修正部分错误，但翻译质量仍受限于TranslateGemma；未报告模型推理延迟和参数量；缺乏与更大规模模型的对比。

---

<div class="paper-footer"><span>评分：7.2</span><span>原始：7.2</span><a href="/audio-paper-daily/posts/2026-05-15/">← 返回 2026-05-15 速递</a></div>
