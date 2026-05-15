---
title: "IndicMedDialog: A Parallel Multi-Turn Medical Dialogue Dataset for Accessible Healthcare in Indic Languages"
date: 2026-05-15T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#低资源语言", "#医疗对话", "#参数高效微调", "#多语言数据集"]
summary: "构建了一个覆盖英语和9种印度语言的平行多轮医疗对话数据集，并基于量化小语言模型微调得到IndicMedLM。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#医疗对话</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#多语言数据集</span> <span class="tag-pill tag-pill-soft">#医疗对话</span> <span class="tag-pill tag-pill-soft">#参数高效微调</span> <span class="tag-pill tag-pill-soft">#低资源语言</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2605.13292</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-05-13</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2605.13292" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2605.13292" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>构建了一个覆盖英语和9种印度语言的平行多轮医疗对话数据集，并基于量化小语言模型微调得到IndicMedLM。
</div>

## 👥 作者与机构

**Shubham Kumar Nigam** ¹ · Suparnojit Sarkar · Piyush Patel

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合从事多语言NLP、医疗对话系统或低资源语言研究的读者。建议重点阅读§3数据集构建和§4模型微调部分，以及表2的跨语言评估结果。

## 🌍 研究背景

现有医疗对话系统多基于单轮问答或模板数据集，缺乏多轮对话的真实性和多语言适用性。之前的工作如MDDial仅覆盖英语，且合成数据质量参差不齐。本文旨在构建一个高质量、多轮、多语言的医疗对话数据集，并探索在低资源印度语言上的对话系统。

## 💡 核心创新

1. 构建IndicMedDialog：平行多轮医疗对话数据集，覆盖10种语言
2. 采用TranslateGemma翻译+母语验证+脚本感知后处理流水线
3. 基于量化小语言模型的参数高效微调IndicMedLM
4. 引入可选的患者预上下文实现个性化多轮症状询问

## 🏗️ 模型架构

输入为多轮对话历史（可选患者预上下文）→ 使用量化后的Gemma-2B作为基座模型 → 通过LoRA进行参数高效微调 → 输出下一轮系统回复。模型参数量约2B，量化后显存需求低。

## 📚 数据集

- MDDial（基础数据集，英语单轮/多轮）
- IndicMedDialog（本文构建，训练/评估，含10种语言平行对话）

## 📊 实验结果

摘要未提供具体数值指标，但提到与零样本多语言基线对比，进行了跨10种语言的系统错误分析，并通过医学专家评估验证临床合理性。

## 🎯 结论与影响

IndicMedDialog数据集和IndicMedLM模型展示了在低资源印度语言上构建多轮医疗对话系统的可行性。该工作为多语言医疗对话研究提供了高质量数据资源和基线模型，有望推动印度地区可及医疗对话应用的发展。

## ⚠️ 局限与未解决问题

数据集依赖机器翻译和后处理，可能仍存在文化或术语偏差；模型仅基于2B参数量化模型，复杂医疗场景能力有限；未报告推理延迟或部署效率；缺乏与更大模型（如GPT-4）的对比。

---

<div class="paper-footer"><span>评分：7.2</span><span>原始：7.2</span><a href="/audio-paper-daily/posts/2026-05-15/">← 返回 2026-05-15 速递</a></div>
