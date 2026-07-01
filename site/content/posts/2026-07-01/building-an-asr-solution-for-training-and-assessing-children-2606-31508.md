---
title: "Building an ASR Solution for Training and Assessing Children's Reading"
date: 2026-07-01T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#语音识别"]
summary: "面向班巴拉语儿童阅读评估的开源ASR系统，通过端到端流程构建基准并优化模型，最佳Soloni模型将WER从0.42降至0.22。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#语音识别</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#儿童语音</span> <span class="tag-pill tag-pill-soft">#低资源语言</span> <span class="tag-pill tag-pill-soft">#端到端ASR</span> <span class="tag-pill tag-pill-soft">#阅读评估</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2606.31508</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-07-01</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2606.31508" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2606.31508" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>面向班巴拉语儿童阅读评估的开源ASR系统，通过端到端流程构建基准并优化模型，最佳Soloni模型将WER从0.42降至0.22。
</div>

## 👥 作者与机构

**Yacouba Diarra** ¹ · Nouhoum Souleymane Coulibaly · Mamadou Dembele · Aymane Dembele · Michael Leventhal

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合从事低资源语言ASR、儿童语音识别或教育技术的研究者。建议重点阅读§3（基准构建）和§4（模型微调实验），尤其是表2的WER/CER对比。可关注Soloni与QuartzNet的架构差异及SpecAugment效果。

## 🌍 研究背景

儿童阅读评估的自动化在非洲语言中严重缺乏，班巴拉语作为马里主要语言尚无公开的儿童语音识别系统。现有ASR模型多针对成人语音，儿童发音不标准、数据稀缺导致性能差。本文旨在构建完整的开源系统，涵盖数据采集、基准构建、模型适配和课堂验证，填补该领域空白。

## 💡 核心创新

1. 端到端流程：从田野数据采集到课堂验证的全链路开源系统
2. 构建首个班巴拉语儿童阅读语音公开基准
3. 对比Soloni（Fast-Conformer+TDT/CTC）与QuartzNet架构
4. 发现重复阅读对不同架构的差异化收益
5. 按年龄分层分析识别误差来源

## 🏗️ 模型架构

输入为80维log-mel滤波器组特征。Soloni模型基于Fast-Conformer编码器，结合TDT（Token-and-Duration Transducer）和CTC解码器；QuartzNet为紧凑型卷积ASR架构，使用1D时间通道可分离卷积。模型输出字符序列，通过CTC或TDT损失训练。参数量未明确给出。

## 📚 数据集

- 班巴拉儿童阅读语音数据集（55小时，60名儿童，用于训练和评估）
- 公开基准（从上述数据构建，用于评估）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| WER | 班巴拉儿童阅读基准 | QuartzNet 0.42 | **Soloni 0.22** | -0.20 |
| CER | 班巴拉儿童阅读基准 | QuartzNet 0.15 | **Soloni 0.08** | -0.07 |

Soloni模型在WER和CER上显著优于QuartzNet，分别降低20和7个百分点。重复阅读对QuartzNet提升明显，但对Soloni增益有限。SpecAugment在无增强配置下未带来额外提升。按年龄分析显示10岁以下儿童是主要误差来源。

## 🎯 结论与影响

本文证明了端到端流程在低资源语言儿童阅读评估中的可行性，Soloni模型大幅超越基线。该开源系统为班巴拉语及其他非洲语言的读写评估提供了可复现框架，有望推动教育技术落地。未来可扩展至更多语言和更大规模数据。

## ⚠️ 局限与未解决问题

数据仅来自60名儿童，样本量较小且年龄分布不均；未报告推理延迟或模型参数量；未与多语言预训练模型（如Whisper）对比；课堂验证仅10次试验，统计显著性未明确。

---

<div class="paper-footer"><span>评分：7.2</span><span>原始：7.2</span><a href="/audio-paper-daily/posts/2026-07-01/">← 返回 2026-07-01 速递</a></div>
