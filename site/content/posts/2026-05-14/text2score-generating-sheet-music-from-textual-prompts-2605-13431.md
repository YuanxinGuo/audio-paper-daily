---
title: "Text2Score: Generating Sheet Music From Textual Prompts"
date: 2026-05-14T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#ABC记谱法", "#LLM规划", "#乐器分离", "#文本到乐谱", "#符号音乐生成"]
summary: "提出两阶段框架Text2Score，先用LLM规划乐谱属性，再生成ABC记谱法，无需文本-乐谱配对数据。"
ShowToc: true
---

**评分**: 8.2 / 10  ·  **分档**: 前25%  ·  **主任务**: #乐器分离  ·  **建议**: ⏳ 按需阅读

🎯 **本站重点关注领域** · 评分已 +1


**标签**: #符号音乐生成 · #文本到乐谱 · #ABC记谱法 · #LLM规划

[← 返回 2026-05-14 速递](/posts/2026-05-14/)  ·  [arxiv](https://arxiv.org/abs/2605.13431)  ·  [pdf](https://arxiv.org/pdf/2605.13431)

---

## 📌 一句话总结

> 提出两阶段框架Text2Score，先用LLM规划乐谱属性，再生成ABC记谱法，无需文本-乐谱配对数据。

## 📖 阅读建议

适合做音乐生成、符号音乐或乐器分离的研究者。建议重点读§3两阶段设计、§4评估框架和表2/3的对比结果。可跳过§2相关工作。

## 🧩 模型一栏概览

| 项 | 内容 |
| --- | --- |
| 应用场景 | 从自然语言描述生成可演奏的乐谱，适用于音乐创作辅助。 |
| 核心创新 | 两阶段规划-执行框架 · 从XML直接获取监督信号，避免文本-乐谱配对 · 引入LLM作为规划器生成结构化音乐属性 |
| 模型架构 | 输入文本提示 → LLM规划器（如GPT-4）生成度量级计划（乐器、调号、拍号、和声等） → 执行阶段生成模型（基于Transformer）输出ABC记谱法。参数量未提及。 |
| 数据集 | WikiMusicXML（训练，含XML乐谱） · 自建评估集（含文本提示和人工标注） |
| 关键结果 | 在客观指标（playability, readability, instrument utilization, structural complexity, prompt adherence）和主观专家评分上均优于纯LLM基线和三个端到端基线。具体数值摘要未给出。 |

## 🎯 与本站重点领域的关联

与乐器分离领域有间接关联：生成的乐谱可视为音乐源分离的参考或先验。但本文主要关注符号音乐生成，而非音频分离。

## 💢 毒舌点评

> 想法不错，用LLM做规划器挺时髦，但执行阶段还是老套的Transformer生成ABC，而且没和任何音频生成模型比，只在符号域自嗨。

## ⚠️ 局限与未解决问题

未与音频域生成模型对比；执行阶段生成模型细节不足；评估集规模小；LLM规划器可能引入额外延迟和成本。

## 👥 作者

<sub>Keshav Bhandari, Sungkyun Chang, Abhinaba Roy, Francesca Ronchini, Emmanouil Benetos, Dorien Herremans, Simon Colton</sub>

---

评分：8.2  |  原始评分：7.2  |  +1 重点领域加权

[arxiv](https://arxiv.org/abs/2605.13431)  ·  [pdf](https://arxiv.org/pdf/2605.13431)
