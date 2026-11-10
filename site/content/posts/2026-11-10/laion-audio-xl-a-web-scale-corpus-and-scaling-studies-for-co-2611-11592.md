---
title: "LAION-Audio-XL: A Web-Scale Corpus and Scaling Studies for Contrastive Language-Audio Pretraining"
date: 2026-11-10T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#音频文本对比学习"]
summary: "构建14.8亿条音频样本的网页级语料并做多阶段清洗，用NaFlex音频编码器研究CLAP的规模定律，发布CLAP2模型。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#音频文本对比学习</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#CLAP</span> <span class="tag-pill tag-pill-soft">#数据规模定律</span> <span class="tag-pill tag-pill-soft">#音频表示学习</span> <span class="tag-pill tag-pill-soft">#数据集构建</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2611.11592</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-11-08</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2611.11592" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2611.11592" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>构建14.8亿条音频样本的网页级语料并做多阶段清洗，用NaFlex音频编码器研究CLAP的规模定律，发布CLAP2模型。
</div>

## 👥 作者与机构

**Gijs Wijngaard** ¹ · Felix Förster · Ross Wightman · Marianna Nezhurina · Christoph Schuhmann · Jenia Jitsev · A. Sophia Koepke

**机构**：LAION

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合做音频-文本预训练、多模态检索与音频表征学习的研究者与工程团队阅读。建议通读：重点看 §3 数据清洗流水线与 caption 生成策略、§4 规模实验的计算预算-模型-数据权衡曲线，以及 MAEB/HEAR 上的对比表；数据配方部分可直接复用于自建 CLAP 训练。

## 🌍 研究背景

对比音频-语言预训练（CLAP）近年进步主要来自训练数据的规模与质量，但公开可用的音频-文本语料规模远小于图像-文本领域（如 LAION-5B），且现有数据集（AudioSet、AudioCaps 等）标注短、覆盖窄。数据瓶颈限制了 CLAP 在检索、零样本分类与下游音频任务上的泛化。本文要解决的是：如何从网页级来源构建十亿量级音频-文本语料，并系统刻画在该规模下模型与数据的缩放规律。

## 💡 核心创新

1. 构建14.8亿音频样本的多源网页级语料与多阶段清洗流水线
2. 为缺失标注样本生成短/长两种粒度的 caption
3. 基于 NaFlex 音频编码器系统研究 CLAP 的规模定律
4. 给出固定计算预算下模型尺寸与数据量的权衡结论
5. 发布 CLAP2 模型在 MAEB/HEAR 上超越同尺寸基线

## 🏗️ 模型架构

音频编码器采用 NaFlex 架构（支持可变长度/分辨率音频输入），与文本编码器做对比学习对齐。输入为音频波形经前端特征化后的表示，主干为 NaFlex 编码器输出定长音频嵌入；文本侧编码 caption 得到文本嵌入，二者在共享嵌入空间用对比损失（InfoNCE 类）训练。数据侧为多阶段清洗流水线：去重、质量过滤、语音/音乐/环境声分类、caption 生成（短 caption 与长 caption 两档）。摘要未给出具体参数量，模型按不同规模档位训练以支撑缩放实验。

## 📚 数据集

- LAION-Audio-XL（训练，14.8亿音频样本，多源网页采集）
- MAEB（评估，音频-文本对比基准）
- HEAR（评估，音频表征基准）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| 基准综合表现 | MAEB | 同尺寸先前音频-文本模型 | **CLAP2** | 优于同尺寸基线（摘要未给具体数值） |
| 基准综合表现 | HEAR | 同尺寸先前音频-文本模型 | **CLAP2** | 优于同尺寸基线（摘要未给具体数值） |

摘要仅定性说明 CLAP2 在 MAEB 与 HEAR 上超过同尺寸先前模型，未给出具体指标数值。规模实验的核心发现是：在固定计算预算下，模型尺寸与训练数据量之间存在权衡关系，即并非一味增大模型或数据都最优。摘要未报告消融细节、推理延迟或跨数据集泛化数字。

## 🎯 结论与影响

最强结论是：网页级十亿量级语料配合多阶段清洗与 caption 补全，能显著提升 CLAP 的表征质量，且规模扩展存在可刻画的计算-模型-数据权衡。该工作为音频-文本预训练提供了可复用的数据配方与缩放经验，对工业界构建通用音频检索与零样本音频分类系统有直接参考价值。

## ⚠️ 局限与未解决问题

摘要未给出具体指标数值与消融，难以判断提升幅度；网页与 YouTube 来源带来版权与噪声标注风险，caption 由模型生成可能引入偏差；未报告推理延迟与训练算力开销；与更大规模闭源模型的对比缺失。

---

<div class="paper-footer"><span>评分：7.8</span><span>原始：7.8</span><a href="/audio-paper-daily/posts/2026-11-10/">← 返回 2026-11-10 速递</a></div>
