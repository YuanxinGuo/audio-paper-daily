---
title: "Speaker Verification with Speech-Aware LLMs: Evaluation and Augmentation"
date: 2026-06-18T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#说话人确认"]
summary: "提出一种协议评估语音感知LLM的说话人区分能力，并通过注入ECAPA-TDNN嵌入和LoRA微调实现接近专用系统的说话人确认性能。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#说话人确认</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#大语言模型</span> <span class="tag-pill tag-pill-soft">#说话人嵌入</span> <span class="tag-pill tag-pill-soft">#ECAPA-TDNN</span> <span class="tag-pill tag-pill-soft">#LoRA</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2603.10827</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-06-18</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2603.10827" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2603.10827" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出一种协议评估语音感知LLM的说话人区分能力，并通过注入ECAPA-TDNN嵌入和LoRA微调实现接近专用系统的说话人确认性能。
</div>

## 👥 作者与机构

**Thomas Thebaud** ¹ · Yuzhe Wang · Laureano Moro-Velazquez · Jesus Villalba-Lopez · Najim Dehak

**机构**：约翰霍普金斯大学

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合说话人确认和语音LLM交叉领域的研究者。建议重点阅读§3的评分协议和§4的ECAPA-LLM架构。可先看表1和表2了解性能对比。

## 🌍 研究背景

语音感知大语言模型（LLMs）能接受语音输入，但其训练目标主要强调语言内容或特定领域（如情感、性别），是否编码说话人身份尚不明确。现有评估方法缺乏统一协议，且LLMs在说话人确认任务上表现未知。本文旨在评估现有模型并提升其说话人区分能力。

## 💡 核心创新

1. 提出模型无关的评分协议，利用Yes/No token概率生成连续确认分数
2. 轻量级增强方法：注入冻结的ECAPA-TDNN嵌入，仅训练LoRA适配器
3. ECAPA-LLM在VoxCeleb1-E上达到1.03% EER，接近专用ASV系统

## 🏗️ 模型架构

输入语音经ECAPA-TDNN提取说话人嵌入（冻结），通过可学习的投影层映射到LLM的嵌入空间，与文本token嵌入拼接后输入TinyLLaMA-1.1B。仅训练LoRA适配器和投影层，保持LLM主干冻结。输出为Yes/No token的对数似然比作为确认分数。

## 📚 数据集

- VoxCeleb1（评估，含E、H、O测试集）
- VoxCeleb2（训练ECAPA-TDNN嵌入提取器）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| EER (%) | VoxCeleb1-E | Qwen2-Audio (API) 约30% | **ECAPA-LLM 1.03** | -28.97% |
| EER (%) | VoxCeleb1-H | Qwen2-Audio (API) 约35% | **ECAPA-LLM 1.76** | -33.24% |

ECAPA-LLM在VoxCeleb1-E和VoxCeleb1-H上分别达到1.03%和1.76%的EER，显著优于现有语音感知LLM（EER>20%），接近专用ASV系统（如ECAPA-TDNN的0.87% EER）。消融实验验证了LoRA和投影层的有效性。

## 🎯 结论与影响

本文证明通过注入冻结的说话人嵌入和轻量级微调，LLM可具备接近专用系统的说话人确认能力，同时保留自然语言接口。该工作为语音LLM的说话人感知能力评估和增强提供了新范式，有望推动多模态身份验证应用。

## ⚠️ 局限与未解决问题

仅基于TinyLLaMA-1.1B实验，未验证更大LLM的泛化性；ECAPA-TDNN嵌入冻结可能限制联合优化；未在噪声或远场条件下评估；未报告推理延迟或计算开销。

---

<div class="paper-footer"><span>评分：7.8</span><span>原始：7.8</span><a href="/audio-paper-daily/posts/2026-06-18/">← 返回 2026-06-18 速递</a></div>
