---
title: "Audio-to-Score Transcription using Pre-trained Features, Data Augmentation, and the New SheetSage-A2S Dataset"
date: 2026-08-08T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#音乐转录"]
summary: "本文提出基于预训练特征和数据增强的音频到乐谱转录模型，并发布首个流行音乐A2S数据集SheetSage-A2S，在古典和流行音乐上均取得显著提升。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#音乐转录</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#音频到乐谱</span> <span class="tag-pill tag-pill-soft">#预训练特征</span> <span class="tag-pill tag-pill-soft">#数据增强</span> <span class="tag-pill tag-pill-soft">#流行音乐</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2608.06165</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-08-08</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">🔥 强烈推荐通读</span></div>
</div>
</div>

<div class="opensource-banner"><div class="oc-headline"><span class="oc-pulse"></span><span class="oc-title">本论文已开源</span><span class="oc-hint">点击下方卡片直达对应资源</span></div><div class="oc-grid"><a class="oc-chip oc-chip-code" href="https://github.com/Multimodal-Music-Research-Lab/SheetSage2Kern_model" target="_blank" rel="noopener"><span class="oc-icon">💻</span><span class="oc-text"><span class="oc-label">代码仓库</span><span class="oc-sub">Multimodal-Music-Research-Lab/SheetSage2Kern_…</span></span></a></div></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2608.06165" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2608.06165" target="_blank" rel="noopener">📑 PDF</a><a class="rsrc rsrc-code" href="https://github.com/Multimodal-Music-Research-Lab/SheetSage2Kern_model" target="_blank" rel="noopener">💻 代码</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>本文提出基于预训练特征和数据增强的音频到乐谱转录模型，并发布首个流行音乐A2S数据集SheetSage-A2S，在古典和流行音乐上均取得显著提升。
</div>

## 👥 作者与机构

**Eoin Cummins** ¹ · Zhongyi Huang · Alexandre D'Hooge · Zhuoro Mo · Yaolong Ju

**机构**：多模态音乐研究实验室

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合音乐信息检索、音频转录方向的研究者阅读。建议重点阅读第3节（数据集构建）和第4节（模型架构与训练策略），可先看摘要中的结果对比和数据集统计。若关注流行音乐转录，值得通读；若仅关注古典音乐，可略读数据集部分。

## 🌍 研究背景

音频到乐谱转录（A2S）旨在将音频转换为符号乐谱，现有系统主要针对古典音乐，对流行音乐研究不足。此前SOTA方法在古典音乐Quartets集合上SER为15.3%，但泛化能力有限。本文旨在解决A2S在流行音乐上的空白，并提升模型泛化能力，通过引入大规模流行音乐数据集和预训练特征提取器MuQ，结合数据增强来改善性能。

## 💡 核心创新

1. 构建首个流行音乐A2S数据集SheetSage-A2S，含61小时音频和9,468个片段
2. 采用预训练特征提取模型MuQ替代传统手工特征，提升特征质量
3. 应用数据增强策略增强模型泛化能力
4. 在古典音乐上SER从15.3%降至4.98%，显著超越SOTA
5. 为流行音乐A2S提供基准，SER为20.92%

## 🏗️ 模型架构

输入音频经预训练模型MuQ提取特征，然后送入转录网络。网络主干可能采用Transformer或卷积结构，具体细节未在摘要中详述。输出为**kern格式的乐谱编码。模型通过数据增强（如音高偏移、速度变化等）提升鲁棒性。参数量未提及。

## 📚 数据集

- SheetSage-A2S（训练/评估，61小时，9,468个片段，6,066首歌曲）
- Quartets（评估，古典音乐，用于对比SOTA）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| SER | Quartets | 15.3% | **4.98%** | -10.32% |
| SER | SheetSage-A2S | 无 | **20.92%** | N/A |

在古典音乐Quartets集合上，本文模型SER为4.98%，显著优于现有SOTA的15.3%，相对提升约67%。在流行音乐SheetSage-A2S数据集上，模型达到20.92%的SER，作为首个基准。摘要未提供消融实验或跨数据集泛化细节，但数据增强和MuQ特征的作用可能通过消融验证。

## 🎯 结论与影响

本文通过发布大规模流行音乐A2S数据集和采用预训练特征与数据增强，显著提升了音频到乐谱转录的性能，尤其在古典音乐上大幅超越SOTA。该工作填补了流行音乐A2S研究的空白，为后续研究提供了基准和开源资源，有望推动A2S在音乐产业中的应用，如自动乐谱生成和音乐教育。

## ⚠️ 局限与未解决问题

摘要未提及模型在复杂编曲或低质量音频上的表现，也未报告推理效率。数据集仅覆盖流行音乐，可能缺乏多样性。对比实验仅针对古典音乐，未与其他流行音乐方法比较。此外，SER指标可能未全面反映音乐结构准确性。

## 🔗 开源资源

- **代码**：<https://github.com/Multimodal-Music-Research-Lab/SheetSage2Kern_model>

---

<div class="paper-footer"><span>评分：8.2</span><span>原始：8.2</span><a href="/audio-paper-daily/posts/2026-08-08/">← 返回 2026-08-08 速递</a></div>
