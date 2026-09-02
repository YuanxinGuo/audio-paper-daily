---
title: "Zero-Shot Respiratory Sound Classification through LLM-Augmented Audio-Text Alignment"
date: 2026-09-02T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#生物声学"]
summary: "利用医学LLM合成语义锚点，将自监督呼吸音编码器与临床术语对齐，实现零样本呼吸音分类，超越通用音频模型。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#生物声学</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#零样本学习</span> <span class="tag-pill tag-pill-soft">#对比学习</span> <span class="tag-pill tag-pill-soft">#医学LLM</span> <span class="tag-pill tag-pill-soft">#呼吸音分类</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2609.00055</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-09-02</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2609.00055" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2609.00055" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>利用医学LLM合成语义锚点，将自监督呼吸音编码器与临床术语对齐，实现零样本呼吸音分类，超越通用音频模型。
</div>

## 👥 作者与机构

Mustafa Talha \.Ilerisoy · Hung Manh Pham · Mathias Funk · Mykola Pechenizkiy · Aaqib Saeed

**机构**：埃因霍温理工大学

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合从事医学音频分析、零样本学习或对比学习的研究者。建议重点阅读方法部分（第3节）和实验部分（第4节），尤其是对比学习框架和负采样策略。可先看摘要和图表，再深入方法细节。

## 🌍 研究背景

自监督呼吸音编码器缺乏临床语义，导致零样本推理能力受限，需要大量任务特定标注数据。现有通用音频模型如CLAP和Qwen2-Audio虽具备零样本能力，但在临床诊断中表现不佳。本文旨在通过将呼吸音编码器与医学术语对齐，构建零样本基础模型，解决标注数据稀缺问题。

## 💡 核心创新

1. 利用医学LLM合成结构化报告作为语义锚点
2. 结合sigmoid对比损失与SSL目标联合训练
3. 相似度感知负采样增强病理边界
4. 实现零样本呼吸音分类，超越通用模型

## 🏗️ 模型架构

输入呼吸音音频，经自监督编码器提取特征，同时使用医学LLM生成文本描述，通过对比学习将音频特征与文本嵌入对齐到共享空间。训练采用sigmoid对比损失与编码器原生SSL目标结合，并引入相似度感知负采样。输出为分类概率，支持零样本推理。

## 📚 数据集

- 6个呼吸音数据集（评估，涵盖9项任务）
- 训练数据（未明确，可能包含自监督预训练数据）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| 零样本AUC | 6个数据集9项任务 | CLAP 51.4% | **61.3%** | +9.9% |
| 零样本AUC | 6个数据集9项任务 | Qwen2-Audio 54.9% | **61.3%** | +6.4% |
| 线性探测AUC | 6个数据集9项任务 | 全规模基线（未给出具体值） | **71.6%** | 使用43%数据达到最高 |

在6个数据集9项任务上，方法平均零样本AUC达61.3%，显著优于CLAP和Qwen2-Audio。线性探测AUC达71.6%，且仅使用全规模基线43%的数据，表明结构化语义对齐在临床诊断中优于大规模通用模型。

## 🎯 结论与影响

本文通过医学LLM增强的音频-文本对齐，成功将自监督呼吸音编码器转化为零样本基础模型，在呼吸音分类任务上超越通用音频模型。该方法为医学音频分析提供了新范式，有望减少对标注数据的依赖，推动临床诊断应用。

## ⚠️ 局限与未解决问题

摘要未提及推理延迟、模型复杂度等效率指标；未提供消融实验细节；数据集规模较小，可能限制泛化性；未与专门针对呼吸音的监督模型对比。

---

<div class="paper-footer"><span>评分：7.8</span><span>原始：7.8</span><a href="/audio-paper-daily/posts/2026-09-02/">← 返回 2026-09-02 速递</a></div>
