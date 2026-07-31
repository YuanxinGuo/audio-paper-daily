---
title: "Teffic-Audio: Tell Fact from Fiction"
date: 2026-07-31T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#语音伪造检测"]
summary: "Teffic-Audio提出基于Conformer的通用语音伪造检测系统，通过多源数据、平衡采样和增强策略，在Speech-DF-Arena上取得1.454%的池化EER，超越现有公开系统。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero">
<div class="hero-score">
<div class="score-num">8.2</div>
<div class="score-stars">★★★★☆</div>
<div class="score-tier">前25%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#语音伪造检测</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#语音伪造检测</span> <span class="tag-pill tag-pill-soft">#Conformer</span> <span class="tag-pill tag-pill-soft">#泛化性</span> <span class="tag-pill tag-pill-soft">#数据增强</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2607.28351</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-07-31</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">🔥 强烈推荐通读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2607.28351" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2607.28351" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>Teffic-Audio提出基于Conformer的通用语音伪造检测系统，通过多源数据、平衡采样和增强策略，在Speech-DF-Arena上取得1.454%的池化EER，超越现有公开系统。
</div>

## 👥 作者与机构

**Wan Lin** ¹ · Li Wang · Jindong Wang · Kunyu Feng · Zhizheng Wu

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合语音安全、伪造检测方向的研究者阅读。建议重点阅读第3节训练策略和第4节实验对比，可先看表1和表2了解整体性能。若关注泛化性，可细读跨数据集测试部分。

## 🌍 研究背景

语音伪造检测面临伪造机制多样（合成、转换、声码器重建、神经编解码重合成）及源语音、环境、信道差异带来的伪影变化，导致系统跨条件泛化困难。现有系统常依赖复杂架构，但泛化性能有限。本文旨在构建一个简单但泛化能力强的检测系统，通过训练策略而非架构复杂度提升鲁棒性。

## 💡 核心创新

1. 采用Conformer编码器+多头注意力统计池化+二分类器，架构简洁
2. 整合多源开源数据，覆盖多种伪造类型
3. 攻击与源平衡采样，缓解数据不平衡
4. 多样音频增强，提升跨条件鲁棒性
5. 在Speech-DF-Arena上取得SOTA，性能-复杂度权衡良好

## 🏗️ 模型架构

输入为语音特征（如log-mel），经Conformer编码器提取帧级表示，随后通过多头注意力统计池化聚合为话语级向量，最后送入二分类器输出真伪概率。Conformer结合卷积与自注意力，有效建模局部与全局依赖。系统参数量未在摘要中提及，但强调与更大系统相比具有性能-复杂度优势。

## 📚 数据集

- Speech-DF-Arena（评估，14个测试集）
- 多源开源数据（训练，具体数据集未列出）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| EER | Speech-DF-Arena（14个测试集） | 现有公开系统（未给出具体值） | **1.454%** | 优于所有公开系统 |

Teffic-Audio在Speech-DF-Arena的14个测试集上取得1.454%的池化EER，超越所有公开系统，并在5个单独测试集上取得最低EER。此外，与更大规模的领先系统相比，Teffic-Audio在性能与复杂度之间取得了良好平衡，表明其高效性。

## 🎯 结论与影响

Teffic-Audio通过简洁的Conformer架构和精心设计的训练策略，实现了通用语音伪造检测的SOTA性能，证明了数据多样性和平衡采样对泛化的重要性。该工作为后续研究提供了强基线，并展示了在资源受限场景下部署的可能性。

## ⚠️ 局限与未解决问题

摘要未提及具体训练数据规模及细节，可能影响可复现性。未报告推理延迟或参数量，性能-复杂度权衡缺乏量化。未进行消融实验验证各训练策略的贡献。跨数据集泛化虽好，但未分析失败案例。

---

<div class="paper-footer"><span>评分：8.2</span><span>原始：8.2</span><a href="/audio-paper-daily/posts/2026-07-31/">← 返回 2026-07-31 速递</a></div>
