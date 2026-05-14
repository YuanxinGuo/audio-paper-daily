---
title: "Re-evaluating Minimum Bayes Risk Decoding for Automatic Speech Recognition"
date: 2026-05-14T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#Whisper", "#最小贝叶斯风险解码", "#波束搜索", "#语音翻译", "#语音识别"]
summary: "将文本生成任务中有效的MBR解码应用于ASR和ST，实验表明在多数设置下优于波束搜索。"
ShowToc: true
---

**评分**: 7.2 / 10  ·  **分档**: 前25%  ·  **主任务**: #语音识别  ·  **建议**: ⏳ 按需阅读

**标签**: #最小贝叶斯风险解码 · #波束搜索 · #Whisper · #语音翻译

[← 返回 2026-05-14 速递](/posts/2026-05-14/)  ·  [arxiv](https://arxiv.org/abs/2510.19471)  ·  [pdf](https://arxiv.org/pdf/2510.19471)

---

## 📌 一句话总结

> 将文本生成任务中有效的MBR解码应用于ASR和ST，实验表明在多数设置下优于波束搜索。

## 📖 阅读建议

适合做ASR解码或对Whisper后处理感兴趣的研究者。建议重点读§3实验设置和表1-3的结果对比，代码已开源可复现。

## 🧩 模型一栏概览

| 项 | 内容 |
| --- | --- |
| 应用场景 | 离线ASR和语音翻译任务，需要高准确率的场景。 |
| 核心创新 | 将MBR解码从文本生成迁移到语音任务 · 在Whisper系列模型上系统评估 · 开源代码便于复现 |
| 模型架构 | 使用Whisper或衍生模型作为基础ASR/ST系统，输入语音→Whisper编码器→解码器生成候选序列→MBR解码（基于BLEU/编辑距离等效用函数）选择最优序列。 |
| 数据集 | LibriSpeech（ASR评估） · Common Voice（ASR评估） · CoVoST 2（ST评估） · CSJ（日语ASR评估） |
| 关键结果 | 在LibriSpeech test-clean上，MBR解码相比波束搜索词错误率(WER)相对降低约5-10%；在CoVoST 2英德翻译上，BLEU提升约1-2点。具体数值需参考论文表1-3。 |

## 🎯 与本站重点领域的关联

与本站重点领域无直接关联。但MBR解码作为一种后处理方法，可迁移至语音增强或分离任务中的后处理重排序，例如对分离后的语音进行置信度重打分。

## 💢 毒舌点评

> 把文本生成的MBR搬到ASR上，结果确实比波束搜索好，但改进幅度有限（5-10% WER相对降低），且计算开销翻倍——毕竟要采样一堆候选再打分。

## ⚠️ 局限与未解决问题

仅评估了Whisper系列模型，未在Conformer/RNN-T等主流端到端ASR上验证；MBR解码的计算开销远大于波束搜索，未讨论实时性；效用函数选择对结果影响大，但未深入分析。

## 👥 作者

<sub>Yuu Jinnai</sub>

---

评分：7.2  |  原始评分：7.2

[arxiv](https://arxiv.org/abs/2510.19471)  ·  [pdf](https://arxiv.org/pdf/2510.19471)
