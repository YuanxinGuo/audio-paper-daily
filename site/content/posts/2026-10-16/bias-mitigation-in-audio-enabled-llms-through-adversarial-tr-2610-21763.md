---
title: "Bias Mitigation in Audio-Enabled LLMs through Adversarial Training and Distillation Methods"
date: 2026-10-16T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#音频-语言模型公平性"]
summary: "用对抗训练让音频大模型遗忘性别感知，再用蒸馏保留感知但去除偏见响应。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#音频-语言模型公平性</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#音频大语言模型</span> <span class="tag-pill tag-pill-soft">#对抗训练</span> <span class="tag-pill tag-pill-soft">#知识蒸馏</span> <span class="tag-pill tag-pill-soft">#偏见缓解</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2610.21763</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-10-16</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2610.21763" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2610.21763" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>用对抗训练让音频大模型遗忘性别感知，再用蒸馏保留感知但去除偏见响应。
</div>

## 👥 作者与机构

**Adnan Al Ali** ¹ · Jind\v{r}ich Libovick\'y · Anne Lauscher

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合研究音频大模型公平性与对齐的读者。建议通读，重点看对抗训练目标设计与蒸馏损失部分，以及三个 AuLLM 上的性别遗忘与蒸馏结果对比表；若关注落地，可先看蒸馏模型在显式询问下的行为分析。

## 🌍 研究背景

音频大语言模型（AuLLM）可直接从语音中推断性别等副语言属性，并据此产生有偏响应。此前偏见缓解多针对文本 LLM，音频模态下的性别偏见去除研究较少。现有方法要么牺牲任务性能，要么无法在需要时保留性别感知。本文要解决：如何在不损失其他基准任务性能的前提下，让 AuLLM 遗忘性别感知，并进一步蒸馏出可保留感知但响应无偏的模型。

## 💡 核心创新

1. 用对抗训练对 AuLLM 做性别属性遗忘
2. 提出性别无关教师到学生模型的蒸馏框架
3. 在三个 AuLLM 上验证遗忘与蒸馏两阶段方法
4. 蒸馏模型仅在显式询问时才表现性别感知

## 🏗️ 模型架构

输入为语音波形经音频编码器得到的表示，接入音频大语言模型主干。第一阶段在模型内部表示上施加对抗训练，通过性别分类器与梯度反转层使编码器学得性别无关表征，同时保持原任务损失。第二阶段以性别无关模型为教师，蒸馏到学生模型，学生保留性别感知能力但输出分布对齐教师，除非提示中显式要求性别信息。摘要未给出参数量与具体网络名。

## 📊 实验结果

摘要未给出具体指标数值，仅说明在三个 AuLLM 上性别遗忘部分取得满意结果，蒸馏部分结果部分满意。未报告 SI-SDR、PESQ、WER 或公平性指标的具体数值，也未说明所用评估数据集与基线对比。

## 🎯 结论与影响

本文证明对抗训练可在不损失其他基准任务的前提下让 AuLLM 遗忘性别感知，蒸馏方法则提供一种保留感知但抑制偏见响应的折中方案。该思路可推广到其他副语言属性偏见缓解，对音频大模型公平性对齐与合规部署有参考意义。

## ⚠️ 局限与未解决问题

摘要未给出任何定量结果与数据集信息，无法判断提升幅度；蒸馏部分作者自述仅部分满意，说明方法尚不成熟；缺少与文本偏见缓解方法的对比、消融实验和推理开销分析。

---

<div class="paper-footer"><span>评分：6.0</span><span>原始：6.0</span><a href="/audio-paper-daily/posts/2026-10-16/">← 返回 2026-10-16 速递</a></div>
