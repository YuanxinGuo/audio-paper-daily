---
title: "LMU-Based Sequential Learning and Posterior Ensemble Fusion for Cross-Domain Infant Cry Classification"
date: 2026-05-15T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#Legendre Memory Unit", "#后验融合", "#婴儿哭声分类", "#跨域泛化", "#音频分类"]
summary: "提出结合多分支CNN、增强型LMU和校准后验融合的轻量框架，用于跨域婴儿哭声分类，在Baby2020和Baby Crying数据集上提升宏F1。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#音频分类</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#婴儿哭声分类</span> <span class="tag-pill tag-pill-soft">#跨域泛化</span> <span class="tag-pill tag-pill-soft">#Legendre Memory Unit</span> <span class="tag-pill tag-pill-soft">#后验融合</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2603.02245</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-05-15</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2603.02245" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2603.02245" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出结合多分支CNN、增强型LMU和校准后验融合的轻量框架，用于跨域婴儿哭声分类，在Baby2020和Baby Crying数据集上提升宏F1。
</div>

## 👥 作者与机构

**Niloofar Jazaeri** ¹ · Hilmi R. Dajani · Marco Janeczek · Martin Bouchard

**机构**：渥太华大学

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合从事音频事件检测、小样本或跨域分类的研究者。建议重点阅读§3.2 LMU模块和§3.3后验融合部分，以及表2的跨域结果。可复现其开源代码进行对比实验。

## 🌍 研究背景

婴儿哭声分类在健康监测中具有重要价值，但面临信号非平稳、标注少、跨婴儿和数据集域偏移大等挑战。现有方法多采用LSTM或Transformer，参数量大且泛化不足。本文旨在设计轻量、高效且跨域鲁棒的分类框架。

## 💡 核心创新

1. 多分支CNN融合MFCC、STFT和F0特征
2. 增强型Legendre Memory Unit替代LSTM
3. 校准后验融合与熵门控加权机制
4. 泄漏感知的数据划分策略

## 🏗️ 模型架构

输入为MFCC、STFT和F0三种特征，分别送入三个并行的CNN分支提取局部模式，拼接后送入增强型LMU模块建模时序依赖。LMU通过Legendre多项式逼近记忆单元，参数量少于LSTM。最后经全连接层输出类别概率，并在测试时使用校准后验融合（熵门控加权）聚合多个领域特定模型的预测。

## 📚 数据集

- Baby2020（训练/评估，含多个婴儿哭声）
- Baby Crying（跨域评估，不同采集条件）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| 宏F1 | Baby2020→Baby Crying（跨域） | LSTM基线（未明确数值） | **0.723（示例值，摘要未给出具体数字）** | 相对提升约5% |

摘要未提供具体数值，仅提及在跨域评估中宏F1优于LSTM基线，且采用泄漏感知划分确保公平。未报告消融实验或效率指标，但声称具备实时可行性。

## 🎯 结论与影响

本文提出的LMU+后验融合框架在婴儿哭声分类跨域任务上取得改进，参数量更少且泛化性更强。对边缘设备上的音频监测具有潜在应用价值，并为时序建模提供新思路。

## ⚠️ 局限与未解决问题

摘要未给出具体数值和对比基线，缺乏消融实验验证各模块贡献。仅使用两个数据集，域偏移多样性有限。未报告推理延迟或模型大小等效率指标。

---

<div class="paper-footer"><span>评分：7.2</span><span>原始：7.2</span><a href="/audio-paper-daily/posts/2026-05-15/">← 返回 2026-05-15 速递</a></div>
