---
title: "TW-Sound580K: A Regional Audio-Text Dataset with Verification-Guided Curation for Localized Audio-Language Modeling"
date: 2026-05-14T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#数据集构建", "#方言", "#语音识别", "#音频语言模型"]
summary: "构建台湾地区音频-文本指令数据集TW-Sound580K，通过验证-生成-批评协议和双ASR验证提升质量，微调DeSTA 2.5模型在TAU基准上提升6.5%准确率。"
ShowToc: true
---

**评分**: 7.2 / 10  ·  **分档**: 前25%  ·  **主任务**: #语音识别  ·  **建议**: ⏳ 按需阅读

**标签**: #音频语言模型 · #方言 · #数据集构建 · #语音识别

[← 返回 2026-05-14 速递](/posts/2026-05-14/)  ·  [arxiv](https://arxiv.org/abs/2603.05094)  ·  [pdf](https://arxiv.org/pdf/2603.05094)

---

## 📌 一句话总结

> 构建台湾地区音频-文本指令数据集TW-Sound580K，通过验证-生成-批评协议和双ASR验证提升质量，微调DeSTA 2.5模型在TAU基准上提升6.5%准确率。

## 📖 阅读建议

适合做音频语言模型、方言语音识别或数据集构建的研究者阅读。建议重点看§3数据集构建流程和§4.2动态仲裁策略，表1和表2值得细读。如果对LALM微调感兴趣，可通读全文。

## 🧩 模型一栏概览

| 项 | 内容 |
| --- | --- |
| 应用场景 | 台湾地区方言语音理解与指令跟随任务 |
| 核心创新 | Verify-Generate-Critique (VGC) 数据筛选协议 · Dual-ASR 验证过滤低质量音频 · 动态 Dual-ASR 仲裁策略优化推理 |
| 模型架构 | 基于DeSTA 2.5-Audio初始化的音频语言模型，输入音频经预训练编码器提取特征，通过语言模型解码生成文本。关键模块包括Dual-ASR验证过滤和动态仲裁策略。参数量未提及。 |
| 数据集 | TW-Sound580K（训练，台湾地区音频-文本指令对） · TAU Benchmark（评估，方言语音理解） |
| 关键结果 | 在TAU Benchmark上，Tai-LALM达到49.1%准确率，相比零样本基线（42.6%）绝对提升6.5%。摘要未给出与其他LALM的对比。 |

## 🎯 与本站重点领域的关联

与本站重点领域无直接关联，但数据集构建方法（VGC协议）可迁移至语音增强/分离任务的数据筛选，双ASR验证思路可用于提升训练数据质量。

## 💢 毒舌点评

> 数据集构建流程扎实，但提升仅6.5%且只在一个benchmark上验证，未与当前主流LALM（如SALMONN）对比，说服力有限。动态仲裁策略的消融实验缺失，难以判断贡献来源。

## ⚠️ 局限与未解决问题

仅在单一基准TAU上评估，缺乏与其他LALM的对比；动态仲裁策略的消融实验未报告；数据集规模相对较小（580K），且未公开；模型参数量和推理速度未提及，实用性存疑。

## 👥 作者

<sub>Hao-Hui Xie, Ho-Lam Chung, Yi-Cheng Lin, Ke-Han Lu, Wenze Ren, Xie Chen, Hung-yi Lee</sub>

---

评分：7.2  |  原始评分：7.2

[arxiv](https://arxiv.org/abs/2603.05094)  ·  [pdf](https://arxiv.org/pdf/2603.05094)
