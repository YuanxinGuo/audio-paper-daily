---
title: "Dolph2Vec: Self-Supervised Representations of Dolphin Vocalizations"
date: 2026-06-12T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#生物声学"]
summary: "提出Dolph2Vec，首个针对海豚发声的大规模物种专用自监督模型，在哨声分类和检测任务上显著优于通用基线。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#生物声学</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#自监督学习</span> <span class="tag-pill tag-pill-soft">#海豚发声</span> <span class="tag-pill tag-pill-soft">#Wav2Vec2.0</span> <span class="tag-pill tag-pill-soft">#动物交流</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2606.12503</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-06-12</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2606.12503" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2606.12503" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出Dolph2Vec，首个针对海豚发声的大规模物种专用自监督模型，在哨声分类和检测任务上显著优于通用基线。
</div>

## 👥 作者与机构

**Chiara Semenzin** ¹ · Faadil Mustun · Roberto Dessi · Pierre Orhan · Alexis Emanuelli · Yair Lakretz · Gonzalo de Polavieja · German Sumbre

**机构**：巴黎高等师范学院 · 巴黎文理研究大学 · 马克斯·普朗克研究所 · 巴黎综合理工学院

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合生物声学、自监督学习研究者。建议通读，重点看§3数据集构建和§4模型微调方法，以及§5.2嵌入分析部分。可复现其训练流程。

## 🌍 研究背景

自监督学习在生物声学中兴起，但现有模型多追求跨物种泛化，忽略了单个物种交流系统的精细结构。海豚发声研究缺乏大规模标注数据和专用模型。本文收集了五年期五只海豚的纵向录音数据集，并基于Wav2Vec2.0构建首个海豚专用SSL模型Dolph2Vec，旨在捕获海豚哨声的细粒度声学单元。

## 💡 核心创新

1. 首个海豚专用大规模自监督模型Dolph2Vec
2. 五年期五只海豚纵向录音数据集
3. 利用Wav2Vec2.0量化器发现可解释的声学单元
4. 在哨声分类和检测任务上显著超越通用基线

## 🏗️ 模型架构

输入为原始波形，经特征编码器提取潜表示，然后送入Transformer上下文网络，中间使用量化模块（Gumbel-Softmax）将连续表示离散化为codebook条目。模型基于Wav2Vec2.0架构，参数量约95M。输出为上下文表示和量化索引，用于下游任务。

## 📚 数据集

- Dolphin Vocalization Dataset（五年期五只海豚纵向录音，训练/评估）
- 哨声分类任务（标注哨声类别，评估）
- 哨声检测任务（标注哨声出现与否，评估）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| 哨声分类准确率 | 海豚哨声数据集 | Wav2Vec2.0通用模型 72.3% | **Dolph2Vec 85.1%** | +12.8% |
| 哨声检测F1 | 海豚哨声数据集 | Wav2Vec2.0通用模型 0.68 | **Dolph2Vec 0.82** | +0.14 |

Dolph2Vec在哨声分类任务上达到85.1%准确率，比通用Wav2Vec2.0基线提升12.8%；哨声检测F1达0.82，提升0.14。消融实验表明，物种专用预训练优于跨物种预训练。嵌入可视化显示codebook捕获了与哨声类别对应的声学单元，甚至可能发现子哨声结构。

## 🎯 结论与影响

Dolph2Vec证明物种专用自监督模型能有效捕获海豚发声的精细结构，为动物交流研究提供新工具。该方法可推广至其他物种，推动生物声学从通用模型向专用模型转变。对海豚保护与行为研究有潜在应用价值。

## ⚠️ 局限与未解决问题

数据集仅包含五只海豚，物种内多样性有限；未与更多生物声学SSL模型（如BirdNET）对比；未报告推理速度或模型效率；哨声分类任务标注可能不够精细；未在真实噪声环境下测试鲁棒性。

---

<div class="paper-footer"><span>评分：8.2</span><span>原始：8.2</span><a href="/audio-paper-daily/posts/2026-06-12/">← 返回 2026-06-12 速递</a></div>
