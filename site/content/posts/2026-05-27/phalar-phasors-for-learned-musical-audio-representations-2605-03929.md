---
title: "PHALAR: Phasors for Learned Musical Audio Representations"
date: 2026-05-27T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#音乐信息检索"]
summary: "提出PHALAR对比学习框架，利用复值谱池化层实现音高和相位等变，在茎检索任务上以更少参数和更快训练速度大幅超越SOTA。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero">
<div class="hero-score">
<div class="score-num">8.5</div>
<div class="score-stars">★★★★☆</div>
<div class="score-tier">前10%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#音乐信息检索</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#茎检索</span> <span class="tag-pill tag-pill-soft">#对比学习</span> <span class="tag-pill tag-pill-soft">#复值网络</span> <span class="tag-pill tag-pill-soft">#音乐表征学习</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2605.03929</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-05-27</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">🔥 强烈推荐通读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2605.03929" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2605.03929" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出PHALAR对比学习框架，利用复值谱池化层实现音高和相位等变，在茎检索任务上以更少参数和更快训练速度大幅超越SOTA。
</div>

## 👥 作者与机构

**Davide Marincione** ¹ · Michele Mancusi · Giorgio Strano · Luca Cerovaz · Donato Crisostomi · Roberto Ribuoli · Emanuele Rodol\`a

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合音乐信息检索、音频表征学习方向的研究者。建议通读，重点看§3的模型架构和§4的实验结果，特别是表1-3的检索性能对比。

## 🌍 研究背景

茎检索（stem retrieval）旨在从音频混合中匹配缺失的乐器茎，现有方法多丢弃时间信息，性能有限。此前SOTA模型参数量大、训练慢，且缺乏对音高和相位等音乐结构的不变性建模。本文提出PHALAR，通过复值谱池化和对比学习，在保持参数高效的同时显著提升检索准确率。

## 💡 核心创新

1. 引入复值谱池化层实现音高和相位等变
2. 对比学习框架结合复值头部网络
3. 7倍训练加速且参数量减少50%以上
4. 零样本节拍跟踪和线性和弦探测验证表征鲁棒性

## 🏗️ 模型架构

输入为对数梅尔谱，经可学习的复值谱池化层（Learned Spectral Pooling）提取等变特征，再通过复值头部网络（complex-valued head）映射到嵌入空间。对比学习框架使用正负样本对训练，输出为茎嵌入向量。整体参数量小于SOTA的50%，训练速度提升7倍。

## 📚 数据集

- MoisesDB（训练/评估，包含多种乐器茎）
- Slakh（训练/评估，合成音乐混合物）
- ChocoChorales（评估，合唱音乐茎）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| 检索准确率（相对提升） | MoisesDB | SOTA模型（未指名具体值） | **相对提升≈70%** | +70% |

在MoisesDB、Slakh和ChocoChorales三个数据集上，PHALAR均达到新的SOTA检索性能，相对准确率提升最高约70%。消融实验验证了复值谱池化和复值头部的有效性。零样本节拍跟踪和线性和弦探测表明模型捕获了鲁棒的音乐结构，且与人类一致性判断的相关性显著高于语义基线。

## 🎯 结论与影响

PHALAR通过复值等变对比学习，在茎检索任务上以更少参数和更快训练速度大幅超越SOTA，并展现出对音乐结构的鲁棒表征能力。该工作为音乐信息检索提供了高效且可解释的新范式，有望推动实际应用中的茎检索和音乐理解系统。

## ⚠️ 局限与未解决问题

未报告推理延迟和参数量具体数值；对比基线未列出所有SOTA方法的具体指标；仅评估了检索任务，未在分离或生成任务上验证；数据集均为合成或受限场景，真实录音泛化性未知。

---

<div class="paper-footer"><span>评分：8.5</span><span>原始：8.5</span><a href="/audio-paper-daily/posts/2026-05-27/">← 返回 2026-05-27 速递</a></div>
