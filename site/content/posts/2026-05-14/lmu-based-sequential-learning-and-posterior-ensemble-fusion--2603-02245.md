---
title: "LMU-Based Sequential Learning and Posterior Ensemble Fusion for Cross-Domain Infant Cry Classification"
date: 2026-05-14T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#LMU", "#后验融合", "#婴儿哭声", "#婴儿哭声分类", "#跨域泛化"]
summary: "提出基于LMU的时序建模与后验融合框架，用于跨域婴儿哭声分类，在Baby2020和Baby Crying数据集上提升宏F1。"
ShowToc: true
---

**评分**: 6.5 / 10  ·  **分档**: 前50%  ·  **主任务**: #婴儿哭声分类  ·  **建议**: ⏳ 按需阅读

**标签**: #LMU · #后验融合 · #跨域泛化 · #婴儿哭声

[← 返回 2026-05-14 速递](/posts/2026-05-14/)  ·  [arxiv](https://arxiv.org/abs/2603.02245)  ·  [pdf](https://arxiv.org/pdf/2603.02245)

---

## 📌 一句话总结

> 提出基于LMU的时序建模与后验融合框架，用于跨域婴儿哭声分类，在Baby2020和Baby Crying数据集上提升宏F1。

## 📖 阅读建议

适合做音频事件检测或婴儿监护的研究者阅读。建议重点看§3的LMU模块和§4的融合策略，实验部分可快速浏览。若对LMU感兴趣可通读全文。

## 🧩 模型一栏概览

| 项 | 内容 |
| --- | --- |
| 应用场景 | 婴儿监护设备中的哭声原因自动分类 |
| 核心创新 | 多分支CNN融合MFCC/STFT/F0特征 · 增强型LMU替代LSTM减少参数量 · 熵门控后验融合提升跨域泛化 |
| 模型架构 | 输入多特征（MFCC, STFT, F0）→ 多分支CNN编码器 → 增强型LMU时序建模 → 熵门控后验融合 → 分类输出。参数量未提及。 |
| 数据集 | Baby2020（训练/评估） · Baby Crying（跨域评估） |
| 关键结果 | 跨域评估下宏F1提升，具体数值摘要未给出。与LSTM对比，LMU参数量更少。 |

## 🎯 与本站重点领域的关联

与本站重点领域无直接关联，但LMU时序建模和熵门控融合思路可迁移至语音增强/分离中的时序建模和域适应问题。

## 💢 毒舌点评

> 用LMU替代LSTM不算新，但熵门控融合有点意思。可惜只在两个婴儿哭声数据集上比，没和SOTA音频分类模型比，而且宏F1具体数值都不给，让人怀疑提升幅度。

## ⚠️ 局限与未解决问题

摘要未给出具体宏F1数值，无法评估提升幅度；仅与LSTM对比，未与Transformer或CNN时序模型比较；未报告模型参数量和推理延迟；数据集规模小，泛化性存疑。

## 👥 作者

<sub>Niloofar Jazaeri, Hilmi R. Dajani, Marco Janeczek, Martin Bouchard</sub>

---

评分：6.5  |  原始评分：6.5

[arxiv](https://arxiv.org/abs/2603.02245)  ·  [pdf](https://arxiv.org/pdf/2603.02245)
